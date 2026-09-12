"""REFEREE turn 593: every number quoted in LEDGER.md reference data 47.

Run:  python3 referee_t593_checks.py
"""
import itertools, random
from kobon import corpus, table

C = corpus.by_key()


def bracketfree(t):
    return not any(isinstance(e, (list, tuple)) for row in t for e in row)


def tris(t):
    return set(frozenset(x) for x in table.triangles(t))


def free_gaps(t):
    """(row, gap index j) with the gap lying between row[j] and row[j+1]."""
    tr = tris(t)
    return [(i, j) for i, row in enumerate(t, start=1)
            for j in range(len(row) - 1)
            if frozenset((i, row[j], row[j + 1])) not in tr]


# --- the base-only Jordan-parity floor --------------------------------------
# Insert a new line L into a bracket-free base. Each row gets L at its front,
# at its back, at an interior gap, or not at all (parallel). For a triple of
# BASE lines tested against L, only the interior rows can contribute: a front
# slot puts L at index 0 and a back slot at the last index, neither of which is
# ever strictly between two other entries, and an absent L short-circuits to
# False. So the base-only violation count is a function of the interior rows
# alone and needs no row L.

def base_floor(t, interior):
    """interior: {row -> gap index}. Odd-parity base-only triples."""
    cut = {i: ({lab: k for k, lab in enumerate(t[i - 1])}, j)
           for i, j in interior.items()}
    return floor_from_cut(len(t), cut)


def floor_from_cut(n, cut):
    bad = 0
    for tri in itertools.combinations(range(1, n + 1), 3):
        s = 0
        for i in tri:
            if i not in cut:
                continue
            posn, j = cut[i]
            a, b = [x for x in tri if x != i]
            if a not in posn or b not in posn:
                continue
            lo, hi = sorted((posn[a], posn[b]))
            if lo <= j < hi:
                s ^= 1
        bad += s
    return bad


def criterion(r1, j1, i2, r2, j2, i1):
    """Zero-floor criterion for two interior rows i1 (row r1, gap j1) and i2."""
    a = (j1 == 0 and r1[0] == i2) or (j1 == len(r1) - 2 and r1[-1] == i2)
    b = (j2 == 0 and r2[0] == i1) or (j2 == len(r2) - 2 and r2[-1] == i1)
    return a and b


