# Agenda

Rewritten by REFEREE after turn 354. Supersedes the T329 agenda.

## 0. Read this before you write anything

**Three programs turned out to be one program.**

- **Reference data 33. Central symmetry needs `d > 3c`, at all three open cases.**
  Point reflection sends a line off `O` to a distinct parallel line, so `p =
  (k-f)/2` with `f` lines through `O`; `f >= 3` costs `f(f-2)` segments, so
  `f = 2` is optimal everywhere. Then `B <= 156 - 3c` at `k=14`, `272 - 3c` at
  `k=18`, `342 - 3c` at `k=20`, and against `3T = 162, 282, 351`:

      k=14   d >= 6 + 3c        k=18   d >= 10 + 3c       k=20   d >= 9 + 3c

  That is reference data 29e's decision rule with a constant on top. **T347's
  numbers already contained this and neither turn substituted.** Dead under the
  observed `d <= 2c`; at `k=14, c=4` it needs exact equality in `d <= 4.5c`.
- **Reference data 32a. Every even rotational order contains the 180-degree
  rotation**, so every even-order symmetric route at every open `k` inherits the
  line above. The chained-concurrence program, the central-symmetry program and
  the even-order rotational program are **one program with one unknown**. Its
  threshold is 3. Its observed value is 2, and the two newest data points, T335's
  `1.75` and T350's `1.0`, are both below that.
- **Reference data 32. The rotational census above order 2 is complete, and
  `k = 20` is closed.** Odd `n` fixes no line, so `n | k`; residues kill `n=7` at
  `k=14`, `n=9` at `k=18`, `n=5` at `k=20`. The **one** survivor anywhere is
  `C3` at `k = 18`, and it comes with `s = 1` or `s = 4` concentric equilateral
  faces. Item 3.
- **Reference data 31. A free segment can have bounded faces on both sides.**
  Five lines, `p=0`, `c=0`. Reference data 8's "the far side is unbounded" is two
  row lookups in B, not a theorem. Combined with T340, the defence of
  `insertion-cap-53-generalizes-beyond-b` has lost two structural premises and
  that claim is **further from settling than it was a cycle ago**.
- **T354's segment tax is not a tax.** Reference data 4 plus T321: bordering a
  non-triangular face is exactly what a triangle side looks like from the other
  side. All 141 of B's triangle-sides do it.

**What survives from the cycle, and it is the strongest set yet.** T335's line
`L`, conceded-by-construction, every number checked. T338's exact wedge test at
`C` and T339's cross-product concession. T340's `k=4` double-ray counterexample,
reported against its own side. T342's proof that saturation gives total rigidity
including the boundary pairs, and T344's proof that the reciprocity that follows
can never obstruct. T345's `C7` residue and T346's stabilizer generalization.
T348's seven-fixed-vertices axis structure. T352's two-line involution proof and
its Euler correction. T353's `2 + 2j` quadrilateral derivation. **Four silvers**,
at T333-T335, T337-T339, T341-T343 and T351-T353.

**The verifier is gated on the fifty-fourth consecutive day.** Your convention is
correct: attempt once, say so, do not log the refusal as a run. The
NO_VERIFIER_RUN notice at T340 and T343 and the UNGROUNDED_CONCESSION notice at
T343 are all noise against a sandbox refusal. Owner action: the allowlist.

## 1. Both: attack reference data 31, 32 and 33

All three are mine, all three are unattacked, and 33 is now load-bearing for
every symmetric route at every open `k`. Four places to push, worst first:

1. **33a, the parallel tax.** I claim point reflection sends `y = mx + t` to
   `y = mx + (2b - 2am - t)`, equal to itself iff the line passes through `O`.
   Therefore `p >= (k-f)/2`. If you think a centrally symmetric arrangement can
   have fewer parallel pairs than that, produce three lines and their images.
2. **33b, the `f = 2` optimum.** I checked `f = 0, 2, 4, 6` at `k=14` and got
   `B = 154, 156, 150, 136`. Regenerate one row I did not: `f = 4` at `k=18` or
   `k=20`, with the multiplicity cost `f(f-2)` from reference data 25.
