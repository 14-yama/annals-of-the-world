# Backend Edit Log — Annals of the World

> Chronological record of all backend data edits, schema fixes, enrichments, and maintenance operations.
> Appwrite is the live source of truth; JSON exports in `data/appwrite-export/` are the backup copy.

---

## Status Summary

| Metric | Value | Last Updated |
|--------|-------|--------------|
| Total entities (Appwrite) | ~357,999 | 2026-04-12 |
| Total enriched entities | 132 | Batch 7, 2026-04-12 |
| Total new entities created | 26 | Batch 7, 2026-04-12 |
| Duplicate removals | 175 (normalized slug dedup) | 2026-04-12 |
| Misclassification fixes | 607 (604 batch + 2 targeted + 1 batch 7) | 2026-04-12 |
| Underscore slugs remaining | ~777 → 0 (fixed batch 5) | 2026-04-12 |
| Stub summaries (<200c) | ~35,568 | 2026-04-12 (backlog) |

---

## Edit History

### Batch 1 — Initial Enrichment (2026-04-05)
- **Scope:** 30 high-profile entities enriched
- **Entities:** julius-caesar, cleopatra-vii, alexander-the-great, genghis-khan, napoleon-bonaparte, queen-victoria, abraham-lincoln, mahatma-gandhi, winston-churchill, nelson-mandela, martin-luther-king-jr, galileo-galilei, isaac-newton, charles-darwin, albert-einstein, leonardo-da-vinci, william-shakespeare, socrates, plato, aristotle, confucius, buddha, muhammad-prophet, moses, jesus-of-nazareth, marco-polo, christopher-columbus, ferdinand-magellan, hippocrates, euclid
- **Actions:** Added rich summaries (800–1300c), causes (3+), effects (3+), relationships (5+), places, frameworks
- **Commit:** Part of `clean/audit-system` branch

### Batch 2 — Enrichment + 11 New Entities (2026-04-06)
- **Scope:** 26 enrichments + 11 new entities created
- **Enriched:** elizabeth-i, charlemagne, augustus-caesar, ramesses-ii, qin-shi-huang, akbar-the-great, suleiman-the-magnificent, peter-the-great, tokugawa-ieyasu, saladin, cyrus-the-great, mansa-musa, sun-tzu, thucydides, herodotus, joan-of-arc, martin-luther, john-locke, karl-marx, pablo-picasso, frida-kahlo, nikola-tesla, mark-twain, louis-pasteur, rachel-carson, george-washington
- **New Entities Created:** marie-antoinette, hatshepsut, hypatia, avicenna, al-khwarizmi, gutenberg, copernicus, kepler, thomas-aquinas, ibn-khaldun, simone-de-beauvoir
- **Commit:** Part of `clean/audit-system` branch

### Batch 3 — Deep Enrichment (2026-04-07)
- **Scope:** 26 entities enriched
- **Entities:** attila-the-hun, hannibal-barca, simon-bolivar, toussaint-louverture, shaka-zulu, mehmed-ii, tamerlane, babur, ashoka, montezuma-ii, pachacuti, menes, hammurabi, nefertiti, sappho, rumi, omar-khayyam, murasaki-shikibu, rabindranath-tagore, wangari-maathai, tu-youyou, alan-turing, ada-lovelace, nikola-tesla, rachel-carson, simone-de-beauvoir
- **Commit:** `399e84e278`

### Batch 4 — Dedup + Enrichment + New Entities (2026-04-12)
- **Scope:** 175 duplicate removals, 2 misclassification fixes, 26 enrichments, 5 new entities

#### Phase 1: Targeted Fixes
| Entity | Old Location | New Location | Issue |
|--------|-------------|--------------|-------|
| `armenian` → `artaxiad-dynasty-of-armenia` | 221 (Person/Monarchs) | 523 (EventWindow) | Corrupt stub, wrong label |
| `bani-yas-island` | 220 (Person/Political) | 462 (Place) | Wrong label — is a geographic place |

#### Phase 2: Normalized Duplicate Removal (175)
- **Method:** Underscore→hyphen normalization, richness scoring (character count), first-occurrence-wins
- **Examples:** `william_the_conqueror` (280, stub) deleted — `william-the-conqueror` (221, enriched) kept
- **Full list:** See `scripts/deduplicate_and_fix.py` output

#### Phase 3: Enrichment (26 entities)
- alan-turing, ada-lovelace, archimedes, marie-curie, otto-von-bismarck, vladimir-lenin, neil-armstrong, rembrandt, thomas-hobbes, jean-jacques-rousseau, michelangelo, leo-tolstoy, deng-xiaoping, vasco-da-gama, james-cook, roald-amundsen, zheng-he, francis-bacon, erasmus, john-calvin, florence-nightingale, thomas-edison, wright-brothers, frederick-douglass, ibn-battuta, tim-berners-lee

