"""The best arrangement currently held for each k.

Stage 1 stores tables only. Stage 2 adds straightened coordinates and the
exact-Fraction cross-check.
"""
from __future__ import annotations

import json
import pathlib

DIR = pathlib.Path(__file__).resolve().parent.parent / "records"


def path(k: int) -> pathlib.Path:
    return DIR / f"{k}.json"


def load(k: int):
    p = path(k)
    if not p.exists():
        return None
    return json.loads(p.read_text())


def save(record) -> pathlib.Path:
    DIR.mkdir(exist_ok=True)
    p = path(record["k"])
    p.write_text(json.dumps(record, indent=1) + "\n")
    return p
