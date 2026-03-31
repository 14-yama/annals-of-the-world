#!/usr/bin/env npx tsx
/**
 * enrich_catalog.ts — Post-processing enrichment for all catalog entities
 *
 * Reads ALL_CATALOG_ENTITIES and outputs enriched geoRegistry.ts with:
 * 1. Text slug linking (match text refs → existing Text entities)
 * 2. Cross-entity relationships (shared country/era/subject connections)
 * 3. Framework enrichment (subject-based framework assignment)
 * 4. Call number reclassification (590→proper division, etc.)
 *
 * Usage: cd ui && npx tsx ../scripts/enrich_catalog.ts
 */

import { ALL_CATALOG_ENTITIES } from '../ui/src/data/catalog/index'
import { GEO_REGISTRY_ENTITIES } from '../ui/src/data/catalog/geoRegistry'
import type { Entity, EntityRelationship, EntityText } from '../ui/src/data/entityTypes'
import * as fs from 'fs'
import * as path from 'path'

/* ═══════════════════════════════════════════════════
   1. BUILD LOOKUP INDEXES
   ═══════════════════════════════════════════════════ */

// Text entity lookup: normalized title → slug
const TEXT_SLUG_MAP = new Map<string, string>()
for (const e of ALL_CATALOG_ENTITIES) {
  if (e.label === 'Text') {
    TEXT_SLUG_MAP.set(e.name.toLowerCase().trim(), e.slug)
  }
}

// All entity slug lookup
const ENTITY_MAP = new Map<string, Entity>()
for (const e of ALL_CATALOG_ENTITIES) {
  ENTITY_MAP.set(e.slug, e)
}

// Country → entities index
const BY_COUNTRY = new Map<string, Entity[]>()
for (const e of ALL_CATALOG_ENTITIES) {
  for (const p of e.places || []) {
    const key = p.name.toLowerCase()
    if (!BY_COUNTRY.has(key)) BY_COUNTRY.set(key, [])
    BY_COUNTRY.get(key)!.push(e)
  }
}

// Era → entities index
const BY_ERA = new Map<string, Entity[]>()
for (const e of ALL_CATALOG_ENTITIES) {
  if (!BY_ERA.has(e.eraSlug)) BY_ERA.set(e.eraSlug, [])
  BY_ERA.get(e.eraSlug)!.push(e)
}

/* ═══════════════════════════════════════════════════
   2. SUBJECT → FRAMEWORK MAPPING
   ═══════════════════════════════════════════════════ */

