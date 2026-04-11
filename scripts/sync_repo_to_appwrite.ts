#!/usr/bin/env npx tsx
/**
 * sync_repo_to_appwrite.ts — Restore/seed Appwrite from exported JSON files
 *
 * Reads from data/appwrite-export/ and upserts documents into Appwrite.
 * Uses slug-based deduplication: if a document with the same slug exists,
 * it updates; otherwise it creates.
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts
 *
 * Flags:
 *   --dry-run          Preview what would be imported without writing
 *   --collection=X     Import only the named collection
 *   --force            Overwrite existing entities (default: skip existing)
 */

import * as fs from 'fs'
import * as path from 'path'
import * as crypto from 'crypto'

// ── Config ──
const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID || '69cc45e3000d587ea5e6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_db'
const API_KEY     = process.env.APPWRITE_API_KEY

if (!API_KEY) {
  console.error('ERROR: Set APPWRITE_API_KEY env var')
  process.exit(1)
}

const ROOT = path.resolve(__dirname, '..')
const EXPORT_DIR = path.join(ROOT, 'data', 'appwrite-export')

// ── REST API Helpers ──

function headers(): Record<string, string> {
  return {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY!,
  }
}

function slugToId(slug: string): string {
  return crypto.createHash('sha256').update(slug).digest('hex').slice(0, 20)
}

async function createDocument(
  collectionId: string,
  documentId: string,
  data: Record<string, unknown>,
): Promise<{ success: boolean; error?: string }> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents`
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: headers(),
      body: JSON.stringify({ documentId, data }),
    })
    if (!res.ok) {
      const body = await res.json().catch(() => ({ message: res.statusText }))
      return { success: false, error: body.message || `HTTP ${res.status}` }
    }
    return { success: true }
  } catch (err) {
    return { success: false, error: (err as Error).message }
  }
}

async function updateDocument(
  collectionId: string,
  documentId: string,
  data: Record<string, unknown>,
): Promise<{ success: boolean; error?: string }> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents/${documentId}`
  try {
    const res = await fetch(url, {
      method: 'PATCH',
      headers: headers(),
      body: JSON.stringify({ data }),
    })
    if (!res.ok) {
      const body = await res.json().catch(() => ({ message: res.statusText }))
      return { success: false, error: body.message || `HTTP ${res.status}` }
    }
    return { success: true }
  } catch (err) {
    return { success: false, error: (err as Error).message }
  }
}

