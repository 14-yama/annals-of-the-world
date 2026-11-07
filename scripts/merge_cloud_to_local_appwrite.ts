#!/usr/bin/env npx tsx
/**
 * merge_cloud_to_local_appwrite.ts
 *
 * One-way staged merge: Appwrite Cloud → local Docker Appwrite.
 * Policy: create-if-missing by $id. Never overwrite existing local docs.
 *
 * Env file: .env.cloud-merge (gitignored)
 *
 * Flags:
 *   --max=N          Max creates attempted this run (default 200)
 *   --dry-run
 *   --collection=    default entities
 *   --reset-cursor
 */
import * as fs from 'fs'
import * as path from 'path'
import { Client, Databases, Query, ID } from 'node-appwrite'

const ROOT = path.resolve(__dirname, '..')
const CURSOR_PATH = path.join(ROOT, 'data', 'governance', 'cloud_merge_cursor.json')

function loadDotEnvFile(filePath: string) {
  if (!fs.existsSync(filePath)) return
  for (const line of fs.readFileSync(filePath, 'utf8').split('\n')) {
    const trimmed = line.trim()
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue
    const eq = trimmed.indexOf('=')
    const key = trimmed.slice(0, eq).trim()
    const val = trimmed.slice(eq + 1).trim().replace(/^['"]|['"]$/g, '')
    if (key && !(key in process.env)) process.env[key] = val
  }
}

loadDotEnvFile(path.join(ROOT, '.env.cloud-merge'))
loadDotEnvFile(path.join(ROOT, '.env'))

const CLOUD = {
  endpoint: process.env.CLOUD_APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1',
  project: process.env.CLOUD_APPWRITE_PROJECT_ID || '66509ba7003618a05af6',
  database: process.env.CLOUD_APPWRITE_DATABASE_ID || 'annals_world_db',
  key: process.env.CLOUD_APPWRITE_API_KEY || '',
}

const LOCAL = {
  endpoint: process.env.LOCAL_APPWRITE_ENDPOINT || process.env.VITE_APPWRITE_ENDPOINT || 'http://localhost:8080/v1',
  project: process.env.LOCAL_APPWRITE_PROJECT_ID || process.env.VITE_APPWRITE_PROJECT_ID || 'annals-local',
  database: process.env.LOCAL_APPWRITE_DATABASE_ID || process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db',
  key: process.env.LOCAL_APPWRITE_API_KEY || process.env.APPWRITE_API_KEY || '',
}

const args = process.argv.slice(2)
const DRY = args.includes('--dry-run')
const RESET = args.includes('--reset-cursor')
const maxFlag = args.find(a => a.startsWith('--max='))
const MAX = maxFlag ? Math.max(1, parseInt(maxFlag.split('=')[1] || '200', 10)) : 200
const colFlag = args.find(a => a.startsWith('--collection='))
const COLLECTION = colFlag?.split('=')[1] || 'entities'
const PAGE = 25

if (!CLOUD.key) {
  console.error('ERROR: CLOUD_APPWRITE_API_KEY missing (use .env.cloud-merge)')
  process.exit(1)
}
if (!LOCAL.key) {
  console.error('ERROR: LOCAL_APPWRITE_API_KEY missing')
  process.exit(1)
}

type Cursor = {
  collection: string
  offset: number
  created: number
  skipped: number
  failed: number
  lastRunAt?: string
}

function readCursor(): Cursor {
  if (RESET || !fs.existsSync(CURSOR_PATH)) {
    return { collection: COLLECTION, offset: 0, created: 0, skipped: 0, failed: 0 }
  }
  try {
    const raw = JSON.parse(fs.readFileSync(CURSOR_PATH, 'utf8')) as Cursor
    if (raw.collection !== COLLECTION) {
      return { collection: COLLECTION, offset: 0, created: 0, skipped: 0, failed: 0 }
    }
    return raw
  } catch {
    return { collection: COLLECTION, offset: 0, created: 0, skipped: 0, failed: 0 }
  }
}

function writeCursor(c: Cursor) {
  fs.mkdirSync(path.dirname(CURSOR_PATH), { recursive: true })
  fs.writeFileSync(CURSOR_PATH, JSON.stringify({ ...c, lastRunAt: new Date().toISOString() }, null, 2))
}

const ENTITY_ATTRS = new Set([
  'slug', 'name', 'label', 'callNumber', 'summary', 'era', 'eraSlug', 'region',
  'continent', 'status', 'born', 'died', 'founded', 'period', 'startDate', 'endDate',
  'subjectHeadings', 'subjects', 'frameworks', 'altNames', 'wikidataQid', 'wikipediaUrl',
  'imageUrl', 'importanceScore', 'detailsJson',
])

const AUDIT_ATTRS = new Set([
  'entityId', 'entitySlug', 'entityName', 'action', 'field', 'oldValue', 'newValue',
  'editorId', 'editorNote', 'timestamp', 'sessionId',
])

const COLLECTION_ATTRS: Record<string, Set<string>> = {
  entities: ENTITY_ATTRS,
  audit_log: AUDIT_ATTRS,
}

function sanitizePayload(doc: Record<string, unknown>): Record<string, unknown> {
  const allowed = COLLECTION_ATTRS[COLLECTION]
  const payload: Record<string, unknown> = {}
  for (const [k, v] of Object.entries(doc)) {
    if (k.startsWith('$') || k.startsWith('_')) continue
    if (allowed && !allowed.has(k)) continue
    if (v === undefined || v === null) continue
    payload[k] = v
  }
  if (COLLECTION === 'entities' && typeof payload.detailsJson === 'string') {
    try {
      const dj = JSON.parse(payload.detailsJson)
      if (dj && typeof dj === 'object' && !dj._mergedFrom) {
        dj._mergedFrom = 'cloud'
        payload.detailsJson = JSON.stringify(dj)
      }
    } catch {
      /* leave */
    }
  }
  if (COLLECTION === 'audit_log') {
    // Ensure curator UI can badge historical cloud rows even when editorId is plain.
    const note = String(payload.editorNote || '')
    if (!note.includes('cloud-merged')) {
      payload.editorNote = note ? `${note} · cloud-merged` : 'cloud-merged'
    }
    const editor = String(payload.editorId || '')
    if (editor && !editor.includes('·cloud·') && !editor.includes('GH#')) {
      // Soft marker — EditorBadge already treats ·cloud· / GH# as CLOUD
      if (!editor.includes('cloud')) {
        payload.editorId = `${editor}·cloud·merged`
      }
    }
    // Truncate to local attribute sizes (oldValue/newValue capped at 4000 on local Docker)
    if (typeof payload.editorId === 'string') payload.editorId = payload.editorId.slice(0, 128)
    if (typeof payload.editorNote === 'string') payload.editorNote = payload.editorNote.slice(0, 1000)
    if (typeof payload.oldValue === 'string') payload.oldValue = payload.oldValue.slice(0, 4000)
    if (typeof payload.newValue === 'string') payload.newValue = payload.newValue.slice(0, 4000)
    if (typeof payload.sessionId === 'string') payload.sessionId = payload.sessionId.slice(0, 128)
  }
  return payload
}

function clientFor(cfg: typeof CLOUD) {
  return new Client().setEndpoint(cfg.endpoint).setProject(cfg.project).setKey(cfg.key)
}

async function main() {
  console.log('=== Cloud → Local merge (create-if-missing) ===')
  console.log(`Cloud:  ${CLOUD.endpoint} / ${CLOUD.project} / ${CLOUD.database}`)
  console.log(`Local:  ${LOCAL.endpoint} / ${LOCAL.project} / ${LOCAL.database}`)
  console.log(`Collection: ${COLLECTION}  max=${MAX}${DRY ? '  DRY-RUN' : ''}`)

  const cloudDb = new Databases(clientFor(CLOUD))
  const localDb = new Databases(clientFor(LOCAL))

  const cursor = readCursor()
  let offset = cursor.offset || 0
  let created = 0
  let skipped = 0
  let failed = 0
  let scanned = 0

  while (created + skipped + failed < MAX) {
    const page = await cloudDb.listDocuments(CLOUD.database, COLLECTION, [
      Query.limit(PAGE),
      Query.offset(offset),
    ])
    const docs = page.documents || []
    if (docs.length === 0) {
      console.log('No more cloud documents at this offset; resetting offset to 0 for next pass.')
      offset = 0
      break
    }

    for (const doc of docs) {
      if (created + skipped + failed >= MAX) break
      scanned++
      const docId = String(doc.$id || '')
      if (!docId) {
        failed++
        continue
      }

      let existing: Record<string, unknown> | null = null
      try {
        existing = await localDb.getDocument(LOCAL.database, COLLECTION, docId) as unknown as Record<string, unknown>
      } catch {
        existing = null
      }

      if (existing) {
        skipped++
        continue
      }

      const payload = sanitizePayload(doc as unknown as Record<string, unknown>)
      if (DRY) {
        created++
        continue
      }

      try {
        await localDb.createDocument(
          LOCAL.database,
          COLLECTION,
          docId || ID.unique(),
          payload,
          ['read("any")', 'update("users")', 'delete("users")'],
        )
        created++
      } catch (err) {
        failed++
        console.warn(`  fail ${docId}: ${(err as Error).message}`)
      }

      if ((created + skipped + failed) % 25 === 0) {
        process.stdout.write(`  progress created=${created} skipped=${skipped} failed=${failed} offset=${offset}\r`)
      }
      await new Promise(r => setTimeout(r, 40))
    }

    offset += docs.length
    if (docs.length < PAGE) break
  }

  const next: Cursor = {
    collection: COLLECTION,
    offset,
    created: (cursor.created || 0) + created,
    skipped: (cursor.skipped || 0) + skipped,
    failed: (cursor.failed || 0) + failed,
  }
  if (!DRY) writeCursor(next)

  console.log()
  console.log('=== Merge batch complete ===')
  console.log(`Scanned this run: ${scanned}`)
  console.log(`Created: ${created}`)
  console.log(`Skipped (already local): ${skipped}`)
  console.log(`Failed: ${failed}`)
  console.log(`Next offset: ${offset}`)
  console.log(`Cursor totals: created=${next.created} skipped=${next.skipped} failed=${next.failed}`)
}

main().catch(err => {
  console.error('Merge failed:', err.message || err)
  process.exit(1)
})
