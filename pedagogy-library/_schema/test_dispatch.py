"""Tests for ``dispatch.py`` and ``principles.json``.

Run from the repo root or this directory::

    python -m pytest pedagogy-library/_schema/test_dispatch.py -v
"""

from __future__ import annotations

import collections
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
PRINCIPLES_PATH = HERE / "principles.json"
README_PATH = HERE.parent / "README.md"
DISPATCH_PATH = HERE / "dispatch.py"

# The exemplar is excluded from principles.json because it's already authored.
EXEMPLAR_ID = "testing-effect"

EXPECTED_PRINCIPLE_COUNT = 49
EXPECTED_TOTAL_INDEX = 50  # exemplar + 49 to author


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------


def _load_principles() -> list[dict]:
    return json.loads(PRINCIPLES_PATH.read_text(encoding="utf-8"))


def _readme_slugs() -> set[str]:
    """Pull every slug from the README's chapter index tables.

    Each chapter row matches ``| <num> | <name> | <slug> | ...`` once; the
    slug column always lives in position 3 of the table. We accept a slug as
    any lowercase-kebab token surrounded by table pipes.
    """
    text = README_PATH.read_text(encoding="utf-8")
    slugs: set[str] = set()
    # The chapter rows have the shape ``| N | <title> | <slug> | <sources> | <effect> |``
    pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*[^|]+\|\s*([a-z0-9][a-z0-9-]+)\s*\|",
        re.MULTILINE,
    )
    for m in pattern.finditer(text):
        slugs.add(m.group(2))
    return slugs


def _run_dispatch(*args: str) -> subprocess.CompletedProcess[str]:
    """Invoke dispatch.py as a subprocess and return the completed process.

    We pass ``PYTHONIOENCODING=utf-8`` so the child's stdout writer uses
    UTF-8 even on Windows consoles whose default is cp1252; this matters for
    the brief's arrows, em-dashes, and curly quotes.
    """
    import os

    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, str(DISPATCH_PATH), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )
    return result


# ---------------------------------------------------------------------------
# principles.json structure
# ---------------------------------------------------------------------------


def test_principles_json_has_49_entries() -> None:
    """principles.json holds exactly the 49 non-exemplar chapters."""
    principles = _load_principles()
    assert len(principles) == EXPECTED_PRINCIPLE_COUNT, (
        f"expected {EXPECTED_PRINCIPLE_COUNT} entries, got {len(principles)}"
    )


def test_principles_have_unique_ids() -> None:
    principles = _load_principles()
    ids = [p["id"] for p in principles]
    duplicates = [i for i, c in collections.Counter(ids).items() if c > 1]
    assert not duplicates, f"duplicate ids: {duplicates}"


def test_principles_match_readme_slugs() -> None:
    """Every id in principles.json is also a slug in the README index."""
    principles = _load_principles()
    readme_slugs = _readme_slugs()
    # Sanity: README should expose all 50 slugs (49 + exemplar).
    assert len(readme_slugs) >= EXPECTED_TOTAL_INDEX, (
        f"README parser found {len(readme_slugs)} slugs, expected at least "
        f"{EXPECTED_TOTAL_INDEX}; the regex may need updating."
    )
    assert EXEMPLAR_ID in readme_slugs, (
        "README should include the exemplar slug 'testing-effect'."
    )

    json_ids = {p["id"] for p in principles}
    missing = json_ids - readme_slugs
    assert not missing, (
        f"principles.json ids that don't appear in README: {sorted(missing)}"
    )

    # Exemplar is the only README slug NOT in principles.json.
    extras_in_readme = readme_slugs - json_ids
    assert extras_in_readme == {EXEMPLAR_ID}, (
        f"README slugs not in principles.json: {sorted(extras_in_readme)} "
        f"(expected only {{{EXEMPLAR_ID!r}}})"
    )


def test_principles_have_required_fields() -> None:
    """Every entry has the documented field set with non-empty values."""
    principles = _load_principles()
    required = {"id", "title", "category", "anchor_citations", "secondary_domain", "notes"}
    valid_categories = {
        "01-learning-science",
        "02-instructional-design",
        "03-assessment-science",
        "04-delivery-patterns",
        "05-tutor-personas",
        "06-motivation-engagement",
        "07-runtime-decisions",
    }
    for entry in principles:
        assert required <= set(entry), (
            f"{entry.get('id')!r} is missing fields: {required - set(entry)}"
        )
        assert entry["id"], "id must be non-empty"
        assert entry["title"], f"{entry['id']}: title must be non-empty"
        assert entry["category"] in valid_categories, (
            f"{entry['id']}: invalid category {entry['category']!r}"
        )
        assert entry["anchor_citations"], (
            f"{entry['id']}: anchor_citations must have at least one entry"
        )
        for c in entry["anchor_citations"]:
            assert isinstance(c, str) and len(c) >= 20, (
                f"{entry['id']}: anchor citation too short / not a string: {c!r}"
            )
        assert entry["secondary_domain"], (
            f"{entry['id']}: secondary_domain must be non-empty"
        )
        # notes is allowed to be null / empty
        assert "notes" in entry, f"{entry['id']}: notes key must be present"


# ---------------------------------------------------------------------------
# Domain distribution
# ---------------------------------------------------------------------------


