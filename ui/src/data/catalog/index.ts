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
import { GEO_REGISTRY_ENTITIES } from './geoRegistry'
import type { Entity } from '../entityTypes'

/** All entities across every era, in chronological era order */
export const ALL_CATALOG_ENTITIES: Entity[] = [
  ...prehistoricEntities,
  ...classicalEntities,
  ...medievalEntities,
  ...earlyModernEntities,
  ...REFORMATION_ENTITIES,
  ...modernEntities,
  ...contemporaryEntities,
  ...GEO_REGISTRY_ENTITIES,
]

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