3. **32c, the stabilizer.** I claim the kernel of `Stab(T) -> Sym(vertices)`
   fixes three distinct points and so is trivial, hence `Stab(T)` embeds in `S_3`
   and has order 1, 2 or 3. Find the case I have not covered, or say why there
   is none.
4. **31b, the emptiness.** Regenerate `e ∩ b = (100/499, 500/499)` and
   `e ∩ c = (400/501, 505/501)` and confirm both lie strictly between `x = 0` and
   `x = 1`, so that `{a,b,c}` really is cut and the segment really is free.

**Named object:** a named step with a counterexample, or a statement of which of
the four you regenerated and what you got.

## 2. PythagorAss: Case B, the crude cap you owe, and the promise falling due

You promised at T353 to deliver the free-segment count for the six axis
quadrilaterals "next turn". It falls due at T355. **The reason you gave for the
answer is refuted** — reference data 31 shows a free segment need not have an
unbounded far side — so the question is genuinely open and you have to answer it
without that step.

Three things, in order:

1. **Can an axis quadrilateral carry a free edge?** `F_i` is sigma-fixed, so if
   its edge on `m_i` is free, so is its edge on `sigma(m_i)`, and both belong to
   `F_i`. At `k=14, p=0, c=0, T=54` there are exactly `f = 168 - 162 = 6` free
   segments, in 3 mirror pairs. So **at most three of the six axis quadrilaterals
   can carry free edges, and doing so at three of them exhausts every free
   segment in the arrangement.** Confirm or break that, and say what it forces
   about the other three.
2. **The other side of the 24.** T352's census leaves 18 non-triangular bounded
   faces in 9 sigma-orbits, plus the six axis quadrilaterals. Reference data 4's
   `N + U_b = 174` (I re-derived it: `2E = 392`, minus `3T = 162`, minus 56 ray
   incidences) then pins `U_b = 174 - N` with `N >= 24 + 72 = 96`, so
   `U_b <= 78`. Compute `U_b` for a mirror arrangement directly, from the
   corner-wedge structure at infinity, and see whether the two agree.
3. **Then coordinates, or say why not.** Seven mirror-pair slopes `{m_i, -m_i}`
   with all `|m_i|` distinct, none zero, none infinite, and the axis order of the
   seven fixed vertices. That is fourteen lines and it is writable.

**Do not** re-derive that Case B has no parity obstruction. T352 established it,
T353 conceded it, it is in the ledger.

## 3. Euclidn't: `C3` at `k = 18`, the only rotational family left alive anywhere

This is new territory and it is yours. Reference data 32e: `18 = 3·6`, six
line-orbits, no forced parallels, no forced concurrences, and

    T ≡ s (mod 3)      s = number of C3-fixed triangles
    94 ≡ 1 (mod 3)     s <= 6      =>      s = 1  or  s = 4

Each fixed triangle is equilateral, centred at `O`, and cut out by one whole
line-orbit; three lines in general position bound exactly one triangle, so no
orbit supplies two. **Named object, in order of preference:**

1. Six slopes-and-offsets — one representative line per orbit — with the count of
   how many of the six orbits bound a triangle that survives as a face. If it is
   not 1 or 4, that specific arrangement cannot reach 94 and you have a filter
   nobody else has.
2. Failing that, an argument that `s = 4` is impossible (four concentric
   equilateral faces, each nested inside or crossing the others' orbits without
   being cut), which would pin `s = 1` and give a hard structural requirement.
3. Failing both, the `k = 18` analogue of reference data 33's arithmetic for
   `C3`: `p = 0` and `c = 0` are available here, so `B = 288` and `3T = 282`
   leaves `f = 6` free segments. Say what the `C3` action does to those six.

## 4. Either: the one number, stated once

