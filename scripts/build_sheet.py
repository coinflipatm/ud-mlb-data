#!/usr/bin/env python3
"""
build_sheet.py — Underdog MLB Battle Royale pre-draft sheet (Rulebook v8, Rule 16 / Appendix A).

Runs the whole pre-slate sequence from data on disk, BEFORE the lobby opens:
  1. park factors (runs index + P20 index by venue, shrunk)
  2. starter K/9, HR/9, ERA, prior GS, win prob -> arm bucket, legal flag
  3. park x arm multiplier per team
  4. team run distributions at tonight's venue (home/road specific) + L15
  5. bat board: mean UD (shrunk) x multiplier; P20, max, L15, modal slot, start rate
  6. legal-arm count vs drafters
  7. Q/O/low-start-rate flags (as probabilities, not facts)
  8. Game A / Game B / ace game + 36-deep queue grouped by team (Appendix A)

Usage:
  python build_sheet.py --date 2026-08-30 [--odds odds.csv] [--games CHC@CIN,SEA@HOU]
                        [--drafters 6] [--rounds 6] [--blocked blocked.txt] [--out outdir]
  odds.csv columns: away,home,away_ml,home_ml,total   (American odds, e.g. -135, +115, 9.5)

Data expected at:  ./ud-mlb-data-main/data/{boxscores,schedule}/YYYY-MM-DD.csv
                   ./mlb-playoff-predictor-2026-main/data/{pitcher_logs,probables,predictions_log}.csv
Every number printed carries its source column (Rule 14). Nothing is projected; everything is a
season-to-date rate at the moment the script ran.
"""
import argparse, glob, math, os, re, sys
from collections import Counter
import numpy as np
import pandas as pd

LEAGUE_BAT_MEAN_PRIOR = None   # filled from data
SHRINK_K_BAT = 40              # starts of prior weight for a bat's mean (report 3.1 used 40+ starts)
SHRINK_K_PARK = 60             # team-games of prior weight for park indexes
SHRINK_IP_ARM = 40.0           # innings of prior weight for an arm's HR/9 and K/9

# ----------------------------------------------------------------------------- helpers
def american_to_prob(ml):
    ml = float(ml)
    return 100.0 / (ml + 100.0) if ml > 0 else -ml / (-ml + 100.0)

def novig(p_a, p_b):
    s = p_a + p_b
    return p_a / s, p_b / s

def implied_totals(p_home, total):
    """Split a game total into team totals so that a Poisson race gives P(home wins)=p_home
    (ties resolved by conditioning on no tie). Returns (home_total, away_total)."""
    from math import exp, factorial
    def pois(lam, n=30):
        return np.array([exp(-lam) * lam**k / factorial(k) for k in range(n)])
    best = None
    for h in np.arange(1.0, total - 0.99, 0.01):
        a = total - h
        ph, pa = pois(h), pois(a)
        M = np.outer(ph, pa)
        p_h_win = np.tril(M, -1).sum(); p_tie = np.trace(M)
        p = p_h_win / (1 - p_tie)
        err = abs(p - p_home)
        if best is None or err < best[0]:
            best = (err, h, a)
    return round(best[1], 2), round(best[2], 2)

def tier(implied):
    if implied is None or (isinstance(implied, float) and math.isnan(implied)): return "?"
    return "A" if implied >= 4.75 else ("B" if implied >= 4.25 else "C")

def bump(t):
    return {"B": "A", "C": "B", "A": "A", "?": "?"}[t]

def fix_ip(s):
    """pitcher_logs IP: handle both true-decimal (6.667) and baseball-decimal (6.2) encodings."""
    s = pd.to_numeric(s, errors="coerce")
    frac = (s - np.floor(s)).round(2)
    if frac.isin([0.1, 0.2]).sum() > frac.isin([0.33, 0.67]).sum():
        return np.floor(s) + (s - np.floor(s)) * 10 / 3
    return s

def norm(name):
    import unicodedata
    n = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode()
    n = re.sub(r"\s+(Jr\.?|Sr\.?|II|III|IV)$", "", n.strip(), flags=re.I)
    return n.lower()

