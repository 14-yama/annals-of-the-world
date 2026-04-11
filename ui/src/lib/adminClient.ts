/**
 * Admin Client — Appwrite REST API with API Key Authentication
 *
 * The Appwrite Web SDK uses client-side sessions which lack write permissions.
 * This module provides direct REST API access using the API key for curator
 * write operations (update, delete). Read operations continue to use the SDK.
 *
 * SECURITY NOTE: The API key is exposed to the browser. This is acceptable for
 * an internal curator tool. Do NOT use this pattern for public-facing apps.
 */

const ENDPOINT = import.meta.env.VITE_APPWRITE_ENDPOINT as string
const PROJECT_ID = import.meta.env.VITE_APPWRITE_PROJECT_ID as string
const API_KEY = import.meta.env.VITE_APPWRITE_API_KEY as string
const DATABASE_ID = (import.meta.env.VITE_APPWRITE_DATABASE_ID as string) || 'annals_db'

/* ─── Curator Identity ─── */

const SESSION_ID = crypto.randomUUID()

/** The head curator's permanent handle */
export const HEAD_CURATOR = '館長 -kanchō'

export type CuratorRole = 'head' | 'curator' | 'viewer'

export interface CuratorProfile {
  name: string
  role: CuratorRole
  addedBy: string
  addedAt: string
}

/**
 * Load authorised curators list from localStorage.
 * Head curator is always included.
 */
export function getCurators(): CuratorProfile[] {
  const stored = localStorage.getItem('curator_roster')
  const roster: CuratorProfile[] = stored ? JSON.parse(stored) : []
  // Ensure head curator is always present
  if (!roster.some(c => c.name === HEAD_CURATOR)) {
    roster.unshift({ name: HEAD_CURATOR, role: 'head', addedBy: 'system', addedAt: new Date().toISOString() })
    localStorage.setItem('curator_roster', JSON.stringify(roster))
  }
  return roster
}

/** Add a new curator (only head curator can do this) */
export function addCurator(name: string, role: CuratorRole = 'curator'): boolean {
  const current = getCuratorId()
  if (current !== HEAD_CURATOR) {
    console.warn('Only the head curator can add new curators')
    return false
  }
  const roster = getCurators()
  if (roster.some(c => c.name === name)) return false // already exists
  roster.push({ name, role, addedBy: current, addedAt: new Date().toISOString() })
  localStorage.setItem('curator_roster', JSON.stringify(roster))
  return true
}

/** Remove a curator (only head curator can do this) */
export function removeCurator(name: string): boolean {
  if (name === HEAD_CURATOR) return false // cannot remove head curator
  const current = getCuratorId()
  if (current !== HEAD_CURATOR) return false
  const roster = getCurators().filter(c => c.name !== name)
  localStorage.setItem('curator_roster', JSON.stringify(roster))
  return true
}

/** Get or prompt for curator name (head curator is default) */
export function getCuratorId(): string {
  let id = localStorage.getItem('curator_id')
  if (!id) {
    // Default to head curator on first use
    id = HEAD_CURATOR
    localStorage.setItem('curator_id', id)
  }
  return id
}

/** Set curator name programmatically */
export function setCuratorId(name: string) {
  localStorage.setItem('curator_id', name.trim())
}

/** Get the current session ID (unique per browser session) */
export function getSessionId(): string {
  return SESSION_ID
}

/* ─── Headers & Config ─── */

/** Common headers for all admin REST requests */
function adminHeaders(): HeadersInit {
  return {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY,
  }
}

/** Check if admin client is properly configured */
export function isAdminConfigured(): boolean {
  return !!(ENDPOINT && PROJECT_ID && API_KEY)
}

/* ─── Audit Log ─── */

export interface AuditEntry {
  entityId: string
  entitySlug: string
  entityName?: string
  action: 'update' | 'delete' | 'create' | 'batch_update'
  field?: string
  oldValue?: string
  newValue?: string
  editorNote?: string
}

/**
 * Create an audit log entry in the audit_log collection.
 * Fire-and-forget — does not block the main write operation.
 */
