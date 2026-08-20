# kobon-duel Phase 2: Verification and Search

Status: approved 2026-08-20, after turn 64.
Supersedes section 14 ("Phase 2, the substance") of the 2026-08-17 design.

## 1. Purpose

Phase 1 shipped a debate that runs on prose. Sixty-four turns in, the referee's
verdict on it is that the debate cannot check itself: turn 44 published five
lines with six-decimal coefficients, turns 45 through 51 argued about them by
hand, and the referee's turn 52 killed the entire thread by recomputing the same
object in exact form in a single pass. Turns 63 and 64 repeated the pattern at
smaller scale.

Phase 2 gives the debate an oracle and gives the project a search. Three
outcomes are in scope, in descending order of likelihood:

1. Every coordinate claim becomes checkable in one command instead of one turn.
2. The debate's outstanding numeric debts get paid from published data.
3. A new optimal arrangement is found at k = 14, 18 or 20.

Outcome 3 is unlikely and the design says so in every place a reader might
otherwise infer confidence.

## 2. What phase 1 exposed

Three concrete failures, all recorded in `LEDGER.md` and `THREAD.md`:

- **Unverifiable coordinates.** No mechanism existed to check a published
  arrangement, so hand arithmetic was the only recourse and it was wrong twice
  (turn 46's rounding-noise inequalities, turn 63's scale-invariance error).
- **Unpaid numeric debts.** `deletion-route-construction` has been CONTESTED
  since turn 5 because nobody produced the per-line triangle-incidence degree
  sequence of a known k = 15, T = 65 optimum. Sixty turns later it is still
  owed. It is a five-minute computation given the arrangement.
- **No path to GOLD.** Agents cannot be trusted to tier their own turns, as
  turn 39 demonstrated by tagging itself silver. Only a verifier can settle a
  construction claim, and there was no verifier.

## 3. Scope

**In scope:** table representation, a combinatorial triangle counter, the
published-arrangement corpus, a reproduction gate, straightening, flip search on
the constructive side, an exhaustive module on the impossibility side, a run
registry, agent tool access, and the GOLD path.

**Out of scope:** a SAT encoding. Savchuk's Kissat attack on k = 14, 18 and 20
did not terminate with a verdict, and beating it requires materially different
encoding work that is its own project. Nothing here forecloses adding one later,
but no interfaces are being designed speculatively to accommodate it.

**Explicitly rejected:** simulated annealing over line coordinates, which was
the original phase 2 plan. The objective is piecewise constant with large
plateaus and optimal arrangements occupy small cells of the realization space.
Coordinate-space local search is the wrong move set for this problem. Flip
search in combinatorial space replaces it.

## 4. Prior art and imported assets

Two repositories by Pavlo Savchuk, both licensed CC BY 4.0:

- `github.com/zegalur/line-order` (LineOrder), the straightening tool and the
  arrangement galleries.
- `github.com/zegalur/kobon-cnf` (KobonCNF), the SAT solver. Not used here;
  its data directories are gitignored and empty.

`line-order/generate_gallery.py` contains published tables for every known
optimum from k = 3 to k = 33. The entries this project depends on:

| entry | k | triangles | attribution |
|---|---|---|---|
| `kobon_14_53tri` | 14 | 53 | Johannes Bader |
| `kobon_15_5_rot_symmetry` | 15 | 65 | Toshitaka Suzuki |
| `kobon_18_93tri` | 18 | 93 | Johannes Bader |
| `kobon_20_116tri` | 20 | 116 | Kyle Wood, based on the n=19 solution |
| `kobon_13_m_sym_47tri` | 13 | 47 | Kabanovitch |
| the remaining 27 entries | 3 to 33 | various | attribution taken verbatim from each gallery `entry_title` |

**Attribution is a hard requirement, not a courtesy.** CC BY 4.0 obliges it and
the artifact is public. Every imported arrangement carries its original
attribution in `corpus.py`, in `KNOWN.md`, and in the README. No imported
arrangement may ever appear in a Telegram or X post without its author's name.
The project's contribution is the search and the harness, never the corpus.

