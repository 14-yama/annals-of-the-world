# Contributor Guide: Corpus Nodes & Major Corpora

This guide helps contributors seed, curate, and expand corpus nodes in the Annals of the World knowledge graph. It covers the structure for the Biblical corpus and outlines other major corpora to anticipate, ensuring consistency and interoperability across traditions.

---

## 1. What is a Corpus Node?
- A `:Corpus` node represents a canonical grouping of texts, traditions, or cultural artifacts.
- Used to organize evidence, link related entities, and support comparative analysis.
- Example: `BIBLICAL_CORPUS` for the Hebrew Bible, Dead Sea Scrolls, and related texts.

## 2. How to Seed a Corpus
- Create a `:Corpus` node with a unique slug, name, and description.
- Link `:Evidence` nodes to the corpus using `(:Evidence)-[:BELONGS_TO]->(:Corpus)`.
- Use corpus tiers (A–D) to indicate primary, peer-reviewed, institutional, or digital sources.
- Include major texts, entities, and their importance in the corpus description.

## 3. The Biblical Corpus (Example)
- **Texts:** Hebrew Bible/Tanakh, Septuagint, New Testament, Dead Sea Scrolls.
- **Entities:** Prophets, scribes, priesthoods, major places (Jerusalem, Babylon).
- **Importance:** Foundation for Abrahamic religions, law, literature, and historical chronology.
- **Cypher Example:**
  ```
  MERGE (c:Corpus {slug:'biblical_corpus', name:'Biblical Corpus'})
  MERGE (e:Evidence {slug:'dead_sea_scrolls'})
  MERGE (e)-[:BELONGS_TO]->(c)
  ```

## 4. Canonical Corpus Registry (v5 Model)

Below is the complete list of corpora recognized in the project, grouped by civilizational zone and consistent with international scholarly conventions (CIDOC, UNESCO, etc.).

### Ancient Near East & Mediterranean
- MESOPOTAMIAN_CORPUS: Sumerian & Akkadian texts — Enūma Eliš, Epic of Gilgamesh, royal inscriptions
- EGYPTIAN_CORPUS: Pyramid Texts, Coffin Texts, Book of the Dead, king lists
- BIBLICAL_CORPUS: Hebrew Bible / Tanakh, Septuagint, New Testament, Dead Sea Scrolls
- JUDAIC_RABBINIC_CORPUS: Mishnah, Talmud, Midrash
- GRAECO_ROMAN_CORPUS: Greek & Latin classics, philosophy, Roman law (Corpus Iuris Civilis)
- CANON_LAW_CORPUS: Gratian’s Decretum, papal decretals, conciliar acts

### Iran & Central / West Asia
- IRANIAN_ZOROASTRIAN_CORPUS: Avesta, Pahlavi theological texts
- ISLAMIC_QURAN_HADITH_CORPUS: Qur’an and canonical ḥadīth collections
- ISLAMIC_FIQH_KALAM_FALSAFA_CORPUS: Madhhab jurisprudence, kalām, falsafa
- PERSIANATE_CHRONICLE_CORPUS: Shāhnāmeh, Bāburnāma, royal court chronicles
- OTTOMAN_ARCHIVE_CORPUS: Kanunnames, Tahrir Defterleri (imperial registers)

### South & Southeast Asia
- INDIC_VEDIC_UPANISHAD_CORPUS: Vedas, Brāhmaṇas, Upaniṣads
- INDIC_EPIC_DHARMA_CORPUS: Mahābhārata, Rāmāyaṇa, Arthaśāstra, Dharmaśāstra
- BUDDHIST_PALI_CANON: Tipiṭaka (Pāli Canon)
- BUDDHIST_MAHAYANA_CORPORA: Sanskrit, Chinese, Tibetan canons
- SE_ASIAN_INSCRIPTIONAL_CORPUS: Khmer, Javanese, Thai inscriptions and chronicles

### East Asia
- SINIC_CLASSICS_CORPUS: Five Classics, Four Books, dynastic histories, military treatises
- JAPANESE_CLASSICAL_CORPUS: Kojiki, Nihon Shoki, Ritsuryō codes
- KOREAN_CLASSICAL_CORPUS: Samguk Sagi, Samguk Yusa, legal and historical chronicles

### Africa (Beyond Egypt)
- ETHIOSEMITIC_GEEZ_CORPUS: Kebra Nagast, Ethiopian royal chronicles
- TIMBUKTU_MANUSCRIPT_CORPUS: Arabic scholarship of the Western Sahel
- AFRICAN_ORAL_EPI_CYCLE: Transcribed epics such as Sundiata

### Americas
- MESOAMERICAN_CORPORA: Maya, Aztec, and Mixtec codices; Nahuatl annals
- ANDEAN_CORPUS: Khipu records and early colonial chronicles

