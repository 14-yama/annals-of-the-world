#!/usr/bin/env python3
"""Ensure clusters have IS_PART_OF relationships to their parents.

This script scans `data/Relationships/relationships.*.json` files and
adds an `IS_PART_OF` relationship if missing for a curated mapping.

It edits files in-place and prints a summary. Use --dry-run to preview.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
RELS_DIR = ROOT / "data" / "Relationships"

# Mapping of cluster -> parent (per cluster_hierarchy.md recommendations)
PARENT_MAP: Dict[str, str] = {
    "English_Reformation": "European_Reformations",
    "German_Reformation": "European_Reformations",
    "Swiss_Reformation": "European_Reformations",
    "Radical_Reformation": "European_Reformations",
    "Scottish_Reformation": "European_Reformations",
    "French_Reformation": "European_Reformations",
    "Dutch_Reformation": "European_Reformations",
    "Scandinavian_Reformations": "European_Reformations",
    "Bohemian_Moravian_Reformation": "European_Reformations",
    "Polish_Lithuanian_Reformation": "European_Reformations",
    "Catholic_Reformation": "European_Reformations",
    "Early_Christianity": "Christian_Tradition",
    "Hebrew_Tradition": "Hebrew_Tradition",
    # Recommended parent for intellectual/exchange clusters
    "Jewish-Islamic_Exchange": "Interreligious_Exchange",
    # Subcluster example: ensure the Luther-focused subcluster is attached
    "Luther_95_Theses_and_Aftermath_1517_1525": "German_Reformation",
}


def find_relationship_files() -> Dict[str, Path]:
    mapping: Dict[str, Path] = {}
    for path in sorted(RELS_DIR.glob("relationships.*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            meta = payload.get("_meta") or {}
            cluster = meta.get("cluster")
            if cluster:
                mapping[cluster] = path
                continue
        except Exception:
            pass
        # Fall back to filename extraction
        name = path.name
        if name.startswith("relationships.") and name.endswith(".json"):
            cluster = name[len("relationships."):-len(".json")]
            mapping[cluster] = path
    return mapping


def ensure_is_part_of(path: Path, cluster: str, parent: str, dry_run: bool = False) -> bool:
    """Return True if file was modified (or would be modified in dry-run)."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    rels: List[dict] = payload.get("relationships") or []

    exists = any(
        (r.get("type") == "IS_PART_OF") and r.get("start_slug") == cluster and r.get("end_slug") == parent
        for r in rels
    )
    if exists:
        print(f"OK: {cluster} already has IS_PART_OF -> {parent} in {path.name}")
        return False

    next_id = 1
    if rels:
        try:
            next_id = max(int(r.get("id", 0)) for r in rels) + 1
        except Exception:
            next_id = len(rels) + 1

    new = {
        "id": next_id,
        "start_slug": cluster,
        "end_slug": parent,
        "type": "IS_PART_OF",
        "description": f"{cluster} has parent root {parent}.",
        "status": "PROPOSED",
        "evidence_url": None,
        "citation_style": "Chicago 17",
        "page_refs": None,
        "source_note": "auto:from_script:ensure_is_part_of",
        "_key": f"{cluster}|IS_PART_OF|{parent}",
        "confidence_score": None,
    }
    rels.append(new)
    payload["relationships"] = rels

    if dry_run:
        print(f"[dry-run] Would add IS_PART_OF for {cluster} -> {parent} into {path.name}")
        return True

    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {path.name}: added IS_PART_OF {cluster} -> {parent}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    args = parser.parse_args()

    rel_files = find_relationship_files()
    modified = []

    for cluster, parent in PARENT_MAP.items():
        path = rel_files.get(cluster)
        if not path:
            print(f"Warning: no relationships JSON found for cluster '{cluster}' (skipping)")
            continue
        changed = ensure_is_part_of(path, cluster, parent, dry_run=args.dry_run)
        if changed:
            modified.append((cluster, parent, path.name))

    print("\nSummary:")
    if modified:
        for c, p, fname in modified:
            print(f"  - {fname}: added {c} IS_PART_OF {p}")
    else:
        print("  No changes were necessary.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
