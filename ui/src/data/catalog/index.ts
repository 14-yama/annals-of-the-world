/**
 * Catalog Index — merges all era entity arrays into a single flat collection.
 *
 * Import from here for the complete catalog; import individual era files
 * when you only need one era's data.
 */
import { prehistoricEntities } from './prehistoric'
import { classicalEntities } from './classical'
import { medievalEntities } from './medieval'
import { earlyModernEntities } from './earlyModern'
import { modernEntities } from './modern'
import { contemporaryEntities } from './contemporary'
import { REFORMATION_ENTITIES } from './reformation'
import { BIBLICAL_ENTITIES } from './biblical'
import { GEO_REGISTRY_ENTITIES } from './geoRegistry'
import { DIVISION_ENRICHMENT_ENTITIES } from './divisionEnrichment'

// ── Corpus imports ──
import { MESOPOTAMIAN_ENTITIES } from './corpuses/mesopotamian'
import { EGYPTIAN_ENTITIES } from './corpuses/egyptian'
import { JUDAIC_RABBINIC_ENTITIES } from './corpuses/judaicRabbinic'
import { GRAECO_ROMAN_ENTITIES } from './corpuses/graecoRoman'
import { CANON_LAW_ENTITIES } from './corpuses/canonLaw'
import { IRAN_CENTRAL_ASIA_ENTITIES } from './corpuses/iranCentralAsia'
import { SOUTH_SE_ASIA_ENTITIES } from './corpuses/southSEAsia'
import { EAST_ASIA_ENTITIES } from './corpuses/eastAsia'
import { AFRICA_ENTITIES } from './corpuses/africa'
import { AMERICAS_ENTITIES } from './corpuses/americas'
import { EUROPE_BATCH1_ENTITIES } from './corpuses/europeBatch1'
import { EUROPE_BATCH2_ENTITIES } from './corpuses/europeBatch2'
import { SCIENCE_TECH_ENTITIES } from './corpuses/scienceTech'

// ── Topic entities (weapons, medicine, architecture, agriculture, navigation, languages) ──
import { ALL_TOPIC_ENTITIES } from './topicEntities'

import type { Entity } from '../entityTypes'

/**
 * Deduplicate: first occurrence of each slug wins.
 * Hand-curated entities appear before auto-generated ones, so they take priority.
 */
function dedup(entities: Entity[]): Entity[] {
  const seen = new Set<string>()
  return entities.filter(e => {
    if (seen.has(e.slug)) return false
    seen.add(e.slug)
    return true
  })
}

/**
 * All entities across every era — the Annals Catalog: source of truth.
 * Deduplicated by slug; hand-curated entries take priority over auto-generated.
 */
export const ALL_CATALOG_ENTITIES: Entity[] = dedup([
  // ── Hand-curated era entities (highest priority) ──
  ...prehistoricEntities,
  ...classicalEntities,
  ...BIBLICAL_ENTITIES,
  ...medievalEntities,
  ...earlyModernEntities,
  ...REFORMATION_ENTITIES,
  ...modernEntities,
  ...contemporaryEntities,
  ...DIVISION_ENRICHMENT_ENTITIES,
  // ── Corpus entities ──
  ...MESOPOTAMIAN_ENTITIES,
  ...EGYPTIAN_ENTITIES,
  ...JUDAIC_RABBINIC_ENTITIES,
  ...GRAECO_ROMAN_ENTITIES,
  ...CANON_LAW_ENTITIES,
  ...IRAN_CENTRAL_ASIA_ENTITIES,
  ...SOUTH_SE_ASIA_ENTITIES,
  ...EAST_ASIA_ENTITIES,
  ...AFRICA_ENTITIES,
  ...AMERICAS_ENTITIES,
  ...EUROPE_BATCH1_ENTITIES,
  ...EUROPE_BATCH2_ENTITIES,
  ...SCIENCE_TECH_ENTITIES,
  // ── Topic entities ──
  ...ALL_TOPIC_ENTITIES,
  // ── Geo-registry (auto-generated, lowest priority) ──
  ...GEO_REGISTRY_ENTITIES,
])

