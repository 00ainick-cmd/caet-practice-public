"""Dispatch helper that generates per-principle agent prompts.

The script is a prompt generator, not an executor. It reads
``principles.json`` and the ``authoring-brief.md`` template, fills the
placeholders for one or all principles, and writes the rendered prompt(s) to
stdout (or to a file via ``--output``). The controller in conversation invokes
the Agent tool manually with the printed prompt as input.

Usage::

    python dispatch.py --principle <id>   # one principle
    python dispatch.py --all               # all 49, separated by markers
    python dispatch.py --list              # list ids only
    python dispatch.py --principle <id> --output <path>

Exit codes:

- ``0`` on success
- ``1`` if ``--principle`` is given an unknown id
- ``2`` on usage errors (handled by argparse)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
PRINCIPLES_PATH = HERE / "principles.json"
BRIEF_PATH = HERE / "authoring-brief.md"

SEPARATOR_FMT = "========== PROMPT FOR {pid} =========="


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def load_principles(path: Path = PRINCIPLES_PATH) -> list[dict]:
    """Read and return the principles list from JSON."""
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_brief(path: Path = BRIEF_PATH) -> str:
    """Read the authoring-brief template as a string."""
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _format_anchor_citations(citations: list[str]) -> str:
    """Render anchor citations as a numbered list."""
    if not citations:
        return "(none — author starts from the literature)"
    return "\n".join(f"{i}. {c}" for i, c in enumerate(citations, start=1))


def render_prompt(entry: dict, brief_template: str) -> str:
    """Substitute the entry's fields into the brief template and append a
    cross-domain reminder.

    The authoring-brief currently uses ``{principle_id}``, ``{title}``,
    ``{category}``, ``{anchor_citations}``, and ``{notes}`` placeholders. We
    treat them as literal substrings (not Python format specifiers) so that
    curly braces elsewhere in the brief — e.g., ``{{ }}`` examples in any
    future revision — pass through untouched.
    """
    notes = entry.get("notes")
    notes_str = notes if notes else "(no special notes)"

    secondary = entry["secondary_domain"]
    rendered = brief_template
    rendered = rendered.replace("{principle_id}", entry["id"])
    rendered = rendered.replace("{title}", entry["title"])
    rendered = rendered.replace("{category}", entry["category"])
    rendered = rendered.replace(
        "{anchor_citations}", _format_anchor_citations(entry["anchor_citations"])
    )
    rendered = rendered.replace("{notes}", notes_str)
    rendered = rendered.replace("{secondary_domain}", secondary)

    # Append the cross-domain assignment as a hard requirement so the agent
    # cannot miss it. The brief itself describes how to *pick* a domain; this
    # line tells the agent which one was pre-assigned by the controller.
    suffix = (
        "\n\n---\n\n"
        "## Controller assignment\n\n"
        f"Cross-domain example MUST use avionics + {secondary}. The first "
        "example is the avionics scenario; the second example uses "
        f"{secondary}. Do not substitute another domain — the controller is "
        "tracking distribution across the 49 chapters and will reject "
        "deviations.\n"
    )
    return rendered + suffix


def render_all(principles: list[dict], brief_template: str) -> str:
    """Concatenate per-principle prompts with separator markers."""
    chunks: list[str] = []
    for entry in principles:
        chunks.append(SEPARATOR_FMT.format(pid=entry["id"]))
        chunks.append(render_prompt(entry, brief_template))
    return "\n\n".join(chunks)


def find_principle(principles: list[dict], pid: str) -> dict | None:
    """Linear lookup by id; the list is small enough that indexing is overkill."""
    for entry in principles:
        if entry["id"] == pid:
            return entry
    return None


def list_ids(principles: list[dict]) -> str:
    """Return one id per line, newline-terminated."""
    return "\n".join(entry["id"] for entry in principles) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dispatch.py",
        description=(
            "Generate per-principle agent prompts from the authoring-brief "
            "template. Output is the literal text the controller pastes into "
            "an Agent tool call."
        ),
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--principle",
        metavar="ID",
        help="Generate the prompt for one principle (slug from principles.json).",
    )
    mode.add_argument(
        "--all",
        action="store_true",
        help="Generate prompts for all 49 principles, separated by markers.",
    )
    mode.add_argument(
        "--list",
        action="store_true",
        help="List all principle ids (one per line) and exit.",
    )
    parser.add_argument(
        "--output",
        metavar="PATH",
        help="Write to PATH instead of stdout.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    principles = load_principles()

    if args.list:
        output = list_ids(principles)
    elif args.principle:
        entry = find_principle(principles, args.principle)
        if entry is None:
            print(
                f"error: no principle with id '{args.principle}' in "
                f"{PRINCIPLES_PATH}",
                file=sys.stderr,
            )
            return 1
        output = render_prompt(entry, load_brief())
    else:  # --all
        output = render_all(principles, load_brief())

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        # Force UTF-8 on stdout so the brief's Unicode characters (arrows,
        # smart quotes, em-dashes) survive on Windows consoles whose default
        # codepage is cp1252. ``reconfigure`` is a no-op on POSIX shells
        # already running in UTF-8.
        try:
            sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except (AttributeError, OSError):  # pragma: no cover - defensive
            pass
        sys.stdout.write(output)
        if not output.endswith("\n"):
            sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
