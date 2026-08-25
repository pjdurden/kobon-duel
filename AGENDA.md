# Agenda

Rewritten daily by the referee. **This edition is an owner override entered after
turn 170, and it supersedes the turn-155 agenda in full.** The referee should
carry both standing rules below into the next rewrite rather than replacing them.

Two things changed. A result the thread has been building on since turn 163 is
wrong, and both agents have had the ability to run the verifier all along and
never used it.

## 0. Read this before you write anything

`insertion-y-capped-at-6-independent-of-concurrence-count` and
`generic-insertion-into-any-simple-13-line-caps-53` are **refuted**. The full
argument is at the top of `LEDGER.md`. The short version: the T/N labelling of
chords is not exhaustive, because a chord can lie in an unbounded face, and
clipping the corner of an unbounded wedge creates a bounded triangle worth +1
that the labelling never counts. Classical values falsify the mechanism on their
own, N(5) - N(4) = 3 from three chords against a cap of two.

Turn 170's segment budget rests on the census, not on the cap, so it is not
directly hit. But do not cite the cap, do not cite T' <= 53 for insertion, and do
not treat agenda items 1 to 3 of the turn-155 agenda as retired. They were retired
by a wrong result.

## 1. Both sides: settle the clippable-unbounded-face count at k=13

This is now the only thing on the board, and it is finite.

Reference data 8 is correct: each free segment of B has an unbounded three-sided
wedge on one side and a hexagon on the other. A chord entering that wedge through
its bounded edge and leaving through one of its two rays cuts off a bounded
triangle. So at a free segment two consecutive chords can both gain, one clipping
the hexagon, one clipping the wedge.

- **PythagorAss:** show it. Exhibit the two crossings explicitly, on the free
  segment `(9,5,4)`, and say which lines l meets and where. If a straight line
  cannot realize both gains, say which constraint stops it.
- **Euclidn't:** bound it. How many of l's twelve chords can lie in clippable
  unbounded faces at all, given that B has 26 unbounded faces and l's two extreme
  pieces are rays? If the answer is small, the cap can be repaired rather than
  abandoned, and the repaired number is what matters.

**The named object:** a corrected bound on Y with the unbounded faces counted, or
an explicit pair of consecutive gaining chords. Not another face.

**Free falsifier:** the two free segments are `(6,10,11)` and `(9,5,4)` and they
are a sigma-pair. That is one verifier call, printed below. If your argument needs
a third free segment, it is wrong before you finish it.

## 2. The step neither of you took, and it is still available

Every 14-line arrangement is a single-line insertion into a 13-line one, because
you can delete any line. N(13) = 47 is closed. So T(A) = T(A') + Y <= 47 + Y, and
54 requires **Y >= 7**. Any correct upper bound on Y strictly below 7 closes k=14
outright.

Turn 168 called his own result "one construction method" and Euclidn't, who
benefits from it, let that pass. Both of you undersold it. The bound was wrong, so
nothing is lost, but the reduction is sound and it is the highest-value target in
the project: **the whole of k=14 now reduces to bounding Y.**

Note the standing prohibition on delete-a-line upper bounds was aimed at
sub-arrangement averaging, which died at turn 21 for unrelated reasons. It does
not cover this. Averaging bounds a maximum over subsets; this is a structural
per-insertion count. **The prohibition is hereby narrowed to averaging arguments
only.**

## Standing rule, new and mechanically enforced: run the verifier

You have Bash. Only `Write`, `Edit` and `NotebookEdit` are blocked. The repository
has enumerated every triangle of every corpus arrangement since phase 2 stage 1
shipped, and across 170 turns `verifier_runs` has been empty 170 times out of 170.
That is how a wrong case split survived six turns of scrutiny.

```
cd ~/kobon-duel && python3 -c "
from kobon import corpus, table
t = corpus.by_key()['kobon_13_m_sym_47tri']['table']
tris = set(map(frozenset, table.triangles(t)))
print(len(tris))                      # 47
print(frozenset({3,7,12}) in tris)    # is a triple a triangle?
print(t[3])                           # row 4, 1-based label -> index 3
"
```

Any turn asserting a vertex `V(a,b)`, a row position, or a triangle triple of a
corpus arrangement with an empty `verifier_runs` now gets a **NO_VERIFIER_RUN**
violation stamped on it in public. The gate is in `bin/thread.py` and it is live.
Record what you ran as a short string, for example
`"table.triangles(kobon_13_m_sym_47tri) -> 47, {3,7,12} present"`.

Hand-walking something you could enumerate is not rigour, it is exposure.

## Standing rule, new: check the partition, not just the algebra

Turns 163 to 168 were six turns of correct algebra on an incomplete case split,
and the adversarial process did not catch it because both agents checked the sums.
When you concede a counting bound, state the partition it rests on and say what is
in the leftover category. If the answer is "nothing," prove it.

## Killed this day

- **The insertion cap in every form.** T163, T164, T167 and T168's generalization.
  Not reopenable without counting chords in unbounded faces.
- **"This closes one construction method, not k=14."** T168's own disclaimer. The
  reduction is total, see item 2.
- **Agenda item 4 and the Suzuki deletion sweep.** Unchanged, still dead.
- **Near-miss and margin arguments.** Unchanged, still banned.

## Standing prohibitions, still in force

- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- No sub-arrangement **averaging** upper bounds at k=14. Structural per-insertion
  bounds are now explicitly permitted, see item 2.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  or a verifier run you cite.
- When you concede, re-derive the step rather than restating it.
- Any proposed edit or perturbation comes with its triangle cost in the same turn.
