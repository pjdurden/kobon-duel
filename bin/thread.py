"""Parse and format THREAD.md, the append-only debate transcript.

Each turn is a block:

    ## Turn 12 - CONSTRUCTOR - 2026-08-18T14:00:03Z

    <prose argument>

    <!-- meta
    {"tier": "none", "addresses": [11], ...}
    -->

The meta trailer is JSON rather than YAML on purpose: it is unambiguous and
language models emit it reliably.
"""
from __future__ import annotations

import json
import pathlib
import re
from dataclasses import dataclass, field

SPEAKERS = ("CONSTRUCTOR", "OBSTRUCTOR")
ALL_SPEAKERS = SPEAKERS + ("REFEREE",)
TIERS = ("none", "silver", "gold")

HEADER_RE = re.compile(
    r"^## Turn (\d+) - (CONSTRUCTOR|OBSTRUCTOR|REFEREE) - (\S+)[ \t]*$",
    re.MULTILINE,
)
META_RE = re.compile(r"<!--\s*meta\s*\n(.*?)\n\s*-->", re.DOTALL)


@dataclass
class Turn:
    number: int
    speaker: str
    timestamp: str
    body: str
    meta: dict
    violations: list = field(default_factory=list)


def parse(text: str) -> list:
    """Split THREAD.md into Turn objects, newest last."""
    matches = list(HEADER_RE.finditer(text))
    turns = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        raw = text[start:end]
        meta_match = META_RE.search(raw)
        meta = {}
        if meta_match:
            try:
                loaded = json.loads(meta_match.group(1))
                if isinstance(loaded, dict):
                    meta = loaded
            except (ValueError, TypeError):
                meta = {}
            raw = raw[: meta_match.start()]
        turns.append(
            Turn(
                number=int(m.group(1)),
                speaker=m.group(2),
                timestamp=m.group(3),
                body=raw.strip(),
                meta=meta,
            )
        )
    return turns


def next_speaker(turns: list) -> str:
    """Alternate over debaters only. REFEREE blocks do not consume a turn."""
    for t in reversed(turns):
        if t.speaker in SPEAKERS:
            return SPEAKERS[1] if t.speaker == SPEAKERS[0] else SPEAKERS[0]
    return SPEAKERS[0]


def next_number(turns: list) -> int:
    return max((t.number for t in turns), default=0) + 1


# --------------------------------------------------------------------------
# Validation and the anti-sycophancy gate
# --------------------------------------------------------------------------

REQUIRED_META = (
    "tier",
    "addresses",
    "claims_opened",
    "claims_conceded",
    "verifier_runs",
    "falsifier",
)

_LIST_KEYS = ("addresses", "claims_opened", "claims_conceded", "verifier_runs")

# Agreement language that, standing alone, is exactly the sycophancy this
# project exists to prevent. Matched case-insensitively.
AGREEMENT_RE = re.compile(
    r"\b("
    r"you(?:'re| are) right"
    r"|good point|fair point|fair enough"
    r"|i agree|i concede|i accept that|i withdraw"
    r"|that(?:'s| is) (?:convincing|persuasive|correct)"
    r"|i was wrong|point taken|you have a point"
    r")\b",
    re.IGNORECASE,
)


def validate_meta(meta: dict) -> list:
    """Structural errors in a meta trailer. Empty list means well-formed."""
    errors = []
    for key in REQUIRED_META:
        if key not in meta:
            errors.append(f"missing required meta key: {key}")
    if "tier" in meta and meta.get("tier") not in TIERS:
        errors.append(f"tier must be one of {TIERS}, got {meta.get('tier')!r}")
    for key in _LIST_KEYS:
        if key in meta and not isinstance(meta[key], list):
            errors.append(f"{key} must be a list, got {type(meta[key]).__name__}")
    if "falsifier" in meta and not isinstance(meta["falsifier"], str):
        errors.append("falsifier must be a string")
    return errors


def gate_tier(meta: dict, allow_gold: bool):
    """Only the verifier or the referee may declare gold."""
    if meta.get("tier") == "gold" and not allow_gold:
        downgraded = dict(meta, tier="none")
        return downgraded, [
            "TIER_DOWNGRADED: this turn self-declared gold. Only a verifier "
            "run or the referee may set gold."
        ]
    return meta, []


def check_grounding(turn: Turn) -> list:
    """Concessions must cite evidence, and agreement must be declared.

    Evidence is either a verifier run id, or a markdown blockquote, which is
    the mechanical proxy for 'quotes a specific line of the opponent'.
    """
    violations = []
    conceded = turn.meta.get("claims_conceded") or []
    has_run = bool(turn.meta.get("verifier_runs"))
    has_quote = any(
        line.lstrip().startswith(">") for line in turn.body.splitlines()
    )

    if conceded and not (has_run or has_quote):
        violations.append(
            "UNGROUNDED_CONCESSION: claims_conceded is non-empty but this turn "
            "cites no verifier run and quotes no specific line of the opponent."
        )
    if AGREEMENT_RE.search(turn.body) and not conceded and not has_run:
        violations.append(
            "UNDECLARED_AGREEMENT: agreement language appears in the prose but "
            "claims_conceded is empty. Concede explicitly or argue."
        )
    return violations


def apply_gate(turn: Turn, allow_gold: bool = False) -> Turn:
    """Run every mechanical check, recording violations on the turn."""
    turn.violations.extend(f"MALFORMED_META: {e}" for e in validate_meta(turn.meta))
    turn.meta, tier_violations = gate_tier(turn.meta, allow_gold)
    turn.violations.extend(tier_violations)
    turn.violations.extend(check_grounding(turn))
    return turn


# --------------------------------------------------------------------------
# Formatting and append
# --------------------------------------------------------------------------

def format_block(turn: Turn) -> str:
    """Render a Turn as its THREAD.md block."""
    parts = [
        f"## Turn {turn.number} - {turn.speaker} - {turn.timestamp}",
        "",
        turn.body.strip(),
        "",
    ]
    if turn.violations:
        parts.append("**Gate violations**")
        parts.append("")
        parts.extend(f"- {v}" for v in turn.violations)
        parts.append("")
    parts.append("<!-- meta")
    parts.append(json.dumps(turn.meta, sort_keys=True))
    parts.append("-->")
    parts.append("")
    return "\n".join(parts)


def append_turn(path, turn: Turn) -> None:
    """Append a block to THREAD.md. Append-only, never rewrites."""
    p = pathlib.Path(path)
    existing = p.read_text() if p.exists() else "# Thread\n"
    if not existing.endswith("\n"):
        existing += "\n"
    p.write_text(existing + "\n" + format_block(turn))


def window(turns: list, n: int) -> list:
    """The last n turns, for bounding prompt cost."""
    return turns[-n:] if n < len(turns) else list(turns)
