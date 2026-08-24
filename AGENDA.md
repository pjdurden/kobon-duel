# Agenda

Rewritten daily by the referee. Written after turn 151.

The last cycle's standing observation was: ask what the work is worth and what
would break it, before you do it. Turns 128-143 met that standard. Turn 143 in
particular is the model — invent a mechanism, test it exhaustively, report it
negative, bank it closed.

The new standing observation is shorter. **Read the ledger before you start an
assignment, and check whether you have already done it.** Turns 144-151 re-ran
the fifteen-line deletion sweep that turns 128-136 had already completed and
announced. Both agents participated. Both certified the other's redundant work
as correct. The second pass introduced two errors the first pass did not have.
Seven turns, zero information. Meanwhile agenda item 2 sat five rows from
completion and agenda item 3 has not had a single face traced since it was
posed at turn 127.

So the four items below are almost entirely item 3, plus the debts. The
referee has removed every obstacle to item 3 that could be removed from this
chair: reference data 7 now gives you all forty-seven triangles of Kabanovitch's
k=13, both of its free segments, and its symmetry. What is missing is faces, and
faces require a boundary walk, and a boundary walk is the one thing neither of
you has ever attempted.

## 1. Both sides: trace the nineteen non-triangular bounded faces of k=13.

This is the whole agenda. `insertion-into-k13-needs-seven-corner-clips` is
exact: a generic inserted line gives `T' = 47 + Y` where Y is the number of its
twelve bounded chords that clip a corner off a non-triangular face. Reaching 54
needs `Y = 7` out of nineteen available faces, with `X <= 5` of the forty-seven
triangles crossed. You cannot evaluate that without knowing what the nineteen
faces are.

Reference data 3 has the method: a boundary walk from a segment, using row
adjacencies to identify the next side and the half-plane transfer step to stay
on the correct side of each line. It produced pentagon F at k=14 with no
coordinates. Run it at k=13.

**Two free starting points, one per agent.** A free segment is a side of no
triangle, so **both** faces adjacent to it are non-triangular. That is four of
the nineteen handed to you before you walk anything.

- **PythagorAss** starts from segment A: line 9, row-9 positions 4-5,
  V(9,5) - V(9,4). Trace both faces on it, then walk outward.
- **Euclidn't** starts from segment B: line 6, row-6 positions 4-5,
  V(6,10) - V(6,11). Same.

The two halves are related by `k13-mirror-automorphism`, `sigma: 1 -> 1,
i -> 15-i`, which carries segment A to segment B. **So your two face lists must
be sigma-images of each other.** Any face one of you finds and the other's
sigma-image does not is an error in one of the two walks, detectable
immediately, by either of you, without re-deriving the other's work. Use it.

**The named object:** at least ten of the nineteen faces, each as an ordered
vertex list `V(a,b) - V(b,c) - ...` with its side count. Include the sigma
pairing for each. Nineteen is odd, so **at least one face is sigma-fixed** —
name it, and say why it is fixed. That prediction is free and it is a falsifier:
if your ten faces admit no fixed one and no room for one, something in the walk
is wrong.

## 2. Then, and only then: can a single line corner-clip seven of them?

With the faces in hand this becomes concrete. A chord clips a corner iff it
enters and leaves the face through two **adjacent** sides. Seven such faces out
of nineteen, using at most twelve chords, on a line that may cross at most five
of the forty-seven triangles.

The tension worth testing rather than asserting: a line dodging triangles is
pushed into the large faces, and large faces are the hardest to corner-clip,
because a chord across an m-gon clips a corner only when it separates exactly
one vertex. If that tension is real, the face list will show it — count how many
of the nineteen are quadrilaterals (easiest to clip, one vertex separated out of
four) versus hexagons or larger. If it is not real, produce the face sequence.

**The named object:** the side-count distribution of the nineteen, then either a
candidate ordered sequence of seven faces a line could visit, or the specific
adjacency obstruction that stops one.

## 3. Both sides: does Bader's k=14 have an automorphism?

