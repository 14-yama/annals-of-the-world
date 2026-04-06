# Slug Naming Convention — Annals of the World

> **Authoritative Reference** for all entity slugs in the knowledge graph.
> Every slug in `data/`, `ui/src/data/catalog/`, and Neo4j MUST follow these rules.

---

## 1. Core Rules

| Rule | Example | Anti-pattern |
|------|---------|--------------|
| **Kebab-case only** (`a-z`, `0-9`, `-`) | `council-of-trent` | `Council_of_Trent`, `councilOfTrent` |
| **Lowercase** | `magna-carta` | `Magna-Carta` |
| **No consecutive hyphens** | `al-khwarizmi` | `al--khwarizmi` |
| **No leading/trailing hyphens** | `bronze-age` | `-bronze-age-` |
| **No special characters** (em-dash, apostrophes, parentheses removed) | `shatt-al-arab-clashes-1974` | `1974–75-shatt-al-arab-clashes` |
| **Max 80 characters** (soft limit) | — | Truncation at 50 creates broken slugs |
| **Globally unique per label** | One `julius-caesar` among all Person entities | Duplicate slugs within same label |

---

## 2. Prefix Conventions

Certain entity types use a **standard prefix** to prevent collisions across labels:

| Prefix | Used For | Example |
|--------|----------|---------|
| `country-` | Country entities (Places class 430) | `country-egypt`, `country-japan` |
| `city-` | City entities (Places class 440) | `city-jerusalem`, `city-rome` |
| `empire-` | Empire/dynasty entities (class 450) | `empire-roman`, `empire-ottoman` |
| `era-` | Timeframe entities (class 9xx) | `era-archaic-period`, `era-hellenistic-period` |
| `field-` | Division/classification entities | `field-250` → **DEPRECATED** (use `division-religious-figures`) |
| `movement-` | Movement entities only when needed to disambiguate | `movement-romanticism` |

### Prefixes NOT Used

| ❌ Never Prefix | Why |
|-----------------|-----|
| `wikipedia-` | Only for `texts[].slug` references, never for entity slugs |
| `wikidata-` | QID goes in `wikidataQid` field, not slug |
| `category-` | Use the label field instead |

---

## 3. Date Handling in Slugs

Dates appear in slugs only when they **disambiguate** otherwise identical names.

| Pattern | Example | When to Use |
|---------|---------|-------------|
| Name first, year last | `treaty-of-paris-1763` | Multiple treaties of Paris |
| Year range with single hyphen | `shatt-al-arab-clashes-1974-75` | Multi-year events |
| BCE suffix | `battle-of-kadesh-1274-bce` | Ancient events needing disambiguation |
| No date | `industrial-revolution` | Uniquely identifiable without date |

### Date Anti-patterns

| ❌ Wrong | ✅ Correct | Issue |
|----------|-----------|-------|
| `197475-shatt-al-arab-clashes` | `shatt-al-arab-clashes-1974-75` | Em-dash stripped; digits merged; date should be suffix |
| `19871989-tibetan-unrest` | `tibetan-unrest-1987-89` | Same issue |
| `1904-wikipedia-japan-korea` | `japan-korea-agreement-1904` | Wikipedia prefix; date as prefix |

---

## 4. Entity-Specific Slug Patterns

### People (Class 2)

```
{first-name}-{last-name}
```

- Use the most commonly known form: `isaac-newton` not `sir-isaac-newton`
- Parenthetical disambiguation stripped, use context: `alexander-the-great`
- Monarchs: `henry-viii`, `louis-xiv`, `cleopatra-vii`
- Eastern name order kept if conventional: `mao-zedong`, `sun-yat-sen`

### Institutions (Class 3)

```
{institution-name}
```

- Drop generic words when unambiguous: `oxford-university` not `university-of-oxford`
- Use common short forms: `un-security-council` not `united-nations-security-council`

### Places (Class 4)

```
country-{name}     (countries)
city-{name}        (cities)
empire-{name}      (empires/dynasties)
region-{name}      (geo regions, optional prefix)
```

- Modern country names preferred: `country-iran` not `country-persia`
- Historical names as separate entities: `empire-persian` for the Achaemenid state

### Events (Class 5)

```
{event-name}[-{year}]
```

- Year only when needed: `french-revolution` (unique), `treaty-of-paris-1763` (not unique)
- War names: `world-war-i`, `hundred-years-war`
- Battles: `battle-of-thermopylae`, `siege-of-constantinople-1453`

### Ideas (Class 0–1)

```
{idea-name}
```

- Philosophical schools: `stoicism`, `confucianism`, `utilitarianism`
- Political systems: `democracy`, `constitutional-monarchy`
- Scientific: `heliocentric-model`, `germ-theory`

### Movements (Class 6)

```
{movement-name}
```

- `protestant-reformation`, `civil-rights-movement`
- Use `movement-` prefix only to disambiguate from an Idea with same name

### Artifacts & Texts (Class 7)

```
{text-name}
```

