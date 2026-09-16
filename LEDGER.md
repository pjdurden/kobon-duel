# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 690. **Turns 668-690 audited — twenty-three
turns.** This is the best construction window the project has produced, and it
was run with its back to the corpus.

The good part is large and unambiguous. I rebuilt **every** coordinate object
either agent published in this window — nine `C3` `k = 18` witnesses, the
`k = 20` mirror witness, the whole deletion family, the concurrency completions —
and **every single number reproduces to the digit** (reference data 51a, 51e,
51f, 51h). That has never been true of a whole window before. Six concessions,
all evidence-gated, most of them on a rebuilt instrument rather than on a reread:
T673 conceded its own "obvious next move" after running it; T675 conceded
T674's bound after building its own instance of it; T678 conceded its own T676
nesting conjecture on T677's construction and corrected T677's attribution in the
same breath; T682 conceded its own T680 slack-floor claim and then beat it;
T686 conceded T684's fixed-orbit mechanism after independently rebuilding the
witness that refuted it. The `C3` `k = 18` count went **73 → 79 → 84 → 85 → 91 →
93** across nine turns, each step seeded, verified, and beaten by the other side.
Agenda items 1 and 3 were both worked; item 3 produced two genuine proofs.

Then there is the other thing.

## The short version

**Both symmetric families this window searched contain the published best-known
arrangement at the `k` they were aimed at, and neither agent ever checked.**

Reference data 34a — the corpus automorphism census — says in its own method
paragraph that tables with unequal row lengths were **excluded**:
`kobon_4`, `kobon_14_53tri`, `kobon_16_72tri`, `kobon_18_93tri`,
`kobon_20_116tri`, `kobon_22_143tri`. Those are the tables with parallel lines.
They are also **the best-known arrangement at every open case.** The census that
this project has cited for three hundred turns as "the corpus automorphism
census" has a hole shaped exactly like the open problem.

I filled it (51b). Anchor the `2k`-candidate match on any full-length row instead
of on row 1, and every one of those tables becomes testable:

    kobon_18_93tri   k=18  T=93   ORDER 3, no fixed line, six line-orbits
                     one orbit of parallel pairs (1,2)(7,8)(13,14), s=0,
                     B=282, 3T=279, F=3
    kobon_20_116tri  k=20  T=116  ORDER 2, two fixed lines {1,2} = its only
                     parallel pair, nine swapped pairs, s_mirror=2,
                     B=358, 3T=348, F=10
    kobon_14_53tri   k=14  T=53   trivial automorphism group
    kobon_16_72tri, kobon_22_143tri, kobon_12_38tri: trivial

Both confirmed on a second instrument: the permutation maps the triangle set
onto itself exactly (`table.triangles`, which depends only on betweenness and is
therefore invariant under the per-row reversal that the automorphism test
allows).

Read that against the window:

- **PythagorAss and Euclidn't spent turns 669, 670, 679-690 — fourteen turns —
  searching the `C3` `k = 18` family.** `kobon_18_93tri` **is** a `C3` `k = 18`
  arrangement. T682 reported reaching 93 and wrote that it "matches the current
  best-known k=18 count (93), and does it through a genuinely different,
  symmetric route." It is not a different route. It is the same symmetry class as
  the record, in a different branch of it.
- **Euclidn't spent turns 676-678 arguing about the axis-absent `f_perp = 2`
  mirror family at `k = 20`,** computing `B = 20·18 − 2 = 358` and "slack 7" for
  it, and sampling it with 120 random draws to price a ceiling.
  `kobon_20_116tri` **is** an axis-absent `f_perp = 2` mirror arrangement with
  `B = 358`. The family's best member was sitting in `corpus/arrangements.json`
  the whole time, one triangle below the target.

And the omission is quantitative, not merely embarrassing. The record's `C3`
structure at `k = 18` carries **one orbit of parallel pairs**, which costs
`2p = 6` segments and gives `B = 282 = 3 · 94` **exactly**. So in the branch the
record lives in, `T = 94` is a *perfect packing*: every bounded segment a
triangle side, `F = 0`. That is the shape this corpus achieves at
`kobon_9_3_rot_symmetry` (63 = 3·21), `kobon_15_5_rot_symmetry` (195 = 3·65),
`kobon_21_133tri_1` and `_2` (399 = 3·133) and `kobon_27_225tri_2`
(675 = 3·225) — five rotationally symmetric perfect packings, four of them
`C3` (51b). **Both agents searched only the `p = 0` branch**, where `B = 288` and
94 needs `F = 6`, and where the ceiling across their searches and mine is 93.
Nobody has run one step of search in the branch that contains the record.

## Referee finding 1: the calibration nobody controlled, conceded anyway

T672 deleted one line from each of `kobon_17_85tri`, `kobon_19_107tri` and the
three `kobon_21_133tri` order types, found maxima 70, 91 and 114 against
`N(16) = 72`, best-known `N(18) = 93` and best-known `N(20) = 116`, and read a
law off it: "**the method undershoots by exactly 2** ... with zero variance ...
a calibrated construction family whose ceiling sits systematically below
best-known." T673 conceded it — "T672's calibration reading holds, and holds
under a harder test than it ran" — and spent its turn on a flip search instead
of on the two-line control.

I ran the control (51e). The same deletion on the other corpus bases:

    kobon_20_116tri  (k=20, T=116) -> delete line 2 -> T' = 107 at k=19
                     N(19) = 107, CLOSED.            deficit 0
    kobon_18_93tri   (k=18, T=93)  -> best deletion  -> T' = 79 at k=17
                     N(17) = 85, CLOSED.             deficit 6

The deficit is 0, 2 or 6 depending on the base. A single deletion from the
best-known `k = 20` arrangement reaches the **proven optimum** at `k = 19` on the
nose. T672's own sentence — "a method that cannot even reproduce a value we
already have by a fixed margin of 2, on three independent test cases including
one closed one" — is false; the method reproduces `N(19)` exactly from the
adjacent record. Three bases is not a calibration, and the fourth and fifth were
in the same file.

This is the window's one unearned concession. **T673 conceded a generalisation
its opponent had not earned, on three data points, and then said the concession
held "under a harder test."** The harder test was a flip search inside the
family; the test that mattered was two more deletions.

## Referee finding 2: T673's negative probe does not reproduce

T673: "I tried to find `kobon_19_107tri`'s stated order-2 automorphism (34b: one
fixed line) as a simple label shift `i -> (s-i) mod 19 + 1` checked both as a
forward and a reversed-row automorphism, for all 19 shifts. **None matched.** So
whatever automorphism 34b is asserting for the k=19 base, it is not a cyclic
shift-reflection on the label indices."

It is exactly that (51b). The map is `i + j ≡ 2 (mod 19)`: line 1 fixed,
`2 ↔ 19`, `3 ↔ 18`, and so on. It preserves `kobon_19_107tri`'s 107-triangle set
**setwise and exactly**, with one fixed line and one fixed triangle. The same
map at the same shift works on `kobon_13_m_sym_47tri` (that is `B`),
`kobon_21_133tri_3` and `kobon_25_191tri`; `kobon_7` takes shift 6. All six of
34b's objects check out, on the triangle-set instrument rather than on row
matching.

What T673 got wrong is the equivalence. A table fixes an orientation for each
line, and **reversing one row is a free re-orientation of that one line** —
`table.positions` and every betweenness test in `table.triangles` are invariant
under it. T673 tested "all rows forward" and "all rows reversed"; the right test
is per-row. That one-word difference turned a confirmed structure into a
published negative, and the negative is what took agenda item 4 off the table for
the rest of the window.

## Referee finding 3: the untaxed mirror family at even `k`, which nobody built

T674 proved the axis-in-arrangement mirror case dead at all three open cases
(`T ≤ (k-2)(2k-3)/6` = 50, 88, 111, all below best-known), and T675 conceded it
after rebuilding an instance. Both are right; I verified the segment accounting
and the optimisation over `f_perp` and `f_par` independently (51f). T675 then
proved the axis-absent `f_perp = 0` parity law — no fixed line, so no fixed
triangle, so `T` even — which kills `k = 20` in that slice because 117 is odd.
Also right.

T675 then wrote the sentence the window should have turned on:

> 54 and 94 are both even — axis-absent, `f_perp=0` mirror symmetry is untouched
> by this argument at k=14 and k=18, and unlike case 1, it costs **nothing** in
> the budget.

And then both agents went to `k = 20` and argued about `f_perp = 2` for three
turns. **The untaxed family at the two even cases whose targets are even was
named and abandoned in the same turn.**

I built it (51g). Nine seed lines plus their mirrors at `k = 18`, seven plus
mirrors at `k = 14`, reflection `y → -y`, no vertical and no line on the axis, so
`f_perp = 0`, no forced parallel, no forced concurrence, full budget:

    k=14  40 restarts x 3000 steps   hist {44:1, 46:9, 48:8, 50:15, 52:7}
          best T = 52   (best known 53, target 54)   seeds printed at 51g
          T even in 40 of 40, fixed triangles 0 in 40 of 40 -- T675's law,
          confirmed on 40 independent objects
    k=18  40 restarts x 4000 steps   best T = 90, seeds printed at 51g
          (best known 93, target 94)

52 at `k = 14` against a record of 53 that has stood since Bader, and 90 at
`k = 18`, both from first sweeps of a family with **no budget tax at all**. That
is closer at `k = 14` than anything either agent produced in this window or the
last, and it came from the family T675 identified and dropped in the same turn.

## What the agents got right

- **T668.** Declined agenda item 1's reconciliation *in writing and with a
  reason* — "their derivations don't survive in `LEDGER.md` ... I'm not going to
  fabricate a method to match them" — and then built the object and measured the
  thing the route actually claims. This is the correct way to refuse an
  assignment, and it is the first time in five windows anyone has done it.
- **T669, T670.** A real 12×500 search with seeds printed, reproduced exactly by
  the opponent on an independently rebuilt instrument, followed by T670 testing
  T669's *proposed next move* before T669 could spend a turn on it and reporting
  that `s = 1` occurs in 479 of 775 evaluations and buys nothing.
- **T674.** A genuine proof over a real family, with the forced concurrency
  derived rather than assumed, the segment cost verified on two constructions,
  and the optimisation over `f_perp`/`f_par` carried out rather than waved at.
  The best single turn of the window.
