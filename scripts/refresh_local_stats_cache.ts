#!/usr/bin/env npx tsx
/**
 * refresh_local_stats_cache.ts
 *
 * Local Docker Appwrite KPI refresh for curator pages that read stats_cache
 * (/catalog, curator audit, ClassHub via useGlobalCounts).
 *
 * Resumable / SIGTERM-safe:
 *   1. Fast ID-only page count → write `total` immediately (empty facets OK)
 *   2. Facet pass in chunks with checkpoint file; mirrors update incrementally
 *
 * Usage:
 *   npx tsx scripts/refresh_local_stats_cache.ts
 *   npx tsx scripts/refresh_local_stats_cache.ts --total-only
 *   npx tsx scripts/refresh_local_stats_cache.ts --facets
 *   npx tsx scripts/refresh_local_stats_cache.ts --from-git
 *   npx tsx scripts/refresh_local_stats_cache.ts --reset-checkpoint
 */
import * as fs from 'fs'
import * as path from 'path'
import { Client, Databases, Query, ID, Permission, Role } from 'node-appwrite'

const ROOT = path.resolve(__dirname, '..')
const CHECKPOINT = path.join(ROOT, 'data/governance/stats_cache_progress.json')

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
const TOTAL_ONLY = process.argv.includes('--total-only')
const FACETS_ONLY = process.argv.includes('--facets')
const RESET_CHECKPOINT = process.argv.includes('--reset-checkpoint')
const STATS_COLLECTION = 'stats_cache'
const ENTITIES = 'entities'
/** Appwrite listDocuments hard-caps page size; 100 is the portable max. */
const PAGE = 100
const PROGRESS_EVERY = 5000
const CHECKPOINT_EVERY = 2000
const MIRROR_EVERY = 25000

if (!KEY) {
  console.error('ERROR: APPWRITE_API_KEY / LOCAL_APPWRITE_API_KEY missing')
  process.exit(1)
}

const client = new Client().setEndpoint(ENDPOINT).setProject(PROJECT).setKey(KEY)
const databases = new Databases(client)

type Bucket = Record<string, number>

interface Checkpoint {
  phase: 'facets'
  cursor: string | null
  totalSeen: number
  byLabel: Bucket
  byEra: Bucket
  byContinent: Bucket
  byClass: Bucket
  startedAt: string
  updatedAt: string
  knownTotal?: number
}

interface StatsPayload {
  total: number
  byLabel: Bucket
  byEra: Bucket
  byContinent: Bucket
  byClass: Bucket
  computeTimeMs: number
  note?: string
  incomplete?: boolean
}

let shuttingDown = false
let lastCheckpoint: Checkpoint | null = null

function onSignal(sig: string) {
  shuttingDown = true
  console.log(`[stats] received ${sig} — saving checkpoint and exiting…`)
  if (lastCheckpoint) writeCheckpoint(lastCheckpoint)
  process.exit(143)
}
process.on('SIGTERM', () => onSignal('SIGTERM'))
process.on('SIGINT', () => onSignal('SIGINT'))

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
  await new Promise((r) => setTimeout(r, 4000))
  console.log('[stats] stats_cache ready')
}

