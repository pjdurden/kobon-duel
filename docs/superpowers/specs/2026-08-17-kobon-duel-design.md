# kobon-duel: adversarial two-agent debate on the Kobon triangle problem

Date: 2026-08-17
Status: approved design, pre-implementation

## 1. Purpose

Two Claude sessions with opposed, seeded biases argue about the Kobon triangle
problem through an append-only markdown file in a public repo. The argument is
rendered as a readable GitHub Pages transcript. When the pair reaches a
mechanically verified result, or genuinely converges after real disagreement,
the owner is notified on Telegram.

Two things are being built at once, and they have different success criteria:

- **The artifact.** A public, legible record of two biased agents doing
  mathematics against each other. Succeeds if it is worth reading.
- **The harness.** An exact verifier plus search over line arrangements.
  Succeeds if it closes one of three open cases.

The artifact is the shell; the harness is the substance. Phase 1 ships the
shell so something is live within a day. Phase 2 adds the substance.

## 2. Non-goals

- Solving the Kobon problem in general. N(k) for arbitrary k is not the target.
- Beating Savchuk's SAT pipeline on the cases it already closed.
- Any autonomous publishing. Nothing leaves the repo except Telegram messages.
- Unattended pushes of a claimed record. GOLD notifies; the owner decides.

## 3. Target

The frontier is three cases where the improved even-k upper bound
`floor(k(k - 7/3)/3)` exceeds the best known construction by exactly one.

| k  | improved UB | best known | gap |
|----|-------------|------------|-----|
| 14 | 54          | 53         | 1   |
| 18 | 94          | 93         | 1   |
| 20 | 117         | 116        | 1   |

Each case is a binary with two winning moves:

- **CONSTRUCTOR wins** by exhibiting an arrangement the verifier confirms at
  the upper bound (54 triangles on 14 lines, etc).
- **OBSTRUCTOR wins** by proving the upper bound unreachable, which settles
  N(k) at the best-known value.

Either outcome is a citable result. Both agents know both win conditions.

## 4. Prior art the agents are seeded with

Both sides receive the same literature packet. Asymmetric seeding was
considered and rejected: the dominant failure mode of a long agent debate is
burning fifty turns rediscovering 2007 results, and that risk outweighs the
sharper bias asymmetric seeding would produce.

Packet contents:

- Tamura's bound `floor(k(k-2)/3)`.
- Clement and Bader (2007), tighter bound; unachievable for `k = 0, 2 (mod 6)`.
- The improved even-k bound `floor(k(k - 7/3)/3)`.
- Forge and Ramirez Alfonsin (1998), projective plane arrangements.
- Bartholdi, Blanc, Loisel (2008), simple arrangements of lines and pseudolines.
- Savchuk (2025), arXiv:2507.07951: table encoding for pseudoline arrangements,
  SAT via Kissat, heuristic straightening. Closed k=23 and k=27, proved no
  optimal solution for k=11.
- The full known-values table, marked proven-optimal versus best-known.

`KNOWN.md` holds this table with per-entry citations. It is the single source
of truth for what counts as a record. Agents may not edit it; only a verifier
run plus owner confirmation changes it.

## 5. Repository layout

```
THREAD.md              append-only debate transcript, the medium
LEDGER.md              claim registry: SETTLED / CONTESTED / DEAD
KNOWN.md               reference values with citations, agent-read-only
AGENDA.md              current focus, rewritten daily by the referee
agents/
  constructor.md       persona brief and priors
  obstructor.md        persona brief and priors
  referee.md           daily Opus brief
kobon/
  verify.py            exact-arithmetic verifier
  search.py            annealing baseline
  records/             verified arrangements, one JSON per accepted claim
  tests/               verifier tests, including all KNOWN.md reproductions
bin/
  turn.sh              one debate turn
  referee.sh           daily referee turn
  notify.sh            Telegram tiering
  render.py            THREAD.md -> docs/index.html
docs/index.html        generated, GitHub Pages root
```

