#!/usr/bin/env python3
"""Normalize relationship attribute fields across cluster relationship files.

Conservative behavior:
- Backup each file to `<file>.bak.<ts>` before changing.
- Ensure each relationship has canonical fields: `id`, `start_slug`, `end_slug`, `type`,
  `description`, `status`, `evidence_url`, `citation_style`, `page_refs`, `source_note`, `_key`.
- Normalize `type` to UPPERCASE with underscores for spaces.
- If `start_slug`/`end_slug` exist, remove numeric `start_id`/`end_id` fields.
- Assign sequential integer `id` values (1..N) in output.
- Default `status` to `PROPOSED` when missing.
- Default `source_note` to `auto:normalized_relationship_attrs` when missing.
- Compute `_key` as `start_slug|TYPE|end_slug` when missing.

This script is intentionally conservative: it will not infer or change slugs, nor
add or remove relationships beyond cleaning attributes. It prints a short report
of backups and counts.
"""

import sys
import json
import glob
import os
from datetime import datetime
from pathlib import Path


TS = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def normalize_type(t):
    if t is None:
        return None
    # Replace spaces and hyphens with underscores and uppercase
    return str(t).strip().replace(" ", "_").replace("-", "_").upper()


def ensure_field(obj, key, default=None):
    if key not in obj or obj.get(key) is None:
        obj[key] = default
        return True
    return False


def compute_key(rel):
    s = rel.get("start_slug") or rel.get("start_id") or ""
    e = rel.get("end_slug") or rel.get("end_id") or ""
    t = rel.get("type") or ""
    return f"{s}|{t}|{e}"


def process_file(path):
    path = Path(path)
    if not path.exists():
        print(f"- Skipping missing file: {path}")
        return None

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as exc:
            print(f"! Failed to parse JSON {path}: {exc}")
            return None

    rels = data.get("relationships")
    if rels is None:
        print(f"- No 'relationships' array in {path}; skipping")
        return None

    # Backup
    backup = path.with_suffix(path.suffix + f".bak.{TS}")
    with open(backup, "w", encoding="utf-8") as bf:
        json.dump(data, bf, ensure_ascii=False, indent=2)

    updated_count = 0
    for idx, r in enumerate(rels, start=1):
        changed = False

        # Normalize type
        t = r.get("type")
        nt = normalize_type(t)
        if nt != t:
            r["type"] = nt
            changed = True

        # Remove numeric ids when slugs present
        if r.get("start_slug") and "start_id" in r:
            del r["start_id"]
            changed = True
        if r.get("end_slug") and "end_id" in r:
            del r["end_id"]
            changed = True

        # Ensure description
        if not r.get("description"):
            s = r.get("start_slug") or r.get("start_id") or ""
            e = r.get("end_slug") or r.get("end_id") or ""
            tval = r.get("type") or ""
            r["description"] = f"{s} {tval} {e}".strip()
            changed = True

        # status default
        if ensure_field(r, "status", "PROPOSED"):
            changed = True

        # evidence/citation/page refs defaults
        if ensure_field(r, "evidence_url", None):
            changed = True
        if ensure_field(r, "citation_style", None):
            changed = True
        if ensure_field(r, "page_refs", None):
            changed = True

        # source_note default
        if ensure_field(r, "source_note", "auto:normalized_relationship_attrs"):
            changed = True

        # compute _key
        if not r.get("_key"):
            r["_key"] = compute_key(r)
            changed = True

        # keep confidence_score if present; otherwise leave as null (do not guess)
        if "confidence_score" not in r:
            r["confidence_score"] = None
            changed = True

        if changed:
            updated_count += 1

    # Reassign sequential ids
    for i, r in enumerate(rels, start=1):
        r["id"] = i

    # Write back
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {"file": str(path), "backup": str(backup), "total": len(rels), "updated": updated_count}


def main(args):
    targets = []
    if args:
        for p in args:
            # expand globs
            targets.extend(glob.glob(p))
    else:
        targets = glob.glob("data/Relationships/*.json")

    if not targets:
        print("No target relationship files found.")
        return 2

    print(f"Normalizing {len(targets)} relationship file(s) at {TS}...")
    results = []
    for t in targets:
        res = process_file(t)
        if res:
            results.append(res)

    print("\nSummary:")
    total_rels = sum(r["total"] for r in results)
    total_updated = sum(r["updated"] for r in results)
    for r in results:
        print(f"- {r['file']}: total={r['total']}, updated={r['updated']}, backup={r['backup']}")
    print(f"Processed files: {len(results)}. Total relationships: {total_rels}. Updated rows: {total_updated}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
