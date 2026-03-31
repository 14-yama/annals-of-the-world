/**
 * Second-pass enrichment: targets entities with 0 relationships after first enrichment,
 * reclassifies div-600 entities, and adds remaining text slugs.
 *
 * Reads the enriched catalog, identifies gaps, generates relationships by subject/era matching,
 * and outputs a merged enrichmentData.ts.
 */
import * as fs from 'fs'
import * as path from 'path'

// Import catalog (already has first-pass enrichment)
import { ALL_CATALOG_ENTITIES } from '../ui/src/data/catalog/index'
import type { Entity } from '../ui/src/data/entityTypes'

interface EntityRelationship {
  sourceSlug: string
  sourceName: string
  verb: string
  targetSlug: string
  targetName: string
  context?: string
}

interface EnrichmentEntry {
  newRels: EntityRelationship[]
  textSlugs: Record<number, string>
  frameworks: string[]
  callNumberFix?: string
}

// ── Build indexes ──
const slugMap = new Map<string, Entity>()
const byLabel = new Map<string, Entity[]>()
const byEra = new Map<string, Entity[]>()
const bySubject = new Map<string, Entity[]>()

ALL_CATALOG_ENTITIES.forEach(e => {
  slugMap.set(e.slug, e)

  if (!byLabel.has(e.label)) byLabel.set(e.label, [])
  byLabel.get(e.label)!.push(e)

  if (!byEra.has(e.era)) byEra.set(e.era, [])
  byEra.get(e.era)!.push(e)

  e.subjects.forEach(s => {
    const key = s.toLowerCase()
    if (!bySubject.has(key)) bySubject.set(key, [])
    bySubject.get(key)!.push(e)
  })
})

// ── Text slug database ──
const textEntities = ALL_CATALOG_ENTITIES.filter(e => e.label === 'Text')
const textSlugByTitle = new Map<string, string>()
textEntities.forEach(e => {
  textSlugByTitle.set(e.name.toLowerCase(), e.slug)
  // Also map without parenthetical
  const base = e.name.replace(/\s*\(.*?\)\s*/g, '').trim().toLowerCase()
  if (base !== e.name.toLowerCase()) textSlugByTitle.set(base, e.slug)
})

// All entity names for fuzzy matching
const allEntitySlugs = new Map<string, string>()
ALL_CATALOG_ENTITIES.forEach(e => {
  allEntitySlugs.set(e.name.toLowerCase(), e.slug)
})

function findTextSlug(title: string): string | undefined {
  const lower = title.toLowerCase()
  // Direct match
  if (textSlugByTitle.has(lower)) return textSlugByTitle.get(lower)
  // Without parenthetical
  const base = lower.replace(/\s*\(.*?\)\s*/g, '').trim()
  if (textSlugByTitle.has(base)) return textSlugByTitle.get(base)
  // Substring match: look for text entities whose name is part of title or vice-versa
  for (const [name, slug] of textSlugByTitle) {
    if (name.length > 4 && (lower.includes(name) || name.includes(base))) return slug
  }
  // Try matching against all entities (not just Text)
  if (allEntitySlugs.has(lower)) return allEntitySlugs.get(lower)
  if (allEntitySlugs.has(base)) return allEntitySlugs.get(base)
  return undefined
}

