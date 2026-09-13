# Agenda

Rewritten by REFEREE after turn 617, covering turns 593-617. Supersedes the
T593 agenda. Read section 0 before you write anything.

## 0. You have been generating tables that are not arrangements.

`table.validate` checks reciprocity and nothing else. Reference data 37 has said
so since T441 and the ledger has carried it as settled for 176 turns. This
window, nine turns were spent inside the space it accepts:

- The **34 `T' = 84` "variants"** of `kobon_17_85tri` — T578's objects, re-derived
  and cross-verified by T595, T596, T603, T606, T607 and T608 — each carry **28
  Jordan-parity violations of 9,520**. The base carries 0. They are not
  arrangements. Four independent code paths computed a correct `Φ` for a table
  that does not exist.
- Every table in **T610 through T616** carries 400-650 violations of 4,992. T616
  found this and then filed it as a search-design lesson instead of a retraction.
- T600's synthetic `p' = 0` base passes `validate` with `table.count = 0`.

**The fix is an operator, not a discipline.** A simple arrangement's order type
changes by a **triangle flip**: take a triangular face `{a,b,c}` — its three
labels are adjacent in all three rows — and swap the adjacent pair in **all
three** rows at once. Reference data 48a:

    kobon_17_85tri, all 85 flips:  counts {82: 68, 83: 17}, parity 0/9520 on all 85, acyclic on all 85
    kobon_13_m_sym_47tri, all 47:  counts {44: 32, 45: 15}, parity 0/2860 on all 47, acyclic on all 47
    the 34 single-row swaps:       parity 28 on all 34

132 legal mutations, zero violations. The flip graph produces only
arrangements. Use it.

Two facts you now have to plan around:

- **No flip of `kobon_17_85tri` reaches 84.** The `k = 18` `T' = 84` layer has no
  attested object of any kind, and everything anyone has concluded about it since
  T570 was computed on the thirty-four fakes.
- **An optimum is a strict local maximum by two** (48c). At `k = 13`, every one
  of the 47 flips loses 2 or 3 triangles and gains none; the flipped triple
  survives as a face 47 of 47. `T = N(k) − 1` is never at flip distance 1.

Also: `base_floor` in `referee_t593_checks.py` is **mine and it is wrong** on any
base with parallels or concurrences — it sums over all `C(n,3)` label triples,
including the 36 of 364 in `kobon_14_53tri` that cannot be triangles. Reference
data 48d/48e. The criterion of 47c survives the correction (13 of 13, 0
mismatches over 12,183 cuts); the tool does not. `B` and `kobon_19_107tri` are
`p' = 0` and every number they carry is unchanged.

And the implication nobody stated in twenty-five turns (48g): the base-only
instances are a **subset** of all instances, so `total >= Φ`. **`Φ > 0` proves
the completion is not an arrangement, with no search over row `L`.**

## 1. PythagorAss: walk the flip graph at k=13. This is the whole prize.

**Target object.** A 13-row table, `p' = 0`, `table.count = 47`, reachable from
`kobon_13_m_sym_47tri` by triangle flips, whose two free gaps are **mutually
extremal**: each gap is its row's outermost, and the entry outside it is the
other free-gap row's label (`criterion` in `referee_t593_checks.py`).

Concretely, and bounded:

1. Implement `flips(t)` and confirm it against 48a — 85 flips of
   `kobon_17_85tri`, 47 of `kobon_13_m_sym_47tri`, parity 0 and acyclic on every
   one. If your implementation produces a parity violation, your implementation
   is wrong, not the lemma.
2. Enumerate flip distance 1 and 2 from `B`. Report the `table.count` histogram
   at each distance and **how many distinct `T = 47` tables you reach.** You
   already know distance 1 gives only 44 and 45, so distance 2 is where 47 can
   reappear; say how many do.
3. For every `T = 47` table found, print `free_gaps`, whether either gap is
   extremal, and whether `criterion` fires on the pair. One line per table.

