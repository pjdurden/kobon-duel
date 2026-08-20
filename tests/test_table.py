import pytest

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


def test_positions_are_sequential_for_a_simple_row():
    pos = table.positions(PENTAGRAM)
    assert pos[1] == {5: 0, 3: 1, 4: 2, 2: 3}


def test_lines_meeting_at_one_point_share_a_position():
    """A nested list in a row means those lines all cross line i at one point."""
    t = [
        [2, [3, 4]],
        [1, [3, 4]],
        [[1, 2], 4],
        [[1, 2], 3],
    ]
    pos = table.positions(t)
    assert pos[1][3] == pos[1][4]
    assert pos[1][2] != pos[1][3]


def test_a_parallel_line_is_absent_from_the_row():
    """Shorter rows are legal: a parallel line never crosses."""
    t = [
        [3],
        [3],
        [1, 2],
    ]
    pos = table.positions(t)
    assert 2 not in pos[1]
    assert 1 not in pos[2]


def test_labels_are_one_based():
    assert list(table.labels(PENTAGRAM)) == [1, 2, 3, 4, 5]


def test_validate_accepts_the_pentagram():
    table.validate(PENTAGRAM)


def test_validate_rejects_an_asymmetric_crossing():
    """If line 2 crosses line 1, line 1 must cross line 2."""
    bad = [
        [5, 3, 4, 2],
        [3, 5, 4],      # line 2 no longer lists line 1
        [2, 5, 1, 4],
        [5, 2, 1, 3],
        [4, 2, 3, 1],
    ]
    with pytest.raises(ValueError, match="1.*2|2.*1"):
        table.validate(bad)


def test_validate_rejects_a_line_listing_itself():
    bad = [[1, 3], [3, 1], [1, 2]]
    with pytest.raises(ValueError, match="itself"):
        table.validate(bad)


def test_validate_rejects_an_out_of_range_label():
    bad = [[2, 9], [1, 3], [1, 2]]
    with pytest.raises(ValueError, match="9"):
        table.validate(bad)
