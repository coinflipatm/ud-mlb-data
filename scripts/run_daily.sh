#!/usr/bin/env bash
# Run from the ud-mlb-data repo root. Usage: scripts/run_daily.sh 2026-08-30 [odds.csv] [AWAY@HOME,...] [blocked.txt]
set -e
D=${1:?date}; ODDS=${2:-}; GAMES=${3:-}; BLOCKED=${4:-}
mkdir -p work && curl -sL https://codeload.github.com/JarvisLee511/mlb-playoff-predictor-2026/tar.gz/main | tar xz -C work
ARGS="--date $D --ud_dir . --pred_dir work/mlb-playoff-predictor-2026-main --out sheets/$D"
[ -n "$ODDS" ] && ARGS="$ARGS --odds $ODDS"; [ -n "$GAMES" ] && ARGS="$ARGS --games $GAMES"; [ -n "$BLOCKED" ] && ARGS="$ARGS --blocked $BLOCKED"
python3 scripts/build_sheet.py $ARGS