def main():
    print("=" * 72)
    print("47(a)  |I| = 1: the floor is (j+1)(R-1-j), never zero")
    rnd = random.Random(0)
    ok = True
    for _ in range(200):
        n = 7
        others = [x for x in range(2, n + 1)]
        rnd.shuffle(others)
        for j in range(n - 2):
            cut = {1: ({l: k for k, l in enumerate(others)}, j)}
            if floor_from_cut(n, cut) != (j + 1) * (n - 2 - j):
                ok = False
    print("   200 random rows x every gap position, n=7 -> formula holds:", ok)

    print()
    print("=" * 72)
    print("47(b)  |I| = 2: floor 0 iff each gap is its row's outermost gap and")
    print("       the entry outside it is the other interior row's label")
    n, i1, i2, rest = 6, 1, 2, [3, 4, 5, 6]
    zero = crit = both = total = 0
    for p1 in itertools.permutations([i2] + rest):
        for p2 in itertools.permutations([i1] + rest):
            for j1 in range(n - 2):
                for j2 in range(n - 2):
                    total += 1
                    cut = {i1: ({l: k for k, l in enumerate(p1)}, j1),
                           i2: ({l: k for k, l in enumerate(p2)}, j2)}
                    f = floor_from_cut(n, cut) == 0
                    c = criterion(p1, j1, i2, p2, j2, i1)
                    zero += f
                    crit += c
                    both += (f == c)
    print("   n=6 exhaustive: %d configs, %d zero-floor, %d criterion, agree %d/%d"
          % (total, zero, crit, both, total))

    rnd = random.Random(7)
    for n in (7, 8, 9, 10):
        rest = list(range(3, n + 1))
        mism = bad = 0
        for _ in range(20000):
            a = [2] + rest[:]; rnd.shuffle(a)
            b = [1] + rest[:]; rnd.shuffle(b)
            j1, j2 = rnd.randrange(n - 2), rnd.randrange(n - 2)
            cut = {1: ({l: k for k, l in enumerate(a)}, j1),
                   2: ({l: k for k, l in enumerate(b)}, j2)}
            if (floor_from_cut(n, cut) == 0) != criterion(a, j1, 2, b, j2, 1):
                mism += 1
        for _ in range(2000):
            a = rest[:]; rnd.shuffle(a)
            b = rest[:]; rnd.shuffle(b)
            e1, e2 = rnd.choice([0, 1]), rnd.choice([0, 1])
            a = ([2] + a) if e1 == 0 else (a + [2])
            b = ([1] + b) if e2 == 0 else (b + [1])
            j1 = 0 if e1 == 0 else n - 3
            j2 = 0 if e2 == 0 else n - 3
            cut = {1: ({l: k for k, l in enumerate(a)}, j1),
                   2: ({l: k for k, l in enumerate(b)}, j2)}
            bad += floor_from_cut(n, cut) != 0
        print("   n=%2d: 20000 random configs, mismatches %d; 2000 forced-criterion"
              " configs, nonzero floors %d" % (n, mism, bad))

    print()
    print("=" * 72)
    print("47(c)  the two open bases both FAIL the criterion")
    for key, gaps in [("kobon_13_m_sym_47tri", [(6, 3), (9, 3)]),
                      ("kobon_19_107tri", [(3, 15), (18, 15)])]:
        t = C[key]["table"]
        print("   %-22s free gaps %s  R=%d" % (key, free_gaps(t), len(t[0])))
        (a, ja), (b, jb) = gaps
        print("       row %-2d = %s" % (a, t[a - 1]))
        print("       row %-2d = %s" % (b, t[b - 1]))
        print("       floor m=1 (%d): %2d   m=1 (%d): %2d   m=2 (both): %2d"
              % (a, base_floor(t, {a: ja}), b, base_floor(t, {b: jb}),
                 base_floor(t, dict(gaps))))

    print()
    print("=" * 72)
    print("47(d)  the criterion is SATISFIABLE -- kobon_14_53tri realizes it")
    t = C["kobon_14_53tri"]["table"]
    print("   free gaps:", free_gaps(t))
    print("   row 11 =", t[10])
    print("   row 12 =", t[11])
    print("   floor rows 11,12 interior at their own free gaps:",
          base_floor(t, {11: 0, 12: 0}))
    print("   floor row 11 only:", base_floor(t, {11: 0}),
          "  row 12 only:", base_floor(t, {12: 0}),
          "  all three free gaps:", base_floor(t, {8: 1, 11: 0, 12: 0}))
    tot = ext = pairs = hits = 0
    for key, e in sorted(C.items()):
        tb = e["table"]
        if not bracketfree(tb):
            continue
        g = free_gaps(tb)
        tot += len(g)
        ext += sum(1 for (i, j) in g if j == 0 or j == len(tb[i - 1]) - 2)
        for (x, jx), (y, jy) in itertools.combinations(g, 2):
            if x == y:
                continue
            pairs += 1
            hits += criterion(tb[x - 1], jx, y, tb[y - 1], jy, x)
    print("   bracket-free corpus: %d free gaps, %d extremal, %d cross-row pairs,"
          " %d criterion hits" % (tot, ext, pairs, hits))

    print()
    print("=" * 72)
    print("47(e)  reference data 46a is FALSE on bracketed bases (T575, reproduced)")
    viol = gviol = inst = 0
    for key, e in sorted(C.items()):
        t = e["table"]
        if bracketfree(t):
            continue
        k = len(t)
        pos = table.positions(t)
        allt = table.triangles(t)
        keep = lambda l: [x for x in range(1, k + 1) if x != l]
        for l in range(1, k + 1):
            inst += 1
            n = k - 1
            q = sum(1 for x in keep(l) if l not in pos[x])
            m = 0
            gs = 0
            for x in keep(l):
                row = t[x - 1]
                idx = [i for i, en in enumerate(row)
                       if (l in en if isinstance(en, (list, tuple)) else en == l)]
                if not idx:
                    continue
                i = idx[0]
                if i not in (0, len(row) - 1):
                    m += 1
                for nb in ([row[i - 1]] if i > 0 else []) + \
                          ([row[i + 1]] if i < len(row) - 1 else []):
                    gs += len(nb) if isinstance(nb, (list, tuple)) else 1
                en = row[i]
                if isinstance(en, (list, tuple)):
                    gs += len(en) - 1
            G = sum(1 for tri in allt if l in tri)
            viol += 2 * G > (n - q) + m
            gviol += 2 * G > gs
    print("   %d bracketed deletion instances: %d violate 2G <= (n-q)+m,"
          " %d violate 2G <= neighbour-group-sum" % (inst, viol, gviol))

    print()
    print("=" * 72)
    print("47(f)  table.py does NOT apply T534's touch correction (contra T587)")
    t = C["kobon_8"]["table"]
    pos = table.positions(t)
    n = len(t)
    naive = inst = conc = 0
    for tri in itertools.combinations(range(1, n + 1), 3):
        i, j, m = tri
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
            conc += 1
            continue
        for x in range(1, n + 1):
            if x in tri:
                continue
            inst += 1
            naive += (table._crosses_between(pos, i, j, m, x)
                      + table._crosses_between(pos, j, i, m, x)
                      + table._crosses_between(pos, m, i, j, x)) % 2
    print("   kobon_8: table.count = %d; %d non-concurrent (triple,x) instances"
          " (%d concurrent triples skipped)" % (table.count(t), inst, conc))
    print("   odd-parity instances via table.positions' native shared indices: %d"
          " -- the settled naive figure, not the corrected 0" % naive)


if __name__ == "__main__":
    main()
