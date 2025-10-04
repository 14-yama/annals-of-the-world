# Curator Runbook — Annals of the World

Purpose

Compact checklist and quick actions for curators to follow when adding or reviewing nodes/edges. Use this during daily curation and pre-publish reviews.

Quick checklist

- [ ] Proposal: create node draft with `status: "PROPOSED"` and a brief `editor_note`.
- [ ] Cite: attach at least one `:Evidence` node (A-tier preferred) or inline citation on relationship.
- [ ] Frame: add `FRAMED_BY` (or active verb equivalent) to a `:Framework` node with citation metadata.
- [ ] Place: assign `Timeframe` and anchor to `Place` nodes with active spatial verbs (e.g., `HAPPENS_IN`).
- [ ] QA: run `docs/guidelines/audit_queries.md` checks (missing FRAMED_BY, temporal sanity, orphan nodes, passive verbs).
- [ ] Publish: set `status: "REVIEWED"` and add provenance (user, timestamp, change_reason).

Provenance pattern (minimal)

- `:Provenance {actor, actor_id, timestamp, action, note}` nodes.
- Link changes: `(node)-[:HAS_PROVENANCE]->(:Provenance)` or record `created_by`/`updated_by` on nodes with provenance node linked.

Quick Cypher snippets

- Record provenance for a node (example):

```
MATCH (n {slug: 'example-node'})
CREATE (p:Provenance {actor: 'alice', actor_id: 'alice@org', timestamp: timestamp(), action: 'publish', note: 'Reviewed by curatorial team'})
CREATE (n)-[:HAS_PROVENANCE]->(p)
```

- Promote a PROPOSED node to REVIEWED if audits pass:

```
MATCH (n {slug: 'example-node', status: 'PROPOSED'})
SET n.status = 'REVIEWED', n.published_at = date()
RETURN n
```

When to escalate

- Missing primary evidence, major temporal contradictions, or network fragmentation affecting >10 nodes → escalate to governance board for RFC.

Want automation

- I can scaffold `scripts/run_audit_and_publish.py` to automate checks and optionally create a provenance node when publishing.