const SUBJECT_TO_FRAMEWORKS: Record<string, string[]> = {
  'warfare': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT'],
  'colonialism': ['EMPIRE_AND_COLONIALISM', 'GEOPOLITICAL_LINKAGE'],
  'independence': ['POLITICAL_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
  'governance': ['POLITICAL_SYSTEMS', 'CAUSE_AND_EFFECT'],
  'trade': ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
  'religion': ['COMPARATIVE_RELIGION', 'DOCTRINE_DEVELOPMENT'],
  'migration': ['CULTURAL_DIFFUSION', 'ENVIRONMENTAL_HISTORY'],
  'art & culture': ['CULTURAL_DIFFUSION', 'CONTINUITY_AND_CHANGE'],
  'education': ['INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
  'science': ['INNOVATION_AND_TECHNOLOGY', 'CAUSE_AND_EFFECT'],
  'agriculture': ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'agriculture & food': ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'medicine & healing': ['INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
  'languages & scripts': ['CULTURAL_DIFFUSION', 'TEXTUAL_TRANSMISSION'],
  'navigation & exploration': ['INNOVATION_AND_TECHNOLOGY', 'EMPIRE_AND_COLONIALISM'],
  'weapons & warfare': ['CONFLICT_AND_RESOLUTION', 'INNOVATION_AND_TECHNOLOGY'],
  'clothing & textiles': ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS'],
  'tribes & peoples': ['CULTURAL_DIFFUSION', 'CONTINUITY_AND_CHANGE'],
  'customs & traditions': ['CULTURAL_DIFFUSION', 'RITUAL_STANDARDIZATION'],
  'marriage & union': ['CULTURAL_DIFFUSION', 'LEGAL_INTERPRETATION'],
  'technology': ['INNOVATION_AND_TECHNOLOGY', 'CAUSE_AND_EFFECT'],
  'indigenous': ['CULTURAL_DIFFUSION', 'EMPIRE_AND_COLONIALISM'],
  'scripture': ['COMPARATIVE_RELIGION', 'TEXTUAL_TRANSMISSION'],
  'transportation': ['INNOVATION_AND_TECHNOLOGY', 'ECONOMIC_SYSTEMS'],
}

/* ═══════════════════════════════════════════════════
   3. CALL NUMBER RECLASSIFICATION
   ═══════════════════════════════════════════════════ */

function reclassifyCallNumber(e: Entity): string {
  const cn = e.callNumber || ''
  const div = cn.split('.')[0]
  const subjects = (e.subjects || []).map(s => s.toLowerCase())

  // Fix undefined division 590 → proper Events/Ideas division
  if (div === '590') {
    if (subjects.includes('agriculture') || subjects.includes('agriculture & food')) {
      // Agriculture ideas → 160 (Environmental/Ecological Ideas) or keep as 590 (now defined)
      return cn.replace('590', '590')
    }
    return cn
  }

  // Fix undefined division 600 → 680 (Trade & Navigation Movements) or 560 (Tech Breakthroughs)
  if (div === '600') {
    return cn.replace('600', '680')
  }

  // People reclassification: military leaders → 280
  if (e.label === 'Person' && div === '220') {
    if (subjects.includes('military') || subjects.includes('warfare') ||
        e.name.toLowerCase().includes('general ') ||
        e.summary?.toLowerCase().includes('military commander') ||
        e.summary?.toLowerCase().includes('military leader')) {
      return cn.replace('220', '280')
    }
    // Explorer → 290
    if (subjects.includes('navigation & exploration') || subjects.includes('exploration') ||
        e.summary?.toLowerCase().includes('explorer') ||
        e.summary?.toLowerCase().includes('navigator')) {
      return cn.replace('220', '290')
    }
  }

  // Institution reclassification: education → 380
  if (e.label === 'Institution' && div === '310') {
    if (subjects.includes('education')) {
      return cn.replace('310', '380')
    }
  }

  return cn
}

/* ═══════════════════════════════════════════════════
   4. TEXT SLUG MATCHING
   ═══════════════════════════════════════════════════ */

function matchTextSlug(text: EntityText): string | undefined {
  if (text.slug) return text.slug

  const title = text.title.toLowerCase().trim()

  // Direct match
  if (TEXT_SLUG_MAP.has(title)) return TEXT_SLUG_MAP.get(title)

  // Fuzzy: remove parenthetical dates/authors
  const noParen = title.replace(/\s*\([^)]*\)\s*/g, '').trim()
  if (TEXT_SLUG_MAP.has(noParen)) return TEXT_SLUG_MAP.get(noParen)

  // Try "the X" → "X"
  if (title.startsWith('the ')) {
    const noThe = title.slice(4)
    if (TEXT_SLUG_MAP.has(noThe)) return TEXT_SLUG_MAP.get(noThe)
  }

  return undefined
}

/* ═══════════════════════════════════════════════════
   5. CROSS-ENTITY RELATIONSHIP BUILDING
   ═══════════════════════════════════════════════════ */

function buildCrossRelationships(e: Entity): EntityRelationship[] {
  const existing = new Set<string>()
  for (const r of e.relationships) {
    existing.add(`${r.sourceSlug}|${r.verb}|${r.targetSlug}`)
  }

  const newRels: EntityRelationship[] = []

  function addRel(rel: EntityRelationship) {
    const key = `${rel.sourceSlug}|${rel.verb}|${rel.targetSlug}`
    const reverseKey = `${rel.targetSlug}|${rel.verb}|${rel.sourceSlug}`
    if (existing.has(key) || existing.has(reverseKey)) return
    if (rel.sourceSlug === rel.targetSlug) return
    existing.add(key)
    newRels.push(rel)
  }

  // Link to cause/effect entities that exist in catalog
  for (const cause of e.causes || []) {
    if (cause.slug && ENTITY_MAP.has(cause.slug)) {
      addRel({
        sourceSlug: cause.slug,
        sourceName: cause.title,
        verb: 'CAUSES',
        targetSlug: e.slug,
        targetName: e.name,
        context: `Causal antecedent (${cause.year})`,
      })
    }
  }

  for (const effect of e.effects || []) {
    if (effect.slug && ENTITY_MAP.has(effect.slug)) {
      addRel({
        sourceSlug: e.slug,
        sourceName: e.name,
        verb: 'CAUSES',
        targetSlug: effect.slug,
        targetName: effect.title,
        context: `Consequent outcome (${effect.year})`,
      })
    }
  }

  // Link texts that have entity pages
  for (const t of e.texts || []) {
    const slug = t.slug || matchTextSlug(t)
    if (slug && ENTITY_MAP.has(slug)) {
      const verb = e.label === 'Person' ? 'AUTHORS' :
                   e.label === 'Institution' ? 'CANONIZES' :
                   e.label === 'Movement' ? 'TRANSMITS' : 'REFERENCES'
      addRel({
        sourceSlug: e.slug,
        sourceName: e.name,
        verb,
        targetSlug: slug,
        targetName: ENTITY_MAP.get(slug)!.name,
        context: `Text reference: ${t.type || 'Document'}`,
      })
    }
  }

  // For Person entities: link to institutions/movements in same country+era
  if (e.label === 'Person') {
    const country = e.places?.[0]?.name?.toLowerCase()
    if (country) {
      const countryEntities = BY_COUNTRY.get(country) || []
      const sameEra = countryEntities.filter(o =>
        o.eraSlug === e.eraSlug && o.slug !== e.slug
      )
      // Link to 1 institution + 1 movement in same country/era
      const inst = sameEra.find(o => o.label === 'Institution')
      if (inst) {
        addRel({
          sourceSlug: e.slug, sourceName: e.name,
          verb: 'LEADS', targetSlug: inst.slug, targetName: inst.name,
          context: `Contemporary institution in ${e.places[0].name}`,
        })
      }
      const mov = sameEra.find(o => o.label === 'Movement')
      if (mov) {
        addRel({
          sourceSlug: e.slug, sourceName: e.name,
          verb: 'INFLUENCES', targetSlug: mov.slug, targetName: mov.name,
          context: `Contemporary movement in ${e.places[0].name}`,
        })
      }
    }
  }

  // For EventWindow: link to related events in same country via sequential eras
  if (e.label === 'EventWindow') {
    const country = e.places?.[0]?.name?.toLowerCase()
    if (country) {
      const countryEntities = BY_COUNTRY.get(country) || []
      // Link to 1 person in same country+era
      const person = countryEntities.find(o =>
        o.eraSlug === e.eraSlug && o.label === 'Person' && o.slug !== e.slug
      )
      if (person) {
        addRel({
          sourceSlug: person.slug, sourceName: person.name,
          verb: 'PARTICIPATES_IN', targetSlug: e.slug, targetName: e.name,
          context: `Historical figure active during this event`,
        })
      }
    }
  }

  // For Movement: link to related ideas
  if (e.label === 'Movement') {
    const country = e.places?.[0]?.name?.toLowerCase()
    if (country) {
      const countryEntities = BY_COUNTRY.get(country) || []
      const idea = countryEntities.find(o =>
        o.label === 'Idea' && o.slug !== e.slug
      )
      if (idea) {
        addRel({
          sourceSlug: idea.slug, sourceName: idea.name,
          verb: 'INSPIRES', targetSlug: e.slug, targetName: e.name,
          context: `Intellectual foundation for movement`,
        })
      }
    }
  }

  return newRels
}

/* ═══════════════════════════════════════════════════
   6. FRAMEWORK ENRICHMENT
   ═══════════════════════════════════════════════════ */

function enrichFrameworks(e: Entity): string[] {
  const existing = new Set(e.frameworks || [])

  for (const s of e.subjects || []) {
    const fws = SUBJECT_TO_FRAMEWORKS[s.toLowerCase()]
    if (fws) {
      for (const fw of fws) existing.add(fw)
    }
  }

  // Ensure minimum: CAUSE_AND_EFFECT
  if (existing.size === 0) existing.add('CAUSE_AND_EFFECT')

  return [...existing]
}

/* ═══════════════════════════════════════════════════
   7. PROCESS ALL GEO-REGISTRY ENTITIES
   ═══════════════════════════════════════════════════ */

console.log(`Processing ${GEO_REGISTRY_ENTITIES.length} geo-registry entities...`)

let textSlugsAdded = 0
let relsAdded = 0
let frameworksAdded = 0
let reclassified = 0

const enriched: Entity[] = GEO_REGISTRY_ENTITIES.map(e => {
  // 1. Reclassify call number
  const newCN = reclassifyCallNumber(e)
  if (newCN !== e.callNumber) reclassified++

  // 2. Match text slugs
  const enrichedTexts = (e.texts || []).map(t => {
    const slug = t.slug || matchTextSlug(t)
    if (slug && !t.slug) textSlugsAdded++
    return slug ? { ...t, slug } : t
  })

  // 3. Build cross-relationships
  const newRels = buildCrossRelationships(e)
  relsAdded += newRels.length

  // 4. Enrich frameworks
  const oldFwCount = (e.frameworks || []).length
  const newFrameworks = enrichFrameworks(e)
  frameworksAdded += newFrameworks.length - oldFwCount

  return {
    ...e,
    callNumber: newCN,
    texts: enrichedTexts,
    relationships: [...e.relationships, ...newRels],
    frameworks: newFrameworks,
  }
})

console.log(`\nEnrichment summary:`)
console.log(`  Text slugs added: ${textSlugsAdded}`)
console.log(`  Relationships added: ${relsAdded}`)
console.log(`  Frameworks added: ${frameworksAdded}`)
console.log(`  Call numbers reclassified: ${reclassified}`)

/* ═══════════════════════════════════════════════════
   8. WRITE OUTPUT
   ═══════════════════════════════════════════════════ */

function escapeString(s: string): string {
  return s.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\n/g, '\\n')
}

function entityToTs(e: Entity): string {
  const lines: string[] = []
  lines.push('  {')
  lines.push(`    slug: '${escapeString(e.slug)}',`)
  lines.push(`    name: '${escapeString(e.name)}',`)
  lines.push(`    label: '${e.label}',`)
  lines.push(`    callNumber: '${escapeString(e.callNumber)}',`)
  lines.push(`    subjectHeadings: [${e.subjectHeadings.map(s => `'${escapeString(s)}'`).join(', ')}],`)
  lines.push(`    subjects: [${e.subjects.map(s => `'${escapeString(s)}'`).join(', ')}],`)
  lines.push(`    summary: '${escapeString(e.summary)}',`)
  if (e.born) lines.push(`    born: '${escapeString(e.born)}',`)
  if (e.died) lines.push(`    died: '${escapeString(e.died)}',`)
  if (e.founded) lines.push(`    founded: '${escapeString(e.founded)}',`)
  if (e.period) lines.push(`    period: '${escapeString(e.period)}',`)
  if (e.startDate) lines.push(`    startDate: '${escapeString(e.startDate)}',`)
  if (e.endDate) lines.push(`    endDate: '${escapeString(e.endDate)}',`)
  lines.push(`    era: '${escapeString(e.era)}',`)
  lines.push(`    eraSlug: '${escapeString(e.eraSlug)}',`)
  lines.push(`    region: '${escapeString(e.region)}',`)
  lines.push(`    continent: '${escapeString(e.continent)}',`)
  lines.push(`    status: '${e.status}',`)
  lines.push(`    frameworks: [${(e.frameworks || []).map(f => `'${f}'`).join(', ')}],`)

  // causes
  lines.push(`    causes: [${e.causes.map(c =>
    `{ title: '${escapeString(c.title)}', type: '${escapeString(c.type)}', year: '${escapeString(c.year)}'${c.slug ? `, slug: '${escapeString(c.slug)}'` : ''} }`
  ).join(', ')}],`)

  // effects
  lines.push(`    effects: [${e.effects.map(eff =>
    `{ title: '${escapeString(eff.title)}', type: '${escapeString(eff.type)}', year: '${escapeString(eff.year)}'${eff.slug ? `, slug: '${escapeString(eff.slug)}'` : ''} }`
  ).join(', ')}],`)

  // relationships
  lines.push(`    relationships: [`)
  for (const r of e.relationships) {
    lines.push(`      { sourceSlug: '${escapeString(r.sourceSlug)}', sourceName: '${escapeString(r.sourceName)}', verb: '${escapeString(r.verb)}', targetSlug: '${escapeString(r.targetSlug)}', targetName: '${escapeString(r.targetName)}'${r.context ? `, context: '${escapeString(r.context)}'` : ''} },`)
  }
  lines.push(`    ],`)

  // places
  lines.push(`    places: [${e.places.map(p =>
    `{ name: '${escapeString(p.name)}', role: '${escapeString(p.role)}'${p.slug ? `, slug: '${escapeString(p.slug)}'` : ''} }`
  ).join(', ')}],`)

  // texts
  lines.push(`    texts: [${e.texts.map(t =>
    `{ title: '${escapeString(t.title)}', type: '${escapeString(t.type)}'${t.year ? `, year: '${escapeString(t.year)}'` : ''}${t.slug ? `, slug: '${escapeString(t.slug)}'` : ''} }`
  ).join(', ')}],`)

  lines.push('  },')
  return lines.join('\n')
}

const outPath = path.join(__dirname, '..', 'ui', 'src', 'data', 'catalog', 'geoRegistry.ts')
const header = `/**
 * Geo-Registry Catalog Entities — Auto-generated + Enriched
 *
 * ${enriched.length} entities from 199 countries × 6 eras.
 * Enriched with cross-entity relationships, text slug linking,
 * framework enrichment, and call number reclassification.
 *
 * DO NOT EDIT MANUALLY — regenerate via: npx tsx scripts/enrich_catalog.ts
 */
import type { Entity } from '../entityTypes'

export const GEO_REGISTRY_ENTITIES: Entity[] = [
`

const body = enriched.map(e => entityToTs(e)).join('\n')
const footer = '\n]\n'

fs.writeFileSync(outPath, header + body + footer)
console.log(`\nWrote ${outPath} (${enriched.length} entities)`)
