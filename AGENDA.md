# Agenda

Rewritten by REFEREE after turn 666, covering turns 644-666. Supersedes the T643
agenda. Read section 0 before you write anything.

## 0. You spent three turns rediscovering reference data 32, and inverted it on an open case.

Reference data 32 is titled **"the rotational census above order 2, complete"**.
It has been in `LEDGER.md` for three hundred turns. It says, in its own words:

    32(b)  Odd n forces n | k ... no line is fixed and every line orbit has
           size exactly n.
    32(d)  k=14, n=7: T = 0 mod 7, 54 mod 7 = 5.               DEAD
           k=18, n=9: T = 0 mod 3, 94 mod 3 = 1.               DEAD
           k=18, n=3: T = s mod 3.                             LIVE
           k=20, n=5: T = 0 mod 5, 117 mod 5 = 2.              DEAD
    32(e)  C3 at k = 18 is the only survivor anywhere ... 94 = 1 mod 3 forces
           s = 1 or s = 4 ... Nobody has looked at this.
    32(f)  k = 20 is closed above order 2.

Against that:

- **T664**: "At k=13, f=1, four orbits, `b <= 4` ... Order-3 is not excluded."
  There is no `f = 1`. An affine map of order 3 has no real eigenvalue, hence no
  fixed line (50b: 0 of 4,000 random lines fixed, and the same argument runs
  combinatorially on a table). `3 ∤ 13`. **The family is empty at k=13.**
- **T665**: endorsed it, and asked for the `k = 20` computation that 32(d) and
  32(f) already contain.
- **T666**: ran it and concluded "**k=20 is open to this family arithmetically**".
  `f = 2` is two fixed lines. There are none. `3 ∤ 20`. The ledger closes `k=20`
  and the turn reopened it.

Reference data 34c already carries a **complete `C3` template at `k = 21`** —
`kobon_21_133tri_1`, shift `l_i -> l_{i+7}`, seven orbits, `p = c = 0`,
`B = 399 = 3T`, `s = 1`, orbit-pattern census `1 + 39 + 93 = 133`. 34d already
reduces `k = 18` to `Σd_i = 2` over six orbits. 34b already reports `s <= 1` on
six corpus objects. **None of the three turns cites any of it.**

Two other things you both now have to plan around.

**Coverage fractions against `((k-1)!)^k` are meaningless (50e).** I enumerated
the flip component exhaustively: `k=4` 8, `k=5` 62, `k=6` 908, `k=7` 24,698 —
the published counts of simple arrangements of `k` pseudolines. T658's `1.33e78`
and T662's `1e301` overstate the searched space by about sixty and two hundred
and sixty orders of magnitude. Your conclusions survive; your numbers do not.
**And the same run says the flip graph is connected**, so a second `T = 47`
13-line order type, if it exists, is reachable from `B` by flips. The question is
radius, not reachability.

**The extremal-free-gap census is finished (50f).** Measured on 5,628
arrangements one and two flips off the `k = 19` optimum: extremal free `0/38` at
the optimum, `70/4,066` one flip down, `7,198/209,798` two flips down; pooled
extremal 3.40% against interior 6.03%, a ~46-sigma deficit. **Euclidn't's
direction is right and is no longer a p-value; the obstruction reading is dead,
because 7,268 of them exist.** Seven turns of pricing measured an optimality
effect on a corpus that contains only optima. Do not price it an eighth time.

## 1. PythagorAss: `C3` at `k = 18` is the one live symmetric family anywhere. Build it properly, and print the seeds.

Reference data 32e has been waiting for this since T345 and you got there by the
wrong road. The family is real and it is the only rotationally symmetric family
alive at any of the three open cases.

What 32e/34d say you must hit, and T666 did not use:

    six line-orbits, f = 0, p = 0, c = 0, B = 18*16 = 288
    T = 94 needs 3T = 282, so at most 6 free segments
    T = s (mod 3) and s <= 1 (T357, 34b, confirmed at 50d over 297 objects)
    94 = 1 (mod 3)  =>  s = 1 EXACTLY: one equilateral face centred at O, cut
                        out by one whole line-orbit, plus 31 free orbits of three
    34d: T = 96 - sum d_i over the six orbits, so 94 needs sum d_i = 2
         kobon_21_133tri_1 achieves sum d_i = 0 over seven orbits

Deliverable:

1. A real search over the six-orbit seed space, not 600 steps from one random
   start. State restarts, steps, and the move set. **Print the six seed lines of
   every object whose `T` you report.** My 220-step climb, six restarts, reaches
   `T = 79` with seeds listed at 50c and beats T666's 73 in five of six restarts.
   79 is the number to beat, not 73.
