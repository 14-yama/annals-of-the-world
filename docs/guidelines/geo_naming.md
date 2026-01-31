# Geographic Naming Conventions

> **Last updated:** 2026-01-30

This document defines how the Annals project handles place names that change over time, ensuring historical accuracy while maintaining queryability.

---

## Core Principle

**The physical location is the stable identity; names are time-scoped attributes.**

A place node represents a *geographic site* (coordinates, physical area), not a political entity or a name. Names are metadata that change; the place itself persists.

In practice we use two layers:

1. **Denormalized labels** on `:Place` for search and UI: `Place.alt_names[]` (SKOS `altLabel` style)
2. **Canonical, time-scoped names** as graph structure: `(:Place)-[:PREVIOUSLY_KNOWN_AS]->(:PlaceName)`

---

## Schema Design

### Place Node (stable identity)

```cypher
(:Place {
  slug: "jerusalem",           // Immutable identifier (never changes)
  name: "Jerusalem",           // Current/preferred display name
  kind: "city",                // city | region | site | feature
  lat: 31.7683,                // Geographic coordinates (stable)
  lon: 35.2137,
  wikidata_id: "Q1218",        // External stable identifiers
  geonames_id: "281184",
  pleiades_id: "687928",       // For ancient places
  is_generic: true,
  // ... other properties
})
```

### PlaceName Node (time-scoped variants)

```cypher
(:PlaceName {
  name: "Jebus",
  slug: "jebus",               // Unique per name variant
  lang: "he",                  // ISO 639-1 language code
  script: "Latn",              // ISO 15924 script code
  is_endonym: true,            // Native name vs exonym
  is_official: false,          // Current official status
  startYear: -3000,            // Approximate validity range
  endYear: -1000,
  source_note: "Pre-Davidic Canaanite name",
  evidence_url: "https://...",
  created_at: "2026-01-24T...",
})
```

### Relationship Pattern

```cypher
(:Place)-[:PREVIOUSLY_KNOWN_AS {startYear, endYear, is_primary, change_reason}]->(:PlaceName)
```

We use a **single authoritative edge** for time-scoped naming history. The relationship properties determine both *time* and *reason* for the name variant.

Semantics:
- **PREVIOUSLY_KNOWN_AS** — the place used this name during a specific period. `endYear` in the past indicates a historical name; `endYear: null` indicates a current name.
- **change_reason** — why the name changed (optional for current names).
  - `CONQUEST_OR_POLITICAL_TAKEOVER`
  - `REGIME_OR_SYSTEM_CHANGE`
  - `DECOLONIZATION_OR_INDEPENDENCE`
  - `STANDARDIZATION_OR_LANGUAGE_POLICY`
  - `ADMINISTRATIVE_REFORM`
  - `OTHER`

We also **optionally materialize** readability edges for endonyms/exonyms (derived from `PREVIOUSLY_KNOWN_AS`):

```cypher
(:Place)-[:ENDONYM]->(:PlaceName)
(:Place)-[:EXONYM]->(:PlaceName)
```

These are for UI/readability only.

**Important (Neo4j constraint):** do not `MERGE` a relationship using a property map that might contain `null` (e.g., `endYear: null`). Neo4j will error.

Use `MERGE` for the relationship shape, then `SET` properties (setting a property to `null` via `SET` removes it, which is allowed):

```cypher
MERGE (p:Place {slug: $place_slug})
MERGE (n:PlaceName {slug: $name_slug})
MERGE (p)-[r:HAS_NAME]->(n)
SET r.startYear = n.startYear,
    r.endYear   = n.endYear,
    r.is_primary = coalesce(r.is_primary, false)
```

---

## Naming Change Categories

### 1. Conquest / Political Takeover

The most common historical case: a place is conquered and renamed by the new rulers.

| Place | Previous Name | New Name | Year | Event |
|-------|---------------|----------|------|-------|
| Jerusalem | Jebus | Jerusalem | c. 1000 BCE | David's conquest |
| Jerusalem | Jerusalem | Aelia Capitolina | 135 CE | Hadrian's renaming |
| Jerusalem | Aelia Capitolina | Jerusalem | 638 CE | Islamic conquest (restored) |
| Istanbul | Byzantium | Constantinople | 330 CE | Constantine's refounding |
| Istanbul | Constantinople | Istanbul | 1930 | Turkish Republic official change |

**Modeling:**
```cypher
// The place
CREATE (p:Place {slug: "jerusalem", name: "Jerusalem", kind: "city"})

// Name variants
CREATE (n1:PlaceName {name: "Jebus", lang: "he"})
CREATE (n2:PlaceName {name: "Jerusalem", lang: "he"})
CREATE (n3:PlaceName {name: "Aelia Capitolina", lang: "la"})
CREATE (n4:PlaceName {name: "Jerusalem", lang: "en"})

// Link them (single authoritative edge)
CREATE (p)-[:PREVIOUSLY_KNOWN_AS {startYear: -3000, endYear: -1000, change_reason: "CONQUEST_OR_POLITICAL_TAKEOVER"}]->(n1)
CREATE (p)-[:PREVIOUSLY_KNOWN_AS {startYear: -1000, endYear: 135, change_reason: "CONQUEST_OR_POLITICAL_TAKEOVER"}]->(n2)
CREATE (p)-[:PREVIOUSLY_KNOWN_AS {startYear: 135, endYear: 638, change_reason: "CONQUEST_OR_POLITICAL_TAKEOVER"}]->(n3)
CREATE (p)-[:PREVIOUSLY_KNOWN_AS {startYear: 638, endYear: null, is_primary: true}]->(n4)
```

