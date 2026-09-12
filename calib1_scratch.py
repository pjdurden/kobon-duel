
import random
from kobon import corpus, table

C = corpus.by_key()
base = C["kobon_14_53tri"]["table"]
n = 14
L = 15

def build(front_back, order15):
    t = [list(r) for r in base]
    t[10] = t[10][:1] + [L] + t[10][1:]
    t[11] = t[11][:1] + [L] + t[11][1:]
    for i in range(1, n+1):
        if i in (11,12):
            continue
        row = t[i-1]
        if front_back[i] == "front":
            t[i-1] = [L] + row
        else:
            t[i-1] = row + [L]
    t.append(list(order15))
    return t

rows_fb = [i for i in range(1,15) if i not in (11,12)]
rnd = random.Random(42)
best = (-1, None, None)
for trial in range(4000):
    fb = {}
    for i in rows_fb:
        fb[i] = rnd.choice(["front","back"])
    order15 = list(range(1,15))
    rnd.shuffle(order15)
    t = build(fb, order15)
    try:
        table.validate(t)
    except ValueError:
        continue
    c = table.count(t)
    if c > best[0]:
        best = (c, dict(fb), list(order15))

print("best count over 4000 random trials:", best[0])
print("fb:", best[1])
print("order15:", best[2])


def total_parity_violations(t):
    from itertools import combinations
    n = len(t)
    pos = table.positions(t)
    bad = 0
    inst = 0
    for i,j,m in combinations(range(1,n+1), 3):
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
            continue
        for x in range(1, n+1):
            if x in (i,j,m):
                continue
            inst += 1
            s = (table._crosses_between(pos, i, j, m, x)
                 + table._crosses_between(pos, j, i, m, x)
                 + table._crosses_between(pos, m, i, j, x)) % 2
            bad += s
    return bad, inst

fb_best = best[1]
rnd2 = random.Random(123)
res = []
for trial in range(3000):
    order15 = list(range(1,15))
    rnd2.shuffle(order15)
    t = build(fb_best, order15)
    try:
        table.validate(t)
    except ValueError:
        continue
    bad, inst = total_parity_violations(t)
    res.append((bad, inst, order15))

res.sort(key=lambda r: r[0])
print("min total violations:", res[0][0], "of", res[0][1])
print("order15:", res[0][2])
print("top5:", [r[0] for r in res[:5]])
print("worst:", res[-1][0])


def hillclimb(fb, start_order, iters=200):
    order = list(start_order)
    t = build(fb, order)
    cur, inst = total_parity_violations(t)
    improved = True
    rounds = 0
    while improved and rounds < iters:
        improved = False
        rounds += 1
        for a in range(14):
            for b in range(a+1, 14):
                order[a], order[b] = order[b], order[a]
                t2 = build(fb, order)
                try:
                    table.validate(t2)
                except ValueError:
                    order[a], order[b] = order[b], order[a]
                    continue
                v, _ = total_parity_violations(t2)
                if v < cur:
                    cur = v
                    improved = True
                else:
                    order[a], order[b] = order[b], order[a]
    return cur, order

best_hc = None
rnd3 = random.Random(7)
for start in [res[0][2], res[1][2], res[2][2]]:
    v, o = hillclimb(fb_best, start)
    print("hillclimb from", v)
    if best_hc is None or v < best_hc[0]:
        best_hc = (v, o)

for _ in range(5):
    order0 = list(range(1,15))
    rnd3.shuffle(order0)
    v, o = hillclimb(fb_best, order0)
    print("hillclimb from random start ->", v)
    if v < best_hc[0]:
        best_hc = (v, o)

print("BEST after hillclimbing:", best_hc[0], best_hc[1])


rnd4 = random.Random(99)
overall_best = best_hc
for trial_fb in range(6):
    fb2 = {}
    for i in rows_fb:
        fb2[i] = rnd4.choice(["front","back"])
    for _ in range(3):
        order0 = list(range(1,15))
        rnd4.shuffle(order0)
        v, o = hillclimb(fb2, order0, iters=100)
        print("fb variant", trial_fb, "hillclimb ->", v)
        if v < overall_best[0]:
            overall_best = (v, o)

print("OVERALL BEST across fb variants + hillclimb:", overall_best[0])

t_final = build(fb_best, best_hc[1])
c = table.count(t_final)
bad, inst = total_parity_violations(t_final)
print("final candidate (original best fb): table.count =", c, " total_parity_violations =", bad, "/", inst)
