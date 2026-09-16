#!/usr/bin/env python3
"""Create a new professor case from the repository template."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "advisor_case.md"
CASES = ROOT / "cases"


def valid_slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise argparse.ArgumentTypeError(
            "Use lowercase letters, numbers, and single hyphens only, for example chan-hku."
        )
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Create one PhD supervisor outreach case.")
    parser.add_argument("slug", type=valid_slug, help="Unique case name, for example chan-hku")
    args = parser.parse_args()

    CASES.mkdir(parents=True, exist_ok=True)
    destination = CASES / f"{args.slug}.md"

    if destination.exists():
        raise SystemExit(f"Case already exists: {destination.relative_to(ROOT)}")

    shutil.copyfile(TEMPLATE, destination)
    text = destination.read_text(encoding="utf-8")
    destination.write_text(text.replace("- Case slug:", f"- Case slug: {args.slug}"), encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