# ----------------------------------------------------------------------------- load
def load(args):
    d = args.date
    UD, PR = args.ud_dir, args.pred_dir
    bx_files = [f for f in sorted(glob.glob(f"{UD}/data/boxscores/*.csv")) if os.path.basename(f)[:10] < d]
    if not bx_files: sys.exit("no boxscores before " + d)
    bx = pd.concat([pd.read_csv(f, dtype=str) for f in bx_files], ignore_index=True)
    for c in ["ud_pts","team_runs","opp_runs","pa","h","2b","3b","hr","r","rbi","bb","hbp","sb","k","ip","er","win","qs","bat_slot"]:
        bx[c] = pd.to_numeric(bx[c], errors="coerce")
    bx["player_id"] = bx.player_id.astype(str).str.replace(r"\.0$", "", regex=True)
    bx["is_bat_start"] = bx.bat_starter.astype(str).str.lower().isin(["1","true"])
    bx["is_sp"] = bx.started.astype(str).str.lower().isin(["1","true"])
    bx["is_home"] = bx.home.astype(str).str.lower().isin(["1","true"])
    sched_path = f"{UD}/data/schedule/{d}.csv"
    sched = pd.read_csv(sched_path, dtype=str) if os.path.exists(sched_path) else None
    pl = pd.read_csv(f"{PR}/data/pitcher_logs.csv", dtype=str)
    pl["pitcher_id"] = pl.pitcher_id.astype(str).str.replace(r"\.0$", "", regex=True)
    for c in ["gs","er","bb","so","hr","hbp","bf"]: pl[c] = pd.to_numeric(pl[c], errors="coerce")
    pl["ip"] = fix_ip(pl.ip)
    pl = pl[pl.date < d]
    pr = pd.read_csv(f"{PR}/data/probables.csv", dtype=str)
    for c in ["home_sp_id","away_sp_id"]: pr[c] = pr[c].astype(str).str.replace(r"\.0$", "", regex=True).replace("nan", np.nan)
    pdl = pd.read_csv(f"{PR}/data/predictions_log.csv", dtype=str)
    return bx, sched, pl, pr, pdl

# ----------------------------------------------------------------------------- park + arm indexes
def park_table(bx):
    H = bx[(bx.kind=="H") & bx.is_bat_start]
    league_p20 = (H.ud_pts >= 20).mean()
    tg = bx[bx.kind=="H"].groupby(["date","game_pk","team","is_home"]).agg(runs=("team_runs","first"), opp=("opp","first")).reset_index()
    league_runs = tg.runs.mean()
    tg["venue"] = np.where(tg.is_home, tg.team, tg.opp)
    H = H.assign(venue=np.where(H.is_home, H.team, H.opp))
    rows = []
    for v, g in tg.groupby("venue"):
        n = len(g); hv = H[H.venue==v]
        r_idx = ((g.runs.mean()/league_runs)*n + 1.0*SHRINK_K_PARK)/(n+SHRINK_K_PARK)
        p_idx = (((hv.ud_pts>=20).mean()/league_p20)*n + 1.0*SHRINK_K_PARK)/(n+SHRINK_K_PARK)
        rows.append(dict(venue=v, team_games=n, runs_idx=round(r_idx,3), p20_idx=round(p_idx,3), raw_p20=round((hv.ud_pts>=20).mean(),4)))
    return pd.DataFrame(rows).set_index("venue"), league_p20, league_runs

def arm_stats(pl, pid):
    g = pl[(pl.pitcher_id==pid)]
    g26 = g[g.season=="2026"]
    ip = g26.ip.sum(); gs = int(g26.gs.sum())
    if ip <= 0: return dict(gs26=0, ip26=0.0, k9=np.nan, bb9=np.nan, hr9=np.nan, era=np.nan, kbb=np.nan, ip_per_gs=np.nan, k9_shr=np.nan, hr9_shr=np.nan)
    k9 = 9*g26.so.sum()/ip; bb9 = 9*g26.bb.sum()/ip; hr9 = 9*g26.hr.sum()/ip; era = 9*g26.er.sum()/ip
    return dict(gs26=gs, ip26=round(ip,1), k9=round(k9,2), bb9=round(bb9,2), hr9=round(hr9,2), era=round(era,2),
                kbb=round(g26.so.sum()/max(g26.bb.sum(),1),2), ip_per_gs=round(ip/max(gs,1),2), _ip=ip, _k=g26.so.sum(), _hr=g26.hr.sum())

