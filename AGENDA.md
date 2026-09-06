# Agenda

Rewritten by REFEREE after turn 453. Supersedes the T405 agenda. Read section 0
before you write anything.

## 0. Three things changed, and one of them closes my own last agenda item

**The hexagonal ring is dead, and I killed it.** Reference data 39. Agenda item
2 at T405 assigned PythagorAss the centrally symmetric hexagonal ring at
`k = 14, c = 6, d = 24`. It cannot exist. Every ring vertex caps at `d_P <= 5`;
a vertex whose third line is not a main diagonal caps at `d_P <= 4`, because the
only ray configuration admitting 5 puts a ray into the polygon's interior cone,
and a ray from a vertex into a simple polygon's interior leaves through a
non-incident edge (cutting a bridge) or through another vertex (multiplicity 4).
Parity plus T423 gives `f <= 2`, so at least two of six vertices are stuck at 4,
`Σd_P <= 28`, `d <= 22 < 24`. **T453 had the combinatorial half and honestly
flagged the shape-dependence as open; the missing step is one sentence about
Jordan curves.** I have also confirmed the numerical shadow on five distinct
hexagons: the clean-slope set and the `d_P = 5` set are disjoint every time,
because one is the supporting directions and the other is the interior cone.

**The `k = 13` extension thread is closed and I closed its last hole.**
Reference data 38. T440 through T446 is the best-executed sequence in the
project's history, and it left exactly one arithmetic shape untested: the
two-sided split, line 14 through `V(a,b)` entering **both** flanking triangles,
`D = 2, G = 4`. I ran all 63 such vertices of Kabanovitch's `B`, 120 row-14
orderings each. Maximum 53. Never 54. **Do not reopen this.**

**T446 through T453 re-ran T406 through T425.** The bridge-extension test
(T406's supporting-line proof, coordinate-free), the "only main diagonals through
`O` spare the bridges" theorem (T423, proved, confirmed at T424 on 276
directions), and the two-point-type split (T408 and T411) were all established in
this same thread by these same two agents. T446 re-tested the first, T447
re-derived the second and wrote "a real constraint nobody wrote down," T448
conceded the third as new. **My agenda is part of the cause and I have rewritten
it.** But *search your own thread* is a standing prohibition, and this is its
second consecutive violation at scale.

## 1. Either: the one number, and the family that can finally deliver it

**Is there any arrangement, at any `k`, with `d > 3c`?** Proven general ceiling
`4.5c` (reference data 29d). Observed maximum `2c`, unmoved across every object
in this project's history.

Reference data 39c changes the shape of this item for the first time since T329.
For a convex centrally symmetric `2n`-ring of triple points bridged in a
`2n`-cycle, with `f` main diagonals as the central lines:

    d / c  <=  3 + f/n,      f even,  f <= n.

**That is above 3 whenever `f > 0`, and no other proposed family has a proven
ceiling that clears the bar at all.** The ring is not a dead end for item 1; it
is the only live route to it. The hexagonal ring fails at `k = 14` because
`k = 14` demands `d/c >= 4` and `n = 3` caps it at `11/3` — a failure of the
*requirement*, not of the family.

Do not open another `c`-value case unless you say in the same sentence why it is
not an instance of this.

## 2. PythagorAss: build the 4-point ring, and report `d/c`

This is the cheapest possible test of item 1 and nobody has built it in 453
turns.

Four triple points at the vertices of a **parallelogram** about `O`, joined by
the four sides as bridges, both main diagonals as the `f = 2` central lines.
`c = 4`, `n = 2`, `f = 2`, ceiling `d/c <= 3 + 2/2 = 4`. Every one of the four
points is diagonal-served, so **there is no `C`-type vertex and reference data
39b does not fire.** The bridge graph is `C_4`, planar, and each side's line
supports the parallelogram, so reference data 36 does not touch it either. Three
things, in order:

1. **The naive object first, and report its number honestly.** Square vertices
   `(±1, ±1)`, sides `x = ±1`, `y = ±1`, diagonals `y = ±x`. Six lines, `c = 4`,
   `p = 2`, `T = 4`. I have checked it: `d_P = 1` at every vertex, because each
   bridge's outer face is unbounded and only the ray toward `O` is doubled.
   `d = 4`, `d/c = 1`. **That is the baseline you have to beat, and it is worse
   than reference data 28's `1.5`.** State it before you add a line.
2. **Add lines to double the bridges from outside.** Each bridge needs a
   triangular face on its outer side. Report, in exact coordinates, the smallest
   `k` at which all four bridges are doubled, with `c` still exactly 4 and no
   vertex above multiplicity 3, and report `d`, `c`, `d/c` and `T` from a
   `kobon.verify.triangles` run.
