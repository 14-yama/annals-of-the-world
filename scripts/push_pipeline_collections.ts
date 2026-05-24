#!/usr/bin/env node
/**
 * push_pipeline_collections.ts
 *
 * Creates (or updates) two Appwrite collections for the pipeline:
 *   - entities_clean    : promoted, validated entities
 *   - entities_rejected : entities that failed any gate
 *
 * Also syncs existing data/pipeline/clean/**\/*.json rows to entities_clean,
 * and data/pipeline/rejected/**\/*.json rows to entities_rejected.
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/push_pipeline_collections.ts
 *   # or:
 *   env $(cat .env | grep -v '^#' | xargs) npx tsx scripts/push_pipeline_collections.ts [--dry-run]
 *
 * Flags:
 *   --dry-run   Print what would be upserted without writing to Appwrite
 *   --schema    Create/verify collections only; skip document sync
 */
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const ROOT = path.resolve(__dirname, '..')

const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT    || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID  || '66509ba7003618a05af6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const API_KEY     = process.env.APPWRITE_API_KEY

const DRY_RUN   = process.argv.includes('--dry-run')
const SCHEMA_ONLY = process.argv.includes('--schema')

const CLEAN_DIR    = path.join(ROOT, 'data', 'pipeline', 'clean')
const REJECTED_DIR = path.join(ROOT, 'data', 'pipeline', 'rejected')

if (!API_KEY) { console.error('ERROR: APPWRITE_API_KEY not set'); process.exit(1) }

function ah(): Record<string, string> {
  return {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY!,
  }
}

async function apiFetch(method: string, url: string, body?: unknown): Promise<unknown> {
  const res = await fetch(url, {
    method, headers: ah(),
    body: body ? JSON.stringify(body) : undefined,
  })
  const text = await res.text()
  if (!res.ok) throw new Error(`${method} ${url} → ${res.status}: ${text.slice(0, 400)}`)
  return JSON.parse(text)
}

async function collectionExists(id: string): Promise<boolean> {
  try {
    await apiFetch('GET', `${ENDPOINT}/databases/${DATABASE_ID}/collections/${id}`)
    return true
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e)
    if (msg.includes('404') || msg.includes('not found')) return false
    throw e
  }
}

async function createStringAttr(collId: string, key: string, size: number): Promise<void> {
  await apiFetch('POST',
    `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/attributes/string`,
    { key, size, required: false, default: null })
  await new Promise(r => setTimeout(r, 300))
}

async function createIntAttr(collId: string, key: string): Promise<void> {
  await apiFetch('POST',
    `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/attributes/integer`,
    { key, required: false, default: null })
  await new Promise(r => setTimeout(r, 300))
}

async function createBoolAttr(collId: string, key: string): Promise<void> {
  await apiFetch('POST',
    `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/attributes/boolean`,
    { key, required: false, default: null })
  await new Promise(r => setTimeout(r, 300))
}

/* ── entities_clean schema ────────────────────────────────────────────────── */

async function ensureCleanCollection(): Promise<void> {
  const id = 'entities_clean'
  if (await collectionExists(id)) {
    console.log(`[schema] 'entities_clean' already exists — skipping creation`)
    return
  }
  console.log(`[schema] creating 'entities_clean'…`)
  if (DRY_RUN) { console.log('  DRY RUN — skipped'); return }

  await apiFetch('POST', `${ENDPOINT}/databases/${DATABASE_ID}/collections`, {
    collectionId: id,
    name: 'Entities Clean',
    permissions: ['read("any")'],
    documentSecurity: false,
    enabled: true,
  })

  // Core identity
  await createStringAttr(id, 'slug',              120)
  await createStringAttr(id, 'label',              50)
  await createStringAttr(id, 'name',              200)
  await createStringAttr(id, 'callNumber',        120)
  await createStringAttr(id, 'era',                40)
  // Content
  await createStringAttr(id, 'summary',          3500)
  await createIntAttr   (id, 'importanceScore')
  await createStringAttr(id, 'wikidataQid',        30)
  // Structured data (serialised JSON)
  await createStringAttr(id, 'historicalSignificance', 2048)
  await createStringAttr(id, 'frameworks',         512)
  await createStringAttr(id, 'subjects',           512)
  await createStringAttr(id, 'subjectHeadings',   1024)
  await createStringAttr(id, 'places',            2048)
  await createStringAttr(id, 'quote',              500)
  await createStringAttr(id, 'causes',           16384)
  await createStringAttr(id, 'effects',          16384)
  await createStringAttr(id, 'relationships',    32768)
  // Pipeline metadata
  await createStringAttr(id, 'pipelineStatus',     20)
  await createStringAttr(id, 'promotedAt',         40)
  await createStringAttr(id, 'gateResults',       2048)
  await createIntAttr   (id, 'enrichmentVersion')
  await createStringAttr(id, 'sourceFile',        300)

  console.log(`[schema] 'entities_clean' created`)
}

/* ── entities_rejected schema ─────────────────────────────────────────────── */

