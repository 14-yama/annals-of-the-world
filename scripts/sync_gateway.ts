#!/usr/bin/env npx tsx
/**
 * sync_gateway.ts — The ONLY writer to Appwrite.
 *
 * Reads from data/appwrite-export/entities/, computes a diff against the
 * last-synced commit (data/governance/last_sync.json), and pushes only the
 * changed entity files. Honors hard caps in data/governance/budget.json.
 *
 * For each entity, also emits one audit_log row per `_editLog[]` entry
 * found in detailsJson, then clears the log + the `_unsyncedEdits` flag in
 * the local file.
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_gateway.ts
 *
 * Flags:
 *   --dry-run       Compute diff and show what would be written. No API calls.
 *   --full          Ignore last_sync.json; sync everything (slow; emergency only).
 *   --max=<N>       Override perRunWriteCap from budget.json.
 */
import * as fs from 'fs'
import * as path from 'path'
import * as crypto from 'crypto'
import { execSync } from 'child_process'

// ── Config ──
const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID || '66509ba7003618a05af6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const API_KEY     = process.env.APPWRITE_API_KEY
const SYNC_EDITOR = process.env.SYNC_EDITOR_ID || 'sync-gateway'

const ROOT       = path.resolve(__dirname, '..')
const EXPORT_DIR = path.join(ROOT, 'data', 'appwrite-export')
const ENTITIES_DIR = path.join(EXPORT_DIR, 'entities')
const BUDGET_FILE = path.join(ROOT, 'data', 'governance', 'budget.json')
const LAST_SYNC_FILE = path.join(ROOT, 'data', 'governance', 'last_sync.json')

const args = process.argv.slice(2)
const DRY_RUN = args.includes('--dry-run')
const FULL = args.includes('--full')
// --local: scan for files with _unsyncedEdits:true instead of git diff.
// Used by local_bot_server so sync runs BEFORE git commit (no commit needed).
const LOCAL = args.includes('--local')
const maxArg = args.find(a => a.startsWith('--max='))
const MAX_OVERRIDE = maxArg ? parseInt(maxArg.split('=')[1], 10) : undefined

if (!API_KEY && !DRY_RUN) {
  console.error('ERROR: Set APPWRITE_API_KEY env var (or pass --dry-run)')
  process.exit(1)
}

// ── Types ──
interface Budget {
  monthlyReadCap: number
  monthlyWriteCap: number
  perRunWriteCap: number
  minMsBetweenWrites: number
  hardStopPercent: number
  resetDay: number
  current: { cycleStart: string; readsUsed: number; writesUsed: number; lastUpdated: string }
  manualPause: boolean
  manualPauseReason: string
}

interface LastSync {
  lastSyncedCommit: string
  lastRunAt: string
  lastRunStatus: string
  lastRunStats: Record<string, unknown>
}

interface EditLogEntry {
  timestamp: string
  editorId: string
  field: string
  oldValue: unknown
  newValue: unknown
}

interface Entity {
  slug?: string
  name?: string
  $id?: string
  detailsJson?: string | Record<string, unknown>
  [k: string]: unknown
}

// ── Helpers ──
function loadJson<T>(p: string): T {
  return JSON.parse(fs.readFileSync(p, 'utf-8')) as T
}

function saveJson(p: string, data: unknown): void {
  fs.writeFileSync(p, JSON.stringify(data, null, 2) + '\n', 'utf-8')
}

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

function sleep(ms: number): Promise<void> {
  return new Promise(r => setTimeout(r, ms))
}

// ── Budget gate ──
function loadBudget(): Budget {
  if (!fs.existsSync(BUDGET_FILE)) {
    throw new Error(`budget.json not found at ${BUDGET_FILE}`)
  }
  return loadJson<Budget>(BUDGET_FILE)
}

function saveBudget(b: Budget): void {
  saveJson(BUDGET_FILE, b)
}

