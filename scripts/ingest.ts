/**
 * Ingest helper for Annals of the World (v4 + v5-ready)
 * - Computes derived fields & fingerprints client-side
 * - Enforces active-voice edges (no *_BY except FRAMED_BY for framework link)
 * - Uses named exports (project preference)
 */

import neo4j, { Driver, Session } from 'neo4j-driver';
import crypto from 'node:crypto';

type BaseNode = {
  slug: string;
  name: string;
  category?: string;
  alt_names?: string[];
  subject_headings?: string[];
  is_generic?: boolean;
  status?: string;       // PROPOSED, FRAMED, etc.
  intl_status?: string;  // ALIGNED, PARTIAL, ...
  lang?: string;
  script?: string;
  version?: number;      // default 4
  created_by?: string;
  modified_by?: string;
};

type TimeBound = {
  startYear: number;
  endYear: number;
  context?: string;
  confidence_score?: number; // 0..1
};

type PlaceNode = BaseNode & {
  kind?: 'region'|'country'|'empire'|'province'|'city'|'culture-area'|'tribe'|'civilization';
  region?: string;
  iso?: string;
  geo?: { lat?: number; lon?: number };
  wikidata_qid?: string;
  external_links?: string[];
  ontology_class?: string;
};

type EventWindowNode = BaseNode & TimeBound & {
  summary?: string;
  significance?: string;
  score?: number;
  tags?: string[];
};

type EvidenceNode = BaseNode & {
  title: string;
  author?: string;
  year?: number;
  publisher?: string;
  doi_or_url?: string;
  corpus_tier?: string; // A..F
  isbn?: string;
  issn?: string;
  license?: string;
  corpus_codes?: string[];
};

type FrameworkLink = {
  ew_slug: string;
  fw_code: string;
  citation_style?: string; // default Chicago 17
  evidence_url: string;
  page_refs?: string;
  source_note?: string;
  confidence_score?: number;
};

export function sha256(s: string): string {
  return crypto.createHash('sha256').update(s).digest('hex');
}

export function framedByKey(ewSlug: string, fwCode: string, evidenceUrl = '', pageRefs = ''): string {
  return sha256(`${ewSlug}|${fwCode}|${evidenceUrl}|${pageRefs}`);
}

export function ensureActiveVoice(relType: string) {
  if (relType.endsWith('_BY') && relType !== 'FRAMED_BY') {
    throw new Error(`Passive relationship "${relType}" is disallowed. Use active voice.`);
  }
}

export function buildDriver(uri: string, user: string, password: string): Driver {
  return neo4j.driver(uri, neo4j.auth.basic(user, password));
}

async function run<T>(session: Session, query: string, params: T) {
  return session.executeWrite(tx => tx.run(query, params));
}

// ---------- Upserts ----------

export async function upsertPlace(session: Session, p: PlaceNode) {
  const q = `
  MERGE (x:Place {slug:$slug})
  ON CREATE SET
    x.name=$name,
    x.is_generic=coalesce($is_generic,true),
    x.kind=$kind, x.region=$region, x.iso=$iso,
    x.category=coalesce($category,'Place'),
    x.alt_names=coalesce($alt_names,[]),
    x.subject_headings=coalesce($subject_headings,[]),
    x.lang=$lang, x.script=$script,
    x.wikidata_qid=$wikidata_qid,
    x.external_links=coalesce($external_links,[]),
    x.ontology_class=$ontology_class,
    x.created_at=datetime(), x.created_by=$actor,
    x.status=coalesce($status,'PROPOSED'),
    x.intl_status=coalesce($intl_status,'ALIGNED'),
    x.version=coalesce($version,4)
  ON MATCH SET
    x.modified_by=$actor, x.updated_at=datetime()
  `;
  await run(session, q, { ...p, actor: p.modified_by ?? p.created_by ?? 'system' });
}

export async function upsertEventWindow(session: Session, w: EventWindowNode) {
  if (w.startYear === 0 || w.endYear === 0) throw new Error('Year zero is not allowed.');

  const q = `
  MERGE (n:EventWindow {slug:$slug})
  ON CREATE SET
    n.name=$name, n.is_generic=false,
    n.startYear=$startYear, n.endYear=$endYear,
    n.summary=$summary, n.significance=$significance, n.score=$score, n.tags=coalesce($tags,[]),
    n.context=$context,
    n.confidence_score=coalesce($confidence_score,1.0),
    n.category=coalesce($category,'EventWindow'),
    n.lang=$lang, n.script=$script,
    n.created_at=datetime(), n.created_by=$actor,
    n.status=coalesce($status,'FRAMED'),
    n.intl_status=coalesce($intl_status,'ALIGNED'),
    n.version=coalesce($version,4)
  ON MATCH SET
    n.modified_by=$actor, n.updated_at=datetime()
  `;
  await run(session, q, { ...w, actor: w.modified_by ?? w.created_by ?? 'system' });
}

