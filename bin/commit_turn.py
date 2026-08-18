"""Read a raw model response on stdin, gate it, append it to THREAD.md."""
import pathlib
import sys

import take_turn
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    speaker, timestamp = sys.argv[1], sys.argv[2]
    raw = sys.stdin.read()
    turns = thread.parse((ROOT / "THREAD.md").read_text())
    turn = take_turn.ingest(
        raw,
        thread.next_number(turns),
        speaker,
        timestamp,
        allow_gold=(speaker == "REFEREE"),
    )
    thread.append_turn(ROOT / "THREAD.md", turn)
    for v in turn.violations:
        sys.stderr.write(f"violation: {v}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
