"""Is T701's p=3 93-witness the published record's order type, or a second one?

Backtracking isomorphism search on the triangle hypergraph together with the
parallel-pair structure.  A line-relabelling that carries one table's triangle
set and parallel classes onto the other's is an isomorphism of the underlying
order type as far as every quantity this project measures is concerned; we then
confirm it on the tables themselves, rows matching up to per-row reversal.
"""
from __future__ import annotations

from referee_t713_s1ball import to_table, T701_93
from referee_t691_par import build
from kobon import corpus, table as T


def structure(t):
    k = len(t)
    tris = set(tuple(x) for x in T.triangles(t))
    deg = T.incidence_degrees(t)
    pos = T.positions(t)
    par = set()
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            if j not in pos[i]:
                par.add((i, j))
    return tris, deg, par, k


def iso(t1, t2):
    tris1, deg1, par1, k = structure(t1)
    tris2, deg2, par2, _ = structure(t2)
    if sorted(deg1.values()) != sorted(deg2.values()):
        return None
    pairs1 = {}
    for tri in tris1:
        for a, b in ((tri[0], tri[1]), (tri[0], tri[2]), (tri[1], tri[2])):
            pairs1[(a, b)] = pairs1.get((a, b), 0) + 1
    pairs2 = {}
    for tri in tris2:
        for a, b in ((tri[0], tri[1]), (tri[0], tri[2]), (tri[1], tri[2])):
            pairs2[(a, b)] = pairs2.get((a, b), 0) + 1

    order = sorted(range(1, k + 1), key=lambda x: (deg1[x], -x))
    m, used = {}, {}

    def compatible(x, y):
        if deg1[x] != deg2[y]:
            return False
        for xx, yy in m.items():
            p1 = pairs1.get((min(x, xx), max(x, xx)), 0)
            p2 = pairs2.get((min(y, yy), max(y, yy)), 0)
            if p1 != p2:
                return False
            if ((min(x, xx), max(x, xx)) in par1) != ((min(y, yy), max(y, yy)) in par2):
                return False
        for tri in tris1:
            if x in tri and all(v in m or v == x for v in tri):
                img = tuple(sorted(y if v == x else m[v] for v in tri))
                if img not in tris2:
                    return False
        return True

    def rec(i):
        if i == len(order):
            return dict(m)
        x = order[i]
        for y in range(1, k + 1):
            if y in used or not compatible(x, y):
                continue
            m[x] = y
            used[y] = x
            r = rec(i + 1)
            if r:
                return r
            del m[x]
            del used[y]
        return None

    return rec(0)


def rows_match(t1, t2, f):
    """Does relabelling t1 by f give t2, up to reversing individual rows?"""
    k = len(t1)
    for i in range(1, k + 1):
        img = [f[x] for x in t1[i - 1]]
        target = list(t2[f[i] - 1])
        if img != target and img[::-1] != target:
            return False
    return True


if __name__ == "__main__":
    rec = corpus.by_key()["kobon_18_93tri"]["table"]
    new = to_table(build(T701_93))
    print("record T =", T.count(rec), " T701 T =", T.count(new))
    f = iso(rec, new)
    print("triangle-hypergraph + parallel isomorphism found:", f is not None)
    if f:
        print("  map:", f)
        print("  rows match up to per-row reversal:", rows_match(rec, new, f))
        tris = set(tuple(x) for x in T.triangles(rec))
        img = set(tuple(sorted(f[x] for x in tri)) for tri in tris)
        print("  triangle set maps onto T701's exactly:",
              img == set(tuple(x) for x in T.triangles(new)))
