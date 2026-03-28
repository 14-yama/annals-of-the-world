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

const ERA_MAP = {
  prehistoric:  { eraSlug: 'prehistoric',    era: 'Prehistoric' },
  ancient:      { eraSlug: 'classical',      era: 'Classical / Ancient' },
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

export const ALL_TOPIC_ENTITIES = [
  ...WEAPONS_ENTITIES,
  ...MEDICINE_ENTITIES,
  ...ARCHITECTURE_ENTITIES,
  ...AGRICULTURE_ENTITIES,
  ...NAVIGATION_ENTITIES,
  ...LANGUAGES_ENTITIES,
]
