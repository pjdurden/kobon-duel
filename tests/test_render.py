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
    out = render.render(THREAD, KNOWN)
    assert "scrollHeight" not in out
    assert 'id="jump"' not in out


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


def test_theme_tokens_defined_on_bare_root():
    """The full palette must exist on bare :root, with dark as an override.

    Matches whitespace-insensitively: asserting on formatting rather than on
    the requirement made this fail the moment the CSS was reflowed.
    """
    out = render.render(THREAD, KNOWN)
    assert re.search(r":root\s*\{[^}]*--bg\s*:", out), "no light palette on bare :root"
    assert re.search(r"prefers-color-scheme\s*:\s*dark", out)
    assert re.search(r':root\[data-theme="dark"\]', out), "no explicit dark override"


def test_body_has_an_explicit_background():
    """A transparent body borrows the host page's colour."""
    out = render.render(THREAD, KNOWN)
    assert re.search(r"body\s*\{[^}]*background\s*:\s*var\(--bg\)", out)


def test_empty_thread_still_renders():
    out = render.render("# Thread\n", KNOWN)
    assert "<!doctype html>" in out.lstrip()


def test_target_table_is_derived_from_known_md():
    out = render.render(THREAD, KNOWN)
    assert "<td>14</td><td>54</td><td>53</td><td>1</td>" in out


def test_target_table_follows_known_md_when_it_changes():
    edited = "| 18 | 96 | 94 | 93 | OPEN | gap of 1 |"
    out = render.render(THREAD, edited)
    assert "<td>18</td>" in out
    assert "<td>14</td>" not in out


def test_nojekyll_marker_exists():
    """docs/ holds pre-generated HTML plus plan docs containing Liquid-looking
    braces. Without .nojekyll, Jekyll tries to parse them and the Pages build
    errors out, which is exactly what happened on the first deploy."""
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    assert (root / "docs" / ".nojekyll").exists()


def test_no_goatcounter_script_without_a_code():
    out = render.render(THREAD, KNOWN, visitor_count=None, gc_code=None)
    assert "goatcounter" not in out.lower()


def test_goatcounter_script_present_with_a_code():
    out = render.render(THREAD, KNOWN, gc_code="kobon-duel")
    assert 'data-goatcounter="https://kobon-duel.goatcounter.com/count"' in out
    assert "//gc.zgo.at/count.js" in out


def test_visitor_count_rendered_when_known():
    out = render.render(THREAD, KNOWN, visitor_count=1234, gc_code="kobon-duel")
    assert '<h2>Visitors</h2><span class="stat">1,234</span>' in out


def test_visitor_count_omitted_when_unknown():
    """A failed fetch must omit the line, never show a broken widget or a zero.

    Checks for the element, not the word: the .visitors CSS rule is always in
    the stylesheet, so a substring test on "visitors" is too coarse to mean
    anything.
    """
    out = render.render(THREAD, KNOWN, visitor_count=None, gc_code="kobon-duel")
    assert "<h2>Visitors</h2>" not in out


def test_render_still_works_with_default_args():
    out = render.render(THREAD, KNOWN)
    assert "<!doctype html>" in out.lstrip()


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


def test_dark_theme_redefines_every_light_token():
    """A token defined only in light leaves dark mode inheriting a light value."""
    out = render.render(THREAD, KNOWN)
    light = re.search(r":root\{(.*?)\}", out, re.S).group(1)
    dark = re.search(r':root\[data-theme="dark"\]\{(.*?)\}', out, re.S).group(1)
    colour = re.compile(r"(--[a-z0-9-]+)\s*:\s*(#|rgba|color-mix)")
    light_colours = {m.group(1) for m in colour.finditer(light)}
    dark_colours = {m.group(1) for m in colour.finditer(dark)}
    assert not (light_colours - dark_colours), (
        f"not redefined in dark: {sorted(light_colours - dark_colours)}"
    )
