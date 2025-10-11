---
title: Interaction Matrix — Allowed Node-Type Pairs & Verbs
status: DRAFT
version: 0.2
summary: Allowed interactions between node categories (Person, Institution, Text/Artifact, Doctrine/Idea, Movement, Event, Place, Framework, Evidence) grouped by type with canonical vs. contextual verbs and example triples.
---

# Interaction Matrix (Node-Type → Node-Type)

Purpose: Make it easy to see how nodes can interact. This file complements `relations_vocabulary.md`:
- Canonical verbs = defined in the core/supplementary lists there.
- Contextual verbs (proposed) = used in clusters or evidence matrix but not yet promoted to the canon; add via proposal if needed.
 - Governance: See [Policy](../governance/GOVERNANCE.md) and [Audit Log](../governance/audit_log.md) for decision records and process.

Compliance
- Use only verbs from `relations_vocabulary.md`. Any deviations must first be proposed and approved; otherwise normalize before merge.

Legend (node categories)
- P = Person
- I = Institution
- T = Text/Artifact
- D = Doctrine/Idea
- M = Movement
- E = Event/Process
- L = Place/Location
- F = Framework lens
- V = Evidence node

Notes
- Prefer a specific canonical verb over INFLUENCES when possible.
- Framework (F) is a target only; use FRAMES from content nodes to a Framework lens.
- Place (L) is typically a target of OCCURS_IN and DIFFUSES; avoid generic Place → X edges.
- Evidence (V) usually documents content; use evidence-only verbs sparingly and register them if broad reuse is expected.

## Quick Pair Matrix (overview)

From \ To | P | I | T | D | M | E | L | F | V
:--|:--|:--|:--|:--|:--|:--|:--|:--|:--
P | COLLABORATES_WITH; DEBATES; INFLUENCES; MARRIES; PARENT_OF; SUCCEEDS; TEACHES; STUDIES_UNDER | ESTABLISHES; INFLUENCES; DECLARES | AUTHORS; TRANSLATES; PUBLISHES; EDITS; COMMENTATES_ON; INTERPRETS; COPIES; COMPILES | ADOPTS; REJECTS; INTERPRETS; DECLARES; DEFINES; ADVOCATES; CRITIQUES | ADOPTS; REJECTS; PROMOTES; INFLUENCES | DECLARES; PROPHESIES_DURING; SURVIVES; PARTICIPATES_IN; LEADS | DIFFUSES | FRAMES | —
I | DECLARES; INFLUENCES | SCHISMS_FROM; RECONCILES_WITH; INFLUENCES | CANONIZES; STANDARDIZES; PRESERVES; PUBLISHES; EDITS; DISTRIBUTES; PRODUCES | CANONIZES; STANDARDIZES; REJECTS; DECLARES; DEFINES; PROMULGATES; PROHIBITS; SANCTIONS; REGULATES | PROMOTES; REJECTS; INFLUENCES | ORGANIZES; DECLARES; PRESIDES_OVER; ORDERS; LEADS | DIFFUSES | FRAMES | —
T | INFLUENCES | INFLUENCES | TRANSMITS; TRANSLATES; COPIES; COMPILES | INTERPRETS; TRANSMITS; EXEMPLIFIES; QUOTES; REFUTES | INFLUENCES; TRANSMITS | ENABLES; CAUSES | DIFFUSES | FRAMES | —
D | INFLUENCES | INFLUENCES | INFLUENCES | INFLUENCES | INFLUENCES | CAUSES; FRAMES | DIFFUSES | FRAMES | —
M | INFLUENCES | SCHISMS_FROM; RECONCILES_WITH; INFLUENCES | INFLUENCES; TRANSMITS; ADOPTS; REJECTS | INFLUENCES; TRANSMITS; ADOPTS; REJECTS | SCHISMS_FROM; RECONCILES_WITH; INFLUENCES | CAUSES; ORGANIZES; LEADS | DIFFUSES | FRAMES | —
E | — | — | — | TRANSFORMS; CAUSES; ENABLES | TRANSFORMS; CAUSES; ENABLES | CAUSES; PRECEDES; IS_PART_OF | OCCURS_IN | FRAMES | —
L | — | — | — | — | — | — | (target-only) | — | —
F | — | — | — | — | — | — | — | (target-only) | —
V | DOCUMENTS | DOCUMENTS | DOCUMENTS | ATTESTS_TO | DOCUMENTS | DATES; DOCUMENTS | — | — | —

