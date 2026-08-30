# METHODOLOGY v1 — Underdog MLB Battle Royale daily operating system
Written 8/30/2026. Process layer under Rulebook v8. **Laws 1–20 are frozen (Rule 20) and unchanged by this document.** Where the season data contradicts a law, the sheet prints both orderings, the queue follows the law, and the conflict is logged in §8 as a recorded observation for the slate-10 review (Rule 15). Every number below carries its n and source (Rule 14). Sources: `ud-mlb-data` boxscores 3/25–8/28/2026 (36,722 batter-starts, 4,081 SP starts, 4,082 team-games); `mlb-playoff-predictor-2026` pitcher_logs through 8/28; the 8/29 status report (15 observed winners, 21 of our tickets).

---

## 0. What a winning ticket is — the arithmetic

- A league-average roster scores **~48** (five bats × ~7.8 + SP 9.0). Cash lines run 58–85; observed winners median **136**, min 96.67; a 96-entry Double Play was won at **98**. (report 5.1)
- A real five-bat stack from lineup slots 1–5 sums to **40.9 on average**. It reaches **70+ in 9.7%** of team-games, **90+ in 2.4%**, **110+ in 0.47%**, **125+ in 0.07%** (n=4,078 team-games, boxscores).
- 110+ from five bats is functionally "the team scored 12+" (base rate **3.2%** of team-games; P(9+) **11.1%**). 77.7% of 20-point games contain a home run (report 1.3).

So a win is three independent-ish events on one ticket: **(1) the stacked lineup goes 9–12+, (2) the arm scores 12+, (3) no slot zeroes.** Everything in this document is one of three jobs: pick the lineup with the fattest tail, pick an arm that can't sink the ticket, protect the floor around the bet. **Individual bat selection inside the chosen lineup is third-order** (report 2.1) — the sheet spends its effort on the lineup, not the name.

Honest expectation: there is no process that wins daily. A stacked ticket built from a top-tier lineup posts a Double-Play-winning score (~98+) roughly **3–4% of the time** vs ~1% for a random entry (5-bat P(90+) 2.4% base, tilted up ~1.5× by team/park/arm selection, plus a 9-point arm). Two Double Play entries a day is on the order of one win every 3–4 weeks, with wide variance. The daily goal is a ticket that is +9 to +16 over baseline every day (our measured range, report 6.1) with a stacked tail, entered where that converts (§6).

---

## 1. Evidence ledger

**PROVEN (large n, reproduced today)**
| Finding | Numbers | n / source |
|---|---|---|
| Scoring | 1B 3 · 2B 6 · 3B 8 · HR 10 · BB 3 · HBP 3 · R 2 · RBI 2 · SB 4 · SP: IP 1, K 1, W 2, QS 3, ER −1 | 100% match, 36,722 rows |
| Team runs drive 20s | P(bat ≥20): 0–2 runs 1.3% → 5–6 10.1% → 9–11 23.5% → 12+ 34.5% | 24,485 slot 1–6 starts |
| Slot gradient (season) | P20: B1 10.0, B2 9.3, B3 9.4, B4 8.6, B5 7.1, B6 6.1, B7 5.7, B8 4.5, B9 4.0%. Mean: 8.7 → 5.6 | ~4,050/slot |
| Slot gradient when the lineup blows up (9+ runs) | P20: B1 30.2, B2 30.0, B3 28.9, B4 27.5, B5 20.9, B6 22.3, B7 20.9, B9 16.8%. Mean B1 15.5 vs B6 13.1 | 4,083 |
| Stack tail (real data, same slot mix) | Slots 1–5 stack: P(90+) 2.4%, P(110+) 0.47%. Five bats slot 1–5 from five teams: 0.7%, 0.03%. **Means identical (40.9 vs 40.7).** 1–5 beats 2–6 beats 3–7 at every threshold | 4,078 stacks / 3,037 spreads |
| SP win probability | mean 6.9 (dog <.40) → 11.2 (fav .60+); P(20) 0.5% → 10.6%. SP season max 29, min −8.3 | report 2.4 / 4,081 SP starts |
| Zero rates by slot | P(≤0): B1 18%, B3 18%, B4 21%, B5 22%, B6 24%, B9 32% | ~4,050/slot |
| Spot starter (≤2 prior GS) | offense +0.28 R vs own avg; 5+ runs 47.7% vs 42.1% | 4,506 instances, 2015–26 |
| Team quality predicts the tail, not the 5+ line | prior R/G tercile low→high: P(5+) 42.0→42.7%, **P(9+) 9.5→12.5%, P(12+) 2.2→4.4%** | 3,482 team-games, expanding out-of-sample mean |
| Ranking metric | season mean UD predicts future P20 better than past P20 (r .374 vs .328); mean is 2× as reliable split-half | report 3.1, 325–367 players |

