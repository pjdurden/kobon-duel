"""Referee T691 checks 2: the deletion route (T671, T672, T673)."""
from kobon import corpus, table


def get(name):
    return corpus.by_key()[name]["table"]


def delete(tab, x):
    out = []
    for i, row in enumerate(tab, start=1):
        if i == x:
            continue
        new = []
        for e in row:
            if isinstance(e, (list, tuple)):
                ee = [v for v in e if v != x]
                if not ee:
                    continue
                new.append(ee if len(ee) > 1 else ee[0])
            elif e != x:
                new.append(e)
        out.append([relabel(e, x) for e in new])
    return out


def relabel(e, x):
    if isinstance(e, (list, tuple)):
        return [v - 1 if v > x else v for v in e]
    return e - 1 if e > x else e


def simple(tab):
    k = len(tab)
    return all(len(r) == k - 1 and all(not isinstance(e, (list, tuple)) for e in r) for r in tab)


if __name__ == "__main__":
    c = corpus.load()
    print("corpus keys:", sorted(c.keys()))
    for name in ["kobon_17_85tri", "kobon_19_107tri", "kobon_21_133tri_1",
                 "kobon_21_133tri_2", "kobon_21_133tri_3"]:
        t = get(name)
        table.validate(t)
        base = table.count(t)
        res = {}
        for x in range(1, len(t) + 1):
            d = delete(t, x)
            table.validate(d)
            res[x] = (table.count(d), simple(d))
        counts = [v[0] for v in res.values()]
        hist = {}
        for v in counts:
            hist[v] = hist.get(v, 0) + 1
        print(f"{name}: k={len(t)} T={base} deletions hist={dict(sorted(hist.items()))} "
              f"max={max(counts)} argmax={[x for x,v in res.items() if v[0]==max(counts)]} "
              f"all_simple={all(v[1] for v in res.values())}")
