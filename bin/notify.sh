#!/usr/bin/env bash
# Send a Telegram message only when the newest turn is silver or gold.
set -uo pipefail

ROOT="$HOME/kobon-duel"
BOT_ENV="$HOME/.claude/x-agent/bot.env"
LOG="$ROOT/run.log"

[ -f "$BOT_ENV" ] || { echo "[$(date -u +%FT%TZ)] no bot.env" >> "$LOG"; exit 0; }
# shellcheck disable=SC1090
. "$BOT_ENV"

MSG="$(cd "$ROOT" && python3 bin/last_tier.py)" || exit 0
[ -z "${MSG// }" ] && exit 0

curl -sS -X POST \
  "https://api.telegram.org/bot${XAGENT_BOT_TOKEN}/sendMessage" \
  -d "chat_id=${XAGENT_CHAT_ID}" \
  --data-urlencode "text=${MSG}" \
  -d "disable_web_page_preview=false" \
  >> "$LOG" 2>&1

echo "[$(date -u +%FT%TZ)] notified" >> "$LOG"
