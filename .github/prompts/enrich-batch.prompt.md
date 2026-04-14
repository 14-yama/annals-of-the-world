---
mode: 'agent'
description: 'Enrich multiple weak entities in a batch session — open entity files and enrich each one'
tools: ['editFiles', 'readFile', 'search', 'runInTerminal']
---

# Batch Entity Enrichment Session

Enrich all entities the user specifies (or find weak ones automatically).

## Finding Weak Entities
Run in terminal to list top candidates:
```bash
python3 scripts/enrichment_queue.py --stats --limit 20
```

## For Each Entity
1. Open the entity JSON file
2. Read current summary length and quality
3. Write a rich 800–1,300 character summary (3–4 paragraphs with `\n\n`)
4. Add/update `detailsJson` with: causes (3), effects (3), relationships (5), places (3)
5. Update `subjects` (8–10 tags) and `frameworks` (3 valid frameworks)
6. Validate the JSON remains valid

## Quality Checklist
- [ ] Summary: 800–1,300 chars, 3–4 paragraphs, concrete dates/events
- [ ] Causes: 3 concise causal antecedents
- [ ] Effects: 3 concise consequent outcomes
- [ ] Relationships: 5 with all 6 required fields and valid verbs
- [ ] Places: 3 with "City, Country" format and role
- [ ] Subjects: 8–10 topic tags including country and domain
- [ ] Frameworks: 3 from the 16 approved frameworks

## Valid Relationship Verbs
CAUSES, INFLUENCES, COLLABORATES_WITH, PARTICIPATES_IN, CREATES, OCCURS_IN, FRAMES, DEFINES, TRANSFORMS, TRANSMITS, SUCCEEDS, CONTAINS, OCCURS_DURING, CANONIZES

## After Enrichment
Sync to Appwrite:
```bash
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts
```
