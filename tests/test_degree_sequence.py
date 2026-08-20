from kobon import corpus, table

ENTRIES = corpus.by_key()


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
    # The sum alone would also pass a bug that redistributes degrees between
    # lines while preserving the total. The published arrangement has
    # 5-rotational symmetry, so pin the actual distribution too: every line
    # sits on exactly 13 triangles.
    assert set(deg.values()) == {13}
    assert len(deg) == 15
