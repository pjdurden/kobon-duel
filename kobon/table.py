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
