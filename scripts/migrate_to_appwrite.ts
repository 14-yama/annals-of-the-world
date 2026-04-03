#!/usr/bin/env npx tsx
/**
 * migrate_to_appwrite.ts
 *
 * Reads all 10,000+ entities from the static Annals Catalog and seeds them
 * into Appwrite Cloud as documents in the `entities` collection.
 *
 * Prerequisites:
 *   1. Create these collections in the Appwrite console (database: annals_db):
 *      - entities          (document-level permissions off)
 *      - relationships     (for future use)
 *      - causes_effects    (for future use)
 *      - places            (for future use)
 *      - texts             (for future use)
 *      - evidence          (for future use)
 *      - media             (for future use)
 *      - timeline_entries  (for future use)
 *
 *   2. Create these attributes on the `entities` collection:
 *      - slug           (string, 256, required, indexed)
 *      - name           (string, 512, required)
 *      - label          (string, 64, required)
 *      - callNumber     (string, 128, required, indexed)
 *      - summary        (string, 10000)
 *      - era            (string, 64, indexed)
 *      - eraSlug        (string, 64, indexed)
 *      - region         (string, 128)
 *      - continent      (string, 64, indexed)
 *      - status         (string, 32)
 *      - born           (string, 128)
 *      - died           (string, 128)
 *      - founded        (string, 128)
 *      - period         (string, 256)
 *      - startDate      (string, 128)
 *      - endDate        (string, 128)
 *      - subjectHeadings (string[])
 *      - subjects       (string[])
 *      - frameworks     (string[])
 *      - tags           (string[])
 *      - altNames       (string[])
 *      - externalLinks  (string[])
 *      - wikidataQid    (string, 32)
 *      - wikipediaUrl   (string, 512)
 *      - imageUrl       (string, 512)
 *      - thumbnailUrl   (string, 512)
 *      - importanceScore (float)
 *      - quote          (string, 2000)
 *      - legacySummary  (string, 5000)
 *      - causesJson     (string, 30000)  — JSON-stringified causes array
 *      - effectsJson    (string, 30000)  — JSON-stringified effects array
 *      - relationshipsJson (string, 30000) — JSON-stringified relationships array
 *      - placesJson     (string, 10000)  — JSON-stringified places array
 *      - textsJson      (string, 10000)  — JSON-stringified texts array
 *
 *   3. Create a full-text index on `name` for search queries.
 *
 *   4. Set an Appwrite API key in env: APPWRITE_API_KEY
 *
 * Usage:
 *   APPWRITE_API_KEY=<your-key> npx tsx scripts/migrate_to_appwrite.ts
 *
 * Dry-run (no writes):
 *   APPWRITE_API_KEY=<your-key> DRY_RUN=1 npx tsx scripts/migrate_to_appwrite.ts
 */

import sdk from 'node-appwrite'

// ── Config ──
const ENDPOINT   = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID = process.env.VITE_APPWRITE_PROJECT_ID  || '69cc45e3000d587ea5e6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_db'
const API_KEY     = process.env.APPWRITE_API_KEY
const DRY_RUN     = process.env.DRY_RUN === '1'
const COLLECTION  = 'entities'
const BATCH_SIZE  = 50   // concurrent writes per batch
const RETRY_LIMIT = 3
const RETRY_DELAY = 1000 // ms

if (!API_KEY && !DRY_RUN) {
  console.error('ERROR: Set APPWRITE_API_KEY env var (or use DRY_RUN=1)')
  process.exit(1)
}

// ── Appwrite client (server SDK) ──
const client = new sdk.Client()
client.setEndpoint(ENDPOINT).setProject(PROJECT_ID)
if (API_KEY) client.setKey(API_KEY)

const databases = new sdk.Databases(client)

// ── Load the catalog ──
// We dynamically import the UI catalog so we get the full deduped & enriched set.
async function loadEntities() {
  // tsx can import TypeScript directly
  const { ALL_CATALOG_ENTITIES } = await import('../ui/src/data/catalog/index')
  return ALL_CATALOG_ENTITIES
}