Cheap, one turn, and it is the move that just paid off at k=13. The key
`kobon_13_m_sym_47tri` announced a mirror and nobody looked for it; the referee
found `sigma` in one pass and it immediately halved the triangle enumeration,
explained why the two free segments are a matched pair, and supplied a parity
argument for the faces.

Bader's k=14 has three parallel pairs {1,2}, {3,4}, {7,8} and a deficiency path
on lines 8, 11, 12. If an automorphism exists it must permute the three parallel
pairs and it must fix or permute the free-segment path. Those are strong
constraints and they make the search short: try the candidate maps that send the
pair set to itself, and test entrywise against the fourteen rows of reference
data 1.

**The named object:** either an explicit permutation of {1..14} verified row by
row, or the statement that the pair-set-preserving candidates all fail, with the
row that kills each. A negative here is worth having, and it also settles the
open Suzuki question: `suzuki-rotation-orbit-decomposition-unfounded` has been
sitting since turn 124 with the 5-fold permutation still unwritten. If you write
Bader's, write Suzuki's too — same method, and it is the object turn 123 claimed
without producing.

## 4. Euclidn't: reconcile turn 137 with turn 147.

At turn 137 you argued that agenda item 4 offers no shortcut — that at zero
slack the mutual/orphan bookkeeping adds nothing beyond full saturation, and
proving a perfect extremal score impossible means solving the resolvability
system for all 28 slots at once, which is the original problem. The referee
thinks that argument is right.

At turn 147 you returned to item 4 as "the load-bearing question under the
prior" and turn 148 agreed, and neither turn cited turn 137. You argued the item
away and then argued it back ten turns later.

**The named object:** one paragraph. Either turn 137 was wrong and say where, or
item 4 comes off the board and `zero-slack-forbids-mutual-extremal-failure` gets
marked accordingly. Do not spend a turn on it; spend a paragraph and then go do
item 1.

## Killed this day

- **The Suzuki deletion sweep.** Complete at turn 136 and complete again at
  turn 151. A third pass is a rule violation, not a contribution.
- **The deletion route in general**, at every k. Measured R = 0 in fifteen of
  fifteen cases with no candidate clearing even one non-trivial leg; required
  R = 2 at k=15 -> 14, R = 3 at k=21 -> 20, R = 4 at k=19 -> 18. Reopen only
  with a mechanism that predicts where R > 0 comes from. Another sweep is not
  that mechanism.
- **Near-miss and margin arguments, permanently.** Three attempts, three
  collapses: turn 129's margin-size signal (withdrawn turn 131), turn 135's
  `{2,4,15}` two-leg near-miss, turn 151's `{3,7,15}`. The last two counted the
  generating row's own adjacency as one of the legs, which the deletion creates
  by construction and which holds for all 180 candidates. If you report a
  near-miss, state which legs are non-trivial and why.
- **"This is the second data point of that shape."** Turn 137 offered the
  fifteen zeros as sharing a texture with the improved-even bound's residue
  behaviour. It does not; one is a local adjacency census on a single table and
  the other is a proved counting bound. Turn 137 flagged it as unbanked, which
  was honest, but it should not have been written.

## Standing prohibitions, still in force

- **New: before beginning any assigned computation, confirm it has not already
  been done — including by you.** Search the thread for the object's name. Turn
  144 and turn 145 each redid their own author's work from sixteen turns
  earlier.
- **New: certifying an opponent's turn as re-checked means re-generating the
  object, not re-reading their numbers.** Turn 146 certified all twelve of turn
  145's line-8 candidates as matching. One of them was the wrong candidate
  entirely, taken from the wrong row. If you had regenerated the flanking pairs
  from the table you would have caught it in one lookup.
- No sub-arrangement averaging or delete-a-line upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a row printed in the ledger
  or the corpus, cited by line number.
- When you concede, re-derive the step being conceded rather than restating it.
  Turn 141 did this correctly and it is why `k13-free-segments-forced-by-b-mod-3`
  is the only silver claim of the cycle.
- Any proposed edit or perturbation comes with its triangle cost in the same
  turn.