async function ensureAuditNewValueAttr() {
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

function loadSeedCursor(): Record<string, unknown> | null {
  const p = path.join(ROOT, 'data/governance/seed_local_cursor.json')
  if (!fs.existsSync(p)) return null
  try {
    return JSON.parse(fs.readFileSync(p, 'utf8'))
  } catch {
    return null
  }
}

function writeCheckpoint(cp: Checkpoint) {
  fs.mkdirSync(path.dirname(CHECKPOINT), { recursive: true })
  fs.writeFileSync(CHECKPOINT, JSON.stringify(cp, null, 2) + '\n')
  lastCheckpoint = cp
}

function readCheckpoint(): Checkpoint | null {
  if (!fs.existsSync(CHECKPOINT)) return null
  try {
    return JSON.parse(fs.readFileSync(CHECKPOINT, 'utf8')) as Checkpoint
  } catch {
    return null
  }
}

function clearCheckpoint() {
  if (fs.existsSync(CHECKPOINT)) fs.unlinkSync(CHECKPOINT)
  lastCheckpoint = null
}

async function writeStats(stats: StatsPayload, extra?: Record<string, unknown>) {
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

  const seedCursor = loadSeedCursor()
  const snapshot = {
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
    note: stats.note || 'paged entity count (ignores API total cap)',
    incomplete: stats.incomplete || false,
    ...(seedCursor
      ? {
          seedCursor: {
            scanned: seedCursor.scanned,
            created: seedCursor.created,
            skipped: seedCursor.skipped,
            failed: seedCursor.failed,
            classDir: seedCursor.classDir,
            file: seedCursor.file,
            lastRunAt: seedCursor.lastRunAt,
          },
        }
      : {}),
    ...extra,
  }
  const body = JSON.stringify(snapshot, null, 2) + '\n'
  for (const rel of ['data/governance/stats_cache.json', 'ui/public/governance/stats_cache.json']) {
    const p = path.join(ROOT, rel)
    fs.mkdirSync(path.dirname(p), { recursive: true })
    fs.writeFileSync(p, body)
  }
  return updatedAt
}

function maxExpectedTotal(): number {
  const seed = loadSeedCursor()
  const scanned = Number(seed?.scanned || 0)
  // Hard stop well above seed/export size — prevents SDK cursor loops (saw 1.9M+)
  return Math.max(scanned * 2 || 0, 600_000)
}

/** Phase 1: ID-only page count — fast, writes total immediately. */
async function countTotalOnly(): Promise<number> {
  const started = Date.now()
  const hardCap = maxExpectedTotal()
  let total = 0
  let cursor: string | undefined
  let prevCursor: string | undefined
  while (!shuttingDown) {
    const queries = [Query.limit(PAGE), Query.select(['$id'])]
    if (cursor) queries.push(Query.cursorAfter(cursor))
    const page = await databases.listDocuments(DATABASE, ENTITIES, queries)
    const docs = page.documents || []
    if (docs.length === 0) break
    total += docs.length
    prevCursor = cursor
    cursor = docs[docs.length - 1].$id
    if (cursor === prevCursor) {
      console.error('[stats] cursor not advancing — aborting runaway count')
      break
    }
    if (total > hardCap) {
      console.error(`[stats] count ${total} exceeded hardCap ${hardCap} — aborting runaway`)
      throw new Error(`runaway count ${total} > ${hardCap}`)
    }
    if (total % PROGRESS_EVERY < PAGE) {
      console.log(`[stats] counted ${total}… (${Date.now() - started}ms)`)
    }
    if (docs.length < PAGE) break
  }
  console.log(`[stats] ground-truth total=${total} (${Date.now() - started}ms)`)
  return total
}

/** Phase 2: facet aggregation with checkpoint / resume. */
async function countFacets(knownTotal: number): Promise<StatsPayload> {
  const started = Date.now()
  let cp = RESET_CHECKPOINT ? null : readCheckpoint()
  if (cp && cp.phase !== 'facets') cp = null

  // Discard corrupt checkpoints from the pre-fix runaway (select omitted $id →
  // cursorAfter never advanced, totalSeen climbed to millions).
  const hardCap = Math.max(knownTotal > 0 ? knownTotal * 2 : 0, maxExpectedTotal())
  if (cp && (cp.totalSeen > hardCap || (!cp.cursor && cp.totalSeen > (knownTotal || 0) + PAGE))) {
    console.warn(
      `[stats] discarding corrupt facet checkpoint (seen=${cp.totalSeen}, hardCap=${hardCap})`,
    )
    clearCheckpoint()
    cp = null
  }

  const byLabel: Bucket = { ...(cp?.byLabel || {}) }
  const byEra: Bucket = { ...(cp?.byEra || {}) }
  const byContinent: Bucket = { ...(cp?.byContinent || {}) }
  const byClass: Bucket = { ...(cp?.byClass || {}) }
  let totalSeen = cp?.totalSeen || 0
  let cursor: string | undefined = cp?.cursor || undefined
  let prevCursor: string | undefined
  const facetStartedAt = cp?.startedAt || new Date().toISOString()

  if (cp) {
    console.log(`[stats] resuming facets from cursor @ ${totalSeen} seen`)
  } else {
    console.log('[stats] starting facet pass…')
  }

  let sinceCheckpoint = 0
  let sinceMirror = 0

  while (!shuttingDown) {
    // MUST include $id — cursorAfter needs it. Omitting $id caused an infinite
    // re-scan loop that starved MariaDB (~4M "seen" on a 392k corpus).
    const queries = [
      Query.limit(PAGE),
      Query.select(['$id', 'label', 'era', 'continent', 'callNumber']),
    ]
    if (cursor) queries.push(Query.cursorAfter(cursor))
    const page = await databases.listDocuments(DATABASE, ENTITIES, queries)
    const docs = page.documents || []
    if (docs.length === 0) break

    for (const doc of docs) {
      totalSeen++
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
    prevCursor = cursor
    cursor = docs[docs.length - 1].$id
    if (!cursor || cursor === prevCursor) {
      console.error('[stats] facet cursor not advancing — aborting runaway facet pass')
      break
    }
    if (totalSeen > hardCap) {
      console.error(
        `[stats] facets ${totalSeen} exceeded hardCap ${hardCap} — aborting runaway`,
      )
      throw new Error(`runaway facets ${totalSeen} > ${hardCap}`)
    }
    sinceCheckpoint += docs.length
    sinceMirror += docs.length

    if (totalSeen % PROGRESS_EVERY < PAGE) {
      console.log(`[stats] facets ${totalSeen}/${knownTotal || '?'}… (${Date.now() - started}ms)`)
    }

    if (sinceCheckpoint >= CHECKPOINT_EVERY) {
      const next: Checkpoint = {
        phase: 'facets',
        cursor: cursor || null,
        totalSeen,
        byLabel,
        byEra,
        byContinent,
        byClass,
        startedAt: facetStartedAt,
        updatedAt: new Date().toISOString(),
        knownTotal,
      }
      writeCheckpoint(next)
      sinceCheckpoint = 0
    }

    if (sinceMirror >= MIRROR_EVERY) {
      await writeStats(
        {
          total: knownTotal || totalSeen,
          byLabel,
          byEra,
          byContinent,
          byClass,
          computeTimeMs: Date.now() - started,
          note: 'facet pass in progress (resumable)',
          incomplete: true,
        },
        { facetProgress: { totalSeen, knownTotal } },
      )
      console.log(`[stats] interim mirror @ ${totalSeen}`)
      sinceMirror = 0
    }

    if (docs.length < PAGE) break
  }

  if (shuttingDown) {
    writeCheckpoint({
      phase: 'facets',
      cursor: cursor || null,
      totalSeen,
      byLabel,
      byEra,
      byContinent,
      byClass,
      startedAt: facetStartedAt,
      updatedAt: new Date().toISOString(),
      knownTotal,
    })
    throw new Error('interrupted')
  }

  clearCheckpoint()
  const total = knownTotal > 0 ? knownTotal : totalSeen
  // Prefer facet-pass count if it exceeds a stale knownTotal
  const finalTotal = Math.max(total, totalSeen)
  return {
    total: finalTotal,
    byLabel,
    byEra,
    byContinent,
    byClass,
    computeTimeMs: Date.now() - started,
    note: 'paged entity count + facets (ignores API total cap)',
    incomplete: false,
  }
}

function loadGitStats(): StatsPayload | null {
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
      note: 'from data/audit-reports/stats.json',
    }
  } catch {
    return null
  }
}