def league_arm_rates(pl):
    p = pl[(pl.season=="2026")&(pl.gs==1)]
    ip = p.ip.sum()
    return 9*p.so.sum()/ip, 9*p.hr.sum()/ip

def arm_p20_index(bx, pl, pr):
    """Empirical P20 of batter-starts by opposing-SP HR/9 tercile (2026). Returns bucket edges + index per bucket."""
    H = bx[(bx.kind=="H") & bx.is_bat_start & (bx.date >= "2026-01-01")].copy()
    m = H.merge(pr[pr.season=="2026"][["game_id","home_sp_id","away_sp_id"]], left_on="game_pk", right_on="game_id", how="left")
    m["opp_sp"] = np.where(m.is_home, m.away_sp_id, m.home_sp_id)
    p26 = pl[(pl.season=="2026")]
    agg = p26.groupby("pitcher_id").agg(ip=("ip","sum"), hr=("hr","sum"), so=("so","sum"))
    lg_k9, lg_hr9 = league_arm_rates(pl)
    agg["hr9_shr"] = (9*agg.hr + lg_hr9*SHRINK_IP_ARM) / (agg.ip + SHRINK_IP_ARM)
    qual = agg[agg.ip >= 30]
    edges = qual.hr9_shr.quantile([1/3, 2/3]).values
    m = m.merge(agg[["hr9_shr"]], left_on="opp_sp", right_index=True, how="left")
    m["bucket"] = pd.cut(m.hr9_shr, bins=[-1, edges[0], edges[1], 99], labels=["LOW_HR","MID_HR","HIGH_HR"])
    lg = (m.ud_pts>=20).mean()
    idx = m.groupby("bucket", observed=True).ud_pts.apply(lambda s: (s>=20).mean()/lg).round(3).to_dict()
    n = m.groupby("bucket", observed=True).size().to_dict()
    return edges, idx, n, lg_k9, lg_hr9

def bucket_of(hr9_shr, edges):
    if hr9_shr is None or np.isnan(hr9_shr): return "MID_HR"
    return "LOW_HR" if hr9_shr <= edges[0] else ("MID_HR" if hr9_shr <= edges[1] else "HIGH_HR")

# ----------------------------------------------------------------------------- team run splits
def team_split(bx, team, at_home, n_recent=15):
    tg = bx[(bx.kind=="H")&(bx.team==team)].groupby(["date","game_pk"]).agg(runs=("team_runs","first"), is_home=("is_home","first")).reset_index().sort_values("date")
    s = tg[tg.is_home==at_home].runs
    l15 = tg.tail(n_recent).runs
    return dict(n=len(s), mean=round(s.mean(),2) if len(s) else np.nan, p5=round((s>=5).mean(),3) if len(s) else np.nan,
                p9=round((s>=9).mean(),3) if len(s) else np.nan, p12=round((s>=12).mean(),3) if len(s) else np.nan,
                l15_mean=round(l15.mean(),2), season_mean=round(tg.runs.mean(),2))

# ----------------------------------------------------------------------------- bats
def bat_profile(bx, pid, team):
    g = bx[(bx.kind=="H")&(bx.player_id==pid)].sort_values("date")
    st = g[g.is_bat_start]
    n = len(st)
    lg = LEAGUE_BAT_MEAN_PRIOR
    mean = st.ud_pts.mean() if n else np.nan
    shr = (st.ud_pts.sum() + lg*SHRINK_K_BAT)/(n + SHRINK_K_BAT) if n else lg
    slots = st.bat_slot.dropna().astype(int).tolist()
    modal = Counter(slots[-10:]).most_common(1)[0][0] if slots else np.nan
    # start rate over the team's last 15 games
    team_games = bx[(bx.kind=="H")&(bx.team==team)].groupby(["date","game_pk"]).size().reset_index().sort_values("date").tail(15)
    keys = set(zip(team_games.date, team_games.game_pk))
    started_recent = sum(1 for _, r in st.iterrows() if (r.date, r.game_pk) in keys)
    pos = Counter(g[g.is_bat_start].pos.tolist()).most_common(1)[0][0] if n else ""
    hr_rate = st.hr.sum()/n if n else 0
    return dict(starts=n, mean_ud=round(mean,2) if n else np.nan, mean_shr=round(shr,2), p20=round((st.ud_pts>=20).mean(),3) if n else np.nan,
                max_ud=st.ud_pts.max() if n else np.nan, l15_mean=round(st.tail(15).ud_pts.mean(),2) if n else np.nan,
                modal_slot=modal, start_rate15=round(started_recent/max(len(keys),1),2), pos=pos, hr_per_start=round(hr_rate,3),
                zeros_rate=round((st.ud_pts<=0).mean(),3) if n else np.nan)

