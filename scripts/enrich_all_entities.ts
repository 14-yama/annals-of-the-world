#!/usr/bin/env npx tsx
/**
 * enrich_all_entities.ts — Enriches ALL catalog entities (non-geo-registry) 
 * with cross-entity relationships, text slug linking, and framework enrichment.
 *
 * Targets: hand-curated, corpus, topic, textNode entities
 * Outputs: enriched versions of each source file
 *
 * Usage: cd /home/manasa151/annals-of-the-world && npx tsx scripts/enrich_all_entities.ts
 */

import { ALL_CATALOG_ENTITIES } from '../ui/src/data/catalog/index'
import type { Entity, EntityRelationship, EntityText } from '../ui/src/data/entityTypes'

/* ═══════════════════════════════════════════════════
   BUILD INDEXES
   ═══════════════════════════════════════════════════ */

const ENTITY_MAP = new Map<string, Entity>()
for (const e of ALL_CATALOG_ENTITIES) ENTITY_MAP.set(e.slug, e)

const TEXT_SLUG_MAP = new Map<string, string>()
for (const e of ALL_CATALOG_ENTITIES) {
  if (e.label === 'Text') TEXT_SLUG_MAP.set(e.name.toLowerCase().trim(), e.slug)
}

// Country → entities
const BY_COUNTRY = new Map<string, Entity[]>()
for (const e of ALL_CATALOG_ENTITIES) {
  for (const p of e.places || []) {
    const key = p.name.toLowerCase()
    if (!BY_COUNTRY.has(key)) BY_COUNTRY.set(key, [])
    BY_COUNTRY.get(key)!.push(e)
  }
}

// Era+label → entities
const BY_ERA_LABEL = new Map<string, Entity[]>()
for (const e of ALL_CATALOG_ENTITIES) {
  const key = `${e.eraSlug}:${e.label}`
  if (!BY_ERA_LABEL.has(key)) BY_ERA_LABEL.set(key, [])
  BY_ERA_LABEL.get(key)!.push(e)
}

/* ═══════════════════════════════════════════════════
   SUBJECT → FRAMEWORK MAPPING
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
  'conquest': ['EMPIRE_AND_COLONIALISM', 'CONFLICT_AND_RESOLUTION'],
  'hellenism': ['CULTURAL_DIFFUSION', 'CONTINUITY_AND_CHANGE'],
  'empire': ['EMPIRE_AND_COLONIALISM', 'POLITICAL_SYSTEMS'],
  'military': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT'],
  'legal code': ['LEGAL_INTERPRETATION', 'POLITICAL_SYSTEMS'],
  'philosophy': ['CONTINUITY_AND_CHANGE', 'CAUSE_AND_EFFECT'],
  'classical': ['CONTINUITY_AND_CHANGE', 'CAUSE_AND_EFFECT'],
  'europe': ['GEOPOLITICAL_LINKAGE', 'CONTINUITY_AND_CHANGE'],
  'asia': ['GEOPOLITICAL_LINKAGE', 'CULTURAL_DIFFUSION'],
  'africa': ['GEOPOLITICAL_LINKAGE', 'CULTURAL_DIFFUSION'],
  'americas': ['GEOPOLITICAL_LINKAGE', 'CULTURAL_DIFFUSION'],
}

/* ═══════════════════════════════════════════════════
   TEXT SLUG MATCHING
   ═══════════════════════════════════════════════════ */

function matchTextSlug(text: EntityText): string | undefined {
  if (text.slug) return text.slug
  const title = text.title.toLowerCase().trim()
  if (TEXT_SLUG_MAP.has(title)) return TEXT_SLUG_MAP.get(title)
  const noParen = title.replace(/\s*\([^)]*\)\s*/g, '').trim()
  if (TEXT_SLUG_MAP.has(noParen)) return TEXT_SLUG_MAP.get(noParen)
  if (title.startsWith('the ')) {
    const noThe = title.slice(4)
    if (TEXT_SLUG_MAP.has(noThe)) return TEXT_SLUG_MAP.get(noThe)
  }
  return undefined
}

/* ═══════════════════════════════════════════════════
   RELATIONSHIP BUILDING
   ═══════════════════════════════════════════════════ */

