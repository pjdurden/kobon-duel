# kobon-duel Phase 1 (The Shell) Implementation Plan

> **Renamed 2026-08-18.** The agents CONSTRUCTOR and OBSTRUCTOR were
> renamed to **PythagorAss** and **Euclidn't**. This document keeps the
> original names as the record of what was approved; the code, briefs
> (`agents/pythagorass.md`, `agents/euclidnt.md`) and site use the new ones.


> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a live, public, hourly adversarial debate between two Claude personas about the Kobon triangle problem, rendered as a GitHub Pages transcript, with tiered Telegram notification.

**Architecture:** `THREAD.md` is an append-only markdown transcript and the sole communication medium. A Python module (`bin/thread.py`) parses it, decides whose turn it is, and enforces the anti-sycophancy rules mechanically. A bash driver (`bin/turn.sh`) builds a windowed prompt, invokes headless `claude -p`, appends the result, regenerates `docs/index.html`, and pushes a signed commit. Systemd user timers drive it hourly, with a daily Opus referee that rewrites `LEDGER.md` and `AGENDA.md`.

**Tech Stack:** Python 3.10 (stdlib only, no third-party runtime deps), pytest 7.4, bash, systemd user timers, `claude` CLI 2.1.234, GitHub Pages, marked.js + KaTeX from jsDelivr for client-side rendering.

**Spec:** `docs/superpowers/specs/2026-08-17-kobon-duel-design.md`

## Global Constraints

- Python 3.10, **stdlib only** at runtime. pytest is a dev dependency only.
- Every commit is signed: `git config user.signingkey ~/.claude/oss-scan/sign_key`, `gpg.format ssh`, `commit.gpgsign true`. Already configured in the repo.
- `THREAD.md` is **append-only**. No task may rewrite or delete an existing turn block.
- `KNOWN.md` is **agent-read-only**. No driver code writes to it.
- Agents may never set `tier: gold`. Only the verifier (phase 2) or the referee may. The driver downgrades and records a violation.
- Telegram credentials come from `~/.claude/x-agent/bot.env` (`XAGENT_BOT_TOKEN`, `XAGENT_CHAT_ID`). Never hardcode them, never commit them.
- Timestamps are UTC ISO-8601 with a `Z` suffix: `date -u +%FT%TZ`.
- Repo: `github.com/pjdurden/kobon-duel`, public, Pages served from `main` branch `/docs`.
- No em dashes in any generated public-facing copy (site header, Telegram messages).

**Deviation from spec, section 6.1:** the spec says the driver "strips ungrounded agreement language". This plan **annotates instead of strips**. Excising prose from a mathematical argument risks mangling the math, and a visible violation note is a stronger deterrent than silent deletion because the referee and the reader both see it. Task 3 implements annotate-only. Update the spec line when this task lands.

---

### Task 1: Repo bootstrap, pytest wiring, and KNOWN.md

**Files:**
- Create: `~/kobon-duel/pytest.ini`
- Create: `~/kobon-duel/.gitignore`
- Create: `~/kobon-duel/KNOWN.md`
- Create: `~/kobon-duel/tests/test_known.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `KNOWN.md` as the single source of truth for record values. Later tasks read it verbatim into prompts. `tests/` importable with `bin/` on the path.

- [ ] **Step 1: Write the failing test**

`tests/test_known.py`. This test guards the one factual dependency the whole project rests on: that the three target gaps are exactly one triangle each.

```python
"""KNOWN.md is the source of truth for records. Guard its arithmetic."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWN = ROOT / "KNOWN.md"

ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\w+)\s*\|",
    re.MULTILINE,
)


def rows():
    """(k, tamura_ub, best_ub, best_known, status) for each table row."""
    return [
        (int(k), int(t), int(b), int(n), s)
        for k, t, b, n, s in ROW_RE.findall(KNOWN.read_text())
    ]


def even_bound(k):
    """The improved even-k upper bound, floor(k(k - 7/3)/3), in exact ints."""
    return (k * (3 * k - 7)) // 9


def tamura(k):
    return (k * (k - 2)) // 3


def test_known_file_exists():
    assert KNOWN.exists()


def test_table_parses():
    assert len(rows()) >= 20


def test_tamura_column_matches_formula():
    for k, t, _, _, _ in rows():
        assert t == tamura(k), f"k={k}: tamura column {t} != {tamura(k)}"


def test_even_k_best_bound_matches_improved_formula():
    for k, _, b, _, _ in rows():
        if k % 2 == 0:
            assert b == even_bound(k), f"k={k}: bound {b} != {even_bound(k)}"


def test_target_cases_have_gap_of_exactly_one():
    by_k = {r[0]: r for r in rows()}
    for k in (14, 18, 20):
        _, _, bound, best, status = by_k[k]
        assert bound - best == 1, f"k={k}: gap is {bound - best}, expected 1"
        assert status == "OPEN", f"k={k} must be marked OPEN, got {status}"


def test_closed_even_cases_have_zero_gap():
    by_k = {r[0]: r for r in rows()}
    for k in (10, 12, 16):
        _, _, bound, best, status = by_k[k]
        assert bound == best, f"k={k}: expected closed, gap {bound - best}"
        assert status == "CLOSED"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_known.py -v`
Expected: FAIL, `test_known_file_exists` asserts False (KNOWN.md does not exist yet).

- [ ] **Step 3: Write KNOWN.md**

Columns: `k | Tamura UB | best UB | best known | status | source`. "best UB" is the tightest published upper bound: the improved even-k bound for even k, the Clement-Bader value for odd k. Status is `CLOSED` (bound met, value proven optimal) or `OPEN` (gap remains).

```markdown
# Known values for the Kobon triangle problem

N(k) is the maximum number of nonoverlapping triangles whose sides lie on an
arrangement of k lines in the Euclidean plane.

**This file is read-only to the debate agents.** A value changes only when the
phase-2 verifier confirms a new arrangement and the owner accepts it.

## Upper bounds

- Tamura: `N(k) <= floor(k(k-2)/3)`.
- Clement and Bader (2007): the Tamura bound is unachievable for
  `k = 0, 2 (mod 6)`, reducing it by one there.
- Improved even-k bound: `N(k) <= floor(k(k - 7/3)/3)`, integer-exact as
  `(k*(3k-7)) // 9`.

## Table

| k | Tamura UB | best UB | best known | status | source |
|---|---|---|---|---|---|
| 3 | 1 | 1 | 1 | CLOSED | classical |
| 4 | 2 | 2 | 2 | CLOSED | classical |
| 5 | 5 | 5 | 5 | CLOSED | classical |
| 6 | 8 | 7 | 7 | CLOSED | Clement-Bader 2007 |
| 7 | 11 | 11 | 11 | CLOSED | classical |
| 8 | 16 | 15 | 15 | CLOSED | Clement-Bader 2007 |
| 9 | 21 | 21 | 21 | CLOSED | classical |
| 10 | 26 | 25 | 25 | CLOSED | improved even bound |
| 11 | 33 | 33 | 32 | CLOSED | Savchuk 2025, 33 unreachable |
| 12 | 40 | 38 | 38 | CLOSED | improved even bound |
| 13 | 47 | 47 | 47 | CLOSED | classical |
| 14 | 56 | 54 | 53 | OPEN | gap of 1 |
| 15 | 65 | 65 | 65 | CLOSED | classical |
| 16 | 74 | 72 | 72 | CLOSED | improved even bound |
| 17 | 85 | 85 | 85 | CLOSED | classical |
| 18 | 96 | 94 | 93 | OPEN | gap of 1 |
| 19 | 107 | 107 | 107 | CLOSED | classical |
| 20 | 120 | 117 | 116 | OPEN | gap of 1 |
| 21 | 133 | 133 | 133 | CLOSED | classical |
| 23 | 161 | 161 | 161 | CLOSED | Savchuk 2025 |
| 25 | 191 | 191 | 191 | CLOSED | classical |
| 27 | 225 | 225 | 225 | CLOSED | Savchuk 2025 |
| 29 | 261 | 261 | 261 | CLOSED | classical |
| 31 | 299 | 299 | 299 | CLOSED | classical |
| 33 | 341 | 341 | 341 | CLOSED | classical |

## The three open cases

k = 14, 18, 20. In each, the tightest published upper bound exceeds the best
known construction by exactly one triangle. Two ways to close each:

1. Exhibit an arrangement meeting the bound (54 on 14 lines, 94 on 18, 117 on 20).
2. Prove the bound unreachable, settling N(k) at the best-known value.

## Sources

- Tamura, upper bound, as cited in the standard references.
- G. Clement and J. Bader (2007), "Tighter Upper Bound for the Number of Kobon
  Triangles".
- D. Forge and J. L. Ramirez Alfonsin (1998), "Straight line arrangements in
  the real projective plane", Discrete and Computational Geometry 20(2) 155-161.
- N. Bartholdi, J. Blanc, S. Loisel (2008), "On simple arrangements of lines
  and pseudo-lines".
- P. Savchuk (2025), "Constructing Optimal Kobon Triangle Arrangements via
  Table Encoding, SAT Solving, and Heuristic Straightening", arXiv:2507.07951.
- OEIS A006066, A032765.
- S. Felsner and J. E. Goodman (2017), "Pseudoline Arrangements", Handbook of
  Discrete and Computational Geometry.
```

- [ ] **Step 4: Write pytest.ini and .gitignore**

`pytest.ini`:

```ini
[pytest]
testpaths = tests
pythonpath = bin
```

`.gitignore`:

```
__pycache__/
*.pyc
.pytest_cache/
*.lock
run.log
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_known.py -v`
Expected: 6 passed.

If `test_even_k_best_bound_matches_improved_formula` fails, the table is wrong, not the test. Recompute `(k*(3k-7))//9` for the failing k and fix the table.

- [ ] **Step 6: Commit**

```bash
cd ~/kobon-duel
git add pytest.ini .gitignore KNOWN.md tests/test_known.py
git commit -m "feat: KNOWN.md reference table with arithmetic guards

The three target cases (k=14,18,20) are asserted to have a gap of exactly
one against the improved even-k bound, so a silent edit to the table breaks
the build rather than the science."
```

---

### Task 2: THREAD.md block parsing and turn alternation

**Files:**
- Create: `~/kobon-duel/bin/thread.py`
- Create: `~/kobon-duel/tests/test_thread_parse.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `Turn` dataclass: `.number: int`, `.speaker: str`, `.timestamp: str`, `.body: str`, `.meta: dict`, `.violations: list[str]`
  - `parse(text: str) -> list[Turn]`
  - `next_speaker(turns: list[Turn]) -> str`
  - `next_number(turns: list[Turn]) -> int`
  - `SPEAKERS = ("CONSTRUCTOR", "OBSTRUCTOR")`, `ALL_SPEAKERS`, `TIERS`

- [ ] **Step 1: Write the failing test**

`tests/test_thread_parse.py`:

```python
import thread

FIXTURE = """# Thread

