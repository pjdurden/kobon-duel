"""One-shot import of the published Kobon arrangement corpus.

Source: https://github.com/zegalur/line-order, generate_gallery.py, CC BY 4.0,
Pavlo Savchuk 2024-2025. Individual arrangements are by their named authors;
see corpus/ATTRIBUTION.md.

Run this to regenerate corpus/arrangements.json. Tests read the committed JSON
and never touch the network.

Usage:
    python3 bin/import_corpus.py [source_path]

With no argument, fetches URL. With an argument, reads that local file
instead (useful when the sandbox has no network egress, or to pin an
exact upstream snapshot). A cached copy of the exact upstream file used
to build the committed corpus/arrangements.json lives at /tmp/g1.py; if
the network fetch fails, that cache is used as a fallback so this script
still works offline. The recorded "source" field in the output JSON is
always the upstream URL constant, regardless of how the bytes were
actually obtained, so provenance stays consistent across runs.
"""
from __future__ import annotations

import ast
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "corpus" / "arrangements.json"
URL = ("https://raw.githubusercontent.com/zegalur/line-order/"
       "master/generate_gallery.py")
FALLBACK_CACHE = pathlib.Path("/tmp/g1.py")

# Published triangle count per entry key. Taken from the gallery entry titles.
# Kept explicit rather than regex-scraped from the title so a upstream wording
# change cannot silently alter a count we gate on.
EXPECTED = {
    "triangle_3_rot_symmetry": 1, "kobon_4": 2, "kobon_4_2": 2,
    "pentagram_5_rot_symmetry": 5, "kobon_6_1": 7, "kobon_6_2": 7,
    "kobon_7": 11, "kobon_8": 15, "kobon_9_3_rot_symmetry": 21,
    "kobon_10_25tri_wajnberg": 25, "kobon_11_32tri": 32,
    "kobon_12_38tri": 38, "kobon_13_m_sym_47tri": 47,
    "kobon_14_53tri": 53, "kobon_15_5_rot_symmetry": 65,
    "kobon_16_72tri": 72, "kobon_17_85tri": 85, "kobon_18_93tri": 93,
    "kobon_19_107tri": 107, "kobon_20_116tri": 116,
    "kobon_21_133tri_1": 133, "kobon_21_133tri_2": 133,
    "kobon_21_133tri_3": 133, "kobon_22_143tri": 143,
    "kobon_23_161tri": 161, "kobon_24_172tri": 172,
    "kobon_25_191tri": 191, "kobon_27_225tri_1": 225,
    "kobon_27_225tri_2": 225, "kobon_28_238tri": 238,
    "kobon_29_261tri": 261, "kobon_31_299tri": 299, "kobon_33_341tri": 341,
}


def _literal_at(src: str, idx: int):
    """Parse the bracketed list literal starting at or after idx."""
    start = src.index("[", idx)
    depth = 0
    for e in range(start, len(src)):
        if src[e] == "[":
            depth += 1
        elif src[e] == "]":
            depth -= 1
            if depth == 0:
                return ast.literal_eval(src[start:e + 1])
    raise ValueError("unterminated list literal")


def _title_at(src: str, idx: int) -> str:
    """Read the entry_title, which upstream may split across concatenated
    string literals."""
    m = re.search(r"'entry_title'\s*:\s*(.+?)\n\s*'entry_table'",
                  src[idx:idx + 800], re.S)
    if not m:
        return ""
    parts = re.findall(r"'([^']*)'", m.group(1))
    return " ".join("".join(parts).split())


def extract(src: str, key: str):
    """Return (title, table). Raises if the table is not a literal."""
    i = src.index("'%s'" % key)
    j = src.index("'entry_table'", i)
    title = _title_at(src, i)
    ref = re.match(r"'entry_table'\s*:\s*([A-Za-z_]\w*)\s*,", src[j:j + 80])
    if ref:
        # Table stored in a module-level variable, e.g. kobon_15.
        var = re.search(r"^%s\s*=\s*\[" % re.escape(ref.group(1)), src, re.M)
        if not var:
            raise ValueError("variable %r not a module-level literal"
                             % ref.group(1))
        return title, _literal_at(src, var.start())
    if not re.match(r"'entry_table'\s*:\s*\[", src[j:j + 40]):
        raise ValueError("entry_table is a call or expression, not a literal")
    return title, _literal_at(src, j)


def fetch(source_path: str | None) -> str:
    """Get the upstream generate_gallery.py source as text.

    If source_path is given, read it from disk. Otherwise fetch URL, falling
    back to the on-disk cache of the exact upstream file if the network is
    unavailable.
    """
    if source_path is not None:
        return pathlib.Path(source_path).read_text(encoding="utf-8")
    try:
        return urllib.request.urlopen(URL, timeout=60).read().decode("utf-8")
    except Exception as exc:  # noqa: BLE001 - network may be sandboxed
        if FALLBACK_CACHE.exists():
            sys.stderr.write(
                "using fallback cache %s because fetching %s raised "
                "%s: %s\n" % (FALLBACK_CACHE, URL, type(exc).__name__, exc))
            return FALLBACK_CACHE.read_text(encoding="utf-8")
        raise


def main() -> int:
    source_path = sys.argv[1] if len(sys.argv) > 1 else None
    src = fetch(source_path)
    entries, skipped = [], []
    for key, count in EXPECTED.items():
        try:
            title, table = extract(src, key)
        except Exception as exc:  # noqa: BLE001 - reason is reported, not swallowed
            skipped.append({"key": key, "reason": f"{type(exc).__name__}: {exc}"})
            continue
        entries.append({"key": key, "k": len(table), "count": count,
                        "title": title, "table": table})
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(
        {"source": URL, "license": "CC BY 4.0",
         "entries": entries, "skipped": skipped}, indent=1) + "\n")
    sys.stderr.write("imported %d entries, skipped %d\n"
                     % (len(entries), len(skipped)))
    for s in skipped:
        sys.stderr.write("  skipped %s: %s\n" % (s["key"], s["reason"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
