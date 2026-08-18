import json
import re
import render

THREAD = """# Thread

## Turn 1 - PythagorAss - 2026-08-18T10:00:00Z

The bound is tight. Consider `k=14`.

<!-- meta
{"tier": "none", "addresses": [], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "x"}
-->

## Turn 2 - Euclidn't - 2026-08-18T11:00:00Z

</script><script>alert(1)</script>

<!-- meta
{"tier": "silver", "addresses": [1], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "y"}
-->
"""

KNOWN = "| 14 | 56 | 54 | 53 | OPEN | gap of 1 |"


def test_output_is_a_full_html_document():
    out = render.render(THREAD, KNOWN)
    assert out.lstrip().startswith("<!doctype html>")
    assert "</html>" in out


def test_every_turn_appears():
    out = render.render(THREAD, KNOWN)
    assert out.count('class="post ') == 2


def test_speaker_classes_are_distinct():
    """Classes use slugs, not display names: "Euclidn't" has an apostrophe."""
    out = render.render(THREAD, KNOWN)
    assert "pythagorass" in out
    assert "euclidnt" in out


def test_each_speaker_gets_its_own_post_tint():
    out = render.render(THREAD, KNOWN)
    assert 'class="post pythagorass"' in out
    assert 'class="post euclidnt"' in out


def test_referee_posts_are_visually_distinct():
    ref = THREAD + (
        "\n## Turn 3 - REFEREE - 2026-08-18T12:00:00Z\n\nruling\n\n"
        '<!-- meta\n{"tier": "none", "addresses": [], "claims_opened": [],'
        ' "claims_conceded": [], "verifier_runs": [], "falsifier": "x",'
        ' "tweet": "t"}\n-->\n'
    )
    out = render.render(ref, KNOWN)
    assert 'class="post referee"' in out


def test_display_names_are_shown_verbatim():
    out = render.render(THREAD, KNOWN)
    assert "PythagorAss" in out
    assert "Euclidn&#x27;t" in out or "Euclidn't" in out


def test_newest_post_comes_first():
    """Forum order, newest at the top. The page scrolls normally; the
    fixed-height auto-scrolling chat panel was tried and rejected."""
    out = render.render(THREAD, KNOWN)
    assert out.index('id="turn-2"') < out.index('id="turn-1"')


def test_only_the_newest_post_is_flagged_latest():
    out = render.render(THREAD, KNOWN)
    assert out.count('class="flag">latest') == 1
    assert out.index("latest") < out.index('id="turn-1"')


def test_addresses_render_as_reply_links():
    """What makes it read as a forum rather than a list of statements."""
    out = render.render(THREAD, KNOWN)
    assert 'In reply to <a href="#turn-1">#1</a>' in out


def test_no_reply_line_on_an_opening_post():
    out = render.render(THREAD, KNOWN)
    first = out[out.index('id="turn-1"'):]
    assert "In reply to" not in first


def test_page_is_not_a_fixed_height_scroll_container():
    """The thread scrolls with the page, not inside a panel.

    Asserts the container, not the string "scrollHeight": the collapse control
    legitimately measures element heights.
    """
    out = render.render(THREAD, KNOWN)
    assert not re.search(r"\.chat\{[^}]*overflow-y:\s*auto", out)
    assert 'id="jump"' not in out
    assert 'class="thread"' in out or 'id="thread"' in out


def test_every_turn_has_a_linkable_anchor():
    out = render.render(THREAD, KNOWN)
    assert 'id="turn-1"' in out and 'href="#turn-1"' in out


def test_turn_count_stat_is_rendered():
    out = render.render(THREAD, KNOWN)
    assert '<h2>Turns</h2><span class="stat">2</span>' in out


def test_empty_thread_says_so_instead_of_rendering_nothing():
    out = render.render("# Thread\n", KNOWN)
    assert "has not started yet" in out


def test_script_injection_in_body_cannot_break_out():
    """Bodies are embedded as JSON string literals, not raw HTML."""
    out = render.render(THREAD, KNOWN)
    assert "<script>alert(1)</script>" not in out
    assert "alert(1)" in out


