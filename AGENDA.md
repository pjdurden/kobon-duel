# Agenda

Rewritten daily by the referee. Written after turn 126.

The standing observation from the last cycle is retired. You stopped saying a
computation needs coordinates and started running computations. Turns 103, 105,
107, 116, 117, 118, 119, 123, 124 and 125 each cite rows by line number and each
verifies. That is the standard now and you are meeting it.

The new standing observation is about what you do between computations. Turns
109 through 115 are six consecutive turns negotiating the size of a verification
bill for an edit that turn 116 then priced, in four lookups, at minus three
triangles. Turns 121 through 124 are four consecutive turns agreeing about a
face-merging lemma whose side count is off by one. In both cases the error was
not in the arithmetic either of you ran. It was in never asking the cheap
question first: **what is this worth, and what would break it.** Turn 116 asked
the first. Nobody asked the second.

Everything below is computable from rows printed in the ledger or cited by line
number in `corpus/arrangements.json`. None of it needs coordinates, a SAT
solver, or a new construction.

## 1. Both sides: R for Suzuki's other fourteen lines. This one can end it.

The deletion identity is `T' = T - deg_T(l) + R_l`, not `T - deg_T(l)`. Suzuki's
k=15 is degree-regular at 13 by theorem, so deleting **any** line gives
`52 + R_l`. **R_l = 2 for a single line is a 14-line arrangement with 54
triangles**, which closes the case the debate has been on since turn 1.

The computation is bounded and mechanical. A triangle that exists after deleting
l but not before must use an adjacency the deletion created, so its triple is
`{a, x, y}` where x and y are the entries flanking l in row a. There is at most
one candidate per row, so at most fourteen candidates per line. Test each with
the settled iff test, **after deleting l from every row you read**. R_l is the
number that fire. The referee ran l = 15: twelve candidates, twelve failures,
R_15 = 0, all twelve listed in the ledger under `suzuki-minus-line15-is-52`.

**The named object:** for each l, the candidate list and the verdict on each,
then `52 + R_l`. PythagorAss takes lines 1-7, Euclidn't takes lines 8-14. Report
the failures with the row positions that killed them, the way the referee's
twelve are reported, so the other side can check without re-deriving.

Do not skip lines on the grounds of five-fold symmetry. Turn 124 was right that
the permutation is not on the record and turn 125 withdrew the claim. If you
want the shortcut, write down the permutation of {1..15} and verify it against
the rows first; then it is a result and not an excuse.

## 2. Both sides: the two free segments of Kabanovitch's k=13 optimum.

Reference data 6: `kobon_13_m_sym_47tri` is p = 0, has 143 bounded segments, 141
of them triangle sides, and **exactly two free**. The referee's extremal sweep
closed all 26 extremal segments, so both free segments are interior, positions 2
through 10 of some row.

**The named object:** both segments as (line, its two endpoint crossings), with
the candidate triple and the row position that kills it. PythagorAss takes rows
1-7, Euclidn't takes rows 8-13, interior positions only, 63 and 54 tests. The
budget guarantees exactly two exist, so a third is proof that the corpus's count
of 47 is wrong, which would be a larger finding than either of you is chasing.

This is the same object at k=13 that took twenty-five turns to complete at k=14,
and you now have the method that did it.

## 3. Both sides: can any line corner-clip seven of the nineteen?

`insertion-into-k13-needs-seven-corner-clips` is exact: inserting a line into the
47-triangle arrangement gives `47 + Y`, so 54 requires **Y = 7 and X <= 5** -
seven chords clipping corners off non-triangular faces, at most five chords
crossing triangles, out of twelve bounded chords total. There are exactly
nineteen non-triangular bounded faces and forty-seven triangular ones.

**The named object:** at least six of the nineteen non-triangular bounded faces,
each as an ordered vertex list with its side count, traced by the boundary walk
of reference data 3. Then the real question: is there a straight line meeting
seven of them, entering and leaving each through two **adjacent** sides? Note
the tension worth testing rather than asserting: dodging triangles pushes a line
into large faces, and large faces are the hardest to corner-clip. If that
tension is real, say what makes it real; if it is not, a counterexample face
sequence is the answer.

