# Agenda

Rewritten daily by the referee. Written after turn 154.

Last cycle's standing observation was: read the ledger before you start an
assignment and check whether you have already done it. It was obeyed. Nobody
recomputed anything this cycle.

The new standing observation is: **before you declare a method blocked, spend
one lookup trying to unblock it.** Turn 153 hit a turning-direction ambiguity
at V(2,4) and stopped. Turn 154 hit the sigma-image of the same ambiguity at
V(11,13), stopped in the same place, and escalated the stop into a sourced
impossibility — "the face-tracing method has a sourced gap." It is two row
lookups. Reference data 8 does both vertices, and reference data 9 and 10
contain the three faces that fell out in the same pass. Turn 153's V(2,4)
resolves to V(2,10); turn 154's V(11,13) resolves to V(13,5).

So the face list is unblocked and it is now the only thing on the board. Three
of the nineteen are named. Sixteen remain, and the mirror tells you their shape
in advance: **exactly five are sigma-fixed and the other fourteen form seven
orbits.** Two of the fourteen are already the hexagon pair; one of the five is
already the pentagon P.

**Do not re-derive reference data 9 or 10.** The hexagon pair and pentagon P
are done. Start from what is not.

## 1. Both sides: the four remaining sigma-fixed faces, walked along the axis.

Reference data 10 gives you the mirror axis as an object: it passes through
V(7,8), the midpoint of edge V(1,7) - V(1,8), and the vertices V(2,13),
V(3,12), V(4,11), V(5,10), V(6,9), and the bounded faces it meets in order are
`{1,7,8}`, then P, then four more. Each of those four is sigma-fixed, so each
has an even number of sides with two of its edges swapped by sigma at the axis
vertex where the axis enters and again where it leaves — which means **you only
have to walk half of each one and reflect.**

F2 is seeded: the axis leaves P at V(3,12), and F2's two edges there are
V(3,12) - V(3,7) (row 3 position 6) and V(12,3) - V(12,8) (row 12 position 6).
Walk from one, stop when you hit the next axis vertex, reflect.

- **PythagorAss:** F2 and F3.
- **Euclidn't:** F4 and F5, working backwards from the far unbounded end of the
  axis if that is cheaper.

**The named object:** the axis order of all seven crossing points, and the four
faces as ordered vertex lists with side counts. The order is a single sequence
and you must agree on it; if your two halves do not meet in the middle, one walk
is wrong and the disagreement localizes it to one vertex.

**Free falsifier:** the five fixed faces have even side counts unless the axis
enters through an edge midpoint, which happens only for line 1 and therefore
only once. So P, entered through the fixed edge and left at a vertex, is odd —
it is a pentagon, and it checks out. F2 through F5 are entered at a vertex and
left at a vertex, so **each of them has an even number of sides.** If you produce
an odd one, the walk is wrong.

## 2. Split by mirror half: the six remaining orbit representatives.

Every non-triangular bounded face has at least one edge, and every edge is
either a triangle side or one of the two free segments. All 141 triangle sides
are known from reference data 7. So the complete search is: for each triangle
side, walk the face on the far side; anything that is not a triangle and not
already listed is new. Dedupe as you go.

Sigma maps lines 2..7 onto 13..8, so:

- **PythagorAss** starts from triangle sides on lines 2, 3, 4, 5, 6, 7.
- **Euclidn't** starts from triangle sides on lines 8, 9, 10, 11, 12, 13.

Your two harvests must be sigma-images of each other, except for fixed faces,
which appear in both. That is the cross-check and it costs nothing.

**The named object:** at least three new orbit representatives each, as ordered
vertex lists with side counts and sigma pairings. Six of them plus the hexagon
pair plus the five fixed faces closes the census at nineteen. If your count
lands anywhere other than 19 = 5 + 7 x 2, say so loudly; that is a
contradiction with reference data 10 and one of us is wrong.

## 3. The corner-clip question, the moment you have fifteen faces.

`insertion-into-k13-needs-seven-corner-clips` is exact: a generic line inserted
into Kabanovitch's k=13 gives `T' = 47 + Y`, where Y counts its bounded chords
that clip a corner off a non-triangular face. Reaching 54 needs **Y = 7 out of
nineteen faces, with X <= 5 of the forty-seven triangles crossed**, from twelve
bounded chords.

The first datum is already in: both free-segment faces are hexagons and the
first fixed face is a pentagon. A chord clips a corner of an m-gon only when it
separates exactly one vertex from the other m-1, so a hexagon offers six of its
fifteen chord-classes as clips and a quadrilateral offers four of six. The
tension to test rather than assert: a line dodging triangles is pushed toward
large faces, and large faces are proportionally harder to clip.

**The named object:** the side-count distribution of the nineteen, then either a
candidate ordered sequence of seven faces one line could visit in order, with
the triangles it must cross counted, or the specific adjacency obstruction that
stops one. Do not start this before you have fifteen faces; a distribution built
on six is a guess.

## 4. Still owed since turn 124: the Suzuki permutation, and Bader's.

One turn, whoever finishes item 1 first. `kobon_15_5_rot_symmetry` announces a
5-fold rotation and turn 123 asserted an orbit decomposition that turn 124
correctly killed on the arithmetic. Thirty turns later the permutation is still
not written down. The k=13 analogue has now paid three separate times: it
halved the triangle enumeration, explained why the two free segments are a
matched pair, and produced the entire fixed-face census in reference data 10.

Same for Bader's k=14: any automorphism must permute the parallel pairs {1,2},
{3,4}, {7,8} and fix or permute the free-segment path on lines 8, 11, 12. That
is a short search.

**The named object:** an explicit permutation verified row by row, or the
statement that every pair-set-preserving candidate fails, with the row that
kills each.

## Killed this day

- **"The table underdetermines the turn direction."** Turn 153's version and
  turn 154's escalation of it are both wrong; reference data 8 is three lines of
  argument and two lookups per turn. Do not cite the phase-2 design doc's circle
  convention as an obstacle again. The quotation was accurate; the inference was
  not.
- **Agenda item 4, permanently.** Turn 154 retired it by re-deriving turn 137.
  `zero-slack-forbids-mutual-extremal-failure` is true, carries no content
  beyond full saturation, and is not a route to an impossibility proof. It
  survives only as a filter on a candidate table.
- **"Four of the nineteen handed to you."** The referee's own line from turn
  152. It is two. Each free segment borders one bounded non-triangular face and
  one unbounded three-sided face. Turn 153 caught it and that is the correction
  of the cycle.
- **The Suzuki deletion sweep and the deletion route at every k.** Unchanged and
  still dead. Fifteen zeros against a requirement of 2, 3 and 4.
- **Near-miss and margin arguments.** Three attempts, three collapses. Still
  banned.

## Standing prohibitions, still in force

- Before beginning any assigned computation, confirm it has not already been
  done, including by you and including by the referee.
- Certifying an opponent's turn as re-checked means re-generating the object,
  not re-reading their numbers.
- Before declaring a method blocked, attempt one concrete instance of the block
  and report what specifically failed. "Neither agent has built it" is not a
  proof that it cannot be built cheaply.
- No sub-arrangement averaging or delete-a-line upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a row printed in the ledger
  or the corpus, cited by line number.
- When you concede, re-derive the step being conceded rather than restating it.
- Any proposed edit or perturbation comes with its triangle cost in the same
  turn.
