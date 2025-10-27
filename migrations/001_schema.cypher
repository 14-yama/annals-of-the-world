// === Canonical Schema Migration (v4 baseline + v5-ready fields) ===
// Run on Neo4j 5.x. Idempotent (`IF NOT EXISTS`).

// ---------- Uniqueness by slug/code ----------
CREATE CONSTRAINT epoch_slug_unique        IF NOT EXISTS FOR (n:Epoch)        REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT era_slug_unique          IF NOT EXISTS FOR (n:Era)          REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT period_slug_unique       IF NOT EXISTS FOR (n:Period)       REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT ew_slug_unique           IF NOT EXISTS FOR (n:EventWindow)  REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT place_slug_unique        IF NOT EXISTS FOR (n:Place)        REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT idea_slug_unique         IF NOT EXISTS FOR (n:Idea)         REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT person_slug_unique       IF NOT EXISTS FOR (n:Person)       REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT institution_slug_unique  IF NOT EXISTS FOR (n:Institution)  REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT movement_slug_unique     IF NOT EXISTS FOR (n:Movement)     REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT artifact_slug_unique     IF NOT EXISTS FOR (n:Artifact)     REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT evidence_slug_unique     IF NOT EXISTS FOR (n:Evidence)     REQUIRE n.slug IS UNIQUE;
CREATE CONSTRAINT framework_code_unique    IF NOT EXISTS FOR (n:Framework)    REQUIRE n.code IS UNIQUE;

// ---------- Required core props ----------
CREATE CONSTRAINT node_slug_required   IF NOT EXISTS FOR (n) REQUIRE n.slug IS NOT NULL;
CREATE CONSTRAINT node_name_required   IF NOT EXISTS FOR (n) REQUIRE n.name IS NOT NULL;

// Time-bounded nodes
CREATE CONSTRAINT ew_dates_required     IF NOT EXISTS FOR (n:EventWindow) REQUIRE (n.startYear, n.endYear) IS NOT NULL;
CREATE CONSTRAINT period_dates_required IF NOT EXISTS FOR (n:Period)      REQUIRE (n.startYear, n.endYear) IS NOT NULL;
CREATE CONSTRAINT era_dates_required    IF NOT EXISTS FOR (n:Era)         REQUIRE (n.startYear, n.endYear) IS NOT NULL;
CREATE CONSTRAINT epoch_dates_required  IF NOT EXISTS FOR (n:Epoch)       REQUIRE (n.startYear, n.endYear) IS NOT NULL;

// Evidence minimums
CREATE CONSTRAINT evidence_title_required IF NOT EXISTS FOR (n:Evidence) REQUIRE n.title IS NOT NULL;

// ---------- Relationship fingerprint (dedupe) ----------
CREATE CONSTRAINT framed_by_key_unique IF NOT EXISTS
FOR ()-[r:FRAMED_BY]-() REQUIRE r._key IS UNIQUE;

// ---------- Helpful indexes ----------
CREATE INDEX name_text_idx        IF NOT EXISTS FOR (n) ON (n.name);
CREATE INDEX start_end_epoch_idx  IF NOT EXISTS FOR (n:Epoch)      ON (n.startYear, n.endYear);
CREATE INDEX start_end_era_idx    IF NOT EXISTS FOR (n:Era)        ON (n.startYear, n.endYear);
CREATE INDEX start_end_period_idx IF NOT EXISTS FOR (n:Period)     ON (n.startYear, n.endYear);
CREATE INDEX start_end_ew_idx     IF NOT EXISTS FOR (n:EventWindow)ON (n.startYear, n.endYear);
CREATE INDEX place_region_idx     IF NOT EXISTS FOR (n:Place)      ON (n.region, n.slug);
CREATE INDEX status_idx           IF NOT EXISTS FOR (n) ON (n.status);
CREATE INDEX intl_status_idx      IF NOT EXISTS FOR (n) ON (n.intl_status);

