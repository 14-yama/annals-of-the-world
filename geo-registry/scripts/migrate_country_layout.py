#!/usr/bin/env python3
"""Migrate geo-registry/places/countries from flat files to per-country directories.

Before:
  geo-registry/places/countries/<slug>.json

After:
  geo-registry/places/countries/<slug>/<slug>.json         # the Place (country) entry
  geo-registry/places/countries/<slug>/institutions.json   # nodes located in country
  geo-registry/places/countries/<slug>/events.json
  geo-registry/places/countries/<slug>/artifacts.json
  geo-registry/places/countries/<slug>/texts.json
  geo-registry/places/countries/<slug>/ideas.json
  geo-registry/places/countries/<slug>/movements.json
  geo-registry/places/countries/<slug>/people.json
  geo-registry/places/countries/<slug>/evidence.json

If a country file contains "_associated_nodes", this script moves those nodes into the
corresponding dedicated JSON files and removes the key from the country file.

Usage:
  python3 geo-registry/scripts/migrate_country_layout.py
  python3 geo-registry/scripts/migrate_country_layout.py --dry-run
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
COUNTRIES_DIR = ROOT / "geo-registry" / "places" / "countries"
REGISTRY_PATH = "docs/nodes/node-attribute-registry.md"

PLACE_FILENAME = "places.json"

NODE_FILES = {
    "institutions": "institutions.json",
    "events": "events.json",
    "artifacts": "artifacts.json",
    "texts": "texts.json",
    "ideas": "ideas.json",
    "movements": "movements.json",
    "people": "people.json",
    "evidence": "evidence.json",
    "frameworks": "frameworks.json",
    "timeframes": "timeframes.json",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def ensure_node_file(path: Path, country_slug: str, node_kind: str, dry_run: bool) -> None:
    if path.exists():
        return

    payload = {
        "_meta": {
            "country_slug": country_slug,
            "node_kind": node_kind,
            "registry": REGISTRY_PATH,
            "generated_at": utc_now(),
            "notes": "Country-scoped curated nodes; link via relationships during ingest.",
        },
        "nodes": [],
    }

    if dry_run:
        return
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_nodes_file(path: Path, country_slug: str, node_kind: str, nodes: list[dict[str, Any]], dry_run: bool) -> None:
    payload = {
        "_meta": {
            "country_slug": country_slug,
            "node_kind": node_kind,
            "registry": REGISTRY_PATH,
            "generated_at": utc_now(),
            "notes": "Extracted from country Place file (_associated_nodes).",
        },
        "nodes": nodes,
    }
    if dry_run:
        return
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print actions but do not write/delete")
    args = parser.parse_args()

    if not COUNTRIES_DIR.exists():
        raise SystemExit(f"Missing directory: {COUNTRIES_DIR}")

    def process_country_dir(country_slug: str, out_dir: Path, place_path: Path) -> bool:
        if not place_path.exists():
            return False

        doc = json.loads(place_path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            return False

        assoc = doc.pop("_associated_nodes", None)

        # Standardize: the country place file is always named places.json
        canonical_place_path = out_dir / PLACE_FILENAME
        if place_path.name != PLACE_FILENAME:
            if args.dry_run:
                print(f"Would rename {place_path} -> {canonical_place_path}")
            else:
                # If places.json already exists, keep it and remove the old file.
                if canonical_place_path.exists():
                    if place_path.resolve() != canonical_place_path.resolve():
                        place_path.unlink()
                else:
                    place_path.rename(canonical_place_path)
            place_path = canonical_place_path

        # If we extracted anything, rewrite the place file without _associated_nodes
        if assoc is not None and not args.dry_run:
            place_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # Write associated nodes files (if present)
        if isinstance(assoc, dict):
            for kind, filename in NODE_FILES.items():
                if kind not in {"institutions", "events", "artifacts", "texts"}:
                    continue
                if kind in assoc and isinstance(assoc[kind], list) and assoc[kind]:
                    write_nodes_file(out_dir / filename, country_slug, kind, assoc[kind], args.dry_run)

        # Ensure all node files exist (empty scaffolds)
        for kind, filename in NODE_FILES.items():
            ensure_node_file(out_dir / filename, country_slug, kind, args.dry_run)

        return True

    migrated = 0
    processed_dirs = 0

    # 1) Migrate any remaining flat files.
    flat_files = sorted([p for p in COUNTRIES_DIR.glob("*.json") if p.is_file()])
    for src in flat_files:
        doc = json.loads(src.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue

        country_slug = doc.get("slug") or src.stem
        if not isinstance(country_slug, str) or not country_slug:
            continue

        out_dir = COUNTRIES_DIR / country_slug
        place_path = out_dir / PLACE_FILENAME

        assoc = doc.pop("_associated_nodes", None)

        if not args.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            place_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # Write associated nodes files (if present)
        if isinstance(assoc, dict):
            for kind, filename in NODE_FILES.items():
                if kind not in {"institutions", "events", "artifacts", "texts"}:
                    continue
                if kind in assoc and isinstance(assoc[kind], list) and assoc[kind]:
                    write_nodes_file(out_dir / filename, country_slug, kind, assoc[kind], args.dry_run)

        for kind, filename in NODE_FILES.items():
            ensure_node_file(out_dir / filename, country_slug, kind, args.dry_run)

        if args.dry_run:
            print(f"Would migrate {src.name} -> {out_dir}/{country_slug}.json and node files")
        else:
            src.unlink()

        migrated += 1

    # 2) Ensure all existing country dirs have scaffolds and extract embedded _associated_nodes.
    for d in sorted([p for p in COUNTRIES_DIR.iterdir() if p.is_dir()], key=lambda p: p.name):
        slug = d.name
        if slug.startswith("_"):
            continue
        # Prefer places.json, but support older filenames during migration.
        place_path = d / PLACE_FILENAME
        if not place_path.exists():
            place_path = d / f"{slug}.json"
        if not place_path.exists():
            place_path = d / "place.json"
        if process_country_dir(slug, d, place_path):
            processed_dirs += 1

    if migrated == 0 and processed_dirs == 0:
        print("Nothing to migrate or process.")
        return 0

    if migrated:
        print(f"Migrated {migrated} flat files into directory layout under {COUNTRIES_DIR}")
    print(f"Ensured node scaffolds for {processed_dirs} country directories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
