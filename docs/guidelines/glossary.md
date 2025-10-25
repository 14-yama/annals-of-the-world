# Annals of the World — Project Glossary

This glossary defines key terms, node types, relationships, conventions, and workflow concepts used throughout the Annals of the World knowledge graph project. Use this as a reference for contributors, curators, and developers.

---

## Node Types
- **Node**: A graph entity representing a person, place, event, idea, institution, artifact, evidence, corpus, or framework.
- **:Person**: Individual historical or cultural figure.
- **:Place**: Geographic location (city, region, site).
- **:Event / :EventWindow**: Historical occurrence or temporally bounded window.
- **:Idea**: Abstract concept, doctrine, or intellectual tradition.
- **:Institution**: Organization, school, or governing body.
- **:Artifact**: Physical object or material culture.
- **:Evidence**: Primary source, archaeological find, or citation.
- **:Corpus**: Canonical grouping of texts, traditions, or cultural artifacts.
- **:Framework**: Interpretive lens or analytical schema.

## Relationships & Properties
- **Relationship (Edge)**: Connection between nodes, defined by a verb (e.g., INFLUENCES, BELONGS_TO, OCCURS_DURING).
- **Active-Voice Relationship**: Edge verb with subject → object directionality (e.g., Person INFLUENCES Idea).
- **Slug**: Canonical short identifier for a node (unique per label).
- **Tier**: Discipline level for corpus/evidence (A–F: Primary, Peer-Reviewed, Scholarly, Institutional, Archaeological, Oral/Quantitative).
- **Provenance**: Metadata for source, creator, and modification history.
- **Classification**: Library-style taxonomy for organizing nodes (class.division.id).
- **Call Number**: Numeric code for node classification.
- **Subject Heading**: Topical label for classification.
- **Registry**: Canonical list of recognized corpora, clusters, or entities.

## Project Structure & Workflow
- **Cluster**: Thematic or civilizational grouping of nodes (e.g., Reformation, Hebrew, Early Christianity).
- **Zone**: Civilizational area (Ancient Near East, East Asia, Americas, etc.).
- **Discipline**: Academic or evidentiary field (history, law, science, etc.).
- **Cypher**: Neo4j query language for graph operations.
- **Contributor**: Project participant who seeds, curates, or expands nodes and relationships.
- **Curator**: Senior contributor responsible for governance, audits, and normalization.
- **Historian**: Contributor focused on historical accuracy and context.
- **Workflow**: Step-by-step process for node creation, validation, linking, and publication.
- **Convention**: Standardized rule or practice (international, scholarly, project-specific).
- **CRM (CIDOC CRM)**: International standard for cultural heritage data modeling.
- **UNESCO**: United Nations Educational, Scientific and Cultural Organization; used for region/style normalization.
- **Matrix**: Table of allowed node-type pairs and relationship verbs.
- **Interaction Matrix**: Overview of valid node-type interactions and example triples.
- **Crosswalk**: Mapping between project schema and external standards (CIDOC, UNESCO).
- **Framework Matrix**: Table of interpretive lenses and their application.
- **Hierarchy**: Organizational structure of clusters, corpora, and disciplines.
- **Runbook**: Stepwise guide for curators and contributors.
- **Audit**: Review of node, relationship, or workflow integrity.

## Evidence & Corpus Tiers
- **Primary**: Direct texts or sources (Bible, Vedas, Avesta).
- **Peer-Reviewed**: Modern academic studies.
- **Scholarly**: Books from academic publishers.
- **Institutional**: Reports from organizations (UNESCO, IMF).
- **Archaeological**: Excavation records, inscriptions.
- **Oral / Quantitative**: Documented oral histories, data series.

## Miscellaneous
- **Overview**: High-level summary of a cluster, corpus, or workflow.
- **Canonical**: Official, authoritative, or standardized within the project.
- **Generic Node**: Atemporal, non-contextual hub (e.g., Place, Corpus).
- **Contextual Node**: Instance with time/place specificity (e.g., Event, Person in a given era).

---

For further details, see:
- [Schema Reference](./schema.md)
- [Classification & Corpus Registry](./classification.md)
- [Relations Vocabulary](./relations_vocabulary.md)
- [Node Descriptions](./node_descriptions.md)
- [Workflow Guide](./workflow.md)
- [International Conventions](./international_conventions.md)