## 4. Both sides: does a perfect extremal score exist at k = 14?

`zero-slack-forbids-mutual-extremal-failure` (T108) is still the sharpest
structural question on the board and neither of you has returned to it in
eighteen turns. At p = 3, a 54-triangle 14-line arrangement has zero free
segments, so by `mutual-extremal-vertex-tv-leq-1-general` every mutual-extremal
vertex must resolve and every orphan must close.

New data the referee put on the board: Kabanovitch's k=13 optimum scores
**perfectly** - eleven of eleven mutual vertices resolve, four of four orphans
close. Perfect extremal scores exist. Bader's k=14 misses by one vertex.

**The named object:** either an argument that a 14-line order type cannot score
perfectly, or the observation that k=13 already does and therefore turn 118's
rigidity reading has a counterexample one row of the corpus away. Euclidn't
should take this one first; it is the load-bearing question under the prior.

## 5. Corrections to bank, not re-argue.

**PythagorAss, turn 121.** "The merged face has exactly (1 fused a-edge) +
(1 fused b-edge) + (F_right's remaining m-2 sides) = m sides." F_right's a-edge
and b-edge are consumed by the two fusions. What remains of F_right is m-3
sides, and the merged face has m-1. At m = 4 that is a triangle. Deletion can
create triangles; your conclusion for line 15 happens to hold and the referee
verified it, but not for the reason you gave.

**Euclidn't, turn 122.** You called the m>=4 conclusion "a real derivation, not
just the assertion turn 121 gave," and re-derived the same off-by-one with more
confidence than the original. In the same turn you correctly said aggregate
Euler arithmetic cannot see individual side counts. That objection was the exact
tool for this error and you pointed it at the wrong half of the turn.

**Euclidn't, turn 124.** "The resulting 14-line count is exactly
`65 - deg_T(l)`, with certainty and no slack, for every l." False as stated, and
the words "with certainty and no slack" are doing the work an argument should.

**PythagorAss, turn 125.** Three lines checked, three times 13, called "strong
evidence this arrangement is triangle-degree-regular." Every line of a
Tamura-tight arrangement carries exactly k-2 triangles, forced by the segment
budget already in the ledger. You proved a theorem three times by hand and
reported it as a sample.

**Both, turn 118 onward.** The free-segment census of Bader's witness was
complete at turn 118 and neither of you noticed. Turn 103 found two, turn 107
predicted the third would be interior, turn 118 found it at row-8 positions 2-3,
and the budget said three all along. Turn 118 called it "the first free segment
either of us has actually located" and sent everyone hunting for two more that
did not exist. Read your opponent's turns as data, not as positions.

## Killed this day

- **The row-11 table surgery.** Dead at turn 116, net 50. Do not revive it, and
  do not open another edit without pricing it against
  `bader-triangle-adjacency-test-is-iff` in the same turn you propose it.
- **Re-verifying Suzuki's per-line triangle degree.** Forced to 13 for all
  fifteen lines by `tamura-tight-implies-every-line-saturated`. Checking it by
  hand is not evidence, it is a slow way to read the ledger. R_l is the open
  quantity, not the degree.
- **Hunting for more free segments in Bader's witness.** There are three, all
  named, forming one connected path. `bader-three-free-segments-form-a-path`.
- **"One witness's rigidity" as evidence either way.** Turn 118 overreached with
  it and turn 119 was right to say so; turn 126 then accepted a version of the
  same move. Two 14-line objects (Bader at 53, Suzuki-minus-15 at 52) and a
  13-line optimum are now on the table. Argue about the class or about a named
  object, not about the mood of a saturation count.

## Standing prohibitions, still in force

- No sub-arrangement averaging or delete-a-line **upper bounds** at k=14.
  Delete-a-line **constructions** are back in play; see item 1.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a row printed in the ledger
  or the corpus, cited by line number.
- **New:** when you concede, re-derive the step being conceded rather than
  restating it more confidently. Turn 122 restated turn 121's error and turn 124
  hardened it into a law. A concession is a check, not an endorsement.
- **New:** any proposed edit or perturbation must come with its triangle cost in
  the same turn. Not the next turn. The cost is four lookups.
