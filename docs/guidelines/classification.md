# International Call Number & Subject Heading System for the Knowledge Graph

See also: [call_number_subject_heading_system.md](./call_number_subject_heading_system.md) — full contributor guide and rationale for the classification system.

This document defines the project call-number taxonomy (class.division.id), second-level divisions, call-number format, versioned feature list (v1–v5), and a Canonical Corpus Registry for primary cultural/textual traditions.

---

## 1. Top-Level Classes (0–9)
These are the “shelves” (analogous to Dewey classes) anchored on the core schema.

- Class: 0 — Ideas (Core Categories)
  - Heading: Political, Ethical, Legal
- Class: 1 — Ideas (Other Theories)
  - Heading: Economic, Scientific, Technological, Religious, Cultural, Environmental, Artistic
- Class: 2 — People
  - Heading: Philosophers, Leaders, Scientists, Activists, Artists
- Class: 3 — Institutions
  - Heading: Political, Legal, Economic, Religious, Scientific, Cultural, International
- Class: 4 — Places
  - Heading: Continent, Region, Country, City, Empire, Civilization, Culture-area
- Class: 5 — Events
  - Heading: Wars, Revolutions, Elections, Scientific Discoveries, Environmental Crises
- Class: 6 — Movements
  - Heading: Political, Social, Religious, Cultural, Scientific, Technological, Environmental
- Class: 7 — Artifacts & Texts
  - Heading: Constitutions, Codes, Scriptures, Scientific Works, Artworks, Technologies
- Class: 8 — Evidence
  - Heading: Primary, Secondary, Archaeological, Quantitative, Oral
- Class: 9 — Timeframes
  - Heading: Period, Era, Epoch

---

## 2. Second-Level Divisions
Each top-level class subdivides into more specific divisions (library-style schedule). Use the numeric division when creating call numbers.

0 – Ideas (Core)
- 010 Political Systems & Governance
- 020 Ethical Systems
- 030 Legal Systems & Law

1 – Ideas (Other)
- 110 Economic Theories & Systems
- 120 Scientific Paradigms
- 130 Technological Innovations
- 140 Religious & Philosophical Concepts
- 150 Social & Cultural Theories
- 160 Environmental & Ecological Ideas
- 170 Artistic & Aesthetic Movements

2 – People
- 210 Philosophers & Thinkers
- 220 Political Leaders
- 230 Legal Figures
- 240 Scientists & Inventors
- 250 Religious Figures
- 260 Artists & Writers
- 270 Activists & Reformers

3 – Institutions
- 310 Political Institutions
- 320 Legal Institutions
- 330 Economic Institutions
- 340 Religious Institutions
- 350 Scientific Institutions
- 360 Cultural Institutions
- 370 International Organizations

4 – Places
- 410 Continents
- 420 Regions
- 430 Countries / Polities
- 440 Cities
- 450 Empires / Dynasties
- 460 Civilizations
- 470 Culture Areas

5 – Events
- 510 Wars & Conflicts
- 520 Revolutions & Uprisings
- 530 Elections & Shifts
- 540 Legal Cases
- 550 Scientific Discoveries
- 560 Technological Breakthroughs
- 570 Religious Events
- 580 Environmental Events

6 – Movements
- 610 Political Movements
- 620 Social Movements
- 630 Religious Movements
- 640 Cultural Movements
- 650 Scientific Movements
- 660 Technological Movements
- 670 Environmental Movements

7 – Artifacts & Texts
- 710 Constitutions & Charters
- 720 Legal Codes
- 730 Religious Texts
- 740 Philosophical Works
- 750 Scientific Texts
- 760 Artworks
- 770 Technological Artifacts

8 – Evidence
- 810 Primary Sources
- 820 Secondary Sources
- 830 Archaeological Evidence
- 840 Quantitative Data
- 850 Oral Traditions

9 – Timeframes
- 910 Prehistoric
- 920 Classical
- 930 Medieval
- 940 Early Modern
- 950 Modern
- 960 Contemporary

---

## 3. Call Number Format
Use the pattern: `[Class].[Division].[ID]`

- Class = 0–9 (top-level)
- Division = subcategory numeric code (2–3 digits as above)
- ID = canonical node identifier (prefer `slug` or a local sequential number)

Example: `4.430.rome-27bce` or `2.210.plato` — the call number is used as a stable classification token when adding nodes.

---

For the project feature timeline (v1–v5) see [features_by_version.md](./features_by_version.md) in this folder.

---

## 📌 Master Feature List (Concise)
- Classification: `class.division.id` call numbers.
- Chronology: `chron_key` for ordering; negative years for BCE.
- Corpus discipline: A–D tiers (Primary → Institutional).
- Evidence model: Evidence nodes + per-edge citations (Chicago 17 required).
- Frameworks: historian frameworks as first-class nodes (v4+).
- Agents: CIDOC CRM E39 Agent model for `Person` & `Institution` (v5 proposal).
- Relationships: Active voice, verb-first, semantically normalized.
- Generic vs Contextual nodes: timeless hubs vs specific contextual instances.
- Event hierarchy: `Epoch → Era → Period → EventWindow`.
- Governance workflow: `Propose → Cite → Frame → Place → Review → Publish → Version`.
- Constraints & hygiene: uniqueness, temporal sanity, no floating concepts.
- QA checks: coverage audits, anachronism scans, passive-voice audits.
- International alignment: UNESCO chronology bins, CIDOC CRM classes, Dublin Core for bibliographic metadata, PROV-O for provenance.

