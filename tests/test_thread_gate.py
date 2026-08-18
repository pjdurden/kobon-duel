import thread


def mk(body="argument", **meta):
    base = {
        "tier": "none",
        "addresses": [],
        "claims_opened": [],
        "claims_conceded": [],
        "verifier_runs": [],
        "falsifier": "something",
    }
    base.update(meta)
    return thread.Turn(1, "CONSTRUCTOR", "2026-08-18T10:00:00Z", body, base)


def test_valid_meta_has_no_errors():
    assert thread.validate_meta(mk().meta) == []


def test_missing_key_is_an_error():
    m = mk().meta
    del m["falsifier"]
    assert any("falsifier" in e for e in thread.validate_meta(m))


def test_unknown_tier_is_an_error():
    assert any("tier" in e for e in thread.validate_meta(mk(tier="platinum").meta))


def test_non_list_claims_is_an_error():
    assert any("claims_opened" in e for e in thread.validate_meta(mk(claims_opened="x").meta))


def test_agent_gold_is_downgraded():
    meta, v = thread.gate_tier(mk(tier="gold").meta, allow_gold=False)
    assert meta["tier"] == "none"
    assert any("TIER_DOWNGRADED" in x for x in v)


def test_referee_gold_survives():
    meta, v = thread.gate_tier(mk(tier="gold").meta, allow_gold=True)
    assert meta["tier"] == "gold"
    assert v == []


def test_silver_is_never_downgraded():
    meta, v = thread.gate_tier(mk(tier="silver").meta, allow_gold=False)
    assert meta["tier"] == "silver"
    assert v == []


def test_concession_without_evidence_is_flagged():
    t = mk(body="You are right, the family is exhausted.",
           claims_conceded=["k14-tight"])
    assert any("UNGROUNDED_CONCESSION" in x for x in thread.check_grounding(t))


def test_concession_with_quote_is_accepted():
    t = mk(
        body="> every 3-fold symmetric family caps at 52\n\n"
             "This is airtight: the orbit count forces it.",
        claims_conceded=["k14-tight"],
    )
    assert thread.check_grounding(t) == []


def test_concession_with_verifier_run_is_accepted():
    t = mk(body="The run settles it.", claims_conceded=["k14-tight"],
           verifier_runs=["run-0f3a91"])
    assert thread.check_grounding(t) == []


def test_agreement_language_without_declared_concession_is_flagged():
    t = mk(body="Fair point, I had not considered the parity argument.")
    assert any("UNDECLARED_AGREEMENT" in x for x in thread.check_grounding(t))


def test_plain_disagreement_is_clean():
    t = mk(body="Your parity argument assumes simplicity, which is unjustified.")
    assert thread.check_grounding(t) == []


def test_apply_gate_collects_everything():
    t = mk(body="I agree completely.", tier="gold", claims_conceded=["x"])
    thread.apply_gate(t, allow_gold=False)
    assert t.meta["tier"] == "none"
    kinds = " ".join(t.violations)
    assert "TIER_DOWNGRADED" in kinds
    assert "UNGROUNDED_CONCESSION" in kinds


def test_apply_gate_returns_the_turn():
    t = mk()
    assert thread.apply_gate(t) is t
