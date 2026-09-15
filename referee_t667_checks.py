"""REFEREE turn 667: symmetry audit of turns 664-666.

(a) point reflection: every point-symmetric arrangement has even T  (T664/T665)
(b) order-3: an affine order-3 map fixes NO line, hence 3 | k  (refutes T664's
    "f = 0 or 1, for k=13 f=1" and T666's "k=20 is open to this family")
(c) an honest order-3 k=18 hillclimb, coordinates printed

Run: python3 referee_t667_checks.py
"""
import random
from fractions import Fraction as F
from kobon import verify

random.seed(667)


def sec(s):
    print()
    print("=" * 74)
    print(s)


# ---------------------------------------------------------------- helpers
# line (a,b,c) means a*x + b*y = c
def mat_mul(M, N):
    return [[sum(M[i][k] * N[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def mat_vec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


def inv2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return [[F(M[1][1], 1) / d, F(-M[0][1], 1) / d],
            [F(-M[1][0], 1) / d, F(M[0][0], 1) / d]]


def transpose(M):
    return [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]


def map_line_linear(M, line):
    """image of {x : n.x = c} under x -> Mx  is  {y : (M^-T n).y = c}"""
    a, b, c = line
    MiT = transpose(inv2(M))
    n = mat_vec(MiT, (F(a), F(b)))
    return (n[0], n[1], F(c))


def same_line(l1, l2):
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    return a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1


def point_reflect_line(center, line):
    """image of line under x -> 2c - x: same normal, c' = 2 n.center - c"""
    a, b, c = line
    return (F(a), F(b), 2 * (F(a) * center[0] + F(b) * center[1]) - F(c))


# ---------------------------------------------------------------- (a)
sec("667(a)  point symmetry: T is even, on arrangements I built myself")
print("  proof steps checked:")
print("   1. point reflection about C sends n.x=c to n.x=2n.C-c: SAME normal")
print("      -> partner is parallel (or equal); equal iff C lies on the line")
print("   2. so the fixed lines are exactly the lines through C, and any two")
print("      lines of a swapped pair never meet")
print("   3. an involution on a 3-element set has a fixed point, so a triple")
print("      fixed setwise has >=1 fixed line; either all 3 fixed (concurrent")
print("      at C, no face) or 1 fixed + 1 parallel pair (no face)")
print("   4. hence no triangular face is fixed; all orbits have size 2; T even")
print()

cases = []
for trial in range(14):
    C0 = (F(random.randint(-3, 3)), F(random.randint(-3, 3)))
    nfix = random.choice([0, 1, 2, 3])
    npair = random.randint(2, 5)
    lines = []
    for _ in range(nfix):                       # lines through the centre
        a, b = random.randint(-9, 9), random.randint(-9, 9)
        if (a, b) == (0, 0):
            a = 1
        lines.append((F(a), F(b), F(a) * C0[0] + F(b) * C0[1]))
    for _ in range(npair):
        a, b = random.randint(-9, 9), random.randint(-9, 9)
        if (a, b) == (0, 0):
            a = 1
        c = F(random.randint(-20, 20))
        L = (F(a), F(b), c)
        lines.append(L)
        lines.append(point_reflect_line(C0, L))
    # drop duplicates
    uniq = []
    for L in lines:
        if not any(same_line(L, U) for U in uniq):
            uniq.append(L)
    if len(uniq) < 4:
        continue
    # confirm the set really is invariant
    inv = all(any(same_line(point_reflect_line(C0, L), U) for U in uniq)
              for L in uniq)
    T = verify.count(uniq)
    cases.append((len(uniq), nfix, T, inv))
    print("   k=%2d  centre-lines=%d  invariant=%s  T=%3d  %s"
          % (len(uniq), nfix, inv, T, "EVEN" if T % 2 == 0 else "*** ODD ***"))
print("   odd counts found: %d of %d" % (sum(1 for c in cases if c[2] % 2), len(cases)))

# ---------------------------------------------------------------- (b)
sec("667(b)  order 3: how many lines can an affine order-3 map fix?")
M = [[0, 1], [-1, -1]]            # T666's rational companion matrix
M2 = mat_mul(M, M)
M3 = mat_mul(M2, M)
print("   T666's M = [[0,1],[-1,-1]],  det = %d,  M^3 = %s"
      % (M[0][0] * M[1][1] - M[0][1] * M[1][0], M3))

print()
print("   A line n.x=c is fixed by x->Mx iff M^-T n is parallel to n AND the")
print("   offsets agree.  Fixed direction => n is a real eigenvector of M^-T,")
print("   i.e. M has a real eigenvalue.  char poly of M is x^2+x+1, whose")
print("   roots are the primitive cube roots of unity: NO real eigenvalue.")
print("   Same for a Euclidean 120 degree rotation (eigenvalues e^{+-2pi i/3}).")
print("   General affine order-3 map: it has a fixed point (average of an")
print("   orbit), so conjugate it to a linear map about that point; a linear")
print("   map of order 3 that is not the identity has minimal polynomial")
print("   x^2+x+1, hence no real eigenvalue, hence no invariant direction.")
print("   => f = 0 ALWAYS, and the k lines split into orbits of size 3:  3 | k")
print()
print("   numeric confirmation, 4000 random lines, T666's M and a true 120deg")
print("   rotation about 3 different centres:")

fixedM = 0
for _ in range(4000):
    a, b = random.randint(-30, 30), random.randint(-30, 30)
    if (a, b) == (0, 0):
        continue
    L = (F(a), F(b), F(random.randint(-30, 30)))
    if same_line(L, map_line_linear(M, L)):
        fixedM += 1
print("   lines fixed by M                     : %d of 4000" % fixedM)

# true 120-degree rotation, exact: use the algebraic number field Q(sqrt(-3))
# represented as a+b*sqrt(3); do it numerically at high precision instead.
import math
fixedR = 0
for _ in range(4000):
    a, b = random.uniform(-30, 30), random.uniform(-30, 30)
    c = random.uniform(-30, 30)
    cx, cy = random.choice([(0.0, 0.0), (1.5, -2.0), (7.0, 7.0)])
    th = 2 * math.pi / 3
    co, si = math.cos(th), math.sin(th)
    # rotation about (cx,cy): x -> R(x-C)+C ; normal n -> R n (R orthogonal)
    na, nb = a * co - b * si, a * si + b * co
    # offset: n'.y = c' where y = R(x-C)+C ; c' = c + n'.C - n.C
    cp = c + (na * cx + nb * cy) - (a * cx + b * cy)
    # same line?
    if abs(a * nb - na * b) < 1e-9 and abs(a * cp - na * c) < 1e-9:
        fixedR += 1
print("   lines fixed by a 120 degree rotation : %d of 4000" % fixedR)

print()
for k in (13, 18, 20):
    print("   k=%2d :  k mod 3 = %d  ->  order-3 symmetric arrangement %s"
          % (k, k % 3, "POSSIBLE" if k % 3 == 0 else "IMPOSSIBLE (f=0 forced)"))
print()
print("   T664: 'At k=13, f=1, four orbits, b <= 4 ... Order-3 is NOT excluded'")
print("   T665: endorsed, asked for the same computation at k=20")
print("   T666: '(20-f)%3==0 only at f=2 ... 117 achievable ... k=20 is open")
print("          to this family arithmetically'")
print("   -> f=2 requires two fixed lines.  There are none.  k=13 and k=20 are")
print("      BOTH excluded outright.  k=18 survives because 3 | 18.")

# ---------------------------------------------------------------- (c)
sec("667(c)  order-3 k=18: my own hillclimb, seeds printed")


def orbit_lines(seeds):
    out = []
    for s in seeds:
        L = (F(s[0]), F(s[1]), F(s[2]))
        out.append(L)
        L2 = map_line_linear(M, L)
        out.append(L2)
        out.append(map_line_linear(M, L2))
    return out


def ok_simple(lines):
    """distinct lines, no two parallel, no three concurrent"""
    n = len(lines)
    for i in range(n):
        for j in range(i + 1, n):
            if verify.intersect(lines[i], lines[j]) is None:
                return False
    pts = {}
    for i in range(n):
        for j in range(i + 1, n):
            p = verify.intersect(lines[i], lines[j])
            pts.setdefault(p, []).append((i, j))
    return all(len(v) == 1 for v in pts.values())


def score(seeds):
    L = orbit_lines(seeds)
    if len(set(L)) != 18 or not ok_simple(L):
        return -1
    return verify.count(L)


best = None
for restart in range(6):
    while True:
        seeds = [(random.randint(-12, 12), random.randint(-12, 12),
                  random.randint(-12, 12)) for _ in range(6)]
        s = score(seeds)
        if s > 0:
            break
    for step in range(220):
        i = random.randrange(6)
        j = random.randrange(3)
        cand = [list(t) for t in seeds]
        cand[i][j] += random.choice([-2, -1, 1, 2])
        cand = [tuple(t) for t in cand]
        sc = score(cand)
        if sc >= s:
            seeds, s = cand, sc
    print("   restart %d: T = %d   seeds %s" % (restart, s, seeds))
    if best is None or s > best[0]:
        best = (s, seeds)

print()
print("   best order-3 k=18 arrangement found: T = %d" % best[0])
print("   seeds (a,b,c) for a*x+b*y=c, each generating an M-orbit of 3:")
for s in best[1]:
    print("       %s" % (s,))
L = orbit_lines(best[1])
print("   18 lines distinct: %s   simple: %s   verify.count = %d"
      % (len(set(L)) == 18, ok_simple(L), verify.count(L)))
print("   Tamura UB(18) = 96, best-known 93, target 94.")
print("   T666 reported T = 73 from a 600-step climb and printed NO seeds.")
