# Curator Workflow Template: English Reformation

This document provides a complete template for curating a cluster through all workflow stages. The English Reformation cluster was the first to complete all stages and serves as the reference implementation.

## Summary

| Metric | Count |
|--------|-------|
| Total Nodes | 182 |
| Nodes with REVIEWED status | 159 |
| Nodes with PROPOSED status | 23 (missing descriptions) |
| Total Relationships | 423 |
| Relationships with evidence | 423 (100%) |
| Timeframe edges (OCCURS_DURING) | 183 |
| Framework edges (FRAMED_BY) | 423 |
| Place edges (OCCURS_IN) | 14 |

---

## Workflow Steps

### Step 1: PROPOSE — Draft nodes and relationships

Ensure all nodes have:
- `slug`: Unique identifier (Pascal_Case)
- `label`: One of `Person`, `Event`, `Text`, `Institution`, `Movement`, `Place`, `Idea`
- `status`: Set to `PROPOSED`
- `description`: Human-readable description
- `cluster`: Cluster name (e.g., `English_Reformation`)

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step propose --dry-run
```

### Step 2: CITE — Add evidence references

Each relationship should reference scholarly evidence:
- `evidence_slug`: Reference to evidence file in `data/Evidence/`
- `citation_style`: `"Chicago 17"`
- `page_refs`: Page references or `"passim"`

**Evidence files available:** See `data/Evidence/` for the complete registry.

**Example assignment strategy:**
```python
# Map node patterns to evidence sources
EVIDENCE_MAP = {
    "Henry_VIII": "evidence_Scarisbrick_1968_Henry_VIII",
    "Thomas_Cranmer": "evidence_MacCulloch_1996_Thomas_Cranmer",
    "Mary_I": "evidence_Duffy_2009_Fires_of_Faith",
    "default": "evidence_Haigh_1993_English_Reformations",
}
```

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step cite --dry-run
```

### Step 3: FRAME — Add FRAMED_BY edges to Frameworks

Link relationships to interpretive frameworks:

| Relationship Type | Framework |
|------------------|-----------|
| CAUSES, ENABLES, TRIGGERS | cause_and_effect |
| INFLUENCES, TRANSMITS, DIFFUSES | cultural_diffusion |
| PROMULGATES, CODIFIES, REFORMS | continuity_and_change |
| OPPOSES, PERSECUTES, EXECUTES | conflict_and_cooperation |
| ENDORSES, SUPPORTS, ALLIES_WITH | conflict_and_cooperation |
| WRITES, AUTHORS, TRANSLATES | intellectual_history |
| LEADS, ORGANIZES, ADMINISTERS | political_analysis |
| TRADES_WITH, PRODUCES, FINANCES, DISTRIBUTES | economic_systems |
| GOVERNS, LEGISLATES, DELEGATES | political_systems |
| COMPARES, SYNCRETIZES, CONVERTS | comparative_religion |
| COLONIZES, ADMINISTERS, RESISTS, DECOLONIZES | empire_and_colonialism |
| EXPLOITS, CONSERVES, DEPLETES, ADAPTS_TO | environmental_history |
| INVENTS, INNOVATES, DISRUPTS, MECHANIZES | innovation_and_technology |

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step frame --dry-run
```

### Step 4: PLACE — Assign timeframes and places

#### Timeframe Edges (OCCURS_DURING)

All English Reformation nodes are assigned to division **940 (Early Modern, 1500-1800)**.

**Command:**
```bash
python scripts/generate_timeframe_edges.py English_Reformation --dry-run
python scripts/generate_timeframe_edges.py English_Reformation --ingest
```

#### Place Edges (OCCURS_IN)

Map events to their geographic locations:

| Event | Place |
|-------|-------|
| English_Reformation | England |
| Execution_of_Thomas_More_1535 | London |
| Pilgrimage_of_Grace_1536 | Northern_England |
| Oxford_Martyrs_1555_1556 | Oxford |
| Convocation_of_1563 | Canterbury |

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step place --dry-run
```

### Step 5: REVIEW — QA checks

Run quality assurance to detect:
- Nodes without status
- Nodes without descriptions
- Relationships without evidence
- Orphan slugs (references to non-existent nodes)

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step review
```

### Step 6: PUBLISH — Update to REVIEWED status

Promote nodes and relationships from `PROPOSED` to `REVIEWED`:
- Nodes: Must have `description` and `label`
- Relationships: Must have `evidence_slug` or `evidence_url`

**Command:**
```bash
python scripts/complete_curator_workflow.py English_Reformation --step publish
```

---

## Complete Workflow

Run all steps in sequence:

```bash
# Dry run first
python scripts/complete_curator_workflow.py English_Reformation --dry-run

# Apply changes
python scripts/complete_curator_workflow.py English_Reformation

# Ingest to Neo4j
python scripts/ingest_nodes.py data/Nodes/nodes.English_Reformation.json
python scripts/ingest_edge_arrays.py English_Reformation
```

---

## Neo4j Verification Queries

### Count nodes by label
```cypher
MATCH (n) WHERE n.cluster = "English_Reformation"
RETURN labels(n)[0] AS label, count(n) AS count
ORDER BY count DESC
```

### Verify timeframe edges
```cypher
MATCH (n)-[:OCCURS_DURING]->(t:Timeframe)
WHERE n.cluster = "English_Reformation"
RETURN t.division, count(n) AS nodes
```

### Verify framework edges
```cypher
MATCH (n)-[:FRAMED_BY]->(f:Framework)
WHERE n.cluster = "English_Reformation"  
RETURN f.name AS framework, count(*) AS edges
ORDER BY edges DESC
```

### Find events in a timeframe
```cypher
MATCH (e:Event)-[:OCCURS_DURING]->(t:Timeframe {division: 940})
WHERE e.cluster = "English_Reformation"
RETURN e.slug, e.description
```

### Find events at a place
```cypher
MATCH (e:Event)-[:OCCURS_IN]->(p:Place {slug: "London"})
WHERE e.cluster = "English_Reformation"
RETURN e.slug, e.description
```

---

## Files Modified

- `data/Nodes/nodes.English_Reformation.json` — Node definitions
- `data/Relationships/relationships.English_Reformation.json` — Relationships + edge arrays

## Metadata

After completing the workflow, files contain:
```json
{
  "_meta": {
    "curator_workflow_completed_at": "2025-01-24T02:42:34.231067+00:00",
    "curator_workflow_script": "scripts/complete_curator_workflow.py"
  }
}
```

---

## Applying to Other Clusters

To apply this workflow to another cluster:

1. **Create the script evidence map** for your cluster's sources
2. **Create the framework map** for relationship types  
3. **Create the place assignments** for events
4. **Run the workflow**:

```bash
# Example for Continental_Reformations
python scripts/complete_curator_workflow.py Continental_Reformations --dry-run
python scripts/complete_curator_workflow.py Continental_Reformations
python scripts/ingest_nodes.py data/Nodes/nodes.Continental_Reformations.json
python scripts/ingest_edge_arrays.py Continental_Reformations
```

The `complete_curator_workflow.py` script can be extended to support additional clusters by adding entries to:
- `EVIDENCE_MAP` — Cluster-specific evidence sources
- `FRAMEWORK_MAPPINGS` — Relationship type to framework mapping
- `PLACE_ASSIGNMENTS` — Event to place mapping
