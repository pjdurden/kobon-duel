# Known values for the Kobon triangle problem

N(k) is the maximum number of nonoverlapping triangles whose sides lie on an
arrangement of k lines in the Euclidean plane.

**This file is read-only to the debate agents.** A value changes only when the
phase-2 verifier confirms a new arrangement and the owner accepts it.

## Upper bounds

- Tamura: `N(k) <= floor(k(k-2)/3)`.
- Clement and Bader (2007): the Tamura bound is unachievable for
  `k = 0, 2 (mod 6)`, reducing it by one there.
- Improved even-k bound: `N(k) <= floor(k(k - 7/3)/3)`, integer-exact as
  `(k*(3k-7)) // 9`.

The "best UB" column is the tightest published upper bound: the improved even-k
bound for even k, Tamura for odd k, except k=11 where Savchuk (2025) proved the
bound of 33 unreachable.

## Table

| k | Tamura UB | best UB | best known | status | source |
|---|---|---|---|---|---|
| 3 | 1 | 1 | 1 | CLOSED | classical |
| 4 | 2 | 2 | 2 | CLOSED | classical |
| 5 | 5 | 5 | 5 | CLOSED | classical |
| 6 | 8 | 7 | 7 | CLOSED | Clement-Bader 2007 |
| 7 | 11 | 11 | 11 | CLOSED | classical |
| 8 | 16 | 15 | 15 | CLOSED | Clement-Bader 2007 |
| 9 | 21 | 21 | 21 | CLOSED | classical |
| 10 | 26 | 25 | 25 | CLOSED | improved even bound |
| 11 | 33 | 32 | 32 | CLOSED | Savchuk 2025, 33 shown unreachable |
| 12 | 40 | 38 | 38 | CLOSED | improved even bound |
| 13 | 47 | 47 | 47 | CLOSED | classical |
| 14 | 56 | 54 | 53 | OPEN | gap of 1 |
| 15 | 65 | 65 | 65 | CLOSED | classical |
| 16 | 74 | 72 | 72 | CLOSED | improved even bound |
| 17 | 85 | 85 | 85 | CLOSED | classical |
| 18 | 96 | 94 | 93 | OPEN | gap of 1 |
| 19 | 107 | 107 | 107 | CLOSED | classical |
| 20 | 120 | 117 | 116 | OPEN | gap of 1 |
| 21 | 133 | 133 | 133 | CLOSED | classical |
| 23 | 161 | 161 | 161 | CLOSED | Savchuk 2025 |
| 25 | 191 | 191 | 191 | CLOSED | classical |
| 27 | 225 | 225 | 225 | CLOSED | Savchuk 2025 |
| 29 | 261 | 261 | 261 | CLOSED | classical |
| 31 | 299 | 299 | 299 | CLOSED | classical |
| 33 | 341 | 341 | 341 | CLOSED | classical |

## The three open cases

k = 14, 18, 20. In each, the tightest published upper bound exceeds the best
known construction by exactly one triangle. Two ways to close each:

1. Exhibit an arrangement meeting the bound (54 on 14 lines, 94 on 18, 117 on 20).
2. Prove the bound unreachable, settling N(k) at the best-known value.

## Sources

- Tamura, upper bound, as cited in the standard references.
- G. Clement and J. Bader (2007), "Tighter Upper Bound for the Number of Kobon
  Triangles".
- D. Forge and J. L. Ramirez Alfonsin (1998), "Straight line arrangements in
  the real projective plane", Discrete and Computational Geometry 20(2) 155-161.
- N. Bartholdi, J. Blanc, S. Loisel (2008), "On simple arrangements of lines
  and pseudo-lines".
- P. Savchuk (2025), "Constructing Optimal Kobon Triangle Arrangements via
  Table Encoding, SAT Solving, and Heuristic Straightening", arXiv:2507.07951.
- OEIS A006066, A032765.
- S. Felsner and J. E. Goodman (2017), "Pseudoline Arrangements", Handbook of
  Discrete and Computational Geometry.

Machine-readable tables for the arrangements above are vendored in
`corpus/arrangements.json`, imported from zegalur/line-order under CC BY 4.0.
Per-arrangement attribution is in `corpus/ATTRIBUTION.md`.
