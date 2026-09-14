
import itertools
from kobon import corpus, table as T
import referee_t593_checks as R

def flip(t, tri):
    a, b, c = tri
    t2 = [list(row) for row in t]
    def swap_adjacent(row, x, y):
        ix = iy = None
        for idx, e in enumerate(row):
            if e == x: ix = idx
            if e == y: iy = idx
        if ix is None or iy is None or abs(ix - iy) != 1:
            raise ValueError("not adjacent")
        row[ix], row[iy] = row[iy], row[ix]
    swap_adjacent(t2[a-1], b, c)
    swap_adjacent(t2[b-1], a, c)
    swap_adjacent(t2[c-1], a, b)
    return t2

def key_of(t):
    return tuple(tuple(row) for row in t)

def all_flips(t):
    out = []
    for tri in T.triangles(t):
        t2 = flip(t, tri)
        T.validate(t2)
        out.append(t2)
    return out

B = corpus.by_key()["kobon_13_m_sym_47tri"]["table"]
base_key = key_of(B)

frontier0 = {base_key: B}
frontier1 = {}
for k0, t0 in frontier0.items():
    for t2 in all_flips(t0):
        frontier1.setdefault(key_of(t2), t2)

frontier2 = {}
for k1, t1 in frontier1.items():
    for t2 in all_flips(t1):
        kk = key_of(t2)
        if kk == base_key or kk in frontier1:
            continue
        frontier2.setdefault(kk, t2)

frontier3 = {}
seen_so_far = set(frontier0) | set(frontier1) | set(frontier2)
for k2, t2 in frontier2.items():
    for t3 in all_flips(t2):
        kk = key_of(t3)
        if kk in seen_so_far:
            continue
        frontier3.setdefault(kk, t3)

for label, fr in [("d1", frontier1), ("d2", frontier2), ("d3", frontier3)]:
    hist = {}
    for t in fr.values():
        c = T.count(t)
        hist[c] = hist.get(c, 0) + 1
    n47 = hist.get(47, 0)
    print(label, "distinct", len(fr), "hist", dict(sorted(hist.items())), "T=47 count:", n47)