## 6. The two agents

### CONSTRUCTOR
Prior: the even-k bound is tight and 14, 18, 20 are reachable; the gap is a
failure of search, not a theorem. Biased toward explicit constructions,
symmetry groups, near-pencil families, perturbation of known optimal odd-k
arrangements. Treats impossibility arguments as unproven until they are a
theorem with no gaps.

### OBSTRUCTOR
Prior: the even-k bound is not tight at 14, 18, 20; there is a parity or
counting obstruction nobody has isolated. Biased toward projective duality,
face-count identities, Euler relations on the arrangement graph, exhaustive
combinatorial exclusion. Treats constructions as anecdotes until verified.

Neither sees the other's brief.

### Anti-sycophancy protocol

Two Claudes agree too easily. Four mechanisms, all enforced by the driver
rather than by good intentions:

1. **Evidence-gated concession.** A concession is valid only if it cites a
   verifier run ID, or quotes a specific line of the opponent and states why
   it is mechanically airtight. The driver strips ungrounded agreement
   language and appends a violation note to the turn.
2. **No repetition.** An argument already recorded in `LEDGER.md` may not be
   re-raised without new evidence. The driver passes the full ledger every turn.
3. **Referee reopening.** The daily Opus referee hunts specifically for
   unearned agreement and may move any claim from SETTLED back to CONTESTED.
4. **Standing priors.** Each brief instructs its agent to hold its prior under
   pressure and to state explicitly what evidence would change its mind. That
   stated falsifier is recorded in the ledger and can be held against it.

`LEDGER.md` is what makes "they agree when the math convinces them"
observable rather than a matter of tone.

## 7. Turn protocol

`THREAD.md` is append-only. One block per turn:

```
## Turn 47 - OBSTRUCTOR - 2026-08-18T14:00:03Z

<prose argument>

<!-- meta
tier: none | silver | gold
addresses: [turn 46]
claims_opened: ["k14-symmetric-families-exhausted"]
claims_conceded: []
verifier_runs: ["run-0f3a91"]
falsifier: "a verified 54-triangle arrangement on 14 lines"
-->
```

`bin/turn.sh`, hourly:

1. Read `THREAD.md` tail, determine whose turn by alternation.
2. Build prompt: persona brief, full `LEDGER.md`, full `KNOWN.md`, current
   `AGENDA.md`, last 6 turn blocks, verifier CLI documentation.
3. Invoke `claude -p` on Sonnet, with the repo as working directory so the
   agent can actually run `kobon/verify.py` and `kobon/search.py`.
4. Validate the meta trailer. Reject and retry once if malformed.
5. Append the block. Regenerate `docs/index.html`. Signed commit. Push.
6. Hand the block to `bin/notify.sh`.

`bin/referee.sh`, daily on Opus: reads the last 24 turns, rewrites `LEDGER.md`
and `AGENDA.md`, and appends its own turn block marked REFEREE.

Context is windowed at 6 turns to bound cost. Continuity comes from the ledger
and agenda, not from the raw transcript.

## 8. Verifier

`kobon/verify.py`. Exact arithmetic only, `fractions.Fraction` throughout.
Floating point is banned in the accept path: float arithmetic manufactures
phantom records, and that is the standard way computational claims die.

Input: `{"k": 14, "lines": [["a","b","c"], ...]}` with each line `ax + by = c`
and coefficients as exact rational strings.

Algorithm. A Kobon triangle is a triangular face of the arrangement. For each
triple of lines:

1. Reject if any pair is parallel.
2. Compute the three pairwise intersections exactly; reject if concurrent.
3. For every other line L, evaluate `L(P) = aP.x + bP.y - c` at the three
   vertices. The triangle is uncut iff no two vertices have strictly opposite
   signs. A line through a vertex with the other two on one side does not cut
   the interior.
4. Count the triple iff uncut by all other lines.

