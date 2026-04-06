/**
 * Entity Service — Appwrite Backend Data Layer
 *
 * All data is fetched from the Appwrite backend (381,000+ entities).
 * No static catalog fallback — the backend IS the source of truth.
 */
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'
import type { Entity } from '../data/entityTypes'

/* ─── Read helpers ─── */

/** Fetch a single entity by slug from Appwrite */
export async function fetchEntity(slug: string): Promise<Entity | undefined> {
  try {
    const res = await databases.listDocuments(
      DATABASE_ID,
      COLLECTIONS.ENTITIES,
      [Query.equal('slug', slug), Query.limit(1)],
    )
    if (res.documents.length > 0) return mapDocToEntity(res.documents[0])
  } catch { /* no fallback */ }
  return undefined
}

/** Fetch entities — paginated from Appwrite */
export async function fetchEntities(opts?: {
  era?: string
  label?: string
  continent?: string
  eraDivision?: string
  limit?: number
  offset?: number
}): Promise<Entity[]> {
  try {
    const queries: string[] = []
    if (opts?.era)           queries.push(Query.equal('eraSlug', opts.era))
    if (opts?.label)         queries.push(Query.equal('label', opts.label))
    if (opts?.continent)     queries.push(Query.equal('continent', opts.continent))
    if (opts?.eraDivision)   queries.push(Query.equal('eraDivisionCode', opts.eraDivision))
    queries.push(Query.limit(opts?.limit ?? 100))
    if (opts?.offset)        queries.push(Query.offset(opts.offset))

    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
    return res.documents.map(mapDocToEntity)
  } catch { return [] }
}

/**
 * Search entities — deep multi-strategy search across 400K+ Appwrite backend.
 *
 * Strategies (run in parallel where possible):
 * 1. Fulltext name search  — word-prefix matching on the `name` field
 * 2. Fulltext summary search — finds entities whose summary mentions the query
 * 3. Slug prefix search    — hyphenated + underscore variants
 * 4. Exact slug lookup     — handles pasted slugs like "julius-caesar"
 * 5. Call number prefix    — "290", "220.06", etc.
 *
 * Results are merged, deduplicated by slug, and sorted by importanceScore.
 */
export async function searchEntities(query: string, limit = 25): Promise<Entity[]> {
  const q = query.trim()
  if (!q) return []

  const seen = new Set<string>()
  const results: Entity[] = []

  const addUnique = (entities: Entity[]) => {
    for (const e of entities) {
      if (!seen.has(e.slug)) {
        seen.add(e.slug)
        results.push(e)
      }
    }
  }

  /** Safe query wrapper — returns empty on any failure */
  const safeQuery = async (queries: string[]): Promise<Entity[]> => {
    try {
      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
      return res.documents.map(mapDocToEntity)
    } catch {
      return []
    }
  }

  // ── Build slug variants ──
  const slugHyphen = q.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '')
  const slugUnder  = q.toLowerCase().replace(/\s+/g, '_').replace(/[^a-z0-9_]/g, '')
  const isCallNum  = /^\d/.test(q)

  // ── Run strategies in parallel for speed ──
  const strategies: Promise<Entity[]>[] = []

  // Strategy 1: Fulltext name search
  strategies.push(safeQuery([Query.search('name', q), Query.limit(limit)]))

  // Strategy 2: Fulltext summary search (catches entities whose name doesn't match but topic does)
  if (q.length >= 3) {
    strategies.push(safeQuery([Query.search('summary', q), Query.limit(limit)]))
  }

  // Strategy 3: Slug prefix search — both hyphen and underscore variants
  if (slugHyphen.length >= 2) {
    strategies.push(safeQuery([Query.startsWith('slug', slugHyphen), Query.limit(limit)]))
  }
  if (slugUnder.length >= 2 && slugUnder !== slugHyphen) {
    strategies.push(safeQuery([Query.startsWith('slug', slugUnder), Query.limit(limit)]))
  }

  // Strategy 4: Exact slug match (user may paste "julius-caesar" or "alexander_the_great")
  if (slugHyphen.length >= 3) {
    strategies.push(safeQuery([Query.equal('slug', slugHyphen), Query.limit(1)]))
  }
  if (slugUnder.length >= 3 && slugUnder !== slugHyphen) {
    strategies.push(safeQuery([Query.equal('slug', slugUnder), Query.limit(1)]))
  }

  // Strategy 5: Call number prefix search
  if (isCallNum) {
    strategies.push(safeQuery([Query.startsWith('callNumber', q), Query.limit(limit)]))
  }

  // Wait for all strategies in parallel
  const batches = await Promise.all(strategies)
  for (const batch of batches) {
    addUnique(batch)
  }

  // Rank by query relevance (primary) + importance (secondary)
  const ql = q.toLowerCase()
  results.sort((a, b) => {
    const ra = nameRelevance(a.name, ql)
    const rb = nameRelevance(b.name, ql)
    if (rb !== ra) return rb - ra                      // exact > starts > contains > partial
    const sa = a.importanceScore ?? 0
    const sb = b.importanceScore ?? 0
    if (sb !== sa) return sb - sa                      // higher importance first
    return a.name.localeCompare(b.name)                // alphabetical tie-break
  })

  return results.slice(0, limit)
}

