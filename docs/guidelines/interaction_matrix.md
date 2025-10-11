---
title: Interaction Matrix — Allowed Node-Type Pairs & Verbs
status: DRAFT
version: 0.1
summary: Allowed interactions between node categories (Person, Institution, Text/Artifact, Doctrine/Idea, Movement, Event, Place, Framework, Evidence) grouped by type with canonical vs. contextual verbs and example triples.
---

# Interaction Matrix (Node-Type → Node-Type)

Purpose: Make it easy to see how nodes can interact. This file complements `relations_vocabulary.md`:
- Canonical verbs = defined in the core/supplementary lists there.
- Contextual verbs (proposed) = used in clusters or evidence matrix but not yet promoted to the canon; add via proposal if needed.

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

## P (Person) → …
- ↔ P
  - Canonical: COLLABORATES_WITH, DEBATES, INFLUENCES
  - Example: (Abraham_Joshua_Heschel) COLLABORATES_WITH (Martin_Luther_King)
- → I
  - Canonical: ESTABLISHES, INFLUENCES, DECLARES
  - Example: (Leader) ESTABLISHES (Council)
- → T
  - Canonical: TRANSLATES, PUBLISHES, EDITS, COMMENTATES_ON, INTERPRETS, SYSTEMATIZES
  - Example: (Rashi) COMMENTATES_ON (Talmud)
- → D
  - Canonical: ADOPTS, REJECTS, INTERPRETS, SYSTEMATIZES, DECLARES, INFLUENCES
  - Example: (Maimonides) SYSTEMATIZES (Jewish_Philosophy)
- → M
  - Canonical: ADOPTS, REJECTS, PROMOTES, INFLUENCES
  - Example: (Thinker) PROMOTES (Haskalah)
- → E
  - Canonical: DECLARES, PROPHESIES_DURING (supplementary), SURVIVES (supplementary)
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
- ↔ I
  - Canonical: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- → P
  - Canonical: DECLARES, INFLUENCES
- → T
  - Canonical: CANONIZES, STANDARDIZES, PRESERVES, PUBLISHES, EDITS, DISTRIBUTES
- → D
  - Canonical: CANONIZES, STANDARDIZES, REJECTS, DECLARES
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
- ↔ M/I
  - Canonical: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- → P
  - Canonical: INFLUENCES
- → T/D
  - Canonical: INFLUENCES, TRANSMITS, ADOPTS, REJECTS
- → E
  - Canonical: CAUSES, ORGANIZES (via P/I operatives)
- → L
  - Canonical: DIFFUSES
- → F
  - Canonical: FRAMES
- → V
  - Typically N/A

## E (Event/Process) → …
- ↔ E
  - Canonical: CAUSES (for “triggers”); Contextual (proposed): PRECEDES, IS_PART_OF
- → D/I/T/M
  - Canonical: TRANSFORMS (supplementary), CAUSES, ENABLES
- → L
  - Canonical: OCCURS_IN
- → F
  - Canonical: FRAMES (when an event is presented through a lens)
- → V
  - Typically N/A (use V → E)

## L (Place/Location) → …
- Typically a target only
  - Receives: OCCURS_IN (from E), DIFFUSES (from P/I/M/T/D)
  - Avoid Place → X edges unless narrowly justified (e.g., ADMINISTERS for polities modeled as I)

## F (Framework lens) → …
- Target only
  - Receives: FRAMES from content nodes

## V (Evidence node) → …
- Evidence-only verbs (proposed; register in vocabulary if reused broadly)
  - ATTESTS_TO, DOCUMENTS, CORROBORATES, DATES, VALIDATES, PROVIDES, FACILITATES, REPORTS
  - Examples:
    - (Dead_Sea_Scrolls_Publication) DOCUMENTS (Dead_Sea_Scrolls)
    - (Ketef_Hinnom_Amulets) ATTESTS_TO (Priestly_Blessing_Formulas)
    - (IAA_Reports) DATES (Excavation_Findings)

---

## Annex — Quick Pair Index
- P ↔ P: COLLABORATES_WITH, DEBATES, INFLUENCES
- P → I: ESTABLISHES, INFLUENCES, DECLARES
- P → T: TRANSLATES, PUBLISHES, EDITS, COMMENTATES_ON, INTERPRETS, SYSTEMATIZES
- P → D: ADOPTS, REJECTS, INTERPRETS, SYSTEMATIZES, DECLARES, INFLUENCES
- P → M: ADOPTS, REJECTS, PROMOTES, INFLUENCES
- P → E: DECLARES, PROPHESIES_DURING, SURVIVES
- P → L: DIFFUSES
- P → F: FRAMES

- I ↔ I: SCHISMS_FROM, RECONCILES_WITH, INFLUENCES
- I → P: DECLARES, INFLUENCES
- I → T: CANONIZES, STANDARDIZES, PRESERVES, PUBLISHES, EDITS, DISTRIBUTES
- I → D: CANONIZES, STANDARDIZES, REJECTS, DECLARES
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
- M → E: CAUSES, ORGANIZES
- M → L: DIFFUSES
- M → F: FRAMES

- E ↔ E: CAUSES; (proposed) PRECEDES, IS_PART_OF
- E → D/I/T/M: TRANSFORMS, CAUSES, ENABLES
- E → L: OCCURS_IN
- E → F: FRAMES

- L: target only (OCCURS_IN, DIFFUSES)
- F: target only (FRAMES)
- V → content: ATTESTS_TO, DOCUMENTS, CORROBORATES, DATES, VALIDATES, PROVIDES, FACILITATES, REPORTS

## Change Log
- 0.1 Initial matrix drafted from current `relations_vocabulary.md` canon + limited contextual verbs.
