"""Exact triangle counting for line arrangements.

A Kobon triangle is a triangular *face* of the arrangement: three lines whose
three pairwise intersections are distinct, with no other line crossing the
interior. Faces cannot overlap, so counting triangular faces is exactly the
non-overlap condition and needs no separate check.

Everything is Fraction arithmetic. Floating point manufactures phantom
triangles at near-degenerate vertices, and that is the standard way
computational claims in this area fall apart.

Lines are (a, b, c) meaning a*x + b*y = c.

This is the core of the phase-2 verifier. The KNOWN.md reproduction gate and
the search harness are still to come; nothing here may be cited as a record.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations

Line = tuple  # (a, b, c) of Fraction
Point = tuple  # (x, y) of Fraction


def _F(v) -> Fraction:
    return v if isinstance(v, Fraction) else Fraction(v)


def normalize(lines) -> list:
    return [(_F(a), _F(b), _F(c)) for a, b, c in lines]


def intersect(l1: Line, l2: Line):
    """Intersection point, or None if parallel or identical."""
    (a1, b1, c1), (a2, b2, c2) = l1, l2
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)


def _side(line: Line, p: Point) -> int:
    a, b, c = line
    v = a * p[0] + b * p[1] - c
    return (v > 0) - (v < 0)


def triangles(lines) -> list:
    """Every triangular face, as (i, j, k, [p1, p2, p3])."""
    L = normalize(lines)
    found = []
    for i, j, k in combinations(range(len(L)), 3):
        p_ij = intersect(L[i], L[j])
        p_jk = intersect(L[j], L[k])
        p_ik = intersect(L[i], L[k])
        if p_ij is None or p_jk is None or p_ik is None:
            continue
        # Concurrent lines give a degenerate "triangle" of zero area.
        if p_ij == p_jk or p_jk == p_ik or p_ij == p_ik:
            continue
        verts = [p_ij, p_jk, p_ik]
        cut = False
        for m, other in enumerate(L):
            if m in (i, j, k):
                continue
            signs = {_side(other, v) for v in verts}
            # A line touching a vertex with the rest on one side does not cut
            # the interior; only a strict sign change does.
            if 1 in signs and -1 in signs:
                cut = True
                break
        if not cut:
            found.append((i, j, k, verts))
    return found


def count(lines) -> int:
    return len(triangles(lines))
