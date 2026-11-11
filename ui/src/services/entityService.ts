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

/* ─── Short-lived entity cache (session) — instant back-nav ─── */
const ENTITY_CACHE_TTL = 5 * 60 * 1000
/** Soft revalidate window for open entity pages while bots enrich */
const ENTITY_STALE_TTL = 20 * 1000
const ENTITY_FETCH_TIMEOUT_MS = 12_000
const _entityCache = new Map<string, { entity: Entity; ts: number }>()

export function invalidateEntityCache(slug?: string) {
  if (slug) _entityCache.delete(slug)
  else _entityCache.clear()
}

function withTimeout<T>(promise: Promise<T>, ms: number, label: string): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    const t = window.setTimeout(() => reject(new Error(`${label} timed out after ${ms}ms`)), ms)
    promise.then(
      (v) => { window.clearTimeout(t); resolve(v) },
      (e) => { window.clearTimeout(t); reject(e) },
    )
  })
}

/** Fetch a single entity by slug from Appwrite */
export async function fetchEntity(
  slug: string,
  opts?: { force?: boolean },
): Promise<Entity | undefined> {
  const hit = _entityCache.get(slug)
  if (!opts?.force && hit && Date.now() - hit.ts < ENTITY_CACHE_TTL) return hit.entity
  try {
    const res = await withTimeout(
      databases.listDocuments(
        DATABASE_ID,
        COLLECTIONS.ENTITIES,
        [Query.equal('slug', slug), Query.limit(1)],
      ),
      ENTITY_FETCH_TIMEOUT_MS,
      `fetchEntity(${slug})`,
    )
    if (res.documents.length > 0) {
      const entity = mapDocToEntity(res.documents[0])
      _entityCache.set(slug, { entity, ts: Date.now() })
      return entity
    }
  } catch { /* no fallback — caller may keep prior paint */ }
  return undefined
}

/** True when cached entity should be silently revalidated (bots may have written). */
export function isEntityCacheStale(slug: string): boolean {
  const hit = _entityCache.get(slug)
  if (!hit) return true
  return Date.now() - hit.ts >= ENTITY_STALE_TTL
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
 * Search entities — multi-strategy search across Appwrite backend.
 *
 * Strategies (run in parallel, results merged + deduped):
 * 1. Fulltext name search  — word-prefix matching on the `name` field
 * 2. Slug exact match     — converts query to slug format for direct lookup
 * 3. Fulltext summary search — finds entities whose summary mentions the query
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

  /** Convert a human-readable query to Appwrite slug format */
  const toSlug = (s: string) =>
    s.trim().toLowerCase()
      .replace(/['']/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')

  const slugQuery = toSlug(q)

  // ── Run strategies in parallel ──
  const strategies: Promise<Entity[]>[] = [
    // Strategy 1: Fulltext name search (word-prefix matching)
    safeQuery([Query.search('name', q), Query.limit(limit)]),
    // Strategy 2: Exact slug lookup — catches "wright brothers" → "wright-brothers"
    safeQuery([Query.equal('slug', slugQuery), Query.limit(1)]),
  ]

  // Strategy 3: Fulltext summary search (catches topic matches)
  if (q.length >= 3) {
    strategies.push(safeQuery([Query.search('summary', q), Query.limit(limit)]))
  }

  // Wait for strategies in parallel
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

/**
 * Fetch shelf neighbors around a callNumber via indexed range seeks.
 *
 * Avoid Query.startsWith('callNumber', '440.') — with ~392k docs that prefix
 * matches thousands of rows and Appwrite's COUNT(*) makes the request take
 * 5–15s, which blocked EntityPage on "Loading Entity…".
 *
 * Bidirectional orderAsc/orderDesc seeks on the callNumber key index stay
 * in the tens–hundreds of ms.
 */
export async function fetchShelfNeighbors(callNumber: string, range = 5): Promise<Entity[]> {
  if (!callNumber) return []
  // Neighbor rail only needs identity fields — skip detailsJson blob
  const neighborSelect = Query.select([
    'slug', 'name', 'label', 'callNumber', 'eraSlug', 'era',
    'importanceScore', 'status', 'imageUrl', 'summary',
  ])
  try {
    const [after, before] = await Promise.all([
      databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.greaterThanEqual('callNumber', callNumber),
        Query.orderAsc('callNumber'),
        Query.limit(range + 1),
        neighborSelect,
      ]),
      databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.lessThan('callNumber', callNumber),
        Query.orderDesc('callNumber'),
        Query.limit(range),
        neighborSelect,
      ]),
    ])
    const prev = before.documents.map(mapDocToEntity).reverse()
    const next = after.documents.map(mapDocToEntity)
    // Dedup current entity if it appears in both (shouldn't, but safe)
    const seen = new Set<string>()
    const merged: Entity[] = []
    for (const e of [...prev, ...next]) {
      if (seen.has(e.slug)) continue
      seen.add(e.slug)
      merged.push(e)
    }
    return merged
  } catch { return [] }
}