**TILT (real but modest; treat as a tiebreak inside a tier, never as the tier)**
| Lever | Size | Caveat |
|---|---|---|
| Park P20 index (shrunk, both teams) | COL 1.39, ATH 1.39, WSH 1.26, CHC 1.14, HOU 1.13 … STL 0.86, DET 0.84, TOR 0.83, LAA 0.80 | includes the home lineup's quality; ~132 team-games/park |
| Opposing-arm HR/9 tercile | P20 index LOW 0.74 · MID 0.99 · HIGH 1.26 | HR/9 shrunk toward league with 40 IP prior |
| Park × arm combined | 0.59 (LAA vs low-HR arm) … 1.75 (ATH vs high-HR arm) on the 8/29 board | **failed its first live test** (Target Field 5 runs, Wrigley 22 — report 4.2). One sample; keep printing, keep grading |
| Home/road run splits | KC 3.74 road vs 5.73 blend → scored 3 (report 4.1) | one live confirmation |

**DISPROVEN / NO EFFECT**
- Handedness for performance: 7.49% same-hand vs 7.28% platoon edge, n=27,579 (report 2.3). Use only for sit risk — and start_rate15 measures that directly.
- Shutout bounce-back: rejected (memory log).
- App projections as a sit/start fact: Carson Kelly "2.8 projected" started B9 and scored 33 on the 1st and 2nd place tickets (report 4.2). Rule 12 already says *ignore the app's projections entirely*; the fade was a rule violation, not a rule gap.
- ERA alone, moneyline alone, "chalk is a wash" (Rules 2, 6).

**OPEN (slate-10 agenda, §9)**: stack vs spread in live results (≈7–3 stacked); adjusted-mean vs adjusted-P20 live; Rule 8's slot order vs season data; the Tier A/B line vs the tails of winning stacks; contest allocation; whether recurring winners have selection or volume edge.

---

## 2. The ranking model (what `build_sheet.py` computes)

**Team / stack score** — every team on the slate gets:
`stack_score = run_est × mult × (1.07 if spot starter)`
where `run_est` = market implied team total (from no-vig moneyline + O/U via a Poisson race) when odds are supplied, else the team's **home/road split** R/G (flagged MODEL/NONE); `mult` = park P20 index × opposing-arm HR/9 bucket index. Tier per Rule 16 (A ≥ 4.75, B 4.25–4.74, C below), spot-starter bump one tier. Also printed: split P(5+), P(9+), P(12+), L15 R/G, lineup posted or not.

**Law order (the queue follows this):** Tier A → B → C; inside a tier, stack_score; inside a team, slots 3–6 → B1–2 with elite power (top-2 HR/start on his own team) → B1–2 → 7–9; inside a slot group, adjusted mean. This is Rules 8 and 16 as written.

**Model order (printed beside it, logged, not queued):** pure `adj_mean = shrunk season mean UD × mult`. Shrinkage: 40 starts of league-mean prior (league bat-start mean 7.36 all slots). Open question 3 is settled by logging both every slate and comparing at slate 10.

**Ceiling column:** `max_ud` (season high). On win-oriented tickets a bat with a 40+ max moves ahead of a bat within ~1 adj_mean of him (report 3.2). This is a tiebreak, decided on the sheet, before the lobby.

