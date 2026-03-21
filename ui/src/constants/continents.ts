/* ─── Continent Constants — Annals of the World ─── */
import type { Continent } from '../types'

export const CONTINENTS: Continent[] = [
  {
    id: 'africa',
    name: 'Africa',
    description: 'The cradle of humankind — 55 nations spanning ancient civilizations to modern independence movements. Home to the world\'s youngest population and richest mineral reserves.',
    countries: 55,
    color: '#DD6B20',
    icon: '🌍',
    heroImage: 'https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800',
    highlights: [
      { title: 'Youth Continent', value: '19.7 years', detail: 'Median age — youngest continent' },
      { title: 'Mineral Wealth', value: '30%', detail: 'World mineral reserves' },
      { title: '3% GDP Paradox', value: '~$2.7T', detail: '17% of world population, 3% GDP' },
    ],
    stats: [
      { label: 'Countries', value: '55', color: '#DD6B20' },
      { label: 'Population', value: '1.4B', color: '#E53E3E' },
      { label: 'Languages', value: '2,000+', color: '#805AD5' },
      { label: 'Land Area', value: '30.3M km²', color: '#38A169' },
    ],
  },
  {
    id: 'asia',
    name: 'Asia',
    description: 'The largest and most populous continent — 48 nations from ancient Silk Road civilizations to modern technological powerhouses. 60% of humanity calls Asia home.',
    countries: 48,
    color: '#C53030',
    icon: '🌏',
    heroImage: 'https://images.unsplash.com/photo-1480796927426-f609979314bd?w=800',
    highlights: [
      { title: 'Population Giant', value: '4.7B', detail: '60% of world population' },
      { title: 'Wealth Gap', value: '228:1', detail: 'GDP per capita: Qatar vs Afghanistan' },
      { title: 'Cultural Cradle', value: '5 Asias', detail: 'East, South, Southeast, Central, West' },
    ],
    stats: [
      { label: 'Countries', value: '48', color: '#C53030' },
      { label: 'Population', value: '4.7B', color: '#DD6B20' },
      { label: 'Languages', value: '2,300+', color: '#805AD5' },
      { label: 'Land Area', value: '44.6M km²', color: '#38A169' },
    ],
  },
  {
    id: 'europe',
    name: 'Europe',
    description: 'A continent of empires, revolutions, and Enlightenment — 44 nations that shaped modern governance, science, and art. From Greek democracy to the European Union.',
    countries: 44,
    color: '#3182CE',
    icon: '🌍',
    heroImage: 'https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800',
    highlights: [
      { title: 'Democratic Roots', value: '508 BCE', detail: 'Athenian democracy — first in history' },
      { title: 'Colonial Legacy', value: '84%', detail: 'Of world colonized by European powers' },
      { title: 'EU Integration', value: '27 nations', detail: 'Largest peaceful political union' },
    ],
    stats: [
      { label: 'Countries', value: '44', color: '#3182CE' },
      { label: 'Population', value: '750M', color: '#DD6B20' },
      { label: 'Languages', value: '200+', color: '#805AD5' },
      { label: 'Land Area', value: '10.2M km²', color: '#38A169' },
    ],
  },
  {
    id: 'americas',
    name: 'Americas',
    description: 'Two continents spanning from Arctic tundra to Patagonia — 35 nations shaped by indigenous civilizations, European colonization, and revolutionary independence movements.',
    countries: 35,
    color: '#38A169',
    icon: '🌎',
    heroImage: 'https://images.unsplash.com/photo-1518179786525-ace88f8da8b0?w=800',
    highlights: [
      { title: 'Ancient Heritage', value: '15,000 years', detail: 'Indigenous civilizations: Maya, Aztec, Inca' },
      { title: 'Migration Hub', value: '1B+', detail: 'Population from diverse global origins' },
      { title: 'Economic Power', value: '$30T+', detail: 'Combined GDP (North + South America)' },
    ],
    stats: [
      { label: 'Countries', value: '35', color: '#38A169' },
      { label: 'Population', value: '1.0B', color: '#DD6B20' },
      { label: 'Languages', value: '1,000+', color: '#805AD5' },
      { label: 'Land Area', value: '42.5M km²', color: '#E53E3E' },
    ],
  },
  {
    id: 'oceania',
    name: 'Oceania',
    description: 'Island nations and continental Australia — 14 countries spanning vast Pacific waters, ancient Aboriginal cultures, and diverse marine ecosystems.',
    countries: 14,
    color: '#38B2AC',
    icon: '🌊',
    heroImage: 'https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=800',
    highlights: [
      { title: 'Oldest Civilization', value: '65,000 years', detail: 'Aboriginal Australians — longest continuous culture' },
      { title: 'Pacific Navigators', value: '25,000+', detail: 'Islands across the vast Pacific Ocean' },
      { title: 'Biodiversity', value: 'Unique', detail: '80% of species found nowhere else (Australia)' },
    ],
    stats: [
      { label: 'Countries', value: '14', color: '#38B2AC' },
      { label: 'Population', value: '45M', color: '#DD6B20' },
      { label: 'Languages', value: '1,300+', color: '#805AD5' },
      { label: 'Land Area', value: '8.5M km²', color: '#38A169' },
    ],
  },
]

export function getContinentById(id: string): Continent | undefined {
  return CONTINENTS.find(c => c.id === id)
}