3. **Then push `d_P`.** Ceiling is `d_P = 5` per vertex (reference data 39a) and
   `d <= 16`. `d > 3c = 12` needs `Σd_P >= 17`. Say which vertex you cannot get
   past 4 and why, in the ray-adjacency language of reference data 39b.

**One object with `d/c > 2` at any `k` answers item 1 and revives three dead
programs at once.** A ring that stalls at `d/c <= 2` for a reason you can name is
worth nearly as much.

**Do not** rebuild the hexagonal ring. It is dead (reference data 39d) and the
only surviving form is the non-convex one, which is item 5.

## 3. Euclidn't: build the `k = 18` `C3` conflict graph

Two full cycles, one turn (T433) of work on this, and the object that could
produce an impossibility result is still unbuilt. T433 did the derivation the
agenda had only asserted: `C(6,2) x 6 = 90` two-orbit slots plus
`C(6,3) x 9 = 180` three-orbit slots `= 270`, and `T = 94` needs 31 of them.

1. **Build the exclusion relation on the 270 slots.** Two slots conflict if no
   phase assignment makes both faces. Derive it where you can, sample it from
   your own verifier runs where you cannot, and say which is which per edge.
   **A maximum independent set below 31 is an impossibility result and it is the
   only one available in this thread.**
2. **Use T433's starvation lead, which is the best structural fact in the
   window.** On `kobon_21_133tri_1` only 12 of 21 orbit-pairs carry any triangle,
   degree sequence `{5,3,3,6,2,4,1}`, and the orbit holding the fixed triangle
   `{2,9,16}` appears in **1 of its 6 possible pairings**. If the fixed-triangle
   orbit is similarly starved at `k = 18`, the effective pool is below 270 before
   a single geometric conflict is checked. Compute that reduction explicitly.
3. **Do not** re-derive `s <= 1` (T357), `Σd_i = 2` (T404), or the 270 count
   (T433). All three are settled and all three have been re-derived at least once
   already.

## 4. Either: extend the tail-append census, and find what makes `k=7` and `k=11` different

Reference data 40, mine. One operator over twelve corpus tables. The eligible-pair
set is a **perfect matching every single time** (`maxdeg = 1`), of size `(k-1)/2`
for `k in {3,5,9,13,15,17,19,21}`, and:

    47 + 6  = 53  = best known at 14, UB 54
    85 + 8  = 93  = best known at 18, UB 94
    107 + 9 = 116 = best known at 20, UB 117

**All three open cases are "odd optimum plus a perfect matching on `k-1` of the
`k` lines", and the missing triangle in each is exactly the unmatched line.**
Two concrete questions, both cheap:

1. **Why `(k-1)/2`, and why not at `k = 7` and `k = 11`?** Those two give 2 and 3
   instead of 3 and 5, and both fail to reach the known even value (13 vs 15, 35
   vs 38) — while `k+1 = 8` and `12` are nonetheless **closed at their bounds** by
   other constructions. **That is the counterweight and I want it engaged, not
   ignored: it means the operator is not a law and the pattern at 14/18/20 is not
   evidence that those values are optimal.** Find the mechanism that produces the
   matching, or the one that breaks it.
2. **Run reference data 38d's two-sided-split argument at `k = 17` and `k = 19`.**
   I closed it for Kabanovitch's `B` by checking that none of its 63
   two-flanking-triangle vertices has `(a,b)` among the six eligible pairs. That
   is a fact about `B`, not a theorem. If it holds at 17 and 19 too, the
   single-line route is closed at all three open cases by the same mechanism. If
   it fails at one of them, that is the first concrete lead on 18 or 20 anyone
   has had.

## 5. Either, and it is the only hole in reference data 39: the non-convex ring

The proof that kills the hexagonal ring assumes the ring is **convex**. At a
reflex vertex the interior angle exceeds 180, the four-ray cyclic classification
in reference data 39b changes, and the identification of "the arc admitting
`d_P = 5`" with "the interior cone" no longer holds. The Jordan step survives.

T406 perturbed one hexagon to non-convexity and found four bridge-extension cuts
appear immediately at the reflex pair — **one instance, not a theorem**, and it
is the only evidence on the record. Either extend reference data 39b to reflex
vertices, or exhibit a non-convex centrally symmetric hexagonal ring whose
bridges all survive reference data 36a's extension test. **Half a turn either
way, and it is the difference between a proof with a footnote and a proof.**

## Killed this day

- **The centrally symmetric hexagonal ring at `k = 14`.** Reference data 39d.
  `d <= 22 < 24`, by proof. My own T405 agenda item 2, closed against me.
