#!/usr/bin/env python3
"""Build a Neo4j Browser-friendly payload for seeding Places from geo-registry/places.json.

This produces a single JSON object with arrays:
  - places:   Place node rows
  - contains: CONTAINS edges (country -> city/extinct)
  - variants: PlaceName rows + PREVIOUSLY_KNOWN_AS edge properties

Usage:
  python geo-registry/scripts/build_places_seed_payload.py > geo-registry/places_seed_payload.json
  python geo-registry/scripts/build_places_seed_payload.py --out geo-registry/places_seed_payload.json

Then in Neo4j Browser:
  :param payload => <paste JSON>
  // run geo-registry/seed_places.cypher
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PLACES_JSON = ROOT / "geo-registry" / "places.json"
PLACES_COUNTRIES_DIR = ROOT / "geo-registry" / "places" / "countries"


def slugify(text: str) -> str:
    t = (text or "").strip().lower()
    t = re.sub(r"[^\w]+", "-", t, flags=re.UNICODE)
    t = re.sub(r"-+", "-", t).strip("-")
    return t or "name"


def iter_variants(place_slug: str, entry: dict[str, Any]):
    for v in entry.get("names", []) or []:
        yield v, bool(v.get("is_primary", False))
    for v in entry.get("former_names", []) or []:
        yield v, False


def build_payload(places_data: dict[str, Any]) -> dict[str, Any]:
    payload = {"places": [], "contains": [], "variants": []}

    def add_place_row(slug: str, entry: dict[str, Any], default_kind: str):
        payload["places"].append(
            {
                "slug": slug,
                "name": entry.get("name", slug),
                "kind": entry.get("kind", default_kind),
                "iso": entry.get("iso"),
                "wikidata_id": entry.get("wikidata_id"),
                "pleiades_id": entry.get("pleiades_id"),
                "status": entry.get("status"),
            }
        )

        for variant, is_primary in iter_variants(slug, entry):
            name = variant.get("name")
            if not name:
                continue
            lang = variant.get("lang", "und")
            script = variant.get("script", "Latn")
            name_slug = f"{slug}:{lang}:{script}:{slugify(name)}"
            payload["variants"].append(
                {
                    "place_slug": slug,
                    "slug": name_slug,
                    "name": name,
                    "lang": lang,
                    "script": script,
                    "is_endonym": bool(variant.get("is_endonym", False)) or None,
                    "note": variant.get("note"),
                    "startYear": variant.get("startYear"),
                    "endYear": variant.get("endYear"),
                    "is_primary": bool(is_primary) or None,
                    "change_reason": variant.get("change_reason"),
                }
            )

    for country_slug, country in places_data.items():
        if country_slug.startswith("_"):
            continue

        add_place_row(country_slug, country, default_kind="country")

        for city_slug, city in (country.get("cities") or {}).items():
            add_place_row(city_slug, city, default_kind="city")
            payload["contains"].append({"parent": country_slug, "child": city_slug})

        for ext_slug, ext in (country.get("extinct_places") or {}).items():
            add_place_row(ext_slug, ext, default_kind="place")
            payload["contains"].append({"parent": country_slug, "child": ext_slug})

    return payload


def load_places_data() -> dict[str, Any]:
    # Prefer directory form if present.
    if PLACES_COUNTRIES_DIR.exists():
        out: dict[str, Any] = {}

        # New layout: countries/<slug>/<slug>.json (or countries/<slug>/place.json)
        subdirs = [p for p in PLACES_COUNTRIES_DIR.iterdir() if p.is_dir()]
        if subdirs:
            for d in sorted(subdirs, key=lambda p: p.name):
                slug = d.name
                if slug.startswith("_"):
                    continue
                place_path = d / "places.json"
                if not place_path.exists():
                    place_path = d / f"{slug}.json"
                if not place_path.exists():
                    place_path = d / "place.json"
                if not place_path.exists():
                    continue
                doc = json.loads(place_path.read_text(encoding="utf-8"))
                if not isinstance(doc, dict):
                    continue
                entry = dict(doc)
                entry.pop("slug", None)
                out[slug] = entry
            if out:
                return out

        # Older split layout: countries/<slug>.json
        flat = sorted([p for p in PLACES_COUNTRIES_DIR.glob("*.json") if p.is_file()])
        if flat:
            for path in flat:
                doc = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(doc, dict):
                    continue
                slug = doc.get("slug") or path.stem
                if not isinstance(slug, str) or not slug or slug.startswith("_"):
                    continue
                entry = dict(doc)
                entry.pop("slug", None)
                out[slug] = entry
            if out:
                return out

    # Fallback to monolithic file.
    data = json.loads(PLACES_JSON.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("places.json must be a JSON object")
    return {k: v for k, v in data.items() if isinstance(k, str) and not k.startswith("_")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="-", help="Output file (default: stdout)")
    args = parser.parse_args()

    data = load_places_data()
    payload = build_payload(data)

    out_text = json.dumps(payload, ensure_ascii=False, indent=2)

    if args.out == "-":
        sys.stdout.write(out_text)
        sys.stdout.write("\n")
        return 0

    out_path = Path(args.out)
    out_path.write_text(out_text + "\n", encoding="utf-8")
    print(f"Wrote payload: {out_path}")
    print(f"Places: {len(payload['places'])}, Contains: {len(payload['contains'])}, Variants: {len(payload['variants'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
