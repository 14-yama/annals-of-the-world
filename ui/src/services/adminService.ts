/**
 * Admin Service — Appwrite Write Operations
 *
 * Provides curator-level CRUD against the Appwrite backend.
 * Uses the same public Databases client (Appwrite permissions handle access).
 * For bulk/batch ops the API key is used server-side via Python scripts.
 */
import { Query, type Models } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'
import { adminUpdateDocument, adminBatchUpdate } from '../lib/adminClient'

/* ─── Types ─── */

export interface AuditStats {
  total: number
  byLabel: Record<string, number>
  byEra: Record<string, number>
  byContinent: Record<string, number>
  missingRelationships: number
  missingEvidence: number
  missingImage: number
  avgScore: number
}

export interface EntityCompleteness {
  slug: string
  name: string
  label: string
  era: string
  score: number
  hasRelationships: boolean
  hasCauses: boolean
  hasEffects: boolean
  hasFrameworks: boolean
  hasPlaces: boolean
  hasTexts: boolean
  hasImage: boolean
  hasWikidata: boolean
  hasSummary: boolean
  relationshipCount: number
  missingFields: string[]
}

export interface DivisionCount {
  code: string
  heading: string
  count: number
}

/* ─── Read: Accurate Counting ─── */

/**
 * Count documents matching queries using Appwrite's res.total (accurate up to ~5000).
 * For counts above 5000, falls back to cursor pagination with localStorage cache.
 *
 * COST-OPTIMISED: Was previously doing full cursor pagination (~4000 API calls
 * for 400K entities). Now uses single query + localStorage cache (24h TTL).
 */
const COUNT_CACHE_TTL = 24 * 60 * 60 * 1000 // 24 hours

export async function countAllDocuments(
  extraQueries: string[] = [],
): Promise<number> {
  // Build a cache key from the queries
  const cacheKey = `annals_count_${JSON.stringify(extraQueries)}`

  // Check localStorage cache first
  try {
    const cached = localStorage.getItem(cacheKey)
    if (cached) {
      const { count, ts } = JSON.parse(cached)
      if (Date.now() - ts < COUNT_CACHE_TTL) return count
    }
  } catch { /* localStorage may not be available */ }

  // Fast path: single query using res.total (accurate for < ~5000)
  const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
    ...extraQueries,
    Query.select(['$id']),
    Query.limit(1),
  ])

  let count = res.total

  // If total >= 5000, Appwrite may be capping — use cursor pagination
  if (count >= 5000) {
    const PAGE = 500
    count = 0
    let cursor: string | undefined

    // eslint-disable-next-line no-constant-condition
    while (true) {
      const q: string[] = [
        ...extraQueries,
        Query.select(['$id']),
        Query.limit(PAGE),
      ]
      if (cursor) q.push(Query.cursorAfter(cursor))

      const batch = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, q)
      count += batch.documents.length

      if (batch.documents.length < PAGE) break
      cursor = batch.documents[batch.documents.length - 1].$id
    }
  }

  // Cache the result
  try {
    localStorage.setItem(cacheKey, JSON.stringify({ count, ts: Date.now() }))
  } catch { /* non-fatal */ }

  return count
}

/* ─── Read: Audit Queries ─── */

const LABELS = ['Person', 'Idea', 'Institution', 'Place', 'EventWindow', 'Movement', 'Text', 'Evidence', 'Timeframe']
const ERAS = ['Prehistoric', 'Classical', 'Medieval', 'Early Modern', 'Modern', 'Contemporary']
const CONTINENTS = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Multiple Regions']

/** Fetch aggregate audit statistics */
export async function fetchAuditStats(): Promise<AuditStats> {
  const [labelCounts, eraCounts, continentCounts, total] = await Promise.all([
    countByField('label', LABELS),
    countByField('era', ERAS),
    countByField('continent', CONTINENTS),
    fetchTotal(),
  ])

  // Sample entities to estimate missing fields
  const sample = await sampleEntities(200)
  let missingRels = 0, missingEvidence = 0, missingImage = 0, totalScore = 0

  for (const doc of sample) {
    const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
    const rels = details.relationships ?? []
    if (rels.length === 0) missingRels++
    if (!doc.imageUrl) missingImage++
    if (!details.texts || details.texts.length === 0) missingEvidence++
    totalScore += (doc.importanceScore as number) ?? 0
  }

  const ratio = total > 0 ? total / Math.max(sample.length, 1) : 1

  return {
    total,
    byLabel: labelCounts,
    byEra: eraCounts,
    byContinent: continentCounts,
    missingRelationships: Math.round(missingRels * ratio),
    missingEvidence: Math.round(missingEvidence * ratio),
    missingImage: Math.round(missingImage * ratio),
    avgScore: sample.length > 0 ? +(totalScore / sample.length).toFixed(1) : 0,
  }
}

/** Count entities grouped by a field */
async function countByField(field: string, values: string[]): Promise<Record<string, number>> {
  const counts: Record<string, number> = {}
  await Promise.all(
    values.map(async (val) => {
      try {
        const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
          Query.equal(field, val), Query.limit(1),
        ])
        counts[val] = res.total
      } catch { counts[val] = 0 }
    }),
  )
  return counts
}

async function fetchTotal(): Promise<number> {
  try {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(1)])
    return res.total
  } catch { return 0 }
}

async function sampleEntities(n: number): Promise<Models.Document[]> {
  try {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(n)])
    return res.documents
  } catch { return [] }
}

