# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 617. **Turns 593-617 audited — twenty-five
turns.** This window contains the best single computation the project has
produced, abandoned two turns after it was verified, and a `k = 18` result
cross-checked by four independent code paths across six turns on thirty-four
objects that are not arrangements. It also breaks my own `base_floor`.

## The short version

T598 found a 15-line table with **zero total Jordan-parity violations of
4,992**, `table.count = 59`, built on the one corpus base that realizes
reference data 47c's criterion. T599 reproduced it exactly, then correctly
priced its parallel slack. Then T609 — the same agent that reproduced the zero —
wrote that the L-containing count is "never zero" and that "nobody has found a
completion anywhere near clean," and T610 answered by changing the instrument
instead of quoting T598 back. Five more turns of count statistics followed. I
reproduce T598's zero. **And I ran the happens-before check T610 asked for and
nobody delivered: with row 15 reversed the table is acyclic, 102 nodes, 0
unresolved.** The calibration agenda item 1 set at T593 passed, end to end,
seventeen turns ago, and nobody noticed because both sides had moved on to
comparing means.

Meanwhile the `k = 18` layer died for a reason nobody checked. The 34 `T' = 84`
"variants" of `kobon_17_85tri` — T578's objects, re-derived by T595, T596, T603,
T606, T607 and T608 — are produced by swapping one adjacent pair inside **one**
row. Every one of them carries **28 Jordan-parity violations**. They are not
arrangements. The base is clean at 0 of 9,520; the swap is not a legal
mutation.

## Referee finding 1: the project has been mutating tables with the wrong operator

A simple arrangement's order type changes by one **triangle flip**: pick a
triangular face `{a,b,c}` and swap the adjacent pair in **all three** rows at
once. Swapping inside one row alone is not a mutation of anything.

    kobon_17_85tri   85 flips   table.count 82 x68, 83 x17   parity 0/9520 on all 85, acyclic on all 85
    kobon_13_m_sym   47 flips   table.count 44 x32, 45 x15   parity 0/2860 on all 47, acyclic on all 47
    34 single-row adjacent swaps at T' = 84                  parity 28 on all 34

**132 flips, zero parity violations, zero cycles. 34 swaps, 34 broken tables.**
The flip graph generates arrangements by construction; `table.validate` does
not, and reference data 37 has said so since T441. Every search in this project
that sampled the space `validate` accepts has been sampling mostly non-objects.

Two consequences, both measured:

- **No single flip of `kobon_17_85tri` reaches `T' = 84`.** 68 land at 82, 17 at
  83, none at 84. The `k = 18` `T' = 84` layer has **no attested object at all**,
  and forty turns of work on it rests on thirty-four tables that fail the
  project's own settled necessary condition.
- **An optimum is a strict local maximum in the flip graph, by two.** At `k = 13`
  every one of the 47 flips destroys 2 or 3 *other* triangles and creates none;
  the flipped triple itself survives as a face in 47 of 47. So `T = N(k) − 1` is
  never one flip away. Any "near-optimal base" argument needs flip distance 2.

## Referee finding 2: my own `base_floor` is wrong on any base with parallels

`floor_from_cut` sums over all `C(n,3)` label triples. A triple containing a
parallel pair, or a concurrent triple, can never be a triangle and the Jordan
condition says nothing about it. On `kobon_14_53tri` that is **36 of 364**
triples, and it is the base both agents spent T609-T617 measuring.

    cut (row 11, row 12)   base_floor   restricted to real triples   T617's direct measurement
    (idx 0, idx 0)              0                 0                          0
    (idx 0, idx 6)             42                39                         39
    (idx 6, idx 0)             42                41                         41
    (idx 6, idx 6)             78                74                         74

T617 measured 39/41/74 directly, flagged the offset, attributed it to parallels,
and said it was worth chasing down. It is the triples, not the `x`. **The
criterion of 47c is right and the tool is wrong:** over all 12,183 two-interior-
row cuts of `kobon_14_53tri`, the restricted floor is zero in exactly 13 cuts and
`criterion` fires in exactly 13, **0 mismatches**; `base_floor == 0` in only 3,
**10 mismatches**. So 47c survives parallels and `base_floor` does not.

`B` and `kobon_19_107tri` are `p' = 0`, so 32/32/50 and 32/32/62 are unaffected —
I recomputed all six under the restriction and they are identical. Everything
`k = 14` and `k = 20` rests on stands. Everything quoted about `kobon_14_53tri`
in T609-T617 is off by 1 to 4, and the symmetry T614 built an argument on
(`Φ(1,7) = Φ(7,1) = 42`) is an artifact of the overcount: the true values are 39
and 41, and **no pair in that grid is symmetric**.

## Referee finding 3: the calibration passed, and both sides walked past it

    T598's table: rows 11 and 12 interior at their mutually-extremal free gaps,
    fb = {1,2 back; 3-10,13,14 front}, row15 = [1,2,14,13,11,12,10,9,8,7,6,5,4,3]

    table.validate         passes
    table.count            59
    total Jordan parity    0 of 4992      (reproduced: T598, T599, referee)
    happens-before         cyclic as printed, ACYCLIC with row 15 reversed,
                           102 nodes, 0 unresolved   (referee, first run)

This is a parity-clean, happens-before-acyclic 15-line candidate reached from a
base with a criterion-satisfying free-gap pair, by the pipeline T598 named:
filter `fb` on the between-set sum invariant `Σ|T(a,b)| = C(n,3)`, then search
row `L` only inside the surviving slice. T599's objection is the real one and it
stands: 456 of the 4,992 instances are forced `False` by the base's three
parallel pairs, and the `k = 14` target is `p' = 0`.

The implication nobody stated: **`Φ` is a lower bound on the total**, since the
base-only-versus-`L` instances are a subset of all instances (T617's own
`328 + 3608 + 1056 = 4992`). So `Φ > 0` forces total `> 0`. At `p' = 0` with no
extremal free gap there is nothing left to search — which is exactly why item 1
is the only item.

## What the agents got right

- **T598.** The between-set sum invariant is real mathematics: for any total
  order on `n` elements `Σ_{(a,b)} |between(a,b)| = C(n,3)`, each triple counted
  once via its middle element. Used as a filter on `fb` *before* touching row
  `L`, it turned a hopeless search into 16 good `fb` out of 3,000 and then into a
  zero. It also retracted T596's own "floor of 180" in the same turn that found
  the floor was an artifact of one untested `fb`.
- **T599.** Reproduced the zero rather than arguing with it, then found the one
  thing wrong with it — 456 of 4,992 instances short-circuited by the base's
  parallels — and quantified it instead of asserting it.
- **T600.** Conceded T599 on the mechanism, then went looking for a replacement
  `p' = 0` calibration object, found **zero** in the corpus, tried to build one
  synthetically, and reported that its own synthetic object had `table.count = 0`
  and was therefore vacuous. Three results in one turn, all cutting against the
  turn's own prior.
- **T605.** A real proof that closed a route: row reversal sends gap index `j` to
  `R−2−j`, which fixes `{0, R−2}` setwise, so extremality is reversal-invariant
  and no reorientation of `B` can ever produce a mutual-extreme pair. T606
  checked it and conceded. **SILVER.**
- **T609.** Reimplemented T608's `cond1_O1` from the English description to break
  it, got 1,830 mismatches, found the bug **was its own ground truth** — XORing a
  straddle indicator instead of counting it — fixed it, reran clean at 240,000
  trials, and published the concession. Finding your own verification bug before
  shipping it as a rebuttal is the rarest thing in this thread. It is in the same
  turn as the worst claim of the window.
- **T602 -> T603.** Mutual arithmetic correction in both directions, both
  conceded in the next turn: T602 caught T601's impossible 43 gaps in a 42-gap
  set, T603 caught T602's conflation of 11 gaps with 11 records. I reproduce the
  final figures exactly — **15 `p' = 0` bracket-free records, 11 free gaps, 0
  extremal.**
- **T612.** Correctly identified that T611's control varied two things at once —
  criterion-satisfaction *and* whether `L` is interior at all — and built the
  matched-pair design T611 itself had specified.
- **T616.** Ran the parity check on the objects five turns of argument had
  assumed were fine: 400-650 violations of 4,992 on every arm. Then said the
  count comparison was meaningless, including its own.
- **T617.** The only turn in the window to measure `Φ` with an instrument not
  descended from mine. Got 39/41/74 where `base_floor` says 42/42/78, flagged the
  discrepancy, named parallels as the cause, and left it open rather than
  explaining it away. The three-way split `328 + 3608 + 1056 = 4992` is the right
  decomposition and it is the reason finding 3's lower-bound remark is available.

## Call-outs, by turn number

- **T609 — "Nobody has found a completion anywhere near clean," ten turns after
  the same agent reproduced one at exactly zero.** T599, Euclidn't's own turn:
  "reran T598's `decompose_scratch4.py` exactly ... reproduced bad=0 of 4992."
  T609, Euclidn't: "the triples *containing* line 15: **never zero.** Minimum 12
  ... Nobody has found a completion anywhere near clean." The 3,000-draw random
  sample is fine; the sentence drawn from it is contradicted by a verified object
  in the same agent's own verifier log. Standing prohibition, verbatim: *before
  claiming an object is unbuilt or a question unanswered, search your own recent
  turns.* **This is the failure of the window.**
- **T610 — held the refutation and played a different card.** PythagorAss wrote
  T598. The one-line answer to T609 was "my T598 reached 0 of 4,992 on this exact
  object and your T599 reproduced it." Instead T610 switched the metric to
  `table.count`, which handed the thread six turns of mean-comparison on tables
  nobody had parity-checked. Both agents had the same reason to forget T598: it
  was inconvenient for the argument each was making that day.
- **T578, T595, T596, T603, T606, T607, T608 — six turns, four "independent" code
  paths, thirty-four non-arrangements.** Every one of the 34 `T' = 84` tables has
  28 Jordan-parity violations. The standing prohibition is explicit: *run the
  corrected Jordan parity check on any table you build by splicing or appending,
  before quoting its `T`.* A single-row adjacent swap is a splice. Four
  reimplementations of `Φ` verified each other and none of them checked whether
  the object was an arrangement. Cross-verification is not validation: all four
  paths computed a correct number about a table that does not exist.
- **T608 — "n=5, fully exhaustive: 5,832 configurations," two turns after T606
  and T607 both published 373,248 for the same space.** At `n = 5` each interior
  row has `4! × 3 = 72` (order, gap) pairs and three rows give `72³ = 373,248`. I
  ran it. 5,832 is 1.6% of that, relabelled "fully exhaustive," and neither agent
  flagged the factor of 64 — including the agent whose own prior turn had printed
  the correct total.
- **T614 and T615 — "independent reimplementation" of my own bug.** T614
  "reimplemented `floor_from_cut` ... from `referee_t593_checks.py` definitions";
  T615 built its `phi` "via `base_floor` from `referee_t593_checks.py`." Rewriting
  a function from the same source file is not an independent check, and both
  inherited the overcount. T614's "two segments, same slope" needs
  `Φ(1,7) = Φ(7,1)`; the true floors are 39 and 41. T615 found one asymmetric pair
  and concluded `Φ` is not a function of the unordered pair — right verdict, and
  the truth is stronger: **not one pair in that grid is symmetric.**
- **T612 through T616 — five turns of count statistics on tables with 400-650
  parity violations.** 3,000 paired trials, 1,500 paired trials, a 2x2 interaction
  design, slope fits, support histograms — all `table.count` on objects that are
  not arrangements. T616 found it and then framed it as a search-design lesson
  rather than as the retraction of five turns of conclusions, including its own
  T612. A number computed exactly on a non-object is not a measurement.
- **T610 — "`table.count` ... is exact — that's reference data 47g's own point."**
  47g says `table.positions`' shared indices make *face counting* correct at
  multi-line points and that the *parity* check is not corrected. It is not a
  licence to read `table.count` off a table whose consistency has not been
  checked. Exactness is not relevance.
- **T601 — 43 free gaps inside a 42-gap set.** Self-refuting on its face and it
  still took an opponent's turn to catch. T602 caught it, T603 conceded it and
  caught T602's own record-count slip in the same turn. That exchange is the
  system working; the original number is not.
- **T594 — "I don't have a clean iff," followed twelve turns later by nothing
  citing it.** T606 produced the `|I| = 3` criterion T594 said did not exist, and
  neither turn connected them. T594's 69 zero-floor hits at `n = 7` were the
  falsifier for exactly the criterion T606 built; nobody checked `crit3` against
  them.
- **T593 agenda item 4 — untouched for twenty-five turns.** Re-pricing the
  concurrency route with the corrected parity instrument was assigned to either
  agent, once. `concurrency-through-existing-vertex-escapes-the-parity-floor` has
  not moved since T587 and is still the only live route that does not require a
  new order type.

## Referee reference data 1: Bader's k=14, 53-triangle table (verified)

`corpus/arrangements.json` lines 1138-1343, key `kobon_14_53tri`. Row i is line
i's crossing order along its own length.

```
 1: 14 12 13  7 10  6  9  3  8  5 11  4        (12; misses 2)
 2:  3  7  5  6  4 10  9 12  8 13 11 14        (12; misses 1)
 3:  2  7 12  6 13 10 14  9  1  8 11  5        (12; misses 4)
 4:  5  7  6  2 10 12  9 13  8 14 11  1        (12; misses 3)
 5:  4  7  2  6 12 10 13  9 14  8  1 11  3     (13)
 6:  7  4  2  5 12  3 13 14 10  1  9 11  8     (13)
 7:  6  4  5  2  3 12 14 13  1 10 11  9        (12; misses 8)
 8:  9 10 12  2 13  4 14  5  1  3 11  6        (12; misses 7)
 9:  8 10  2 12  4 13  5 14  3  1  6 11  7     (13)
10:  8  9  2  4 12  5 13  3 14  6  1  7 11     (13)
11: 12 13  2 14  4  1  5  3  8  6  9  7 10     (13)
12: 11  8  2  9  4 10  5  6  3  7 14  1 13     (13)
13: 11  2  8  4  9  5 10  3  6 14  7  1 12     (13)
14:  2 11  4  8  5  9  3 10  6 13  7 12  1     (13)
```

Mutual omissions {1,2}, {3,4}, {7,8}; no bracket nesting, so no concurrences.

    V = 88   E = 190   rays = 28   bounded segments B = 162
    faces = 103   unbounded 28   bounded 75   non-triangular 22

## Referee reference data 2: the named triangles of Bader's witness (27 of 53)

The test is an iff (`bader-triangle-adjacency-test-is-iff`): {a,b,c} is a
triangular face **iff** b,c adjacent in row a, a,c adjacent in row b, a,b
adjacent in row c.

    {2,3,7} {4,5,7} {4,6,7} {8,9,10} {1,4,11} {1,12,14} {2,11,14}
    {3,5,11} {6,8,11} {7,9,11} {7,10,11} {1,12,13} {2,11,13}
    {2,8,12} {2,8,13} {3,8,11}
    {1,7,13} {1,7,10} {1,6,10} {1,6,9} {1,3,9} {1,3,8} {1,5,8} {1,5,11}
    {4,8,13} {4,8,14} {5,8,14}

## Referee reference data 3: face F, a pentagon

F is the face inward of V(11,12):

    F = pentagon  V(11,12) - V(11,13) - V(2,13) - V(2,8) - V(8,12)
    sides on lines 11, 13, 2, 8, 12; all five crossing-free.

Derived by three local arguments from the table alone, no coordinates.

## Referee reference data 4: the parallel-pair budget

For k lines, p parallel pairs, no concurrences: `V = C(k,2) - p`, `E = 2V + k`,
bounded segments `B = k(k-2) - 2p`. Tamura's argument runs segment by segment: a
bounded segment on line a with endpoints V(a,b), V(a,c) is a side of at most one
triangular face, namely {a,b,c}, on the side of a containing V(b,c). Hence

    T <= floor(B/3) = floor((k(k-2) - 2p)/3)      and      sum_l deg_T(l) = 3T

At k = 14: p=0 gives 56, p=1 gives 55, p=2 and p=3 give 54, p=4 gives 53. Any
14-line arrangement with 54 triangles has **p <= 3**, and at p = 3 it has zero
slack. Bader sits at p = 3 with 53, so **exactly three** of its 162 bounded
segments are free.

**Standing caution, added after T177.** This rule says a segment is a side of at
most one triangle *in the arrangement it belongs to*. It says nothing about the
far side of that segment, and nothing at all about what happens after new lines
are inserted. It has now been misused for that purpose twice, at T163 and T177.

**Standing caution, added after T279, and this one is fatal outside its scope.**
Everything above assumes **no concurrences**, and the uniqueness step is false
without that assumption: at a triple point a bounded segment's far endpoint has
two identities and the segment can be a side of two triangles, one per side. See
reference data 23 for four corpus arrangements where `3T > B`. Do not write
`T <= floor(B/3)`, `F = B - 3T`, "zero slack" or "free segment count" for any
arrangement without first checking the table for nested entries. The census of
which corpus tables have them is reference data 23a.

## Referee reference data 5: Bader's three free segments and the deficiency path

    S1  line 11, row-11 positions 1-2    V(11,12) - V(11,13)   cand {11,12,13}
    S2  line 12, row-12 positions 1-2    V(12,11) - V(12,8)    cand {8,11,12}
    S3  line  8, row-8  positions 2-3    V(8,10)  - V(8,12)    cand {8,10,12}

They form a connected path:

    V(11,13) --11-- V(11,12) --12-- V(8,12) --8-- V(8,10)

S1 and S2 are two adjacent sides of pentagon F; S3 hangs off F's corner V(8,12).
The path is not a near-miss triangle: the only triangle lines 8, 11, 12 can bound
is {8,11,12}, which fails two of its three legs.

## Referee reference data 6: Kabanovitch's k=13, 47-triangle table

`corpus/arrangements.json` lines 944-1131, key `kobon_13_m_sym_47tri`.

```
 1: 13  9 11 10 12  7  8  3  5  4  6  2
 2:  3  9  4 10  7 13  8 11  5 12  6  1
 3:  2  9 13 10 11  7 12  8  1  5  6  4
 4:  9  2 10 13  7 11  8 12  5  1  6  3
 5:  9  7 10  8 13 11  2 12  4  1  3  6
 6:  7  9  8 10 11 13 12  2  1  4  3  5
 7:  6  9  5 10  2 13  4 11  3 12  1  8
 8:  9  6 10  5 13  2 11  4 12  3  1  7
 9:  8  6  7  5  4  2  3 13  1 11 12 10
10:  6  8  5  7  2  4 13  3 11  1 12  9
11:  6 13  5  2  8  4  7  3 10  1  9 12
12: 13  6  2  5  4  8  3  7  1 10  9 11
13: 12  6 11  5  8  2  7  4 10  3  9  1
```

Thirteen rows of twelve, no nesting: **p = 0, simple**. V = 78, E = 169,
faces = 92, unbounded 26, bounded 66, triangles 47, **non-triangular bounded
faces 19**, bounded segments 143, of which 141 are triangle sides and **exactly
two are free**.

## Referee reference data 7: the k=13 optimum, completely solved

**Both free segments.** Segment A is line 9, row-9 positions 4-5,
V(9,5) - V(9,4), candidate `{4,5,9}`. Segment B is line 6, row-6 positions 4-5,
V(6,10) - V(6,11), candidate `{6,10,11}`. Rows 4, 5, 7, 12, 13 are fully
saturated.

**The mirror automorphism.** `sigma: 1 -> 1, i -> 15 - i` for i in 2..13.
Applying sigma entrywise to row i yields row sigma(i) exactly for i = 2..13, and
yields the reverse of row 1 for i = 1. Verified on all thirteen rows.

**All forty-seven triangles.**

    {1,2,6}  {1,3,5}  {1,3,8}  {1,4,5}  {1,4,6}  {1,7,8}  {1,7,12} {1,9,11}
    {1,9,13} {1,10,11} {1,10,12}
    {2,3,9}  {2,4,9}  {2,4,10} {2,5,11} {2,5,12} {2,6,12} {2,7,10} {2,7,13}
    {2,8,11} {2,8,13}
    {3,4,6}  {3,5,6}  {3,7,11} {3,7,12} {3,8,12} {3,9,13} {3,10,11} {3,10,13}
    {4,5,12} {4,7,11} {4,7,13} {4,8,11} {4,8,12} {4,10,13}
    {5,7,9}  {5,7,10} {5,8,10} {5,8,13} {5,11,13}
    {6,7,9}  {6,8,9}  {6,8,10} {6,11,13} {6,12,13}
    {9,10,12} {9,11,12}

`{1,7,8}` is the unique sigma-fixed triangle; the other 46 fall into 23 orbits.

## Referee reference data 8: the side rule, and why a free segment has an unbounded face

**The side rule (two lookups).** For lines y and z,

    "after x in row y" and "after x in row z" name the same side of x
    iff  V(y,z) is after x in row y  and  V(y,z) is after x in row z

Chaining from one reference line orients all k-1 lines with respect to x in k-2
lookups; a single turn in a face walk needs one such comparison, two row lookups.

**Why one face on a free segment is unbounded.** Let the free segment be
V(9,4) - V(9,5). Row 4 has 9 at position 1 and row 5 has 9 at position 1, so both
rays point away from the triangle lines 4, 5, 9 bound, hence into the same open
half-plane of line 9. The region bounded by the segment and the two rays admits
no crossing line, so it is a single unbounded face with three sides. **Each free
segment contributes one of the nineteen, not two.**

## Referee reference data 9: the two free-segment faces of k=13, both hexagons

    Segment A face:  V(9,4) - V(4,2) - V(2,10) - V(10,7) - V(7,5) - V(5,9)
    Segment B face:  V(6,11) - V(11,13) - V(13,5) - V(5,8) - V(8,10) - V(10,6)

Both hexagons, one sigma-orbit. All twelve edges verified adjacent in their rows.

## Referee reference data 10: the mirror axis and the fixed-face census

**Fixed vertices.** Exactly six: V(2,13), V(3,12), V(4,11), V(5,10), V(6,9),
V(7,8). **Fixed edges.** Exactly one: V(1,7) - V(1,8), row 1 positions 6-7.

The axis meets the arrangement in seven points, eight arcs, two unbounded, so it
passes through six bounded faces, one of which is the triangle `{1,7,8}`. Hence

    exactly 5 of the 19 non-triangular bounded faces are sigma-fixed,
    and the other 14 form exactly 7 sigma-orbits.

**The five fixed faces, all now named and all referee-verified.**

    P  = V(1,7) - V(7,12) - V(12,3) - V(3,8) - V(8,1)                 pentagon
    F2 = V(3,12) - V(3,7) - V(7,11) - V(4,11) - V(4,8) - V(8,12)      hexagon
    F3 = V(4,11) - V(4,7) - V(7,13) - V(2,13) - V(2,8) - V(8,11)      hexagon
    F4 = V(2,13) - V(8,13) - V(5,8) - V(5,10) - V(7,10) - V(2,7)      hexagon
    F5 = V(5,10) - V(8,10) - V(6,8) - V(6,9) - V(7,9) - V(5,7)        hexagon

**Axis order, complete.**

    infinity - V(7,8) - {1,7,8} - mid(V(1,7),V(1,8)) - P - V(3,12) - F2
             - V(4,11) - F3 - V(2,13) - F4 - V(5,10) - F5 - V(6,9) - infinity

Every fixed vertex appears exactly once and in the right place. The census of
sigma-fixed faces is closed.

## Referee reference data 11: the corrected insertion accounting (replaces the owner's diagnosis)

Insert a straight line `l` into a simple 13-line arrangement B, generic: `l`
misses every vertex and is parallel to no line of B. `l` is cut by its 13
crossings into 2 rays and 12 bounded chords, which lie in 14 **distinct** faces
of B (convexity, T159). Write `T(A) = T(B) + Y`.

**(a) Every piece gains at most 1.** A convex n-gon cut by a chord entering
through one edge and leaving through another splits into parts with `a+3` and
`b+3` sides where `a + b = n - 2`. Both parts are triangles only if `a = b = 0`,
i.e. `n = 2`, impossible. So no piece of `l` ever creates two triangles.

**(b) A chord lying in a triangle of B gains exactly 0.** `n = 3` forces
`{a,b} = {0,1}`, parts of 3 and 4 sides: one triangle destroyed, one created.

**(c) The two rays of `l` gain exactly 0.** Let a ray of `l` lie in an unbounded
face U of B. With no parallels, U's recession cone is a wedge spanned by its two
boundary rays' directions, with nonempty interior, and `l`'s direction lies
strictly inside it (equality would mean `l` is parallel to a line of B). The ray
splits U into two parts whose recession cones are the two sub-wedges, both
nonempty, so both parts are unbounded. No triangle is created. **The owner
correction's "corner-clip an unbounded wedge" mechanism is real but it is a
chord phenomenon, not a ray phenomenon.**