/** Score how well an entity name matches the query — higher is better */
function nameRelevance(name: string, queryLower: string): number {
  const nl = name.toLowerCase()
  if (nl === queryLower) return 100                    // exact
  if (nl.startsWith(queryLower)) return 80             // prefix
  // Check if ALL query words appear in the name
  const words = queryLower.split(/\s+/)
  const allPresent = words.every(w => nl.includes(w))
  if (allPresent) return 60                            // all words match
  if (nl.includes(queryLower)) return 50               // substring
  // At least one word matches
  if (words.some(w => nl.includes(w))) return 30
  return 0                                             // matched via slug/callNumber only
}

/** Fetch shelf neighbors by callNumber prefix from Appwrite */
export async function fetchShelfNeighbors(callNumber: string, range = 5): Promise<Entity[]> {
  try {
    // Extract division prefix (e.g., "220.06-julius-caesar" → "220")
    const parts = callNumber.split('.')
    const prefix = parts[0] || ''
    if (!prefix) return []
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
      Query.startsWith('callNumber', prefix + '.'),
      Query.limit(range * 2 + 1),
    ])
    return res.documents.map(mapDocToEntity)
  } catch { return [] }
}

/** Fetch entity counts by label — for dashboards and stats */
export async function fetchLabelCounts(): Promise<Record<string, number>> {
  try {
    const labels = ['EventWindow', 'Person', 'Movement', 'Institution', 'Text', 'Idea', 'Place', 'Evidence']
    const results = await Promise.all(
      labels.map(async (label) => {
        const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
          Query.equal('label', label), Query.limit(1),
        ])
        return { label, count: res.total }
      })
    )
    return Object.fromEntries(results.map(r => [r.label, r.count]))
  } catch { return {} }
}

/** Fetch total entity count */
export async function fetchTotalCount(): Promise<number> {
  try {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(1)])
    return res.total
  } catch { return 0 }
}

/** Fetch entities with total count — server-side filtered, paginated */
export async function fetchEntitiesWithTotal(opts?: {
  era?: string
  label?: string
  continent?: string
  eraDivision?: string
  search?: string
  limit?: number
  offset?: number
}): Promise<{ entities: Entity[]; total: number }> {
  try {
    const queries: string[] = []
    if (opts?.era)           queries.push(Query.equal('eraSlug', opts.era))
    if (opts?.label)         queries.push(Query.equal('label', opts.label))
    if (opts?.continent)     queries.push(Query.equal('continent', opts.continent))
    if (opts?.eraDivision)   queries.push(Query.equal('eraDivisionCode', opts.eraDivision))
    if (opts?.search)        queries.push(Query.search('name', opts.search))
    queries.push(Query.limit(opts?.limit ?? 100))
    if (opts?.offset)        queries.push(Query.offset(opts.offset))

    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
    return { entities: res.documents.map(mapDocToEntity), total: res.total }
  } catch { return { entities: [], total: 0 } }
}

/** Fetch entities by subjects array — for corpus pages */
export async function fetchEntitiesBySubject(subject: string, opts?: {
  limit?: number
  offset?: number
}): Promise<{ entities: Entity[]; total: number }> {
  try {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
      Query.search('name', subject),
      Query.limit(opts?.limit ?? 100),
      ...(opts?.offset ? [Query.offset(opts.offset)] : []),
    ])
    return { entities: res.documents.map(mapDocToEntity), total: res.total }
  } catch { return { entities: [], total: 0 } }
}

/** Check if an entity exists by slug (lightweight) */
export async function entityExists(slug: string): Promise<boolean> {
  try {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
      Query.equal('slug', slug), Query.limit(1), Query.select(['slug']),
    ])
    return res.documents.length > 0
  } catch { return false }
}

/* ─── Evidence & Media (Appwrite-only, no static fallback) ─── */

