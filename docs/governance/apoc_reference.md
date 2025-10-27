# APOC Reference Guide for Project

This document lists all APOC procedures and functions planned for use in the project, with descriptions and example usages tailored to our graph schema and workflows.

---

## 1. apoc.trigger.add
**Description:** Adds a trigger to automatically execute Cypher code on data changes (create, update, delete). Used for audit logging of node and relationship changes.
**Example:**
```cypher
CALL apoc.trigger.add('audit_log',
  "UNWIND $createdNodes AS n CREATE (a:AuditLog {timestamp: timestamp(), action: 'CREATE', nodeId: id(n), labels: labels(n), properties: properties(n)})
   UNWIND $deletedNodes AS n CREATE (a:AuditLog {timestamp: timestamp(), action: 'DELETE', nodeId: id(n), labels: labels(n)})
   UNWIND $assignedNodeProperties AS change CREATE (a:AuditLog {timestamp: timestamp(), action: 'UPDATE', nodeId: id(change.node), key: change.key, old: change.old, new: change.new})",
  {phase:'after'})
```

---

## 2. apoc.periodic.commit
**Description:** Runs a Cypher statement in batches for large data updates or imports, reducing transaction size and memory usage. Useful for seeding Person, Event, or Evidence nodes from CSV.
**Example:**
```cypher
CALL apoc.periodic.commit(
  "LOAD CSV WITH HEADERS FROM 'file:///persons.csv' AS row
   MERGE (p:Person {slug: row.slug})
   SET p.name = row.name, p.birth = row.birth RETURN count(*)",
  {})
```

---

## 3. apoc.create.node / apoc.create.relationship
**Description:** Programmatically creates nodes or relationships with dynamic labels/types and properties. Useful for adding Evidence nodes or linking Events to Persons.
**Example:**
```cypher
CALL apoc.create.node(['Evidence'], {type:'primary', source:'archive', tier:'A'}) YIELD node RETURN node
CALL apoc.create.relationship(person, 'PARTICIPATED_IN', {role:'leader'}, event) YIELD rel RETURN rel
```

---

## 4. apoc.merge.node / apoc.merge.relationship
**Description:** Merges (creates or matches) nodes or relationships with given labels/types and properties, similar to Cypher's MERGE but more flexible. Useful for canonicalizing corpus nodes or relationships.
**Example:**
```cypher
CALL apoc.merge.node(['Corpus'], {slug:'medieval_manuscripts'}, {discipline:'history'}) YIELD node RETURN node
CALL apoc.merge.relationship(person, 'CITED_IN', {}, {}, evidence) YIELD rel RETURN rel
```

---

## 5. apoc.date.format
**Description:** Formats timestamps or dates for display or storage. Useful for event timelines or audit logs.
**Example:**
```cypher
RETURN apoc.date.format(timestamp(), 'ms', 'yyyy-MM-dd HH:mm:ss') AS formatted
```

---

## 6. apoc.export.csv / apoc.export.json / apoc.export.graphml
**Description:** Exports graph data to CSV, JSON, or GraphML formats for backup, sharing, or analysis. Useful for exporting node registries or event networks.
**Example:**
```cypher
CALL apoc.export.csv.query("MATCH (e:Event)-[:HAS_EVIDENCE]->(ev:Evidence) RETURN e, ev", "/tmp/events_evidence.csv", {})
CALL apoc.export.json.query("MATCH (p:Person)-[:PARTICIPATED_IN]->(ev:Event) RETURN p, ev", "/tmp/person_events.json", {})
```

---

## 7. apoc.load.csv / apoc.load.json
**Description:** Loads external CSV or JSON data for import into the graph. Useful for onboarding new corpus or evidence nodes.
**Example:**
```cypher
CALL apoc.load.csv('file:///corpus_registry.csv') YIELD map RETURN map
CALL apoc.load.json('file:///evidence_sources.json') YIELD value RETURN value
```

---

## 8. apoc.util.validate
**Description:** Validates conditions in Cypher and throws errors if validation fails (useful for enforcing business rules, e.g., required fields for Evidence nodes).
**Example:**
```cypher
CALL apoc.util.validate(NOT exists(e.type), 'Evidence type required', [0])
```

---

## 9. apoc.map.fromPairs
**Description:** Creates a map from a list of key-value pairs, useful for dynamic property assignment (e.g., batch node creation).
**Example:**
```cypher
RETURN apoc.map.fromPairs([['slug','event_001'],['name','Council of Trent']]) AS props
```

---

## 10. apoc.coll.flatten
**Description:** Flattens nested lists into a single list, useful for aggregating results (e.g., collecting all related node slugs).
**Example:**
```cypher
RETURN apoc.coll.flatten([['Henry_VIII','Anne_Boleyn'],['Thomas_More']]) AS all_persons
```

---

## 11. apoc.cypher.run / apoc.cypher.runFile
**Description:** Runs dynamic Cypher statements or loads Cypher from a file for advanced scripting. Useful for batch updates or custom reporting.
**Example:**
```cypher
CALL apoc.cypher.run("MATCH (n:Evidence) WHERE n.tier = 'A' RETURN n", {}) YIELD value RETURN value
CALL apoc.cypher.runFile('file:///batch_update.cypher') YIELD row RETURN row
```

---

## 12. apoc.meta.schema
**Description:** Returns the schema of the graph (labels, relationship types, properties) for documentation or analysis. Useful for maintaining contributor guides and node registries.
**Example:**
```cypher
CALL apoc.meta.schema() YIELD value RETURN value
```

---

*For more details, see the [APOC documentation](https://neo4j.com/labs/apoc/).*