# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 126. Turns 102-126 audited.

Three things happened in this cycle. Turns 103-108 finished the local program at
V(11,12) and were good. Turns 109-116 spent eight turns pricing the
realizability of a table edit that turned out to be worth minus three triangles,
a number four lookups away at any point. Turns 119-126 opened a second witness,
Suzuki's k=15, and converged on a deletion count of 52 through a chain of
concessions that read beautifully and rests on a proof with an off-by-one in it.

The referee's findings, all reproducible from rows cited by line number:

1. **Bader's free-segment census has been complete since turn 118 and neither
   agent noticed.** Turn 103 found two, turn 118 found the third, the budget
   says there are exactly three. They form a **connected three-edge path**.
   See `bader-three-free-segments-form-a-path`.
2. **Turn 121's fusion lemma miscounts by one side.** A merged face has `m-1`
   sides, not `m`, so a quadrilateral on the far side of a deleted segment does
   collapse to a triangle. Deletion can create triangles. Turn 122 endorsed the
   error with a "sharper derivation," turns 123-124 banked it, turn 124
   generalized it into a false law. The referee ran the twelve candidate merges
   for Suzuki's line 15; all twelve fail, so 52 survives. The law does not.
   See `deletion-identity-is-T-minus-deg-plus-R`.
3. **Suzuki's k=15 arrangement is triangle-degree-regular at 13 by arithmetic,
   not by sampling.** Turn 125 called three matching computations "strong
   evidence" of a fact that follows in one line from the segment budget already
   in this ledger. See `tamura-tight-implies-every-line-saturated`.
4. **Kabanovitch's k=13 table read and swept.** p = 0, agenda item 4's
   prediction confirmed; exactly two free segments, both interior; all 26
   extremal segments carry triangles; fifteen triangles named. Reference data 6.

---

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

Thirteen from turns 97 and 100:

    {2,3,7} {4,5,7} {4,6,7} {8,9,10} {1,4,11} {1,12,14} {2,11,14}
    {3,5,11} {6,8,11} {7,9,11} {7,10,11} {1,12,13} {2,11,13}

Two from turn 103: `{2,8,12}`, `{2,8,13}`. One from turn 116: `{3,8,11}`.
Eight from turn 117, line 1's remaining segments:

    {1,7,13} {1,7,10} {1,6,10} {1,6,9} {1,3,9} {1,3,8} {1,5,8} {1,5,11}

Three from turn 118, line 8's remaining segments: `{4,8,13}`, `{4,8,14}`,
`{5,8,14}`. Referee re-verified all twenty-seven. Twenty-six unnamed.

## Referee reference data 3: face F, a pentagon

Unchanged from the last cycle. F is the face inward of V(11,12):

    F = pentagon  V(11,12) - V(11,13) - V(2,13) - V(2,8) - V(8,12)
    sides on lines 11, 13, 2, 8, 12; all five crossing-free.

Derived by three local arguments from the table alone, no coordinates. The
half-plane transfer step: lines 12 and 13 meet line 11 exactly once each, at the
first entry of rows 12 and 13, so their forward portions, which share V(12,13),
lie in the same open half-plane of line 11.

## Referee reference data 4: the parallel-pair budget

For k lines, p parallel pairs, no concurrences: `V = C(k,2) - p`, `E = 2V + k`,
bounded segments `B = k(k-2) - 2p`. Tamura's argument runs segment by segment: a
bounded segment on line a with endpoints V(a,b), V(a,c) is a side of at most one
triangular face, namely {a,b,c}, on the side of a containing V(b,c). Hence

    T <= floor(B/3) = floor((k(k-2) - 2p)/3)      and      sum_l deg_T(l) = 3T

where `deg_T(l)` is the number of triangles with a side on l, bounded above by
l's own bounded-segment count, which is (crossings on l) - 1.

At k = 14: p=0 gives 56, p=1 gives 55, p=2 and p=3 give 54, p=4 gives 53. Any
14-line arrangement with 54 triangles has **p <= 3**, and at p = 3 it has zero
slack: B = 162 = 54 x 3, so every bounded segment is a triangle side. Bader sits
at p = 3 with 53, so **exactly three** of its 162 bounded segments are free.

## Referee reference data 5: Bader's three free segments and the deficiency path

All three are now known and the census is closed.

    S1  line 11, row-11 positions 1-2    V(11,12) - V(11,13)   cand {11,12,13}
    S2  line 12, row-12 positions 1-2    V(12,11) - V(12,8)    cand {8,11,12}
    S3  line  8, row-8  positions 2-3    V(8,10)  - V(8,12)    cand {8,10,12}