export async function linkOccurredIn(session: Session, ew_slug: string, place_slug: string) {
  const q = `
  MATCH (w:EventWindow {slug:$ew}), (p:Place {slug:$pl})
  MERGE (w)-[:OCCURRED_IN]->(p)
  `;
  await run(session, q, { ew: ew_slug, pl: place_slug });
}

export async function upsertEvidence(session: Session, e: EvidenceNode) {
  const q = `
  MERGE (x:Evidence {slug:$slug})
  ON CREATE SET
    x.name=$name, x.title=$title, x.author=$author, x.year=$year, x.publisher=$publisher,
    x.doi_or_url=$doi_or_url, x.lang=$lang, x.script=$script,
    x.corpus_tier=$corpus_tier, x.isbn=$isbn, x.issn=$issn, x.license=$license,
    x.is_generic=true, x.created_at=datetime(), x.created_by=$actor, x.version=coalesce($version,4)
  ON MATCH SET
    x.updated_at=datetime(), x.modified_by=$actor;
  `;
  await run(session, q, { ...e, actor: e.modified_by ?? e.created_by ?? 'system' });

  if (e.corpus_codes?.length) {
    const linkQ = `
      UNWIND $codes AS code
      MERGE (c:Corpus {code:code})
      WITH c
      MATCH (x:Evidence {slug:$slug})
      MERGE (x)-[:BELONGS_TO]->(c)
    `;
    await run(session, linkQ, { codes: e.corpus_codes, slug: e.slug });
  }
}

export async function linkFramedBy(session: Session, link: FrameworkLink) {
  const { ew_slug, fw_code, evidence_url, page_refs = '', source_note = '', citation_style = 'Chicago 17' } = link;
  const key = framedByKey(ew_slug, fw_code, evidence_url, page_refs);

  const q = `
  MATCH (w:EventWindow {slug:$ew}), (f:Framework {code:$fw})
  MERGE (w)-[r:FRAMED_BY]->(f)
  ON CREATE SET
    r._key=$key,
    r.citation_style=$citation_style,
    r.evidence_url=$evidence_url,
    r.page_refs=$page_refs,
    r.source_note=$source_note,
    r.source_hash:$source_hash,
    r.confidence_score=coalesce($confidence_score,1.0),
    r.created_at=datetime()
  ON MATCH SET
    r.updated_at=datetime()
  `;
  await run(session, q, {
    ew: ew_slug,
    fw: fw_code,
    key,
    citation_style,
    evidence_url,
    page_refs,
    source_note,
    source_hash: sha256((evidence_url ?? '') + page_refs),
    confidence_score: link.confidence_score ?? 1.0,
  });
}

// ---------- Convenience bootstrap ----------

export async function attachEraByOverlap(session: Session) {
  const q = `
  MATCH (w:EventWindow), (e:Era)
  WHERE w.startYear <= e.endYear AND w.endYear >= e.startYear
  MERGE (w)-[:OCCURS_DURING]->(e)
  `;
  await run(session, q, {});
}

// ---------- Example usage ----------
// (Put this in a separate runner file if you prefer)

export async function demo() {
  const uri = process.env.NEO4J_URI ?? 'bolt://localhost:7687';
  const user = process.env.NEO4J_USER ?? 'neo4j';
  const pass = process.env.NEO4J_PASSWORD ?? 'password';

  const driver = buildDriver(uri, user, pass);
  const session = driver.session({ defaultAccessMode: neo4j.session.WRITE });

  try {
    await upsertPlace(session, {
      slug: 'babylon',
      name: 'Babylon',
      is_generic: true,
      kind: 'city',
      region: 'West Asia',
      category: 'Place',
      created_by: 'curator_demo',
    });

    await upsertEventWindow(session, {
      slug: 'babylonian-exile-586-539-bce',
      name: 'Babylonian Exile',
      startYear: -586,
      endYear: -539,
      summary: 'Forced displacement of Jews to Babylon.',
      significance: 'Crisis in Judah; formative for Judaism.',
      tags: ['Judah','Babylon'],
      confidence_score: 0.9,
      created_by: 'curator_demo',
    });

    await linkOccurredIn(session, 'babylonian-exile-586-539-bce', 'babylon');

    await upsertEvidence(session, {
      slug: 'needham-demo',
      name: 'Needham Ref',
      title: 'Illustrative Source',
      doi_or_url: 'https://doi.org/10.0000/demo',
      corpus_tier: 'B',
      created_by: 'curator_demo',
      corpus_codes: ['MESOPOTAMIAN_CORPUS'],
    });

    await linkFramedBy(session, {
      ew_slug: 'babylonian-exile-586-539-bce',
      fw_code: 'CAUSE_EFFECT',
      evidence_url: 'https://doi.org/10.0000/demo',
      page_refs: 'pp. 12–15',
      source_note: 'Standard synthesis',
      confidence_score: 0.95,
    });

    await attachEraByOverlap(session);
  } finally {
    await session.close();
    await driver.close();
  }
}