function checkBudget(b: Budget, additionalWrites = 0): { ok: boolean; reason?: string } {
  if (b.manualPause) {
    return { ok: false, reason: `manual pause: ${b.manualPauseReason || '(no reason)'}` }
  }
  // Cycle reset: if today is after resetDay and cycleStart is older than this cycle, reset.
  const now = new Date()
  const cycleStart = new Date(b.current.cycleStart)
  const cycleAge = (now.getTime() - cycleStart.getTime()) / (1000 * 60 * 60 * 24)
  if (cycleAge > 32) {
    console.log(`[budget] Cycle older than 32 days — resetting counters`)
    b.current.cycleStart = now.toISOString().slice(0, 10)
    b.current.readsUsed = 0
    b.current.writesUsed = 0
  }
  const cap = b.monthlyWriteCap
  const projected = b.current.writesUsed + additionalWrites
  const pct = cap > 0 ? (projected / cap) * 100 : 0
  if (pct >= b.hardStopPercent) {
    return { ok: false, reason: `BUDGET_EXCEEDED writes ${projected}/${cap} (${pct.toFixed(1)}%) >= ${b.hardStopPercent}%` }
  }
  return { ok: true }
}

// ── Diff against last-synced commit ──
function changedEntityFiles(lastCommit: string): string[] {
  // --local mode: scan all entity files for those with _unsyncedEdits:true in
  // detailsJson. Used when local bots write to disk but haven't git-committed yet.
  if (LOCAL) {
    console.log('[diff] --local mode: scanning for _unsyncedEdits:true files')
    const dirty: string[] = []
    walkDir(ENTITIES_DIR, filePath => {
      if (!filePath.endsWith('.json')) return
      try {
        const raw = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as { entities?: Array<Record<string, unknown>> }
        const entities = raw.entities || []
        const hasDirty = entities.some(e => {
          if (e._unsyncedEdits) return true
          if (typeof e.detailsJson === 'string') {
            try {
              const dj = JSON.parse(e.detailsJson) as Record<string, unknown>
              return dj._unsyncedEdits === true || (Array.isArray(dj._editLog) && (dj._editLog as unknown[]).length > 0)
            } catch { return false }
          }
          return false
        })
        if (hasDirty) dirty.push(filePath)
      } catch { /* skip unparseable */ }
    })
    console.log(`[diff] --local found ${dirty.length} dirty files`)
    return dirty
  }

  if (!lastCommit || FULL) {
    if (FULL) console.log('[diff] --full mode: scanning ALL entity files')
    else console.log('[diff] no last_sync commit recorded; scanning ALL entity files')
    const out: string[] = []
    walkDir(ENTITIES_DIR, p => {
      if (p.endsWith('.json')) out.push(p)
    })
    return out
  }
  let changed: string[]
  try {
    const raw = execSync(
      `git -C ${ROOT} diff --name-only --diff-filter=AMR ${lastCommit} HEAD -- data/appwrite-export/entities/`,
      { encoding: 'utf-8' }
    )
    changed = raw.split('\n').map(s => s.trim()).filter(Boolean)
  } catch (e) {
    console.warn(`[diff] git diff failed (${(e as Error).message}); falling back to full scan`)
    const out: string[] = []
    walkDir(ENTITIES_DIR, p => {
      if (p.endsWith('.json')) out.push(p)
    })
    return out
  }
  return changed
    .filter(p => p.startsWith('data/appwrite-export/entities/') && p.endsWith('.json'))
    .map(p => path.join(ROOT, p))
}

function walkDir(dir: string, cb: (p: string) => void): void {
  if (!fs.existsSync(dir)) return
  for (const name of fs.readdirSync(dir)) {
    const p = path.join(dir, name)
    const st = fs.statSync(p)
    if (st.isDirectory()) walkDir(p, cb)
    else cb(p)
  }
}

