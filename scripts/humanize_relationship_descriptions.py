#!/usr/bin/env python3
"""Update relationship `description` fields to be human-readable.

Behavior:
- Backup the target file to `<file>.bak.<ts>`.
- For each relationship, generate `description` as:
    <start_label> <verb_phrase> <end_label>
  where labels are the `start_slug`/`end_slug` turned into readable text
  (underscores -> spaces, parentheses preserved and cleaned) and
  `verb_phrase` is derived from `type` by lowercasing and replacing underscores with spaces.
- Write updated JSON back to the file.

This is intentionally conservative: it only changes `description` and creates a backup.
"""

from pathlib import Path
from datetime import datetime
import json
import re
import sys


TS = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def slug_to_label(slug: str) -> str:
    if slug is None:
        return ""
    s = str(slug)
    # Replace underscores with spaces
    s = s.replace("_", " ")
    # Normalize multiple spaces
    s = re.sub(r"\s+", " ", s)
    # Trim
    s = s.strip()
    return s


def verb_phrase_from_type(t: str) -> str:
    if not t:
        return ""
    # Use a conservative transformation: uppercase types were canonical; make them human
    return str(t).lower().replace("_", " ")


def humanize_file(path: Path):
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rels = data.get("relationships")
    if not rels:
        print(f"No relationships found in {path}")
        return 1

    backup = path.with_suffix(path.suffix + f".bak.{TS}")
    with open(backup, "w", encoding="utf-8") as bf:
        json.dump(data, bf, ensure_ascii=False, indent=2)

    changed = 0
    for r in rels:
        start = slug_to_label(r.get("start_slug") or r.get("start_id"))
        end = slug_to_label(r.get("end_slug") or r.get("end_id"))
        verb = verb_phrase_from_type(r.get("type"))
        new_desc = f"{start} {verb} {end}".strip()
        if r.get("description") != new_desc:
            r["description"] = new_desc
            changed += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Processed {path}: total={len(rels)}, descriptions_updated={changed}, backup={backup}")
    return 0


def main(argv):
    if len(argv) < 1:
        print("Usage: humanize_relationship_descriptions.py <path-to-relationships.json>")
        return 2
    return humanize_file(Path(argv[0]))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