IF_POS = {"C","1B","2B","3B","SS"}; OF_POS = {"LF","CF","RF","OF"}
def pos_class(p):
    return "IF" if p in IF_POS else ("OF" if p in OF_POS else "DH?")

def parse_lineup(s):
    out = []
    if not isinstance(s, str) or not s.strip(): return out
    for part in s.split("|"):
        m = re.match(r"\s*(\d+):(.+?)\((\w+)\)\s*$", part)
        if m: out.append((int(m.group(1)), m.group(2).strip(), m.group(3)))
    return out

def modal_lineup(bx, team):
    """If no lineup is posted: players by start rate over last 10 team games, ordered by modal slot."""
    g = bx[(bx.kind=="H")&(bx.team==team)&bx.is_bat_start].sort_values("date")
    last10 = g.groupby(["date","game_pk"]).size().reset_index().tail(10)
    keys = set(zip(last10.date, last10.game_pk))
    gg = g[[ (d,p) in keys for d,p in zip(g.date, g.game_pk)]]
    rows = []
    for pid, h in gg.groupby("player_id"):
        rate = len(h)/max(len(keys),1)
        if rate >= 0.5:
            rows.append((int(Counter(h.bat_slot.dropna().astype(int)).most_common(1)[0][0]), h.player.iloc[-1], h.pos.iloc[-1], pid, rate))
    rows.sort()
    return rows