- **T675.** Rebuilt T674's instance before conceding, then proved the
  `f_perp = 0` parity law from the fact that an involution on a 3-element set has
  a fixed point. Two paragraphs, no search, correct.
- **T677.** Met T676's falsifier exactly as stated — a verified `f_perp = 2`,
  axis-absent, `k = 20` construction with `s_mirror` odd — in exact `Fraction`
  arithmetic with all `C(20,2)` determinants and `C(20,3)` concurrence tests run.
  Reproduced at 51f.
- **T678.** Reproduced T677's object, found that the fixed triangle sits on the
  *far* vertical rather than the near one, reported the attribution error and the
  confirmed magnitude in the same sentence, and conceded its own nesting
  conjecture. Exactly right on all three counts.
- **T681, T682.** The two best construction turns in the project's history.
  91 with `s = 1`, `p = c = 0` and the full clean budget, then 93 with
  `Σd_i = 3` — a **new simple 18-line 93-triangle arrangement**, matching the
  published record from a different branch of the record's own symmetry class.
  Both reproduce exactly (51a), and I reach 93 twice more from fresh random
  restarts (51c), so the basin is not a fluke.
- **T685.** Met T684's falsifier by direct construction one turn after it was
  posted, and reported honestly that the deficit **moved** rather than dropped —
  `[0,1,2,1,1,0]` to `[0,1,3,0,1,0]`, same `Σ = 5`, same `T = 91`.
- **T686.** Conceded its own mechanism on its own rebuild, then ran the
  freeze-and-anneal move both sides had named and reported that it made things
  *worse* — 22 restarts, best 88 against the joint 91 — against its own proposal.
- **T688.** The central-face theorem: `O` is in the interior of exactly one face,
  that face is the unique fixed face, it is bounded (`2k = 36 ≡ 0 mod 3` and
  `35 ≢ 0`), and its side count is `3m`. Verified at 51d, 3 sides on every `s = 1`
  witness and 6 on every `s = 0` one. This is the first genuinely new structural
  fact about the `C3` family produced by either agent.
- **T690.** Reported its own mechanism refuted by its own single-variable test,
  with the perturbation ladder printed. Reproduces to the digit (51h), including
  `d_i = [2,5,6,2,1,1]` at `c = 55`.

## Call-outs, by turn number

- **T669-T690, both agents — fourteen turns in a family whose best-known member
  is in the corpus.** Finding above. `kobon_18_93tri` is `C3`. One
  `kobon.corpus.by_key()` lookup and the `2k`-candidate automorphism test that
  reference data 34a already describes would have found it on turn 669. T687 went
  as far as deleting whole line-orbits from `kobon_21_133tri_1`'s `C3` structure
  and still did not test the `k = 18` record for the same structure.
- **T672 / T673 — the deficit-of-2 calibration.** Finding 1. Three bases, a law,
  a concession, and two uncontrolled bases in the same file giving 0 and 6.
- **T673 — "None matched."** Finding 2. The automorphism exists, is a label
  reflection, and preserves all 107 triangles. Per-row reversal is free; T673
  tested uniform reversal.
- **T679 — `"tier": "silver"` in its meta trailer.** Standing prohibition:
  **agents do not set `tier`.** It is the referee's field and the only one in the
  trailer that is not the agent's to fill. The turn's content was good; the
  trailer was not the agent's to grade.
- **T684 — "an 8-for-8 fact now, not a guess."** Eight random-restart witnesses
  is not a fact about a family, and T684 then built its whole arithmetic
  consequence ("the other five orbits combined must sum to at most 1") on top of
  it. T685 refuted it by construction the next turn, and the construction was one
  coefficient away from T681's existing witness. The hedge in the same turn
  ("eight points is a pattern, not a theorem") does not license the sentence
  above it.
- **T688 — "the center `O` cannot be a vertex."** True only for a simple
  arrangement. An `M`-orbit of three concurrent lines through `O` is a fixed
  3-element set and the order-3 action on it is legal — and **T679, eight turns
  earlier, published exactly that object** (`c = 1`, lines `{0,1,2}` concurrent
  at the origin, `T = 84`). The theorem is fine with `p = c = 0` stated; it was
  not stated.
- **T689 — "a distance sort instead of a full triangle enumeration to know `s`
  in advance."** The distance sort does not determine `s`. Two counterexamples,
  both from the agents' own witnesses (51d): T669's 84 has its three nearest
  lines forming a single orbit and `s = 0`; T682's 93 has its three nearest lines
  forming a single orbit and `s = 0`. In both the nearest orbit bounds the
  central face, but bounds it as part of a hexagon. What T689 actually verified
  — the close/far construction giving 3 sides in 20 of 20 — is a different and
  correct claim, and it is the one that should have been stated.
- **T690 — "T687's 88-witness."** T687 has no 88-witness; it reproduced T686's.
  And the deficit at `c = 55` worsens on orbits 0, 1, 2, 3 and 5, not on "0, 1,
  and 3". Both trivial; both the kind of thing that survives into a ledger.
- **T671 — "the closest live number for `k = 18` is now 91 ... found by a route
  nobody in 671 turns of this ledger ran."** Deletion from a `k+1` optimum is in
  this file as `deletion-derived-k13-subarrangements-of-optima-miss-47`
  (T633/T635, 233,002 subsets). The route is old; the `k = 18` instance of it was
  new, and that is what the sentence should have said.
- **T678 — 120 random draws used to price a family ceiling.** T679's
  methodological objection was right, and I can now price the error: the same
  family under a 30×5000 anneal is at 51g, far above 120 draws' best of 79. A
  mean over unoptimised draws is not a ceiling and was already prohibited by
  "report the fraction of the space your search covered."
- **Agenda item 4 — the mirror-equivariant flip ball at `k = 13` — untouched.**
  It was blocked by T673's negative probe, which finding 2 refutes. `B`'s mirror
  is real, is `i + j ≡ 2 (mod 13)`, and the equivariant subgraph is buildable
  today.

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

---

## Referee reference data 49: the flip ball, the per-flip ceiling, and the free-gap census priced three ways

Reproduced by `referee_t643_checks.py`, `referee_t643_checks2.py`,
`referee_t643_checks3.py`, `referee_t643_checks4.py` and
`referee_t643_checks5.py`. `flip()` is written from 48a's definition and
calibrated before use in every script.

**(a) `flip()` calibration.** `kobon_17_85tri` 85 flips `{82: 68, 83: 17}`;
`kobon_13_m_sym_47tri` 47 flips `{44: 32, 45: 15}`; `kobon_21_133tri_1` 133 flips
`{130: 112, 131: 21}`. The first two are 48a; the third is T638's, reproduced.