function currentCommit(): string {
  try {
    return execSync(`git -C ${ROOT} rev-parse HEAD`, { encoding: 'utf-8' }).trim()
  } catch {
    return ''
  }
}

// ── Appwrite REST ──
async function patchDoc(coll: string, docId: string, data: Record<string, unknown>):
  Promise<{ ok: boolean; status: number; body?: unknown }> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${coll}/documents/${docId}`
  const res = await fetch(url, {
    method: 'PATCH', headers: headers(),
    body: JSON.stringify({ data }),
  })
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    return { ok: false, status: res.status, body }
  }
  return { ok: true, status: 200 }
}

async function postDoc(coll: string, docId: string, data: Record<string, unknown>):
  Promise<{ ok: boolean; status: number; body?: unknown }> {
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${coll}/documents`
  const res = await fetch(url, {
    method: 'POST', headers: headers(),
    body: JSON.stringify({ documentId: docId, data }),
  })
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    return { ok: false, status: res.status, body }
  }
  return { ok: true, status: 200 }
}

/** Query Appwrite for the real $id of a document whose slug attribute equals `slug`. */
async function findDocIdBySlug(coll: string, slug: string): Promise<string | null> {
  // Appwrite 1.5+ query format: JSON-serialized Query object
  const query = JSON.stringify({ method: 'equal', attribute: 'slug', values: [slug] })
  const url = `${ENDPOINT}/databases/${DATABASE_ID}/collections/${coll}/documents?queries[]=${encodeURIComponent(query)}&limit=1`
  const res = await fetch(url, { method: 'GET', headers: headers() })
  if (!res.ok) return null
  const body = await res.json().catch(() => null)
  const docs = body?.documents ?? []
  return docs.length > 0 ? (docs[0].$id as string) : null
}

// ── Entity payload ──
function entityToPayload(e: Entity): Record<string, unknown> {
  // Re-stringify detailsJson but strip _editLog (it's been emitted to audit_log)
  let dj: Record<string, unknown> = {}
  if (typeof e.detailsJson === 'string' && e.detailsJson) {
    try { dj = JSON.parse(e.detailsJson) } catch { dj = {} }
  } else if (e.detailsJson && typeof e.detailsJson === 'object') {
    // Shallow-copy to avoid mutating ent.detailsJson — mutation would destroy
    // _editLog before audit emission can read it.
    dj = { ...(e.detailsJson as Record<string, unknown>) }
  }
  delete dj._editLog
  delete dj._unsyncedEdits

  const out: Record<string, unknown> = {}
  const allowed = [
    'slug', 'name', 'label', 'callNumber', 'era', 'eraSlug', 'eraDivision',
    'eraDivisionCode', 'region', 'continent', 'status', 'born', 'died',
    'founded', 'period', 'wikidataQid', 'wikipediaUrl', 'imageUrl',
    'subjectHeadings', 'subjects', 'frameworks', 'summary', 'importanceScore',
  ]
  for (const k of allowed) if (e[k] !== undefined) out[k] = e[k]
  out.detailsJson = JSON.stringify(dj)
  return out
}

// ── Audit log emission ──
async function emitAuditRow(entity: Entity, log: EditLogEntry): Promise<boolean> {
  const docId = crypto.randomUUID()
  const r = await postDoc('audit_log', docId, {
    entityId: (entity.$id as string) || slugToId(entity.slug || ''),
    entitySlug: entity.slug || '',
    entityName: entity.name || entity.slug || '',
    action: 'update',
    field: log.field,
    oldValue: typeof log.oldValue === 'string' ? log.oldValue : (JSON.stringify(log.oldValue) ?? '').slice(0, 1000),
    newValue: typeof log.newValue === 'string' ? log.newValue : (JSON.stringify(log.newValue) ?? '').slice(0, 1000),
    editorId: log.editorId,
    editorNote: 'replayed by sync_gateway from _editLog',
    timestamp: log.timestamp,
    sessionId: process.env.GITHUB_RUN_ID
      ? `sync-gateway·cloud·GH#${process.env.GITHUB_RUN_ID}`
      : `sync-gateway·local·${Date.now()}`,
  })
  return r.ok
}