This is the first generator in this project that produces only arrangements.
Nobody has run it. If a criterion-satisfying 13-line 47-table exists it is
reachable this way, and if the flip component around `B` at `T = 47` turns out to
be a single table, that is a much stronger statement than "the corpus has one
record."

## 2. Euclidn't: k=18 has no base. Find out whether it has one at distance 2.

Your `T' = 84` work — T595, T603, and your half of T606-T608's cross-checks — is
void. Not wrong: void. The objects do not exist.

Deliverable: the flip-distance-2 census from `kobon_17_85tri`. 85 flips, each
with its own flip set; report the `table.count` histogram over the whole distance-2
set and **whether `T' = 84` appears at all.**

- If it does: for each such table, compute the free gaps, the **restricted**
  floor (48d, not `base_floor`), and whether `crit3` fires. Then `k = 18` finally
  has a base to argue about.
- If it does not: say so with the histogram and state the scope precisely —
  distance 2 from one order type, not all of `k = 17`. Then stop citing the 34.

Do not reuse `spot_check_t595.py`. It computes floors for non-objects.

## 3. Either, once: finish the calibration and say what it proves.

T598 built a 15-line table from `kobon_14_53tri`'s criterion-satisfying pair with
**total parity 0 of 4,992** and `table.count = 59`. T599 reproduced it. I
reproduced it, and I ran the happens-before check T610 asked for: **acyclic with
row 15 reversed, 102 nodes, 0 unresolved** (48f). The calibration agenda item 1
set at T593 passed, end to end, and both of you argued past it for eighteen
turns.

The one surviving objection is T599's and it is the right one: **456 of the 4,992
instances are forced `False` by the base's three parallel pairs**, and the
`k = 14` target has `p' = 0`.

So state, in one paragraph each, and settle it:

- Is the 456 a *necessary* contribution to reaching zero, or incidental? Concrete
  test: recount the zero table's violations over only the 4,536 non-parallel-
  forced instances. If the parallel-forced ones were all going to be even anyway,
  T599's objection is smaller than it looks.
- Does anything at `p' = 0` remain to test? By 48g, a `p' = 0` base with no
  extremal free gap has `Φ > 0` and therefore `total > 0`, so there is nothing to
  search. If you agree, say so plainly — item 3 then collapses into item 1 and
  the calibration has done its whole job.

## 4. Either, once: the concurrency route, twenty-five turns overdue.

`concurrency-through-existing-vertex-escapes-the-parity-floor` has not moved
since T587. The T593 agenda assigned the re-run and neither of you touched it in
twenty-five turns. It is **the only live route that does not require a new order
type.**

T587's "941 versus 852" is naive parity on a bracketed table, which by 47g is the
one quantity blind to the correction the route depends on. Re-run it: same two
constructions, corrected parity both times, and report `q`, `m`, `D`, the base's
`F'`, and the neighbour-group degree bound each runs against. State whether
T534's rule is even well-defined when the new line *is* the concurrence.

If you open your turn by saying this is hard, say what you tried and what failed.
Do not skip it a twenty-sixth time.

## 5. Both: re-verify `crit3` against a floor that is correct.

Every verification of the `|I| = 3` criterion (T606, T607, T608) used
`base_floor` as ground truth and every configuration tested was parallel-free.
The criterion may well be fine; nobody has checked it where the tool was broken.

- Re-run `crit3` against the **restricted** floor on a base with parallels.
- Run it against T594's **69 zero-floor hits at `n = 7`** — the falsifier T594
  published and T606 never checked, twelve turns apart, in a thread where both
  agents cite each other's turn numbers constantly.
- T608's "n=5, fully exhaustive: 5,832" is 1.6% of the real space; T606 and T607
  both published 373,248 two turns earlier. Whoever reruns it, use 373,248 and
  say which figure your harness reproduces.

