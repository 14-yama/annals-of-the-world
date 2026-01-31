#!/usr/bin/env python3
"""Seed Place aliases and PlaceName edges from geo-registry JSON.

This script intentionally supports TWO layers:
1) Denormalized convenience on :Place
   - Place.alt_names[] (unscoped name variants; good for search/autocomplete)
2) Canonical historical modeling
   - (:Place)-[:HAS_NAME {startYear,endYear,is_primary}]->(:PlaceName)
   - Optional visualization edge: (:Place)-[:PREVIOUSLY_KNOWN_AS]->(:PlaceName)

Why both?
- International conventions (UNGEGN, GeoNames, SKOS) treat alt names as labels.
- Historians need time-scoped names to resolve "Constantinople" vs "Istanbul" by year.

Usage:
  python geo-registry/scripts/seed_from_registry.py --run
  python geo-registry/scripts/seed_from_registry.py --run --countries-only

Notes:
- Matches existing :Place nodes by slug first, then by exact name.
- Does NOT attempt to rename Place.slug; slug is treated as immutable identity.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from db import get_neo4j_driver

COUNTRIES_JSON = ROOT / "geo-registry" / "countries.json"
COUNTRY_OVERRIDES_JSON = ROOT / "geo-registry" / "countries_overrides.json"
CITIES_JSON = ROOT / "geo-registry" / "cities_major.json"


def slugify_name_component(text: str) -> str:
    t = (text or "").strip().lower()
    # Keep unicode word characters so non-Latin scripts (e.g., 北京) remain unique.
    t = re.sub(r"[^\w]+", "-", t, flags=re.UNICODE)
    t = re.sub(r"-+", "-", t).strip("-")
    return t or "name"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def merge_country_overrides(countries: list[dict[str, Any]], overrides: dict[str, Any]) -> list[dict[str, Any]]:
    ov = (overrides or {}).get("overrides", {})
    merged: list[dict[str, Any]] = []

    for c in countries:
        c2 = dict(c)
        key = c2.get("slug")
        if key in ov:
            o = ov[key]
            # augment fields
            if "match_names" in o:
                c2["match_names"] = list(dict.fromkeys((c2.get("match_names") or []) + o["match_names"]))
            if "names" in o:
                c2["names"] = o["names"]
            if "former_names" in o:
                c2["former_names"] = o["former_names"]
        merged.append(c2)

    return merged


def resolve_place(session, *, slug: str | None, name: str | None, match_names: list[str] | None) -> dict[str, Any] | None:
    if slug:
        row = session.run("MATCH (p:Place {slug:$slug}) RETURN p.slug AS slug, p.name AS name", slug=slug).single()
        if row:
            return {"slug": row["slug"], "name": row["name"]}

    candidates = [n for n in ([name] + (match_names or [])) if n]
    for cand in candidates:
        row = session.run("MATCH (p:Place {name:$name}) RETURN p.slug AS slug, p.name AS name", name=cand).single()
        if row:
            return {"slug": row["slug"], "name": row["name"]}

    return None


def upsert_place_alt_names(session, *, place_slug: str, alt_names: list[str]) -> None:
    session.run(
        """
        MATCH (p:Place {slug:$slug})
        WITH p, (coalesce(p.alt_names, []) + $alt_names) AS merged
        SET p.alt_names = reduce(out = [], x IN merged | CASE WHEN x IN out THEN out ELSE out + x END)
        """,
        slug=place_slug,
        alt_names=alt_names,
    )


def upsert_place_name(session, *, place_slug: str, variant: dict[str, Any], relationship_is_primary: bool) -> None:
    # Create deterministic PlaceName slug tied to the Place.
    base = f"{place_slug}:{variant.get('lang','und')}:{variant.get('script','Zyyy')}:{slugify_name_component(variant.get('name',''))}"

    session.run(
        """
        MERGE (n:PlaceName {slug:$slug})
        SET n.name=$name,
            n.lang=coalesce($lang, n.lang),
            n.script=coalesce($script, n.script),
            n.is_endonym=coalesce($is_endonym, n.is_endonym),
            n.is_official=coalesce($is_official, n.is_official)
        """,
        slug=base,
        name=variant.get("name"),
        lang=variant.get("lang"),
        script=variant.get("script"),
        is_endonym=variant.get("is_endonym"),
        is_official=variant.get("is_official"),
    )

    session.run(
        """
        MATCH (p:Place {slug:$place_slug}), (n:PlaceName {slug:$name_slug})
        MERGE (p)-[r:HAS_NAME]->(n)
        SET r.is_primary = coalesce(r.is_primary, false)
        """,
        place_slug=place_slug,
        name_slug=base,
    )

    # Set temporal properties (nullable-safe): SET can remove a property if null.
    session.run(
        """
        MATCH (p:Place {slug:$place_slug})-[r:HAS_NAME]->(n:PlaceName {slug:$name_slug})
        SET r.startYear = $startYear,
            r.endYear   = $endYear,
            r.is_primary = coalesce($is_primary, r.is_primary)
        """,
        place_slug=place_slug,
        name_slug=base,
        startYear=variant.get("startYear"),
        endYear=variant.get("endYear"),
        is_primary=True if relationship_is_primary else None,
    )

    # Visualization edge: show non-primary variants as ALSO_KNOWN_AS
    # (covers both historical names AND concurrent exonyms/endonyms)
    if not relationship_is_primary:
        session.run(
            """
            MATCH (p:Place {slug:$place_slug}), (n:PlaceName {slug:$name_slug})
            MERGE (p)-[:ALSO_KNOWN_AS]->(n)
            """,
            place_slug=place_slug,
            name_slug=base,
        )


def seed_countries(session, payload: dict[str, Any], overrides: dict[str, Any]) -> None:
    countries = payload.get("countries", [])
    countries = merge_country_overrides(countries, overrides)

    for c in countries:
        resolved = resolve_place(
            session,
            slug=c.get("slug"),
            name=c.get("name"),
            match_names=c.get("match_names"),
        )
        if not resolved:
            # If a Place node doesn't exist yet, we skip (geo_registry.py seeds them).
            continue

        place_slug = resolved["slug"]

        variants = c.get("names", [])
        former = c.get("former_names", [])

        alt_names = []
        for v in variants:
            if v.get("name"):
                alt_names.append(v["name"])
        for v in former:
            if v.get("name"):
                alt_names.append(v["name"])

        if alt_names:
            upsert_place_alt_names(session, place_slug=place_slug, alt_names=alt_names)

        # PlaceName graph
        for v in variants:
            is_primary = bool(v.get("is_primary"))
            upsert_place_name(session, place_slug=place_slug, variant=v, relationship_is_primary=is_primary)

        for v in former:
            v2 = dict(v)
            # Former names are never primary
            upsert_place_name(session, place_slug=place_slug, variant=v2, relationship_is_primary=False)


def seed_cities(session, payload: dict[str, Any]) -> None:
    for c in payload.get("cities", []):
        resolved = resolve_place(session, slug=c.get("slug"), name=c.get("name"), match_names=c.get("match_names"))
        if not resolved:
            continue
        place_slug = resolved["slug"]

        variants = c.get("names", [])
        alt_names = [v["name"] for v in variants if v.get("name")]
        if alt_names:
            upsert_place_alt_names(session, place_slug=place_slug, alt_names=alt_names)

        for v in variants:
            is_primary = bool(v.get("is_primary"))
            upsert_place_name(session, place_slug=place_slug, variant=v, relationship_is_primary=is_primary)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--countries-only", action="store_true")
    parser.add_argument("--cities-only", action="store_true")
    args = parser.parse_args()

    countries_payload = load_json(COUNTRIES_JSON) if COUNTRIES_JSON.exists() else {"countries": []}
    overrides_payload = load_json(COUNTRY_OVERRIDES_JSON) if COUNTRY_OVERRIDES_JSON.exists() else {"overrides": {}}
    cities_payload = load_json(CITIES_JSON) if CITIES_JSON.exists() else {"cities": []}

    if not args.run:
        print("[DRY-RUN] Would seed:")
        print(f"  Countries: {len(countries_payload.get('countries', []))} base entries")
        print(f"  Overrides: {len((overrides_payload.get('overrides', {}) or {}))} entries")
        print(f"  Cities:    {len(cities_payload.get('cities', []))} entries")
        print("Run with --run to execute against Neo4j.")
        return 0

    driver = get_neo4j_driver()
    try:
        with driver.session() as session:
            # Requires APOC for apoc.coll.toSet
            if not args.cities_only:
                seed_countries(session, countries_payload, overrides_payload)
            if not args.countries_only:
                seed_cities(session, cities_payload)
        print("✓ Seeded Place alt_names + PlaceName edges from geo-registry")
        return 0
    finally:
        driver.close()


if __name__ == "__main__":
    raise SystemExit(main())
