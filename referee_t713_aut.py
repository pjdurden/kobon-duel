"""Full automorphism count for the record and for T701's new 93-witness."""
from referee_t713_iso import structure, rows_match
from referee_t713_s1ball import to_table, T701_93
from referee_t691_par import build
from kobon import corpus, table as T


def all_autos(t):
    tris, deg, par, k = structure(t)
    pairs = {}
    for tri in tris:
        for a, b in ((tri[0], tri[1]), (tri[0], tri[2]), (tri[1], tri[2])):
            pairs[(a, b)] = pairs.get((a, b), 0) + 1
    order = sorted(range(1, k + 1), key=lambda x: (deg[x], -x))
    m, used, out = {}, {}, []

    def compatible(x, y):
        if deg[x] != deg[y]:
            return False
        for xx, yy in m.items():
            if pairs.get((min(x, xx), max(x, xx)), 0) != pairs.get((min(y, yy), max(y, yy)), 0):
                return False
            if ((min(x, xx), max(x, xx)) in par) != ((min(y, yy), max(y, yy)) in par):
                return False
        for tri in tris:
            if x in tri and all(v in m or v == x for v in tri):
                if tuple(sorted(y if v == x else m[v] for v in tri)) not in tris:
                    return False
        return True

    def rec(i):
        if i == len(order):
            out.append(dict(m))
            return
        x = order[i]
        for y in range(1, k + 1):
            if y in used or not compatible(x, y):
                continue
            m[x] = y
            used[y] = x
            rec(i + 1)
            del m[x]
            del used[y]

    rec(0)
    return [f for f in out if rows_match(t, t, f)]


if __name__ == "__main__":
    rec = corpus.by_key()["kobon_18_93tri"]["table"]
    new = to_table(build(T701_93))
    for name, t in (("kobon_18_93tri", rec), ("T701_93_witness", new)):
        A = all_autos(t)
        orders = []
        for f in A:
            o, g = 1, dict(f)
            while any(g[x] != x for x in g):
                g = {x: f[g[x]] for x in g}
                o += 1
            orders.append(o)
        print(name, "T =", T.count(t), "|Aut| =", len(A),
              "element orders:", sorted(orders))
