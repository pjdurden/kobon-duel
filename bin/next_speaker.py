"""Print whose turn it is."""
import pathlib
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    turns = thread.parse((ROOT / "THREAD.md").read_text())
    sys.stdout.write(thread.next_speaker(turns))
    return 0


if __name__ == "__main__":
    sys.exit(main())
