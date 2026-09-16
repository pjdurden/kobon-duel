"""Referee T691: independent rebuild of T668's clean-vs-concurrent V(3,18) test."""
import random
from kobon import corpus, table

BASE = corpus.by_key()["kobon_19_107tri"]["table"]


def completion(row20_order, slot, concurrent):
    """Extend the 19-line base to 20 lines, inserting line 20 at V(3,18) either
    cleanly (its own gap on rows 3 and 18) or merged into the existing vertex."""
    t = [list(r) for r in BASE]
    for i in range(1, 20):
        if i in (3, 18):
            continue
        t[i - 1].append(20)
    if concurrent:
        for i, other in ((3, 18), (18, 3)):
            row = t[i - 1]
            row[row.index(other)] = [other, 20]
    else:
        # clean: place 20 immediately next to the partner crossing on each row
        for i, other in ((3, 18), (18, 3)):
            row = t[i - 1]
            row.insert(row.index(other) + 1, 20)
    r20 = list(row20_order)
    blk = [[3, 18]] if concurrent else [3, 18]
    if concurrent:
        r20.insert(slot, [3, 18])
    else:
        r20[slot:slot] = [3, 18]
    t.append(r20)
    return t


def trial(rng):
    others = [x for x in range(1, 20) if x not in (3, 18)]
    rng.shuffle(others)
    slot = rng.randrange(len(others) + 1)
    a = completion(others, slot, False)
    b = completion(others, slot, True)
    table.validate(a)
    table.validate(b)
    return table.count(a), table.count(b)


if __name__ == "__main__":
    rng = random.Random(4242)
    hist = {}
    besta = bestb = 0
    for _ in range(500):
        ca, cb = trial(rng)
        hist[cb - ca] = hist.get(cb - ca, 0) + 1
        besta = max(besta, ca)
        bestb = max(bestb, cb)
    print("base count", table.count(BASE))
    print("500 paired trials, diff (concurrent - clean) histogram:", dict(sorted(hist.items())))
    print("best clean", besta, "best concurrent", bestb)
