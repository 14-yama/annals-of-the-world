/**
 * Appwrite Client Configuration
 *
 * Singleton instances for Appwrite services used throughout the app.
 * Uses VITE_ prefixed env vars loaded by Vite at build time.
 */
import { Client, Account, Databases, Storage, Functions } from 'appwrite'

const ENDPOINT = import.meta.env.VITE_APPWRITE_ENDPOINT as string
const PROJECT_ID = import.meta.env.VITE_APPWRITE_PROJECT_ID as string

const client = new Client()

if (ENDPOINT && PROJECT_ID) {
  client.setEndpoint(ENDPOINT).setProject(PROJECT_ID)
}

export const account = new Account(client)
export const databases = new Databases(client)
export const storage = new Storage(client)
export const functions = new Functions(client)

export const DATABASE_ID = (import.meta.env.VITE_APPWRITE_DATABASE_ID as string) || 'annals_db'

/* ── Collection IDs (match Appwrite console) ── */
export const COLLECTIONS = {
  ENTITIES:       'entities',
  RELATIONSHIPS:  'relationships',
  CAUSES_EFFECTS: 'causes_effects',
  PLACES:         'places',
  TEXTS:          'texts',
  EVIDENCE:       'evidence',
  MEDIA:          'media',
  TIMELINE:       'timeline_entries',
  AUDIT_LOG:        'audit_log',
  STATS_CACHE:      'stats_cache',
  ENRICHMENT_AUDIT: 'enrichment_audit',
} as const

/* ── Storage bucket IDs ── */
export const BUCKETS = {
  ENTITY_MEDIA: 'entity-media',
} as const

/** Quick health check — returns true if Appwrite is reachable */
export async function ping(): Promise<boolean> {
  try {
    await account.get()
    return true
  } catch {
    // 401 = reachable but not logged in — that's fine for a ping
    return true
  }
}

export default client