# ----------------------------------------------------------------------------- main
def main():
    global LEAGUE_BAT_MEAN_PRIOR
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True); ap.add_argument("--odds"); ap.add_argument("--games")
    ap.add_argument("--drafters", type=int, default=6); ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--blocked"); ap.add_argument("--out", default="out"); ap.add_argument("--exclude_pk", help="comma-separated game_pk to drop (e.g. DH game not in contest)")
    ap.add_argument("--ud_dir", default="ud-mlb-data-main", help="ud-mlb-data checkout (use . when running inside the repo)")
    ap.add_argument("--pred_dir", default="mlb-playoff-predictor-2026-main", help="mlb-playoff-predictor-2026 checkout")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    bx, sched, pl, pr, pdl = load(args)
    H_all = bx[(bx.kind=="H") & bx.is_bat_start]
    LEAGUE_BAT_MEAN_PRIOR = H_all.ud_pts.mean()
    league_p20_all = (H_all.ud_pts>=20).mean()
    parks, league_p20, league_runs = park_table(bx)
    edges, arm_idx, arm_n, lg_k9, lg_hr9 = arm_p20_index(bx, pl, pr)
    blocked = set()
    if args.blocked and os.path.exists(args.blocked):
        blocked = {norm(l) for l in open(args.blocked) if l.strip()}

    if sched is None:
        print(f"!! No schedule file for {args.date} ({UD}/data/schedule/{args.date}.csv). Trigger the pull-mlb workflow, re-download, re-run.")
        print(f"   Park table and league baselines still written to {args.out}/.")
        parks.to_csv(f"{args.out}/parks_{args.date}.csv"); return
    sched["is_home"] = sched.home.astype(str).str.lower().isin(["1","true"])
    if args.games:
        keep = set()
        for gm in args.games.split(","):
            a, h = gm.upper().split("@"); keep |= {a, h}
        sched = sched[sched.team.isin(keep)]
    if args.exclude_pk:
        sched = sched[~sched.game_pk.isin(args.exclude_pk.split(","))]
    dh = sched.groupby(["team","opp"]).size(); dh = dh[dh > 1]
    if len(dh): print(f"!! Doubleheader(s) on the schedule: {sorted(set(dh.index.get_level_values(0)))} — both games are on this sheet; use --exclude_pk to drop the one not in the contest.")

    # ---------------- odds
    odds = None
    if args.odds and os.path.exists(args.odds):
        odds = pd.read_csv(args.odds, dtype=str)
        odds["away"] = odds.away.str.upper(); odds["home"] = odds.home.str.upper()

    # ---------------- pitchers + teams
    prow, trow = [], []
    for _, g in sched.iterrows():
        team, opp, home = g.team, g.opp, g.is_home
        venue = team if home else opp
        sp_id = str(g.prob_sp_id).replace(".0","") if isinstance(g.prob_sp_id, str) else None
        osp_id = str(g.opp_sp_id).replace(".0","") if isinstance(g.opp_sp_id, str) else None
        # win prob: market first, else model
        wp, src, implied, total = np.nan, "NONE", np.nan, np.nan
        if odds is not None:
            o = odds[(odds.away==(opp if home else team)) & (odds.home==(team if home else opp))]
            if len(o):
                o = o.iloc[0]
                pa, ph = novig(american_to_prob(o.away_ml), american_to_prob(o.home_ml))
                total = float(o.total); ht, at = implied_totals(ph, total)
                wp = ph if home else pa; implied = ht if home else at; src = "MARKET"
        if np.isnan(wp):
            m = pdl[(pdl.game_id==g.game_pk)]
            if len(m) and pd.notna(m.iloc[-1].p_home_ens):
                ph = float(m.iloc[-1].p_home_ens); wp = ph if home else 1-ph; src = "MODEL(p_home_ens)"
        a = arm_stats(pl, sp_id) if sp_id else arm_stats(pl, "x")
        oa = arm_stats(pl, osp_id) if osp_id else arm_stats(pl, "x")
        # shrunk rates for bucket
        def shr(st):
            if not st.get("_ip"): return np.nan, np.nan
            return (9*st["_k"] + lg_k9*SHRINK_IP_ARM)/(st["_ip"]+SHRINK_IP_ARM), (9*st["_hr"] + lg_hr9*SHRINK_IP_ARM)/(st["_ip"]+SHRINK_IP_ARM)
        k9s, hr9s = shr(a); ok9s, ohr9s = shr(oa)
        # SP UD distribution from boxscores
        sp_hist = bx[(bx.kind=="P")&bx.is_sp&(bx.player_id==sp_id)].ud_pts if sp_id else pd.Series(dtype=float)
        coors = (venue == "COL")
        legal = (src != "NONE") and (wp >= 0.50) and (not coors) and (sp_id is not None)
        prow.append(dict(pitcher=g.prob_sp, team=team, opp=opp, home="H" if home else "A", win_prob=round(wp,3) if pd.notna(wp) else np.nan, wp_src=src,
                         k9=a["k9"], k9_shr=round(k9s,2) if pd.notna(k9s) else np.nan, kbb=a["kbb"], hr9=a["hr9"], era=a["era"], gs26=a["gs26"], ip_per_gs=a["ip_per_gs"],
                         ud_mean=round(sp_hist.mean(),2) if len(sp_hist) else np.nan, ud_p20=round((sp_hist>=20).mean(),3) if len(sp_hist) else np.nan,
                         ud_max=sp_hist.max() if len(sp_hist) else np.nan, ud_min=sp_hist.min() if len(sp_hist) else np.nan, ud_n=len(sp_hist),
                         spot_starter=(a["gs26"]<=2), coors=coors, legal=legal, game_pk=g.game_pk, venue=venue))
        split = team_split(bx, team, home)
        pk = parks.loc[venue] if venue in parks.index else None
        bucket = bucket_of(ohr9s, edges)
        park_idx = float(pk.p20_idx) if pk is not None else 1.0
        mult = round(park_idx * float(arm_idx.get(bucket, 1.0)), 3)
        t = tier(implied) if src=="MARKET" else "?"
        t_adj = bump(t) if (oa["gs26"]<=2) else t
        trow.append(dict(team=team, opp=opp, home="H" if home else "A", venue=venue, implied=implied, total=total, win_prob=round(wp,3) if pd.notna(wp) else np.nan, src=src,
                         tier=t, tier_adj=t_adj, opp_sp=g.opp_sp, opp_k9=oa["k9"], opp_hr9=oa["hr9"], opp_hr9_shr=round(ohr9s,2) if pd.notna(ohr9s) else np.nan,
                         opp_era=oa["era"], opp_gs26=oa["gs26"], spot_starter=(oa["gs26"]<=2), arm_bucket=bucket,
                         park_runs_idx=float(pk.runs_idx) if pk is not None else np.nan, park_p20_idx=round(park_idx,3), arm_idx=arm_idx.get(bucket, np.nan), mult=mult,
                         split_n=split["n"], split_mean=split["mean"], split_p5=split["p5"], split_p9=split["p9"], split_p12=split["p12"], l15_mean=split["l15_mean"], season_mean=split["season_mean"],
                         lineup_posted=isinstance(g.lineup, str) and len(g.lineup)>10, game_pk=g.game_pk, lineup=g.lineup))
    P = pd.DataFrame(prow); T = pd.DataFrame(trow)
    # stack score: what the sheet ranks games on (market implied when available; else venue-split mean) x multiplier, spot-starter bump
    T["run_est"] = np.where(T.src=="MARKET", T.implied, T.split_mean)
    T["stack_score"] = (T.run_est * T.mult * np.where(T.spot_starter, 1.07, 1.0)).round(2)
    # Game order is tier-first (Rule 16 / Appendix A): the multiplier breaks ties inside a tier, it never outranks the tier (O-14).
    T["tier_rank"] = T.tier_adj.map({"A":0,"B":1,"C":2,"?":3})
    T = T.sort_values(["tier_rank","stack_score"], ascending=[True,False]).reset_index(drop=True)

    # ---------------- bats
    brow = []
    for _, t in T.iterrows():
        lu = parse_lineup(t.lineup) if t.lineup_posted else []
        src = "POSTED"
        if not lu:
            src = "MODAL(last10)"; lu = [(s, nm, ps, pid) for s, nm, ps, pid, rate in modal_lineup(bx, t.team)]
        for entry in lu:
            slot, name, pos = entry[0], entry[1], entry[2]
            pid = entry[3] if len(entry) > 3 else None
            if pid is None:
                cand = bx[(bx.kind=="H")&(bx.team==t.team)&(bx.player.map(norm)==norm(name))].player_id
                pid = cand.iloc[-1] if len(cand) else None
            prof = bat_profile(bx, pid, t.team) if pid else dict(starts=0, mean_ud=np.nan, mean_shr=LEAGUE_BAT_MEAN_PRIOR, p20=np.nan, max_ud=np.nan, l15_mean=np.nan, modal_slot=np.nan, start_rate15=0, pos=pos, hr_per_start=0, zeros_rate=np.nan)
            slot_group = 1 if 3 <= slot <= 6 else (2 if slot <= 2 else 3)
            brow.append(dict(player=name, team=t.team, tier=t.tier_adj, slot=slot, slot_group=slot_group, pos=pos, pos_class=pos_class(pos), lineup_src=src,
                             adj_mean=round(prof["mean_shr"]*t.mult,2), mean_shr=prof["mean_shr"], mean_ud=prof["mean_ud"], l15_mean=prof["l15_mean"], p20=prof["p20"],
                             adj_p20=round(prof["p20"]*t.mult,3) if pd.notna(prof["p20"]) else np.nan, max_ud=prof["max_ud"], starts=prof["starts"], modal_slot=prof["modal_slot"],
                             start_rate15=prof["start_rate15"], hr_per_start=prof["hr_per_start"], zeros_rate=prof["zeros_rate"], mult=t.mult, stack_score=t.stack_score,
                             blocked=(norm(name) in blocked), pid=pid))
    B = pd.DataFrame(brow)
    # elite-power exception for B1/B2: top-2 HR/start on his own team
    B["elite_power"] = False
    for tm, g in B.groupby("team"):
        top2 = g.sort_values("hr_per_start", ascending=False).head(2).index
        B.loc[top2, "elite_power"] = True
    B["law_slot_rank"] = np.where(B.slot_group==1, 1, np.where((B.slot_group==2)&B.elite_power, 2, np.where(B.slot_group==2, 3, 4)))
    tier_rank = {"A":0, "B":1, "C":2, "?":3}
    B["tier_rank"] = B.tier.map(tier_rank)
    B["model_rank"] = B.adj_mean.rank(ascending=False, method="first").astype(int)   # pure adjusted-mean order (open question 3)
    B = B.sort_values(["tier_rank","stack_score","law_slot_rank","adj_mean"], ascending=[True,False,True,False]).reset_index(drop=True)
    B["law_rank"] = np.arange(1, len(B)+1)

    # ---------------- game A / B / ace
    A_team = T.iloc[0].team; A_game = T.iloc[0].game_pk
    B_cands = T[T.game_pk != A_game]; B_team = B_cands.iloc[0].team if len(B_cands) else None; B_game = B_cands.iloc[0].game_pk if len(B_cands) else None
    legal = P[P.legal].copy()
    legal = legal[~legal.game_pk.isin([A_game, B_game])]
    legal = legal.sort_values(["k9_shr","win_prob"], ascending=[False,False])
    ace = legal.iloc[0] if len(legal) else None
    all_legal = P[P.legal].sort_values(["k9_shr","win_prob"], ascending=[False,False])
    r1_exception = False
    if len(all_legal) >= 2 and all_legal.iloc[0].k9_shr - all_legal.iloc[1].k9_shr >= 1.0: r1_exception = True
    n_legal = int(P.legal.sum())

    # ---------------- queue (Appendix A): A bats (law order), B bats, ace, backup arms, rest by tier
    depth = args.drafters * args.rounds
    q = []
    def add_team(tm, cap):
        for _, r in B[(B.team==tm)&(~B.blocked)].sort_values(["law_slot_rank","adj_mean"], ascending=[True,False]).head(cap).iterrows():
            q.append(("BAT", r.player, tm, f"B{r.slot}", r.adj_mean, r.max_ud, r.start_rate15))
    add_team(A_team, 6)
    if B_team: add_team(B_team, 4)
    if ace is not None: q.append(("P", ace.pitcher, ace.team, f"wp{ace.win_prob}", ace.k9, ace.ud_max, ""))
    for _, r in legal.iloc[1:3].iterrows(): q.append(("P-backup", r.pitcher, r.team, f"wp{r.win_prob}", r.k9, r.ud_max, ""))
    used = {x[1] for x in q}
    for _, r in B[~B.blocked].iterrows():
        if len(q) >= depth: break
        if r.player in used or r.team in (A_team, B_team): continue
        q.append(("BAT", r.player, r.team, f"B{r.slot}", r.adj_mean, r.max_ud, r.start_rate15)); used.add(r.player)
    for _, r in B[(~B.blocked)&(B.team.isin([A_team, B_team]))].iterrows():   # deeper A/B bats last, as swap-pool
        if len(q) >= depth: break
        if r.player in used: continue
        q.append(("BAT", r.player, r.team, f"B{r.slot}", r.adj_mean, r.max_ud, r.start_rate15)); used.add(r.player)
    Q = pd.DataFrame(q, columns=["type","name","team","slot_or_wp","adj_mean_or_k9","max","start_rate15"]); Q.index = Q.index + 1

    # ---------------- write
    P.to_csv(f"{args.out}/pitchers_{args.date}.csv", index=False); T.drop(columns=["lineup"]).to_csv(f"{args.out}/teams_{args.date}.csv", index=False)
    B.to_csv(f"{args.out}/bats_{args.date}.csv", index=False); Q.to_csv(f"{args.out}/queue_{args.date}.csv"); parks.to_csv(f"{args.out}/parks_{args.date}.csv")
    pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 400)
    L = []
    L.append(f"# PRE-DRAFT SHEET {args.date}  (built from boxscores through {bx.date.max()}, pitcher_logs through {pl.date.max()})")
    L.append(f"League baselines (source: ud-mlb-data boxscores): bat-start mean {LEAGUE_BAT_MEAN_PRIOR:.2f}, P20 {league_p20_all:.3f}; team-game mean runs {league_runs:.2f}. "
             f"Arm buckets by shrunk HR/9 terciles {edges.round(2).tolist()} -> P20 index {arm_idx} (n {arm_n}).")
    L.append(f"\n## PITCHERS  (legal = win prob >= .50, not Coors, probable listed)  legal arms: {n_legal} vs {args.drafters} drafters"
             + ("  -> SCARCE: arm moves up (R2-R3)" if n_legal < args.drafters else "  -> abundant: arm waits (R3-R4)"))
    if r1_exception: L.append(f"** RULE 1 EXCEPTION MET: {all_legal.iloc[0].pitcher} k9_shr {all_legal.iloc[0].k9_shr} is >= 1.0 above next legal arm ({all_legal.iloc[1].pitcher} {all_legal.iloc[1].k9_shr}) — R1 pick from any slot.")
    L.append(P.sort_values(["legal","k9_shr"], ascending=[False,False])[["pitcher","team","opp","home","win_prob","wp_src","k9","k9_shr","kbb","hr9","era","gs26","ip_per_gs","ud_mean","ud_p20","ud_max","ud_min","ud_n","spot_starter","coors","legal"]].to_string(index=False))
    L.append(f"\n## TEAMS  (sorted tier-first, then stack_score = run_est x park*arm mult x spot bump; tier per Rule 16; tier_adj = spot-starter bump)")
    L.append(T[["team","opp","home","venue","implied","total","win_prob","src","tier","tier_adj","opp_sp","opp_k9","opp_hr9","opp_gs26","spot_starter","arm_bucket","park_runs_idx","park_p20_idx","arm_idx","mult","split_n","split_mean","split_p5","split_p9","split_p12","l15_mean","stack_score","lineup_posted"]].to_string(index=False))
    L.append(f"\n## GAME A = {A_team} (game {A_game})   GAME B = {B_team} (game {B_game})   ACE = {ace.pitcher if ace is not None else 'NONE LEGAL outside A/B'}"
             + (f" ({ace.team}, wp {ace.win_prob} {ace.wp_src}, k9 {ace.k9}, ud_mean {ace.ud_mean}, max {ace.ud_max})" if ace is not None else ""))
    L.append("   Override A/B by hand if the market disagrees with the sheet — but do it BEFORE the lobby, never on the clock.")
    L.append(f"\n## BATS  (law_rank = Rule 8/16 order: tier, then stack_score, then slots 3-6 > B1-2 elite power > B1-2 > 7-9, then adj_mean.  model_rank = pure adj_mean, logged for open question 3)")
    L.append("   adj_mean = shrunk season mean UD x park*arm mult.  start_rate15 < 0.8 = sit risk (probability, not a fact).  starts < 40 = thin sample.")
    L.append(B[["law_rank","model_rank","player","team","tier","slot","pos","lineup_src","adj_mean","mean_ud","l15_mean","p20","adj_p20","max_ud","starts","modal_slot","start_rate15","zeros_rate","elite_power","blocked"]].to_string(index=False))
    L.append(f"\n## QUEUE ({depth} deep, Appendix A: A bats in law order -> B bats -> ace -> backup arms -> other tiers; blocked names removed)")
    L.append(Q.to_string())
    ab = B[B.team.isin([A_team, B_team]) & ~B.blocked].head(10)
    L.append(f"\n## CHECKS: A+B top-10 position mix: {ab.pos_class.value_counts().to_dict()} (roster needs 2 IF + 2 OF + flex; DH? = check UD eligibility)")
    thin = B[(B.starts < 40) & (B.team.isin([A_team, B_team]))].player.tolist(); sit = B[(B.start_rate15 < 0.8) & (B.team.isin([A_team, B_team]))].player.tolist()
    L.append(f"   thin-sample A/B bats: {thin}\n   sit-risk A/B bats (start_rate15<0.8): {sit}")
    L.append("   Not on this sheet: Underdog tags (green check / B# / Q / O / no-ADP). Tags come from the user's screenshot and override everything here (Rule 12).")
    txt = "\n".join(L)
    open(f"{args.out}/sheet_{args.date}.md", "w").write(txt); print(txt)

if __name__ == "__main__":
    main()
