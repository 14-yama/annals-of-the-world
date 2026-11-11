# Backend Edit Log — Annals of the World

> Chronological record of all backend data edits, schema fixes, enrichments, and maintenance operations.
> Appwrite is the live source of truth; JSON exports in `data/appwrite-export/` are the backup copy.

---

## Status Summary

| Metric | Value | Last Updated |
|--------|-------|--------------|
| Total entities (Appwrite) | ~357,999 | 2026-04-12 |
| Total enriched entities | 146 | Batch 8, 2026-04-12 |
| Total new entities created | 32 | Batch 8, 2026-04-12 |
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
- **Commit:** `afa3bf3189`

### Batch 8 — Worst PARTIAL/STUB Enrichment + New Notable Entities (2026-04-12)
- **Scope:** 14 worst PARTIAL/STUB entities (<300c) enriched + 6 missing high-importance entities created
- **Priority:** P0 (critical stubs blaise-pascal 96c, nikita-khrushchev 151c) and P1 (worst PARTIALs + missing figures)

#### Enrichments (14 entities)
| Entity | Old (c) | Category | Fix Applied |
|--------|---------|----------|-------------|
| blaise-pascal | 96c | **STUB** | Complete rewrite — mathematician/philosopher/inventor |
| nikita-khrushchev | 151c | **STUB** | Full enrichment — Soviet leader, Cuban Missile Crisis |
| pericles | 207c | PARTIAL | Full enrichment — Athenian Golden Age |
| fidel-castro | 228c | PARTIAL | Full enrichment — Cuban Revolution |
| xerxes-i | 228c | PARTIAL | Full enrichment — Persian Wars |
| margaret-thatcher | 238c | PARTIAL | Full enrichment — Iron Lady, Thatcherism |
| igor-stravinsky | 239c | PARTIAL | Full enrichment — Rite of Spring, modernism |
| louis-xiv | 249c | PARTIAL | Full enrichment — Sun King, Versailles |
| mikhail-gorbachev | 249c | PARTIAL | Full enrichment — glasnost, perestroika |
| francis-of-assisi | 252c | PARTIAL | Full enrichment — Franciscan Order |
| ibn-sina | 256c | PARTIAL | Full enrichment — Canon of Medicine |
| henry-viii | 268c | PARTIAL | Full enrichment — English Reformation |
| niels-bohr | 271c | PARTIAL | Full enrichment — quantum mechanics |
| ronald-reagan | 248c | PARTIAL | Full enrichment — Reaganomics, Cold War |

#### New Entities Created (6)
| Entity | Call Number | Era | Importance |
|--------|------------|-----|------------|
| oliver-cromwell | 222 | Early Modern | 8 |
| gottfried-wilhelm-leibniz | 210 | Early Modern | 9 |
| alfred-hitchcock | 260 | Contemporary | 8 |
| gabriel-garcia-marquez | 261 | Contemporary | 8 |
| werner-heisenberg | 240 | Contemporary | 8 |
| erwin-schrodinger | 240 | Contemporary | 8 |

- **Script:** `scripts/enrich_batch8.py`
- **Appwrite Sync:** 20/20 synced
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
   - 146 now enriched across batches 1–8 (14 worst PARTIALs/STUBs fixed in batch 8: blaise-pascal, nikita-khrushchev, pericles, fidel-castro, henry-viii, margaret-thatcher, etc.)
   - 32 new entities created (6 in batch 8: oliver-cromwell, leibniz, hitchcock, garcia-marquez, heisenberg, schrodinger)
   - Examples still needing work: democritus, desmond-tutu, titian, max-weber, al-biruni, ernest-hemingway, franz-kafka, charlie-chaplin
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
| `scripts/enrich_batch8.py` | 14 PARTIAL/STUB enrichments + 6 new entities | 2026-04-12 |
| `scripts/sync_batch4_deletions.py` | Delete 177 entities from Appwrite | 2026-04-12 |
| `scripts/sync_batch4_upserts.py` | Upsert 33 entities to Appwrite | 2026-04-12 |
| `scripts/sync_appwrite_to_repo.ts` | Export Appwrite → JSON | On demand |
| `scripts/sync_repo_to_appwrite.ts` | Import JSON → Appwrite | On demand |

### AI Enrichment — 2026-04-13T23:47:43Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19 | **Synced:** 1
- **Entities:** era-modern

### AI Enrichment — 2026-05-09T11:58:49Z

- **Model:** gemini
- **Enriched:** 10 | **Failed:** 0
- **Entities:** era-late-medieval, era-high-medieval, era-interwar-period, era-world-war-ii-era, era-bronze-age, era-archaic-period, era-digital-age, era-cold-war-era, era-hellenistic-period, era-reformation-era

### AI Enrichment — 2026-05-09T12:26:42Z

- **Model:** gemini
- **Enriched:** 10 | **Failed:** 0
- **Entities:** era-late-medieval, era-high-medieval, era-hellenistic-period, era-reformation-era, era-bronze-age, era-interwar-period, era-world-war-ii-era, era-cold-war-era, era-archaic-period, era-digital-age

### AI Enrichment — 2026-05-09T14:49:12Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 19
- **Entities:** era-age-of-enlightenment

### AI Enrichment — 2026-05-10T02:17:08Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 19
- **Entities:** era-renaissance-period

### AI Enrichment — 2026-05-10T02:23:14Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 47
- **Entities:** era-age-of-empire, magnus-of-trani, new-testament

### AI Enrichment — 2026-05-10T13:58:10Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 17
- **Entities:** leonard-of-noblac, era-age-of-exploration

### AI Enrichment — 2026-05-10T17:50:25Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 17
- **Entities:** demosthenes

### AI Enrichment — 2026-05-10T17:54:31Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 17
- **Entities:** era-early-medieval

### AI Enrichment — 2026-05-10T18:37:43Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** era-paleolithic-mesolithic

### AI Enrichment — 2026-05-10T19:28:45Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** jan-elivsk

### AI Enrichment — 2026-05-10T21:25:33Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** era-post-cold-war

### AI Enrichment — 2026-05-11T22:33:07Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 18
- **Entities:** moses-of-chorene, antonio-joaqun-prez-martnez

### AI Enrichment — 2026-05-11T22:42:06Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** jan-želivský

### AI Enrichment — 2026-05-12T09:14:53Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 18
- **Entities:** era-neolithic-chalcolithic, wazo-of-liège

### AI Enrichment — 2026-05-12T20:13:50Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** yuya

### AI Enrichment — 2026-05-13T09:00:24Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** peisandros, konstantinos-maleinos

### AI Enrichment — 2026-05-13T11:54:44Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** john-mystacon

### AI Enrichment — 2026-05-13T12:54:53Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** publius-aelius-paetus

### AI Enrichment — 2026-05-13T23:26:54Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** cuthbert

### AI Enrichment — 2026-05-14T10:42:07Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** theophilus-protospatharius

### AI Enrichment — 2026-05-15T03:37:38Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** guan-yu, jami

### AI Enrichment — 2026-05-15T16:17:33Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** lucius-ii

### AI Enrichment — 2026-05-15T21:09:02Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 18
- **Entities:** wazo-of-lige, boniface-iii

### AI Enrichment — 2026-05-16T02:02:25Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** jainism, lucio-marineo-sculo

### AI Enrichment — 2026-05-16T03:22:45Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** menon-of-pharsalus, adémar-de-chabannes, admar-de-chabannes

### AI Enrichment — 2026-05-16T04:39:08Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** chad-of-mercia, anastasius-ii

### AI Enrichment — 2026-05-16T05:59:02Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** trojan-war, hisham-ibn-urwah, juan-gil-de-hontan, giovanni-boccamazza

### AI Enrichment — 2026-05-16T07:25:49Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** tatzates

### AI Enrichment — 2026-05-16T07:51:06Z

- **Model:** ollama
- **Enriched:** 89 | **Failed:** 10
- **Entities:** time, sabinus-of-canosa, saint-marcian-of-syracuse, nerikare, shaqilath, mattan-i, ruben-ii-prince-of-armenia, gnaeus-pinarius-cornelius-severus, ermon-de-jerusalém, ermon-de-jerusalm ... +79 more

### AI Enrichment — 2026-05-16T08:25:26Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** gupta-empire, central-africa, true-jesus-church

### AI Enrichment — 2026-05-16T09:13:23Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** east-africa

### AI Enrichment — 2026-05-16T10:17:19Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** dorotea-bucca, prokop-the-great, epic-of-gilgamesh, latin-america

### AI Enrichment — 2026-05-16T11:24:46Z

- **Model:** gemini
- **Enriched:** 24 | **Failed:** 68
- **Entities:** prosdocimus, epistle-to-the-philippians, joseph-rabban, eyvindr-skldaspillir, memnon-of-ephesus, æthelburh-of-faremoutiers, murshid-quli-khan, arakamani, néféroukait, nfroukait ... +14 more

### AI Enrichment — 2026-05-16T11:31:07Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** andrea-dittis, antonio-joaquín-pérez-martínez, mansuy-of-toul

### AI Enrichment — 2026-05-16T12:49:34Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** richard-fitzralph, luis-antonio-belluga-y-moncada, fulk-of-reims

### AI Enrichment — 2026-05-16T14:21:35Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** johann-pfeffinger, katakalon-kekaumenos

### AI Enrichment — 2026-05-16T15:35:09Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** lazarus-spengler, antiochus-chuzon, guala-bicchieri

### AI Enrichment — 2026-05-16T16:53:10Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** taras-fedorovych

### AI Enrichment — 2026-05-16T16:56:42Z

- **Model:** ollama
- **Enriched:** 87 | **Failed:** 13
- **Entities:** fa-of-xia, domangart-réti, domangart-rti, keran-queen-of-armenia, nicasius-of-rheims, black-hole, enetarzi, sobekhotep-v, vologases-iii-of-parthia, orontes-i-sakavakyats ... +77 more

### AI Enrichment — 2026-05-16T17:43:25Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** cristoforo-landino, saint-marcouf

### AI Enrichment — 2026-05-16T18:29:43Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** peter-shafirov, empire, zai-yu, juan-margarit-i-pau

### AI Enrichment — 2026-05-16T19:23:53Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** john-of-rokycan, pantaenus, marcus-popillius-laenas, johannes-despauterius, justus-of-urgell

### AI Enrichment — 2026-05-16T20:14:56Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** felician-of-foligno, peter-the-iberian, lupus-of-sens

### AI Enrichment — 2026-05-16T21:02:27Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** snorri-thorfinnsson, pietro-pileo-di-prata, ammonius-grammaticus, ildibad

### AI Enrichment — 2026-05-16T21:47:59Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** vitello, henry-cromwell, orientius, assyrian-empire, hieronymus-van-beverningh

### AI Enrichment — 2026-05-16T22:36:34Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** melaine, victor-of-capua, venezuela, sweden, arame-of-urartu

### AI Enrichment — 2026-05-16T23:27:38Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** pacian, pomponio-cecci, peter-of-toledo

### AI Enrichment — 2026-05-17T00:15:59Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** gil-eanes, benin, alfonso-i-deste

### AI Enrichment — 2026-05-17T01:13:37Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** aeschines, vima-takto, pha-mueang, saadia-gaon

### AI Enrichment — 2026-05-17T01:36:17Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 0
- **Entities:** wikimedia-foundation, gonçalo-coelho, aeacides-of-epirus, magnus-felix-ennodius, paphnutius-of-thebes, international-monetary-fund

### AI Enrichment — 2026-05-17T03:33:09Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 0
- **Entities:** thorfinn-of-hamar, antarctica, procopius, gaius-sallustius-crispus-passienus, bachelors-degree, old-kingdom-of-egypt, eusebius, harald-klak, roman-republic, publius-acilius-attianus ... +15 more

### AI Enrichment — 2026-05-17T04:25:52Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** william-of-paris, poetry

### AI Enrichment — 2026-05-17T05:34:20Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** vikings, map, gospel-of-mark

### AI Enrichment — 2026-05-17T06:20:39Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 0
- **Entities:** confucianism, ecology, medicine, vikings, theatre-art, galaxy, atheism, president, astronomy, middle-ages ... +6 more

### AI Enrichment — 2026-05-17T06:26:24Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** nicene-creed, upanishads, anna-karenina, epistle-to-the-galatians, animal-farm

### AI Enrichment — 2026-05-17T07:21:27Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 1
- **Entities:** animal-farm, alices-adventures-in-wonderland, westminster-confession-of-faith, ramayana, around-the-world-in-eighty-days, the-raven, capital-a-critique-of-political-economy, paradise-lost, waiting-for-godot, hansel-and-gretel ... +5 more

### AI Enrichment — 2026-05-17T07:28:45Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** a-song-of-ice-and-fire

### AI Enrichment — 2026-05-17T08:23:50Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** classic-of-poetry

### AI Enrichment — 2026-05-17T08:40:47Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 1
- **Entities:** snow-white, the-decameron, beowulf, analects, kalevala, diary-of-anne-frank, book-of-job, sabinus-of-piacenza, panchatantra, gospel-of-judas ... +6 more

### AI Enrichment — 2026-05-17T09:30:18Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** adriaen-isenbrandt, umara-ibn-abi-al-hasan-al-yamani, all-quiet-on-the-western-front

### AI Enrichment — 2026-05-17T09:46:41Z

- **Model:** ollama
- **Enriched:** 9 | **Failed:** 1
- **Entities:** georgics, sermon-on-the-mount, abd-allah-ibn-amir, all-quiet-on-the-western-front, zohar, meditations, rapunzel, town-musicians-of-bremen, crito

### AI Enrichment — 2026-05-17T10:33:01Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** candide, a-farewell-to-arms

### AI Enrichment — 2026-05-17T10:54:38Z

- **Model:** ollama
- **Enriched:** 10 | **Failed:** 0
- **Entities:** eclogues, pham-ngu-lao, book-of-the-later-han, de-rerum-natura, turahan-bey, the-emperors-new-clothes, a-farewell-to-arms, the-adventures-of-sherlock-holmes, life-is-a-dream, the-ugly-duckling

### AI Enrichment — 2026-05-17T11:38:51Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** the-gulag-archipelago, su-shi, the-merchant-of-venice

### AI Enrichment — 2026-05-17T11:49:50Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 0
- **Entities:** the-little-match-girl, watchmen, a-study-in-scarlet, the-gulag-archipelago, les-fleurs-du-mal, su-shi, the-merchant-of-venice, bibliotheca, prose-edda, gospel-of-thomas ... +2 more

### AI Enrichment — 2026-05-17T12:50:52Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** charlotte-guillard, muammad-ibn-ysuf-al-kindi, anglo-saxon-chronicle

### AI Enrichment — 2026-05-17T12:57:34Z

- **Model:** ollama
- **Enriched:** 11 | **Failed:** 0
- **Entities:** the-three-little-pigs, trinity-college-dublin, gonalo-coelho, jtaka, gaspar-de-guzmn-count-duke-of-olivares, periplus-of-the-erythraean-sea, charlotte-guillard, muammad-ibn-ysuf-al-kindi, anglo-saxon-chronicle, metamorphoses ... +1 more

### AI Enrichment — 2026-05-17T14:00:38Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** alatheus, dúnchad-bec, dnchad-bec

### AI Enrichment — 2026-05-17T14:16:46Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** jinasena, shakespeares-sonnets, works-and-days, abd-al-wahhb-ibn-abd-al-raman, neşri, esteban-jos-martnez-fernndez-y-martnez-de-la-sierra, alatheus, dúnchad-bec, dnchad-bec, áed-mac-boanta ... +4 more

### AI Enrichment — 2026-05-17T14:59:49Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** juozas-urbšys, tiberius-julius-cotys-iii

### AI Enrichment — 2026-05-17T15:03:34Z

- **Model:** ollama
- **Enriched:** 10 | **Failed:** 0
- **Entities:** donnchad-mac-gilla-pádraig, donnchad-mac-gilla-pdraig, gayatri-mantra, translation, suibne-menn, owain-ap-hywel, tiberius-julius-cotys-iii, ziaelas-of-bithynia, mithridates-chrestus, dai-jin

### AI Enrichment — 2026-05-17T16:20:54Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** galactorius-of-lescar, henti

### AI Enrichment — 2026-05-17T16:36:21Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** juozas-urbys, ancient-greek, eulpaso, drest-iv, ibn-al-jib, tyrannion, galactorius-of-lescar, neferkare-iv, uranius, henti ... +4 more

### AI Enrichment — 2026-05-17T18:01:45Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 0
- **Entities:** galactorius-of-lescar, uranius, spargapeithes, ibn-khuzaymah, gartnait-iii, drest-i, trebeta, bacurius-i-of-iberia, de-administrando-imperio, álvaro-of-braganza ... +3 more

### AI Enrichment — 2026-05-17T18:46:54Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** donatian-of-reims, vassili-poyarkov, first-epistle-to-the-thessalonians, grabus

### AI Enrichment — 2026-05-17T18:58:57Z

- **Model:** ollama
- **Enriched:** 10 | **Failed:** 0
- **Entities:** king-xian-of-zhou, trdat-of-iberia, john-the-baptist, donatian-of-reims, vassili-poyarkov, first-epistle-to-the-thessalonians, bible, grabus, ardaric, wikimedia-commons

### AI Enrichment — 2026-05-17T19:50:29Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** mantra

### AI Enrichment — 2026-05-17T20:06:46Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 0
- **Entities:** donatian-of-reims, first-epistle-to-the-thessalonians, ælfsige, theophilus-ben-ananus, theuderic-i, mantra, dromichaetes, mihrdat-ii-of-iberia, lucius-calpurnius-piso, robert-of-thourotte ... +5 more

### AI Enrichment — 2026-05-17T22:12:08Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** sharwin-i, emperor-huai-of-jin, mihrdat-iv-of-iberia

### AI Enrichment — 2026-05-17T23:37:34Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** saint-bassian, first-epistle-to-the-corinthians, sigobert-the-lame

### AI Enrichment — 2026-05-17T23:48:28Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 0
- **Entities:** edwin-ap-hywel, sharwin-i, emperor-huai-of-jin, mihrdat-iv-of-iberia, hermas-of-dalmatia, diplomacy, muthis, mihrdat-iii-of-iberia, anushirvan-sharaf-al-maali, fei-shi ... +8 more

### AI Enrichment — 2026-05-18T00:58:42Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** tiberius-julius-rhoemetalces

### AI Enrichment — 2026-05-18T02:16:51Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** buddhism, rainbow, muhyi-al-dn-al-maghrib

### AI Enrichment — 2026-05-18T02:57:59Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** edeko, king-zhao-of-wei, khushnavaz, aimo-of-toul, sehetepkare-intef, gospel-of-philip, buddhism, southern-ocean, muhyi-al-dn-al-maghrib, venerius ... +4 more

### AI Enrichment — 2026-05-18T03:25:34Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 0
- **Entities:** yan-yan, quintus-fabius-vibulanus, mithridates-iii-of-parthia, photography

### AI Enrichment — 2026-05-18T03:53:14Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 0
- **Entities:** mithridates-iii-of-parthia, vortimer, qi-of-xia, hdde, biology, meryhathor, trophimus-of-arles

### AI Enrichment — 2026-05-18T04:51:50Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** shalmaneser-i

### AI Enrichment — 2026-05-18T05:19:53Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 0
- **Entities:** mithridates-iii-of-parthia, guillaume-brionnet, ala-ud-din-masud-shah, imta, shalmaneser-i, almere, antimachus-i, theudebert-i, julianus-pomerius, junius-rusticus ... +2 more

