#!/usr/bin/env npx tsx
/**
 * setup_appwrite.ts — Create database, collections, attributes, and indexes
 *
 * Idempotent: skips resources that already exist (409 errors).
 *
 * Usage:
 *   APPWRITE_API_KEY=<your-key> npx tsx scripts/setup_appwrite.ts
 *
 * Optional env overrides:
 *   VITE_APPWRITE_ENDPOINT    (default: https://fra.cloud.appwrite.io/v1)
 *   VITE_APPWRITE_PROJECT_ID  (default: 69cc45e3000d587ea5e6)
 *   VITE_APPWRITE_DATABASE_ID (default: annals_db)
 */

import sdk from 'node-appwrite'

// ── Config ──
const ENDPOINT    = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID  = process.env.VITE_APPWRITE_PROJECT_ID || '69cc45e3000d587ea5e6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_db'
const API_KEY     = process.env.APPWRITE_API_KEY

if (!API_KEY) {
  console.error('ERROR: Set APPWRITE_API_KEY env var')
  process.exit(1)
}

const client = new sdk.Client()
client.setEndpoint(ENDPOINT).setProject(PROJECT_ID).setKey(API_KEY)

const databases = new sdk.Databases(client)

// ── Helpers ──

async function safe(label: string, fn: () => Promise<unknown>) {
  try {
    await fn()
    console.log(`  ✓ ${label}`)
  } catch (err: unknown) {
    const e = err as { code?: number; message?: string }
    if (e.code === 409 || (e.message && e.message.includes('maximum'))) {
      console.log(`  – ${label} (already exists)`)
    } else {
      console.error(`  ✗ ${label}: ${e.message}`)
      throw err
    }
  }
}

async function sleep(ms: number) {
  return new Promise(r => setTimeout(r, ms))
}

// Short pause between attribute creations to avoid Appwrite rate limits
const ATTR_DELAY = 300

// ── Schema Definitions ──

interface AttrDef {
  key: string
  type: 'string' | 'integer' | 'float' | 'boolean' | 'string[]'
  size?: number
  required?: boolean
  default_?: string | number | boolean | string[] | null
}

interface CollectionDef {
  id: string
  name: string
  attrs: AttrDef[]
  indexes: { key: string; type: 'key' | 'fulltext' | 'unique'; attrs: string[] }[]
}

const COLLECTIONS: CollectionDef[] = [
  {
    id: 'entities',
    name: 'Entities',
    attrs: [
      { key: 'slug',            type: 'string',   size: 256,   required: true },
      { key: 'name',            type: 'string',   size: 512,   required: true },
      { key: 'label',           type: 'string',   size: 64,    required: true },
      { key: 'callNumber',      type: 'string',   size: 128,   required: true },
      { key: 'summary',         type: 'string',   size: 10000 },
      { key: 'era',             type: 'string',   size: 64 },
      { key: 'eraSlug',         type: 'string',   size: 64 },
      { key: 'region',          type: 'string',   size: 128 },
      { key: 'continent',       type: 'string',   size: 64 },
      { key: 'status',          type: 'string',   size: 32 },
      { key: 'born',            type: 'string',   size: 128 },
      { key: 'died',            type: 'string',   size: 128 },
      { key: 'founded',         type: 'string',   size: 128 },
      { key: 'period',          type: 'string',   size: 256 },
      { key: 'startDate',       type: 'string',   size: 128 },
      { key: 'endDate',         type: 'string',   size: 128 },
      { key: 'subjectHeadings', type: 'string[]', size: 512 },
      { key: 'subjects',        type: 'string[]', size: 256 },
      { key: 'frameworks',      type: 'string[]', size: 128 },
      { key: 'altNames',        type: 'string[]', size: 256 },
      { key: 'wikidataQid',     type: 'string',   size: 32 },
      { key: 'wikipediaUrl',    type: 'string',   size: 512 },
      { key: 'imageUrl',        type: 'string',   size: 512 },
      { key: 'importanceScore', type: 'float' },
      // Consolidated JSON blob: causes, effects, relationships, places, texts, quote, legacySummary, tags, externalLinks
      { key: 'detailsJson',     type: 'string',   size: 100000 },
    ],
    indexes: [
      { key: 'idx_slug',       type: 'unique',   attrs: ['slug'] },
      { key: 'idx_callNumber', type: 'key',      attrs: ['callNumber'] },
      { key: 'idx_era',        type: 'key',      attrs: ['eraSlug'] },
      { key: 'idx_label',      type: 'key',      attrs: ['label'] },
      { key: 'idx_continent',  type: 'key',      attrs: ['continent'] },
      { key: 'idx_search',     type: 'fulltext', attrs: ['name'] },
    ],
  },
  {
    id: 'relationships',
    name: 'Relationships',
    attrs: [
      { key: 'sourceSlug',  type: 'string', size: 256, required: true },
      { key: 'sourceName',  type: 'string', size: 512 },
      { key: 'verb',        type: 'string', size: 64,  required: true },
      { key: 'targetSlug',  type: 'string', size: 256, required: true },
      { key: 'targetName',  type: 'string', size: 512 },
      { key: 'context',     type: 'string', size: 2000 },
    ],
    indexes: [
      { key: 'idx_source', type: 'key', attrs: ['sourceSlug'] },
      { key: 'idx_target', type: 'key', attrs: ['targetSlug'] },
      { key: 'idx_verb',   type: 'key', attrs: ['verb'] },
    ],
  },
  {
    id: 'evidence',
    name: 'Evidence',
    attrs: [
      { key: 'entitySlug',  type: 'string', size: 256, required: true },
      { key: 'title',       type: 'string', size: 512, required: true },
      { key: 'author',      type: 'string', size: 256 },
      { key: 'year',        type: 'integer' },
      { key: 'doiOrUrl',    type: 'string', size: 512 },
      { key: 'tier',        type: 'string', size: 8 },
      { key: 'citation',    type: 'string', size: 2000 },
      { key: 'sourceNote',  type: 'string', size: 2000 },
    ],
    indexes: [
      { key: 'idx_entity', type: 'key', attrs: ['entitySlug'] },
      { key: 'idx_tier',   type: 'key', attrs: ['tier'] },
    ],
  },
  {
    id: 'media',
    name: 'Media',
    attrs: [
      { key: 'entitySlug', type: 'string', size: 256, required: true },
      { key: 'fileId',     type: 'string', size: 128 },
      { key: 'url',        type: 'string', size: 512, required: true },
      { key: 'alt',        type: 'string', size: 512, required: true },
      { key: 'credit',     type: 'string', size: 256 },
      { key: 'category',   type: 'string', size: 32 },
      { key: 'caption',    type: 'string', size: 1000 },
    ],
    indexes: [
      { key: 'idx_entity', type: 'key', attrs: ['entitySlug'] },
    ],
  },
  {
    id: 'timeline_entries',
    name: 'Timeline Entries',
    attrs: [
      { key: 'entitySlug',   type: 'string',  size: 256, required: true },
      { key: 'year',         type: 'integer',             required: true },
      { key: 'endYear',      type: 'integer' },
      { key: 'title',        type: 'string',  size: 512, required: true },
      { key: 'description',  type: 'string',  size: 2000 },
      { key: 'significance', type: 'string',  size: 16 },
    ],
    indexes: [
      { key: 'idx_entity', type: 'key', attrs: ['entitySlug'] },
      { key: 'idx_year',   type: 'key', attrs: ['year'] },
    ],
  },
  {
    id: 'audit_log',
    name: 'Audit Log',
    attrs: [
      { key: 'entityId',     type: 'string', size: 128, required: true },
      { key: 'entitySlug',   type: 'string', size: 256, required: true },
      { key: 'entityName',   type: 'string', size: 512 },
      { key: 'action',       type: 'string', size: 32,  required: true },  // update | delete | create | batch_update
      { key: 'field',        type: 'string', size: 128 },                  // which field changed
      { key: 'oldValue',     type: 'string', size: 10000 },
      { key: 'newValue',     type: 'string', size: 10000 },
      { key: 'editorId',     type: 'string', size: 128, required: true },
      { key: 'editorNote',   type: 'string', size: 1000 },
      { key: 'timestamp',    type: 'string', size: 64,  required: true },  // ISO 8601
      { key: 'sessionId',    type: 'string', size: 64 },
    ],
    indexes: [
      { key: 'idx_entity',    type: 'key', attrs: ['entitySlug'] },
      { key: 'idx_timestamp', type: 'key', attrs: ['timestamp'] },
      { key: 'idx_editor',    type: 'key', attrs: ['editorId'] },
      { key: 'idx_action',    type: 'key', attrs: ['action'] },
    ],
  },
]