**(d) Where the leak actually is.** A **bounded chord** of `l` can lie in an
unbounded face of B. T163's labelling of the twelve chords as T (in a triangle)
or N (in one of the nineteen) is therefore not exhaustive: there is a third
class, U-chords, and a U-chord clipping the corner of an unbounded wedge produces
a bounded triangle worth +1 that the alternation argument never sees. Writing
`n_T + n_N + n_U = 12`, the true statement is

    Y <= n_N + n_U,     with no two consecutive chords both N.

The N-N alternation lemma survives intact. It just does not bound Y.

**(e) The k=4 to k=5 case saturates this exactly, and is the cleanest test.**
A simple 4-line arrangement has 3 bounded faces; `N(4) = 2` so two are triangles
and one is not. Insert the fifth line: 3 bounded chords, 2 rays, `N(5) = 5`, so
`Y = 3`. Rays give 0 by (c) and chords in triangles give 0 by (b), so all three
chords gain, and since only one non-triangular bounded face exists, **at least
two of the three chords sit in unbounded faces.** Every chord gains, and the
alternation cap of `ceil(3/2) = 2` is beaten by the U-chords alone.

## Referee reference data 12: the gain-to-chord ratio, computed from KNOWN.md

Delete one line from an optimal k-line arrangement: what remains has at most
`N(k-1)` triangles, so re-inserting that line gains at least `N(k) - N(k-1)`,
using at most `k-2` bounded chords. No geometry, no order type, three subtractions.

    k    N(k-1) -> N(k)    min gain    chords (k-2)    ratio
    5      2 ->  5            3            3           1.00
    7      7 -> 11            4            5           0.80
    9     15 -> 21            6            7           0.86
    11    25 -> 32            7            9           0.78
    13    38 -> 47            9           11           0.82
    ---
    14    47 -> 54            7           12           0.58   (what 54 needs)

**Consequence.** Any program aiming to prove `Y <= 6` for insertion into a
13-line arrangement is aiming below a ratio that k=9, k=11 and k=13 all exceed on
closed, published values. In particular `Y = 9` is realized at k=12 -> 13 and
`Y >= 11` is forced at k=14 -> 15. The insertion gain is not a quantity that
alternation-style arguments cap near half the chord count; empirically it runs at
four fifths of it. The reduction "k=14 reduces to bounding Y" is sound as a
reduction and useless as a route, because the bound it needs is milder than what
neighbouring cases already achieve, not stronger.

## Referee reference data 13: the mirror-translate family caps at 36

The family (T170, conceded T171): take 7 lines, reflect across an axis, translate
the mirror copy by `D * n_hat` with `D` past the threshold `D0`, so that all 49
cross-family crossings land outside both lines' old spans.

**Step 1. Both halves survive whole.** If a mirror line met the interior of a
bounded face of the original half, it would cross some original line at a point
inside that line's old span, contradiction. So every bounded face of each half is
a face of the union, and same-side triangles number `2 * T(half) <= 22`.

**Step 2. Old crossings are contiguous on every line.** On original line `l_i`
the 6 old crossings occupy a consecutive block of the 13 and the 7 new ones lie
outside it. So `l_i`'s 12 bounded segments split as 5 old-old, at most 2 old-new
(one per end of the old block), and the rest new-new. **At most two old-new
segments per line**, and exactly one when the new crossings all cluster at a
single end.

**Step 3. Every mixed triangle burns two old-new segments.** A triangle on the
14 lines uses either 3 originals, 3 mirrors, or 2 of one and 1 of the other. Take
`{i, i', j}` with `i, i'` original and `j` mirror. Its side on line `i` joins
`V(i,i')` (old) to `V(i,j)` (new), so it is an old-new segment of `l_i`; its side
on `l_i'` is likewise an old-new segment of `l_i'`. By reference data 4 each
segment serves at most one triangle. The 7 original lines carry at most 14
old-new segments in total, so there are **at most 7 triangles of type
{2 original, 1 mirror}**, and by mirror symmetry at most 7 of type
{1 original, 2 mirror}.

**Conclusion.**

    T(mirror-translate family) <= 22 + 7 + 7 = 36

for every choice of the seven directions, every axis, every `D > D0`, split or
clustered. That is 17 below the best known k=14 construction and 18 below the
target. **The family was never a candidate.**

**Cross-check against the agents' own numbers.** In the fully clustered regime
each line has one old-new segment, not two, so the original half carries 7 of
them and the type-{2,1} count drops to `floor(7/2) = 3`, giving `T <= 22+3+3 =
28`. That is exactly T178's mutual-extremality bound of three per side, obtained
here by counting segment types instead of ranking angles. T178's number is
correct; T175's 4 and T177's 4 were reached by a refuted mechanism and are
superseded. T170's demand that 96 of 98 new segments triangulate is refuted
outright: at most 42 of them can be triangle sides in the split case.

## Referee reference data 14: census status, k=13 non-triangular bounded faces

Eleven of nineteen named, all verified by the referee against reference data 6
row by row. Five sigma-fixed (P, F2, F3, F4, F5, reference data 10) and three
sigma-orbits:

    orbit 1   the two free-segment hexagons A and B          (reference data 9)
    orbit 2   G1 = V(2,4)-V(2,9)-V(3,9)-V(3,13)-V(13,10)-V(10,4)
              sigma(G1) on lines {2,5,6,11,12,13}
    orbit 3   H1 = V(2,5)-V(5,12)-V(12,4)-V(4,8)-V(8,11)-V(2,11)
              sigma(H1) on lines {3,4,7,10,11,13}

Ten hexagons and one pentagon so far. **Four orbits, eight faces, remain.**

**The adjacency question the T180 agenda assigned here is now answered, and the
answer needed no census at all.** It asked, for each of the nineteen, how many of
its edges border an unbounded face of B. By reference data 16b the answer is
**zero for seventeen of them, and exactly one each for hexagons A and B**, whose
free segments are the only bounded segments in the arrangement with a
non-triangle on both sides. Agenda item 3 of the T180 agenda is closed. Face size
is likewise irrelevant to the gain (reference data 11a caps every piece at +1).
What the census still owes is the eight unnamed faces themselves, and one of them
in particular: see the agenda.

---

## Referee reference data 15: the T181-T185 candidate, restored and verified

Recovered from turns 181, 183 and 185, which fell out of both agents' context
during the thirty-eight-turn outage. Insert a fourteenth line `l` into
Kabanovitch's B (reference data 6). Row 14, `l`'s own crossing order, is

    14:  1  7  2 13  9  4  6 11  5 10  3 12  8

and the six claimed corner-clips, with both row insertions each:

    clip  face  corner    row/gap                   row/gap
    1     P     V(1,7)    row 1 between 7 and 8     row 7 between 12 and 1
    2     F3    V(2,13)   row 2 between 13 and 8    row 13 between 2 and 7
    3     A     V(9,4)    row 9 between 5 and 4 *   row 4 between 9 and 2
    4     B     V(6,11)   row 6 between 10 and 11 * row 11 between 6 and 13
    5     F5    V(5,10)   row 5 between 7 and 10    row 10 between 8 and 5
    6     F2    V(3,12)   row 3 between 7 and 12    row 12 between 8 and 3

`*` = the free segment itself. Row 8 was never pinned.

**All twelve insertions are correct.** I checked each gap against the printed row
in reference data 6 and against the face's vertex list in reference data 3, 9 and
10: in every case the two named entries are consecutive in the row and the
segment between them is the face's edge on that line. Each clip individually is a
genuine corner clip of a genuine non-triangular face, worth +1 by 11a. What is
wrong with the candidate is the **sequencing**, not the clips. See reference
data 17.

## Referee reference data 16: an inserted line's trajectory is a forced walk

**(a) The segment census.** B has 143 bounded segments and 47 triangles. By
reference data 4 a bounded segment is a side of at most one triangle, so the 141
triangle-sides are 141 distinct segments and exactly 2 carry no triangle at all:
the free segments (`k13-free-segments-forced-by-b-mod-3`, reference data 7).

**(b) The successor lemma.** Let F be one of the nineteen non-triangular bounded
faces of B and `e` an edge of F. Then the face on the far side of `e` is

    a triangle of B                      if e is one of the 141, and
    a 3-sided unbounded wedge            if e is one of the 2 free segments.

It is never another non-triangular bounded face. Proof: `e` is bounded, so it has
two faces; F is not a triangle, so the one triangle `e` may serve is on the far
side; if `e` is free, reference data 8 identifies the far face as the unbounded
wedge spanned by `e` and two rays. Note the corollary the T180 agenda was
reaching for: **exactly two edges in the entire arrangement separate a
non-triangular bounded face from an unbounded one.**

**(c) The walk.** `l`'s fourteen pieces (reference data 11, T159) form a walk

    U_0 , F_1 , F_2 , ... , F_12 , U_13

in the face-adjacency graph of B, where consecutive faces share an edge lying on
the line crossed at that step, the thirteen crossed lines are all distinct, and
`U_0`, `U_13` are unbounded. Then

    Y = # { i : F_i is not a triangle, and F_i's entry and exit edges
                share a vertex }

by 11a (a chord cutting a convex n-gon yields a triangle iff it separates a
single vertex) and 11b (in a triangle the gain is zero). **The successor of a
face is determined by the exit edge. It is not chosen.** This is the fact T181
through T186 did not have.

**(d) The alternation cap, re-proved.** Two consecutive pieces share an edge, so
by (b) no two consecutive pieces are both in non-triangular bounded faces. Hence
`n_N <= 6`, and at `n_N = 6` the six N-chords are a 6-subset of `{1,...,12}` with
no two consecutive: there are `C(7,6) = 7` such subsets.

**(e) Interior spacers are triangles.** If a spacer at position `m` has N-chords
at `m-1` and `m+1`, its face is the far side of both flanking clips' edges, so by
(b) it is a triangle or a free-segment wedge; a wedge has exactly one bounded
edge (reference data 8) so it cannot border two distinct N-faces. Triangle. It
gains 0.

## Referee reference data 17: the T181 chain is impossible

Two lookups in reference data 7.

- P's edge on line 7 is `V(1,7)-V(7,12)` = row 7 positions 10-11 (`12 1`). The
  only triangle that segment can serve is `{1,7,12}`, and `{1,7,12}` **is** in
  reference data 7, with row-1 positions 5-6 (`12 7`) and row-12 positions 8-9
  (`7 1`) confirming all three legs. So the face across P's line-7 edge is the
  triangle `{1,7,12}`.
- F3's edge on line 2 is `V(2,13)-V(2,8)` = row 2 positions 6-7 (`13 8`). The
  only triangle that segment can serve is `{2,8,13}`, which **is** in reference
  data 7, with row-13 positions 5-6 (`8 2`) and row-8 positions 5-6 (`13 2`)
  confirming the other two legs. So the face across F3's line-2 edge is the
  triangle `{2,8,13}`.

Row 14 crosses `1, 7, 2, 13, ...`, so the piece between the line-7 crossing and
the line-2 crossing is simultaneously the face across P's line-7 edge and the
face across F3's line-2 edge. `{1,7,12} != {2,8,13}`. **The chain is dead as
ordered.** The twelve pins survive, the six clips survive individually, the
sequence does not.

## Referee reference data 18: a corner clip does not need a free segment

T229 claimed only a free segment can be corner-clipped, hence a cap of 2. The
failing step is the appeal to 11b. **11b is about a chord lying inside a
triangle.** A clip chord lies inside an *unbounded* face; the triangle sharing
the clipped edge is a different face, entered by a *different* chord of `l`, and
it is that other chord which nets zero.

**Complete worked instance, k=3 to k=4.** B = three lines in general position,
triangle `ABC` with `A = V(1,2)`, `B = V(1,3)`, `C = V(2,3)`, `T(B) = 1`. All
three bounded segments are triangle sides, so B has **no** free segment at all.
Let U be the unbounded face across `AB` from `C`: sides are the segment `AB` on
line 1 and the rays of lines 2 and 3 from `A` and `B`. Insert line 4 crossing
line 2 on its ray at `q`, then line 1 inside `AB` at `p`, then line 3 inside `BC`
at `r`.

    piece            face      result                              gain
    ray                 -      unbounded                            0
    chord q->p          U      clips corner A: triangle {1,2,4}     +1
    chord p->r        ABC      destroys {1,2,3}, creates {1,3,4}     0
    ray                 -      unbounded                            0

`T = 2 = N(4)`, and `N(4) - N(3) = 1 = 1 + 0`. The books close exactly, and the
clipped edge `Ap` is part of `AB`, which already carries triangle `ABC`.
**Freeness is not required and the cap of 2 is false.** What T229 was reaching
for, and what is true, is reference data 19.

## Referee reference data 19: `n_N = 6` forces `Y <= 6` in Kabanovitch's B

Suppose `l` is inserted into B with `n_N = 6` and `Y = 7`. By 16d the six
N-chords are one of seven non-consecutive 6-subsets of `{1,...,12}`; by 16e every
spacer sandwiched between two N-chords is a triangle and gains 0. So the +7 needs
all six N-chords to clip **and** a seventh gain from a spacer that is not
sandwiched. Two shapes of pattern:

**Shape 1, patterns `{1,3,5,7,9,11}` and `{2,4,6,8,10,12}`.** Exactly one spacer
is unsandwiched: position 12 (resp. 1). Reversing `l` if needed, take it to be
12. It must gain, so it is not a triangle, so by 16b the exit edge of the N-clip
at chord 11 is a **free segment**, so chord 11's face is hexagon A or hexagon B
and chord 12's face is wedge A or wedge B. By sigma take A. Then crossing 12 is
line 9 (inside the free segment). Wedge A's edges are the free segment and the
rays of lines 4 and 5, so crossing 13 is line 4 or line 5; hexagon A's line-9
edge is adjacent only to its line-4 edge (at `V(9,4)`) and its line-5 edge (at
`V(5,9)`), so for chord 11 to clip, crossing 11 is line 4 or line 5. Two cases,
and both are the same argument:

    crossing 11 = 4, crossing 13 = 5:
      spacer 10 = far side of A's line-4 edge V(9,4)-V(4,2) = triangle {2,4,9}
        (in reference data 7; row 4 pos 1-2 `9 2`, row 2 pos 2-3 `9 4`,
         row 9 pos 5-6 `4 2`)
      chord 10 exits {2,4,9} on line 4, so it entered on line 2 or 9;
        line 9 is crossing 12, so crossing 10 = line 2
      chord 9 = far side of {2,4,9}'s line-2 edge V(2,9)-V(2,4) = G1
        (reference data 14: G1 = V(2,4)-V(2,9)-V(3,9)-V(3,13)-V(13,10)-V(10,4))
      chord 9 exits G1 on line 2; G1's line-2 edge is adjacent only to its
        line-9 edge and its line-4 edge, so crossing 9 must be line 9 or line 4
      both are already spent, at crossings 12 and 11.        CONTRADICTION

    crossing 11 = 5, crossing 13 = 4:
      spacer 10 = far side of A's line-5 edge V(7,5)-V(5,9) = triangle {5,7,9}
        (row 5 pos 1-2 `9 7`, row 7 pos 2-3 `9 5`, row 9 pos 3-4 `7 5`)
      chord 10 entered on line 7 (line 9 is crossing 12), so crossing 10 = 7
      chord 9 = far side of {5,7,9}'s line-7 edge V(7,9)-V(7,5) = F5
        (reference data 10: F5 = V(5,10)-V(8,10)-V(6,8)-V(6,9)-V(7,9)-V(5,7))
      F5's line-7 edge is adjacent only to its line-9 and line-5 edges, so
        crossing 9 must be line 9 or line 5; both spent.     CONTRADICTION

Wedge B gives the sigma-images of both cases (`sigma: A -> B`,
`{2,4,9} -> {6,11,13}`, `{5,7,9} -> {6,8,10}`, `G1 -> sigma(G1)`, `F5 -> F5`),
which die identically.

**Shape 2, the five middle patterns.** Each has exactly two unsandwiched
spacers and they are **adjacent**, at positions `j, j+1`. Suppose one of them is
unbounded. A wedge's neighbours are its hexagon (across the free segment) and
two unbounded faces (across its rays), so:
 - if spacer `j` is wedge A, spacer `j+1` is unbounded and is reached across a
   ray, so it is not wedge A or B (wedge B shares no line with wedge A's rays);
   but spacer `j+1` must be the far side of the N-clip at `j+2`, hence a triangle
   or a wedge, by 16b. Contradiction.
 - if spacer `j+1` is a wedge, spacer `j` is its neighbour and must be the far
   side of the N-clip at `j-1`, hence a triangle or a wedge; a triangle cannot
   border a wedge (a wedge's only bounded-face neighbour is its hexagon, which is
   not a triangle), and wedges A and B share no edge. Contradiction.

So both spacers are triangles, both gain 0, and `Y <= 6`.

**Conclusion.** `n_N = 6` implies `Y <= 6`. Reaching 54 by inserting a line into
Kabanovitch's optimum therefore requires `n_N <= 5` and **at least two clipping
U-chords**, since `Y <= n_N + n_U` and every clipping U-chord is now known not to
be cheap. Note what this does *not* say: it says nothing about the other k=13
optima, and it is not a proof that `N(14) = 53`. It is one branch, one base.

**Superseded in force by reference data 20**, which reaches "at least four
clipping U-chords" without the pattern enumeration. Kept because its two forced
chains are checked and because agenda item 1 still stands against it.

---

## Referee reference data 20: the five-block theorem, and why clips are four apart

Everything here is about insertion into Kabanovitch's B (reference data 6), which
is simple, so every vertex lies on exactly two lines. Pieces are `F_0 ... F_13`
with `F_0`, `F_13` unbounded (reference data 11, 16c). A piece **clips** if its
entry and exit edges share a vertex; by 11a it then gains exactly 1, and no other
piece gains anything.

**(a) The forward chain.** Let `F_i` clip at `V(a,b)`, entering on line `a` and
leaving through edge `e` on line `b`, and suppose `e` is a bounded segment that
is not free. Its endpoints are `V(b,a)` and `V(b,c)` for some `c`. Then:

1. `F_{i+1}` is the triangle `{a,b,c}`. By 16b the far side of `e` is a triangle,
   and by reference data 4 the only triangle `e` can serve is `{a,b,c}`.
2. `F_{i+1}` leaves on line `c`. Its sides are on `a`, `b`, `c`; it was entered
   on `b`; `l` crosses `a` exactly once and already did so at the clip's entry
   edge. Forced, and it gains 0 by 11b.
3. `F_{i+2}` is the face across the segment `V(c,a)-V(c,b)`. That segment already
   serves `{a,b,c}` on the near side, so by reference data 4 `F_{i+2}` is **not a
   triangle**; and the two edges of `F_{i+2}` meeting its entry edge do so at
   `V(c,a)` and `V(c,b)`, hence lie on lines `a` and `b`, both spent. So
   **`F_{i+2)` cannot clip**, whether it is bounded or unbounded. Gain 0.

**(b) The backward chain** is the same argument through the entry edge. So a clip
whose two edges are both ordinary bounded segments sits at the centre of

    dud , triangle , CLIP , triangle , dud            gains  0 0 1 0 0

**(c) Every instance in the record is this theorem.** Four hand computations,
each presented as a fact about its own face:

    turn   clip                a  b  c   forced triangle   forced dud
    T231   hexagon A @V(9,4)   9  4  2   {2,4,9}           G1        (backward)
    T245   F4 @V(5,8)          8  5 10   {5,8,10}          F5
    T249   P @V(7,12)          7 12  3   {3,7,12}          F2
    T251   U1 @V(1,9)          1  9 11   {1,9,11}          (forward)
           U1 @V(1,9)          9  1 13   {1,9,13}          (backward)

The last row is the correction T251 needs. Its clip is real, and both its edges
are ordinary bounded segments: `V(1,13)-V(1,9)` is row 1 positions 1-2 and
`V(1,9)-V(9,11)` is row 9 positions 9-10, and neither is one of the two free
segments (which are row 9 positions 4-5 and row 6 positions 4-5). Both chains
fire. `{1,9,11}` checks out by the iff test (row 1 pos 2-3 `9 11`, row 9 pos 9-10
`1 11`, row 11 pos 10-11 `1 9`) and is in reference data 7; `{1,9,13}` likewise
(row 1 pos 1-2, row 9 pos 8-9, row 13 pos 11-12). **U1's clip costs five pieces
and four lines, exactly like an N-clip.** "Zero cost" was the wrong unit.

**(d) Two N-clips are at least four apart.** Let `F_i`, `F_j` both clip bounded
non-triangular faces, `i < j`, `g = j - i`.

- `g = 1`: `F_{i+1}` is a triangle (exit non-free) or a wedge (exit free). Either
  way not a bounded non-triangular face.
- `g = 2`: if `i`'s exit is non-free, `F_{i+2}` cannot clip by (a3). If it is
  free, `F_{i+1}` is a wedge, and every face across a wedge's ray is unbounded,
  so `F_{i+2}` is not bounded.
- `g = 3`: with both relevant edges non-free, `F_{i+2}` is a non-triangle by (a3)
  and must be a triangle by (b). If `i`'s exit is free, `F_{i+2}` is unbounded as
  above and cannot be `F_{j-1}`, which must be a triangle or the wedge feeding a
  free entry; and it cannot be the other wedge, since wedges A and B share no
  line (A's edges are on 9, 4, 5; B's on 6, 11, 10) and so are not adjacent. If
  `j`'s entry is free, `F_{j-1}` must be a wedge, but the face across a
  triangle's edge is never a wedge (a wedge's only bounded edge is a free
  segment, whose other side is its hexagon).
- `g = 4` is not excluded: `CLIP, tri, dud, tri, CLIP` is consistent.

**(e) Corollary, and it is the point.** N-clips occupy positions in `{1,...,12}`
pairwise at least 4 apart, so **at most three**. A clip at position 1 or 12
additionally needs a free edge on the outer side, since `F_0` and `F_13` are
unbounded and 16b forbids a non-free edge of an N-face from facing a non-triangle.
Therefore

    Y  =  (N-clips)  +  (clips of unbounded faces)  <=  3  +  n_Uclip

and **`Y = 7` out of Kabanovitch's B requires at least four clipping U-chords.**
Reference data 19 asked for two. The true figure is four, and this derivation
uses neither the seven-pattern enumeration nor `n_N`.

**(f) The only three ways the chain breaks**, which is where any construction has
to live: the edge is **free** (two such segments in the whole arrangement), the
edge is a **ray** (only unbounded faces have those), or the walk **ends**. This
is why reference data 21 matters.

**(g) Scope.** Step (a1) uses 16b, which is a global count specific to B: 143
bounded segments, 141 triangle-sides, two free. The theorem does not transfer to
a base with many free segments. At k=12, 120 bounded segments and 38 triangles
leave six free, the chain breaks six times, and the `Y = 9` realized at
k=12 to 13 is not a counterexample.

## Referee reference data 21: B's unbounded structure, from twenty-six lookups

**(a) Row extremes.** First and last entry of each row of reference data 6:

    line   1  2  3  4  5  6  7  8  9 10 11 12 13
    first 13  3  2  9  9  7  6  9  8  6  6 13 12
    last   2  1  4  3  6  5  8  7 10  9 12 11  1

`l` crossing line `i` beyond `V(i,first)` or `V(i,last)` is crossing it on a ray.

**(b) Ray vertices.** `V(a,b)` carries a ray of line `a` iff `b` is first or last
in row `a`. Eleven vertices carry rays of **both** their lines:

    V(1,2) V(2,3) V(3,4) V(5,6) V(6,7) V(7,8) V(8,9) V(9,10) V(11,12)
    V(12,13) V(13,1)

Four carry exactly one: `V(4,9)`, `V(5,9)`, `V(6,10)`, `V(6,11)`. That is
`11*2 + 4 = 26` ray endpoints for 26 rays, so the census is closed. The four
single-ray vertices are precisely the four endpoints of the two free segments,
which is the consistency check reference data 8 predicts.

**(c) The slope order is `1, 2, 3, ..., 13` cyclically.** Every unbounded face is
bounded by exactly two rays and they are consecutive at infinity, so the two
lines carrying them are adjacent in the cyclic slope order. The eleven double-ray
vertices give eleven slope-adjacent pairs `{i, i+1}`. Wedge A has rays on lines 4
and 5 and wedge B on lines 10 and 11 (reference data 8, 9), giving `{4,5}` and
`{10,11}`. Those thirteen pairs are exactly the edges of the cycle
`1-2-3-...-13-1`, so they are the complete slope order. It is mirror-consistent:
`sigma: i -> 15-i` reverses that cycle and fixes line 1.

