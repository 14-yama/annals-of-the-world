---
title: Reformation Clusters — Interaction Edges (Framework lenses)
summary: Chronological interactions between Reformation clusters mapped to interpretive frameworks and recommended verbs from the project's framework matrix.
---

This file summarizes cluster-to-cluster interactions in a single, easy-to-scan table. Each row shows the start cluster, the interpretive framework and recommended verb(s) (from `docs/guidelines/framework_matrix.md`), and the end cluster or descriptive target.

| Start node (cluster) | FRAMEWORK — VERB(s) | End node (cluster / descriptor) |
| --- | --- | --- |
| Bohemian_Moravian_Reformation | CULTURAL_DIFFUSION — TRANSMITS | German_Reformation |
| Bohemian_Moravian_Reformation | ADAPTATION — FRAMES | Radical_Reformation |
| German_Reformation | TEXTUAL_TRANSMISSION — TRANSLATES / TRANSMITS | Scandinavian_Reformations |
| German_Reformation | CONFLICT_AND_RESOLUTION — DISPUTES / CAUSES | Radical_Reformation |
| German_Reformation | DOCTRINE_DEVELOPMENT — DISPUTES / DIALOGUES | Swiss_Reformation |
| Swiss_Reformation | CULTURAL_DIFFUSION — DIFFUSES / TRANSMITS | French_Reformation |
| Swiss_Reformation | DOCTRINE_DEVELOPMENT — TRANSMITS / STANDARDIZES | Dutch_Reformation |
| Swiss_Reformation | CAUSE_AND_EFFECT — TRANSMITS / FRAMES | Scottish_Reformation |
| Radical_Reformation | CULTURAL_DIFFUSION — DIFFUSES / ORGANIZES | Dutch_Reformation |
| Radical_Reformation | CULTURAL_DIFFUSION / TEXTUAL_TRANSMISSION — DIFFUSES / TRANSMITS | Polish_Lithuanian_Reformation |
| English_Reformation | TEXTUAL_TRANSMISSION — TRANSMITS / SHARED_TEMPLATES | Scandinavian_Reformations |
| English_Reformation | CONFLICT_AND_RESOLUTION — CENSORS / RECONCILES_WITH / TRANSFORMS | Catholic_Reformation |
| Scottish_Reformation | GEOPOLITICAL_LINKAGE — INTERFACES_WITH / DISPUTES | English_Reformation |
| Scottish_Reformation | TEXTUAL_TRANSMISSION — TRANSMITS | Swiss_Reformation |
| French_Reformation | CULTURAL_DIFFUSION — DIFFUSES / ORGANIZES | Dutch_Reformation |
| French_Reformation | CONFLICT_AND_RESOLUTION — CAUSES / CENSORS / RESOLVES | Catholic_Reformation |
| Dutch_Reformation | CULTURAL_DIFFUSION — DIFFUSES / TRANSMITS | English_Reformation |
| Dutch_Reformation | TEXTUAL_TRANSMISSION — TRANSMITS | Polish_Lithuanian_Reformation |
| Polish_Lithuanian_Reformation | CONFLICT_AND_RESOLUTION — DISPUTES / CENSORS / EXILES | Catholic_Reformation |
| Scandinavian_Reformations | RITUAL_STANDARDIZATION — STANDARDIZES / ENABLES | Regional_Confessionalization |
| Catholic_Reformation | DOCTRINE_DEVELOPMENT — STANDARDIZES / PROMULGATES | Multiple_Protestant_Clusters (reactive) |

Guidance: when implementing these interactions as triples in the registry or graph, attach `FRAMED_BY` edges that name the framework lens and include evidence (inline or promoted `:Evidence` nodes) per `docs/guidelines/historian_framework.md`.

If you'd like, I can now:
- export this table to CSV for import into the registry, or
- expand each row into canonical triples (start node → verb → end node) and add example `FRAMED_BY` edges with evidence slugs.
