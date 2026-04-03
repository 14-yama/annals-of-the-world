#!/usr/bin/env npx tsx
/**
 * cleanup_appwrite.ts — Delete all collections to start fresh
 */
import sdk from 'node-appwrite'

const ENDPOINT   = process.env.VITE_APPWRITE_ENDPOINT   || 'https://fra.cloud.appwrite.io/v1'
const PROJECT_ID = process.env.VITE_APPWRITE_PROJECT_ID  || '69cc45e3000d587ea5e6'
const DATABASE_ID = process.env.VITE_APPWRITE_DATABASE_ID || 'annals_db'
const API_KEY    = process.env.APPWRITE_API_KEY

if (!API_KEY) { console.error('Set APPWRITE_API_KEY'); process.exit(1) }

const client = new sdk.Client()
client.setEndpoint(ENDPOINT).setProject(PROJECT_ID).setKey(API_KEY)
const db = new sdk.Databases(client)

async function main() {
  for (const col of ['entities', 'relationships', 'evidence', 'media', 'timeline_entries']) {
    try {
      await db.deleteCollection(DATABASE_ID, col)
      console.log(`Deleted ${col}`)
    } catch (e: unknown) {
      const err = e as { code?: number }
      console.log(`Skip ${col} (${err.code || 'unknown'})`)
    }
  }
  console.log('Done')
}

main()