async function ensureRejectedCollection(): Promise<void> {
  const id = 'entities_rejected'
  if (await collectionExists(id)) {
    console.log(`[schema] 'entities_rejected' already exists — skipping creation`)
    return
  }
  console.log(`[schema] creating 'entities_rejected'…`)
  if (DRY_RUN) { console.log('  DRY RUN — skipped'); return }

  await apiFetch('POST', `${ENDPOINT}/databases/${DATABASE_ID}/collections`, {
    collectionId: id,
    name: 'Entities Rejected',
    permissions: ['read("any")'],
    documentSecurity: false,
    enabled: true,
  })

  await createStringAttr(id, 'slug',        120)
  await createStringAttr(id, 'label',        50)
  await createStringAttr(id, 'callNumber',  120)
  await createStringAttr(id, 'era',          40)
  await createStringAttr(id, 'rejectedAt',   40)
  await createStringAttr(id, 'reason',      100)
  await createStringAttr(id, 'details',    2048)
  await createStringAttr(id, 'lastGate',    40)
  await createIntAttr   (id, 'attempts')
  await createStringAttr(id, 'sourceFile', 300)

  console.log(`[schema] 'entities_rejected' created`)
}

/* ── pipeline_status schema ───────────────────────────────────────────────── */

async function ensurePipelineStatusCollection(): Promise<void> {
  const id = 'pipeline_status'
  if (await collectionExists(id)) {
    console.log(`[schema] 'pipeline_status' already exists — skipping creation`)
    return
  }
  console.log(`[schema] creating 'pipeline_status'…`)
  if (DRY_RUN) { console.log('  DRY RUN — skipped'); return }

  await apiFetch('POST', `${ENDPOINT}/databases/${DATABASE_ID}/collections`, {
    collectionId: id,
    name: 'Pipeline Status',
    permissions: ['read("any")'],
    documentSecurity: false,
    enabled: true,
  })

  await createStringAttr(id, 'generatedAt',   40)
  await createIntAttr   (id, 'cleanCount')
  await createIntAttr   (id, 'rejectedCount')
  await createIntAttr   (id, 'pendingCount')
  await createIntAttr   (id, 'inFlightCount')
  await createIntAttr   (id, 'triagedCount')
  await createIntAttr   (id, 'validatedCount')
  await createStringAttr(id, 'triageReport',    4096)
  await createStringAttr(id, 'validateReport',  4096)
  await createStringAttr(id, 'enrichReport',    1024)

  console.log(`[schema] 'pipeline_status' created`)
}

/* ── sync documents ──────────────────────────────────────────────────────── */

function walkJsonFiles(dir: string): string[] {
  if (!fs.existsSync(dir)) return []
  const results: string[] = []
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) results.push(...walkJsonFiles(full))
    else if (entry.name.endsWith('.json')) results.push(full)
  }
  return results
}

/** Appwrite string attribute sizes — fields that need truncation at sync time */
const FIELD_MAX: Record<string, number> = {
  slug: 120, label: 50, name: 200, callNumber: 120, era: 40,
  wikidataQid: 30, pipelineStatus: 20, promotedAt: 40, sourceFile: 300,
  reason: 100, lastGate: 40, rejectedAt: 40, generatedAt: 40,
  subjects: 512, subjectHeadings: 1024, frameworks: 512, places: 2048,
  historicalSignificance: 2048, gateResults: 2048,
}

/** Fields that exceed Appwrite collection row budget — skip in sync (full data in local JSON) */
const SKIP_SYNC_FIELDS = new Set(['texts'])

function serializeField(val: unknown, key?: string): unknown {
  if (val === null || val === undefined) return null
  if (key && SKIP_SYNC_FIELDS.has(key)) return null
  if (typeof val === 'number' || typeof val === 'boolean') return val
  const s = typeof val === 'string' ? val : JSON.stringify(val)
  const max = key ? FIELD_MAX[key] : undefined
  if (max && s.length > max) return s.slice(0, max)
  return s
}

async function ensureStringAttrSize(collId: string, key: string, newSize: number): Promise<void> {
  try {
    const attr = await apiFetch('GET',
      `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/attributes/${key}`) as Record<string,unknown>
    if (typeof attr.size === 'number' && attr.size < newSize) {
      await apiFetch('PATCH',
        `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/attributes/string/${key}`,
        { size: newSize, required: false, default: null })
      console.log(`[schema] updated ${collId}.${key} → size ${newSize}`)
      await new Promise(r => setTimeout(r, 800))
    }
  } catch { /* attribute may not exist yet or already correct */ }
}