Triangles that survive are faces of the arrangement, so pairwise
non-overlap is automatic and needs no separate check. Cost is O(k^4) exact
operations, trivial at k=20.

Acceptance gate: the verifier must reproduce every entry in `KNOWN.md` before
any agent may cite it. This is a test, not a convention.

## 9. Search

`kobon/search.py`. Simulated annealing over line parameters, float evaluation
for speed, exact re-verification of any candidate that meets or beats the
target. A float-only claim is never accepted.

The baseline exists to answer one question: is the learned component
contributing anything? Without it there is no way to distinguish "the agents
found this" from "annealing would have found it in ten seconds." The baseline
is built and its results recorded before any agent is allowed to claim credit.

## 10. Notification tiers

- **GOLD.** The verifier confirms a count exceeding `KNOWN.md` for some k, or
  a claimed impossibility proof is marked complete by the referee. Immediate
  Telegram. Only the verifier or the referee can set this; agents cannot
  self-declare.
- **SILVER.** Both agents converge on a concrete falsifiable claim after
  recorded disagreement, and the referee confirms the concession was
  evidence-gated. Immediate Telegram.
- **BRONZE.** Weekly digest of where the argument stands. Quiet, no push.

`bin/notify.sh` reuses the existing bot credentials in
`~/.claude/x-agent/bot.env`.

## 11. Scheduling

Local systemd user timers, mirroring the existing eight. Chosen over GitHub
Actions because it runs against the Claude subscription rather than metered
API billing, and because commits stay signed with the existing key and show
as Verified.

- `kobon-turn.timer`, hourly.
- `kobon-referee.timer`, daily.

Single timer per role, strict alternation, no concurrency. A lockfile guards
against overlapping runs.

## 12. Error handling

- Malformed meta trailer: one retry, then skip the turn and log. The thread
  never breaks.
- Verifier disagreement with an agent's claim: the disagreement is appended to
  the thread verbatim. Agents do not get to suppress a failed run.
- Push failure: commit locally, retry next turn. The thread is the source of
  truth, not the remote.
- Dirty tree from a killed run: park to a `wip/` branch, same pattern as
  `nano-daily.sh`, rather than stalling indefinitely.
- Repetition or stall: the referee detects it and rewrites `AGENDA.md`. Three
  consecutive stalled days triggers a BRONZE notification.

## 13. Testing

- Verifier unit tests on hand-checked small arrangements, k=3 through k=6.
- Reproduction test over every `KNOWN.md` entry with a published arrangement.
- Negative tests: concurrent lines, parallel lines, duplicate lines,
  near-degenerate coordinates that a float implementation would get wrong.
- Driver tests: turn alternation, trailer parsing, ledger merge, tier
  detection, all against fixture threads.
- Renderer test: `THREAD.md` fixture to expected HTML.

## 14. Phases

**Phase 1, the shell.** `KNOWN.md` built and cited. Agent briefs. `THREAD.md`
protocol, turn driver, renderer, Pages published, timers installed, Telegram
wired. The debate runs on literature and reasoning only, no verifier.

**Phase 2, the substance.** Verifier plus tests, reproduction gate, search
baseline, agents given tool access, GOLD path live.

## 15. Risks

- **Convergence to agreement.** Highest-probability failure. Mitigated by the
  four anti-sycophancy mechanisms; if it still happens, the referee's ledger
  will make it visible within a day rather than after a month.
- **Confident nonsense.** Agents assert unverified counts. Mitigated by phase
  2 gating and by the verifier being the only path to GOLD.
- **The result never comes.** Likely. Three cases have resisted a dedicated
  SAT attack. The artifact and the harness are the floor, and both have value
  independent of closing a case.
- **Competition.** Savchuk is active with better tooling. The edge, if any, is
  in search rather than in SAT encoding. This is accepted, not mitigated.
- **Cost drift.** Windowed context and a single hourly turn bound it. Reviewed
  after week one against actual usage.