## P (Person) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| P | P | COLLABORATES_WITH; DEBATES; INFLUENCES; MARRIES; PARENT_OF; SUCCEEDS; TEACHES; STUDIES_UNDER | Heschel COLLABORATES_WITH King |
| P | I | ESTABLISHES; INFLUENCES; DECLARES | Leader ESTABLISHES Council |
| P | T | AUTHORS; TRANSLATES; PUBLISHES; EDITS; COMMENTATES_ON; INTERPRETS; COPIES; COMPILES | Rashi COMMENTATES_ON Talmud |
| P | D | ADOPTS; REJECTS; INTERPRETS; DECLARES; DEFINES | Maimonides INTERPRETS Jewish_Philosophy |
| P | M | ADOPTS; REJECTS; PROMOTES; INFLUENCES | Thinker PROMOTES Haskalah |
| P | E | DECLARES; PROPHESIES_DURING; SURVIVES; PARTICIPATES_IN; LEADS | Jeremiah PROPHESIES_DURING Babylonian_Exile |
| P | L | DIFFUSES | Teacher DIFFUSES Practice (to Place via practice chain) |
| P | F | FRAMES | Author FRAMES TEXTUAL_TRANSMISSION |
- ↔ P
  - Canonical: COLLABORATES_WITH, DEBATES, INFLUENCES, MARRIES, PARENT_OF, SUCCEEDS, TEACHES, STUDIES_UNDER
  - Example: (Abraham_Joshua_Heschel) COLLABORATES_WITH (Martin_Luther_King)
- → I
  - Canonical: ESTABLISHES, INFLUENCES, DECLARES
  - Example: (Leader) ESTABLISHES (Council)
- → T
  - Canonical: AUTHORS, TRANSLATES, PUBLISHES, EDITS, COMMENTATES_ON, INTERPRETS, COPIES, COMPILES
  - Example: (Rashi) COMMENTATES_ON (Talmud)
- → D
  - Canonical: ADOPTS, REJECTS, INTERPRETS, DECLARES, DEFINES, INFLUENCES
  - Example: (Maimonides) INTERPRETS (Jewish_Philosophy)
- → M
  - Canonical: ADOPTS, REJECTS, PROMOTES, INFLUENCES
  - Example: (Thinker) PROMOTES (Haskalah)
- → E
  - Canonical: DECLARES; Supplementary: PROPHESIES_DURING, SURVIVES, PARTICIPATES_IN, LEADS
  - Example: (Jeremiah) PROPHESIES_DURING (Babylonian_Exile)
- → L
  - Canonical: DIFFUSES
  - Example: (Teacher) DIFFUSES (Practice) → target L via practice chain (see notes)
- → F
  - Canonical: FRAMES
  - Example: (Author) FRAMES (TEXTUAL_TRANSMISSION)
- → V
  - Typically N/A (use V → content edge)

## I (Institution) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| I | I | SCHISMS_FROM; RECONCILES_WITH; INFLUENCES | Synod SCHISMS_FROM Patriarchate |
| I | P | DECLARES; INFLUENCES | Council DECLARES Office |
| I | T | CANONIZES; STANDARDIZES; PRESERVES; PUBLISHES; EDITS; DISTRIBUTES; PRODUCES | Church CANONIZES Text |
| I | D | CANONIZES; STANDARDIZES; REJECTS; DECLARES | Academy STANDARDIZES Curriculum |
| I | M | PROMOTES; REJECTS; INFLUENCES | Institution PROMOTES Movement |
| I | E | ORGANIZES; DECLARES | Committee ORGANIZES Congress |
| I | L | DIFFUSES | Order DIFFUSES Practices (region) |
| I | F | FRAMES | Institution FRAMES DOCTRINE_DEVELOPMENT |
- ↔ I
  - Canonical: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- → P
  - Canonical: DECLARES, INFLUENCES
- → T
  - Canonical: CANONIZES, STANDARDIZES, PRESERVES, PUBLISHES, EDITS, DISTRIBUTES, PRODUCES
- → D
  - Canonical: CANONIZES, STANDARDIZES, REJECTS, DECLARES, DEFINES, PROMULGATES, PROHIBITS, SANCTIONS, REGULATES
