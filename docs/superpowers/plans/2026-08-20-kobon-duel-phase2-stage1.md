# kobon-duel Phase 2 Stage 1 (Corpus and Counter) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give kobon-duel a combinatorial triangle counter validated against every published optimal arrangement from k=3 to k=33, and use it to pay the debate's oldest outstanding numeric debt.

**Architecture:** Import Savchuk's published arrangement corpus as committed JSON. Represent an arrangement as a table (per line, the ordered list of lines crossing it). Count triangular faces directly from the table using the rule that a triangle {i,j,k} survives iff no other line crosses two of its three sides. Gate the counter by requiring it to reproduce all published counts.

**Tech Stack:** Python 3.10, stdlib only (`itertools`, `json`, `pathlib`, `urllib`), pytest.

**Spec:** `docs/superpowers/specs/2026-08-20-kobon-duel-phase2-design.md`

## Global Constraints

- Python 3.10, stdlib only. No new third-party dependencies in stage 1.
- All imported arrangements are CC BY 4.0 by Pavlo Savchuk and the original arrangement authors. Attribution is mandatory in `corpus/ATTRIBUTION.md`, `KNOWN.md`, and `README.md`. No imported arrangement may appear in a Telegram or X post without its author's name.
- Tests must run offline. Network access is confined to the one-shot importer.
- Existing test suite (119 tests) must stay green. Run `python3 -m pytest` from the repo root.
- `pytest.ini` sets `pythonpath = bin . tests`, so `from kobon import x` and `import thread` both work in tests without changes.
- Commit style matches the repo: lowercase `type: summary`. Commits are SSH-signed automatically via existing git config; do not pass `-S` or `--no-gpg-sign`.
- Never edit `THREAD.md` by hand. It is append-only and driver-owned.

## Stage scope

This plan covers stage 1 only. Stage 2 (integer counter, straightening, registry, agent tool access, GOLD path, flip search) and stage 3 (`exhaust.py`) get their own plans once this lands.

**Spec correction adopted here:** the spec's section 7 "gate layer 2" recounts `records/` through `verify.py` on coordinates. Coordinates do not exist until stage 2 builds the straightener. Stage 1 therefore implements gate layer 1 (counter against corpus) and a table-level records gate; the coordinate cross-check moves to stage 2. Task 6 updates the spec to say so.

**Spec correction adopted here:** multi-line intersection points are encoded as a nested list inside a table row, not by the positional prose convention in the LineOrder README. A row entry that is a list means every line named in it meets line `i` at one common point.

---

### Task 1: Import the published corpus

**Files:**
- Create: `bin/import_corpus.py`
- Create: `corpus/arrangements.json`
- Create: `corpus/ATTRIBUTION.md`
- Test: `tests/test_corpus_data.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `corpus/arrangements.json`, a JSON object with keys `"entries"` (list) and `"skipped"` (list). Each entry is `{"key": str, "k": int, "count": int, "title": str, "table": list}` where `table` is a list of `k` rows and each row is a list whose items are either `int` or `list[int]`. Each skipped item is `{"key": str, "reason": str}`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_corpus_data.py
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "corpus" / "arrangements.json"


def load():
    return json.loads(DATA.read_text())


def test_corpus_file_exists_and_parses():
    data = load()
    assert "entries" in data and "skipped" in data


def test_corpus_has_the_open_cases():
    entries = {e["key"]: e for e in load()["entries"]}
    for key, k, count in [
        ("kobon_14_53tri", 14, 53),
        ("kobon_18_93tri", 18, 93),
        ("kobon_20_116tri", 20, 116),
        ("kobon_15_5_rot_symmetry", 15, 65),
    ]:
        assert key in entries, f"{key} missing from corpus"
        assert entries[key]["k"] == k
        assert entries[key]["count"] == count


def test_every_entry_has_k_rows_and_an_attribution():
    for e in load()["entries"]:
        assert len(e["table"]) == e["k"], e["key"]
        assert e["title"].strip(), e["key"]


def test_skipped_entries_are_recorded_not_hidden():
    """A corpus that silently drops entries reads as complete when it is not."""
    for s in load()["skipped"]:
        assert s["key"] and s["reason"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_corpus_data.py -v`
Expected: FAIL, all four tests error with `FileNotFoundError` on `corpus/arrangements.json`.

- [ ] **Step 3: Write the importer**