async function upsertDoc(collId: string, docId: string, payload: Record<string, unknown>): Promise<void> {
  const collUrl = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${collId}/documents`
  const docUrl  = `${collUrl}/${docId}`
  try {
    await apiFetch('PATCH', docUrl, { data: payload })
  } catch (e) {
    const msg = e instanceof Error ? e.message : String(e)
    if (msg.includes('404') || msg.includes('not found') || msg.includes('Document with the requested ID could not be found')) {
      await apiFetch('POST', collUrl, { documentId: docId, data: payload })
    } else throw e
  }
}

function toDocId(slug: string | undefined, fallback: string): string {
  const base = slug || fallback
  return base.replace(/[^a-zA-Z0-9_]/g, '_').replace(/^_+/, 'e').slice(0, 36)
}

async function syncCleanDocs(): Promise<void> {
  const files = walkJsonFiles(CLEAN_DIR)
  console.log(`[sync] entities_clean: ${files.length} files to sync`)
  let done = 0; let errors = 0
  for (const file of files) {
    try {
      const raw = JSON.parse(fs.readFileSync(file, 'utf8'))
      const docId = toDocId(raw.slug, path.basename(file, '.json'))
      const payload: Record<string, unknown> = {}
      for (const [k, v] of Object.entries(raw)) {
        if (k.startsWith('_') || k === '$id') continue
        payload[k] = serializeField(v, k)
      }
      if (DRY_RUN) {
        if (done < 3) console.log(`  DRY: would upsert ${docId}`)
      } else {
        await upsertDoc('entities_clean', docId, payload)
        await new Promise(r => setTimeout(r, 80))
      }
      done++
      if (done % 100 === 0) console.log(`  …synced ${done}/${files.length}`)
    } catch (e) {
      errors++
      if (errors <= 5) console.error(`  ERROR ${file}: ${e}`)
    }
  }
  console.log(`[sync] entities_clean done: ${done} upserted, ${errors} errors`)
}

async function syncRejectedDocs(): Promise<void> {
  const files = walkJsonFiles(REJECTED_DIR)
  console.log(`[sync] entities_rejected: ${files.length} files to sync`)
  let done = 0; let errors = 0
  for (const file of files) {
    try {
      const raw = JSON.parse(fs.readFileSync(file, 'utf8'))
      const docId = toDocId(raw.slug, path.basename(file, '.json'))
      const payload: Record<string, unknown> = {}
      for (const [k, v] of Object.entries(raw)) {
        if (k.startsWith('_') || k === '$id') continue
        payload[k] = serializeField(v, k)
      }
      if (DRY_RUN) {
        if (done < 3) console.log(`  DRY: would upsert ${docId}`)
      } else {
        await upsertDoc('entities_rejected', docId, payload)
        await new Promise(r => setTimeout(r, 80))
      }
      done++
      if (done % 100 === 0) console.log(`  …synced ${done}/${files.length}`)
    } catch (e) {
      errors++
      if (errors <= 5) console.error(`  ERROR ${file}: ${e}`)
    }
  }
  console.log(`[sync] entities_rejected done: ${done} upserted, ${errors} errors`)
}

async function syncPipelineStatus(): Promise<void> {
  const statusFile = path.join(ROOT, 'data', 'pipeline', 'pipeline_status.json')
  if (!fs.existsSync(statusFile)) { console.log('[sync] pipeline_status.json not found, skipping'); return }
  const raw = JSON.parse(fs.readFileSync(statusFile, 'utf8'))
  const triageReport = path.join(ROOT, 'data', 'pipeline', 'triage_report.json')
  const validateReport = path.join(ROOT, 'data', 'pipeline', 'validate_report.json')
  const enrichReport = path.join(ROOT, 'data', 'pipeline', 'enrich_report.json')

  const payload: Record<string, unknown> = {
    generatedAt:     raw.generatedAt,
    cleanCount:      raw.clean || 0,
    rejectedCount:   raw.triage?.counts?.rejected || raw.rejected || 0,
    triagedCount:    raw.triage?.counts?.triaged || 0,
    validatedCount:  raw.clean || raw.validate?.counts?.validated || 0,
    pendingCount:    (raw.triage?.counts?.triaged || 0) - (raw.clean || 0),
    inFlightCount:   raw.triage?.counts?.['in-flight'] || 0,
    triageReport:    fs.existsSync(triageReport)  ? fs.readFileSync(triageReport, 'utf8').slice(0, 4000)  : null,
    validateReport:  fs.existsSync(validateReport) ? fs.readFileSync(validateReport, 'utf8').slice(0, 4000) : null,
    enrichReport:    fs.existsSync(enrichReport)   ? fs.readFileSync(enrichReport, 'utf8').slice(0, 1000)  : null,
  }
  if (DRY_RUN) { console.log('[sync] DRY — would upsert pipeline_status doc'); return }
  await upsertDoc('pipeline_status', 'global', payload)
  console.log('[sync] pipeline_status upserted')
}

/* ── main ────────────────────────────────────────────────────────────────── */

async function main() {
  console.log(`\n${'═'.repeat(60)}`)
  console.log(`PIPELINE COLLECTIONS PUSH${DRY_RUN ? ' [DRY RUN]' : ''}`)
  console.log(`${'═'.repeat(60)}\n`)

  await ensureCleanCollection()
  await ensureRejectedCollection()
  await ensurePipelineStatusCollection()

  // Upgrade any attributes that were created with smaller sizes
  await ensureStringAttrSize('entities_clean',    'callNumber', 120)
  await ensureStringAttrSize('entities_rejected', 'callNumber', 120)

  if (!SCHEMA_ONLY) {
    await syncCleanDocs()
    await syncRejectedDocs()
    await syncPipelineStatus()
  }

  console.log('\nDone.')
}

main().catch(e => { console.error(e); process.exit(1) })
