"""Compose and post the daily referee tweet.

The referee writes its own tweet text into its meta trailer. This module only
budgets, validates, and posts it. Anything questionable is refused rather than
posted: a skipped tweet costs nothing, a malformed one is public.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent
XDIR = pathlib.Path.home() / ".claude" / "x-agent"

SITE = "https://pjdurden.github.io/kobon-duel/"
REPO = "https://github.com/pjdurden/kobon-duel"

LIMIT = 280
TCO = 23  # X counts every URL as 23 characters, whatever its real length.

_URL_RE = re.compile(r"https?://\S+")

# text + "\n\n" + SITE + "\n" + REPO
_TAIL = 2 + TCO + 1 + TCO
MAX_TEXT = LIMIT - _TAIL


def weighted_len(text: str) -> int:
    """Length as X counts it, with every URL costing TCO characters."""
    return len(_URL_RE.sub("U" * TCO, text))


def compose(text):
    """Return (tweet, reason). tweet is None when it must not be posted."""
    if not text or not str(text).strip():
        return None, "no tweet text supplied"
    body = str(text).strip()

    # His posting rule: never an em dash in anything published.
    body = body.replace("—", ", ").replace("–", "-")
    body = re.sub(r"\s+,", ",", body)

    if _URL_RE.search(body):
        return None, "tweet text contains its own link; the driver adds them"
    if "#" in body:
        return None, "tweet text contains a hashtag; not allowed here"
    if len(body) > MAX_TEXT:
        return None, f"tweet text too long: {len(body)} > {MAX_TEXT}"

    out = f"{body}\n\n{SITE}\n{REPO}"
    if weighted_len(out) > LIMIT:
        return None, f"composed tweet too long: {weighted_len(out)} > {LIMIT}"
    return out, "ok"


def from_thread(thread_text: str):
    """Compose from the most recent REFEREE turn. Debater turns are ignored."""
    referee_turns = [t for t in thread.parse(thread_text) if t.speaker == "REFEREE"]
    if not referee_turns:
        return None, "no referee turn in the thread"
    return compose((referee_turns[-1].meta or {}).get("tweet"))


def post(text: str, dry: bool = False):
    """Post via the existing x-agent client. cwd is x-agent so bun loads .env."""
    cmd = ["bun", str(ROOT / "bin" / "post_tweet.ts"), text]
    if dry:
        cmd.append("--dry")
    return subprocess.run(
        cmd, cwd=str(XDIR), capture_output=True, text=True, timeout=60
    )


def main() -> int:
    dry = "--dry" in sys.argv
    out, why = from_thread((ROOT / "THREAD.md").read_text())
    if out is None:
        sys.stderr.write(f"tweet skipped: {why}\n")
        return 1
    res = post(out, dry=dry)
    sys.stdout.write(res.stdout)
    sys.stderr.write(res.stderr)
    return res.returncode


if __name__ == "__main__":
    sys.exit(main())