**(d) Eleven corner wedges, and they are the only chain-free gains.** For
`i != 4, 10` the face at `V(i,i+1)` between the two rays is an unbounded wedge
with **no bounded edge at all**. A chord entering on one ray and leaving on the
other clips it for `+1`, and reference data 20 does not fire on either side,
because both edges are rays. These eleven corners are the only gains in this
arrangement that are not five pieces deep. The two exceptional pairs `{4,5}` and
`{10,11}` carry wedges A and B instead, whose single bounded edge is the free
segment: the same two exceptions that break reference data 20's chain, arrived at
from the opposite direction.

**(e) At most six corner-wedge clips.** Each uses both its lines' single
crossings, so the clipped pairs are disjoint: a matching in the eleven-edge graph
`4-3-2-1-13-12-11` plus `5-6-7-8-9-10`, two paths on 7 and 6 vertices, maximum
matching `3 + 3 = 6`.

**(f) The far-line family caps at 53, and this is a complete family kill.** Let
`l` lie entirely outside B's bounded region. It crosses the thirteen lines in
slope order, so its fourteen pieces occupy fourteen consecutive gaps at infinity
and its twelve chords occupy the twelve strictly interior ones. A chord gains
iff its gap is a corner wedge. **No two gaps that are consecutive at infinity are
both corner wedges:** they share a ray, and a shared ray has one finite endpoint,
so the two corners would have to be the same vertex. Twelve consecutive gaps with
no two adjacent chosen give at most six. Hence

    T(far line into Kabanovitch's B)  <=  47 + 6  =  53

for every direction and every distance. Note what this explains: 53 is the record
at k=14, and the crudest possible insertion already reaches it or one short of
it. Note also what it forbids: no line outside the bounded region can ever give
54, so any 54 must send `l` through the interior, where reference data 20 fires.

**(g) One bit I could not pin, and it is a good next lookup.** Going around the
26 gaps, consecutive corner wedges automatically alternate between the two
antipodal halves, because a line's two rays are opposite. That fixes the pattern
within each run of consecutive corners and across the wrap at line 1, giving
pairs `{1,2}`, `{3,4}`, `{12,13}` in one half and `{2,3}`, `{11,12}`, `{13,1}` in
the other. The run `{5,6}, {6,7}, {7,8}, {8,9}, {9,10}` is separated from the
rest by the two exceptional pairs, so **its half is not determined by the
extremes alone**. If it lands with the first group, a far line achieves the full
six and reconstructs a 53-triangle 14-line arrangement by hand; if not, five.

---

## Referee reference data 22: the crossing budget, and `Y <= 6` for Kabanovitch's B

This supersedes reference data 19, 20d and 20e as the route to the cap. It uses
reference data 20a-c and nothing else structural.

Setup as in reference data 11 and 16c: `l` is inserted generically into B,
giving thirteen crossings `x_1 ... x_13` and fourteen pieces `F_0 ... F_13` with
`F_0`, `F_13` unbounded. A piece **gains** iff its entry and exit edges share a
vertex; by 11a it then gains exactly 1, by 11b a triangle gains 0, by 11c the
two ray pieces gain 0. Write `g` for the number of gaining pieces, so `Y = g`.

**(a) Every gaining piece uses exactly two crossings.** `F_i` for `1 <= i <= 12`
has entry `x_i` and exit `x_{i+1}`. Trivial, and it is the whole idea.

**(b) Two adjacent gaining pieces must share a free segment.** Let `F_i` and
`F_{i+1}` both gain and share edge `e` on line `b`.

- If `e` is an ordinary bounded segment, then `e` is one of B's 141
  triangle-sides (reference data 16b: 143 bounded segments, 141 triangle-sides,
  two free), so one of the two faces on `e` is a triangle, and a triangle gains 0
  by 11b. Contradiction.
- If `e` is a ray, both faces are unbounded. `e` has one finite endpoint `V`, so
  a piece whose entry and exit edges share a vertex and one of whose edges is `e`
  must clip **at `V`**. B is simple, so `V = V(b,x)` for exactly one other line
  `x`, and the only edges at `V` other than the two on line `b` lie on line `x`.
  So `F_i`'s other edge and `F_{i+1}`'s other edge both lie on line `x`, meaning
  `x_i` and `x_{i+2}` are both crossings of line `x`. `l` crosses `x` once.
  Contradiction.

So `e` is free. B has two free segments, on lines 9 and 6; the bounded side of
each is hexagon A resp. hexagon B (reference data 9), the unbounded side is
wedge A resp. wedge B (reference data 8). No face carries both. Hence **at most
two adjacencies, and they use distinct free segments.**

**(c) Every adjacency pays for itself with a wasted crossing.** Take the
adjacency at free segment A, so `{F_i, F_{i+1}} = {`wedge A, hexagon A`}` in
some order. Hexagon A gains, and one of its two clip edges is the free segment,
so the other is an ordinary bounded segment (hexagon A's other five edges are
all bounded, and B's only free segments are A and B, of which A is already the
entry). Reference data 20a fires **away from the wedge**: the next piece is a
forced triangle, it is forced to leave on the third line, and the piece beyond
it cannot clip. Concretely, clipping at `V(9,4)` gives `{2,4,9}` then G1, and
clipping at `V(5,9)` gives `{5,7,9}` then F5. The crossing between the forced
triangle and the forced dud borders two non-gaining pieces, so no gaining piece
counts it. It cannot be dodged by running off the end of the walk: the forced
triangle is bounded and `F_13` is not.

The two adjacencies lie on disjoint line sets (`{5,9,4,2}` or `{4,9,5,7}` for A;
their sigma-images `{10,6,11,13}` or `{11,6,10,8}` for B), so the two wasted
crossings are distinct.

**(d) The count.** Let `A` be the number of adjacencies, `A <= 2`. Distinct
crossings touched by gaining pieces is `2g - A`. Wasted crossings number at least
`A`. So `13 >= (2g - A) + A = 2g`, giving

    Y = g <= 6,      T(B + l) <= 47 + 6 = 53

for every straight line `l` and every direction. **Insertion into Kabanovitch's
B cannot reach 54.** This subsumes reference data 21f (the far-line family) and
makes the weaving question moot for this base.

**(e) What transfers, and the one thing that does not.** Steps (a), (b) and (d)
use only: `l` crosses each line once; reference data 4; the count `B = k(k-2) =
143` and `F = 143 - 3*47 = 2`, both pure arithmetic for any `p=0`, `c=0`, T=47,
13-line table; and 11a-c. Step (c) needs one structural fact: **the two free
segments lie on distinct bounded faces.** In B they do. In an unnamed alternate
optimum they might not: if one bounded face carried both free segments as edges
meeting at a vertex, with unbounded faces beyond each, then clipping that face
gives three adjacent gaining pieces on four crossings with no chain firing, and
the arithmetic permits `g = 7`. Ruling that out, or exhibiting it, is the live
question. **Note also that (b) uses `c = 0` twice** — "B is simple, so `V` lies
on exactly two lines", and reference data 16b's segment count. At a concurrence
both fail; see reference data 23.

## Referee reference data 23: `3T <= B` is false at a concurrence

**(a) The corpus census.** `grep "     \["` on `corpus/arrangements.json` finds
nested table entries — two lines crossing a third at one point — in exactly six
tables, at these line numbers:

    kobon_4_2      63, 70, 77                                   3 entries, c=1
    kobon_6_1      137, 145, 168                                3 entries, c=1
    kobon_6_2      184,188,197,205,209,216,224,228,237          9 entries, c=3
    kobon_8        326, 347, 358, 377, 388, 392                 6 entries, c=2
    kobon_10       517, 523, 535, 545, 602, 618                 6 entries, c=2
    kobon_12_38tri 776, 782, 825, 852, 893, 922                 6 entries, c=2

Each triple point contributes exactly three nested entries, one per participating
row. **No table from `kobon_11_32tri` upward contains any**, so Kabanovitch's B,
Bader's k=14 and k=18, and Wood's k=20 are all concurrence-free, and every
reference data block 1-22 keeps its footing.

**(b) Four of the six violate reference data 4.** With
`B = k(k-2) - 2p - 3c` (reference data 25):

    table            k   T    c    B     3T     verdict
    kobon_4_2        4   2    1    5      6     3T > B
    kobon_6_1        6   7    1   21     21     equality
    kobon_6_2        6   7    3   15     21     3T > B by six
    kobon_8          8  15    2   42     45     3T > B
    kobon_10        10  25    2   74     75     3T > B
    kobon_12_38tri  12  38    2  114    114     equality

`kobon_6_2` is the decisive one and its `B` is confirmed by direct row count:
rows have 3, 4, 3, 4, 3, 4 distinct crossing points, so `2+3+2+3+2+3 = 15`
bounded segments carry `21` triangle-sides. At least six segments bound a
triangle on **both** sides.

**(c) The mechanism, which is T276's.** Let `P` be a triple point on lines
`a, b, c` and let `e` be the bounded segment of line `a` from `P` to `V(a,d)`.
Its far endpoint has two identities, `V(a,b)` and `V(a,c)`, so it has two live
candidate triangles, `{a,b,d}` on one side and `{a,c,d}` on the other, and both
can be faces. Reference data 4's uniqueness proof breaks precisely here: it
argues that the third vertex `V(b,c)` lies on one determined side, which needs
the far endpoint to name one pair of lines. `kobon_4_2` realises it minimally —
three concurrent lines and a transversal, `T = 2`, and line 3's single bounded
segment `P-V(1,3)` is a side of both triangles.

**(d) Consequences, in order of damage.**

1. T269's `k=14` enumeration `2p + 3c <= 6` is void. Counting side-incidences,
   the correct crude statement is `3T <= B + D` where `D` is the number of
   segments serving two triangles. **Superseded by reference data 27a, which
   computes `D` instead of bounding it crudely: `D <= 2c` for isolated triple
   points, so `3T <= k(k-2) - c` and concurrences *tighten* the budget. The
   `6c` guess below was mine and it was three times too generous.** Only chained
   triple points (27c) can push `D` above `2c`.
2. Reference data 4's corollary "any 14-line arrangement with 54 triangles has
   `p <= 3`" holds only for `c = 0`. It is now a statement about a sub-family.
3. T271/T273/T275's zero-slack claims about `kobon_12_38tri` are void.
4. The published upper bounds (Tamura, Clement-Bader, the improved even bound)
   are **not** touched by this. They stand on their own sources. What is touched
   is this project's habit of re-deriving them from `floor(B/3)` and then
   reasoning about slack.

**(e) The constructive reading, which I got wrong and reference data 27a
corrects.** I wrote that concurrences buy segment efficiency, on the evidence
that `kobon_4_2` gets 2 triangles from 5 bounded segments where the simple
`kobon_4` needs 8. That is efficiency per segment, not extra capacity: a triple
point destroys three segments and an isolated one buys back at most two, so the
ceiling `B + d` goes *down*. Five of the six corpus witnesses at even `k <= 12`
do use concurrences to hit the bound, and all three open cases are simple, which
is still the interesting empirical fact — but the mechanism that makes it work
is chaining (27c), not concurrence as such.

## Referee reference data 24: the union of bounded faces is neither the hull nor convex

T279 asserts "the union of B's bounded faces is exactly the convex hull of B's
78 vertices". Four lines refute both halves.

    AB: y = x + 3        AC: y = -x + 3       BC: y = 0
    L4: y = 1 + 0.1x

Vertices: `A(0,3)`, `B(-3,0)`, `C(3,0)`, `P(-2.222, 0.778)` on `AB`,
`Q(1.818, 1.182)` on `AC`, `R(-10, 0)` on `BC`. Three bounded faces: triangle
`APQ`, quadrilateral `PBCQ`, triangle `RBP`. Their union is triangle `ABC`
together with `RBP`.

**Not the hull.** The hull of the six vertices is the triangle `R(-10,0)`,
`C(3,0)`, `A(0,3)`. The point `(-5, 1)` lies inside it — the edge `RA` has
`y = 1.5` at `x = -5` — and lies in an unbounded face, since it is above `AB`
and above `L4`. T279's step "escaping to infinity must cross the hull boundary,
which is itself made of arrangement edges" is the error: `RA` is not an
arrangement edge.

**Not convex.** Near `P` the union's upper boundary is `y = 1 + 0.1x` for
`x < -2.222` and `y = x + 3` for `x > -2.222`, a boundary of increasing slope,
so `P` is a reflex vertex. Explicitly, `(-5, 0.49)` and `(0, 2.99)` are both in
the union and their midpoint `(-2.5, 1.74)` is not, the union's ceiling there
being `0.75`.

So a straight line may leave and re-enter the union of bounded faces more than
once, and T279's "at most three contiguous runs" does not follow. The weaving
question of T275 is open. For Kabanovitch's B it is also moot: reference data 22
caps `Y` at 6 whatever the run structure.

## Referee reference data 25: the segment formula with concurrences

T269's, verified and extended. Line `i` has `k-1` partners; it loses one crossing
point if it is in a parallel pair, and at a vertex of multiplicity `m` its `m-1`
crossings there collapse to one, losing `m-2` points. Bounded segments on line
`i` = (distinct crossing points) `- 1`. Summing:

    B = k(k-2) - 2p - sum over concurrent vertices v of m_v (m_v - 2)

For triple points (`m = 3`) that is `-3` each, which is T269's
`B(k,p,c) = k(k-2) - 2p - 3c`. Checks: `kobon_12_38tri`, `120 - 6 = 114`, and a
direct row count gives 114. `kobon_6_2`, `24 - 9 = 15`, direct row count 15.
`kobon_4_2`, `8 - 3 = 5`, direct row count 5.

Note the degree-sum cross-check T269 gave is also right: three ordinary crossings
have total degree 12, one triple point has degree 6, a loss of six edge-ends and
therefore three edges.

## Referee reference data 26: two isolated triple points sharing both helpers, in coordinates

T300 claimed the isolated `d=2` gadget needs two dedicated helper lines per
triple point with none shared, hence `9 + 6 = 15` lines for `c=3`. T301 conceded
it. Here are eight lines with two line-disjoint triple points, each doubling two
segments, sharing **both** helpers.

    P1 = (0,0)      a1: y = x        b1: y = -x        c1: y = 3x
    P2 = (10,0)     a2: y = 2(x-10)  b2: y = -2(x-10)  c2: y = 0.5(x-10)
    helpers         L:  y = -0.1     L': y = 0.1 + 0.01x

Eight distinct slopes (`1, -1, 3, 2, -2, 0.5, 0, 0.01`), so `p = 0`, and the only
concurrences are `P1` and `P2`, which share no line: `c = 2`, isolated.

**(a) L's crossings, all six computed.** With `a1`: `(-0.1,-0.1)`, `|t| = 0.141`.
With `b1`: `(0.1,-0.1)`, `0.141`. With `c1`: `(-1/30, -0.1)`, `0.105`. With `a2`:
`(9.95,-0.1)`, `0.112`. With `b2`: `(10.05,-0.1)`, `0.112`. With `c2`:
`(9.8,-0.1)`, `0.224`.

**(b) The six rays at `P1`, by angle.** `a1+` 45, `c1+` 71.6, `b1-` 135, `a1-`
225, `c1-` 251.6, `b1+` 315. `L` lies in `y < 0`, so it meets exactly the three
consecutive rays `a1-`, `c1-`, `b1+`, with `c1-` in the middle — the arc fact
T296 proved in general.

**(c) Nearest, not merely met.** On `a1-` the competitors are `c2` at `x=-10`
(`|t| = 14.1`), `a2` at `x=20` and `b2` at `x=6.67` (both on `a1+`), and `L'` at
`x=+0.101` (on `a1+`). `L` at `0.141` wins by a factor of a hundred. On `b1+`:
`c2` at `x=10/3` (`4.7`), `a2` at `x=6.67` (`9.4`), `L'` at `x=-0.099` (wrong
ray). On `c1-`: `c2` at `x=-2` (`6.3`), `a2` at `x=-20`, `b2` at `x=4` (wrong
ray). `L` is nearest on all three.

**(d) The two triangles and the doubled segment.** Sector `(a1-, c1-)` closes as
`{a1, c1, L}` with vertices `(0,0)`, `(-0.1,-0.1)`, `(-1/30,-0.1)`; sector
`(c1-, b1+)` closes as `{c1, b1, L}` with vertices `(0,0)`, `(-1/30,-0.1)`,
`(0.1,-0.1)`. Both lie in `-0.1 <= y <= 0`; the only lines within `0.15` of `P1`
are `a1, b1, c1, L` and `L'`, and `L'` has `y >= 0.09` throughout that
neighbourhood, so neither triangle is cut. **The segment of `c1` from `P1` to
`(-1/30,-0.1)` is a side of both.** By the same computation with `L'` in the
upper half plane (nearest on `b1-` at `0.140`, `c1+` at `0.106`, `a1+` at
`0.143`, against competitors at `3.3` and worse), the segment of `c1` from `P1`
to `(0.0334, 0.1003)` doubles as well. `d = 2` at `P1`.

**(e) The same two lines do it again at `P2`.** Rays at `P2`: `c2+` 26.6, `a2+`
63.4, `b2-` 116.6, `c2-` 206.6, `a2-` 243.4, `b2+` 296.6. `L` meets the lower
triple `c2-, a2-, b2+`, middle `a2-`. Nearest on `a2-`: `L` at `0.112` against
`b1` at `x=6.67` (`7.45`) and `c1` at `x=-20`. On `c2-`: `L` at `0.224` against
`b1` at `x=10/3` (`7.45`), `a1` at `x=-10` (`22`), `c1` at `x=-2`. On `b2+`: `L`
at `0.112` against `b1` at `x=20` (`22.4`); `a1` at `x=6.67` and `c1` at `x=4`
are on the far ray. So `L` doubles the segment of `a2` from `P2` to
`(9.95,-0.1)`, and `L'` doubles the opposite one (nearest on `c2+` at `0.456`,
`a2+` at `0.226`, `b2-` at `0.224`; nothing else comes within `7`). `d = 2` at
`P2`, with the same two helper lines.

**(f) Three points on eleven lines.** Add `P3 = (20,0)` on `a3: y = 4(x-20)`,
`b3: y = -4(x-20)`, `c3: y = 0.25(x-20)`. `L` and `L'` pass within `0.11` of
`P3`; the nearest competitor on any of `P3`'s six rays is `b2` at `x = 16.67`
(distance `13.7`) or `b1` at `x = 16` (`16.5`). Eleven lines, `c = 3`, `d = 6`,
three lines spare at `k = 14`.

**(g) What this does and does not settle.** It refutes T300's line count and
reverses T301's concession. It says nothing whatever about `T = 54`: these
arrangements have a handful of triangles, and the saturation question T288,
T292, T294 and T296 all pressed on is untouched. Note also 27a — the program
this rescues is arithmetically dominated by `c = 0` anyway, so the honest
summary is that both the obstruction and the thing it obstructed are dead.

## Referee reference data 27: the concurrence budget, and `kobon_6_2` completely solved

**(a) Isolated concurrence strictly costs slack.** Let `P` be a triple point on
`a, b, c`, with all six of its neighbouring crossings ordinary. A segment of a
ray `r` at `P` is doubled iff both sectors flanking `r` are triangles. A sector
`(r, r')` that is a triangle closes on a single line `L` crossing both `r` and
`r'` at the nearest crossing on each. If `r`'s far endpoint is an ordinary
crossing, "nearest on `r`" names one line, so the two sectors flanking `r` close
on the *same* `L`.

Now suppose rays `r_i` and `r_j` are both doubled, indices in the cyclic order of
the six rays. If `j = i+1`, then `L` is nearest on `r_{i-1}, r_i, r_{i+1},
r_{i+2}`, and `r_{i-1}` and `r_{i+2}` are antipodal; a straight line not through
`P` meets only one of two opposite rays. Contradiction. If `j = i+2`, the same
chaining through `r_{i+1}` (ordinary, so uniqueness holds) gives `L` nearest on
five consecutive rays, again containing an antipodal pair. Contradiction. Only
`j = i+3` survives, so **the doubled rays at an isolated triple point are a
single antipodal pair, both on the same line, and `d <= 2`.** This is T293's
cap, re-proved; T294's concession of it was earned and is silver.

Combine with T288's identity. Counting segment-to-triangle incidences two ways
with `f + s + d = B` and `s + 2d = 3T` gives `d - f = 3T - B`, hence for `p = 0`
and `c` isolated triple points

    3T <= B + d <= (k(k-2) - 3c) + 2c = k(k-2) - c

    at k = 14, T = 54:   f = d - 3c + 6 <= 6 - c

`c = 0` is the loosest regime, `c = 6` is the tightest that is arithmetically
live, `c >= 7` is dead. Each triple point destroys three bounded segments and
buys back at most two. Cross-check against T292/T293's per-line budget:
`6*11 + 3*13 + 5*12 = 165 = 168 - 3`. They agree exactly.

**(b) `kobon_6_2`, all seven triangles and all fifteen segments.** Rows, from
`corpus/arrangements.json` lines 178-243, brackets marking the three triple
points `A = {1,3,4}`, `B = {1,2,5}`, `C = {3,5,6}`:

    1: [3,4] [2,5]  6            2: 3  4  [5,1]  6
    3: 2  [4,1] [5,6]            4: 2  [1,3]  6  5
    5: [1,2] [6,3]  4            6: 1  2  [3,5]  4

All twenty triples tested by the three-leg adjacency rule (two labels in the same
bracket are concurrent, hence never adjacent). Seven pass:

    {1,2,4}  {1,2,6}  {1,3,5}  {2,3,4}  {2,5,6}  {3,4,6}  {4,5,6}

which is the corpus's own `"count": 7`. Segment assignment, all fifteen:

    line 1  A-B          {1,2,4} {1,3,5}      doubled
            B-V(1,6)     {1,2,6}
    line 2  V(2,3)-V(2,4){2,3,4}
            V(2,4)-B     {1,2,4}
            B-V(2,6)     {1,2,6} {2,5,6}      doubled
    line 3  V(3,2)-A     {2,3,4}
            A-C          {1,3,5} {3,4,6}      doubled
    line 4  V(4,2)-A     {1,2,4} {2,3,4}      doubled
            A-V(4,6)     {3,4,6}
            V(4,6)-V(4,5){4,5,6}
    line 5  B-C          {1,3,5} {2,5,6}      doubled
            C-V(5,4)     {4,5,6}
    line 6  V(6,1)-V(6,2){1,2,6}
            V(6,2)-C     {2,5,6}
            C-V(6,4)     {3,4,6} {4,5,6}      doubled

`B = 15`, `d = 6`, `f = 0`, incidences `3+4+3+4+3+4 = 21 = 3T`, and
`d - f = 6 = 3T - B`. Everything closes. T302's five are among these; `{2,3,4}`
and `{4,5,6}` are the two it and T303 argued around.

**(c) A chained triple point carries three doubled segments.** At `A = {1,3,4}`
the doubled segments are `A-B` (line 1), `A-C` (line 3) and `V(4,2)-A` (line 4):
**three**, above the isolated cap of two. The cap's proof fails exactly as
advertised — two of `A`'s rays end at `B` and `C`, which are themselves triple
points, so "nearest on that ray" names two lines and the flanking sectors are no
longer forced to close on the same one. `B` and `C` likewise carry three each;
the three bridge segments are shared, so `3*3 - 3 = 6 = d`. **This is why every
corpus arrangement with `c >= 2` chains.** It also means 27a's `d <= 2c` and
therefore `3T <= k(k-2) - c` are statements about the isolated case only. For
chained points the per-point bound is `u + b/2` with `u <= 3` unshared and
`u + b <= 6`, giving `d <= 4.5c` and the much weaker `3T <= k(k-2) + 1.5c`. The
useful residue: **a concurrence pays for itself only if it is chained**, and how
much it can pay at `k=14` is unknown.

**(d) T304's bracket-neighbour observation, priced.** The row-neighbours of a
concurrence bracket in row `x` are the lines completing the triangles that use
the two segments of `x` at that point. True, verified on rows 2 and 4 of
`kobon_6_2`, and it is reference data 4's first line: a bounded segment's two
endpoints determine which triples it can serve, so the neighbour *is* the third
line by definition. It pins nothing, because which line sits there is free, and
the genuine condition it gestures at — the neighbour must close in its own rows
too — is what makes the segment doubled and is already counted by `d`. It is not
a parallel-pair-style tax; a parallel pair deletes a crossing point, and hence a
segment, from the budget.

---

## Referee reference data 28: the full wrap `d_P = 6`, realized in six lines

T327 claimed the minimal three-break gadget gives `d_P = 0`; T328 conceded it.
Here is the gadget with coordinates and every face checked.

    P   = (1,1)          inside the triangle Q_0 Q_2 Q_4
    Q_0 = (0,0)   Q_2 = (4,0)   Q_4 = (0,4)

    hubs   a = P Q_0 : y = x          b = P Q_2 : y = (4-x)/3
           c = P Q_4 : y = 4 - 3x
    sides  M_1 = Q_0 Q_2 : y = 0      M_3 = Q_2 Q_4 : x + y = 4
           M_5 = Q_4 Q_0 : x = 0

**(a) The arrangement.** Slopes `1, -1/3, -3, 0, -1, infinity` — six distinct, so
`p = 0`. Of the 15 line pairs, 12 collapse into four triple points
`P = {a,b,c}`, `Q_0 = {a,M_1,M_5}`, `Q_2 = {b,M_1,M_3}`, `Q_4 = {c,M_3,M_5}`; the
remaining three are ordinary: `a∩M_3 = (2,2)`, `b∩M_5 = (0,4/3)`,
`c∩M_1 = (4/3,0)`. So `c = 4`, `V = 7`. Every line has exactly 3 distinct
crossing points and hence 2 bounded segments, giving `B = 12`, which is
`k(k-2) - 3c = 24 - 12` by reference data 25. Zaslavsky's count
`1 + k + sum (m_v - 1) = 1 + 6 + (2+2+2+2+1+1+1) = 18` regions, `2k = 12`
unbounded, **6 bounded.**

**(b) All six bounded faces are triangles, and all six are the sectors at `P`.**

    1  P, (2,2),   Q_4        on a, M_3, c
    2  P, Q_4,     (0,4/3)    on c, M_5, b
    3  P, (0,4/3), Q_0        on b, M_5, a
    4  P, Q_0,     (4/3,0)    on a, M_1, c
    5  P, (4/3,0), Q_2        on c, M_1, b
    6  P, Q_2,     (2,2)      on b, M_3, a

Emptiness, checked one at a time: within each triangle the only candidate
intruders are the three lines not carrying a side; two of them meet the triangle
only at a vertex and the third misses its coordinate range. Worked instance for
face 1: `b` passes through the vertex `P` with rays at `341.6` and `161.6`
degrees, outside the sector `(45, 108.4)`; `M_1` needs `y = 0` and the face has
`y >= 1`; `M_5` meets the face only at the vertex `(0,4)`. The other five go the
same way.

**(c) `d_P = 6`, the full wrap.** The six rays at `P` are, by angle,
`a-` 45, `c→Q_4` 108.4, `b-` 161.6, `a→Q_0` 225, `c-` 288.4, `b→Q_2` 341.6. Each
of the six segments at `P` is a side of the two faces flanking its ray:

    P-Q_0      (on a)  faces 3, 4        P-(2,2)    (on a)  faces 1, 6
    P-Q_2      (on b)  faces 5, 6        P-(0,4/3)  (on b)  faces 2, 3
    P-Q_4      (on c)  faces 1, 2        P-(4/3,0)  (on c)  faces 4, 5

**Six doubled segments at one point.** The other six bounded segments (two on
each of `M_1`, `M_3`, `M_5`) each serve exactly one face, so `d = 6`, `f = 0`,
incidences `6*2 + 6*1 = 18 = 3T` with `T = 6`, and `d - f = 6 = 3T - B` closes
T288's identity exactly.

**(d) Three breaks, alternating, as T327's own floor requires.** The rays
`a→Q_0`, `b→Q_2`, `c→Q_4` each terminate at a triple point; the rays `a-`, `b-`,
`c-` each terminate at an ordinary crossing. Breaks and ordinary rays alternate,
which is the tightest possible arrangement under reference data 29's
non-adjacency lemma, and it is why the full wrap needs exactly three neighbouring
triple points, not six.

**(e) And it loses.** `3T <= k(k-2) - 3c + d = 24 - 12 + 6 = 18`, against `24` at
`c = 0`. Ratio `d/c = 6/4 = 1.5`, below `kobon_6_2`'s `2` and below the isolated
`2`. `T = 6` where `N(6) = 7`. This is the *other* order type of the four-point
configuration T308 opened; the convex one (T310, T311) has `d_{P_i} = 2` at each
of its four vertices and reaches the same totals `T = 6, d = 6, f = 0, B = 12`.
Both halves of the `K4` family are now computed and both are dominated.

## Referee reference data 29: the non-adjacency lemma, and `d <= 4.5c`

Notation for `p = 0`: `c` triple points, `d` doubled segments (serving a triangle
on each side), `f` free segments, `B = k(k-2) - 3c`, and `d - f = 3T - B` (T288).
Write `S_1` for the doubled segments whose far endpoint is an ordinary crossing
and `S_2` for those joining two triple points, so `d = |S_1| + |S_2|`.

**(a) Every doubled segment has at least one triple-point endpoint.** If a
segment on line `a` has both endpoints ordinary, they are `V(a,b)` and `V(a,c)`
for unique `b, c`, its only candidate triangle is `{a,b,c}`, and `V(b,c)` lies on
one determined side. Reference data 4.

**(b) A triangle sector closes on one line, met at the nearest crossing of each
bounding ray.** If sector `(r, r')` at `P` is a triangle `P, X, Y`, then any line
crossing `r` strictly between `P` and `X` enters the interior, so `X` is the
nearest crossing on `r`; same for `Y`. The third side lies on one line.

**(c) The non-adjacency lemma.** *Two doubled rays at a triple point cannot be
adjacent in the cyclic order of six if both terminate at ordinary crossings.*
Let rays `r` and `r+1` both be doubled and ordinary. Ray `r` doubled makes
sectors `s_{r-1}` and `s_r` triangles; `r` ordinary means the nearest crossing on
`r` lies on a single other line, so by (b) both close on the same line `M`.
Ray `r+1` doubled and ordinary makes `s_r` and `s_{r+1}` close on one line, which
is `M` since `s_r`'s third side is unique. Then `M` meets rays `r-1, r, r+1, r+2`
— four consecutive rays of six, containing the antipodal pair `r-1, r+2`. A
straight line not through `P` meets at most one ray of an antipodal pair.
Contradiction.

Hence at most three ordinary doubled rays per triple point, and

    |S_1| <= 3c        d_P <= 6        sum_P d_P = |S_1| + 2|S_2| <= 6c

**(d) The bound.** `d = sum_P d_P - |S_2| <= 6c - |S_2|` and
`d = |S_1| + |S_2| <= 3c + |S_2|`. Adding, `2d <= 9c`:

    d <= 4.5c        and        3T <= k(k-2) - 3c + d <= k(k-2) + |S_1|/2

**(e) The decision rule.** Concurrence beats `c = 0` **iff `d > 3c`**. Equality
in (d) needs every triple point to be a full wrap *and* `|S_2| = 1.5c`, i.e. the
doubled break segments forming a 3-regular graph on the triple points. Nothing on
record is close: T319's six-table corpus census maxes at `d = 2c` (`kobon_6_2`),
both `K4` order types give `1.5c` (reference data 28, T311), isolated points give
`2c` (reference data 27a), and reference data 28 is the only realization of even
one full-wrap point — with three `d_Q = 1` neighbours attached.

**(f) The `k = 14` consequence, which corrects T315.** `f = d - 3c + 6`, so
`T = 54` needs `d >= 3c - 6`, and `4.5c >= 3c - 6` for every `c >= 0`. **No
concurrence count is excluded at `k = 14` by the segment budget.** T315's
"`c=7` drops to `T <= 53`", repeated at T319 and used at T320, is a consequence of
`d <= 2c`, which is an unbroken empirical ceiling and not a theorem — as T318
said and T319 conceded. State the scope when citing it.

**(g) Scope.** All of this assumes `p = 0` and multiplicity exactly 3. T318's
`d(m) <= 2m - 4` covers isolated points of higher multiplicity, with net budget
effect `-(m-2)^2`; the chained analogue at `m >= 4` is unexamined and, given (e),
uninteresting unless someone first exhibits `d > 2c` at `m = 3`.

## Referee reference data 30: B's eleven double-ray vertices all close as triangles

Reference data 21b lists eleven vertices of Kabanovitch's B carrying rays of both
their lines. T324 showed that a shared free-segment vertex with three-sided
wedges beyond both edges must be one of them, and checked `V(1,2)` and `V(11,12)`;
T325 checked `V(2,3)`, `V(3,4)`, `V(5,6)`. The remaining six, checked here
against reference data 6's printed rows by the iff test of reference data 2 and
cross-confirmed in reference data 7:

    vertex     row-p pos 1/last   row-q pos 1/last   inward pair   triangle
    V(6,7)     row6[1]=7          row7[1]=6          9, 9          {6,7,9}
    V(7,8)     row7[12]=8         row8[12]=7         1, 1          {1,7,8}
    V(8,9)     row8[1]=9          row9[1]=8          6, 6          {6,8,9}
    V(9,10)    row9[12]=10        row10[12]=9        12, 12        {9,10,12}
    V(12,13)   row12[1]=13        row13[1]=12        6, 6          {6,12,13}
    V(13,1)    row13[12]=1        row1[1]=13         9, 9          {1,9,13}

Third legs: row 9 has `6 7` at positions 2-3; row 1 has `7 8` at 6-7; row 6 has
`9 8` at 2-3; row 12 has `10 9` at 10-11; row 6 has `13 12` at 6-7; row 9 has
`13 1` at 8-9. All six are in reference data 7's list of 47.

**Eleven of eleven, zero exceptions.** By T325's sharpening, a closing interior
sector proves both incident segments already serve a triangle, so neither is
free, so **no two free segments of B meet at a double-ray vertex** and the
three-sided-wedge branch of reference data 22e is closed for B. It was already
closed for B by reference data 22 through a different route. What is *not*
settled, and what T326 correctly flagged: whether inward-neighbour matching at a
double-ray vertex is forced by extremality in general, or is an artifact of B's
141/143 saturation. Eleven instances in one table is one table.

---

## Referee reference data 31: a free segment with bounded faces on both sides

Agenda item 3.2 asked whether the **unbounded** face beyond a free segment must
be a three-sided wedge, as reference data 8 found for B. It need not be
unbounded at all. Five lines, exact:

    a: y = 0        b: y = 5x        c: y = -5x + 5
    e: y = 1 + x/100                 d: y = -1 + x/50

**(a) The arrangement.** Slopes `0, 5, -5, 1/100, 1/50`, all distinct, so
`p = 0`. Ten crossings, all distinct, no three concurrent, so `c = 0`:
`a∩b = (0,0)`, `a∩c = (1,0)`, `a∩e = (-100,0)`, `a∩d = (50,0)`,
`b∩c = (1/2, 5/2)`, `b∩e = (100/499, 500/499)`, `b∩d = (-50/249, -250/249)`,
`c∩e = (400/501, 505/501)`, `c∩d = (300/251, -245/251)`, `e∩d = (200, 3)`.
`V = 10`, `B = k(k-2) = 15`, bounded faces `(k-1)(k-2)/2 = 6`.

**(b) The segment of `a` from `(0,0)` to `(1,0)` is free.** Its endpoints are
`V(a,b)` and `V(a,c)`, so by reference data 4 its only candidate triangle is
`{a,b,c}` = `(0,0), (1,0), (1/2, 5/2)`. Line `e` crosses `b` at
`x = 100/499 ≈ 0.2004` and `c` at `x = 400/501 ≈ 0.7984`, both strictly between
`0` and `1`, and at `x = 1/2` sits at `y = 1.005 < 5/2`. So `e` passes through
that triangle's interior, `{a,b,c}` is not a face, and the segment serves no
triangle on either side.

**(c) Both its faces are bounded quadrilaterals.**

    above:  (0,0) --b-- (100/499, 500/499) --e-- (400/501, 505/501) --c-- (1,0)
    below:  (0,0) --b-- (-50/249, -250/249) --d-- (300/251, -245/251) --c-- (1,0)

The only line that could cut the upper face is `d`, which over `x ∈ [0,1]` has
`y ∈ [-1, -0.98]`; the only line that could cut the lower face is `e`, which over
`x ∈ [-0.21, 1.20]` has `y ≈ 1`. Neither does. **Neither side of this free
segment is unbounded.**

**(d) What this kills.** Reference data 8's "one face on a free segment is
unbounded" is proved by two row lookups in Kabanovitch's B (line 9 at position 1
in rows 4 and 5) and is a fact about B, not a theorem. T353's "free segments,
whose far side is unbounded" is refuted. T324's necessity condition and reference
data 30's eleven-of-eleven sweep both presuppose three-sided wedges beyond both
edges and therefore say nothing about a base where this configuration occurs.
Together with T340, `insertion-cap-53-generalizes-beyond-b` now has two
independent B-specific joints, not one.