- → M
  - Canonical: PROMOTES, REJECTS, INFLUENCES
- → E
  - Canonical: ORGANIZES, DECLARES
- → L
  - Canonical: DIFFUSES (institutional reach)
- → F
  - Canonical: FRAMES
- → V
  - Typically N/A

## T (Text/Artifact) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| T | T | TRANSMITS; TRANSLATES | Septuagint TRANSMITS Hebrew_Scriptures_Greek_Tradition |
| T | D | INTERPRETS; TRANSMITS; EXEMPLIFIES | Text EXEMPLIFIES Doctrine |
| T | M | INFLUENCES; TRANSMITS | Treatise INFLUENCES Movement |
| T | P/I | INFLUENCES | Work INFLUENCES Scholar |
| T | E | ENABLES; CAUSES | Manual ENABLES Practice_Event |
| T | L | DIFFUSES | Manuscript DIFFUSES Region |
| T | F | FRAMES | Text FRAMES TEXTUAL_TRANSMISSION |
- ↔ T
  - Canonical: TRANSLATES (via P/I actor), TRANSMITS
  - Example: (Septuagint) TRANSMITS (Hebrew_Scriptures_Greek_Tradition)
- → D
  - Canonical: INTERPRETS, TRANSMITS, EXEMPLIFIES (supplementary)
- → M
  - Canonical: INFLUENCES, TRANSMITS
- → P/I
  - Canonical: INFLUENCES
- → E
  - Canonical: ENABLES (supplementary), CAUSES (rare, use carefully)
- → L
  - Canonical: DIFFUSES (via circulation)
- → F
  - Canonical: FRAMES (when a text explicitly frames a lens)
- → V
  - Typically N/A

## D (Doctrine/Idea) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| D | D/T/M/P/I | INFLUENCES; ADOPTS; REJECTS; STANDARDIZES (via I/P) | Doctrine INFLUENCES Institution |
| D | E | CAUSES; FRAMES | Doctrine CAUSES Reform_Event |
| D | L | DIFFUSES | Idea DIFFUSES Region |
| D | F | FRAMES | Theory FRAMES CAUSE_AND_EFFECT |
- → D/T/M/P/I
  - Canonical: INFLUENCES, ADOPTS, REJECTS (as appropriate), CAUSES (for doctrinal causality), STANDARDIZES (via I/P)
- → E
  - Canonical: CAUSES (if doctrine prompts event), FRAMES (lens)
- → L
  - Canonical: DIFFUSES
- → F
  - Canonical: FRAMES
- → V
  - Typically N/A

## M (Movement) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| M | M/I | SCHISMS_FROM; RECONCILES_WITH; INFLUENCES | Sect SCHISMS_FROM Movement |
| M | P | INFLUENCES | Movement INFLUENCES Leader |
| M | T/D | INFLUENCES; TRANSMITS; ADOPTS; REJECTS | Movement ADOPTS Doctrine |
| M | E | CAUSES; ORGANIZES | Movement ORGANIZES Congress |
| M | L | DIFFUSES | Movement DIFFUSES Geography |
| M | F | FRAMES | Movement FRAMES CULTURAL_DIFFUSION |
- ↔ M/I
  - Canonical: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- → P
  - Canonical: INFLUENCES
- → T/D
  - Canonical: INFLUENCES, TRANSMITS, ADOPTS, REJECTS
- → E
  - Canonical: CAUSES, ORGANIZES (via P/I operatives), LEADS
- → L
  - Canonical: DIFFUSES
- → F
  - Canonical: FRAMES
- → V
  - Typically N/A

## E (Event/Process) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| E | E | CAUSES; PRECEDES; IS_PART_OF | Event PRECEDES Event |
| E | D/I/T/M | TRANSFORMS; CAUSES; ENABLES | War TRANSFORMS Institution |
| E | L | OCCURS_IN | Battle OCCURS_IN Place |
| E | F | FRAMES | Event FRAMES GEOPOLITICAL_LINKAGE |
- ↔ E
  - Canonical: CAUSES (for “triggers”); Supplementary: PRECEDES, IS_PART_OF
- → D/I/T/M
  - Canonical: TRANSFORMS, CAUSES, ENABLES
- → L
  - Canonical: OCCURS_IN
- → F
  - Canonical: FRAMES (when an event is presented through a lens)
