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

## 6. Contributor Checklist
...existing code...

## 5. Contributor Checklist
- [ ] Use unique slugs and descriptive names for corpus nodes.
- [ ] Link evidence and major texts to the corpus using `BELONGS_TO`.
- [ ] Document entities and importance in the corpus description.
- [ ] Follow schema and classification guidelines for consistency.
- [ ] Anticipate and propose new corpora as the project expands.

---

For more details, see:
- [Schema Reference](./schema.md)
- [Classification & Corpus Registry](./classification.md)
- [Node Descriptions](./node_descriptions.md)