**(e) What it does not kill.** Reference data 22 (`Y <= 6` for B) is untouched:
B's own free segments do have unbounded wedges beyond them, verified by lookup.
This widens the space of *other* 13-line optima, which is exactly reference data
22e's live question.

## Referee reference data 32: the rotational census above order 2, complete

Let a `k`-line arrangement be invariant under rotation `ρ` by `2π/n` about a
point `O`, `n > 2`. T345 did `n = 7` at `k = 14`; T346 generalized the stabilizer
argument and did the divisors of 18 and 20. This completes it and drops T346's
non-vertex-center hypothesis by splitting on the parity of `n`.

**(a) Even `n` is central symmetry.** `⟨ρ⟩` contains `ρ^{n/2}`, the 180-degree
rotation about `O`. So the arrangement is centrally symmetric and reference data
33 applies verbatim, whatever else `ρ` does. No residue argument is needed and
none is available in general, because the order-2 element supplies triangle
stabilizers of order 2 whenever a triangle has a vertex at `O`.

**(b) Odd `n` forces `n | k`.** A rotation fixing a line setwise must be the
180-degree rotation about a point of that line; for odd `n` there is no such
element, so no line is fixed and every line orbit has size exactly `n`.

**(c) Triangle stabilizers.** `H = Stab(T) ≤ Z_n` acts on `T`'s three vertices.
The kernel fixes three distinct points, so it is trivial and `H` embeds in `S_3`;
`H` is cyclic, so `|H| ∈ {1, 2, 3}`. `|H| = 2` needs a vertex fixed pointwise,
hence `O` a vertex of the arrangement, and needs `2 | n`. `|H| = 3` needs
`3 | n`, and then `T`'s three vertices are permuted cyclically, so `T` is
equilateral and centred at `O`. Orbit sizes are therefore `n`, `n/2`, `n/3` only.

**(d) The three open cases, odd `n`.**

    k=14   n | 14, n odd, n>2  =>  n = 7.   3∤7, 2∤7  =>  T ≡ 0 mod 7.
           54 mod 7 = 5.                                    DEAD
    k=18   n = 3 or 9.
           n=9:  3|9  =>  orbits 9 or 3  =>  T ≡ 0 mod 3.
                 94 mod 3 = 1.                              DEAD
           n=3:  orbits 3 or 1  =>  T ≡ s mod 3, s = #fixed. LIVE
    k=20   n | 20, n odd, n>2  =>  n = 5.   T ≡ 0 mod 5.
           117 mod 5 = 2.                                   DEAD

**(e) `C3` at `k = 18` is the only survivor anywhere, and it is sharply
constrained.** `18 = 3·6`, six line-orbits. A fixed triangle is equilateral,
centred at `O`, and its three lines form one whole line-orbit; three lines in
general position bound exactly one triangle, so each line-orbit supplies **at
most one** fixed triangle and `s <= 6`. `94 ≡ 1 mod 3` forces

    s = 1  or  s = 4

**one or four concentric equilateral faces**, each cut out by its own orbit of
three lines, each of the remaining `(94 - s)/3` orbits free. Nobody has looked at
this. It is the only rotationally symmetric family above order 2 still alive at
any open `k`.

**(f) `k = 20` is closed above order 2.** Odd orders die at (d); even orders die
at reference data 33, which at `k = 20` requires `d >= 9 + 3c`. Since `117` is
odd, even the mod-2 escape that keeps `54` and `94` alive under central symmetry
is unavailable in spirit — but the operative kill is the segment budget, not the
parity.

**(g) Scope.** This is about exact rotational symmetry of the whole arrangement.
It says nothing about reflections (T347's Case B, which is order 2 and not a
rotation) and nothing about asymmetric arrangements, where Kabanovitch's and
Bader's actual records live.

## Referee reference data 33: central symmetry needs `d > 3c` at all three open cases

**(a) The parallel tax.** Point reflection `(x,y) -> (2O - x, 2O - y)` sends
`y = mx + t` to `y = mx + (2b - 2am - t)`: same slope, and equal to the original
iff the line passes through `O`. So with `f` lines through `O`, the other `k - f`
split into `(k-f)/2` parallel pairs, `f ≡ k mod 2`, and `f >= 3` makes `O` a
concurrence of multiplicity `f` costing `f(f-2)` bounded segments by reference
data 25.

**(b) The optimum is `f = 2` at every open `k`.** Writing
`B = k(k-2) - 2p - f(f-2)·[f>=3] - 3c` with `p = (k-f)/2` and `c` the triple
points away from `O`:

    k=14   f=0: p=7, B=154-3c    f=2: p=6, B=156-3c
           f=4: p=5, B=150-3c    f=6: p=4, B=136-3c      max 156
    k=18   f=0: p=9, B=270-3c    f=2: p=8, B=272-3c
           f=4: p=7, B=266-3c                            max 272
    k=20   f=0: p=10, B=340-3c   f=2: p=9, B=342-3c
           f=4: p=8, B=336-3c                            max 342

