"""Referee T691 checks: the C3 k=18 witness chain, T668-T690."""
from fractions import Fraction
from itertools import combinations
from kobon import verify

M_SEEDS = {
    "T669_84": [(3,-4,9),(0,-4,-13),(-8,3,-11),(13,-11,-9),(-8,-7,2),(5,14,-11)],
    "T679_84": [(-19,22,0),(6,8,8),(-9,0,38),(19,-9,21),(22,14,-39),(12,22,-28)],
    "T680_85": [(-19,22,1),(6,8,8),(-9,0,38),(19,-9,21),(22,14,-39),(12,22,-28)],
    "T681_91": [(-37,-8,37),(4,-6,27),(-3,-10,39),(39,20,4),(-39,29,38),(25,-6,10)],
    "T682_93": [(-44,-10,24),(1,-6,38),(1,7,37),(36,19,3),(14,6,76),(48,-12,10)],
    "T683_88": [(-38,-10,20),(3,-6,48),(1,7,41),(41,20,7),(14,7,72),(78,-7,7)],
    "T685_91": [(-36,-8,37),(4,-6,27),(-3,-10,39),(37,20,4),(-39,29,38),(25,-6,10)],
    "T686_88": [(-47,-8,39),(5,-8,28),(0,-13,38),(37,20,4),(-42,35,34),(28,-8,10)],
    "T689_79": [(-39,41,-500),(-45,55,-404),(11,-28,-458),(25,12,-18),(16,-40,-350),(8,-79,-280)],
}

def orbit(seed):
    a,b,c = seed
    L=[(a,b,c)]
    for _ in range(2):
        a,b,c = L[-1]
        L.append((b-a,-a,c))
    return L

def build(seeds):
    out=[]
    for s in seeds: out.extend(orbit(s))
    return out

def analyse(seeds):
    L = verify.normalize(build(seeds))
    n = len(L)
    # distinctness
    keys = set()
    for (a,b,c) in L:
        g = max(abs(a),abs(b))
        keys.add((a/g, b/g, c/g) if g else (a,b,c))
    distinct = len(keys) == n
    # parallels
    par = 0
    pts = {}
    for i,j in combinations(range(n),2):
        p = verify.intersect(L[i],L[j])
        if p is None: par += 1
        else: pts.setdefault(p,set()).update([i,j])
    conc = sum(1 for p,s in pts.items() if len(s) > 2)
    tris = verify.triangles(L)
    T = len(tris)
    part = [0]*n
    s = 0
    for (i,j,k,_) in tris:
        for x in (i,j,k): part[x]+=1
        if i//3 == j//3 == k//3: s += 1
    orb = [sum(part[3*o:3*o+3]) for o in range(6)]
    d = [16 - part[3*o] for o in range(6)]
    uniform = all(part[3*o]==part[3*o+1]==part[3*o+2] for o in range(6))
    return dict(T=T, p=par, c=conc, distinct=distinct, s=s, part=part,
                orbsum=orb, d=d, sumd=sum(d), uniform=uniform)

if __name__ == "__main__":
    for name, seeds in M_SEEDS.items():
        r = analyse(seeds)
        print(f"{name:10s} T={r['T']:3d} p={r['p']} c={r['c']} distinct={r['distinct']} "
              f"s={r['s']} d={r['d']} sumd={r['sumd']} uniform={r['uniform']}")
        print(f"           part={r['part']}")