def test_bodies_are_valid_json_literals():
    out = render.render(THREAD, KNOWN)
    for payload in re.findall(r'data-md="([^"]*)"', out):
        json.loads(payload.replace("&quot;", '"'))


def test_silver_tier_is_badged():
    out = render.render(THREAD, KNOWN)
    assert "tier-silver" in out


def test_page_is_light_only_with_no_dark_override():
    """Light only, deliberately.

    A prefers-color-scheme block meant the page rendered dark for anyone whose
    machine is in dark mode, which is not what this site is. Anthropic's own
    landing page is light only; so is this.
    """
    out = render.render(THREAD, KNOWN)
    # Match the media query, not the bare phrase: the stylesheet comment
    # explaining this decision contains the words too.
    assert not re.search(r"@media\s*\(\s*prefers-color-scheme", out), (
        "a dark override crept back in"
    )
    assert 'data-theme="dark"' not in out
    assert "color-scheme:light" in out.replace(" ", "")
    assert '<meta name="color-scheme" content="light">' in out


def test_ground_is_the_ivory_not_white():
    """Ivory ground with white cards is the whole look; a white ground kills it."""
    out = render.render(THREAD, KNOWN)
    assert re.search(r"--bg\s*:\s*#f0eee6", out, re.I)
    assert re.search(r"--card\s*:\s*#ffffff", out, re.I)


def test_body_has_an_explicit_background():
    """A transparent body borrows the host page's colour."""
    out = render.render(THREAD, KNOWN)
    assert re.search(r"body\s*\{[^}]*background\s*:\s*var\(--bg\)", out)


def test_problem_section_is_present_and_names_the_open_cases():
    out = render.render(THREAD, KNOWN)
    assert "The problem" in out
    assert "14, 18 and 20 lines" in out


def test_diagram_is_embedded_as_inline_svg():
    out = render.render(THREAD, KNOWN)
    assert out.count("<svg") >= 3, "expected three explainer panels"
    assert "polygon" in out, "expected shaded triangles"


def test_diagram_captions_match_verified_counts():
    """The captions are asserted against exact arithmetic inside diagram.figure()."""
    out = render.render(THREAD, KNOWN)
    assert "1 triangle" in out and "5 triangles" in out


def test_repo_link_is_in_the_top_bar():
    out = render.render(THREAD, KNOWN)
    bar = out[out.index('class="bar"'):out.index('class="wrap"')]
    assert "github.com/pjdurden/kobon-duel" in bar


def test_no_css_variable_is_used_without_being_defined():
    """Regression guard.

    Renaming the palette once left the diagram shading pointing at --a-ac,
    which no longer existed, so the triangles silently rendered black. An
    undefined var() fails at computed-value time and is invisible in tests
    that only check for substrings.
    """
    out = render.render(THREAD, KNOWN, visitor_count=7, gc_code="kobon-duel")
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", out))
    used = set(re.findall(r"var\((--[a-z0-9-]+)", out))
    assert not (used - defined), f"undefined CSS variables: {sorted(used - defined)}"


def test_reveal_and_progress_hooks_are_present():
    out = render.render(THREAD, KNOWN)
    assert 'id="progress"' in out
    assert "IntersectionObserver" in out
    assert 'class="rise' in out


def test_motion_is_disabled_under_reduced_motion():
    """Every animation must have a reduced-motion escape."""
    out = render.render(THREAD, KNOWN)
    assert "prefers-reduced-motion: reduce" in out.replace("(prefers-reduced-motion:reduce)", "(prefers-reduced-motion: reduce)")
    assert re.search(r"@media\s*\(prefers-reduced-motion:reduce\)\{[^}]*\.rise", out)


def test_triangles_carry_the_lines_that_bound_them():
    """Hovering a face should be able to name its three lines."""
    out = render.render(THREAD, KNOWN)
    assert re.search(r'class="tri" data-tri="\d+,\d+,\d+"', out)
    assert re.search(r'class="ln" data-ln="\d+"', out)


def test_filter_and_collapse_controls_are_wired():
    out = render.render(THREAD, KNOWN)
    assert 'id="filters"' in out
    assert "Read the full argument" in out
