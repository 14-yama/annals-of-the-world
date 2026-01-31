# Place Name Variants (Endonym, Exonym, Historical)

> **Last updated:** 2026-01-30

This document defines how to represent *all name variants* for a `:Place` node, including native endonyms, foreign-language exonyms, and historical names that resulted from regime change, conquest, or decolonization.

For broader context, see [docs/guidelines/geo_naming.md](../guidelines/geo_naming.md).

---

## Core Model

**Stable identity:** the physical location (`:Place`) never changes.

**Name variants:** stored as time-scoped `:PlaceName` nodes connected via `PREVIOUSLY_KNOWN_AS`.

Authoritative structure:

- `(:Place)-[:PREVIOUSLY_KNOWN_AS {startYear, endYear, is_primary, change_reason}]->(:PlaceName)`

**Derived readability edges** (optional):

- `(:Place)-[:ENDONYM]->(:PlaceName)` — current native/local name(s)
- `(:Place)-[:EXONYM]->(:PlaceName)` — current foreign-language name(s)
- `(:Place)-[:PREVIOUSLY_KNOWN_AS]->(:PlaceName)` — historical names (no longer current)

These derived edges are **not authoritative**; they are computed from `PREVIOUSLY_KNOWN_AS` using the rules below.

---

## Variant Categories

### 1. Endonyms (native/local)

**Definition:** the name used locally, in the local language/script.

**Rule:** `is_endonym: true` and a **current** validity window (no `endYear`, or `endYear` >= present year).

### 2. Exonyms (other languages)

**Definition:** names used by other languages for the same place (e.g., Germany/Allemagne).

**Rule:** `is_endonym: false` and a **current** validity window.

### 3. Previously Known As (historical)

**Definition:** names used in the past due to regime change, conquest, decolonization, or official renaming.

**Rule:** `endYear` is in the past (or the `PlaceName` is explicitly marked historical via `note`), regardless of `is_endonym`.

---

## PlaceName Fields (JSON + Graph)

Each `PlaceName` record should include:

- `name` — the name string
- `lang` — ISO 639-1/639-3 language code
- `script` — ISO 15924 script code
- `is_endonym` — boolean
- `startYear`, `endYear` — approximate validity window (optional)
- `note` — short provenance note (optional)

**Primary display name:**

Use `is_primary: true` only for the preferred **current** display name (usually an endonym if Latin script; otherwise a widely used exonym).

---

## Derived Edge Rules (Summary)

| Edge | Selection Rule | Purpose |
|------|----------------|---------|
| `ENDONYM` | `is_endonym: true` and current | Native/local current names |
| `EXONYM` | `is_endonym: false` and current | Foreign-language current names |
| `PREVIOUSLY_KNOWN_AS` | `endYear` in the past | Historical names |

> If a name is historical **and** endonym/exonym, prefer `PREVIOUSLY_KNOWN_AS` as the readability edge, while preserving `is_endonym` on the `PlaceName` node.

---

## JSON Structure (places.json)

Each place entry should use this pattern:

- `name` — current preferred display name
- `names[]` — current names in multiple languages/scripts
- `former_names[]` — historical names with `endYear`

Example (conceptual):

- `names[]` → endonyms and current exonyms
- `former_names[]` → historical names only

> Keep the JSON human-readable and nested (countries → cities), as documented in [geo-registry/README.md](../../geo-registry/README.md).

---

## Notes

- `Place.alt_names[]` remains a **denormalized** search aid and can include *all* known labels (endonym, exonym, romanizations, historical).
- The graph structure (`PREVIOUSLY_KNOWN_AS`) is the authoritative source of truth.
- Derived readability edges are optional and should be regenerated when name data changes.