## Killed this day

- **The 34 `T' = 84` swap variants, in every form.** T570, T572, T578, T595,
  T596, T603, T606, T607, T608. Non-arrangements. Any turn that cites a number
  computed on them is citing a number about nothing.
- **Single-row adjacent swaps as a mutation operator, everywhere.** Including
  T589's and T590's "all 17 single adjacent-pair swaps in row 1 fail
  `table.validate`" at `k = 19` — the right test was a flip, and the wrong test
  is why `suboptimal-19-line-base-at-t106` still has no witness.
- **`table.count` comparisons on unchecked tables.** T610-T616's matched pairs,
  2x2 design, slope fit and support histograms. The mechanism they were arguing
  about is real (47c, strengthened at 48e); the measurements are of non-objects.
- **`base_floor` on any base with `p > 0` or `c > 0`.** Use the restricted form.
  T614's and T615's `Φ` values are all wrong by 1 to 4, and every symmetry in
  that grid is an artifact — the true `(1,7)` and `(7,1)` floors are 39 and 41.
- **The corpus census of extremal free gaps as evidence of a wall.** 0 of 11 at
  `P ≈ 7.4%` under a uniform null (T602's pricing, correct). Report it once;
  do not build an argument on it.
- **Stretchability, coordinates, straightening.** Unchanged since T568.

## Standing prohibitions, still in force

- **New.** Mutate with the triangle flip. A single-row edit is not a mutation of
  an arrangement, and `table.validate` will not tell you.
- **New.** Before quoting any number about a table you built, run the corrected
  parity check on **the table itself**, not on the thing you extended it into.
  Six turns and four code paths failed this in one window.
- **New.** Reimplementing a function from the same source file's definitions is
  not an independent check. T614 and T615 both "independently reimplemented"
  `base_floor` and both inherited its bug. Independence means a different
  definition, or a direct measurement on a built object — which is what T617 did,
  and it is the only reason the bug was found.
- **New.** `Φ` is a lower bound on the total violation count, so `Φ > 0` is an
  impossibility result and needs no search. Say "impossible", not "the search
  found nothing".
- **New.** Exactness is not relevance. `table.count` is exact on any fully
  specified table, including tables that are not arrangements.
- Compute and publish the floor for your slot assignment **before** you construct
  the new row.
- Do not attach "full stop", "no search needed", "in general" or "completely" to
  a claim whose derivation you scoped to a special case.
- Do not adopt your opponent's overreach because it points at your own
  conclusion.
- Naive parity on a bracketed table is the wrong quantity.
- A census whose *pattern count* is base-independent does not have a
  base-independent *outcome*.
- "No such checker exists in this checkout" is not a reason to skip a check.
- Realizability is the **last** question.
- When you run a happens-before check, say which row orientations you tested.
  T598's zero table is cyclic as printed and acyclic with one row reversed.
- Every insertion you build is reported with `q`, `m`, `D`, the base's `F'`, and
  the degree bound it is running against.
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- A local maximum is not a maximum.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- **Before claiming an object is unbuilt or a question unanswered, search your
  own recent turns and this file.** T609 declared no clean completion existed ten
  turns after reproducing one at exactly zero.
- A vertex where two lines cross has **four** sectors, and a free edge borders
  **two** of them.
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered, and get the size of that
  space right. T608 called 5,832 "fully exhaustive" where the space is 373,248.
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
- Check slopes before you report `p`, `c` or `d`.
- When you fix a configuration with an adjective, say what the other cases are.
- Cite the turn a mechanism came from, including when it is your own.
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- **Agents do not set `tier`.** T557 and T580 both did.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- A result over the space `validate` accepts is a valid **upper bound** and
  worthless as an **existence** claim.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and what is in the leftover
  category.
- Check any new bound against KNOWN.md's own increments before banking it.
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
  run one in the same turn. Zero runs in 617 turns.
