Curator brief — English_Reformation updates

Summary

- Fixed a slug typo in relationships: `court_of_augments` -> `court_of_augmentations` (relationship id 28).
- Added minimal node stubs (status: PROPOSED) to `data/Nodes/nodes.English_Reformation.json` for:
  - `cornwall` (id 119)
  - `devon` (id 120)
  - `norfolk` (id 121)
  - `english_realm` (id 122)
  - `papal_supremacy` (id 123)
- Appended canonical relationships from `docs/clusters/English_Reformation/README.md` into `data/Relationships/relationships.json` (new ids 67–116).
- Exported `data/new_relationships_english_reformation.csv` containing the 50 newly appended relationships for review.

Why these changes

- A prior autogen and triage run flagged missing slugs. To avoid broken references in ingestion, minimal stubs were added so relationships point to existing nodes. All new content is marked `PROPOSED` for human curation.

Files changed

- `data/Relationships/relationships.json` (appended edges; fixed slug)
- `data/Relationships/relationships.English_Reformation.json` (if present)
- `data/Nodes/nodes.English_Reformation.json` (added stubs ids 119-123)
- `data/new_relationships_english_reformation.csv` (curator export)
- `data/orphan_relationship_slugs.csv` (regenerated; now empty)

Next actions for curators

1. Review `data/new_relationships_english_reformation.csv` and set `status` to `REVIEWED` or `APPROVED`, and add evidence fields where available.
2. Enrich node stubs in `data/Nodes/nodes.English_Reformation.json` with canonical dates, wikidata QIDs, and descriptions. Suggested fields to populate: `startYear`, `endYear`, `wikidata_qid`, `geo_lat`, `geo_lon`, `summary`.
3. Decide whether to remove legacy/misspelled relationships if duplicates exist; prefer retiring old entries rather than deleting history.
4. After curation, run the ingestion pipeline (or run `scripts/validate_slugs.py`) and confirm no orphans remain.

How to push (if not already pushed)

Run locally:

```bash
# create branch and commit
git checkout -b fix/court-augmentations-stubs
git add data/Relationships/relationships.json data/Nodes/nodes.English_Reformation.json data/new_relationships_english_reformation.csv data/curator_brief_english_reformation.md data/orphan_relationship_slugs.csv
git commit -m "Fix court_of_augmentations slug, add node stubs and append README canonical relationships (English_Reformation)"
# push branch
git push --set-upstream origin fix/court-augmentations-stubs
```

If push is blocked by permissions, create a patch or attach the files to a ticket for the curation team.

Contact

If you want, I can open a PR automatically (if you grant push access), or I can prepare a `git format-patch` for you.
