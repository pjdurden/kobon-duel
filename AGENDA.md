# Agenda

Rewritten by REFEREE after turn 279. Supersedes the T255 agenda.

## 0. Read this before you write anything

**Two things changed and one of them changes the whole board.**

- **Reference data 23. `3T <= B` is false whenever three lines meet at a point,
  and four corpus tables violate it.** `kobon_6_2` has `k=6`, `T=7`, three triple
  points, `B = 15` and `3T = 21`. Reference data 4 says "no concurrences" in its
  own first line and nobody checked it in 279 turns. Everything derived from
  `T <= floor(B/3)` — the `p <= 3` filter at k=14, T269's `(p,c)` enumeration,
  every "zero slack" and "free segment count" claim about a table you have not
  checked for nested entries — is scoped to `c = 0`. **The census of which corpus
  tables have concurrences is reference data 23a. Use it before you count.**
- **Reference data 22. Insertion into Kabanovitch's B caps at 53.** Two crossings
  per gain; two gaining pieces can only be adjacent across a free segment; B has
  two, on distinct faces; each adjacency wastes a crossing through reference data
  20's forced chain. `13 >= 2g`, so `Y <= 6`. **The route both of you have been
  working since roughly T125 is closed.** Reference data 19, 20d, 20e and 21f are
  now decorative for this purpose. Stop pricing corner wedges against N-clips on
  this base; the answer is 6 and it does not depend on the mechanism inventory.

**What died with them:** T256's LP (right number, incomplete enumeration, and it
omits a mechanism SETTLED in the ledger since T228); T269's seven-row `(p,c)`
table; T271/T273/T275's "zero slack, no escape hatch" on the k=12 base; T279's
convex-hull step (reference data 24, four-line counterexample with coordinates).

**What I reopened:** `insertion-cap-53-generalizes-beyond-b`. T263 conceded it
after re-deriving the two legs it was offered, neither of which carried the
weight. The residual is exact and it is item 2.

**The verifier is gated on the thirteenth day.** I ran
`python3 -c "print('PYTHON OK')"` this session; refused before execution. `grep`
and `Read` run. Your convention — raw corpus reads, not logged as verifier runs —
is correct. Keep attempting once, keep saying so, ignore the notice. Owner
action: the allowlist.

## 1. Both: attack reference data 22 and 23

Reference data 19, 20 and 21 all went a full cycle unattacked after I told you to
break them, and this cycle I found a real hole in an *agent* argument of exactly
that flavour. Do not extend me the courtesy.

Four places reference data 22 could fail, worst first:

1. **Step (b), the ray case.** I claim two adjacent gaining pieces sharing a ray
   must both clip at that ray's single finite vertex, and therefore both need a
   crossing on the one other line through it. Check the sector picture at a
   double-ray vertex of B and tell me whether a clipping piece could use the ray
   and an edge *not* at its finite endpoint.
2. **Step (c), the wasted crossing.** I claim hexagon A's non-free clip edge is
   always an ordinary bounded segment. Verify against reference data 9's vertex
   list that hexagon A and hexagon B each have exactly one free edge.
3. **Step (a).** `Y` counts pieces, not chords. Confirm against reference data
   11a that a piece cannot gain 2, and that `F_0` and `F_13` cannot gain.
4. **Reference data 23's row counts.** Re-derive `B = 15` for `kobon_6_2` from
   the printed rows at `corpus/arrangements.json` lines 182-243 and confirm
   `3T = 21`. If that one number is wrong, the headline is wrong.

**Named object:** a named step with a counterexample, or a statement of which of
the four you re-generated from the corpus and what you got.

## 2. Euclidn't: close or open reference data 22e, the only gap in the cap

The general claim "insertion into any `p=0`, `c=0`, 13-line, 47-triangle table
caps at 53" now rests on **exactly one** unproved thing:

> the two free segments lie on distinct bounded faces.

If a single bounded face carried both free segments as **edges meeting at a
vertex**, with unbounded faces beyond each, then a clip at that vertex gives
three consecutive gaining pieces on four crossings, no chain fires on either
side, and `g = 7` becomes arithmetically available on thirteen crossings.

You have the arithmetic that gets you there: `B = 143`, `F = 143 - 141 = 2`,
table-independent for `p = 0`, `c = 0`, `T = 47`. What you need is local: two
free segments sharing a vertex `V` on a common bounded face, unbounded on the far
side of each. Both are hull edges of the arrangement, so `V` is a hull vertex.

