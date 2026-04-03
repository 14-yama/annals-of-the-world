---
title: Wikidata Fetch Guide — Full Coverage Strategy
status: PUBLISHED
version: 1.0
summary: Step-by-step guide for fetching comprehensive datasets from Wikidata for any node class (People, Institutions, Places, etc.) using SPARQL. Documents proven strategies that yielded 238K+ people and 36K+ institutions.
---

# Wikidata Fetch Guide

Purpose: Document the proven methodology for fetching large, high-quality datasets from
Wikidata's SPARQL endpoint. This guide covers the patterns, pitfalls, and best practices
learned from the People (238,466 entities) and Institutions (36,738 entities) fetches.

## 1. Overview

| Class | Script | QIDs | Batches | Entities | File |
|-------|--------|------|---------|----------|------|
| 2 People | `scripts/fetch_wikidata_people.py` | 131 occupation QIDs | 40 | 238,466 | `data/wikidata_people.json` |
| 3 Institutions | `scripts/fetch_wikidata_institutions.py` | 213 type QIDs | 76 | 36,738 (cleaned) | `data/wikidata_institutions.json` |
| 4 Places | `scripts/fetch_wikidata_places.py` | 150+ type QIDs | 70+ | TBD | `data/wikidata_places.json` |

## 2. Architecture

Each fetch script follows a consistent pattern:

```
┌──────────────────┐     ┌───────────────┐     ┌──────────────┐
│ callNumbers.ts   │────▶│ TYPE_MAP dict  │────▶│ SPARQL Query │
│ (Class divisions)│     │ (QID→Division) │     │ per batch    │
└──────────────────┘     └───────────────┘     └──────┬───────┘
                                                       │
                                               ┌───────▼───────┐
                                               │ Wikidata SPARQL│
                                               │ endpoint       │
                                               └───────┬───────┘
                                                       │
                                               ┌───────▼───────┐
                                               │ Transform &   │
                                               │ Deduplicate   │
                                               └───────┬───────┘
                                                       │
                                               ┌───────▼───────┐
                                               │ data/*.json   │
                                               └───────────────┘
```

## 3. Key Components

### 3.1 Type QID Mapping

Map Wikidata `P31` (instance-of) QIDs to callNumber divisions:

```python
INSTITUTION_TYPE_MAP = {
    "Q3918":  ("381", "Universities & Colleges"),
    "Q33506": ("361", "Museums & Galleries"),
    "Q7278":  ("316", "Political Parties & Organizations"),
    # ...
}
```

**How to find QIDs:**
1. Go to `https://www.wikidata.org/wiki/Q<QID>` for any entity
2. Look at the `P31` (instance of) claim for type QIDs
3. Use Wikidata Query Service to explore subtypes: `SELECT ?type ?typeLabel WHERE { ?type wdt:P279* wd:Q<parent> . }`
4. Target **specific** types, not broad ones like Q43229 (organization) — too many false positives

### 3.2 Batch Strategy

Split queries into granular batches to avoid Wikidata's 60-second timeout:

```python
QUERIES = {
    "330_bank":     (["Q22687"], 15),        # 1 heavy QID, high sitelinks
    "341_church_a": (["Q16970"], 5),          # 1 frequent QID, low sitelinks
    "350_research": (["Q31855", "Q1298668", "Q3354859", "Q1365560"], 5),  # 4 light QIDs
}
```

**Rules of thumb:**
- Heavy types (>5000 Wikidata results): Solo batch + higher `min_sitelinks` (10–20)
- Medium types (1000–5000): 1–3 QIDs per batch
- Light types (<1000): 3–6 QIDs per batch
- Always use adaptive limit fallback

### 3.3 Adaptive Limit Fallback

When a batch times out, halve the SPARQL LIMIT until it succeeds:

```python
def fetch_adaptive(type_qids, target_limit, min_sl):
    limits = [target_limit]
    lim = target_limit
    while lim > 500:
        lim = lim // 2
        limits.append(lim)
    limits.append(500)
    for lim in limits:
        rows = fetch_sparql(build_query(type_qids, limit=lim, min_sitelinks=min_sl))
        if rows:
            return rows
    return []
```

### 3.4 Sitelinks Threshold

The `sitelinks` count (number of Wikipedia language editions) is the primary quality/notability filter:

