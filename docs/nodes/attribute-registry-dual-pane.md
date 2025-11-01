# 📘 Canonical Attribute Registry (v4+ International Alignment)

## Dual-Pane Reference Table

This format presents each attribute with a left pane for **curator shorthand** and a right pane for **full academic mapping** (international standards, provenance, and schema notes).

---

### 🧩 1. Global Attributes (All Nodes)

| Curator Shorthand         | Academic Mapping / Notes                                                                 |
|--------------------------|----------------------------------------------------------------------------------------|
| `slug`                   | Unique ID; `dc:identifier`, `prov:Entity.id`                                           |
| `name`                   | Display name; `dc:title`, `skos:prefLabel`                                             |
| `alt_names[]`            | Synonyms; `skos:altLabel`                                                              |
| `definition` / `description` | Meaning; `dc:description`                                                            |
| `category`               | Thematic group; `dc:type`, `cidoc:E55_Type`                                            |
| `class_number` / `division_code` / `call_number` | Library codes; for ordering, breadcrumbs; —                                 |
| `subject_headings[]`     | Controlled vocabularies; `skos:Concept`                                                |
| `is_generic`             | Timeless hub vs. contextual; `cidoc:E28` vs. `E4`                                      |
| `status`                 | Lifecycle; Project Governance                                                          |
| `intl_status`            | Standards compliance; QA / PROV alignment                                              |
| `created_at`, `updated_at` | Timestamps; `prov:generatedAtTime`, `prov:invalidatedAtTime`                          |
| `created_by`, `modified_by`, `status_by` | Curator attribution; `prov:wasAttributedTo`                                 |
| `version`                | Schema/governance version                                                              |
| `corpus[]`               | Corpus registry link; Project corpus model                                             |
| `lang`                   | ISO 639-1 code; `dc:language`                                                          |
| `script`                 | ISO 15924 code; `cidoc:E33 Linguistic Object`                                          |

---

### 🕰 2. Contextual Attributes (Time-Bound Nodes)

| Curator Shorthand         | Academic Mapping / Notes                      |
|--------------------------|-----------------------------------------------|
| `startYear`, `endYear`   | Temporal span; `cidoc:E52_Time-Span`          |
| `chron_key`              | Ordering key; —                               |
| `context`                | Temporal scope; `skos:scopeNote`              |
| `confidence_score`       | Chronology certainty; `cidoc:P148 has certainty` |

---

### 🧠 3. Label-Specific Attributes

#### Idea
| Curator Shorthand | Academic Mapping / Notes                |
|-------------------|----------------------------------------|
| `idea_index`      | Import/publication order                |

#### Person
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `birthYear`, `deathYear` | Life span; `cidoc:E67_Birth`, `E69_Death` |
| `titles[]`               | Titles; `cidoc:E41_Appellation`         |
| `aliases[]`              | Alternate names; `skos:altLabel`        |

#### Institution
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `foundedYear`, `dissolvedYear` | Existence range; `cidoc:E63`, `E64` |
| `jurisdiction`           | Geographic/legal scope; —               |

#### Event / EventWindow
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `summary`                | Overview                                |
| `significance`           | Historical importance                   |
| `score`                  | Importance weight                       |
| `tags[]`                 | Keywords                                |

#### Place
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `kind`                   | Type (city, region, etc.)               |
| `region`                 | Macro region                            |
| `geo.lat`, `geo.lon`     | Coordinates (WGS84)                     |
| `iso`                    | ISO-3166 code                           |

#### Movement
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `startYear`, `endYear`   | Activity duration                       |
| `tags[]`                 | Topics                                  |
| `confidence_score`       | Periodization certainty                 |

#### Artifact / ArtifactText
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `material`                | Composition; `cidoc:E57_Material`       |
| `origin`                  | Provenance                              |
| `date` / `startYear`–`endYear` | Manufacture/publication; `cidoc:E12_Production` |
| `lang`, `script`          | Language/script; ISO 639-1 / 15924      |

#### Evidence
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `title`                   | Work title; `dc:title`                  |
| `author`                  | Creator; `dc:creator`                   |
| `year`                    | Publication year; `dc:date`             |
| `publisher`               | Publishing body; `dc:publisher`         |
| `doi_or_url`              | Digital ID; `dc:identifier`             |
| `lang`, `script`          | Language/script                         |
| `corpus_tier`             | Reliability; Corpus Tier Model          |
| **Link**                  | Corpus linkage; `(:Evidence)-[:BELONGS_TO]->(:Corpus)` |

#### Framework
| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `code`                    | Unique code                            |
| `name`                    | Full name                              |
| `category`                | Interpretive lens                      |
| `definition` / `notes`    | Conceptual explanation                 |

---

### 🗓 4. Chronology Stack

| Curator Shorthand | Academic Mapping / Notes                |
|-------------------|----------------------------------------|
| Epoch             | Largest division; `name`, `slug`, `startYear`, `endYear` |
| Era               | Nested under Epoch; same properties     |
| Period            | Regional bin; add `region`, `culture`, `tags[]` |
| EventWindow       | Fine-grained; add `summary`, `significance`, `score`, `tags[]` |

---

### 🔗 5. Relationship Metadata

| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| `citation_style`          | Citation format; `dc:bibliographicCitation` |
| `evidence_url`            | DOI/link; `prov:hadPrimarySource`       |
| `page_refs`               | Page/chapter references                 |
| `section`, `quote_snippet`, `source_note` | Contextual info                  |
| `source_hash`             | SHA-256 fingerprint                     |
| `_key`                    | Unique relationship fingerprint         |
| `confidence_score`        | Certainty; `prov:confidence`            |

---

### 🧭 6. Why It Matters

| Curator Shorthand         | Academic Mapping / Notes                |
|--------------------------|-----------------------------------------|
| Interoperable            | Mapped to Dublin Core, CIDOC CRM, PROV-O, SKOS |
| Auditable                | Provenance: `created_by`, `version`, `evidence_url` |
| Chronologically sortable | `chron_key` for deterministic order     |
| QA-ready                 | Validation for duplicates, missing years, alignment |
