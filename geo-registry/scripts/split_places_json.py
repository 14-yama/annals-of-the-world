#!/usr/bin/env python3
"""Split geo-registry/places.json into one JSON per country.

Creates:
  geo-registry/places/countries/<country-slug>.json

Each country file contains the original country entry plus a top-level "slug" field.

Usage:
  python3 geo-registry/scripts/split_places_json.py
  python3 geo-registry/scripts/split_places_json.py --outdir geo-registry/places/countries

Notes:
- This is a one-way convenience transform for separation of concerns.
- Seed scripts are able to read either the monolithic places.json or the directory form.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_IN = ROOT / "geo-registry" / "places.json"
DEFAULT_OUTDIR = ROOT / "geo-registry" / "places" / "countries"


def load_monolith(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("places.json must be a JSON object")
    return {k: v for k, v in data.items() if isinstance(k, str) and not k.startswith("_")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", default=str(DEFAULT_IN), help="Input places.json")
    parser.add_argument(
        "--outdir",
        default=str(DEFAULT_OUTDIR),
        help="Output directory for per-country JSON files",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing country files",
    )
    args = parser.parse_args()

    inp = Path(args.inp)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    places = load_monolith(inp)

    written = 0
    skipped = 0

    for slug, entry in sorted(places.items(), key=lambda kv: kv[0]):
        if not isinstance(entry, dict):
            continue
        out_path = outdir / f"{slug}.json"
        if out_path.exists() and not args.overwrite:
            skipped += 1
            continue

        country_doc = {"slug": slug, **entry}
        out_path.write_text(json.dumps(country_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written += 1

    print(f"Wrote {written} country files to {outdir} (skipped {skipped})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
