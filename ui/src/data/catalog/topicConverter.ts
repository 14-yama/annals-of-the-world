/**
 * Topic Entity Converter — transforms flat topic items (weapons, medicine, etc.)
 * into proper Entity objects so they appear in the catalog with full tabs.
 */
import type { Entity, NodeLabel } from '../entityTypes'

/** The flat shape shared by weapons, medicine, architecture, agriculture, navigation, languages */
interface TopicItem {
  slug: string
  name: string
  era: string
  category: string
  subcategory: string
  origin: string
  civilization: string
  yearIntroduced: string
  description: string
  impact: string
}

interface TopicConfig {
  /** Call number class prefix, e.g. '560' for weapons */
  classPrefix: string
  /** NodeLabel for all entities in this topic */
  label: NodeLabel
  /** Topic tag used in subjects */
  topicTag: string
  /** Map era slugs → eraSlug values used in the Entity interface */
  eraMap: Record<string, { eraSlug: string; era: string }>
}

const ERA_MAP: Record<string, { eraSlug: string; era: string }> = {
  prehistoric:  { eraSlug: 'prehistoric',    era: 'Prehistoric' },
  ancient:      { eraSlug: 'classical',      era: 'Classical / Ancient' },
  medieval:     { eraSlug: 'medieval',        era: 'Medieval' },
  earlyModern:  { eraSlug: 'early-modern',   era: 'Early Modern' },
  modern:       { eraSlug: 'modern',          era: 'Modern' },
  contemporary: { eraSlug: 'contemporary',    era: 'Contemporary' },
}

/** Map topic tags to proper framework IDs */
const TOPIC_TO_FRAMEWORK: Record<string, string[]> = {
  'Weapons & Warfare':           ['CONFLICT_AND_RESOLUTION', 'INNOVATION_AND_TECHNOLOGY'],
  'Medicine & Healing':          ['INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
  'Architecture & Monuments':    ['INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION'],
  'Agriculture & Food':          ['ENVIRONMENTAL_HISTORY', 'ECONOMIC_SYSTEMS'],
  'Navigation & Exploration':    ['EMPIRE_AND_COLONIALISM', 'INNOVATION_AND_TECHNOLOGY'],
  'Languages & Scripts':         ['CULTURAL_DIFFUSION', 'TEXTUAL_TRANSMISSION'],
  'Tribes & Peoples':            ['CULTURAL_DIFFUSION', 'POLITICAL_SYSTEMS'],
  'Transportation':              ['INNOVATION_AND_TECHNOLOGY', 'ECONOMIC_SYSTEMS'],
  'Clothing & Textiles':         ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS'],
  'Marriage & Union':            ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'],
  'Customs & Traditions':        ['CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION'],
  'Corporal Punishment & Justice': ['POLITICAL_SYSTEMS', 'CONFLICT_AND_RESOLUTION'],
}

export function convertTopicItems(
  items: TopicItem[],
  config: TopicConfig
): Entity[] {
  let counter = 1
  return items.map((item): Entity => {
    const eraInfo = config.eraMap[item.era] ?? ERA_MAP[item.era] ?? { eraSlug: item.era, era: item.era }
    const callNumber = `${config.classPrefix}.${String(counter++).padStart(2, '0')}-${item.slug}`
    return {
      slug: item.slug,
      name: item.name,
      label: config.label,
      callNumber,
      subjectHeadings: [config.topicTag, item.category, item.subcategory],
      subjects: [config.topicTag, item.category, item.subcategory, item.civilization, item.origin],
      summary: item.description,
      period: item.yearIntroduced,
      era: eraInfo.era,
      eraSlug: eraInfo.eraSlug,
      region: item.origin,
      continent: inferContinent(item.origin, item.civilization),
      status: 'published',
      frameworks: TOPIC_TO_FRAMEWORK[config.topicTag] ?? ['CULTURAL_DIFFUSION'],
      causes: [],
      effects: [{
        title: item.impact,
        type: 'Historical Impact',
        year: item.yearIntroduced,
      }],
      relationships: [],
      places: item.origin !== 'Global' && item.origin !== 'Multiple' ? [{
        name: item.origin,
        role: 'Origin',
      }] : [],
      texts: [],
    }
  })
}

function inferContinent(origin: string, civilization: string): string {
  const combined = `${origin} ${civilization}`.toLowerCase()
  if (/africa|egyptian|nubian|ethiop|timbuktu|nile|sahara|morocco|mali|ghana|swahili|zulu|bantu/.test(combined)) return 'Africa'
  if (/china|chinese|japan|korea|mongol|song|ming|tang|han|zhou|shang|qin|vietnam|tibet|khmer|angkor|southeast asia|austronesian|polynesi|pacific|java|indonesia|malay|burm|thai|india|hindu|vedic|mughal|gupta|maurya|persian|persia|iran|ottoman|arab|islamic|mesopotamia|sumerian|akkad|babylon|assyria|fertile|anatolia|levant|phoenici|yemen/.test(combined)) return 'Asia'
  if (/europe|roman|greek|byzantine|frank|germanic|norse|viking|celtic|gaul|british|english|french|german|dutch|spanish|italian|portuguese|scandinavian|poland|russia|flanders|sicily|medieval|carolingian/.test(combined)) return 'Europe'
  if (/america|aztec|maya|inca|olmec|mesoamerican|caribbean|brazil|mexico|andes|peru|united states|canada|navajo/.test(combined)) return 'Americas'
  if (/australia|oceania|maori|aboriginal/.test(combined)) return 'Oceania'
  if (/global|multiple|cross-regional/.test(combined)) return 'Cross-Regional'
  return 'Cross-Regional'
}
