"""Referee T691: the central face of a C3 arrangement (T688, T689 checks)."""
from fractions import Fraction as F
from referee_t691_checks import build, M_SEEDS
from kobon import verify


def clip(poly, a, b, c, keep_sign):
    """Keep the part of poly with sign(a x + b y - c) == keep_sign (or 0)."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp = a * p[0] + b * p[1] - c
        fq = a * q[0] + b * q[1] - c
        sp = (fp > 0) - (fp < 0)
        sq = (fq > 0) - (fq < 0)
        if sp != -keep_sign:
            out.append(p)
        if sp * sq == -1:
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def central_face(lines, R=10 ** 7):
    R = F(R)
    poly = [(-R, -R), (R, -R), (R, R), (-R, R)]
    for (a, b, c) in lines:
        a, b, c = F(a), F(b), F(c)
        assert c != 0, "origin lies on a line"
        keep = 1 if -c > 0 else -1
        poly = clip(poly, a, b, c, keep)
    # drop duplicate and collinear vertices
    ded = []
    for p in poly:
        if not ded or ded[-1] != p:
            ded.append(p)
    if len(ded) > 1 and ded[0] == ded[-1]:
        ded.pop()
    out = []
    n = len(ded)
    for i in range(n):
        o, p, q = ded[i - 1], ded[i], ded[(i + 1) % n]
        cross = (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
        if cross != 0:
            out.append(p)
    return out


def bounding_lines(lines, verts):
    idx = []
    for i, (a, b, c) in enumerate(lines):
        a, b, c = F(a), F(b), F(c)
        if sum(1 for v in verts if a * v[0] + b * v[1] == c) >= 2:
            idx.append(i)
    return idx


if __name__ == "__main__":
    for name in ["T681_91", "T682_93", "T683_88", "T685_91", "T689_79", "T669_84", "T686_88"]:
        L = build(M_SEEDS[name])
        v = central_face(L)
        bl = bounding_lines(L, v)
        d2 = sorted(((F(c) ** 2) / (F(a) ** 2 + F(b) ** 2), i) for i, (a, b, c) in enumerate(L))
        print(f"{name}: central face sides={len(v)} bounded by {bl} "
              f"three nearest lines={[i for _, i in d2[:3]]}")