#### Phase 4: New Notable Entities (5)
- dante-alighieri, fyodor-dostoevsky, rosa-parks, queen-elizabeth-ii, pope-john-paul-ii

#### Appwrite Sync
- 177 deletions (175 duplicates + armenian + bani-yas-island old location)
- 33 upserts (26 enriched + 5 new + 2 reclassified)
- **Commit:** `9a81d732ea`

### Batch 5 — Slug Normalization + Audit Enhancement (2026-04-12)
- **Scope:** Fix 777 underscore slugs → kebab-case, enhance Appwrite audit functions
- **Actions:**
  - Normalize all `_` slugs to `-` in local JSON + Appwrite (777 files)
  - Add stub summary detection to `audit-consistency`
  - Add slug variant duplicate detection to `audit-duplicates`
  - Add slug normalization auto-fix to `audit-consistency`
- **Commit:** `2136d24cd6`

### Batch 6 — High-Value Entity Enrichment (2026-04-12)
- **Scope:** 14 PARTIAL/STUB entities enriched to full quality (800–1300c summaries)
- **Targets:** Entities with summaries 243–595 characters, all importanceScore ≥ 6
- **Enriched:**
  - **STUB → FULL:** jan-hus (331c→1256c), thomas-more (304c→1295c), wolfgang-amadeus-mozart (243c→1183c)
  - **PARTIAL → FULL:** caravaggio (447c→1189c), charles-dickens (404c→1273c), giuseppe-garibaldi (448c→1291c), harriet-tubman (471c→1282c), johann-sebastian-bach (534c→1211c), leon-trotsky (583c→1296c), ludwig-van-beethoven (505c→1258c), mother-teresa (595c→1175c), rabindranath-tagore (409c→1282c), vincent-van-gogh (502c→1279c), yuri-gagarin (505c→1228c)
- **Quality:** All entities now have: rich summaries (3–4 paragraphs), 3+ causes, 3+ effects, 5 relationships (full EntityRelationship format), 3 places, 8 subjects, 3 frameworks
- **Script:** `scripts/enrich_batch6.py`
- **Appwrite Sync:** 14 entities updated
- **Commit:** `66b1e722f5`

### Batch 7 — Stub Enrichment + New Notable Entities (2026-04-12)
- **Scope:** 10 worst STUB enrichments + 10 missing high-importance entities created
- **Priority:** P0 (stubs with wrong/tiny data) and P1 (missing notable figures)

#### Enrichments (10 STUB → FULL)
| Entity | Old (c) | Issue | Fix Applied |
|--------|---------|-------|-------------|
| richard-wagner | 110c | **Wrong person** — listed as Romanian novelist | Rewritten as German composer; moved 201→263 |
| victor-hugo | 139c | Stub | Full enrichment |
| henry-v | 158c | Wrong Henry V (HRE) | Rewritten as English king of Agincourt |
| nero | 161c | Minimal stub | Full enrichment |
| justinian-i | 179c | Minimal stub | Full enrichment |
| jane-austen | 180c | Stub | Full enrichment |
| montesquieu | 180c | Stub | Full enrichment |
| robert-koch | 195c | Stub | Full enrichment |
| virginia-woolf | 197c | Stub | Full enrichment |
| max-planck | 199c | Stub | Full enrichment |

#### New Entities Created (10)
| Entity | Call Number | Era | Importance |
|--------|------------|-----|------------|
| rene-descartes | 210 | Early Modern | 9 |
| baruch-spinoza | 210 | Early Modern | 8 |
| miguel-de-cervantes | 260 | Early Modern | 9 |
| johann-wolfgang-von-goethe | 260 | Early Modern | 9 |
| frederic-chopin | 263 | Modern | 8 |
| george-orwell | 260 | Contemporary | 9 |
| ho-chi-minh | 222 | Contemporary | 8 |
| stephen-hawking | 240 | Contemporary | 8 |
| j-robert-oppenheimer | 240 | Contemporary | 8 |
| pyotr-ilyich-tchaikovsky | 263 | Modern | 8 |

- **Reclassification:** richard-wagner moved from 201 (Educators) to 263 (Musicians)
- **Script:** `scripts/enrich_batch7.py`
- **Appwrite Sync:** 20/20 synced (2 required slug-based ID lookup)
- **Commit:** TBD

---

## Classification Fix Log