// ── Transform entity → Appwrite document data ──
function toDocument(entity: Record<string, unknown>) {
  const e = entity as Record<string, unknown>
  return {
    slug:             e.slug,
    name:             e.name,
    label:            e.label,
    callNumber:       e.callNumber,
    summary:          truncate(e.summary as string, 10000),
    era:              e.era || '',
    eraSlug:          e.eraSlug || '',
    region:           e.region || '',
    continent:        e.continent || '',
    status:           e.status || '',
    born:             e.born || null,
    died:             e.died || null,
    founded:          e.founded || null,
    period:           e.period || null,
    startDate:        e.startDate || null,
    endDate:          e.endDate || null,
    subjectHeadings:  e.subjectHeadings || [],
    subjects:         e.subjects || [],
    frameworks:       e.frameworks || [],
    altNames:         e.altNames || [],
    wikidataQid:      e.wikidataQid || null,
    wikipediaUrl:     e.wikipediaUrl || null,
    imageUrl:         e.imageUrl || null,
    importanceScore:  e.importanceScore ?? null,
    // Consolidated JSON blob for nested/overflow data
    detailsJson:      JSON.stringify({
      tags:           e.tags || [],
      externalLinks:  e.externalLinks || [],
      thumbnailUrl:   e.thumbnailUrl || null,
      quote:          truncate(e.quote as string, 2000) || null,
      legacySummary:  truncate(e.legacySummary as string, 5000) || null,
      causes:         e.causes || [],
      effects:        e.effects || [],
      relationships:  e.relationships || [],
      places:         e.places || [],
      texts:          e.texts || [],
    }),
  }
}

function truncate(s: string | undefined | null, max: number): string {
  if (!s) return ''
  return s.length > max ? s.slice(0, max - 3) + '...' : s
}

/** Generate a deterministic document ID from slug (Appwrite IDs: [a-zA-Z0-9_-], max 36) */
function toDocId(slug: string): string {
  const clean = slug.replace(/[^a-zA-Z0-9_-]/g, '_')
  // Ensure it doesn't start with a special char
  const safe = clean.replace(/^[_-]+/, '')
  if (safe.length <= 36 && safe.length > 0) return safe
  // Long slugs: use first 27 chars + '_' + 8-char hash for uniqueness
  const hash = djb2(slug).toString(36).replace(/[^a-zA-Z0-9]/g, '').padStart(8, '0').slice(0, 8)
  const prefix = safe.slice(0, 27).replace(/[_-]+$/, '')
  return (prefix + '_' + hash).slice(0, 36)
}

/** Simple djb2 hash → unsigned 32-bit integer */
function djb2(s: string): number {
  let h = 5381
  for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0
  return h
}

async function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

async function createWithRetry(docId: string, data: Record<string, unknown>, attempt = 1): Promise<boolean> {
  try {
    await databases.createDocument(DATABASE_ID, COLLECTION, docId, data)
    return true
  } catch (err: unknown) {
    const error = err as { code?: number; message?: string }
    // 409 = document already exists → skip
    if (error.code === 409) return false
    if (attempt < RETRY_LIMIT) {
      await sleep(RETRY_DELAY * attempt)
      return createWithRetry(docId, data, attempt + 1)
    }
    throw err
  }
}

// ── Main ──
async function main() {
  console.log('Loading Annals Catalog...')
  const entities = await loadEntities()
  console.log(`Loaded ${entities.length} entities`)

  if (DRY_RUN) {
    console.log('\n=== DRY RUN — no documents will be created ===\n')
    // Show a sample
    const sample = entities.slice(0, 3)
    for (const e of sample) {
      const doc = toDocument(e as unknown as Record<string, unknown>)
      console.log(`  [${doc.callNumber}] ${doc.name} (${doc.label}) — ${doc.era}`)
    }
    console.log(`  ... and ${entities.length - 3} more`)
    console.log('\nTo run for real: remove DRY_RUN=1')
    return
  }

  let created = 0
  let skipped = 0
  let failed = 0
  const errors: string[] = []

  // Process in batches
  for (let i = 0; i < entities.length; i += BATCH_SIZE) {
    const batch = entities.slice(i, i + BATCH_SIZE)
    const results = await Promise.allSettled(
      batch.map(async (entity) => {
        const e = entity as unknown as Record<string, unknown>
        const docId = toDocId(e.slug as string)
        const data = toDocument(e)
        const wasCreated = await createWithRetry(docId, data)
        return { slug: e.slug as string, wasCreated }
      }),
    )

    for (const result of results) {
      if (result.status === 'fulfilled') {
        if (result.value.wasCreated) created++
        else skipped++
      } else {
        failed++
        const reason = result.reason?.message || String(result.reason)
        errors.push(reason)
      }
    }

    // Progress log every 500
    const progress = Math.min(i + BATCH_SIZE, entities.length)
    if (progress % 500 === 0 || progress === entities.length) {
      console.log(`  Progress: ${progress}/${entities.length} (created: ${created}, skipped: ${skipped}, failed: ${failed})`)
    }

    // Rate limit: short pause between batches
    if (i + BATCH_SIZE < entities.length) {
      await sleep(200)
    }
  }

  console.log('\n=== Migration Complete ===')
  console.log(`  Created:  ${created}`)
  console.log(`  Skipped:  ${skipped} (already exist)`)
  console.log(`  Failed:   ${failed}`)

  if (errors.length > 0) {
    console.log('\nFirst 10 errors:')
    errors.slice(0, 10).forEach(e => console.log(`  - ${e}`))
  }
}

main().catch((err) => {
  console.error('Migration failed:', err)
  process.exit(1)
})