### AI Enrichment — 2026-05-18T05:52:23Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** sobekhotep-iii, domnall-ilchelgach, mang-of-xia, preah-ream-ii, uli-i-of-mali, sölve, slve, ursinus-of-bourges

### AI Enrichment — 2026-05-18T06:06:28Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** ursinus-of-bourges, janbirdi-al-ghazali

### AI Enrichment — 2026-05-18T07:13:52Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** socialism, takelot-i, perdiccas-iii-of-macedon, tai-jia, ariamnes-of-cappadocia

### AI Enrichment — 2026-05-18T07:37:41Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 0
- **Entities:** konstantinos-doukas, middle-east

### AI Enrichment — 2026-05-18T07:56:59Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** kumaragupta-iii, kuzi-teshub, phraates-iii-of-parthia, mutnedjmet, eucratides-ii, eumelus-of-bosphorus, dubricius

### AI Enrichment — 2026-05-18T08:47:10Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 1
- **Entities:** abba-saul, isetemkheb-d, gauscelin-de-jean, enrico-minutoli, innocent-iv, sangara

### AI Enrichment — 2026-05-18T08:55:43Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** gauscelin-de-jean, enrico-minutoli, innocent-iv, sangara

### AI Enrichment — 2026-05-18T09:16:19Z

- **Model:** ollama
- **Enriched:** 17 | **Failed:** 0
- **Entities:** konstantinos-doukas, middle-east, eumelus-of-bosphorus, dubricius, abba-saul, sharek, aulus-licinius-archias, isetemkheb-d, gauscelin-de-jean, enrico-minutoli ... +7 more

### AI Enrichment — 2026-05-18T09:26:48Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** arshak-ii-of-iberia, wigstan, silvio-passerini, sabinus-of-spoleto, prehotep-i, leo-the-mathematician, psusennes-i, antiochus

### AI Enrichment — 2026-05-18T10:16:44Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** oldowan

### AI Enrichment — 2026-05-18T10:21:32Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** mathgamain-mac-cennétig, mathgamain-mac-cenntig, oldowan, arnaud-amalric, neferronpet, benedetto-ii-caetani, optatus

### AI Enrichment — 2026-05-18T10:59:21Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** vachagan-iii, philip-repyngdon, hyechong, francesco-cornaro, maria-pronchishcheva, faustus-of-riez, johann-iv-von-dražice, johann-iv-von-draice

### AI Enrichment — 2026-05-18T11:29:16Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** twosret

### AI Enrichment — 2026-05-18T11:43:12Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** andr-despinay, benedetto-ii-caetani, optatus, vachagan-iii, philip-repyngdon, francesco-cornaro, maria-pronchishcheva, johann-iv-von-dražice, johann-iv-von-draice, apollonius-of-tyre ... +4 more

### AI Enrichment — 2026-05-18T11:50:27Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** apollonius-of-tyre, twosret, aahotepre, luli, organic-chemistry, marcus-fulvius-nobilior, amat-mamu

### AI Enrichment — 2026-05-18T12:24:37Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** patriarch-john-i-of-alexandria, felicia-malipiero, lucius-cassius-hemina, john-randolph-3rd-earl-of-moray, istvn-vrday, biochemistry, saiful-hoque

### AI Enrichment — 2026-05-18T12:40:33Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** michael-bourtzes, malichus-i

### AI Enrichment — 2026-05-18T13:02:57Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 0
- **Entities:** eusebius-of-vercelli, malichus-i, publius-porcius-laeca, giovanni-de-ponte, jorge-da-costa, durand

### AI Enrichment — 2026-05-18T13:53:01Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** nicomedes, zenodorus, john-elton, osorkon-i, sosurim, zhao-mo, tritantaechmes, guido-tarlati

### AI Enrichment — 2026-05-18T13:55:00Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** john-elton, osorkon-i, zhao-mo

### AI Enrichment — 2026-05-18T14:22:39Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 2
- **Entities:** malichus-i, publius-porcius-laeca, paullus-aemilius-lepidus, vitonus, giovanni-de-ponte, jorge-da-costa, durand, john-elton, tritantaechmes, conservatism ... +2 more

### AI Enrichment — 2026-05-18T14:41:09Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** ludovico-bonito, geert-groote, eurozone, alexander-i, rudolf-of-rdesheim, artemidoros, childebert-the-adopted

### AI Enrichment — 2026-05-18T15:13:58Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** artemidoros, childebert-the-adopted

### AI Enrichment — 2026-05-18T15:33:51Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** federico-frezzi, saint-monitor, diocles-of-carystus, kingdom-of-numidia, history-of-rome, lucifer-of-cagliari, ferenc-frangepn

### AI Enrichment — 2026-05-18T16:18:07Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** natural-science, juan-gil-de-hontañón, vithimiris, publius-claudius-pulcher, tommaso-badia, bonfilius, wenennefer, penthelia

### AI Enrichment — 2026-05-18T16:28:12Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** wenennefer, abu-hashim-al-jubbai

### AI Enrichment — 2026-05-18T16:55:21Z

- **Model:** ollama
- **Enriched:** 11 | **Failed:** 0
- **Entities:** spurius-mummius, lucifer-of-cagliari, ferenc-frangepn, juan-gil-de-hontañón, vithimiris, publius-claudius-pulcher, penthelia, abu-hashim-al-jubbai, gaius-fabricius-luscinus, quintus-minucius-thermus ... +1 more

### AI Enrichment — 2026-05-18T17:17:59Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** abu-hashim-al-jubbai, gaius-fabricius-luscinus, quintus-minucius-thermus, martin, gaudentius-of-brescia, dorotheus-of-tyre, adalbero-of-wrzburg, electronics

### AI Enrichment — 2026-05-18T17:37:00Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** adalbero-of-wrzburg, kindattu, planet

### AI Enrichment — 2026-05-18T18:17:23Z

- **Model:** ollama
- **Enriched:** 8 | **Failed:** 0
- **Entities:** kindattu, planet, pietro-gallocia, theophilus-of-caesarea, maurya-empire, kingdom-of-aksum, uruk-period, macrianus-minor

### AI Enrichment — 2026-05-18T18:59:14Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** leukon-ii-of-bosporus, kojiki, bryson-of-achaea

### AI Enrichment — 2026-05-18T21:06:05Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** hestiaeus-of-perinthus, curt-von-stedingk, giovanni-de-primis

### AI Enrichment — 2026-05-18T22:29:36Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** agoracritus

### AI Enrichment — 2026-05-18T22:52:29Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 0
- **Entities:** virgilius-of-arles, alferius, amphicrates-of-athens, adamantius, archil-of-iberia, jakub-plichta, ingenuinus, kazimierz-pac, agoracritus, emperor-ming-of-han ... +3 more

### AI Enrichment — 2026-05-18T23:34:29Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** mery

### AI Enrichment — 2026-05-19T00:50:27Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 0
- **Entities:** alain-chartier, vologases-ii-of-parthia, pietro-foscari, girolamo-doria

### AI Enrichment — 2026-05-19T01:04:20Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 0
- **Entities:** tysilio, quintus-baebius-tamphilus, siro-the-epicurean, guillaume-pellicier, ausiàs-despuig, ausis-despuig, alain-chartier, al-malik-al-rahim, vologases-ii-of-parthia, pietro-foscari ... +3 more

### AI Enrichment — 2026-05-19T01:56:12Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** brics, anarchism, raban-gamaliel-vi

### AI Enrichment — 2026-05-19T03:03:37Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 0
- **Entities:** demetrius-ii-aetolicus, quintus-marcius-philippus, servius-sulpicius-galba, genesius-of-lyon

### AI Enrichment — 2026-05-19T03:25:13Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 0
- **Entities:** tellus-of-athens, ini, nicomedes-iii-of-bithynia, bartatua, demetrius-ii-aetolicus, quintus-marcius-philippus, servius-sulpicius-galba, genesius-of-lyon, gerard-of-csanád, gnter-gaus ... +2 more

### AI Enrichment — 2026-05-19T04:04:55Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** juan-de-cervantes, jaime-de-casanova, postumus-cominius-auruncus, perictione

### AI Enrichment — 2026-05-19T05:16:31Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** leonardo-patrasso, senewosret-ankh

### AI Enrichment — 2026-05-19T06:11:50Z

- **Model:** ollama
- **Enriched:** 17 | **Failed:** 0
- **Entities:** pietro-riario, merymose, nicomedes-iv-of-bithynia, sengann-mac-dela, ciriaco-de-pizzicolli, afro-eurasia, leonardo-patrasso, senewosret-ankh, gaius-licinius-macer, enyego-dvalos ... +7 more

### AI Enrichment — 2026-05-19T06:28:21Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** iuput-i, rabbel-ii-soter, dagobert-iii, enakalle, palladas

### AI Enrichment — 2026-05-19T07:34:45Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** prætextatus, sekhemre-khutawy-sobekhotep, nubel

### AI Enrichment — 2026-05-19T07:36:56Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** prætextatus, sekhemre-khutawy-sobekhotep, nubel

### AI Enrichment — 2026-05-19T08:46:47Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** george-spalatin, naburimannu, the-interpretation-of-dreams, agostino-trivulzio

### AI Enrichment — 2026-05-19T10:15:52Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** juan-lpez, mirocles, peter-ii-novk

### AI Enrichment — 2026-05-19T10:34:00Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 1
- **Entities:** george-maniakes, the-interpretation-of-dreams, agostino-trivulzio, sima-zhao, mirza-yusuf, dervish-khan, muiredach-muinderg, king-mu-of-zhou, honoratus, juan-lópez ... +5 more

### AI Enrichment — 2026-05-19T11:15:34Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** double-falcon, didia, zeno-of-rhodes

### AI Enrichment — 2026-05-19T12:43:15Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** suda, pietro-del-monte

### AI Enrichment — 2026-05-19T13:18:10Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 0
- **Entities:** amantius-of-como, a-dance-with-dragons, a-storm-of-swords, the-adventures-of-tom-bombadil, euthyphro, suda, nepherites-ii, pietro-del-monte, senkamanisken, antonio-bettini ... +5 more

### AI Enrichment — 2026-05-19T13:48:49Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** gaspar-de-guzmán-count-duke-of-olivares, adam-easton, nedjemibre, john-of-procida

### AI Enrichment — 2026-05-19T15:26:09Z

- **Model:** ollama
- **Enriched:** 9 | **Failed:** 0
- **Entities:** nedjemibre, central-african-republic, cosma-orsini, federigo-fregoso, herman-van-horne, mithridates-i-of-iberia, petosiris, thumbelina, enda-of-aran

### AI Enrichment — 2026-05-19T16:09:08Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** pedro-v-of-kongo, álpin-de-dalriada, eastern-europe, schengen-area

### AI Enrichment — 2026-05-19T17:21:03Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** manava, meryibre-khety, duarte-galvão, duarte-galvo

### AI Enrichment — 2026-05-19T18:29:41Z

- **Model:** github
- **Enriched:** 10 | **Failed:** 0
- **Entities:** puerto-rican-independence-party, forbes, fifa, republican-party, democratic-party, renault, lufthansa, intel, yale-university, grupo-televisa

### AI Enrichment — 2026-05-19T19:37:17Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** quintus-minucius-rufus, numerius-fabius-pictor, philibert-hugonet

### AI Enrichment — 2026-05-19T21:22:56Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** iwo-odrowąż, maturinus

### AI Enrichment — 2026-05-19T21:41:48Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 2
- **Entities:** quintus-minucius-rufus, bartolomeo-di-breganze, guiraud, thraseas, jesus-ben-fabus, antonio-ferrero, iwo-odrow, stefano-nardini, john-colet, maturinus ... +2 more

### AI Enrichment — 2026-05-19T22:29:24Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** ascanio-parisani, giovanni-vitelleschi

### AI Enrichment — 2026-05-19T23:40:57Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** jacques-goyon-de-matignon

### AI Enrichment — 2026-05-20T01:03:01Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 2
- **Entities:** juan-de-ziga-y-pimentel, simplician, domninus-of-larissa, yax-ehb-xok, mamurra, publius-valerius-falto, cristoforo-foppa, francesco-crasso, giacomo-simonetta, alessandro-oliva ... +2 more

### AI Enrichment — 2026-05-20T01:09:00Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** husam-al-din-chalabi, hans-ulrich-von-eggenberg, emile-or-on-education

### AI Enrichment — 2026-05-20T02:21:33Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** gaius-claudius-canina, gaius-claudius-marcellus-major

### AI Enrichment — 2026-05-20T04:07:20Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 0
- **Entities:** gaius-claudius-marcellus-major, paolo-emilio-cesi, porphyry-of-gaza, domenico-della-rovere, franciotto-orsini, luis-julian-de-mil, marcello-crescenzi, quintian-of-rodez, ludovico-simonetta, ambrosios-of-alexandria ... +6 more

### AI Enrichment — 2026-05-20T04:54:14Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** francesco-argentino, giovanni-daragona, godefroid-de-claire, boso

### AI Enrichment — 2026-05-20T05:59:53Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** beyond-good-and-evil, nectanebo-ii, francisco-álvares, francisco-lvares

### AI Enrichment — 2026-05-20T06:30:38Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 0
- **Entities:** boso, pierre-desprs, emperor-he-of-han, mirian-iii-of-iberia, syrus-of-genoa, andr-chnier, beyond-good-and-evil, confessions, francisco-lvares, ferrex ... +3 more

### AI Enrichment — 2026-05-20T07:14:21Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** gaius-mamilius-turrinus, protasius, william-petow

### AI Enrichment — 2026-05-20T08:25:22Z

- **Model:** ollama
- **Enriched:** 11 | **Failed:** 0
- **Entities:** marcus-ceionius-silvanus, gaugericus, parallel-lives, bluebeard, piero-vettori, pepin-i-of-aquitaine, king-jun-of-gojoseon, maghan-ii, utbah-ibn-abi-lahab, antipater-of-thessalonica ... +1 more

### AI Enrichment — 2026-05-20T08:28:40Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** pepin-i-of-aquitaine

### AI Enrichment — 2026-05-20T09:30:37Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** sextus-atilius-serranus, john-the-good

### AI Enrichment — 2026-05-20T10:40:05Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** stephen-ii-of-antioch, antonio-cerdà-i-lloscos

### AI Enrichment — 2026-05-20T10:50:46Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 1
- **Entities:** sextus-atilius-serranus, john-the-good, gnaeus-baebius-tamphilus, titus-quinctius-crispinus, timoleon, seychelles, georgia, fazio-giovanni-santori, stephen-ii-of-antioch, proculus-of-verona ... +2 more

### AI Enrichment — 2026-05-20T11:48:27Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** publius-sestius, desiderius-of-vienne

### AI Enrichment — 2026-05-20T14:15:07Z

- **Model:** ollama
- **Enriched:** 19 | **Failed:** 0
- **Entities:** nicetas-of-remesiana, peter-of-benevento, pedro-ferris, jutta-of-kulmsee, cristoforo-della-rovere, shapur-i-shahrvaraz, donnchad-mac-briain, demetrius-iii, brenger-fredoli, donus ... +9 more

### AI Enrichment — 2026-05-20T14:27:08Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** jinheung-of-silla, eochaid-mac-engusa, marcus-furius-fusus, quintus-petillius-spurinus

### AI Enrichment — 2026-05-20T15:45:26Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** antiochus-nikator

### AI Enrichment — 2026-05-20T17:12:00Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 0
- **Entities:** zisi, gay-science, antiochus-nikator, fiacha-cennfinnán, fiacha-cennfinnn, drest-mac-caustantín, drest-mac-caustantn, meenakshi, lake-baikal, gaius-fabius-dorso-licinus ... +5 more

### AI Enrichment — 2026-05-20T17:17:28Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** marcus-sempronius-tuditanus, gaius-marcius-censorinus, lucius-caninius-gallus, zambia

### AI Enrichment — 2026-05-20T18:45:40Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** attilio-piccioni

### AI Enrichment — 2026-05-20T20:01:06Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** fortunatianus-of-aquileia, girolamo-seripando, philippe-de-la-chambre

### AI Enrichment — 2026-05-20T20:23:07Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 0
- **Entities:** attilio-piccioni, herillus, gregory-of-elvira, yazdegerd-i, geumwa-of-buyeo, abu-al-hasan-ali, reality, nukualofa, quintus-fulvius-flaccus, decimus-junius-brutus ... +8 more

### AI Enrichment — 2026-05-20T21:07:49Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** snaaib, caribbean-sea, antipater-of-sidon

### AI Enrichment — 2026-05-20T22:32:07Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** tiberius-minucius-augurinus, gnaeus-domitius-calvinus-maximus, publius-popillius-laenas, ludwig-andreas-von-khevenhller

### AI Enrichment — 2026-05-20T22:54:19Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 0
- **Entities:** dumnagual-iii-of-alt-clut, sextus-aelius-paetus-catus, gaius-annius-anullinus, tiberius-minucius-augurinus, gnaeus-domitius-calvinus-maximus, publius-popillius-laenas, ludwig-andreas-von-khevenhüller, ludwig-andreas-von-khevenhller, gondulphus-of-metz, diomede-carafa ... +5 more

### AI Enrichment — 2026-05-20T23:33:36Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** kanishka-ii

### AI Enrichment — 2026-05-20T23:39:23Z

- **Model:** ollama
- **Enriched:** 9 | **Failed:** 0
- **Entities:** publius-popillius-laenas, nicholas-kallikles, mark, homeric-hymns, age-of-enlightenment, kanishka-ii, rhodri-mawr, king-you-of-zhou, demetrius-the-fair

### AI Enrichment — 2026-05-21T00:48:34Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** clemente-grosso-della-rovere, ptolemy-philadelphus

### AI Enrichment — 2026-05-21T00:52:50Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** homeric-hymns, sataspes, servius-sulpicius-rufus, gaius-licinius-geta, appius-claudius-crassus, lucius-cornelius-merula, lucius-volcatius-tullus, gnaeus-aufidius-orestes, clemente-grosso-della-rovere, leonardo-grosso-della-rovere ... +4 more

### AI Enrichment — 2026-05-21T01:51:42Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 0
- **Entities:** polyxenos-epiphanes-soter, cristvo-jacques, gatianus-of-tours, stephen-i, lucius-tarutius-firmanus, the-memoirs-of-sherlock-holmes, cat-on-a-hot-tin-roof, the-return-of-sherlock-holmes, the-prophet, sint-maarten ... +3 more

### AI Enrichment — 2026-05-21T02:00:10Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** the-prophet, covid-19-pandemic, jan-hasitejnsk-of-lobkowicz

### AI Enrichment — 2026-05-21T02:45:23Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** gastronomy

### AI Enrichment — 2026-05-21T03:15:43Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 0
- **Entities:** jan-hasištejnský-of-lobkowicz, nicolò-albertini, nicol-albertini, iytjenu, micronesia, theagenes-of-thasos, publius-cornelius-cossus, titus-flavius-petro, marcus-quinctilius-varus, proculus-verginius-tricostus-rutilus ... +6 more

### AI Enrichment — 2026-05-21T03:41:40Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** sophroniscus, l-hin-tng

### AI Enrichment — 2026-05-21T04:37:35Z

- **Model:** ollama
- **Enriched:** 20 | **Failed:** 0
- **Entities:** southern-italy, sophroniscus, l-hin-tng, quintian-of-rodez, francis-of-brunswick-wolfenbttel, alejandro-orfila, murat-karayaln, germania, mithridates-ii-of-commagene, gabaro ... +10 more

