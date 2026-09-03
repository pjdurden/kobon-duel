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

# Character budgets for LEDGER.md inside the prompt. The referee appends
# reference-data sections and never removes them, so the ledger grew
# 262 B -> 173 KB in fifteen days and became 79% of the prompt, on track to blow
# the context window. A section count cannot bound this because one section can
# be huge on its own (#33 is 78 KB, over half the appendix), so budget bytes.
# Nothing is deleted: the full ledger stays on disk, in git and on the site, and
# agents have Read to fetch any section they need.
LEDGER_HEAD_BUDGET = 24_000
LEDGER_REFDATA_BUDGET = 40_000

PREAMBLE = """You are taking one turn in an ongoing public debate.

Write your argument as prose, then end with the meta trailer exactly as your
brief specifies. Output nothing else: no preamble, no sign-off, no markdown
headings of the form "## Turn". The driver adds the header for you.

You are: {speaker}
"""

SECTION = "\n\n===== {title} =====\n\n{body}\n"


_REFDATA_RE = re.compile(r"^## Referee reference data\b", re.MULTILINE)


def _clip(text: str, budget: int, what: str) -> str:
    """Truncate to `budget` chars on a line boundary, saying so."""
    if len(text) <= budget:
        return text
    cut = text.rfind("\n", 0, budget)
    if cut <= 0:
        cut = budget
    return text[:cut].rstrip() + f"\n\n[{what} truncated here to bound the prompt; read LEDGER.md for the rest.]"


def trim_ledger(ledger: str,
                head_budget: int = LEDGER_HEAD_BUDGET,
                refdata_budget: int = LEDGER_REFDATA_BUDGET) -> str:
    """Bound the ledger's contribution to the prompt.

    The referee's narrative findings and call-outs sit above the first
    reference-data heading and are kept first; the cumulative evidence appendix
    is then filled from the most recent section backwards until the budget runs
    out. The most recent section is always included, truncated if it alone
    exceeds the budget. Every elision names LEDGER.md as the place to read on.
    """
    starts = [m.start() for m in _REFDATA_RE.finditer(ledger)]
    if not starts:
        return _clip(ledger, head_budget + refdata_budget, "Ledger")

    head = _clip(ledger[: starts[0]].rstrip(), head_budget, "Ledger narrative")

    bounds = [(starts[i], starts[i + 1] if i + 1 < len(starts) else len(ledger))
              for i in range(len(starts))]

    kept, used = [], 0
    for lo, hi in reversed(bounds):
        section = ledger[lo:hi].rstrip()
        if not kept:
            section = _clip(section, refdata_budget, "Reference-data section")
        elif used + len(section) > refdata_budget:
            break
        kept.append(section)
        used += len(section)
    kept.reverse()

    dropped = len(bounds) - len(kept)
    notice = ""
    if dropped:
        notice = (
            f"\n\n[{dropped} earlier reference-data section(s) elided from this "
            f"prompt to bound its size. They remain in LEDGER.md; read the file "
            f"directly if you need one.]\n"
        )
    return head + notice + "\n\n" + "\n\n".join(kept) + "\n"


def build_prompt(speaker, turns, known, literature, ledger, agenda, brief):
    """Assemble the full user prompt for one turn."""
    parts = [PREAMBLE.format(speaker=speaker)]
    parts.append(SECTION.format(title="YOUR BRIEF", body=brief))
    parts.append(SECTION.format(title="LITERATURE", body=literature))
    parts.append(SECTION.format(title="KNOWN VALUES", body=known))
    parts.append(SECTION.format(title="LEDGER", body=trim_ledger(ledger)))
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
