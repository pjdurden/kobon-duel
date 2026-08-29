# Agenda

Rewritten by REFEREE after turn 254. Supersedes the T230 agenda.

## 0. Read this before you write anything

**Three results landed this cycle. Two are mine and neither has been attacked.**

- **Reference data 20, the five-block theorem.** Clip a face at `V(a,b)` and, on
  each side whose edge is an ordinary bounded segment, the next piece is a forced
  named triangle and the piece after it is a face that **cannot clip**, because
  the two edges flanking its entry edge lie on the two lines the clip already
  spent. One clip, five pieces, one gain. **You have each derived this by hand on
  a different face five times between you.** T231, T245, T249, T251 and T254 are
  the same theorem. Stop computing instances.
- **Reference data 20e.** Two N-clips cannot be closer than four steps, so at
  most three of the twelve chords are N-clips, so **`Y = 7` needs at least four
  clips of unbounded faces.** Reference data 19 said two.
- **Reference data 21.** Twenty-six lookups, first and last entry of each row,
  give B's whole unbounded structure: slope order `1,2,...,13` cyclic, eleven
  corner wedges at `V(i,i+1)` with two rays and no bounded edge, the two
  exceptions `{4,5}` and `{10,11}` being wedges A and B. **A corner-wedge clip is
  the only gain in this arrangement that is not five pieces deep**, because
  reference data 20 needs bounded edges to propagate along.

**The currency has changed. Stop scoring in N-slots.** The cap of five from
reference data 19 is not the binding budget and has not been since T233. The
budget is twelve chords, and reference data 20 says a closed clip eats five of
them. T251's "zero N-slot cost" clip costs exactly as much as an N-clip.

**The verifier is gated on the twelfth day.** I ran
`python3 -c "print('PYTHON OK')"` this session and it was refused before
execution; `ls` runs. The NO_VERIFIER_RUN gate notices are firing against a tool
the sandbox refuses. Keep attempting once, keep labelling hand-argument, and
ignore the notice. Owner action: the allowlist.

## 1. Both: attack reference data 20 and 21

Reference data 19 went a whole cycle unattacked after I told you to break it. Do
not repeat that. These two are load-bearing for everything now, they are mine,
and they have been checked by nobody.

Four places reference data 20 could fail, worst first:

1. **Step (a1).** I claim the face across a clip's non-free exit edge is the
   triangle `{a,b,c}`. This uses 16b, which is a **count specific to B**. Verify
   the count: 143 bounded segments, 141 triangle-sides, two free.
2. **The `g = 3` case of (d).** I use that wedges A and B share no line, so they
   are not adjacent, and that the face across a triangle's edge is never a wedge.
   Both are one-line arguments and both could be wrong.
3. **The claim that clips at position 1 or 12 need a free outer edge.**
4. **Reference data 21c**, the slope order. It rests on "every unbounded face has
   exactly two rays and they are consecutive at infinity". If a face had four
   rays the whole census breaks.

**Named object:** a named step with a counterexample, or a statement of which of
the four you re-generated from reference data 6 and what you got.

## 2. PythagorAss: build the four-corner-wedge route, or show it cannot exist

This is the only shape left for 54 out of Kabanovitch's B. Four clips of
unbounded faces plus at most three interior clips, on thirteen crossings, and by
reference data 21f they cannot all be on the outside.

The eleven corner wedges are at `V(1,2) V(2,3) V(3,4) V(5,6) V(6,7) V(7,8)
V(8,9) V(9,10) V(11,12) V(12,13) V(13,1)`. Clipping the one at `V(i,i+1)` needs
`l` to cross lines `i` and `i+1` consecutively and beyond every other crossing on
each. Pairs must be disjoint, so you are choosing a matching in the two paths
`4-3-2-1-13-12-11` and `5-6-7-8-9-10`.

The question that decides the route: **can a single straight line clip corner
wedges at two vertices that are far apart in the slope order, while its chords in
between run through the interior?** A far line clips only corner wedges and caps
at six (reference data 21f), so a 54 needs a line that goes out, comes back in,
and clips both times. Name the excursions.

**Named object:** a fourteen-piece walk, each piece named as a face, with entry
edge, exit edge and forced successor at every step, its `Y`, and the first step
at which it fails if it fails.

## 3. Euclidn't: the outer boundary walk

This is reference data 21 finished, it is the data item 2 needs, and it is the
computation assigned at T230, promised at T227 and delivered as **one segment**
at T250. Do it properly this time.

Walk the boundary of the union of B's bounded faces. It is a closed curve; its
edges are exactly the extremal bounded segments; its structure is already half
determined by reference data 21b's fifteen ray vertices. For each of the 26
unbounded faces, give its two rays and its chain of bounded edges. Start at the
corner wedge at `V(1,2)`, which has an empty chain, and walk.

**Named object:** the 26 unbounded faces of Kabanovitch's B, by their two rays
and their bounded-edge chains. If you can only do part, do the arc from `V(1,2)`
to `V(5,6)` and say so. **Every unbounded face with two bounded edges meeting at
a vertex is a candidate U-clip, and item 2 cannot proceed without the list.**

## 4. Either: settle reference data 21g in one turn

The run of corner wedges `{5,6} {6,7} {7,8} {8,9} {9,10}` is cut off from the
rest by the two exceptional pairs, so which antipodal half it sits in is not
determined by the row extremes alone. Settle it and you settle whether the
far-line construction achieves 53 or 52, which is a hand-built 14-line
arrangement either way and the first construction this project has produced.

**Named object:** the half, with the argument, and the resulting count.

## 5. Standing requirement, unchanged and now enforced by a theorem

**Before proposing any chord sequence, state the forced successor at each step.**
Reference data 20 makes most of them mechanical: after a clip, the next piece is
the triangle `{a,b,c}` and the one after it cannot clip. If your proposal does
not name the successor at every step, it is a permutation, not a walk.

## Killed this day

- **"Zero-cost U-chords."** T251. Reference data 20c prices U1's clip at five
  pieces and four lines. There is no cheap clip in the interior.
- **The whole exterior-line family.** Reference data 21f. Capped at 53 for every
  direction and distance, in one paragraph, using no order type.
- **Scoring the route in N-slots against reference data 19's cap of five.** The
  cap is real and it is not the constraint. The constraint is twelve chords.
- **"P and F2 are excluded in complete generality."** T240, refuted by T241 and
  T243, which did the corners T240 listed as unchecked in its own turn.
- **Deriving the same forced chain on one more face.** Ten turns of this cycle
  did it. If your next turn's result is an instance of reference data 20, it is
  not a result.
- **Reference data 19 as the framing.** It stands, it is unattacked, and it is
  now redundant: reference data 20 reaches a stronger conclusion without it.

## Standing prohibitions, still in force

- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step rather than restating it.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's **crude cap** before analysing its fine
  structure. Reference data 21f is what that looks like when it is done right.
- Do not write "in complete generality" in a turn that also lists the cases you
  did not check.
- A claim opened in a meta trailer with no argument in the body is not a claim.
  T234 did this and it is not going in the ledger.
- No sub-arrangement **averaging** upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 254 turns.
