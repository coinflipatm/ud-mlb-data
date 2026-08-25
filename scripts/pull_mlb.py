#!/usr/bin/env python3
"""Pull MLB box scores (scored with Underdog DAILY scoring) plus today's probables/lineups
from the MLB Stats API and write CSVs under data/. Runs inside GitHub Actions.

Usage:  python scripts/pull_mlb.py                 -> box scores for yesterday (ET), schedule for today
        python scripts/pull_mlb.py 2026-08-24      -> box scores for that date (schedule for today)
        python scripts/pull_mlb.py 2026-08-20,2026-08-21,2026-08-22   -> several dates
        python scripts/pull_mlb.py 2026-04-01:2026-04-30              -> a date range
        python scripts/pull_mlb.py season                             -> whole current season to yesterday
Dates whose CSV already exists are skipped (set FORCE=1 to re-pull).
"""
import csv, json, os, sys, time, urllib.request
from datetime import datetime, timedelta, timezone

API = "https://statsapi.mlb.com/api/v1"
ET = timezone(timedelta(hours=-4))          # EDT; fine for the season

# ---- Underdog MLB Battle Royale (DAILY) scoring ----------------------------
HIT = {"single": 3, "double": 6, "triple": 8, "hr": 10, "bb": 3, "hbp": 3, "run": 2, "rbi": 2, "sb": 4}
PIT = {"win": 2, "qs": 3, "k": 1, "ip": 1, "er": -1}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ud-mlb-data/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def ipf(ip):                                 # "6.1" -> 6.333
    s = str(ip or "0.0"); whole, _, thirds = s.partition(".")
    return int(whole or 0) + int(thirds or 0) / 3.0

def hitter_pts(b):
    g = lambda k: int(b.get(k, 0) or 0)
    singles = g("hits") - g("doubles") - g("triples") - g("homeRuns")
    return (HIT["single"] * singles + HIT["double"] * g("doubles") + HIT["triple"] * g("triples")
            + HIT["hr"] * g("homeRuns") + HIT["bb"] * g("baseOnBalls") + HIT["hbp"] * g("hitByPitch")
            + HIT["run"] * g("runs") + HIT["rbi"] * g("rbi") + HIT["sb"] * g("stolenBases"))

def pitcher_pts(p, won):
    ip = ipf(p.get("inningsPitched")); er = int(p.get("earnedRuns", 0) or 0)
    qs = 1 if (ip >= 6 and er <= 3) else 0
    pts = PIT["ip"] * ip + PIT["k"] * int(p.get("strikeOuts", 0) or 0) + PIT["win"] * won + PIT["qs"] * qs + PIT["er"] * er
    return round(pts, 2), round(ip, 2), qs