Also relevant, already in `LITERATURE.md`: Forge and Ramirez Alfonsin (1998),
whose Proposition 3.1 describes arrangements of the form `y = m_i(x - a_i)` with
`a_i` either near-zero or `tan(+/- i*pi/(N-1))`. LineOrder can generate these.
This is a structured sub-family worth searching and is noted as a stage 2
stretch item, not a committed deliverable.

## 5. Representation

### 5.1 Tables

Savchuk's table format, adopted verbatim so the corpus imports without
translation.

Enclose all crossings in a circle. Pick a line as #1, go clockwise, number the
lines as they enter the circle. Each line now has a number and a direction. Row
`i` of the table lists the lines crossing line `i`, in order along line `i`.

Two degeneracies matter and both appear in the corpus:

- **Parallel lines.** A line parallel to line `i` never crosses it and is absent
  from row `i`, so that row is shorter than `k - 1`. Bader's 53-triangle k = 14
  arrangement has rows of length 12 and 13, so it has parallels. Any
  implementation assuming uniform row length is wrong on the seed itself.
- **Multi-line intersection points.** Where three or more lines meet, row `i`
  lists all of them consecutively in the same order, starting from line `i`.

The combinatorial counter must handle both. Correctness is established by the
reproduction gate in section 7, not by argument.

### 5.2 Coordinates

Lines as integer triples `(a, b, c)` meaning `ax + by = c`. Integer rather than
float, because the sign test that decides whether line `m` cuts the triangle of
lines `i, j, k` reduces to the sign of an integer expression once the
intersection denominators are cleared:

```
sign(side) = sign(a*(c1*b2 - c2*b1) + b*(a1*c2 - a2*c1) - c*det) * sign(det)
```

Exact and fast, with no tolerance parameter anywhere. This matters because
`verify.py` already warns in its own docstring that floats manufacture phantom
triangles at near-degenerate vertices, and that is the standard way
computational claims in this area fall apart. Restricting to integers costs no
generality: the realization space of a simple arrangement is open, so every
realizable simple combinatorial type has an integer representative.

## 6. Components

### 6.1 `kobon/table.py`

Parse, validate and canonicalize tables. Count triangular faces combinatorially
from the table alone, handling parallels and multi-line points. Expose the
per-line triangle-incidence degree sequence, which is what pays the turn-5 debt.

### 6.2 `kobon/corpus.py`

The imported arrangements with their attributions and published counts. Read
only. Serves both as search seeds and as the reproduction gate's fixture set.

### 6.3 `kobon/verify.py` (exists, unchanged)

The exact `Fraction` face counter over coordinates. Stays as the independent
second opinion. Two independently written counters that must agree is the
property that makes a record claim credible.

### 6.4 `kobon/exact.py`

The integer sign-test counter from section 5.2. Fast path for search over
coordinates. A test asserts it agrees with `verify.py` on randomly generated
arrangements, so the fast path cannot silently drift from the oracle.

### 6.5 `kobon/straighten.py`

Vendored from LineOrder with attribution rather than reimplemented. Solves for
`(a_i, C_i)` in `x*cos(a_i) + y*sin(a_i) + C_i = 0` subject to the table's
ordering inequalities, which take the form `S(i,j,k) * F(i,j,k) < 0` with
`F(i,j,k) = C_i*sin(a_k - a_j) + C_j*sin(a_i - a_k) + C_k*sin(a_j - a_i)`.
Multi-line points turn the corresponding inequalities into equalities.

Straightening is heuristic and may fail. A failure is reported, never hidden: a
table with 54 triangles that does not straighten is a pseudoline result, which
is a weaker but still real and still reportable outcome.

### 6.6 `kobon/flip.py`

The constructive side. Local search over tables, seeded from Bader's 53.

Moves are mutations of the table that land on another valid arrangement.
Because every move stays in the space of arrangements and changes the triangle
count by a small amount, the search landscape is navigable in a way the
coordinate landscape is not. Search strategy is tabu or annealed hill climbing
over the mutation graph; the specific schedule is an implementation choice to be
tuned against the small-k ladder, not fixed here.

Degeneracy moves (making lines concurrent, making lines parallel) are included
rather than excluded. The naive expectation is that simple arrangements dominate
because a simple k-line arrangement attains the maximum 78 bounded faces at
k = 14 while every degeneracy costs at least one face, and 54 triangles out of
78 faces leaves only 24 non-triangles. That expectation is wrong, or at least
incomplete: Bader's 53 is not simple. Degeneracy can pay for itself by removing
a crossing that would otherwise cut triangles elsewhere. The search explores
both and the data decides.

