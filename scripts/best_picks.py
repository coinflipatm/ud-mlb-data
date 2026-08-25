#!/usr/bin/env python3
"""Who were the best picks? Reads data/boxscores/<date>.csv and prints the board.
Usage: python scripts/best_picks.py 2026-08-24
"""
import csv, sys
from collections import defaultdict

IF_POS = {"C", "1B", "2B", "3B", "SS"}; OF_POS = {"LF", "CF", "RF", "OF"}
date = sys.argv[1]
rows = list(csv.DictReader(open(f"data/boxscores/{date}.csv")))
for r in rows: r["ud_pts"] = float(r["ud_pts"] or 0)
H = [r for r in rows if r["kind"] == "H"]; P = [r for r in rows if r["kind"] == "P" and r["started"] == "1"]

print(f"\n=== {date}: top 20 bats ===")
for r in sorted(H, key=lambda r: -r["ud_pts"])[:20]:
    print(f'{r["ud_pts"]:5.0f}  {r["player"]:<24} {r["team"]:<4} B{r["bat_slot"]:<2} {r["pos"]:<3} ({r["team_runs"]} runs)')
print(f"\n=== top 10 starting pitchers ===")
for r in sorted(P, key=lambda r: -r["ud_pts"])[:10]:
    print(f'{r["ud_pts"]:6.2f}  {r["player"]:<24} {r["team"]:<4} {r["ip"]} IP {r["k"]} K {r["er"]} ER W{r["win"]} QS{r["qs"]}')

team = defaultdict(list)
for r in H:
    if r["bat_starter"] == "1": team[r["team"]].append(r)
print(f"\n=== team stacks: sum of top-5 bats, and slots 3-6 ===")
for t, rs in sorted(team.items(), key=lambda kv: -sum(sorted((x["ud_pts"] for x in kv[1]), reverse=True)[:5])):
    top5 = sum(sorted((x["ud_pts"] for x in rs), reverse=True)[:5])
    s36 = sum(x["ud_pts"] for x in rs if x["bat_slot"] in ("3", "4", "5", "6"))
    print(f'{t:<4} runs {rs[0]["team_runs"]:>2}  top5 {top5:5.0f}  slots3-6 {s36:5.0f}')

print(f"\n=== avg points by lineup slot (starters) ===")
slot = defaultdict(list)
for r in H:
    if r["bat_starter"] == "1" and r["bat_slot"]: slot[int(r["bat_slot"])].append(r["ud_pts"])
for s in sorted(slot): print(f'B{s}: {sum(slot[s])/len(slot[s]):5.1f}  (n={len(slot[s])})')

best_p = max(P, key=lambda r: r["ud_pts"]) if P else None
inf = sorted((r for r in H if r["pos"] in IF_POS), key=lambda r: -r["ud_pts"])
of = sorted((r for r in H if r["pos"] in OF_POS), key=lambda r: -r["ud_pts"])
pick = ([best_p] if best_p else []) + inf[:2] + of[:2]
flex = next((r for r in sorted(H, key=lambda r: -r["ud_pts"]) if r not in pick), None)
print(f"\n=== optimal 6 (by API position; Underdog eligibility may differ) ===")
for r in pick + ([flex] if flex else []):
    print(f'{r["ud_pts"]:6.2f}  {r["player"]:<24} {r["team"]:<4} {r["pos"]}')
print(f'TOTAL {sum(r["ud_pts"] for r in pick + ([flex] if flex else [])):.2f}')