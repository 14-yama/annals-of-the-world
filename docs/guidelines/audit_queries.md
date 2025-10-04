# Audit Queries — Annals of the World

This file collects runnable Cypher checks curators can run against a Neo4j dataset to validate schema hygiene, citation coverage, chronology, and classification.

Notes
- These queries assume your DB uses the labels and properties described in the docs (e.g., `:EventWindow`, `:Evidence`, `:Corpus`, `call_number`, `slug`, `startYear`, `endYear`, `citation_style`, `evidence_url`, `page_refs`, `source_note`).
- Adjust property names or labels to match your implementation.

1) Missing FRAMED_BY edges (events/frameworks)

```
MATCH (e:EventWindow)
WHERE NOT (e)-[:FRAMED_BY]->()
RETURN count(e) AS events_missing_framed_by LIMIT 1;
```

2) FRAMED_BY edges missing required citation fields

```
MATCH (e:EventWindow)-[r:FRAMED_BY]->(f:Framework)
WHERE r.citation_style IS NULL OR r.evidence_url IS NULL OR r.page_refs IS NULL
RETURN e.slug AS event, id(r) AS rel_id, keys(r) AS missing_fields LIMIT 50;
```

3) Temporal sanity (startYear ≤ endYear)

```
MATCH (e:EventWindow)
WHERE e.startYear IS NOT NULL AND e.endYear IS NOT NULL AND e.startYear > e.endYear
RETURN e.slug AS event, e.startYear, e.endYear LIMIT 50;
```

4) Orphan nodes (no relationships)

```
MATCH (n)
WHERE size((n)--()) = 0
RETURN labels(n) AS labels, count(n) AS orphan_count
ORDER BY orphan_count DESC LIMIT 50;
```

5) Duplicate slugs (should be unique)

```
MATCH (n)
WHERE exists(n.slug)
WITH n.slug AS slug, collect(n) AS nodes, size(collect(n)) AS cnt
WHERE cnt > 1
RETURN slug, cnt, [x IN nodes | id(x)][0..5] AS sample_node_ids LIMIT 50;
```

6) Passive-voice relationship names (detect `_BY`, `BY_`, `ED_BY` patterns)

```
CALL db.relationshipTypes() YIELD relationshipType
WITH relationshipType
WHERE relationshipType CONTAINS '_BY' OR relationshipType ENDS WITH 'ED_BY' OR relationshipType STARTS WITH 'WAS_' OR relationshipType =~ '.*_BY$'
RETURN relationshipType LIMIT 200;
```

7) Duplicate relationships fingerprint (same type + same endpoints + same key props)

```
MATCH (a)-[r]->(b)
WITH a,b,type(r) AS t, r, size(collect(r)) AS cnt
WHERE cnt > 1
RETURN labels(a) AS from_label, t AS rel_type, labels(b) AS to_label, cnt LIMIT 50;
```

8) Call-number format checks (simple regex for `digit.digit.slug`)

```
MATCH (n)
WHERE exists(n.call_number) AND NOT n.call_number =~ '^\d+\.\d+\.[a-z0-9\-]+'
RETURN labels(n) AS labels, n.call_number AS bad_call_number LIMIT 50;
```

9) Division vs label mismatch (example: call numbers starting with 4.* should be Places)

```
MATCH (n)
WHERE exists(n.call_number)
WITH n, split(n.call_number, '.') AS parts
WHERE parts[0] = '4' AND NOT n:Place
RETURN n.slug AS node, n.call_number LIMIT 50;
```

10) Evidence coverage summary (how many edges have at least one evidence/citation)

```
MATCH ()-[r]->()
WITH type(r) AS relType, count(r) AS total, sum(CASE WHEN r.evidence_url IS NOT NULL OR r.citation_style IS NOT NULL THEN 1 ELSE 0 END) AS with_evidence
RETURN relType, total, with_evidence, (with_evidence*1.0/total) AS coverage
ORDER BY coverage ASC LIMIT 200;
```

Usage notes
- Run these queries in Neo4j Browser or via cypher-shell. Redirect output to CSV for ingest into dashboards.
- If your relationship stores evidence as a linked `:Evidence` node rather than inline properties, adapt the queries to check `(a)-[r]->(b) WHERE (r)-[:CITED_BY]->(:Evidence)` or similar.

Want more
- I can add an executable script `scripts/run_audits.py` that runs these queries and writes a report to `reports/audit-YYYYMMDD.json`.
