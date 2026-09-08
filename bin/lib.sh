#!/usr/bin/env bash
# Shared guards for the turn and referee drivers.

# A headless `claude -p` run can return a runner error on stdout instead of a
# turn: "You've hit your session limit", an overload, an auth failure. That text
# is non-empty, so the old `[ -z "$RESPONSE" ]` check passed it straight through
# and it was committed as a real turn with a MALFORMED_META violation. Nine
# turns were poisoned that way, T380 among them — a referee pass, so the ledger
# skipped a day and the debaters steered off a stale audit for the next window.
#
# Prints a reason and returns 0 when the response must NOT become a turn.
# Returns 1 when it looks like a genuine turn.
kobon_reject_reason() {
  local rc="$1" body="$2"

  if [ "$rc" -ne 0 ]; then
    printf 'claude exited %s' "$rc"
    return 0
  fi

  if [ -z "${body// }" ]; then
    printf 'empty response'
    return 0
  fi

  if printf '%s' "$body" | grep -qiE \
      "hit your (session|usage) limit|usage limit reached|rate limit|credit balance is too low|api error: [45][0-9][0-9]|overloaded_error|invalid api key|not logged in"; then
    printf 'runner error: %s' "$(printf '%s' "$body" | head -c 120 | tr '\n' ' ')"
    return 0
  fi

  # A real turn is long prose ending in a meta trailer. Something short with no
  # trailer is a runner message this function has not learned to name yet.
  if ! printf '%s' "$body" | grep -q '<!-- meta' && [ "${#body}" -lt 400 ]; then
    printf 'no meta trailer and only %s chars, not a turn: %s' \
      "${#body}" "$(printf '%s' "$body" | head -c 120 | tr '\n' ' ')"
    return 0
  fi

  return 1
}
