# Agenda

Rewritten by REFEREE after turn 229. Supersedes the T180 agenda.

## 0. Read this before you write anything

**Thirty-eight turns are missing and you have been working from a stale
baseline.** Turns 188 through 225, plus the turn-205 referee pass, all failed on
OAuth expiry. Turn 226 believed the gap was five turns and that turn 180 was the
last real content. It was not. **Turns 181 through 187 built a six-corner-clip
candidate against Kabanovitch's B with all twelve two-row insertions pinned and
correct.** I have restored it as reference data 15. Read it before you propose
anything, because turns 226 to 229 spent four turns rebuilding a two-clip version
of a six-clip object that was already on the record.

**Three results landed this cycle. Do not re-derive them.**

- Reference data 16: an inserted line's trajectory is a **forced walk** in B's
  face-adjacency graph. The successor face is determined by the exit edge, not
  chosen. `Y` counts pieces whose entry and exit edges share a vertex and whose
  face is not a triangle.
- Reference data 16b: every edge of a non-triangular bounded face has a triangle
  across it, except the two free segments. This answers the old agenda item 3
  ("how many edges border an unbounded face") completely: zero for seventeen of
  the nineteen, one each for hexagons A and B. Do not run that census.
- Reference data 19: `n_N = 6` forces `Y <= 6` for Kabanovitch's B. So 54 from
  this base needs `n_N <= 5` and **two clipping U-chords**.

**The verifier is still gated.** I ran `python3 -c "print(1)"` this session and it
was refused before execution. Keep attempting once per turn, keep labelling
hand-argument honestly. Owner action, along with the OAuth refresh.

## 1. Both: attack reference data 19

It is my argument and nobody has had a turn on it. It is the only obstruction
result in this project's history that has not been refuted within ten turns, and
that is a reason for suspicion, not confidence. Break it or certify it, and
certifying means re-generating the object, not re-reading my prose.

Four places it could fail, in descending order of how worried I am:

1. **The wedge-neighbour step in Shape 2.** I claim wedges A and B share no edge
   and that a triangle cannot border a wedge. The second rests on wedge A having
   exactly one bounded edge (reference data 8). Check that.
2. **The `{2,4,9}` and `{5,7,9}` identifications.** I verified all six legs
   against reference data 6. Re-verify them independently.
3. **`G1` and `F5` as the faces two steps upstream.** I identified them by
   matching an edge in reference data 10 and 14. If either face is misidentified,
   the contradiction may not hold.
4. **The seven-pattern enumeration.** `C(7,6) = 7` non-consecutive 6-subsets of
   `{1,...,12}`. If you find an eighth shape I have missed a case.

**Named object:** either a named step with a counterexample, or a statement of
which of the four you re-generated and what you got.

## 2. PythagorAss: build the `n_N <= 5` route, or say it is blocked

Reference data 19 leaves exactly one shape for 54 out of Kabanovitch's B: five
N-clips and two clipping U-chords, on thirteen crossings. Build it as a walk,
not as a set of corners. At every step name the face, the entry edge, the exit
edge, and the **forced successor**. That is what T181 skipped and it is what
reference data 17 kills.

Note what makes this harder than it looks: a U-chord is only worth anything if it
clips, and to clip an unbounded face `U` your entry and exit edges of `U` must
share a vertex. Reference data 18 shows the edges need not be free, so most of
B's 26 unbounded faces are in play, but you owe the vertex.

**Named object:** a fourteen-face walk with thirteen distinct line labels, its
`Y`, and the first step at which it fails if it fails.

## 3. Euclidn't: the extremal segment inventory

This is the data item 2 needs and it is the one computation nobody has run. A
bounded segment is **extremal** if one of its two faces is unbounded. By 16b no
extremal segment borders a non-triangular bounded face except the two free ones,
so every other extremal segment has a triangle on one side and an unbounded face
on the other. These segments are precisely the boundary of the union of B's
bounded faces, and they are precisely the edges through which `l` can leave the
bounded region and start a U-chord.

**Named object:** the list of extremal bounded segments of Kabanovitch's B, by
line and row position, or a count with an argument. If you can only do part of
it, do lines 1 through 4 and say so.

## 4. Euclidn't: one face, named

The segment on line 12 at **row-12 positions 8-9** (entries `7 1`) carries
triangle `{1,7,12}` on one side. The other side is **not** one of the eleven
named faces: I checked the line-12 edges of all four named faces that touch
line 12 and they sit at row-12 gaps 2-3, 4-5, 6-7 and 7-8. So the far side of
gap 8-9 is either one of the eight unnamed non-triangular faces or an unbounded
face, and either answer is worth a turn. It is one walk with turn 156's triangle
list tool.

**Named object:** the face, by vertex list, with each edge's row adjacency cited.

## 5. Standing requirement, new this cycle

**Before proposing any chord sequence, state the forced successor at each step.**
A clip of face `F` exiting through edge `e` does not leave you a choice about the
next face: it is the face across `e`, and by 16b that is a named triangle unless
`e` is free. Reference data 17 refutes a six-turn construction with two such
lookups. If your proposal does not name the successor at every step, it is a
permutation, not a walk, and T182 already explained why a permutation is not a
table.

## Killed this day

- **The T181 chain as ordered.** Reference data 17. The clips survive; the
  sequence does not.
- **The `n_N = 6` branch for Kabanovitch's B.** Reference data 19. Every
  constructive turn from T181 to T229 lives inside it.
- **"Only free segments can be corner-clipped."** T229, reference data 18. The
  cap of 2 is false and the k=3 to k=4 instance shows it in four lines.
- **The 7-8 corridor as a density claim.** T226, refuted T227, conceded T228.
  The lemma stands, the inference does not.
- **The adjacency census the T180 agenda ordered.** Answered by 16b without
  doing it. Do not run it.
- **"Run the signotope gate" as a next step.** Nominated five times in 229 turns,
  run zero times, twice in place of a two-lookup argument that would have
  settled the question. Do not name it again unless you run one in the same turn
  or state why it cannot be run by hand.

## Standing prohibitions, still in force

- Confirm an assigned computation has not already been done before starting it.
  This cycle it cost four turns.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table. Six locally-true triples were checked three times
  across T184-T186 and the table they sat in does not exist.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step rather than restating it. When a
  concession hands you your own conclusion, audit it harder, not less.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's **crude cap** before analysing its fine
  structure: count segment types on a single line and multiply out. A family
  whose crude cap is below 54 does not get a second turn.
- No sub-arrangement **averaging** upper bounds at k=14. Structural per-insertion
  bounds remain permitted.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. T227 promised the adjacency data and
  T229 brought something else; T226 and T228 each promised a full chord typing
  and neither delivered.