// ── Main ──
async function main(): Promise<void> {
  console.log('=== sync_gateway: git → Appwrite ===')
  console.log(`Endpoint:  ${ENDPOINT}`)
  console.log(`Database:  ${DATABASE_ID}`)
  console.log(`Source:    ${EXPORT_DIR}`)
  if (DRY_RUN) console.log('MODE:      DRY RUN (no writes, no API calls)')
  if (LOCAL) console.log('MODE:      LOCAL (dirty-file scan — no git commit needed)')

  const budget = loadBudget()
  const lastSync = fs.existsSync(LAST_SYNC_FILE)
    ? loadJson<LastSync>(LAST_SYNC_FILE)
    : { lastSyncedCommit: '', lastRunAt: '', lastRunStatus: '', lastRunStats: {} }

  const perRunCap = MAX_OVERRIDE ?? budget.perRunWriteCap
  console.log(`[budget] perRunWriteCap=${perRunCap} writesUsed=${budget.current.writesUsed}/${budget.monthlyWriteCap} (hardStop=${budget.hardStopPercent}%)`)

  const gate = checkBudget(budget, 0)
  if (!gate.ok) {
    console.error(`[budget] BLOCKED: ${gate.reason}`)
    process.exit(2)
  }

  const files = changedEntityFiles(lastSync.lastSyncedCommit)
  console.log(`[diff] ${files.length} entity files to sync`)

  let entitiesUpserted = 0
  let auditRowsEmitted = 0
  let writesPerformed = 0
  let stoppedReason = ''
  const headCommit = currentCommit()

  outer: for (const file of files) {
    let data: { entities?: Entity[] }
    try {
      data = JSON.parse(fs.readFileSync(file, 'utf-8'))
    } catch {
      console.warn(`[skip] unparseable: ${file}`)
      continue
    }
    const entities = data.entities || []
    for (const ent of entities) {
      if (!ent.slug) continue
      // In --local mode only process entities that are actually dirty.
      // The dirty flag can live at the top level OR inside detailsJson — ai_enrich
      // writes it nested, so we MUST check both. (Previously this only checked
      // ent._unsyncedEdits, causing 499 enriched entities to silently skip.)
      if (LOCAL) {
        let dirty = ent._unsyncedEdits === true
        if (!dirty && typeof ent.detailsJson === 'string') {
          try {
            const dj = JSON.parse(ent.detailsJson) as Record<string, unknown>
            dirty = dj._unsyncedEdits === true
              || (Array.isArray(dj._editLog) && (dj._editLog as unknown[]).length > 0)
          } catch { /* ignore */ }
        } else if (!dirty && ent.detailsJson && typeof ent.detailsJson === 'object') {
          const dj = ent.detailsJson as Record<string, unknown>
          dirty = dj._unsyncedEdits === true
            || (Array.isArray(dj._editLog) && (dj._editLog as unknown[]).length > 0)
        }
        if (!dirty) continue
      }
      // Per-run cap
      if (writesPerformed >= perRunCap) {
        stoppedReason = `perRunWriteCap=${perRunCap} reached`
        break outer
      }
      // Budget check before each write
      const g = checkBudget(budget, writesPerformed + 1)
      if (!g.ok) { stoppedReason = g.reason || 'budget exceeded'; break outer }

      const docId = (ent.$id as string) || slugToId(ent.slug)
      const payload = entityToPayload(ent)

      if (DRY_RUN) {
        console.log(`[dry] would PATCH entities/${docId} (${ent.slug})`)
        entitiesUpserted++
      } else {
        // Upsert strategy:
        //  1. PATCH by $id (fastest — most entities already exist)
        //  2. If 404 and docId ≠ slug: PATCH by slug (some docs use slug as Appwrite $id)
        //  3. If still 404: POST (new entity)
        //  4. If POST returns 409 (slug unique-key conflict): document exists with a UUID $id
        //     → query Appwrite by slug to get the real $id → PATCH by real $id
        let r = await patchDoc('entities', docId, payload)
        if (!r.ok && r.status === 404 && docId !== ent.slug) {
          r = await patchDoc('entities', ent.slug!, payload)
        }
        if (!r.ok && r.status === 404) {
          r = await postDoc('entities', docId, payload)
        }
        if (!r.ok && r.status === 409) {
          // Entity exists in Appwrite with a UUID $id, not the slug as $id.
          // Query to find the real $id, then PATCH.
          const realId = await findDocIdBySlug('entities', ent.slug!)
          if (realId) {
            r = await patchDoc('entities', realId, payload)
          } else {
            // Fallback: try slug directly (rare legacy case)
            r = await patchDoc('entities', ent.slug!, payload)
          }
        }
        if (r.ok) {
          entitiesUpserted++
          writesPerformed++
          budget.current.writesUsed++
        } else {
          console.warn(`[fail] ${ent.slug}: HTTP ${r.status}`, r.body)
          continue
        }
        await sleep(budget.minMsBetweenWrites)
      }

      // Replay _editLog → audit_log
      let dj: Record<string, unknown> = {}
      if (typeof ent.detailsJson === 'string' && ent.detailsJson) {
        try { dj = JSON.parse(ent.detailsJson) } catch { /* */ }
      } else if (ent.detailsJson && typeof ent.detailsJson === 'object') {
        dj = ent.detailsJson as Record<string, unknown>
      }
      const log = (dj._editLog as EditLogEntry[] | undefined) || []
      for (const entry of log) {
        if (writesPerformed >= perRunCap) {
          stoppedReason = `perRunWriteCap=${perRunCap} reached during audit emission`
          break outer
        }
        if (DRY_RUN) {
          console.log(`[dry] would POST audit_log: ${ent.slug} ${entry.field}`)
          auditRowsEmitted++
        } else {
          const ok = await emitAuditRow(ent, entry)
          if (ok) {
            auditRowsEmitted++
            writesPerformed++
            budget.current.writesUsed++
            await sleep(budget.minMsBetweenWrites)
          }
        }
      }

      // Clear _editLog and dirty flags from local file (real run only)
      if (!DRY_RUN) {
        dj._editLog = []
        delete dj._unsyncedEdits
        ent.detailsJson = JSON.stringify(dj)
        // Also clear the top-level entity flag — without this the --local scanner
        // re-detects the file as dirty on every subsequent run.
        delete (ent as Record<string, unknown>)._unsyncedEdits
      }
    }

    // Persist cleared _editLog back to file
    if (!DRY_RUN) {
      fs.writeFileSync(file, JSON.stringify(data, null, 2) + '\n', 'utf-8')
    }
  }

  // ── Persist state ──
  const stats = {
    filesChanged: files.length,
    entitiesUpserted,
    auditRowsEmitted,
    writesPerformed,
    stoppedReason,
  }
  console.log('\n=== Summary ===')
  console.log(JSON.stringify(stats, null, 2))

  if (!DRY_RUN) {
    budget.current.lastUpdated = new Date().toISOString()
    saveBudget(budget)
    saveJson(LAST_SYNC_FILE, {
      lastSyncedCommit: headCommit,
      lastRunAt: new Date().toISOString(),
      lastRunStatus: stoppedReason ? 'partial' : 'ok',
      lastRunStats: stats,
    })
    console.log(`[state] last_sync.json updated → commit ${headCommit.slice(0, 8)}`)
  }
}

main().catch(err => {
  console.error('[fatal]', err)
  process.exit(1)
})
