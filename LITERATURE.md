# Literature packet

Both agents receive this file in full. It exists so neither of you burns turns
rediscovering results from 2007.

## The problem

N(k) is the maximum number of nonoverlapping triangles whose sides lie on an
arrangement of k lines in the Euclidean plane. Posed by Kobon Fujimura. Open in
general.

## Upper bounds

- **Tamura:** `N(k) <= floor(k(k-2)/3)`.
- **Clement and Bader (2007):** the Tamura bound is unachievable for
  `k = 0, 2 (mod 6)`, reducing it by one there. By residue class:
  - `k = 3, 5 (mod 6)`: `k(k-2)/3`
  - `k = 0, 2 (mod 6)`: `(k+1)(k-3)/3`
  - `k = 1, 4 (mod 6)`: `(k^2 - 2k - 2)/3`
- **Improved even-k bound:** `N(k) <= floor(k(k - 7/3)/3)`, exactly
  `(k(3k-7)) // 9` in integers.

## Prior art you must not reinvent

- **Savchuk (2025), arXiv:2507.07951.** Compact table notation for pseudoline
  arrangements. A heuristic straightening tool recovering straight-line
  arrangements from a table, able to enforce symmetry. A SAT encoding of the
  optimal-table search, solved with Kissat, used both to find solutions and to
  prove none exists. Results: new optimal arrangements for k=23 and k=27;
  confirmed no optimal solution for k=11. **A bare "let us SAT-encode it"
  proposal is not a contribution. State what you would encode differently and
  why Kissat did not already find it.**
- **Forge and Ramirez Alfonsin (1998).** Straight line arrangements in the real
  projective plane.
- **Bartholdi, Blanc, Loisel (2008).** Simple arrangements of lines and
  pseudolines. Relevant to whether a pseudoline solution straightens.
- **Felsner and Goodman (2017).** Pseudoline Arrangements, in the Handbook of
  Discrete and Computational Geometry. Standard reference for order types,
  allowable sequences, and wiring diagrams.

## The gap between pseudolines and lines

A table or wiring diagram gives a **pseudoline** arrangement. Not every
pseudoline arrangement is stretchable to straight lines; stretchability is
decidable but complete for the existential theory of the reals. Any argument
that produces a table owes an account of stretchability. Any impossibility
argument that only rules out pseudoline arrangements proves something strictly
stronger than needed, which is fine, but an argument that rules out only
straight-line arrangements does not transfer back to tables.

## Useful identities

For a simple arrangement of k lines: `k(k-1)/2` vertices, `k^2` edges,
`(k^2 + k + 2)/2` faces of which `(k-1)(k-2)/2` are bounded. Euler's relation
on the arrangement graph is the usual source of counting obstructions.
Non-simple arrangements, with parallel lines or multiple lines through a point,
are permitted and Savchuk's table notation covers them.
