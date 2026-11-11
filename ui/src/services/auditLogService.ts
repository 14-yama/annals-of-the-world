/**
 * Audit log fetch helpers.
 *
 * Appwrite listDocuments `.total` hard-caps at 5000 — never treat that as the
 * true audit_log size. Prefer stats_cache.auditTotal (paged cursor count),
 * and fall back to honest capped messaging.
 */
import { Query, type Models } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'

export const APPWRITE_TOTAL_CAP = 5000

export interface AuditLogRow {
  $id: string
  entityId: string
  entitySlug: string
  entityName: string
  action: string
  field: string
  oldValue: string
  newValue: string
  editorId: string
  editorNote: string
  timestamp: string
  sessionId: string
}

export interface AuditLogTotal {
  /** Best-known total (cache or live). */
  total: number
  /** True when value comes from a full/uncapped source. */
  exact: boolean
  /** True when Appwrite returned the 5k cap and we lack a better cache. */
  capped: boolean
  /** Human-readable provenance for the UI. */
  source: 'stats_cache' | 'listDocuments' | 'realtime' | 'unknown'
  updatedAt: string | null
}

export interface AuditLogPage {
  rows: AuditLogRow[]
  /** listDocuments.total for this filtered query (may be capped). */
  queryTotal: number
  queryCapped: boolean
  /** Cursor for the next page (last doc $id), or null at end. */
  nextCursor: string | null
}

export function mapAuditDoc(doc: Models.Document): AuditLogRow {
  return {
    $id: doc.$id,
    entityId: (doc.entityId as string) ?? '',
    entitySlug: (doc.entitySlug as string) ?? '',
    entityName: (doc.entityName as string) ?? '',
    action: (doc.action as string) ?? '',
    field: (doc.field as string) ?? '',
    oldValue: (doc.oldValue as string) ?? '',
    newValue: (doc.newValue as string) ?? '',
    editorId: (doc.editorId as string) ?? '',
    editorNote: (doc.editorNote as string) ?? '',
    timestamp: (doc.timestamp as string) ?? '',
    sessionId: (doc.sessionId as string) ?? '',
  }
}

function isCapped(n: number | undefined | null): boolean {
  return typeof n === 'number' && n >= APPWRITE_TOTAL_CAP
}

/** Read auditTotal from the public stats_cache mirror (same origin). */
export async function fetchAuditTotalFromCache(): Promise<AuditLogTotal | null> {
  try {
    const r = await fetch(`/governance/stats_cache.json?t=${Date.now()}`, { cache: 'no-store' })
    if (!r.ok) return null
    const mirrored = await r.json() as {
      auditTotal?: number
      auditTotalUpdatedAt?: string
      updatedAt?: string
    }
    const n = Number(mirrored.auditTotal || 0)
    // Large values are the POINT of the cache (Appwrite caps listDocuments.total
    // at 5000). Never treat auditTotal ≥ 5000 as "capped / unusable".
    if (!Number.isFinite(n) || n <= 0) return null
    return {
      total: n,
      exact: true,
      capped: false,
      source: 'stats_cache',
      updatedAt: mirrored.auditTotalUpdatedAt || mirrored.updatedAt || null,
    }
  } catch {
    return null
  }
}

/**
 * Best available audit_log total.
 * Prefer stats_cache.auditTotal; otherwise listDocuments head (may be capped).
 */
export async function fetchAuditLogTotal(filters?: {
  entitySlug?: string
  editorId?: string
  action?: string
}): Promise<AuditLogTotal> {
  const hasFilters = !!(filters?.entitySlug || filters?.editorId || filters?.action)

  // Unfiltered: prefer cache (true corpus size)
  if (!hasFilters) {
    const cached = await fetchAuditTotalFromCache()
    if (cached) return cached
  }

  try {
    const queries: string[] = [Query.limit(1)]
    if (filters?.entitySlug) queries.push(Query.search('entitySlug', filters.entitySlug))
    if (filters?.editorId) queries.push(Query.equal('editorId', filters.editorId))
    if (filters?.action) queries.push(Query.equal('action', filters.action))
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, queries)
    const capped = isCapped(res.total)
    return {
      total: res.total,
      exact: !capped,
      capped,
      source: 'listDocuments',
      updatedAt: null,
    }
  } catch {
    return { total: 0, exact: false, capped: false, source: 'unknown', updatedAt: null }
  }
}

/**
 * Fetch one page of audit rows, newest-first.
 * Prefer cursorAfter over large offsets (Appwrite also caps offset reach ~5k).
 */
export async function fetchAuditLogPage(opts: {
  limit?: number
  cursorAfter?: string | null
  entitySlug?: string
  editorId?: string
  action?: string
}): Promise<AuditLogPage> {
  const limit = opts.limit ?? 50
  const queries: string[] = [
    Query.orderDesc('timestamp'),
    Query.limit(limit),
  ]
  if (opts.cursorAfter) queries.push(Query.cursorAfter(opts.cursorAfter))
  if (opts.entitySlug) queries.push(Query.search('entitySlug', opts.entitySlug))
  if (opts.editorId) queries.push(Query.equal('editorId', opts.editorId))
  if (opts.action) queries.push(Query.equal('action', opts.action))

  const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, queries)
  const rows = res.documents.map(mapAuditDoc)
  const nextCursor =
    rows.length >= limit ? rows[rows.length - 1].$id : null

  return {
    rows,
    queryTotal: res.total,
    queryCapped: isCapped(res.total),
    nextCursor,
  }
}
