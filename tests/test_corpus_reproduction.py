"""The gate: our counter must agree with every published count.

A disagreement here is a bug in us, not a discovery. This is the single test
that licenses every other number this project will ever produce.
"""
import pytest

from kobon import corpus, table

ENTRIES = corpus.entries()


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e["key"])
def test_published_count_is_reproduced(entry):
    table.validate(entry["table"])
    assert table.count(entry["table"]) == entry["count"]


def test_the_gate_covers_the_three_open_cases():
    keys = {e["key"] for e in ENTRIES}
    assert {"kobon_14_53tri", "kobon_18_93tri", "kobon_20_116tri"} <= keys


def test_the_gate_is_not_vacuous():
    # Exact, not a floor: this is the project's only external ground truth,
    # so entries silently disappearing from the corpus must fail the gate
    # loudly rather than leave it merely "still large enough" and green.
    assert len(ENTRIES) == 27