Targets k = 14 first, then 18 and 20, which come free from the same machinery
and the same corpus.

### 6.7 `kobon/exhaust.py`

The impossibility side. Complete search with pruning, aiming to prove that 54 is
unreachable at k = 14, which would settle N(14) = 53 as decisively as finding 54
would settle it the other way.

The pruning is driven by the face budget: at most 78 bounded faces at k = 14, so
at most 24 non-triangles, which is a tight constraint that propagates well.

This module is gated on reproducing a known result: it must independently derive
that 33 is unreachable at k = 11, which is Savchuk's published result. A module
that cannot reproduce a known impossibility proof is not an impossibility proof.

Expected to not terminate at k = 14. Built last for that reason.

### 6.8 `kobon/registry.py`

Every verifier invocation appends to `runs/index.jsonl`: run id, k, count,
lines or table, caller, timestamp, and whether it set a record.

Run id is `v-<k>-<first 8 hex of sha256 of the canonical arrangement>`.
Deterministic, so the same arrangement always yields the same id, an agent
cannot fabricate an id that resolves, and re-running a known arrangement
deduplicates rather than accumulating.

### 6.8b `records/`

One JSON file per k holding the best arrangement currently held, in both
representations where available, with its triangle count and provenance: either
a corpus attribution or a registry run id. Seeded from the corpus at stage 1 so
gate layer 2 has something to check before any search has run, then advanced by
the search.

### 6.9 `bin/kobon-verify`

The CLI agents invoke. Reads a JSON arrangement on stdin, in either
representation, prints the triangle count and the run id. This is the entire
surface area agents gain.

### 6.10 `bin/search.sh` and `kobon-search.timer`

Daily bounded search run. See section 10.

### 6.11 `SEARCH.md`

One page of current search state, injected into every turn prompt by
`take_turn.py` alongside `LEDGER.md` and `AGENDA.md`. Without this the search
runs and the debate never learns anything from it.

## 7. The reproduction gate

Three layers, proving three different things.

**Layer 1, the counter (fast, in pytest).** The combinatorial table counter must
reproduce the published triangle count for all 32 corpus entries, k = 3 to
k = 33. Disagreement anywhere means a bug in the counter, not a discovery. This
is a far stronger gate than a hand-built fixture set and it is the main reason
importing the corpus is worth the attribution obligation.

**Layer 2, the coordinate path (fast, in pytest).** Every arrangement in
`records/` is recounted by the exact `Fraction` verifier and must match its
stored count and meet or beat the `KNOWN.md` best-known for that k. Catches
stale or corrupted records.

**Layer 3, the search (slow, `bin/selftest_ladder.py`, not in pytest).** Flip
search must independently rediscover N(k) climbing from k = 6, and
`exhaust.py` must independently re-derive the k = 11 impossibility. This is the
honest gate. If flip search cannot find 25 triangles at k = 10 it has no
business being pointed at 54 at k = 14, and we learn that in week one rather
than month three.

## 8. Agent tool access and driver gates

`bin/turn.sh` gains exactly one capability:

```
--allowedTools "Bash(python3 bin/kobon-verify:*)"
```

alongside the existing `--disallowed-tools "Write,Edit,NotebookEdit"`. Agents
can ask how many triangles an arrangement has. They cannot write files, cannot
touch the ledger, and cannot reach the registry except through the CLI.

`bin/commit_turn.py` gains two violations:

- `FABRICATED_RUN`: the turn cites a `verifier_runs` id that is not in the
  registry. Since ids are content hashes, this is decidable.
- `UNVERIFIED_COORDINATES`: the turn's prose contains explicit coordinates but
  `verifier_runs` is empty. This is the turn 63 and 64 failure mode named
  directly.

Both agent briefs gain a paragraph stating that published coordinates must cite
a run id, and that hand-computed triangle counts are no longer admissible when
the command exists.

The referee brief gains a paragraph noting that verifier runs outrank prose, and
that a claim contradicted by a registry run is DEAD without further argument.

## 9. The GOLD path

Gold remains unsettable by agents, consistent with the existing rule that turn
39 violated.

