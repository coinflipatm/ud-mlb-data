# ud-mlb-data

Nightly MLB box scores scored with Underdog Battle Royale **daily** scoring, plus each day's probable pitchers and posted lineups. Pulled from the MLB Stats API by GitHub Actions and committed to `data/`.

## One-time setup (about 10 minutes, phone browser is fine)
1. Create a free GitHub account, then a new **public** repository named `ud-mlb-data`.
2. Add these files with **Add file → Create new file**, pasting each one at the exact path:
   - `scripts/pull_mlb.py`
   - `scripts/best_picks.py`
   - `.github/workflows/pull-mlb.yml`
   - `README.md`
3. Settings → Actions → General → Workflow permissions → **Read and write permissions** → Save.
4. Actions tab → **pull-mlb** → **Run workflow**. Put `2026-08-22,2026-08-23,2026-08-24` in the date box to backfill the logged slates, then run it.
5. Check the run went green and `data/boxscores/2026-08-24.csv` exists. From then on it runs itself at 7 AM and 6 PM ET.

## Files produced
- `data/boxscores/YYYY-MM-DD.csv` — one row per player per game: line, batting slot, and `ud_pts` (Underdog daily points).
- `data/schedule/YYYY-MM-DD.csv` — today's games, probable pitchers, posted lineups (once posted).

## Scoring used (Underdog daily, from the Underdog help center article "Daily vs Best Ball Scoring")
Hitters: 1B 3, 2B 6, 3B 8, HR 10, BB 3, HBP 3, R 2, RBI 2, SB 4.
Pitchers: W 2, QS 3, K 1, IP 1 (fractional), ER −1.