**Floor guards (printed, never used live):**
- `start_rate15` < 0.80 → sit risk. It is a probability. On a win ticket at low ownership you may take him once the B# tag confirms he's in; on a floor ticket you don't.
- `starts` < 40 → thin sample; his adj_mean is mostly prior.
- `zeros_rate` → P(≤0) this season. Prefer the lower one when two bats are otherwise close.

**Pitchers:** legal = win prob ≥ .50 (market; MODEL fallback flagged), not Coors, probable/confirmed, not facing Game A or B. Ranked by shrunk K/9, then win prob (Rule 2). Printed beside each arm: his own UD distribution — `ud_mean`, `ud_p20`, `ud_max`, `ud_min`, `ud_n` — so a .669 favorite with a 19 max and zero 20-point games (the Gausman case) is visible before the draft. `legal arms vs drafters` is the scarcity switch (§4). Rule 1's R1 exception is flagged automatically when the top legal arm clears the next by ≥ 1.0 shrunk K/9.

**Tags override the sheet.** Green check / B# / Q / O / no-ADP come from the screenshot, never from data (Rule 12). The sheet has no Underdog eligibility data; `pos_class` is the player's most common fielded position and DH is flagged for a manual check.

---

## 3. Build shape (inside Appendix A)

Appendix A yields "3–5 bats from A (≥3 from one lineup), the rest from B, ace from C." That range is the process choice, and the evidence says which end:

- **Win ticket (Double Play / Triple Play / Fastball lotto): 5 from Game A, slots 1–5 (or 1–6 skipping a sit-risk), ace from a third game.** Real-data tails: 5-stack P(110+) 0.47% vs 3+2 (report sim) 0.08% vs spread 0.03%. The mean is the same either way; the shape costs nothing. A 3+2 needs both games to produce; you only need one.
- **When to drop to 4+1:** Game A has a sit-risk or thin-sample bat inside slots 1–5 *and* a B1–B4 bat from Game B sits within 1 adj_mean. Never to "cover" a second game.
- **Cash ticket (deep-payout contest):** still a stack. The cash line (58–85) sits *above* the ticket mean (~50), so variance helps at every payout threshold: 1–5 stack P(70+) 9.7% vs spread 6.0%. Prefer the lowest-zero-rate bats in the stack.
- **Portfolio (Rules 9–11):** each ticket anchors a *different* Game A lineup and a *different* arm; zero overlap by default; the blocked list is written before the next room and passed to the script (`--blocked`). Three tickets = three lineups' tails, not one lineup three ways.
- **Ownership** is share of rooms (Rule 6). It changes nothing about who is drafted; it is logged on winners for the autopsy only.

---

## 4. Pitcher rules, operational

1. Count legal arms before the lobby. **Legal < drafters → arm at R2–R3** (someone leaves with a leftover). **Legal ≥ drafters → arm waits to R3–R4**, bats first (Rule 1). A confirmed favorite falling to R5 is fine; a dog never is.
2. R1 arm only when the sheet prints the Rule 1 exception (≥ 1.0 K/9 clear, not a dog).
3. The arm never faces Game A or Game B (Rule 7 / Appendix A). If the best arm faces A, take the next legal arm — do not move the stack.
4. Check `ud_p20` and `ud_max` on the arm you intend to take. A high-K favorite with a 20+ max is the profile; a favorite with a 17 max is a cap you're paying full price for.
5. Room behavior does not generalize (report 3.3). No waiting strategy is built on one room's pattern.

---

## 5. Daily timeline (the checklist)

**Morning — before anything else is discussed**
1. Trigger `pull-mlb` (Actions → Run workflow) so `data/schedule/TODAY.csv` exists with probables. Also confirm `predictions_log.csv` in the predictor repo has today's games.
2. Fino sends the contest page (games, format, entry cap, drafters/rounds) and the day's lines, or Claude fetches `covers.com/sport/baseball/mlb/odds` and writes `odds.csv` (`away,home,away_ml,home_ml,total`).
3. Claude downloads both repos fresh (codeload tarballs; a cached extract never reflects a new commit) and runs
   `python build_sheet.py --date TODAY --odds odds.csv --games AWAY@HOME,... --drafters 6 --rounds 6 --out out`
