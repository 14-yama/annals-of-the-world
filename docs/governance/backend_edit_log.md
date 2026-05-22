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