---

## Corpus Registry (Canonical — primary traditions)
We maintain a focused registry of cultural/textual corpora to tag evidence and help disambiguate traditions. Store corpus membership on `:Evidence` nodes via `corpus`/`corpus_tier` fields or by linking `(:Evidence)-[:BELONGS_TO]->(:Corpus)`.

Corpus tiers (CorpusTier / Evidence.corpus_tier):
- A — Primary
- B — Peer-reviewed
- C — Scholarly press
- D — Institutional
- (E — Archaeological, F — Oral/Quantitative — optional)

Canonical Corpus Registry (examples)

### Ancient Near East & Mediterranean
- `MESOPOTAMIAN_CORPUS` — Sumerian/Akkadian inscriptions, Enūma Eliš, Gilgamesh, royal inscriptions.
- `EGYPTIAN_CORPUS` — Pyramid/Coffin Texts, Book of the Dead, king lists.
- `BIBLICAL_CORPUS` — Hebrew Bible/Tanakh, Septuagint, NT, Dead Sea Scrolls.
- `JUDAIC_RABBINIC_CORPUS` — Mishnah, Talmud, Midrash.
- `GRAECO_ROMAN_CORPUS` — Greek/Latin literature & philosophy; Roman legal corpus.
- `CANON_LAW_CORPUS` — Gratian’s Decretum, papal decretals, council records.

### Iran & Central/West Asia
- `IRANIAN_ZOROASTRIAN_CORPUS` — Avesta, Pahlavi texts.
- `ISLAMIC_QURAN_HADITH_CORPUS` — Qur'ān, canonical ḥadīth collections.
- `ISLAMIC_FIQH_KALAM_FALSAFA_CORPUS` — fiqh, kalām, falsafa traditions.
- `PERSIANATE_CHRONICLE_CORPUS` — Shāhnāmeh, Bāburnāma, court histories.
- `OTTOMAN_ARCHIVE_CORPUS` — kanunnames, tahrir defterleri.

### South & Southeast Asia
- `INDIC_VEDIC_UPANISHAD_CORPUS` — Vedas, Brāhmaṇas, Upaniṣads.
- `INDIC_EPIC_DHARMA_CORPUS` — Mahābhārata, Rāmāyaṇa, Arthaśāstra.
- `BUDDHIST_PALI_CANON` — Pāli Tipiṭaka.
- `BUDDHIST_MAHAYANA_CORPORA` — Sanskrit/Chinese/Tibetan canons.
- `SE_ASIAN_INSCRIPTIONAL_CORPUS` — Khmer, Javanese, Thai inscriptions & chronicles.

### East Asia
- `SINIC_CLASSICS_CORPUS` — Five Classics, Four Books, dynastic histories.
- `JAPANESE_CLASSICAL_CORPUS` — Kojiki, Nihon Shoki, ritsuryō texts.
- `KOREAN_CLASSICAL_CORPUS` — Samguk Sagi, Samguk Yusa.

### Africa (beyond Egypt)
- `ETHIOSEMITIC_GEEZ_CORPUS` — Kebra Nagast, Ethiopian chronicles.
- `TIMBUKTU_MANUSCRIPT_CORPUS` — Arabic scholarship of the Western Sahel.
- `AFRICAN_ORAL_EPI_CYCLE` — documented epic cycles (e.g., Sundiata).

### Americas
- `MESOAMERICAN_CORPORA` — Maya/Aztec/Mixtec codices, Nahuatl annals.
- `ANDEAN_CORPUS` — khipu records, early chronicles.

### Technology / Science Traditions
- `MILITARY_TECHNICAL_CORPUS_EARLY` — early ordnance, Chinese/Islamic/European military texts.
- `EARLY_MODERN_SCIENCE_CORPUS` — Philosophical Transactions, academy publications (as primary where appropriate).

Keep these corpora focused on primary traditions; monographs and modern journals remain in tiers B–D.

---

## Implementation notes
- Store call numbers as `node.call_number = "{class}.{division}.{id}"` or `meta.call_number` when importing.
- Index `node.call_number` for quick lookup and faceting.
- Validate `division` membership matches node label (e.g., `4.430.*` = Place/Country).
- Provide an administrative UI for assigning corpus tags and promoting evidence tiers when necessary.

---

If you'd like, I will:
- add `docs/guidelines/audit_queries.md` with Cypher queries for call-number checks, missing corpus tags, and temporal sanity,
- or scaffold `src/annals/models.py` to reflect `call_number`, `corpus_tier`, and `chron_key` fields and add a basic test.