4. **Board v1** goes to Fino: pitcher table with legal count and scarcity switch, team table with tiers and stack_score, Game A / B / ace, bat board (law rank + model rank), 36-deep queue, checks (position mix, thin, sit-risk). Any A/B override happens now, by hand, with the reason written down.

**Lineups posted (2–4 h before first pitch)**
5. Re-trigger `pull-mlb` (or Fino screenshots the Players tab), re-download, re-run with `--blocked` for tickets already drafted. **Board v2 = the final queue.** Tags from the screenshot override the sheet: Q/O/no-ADP are removed, B# confirms slots. Sit-risk names are either confirmed in or dropped — never carried as a guess.
6. Claude states the slot map: for each draft position, R1–R6 by round from the queue, with the scarcity switch applied.

**Lobby (~60 s after the slot is assigned)**
7. Queue the ace plus the next 4–5 bats, then keep loading to 36 in the gaps between picks (Rule 17). Queue depth = drafters × rounds so the swap pool never falls back to ADP.

**On the clock**
8. One name, one backup, sheet order. Full first and last names. No reasoning, no "wait", no substitutions. Off-sheet name → "send the Players tab." Every 8/29 error traced to analysis run during the draft (report 7.1) — there is no analysis on the clock.

**Post-draft**
9. Roster screenshot → tag and overlap audit. Exposure page when lineups finalize → O tags flagged, swap-pool order confirmed (auto-swap does fire on O tags).

**Post-game**
10. One line per ticket in `logs/tickets.csv`, one per slate in `logs/slates.csv`, money by contest in `logs/money.csv`. Autopsy the top 5–10 with ownership; log the falco/samolson line when visible. Grade boxes (a) ≤2 games with ≥3 from one lineup, (b) every slot ≥7, (c) Game A a top-two team total. New patterns → `logs/observations.csv`, recorded only.
11. `python scripts/best_picks.py TODAY` for the actual optimal board; compare to Board v2's law rank and model rank; log which ranked the real top-5 bats higher.

Persistence: the sandbox resets every session. Keep `build_sheet.py` and `logs/` in the `ud-mlb-data` repo (`scripts/` and `logs/`) so every session starts from code and the ledger, not from memory.

---

## 6. Contest selection (process)

- Rake is 11.2–11.3% everywhere (report 6.3): break-even needs ~12.6% better than the average entrant. Our measured edge is +9 (all 21 tickets) to +16 (8/29) over a 48 baseline — but capped rooms are sharper per entry, so the true margin is smaller than that.
- Every payout line is in the right tail of the ticket distribution, so the stack goes on *every* ticket, not just the lottery ones.
- **Allocation for now:** the best Game A stack goes to the win-oriented capped room(s) (Double Play / Triple Play); the second-best lineup goes to the deepest-paying contest available that day (the 288-place, 12.8%-cash format when it runs). Fixed daily stake; no ticket gets a fourth game.
- One day's contest ROI (+567% / 0% / −100% on 8/28) is noise. `logs/money.csv` by contest type over 10+ slates decides the split at slate 10. No EV model is reported until it survives a sanity check (report 7.1 #7).
- Volume accounts (falco1002, samolson31, JJB2386…) hold multiple top-10 spots with near-ADP picks. Entry caps neutralize volume; they do not neutralize skill. Log their line on every slate (memory note) and grade whether it is selection or coverage.

---

## 7. Log schemas (`logs/`)

`tickets.csv`: date, slate_games, contest, entry_fee, draft_slot, P, P_score, bat1..bat5, bat1_score..bat5_score, n_under3, stack_team, stack_implied, stack_actual_runs, build_shape, ticket_score, cash_line, room_finish, overall_finish, payout, grade_a, grade_b, grade_c, notes
`slates.csv`: date, games, contests, winner_score, winner_P, winner_P_score, winner_stack_team, winner_stack_implied, winner_stack_actual, winner_shape, falco_samolson_line, notes
`money.csv`: date, contest, entries, dollars_in, dollars_out, net
`observations.csv`: id, date, rule_touched, observation, numbers, source

