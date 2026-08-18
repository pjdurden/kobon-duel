import take_turn
import thread

RAW_GOOD = """Here is my argument about k=14.

<!-- meta
{"tier": "none", "addresses": [3], "claims_opened": ["k14-family-a"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "an orbit count above 54"}
-->"""

RAW_NO_META = "I have opinions but no trailer."

RAW_GOLD = """I have solved it.

<!-- meta
{"tier": "gold", "addresses": [], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "n/a"}
-->"""


def test_ingest_extracts_body_and_meta():
    t = take_turn.ingest(RAW_GOOD, 4, "CONSTRUCTOR", "2026-08-18T10:00:00Z", False)
    assert t.number == 4
    assert t.speaker == "CONSTRUCTOR"
    assert "Here is my argument" in t.body
    assert t.meta["claims_opened"] == ["k14-family-a"]
    assert t.violations == []


def test_ingest_flags_missing_meta():
    t = take_turn.ingest(RAW_NO_META, 4, "CONSTRUCTOR", "ts", False)
    assert any("MALFORMED_META" in v for v in t.violations)
    assert t.meta["tier"] == "none"


def test_ingest_downgrades_agent_gold():
    t = take_turn.ingest(RAW_GOLD, 4, "CONSTRUCTOR", "ts", False)
    assert t.meta["tier"] == "none"
    assert any("TIER_DOWNGRADED" in v for v in t.violations)


def test_ingest_allows_referee_gold():
    t = take_turn.ingest(RAW_GOLD, 4, "REFEREE", "ts", True)
    assert t.meta["tier"] == "gold"


def test_build_prompt_contains_every_source():
    p = take_turn.build_prompt(
        "CONSTRUCTOR", [], "KNOWNTEXT", "LITTEXT", "LEDGERTEXT",
        "AGENDATEXT", "BRIEFTEXT",
    )
    for marker in ("KNOWNTEXT", "LITTEXT", "LEDGERTEXT", "AGENDATEXT"):
        assert marker in p


def test_build_prompt_windows_to_six_turns():
    turns = [
        thread.Turn(i, "CONSTRUCTOR", "ts", f"BODY{i}", {})
        for i in range(1, 11)
    ]
    p = take_turn.build_prompt("OBSTRUCTOR", turns, "k", "l", "g", "a", "b")
    assert "BODY10" in p and "BODY5" in p
    assert "BODY4" not in p


def test_build_prompt_names_the_speaker():
    p = take_turn.build_prompt("OBSTRUCTOR", [], "k", "l", "g", "a", "b")
    assert "OBSTRUCTOR" in p


def test_ingest_strips_code_fences_around_meta():
    raw = "Body.\n\n```\n<!-- meta\n{\"tier\": \"none\", \"addresses\": [], " \
          "\"claims_opened\": [], \"claims_conceded\": [], " \
          "\"verifier_runs\": [], \"falsifier\": \"x\"}\n-->\n```"
    t = take_turn.ingest(raw, 1, "CONSTRUCTOR", "ts", False)
    assert t.meta["tier"] == "none"
    assert not any("MALFORMED_META" in v for v in t.violations)
    assert "```" not in t.body