S1 fails because 11,13 sit at row-12 positions 1 and 13. S2 fails because 12,8
sit at row-11 positions 1 and 9 and 12,11 at row-8 positions 3 and 11. S3 fails
because 8,12 sit at row-10 positions 1 and 5. Turn 103 found S1 and S2, turn 118
found S3, the budget says three, so there are no others.

**They form a connected path.** S1 and S2 meet at V(11,12); S2 and S3 meet at
V(8,12). The whole deficiency of this witness is the three-edge path

    V(11,13) --11-- V(11,12) --12-- V(8,12) --8-- V(8,10)

S1 and S2 are two adjacent sides of pentagon F; S3 hangs off F's corner V(8,12).
Each of the three has an unbounded face on its far side: at V(11,12) both of the
other half-edges are rays (it is the first entry of both rows 11 and 12), so
three of the four sectors there are unbounded, and the sector between S2 and S3
at V(8,12) is the continuation of one of them.

**The path is not a near-miss triangle.** The three free segments lie on lines
8, 11, 12 and the only triangle those three lines can bound is {8,11,12}, which
fails two of its three legs: row 11 has 12 at position 1 and 8 at position 9,
seven crossings apart, and row 8 has 12 at position 3 and 11 at position 11,
also seven apart. Closing this path is not a perturbation, it is a reordering of
seven crossings on each of two rows, which is exactly the size of edit turn 116
priced at minus three triangles.

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

All thirteen rows have twelve entries, no nesting: **p = 0, simple**. This is
agenda item 4's k=13 prediction (p <= 1) confirmed, and it fixes the numbers:
V = 78, E = 169, faces = 92, unbounded 26, bounded 66, triangles 47,
**non-triangular bounded faces 19**, bounded segments 143, of which 141 are
triangle sides and **exactly two are free**.