`registry.py` compares every run against `KNOWN.md`. A count exceeding the
best-known for that k is a record. The driver then, in order: writes the
arrangement to `records/`, stamps the turn gold, fires a Telegram notification
with the arrangement attached, and stops the search timer pending human review.

Because the run id is a content hash of the arrangement, a gold notification is
independently reproducible by any reader from the notification alone. That is
the standard a record claim has to meet.

A gold event does not update `KNOWN.md`. That file changes only when the owner
accepts the result, which stays a human decision.

## 10. Compute budget

Its own systemd timer, once daily, entirely separate from the hourly turn timer.

- `nice -n 19`, `CPUQuota=150%`, hard 30 minute `TimeoutStartSec`.
- Checkpoints best-found arrangements per k to `records/` so progress
  accumulates across days rather than restarting cold.
- Ladder mode first: advance k only on matching the known optimum. Remaining
  budget goes to k = 14, then 18, then 20.

The machine already runs the hourly debate turn plus six other timers and is the
owner's daily driver. The search must be invisible.

## 11. Testing

Following the repo's existing 119-test convention, TDD throughout.

- Table parse and canonicalization, including short rows (parallels) and
  multi-line points.
- Combinatorial counter against all 32 corpus entries.
- Integer counter agrees with the `Fraction` verifier on random arrangements.
- Registry ids deterministic, stable under canonicalization, and unique.
- The gate catches a deliberately corrupted record.
- `FABRICATED_RUN` and `UNVERIFIED_COORDINATES` stamp correctly against fixture
  turns, and do not false-positive on prose that merely mentions numbers.
- Flip search finds N(5) = 5 and N(6) = 7 within a second.
- Straightening round-trips a known table to coordinates whose exact count
  matches the table count.

## 12. Staging

**Stage 1, one day.** Table representation, combinatorial counter, corpus
import, `records/` seeded from the corpus, reproduction gate layers 1 and 2. Deliverable beyond the code: the
per-line triangle-incidence degree sequence of Suzuki's k = 15, T = 65
arrangement, written into the ledger, paying a debt outstanding since turn 5.

**Stage 2.** Integer counter, straightening, registry, CLI, agent tool access,
driver gates, GOLD path, flip search, search timer, `SEARCH.md`. This is the
bulk of the work and the point at which the debate changes character.

**Stage 3.** `exhaust.py`, gated on reproducing k = 11. Built last because it is
the most likely to not terminate.

## 13. Risks

- **The search finds nothing.** Most likely outcome by a wide margin. Savchuk
  pointed better-developed tooling at these three cases in 2025 and got no
  verdict. Mitigated only in the sense that stages 1 and 2 have standalone value
  regardless: the reproduction gate, the oracle, and the paid debts do not
  depend on finding anything.
- **Corpus attribution handled carelessly.** The corpus is other people's work
  under a license with an attribution obligation, and this project is public and
  posts to X daily. Mitigated by section 4 being a hard requirement and by the
  posting rule that no imported arrangement is ever shown without its author.
- **Breaking the live loop.** `turn.sh` runs hourly and the change touches it.
  Mitigated by testing the modified invocation against a fixture prompt before
  installing, and by keeping the change to a single added flag.
- **Table semantics misread.** The degeneracy conventions are documented in
  prose, not formally specified. Mitigated by gate layer 1: a misreading fails
  loudly against 32 published counts rather than silently producing wrong
  research.
- **Agents ignore the tool.** Possible; they ignored agenda item 2 for
  twenty-four consecutive turns. Mitigated by `UNVERIFIED_COORDINATES` making
  the omission a recorded, public violation rather than a silent choice.

## 14. Success criteria

Phase 2 is done when:

- The combinatorial counter reproduces all 32 published counts.
- `python3 -m pytest` is green.
- A turn citing a fabricated run id gets a violation stamped in public.
- A turn publishing coordinates without a run id gets a violation stamped.
- The daily search timer has run for a week without the owner noticing it.
- `SEARCH.md` is non-empty and at least one turn has cited a real run id.
- The k = 15 degree sequence is in the ledger and
  `deletion-route-construction` is resolved one way or the other.

Finding 54 is not a success criterion. It is a low-probability upside on a
project whose floor is the harness.
