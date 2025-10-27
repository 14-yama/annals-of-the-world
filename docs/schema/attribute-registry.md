# 📘 Canonical Attribute Registry (v4+ International Alignment)

### 🧩 1. Global Attributes (apply to all nodes)

| **Attribute**                                  | **Purpose / Description**                                                                       | **International Alignment**                      | **Example**                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------- |
| `slug`                                         | Permanent unique ID (used in URLs, cross-refs)                                                  | `dc:identifier`, `prov:Entity.id`                | "monotheism"                |
| `name`                                         | Main display name / preferred label                                                             | `dc:title`, `skos:prefLabel`                     | "Monotheism"                |
| `alt_names[]`                                  | Synonyms or alternate spellings                                                                 | `skos:altLabel`                                  | ["Monolatry", "Henotheism"] |
| `definition` / `description`                   | Concise statement of meaning                                                                    | `dc:description`                                 | "Belief in a single deity." |
| `category`                                     | Thematic grouping (Political, Religious, Economic, etc.)                                        | `dc:type`, `cidoc:E55_Type`                      | "Religious Concept"         |
| `class_number`, `division_code`, `call_number` | Librarian classification (used for breadcrumbs and ordering)                                    | —                                                | 1.140.03                      |
| `subject_headings[]`                           | Controlled vocabularies (LCSH, SKOS concepts)                                                   | `skos:Concept`                                   | ["Theology—Monotheism"]     |
| `is_generic`                                   | `true` = timeless hub; `false` = contextual                                                     | `cidoc:E28 Conceptual Object` vs. `E4 Period`    | true                         |
| `status`                                       | Node lifecycle (`PROPOSED`, `CITED`, `FRAMED`, `PLACED`, `REVIEWED`, `PUBLISHED`, `DEPRECATED`) | Project Governance                               | "FRAMED"                    |
| `intl_status`                                  | Standards compliance (`ALIGNED`, `PARTIAL`, `NEEDS_REVIEW`, `NONCONFORMANT`)                    | QA / PROV alignment                              | "ALIGNED"                   |
| `created_at`, `updated_at`                     | Creation / modification timestamps                                                              | `prov:generatedAtTime`, `prov:invalidatedAtTime` | "2025-08-24T15:20Z"         |
| `created_by`, `modified_by`, `status_by`       | Curator attribution                                                                             | `prov:wasAttributedTo`                           | "curator_42"                |
| `version`                                      | Schema/governance version number                                                                | —                                                | 4                            |
| `corpus[]`                                     | Link to corpus registry (textual/cultural source family)                                        | Project corpus model                             | ["BIBLICAL_CORPUS"]         |
| `lang`                                         | ISO 639-1 language code                                                                         | `dc:language`                                    | "en"                        |
| `script`                                       | ISO 15924 script code                                                                           | `cidoc:E33 Linguistic Object`                    | "Latn"                      |

---

### 🕰 2. Contextual Attributes (for time-bound nodes only)

| **Attribute**          | **Purpose / Description**                     | **International Alignment** | **Example**           |
| ---------------------- | --------------------------------------------- | --------------------------- | --------------------- |
| `startYear`, `endYear` | Temporal span (BCE negative; no year 0)       | `cidoc:E52_Time-Span`       | -586, -539            |
| `chron_key`            | Deterministic ordering key (YYYY or YYYYMMDD) | —                           | -0586                 |
| `context`              | Descriptive temporal scope                    | `skos:scopeNote`            | "Second Temple Era"  |
| `confidence_score`     | Certainty level of chronology (0–1)           | `cidoc:P148 has certainty`  | 0.9                   |

---

### 🧠 3. Label-Specific Attributes

#### Idea
| Attribute    | Description                       | Example |
| ------------ | --------------------------------- | ------- |
| `idea_index` | Batch import or publication order | 17      |

#### Person
| Attribute                | Description              | International Alignment        | Example                         |
| ------------------------ | ------------------------ | ------------------------------ | ------------------------------- |
| `birthYear`, `deathYear` | Life span                | `cidoc:E67_Birth`, `E69_Death` | -428, -348                      |
| `titles[]`               | Official or noble titles | `cidoc:E41_Appellation`        | ["King"]                       |
| `aliases[]`              | Alternate names          | `skos:altLabel`                | ["Amenhotep IV", "Akhenaten"] |

#### Institution
| Attribute                      | Description              | Alignment          | Example            |
| ------------------------------ | ------------------------ | ------------------ | ------------------ |
| `foundedYear`, `dissolvedYear` | Existence range          | `cidoc:E63`, `E64` | 590, 1054          |
| `jurisdiction`                 | Geographic / legal scope | —                  | "Western Europe"  |