### AI Enrichment — 2026-05-21T04:47:13Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** bernardo-clesio, modest, euthalius

### AI Enrichment — 2026-05-21T05:54:31Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** vande-mataram, genetics

### AI Enrichment — 2026-05-21T06:26:35Z

- **Model:** ollama
- **Enriched:** 13 | **Failed:** 3
- **Entities:** aphrodisius, the-birth-of-tragedy, ecce-homo, genetics, anat-her, fú-jiān, vasudeva-ii, tiridates-iii-of-parthia, mihrdat-v-of-iberia, drest-v ... +3 more

### AI Enrichment — 2026-05-21T08:17:46Z

- **Model:** ollama
- **Enriched:** 20 | **Failed:** 0
- **Entities:** a-streetcar-named-desire, f-jin, gnaeus-cornelius-scipio-hispallus, quintus-sulpicius-camerinus-cornutus, lucius-cornelius-lentulus-caudinus, albero-i-of-louvain, rinaldo-piscicello, nicola-da-guardiagrele, niccolò-fortiguerra, niccol-fortiguerra ... +10 more

### AI Enrichment — 2026-05-21T08:19:03Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** mershepsesre-ini-ii, nicolaes-molenaer

### AI Enrichment — 2026-05-21T09:57:34Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 0
- **Entities:** nicolaes-molenaer, publius-manlius-capitolinus, publius-cornelius-lentulus-caudinus, gnaeus-servilius-caepio, benedict-i, giovanni-castiglione, galeotto-franciotti-della-rovere, bartolomeo-roverella, hlias-de-saint-yrieix, muneko-naishinn ... +6 more

### AI Enrichment — 2026-05-21T10:38:08Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** quintus-ogulnius-gallus

### AI Enrichment — 2026-05-21T10:46:22Z

- **Model:** ollama
- **Enriched:** 10 | **Failed:** 0
- **Entities:** andronicus-of-olynthus, quintus-ogulnius-gallus, servius-cornelius-maluginensis-cossus, marcus-titius, anthony-neyrot, james-of-pecorara, honoratus-of-amiens, marcantonio-bobba, phlegon-of-marathon, world-war-ii

### AI Enrichment — 2026-05-21T11:40:32Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** song-higyng

### AI Enrichment — 2026-05-21T11:43:25Z

- **Model:** ollama
- **Enriched:** 12 | **Failed:** 0
- **Entities:** marcus-titius, priscus, jakub-of-nin, apollodorus-the-epicurean, parkinsons-law, rumplestiltskin, song-hŭigyŏng, song-higyng, pepi-iii, duke-of-ye ... +2 more

### AI Enrichment — 2026-05-21T12:58:33Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** marcus-valerius-messalla-rufus, leochares

### AI Enrichment — 2026-05-21T13:02:23Z

- **Model:** ollama
- **Enriched:** 14 | **Failed:** 0
- **Entities:** ka, manapa-tarhunta, rhodogune-of-parthia, oxford, martim-afonso-de-sousa, marcus-calpurnius-flamma, publius-cornelius-rufinus, marcus-valerius-messalla-rufus, andrea-matteo-palmieri, gabriele-de-gabrielli ... +4 more

### AI Enrichment — 2026-05-21T14:30:36Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 0
- **Entities:** marco-vigerio-della-rovere, laodice-v, guy-par, geoffrey-of-vendme, pere-oller, acron, nyuserre-ini, king-xiaowen-of-qin, amanitenmemide, peter-ii-of-aragon ... +5 more

### AI Enrichment — 2026-05-21T15:18:34Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** teodoro-paleologo-di-montferrato, conrad-of-ascoli, the-tale-of-genji

### AI Enrichment — 2026-05-21T16:05:54Z

- **Model:** ollama
- **Enriched:** 10 | **Failed:** 1
- **Entities:** anselm-of-lucca, teodoro-paleologo-di-montferrato, conrad-of-ascoli, franca-visalta, lycophron, euenus, the-pilgrims-progress, udaya-iii-of-anuradhapura, orodes-iv-of-elymais, east-asia

### AI Enrichment — 2026-05-21T16:23:19Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** east-asia, françois-marie-de-broglie-1st-count-of-broglie, franois-marie-de-broglie-1st-count-of-broglie

### AI Enrichment — 2026-05-21T17:24:53Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** juan-castellar-y-de-borja, maifreda-da-pirovano

### AI Enrichment — 2026-05-21T17:48:35Z

- **Model:** ollama
- **Enriched:** 15 | **Failed:** 1
- **Entities:** publius-sulpicius-saverrio, marcus-acilius-glabrio, theodwin, guido-of-acqui, anna-koltovskaya, grard-du-puy, giovanni-stefano-ferrero, juan-castellar-y-de-borja, girolamo-verallo, nurul-huq-bhuiyan ... +5 more

### AI Enrichment — 2026-05-21T18:42:06Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** gojoseon, meles-of-lydia

### AI Enrichment — 2026-05-21T20:01:23Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** lucius-roscius-fabatus, marcus-porcius-cato, roger-of-cannae, christiern-pedersen

### AI Enrichment — 2026-05-21T20:39:09Z

- **Model:** ollama
- **Enriched:** 19 | **Failed:** 0
- **Entities:** gojoseon, gwangjong-of-goryeo, tranquillina, perdiccas-ii-of-macedon, vinekh-of-bulgaria, central-europe, gaius-julius-mento, lucius-roscius-fabatus, flavius-dionysius, marcus-porcius-cato ... +9 more

### AI Enrichment — 2026-05-21T21:17:41Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** shoshenq-i, seqenenre-tao

### AI Enrichment — 2026-05-21T22:14:53Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** titus-quinctius-crispinus-sulpicianus

### AI Enrichment — 2026-05-21T22:42:53Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 0
- **Entities:** the-rime-of-the-ancient-mariner, ethics, archigenes, nulji-of-silla, xiang-of-xia, laodice-i, artabasdos, pythagoras-of-samos, gaius-fundanius-fundulus, lucius-titinius-pansa-saccus ... +8 more

### AI Enrichment — 2026-05-21T23:23:13Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** eucherius-of-orléans, eucherius-of-orlans

### AI Enrichment — 2026-05-23T21:00:16Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** csar-destres, bartolom-ordez, joseph-emmanuel-de-la-trmoille

### AI Enrichment — 2026-05-23T21:17:06Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** bartolom-ordez

### AI Enrichment — 2026-05-23T21:35:32Z

- **Model:** gemini
- **Enriched:** 21 | **Failed:** 4
- **Entities:** alfonso-daz-de-montalvo, jos-nicols-de-azara, gaspard-thodore-mollien, dietrich-von-blow, ignacio-de-arteaga-y-bazn, rome-de-villeneuve, ng-s-lin, rimini, johannes-hltz, joaqun-surez ... +11 more

### AI Enrichment — 2026-05-23T22:52:26Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** francesco-sassetti

### AI Enrichment — 2026-05-23T23:34:33Z

- **Model:** gemini
- **Enriched:** 2 | **Failed:** 23
- **Entities:** domenico-rosselli, kreimir-i-of-croatia

### AI Enrichment — 2026-05-23T23:36:30Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** baldassare-estense

### AI Enrichment — 2026-05-24T00:01:55Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 0
- **Entities:** francesco-sassetti, jules-louis-bol-marquis-de-chamlay, lorenzo-iv-surez-de-figueroa-y-crdoba, baldassare-estense, odo-of-cluny, anton-reinhard-falck, friedrich-von-müller, philibert-babou-de-la-bourdaisire, macas, l-tc-tng ... +8 more

### AI Enrichment — 2026-05-24T00:42:13Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** stephen-of-besanon, trajan-the-patrician

### AI Enrichment — 2026-05-24T01:17:34Z

- **Model:** gemini
- **Enriched:** 2 | **Failed:** 23
- **Entities:** cornelis-van-aarsens, juan-ramn-balcarce

### AI Enrichment — 2026-05-24T01:38:23Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 0
- **Entities:** joris-van-spilbergen, stephen-of-besanon, trajan-the-patrician, david-mallet, marie-melchior-joseph-thodose-de-lagren, gervase-of-canterbury, ibn-khalaf-al-muradi, robert-barnes, juan-fernndez-de-velasco-5th-duke-of-fras, naili-abdullah-paşa ... +8 more

### AI Enrichment — 2026-05-24T01:43:30Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** ibn-khalaf-al-muradi

### AI Enrichment — 2026-05-24T09:26:46Z

- **Model:** gemini
- **Enriched:** 20 | **Failed:** 0
- **Entities:** egbert-ii-of-kent, franco-sacchetti, anna-svensdotter, luca-fancelli, alvarus-pelagius, willem-boreel, toktu-of-bulgaria, eiludd-powys, matteo-villani, petar-hektorović ... +10 more

### AI Enrichment — 2026-05-24T09:51:08Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** gilles-li-muisis, yavuz-blent-bkiler, lon-bouthillier-comte-de-chavigny, george-hamilton-seymour

### AI Enrichment — 2026-05-24T10:45:19Z

- **Model:** gemini
- **Enriched:** 4 | **Failed:** 16
- **Entities:** maria-da-conceio-nobre-cabral, charles-de-marillac, iago-ab-idwal, vasili-pronchishchev

### AI Enrichment — 2026-05-24T11:38:13Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** rhys-ab-owain, titus-julius-priscus, waldo-of-reichenau

### AI Enrichment — 2026-05-24T12:03:21Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** taddeo-gaddi

### AI Enrichment — 2026-05-24T13:16:53Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** league-of-arab-states, nicholas-of-clamanges, thrasymachus, muayyad-al-din-al-urdi

### AI Enrichment — 2026-05-24T13:25:27Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** agnes-ii

### AI Enrichment — 2026-05-24T14:15:49Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** franz-von-pillersdorf, domingo-martínez-de-irala, murat-beg-tardić

### AI Enrichment — 2026-05-24T14:51:48Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 0
- **Entities:** august-heinrich-hermann-von-dönhoff, satire

### AI Enrichment — 2026-05-24T15:34:10Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** adam-of-balsham, history-of-europe, paleontology, united-airlines, zionism

### AI Enrichment — 2026-05-24T16:05:39Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** girolamo-lucchesini

### AI Enrichment — 2026-05-24T16:08:30Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** zionism

### AI Enrichment — 2026-05-24T17:02:30Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** stefano-de-normandis-dei-conti, antonio-maria-ciocchi-del-monte, girolamo-basso-della-rovere

### AI Enrichment — 2026-05-24T17:43:48Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** lotharius-van-hochstaden

### AI Enrichment — 2026-05-24T18:31:42Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 2
- **Entities:** monimus, anselm-of-besate

### AI Enrichment — 2026-05-24T18:46:46Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** beirut

### AI Enrichment — 2026-05-24T19:20:00Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** osanna-of-mantua, ardicino-della-porta-iuniore, eskil-of-lund, john-of-epiphania

### AI Enrichment — 2026-05-24T20:55:45Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** edmund-lockyer, patrocles, ernest-i-of-schauenburg

### AI Enrichment — 2026-05-24T21:28:27Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** henry-percy-3rd-earl-of-northumberland

### AI Enrichment — 2026-05-24T22:28:17Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** bit, ivan-yevreinov, lucius-afranius

### AI Enrichment — 2026-05-24T23:25:45Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** sphaerus, philippe-de-mézières

### AI Enrichment — 2026-05-25T00:08:14Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** pietro-senex

### AI Enrichment — 2026-05-25T00:15:24Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** mnesikles

### AI Enrichment — 2026-05-25T01:11:03Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** alexander-barclay, gaspar-de-valos-de-la-cueva, johannes-manardus

### AI Enrichment — 2026-05-25T01:31:21Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** anthelm-of-belley

### AI Enrichment — 2026-05-25T02:07:50Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** konrad-witz, allergy, leo-rhabdouchos

### AI Enrichment — 2026-05-25T02:49:15Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** girolamo-aleandro

### AI Enrichment — 2026-05-25T03:18:02Z

- **Model:** gemini
- **Enriched:** 18 | **Failed:** 2
- **Entities:** lucius-aemilius-regillus, marcus-fulvius-flaccus, mjej-ii-gnuni, tiberius-claudius-nero, gilbert-de-clare-1st-earl-of-pembroke, numerius-fabius-buteo, pietro-diana, gabriele-rangone, judoc-ii-of-romberk, agericus ... +8 more

### AI Enrichment — 2026-05-25T04:13:05Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** domnall-donn

### AI Enrichment — 2026-05-25T04:36:40Z

- **Model:** gemini
- **Enriched:** 2 | **Failed:** 18
- **Entities:** konstantin-von-benckendorff, lourenço-de-almeida

### AI Enrichment — 2026-05-25T05:04:30Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** leodamas-of-thasos, erastus-of-scepsis, daniel-of-morley, jacopo-passavanti

### AI Enrichment — 2026-05-25T06:27:57Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** didius-julianus, dorothea-of-brandenburg-duchess-of-mecklenburg, jacopo-piccolomini-ammannati

### AI Enrichment — 2026-05-25T07:09:27Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** appius-claudius-russus

### AI Enrichment — 2026-05-25T07:58:56Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** august-kestner, michał-jerzy-mniszech, jan-jacobszoon-may-van-schellinkhout

### AI Enrichment — 2026-05-25T09:40:05Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** denis-i-of-portugal, juan-maria-schuver, filippo-pigafetta

### AI Enrichment — 2026-05-25T10:01:29Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** hernando-de-aragn-y-gurrea

### AI Enrichment — 2026-05-25T10:31:36Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** zhan-ruoshui, aetius

### AI Enrichment — 2026-05-25T11:12:04Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** wilhelm-gnapheus, gaudenzio-ferrari

### AI Enrichment — 2026-05-25T12:04:55Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** æthelstan-of-sussex, cailtram, ruben-iii-prince-of-armenia

### AI Enrichment — 2026-05-25T12:43:25Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 0
- **Entities:** hywel-ap-ieuaf, samuel-hearne

### AI Enrichment — 2026-05-25T13:34:34Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** anacharsis, mazda, democedes

### AI Enrichment — 2026-05-25T15:01:29Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** quintus-sulpicius-camerinus-praetextatus, leonardo-foscolo, firmus, neoptolemus, quintus-fabius-maximus-eburnus

### AI Enrichment — 2026-05-25T16:40:43Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** die-linke, william-elphinstone

### AI Enrichment — 2026-05-25T17:29:29Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** stefano-pignatelli, theophanes-the-greek, yu-huan

### AI Enrichment — 2026-05-25T18:08:01Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** kuiper-belt

### AI Enrichment — 2026-05-25T18:08:27Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 0
- **Entities:** hugh-of-saint-cher, phlegon-of-tralles

### AI Enrichment — 2026-05-25T18:56:16Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** gaius-marcius-rutilus, lucius-minucius-esquilinus-augurinus

### AI Enrichment — 2026-05-25T19:37:52Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 2
- **Entities:** publius-manlius-vulso

### AI Enrichment — 2026-05-25T20:25:52Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 4
- **Entities:** antonius-andreas

### AI Enrichment — 2026-05-25T21:11:20Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 1
- **Entities:** george-of-trebizond, girolamo-mazzola-bedoli, giovanni-francesco-mormando

### AI Enrichment — 2026-05-25T22:05:16Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** giandomenico-spinola, rolling-stone

### AI Enrichment — 2026-05-25T22:55:15Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** quintus-poetelius-libo-visolus, eutychianus, gaius-livius-salinator

### AI Enrichment — 2026-05-25T23:31:46Z

- **Model:** gemini
- **Enriched:** 2 | **Failed:** 18
- **Entities:** polymedes-of-argos, gian-giacomo-dolcebuono

### AI Enrichment — 2026-05-26T00:28:42Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** visconte-maggiolo, johann-heß, dinus-de-rossonis, domenico-silvio-passionei, muhammad-ali-al-halabi

### AI Enrichment — 2026-05-26T00:50:31Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** biagio-assereto

### AI Enrichment — 2026-05-26T01:16:03Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** seventh-day-adventist-church, citron

### AI Enrichment — 2026-05-26T01:55:42Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** sancha-of-portugal, fernando-de-valds-y-salas, lorenzo-raggi

### AI Enrichment — 2026-05-26T02:40:56Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** george-ix-of-kartli, heaberht-of-kent, wu-guang, cristóvão-de-mendonça

### AI Enrichment — 2026-05-26T03:04:23Z

- **Model:** gemini
- **Enriched:** 8 | **Failed:** 12
- **Entities:** cornelis-evertsen-the-elder, diego-hurtado-de-mendoza-y-quiñones, mario-theodoli, eanbald-ii, baccio-bandinelli, andrea-della-robbia, rashid-al-din-hamadani, demetrius-the-cynic

### AI Enrichment — 2026-05-26T03:13:34Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** mario-lago

### AI Enrichment — 2026-05-26T03:56:22Z

- **Model:** gemini
- **Enriched:** 8 | **Failed:** 12
- **Entities:** matteo-di-andrea-de-pasti, jacopo-di-cione, diomedes-of-tarsus, romanian, mario-lago, nikolay-firyubin, william-richard-hamilton, yakov-malik

### AI Enrichment — 2026-05-26T04:35:40Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** giovanni-andrea-archetti, federico-sforza, carlo-gualterio, annibale-albani

### AI Enrichment — 2026-05-26T05:57:02Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** niall-caille, hendrick-hamel, garcía-lópez-de-cárdenas

### AI Enrichment — 2026-05-26T06:33:04Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** girolamo-verospi

### AI Enrichment — 2026-05-26T06:35:52Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 0
- **Entities:** marcin-kazanowski, sigered-of-kent

### AI Enrichment — 2026-05-26T07:29:08Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 3
- **Entities:** nicholas-of-autrecourt

### AI Enrichment — 2026-05-26T07:52:56Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** lelio-falconieri

### AI Enrichment — 2026-05-26T08:20:34Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 3
- **Entities:** quintus-caecilius-metellus-balearicus, gerard-callenburgh

### AI Enrichment — 2026-05-26T08:59:34Z

- **Model:** ollama
- **Enriched:** 2 | **Failed:** 1
- **Entities:** gnaeus-domitius-calvinus, franz-sznayde

### AI Enrichment — 2026-05-26T09:10:21Z

- **Model:** gemini
- **Enriched:** 1 | **Failed:** 19
- **Entities:** józef-potocki

### AI Enrichment — 2026-05-26T09:53:14Z

- **Model:** ollama
- **Enriched:** 4 | **Failed:** 1
- **Entities:** lodovico-piavi, frederick-howard-5th-earl-of-carlisle, jan-lutek, jaan-teemant

### AI Enrichment — 2026-05-26T10:39:19Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 2
- **Entities:** orazio-giustiniani, etienne-de-poissy, cesare-facchinetti

### AI Enrichment — 2026-05-26T11:30:15Z

- **Model:** ollama
- **Enriched:** 5 | **Failed:** 0
- **Entities:** hierocles-of-alexandria, julius-pomponius-laetus, berenguer-de-montagut, hezbollah, muḥammad-b-ibrāhīm-b-saʿīd-shams-al-dīn-abū-ʿabda-al-anṣārī

### AI Enrichment — 2026-05-26T13:00:59Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 1
- **Entities:** marcus-fabius-ambustus

### AI Enrichment — 2026-05-26T13:50:20Z

- **Model:** ollama
- **Enriched:** 17 | **Failed:** 0
- **Entities:** marcus-fabius-ambustus, gaius-coelius-caldus, ulderico-carpegna, simone-paltanieri, theodora-of-arta, veríssimo-de-lencastre, hans-leonhard-schäufelein, bicci-di-lorenzo, liu-yuxi, seongjong ... +7 more