// v5-ready optional lookups
CREATE INDEX wikidata_qid_idx     IF NOT EXISTS FOR (n) ON (n.wikidata_qid);
CREATE INDEX external_links_idx   IF NOT EXISTS FOR (n) ON (n.external_links);
CREATE INDEX ontology_class_idx   IF NOT EXISTS FOR (n) ON (n.ontology_class);

// ---------- APOC Triggers (guards, validators, derived) ----------
// Requires apoc core enabled.

// Active-voice enforcement: disallow relationship types ending in "_BY"
CALL apoc.trigger.remove('enforceActiveVoice') YIELD name AS _drop1;
CALL apoc.trigger.add(
  'enforceActiveVoice',
  '
  UNWIND $createdRelationships AS r
  WITH r WHERE type(r) ENDS WITH "_BY" AND type(r) <> "FRAMED_BY"
  CALL apoc.util.validate(true, "Passive relationship names are disallowed. Use active voice.", [type(r)]) YIELD value
  RETURN value
  ',
  {phase:"after"}
);

// Temporal sanity: startYear <= endYear
CALL apoc.trigger.remove('temporalSanity') YIELD name AS _drop2;
CALL apoc.trigger.add(
  'temporalSanity',
  '
  UNWIND ($createdNodes + $assignedNodeProperties) AS n
  WITH n WHERE any(l IN labels(n) WHERE l IN ["Epoch","Era","Period","EventWindow"])
    AND n.startYear IS NOT NULL AND n.endYear IS NOT NULL
  CALL apoc.util.validate(n.startYear > n.endYear,
    "Invalid time-span: startYear must be <= endYear for " + apoc.text.join(labels(n), ","),
    [coalesce(n.slug, n.name)]) YIELD value
  RETURN value
  ',
  {phase:"after"}
);

// No year zero
CALL apoc.trigger.remove('noYearZero') YIELD name AS _drop3;
CALL apoc.trigger.add(
  'noYearZero',
  '
  UNWIND ($createdNodes + $assignedNodeProperties) AS n
  WITH n WHERE n.startYear IS NOT NULL OR n.endYear IS NOT NULL
  CALL apoc.util.validate( (coalesce(n.startYear,1) = 0 OR coalesce(n.endYear,1) = 0),
    "Year zero is not allowed (use -1 for 1 BCE, 1 for 1 CE).",
    [coalesce(n.slug, n.name)]) YIELD value
  RETURN value
  ',
  {phase:"after"}
);

// Evidence required on FRAMED_BY
CALL apoc.trigger.remove('framedByEvidenceRequired') YIELD name AS _drop4;
CALL apoc.trigger.add(
  'framedByEvidenceRequired',
  '
  UNWIND $createdRelationships AS r
  WITH r WHERE type(r) = "FRAMED_BY"
  CALL apoc.util.validate(r.evidence_url IS NULL,
    "FRAMED_BY requires evidence_url.",
    [id(r)]) YIELD value
  RETURN value
  ',
  {phase:"after"}
);

// Derived fields: chron_key, midYear, duration, display_label
CALL apoc.trigger.remove('computeDerived') YIELD name AS _drop5;
CALL apoc.trigger.add(
  'computeDerived',
  '
  UNWIND ($createdNodes + $assignedNodeProperties) AS n
  WITH n
  FOREACH (_ IN CASE WHEN exists(n.startYear) AND exists(n.endYear) THEN [1] ELSE [] END |
    SET n.chron_key = toInteger(n.startYear),
        n.midYear   = toInteger(round((n.startYear + n.endYear)/2.0)),
        n.duration  = toInteger(abs(n.endYear - n.startYear) + 1)
  )
  SET n.display_label = CASE WHEN n.context IS NOT NULL THEN n.name + " (" + n.context + ")" ELSE n.name END
  ',
  {phase:"after"}
);

// ---------- Helpful QA views ----------
/*
MATCH (w:EventWindow)
WHERE NOT (w)-[:OCCURS_DURING]->(:Era) OR NOT (w)-[:OCCURRED_IN]->(:Place)
RETURN w.slug, w.name;

MATCH ()-[r]->() WHERE type(r) ENDS WITH "_BY" AND type(r) <> "FRAMED_BY"
RETURN type(r), count(*);
*/
