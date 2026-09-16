"""Referee T691: full table-automorphism group of a corpus arrangement.

A table automorphism is a label permutation s such that row s(i) equals
s(row i) up to reversal (per-row reversal is a free re-orientation of the line,
so it is the right equivalence).  Fixing the image of line 1 and the orientation
of the match determines s completely, so there are at most 2k candidates.
"""
from kobon import corpus, table


def flat(row):
    out = []
    for e in row:
        if isinstance(e, (list, tuple)):
            out.append(tuple(sorted(e)))
        else:
            out.append(e)
    return out


def norm(row):
    return [tuple(sorted(e)) if isinstance(e, (list, tuple)) else e for e in row]


def candidates(tab):
    k = len(tab)
    r1 = tab[0]
    if any(isinstance(e, (list, tuple)) for e in r1):
        return []
    out = []
    for a in range(1, k + 1):
        ra = tab[a - 1]
        if any(isinstance(e, (list, tuple)) for e in ra) or len(ra) != len(r1):
            continue
        for rev in (False, True):
            tgt = list(reversed(ra)) if rev else list(ra)
            p = {1: a}
            ok = True
            for x, y in zip(r1, tgt):
                if x in p and p[x] != y:
                    ok = False
                    break
                p[x] = y
            if ok and len(set(p.values())) == len(p) and len(p) == k:
                out.append(p)
    return out


def is_auto(tab, p):
    k = len(tab)
    new = [None] * k
    for i, row in enumerate(tab, 1):
        new[p[i] - 1] = [[p[v] for v in e] if isinstance(e, (list, tuple)) else p[e] for e in row]
    for a, b in zip(tab, new):
        na, nb = norm(a), norm(b)
        if na != nb and na != nb[::-1]:
            return False
    return True


def order(p):
    o = 1
    q = dict(p)
    ident = {i: i for i in p}
    while q != ident:
        q = {i: p[q[i]] for i in p}
        o += 1
        if o > 100:
            return None
    return o


if __name__ == "__main__":
    for name, e in sorted(corpus.by_key().items(), key=lambda kv: kv[1]["k"]):
        tab = e["table"]
        autos = [p for p in candidates(tab) if is_auto(tab, p)]
        if not autos:
            print(f"{name:26s} k={e['k']:2d} T={e['count']:4d}  automorphisms: none found (or row 1 bracketed)")
            continue
        desc = []
        for p in autos:
            o = order(p)
            fx = [i for i in p if p[i] == i]
            if o != 1:
                desc.append(f"order{o}(fixed lines {fx})")
        print(f"{name:26s} k={e['k']:2d} T={e['count']:4d}  |Aut|={len(autos)}  {sorted(set(desc))}")
