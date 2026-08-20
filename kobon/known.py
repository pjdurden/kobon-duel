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
