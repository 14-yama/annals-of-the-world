#!/usr/bin/env npx tsx
import sdk from 'node-appwrite'
const c = new sdk.Client()
c.setEndpoint(process.env.VITE_APPWRITE_ENDPOINT!).setProject(process.env.VITE_APPWRITE_PROJECT_ID!).setKey(process.env.APPWRITE_API_KEY!)
const db = new sdk.Databases(c)
async function main() {
  // Set read permission for all collections
  for (const col of ['entities', 'relationships', 'evidence', 'media', 'timeline_entries']) {
    try {
      await db.updateCollection('annals_db', col, col, [
        sdk.Permission.read(sdk.Role.any()),
      ])
      console.log(`✓ ${col} — read(any) set`)
    } catch (e: unknown) {
      const err = e as { message?: string }
      console.log(`✗ ${col}: ${err.message}`)
    }
  }
}
main()