### Technology / Science
- MILITARY_TECHNICAL_CORPUS_EARLY: Chinese, Islamic, and European ordnance treatises
- EARLY_MODERN_SCIENCE_CORPUS: Philosophical Transactions, early academies and natural philosophy papers

### Europe & Mediterranean (Post-Classical Traditions)
- BYZANTINE_CORPUS: Byzantine chronicles, legal codes, theological treatises
- SLAVIC_ORTHODOX_CORPUS: Russian Primary Chronicle, Orthodox liturgical texts
- MEDIEVAL_LATIN_CORPUS: Scholastic treatises, papal bulls, monastic rules
- CAROLINGIAN_FRANKISH_CORPUS: Capitularies, royal annals, Carolingian Renaissance texts
- IBERIAN_CORPUS: Mozarabic liturgy, Cantigas, fueros, chronicles
- ITALIAN_COMMUNAL_CORPUS: City statutes, communal chronicles, merchant manuals
- FRENCH_MEDIEVAL_CORPUS: Chansons de geste, Capetian chronicles, legal codes
- GERMANIC_MEDIEVAL_CORPUS: Sachsenspiegel, Nibelungenlied, imperial records
- CELTIC_MEDIEVAL_CORPUS: Irish annals, Welsh law codes, bardic poetry
- VIKING_NORDIC_CORPUS: Sagas, runic inscriptions, law codes
- OTTOMAN_BALKAN_CORPUS: Defters, imperial decrees, Balkan chronicles
- JUDEO_SEPHARDIC_CORPUS: Responsa, Ladino literature, communal records
- ARMENIAN_CORPUS: Medieval chronicles, liturgical texts, legal codes
- GEORGIAN_CORPUS: Chronicles, hagiographies, legal texts
- MAGYAR_HUNGARIAN_CORPUS: Gesta Hungarorum, medieval laws, chronicles
- POLISH_LITHUANIAN_CORPUS: Statutes, chronicles, union documents
- CZECH_BOHEMIAN_CORPUS: Hussite chronicles, law codes, annals
- BALKAN_SLAVIC_CORPUS: Serbian, Bulgarian, Croatian chronicles, legal codes
- ROMANIAN_MOLDAVIAN_CORPUS: Chronicles, princely decrees, church records
- VENETIAN_CORPUS: State archives, merchant manuals, chronicles
- SICILIAN_NORMAN_CORPUS: Multilingual chronicles, legal codes, poetry
- MALTESE_CORPUS: Notarial records, chronicles, legal codes
- CYPRIOT_CORPUS: Lusignan chronicles, legal codes, church records
- GREEK_MEDIEVAL_CORPUS: Byzantine, post-Byzantine chronicles, legal codes
- ALBANIAN_CORPUS: Chronicles, oral epics, legal codes

---

## 5. Corpus Tiers (A–F)

These corpora align with the Corpus discipline tiers for evidentiary rigor:

| Tier  | Type                  | Examples                                  |
| ----- | --------------------- | ----------------------------------------- |
| A     | Primary Corpus        | Direct texts (Bible, Vedas, Avesta, etc.) |
| B     | Peer-Reviewed         | Modern academic studies                   |
| C     | Scholarly Press       | Books from academic publishers            |
| D     | Institutional Reports | UNESCO, IMF, government archives          |
| E     | Archaeological        | Excavation records, inscriptions          |
| F     | Oral / Quantitative   | Documented oral histories, data series    |

---

## 6. Advanced Metadata Fields

Corpus nodes support extended metadata for scholarly auditability and interoperability:

| Field               | Type       | Description                                                   | Example                                    |
| ------------------- | ---------- | ------------------------------------------------------------- | ------------------------------------------ |
| `slug`              | string     | Unique identifier (UPPER_SNAKE_CASE)                          | `BIBLICAL_CORPUS`                          |
| `name`              | string     | Human-readable canonical name                                 | `Biblical Corpus`                          |
| `description`       | string     | Scholarly summary of the corpus                               | `Primary texts of the Abrahamic traditions`|
| `tier`              | A–F        | Evidentiary discipline tier                                   | `A`                                        |
| `civilizational_zone` | string   | Geographic/cultural region of origin                          | `Ancient Near East & Mediterranean`        |
| `primary_language`  | string     | Original language(s) of the core texts                        | `Hebrew, Aramaic, Koine Greek`             |
| `primary_script`    | string     | Script used in earliest surviving manuscripts                 | `Paleo-Hebrew, Square Hebrew, Greek uncial`|
| `transmission_mode` | string     | How the corpus was transmitted (manuscript, oral, inscription) | `manuscript, oral recitation`             |
| `date_range`        | string     | Approximate span of composition                               | `c. 1200 BCE – 100 CE`                    |
| `canonical_status`  | string     | Whether the corpus has an official "canon" definition          | `Closed (Tanakh), Open (Deuterocanon)`     |
| `tradition`         | string[]   | Religious/cultural traditions that claim the corpus            | `['Judaism', 'Christianity', 'Islam']`     |
| `related_corpora`   | string[]   | Slugs of related/sibling corpora                              | `['JUDAIC_RABBINIC_CORPUS']`               |
| `text_count`        | number     | Approximate number of distinct texts                          | `66` (Protestant Bible)                    |
| `evidence_slugs`    | string[]   | Linked evidence nodes                                         | `['dead_sea_scrolls', 'codex_sinaiticus']` |
| `unesco_domain`     | string     | UNESCO thematic domain alignment                              | `Written Heritage`                         |
| `cidoc_class`       | string     | CIDOC CRM class alignment                                     | `E73 Information Object`                   |