The rulebook's own log block says "freeze count: 2 of 10" while the 8/29 report covers 21 tickets across 8/22–8/29. **The canonical count is the number of rows in `slates.csv`.** Fill 8/24–8/29 from the 8/28 slate log and the 8/29 session so the count is one number.

---

## 8. Recorded observations from this build (Rule 15 — recorded, not proposed)

| id | rule | observation | numbers | source |
|---|---|---|---|---|
| O-9 | 8 | Slot order. Season and conditional data both put slots 1–4 above 5–6; 3–6 > 1–2 does not appear at any run level. | P20 B1 10.0 / B3 9.4 / B4 8.6 / B6 6.1%; in 9+ run games B1–B3 ≈ 29–30%, B5–B6 21–22% | boxscores, 36,722 / 4,083 |
| O-10 | 11 | Stack tail is real, not a simulation artifact. Same slot mix, identical means. | 1–5 stack P(90+) 2.4% vs spread 0.7%; P(110+) 0.47% vs 0.03% | boxscores, 4,078 / 3,037 |
| O-11 | 5, 16 | "Projected 5+" is not what team quality predicts. Team quality (prior R/G) moves the 9+/12+ tail and leaves P(5+) flat. | P(5+) 42.0→42.7%; P(9+) 9.5→12.5%; P(12+) 2.2→4.4% low→high tercile | boxscores, 3,482 |
| O-12 | 8 | "No zeros" is an outcome. Per-slot zero rates are 18–32%; five independent slot 1–5 bats clear zero ~33% of the time. Slot and OBP are the controllables. | P(≤0) B1 18% … B9 32% | boxscores |
| O-13 | 8, 16 | 8/29 rebuilt board: inside CHC the law order put Busch (B4, model 41st) ahead of Crow-Armstrong (B1, model 10th). Scores 0 and 53. One sample. | law_rank 20 vs 23; model_rank 41 vs 10 | out/bats_2026-08-29.csv |
| O-14 | 16 | 8/29: without market input the multiplier ranked CWS/MIN 2nd and CHC 3rd. If CHC was Tier A and MIN/CWS Tier B on the market, the law order (tier first) puts CHC at Game A. The live miss came from letting the multiplier outrank the tier. | stack_score 5.85 / 5.64; Wrigley 1.14, Target Field 0.99 park idx | out/teams_2026-08-29.csv, report 4.2 |
| O-15 | 12 | The bench-projection fade contradicts Rule 12 as written. Sit risk is measured by start_rate15 instead. | Kelly 0.60 start rate, scored 33 | report 4.2 |
| O-16 | 2 | SP scoring is capped: season max 29, 3.8% of starts ≥20; bats reach 59. | 4,081 SP starts | boxscores |
| O-17 | — | Handedness is not wired (no Lahman in the sandbox); adding batSide/pitchHand to `pull_mlb.py` from the Stats API `people` endpoint is a repo TODO. | — | — |

(O-1–O-8 are the observations already in the memory/report log: winning stacks below the A/B line, 3+2+ace/5+P shapes, run-total primacy, spot-starter edge, shutout bounce-back rejected, auto-swap confirmed, ownership framing, Sutter Health park effect.)

---

## 9. Slate-10 review agenda

Each item is decided by the aggregate log, not the last winner.
1. **Ranking metric** — law rank vs model rank: which put more of each slate's actual top-10 bats in its top 20? (`logs/observations.csv` after step 11 each day.)
2. **Slot order inside a stack** — does B1–B4 or B3–B6 carry the winning stacks in the log? (O-9, O-13)
3. **Shape** — count of 5-stack vs 3+2 vs spread among logged winners, with ticket scores. (O-10, report 5.4)
4. **Tier line** — how many winning stacks were Tier A/B pre-game vs C? (O-1, O-11)
5. **Park × arm** — for every logged slate, did the top multiplier cell out-score the bottom? (report 8.1)
6. **Arm timing** — scarcity switch outcomes: rounds the ace went, score, and rooms where legal < drafters.
7. **Contest allocation** — ROI by contest type from `money.csv`.
8. **Volume accounts** — their logged lines: chalk coverage or something we can copy?
