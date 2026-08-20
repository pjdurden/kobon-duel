"""Seed records/ from the published corpus, best entry per k."""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from kobon import corpus, records, table  # noqa: E402


def main() -> int:
    best = {}
    for e in corpus.entries():
        counted = table.count(e["table"])
        if counted != e["count"]:
            sys.stderr.write("refusing to seed %s: counted %d, published %d\n"
                             % (e["key"], counted, e["count"]))
            return 1
        if e["k"] not in best or counted > best[e["k"]]["count"]:
            best[e["k"]] = {"k": e["k"], "count": counted, "table": e["table"],
                            "provenance": "corpus: %s (%s)" % (e["key"], e["title"])}
    for rec in best.values():
        records.save(rec)
    sys.stderr.write("seeded %d records\n" % len(best))
    return 0


if __name__ == "__main__":
    sys.exit(main())
