#!/usr/bin/env python3
"""Generate geo-registry/countries.json from docs/registry/iso3166_country_codes.md.

Design goals:
- Keep the base ISO list machine-generated and easy to refresh.
- Keep historical/exonym/endonym richness in countries_overrides.json.

Usage:
  python geo-registry/scripts/build_countries_json.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ISO_MD = ROOT / "docs" / "registry" / "iso3166_country_codes.md"
OUT = ROOT / "geo-registry" / "countries.json"


def slugify(text: str) -> str:
    t = (text or "").strip().lower()
    t = t.replace(" ", "-").replace("/", "-").replace("_", "-")
    t = re.sub(r"-+", "-", t)
    return t


def parse_iso_table(md_text: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if "---" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        country, code = parts[0], parts[1]
        if country == "Country Name" and code.startswith("ISO"):
            continue
        if not country or not code:
            continue
        rows.append((country, code))
    return rows


def main() -> int:
    md = ISO_MD.read_text(encoding="utf-8")
    rows = parse_iso_table(md)

    countries = []
    for country, iso_a2 in rows:
        countries.append(
            {
                "slug": slugify(country),
                "name": country,
                "kind": "country",
                "iso_alpha2": iso_a2,
                "status": "ACTIVE",
                "names": [
                    {
                        "name": country,
                        "lang": "en",
                        "script": "Latn",
                        "is_primary": True,
                        "is_official": True,
                    }
                ],
                "former_names": [],
            }
        )

    payload = {
        "_meta": {
            "description": "Generated from docs/registry/iso3166_country_codes.md",
            "last_updated": "2026-01-30",
            "count": len(countries),
        },
        "countries": countries,
    }

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(countries)} countries to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
