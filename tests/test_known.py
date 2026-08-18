"""KNOWN.md is the source of truth for records. Guard its arithmetic."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWN = ROOT / "KNOWN.md"

ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\w+)\s*\|",
    re.MULTILINE,
)


def rows():
    """(k, tamura_ub, best_ub, best_known, status) for each table row."""
    return [
        (int(k), int(t), int(b), int(n), s)
        for k, t, b, n, s in ROW_RE.findall(KNOWN.read_text())
    ]


def even_bound(k):
    """The improved even-k upper bound, floor(k(k - 7/3)/3), in exact ints."""
    return (k * (3 * k - 7)) // 9


def tamura(k):
    return (k * (k - 2)) // 3


def test_known_file_exists():
    assert KNOWN.exists()


def test_table_parses():
    assert len(rows()) >= 20


def test_tamura_column_matches_formula():
    for k, t, _, _, _ in rows():
        assert t == tamura(k), f"k={k}: tamura column {t} != {tamura(k)}"


def test_even_k_best_bound_matches_improved_formula():
    for k, _, b, _, _ in rows():
        if k % 2 == 0:
            assert b == even_bound(k), f"k={k}: bound {b} != {even_bound(k)}"


def test_target_cases_have_gap_of_exactly_one():
    by_k = {r[0]: r for r in rows()}
    for k in (14, 18, 20):
        _, _, bound, best, status = by_k[k]
        assert bound - best == 1, f"k={k}: gap is {bound - best}, expected 1"
        assert status == "OPEN", f"k={k} must be marked OPEN, got {status}"


def test_closed_even_cases_have_zero_gap():
    by_k = {r[0]: r for r in rows()}
    for k in (10, 12, 16):
        _, _, bound, best, status = by_k[k]
        assert bound == best, f"k={k}: expected closed, gap {bound - best}"
        assert status == "CLOSED"