async function main() {
  console.log(`[stats] endpoint=${ENDPOINT} project=${PROJECT} db=${DATABASE}`)
  if (RESET_CHECKPOINT) {
    clearCheckpoint()
    console.log('[stats] checkpoint cleared')
  }
  await ensureStatsCollection()
  await ensureAuditNewValueAttr()

  if (FROM_GIT) {
    const stats = loadGitStats()
    if (!stats) {
      console.error('[stats] no git stats available')
      process.exit(1)
    }
    const updatedAt = await writeStats(stats)
    console.log(`[stats] wrote stats_cache total=${stats.total} updatedAt=${updatedAt}`)
    return
  }

  let knownTotal = 0
  if (!FACETS_ONLY) {
    knownTotal = await countTotalOnly()
    // Write total first so UI/API consumers never sit on 5000 / stale interim.
    const updatedAt = await writeStats({
      total: knownTotal,
      byLabel: {},
      byEra: {},
      byContinent: {},
      byClass: {},
      computeTimeMs: 0,
      note: 'paged entity count (facets pending)',
      incomplete: true,
    })
    console.log(`[stats] wrote TOTAL-FIRST total=${knownTotal} updatedAt=${updatedAt}`)
    if (TOTAL_ONLY) return
  } else {
    const mirror = path.join(ROOT, 'data/governance/stats_cache.json')
    if (fs.existsSync(mirror)) {
      try {
        knownTotal = Number(JSON.parse(fs.readFileSync(mirror, 'utf8')).total || 0)
      } catch { /* ignore */ }
    }
    const cp = readCheckpoint()
    if (cp?.knownTotal) knownTotal = cp.knownTotal
  }

  const stats = await countFacets(knownTotal)
  const updatedAt = await writeStats(stats)
  console.log(`[stats] wrote stats_cache total=${stats.total} updatedAt=${updatedAt} (${stats.computeTimeMs}ms)`)
  console.log(`[stats] facets labels=${Object.keys(stats.byLabel).length} eras=${Object.keys(stats.byEra).length}`)
}

main().catch((err) => {
  const msg = (err as Error).message || String(err)
  if (msg === 'interrupted') {
    console.error('[stats] interrupted — re-run to resume facets from checkpoint')
    process.exit(143)
  }
  console.error('[stats] failed:', msg)
  process.exit(1)
})
