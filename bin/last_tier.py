"""Report the tier of the most recent turn, with a Telegram-ready message."""
from __future__ import annotations

import pathlib
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://pjdurden.github.io/kobon-duel/"


def summarize(text: str):
    turns = thread.parse(text)
    if not turns:
        return "none", ""
    t = turns[-1]
    tier = (t.meta or {}).get("tier", "none")
    if tier not in ("silver", "gold"):
        return "none", ""

    label = "GOLD" if tier == "gold" else "SILVER"
    excerpt = " ".join(t.body.split())[:400]
    claims = ", ".join((t.meta.get("claims_conceded") or [])) or "none declared"
    msg = (
        f"kobon-duel {label}\n\n"
        f"Turn {t.number}, {t.speaker}, {t.timestamp}\n"
        f"Claims conceded: {claims}\n\n"
        f"{excerpt}\n\n"
        f"{SITE}"
    )
    return tier, msg


def main() -> int:
    tier, msg = summarize((ROOT / "THREAD.md").read_text())
    if tier == "none":
        return 1
    sys.stdout.write(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
