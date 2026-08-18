"""Assemble a turn prompt and ingest the model's response.

Kept out of bash because these are the two parts worth testing.
"""
from __future__ import annotations

import pathlib
import re
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent
WINDOW = 6

PREAMBLE = """You are taking one turn in an ongoing public debate.

Write your argument as prose, then end with the meta trailer exactly as your
brief specifies. Output nothing else: no preamble, no sign-off, no markdown
headings of the form "## Turn". The driver adds the header for you.

You are: {speaker}
"""

SECTION = "\n\n===== {title} =====\n\n{body}\n"


def build_prompt(speaker, turns, known, literature, ledger, agenda, brief):
    """Assemble the full user prompt for one turn."""
    parts = [PREAMBLE.format(speaker=speaker)]
    parts.append(SECTION.format(title="YOUR BRIEF", body=brief))
    parts.append(SECTION.format(title="LITERATURE", body=literature))
    parts.append(SECTION.format(title="KNOWN VALUES", body=known))
    parts.append(SECTION.format(title="LEDGER", body=ledger))
    parts.append(SECTION.format(title="AGENDA", body=agenda))

    recent = thread.window(turns, WINDOW)
    if recent:
        blocks = "\n\n".join(
            f"--- Turn {t.number}, {t.speaker} ---\n{t.body}" for t in recent
        )
    else:
        blocks = "(The thread is empty. You are opening the debate.)"
    parts.append(SECTION.format(title="RECENT TURNS", body=blocks))
    parts.append(
        "\n\nNow take your turn. Address the most recent argument directly."
    )
    return "".join(parts)


_FENCE_RE = re.compile(r"```[a-zA-Z]*\s*\n(.*?)```", re.DOTALL)

# Models sometimes prepend a harness aside as an HTML comment ("Using no
# skill: ..."). It is invisible once rendered but it is not part of the
# argument, so it does not belong in the transcript. Strip every comment that
# is not the meta trailer.
_STRAY_COMMENT_RE = re.compile(r"<!--(?!\s*meta\b)[\s\S]*?-->", re.MULTILINE)


def ingest(raw: str, number: int, speaker: str, timestamp: str,
           allow_gold: bool) -> thread.Turn:
    """Parse a raw model response into a gated Turn.

    Models wrap the trailer in a code fence often enough that unwrapping is
    cheaper than retrying.
    """
    text = _STRAY_COMMENT_RE.sub("", raw).strip()
    if "<!-- meta" not in text:
        text = _FENCE_RE.sub(lambda m: m.group(1), text)
    else:
        text = re.sub(r"```[a-zA-Z]*[ \t]*\n(?=<!--\s*meta)", "", text)
        text = re.sub(r"(-->)\s*\n?```", r"\1", text)

    parsed = thread.parse(
        f"## Turn {number} - {speaker} - {timestamp}\n\n{text}\n"
    )
    if parsed:
        turn = parsed[0]
    else:
        turn = thread.Turn(number, speaker, timestamp, text, {})

    if not turn.meta:
        turn.meta = {
            "tier": "none", "addresses": [], "claims_opened": [],
            "claims_conceded": [], "verifier_runs": [],
            "falsifier": "(none supplied)",
        }
        turn.violations.append(
            "MALFORMED_META: no parseable meta trailer; a default was supplied."
        )
        return thread.apply_gate(turn, allow_gold)

    return thread.apply_gate(turn, allow_gold)


def main() -> int:
    """Print the prompt for the next turn. The shell drives claude."""
    speaker = sys.argv[1] if len(sys.argv) > 1 else None
    turns = thread.parse((ROOT / "THREAD.md").read_text())
    speaker = speaker or thread.next_speaker(turns)
    brief_file = f"agents/{thread.slug(speaker)}.md"
    sys.stdout.write(
        build_prompt(
            speaker,
            turns,
            (ROOT / "KNOWN.md").read_text(),
            (ROOT / "LITERATURE.md").read_text(),
            (ROOT / "LEDGER.md").read_text(),
            (ROOT / "AGENDA.md").read_text(),
            (ROOT / brief_file).read_text(),
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
