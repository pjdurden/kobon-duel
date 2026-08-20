import json
import pathlib

from kobon import table

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES = {e["key"]: e for e in
           json.loads((ROOT / "corpus" / "arrangements.json").read_text())["entries"]}


def test_each_triangle_contributes_three_incidences():
    t = ENTRIES["pentagram_5_rot_symmetry"]["table"]
    deg = table.incidence_degrees(t)
    assert sum(deg.values()) == 3 * table.count(t)


def test_every_line_gets_an_entry_even_at_zero():
    """A line touching no triangle must still appear, or the sequence lies."""
    t = [[3], [3], [1, 2]]
    deg = table.incidence_degrees(t)
    assert set(deg) == {1, 2, 3}
    assert deg == {1: 0, 2: 0, 3: 0}


def test_k15_optimum_degree_sum_is_consistent():
    t = ENTRIES["kobon_15_5_rot_symmetry"]["table"]
    deg = table.incidence_degrees(t)
    assert table.count(t) == 65
    assert sum(deg.values()) == 195
