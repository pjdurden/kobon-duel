from fractions import Fraction as F

from kobon import verify


def test_three_lines_make_one_triangle():
    lines = [(1, 0, 0), (0, 1, 0), (1, 1, 1)]
    assert verify.count(lines) == 1


def test_concurrent_lines_make_no_triangle():
    """Three lines through the origin bound nothing."""
    lines = [(1, 0, 0), (0, 1, 0), (1, 1, 0)]
    assert verify.count(lines) == 0


def test_parallel_lines_are_skipped():
    lines = [(1, 0, 0), (1, 0, 1), (0, 1, 0)]
    assert verify.count(lines) == 0


def test_a_fourth_line_can_cut_the_triangle_away():
    """Cutting straight through the interior destroys the only triangle."""
    base = [(1, 0, 0), (0, 1, 0), (1, 1, 1)]
    assert verify.count(base) == 1
    cutter = (1, -1, 0)  # y = x, passes through the interior
    assert verify.count(base + [cutter]) == 2


def test_exact_arithmetic_survives_a_near_degenerate_vertex():
    """Floats would collapse this; Fractions must not."""
    eps = F(1, 10**12)
    lines = [(1, 0, 0), (0, 1, 0), (1, 1, 1), (1, 1, 1 + eps)]
    assert verify.count(lines) == 1


def test_pentagram_is_the_optimal_five_line_arrangement():
    """N(5) = 5, and a pentagram achieves it. This is the site's diagram."""
    from bin_diagram_helper import pentagram
    assert verify.count(pentagram()) == 5


def test_triangles_returns_three_distinct_vertices_each():
    for i, j, k, verts in verify.triangles([(1, 0, 0), (0, 1, 0), (1, 1, 1)]):
        assert len({verts[0], verts[1], verts[2]}) == 3
