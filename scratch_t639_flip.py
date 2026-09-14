
import copy
from kobon import corpus, table as T

def flip(t, tri):
    a, b, c = tri
    t2 = copy.deepcopy(t)
    def swap_adjacent(row, x, y):
        ix = iy = None
        for idx, e in enumerate(row):
            if isinstance(e, (list, tuple)):
                if x in e or y in e:
                    raise ValueError("bracket at flip site")
                continue
            if e == x: ix = idx
            if e == y: iy = idx
        if ix is None or iy is None or abs(ix - iy) != 1:
            raise ValueError(f"not adjacent: {x},{y} at {ix},{iy}")
        row[ix], row[iy] = row[iy], row[ix]
    swap_adjacent(t2[a-1], b, c)
    swap_adjacent(t2[b-1], a, c)
    swap_adjacent(t2[c-1], a, b)
    return t2

def all_flips(t):
    tris = T.triangles(t)
    out = []
    for tri in tris:
        try:
            t2 = flip(t, tri)
            T.validate(t2)
            out.append((tri, t2))
        except ValueError:
            out.append((tri, None))
    return out

if __name__ == "__main__":
    ks = corpus.by_key()
    for key in ["kobon_17_85tri", "kobon_13_m_sym_47tri"]:
        t = ks[key]["table"]
        n0 = T.count(t)
        results = all_flips(t)
        hist = {}
        fails = 0
        for tri, t2 in results:
            if t2 is None:
                fails += 1
                continue
            c = T.count(t2)
            hist[c] = hist.get(c, 0) + 1
        print(key, "base", n0, "flips", len(results), "fails", fails, "hist", hist)