| Sitelinks | Quality | Use For |
|-----------|---------|---------|
| > 5 | Standard | Most types — good balance of coverage and quality |
| > 8 | Medium | Broad types with many entries (newspapers, magazines) |
| > 10–15 | Strict | Very broad types (political parties, banks, schools) |
| > 20 | Very strict | Extremely broad types that return 10K+ results (buildings, organizations) |

**People script:** Used `sitelinks > 5` across all 131 QIDs → 238,466 entities.

### 3.5 SPARQL Query Template

Standard query structure used by all fetch scripts:

```sparql
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception ?dissolved
       ?country ?countryLabel
       ?headquartersLabel ?founderLabel
       ?image ?article ?sitelinks
WHERE {
  VALUES ?type { wd:Q3918 wd:Q875538 }
  ?item wdt:P31 ?type .
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > 5)

  OPTIONAL { ?item wdt:P571 ?inception . }
  OPTIONAL { ?item wdt:P576 ?dissolved . }
  OPTIONAL { ?item wdt:P17  ?country . }
  OPTIONAL { ?item wdt:P159 ?headquarters . }
  OPTIONAL { ?item wdt:P112 ?founder . }
  OPTIONAL { ?item wdt:P18  ?image . }
  OPTIONAL {
    ?article schema:about ?item ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
}
ORDER BY DESC(?sitelinks)
LIMIT 5000
```

**Key properties by class:**
- People: `P106` (occupation), `P21` (gender), `P569/P570` (birth/death)
- Institutions: `P571/P576` (inception/dissolved), `P17` (country), `P159` (HQ), `P112` (founder)
- Places: `P625` (coordinates), `P1082` (population), `P17` (country), `P131` (admin region)

## 4. Entity Quality Requirements

Every entity in the output JSON must have:

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Lowercase kebab-case identifier, max 80 chars |
| `name` | ✅ | Human-readable entity name |
| `label` | ✅ | Node type: "Person", "Institution", "Place" |
| `callNumber` | ✅ | Format: `{divisionCode}.{slug}` |
| `summary` | ✅ | Descriptive overview (not a placeholder) |
| `era` | ✅ | One of: Prehistoric, Classical, Medieval, Early Modern, Modern, Contemporary |
| `divisionCode` | ✅ | 3-digit code from callNumbers.ts |
| `divisionHeading` | ✅ | Human-readable division name |
| `historicalSignificance` | ✅ | Object: `{score: 1-10, label: "Minor"/"Moderate"/"Notable"/"Major"/"Landmark", sitelinks: N}` |
| `inAppwrite` | ✅ | Boolean — false for bulk Wikidata entities, true when seeded to backend |
| `subjects` | ✅ | Array of topic tags (country, type, continent, division) |
| `frameworks` | ✅ | At least 1 interpretive framework |

### Historical Significance Scoring

```
Sitelinks ≥ 150 → Score 8 (base)
Sitelinks ≥ 100 → Score 7
Sitelinks ≥ 70  → Score 6
Sitelinks ≥ 50  → Score 5
Sitelinks ≥ 35  → Score 4
Sitelinks ≥ 20  → Score 3
Sitelinks ≥ 12  → Score 2
Sitelinks < 12  → Score 1

Bonuses:
  Founded before 1000 BCE → +2
  Founded before 500 CE   → +1
  Still active (not dissolved) → +1

Labels:
  9-10 → Landmark (world-shaping)
  7-8  → Major (globally recognized)
  5-6  → Notable (regionally important)
  3-4  → Moderate (nationally significant)
  1-2  → Minor (documented but limited impact)
```

### `inAppwrite` Flag

- **`false`** — Bulk Wikidata entity, not yet seeded to Appwrite backend
- **`true`** — Entity has been imported to the Appwrite backend for API access
- Use `historicalSignificance.score ≥ 7` to prioritize entities for Appwrite seeding

## 5. Post-Fetch Cleanup

After fetching, always run a cleanup pass to:

1. **Remove non-target entities** — Wikidata type hierarchies can return unexpected subtypes
   (e.g., fetching "Q43229 organization" returns football clubs)
2. **Reclassify misassigned divisions** — Some QIDs map to wrong divisions due to Wikidata
   subtype inheritance