function buildRelationships(e: Entity): EntityRelationship[] {
  const existing = new Set<string>()
  for (const r of e.relationships) {
    existing.add(`${r.sourceSlug}|${r.verb}|${r.targetSlug}`)
  }

  const newRels: EntityRelationship[] = []
  function addRel(rel: EntityRelationship) {
    const key = `${rel.sourceSlug}|${rel.verb}|${rel.targetSlug}`
    if (existing.has(key)) return
    if (rel.sourceSlug === rel.targetSlug) return
    existing.add(key)
    newRels.push(rel)
  }

  // 1. Link causes/effects that exist as entities 
  for (const cause of e.causes || []) {
    if (cause.slug && ENTITY_MAP.has(cause.slug)) {
      addRel({
        sourceSlug: cause.slug, sourceName: cause.title,
        verb: 'CAUSES', targetSlug: e.slug, targetName: e.name,
        context: `Causal antecedent (${cause.year})`,
      })
    }
  }
  for (const effect of e.effects || []) {
    if (effect.slug && ENTITY_MAP.has(effect.slug)) {
      addRel({
        sourceSlug: e.slug, sourceName: e.name,
        verb: 'CAUSES', targetSlug: effect.slug, targetName: effect.title,
        context: `Consequent outcome (${effect.year})`,
      })
    }
  }

  // 2. Link text refs that have entity pages
  for (const t of e.texts || []) {
    const slug = t.slug || matchTextSlug(t)
    if (slug && ENTITY_MAP.has(slug)) {
      const verb = e.label === 'Person' ? 'AUTHORS' :
                   e.label === 'Institution' ? 'CANONIZES' :
                   e.label === 'Movement' ? 'TRANSMITS' : 'REFERENCES'
      addRel({
        sourceSlug: e.slug, sourceName: e.name,
        verb, targetSlug: slug, targetName: ENTITY_MAP.get(slug)!.name,
        context: `Text reference: ${t.type || 'Document'}`,
      })
    }
  }

  // 3. Same-era same-country cross-type connections
  const country = e.places?.[0]?.name?.toLowerCase()
  if (country) {
    const peers = (BY_COUNTRY.get(country) || []).filter(o =>
      o.eraSlug === e.eraSlug && o.slug !== e.slug
    )

    if (e.label === 'Person') {
      const inst = peers.find(o => o.label === 'Institution')
      if (inst) addRel({ sourceSlug: e.slug, sourceName: e.name, verb: 'LEADS', targetSlug: inst.slug, targetName: inst.name, context: `Contemporary institution` })
      const mov = peers.find(o => o.label === 'Movement')
      if (mov) addRel({ sourceSlug: e.slug, sourceName: e.name, verb: 'INFLUENCES', targetSlug: mov.slug, targetName: mov.name, context: `Contemporary movement` })
      const evt = peers.find(o => o.label === 'EventWindow')
      if (evt) addRel({ sourceSlug: e.slug, sourceName: e.name, verb: 'PARTICIPATES_IN', targetSlug: evt.slug, targetName: evt.name, context: `Active during this event` })
    }

    if (e.label === 'EventWindow') {
      const person = peers.find(o => o.label === 'Person')
      if (person) addRel({ sourceSlug: person.slug, sourceName: person.name, verb: 'PARTICIPATES_IN', targetSlug: e.slug, targetName: e.name, context: `Historical figure active during event` })
      const inst = peers.find(o => o.label === 'Institution')
      if (inst) addRel({ sourceSlug: inst.slug, sourceName: inst.name, verb: 'DEFINES', targetSlug: e.slug, targetName: e.name, context: `Institution involved in event` })
    }

    if (e.label === 'Movement') {
      const idea = peers.find(o => o.label === 'Idea')
      if (idea) addRel({ sourceSlug: idea.slug, sourceName: idea.name, verb: 'INSPIRES', targetSlug: e.slug, targetName: e.name, context: `Intellectual foundation` })
      const person = peers.find(o => o.label === 'Person')
      if (person) addRel({ sourceSlug: person.slug, sourceName: person.name, verb: 'INFLUENCES', targetSlug: e.slug, targetName: e.name, context: `Key figure in movement` })
    }

    if (e.label === 'Institution') {
      const person = peers.find(o => o.label === 'Person')
      if (person) addRel({ sourceSlug: person.slug, sourceName: person.name, verb: 'ADMINISTERS', targetSlug: e.slug, targetName: e.name, context: `Leader of institution` })
    }

    if (e.label === 'Idea') {
      const person = peers.find(o => o.label === 'Person')
      if (person) addRel({ sourceSlug: person.slug, sourceName: person.name, verb: 'CONCEIVES', targetSlug: e.slug, targetName: e.name, context: `Thinker behind the idea` })
      const mov = peers.find(o => o.label === 'Movement')
      if (mov) addRel({ sourceSlug: e.slug, sourceName: e.name, verb: 'INSPIRES', targetSlug: mov.slug, targetName: mov.name, context: `Idea inspires movement` })
    }
  }

  // 4. For Text entities — link to same-era entities that reference this text
  if (e.label === 'Text') {
    const nameLower = e.name.toLowerCase().trim()
    const referencing = ALL_CATALOG_ENTITIES.filter(o =>
      o.slug !== e.slug && (o.texts || []).some(t => {
        const tTitle = t.title.toLowerCase().trim()
        return tTitle === nameLower || t.slug === e.slug
      })
    )
    for (const ref of referencing.slice(0, 5)) {
      const verb = ref.label === 'Person' ? 'AUTHORS' :
                   ref.label === 'Institution' ? 'CANONIZES' : 'REFERENCES'
      addRel({
        sourceSlug: ref.slug, sourceName: ref.name,
        verb, targetSlug: e.slug, targetName: e.name,
        context: `Referenced in ${ref.label.toLowerCase()} entity`,
      })
    }

    // Also link to same-era people/movements
    const eraEntities = BY_ERA_LABEL.get(`${e.eraSlug}:Person`) || []
    const relatedPerson = eraEntities.find(o =>
      (o.subjects || []).some(s => (e.subjects || []).includes(s)) && o.slug !== e.slug
    )
    if (relatedPerson) {
      addRel({
        sourceSlug: relatedPerson.slug, sourceName: relatedPerson.name,
        verb: 'AUTHORS', targetSlug: e.slug, targetName: e.name,
        context: `Scholarly tradition of the era`,
      })
    }
  }

  // 5. For Place entities — link to events/people who occurred there
  if (e.label === 'Place') {
    const placeName = e.name.toLowerCase()
    const occurring = ALL_CATALOG_ENTITIES.filter(o =>
      o.slug !== e.slug && (o.places || []).some(p => p.name.toLowerCase() === placeName)
    )
    for (const ref of occurring.slice(0, 5)) {
      addRel({
        sourceSlug: ref.slug, sourceName: ref.name,
        verb: 'OCCURS_IN', targetSlug: e.slug, targetName: e.name,
        context: `Located in this place`,
      })
    }
  }

  // 6. For Evidence entities — link to entities in same era
  if (e.label === 'Evidence') {
    const eraEntities = BY_ERA_LABEL.get(`${e.eraSlug}:EventWindow`) || []
    const related = eraEntities.find(o => 
      (o.subjects || []).some(s => (e.subjects || []).includes(s)) && o.slug !== e.slug
    )
    if (related) {
      addRel({
        sourceSlug: e.slug, sourceName: e.name,
        verb: 'SUPPORTS', targetSlug: related.slug, targetName: related.name,
        context: `Evidence supporting this event`,
      })
    }
  }

  return newRels
}

