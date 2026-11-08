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
 *   --max=N            Stop after N entity create/skip attempts (staged)
 *   --source=DIR       Read from DIR instead of data/appwrite-export
 *   --fast             Local bulk mode: create-first (409=skip), no audit, tiny delay
 *   --cursor-file=PATH Persist scan progress so staged --max runs advance (default: data/governance/seed_local_cursor.json when --max set)
 *   --reset-cursor     Ignore/reset cursor file
 */

import * as fs from 'fs'
import * as path from 'path'
import * as crypto from 'crypto'

// ── Config ──
const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID || '66509ba7003618a05af6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const API_KEY     = process.env.APPWRITE_API_KEY
const SYNC_EDITOR = process.env.SYNC_EDITOR_ID || 'repo-sync-manual'

if (!API_KEY) {
  console.error('ERROR: Set APPWRITE_API_KEY env var')
  process.exit(1)
}

const ROOT = path.resolve(__dirname, '..')
const argvEarly = process.argv.slice(2)
const sourceFlag = argvEarly.find(a => a.startsWith('--source='))
const EXPORT_DIR = sourceFlag
  ? path.resolve(ROOT, sourceFlag.slice('--source='.length))
  : path.join(ROOT, 'data', 'appwrite-export')

type SeedCursor = {
  source: string
  classDir: string
  file: string
  entityOffset: number
  scanned: number
  created: number
  skipped: number
  failed: number
  poisonSkipped?: number
  lastRunAt?: string
  lastPoison?: { path: string; reason: string; at: string }
}

const CONFLICT_MARKERS = ['<<<<<<<', '=======', '>>>>>>>'] as const

function hasConflictMarkers(raw: string): boolean {
  return CONFLICT_MARKERS.some((m) => raw.includes(m))
}

/** Newest side-path cloud backup under data/backups/cloud-* (if any). */
function resolveBackupRoot(): string | null {
  const envBackup = process.env.ANNALS_CLOUD_BACKUP_DIR
  if (envBackup) {
    const abs = path.resolve(ROOT, envBackup)
    if (fs.existsSync(abs)) return abs
  }
  const backupsRoot = path.join(ROOT, 'data', 'backups')
  if (!fs.existsSync(backupsRoot)) return null
  const dirs = fs
    .readdirSync(backupsRoot)
    .filter((d) => d.startsWith('cloud-'))
    .map((d) => path.join(backupsRoot, d))
    .filter((d) => fs.statSync(d).isDirectory())
    .sort()
  return dirs.length ? dirs[dirs.length - 1] : null
}

function tryRecoverFromBackup(relFromExport: string): string | null {
  const backupRoot = resolveBackupRoot()
  if (!backupRoot) return null
  // relFromExport like entities/205-Class-205/205nicander.json
  const candidate = path.join(backupRoot, relFromExport)
  if (!fs.existsSync(candidate)) return null
  try {
    const raw = fs.readFileSync(candidate, 'utf-8')
    if (hasConflictMarkers(raw)) return null
    JSON.parse(raw)
    return candidate
  } catch {
    return null
  }
}

type LoadJsonResult =
  | { ok: true; data: { documents?: Record<string, unknown>[]; entities?: Record<string, unknown>[] }; recoveredFrom?: string }
  | { ok: false; reason: string; recoveredAttempted?: boolean }

function loadEntityExportFile(filePath: string): LoadJsonResult {
  const rel = path.relative(EXPORT_DIR, filePath).split(path.sep).join('/')
  let raw: string
  try {
    raw = fs.readFileSync(filePath, 'utf-8')
  } catch (err) {
    return { ok: false, reason: `unreadable: ${(err as Error).message}` }
  }

  const tryParse = (text: string, label: string): LoadJsonResult => {
    if (hasConflictMarkers(text)) {
      return { ok: false, reason: `git conflict markers (${label})` }
    }
    try {
      const data = JSON.parse(text) as {
        documents?: Record<string, unknown>[]
        entities?: Record<string, unknown>[]
      }
      return { ok: true, data }
    } catch (err) {
      return { ok: false, reason: `invalid JSON (${label}): ${(err as Error).message}` }
    }
  }

  const primary = tryParse(raw, 'export')
  if (primary.ok) return primary

  // Auto-recover from side-path backup when export is poisoned
  const backupPath = tryRecoverFromBackup(rel)
  if (backupPath) {
    try {
      const backupRaw = fs.readFileSync(backupPath, 'utf-8')
      const recovered = tryParse(backupRaw, 'backup')
      if (recovered.ok) {
        fs.copyFileSync(backupPath, filePath)
        console.warn(`  [recover] restored ${rel} from ${path.relative(ROOT, backupPath)}`)
        return { ...recovered, recoveredFrom: backupPath }
      }
    } catch (err) {
      return {
        ok: false,
        reason: `${primary.reason}; backup restore failed: ${(err as Error).message}`,
        recoveredAttempted: true,
      }
    }
  }

  return { ...primary, recoveredAttempted: Boolean(resolveBackupRoot()) }
}

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

