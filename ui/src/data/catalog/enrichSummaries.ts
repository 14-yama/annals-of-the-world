/**
 * Summary Enrichment — Upgrades thin/generic entity summaries
 *
 * Detects placeholder summaries (e.g., "X — historical figure of Country")
 * and generates richer text using entity metadata: name, era, country,
 * label, subject headings, causes, effects, period.
 *
 * Applied as a pipeline step in catalog/index.ts.
 */
import type { Entity } from '../entityTypes'

/* ── Thin summary detection patterns ── */

const THIN_PATTERNS = [
  /^(?:The )?(.+?) — historical figure of (.+)$/i,
  /^(?:The )?(.+?) — document related to (.+)$/i,
  /^(?:The )?(.+?) — institution in (.+)$/i,
  /^(?:The )?(.+?) in ([A-Z][\w\s]+)$/i,
]

function isThinSummary(summary: string): boolean {
  if (summary.length < 60) return THIN_PATTERNS.some(p => p.test(summary))
  return false
}

/* ── Context extraction helpers ── */

function extractCountry(entity: Entity): string {
  const place = entity.places?.[0]?.name
  if (place) return place
  const sub = (entity.subjects || []).find(s =>
    !['Warfare', 'Trade', 'Colonialism', 'Migration', 'Religion', 'Governance',
      'Independence', 'Art & Culture', 'Education', 'Science', 'Agriculture',
      'Technology', 'Indigenous', 'Scripture', 'Medicine & Healing',
    ].includes(s)
  )
  return sub || ''
}

function extractCluster(entity: Entity): string {
  const sh = entity.subjectHeadings?.[0] || ''
  // Format: "Label — Cluster — Country — Era"
  const parts = sh.split(' — ')
  return parts.length >= 2 ? parts[1] : ''
}

function eraLabel(eraSlug: string): string {
  const map: Record<string, string> = {
    prehistoric: 'Prehistoric',
    classical: 'Classical',
    medieval: 'Medieval',
    'early-modern': 'Early Modern',
    modern: 'Modern',
    contemporary: 'Contemporary',
  }
  return map[eraSlug] || eraSlug
}

function periodPhrase(entity: Entity): string {
  if (entity.period) return ` (${entity.period})`
  if (entity.startDate && entity.endDate) return ` (${entity.startDate}–${entity.endDate})`
  if (entity.startDate) return ` (from ${entity.startDate})`
  return ''
}

/* ── Label-specific summary generators ── */

function enrichPerson(entity: Entity, country: string, cluster: string): string {
  const era = eraLabel(entity.eraSlug)
  const period = periodPhrase(entity)

  // Use cause/effect context if available
  const causeNames = (entity.causes || []).slice(0, 2).map(c => c.title)
  const effectNames = (entity.effects || []).slice(0, 2).map(e => e.title)

  let desc = `${entity.name}, a notable figure`
  if (country) desc += ` in the history of ${country}`
  if (cluster) desc += `, associated with ${cluster}`
  desc += period ? `${period}.` : ` during the ${era} period.`

  if (causeNames.length > 0) {
    desc += ` Preceded by ${causeNames.join(' and ')}.`
  }
  if (effectNames.length > 0) {
    desc += ` Their legacy influenced ${effectNames.join(' and ')}.`
  }

  return desc
}

function enrichInstitution(entity: Entity, country: string, cluster: string): string {
  const era = eraLabel(entity.eraSlug)
  const period = periodPhrase(entity)

  const causeNames = (entity.causes || []).slice(0, 2).map(c => c.title)
  const effectNames = (entity.effects || []).slice(0, 2).map(e => e.title)

  let desc = `${entity.name}, a political institution`
  if (country) desc += ` in ${country}`
  if (cluster) desc += ` during ${cluster}`
  desc += period ? `${period}.` : ` of the ${era} era.`

  if (causeNames.length > 0) {
    desc += ` Grew from ${causeNames.join(' and ')}.`
  }
  if (effectNames.length > 0) {
    desc += ` Led to the emergence of ${effectNames.join(' and ')}.`
  }

  return desc
}

function enrichText(entity: Entity, country: string, cluster: string): string {
  const era = eraLabel(entity.eraSlug)
  const period = periodPhrase(entity)

  const causeNames = (entity.causes || []).slice(0, 2).map(c => c.title)
  const effectNames = (entity.effects || []).slice(0, 2).map(e => e.title)

  let desc = `${entity.name}, a significant document`
  if (country) desc += ` in the history of ${country}`
  desc += period ? `${period}.` : ` from the ${era} period.`

  if (cluster) desc += ` Part of ${cluster}.`
  if (effectNames.length > 0) {
    desc += ` Shaped ${effectNames.join(' and ')}.`
  }

  return desc
}

function enrichMovement(entity: Entity, country: string, cluster: string): string {
  const era = eraLabel(entity.eraSlug)
  const period = periodPhrase(entity)

  const causeNames = (entity.causes || []).slice(0, 2).map(c => c.title)
  const effectNames = (entity.effects || []).slice(0, 2).map(e => e.title)

  let desc = `${entity.name}, a transformative movement`
  if (country) desc += ` in ${country}`
  desc += period ? `${period}.` : ` during the ${era} period.`

  if (causeNames.length > 0) {
    desc += ` Emerged from ${causeNames.join(' and ')}.`
  }
  if (effectNames.length > 0) {
    desc += ` Catalyzed ${effectNames.join(' and ')}.`
  }

  return desc
}

function enrichEvent(entity: Entity, country: string, cluster: string): string {
  const era = eraLabel(entity.eraSlug)
  const period = periodPhrase(entity)

  const causeNames = (entity.causes || []).slice(0, 2).map(c => c.title)
  const effectNames = (entity.effects || []).slice(0, 2).map(e => e.title)

  let desc = `${entity.name}, a pivotal event`
  if (country) desc += ` in the history of ${country}`
  desc += period ? `${period}.` : ` during the ${era} period.`

  if (cluster) desc += ` Part of ${cluster}.`
  if (causeNames.length > 0) {
    desc += ` Triggered by ${causeNames.join(' and ')}.`
  }
  if (effectNames.length > 0) {
    desc += ` This led to ${effectNames.join(' and ')}.`
  }

  return desc
}

/* ── Main enrichment function ── */

function enrichSummary(entity: Entity): string {
  const country = extractCountry(entity)
  const cluster = extractCluster(entity)

  switch (entity.label) {
    case 'Person': return enrichPerson(entity, country, cluster)
    case 'Institution': return enrichInstitution(entity, country, cluster)
    case 'Text': return enrichText(entity, country, cluster)
    case 'Movement': return enrichMovement(entity, country, cluster)
    case 'EventWindow': return enrichEvent(entity, country, cluster)
    default: return enrichEvent(entity, country, cluster)
  }
}

/**
 * Enrich all thin summaries in the catalog.
 * Applied as a pipeline step — entities with rich summaries are not touched.
 */
export function enrichThinSummaries(entities: Entity[]): Entity[] {
  return entities.map(e => {
    if (!isThinSummary(e.summary)) return e
    return { ...e, summary: enrichSummary(e) }
  })
}
