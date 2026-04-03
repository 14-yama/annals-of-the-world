/**
 * Entity Service — Hybrid Data Layer
 *
 * Queries Appwrite first; falls back to the static catalog.
 * This allows the app to work fully offline with bundled data
 * while progressively migrating to Appwrite-backed dynamic queries.
 */
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'
import { getEntity as getCatalogEntity, getAllEntities as getCatalogEntities, getShelfNeighbors as getCatalogShelfNeighbors } from '../data/catalog'
import type { Entity } from '../data/entityTypes'

/* ─── Flag: set to true once Appwrite collections are seeded ─── */
const USE_APPWRITE = true

/* ─── Read helpers ─── */

/** Fetch a single entity by slug — Appwrite first, static fallback */
export async function fetchEntity(slug: string): Promise<Entity | undefined> {
  if (USE_APPWRITE) {
    try {
      const res = await databases.listDocuments(
        DATABASE_ID,
        COLLECTIONS.ENTITIES,
        [Query.equal('slug', slug), Query.limit(1)],
      )
      if (res.documents.length > 0) return mapDocToEntity(res.documents[0])
    } catch { /* fall through */ }
  }
  return getCatalogEntity(slug)
}

/** Fetch all entities — paginated from Appwrite or full static catalog */
export async function fetchEntities(opts?: {
  era?: string
  label?: string
  continent?: string
  limit?: number
  offset?: number
}): Promise<Entity[]> {
  if (USE_APPWRITE) {
    try {
      const queries: string[] = []
      if (opts?.era)       queries.push(Query.equal('eraSlug', opts.era))
      if (opts?.label)     queries.push(Query.equal('label', opts.label))
      if (opts?.continent) queries.push(Query.equal('continent', opts.continent))
      queries.push(Query.limit(opts?.limit ?? 100))
      if (opts?.offset)    queries.push(Query.offset(opts.offset))

      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, queries)
      return res.documents.map(mapDocToEntity)
    } catch { /* fall through */ }
  }
  let entities = getCatalogEntities()
  if (opts?.era)       entities = entities.filter(e => e.eraSlug === opts.era)
  if (opts?.label)     entities = entities.filter(e => e.label === opts.label)
  if (opts?.continent) entities = entities.filter(e => e.continent === opts.continent)
  const start = opts?.offset ?? 0
  return entities.slice(start, start + (opts?.limit ?? entities.length))
}

/** Search entities by name or summary text */
export async function searchEntities(query: string, limit = 20): Promise<Entity[]> {
  if (USE_APPWRITE) {
    try {
      const res = await databases.listDocuments(
        DATABASE_ID,
        COLLECTIONS.ENTITIES,
        [Query.search('name', query), Query.limit(limit)],
      )
      return res.documents.map(mapDocToEntity)
    } catch { /* fall through */ }
  }
  const q = query.toLowerCase()
  return getCatalogEntities()
    .filter(e => e.name.toLowerCase().includes(q) || e.summary.toLowerCase().includes(q))
    .slice(0, limit)
}

/** Fetch shelf neighbors (same division) — uses static catalog for fast prefix matching */
export function fetchShelfNeighbors(callNumber: string, range = 5): Entity[] {
  return getCatalogShelfNeighbors(callNumber, range)
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
  if (!USE_APPWRITE) return []
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
  if (!USE_APPWRITE) return []
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
  if (!USE_APPWRITE) return []
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
