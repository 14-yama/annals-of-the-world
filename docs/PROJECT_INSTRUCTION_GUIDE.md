# Annals of the World — GitHub Project Instruction Guide

**A comprehensive guide for contributors working on the geo-registry country profiles and data enrichment pipeline.**

*Last updated: March 2026*

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Getting Started](#getting-started)
4. [Country Profile Schema](#country-profile-schema)
5. [Data Enrichment Workflow](#data-enrichment-workflow)
6. [Batch Processing Strategy](#batch-processing-strategy)
7. [Known Issues & Error Avoidance](#known-issues--error-avoidance)
8. [Commit Strategy](#commit-strategy)
9. [Validation & QA](#validation--qa)
10. [Data Sources & Citation Standards](#data-sources--citation-standards)
11. [Analysis & Reporting](#analysis--reporting)
12. [Contributing Checklist](#contributing-checklist)

---

## 1. Project Overview

**Annals of the World** is a Neo4j-based historical knowledge graph that models people, ideas, places, events, institutions, texts, and evidence across time and space. The **geo-registry** component provides comprehensive country profiles with ~319 data points per country across 27 sections.

### Key Goals
- Build analysis-ready country profiles enabling **country vs. continent vs. global** comparisons
- Maintain strict data governance with evidence-backed, version-controlled data
- Support cross-civilizational and cross-continental pattern analysis

### Current Coverage
- **199 countries** across 5 continents + Russia (transcontinental)
- **55 African countries** fully enhanced with 319 data points each
- **12 enhanced sections** per country beyond the original 11 base sections

---

## 2. Repository Structure

```
annals-of-the-world/
├── geo-registry/
│   └── places/
│       └── countries/
│           ├── _template/
│           │   └── index.json          # Master template (~319 data points)
│           ├── {country-slug}/
│           │   └── index.json          # Individual country profile
│           └── ...
├── analyses/                           # All analysis outputs
│   └── Global_Analysis_199_Countries.md
├── scripts/
│   ├── enhance_africa_batch1.py        # Reference enrichment script
│   └── ...
├── docs/
│   ├── PROJECT_INSTRUCTION_GUIDE.md    # This file
│   └── ...
└── ...
```

### Country Slug Convention
- All lowercase, hyphen-separated: `south-africa`, `dr-congo`, `cabo-verde`
- **Critical slug mappings** (frequently mis-guessed):
  - Côte d'Ivoire → `cote-divoire` (NOT `cote-d-ivoire`)
  - DR Congo → `dr-congo` (NOT `democratic-republic-of-the-congo`)
  - São Tomé and Príncipe → `sao-tome-and-principe`
  - Guinea-Bissau → `guinea-bissau`
  - Central African Republic → `central-african-republic`

> **Always verify slugs** by listing the directory before running batch scripts:
> ```bash
> ls geo-registry/places/countries/ | grep -i "partial-name"
> ```

---

## 3. Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for UI dev server)
- Git
- Neo4j (optional, for graph database operations)

### Setup
```bash
# Clone the repository
git clone <repo-url>
cd annals-of-the-world

# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Start UI dev server (optional)
cd ui && npm install && npm run dev:demo
```

### Branch Strategy
- Work on feature branches: `scaffold/docs`, `feat/enrich-asia`, etc.
- Keep changes focused: one continent or batch per branch when possible

---

## 4. Country Profile Schema

Each `index.json` follows the master template at `_template/index.json` with ~319 data points across 27 sections:

### Base Identity Fields
| Field | Example |
|-------|---------|
| `name` | "South Africa" |
| `capital` | "Pretoria" |
| `capital_coordinates` | `{"lat": -25.7461, "lon": 28.1881}` |
| `other_major_cities` | `["Johannesburg", "Cape Town", ...]` |
| `area_km2` | 1221037 |
| `currency` / `currency_code` | "South African Rand" / "ZAR" |
| `internet_tld` | ".za" |
| `utc_offset` | "UTC+2" |
| `drives_on` | "left" |

### 27 Sections

**Original 11 sections:**
1. `demographics` — population, age structure, urbanization, literacy
2. `economy` — GDP, HDI, sectors, major industries
3. `natural_resources` — primary resources, resource dependency
4. `independence` — year, colonial power, method
5. `government_type` — political system
6. `official_languages` — array of languages
7. `major_religions` — array of religions
8. `ethnic_groups` — array of ethnic groups
9. `international_memberships` — AU, UN, regional bodies
10. `infrastructure` — internet, roads, telecoms
11. `military` — personnel, budget, alliances

**12 Enhanced sections (added Phase 5):**
12. `geography` — coordinates, bounding box, terrain, borders, rivers, lakes, land use
13. `economy_extended` — GDP PPP, Gini, poverty, labor force, FDI, credit ratings
14. `health` — HIV, maternal mortality, physicians, clean water, vaccination
15. `food_agriculture` — food security, crops, livestock, undernourishment
16. `energy` — energy mix, installed capacity, rural/urban access
17. `transport` — airports, seaports, airlines, railways
18. `tourism` — visitors, UNESCO sites, attractions, passport rank
19. `human_rights_gender` — Freedom House, gender indices, LGBTQ status, death penalty
20. `security_stability` — GPI, conflicts, homicide rate, IDPs
21. `cultural_heritage` — symbols, cuisine, festivals, music, intangible heritage
22. `legal_system` — legal tradition, constitution, ICC membership, sharia
23. `comparative_rankings` — continent and global ranks across key metrics

**Expanded fields (added to existing sections):**
- `_expand_demographics` — population growth, age structure, density
- `_expand_infrastructure` — 4G/5G coverage, submarine cables
- `_expand_trade` — exports/imports, trade partners, SEZs
- `_expand_debt_aid` — external debt, aid donors, IMF/HIPC status
- `_expand_climate_environment` — CO2, deforestation, EPI, biodiversity
- `_expand_education` — expenditure, completion rates, PISA
- `_expand_diaspora_migration` — diaspora, remittances, refugees
- `_expand_digital_economy` — mobile money, fintech, AI readiness
- `_expand_governance_indices` — rule of law, government effectiveness
- `_expand_military` — paramilitary, conscription, firepower rank

---

## 5. Data Enrichment Workflow

### Phase Overview
1. **Phase 1-3**: Populate thematic files, people.json, basic 11-section profiles
2. **Phase 4**: Enhance `_template/index.json` from ~85 to ~319 data points
3. **Phase 5**: Apply enhanced template to all countries with real data
4. **Phase 6**: Analysis and cross-continental comparison

### The `patch_country()` Pattern

All enrichment scripts use the same function pattern:

```python
import json, os, copy

BASE = os.path.join("geo-registry", "places", "countries")

def patch_country(slug, patch):
    """Read index.json, merge new sections + expanded fields, write back."""
    path = os.path.join(BASE, slug, "index.json")
    with open(path) as f:
        data = json.load(f)
    cp = data["country_profile"]

    # 1. Add _basics (capital_coordinates, cities, motto, etc.)
    basics = patch.pop("_basics", {})
    for k, v in basics.items():
        cp[k] = v

    # 2. Add 12 new sections
    new_sections = {k: v for k, v in patch.items() if not k.startswith("_")}
    for sec, val in new_sections.items():
        cp[sec] = val

    # 3. Expand existing sections with _expand_ prefixed keys
    for key, val in patch.items():
        if key.startswith("_expand_"):
            sec_name = key.replace("_expand_", "")
            if sec_name in cp and isinstance(cp[sec_name], dict):
                cp[sec_name].update(val)

    # 4. Update metadata
    meta = data.get("_meta", {})
    meta["data_year"] = 2024

    # 5. Update leadership
    lead = data.get("leadership", {})
    if "head_of_government" not in lead:
        lead["head_of_government"] = {"name": "", "title": "", "since": "", "party": ""}
    if "legislature" not in lead:
        lead["legislature"] = {"type": "", "chambers": [], "total_seats": 0,
                               "ruling_party": "", "next_election": ""}
    for lk in ["current_leader", "head_of_state"]:
        if lk in lead and isinstance(lead[lk], dict) and "party" not in lead[lk]:
            lead[lk]["party"] = ""

    data["country_profile"] = cp
    data["_meta"] = meta
    data["leadership"] = lead
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return len(new_sections)
```

### Data Dictionary Per Country

Each country DATA entry requires:
- `_basics` dict — 8 fields (coordinates, cities, motto, anthem, currency_code, tld, utc, drives_on)
- 12 new section dicts — geography, economy_extended, health, food_agriculture, energy, transport, tourism, human_rights_gender, security_stability, cultural_heritage, legal_system, comparative_rankings
- 10 `_expand_*` dicts — demographics, infrastructure, trade, debt_aid, climate_environment, education, diaspora_migration, digital_economy, governance_indices, military

---

## 6. Batch Processing Strategy

### Why Batches?
Enriching 55 countries produces ~16,000+ lines of Python data. Processing all at once is impractical and error-prone. Batches provide:
- Incremental progress with safe checkpoints
- Manageable review sizes
- Error isolation to specific countries

### Recommended Batch Size: 3 Countries

After testing, **3 countries per execution** (~900 lines) is the optimal balance of speed and reliability.

### Execution Method: Terminal Heredoc

```bash
cd /path/to/annals-of-the-world && python3 << 'PYEOF'
import json, os, copy
# ... patch_country() function ...
# ... DATA dict for 3 countries ...
# ... main loop ...
PYEOF
```

> **Why heredoc?** See [Known Issues](#known-issues--error-avoidance) for the HTTP/2 error that blocks file-based approaches for large scripts.

### Batch Grouping
- Alphabetically grouped, 3 countries each
- Every 3 batches (9 countries) → git commit
- Validation after each batch (check terminal output for "OK {slug}: 12 new sections")

---

## 7. Known Issues & Error Avoidance

### ⚠️ CRITICAL: `ERR_HTTP2_PROTOCOL_ERROR` (File Size Limit)

**What happened:** During Phase 5, Batch 2 attempted to create a Python script with 10 countries (~3,000+ lines) using the VS Code `create_file` API. The operation failed with:

```
ERR_HTTP2_PROTOCOL_ERROR
```

**Root cause:** VS Code's extension API communicates over HTTP/2, which has frame size limits. Files exceeding approximately **1,500 lines** can trigger this protocol error, causing the file creation to fail silently or abort.

**Impact:** The batch script was not written to disk, but the agent proceeded as if it had, leading to confusion and wasted time.

**How to avoid this in the future:**

1. **Never create script files larger than ~1,500 lines** via IDE file creation APIs
2. **Use terminal heredoc execution** for large data scripts:
   ```bash
   python3 << 'PYEOF'
   # ... your script here ...
   PYEOF
   ```
3. **Keep batches to 3 countries maximum** (~300 lines per country × 3 = ~900 lines)
4. **If you must create a file**, split into multiple smaller files (e.g., `batch2a.py`, `batch2b.py`)
5. **Always verify the file was actually created** before proceeding:
   ```bash
   wc -l scripts/my_script.py  # Should show expected line count
   ```

### ⚠️ Slug Mismatches

**What happened:** Validation scripts used assumed slugs like `cote-d-ivoire` and `democratic-republic-of-the-congo`, but actual slugs are `cote-divoire` and `dr-congo`.

**How to avoid:**
```bash
# Always verify actual slugs before writing batch scripts
ls geo-registry/places/countries/ | sort
```

### ⚠️ JSON Encoding Issues

**Risk:** Country names with diacritics (São Tomé, Côte d'Ivoire) can cause encoding issues.

**Solution:** Always use `ensure_ascii=False` in `json.dump()`:
```python
json.dump(data, f, indent=2, ensure_ascii=False)
```

### ⚠️ Large Terminal Output Truncation

**What happens:** Terminal output exceeding ~60KB is truncated. For batch scripts that print verbose output, this can hide errors.

**How to avoid:**
- Keep print output minimal (one line per country)
- Use `tail -5` to check final output if truncated
- For validation, use targeted checks rather than dumping entire files

---

## 8. Commit Strategy

### Commit Frequency
- **Every 3 batches** (9 countries) = 1 commit
- **Never exceed 10 changed files** per commit for reviewability
- **Final batch** may be smaller (2-5 countries) — commit immediately

### Commit Message Format
```
enhance: batches N-M (FirstCountry–LastCountry) – X countries with 12 new sections + expanded fields
```

**Example:**
```
enhance: batches 14-16 (Senegal–Togo) – 9 countries with 12 new sections + expanded fields
```

### Git Workflow
```bash
# Stage all changes
git add -A

# Commit with descriptive message
git commit -m "enhance: batches 5-7 (DR Congo–Ghana) – 9 countries with 12 new sections + expanded fields"

# Verify commit
git log --oneline -1
```

### Phase 5 Commit History (Reference)
| Commit | Batch | Countries | Count |
|--------|-------|-----------|-------|
| `f024981` | Template | Enhanced `_template/index.json` | — |
| `f152b53` | 1 | Algeria → Burkina Faso | 5 |
| `7372a9a` | 2–4 | Burundi → Djibouti | 9 |
| `ea602c6` | 5–7 | DR Congo → Ghana | 9 |
| `9ed2ef5` | 8–10 | Guinea → Mali | 9 |
| `8ca95a7` | 11–13 | Mauritania → São Tomé | 9 |
| `edefcbd` | 14–16 | Senegal → Togo | 9 |
| `7de2fc4` | 17–18 | Tunisia → Zimbabwe | 5 |

---

## 9. Validation & QA

### Per-Batch Validation
After each batch execution, check terminal output for success messages:
```
OK algeria: 12 new sections + expanded fields added
OK angola: 12 new sections + expanded fields added
...
Batch N done. 3 countries enhanced.
```

### Full Continent Validation
Run after completing all countries for a continent:

```python
python3 -c "
import json, os
base = 'geo-registry/places/countries'
new_secs = ['geography','economy_extended','health','food_agriculture','energy',
            'transport','tourism','human_rights_gender','security_stability',
            'cultural_heritage','legal_system','comparative_rankings']

# List actual slugs for your continent
slugs = ['algeria', 'angola', ...]  # USE ACTUAL VERIFIED SLUGS

ok, fail = 0, 0
for s in slugs:
    path = os.path.join(base, s, 'index.json')
    if not os.path.exists(path):
        print(f'FILE MISSING: {s}')
        fail += 1
        continue
    with open(path) as f:
        data = json.load(f)
    cp = data.get('country_profile', {})
    missing = [sec for sec in new_secs if sec not in cp]
    if missing:
        print(f'MISSING {s}: {missing}')
        fail += 1
    else:
        ok += 1
print(f'\n{ok}/{len(slugs)} OK, {fail} issues')
"
```

### Data Quality Checks
- **Numeric ranges**: GDP per capita should be reasonable ($200–$200,000)
- **Percentages**: Should be 0–100 (not decimals like 0.45 for 45%)
- **Coordinates**: Latitude -90 to 90, Longitude -180 to 180
- **Consistency**: Life expectancy female > male (almost always true)
- **Cross-reference**: UNESCO site count should match `unesco_sites_list` length

---

## 10. Data Sources & Citation Standards

### Primary Sources (all data hardcoded, NOT fetched at runtime)
| Source | Used For |
|--------|----------|
| World Bank Open Data | GDP, population, poverty, Gini, infrastructure |
| IMF World Economic Outlook | GDP growth, inflation, fiscal data |
| CIA World Factbook | Geography, government, military, demographics |
| UNDP Human Development Report | HDI, gender indices, education |
| WHO Global Health Observatory | Health expenditure, disease prevalence, mortality |
| FAO/WFP | Food security, agriculture, undernourishment |
| Freedom House | Freedom scores, political rights, civil liberties |
| Global Peace Index (IEP) | Peace rankings, conflict data |
| Transparency International | Corruption Perceptions Index |
| UNESCO | World Heritage Sites, intangible heritage |
| ITU | Internet penetration, telecoms data |
| WIPO Global Innovation Index | Innovation rankings |
| UNWTO | Tourism arrivals, revenue |

### Data Year
- Default data year: **2024** (set in `_meta.data_year`)
- Some metrics use 2023 estimates where 2024 unavailable
- Always note the reference year in section-level `notes` fields

---

## 11. Analysis & Reporting

### Analysis Output Location
All analysis files go in the `analyses/` directory:
```
analyses/
├── Global_Analysis_199_Countries.md
├── Africa_Hidden_Patterns_55_Countries.md
├── Africa_Continent_Analysis.md
└── ...
```

### Analysis Types
1. **Country-level "Hidden Patterns"**: Unique, non-obvious insights per country
2. **Continent-level comparison**: Africa vs. Asia vs. Europe vs. Americas vs. Oceania
3. **Global analysis**: Cross-continental patterns and rankings

---

## 12. Contributing Checklist

Before submitting changes to country profiles:

- [ ] Verified country slug matches actual directory name
- [ ] Used `ensure_ascii=False` in JSON serialization
- [ ] All 12 new sections present in updated `country_profile`
- [ ] All 10 `_expand_*` fields merged into existing sections
- [ ] `_meta.data_year` set to current data year
- [ ] `leadership` contains `head_of_government` and `legislature`
- [ ] Numeric values use correct units (km², USD, percentages as integers)
- [ ] `notes` fields include source context and caveats
- [ ] Batch size ≤ 3 countries (to avoid HTTP/2 errors)
- [ ] Terminal output shows "OK" for all countries in batch
- [ ] Committed with standard message format
- [ ] Validation script confirms all sections present

---

## Quick Reference

### Common Commands
```bash
# Activate virtual environment
source .venv/bin/activate

# List all country slugs
ls geo-registry/places/countries/ | grep -v _template | sort

# Check a specific country's sections
python3 -c "import json; d=json.load(open('geo-registry/places/countries/SLUG/index.json')); print(list(d['country_profile'].keys()))"

# Count data points in a country
python3 -c "
import json
def count_keys(d, prefix=''):
    n = 0
    for k, v in d.items():
        n += 1
        if isinstance(v, dict):
            n += count_keys(v, prefix + k + '.')
    return n
d = json.load(open('geo-registry/places/countries/SLUG/index.json'))
print(f'Total data points: {count_keys(d)}')
"

# Run dev server
cd ui && npm run dev:demo
```

---

*This guide was created to document lessons learned during the Phase 5 Africa enrichment campaign (55 countries, 18 batches, 7 commits). Apply these patterns when enriching other continents.*