### AI Enrichment — 2026-05-26T13:55:35Z

- **Model:** ollama
- **Enriched:** 1 | **Failed:** 0
- **Entities:** gaius-coelius-caldus

### AI Enrichment — 2026-11-07T15:57:26Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 2
- **Entities:** bodh-gaya, quintus-servilius-structus-priscus, antigonus-i-monophthalmus, yadail-dharih-i, rufinus-of-byzantium, bertha-of-artois

### AI Enrichment — 2026-11-07T16:02:11Z

- **Model:** ollama
- **Enriched:** 3 | **Failed:** 0
- **Entities:** antigonus-i-monophthalmus, gaius-plautius-proculus, publius-servilius-priscus-structus

### AI Enrichment — 2026-11-07T17:06:49Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** annales-veteris-testamenti, philogonius-of-antioch, postumus-aebutius-helva-cornicen, socrates-chrestus, pamphilus-of-alexandria, enrique-de-cardona-y-enríquez, enrique-de-cardona-y-enrquez

### AI Enrichment — 2026-11-07T17:07:31Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 2
- **Entities:** annales-veteris-testamenti, philogonius-of-antioch, postumus-aebutius-helva-cornicen, socrates-chrestus, pamphilus-of-alexandria, enrique-de-cardona-y-enríquez

### AI Enrichment — 2026-11-07T17:14:21Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 2
- **Entities:** mirian-ii-of-iberia, pêro-da-covilhã, epistle-of-jude, quotations-from-chairman-mao-tse-tung, gitanjali, beli-ab-eiludd

### AI Enrichment — 2026-11-07T17:25:13Z

- **Model:** ollama
- **Enriched:** 7 | **Failed:** 1
- **Entities:** pro-da-covilh, beli-ab-eiludd, eletu-kekere, saint-servatius, lucius-saenius-balbinus, lucius-furius-medullinus, gurguit-barbtruc

### AI Enrichment — 2026-11-07T19:20:35Z

- **Model:** ollama
- **Enriched:** 22 | **Failed:** 2
- **Entities:** ishanavarman-ii, tudhaliya-ii, sin-iddinam, geography, pelagius-ii, haito, matteo-ii-visconti, giovanni-battista-consiglieri, pier-paolo-vergerio, paulinus-i-of-aquileia ... +12 more

### AI Enrichment — 2026-11-07T19:41:07Z

- **Model:** ollama
- **Enriched:** 20 | **Failed:** 4
- **Entities:** nashwn-ibn-sad-al-imyar, hori-ii, alessandro-cesarini, marino-caracciolo, john-of-gorze, mostar, newel-k-whitney, symmachus, fan-jian, publius-lucretius-tricipitinus ... +10 more

### AI Enrichment — 2026-11-07T20:22:25Z

- **Model:** ollama
- **Enriched:** 6 | **Failed:** 2
- **Entities:** jie-of-xia, marcus-valerius-volusus, orlando-furioso, falco-of-maastricht, guy-de-bourgogne, reniero-zeno

### AI Enrichment — 2026-11-07T21:25:36Z

- **Model:** ollama
- **Enriched:** 41 | **Failed:** 7
- **Entities:** herintsalama-rajaonarivelo, munju, helü, hel, kalinga-magha, ostrogota, andromachus-the-elder, methodius-of-olympus, ailbe-of-emly, simon-islip ... +31 more

### AI Enrichment — 2026-11-07T22:13:30Z

- **Model:** ollama
- **Enriched:** 42 | **Failed:** 6
- **Entities:** jarosław-duke-of-opole, odysseas-androutsos, andrea-vanni, antnio-martins-de-chaves, qiu-ying, lucius-verginius-tricostus-esquilinus, manius-rabuleius, conrad-i-of-salzburg, menkheperre, david-beaton ... +32 more

### AI Enrichment — 2026-11-07T22:54:15Z

- **Model:** ollama
- **Enriched:** 41 | **Failed:** 7
- **Entities:** manius-rabuleius, gudrid-thorbjarnardóttir, antipater-of-bostra, giacomo-colonna, ludovico-prodocator, nicol-da-ponte, basseterre, anthimus-of-nicomedia, celestine-iv, ibn-abi-al-khisal ... +31 more

### AI Enrichment — 2026-11-08T00:43:56Z

- **Model:** ollama
- **Enriched:** 19 | **Failed:** 1
- **Entities:** hip-hop, rhetoric, richard-of-saint-victor, idomeneus-of-lampsacus, emilian-of-cogolla, cleopatra-selene-ii, bademus, caius, eunomius-of-cyzicus, felix-iii ... +9 more

### AI Enrichment — 2026-11-08T01:31:11Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 2
- **Entities:** peder-mnsson, ed-dub-mac-colmin, adrastus-of-aphrodisias, argonautica, mani, the-pillow-book, eardwulf-of-kent, aelius-donatus, shah-jalal, ismenias ... +8 more

### AI Enrichment — 2026-11-08T01:38:49Z

- **Model:** ollama
- **Enriched:** 54 | **Failed:** 10
- **Entities:** theagenes-of-rhegium, murat-beg-tardi, john-iv-of-saxe-lauenburg, reginald-pecock, mesh-ki-ang-gasher, papulus, john-ix, sakir-har, adi-ibn-zayd, gobryas ... +44 more

### AI Enrichment — 2026-11-08T02:25:51Z

- **Model:** ollama
- **Enriched:** 16 | **Failed:** 4
- **Entities:** mul-of-kent, thoros-i-prince-of-armenia, constitutional-monarchy, book-of-mormon, gomoarius, mahinda-iv-of-anuradhapura, eystein-halfdansson, nguanamthom, al-fadl-ibn-abbas, wilhelm-von-brandenburg ... +6 more

### AI Enrichment — 2026-11-08T03:13:44Z

- **Model:** ollama
- **Enriched:** 55 | **Failed:** 9
- **Entities:** lucius-cornificius, wadjkare, oenopides, stabat-mater, lucius-apronius, mul-of-kent, thoros-i-prince-of-armenia, constitutional-monarchy, book-of-mormon, gomoarius ... +45 more

### AI Enrichment — 2026-11-08T03:14:14Z

- **Model:** ollama
- **Enriched:** 19 | **Failed:** 1
- **Entities:** comet, yiran-qaghan, playboy, ichasagua, hippalus, sigismondo-gonzaga, joseph-of-freising, guillaume-fillastre, nostrianus, pero-fernandes-sardinha ... +9 more

### AI Enrichment — 2026-11-08T04:02:04Z

- **Model:** ollama
- **Enriched:** 20 | **Failed:** 0
- **Entities:** don-quixote, ansovinus, clement-iii, benedict-ix, epiphanius-of-pavia, boniface-vi, trechn, benedict-vi, boniface-ii, lian-po ... +10 more

### AI Enrichment — 2026-11-08T05:15:12Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** a-portrait-of-the-artist-as-a-young-man, reinbern, felix-i, tiberius-aemilius-mamercinus, danish, mac-grine, alfonso-iv-of-len, giambattista-orsini, severus-of-trier, kheti-v ... +20 more

### AI Enrichment — 2026-11-08T05:21:02Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** juliana-falconieri, yoga-sutras-of-patanjali, pieter-nanninck, evagrius-of-antioch, quintus-fabius-vibulanus-ambustus, titus-geganius-macerinus, mac-gréine, alfonso-iv-of-león, vologases-i-of-parthia, imyremeshaw ... +19 more

### AI Enrichment — 2026-11-08T05:44:11Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** jan-latalski, bertrand-de-saint-martin, agnes-dharcourt, amico-agnifili, maximus-of-turin, john-i-sanudo, ecgberht-of-kent, french-southern-and-antarctic-lands, romen, baga ... +21 more

### AI Enrichment — 2026-11-08T05:44:43Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** epistle-to-the-romans, pomponius-porphyrion, rhuddfedel-frych, ennio-filonardi, henut-taui, nicolas-rolin, hugh-of-poitiers, youtab, yaqub-ibn-ishaq-al-israili, justin ... +20 more

### AI Enrichment — 2026-11-08T06:17:23Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** jn-arason, bülbül-hatun, publius-calvisius-tullus-ruso, sopater-of-apamea, wenceslaus-ii-of-bohemia, andrés-de-urdaneta, domenico-morosini, comita-of-gallura, givi-amilakhvari, head-of-state ... +18 more

### AI Enrichment — 2026-11-08T06:17:36Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** jn-arason, archbishop-sisinnius-i-of-constantinople, bülbül-hatun, hallstatt-culture, bernold, marcus-aemilius-barbula, lou-jing, alpin-de-châlons, arnošt-of-pardubice, landolfo-brancaccio ... +18 more

### AI Enrichment — 2026-11-08T06:39:24Z

- **Model:** ollama
- **Enriched:** 32 | **Failed:** 0
- **Entities:** censorius, reggae, andronikos-doukas, niqmaddu-ii, robert-bylot, novatian, sergius-paulus, shō-sei, pelagio-galvani, university-of-cambridge ... +22 more

### AI Enrichment — 2026-11-08T06:47:08Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** king-xiao-of-zhou, rhun-ab-arthgal, garca-lpez-de-crdenas, ottaviano-degli-ubaldini, arnot-of-pardubice, john-maffey-1st-baron-rugby, gindibu, gjon-buzuku, parnajom-of-iberia, titus-romilius-rocus-vaticanus ... +17 more

### AI Enrichment — 2026-11-08T07:05:53Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** blbl-hatun, fastida, flavius-salia, maximianus-of-ravenna, hanalaa, giovanni-domenico-de-cupis, aure, bogumił, vindex, marcus-octavius ... +18 more

### AI Enrichment — 2026-11-08T07:08:36Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** victor-maurus, second-epistle-to-the-corinthians, acesias, baldwin-of-alna, pesakh, michael-palaiologos, nicholas-of-šalčininkai, buldus, artabanus-iv-of-parthia, francisco-roldán ... +21 more

### AI Enrichment — 2026-11-08T07:38:40Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** diana-degli-andalò, pietro-accolti, al-ashraf, lamprus-of-athens, hablum, breage, wang-san-ak, arnulf-of-chocques, mascezel, ciniod-ii ... +19 more

### AI Enrichment — 2026-11-08T07:40:52Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** stanisław-kostka-czartoryski, jan-čapek-of-sány, ciniod-i, tobias-el-khazen, leo-phokas-the-younger, haka-of-oahu, cynddylan, paulo-da-gama, leonardo-dati, bucolus ... +17 more

### AI Enrichment — 2026-11-08T08:10:47Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** second-epistle-to-the-corinthians, notker-of-liège, thrasaric, françoise-damboise, wartislaw-vii-duke-of-pomerania, conall-cóel, dondup-tseten-dorje, andouin-aubert, alexander-iv, pietro-lippomano ... +19 more

### AI Enrichment — 2026-11-08T08:22:08Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** harald-grenske, dream-of-the-red-chamber, hydrology, parsman-v-of-iberia, marianus-ii-of-torres, george-herbert, alessandro-mattei, neferkare-ninth-dynasty, book-of-revelation, gnaeus-genucius-augurinus ... +15 more

### AI Enrichment — 2026-11-08T08:45:23Z

- **Model:** ollama
- **Enriched:** 32 | **Failed:** 0
- **Entities:** finnian-of-moville, future, li-su, conaire-cóem, cecilia-of-normandy, croesus, julian-of-le-mans, fulcran, titus-verginius-tricostus-rutilus, flavius-caper ... +22 more

### AI Enrichment — 2026-11-08T08:48:01Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** manuel-pessanha, zacharias-rhetor, kingdom-of-the-netherlands, publius-sestius-capitolinus-vaticanus, barom-reamea, duan-xingzhi, timocharis, giovanni-giacomo-sclafenati, clement-ii, lucas-watzenrode ... +18 more

### AI Enrichment — 2026-11-08T09:15:53Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** spotify, sláine-mac-dela, osmund-of-sussex, vsishka, william-melton, memnon-of-rhodes, ceretic-of-elmet, gohard-of-nantes, paul-iii, hetepheres-i ... +20 more

### AI Enrichment — 2026-11-08T09:19:21Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** conall-cel, lucius-quinctius-cincinnatus, alexander-vi, metrodorus-of-chios, halime-sultan, neanthes-of-cyzicus, piotr-i, hafz-mehmed-paa, sláine-mac-dela, obez ... +19 more

### AI Enrichment — 2026-11-08T09:45:54Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** memnon-of-rhodes, vasos-mavrovouniotis, cybi, wigmund, psychoanalysis, publius-carisius, cathal-mac-edo, pekahiah, pahemnetjer, guglielmo-fieschi ... +20 more

### AI Enrichment — 2026-11-08T09:51:59Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** aghatai-khan, quintus-claudius-quadrigarius, gonzalo-de-mendoza, albert-suerbeer, marcus-valerius-messalla-messallinus, vāsishka, aemilius-asper, dedumose-i, harkhuf, celestine-i ... +17 more

### AI Enrichment — 2026-11-08T10:11:40Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** ashot-iii-of-armenia, hyginus, shahi-tegin, augustine-grimaldi, agathinus, conchobar-mac-tadg, werburgh, yin-mo, roman-danylovich, childebert-i ... +18 more

### AI Enrichment — 2026-11-08T10:26:24Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** ceretic-guletic, virius-lupus, the-communist-manifesto, khasekhemwy, stefano-palosti-de-verayneris, frumar, dedumose-ii, ibrhm-al-fazr, european-free-trade-association, darius-ii ... +20 more

### AI Enrichment — 2026-11-08T10:42:18Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ceretic-guletic, mahipala-ii, barisone-iii-of-torres, benignus-of-todi, baal-i, yarlaganda, matteuccia-de-francesco, angelus-of-jerusalem, koskowola, valerius-gratus ... +17 more

### AI Enrichment — 2026-11-08T11:06:25Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** hesiod, zoilus-i, jan-andruszewicz, sauve-damiens, mei-bo, george-i-of-imereti, colmn-of-dromore, miriam-altman, appius-claudius-caudex, blcaire-mac-gofrith ... +19 more

### AI Enrichment — 2026-11-08T11:07:14Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ateas, austromoine, wacław-wierzbicki, huni, pierre-thiam, fngen-mac-edo-duib, du-qiong, odo-arpin-of-bourges, philip-i-count-of-savoy, bardo ... +17 more

### AI Enrichment — 2026-11-08T11:34:26Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** sneferka, hortar, latina, krzysztof-chodkiewicz, jános-forgách, claffone, pharasmanes-iii-of-iberia, argishti-i-of-urartu, ushshi, marone ... +20 more

### AI Enrichment — 2026-11-08T11:37:20Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** asander, hymn, eutocius-of-ascalon, libon, ursula-of-mnsterberg, bongsang, agum-i, ponhea-yat, coel-hen, tatian ... +16 more

### AI Enrichment — 2026-11-08T12:08:34Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** publius-volumnius-amintinus-gallus, obodas-iii, cunobeline, tróndur-í-gøtu, felix-of-como, ptahmose-son-of-menkheper, alberic-of-utrecht, napoleone-orsini-frangipani, lucius-annaeus-cornutus, mogadishu ... +16 more

### AI Enrichment — 2026-11-08T12:11:18Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** guillaume-court, jacopo-sadoleto, virtue, gaius-suetonius-paulinus, lollianus-mavortius, atlanersa, theudemeres, cellach-mac-máele-coba, hkun-law, aspacures-ii-of-iberia ... +15 more

### AI Enrichment — 2026-11-08T13:09:11Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** titus-aurelius-fulvus, antiochis, theodora-komnene, matthäus-lang-von-wellenburg, astorgio-agnensi, vetranio, fei-yao, kunzang, pelopidas, lucius-antonius ... +20 more

### AI Enrichment — 2026-11-08T13:09:22Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** tiptakzi, cellach-mac-mele-coba, juan-díaz-de-solís, hilary-of-arles, ibn-hibban, buddhamitra, traianus, alexander-neville, publius-cornelius-rutilus-cossus, báetán-mac-muirchertaig ... +19 more

### AI Enrichment — 2026-11-08T17:13:41Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 21 | **Failed:** 0
- **Entities:** marcus-manilius, pang-juan, quintus-sextius, sassetta, alexander-neville, darius-the-mede, crinagoras-of-mytilene, calimerius, marguerite-doingt, ulrich-of-zell ... +11 more

### AI Enrichment — 2026-11-08T13:26:34Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** dafydd-gam, daduhepa, ariogaisus, great-britain, humbert-of-romans, crinagoras-of-mytilene, cardiology, social-media, hanno-the-elder, betn-mac-muirchertaig ... +18 more

### AI Enrichment — 2026-11-08T13:42:30Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** caesar-of-dyrrhachium, castritian, republic-of-artsakh, dappula-i-of-anuradhapura, ptolemy-eupator, andries-bicker, paleolithic, ferenc-frangepán, lucius-lucretius-tricipitinus, constantine-iii-of-gallura ... +21 more

### AI Enrichment — 2026-11-08T13:51:22Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** gerolamo-emiliani, caesar-of-dyrrhachium, castritian, manuele-zaccaria, republic-of-artsakh, ulrich-of-zell, sassetta, hans-putmans, henri-de-la-tour-dauvergne-duke-of-bouillon, kharbashikhu ... +19 more

### AI Enrichment — 2026-11-08T14:16:27Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** coroebus-of-elis, kenneth-f-smith, urzigurumash, apollodorus-of-phaleron, henry-iii-of-brunswick-lüneburg, mirian-i-of-iberia, burnaburiash-i, albert-of-mainz, albino, merobaudes ... +18 more

### AI Enrichment — 2026-11-08T14:31:32Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** bocchus-i, wang-dayuan, stanisaw-chodecki, sthryth, jima-of-silla, euphemia-of-racibrz, theodorus-of-asine, khosrau-iii, robert-i-count-of-hesbaye, 1918-1920-flu-pandemic ... +16 more

### AI Enrichment — 2026-11-08T14:37:48Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** hans-putmans, rieul, rusa-i, raimondo-della-torre, antoine-bohier-du-prat, coirpre-cromm-mac-crimthainn, euphemia-of-racibórz, sankhenre-sewadjtu, joaqun-setant, womens-rights ... +16 more

### AI Enrichment — 2026-11-08T15:05:49Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** spártokos-ii, publius-sempronius-tuditanus, cissa-of-sussex, niccolò-perotti, philippus-de-caserta, rajadhi-rajasinha-of-kandy, grattius, saint-aye, sextus-lucilius-bassus, zidanta-ii ... +17 more

### AI Enrichment — 2026-11-08T15:25:35Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** avitus-of-vienne, henry-iii-of-england, francesco-chieregati, cynric-of-wessex, joaquín-setantí, zidanta-ii, gundekar-ii-of-eichsttt, zuo-si, metaphysics, diarmait-mac-nna-meic-murchada ... +18 more

### AI Enrichment — 2026-11-08T15:27:14Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** ireland, constantine-iii-of-abkhazia, anthemiolus, nineteen-eighty-four, eannatum-ii, computer-monitor, giovanni-salviati, anaxilas, cold-war, bentivenga-da-bentivengi ... +15 more