```python
# bin/import_corpus.py
"""One-shot import of the published Kobon arrangement corpus.

Source: https://github.com/zegalur/line-order, generate_gallery.py, CC BY 4.0,
Pavlo Savchuk 2024-2025. Individual arrangements are by their named authors;
see corpus/ATTRIBUTION.md.

Run this to regenerate corpus/arrangements.json. Tests read the committed JSON
and never touch the network.
"""
from __future__ import annotations

import ast
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "corpus" / "arrangements.json"
URL = ("https://raw.githubusercontent.com/zegalur/line-order/"
       "main/generate_gallery.py")

# Published triangle count per entry key. Taken from the gallery entry titles.
# Kept explicit rather than regex-scraped from the title so a upstream wording
# change cannot silently alter a count we gate on.
EXPECTED = {
    "triangle_3_rot_symmetry": 1, "kobon_4": 2, "kobon_4_2": 2,
    "pentagram_5_rot_symmetry": 5, "kobon_6_1": 7, "kobon_6_2": 7,
    "kobon_7": 11, "kobon_8": 15, "kobon_9_3_rot_symmetry": 21,
    "kobon_10_25tri_wajnberg": 25, "kobon_11_32tri": 32,
    "kobon_12_38tri": 38, "kobon_13_m_sym_47tri": 47,
    "kobon_14_53tri": 53, "kobon_15_5_rot_symmetry": 65,
    "kobon_16_72tri": 72, "kobon_17_85tri": 85, "kobon_18_93tri": 93,
    "kobon_19_107tri": 107, "kobon_20_116tri": 116,
    "kobon_21_133tri_1": 133, "kobon_21_133tri_2": 133,
    "kobon_21_133tri_3": 133, "kobon_22_143tri": 143,
    "kobon_23_161tri": 161, "kobon_24_172tri": 172,
    "kobon_25_191tri": 191, "kobon_27_225tri_1": 225,
    "kobon_27_225tri_2": 225, "kobon_28_238tri": 238,
    "kobon_29_261tri": 261, "kobon_31_299tri": 299, "kobon_33_341tri": 341,
}


def _literal_at(src: str, idx: int):
    """Parse the bracketed list literal starting at or after idx."""
    start = src.index("[", idx)
    depth = 0
    for e in range(start, len(src)):
        if src[e] == "[":
            depth += 1
        elif src[e] == "]":
            depth -= 1
            if depth == 0:
                return ast.literal_eval(src[start:e + 1])
    raise ValueError("unterminated list literal")


def _title_at(src: str, idx: int) -> str:
    """Read the entry_title, which upstream may split across concatenated
    string literals."""
    m = re.search(r"'entry_title'\s*:\s*(.+?)\n\s*'entry_table'",
                  src[idx:idx + 800], re.S)
    if not m:
        return ""
    parts = re.findall(r"'([^']*)'", m.group(1))
    return " ".join("".join(parts).split())


def extract(src: str, key: str):
    """Return (title, table). Raises if the table is not a literal."""
    i = src.index("'%s'" % key)
    j = src.index("'entry_table'", i)
    title = _title_at(src, i)
    ref = re.match(r"'entry_table'\s*:\s*([A-Za-z_]\w*)\s*,", src[j:j + 80])
    if ref:
        # Table stored in a module-level variable, e.g. kobon_15.
        var = re.search(r"^%s\s*=\s*\[" % re.escape(ref.group(1)), src, re.M)
        if not var:
            raise ValueError("variable %r not a module-level literal"
                             % ref.group(1))
        return title, _literal_at(src, var.start())
    if not re.match(r"'entry_table'\s*:\s*\[", src[j:j + 40]):
        raise ValueError("entry_table is a call or expression, not a literal")
    return title, _literal_at(src, j)


def main() -> int:
    src = urllib.request.urlopen(URL, timeout=60).read().decode("utf-8")
    entries, skipped = [], []
    for key, count in EXPECTED.items():
        try:
            title, table = extract(src, key)
        except Exception as exc:  # noqa: BLE001 - reason is reported, not swallowed
            skipped.append({"key": key, "reason": f"{type(exc).__name__}: {exc}"})
            continue
        entries.append({"key": key, "k": len(table), "count": count,
                        "title": title, "table": table})
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(
        {"source": URL, "license": "CC BY 4.0",
         "entries": entries, "skipped": skipped}, indent=1) + "\n")
    sys.stderr.write("imported %d entries, skipped %d\n"
                     % (len(entries), len(skipped)))
    for s in skipped:
        sys.stderr.write("  skipped %s: %s\n" % (s["key"], s["reason"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the importer and inspect what it skipped**

Run: `python3 bin/import_corpus.py`
Expected: stderr reports roughly 27 imported and up to 6 skipped. Each skipped entry names a reason. Skipped entries are acceptable; silently missing ones are not.

- [ ] **Step 5: Write the attribution file**

```markdown
<!-- corpus/ATTRIBUTION.md -->
# Corpus attribution