export interface EvidenceRecord {
  id: string
  entitySlug: string
  title: string
  author?: string
  year?: number
  doiOrUrl?: string
  tier: string          // A–F
  citation: string
  sourceNote?: string
}

export interface MediaRecord {
  id: string
  entitySlug: string
  fileId?: string
  url: string
  alt: string
  credit?: string
  category: 'portrait' | 'artifact' | 'map' | 'architecture' | 'landscape' | 'art'
  caption?: string
}

export interface TimelineEntry {
  id: string
  entitySlug: string
  year: number
  endYear?: number
  title: string
  description: string
  significance: 'low' | 'medium' | 'high' | 'critical'
}

/** Fetch evidence records for an entity */
export async function fetchEvidence(entitySlug: string): Promise<EvidenceRecord[]> {
  try {
    const res = await databases.listDocuments(
      DATABASE_ID, COLLECTIONS.EVIDENCE,
      [Query.equal('entitySlug', entitySlug), Query.limit(50)],
    )
    return res.documents.map((d: Record<string, unknown>) => ({
      id: d.$id as string,
      entitySlug: d.entitySlug as string,
      title: d.title as string,
      author: d.author as string | undefined,
      year: d.year as number | undefined,
      doiOrUrl: d.doiOrUrl as string | undefined,
      tier: d.tier as string,
      citation: d.citation as string,
      sourceNote: d.sourceNote as string | undefined,
    }))
  } catch { return [] }
}

/** Fetch media records for an entity */
export async function fetchMedia(entitySlug: string): Promise<MediaRecord[]> {
  try {
    const res = await databases.listDocuments(
      DATABASE_ID, COLLECTIONS.MEDIA,
      [Query.equal('entitySlug', entitySlug), Query.limit(50)],
    )
    return res.documents.map((d: Record<string, unknown>) => ({
      id: d.$id as string,
      entitySlug: d.entitySlug as string,
      fileId: d.fileId as string | undefined,
      url: d.url as string,
      alt: d.alt as string,
      credit: d.credit as string | undefined,
      category: d.category as MediaRecord['category'],
      caption: d.caption as string | undefined,
    }))
  } catch { return [] }
}

/** Fetch timeline entries for an entity */
export async function fetchTimeline(entitySlug: string): Promise<TimelineEntry[]> {
  try {
    const res = await databases.listDocuments(
      DATABASE_ID, COLLECTIONS.TIMELINE,
      [Query.equal('entitySlug', entitySlug), Query.orderAsc('year'), Query.limit(100)],
    )
    return res.documents.map((d: Record<string, unknown>) => ({
      id: d.$id as string,
      entitySlug: d.entitySlug as string,
      year: d.year as number,
      endYear: d.endYear as number | undefined,
      title: d.title as string,
      description: d.description as string,
      significance: d.significance as TimelineEntry['significance'],
    }))
  } catch { return [] }
}

/* ─── Helpers ─── */

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function mapDocToEntity(doc: any): Entity {
  // Unpack consolidated details blob
  const details = doc.detailsJson ? JSON.parse(doc.detailsJson) : {}
  return {
    slug:           doc.slug,
    name:           doc.name,
    label:          doc.label,
    callNumber:     doc.callNumber,
    subjectHeadings: doc.subjectHeadings ?? [],
    subjects:       doc.subjects ?? [],
    summary:        doc.summary ?? '',
    born:           doc.born,
    died:           doc.died,
    founded:        doc.founded,
    period:         doc.period,
    startDate:      doc.startDate,
    endDate:        doc.endDate,
    era:            doc.era,
    eraSlug:        doc.eraSlug,
    eraDivision:    doc.eraDivision,
    eraDivisionCode: doc.eraDivisionCode,
    region:         doc.region,
    continent:      doc.continent,
    status:         doc.status,
    frameworks:     doc.frameworks ?? [],
    causes:         details.causes ?? [],
    effects:        details.effects ?? [],
    relationships:  details.relationships ?? [],
    places:         details.places ?? [],
    texts:          details.texts ?? [],
    wikidataQid:    doc.wikidataQid,
    wikipediaUrl:   doc.wikipediaUrl,
    imageUrl:       doc.imageUrl,
    thumbnailUrl:   details.thumbnailUrl,
    importanceScore: doc.importanceScore,
    altNames:       doc.altNames ?? [],
    externalLinks:  details.externalLinks ?? [],
    tags:           details.tags ?? [],
    quote:          details.quote,
    legacySummary:  details.legacySummary,
  } as Entity
}