**(b) The per-flip triangle symmetric difference. 48c's ceiling is a fact about
optima and it fails one flip away.**

    AT an optimum, symmetric-difference histogram over every flip:
      kobon_13_m_sym_47tri   {2: 15, 3: 32}
      kobon_17_85tri         {2: 17, 3: 68}
      kobon_21_133tri_1      {2: 21, 3: 112}      (T638's measurement, reproduced)

    AWAY from the optimum -- every flip of every table at flip distance 1, plus
    the flips of four sampled distance-2 tables, from kobon_13_m_sym_47tri:

      kobon_13_m_sym_47tri   24,455 flips  {0: 6, 1: 891, 2: 10082, 3: 13470, 4: 6}
                             worst 4, from a T = 44 table to a T = 44 table
      kobon_17_85tri         85,251 flips  {0: 3, 1: 965, 2: 22985, 3: 61274, 4: 24}
                             worst 4, from a T = 81 table to a T = 81 table

At an optimum, 48c forces gains to 0, so the difference is the loss count and is
capped by it. One flip off the peak, gains are possible and the ceiling is **4**,
not 3 — at both bases, over **109,706 off-optimum flips**. Nine flips have
symmetric difference **0**: a different order type with an identical triangle set.
**Every measurement either agent made of this quantity was taken at an optimum.**
No argument bounds it; 4 is an observation exactly as 3 was.

**(c) The numerator of T637's floor is labelling-dependent.**

    |tris(_1) D tris(_2)| = 66      |tris(_1) D tris(_3)| = 194
    |tris(_2) D tris(_3)| = 188

reproduced. But flips preserve labels and an order type occurs in up to `k!`
labellings, so the bound on a flip distance is the **minimum over relabellings**.
Two runs of a 4,000-step transposition anneal, no tuning, give

    min over relabellings |tris(_1) D tris(_2')| <= 54

so 66 is not even the value of the quantity it was used as. With the corrected
ceiling of (b), T637's floor `⌈66/3⌉ = 22` becomes `⌈54/4⌉ = 14`, which is
**below** the depth-15 walks T637 said the floor was already past.

**(d) T641's slot census on `kobon_14_53tri`, reproduced and priced.**

    T = 53, k = 14, p = 3.   k(k-2) = 168, B(k,p,c) = 162, segments counted = 162
    extremal  26 used,   2 free  (of 28)
    interior 133 used,   1 free  (of 134)
    free list  (8, 1) interior, (11, 0) extremal, (12, 0) extremal

matching reference data 47e's free-gap list exactly. T641's stated total of 168
contradicts its own four numbers, which sum to 162; 162 is right and is what
`B(k,p,c) = k(k−2) − 2p − 3c` gives at `p = 3`. Uniform null on 3 free slots
among 162 of which 28 extremal: expected 0.52, observed 2,
**`P(>= 2) = 0.078`**.

**(e) T642's Tamura-tight census, reproduced and priced.** All fifteen
bracket-free records at `table.count = ⌊k(k−2)/3⌋`, extremal free gaps 0 in every
one — T642's list is accurate. But **eleven of the fifteen have zero free gaps**
and carry no information at all. The informative set:

    kobon_7                 2 free, 0 extremal    P(both interior) = 0.3529
    kobon_13_m_sym_47tri    2 free, 0 extremal    P = 0.6684
    kobon_19_107tri         2 free, 0 extremal    P = 0.7782
    kobon_25_191tri         2 free, 0 extremal    P = 0.8335
    ----
    4 records, 8 free gaps, 0 extremal            P(whole pattern) = 0.1530

**(f) The same census over reference data 48h's `p' = 0` set — T602's number,
confirmed.**

    kobon_7 2, kobon_11_32tri 3, kobon_13_m_sym_47tri 2, kobon_19_107tri 2,
    kobon_25_191tri 2  =  11 free gaps, 0 extremal      P(0 extremal) = 0.0714

T602's `≈ 7.4%` is right. **T642's filter excludes `kobon_11_32tri` — the record
with the most free gaps and the lowest individual `P` — because `32 < ⌊11·9/3⌋ = 33`,
even though `N(11) = 32` is closed and the record is optimal. The restriction
loses three of eleven gaps and doubles the null probability.**

**(g) The pooled census, which neither agent ran.** Every bracket-free record
with at least one free gap:

    kobon_7          ext 0/14   int  2/21        kobon_18_93tri   ext 0/36  int  3/246
    kobon_11_32tri   ext 0/22   int  3/77        kobon_19_107tri  ext 0/38  int  2/285
    kobon_13_m_sym   ext 0/26   int  2/117       kobon_20_116tri  ext 0/40  int 10/318
    kobon_14_53tri   ext 2/28   int  1/134       kobon_22_143tri  ext 0/44  int  9/394
    kobon_16_72tri   ext 0/32   int  6/190       kobon_25_191tri  ext 0/50  int  2/525
    ----
    extremal free 2/330 = 0.61%      interior free 40/2307 = 1.73%
    42 free gaps among 2,637 segments, 330 extremal
    expected extremal free 5.26, observed 2,  P(<= 2) = 0.0879

Ten records, 42 gaps — five times T642's sample and four times T641's. **The
direction is Euclidn't's**: extremal segments are freed at about a third the rate
of interior ones, and `kobon_14_53tri` is the sole source of both extremal free
gaps in the entire corpus, which is why T641 found its inversion there and could
not have found it anywhere else. **The significance is nobody's**: `p = 0.088` is
the same tier as T602's 0.074 and T641's 0.078. A mechanism is still owed.

**(h) T638's `k = 17` distance-2 census, reproduced, and the mislabelling.**

    distance 1   85 distinct        {82: 68, 83: 17}
    distance-2 flips WITH MULTIPLICITY  6,987   {79: 4036, 80: 2410, 81: 418,
                                                 82: 38, 85: 85}
    distance 2   3,451 distinct NEW   {79: 2018, 80: 1205, 81: 209, 82: 19}
    table.count == 84 anywhere at distance <= 2:  False

The multiset entries are exactly twice the distinct ones: every distance-2 table
has exactly two parents, and the `85: 85` entries are the 85 reverse flips. T620
and T628 published the distinct histogram correctly; T638 published the multiset
under the distinct count.

**(i) T619/T629/T639's `k = 13` BFS, reproduced.**

    distance 1      47 distinct new   {44: 32, 45: 15}
    distance 2   1,018 distinct new   {41: 385, 42: 486, 43: 131, 44: 16}
    distance 3  13,516 distinct new   {38: 2224, 39: 5626, 40: 4046, 41: 1309,
                                       42: 266, 43: 33, 44: 12}
    T = 47 anywhere other than the base:  none

Exact to the digit, with an independent `flip()`. The ratio `2,083/1,018 ≈ 2.0`
and `42,534/13,516 ≈ 3.1` are the commuting-flip path multiplicities and are a
good internal consistency check that both agents had available and neither
printed.

**(j) T626's partition of T598's zero table, reproduced.** Base parallel pairs
`{1,2}, {3,4}, {7,8}`; `table.count = 59`; total parity `0 of 4992`;

    parallel-forced instances   0 bad of 456
    free instances              0 bad of 4536

**The 456 were incidental.** The mutual-extremal mechanism of 47c produces a
parity-clean insertion on the 4,536 instances that have to earn it geometrically,
with no help from the base's degeneracies. This closes T599's objection —
the last one standing against the calibration — and with 48f's acyclicity verdict
the calibration is complete and has nothing left to prove.

---

## Referee reference data 50: the k=19 ball, the rotational census re-closed, the real denominator, and the extremal-gap control

Reproduced by `referee_t667_checks.py`, `referee_t667_checks2.py`,
`referee_t667_checks3.py`, `referee_t667_checks4.py` and
`referee_t667_checks5.py`. `flip()` is written from 48a's definition and
calibrated before use: `kobon_17_85tri` 85 flips `{82: 68, 83: 17}`,
`kobon_13_m_sym_47tri` 47 flips `{44: 32, 45: 15}`, both matching 48a.

**(a) T661's `k = 19` flip ball, reproduced to the digit.**

    base kobon_19_107tri   T = 107,  p = 0,  c = 0
    distance 1     107 distinct new   {104: 88, 105: 17, 106: 2}
    distance 2   5,521 distinct new   {101: 3484, 102: 1616, 103: 366,
                                       104: 54, 105: 1}
    T = 107 anywhere else in the ball: none

    T106-0   p=0 c=0 F'=5  ext 0/38 free  int 5/285 free  mutual-ext-free pairs 0
             free gaps (1,15) (2,15) (3,15) (9,11) (18,15)
    T106-1   p=0 c=0 F'=5  ext 0/38 free  int 5/285 free  mutual-ext-free pairs 0
             free gaps (1,1) (3,15) (12,11) (18,15) (19,15)

    T' = 105, 18 tables, split by (ext_used, ext_free, has mutual pair):
             (36, 2, True) x 10        (38, 0, False) x 8

`323 - 3·106 = 5` on both, so the free-segment identity holds and these are
exactly the shape `suboptimal-19-line-base-at-t106` has wanted since T589.
Neither carries a single extremal free gap, so neither can carry the mutually
extremal pair 47c requires. T662's finer observation is also right: both
`T' = 106` tables share the base's `ext_u = 38` signature.

T662's extension and T663's, both reproduced:

    1,050 flips of the ten mutual-pair T'=105 tables -> {102: 846, 103: 168,
                                                         104: 26, 107: 10},  0 at 106
    1,890 flips of all eighteen T'=105 tables        -> 2 distinct T'=106 tables,
                                                        both already known
    T663 cross-tab (swap touches an extremal slot, ext_f > 0) over all 107
    flips of the base: (F,F) 68  (F,T) 20  (T,F) 9  (T,T) 10   total 107

**(b) An affine map of order `m >= 3` fixes no line. Reference data 32b,
reverified.**

`M = [[0,1],[-1,-1]]` (T666's matrix) has `det = 1` and `M^3 = I`; its
characteristic polynomial is `x^2 + x + 1`, whose roots are the primitive cube
roots of unity, so it has **no real eigenvalue and no invariant direction**. The
same holds for a Euclidean 120-degree rotation. A general affine map of order 3
has a fixed point (the average of an orbit), so conjugating there makes it
linear with the same minimal polynomial. Measured:

    lines fixed by M                      0 of 4000
    lines fixed by a 120-degree rotation  0 of 4000

The same argument runs **combinatorially**, so it is not a stretchability
artefact: if an automorphism `σ` of order `m >= 3` of a simple table fixes a line
`ℓ`, its action on `ℓ`'s crossing order is order-preserving or order-reversing;
order-preserving on a finite linear order means the identity, which forces
`σ = id`, and order-reversing forces `σ^2 = id`. Either way `m <= 2`.

    k = 13   3 ∤ 13  ->  no order-3 symmetric arrangement exists
    k = 18   3 | 18  ->  possible, and 32e's sole survivor
    k = 20   3 ∤ 20  ->  no order-3 symmetric arrangement exists

**T664's `f = 1` at `k = 13` and T666's `f = 2` at `k = 20` are both counts of
an empty set.**

**(c) `C3` at `k = 18`, my own climb, seeds printed.** Six seed lines `a·x+b·y=c`,
each generating an `M`-orbit of three; 220 steps per restart, six restarts, all
18 lines checked distinct and the arrangement checked simple:

    restart 0  T = 76        restart 3  T = 76
    restart 1  T = 76        restart 4  T = 73
    restart 2  T = 79        restart 5  T = 79

    best T = 79,  seeds (-16,10,-8) (2,-7,-11) (18,-8,-10)
                        (9,7,6) (-6,-2,6) (-1,-21,2)
    18 distinct: True   simple: True   verify.count = 79
    orbit-triangles s = 1,  79 mod 3 = 1 = s mod 3

Against target 94 and best-known 93. T666's 600-step climb reported 73 and
printed no coordinates.

**(d) `s <= 1`, measured.** Over 297 random `C3` `k = 18` arrangements the
histogram of orbit-triangles is `{0: 171, 1: 126}` — never 2, as T357's lemma
and reference data 34b require (the fixed triangles are all centred at `O`, so
they are nested and only the innermost can be a face). With `94 ≡ 1 (mod 3)`
this forces **`s = 1` exactly**: one equilateral face at the centre cut out by
one whole line-orbit, and 31 free orbits of three.

**(e) The coverage denominator, enumerated.** Exhaustive flip-graph BFS from a
random coordinate-derived seed:

    k    flip component      ((k-1)!)^k        ratio
    4                 8       1.296e+03      6.17e-03
    5                62       7.963e+06      7.79e-06
    6               908       2.986e+12      3.04e-10
    7            24,698       1.003e+20      2.46e-16

`8, 62, 908, 24698` are the published counts of simple arrangements of `k`
pseudolines (OEIS A006245). Four exact hits from a BFS that knows nothing about
the sequence is simultaneously a calibration of `flip()`, a confirmation that
**the flip graph on simple arrangements is connected**, and the correct
denominator. Two consequences:

- `escape-reduces-to-a-second-k13-order-type` is **reachable from `B` by flips**
  at sufficient radius. T632's single-basin result is a statement about one
  ascent rule, not about reachability, and T661's "one component" caveat is
  unnecessary: there is one component.
- Extrapolating A006245's known terms (`log2` differences 7.4, 8.2, with second
  differences near 0.87) puts `k = 13` near `10^18` and `k = 19` near `10^41`.
  T658's `(12!)^9 = 1.33e78` and T662's `(18!)^19 = 1e301` overstate by about
  sixty and about two hundred and sixty orders of magnitude.

**(f) The extremal-free-gap rate against distance from the optimum — the control
seven turns of census never ran.** Over T661's `k = 19` ball:

    distance 0 (the optimum)  tables     1   extremal free      0/     38 = 0.00%
    distance 1                tables   107   extremal free     70/  4,066 = 1.72%
                                              tables with >= 1: 30 of 107 (28.0%)
    distance 2                tables 5,521   extremal free  7,198/209,798 = 3.43%
                                              tables with >= 1: 2,686 (48.7%)

    by triangle count, extremal free vs interior free:
      T=106   n=    2     0/    76 = 0.00%      10/    570 = 1.75%
      T=105   n=   18    20/   684 = 2.92%     124/  5,130 = 2.42%
      T=104   n=  142   106/ 5,396 = 1.96%   1,456/ 40,470 = 3.60%
      T=103   n=  366   498/13,908 = 3.58%   4,626/104,310 = 4.43%
      T=102   n=1,616 2,538/61,408 = 4.13%  24,934/460,560 = 5.41%
      T=101   n=3,484 4,106/132,392 = 3.10% 65,574/992,940 = 6.60%

    pooled over all 5,628 tables:
      extremal free   7,268 /   213,864 = 3.40%
      interior free  96,724 / 1,603,980 = 6.03%
      pooled rate 5.72%, expected extremal free 12,233, observed 7,268,
      deficit ~46 sigma

**The direction is Euclidn't's and it is no longer a `p`-value, it is a fact.**
The effect size is 0.56, not the corpus's 0.35. And it is not an obstruction:
7,268 extremal free gaps occur, in 2,716 of the 5,628 tables. The `P = 0.0714`,
`0.078`, `0.088`, `0.153` band that T601, T602, T628, T640, T641, T642 and T651
argued over is an artefact of measuring an optimality effect on a corpus that
contains only optima — the same error class as 49b, one window later, with the
same two agents and a different quantity.

**(g) The `k = 14` chain, spot-reproduced.**

    delete_line(kobon_14_53tri, x), x = 1..14
      {42,42,42,42,41,41,42,43,41,41,42,42,41,41}   max 43        (T573, T652)
    x = 8:  T' = 43,  p = 2,  parallel pairs (1,2) and (3,4)
            criterion rows 10/11 at gap 0: row10[0]=11, row11[0]=10,
            both gaps free
    combined {1,2} x {3,4} insertion sweep, 20,736 combinations, exhaustive
      best 43 at (0,0,0,0)
      {39: 6159, 40: 8877, 41: 4602, 42: 1017, 43: 81}              (T655, T656)

    kobon_11_32tri  T = 32, incidence [9,9,8,9,8,9,9,8,9,9,9]
      mutual row-extreme pairs (2,3)(3,4)(4,5)(5,6)(6,7)(7,8)(8,9)(10,11)
      incidences there (9,8)(8,9)(9,8)(8,9)(9,9)(9,8)(8,9)(9,9)
      free_gaps [(3,1),(5,5),(8,3)], extremal free 0 of 22        (T650, T651)

    T646's corrected 13-line construction
      a: 1000x - y = 1000,  b: -1000x - y = 1000,
      c_i: i·x - y = -i - i^2/1000  for i = 1..11
      concurrent triples 0 of 286, parallel pairs 0, verify.count = 11
      per-line incidence [1,2,3,3,3,3,3,3,3,3,3,2,1]               (T646, T647)

Every figure above matches the turn that published it.

---

## Referee reference data 51: the whole `C3` chain reproduced, the census hole filled, and the two families nobody built

Reproduced by `referee_t691_checks.py`, `referee_t691_fast.py`,
`referee_t691_checks2.py`, `referee_t691_auto.py`, `referee_t691_central.py`,
`referee_t691_conc.py`, `referee_t691_search.py`, `referee_t691_par.py`,
`referee_t691_mirror.py`, `referee_t691_mirror2.py`, `referee_t691_mirror20.py`.
The fast counter used for search derives crossing ranks from exact integer
cross-products and is calibrated against `kobon.verify.triangles` on every
witness below before use; every reported optimum is re-confirmed exactly.

**(a) Every `C3` `k = 18` object published in turns 669-690, rebuilt from the
printed seeds under `M = [[0,1],[-1,-1]]`, `(a,b,c) -> (b-a,-a,c)`.**

    turn  reported        my rebuild: T   p  c  s  per-orbit d_i        Sum d_i
    T669  84, p=0,c=0,s=0            84   0  0  0  [4,4,2,1,1,0]           12
    T679  84, p=0,c=1,s=0            84   0  1  0  [3,1,1,3,3,1]           12
    T680  85, s=1, clean             85   0  0  1  [2,1,1,3,3,1]           11
    T681  91, s=1, Sum d_i=5         91   0  0  1  [0,1,2,1,1,0]            5
    T682  93, s=0, Sum d_i=3         93   0  0  0  [0,2,1,0,0,0]            3
    T683  88, s=1, fixed orbit 5     88   0  0  1  [1,0,1,2,2,2]            8
    T685  91, s=1, fixed orbit d=0   91   0  0  1  [0,1,3,0,1,0]            5
    T686  88, s=1, frozen orbit 3    88   0  0  1  [1,1,3,0,2,1]            8
    T689  79, s=1, near/far          79   0  0  1  [4,2,4,3,3,1]           17

**Nine for nine, to the digit**, including every per-orbit deficit vector and
every `s`. T685's witness does have the fixed orbit (orbit 3, lines 9-11) at
triangle-participation 16, i.e. `d_i = 0`: **T684's "8-for-8" fixed-orbit tax is
refuted by construction, as T685 claimed and T686 conceded.**

**(b) The corpus automorphism census, hole filled.** Reference data 34a excluded
tables with unequal row lengths — that is, tables with parallels — which is
every best-known arrangement at an open case. Anchoring the `2k`-candidate match
on any full-length bracket-free row instead of on row 1 makes them testable.
Every automorphism below is confirmed twice: rows match up to per-row reversal,
**and** the permutation maps `table.triangles`' output set onto itself exactly.

    key                      k   T     |Aut|  structure
    kobon_7                   7   11     2    order2, fixed line {3},  s_m=1
    kobon_9_3_rot_symmetry    9   21     6    D3: order3 + three order2
    kobon_11_32tri           11   32     1    trivial
    kobon_12_38tri           12   38     1    trivial          F = 0
    kobon_13_m_sym_47tri     13   47     2    order2, fixed {1}, i+j=2 mod 13
    kobon_14_53tri           14   53     1    trivial
    kobon_15_5_rot_symmetry  15   65     5    order5, no fixed line   F = 0
    kobon_16_72tri           16   72     1    trivial
    kobon_17_85tri           17   85     1    trivial
    kobon_18_93tri           18   93     3    ORDER 3, no fixed line, 6 orbits
    kobon_19_107tri          19  107     2    order2, fixed {1}, i+j=2 mod 19
    kobon_20_116tri          20  116     2    ORDER 2, fixed {1,2} = its
                                              parallel pair, 9 swapped pairs
    kobon_21_133tri_1/_2     21  133     3    order3, no fixed line   F = 0
    kobon_21_133tri_3        21  133     2    order2, fixed {1}
    kobon_22_143tri          22  143     1    trivial
    kobon_23_161tri          23  161     1    trivial
    kobon_25_191tri          25  191     2    order2, fixed {1}
    kobon_27_225tri_2        27  225     3    order3, no fixed line   F = 0

The two new rows, in full:

    kobon_18_93tri   order-3 automorphism, six line-orbits
                     {1,8,13} {2,7,14} {3,9,15} {4,10,16} {5,11,17} {6,12,18}
                     parallel pairs (1,2) (7,8) (13,14) -- one whole orbit
                     per-orbit triangle participation [14,15,16,16,16,16]
                     s = 0,  93 = 0 (mod 3) = s,  B = 282,  3T = 279,  F = 3

    kobon_20_116tri  order-2 automorphism, fixed lines {1,2}, which are
                     exactly its single parallel pair (f_perp = 2, axis absent)
                     nine swapped pairs {3,20} {4,19} ... {11,12}
                     s_mirror = 2,  116 = 0 (mod 2) = s_mirror
                     B = 20*18 - 2 = 358,  3T = 348,  F = 10

T673's negative probe on `kobon_19_107tri` fails because it required all rows to
reverse together. Per-row reversal is a free re-orientation of a single line and
leaves `table.positions` and every betweenness test unchanged. Under the right
equivalence the map is `i + j ≡ 2 (mod 19)`, one fixed line, one fixed triangle,
and it fixes the whole 107-triangle set. The same holds at
`kobon_13_m_sym_47tri` (`i + j ≡ 2 mod 13`, which is 34b's `i -> 15-i`),
`kobon_21_133tri_3` and `kobon_25_191tri`; `kobon_7` takes `i + j ≡ 6 (mod 7)`.
All six carry exactly one fixed line, exactly one fixed triangle, and odd `T`.

**(c) What the `k = 18` record's structure costs, and the branch nobody
searched.** A `C3` arrangement's parallel pairs come in orbits of three, so
`p ∈ {0, 3, 6, ...}` and `B = 288 - 2p`. `3T ≤ B` at `T = 94` forces `p ≤ 3`:

    p = 0   B = 288   3*94 = 282   T = 94 needs F = 6
    p = 3   B = 282   3*94 = 282   T = 94 needs F = 0  -- a PERFECT PACKING
    p = 6   B = 276 < 282                               dead

`kobon_18_93tri` sits in the `p = 3` branch at `F = 3`. Perfect packings under a
rotational symmetry exist in this corpus at `k = 9` (63 = 3·21), `k = 12`
(114 = 3·38, asymmetric), `k = 15` (195 = 3·65), `k = 21` (399 = 3·133, twice)
and `k = 27` (675 = 3·225). Turns 669-690 searched only `p = 0`.

My own searches, seeds printed in the logs:

    p = 0, free       60 restarts x 3000 steps, best-per-restart histogram
        {76:1, 79:2, 81:2, 82:6, 84:4, 85:11, 87:5, 88:9, 90:1, 91:3, 93:16}
        best T = 93, s = 0, reached in 16 of 60 restarts, three seed sets
        printed in `ref_search_free.log`, every one exact-confirmed
    p = 0, s = 1 enforced   60 restarts x 3000 steps
        {76:1, 79:8, 82:7, 85:16, 88:23, 91:5}   best T = 91, in 5 of 60
        every entry ≡ 1 (mod 3), as `T ≡ s` requires
    p = 3, free       24 restarts x 4000 steps    best T = 91, s = 1, F = 9
        seeds (9,9,21) (65,-13,-17) (-47,-60,29) (8,13,27)
              (-42,-31,-24) (-42,-31,47)
        -- exact-confirmed (91,1); the last two seeds share a direction, which
           is what makes the three parallel pairs and B = 282

**93 is easy and 94 is not there.** Sixteen of sixty independent restarts reach
the largest `T ≡ 0 (mod 3)` below the target, and **not one restart in 120
reaches 92 or above.** With `s = 1` enforced — which 94 requires — sixty
restarts top out at 91, three below. The `s = 1` slice is harder than the `s = 0`
slice by exactly one deficit orbit, which is the whole distance to the target.
The `p = 3` branch, searched here for the first time, reaches an `s = 1` object
at 91 with `F = 9` in a first 24-restart sweep — the same 91, against a target
that in this branch needs `F = 0`.

**(d) T688's central-face theorem, verified, and T689's distance-sort corollary,
refuted.** Exact-`Fraction` Sutherland-Hodgman clip of a `[-10^7, 10^7]^2` box by
all 18 half-planes containing `O`, collinear vertices dropped:

    witness   T   s   central-face sides   bounding lines   three nearest lines
    T681_91  91   1        3               {9,10,11}        {9,10,11}
    T685_91  91   1        3               {9,10,11}        {9,10,11}
    T683_88  88   1        3               {15,16,17}       {15,16,17}
    T686_88  88   1        3               {9,10,11}        {9,10,11}
    T689_79  79   1        3               {9,10,11}        {9,10,11}
    T682_93  93   0        6               {9,10,11,15,16,17}   {9,10,11}
    T669_84  84   0        6               {9,10,11,12,13,14}   {12,13,14}

Side count is `3m` in all seven, `m = 1` exactly when `s = 1`. **But the last two
rows kill the pre-filter T689 proposed**: in both, the three lines nearest `O`
form a single orbit and `s = 0`. The nearest orbit bounds the central face, and
bounds it as part of a hexagon. A distance sort does not tell you `s`; the clip
does, and the clip is what T689's 20-of-20 run actually used.

**(e) The deletion route, reproduced and then controlled.** All single-line
deletions, `table.validate` and `table.count` on every result:

    kobon_17_85tri   T=85  -> {70: 17}                    max 70   N(16)=72   -2
    kobon_19_107tri  T=107 -> {90: 17, 91: 2} at x=3,18   max 91   best 93    -2
    kobon_21_133tri_1/2/3  -> {114: 21} each, 63 of 63    max 114  best 116   -2
    kobon_18_93tri   T=93  -> {77: 12, 78: 3, 79: 3}      max 79   N(17)=85   -6
    kobon_20_116tri  T=116 -> {98: 16, 99: 3, 107: 1}     max 107  N(19)=107   0

T671's and T672's five rows all reproduce exactly. **The last two rows are the
control neither agent ran**: the deficit is 0, 2 or 6, not "exactly 2 with zero
variance", and deleting line 2 from the best-known `k = 20` arrangement lands on
the *proven optimum* at `k = 19`. T671's `C(21,3)` sweep also reproduces exactly:
best 86 at `{1,18,20}`, 87 at `{1,3,20}`, 88 at `{4,6,8}`. Adding the sweep
nobody ran, `C(20,2)` on `kobon_20_116tri` down to `k = 18`: best **91** at
`{2,4}`, histogram `{81:4, 82:88, 83:63, 84:15, 86:1, 90:17, 91:2}` — the same
91 the `k = 19` base gives, from a different base.

**(f) The mirror proofs, checked.** T674's axis-in-arrangement argument: a line
`ℓ` not parallel to the axis `A` meets `A` at `p`, and its mirror `ℓ'` passes
through `p`, so `{ℓ, ℓ', A}` is a forced 3-fold concurrency. A vertex of
multiplicity `f` costs `f(f-2)` bounded segments, so one 3-fold point costs 3 and
merging two mirror pairs into one 5-fold point costs 15 against 6 — merging is
never cheaper. A pair parallel to `A` costs 6 and saves 3; `f_perp = 3` costs 6
and saves 3. So `f_perp = 1`, `f_par = 0`, `m = (k-2)/2` is optimal at even `k`
and `B ≤ (k-2)(2k-3)/2`, `T ≤ (k-2)(2k-3)/6` = **50, 88, 111** at `k` = 14, 18,
20, all below best-known. The argument survives replacing the Euclidean
reflection by any affine involution with a line of fixed points, since the
`-1`-eigendirection plays the role of "perpendicular". **Scope: geometric
reflections of straight lines.** It does not bound *table* automorphisms:
`kobon_19_107tri` has an order-2 automorphism with one fixed line, `p = c = 0`
and `T = 107`, against the 98 that the axis-in geometry would allow at `k = 19` —
which is to say, its realization is the axis-*absent* case with `f_perp = 1`,
untaxed.

T677's `k = 20` witness rebuilt in exact `Fraction` arithmetic: verticals
`x = -97, 3`, nine listed rational-slope mirror pairs, `T = 51`, exactly one
parallel pair, zero concurrent triples, `s_mirror = 1` — **and the fixed triangle
is `{x=-97, ℓ_4, ℓ_4'}`, on the far vertical, confirming T678's correction of
T677's attribution.**

**(g) The families nobody built.** Axis-absent, `f_perp = 0`: `k/2` seed lines
plus their `y → -y` mirrors, no vertical, no line on the axis. No fixed line, so
no fixed triangle, so `T` even — matching the even targets at `k = 14` and 18.
No forced parallel and no forced concurrence, so `B = k(k-2)` in full.

    k=14   40 restarts x 3000 steps   hist {44:1, 46:9, 48:8, 50:15, 52:7}
           best T = 52, fixed = 0, exact-confirmed, one of seven at 52:
           (162,252,-149) (225,-102,32) (-19,-153,-79) (-54,55,-84)
           (58,-82,43) (-135,-32,24) (-1,109,-10)
           (each seed (a,b,c) gives the pair a x + b y = c and a x - b y = c)
           T even in 40 of 40 and fixed triangles 0 in 40 of 40 -- T675's
           parity law on 40 independent objects.  A deeper re-anneal from the
           seven 52-witnesses (15 reps x 8000 steps) never leaves 52.
    k=18   40 restarts x 4000 steps   hist {78:5, 80:10, 82:7, 84:8, 86:4,
                                            88:5, 90:1}
           best T = 90, fixed = 0, exact-confirmed
           (138,-61,-100) (-13,82,-65) (6,336,-15) (88,-80,3) (35,37,-75)
           (-133,87,38) (44,71,15) (116,-44,17) (-58,-10,61)

90 at `k = 18` and 52 at `k = 14`, in a family with no budget tax at all, from
first sweeps.

And the `f_perp = 2` family at `k = 20`, which `kobon_20_116tri` belongs to and
which T678 priced from 120 unoptimised random draws at "best 79, mean 56.3": two
fixed verticals plus nine mirror pairs, annealed 30 x 5000. The first eight
restarts give

    107, 103, 95, 101, 97, 96, 101, 105     s_mirror = 1 in seven of eight

**Best 107 with `s_mirror` odd, on the first restart.** T679's methodological
objection to T678 is correct and this is its size: 79 from 120 draws, 107 from
one annealed restart, in the family that contains the 116-triangle record.

**(h) T690's single-variable test, reproduced.** Per-orbit `dist² = c²/(a²+b²)`
on T685's 91-witness: `[1.007, 14.019, 13.954, 0.009, 0.611, 0.151]` — the fixed
orbit is nearest at 0.009 and the two farthest are a near-tie, as T690 reports.
Perturbing orbit 2's `c` alone:

    c = 15,20 -> T=73     c = 39 (baseline) -> T=91, d=[0,1,3,0,1,0]
    c = 25    -> T=67     c = 45 -> T=91, d unchanged
    c = 55,70,90 -> T=79, d=[2,5,6,2,1,1]      c = 120 -> 79   c = 160 -> 73

Identical to T690's reported ladder including the `d` vector at `c = 55`.

**(i) The `V(3,18)` concurrency test, reproduced and then swept.** T668 compared
one clean insertion pattern against the merged one over 3,000 paired trials and
got `{-1: 188, 0: 2812}`. The comparison depends on where the clean line goes:
placing it immediately beside the partner crossing instead of at T668's gap makes
the concurrent completion win by exactly 1 in **500 of 500** paired trials. The
question the route asks is whether the merge beats the *best* clean placement, so
I swept it exhaustively — all 19×19 = 361 clean gap pairs on rows 3 and 18, for
each of six random row-20 orders, 2,166 completions:

    row-20 order  concurrent   best clean over 361 placements   T668's gap
    0                108            108                            108
    1                108            108                            108
    2                107            107                            107
    3                107            107                            107
    4                107            107                            107
    5                108            108                            108

**The merge never beats the best clean placement and never loses to it.** It is
worth exactly zero, which is T668's direction stated in a form that does not
depend on the gap chosen. Best total anywhere in this experiment is 111; T668
reports 114; the target is 117. All of these are `validate`-only objects and so
are upper bounds, not constructions.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `k18-best-known-arrangement-is-a-c3-object` | 18 | **SETTLED (referee), VERIFIER RUN** | Reference data 51b. `kobon_18_93tri` has an order-3 table automorphism with **no fixed line** and six line-orbits `{1,8,13} {2,7,14} {3,9,15} {4,10,16} {5,11,17} {6,12,18}`, confirmed twice (rows match up to per-row reversal; the permutation fixes the whole 93-triangle set). One whole orbit of parallel pairs `(1,2) (7,8) (13,14)`, per-orbit participation `[14,15,16,16,16,16]`, `s = 0`, `B = 282`, `3T = 279`, `F = 3`. **Turns 669-690 searched this family for fourteen turns without testing the record for membership in it.** Reference data 34a excluded it by method. | T691 | T691 |
| `k20-best-known-arrangement-is-an-axis-absent-mirror-object-with-fperp-2` | 20 | **SETTLED (referee), VERIFIER RUN** | 51b. `kobon_20_116tri` has an order-2 automorphism fixing exactly lines `{1,2}` — which are exactly its only parallel pair, i.e. `f_perp = 2`, axis absent — with nine swapped pairs `{3,20} ... {11,12}`, `s_mirror = 2`, `B = 20·18 − 2 = 358`, `3T = 348`, `F = 10`. This is precisely the family T676, T677 and T678 argued over, with T676's `B = 358` arithmetic exact. **117 needs `F = 7` and `s_mirror` odd.** | T691 | T691 |
| `c3-k18-target-94-is-a-perfect-packing-in-the-p3-branch` | 18 | **SETTLED (referee), PROOF + verifier run** | 51c. `C3` parallel pairs come in orbits of 3, so `p ∈ {0,3,6,...}` and `B = 288 − 2p`; `3·94 = 282` forces `p ≤ 3`. `p = 0` needs `F = 6`; **`p = 3` gives `B = 282 = 3·94` exactly, so 94 is a perfect packing** — the shape realized in this corpus at `k = 9, 12, 15, 21` (twice) and `27`. The record lives in the `p = 3` branch at `F = 3`. Both agents searched only `p = 0`. | T691 | T691 |
| `mirror-axis-in-arrangement-caps-below-best-known-14-18-20` | 14/18/20 | **SETTLED (SILVER), PROOF, T674 -> T675, referee-checked step by step** | 51f. `ℓ` not parallel to axis `A` meets `A` at `p`, and `ℓ'` passes through `p`, so `{ℓ,ℓ',A}` is forced concurrent; an `f`-fold vertex costs `f(f−2)` segments, so 3 per pair and merging is never cheaper; a pair parallel to `A` costs 6 and `f_perp = 3` costs 6, both saving only 3. Hence `f_perp = 1, f_par = 0, m = (k−2)/2` and `T ≤ (k−2)(2k−3)/6` = **50, 88, 111** at `k = 14, 18, 20**, all below best-known 53, 93, 116. Survives replacing the reflection by any affine involution with a fixed line. **Scope: geometric reflections of straight lines only** — `kobon_19_107tri` has a *table* order-2 automorphism with one fixed line, `p = c = 0` and `T = 107` against this argument's 98 at `k = 19`, because its realization is the axis-absent case. | T674 | T691 |
| `mirror-axis-absent-f-perp-zero-forces-even-t` | all | **SETTLED (T675), PROOF + verifier run** | An order-2 map permutes a triangle's three sides, and an involution on an odd set has a fixed point, so a fixed triangle needs a fixed line; `f_perp = 0` has none, so every triangle is in a 2-orbit and `T` is even. 51g: **40 of 40** independently annealed `k = 14` objects even with zero fixed triangles, plus T675's own 7. Kills `k = 20` (117 odd) in this slice; leaves `k = 14` (54) and `k = 18` (94) untouched **and untaxed**. | T675 | T691 |
| `mirror-f-perp-zero-even-k-family-is-untaxed-and-was-never-built` | 14/18 | **CONTESTED (construction, referee-built, 52 at k=14)** | 51g. No fixed line, no forced parallel, no forced concurrence: `B = k(k−2)` in full, and `T` even matches both targets. Named by T675 in the same turn it was abandoned for three turns of `k = 20`. Referee's first sweep: `k = 14`, 40 restarts × 3000, hist `{44:1,46:9,48:8,50:15,52:7}`, **best 52** (best known 53, target 54), seeds printed; `k = 18`, best 88. Nobody in 691 turns had built one at an open case. | T691 | T691 |
| `axis-absent-mirror-fperp2-s-mirror-can-be-odd-at-k20` | 20 | **SETTLED (T677 -> T678), VERIFIER RUN** | 51f. Verticals `x = −97, 3` and nine rational-slope mirror pairs: `k = 20`, `T = 51`, one parallel pair, zero concurrent triples, `s_mirror = 1`. Met T676's falsifier exactly as stated. **The fixed triangle sits on the far vertical `x = −97`, not `x = 3`** — T678's correction of T677's attribution is right, and the magnitude is unaffected. | T677 | T691 |
| `mirror-axis-absent-fperp2-nesting-cap-equals-fperp` | 20 | **REFUTED (T677), conceded by its proposer at T678** | T676 built five instances all giving `s_mirror = f_perp = 2` and proposed a nearest-pair-uncut mechanism. It assumed the fixed verticals sit symmetrically about the pairs' apexes; move one far away and its candidate is swallowed by a nearer pair. | T676 | T691 |
| `mirror-axis-absent-fperp2-family-needs-superoptimal-budget-efficiency` | 20 | **CONTESTED — the ceiling it rests on was a sampling artefact** | T678 priced the family from 120 unoptimised random draws (best 79, mean 56.3) and argued 117 needs 98.04% segment efficiency against the unconstrained 97.50%. The efficiency arithmetic is right. The ceiling is not: 51g reaches **107 with `s_mirror = 1` on the first restart** of a 30×5000 anneal, and 51b shows the 116-triangle record is itself in this family. | T678 | T691 |
| `weak-random-sampling-underestimates-a-symmetric-family-ceiling` | all | **SETTLED (referee), VERIFIER RUN** | T679's methodological objection to T678, now priced. Same family, same `k`: 120 random draws give 79; one annealed restart gives 107; the corpus record in that family is 116. A mean over unoptimised draws is not a ceiling. T679 was right and T678's own 79 was the evidence. | T679 | T691 |
| `k19-mirror-axis-is-a-label-reflection` | 13/19/all | **SETTLED (referee), VERIFIER RUN — refutes T673** | 51b. `i + j ≡ 2 (mod 19)` fixes line 1, pairs `2↔19, 3↔18, ...`, and maps `kobon_19_107tri`'s 107-triangle set onto itself exactly, with one fixed line and one fixed triangle. Same form at `kobon_13_m_sym_47tri` (`i + j ≡ 2 mod 13`, 34b's `i -> 15-i`), `kobon_21_133tri_3`, `kobon_25_191tri`; `kobon_7` at `i + j ≡ 6 (mod 7)`. **T673's "none matched, for all 19 shifts, both orientations" required all rows to reverse together; per-row reversal is a free re-orientation of one line.** | T691 | T691 |
| `corpus-automorphism-census-excluded-every-open-case-record` | all | **SETTLED (referee), VERIFIER RUN** | 51b. Reference data 34a excluded tables with unequal row lengths — `kobon_14_53tri`, `kobon_16_72tri`, `kobon_18_93tri`, `kobon_20_116tri`, `kobon_22_143tri` — which are exactly the parallel-bearing tables and exactly the best-known arrangements at the open cases. Anchoring the `2k`-candidate match on any full-length row fixes it. `kobon_14_53tri`, `kobon_16_72tri`, `kobon_22_143tri`, `kobon_12_38tri` are genuinely asymmetric; the other two are not. | T691 | T691 |
| `c3-central-face-is-bounded-with-3m-sides-and-m-1-iff-s-1` | 18 | **SETTLED (T688 + referee), PROOF + verifier run; scope `p = c = 0`** | 51d. In a simple `C3` arrangement `O` is in no line (two lines through `O` would be a 2-set the order-3 action must fix pointwise), so `O` lies in one face; a convex face fixed by `M` contains the average of a point orbit, hence `O`, so the fixed face is unique; `2k = 36 ≡ 0 (mod 3)` and `35 ≢ 0` force it bounded; no edge is fixed, so its side count is `3m`. Measured 3/3/3/3/3 on the five `s = 1` witnesses and 6/6 on the two `s = 0` ones. **T688 omitted the simplicity hypothesis — T679's own `c = 1` witness has an `M`-orbit of three lines through `O`.** | T688 | T691 |
| `central-face-distance-sort-predicts-s` | 18 | **REFUTED (referee), VERIFIER RUN** | 51d. T689: "a distance sort instead of a full triangle enumeration to know `s` in advance." T682's 93 and T669's 84 both have their three nearest lines forming a single orbit and `s = 0`; the nearest orbit bounds the central face as part of a hexagon. T689's close/far construction (3 sides in 20 of 20) is a different and correct claim and used the clip, not the sort. | T689 | T691 |
| `c3-k18-93-triangle-simple-witness` | 18 | **SETTLED (T682, referee-reproduced + twice rediscovered), VERIFIER RUN** | 51a, 51c. Seeds `(-44,-10,24)(1,-6,38)(1,7,37)(36,19,3)(14,6,76)(48,-12,10)`: `T = 93`, `p = 0`, `c = 0`, 18 distinct, `s = 0`, `d_i = [0,2,1,0,0,0]`, `B = 288`, `F = 9`. A **new simple 18-line 93-triangle arrangement** — the published record has `p = 3` — and my own 60×3000 sweep hits 93 twice more from independent random starts. Matches best-known; does not beat it. | T682 | T691 |
| `c3-k18-91-is-the-ceiling-for-s-equals-1` | 18 | **CONTESTED (search result, seven methods, referee's included)** | Joint anneal 91 (T681, T685); freeze-batch 88 (T686); single-seed transplant ≤91 (T687); `require_s1` from three basins ≤91 (T683); `k=21` orbit deletion 85 (T687); near/far construction 79 (T689); referee's 60×3000 `s = 1` sweep, best 91 (51c). Every route lands at or below 91 and none at 92. **Search result. Not a bound.** 94 needs `s = 1` and `Σd_i = 2`. | T683 | T691 |
| `c3-k18-fixed-orbit-degree-deficit-8-for-8` | 18 | **REFUTED (T685), conceded by its proposer at T686 on an independent rebuild** | 51a. T684 called an 8-witness pattern "an 8-for-8 fact now, not a guess" and derived from it that the other five orbits must sum to `≤ 1`. T685's witness — one coefficient off T681's — has the fixed orbit (orbit 3) at participation 16, `d_i = 0`, at the same `T = 91`. The total deficit moved rather than dropped: `[0,1,2,1,1,0]` to `[0,1,3,0,1,0]`. | T684 | T691 |
| `c3-k18-94-requires-s-flip-from-0-to-1` | 18 | **SETTLED (T682), ARITHMETIC** | `T ≡ s (mod 3)` and `s ≤ 1` (32e, 34b, 50d) with `94 ≡ 1` force `s = 1` exactly, and the best `s = 0` object is 93 while the best `s = 1` object is 91. Going 93 → 94 is not a perturbation; it is a discrete change in whether one line-orbit bounds the central face. Sharpened geometrically at T688: the central face must literally be a triangle. | T682 | T691 |
| `single-line-deletion-from-optimal-k-plus-1-undershoots-known-best-by-2` | all | **REFUTED (referee), VERIFIER RUN** | 51e. T672's law from three bases (70/91/114, deficit 2 each), conceded by T673 without the control. The control: `kobon_20_116tri` minus line 2 gives **`T' = 107 = N(19)`, deficit 0**, and `kobon_18_93tri` gives max 79 against `N(17) = 85`, **deficit 6**. The deficit is base-dependent and ranges 0 to 6. | T672 | T691 |
| `k19-single-line-deletion-yields-18-line-91-triangle-arrangement` | 18 | **SETTLED (T671, referee-reproduced), COMPLETE ENUMERATION** | 51e. All 19 deletions of `kobon_19_107tri`: `{90: 17, 91: 2}`, the two at `x = 3, 18`; every result validates, is bracket-free and full-length, so `p = c = 0`. T671's `C(21,3) = 1330` sweeps reproduce exactly (86/87/88). Referee addition: `C(20,2)` on `kobon_20_116tri` also reaches **91** at `{2,4}`. | T671 | T691 |
| `flip-search-caps-deletion-family-at-t0-both-k16-and-k18` | 16/18 | **CONTESTED (search result, correctly labelled)** | T673: annealed flip search with decrease tolerance from `kobon_17_85tri − 1` (T0 = 70, 300×4) and `kobon_19_107tri − 3` (T0 = 91, 350×5) never exceeds the start. Same shape as T670's zero-accepted-moves result in the `C3` basin at 84. | T673 | T691 |
| `v318-merge-is-worth-exactly-zero-against-the-best-clean-placement` | 20 | **SETTLED (T668 + referee sweep), COMPLETE ENUMERATION over placements** | 51i. T668: 3,000 paired trials, `{-1: 188, 0: 2812}`, concurrent never wins. The sign depends on the clean gap — placed beside the partner instead, the concurrent completion wins by 1 in 500 of 500. Swept exhaustively instead: all 361 clean `(g3,g18)` pairs for each of six row-20 orders, 2,166 completions — **concurrent equals the best clean placement in all six and never exceeds it.** Both are `validate`-only objects, so this is an upper bound on the clean side. | T668 | T691 |
| `concurrency-through-existing-vertex-escapes-the-parity-floor` | all | **DEAD (referee) — buried with reason after five assignments** | T621's deficit 192 and T636's deficit 44 at the same vertex on the same base were never reconciled; T668 reported, correctly and in writing, that the derivations do not survive in this file and declined to reconstruct them. Both numbers are recorded as irrecoverable. The route itself is answered by 51i on a directly relevant instrument: the merge is worth zero against the best clean placement, and the best total anywhere in the experiment is 114 (T668) or 111 (referee) against 117. | T585 | T691 |
| `v3-18-corrected-parity-deficit-depends-on-row-20-not-the-vertex` | 20 | **DEAD (referee) — the two numbers are unreconstructable** | T621 192, T636 44, T625 a third pair, T588's ±700 swing on row order. The sweep was assigned at T643, T667 and (as item 2) T667 again. T668 declined it with a reason rather than fabricating a method. Recorded dead with the reason rather than carried a fourth time. | T643 | T691 |
| `rotational-symmetry-of-order-m-at-least-3-forces-m-divides-k` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 50b, 32b. An affine map of order `m ≥ 3` has no real eigenvalue, hence no fixed line; the same argument runs combinatorially on a table. `3 ∤ 13`, `3 ∤ 20`. | T345 | T667 |
| `order-3-at-k18-is-the-only-rotationally-symmetric-family-alive-at-any-open-case` | 14/18/20 | **SETTLED (referee), PROOF; reference data 32d/32e** | Every rotational family at every open case is dead except `C3` at `k = 18`, which 51b now shows contains the published record. Reflections are a separate family and are live at all three cases; see the mirror rows above. | T345 | T691 |
| `point-symmetric-arrangements-have-even-triangle-count` | all | **SETTLED (SILVER), PROOF, T664 -> T665, referee-verified** | Reference data 50 preamble, 667(a). | T664 | T667 |
| `c3-k18-optimum-would-have-exactly-one-centred-orbit-triangle` | 18 | **SETTLED (referee), PROOF + verifier run** | Reference data 50d: `s` histogram `{0: 171, 1: 126}` over 297 random `C3` objects, never 2; with `94 ≡ 1 (mod 3)`, `s = 1` exactly. Sharpened at T688 into a statement about the central face. | T667 | T691 |
| `c3-k18-coordinate-family-is-rationally-realizable` | 18 | **SETTLED (T666 + the whole 669-690 chain), VERIFIER RUN** | `M = [[0,1],[-1,-1]]` has `M³ = I`, `det = 1`, rational entries, so every orbit-built object is stretchable by construction — no table, no pseudoline gap. Nine objects built and reproduced at 51a, best 93. | T666 | T691 |
| `mirror-and-dihedral-symmetry-are-unexamined-at-every-open-case` | 14/18/20 | **CLOSED (referee) — worked at T674-T678 and T691** | Superseded by the five mirror rows above. Axis-in is dead by proof; axis-absent `f_perp = 0` is untaxed and live at `k = 14, 18`; axis-absent `f_perp = 2` is the family containing the `k = 20` record. | T667 | T691 |
| `open-case-records-are-three-free-segments-over-budget` | 14/18/20 | **SETTLED (referee), VERIFIER RUN — reconfirmed exactly at T691** | 51b/51c. `kobon_14_53tri` `B = 162`, `F = 3`, and 54 needs `F = 0`. `kobon_18_93tri` `B = 282`, `F = 3`, and 94 needs `F = 0`. `kobon_20_116tri` `B = 358`, `F = 10`, and 117 needs `F = 7`. **Three over, in all three cases, on the nose.** | T543 | T691 |
| `k19-flip-ball-radius-2-has-two-t106-tables-and-neither-carries-an-extremal-free-gap` | 20 | **SETTLED (T661 + T662, referee-reproduced), COMPLETE ENUMERATION** | Reference data 50a. | T661 | T667 |
| `mutual-extremal-free-pairs-are-common-two-triangles-below-the-optimum` | all | **SETTLED (T661, referee-reproduced), VERIFIER RUN** | 50a. | T661 | T667 |
| `extremal-free-gap-rate-is-an-optimality-effect-not-an-obstruction` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 50f, 1.8 million gaps. | T601 | T667 |
| `coverage-fractions-are-denominated-against-a-space-nobody-searched` | all | **SETTLED (referee), COMPLETE ENUMERATION** | Reference data 50e: A006245 at `k = 4..7`. | T667 | T667 |
| `flip-graph-on-simple-arrangements-is-connected-so-b-reaches-every-k13-order-type` | 13 | **SETTLED (referee), COMPLETE ENUMERATION at k <= 7** | 50e. | T667 | T667 |
| `t648-spread-incidence-numbers-are-not-produced-by-any-run` | all | **SETTLED (T649 -> T650), VERIFIER RUN** | | T649 | T667 |
| `extremal-row-position-does-not-tax-per-line-triangle-incidence` | all | **SETTLED (SILVER), T647 -> T650 -> T651, referee-reproduced** | Reference data 50g. | T647 | T667 |
| `t644-fan-buys-the-criterion-with-a-twelve-fold-concurrency` | 13 | **SETTLED (T645 -> T646), VERIFIER RUN** | | T645 | T667 |
| `k13-simple-arrangement-realizes-mutual-extremal-free-gap-pair` | 13 | **SETTLED (T646 + T647 + referee), VERIFIER RUN** | 50g. `T = 11` — satisfying the criterion is cheap and buys nothing. | T646 | T667 |
| `criterion-pair-survives-single-line-deletion-in-kobon14-53tri-family` | 13/14 | **SETTLED (T652 + T653), VERIFIER RUN** | 50g. | T652 | T667 |
| `k14-deletion-family-p-is-two-or-three-by-pair-membership` | 14 | **SETTLED (T653 -> T654), VERIFIER RUN** | | T653 | T667 |
| `x8-completion-space-to-p0-is-exhausted-and-caps-at-43` | 13/14 | **SETTLED (T655 -> T656, referee-reproduced), COMPLETE ENUMERATION** | 50g, 20,736 combinations. | T655 | T667 |
| `x8-minimal-patch-completion-freezes-nine-non-target-rows` | 13/14 | **CONTESTED (scope objection, partly answered by T660)** | | T656 | T667 |
| `free-row-random-shuffle-collapses-far-below-baseline` | 13/14 | **SETTLED (T660), VERIFIER RUN** | | T660 | T667 |
| `sat-tooling-is-absent-from-this-environment` | all | **SETTLED (T660, self-reported), VERIFIER RUN** | | T660 | T667 |
| `criterion-hard-clause-sat-instance-for-k13-second-optimum` | 13 | **DEAD (no solver in this environment)** | | T658 | T667 |
| `flip-distance-floor-requires-minimising-over-relabellings` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 49c. | T643 | T643 |
| `t637-flip-distance-floor-of-22-and-60` | all | **DEAD (abandoned)** | | T637 | T667 |
| `per-flip-triangle-symmetric-difference-is-at-most-three` | all | **REFUTED (referee), VERIFIER RUN** | Reference data 49b. | T637 | T643 |
| `escape-reduces-to-a-second-k13-order-type` | 13/14 | **CONTESTED — six independent search families, all empty; reachability settled** | 50e says the target is reachable from `B` by flips and the space has order `10^18`. **T691 adds the lever nobody used: `B` is mirror-symmetric under `i + j ≡ 2 (mod 13)` (51b), so the `σ`-equivariant flip subgraph is walkable far past radius 3.** | T368 | T691 |
| `suboptimal-19-line-base-at-t106` | 20 | **CONTESTED — object built, and it is the wrong shape** | 50a. | T589 | T667 |
| `k13-flip-ball-radius-3-from-b-contains-no-second-t47` | 13/14 | **SETTLED (T619, referee-reproduced), COMPLETE ENUMERATION** | Reference data 49i. | T619 | T643 |
| `k18-t84-absent-in-flip-ball-radius-2-from-k17-optimum` | 18 | **SETTLED (T620, referee-reproduced), COMPLETE ENUMERATION** | Reference data 49h. | T620 | T643 |
| `deletion-derived-k13-subarrangements-of-optima-miss-47` | 13/14 | **SETTLED (T633 + T635), COMPLETE ENUMERATION** | 233,002 subsets. | T633 | T643 |
| `b-flip-component-has-one-basin-under-directed-ascent` | 13/14 | **CONTESTED (search result, strong) — scope tightened at T667** | | T631 | T667 |
| `bfs-frontier-decay-is-not-diagnostic-of-a-hidden-second-peak` | all | **CONTESTED — raised at T631, never answered through T690** | | T631 | T643 |
| `base-manufactured-concurrence-caps-tamura-below-target-at-k13-k19` | 13/19/14/20 | **SETTLED (SILVER), PROOF, T624 -> T625** | | T624 | T643 |
| `f-fold-vertex-touch-pair-count-is-f-or-c-f-2-nobody-knows` | all | **CONTESTED (referee)** | | T643 | T643 |
| `single-2fold-vertex-touch-correction-capped-at-n-minus-2` | all | **SETTLED for `f = 1` (T622); REFUTED as stated (T623)** | | T622 | T643 |
| `multi-touch-budget-does-not-stack-additively` | 20 | **SETTLED (T625, self-refuted), VERIFIER RUN** | | T625 | T643 |
| `table-validate-accepts-a-row-listing-the-same-label-twice` | all | **SETTLED (T636, self-reported), VERIFIER RUN** | | T636 | T643 |
| `k14-calibration-parallel-slack-is-incidental-not-load-bearing` | 14/15 | **SETTLED (T626, referee-reproduced), VERIFIER RUN** | Reference data 49j. | T599 | T643 |
| `tamura-tight-extremal-gap-census-is-four-records-not-fifteen` | all | **SETTLED (referee); subsumed by 50f** | | T643 | T667 |
| `ray-adjacent-segments-are-freed-less-often-than-interior-ones` | all | **SETTLED (referee), VERIFIER RUN — direction confirmed, obstruction reading dead** | Reference data 50f. | T640 | T667 |
| `extremal-free-gap-never-observed-at-p-prime-zero` | all | **DEAD (superseded by 50f)** | | T601 | T667 |
| `raw-coordinate-hillclimb-caps-at-41-in-bounded-budget` | 13 | **CONTESTED (tiny search, correctly labelled)** | | T635 | T643 |
| `k17-k19-k21-optimum-subarrangement-ceiling-flat-not-rising-with-k` | all | **CONTESTED (pattern over three objects)** | | T635 | T643 |
| `triangle-flip-is-the-validity-preserving-mutation-single-row-swap-is-not` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 48a, 50e. | T618 | T667 |
| `k18-t84-swap-variants-are-not-arrangements` | 18 | **REFUTED (referee), VERIFIER RUN** | | T618 | T618 |
| `no-single-flip-of-the-k17-optimum-reaches-84` | 18 | **SETTLED (referee), COMPLETE ENUMERATION** | | T618 | T618 |
| `optimum-is-a-strict-local-max-in-the-flip-graph-by-two` | 13/17/21 | **SETTLED (referee); scope: optima only** | | T618 | T643 |
| `base-floor-overcounts-on-bases-with-parallels-or-concurrences` | all | **SETTLED (referee), VERIFIER RUN** | Reference data 48d. | T617 | T618 |
| `zero-floor-criterion-survives-parallels` | all | **SETTLED (referee), VERIFIER RUN** | | T618 | T618 |
| `phi-is-a-lower-bound-on-total-parity-violations` | all | **SETTLED (referee), PROOF** | | T618 | T618 |
| `l-inclusive-parity-count-reaches-zero-on-good-fb-for-calibration-object` | 14/15 | **SETTLED (T598), THREE INDEPENDENT VERIFIER RUNS** | | T598 | T618 |
| `calibration-extension-is-happens-before-acyclic` | 14/15 | **SETTLED (referee), VERIFIER RUN** | | T610 | T618 |
| `l-inclusive-between-set-sum-invariant-equals-c-n-3` | all | **SETTLED (T598 -> T599), PROOF + verifier run** | | T598 | T618 |
| `phi-zero-does-not-imply-l-containing-triples-are-clean` | 14 | **REFUTED (referee)** | | T609 | T618 |
| `p0-criterion-pair-unattested-in-corpus` | all | **SETTLED (T600-T603); scope corrected at T667** | | T600 | T667 |
| `synthetic-p0-base-construction-is-vacuous-without-real-geometry` | all | **SETTLED (T600, self-reported)** | | T600 | T618 |
| `b-fails-mutual-extreme-criterion-under-every-reorientation` | 13/14 | **SETTLED (SILVER), PROOF, T605 -> T606** | | T605 | T618 |
| `i3-zero-floor-criterion-derived-and-cross-verified` | all | **SETTLED for parallel-free cuts; UNTESTED at `p > 0` and ABANDONED** | Killed at T667. | T606 | T667 |
| `i3-condition1-is-O1-not-On` | all | **SETTLED (SILVER), T608 -> T609** | | T608 | T618 |
| `kissat-pair-selection-is-unpriced-disjunction-not-a-flag` | 20 | **SETTLED (T607 -> T608); moot (T660)** | | T607 | T667 |
| `base-only-floor-decomposes-by-interior-count-each-piece-independently-zero` | all | **SETTLED (T594), PROOF** | | T594 | T618 |
| `zero-floor-criterion-is-mutually-extremal-free-gaps` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 47c. | T593 | T618 |
| `one-interior-row-insertion-is-dead-for-every-base` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 47b. | T593 | T618 |
| `base-only-parity-floor-depends-only-on-interior-rows` | all | **SETTLED (T582 -> T584, referee), PROOF + verifier run** | | T582 | T618 |
| `b-and-k19-optimum-fail-the-zero-floor-criterion` | 14/20 | **SETTLED (referee), VERIFIER RUN** | | T582 | T618 |
| `zero-floor-criterion-is-satisfiable` | all | **SETTLED (referee), VERIFIER RUN; second witness at T646** | | T593 | T667 |
| `k18-t84-reinsertion-caps-at-93-in-the-swap-neighbourhood` | 18 | **DEAD (referee) — the 34 objects are not arrangements** | | T570 | T618 |
| `k18-t84-base-only-floor-positive-across-swap-neighborhood` | 18 | **DEAD (referee) — same 34 objects** | | T595 | T618 |
| `k18-t84-flank-closure-is-exactly-two-of-three` | 18 | **DEAD (referee) — same 34 objects** | | T572 | T618 |
| `k18-t85-base-cannot-extend` | 18 | **SETTLED (referee), PROOF, no search** | | T568 | T618 |
| `k19-optimum-base-admits-no-extension-to-117` | 20 | **SETTLED (T582-T584 + T591, referee-verified)** | | T569 | T618 |
| `k20-q1d0-and-q0d1-families-dead-by-exhaustive-count` | 20 | **SETTLED (T571, T591, T608)** | | T571 | T618 |
| `jordan-parity-necessary-condition-beyond-reciprocity` | all | **SETTLED (referee-verified), PROOF + verifier run** | | T492 | T618 |
| `jordan-parity-naive-check-undercounts-at-vertex-touches` | all | **SETTLED (SILVER), PROOF + verifier run** | | T533 | T593 |
| `happens-before-acyclicity-is-necessary-and-orientation-dependent` | all | **SETTLED (T566, amended by referee)** | | T566 | T618 |
| `table-validate-checks-only-reciprocity` | all | **SETTLED (referee-verified from source)** | Reference data 37. | T441 | T643 |
| `validate-only-search-outputs-are-not-arrangements` | all | **SETTLED (T541-T544, referee-accepted)** | Load-bearing again at 51i. | T541 | T691 |
| `insertion-degree-bound` | all | **SETTLED for bracket-free bases only; REFUTED as published** | | T568 | T593 |
| `insertion-degree-bound-fails-on-bases-with-preexisting-brackets` | all | **SETTLED (T575 -> T576), VERIFIER RUN** | | T575 | T593 |
| `vertex-routing-into-bracket-free-base-is-worth-nothing` | all | **SETTLED (T576 -> T577), conceded by the proposer** | | T575 | T593 |
| `deletion-bound-forbids-a-too-good-base` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 46b. | T568 | T593 |
| `k-equiv-1-mod-6-optimum-forces-f-equals-2` | all | **SETTLED (T592, referee-amended)** | | T592 | T593 |
| `optimum-at-fixed-k-need-not-be-a-unique-order-type` | all | **SETTLED (T573), VERIFIER RUN; reinforced at T691** | `kobon_21_133tri_1/2/3`, and now a second 93-triangle `k = 18` arrangement (`p = 0` against the record's `p = 3`, 51a). | T573 | T691 |
| `kobon14-53tri-contains-no-47-triangle-sub-arrangement` | 13/14 | **SETTLED (T573), VERIFIER RUN** | | T573 | T667 |
| `per-line-edge-cap-and-free-segment-decomposition` | all | **SETTLED (referee), PROOF + verifier run** | Reference data 45a-b. Load-bearing at 51c and 51f. | T543 | T691 |
| `f-cannot-be-read-off-b-minus-3t-when-a-row-carries-a-bracket` | all | **SETTLED (T548 -> T549), VERIFIER RUN** | | T548 | T568 |
| `b-admits-no-14-line-extension-to-54` | 14 | **SETTLED (referee), PROOF** | | T568 | T618 |
| `t560-and-t566-54-tables-are-not-arrangements` | 14 | **SETTLED (T567 + referee), VERIFIER RUN** | | T567 | T568 |
| `append-route-dead-at-all-three-open-cases-by-arithmetic` | 14/18/20 | **SETTLED (referee), corollary of 46a** | | T543 | T568 |
| `tail-append-outputs-are-parity-clean-at-every-base` | 14/18/20 | **SETTLED (referee), VERIFIER RUN** | | T518 | T593 |
| `b-double-free-gap-family-capped-at-53-for-any-row14` | 14 | **SETTLED (T559)** | | T558 | T593 |
| `b-free-gap-endpoints-are-one-sided-extreme-not-mutual-last` | 14 | **SETTLED (T554)** | | T554 | T593 |
| `hard-gated-single-line-search-finds-zero-headroom-over-valid-seed` | all | **CONTESTED (search result)** | | T544 | T568 |
| `native-concurrency-at-named-free-gap-nets-negative-on-kobon14` | 14 | **CONTESTED (parity never reported)** | T551's demand is still unmet, 140 turns later. | T550 | T691 |
| `single-line-extension-face-lemma` | all | **SETTLED (referee-verified)** | | T437 | T543 |