#### Event / EventWindow
| Attribute      | Description                    | Example                            |
| -------------- | ------------------------------ | ---------------------------------- |
| `summary`      | One-sentence overview          | "Siege ending Byzantine Empire"   |
| `significance` | Why it matters historically    | "Introduced gunpowder artillery"  |
| `score`        | Quantitative importance weight | 0.85                               |
| `tags[]`       | Keywords for categorization    | ["Ottoman", "Gunpowder"]          |

#### Place
| Attribute            | Description                                     | Example          |
| -------------------- | ----------------------------------------------- | ---------------- |
| `kind`               | Type (region, empire, city, culture-area, etc.) | "city"          |
| `region`             | UNESCO / Oxford macro region                    | "West Asia"     |
| `geo.lat`, `geo.lon` | Coordinates (decimal, WGS84)                    | 32.54, 44.42     |
| `iso`                | Modern ISO-3166 code                            | "IQ"            |

#### Movement
| Attribute              | Description                     | Example                  |
| ---------------------- | ------------------------------- | ------------------------ |
| `startYear`, `endYear` | Duration of activity            | 1848–1917                |
| `tags[]`               | Associated topics               | ["Labor", "Socialism"]  |
| `confidence_score`     | Uncertainty about periodization | 0.8                      |

#### Artifact / ArtifactText
| Attribute                      | Description                     | Alignment              | Example                |
| ------------------------------ | ------------------------------- | ---------------------- | ---------------------- |
| `material`                     | Physical composition            | `cidoc:E57_Material`   | "Bronze"              |
| `origin`                       | Provenance location             | —                      | "Mesopotamia"         |
| `date` / `startYear`–`endYear` | Manufacture/publication date    | `cidoc:E12_Production` | -1750                  |
| `lang`, `script`               | Language/script (textual items) | ISO 639-1 / 15924      | "akk", "Cuneiform"    |

#### Evidence
| Attribute        | Description                            | Alignment                 | Example                                      |
| ---------------- | -------------------------------------- | ------------------------- | -------------------------------------------- |
| `title`          | Work title                             | `dc:title`                | "Guns for the Sultan"                        |
| `author`         | Creator/author                         | `dc:creator`              | "Gábor Ágoston"                              |
| `year`           | Publication year                       | `dc:date`                 | 2005                                         |
| `publisher`      | Publishing body                        | `dc:publisher`            | "Cambridge University Press"                 |
| `doi_or_url`     | Digital identifier                     | `dc:identifier`           | "https://doi.org/10.1017/CBO9780511497433"   |
| `lang`, `script` | Language/script                        | —                         | "en", "Latn"                                 |
| `corpus_tier`    | Scholarly reliability (A–F scale)      | Project Corpus Tier Model | "B"                                          |
| **Link**         | `(:Evidence)-[:BELONGS_TO]->(:Corpus)` | Cultural corpus linkage   | "BIBLICAL_CORPUS"                            |

#### Framework
| Attribute              | Description               | Example                                   |
| ---------------------- | ------------------------- | ----------------------------------------- |
| `code`                 | Unique code identifier    | "CAUSE_EFFECT"                            |
| `name`                 | Full framework name       | "Cause & Effect"                          |
| `category`             | Type of interpretive lens | "Causation"                               |
| `definition` / `notes` | Conceptual explanation    | "Direct causal linkage between events."   |

---

### 🗓 4. Chronology Stack (Epoch → Era → Period → EventWindow)

| Label           | Core Properties                                                                      | Notes                                    |
| --------------- | ------------------------------------------------------------------------------------ | ---------------------------------------- |
| **Epoch**       | `name`, `slug`, `startYear`, `endYear`                                               | Largest time division (e.g., Bronze Age) |
| **Era**         | same as above                                                                        | Nested under Epoch (e.g., Classical Era) |
| **Period**      | `name`, `slug`, `startYear`, `endYear`, `region`, `culture`, `tags[]`                | Mid-level regional bin                   |
| **EventWindow** | `name`, `slug`, `startYear`, `endYear`, `summary`, `significance`, `score`, `tags[]` | Fine-grained event layer                 |

---

### 🔗 5. Relationship Metadata (Edge-level)