## 7. Implementation Tips (v4 Framework Structure)

### Linking Corpus → Text
Use `CONTAINS` for canonical membership, `INCLUDES` for broader association:
```cypher
MATCH (c:Corpus {slug:'BIBLICAL_CORPUS'})
MERGE (t:Text {slug:'genesis'})
MERGE (c)-[:CONTAINS {order:1, division:'Torah'}]->(t)
```

### Linking Corpus → Evidence
Evidence nodes `BELONGS_TO` a corpus when they attest to its textual content:
```cypher
MATCH (c:Corpus {slug:'BIBLICAL_CORPUS'})
MERGE (e:Evidence {slug:'dead_sea_scrolls'})
MERGE (e)-[:BELONGS_TO]->(c)
```

### Linking Corpus → Framework
Corpus nodes can be `FRAMES`-d by interpretive lenses:
```cypher
MATCH (c:Corpus {slug:'BIBLICAL_CORPUS'})
MERGE (f:Framework {slug:'TEXTUAL_TRANSMISSION'})
MERGE (c)-[:FRAMES]->(f)
```

### Corpus ↔ Corpus Hierarchies
Use `SUBSUMES` for parent–child and `IS_PART_OF` for part–whole:
```cypher
MATCH (parent:Corpus {slug:'BIBLICAL_CORPUS'})
MERGE (child:Corpus {slug:'JUDAIC_RABBINIC_CORPUS'})
MERGE (parent)-[:SUBSUMES]->(child)
```

## 8. Extended Modeling Patterns

### Pattern A: Book-Level Granularity
For large corpora, model individual books as `:Text` nodes connected via `CONTAINS`:
```
(:Corpus {slug:'BIBLICAL_CORPUS'})
  -[:CONTAINS {order:1, division:'Torah'}]->(:Text {slug:'genesis'})
  -[:CONTAINS {order:2, division:'Torah'}]->(:Text {slug:'exodus'})
  ...
  -[:CONTAINS {order:66, division:'Epistles'}]->(:Text {slug:'revelation'})
```

### Pattern B: Person → Text → Corpus Chain
Authors connect to texts which connect to corpora:
```
(:Person {slug:'moses'})-[:AUTHORS]->(:Text {slug:'genesis'})
(:Text {slug:'genesis'})<-[:CONTAINS]-(:Corpus {slug:'BIBLICAL_CORPUS'})
```

### Pattern C: Institution → Corpus Governance
Institutions canonize, standardize, or preserve corpora:
```
(:Institution {slug:'council_of_nicaea'})-[:CANONIZES]->(:Corpus {slug:'BIBLICAL_CORPUS'})
```

### Pattern D: Evidence Attestation
Archaeological evidence documents corpus claims:
```
(:Evidence {slug:'dead_sea_scrolls'})-[:DOCUMENTS]->(:Text {slug:'isaiah'})
(:Evidence {slug:'dead_sea_scrolls'})-[:BELONGS_TO]->(:Corpus {slug:'BIBLICAL_CORPUS'})
```

## 9. Full Canonical Corpus Registry Audit

### Status Key
- **Seeded**: Corpus node exists with basic metadata
- **Populated**: Corpus node has linked texts, persons, and evidence
- **Audited**: Corpus has been reviewed for completeness and accuracy
- **Gap**: Corpus is recognized but not yet seeded

### Audit Results (53 Corpora)

