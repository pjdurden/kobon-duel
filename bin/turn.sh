#!/usr/bin/env bash
# One debate turn: pick the speaker, build the prompt, run headless Claude,
# gate the response, append it, re-render, commit, push, notify.
set -uo pipefail
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin:$HOME/.bun/bin:/snap/bin"

ROOT="$HOME/kobon-duel"
LOG="$ROOT/run.log"
LOCK="$ROOT/.turn.lock"
MODEL="${KOBON_MODEL:-sonnet}"
# shellcheck source=lib.sh
. "$ROOT/bin/lib.sh"
SPEAKER="${1:-}"

exec 9>"$LOCK"
if ! flock -n 9; then
  echo "[$(date -u +%FT%TZ)] another run holds the lock, skipping" >> "$LOG"
  exit 0
fi

cd "$ROOT" || exit 1
[ -z "$SPEAKER" ] && SPEAKER="$(python3 bin/next_speaker.py)"
TS="$(date -u +%FT%TZ)"

echo "[$TS] turn start, speaker=$SPEAKER model=$MODEL" >> "$LOG"

PROMPT="$(python3 bin/take_turn.py "$SPEAKER")"
# Debate turns produce text only. Plan mode is wrong here: it steers the model
# toward an ExitPlanMode-shaped response instead of an argument. Write tools are
# blocked instead, so a turn can never mutate the repo behind the driver's back.
# --allowedTools is required: headless runs start in `manual` permission mode,
# so anything needing approval is denied. Without it the repository's verifier
# was unreachable for 377 turns and every "silver" was self-assessed prose.
START_EPOCH="$(date -u +%s)"
RESPONSE="$(printf '%s' "$PROMPT" | claude -p --model "$MODEL" \
    --allowedTools "Bash(python3:*),Read,Glob,Grep" \
    --disallowed-tools "Write,Edit,NotebookEdit" 2>>"$LOG")"
RC=$?

# Exit non-zero: an empty response, a session limit, or any other runner error
# means the model never produced a turn. Exiting 0 here made systemd report
# success while the debate had silently stopped, which is how a stall could go
# unnoticed for weeks. Committing the error text made it worse: it entered
# THREAD.md as a turn and consumed the speaker's slot.
if REASON="$(kobon_reject_reason "$RC" "$RESPONSE")"; then
  echo "[$TS] no turn taken ($REASON), failing loudly" >> "$LOG"
  exit 1
fi

printf '%s' "$RESPONSE" | python3 bin/commit_turn.py "$SPEAKER" "$TS" || {
  echo "[$TS] commit_turn failed" >> "$LOG"; exit 1; }

python3 bin/render.py
git add -A
git commit -q -m "turn: $SPEAKER at $TS" || true
git push -q origin main 2>>"$LOG" || \
  echo "[$TS] push failed, will retry next turn" >> "$LOG"

bash bin/notify.sh
# Log the real completion time, not $TS. Logging the start timestamp for both
# lines made every turn look instantaneous and hid how long the lock was held.
echo "[$(date -u +%FT%TZ)] turn done, started $TS, took $(( $(date -u +%s) - START_EPOCH ))s" >> "$LOG"
