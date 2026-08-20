import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "corpus" / "arrangements.json"


def load():
    return json.loads(DATA.read_text())


def test_corpus_file_exists_and_parses():
    data = load()
    assert "entries" in data and "skipped" in data


def test_corpus_has_the_open_cases():
    entries = {e["key"]: e for e in load()["entries"]}
    for key, k, count in [
        ("kobon_14_53tri", 14, 53),
        ("kobon_18_93tri", 18, 93),
        ("kobon_20_116tri", 20, 116),
        ("kobon_15_5_rot_symmetry", 15, 65),
    ]:
        assert key in entries, f"{key} missing from corpus"
        assert entries[key]["k"] == k
        assert entries[key]["count"] == count


def test_every_entry_has_k_rows_and_an_attribution():
    for e in load()["entries"]:
        assert len(e["table"]) == e["k"], e["key"]
        assert e["title"].strip(), e["key"]


def test_skipped_entries_are_recorded_not_hidden():
    """A corpus that silently drops entries reads as complete when it is not."""
    for s in load()["skipped"]:
        assert s["key"] and s["reason"]
