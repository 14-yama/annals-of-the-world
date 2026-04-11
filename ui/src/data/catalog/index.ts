/**
 * Catalog Index — merges all era entity arrays into a single flat collection.
 *
 * DEPRECATED: Entity data files have been moved to ../deprecated-catalog/.
 * The Appwrite backend is now the canonical source of truth.
 * This index remains for backward compatibility with scripts and seeding tools.
 *
 * Import from here for the complete catalog; import individual era files
 * when you only need one era's data.
 */
import { prehistoricEntities } from '../deprecated-catalog/prehistoric'
import { classicalEntities } from '../deprecated-catalog/classical'
import { medievalEntities } from '../deprecated-catalog/medieval'
import { earlyModernEntities } from '../deprecated-catalog/earlyModern'
import { modernEntities } from '../deprecated-catalog/modern'
import { contemporaryEntities } from '../deprecated-catalog/contemporary'
import { REFORMATION_ENTITIES } from '../deprecated-catalog/reformation'
import { BIBLICAL_ENTITIES } from '../deprecated-catalog/biblical'
import { GEO_REGISTRY_ENTITIES } from '../deprecated-catalog/geoRegistry'
import { DIVISION_ENRICHMENT_ENTITIES } from '../deprecated-catalog/divisionEnrichment'
import { DIVISION_EXPANSION_ENTITIES } from '../deprecated-catalog/divisionExpansion'
import { DIV_280_ENTITIES } from '../deprecated-catalog/divisionExpansion280'
import { DIV_290_ENTITIES } from '../deprecated-catalog/divisionExpansion290'
import { DIV_380_ENTITIES } from '../deprecated-catalog/divisionExpansion380'
import { DIV_590_ENTITIES } from '../deprecated-catalog/divisionExpansion590'
import { DIV_680_ENTITIES } from '../deprecated-catalog/divisionExpansion680'
import { DIV_780_ENTITIES } from '../deprecated-catalog/divisionExpansion780'
import { seedExpansionEntities } from '../deprecated-catalog/seedExpansion'
import { divisionGapFillEntities } from '../deprecated-catalog/divisionGapFill'
import { placeEntities } from '../deprecated-catalog/placeEntities'

// ── Wikidata-sourced people (5,014 notable figures from Wikidata SPARQL) ──
import { WIKIDATA_PEOPLE_ENTITIES } from '../deprecated-catalog/wikidataPeople'

// ── Corpus imports ──
import { MESOPOTAMIAN_ENTITIES } from '../deprecated-catalog/corpuses/mesopotamian'
import { EGYPTIAN_ENTITIES } from '../deprecated-catalog/corpuses/egyptian'
import { JUDAIC_RABBINIC_ENTITIES } from '../deprecated-catalog/corpuses/judaicRabbinic'
import { GRAECO_ROMAN_ENTITIES } from '../deprecated-catalog/corpuses/graecoRoman'
import { CANON_LAW_ENTITIES } from '../deprecated-catalog/corpuses/canonLaw'
import { IRAN_CENTRAL_ASIA_ENTITIES } from '../deprecated-catalog/corpuses/iranCentralAsia'
import { SOUTH_SE_ASIA_ENTITIES } from '../deprecated-catalog/corpuses/southSEAsia'
import { EAST_ASIA_ENTITIES } from '../deprecated-catalog/corpuses/eastAsia'
import { AFRICA_ENTITIES } from '../deprecated-catalog/corpuses/africa'
import { AMERICAS_ENTITIES } from '../deprecated-catalog/corpuses/americas'
import { EUROPE_BATCH1_ENTITIES } from '../deprecated-catalog/corpuses/europeBatch1'
import { EUROPE_BATCH2_ENTITIES } from '../deprecated-catalog/corpuses/europeBatch2'
import { SCIENCE_TECH_ENTITIES } from '../deprecated-catalog/corpuses/scienceTech'

// ── Topic entities (weapons, medicine, architecture, agriculture, navigation, languages) ──
import { ALL_TOPIC_ENTITIES } from '../deprecated-catalog/topicEntities'

// ── Text node entities (generated from actor text references) ──
import { TEXT_NODE_ENTITIES } from '../deprecated-catalog/textNodes'

// ── Post-processing enrichment data ──
import { ENRICHMENT_DATA } from '../deprecated-catalog/enrichmentData'

// ── Call number reclassification ──
import { reclassifyDivisions } from '../deprecated-catalog/reclassify'

// ── Summary enrichment for thin/generic entries ──
import { enrichThinSummaries } from '../deprecated-catalog/enrichSummaries'

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
 * Fix era assignment for entities whose numeric period contradicts their era.
 * Auto-generated textNode entities inherit the parent entity's era, which is
 * the era of the SUBJECT. But texts published in modern times should reflect
 * their publication date so they appear in the correct era timeline.
 */
const ERA_FIX_MAP: Record<string, [string, string]> = {} // slug → [era, eraSlug] — manual overrides if needed

