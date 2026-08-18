import json
import re
import render

THREAD = """# Thread

## Turn 1 - CONSTRUCTOR - 2026-08-18T10:00:00Z

The bound is tight. Consider `k=14`.

<!-- meta
{"tier": "none", "addresses": [], "claims_opened": [], "claims_conceded": [],
 "verifier_runs": [], "falsifier": "x"}
-->

## Turn 2 - OBSTRUCTOR - 2026-08-18T11:00:00Z

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
    assert out.count('class="turn') == 2


def test_speaker_classes_are_distinct():
    out = render.render(THREAD, KNOWN)
    assert "turn constructor" in out
    assert "turn obstructor" in out


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
    out = render.render(THREAD, KNOWN)
    assert ":root {" in out
    assert "prefers-color-scheme: dark" in out


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
