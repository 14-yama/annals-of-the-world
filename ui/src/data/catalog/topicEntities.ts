/**
 * Topic Entities — converts all 6 topic collections into Entity objects
 * for catalog integration. Each topic gets its own call number class.
 *
 * Call number classes:
 *   560 — Weapons & Warfare
 *   570 — Medicine & Healing
 *   580 — Architecture & Monuments
 *   590 — Agriculture & Food
 *   600 — Navigation & Exploration
 *   610 — Languages & Scripts
 */
import { convertTopicItems } from './topicConverter'
import { WEAPONS } from '../weapons'
import { MEDICINES } from '../medicine'
import { ARCHITECTURE } from '../architecture'
import { AGRICULTURE } from '../agriculture'
import { NAVIGATION } from '../navigation'
import { LANGUAGES } from '../languages'
import { TRIBES } from '../tribes'
import { TRANSPORTATION } from '../transportation'
import { CLOTHING } from '../clothing'
import { MARRIAGES } from '../marriage'
import { CUSTOMS } from '../customs'
import { PUNISHMENTS } from '../punishment'
import { IDEAS } from '../ideas'
import type { Entity } from '../entityTypes'

const ERA_MAP = {
  prehistoric:  { eraSlug: 'prehistoric',    era: 'Prehistoric' },
  ancient:      { eraSlug: 'classical',      era: 'Classical' },
  medieval:     { eraSlug: 'medieval',        era: 'Medieval' },
  earlyModern:  { eraSlug: 'early-modern',   era: 'Early Modern' },
  modern:       { eraSlug: 'modern',          era: 'Modern' },
  contemporary: { eraSlug: 'contemporary',    era: 'Contemporary' },
}

export const WEAPONS_ENTITIES = convertTopicItems(WEAPONS, {
  classPrefix: '560', label: 'EventWindow', topicTag: 'Weapons & Warfare', eraMap: ERA_MAP,
})

export const MEDICINE_ENTITIES = convertTopicItems(MEDICINES, {
  classPrefix: '570', label: 'Idea', topicTag: 'Medicine & Healing', eraMap: ERA_MAP,
})

export const ARCHITECTURE_ENTITIES = convertTopicItems(ARCHITECTURE, {
  classPrefix: '580', label: 'Place', topicTag: 'Architecture & Monuments', eraMap: ERA_MAP,
})

export const AGRICULTURE_ENTITIES = convertTopicItems(AGRICULTURE, {
  classPrefix: '590', label: 'Idea', topicTag: 'Agriculture & Food', eraMap: ERA_MAP,
})

export const NAVIGATION_ENTITIES = convertTopicItems(NAVIGATION, {
  classPrefix: '600', label: 'EventWindow', topicTag: 'Navigation & Exploration', eraMap: ERA_MAP,
})

export const LANGUAGES_ENTITIES = convertTopicItems(LANGUAGES, {
  classPrefix: '610', label: 'Idea', topicTag: 'Languages & Scripts', eraMap: ERA_MAP,
})

export const TRIBES_ENTITIES = convertTopicItems(TRIBES, {
  classPrefix: '620', label: 'Movement', topicTag: 'Tribes & Peoples', eraMap: ERA_MAP,
})

export const TRANSPORTATION_ENTITIES = convertTopicItems(TRANSPORTATION, {
  classPrefix: '630', label: 'EventWindow', topicTag: 'Transportation', eraMap: ERA_MAP,
})

export const CLOTHING_ENTITIES = convertTopicItems(CLOTHING, {
  classPrefix: '640', label: 'Idea', topicTag: 'Clothing & Textiles', eraMap: ERA_MAP,
})

export const MARRIAGE_ENTITIES = convertTopicItems(MARRIAGES, {
  classPrefix: '650', label: 'Movement', topicTag: 'Marriage & Union', eraMap: ERA_MAP,
})

export const CUSTOMS_ENTITIES = convertTopicItems(CUSTOMS, {
  classPrefix: '660', label: 'Movement', topicTag: 'Customs & Traditions', eraMap: ERA_MAP,
})

export const PUNISHMENT_ENTITIES = convertTopicItems(PUNISHMENTS, {
  classPrefix: '670', label: 'EventWindow', topicTag: 'Corporal Punishment & Justice', eraMap: ERA_MAP,
})

/* Ideas use a different shape — convert manually */
function inferContinent(origin: string): string {
  const o = origin.toLowerCase()
  if (/africa|egypt|nubian|ethiop|nile|sahara/.test(o)) return 'Africa'
  if (/china|india|persia|mesopotamia|arab|japan|korea|ottoman|anatolia|levant|phoenici/.test(o)) return 'Asia'
  if (/europe|greek|roman|britain|france|germany|italy|vienna|england|scotland|switzerland/.test(o)) return 'Europe'
  if (/america|brazil|mexico/.test(o)) return 'Americas'
  if (/australia|oceania/.test(o)) return 'Oceania'
  return 'Cross-Regional'
}

export const IDEAS_ENTITIES: Entity[] = IDEAS.map((idea, i) => {
  const eraInfo = ERA_MAP[idea.era as keyof typeof ERA_MAP] ?? { eraSlug: idea.era, era: idea.era }
  return {
    slug: idea.slug,
    name: idea.name,
    label: 'Idea' as const,
    callNumber: `680.${String(i + 1).padStart(2, '0')}-${idea.slug}`,
    subjectHeadings: ['Ideas & Thought', idea.domain, idea.subdomain],
    subjects: ['Ideas & Thought', idea.domain, idea.subdomain, idea.originator, idea.originPlace],
    summary: idea.description,
    period: idea.yearLabel,
    era: eraInfo.era,
    eraSlug: eraInfo.eraSlug,
    region: idea.region,
    continent: inferContinent(idea.originPlace),
    status: 'published',
    frameworks: ['CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION'],
    causes: idea.parentIdeas.map(slug => ({ title: slug, type: 'Parent Idea', year: '' })),
    effects: [{ title: idea.impact, type: 'Historical Impact', year: idea.yearLabel }],
    relationships: [],
    places: [{ name: idea.originPlace, role: 'Origin' }],
    texts: [],
  }
})

export const ALL_TOPIC_ENTITIES = [
  ...WEAPONS_ENTITIES,
  ...MEDICINE_ENTITIES,
  ...ARCHITECTURE_ENTITIES,
  ...AGRICULTURE_ENTITIES,
  ...NAVIGATION_ENTITIES,
  ...LANGUAGES_ENTITIES,
  ...TRIBES_ENTITIES,
  ...TRANSPORTATION_ENTITIES,
  ...CLOTHING_ENTITIES,
  ...MARRIAGE_ENTITIES,
  ...CUSTOMS_ENTITIES,
  ...PUNISHMENT_ENTITIES,
  ...IDEAS_ENTITIES,
]