/** Misclassified entities → correct division (uses expanded sub-divisions) */
const CALL_NUMBER_FIXES: Record<string, string> = {
  'national-assembly-bhutan':              '311.national-assembly-bhutan',
  'western-bulgarian-empire':              '312.western-bulgarian-empire',
  'yellow-turban-rebellion-devastates-the-empire-and-leads-to-the-three-kingdoms':
                                           '522.yellow-turban-rebellion',
  'kong-empire':                           '312.kong-empire',
  'jan-hus-burned-at-stake-at-council-of-constance':
                                           '574.jan-hus-burned-at-stake',
  'livonian-confederation-estonia':        '312.livonian-confederation-estonia',
  'abbasid-caliphate-indonesia':           '312.abbasid-caliphate-indonesia',
  'union-of-lublin-creates-the-polish-lithuanian-commonwealth':
                                           '311.union-of-lublin',
  'philippine-commonwealth-established-with-manuel-quezon-as-president':
                                           '313.philippine-commonwealth-established',
  'philippine-commonwealth':               '313.philippine-commonwealth',
  'socialist-republic-vietnam':            '310.socialist-republic-vietnam',
}

function fixEras(entities: Entity[]): Entity[] {
  return entities.map(e => {
    // Apply call-number fixes for misclassified entities
    const cnFix = CALL_NUMBER_FIXES[e.slug]

    const p = e.period
    if (!p && !cnFix) return e
    if (!p && cnFix) return { ...e, callNumber: cnFix }

    // Parse numeric year (handles "1997", "534 CE", "c. 1300")
    const cleaned = String(p).replace(/c\.\s*/i, '').replace(/\s*CE/i, '').replace(/\s*BCE/i, '').trim()
    const num = parseInt(cleaned, 10)
    if (isNaN(num)) return cnFix ? { ...e, callNumber: cnFix } : e
    // BCE handling: if original has BCE, negate
    const year = /BCE/i.test(String(p)) ? -num : num

    let expectedEra: string
    let expectedSlug: string
    if (year < -3000)       { expectedEra = 'Prehistoric';  expectedSlug = 'prehistoric' }
    else if (year <= 500)   { expectedEra = 'Classical';    expectedSlug = 'classical' }
    else if (year <= 1500)  { expectedEra = 'Medieval';     expectedSlug = 'medieval' }
    else if (year <= 1800)  { expectedEra = 'Early Modern'; expectedSlug = 'early-modern' }
    else if (year <= 1945)  { expectedEra = 'Modern';       expectedSlug = 'modern' }
    else                    { expectedEra = 'Contemporary'; expectedSlug = 'contemporary' }

    const eraChanged = e.era !== expectedEra
    if (eraChanged || cnFix) {
      return {
        ...e,
        ...(eraChanged ? { era: expectedEra, eraSlug: expectedSlug } : {}),
        ...(cnFix ? { callNumber: cnFix } : {}),
      }
    }
    return e
  })
}

/**
 * Apply enrichment data: add cross-entity relationships, text slugs, and frameworks.
 */
function applyEnrichment(entities: Entity[]): Entity[] {
  return entities.map(e => {
    const en = ENRICHMENT_DATA[e.slug]
    if (!en) return e

    // Add new relationships
    const relationships = en.newRels.length > 0
      ? [...e.relationships, ...en.newRels]
      : e.relationships

    // Add text slugs
    const texts = Object.keys(en.textSlugs).length > 0
      ? e.texts.map((t, i) => en.textSlugs[i] ? { ...t, slug: en.textSlugs[i] } : t)
      : e.texts

    // Replace frameworks if enriched
    const frameworks = en.frameworks.length > 0 ? en.frameworks : e.frameworks

    // Fix call number if needed (e.g., div 600 → 680)
    const callNumber = (en as any).callNumberFix || e.callNumber

    return { ...e, relationships, texts, frameworks, callNumber }
  })
}

/**
 * All entities across every era — the Annals Catalog: source of truth.
 * Deduplicated by slug; hand-curated entries take priority over auto-generated.
 * Enriched with cross-entity relationships, text slug linking, and frameworks.
 */
export const ALL_CATALOG_ENTITIES: Entity[] = reclassifyDivisions(enrichThinSummaries(fixEras(applyEnrichment(dedup([
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
  ...DIVISION_EXPANSION_ENTITIES,
  ...DIV_280_ENTITIES,
  ...DIV_290_ENTITIES,
  ...DIV_380_ENTITIES,
  ...DIV_590_ENTITIES,
  ...DIV_680_ENTITIES,
  ...DIV_780_ENTITIES,
  // ── Seed expansion (scholarly balance) ──
  ...seedExpansionEntities,
  // ── Division gap fill (covers all 122 previously empty divisions) ──
  ...divisionGapFillEntities,
  // ── Place entities (294 entities: continents, regions, countries, cities, empires, civilizations, culture areas) ──
  ...placeEntities,
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
  // ── Text node entities (auto-generated from text references) ──
  ...TEXT_NODE_ENTITIES,
  // ── Wikidata people (5,014 notable figures — yields to hand-curated) ──
  ...WIKIDATA_PEOPLE_ENTITIES,
  // ── Geo-registry (auto-generated, lowest priority) ──
  ...GEO_REGISTRY_ENTITIES,
])))))

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
