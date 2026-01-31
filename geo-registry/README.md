# Geo Registry

> **Canonical Source of Truth for Place Names**

This directory contains JSON registries for geographic entities with their names, aliases, and historical variants. These files drive the seeding of `Place` and `PlaceName` nodes in Neo4j.

---

## Directory Structure

```
geo-registry/
├── README.md                    # This file
├── places.json                  # ⭐ MAIN FILE: Countries + nested cities (human-readable)
├── places/                      # Optional: split-by-country view of places.json
│   └── countries/
│       └── united-kingdom/
│           ├── places.json             # Country Place entry (with nested cities)
│           ├── institutions.json       # Country-scoped nodes (curation)
│           ├── events.json
│           ├── artifacts.json
│           ├── texts.json
│           ├── ideas.json
│           ├── movements.json
│           ├── people.json
│           ├── evidence.json
│           ├── frameworks.json
│           └── timeframes.json
├── countries.json               # Generated list (196 from ISO registry doc)
├── countries_overrides.json     # Legacy overrides (being phased out)
├── cities_major.json            # Starter set of cities (being merged into places.json)
├── cities_historical.json       # Extinct/ancient cities
├── countries_historical.json    # Extinct countries (Prussia, USSR, etc.)
├── regions.json                 # Sub-national regions with disputed names
└── scripts/
    ├── build_countries_json.py  # Generates countries.json from ISO doc
    └── seed_from_registry.py    # Seeds Neo4j from registry JSONs
```

---

## Data Model

### Primary Format: `places.json` (Human-Readable)

Countries with nested cities, clean and easy to read/edit:

```json
{
  "israel": {
    "name": "Israel",
    "iso": "IL",
    "wikidata_id": "Q801",
    "names": [
      { "name": "Israel", "lang": "en", "is_primary": true },
      { "name": "יִשְׂרָאֵל", "lang": "he", "script": "Hebr", "is_endonym": true }
    ],
    "cities": {
      "jerusalem": {
        "name": "Jerusalem",
        "names": [
          { "name": "Jerusalem", "lang": "en", "is_primary": true },
          { "name": "יְרוּשָׁלַיִם", "lang": "he", "script": "Hebr", "is_endonym": true },
          { "name": "Jebus", "lang": "und", "startYear": -3000, "endYear": -1000 },
          { "name": "Aelia Capitolina", "lang": "la", "startYear": 135, "endYear": 638 }
        ]
      },
      "tel-aviv": { ... },
      "haifa": { ... }
    }
  }
}
```

### Neo4j Edges Created

| Relationship | Purpose |
|--------------|---------|
| `(:Place)-[:HAS_NAME {startYear, endYear, is_primary}]->(:PlaceName)` | Canonical, time-scoped (authoritative) |
| `(:Place)-[:ALSO_KNOWN_AS]->(:PlaceName)` | Visualization edge for Neo4j Browser |
| `Place.alt_names[]` | Denormalized array for search/autocomplete |

### Legacy Format: `countries.json` + `countries_overrides.json`

```json
{
  "slug": "germany",
  "name": "Germany",
  "iso_alpha2": "DE",
  "iso_alpha3": "DEU",
  "iso_numeric": "276",
  "wikidata_id": "Q183",
  "geonames_id": "2921044",
  "kind": "country",
  "status": "ACTIVE",
  "names": [
    {
      "name": "Deutschland",
      "lang": "de",
      "script": "Latn",
      "is_endonym": true,
      "is_official": true
    },
    {
      "name": "Germany",
      "lang": "en",
      "script": "Latn",
      "is_endonym": false,
      "is_official": true
    },
    {
      "name": "Allemagne",
      "lang": "fr",
      "script": "Latn"
    }
  ],
  "historical_names": [
    {
      "name": "West Germany",
      "formal_name": "Federal Republic of Germany",
      "startYear": 1949,
      "endYear": 1990,
      "note": "Cold War partition"
    }
  ]
}
```

### Neo4j Mapping

| JSON Field | Neo4j Property/Node |
|------------|---------------------|
| `slug` | `Place.slug` (immutable) |
| `name` | `Place.name` (current preferred) |
| `iso_alpha2` | `Place.iso` |
| `wikidata_id` | `Place.wikidata_id` |
| `names[].name` | `PlaceName.name` OR `Place.alt_names[]` |
| `historical_names[]` | `PlaceName` nodes with `startYear`/`endYear` |

---

## Conventions

### 1. Slug Rules

| Convention | Example | Rationale |
|------------|---------|-----------|
| Lowercase, hyphenated slug | `united-kingdom`, `sri-lanka` | URL-safe, queryable |
| Hyphens for spaces | `new-zealand` | Consistent |
| Use modern English name | `germany` not `deutschland` | Discoverability |
| Disambiguate with context | `georgia-country` vs `georgia-us-state` | Avoid collisions |

Note: the existing graph may contain non-ASCII slugs (e.g., `türkiye`). **Do not change slugs once created.** Prefer ASCII for new slugs, but treat `Place.slug` as immutable identity.

### 2. Name Priority (for `Place.name`)

1. **Current official endonym** (if Latin script): `Türkiye`, `Deutschland`
2. **UN official short name**: "Germany", "Japan"
3. **Common English exonym**: "China" (not Zhōngguó)

### 3. Language Codes

- Use **ISO 639-1** (2-letter): `en`, `de`, `fr`, `zh`, `ar`
- Fall back to **ISO 639-3** (3-letter) for ancient languages: `akk` (Akkadian), `grc` (Ancient Greek)

### 4. Script Codes

- Use **ISO 15924** (4-letter): `Latn`, `Cyrl`, `Arab`, `Hani`, `Hebr`

---

## Sources

| Source | Coverage | URL |
|--------|----------|-----|
| **GeoNames** | Modern places + alt names | https://www.geonames.org/ |
| **Wikidata** | Universal entity IDs | https://www.wikidata.org/ |
| **UN GEGN** | Official country names | https://unstats.un.org/unsd/geoinfo/UNGEGN/ |
| **ISO 3166-1** | Country codes | https://www.iso.org/iso-3166-country-codes.html |
| **Pleiades** | Ancient places | https://pleiades.stoa.org/ |

---

## Relationship to Other Files

| File | Purpose |
|------|---------|
| `geo_registry.py` | Seeds continent→region→country hierarchy (uses this data) |
| `docs/guidelines/geo_naming.md` | Naming conventions documentation |
| `docs/registry/iso3166_country_codes.md` | ISO code reference |
| `scripts/admin/seed_place_names_comprehensive.py` | Example PlaceName seeder |

---

## Contributing

1. **Adding a country:** Add entry to `countries.json` with all required fields
2. **Adding name variants:** Append to `names[]` array with `lang` and `script`
3. **Historical names:** Use `historical_names[]` with `startYear`/`endYear`
4. **Extinct places:** Use `status: "EXTINCT"` and `contained_in` for modern container

---

## Change Log

| Date | Change |
|------|--------|
| 2026-01-30 | Initial scaffolding; countries list is generated from ISO registry doc |