// ── Main ──

async function main() {
  console.log('=== Appwrite Schema Setup ===')
  console.log(`Endpoint:  ${ENDPOINT}`)
  console.log(`Project:   ${PROJECT_ID}`)
  console.log(`Database:  ${DATABASE_ID}`)
  console.log()

  // 1. Create database
  console.log('Creating database...')
  await safe(`Database "${DATABASE_ID}"`, () =>
    databases.create(DATABASE_ID, 'Annals of the World'),
  )
  console.log()

  // 2. Create collections
  for (const col of COLLECTIONS) {
    console.log(`Collection: ${col.name} (${col.id})`)
    await safe(`Collection "${col.id}"`, () =>
      databases.createCollection(DATABASE_ID, col.id, col.name),
    )

    // 3. Create attributes
    for (const attr of col.attrs) {
      const label = `  Attr "${attr.key}" (${attr.type})`
      await safe(label, async () => {
        switch (attr.type) {
          case 'string':
            await databases.createStringAttribute(
              DATABASE_ID, col.id, attr.key,
              attr.size || 256,
              attr.required || false,
              attr.default_ as string | undefined,
            )
            break
          case 'string[]':
            await databases.createStringAttribute(
              DATABASE_ID, col.id, attr.key,
              attr.size || 256,
              attr.required || false,
              undefined,
              true, // array
            )
            break
          case 'integer':
            await databases.createIntegerAttribute(
              DATABASE_ID, col.id, attr.key,
              attr.required || false,
            )
            break
          case 'float':
            await databases.createFloatAttribute(
              DATABASE_ID, col.id, attr.key,
              attr.required || false,
            )
            break
          case 'boolean':
            await databases.createBooleanAttribute(
              DATABASE_ID, col.id, attr.key,
              attr.required || false,
            )
            break
        }
      })
      await sleep(ATTR_DELAY)
    }

    // 4. Wait for attributes to be available before creating indexes
    console.log('  Waiting for attributes to propagate...')
    await sleep(3000)

    // 5. Create indexes
    for (const idx of col.indexes) {
      await safe(`  Index "${idx.key}" (${idx.type})`, () =>
        databases.createIndex(
          DATABASE_ID, col.id, idx.key,
          idx.type,
          idx.attrs,
        ),
      )
      await sleep(ATTR_DELAY)
    }
    console.log()
  }

  console.log('=== Schema setup complete ===')
}

main().catch((err) => {
  console.error('Setup failed:', err.message || err)
  process.exit(1)
})