### AI Enrichment — 2026-11-08T15:43:03Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** humban-haltash-ii, eleanor-of-anjou-queen-of-sicily, vercingetorix, tyrrhenian-sea, alexander-iii, lucius-afinius-gallus, jabi-of-silla, ashur-nirari-iii, oswald-von-wolkenstein, mutim-ibn-adi ... +20 more

### AI Enrichment — 2026-11-08T16:05:58Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** giovanni-salviati, hildebold, gaius-servilius-geminus, anastasius-iv, asteroid-belt, demetrius-i-soter, henry-of-blois, so-tom, brendan-the-navigator, sebestyn-archbishop-of-esztergom ... +20 more

### AI Enrichment — 2026-11-08T16:13:00Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** burnaburiash-i, tadc-mac-briain, gregory-i, bato-of-dardania, diuma, rudolf-i, kutir-nahhunte-iv, pepi-ii, southeast-asia, rené-de-prie ... +19 more

### AI Enrichment — 2026-11-08T16:22:59Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** saint-alice, robert-pullen, myron-of-sicyon, georg-hesler, polycrates-of-ephesus, charles-of-provence, alexander-ypsilantis, arsaces-ii-of-parthia, dong-xi, macrian ... +20 more

### AI Enrichment — 2026-11-08T16:40:31Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** humban-haltash-ii, artoces-of-iberia, cristina-daughter-of-edward-the-exile, pedro-fernández-manrique, quintus-petilius-secundus, rajyapala, zoticus-of-constantinople, st-ada, marcus-of-viterbo, manius-valerius-maximus-messalla ... +21 more

### AI Enrichment — 2026-11-08T16:50:24Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** dong-xi, eulogius-of-córdoba, fot, ordoo-iv-of-len, muhammad-hayat-al-sindi, ramiro-iii-of-león, alusian-of-bulgaria, john-of-nepomuk, teles-of-megara, arsinoe-iii-of-egypt ... +18 more

### AI Enrichment — 2026-11-08T17:02:54Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** dong-xi, narcissus-of-girona, polyaenus-of-lampsacus, the-city-of-god, artaxias-i-of-iberia, manius-valerius-maximus-messalla, bernat-calbó, gabriel-de-gramont, lacedaemonius, khosrau-the-usurper ... +18 more

### AI Enrichment — 2026-11-08T17:18:24Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** philo-of-alexandria, sextus-quinctilius, loarn-mac-eirc, anna-of-kashin, sitriuc-mac-mair, jean-françois-de-la-trémoille, arsinoe-i, bernat-calb, alahis, parthenius-of-lampsacus ... +21 more

### AI Enrichment — 2026-11-08T17:37:41Z

- **Model:** ollama
- **Enriched:** 23 | **Failed:** 9
- **Entities:** enyego-dàvalos, sextus-quinctilius, daniel-the-stylite, docimus, jean-françois-de-la-trémoille, sunifred, mustafa-al-misbah, eugenius-of-carthage, titus-quinctius-atta, tiberius-julius-abdes-pantera ... +13 more

### AI Enrichment — 2026-11-08T17:38:43Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** eugenius-of-carthage, ingvar-the-far-travelled, ealdwulf-of-sussex, herjólfur-bárðarson, odgar, perseus, apringius, soraya-hakuziyaremye, amara-dunqas, saint-pothinus ... +19 more

### AI Enrichment — 2026-11-08T17:58:17Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** ardabur, geoffrey-ii-of-villehardouin, takamuko-no-kuromaro, neferka, gratus-of-aosta, ipuki, melchior-von-meckau, sigfred, ageladas, garcía-de-loaysa ... +19 more

### AI Enrichment — 2026-11-08T18:18:36Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** ahmad-ibn-rustah, demetrius-of-thessaloniki, telecles, hugh-of-remiremont, anna-of-bulgaria, illus, ivan-dmitriev, śabara, publius-cornelius-lentulus-sura, urtak ... +19 more

### AI Enrichment — 2026-11-08T18:27:51Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** ahmad-ibn-rustah, ptracu-cel-bun, titus-vinius, beatrice-of-ornacieux, tiberius-julius-theothorses, demetrius-of-thessaloniki, the-fox-and-the-grapes, angelo-sanudo, cassian-of-imola, maximilian-of-lorch ... +19 more

### AI Enrichment — 2026-11-08T18:42:30Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** tiberius-julius-sauromates-i, gunther, maximus, aribert-archbishop-of-milan, himilco-fameas, gonario-i-of-lacon-gunale, ariobarzanes-i-of-cappadocia, messius-phoebus-severus, felix-ii, demophilus-of-thespiae ... +17 more

### AI Enrichment — 2026-11-08T22:58:40Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 26 | **Failed:** 0
- **Entities:** ulpius-marcellus, sextus-catius-clementinus-priscillianus, peter-kreimir-iv-of-croatia, arab-spring, ibn-al-dawadari, pierre-de-la-vergne, françois-joachim-de-pierre-de-bernis, acragas, ali-ibn-abi-bakr-al-harawi, giovanni-di-casali ... +16 more

### AI Enrichment — 2026-11-08T19:02:13Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ludvig-holberg, bartolomé-de-la-cueva-y-toledo, saint-ingrid-of-sknninge, ur-ningirsu-ii, izadgushasp, khaba, llywelyn-ap-merfyn, emperor-xian-of-han, sobekemsaf-i, quintus-fabius-memmius-symmachus ... +17 more

### AI Enrichment — 2026-11-08T23:04:54Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 24 | **Failed:** 0
- **Entities:** hélie-de-bourdeilles, malnutrition, eurasian-economic-union, alv-erlingsson, jerome, conakry, vettius-agorius-basilius-mavortius, spirituality, eochaid-mac-áeda-find, pasion ... +14 more

### AI Enrichment — 2026-11-08T19:16:56Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** florian-geyer, ea-mukin-zeri, min-saw-mon, bala-i, gaius-antistius-reginus, zoilus, djedankhre-montemsaf, æthelstan-of-kent, ottaviano-riario, arno-of-salzburg ... +17 more

### AI Enrichment — 2026-11-08T19:17:44Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** lucius-valerius-messalla-thrasea-priscus, nomus, john-stewart-1st-earl-of-atholl, han-fei, corentin-of-quimper, miltiades, bamako, appian, hovhannès-ier-mandakouni, marcus-junius-silanus-torquatus ... +21 more

### AI Enrichment — 2026-11-08T19:42:46Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** so-tom-and-prncipe, mac-gréine, johann-gottfried-herder, lucius-furius-purpureo, jerome, umar-al-aqta, joseph-ben-ephraim-karo, first-epistle-to-timothy, easter-island, stephen-harding ... +18 more

### AI Enrichment — 2026-11-08T19:54:18Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** nomus, bernard-of-vienne, dou-xian, imi, centwine-of-wessex, wenceslaus-ii-of-legnica, charles-i-de-croÿ, jan-gruszczyński, an-nasir-ahmad, diogenes-of-sinope ... +18 more

### AI Enrichment — 2026-11-08T19:55:26Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** parthenius-of-lampsacus, ibn-hud, rabbi-ishmael, nuya, 3, pierre-desprès, wu-ban, conall-mac-áedáin, berthold-of-hanover, marcus-genucius-augurinus ... +19 more

### AI Enrichment — 2026-11-08T20:26:54Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** lucius-manlius-torquatus, phylarchus, otto-i-of-olomouc, emperor-huan-of-han, francesco-francia, przemysaw-of-owicim, publius-aelius-ligus, hormizd-vi, jan-gruszczyski, caesaria-of-arles ... +17 more

### AI Enrichment — 2026-11-08T20:38:18Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** anders-sunesen, marcus-minucius-rufus, rawn-ibn-muammad-al-st, kalokyros-delphinas, juvenal-of-narni, mamercus-aemilius-mamercinus, zdislava-from-lemberk, said-ibn-amir-al-jumahi, petar-hektorovi, erik-gnupsson ... +18 more

### AI Enrichment — 2026-11-08T20:41:16Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** diego-gelmírez, shahabuddin-delawar, phayllos-of-croton, raḍwān-ibn-muḥammad-al-sāʻātī, antoninus-of-florence, orlkur-runlfsson, dafydd-ab-owain-gwynedd, charles-i-de-cro, agilulfus-of-cologne, hugoln-gavlovi ... +18 more

### AI Enrichment — 2026-11-08T21:11:44Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** kalokyros-delphinas, agnes-of-bavaria, heinrich-isaac, sextus-of-chaeronea, henrique-dias, soffredo, caesarius-of-arles, mikoaj-iii-radziwi, neferkare-pepiseneb, gebhard-iii-of-constance ... +17 more

### AI Enrichment — 2026-11-08T21:15:24Z

- **Model:** ollama
- **Enriched:** 19 | **Failed:** 1
- **Entities:** rodrigo-de-bastidas, brard-de-got, netflix, volcatius-sedigitus, hugolín-gavlovič, eadberht-of-lindisfarne, cleopatra-ii-of-egypt, kamose, bartholomew-columbus, aerodynamics ... +9 more

### AI Enrichment — 2026-11-08T21:23:47Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** bjarni-herjlfsson, yan-liang, amina-inloes, teutamus, jayapangus, abān-ibn-saʻīd, lanarote-de-freitas, mikołaj-iii-radziwiłł, pietro-capocci, information-technology ... +20 more

### AI Enrichment — 2026-11-08T21:28:14Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** amina-inloes, leontios, edmund-abaka, zeno-of-citium, mellonius, popular-culture, gabriel-franchre, maximus-i-of-constantinople, am-thrse-joseph-masclet, messenger ... +18 more

### AI Enrichment — 2026-11-08T21:57:21Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** emperor-xuan-of-han, maredudd-ab-owain-ab-edwin, smundr-fri, neurology, human-sexuality, skilurus, cybernetics, csar-gabriel-de-choiseul, gaius-memmius-regulus, marcus-gratidius ... +17 more

### AI Enrichment — 2026-11-08T22:03:50Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** agrippinus-of-naples, colmán-of-lindisfarne, sabou-kem, neutron-star, johannes-soreth, andronicus-of-pannonia, geomorphology, creoda-of-wessex, visual-basic, pandolfo-masca-of-pisa ... +16 more

### AI Enrichment — 2026-11-08T22:13:10Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** konrad-iii-the-old, rahotep, the-metamorphosis, kōtoku, celio-calcagnini, newaya-krestos, unitary-state, mahikeng, pertinax, fergus-mac-echdach ... +18 more

### AI Enrichment — 2026-11-08T22:27:25Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** harivarman-ii, finan-of-lindisfarne, riccardo-petroni, julius-iii, tibullus, voice-over-ip, literacy, sigtrygg-gnupasson, bernhard-von-breydenbach, thales ... +20 more

### AI Enrichment — 2026-11-08T22:41:02Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** lysimachus, aleksandr-bakunin, intellectual-property, sechnassach, dilmun, svatopluk-duke-of-bohemia, neferefre, niccolò-leoniceno, phaedrus, francis-of-brunswick-wolfenbüttel ... +20 more

### AI Enrichment — 2026-11-08T23:03:38Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** nishandji-tadji-zade-djafer-elebi, durandus-of-saint-pourain, pierre-franois-hugues-dhancarville, purana-kassapa, marcus-livius-salinator, fyodor-minin, stanislaus-of-szczepanw, dracula, amalgaid-mac-éndai, hermogenian ... +17 more

### AI Enrichment — 2026-11-08T23:15:43Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** king-zhaoxiang-of-qin, marcus-livius-salinator, nicols-de-cardona, astrometry, ulysses, ali-ibn-hammud-al-nasir, philip-i-of-croÿ-chimay, abu-shama-al-maqdiss, neferirkare-kakai, henry-iii-prince-of-anhalt-aschersleben ... +18 more

### AI Enrichment — 2026-11-08T23:18:35Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** nicholas-of-ilok, niall-mac-eochada, gotthard-of-hildesheim, pride-and-prejudice, maximianus, talorgan-ii, glappo, leo-i-of-cava, gaspar-de-bracamonte-3rd-count-of-pearanda, rudolf-of-zhringen ... +19 more

### AI Enrichment — 2026-11-08T23:47:25Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** sextus-pompeius-festus, niccolò-de-niccoli, hipponicus-iii, jayasimha-siddharaja, asser-thorkilsson, r, ordoo-lvarez, lorenz, kapila, publius-postumius-albus-regillensis ... +15 more

### AI Enrichment — 2026-11-08T23:56:22Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** johannes-ockeghem, hydrography, war-and-peace, mandane-of-media, franois-ducaud-bourget, 55, microeconomics, moby-dick, man-ibn-zaida-al-shaybani, domingo-martnez-de-irala ... +19 more

### AI Enrichment — 2026-11-09T00:01:26Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** ilulu, gjin-gazulli, sambhaji, anna-of-hohenstaufen, marcus-herennius-picens, victor-of-solothurn, maha-sawa, amedi, mirim-elebi, juan-de-borja-lanzol-de-roman-el-mayor ... +16 more

### AI Enrichment — 2026-11-09T00:21:45Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** heinrich-gro-von-trockau, louis-of-teck, william-worcester, 34, computer-programming, lucius-aemilius-paullus-macedonicus, nabarzanes, marcantonio-zimara, nanum, alonso-de-fonseca-y-ulloa ... +19 more

### AI Enrichment — 2026-11-09T00:40:39Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** noman-bashir, gunderic, pamphilus-of-sulmona, isa-kelemechi, david-buchan, jakub-of-żnin, lucius-antistius-vetus, mallorca, robert-brionnet, linguistics ... +18 more

### AI Enrichment — 2026-11-09T00:41:34Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** remmius-palaemon, the-adventures-of-pinocchio, lambert-iii, apion, netherlands, william-ii-of-athens, sanj, lubentius, philipp-von-neumann, libertarianism ... +17 more

### AI Enrichment — 2026-11-09T01:00:15Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** lambert-iii, arnaud-de-pellegrue, theism, materials-science, paschal, arnail-franois-marquis-de-jaucourt, sicard-of-benevento, attilanus-of-zamora, adam-reiner, treaty-of-brest-litovsk ... +20 more

### AI Enrichment — 2026-11-09T01:13:18Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** theodorus-priscianus, george-duke-of-brunswick-lneburg, leotychidas-ii, oliver-von-paderborn, emirate, diagonal, amsicora, john-of-segovia, gérard-du-puy, andalò-del-negro ... +18 more

### AI Enrichment — 2026-11-09T01:23:25Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** oligarchy, bernardim-ribeiro, jon-kuvlung, gratian, nemesianus, lolita, andal-del-negro, g7, anund, wiching ... +21 more

### AI Enrichment — 2026-11-09T01:25:47Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** abu-shama-al-maqdiss, samuel-aba, juan-de-borja-lanzol-de-romaní-el-mayor, senn-mac-geirrcinn, gaius-antistius-vetus, althias, nuño-sánchez, epistle-to-the-colossians, kgyoku, theodore-of-mopsuestia ... +15 more

### AI Enrichment — 2026-11-09T05:36:53Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 12 | **Failed:** 0
- **Entities:** islamism, childrens-literature, lucius-aelius-stilo-praeconinus, physical-geography, soviet-afghan-war, heraclides-lembus, rajah-sulayman, donatus-magnus, john-of-wildeshausen, louis-gabriel-du-buat-nanay ... +2 more

### AI Enrichment — 2026-11-09T05:43:28Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 22 | **Failed:** 0
- **Entities:** echembrotus, patricia-may-urza, human-evolution, book-of-habakkuk, mahajanapada, nivard, infanta-philippa-of-coimbra, charles-erskine, gerard-geldenhouwer, cem-sultan ... +12 more

### AI Enrichment — 2026-11-09T05:49:50Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 20 | **Failed:** 0
- **Entities:** publius-petronius-turpilianus, loureno-de-almeida, ímar-ua-ímair, krešimir-i-of-croatia, pieter-nuyts, burchard-i, carlo-domenico-del-carretto, gil-de-torres, ferdinando-marescalchi, konstantinos-maliasenos ... +10 more

### AI Enrichment — 2026-11-09T02:09:27Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** theodor-von-sitten, valerian-ii, mieszko-bolesławowic, johannes-martini, eleazar-of-worms, madame-bovary, sophia-of-bavaria, clovis-iv, scopas, reinald ... +17 more

### AI Enrichment — 2026-11-09T02:11:10Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** basolus, john-raoul-petraliphas, herman-i-margrave-of-baden, narrative, software-engineering, jijeung-of-silla, lawrence-of-portugal, an-nasir-muhammad-ibn-qaitbay, heraclides-lembus, nicholas-iv ... +19 more

### AI Enrichment — 2026-11-09T02:21:53Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** sosigenes-of-alexandria, spurius-carvilius-maximus, fei-yi, jayavarman-i, veterinary-medicine, albert-of-louvain, soviet-afghan-war, john-of-wildeshausen, neferkasokar, patricia-may-urza ... +17 more

### AI Enrichment — 2026-11-09T02:42:14Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** berardo-dei-marsi, walter-of-palearia, bertrada-of-prm, federico-wanga, thomas-basin, mehmed-iv, parody, gnaeus-pinarius-cornelius-clemens, laodice-vii-thea, yarim-lim-of-alalakh ... +20 more

### AI Enrichment — 2026-11-09T02:56:51Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** aulus-hirtius, cristbal-vaca-de-castro, donat-de-besanon, hermann-of-dorpat, fula, scythia, muammad-ibn-abb, goeric, jan-dymitr-solikowski, brian-urquhart ... +20 more

### AI Enrichment — 2026-11-09T02:59:42Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** owain-goch-ap-gruffydd, theodotus-of-antioch, ren-charles-de-maupeou, timor, paul-wolff-metternich, varese, roseline-de-villeneuve, paeonius-of-ephesus, domenico-grimani, cadwallon-ab-ieuaf ... +15 more

### AI Enrichment — 2026-11-09T03:24:03Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** joão-gonçalves-zarco, tydfil, harry-potter-and-the-deathly-hallows, nepotian-of-asturias, senusret-iv, ricsige-of-northumbria, micha-jerzy-mniszech, musicology, theodwin-of-liège, andreas-van-cuijk ... +18 more

### AI Enrichment — 2026-11-09T03:33:46Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** jakob-salomon-bartholdy, vsevolod-ii-of-kiev, slavomr, emperor-yuan-of-han, john-of-heinsberg, stanisaw-mateusz-rzewuski, johannes-von-baysen, uriel-grka, ithobaal-ii, albertanus-of-brescia ... +17 more

### AI Enrichment — 2026-11-09T03:47:38Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** adl-lgnj, hermaeus, lucius-passienus-rufus, pausanias-of-orestis, loe-thai, othmar, simon-mepeham, numenius-of-apamea, geodesy, maría-a-balteira ... +18 more

### AI Enrichment — 2026-11-09T04:14:43Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** gaius-of-milan, adrianus-petit-coclico, willigis, árni-þorláksson, otbert-of-lige, manuc-bei-mirzoyan, berenguer-de-cruïlles, quakers, han-mynghoe, alessandro-leopardi ... +14 more

### AI Enrichment — 2026-11-09T04:16:30Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** karibil-watar-i, commonwealth-of-independent-states, quintus-cloelius-siculus, wigbold-von-holte, pao-ching-yen, pomponius-of-naples, mara-a-balteira, grigorios-of-antioch, rolandino-of-padua, stephen-of-besançon ... +17 more

### AI Enrichment — 2026-11-09T04:30:57Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** willigis, basque, k-g-ambegaonkar, marcantonio-barbaro, delft, abū-kāmil-shujāʿ-ibn-aslam, shalmaneser-iv, stna-airt, radboud-of-utrecht, frederick-iv-of-baden ... +14 more

