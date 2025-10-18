---
title: Case Study — Hebrew Cluster Comparison (Moved)
status: DEPRECATED
summary: This comparison has moved under the Hebrew_Tradition cluster cases.
moved_to: ../clusters/Hebrew_Tradition/cases/rituals_vs_royal_divorce_comparison.md
---

This file has been relocated. Please use the standardized cluster case:
- ../clusters/Hebrew_Tradition/cases/rituals_vs_royal_divorce_comparison.md

See modeling conventions in:
- ../guidelines/cluster_hierarchy.md
- ../guidelines/relations_vocabulary.md

# (Legacy content below — archived)
# Scope & Focus Differences
- Royal Divorce (Henry VIII):
  - Person-centered marital edge (DIVORCES) with immediate institutional conflict and legal/doctrinal restructuring.
  - Institutions act through PROMULGATES, EXCOMMUNICATES, DECLARES; doctrine shifts via STANDARDIZES, REJECTS.
  - Texts (acts, decrees) ENABLE and document institutional change.
  - Event chain emphasizes governance/legal transformations (CAUSES → TRANSFORMS).

- Hebrew Cluster (typical):
  - Emphasis on doctrine and ritual observance with people and institutions as carriers.
  - Frequent use of OBSERVES, PRESCRIBES, DESCRIBES, PROMULGATES (law), PARTICIPATES_IN and LEADS (events), COMMENTATES_ON/INTERPRETS (texts).
  - Textual transmission and exegesis (TRANSLATES, TRANSMITS, COMMENTATES_ON) drive doctrinal diffusion; OCCURS_IN ties events to places.
  - Movements and schisms (SCHISMS_FROM, RECONCILES_WITH) reflect community dynamics rather than personal marital ties.

# Node Sets (illustrative)
- Royal Divorce:
  - P: Henry_VIII, Catherine_of_Aragon, Thomas_Cranmer, Pope_Clement_VII
  - I: Church_of_England, Papacy, English_Parliament
  - T: Act_of_Supremacy_1534, Cranmer_Annulment_Decree
  - D: Royal_Supremacy, Papal_Supremacy
  - E: Annulment_Proceedings, Break_with_Rome, Act_of_Supremacy_Passage
  - L: London, Rome

- Hebrew Cluster (example):
  - P: Prophet, Priest, Scribe
  - I: Temple_Priesthood, Synagogue_Community
  - T: Torah, Prophetic_Book, Targum
  - D: Holiness_Code, Covenant_Law
  - E: Exile, Return, Festival_Assembly
  - L: Jerusalem, Babylon

# Canonical Edges — Contrast
- Royal Divorce highlights:
  - (Henry_VIII) DIVORCES (Catherine_of_Aragon)
  - (Papacy) EXCOMMUNICATES (Henry_VIII)
  - (English_Parliament) PROMULGATES (Act_of_Supremacy_1534)
  - (Act_of_Supremacy_Passage) TRANSFORMS (Church_of_England)

- Hebrew Cluster highlights:
  - (Temple_Priesthood) PRESCRIBES (Holiness_Code)
  - (Priest) OBSERVES (Covenant_Law)
  - (Scribe) COMMENTATES_ON (Torah)
  - (Prophet) PROPHESIES_DURING (Exile)
  - (Festival_Assembly) OCCURS_IN (Jerusalem)

# Takeaways
- The divorce case is a high-salience P↔P edge that cascades into I→P and I→D/T/E edges; the Hebrew cluster is doctrine/ritual-centered with P/I as executors.
- Keep verbs standardized: avoid specialized ritual synonyms; prefer OBSERVES, PRESCRIBES, PARTICIPATES_IN/LEADS, PROMULGATES, COMMENTATES_ON.
