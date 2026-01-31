---
title: International Scholarly Conventions — Use-in-Production
status: DRAFT
summary: Practical, production-ready conventions for chronology, geography, provenance, ontology, and Neo4j modeling used by Annals of the World.
---

# How to apply international conventions (do this every time)

Here’s a crisp, “use-this-in-production” guide for applying international scholarly conventions in **Annals of the World**—followed by the canon of conventions most relevant to your graph.

## 1. Chronology (names, bins, math)

- Use globally recognized era bins (Prehistory → Ancient → Middle Ages → Early Modern → Modern → Contemporary).
- Store BCE years as **negative integers** (no year zero) so sorting and ranges work numerically.
- Keep Epoch/Era/Period/EventWindow distinct and nested via `OCCURS_DURING` with **overlap logic** (not freehand).

## 2. Geography (names, regions, kinds)

- Normalize regions (UNESCO/Oxford style), and type places with a `kind` (region, country, empire, province, city, culture-area).
- Use **generic** place nodes (e.g., “Babylon”) and attach time or specificity through contextual supporting nodes (events, institutions) instead of duplicating places by era.

## 3. Provenance & evidence (what, where, how)

- Model interpretive lenses as **Framework nodes** and link them with `FRAMED_BY` edges that carry Chicago-style citations (URL/DOI, page refs, notes); never leave interpretive links uncited.
- Reuse **Evidence nodes** for sources cited many times; use one-off inline citation properties only for truly single-use cases.

## 4. Ontology & voice (labels, verbs, direction)

- Use broad labels (`:Person`, `:Event`, `:Place`, `:Institution`, `:Idea`, `:Artifact`, `:Evidence`) with **category** as a property; avoid label explosion.
- Enforce **active-voice, verb-first** relationships (e.g., `INFLUENCES`, `OCCURS_DURING`, `FRAMED_BY`) with uniform directionality.
- For **symmetric social ties** that carry rich metadata (date, place, legal context), model them as **events** rather than P↔P edges.
	- Example: marriage as `(:Event {kind:"Marriage"})` plus `(:Person)-[:PARTICIPATES_IN {role:"spouse"}]->(:Event)`.
	- Attach time/place to the marriage event (`OCCURS_DURING`, `OCCURS_IN`, `startYear`, `endYear`) instead of encoding direction or gender.
- For **place appearance / extinction**, keep the `:Place` generic and attach an `:EventWindow` for its attested existence.
	- Example: `(:Place)-[:HAS_EXISTENCE]->(:EventWindow {startYear:-55, endYear:23})-[:OCCURS_DURING]->(:Timeframe)`.

## 5. Data hygiene (constraints, indices, QA)

- Create uniqueness constraints (e.g., slug/code), range indexes on years, and relationship fingerprinting to prevent duplicate `FRAMED_BY` edges.
- Run the provided QA queries (missing Era/Place, anachronisms, duplicate frameworks) as part of ingestion.

## 6. Neo4j modeling do’s/don’ts (house style aligned to standards)

- **MERGE** for nodes & edges, use slugs for uniqueness, and verify before linking to avoid unintended Cartesian products.
- Keep labels vs categories clean (label = entity type, category = property), and restrict relationship paths to sensible pairs (e.g., `:Artifact-[:USED_IN]->:Event` not `:Place`).

---

# The conventions you should rely on (and where they show up in your stack)

## Chronology & Geography

- **UNESCO/Oxford historical bins** for era naming and regional normalization (apply to Era/Period naming; Place.region taxonomy).
- **Numeric year encoding** for BCE/CE (BCE = negative integers; supports math & sorting).

## Provenance, Bibliography, & Citation

- **Chicago Manual of Style (17th ed.)** for citations on `FRAMED_BY` (book/article patterns, page refs, stable DOI/URL).
- **Dublin Core** for bibliographic fields on Evidence (title, creator, publisher, date, identifier/DOI)—your policy notes align to using standardized biblio fields.
- **W3C PROV-O** for provenance thinking (who/what/when/how of data creation, sources, derivations) across ingestion and link evidence—adopted at policy level.

## Cultural-heritage / Museum-grade ontology alignment

- **CIDOC CRM (incl. E39 Agent)** for treating Persons & Institutions consistently as Agents and for event-centric modeling. Use this to keep people/institutions interchangeable where appropriate.

## Graph & Modeling House Rules (standardized to support the above)

- **Active-voice relationships** (verb-first) to reduce redundancy and support clear querying.
- **Generic vs Contextual node strategy** (timeless hubs vs time-specific support) to avoid duplication across eras.
- **Constraint & indexing regime** (slug/code uniqueness; year range indices; relationship fingerprints) for integrity at scale.
- **Region & place kinds** standardized to keep cross-cultural comparability (region, country, empire, city, culture-area).

---


---

## Contributor Checklist

- [ ] Use globally recognized era bins and numeric year encoding (BCE = negative, CE = positive).
- [ ] Normalize regions and place types using UNESCO/Oxford standards.
- [ ] Model provenance with Framework nodes and Chicago-style citations; never leave interpretive links uncited.
- [ ] Use broad labels and category properties; avoid label explosion.
- [ ] Enforce active-voice, verb-first relationships with uniform directionality.
- [ ] Create uniqueness constraints, range indexes, and relationship fingerprints.
- [ ] Use MERGE for nodes/edges and slugs for uniqueness.
- [ ] Run QA queries for missing Era/Place, anachronisms, and duplicate frameworks.
- [ ] Follow Neo4j modeling house style and restrict relationship paths to sensible pairs.

---

## Related Guides

- [Schema Reference](./schema.md)
- [Classification & Corpus Registry](./classification.md)
- [Contributor Guide: Corpus](./contributor_guide_corpus.md)
- [Node Descriptions](./node_descriptions.md)