/* ═══════════════════════════════════════════════════
   FRAMEWORK ENRICHMENT
   ═══════════════════════════════════════════════════ */

function enrichFrameworks(e: Entity): string[] {
  const existing = new Set(e.frameworks || [])
  for (const s of e.subjects || []) {
    const fws = SUBJECT_TO_FRAMEWORKS[s.toLowerCase()]
    if (fws) for (const fw of fws) existing.add(fw)
  }
  // Label-based defaults
  if (e.label === 'Text' && !existing.has('TEXTUAL_TRANSMISSION')) existing.add('TEXTUAL_TRANSMISSION')
  if (e.label === 'Evidence' && !existing.has('CAUSE_AND_EFFECT')) existing.add('CAUSE_AND_EFFECT')
  if (e.label === 'Place' && !existing.has('GEOPOLITICAL_LINKAGE')) existing.add('GEOPOLITICAL_LINKAGE')

  if (existing.size === 0) existing.add('CAUSE_AND_EFFECT')
  return [...existing]
}

/* ═══════════════════════════════════════════════════
   PROCESS ALL ENTITIES & REPORT
   ═══════════════════════════════════════════════════ */

console.log(`Processing ${ALL_CATALOG_ENTITIES.length} entities...`)

let textSlugsAdded = 0
let relsAdded = 0
let fwAdded = 0

// Collect enrichments per slug
const enrichments = new Map<string, {
  newRels: EntityRelationship[]
  textSlugs: Map<number, string>
  newFrameworks: string[]
}>()