/** Attributes allowed by scripts/setup_appwrite.ts entities collection */
const ENTITY_ATTRS = new Set([
  'slug', 'name', 'label', 'callNumber', 'summary', 'era', 'eraSlug', 'region',
  'continent', 'status', 'born', 'died', 'founded', 'period', 'startDate', 'endDate',
  'subjectHeadings', 'subjects', 'frameworks', 'altNames', 'wikidataQid', 'wikipediaUrl',
  'imageUrl', 'importanceScore', 'detailsJson',
])

function sanitizeEntityPayload(entity: Record<string, unknown>): Record<string, unknown> {
  const payload: Record<string, unknown> = {}
  for (const [k, v] of Object.entries(entity)) {
    if (k.startsWith('$') || k.startsWith('_')) continue
    if (!ENTITY_ATTRS.has(k)) continue
    if (v === undefined) continue
    payload[k] = v
  }
  // Local schema requires label; fall back to name/slug for sparse export rows.
  if (!payload.label) {
    payload.label = payload.name || payload.slug || 'untitled'
  }
  if (!payload.name && payload.label) {
    payload.name = payload.label
  }
  return payload
}

async function createDocument(
  collectionId: string,
  documentId: string,
  data: Record<string, unknown>,
): Promise<{ success: boolean; conflict?: boolean; error?: string }> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collectionId}/documents`
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: headers(),
      body: JSON.stringify({
        documentId,
        data,
        // Guest-readable so Vite UI can fetch without a user session
        permissions: ['read("any")', 'update("users")', 'delete("users")'],
      }),
    })
    if (res.status === 409) {
      return { success: false, conflict: true, error: 'Document already exists' }
    }
    if (!res.ok) {
      const body = await res.json().catch(() => ({ message: res.statusText }))
      const message = (body as { message?: string }).message || `HTTP ${res.status}`
      // Some Appwrite builds return 409 text without status 409
      if (res.status === 409 || /already exists|document_already_exists/i.test(message)) {
        return { success: false, conflict: true, error: message }
      }
      return { success: false, error: message }
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
  if (hasConflictMarkers(raw)) {
    throw new Error(`git conflict markers in ${filePath}`)
  }
  return JSON.parse(raw)
}

async function writeAuditEntry(
  action: string,
  entity: Record<string, unknown>,
  editorId: string,
  note: string,
): Promise<void> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/audit_log/documents`
  try {
    await fetch(url, {
      method: 'POST',
      headers: headers(),
      body: JSON.stringify({
        documentId: crypto.randomUUID(),
        data: {
          entityId: (entity.$id as string) || '',
          entitySlug: (entity.slug as string) || '',
          entityName: (entity.name as string) || '',
          action,
          field: 'entity',
          oldValue: action === 'create' ? '' : '(sync overwrite)',
          newValue: ((entity.summary as string) || '').slice(0, 500),
          editorId,
          editorNote: note,
          timestamp: new Date().toISOString(),
          sessionId: `repo-sync-${Date.now()}`,
        },
      }),
    })
  } catch {
    // Non-fatal — sync continues
  }
}

// ── Main ──

