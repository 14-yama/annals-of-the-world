---
mode: 'agent'
description: 'Enrich a weak/stub entity to FULL quality using project enrichment standards'
tools: ['editFiles', 'readFile', 'search']
---

# Enrich Entity to FULL Quality

You are enriching a historical entity in the Annals of the World knowledge base.
Read the entity JSON file and enrich it following these exact standards.

## Summary Standards (800–1,300 characters)
- 3–4 paragraphs separated by `\n\n`
- **Paragraph 1:** Identity + dates + core significance
- **Paragraph 2:** Key achievements, events, contributions
- **Paragraph 3:** Impact, consequences, legacy
- **Paragraph 4 (optional):** Vivid closing fact or attributed quote
- Include **concrete dates, numbers, named events** — never vague generalities
- Tone: scholarly but engaging

## Structured Data Requirements
- **causes:** 3 concise sentences — causal antecedents
- **effects:** 3 concise sentences — consequent outcomes
- **relationships:** 5 items, each with: `{sourceSlug, sourceName, verb, targetSlug, targetName, context}`
  - Valid verbs: CAUSES, INFLUENCES, COLLABORATES_WITH, PARTICIPATES_IN, CREATES, OCCURS_IN, FRAMES, DEFINES, TRANSFORMS, TRANSMITS, SUCCEEDS, CONTAINS, OCCURS_DURING, CANONIZES
  - At least 1 incoming (entity as target), at least 1 OCCURS_IN for a place
- **places:** 3 items with `{name, role}` — "City, Country" format
- **subjects:** 8–10 topic tags including country/region and primary field
- **frameworks:** 3 from: CAUSE_AND_EFFECT, STRUCTURAL_ANALYSIS, WORLD_SYSTEMS, CULTURAL_TRANSMISSION, COMPARATIVE_CIVILIZATIONS, RELIGIOUS_INTERPRETATION, FEMINIST_PERSPECTIVE, MARXIST_ANALYSIS, PSYCHOLOGICAL_ANALYSIS, ENVIRONMENTAL_HISTORY, POSTCOLONIAL_ANALYSIS, SUBALTERN_STUDIES, DIPLOMATIC_HISTORY, ECONOMIC_ANALYSIS, TECHNOLOGICAL_DETERMINISM, LONGUE_DUREE

## Process
1. Read the entity file the user points you to
2. Research the entity using your knowledge
3. Update the `summary` field directly
4. Update `detailsJson` (parsed as JSON string) with causes, effects, relationships, places
5. Update `subjects` and `frameworks` arrays
6. Ensure the JSON file remains valid