| **Property**                              | **Purpose / Description**                     | **Convention / Alignment** |
| ----------------------------------------- | --------------------------------------------- | -------------------------- |
| `citation_style`                          | Citation format (default: *Chicago 17*)       | `dc:bibliographicCitation` |
| `evidence_url`                            | DOI or stable link                            | `prov:hadPrimarySource`    |
| `page_refs`                               | Page / chapter references                     | —                          |
| `section`, `quote_snippet`, `source_note` | Optional contextual info                      | —                          |
| `source_hash`                             | SHA-256 fingerprint (deduplication)           | —                          |
| `_key`                                    | Unique relationship fingerprint (constraint)  | —                          |
| `confidence_score`                        | Certainty level of this specific relationship | `prov:confidence`          |

---

### 🧭 6. Why It Matters

* **Interoperable:** fully mapped to **Dublin Core**, **CIDOC CRM**, **W3C PROV-O**, and **SKOS**.
* **Auditable:** every node and relationship carries provenance (`created_by`, `version`, `evidence_url`).
* **Chronologically sortable:** `chron_key` supports deterministic left-to-right visualization.
* **QA-ready:** attributes support validation queries for duplicates, missing years, non-aligned data.

---

# 📘 Canonical Attribute Registry — Proposed Additions (v5 Readiness)

> These extensions build on the **v4+ International Alignment Registry** to improve provenance, interoperability, QA, and analytics.
> They are fully compatible with **CIDOC CRM**, **PROV-O**, **Dublin Core**, and **SKOS** standards.

---

### 🧾 1. Provenance & Audit Extensions

| **Attribute**       | **Tag** | **Purpose / Description**                                                 | **International Alignment**   | **Example**                                 |
| ------------------- | ------- | ------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------- |
| `source_origin`     | ✅       | Describes origin of the record (`Curator Seed`, `Automated Import`, etc.) | `prov:wasDerivedFrom`         | `"Curator Seed"`                            |
| `source_id`         | ✅       | External identifier (e.g., Wikidata QID, VIAF, DOI)                       | `owl:sameAs`, `schema:sameAs` | `"Q42887"`                                  |
| `reviewed_by[]`     | ✅       | Curator(s) who reviewed this node                                         | `prov:wasInfluencedBy`        | `["curator_12", "curator_47"]`              |
| `review_date`       | ✅       | ISO timestamp of peer review approval                                     | `prov:qualifiedAttribution`   | `"2025-09-10T18:00Z"`                       |
| `deprecated_reason` | ✅       | Explanation for deprecation or merge                                      | `prov:invalidatedAtTime`      | `"Merged with monotheism (canonical form)"` |

---

### 🌐 2. Semantic Interoperability Extensions

| **Attribute**      | **Tag** | **Purpose / Description**                                         | **Alignment**                | **Example**                                |
| ------------------ | ------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------------------ |
| `external_links[]` | ✅       | URIs to external databases (Wikidata, VIAF, Getty AAT, LOC, etc.) | `owl:sameAs`, `schema:about` | `["https://www.wikidata.org/wiki/Q42887"]` |
| `ontology_class`   | ✅       | Mapped ontology class (e.g., `E39 Actor`, `E4 Period`)            | `cidoc:E*`                   | `"E39 Actor"`                              |
| `thesaurus_ref`    | 🧪      | Reference ID to AAT or ULAN term                                  | Getty Vocabularies           | `"AAT_300054216"`                          |
| `wikidata_qid`     | ✅       | Direct link to Wikidata entity                                    | Wikidata                     | `"Q42887"`                                 |
| `schema_context`   | 🧪      | JSON-LD context reference for RDF export                          | `@context`                   | `"https://schema.org"`                     |

---

### 📊 3. Graph Analytics & QA Metrics

| **Attribute**      | **Tag** | **Purpose / Description**                             | **Alignment**    | **Example**                 |
| ------------------ | ------- | ----------------------------------------------------- | ---------------- | --------------------------- |
| `importance_score` | ✅       | Curator-assigned significance weight (0–1)            | project-specific | `0.85`                      |
| `citation_count`   | ✅       | Number of supporting Evidence nodes                   | bibliometric     | `12`                        |
| `connectedness`    | 🧪      | Precomputed degree centrality                         | graph metric     | `0.67`                      |
| `review_status`    | ✅       | Simplified QA flag (`PASSED`, `FLAGGED`, `IN_REVIEW`) | internal         | `"PASSED"`                  |
| `qa_notes`         | 🧪      | Internal notes for validation or audit                | —                | `"Needs date verification"` |

---

### 🕯 4. Cultural & Linguistic Context

