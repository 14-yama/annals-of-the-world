
# 📖 Annals of the World — Historical Knowledge Graph

This repository contains the **Annals of the World** project: a Neo4j-based historical knowledge graph designed to model people, ideas, places, events, institutions, texts, and evidence **across time and space** using international scholarly conventions.

The project provides a **source of truth** for historical data, ensuring relationships are active-voice, evidence-backed, and version-controlled.

---

## Table of Contents

- [Project summary](docs/summary.md)
- [Schema & guidelines index](docs/guidelines/README.md)
- [Relations vocabulary](docs/guidelines/relations_vocabulary.md)
- [Node interaction matrix](docs/guidelines/node_interaction_matrix.md#quick-pair-matrix-overview)
- [Hebrew cluster scaffold](docs/guidelines/hebrew_cluster.md)
- [Framework matrix](docs/guidelines/framework_matrix.md)
- [CRM/PROV crosswalk](docs/guidelines/crosswalk_crm_prov.md)
- [Features by version](docs/guidelines/features_by_version.md)
- [Audit queries](docs/guidelines/audit_queries.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- Governance: [Policy](docs/governance/GOVERNANCE.md) • [Audit Log](docs/governance/audit_log.md)
- [Getting started / scripts](scripts/)


## 🎯 Purpose

* Build a **scalable, queryable knowledge graph** for world history.
* Capture **core ideas, people, institutions, places, events, texts, movements, evidence** in a structured form.
* Apply **historian frameworks** (Cause & Effect, Continuity & Change, Cultural Diffusion, etc.) to interpret history consistently.
* Ensure **auditability** with evidence citations (DOI, URL, Chicago 17 style).
* Enforce **strict verb governance**: use only verbs from the source of truth and record any governance change in the Audit Log.
* Support **cross-civilizational comparisons** (e.g., Hebrew Bible cluster vs. Gunpowder cluster).


## 🏗️ Schema Overview

We follow the **v4 optimized schema**【v4.pdf】:

### Core Labels

* `:Idea` — Abstract concepts (Monotheism, Covenant, Meritocracy).
* `:Person` — Historical figures (Abraham, Maimonides, Spinoza).
* `:Institution` — Organized bodies (Second Temple Priesthood, Zionist Congress).
* `:Place` — Geographic nodes (Jerusalem, Babylon, Alexandria).
* `:Event` — Historical occurrences (Exodus, Babylonian Exile, Holocaust).
* `:Movement` — Social/religious/cultural trends (Rabbinic Judaism, Kabbalah, Zionism).
* `:Artifact` / `:Text` — Material culture or texts (Dead Sea Scrolls, Masoretic Text, Zohar).
* `:Evidence` — Primary sources & archaeological finds (Ketef Hinnom amulets, Tel Dan Stele).
* `:Corpus` — Canonical text groupings (BIBLICAL_CORPUS, RABBINIC_CORPUS).
* `:Timeframe` — Parent nodes for eras (910 Prehistoric, 920 Classical, 930 Medieval, 940 Early Modern, 950 Modern, 960 Contemporary).
* `:Framework` — Historian interpretive lenses (Cause & Effect, Continuity & Change, Cultural Diffusion, etc.).

### Key Relationship Types

* `(:Event)-[:OCCURRED_IN]->(:Place)`
* `(:Person)-[:INFLUENCES]->(:Idea)`
* `(:Institution)-[:CODIFIES]->(:Text)`
* `(:EventWindow)-[:FRAMED_BY {citation,…}]->(:Framework)`
* `(:Evidence)-[:BELONGS_TO]->(:Corpus)`
* `(:Movement)-[:ARISES_FROM]->(:Event)`
* `(:Place)-[:CONTAINS]->(:Institution)`

All relationship names are **active voice** (per Active Relationship Standard).

---

## 🗂️ Workflow


### Curator Workflow: File-First, Database-Second (Resilient)

All data and workflow stages are managed in versioned seed files stored in the repository. JSON is the preferred canonical seed format for seed files (nodes, relationships, and exports) because it preserves native arrays, nested maps, typed values, and is easier for humans to read and review. CSV/TSV remains supported for quick spreadsheet-style edits and bulk exports, but contributors should prefer JSON for any canonical or nested data.

Seed files live under `/data/` (for example `data/nodes.json` and `data/relationships.json`). The database is treated as a cache and can be reseeded at any time from these files.

**Stages:**

1. **Propose** — Curator drafts node(s) and relationships in seed files with `status:"PROPOSED"`.
2. **Cite** — Add evidence fields (manuscripts, scholarly works, archaeological data) in seed files.
3. **Frame** — Add framework relationships (e.g., FRAMED_BY edges with citation metadata) in seed files.
4. **Place** — Assign timeframes and places in seed files.
5. **Review** — Update status in seed files after QA for redundancy, active voice, and evidence compliance.
6. **Publish** — Change status to `"REVIEWED"` in seed files; nodes are locked for queries.
7. **Version** — Mark deprecated and new versions in seed files; all changes are tracked in Git.

**Best Practice:**
- Prefer `data/nodes.json` as the canonical nodes seed. The file may contain a top-level `_meta` object and a `nodes` array (see `data/nodes.json` for an example and inline guidance). This lets us include human-readable comments and schema hints while keeping valid JSON.
- All changes are made to seed files and committed via pull requests.
- Ingest scripts load seed files into Neo4j; contributors never edit the database directly.
- If the database is lost or compromised, reseed by running ingest scripts on the latest seed files.
- Regularly export the database to files for backup and disaster recovery.

**Example Directory Structure:**

```
/data/
  nodes.json        # canonical nodes seed (preferred)
  relationships.json  # canonical relationships seed (preferred)
/scripts/
  ingest_nodes.py
  ingest_relationships.py
  export_graph.py
/docs/
  workflow.md
  contributor_guide.md
```

**Reseeding Steps (quick):**
1. Clone repo.
2. Ensure `.env.local` points to your Neo4j instance (NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD).
3. Run the nodes importer (defaults to `data/nodes.json`):

```bash
python scripts/ingest_nodes.py         # reads data/nodes.json (preferred)
python scripts/ingest_nodes.py data/nodes.csv  # or explicitly import CSV
```

4. Run `scripts/ingest_relationships.py` to apply relationships (if present).
5. Database is restored to latest committed state.

---

## 📊 Governance Rules

* **Active Voice Only:** No passive relationships (`CONTROLLED_BY` → ❌, `CONTROLS` → ✅).
* **Generic vs. Contextual Nodes:** Places and ideas are generic hubs; contextual supporting nodes (e.g., *Babylonian Exile 586 BCE*) provide historical anchoring【Guidelines for Generic Nodes.pdf】.
* **Citation Integrity:** Each FRAMED_BY must have:

  * `citation_style: "Chicago 17"`
  * `evidence_url` (stable DOI/URL)
  * `page_refs`
  * `source_note`
* **Chronology:** BCE as negative integers, CE as positive, ensuring numeric sortability【v2.pdf】.
* **Versioning:** Nodes can be superseded but never silently deleted.

---

## 📂 Example Cluster: Hebrew Bible

**Timeframe → Nodes**

* **920 Classical:** Exodus, Babylonian Exile, Prophets, Second Temple Priesthood, Dead Sea Scrolls.
* **930 Medieval:** Maimonides, Rashi, Zohar, Babylonian Talmud, Kabbalah.
* **940 Early Modern:** Spinoza, Printing houses, Enlightenment critiques.
* **950 Modern:** Herzl, Geiger, Hirsch, Zionism, Biblical Criticism.
* **960 Contemporary:** Holocaust, Founding of Israel, Dead Sea Scrolls publication, Heschel, Wiesel.

---

## ✅ QA & Best Practices

* **No label explosion** → use `:Person {category:…}` instead of separate labels.
* **Evidence-first culture** → no relationship published without at least one citation.
* **Sharding strategy** → Eras (Prehistoric, Classical, Medieval, etc.) serve as partitions for scalability【v2.pdf】.
* **Audit queries** (examples included in docs) detect missing FRAMED_BY, passive voice, orphan nodes.

---

## 📅 Status

* Gunpowder cluster: Seeded, in review.
* Hebrew Bible cluster: Expanded scaffold drafted (≈200 nodes, spanning Creation → today).
* Other clusters (Islamic Philosophy, Meritocracy, etc.): Upcoming.

