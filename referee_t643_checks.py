"""REFEREE turn 643: audit of turns 637-642.

Independent flip(), independent slot census, independent null pricing.
Run:  python3 referee_t643_checks.py
"""
import itertools, random
from kobon import corpus, table
import referee_t593_checks as R
from referee_t618_checks2 import total_parity, hb_cyclic

C = corpus.by_key()


def tset(t):
    return set(frozenset(x) for x in table.triangles(t))


def flips(t):
    """Every triangle flip of t: swap the adjacent pair in all three rows."""
    out = []
    for tri in table.triangles(t):
        tb = [list(r) for r in t]
        ok = True
        for i in tri:
            a, b = [x for x in tri if x != i]
            row = tb[i - 1]
            try:
                ia, ib = row.index(a), row.index(b)
            except ValueError:
                ok = False; break
            if abs(ia - ib) != 1:
                ok = False; break
            row[ia], row[ib] = row[ib], row[ia]
        if ok:
            out.append((tuple(sorted(tri)), tb))
    return out


def key(t):
    return tuple(tuple(r) for r in t)


def sec(s):
    print(); print("=" * 74); print(s)


# ------------------------------------------------------------------ 49(a)
sec("49(a)  flip() calibration against reference data 48a")
for name in ("kobon_17_85tri", "kobon_13_m_sym_47tri", "kobon_21_133tri_1"):
    t = [list(r) for r in C[name]["table"]]
    fs = flips(t)
    h = {}
    for _, tb in fs:
        c = table.count(tb); h[c] = h.get(c, 0) + 1
    print("   %-22s T=%3d  %3d flips  counts %s"
          % (name, table.count(t), len(fs), dict(sorted(h.items()))))

# ------------------------------------------------------------------ 49(b)
sec("49(b)  per-flip triangle symmetric difference, AT optima and AWAY from them")
base13 = [list(r) for r in C["kobon_13_m_sym_47tri"]["table"]]
base17 = [list(r) for r in C["kobon_17_85tri"]["table"]]
base21 = [list(r) for r in C["kobon_21_133tri_1"]["table"]]
for name, t in (("kobon_13_m_sym_47tri", base13), ("kobon_17_85tri", base17),
                ("kobon_21_133tri_1", base21)):
    s0 = tset(t); h = {}
    for _, tb in flips(t):
        d = len(s0 ^ tset(tb)); h[d] = h.get(d, 0) + 1
    print("   AT optimum   %-22s symmetric-difference histogram %s"
          % (name, dict(sorted(h.items()))))

rnd = random.Random(11)
for name, t in (("kobon_13_m_sym_47tri", base13), ("kobon_17_85tri", base17)):
    # generic (non-optimal) tables: flip-distance 1 and 2 from the optimum
    gen = []
    d1 = [tb for _, tb in flips(t)]
    gen += d1
    for tb in rnd.sample(d1, min(12, len(d1))):
        gen += [x for _, x in flips(tb)]
    h = {}; worst = None
    for tb in gen:
        s0 = tset(tb)
        for _, tc in flips(tb):
            d = len(s0 ^ tset(tc)); h[d] = h.get(d, 0) + 1
            if worst is None or d > worst[0]:
                worst = (d, table.count(tb), table.count(tc))
    print("   AWAY (d1+d2) %-22s %6d flips measured, hist %s   worst %s"
          % (name, sum(h.values()), dict(sorted(h.items())), worst))