async function getDocument(
  collectionId: string,
  documentId: string,
): Promise<Record<string, unknown> | null> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents/${documentId}`
  try {
    const res = await fetch(url, { headers: headers() })
    if (res.status === 404) return null
    if (!res.ok) return null
    return res.json()
  } catch {
    return null
  }
}

function readJsonFile(filePath: string): { documents?: Record<string, unknown>[]; entities?: Record<string, unknown>[] } {
  const raw = fs.readFileSync(filePath, 'utf-8')
  return JSON.parse(raw)
}

// ── Main ──

async function main() {
  const args = process.argv.slice(2)
  const dryRun = args.includes('--dry-run')
  const force = args.includes('--force')
  const collectionFlag = args.find(a => a.startsWith('--collection='))
  const singleCollection = collectionFlag?.split('=')[1]

  console.log('=== Repo → Appwrite Sync ===')
  console.log(`Endpoint:  ${ENDPOINT}`)
  console.log(`Database:  ${DATABASE_ID}`)
  console.log(`Source:    ${EXPORT_DIR}`)
  if (dryRun) console.log('MODE:      DRY RUN (no writes)')
  if (force) console.log('MODE:      FORCE (overwrite existing)')
  console.log()

  if (!fs.existsSync(EXPORT_DIR)) {
    console.error(`Export directory not found: ${EXPORT_DIR}`)
    console.error('Run sync_appwrite_to_repo.ts first to create the export.')
    process.exit(1)
  }

  let created = 0, updated = 0, skipped = 0, failed = 0

  // ─── Import Entities ───
  if (!singleCollection || singleCollection === 'entities') {
    const entitiesDir = path.join(EXPORT_DIR, 'entities')
    if (fs.existsSync(entitiesDir)) {
      console.log('Importing entities...')

      const classDirs = fs.readdirSync(entitiesDir).filter(d =>
        fs.statSync(path.join(entitiesDir, d)).isDirectory()
      )

      for (const classDir of classDirs) {
        const divFiles = fs.readdirSync(path.join(entitiesDir, classDir))
          .filter(f => f.endsWith('.json'))

        for (const divFile of divFiles) {
          const data = readJsonFile(path.join(entitiesDir, classDir, divFile))
          const entities = data.entities || data.documents || []

          for (const entity of entities) {
            const slug = entity.slug as string
            if (!slug) { failed++; continue }

            const docId = (entity.$id as string) || slugToId(slug)

            // Strip Appwrite metadata from the data payload
            const payload = { ...entity }
            delete payload.$id
            delete payload.$createdAt
            delete payload.$updatedAt
            delete payload.$databaseId
            delete payload.$collectionId
            delete payload.$permissions

            if (dryRun) {
              console.log(`  [DRY] Would upsert: ${slug} (${docId})`)
              created++
              continue
            }

            // Check if exists
            const existing = await getDocument('entities', docId)

            if (existing) {
              if (force) {
                const result = await updateDocument('entities', docId, payload)
                if (result.success) { updated++ } else { failed++ }
              } else {
                skipped++
              }
            } else {
              const result = await createDocument('entities', docId, payload)
              if (result.success) { created++ } else { failed++ }
            }

            const total = created + updated + skipped + failed
            if (total % 100 === 0) {
              process.stdout.write(`  Progress: ${total} (created=${created}, updated=${updated}, skipped=${skipped}, failed=${failed})\r`)
            }

            // Rate limit: 50ms between writes
            if (!dryRun && (created + updated) % 10 === 0) {
              await new Promise(r => setTimeout(r, 200))
            }
          }
        }

        console.log(`  ${classDir}: done`)
      }
    }
  }

  // ─── Import Other Collections ───
  const otherCollections = ['relationships', 'evidence', 'media', 'timeline_entries', 'audit_log']

  for (const colId of otherCollections) {
    if (singleCollection && singleCollection !== colId) continue

    const filePath = path.join(EXPORT_DIR, `${colId}.json`)
    if (!fs.existsSync(filePath)) continue

    console.log(`Importing ${colId}...`)
    const data = readJsonFile(filePath)
    const docs = data.documents || []

    for (const doc of docs) {
      const docId = doc.$id as string
      if (!docId) { failed++; continue }

      const payload = { ...doc }
      delete payload.$id
      delete payload.$createdAt
      delete payload.$updatedAt
      delete payload.$databaseId
      delete payload.$collectionId
      delete payload.$permissions

      if (dryRun) {
        created++
        continue
      }

      const existing = await getDocument(colId, docId)
      if (existing && !force) {
        skipped++
      } else if (existing) {
        const result = await updateDocument(colId, docId, payload)
        if (result.success) { updated++ } else { failed++ }
      } else {
        const result = await createDocument(colId, docId, payload)
        if (result.success) { created++ } else { failed++ }
      }

      const total = created + updated + skipped + failed
      if (total % 100 === 0) {
        process.stdout.write(`  ${colId}: ${total} processed\r`)
      }

      if (!dryRun && (created + updated) % 10 === 0) {
        await new Promise(r => setTimeout(r, 200))
      }
    }

    console.log(`  ${colId}: ${docs.length} documents processed`)
  }

  console.log()
  console.log('=== Import Complete ===')
  console.log(`Created: ${created}`)
  console.log(`Updated: ${updated}`)
  console.log(`Skipped: ${skipped}`)
  console.log(`Failed:  ${failed}`)
}

main().catch((err) => {
  console.error('Import failed:', err.message || err)
  process.exit(1)
})
