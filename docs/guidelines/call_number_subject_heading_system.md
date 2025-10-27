# Contributor Guide: Understanding the Classification & Call Number System

Welcome, contributor! This guide explains the classification and subject heading system used in the Annals of the World knowledge graph. Before making a contribution, review this document to understand how nodes are organized, how to assign class numbers, and why "Idea" is the generative core of our schema.

## Why "Idea" Is the Generative Core

All historical change and structure in our graph originates from ideas. Every person, institution, movement, event, artifact, and even evidence ultimately traces back to an originating idea. "Idea" is the root of causality and intellectual lineage, while "Timeframe" provides universal context. This approach aligns with international scholarly conventions and supports robust, queryable graph modeling.

**Key Principles:**
- Nodes are classified by type and assigned a class number (see below).
- "Idea" is always Class 0—the generative source for all other nodes.
- "Timeframe" (Class 9) anchors nodes in history but does not drive causality.
- Use call numbers and subject headings for navigation, curation, and scholarly search.

---

## 1. Top-Level Classes (0–9)

| Class | Heading                    | Node Types |
|-------|----------------------------|------------|
| 0     | Ideas – Core Categories    | Political, Ethical, Legal |
| 1     | Ideas – Other Theories     | Economic, Scientific, Technological, Religious, Cultural, Environmental, Artistic |
| 2     | People                     | Philosophers, Leaders, Scientists, Activists, Artists |
| 3     | Institutions               | Political, Legal, Economic, Religious, Scientific, Cultural, International |
| 4     | Places                     | Continent, Region, Country, City, Empire, Civilization, Culture-area |
| 5     | Events                     | Wars, Revolutions, Elections, Scientific Discoveries, Environmental Crises |
| 6     | Movements                  | Political, Social, Religious, Cultural, Scientific, Technological, Environmental |
| 7     | Artifacts & Texts          | Constitutions, Codes, Scriptures, Scientific Works, Artworks, Technologies |
| 8     | Evidence                   | Primary, Secondary, Archaeological, Quantitative, Oral |
| 9     | Timeframes                 | Period, Era, Epoch |
| 10    | Corpus                     | Canonical Texts, Traditions, Artifacts |

---

## 2. Second-Level Divisions

Each class subdivides into thematic categories, e.g.:

- **0 – Ideas (Core)**
  - 010 Political Systems & Governance
  - 020 Ethical Systems
  - 030 Legal Systems & Law
- **1 – Ideas (Other)**
  - 110 Economic Theories & Systems
  - 120 Scientific Paradigms
  - 130 Technological Innovations
  - 140 Religious & Philosophical Concepts
  - 150 Social & Cultural Theories
  - 160 Environmental & Ecological Ideas
  - 170 Artistic & Aesthetic Movements
- **2 – People**
  - 210 Philosophers & Thinkers
  - 220 Political Leaders
  - 230 Legal Figures
  - 240 Scientists & Inventors
  - 250 Religious Figures
  - 260 Artists & Writers
  - 270 Activists & Reformers
- **3 – Institutions**
  - 310 Political Institutions
  - 320 Legal Institutions
  - 330 Economic Institutions
  - 340 Religious Institutions
  - 350 Scientific Institutions
  - 360 Cultural Institutions
  - 370 International Organizations
- **4 – Places**
  - 410 Continents
  - 420 Regions
  - 430 Countries / Polities
  - 440 Cities
  - 450 Empires / Dynasties
  - 460 Civilizations
  - 470 Culture Areas
- **5 – Events**
  - 510 Wars & Conflicts
  - 520 Revolutions & Uprisings
  - 530 Elections & Shifts
  - 540 Legal Cases
  - 550 Scientific Discoveries
  - 560 Technological Breakthroughs
  - 570 Religious Events
  - 580 Environmental Events
- **6 – Movements**
  - 610 Political Movements
  - 620 Social Movements
  - 630 Religious Movements
  - 640 Cultural Movements
  - 650 Scientific Movements
  - 660 Technological Movements
  - 670 Environmental Movements
- **7 – Artifacts & Texts**
  - 710 Constitutions & Charters
  - 720 Legal Codes
  - 730 Religious Texts
  - 740 Philosophical Works
  - 750 Scientific Texts
  - 760 Artworks
  - 770 Technological Artifacts
- **8 – Evidence**
  - 810 Primary Sources
  - 820 Secondary Sources
  - 830 Archaeological Evidence
  - 840 Quantitative Data
  - 850 Oral Traditions
- **9 – Timeframes**
  - 910 Prehistoric
  - 920 Classical
  - 930 Medieval
  - 940 Early Modern
  - 950 Modern
  - 960 Contemporary
- **10 – Corpus**
  - 101 Canonical Textual Corpora
  - 102 Cultural Artifact Groupings
  - 103 Scholarly Tradition Registries
  - 104 Comparative Corpus Sets

---

## 3. Call Number Format

`[Class].[Division].[ID]`
- **Class**: 0–9 (top-level type)
- **Division**: subcategory (2–3 digits)
- **ID**: Neo4j slug or local sequential number

**Examples:**
- `020.12-human-rights` → Ethical Systems, Human Rights
- `030.21-constitutional-law` → Legal Systems, Constitutional Law
- `510.34-ww2-asia` → Event, War, WWII in Asia
- `710.05-magna-carta` → Artifact/Text, Constitution, Magna Carta
- `10.101.biblical_corpus` → Corpus, Canonical Textual Corpora, Biblical Corpus