3. **Deduplicate by slug** — First-occurrence wins

Example cleanup types for Institutions:
```python
REMOVE_TYPES = {
    'association football club', 'television series', 'county seat',
    'sovereign state', 'park', 'cemetery', 'historical period',
    'monument', 'sports club', 'record label', 'criminal organization',
}
```

## 6. Common Pitfalls

| Problem | Cause | Solution |
|---------|-------|----------|
| SPARQL timeout (504) | Query returns too many rows | Split into smaller batches; raise sitelinks threshold; use adaptive limit |
| JSON parse error | Malformed response from large result | Add retry with smaller LIMIT |
| Rate limiting (429) | Too many requests in short time | Add 2s delay between batches; exponential backoff on 429 |
| Duplicate entities | Same entity matched by multiple type QIDs | Deduplicate by slug (first-occurrence wins) |
| Non-target entities | Broad Wikidata types capture unrelated items | Use specific QIDs; post-fetch cleanup removes bad types |
| Missing labels | Entity name resolves to QID string | Filter out entities where name matches `^Q\d+$` |
| Wrong division | QID inheritance captured subtypes | Post-fetch reclassification pass |

## 7. Running a Fetch

### Standard run (5000 limit per batch):
```bash
cd /path/to/annals-of-the-world
source .venv/bin/activate
python3 scripts/fetch_wikidata_<class>.py --limit 5000
```

### Dry run (validate batch configuration without queries):
```bash
python3 scripts/fetch_wikidata_<class>.py --dry-run
```

### Custom output path:
```bash
python3 scripts/fetch_wikidata_<class>.py --output data/wikidata_places_v2.json
```

### Expected runtime:
- People (40 batches): ~15-25 minutes
- Institutions (76 batches): ~30-45 minutes
- Places (70+ batches): ~25-40 minutes

## 8. Output JSON Structure

```json
{
  "_meta": {
    "source": "Wikidata SPARQL (query.wikidata.org)",
    "generated": "2026-04-02T...",
    "version": "2.0",
    "total_raw_results": 68503,
    "total_unique_entities": 36738,
    "label": "Institution",
    "classCode": 3,
    "division_counts": { "310": 316, "311": 163, ... },
    "era_counts": { "Classical": 14550, "Modern": 12928, ... },
    "significance_distribution": { "Landmark": 19, "Major": 336, ... },
    "continent_counts": { "Europe": 21330, "Asia": 9022, ... }
  },
  "entities": [
    {
      "slug": "university-of-oxford",
      "name": "University of Oxford",
      "label": "Institution",
      "callNumber": "381.university-of-oxford",
      "divisionCode": "381",
      "divisionHeading": "Universities & Colleges",
      "summary": "...",
      "era": "Medieval",
      "historicalSignificance": { "score": 9, "label": "Landmark", "sitelinks": 195 },
      "inAppwrite": false,
      ...
    }
  ]
}
```

## 9. Adding a New Class Fetch

To create a fetch script for a new class:

1. **Map divisions to QIDs:** Review `ui/src/constants/callNumbers.ts` for all divisions in the class
2. **Find Wikidata QIDs:** Use Wikidata Query Service to identify type QIDs for each division
3. **Copy the template:** Use `fetch_wikidata_institutions.py` as the base template
4. **Adapt the SPARQL:** Change properties to match the class (e.g., coordinates for Places)
5. **Split heavy types:** Any QID expected to return >3000 results should be a solo batch
6. **Test with dry run:** `python3 scripts/fetch_wikidata_<class>.py --dry-run`
7. **Run and clean:** Fetch, then run cleanup to remove non-target entities
8. **Update this guide:** Add the new class to the overview table in Section 1

## 10. Integration with Catalog

Fetched Wikidata data integrates with the Annals Catalog pipeline:

1. Fetch script writes to `data/wikidata_<class>.json`
2. Catalog converter reads the JSON and maps to `Entity` interface
3. Deduplication: hand-curated catalog entities win over auto-generated Wikidata entities
4. Entities appear in `ALL_CATALOG_ENTITIES` via `ui/src/data/catalog/index.ts`

See: [Call Number Classification](./classification.md) | [Catalog Architecture](../../.github/instructions/project-guidelines.instructions.md)
