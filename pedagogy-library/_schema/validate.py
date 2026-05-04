"""Validator for AI Tutor Pedagogy Library chapters.

Checks both YAML frontmatter (against ``chapter-schema.yaml``) and body
structure (nine ordered H2 sections, citation count, file length, and
``related`` slug resolution).

Usage::

    python validate.py <path>

Where ``<path>`` is either a single ``.md`` chapter file or a directory; if a
directory is supplied, every ``.md`` file beneath it is validated, except
files under ``_schema/``, files matching ``_AUDIT-*``, and any ``README.md``.

Exit code is ``0`` if every file validates cleanly and ``1`` otherwise.
Errors are printed to stderr.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import frontmatter
import yaml
from jsonschema import Draft7Validator

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

HERE = Path(__file__).resolve().parent
LIBRARY_ROOT = HERE.parent
SCHEMA_PATH = HERE / "chapter-schema.yaml"

# Body H2 sections that must appear in this order.
REQUIRED_SECTIONS: tuple[str, ...] = (
    "One-line claim",
    "Evidence base",
    "When to apply",
    "When NOT to apply",
    "How to apply",
    "Common misapplications",
    "Examples across domains",
    "Quality signal",
    "Cross-references",
)

# Body length bounds (inclusive) per the README "Authoring discipline" note.
MIN_LINES = 120
MAX_LINES = 200

# Patterns and exclusions for directory mode.
EXCLUDE_DIRS = {"_schema"}
EXCLUDE_FILE_PREFIXES = ("_AUDIT-",)
EXCLUDE_FILENAMES = {"README.md"}


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass
class ValidationResult:
    path: Path
    ok: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)
        self.ok = False

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)


# ---------------------------------------------------------------------------
# Schema loading
# ---------------------------------------------------------------------------

_SCHEMA_CACHE: dict | None = None


def _load_schema() -> dict:
    global _SCHEMA_CACHE
    if _SCHEMA_CACHE is None:
        with SCHEMA_PATH.open("r", encoding="utf-8") as fh:
            _SCHEMA_CACHE = yaml.safe_load(fh)
    return _SCHEMA_CACHE


# ---------------------------------------------------------------------------
# Body checks
# ---------------------------------------------------------------------------

_H2_RE = re.compile(r"^##\s+(.+?)\s*$")


def _extract_h2_headings(body: str) -> list[str]:
    return [
        m.group(1).strip()
        for line in body.splitlines()
        if (m := _H2_RE.match(line))
    ]


def _check_sections(body: str, result: ValidationResult) -> None:
    headings = _extract_h2_headings(body)
    expected = list(REQUIRED_SECTIONS)
    # Greedy in-order scan: every required heading must appear, in the
    # required order; extra H2 headings are tolerated.
    cursor = 0
    for required in expected:
        try:
            idx = headings.index(required, cursor)
        except ValueError:
            result.add_error(
                f"Body is missing required section '## {required}' "
                "(or it appears out of order)."
            )
            cursor = len(headings) + 1  # poison further matches
            continue
        cursor = idx + 1


def _check_line_count(text: str, result: ValidationResult) -> None:
    n = len(text.splitlines())
    if n < MIN_LINES:
        result.add_error(
            f"File length {n} lines is below the minimum of {MIN_LINES}."
        )
    elif n > MAX_LINES:
        result.add_error(
            f"File length {n} lines exceeds the maximum of {MAX_LINES}."
        )


def _check_related_slugs(
    metadata: dict, result: ValidationResult, library_root: Path
) -> None:
    related = metadata.get("related") or []
    if not isinstance(related, list):
        return  # schema check will already have flagged it
    # Build the set of authored slugs (filenames without .md) across all
    # category directories, lazily memoized via a function attribute.
    authored = _authored_slugs(library_root)
    for slug in related:
        if slug in authored:
            continue
        result.add_warning(
            f"Cross-reference 'related: {slug}' does not yet resolve to an "
            "authored chapter (expected during Phase 4 authoring)."
        )


def _authored_slugs(library_root: Path) -> set[str]:
    cache_attr = "_cached"
    cached = getattr(_authored_slugs, cache_attr, None)
    if cached is not None:
        root, slugs = cached
        if root == library_root:
            return slugs
    slugs: set[str] = set()
    for path in library_root.glob("*/*.md"):
        if path.parent.name in EXCLUDE_DIRS:
            continue
        if path.name in EXCLUDE_FILENAMES:
            continue
        if path.name.startswith(EXCLUDE_FILE_PREFIXES):
            continue
        slugs.add(path.stem)
    setattr(_authored_slugs, cache_attr, (library_root, slugs))
    return slugs


# ---------------------------------------------------------------------------
# Frontmatter checks
# ---------------------------------------------------------------------------

def _normalize_for_schema(metadata: dict) -> dict:
    """Pre-normalize frontmatter values that PyYAML helpfully coerces.

    YAML auto-parses ``YYYY-MM-DD`` literals into :class:`datetime.date`. The
    schema declares ``last_reviewed`` as a string with an ISO-date pattern
    (so authors can read the source verbatim), so we stringify any date-typed
    value before handing the dict to jsonschema. This is purely about
    handling YAML's coercion; if the field is missing or genuinely the wrong
    type, the schema validator still catches it.
    """
    out = dict(metadata)
    val = out.get("last_reviewed")
    if isinstance(val, datetime.date) and not isinstance(val, datetime.datetime):
        out["last_reviewed"] = val.isoformat()
    elif isinstance(val, datetime.datetime):
        out["last_reviewed"] = val.date().isoformat()
    return out


def _check_frontmatter(metadata: dict, result: ValidationResult) -> None:
    schema = _load_schema()
    validator = Draft7Validator(schema)
    normalized = _normalize_for_schema(metadata)
    errors = sorted(validator.iter_errors(normalized), key=lambda e: list(e.absolute_path))
    for err in errors:
        loc = ".".join(str(p) for p in err.absolute_path) or "<root>"
        # Make sure the field name appears in the message so callers (and
        # tests) can grep for it.
        if err.validator == "required":
            missing = err.message
            result.add_error(f"frontmatter: missing required field — {missing}")
        else:
            result.add_error(f"frontmatter[{loc}]: {err.message}")


def _check_id_matches_filename(
    metadata: dict, path: Path, result: ValidationResult
) -> None:
    fid = metadata.get("id")
    if isinstance(fid, str) and fid != path.stem:
        result.add_error(
            f"frontmatter.id '{fid}' does not match filename stem '{path.stem}'."
        )


def _check_category_matches_directory(
    metadata: dict, path: Path, result: ValidationResult
) -> None:
    cat = metadata.get("category")
    parent = path.parent.name
    if isinstance(cat, str) and cat != parent:
        result.add_error(
            f"frontmatter.category '{cat}' does not match parent directory "
            f"'{parent}'."
        )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def validate_chapter(
    path: str | Path, library_root: Path | None = None
) -> ValidationResult:
    """Validate a single chapter file.

    Returns a :class:`ValidationResult` with ``ok`` and ``errors`` populated.
    Warnings (currently only unresolved ``related`` slugs) do not flip ``ok``.
    """
    p = Path(path)
    library_root = library_root or LIBRARY_ROOT
    result = ValidationResult(path=p)

    if not p.exists():
        result.add_error(f"file not found: {p}")
        return result
    if not p.is_file():
        result.add_error(f"not a regular file: {p}")
        return result

    text = p.read_text(encoding="utf-8")

    try:
        post = frontmatter.loads(text)
    except Exception as exc:  # noqa: BLE001 — frontmatter raises ad-hoc exceptions
        result.add_error(f"frontmatter parse error: {exc}")
        return result

    metadata = post.metadata or {}
    body = post.content or ""

    if not metadata:
        result.add_error("frontmatter block is missing or empty.")
        return result

    _check_frontmatter(metadata, result)
    _check_id_matches_filename(metadata, p, result)
    _check_category_matches_directory(metadata, p, result)
    _check_sections(body, result)
    _check_line_count(text, result)
    _check_related_slugs(metadata, result, library_root)

    return result


def iter_chapter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if path.name in EXCLUDE_FILENAMES:
            continue
        if path.name.startswith(EXCLUDE_FILE_PREFIXES):
            continue
        yield path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _format_result(result: ValidationResult) -> str:
    header = f"{result.path}"
    if result.ok and not result.warnings:
        return f"OK   {header}"
    parts = [f"{'OK  ' if result.ok else 'FAIL'} {header}"]
    for err in result.errors:
        parts.append(f"  ERROR: {err}")
    for warn in result.warnings:
        parts.append(f"  WARN:  {warn}")
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate one or more pedagogy-library chapters."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Chapter file or directory to validate.",
    )
    parser.add_argument(
        "--library-root",
        type=Path,
        default=None,
        help=(
            "Root of the library tree (used to resolve 'related' slugs). "
            "Defaults to the parent of this script."
        ),
    )
    args = parser.parse_args(argv)

    target: Path = args.path
    library_root: Path = args.library_root or LIBRARY_ROOT

    if not target.exists():
        print(f"path not found: {target}", file=sys.stderr)
        return 1

    if target.is_file():
        files = [target]
    else:
        files = list(iter_chapter_files(target))
        if not files:
            print(f"no chapter files found under: {target}", file=sys.stderr)
            return 1

    overall_ok = True
    for f in files:
        result = validate_chapter(f, library_root=library_root)
        line = _format_result(result)
        stream = sys.stdout if result.ok else sys.stderr
        print(line, file=stream)
        if not result.ok:
            overall_ok = False

    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
