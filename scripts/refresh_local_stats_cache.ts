#!/usr/bin/env npx tsx
/**
 * refresh_local_stats_cache.ts
 *
 * Local Docker Appwrite KPI refresh for curator pages that read stats_cache
 * (/catalog, curator audit, ClassHub via useGlobalCounts).
 *
 * - Ensures stats_cache (+ optional enrichment_audit) collections exist
 * - Counts entities by label / era / continent / class (live local DB)
 * - Appends a new stats_cache row (UI reads latest by updatedAt)
 * - Mirrors a compact JSON snapshot under ui/public/governance/stats_cache.json
 *
 * Usage:
 *   npx tsx scripts/refresh_local_stats_cache.ts
 *   npx tsx scripts/refresh_local_stats_cache.ts --from-git   # use data/audit-reports/stats.json
 */
import * as fs from 'fs'
import * as path from 'path'
import { Client, Databases, Query, ID, Permission, Role } from 'node-appwrite'

const ROOT = path.resolve(__dirname, '..')

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

loadDotEnvFile(path.join(ROOT, '.env'))
loadDotEnvFile(path.join(process.env.HOME || '', '.config/annals/env'))

const ENDPOINT = process.env.LOCAL_APPWRITE_ENDPOINT || process.env.VITE_APPWRITE_ENDPOINT || 'http://localhost:8080/v1'
const PROJECT = process.env.LOCAL_APPWRITE_PROJECT_ID || process.env.VITE_APPWRITE_PROJECT_ID || 'annals-local'
const DATABASE = process.env.LOCAL_APPWRITE_DATABASE_ID || process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const KEY = process.env.LOCAL_APPWRITE_API_KEY || process.env.APPWRITE_API_KEY || ''
const FROM_GIT = process.argv.includes('--from-git')
const STATS_COLLECTION = 'stats_cache'
const ENTITIES = 'entities'
const PAGE = 100

if (!KEY) {
  console.error('ERROR: APPWRITE_API_KEY / LOCAL_APPWRITE_API_KEY missing')
  process.exit(1)
}

const client = new Client().setEndpoint(ENDPOINT).setProject(PROJECT).setKey(KEY)
const databases = new Databases(client)

async function ensureStatsCollection() {
  try {
    await databases.getCollection(DATABASE, STATS_COLLECTION)
    return
  } catch {
    console.log('[stats] creating stats_cache collection…')
  }
  await databases.createCollection(
    DATABASE,
    STATS_COLLECTION,
    'Stats Cache',
    [Permission.read(Role.any())],
    false,
    true,
  )
  const attrs: Array<() => Promise<unknown>> = [
    () => databases.createIntegerAttribute(DATABASE, STATS_COLLECTION, 'total', true),
    () => databases.createStringAttribute(DATABASE, STATS_COLLECTION, 'byLabel', 4000, true),
    () => databases.createStringAttribute(DATABASE, STATS_COLLECTION, 'byEra', 2000, true),
    () => databases.createStringAttribute(DATABASE, STATS_COLLECTION, 'byContinent', 2000, true),
    () => databases.createStringAttribute(DATABASE, STATS_COLLECTION, 'byClass', 1000, true),
    () => databases.createStringAttribute(DATABASE, STATS_COLLECTION, 'updatedAt', 64, true),
    () => databases.createIntegerAttribute(DATABASE, STATS_COLLECTION, 'computeTimeMs', false),
  ]
  for (const make of attrs) {
    try {
      await make()
    } catch (err) {
      const msg = (err as Error).message || ''
      if (!/already exists|409/i.test(msg)) throw err
    }
    await new Promise((r) => setTimeout(r, 250))
  }
  // Attribute availability lag on fresh Appwrite
  await new Promise((r) => setTimeout(r, 4000))
  console.log('[stats] stats_cache ready')
}

async function ensureAuditNewValueAttr() {
  // Local Docker schema may already include newValue (4000). Best-effort only.
  try {
    const res = await databases.listAttributes(DATABASE, 'audit_log')
    const attrs = (res as { attributes?: Array<{ key: string }> }).attributes || []
    if (attrs.some((a) => a.key === 'newValue')) return
    console.log('[stats] adding audit_log.newValue attribute…')
    await databases.createStringAttribute(DATABASE, 'audit_log', 'newValue', 4000, false)
    await new Promise((r) => setTimeout(r, 3000))
  } catch (err) {
    console.warn('[stats] audit_log.newValue ensure skipped:', (err as Error).message)
  }
}

type Bucket = Record<string, number>