### 604 Misclassification Batch (2026-04-06)
- **Script:** `scripts/fix_classifications.py`
- **Method:** Automated Dewey division reassignment based on label→class mapping
- **Labels fixed:** Person→2xx, Institution→3xx, Place→4xx, EventWindow→5xx, Movement→6xx, Idea→0xx/1xx, Text→7xx, Evidence→8xx

---

## Outstanding Issues — Backend Backlog

### P0 — Data Integrity (fix now)
1. ~~**777 underscore slugs** violate kebab-case convention (`slug_naming_convention.md`)~~ → Fixed in Batch 5
2. **Stub summaries** — 35,568 entities have summaries <200 characters or auto-generated text
   - Pattern: "A notable figure associated with X" / name-only descriptions
   - Priority: Enrich top-importance entities first (importanceScore ≥ 7)
3. **Detached relationship targets** — Some `detailsJson.relationships[].targetSlug` point to deleted/nonexistent entities

### P1 — Enrichment Debt
4. **Top 100 historical figures still stubs** — Many entities with importanceScore ≥ 8 lack rich summaries
   - 132 now enriched across batches 1–7 (10 stubs fixed in batch 7: richard-wagner, victor-hugo, nero, justinian-i, jane-austen, montesquieu, robert-koch, virginia-woolf, max-planck, henry-v)
   - 26 new entities created (10 in batch 7: descartes, spinoza, cervantes, goethe, chopin, orwell, ho chi minh, hawking, oppenheimer, tchaikovsky)
   - Examples still needing work: pericles, fidel-castro, henry-viii, margaret-thatcher, ernest-hemingway, franz-kafka
5. **Missing Wikidata QIDs** — Majority of entities have empty `wikidataQid` field
6. **Missing image URLs** — Most entities have no `imageUrl` or `thumbnailUrl`
7. **Event windows lack causes/effects** — Geo-registry event windows (majority of dataset) have zero causal chains

### P2 — Schema Health
8. **Single-relationship entities** — Many entities only have `OCCURS_DURING` as their sole relationship
9. **Empty frameworks** — Entities without any interpretive framework assignments
10. **Call number format inconsistencies** — Some call numbers don't match `Class.Division.Slug` pattern
11. **Era-division code mismatches** — Some entities have era values that don't match their eraDivisionCode

### P3 — Ongoing Maintenance
12. **Weekly duplicate scan** — Run `audit-duplicates` function and review output
13. **Monthly enrichment targets** — Select 25-50 high-importance stubs for enrichment each month
14. **Relationship graph density** — Improve average relationships per entity (currently ~1.2, target: 3+)
15. **Cross-corpus relationships** — Add relationships between entities across different corpus collections

---

## Appwrite Cloud Functions — Audit Coverage

| Function | Schedule | Slug Check | Stub Check | Dedup | Status |
|----------|----------|-----------|------------|-------|--------|
| `audit-consistency` | Every 30 min | Format regex ✅ | Length ≥ 50 only | Exact slug ✅ | Enhanced (Batch 5) |
| `audit-completeness` | Every 10 min | ❌ | Length ≥ 50 only | ❌ | Stats mode only |
| `audit-duplicates` | Weekly Sun 04:00 | ❌ → ✅ | ❌ | Name-based ✅ | Enhanced (Batch 5) |
| `audit-orphans` | Daily 03:00 | ❌ | ❌ | ❌ | Unchanged |
| `audit-classification` | Daily 06:00 | ❌ | ❌ | ❌ | Unchanged |

### Enhancements Added (Batch 5)
- `audit-consistency`: Added underscore slug auto-detection, stub summary pattern matching, auto-fix mode
- `audit-duplicates`: Added normalized slug variant comparison (underscore↔hyphen)

---

## Scripts Reference

| Script | Purpose | Last Run |
|--------|---------|----------|
| `scripts/deduplicate_and_fix.py` | Phase 1 specific fixes + Phase 2 normalized dedup | 2026-04-12 |
| `scripts/enrich_batch4.py` | 26 enrichments + 5 new entities | 2026-04-12 |
| `scripts/fix_slugs_batch5.py` | Normalize 777 underscore slugs | 2026-04-12 |
| `scripts/enrich_batch6.py` | 14 high-value entity enrichments | 2026-04-12 |
| `scripts/enrich_batch7.py` | 10 stub enrichments + 10 new entities | 2026-04-12 |
| `scripts/sync_batch4_deletions.py` | Delete 177 entities from Appwrite | 2026-04-12 |
| `scripts/sync_batch4_upserts.py` | Upsert 33 entities to Appwrite | 2026-04-12 |
| `scripts/sync_appwrite_to_repo.ts` | Export Appwrite → JSON | On demand |
| `scripts/sync_repo_to_appwrite.ts` | Import JSON → Appwrite | On demand |