def test_secondary_domain_distribution() -> None:
    """No single domain is used more than 7 times across the 49 entries."""
    principles = _load_principles()
    counts = collections.Counter(p["secondary_domain"] for p in principles)
    overused = {d: c for d, c in counts.items() if c > 7}
    assert not overused, (
        f"domain(s) used >7 times: {overused}. Domain counts: {dict(counts)}"
    )
    # Belt and suspenders: we also expect every domain to appear at least
    # once so the library doesn't silently collapse to a few favorites.
    assert min(counts.values()) >= 1


# ---------------------------------------------------------------------------
# dispatch.py CLI behavior
# ---------------------------------------------------------------------------


def test_dispatch_list_prints_49_ids() -> None:
    """``--list`` prints exactly 49 ids, one per line."""
    result = _run_dispatch("--list")
    assert result.returncode == 0, result.stderr
    lines = [ln for ln in result.stdout.splitlines() if ln.strip()]
    assert len(lines) == EXPECTED_PRINCIPLE_COUNT, (
        f"expected {EXPECTED_PRINCIPLE_COUNT} ids, got {len(lines)}"
    )
    # Every line should be a kebab-case id, no extra punctuation.
    for ln in lines:
        assert re.fullmatch(r"[a-z0-9][a-z0-9-]*[a-z0-9]", ln), (
            f"unexpected list output line: {ln!r}"
        )


def test_dispatch_for_single_principle() -> None:
    """``--principle spaced-retrieval`` substitutes the placeholders."""
    result = _run_dispatch("--principle", "spaced-retrieval")
    assert result.returncode == 0, result.stderr
    out = result.stdout

    # Placeholder substitutions present.
    assert "spaced-retrieval" in out
    assert "01-learning-science" in out
    assert "Spaced Retrieval" in out  # title

    # No raw placeholders remain.
    for placeholder in (
        "{principle_id}",
        "{title}",
        "{category}",
        "{anchor_citations}",
        "{notes}",
        "{secondary_domain}",
    ):
        assert placeholder not in out, (
            f"unsubstituted placeholder {placeholder!r} in output"
        )

    # Cross-domain controller assignment line.
    assert "Cross-domain example MUST use avionics +" in out
    assert "basketball coaching" in out  # spaced-retrieval's pre-assigned domain


def test_dispatch_unknown_principle_exits_1() -> None:
    """Unknown id exits 1 with an error message on stderr."""
    result = _run_dispatch("--principle", "no-such-principle")
    assert result.returncode == 1
    assert "no-such-principle" in result.stderr


def test_dispatch_all_produces_49_prompts() -> None:
    """``--all`` produces exactly 49 prompt blocks separated by markers."""
    result = _run_dispatch("--all")
    assert result.returncode == 0, result.stderr
    out = result.stdout
    markers = re.findall(r"^=+ PROMPT FOR ([a-z0-9][a-z0-9-]+) =+$", out, re.MULTILINE)
    assert len(markers) == EXPECTED_PRINCIPLE_COUNT, (
        f"expected {EXPECTED_PRINCIPLE_COUNT} separator markers, got {len(markers)}"
    )

    # Order matches principles.json order.
    expected_order = [p["id"] for p in _load_principles()]
    assert markers == expected_order, "marker order should follow principles.json"


def test_anchor_citations_appear_in_output() -> None:
    """The rendered prompt contains the seed citation text from principles.json."""
    principles = _load_principles()
    # Pick a principle with a distinctive citation string.
    target = next(p for p in principles if p["id"] == "spaced-retrieval")
    seed_citation = target["anchor_citations"][0]
    # Pull a 30-char distinctive substring (avoids whitespace-normalization issues).
    needle = seed_citation[:60]

    result = _run_dispatch("--principle", "spaced-retrieval")
    assert result.returncode == 0, result.stderr
    assert needle in result.stdout, (
        f"seed citation {needle!r} not found in dispatch output"
    )


def test_dispatch_output_is_copy_paste_ready() -> None:
    """Sanity check: rendered prompt has the expected structure for an Agent call."""
    result = _run_dispatch("--principle", "spaced-retrieval")
    assert result.returncode == 0, result.stderr
    out = result.stdout

    # Brief headers we expect to survive substitution.
    for header in (
        "## Role",
        "## Inputs",
        "## Required reading",
        "## The work",
        "## Cross-domain examples",
        "## Citation rigor",
    ):
        assert header in out, f"missing brief header: {header!r}"

    # Controller assignment block (from the suffix).
    assert "## Controller assignment" in out


def test_notes_null_renders_default_string() -> None:
    """Entries with notes==null render the '(no special notes)' fallback."""
    principles = _load_principles()
    null_notes = [p for p in principles if p.get("notes") is None]
    assert null_notes, "test fixture assumption: at least one entry has notes==null"
    target = null_notes[0]
    result = _run_dispatch("--principle", target["id"])
    assert result.returncode == 0, result.stderr
    assert "(no special notes)" in result.stdout


def test_dispatch_output_to_file(tmp_path: Path) -> None:
    """``--output`` writes to file and stdout stays empty."""
    out_file = tmp_path / "prompt.txt"
    result = _run_dispatch(
        "--principle", "spaced-retrieval", "--output", str(out_file)
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == ""
    assert out_file.exists()
    body = out_file.read_text(encoding="utf-8")
    assert "spaced-retrieval" in body
    assert "## Controller assignment" in body