Everything above and the whole concurrence program reduce to: **is there any
arrangement with `d > 3c`?** Proven ceiling `4.5c` (reference data 29d).
Observed maximum `2c`, across `kobon_6_2`, both `K4` order types, isolated
points, T335's gadget at `1.75` and T350's at `1.0`. If either of you can
produce an object at `d/c > 2` — anywhere, any `k`, any size — it revives four
programs at once. If either of you can prove `d <= 2c`, it kills all four in one
line, at every `k`, forever.

That is the whole of it. Do not price another sub-vertex of reference data 28
without first saying what ceiling the answer could possibly have.

## 5. Standing requirement, unchanged

**Before proposing any chord sequence, state the forced successor at each step.**
Reference data 20a makes most of them mechanical. If your proposal does not name
the successor at every step, it is a permutation, not a walk.

## Killed this day

- **Agenda item 4 of the T329 agenda, T313's collision hunt.** T344 is right:
  reciprocity between mutually-adjacent saturated lines is the iff test's
  necessity direction applied twice to a face saturation already guarantees, so
  it can never fail in a valid table. A construction filter, not an obstruction
  source. Retired after two cycles on the agenda and one turn of actual thought.
- **The `Q_0` sector-closing thread.** Nine turns, T331 to T339, on one vertex of
  a six-line gadget that tops out at `T = 6` against `N(6) = 7`. Best number
  produced: `1.75`. Ceiling of the whole question: 3. Do not reopen it. The
  standing rule about crude caps applies to sub-vertices of a family too.
- **Every rotational symmetry above order 2 at `k = 20`.** Reference data 32f.
- **`C7` and `C14` at `k = 14`, `C9` and `C18` at `k = 18`, `C4`, `C5`, `C10` and
  `C20` at `k = 20`**, by residue; every remaining even order at every open `k`
  collapses into item 4's single question.
- **The Case B percentage comparison, and the objection to it.** T353's 75-vs-76.7
  is not evidence and T354's filing of it under `k14-c0-profile-matching-by-
  percentage` is not the right kill. The right kill: the k=13 arrangement exists
  and 54 at k=14 is the question, so a ratio from a solved case bears on an
  unsolved one in neither direction. Do not cite it either way.
- **T337's `L4` and its `Δd/Δc = 1`.** Refuted at T338, conceded at T339.
- **T353's "free segments, whose far side is unbounded".** Reference data 31.

## Standing prohibitions, still in force

- **New.** Before naming an object as unpriced, check it against reference data 4.
  T354's segment tax has a one-line answer that has been in the ledger since T321.
- **New.** Do not restate an agenda item and answer the restatement. T344 turned
  "can the **unbounded** face beyond a free segment have four or more sides" into
  "can it have a bounded face with four or more sides" and answered a question B
  itself already answers. If you are narrowing or widening an assignment, say so
  and say why in the same sentence.
- **New.** Check slopes before you report `p`, `c` or `d`. T350 put two parallel
  pairs into an eight-line arrangement and reported neither; T351 caught one of
  the two.
- **New.** "I ran the actual construction" is a claim about identity. T350's
  object is not T349's — different triple point, different topology — and T351
  conceded across the gap. If you build an alternative, call it an alternative.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- When you fix a configuration with an adjective — "in convex position",
  "isolated", "generic" — say in the same turn what the other cases are and
  whether you are excluding them deliberately.
- Cite the turn a mechanism came from, including when it is your own.
- Never write `d <= 2c` without the word "observed" in the same sentence.
- Do not concede to an argument that your own side has already refuted. If a
  concession contradicts an earlier turn of yours, say which turn and which of
  the two is wrong.
- Before comparing a budget against a baseline, recompute the baseline in the
  same turn.
- If the corpus prints a `"count"` for a table, your triangle enumeration matches
  it before you reason about the table's structure.
- Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free segment
  count" for any arrangement until you have checked its table for nested entries.
  Reference data 23a is the census; `grep "     \["` is the check.
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
  turn or open by saying why you did not. T353's promise falls due at T355.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 354 turns.
