"""Per-line triangle-incidence degree sequence for a corpus arrangement.

Usage: python3 bin/degree_sequence.py <corpus-key>
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# sys.path[0] is bin/ when run as a script, so the repo root is not importable
# by default. pytest gets this from pytest.ini; a bare script does not.
sys.path.insert(0, str(ROOT))

from kobon import table  # noqa: E402


def main(argv) -> int:
    if len(argv) != 2:
        sys.stderr.write(__doc__)
        return 2
    entries = {e["key"]: e for e in json.loads(
        (ROOT / "corpus" / "arrangements.json").read_text())["entries"]}
    key = argv[1]
    if key not in entries:
        sys.stderr.write("unknown key %r; known keys:\n  %s\n"
                         % (key, "\n  ".join(sorted(entries))))
        return 2
    entry = entries[key]
    deg = table.incidence_degrees(entry["table"])
    total = table.count(entry["table"])
    print(entry["title"])
    print("k = %d, triangles = %d (published %d)"
          % (entry["k"], total, entry["count"]))
    print("degree sequence, sorted ascending:")
    print("  " + ", ".join(str(d) for d in sorted(deg.values())))
    print("by line: " + ", ".join("%d:%d" % (i, deg[i]) for i in sorted(deg)))
    print("sum = %d (must equal 3 * %d = %d)" % (sum(deg.values()), total, 3 * total))
    print("min degree = %d, so deleting that line leaves >= %d triangles on %d lines"
          % (min(deg.values()), total - min(deg.values()), entry["k"] - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