def pull_boxscores(date):
    sched = get(f"{API}/schedule?sportId=1&date={date}&gameType=R")
    games = [g for d in sched.get("dates", []) for g in d.get("games", [])]
    rows = []
    for g in games:
        pk = g["gamePk"]
        time.sleep(0.15)
        try:
            feed = get(f"https://statsapi.mlb.com/api/v1.1/game/{pk}/feed/live")
        except Exception as e:
            print(f"skip {pk}: {e}"); continue
        gd, ld = feed.get("gameData", {}), feed.get("liveData", {})
        status = gd.get("status", {}).get("detailedState", "")
        abbr = {s: gd.get("teams", {}).get(s, {}).get("abbreviation", "") for s in ("home", "away")}
        runs = {s: ld.get("linescore", {}).get("teams", {}).get(s, {}).get("runs", "") for s in ("home", "away")}
        dec = ld.get("decisions", {}); winner = dec.get("winner", {}).get("id")
        for side in ("home", "away"):
            opp = "away" if side == "home" else "home"
            team = ld.get("boxscore", {}).get("teams", {}).get(side, {})
            starter_id = (team.get("pitchers") or [None])[0]
            for pid, pl in team.get("players", {}).items():
                person = pl.get("person", {}); st = pl.get("stats", {})
                bat, pit = st.get("batting", {}), st.get("pitching", {})
                bo = str(pl.get("battingOrder", "") or "")
                base = dict(date=date, game_pk=pk, status=status, team=abbr[side], opp=abbr[opp],
                            home=int(side == "home"), team_runs=runs[side], opp_runs=runs[opp],
                            player_id=person.get("id"), player=person.get("fullName"),
                            pos=pl.get("position", {}).get("abbreviation", ""),
                            bat_slot=(int(bo) // 100 if bo.isdigit() else ""), bat_starter=int(bo.endswith("00")) if bo else 0)
                if bat and (int(bat.get("plateAppearances", 0) or 0) > 0):
                    rows.append({**base, "kind": "H", "pa": bat.get("plateAppearances", 0), "ab": bat.get("atBats", 0),
                                 "h": bat.get("hits", 0), "2b": bat.get("doubles", 0), "3b": bat.get("triples", 0),
                                 "hr": bat.get("homeRuns", 0), "r": bat.get("runs", 0), "rbi": bat.get("rbi", 0),
                                 "bb": bat.get("baseOnBalls", 0), "hbp": bat.get("hitByPitch", 0), "sb": bat.get("stolenBases", 0),
                                 "k": bat.get("strikeOuts", 0), "ip": "", "er": "", "win": "", "qs": "", "started": "",
                                 "ud_pts": hitter_pts(bat)})
                if pit and pit.get("inningsPitched") not in (None, "", "0.0") or (pit and int(pit.get("battersFaced", 0) or 0) > 0):
                    won = int(person.get("id") == winner)
                    pts, ip, qs = pitcher_pts(pit, won)
                    rows.append({**base, "kind": "P", "pa": "", "ab": "", "h": pit.get("hits", 0), "2b": "", "3b": "",
                                 "hr": pit.get("homeRuns", 0), "r": pit.get("runs", 0), "rbi": "", "bb": pit.get("baseOnBalls", 0),
                                 "hbp": pit.get("hitBatsmen", 0), "sb": "", "k": pit.get("strikeOuts", 0), "ip": ip,
                                 "er": pit.get("earnedRuns", 0), "win": won, "qs": qs,
                                 "started": int(person.get("id") == starter_id), "ud_pts": pts})
    return rows

def pull_schedule(date):
    sched = get(f"{API}/schedule?sportId=1&date={date}&hydrate=probablePitcher,lineups,team")
    rows = []
    for d in sched.get("dates", []):
        for g in d.get("games", []):
            t = g["teams"]; lu = g.get("lineups", {})
            for side in ("away", "home"):
                opp = "home" if side == "away" else "away"
                pp = t[side].get("probablePitcher", {}); opp_pp = t[opp].get("probablePitcher", {})
                lineup = lu.get(f"{side}Players", []) or []
                rows.append(dict(date=date, game_pk=g["gamePk"], time_utc=g.get("gameDate", ""), status=g.get("status", {}).get("detailedState", ""),
                                 team=t[side]["team"].get("abbreviation", ""), opp=t[opp]["team"].get("abbreviation", ""), home=int(side == "home"),
                                 prob_sp_id=pp.get("id", ""), prob_sp=pp.get("fullName", ""),
                                 opp_sp_id=opp_pp.get("id", ""), opp_sp=opp_pp.get("fullName", ""),
                                 lineup=" | ".join(f"{i+1}:{p.get('fullName')}({p.get('primaryPosition',{}).get('abbreviation','')})" for i, p in enumerate(lineup))))
    return rows

def write(path, rows):
    if not rows: print(f"no rows for {path}"); return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"wrote {path}: {len(rows)} rows")

def expand(arg, now):
    """blank -> yesterday | date | date,date | start:end | season[:YYYY]"""
    yday = (now - timedelta(days=1)).date()
    if not arg: return [yday.isoformat()]
    if arg.startswith("season"):
        yr = int(arg.split(":")[1]) if ":" in arg else now.year
        start = datetime(yr, 3, 15).date(); end = yday if yr == now.year else datetime(yr, 11, 5).date()
        return [(start + timedelta(days=i)).isoformat() for i in range((end - start).days + 1)]
    if ":" in arg:
        a, b = [datetime.strptime(x.strip(), "%Y-%m-%d").date() for x in arg.split(":")]
        return [(a + timedelta(days=i)).isoformat() for i in range((b - a).days + 1)]
    return [x.strip() for x in arg.split(",") if x.strip()]

if __name__ == "__main__":
    now = datetime.now(ET)
    dates = expand((sys.argv[1] if len(sys.argv) > 1 else "").strip(), now)
    force = os.environ.get("FORCE") == "1"
    for d in dates:
        path = f"data/boxscores/{d}.csv"
        if os.path.exists(path) and not force:
            continue
        rows = pull_boxscores(d)
        if rows: write(path, rows)
        else: print(f"{d}: no regular-season games")
    today = now.strftime("%Y-%m-%d")
    write(f"data/schedule/{today}.csv", pull_schedule(today))
