/**
 * wikidataPeople.ts — Wikidata-sourced Person entities
 *
 * Loads ui/src/data/wikidata_people.json (catalog extract of top 5,014 notable
 * people per division, extracted from 238,466 Wikidata SPARQL results).
 * 2,800 people seeded to Appwrite backend (as of 2026-04-02).
 *
 * Full dataset: data/wikidata_people.json (238K+ entities, 289 MB — backend only)
 * Extract script: scripts/extract_wikidata_catalog.py
 * Fetch script: scripts/fetch_wikidata_all_people.py
 */
import type { Entity } from '../entityTypes'
import wikidataRaw from '../wikidata_people.json'

interface WikidataPersonRaw {
  slug: string
  name: string
  label: string
  callNumber: string
  subjectHeadings: string[]
  subjects: string[]
  summary: string
  era: string
  eraSlug: string
  region: string
  continent: string
  status: string
  frameworks: string[]
  causes: { title: string; type: string; year: string; slug?: string }[]
  effects: { title: string; type: string; year: string; slug?: string }[]
  relationships: {
    sourceSlug: string
    sourceName: string
    verb: string
    targetSlug: string
    targetName: string
    context?: string
  }[]
  places: { name: string; role: string; slug?: string }[]
  texts?: { title: string; type: string; year?: string; slug?: string }[]
  born?: string
  died?: string
  wikidataQid?: string
  wikipediaUrl?: string
  imageUrl?: string
  inAppwrite?: boolean
}

interface WikidataFile {
  _meta: Record<string, unknown>
  entities: WikidataPersonRaw[]
}

const data = wikidataRaw as WikidataFile

export const WIKIDATA_PEOPLE_ENTITIES: Entity[] = data.entities.map((p) => ({
  slug: p.slug,
  name: p.name,
  label: p.label as Entity['label'],
  callNumber: p.callNumber,
  subjectHeadings: p.subjectHeadings,
  subjects: p.subjects,
  summary: p.summary,
  era: p.era,
  eraSlug: p.eraSlug,
  region: p.region,
  continent: p.continent,
  status: p.status,
  frameworks: p.frameworks,
  causes: p.causes,
  effects: p.effects,
  relationships: p.relationships,
  places: p.places,
  texts: p.texts ?? [],
  ...(p.born ? { born: p.born } : {}),
  ...(p.died ? { died: p.died } : {}),
  ...(p.wikidataQid ? { wikidataQid: p.wikidataQid } : {}),
  ...(p.wikipediaUrl ? { wikipediaUrl: p.wikipediaUrl } : {}),
  ...(p.imageUrl ? { imageUrl: p.imageUrl } : {}),
}))
