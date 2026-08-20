# kobon-duel

Two Claude sessions with opposed priors argue about the Kobon triangle problem
through an append-only file. A daily referee on a stronger model rewrites the
ledger and can reopen anything they agreed on.

**Live transcript: https://pjdurden.github.io/kobon-duel/**

## The target

N(k) is the maximum number of nonoverlapping triangles formed by an arrangement
of k lines. For even k the tightest published bound is `floor(k(3k-7)/9)`. It is
met at k = 10, 12, 16 and misses by exactly one at k = 14, 18, 20.

| k | best upper bound | best known | gap |
|---|---|---|---|
| 14 | 54 | 53 | 1 |
| 18 | 94 | 93 | 1 |
| 20 | 117 | 116 | 1 |

Each case closes in one of two ways: exhibit an arrangement meeting the bound,
or prove the bound unreachable. PythagorAss argues the first is possible,
Euclidn't argues the second.

## Why two agents

Two instances of the same model agree with each other by default, which is
useless. Four mechanisms push against that, all enforced by the driver rather
than by instruction:

1. Opposed seeded priors, and neither agent sees the other's brief.
2. A concession is valid only if it cites a verifier run or quotes the specific
   line being conceded to. Ungrounded agreement gets a violation note stamped on
   the turn, in public.
3. An argument already in the ledger cannot be re-raised without new evidence.
4. The referee hunts specifically for unearned agreement and can move any claim
   from SETTLED back to CONTESTED.

Neither debater can declare a result. Only the verifier or the referee can.

## Prior art

Savchuk (2025), [arXiv:2507.07951](https://arxiv.org/abs/2507.07951), gives a
table encoding for pseudoline arrangements, a SAT search via Kissat, and a
straightening heuristic. It closed k=23 and k=27 and proved no optimal solution
exists for k=11. Both agents are seeded with it. It did not close 14, 18, or 20.

## Layout

| path | role |
|---|---|
| `THREAD.md` | the transcript, append-only, the medium |
| `LEDGER.md` | claim registry, rewritten daily by the referee |
| `AGENDA.md` | current focus, rewritten daily |
| `KNOWN.md` | reference values, read-only to agents |
| `LITERATURE.md` | shared literature packet |
| `agents/` | the three briefs |
| `bin/` | drivers, parser, renderer, notifier |
| `docs/` | generated site |
| `corpus/` | published arrangements, imported, read-only |
| `records/` | best arrangement currently held per k |

## Status

Phase 1: the debate loop. Live.
Phase 2 stage 1: arrangement corpus, combinatorial triangle counter,
reproduction gate. Live. The counter reproduces every published best-known
count in the imported corpus: 27 of 33 candidate arrangements, spanning k=3 to
k=27. The remaining six candidates (the largest, up to k=33) are skipped
because their tables are built by function calls upstream rather than stored
as list literals; importing those is deferred to a later stage.
Phase 2 stages 2 and 3: registry, agent tool access, flip search, exhaustive
search. Not yet built. Until the registry exists, no claimed construction can
be marked gold.

## Credits

The arrangement corpus in `corpus/` is imported from
[zegalur/line-order](https://github.com/zegalur/line-order) by Pavlo Savchuk,
CC BY 4.0. The arrangements themselves are the work of Johannes Bader,
Toshitaka Suzuki, Kyle Wood, Kabanovitch, Wajnberg, Honma and Savchuk. This
project discovered none of them. Full attribution in `corpus/ATTRIBUTION.md`.
