/**
 * Corpus Metadata — display config for the 14 textual tradition collections.
 * No entity data — entities are fetched from the Appwrite backend.
 * `searchTerm` is used to query the backend for matching entities.
 */
export interface CorpusMeta {
  slug: string
  name: string
  shortName: string
  description: string
  color: string
  zone: string
  searchTerm: string
}

export const CORPUS_META: CorpusMeta[] = [
  {
    slug: 'biblical',
    name: 'The Biblical Corpus',
    shortName: 'Biblical',
    description: 'Genesis through Revelation — patriarchs, prophets, gospels, and epistles.',
    color: '#8B3A3A',
    zone: 'Near East',
    searchTerm: 'Biblical',
  },
  {
    slug: 'mesopotamian',
    name: 'The Mesopotamian Corpus',
    shortName: 'Mesopotamian',
    description: 'Sumer, Akkad, Babylon & Assyria — cuneiform tablets, epics, and law codes.',
    color: '#6B4D1B',
    zone: 'Near East',
    searchTerm: 'Mesopotamian',
  },
  {
    slug: 'egyptian',
    name: 'The Egyptian Corpus',
    shortName: 'Egyptian',
    description: 'Pharaonic Egypt — pyramid texts, papyri, and temple inscriptions.',
    color: '#C5963A',
    zone: 'Near East',
    searchTerm: 'Egyptian',
  },
  {
    slug: 'judaic-rabbinic',
    name: 'The Judaic Rabbinic Corpus',
    shortName: 'Judaic Rabbinic',
    description: 'Talmud, Mishnah, and the oral tradition of rabbinic Judaism.',
    color: '#96770B',
    zone: 'Near East',
    searchTerm: 'Rabbinic',
  },
  {
    slug: 'graeco-roman',
    name: 'The Graeco-Roman Corpus',
    shortName: 'Graeco-Roman',
    description: 'Greek philosophy, Roman law, and the classical literary tradition.',
    color: '#4A90D9',
    zone: 'Near East',
    searchTerm: 'Graeco-Roman',
  },
  {
    slug: 'canon-law',
    name: 'The Canon Law Corpus',
    shortName: 'Canon Law',
    description: 'Ecclesiastical law — decretals, councils, and papal governance.',
    color: '#5A2222',
    zone: 'Near East',
    searchTerm: 'Canon Law',
  },
  {
    slug: 'iran-central-asia',
    name: 'The Iran & Central Asia Corpus',
    shortName: 'Iran & Central Asia',
    description: 'Zoroastrian, Islamic, and Persianate literary traditions.',
    color: '#2F855A',
    zone: 'Iran & Central Asia',
    searchTerm: 'Persian',
  },
  {
    slug: 'south-se-asia',
    name: 'The South & Southeast Asian Corpus',
    shortName: 'South & SE Asia',
    description: 'Vedic, Buddhist, and Indic literary traditions of the subcontinent.',
    color: '#DD6B20',
    zone: 'South & SE Asia',
    searchTerm: 'Vedic',
  },
  {
    slug: 'east-asia',
    name: 'The East Asian Corpus',
    shortName: 'East Asia',
    description: 'Confucian classics, Japanese court literature, and Korean scholarship.',
    color: '#C53030',
    zone: 'East Asia',
    searchTerm: 'Confucian',
  },
  {
    slug: 'africa',
    name: 'The African Corpus',
    shortName: 'Africa',
    description: "Ge'ez manuscripts, Timbuktu libraries, and West African oral epics.",
    color: '#38B2AC',
    zone: 'Africa',
    searchTerm: 'African',
  },
  {
    slug: 'americas',
    name: 'The Americas Corpus',
    shortName: 'Americas',
    description: 'Mesoamerican codices, Andean chronicles, and indigenous knowledge.',
    color: '#805AD5',
    zone: 'Americas',
    searchTerm: 'Mesoamerican',
  },
  {
    slug: 'europe-major',
    name: 'European Corpuses — Major Traditions',
    shortName: 'Europe (Major)',
    description: 'Byzantine, Latin, Iberian, Nordic, and other major European literary traditions.',
    color: '#A67C2E',
    zone: 'Europe',
    searchTerm: 'Byzantine',
  },
  {
    slug: 'europe-regional',
    name: 'European Corpuses — Regional Traditions',
    shortName: 'Europe (Regional)',
    description: 'Georgian, Hungarian, Czech, Balkan, Venetian, and other regional traditions.',
    color: '#6B3FA0',
    zone: 'Europe',
    searchTerm: 'Georgian',
  },
  {
    slug: 'science-tech',
    name: 'The Science & Technology Corpus',
    shortName: 'Science & Tech',
    description: 'Military manuals, the Scientific Revolution, and foundational scientific texts.',
    color: '#4A90D9',
    zone: 'Cross-Regional',
    searchTerm: 'Scientific',
  },
]

export function getCorpusMeta(slug: string): CorpusMeta | undefined {
  return CORPUS_META.find(c => c.slug === slug)
}
