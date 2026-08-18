import thread

FIXTURE = """# Thread

## Turn 1 - PythagorAss - 2026-08-18T10:00:00Z

The even bound is tight at 14.

<!-- meta
{"tier": "none", "addresses": [], "claims_opened": ["k14-tight"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "a proof of 53"}
-->

## Turn 2 - Euclidn't - 2026-08-18T11:00:00Z

It is not, and you have shown nothing.

<!-- meta
{"tier": "none", "addresses": [1], "claims_opened": ["k14-obstruction"],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "a 54 arrangement"}
-->

## Turn 3 - REFEREE - 2026-08-18T12:00:00Z

Both sides are asserting priors without argument.

<!-- meta
{"tier": "none", "addresses": [1, 2], "claims_opened": [],
 "claims_conceded": [], "verifier_runs": [], "falsifier": "n/a"}
-->
"""


def test_parses_all_blocks():
    turns = thread.parse(FIXTURE)
    assert [t.number for t in turns] == [1, 2, 3]
    assert [t.speaker for t in turns] == ["PythagorAss", "Euclidn't", "REFEREE"]


def test_body_excludes_meta_trailer():
    turns = thread.parse(FIXTURE)
    assert "The even bound is tight at 14." in turns[0].body
    assert "<!-- meta" not in turns[0].body
    assert "k14-tight" not in turns[0].body


def test_meta_is_parsed_as_dict():
    turns = thread.parse(FIXTURE)
    assert turns[0].meta["claims_opened"] == ["k14-tight"]
    assert turns[1].meta["addresses"] == [1]


def test_timestamp_captured():
    assert thread.parse(FIXTURE)[0].timestamp == "2026-08-18T10:00:00Z"


def test_next_speaker_alternates():
    turns = thread.parse(FIXTURE)
    assert thread.next_speaker(turns) == "PythagorAss"


def test_next_speaker_ignores_trailing_referee_run():
    turns = thread.parse(FIXTURE)[:2]
    assert thread.next_speaker(turns) == "PythagorAss"


def test_next_speaker_on_empty_thread_is_constructor():
    assert thread.next_speaker([]) == "PythagorAss"


def test_next_number_is_max_plus_one():
    assert thread.next_number(thread.parse(FIXTURE)) == 4
    assert thread.next_number([]) == 1


def test_parse_empty_text():
    assert thread.parse("") == []


def test_block_without_meta_yields_empty_meta():
    text = "## Turn 1 - PythagorAss - 2026-08-18T10:00:00Z\n\nno trailer here\n"
    turns = thread.parse(text)
    assert turns[0].meta == {}
    assert "no trailer here" in turns[0].body


def test_malformed_meta_json_yields_empty_meta():
    text = (
        "## Turn 1 - PythagorAss - 2026-08-18T10:00:00Z\n\nbody\n\n"
        "<!-- meta\n{not json}\n-->\n"
    )
    assert thread.parse(text)[0].meta == {}