async function createAuditEntry(entry: AuditEntry): Promise<void> {
  if (!isAdminConfigured()) return

  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/audit_log/documents`
  const docId = crypto.randomUUID().replace(/-/g, '').slice(0, 20)

  try {
    await fetch(url, {
      method: 'POST',
      headers: adminHeaders(),
      body: JSON.stringify({
        documentId: docId,
        data: {
          entityId: entry.entityId,
          entitySlug: entry.entitySlug,
          entityName: entry.entityName ?? '',
          action: entry.action,
          field: entry.field ?? '',
          oldValue: (entry.oldValue ?? '').slice(0, 9999),
          newValue: (entry.newValue ?? '').slice(0, 9999),
          editorId: getCuratorId(),
          editorNote: entry.editorNote ?? '',
          timestamp: new Date().toISOString(),
          sessionId: SESSION_ID,
        },
      }),
    })
  } catch (err) {
    console.warn('Audit log write failed (non-blocking):', err)
  }
}

/**
 * Log all changed fields between old and new data as individual audit entries.
 * Returns a promise that resolves when all entries are written.
 */
export async function logFieldChanges(
  entityId: string,
  entitySlug: string,
  entityName: string,
  oldData: Record<string, unknown>,
  newData: Record<string, unknown>,
  editorNote?: string,
): Promise<void> {
  const entries: AuditEntry[] = []

  for (const [key, newVal] of Object.entries(newData)) {
    const oldVal = oldData[key]
    const oldStr = oldVal == null ? '' : String(oldVal)
    const newStr = newVal == null ? '' : String(newVal)

    if (oldStr !== newStr) {
      entries.push({
        entityId,
        entitySlug,
        entityName,
        action: 'update',
        field: key,
        oldValue: oldStr,
        newValue: newStr,
        editorNote,
      })
    }
  }

  // Fire all audit entries (non-blocking, parallel)
  await Promise.allSettled(entries.map(createAuditEntry))
}

/**
 * Update a single document via Appwrite REST API.
 * Uses PATCH endpoint with API key auth.
 * Optionally logs changes to the audit trail.
 */
export async function adminUpdateDocument(
  collectionId: string,
  documentId: string,
  data: Record<string, unknown>,
  auditMeta?: { slug: string; name: string; oldData?: Record<string, unknown> },
): Promise<{ success: boolean; error?: string }> {
  if (!isAdminConfigured()) {
    return { success: false, error: 'Admin client not configured — check VITE_APPWRITE_API_KEY' }
  }

  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents/${documentId}`
  try {
    const res = await fetch(url, {
      method: 'PATCH',
      headers: adminHeaders(),
      body: JSON.stringify({ data }),
    })

    if (!res.ok) {
      const body = await res.json().catch(() => ({ message: res.statusText }))
      return { success: false, error: body.message || `HTTP ${res.status}` }
    }

    // Log audit trail (non-blocking) if entity metadata provided
    if (auditMeta && collectionId === 'entities') {
      logFieldChanges(
        documentId,
        auditMeta.slug,
        auditMeta.name,
        auditMeta.oldData ?? {},
        data,
      ).catch(() => {})  // swallow — audit failure should not fail the save
    }

    return { success: true }
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Network error' }
  }
}

/**
 * Delete a document via Appwrite REST API.
 */
export async function adminDeleteDocument(
  collectionId: string,
  documentId: string,
): Promise<{ success: boolean; error?: string }> {
  if (!isAdminConfigured()) {
    return { success: false, error: 'Admin client not configured — check VITE_APPWRITE_API_KEY' }
  }

  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents/${documentId}`
  try {
    const res = await fetch(url, {
      method: 'DELETE',
      headers: adminHeaders(),
    })

    if (!res.ok) {
      const body = await res.json().catch(() => ({ message: res.statusText }))
      return { success: false, error: body.message || `HTTP ${res.status}` }
    }

    return { success: true }
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Network error' }
  }
}

/**
 * Batch update documents — chunked at 10/batch with delays.
 */
export async function adminBatchUpdate(
  collectionId: string,
  updates: Array<{ documentId: string; data: Record<string, unknown> }>,
  onProgress?: (done: number, total: number) => void,
): Promise<{ success: number; failed: number; errors: string[] }> {
  let success = 0, failed = 0
  const errors: string[] = []
  const BATCH_SIZE = 10

  for (let i = 0; i < updates.length; i += BATCH_SIZE) {
    const batch = updates.slice(i, i + BATCH_SIZE)
    const results = await Promise.allSettled(
      batch.map(({ documentId, data }) =>
        adminUpdateDocument(collectionId, documentId, data),
      ),
    )

    for (const r of results) {
      if (r.status === 'fulfilled' && r.value.success) {
        success++
      } else {
        failed++
        const msg = r.status === 'fulfilled' ? r.value.error : String(r.reason)
        if (msg) errors.push(msg)
      }
    }

    onProgress?.(Math.min(i + BATCH_SIZE, updates.length), updates.length)
    if (i + BATCH_SIZE < updates.length) {
      await new Promise((r) => setTimeout(r, 200))
    }
  }

  return { success, failed, errors }
}
