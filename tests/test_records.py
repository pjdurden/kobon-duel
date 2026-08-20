import json
import pathlib

import pytest

from kobon import known, records, table

ROOT = pathlib.Path(__file__).resolve().parent.parent
RECORD_FILES = sorted((ROOT / "records").glob("*.json"))


def test_records_directory_is_populated():
    assert RECORD_FILES, "run: python3 bin/seed_records.py"


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_stored_count_matches_a_recount(path):
    rec = json.loads(path.read_text())
    assert table.count(rec["table"]) == rec["count"]


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_record_meets_or_beats_best_known(path):
    rec = json.loads(path.read_text())
    reference = known.best_known().get(rec["k"])
    if reference is None:
        pytest.skip(
            f"KNOWN.md has no reference value for k={rec['k']} "
            "(the table only lists k values with an established "
            "reference; this record is still checked for a correct "
            "recount by test_stored_count_matches_a_recount)"
        )
    assert rec["count"] >= reference


@pytest.mark.parametrize("path", RECORD_FILES, ids=lambda p: p.stem)
def test_record_carries_provenance(path):
    rec = json.loads(path.read_text())
    assert rec["provenance"].strip()


def test_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(records, "DIR", tmp_path)
    rec = {"k": 3, "count": 1, "table": [[2, 3], [1, 3], [1, 2]],
           "provenance": "test"}
    records.save(rec)
    assert records.load(3) == rec
    assert records.load(99) is None