/* ─── In-memory caches (30 min TTL) — reduce Appwrite reads ─── */
const CACHE_TTL = 30 * 60 * 1000
let _labelCache: { data: Record<string, number>; ts: number } | null = null
let _totalCache: { data: number; ts: number } | null = null

/** Prefer public stats_cache mirror — Appwrite listDocuments.total caps at 5000. */
async function readStatsMirror(): Promise<{ total?: number; byLabel?: Record<string, number> } | null> {
  try {
    const r = await fetch('/governance/stats_cache.json', { cache: 'no-store' })
    if (!r.ok) return null
    return await r.json()
  } catch {
    return null
  }
}

/** Fetch entity counts by label — prefer stats_cache mirror (API totals cap at 5000) */
export async function fetchLabelCounts(): Promise<Record<string, number>> {
  if (_labelCache && Date.now() - _labelCache.ts < CACHE_TTL) return _labelCache.data
  try {
    const mirrored = await readStatsMirror()
    if (mirrored?.byLabel && Object.keys(mirrored.byLabel).length > 0) {
      _labelCache = { data: mirrored.byLabel, ts: Date.now() }
      return mirrored.byLabel
    }
    const labels = ['EventWindow', 'Person', 'Movement', 'Institution', 'Text', 'Idea', 'Place', 'Evidence']
    const results = await Promise.all(
      labels.map(async (label) => {
        const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
          Query.equal('label', label), Query.limit(1),
        ])
        return { label, count: res.total }
      })
    )
    const data = Object.fromEntries(results.map(r => [r.label, r.count]))
    _labelCache = { data, ts: Date.now() }
    return data
  } catch { return _labelCache?.data ?? {} }
}

/** Fetch total entity count — prefer stats_cache mirror (API total caps at 5000) */
export async function fetchTotalCount(): Promise<number> {
  if (_totalCache && Date.now() - _totalCache.ts < CACHE_TTL) return _totalCache.data
  try {
    const mirrored = await readStatsMirror()
    if (typeof mirrored?.total === 'number' && mirrored.total > 0) {
      _totalCache = { data: mirrored.total, ts: Date.now() }
      return mirrored.total
    }
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(1)])
    // 5000 is Appwrite's hard cap — treat as unknown rather than truth
    const n = res.total >= 5000 ? 0 : res.total
    _totalCache = { data: n, ts: Date.now() }
    return n
  } catch { return _totalCache?.data ?? 0 }
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
    historicalSignificance: doc.historicalSignificance ?? details.historicalSignificance,
    altNames:       doc.altNames ?? [],
    externalLinks:  details.externalLinks ?? [],
    tags:           details.tags ?? [],
    quote:          details.quote,
    legacySummary:  details.legacySummary,
  } as Entity
}
