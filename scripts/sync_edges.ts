#!/usr/bin/env npx tsx
/**
 * sync_edges.ts — Push edge records from data/appwrite-export/edges/ to Appwrite.
 *
 * Reads dated edge JSON files produced by ai_edge_bot.py, upserts each edge
 * into the Appwrite 'relationships' collection, then marks files as synced.
 * Respects the same budget limits as sync_gateway.ts.
 *
 * Usage:
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_edges.ts
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_edges.ts --dry-run
 *   APPWRITE_API_KEY=<key> npx tsx scripts/sync_edges.ts --max=100
 */
import * as fs from 'fs'
import * as path from 'path'

const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT    || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID  || '66509ba7003618a05af6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const API_KEY     = process.env.APPWRITE_API_KEY

const ROOT      = path.resolve(__dirname, '..')
const EDGES_DIR = path.join(ROOT, 'data', 'appwrite-export', 'edges')
const BUDGET_FILE = path.join(ROOT, 'data', 'governance', 'budget.json')

const args = process.argv.slice(2)
const DRY_RUN = args.includes('--dry-run')
const maxArg  = args.find(a => a.startsWith('--max='))
const MAX_OVERRIDE = maxArg ? parseInt(maxArg.split('=')[1], 10) : undefined

if (!API_KEY && !DRY_RUN) {
  console.error('ERROR: Set APPWRITE_API_KEY env var')
  process.exit(1)
}

interface Budget {
  monthlyWriteCap: number
  perRunWriteCap: number
  hardStopPercent: number
  manualPause: boolean
  current: { writesUsed: number }
}

interface Edge {
  $id: string
  entitySlug: string
  sourceSlug: string
  sourceName?: string
  verb: string
  targetSlug: string
  targetName?: string
  context?: string
  _source?: string
  _synced?: boolean
}

function loadBudget(): Budget {
  try { return JSON.parse(fs.readFileSync(BUDGET_FILE, 'utf-8')) }
  catch { return { monthlyWriteCap: 100000, perRunWriteCap: 500, hardStopPercent: 80, manualPause: false, current: { writesUsed: 0 } } }
}

function sleep(ms: number) { return new Promise(r => setTimeout(r, ms)) }

async function appwriteRequest(method: string, urlPath: string, body?: object): Promise<any> {
  const url = `${ENDPOINT}${urlPath}`
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    'X-Appwrite-Project': PROJECT_ID,
    'X-Appwrite-Key': API_KEY!,
  }
  const opts: RequestInit = { method, headers }
  if (body) opts.body = JSON.stringify(body)
  const resp = await fetch(url, opts)
  const text = await resp.text()
  if (!resp.ok && resp.status !== 404 && resp.status !== 409) {
    throw new Error(`HTTP ${resp.status}: ${text.slice(0, 200)}`)
  }
  return { status: resp.status, body: text ? JSON.parse(text) : {} }
}

async function upsertEdge(edge: Edge): Promise<'created' | 'updated' | 'skipped'> {
  const docId   = edge.$id.replace(/[|]/g, '__')   // Appwrite $id safe chars
  const colPath = `/databases/${DATABASE_ID}/collections/relationships/documents`
  const payload = {
    entitySlug: edge.entitySlug,
    sourceSlug: edge.sourceSlug,
    sourceName: edge.sourceName || edge.sourceSlug,
    verb:       edge.verb,
    targetSlug: edge.targetSlug,
    targetName: edge.targetName || edge.targetSlug,
    context:    edge.context || '',
  }

  // Try PATCH first (update)
  const patch = await appwriteRequest('PATCH', `${colPath}/${docId}`, { data: payload })
  if (patch.status === 200) return 'updated'

  // 404 → create
  const post = await appwriteRequest('POST', colPath, { documentId: docId, data: payload })
  if (post.status === 201) return 'created'

  // 409 → already exists with different $id — update by querying
  return 'skipped'
}

async function main() {
  const budget = loadBudget()
  const cap = MAX_OVERRIDE ?? budget.perRunWriteCap
  const hardStop = Math.floor(budget.monthlyWriteCap * budget.hardStopPercent / 100)
  const used = budget.current.writesUsed

  console.log('=== sync_edges: git → Appwrite relationships ===')
  console.log(`[budget] perRunCap=${cap} writesUsed=${used}/${budget.monthlyWriteCap} (hardStop=${budget.hardStopPercent}%)`)

  if (budget.manualPause) {
    console.log('[budget] manualPause=true — aborting')
    return
  }
  if (used >= hardStop) {
    console.log(`[budget] hard stop reached (${used} >= ${hardStop}) — aborting`)
    return
  }

  if (!fs.existsSync(EDGES_DIR)) {
    console.log('No edges directory found — nothing to sync')
    return
  }

  const files = fs.readdirSync(EDGES_DIR)
    .filter(f => f.endsWith('.json') && !f.startsWith('_'))
    .sort()

  let totalEdges = 0; let totalCreated = 0; let totalUpdated = 0; let writesThisRun = 0

  for (const file of files) {
    const fp = path.join(EDGES_DIR, file)
    let data: any
    try { data = JSON.parse(fs.readFileSync(fp, 'utf-8')) } catch { continue }
    if (!data._unsyncedEdits) continue

    const edges: Edge[] = data.edges || []
    const unsynced = edges.filter(e => !e._synced)
    if (!unsynced.length) continue

    console.log(`\n[file] ${file} — ${unsynced.length} unsynced edges`)

    for (const edge of unsynced) {
      if (writesThisRun >= cap || used + writesThisRun >= hardStop) {
        console.log(`[budget] cap reached (${writesThisRun}/${cap}) — stopping`)
        break
      }

      if (DRY_RUN) {
        console.log(`  [dry] ${edge.sourceSlug} --${edge.verb}--> ${edge.targetSlug}`)
        totalEdges++
        continue
      }

      try {
        const result = await upsertEdge(edge)
        edge._synced = true
        writesThisRun++
        totalEdges++
        if (result === 'created') totalCreated++
        else if (result === 'updated') totalUpdated++
        console.log(`  [${result}] ${edge.sourceSlug} --${edge.verb}--> ${edge.targetSlug}`)
        await sleep(250)
      } catch (err: any) {
        console.error(`  [error] ${edge.$id}: ${err.message}`)
      }
    }

    // Mark file as synced if all edges processed
    if (!DRY_RUN) {
      const allSynced = edges.every(e => e._synced)
      data._unsyncedEdits = !allSynced
      data.lastSyncedAt = new Date().toISOString()
      fs.writeFileSync(fp, JSON.stringify(data, null, 2) + '\n')
    }
  }

  // Update budget
  if (!DRY_RUN && writesThisRun > 0) {
    budget.current.writesUsed += writesThisRun
    budget.current.lastUpdated = new Date().toISOString()
    fs.writeFileSync(BUDGET_FILE, JSON.stringify(budget, null, 2) + '\n')
  }

  console.log(`\n=== Summary ===`)
  console.log(JSON.stringify({ edgesProcessed: totalEdges, created: totalCreated, updated: totalUpdated, writesPerformed: writesThisRun }, null, 2))
}

main().catch(err => { console.error(err); process.exit(1) })