/** Fetch entities by division code — for division browser */
export async function fetchEntitiesByDivision(
  divisionCode: string,
  opts?: { limit?: number; offset?: number; search?: string },
): Promise<{ entities: Models.Document[]; total: number }> {
  try {
    const queries: string[] = [
      Query.startsWith('callNumber', divisionCode + '.'),
      Query.limit(opts?.limit ?? 50),
    ]
    if (opts?.offset) queries.push(Query.offset(opts.offset))
    if (opts?.search) queries.push(Query.search('name', opts.search))
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
    return { entities: res.documents, total: res.total }
  } catch { return { entities: [], total: 0 } }
}

/** Count entities for each division code (for People Hub cards) */
export async function fetchDivisionCounts(divisionCodes: string[]): Promise<DivisionCount[]> {
  const results: DivisionCount[] = []
  // Batch in groups of 10 to avoid rate limits
  for (let i = 0; i < divisionCodes.length; i += 10) {
    const batch = divisionCodes.slice(i, i + 10)
    const batchResults = await Promise.all(
      batch.map(async (code) => {
        try {
          const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
            Query.startsWith('callNumber', code + '.'),
            Query.limit(1),
          ])
          return { code, heading: '', count: res.total }
        } catch { return { code, heading: '', count: 0 } }
      }),
    )
    results.push(...batchResults)
  }
  return results
}

/** Fetch entities that need audit attention (low score, missing fields) */
export async function fetchEntitiesNeedingAudit(opts?: {
  label?: string
  maxScore?: number
  limit?: number
  offset?: number
}): Promise<{ entities: Models.Document[]; total: number }> {
  try {
    const queries: string[] = []
    if (opts?.label) queries.push(Query.equal('label', opts.label))
    // Sort by importanceScore descending to prioritize important entities
    queries.push(Query.orderDesc('importanceScore'))
    queries.push(Query.limit(opts?.limit ?? 50))
    if (opts?.offset) queries.push(Query.offset(opts.offset))
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
    return { entities: res.documents, total: res.total }
  } catch { return { entities: [], total: 0 } }
}

/** Analyze entity completeness from a raw Appwrite document */
export function analyzeCompleteness(doc: Models.Document): EntityCompleteness {
  const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
  const rels = details.relationships ?? []
  const causes = details.causes ?? []
  const effects = details.effects ?? []
  const places = details.places ?? []
  const texts = details.texts ?? []
  const frameworks = (doc.frameworks as string[]) ?? []

  const hasRelationships = rels.length > 0
  const hasCauses = causes.length > 0
  const hasEffects = effects.length > 0
  const hasFrameworks = frameworks.length > 0
  const hasPlaces = places.length > 0
  const hasTexts = texts.length > 0
  const hasImage = !!(doc.imageUrl as string)
  const hasWikidata = !!(doc.wikidataQid as string)
  const hasSummary = ((doc.summary as string) ?? '').length > 50

  const missing: string[] = []
  if (!hasRelationships) missing.push('relationships')
  if (!hasCauses) missing.push('causes')
  if (!hasEffects) missing.push('effects')
  if (!hasFrameworks) missing.push('frameworks')
  if (!hasPlaces) missing.push('places')
  if (!hasTexts) missing.push('texts/evidence')
  if (!hasImage) missing.push('image')
  if (!hasWikidata) missing.push('wikidataQid')
  if (!hasSummary) missing.push('summary')

  return {
    slug: doc.slug as string,
    name: doc.name as string,
    label: doc.label as string,
    era: doc.era as string,
    score: (doc.importanceScore as number) ?? 0,
    hasRelationships,
    hasCauses,
    hasEffects,
    hasFrameworks,
    hasPlaces,
    hasTexts,
    hasImage,
    hasWikidata,
    hasSummary,
    relationshipCount: rels.length,
    missingFields: missing,
  }
}

/* ─── Write: Entity Updates ─── */

/** Update a single entity field(s) in Appwrite via admin API key */
export async function updateEntity(
  documentId: string,
  fields: Record<string, unknown>,
): Promise<boolean> {
  const result = await adminUpdateDocument(COLLECTIONS.ENTITIES, documentId, fields)
  if (!result.success) {
    console.error('Failed to update entity:', documentId, result.error)
  }
  return result.success
}

/**
 * Update the detailsJson blob — merges new fields into existing JSON.
 * Pass only the keys you want to change.
 */
export async function updateEntityDetails(
  documentId: string,
  detailsJson: string,
  updates: Record<string, unknown>,
): Promise<boolean> {
  try {
    const existing = detailsJson ? JSON.parse(detailsJson) : {}
    const merged = { ...existing, ...updates }
    const result = await adminUpdateDocument(COLLECTIONS.ENTITIES, documentId, {
      detailsJson: JSON.stringify(merged),
    })
    if (!result.success) {
      console.error('Failed to update entity details:', documentId, result.error)
    }
    return result.success
  } catch (err) {
    console.error('Failed to update entity details:', documentId, err)
    return false
  }
}

/** Batch update multiple entities — chunked at 10/batch to respect rate limits */
export async function batchUpdateEntities(
  updates: Array<{ documentId: string; fields: Record<string, unknown> }>,
  onProgress?: (done: number, total: number) => void,
): Promise<{ success: number; failed: number }> {
  const mapped = updates.map(u => ({ documentId: u.documentId, data: u.fields }))
  const result = await adminBatchUpdate(COLLECTIONS.ENTITIES, mapped, onProgress)
  return { success: result.success, failed: result.failed }
}
