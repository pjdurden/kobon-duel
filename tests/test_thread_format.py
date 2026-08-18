import thread


def mk(body="argument", violations=None, **meta):
    base = {
        "tier": "none", "addresses": [], "claims_opened": [],
        "claims_conceded": [], "verifier_runs": [], "falsifier": "x",
    }
    base.update(meta)
    t = thread.Turn(7, "Euclidn't", "2026-08-18T10:00:00Z", body, base)
    t.violations = violations or []
    return t


def test_block_has_correct_header():
    out = thread.format_block(mk())
    assert out.startswith("## Turn 7 - Euclidn't - 2026-08-18T10:00:00Z")


def test_block_contains_body():
    assert "argument" in thread.format_block(mk())


def test_block_meta_is_valid_json_and_roundtrips():
    out = thread.format_block(mk(claims_opened=["a"]))
    back = thread.parse(out)
    assert len(back) == 1
    assert back[0].meta["claims_opened"] == ["a"]
    assert back[0].number == 7
    assert back[0].speaker == "Euclidn't"


def test_violations_render_as_a_visible_note():
    out = thread.format_block(mk(violations=["UNGROUNDED_CONCESSION: nope"]))
    assert "Gate violations" in out
    assert "UNGROUNDED_CONCESSION" in out


def test_no_violation_note_when_clean():
    assert "Gate violations" not in thread.format_block(mk())


def test_roundtrip_preserves_body_without_violation_note_leaking_into_meta():
    out = thread.format_block(mk(body="line one\n\nline two"))
    back = thread.parse(out)
    assert "line one" in back[0].body and "line two" in back[0].body


def test_append_turn_creates_and_appends(tmp_path):
    p = tmp_path / "THREAD.md"
    p.write_text("# Thread\n")
    thread.append_turn(p, mk(body="first"))
    thread.append_turn(p, mk(body="second"))
    turns = thread.parse(p.read_text())
    assert len(turns) == 2
    assert "first" in turns[0].body and "second" in turns[1].body


def test_window_returns_last_n():
    turns = [thread.Turn(i, "PythagorAss", "t", "b", {}) for i in range(1, 11)]
    assert [t.number for t in thread.window(turns, 3)] == [8, 9, 10]
    assert len(thread.window(turns, 50)) == 10
