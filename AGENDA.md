# Agenda

Rewritten by REFEREE after turn 304. Supersedes the T280 agenda.

## 0. Read this before you write anything

**Two reversals and one number.**

- **Reference data 26. Two isolated triple points can share both helper lines.**
  Eight lines, explicit coordinates, every crossing parameter written down.
  T300's "nine hubs plus six dedicated helpers, none shared, hence fifteen lines"
  is false, and **T301's concession of it is reversed**. The reason T301 gave —
  a helper near `P1` must be far from `P2` — is the scale framing that T297, on
  the same side of the debate, had already replaced with an ordering condition
  four turns earlier. Do not concede to an argument your own side has refuted.
- **Reference data 27a. Isolated concurrence strictly costs slack.** `d <= 2`
  per isolated triple point (T293's cap, re-proved) plus `d - f = 3T - B`
  (T288's identity) gives, for `p = 0`,

      3T <= k(k-2) - c        and at k=14, T=54:   f <= 6 - c

  So the loosest regime for 54 is `c = 0`, with **six** free segments. The
  program of T288-T301 was aimed at `c = 3`, which allows three. Every triple
  point destroys three bounded segments and buys back at most two.
- **The error that inverted the cycle is one sentence in T288**: reference data
  4 gives `p <= 3`, a permission, and T288 read it as `p = 3` and got `f = 0` at
  `c = 0`. T292, T293 and T294 then compared against that baseline. Their
  numbers are right; the baseline is not.

**What survives from the cycle, and it is more than usual.** T288's identity
`d - f = 3T - B`. T293's `d <= 2` cap, now silver. T295's `k=5` coordinate
gadget, verified line by line. T284/T285's kill of non-generic insertion, now
silver. T286/T287's generalisation of it to all 78 vertices of B. T298's census.
T299's two-copy build. These are real and this is the strongest cycle on record
for object-production.

**What died:** T300's fifteen-line count; T304's row-neighbour "tax" (it is
reference data 4's candidate rule restated, and it pins nothing); T302's "zero
lines in this witness are generic" and T303's "the coupling is free", both drawn
from five of `kobon_6_2`'s seven triangles.

**The verifier is gated on the fourteenth day.** I ran
`python3 -c "print('PYTHON OK')"` this session; refused before execution. `sed
-i` is refused too. `grep` and `Read` run. Your convention is correct: raw corpus
reads, attempt once, say so, do not log it as a verifier run. Owner action: the
allowlist.

## 1. Both: attack reference data 26 and 27a

Reference data 26 is a construction and 27a is a proof, both mine, both
unattacked. Four places to push, worst first:

1. **27a's chaining step.** I claim that if ray `r`'s far endpoint is an ordinary
   crossing, the two sectors flanking `r` must close on the same line, because
   "nearest crossing on `r`" names one line. Check that against a sector whose
   third side lies on a line crossing `r` *beyond* the nearest crossing — I say
   that face is not a triangle. Say why I am right or produce the face.
2. **26's emptiness claims.** I assert that the four triangles at `P1` are faces
   because the only lines within `0.15` of `P1` are `a1, b1, c1, L, L'`. Verify
   by computing where `a2, b2, c2` cross each of `a1, b1, c1` and confirming
   every such point is at least `4.7` from `P1`.
3. **26f, the three-point extension.** I did the competitor check for `P3` on two
   lines, not six. Do the other four, or find the one that fails.
4. **27b's segment assignment.** Fifteen segments, twenty-one incidences. If any
   one of the six doubled segments I list is not doubled, `f = 0` breaks and
   `d - f = 6` has to be rebalanced. Re-derive one row of it from the raw table.

**Named object:** a named step with a counterexample, or a statement of which of
the four you regenerated and what you got.

## 2. PythagorAss: price the chained concurrence at k=14

This is yours because reference data 27c says it is the only version of your own
route that can pay, and because you have been three turns from it since T289.

An isolated triple point nets `-1` on the segment budget. A **chained** one can
carry three doubled segments instead of two (`kobon_6_2`'s `{1,3,4}`, verified,
reference data 27c), and a bridge segment is shared between two points, so it is
paid for once and counted once. The question is what the best chained topology
at `k=14` actually yields.

    B(14, 0, c) = 168 - 3c        3T <= B + d        target 3T = 162

- For the 3-cycle of `kobon_6_2` scaled up (6 hub lines, three points, three
  bridges): `kobon_6_2` itself achieves `d = 6`, three per point with the three
  bridges shared. I have **not** proved that is the maximum for that topology and
  I am not asserting it. Whether `k=14` can beat it, with eight further lines
  crossing the hubs, is the question.
- For a path of triple points, or a point of multiplicity four, or two points
  sharing two lines: does `d` per point ever exceed three? My crude per-point
  ceiling is `u + b/2 <= 4.5` with `u <= 3` unshared doublings. **Get the real
  figure from the six-ray picture, the way T293 got the isolated cap.**

**Named object:** the maximum `d` for a chained configuration at `k=14, p=0`,
derived from the ray picture rather than assumed, with the resulting bound on
`T` for `c = 2, 3, 4`, and the line-sharing pattern that achieves it. If no
chained topology beats `3T <= 168`, say so plainly and the concurrence route is
finished on arithmetic alone.

## 3. Euclidn't: reference data 22e, still untouched after twenty-five turns

This was agenda item 2 on T280, assigned to you, and no turn of the cycle went
near it. It is still the last brick in the k=13 insertion program.

`insertion-cap-53-generalizes-beyond-b` rests on **exactly one** unproved thing:

> the two free segments lie on distinct bounded faces.

For any `p=0, c=0, T=47` 13-line table, `B = 143` and `f = 143 - 141 = 2`, with
no geometry. If a single bounded face carried both free segments as **edges
meeting at a vertex**, with unbounded faces beyond each, a clip at that vertex
gives three consecutive gaining pieces on four crossings, no chain fires, and
`g = 7` is arithmetically available on thirteen crossings.

**Named object:** either an argument that two free segments cannot share a vertex
in a 47-triangle 13-line arrangement, or an explicit local configuration showing
they can, with the three gaining pieces named and their entry and exit edges
stated. Both free segments border an unbounded face (reference data 8), so the
shared vertex would be a hull vertex; that is where to look.

## 4. Either: the `c = 0, p = 0` regime, which is the loosest one and is unexamined

Reference data 27a says a 54-triangle `k=14` arrangement with no parallels and no
concurrences has `B = 168` and exactly **six** free segments — more slack than
any other regime, and more than Bader's `f = 3` at 53. Nobody has ever asked what
that arrangement looks like, because for 180 turns the ledger believed `p <= 3`
meant `p = 3`.

The per-line accounting is immediate and checkable by hand: fourteen lines, each
with twelve bounded segments, `168` slots, `162` of them triangle-sides. So
`sum_l deg_T(l) = 162` with `deg_T(l) <= 12`, and the six free segments are
distributed across the lines. At most six lines can fall short of 12, and a line
falling short by `j` uses `j` of the six.

**Named object:** the free-segment distribution profiles for `k=14, p=0, c=0,
T=54` — the partitions of 6 into per-line deficiencies — and, for the two or
three most constrained profiles, what each forces about the lines at `deg_T =
12` (a fully saturated line has every one of its twelve segments a triangle
side, which is a strong local condition; reference data 4 and the segment
exclusivity invariant both bite). Compare against Bader's actual profile at 53,
which reference data 5 gives: three free segments on lines 11, 12, 8, forming a
connected path.

## 5. Standing requirement, unchanged

**Before proposing any chord sequence, state the forced successor at each step.**
Reference data 20a makes most of them mechanical. If your proposal does not name
the successor at every step, it is a permutation, not a walk.

## Killed this day

- **T300's fifteen-line count**, and with it the conclusion that the isolated
  `d=2` program is dead for `k=14` on line supply. Reference data 26.
- **T304's row-neighbour tax.** Reference data 27d. It is reference data 4's
  candidate rule; it removes no degree of freedom.
- **The claim that concurrence buys budget**, including my own reference data
  23e. Reference data 27a: isolated concurrence costs one segment of budget per
  triple point.
- **The k=18 free-segment lookup**, promised at T264 and re-assigned by me at
  T280. Enumerating 93 triangles from an eighteen-row table is roughly eight
  hundred adjacency tests by hand. It is a verifier job, the verifier is gated,
  and assigning it a fourth time would be my error, not yours. It comes back the
  day `python3` runs.
- **Arguing about whether `kobon_6_2`'s lines are "committed" or "free".** T302
  and T303 spent two turns on it with no defined budget on either side and an
  incomplete triangle list on both. The budget is `d <= 2` per isolated point and
  reference data 27b is the complete object. Do not reopen the qualitative
  version.

## Standing prohibitions, still in force

- **New.** Do not concede to an argument that your own side has already refuted.
  If a concession contradicts an earlier turn of yours, say which turn and which
  of the two is wrong. T301 conceded on scale after T297 had established
  ordering.
- **New.** Before comparing a budget against a baseline, recompute the baseline
  in the same turn. T288 imported `p = 3` from a bound that says `p <= 3` and
  three turns of comparison inherited it.
- **New.** If the corpus prints a `"count"` for a table, your triangle
  enumeration matches it before you reason about the table's structure. T302
  found five of seven and T303 and T304 built on the five.
- Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free segment
  count" for any arrangement until you have checked its table for nested
  entries. Reference data 23a is the census; `grep "     \["` is the check.
- Agents do not set `tier`. The field is the referee's.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on, not the
  ones you were handed.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's **crude cap** before analysing its fine
  structure.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check.
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement **averaging** upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 304 turns.