`corpus/arrangements.json` is imported from
[zegalur/line-order](https://github.com/zegalur/line-order),
`generate_gallery.py`, by Pavlo Savchuk (2024-2025), licensed
**CC BY 4.0**. See also the accompanying paper,
[arXiv:2507.07951](https://arxiv.org/abs/2507.07951).

Individual arrangements are credited to their original discoverers in each
entry's `title` field. Named authors in this corpus include Johannes Bader
(k=14 with 53 triangles, k=18 with 93), Toshitaka Suzuki (k=15 with 65),
Kyle Wood (k=20 with 116), Kabanovitch (k=13 with 47), Wajnberg (k=10 with 25)
and Pavlo Savchuk (k=23, k=27).

**This project did not discover any arrangement in this corpus.** The corpus is
input to our search and the fixture set for our reproduction gate. Any public
post referencing one of these arrangements names its author.
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_corpus_data.py -v`
Expected: 4 passed.

- [ ] **Step 7: Commit**

```bash
git add bin/import_corpus.py corpus/arrangements.json corpus/ATTRIBUTION.md tests/test_corpus_data.py
git commit -m "feat: import published Kobon arrangement corpus, CC BY 4.0"
```

---

### Task 2: Table representation and position maps

**Files:**
- Create: `kobon/table.py`
- Test: `tests/test_table.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `kobon.table.positions(table) -> dict[int, dict[int, int]]` mapping line label to a dict of {other line label: position index along this line}. Lines meeting line `i` at one common point share a position index. Labels are 1-based.
  - `kobon.table.validate(table) -> None`, raising `ValueError` with a message naming the offending lines.
  - `kobon.table.labels(table) -> range` giving `range(1, k+1)`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_table.py
import pytest

from kobon import table

# Verbatim from corpus entry pentagram_5_rot_symmetry. Do not hand-edit:
# a table can be well-formed and symmetric yet bound a different number of
# triangles than you expect.
PENTAGRAM = [
    [5, 3, 4, 2],
    [3, 5, 4, 1],
    [2, 5, 1, 4],
    [5, 2, 1, 3],
    [4, 2, 3, 1],
]


def test_positions_are_sequential_for_a_simple_row():
    pos = table.positions(PENTAGRAM)
    assert pos[1] == {5: 0, 3: 1, 4: 2, 2: 3}


def test_lines_meeting_at_one_point_share_a_position():
    """A nested list in a row means those lines all cross line i at one point."""
    t = [
        [2, [3, 4]],
        [1, [3, 4]],
        [[1, 2], 4],
        [[1, 2], 3],
    ]
    pos = table.positions(t)
    assert pos[1][3] == pos[1][4]
    assert pos[1][2] != pos[1][3]


def test_a_parallel_line_is_absent_from_the_row():
    """Shorter rows are legal: a parallel line never crosses."""
    t = [
        [3],
        [3],
        [1, 2],
    ]
    pos = table.positions(t)
    assert 2 not in pos[1]
    assert 1 not in pos[2]


def test_labels_are_one_based():
    assert list(table.labels(PENTAGRAM)) == [1, 2, 3, 4, 5]


def test_validate_accepts_the_pentagram():
    table.validate(PENTAGRAM)


def test_validate_rejects_an_asymmetric_crossing():
    """If line 2 crosses line 1, line 1 must cross line 2."""
    bad = [
        [5, 3, 4, 2],
        [3, 5, 4],      # line 2 no longer lists line 1
        [2, 5, 1, 4],
        [5, 2, 1, 3],
        [4, 2, 3, 1],
    ]
    with pytest.raises(ValueError, match="1.*2|2.*1"):
        table.validate(bad)


def test_validate_rejects_a_line_listing_itself():
    bad = [[1, 3], [3, 1], [1, 2]]
    with pytest.raises(ValueError, match="itself"):
        table.validate(bad)


def test_validate_rejects_an_out_of_range_label():
    bad = [[2, 9], [1, 3], [1, 2]]
    with pytest.raises(ValueError, match="9"):
        table.validate(bad)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_table.py -v`
Expected: FAIL with `ImportError: cannot import name 'table' from 'kobon'`.

- [ ] **Step 3: Write the implementation**

```python
# kobon/table.py
"""Arrangement tables, the combinatorial representation.

A table has one row per line. Row `i` lists the lines crossing line `i`, in
order along line `i`. Labels are 1-based, matching the published corpus.

Two degeneracies occur in the corpus and both are represented structurally:

- A **parallel** line never crosses line `i` and is simply absent from row `i`,
  so rows may be shorter than `k - 1`.
- A **multi-line intersection point** is a nested list: every line named in that
  list crosses line `i` at one common point, so they share a position index.

Format credit: Pavlo Savchuk, CC BY 4.0. See corpus/ATTRIBUTION.md.
"""
from __future__ import annotations


def labels(table):
    """The 1-based line labels of the arrangement."""
    return range(1, len(table) + 1)


def positions(table):
    """Position of every crossing along every line.

    Returns {line: {other line: index}}. Lines sharing an intersection point
    share an index, which is what makes the betweenness test in `triangles`
    correct at multi-line points rather than merely approximate.
    """
    pos = {}
    for i, row in enumerate(table, start=1):
        along = {}
        for index, entry in enumerate(row):
            if isinstance(entry, (list, tuple)):
                for j in entry:
                    along[j] = index
            else:
                along[entry] = index
        pos[i] = along
    return pos


def validate(table):
    """Raise ValueError if the table is not a well-formed arrangement."""
    k = len(table)
    pos = positions(table)
    for i in labels(table):
        for j in pos[i]:
            if j == i:
                raise ValueError(f"line {i} lists itself")
            if not 1 <= j <= k:
                raise ValueError(f"line {i} lists out-of-range label {j}")
    for i in labels(table):
        for j in pos[i]:
            if i not in pos[j]:
                raise ValueError(
                    f"line {i} crosses line {j} but line {j} does not "
                    f"cross line {i}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_table.py -v`
Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
git add kobon/table.py tests/test_table.py
git commit -m "feat: arrangement table representation with parallels and multi-line points"
```

---

### Task 3: Triangle enumeration, gated on the whole corpus

**Files:**
- Modify: `kobon/table.py` (append `triangles` and `count`)
- Test: `tests/test_table_triangles.py`
- Test: `tests/test_corpus_reproduction.py`

**Interfaces:**
- Consumes: `kobon.table.positions`, `kobon.table.labels`.
- Produces:
  - `kobon.table.triangles(table) -> list[tuple[int, int, int]]`, each a sorted 1-based triple, in lexicographic order.
  - `kobon.table.count(table) -> int`.

The rule: triple `{i,j,m}` bounds a triangular face iff the three lines pairwise cross, are not concurrent, and no fourth line `x` crosses two of the three sides. A line meeting a triangle's boundary meets it an even number of times, so "crosses the interior" is exactly "crosses two sides"; testing for any positive count is therefore sufficient and cheaper.

- [ ] **Step 1: Write the failing unit test**

```python
# tests/test_table_triangles.py
from kobon import table

# Verbatim from corpus entry pentagram_5_rot_symmetry. Do not hand-edit:
# a table can be well-formed and symmetric yet bound a different number of
# triangles than you expect.
PENTAGRAM = [
    [5, 3, 4, 2],
    [3, 5, 4, 1],
    [2, 5, 1, 4],
    [5, 2, 1, 3],
    [4, 2, 3, 1],
]


def test_three_crossing_lines_bound_one_triangle():
    assert table.count([[2, 3], [1, 3], [1, 2]]) == 1


def test_three_concurrent_lines_bound_nothing():
    """One nested group: all three meet at a single point."""
    assert table.count([[[2, 3]], [[1, 3]], [[1, 2]]]) == 0


def test_two_parallel_lines_bound_nothing():
    """Lines 1 and 2 never cross, so no triple can close."""
    assert table.count([[3], [3], [1, 2]]) == 0


def test_pentagram_has_five_triangles():
    assert table.count(PENTAGRAM) == 5


def test_triangles_are_sorted_triples_and_match_the_count():
    tris = table.triangles(PENTAGRAM)
    assert len(tris) == table.count(PENTAGRAM)
    for t in tris:
        assert list(t) == sorted(t)
        assert len(set(t)) == 3
    assert tris == sorted(tris)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_table_triangles.py -v`
Expected: FAIL with `AttributeError: module 'kobon.table' has no attribute 'count'`.

- [ ] **Step 3: Write the implementation**

```python
# append to kobon/table.py
from itertools import combinations


def _crosses_between(pos, i, a, b, x):
    """Does line x cross line i strictly between i's crossings with a and b?"""
    along = pos[i]
    if x not in along or a not in along or b not in along:
        return False
    lo, hi = sorted((along[a], along[b]))
    return lo < along[x] < hi


def triangles(table):
    """Every triangular face, as sorted 1-based triples."""
    pos = positions(table)
    found = []
    for i, j, m in combinations(labels(table), 3):
        # All three pairs must actually cross.
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        # Concurrent at one point: zero area, not a face.
        if pos[i][j] == pos[i][m]:
            continue
        cut = any(
            _crosses_between(pos, i, j, m, x)
            or _crosses_between(pos, j, i, m, x)
            or _crosses_between(pos, m, i, j, x)
            for x in labels(table) if x not in (i, j, m)
        )
        if not cut:
            found.append((i, j, m))
    return found


def count(table):
    return len(triangles(table))
```

- [ ] **Step 4: Run unit tests to verify they pass**

Run: `python3 -m pytest tests/test_table_triangles.py -v`
Expected: 5 passed.

- [ ] **Step 5: Write the corpus reproduction gate**

```python
# tests/test_corpus_reproduction.py
"""The gate: our counter must agree with every published count.

A disagreement here is a bug in us, not a discovery. This is the single test
that licenses every other number this project will ever produce.
"""
import json
import pathlib

import pytest

from kobon import table

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES = json.loads((ROOT / "corpus" / "arrangements.json").read_text())["entries"]


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e["key"])
def test_published_count_is_reproduced(entry):
    table.validate(entry["table"])
    assert table.count(entry["table"]) == entry["count"]


def test_the_gate_covers_the_three_open_cases():
    keys = {e["key"] for e in ENTRIES}
    assert {"kobon_14_53tri", "kobon_18_93tri", "kobon_20_116tri"} <= keys


def test_the_gate_is_not_vacuous():
    assert len(ENTRIES) >= 20
```

- [ ] **Step 6: Run the gate**

Run: `python3 -m pytest tests/test_corpus_reproduction.py -v`
Expected: every parametrized case passes, roughly 27 of them plus the two guards. If any case fails, stop and fix the counter; do not adjust the expected count.

- [ ] **Step 7: Run the full suite**

Run: `python3 -m pytest`
Expected: all green, previous 119 tests plus the new ones.

- [ ] **Step 8: Commit**

```bash
git add kobon/table.py tests/test_table_triangles.py tests/test_corpus_reproduction.py
git commit -m "feat: combinatorial triangle counter, gated on all published counts"
```

---

### Task 4: Per-line incidence degrees, and pay the turn-5 debt

**Files:**
- Modify: `kobon/table.py` (append `incidence_degrees`)
- Create: `bin/degree_sequence.py`
- Test: `tests/test_degree_sequence.py`

**Interfaces:**
- Consumes: `kobon.table.triangles`.
- Produces: `kobon.table.incidence_degrees(table) -> dict[int, int]`, mapping each 1-based line label to the number of triangular faces having a side on that line.

Why this task exists: `deletion-route-construction` has been CONTESTED in `LEDGER.md` since turn 5, blocked on exactly this number for a k=15, T=65 optimum. Deleting a line of triangle-incidence `d` from a 65-triangle arrangement leaves at least `65 - d` triangles on 14 lines. Clearing 53 needs a line with `d <= 12`; clearing 54 needs `d <= 11`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_degree_sequence.py
import json
import pathlib

from kobon import table

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES = {e["key"]: e for e in
           json.loads((ROOT / "corpus" / "arrangements.json").read_text())["entries"]}


def test_each_triangle_contributes_three_incidences():
    t = ENTRIES["pentagram_5_rot_symmetry"]["table"]
    deg = table.incidence_degrees(t)
    assert sum(deg.values()) == 3 * table.count(t)


def test_every_line_gets_an_entry_even_at_zero():
    """A line touching no triangle must still appear, or the sequence lies."""
    t = [[3], [3], [1, 2]]
    deg = table.incidence_degrees(t)
    assert set(deg) == {1, 2, 3}
    assert deg == {1: 0, 2: 0, 3: 0}


def test_k15_optimum_degree_sum_is_consistent():
    t = ENTRIES["kobon_15_5_rot_symmetry"]["table"]
    deg = table.incidence_degrees(t)
    assert table.count(t) == 65
    assert sum(deg.values()) == 195
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_degree_sequence.py -v`
Expected: FAIL with `AttributeError: module 'kobon.table' has no attribute 'incidence_degrees'`.

- [ ] **Step 3: Write the implementation**

```python
# append to kobon/table.py
def incidence_degrees(table):
    """Triangles per line. Lines touching none are present with a zero."""
    deg = {i: 0 for i in labels(table)}
    for tri in triangles(table):
        for i in tri:
            deg[i] += 1
    return deg
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_degree_sequence.py -v`
Expected: 3 passed.

- [ ] **Step 5: Write the CLI**

```python
# bin/degree_sequence.py
"""Per-line triangle-incidence degree sequence for a corpus arrangement.

Usage: python3 bin/degree_sequence.py <corpus-key>
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# sys.path[0] is bin/ when run as a script, so the repo root is not importable
# by default. pytest gets this from pytest.ini; a bare script does not.
sys.path.insert(0, str(ROOT))

from kobon import table  # noqa: E402


def main(argv) -> int:
    if len(argv) != 2:
        sys.stderr.write(__doc__)
        return 2
    entries = {e["key"]: e for e in json.loads(
        (ROOT / "corpus" / "arrangements.json").read_text())["entries"]}
    key = argv[1]
    if key not in entries:
        sys.stderr.write("unknown key %r; known keys:\n  %s\n"
                         % (key, "\n  ".join(sorted(entries))))
        return 2
    entry = entries[key]
    deg = table.incidence_degrees(entry["table"])
    total = table.count(entry["table"])
    print(entry["title"])
    print("k = %d, triangles = %d (published %d)"
          % (entry["k"], total, entry["count"]))
    print("degree sequence, sorted ascending:")
    print("  " + ", ".join(str(d) for d in sorted(deg.values())))
    print("by line: " + ", ".join("%d:%d" % (i, deg[i]) for i in sorted(deg)))
    print("sum = %d (must equal 3 * %d = %d)" % (sum(deg.values()), total, 3 * total))
    print("min degree = %d, so deleting that line leaves >= %d triangles on %d lines"
          % (min(deg.values()), total - min(deg.values()), entry["k"] - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 6: Run it on the k=15 optimum**

Run: `python3 bin/degree_sequence.py kobon_15_5_rot_symmetry`
Expected: prints the full degree sequence, sum 195, and the deletion floor. Record the actual output; the next step writes it into the ledger.

- [ ] **Step 7: Record the result in the ledger**

Edit `LEDGER.md`, row `deletion-route-construction`. Replace the sentence "The per-line triangle-incidence degree sequence of a known k=15, T=65 optimum has never been produced by either side." with the computed sequence, the minimum degree, and the resulting bound, attributed to Suzuki's arrangement via the corpus. State plainly whether the minimum degree is at most 12 (clears 53), at most 11 (clears 54), or neither.

Use this shape, filling the bracketed values from step 6's actual output:

```
Referee-checkable computation, from Suzuki's k=15, T=65 arrangement
(corpus entry `kobon_15_5_rot_symmetry`, CC BY 4.0). Degree sequence:
[...]. Minimum incidence degree d_min = [..]. Deleting that line leaves a
14-line arrangement with at least 65 - [..] = [..] triangles. The antecedent
owed since turn 5 is now discharged: [it clears 53 / it clears 54 / it clears
neither].
```

Do not overstate. Deleting a line gives a 14-line arrangement with at least `65 - d_min` triangles; that is a lower bound on what deletion yields from this particular arrangement, not a claim about N(14). Note also that the deleted-line result is a *table*, so run it through `kobon.table.count` rather than asserting the bound is attained.

- [ ] **Step 8: Run the full suite and commit**

```bash
python3 -m pytest
git add kobon/table.py bin/degree_sequence.py tests/test_degree_sequence.py LEDGER.md
git commit -m "feat: incidence degree sequence; settle the k=15 number owed since turn 5"
```

---

### Task 5: Records, and the KNOWN.md consistency gate

**Files:**
- Create: `kobon/known.py`
- Create: `kobon/records.py`
- Create: `bin/seed_records.py`
- Create: `records/` (populated by the seeder)
- Test: `tests/test_known.py` already exists for other purposes; create `tests/test_known_table.py`
- Test: `tests/test_records.py`

**Interfaces:**
- Consumes: `kobon.table.count`, `corpus/arrangements.json`.
- Produces:
  - `kobon.known.best_known() -> dict[int, int]` mapping k to the best-known triangle count parsed from `KNOWN.md`.
  - `kobon.known.best_upper_bound() -> dict[int, int]` mapping k to the "best UB" column.
  - `kobon.records.load(k) -> dict | None` and `kobon.records.save(record) -> pathlib.Path`, where a record is `{"k": int, "count": int, "table": list, "provenance": str}`.

- [ ] **Step 1: Write the failing test for the KNOWN.md parser**

```python
# tests/test_known_table.py
from kobon import known


def test_parses_the_closed_cases():
    bk = known.best_known()
    assert bk[3] == 1
    assert bk[5] == 5
    assert bk[13] == 47
    assert bk[15] == 65


def test_parses_the_open_cases():
    bk = known.best_known()
    assert bk[14] == 53
    assert bk[18] == 93
    assert bk[20] == 116


def test_upper_bounds_exceed_best_known_exactly_at_the_open_cases():
    bk, ub = known.best_known(), known.best_upper_bound()
    open_cases = {k for k in bk if ub[k] > bk[k]}
    assert open_cases == {14, 18, 20}
    for k in open_cases:
        assert ub[k] - bk[k] == 1


def test_k_is_not_in_the_table_when_absent():
    assert 26 not in known.best_known()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_known_table.py -v`
Expected: FAIL with `ImportError: cannot import name 'known' from 'kobon'`.

- [ ] **Step 3: Write the KNOWN.md parser**

```python
# kobon/known.py
"""Read the reference table out of KNOWN.md.

KNOWN.md is the single source of truth for best-known values and is read-only
to the debate agents. Parsing it rather than duplicating it means a record
claim is always checked against the file a human maintains.
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWN = ROOT / "KNOWN.md"

# | k | Tamura UB | best UB | best known | status | source |
_ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|")


def _rows():
    for line in KNOWN.read_text().splitlines():
        m = _ROW.match(line.strip())
        if m:
            yield tuple(int(g) for g in m.groups())


def best_known():
    return {k: bk for k, _tamura, _ub, bk in _rows()}


def best_upper_bound():
    return {k: ub for k, _tamura, ub, _bk in _rows()}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_known_table.py -v`
Expected: 4 passed.

- [ ] **Step 5: Write the failing test for records**

```python
# tests/test_records.py
import json
import pathlib

import pytest

from kobon import known, records, table

ROOT = pathlib.Path(__file__).resolve().parent.parent
RECORD_FILES = sorted((ROOT / "records").glob("*.json"))


def test_records_directory_is_populated():
    assert RECORD_FILES, "run: python3 bin/seed_records.py"


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_stored_count_matches_a_recount(path):
    rec = json.loads(path.read_text())
    assert table.count(rec["table"]) == rec["count"]


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_record_meets_or_beats_best_known(path):
    rec = json.loads(path.read_text())
    assert rec["count"] >= known.best_known()[rec["k"]]


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_record_carries_provenance(path):
    rec = json.loads(path.read_text())
    assert rec["provenance"].strip()


def test_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(records, "DIR", tmp_path)
    rec = {"k": 3, "count": 1, "table": [[2, 3], [1, 3], [1, 2]],
           "provenance": "test"}
    records.save(rec)
    assert records.load(3) == rec
    assert records.load(99) is None
```

- [ ] **Step 6: Run test to verify it fails**

Run: `python3 -m pytest tests/test_records.py -v`
Expected: FAIL with `ImportError: cannot import name 'records' from 'kobon'`.

- [ ] **Step 7: Write records and the seeder**

```python
# kobon/records.py
"""The best arrangement currently held for each k.

Stage 1 stores tables only. Stage 2 adds straightened coordinates and the
exact-Fraction cross-check.
"""
from __future__ import annotations

import json
import pathlib

DIR = pathlib.Path(__file__).resolve().parent.parent / "records"


def path(k: int) -> pathlib.Path:
    return DIR / f"{k}.json"


def load(k: int):
    p = path(k)
    if not p.exists():
        return None
    return json.loads(p.read_text())


def save(record) -> pathlib.Path:
    DIR.mkdir(exist_ok=True)
    p = path(record["k"])
    p.write_text(json.dumps(record, indent=1) + "\n")
    return p
```

```python
# bin/seed_records.py
"""Seed records/ from the published corpus, best entry per k."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from kobon import records, table  # noqa: E402


def main() -> int:
    entries = json.loads(
        (ROOT / "corpus" / "arrangements.json").read_text())["entries"]
    best = {}
    for e in entries:
        counted = table.count(e["table"])
        if counted != e["count"]:
            sys.stderr.write("refusing to seed %s: counted %d, published %d\n"
                             % (e["key"], counted, e["count"]))
            return 1
        if e["k"] not in best or counted > best[e["k"]]["count"]:
            best[e["k"]] = {"k": e["k"], "count": counted, "table": e["table"],
                            "provenance": "corpus: %s (%s)" % (e["key"], e["title"])}
    for rec in best.values():
        records.save(rec)
    sys.stderr.write("seeded %d records\n" % len(best))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 8: Seed and run the tests**

Run: `python3 bin/seed_records.py && python3 -m pytest tests/test_records.py -v`
Expected: seeder reports the number of records written; all record tests pass.

- [ ] **Step 9: Commit**

```bash
git add kobon/known.py kobon/records.py bin/seed_records.py records tests/test_known_table.py tests/test_records.py
git commit -m "feat: records seeded from corpus, gated against KNOWN.md"
```

---

### Task 6: Documentation and spec reconciliation

**Files:**
- Modify: `README.md`
- Modify: `KNOWN.md`
- Modify: `docs/superpowers/specs/2026-08-20-kobon-duel-phase2-design.md`

- [ ] **Step 1: Update the README status section**

Replace the `## Status` block and extend the layout table:

```markdown
## Status

Phase 1: the debate loop. Live.
Phase 2 stage 1: arrangement corpus, combinatorial triangle counter,
reproduction gate. Live. The counter reproduces every published optimal count
from k=3 to k=33.
Phase 2 stages 2 and 3: registry, agent tool access, flip search, exhaustive
search. Not yet built. Until the registry exists, no claimed construction can
be marked gold.

## Credits

The arrangement corpus in `corpus/` is imported from
[zegalur/line-order](https://github.com/zegalur/line-order) by Pavlo Savchuk,
CC BY 4.0. The arrangements themselves are the work of Johannes Bader,
Toshitaka Suzuki, Kyle Wood, Kabanovitch, Wajnberg and Savchuk. This project
discovered none of them. Full attribution in `corpus/ATTRIBUTION.md`.
```

Add these two rows to the layout table:

```markdown
| `corpus/` | published arrangements, imported, read-only |
| `records/` | best arrangement currently held per k |
```

- [ ] **Step 2: Update KNOWN.md**

Append to the Sources section, changing no value in the table itself:

```markdown
Machine-readable tables for the arrangements above are vendored in
`corpus/arrangements.json`, imported from zegalur/line-order under CC BY 4.0.
Per-arrangement attribution is in `corpus/ATTRIBUTION.md`.
```

- [ ] **Step 3: Reconcile the spec with what was learned**

In `docs/superpowers/specs/2026-08-20-kobon-duel-phase2-design.md`:

- Section 5.1: replace the prose description of multi-line points with the actual encoding, a nested list inside a row.
- Section 7: split gate layer 2 into "stage 1: records recounted from their tables against `KNOWN.md`" and "stage 2: records recounted from coordinates through `verify.py`".
- Section 12: note that stage 1 delivered N of the 32 corpus entries, with the remainder skipped because their tables are generated by function calls upstream rather than stored as literals, and that importing those is deferred to stage 2.

- [ ] **Step 4: Run the full suite and commit**

```bash
python3 -m pytest
git add README.md KNOWN.md docs/superpowers/specs/2026-08-20-kobon-duel-phase2-design.md
git commit -m "docs: phase 2 stage 1 status, corpus credits, spec reconciliation"
git push origin main
```

---

## Stage 1 done when

- `python3 -m pytest` is green, including a parametrized reproduction test over every imported corpus entry.
- `python3 bin/degree_sequence.py kobon_15_5_rot_symmetry` prints a degree sequence summing to 195.
- `LEDGER.md` states the k=15 minimum incidence degree and what it implies for the deletion route, replacing the "never been produced by either side" sentence.
- `records/` holds one JSON per k, each recounting to its stored value.
- `corpus/ATTRIBUTION.md` exists and the README credits it.
