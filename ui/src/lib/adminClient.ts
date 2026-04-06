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

/**
 * Update a single document via Appwrite REST API.
 * Uses PATCH endpoint with API key auth.
 */
export async function adminUpdateDocument(
  collectionId: string,
  documentId: string,
  data: Record<string, unknown>,
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