// ── Relationship verbs by label-pair ──
const VERB_MAP: Record<string, Record<string, string[]>> = {
  Person: {
    EventWindow: ['PARTICIPATES_IN'],
    Institution: ['LEADS', 'AFFILIATES_WITH'],
    Movement: ['PARTICIPATES_IN', 'INFLUENCES'],
    Idea: ['CONCEIVES', 'ADVOCATES'],
    Text: ['AUTHORS', 'REFERENCES'],
    Place: ['RESIDES_IN'],
    Person: ['INFLUENCES', 'CONTEMPORARY_OF'],
  },
  EventWindow: {
    Person: ['INVOLVES'],
    Place: ['OCCURS_IN'],
    Institution: ['INVOLVES'],
    Movement: ['ADVANCES'],
    Idea: ['MANIFESTS'],
    Text: ['DOCUMENTED_IN'],
    EventWindow: ['CAUSES', 'PRECEDES'],
  },
  Movement: {
    Idea: ['PROMOTES'],
    Person: ['INVOLVES'],
    Institution: ['INFLUENCES'],
    EventWindow: ['CAUSES'],
    Place: ['SPREADS_TO'],
    Movement: ['INSPIRES'],
    Text: ['DOCUMENTED_IN'],
  },
  Idea: {
    Person: ['CONCEIVED_BY'],
    Movement: ['INSPIRES'],
    Institution: ['SHAPES'],
    Text: ['DOCUMENTED_IN'],
    EventWindow: ['INFLUENCES'],
    Place: ['ORIGINATES_IN'],
    Idea: ['RELATES_TO'],
  },
  Institution: {
    Person: ['EMPLOYS'],
    EventWindow: ['PARTICIPATES_IN'],
    Place: ['LOCATED_IN'],
    Movement: ['SUPPORTS'],
    Idea: ['PROMOTES'],
    Text: ['PRODUCES'],
    Institution: ['ALLIES_WITH'],
  },
  Text: {
    Person: ['AUTHORED_BY'],
    EventWindow: ['DOCUMENTS'],
    Idea: ['EXPRESSES'],
    Movement: ['DOCUMENTS'],
    Place: ['ORIGINATES_IN'],
    Institution: ['PRODUCED_BY'],
    Text: ['REFERENCES'],
  },
  Place: {
    EventWindow: ['HOSTS'],
    Person: ['HOME_OF'],
    Institution: ['HOUSES'],
    Movement: ['SITE_OF'],
    Idea: ['BIRTHPLACE_OF'],
    Place: ['NEAR'],
  },
  Evidence: {
    Text: ['SUPPORTS'],
    Person: ['ABOUT'],
    EventWindow: ['SUPPORTS'],
    Idea: ['EVALUATES'],
    Place: ['FROM'],
  },
}

