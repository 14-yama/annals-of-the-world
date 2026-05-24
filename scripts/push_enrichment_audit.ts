#!/usr/bin/env node
/**
 * push_enrichment_audit.ts
 *
 * Reads data/governance/enrichment_audit.json (written by audit_enrichment.py)
 * and upserts a single document into the Appwrite `enrichment_audit` collection.
 *
 * Creates the collection (and attributes) if it doesn't exist yet.
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/push_enrichment_audit.ts
 *   # or: env $(cat .env | grep -v '^#' | xargs) npx tsx scripts/push_enrichment_audit.ts
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

const COLLECTION_ID = 'enrichment_audit'
const DOC_ID        = 'global'
const AUDIT_FILE    = path.join(ROOT, 'data', 'governance', 'enrichment_audit.json')

if (!API_KEY) {
  console.error('ERROR: APPWRITE_API_KEY not set')
  process.exit(1)
}

function ah(): Record<string, string> {
  return {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY!,
  }
}

async function apiFetch(method: string, url: string, body?: unknown): Promise<unknown> {
  const res = await fetch(url, {
    method,
    headers: ah(),
    body: body ? JSON.stringify(body) : undefined,
  })
  const text = await res.text()
  if (!res.ok) {
    throw new Error(`${method} ${url} → ${res.status}: ${text.slice(0, 400)}`)
  }
  return JSON.parse(text)
}

async function ensureCollection(): Promise<void> {
  const listUrl = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${COLLECTION_ID}`
  try {
    await apiFetch('GET', listUrl)
    console.log(`[setup] collection '${COLLECTION_ID}' already exists`)
    return
  } catch (e: unknown) {
    const msg = e instanceof Error ? e.message : String(e)
    if (!msg.includes('404') && !msg.includes('not found')) throw e
  }

  console.log(`[setup] creating collection '${COLLECTION_ID}'…`)
  await apiFetch('POST', `${ENDPOINT}/databases/${DATABASE_ID}/collections`, {
    collectionId: COLLECTION_ID,
    name: 'Enrichment Audit',
    permissions: ['read("any")'],
    documentSecurity: false,
    enabled: true,
  })

  const attrs: Array<{ key: string; type: string; size?: number; required?: boolean }> = [
    { key: 'generatedAt',       type: 'string',  size: 40 },
    { key: 'computeTimeMs',     type: 'integer' },
    { key: 'filesScanned',      type: 'integer' },
    { key: 'total',             type: 'integer' },
    { key: 'enriched',          type: 'integer' },
    { key: 'highQuality',       type: 'integer' },
    { key: 'stubs',             type: 'integer' },
    { key: 'weak',              type: 'integer' },
    { key: 'lowEdges',          type: 'integer' },
    { key: 'fieldCoverage',     type: 'string',  size: 1024 },
    { key: 'byLabel',           type: 'string',  size: 16384 },
    { key: 'byClass',           type: 'string',  size: 8192 },
    { key: 'byDivision',        type: 'string',  size: 131072 },
    { key: 'significanceDist',  type: 'string',  size: 2048 },
    { key: 'velocity',          type: 'string',  size: 2048 },
  ]

  const base = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${COLLECTION_ID}/attributes`
  for (const attr of attrs) {
    if (attr.type === 'string') {
      await apiFetch('POST', `${base}/string`, {
        key: attr.key, size: attr.size ?? 1024, required: false, default: null,
      })
    } else {
      await apiFetch('POST', `${base}/integer`, {
        key: attr.key, required: false, default: null,
      })
    }
    await new Promise(r => setTimeout(r, 300))  // gentle pace
  }
  console.log(`[setup] collection created with ${attrs.length} attributes`)
}

async function upsertDoc(data: Record<string, unknown>): Promise<void> {
  const docUrl = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${COLLECTION_ID}/documents/${DOC_ID}`

  // Serialize JSON sub-objects to strings (Appwrite string attributes)
  const payload: Record<string, unknown> = {
    generatedAt:       data.generatedAt,
    computeTimeMs:     data.computeTimeMs,
    filesScanned:      data.filesScanned,
    total:             data.total,
    enriched:          data.enriched,
    highQuality:       data.highQuality,
    stubs:             data.stubs,
    weak:              data.weak,
    lowEdges:          data.lowEdges,
    fieldCoverage:     JSON.stringify(data.fieldCoverage),
    byLabel:           JSON.stringify(data.byLabel),
    byClass:           JSON.stringify(data.byClass),
    byDivision:        JSON.stringify(data.byDivision),
    significanceDist:  JSON.stringify(data.significanceDist),
    velocity:          JSON.stringify(data.velocity ?? {}),
  }

  // Try PATCH first, then POST if 404
  try {
    await apiFetch('PATCH', docUrl, { data: payload })
    console.log(`[upsert] updated document '${DOC_ID}'`)
    return
  } catch (e: unknown) {
    const msg = e instanceof Error ? e.message : String(e)
    if (!msg.includes('404') && !msg.includes('not found')) throw e
  }

  await apiFetch('POST', `${ENDPOINT}/databases/${DATABASE_ID}/collections/${COLLECTION_ID}/documents`, {
    documentId: DOC_ID,
    data: payload,
    permissions: [],
  })
  console.log(`[upsert] created document '${DOC_ID}'`)
}

async function main() {
  if (!fs.existsSync(AUDIT_FILE)) {
    console.error(`ERROR: ${AUDIT_FILE} not found — run audit_enrichment.py first`)
    process.exit(1)
  }
  const data = JSON.parse(fs.readFileSync(AUDIT_FILE, 'utf-8')) as Record<string, unknown>
  console.log(`[push] generatedAt=${data.generatedAt}, total=${data.total}, enriched=${data.enriched}`)

  await ensureCollection()
  await upsertDoc(data)
  console.log('[push] done ✓')
}

main().catch(err => { console.error('[push] FATAL:', err); process.exit(1) })
