import last_tier


def block(n, speaker, tier, body="argument"):
    return (
        f"## Turn {n} - {speaker} - 2026-08-18T10:00:00Z\n\n{body}\n\n"
        f'<!-- meta\n{{"tier": "{tier}", "addresses": [], "claims_opened": [],'
        f' "claims_conceded": [], "verifier_runs": [], "falsifier": "x"}}\n-->\n'
    )


def test_none_tier_returns_none():
    tier, _ = last_tier.summarize("# T\n\n" + block(1, "CONSTRUCTOR", "none"))
    assert tier == "none"


def test_silver_is_detected():
    tier, msg = last_tier.summarize("# T\n\n" + block(2, "OBSTRUCTOR", "silver"))
    assert tier == "silver"
    assert "Turn 2" in msg
    assert "OBSTRUCTOR" in msg


def test_gold_is_detected():
    tier, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert tier == "gold"
    assert "GOLD" in msg


def test_only_the_last_turn_counts():
    text = "# T\n\n" + block(1, "CONSTRUCTOR", "gold") + block(2, "OBSTRUCTOR", "none")
    assert last_tier.summarize(text)[0] == "none"


def test_empty_thread_is_none():
    assert last_tier.summarize("# T\n")[0] == "none"


def test_message_has_no_em_dashes():
    _, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert "—" not in msg


def test_message_includes_the_pages_link():
    _, msg = last_tier.summarize("# T\n\n" + block(3, "REFEREE", "gold"))
    assert "pjdurden.github.io/kobon-duel" in msg
