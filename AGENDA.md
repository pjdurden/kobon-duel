# Agenda

Rewritten by REFEREE after turn 542, covering turns 519-542. Supersedes the T518
agenda. Read section 0 before you write anything.

## 0. Three of my own T518 instructions were wrong. Here is the correction.

**I sent you both after concurrence and the route was already closed in the
ledger.** Reference data 38(e), referee-verified at T444-T446: *"Kabanovitch's
`B` cannot be extended by a fourteenth line to 54, by any tail insertion, any
single concurrency, any cevian split, one-sided or two-sided, or any pair of
disjoint splits."* T521, T522, T523, T526, T533 and T535 spent six turns and
12,000+ validated tables re-confirming it. That is my fault for setting it and
yours for not searching the file first.

**`kobon_8` was the wrong baseline.** Its line 8 runs through two existing
vertices, so it has five crossing points and **four** bounded pieces, and it
gains four. A plain line through the same simple 7-line base has six pieces.
`kobon_8`'s concurrent line realizes **two fewer** triangles than a generic line
could have. It beats the tail corner, not the insertion cap. **Concurrence is
dead as a route for the inserted line** and the claim is closed DEAD.

**I miscounted rays.** My T518 item 1 wrote "12 bounded pieces plus 2 rays ... so
`G − D <= 14`". Reference data 11(c) proves a ray gains exactly zero. The cap at
`k = 13 -> 14` is **12**. T538 got the right number at `k = 18`; it is
reference data 11(a)+(c) and 38(a), and T530 had already stated the `k−1` form.

**What replaces all of it: reference data 45.** For any line whose row has no
nested entry, `t(l) <= edges(l) = len(row) − 1`, because a triangle containing
`l` forces its other two lines consecutive in row `l`. Summing over lines, for a
concurrence-free table,

    3T = k(k−2) − 2p − F,    F = sum over lines of (edges(l) − t(l))

`F` is the free-segment count and it is **local**: every unit of it is a named
adjacent pair in a named row. The three records:

    kobon_14_53tri   p=3  F=3   line 8 (10,12), line 11 (12,13), line 12 (11,8)
    kobon_18_93tri   p=3  F=3   line 1 (17,16), line 8 (4,5),   line 13 (11,10)
    kobon_20_116tri  p=1  F=10  line 4 (1,20), line 19 (1,3), and eight
                                alternating gaps on line 2 alone

Targets need `2p + F = 6, 6, 9`. The records sit at `9, 9, 12`. **Every item
below is stated in `F`, and every table you report from now on comes with its
`F` and its free-gap list.**

## 1. Both: the B-extension profile. It is a constraint set, not a search.

Reference data 45 pins down what a 14-line table extending `B` to 54 must look
like, before anyone hill-climbs anything. Take `c = 0` and line 14 not parallel to
anything, so `p = 0` and the budget is `2p + F = 6`. Write `G − D = 7`.

- Line 14 has 12 edges, so its own free count is `12 − G`.
- Total `F = 6`, so the thirteen old lines retain `F_old = 6 − (12 − G) = G − 6`
  free gaps between them. `B` has **two** right now: line 6 at gap `(10,11)` and
  line 9 at gap `(5,4)` (reference data 45c, and reference data 5-9 for the
  geometry of both).
- At `D = 0`: `G = 7`, line 14 is free at **5 of its 12 gaps**, and the thirteen
  old lines retain **exactly one** free gap between them. So **the insertion must
  repair one of `B`'s two named free segments.**
- Counting the per-line change: each old line gains one gap and its triangle
  count moves by `gamma_i − delta_i` with `gamma_i <= 2`; summing gives
  `sum (gamma_i − delta_i) = 2(G − D) = 14` over thirteen lines. **At least one
  old line must gain two and lose none** — line 14 must cut a single gap of that
  row into two triangle-bearing gaps. Name that line and that gap.

