/**
 * Topic Registry — metadata + entity arrays for all civilization-shaping topics.
 * Used by the TopicPage hub and sidebar navigation.
 * Mirrors the pattern of corpuses/registry.ts.
 */
import type { Entity } from '../entityTypes'
import {
  WEAPONS_ENTITIES,
  MEDICINE_ENTITIES,
  ARCHITECTURE_ENTITIES,
  AGRICULTURE_ENTITIES,
  NAVIGATION_ENTITIES,
  LANGUAGES_ENTITIES,
  TRIBES_ENTITIES,
  TRANSPORTATION_ENTITIES,
  CLOTHING_ENTITIES,
  MARRIAGE_ENTITIES,
  CUSTOMS_ENTITIES,
  PUNISHMENT_ENTITIES,
} from './topicEntities'

export interface TopicEntry {
  slug: string
  name: string
  shortName: string
  description: string
  color: string
  icon: string
  route: string
  entities: Entity[]
}

export const TOPIC_REGISTRY: TopicEntry[] = [
  {
    slug: 'weapons',
    name: 'Arms & Warfare',
    shortName: 'Weapons',
    description: 'From stone axes to hypersonic missiles — every weapon that shaped the battlefield.',
    color: '#8B3A3A',
    icon: 'Swords',
    route: '/weapons',
    entities: WEAPONS_ENTITIES,
  },
  {
    slug: 'medicine',
    name: 'Medicine & Healing',
    shortName: 'Medicine',
    description: 'From herbal remedies to gene therapy — the medical breakthroughs that extended human life.',
    color: '#2F855A',
    icon: 'Heart',
    route: '/medicine',
    entities: MEDICINE_ENTITIES,
  },
  {
    slug: 'architecture',
    name: 'Architecture & Monuments',
    shortName: 'Architecture',
    description: 'From Göbekli Tepe to parametric skyscrapers — humanity\'s built environment.',
    color: '#C5963A',
    icon: 'Building2',
    route: '/architecture',
    entities: ARCHITECTURE_ENTITIES,
  },
  {
    slug: 'agriculture',
    name: 'Agriculture & Food',
    shortName: 'Agriculture',
    description: 'From wild grain gathering to vertical farms — how we learned to feed 8 billion.',
    color: '#38A169',
    icon: 'Wheat',
    route: '/agriculture',
    entities: AGRICULTURE_ENTITIES,
  },
  {
    slug: 'navigation',
    name: 'Navigation & Exploration',
    shortName: 'Navigation',
    description: 'From star-guided canoes to GPS satellites — charting the unknown.',
    color: '#3182CE',
    icon: 'Compass',
    route: '/navigation',
    entities: NAVIGATION_ENTITIES,
  },
  {
    slug: 'languages',
    name: 'Languages & Scripts',
    shortName: 'Languages',
    description: 'From cave paintings to Unicode — the evolution of human communication.',
    color: '#6B3FA0',
    icon: 'BookOpen',
    route: '/languages',
    entities: LANGUAGES_ENTITIES,
  },
  {
    slug: 'tribes',
    name: 'Tribes & Peoples',
    shortName: 'Tribes',
    description: 'From the San Bushmen to the Mongol hordes — every tribe that shaped human history.',
    color: '#8B6914',
    icon: 'Users',
    route: '/tribes',
    entities: TRIBES_ENTITIES,
  },
  {
    slug: 'transportation',
    name: 'Transportation',
    shortName: 'Transport',
    description: 'From dugout canoes to spacecraft — every breakthrough in human mobility.',
    color: '#3182CE',
    icon: 'TrainFront',
    route: '/transportation',
    entities: TRANSPORTATION_ENTITIES,
  },
  {
    slug: 'clothing',
    name: 'Clothing & Textiles',
    shortName: 'Clothing',
    description: 'From animal hides to smart fabrics — every fiber and fashion revolution.',
    color: '#9B2C6E',
    icon: 'Shirt',
    route: '/clothing',
    entities: CLOTHING_ENTITIES,
  },
  {
    slug: 'marriage',
    name: 'Marriage & Union',
    shortName: 'Marriage',
    description: 'From pair bonding to same-sex marriage — every form of union across 12,000 years.',
    color: '#C53D6E',
    icon: 'Heart',
    route: '/marriage',
    entities: MARRIAGE_ENTITIES,
  },
  {
    slug: 'customs',
    name: 'Customs & Traditions',
    shortName: 'Customs',
    description: 'From burial rites to digital etiquette — the rituals and social rules that defined civilizations.',
    color: '#B8860B',
    icon: 'Crown',
    route: '/customs',
    entities: CUSTOMS_ENTITIES,
  },
  {
    slug: 'punishment',
    name: 'Corporal Punishment & Justice',
    shortName: 'Punishment',
    description: 'From blood feud to restorative justice — how civilizations punished and reformed.',
    color: '#B22222',
    icon: 'Gavel',
    route: '/punishment',
    entities: PUNISHMENT_ENTITIES,
  },
]

export function getTopicBySlug(slug: string): TopicEntry | undefined {
  return TOPIC_REGISTRY.find(t => t.slug === slug)
}