// Subject-to-framework mapping (broader than first pass)
const SUBJECT_FRAMEWORKS: Record<string, string[]> = {
  'warfare': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT'],
  'battle': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT'],
  'military': ['CONFLICT_AND_RESOLUTION', 'POLITICAL_SYSTEMS'],
  'war': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT'],
  'conquest': ['CONFLICT_AND_RESOLUTION', 'EMPIRE_AND_COLONIALISM'],
  'trade': ['ECONOMIC_SYSTEMS', 'DIFFUSION_AND_EXCHANGE'],
  'commerce': ['ECONOMIC_SYSTEMS', 'DIFFUSION_AND_EXCHANGE'],
  'economy': ['ECONOMIC_SYSTEMS'],
  'empire': ['EMPIRE_AND_COLONIALISM', 'POLITICAL_SYSTEMS'],
  'colonialism': ['EMPIRE_AND_COLONIALISM', 'POLITICAL_SYSTEMS'],
  'religion': ['COMPARATIVE_RELIGION', 'CONTINUITY_AND_CHANGE'],
  'prophet': ['COMPARATIVE_RELIGION', 'GREAT_PERSON'],
  'theology': ['COMPARATIVE_RELIGION', 'IDEAS_AND_WORLDVIEWS'],
  'philosophy': ['IDEAS_AND_WORLDVIEWS', 'CONTINUITY_AND_CHANGE'],
  'science': ['INNOVATION_AND_TECHNOLOGY', 'CAUSE_AND_EFFECT'],
  'technology': ['INNOVATION_AND_TECHNOLOGY'],
  'invention': ['INNOVATION_AND_TECHNOLOGY', 'CAUSE_AND_EFFECT'],
  'medicine': ['INNOVATION_AND_TECHNOLOGY', 'ENVIRONMENTAL_HISTORY'],
  'agriculture': ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'navigation': ['INNOVATION_AND_TECHNOLOGY', 'DIFFUSION_AND_EXCHANGE'],
  'education': ['IDEAS_AND_WORLDVIEWS', 'INSTITUTIONAL_ANALYSIS'],
  'law': ['INSTITUTIONAL_ANALYSIS', 'POLITICAL_SYSTEMS'],
  'government': ['POLITICAL_SYSTEMS', 'INSTITUTIONAL_ANALYSIS'],
  'democracy': ['POLITICAL_SYSTEMS', 'IDEAS_AND_WORLDVIEWS'],
  'monarchy': ['POLITICAL_SYSTEMS', 'GREAT_PERSON'],
  'revolution': ['CONFLICT_AND_RESOLUTION', 'CAUSE_AND_EFFECT', 'CONTINUITY_AND_CHANGE'],
  'independence': ['POLITICAL_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
  'migration': ['DIFFUSION_AND_EXCHANGE', 'ENVIRONMENTAL_HISTORY'],
  'language': ['DIFFUSION_AND_EXCHANGE', 'IDEAS_AND_WORLDVIEWS'],
  'writing': ['INNOVATION_AND_TECHNOLOGY', 'IDEAS_AND_WORLDVIEWS'],
  'literature': ['IDEAS_AND_WORLDVIEWS', 'COMPARATIVE_RELIGION'],
  'art': ['IDEAS_AND_WORLDVIEWS', 'DIFFUSION_AND_EXCHANGE'],
  'architecture': ['INNOVATION_AND_TECHNOLOGY', 'INSTITUTIONAL_ANALYSIS'],
  'urbanization': ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'city': ['ENVIRONMENTAL_HISTORY', 'INSTITUTIONAL_ANALYSIS'],
  'kingdom': ['POLITICAL_SYSTEMS', 'GREAT_PERSON'],
  'dynasty': ['POLITICAL_SYSTEMS', 'CONTINUITY_AND_CHANGE'],
  'reform': ['CONTINUITY_AND_CHANGE', 'INSTITUTIONAL_ANALYSIS'],
  'covenant': ['COMPARATIVE_RELIGION', 'INSTITUTIONAL_ANALYSIS'],
  'worship': ['COMPARATIVE_RELIGION'],
  'liturgy': ['COMPARATIVE_RELIGION', 'INSTITUTIONAL_ANALYSIS'],
  'scripture': ['COMPARATIVE_RELIGION', 'IDEAS_AND_WORLDVIEWS'],
  'manuscript': ['IDEAS_AND_WORLDVIEWS', 'INNOVATION_AND_TECHNOLOGY'],
  'papyrus': ['INNOVATION_AND_TECHNOLOGY', 'IDEAS_AND_WORLDVIEWS'],
  'justice': ['POLITICAL_SYSTEMS', 'IDEAS_AND_WORLDVIEWS'],
  'slavery': ['ECONOMIC_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
  'exploration': ['DIFFUSION_AND_EXCHANGE', 'INNOVATION_AND_TECHNOLOGY'],
  'pilgrimage': ['COMPARATIVE_RELIGION', 'DIFFUSION_AND_EXCHANGE'],
  'diplomacy': ['POLITICAL_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
  'treaty': ['POLITICAL_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
  'culture': ['IDEAS_AND_WORLDVIEWS', 'DIFFUSION_AND_EXCHANGE'],
  'ritual': ['COMPARATIVE_RELIGION', 'CONTINUITY_AND_CHANGE'],
  'mythology': ['COMPARATIVE_RELIGION', 'IDEAS_AND_WORLDVIEWS'],
  'ceremony': ['COMPARATIVE_RELIGION', 'INSTITUTIONAL_ANALYSIS'],
  'persecution': ['CONFLICT_AND_RESOLUTION', 'COMPARATIVE_RELIGION'],
  'heresy': ['COMPARATIVE_RELIGION', 'CONFLICT_AND_RESOLUTION'],
  'canon': ['COMPARATIVE_RELIGION', 'INSTITUTIONAL_ANALYSIS'],
  'council': ['INSTITUTIONAL_ANALYSIS', 'COMPARATIVE_RELIGION'],
  'surgery': ['INNOVATION_AND_TECHNOLOGY'],
  'astronomy': ['INNOVATION_AND_TECHNOLOGY', 'IDEAS_AND_WORLDVIEWS'],
  'mathematics': ['INNOVATION_AND_TECHNOLOGY', 'IDEAS_AND_WORLDVIEWS'],
  'engineering': ['INNOVATION_AND_TECHNOLOGY'],
  'transportation': ['INNOVATION_AND_TECHNOLOGY', 'DIFFUSION_AND_EXCHANGE'],
  'food': ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'famine': ['ENVIRONMENTAL_HISTORY', 'CAUSE_AND_EFFECT'],
  'plague': ['ENVIRONMENTAL_HISTORY', 'CAUSE_AND_EFFECT'],
  'climate': ['ENVIRONMENTAL_HISTORY'],
  'environment': ['ENVIRONMENTAL_HISTORY'],
}

function getFrameworksForEntity(e: Entity): string[] {
  const fws = new Set<string>(e.frameworks || [])
  const allText = [e.name, e.summary, ...e.subjects].join(' ').toLowerCase()
  for (const [keyword, frameworks] of Object.entries(SUBJECT_FRAMEWORKS)) {
    if (allText.includes(keyword)) {
      frameworks.forEach(f => fws.add(f))
    }
  }
  return Array.from(fws)
}

// ── Find related entities by shared subjects ──
function findRelatedBySubjects(entity: Entity, maxResults = 8): Entity[] {
  const candidates = new Map<string, {entity: Entity, score: number}>()
  const entitySubjects = entity.subjects.map(s => s.toLowerCase())

  for (const subj of entitySubjects) {
    const matches = bySubject.get(subj) || []
    for (const m of matches) {
      if (m.slug === entity.slug) continue
      const key = m.slug
      if (!candidates.has(key)) candidates.set(key, { entity: m, score: 0 })
      candidates.get(key)!.score += 1
      // Bonus for same era
      if (m.era === entity.era) candidates.get(key)!.score += 0.5
    }
  }

  // Also find by name/summary keyword matching
  const nameWords = entity.name.toLowerCase().split(/[\s\-_]+/).filter(w => w.length > 3)
  for (const word of nameWords) {
    const matches = bySubject.get(word) || []
    for (const m of matches) {
      if (m.slug === entity.slug) continue
      if (!candidates.has(m.slug)) candidates.set(m.slug, { entity: m, score: 0 })
      candidates.get(m.slug)!.score += 0.3
    }
  }

  return Array.from(candidates.values())
    .sort((a, b) => b.score - a.score)
    .slice(0, maxResults)
    .map(c => c.entity)
}

// ── Find related entities by era + label ──
function findRelatedByEraLabel(entity: Entity, targetLabel: string, maxResults = 3): Entity[] {
  const eraEntities = byEra.get(entity.era) || []
  return eraEntities
    .filter(e => e.slug !== entity.slug && e.label === targetLabel && e.relationships.length > 0)
    .slice(0, maxResults)
}

// ── Generate relationships for sparse entity ──
function generateRelationships(entity: Entity): EntityRelationship[] {
  const rels: EntityRelationship[] = []
  const added = new Set<string>()

  function addRel(verb: string, target: Entity, context?: string) {
    const key = `${verb}:${target.slug}`
    if (added.has(key)) return
    added.add(key)
    rels.push({
      sourceSlug: entity.slug,
      sourceName: entity.name,
      verb,
      targetSlug: target.slug,
      targetName: target.name,
      context: context || `${entity.era} era connection`,
    })
  }

  function addReverseRel(verb: string, source: Entity, context?: string) {
    const key = `${verb}:${source.slug}`
    if (added.has(key)) return
    added.add(key)
    rels.push({
      sourceSlug: source.slug,
      sourceName: source.name,
      verb,
      targetSlug: entity.slug,
      targetName: entity.name,
      context: context || `${entity.era} era connection`,
    })
  }

  // 1. Find related entities by subject overlap
  const related = findRelatedBySubjects(entity)

  for (const rel of related) {
    const verbs = VERB_MAP[entity.label]?.[rel.label]
    if (verbs && verbs.length > 0) {
      addRel(verbs[0], rel, `Shared subjects: ${entity.subjects.filter(
        s => rel.subjects.map(rs => rs.toLowerCase()).includes(s.toLowerCase())
      ).join(', ')}`)
    }
  }

  // 2. Label-specific enrichment patterns
  const label = entity.label
  const verbsByLabel = VERB_MAP[label] || {}

  // If still < 3 rels, find era-peers by different labels
  if (rels.length < 3) {
    const targetLabels = Object.keys(verbsByLabel).filter(l => l !== label)
    for (const tl of targetLabels) {
      if (rels.length >= 5) break
      const peers = findRelatedByEraLabel(entity, tl, 2)
      for (const peer of peers) {
        if (rels.length >= 5) break
        const verbs = verbsByLabel[tl]
        if (verbs) addRel(verbs[0], peer)
      }
    }
  }

  // 3. Place-based OCCURS_IN from entity.places
  if (entity.places && entity.places.length > 0) {
    for (const pl of entity.places) {
      const placeName = typeof pl === 'string' ? pl : (pl as any).name || ''
      if (!placeName) continue
      const placeSlug = placeName.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '')
      const placeEntity = slugMap.get(placeSlug) || slugMap.get(`${placeSlug}_city`)
      if (placeEntity && placeEntity.label === 'Place') {
        addRel('OCCURS_IN', placeEntity, `Located in ${placeEntity.name}`)
      }
    }
  }

  return rels
}

// ── Main processing ──
const enrichmentPatch: Record<string, EnrichmentEntry> = {}
let relsAdded = 0
let textSlugsAdded = 0
let fwsEnriched = 0
let callNumbersFixed = 0

// Process entities with 0 relationships
const sparseEntities = ALL_CATALOG_ENTITIES.filter(e => e.relationships.length === 0)
console.log(`Processing ${sparseEntities.length} entities with 0 relationships...`)

for (const entity of sparseEntities) {
  const newRels = generateRelationships(entity)

  // Text slug matching
  const textSlugs: Record<number, string> = {}
  entity.texts.forEach((t, i) => {
    if (!t.slug) {
      const slug = findTextSlug(t.title)
      if (slug) textSlugs[i] = slug
    }
  })

  // Framework enrichment
  const frameworks = getFrameworksForEntity(entity)

  // Call number fix for div 600
  let callNumberFix: string | undefined
  if (entity.callNumber.startsWith('600.')) {
    callNumberFix = entity.callNumber.replace('600.', '680.')
    callNumbersFixed++
  }

  if (newRels.length > 0 || Object.keys(textSlugs).length > 0 || frameworks.length > entity.frameworks.length || callNumberFix) {
    enrichmentPatch[entity.slug] = {
      newRels,
      textSlugs,
      frameworks: frameworks.length > entity.frameworks.length ? frameworks : [],
      callNumberFix,
    }
    relsAdded += newRels.length
    textSlugsAdded += Object.keys(textSlugs).length
    if (frameworks.length > entity.frameworks.length) fwsEnriched++
  }
}

// Also process entities that have rels but text refs without slugs
const needTextSlugs = ALL_CATALOG_ENTITIES.filter(
  e => e.relationships.length > 0 && e.texts.some(t => !t.slug)
)
console.log(`Processing ${needTextSlugs.length} entities needing text slugs...`)

for (const entity of needTextSlugs) {
  if (enrichmentPatch[entity.slug]) continue // already processed
  const textSlugs: Record<number, string> = {}
  entity.texts.forEach((t, i) => {
    if (!t.slug) {
      const slug = findTextSlug(t.title)
      if (slug) textSlugs[i] = slug
    }
  })
  if (Object.keys(textSlugs).length > 0) {
    enrichmentPatch[entity.slug] = {
      newRels: [],
      textSlugs,
      frameworks: [],
    }
    textSlugsAdded += Object.keys(textSlugs).length
  }
}

// Also fix div 600 entities that already have rels
const div600WithRels = ALL_CATALOG_ENTITIES.filter(
  e => e.callNumber.startsWith('600.') && e.relationships.length > 0 && !enrichmentPatch[e.slug]
)
for (const entity of div600WithRels) {
  enrichmentPatch[entity.slug] = {
    newRels: [],
    textSlugs: {},
    frameworks: [],
    callNumberFix: entity.callNumber.replace('600.', '680.'),
  }
  callNumbersFixed++
}

console.log(`\n=== Second-pass results ===`)
console.log(`Entities patched: ${Object.keys(enrichmentPatch).length}`)
console.log(`Relationships added: ${relsAdded}`)
console.log(`Text slugs added: ${textSlugsAdded}`)
console.log(`Frameworks enriched: ${fwsEnriched}`)
console.log(`Call numbers fixed (600→680): ${callNumbersFixed}`)

// ── Merge with existing enrichmentData.ts ──
// Read existing enrichment data
import { ENRICHMENT_DATA } from '../ui/src/data/catalog/enrichmentData'

const merged: Record<string, any> = { ...ENRICHMENT_DATA }

for (const [slug, patch] of Object.entries(enrichmentPatch)) {
  if (merged[slug]) {
    // Merge new rels
    const existingRels = merged[slug].newRels || []
    const existingRelKeys = new Set(existingRels.map((r: any) => `${r.verb}:${r.targetSlug}`))
    const uniqueNewRels = patch.newRels.filter(
      (r: EntityRelationship) => !existingRelKeys.has(`${r.verb}:${r.targetSlug}`)
    )
    merged[slug] = {
      newRels: [...existingRels, ...uniqueNewRels],
      textSlugs: { ...merged[slug].textSlugs, ...patch.textSlugs },
      frameworks: patch.frameworks.length > 0 ? patch.frameworks : merged[slug].frameworks,
      ...(patch.callNumberFix ? { callNumberFix: patch.callNumberFix } : {}),
    }
  } else {
    merged[slug] = patch
  }
}

// ── Write merged enrichmentData.ts ──
const outPath = path.resolve(__dirname, '../ui/src/data/catalog/enrichmentData.ts')

const entries: string[] = []
for (const [slug, data] of Object.entries(merged)) {
  const relsStr = (data.newRels || []).map((r: any) =>
    `{sourceSlug:${JSON.stringify(r.sourceSlug)},sourceName:${JSON.stringify(r.sourceName)},verb:${JSON.stringify(r.verb)},targetSlug:${JSON.stringify(r.targetSlug)},targetName:${JSON.stringify(r.targetName)}${r.context ? `,context:${JSON.stringify(r.context)}` : ''}}`
  ).join(',')
  const tsStr = JSON.stringify(data.textSlugs || {})
  const fwStr = JSON.stringify(data.frameworks || [])
  const cnStr = data.callNumberFix ? `,callNumberFix:${JSON.stringify(data.callNumberFix)}` : ''
  entries.push(`${JSON.stringify(slug)}:{newRels:[${relsStr}],textSlugs:${tsStr},frameworks:${fwStr}${cnStr}}`)
}

const fileContent = `/**
 * Auto-generated enrichment data — merged from two enrichment passes.
 * DO NOT EDIT MANUALLY. Regenerate via scripts/enrich_sparse.ts
 *
 * Pass 1 (enrich_all_entities.ts): cross-entity relationships, text slugs, frameworks
 * Pass 2 (enrich_sparse.ts): targeted enrichment for 0-relationship entities + div-600 fix
 */
import type { EntityRelationship } from '../entityTypes'

interface EnrichmentEntry {
  newRels: EntityRelationship[]
  textSlugs: Record<number, string>
  frameworks: string[]
  callNumberFix?: string
}

export const ENRICHMENT_DATA: Record<string, EnrichmentEntry> = {
${entries.join(',\n')}
}
`

fs.writeFileSync(outPath, fileContent, 'utf-8')
console.log(`\nWrote merged enrichmentData.ts (${Object.keys(merged).length} entries)`)

// Verify
const stillSparse = sparseEntities.filter(e => {
  const patch = enrichmentPatch[e.slug]
  return !patch || patch.newRels.length === 0
})
console.log(`Entities still with 0 rels after patch: ${stillSparse.length}`)
stillSparse.slice(0, 10).forEach(e => {
  console.log(`  ${e.slug} | ${e.label} | subj=${e.subjects.join(',')}`)
})
