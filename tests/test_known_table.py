from kobon import known


def test_parses_the_closed_cases():
    bk = known.best_known()
    assert bk[3] == 1
    assert bk[5] == 5
    assert bk[13] == 47
    assert bk[15] == 65


def test_parses_the_open_cases():
    bk = known.best_known()
    assert bk[14] == 53
    assert bk[18] == 93
    assert bk[20] == 116


def test_upper_bounds_exceed_best_known_exactly_at_the_open_cases():
    bk, ub = known.best_known(), known.best_upper_bound()
    open_cases = {k for k in bk if ub[k] > bk[k]}
    assert open_cases == {14, 18, 20}
    for k in open_cases:
        assert ub[k] - bk[k] == 1


def test_k_is_not_in_the_table_when_absent():
    assert 26 not in known.best_known()
