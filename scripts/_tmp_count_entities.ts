#!/usr/bin/env npx tsx
/** One-shot accurate entity page-count + stats_cache rewrite (local). */
import * as fs from 'fs'
import * as path from 'path'
import { Client, Databases, Query, ID, Permission, Role } from 'node-appwrite'

const ROOT = path.resolve(__dirname, '..')
function loadDotEnv(filePath: string) {
  if (!fs.existsSync(filePath)) return
  for (const line of fs.readFileSync(filePath, 'utf8').split('\n')) {
    const t = line.trim()
    if (!t || t.startsWith('#') || !t.includes('=')) continue
    const i = t.indexOf('=')
    const k = t.slice(0, i).trim()
    const v = t.slice(i + 1).trim().replace(/^['"]|['"]$/g, '')
    if (k && !(k in process.env)) process.env[k] = v
  }
}
loadDotEnv(path.join(ROOT, '.env'))
loadDotEnv(path.join(ROOT, 'ui/.env'))

const ENDPOINT = process.env.VITE_APPWRITE_ENDPOINT || 'http://localhost:8080/v1'
const PROJECT = process.env.VITE_APPWRITE_PROJECT_ID || 'annals-local'
const DATABASE = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_world_db'
const KEY = process.env.APPWRITE_API_KEY || ''
if (!KEY) {
  console.error('missing APPWRITE_API_KEY')
  process.exit(1)
}

const client = new Client().setEndpoint(ENDPOINT).setProject(PROJECT).setKey(KEY)
const databases = new Databases(client)

async function main() {
  const t0 = Date.now()
  const byLabel: Record<string, number> = {}
  const byEra: Record<string, number> = {}
  const byContinent: Record<string, number> = {}
  const byClass: Record<string, number> = {}
  let total = 0
  let cursor: string | undefined

  while (true) {
    const queries = [
      Query.limit(100),
      Query.select(['label', 'era', 'continent', 'callNumber']),
    ]
    if (cursor) queries.push(Query.cursorAfter(cursor))
    const page = await databases.listDocuments(DATABASE, 'entities', queries)
    const docs = page.documents || []
    if (!docs.length) break
    for (const doc of docs) {
      total++
      const label = String((doc as { label?: string }).label || 'Unknown')
      const era = String((doc as { era?: string }).era || 'Unknown')
      const continent = String((doc as { continent?: string }).continent || 'Unknown')
      const cn = String((doc as { callNumber?: string }).callNumber || '')
      byLabel[label] = (byLabel[label] || 0) + 1
      byEra[era] = (byEra[era] || 0) + 1
      byContinent[continent] = (byContinent[continent] || 0) + 1
      if (cn && /^\d/.test(cn)) byClass[cn[0]] = (byClass[cn[0]] || 0) + 1
    }
    cursor = docs[docs.length - 1].$id
    if (total % 25000 === 0) console.log(`… ${total} (${Date.now() - t0}ms)`)
    if (docs.length < 100) break
  }

  const computeTimeMs = Date.now() - t0
  const updatedAt = new Date().toISOString()
  const seed = JSON.parse(
    fs.readFileSync(path.join(ROOT, 'data/governance/seed_local_cursor.json'), 'utf8'),
  )
  const payload = {
    total,
    byLabel,
    byEra,
    byContinent,
    byClass,
    updatedAt,
    computeTimeMs,
    note: 'paged entity count (ignores API total cap)',
    source: 'local-appwrite',
    endpoint: ENDPOINT,
    project: PROJECT,
    database: DATABASE,
    seedCursor: {
      scanned: seed.scanned,
      created: seed.created,
      skipped: seed.skipped,
      failed: seed.failed,
      classDir: seed.classDir,
      file: seed.file,
      lastRunAt: seed.lastRunAt,
    },
  }

  for (const rel of ['data/governance/stats_cache.json', 'ui/public/governance/stats_cache.json']) {
    const p = path.join(ROOT, rel)
    fs.mkdirSync(path.dirname(p), { recursive: true })
    fs.writeFileSync(p, JSON.stringify(payload, null, 2) + '\n')
    console.log('wrote', rel, 'total=', total)
  }

  await databases.createDocument(
    DATABASE,
    'stats_cache',
    ID.unique(),
    {
      total,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt,
      computeTimeMs,
    },
    [Permission.read(Role.any())],
  )
  console.log(`ACCURATE_TOTAL=${total} computeTimeMs=${computeTimeMs}`)
}

main().catch((e) => {
  console.error(e)
  process.exit(1)
})