| # | Corpus Slug | Zone | Status | Text Count | Notes |
|---|-------------|------|--------|------------|-------|
| 1 | MESOPOTAMIAN_CORPUS | ANE | Gap | ~50 | Needs Enūma Eliš, Gilgamesh, Code of Hammurabi |
| 2 | EGYPTIAN_CORPUS | ANE | Gap | ~40 | Pyramid Texts, Book of the Dead |
| 3 | BIBLICAL_CORPUS | ANE | **Populated** | 66+ | Genesis–Revelation + DSS, Septuagint |
| 4 | JUDAIC_RABBINIC_CORPUS | ANE | Gap | ~30 | Mishnah, Talmud, Midrash |
| 5 | GRAECO_ROMAN_CORPUS | Mediterranean | Gap | ~100 | Homer to Justinian |
| 6 | CANON_LAW_CORPUS | Mediterranean | Gap | ~20 | Gratian's Decretum onward |
| 7 | IRANIAN_ZOROASTRIAN_CORPUS | Iran/CA | Gap | ~15 | Avesta, Pahlavi texts |
| 8 | ISLAMIC_QURAN_HADITH_CORPUS | Islamic | Gap | ~20 | Qur'an + six canonical hadith |
| 9 | ISLAMIC_FIQH_KALAM_FALSAFA_CORPUS | Islamic | Gap | ~40 | Jurisprudence, philosophy |
| 10 | PERSIANATE_CHRONICLE_CORPUS | Iran/CA | Gap | ~25 | Shāhnāmeh, court chronicles |
| 11 | OTTOMAN_ARCHIVE_CORPUS | Ottoman | Gap | ~30 | Imperial registers |
| 12 | INDIC_VEDIC_UPANISHAD_CORPUS | South Asia | Gap | ~20 | Vedas, Upaniṣads |
| 13 | INDIC_EPIC_DHARMA_CORPUS | South Asia | Gap | ~15 | Mahābhārata, Rāmāyaṇa |
| 14 | BUDDHIST_PALI_CANON | South/SE Asia | Gap | ~3 baskets | Tipiṭaka |
| 15 | BUDDHIST_MAHAYANA_CORPORA | East/South Asia | Gap | ~50 | Multi-tradition canons |
| 16 | SE_ASIAN_INSCRIPTIONAL_CORPUS | SE Asia | Gap | ~30 | Khmer, Javanese inscriptions |
| 17 | SINIC_CLASSICS_CORPUS | East Asia | Gap | ~20 | Five Classics, Four Books |
| 18 | JAPANESE_CLASSICAL_CORPUS | East Asia | Gap | ~15 | Kojiki, Nihon Shoki |
| 19 | KOREAN_CLASSICAL_CORPUS | East Asia | Gap | ~10 | Samguk Sagi |
| 20 | ETHIOSEMITIC_GEEZ_CORPUS | Africa | Gap | ~15 | Kebra Nagast |
| 21 | TIMBUKTU_MANUSCRIPT_CORPUS | Africa | Gap | ~20 | Sahel scholarship |
| 22 | AFRICAN_ORAL_EPI_CYCLE | Africa | Gap | ~10 | Sundiata cycle |
| 23 | MESOAMERICAN_CORPORA | Americas | Gap | ~15 | Maya/Aztec codices |
| 24 | ANDEAN_CORPUS | Americas | Gap | ~10 | Khipu records |
| 25–49 | European post-classical | Europe | Gap | varies | 25 traditions listed above |
| 50 | MILITARY_TECHNICAL_CORPUS_EARLY | Cross-civ | Gap | ~20 | Ordnance treatises |
| 51 | EARLY_MODERN_SCIENCE_CORPUS | Cross-civ | Gap | ~30 | Phil. Transactions |
| 52 | OTTOMAN_BALKAN_CORPUS | Balkans | Gap | ~15 | Imperial Balkan records |
| 53 | PALESTINIAN_OTTOMAN_CORPUS | Levant | Gap | ~10 | Ottoman Palestine records |

**Priority**: BIBLICAL_CORPUS (Tier A, populated) → GRAECO_ROMAN_CORPUS → ISLAMIC_QURAN_HADITH_CORPUS → INDIC_VEDIC_UPANISHAD_CORPUS

## 10. Contributor Checklist (Expanded)

- [ ] Use unique slugs (UPPER_SNAKE_CASE) and descriptive names for corpus nodes
- [ ] Include all advanced metadata fields (language, script, transmission, tier)
- [ ] Link evidence and major texts to the corpus using `BELONGS_TO` / `CONTAINS`
- [ ] Document entities and importance in the corpus description
- [ ] Follow schema and classification guidelines for consistency
- [ ] Add `related_corpora` cross-references for sibling/parent corpora
- [ ] Include `tradition` array for multi-tradition corpora
- [ ] Specify `canonical_status` (Open, Closed, Disputed)
- [ ] Map to UNESCO domain and CIDOC CRM class where applicable
- [ ] Register corpus in the Canonical Corpus Registry (Section 9)
- [ ] Anticipate and propose new corpora as the project expands
- [ ] Update `callNumbers.ts` if a new classification division is needed

---

For more details, see:
- [Schema Reference](./schema.md)
- [Classification & Corpus Registry](./classification.md)
- [Node Descriptions](./node_descriptions.md)
- [Interaction Matrix](./interaction_matrix.md)
- [Relations Vocabulary](./node-relationship-vocabulary.md)
