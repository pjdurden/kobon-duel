import pathlib
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(name):
    return (ROOT / name).read_text()


BRIEFS = [f"agents/{thread.slug(s)}.md" for s in thread.ALL_SPEAKERS]
DEBATER_BRIEFS = [f"agents/{thread.slug(s)}.md" for s in thread.SPEAKERS]


def test_all_brief_files_exist():
    for f in ["LITERATURE.md", "THREAD.md", "LEDGER.md", "AGENDA.md"] + BRIEFS:
        assert (ROOT / f).exists(), f


def test_briefs_state_opposed_priors():
    con, obs = read(DEBATER_BRIEFS[0]), read(DEBATER_BRIEFS[1])
    assert "tight" in con.lower()
    assert "not tight" in obs.lower() or "obstruction" in obs.lower()


def test_briefs_name_the_three_target_cases():
    for f in DEBATER_BRIEFS:
        body = read(f)
        for k in ("14", "18", "20"):
            assert k in body, f"{f} missing k={k}"


def test_briefs_forbid_self_declaring_gold():
    for f in DEBATER_BRIEFS:
        assert "gold" in read(f).lower()


def test_briefs_require_the_meta_trailer_keys():
    for f in BRIEFS:
        body = read(f)
        for key in thread.REQUIRED_META:
            assert key in body, f"{f} does not document meta key {key}"


def test_live_thread_is_parseable_and_alternation_is_well_formed():
    """THREAD.md grows, so assert invariants, not a fixed state.

    The original version asserted PythagorAss was next, which was only true
    while the thread was empty. That tested the clock, not the code.
    """
    turns = thread.parse(read("THREAD.md"))
    assert thread.next_speaker(turns) in thread.SPEAKERS
    numbers = [t.number for t in turns]
    assert numbers == sorted(numbers), "turn numbers must be monotonic"
    assert len(set(numbers)) == len(numbers), "turn numbers must be unique"
    debaters = [t.speaker for t in turns if t.speaker in thread.SPEAKERS]
    for a, b in zip(debaters, debaters[1:]):
        assert a != b, "debaters must alternate"


def test_literature_cites_savchuk():
    assert "2507.07951" in read("LITERATURE.md")


def test_each_speaker_has_a_brief_named_by_its_slug():
    """Guards the rename: a new display name needs a matching brief file."""
    for speaker in thread.ALL_SPEAKERS:
        assert (ROOT / "agents" / f"{thread.slug(speaker)}.md").exists(), speaker


def test_briefs_do_not_mention_the_retired_names():
    for f in BRIEFS:
        body = read(f)
        assert "CONSTRUCTOR" not in body
        assert "OBSTRUCTOR" not in body
