/**
 * Entity Type Definitions
 *
 * Shared interfaces for the entity/catalog data layer.
 * Extracted to avoid circular dependencies between catalog data files and entities.ts.
 */

export interface EntityRelationship {
  sourceSlug: string
  sourceName: string
  verb: string
  targetSlug: string
  targetName: string
  context?: string
}

export interface EntityCause {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityEffect {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityPlace {
  name: string
  role: string
  slug?: string
}

export interface EntityText {
  title: string
  type: string
  year?: string
  slug?: string
}

export type NodeLabel =
  | 'Person'
  | 'Idea'
  | 'Institution'
  | 'Place'
  | 'EventWindow'
  | 'Movement'
  | 'Text'
  | 'Evidence'

export interface Entity {
  slug: string
  name: string
  label: NodeLabel
  callNumber: string
  subjectHeadings: string[]
  subjects: string[]
  summary: string
  born?: string
  died?: string
  founded?: string
  period?: string
  startDate?: string
  endDate?: string
  era: string
  eraSlug: string
  eraDivision?: string      // Specific sub-period (e.g. "Age of Enlightenment")
  eraDivisionCode?: string  // Dewey code (e.g. "944")
  region: string
  continent: string
  status: string
  frameworks?: string[]
  causes: EntityCause[]
  effects: EntityEffect[]
  relationships: EntityRelationship[]
  places: EntityPlace[]
  texts: EntityText[]

  /* ── v2 attributes (Appwrite backend + enrichment) ── */
  wikidataQid?: string
  wikipediaUrl?: string
  imageUrl?: string
  thumbnailUrl?: string
  importanceScore?: number
  altNames?: string[]
  externalLinks?: string[]
  tags?: string[]
  quote?: string
  legacySummary?: string

  /* ── v3 attributes (historical significance + edge quality) ── */
  historicalSignificance?: HistoricalSignificance
}

/** Historical significance rating — required on all enriched entities (summary ≥ 600c). */
export interface HistoricalSignificance {
  /** 1–10 calibrated score. 9–10 = world-changing (e.g. Einstein, French Revolution). */
  significanceScore: number
  /** 1–2 sentence explanation naming real consequences, numbers, or successor events. */
  significanceNarrative: string
  /** Broad impact category. */
  significanceCategory: 'world-changing' | 'continental' | 'regional' | 'local'
}

/**
 * Returns the minimum number of graph edges required for an entity with the given
 * significanceScore. Entities with fewer edges are flagged as quality violations.
 *
 * | Score | Category      | Min Edges | Example                     |
 * |-------|---------------|-----------|-----------------------------|
 * | 9–10  | world-changing| 15        | Einstein, Islam, printing press |
 * | 7–8   | continental   | 8         | Napoleon, Black Death        |
 * | 5–6   | regional      | 4         | Major battles, key inventors |
 * | 3–4   | local         | 2         | Secondary rulers, movements  |
 * | 1–2   | minor         | 1         | Local events, footnote figures |
 * | —     | unrated       | 0         | Stubs awaiting enrichment    |
 */
export function minEdgesForScore(score: number): number {
  if (score >= 9) return 15
  if (score >= 7) return 8
  if (score >= 5) return 4
  if (score >= 3) return 2
  return 1
}

/** True if the entity has fewer edges than its significance requires. */
export function isUnderConnected(entity: Pick<Entity, 'relationships' | 'historicalSignificance'>): boolean {
  const score = entity.historicalSignificance?.significanceScore
  if (!score) return false
  return (entity.relationships?.length ?? 0) < minEdgesForScore(score)
}