| **Attribute**        | **Tag** | **Purpose / Description**                         | **Alignment**                  | **Example**                     |
| -------------------- | ------- | ------------------------------------------------- | ------------------------------ | ------------------------------- |
| `cultural_context`   | ✅       | Civilizational or cultural frame                  | `cidoc:E55_Type`               | `"Hellenistic"`                 |
| `translation_status` | 🧪      | Indicates if text is machine- or human-translated | `dc:language` + project policy | `"Verified"`                    |
| `translators[]`      | 🧪      | Names or IDs of translators                       | `prov:wasAttributedTo`         | `["translator_8"]`              |
| `orthography_note`   | 🧪      | Notes on script conventions or spelling           | `cidoc:E33_Linguistic_Object`  | `"Classical Latin orthography"` |

---

### ⏳ 5. Temporal & Spatial Refinements

| **Attribute**        | **Tag** | **Purpose / Description**                              | **Alignment**               | **Example**                      |
| -------------------- | ------- | ------------------------------------------------------ | --------------------------- | -------------------------------- |
| `midYear`            | ✅       | Computed midpoint (average of startYear and endYear)   | derived field               | `-560`                           |
| `duration`           | ✅       | Duration (years)                                       | derived field               | `47`                             |
| `periodic_overlap[]` | 🧪      | Array of overlapping Period/Era slugs                  | QA optimization             | `["classical-era", "axial-age"]` |
| `spatial_extent`     | 🧪      | GeoJSON polygon or bounding box                        | `geo:SpatialThing`          | `{ "type": "Polygon", ... }`     |
| `geo_precision`      | ✅       | Spatial certainty (`exact`, `approximate`, `inferred`) | `prov:confidence` (spatial) | `"approximate"`                  |

---

### 📚 6. Evidence & Citation Enhancements

| **Attribute** | **Tag** | **Purpose / Description**                | **Alignment**   | **Example**         |
| ------------- | ------- | ---------------------------------------- | --------------- | ------------------- |
| `isbn`        | ✅       | Book identifier                          | `dc:identifier` | `"978-0521834205"`  |
| `issn`        | ✅       | Journal identifier                       | `dc:identifier` | `"1471-5457"`       |
| `edition`     | 🧪      | Edition or version of publication        | `prism:edition` | `"2nd ed."`         |
| `pages_total` | 🧪      | Total page count (useful for monographs) | —               | `420`               |
| `license`     | ✅       | Copyright or usage rights                | `dc:rights`     | `"CC-BY-NC-SA 4.0"` |

---

### 🧮 7. Governance / Workflow Metadata

| **Attribute**        | **Tag** | **Purpose / Description**                                   | **Alignment**      | **Example**     |
| -------------------- | ------- | ----------------------------------------------------------- | ------------------ | --------------- |
| `workflow_stage`     | ✅       | Current stage in curation workflow (`PROPOSED → PUBLISHED`) | project governance | `"REVIEWED"`    |
| `governance_version` | ✅       | Version of governance policy applied at creation            | internal           | `5`             |
| `validation_hash`    | 🧪      | SHA-256 hash of full node data for integrity checks         | `prov:checksum`    | `"f84c9...eab"` |

---

### ✨ 8. Smart / Derived Fields

| **Attribute**      | **Tag** | **Purpose / Description**                            | **Computation Rule**       |
| ------------------ | ------- | ---------------------------------------------------- | -------------------------- |
| `display_label`    | ✅       | Concatenation of `name + (context)` for UI rendering | Auto-generated             |
| `era_ref`          | ✅       | Resolved Era slug based on overlapping years         | Computed                   |
| `citation_density` | 🧪      | Number of `[:FRAMED_BY]` edges per EventWindow       | Computed                   |
| `has_geo`          | ✅       | Boolean flag for geographic visualization            | Derived from `geo.lat`     |
| `has_text`         | ✅       | Boolean flag for textual Evidence nodes              | Derived from `lang/script` |

---

### 🧭 9. Recommended Implementation Order

| **Priority** | **Category**                   | **Rationale**                                       |
| ------------ | ------------------------------ | --------------------------------------------------- |
| 1️⃣          | Provenance & Audit             | Strengthens data lineage and accountability.        |
| 2️⃣          | Semantic Interoperability      | Enables external dataset linking (Wikidata, AAT).   |
| 3️⃣          | QA & Analytics                 | Adds measurable metrics for curator dashboards.     |
| 4️⃣          | Temporal / Spatial Refinements | Supports timeline and map visualization.            |
| 5️⃣          | Evidence & Governance          | Improves bibliographic rigor and curator workflows. |

---

### 🧠 Summary

✅ **Recommended Fields** → immediately usable and compatible with v4 schema.
🧪 **Experimental Fields** → optional; implement once automation or RDF export is introduced.

---
