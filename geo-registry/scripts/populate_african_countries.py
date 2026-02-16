#!/usr/bin/env python3
"""Populate missing template attributes for country index.json files.

Scans every country directory under geo-registry/places/countries/ and injects
any missing sections from the canonical _template/index.json into
country_profile and leadership.

By default processes African countries only.  Use --all to process every country.

Sections checked (inside country_profile):
  notes_unique, demographics, natural_resources, military, trade,
  infrastructure, international_memberships, governance_indices,
  climate_environment, debt_aid, education, diaspora_migration, digital_economy

Also checks:
  leadership.head_of_state

Usage:
  python geo-registry/scripts/populate_african_countries.py            # Africa only
  python geo-registry/scripts/populate_african_countries.py --all      # all countries
  python geo-registry/scripts/populate_african_countries.py --dry-run
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTRIES_DIR = ROOT / "geo-registry" / "places" / "countries"
TEMPLATE_PATH = COUNTRIES_DIR / "_template" / "index.json"

# ── Template defaults for every section that might be missing ─────────────────

PROFILE_DEFAULTS: dict[str, object] = {
    "notes_unique": "",
    "demographics": {
        "median_age": 0,
        "urbanization_pct": 0,
        "fertility_rate": 0,
        "life_expectancy": 0,
        "infant_mortality_per_1k": 0,
        "literacy_rate_pct": 0,
        "net_migration_rate": 0,
    },
    "natural_resources": {
        "primary": [],
        "resource_dependency_pct_gdp": 0,
        "notes": "",
    },
    "military": {
        "budget_usd": "",
        "pct_of_gdp": 0,
        "active_personnel": 0,
        "reserve_personnel": 0,
        "nuclear_status": "Non-nuclear",
        "alliances": [],
        "notes": "",
    },
    "trade": {
        "top_exports": [],
        "top_imports": [],
        "major_partners": [],
        "trade_balance": "",
        "remittances_pct_gdp": 0,
    },
    "infrastructure": {
        "internet_penetration_pct": 0,
        "electricity_access_pct": 0,
        "mobile_subscriptions_per_100": 0,
        "railway_km": 0,
        "paved_roads_pct": 0,
    },
    "international_memberships": [],
    "governance_indices": {
        "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
        "press_freedom_index": {"rank": 0, "year": 0},
        "democracy_index": {"score": 0, "category": "", "year": 0},
        "fragile_states_index": {"score": 0, "year": 0},
    },
    "climate_environment": {
        "climate_zones": [],
        "co2_emissions_mt": 0,
        "renewable_energy_pct": 0,
        "natural_hazards": [],
        "protected_areas_pct": 0,
    },
    "debt_aid": {
        "national_debt_pct_gdp": 0,
        "foreign_aid_received_usd": "",
        "notes": "",
    },
    "education": {
        "primary_enrollment_pct": 0,
        "secondary_enrollment_pct": 0,
        "tertiary_enrollment_pct": 0,
        "pisa_participation": False,
        "top_universities": [],
        "notes": "",
    },
    "diaspora_migration": {
        "diaspora_population": "",
        "refugees_hosted": 0,
        "refugees_produced": 0,
        "remittances_usd": "",
        "notes": "",
    },
    "digital_economy": {
        "e_government_index": 0,
        "mobile_money_adoption": "",
        "tech_hubs": [],
        "notes": "",
    },
}

HEAD_OF_STATE_DEFAULT: dict[str, str] = {
    "name": "",
    "title": "",
    "since": "",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def deep_copy(obj: object) -> object:
    """Return a deep copy using JSON round-trip (safe for our data)."""
    return json.loads(json.dumps(obj))


def is_african(data: dict) -> bool:
    """Check whether the index.json belongs to an African country."""
    meta = data.get("_meta", {})
    profile = data.get("country_profile", {})
    return (
        meta.get("continent", "").strip() == "Africa"
        or profile.get("continent", "").strip() == "Africa"
    )


def populate_missing(data: dict, dry_run: bool = False) -> list[str]:
    """Inject missing template sections into *data* in-place.

    Returns a list of human-readable strings describing what was added.
    """
    changes: list[str] = []
    profile = data.get("country_profile")
    if profile is None:
        return changes

    # ── country_profile sections ──────────────────────────────────────────
    for key, default in PROFILE_DEFAULTS.items():
        if key not in profile:
            profile[key] = deep_copy(default)
            changes.append(f"  + country_profile.{key}")

    # ── leadership.head_of_state ──────────────────────────────────────────
    leadership = data.get("leadership")
    if leadership is not None and "head_of_state" not in leadership:
        leadership["head_of_state"] = deep_copy(HEAD_OF_STATE_DEFAULT)
        changes.append("  + leadership.head_of_state")

    # ── Update timestamp ──────────────────────────────────────────────────
    if changes and not dry_run:
        data.setdefault("_meta", {})["updated_at"] = utc_now()

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Populate missing template attributes for country index.json files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing files.",
    )
    parser.add_argument(
        "--country",
        type=str,
        default=None,
        help="Process only this country slug (e.g. 'nigeria').",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="all_countries",
        help="Process ALL countries, not just African ones.",
    )
    args = parser.parse_args()

    if not COUNTRIES_DIR.exists():
        raise SystemExit(f"Missing directory: {COUNTRIES_DIR}")

    country_dirs = sorted(
        d
        for d in COUNTRIES_DIR.iterdir()
        if d.is_dir() and d.name != "_template" and d.name != "__pycache__"
    )

    if args.country:
        country_dirs = [d for d in country_dirs if d.name == args.country]
        if not country_dirs:
            raise SystemExit(f"Country slug '{args.country}' not found.")

    total_updated = 0
    total_sections_added = 0
    skipped_non_african = 0

    for cdir in country_dirs:
        index_path = cdir / "index.json"
        if not index_path.exists():
            continue

        data = json.loads(index_path.read_text(encoding="utf-8"))

        if not args.all_countries and not is_african(data):
            skipped_non_african += 1
            continue

        changes = populate_missing(data, dry_run=args.dry_run)

        if not changes:
            continue

        slug = data.get("_meta", {}).get("country_slug", cdir.name)
        label = "[DRY-RUN] " if args.dry_run else ""
        print(f"{label}{slug}:")
        for c in changes:
            print(c)

        total_updated += 1
        total_sections_added += len(changes)

        if not args.dry_run:
            index_path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    print(f"\n{'[DRY-RUN] ' if args.dry_run else ''}Summary:")
    print(f"  African countries updated : {total_updated}")
    print(f"  Sections injected         : {total_sections_added}")
    print(f"  Non-African countries skip : {skipped_non_african}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
