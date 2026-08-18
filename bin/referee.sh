#!/usr/bin/env bash
# Daily referee pass on Opus. Rewrites LEDGER.md and AGENDA.md, appends its
# own turn, and is the only participant allowed to set gold.
set -uo pipefail
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin:$HOME/.bun/bin:/snap/bin"

ROOT="$HOME/kobon-duel"
LOG="$ROOT/run.log"
LOCK="$ROOT/.turn.lock"
MODEL="${KOBON_REFEREE_MODEL:-opus}"

exec 9>"$LOCK"
if ! flock -w 300 9; then
  echo "[$(date -u +%FT%TZ)] referee could not get the lock" >> "$LOG"
  exit 0
fi

cd "$ROOT" || exit 1
TS="$(date -u +%FT%TZ)"
echo "[$TS] referee start, model=$MODEL" >> "$LOG"

PROMPT="$(python3 bin/take_turn.py REFEREE)

You are running with write access to this repository. Rewrite LEDGER.md and
AGENDA.md directly using your file tools before you produce your turn text.
Then output ONLY your turn prose and its meta trailer."

RESPONSE="$(printf '%s' "$PROMPT" | claude -p --model "$MODEL" \
    --permission-mode acceptEdits --add-dir "$ROOT" 2>>"$LOG")"

if [ -z "${RESPONSE// }" ]; then
  echo "[$TS] referee returned nothing" >> "$LOG"
  exit 0
fi

printf '%s' "$RESPONSE" | python3 bin/commit_turn.py REFEREE "$TS"

python3 bin/render.py
git add -A
git commit -q -m "referee: daily pass at $TS" || true
git push -q origin main 2>>"$LOG" || echo "[$TS] push failed" >> "$LOG"

bash bin/notify.sh

# Daily build-in-public post. A skipped tweet is logged and never fatal: the
# referee pass itself has already landed and must not be retried for this.
python3 bin/tweet.py >> "$LOG" 2>&1 || \
  echo "[$TS] tweet skipped (see above)" >> "$LOG"

echo "[$TS] referee done" >> "$LOG"
