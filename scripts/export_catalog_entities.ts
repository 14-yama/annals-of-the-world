/**
 * export_catalog_entities.ts — Export ALL_CATALOG_ENTITIES to JSON
 * for seeding to Appwrite backend.
 *
 * Pre-requisite: Run Python slug extraction first:
 *   python3 -c "..." → data/.existing_slugs.json
 *
 * Usage: npx tsx scripts/export_catalog_entities.ts
 *
 * Outputs: data/catalog_entities.json (entities NOT in wikidata JSON files)
 */
import { ALL_CATALOG_ENTITIES } from '../ui/src/data/catalog/index'
import * as fs from 'fs'
import * as path from 'path'

const dataDir = path.resolve(__dirname, '..', 'data')
const outPath = path.join(dataDir, 'catalog_entities.json')
const slugsPath = path.join(dataDir, '.existing_slugs.json')

// Load pre-built slug set (from Python extraction — handles 818 MB files)
if (!fs.existsSync(slugsPath)) {
  console.error('ERROR: data/.existing_slugs.json not found. Run Python slug extraction first.')
  process.exit(1)
}
const existingSlugs = new Set<string>(JSON.parse(fs.readFileSync(slugsPath, 'utf-8')))

console.log(`Existing slugs in wikidata JSON: ${existingSlugs.size.toLocaleString()}`)
console.log(`Total catalog entities: ${ALL_CATALOG_ENTITIES.length.toLocaleString()}`)

// Separate: entities NOT in wikidata JSON vs those that overlap (for updating)
const missing = ALL_CATALOG_ENTITIES.filter(e => !existingSlugs.has(e.slug))
const overlapping = ALL_CATALOG_ENTITIES.filter(e => existingSlugs.has(e.slug))

// Only export overlapping entities that are "richer" (3+ relationships)
const richOverlap = overlapping.filter(e => e.relationships.length >= 3)

console.log(`Missing from backend: ${missing.length.toLocaleString()}`)
console.log(`Overlapping with richer data (3+ rels): ${richOverlap.length.toLocaleString()}`)

const allToExport = [...missing, ...richOverlap]

// Write as JSON (matching wikidata format)
const output = {
  source: 'catalog_export',
  exportedAt: new Date().toISOString(),
  count: allToExport.length,
  missingCount: missing.length,
  updateCount: richOverlap.length,
  entities: allToExport.map(e => ({
    _action: existingSlugs.has(e.slug) ? 'update' : 'create',
    slug: e.slug,
    name: e.name,
    label: e.label,
    callNumber: e.callNumber,
    summary: e.summary,
    era: e.era,
    eraSlug: e.eraSlug,
    region: e.region || '',
    continent: e.continent || '',
    status: e.status || 'Published',
    born: (e as any).born || '',
    died: (e as any).died || '',
    founded: (e as any).founded || '',
    period: (e as any).period || '',
    startDate: (e as any).startDate || (e as any).born || '',
    endDate: (e as any).endDate || (e as any).died || '',
    subjectHeadings: e.subjectHeadings || [],
    subjects: e.subjects || [],
    frameworks: e.frameworks || [],
    altNames: (e as any).altNames || [],
    wikidataQid: (e as any).wikidataQid || '',
    wikipediaUrl: (e as any).wikipediaUrl || '',
    imageUrl: (e as any).imageUrl || (e as any).thumbnailUrl || '',
    importanceScore: (e as any).importanceScore || null,
    causes: e.causes || [],
    effects: e.effects || [],
    relationships: e.relationships || [],
    places: e.places || [],
    texts: e.texts || [],
    externalLinks: (e as any).externalLinks || [],
    tags: (e as any).tags || [],
    thumbnailUrl: (e as any).thumbnailUrl || '',
    quote: (e as any).quote || '',
    legacySummary: (e as any).legacySummary || '',
  })),
}

fs.writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf-8')
console.log(`\nWritten to: ${outPath}`)
console.log(`File size: ${(fs.statSync(outPath).size / 1024 / 1024).toFixed(1)} MB`)

// Stats
const byLabel: Record<string, number> = {}
const byEra: Record<string, number> = {}
for (const e of allToExport) {
  byLabel[e.label] = (byLabel[e.label] || 0) + 1
  byEra[e.era] = (byEra[e.era] || 0) + 1
}
console.log('\nBy label:')
for (const [k, v] of Object.entries(byLabel).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${k}: ${v}`)
}
console.log('\nBy era:')
for (const [k, v] of Object.entries(byEra).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${k}: ${v}`)
}