async function main() {
  const args = process.argv.slice(2)
  const dryRun = args.includes('--dry-run')
  const force = args.includes('--force')
  const fast = args.includes('--fast') || /localhost|127\.0\.0\.1/.test(ENDPOINT)
  const resetCursor = args.includes('--reset-cursor')
  const collectionFlag = args.find(a => a.startsWith('--collection='))
  const singleCollection = collectionFlag?.split('=')[1]
  const maxFlag = args.find(a => a.startsWith('--max='))
  const maxDocs = maxFlag ? Math.max(1, parseInt(maxFlag.split('=')[1] || '0', 10)) : 0
  const cursorFlag = args.find(a => a.startsWith('--cursor-file='))
  const cursorPath = cursorFlag
    ? path.resolve(ROOT, cursorFlag.slice('--cursor-file='.length))
    : (maxDocs ? path.join(ROOT, 'data', 'governance', 'seed_local_cursor.json') : '')

  console.log('=== Repo → Appwrite Sync ===')
  console.log(`Endpoint:  ${ENDPOINT}`)
  console.log(`Database:  ${DATABASE_ID}`)
  console.log(`Source:    ${EXPORT_DIR}`)
  if (dryRun) console.log('MODE:      DRY RUN (no writes)')
  if (force) console.log('MODE:      FORCE (overwrite existing)')
  if (fast) console.log('MODE:      FAST (create-first, no audit writes)')
  if (maxDocs) console.log(`MODE:      STAGED (max=${maxDocs} entity upserts)`)
  if (cursorPath) console.log(`Cursor:    ${cursorPath}`)
  console.log()

  if (!fs.existsSync(EXPORT_DIR)) {
    console.error(`Export directory not found: ${EXPORT_DIR}`)
    console.error('Run sync_appwrite_to_repo.ts first to create the export.')
    process.exit(1)
  }

  let created = 0, updated = 0, skipped = 0, failed = 0
  let poisonSkipped = 0
  let processedEntities = 0
  let hitMax = false
  let resumeClass = ''
  let resumeFile = ''
  let resumeEntityOffset = 0
  let cursorBase: SeedCursor | null = null
  let lastPoison: SeedCursor['lastPoison'] | undefined

  const backupRoot = resolveBackupRoot()
  if (backupRoot) {
    console.log(`Backup:   ${path.relative(ROOT, backupRoot)} (auto-recover enabled)`)
  }

  if (cursorPath && !resetCursor && fs.existsSync(cursorPath)) {
    try {
      const raw = JSON.parse(fs.readFileSync(cursorPath, 'utf8')) as SeedCursor
      if (raw.source === EXPORT_DIR) {
        resumeClass = raw.classDir || ''
        resumeFile = raw.file || ''
        resumeEntityOffset = Math.max(0, raw.entityOffset || 0)
        cursorBase = raw
        console.log(`Resuming after ${resumeClass}/${resumeFile} entityOffset=${resumeEntityOffset} (scanned=${raw.scanned || 0})`)
      } else {
        console.log('Cursor source mismatch — starting from beginning')
      }
    } catch {
      console.log('Cursor unreadable — starting from beginning')
    }
  }

  const writeCursor = (classDir: string, file: string, entityOffset: number) => {
    if (!cursorPath || dryRun) return
    const payload: SeedCursor = {
      source: EXPORT_DIR,
      classDir,
      file,
      entityOffset,
      scanned: (cursorBase?.scanned || 0) + processedEntities,
      created: (cursorBase?.created || 0) + created,
      skipped: (cursorBase?.skipped || 0) + skipped,
      failed: (cursorBase?.failed || 0) + failed,
      poisonSkipped: (cursorBase?.poisonSkipped || 0) + poisonSkipped,
      lastRunAt: new Date().toISOString(),
      ...(lastPoison ? { lastPoison } : {}),
    }
    fs.mkdirSync(path.dirname(cursorPath), { recursive: true })
    fs.writeFileSync(cursorPath, JSON.stringify(payload, null, 2) + '\n')
  }

  // ─── Import Entities ───
  if (!singleCollection || singleCollection === 'entities') {
    const entitiesDir = path.join(EXPORT_DIR, 'entities')
    if (fs.existsSync(entitiesDir)) {
      console.log('Importing entities...')

      const classDirs = fs.readdirSync(entitiesDir).filter(d =>
        fs.statSync(path.join(entitiesDir, d)).isDirectory()
      ).sort()

      for (const classDir of classDirs) {
        if (hitMax) break
        if (resumeClass && classDir < resumeClass) continue

        const divFiles = fs.readdirSync(path.join(entitiesDir, classDir))
          .filter(f => f.endsWith('.json'))
          .sort()

        for (const divFile of divFiles) {
          if (hitMax) break
          if (resumeClass === classDir && resumeFile && divFile < resumeFile) continue

          const filePath = path.join(entitiesDir, classDir, divFile)
          const loaded = loadEntityExportFile(filePath)
          if (!loaded.ok) {
            poisonSkipped++
            lastPoison = {
              path: path.relative(ROOT, filePath),
              reason: loaded.reason,
              at: new Date().toISOString(),
            }
            console.warn(`  [poison-skip] ${lastPoison.path}: ${loaded.reason}`)
            // Advance cursor past this file so KeepAlive seed does not abort/loop forever
            writeCursor(classDir, divFile, Number.MAX_SAFE_INTEGER)
            processedEntities++
            continue
          }
          const data = loaded.data
          const entities = data.entities || data.documents || []
          const startIdx =
            resumeClass === classDir && resumeFile === divFile ? resumeEntityOffset : 0

          for (let ei = startIdx; ei < entities.length; ei++) {
            if (maxDocs && processedEntities >= maxDocs) {
              hitMax = true
              writeCursor(classDir, divFile, ei)
              break
            }
            const entity = entities[ei]
            const slug = entity.slug as string
            if (!slug) { failed++; processedEntities++; continue }

            const docId = (entity.$id as string) || slugToId(slug)
            const payload = sanitizeEntityPayload(entity)

            processedEntities++

            if (dryRun) {
              console.log(`  [DRY] Would upsert: ${slug} (${docId})`)
              created++
              continue
            }

            if (fast && !force) {
              const result = await createDocument('entities', docId, payload)
              if (result.success) {
                created++
              } else if (result.conflict) {
                skipped++
              } else {
                // Fallback GET+create once on unexpected errors
                const existing = await getDocument('entities', docId)
                if (existing) {
                  skipped++
                } else {
                  const retry = await createDocument('entities', docId, payload)
                  if (retry.success) created++
                  else if (retry.conflict) skipped++
                  else failed++
                }
              }
            } else {
              const existing = await getDocument('entities', docId)
              if (existing) {
                if (force) {
                  const result = await updateDocument('entities', docId, payload)
                  if (result.success) {
                    updated++
                    if (!fast) {
                      await writeAuditEntry('batch_update', { ...payload, $id: docId }, SYNC_EDITOR, `Repo→Appwrite sync (force overwrite)`)
                    }
                  } else { failed++ }
                } else {
                  skipped++
                }
              } else {
                const result = await createDocument('entities', docId, payload)
                if (result.success) {
                  created++
                  if (!fast) {
                    await writeAuditEntry('create', { ...payload, $id: docId }, SYNC_EDITOR, `Repo→Appwrite sync (new entity)`)
                  }
                } else if (result.conflict) {
                  skipped++
                } else { failed++ }
              }
            }

            const total = created + updated + skipped + failed
            if (total % 100 === 0) {
              process.stdout.write(`  Progress: ${total} (created=${created}, updated=${updated}, skipped=${skipped}, failed=${failed})\r`)
            }

            if (!dryRun && (created + updated) % 25 === 0) {
              await new Promise(r => setTimeout(r, fast ? 20 : 200))
            }

            if (cursorPath && processedEntities % 250 === 0) {
              writeCursor(classDir, divFile, ei + 1)
            }
          }

          if (!hitMax) writeCursor(classDir, divFile, entities.length)
        }

        console.log(`  ${classDir}: done`)
      }
      if (hitMax) console.log(`  Stopped early at --max=${maxDocs}`)
    }
  }

  // ─── Import Other Collections ───
  const otherCollections = ['relationships', 'evidence', 'media', 'timeline_entries', 'audit_log']

  for (const colId of otherCollections) {
    if (singleCollection && singleCollection !== colId) continue

    const filePath = path.join(EXPORT_DIR, `${colId}.json`)
    if (!fs.existsSync(filePath)) continue

    console.log(`Importing ${colId}...`)
    let data: { documents?: Record<string, unknown>[]; entities?: Record<string, unknown>[] }
    try {
      data = readJsonFile(filePath)
    } catch (err) {
      poisonSkipped++
      lastPoison = {
        path: path.relative(ROOT, filePath),
        reason: (err as Error).message,
        at: new Date().toISOString(),
      }
      console.warn(`  [poison-skip] ${lastPoison.path}: ${lastPoison.reason}`)
      continue
    }
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
  console.log(`Poison:  ${poisonSkipped} (conflict/invalid JSON files skipped)`)
}

main().catch((err) => {
  // Unexpected fatal errors only — per-file poison is handled inline and must not kill seed
  console.error('Import failed:', err.message || err)
  process.exit(1)
})