- → V
  - Typically N/A (use V → E)

## L (Place/Location) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| L | — | Target-only | — |
- Typically a target only
  - Receives: OCCURS_IN (from E), DIFFUSES (from P/I/M/T/D)
  - Avoid Place → X edges unless narrowly justified (e.g., ADMINISTERS for polities modeled as I)

## F (Framework lens) → …

| From | To | Canonical verbs | Example |
|:--|:--|:--|:--|
| F | — | Target-only | — |
- Target only
  - Receives: FRAMES from content nodes

## V (Evidence node) → …

| From | To | Evidence verbs (proposed) | Example |
|:--|:--|:--|:--|
| V | P/I/T/D/M | ATTESTS_TO; DOCUMENTS; CORROBORATES; VALIDATES; PROVIDES | DSS Publication DOCUMENTS Dead_Sea_Scrolls |
| V | E | DATES; DOCUMENTS | IAA Reports DATES Excavation_Findings |
| V | L/F/V | — | — |
- Evidence-only verbs (proposed; register in vocabulary if reused broadly)
  - ATTESTS_TO, DOCUMENTS, CORROBORATES, DATES, VALIDATES, PROVIDES, REPORTS
  - Examples:
    - (Dead_Sea_Scrolls_Publication) DOCUMENTS (Dead_Sea_Scrolls)
    - (Ketef_Hinnom_Amulets) ATTESTS_TO (Priestly_Blessing_Formulas)
    - (IAA_Reports) DATES (Excavation_Findings)

---

## Annex — Quick Pair Index
- P ↔ P: COLLABORATES_WITH, DEBATES, INFLUENCES, MARRIES, PARENT_OF, SUCCEEDS, TEACHES, STUDIES_UNDER
- P → I: ESTABLISHES, INFLUENCES, DECLARES
- P → T: AUTHORS, TRANSLATES, PUBLISHES, EDITS, COMMENTATES_ON, INTERPRETS, COPIES, COMPILES
- P → D: ADOPTS, REJECTS, INTERPRETS, DECLARES, DEFINES, INFLUENCES
- P → M: ADOPTS, REJECTS, PROMOTES, INFLUENCES
- P → E: DECLARES, PROPHESIES_DURING, SURVIVES, PARTICIPATES_IN, LEADS
- P → L: DIFFUSES
- P → F: FRAMES

- I ↔ I: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- I → P: DECLARES, INFLUENCES
- I → T: CANONIZES, STANDARDIZES, PRESERVES, PUBLISHES, EDITS, DISTRIBUTES, PRODUCES
- I → D: CANONIZES, STANDARDIZES, REJECTS, DECLARES, DEFINES, PROMULGATES, PROHIBITS, SANCTIONS, REGULATES
- I → M: PROMOTES, REJECTS, INFLUENCES
- I → E: ORGANIZES, DECLARES
- I → L: DIFFUSES
- I → F: FRAMES

- T ↔ T: TRANSMITS, TRANSLATES
- T → D: INTERPRETS, TRANSMITS, EXEMPLIFIES
- T → M: INFLUENCES, TRANSMITS
- T → P/I: INFLUENCES
- T → E: ENABLES, CAUSES (rare)
- T → L: DIFFUSES
- T → F: FRAMES

- D → D/T/M/P/I: INFLUENCES, ADOPTS, REJECTS, CAUSES
- D → E: CAUSES, FRAMES
- D → L: DIFFUSES
- D → F: FRAMES

- M ↔ M/I: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- M → P: INFLUENCES
- M → T/D: INFLUENCES, TRANSMITS, ADOPTS, REJECTS
- M → E: CAUSES, ORGANIZES, LEADS
- M → L: DIFFUSES
- M → F: FRAMES

- E ↔ E: CAUSES; PRECEDES, IS_PART_OF
- E → D/I/T/M: TRANSFORMS, CAUSES, ENABLES
- E → L: OCCURS_IN
- E → F: FRAMES

- L: target only (OCCURS_IN, DIFFUSES)
- F: target only (FRAMES)
- V → content: ATTESTS_TO, DOCUMENTS, CORROBORATES, DATES, VALIDATES, PROVIDES, REPORTS

## Change Log
- 0.2 Added overview matrix and per-section tables for readability.
- 0.1 Initial matrix drafted from current `relations_vocabulary.md` canon + limited contextual verbs.