Referee's extremal sweep, 26 announcements, M = 11 mutual pairs and O = 4
orphans (2M + O = 26, turn 108's parity holds):

    mutual   (1,13) (1,2) (2,3) (3,4) (5,6) (6,7) (7,8) (8,9) (9,10) (11,12) (12,13)
    orphans  f(4)=9, f(5)=9, f(10)=6, f(11)=6

Every one of the eleven mutual vertices resolves, and all four orphans close:

    {1,9,13} {1,2,6} {2,3,9} {3,4,6} {3,5,6} {6,7,9} {1,7,8} {6,8,9}
    {9,10,12} {9,11,12} {6,12,13} {2,4,9} {5,7,9} {6,8,10} {6,11,13}

Fifteen of the forty-seven named, all 26 extremal segments accounted for, so
**both free segments of the k=13 optimum are interior**, exactly as at k=14.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Referee, reference data 5. Turn 103's two plus turn 118's one is three, the budget says exactly three, so the census is closed. They form the path V(11,13)-V(11,12)-V(8,12)-V(8,10) on lines 11, 12, 8. **This was true at turn 118 and neither agent said it.** Turn 118 wrote "the first free segment either of us has actually located" and "the remaining two free segments concentrated elsewhere" fifteen turns after its opponent located them and eleven turns after turn 107 correctly predicted the third would be interior. Turn 107's prediction and turn 118's find are the same object and nobody joined them. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | Referee. Three verified free segments give `3T <= 162 - 3`, so `T <= 53` for `kobon_14_53tri` independently of the corpus's own count field. Combined with 27 individually verified triangles, the table decoding of turn 84 is now confirmed from both directions. This is what agenda item 1 was for, obtained at a fraction of its cost. A **fourth** free segment would mean the corpus label is wrong; that is now the cheapest falsifier on the board. | T127 | T127 |
| `deletion-identity-is-T-minus-deg-plus-R` | 14/15 | **SETTLED (referee correction of T121, T122, T123, T124)** | Deleting line l from a simple arrangement gives `T' = T - deg_T(l) + R`, where R counts faces of the reduced arrangement that are triangles and were crossed by l. **R is not always zero.** Turn 121's proof that it is: "the merged face has exactly (1 fused a-edge) + (1 fused b-edge) + (F_right's remaining m-2 sides) = m sides." F_right's a-edge and b-edge are consumed by the two fusions, so what remains of F_right is `m-3` sides, not `m-2`, and the merged face has **m-1** sides. At m = 4 that is a triangle, and m = 4 is exactly the corner-clip configuration. Turn 122 called the m>=4 conclusion "a real derivation, not just the assertion turn 121 gave" and re-derived the same error. Turn 124 then generalized it: "the resulting 14-line count is exactly 65 - deg_T(l), with certainty and no slack, for every l." False. | T119 | T127 |
| `suzuki-minus-line15-is-52` | 14 | **SETTLED (referee computation, replacing T121's proof)** | The conclusion survives. A new triangle after deleting line 15 must use an adjacency created by the deletion, so it must be {a, x, y} where x, y flank 15 in row a. Twelve rows have 15 interior (rows 1 and 14 have it first). All twelve candidates fail: {2,8,10} (2,10 at row-8 positions 6,12), {3,8,9} (3,8 at row-9 positions 7,1), {4,10,14} (4,14 at row-10 positions 4,6), {5,11,12} (5,12 at row-11 positions 9,13), {6,9,12} (9,6 at row-12 positions 6,8), {7,11,13} (11,7 at row-13 positions 3,11), {2,3,8} (3,8 at row-2 positions 1,9), {3,6,9} (6,9 at row-3 positions 6,8), {2,4,10} (10,2 at row-4 positions 9,11), {5,7,11} (7,11 at row-5 positions 2,6), {5,6,12} (12,5 at row-6 positions 7,13), {1,7,13} (13,1 at row-7 positions 6,10), all after deleting 15 from the row. R = 0, so T = 65 - 13 + 0 = 52. Corpus lines 1350-1591. | T119 | T127 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | If a k-line arrangement attains `T = k(k-2)/3` then `p = 0` and `sum deg_T(l) = 3T = k(k-2)`, while each line has at most `k-2` bounded segments and so `deg_T(l) <= k-2`, with `k(k-2)` as the total. Equality forces **`deg_T(l) = k-2` for every line**. Suzuki's k=15 is degree-regular at 13 as a theorem. Turn 125 checked lines 1, 2 and 15 by hand, got 13 three times, and called it "strong evidence this arrangement is triangle-degree-regular" from three samples landing on a forced average. It was not evidence, it was a corollary of `parallel-pair-budget-for-54`, which was already in the ledger. Turn 126 accepted the framing ("a second data point for rigidity, not a stray coincidence") without noticing either. The row work was correct; the inference was the wrong shape. | T127 | T127 |
| `deletion-from-a-known-optimum-needs-R` | all | **CONTESTED (open, and now precisely posed)** | With the corrected identity, deleting line l from a k+1 optimum gives `T - (k-1) + R_l`. k=15 to 14: `52 + R`, needs R = 2 for 54. k=21 to 20: `114 + R`, needs R = 3 for 117. k=19 to 18: at most `92 + R`, needs R = 2 for 94. So the deletion route is **not** dead, contrary to what a reading of turn 121's lemma would give you; it is exactly as alive as R. R_15 = 0 for Suzuki. The other fourteen lines are unchecked and cost twelve lookups each. | T119 | T127 |
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **SETTLED (referee sharpening of T126)** | Turn 126's correction of turn 125 is right and is the best turn of the cycle: clipping a corner off a triangular face destroys one and creates one, net zero, so destructions are not a separate budget to net against. Exact form: inserting a generic line l into an arrangement B gives `T' = T(B) + Y` where Y counts l's chords that clip a corner off a **non-triangular** face, and `deg(l) = X + Y` where X counts triangular faces l crosses. l has 12 bounded chords at k=13, so to reach 54 from 47 you need **Y = 7 and X <= 5**: the inserted line must corner-clip seven of Kabanovitch's **nineteen** non-triangular bounded faces while crossing at most five of its forty-seven triangles. Turn 125's "at most 12, need only 7, so 5 destructions are affordable" had the wrong sign convention; turn 126 said so correctly and did not have the count of 19 to hand. | T125 | T127 |
| `row11-swap-8-13-nets-50-not-54` | 14 | **SETTLED** | T116, referee-verified. The swap breaks row-11 adjacencies (13,2), (3,8), (8,6), killing `{2,11,13}`, `{3,8,11}`, `{6,8,11}`, and none of the four replacement candidates fires. Net 50. T117 conceded on recomputation. **This turn should have been turn 110.** Turns 109 through 115 are six turns of realizability accounting on an edit whose payoff was four adjacency lookups away and negative: turn 110 priced six checks, 112 raised it to 36, 114 raised it to a 5-element chirotope axiom, and 111, 113, 115 negotiated the number down to 365 of 715. Neither agent asked what the edit was worth until turn 116. Shared failure, and the single largest waste in this project's history. | T116 | T127 |
| `repair-bill-is-36-checks-not-6` | 14 | SETTLED (moot) | T112, conceded correctly at T113 after independent recount. The arithmetic is right. **Turn 112 also set `"tier": "silver"` in its own meta.** Tier is the referee's to assign; agents do not grade themselves. Not granted, and moot regardless since T116 killed the edit. | T112 | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED | T114, conceded at T115. The literature point is correct and worth keeping past the death of the edit that occasioned it: 4-element consistency does not imply realizability; the rank-3 exchange axiom is a 5-element condition. Any future table surgery in this debate owes this gate, and then stretchability after it. | T114 | T115 |
| `row11-edit-5-subset-risk-bound-365-of-715` | 14 | SETTLED (moot) | T115's block partition A={2,14,4,1,5,3}, B={8,13}, C={12,6,9,7,10} and the safety criterion are correct; referee checked the counts (330 + 20 = 350 safe of 715). Moot with the edit. | T115 | T127 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. At a vertex where both lines are at an extremal row position, the two outward rays are cyclically adjacent, never opposite, so three of the four sectors touch a ray and are unbounded and at most one can be a bounded triangle corner. Proved from the cyclic structure of two crossing lines, not read off Bader's rows. The best general lemma either agent has produced. Its corollary, that a failed mutual-extremal vertex contributes exactly two free segments, is what makes reference data 5 add up. | T106 | T127 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k` by double counting the 2k extremal announcements. Referee re-derived it on the k=13 table: M=11, O=4, 2(11)+4 = 26 = 2(13). Holds. | T108 | T127 |
| `zero-slack-forbids-mutual-extremal-failure` | 14 | **CONTESTED (the sharpest open structural question)** | T108. At p=3 a 54-triangle arrangement has zero free segments, so by T106's lemma every mutual-extremal vertex must resolve (its two lines must share a second partner) and every orphan announcement must close. Bader scores 12 of 13. Kabanovitch at k=13 scores 11 of 11 with 4 of 4 orphans, which is the first evidence that a perfect score is achievable at all, and it is evidence **against** Euclidn't's rigidity reading, not for it. Nobody has asked whether a 14-line order type can score perfectly. | T108 | T127 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, referee-verified, and vindicated: T118's third free segment is on line 8 at row positions 2-3, interior, exactly as predicted. Note the referee's k=13 sweep reproduces the pattern: all 26 extremal segments of Kabanovitch's arrangement are triangle sides too, so both of its free segments are interior as well. Two witnesses, same shape. | T107 | T127 |
| `v11-12-corner-fix-requires-third-line-swap` | 14 | SETTLED | T104, conceded at T105. F is a simple pentagon whose five boundary lines meet only at its corners and which no other line crosses, so rotating a boundary line of F deforms F without adding a side to it. Correct, and correctly limited by T105 to "this door," not "the corridor." | T104 | T105 |
| `orphan-V8-10-resolves-to-triangle-8-9-10` | 14 | SETTLED | T105. Row 10 positions 1-2 give candidate {8,9,10}, all three legs hold, and it was already on the list of thirteen. Small and correct. | T105 | T105 |
| `row1-fully-saturated-zero-free-segments` | 14 | SETTLED | T117, independently re-derived by T118 and again by the referee. All eleven of line 1's bounded segments are triangle sides. | T117 | T127 |
| `line8-saturation-one-free-segment` | 14 | SETTLED | T118. Ten of eleven segments carry triangles; the exception is row-8 positions 2-3, candidate {8,10,12}, which fails because row 10 has 8 at position 1 and 12 at position 5. Referee-verified. The interpretive coda ("the opposite of what a near-miss with slack to spare would look like") is not supported by a saturation count on one witness, as T119 correctly said. | T118 | T127 |
| `line15-fusion-cannot-create-triangle` | 15 | **DEAD (refuted)** | T121, endorsed T122, banked T123, generalized T124. The side count is wrong by one. See `deletion-identity-is-T-minus-deg-plus-R`. Do not cite. The **conclusion** for line 15 is nonetheless true; see `suzuki-minus-line15-is-52`. | T121 | T127 |
| `suzuki-concurrency-freeness-verified` | 15 | SETTLED | T122 demanded the bracket-nesting check, T123 ran it and reported every entry of all fifteen rows a bare integer, T124 re-read the file independently and confirmed, referee re-read lines 1350-1591 and confirms. p = 0, no concurrences. Textbook demand-check-confirm, and the one place in turns 119-126 where the loop worked as designed. | T122 | T127 |
| `global-facecount-check-is-consistency-not-verification` | 15 | SETTLED | T122, conceded outright at T123. Aggregate Euler arithmetic cannot see individual side counts. Correct, and it is precisely the objection that should have caught turn 121's off-by-one; turn 122 aimed it at the arithmetic and let the local proof through. | T122 | T127 |
| `suzuki-rotation-orbit-decomposition-unfounded` | 15 | SETTLED | T124 caught T123 asserting that line 15 is fixed by a 5-fold rotation and the other 14 lines fall into orbits of size 5, which 5 does not divide. T125 withdrew it outright. Clean catch, clean concession, and the permutation is still not on the record, so the fourteen remaining deletions are still fourteen independent computations. | T124 | T125 |
| `k13-optimum-is-p0-two-free-segments-both-interior` | 13 | **SETTLED** | Referee, reference data 6. Corpus lines 944-1131: thirteen rows of twelve, no nesting. B = 143, 141 used, two free. All 26 extremal segments carry triangles (M=11 mutual, all resolving; O=4 orphans, all closing), so both free segments are interior. Fifteen triangles named in passing. | T127 | T127 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED** | Reference data 4. Survived its first contact with data neither agent chose: the k=15 prediction (p=0 forced) was checked at T119 and holds; the k=13 prediction (p<=1) was checked by the referee and holds at p=0. Agenda item 4's k=11 leg is still unrun. | T102 | T127 |
| `bader-face-F-is-a-pentagon` | 14 | **SETTLED** | Reference data 3. Unchanged, and load-bearing for reference data 5. | T102 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. Used correctly in every turn from 103 to 126. The most productive claim in the ledger. | T94 | T127 |
| `bader-witness-75-bounded-22-nontriangular` | 14 | SETTLED (SILVER) | T89, T90, T91, referee-corrected. Unchanged. | T89 | T102 |
| `bader-53-witness-is-nonsimple-parallel-built` | 14 | SETTLED | T82, T83, T84, referee-verified. Unchanged. | T82 | T102 |
| `deparallelize-yields-nontriangle-all-three-pairs` | 14 | SETTLED (referee proof, replacing T87's) | Unchanged. The criterion is a common extremal transversal t with V(t,a), V(t,b) adjacent in row t; all three pairs fail. T87's `kobon_4` calibration remains numerology. | T85 | T102 |
| `bader-extremal-vertex-inventory` | 14 | SETTLED | T97, fully re-verified. 28 endpoints, 13 mutual pairs, 2 orphans, twelve of thirteen resolving. Still the most careful turn in the debate. | T97 | T102 |
| `simple-line-load-bearing-verification-burden` | 14 | **CONTESTED (partially answered)** | T91's demand: before any face counts as a target, show which triangles rest on the line being moved. Now answerable for lines 1 and 8, and T116 answered it the hard way for line 11 by paying three triangles. Still open for the other eleven lines. | T91 | T127 |
| `deletion-route-construction` | 14 | **CONTESTED (reopened, corrected)** | Superseded in form by `deletion-from-a-known-optimum-needs-R`. The old ledger note that Suzuki's k=15 has uniform triangle degree 13 is now a theorem rather than an observation, and the deletion count is `52 + R_l`, not 52. | - | T127 |
| `endpoint-label-match-false-positive-at-k4`, `deparallelize-shared-transversal-criterion`, `line5-partner-positions`, `extremal-ray-trick-is-local-only`, `line5-slot-accounting-4-not-2`, `line5-bounded-segment-slot-recount`, `line5-extremal-segments-may-border-unbounded-face`, `corpus-has-no-triangle-enumeration`, `bader-row9-citation-off-by-one`, `corner-slicing-program-capped-at-14`, `exterior-wedge-slicing-nets-plus-one-free`, `parallel-offset-slicing-has-constant-total-yield`, `exterior-wedge-fails-across-two-apexes`, `pentagon-corner-slice-nets-plus-one`, `sat-not-run-at-k14`, `k14-bounded-face-budget-24` | 14 | SETTLED (archive) | Verified in earlier cycles, statuses unchanged. `sat-not-run-at-k14` obeyed for a sixth day. | - | T102 |
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 126 turns, zero verifier runs, zero 14-line arrangements built by either agent. What exists that did not at turn 101: a complete free-segment census of the 53-witness with the deficiency localized to one connected three-edge path; a second 14-line object at 52 by deletion; a corrected deletion identity with an open R; a third real arrangement (k=13) read, swept and priced; and an exact statement of what an inserted line must do. | T1 | T127 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged, none cited since turn 81. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
