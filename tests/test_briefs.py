import pathlib
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(name):
    return (ROOT / name).read_text()


def test_all_brief_files_exist():
    for f in ("LITERATURE.md", "agents/constructor.md",
              "agents/obstructor.md", "agents/referee.md",
              "THREAD.md", "LEDGER.md", "AGENDA.md"):
        assert (ROOT / f).exists(), f


def test_briefs_state_opposed_priors():
    con, obs = read("agents/constructor.md"), read("agents/obstructor.md")
    assert "tight" in con.lower()
    assert "not tight" in obs.lower() or "obstruction" in obs.lower()


def test_briefs_name_the_three_target_cases():
    for f in ("agents/constructor.md", "agents/obstructor.md"):
        body = read(f)
        for k in ("14", "18", "20"):
            assert k in body, f"{f} missing k={k}"


def test_briefs_forbid_self_declaring_gold():
    for f in ("agents/constructor.md", "agents/obstructor.md"):
        assert "gold" in read(f).lower()


def test_briefs_require_the_meta_trailer_keys():
    for f in ("agents/constructor.md", "agents/obstructor.md", "agents/referee.md"):
        body = read(f)
        for key in thread.REQUIRED_META:
            assert key in body, f"{f} does not document meta key {key}"


def test_live_thread_is_parseable_and_alternation_is_well_formed():
    """THREAD.md grows, so assert invariants, not a fixed state.

    The original version asserted CONSTRUCTOR was next, which was only true
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
