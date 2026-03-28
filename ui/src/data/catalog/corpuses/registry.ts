/**
 * Corpus Registry — metadata + entity arrays for every corpus.
 * Used by the generic CorpusPage and sidebar navigation.
 */
import type { Entity } from '../../entityTypes'

import { BIBLICAL_ENTITIES } from '../biblical'
import { MESOPOTAMIAN_ENTITIES } from './mesopotamian'
import { EGYPTIAN_ENTITIES } from './egyptian'
import { JUDAIC_RABBINIC_ENTITIES } from './judaicRabbinic'
import { GRAECO_ROMAN_ENTITIES } from './graecoRoman'
import { CANON_LAW_ENTITIES } from './canonLaw'
import { IRAN_CENTRAL_ASIA_ENTITIES } from './iranCentralAsia'
import { SOUTH_SE_ASIA_ENTITIES } from './southSEAsia'
import { EAST_ASIA_ENTITIES } from './eastAsia'
import { AFRICA_ENTITIES } from './africa'
import { AMERICAS_ENTITIES } from './americas'
import { EUROPE_BATCH1_ENTITIES } from './europeBatch1'
import { EUROPE_BATCH2_ENTITIES } from './europeBatch2'
import { SCIENCE_TECH_ENTITIES } from './scienceTech'

export interface CorpusEntry {
  slug: string
  name: string
  shortName: string
  description: string
  color: string
  zone: string
  entities: Entity[]
}

export const CORPUS_REGISTRY: CorpusEntry[] = [
  {
    slug: 'biblical',
    name: 'The Biblical Corpus',
    shortName: 'Biblical',
    description: 'Genesis through Revelation — patriarchs, prophets, gospels, and epistles.',
    color: '#8B3A3A',
    zone: 'Near East',
    entities: BIBLICAL_ENTITIES,
  },
  {
    slug: 'mesopotamian',
    name: 'The Mesopotamian Corpus',
    shortName: 'Mesopotamian',
    description: 'Sumer, Akkad, Babylon & Assyria — cuneiform tablets, epics, and law codes.',
    color: '#6B4D1B',
    zone: 'Near East',
    entities: MESOPOTAMIAN_ENTITIES,
  },
  {
    slug: 'egyptian',
    name: 'The Egyptian Corpus',
    shortName: 'Egyptian',
    description: 'Pharaonic Egypt — pyramid texts, papyri, and temple inscriptions.',
    color: '#C5963A',
    zone: 'Near East',
    entities: EGYPTIAN_ENTITIES,
  },
  {
    slug: 'judaic-rabbinic',
    name: 'The Judaic Rabbinic Corpus',
    shortName: 'Judaic Rabbinic',
    description: 'Talmud, Mishnah, and the oral tradition of rabbinic Judaism.',
    color: '#96770B',
    zone: 'Near East',
    entities: JUDAIC_RABBINIC_ENTITIES,
  },
  {
    slug: 'graeco-roman',
    name: 'The Graeco-Roman Corpus',
    shortName: 'Graeco-Roman',
    description: 'Greek philosophy, Roman law, and the classical literary tradition.',
    color: '#4A90D9',
    zone: 'Near East',
    entities: GRAECO_ROMAN_ENTITIES,
  },
  {
    slug: 'canon-law',
    name: 'The Canon Law Corpus',
    shortName: 'Canon Law',
    description: 'Ecclesiastical law — decretals, councils, and papal governance.',
    color: '#5A2222',
    zone: 'Near East',
    entities: CANON_LAW_ENTITIES,
  },
  {
    slug: 'iran-central-asia',
    name: 'The Iran & Central Asia Corpus',
    shortName: 'Iran & Central Asia',
    description: 'Zoroastrian, Islamic, and Persianate literary traditions.',
    color: '#2F855A',
    zone: 'Iran & Central Asia',
    entities: IRAN_CENTRAL_ASIA_ENTITIES,
  },
  {
    slug: 'south-se-asia',
    name: 'The South & Southeast Asian Corpus',
    shortName: 'South & SE Asia',
    description: 'Vedic, Buddhist, and Indic literary traditions of the subcontinent.',
    color: '#DD6B20',
    zone: 'South & SE Asia',
    entities: SOUTH_SE_ASIA_ENTITIES,
  },
  {
    slug: 'east-asia',
    name: 'The East Asian Corpus',
    shortName: 'East Asia',
    description: 'Confucian classics, Japanese court literature, and Korean scholarship.',
    color: '#C53030',
    zone: 'East Asia',
    entities: EAST_ASIA_ENTITIES,
  },
  {
    slug: 'africa',
    name: 'The African Corpus',
    shortName: 'Africa',
    description: "Ge'ez manuscripts, Timbuktu libraries, and West African oral epics.",
    color: '#38B2AC',
    zone: 'Africa',
    entities: AFRICA_ENTITIES,
  },
  {
    slug: 'americas',
    name: 'The Americas Corpus',
    shortName: 'Americas',
    description: 'Mesoamerican codices, Andean chronicles, and indigenous knowledge.',
    color: '#805AD5',
    zone: 'Americas',
    entities: AMERICAS_ENTITIES,
  },
  {
    slug: 'europe-major',
    name: 'European Corpuses — Major Traditions',
    shortName: 'Europe (Major)',
    description: 'Byzantine, Latin, Iberian, Nordic, and other major European literary traditions.',
    color: '#A67C2E',
    zone: 'Europe',
    entities: EUROPE_BATCH1_ENTITIES,
  },
  {
    slug: 'europe-regional',
    name: 'European Corpuses — Regional Traditions',
    shortName: 'Europe (Regional)',
    description: 'Georgian, Hungarian, Czech, Balkan, Venetian, and other regional traditions.',
    color: '#6B3FA0',
    zone: 'Europe',
    entities: EUROPE_BATCH2_ENTITIES,
  },
  {
    slug: 'science-tech',
    name: 'The Science & Technology Corpus',
    shortName: 'Science & Tech',
    description: 'Military manuals, the Scientific Revolution, and foundational scientific texts.',
    color: '#4A90D9',
    zone: 'Cross-Regional',
    entities: SCIENCE_TECH_ENTITIES,
  },
]

export function getCorpusBySlug(slug: string): CorpusEntry | undefined {
  return CORPUS_REGISTRY.find(c => c.slug === slug)
}
