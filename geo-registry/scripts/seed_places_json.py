#!/usr/bin/env python3
"""Seed Place nodes and name variants from places.json (human-readable format).

Single-edge model using PREVIOUSLY_KNOWN_AS as the authoritative relationship.

Creates:
  - Place.alt_names[] for search
  - (:Place)-[:PREVIOUSLY_KNOWN_AS {startYear, endYear, is_primary, change_reason}]->(:PlaceName)
  - Optional derived: (:Place)-[:ENDONYM]->(:PlaceName), (:Place)-[:EXONYM]->(:PlaceName)

Usage:
  python geo-registry/scripts/seed_places_json.py           # dry-run
  python geo-registry/scripts/seed_places_json.py --run     # execute
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
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from db import get_neo4j_driver

PLACES_JSON = ROOT / "geo-registry" / "places.json"
PLACES_COUNTRIES_DIR = ROOT / "geo-registry" / "places" / "countries"
CURRENT_YEAR = datetime.now().year


def slugify(text: str) -> str:
    t = (text or "").strip().lower()
    t = re.sub(r"[^\w]+", "-", t, flags=re.UNICODE)
    t = re.sub(r"-+", "-", t).strip("-")
    return t or "name"


def load_places() -> dict[str, Any]:
    # Prefer the directory form if present.
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
    return {k: v for k, v in data.items() if isinstance(k, str) and not k.startswith("_")}


def resolve_or_create_place(session, slug: str, name: str, kind: str = "country", **extra) -> str:
    """Find existing Place by slug or name, or create if not found."""
    row = session.run("MATCH (p:Place {slug:$slug}) RETURN p.slug AS slug", slug=slug).single()
    if row:
        return row["slug"]

    # Name-based resolution is only safe for high-level geopolitical entities.
    # Cities and many historical places can share names (e.g., London), so do not
    # attempt to resolve them by name.
    if kind in {"continent", "region", "country"}:
        row = session.run(
            "MATCH (p:Place {name:$name, kind:$kind}) RETURN p.slug AS slug",
            name=name,
            kind=kind,
        ).single()
        if row:
            return row["slug"]
    
    session.run(
        """
        CREATE (p:Place {slug: $slug, name: $name, kind: $kind})
        SET p += $extra
        """,
        slug=slug, name=name, kind=kind, extra=extra
    )
    return slug


def set_alt_names(session, place_slug: str, names: list[str]) -> None:
    """Set Place.alt_names[] (deduped)."""
    session.run(
        """
        MATCH (p:Place {slug:$slug})
        WITH p, (coalesce(p.alt_names, []) + $names) AS merged
        SET p.alt_names = reduce(out = [], x IN merged | CASE WHEN x IN out THEN out ELSE out + x END)
        """,
        slug=place_slug, names=names
    )


def is_current(variant: dict[str, Any]) -> bool:
    """Check if a name variant is current (no endYear or endYear >= current year)."""
    end = variant.get("endYear")
    return end is None or end >= CURRENT_YEAR


def upsert_place_name(session, place_slug: str, variant: dict[str, Any], is_primary: bool) -> None:
    """Create PlaceName node and PREVIOUSLY_KNOWN_AS edge (authoritative).
    
    Also creates optional ENDONYM/EXONYM derived edges for current names.
    """
    name = variant.get("name", "")
    lang = variant.get("lang", "und")
    script = variant.get("script", "Latn")
    is_endonym = variant.get("is_endonym", False)
    
    # Deterministic PlaceName slug
    name_slug = f"{place_slug}:{lang}:{script}:{slugify(name)}"
    
    # Create PlaceName node
    session.run(
        """
        MERGE (n:PlaceName {slug:$slug})
        SET n.name = $name,
            n.lang = $lang,
            n.script = $script,
            n.is_endonym = $is_endonym,
            n.note = $note
        """,
        slug=name_slug,
        name=name,
        lang=lang,
        script=script,
        is_endonym=is_endonym if is_endonym else None,
        note=variant.get("note")
    )
    
    # Create PREVIOUSLY_KNOWN_AS edge (authoritative, time-scoped)
    session.run(
        """
        MATCH (p:Place {slug:$place_slug}), (n:PlaceName {slug:$name_slug})
        MERGE (p)-[r:PREVIOUSLY_KNOWN_AS]->(n)
        SET r.startYear = $startYear,
            r.endYear = $endYear,
            r.is_primary = $is_primary,
            r.change_reason = $change_reason
        """,
        place_slug=place_slug,
        name_slug=name_slug,
        startYear=variant.get("startYear"),
        endYear=variant.get("endYear"),
        is_primary=is_primary,
        change_reason=variant.get("change_reason")
    )
    
    # Create derived ENDONYM/EXONYM edges for current names only
    if is_current(variant):
        if is_endonym:
            session.run(
                """
                MATCH (p:Place {slug:$place_slug}), (n:PlaceName {slug:$name_slug})
                MERGE (p)-[:ENDONYM]->(n)
                """,
                place_slug=place_slug,
                name_slug=name_slug
            )
        elif not is_primary:
            # Current exonyms (non-primary, non-endonym, current)
            session.run(
                """
                MATCH (p:Place {slug:$place_slug}), (n:PlaceName {slug:$name_slug})
                MERGE (p)-[:EXONYM]->(n)
                """,
                place_slug=place_slug,
                name_slug=name_slug
            )


def seed_place_entry(session, slug: str, entry: dict[str, Any], parent_slug: str | None = None) -> None:
    """Seed a single place (country or city) with its name variants."""
    name = entry.get("name", slug)
    kind = entry.get("kind", "country" if parent_slug is None else "city")
    
    extra = {}
    if entry.get("wikidata_id"):
        extra["wikidata_id"] = entry["wikidata_id"]
    if entry.get("iso"):
        extra["iso"] = entry["iso"]
    if entry.get("pleiades_id"):
        extra["pleiades_id"] = entry["pleiades_id"]
    if entry.get("status"):
        extra["status"] = entry["status"]
    
    place_slug = resolve_or_create_place(session, slug, name, kind, **extra)
    
    # Link to parent country if this is a city
    if parent_slug:
        session.run(
            """
            MATCH (parent:Place {slug:$parent}), (child:Place {slug:$child})
            MERGE (parent)-[:CONTAINS]->(child)
            """,
            parent=parent_slug, child=place_slug
        )
    
    # Process name variants
    names = entry.get("names", [])
    former = entry.get("former_names", [])
    all_variants = names + former
    
    # Set alt_names for search
    alt_list = [v["name"] for v in all_variants if v.get("name")]
    if alt_list:
        set_alt_names(session, place_slug, alt_list)
    
    # Create PlaceName nodes and edges
    for v in names:
        is_primary = bool(v.get("is_primary"))
        upsert_place_name(session, place_slug, v, is_primary)
    
    for v in former:
        upsert_place_name(session, place_slug, v, is_primary=False)
    
    return place_slug


def seed_all(session, places: dict[str, Any]) -> dict[str, int]:
    """Seed all places from the registry."""
    stats = {"countries": 0, "cities": 0, "extinct": 0}
    
    for country_slug, country in places.items():
        resolved_country_slug = seed_place_entry(session, country_slug, country)
        stats["countries"] += 1
        
        cities = country.get("cities", {})
        for city_slug, city in cities.items():
            seed_place_entry(session, city_slug, city, parent_slug=resolved_country_slug)
            stats["cities"] += 1
        
        extinct = country.get("extinct_places", {})
        for ext_slug, ext in extinct.items():
            seed_place_entry(session, ext_slug, ext, parent_slug=resolved_country_slug)
            stats["extinct"] += 1
    
    return stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Execute against Neo4j")
    args = parser.parse_args()
    
    if not PLACES_JSON.exists():
        print(f"Error: {PLACES_JSON} not found")
        return 1
    
    places = load_places()
    
    if not args.run:
        print("[DRY-RUN] Would seed from places.json:")
        print(f"  Countries: {len(places)}")
        total_cities = sum(len(c.get("cities", {})) for c in places.values())
        total_extinct = sum(len(c.get("extinct_places", {})) for c in places.values())
        print(f"  Cities: {total_cities}")
        print(f"  Extinct places: {total_extinct}")
        print("\nRun with --run to execute.")
        return 0
    
    driver = get_neo4j_driver()
    try:
        with driver.session() as session:
            stats = seed_all(session, places)
        print(f"✓ Seeded {stats['countries']} countries, {stats['cities']} cities, {stats['extinct']} extinct places")
        print("  → Place.alt_names[] populated")
        print("  → (:Place)-[:PREVIOUSLY_KNOWN_AS {startYear,endYear,is_primary,change_reason}]->(:PlaceName)")
        print("  → (:Place)-[:ENDONYM]->(:PlaceName) (derived, current endonyms)")
        print("  → (:Place)-[:EXONYM]->(:PlaceName) (derived, current exonyms)")
        return 0
    finally:
        driver.close()


if __name__ == "__main__":
    raise SystemExit(main())