/** Slug → Entity lookup map (built once at import time) */
const SLUG_MAP = new Map<string, Entity>()
for (const e of ALL_CATALOG_ENTITIES) {
  SLUG_MAP.set(e.slug, e)
}

/** Call-number → Entity lookup map */
const CN_MAP = new Map<string, Entity>()
for (const e of ALL_CATALOG_ENTITIES) {
  CN_MAP.set(e.callNumber, e)
}

/* ── Public Accessors ── */

export function getEntity(slug: string): Entity | undefined {
  return SLUG_MAP.get(slug)
}

export function getAllEntities(): Entity[] {
  return ALL_CATALOG_ENTITIES
}

export function getEntityByCallNumber(cn: string): Entity | undefined {
  return CN_MAP.get(cn)
}

export function getEntitiesByShelf(prefix: string): Entity[] {
  return ALL_CATALOG_ENTITIES
    .filter(e => e.callNumber.startsWith(prefix))
    .sort((a, b) => a.callNumber.localeCompare(b.callNumber))
}

/**
 * Extract a numeric sort year from an entity.
 * Checks startDate, born, founded, period in that order.
 * Returns a comparable number: negative for BCE, positive for CE.
 * Falls back to Infinity so undated entities sort last.
 */
export function parseSortYear(entity: Entity): number {
  const raw = entity.startDate || entity.born || entity.founded || entity.period || ''
  return extractYear(raw)
}

function extractYear(s: string): number {
  if (!s) return Infinity
  const bce = /(\d[\d,]*)\s*BC(?:E)?/i.exec(s)
  if (bce) return -parseInt(bce[1].replace(/,/g, ''), 10)
  const ce = /(\d[\d,]*)\s*(?:CE|AD)/i.exec(s)
  if (ce) return parseInt(ce[1].replace(/,/g, ''), 10)
  // "c. 1300" or just "1517"
  const plain = /\b(\d{3,4})\b/.exec(s)
  if (plain) return parseInt(plain[1], 10)
  // "5th century"
  const cent = /(\d+)(?:st|nd|rd|th)\s*century/i.exec(s)
  if (cent) {
    const n = parseInt(cent[1], 10)
    const isBce = /BCE|BC/i.test(s)
    return isBce ? -(n * 100) : (n - 1) * 100
  }
  return Infinity
}

export function getShelfNeighbors(callNumber: string, range = 5): Entity[] {
  const dotIndex = callNumber.indexOf('.')
  if (dotIndex === -1) return []
  const prefix = callNumber.substring(0, dotIndex + 1)
  const shelf = getEntitiesByShelf(prefix)
  const idx = shelf.findIndex(e => e.callNumber === callNumber)
  if (idx === -1) return shelf.slice(0, range * 2)
  const start = Math.max(0, idx - range)
  const end = Math.min(shelf.length, idx + range + 1)
  return shelf.slice(start, end)
}

export function getShelfSummary(): { prefix: string; heading: string; count: number }[] {
  const map = new Map<string, number>()
  for (const e of ALL_CATALOG_ENTITIES) {
    const dotIdx = e.callNumber.indexOf('.')
    if (dotIdx >= 0) {
      const prefix = e.callNumber.substring(0, dotIdx)
      map.set(prefix, (map.get(prefix) || 0) + 1)
    }
  }
  return Array.from(map.entries())
    .map(([prefix, count]) => ({ prefix, heading: prefix, count }))
    .sort((a, b) => a.prefix.localeCompare(b.prefix))
}

export function getEntitiesByEra(eraSlug: string): Entity[] {
  return ALL_CATALOG_ENTITIES.filter(e => e.eraSlug === eraSlug)
}

export function getEntitiesByContinent(continent: string): Entity[] {
  return ALL_CATALOG_ENTITIES.filter(
    e => e.continent.toLowerCase() === continent.toLowerCase()
  )
}

export function getEntitiesByLabel(label: Entity['label']): Entity[] {
  return ALL_CATALOG_ENTITIES.filter(e => e.label === label)
}

// Re-export types for convenience
export type { Entity, NodeLabel, EntityRelationship, EntityCause, EntityEffect, EntityPlace, EntityText } from '../entityTypes'