### 2. Regime / Political System Change

Name changes due to political ideology, not conquest.

| Place | Previous Name | New Name | Year | Regime |
|-------|---------------|----------|------|--------|
| St. Petersburg | Sankt-Peterburg | Petrograd | 1914 | WWI anti-German sentiment |
| Petrograd | Petrograd | Leningrad | 1924 | Soviet era |
| Leningrad | Leningrad | Sankt-Peterburg | 1991 | Post-Soviet restoration |
| Saigon | Saigon | Ho Chi Minh City | 1976 | Communist Vietnam |
| Stalingrad | Stalingrad | Volgograd | 1961 | De-Stalinization |

### 3. Decolonization / Independence

Former colonial names replaced with indigenous or nationalist names.

| Place | Colonial Name | Current Name | Year | Context |
|-------|---------------|--------------|------|---------|
| Mumbai | Bombay | Mumbai | 1995 | Marathi restoration |
| Chennai | Madras | Chennai | 1996 | Tamil restoration |
| Kolkata | Calcutta | Kolkata | 2001 | Bengali restoration |
| Sri Lanka | Ceylon | Sri Lanka | 1972 | Independence naming |
| Zimbabwe | Rhodesia | Zimbabwe | 1980 | Independence |
| Türkiye | Turkey | Türkiye | 2022 | Endonym adoption by UN |
| Iran | Persia | Iran | 1935 | Official name change |

### 4. Exonyms vs Endonyms

Different names used by locals vs foreigners for the same place.

| Endonym | Exonym(s) | Language |
|---------|-----------|----------|
| Deutschland | Germany (en), Allemagne (fr), Alemania (es) | de |
| 日本 (Nihon/Nippon) | Japan | ja |
| Ελλάδα (Elláda) | Greece | el |
| 中国 (Zhōngguó) | China | zh |
| Suomi | Finland | fi |
| Magyarország | Hungary | hu |

**Convention:** Store both; mark `is_endonym: true/false`. Prefer endonyms for `Place.name` where practical.

### 5. Script / Transliteration Variants

Same name, different writing systems or romanization standards.

| Place | Variants |
|-------|----------|
| Beijing | 北京, Peking, Peiping, Beijing |
| Moscow | Москва, Moskva, Moscow |
| Kyiv | Київ, Kiev, Kyiv |
| Mecca | مكة, Makkah, Mecca |

**Convention:** Store the native script as primary; store romanizations with `script` field.

### 6. Extinct / Ancient Places

Places that no longer exist as settlements but have historical significance.

| Ancient Name | Modern Location | Status |
|--------------|-----------------|--------|
| Babylon | near Hillah, Iraq | ruins/archaeological site |
| Troy | Hisarlik, Türkiye | ruins |
| Carthage | suburb of Tunis, Tunisia | ruins |
| Pompeii | near Naples, Italy | ruins |
| Ur | Tell el-Muqayyar, Iraq | ruins |
| Nineveh | near Mosul, Iraq | ruins |

**Modeling:**
```cypher
CREATE (p:Place {
  slug: "babylon",
  name: "Babylon",
  kind: "site",              // "site" for ruins/archaeological
  status: "EXTINCT",
  lat: 32.5355,
  lon: 44.4275,
  pleiades_id: "893951"
})

// Link to modern container for geographic queries
CREATE (p)-[:LOCATED_IN]->(:Place {slug: "iraq"})
```

### 7. Border Changes (Place Stays, Country Changes)

The place doesn't move, but sovereignty changes.

| Place | Historical Sovereignty | Modern Country |
|-------|----------------------|----------------|
| Alsace | France ↔ Germany (multiple times) | France |
| Kaliningrad | Prussia → Germany → USSR → Russia | Russia |
| Lviv | Poland → Austria → Poland → USSR → Ukraine | Ukraine |
| Gdańsk | Danzig (free city) → Germany → Poland | Poland |

**Convention:** Model sovereignty separately:
```cypher
(:Place {slug: "alsace"})-[:GOVERNED_BY {startYear: 1871, endYear: 1918}]->(:Polity {slug: "german-empire"})
(:Place {slug: "alsace"})-[:GOVERNED_BY {startYear: 1918, endYear: null}]->(:Polity {slug: "france"})
```

### 8. City Mergers / Administrative Changes

Multiple settlements merge into one, or a city's boundaries expand significantly.