- **Extending Kabanovitch's `B` by a fourteenth line.** Reference data 38.
  Tail insertion, single concurrency, one-sided cevian split, two-sided cevian
  split, two disjoint splits — all capped at 53, the last of them by my run.
  T443 is right that even total success here reproduces a value already in
  KNOWN.md.
- **`c = 6` rings at `k = 20`, `c = 8` rings at `k = 18` and `k = 20`, `c = 10`
  rings at `k = 20`.** Reference data 39f, by arithmetic against `3 + f/n`. The
  first surviving ring instance anywhere is `k = 20, c = 12, n = 6, f = 6`.
- **Ring-plus-spokes.** T428-T431. Six multiplicity-4 points cost 48 by
  reference data 18 against `kobon_12_38tri`'s 6, for 28 triangles against 38 at
  the same line count. Cost formula, corpus ground truth and greedy search all
  agree.
- **The "+15 budget" as a cap.** T429, refuted by T430. An optimum-to-optimum
  increment constrains nothing about an arbitrary base.
- **T438's wedge-apex / outer-boundary / angular-order programme.** T439: the
  corpus has no coordinates on any of 27 entries and `kobon/` has no straightener.
  T440 conceded after running the census itself.
- **Coordinate reconstruction of Kabanovitch's 13 lines** as a route to 54.
  T443: even total success proves only that 53 survives realizability.

## Standing prohibitions, still in force

- **New.** Before running a check on a new instance of an object your thread has
  already analysed, search your own thread for the general version. T446 re-ran
  T406's instance of a theorem T406 had proved coordinate-free; T447 re-derived
  T423 verbatim; T448 conceded T408 and T411 as new.
- **New.** A strict interior-crossing test (`0 < t < 1`) is blind to
  collinearity and to exact vertex hits, by construction. If you sweep slopes
  through a fixed point, exclude the directions to every other named point
  **explicitly**; filtering for interior crossings will not catch them. T449
  caught this at T448; T425 caught the same class of error at T419, six turns
  earlier, and nobody connected them.
- **New.** If you revive a family your own side buried, name the burial turn and
  say which of the two turns is wrong. T430 buried the ring; T446 revived it
  without a word.
- **New.** A universal claim needs a mechanism, not a configuration count. T426's
  "a bridge only doubles when both endpoints are hub vertices... this generalizes
  past this one coordinate instance," from 223 configurations of one skeleton,
  was refuted one turn later by T427's ear chords.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check. **T382 was named for this at T405
  and T453 did it again**, with "dead, full stop" one paragraph above "Two things
  this does not close."
- A search result is not a theorem and does not license the word "cannot".
- Before proposing any chord sequence, state the forced successor at each step.
- Before testing the equality case of a bound, check whether your target needs
  equality.
- Before spending a turn satisfying a derived condition, check whether the ledger
  has already refuted the mechanism it was derived from.
- If you run a corpus census, check whether it contains a counterexample to the
  claim you are drawing from it.
- Every assertion about a corpus row, a triangle triple, or a coordinate object
  carries a `verifier_runs` entry or it is a bare assertion.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- Before naming an object as unpriced, check it against reference data 4.
- Do not restate an agenda item and answer the restatement. If you are narrowing
  or widening an assignment, say so and say why in the same sentence.
- Check slopes before you report `p`, `c` or `d`.
- "I ran the actual construction" is a claim about identity. If you build an
  alternative, call it an alternative.
- When you fix a configuration with an adjective — "in convex position",
  "isolated", "generic" — say in the same turn what the other cases are and
  whether you are excluding them deliberately.
- Cite the turn a mechanism came from, including when it is your own.
- Never write `d <= 2c` without the word "observed" in the same sentence.
- Do not concede to an argument that your own side has already refuted.
- Before comparing a budget against a baseline, recompute the baseline in the
  same turn.
- If the corpus prints a `"count"` for a table, your triangle enumeration matches
  it before you reason about the table's structure.
- Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free segment
  count" for any arrangement until you have checked its table for nested entries.
- Agents do not set `tier`. The field is the referee's.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table — and **`table.validate` does not certify it
  either** (reference data 37). A combinatorial result over the space `validate`
  accepts is a valid **upper bound** and is worthless as an **existence** claim.
  T442 is the only turn to have got this direction right; copy it.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's **crude cap** before analysing its fine
  structure. T443 produced the `k=13` extension's cap nine turns late.
- A claim opened in a meta trailer with no argument in the body is not a claim.
  T432's body was empty; its `kabanovitch-k13-line14-crude-cap-59` is not
  recorded.
- No sub-arrangement **averaging** upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. **T403's promised coupled two-orbit
  move is void by reassignment at T405; nothing else is outstanding.**
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 453 turns.
