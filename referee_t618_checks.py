"""REFEREE turn 618: audit of turns 593-617.

Run:  python3 referee_t618_checks.py
"""
import itertools, random
from kobon import corpus, table
import referee_t593_checks as R

C = corpus.by_key()


def valid_triples(t):
    """Triples of mutually crossing, non-concurrent lines -- the only triples
    the Jordan-parity condition is a statement about."""
    n = len(t)
    pos = table.positions(t)
    out = []
    for i, j, m in itertools.combinations(range(1, n + 1), 3):
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
            continue
        out.append((i, j, m))
    return out


def floor_restricted(t, interior):
    """base_floor, but summed only over triples that are actually triangulable."""
    cut = {i: ({lab: k for k, lab in enumerate(t[i - 1])}, j)
           for i, j in interior.items()}
    bad = 0
    for tri in valid_triples(t):
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


def sec(s):
    print()
    print("=" * 72)
    print(s)


def main():
    # ---------------------------------------------------------------- 48(a)
    sec("48(a)  base_floor counts triples that cannot be triangles")
    t = C["kobon_14_53tri"]["table"]
    n = len(t)
    print("   kobon_14_53tri row lengths:", [len(r) for r in t])
    print("   C(14,3) = %d ; mutually-crossing non-concurrent triples = %d"
          % (len(list(itertools.combinations(range(1, n + 1), 3))),
             len(valid_triples(t))))
    for name, interior in [("A  (11:0, 12:0)", {11: 0, 12: 0}),
                           ("B  (11:0, 12:6)", {11: 0, 12: 6}),
                           ("C  (11:6, 12:0)", {11: 6, 12: 0}),
                           ("D  (11:6, 12:6)", {11: 6, 12: 6}),
                           ("row 11 only    ", {11: 0}),
                           ("row 12 only    ", {12: 0}),
                           ("rows 8, 11, 12 ", {8: 1, 11: 0, 12: 0})]:
        print("   %s  base_floor = %3d    restricted to real triples = %3d"
              % (name, R.base_floor(t, interior), floor_restricted(t, interior)))

    sec("48(b)  the two open bases are p'=0, so the two agree there")
    for key, gaps in [("kobon_13_m_sym_47tri", {6: 3, 9: 3}),
                      ("kobon_19_107tri", {3: 15, 18: 15})]:
        tb = C[key]["table"]
        lens = set(len(r) for r in tb)
        print("   %-22s row lengths %s  base_floor %3d  restricted %3d"
              % (key, sorted(lens), R.base_floor(tb, gaps),
                 floor_restricted(tb, gaps)))
        for i, j in gaps.items():
            print("       m=1 via row %-2d  base_floor %3d  restricted %3d"
                  % (i, R.base_floor(tb, {i: j}), floor_restricted(tb, {i: j})))

    # ---------------------------------------------------------------- 48(c)
    sec("48(c)  are the 34 k=18 T'=84 swap variants even arrangements?")
    t17 = C["kobon_17_85tri"]["table"]

    def parity_violations(tb):
        pos = table.positions(tb)
        k = len(tb)
        bad = inst = 0
        for tri in valid_triples(tb):
            i, j, m = tri
            for x in range(1, k + 1):
                if x in tri:
                    continue
                inst += 1
                bad += (table._crosses_between(pos, i, j, m, x)
                        + table._crosses_between(pos, j, i, m, x)
                        + table._crosses_between(pos, m, i, j, x)) % 2
        return bad, inst

    variants = []
    for r in range(len(t17)):
        for c in range(len(t17[r]) - 1):
            tb = [list(row) for row in t17]
            tb[r][c], tb[r][c + 1] = tb[r][c + 1], tb[r][c]
            try:
                table.validate(tb)
            except ValueError:
                continue
            if table.count(tb) == 84:
                variants.append(tb)
    print("   variants at T'=84 by single adjacent swap:", len(variants))
    b0, i0 = parity_violations(t17)
    print("   kobon_17_85tri itself: %d odd of %d instances" % (b0, i0))
    hist = {}
    floors = []
    for tb in variants:
        b, i = parity_violations(tb)
        hist[b] = hist.get(b, 0) + 1
        g = R.free_gaps(tb)
        floors.append(R.base_floor(tb, dict(g)))
    print("   the 34 variants, own Jordan-parity violation counts:", dict(sorted(hist.items())))
    print("   their base-only floors:", sorted(floors)[:5], "... min", min(floors))

    # ---------------------------------------------------------------- 48(d)
    sec("48(d)  the p'=0 bracket-free corpus census (T601 vs T602 vs T603)")
    recs = gaps_tot = extremal = 0
    detail = []
    for key, e in sorted(C.items()):
        tb = e["table"]
        if not R.bracketfree(tb):
            continue
        nn = len(tb)
        if any(len(row) != nn - 1 for row in tb):
            continue
        recs += 1
        g = R.free_gaps(tb)
        gaps_tot += len(g)
        ex = sum(1 for (i, j) in g if j == 0 or j == len(tb[i - 1]) - 2)
        extremal += ex
        if g:
            detail.append((key, len(g), ex))
    print("   p'=0 bracket-free records: %d ; free gaps %d ; extremal %d"
          % (recs, gaps_tot, extremal))
    print("   the ones with F > 0:", detail)

    # ---------------------------------------------------------------- 48(e)
    sec("48(e)  |I|=3 exhaustive space at n=5 (T606/T607 vs T608)")
    cnt = 0
    for p1 in itertools.permutations([2, 3, 4, 5]):
        for j1 in range(3):
            cnt += 1
    print("   per interior row at n=5: %d (order, gap) pairs; three rows: %d"
          % (cnt, cnt ** 3))
    print("   T606/T607 reported 373248 exhaustive; T608 reported 5832 'fully exhaustive'")


if __name__ == "__main__":
    main()