### AI Enrichment — 2026-11-09T04:51:53Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** selbach-mac-ferchair, guy-du-faur-seigneur-de-pibrac, nechtan-morbet, fernando-snchez-de-tovar, guido-da-velate, ermengarde-of-burgundy, smund-kresson, íte-of-killeedy, marcus-valerius-messala-corvinus, jan-van-virneburg ... +17 more

### AI Enrichment — 2026-11-09T04:53:46Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** decimus-haterius-agrippa, den, magnacar, nicanor-of-stageira, flavius-bauto, kiya-afrasiyab, gopala-iii, alypius, theoderich-von-wied, saint-modoald ... +19 more

### AI Enrichment — 2026-11-09T05:09:35Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** fan-zhen, lucius-caecilius-metellus-denter, johann-iii-romka, one-hundred-years-of-solitude, billboard, quintus-pompeius-sosius-falco, leontius-of-caesarea, xenophanes, jericho, gaius-fonteius-capito ... +18 more

### AI Enrichment — 2026-11-09T05:23:59Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** guido-da-velate, chrodobert, cadwgan-ap-bleddyn, francis-wogan-festing, semi-presidential-system, franois-savary-de-brves, lucius-caesonius-ovinius-manilius-rufinianus-bassus, agostino-giustiniani, musical, hamilcar-barca ... +21 more

### AI Enrichment — 2026-11-09T05:38:10Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** gaius-fonteius-capito, jonas-i-losovičius, diogo-soares, marcus-antonius-creticus, bartolom-torres-naharro, william-of-saliceto, shusha, priarius, gruffudd-fychan-i, bidoux-pregent ... +15 more

### AI Enrichment — 2026-11-09T05:48:26Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** thomas-ebendorfer, guan-daosheng, solina-nyirahabimana, the-prince, salomea-of-poland, castries, bárid, zina-kalay-kleitman, polyperchon, urbice-of-metz ... +17 more

### AI Enrichment — 2026-11-09T06:11:11Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** ivan-moskvitin, friedrich-von-zollern, skalla-grímr, senenmut, jaya-harivarman-i, james-lancaster, funmilade-akingbagbohun, blessed-beatrice-deste, byzantium, plechelm ... +16 more

### AI Enrichment — 2026-11-09T06:12:16Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** gynaecology, jhalkaribai, giovanni-battista-del-tasso, yudra-nyingpo, violant-of-bar, gmundur-plsson, ustad-isa, ono-no-imoko, chaldea, tedald ... +19 more

### AI Enrichment — 2026-11-09T06:25:42Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** merdjefare, hazard-analysis-and-critical-control-points, philippe-emmanuel-duke-of-mercœur, quintus-lucretius-vespillo, áurea-of-san-millán, rhodo, pll-jnsson, heinrich-xiii-prince-reuss-of-greiz, quintus-marcius-turbo, eochaid-son-of-rhun ... +19 more

### AI Enrichment — 2026-11-09T06:50:28Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** lucius-caecilius-metellus-denter, alexander-de-brus, publius-silius-nerva, environmental-protection, destiny, regelinda, pierre-sylvain-rgis, beslan, onomacles, kabir ... +16 more

### AI Enrichment — 2026-11-09T06:56:00Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** eochaid-son-of-rhun, sebestyn-tindi-lantos, crimean-khanate, antonio-cornazzano, south-china-sea, giorgio-valla, fadrique-lvarez-de-toledo, katyayana, ankara, wacaw-seweryn-rzewuski ... +16 more

### AI Enrichment — 2026-11-09T07:04:25Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** plutocracy, acadmie-franaise, jacobus-de-teramo, yan-hui, jaromr, vtsyyana, aulus-plautius, john-dominici, al-rabi-ibn-yunus, juan-de-lava ... +17 more

### AI Enrichment — 2026-11-09T07:30:33Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** bai-renfu, franciszek-krasiski, bangla, tatadim, lucius-postumius-albinus-megellus, ed-alln, lund, robert-ii-of-capua, marianus-i-of-torres, edmund-burke ... +15 more

### AI Enrichment — 2026-11-09T07:31:57Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** niketas-chalkoutzes, franciszek-krasiski, ulfilas, ernest-ii-of-saxony, irish-sea, yagbeu-seyon, maria-da-conceição-nobre-cabral, sewadjkare-iii, vmara-peres, palindrome ... +18 more

### AI Enrichment — 2026-11-09T07:44:37Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** abul-fadl-al-balami, robert-of-nantes, tatadim, english, cosmic-microwave-background, gómez-manrique, anushirvan-ibn-khalid, james-of-baux, cassius-chaerea, konstantinos-laskaris ... +20 more

### AI Enrichment — 2026-11-09T08:12:03Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** determinism, limit, khosrow-ii, sebastian-maggi, vedast, vezhan-buzmihr, hugo-van-lannoy, macedonian, civil-engineering, francisco-galcerán-de-lloris-y-de-borja ... +17 more

### AI Enrichment — 2026-11-09T08:16:35Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** theodotus-of-byzantium, isidore-of-chios, physiology, ralph-montagu-1st-duke-of-montagu, haneefah-adam, graph-theory, muammad-b-ibrhm-b-sad-shams-al-dn-ab-abda-al-anr, elara, faustus-of-mileve, niccolò-dacciapaccio ... +17 more

### AI Enrichment — 2026-11-09T08:23:09Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** gilles-i-aycelin-de-montaigut, william-the-hardy-lord-of-douglas, biometrics, nikolaos-of-otranto, francisco-galcern-de-lloris-y-de-borja, abdullah-ibn-hudhafah-as-sahmi, lydia-of-thyatira, orophernes-of-cappadocia, antiochus-of-ascalon, gustav-trolle ... +20 more

### AI Enrichment — 2026-11-09T08:55:27Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** franchinus-gaffurius, engelberga, aron, international-labour-organization, appius-annius-trebonius-gallus, alessandro-della-spina, christian-günther-von-bernstorff, john-peckham, abd-al-wid-al-marrkush, aribo ... +19 more

### AI Enrichment — 2026-11-09T08:56:27Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** landnmabk, heraldry, frothar-of-toul, alesso-baldovinetti, myspace, sebastianus, ivan-osterman, konstanty-ostrogski, juan-del-encina, jacob-of-mies ... +19 more

### AI Enrichment — 2026-11-09T08:58:16Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** icelandic, zaradust-e-khuragen, fort-de-france, flavius-appalius-illus-trocundes, joo-fernandes, caspar-aquila, lucius-papirius-mugillanus, ʻabd-al-wāḥid-al-marrākushī, acts-of-the-apostles, ebremaro-di-thérouanne ... +16 more

### AI Enrichment — 2026-11-09T09:31:27Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** jordi-dornós, eusebius-of-myndus, safiyyah-bint-abd-al-muttalib, amazasp-ii-of-iberia, andrzej-zebrzydowski, immunology, anthimos-gazis, csar-oudin, biophysics, dōjo-nyūdōshinnō ... +19 more

### AI Enrichment — 2026-11-09T09:35:03Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** gorgonius, richard-foxe, zhang-xuan, raymond-nonnatus, piotr-dunin, henry-vii-of-england, albert-ii-duke-of-austria, odo-of-cambrai, book-of-tobit, ponç-hug-iv-count-of-empúries ... +19 more

### AI Enrichment — 2026-11-09T09:42:45Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** richard-foxe, apostles-creed, seraphina-sforza, tryphiodorus, phaedrus-the-epicurean, csar-oudin, tang-jian, acharya-vamana, esteban-fernández-de-castro, jan-žižka ... +17 more

### AI Enrichment — 2026-11-09T10:14:50Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** tamagnino, siena, constantine-lempereur-van-oppyck, pon-hug-iv-count-of-empries, pal-engjëlli, marcus-cluvius-rufus, theophiliscus, hugues-de-lionne, presbyterianism, diego-lopez-de-pacheco-2nd-duke-of-escalona ... +18 more

### AI Enrichment — 2026-11-09T10:16:14Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** aelius-gallus, eudorus-of-alexandria, sneferu, gaius-silius, jan-ika, sigismund-albicus, venevisin, tielman-susato, cognition, rudolf-van-diepholt ... +17 more

### AI Enrichment — 2026-11-09T10:28:20Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** odo-of-cambrai, dominican-order, wuthering-heights, enhegal, hierocles, kingdom-of-prussia, gil-gonzález-dávila, panini, ida-of-toggenburg, joseph-roettiers ... +15 more

### AI Enrichment — 2026-11-09T10:53:25Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** lithuanian, attala, joseph-bonomi-the-younger, william-of-tripoli, 1-maccabees, gaspare-del-fosso, synesius-of-cyrene, david-alopaeus, albert-pighius, second-book-of-kings ... +19 more

### AI Enrichment — 2026-11-09T10:57:53Z

- **Model:** ollama
- **Enriched:** 18 | **Failed:** 2
- **Entities:** thomas-elmham, hyecho, gandhara, christian-detlev-reventlow, jakov-lukarevi, federation, paul-of-burgos, priscus-of-epirus, bupalus, sharaf-al-zaman-al-marwazi ... +8 more

### AI Enrichment — 2026-11-09T11:03:11Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** dang-hyang-nirartha, jan-joosten-van-lodensteijn, swithun, margaret-of-castello, pedro-rodrguez, john-doukas, sir-george-staunton-2nd-baronet, jørgen-sadolin, juan-boscán-almogáver, david-anhaght ... +16 more

### AI Enrichment — 2026-11-09T11:28:13Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** wendjebauendjed, robert-i-of-burgundy, cockburn-town, giovanni-battista-zeno, philoxenus-of-mabbug, brochwel-ysgithrog, world-meteorological-organization, iberomaurusian, lucius-fulvius-curvus, benedictines ... +21 more

### AI Enrichment — 2026-11-09T11:37:56Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** hud, giuseppe-archinto, matthäus-schiner, jean-i, philip-stanhope-4th-earl-of-chesterfield, the-washington-post, gaius-julius-erucius-clarus-vibianus, maurice-de-saxe, valentinian-iii, simon-kenton ... +20 more

### AI Enrichment — 2026-11-09T11:47:57Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** quintus-caecilius-metellus-pius-scipio-nasica, theravda, spiridon-lusi, shedsu-nefertum, kingdom-of-naples, zong-ai, archias-of-thurii, john-chrysostom, reformed-christianity, gaspar-de-ávalos-de-la-cueva ... +18 more

### AI Enrichment — 2026-11-09T12:08:42Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** gaius-julius-erucius-clarus-vibianus, shabbethai-donnolo, wegaf, gaius-fufius-geminus, yaroslav-ii-of-vladimir, pius-ix, resego-kgosidintsi, bamshad, joseph-hueber, mlada ... +19 more

### AI Enrichment — 2026-11-09T12:11:29Z

- **Model:** ollama
- **Enriched:** 32 | **Failed:** 0
- **Entities:** mithridates-iv-of-parthia, subset, euphemism, damarchus, zheng-guo, chrodobertus, innocenzo-di-pietro-francucci-da-imola, manuel-gmez-pedraza, homage-to-catalonia, mile-peynot ... +22 more

### AI Enrichment — 2026-11-09T12:24:09Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** franois-marie-marquis-de-barthlemy, esen-taishi, christian-mauritius-of-königsegg-rothenfels, citizenship, christoph-rudolff, kanada, pawe-holszaski, zhao-mengjian, cora-richardson-hodge, edward-von-lngus ... +18 more

### AI Enrichment — 2026-11-09T12:53:41Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** marcus-peducaeus-stloga-priscinus, jean-iv-de-beaumont, marcus-petreius, olivier-van-noort, lucius-postumius-albinus, lucius-verginius-rufus, micha-kazimierz-ogiski, lucius-aemilius-mamercinus, the-younger-lady, datis ... +17 more

### AI Enrichment — 2026-11-09T12:55:37Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** mariehamn, john-ii-duke-of-lorraine, information-theory, śaunaka, alexander-of-jlich, leninism, kingston-upon-hull, publius-rutilius-lupus, henry-iv-of-england, lucrezia-buti ... +16 more

### AI Enrichment — 2026-11-09T13:09:13Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** charles-archbishop-of-mainz, arignote, philip-ii-count-of-nevers, hanibal-luci, aibert, tauriskos-of-tralles, alfonso-enrquez, zakariya-al-qazwini, usama-ibn-zayd, bridei-v ... +17 more

### AI Enrichment — 2026-11-09T13:31:32Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** palla-strozzi, alexander-callimachis, silseong-of-silla, teti, marinus-of-tyre, eudes-rigaud, gnaeus-fulvius-centumalus-maximus, telauges, sh-toku, aleksander-michał-sapieha ... +17 more

### AI Enrichment — 2026-11-09T13:44:17Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** eudes-rigaud, north-america, mitanni, mikoaj-hlebowicz, douglas-clavering, polycrates-of-argos, hkan-the-red, philippe-mouskes, al-husayn-ibn-said, coptic ... +16 more

### AI Enrichment — 2026-11-09T13:55:34Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** tauriskos-of-tralles, jean-iv-de-beaumont, krenites-arotras, niall-glúndub, dionysius-of-halicarnassus, abu-asim-muhammad-ben-ahmad, urology, manius-pomponius-matho, mikołaj-hlebowicz, charles-philippe-de-croÿ-marquis-dhavré ... +17 more

### AI Enrichment — 2026-11-09T14:21:55Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** ottone-visconti, computer-security, hugh-of-fosses, kenneth-ii-of-scotland, ísleifur-gissurarson, ata-al-ayyubi, francesco-filelfo, hanno, gian-giacomo-adria, visigothic-kingdom ... +16 more

### AI Enrichment — 2026-11-09T14:32:28Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** peter-nolasco, theodore, quintus-pompeius-senecio-sosius-priscus, adad-guppi, william-of-rosenberg, shurasena, pan-chakri-chao-phraya-kosathibodi, jrg-breu-the-elder, mtwara, joan-darag ... +18 more

### AI Enrichment — 2026-11-09T14:38:41Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ōtomo-no-satehiko, proculus, christian-tuxen-falbe, papinian, tiberius-claudius-candidus, švitrigaila, bonaventure, saint-wenceslaus-i-duke-of-bohemia, sigismund-kstutaitis, diether-of-nassau ... +17 more

### AI Enrichment — 2026-11-09T15:01:35Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** hugh-of-fosses, polus, cesare-monti, lê-thái-tông, arnaud-du-ferrier, coriscus-of-scepsis, mussa-bin-bique, flix-varela, john-count-of-werdenberg-trochtelfingen, giovanni-da-milano ... +17 more

### AI Enrichment — 2026-11-09T15:15:33Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** cesare-monti, judoc-ii-of-rožmberk, lagus, nicholas-carew, choricius-of-gaza, otomārs-oškalns, amon, flavius-sallustius, hrafna-flki-vilgerarson, eoban ... +17 more

### AI Enrichment — 2026-11-09T15:22:49Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** coriscus-of-scepsis, eustathios-palatinos, university-of-glasgow, wezilo, felix-hemmerlin, gnaeus-octavius, yunmen-wenyan, bartolomeo-maranta, francisco-de-garay, óengus-mac-nad-froích ... +19 more

### AI Enrichment — 2026-11-09T15:49:35Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** saint-wenceslaus-i-duke-of-bohemia, carlo-gaetano-stampa, tribigild, angela-merici, lucius-sestius-albanianus-quirinalis, gómez-manrique, manuel-antonio-flrez, mary-theisen-lappen, şükrullah, alfonso-i-of-asturias ... +14 more

### AI Enrichment — 2026-11-09T16:02:39Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** medardus, bedrettin-tebrizi, paolo-fregoso, publius-sulpicius-galba-maximus, pacificus-of-ceredano, kab-bin-zuhayr, engineering, giovanni-solari, gaius-antius-aulus-julius-quadratus, khabekhnet ... +17 more

### AI Enrichment — 2026-11-09T16:03:14Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** juvencus, ferry-de-clugny, julie-zhuo, jonas-of-orléans, anton-woensam, angelo-decembrio, paul-de-thermes, marcus-roscius-coelius, gaius-ateius-capito, al-hasan-ibn-sahl ... +17 more

### AI Enrichment — 2026-11-09T16:29:58Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** pharas-the-herulian, georgios-pachymeres, konrad-v-kantner, erazm-ciołek, kfc, muhammad-ibn-aslam-al-ghafiqi, foillan, abul-hasan-ali, igo-melchor-de-velasco-7th-duke-of-fras, engelbert-iii-of-the-marck-archbishop-of-cologne ... +21 more

### AI Enrichment — 2026-11-09T16:57:46Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** al-jarīrī, eirene, rudolf-von-scherenberg, ukrainian, gaston-pierre-de-lvis, aristo-of-alexandria, januarius, remigius-de-fcamp, disney-channel, l-uy-mc ... +17 more

### AI Enrichment — 2026-11-09T16:59:16Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** rené-de-birague, gaius-lucilius, quintus-sulpicius-longus, godelaib, bjørn-farmann, rupa-bai-furdoonji, hygeburg, j-hector-st-john-de-crvecur, irony, john-de-la-pole-1st-earl-of-lincoln ... +17 more

### AI Enrichment — 2026-11-09T17:08:22Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** shams-tabrizi, ophthalmology, empress-zhao-feiyan, brenger-de-landore, alan-i-king-of-brittany, october-revolution, lê-uy-mục, charles-emil-lewenhaupt-the-elder, peter-hagendorf, ibn-ʿabd-rabbih ... +20 more

### AI Enrichment — 2026-11-09T17:32:25Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** shuliang-he, mancio-it, christopher-gore, polygnotus-of-thasos, aloys-von-kaunitz-rietberg, publius-attius-varus, appius-claudius-caecus, musa-çelebi, thietmar-of-minden, gonçalo-velho ... +20 more

### AI Enrichment — 2026-11-09T17:45:23Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** braunau-am-inn, peter, hua-xiong, blanche-of-france, first-book-of-kings, tathal-melgarb, william-of-macclesfield, bernardo-de-iriarte, cleanthes, calanus ... +17 more

### AI Enrichment — 2026-11-09T17:49:27Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** joseph-emmanuel-de-la-trémoille, stepanos-asoghik, lucius-marcius-philippus, crantor, stig-andersen-hvide, bjrn-farmann, hans-brggemann, ibn-abd-rabbih, sosibius-of-tarentum, aristokles ... +14 more

### AI Enrichment — 2026-11-09T18:13:24Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** canachus, hannu, charles-de-montmorency, jean-i-de-grailly, giulio-gabrielli-the-younger, philemon, moldova, jamshd-al-ksh, olivia-rouamba, bolesław-i-of-masovia ... +19 more

### AI Enrichment — 2026-11-09T18:23:53Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** catalo, kosovo, diego-colombos, georg-pencz, tommaso-rodari, angel-grimoard, amr-ibn-al-jamuh, vitellozzo-vitelli, bolesaw-i-of-masovia, johannes-brenz ... +18 more

### AI Enrichment — 2026-11-09T18:29:37Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** hypatia, yahya-al-shirvani-al-bakubi, nikephoros-kallistos-xanthopoulos, ling-cao, mahyna, cædmon, croatia, zephyrinus, oswald-myconius, nikephoros-i-of-constantinople ... +19 more