- `code-of-hammurabi`, `magna-carta`, `origin-of-species`
- `rosetta-stone`, `dead-sea-scrolls`

### Evidence (Class 8)

```
{evidence-name}
```

- `pompeii-excavation`, `carbon-14-dating`

### Timeframes (Class 9)

```
era-{period-name}
```

- `era-archaic-period`, `era-hellenistic-period`, `era-roman-period`
- `era-industrial-age`, `era-cold-war`
- Parent eras: `era-classical`, `era-medieval`, `era-modern`

---

## 5. Slug Generation Algorithm

```python
import re

def slugify(name: str) -> str:
    """Generate a canonical slug from a display name."""
    s = name.lower().strip()
    # Replace em-dash, en-dash with hyphen
    s = s.replace("–", "-").replace("—", "-")
    # Remove parentheticals
    s = re.sub(r"\s*\([^)]*\)\s*", " ", s)
    # Remove non-alphanumeric (keep hyphens and spaces)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    # Collapse whitespace to hyphen
    s = re.sub(r"[\s_]+", "-", s)
    # Collapse multiple hyphens
    s = re.sub(r"-+", "-", s)
    # Strip leading/trailing hyphens
    s = s.strip("-")
    return s[:80]  # Soft limit
```

---

## 6. Relationship Target Slugs

Every `targetSlug` in a `relationships[]` entry MUST point to a real entity that
exists somewhere in the dataset. **No phantom slugs.**

### Allowed Relationship Target Types

| Target Type | Slug Pattern | Lives In |
|-------------|-------------|----------|
| Timeframe / Era | `era-{period-name}` | `wikidata_timeframes.json` |
| Country | `country-{name}` | `wikidata_places_part*.json` |
| City | `city-{name}` | `wikidata_places_part*.json` |
| Division / Field | `division-{heading}` | Same JSON as source (or cross-file) |
| Person / Idea / … | `{slug}` | Respective label's JSON file |

### Relationship Verbs for OCCURS_DURING

The `OCCURS_DURING` verb MUST target a **Timeframe entity** whose slug matches
a division from Class 9 (Timeframes) in `callNumbers.ts`:

| Division | Heading | Target Slug |
|----------|---------|-------------|
| 910 | Prehistoric | `era-prehistoric` |
| 911 | Paleolithic & Mesolithic | `era-paleolithic-mesolithic` |
| 912 | Neolithic & Chalcolithic | `era-neolithic-chalcolithic` |
| 913 | Bronze Age | `era-bronze-age` |
| 920 | Classical | `era-classical` |
| 921 | Archaic Period | `era-archaic-period` |
| 922 | Hellenistic Period | `era-hellenistic-period` |
| 923 | Roman Period | `era-roman-period` |
| 924 | Late Antiquity | `era-late-antiquity` |
| 930 | Medieval | `era-medieval` |
| 931 | Early Medieval / Dark Ages | `era-early-medieval` |
| 932 | High Medieval | `era-high-medieval` |
| 933 | Late Medieval | `era-late-medieval` |
| 940 | Early Modern | `era-early-modern` |
| 941 | Age of Exploration | `era-age-of-exploration` |
| 942 | Renaissance Period | `era-renaissance-period` |
| 943 | Reformation Era | `era-reformation-era` |
| 944 | Age of Enlightenment | `era-age-of-enlightenment` |
| 950 | Modern | `era-modern` |
| 951 | Industrial Age | `era-industrial-age` |
| 952 | Age of Empire / New Imperialism | `era-age-of-empire` |
| 953 | Interwar Period | `era-interwar-period` |
| 954 | World War II Era | `era-world-war-ii-era` |
| 960 | Contemporary | `era-contemporary` |
| 961 | Cold War Era | `era-cold-war-era` |
| 962 | Post-Cold War & Globalization | `era-post-cold-war` |
| 963 | Digital Age | `era-digital-age` |

---

## 7. Forbidden Patterns

| Pattern | Why Forbidden |
|---------|---------------|
| Sentence-as-slug (`influenced-subsequent-historical-developments`) | Phantom node; not a real entity |
| Truncated slug (cut at 50 chars) | Broken references; unresolvable |
| Generic cause/effect slug (`historical-forces-and-geopolitical-developments`) | Boilerplate; adds no information |
| Duplicate prefix (`country-country-egypt`) | Redundant; parsing breaks |
| Mixed case (`Henry-VIII`) | Violates kebab-case rule |
| Underscore (`magna_carta`) | Violates kebab-case rule |

---

## 8. Migration Notes

Phase 4 enrichment (April 2026) standardized all slugs from the Wikidata pipeline:
- Fixed em-dash date ranges (`197475` → `1974-75`)
- Removed `field-XXX` numeric targets → replaced with `division-{heading-slug}`
- Removed place-based relationships from `relationships[]` (covered by `places[]` tab)
- Removed phantom cause/effect slugs (sentence-derived non-entities)
- Added `era-` prefix to all OCCURS_DURING targets
- Created Timeframe entities for all 28 callNumbers.ts divisions (class 9)