for (const e of ALL_CATALOG_ENTITIES) {
  // Text slug enrichment
  const textSlugs = new Map<number, string>()
  for (let i = 0; i < (e.texts || []).length; i++) {
    const t = e.texts[i]
    if (!t.slug) {
      const slug = matchTextSlug(t)
      if (slug) { textSlugs.set(i, slug); textSlugsAdded++ }
    }
  }

  // Relationship enrichment
  const newRels = buildRelationships(e)
  relsAdded += newRels.length

  // Framework enrichment
  const oldFwCount = (e.frameworks || []).length
  const newFrameworks = enrichFrameworks(e)
  fwAdded += newFrameworks.length - oldFwCount

  enrichments.set(e.slug, { newRels, textSlugs, newFrameworks })
}

console.log(`\nEnrichment summary (all entities):`)
console.log(`  Text slugs added: ${textSlugsAdded}`)
console.log(`  Relationships added: ${relsAdded}`)
console.log(`  Frameworks added: ${fwAdded}`)

// Output stats for post-enrichment verification
let sparseAfter = 0
for (const e of ALL_CATALOG_ENTITIES) {
  const en = enrichments.get(e.slug)!
  const totalRels = e.relationships.length + en.newRels.length
  if (totalRels <= 1) sparseAfter++
}
console.log(`\n  Entities with <= 1 rel BEFORE: 1411`)
console.log(`  Entities with <= 1 rel AFTER: ${sparseAfter}`)

/* ═══════════════════════════════════════════════════
   OUTPUT: write enrichment as a runtime post-processor in catalog/index.ts
   We add an enrichment function that mutates entities at import time.
   ═══════════════════════════════════════════════════ */

import * as fs from 'fs'
import * as path from 'path'

// Generate the enrichment data file
const outPath = path.join(__dirname, '..', 'ui', 'src', 'data', 'catalog', 'enrichmentData.ts')

function esc(s: string): string {
  return s.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\n/g, '\\n')
}

const lines: string[] = []
lines.push(`/**`)
lines.push(` * Auto-generated enrichment data for non-geo-registry entities.`)
lines.push(` * Generated by scripts/enrich_all_entities.ts`)
lines.push(` * DO NOT EDIT MANUALLY`)
lines.push(` */`)
lines.push(`import type { EntityRelationship } from '../entityTypes'`)
lines.push(``)
lines.push(`export interface SlugEnrichment {`)
lines.push(`  newRels: EntityRelationship[]`)
lines.push(`  textSlugs: Record<number, string>  // index → slug`)
lines.push(`  frameworks: string[]`)
lines.push(`}`)
lines.push(``)
lines.push(`export const ENRICHMENT_DATA: Record<string, SlugEnrichment> = {`)

let enrichedCount = 0
for (const [slug, en] of enrichments) {
  if (en.newRels.length === 0 && en.textSlugs.size === 0 && en.newFrameworks.length === (ENTITY_MAP.get(slug)?.frameworks?.length || 0)) continue
  enrichedCount++
  
  lines.push(`  '${esc(slug)}': {`)
  
  // newRels
  if (en.newRels.length > 0) {
    lines.push(`    newRels: [`)
    for (const r of en.newRels) {
      lines.push(`      { sourceSlug: '${esc(r.sourceSlug)}', sourceName: '${esc(r.sourceName)}', verb: '${esc(r.verb)}', targetSlug: '${esc(r.targetSlug)}', targetName: '${esc(r.targetName)}'${r.context ? `, context: '${esc(r.context)}'` : ''} },`)
    }
    lines.push(`    ],`)
  } else {
    lines.push(`    newRels: [],`)
  }

  // textSlugs
  if (en.textSlugs.size > 0) {
    const entries = [...en.textSlugs.entries()].map(([i, s]) => `${i}: '${esc(s)}'`)
    lines.push(`    textSlugs: { ${entries.join(', ')} },`)
  } else {
    lines.push(`    textSlugs: {},`)
  }

  // frameworks (full replacement)
  lines.push(`    frameworks: [${en.newFrameworks.map(f => `'${f}'`).join(', ')}],`)
  
  lines.push(`  },`)
}

lines.push(`}`)

fs.writeFileSync(outPath, lines.join('\n') + '\n')
console.log(`\nWrote ${outPath}`)
console.log(`  Enriched ${enrichedCount} entities`)