### AI Enrichment — 2026-11-09T18:59:00Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** emerik-derenin, albrecht-von-eyb, jamshīd-al-kāshī, sulayman-al-arabi, titus, andrzej-jastrzębiec, luscius-lanuvinus, munio-of-zamora, virtual-private-network, menelaus ... +17 more

### AI Enrichment — 2026-11-09T19:00:28Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** brit-ecclesiarum-antiquitates, giacomo-rospigliosi, antn-de-alaminos, marcellus-of-tangier, pietro-ziani, abul-fazl-bayhaqi, chen-yu, criton, jindich-zdk, benedetto-buglioni ... +17 more

### AI Enrichment — 2026-11-09T19:13:51Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** cynisca, chion-of-heraclea, pandulf-iv-of-benevento, sinanddin-fakih-yusuf-pasha, sextus-vettulenus-cerialis, nicetas-eugenianus, fulk-of-neuilly, lithuania, gulf-war, agnolo-firenzuola ... +19 more

### AI Enrichment — 2026-11-09T23:14:25Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 25 | **Failed:** 0
- **Entities:** lorenzo-marcello, rainiero-delci, niccolò-ridolfi, virginio-orsini, lodovico-calini, dragutin-lerman, pierre-cartellier, vincenzo-macchi, josé-maría-ruda, yoshinao-nakada ... +15 more

### AI Enrichment — 2026-11-09T23:20:44Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 25 | **Failed:** 0
- **Entities:** erik-prosperin, neal-zaslaw, andré-du-laurens, georges-rol, jean-antoine-roucher, pierre-antoine-lebrun, thomas-southerne, armand-gensonné, barthélemy-prieur, hans-michelsen ... +15 more

### AI Enrichment — 2026-11-09T19:42:08Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** jordan, antonio-doria-pamphili, william-the-breton, jos-mara-calatrava-y-peinado, domenico-fattori, coluthus, cerinthus, henning-van-der-heide, pargal-ibrahim-pasha, amalric-i-of-jerusalem ... +19 more

### AI Enrichment — 2026-11-09T19:43:15Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** mederich, poncello-orsini, israhel-van-meckenem, filippo-strozzi-the-elder, sibylla, godefroi-comte-destrades, jordan, agostino-di-duccio, antonio-doria-pamphili, connad-cerr ... +18 more

### AI Enrichment — 2026-11-09T20:12:12Z

- **Model:** ollama
- **Enriched:** 21 | **Failed:** 11
- **Entities:** roxana-moslehi, andrzej-jastrzbiec, azalas-de-porcairagues, pedro-de-soto, jacques-mahu, tegueste, galon, zhi-dun, joachim-vadian, konstantinos-phokas ... +11 more

### AI Enrichment — 2026-11-09T20:13:07Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** bulgaria, robert-crispin, johan-van-horne, carneades, nicholas-trivet, xiao-chuo, william-v-prince-of-orange, veera-ballala-ii, humbeline-of-jully, agostino-casaroli ... +20 more

### AI Enrichment — 2026-11-09T20:25:43Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** paullus-fabius-maximus, calrice-di-durisio, dnes-szcsi, alonso-iii-fonseca, teudebur-of-alt-clut, donald-mackenzie, nasir-khusraw, contardus-of-naples, ignacio-de-arteaga-y-bazán, cratippus-of-athens ... +18 more

### AI Enrichment — 2026-11-09T20:51:27Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** attalus, henry-francis-of-mansfeld, veronica-gambara, dhimitër-frëngu, ludovik-crijević-tuberon, niccolò-antonio-colantonio, filippo-calendario, bodzanta, publius-valerius-laevinus, tlepolemus ... +18 more

### AI Enrichment — 2026-11-09T20:53:31Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** the-old-man-and-the-sea, lucius-minicius-natalis-quadronius-verus, international-statistical-classification-of-diseases-and-related-health-problems, un-tourism, lucido-conti, aristion-of-paros, john-strong, glycon-of-athens, federated-states-of-micronesia, antonio-pallavicini-gentili ... +19 more

### AI Enrichment — 2026-11-09T21:04:09Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** arshak-jamalyan, chariton, muhammad-ibn-mahmud-amuli, pedro-gmez-labrador-marquis-of-labrador, terminologia-anatomica, felix-anthony, atharvan, giovanni-giocondo, mummolus, fluid-mechanics ... +17 more

### AI Enrichment — 2026-11-09T21:24:06Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** sylvester-i, novella-dandrea, manuel-the-armenian, abd-as-salam-ibn-mashish-al-alami, giuseppe-doria-pamphili, niccol-antonio-colantonio, lars-herminius-aquilinus, zbynk-zajc, hard-rock, universit-de-versailles-saint-quentin-en-yvelines ... +17 more

### AI Enrichment — 2026-11-09T21:31:46Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** felipe-de-guevara, aladdevle-bozkurt-bey, daud-khan, edmund-bourke, chares-of-lindos, ruy-gmez-de-silva, olaf-haraldsson-geirstadalf, joaquín-suárez, crates, niccolò-fieschi ... +17 more

### AI Enrichment — 2026-11-09T21:45:11Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** christopher-lekapenos, bardaisan, president-of-georgia, joaquín-suárez, story-of-sinuhe, alexander-ii-of-imereti, cavalcante-de-cavalcanti, yakov-bulgakov, alexandros-mavrokordatos, anvari ... +19 more

### AI Enrichment — 2026-11-09T22:01:52Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** marino-bulcani, martin-cellarius, heinrich-faber, herennius-senecio, ibn-al-tiqtaqa, lucius-verginius, abu-said-al-afif, cadfan, caelestius, chaerephon ... +19 more

### AI Enrichment — 2026-11-09T22:02:12Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** richard-hawkins, hroznata-von-ovenec, cormac-mac-cuilennáin, john-carmichael-3rd-earl-of-hyndford, titus-manlius-torquatus, cinci-hüseyin-efendi, martinho-de-zamora, isaac-manasses-de-pas-marquis-de-feuquieres, crimthann-nia-nir, philip-of-swabia ... +19 more

### AI Enrichment — 2026-11-09T22:31:20Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** beatus-rhenanus, butades, godwin-earl-of-wessex, béroul, lucius-marcius-censorinus, laodice-of-cappadocia, roffredo-dellisola, miguel-moreno, damon-of-athens, al-ballanb ... +16 more

### AI Enrichment — 2026-11-09T22:39:00Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** johann-von-bucka, thomas-murner, leptines-of-syracuse, rainerius, agasias-of-ephesus, simon-ben-boethos, matthew-of-aquasparta, natakamani, strachkvas, pavle-đurišić ... +20 more

### AI Enrichment — 2026-11-09T22:43:31Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** bandello-bandelli, yaʿīsh-ibn-ibrāhīm-al-umawī, john-tornike, arion, franciszek-ksawery-lampi, anton-giulio-brignole-sale, jean-doutremeuse, conon, al-ballanūbī, apollonius-of-athens ... +20 more

### AI Enrichment — 2026-11-09T23:08:45Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** giovanni-da-amelia, johan-verstolk-van-soelen, andr-seeldrayers, qara-iskander, pacific-ocean, giovanni-battagio, alexander-vorontsov, sanremo, ma-bufang, giovanni-battista-caporali ... +17 more

### AI Enrichment — 2026-11-09T23:20:23Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** stefano-di-ceccano, chrysippus-of-soli, pavle-urii, stjepan-brodarić, john-zpolya, andreas-de-vega, pelbartus-ladislaus-of-temesvár, dorothy-ooko, cangjie, robert-sidney-1st-earl-of-leicester ... +20 more

### AI Enrichment — 2026-11-09T23:21:45Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** adrian-iv, alonso-de-salazar, jnos-czetz, bek, arthur-paget, cylon-of-athens, fruela-of-cantabria, siger-of-brabant, ferdinand-tnnies, curiatius-maternus ... +16 more

### AI Enrichment — 2026-11-09T23:51:55Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** bolus-of-mendes, ebony-flowers, theodoros-ii-palaiologos, mark-antony, étienne-de-poncher, cai-yan, cerball-mac-dnlainge, cleinias-of-tarentum, glniairn, cenfus ... +18 more

### AI Enrichment — 2026-11-10T00:01:05Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** lippo-memmi, parsman-vi-of-iberia, marcus-antonius-primus, rené-de-voyer-de-paulmy-dargenson, sarah-belzoni, application-programming-interface, jorge-da-costa, vincent-conessao, gian-luca-pallavicini, jan-maachowski ... +17 more

### AI Enrichment — 2026-11-10T00:06:37Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** sergiyev-posad, evaristus, guillaume-de-la-jugie, epicharmus-of-kos, peter-iii-of-arborea, tan-yunxian, asad-ibn-al-furat, jan-małachowski, roger, alfonso-sanches ... +20 more

### AI Enrichment — 2026-11-10T00:27:47Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** cinci-hseyin-efendi, yahya-of-antioch, achille-le-tonnelier-de-breteuil, aristidis-of-athens, mel-din-mac-conaill, pascual-de-andagoya, barranquilla, constantine-gongyles, michalon-lituanus, spycimir-leliwita ... +19 more

### AI Enrichment — 2026-11-10T00:38:31Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** bartolomeo-mezzavacca, harry-potter-and-the-philosophers-stone, dmitry-gerasimov, pelicar, abd-al-aziz-ibn-shuayb, prochorus-cydones, david-malan, agnaptus, yemelyan-ukraintsev, ablgharib-artsruni ... +19 more

### AI Enrichment — 2026-11-10T00:50:11Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** harry-potter-and-the-philosophers-stone, basque-country, zhao-dezhao, wikivoyage, erzhu-tianguang, pagan-of-bulgaria, michele-pesenti, charles-colbert-marquis-de-croissy, olympiodorus-the-elder, an-nadhar-bin-syamil ... +16 more

### AI Enrichment — 2026-11-10T01:10:13Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** marcus-arruntius-aquila, eadberht-iii-præn, aksapada-gautama, louis-jérôme-gohier, kamill-lendvay, dwarf-planet, ali-ibn-ridwan, gustaf-mauritz-armfelt, antónio-de-saldanha, richard-de-fournival ... +16 more

### AI Enrichment — 2026-11-10T01:15:42Z

- **Model:** ollama
- **Enriched:** 32 | **Failed:** 0
- **Entities:** aristidis-of-athens, cleomenes, marcian, callinicus, aksapada-gautama, claudian, calippus-of-syracuse, aloi-de-montbrai, sir-harford-jones-brydges-1st-baronet, vasily-popov ... +22 more

### AI Enrichment — 2026-11-10T01:40:13Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** manuha, bonaire, francesco-della-penna, calippus-of-syracuse, aziz-ad-din-nasafi, herod-of-chalcis, hugh-of-lincoln, charondas, caspar-schoppe, philippe-néricault-destouches ... +17 more

### AI Enrichment — 2026-11-10T02:05:24Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** damocrates, bernardus-papiensis, xu-you, peter-abelard, julian-of-emesa, choerilus-of-samos, arrian, gaius-prastina-messalinus, bhatta-narayana, bacurius-the-iberian ... +20 more

### AI Enrichment — 2026-11-10T02:05:55Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** andr-de-foix, polishlithuanian-commonwealth, sextius-niger, atika-bint-shuhda, mans-de-guzmn, ubaydallah-ibn-abdallah-ibn-tahir, charles-jean-baptiste-fleuriau, ban-biao, srei-reachea, claudine-uwera ... +14 more

### AI Enrichment — 2026-11-10T02:20:52Z

- **Model:** ollama
- **Enriched:** 17 | **Failed:** 3
- **Entities:** choerilus-of-samos, awana-ibn-al-hakam, enheduanna, vratko-nemanji, celsus, senorina-of-basto, merneptah, zheng-xuan, fati-abubakar, union-of-south-american-nations ... +7 more

### AI Enrichment — 2026-11-10T02:27:52Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** charondas, interview, manius-curius-dentatus, philippe-canaye, sri-vijaya-rajasinha-of-kandy, saumur, jan-ii-van-wassenaer, cyprian, damià-forment, aulus-hostilius-mancinus ... +18 more

### AI Enrichment — 2026-11-10T02:46:10Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** vratko-nemanji, elias, gaius-sulpicius-peticus, lorenzo-iv-suárez-de-figueroa-y-córdoba, ubertino-of-casale, lothar-i-von-stade, sohaemus-of-emesa, fernando-prez-calvillo, gregory-of-langres, avianus ... +18 more

### AI Enrichment — 2026-11-10T03:05:55Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** choerilus-of-samos, kara-sea, arnulf-of-leuven, aziz-ul-rahman-usmani, jeongjong-of-joseon, brnjača, philip-louis-ii-count-of-hanau-mnzenberg, sasanian-empire, pawe-jan-sapieha, lê-nghi-dân ... +20 more

### AI Enrichment — 2026-11-10T03:12:04Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** zheng-xuan, joachim-mrlin, aristocles-of-messene, brezno, imre-csky, vittore-trincavelli, stephen-kontostephanos, arnoald, florinus-of-rems, philippe-de-courcillon-de-dangeau ... +16 more

### AI Enrichment — 2026-11-10T03:41:01Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** fernando-prez-calvillo, kara-sea, clitomachus-of-thebes, louis-douard-bout-willaumez, you-ruo, oliver-mbamara, zhu-shuzhen, shan-xiongxin, wilhelm-von-dörnberg, aulus-manlius-vulso ... +17 more

### AI Enrichment — 2026-11-10T03:50:17Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** avianus, martín-de-zalba, gaius-julius-solinus, louise-allcock, luca-ridolfucci-gentili, planetary-nebula, michel-erhart, hans-georg-ngeli, charulata-mukherjee, emilio-dandolo ... +16 more

### AI Enrichment — 2026-11-10T03:51:51Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** guillem-de-copons, tulien, planetary-nebula, wilhelm-von-drnberg, johan-oxenstierna, gaius-quintius-atticus, jan-juriewicz-hlebowicz, l-nghi-dn, shapur-ibn-sahl, gonalo-de-amarante ... +15 more

### AI Enrichment — 2026-11-10T04:14:48Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** maria-afonso, henry-of-the-palatinate, oppian, john-tiptoft-1st-earl-of-worcester, alois-paroubek, villarreal, gruffydd-maelor-i, canterbury, chen-wu, martianus-capella ... +20 more

### AI Enrichment — 2026-11-10T04:31:19Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** sextus-erucius-clarus, robert-le-danois, mc-hin-tng, adam-of-łowicz, ala-al-din-al-bukhari, sebastián-de-ocampo, abd-al-dar-ibn-qusai, ferchar-fota, cleopatra-the-alchemist, chen-dao ... +21 more

### AI Enrichment — 2026-11-10T04:42:14Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** john-stone, cato-the-elder, johann-albrecht-korff, austriahungary, jean-de-witte, joo-pessoa, medina, konstantinos-aspietes, cao-ren, bao-xun ... +16 more

### AI Enrichment — 2026-11-10T04:57:04Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** salomon-king-of-brittany, alois-paroubek, elisabeth-valerio, charmadas, iwan-bohdanowicz-sapieha, francisco-gutiérrez-de-los-ríos, dinon, cadafael-cadomedd-ap-cynfeddw, john-of-moravia, buddhapālita ... +19 more

### AI Enrichment — 2026-11-10T05:11:26Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** konrad-von-marburg, binnya-ran-ii, so-bernardo-do-campo, marcus-ummidius-quadratus-annianus, bernard-franois-marquis-de-chauvelin, mirza-muhammad-khan-i, bharadwaja, oranjestad, khālid-ibn-ʿabd-almalik-almarwarrūdhī, boško-palkovljević-pinki ... +19 more

### AI Enrichment — 2026-11-10T05:20:27Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** bhatta-narayana, fakhr-un-nisa, john-palsgrave, jurij-slatkonja, gabrn-mac-domangairt, cao-zhi, saimaa, goalkeeper, saint-ovidius, büri ... +18 more

### AI Enrichment — 2026-11-10T05:32:11Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** diadumenian, pseudo-marius, vasily-golovnin, gaius-oppius, khlid-ibn-abd-almalik-almarwarrdh, axel-otto-mrner, hundred-years-war, thekla, zvonimir-eparovi, gaius-claudius-glaber ... +18 more

### AI Enrichment — 2026-11-10T05:59:58Z

- **Model:** ollama
- **Enriched:** 22 | **Failed:** 10
- **Entities:** dinon, saimaa, haakon-ii-of-norway, bischr-ibn-al-mutamir, hafiz-tanish, joo-carlos-saldanha-de-oliveira-daun-1st-duke-of-saldanha, marcus-horatius-pulvillus, arnold-of-selenhofen, thailand, david-ii-catholicos-patriarch-of-georgia ... +12 more

### AI Enrichment — 2026-11-10T06:09:37Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** thalelaeus, clinomachus, mathematics, asterius, diego-de-losada, francesco-salviati, marie-melchior-joseph-théodose-de-lagrené, aratus-of-sicyon, peter-von-meyendorff, pir-muhammad ... +15 more

### AI Enrichment — 2026-11-10T06:13:26Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** gar-trinring-tsendro, bao-xin, simon-van-limburg, arnoul-daudrehem, cicero-minor, caelius-aurelianus, manuel-rodrguez-erdoza, ban-zhao, ma-jun, khayran-as-saqlab ... +18 more

### AI Enrichment — 2026-11-10T06:33:38Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** decimus-junius-pera, titus-ampius-balbus, funk, john-i-of-lubin, alexon, juan-ramón-balcarce, fabrizio-i-colonna, oshere, august-von-nostitz, democrates ... +17 more

### AI Enrichment — 2026-11-10T06:52:50Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** tianjin, amyntas-ii-of-macedon, feng-yi, oscar-camilin, ivan-vyhovskyi, claudius-maximus, niccol-di-giovanni-fiorentino, nusaybah-bint-kaab, baltolu-sleyman-bey, charles-vi-of-france ... +18 more

### AI Enrichment — 2026-11-10T06:55:55Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** francisco-ramn-vicua, commodian, critolaus-of-megalopolis, chen-lin, lucius-funisulanus-vettonianus, cui-bi, wojciech-radziwi, franz-georg-karl-von-metternich, abdul-khaliq-ghijduwani, john-geometres ... +16 more

### AI Enrichment — 2026-11-10T11:07:50Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 50 | **Failed:** 0
- **Entities:** gnaeus-pinarius-cornelius-severus, timur-khoja, domangart-rti, enetarzi, psammetichus-iv, zoology, septimius, international-labour-organization, confederation-of-african-football, university-of-glasgow ... +40 more

### AI Enrichment — 2026-11-10T07:09:14Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** juan-ramón-balcarce, xenophon-of-ephesus, rodrigo-gil-de-hontañón, glaucias-of-aegina, mahmud-al-kashgari, jos-mara-rojas-garrido, theodore-mangaphas, diego-de-lepe, simon-grynaeus, stefan-dragutin ... +18 more

### AI Enrichment — 2026-11-10T07:34:50Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** mikoaj-kurowski, thomas-of-celano, wang-ji, marcellinus-comes, defendens, philippa-mareri, sauromaces-ii-of-iberia, michele-bonelli, gaston-iii-count-of-foix, cotys-iv ... +18 more

### AI Enrichment — 2026-11-10T07:42:55Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** sauromaces-ii-of-iberia, bakjur, bardas-phokas-the-younger, henry-viii-of-legnica, demetrios-palaiologos, jean-armand-de-maillé-brézé, michael-stryphnos, zhou-zhi, muhammad-ibn-buzurg-ummid, stanisaw-ciosek ... +19 more