async function countLive(): Promise<{
  total: number
  byLabel: Bucket
  byEra: Bucket
  byContinent: Bucket
  byClass: Bucket
  computeTimeMs: number
}> {
  const started = Date.now()
  const byLabel: Bucket = {}
  const byEra: Bucket = {}
  const byContinent: Bucket = {}
  const byClass: Bucket = {}
  let total = 0
  let cursor: string | undefined

  // Prefer cheap totals when corpus is small; still page for breakdowns
  const head = await databases.listDocuments(DATABASE, ENTITIES, [Query.limit(1)])
  total = head.total || 0

  if (total === 0) {
    return { total: 0, byLabel, byEra, byContinent, byClass, computeTimeMs: Date.now() - started }
  }

  // Full scan for facet buckets (local Mini corpus during seed is small; scales with cursor)
  let scanned = 0
  while (scanned < total) {
    const queries = [Query.limit(PAGE), Query.select(['label', 'era', 'continent', 'callNumber'])]
    if (cursor) queries.push(Query.cursorAfter(cursor))
    const page = await databases.listDocuments(DATABASE, ENTITIES, queries)
    const docs = page.documents || []
    if (docs.length === 0) break
    for (const doc of docs) {
      scanned++
      const label = String((doc as { label?: string }).label || 'Unknown')
      const era = String((doc as { era?: string }).era || 'Unknown')
      const continent = String((doc as { continent?: string }).continent || 'Unknown')
      const cn = String((doc as { callNumber?: string }).callNumber || '')
      byLabel[label] = (byLabel[label] || 0) + 1
      byEra[era] = (byEra[era] || 0) + 1
      byContinent[continent] = (byContinent[continent] || 0) + 1
      if (cn && /^\d/.test(cn)) {
        const cls = cn[0]
        byClass[cls] = (byClass[cls] || 0) + 1
      }
    }
    cursor = docs[docs.length - 1].$id
    if (docs.length < PAGE) break
  }

  // Prefer authoritative Appwrite total when pagination truncated
  if (head.total && head.total > scanned) {
    total = head.total
  } else {
    total = scanned
  }

  return { total, byLabel, byEra, byContinent, byClass, computeTimeMs: Date.now() - started }
}

function loadGitStats(): {
  total: number
  byLabel: Bucket
  byEra: Bucket
  byContinent: Bucket
  byClass: Bucket
  computeTimeMs: number
} | null {
  const p = path.join(ROOT, 'data/audit-reports/stats.json')
  if (!fs.existsSync(p)) return null
  try {
    const raw = JSON.parse(fs.readFileSync(p, 'utf8'))
    return {
      total: Number(raw.total || 0),
      byLabel: raw.byLabel || {},
      byEra: raw.byEra || {},
      byContinent: raw.byContinent || {},
      byClass: raw.byClass || {},
      computeTimeMs: 0,
    }
  } catch {
    return null
  }
}

async function appendStats(stats: {
  total: number
  byLabel: Bucket
  byEra: Bucket
  byContinent: Bucket
  byClass: Bucket
  computeTimeMs: number
}) {
  const updatedAt = new Date().toISOString()
  const payload = {
    total: stats.total,
    byLabel: JSON.stringify(stats.byLabel),
    byEra: JSON.stringify(stats.byEra),
    byContinent: JSON.stringify(stats.byContinent),
    byClass: JSON.stringify(stats.byClass),
    updatedAt,
    computeTimeMs: stats.computeTimeMs,
  }
  await databases.createDocument(
    DATABASE,
    STATS_COLLECTION,
    ID.unique(),
    payload,
    [Permission.read(Role.any())],
  )

  // Prune old rows (keep 40)
  try {
    const old = await databases.listDocuments(DATABASE, STATS_COLLECTION, [
      Query.orderDesc('updatedAt'),
      Query.offset(40),
      Query.limit(50),
    ])
    for (const doc of old.documents || []) {
      await databases.deleteDocument(DATABASE, STATS_COLLECTION, doc.$id)
    }
  } catch {
    /* best-effort */
  }

  const publicPath = path.join(ROOT, 'ui/public/governance/stats_cache.json')
  fs.mkdirSync(path.dirname(publicPath), { recursive: true })
  fs.writeFileSync(
    publicPath,
    JSON.stringify(
      {
        updatedAt,
        source: FROM_GIT ? 'git-stats' : 'local-appwrite',
        endpoint: ENDPOINT,
        project: PROJECT,
        database: DATABASE,
        total: stats.total,
        byLabel: stats.byLabel,
        byEra: stats.byEra,
        byContinent: stats.byContinent,
        byClass: stats.byClass,
        computeTimeMs: stats.computeTimeMs,
      },
      null,
      2,
    ) + '\n',
  )
  return updatedAt
}

async function main() {
  console.log(`[stats] endpoint=${ENDPOINT} project=${PROJECT} db=${DATABASE}`)
  await ensureStatsCollection()
  await ensureAuditNewValueAttr()

  const stats = FROM_GIT ? loadGitStats() : await countLive()
  if (!stats) {
    console.error('[stats] no stats available')
    process.exit(1)
  }

  const updatedAt = await appendStats(stats)
  console.log(`[stats] wrote stats_cache total=${stats.total} updatedAt=${updatedAt} (${stats.computeTimeMs}ms)`)
}

main().catch((err) => {
  console.error('[stats] failed:', err.message || err)
  process.exit(1)
})
