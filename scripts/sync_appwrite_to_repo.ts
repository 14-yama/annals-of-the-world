#!/usr/bin/env npx tsx
/**
 * sync_appwrite_to_repo.ts — Export all Appwrite entities to organised JSON files
 *
 * Creates a class-based folder structure under data/appwrite-export/:
 *   entities/{classCode}-{className}/{divisionCode}.json
 *   relationships.json
 *   evidence.json
 *   audit_log.json
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_appwrite_to_repo.ts
 *
 * Flags:
 *   --entities-only   Only export entities (skip relationships, evidence, etc.)
 *   --collection=X    Export only the named collection
 */

import * as fs from 'fs'
import * as path from 'path'

// ── Config ──
const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID || '66509ba7003618a05af6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const API_KEY     = process.env.APPWRITE_API_KEY

if (!API_KEY) {
  console.error('ERROR: Set APPWRITE_API_KEY env var')
  console.error('  APPWRITE_API_KEY=<key> npx tsx scripts/sync_appwrite_to_repo.ts')
  process.exit(1)
}

const ROOT = path.resolve(__dirname, '..')
const EXPORT_DIR = path.join(ROOT, 'data', 'appwrite-export')

// ── Class name map (matching callNumbers.ts) ──
const CLASS_NAMES: Record<string, string> = {
  '0': 'Ideas-Core',
  '1': 'Ideas-Other',
  '2': 'People',
  '3': 'Institutions',
  '4': 'Places',
  '5': 'Events',
  '6': 'Movements',
  '7': 'Artifacts-Texts',
  '8': 'Evidence',
  '9': 'Timeframes',
}

// ── REST API Helpers ──

function headers(): Record<string, string> {
  return {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY!,
  }
}

interface AppwriteListResponse {
  total: number
  documents: Record<string, unknown>[]
}

async function listDocuments(
  collectionId: string,
  queries: string[] = [],
): Promise<AppwriteListResponse> {
  const params = new URLSearchParams()
  for (const q of queries) params.append('queries[]', q)

  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents?${params}`
  const res = await fetch(url, { headers: headers() })
  if (!res.ok) {
    const body = await res.text()
    throw new Error(`List ${collectionId} failed: ${res.status} ${body}`)
  }
  return res.json() as Promise<AppwriteListResponse>
}

/**
 * Paginate through all documents in a collection using cursor-based pagination.
 */
async function paginateAll(
  collectionId: string,
  extraQueries: string[] = [],
): Promise<Record<string, unknown>[]> {
  const PAGE = 5000
  const all: Record<string, unknown>[] = []
  let cursor: string | undefined

  while (true) {
    const queries = [
      ...extraQueries,
      JSON.stringify({ method: 'limit', values: [PAGE] }),
    ]
    if (cursor) {
      queries.push(JSON.stringify({ method: 'cursorAfter', values: [cursor] }))
    }

    const res = await listDocuments(collectionId, queries)
    all.push(...res.documents)

    if (res.documents.length < PAGE) break
    cursor = res.documents[res.documents.length - 1].$id as string

    if (all.length % 5000 === 0) {
      process.stdout.write(`  ${collectionId}: ${all.length} docs...\r`)
    }
  }

  return all
}

function ensureDir(dir: string) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true })
}

function writeJson(filePath: string, data: unknown) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + '\n')
}

// ── Main ──

async function main() {
  const args = process.argv.slice(2)
  const entitiesOnly = args.includes('--entities-only')
  const collectionFlag = args.find(a => a.startsWith('--collection='))
  const singleCollection = collectionFlag?.split('=')[1]

  console.log('=== Appwrite → Repo Sync ===')
  console.log(`Endpoint:  ${ENDPOINT}`)
  console.log(`Database:  ${DATABASE_ID}`)
  console.log(`Output:    ${EXPORT_DIR}`)
  console.log()

  ensureDir(EXPORT_DIR)

  const timestamp = new Date().toISOString()
  const summary: Record<string, number> = {}

  // ─── Export Entities ───
  if (!singleCollection || singleCollection === 'entities') {
    console.log('Exporting entities...')
    const allEntities = await paginateAll('entities')
    console.log(`  Fetched ${allEntities.length} entities`)

    // Group by class code
    const byClass: Record<string, Record<string, Record<string, unknown>[]>> = {}

    for (const doc of allEntities) {
      const callNumber = (doc.callNumber as string) || '9.999.unknown'
      const parts = callNumber.split('.')
      const classCode = parts[0] || '9'
      const divCode = parts.length >= 2 ? `${parts[0]}${parts[1]}` : `${classCode}00`

      if (!byClass[classCode]) byClass[classCode] = {}
      if (!byClass[classCode][divCode]) byClass[classCode][divCode] = []

      // Strip Appwrite internal fields
      const clean = { ...doc }
      delete clean.$databaseId
      delete clean.$collectionId
      delete clean.$permissions
      byClass[classCode][divCode].push(clean)
    }

    // Write per-class/division files
    const entitiesDir = path.join(EXPORT_DIR, 'entities')
    ensureDir(entitiesDir)

    for (const [classCode, divisions] of Object.entries(byClass)) {
      const className = CLASS_NAMES[classCode] || `Class-${classCode}`
      const classDir = path.join(entitiesDir, `${classCode}-${className}`)
      ensureDir(classDir)

      for (const [divCode, docs] of Object.entries(divisions)) {
        writeJson(path.join(classDir, `${divCode}.json`), {
          _meta: { classCode, divisionCode: divCode, count: docs.length, exportedAt: timestamp },
          entities: docs,
        })
      }

      const classTotal = Object.values(divisions).reduce((s, d) => s + d.length, 0)
      console.log(`  Class ${classCode} (${className}): ${classTotal} entities, ${Object.keys(divisions).length} divisions`)
    }

    summary.entities = allEntities.length
  }

  // ─── Export Other Collections ───
  const otherCollections = ['relationships', 'evidence', 'media', 'timeline_entries', 'audit_log']

  if (!entitiesOnly) {
    for (const colId of otherCollections) {
      if (singleCollection && singleCollection !== colId) continue

      console.log(`Exporting ${colId}...`)
      try {
        const docs = await paginateAll(colId)
        const cleaned = docs.map(d => {
          const c = { ...d }
          delete c.$databaseId
          delete c.$collectionId
          delete c.$permissions
          return c
        })

        writeJson(path.join(EXPORT_DIR, `${colId}.json`), {
          _meta: { collection: colId, count: cleaned.length, exportedAt: timestamp },
          documents: cleaned,
        })

        console.log(`  ${colId}: ${cleaned.length} documents`)
        summary[colId] = cleaned.length
      } catch (err) {
        console.error(`  ${colId}: ERROR — ${(err as Error).message}`)
        summary[colId] = 0
      }
    }
  }

  // Write manifest
  writeJson(path.join(EXPORT_DIR, 'manifest.json'), {
    exportedAt: timestamp,
    databaseId: DATABASE_ID,
    projectId: PROJECT_ID,
    summary,
  })

  console.log()
  console.log('=== Export Complete ===')
  const totalDocs = Object.values(summary).reduce((a, b) => a + b, 0)
  console.log(`Total: ${totalDocs} documents exported to ${EXPORT_DIR}`)
}

main().catch((err) => {
  console.error('Sync failed:', err.message || err)
  process.exit(1)
})