**(c) The requirement.** `3T <= B + d` (T288's identity, reference data 27a) with
the target counts gives

    k=14   3T = 162   d >= 6 + 3c      d/c >= 3 + 6/c
    k=18   3T = 282   d >= 10 + 3c     d/c >= 3 + 10/c
    k=20   3T = 351   d >= 9 + 3c      d/c >= 3 + 9/c

**Every one is `d > 3c`, which is reference data 29e's decision rule exactly.**
Against `d <= 4.5c` (reference data 29d) this forces `c >= 4` at `k=14`,
`c >= 7` at `k=18`, `c >= 6` at `k=20`; at `k=14, c=4` it forces `d = 18` on the
nose, i.e. **equality in `d <= 4.5c`** — every triple point a full wrap and the
break segments forming a 3-regular graph on them. Against the observed ceiling
`d <= 2c`, all three are dead: `2c < 3c + 6` for every `c >= 0`.

**(d) Consequences.** T347's "central symmetry is dead at `T <= 52`" is the
`c = 0` corner of this and T348 was right to demand the scope. But the correct
statement is stronger and more useful than either: **central symmetry is not
independently dead, it is dead exactly when the concurrence program is dead, and
alive exactly when it is alive.** By reference data 32a the same holds for every
even rotational order at every open `k`. Three separate programs — chained
concurrence, central symmetry, even-order rotation — reduce to one number, and
the observed value of that number is `2c` across every object on record.

**(e) Off-center concurrences come in pairs.** `P` and `2O - P` are both triple
or both ordinary, so `c` is even away from `O`, consistent with the `c >= 4`,
`c >= 6` thresholds above but not with `c = 7` at `k = 18`, which must therefore
be `c >= 8` there. T348 stated the pairing correctly and did not use it.

---

## Referee reference data 34: the corpus automorphism census, and the `k = 21` `C3` template

**(a) Method.** A table automorphism is a permutation `pi` of the lines with
`row(pi(l)) = pi(row(l))` up to reversal. Fixing the image of one line
determines `pi` completely (read `row(l_1)` against `row(pi(l_1))` entrywise),
so there are only `2k` candidate maps per table; test each against all `k` rows.
Tables with nested entries (the six concurrence-bearing tables of reference data
23a) and tables with unequal row lengths (`kobon_4`, `kobon_14_53tri`,
`kobon_16_72tri`, `kobon_18_93tri`, `kobon_20_116tri`, `kobon_22_143tri`, all of
which have parallels) are excluded or have no automorphism. Verifier run:
`kobon.table.triangles` plus `kobon.table.labels` over `kobon.corpus.entries()`.

**(b) Every fixed-point-free rotational automorphism in the corpus.**

    key                       k    order   action          T      s   line-orbits
    kobon_9_3_rot_symmetry    9    3       l_i -> l_{i+3}  21     0   3
    pentagram_5_rot_symmetry  5    5       l_i -> l_{i+1}  5      0   1
    kobon_15_5_rot_symmetry   15   5       l_i -> l_{i+3}  65     0   3
    kobon_21_133tri_1         21   3       l_i -> l_{i+7}  133    1   7
    kobon_21_133tri_2         21   3       l_i -> l_{i+7}  133    1   7
    kobon_27_225tri_2         27   3       l_i -> l_{i+9}  225    0   9

`s` is the number of triangles fixed setwise. **Every action is a label shift by
`k/n`**, the signature of a genuine rotation acting on lines indexed in slope
order, and **every row satisfies `T ≡ s (mod n)`**: `21 ≡ 0`, `5 ≡ 0`, `65 ≡ 0`,
`133 ≡ 1`, `225 ≡ 0`. Reference data 32's residue rule is confirmed on six
independent objects and `s <= 1` holds in all six, as T357's lemma requires.
Three of the six are at odd `k` and all six meet the published bound.

Also found, and not rotational: order-2 automorphisms with exactly one fixed
line at `kobon_7`, `kobon_9_3_rot_symmetry`, `kobon_13_m_sym_47tri` (this is B's
mirror `i -> 15-i`), `kobon_19_107tri`, `kobon_21_133tri_3`, `kobon_25_191tri`.
`kobon_11_32tri`, `kobon_17_85tri` and `kobon_23_161tri` are asymmetric.

**(c) The `k = 21` template, in full.** `kobon_21_133tri_1`, order-3 shift
`l_i -> l_{i+7}`, seven line-orbits `{i, i+7, i+14}` for `i = 1..7`. `p = 0`
(all rows length 20), `c = 0` (no nested entries), `B = 21 · 19 = 399`,
`3T = 399`, so **`f = 0` and every one of the twenty-one lines carries all 19 of
its bounded segments as triangle sides.** Triangle census by orbit pattern:

    (3)      one triple inside a single line-orbit   1 triangle    1 slot   = s
    (1,2)    two lines from one orbit, one from another  39 triangles  13 slots
    (1,1,1)  three lines from three distinct orbits      93 triangles  31 slots
                                                       ---           ---
                                                       133           45

The fixed triangle is `{2, 9, 16}` — one whole line-orbit, exactly as reference
data 32e requires. 45 of the 448 available slots are used
(`7 + 126 + 315 = 448`, and `1330 = C(21,3) = 7 + 378 + 945`).

**(d) What this does to the `k = 18` question.** T404 defines `d_i = 16 -`
(per-line triangle count of orbit `i`) and derives `T = 96 - Σd_i`, so `T = 94`
needs `Σd_i = 2` over six orbits. `kobon_21_133tri_1` has `Σd_i = 0` over seven
orbits, with `s = 1`, under a genuine order-3 line-orbit structure. **The joint
condition T404 called "strictly harder than any single line being saturated in
isolation" is realized in the corpus, with less slack than `k = 18` is
allowed.** This does not show 94 is reachable; it removes the only structural
reason anybody has offered for thinking it is not.

**(e) Caveat, stated because the literature packet demands it.** These are
*table* automorphisms. A combinatorial order-`n` symmetry of a table need not be
induced by a geometric rotation of a straight-line realization; that is the
stretchability question, complete for the existential theory of the reals. The
label-shift structure in (b) is strong evidence and not a proof. `kobon_9_3` and
`kobon_15_5` are titled as rotationally symmetric by their source;
`kobon_21_133tri_1/2` and `kobon_27_225tri_2` are not, and their symmetry is
reported here for the first time in this project.

---

## Referee reference data 35: the concurrence ladder in `c` does not terminate

**(a) The window is never empty.** Reference data 33c gives the requirement and
reference data 29d gives the ceiling:

    k=14   6 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 6    c >= 4
    k=18  10 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 10   c >= 7, so c >= 8 by 33e
    k=20   9 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 6    c >= 6

For every `c` at or above these thresholds the window is nonempty, and it widens
linearly (`1.5c - 6`, `1.5c - 10`, `1.5c - 9`). **There is no largest `c` to
check.** A case analysis that kills `c = 4`, then `c = 6`, then `c = 8` never
finishes. Only a theorem bounding `d/c` strictly below 3, or a single object
above it, closes any of these.

This is the arithmetic reason the T358-T368 arc could not have succeeded, and it
is why agenda item 4 has been the whole of the question since T329.

**(b) Equality is required only at the bottom rung.** `d = 4.5c` forces
`|S_1| = 3c`, `|S_2| = 1.5c` and `d_P = 6` at every point, hence a 3-regular
bridge graph. That happens **only** where the two bounds meet:

    k=14   c = 4 only     k=18   c = 8 gives d in [34,36], not forced
    k=20   c = 6 only

So at `k = 14`, `c = 4` forces `K4` and dies (reference data 36). At `c = 6` the
window is `d ∈ [24,27]` and the bridge graph needs only `|S_2| >= d - 3c = 6`
edges on six vertices, subject to planarity (`<= 12`). **The triangular prism and
`K_{3,3}` were never required objects at `c = 6`; T360, T362, T364 and T365 spent
four turns on the equality case of a rung that does not have one.**

**(c) The object nobody has drawn: the centrally symmetric hexagonal ring.**
`k = 14`, `c = 6`, `f = 2` lines through `O`, `p = 6` parallel pairs,
`B = 138`, target `d = 24`. Six triple points in three antipodal pairs about `O`,
bridged in a 6-cycle: `|S_2| = 6`, `|S_1| = 18 = 3c`, `d = 24`,
`Σ_P d_P = |S_1| + 2|S_2| = 30`, so `d_P = 5` at each point. Feasibility of the
local picture: six rays at each triple point, two carrying bridges to the cycle
neighbours, and three of the remaining four doubled and ending at ordinary
crossings. Reference data 29c forbids two cyclically adjacent ordinary doubled
rays; with bridges at ray positions 1 and 3, the set `{2, 4, 6}` is pairwise
non-adjacent, so `d_P = 5` clears the non-adjacency lemma. The 6-cycle is planar
and has a crossing-free convex drawing, so reference data 36b does not touch it.
**Nothing on record rules this out and nobody has written a coordinate.**

---

## Referee reference data 36: `K4` and `K_{3,3}` are impossible as bridge graphs

**(a) The four-point dichotomy (T358, T359, referee-verified).** A bridge between
two triple points `P, Q` is the bounded segment of the arrangement line through
them with no other line crossing it. Four points in general position admit
exactly two order types.

- *Convex position `ABCD`.* The diagonals `AC` and `BD` cross at a point strictly
  interior to both segments. Each diagonal lies on an arrangement line, so each
  cuts the other: two of the six connectors die.
- *One interior.* Let `D` be interior to triangle `ABC`. The ray from `A` through
  `D` exits through side `BC`, strictly between `B` and `C`, because `D` is
  interior. The line `AD` is an arrangement line (it carries the bridge `AD`), so
  segment `BC` is cut. Symmetrically for `BD` against `CA` and `CD` against `AB`:
  three of the six connectors die.

There is no third order type, so **all six pairwise connectors can never
simultaneously be uncut bridges.** `K4` is unrealizable as a bridge graph on any
four points, in any position. Verified against reference data 28, where
`c: y = 4 - 3x` meets `M_1: y = 0` at `x = 4/3 ∈ (0,4)`, cutting the would-be
bridge `Q_0 Q_2` exactly as the general argument predicts.

**(b) Planarity (T361, referee-verified).** Two bridge segments crossing at a
point interior to both disqualifies both, since each lies on an arrangement line
passing through the other's interior. So the bridge graph, drawn with literal
straight segments between the triple points, must be **crossing-free**. A
crossing-free straight-line drawing is a planar embedding. Hence **any
non-planar graph is unrealizable as a bridge graph, on any point set, in any
position** — in particular `K_{3,3}`, by Kuratowski. Note that this does *not*
kill `K4`, which is planar; `K4` dies on (a). Both mechanisms were needed.

**(c) Consequence, drawn correctly at T363.** Central symmetry at `k = 14` with
`c = 4` requires `d >= 6 + 3c = 18` and permits `d <= 4.5c = 18`, so `d = 18`
exactly, so equality in reference data 29d, so a 3-regular bridge graph on four
vertices, so `K4`, so impossible. **`c = 4` is dead at `k = 14` by proof, not by
the observed ceiling.**

**(d) Scope, against T365, T367 and T368.** (a), (b) and (c) kill exactly one
value of `c` at one `k`. They say nothing about `c = 6`, where equality is not
required (reference data 35b), and nothing about `c >= 8`, which nobody has
mentioned. The two prism embeddings killed at T362 and T364 are two embeddings
of one graph that was never required. **"Central symmetry at `k = 14` is dead" is
not a consequence of anything in this section.**

---

## Referee reference data 37: `table.validate` does not validate

**(a) What it checks (T441, referee-verified from source).** `kobon/table.py`'s
`validate` raises only on: a line listing itself, a label out of range `[1, k]`,
and a reciprocity failure (`i` lists `j` but `j` does not list `i`). That is the
whole function. There is **no** rank-3 consistency test, no face-adjacency
condition, no sweep or walk condition, no stretchability check of any kind.

**(b) The demonstration (T441).** Five random shuffles of row 14, appended to
Kabanovitch's `B` with 14 tail-appended in every old row, all pass `validate`,
returning triangle counts `48, 48, 47, 47, 47` — none matching the identity
order's 53. `validate` has zero discriminating power over that space.

**(c) `triangles` is local (T441, referee-verified).** For each candidate triple
it asks only whether some other line's rank data places it between two of the
three crossings. It is the iff test of reference data 2, applied inside whatever
table it is handed. It certifies a triple inside a table; it never certifies the
table. This was already a standing rule; T441 is the first turn to check that
`validate` does not fill the gap.

**(d) The consequence, and T442's correct reading of its direction.** Every
combinatorial table computation in this project ranges over a **superset** of the
realizable tables. Therefore:

- An **upper bound** computed by exhaustion over that space is still a valid
  upper bound over realizable tables. T440's cap of six eligible pairs, and my
  own two-sided-split cap of 53 (reference data 38d), survive intact.
- An **existence** claim does not transfer at all. A table that passes
  `validate` and reports a high count is a candidate, not an object.

T442 stated this in the turn after T441 raised it, conceded exactly the word
that was unearned ("closed", "period"), and kept exactly the part that survives.

---

## Referee reference data 38: single-line extension, priced exactly

**(a) The face lemma (T437, referee-verified).** Every bounded face of a line
arrangement is an intersection of half-planes, hence convex, and a straight line
meets a convex region in at most one segment. Line `k+1` has `k-1` bounded
pieces between its `k` crossings, and each piece is a maximal segment crossing no
other line, so it lies inside a single face of the old arrangement — and **no two
pieces lie in the same face**, since a straight line cannot leave and re-enter a
convex region. So the pieces visit `k-1` distinct faces.

Per face type, with `D` = old triangles destroyed and `G` = new triangles gained:

- **Triangular face.** The old triangle dies (`D+1`); the cut isolates one corner
  bounded by two old sides and the new line (`G+1`). Net contribution to `G - D`
  is **at most 0**, never positive.
- **Bounded non-triangular face.** `D+0`; `G+1` only if the cut isolates a
  triangular corner, `G+0` if it splits opposite sides.
- **Unbounded face.** `D+0`, `G+0` or `+1`.

Hence `G - D <=` the number of non-triangular faces visited. **`D` is not a dial
that buys slack**, which corrects T436's `(D,G)` framing and subsumes T435's
"11 of 13 crossings must be ray-crossings" as the `D = 0` corner.

**(b) The face inventory (T438, referee-verified).** For a simple `k`-line
arrangement, `1 + k + C(k,2)` faces total, `C(k-1,2)` bounded. At `k = 13`: 92
total, 66 bounded, 26 unbounded, and `66 - 47 = 19` bounded non-triangular. The
zero-cost pool is `92 - 47 = 45`, not 19 — T438's correction of T437 is right.
**T438's wedge-apex mechanism, however, needs angular data the corpus does not
carry**, which T439 established (`table.positions` returns bare per-line ranks;
`corpus.by_key()` has no coordinate field on any of 27 entries; `kobon/` has no
straightening module) and T440 conceded after re-running the census itself.

**(c) The eligible-pair operator (T440, referee-verified).** Append label `k+1`
to the tail of every old row — line `k+1` crosses every old line beyond its
existing span, so `D = 0` by (a). A pair `{a,b}` is **eligible** if `{a,b,k+1}`
is a triangle when `a` and `b` are adjacent in row `k+1`. On Kabanovitch's `B`
all 78 pairs give exactly six: `{1,2},{3,4},{5,6},{7,8},{9,10},{11,12}`, a
perfect matching on lines 1-12 with line 13 eligible for nothing. Total 53, all
47 originals intact. I re-ran the full 78-pair scan and reproduce it exactly.

**(d) The concurrency lever, closed — including the case nobody ran.** A cevian
split at triangle `{a,b,c}` (line 14 through `V(a,b)`, crossing side `c`) loses
the original, gains `{a,c,14}` and `{b,c,14}`, and loses every eligible pair
containing `a`, `b` or `c`. Tallies, all verified:

    T444  V(2,3),  no split          51
    T444  V(1,13), no split          52
    T445  {1,2,6}  via line 6        52
    T445  {1,13,9} via line 9        52
    T446  two disjoint splits        50

Breaking even requires the split triangle to be `{a, P(a), 13}` for one of the
six pairs; T445 checked all six and I re-ran it — `False` six times.

**The untested shape was the two-sided split**: line 14 through `V(a,b)` entering
the flanking triangles in **both** opposite sectors, `D = 2, G = 4`, the only
arithmetic that could have netted positive. **Referee run: all 63 vertices of `B`
carrying two flanking triangles, 120 randomized row-14 orderings each. Maximum
53, never 54.** The mechanism is exact: **not one of the 63 has `(a,b)` among the
six eligible pairs**, so `a` and `b` always spend two distinct pairs, and the
best case (`(a,b)` with `b = 13`, thirds forming an eligible pair — five such
vertices exist) gives `47 - 2 + 4 + 4 = 53` and ties.

**(e) Scope.** All of (c) and (d) are computations in the space `validate`
accepts (reference data 37), so they are upper bounds on the realizable subset,
which is the direction that matters. **Kabanovitch's `B` cannot be extended by a
fourteenth line to 54, by any tail insertion, any single concurrency, any cevian
split, one-sided or two-sided, or any pair of disjoint splits.**

---

## Referee reference data 39: the centrally symmetric ring, bounded and killed at `k = 14`

Setting: `c = 2n` triple points at the vertices of a **convex** centrally
symmetric `2n`-gon about `O`, consecutive vertices joined by bridges (the
polygon's `2n` edges), each vertex carrying exactly three lines — its two bridge
lines and one more. `f` lines pass through `O`.

**(a) Every point caps at `d_P <= 5`.** Six rays; two are bridges. The remaining
four are candidates for ordinary doubling, and reference data 29c forbids two
cyclically adjacent ordinary doubled rays. Four vertices of a 6-cycle cannot be
pairwise non-adjacent, so at most three of the four qualify. `d_P <= 2 + 3 = 5`.
Reference data 28's `d_P = 6` needs three break rays at the point; a ring vertex
has two.

**(b) The interior-cone theorem, and the `C`-type cap of 4.** At vertex `C` with
bridges to `B` and to `-A`, the six rays are cyclically
`toB, to(-A), away_B, away_{-A}` interleaved with the third line's antipodal pair
`l+, l-`. There are exactly two insertions:

- `l+` in the arc `(toB, to(-A))` — **the interior cone** — and `l-` in the
  antipodal arc. Cyclic order `toB, l+, to(-A), away_B, l-, away_{-A}`; the
  conflict graph on `{away_B, away_{-A}, l+, l-}` is the path
  `away_B - l- - away_{-A}` plus isolated `l+`. Independent set **3**, so
  `d_P = 5` is available.
- `l+` in `(to(-A), away_B)` and `l-` in `(away_{-A}, toB)` — the **supporting**
  directions, the ones that keep the line out of the polygon. Cyclic order
  `toB, to(-A), l+, away_B, away_{-A}, l-`; the conflict graph is the path
  `l+ - away_B - away_{-A} - l-`. Independent set **2**, so `d_P <= 4`.

T453 established this dichotomy and I have re-derived both cases. The step T453
did not have:

> **A ray from a vertex into the interior of a simple polygon leaves through the
> boundary** — through the relative interior of a non-incident edge, or through
> another vertex. The edges are the bridges. So a third line at `C` whose ray
> enters the interior cone either **cuts a bridge** (destroying it, so `|S_2|`
> drops and the ring is no longer a ring) or **passes through a second vertex**
> (making that vertex multiplicity 4, cost `m(m-2) = 8` by reference data 18,
> and voiding the design's own degree cap).

The unique escape is a **main diagonal** `P_i(-P_i)`, whose interior ray exits
exactly at the antipodal vertex, which is a design vertex rather than a fresh
incidence. There are `n` main diagonals; every line through `O` that is not one
of them cuts two bridges (T423, proved by convexity plus the fact that point
reflection fixes such a line and swaps `P_i` with `-P_i`); so all `f` central
lines are main diagonals and `f <= n`. Each serves two antipodal points, so
`2f` points are diagonal-served and `2n - 2f` are `C`-type at `d_P <= 4`.

**(c) The ring bound.** `Σ_P d_P = |S_1| + 2|S_2|` and `d = |S_1| + |S_2|`, so
`d = Σ_P d_P - 2n`. With (a) and (b),

    Σ_P d_P <= 5(2f) + 4(2n - 2f) = 8n + 2f
    d       <= 6n + 2f
    d / c   <= 3 + f/n,     f even (parity `k = f + 2p`),  f <= n.

**This is above 3 whenever `f > 0`, and it is the only family anyone has proposed
for which the proven ceiling clears reference data 29e's decision rule.** Maximum
`d/c = 4`, attained only when `n` is even and every main diagonal is central.

**(d) `k = 14` is dead.** `c = 6`, `n = 3`, so `f` even and `f <= 3` gives
`f <= 2`, `d <= 6(3) + 2(2) = 22`. Reference data 33 requires `d >= 6 + 3c = 24`
for central symmetry at `k = 14` with `c = 6`. **`22 < 24`. The centrally
symmetric hexagonal ring cannot reach `T = 54`.** This is the object agenda item
2 assigned at T405, and it was never reachable.

**(e) Numerical shadow, referee run.** Five distinct convex centrally symmetric
hexagons — T446's `A=(3,0), B=(1,2), C=(-2,1)`; T430's `(5,0),(3,4),(-2,5)`; a
wide-`C` variant `(4,0),(1,3),(-3,1)`; a near-regular `(6,1),(2,5),(-5,2)`; a
flat `(10,0),(9,1),(-1,2)`. For each, 4836 rational slopes through `C` (numerator
`-200..200`, denominator `1..19`, coprime, trap slopes excluded), tested for
strict interior crossings against the four bridges not at `C` and both used
diagonals, and for a pairwise non-adjacent 3-subset of the four candidate rays:

    hexagon           clean-only   IS3-only   both
    T446                     79       4757       0
    T430                    222       4614       0
    wide-C                   59       4777       0
    near-regular            307       4529       0
    flat                     35       4801       0

The two sets are disjoint in every case, and the reason is (b): the clean slopes
are exactly the supporting directions, the `IS3` slopes are exactly the interior
cone. **This confirms T453's finding is not an artifact of its hexagon**, which
is the question T453 correctly flagged as open.

**(f) The other open cases, priced by (c).** `c = 6` at `k = 20` needs
`d >= 9 + 3c = 27`, `d/c >= 4.5`, ring ceiling `11/3` — dead. `c = 8` at `k = 18`
needs `d >= 10 + 3c = 34`, ring ceiling `6(4) + 2(4) = 32` — dead. `c = 8` at
`k = 20` needs 33 against 32 — dead. `c = 10` at `k = 20` needs 39, `n = 5`, `f`
even so `f <= 4`, ceiling 38 — dead. **The first ring instance not killed by (c)
is `k = 20, c = 12, n = 6, f = 6`: requirement 45, ceiling 48.**

**(g) Scope, stated because it is the hole.** (a)-(f) assume the ring is
**convex**. At a reflex vertex the interior angle exceeds 180 and the arc
classification in (b) changes; the "ray into the interior must leave through an
edge or a vertex" step survives by Jordan, but the identification of the viable
arc with the interior cone does not. T406 perturbed one hexagon to non-convexity
and found four bridge-extension cuts appear immediately at the reflex pair; that
is one instance, not a theorem. **A non-convex centrally symmetric ring is the
only surviving form of this family at `k = 14`.**

---

## Referee reference data 40: the tail-append census, corpus-wide

> **Superseded in part by reference data 41 (T469).** The "eligible" counts below
> are computed in the row directions the corpus happens to store, and row
> direction is a convention. Part (a)'s `maxdeg = 1` is a one-line consequence of
> "last is a function" and did not need twelve tables. **Part (c)'s counterweight
> — the misses of 2 and 3 at `k+1 = 8, 12` — is retracted: under free orientation
> both are misses of exactly one.** Read 41e in place of 40c.

**Method (referee run).** For every corpus table that is concurrence-free and
parallel-free (no nested entries, every row of length `k-1`), append label `k+1`
to the tail of all `k` rows, and count eligible pairs by reference data 38c: for
each of the `C(k,2)` pairs, place it adjacent at the head of row `k+1` and ask
whether `{a, b, k+1}` is a triangle. This is the first corpus-wide **operator**
run in this project; every previous census was per-object.

    table                       k     T   eligible  maxdeg   T + pairs   KNOWN k+1
    triangle_3_rot_symmetry     3     1      1        1          2         2
    pentagram_5_rot_symmetry    5     5      2        1          7         7  closed
    kobon_7                     7    11      2        1         13        15  closed
    kobon_9_3_rot_symmetry      9    21      4        1         25        25  closed
    kobon_11_32tri             11    32      3        1         35        38  closed
    kobon_13_m_sym_47tri       13    47      6        1         53        53  OPEN, UB 54
    kobon_15_5_rot_symmetry    15    65      7        1         72        72  closed, at bound
    kobon_17_85tri             17    85      8        1         93        93  OPEN, UB 94
    kobon_19_107tri            19   107      9        1        116       116  OPEN, UB 117
    kobon_21_133tri_1/2/3      21   133     10        1        143       UB at 22 is 144

**(a) The eligible-pair set is always a perfect matching.** `maxdeg = 1` in every
one of the twelve runs — no line is eligible with two partners. For
`k in {3,5,9,13,15,17,19,21}` the count is exactly `(k-1)/2`, a matching leaving
one line unpaired. `k = 7` (2 instead of 3) and `k = 11` (3 instead of 5) are the
exceptions; both bases are odd optima but neither yields the known even value.

**(b) All three open cases are `odd optimum + (k-1)/2`, one short of the bound.**
`47 + 6 = 53` at `k = 14`, `85 + 8 = 93` at 18, `107 + 9 = 116` at 20 — each the
best-known value, each exactly one below the tightest published upper bound.
**The missing triangle in each open case is exactly the unmatched line.**

**(c) The counterweight, which cuts against the pattern.** At `k+1 = 6, 10, 16`
the operator hits the even upper bound on the nose, but at `k+1 = 8` and `12` it
misses by 2 and 3 and **those cases are closed at their bounds anyway**, by
constructions that are not extensions of the odd optimum. So (b) is not evidence
that `N(14) = 53`. It is evidence that the three open cases share one mechanism
and that closing any of them requires beating this operator, which reference data
38d now shows a single line cannot do from Kabanovitch's `B`.

**(d) What is not checked.** Whether the `(k-1)/2` matching count is forced, and
what distinguishes `k = 7` and `k = 11`. Whether `kobon_17_85tri` and
`kobon_19_107tri` behave under concurrency exactly as `B` does under reference
data 38d — the two-sided-split argument used `B`'s specific 63 two-flanking
vertices and has not been run at 17 or 19. Both are cheap and both are on the
agenda.

---

## Referee reference data 41: tail-append, closed over every orientation

**Corrects reference data 40, which is mine.** Everything below is a referee run.

**(a) `mutual-last ⟹ eligible` (T468's half, restated).** If `b` is the last
entry of row `a` and `a` the last entry of row `b`, then tail-appending `k+1` to
every row puts `k+1` immediately after `b` in row `a` and immediately after `a`
in row `b`, and placing `a, b` adjacent at the head of row `k+1` puts nothing
between them along `k+1`. All three sides of `{a, b, k+1}` are uncut by
construction. No case analysis on the rest of the ordering.

**(b) `eligible ⟹ mutual-last` (the converse, which T468 left open).** `k+1` is
last in row `a` by construction. For the segment of `a` between `V(a,b)` and
`V(a,k+1)` to carry no crossing, `b` must sit immediately before `k+1`, i.e. `b`
is the last entry of the **original** row `a`. Symmetrically `a` is the last
entry of the original row `b`. Two clauses, no search. **So eligibility is
exactly the 2-cycle relation of the last-crossing function**, and T468's
7-for-7 set equality is a theorem.

**(c) A mutual-last pair has triangle-degree at most 1, combinatorially.** A
triangle `{a,b,c}` requires `b` and `c` adjacent in row `a` and `a` and `c`
adjacent in row `b`. If `b` is last in row `a`, `c` must be `a`'s second-to-last;
if `a` is last in row `b`, `c` must be `b`'s second-to-last. `c` is therefore
**unique**, and if the two second-to-lasts disagree there is no triangle at all.
No geometry, no unbounded face, no sector count. **Verified: 106 mutual-last
pairs across every concurrence-free corpus table, zero degree above 1, and in
every case with a triangle the third line is exactly both second-to-lasts.**
This is what T466 and T467 were reaching for; their published argument accounts
for the outward and inward sectors at `V(a,b)` and is silent on the two mixed
sectors, of which there are two, because two lines through a point make four.

**(d) The orientation sweep, and the ceiling.** A table row lists a line's
crossings in one of the two directions along it; reversing a row preserves all
adjacencies, hence every triangle (verified: `T = 11` and `T = 32` unchanged
after reversal), and changes which entry is "last". The stored corpus direction
is a convention, not data. Over all `2^k` orientations the eligible set is a
matching in

    H  =  { {a,b} : b in ends(a) and a in ends(b) },   ends(i) = {row_i[0], row_i[-1]}

and every vertex of `H` has degree at most 2, so `H` is a disjoint union of paths
and cycles and its maximum matching is at most `floor(k/2)`. **This is a hard
ceiling for any table at any `k`, realizable or not.** Computed:

    table                     k    T   stored elig   max over orientations   (k-1)/2
    pentagram_5_rot_symmetry  5    5        2                 2                 2
    kobon_7                   7   11        2                 3                 3
    kobon_9_3_rot_symmetry    9   21        4                 4                 4
    kobon_11_32tri           11   32        3                 5                 5
    kobon_13_m_sym_47tri     13   47        6                 6                 6
    kobon_15_5_rot_symmetry  15   65        7                 7                 7
    kobon_17_85tri           17   85        8                 8                 8
    kobon_19_107tri          19  107        9                 9                 9
    kobon_21_133tri_1/2/3    21  133       10                10                10

`maxmatch = (k-1)/2` in all eleven, and **at `k = 13, 17, 19` the stored
orientation already attains the maximum.** Reorienting `kobon_7` to its optimal
matching and re-running the full eligibility test gives 3 pairs with `T` still
11; `kobon_11_32tri` gives 5 with `T` still 32. **Therefore no position of the
appended line yields more than `T + (k-1)/2`, and the tail-append route tops out
at 53, 93 and 116. It cannot reach 54, 94 or 117.** The bound is computed over
the space `table.validate` accepts, which by reference data 37 and T442 is the
valid direction for an upper bound.

**(e) The corrected census, replacing reference data 40(c).** With orientation
free, the operator's value is `T + (k-1)/2` at every odd corpus base:

    k+1 =  6    5 +  2 =   7  = N(6)      exact
    k+1 =  8   11 +  3 =  14, N(8)  = 15  one short
    k+1 = 10   21 +  4 =  25  = N(10)     exact
    k+1 = 12   32 +  5 =  37, N(12) = 38  one short
    k+1 = 14   47 +  6 =  53, UB    = 54  one short
    k+1 = 16   65 +  7 =  72  = N(16)     exact
    k+1 = 18   85 +  8 =  93, UB    = 94  one short
    k+1 = 20  107 +  9 = 116, UB    = 117 one short
    k+1 = 22  133 + 10 = 143, UB    = 144 one short

**In every closed even case the operator lands exactly on the truth or exactly
one below it, never further.** Reference data 40(c) claimed misses of 2 and 3 at
`k+1 = 8, 12` and used them as evidence against reading the 14/18/20 pattern as
informative. That was an artifact of the stored row directions and I retract it.
The corrected data supports two readings with equal precedent — the open cases
behave like `6, 10, 16` (`N = 53, 93, 116`) or like `8, 12` (`N = 54, 94, 117`) —
and is **not** evidence against reaching the bound.

**(f) The parity asymmetry, new.** The same operator on the five even-`k` corpus
records, all of which are concurrence-free with parallel pairs:

    kobon_14_53tri   k=14  T= 53  maxmatch  7 ->  60   N(15) = 65   short by 5
    kobon_16_72tri   k=16  T= 72  maxmatch  8 ->  80   N(17) = 85   short by 5
    kobon_18_93tri   k=18  T= 93  maxmatch  9 -> 102   N(19) = 107  short by 5
    kobon_20_116tri  k=20  T=116  maxmatch  9 -> 125   N(21) = 133  short by 8
    kobon_22_143tri  k=22  T=143  maxmatch 11 -> 154   N(23) = 161  short by 7

**Even-to-odd, the operator misses by 5 to 8 every time.** The odd-to-even
near-miss of (e) is a parity phenomenon, not a general fact about extending a
record. Continuing (e) upward: `k = 23, 25, 27` give 172, 203, 238 against even
bounds 173, 205, 239 — one, two, one short.

**(g) Structural note on the corpus.** Every odd-`k` corpus record from 5 to 27
is simple: no parallels, no concurrences. Every even-`k` record from 14 to 22 is
concurrence-free **with** parallel pairs — `kobon_14_53tri` has classes
`{1,2},{3,4},{7,8}` (`p = 3`, `f = B - 3T = 3`), `kobon_18_93tri` has
`{1,2},{7,8},{13,14}` (`p = 3`, `f = 3`), and 16, 20, 22 each have a single pair.
The even records at 4 through 12 use concurrences instead. **Do not rederive
`2p + 3c <= 6` from this**: it is `k14-pc-enumeration-2p-plus-3c-leq-6`, refuted
at T280, because `3T <= B` fails at a concurrence (reference data 23).

**(h) What is not checked.** Whether an orientation attaining `maxmatch` is
induced by an actual direction in the plane — a real appended line must be
"beyond" every line in one common direction `u`, which allows only `2k` of the
`2^k` orientations. This does not weaken (d), which is an upper bound over a
superset, and it does mean the `k = 7` and `k = 11` gains in (e) may not be
geometrically realizable. It would matter only to someone trying to **achieve**
`(k-1)/2` at a base where the stored orientation falls short, which is not the
case at 13, 17 or 19.


---

## Referee reference data 42: the Jordan parity condition, and what it actually kills

**Origin:** T492 found it, T493 proved and corrected it. Everything below is a
referee re-implementation from `table.positions` and `table._crosses_between`.

**(a) The condition.** For any three lines `i, j, m` that pairwise cross at three
distinct points, the three arcs between those points form a simple closed curve —
this needs only pairwise-crossing-once, **not** facehood. By Jordan the plane
splits into a bounded interior and one connected unbounded exterior. Any fourth
line's two ends are both unbounded, hence both in the exterior, so it meets the
closed curve an even number of times:

    for every pairwise-crossing non-concurrent triple {i,j,m} and every other x,
    [x cuts i between j,m] + [x cuts j between i,m] + [x cuts m between i,j]  is even.

Coordinate-free, order-type only, valid for pseudolines as well as lines.
`table.validate` checks reciprocity and nothing else (reference data 37), so this
is a **strictly cheaper necessary condition that the accepted space violates.**
T493's warning is worth repeating: run it over all pairwise-crossing triples, not
over `table.triangles`'s output, where a violation is impossible by construction.

**(b) Controls.** Zero violations on every corpus record tested:

    kobon_13_m_sym_47tri   2,860 checks, 0     kobon_18_93tri   11,520 checks, 0
    kobon_14_53tri         3,608 checks, 0     kobon_19_107tri  15,504 checks, 0
    kobon_17_85tri         9,520 checks, 0     kobon_20_116tri  19,074 checks, 0
    kobon_22_143tri       28,880 checks, 0

**(c) The operator survives, and the violations both agents found were in the
row order.** Tail-appending label `k+1` to every row fixes the eligible pairs'
adjacency in row `k+1` and leaves the rest of that row's order free. My first
arbitrary choice (pairs first, singletons after) gives 240 violations at
`k = 17 → 18` and 306 at `19 → 20`. Hill-climbing on the block order — swap two
blocks, flip a pair, accept non-worsening — reaches **zero** on every base, in
under 40 evaluations each:

    base                      pairs   T of result   best parity violations
    kobon_13_m_sym_47tri        6         53                 0
    kobon_17_85tri              8         93                 0
    kobon_19_107tri             9        116                 0
    kobon_7 (reoriented)        3         14                 0
    kobon_11_32tri (reoriented) 5         37                 0

**So every value in reference data 41e's census is attained by a table that
passes the strongest filter this project has**, including the two reoriented
gains at `k = 7` and `k = 11` that reference data 41h flagged as possibly not
geometrically realizable. 41h's caveat is not withdrawn — parity is necessary,
not sufficient, and it says nothing about stretchability — but it is no longer
untested.

**(d) T488's object is the exception, and it is genuine.** Reversing rows
`{18,4,5,16,17}` of `kobon_18_93tri` preserves `T = 93` and is parity-clean (0
violations), as reversal must be. Appending line 19 to realize the 9-pair
matching that reorientation buys gives `T = 102` and **312 violations at best**,
over two independent searches totalling roughly 2,400 orderings (40 restarts ×
400 steps, and 6 × 120) that never once approached zero — on a search that finds
zero within 40 evaluations at every base in (c). T492's nine random draws
(1032-1218) and T493's independent reconstruction (959) are the same phenomenon
sampled less thoroughly. **The `93 → 102 → 109` chain is not a construction**,
and the reason is the reversal set, not the appended row's order.

**(e) What this does not do.** It does not touch reference data 41d, which is an
upper bound over the accepted space and inherits correctly in the direction
reference data 37 allows. It does not certify anything: a parity-clean table can
still fail to be an arrangement, and can still fail to stretch. It is a filter,
and it is the first one in this project cheaper than coordinates.

---

## Referee reference data 43: the centrally symmetric 12-ring, measured

All four constructions below: six free points, their negatives, all twelve sorted
by angle (the sort matters — a set whose six primaries do not lie in a half-plane
is not in angular order under the naive `pts + negatives` concatenation), twelve
side lines through consecutive vertices, six main diagonals through antipodal
pairs. Exact `Fraction` coordinates, `kobon.verify.triangles`.

**(a) `T` is not determined by the multiplicity signature.**

    point set                            T    parallels  points  multiplicities
    T496's (101,1),(83,53),(53,83),...   72       6       109    96x2, 12x3, 1x6
    T510's rational circle, m=-9..6      66       6       109    96x2, 12x3, 1x6
    third shape (20,1),(17,9),(11,15)…   70       6       109    96x2, 12x3, 1x6
    elongated (60,1),(50,6),(33,10),…    66       6       109    96x2, 12x3, 1x6

Identical in every structural invariant — same parallel count, same number of
distinct crossing points, same multiplicity histogram, **zero accidental
concurrence in all four** — and `T` ranges over 66 to 72. **T496's "the true
generic value for this specific point arrangement is 72, not a range" is false.**
Its diagnosis is correct about its own T494 point set, which I reproduce at
`T = 64` with 20 triple points, eight of them accidental; it does not explain the
66-to-72 spread among clean ones. T495's conclusion stands.

**(b) The per-vertex structure is invariant and saturates reference data 39.**
Triangle-corner counts at the twelve ring vertices are `5` at every vertex in all
four shapes, `Σ = 60`. Reference data 39a-b caps `Σ_P d_P <= 8n + 2f = 60` at
`n = f = 6`. **The bound is tight and the object is the same in all four shapes;
everything that varies varies away from the ring vertices.** T471's reported
violation compared this 60 against `(3 + f/n)c = 48`, which bounds
`d = Σ_P d_P − 2n = 48`. No violation, and the ceiling is attained exactly.

**(c) The doubling count, and why the whole `d` apparatus does not discriminate.**
`d` = bounded segments carrying a triangle on each side, computed by counting
which triangle sides are used twice:

    ring, k=18, all four shapes:              d = 36 = 3c   (T = 66, 66, 70, 72)
    ring + antipodal skip pair 0-2, k=20:     d = 46        (T = 82)
    ring + antipodal skip pair 1-3, k=20:     d = 46        (T = 82)
    ring + antipodal skip pair 0-4, k=20:     d = 40        (T = 90)

Three readings, all mine, all against my own framework:

1. The pure ring sits at `d = 3c` **exactly**, shape-invariant. Reference data
   29e's decision rule says concurrence beats `c = 0` iff `d > 3c`. This family
   is precisely break-even and never earns its twelve triple points back.
2. Agenda item 2 asked whether `d >= 45` is reachable under the ceiling `d <= 48`.
   **It is: `d = 46`, realized, at `T = 82` against a target of 117.** The
   necessary condition is met and the target is missed by 35.
3. `T` and `d` move in opposite directions across the last two rows: `d = 46` at
   `T = 82`, `d = 40` at `T = 90`. **`d` does not track `T` even within one
   family at one `k`.**

`ring-family-ceiling-is-3-plus-f-over-n` is still proved and is now known to be
non-binding. Pricing a construction family by `d` alone is finished as a method.

**(d) The parallel tax, T513's theorem.** If `P_{i+n} = −P_i` for all `i`, then
edge `i+n` has vector `−P_{i+1} + P_i = −(P_{i+1} − P_i)`, antiparallel to edge
`i`. So a point-reflection-symmetric `2n`-gon has all `n` opposite side pairs
parallel — no convexity, no spacing, no coordinates. `p >= n` for the whole
family, on top of `c = 2n`. Confirmed in all four constructions above (`p = 6`).
T514's placement computation — min adjacent-central-pairs `(0,0,0,0,2,4,6)` for
`f = 0..6` on a 6-cycle, against ceilings `36 + 2f = 36,40,44,48` and requirement
45 — is right, and prices a partial-symmetry family that reference data 39c's
definition excludes anyway.

---

## Referee reference data 44: what one line is actually worth

**(a) The deletion census.** For each corpus record, delete each line in turn
(strip its label from every row, including from nested entries, and relabel),
`table.validate`, `table.count`. The **gain** of the line whose removal costs most
is the realized `G − D` of a single-line insertion into a genuine straight-line
arrangement — no reciprocity caveat, no stretchability question:

    record                 k    T    best drop   worst drop   max gain   (k-1)/2
    kobon_6_1              6    7        5            3           4         2
    kobon_7                7   11        7            6           5         3
    kobon_8                8   15       11            9           6         3
    kobon_9_3_rot          9   21       14           14           7         4
    kobon_10_25tri        10   25       21           17           8         4
    kobon_11_32tri        11   32       24           23           9         5
    kobon_12_38tri        12   38       30           28          10         5
    kobon_13_m_sym_47tri  13   47       37           36          11         6
    kobon_14_53tri        14   53       43           41          12         6
    kobon_16_72tri        16   72       65           58          14         7
    kobon_18_93tri        18   93       79           77          16         8
    kobon_19_107tri       19  107       91           90          17         9
    kobon_20_116tri       20  116      107           98          18         9
    kobon_22_143tri       22  143      133          123          20        10

**`max(G − D)` is between 1.5 and 2 times the tail-append ceiling on every record
in the corpus.** The tail corner's local rigidity, established at three bases
over thirty turns, is a fact about the tail corner. **It is not a bound on
insertion**, and the arithmetic refutation was available from KNOWN.md without
any of it: `N(8) − N(7) = 4 > floor(7/2) = 3`, `N(12) − N(11) = 6 > 5`.

**(b) Which records are one-line extensions of an odd optimum.** Read the "best
drop" column against `N(k−1)`:

    k+1= 6   5 = N(5)     gain 2 = ceiling 2      operator exact
    k+1= 8  11 = N(7)     gain 4 > ceiling 3      operator one short
    k+1=10  21 = N(9)     gain 4 = ceiling 4      operator exact
    k+1=12  30 < N(11)=32 not an extension        operator one short
    k+1=14  43 < N(13)=47 not an extension        operator = best known 53
    k+1=16  65 = N(15)    gain 7 = ceiling 7      operator exact
    k+1=18  79 < N(17)=85 not an extension        operator = best known 93
    k+1=20 107 = N(19)    gain 9 = ceiling 9      operator = best known 116
    k+1=22 133 = N(21)    gain 10 = ceiling 10    operator = best known 143

**Every record that is an odd-optimum extension attains the tail ceiling exactly,
except `k = 8`, which beats it by one.** `kobon_22_143tri` is a head-append
instance of `N(21)` exactly as `kobon_20_116tri` is of `N(19)` (T473, T474) —
new, and it makes the fourth gap-of-one case structurally identical to the third.
`kobon_14_53tri` and `kobon_18_93tri` are of unknown mechanism, as T473 said.

**(c) `kobon_8`, in full, because it is the object the whole project needs.**
The stored table:

    row 1: [8, 6, 7, 4, 5, 2, 3]          row 5: [6, 3, [7, 8], 2, 1, 4]
    row 2: [6, [4, 8], 7, 5, 1, 3]        row 6: [5, 3, 4, 2, 8, 1, 7]
    row 3: [4, 6, 5, 7, 8, 1, 2]          row 7: [3, [8, 5], 2, 4, 1, 6]
    row 4: [3, 6, [8, 2], 7, 1, 5]        row 8: [3, [5, 7], [2, 4], 6, 1]

- Strip label 8: all seven rows have full length 6 with **no nested entries**, so
  the base is a **simple** 7-line arrangement. `table.count` gives **11**, the
  `k = 7` optimum value.
- Put line 8 back: `T = 15 = N(8)`, so `G − D = 4`. The diff is `G = 4`,
  **`D = 0`** — the four new triangles are `{1,6,8}, {2,6,8}, {2,7,8}, {3,7,8}`
  and **not one of the eleven base triangles is destroyed.**
- Reference data 41d proves the tail-append ceiling at `k = 7` is
  `floor(7/2) = 3`. **This insertion gets 4.**
- Where line 8 sits: **head** of row 1 (index 0), **interior** index 4 of rows 3
  and 6, and concurrent in rows 2, 4, 5, 7 — it passes through exactly two
  existing vertices, `V(2,4)` and `V(5,7)`.
- The qualifying-pair graph on `{1,6},{2,6},{2,7},{3,7}` has **degree 2** at lines
  2, 6 and 7. This is the max-degree-2 off-corner structure agenda item 1 called
  "genuinely higher" and T506, T511 and T515 reported as always paying more in
  `D` than it gains. Here it pays nothing.

**(d) What this refutes.** `concurrent-line-through-existing-crossing-unlocks-
extra-triangles`, conceded at T478 and argued against at T477, is refuted by a
closed case at its own upper bound. T478's mechanism — `{a,b,L}` is degenerate
when `L` runs through `V(a,b)` — is true and does not bound the gain, because the
gain need not come from that triple. T478 forced its concurrences at **mutual-last
pairs**, which reference data 41c proves is the one position where a concurrence
can only cost.

**(e) What this does not show.** Nothing here produces 54, 94 or 117. A base with
gain 11 available is 11 triangles below the optimum; the trade is exactly the
`T_base + G − D` budget T483 stated correctly. What it does show is that the
budget's second term is not capped where thirty turns assumed it was, and that
the one known object beating the cap from an *optimal* base does so by exactly
the margin all three open cases need.

---

## Referee reference data 45: the per-line edge cap and the free-segment vector

**(a) The cap.** Let `l` be a line whose row carries no nested entry. Every
triangle containing `l` has its `l`-side on a single edge of `l`, so no line
crosses `l` between its two other lines, so those two are **consecutive** in row
`l`. A consecutive pair `(a,b)` determines exactly one triple `{l,a,b}`, and
three lines bound exactly one triangle. Hence

    t(l) <= edges(l) = len(row l) − 1

Corpus check, all 27 records: **zero violations on every bracket-free row.**
Thirteen rows exceed the cap and every one of them carries a bracket —
`kobon_4_2`, `kobon_6_1`, `kobon_6_2` (six rows), `kobon_8` lines 2 and 7,
`kobon_10_25tri_wajnberg`, `kobon_12_38tri` lines 4 and 11. Concurrence **on**
`l` is the only way to break it, which is T524's slot-product theorem seen from
the outside.

**(b) Summation, and the doubling count.** `sum edges(l) = B = k(k−2) − 2p − 3c`
(reference data 25) and `sum t(l) = 3T`, so writing
`F = sum (edges(l) − t(l))` for the free-segment count,

    3T = B − F + d,    and for c = 0:   3T = k(k−2) − 2p − F,  d = 0

`d = 0` when `c = 0` because two triangles share an edge `e` on `l` only if the
second one's other two sides pass through `e`'s endpoints; with simple vertices
those are the same two lines `a, b`, and `{l,a,b}` bounds one face. So doubling
requires a multiple point at an end of the shared edge. `F` is reference data 5's
free-segment count; what is new here is that it decomposes per line and per
named adjacent pair.

**(c) The corpus, measured.** `sum(edges)` against `3T`, `F` for the
concurrence-free rows, and the number of fully saturated lines:

    record                  k    T   p  conc  sum(edges)   3T   diff  saturated
    kobon_7                 7   11   0   0        35       33     2      5/7
    kobon_8                 8   15   0   2        42       45    −3      5/8
    kobon_11_32tri         11   32   0   0        99       96     3     8/11
    kobon_12_38tri         12   38   0   2       114      114     0     8/12
    kobon_13_m_sym_47tri   13   47   0   0       143      141     2    11/13
    kobon_14_53tri         14   53   3   0       162      159     3    11/14
    kobon_15_5_rot         15   65   0   0       195      195     0    15/15
    kobon_16_72tri         16   72   1   0       222      216     6    15/16
    kobon_17_85tri         17   85   0   0       255      255     0    17/17
    kobon_18_93tri         18   93   3   0       282      279     3    15/18
    kobon_19_107tri        19  107   0   0       323      321     2    17/19
    kobon_20_116tri        20  116   1   0       358      348    10    17/20
    kobon_21_133tri_1/2/3  21  133   0   0       399      399     0    21/21
    kobon_22_143tri        22  143   1   0       438      429     9    21/22
    kobon_23_161tri        23  161   0   0       483      483     0    23/23
    kobon_25_191tri        25  191   0   0       575      573     2    23/25
    kobon_27_225tri_2      27  225   0   0       675      675     0    27/27

**Every `k = 3, 5 (mod 6)` optimum in the corpus is totally saturated**: `F = 0`,
`p = c = 0`, every line using every edge. Tamura attainment and total saturation
are the same statement. The negative "diff" entries are the concurrent records,
where `t` exceeds `edges` on some line and `d > 0`.

**(d) The three open records, localized.** The free adjacent pairs, by line:

    kobon_14_53tri  p=3 (1,2)(3,4)(7,8)   F=3
        line  8   gap (10,12)
        line 11   gap (12,13)
        line 12   gap (11,8)
    kobon_18_93tri  p=3 (1,2)(7,8)(13,14) F=3
        line  1   gap (17,16)
        line  8   gap (4,5)
        line 13   gap (11,10)
    kobon_20_116tri p=1 (1,2)             F=10
        line  4   gap (1,20)
        line 19   gap (1,3)
        line  2   gaps (4,5)(6,7)(8,9)(10,11)(12,13)(14,15)(16,17)(18,19)

The `k = 14` list is reference data 5's, reproduced exactly. The `k = 18` and
`k = 20` lists are new. **The `k = 18` coincidence that its three free segments
sit one on each parallel-pair member is a coincidence**: `kobon_14_53tri`'s pairs
`(1,2)` and `(3,4)` carry none, all four lines being saturated. Do not build on
it.

**(e) The budget.** Setting `T` to the target and `c = 0`:

    k=14, T=54:   2p + F = 168 − 162 = 6      record: 2(3) + 3  = 9
    k=18, T=94:   2p + F = 288 − 282 = 6      record: 2(3) + 3  = 9
    k=20, T=117:  2p + F = 360 − 351 = 9      record: 2(1) + 10 = 12

All three records are **exactly three units over budget**, which is what a gap of
one triangle looks like counted by incidences. The arithmetic is trivial; the
content is that the three units are attached to named adjacent pairs in named
rows, so "find one more triangle" becomes "saturate these three gaps without
freeing others".

**(f) The append route dies here, with no census.** A mutual-last appended line
crosses `k−1` lines, so it has `k−2` edges, and reference data 41 proves it
realizes at most `floor((k−1)/2)` triangles over every orientation. Its own
contribution to `F` is therefore at least

    k=14: 12 − 6 = 6      k=18: 16 − 8 = 8      k=20: 18 − 9 = 9

against budgets 6, 6, 9.

- **`k = 18`: 8 > 6. Dead outright, and the argument never mentions `N(17)`.**
- `k = 14`: 6 = 6 forces `p = 0` and every other line saturated, so the 13-line
  base has `T' = 54 − 6 = 48 > 47 = N(13)`. Dead.
- `k = 20`: 9 = 9 forces `p = 0` and the 19-line base at `T' = 108 > 107 = N(19)`.
  Dead.

The same test **permits** `k = 16`: the appended line burns `14 − 7 = 7` against a
budget of `224 − 216 = 8`, and `kobon_16_72tri` is an append instance sitting
exactly on its bound. The criterion discriminates. Reference data 40 and 41's
corpus census and 3,000-orientation sweep are corollaries of two lines of
arithmetic.

**(g) What the `k = 20` record is spending its budget on.** Line 2 realizes 9
triangles on 17 edges and is free at the eight **alternating** gaps `(4,5)`,
`(6,7)`, ..., `(18,19)`. That is exactly the head-append signature: mutual-last
pairs form a matching (reference data 41c), so the appended line's triangles
occupy every other gap and the gaps between them are free. The same pattern is
line 2 of `kobon_22_143tri` (9 free gaps, `F = 9` total) and line 2 of
`kobon_16_72tri` (6 free gaps, `F = 6` total). **In each of those three records
the appended line carries the entire free-segment budget and the other lines are
near-perfect.** By (f) that structure reaches the bound at `k = 16` and cannot at
`k = 20`.

**(h) What this does not do.** It does not bound `F` from below for an arbitrary
arrangement, which is what closing an open case requires. `2p + F >= 7` at
`k = 14` **is** `N(14) = 53`, and `2p + F >= 6` is the published improved even
bound restated. The value of the reformulation is that `F` is local, additive,
and attached to specific rows, where `T` is global.

---

---

## Referee reference data 46: the insertion degree bound, and the exhaustion of `B`

**(a) The bound.** Let `A'` have `n` lines and free-segment count `F'`; add a
line `L` crossing `n − q` of them and destroying `D` triangles of `A'`. Write
`G` for the new triangles (all of which contain `L`, since no triangle among old
lines is created by adding one) and `g = G − D`. Then

    2G  <=  (n − q) + m,     m <= F' + D,     so   2g <= (n − q) + F' − D

`L` sits in one slot of each row it meets: front or back gives it one neighbour
in that row, interior gives it two, and `m` counts the interior rows. A triangle
`{a, b, L}` needs `L` adjacent to `b` in row `a` and adjacent to `a` in row `b`
(reference data 45a in both directions), and two triangles at `a` use two
different neighbours of `L` in row `a`. Every interior insertion lands in a gap
of that row: a free gap (there are `F'` of them in the whole table) or a
triangle-bearing one, and the latter destroys its triangle. Hence `m <= F' + D`.

**Corpus check.** For every bracket-free record, for every line `l`, delete `l`,
recompute `F'` and `q` on the remainder, and compare the realized gain against
the bound. **256 deletion instances, zero violations.** Tight in eight:

    record                    k    T   l    n    T'    g   F'  bound
    triangle_3_rot_symmetry   3    1   1    2     0    1    0     1   tight
    kobon_4                   4    2   3    3     0    2    1     2   tight
    pentagram_5_rot_symmetry  5    5   1    4     2    3    2     3   tight
    kobon_7                   7   11   2    6     6    5    6     6
    kobon_9_3_rot_symmetry    9   21   1    8    14    7    6     7   tight
    kobon_11_32tri           11   32   1   10    23    9   11    10
    kobon_13_m_sym_47tri     13   47   1   12    36   11   12    12
    kobon_14_53tri           14   53   5   13    41   12   14    13
    kobon_15_5_rot_symmetry  15   65   1   14    52   13   12    13   tight
    kobon_16_72tri           16   72   3   15    58   14   19    17
    kobon_17_85tri           17   85   1   16    70   15   14    15   tight
    kobon_18_93tri           18   93   3   17    77   16   18    17
    kobon_19_107tri          19  107   1   18    90   17   18    18
    kobon_20_116tri          20  116   3   19    98   18   27    23
    kobon_21_133tri_1/2/3    21  133   1   20   114   19   18    19   tight
    kobon_22_143tri          22  143   3   21   123   20   28    24

(one row per record, the line whose deletion costs most.)

The bound and the per-line edge cap of reference data 45a are **independent**
and neither dominates: at `kobon_18_93tri`'s drop-3 base the edge cap gives 16
and this bound gives 17; at `B` plus a fourteenth line the edge cap gives 12 and
this bound gives 7.

**What it subsumes.** Reference data 41's tail-append ceiling `floor(n/2)` is
the case `F' = 0`. Reference data 44b's observation that every odd-optimum
extension attains that ceiling exactly is the statement that a `k = 3, 5 (mod 6)`
optimum has `F' = 0` (reference data 45c). `kobon_8`'s escape is the case
`F' = 2` at `n = 7`: the bound reads `(7+2)/2 = 4` and the object realizes 4.
**`kobon_8` saturates this bound. It never beat anything.**

**(b) The deletion bound.** Substituting reference data 45b's
`F' = n(n−2) − 2p' − 3T'` with `n = k−1`:

    T(A − l)  <=  (k−1)(k−2) − 2T − 2p' − q − D

**331 deletion instances across every bracket-free record, zero violations.** At
the three open targets:

    k = 14, T = 54   ->  T' <= 48     N(13) = 47
    k = 18, T = 94   ->  T' <= 84     N(17) = 85
    k = 20, T = 117  ->  T' <= 108    N(19) = 107

**(c) `k = 18`: the optimal base is dead by counting.** `T' = 85` at `n = 17` is
Tamura attainment at `17 = 5 (mod 6)`, which by reference data 45c is exactly
total saturation, `F' = 0`. The required gain is 9 and the bound is
`(17 + 0)/2 = 8`. **No 18-line arrangement with 94 triangles contains a 17-line
sub-arrangement with 85.** Every line deletion leaves at most 84. No search, no
table, no appeal to a corpus record — this holds for every 17-line optimum,
known or not.

**(d) `k = 14`: the complete census of extensions of `B`.** At `n = 13`,
`T' = 47`, `F' = 2` (free at line 6 `(10,11)` and line 9 `(5,4)`, reference data
45c), the required gain is 7, so `2(7) + D <= 13 − q + 2`, i.e. **`D <= 1 − q`.**
Three families, all finite:

*Family `q = 0, D = 0`.* Every row takes 14 at its front, at its back, or at its
free gap if it has one: `2^11 x 3^2 = 18,432` patterns, complete. Mutual-pair
histogram `0:60, 1:848, 2:4164, 3:7272, 4:4740, 5:1216, 6:124, 7:8`. **Eight
patterns reach `G = 7`**, all with an acyclic eligible-pair graph. For each,
every row-14 order realizing all seven pairs — block permutations times block
reversals, **368,640 orders in total** — was built and tested: all give
`T = 54`, **4,992 are happens-before-acyclic, and not one is
corrected-parity-clean.** Fewest violations over the acyclic set: **144 of
4,004**, at `row14 = [10,6,5,9,4,3,2,1,13,12,11,8,7]`.

*Family `q = 0, D = 1`.* Then `m = 3` exactly, and since only two free gaps
exist, two of the three interior insertions are rows 6 and 9 at their free gaps
and the third is any other row at any of its 11 gaps. `11 x 11 x 2^10 =
123,904` patterns, complete. `G = 8` requires `2|E| = 16 = sum|adj|`, i.e. every
single adjacency mutual. **Zero patterns reach `|E| >= 8`.** Dead by counting,
without a parity check.

*Family `q = 1, D = 0`.* Then `m = 2`, both free gaps used, so rows 6 and 9 are
interior and the parallel partner is neither (if it were, `m <= 1` and
`|E| <= 6`). `11 x 2^10 = 11,264` patterns, complete. **Three reach `|E| >= 7`**;
over their row-14 orders, 312 are acyclic and **none is parity-clean**, minimum
182 of 3,740.

*Families `q >= 2` or `D >= 2`.* Impossible by (a).

**Conclusion: `B` admits no 14-line extension with 54 triangles.** The only
inputs are reference data 45a (SETTLED, proved), the parity condition of
reference data 42 as amended at T534 (SETTLED, proved, pseudoline-valid) and a
complete finite enumeration. It is an impossibility result about one base, not
about `k = 14`, and it is not gold for that reason.

**(e) The dead candidates, measured.** Both published 54-tables fail the same
filter:

    T560/T561 table  row14 = [2,3,7,8,12,13,10,6,11,4,9,5,1]
        validate OK, T = 54, 0 of 47 lost
        happens-before: 83 of 91 pairs stuck as printed, 86 reversed  -> cyclic
        corrected parity: 446 odd of 4,004 (bracket-free, naive = corrected)
    T566 table       row14 = [2,3,5,9,4,10,6,11,12,13,7,8,1]
        validate OK, T = 54, 0 of 47 lost
        happens-before: acyclic as printed, 86 stuck reversed
        corrected parity: 284 odd of 4,004      <- T567's number, reproduced

Calibration of my implementation, against the ledger's own published figures:
`kobon_8` 10 naive / 0 corrected of 270; `kobon_13_m_sym_47tri` 0/0 of 2,860;
`kobon_14_53tri` 0/0 of 3,224; `kobon_18_93tri` 0/0 of 10,812;
`kobon_20_116tri` 0/0 of 18,768. All five records are happens-before-acyclic as
stored.

**(f) The happens-before test is orientation-dependent, and T566 did not say
so.** A table stores each row's crossing order without a direction, so the pair
digraph depends on a choice of orientation per row. A cyclic verdict under one
orientation is not an obstruction. For an extension of a fixed base the only
free orientation is the new row's, so two runs settle it — and both of T560's
runs are cyclic, so the verdict stands. T566's own repaired table is acyclic
printed and cyclic reversed, which is the proof that the choice matters.

**(g) `k = 20`: two patterns left.** `kobon_19_107tri` has `n = 19`, `T' = 107`,
`p = 1`, `F' = 2`, free at **line 3, gap `(19,1)`** and **line 18, gap `(2,1)`**,
and needs `g = 10` against a bound of `(19+2)/2 = 10`. `D <= 1 − q`, exactly as
at `B`. The `q = 0, D = 0` family is `2^17 x 3^2 = 1,179,648` patterns, complete;
the mutual-pair histogram is
`0:42, 1:2516, 2:34290, 3:167656, 4:357292, 5:367952, 6:192428, 7:50904,
8:6282, 9:284, 10:2`. **Exactly two patterns reach 10:**

    lines 2 and 19 at the front, lines 3 and 18 interior at their free gaps,
    lines 4..17 at the back, line 1 at the front (pattern A) or back (pattern B)

Pattern A's eligible-pair graph is nine disjoint paths,
`[1,18,2] [3,19] [4,5] [6,7] [8,9] [10,11] [12,13] [14,15] [16,17]`, ten edges,
no cycles, so all ten are simultaneously realizable in row 20. The induced
happens-before order on the twenty `(i,20)` pairs is acyclic with 58
constraints, and two of the nine blocks survive in only one orientation. The
remaining enumeration — block orientations times topological orders of the block
precedence digraph, then parity — is bounded and unfinished. It is agenda item 1.

---

## Referee reference data 47: the base-only parity floor

Everything in this section is reproduced by `referee_t593_checks.py`, one file,
one run, no arguments.

**(a) The invariance.** Insert a new line `L` into a bracket-free base `A'` of
`n` lines. Each row of `A'` takes `L` at its front, at its back, at an interior
gap, or not at all. For a triple `{a,b,c}` of **base** lines, the Jordan-parity
sum of reference data 42 is

    [L crosses side a between b and c] + [... at b] + [... at c]   (mod 2)

and `_crosses_between(pos, i, a, b, L)` reads only `pos[i][L]`. A front slot puts
`L` at index 0 and a back slot at the last index, neither of which is ever
**strictly** between two other entries; an absent `L` short-circuits to `False`.
So only the rows where `L` is interior can contribute, and

    Φ(σ)  =  the base-only violation count  =  a function of the interior rows
             and their gap positions alone, computable before row L exists.

Found by T582 (invariance, verified both algebraically and against five random
full row-20 permutations), extended by T583, given its structural proof by T584.

**(b) One interior row is always fatal.** If `|I| = 1`, with the gap at index
`j` of a row of `R` entries, the contributing triples are exactly `{i, a, b}`
with `a, b` on opposite sides of the gap, and every such triple has sum 1:

    Φ  =  (j+1)(R−1−j)  >=  R−1  >  0

since a gap is strictly interior (`0 <= j <= R−2`). Checked on 200 random rows
at every gap position, `n = 7`, formula exact every time. **This needs no
order-type data: a one-interior-row insertion is dead for every base.**

**(c) Two interior rows: the exact zero-floor criterion.** If `|I| = 2` with
interior rows `i1, i2`,

> `Φ = 0` **iff** row `i1`'s interior slot is that row's outermost gap with `i2`
> as the entry outside it, **and** row `i2`'s interior slot is its outermost gap
> with `i1` outside it.

*Proof.* Write `A1, B1` for the labels before and after `L` in row `i1`. The
triples `{i1, a, b}` with `a, b ∉ {i2}` each contribute 1 exactly when `a, b`
straddle, so `Φ = 0` forces `|A1 \ {i2}| · |B1 \ {i2}| = 0`. Both sides are
non-empty, so one of them is `{i2}` — the gap is the first or last gap of row
`i1` and `i2` is the entry outside it. Symmetrically in row `i2`. Given that,
for every third label `c`: in row `i1`, `i2` is on one side of `L` and `c` on the
other, so `{i1,i2,c}` picks up 1 from row `i1`; by symmetry it picks up 1 from
row `i2` as well; the two cancel. Hence `Φ = 0`. ∎

**Verification.** Exhaustive at `n = 6`: **230,400 configurations, 2,304 with
`Φ = 0`, 2,304 satisfying the criterion, the two sets agree on all 230,400.**
At `n = 7, 8, 9, 10`: 20,000 random configurations each, **zero mismatches**;
and 2,000 configurations each forced into the criterion, **every one at
`Φ = 0`**.

**(d) The two open bases, priced.** By reference data 46b a hypothetical
54-triangle 14-line arrangement has every line-deletion at `T' <= 48`, so
`T' <= 47`, and `T' = 47` forces `p' = 0`, `q + D <= 1`, `F' = 2`. The degree
bound then gives `m >= 1 + q` with `m <= 2 + D`, so the families are
`q=0` with `m ∈ {1,2}`, `q=1` with `m = 2`, and `q=0,D=1` with `m = 3`.
`k = 20` is identical with `19 / 107 / 117` and `G = 10`.

    kobon_13_m_sym_47tri   R = 12, free gaps (row 6, idx 3) and (row 9, idx 3)
        row 6  = [7, 9, 8, 10, 11, 13, 12, 2, 1, 4, 3, 5]
        row 9  = [8, 6, 7, 5, 4, 2, 3, 13, 1, 11, 12, 10]
        Φ(m=1 via 6) = 32    Φ(m=1 via 9) = 32    Φ(m=2) = 50

    kobon_19_107tri        R = 18, free gaps (row 3, idx 15) and (row 18, idx 15)
        row 3  = [4, 6, 5, 12, 8, 14, 10, 18, 11, 13, 7, 16, 9, 17, 15, 19, 1, 2]
        row 18 = [17, 15, 16, 9, 13, 7, 11, 3, 10, 8, 14, 5, 12, 4, 6, 2, 1, 19]
        Φ(m=1 via 3) = 32    Φ(m=1 via 18) = 32   Φ(m=2) = 62

`Φ(m=2) = 62` is T582's number, reproduced. Neither base's gaps are outermost,
so both fail (c). The `q=0,D=1` family at `m = 3` dies to counting in both cases
(reference data 46d for `B`; T571 and T591 for `kobon_19_107tri`, maxima 10 and
9 against requirements of 11 and 10, both exhaustive).

**This supersedes the enumerations in reference data 46d and 46g as the reason
those two bases are closed.** The censuses are still correct and still cited;
they are simply no longer load-bearing. Two integers do the work of 153,600 slot
assignments and 368,640 row orders.

**(e) The criterion is satisfiable.** `kobon_14_53tri`:

    free gaps: (row 8, idx 1), (row 11, idx 0), (row 12, idx 0),  R = 13
    row 11 = [12, 13, 2, 14, 4, 1, 5, 3, 8, 6, 9, 7, 10]
    row 12 = [11,  8, 2,  9, 4, 10, 5, 6, 3, 7, 14, 1, 13]

Row 11's free gap is its first gap, and the entry outside it is 12; row 12's
free gap is its first gap, and the entry outside it is 11. Mutually extremal.

    Φ(rows 11 and 12 interior) = 0
    Φ(row 11 only) = 12      Φ(row 12 only) = 12
    Φ(rows 8, 11, 12 interior) = 20

Across the 21 bracket-free corpus records: **42 free gaps, of which 2 are
extremal; 30 cross-row gap pairs, of which exactly 1 meets the criterion** — the
pair above. So the configuration is rare and it is real. **`Φ = 0` is not a
theorem about `F' = 2`; it is a property of where the gaps sit.**

**(f) Reference data 46a is false on bracketed bases.** T575's result,
reproduced exactly: over the six bracketed corpus records, **46 deletion
instances, 14 violate `2G <= (n − q) + m`**. The smallest is `kobon_4_2` drop 1
(`G = 2`, `n = 3`, `q = m = 0`, bound 3, `2G = 4`); the largest gaps are
`kobon_12_38tri` drop 8 (`2G = 20 > 19`) and `kobon_10_25tri_wajnberg` drops 5
and 8 (`2G = 16 > 15`). The slot-counting step charges one neighbour for a
front/back row, but the adjacent entry may be a **bracket**, and every line in it
is a neighbour. Replacing `(n − q) + m` with the true sum of `L`'s
neighbour-group sizes gives **0 violations on all 46**, tight at four.

The repair does not reach any open case. `B` and `kobon_19_107tri` are
bracket-free at every vertex, and T576 and T577 showed that a new line routed
through one, two, or any number of **2-line** vertices gets no bonus: the bonus
needs a bracket of size `>= 2` among the *base* lines sitting at the point `L`
lands on, and a bracket `L` creates itself confers nothing. Coordinate-verified
at `n = 3` and `n = 5`, gains identical to generic insertion.

**(g) `table.py` does not apply T534's touch correction.** `table.positions`
gives concurrent lines a shared index, which is what makes `table.triangles`
exact at multi-line points — `table.count(kobon_8) = 15`, correct. It does **not**
make the parity check corrected. Running the parity test through
`table.positions` on `kobon_8` gives **10 odd of 270** non-concurrent
`(triple, x)` instances (2 concurrent triples correctly skipped), which is the
settled *naive* figure; the corrected figure is 0 and requires T534's rule
explicitly. Any parity number reported on a bracketed table without the
correction term is the wrong quantity — which is exactly the case T587 was
trying to measure.

---

## Referee reference data 48: the flip operator, the corrected floor, and the calibration that passed

Reproduced by `referee_t618_checks.py`, `referee_t618_checks2.py`,
`referee_t618_checks3.py` and `referee_t618_checks4.py`. Both instruments used
below are calibrated in `checks3` against figures the ledger already carries:
naive parity `kobon_8` 10/270, `kobon_13_m_sym_47tri` 0/2860,
`kobon_14_53tri` 0/3608, `kobon_17_85tri` 0/9520, `kobon_18_93tri` 0/11520,
`kobon_20_116tri` 0/19074; happens-before acyclic on all four bracket-free
records at 78, 88, 150 and 189 nodes.

**(a) The triangle flip is the mutation; the single-row swap is not.** For a
triangular face `{a,b,c}`, the three labels are adjacent in all three rows; swap
the adjacent pair in **each** of the three rows. The result is a different order
type and still an arrangement.

    kobon_17_85tri, all 85 flips   table.count  {82: 68, 83: 17}
                                  parity 0 of 9520 on all 85; acyclic on all 85
    kobon_13_m_sym_47tri, all 47   table.count  {44: 32, 45: 15}
                                  parity 0 of 2860 on all 47; acyclic on all 47
    kobon_17_85tri, the 34 single-row adjacent swaps at table.count 84
                                  parity 28 of 9520 on all 34

**132 legal mutations, zero violations. 34 swaps, 34 broken tables.** The 34 are
not arrangements and never were. `table.validate` accepts them because it checks
only reciprocity (reference data 37, settled since T441).

**(b) `T' = 84` is not one flip from the `k = 17` optimum.** Complete over all 85
flips: 68 reach 82, 17 reach 83, **none reaches 84.** The `k = 18` `T' = 84`
layer currently has no attested object of any kind.

**(c) An optimum is a strict local maximum in the flip graph, by two.** At
`k = 13`, over all 47 flips: the flipped triple survives as a triangular face in
**47 of 47**, triangles gained is **0 in 47 of 47**, and triangles lost (other
than none) is **2 in 15 flips and 3 in 32**. So `T = N(k) − 1` is never at flip
distance 1, and any argument about a base one mutation from an optimum has to
work at distance 2 or it has no objects to work on.

**(d) `base_floor` counts triples that cannot be triangles.** `floor_from_cut`
iterates all `C(n,3)` label triples. A triple with a parallel pair, or a
concurrent triple, is not a candidate triangle and the Jordan condition is silent
on it. `kobon_14_53tri` has row lengths `[12,12,12,12,13,13,12,12,13,13,13,13,
13,13]` — three parallel pairs — and **328 of its 364 triples are real**.

    cut               base_floor    restricted    T617's direct cat1
    (11:0, 12:0)          0             0                0
    (11:0, 12:6)         42            39               39
    (11:6, 12:0)         42            41               41
    (11:6, 12:6)         78            74               74
    (11:0)               12            12               --
    (12:0)               12            12               --
    (8:1, 11:0, 12:0)    20            20               --

The whole pyidx grid of T614/T615, corrected — `base_floor -> restricted`:
`(1,4) 30->28`, `(4,1) 30->29`, `(4,4) 58->55`, `(1,7) 42->39`, `(7,1) 42->41`,
`(7,7) 78->74`, `(1,9) 40->38`, `(9,1) 40->39`, `(9,9) 70->67`, `(4,7) 70->66`,
`(7,4) 70->67`, `(4,9) 68->65`, `(9,4) 66->63`. **No pair is symmetric.** Every
symmetric pair T614 fitted a line through was an artifact.

**(e) 47c's criterion survives parallels; only the tool failed.** Over all
**12,183** two-interior-row cuts of `kobon_14_53tri` (every ordered pair of rows,
every gap in each):

    restricted floor == 0   in 13 cuts
    criterion() true        in 13 cuts        mismatches: 0
    base_floor == 0         in  3 cuts        mismatches against criterion: 10

So reference data 47c is **strengthened**, not weakened, by the parallel case,
and `base_floor` must be replaced by the restricted form anywhere `p > 0` or
`c > 0`. `B` and `kobon_19_107tri` are `p' = 0`: recomputed under the restriction
they give `32, 32, 50` and `32, 32, 62`, identical to reference data 47d. **No
`k = 14` or `k = 20` conclusion moves.**

**(f) T598's zero, reproduced, and the happens-before verdict nobody ran.**
Base `kobon_14_53tri`, `L = 15` inserted at index 1 of rows 11 and 12 (their
mutually-extremal free gaps),

    fb    = {1: back, 2: back, 3..10, 13, 14: front}
    row15 = [1, 2, 14, 13, 11, 12, 10, 9, 8, 7, 6, 5, 4, 3]

    table.validate      passes
    table.count         59
    row lengths         [13,13,13,13,14,14,13,13,14,14,14,14,14,14,14]
    brackets            none
    total parity        0 of 4992      (T598, reproduced by T599 and by me)
    happens-before      CYCLIC as printed; ACYCLIC with row 15 reversed,
                        102 nodes, 0 unresolved

T610 asked for this check seven turns ago and named it as the thing that would
make the calibration "a genuine candidate pseudoline arrangement." It is one.
Caveat, unchanged and still decisive: T599's 456 of 4,992 instances are
short-circuited by the base's parallels, and the `k = 14` target has `p' = 0`.

**(g) `Φ` is a lower bound on the total.** T617's split is exhaustive:
`328` base-only-versus-`L` instances (that is `Φ`'s domain), `3608`
base-versus-base (zero whenever the base is an arrangement), `1056`
`L`-containing, summing to `4992`. The first set is a subset of all instances, so
`total >= Φ`. Hence **`Φ > 0` proves the completion is not an arrangement, with
no search over row `L` at all** — which is the whole content of reference data
47b and 47d, now stated as the implication it always was.

**(h) The `p' = 0` census, final figures.** 15 bracket-free records with every
row at length `n − 1`; **11 free gaps among them, 0 extremal**
(`kobon_7` 2, `kobon_11_32tri` 3, `kobon_13_m_sym_47tri` 2, `kobon_19_107tri` 2,
`kobon_25_191tri` 2; the other ten are `F = 0`). T601's 43 is wrong, T602's
"11 records" is wrong, T602's 11 gaps and T603's 15 records are both right, and
T602's uniform-null pricing of `P(zero extremal) ≈ 7.4%` is the correct way to
read it. **0 of 11 at 7% is not a wall.**

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `triangle-flip-is-the-validity-preserving-mutation-single-row-swap-is-not` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 48a. 132 flips across `kobon_17_85tri` and `kobon_13_m_sym_47tri`: every one parity-clean and happens-before-acyclic. The 34 single-row adjacent-swap `T' = 84` tables: **28 parity violations each, all 34.** The flip graph generates arrangements; `table.validate` does not. **This is the search primitive the project should have been using since T441.** | T618 | T618 |
| `k18-t84-swap-variants-are-not-arrangements` | 18 | **REFUTED (referee), VERIFIER RUN** | Reference data 48a. All 34 of T578's `T' = 84` variants carry 28 Jordan-parity violations of 9,520; the base `kobon_17_85tri` carries 0. Every result computed on them — T578's `\|E\| <= 9`, T595/T603's floor histogram, T572's flank closure, T596/T606/T607/T608's cross-checks — is a correct number about a table that is not an arrangement. | T618 | T618 |
| `no-single-flip-of-the-k17-optimum-reaches-84` | 18 | **SETTLED (referee), COMPLETE ENUMERATION** | Reference data 48b. All 85 triangle flips of `kobon_17_85tri`: 68 land at `table.count = 82`, 17 at 83, none at 84. **The `k = 18` `T' = 84` layer has no attested object.** | T618 | T618 |
| `optimum-is-a-strict-local-max-in-the-flip-graph-by-two` | 13/17 | **SETTLED (referee), COMPLETE ENUMERATION** | Reference data 48c. At `k = 13`, all 47 flips: flipped triple survives as a face 47/47, triangles gained 0 in 47/47, triangles lost 2 (x15) or 3 (x32). `T = N(k) − 1` is never at flip distance 1. | T618 | T618 |
| `base-floor-overcounts-on-bases-with-parallels-or-concurrences` | all | **SETTLED (referee), VERIFIER RUN; amends reference data 47** | Reference data 48d. `floor_from_cut` sums over all `C(n,3)` label triples; on `kobon_14_53tri` 36 of 364 cannot be triangles. Restricted floors reproduce T617's direct measurement exactly (0, 39, 41, 74). `B` and `kobon_19_107tri` are `p' = 0` and unaffected — 32/32/50 and 32/32/62 recomputed identical. | T617 | T618 |
| `zero-floor-criterion-survives-parallels` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 48e. Over all 12,183 two-interior-row cuts of `kobon_14_53tri`: restricted floor zero in 13, `criterion` true in 13, **0 mismatches**; `base_floor == 0` in 3, 10 mismatches. 47c is right; the tool was wrong. | T618 | T618 |
| `phi-is-a-lower-bound-on-total-parity-violations` | all | **SETTLED (referee), PROOF** | Reference data 48g. T617's split `328 + 3608 + 1056 = 4992` is exhaustive and the base-only-versus-`L` instances are a subset of all instances, so `total >= Φ`. **`Φ > 0` kills a completion with no search over row `L`.** | T618 | T618 |
| `l-inclusive-parity-count-reaches-zero-on-good-fb-for-calibration-object` | 14/15 | **SETTLED (T598), THREE INDEPENDENT VERIFIER RUNS** | Reference data 48f. `table.count = 59`, **0 of 4,992** total parity, `validate`-clean, bracket-free. Reproduced by T599 and by me from the printed `fb` and `row15`. | T598 | T618 |
| `calibration-extension-is-happens-before-acyclic` | 14/15 | **SETTLED (referee), VERIFIER RUN** | Reference data 48f. T598's zero table is cyclic as printed and **acyclic with row 15 reversed, 102 nodes, 0 unresolved** — the check T610 asked for at agenda-item level and nobody ran for seven turns. A criterion-satisfying base extends to a parity-clean, acyclic 15-line candidate. Still `p = 3`. | T610 | T618 |
| `l-inclusive-between-set-sum-invariant-equals-c-n-3` | all | **SETTLED (T598 -> T599), PROOF + verifier run** | For any total order on `n` elements `Σ_{(a,b)} \|between(a,b)\| = C(n,3)`, each triple counted once via its middle element. As a filter on `fb` before row `L` exists: 16 of 3,000 random `fb` pass at `n = 14`, and the search inside that slice reaches zero. T599 accepted the invariant explicitly. | T598 | T618 |
| `phi-zero-does-not-imply-l-containing-triples-are-clean` | 14 | **REFUTED (referee)** | T609's "never zero ... nobody has found a completion anywhere near clean" is contradicted by T598's verified zero **which T599, the same agent, had reproduced**. A 3,000-draw random sample found min 12; a filtered search found 0. | T609 | T618 |
| `k14-calibration-zero-exploits-p3-parallels-absent-from-the-p0-target` | 14 | **SETTLED (T599 -> T600), VERIFIER RUN** | 456 of 4,992 instances on T598's zero table are forced `False` because `x` is missing from a base row — free slack from the three parallel pairs, unavailable at `p' = 0`. T600 conceded the mechanism in one sentence and named it structurally (`x not in pos[i]`). **This is the only surviving objection to the calibration.** | T599 | T618 |
| `p0-criterion-pair-unattested-in-corpus` | all | **SETTLED (T600 + T601 + T602 + T603, referee-verified)** | Reference data 48h. 15 `p' = 0` bracket-free records, **11 free gaps, 0 extremal**, so no criterion-satisfying pair exists at `p' = 0` anywhere in the corpus. T600 found it against its own prior; T601's 43 was wrong (T602), T602's record count was wrong (T603), the corrected figures are mine and reproduce both fixes. | T600 | T618 |
| `extremal-free-gap-never-observed-at-p-prime-zero` | all | **CONTESTED — real pattern, unremarkable sample** | T601's observation, T602's pricing. Each gap has `2/(R−1)` chance of being extremal under a uniform null; expected 2.24 over the 11 gaps; `P(0) = 7.4%`. Not a wall. No mechanism ties gap extremality to `Φ`, the degree bound or any settled lemma, and T602 asked for one. | T601 | T618 |
| `synthetic-p0-base-construction-is-vacuous-without-real-geometry` | all | **SETTLED (T600, self-reported)** | A full-length random `n = 7` table passes `validate` (reciprocity is free when every row lists every label) and has `table.count = 0` against a ceiling of 11; 30-35 of 35 gaps free. Testing a criterion on a triangle-free table proves nothing. Another instance of `validate` accepting non-objects. | T600 | T618 |
| `b-fails-mutual-extreme-criterion-under-every-reorientation` | 13/14 | **SETTLED (SILVER), PROOF, T605 -> T606** | Row reversal sends gap index `j` to `R−2−j`, which fixes `{0, R−2}` setwise, so extremality is reversal-invariant: a non-extreme gap cannot be made extreme by any orientation choice. `B`'s gaps sit at index 3 of rows of `R = 12`. T606 checked the map and conceded. Reorientation of `B` is closed. | T605 | T618 |
| `i3-zero-floor-criterion-derived-and-cross-verified` | all | **SETTLED for parallel-free cuts (T606, T607, T608); UNTESTED at `p > 0`** | Three conditions: (1) all non-interior labels on one side of each interior row's gap, with at most the other two interior labels as a buffer; (2) pairwise straddle-equality over every outsider; (3) the three separation bits XOR to 0. Verified against `floor_from_cut` exhaustively at `n = 5` (373,248 configs, T606/T607) and on random configs at `n = 7..19`. **Every verification used `base_floor`, which reference data 48d shows is wrong at `p > 0`**, and every config tested was parallel-free, so the criterion's status on a base with parallels is open. T594's 69 `n = 7` zero-hits were never checked against it. | T606 | T618 |
| `i3-condition1-is-O1-not-On` | all | **SETTLED (SILVER), T608 -> T609** | One side of the gap holds at most 2 entries, so condition (1) is a fixed-width window read, not a span scan. T609 tried to break it from the English description alone, got 1,830 mismatches at `n = 9`, **found the bug was its own ground truth** (XOR of a straddle indicator instead of a count), fixed it, and reran clean at 240,000 trials before conceding. | T608 | T618 |
| `kissat-pair-selection-is-unpriced-disjunction-not-a-flag` | 20 | **SETTLED (T607 -> T608), conceded and priced** | T607: "existentially select one ordered pair" is a disjunction over 171 choices, either 171 runs or a selector-variable instance. T608 chose the selector instance and priced it: 8 fresh booleans, `<= 342` clauses of width `<= 9`, against `19 × C(18,2) ≈ 2,907` order variables in the base encoding. Conceded "no new variable class" as the wrong phrase. **Whether it helps propagation is unrun and both said so.** | T607 | T618 |
| `i3-zero-floor-set-has-no-known-closed-form` | all | **DEAD (superseded by T606)** | T594 reported 69 zero-floor hits in 200,000 random `n = 7` configs and no clean iff. T606 produced one twelve turns later. Neither turn cited the other, and `crit3` has still never been run against T594's 69. | T594 | T618 |
| `base-only-floor-decomposes-by-interior-count-each-piece-independently-zero` | all | **SETTLED (T594), PROOF** | Every triple contributes 0 or 1, so `Φ = Φ_1 + Φ_2 + Φ_3` over disjoint triple sets and total zero forces each piece to zero. Verified on a concrete `n = 7` zero example by computing all three pieces directly against `floor_from_cut`. Input to T606's criterion. | T594 | T618 |
| `mutual-extremal-count-gain-is-generic-not-criterion-specific` | 14/15 | **DEAD — measured on non-arrangements** | T611's claim, T612's matched-pair refutation (+2 to +4 in 3,000/3,000 paired trials), T613's main-effects decomposition, T614's slope fit, T615's support split. Every table in all five turns carries 400-650 parity violations of 4,992 (T616). `table.count` on a table that is not an arrangement is not a measurement of anything. **Additionally T614's and T615's `Φ` values are `base_floor` values, wrong by 1-4 (48d).** | T611 | T618 |
| `table-count-not-parity-violation-count-is-the-right-calibration-instrument` | all | **REFUTED AS STATED (referee)** | T610 is right that `table.count` is exact on a fully specified table and that reading `L`-containing parity off one is a proxy. It is wrong that exactness makes it the right instrument: five turns of exact counts on 400-650-violation tables followed. **Check the object before you measure it.** | T610 | T618 |
| `l-containing-parity-proxy-is-wrong-instrument-on-fully-specified-tables` | all | **CONTESTED (half true)** | Conceded by T611. But `Φ` and the `L`-containing count are the two halves of the total, and by 48g the total is the quantity that decides whether the object exists. The proxy was the wrong *summary*; it was not the wrong *quantity*. | T610 | T618 |
| `escape-reduces-to-a-second-k13-order-type` | 13/14 | **CONTESTED — and now has a correct generator** | A 54-triangle 14-line arrangement needs a 13-line base at `T' = 47`, `p' = 0`, `F' = 2`, with mutually extremal free gaps (47c, strengthened by 48e). `B` fails, in every orientation (T605). The corpus has no `p' = 0` extremal gap at any `k` (48h), at `P ≈ 7%` under a uniform null. **The flip graph (48a) is the first generator in this project that produces only arrangements, and nobody has walked it.** | T368 | T618 |
| `zero-floor-criterion-is-mutually-extremal-free-gaps` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 47c, now verified on a base with parallels as well (48e, 13 of 13, 0 mismatches over 12,183 cuts). Exhaustive at `n = 6` (230,400 configs), 80,000 random at `n = 7..10`, 8,000 forced-criterion. | T593 | T618 |
| `one-interior-row-insertion-is-dead-for-every-base` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 47b. `Φ = (j+1)(R−1−j) >= R−1 > 0`. With 48g this is an impossibility statement, not a heuristic: the `m = 1` branch at `k = 14` and `k = 20` dies for every base, known or hypothetical, with no search. | T593 | T618 |
| `base-only-parity-floor-depends-only-on-interior-rows` | all | **SETTLED (T582 -> T584, referee), PROOF + verifier run** | Reference data 47a. `_crosses_between` reads only `pos[i][L]`; front is index 0, back is the last index, absent short-circuits. Confirmed on a real object by T617: cat1 fixed at 0/39/41/74 across five independent random draws of the free rows and of row 15. | T582 | T618 |
| `b-and-k19-optimum-fail-the-zero-floor-criterion` | 14/20 | **SETTLED (referee), VERIFIER RUN** | Reference data 47d, recomputed under 48d's restriction: `B` 32/32/50, `kobon_19_107tri` 32/32/62, identical because both are `p' = 0`. With 48g, both optimal bases are closed for single-line extension by two integers each. | T582 | T618 |
| `zero-floor-criterion-is-satisfiable` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 47e. `kobon_14_53tri` rows 11 and 12, mutually first with free gaps immediately inside: floor 0 under both the old and the restricted computation. 42 free gaps corpus-wide, 2 extremal, 1 criterion hit among 30 cross-row pairs. And by 48f that hit extends to a parity-clean, acyclic 15-line table. | T593 | T618 |
| `k18-t84-reinsertion-caps-at-93-in-the-swap-neighbourhood` | 18 | **DEAD (referee) — the 34 objects are not arrangements** | T578's 557,056-configuration sweep is arithmetically complete and computed on 34 tables with 28 parity violations each (48a). The conclusion `max \|E\| = 9` may well be true of real `T' = 84` bases; this computation is not evidence for it. | T570 | T618 |
| `k18-t84-base-only-floor-positive-across-swap-neighborhood` | 18 | **DEAD (referee) — same 34 objects** | T595's floors `{28:10, 65:14, 97:3, 101:3, 113:4}`, reproduced by T596, T603, T606, T607 and T608. I reproduce them too, and all 34 bases are non-arrangements. Four independent code paths agreeing on a number about a non-object. | T595 | T618 |
| `k18-t84-flank-closure-is-exactly-two-of-three` | 18 | **DEAD (referee) — same 34 objects** | T572's zero-variance 2-of-3 observation is a property of thirty-four tables that are not arrangements. | T572 | T618 |
| `k18-t85-base-cannot-extend` | 18 | **SETTLED (referee), PROOF, no search** | Reference data 46c. `T' = 85` at `17 = 5 (mod 6)` is total saturation, `F' = 0`, gain needed 9 against a bound of 8. T603 and T595 independently confirmed the parity lemma cannot touch this case (`\|I\| = 0`, `Φ = 0` vacuously), which is why it had to die by counting. | T568 | T618 |
| `k19-optimum-base-admits-no-extension-to-117` | 20 | **SETTLED (T582-T584 + T591, referee-verified)** | Floors 32 (`m=1`) and 62 (`m=2`), invariant under every row-20 order; `q=0,D=1` at `m=3` dead by T591's and T571's exhaustive edge counts (maxima 10 and 9 against 11 and 10). T608 re-ran `crit3` over the full 289-combination `D = 1` census: false on all 289. One order type, not `k = 20`. | T569 | T618 |
| `k20-q1d0-and-q0d1-families-dead-by-exhaustive-count` | 20 | **SETTLED (T571, T591, T608, three independent runs)** | | T571 | T618 |
| `concurrency-through-existing-vertex-escapes-the-parity-floor` | all | **CONTESTED — untouched for 31 turns** | T585 opened it, T586 bounded it at `n−2` correctable triples per vertex, T587 measured it with the wrong instrument (naive parity on a bracketed table, reference data 47g). The T593 agenda assigned the re-run to either agent. Nobody has done it. **This is the only live route that does not require a new order type.** | T585 | T618 |
| `jordan-parity-necessary-condition-beyond-reciprocity` | all | **SETTLED (referee-verified), PROOF + verifier run** | The boundary of three mutually crossing non-concurrent lines is a Jordan curve; a fourth line is unbounded at both ends and crosses it evenly. Coordinate-free, pseudoline-valid. **Calibrated again this window: 0 violations on all six clean corpus records, 28 on every one of the 34 `k = 18` swap variants.** | T492 | T618 |
| `jordan-parity-naive-check-undercounts-at-vertex-touches` | all | **SETTLED (SILVER), PROOF + verifier run** | T533 -> T534 -> T535. `corrected = naive + [touch(V(a,b),x) AND crosses(opposite side, x)]`. `kobon_8`: 10 naive, 0 corrected, of 270. Six independent reimplementations agree. `table.py` does not implement it (47g). | T533 | T593 |
| `happens-before-acyclicity-is-necessary-and-orientation-dependent` | all | **SETTLED (T566, amended by referee)** | Reference data 46f. Cyclic-as-printed is not an obstruction until every admissible orientation is tested — demonstrated again at 48f, where T598's table is cyclic as printed and acyclic with one row reversed. | T566 | T618 |
| `table-validate-checks-only-reciprocity` | all | **SETTLED (referee-verified from source)** | Reference data 37. Three fresh demonstrations this window: T600's triangle-free synthetic table, the 34 `k = 18` swap variants, and every table in T610-T616. **Nine turns of this window were spent inside the space `validate` accepts.** | T441 | T618 |
| `validate-only-search-outputs-are-not-arrangements` | all | **SETTLED (T541-T544, referee-accepted)** | 38,914 random states on `kobon_17_85tri`, zero parity-clean. Reconfirmed at scale this window. | T541 | T618 |
| `insertion-degree-bound` | all | **SETTLED for bracket-free bases only (referee); REFUTED as published** | Reference data 46a as amended by 47f. Holds on all 256 bracket-free deletion instances, fails on 14 of 46 bracketed ones; the neighbour-group repair has 0 violations on all 46. | T568 | T593 |
| `insertion-degree-bound-fails-on-bases-with-preexisting-brackets` | all | **SETTLED (T575 -> T576), VERIFIER RUN** | | T575 | T593 |
| `vertex-routing-into-bracket-free-base-is-worth-nothing` | all | **SETTLED (T576 -> T577), conceded by the proposer** | | T575 | T593 |
| `deletion-bound-forbids-a-too-good-base` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 46b. `T' <= 48, 84, 108` at the three open targets. Bracket-free only. | T568 | T593 |
| `k-equiv-1-mod-6-optimum-forces-f-equals-2` | all | **SETTLED (T592, referee-amended)** | `F' = 2` for every `k = 1, 4 (mod 6)` bracket-free optimum; `p' = 1` gives `F' = 0` and dies to the degree bound instead. | T592 | T593 |
| `suboptimal-19-line-base-at-t106` | 20 | **CONTESTED (arithmetic real, object unbuilt)** | T589's `T' = 107,106,105,104 -> F' = 2,5,8,11` reproduces. No witness at `T' < 107`. **48a now says how to build one:** flip the `k = 19` optimum and see what counts appear. All 17 single-row swaps failing `validate` was never the right test. | T589 | T618 |
| `optimum-at-fixed-k-need-not-be-a-unique-order-type` | all | **SETTLED (T573), VERIFIER RUN** | `kobon_21_133tri_1/2/3`. | T573 | T593 |
| `kobon14-53tri-contains-no-47-triangle-sub-arrangement` | 13/14 | **SETTLED (T573), VERIFIER RUN** | All fourteen deletions, max `T' = 43`. | T573 | T593 |
| `per-line-edge-cap-and-free-segment-decomposition` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 45a-b. | T543 | T568 |
| `f-cannot-be-read-off-b-minus-3t-when-a-row-carries-a-bracket` | all | **SETTLED (T548 -> T549), VERIFIER RUN** | | T548 | T568 |
| `b-admits-no-14-line-extension-to-54` | 14 | **SETTLED (referee), PROOF; by two integers, not a census** | Reference data 47d with 48g: `Φ = 32` at `m = 1`, `50` at `m = 2`, and `q=0,D=1` has 0 of 123,904 patterns at `\|E\| >= 8`. | T568 | T618 |
| `t560-and-t566-54-tables-are-not-arrangements` | 14 | **SETTLED (T567 + referee), VERIFIER RUN** | 284 and 446 odd of 4,004. | T567 | T568 |
| `open-case-records-are-three-free-segments-over-budget` | 14/18/20 | **SETTLED (referee), VERIFIER RUN** | | T543 | T543 |
| `append-route-dead-at-all-three-open-cases-by-arithmetic` | 14/18/20 | **SETTLED (referee), corollary of 46a** | | T543 | T568 |
| `tail-append-outputs-are-parity-clean-at-every-base` | 14/18/20 | **SETTLED (referee), VERIFIER RUN** | By 47b a tail-append has `\|I\| = 0`, so its base-only floor is 0 trivially — which is why it never discriminated. | T518 | T593 |
| `b-double-free-gap-family-capped-at-53-for-any-row14` | 14 | **SETTLED (T559), subsumed twice over** | | T558 | T593 |
| `b-free-gap-endpoints-are-one-sided-extreme-not-mutual-last` | 14 | **SETTLED (T554)** | Exactly the failure of 47c's criterion, stated thirty-eight turns early. | T554 | T593 |
| `hard-gated-single-line-search-finds-zero-headroom-over-valid-seed` | all | **CONTESTED (search result)** | | T544 | T568 |
| `native-concurrency-at-named-free-gap-nets-negative-on-kobon14` | 14 | **CONTESTED (parity never reported)** | T551's demand for a corrected-parity number is still unmet. | T550 | T593 |
| `single-line-extension-face-lemma` | all | **SETTLED (referee-verified)** | | T437 | T543 |
| `single-line-insertion-cap-is-bounded-pieces-not-pieces-plus-rays` | all | **SETTLED (referee), PROOF** | | T437 | T568 |
| `corner-cut-necessary-for-nontriangular-face-gain` | all | **SETTLED (T532, referee-accepted), PROOF** | | T532 | T543 |
| `drop3-reinsertions-saturate-the-edge-cap-at-k18-and-k20` | 18/20 | **SETTLED (referee-verified)** | | T537 | T568 |
| `concurrent-line-through-existing-crossing-unlocks-extra-triangles` | all | **DEAD (referee)** | | T476 | T593 |
| `mutual-adjacency-graph-is-a-linear-forest-not-a-matching` | all | **SETTLED (T530), PROOF + verifier run** | | T528 | T568 |
| `eligible-pair-degree-at-most-one` | all | **SETTLED (referee), PROOF** | Directly relevant to 47c: the criterion demands a mutual-extreme pair, and T605's `H` has 11 edges on 13 lines at `B`. | T466 | T618 |
| `tail-append-caps-at-t-plus-half-k-over-all-orientations` | 14/18/20 | **SETTLED (referee), PROOF** | | T454 | T568 |
| `single-line-gain-far-exceeds-the-tail-ceiling` | all | **SETTLED (referee), and now bounded** | | T469 | T568 |
| `b-plus-14-stretchability-is-the-wrong-question` | 14 | **DEAD (referee)** | Realizability is the last question. | T561 | T568 |
| `k8-record-beats-the-matching-ceiling-from-an-optimal-base` | 8 | **SETTLED but fully explained (referee)** | | T518 | T568 |
| `concurrence-raises-the-ceiling-on-base-lines-only` | all | **SETTLED (T524, referee-verified)** | | T520 | T543 |
| `ring-total-t-not-determined-by-multiplicity-signature` | 18/20 | **SETTLED (referee), VERIFIER RUN** | | T495 | T518 |
| `ring-realized-d-is-3c-and-the-d-framework-does-not-discriminate` | 18/20 | **SETTLED (referee), against my own framework** | | T518 | T543 |
| `k20-c12-n6-f6-ring-dead` | 20 | **SETTLED (referee), three independent routes** | | T405 | T518 |
| `centrally-symmetric-diagonals-force-n-parallel-side-pairs` | all | **SETTLED (SILVER), PROOF, T513 -> T514** | | T512 | T518 |
| `hexagonal-ring-impossible-at-k14` | 14 | **SETTLED (referee), PROOF** | | T405 | T469 |
| `centrally-symmetric-hexagon-at-most-one-reflex-pair` | 14 | **SETTLED (referee-verified), PROOF** | | T461 | T469 |
| `wood-k20-and-k22-records-are-head-append-instances` | 20/22 | **SETTLED (SILVER), T474 -> T475** | | T473 | T543 |
| `bader-k14-and-k18-records-are-not-single-line-extensions` | 14/18 | **SETTLED (referee-verified)** | | T473 | T568 |
| `c3-shift-automorphism-uses-per-row-orientation-flip` | all | **SETTLED (T487)** | | T487 | T518 |
| `c3-orbit-starvation-does-not-transfer-across-k21-optima` | 18 | **CONTESTED (weak form only)** | | T456 | T518 |
| `record-holders-k14-18-20-have-no-dihedral-symmetry` | 14/18/20 | **SETTLED (T500)** | | T500 | T518 |
| `optimal-increment-is-not-a-per-arrangement-cap` | all | **SETTLED (T430), replaced by a real cap** | | T430 | T568 |
| `concurrence-ladder-in-c-does-not-terminate` | 14/18/20 | **SETTLED (referee), UNATTACKED** | | T405 | T543 |
| `central-symmetry-k14-dead-above-c4` | 14 | **CONTESTED (narrowed)** | Open: `c >= 8` at `k = 14`, and any ring with split bridges (T458's hole, untouched for 159 turns). | T365 | T469 |
| `b-formula-with-parallels-and-concurrences` | all | **SETTLED (referee-verified)** | `B(k,p,c) = k(k−2) − 2p − 3c`. | T269 | T543 |
| `k14-pc-enumeration-2p-plus-3c-leq-6` | 14 | **REFUTED as stated; correct form is `2p + F = 6`** | | T269 | T543 |
| `c3-k18-per-orbit-saturation-has-a-realized-precedent` | 18 | **SETTLED (referee-verified)** | | T404 | T543 |
| `c3-k18-free-segments-form-two-orbits` | 18 | **SETTLED (T404 + referee)** | | T404 | T543 |
| `parallelogram-whole-bridge-doubling-impossible-at-mult3` | all | **SETTLED (referee-verified), PROOF** | | T455 | T469 |
| `parallelogram-ring-doubling-forces-mult4` | all | **SETTLED (referee-verified)** | | T467 | T469 |
| `bridge-split-nets-positive-refutes-t457-pricing` | all | **REFUTED (SILVER), T458 -> T459** | | T457 | T469 |
| `k4-bridge-graph-impossible-for-any-four-points` | all | **SETTLED (referee-verified), PROOF** | | T358 | T454 |
| `bridge-graph-must-have-a-crossing-free-straight-line-drawing` | all | **SETTLED (referee-verified), PROOF** | | T361 | T405 |
| `central-symmetry-c4-dead-at-k14` | 14 | **SETTLED (referee-verified)** | | T358 | T405 |
| `fill-rate-extrapolation-is-circular-and-crosses-a-residue-boundary` | 18 | **REFUTED (SILVER), T499 -> T500** | | T497 | T518 |
| `t488-reoriented-double-append-is-not-an-arrangement` | 18/20 | **SETTLED (referee), VERIFIER RUN** | | T492 | T518 |
| `t471-ring-ceiling-violation` | 18 | **REFUTED (referee), units error** | | T471 | T518 |
| `double-tail-append-two-round-cap-leq-n-plus-2` | 18/20 | **SETTLED, subsumed** | | T491 | T568 |
| `interior-crossing-tests-are-blind-to-collinearity` | all | **SETTLED (T449), FLAG RETIRED UNRUN** | | T449 | T518 |
| `only-main-diagonals-through-o-spare-the-bridges` | all | **SETTLED (referee-verified), PROOF** | | T423 | T518 |
| `convex-ring-bridges-survive-the-extension-test` | all | **SETTLED (referee-verified), PROOF** | | T406 | T469 |
| `reflex-vertex-continuation-ray-kills-far-bridge` | 14 | **SETTLED (referee-verified)** | | T461 | T469 |
| `ring-plus-spokes-family-dominated` | 14 | **SETTLED (T429-T431)** | | T428 | T454 |
| `ring-family-ceiling-is-3-plus-f-over-n` | all | **SETTLED, PROVED, NON-BINDING** | | T454 | T518 |
| `adjacent-gap-triangles-mutually-exclusive` | 14 | **CONTESTED (machine evidence)** | | T392 | T405 |
| `chain-gap-triangles-cap-at-two-in-the-full-14-line-arrangement` | 14 | **CONTESTED (search evidence)** | | T393 | T405 |
| `axis-quadrilateral-free-edge-cap-is-three` | 14 | **SETTLED (referee-verified)** | | T356 | T405 |
| `double-ray-vertex-unnecessary-for-the-escape` | 13/14 | **SETTLED (referee-verified)** | | T376 | T405 |
| `central-symmetry-needs-d-above-3c` | 14/18/20 | **SETTLED (referee), nowhere near sufficient** | | T347 | T518 |
| `rotational-census-above-order-2-complete` | 14/18/20 | **SETTLED (referee)** | | T345 | T405 |
| `free-segment-can-have-bounded-faces-on-both-sides` | all | **SETTLED (referee), UNATTACKED** | | T354 | T355 |
| `corpus-rotational-automorphism-census` | all | **SETTLED (referee-verified)** | | T405 | T518 |
| `c3-k18-forces-s-equals-one` | 18 | **SETTLED (referee-verified)** | | T357 | T405 |
| `saturation-implies-total-rigidity-boundary-included` | all | **SETTLED (SILVER)** | | T341 | T355 |
| `interleaved-mirror-axis-structure` | 14 | **SETTLED (referee-verified)** | | T348 | T355 |
| `reciprocity-between-saturated-rows-cannot-obstruct` | all | **SETTLED** | | T344 | T355 |
| `prism-symmetric-embeddings-both-fail` | all | **SETTLED (T362, T364)** | | T360 | T405 |
