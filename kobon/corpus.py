"""The imported arrangement corpus: published tables, counts and attribution.

Read only. Serves both as search seeds (stage 2) and as the reproduction
gate's fixture set. Per-arrangement attribution lives in
corpus/ATTRIBUTION.md, not here; this module only loads the data.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "corpus" / "arrangements.json"

_cache = None


def _load():
    global _cache
    if _cache is None:
        _cache = json.loads(DATA.read_text())
    return _cache


def entries():
    """All successfully imported arrangements, in corpus order."""
    return _load()["entries"]


def skipped():
    """Entries the importer could not translate, each with its skip reason."""
    return _load()["skipped"]


def by_key():
    """Imported arrangements indexed by their corpus key."""
    return {e["key"]: e for e in entries()}