| Result | Components | Year |
|--------|------------|------|
| Greater London | City of London + boroughs | 1965 |
| Tokyo | Edo renamed + expansion | 1868+ |
| New York City | Manhattan + 4 boroughs | 1898 |

**Convention:** Create separate nodes if historically significant; link with `MERGED_INTO` or `PART_OF`.

---

## Standardization Rules

### Slug Conventions

| Rule | Example | Rationale |
|------|---------|-----------|
| Use most common modern English name | `jerusalem`, `istanbul` | Discoverability |
| Lowercase, hyphens for spaces | `new-york-city` | URL-safe, consistent |
| Add disambiguation suffix if needed | `alexandria-egypt` vs `alexandria-virginia` | Avoid collisions |
| Never change slug once created | — | Referential integrity |

### Name Selection for `Place.name`

| Priority | Criteria |
|----------|----------|
| 1 | Current official endonym (if Latin script) |
| 2 | Current official English exonym |
| 3 | Most widely recognized English name |
| 4 | Transliteration of official endonym |

### Required External IDs (when available)

| ID Type | Use Case | Registry |
|---------|----------|----------|
| `wikidata_id` | All places | Q-numbers, universal |
| `geonames_id` | Modern places | Numeric, good geocoding |
| `pleiades_id` | Ancient/classical places | Authoritative for antiquity |
| `iso_a2`, `iso_a3` | Countries only | ISO 3166-1 |

---

## Query Patterns

### Find a place by any historical name

```cypher
// "What events happened in Constantinople?"
MATCH (pn:PlaceName {name: "Constantinople"})<-[:HAS_NAME]-(p:Place)
MATCH (e:Event)-[:OCCURS_IN]->(p)
RETURN e.name, e.startYear

You can also do fast fuzzy lookups via `Place.alt_names[]`:

```cypher
MATCH (p:Place)
WHERE $q IN coalesce(p.alt_names, [])
RETURN p.slug, p.name
```
```

### Find all names a place has had

```cypher
// "What was Jerusalem called throughout history?"
MATCH (p:Place {slug: "jerusalem"})-[:HAS_NAME]->(pn:PlaceName)
RETURN pn.name, pn.startYear, pn.endYear, pn.lang
ORDER BY pn.startYear
```

### Find the name valid at a specific time

```cypher
// "What was Istanbul called in 500 CE?"
MATCH (p:Place {slug: "istanbul"})-[:HAS_NAME]->(pn:PlaceName)
WHERE pn.startYear <= 500 AND (pn.endYear IS NULL OR pn.endYear > 500)
RETURN pn.name
// Returns: "Constantinople"
```

### Events at a place during a specific name era

```cypher
// "Events in Jerusalem while it was called Aelia Capitolina"
MATCH (p:Place {slug: "jerusalem"})-[:HAS_NAME]->(pn:PlaceName {name: "Aelia Capitolina"})
MATCH (e:Event)-[:OCCURS_IN]->(p)
WHERE e.startYear >= pn.startYear AND e.startYear < pn.endYear
RETURN e.name, e.startYear
```

---

## Migration Path

### Phase 1: Current State (now)
- `Place.name` holds current/preferred name
- No `PlaceName` nodes yet
- Modern geo registry uses ISO names

### Phase 2: Add PlaceName Support (when needed)
- Create `PlaceName` nodes for places with historical name changes
- Add `HAS_NAME` edges
- Keep `Place.name` as the "current preferred" for backward compatibility

### Phase 3: Polity Layer (future)
- Add `(:Polity)` nodes for time-scoped political entities
- Add `GOVERNED_BY` edges for sovereignty tracking
- Enables queries like "events in Prussian territory"

---

## Examples for English Reformation Cluster

Current places that may need name variants in future:

| Current Node | Historical Consideration |
|--------------|-------------------------|
| `england` | Kingdom of England (pre-1707) vs England (geographic region) |
| `rome` | Roma (Latin), multiple historical periods |
| `antwerp` | Antwerpen (Dutch), Anvers (French) |
| `westminster` | Part of London vs separate city (historical) |

For now, these are fine as-is. Add `PlaceName` nodes when:
1. An event references the place by a historical name
2. A query needs time-scoped name resolution
3. Disambiguation is needed for scholarly accuracy

---

## References

- [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) — Country codes
- [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) — Language codes
- [ISO 15924](https://unicode.org/iso15924/) — Script codes
- [GeoNames](https://www.geonames.org/) — Modern geographic database
- [Pleiades](https://pleiades.stoa.org/) — Ancient place gazetteer
- [Wikidata](https://www.wikidata.org/) — Universal entity identifiers

---

## Summary

| Principle | Implementation |
|-----------|----------------|
| Stable identity | `Place.slug` never changes |
| Time-scoped names | `(:Place)-[:HAS_NAME]->(:PlaceName)` |
| External IDs | `wikidata_id`, `geonames_id`, `pleiades_id` |
| Geography ≠ Sovereignty | Separate `GOVERNED_BY` edges for polities |
| Modern registry for convenience | Keep ISO countries for broad queries |
| Add detail incrementally | Start simple, add PlaceName when needed |
