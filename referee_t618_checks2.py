"""REFEREE turn 618, part 2: the happens-before verdict on T598's zero table,
and legal mutations at k=17.

Run:  python3 referee_t618_checks2.py
"""
import itertools, random
from kobon import corpus, table
import referee_t593_checks as R

C = corpus.by_key()


# ---------------------------------------------------------------- machinery
def hb_cyclic(t, flipped=()):
    """Happens-before digraph: node = crossing pair, edge p->q when p precedes q
    along a shared line. `flipped` = rows read right-to-left. Returns
    (cyclic?, nodes, unresolved)."""
    adj = {}
    nodes = set()
    for i, row in enumerate(t, start=1):
        seq = list(row)[::-1] if i in flipped else list(row)
        pairs = [frozenset((i, x)) for x in seq]
        nodes.update(pairs)
        for a in range(len(pairs) - 1):
            adj.setdefault(pairs[a], set()).add(pairs[a + 1])
    indeg = {p: 0 for p in nodes}
    for p, outs in adj.items():
        for q in outs:
            indeg[q] += 1
    queue = [p for p in nodes if indeg[p] == 0]
    seen = 0
    while queue:
        p = queue.pop()
        seen += 1
        for q in adj.get(p, ()):
            indeg[q] -= 1
            if indeg[q] == 0:
                queue.append(q)
    return seen != len(nodes), len(nodes), len(nodes) - seen


def total_parity(t):
    n = len(t)
    pos = table.positions(t)
    bad = inst = 0
    for i, j, m in itertools.combinations(range(1, n + 1), 3):
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
            continue
        for x in range(1, n + 1):
            if x in (i, j, m):
                continue
            inst += 1
            bad += (table._crosses_between(pos, i, j, m, x)
                    + table._crosses_between(pos, j, i, m, x)
                    + table._crosses_between(pos, m, i, j, x)) % 2
    return bad, inst


# --------------------------------------------------- T598's zero-parity table
base = C["kobon_14_53tri"]["table"]
L = 15
FB = {1: 'back', 2: 'back', 3: 'front', 4: 'front', 5: 'front', 6: 'front',
      7: 'front', 8: 'front', 9: 'front', 10: 'front', 13: 'front', 14: 'front'}
ROW15 = [1, 2, 14, 13, 11, 12, 10, 9, 8, 7, 6, 5, 4, 3]


def build(fb, order15):
    t = [list(r) for r in base]
    t[10] = t[10][:1] + [L] + t[10][1:]
    t[11] = t[11][:1] + [L] + t[11][1:]
    for i in range(1, 15):
        if i in (11, 12):
            continue
        t[i - 1] = ([L] + t[i - 1]) if fb[i] == 'front' else (t[i - 1] + [L])
    t.append(list(order15))
    return t


def main():
    print("=" * 72)
    print("48(f)  T598's total-parity-zero 15-line table, happens-before")
    tz = build(FB, ROW15)
    table.validate(tz)
    bad, inst = total_parity(tz)
    print("   table.count = %d, total parity %d of %d, row lengths %s"
          % (table.count(tz), bad, inst, [len(r) for r in tz]))
    for name, fl in [("as printed", ()), ("row 15 reversed", (15,))]:
        cyc, nn, un = hb_cyclic(tz, fl)
        print("   %-16s -> %s  (%d nodes, %d unresolved)"
              % (name, "CYCLIC" if cyc else "acyclic", nn, un))
    rnd = random.Random(0)
    cy = 0
    for _ in range(200):
        fl = frozenset(i for i in range(1, 16) if rnd.random() < .5)
        cy += hb_cyclic(tz, fl)[0]
    print("   200 random orientations of all 15 rows: %d cyclic, %d acyclic"
          % (cy, 200 - cy))
    print("   base kobon_14_53tri as printed:",
          "CYCLIC" if hb_cyclic(base)[0] else "acyclic")

    print()
    print("=" * 72)
    print("48(g)  legal mutations of kobon_17_85tri: triangle flips, not swaps")
    t17 = [list(r) for r in C["kobon_17_85tri"]["table"]]
    tris = table.triangles(t17)
    print("   kobon_17_85tri: T = %d, parity %s" % (len(tris), total_parity(t17)))
    counts = {}
    ok84 = []
    for tri in tris:
        tb = [list(r) for r in t17]
        good = True
        for i in tri:
            a, b = [x for x in tri if x != i]
            row = tb[i - 1]
            ia, ib = row.index(a), row.index(b)
            if abs(ia - ib) != 1:
                good = False
                break
            row[ia], row[ib] = row[ib], row[ia]
        if not good:
            print("   flip of", tri, "is not adjacent in all three rows -- skipped")
            continue
        try:
            table.validate(tb)
        except ValueError:
            continue
        c = table.count(tb)
        counts[c] = counts.get(c, 0) + 1
        if c == 84:
            ok84.append((tri, tb))
    print("   triangle-flip results, table.count histogram:", dict(sorted(counts.items())))
    print("   flips landing at T = 84:", len(ok84))
    seen = set()
    for tri, tb in ok84:
        b, i = total_parity(tb)
        g = R.free_gaps(tb)
        key = (b, len(g))
        if key not in seen:
            seen.add(key)
        print("       flip %-12s parity %3d of %d, free gaps %s, floor %s"
              % (str(tri), b, i, g, R.base_floor(tb, dict(g)) if len(g) == 3 else "-"))


if __name__ == "__main__":
    main()