### AI Enrichment — 2026-11-10T07:46:05Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** caelius-aurelianus, the-threepenny-opera, franois-de-joyeuse, zimrilim, ivan-bezpaly, augustin-von-alveld, jean-baptiste-charles-bouvet-de-lozier, thomas-kantakouzenos, muhammad-aufi, cornelius-scipio-salvito ... +17 more

### AI Enrichment — 2026-11-10T08:21:24Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** jaya-ananda, zamo, haki, carl-löwenhielm, callixenus-of-rhodes, crateuas, lokman-han, cincinnatus, antonn-brus-z-mohelnice, michał-jerzy-mniszech ... +20 more

### AI Enrichment — 2026-11-10T08:25:48Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** saturninus, thomas-dagworth, alexander-akimetes, cecilia-johansdotter-of-sweden, ballomar, layla-zakaria-abdel-rahman, cornelius-nepos, somerled, jean-de-liège, cocceius-auctus ... +18 more

### AI Enrichment — 2026-11-10T08:35:45Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** crates-of-athens, hans-burgkmair-the-elder, bonaventura-badoardo-de-peraga, giovannino-de-grassi, johann-wenzel-von-gallas, jean-de-lige, william-austin-burt, charles-dangennes-de-rambouillet, otto-iii-van-holland, fa-al-dn-amad-fa-khvf ... +17 more

### AI Enrichment — 2026-11-10T09:01:06Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ibn-funduq, john-of-gogw, eisenstadt, eligius, strasbourg, alan-basil-de-lastic, calvisia-domitia-lucilla, ceionius-proculus, alcibiades, juan-cobo ... +17 more

### AI Enrichment — 2026-11-10T09:08:30Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** cornificia, jean-baptiste-budes-comte-de-gubriant, wu-jianmin, coenus, pedro-alonso-nio, franois-arnaud, erasistratus, jános-kanizsai, alois-friedrich-von-brühl, bruno-of-bretten ... +15 more

### AI Enrichment — 2026-11-10T09:11:19Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** sithu-kyawhtin, claudius-clavus, baltoğlu-süleyman-bey, matsui-keishir, aspasia-the-physician, count-karl-ferdinand-von-buol, titus-tarquinius, gabriel-franchère, wadysaw-the-white, john-of-la-rochelle ... +19 more

### AI Enrichment — 2026-11-10T09:45:11Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** astyochus, pedro-fajardo-1st-marquis-of-los-vlez, cephisodotus-the-elder, finger-snail, abu-kelevi, zhou-tai, isidore-of-kyiv, cristbal-de-morales, henrik-lindstrm, olbram-iii-von-kvorec ... +19 more

### AI Enrichment — 2026-11-10T09:50:35Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** francis-seymour-conway-1st-marquess-of-hertford, aulus-cornelius-palma-frontonianus, wolfgang-capito, aristogenes, willerich, yuri-nemyrych, piyale-pasha, george-kodinos, jan-roháč-of-dubá, władysław-anders ... +18 more

### AI Enrichment — 2026-11-10T09:59:17Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** lazare-de-baf, matteo-i-visconti, fadrique-enrquez-de-velasco, władysław-the-white, shen-yue, l-hy-tng, gasparinus-de-bergamo, bartholomaeus-of-neocastro, damat-gürcü-halil-rifat-pasha, guiguzi ... +17 more

### AI Enrichment — 2026-11-10T10:34:47Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** titus-tarquinius, byrhtnoth, isaac-doukas-vatatzes, seleucus, marcus-peducaeus-priscinus, asclepiodotus-of-alexandria, ferdinand-august-of-lobkowicz, arusianus-messius, kemalpaşazade, giovanni-arrivabene ... +18 more

### AI Enrichment — 2026-11-10T10:35:38Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** kaspar-rist, vietnam-war, battle-of-issus, tribonian, maximilianus-transylvanus, jrme-souchier, francesco-daquino, bernardino-ochino, clearchus-of-heraclea, properzia-de-rossi ... +19 more

### AI Enrichment — 2026-11-10T10:51:21Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** indrajayavarman, saad-al-dawla, baldassare-estense, aristobulus-of-paneas, charidemus, ninurta-apla-x, charles-antoine-leclerc-de-la-bruère, jean-françois-georgel, andrea-pisano, johann-christoph-von-bartenstein ... +14 more

### AI Enrichment — 2026-11-10T11:13:36Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** euthymus, andronicus-of-rhodes, giovanni-boccaccio, antão-gonçalves, shō-shishō, jan-stanisaw-sapieha, nicola-filotesio, cristóbal-de-olid, jean-de-thvenot, second-punic-war ... +18 more

### AI Enrichment — 2026-11-10T11:19:54Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** olbram-iii-von-kvorec, aulus-postumius-albinus-luscus, theodore-of-raithu, hydarnes-ii, pandulf-ii-of-benevento, bonus, abu-madyan, basilides-the-epicurean, abul-hasan-ash-shadhili, aulus-vitellius ... +21 more

### AI Enrichment — 2026-11-10T11:43:36Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** archdeacon-theophylact, jos-francisco-gana-lpez, hersekzade-ahmed-pasha, masud-ibn-muhammad-sijzi, karl-ernst-wilhelm-von-canitz-und-dallwitz, claudius-lysias, guillaume-bud, chares-of-athens, herman-i-count-of-salm, annius-of-viterbo ... +17 more

### AI Enrichment — 2026-11-10T11:59:02Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** raimondo-guglielmo-des-fargues, eochaid-mac-domangairt, sh-shish, kemalpaazade, emperor-jing-of-northern-zhou, nicolaus-ragvaldi, paul-gssfeldt, caduceus, samba, adolph-ii-prince-of-anhalt-kthen ... +21 more

### AI Enrichment — 2026-11-10T12:12:09Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** chares-of-athens, coelius-sedulius, henry-george-ward, gilbert-elliot-murray-kynynmound-2nd-earl-of-minto, avidius-cassius, umm-jamil, charon-of-lampsacus, karl-bttiger, franois-de-mailly, wratislav-von-frstenberg ... +17 more

### AI Enrichment — 2026-11-10T12:16:38Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** marcus-peducaeus-priscinus, jan-ostrorg, tettius-julianus, mormonism, iraniraq-war, gabriel-marie-joseph-comte-dhédouville, mahmud-injir-al-faghnawi, simon-constable-of-jerusalem, lucius-roscius-aelianus-maecius-celer, ethirimana-cinkam ... +18 more

### AI Enrichment — 2026-11-10T12:38:02Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** juan-de-ayala, alexander-ales, muḥammad-ibn-maʻn-ibn-sumādiḥ-al-muʻtaṣim, asclepiades, aulus-ofilius, aristonous-of-pella, eochaid-mac-domnaill, leonard-of-chios, nils-bielke, nicocles ... +18 more

### AI Enrichment — 2026-11-10T12:53:06Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** þangbrandr, cronius-the-pythagorean, archangela-girlani, william-of-volpiano, padmini-murthy, giulio-alberoni, homs, daniel-czapliski, jacques-franois-lefranc, francesco-de-tatti ... +20 more

### AI Enrichment — 2026-11-10T13:11:31Z

- **Model:** ollama
- **Enriched:** 24 | **Failed:** 8
- **Entities:** andrea-alciato, andrea-doria, jacques-franois-lefranc, julius-pollux, batis, henri-de-mondeville, guillaume-arrufat, pedro-csar-dominici, jaime-torres-bodet, andrzej-hieronim-zamoyski ... +14 more

### AI Enrichment — 2026-11-10T13:26:06Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** charles-cathcart-9th-lord-cathcart, jean-de-meun, asclepiades-of-bithynia, hipponicus-ii, cornelius-sabinus, dervish-ibrahim-pasha, bo-cai, þorlákur-runólfsson, fuzuli, claude-franois-bidal-dasfeld ... +18 more

### AI Enrichment — 2026-11-10T13:35:34Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** horsa, isaac-albalag, dardanus-of-athens, daeso, francesco-di-simone-da-santacroce, eystein-orre, syrian-civil-war, charles-de-lorraine-de-vaudmont, mireya-agüero, tellos-agras ... +19 more

### AI Enrichment — 2026-11-10T13:55:53Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** lantbert-von-lyon, sonchis-of-sais, cui-hao, jean-xavier-lefvre, wang-gen, gaius-volusenus, jorge-cabral, sancha-of-majorca, artemidorus-capito, paul-i ... +19 more

### AI Enrichment — 2026-11-10T14:08:02Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** harthacanute, fortanerius-vassalli, reginhard-von-lttich, aufidius-bassus, angilbert, ptolemais-of-cyrene, philippe-de-cabassole, muhammad-salih, boiorix, muhmmad-ibn-ghniya ... +19 more

### AI Enrichment — 2026-11-10T14:15:20Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** august-friedrich-ferdinand-von-der-goltz, sun-kai, zeno, kunda-culture, pasha-yiğit-bey, dong-min, cao-zhen, meng-ao, otto-ii-of-lippe, clement-ix ... +18 more

### AI Enrichment — 2026-11-10T14:48:48Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** vincenzo-cartari, theodemar, nahariya, muhàmmad-ibn-ghàniya, pang-lin, count-karl-ludwig-von-ficquelmont, vladimr-clementis, abu-nasr-mansur, aulus-caecina-alienus, bangkok ... +18 more

### AI Enrichment — 2026-11-10T14:51:18Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** monism, qara-yusuf, lobamba, caranus, william-à-court-1st-baron-heytesbury, arthur-p-bagby, lucius-aurunculeius-cotta, dagalaifus, capelianus, diego-lpez-iii-de-haro ... +21 more

### AI Enrichment — 2026-11-10T15:04:11Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** cao-chun, second-sino-japanese-war, dacianus, sigebert-ii, catanzaro, metrodorus-of-lampsacus, paulina-oduro, miguel-gmez-damas, gedik-ahmed-pasha, yun-kwan ... +19 more

### AI Enrichment — 2026-11-10T15:37:44Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** gervais-count-of-rethel, pasha-yiit-bey, pavel-tsitsianov, urnfield-culture, laurent-jean-franois-truguet, edward-clinton-1st-earl-of-lincoln, vinko-pribojević, marinus-ii, john-ponsonby-1st-viscount-ponsonby, dinah-musindarwezo ... +17 more

### AI Enrichment — 2026-11-10T15:40:38Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** alfonso-de-cartagena, bomilkar, naukydes-of-argos, jan-carstenszoon, censorinus, richard-of-middleton, constantius, herv-de-portzmoguer, rurik, thomas-of-cana ... +17 more

### AI Enrichment — 2026-11-10T15:42:14Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** diemoth, ibn-alhaim-alishbili, alinah-kelo-segobye, jan-carstenszoon, william-of-conches, king-nan-of-zhou, anthony-bacon, émile-peynot, bernardo-bandini, andronikos-lapardas ... +20 more

### AI Enrichment — 2026-11-10T16:17:54Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** ansbert-of-rouen, william-sharp-macleay, francis-de-pressens, aulus-claudius-charax, demetrius-of-guria, lucius-cornelius-sulla, lucius-ceionius-commodus, carlo-andrea-pozzo-di-borgo, jean-franois-de-bette-marquis-of-lede, miss-fatima ... +21 more

### AI Enrichment — 2026-11-10T16:29:52Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** guillaume-le-testu, vladimír-clementis, ibar-of-beggerin, leander-of-seville, mikhail-bestuzhev-ryumin, john-of-worcester, foggia, saint-martial, gaius-caecina-largus, kṣemā ... +20 more

### AI Enrichment — 2026-11-10T16:31:19Z

- **Model:** ollama
- **Enriched:** 23 | **Failed:** 9
- **Entities:** callixtus-iii, folk-music, arnegisclo, françois-annibal-destrées, william-sharp-macleay, kem, antanas-purnas, la-hire, jernimo-bcker, idomeneus-of-lampsacus ... +13 more

### AI Enrichment — 2026-11-10T16:53:23Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** idomeneus-of-lampsacus, philibert-of-chalon, piero-di-cosimo-de-medici, first-chechen-war, erispoe, honor-gabriel-riqueti-comte-de-mirabeau, rimbert, philibert-of-jumiges, john-vii, john-of-antioch ... +19 more

### AI Enrichment — 2026-11-10T17:18:59Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** first-punic-war, francesco-di-marco-datini, lucius-rubellius-geminus, gaius-ateius-capito, lucius-apronius-caesianus, girim-of-silla, walter-of-st-victor, akash-khurana, gnaeus-pedanius-fuscus-salinator, nicolás-de-cardona ... +15 more

### AI Enrichment — 2026-11-10T17:28:37Z

- **Model:** ollama
- **Enriched:** 25 | **Failed:** 7
- **Entities:** muammad-b-ibrhm-b-sad-shams-al-dn-ab-abda-al-anr, stanisaw-of-skarbimierz, cellach-mac-dnchada, indabibi, clement-viii, abu-mikhnaf, domenico-gagini, niu-jin, hananchi, william-neville-earl-of-kent ... +15 more

### AI Enrichment — 2026-11-10T17:33:18Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** friedrich-von-canitz, cleitus-the-black, asclepiades-pharmacion, alvise-cadamosto, john-mavrocordatos, ushuaia, saint-sarkis-the-warrior, mehmed-i-giray, claude-louis-de-la-chtre, master-ms ... +21 more

### AI Enrichment — 2026-11-10T21:57:11Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** wang-chung-hui, al-mufaddal-ibn-abi-al-fadail, titus-aebutius-helva, moses-bar-kepha, constantine-akropolites, chiara-gambacorti, pedro-téllez-girón, aradius-rufinus, jen-zichy, mehou ... +19 more

### AI Enrichment — 2026-11-10T22:05:40Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** piero-de-bonzi, sextus-calpurnius-agricola, thomas-the-slav, charles-ii-count-of-alenon, cecilia-cesarini, patricia-may-urzúa, alexandre-thodore-victor-comte-de-lameth, clement-x, gaero, gan-de ... +18 more

### AI Enrichment — 2026-11-10T22:12:55Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** leukon-ii-of-bosporus, gomes-eanes-de-zurara, tadhg-mac-cárthaigh, cerrah-mehmed-paa, bouzes, idwal-foel, paul-thrse-david-dastros, harith-ibn-hilliza-ul-yashkuri, fernão-lopes, pietro-di-giovanni-tedesco ... +20 more

### AI Enrichment — 2026-11-10T22:30:47Z

- **Model:** ollama
- **Enriched:** 31 | **Failed:** 1
- **Entities:** george-elmacin, sargis-ii-jaqeli, agesidamus-of-locris, nguyn-nhc, thomas-elyot, robert-i-count-of-conversano, potitus-valerius-messalla, menander, shams-al-dīn-al-samarqandī, aurignacian ... +21 more

### AI Enrichment — 2026-11-10T22:47:51Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 23 | **Failed:** 0
- **Entities:** petrus-gyllius, li-zhengji, stanislaus-of-szczepanów, hugh-of-flavigny, tunisia, paulinus-of-york, french-invasion-of-russia, gnaeus-cornelius-lentulus-marcellinus, richard-iii-of-england, metrology ... +13 more

### AI Enrichment — 2026-11-10T22:52:10Z

- **Model:** ollama
- **Enriched:** 27 | **Failed:** 5
- **Entities:** ansbert-of-rouen, mahathammaracha-i, bernardo-de-velasco, giovanni-sercambi, lucius-aemilius-barbula, johannes-bonemilch, scouting, juan-de-aragón-y-de-jonqueras-2nd-count-of-ribagorza, joseph-von-hammer-purgstall, autocles ... +17 more

### AI Enrichment — 2026-11-10T22:52:44Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 25 | **Failed:** 0
- **Entities:** gaius-caelius-rufus, claudius-mamertinus, jayavarman-vi, berowulf, victoriano-salado-álvarez, johannes-murmellius, hong-mai, kiruna, ramat-gan, meno ... +15 more

### AI Enrichment — 2026-11-10T22:56:26Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 27 | **Failed:** 0
- **Entities:** alonso-de-covarrubias, franois-sverin-marceau, william-daubigny-3rd-earl-of-arundel, louis-the-stammerer, wang-l, ricardo-mir, redemptus-of-the-cross, bernardino-of-siena, maximus-the-confessor, li-jie ... +17 more

### AI Enrichment — 2026-11-10T22:56:35Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 27 | **Failed:** 0
- **Entities:** alonso-de-covarrubias, franois-sverin-marceau, william-daubigny-3rd-earl-of-arundel, louis-the-stammerer, wang-l, ricardo-mir, redemptus-of-the-cross, bernardino-of-siena, maximus-the-confessor, li-jie ... +17 more

### AI Enrichment — 2026-11-10T22:58:46Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 25 | **Failed:** 0
- **Entities:** thomas-grey-2nd-marquess-of-dorset, theodoret-of-antioch, john-digby-1st-earl-of-bristol, gnaeus-pedius-cascus, junius-veldumnianus, william-lithgow, motono-ichir, theodoros-prodromos, jeong-do-jeon, guy-of-anderlecht ... +15 more

### AI Enrichment — 2026-11-10T22:59:11Z

- **Model:** composer·local·Jeltons-Mac-Mini.local
- **Enriched:** 25 | **Failed:** 0
- **Entities:** thomas-grey-2nd-marquess-of-dorset, theodoret-of-antioch, john-digby-1st-earl-of-bristol, gnaeus-pedius-cascus, junius-veldumnianus, william-lithgow, motono-ichir, theodoros-prodromos, jeong-do-jeon, guy-of-anderlecht ... +15 more

### AI Enrichment — 2026-11-10T23:26:11Z

- **Model:** ollama
- **Enriched:** 26 | **Failed:** 6
- **Entities:** walter-of-winterburn, kab-ibn-al-ashraf, quintus-sertorius, ethan-allen-brown, ertuğrul, ferréol-de-vienne, yakareb, miyoshi-kiyotsura, puxian-wannu, julius-constantius ... +16 more

### AI Enrichment — 2026-11-10T23:31:58Z

- **Model:** ollama
- **Enriched:** 30 | **Failed:** 2
- **Entities:** hasanak-the-vizier, stephen-of-armenia, liu-hong, qarin-i, metrology, henryk-kietlicz, greek-war-of-independence, sultan-ahmed-mosque, berchtold-haller, talorc-ii ... +20 more

### AI Enrichment — 2026-11-10T23:53:50Z

- **Model:** ollama
- **Enriched:** 29 | **Failed:** 3
- **Entities:** french-invasion-of-russia, onomacritus, petronius-annianus, berchtold-haller, jayavarman-vi, johannes-murmellius, wen-zhengming, marino-sanuto-the-younger, ab-anfa-dnawar, yerevan ... +19 more

### AI Enrichment — 2026-11-10T23:55:40Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** richard-iii-of-england, quintus-veranius, berowulf, ramat-gan, urraca-of-portugal, bhskara, jnos-vitz, ribeiro-preto, antonius-marcellinus, abu-al-hasan-al-tabari ... +18 more

### AI Enrichment — 2026-11-10T23:59:45Z

- **Model:** ollama
- **Enriched:** 28 | **Failed:** 4
- **Entities:** reginald-de-cobham-1st-baron-cobham, measurement, quintus-veranius, gaius-caelius-rufus, rufinus, king-xiang-of-wei, bhskara, adolfo-saldas, ssuke-uno, sulpicia ... +18 more