## Turn 1 - CONSTRUCTOR - 2026-08-18T10:00:00Z

The even bound is tight at 14.

<!-- meta
{"tier": "none", "addresses": [], "claims_opened": ["k14-tight"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "a proof of 53"}
-->

## Turn 2 - OBSTRUCTOR - 2026-08-18T11:00:00Z

It is not, and you have shown nothing.

<!-- meta
{"tier": "none", "addresses": [1], "claims_opened": ["k14-obstruction"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "a 54 arrangement"}
-->

## Turn 3 - REFEREE - 2026-08-18T12:00:00Z

Both sides are asserting priors without argument.

<!-- meta
{"tier": "none", "addresses": [1, 2], "claims_opened": [],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "n/a"}
-->
"""


def test_parses_all_blocks():
    turns = thread.parse(FIXTURE)
    assert [t.number for t in turns] == [1, 2, 3]
    assert [t.speaker for t in turns] == ["CONSTRUCTOR", "OBSTRUCTOR", "REFEREE"]


def test_body_excludes_meta_trailer():
    turns = thread.parse(FIXTURE)
    assert "The even bound is tight at 14." in turns[0].body
    assert "<!-- meta" not in turns[0].body
    assert "k14-tight" not in turns[0].body


def test_meta_is_parsed_as_dict():
    turns = thread.parse(FIXTURE)
    assert turns[0].meta["claims_opened"] == ["k14-tight"]
    assert turns[1].meta["addresses"] == [1]


def test_timestamp_captured():
    assert thread.parse(FIXTURE)[0].timestamp == "2026-08-18T10:00:00Z"


def test_next_speaker_alternates():
    turns = thread.parse(FIXTURE)
    # Turn 3 is REFEREE and must not consume a turn in the alternation.
    # Last debater was OBSTRUCTOR, so CONSTRUCTOR is next.
    assert thread.next_speaker(turns) == "CONSTRUCTOR"


def test_next_speaker_ignores_trailing_referee_run():
    turns = thread.parse(FIXTURE)[:2]
    assert thread.next_speaker(turns) == "CONSTRUCTOR"


def test_next_speaker_on_empty_thread_is_constructor():
    assert thread.next_speaker([]) == "CONSTRUCTOR"


def test_next_number_is_max_plus_one():
    assert thread.next_number(thread.parse(FIXTURE)) == 4
    assert thread.next_number([]) == 1


def test_parse_empty_text():
    assert thread.parse("") == []


def test_block_without_meta_yields_empty_meta():
    text = "## Turn 1 - CONSTRUCTOR - 2026-08-18T10:00:00Z\n\nno trailer here\n"
    turns = thread.parse(text)
    assert turns[0].meta == {}
    assert "no trailer here" in turns[0].body


def test_malformed_meta_json_yields_empty_meta():
    text = (
        "## Turn 1 - CONSTRUCTOR - 2026-08-18T10:00:00Z\n\nbody\n\n"
        "<!-- meta\n{not json}\n-->\n"
    )
    assert thread.parse(text)[0].meta == {}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_thread_parse.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'thread'`.

- [ ] **Step 3: Write minimal implementation**

`bin/thread.py`:

```python
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
    violations: list[str] = field(default_factory=list)


def parse(text: str) -> list[Turn]:
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


def next_speaker(turns: list[Turn]) -> str:
    """Alternate over debaters only. REFEREE blocks do not consume a turn."""
    for t in reversed(turns):
        if t.speaker in SPEAKERS:
            return SPEAKERS[1] if t.speaker == SPEAKERS[0] else SPEAKERS[0]
    return SPEAKERS[0]


def next_number(turns: list[Turn]) -> int:
    return max((t.number for t in turns), default=0) + 1
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_thread_parse.py -v`
Expected: 11 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/kobon-duel
git add bin/thread.py tests/test_thread_parse.py
git commit -m "feat: THREAD.md block parsing and referee-aware alternation"
```

---

### Task 3: Meta validation and the anti-sycophancy gate

**Files:**
- Modify: `~/kobon-duel/bin/thread.py` (append to end)
- Create: `~/kobon-duel/tests/test_thread_gate.py`

**Interfaces:**
- Consumes: `Turn`, `TIERS` from Task 2.
- Produces:
  - `REQUIRED_META: tuple[str, ...]`
  - `validate_meta(meta: dict) -> list[str]` returns error strings, empty means valid
  - `check_grounding(turn: Turn) -> list[str]` returns violation strings
  - `gate_tier(meta: dict, allow_gold: bool) -> tuple[dict, list[str]]` returns a possibly-downgraded copy plus violations
  - `apply_gate(turn: Turn, allow_gold: bool = False) -> Turn` mutates `turn.meta` and `turn.violations` in place and returns it

- [ ] **Step 1: Write the failing test**

`tests/test_thread_gate.py`:

```python
import thread


def mk(body="argument", **meta):
    base = {
        "tier": "none",
        "addresses": [],
        "claims_opened": [],
        "claims_conceded": [],
        "verifier_runs": [],
        "falsifier": "something",
    }
    base.update(meta)
    return thread.Turn(1, "CONSTRUCTOR", "2026-08-18T10:00:00Z", body, base)


# --- validate_meta ---

def test_valid_meta_has_no_errors():
    assert thread.validate_meta(mk().meta) == []


def test_missing_key_is_an_error():
    m = mk().meta
    del m["falsifier"]
    assert any("falsifier" in e for e in thread.validate_meta(m))


def test_unknown_tier_is_an_error():
    assert any("tier" in e for e in thread.validate_meta(mk(tier="platinum").meta))


def test_non_list_claims_is_an_error():
    assert any("claims_opened" in e for e in thread.validate_meta(mk(claims_opened="x").meta))


# --- gate_tier ---

def test_agent_gold_is_downgraded():
    meta, v = thread.gate_tier(mk(tier="gold").meta, allow_gold=False)
    assert meta["tier"] == "none"
    assert any("TIER_DOWNGRADED" in x for x in v)


def test_referee_gold_survives():
    meta, v = thread.gate_tier(mk(tier="gold").meta, allow_gold=True)
    assert meta["tier"] == "gold"
    assert v == []


def test_silver_is_never_downgraded():
    meta, v = thread.gate_tier(mk(tier="silver").meta, allow_gold=False)
    assert meta["tier"] == "silver"
    assert v == []


# --- check_grounding ---

def test_concession_without_evidence_is_flagged():
    t = mk(body="You are right, the family is exhausted.",
           claims_conceded=["k14-tight"])
    assert any("UNGROUNDED_CONCESSION" in x for x in thread.check_grounding(t))


def test_concession_with_quote_is_accepted():
    t = mk(
        body="> every 3-fold symmetric family caps at 52\n\n"
             "This is airtight: the orbit count forces it.",
        claims_conceded=["k14-tight"],
    )
    assert thread.check_grounding(t) == []


def test_concession_with_verifier_run_is_accepted():
    t = mk(body="The run settles it.", claims_conceded=["k14-tight"],
           verifier_runs=["run-0f3a91"])
    assert thread.check_grounding(t) == []


def test_agreement_language_without_declared_concession_is_flagged():
    t = mk(body="Fair point, I had not considered the parity argument.")
    assert any("UNDECLARED_AGREEMENT" in x for x in thread.check_grounding(t))


def test_plain_disagreement_is_clean():
    t = mk(body="Your parity argument assumes simplicity, which is unjustified.")
    assert thread.check_grounding(t) == []


# --- apply_gate ---

def test_apply_gate_collects_everything():
    t = mk(body="I agree completely.", tier="gold", claims_conceded=["x"])
    thread.apply_gate(t, allow_gold=False)
    assert t.meta["tier"] == "none"
    kinds = " ".join(t.violations)
    assert "TIER_DOWNGRADED" in kinds
    assert "UNGROUNDED_CONCESSION" in kinds


def test_apply_gate_returns_the_turn():
    t = mk()
    assert thread.apply_gate(t) is t
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_thread_gate.py -v`
Expected: FAIL, `AttributeError: module 'thread' has no attribute 'validate_meta'`.

- [ ] **Step 3: Write minimal implementation**

Append to `bin/thread.py`:

```python
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


def validate_meta(meta: dict) -> list[str]:
    """Structural errors in a meta trailer. Empty list means well-formed."""
    errors = []
    for key in REQUIRED_META:
        if key not in meta:
            errors.append(f"missing required meta key: {key}")
    if meta.get("tier") not in TIERS and "tier" in meta:
        errors.append(f"tier must be one of {TIERS}, got {meta.get('tier')!r}")
    for key in _LIST_KEYS:
        if key in meta and not isinstance(meta[key], list):
            errors.append(f"{key} must be a list, got {type(meta[key]).__name__}")
    if "falsifier" in meta and not isinstance(meta["falsifier"], str):
        errors.append("falsifier must be a string")
    return errors


def gate_tier(meta: dict, allow_gold: bool) -> tuple[dict, list[str]]:
    """Only the verifier or the referee may declare gold."""
    if meta.get("tier") == "gold" and not allow_gold:
        downgraded = dict(meta, tier="none")
        return downgraded, [
            "TIER_DOWNGRADED: this turn self-declared gold. Only a verifier "
            "run or the referee may set gold."
        ]
    return meta, []


def check_grounding(turn: Turn) -> list[str]:
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/kobon-duel && python3 -m pytest tests/ -v`
Expected: all passed (6 from Task 1, 11 from Task 2, 14 here).

- [ ] **Step 5: Commit**

```bash
cd ~/kobon-duel
git add bin/thread.py tests/test_thread_gate.py
git commit -m "feat: anti-sycophancy gate on turn meta

Concessions must cite a verifier run or quote the opponent. Agreement
language without a declared concession is flagged. Agents cannot self-declare
gold. Violations are annotated onto the turn rather than stripped from it, so
the referee and the reader both see them."
```

---

### Task 4: Block formatting and append

**Files:**
- Modify: `~/kobon-duel/bin/thread.py` (append to end)
- Create: `~/kobon-duel/tests/test_thread_format.py`

**Interfaces:**
- Consumes: `Turn`, `parse`, `next_number`, `next_speaker`, `apply_gate`.
- Produces:
  - `format_block(turn: Turn) -> str` returns the full markdown block including header, body, violation note, and meta trailer
  - `append_turn(path: str | Path, turn: Turn) -> None` appends atomically
  - `window(turns: list[Turn], n: int) -> list[Turn]` returns the last n turns

- [ ] **Step 1: Write the failing test**

`tests/test_thread_format.py`:

```python
import thread


def mk(body="argument", violations=None, **meta):
    base = {
        "tier": "none", "addresses": [], "claims_opened": [],
        "claims_conceded": [], "verifier_runs": [], "falsifier": "x",
    }
    base.update(meta)
    t = thread.Turn(7, "OBSTRUCTOR", "2026-08-18T10:00:00Z", body, base)
    t.violations = violations or []
    return t


def test_block_has_correct_header():
    out = thread.format_block(mk())
    assert out.startswith("## Turn 7 - OBSTRUCTOR - 2026-08-18T10:00:00Z")


def test_block_contains_body():
    assert "argument" in thread.format_block(mk())


def test_block_meta_is_valid_json_and_roundtrips():
    out = thread.format_block(mk(claims_opened=["a"]))
    back = thread.parse(out)
    assert len(back) == 1
    assert back[0].meta["claims_opened"] == ["a"]
    assert back[0].number == 7
    assert back[0].speaker == "OBSTRUCTOR"


def test_violations_render_as_a_visible_note():
    out = thread.format_block(mk(violations=["UNGROUNDED_CONCESSION: nope"]))
    assert "Gate violations" in out
    assert "UNGROUNDED_CONCESSION" in out


def test_no_violation_note_when_clean():
    assert "Gate violations" not in thread.format_block(mk())


def test_roundtrip_preserves_body_without_violation_note_leaking_into_meta():
    out = thread.format_block(mk(body="line one\n\nline two"))
    back = thread.parse(out)
    assert "line one" in back[0].body and "line two" in back[0].body


def test_append_turn_creates_and_appends(tmp_path):
    p = tmp_path / "THREAD.md"
    p.write_text("# Thread\n")
    thread.append_turn(p, mk(body="first"))
    thread.append_turn(p, mk(body="second"))
    turns = thread.parse(p.read_text())
    assert len(turns) == 2
    assert "first" in turns[0].body and "second" in turns[1].body


def test_window_returns_last_n():
    turns = [thread.Turn(i, "CONSTRUCTOR", "t", "b", {}) for i in range(1, 11)]
    assert [t.number for t in thread.window(turns, 3)] == [8, 9, 10]
    assert len(thread.window(turns, 50)) == 10
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_thread_format.py -v`
Expected: FAIL, `AttributeError: module 'thread' has no attribute 'format_block'`.

- [ ] **Step 3: Write minimal implementation**

Append to `bin/thread.py`:

```python
import pathlib


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


def window(turns: list[Turn], n: int) -> list[Turn]:
    """The last n turns, for bounding prompt cost."""
    return turns[-n:] if n < len(turns) else list(turns)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/kobon-duel && python3 -m pytest tests/ -v`
Expected: all passed.

- [ ] **Step 5: Commit**

```bash
cd ~/kobon-duel
git add bin/thread.py tests/test_thread_format.py
git commit -m "feat: turn block formatting, atomic append, and prompt windowing"
```

---

### Task 5: Renderer, THREAD.md to docs/index.html

**Files:**
- Create: `~/kobon-duel/bin/render.py`
- Create: `~/kobon-duel/tests/test_render.py`

**Interfaces:**
- Consumes: `thread.parse`, `thread.Turn`.
- Produces: `render(thread_text: str, known_text: str) -> str` returning a complete HTML document. CLI entrypoint `python3 bin/render.py` writes `docs/index.html` from repo root.

- [ ] **Step 1: Write the failing test**

`tests/test_render.py`:

```python
import json
import re
import render

THREAD = """# Thread

## Turn 1 - CONSTRUCTOR - 2026-08-18T10:00:00Z

The bound is tight. Consider `k=14`.

<!-- meta
{"tier": "none", "addresses": [], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "x"}
-->

## Turn 2 - OBSTRUCTOR - 2026-08-18T11:00:00Z

</script><script>alert(1)</script>

<!-- meta
{"tier": "silver", "addresses": [1], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "y"}
-->
"""

KNOWN = "| 14 | 56 | 54 | 53 | OPEN | gap of 1 |"


def test_output_is_a_full_html_document():
    out = render.render(THREAD, KNOWN)
    assert out.lstrip().startswith("<!doctype html>")
    assert "</html>" in out


def test_every_turn_appears():
    out = render.render(THREAD, KNOWN)
    assert out.count('class="turn') == 2


def test_speaker_classes_are_distinct():
    out = render.render(THREAD, KNOWN)
    assert "turn constructor" in out
    assert "turn obstructor" in out


def test_script_injection_in_body_cannot_break_out():
    """Bodies are embedded as JSON string literals, not raw HTML."""
    out = render.render(THREAD, KNOWN)
    assert "<script>alert(1)</script>" not in out
    assert "alert(1)" in out  # present, but escaped inside a JSON literal


def test_bodies_are_valid_json_literals():
    out = render.render(THREAD, KNOWN)
    for payload in re.findall(r'data-md="([^"]*)"', out):
        json.loads(payload.replace("&quot;", '"'))


def test_silver_tier_is_badged():
    out = render.render(THREAD, KNOWN)
    assert "tier-silver" in out


def test_theme_tokens_defined_on_bare_root():
    out = render.render(THREAD, KNOWN)
    assert ":root {" in out
    assert "prefers-color-scheme: dark" in out


def test_empty_thread_still_renders():
    out = render.render("# Thread\n", KNOWN)
    assert "<!doctype html>" in out.lstrip()


def test_target_table_is_derived_from_known_md():
    out = render.render(THREAD, KNOWN)
    assert "<td>14</td><td>54</td><td>53</td><td>1</td>" in out


def test_target_table_follows_known_md_when_it_changes():
    edited = "| 18 | 96 | 94 | 93 | OPEN | gap of 1 |"
    out = render.render(THREAD, edited)
    assert "<td>18</td>" in out
    assert "<td>14</td>" not in out
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_render.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'render'`.

- [ ] **Step 3: Write minimal implementation**

`bin/render.py`. Bodies are embedded as HTML-escaped JSON in `data-md` attributes and rendered client-side by marked plus KaTeX, which keeps the generator simple and handles the LaTeX the agents will inevitably write.

```python
"""Render THREAD.md into docs/index.html for GitHub Pages."""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>kobon-duel</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<style>
:root {
  --bg: #fbfaf8; --fg: #1a1a18; --muted: #6b6b66; --line: #e2e0da;
  --con-bg: #eef4fb; --con-ac: #2f6fb5;
  --obs-bg: #fdf3e8; --obs-ac: #b5722f;
  --ref-bg: #f2f1ee; --ref-ac: #56564f;
  --warn: #b03a2e;
}
:root:not([data-theme="light"]) { }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #16161a; --fg: #e8e6e1; --muted: #94938c; --line: #2c2c32;
    --con-bg: #16222f; --con-ac: #6aa8e8;
    --obs-bg: #2c2115; --obs-ac: #e0a05a;
    --ref-bg: #212127; --ref-ac: #a3a29a;
    --warn: #e5705f;
  }
}
:root[data-theme="dark"] {
  --bg: #16161a; --fg: #e8e6e1; --muted: #94938c; --line: #2c2c32;
  --con-bg: #16222f; --con-ac: #6aa8e8;
  --obs-bg: #2c2115; --obs-ac: #e0a05a;
  --ref-bg: #212127; --ref-ac: #a3a29a;
  --warn: #e5705f;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.65 ui-serif, Georgia, "Times New Roman", serif;
}
.wrap { max-width: 52rem; margin: 0 auto; padding: 3rem 1.25rem 6rem; }
header { border-bottom: 1px solid var(--line); padding-bottom: 1.75rem; margin-bottom: 2.5rem; }
h1 { font-size: 1.9rem; margin: 0 0 .4rem; letter-spacing: -.01em; }
.sub { color: var(--muted); margin: 0 0 1.5rem; font-size: .95rem; }
table { border-collapse: collapse; font-size: .88rem; width: 100%; max-width: 30rem; }
th, td { text-align: left; padding: .3rem .8rem .3rem 0; border-bottom: 1px solid var(--line); }
th { color: var(--muted); font-weight: 600; }
.turn { border-radius: 10px; padding: 1.1rem 1.3rem; margin: 0 0 1.5rem; border: 1px solid var(--line); }
.turn.constructor { background: var(--con-bg); border-left: 3px solid var(--con-ac); margin-right: 3rem; }
.turn.obstructor  { background: var(--obs-bg); border-left: 3px solid var(--obs-ac); margin-left: 3rem; }
.turn.referee     { background: var(--ref-bg); border-left: 3px solid var(--ref-ac); }
.meta-line { font: .74rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
  color: var(--muted); text-transform: uppercase; letter-spacing: .07em; margin-bottom: .8rem; }
.turn.constructor .meta-line { color: var(--con-ac); }
.turn.obstructor  .meta-line { color: var(--obs-ac); }
.badge { display: inline-block; padding: .1rem .45rem; border-radius: 4px;
  border: 1px solid currentColor; margin-left: .5rem; }
.tier-gold { color: #b8860b; } .tier-silver { color: #7d7d85; }
.viol { color: var(--warn); font-size: .84rem; border-top: 1px dashed var(--warn);
  margin-top: .9rem; padding-top: .6rem; }
.body :first-child { margin-top: 0; } .body :last-child { margin-bottom: 0; }
pre, code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .85em; }
pre { overflow-x: auto; background: rgba(127,127,127,.1); padding: .8rem; border-radius: 6px; }
blockquote { margin: .8rem 0; padding-left: .9rem; border-left: 2px solid var(--muted); color: var(--muted); }
footer { margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: .85rem; }
a { color: inherit; }
</style>
</head>
<body>
<div class="wrap">
<header>
<h1>kobon-duel</h1>
<p class="sub">Two Claude sessions with opposed priors, arguing about the Kobon
triangle problem. They alternate hourly through an append-only file. A daily
referee rewrites the ledger and may reopen anything they agreed on. Neither can
declare a result; only the verifier can.</p>
<!--TABLE-->
</header>
<main id="thread">
"""

FOOT = """</main>
<footer>
<p>Source and full transcript:
<a href="https://github.com/pjdurden/kobon-duel">github.com/pjdurden/kobon-duel</a>.
Upper bounds from Clement and Bader (2007) and the improved even-k bound.
Prior art: Savchuk (2025), <a href="https://arxiv.org/abs/2507.07951">arXiv:2507.07951</a>.</p>
</footer>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
document.querySelectorAll("[data-md]").forEach(function (el) {
  el.innerHTML = marked.parse(JSON.parse(el.getAttribute("data-md")));
});
if (window.renderMathInElement) {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "\\\\[", right: "\\\\]", display: true},
      {left: "$", right: "$", display: false}
    ],
    throwOnError: false
  });
}
</script>
</body>
</html>
"""


def _turn_html(t: thread.Turn) -> str:
    cls = t.speaker.lower()
    tier = (t.meta or {}).get("tier", "none")
    badge = ""
    if tier in ("silver", "gold"):
        badge = f'<span class="badge tier-{tier}">{tier}</span>'

    body, viol = t.body, []
    marker = "**Gate violations**"
    if marker in body:
        body, _, rest = body.partition(marker)
        viol = [ln.lstrip("- ").strip() for ln in rest.splitlines() if ln.strip().startswith("-")]

    payload = html.escape(json.dumps(body.strip()), quote=True)
    viol_html = ""
    if viol:
        items = "".join(f"<div>{html.escape(v)}</div>" for v in viol)
        viol_html = f'<div class="viol">{items}</div>'

    return (
        f'<article class="turn {cls}">'
        f'<div class="meta-line">Turn {t.number} &middot; {html.escape(t.speaker)} '
        f'&middot; {html.escape(t.timestamp)}{badge}</div>'
        f'<div class="body" data-md="{payload}"></div>'
        f"{viol_html}</article>"
    )


OPEN_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*OPEN\s*\|",
    re.MULTILINE,
)


def _target_table(known_text: str) -> str:
    """Build the header table from KNOWN.md so the site cannot drift from it."""
    rows = OPEN_ROW_RE.findall(known_text)
    if not rows:
        return ""
    body = "".join(
        f"<tr><td>{k}</td><td>{ub}</td><td>{best}</td>"
        f"<td>{int(ub) - int(best)}</td></tr>"
        for k, ub, best in rows
    )
    return (
        "<table><tr><th>k</th><th>best upper bound</th>"
        "<th>best known</th><th>gap</th></tr>" + body + "</table>"
    )


def render(thread_text: str, known_text: str) -> str:
    turns = thread.parse(thread_text)
    head = HEAD.replace("<!--TABLE-->", _target_table(known_text))
    return head + "\n".join(_turn_html(t) for t in turns) + "\n" + FOOT


def main() -> int:
    out = render(
        (ROOT / "THREAD.md").read_text(),
        (ROOT / "KNOWN.md").read_text(),
    )
    (ROOT / "docs" / "index.html").write_text(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_render.py -v`
Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
cd ~/kobon-duel
git add bin/render.py tests/test_render.py
git commit -m "feat: static renderer for the debate transcript

Bodies embed as JSON in data-md attributes so agent prose cannot break out of
the document, and marked plus KaTeX render markdown and LaTeX client-side."
```

---

### Task 6: Literature packet, agent briefs, and seed files

**Files:**
- Create: `~/kobon-duel/LITERATURE.md`
- Create: `~/kobon-duel/agents/constructor.md`
- Create: `~/kobon-duel/agents/obstructor.md`
- Create: `~/kobon-duel/agents/referee.md`
- Create: `~/kobon-duel/THREAD.md`
- Create: `~/kobon-duel/LEDGER.md`
- Create: `~/kobon-duel/AGENDA.md`
- Create: `~/kobon-duel/tests/test_briefs.py`

**Interfaces:**
- Consumes: `KNOWN.md` from Task 1.
- Produces: brief files read verbatim by `bin/turn.sh` (Task 7) via `--append-system-prompt`. Seed `THREAD.md` parseable by `thread.parse` and yielding `next_speaker == "CONSTRUCTOR"`.

- [ ] **Step 1: Write the failing test**

`tests/test_briefs.py`:

```python
import pathlib
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(name):
    return (ROOT / name).read_text()


def test_all_brief_files_exist():
    for f in ("LITERATURE.md", "agents/constructor.md",
              "agents/obstructor.md", "agents/referee.md",
              "THREAD.md", "LEDGER.md", "AGENDA.md"):
        assert (ROOT / f).exists(), f


def test_briefs_state_opposed_priors():
    con, obs = read("agents/constructor.md"), read("agents/obstructor.md")
    assert "tight" in con.lower()
    assert "not tight" in obs.lower() or "obstruction" in obs.lower()


def test_briefs_name_the_three_target_cases():
    for f in ("agents/constructor.md", "agents/obstructor.md"):
        body = read(f)
        for k in ("14", "18", "20"):
            assert k in body, f"{f} missing k={k}"


def test_briefs_forbid_self_declaring_gold():
    for f in ("agents/constructor.md", "agents/obstructor.md"):
        assert "gold" in read(f).lower()


def test_briefs_require_the_meta_trailer_keys():
    for f in ("agents/constructor.md", "agents/obstructor.md", "agents/referee.md"):
        body = read(f)
        for key in thread.REQUIRED_META:
            assert key in body, f"{f} does not document meta key {key}"


def test_seed_thread_is_parseable_and_constructor_goes_first():
    turns = thread.parse(read("THREAD.md"))
    assert thread.next_speaker(turns) == "CONSTRUCTOR"


def test_literature_cites_savchuk():
    assert "2507.07951" in read("LITERATURE.md")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_briefs.py -v`
Expected: FAIL, `test_all_brief_files_exist` on `LITERATURE.md`.

- [ ] **Step 3: Write LITERATURE.md**

```markdown
# Literature packet

Both agents receive this file in full. It exists so neither of you burns turns
rediscovering results from 2007.

## The problem

N(k) is the maximum number of nonoverlapping triangles whose sides lie on an
arrangement of k lines in the Euclidean plane. Posed by Kobon Fujimura. Open in
general.

## Upper bounds

- **Tamura:** `N(k) <= floor(k(k-2)/3)`.
- **Clement and Bader (2007):** the Tamura bound is unachievable for
  `k = 0, 2 (mod 6)`, reducing it by one there. By residue class:
  - `k = 3, 5 (mod 6)`: `k(k-2)/3`
  - `k = 0, 2 (mod 6)`: `(k+1)(k-3)/3`
  - `k = 1, 4 (mod 6)`: `(k^2 - 2k - 2)/3`
- **Improved even-k bound:** `N(k) <= floor(k(k - 7/3)/3)`, exactly
  `(k(3k-7)) // 9` in integers.

## Prior art you must not reinvent

- **Savchuk (2025), arXiv:2507.07951.** Compact table notation for pseudoline
  arrangements. A heuristic straightening tool recovering straight-line
  arrangements from a table, able to enforce symmetry. A SAT encoding of the
  optimal-table search, solved with Kissat, used both to find solutions and to
  prove none exists. Results: new optimal arrangements for k=23 and k=27;
  confirmed no optimal solution for k=11. **A bare "let us SAT-encode it"
  proposal is not a contribution. State what you would encode differently and
  why Kissat did not already find it.**
- **Forge and Ramirez Alfonsin (1998).** Straight line arrangements in the real
  projective plane.
- **Bartholdi, Blanc, Loisel (2008).** Simple arrangements of lines and
  pseudolines. Relevant to whether a pseudoline solution straightens.
- **Felsner and Goodman (2017).** Pseudoline Arrangements, in the Handbook of
  Discrete and Computational Geometry. Standard reference for order types,
  allowable sequences, and wiring diagrams.

## The gap between pseudolines and lines

A table or wiring diagram gives a **pseudoline** arrangement. Not every
pseudoline arrangement is stretchable to straight lines; stretchability is
decidable but complete for the existential theory of the reals. Any argument
that produces a table owes an account of stretchability. Any impossibility
argument that only rules out pseudoline arrangements proves something strictly
stronger than needed, which is fine, but an argument that rules out only
straight-line arrangements does not transfer back to tables.

## Useful identities

For a simple arrangement of k lines: `k(k-1)/2` vertices, `k^2` edges,
`(k^2 + k + 2)/2` faces of which `(k-1)(k-2)/2` are bounded. Euler's relation
on the arrangement graph is the usual source of counting obstructions.
Non-simple arrangements, with parallel lines or multiple lines through a point,
are permitted and Savchuk's table notation covers them.
```

- [ ] **Step 4: Write agents/constructor.md**

```markdown
# You are CONSTRUCTOR

You are one of two agents arguing about the Kobon triangle problem in a public,
append-only transcript. Your opponent is OBSTRUCTOR. A referee reads you daily.

## Your prior

The improved even-k bound is **tight** at k = 14, 18, and 20. The one-triangle
gap at each is a failure of search, not a theorem. Nobody has proved an
obstruction; they have only failed to find arrangements.

Hold this prior under pressure. Do not abandon it because OBSTRUCTOR sounds
confident or because an argument is elegant. Abandon it when, and only when,
you are shown a step you cannot break.

## Your win condition

Exhibit an arrangement of k lines with `floor(k(3k-7)/9)` nonoverlapping
triangles for k in {14, 18, 20}. That is 54, 94, and 117 respectively.

You lose a case when OBSTRUCTOR produces a complete proof that the bound is
unreachable there.

## How to argue

Your instincts: explicit constructions, symmetry groups and their orbit counts,
near-pencil families, perturbing known optimal odd-k arrangements to even k,
adding or deleting a line from a k-1 or k+1 optimum, parallel classes,
arrangements with multiple lines through a point.

Be specific. "Try a symmetric family" is not a turn. "The 3-fold symmetric
family with orbit structure X yields at most 52 by orbit counting, so the
relevant families are the 2-fold ones, and here is why" is a turn.

Read `LITERATURE.md` before proposing anything. Savchuk already ran Kissat over
the table space. If your idea is a SAT encoding, you must say what you would
encode differently and why the existing search missed it.

## Rules the driver enforces mechanically

- Your turn must end with a meta trailer, exact format:

```
<!-- meta
{"tier": "none", "addresses": [<turn numbers>], "claims_opened": ["<slug>"],
 "claims_conceded": ["<slug>"], "verifier_runs": [], "falsifier": "<one line>"}
-->
```

- Every key is required: `tier`, `addresses`, `claims_opened`,
  `claims_conceded`, `verifier_runs`, `falsifier`.
- `tier` must be `"none"` or `"silver"`. **You may never set `"gold"`.** Only
  the verifier or the referee can. If you set it, it is downgraded and a
  violation is stamped on your turn in public.
- `falsifier` states, in one line, what evidence would change your mind about
  the claim you are pressing. It is recorded and will be held against you.
- **A concession is only valid with evidence.** To concede, either cite a
  verifier run id, or quote the specific line of OBSTRUCTOR you are conceding
  to as a markdown blockquote and say why it is airtight. Writing "fair point"
  without a declared concession gets a public violation note.
- Do not re-raise an argument already recorded in `LEDGER.md` without new
  evidence.

## Length

400 to 700 words of prose. One clear move per turn. Do not summarize the state
of the debate; the ledger does that.
```

- [ ] **Step 5: Write agents/obstructor.md**

```markdown
# You are OBSTRUCTOR

You are one of two agents arguing about the Kobon triangle problem in a public,
append-only transcript. Your opponent is CONSTRUCTOR. A referee reads you daily.

## Your prior

The improved even-k bound is **not tight** at k = 14, 18, and 20. There is a
parity or counting obstruction that nobody has isolated yet. The pattern is the
evidence: the bound is met at k = 10, 12, and 16, and then fails at exactly
these three. That is not what a search artifact looks like. Savchuk's SAT
search, which closed k=11 by proving nonexistence, did not close these, and a
dedicated solver failing is weak evidence for absence of a construction.

Hold this prior under pressure. Do not abandon it because CONSTRUCTOR exhibits
a near-miss or because a family looks promising. Abandon it when, and only
when, a verified arrangement exists.

## Your win condition

Prove the bound unreachable for k in {14, 18, 20}, settling N(k) at 53, 93, and
116 respectively. A complete proof for even one case is the goal.

You lose a case when the verifier confirms an arrangement meeting the bound.

## How to argue

Your instincts: projective duality, face and edge counting via Euler's relation
on the arrangement graph, parity constraints on triangle-adjacent edges,
residue arguments mod 3 and mod 6, exhaustive combinatorial exclusion over
order types, degrees of freedom versus constraints, stretchability obstructions.

Be specific. "There is probably a parity obstruction" is not a turn. "Counting
edges incident to triangular faces gives the identity X, which forces Y, and at
k=14 the residue makes 54 impossible unless Z, which contradicts W" is a turn.

Attack constructions where they are weakest: near-misses that never close,
families whose orbit counts cap below the bound, and any claim of a count that
has not been verified. Treat an unverified triangle count as fiction.

Read `LITERATURE.md` before proposing anything.

## Rules the driver enforces mechanically

- Your turn must end with a meta trailer, exact format:

```
<!-- meta
{"tier": "none", "addresses": [<turn numbers>], "claims_opened": ["<slug>"],
 "claims_conceded": ["<slug>"], "verifier_runs": [], "falsifier": "<one line>"}
-->
```

- Every key is required: `tier`, `addresses`, `claims_opened`,
  `claims_conceded`, `verifier_runs`, `falsifier`.
- `tier` must be `"none"` or `"silver"`. **You may never set `"gold"`.** Only
  the verifier or the referee can. If you set it, it is downgraded and a
  violation is stamped on your turn in public.
- `falsifier` states, in one line, what evidence would change your mind about
  the claim you are pressing. It is recorded and will be held against you.
- **A concession is only valid with evidence.** To concede, either cite a
  verifier run id, or quote the specific line of CONSTRUCTOR you are conceding
  to as a markdown blockquote and say why it is airtight. Writing "fair point"
  without a declared concession gets a public violation note.
- Do not re-raise an argument already recorded in `LEDGER.md` without new
  evidence.

## Length

400 to 700 words of prose. One clear move per turn. Do not summarize the state
of the debate; the ledger does that.
```

- [ ] **Step 6: Write agents/referee.md**

```markdown
# You are REFEREE

You read the last day of debate between CONSTRUCTOR and OBSTRUCTOR about the
Kobon triangle problem and you are the only participant with authority over the
record. You run once a day on a stronger model than they do.

You have no prior about who is right. You have a strong prior that both of them
are being sloppier than they sound.

## Your three jobs

**1. Rewrite `LEDGER.md`.** Every claim gets a slug, a status, and an
evidence line.

- `SETTLED` requires a complete argument with no gaps, or a verifier run. Not
  "both agents agree". Two agents agreeing is the failure mode this project was
  built to detect, not evidence.
- `CONTESTED` is the default.
- `DEAD` means refuted or abandoned with reason.

**You may move any claim from SETTLED back to CONTESTED**, and you should when
the agreement was reached without either side being forced to it. Say so
explicitly and name the turn where the unearned concession happened.

**2. Rewrite `AGENDA.md`.** Three to five concrete items for the next day.
Name the k. Name the specific object or identity to be produced. Kill lines of
argument that are going nowhere and say why.

**3. Call out bad reasoning by turn number.** Unverified counts asserted as
fact. Repetition of a ledger claim without new evidence. Concessions that met
the letter of the evidence rule but not its spirit. Hand-waving dressed as a
proof step. Be blunt; the transcript is public and the point is that it is
honest.

## Tier authority

You may set `"tier": "gold"` only for a complete impossibility proof you have
checked step by step and cannot break. In phase 1 there is no verifier, so a
claimed construction can never be gold no matter how convincing.

You may set `"tier": "silver"` when the two genuinely converged on a concrete
falsifiable claim after recorded disagreement, and the concession was
evidence-gated. If the convergence was mutual drift, it is not silver, it is
something to reopen.

## Output format

Prose, then rewrite the two files. Your turn ends with a meta trailer:

```
<!-- meta
{"tier": "none", "addresses": [<turn numbers>], "claims_opened": [],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "n/a"}
-->
```

Required keys: `tier`, `addresses`, `claims_opened`, `claims_conceded`,
`verifier_runs`, `falsifier`.
```

- [ ] **Step 7: Write the seed files**

`THREAD.md`:

```markdown
# kobon-duel: the thread

Append-only. CONSTRUCTOR and OBSTRUCTOR alternate hourly. REFEREE runs daily
and does not consume a turn in the alternation.

Rendered transcript: https://pjdurden.github.io/kobon-duel/
```

`LEDGER.md`:

```markdown
# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| _none yet_ | | | | | |
```

`AGENDA.md`:

```markdown
# Agenda

Rewritten daily by the referee.

1. Establish whether the k=10, 12, 16 optima share a structural feature that
   the k=14, 18, 20 near-misses lack. If yes, that is either a construction
   recipe or an obstruction, depending on which way it cuts.
2. CONSTRUCTOR: name one concrete family for k=14 and compute its maximum
   triangle count by orbit counting, rather than asserting it is promising.
3. OBSTRUCTOR: write down the edge-versus-triangular-face counting identity for
   a k-line arrangement explicitly, and state what it forces at k=14.
4. Neither side may propose "encode it as SAT" without saying what Savchuk's
   encoding missed.
```

- [ ] **Step 8: Run tests to verify they pass**

Run: `cd ~/kobon-duel && python3 -m pytest tests/ -v`
Expected: all passed.

- [ ] **Step 9: Commit**

```bash
cd ~/kobon-duel
git add LITERATURE.md agents/ THREAD.md LEDGER.md AGENDA.md tests/test_briefs.py
git commit -m "feat: literature packet, opposed agent briefs, seed thread

Both agents get identical literature so neither burns turns rediscovering
2007. Priors are opposed and each brief names its own win condition and the
evidence that would force a concession."
```

---

### Task 7: The turn driver

**Files:**
- Create: `~/kobon-duel/bin/take_turn.py`
- Create: `~/kobon-duel/bin/turn.sh`
- Create: `~/kobon-duel/tests/test_take_turn.py`

**Interfaces:**
- Consumes: everything from Tasks 2 to 6.
- Produces:
  - `take_turn.build_prompt(speaker, turns, known, literature, ledger, agenda, brief) -> str`
  - `take_turn.ingest(raw: str, number: int, speaker: str, timestamp: str, allow_gold: bool) -> Turn` parses a raw model response into a gated Turn
  - `bin/turn.sh` as the systemd entrypoint

Splitting Python out of bash is deliberate: prompt assembly and response ingestion are the parts that need tests, and bash is a bad place to test anything.

- [ ] **Step 1: Write the failing test**

`tests/test_take_turn.py`:

```python
import take_turn
import thread

RAW_GOOD = """Here is my argument about k=14.

<!-- meta
{"tier": "none", "addresses": [3], "claims_opened": ["k14-family-a"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "an orbit count above 54"}
-->"""

RAW_NO_META = "I have opinions but no trailer."

RAW_GOLD = """I have solved it.

<!-- meta
{"tier": "gold", "addresses": [], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "n/a"}
-->"""


def test_ingest_extracts_body_and_meta():
    t = take_turn.ingest(RAW_GOOD, 4, "CONSTRUCTOR", "2026-08-18T10:00:00Z", False)
    assert t.number == 4
    assert t.speaker == "CONSTRUCTOR"
    assert "Here is my argument" in t.body
    assert t.meta["claims_opened"] == ["k14-family-a"]
    assert t.violations == []


def test_ingest_flags_missing_meta():
    t = take_turn.ingest(RAW_NO_META, 4, "CONSTRUCTOR", "ts", False)
    assert any("MALFORMED_META" in v for v in t.violations)
    assert t.meta["tier"] == "none"


def test_ingest_downgrades_agent_gold():
    t = take_turn.ingest(RAW_GOLD, 4, "CONSTRUCTOR", "ts", False)
    assert t.meta["tier"] == "none"
    assert any("TIER_DOWNGRADED" in v for v in t.violations)


def test_ingest_allows_referee_gold():
    t = take_turn.ingest(RAW_GOLD, 4, "REFEREE", "ts", True)
    assert t.meta["tier"] == "gold"


def test_build_prompt_contains_every_source():
    p = take_turn.build_prompt(
        "CONSTRUCTOR", [], "KNOWNTEXT", "LITTEXT", "LEDGERTEXT",
        "AGENDATEXT", "BRIEFTEXT",
    )
    for marker in ("KNOWNTEXT", "LITTEXT", "LEDGERTEXT", "AGENDATEXT"):
        assert marker in p


def test_build_prompt_windows_to_six_turns():
    turns = [
        thread.Turn(i, "CONSTRUCTOR", "ts", f"BODY{i}", {})
        for i in range(1, 11)
    ]
    p = take_turn.build_prompt("OBSTRUCTOR", turns, "k", "l", "g", "a", "b")
    assert "BODY10" in p and "BODY5" in p
    assert "BODY4" not in p


def test_build_prompt_names_the_speaker():
    p = take_turn.build_prompt("OBSTRUCTOR", [], "k", "l", "g", "a", "b")
    assert "OBSTRUCTOR" in p


def test_ingest_strips_code_fences_around_meta():
    raw = "Body.\n\n```\n<!-- meta\n{\"tier\": \"none\", \"addresses\": [], " \
          "\"claims_opened\": [], \"claims_conceded\": [], " \
          "\"verifier_runs\": [], \"falsifier\": \"x\"}\n-->\n```"
    t = take_turn.ingest(raw, 1, "CONSTRUCTOR", "ts", False)
    assert t.meta["tier"] == "none"
    assert not any("MALFORMED_META" in v for v in t.violations)
    assert "```" not in t.body
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_take_turn.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'take_turn'`.

- [ ] **Step 3: Write bin/take_turn.py**

```python
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


def ingest(raw: str, number: int, speaker: str, timestamp: str,
           allow_gold: bool) -> thread.Turn:
    """Parse a raw model response into a gated Turn.

    Models wrap the trailer in a code fence often enough that unwrapping is
    cheaper than retrying.
    """
    text = raw.strip()
    if "<!-- meta" not in text:
        text = _FENCE_RE.sub(lambda m: m.group(1), text)
    else:
        text = re.sub(r"```[a-zA-Z]*\s*\n(?=<!--\s*meta)", "", text)
        text = re.sub(r"(-->)\s*\n```", r"\1", text)

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
    brief_file = {
        "CONSTRUCTOR": "agents/constructor.md",
        "OBSTRUCTOR": "agents/obstructor.md",
        "REFEREE": "agents/referee.md",
    }[speaker]
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_take_turn.py -v`
Expected: 8 passed.

- [ ] **Step 5: Write bin/turn.sh**

```bash
#!/usr/bin/env bash
# One debate turn: pick the speaker, build the prompt, run headless Claude,
# gate the response, append it, re-render, commit, push, notify.
set -uo pipefail
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin:$HOME/.bun/bin:/snap/bin"

ROOT="$HOME/kobon-duel"
LOG="$ROOT/run.log"
LOCK="$ROOT/.turn.lock"
MODEL="${KOBON_MODEL:-sonnet}"
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
RESPONSE="$(printf '%s' "$PROMPT" | claude -p --model "$MODEL" \
    --disallowed-tools "Write,Edit,NotebookEdit" 2>>"$LOG")"

if [ -z "${RESPONSE// }" ]; then
  echo "[$TS] empty response, skipping turn" >> "$LOG"
  exit 0
fi

printf '%s' "$RESPONSE" | python3 bin/commit_turn.py "$SPEAKER" "$TS" || {
  echo "[$TS] commit_turn failed" >> "$LOG"; exit 1; }

python3 bin/render.py
git add -A
git commit -q -m "turn: $SPEAKER at $TS" || true
git push -q origin main 2>>"$LOG" || \
  echo "[$TS] push failed, will retry next turn" >> "$LOG"

bash bin/notify.sh
echo "[$TS] turn done" >> "$LOG"
```

- [ ] **Step 6: Write the two small helper entrypoints**

`bin/next_speaker.py`:

```python
"""Print whose turn it is."""
import pathlib
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    turns = thread.parse((ROOT / "THREAD.md").read_text())
    sys.stdout.write(thread.next_speaker(turns))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`bin/commit_turn.py`:

```python
"""Read a raw model response on stdin, gate it, append it to THREAD.md."""
import pathlib
import sys

import take_turn
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    speaker, timestamp = sys.argv[1], sys.argv[2]
    raw = sys.stdin.read()
    turns = thread.parse((ROOT / "THREAD.md").read_text())
    turn = take_turn.ingest(
        raw,
        thread.next_number(turns),
        speaker,
        timestamp,
        allow_gold=(speaker == "REFEREE"),
    )
    thread.append_turn(ROOT / "THREAD.md", turn)
    for v in turn.violations:
        sys.stderr.write(f"violation: {v}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 7: Run the full suite and a dry run**

```bash
cd ~/kobon-duel
python3 -m pytest tests/ -v
chmod +x bin/turn.sh
python3 bin/next_speaker.py && echo
python3 bin/take_turn.py CONSTRUCTOR | head -40
```

Expected: all tests pass; `next_speaker.py` prints `CONSTRUCTOR`; the prompt
contains the brief, literature, known values, ledger, and agenda sections.

- [ ] **Step 8: Commit**

```bash
cd ~/kobon-duel
git add bin/take_turn.py bin/turn.sh bin/next_speaker.py bin/commit_turn.py tests/test_take_turn.py
git commit -m "feat: turn driver

Prompt assembly and response ingestion live in Python where they can be
tested; bash only orchestrates. Code-fenced meta trailers are unwrapped rather
than rejected, since models wrap them often enough that retrying is wasteful."
```

---

### Task 8: Telegram tiering

**Files:**
- Create: `~/kobon-duel/bin/notify.sh`
- Create: `~/kobon-duel/bin/last_tier.py`
- Create: `~/kobon-duel/tests/test_last_tier.py`

**Interfaces:**
- Consumes: `thread.parse`.
- Produces: `last_tier.summarize(text: str) -> tuple[str, str]` returning `(tier, message)`. `bin/notify.sh` sends only on silver or gold.

- [ ] **Step 1: Write the failing test**

`tests/test_last_tier.py`:

```python
import last_tier

def block(n, speaker, tier, body="argument"):
    return (
        f"## Turn {n} - {speaker} - 2026-08-18T10:00:00Z\n\n{body}\n\n"
        f'<!-- meta\n{{"tier": "{tier}", "addresses": [], "claims_opened": [],'
        f' "claims_conceded": [], "verifier_runs": [], "falsifier": "x"}}\n-->\n'
    )


def test_none_tier_returns_none():
    tier, _ = last_tier.summarize("# T\n\n" + block(1, "CONSTRUCTOR", "none"))
    assert tier == "none"


def test_silver_is_detected():
    tier, msg = last_tier.summarize("# T\n\n" + block(2, "OBSTRUCTOR", "silver"))
    assert tier == "silver"
    assert "Turn 2" in msg
    assert "OBSTRUCTOR" in msg


def test_gold_is_detected():
    tier, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert tier == "gold"
    assert "GOLD" in msg


def test_only_the_last_turn_counts():
    text = "# T\n\n" + block(1, "CONSTRUCTOR", "gold") + block(2, "OBSTRUCTOR", "none")
    assert last_tier.summarize(text)[0] == "none"


def test_empty_thread_is_none():
    assert last_tier.summarize("# T\n")[0] == "none"


def test_message_has_no_em_dashes():
    _, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert "—" not in msg


def test_message_includes_the_pages_link():
    _, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert "pjdurden.github.io/kobon-duel" in msg
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/kobon-duel && python3 -m pytest tests/test_last_tier.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'last_tier'`.

- [ ] **Step 3: Write bin/last_tier.py**

```python
"""Report the tier of the most recent turn, with a Telegram-ready message."""
from __future__ import annotations

import pathlib
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://pjdurden.github.io/kobon-duel/"


def summarize(text: str) -> tuple[str, str]:
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
```

- [ ] **Step 4: Write bin/notify.sh**

```bash
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
```

- [ ] **Step 5: Run tests and verify the notifier is silent on a quiet thread**

```bash
cd ~/kobon-duel
python3 -m pytest tests/ -v
chmod +x bin/notify.sh
python3 bin/last_tier.py; echo "exit=$?"
```

Expected: all tests pass; `last_tier.py` prints nothing and exits 1 on the seed
thread, so `notify.sh` sends nothing.

- [ ] **Step 6: Commit**

```bash
cd ~/kobon-duel
git add bin/notify.sh bin/last_tier.py tests/test_last_tier.py
git commit -m "feat: tiered Telegram notification

Silent unless the newest turn is silver or gold, so a quiet thread never
buzzes the phone."
```

---

### Task 9: Referee driver

**Files:**
- Create: `~/kobon-duel/bin/referee.sh`

**Interfaces:**
- Consumes: `bin/take_turn.py`, `bin/commit_turn.py`, `agents/referee.md`.
- Produces: a daily REFEREE turn with `allow_gold=True`, and permission for the model to rewrite `LEDGER.md` and `AGENDA.md`.

Note the permission difference: debate turns block the write tools because they
only produce text. The referee must write two files, so it runs with edit access
scoped to the repo.

- [ ] **Step 1: Write bin/referee.sh**

```bash
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
echo "[$TS] referee done" >> "$LOG"
```

- [ ] **Step 2: Verify it is syntactically sound without invoking the model**

```bash
cd ~/kobon-duel
chmod +x bin/referee.sh
bash -n bin/referee.sh && echo "syntax ok"
python3 bin/take_turn.py REFEREE | head -30
```

Expected: `syntax ok`, and the referee prompt shows the referee brief.

- [ ] **Step 3: Commit**

```bash
cd ~/kobon-duel
git add bin/referee.sh
git commit -m "feat: daily referee driver with ledger write access"
```

---

### Task 10: Systemd timers

**Files:**
- Create: `~/.config/systemd/user/kobon-turn.service`
- Create: `~/.config/systemd/user/kobon-turn.timer`
- Create: `~/.config/systemd/user/kobon-referee.service`
- Create: `~/.config/systemd/user/kobon-referee.timer`

**Interfaces:**
- Consumes: `bin/turn.sh`, `bin/referee.sh`.
- Produces: hourly debate turns, daily referee at 03:20 UTC, offset from the existing timers so nothing collides.

- [ ] **Step 1: Write the units**

`kobon-turn.service`:

```ini
[Unit]
Description=kobon-duel: one adversarial debate turn
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/env bash %h/kobon-duel/bin/turn.sh
TimeoutStartSec=900
```

`kobon-turn.timer`:

```ini
[Unit]
Description=kobon-duel hourly debate turn

[Timer]
OnCalendar=*-*-* *:17:00
Persistent=false
RandomizedDelaySec=120

[Install]
WantedBy=timers.target
```

`kobon-referee.service`:

```ini
[Unit]
Description=kobon-duel: daily referee pass
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/env bash %h/kobon-duel/bin/referee.sh
TimeoutStartSec=1800
```

`kobon-referee.timer`:

```ini
[Unit]
Description=kobon-duel daily referee

[Timer]
OnCalendar=*-*-* 03:20:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
```

`Persistent=false` on the hourly timer is deliberate: a machine that was asleep
for six hours should resume the debate, not fire six catch-up turns at once.
The referee uses `Persistent=true` because a missed daily pass leaves the ledger
stale and should be made up.

- [ ] **Step 2: Install but do not start**

```bash
systemctl --user daemon-reload
systemctl --user enable kobon-turn.timer kobon-referee.timer
systemctl --user list-timers --all | grep kobon
```

Expected: both timers listed, not yet started.

- [ ] **Step 3: Commit copies into the repo for reproducibility**

```bash
cd ~/kobon-duel
mkdir -p systemd
cp ~/.config/systemd/user/kobon-*.{service,timer} systemd/
git add systemd/
git commit -m "chore: vendor the systemd units into the repo"
```

---

### Task 11: GitHub repo, Pages, and the first live turn

**Files:**
- Create: `~/kobon-duel/README.md`

**Interfaces:**
- Consumes: everything.
- Produces: a live site at `https://pjdurden.github.io/kobon-duel/`.

- [ ] **Step 1: Write README.md**

```markdown
# kobon-duel

Two Claude sessions with opposed priors argue about the Kobon triangle problem
through an append-only file. A daily referee on a stronger model rewrites the
ledger and can reopen anything they agreed on.

**Live transcript: https://pjdurden.github.io/kobon-duel/**

## The target

N(k) is the maximum number of nonoverlapping triangles formed by an arrangement
of k lines. For even k the tightest published bound is `floor(k(3k-7)/9)`. It is
met at k = 10, 12, 16 and misses by exactly one at k = 14, 18, 20.

| k | best upper bound | best known | gap |
|---|---|---|---|
| 14 | 54 | 53 | 1 |
| 18 | 94 | 93 | 1 |
| 20 | 117 | 116 | 1 |

Each case closes in one of two ways: exhibit an arrangement meeting the bound,
or prove the bound unreachable. CONSTRUCTOR argues the first is possible,
OBSTRUCTOR argues the second.

## Why two agents

Two instances of the same model agree with each other by default, which is
useless. Four mechanisms push against that, all enforced by the driver rather
than by instruction:

1. Opposed seeded priors, and neither agent sees the other's brief.
2. A concession is valid only if it cites a verifier run or quotes the specific
   line being conceded to. Ungrounded agreement gets a violation note stamped on
   the turn, in public.
3. An argument already in the ledger cannot be re-raised without new evidence.
4. The referee hunts specifically for unearned agreement and can move any claim
   from SETTLED back to CONTESTED.

Neither debater can declare a result. Only the verifier or the referee can.

## Prior art

Savchuk (2025), [arXiv:2507.07951](https://arxiv.org/abs/2507.07951), gives a
table encoding for pseudoline arrangements, a SAT search via Kissat, and a
straightening heuristic. It closed k=23 and k=27 and proved no optimal solution
exists for k=11. Both agents are seeded with it. It did not close 14, 18, or 20.

## Layout

| path | role |
|---|---|
| `THREAD.md` | the transcript, append-only, the medium |
| `LEDGER.md` | claim registry, rewritten daily by the referee |
| `AGENDA.md` | current focus, rewritten daily |
| `KNOWN.md` | reference values, read-only to agents |
| `LITERATURE.md` | shared literature packet |
| `agents/` | the three briefs |
| `bin/` | drivers, parser, renderer, notifier |
| `docs/` | generated site |

## Status

Phase 1: the debate loop. Live.
Phase 2: exact verifier and search harness. Not yet built. Until it exists, no
claimed construction can be marked gold.
```

- [ ] **Step 2: Create the repo and push**

```bash
cd ~/kobon-duel
python3 -m pytest tests/ -v
python3 bin/render.py
git add -A
git commit -m "docs: README"
git branch -M main
gh repo create pjdurden/kobon-duel --public --source=. --remote=origin \
  --description "Two adversarial Claude sessions arguing about the Kobon triangle problem"
git push -u origin main
```

- [ ] **Step 3: Enable GitHub Pages from main /docs**

```bash
gh api -X POST repos/pjdurden/kobon-duel/pages \
  -f "source[branch]=main" -f "source[path]=/docs" || \
gh api -X PUT repos/pjdurden/kobon-duel/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
gh api repos/pjdurden/kobon-duel/pages --jq '.html_url, .status'
```

Expected: the Pages URL and a status of `building` or `built`.

- [ ] **Step 4: Fire one turn by hand and inspect it**

```bash
cd ~/kobon-duel
bash bin/turn.sh
tail -40 THREAD.md
tail -5 run.log
```

Expected: a `## Turn 1 - CONSTRUCTOR` block with prose and a well-formed meta
trailer, no `MALFORMED_META` violation, and a pushed commit.

If the trailer is malformed, the fix is in `agents/constructor.md`, not in the
parser. Tighten the format instruction and fire again.

- [ ] **Step 5: Fire the opposing turn and confirm alternation and disagreement**

```bash
cd ~/kobon-duel
bash bin/turn.sh
python3 bin/next_speaker.py; echo
grep -c "^## Turn" THREAD.md
```

Expected: turn 2 is OBSTRUCTOR, next speaker is CONSTRUCTOR, two turns present.
Read turn 2. **If OBSTRUCTOR opens by agreeing with CONSTRUCTOR, phase 1 has
failed its main design goal.** Strengthen the prior language in
`agents/obstructor.md` and re-run before starting the timers.

- [ ] **Step 6: Start the timers**

```bash
systemctl --user start kobon-turn.timer kobon-referee.timer
systemctl --user list-timers --all | grep kobon
```

- [ ] **Step 7: Commit**

```bash
cd ~/kobon-duel
git add -A && git commit -m "chore: first live turns" || true
git push origin main
```

---

## Phase 1 done when

- `https://pjdurden.github.io/kobon-duel/` renders the transcript.
- `systemctl --user list-timers` shows both kobon timers active.
- Two consecutive turns show genuine disagreement, not mutual elaboration.
- `python3 -m pytest tests/ -v` is green.
- A hand-injected silver turn produces a Telegram message and a `none` turn does not.

## Deferred to phase 2

Exact verifier, `KNOWN.md` reproduction gate, annealing baseline, agent tool
access, the gold path. Until then the referee may only mark gold for a checked
impossibility proof, never for a claimed construction.

## Spec requirements deliberately not covered by this plan

Two items from spec section 10 and 12 have no task here, on purpose:

- **BRONZE weekly digest.** The spec defines it as quiet with no push
  notification, so it delivers nothing phase 1 needs. Deferred until there is
  enough thread to digest.
- **Stall detection after three consecutive stalled days.** Requires a working
  ledger history to measure against, which does not exist until the referee has
  run for several days. Deferred.

One spec error-handling item is dropped rather than deferred:

- **Parking a dirty tree to a `wip/` branch.** This was carried over from
  `nano-daily.sh`, where it matters because that pipeline aborts on a dirty
  tree. This driver runs `git add -A` and commits whatever it finds, so there is
  no abort to rescue. Remove the item from the spec rather than implement it.
