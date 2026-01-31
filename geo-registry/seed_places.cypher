// Seed Places + PlaceName variants from a parameter payload.
//
// How to run (Neo4j Browser):
//   1) Paste the JSON payload into the Browser params panel as `payload`
//      (or paste the payload directly as `:param payload => {...}`)
//   2) Run each block below.
//
// Expected parameters:
//   $payload.places   :: [{slug,name,kind,iso,wikidata_id,pleiades_id,status}]
//   $payload.contains :: [{parent,child}]
//   $payload.variants :: [{place_slug,slug,name,lang,script,is_endonym,note,startYear,endYear,is_primary,change_reason}]

// ---------------------------------------------------------------------------
// Constraints / indexes
// ---------------------------------------------------------------------------
CREATE CONSTRAINT place_slug_unique IF NOT EXISTS
FOR (p:Place) REQUIRE p.slug IS UNIQUE;

CREATE CONSTRAINT place_name_slug_unique IF NOT EXISTS
FOR (n:PlaceName) REQUIRE n.slug IS UNIQUE;

CREATE INDEX place_name_name_index IF NOT EXISTS
FOR (n:PlaceName) ON (n.name);

CREATE INDEX place_name_lang_index IF NOT EXISTS
FOR (n:PlaceName) ON (n.lang);

// ---------------------------------------------------------------------------
// Upsert Place nodes
// ---------------------------------------------------------------------------
UNWIND $payload.places AS row
MERGE (p:Place {slug: row.slug})
ON CREATE SET
  p.created_at = datetime(),
  p.category = 'Place'
SET
  p.name = coalesce(row.name, p.name),
  p.kind = coalesce(row.kind, p.kind),
  p.iso = coalesce(row.iso, p.iso),
  p.wikidata_id = coalesce(row.wikidata_id, p.wikidata_id),
  p.pleiades_id = coalesce(row.pleiades_id, p.pleiades_id),
  p.status = coalesce(row.status, p.status),
  p.updated_at = datetime();

// ---------------------------------------------------------------------------
// Parent -> child containment edges
// ---------------------------------------------------------------------------
UNWIND $payload.contains AS rel
MATCH (a:Place {slug: rel.parent})
MATCH (b:Place {slug: rel.child})
MERGE (a)-[:CONTAINS]->(b);

// ---------------------------------------------------------------------------
// PlaceName nodes + authoritative PREVIOUSLY_KNOWN_AS edges
// ---------------------------------------------------------------------------
UNWIND $payload.variants AS row
MATCH (p:Place {slug: row.place_slug})
MERGE (n:PlaceName {slug: row.slug})
SET
  n.name = row.name,
  n.lang = coalesce(row.lang, 'und'),
  n.script = coalesce(row.script, 'Latn'),
  n.is_endonym = CASE WHEN row.is_endonym = true THEN true ELSE null END,
  n.note = row.note
MERGE (p)-[r:PREVIOUSLY_KNOWN_AS]->(n)
SET
  r.startYear = row.startYear,
  r.endYear = row.endYear,
  r.is_primary = CASE WHEN row.is_primary = true THEN true ELSE null END,
  r.change_reason = row.change_reason

// Maintain Place.alt_names[] for search (deduped)
SET p.alt_names =
  CASE
    WHEN row.name IS NULL THEN coalesce(p.alt_names, [])
    ELSE reduce(out = coalesce(p.alt_names, []), x IN [row.name] |
      CASE WHEN x IN out THEN out ELSE out + x END)
  END

// Derived edges for *current* variants
FOREACH (_ IN CASE
  WHEN (row.endYear IS NULL OR row.endYear >= date().year) AND row.is_endonym = true
  THEN [1] ELSE [] END |
  MERGE (p)-[:ENDONYM]->(n)
)
FOREACH (_ IN CASE
  WHEN (row.endYear IS NULL OR row.endYear >= date().year)
   AND coalesce(row.is_primary,false) = false
   AND coalesce(row.is_endonym,false) = false
  THEN [1] ELSE [] END |
  MERGE (p)-[:EXONYM]->(n)
);
