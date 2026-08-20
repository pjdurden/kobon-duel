from kobon import table

# Verbatim from corpus entry pentagram_5_rot_symmetry. Do not hand-edit:
# a table can be well-formed and symmetric yet bound a different number of
# triangles than you expect.
PENTAGRAM = [
    [5, 3, 4, 2],
    [3, 5, 4, 1],
    [2, 5, 1, 4],
    [5, 2, 1, 3],
    [4, 2, 3, 1],
]


def test_three_crossing_lines_bound_one_triangle():
    assert table.count([[2, 3], [1, 3], [1, 2]]) == 1


def test_three_concurrent_lines_bound_nothing():
    """One nested group: all three meet at a single point."""
    assert table.count([[[2, 3]], [[1, 3]], [[1, 2]]]) == 0


def test_two_parallel_lines_bound_nothing():
    """Lines 1 and 2 never cross, so no triple can close."""
    assert table.count([[3], [3], [1, 2]]) == 0


def test_pentagram_has_five_triangles():
    assert table.count(PENTAGRAM) == 5


def test_triangles_are_sorted_triples_and_match_the_count():
    tris = table.triangles(PENTAGRAM)
    assert len(tris) == table.count(PENTAGRAM)
    for t in tris:
        assert list(t) == sorted(t)
        assert len(set(t)) == 3
    assert tris == sorted(tris)
