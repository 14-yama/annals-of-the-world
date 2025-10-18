# Node Descriptions Guide — Generic vs Contextual

Purpose: provide concise, copyable guidance for writing node descriptions, separated by is_generic=true (timeless hubs) vs is_generic=false (contextual instances). See the policy banner in `schema.md` (Generic vs Contextual nodes) for the canonical rules.

Links
- Canonical policy: `./schema.md#generic-vs-contextual-nodes-policy-banner`
- Verbs and pairs: `./relations_vocabulary.md` and `./interaction_matrix.md`

Scope and defaults
- Use is_generic=true primarily for Place, Idea, Corpus and select Text-family hubs; everything else defaults to is_generic=false.
- Never duplicate a generic node by era/region; attach time/place via relationships (OCCURS_IN, OCCURS_DURING, CONTAINS, ADMINISTERS, etc.).

---

## Place (`:Place`)

Generic (is_generic=true)
- Use for timeless geography (e.g., Egypt, Jerusalem, Babylon).
- Description: neutral, atemporal; no dynastic/timestamped claims.
- Don’ts: no startYear/endYear; no era-specific qualifiers in slug/name.
- Example: Egypt
  - slug: `egypt`
  - name: `Egypt`
  - is_generic: `true`
  - description: “North‑East African region centered on the Nile; used as a timeless geographic hub across periods.”

Contextual (is_generic=false)
- Prefer modeling polities as `:Institution` and occurrences as `:Event` attached to the generic Place.
- Allowed only when a specific site/feature must be distinct (e.g., “Second_Temple_Platform” as Place of kind=site), but still avoid dates in slug.
- Description: scope and nature of the site; time via relationships.

## Idea / Doctrine (`:Idea`)

Generic (is_generic=true)
- Use for abstract ideas/doctrines (Monotheism, Covenant, Meritocracy).
- Description: definition, scope, key variants; avoid periodized claims.

Contextual (is_generic=false)
- Rare; if time‑bound formulation dominates, consider `:Movement` (e.g., “Early_Christian_Orthodoxy”) or attach time via events and frameworks.
- Description: define the specific formulation and its scope; cite edges for context.

## Institution (`:Institution`)

Generic (is_generic=true)
- Rare; only for type families (e.g., “Synagogue” as an abstract institution family). Description: abstract definition.

Contextual (is_generic=false)
- Default. Concrete bodies (Sanhedrin, Church_of_England, Papacy, Geonic_Academies).
- Description: concise remit/competence; seat(s) optional; time via properties or edges; avoid narrative history (leave to Evidence/edges).

## Text / Artifact (`:Text`, `:Artifact`)

Generic (is_generic=true)
- Use for corpora or families (Torah_Corpus, Masoretic_Tradition as text family hub).
- Description: scope and inclusion criteria; editions go under contextual.

Contextual (is_generic=false)
- Specific works/editions (Guide_for_the_Perplexed, Book_of_Common_Prayer_1552).
- Description: brief work statement (genre, authorship tradition, purpose). Time belongs in properties/edges; keep neutral tone.

## Movement (`:Movement`)

Generic (is_generic=true)
- Generally avoid; movements are typically time/region bounded. Only use if modeling an abstract family of movements.

Contextual (is_generic=false)
- Default (Rabbinic_Judaism, Zionist_Movement, Via_Media). Describe scope, typical claims, social carrier; attach places/times via edges.

## Event / EventWindow (`:Event`, `:EventWindow`)

Generic (is_generic=true)
- Not applicable; events are inherently temporal/contextual.

Contextual (is_generic=false)
- Default. Keep description to what/why/how in one or two sentences; time/place via properties and OCCURS_IN/OCCURS_DURING.

## Person (`:Person`)

Generic (is_generic=true)
- Not applicable.

Contextual (is_generic=false)
- Default. One‑line identification (role, domain). Biographical detail belongs in Evidence; dates as properties, not embedded in `name`.

## Framework (`:Framework`)

Generic (is_generic=true)
- Default. Interpretive lenses (Cause & Effect, Continuity & Change). Description: neutral definition and when to apply.

Contextual (is_generic=false)
- Rare; only if you must scope a framework variant (avoid when possible).

## Evidence (`:Evidence`)

Generic (is_generic=true)
- Not applicable.

Contextual (is_generic=false)
- Default. Description: bibliographic/citation synopsis; keep facts in edge properties; include stable identifiers.

## Corpus (`:Corpus`)

Generic (is_generic=true)
- Default. Canonical groupings (BIBLICAL_CORPUS, RABBINIC_CORPUS). Description: inclusion criteria.

Contextual (is_generic=false)
- Rare; avoid unless sub‑corpus is required with stable boundaries.

## Timeframe (`:Timeframe`)

Generic (is_generic=true)
- Not applicable.

Contextual (is_generic=false)
- Default. Description: concise label; semantics live in hierarchy and properties (`kind: epoch/era/period`).

---

## Writing templates (copy/paste)

Generic template (is_generic=true)
```
slug: <short-id, no dates>
name: <canonical name>
is_generic: true
description: <atemporal definition; no year-like tokens; neutral scope>
notes: <optional synonyms/variant labels>
```

Contextual template (is_generic=false)
```
slug: <short-id, scoped if needed>
name: <canonical contextual name>
is_generic: false
description: <what it is, scope/salience; avoid embedding dates here>
startYear/endYear: <optional ints>
place_refs: <optional place slugs if helpful>
```

---

## QA checklist
- If is_generic=true:
  - No startYear/endYear set; no dates/eras in description.
  - Slug has no time/region qualifiers.
- If is_generic=false:
  - Time/space modeled via edges (OCCURS_IN/OCCURS_DURING) and properties, not baked into name.
  - Description is concise and neutral; rich narrative goes to Evidence.
- For Places: polities/states should be Institutions linked to the generic Place.

---

## Quick examples

- Generic Place — Egypt
  - slug: `egypt`; name: `Egypt`; is_generic: `true`
  - description: “North‑East African region centered on the Nile; used as a timeless geographic hub across periods.”

- Contextual Institution — Ptolemaic Kingdom
  - slug: `ptolemaic_kingdom`; is_generic: `false`; startYear: `-305`; endYear: `-30`
  - description: “Hellenistic monarchy administering Egypt and adjacent territories.”
  - edges: `(:Institution)-[:ADMINISTERS]->(:Place {slug:'egypt'})`

- Contextual Event — Second Temple destruction (70 CE)
  - slug: `temple_destruction_70ce`; is_generic: `false`
  - description: “Roman destruction of the Second Temple in Jerusalem.”
  - edges: `(:Event)-[:OCCURS_IN]->(:Place {slug:'jerusalem'})`