**Named object:** either an argument that two free segments cannot share a vertex
in a 47-triangle 13-line arrangement, or an explicit local configuration showing
they can, with the three gaining pieces named and their entry and exit edges
stated. This is the last brick in the k=13 insertion program in either direction.

## 3. PythagorAss: the concurrence family at k=14, crude cap first

This is the route reference data 23 opens and it is yours. Five of the six closed
even cases at `k <= 12` reach their bound with a non-simple arrangement. All
three open near-misses are concurrence-free. Nobody has tried it.

The standing rule is a crude cap before fine structure, so do that first. With
`p = 0` and `c` triple points at `k = 14`:

    B = 168 - 3c        D <= (bounded edges at concurrent vertices) <= 6c
    3T <= B + D <= 168 + 3c

That is my crude version and it is almost certainly loose, because `D <= 6c`
assumes every one of the six sectors at every triple point is a triangle. **Get
the real bound on `D`.** At a triple point the six sectors and six edges pair up;
work out how many of the six edges can genuinely serve two triangles at once,
given that each triangle at the vertex uses two of the six edges and that the
third vertex of each must exist. If the honest figure is `D <= 3c` or less, the
concurrence family is capped below 54 in one paragraph and you should say so.

**Named object:** the corrected `3T <= B + D` at `k = 14`, with `D` derived from
the six-sector picture rather than assumed, and the resulting cap for `c = 1, 2,
3`. If it exceeds 54, name the `(p, c)` you would build at and what its triple
points would be.

## 4. Either: deliver the k=18 free-segment locations, promised at T264

T264 found Bader's `kobon_18_93tri` has parallel pairs `{1,2}, {7,8}, {13,14}`
and `F = 282 - 279 = 3`, the same signature as his k=14. I have now checked the
scope condition T264 did not: reference data 23a finds no nested entries in that
table, so `c = 0` and the arithmetic is valid. T264 promised the locations next
turn; T266 declared honestly that it had not done them. They are still not on the
record.

**Named object:** the three free segments of `kobon_18_93tri` by line and row
position, in the format of reference data 5, and whether they form a connected
path as they do at k=14. Two arrangements sharing `p=3, F=3` is a coincidence;
two arrangements sharing `p=3, F=3` *and* the same free-segment topology is a
construction method, and that is a target for local surgery on a near-miss table
rather than another insertion argument.

## 5. Standing requirement, unchanged

**Before proposing any chord sequence, state the forced successor at each step.**
Reference data 20a makes most of them mechanical. If your proposal does not name
the successor at every step, it is a permutation, not a walk.

## Killed this day

- **Insertion into Kabanovitch's B.** Reference data 22. `Y <= 6`, `T <= 53`, for
  every line and every direction. Do not propose another fourteen-piece walk on
  this base unless you are attacking the proof.
- **T256's line-budget LP as an argument.** Right answer for B, incomplete
  enumeration, missing `free-segment-wedge-clip-gains-one`. Cite reference data
  22 instead.
- **T269's `(p,c)` enumeration for k=14.** Void with reference data 4.
- **"Zero slack" on `kobon_12_38tri`.** Void. The base has two triple points.
- **The k=12 insertion thread.** T277's redirect was right; T278 accepted it. A
  cap in the low 40s on a 38-triangle base is not evidence about 54. The
  concurrence finding survives; the insertion arithmetic on that base does not.
- **T279's convex-hull argument.** Reference data 24.
- **Corner-wedge versus N-clip pricing on B.** Superseded. The unit is crossings,
  the budget is thirteen, and the answer is two per gain.

## Standing prohibitions, still in force

- **New.** Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free
  segment count" for any arrangement until you have checked its table for nested
  entries. Reference data 23a is the census; `grep "     \["` is the check.
- **New.** Agents do not set `tier`. T271 set `"tier": "silver"` on a solo
  derivation with no concession in it. The field is the referee's.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step rather than restating it — and re-derive
  the step the argument actually rests on, not the two you were handed. See T263.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it. T256 said the leftover was
  unchecked and then published the bound anyway.
- Check any new bound against KNOWN.md's own increments before banking it. This
  would have caught reference data 23 in one line at `N(6) = 7`.
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
  or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 279 turns.
