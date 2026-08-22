# Agenda

Rewritten daily by the referee. Written after turn 101.

The standing observation of the last three cycles is retired. Turn 82 opened
`corpus/arrangements.json` and the debate stopped being about a 5-line toy. You
are now working on a real 14-line arrangement that scores 53, its face budget is
known exactly (88 vertices, 190 edges, 103 faces, 75 bounded, 22 non-triangular),
and thirteen of its fifty-three triangles have names. That is more progress in
twenty turns than the previous eighty produced.

The new standing observation replaces it. Turns 92 through 101 kept deferring to
"the global sweep reconstruction," a computation neither of you attempted and
both of you described as expensive and possibly infeasible. Reference data 3 in
the ledger traces a face of Bader's arrangement to completion using three local
arguments and nothing else. It is a pentagon. The reconstruction you were afraid
of is a boundary walk: at each vertex, the next edge is forced by which side of
the current line the face is on, and that side is transferable along any line
that crosses your reference line exactly once. Stop saying it needs coordinates.

Everything below is computable from the fourteen rows printed in the ledger.
None of it needs coordinates, a SAT solver, or a new construction.

## 1. Both sides: the triangle census. Split it and finish it in one day.

`bader-triangle-adjacency-test-is-iff` makes this mechanical and complete: the
triple {a,b,c} is a triangular face **if and only if** b,c are adjacent in row a,
a,c are adjacent in row b, and a,b are adjacent in row c. There are 162 adjacent
pairs across the fourteen rows (six rows of 12 entries contribute 11 each, eight
rows of 13 contribute 12 each). Every one is a bounded segment. Test each.

**The named object:** the complete list of triples passing the test.
PythagorAss takes rows 1 through 7, Euclidn't takes rows 8 through 14; each
reports every triangle whose smallest label lies in their range, so the union is
the census and the overlap is a cross-check. Every genuine triangle must be
found from all three of its rows, so a triple reported by one of you and not
confirmable from the other's rows is an error, not a discovery.

**The count must come out 53.** If it comes out anything else, the corpus table
is not what turn 84 decoded it to be, and that is a bigger finding than 54.

## 2. Both sides: name the three free segments.

This is the sharpest object on the board and it falls out of item 1 for free.
`parallel-pair-budget-for-54`: Bader's arrangement has exactly 162 bounded
segments; 53 triangles consume exactly 159 of them, and no bounded segment can
serve two triangles. So **exactly three bounded segments of this arrangement are
not a side of any triangle.** Those three edges are the entire gap between 53
and 54, localized.

**The named object:** the three segments, each given as (line, its two endpoint
crossings), plus, for each, the identity of the face on either side of it, traced
by the reference-data-3 method. If any two of the three lie on a common face,
say so; if all three lie on distinct faces, say that. Then, and only then, the
question "what perturbation packs them" has a target instead of a vibe.

Do not guess which three before running item 1.

## 3. Both sides: the non-triangular face census, twenty-two faces.

Reference data 3 gives one of them: the pentagon on lines 11, 13, 2, 8, 12. That
leaves 21. The method is the boundary walk, and it terminates.

**The named object:** each of the 22 faces as an ordered vertex list with its
side count, and the arithmetic check `159 + X + 56 + U = 380`, where X is the
total side count of the 22, U is the number of (bounded edge, unbounded face)
incidences, 56 is the ray count doubled, and 380 is 2E. If your census does not
satisfy that identity, it is wrong and you will know it before publishing.

This is the item that turns 88, 89, 90 and 91 all promised and none delivered.

## 4. Both sides: calibrate the segment budget against a closed case.

`parallel-pair-budget-for-54` is a referee claim one day old and neither of you
has attacked it. It makes hard predictions about arrangements already in the
corpus, and checking them costs one lookup each.

- **k = 15, N = 65 (CLOSED).** `B = 15*13 - 2p = 195 - 2p` and `65*3 = 195`, so
  the 65-triangle table must have **p = 0**: no short rows, no bracket nesting,
  and every one of its 195 bounded segments a triangle side. Read the row
  lengths of `kobon_15_5_rot_symmetry` (and any other k=15 entry). All fifteen
  rows must have fourteen entries.
- **k = 13, N = 47 (CLOSED).** `143 - 2p >= 141` forces **p <= 1**.
- **k = 11, N = 32, with 33 proved unreachable by Savchuk.** `99 - 2p >= 96`
  forces `p <= 1`; check what the corpus's k=11 table actually has.

If any of those tables violates its prediction, the budget is broken and the
k=14 conclusion goes with it. If they all hold, `parallel-pair-budget-for-54`
is the first structural constraint in this ledger that survived contact with
data neither agent chose.

## 5. Euclidn't specifically: two corrections to bank, not re-argue.

`deparallelize-yields-nontriangle-all-three-pairs` is now proved, but not by
turn 87's argument. Your `kobon_4` calibration compared row-1-first against
row-2-first on two-entry rows and inferred a global row-orientation convention
from a single degenerate example. Nothing in the corpus establishes that two
different rows are traversed in the same spatial direction, and your own turn 86
control was a better piece of work than the turn 87 conclusion that overrode it.
The real criterion is in the ledger: a common extremal partner t, with V(t,a) and
V(t,b) adjacent in row t. Read it, check it, and if you can break it, do.

Second: turn 91's bounded/unbounded split for `bader-witness-75-bounded-22`
reached the right number through an argument about ray-to-region correspondence
that is not needed and whose k=3 counterexample fails for a different reason
than you gave. The number is safe. The reasoning under it was not.

## Killed this day

- **"It needs the global reconstruction."** Turns 92, 95, 99, 100 and 101 all
  end on some version of this. It is refuted by reference data 3. Do not open
  another claim whose content is that a computation is too hard until you have
  attempted the computation in the turn that says so.
- **Turn 101's exhaustion argument.** "Four independent mechanisms, four dead
  ends... is itself evidence that no bounded-lookahead technique settles this
  witness's face structure." Four failures is not a proof. The fifth attempt
  worked. `local-lookup-program-exhausted` is DEAD.
- **The pentagram program, formally.** Turn 81 capped it at 14 triangles on 14
  lines against a target of 54, correctly, and turn 82 walked away. Nothing in
  turns 20 through 81 is a live line of work. Do not restart it.
- **The whole turn 70-76 parameter-counting thread**, eight claims, closed in
  the ledger as moot. Cluster B never got coordinates and never will.

## Standing prohibitions, still in force

- No sub-arrangement averaging or delete-a-line upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data. Note that
  `parallel-pair-budget-for-54` consumes p, which is order-type data.
- **New:** no claim whose only content is that the opponent's method fails.
  Turns 99, 100 and 101 are three consecutive turns of exactly that, and the
  thing they proved impossible took the referee three paragraphs.
- **New:** every count you assert must be reproducible from a row printed in the
  ledger or the corpus, cited by line number. Turns 96, 97 and 100 did this and
  all three verified perfectly. That is the standard now.
- Check every new number against the ledger before publishing it.
