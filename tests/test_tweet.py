import tweet


def test_compose_appends_both_links():
    out, why = tweet.compose("Day 3. They are still arguing about mod-2 filters.")
    assert out is not None, why
    assert tweet.SITE in out
    assert tweet.REPO in out


def test_compose_fits_the_x_budget():
    out, _ = tweet.compose("x" * tweet.MAX_TEXT)
    assert out is not None
    assert tweet.weighted_len(out) <= tweet.LIMIT


def test_compose_rejects_text_one_char_over_budget():
    out, why = tweet.compose("x" * (tweet.MAX_TEXT + 1))
    assert out is None
    assert "too long" in why.lower()


def test_compose_rejects_empty():
    assert tweet.compose("")[0] is None
    assert tweet.compose(None)[0] is None
    assert tweet.compose("   ")[0] is None


def test_compose_rejects_text_containing_its_own_link():
    out, why = tweet.compose("See https://example.com for details.")
    assert out is None
    assert "link" in why.lower()


def test_compose_rejects_hashtags():
    out, why = tweet.compose("Big news #math #ai")
    assert out is None
    assert "hashtag" in why.lower()


def test_compose_strips_em_dashes():
    out, _ = tweet.compose("Two agents — one referee.")
    assert out is not None
    assert "—" not in out


def test_weighted_len_counts_links_as_tco_length():
    """X counts every URL as 23 characters regardless of real length."""
    short = "a " + "https://x.co/1"
    long = "a " + "https://pjdurden.github.io/kobon-duel/some/very/long/path"
    assert tweet.weighted_len(short) == tweet.weighted_len(long) == 2 + tweet.TCO


def test_from_thread_uses_the_last_referee_turn():
    text = (
        "# T\n\n"
        "## Turn 1 - REFEREE - ts\n\nbody\n\n"
        '<!-- meta\n{"tier": "none", "addresses": [], "claims_opened": [],'
        ' "claims_conceded": [], "verifier_runs": [], "falsifier": "x",'
        ' "tweet": "REFEREE ONE"}\n-->\n\n'
        "## Turn 2 - PythagorAss - ts\n\nbody\n\n"
        '<!-- meta\n{"tier": "none", "addresses": [], "claims_opened": [],'
        ' "claims_conceded": [], "verifier_runs": [], "falsifier": "x",'
        ' "tweet": "DEBATER SHOULD BE IGNORED"}\n-->\n'
    )
    out, _ = tweet.from_thread(text)
    assert out is not None
    assert "REFEREE ONE" in out
    assert "DEBATER" not in out


def test_from_thread_returns_none_when_referee_omitted_the_field():
    text = (
        "# T\n\n## Turn 1 - REFEREE - ts\n\nbody\n\n"
        '<!-- meta\n{"tier": "none", "addresses": [], "claims_opened": [],'
        ' "claims_conceded": [], "verifier_runs": [], "falsifier": "x"}\n-->\n'
    )
    out, why = tweet.from_thread(text)
    assert out is None
    assert "no tweet" in why.lower()


def test_from_thread_returns_none_with_no_referee_turn():
    text = (
        "# T\n\n## Turn 1 - PythagorAss - ts\n\nbody\n\n"
        '<!-- meta\n{"tier": "none", "addresses": [], "claims_opened": [],'
        ' "claims_conceded": [], "verifier_runs": [], "falsifier": "x",'
        ' "tweet": "nope"}\n-->\n'
    )
    assert tweet.from_thread(text)[0] is None


def test_posting_is_disabled_by_default(tmp_path, monkeypatch):
    """Absent flag file means never post. The referee runs unattended."""
    monkeypatch.setattr(tweet, "ENABLE_FLAG", tmp_path / "tweets.enabled")
    assert tweet.posting_enabled() is False


def test_posting_enabled_when_the_flag_exists(tmp_path, monkeypatch):
    flag = tmp_path / "tweets.enabled"
    flag.write_text("")
    monkeypatch.setattr(tweet, "ENABLE_FLAG", flag)
    assert tweet.posting_enabled() is True