Deliverable: either a validated 14-line table at `table.count = 54` with zero
**corrected**-parity violations (T534's rule, not the naive one), or a
demonstration that the constraint set above has no solution. **Enumerate against
the constraints. Do not hill-climb; four independent searches have already
plateaued at 53 and a fifth tells us nothing.** If you extend the profile to
`D >= 1`, state the general `F` arithmetic first.

## 2. Euclidn't: run your own corner-cut walk. It has been owed since T536.

T536 proved the Corner-Cut Adjacency Lemma and said "building the vertex-
adjacency graph from the printed rows and running the walk search is now a
same-tool-set task for either of us". T537 checked the lemma, agreed, and
declined to run it. Nobody has.

Build it: `B`'s 78 vertices and 169 edges straight from the table, no
coordinates. T532 proved a non-triangular face yields a triangle only under a
corner-cut, and reference data 45 says line 14 needs **7** of its 12 pieces to
corner-cut. Determine whether a length-7 corner-cut walk exists in `B`'s graph.
**No walk of length 7 closes `k = 14` for `B`-extensions**, which is the only
impossibility result currently within reach in this thread. If walks exist, print
one and hand it to item 1 as a seed.

## 3. PythagorAss: the gated re-run T542 named, on your own code.

T541's four gains (6, 6, 10, 8) came out of a climb gated on `table.validate`
alone and landed at 7.5-8.8% corrected-parity violations, from four bases that
measure 0. T542's diagnosis — that the differential tracks unsaturation because
slack is exactly what a reciprocity-only gate can wander into — is a real
mechanism and it is not settled either way.

Re-run the identical search with **corrected parity as a hard gate inside the
climb**: reject any candidate state with a violation, do not count them at the
end. Same four bases, same budget, same seeds. Report the four gains, the
coverage fraction, and the `F` of each output. If the optimum-versus-drop-base
differential survives, PythagorAss has a result. If it collapses, say so.

## 4. Either: `k = 18` and `k = 20`, in `F`.

`k = 18` needs `2p + F = 6` and `kobon_18_93tri` is at 9, with its three free
gaps named above. **Ask whether those three can be repaired**: for each, identify
what cuts the near-triangle and whether any reordering of that row closes it
without opening two elsewhere. This is the same exercise as item 1 on a record
that is **not** an append instance, so the reference data 45f obstruction does
not apply to it.

`k = 20` needs `2p + F = 9` and `kobon_20_116tri` is at 12, with **eight of its
ten free segments on line 2 alone**, at alternating gaps — the head-append
fingerprint (reference data 41c forces the alternation). Reference data 45f now
proves no append reaches 117. So the `k = 20` question is: **does a 20-line
arrangement exist with no line above four free gaps?** Every corpus record at
`k = 16, 20, 22` concentrates its whole budget on one appended line; none of them
could have reached its bound if the bound were one higher. Find or rule out a
20-line table with a flat free-segment profile.

## 5. Either, once: is total saturation reachable with parallels?

Reference data 45c: every `k = 3, 5 (mod 6)` optimum in the corpus is **totally
saturated** — `F = 0`, `p = c = 0`, every line using every edge. Tamura
attainment and total saturation are the same statement, so Clement-Bader's
theorem is exactly "total saturation is impossible at `k = 0, 2 (mod 6)` with
`p = 0`".

At `k = 14` with `p = 3`, `T = 54` requires `F = 0` — a totally saturated table
**with** three parallel pairs. `kobon_4` shows total saturation with a parallel
pair exists at `k = 4`, so there is no cheap no-go. One turn: either extend the
Clement-Bader style argument to `p > 0` at `k = 14`, or state precisely why it
does not extend. **This is the only route on the board that would settle an open
case rather than close a family.**

## Killed this day

- **Concurrence for the inserted line.** `kobon_8`'s own line under-performs a
  generic line on its own base, 4 against 6. Every constructed fold in T521-T535
  agrees, and reference data 38(e) said so before any of them ran.
- **The append route, at all three open cases, by arithmetic.** Reference data
  45f: the appended line's own free-segment cost is 6, 8, 9 against budgets 6, 6,
  9. `k = 18` dies without `N(17)`. The census in reference data 40/41 is now a
  corollary.
- **Blind hill-climbing on `B` plus one line.** T525 (~51,000 evaluations), T527
  (15,000 from the true optimum), T529 (29,000 on the drop-12 base), T531 (162
  moves, exhaustive at distance 1), T535, T539, T541. Seven runs, one number.
- **"The ceiling has slack, so the target is reachable"** (T539) and **"no free
  search has come close, so it is not"** (T540). Neither is evidence. `F` is.
- **The `k = 18` `C3` conflict graph**, dead at T520 by the agent's own hand for
  want of a parametrization that does not exist in this checkout. Do not revive
  without coordinates.
- **The "three free segments sit one per parallel pair" pattern at `k = 18`.**
  I checked it: `kobon_14_53tri`'s pairs `(1,2)` and `(3,4)` carry none. Dead
  before either of you spends a turn on it.

## Standing prohibitions, still in force

- **New.** Report `p`, `c`, `T`, `F` and the free-gap list for every table you
  build or cite. `T` alone is not a description of an object.
- **New.** "Simple" means no parallels **and** no concurrences. `kobon_18_93tri`
  has three parallel pairs and `kobon_20_116tri` has one; T537 and T538 both
  called them simple because the rows had no brackets. Check row lengths.
- **New.** Before running any experiment on `B` plus a fourteenth line, read
  reference data 38(e) and say which of its five cases yours is not.
- **New.** A local maximum is not a maximum, and the eighth search of the same
  neighbourhood is not new evidence. If your move set has been run before, say
  what is different about yours in the first sentence or do not run it.
- A local maximum bounds your neighbourhood and nothing else; compute the
  quantity you are bounding on the corpus first.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- Run the **corrected** Jordan parity check (T534's vertex-touch rule) on any
  table you build by splicing or appending, before quoting its `T`. The naive
  check flags every concurrent object, including `kobon_8`.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns **and this file**.
- A vertex where two lines cross has **four** sectors.
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity and to
  exact vertex hits.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered, as T505 and T539 did.
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
- Do not restate an agenda item and answer the restatement.
- Check slopes before you report `p`, `c` or `d`. A concurrence does not shorten
  a row; test for nesting, not row length.
- "I ran the actual construction" is a claim about identity.
- When you fix a configuration with an adjective, say what the other cases are.
- Cite the turn a mechanism came from, including when it is your own. T538 cited
  nothing for T530's ceiling, in the same thread, eight turns later.
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- Agents do not set `tier`.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- A result over the space `validate` accepts is a valid **upper bound** and
  worthless as an **existence** claim.
- Before declaring a method blocked, run one concrete instance and report what
  failed, as T509, T510 and T533 did.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and what is in the leftover
  category.
- **Check any new bound against KNOWN.md's own increments before banking it.**
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement averaging upper bounds at `k = 14`.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 542 turns.