---

## 4. Subject Headings (LCSH-style)

Each node gets one or more controlled subject headings for scholarly navigation.

**Examples:**
- Human Rights
  - Subject Heading: Ethical Systems — Rights — Universal
  - Call Number: 020.12-human-rights
- Magna Carta
  - Subject Heading: Legal Texts — Constitutional — England — Medieval
  - Call Number: 710.05-magna-carta
- Industrial Revolution
  - Subject Heading: Events — Technological Breakthroughs — Britain — Modern
  - Call Number: 560.01-industrial-revolution
- Biblical Corpus
  - Subject Heading: Religious Texts — Canonical — Judeo-Christian
  - Call Number: 10.101.biblical_corpus


## 5. Why This Matters
- Every node has a fixed anchor (call number) for navigation and reference.
- Subject headings support scholarly search and comparison.
- The system is scalable: new categories slot into the schedule without breaking structure.
- Aligned with your active canonical verbs and schema.

---

## 6. Real Historical Examples (Graph Links)

**Event + Primary Evidence**
- Event: Assassination of Archduke Franz Ferdinand (1914)
- Person: Gavrilo Princip
- Evidence: Court transcript, preserved pistol, folk songs
- Graph Links:
  - (:Person {name:"Gavrilo Princip"})-[:PARTICIPATES_IN]->(:Event {name:"Assassination of Archduke Franz Ferdinand"})
  - (:Evidence {type:"Primary Source", title:"Trial transcript of Gavrilo Princip"})-[:EVIDENCES]->(:Event {name:"Assassination of Archduke Franz Ferdinand"})

**Idea + Secondary Evidence**
- Idea: Marxism
- Institution: Soviet Communist Party
- Evidence: Popper’s critique, Soviet economic data
- Graph Links:
  - (:Idea {name:"Marxism"})-[:INFLUENCES]->(:Institution {name:"Soviet Communist Party"})
  - (:Evidence {type:"Secondary Source", title:"Popper - The Open Society and Its Enemies"})-[:EVIDENCES]->(:Idea {name:"Marxism"})

**Person + Oral Tradition + Archaeology**
- Person: Homer
- Idea: Epic Poetry
- Evidence: Oral transmission, Troy excavations
- Graph Links:
  - (:Person {name:"Homer"})-[:CREATES]->(:Idea {name:"Epic Poetry"})
  - (:Evidence {type:"Oral Tradition", title:"Oral transmission of Iliad & Odyssey"})-[:EVIDENCES]->(:Person {name:"Homer"})

**Event + Quantitative Data + Secondary**
- Event: Black Death Pandemic (1347–1351)
- Idea: Miasma Theory
- Evidence: Mortality records, Tuchman’s synthesis, Boccaccio’s eyewitness account
- Graph Links:
  - (:Event {name:"Black Death"})-[:INFLUENCES]->(:Idea {name:"Miasma Theory"})
  - (:Evidence {type:"Quantitative Data", title:"English manorial rolls - mortality rates"})-[:EVIDENCES]->(:Event {name:"Black Death"})

---

## 7. Directional Cheat-Sheet (Canonical Verbs)
- Idea INFLUENCES Idea
- Idea CAUSES Event
- Event RESULTS_IN Idea
- Person PROPOSES Idea; WRITES Artifact; FOUNDS/LEADS Institution/Movement; PARTICIPATES_IN Event
- Institution GOVERNS Place; CODIFIES/IMPLEMENTS Idea; CONVENES Event; PROMULGATES Artifact
- Movement CENTERS_ON Idea; EMERGES_IN Place; CHALLENGES Institution; ESCALATES Event
- Artifact SYMBOLIZES/ENACTS/DOCUMENTS Idea/Event/Institution/Movement; ATTRIBUTES_TO Person/Institution
- Event OCCURS_IN Place; FALLS_WITHIN Period/Era/Epoch; EventWindow DELINEATES Event
- Evidence EVIDENCES (Idea | Event | Person | Institution | Movement | Artifact | Place)


## 8. Relationship Diagram: Core Classes

Below is a conceptual diagram showing how the core classes relate, with **Idea** as the generative core and **Timeframe** as the universal context:

```
           [Timeframe]
                |
                v
             [Idea] <-------------------+
                |                       |
                v                       |
   +--------+---+---+--------+          |
   |        |       |        |          |
 [Person] [Institution] [Movement]      |
   |        |       |        |          |
   v        v       v        v          |
 [Event] [Artifact/Text] [Place]        |
   |        |       |        |          |
   v        v       v        v          |
           [Evidence]                   |
                ^                       |
                |                       |
                +-----------------------+
```

**Legend:**
- Arrows show direction of influence or anchoring.
- "Idea" is the generative source; all other nodes derive from or are shaped by ideas.
- "Timeframe" provides context for all nodes, including ideas.
- "Evidence" substantiates any node, supporting provenance and auditability.

- "Idea" is the generative core (Class 0), per international conventions and schema logic.
- "Timeframe" (Class 9) is the universal context, anchoring all nodes but not driving causality.
- This structure supports causality, provenance, and scalable navigation.

---

## 9. Next Steps
- Integrate call numbers and subject headings into node metadata.
- Use this schedule for curation, ingestion, and scholarly navigation.
- Optionally, formalize Evidence schema for Neo4j (enums, constraints, citation fields).