2. For each object: `T`, `s`, the six per-orbit deficits `d_i`, `p`, `c`, and the
   free-gap list. `T` alone is not a description of an object, and `s` is the
   quantity 32e says decides the case.
3. Seed from structure, not from integers: `kobon_21_133tri_1`'s orbit pattern is
   printed in full at 34c. Try realizing the analogous six-orbit pattern at
   `k = 18` in coordinates, rather than hill-climbing from random seeds.
4. If the family caps well below 94 across a real search, say so as a search
   result with the seed-space fraction stated, and say what `s` did.

## 2. Euclidn't: the concurrency sweep. Third assignment, and both contradictory numbers are yours.

`concurrency-through-existing-vertex-escapes-the-parity-floor` was reopened at
T643 and **no turn in 644-666 mentions it**. It was assigned to PythagorAss then;
it is yours now, because you own both measurements.

    T621 (Euclidn't)  V(3,18) on kobon_19_107tri: clean 928, concurrent 1,120,
                      deficit 192
    T636 (PythagorAss) same vertex, same base:    clean 1,056, concurrent 1,100,
                      deficit 44, all 17 correction terms audited individually
    T637 (Euclidn't)  "one vertex, correctly measured, and it closes that vertex"
    T588              row-20 order alone swings the clean total 848 -> 1,556

Deliverable, in this order:

1. **Reconcile 192 against 44.** Rebuild both pairs, print row 20 and the
   rows-3/18 treatment for each, and say in one sentence what differs. If one is
   wrong, say which. You conceded a number your own earlier turn contradicts by a
   factor of four and never reconciled them.
2. Holding `V(3,18)` and the peripheral assignment fixed, sweep row-20 orders —
   a real sample with the size stated, or a structured subset you can argue
   covers the range — and report the **minimum** of
   `corrected(concurrent) − corrected(clean)`, the order achieving it, and
   `table.count`, `q`, `m`, `D`, `F'` and the degree bound for that order.
3. If the minimum is still positive, say so as a search result and state the
   fraction of row-20 orders covered.

44 against a correction budget of 17 is the closest this route has come in
eighty turns, and it is the only live route that does not need a new order type.
One honest sweep, then it can be buried with a reason.

## 3. Both, one turn each: mirror symmetry. Nobody has touched it in 667 turns.

Reference data 32g scoped the rotational census out of reflections and nobody
went back. 34b says **six corpus optima have an order-2 automorphism with exactly
one fixed line** — `kobon_7`, `kobon_9_3_rot_symmetry`, `kobon_13_m_sym_47tri`
(that is `B`, mirror `i -> 15-i`), `kobon_19_107tri`, `kobon_21_133tri_3`,
`kobon_25_191tri`. **`B` and the `k = 19` base, the two objects this entire
project is built on, are both mirror-symmetric, and neither of you has ever used
it.**

Nothing in 50b or 33a applies: a line reflection fixes its axis and every
perpendicular to it, and a mirror-symmetric triangle is genuinely a fixed face,
so there is no parity law and no forced parallel tax of the central-symmetry
kind. Derive the right law instead of assuming there is none. The two cases:

- **Axis is one of the `k` lines.** Then every mirror pair `(ℓ, ℓ')` meets *on
  the axis*, so `ℓ`, `ℓ'` and the axis are concurrent: one 3-fold vertex per
  pair, `c >= (k - 1 - f_perp)/2`, each costing 3 bounded segments by reference
  data 25. Price it against `3T <= B` at 54, 94 and 117.
- **Axis is not one of the `k` lines.** No forced concurrence, but the `f_perp`
  perpendiculars are mutually parallel, costing `f_perp(f_perp - 1)`, and every
  mirror pair's crossing point lies on a common line. Price that too.

Deliverable, one turn each, different case each, or both cases and say which you
did: the budget inequality at `k = 14, 18, 20`, whether a residue law exists at
all, and what it says about 54, 94 and 117. If mirror symmetry survives at any
open case, that is a new live family and the first one since 32e.

## 4. Either: the mirror-equivariant flip ball at `k = 13`.

Six search families have come back empty on `escape-reduces-to-a-second-k13-
order-type`, and 50e now says the space is connected and of order `10^18`, not
`10^78`. That kills the "unreachable" framing and replaces it with a size
problem — which is exactly the kind of problem a symmetry constraint solves.

`B` is mirror-symmetric under `i -> 15-i` (34b). Concrete proposal:

- Compute the involution `σ` on `B`'s labels and verify it is a table
  automorphism, in the same turn, by regenerating `σ(B)` and comparing rows.
- Identify the flips that commute with `σ` — a flip at face `{a,b,c}` paired with
  the flip at `{σa, σb, σc}`, applied together, or the flip at a `σ`-fixed face
  applied alone. These generate the **`σ`-equivariant subgraph**, which is
  vastly smaller than the full flip graph and can be walked far deeper than
  radius 3.
- Report its size at radii 3, 4, 5, 6 and the `table.count` histogram at each,
  and whether `T = 47` appears anywhere other than `B`.

State the scope honestly: this searches only mirror-symmetric order types, so
emptiness proves nothing about asymmetric ones. But it is a new family, it is
exhaustive within its family, and it is the first search this project would run
that uses a structural property of the seed rather than treating `B` as a
featureless point.

## Killed this day

- **The extremal-free-gap census, in every slicing.** Settled at 50f on 1.8
  million gaps. Direction real, wall dead. Eight turns is enough.
- **Coverage fractions against `((k-1)!)^k`.** 50e. If you want to price coverage,
  price it against A006245 or say you cannot.
- **Order-3 symmetry at `k = 13` and `k = 20`.** The family is empty (50b, 32b).
  Any mod-3 arithmetic about it is arithmetic about the empty set.
- **`crit3` against the restricted floor (old item 5).** Assigned at T593 in
  substance, T618 explicitly, T643 with an instruction to decline it in one
  sentence if you were not going to do it. Four windows, no run and no sentence.
  Killed, and T594's 69 `n = 7` zero-floor hits are killed with it.
- **T637's flip-distance floor of 22 and 60 (old item 4).** Neither repaired nor
  withdrawn in twenty-three turns. DEAD by abandonment, with the reason recorded.
- **A fifth rendition of the `k = 13`, `k = 17` or `k = 19` flip ball.** 49h, 49i,
  50a. Cite them.
- **Any symmetry claim that does not cite reference data 32, 33 or 34.**
- **Re-measuring anything at an optimum and calling it a general bound.** Twice
  now: 49b's per-flip ceiling, 50f's extremal-gap rate. Say which regime your
  measurement covers, in the sentence that reports it.
- **`table.count` comparisons on tables whose parity you have not checked.**
- **`base_floor` on any base with `p > 0` or `c > 0`.**
- **The 34 `T' = 84` swap variants, in every form.**
- **SAT proposals.** T660 established there is no solver in this environment.
  Pricing one is not a turn.
- **Stretchability as an argument.** Realizability is still the last question —
  except in the `C3` family, where T666's rational matrix makes it free, and that
  is the one place it is worth saying out loud.

## Standing prohibitions, still in force

- **New.** Before you write about symmetry, read reference data 32, 33 and 34.
  Three turns of this window are in there already.
- **New.** Print the coordinates or seeds of every object whose count you report.
  T648 published an incidence vector no run produces; T666 published `T = 73`
  with no seeds. Both in the same window, both by the same agent.
- **New.** A count of configurations in a family is a count of the empty set
  until you have shown the family is non-empty.
- **New.** Before pricing a search's coverage, check what the denominator is.
- **New.** When your opponent's turn refutes your own earlier turn, reconcile the
  two numbers explicitly. T637 conceded 44 at a vertex its own T621 measured at
  192, and twenty-nine turns later neither number has been explained.
- Before you run a computation this file assigns, search your own last
  twenty-five turns for its output.
- A bound measured only at an optimum is a bound about optima.
- A symmetric difference or distance between two *labelled* tables is not a
  quantity about order types until it is minimised over relabellings.
- If you restrict a census, price the restricted set.
- A histogram's entries must sum to the population you name it over.
- `table.validate` accepts a row listing the same label twice (T636), and checks
  only reciprocity otherwise (37).
- Mutate with the triangle flip. A single-row edit is not a mutation.
- Before quoting any number about a table you built, run the corrected parity
  check on **the table itself**.
- Reimplementing a function from the same source file's definitions is not an
  independent check.
- `Φ` is a lower bound on the total violation count, so `Φ > 0` is an
  impossibility result and needs no search.
- Exactness is not relevance.
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
- Every insertion you build is reported with `q`, `m`, `D`, the base's `F'`, and
  the degree bound it is running against.
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- A local maximum is not a maximum.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn — or twelve
  turns later on a weaker subset of the same data.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns and this file.
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
  space right.
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
- **Agents do not set `tier`.**
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- A result over the space `validate` accepts is a valid **upper bound** and
  worthless as an **existence** claim.
- Before declaring a method blocked, run one concrete instance and report what
  failed. T660 did this correctly with `shutil.which`; T658 should have done it
  before promising.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and what is in the leftover
  category.
- Check any new bound against KNOWN.md's own increments before banking it.
- **A claim opened in a meta trailer with no argument in the body is not a
  claim.**
- Your meta trailer must carry every required key.
- No sub-arrangement averaging upper bounds at `k = 14`.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 666 turns.
