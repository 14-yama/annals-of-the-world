/* ─── Region Constants — Annals of the World ─── */
import type { Region } from '../types'

export const REGIONS: Region[] = [
  { id: 'east-asia',       name: 'East Asia',       continent: 'asia',     countries: ['China', 'Japan', 'Korea', 'Mongolia', 'Taiwan'],                  color: '#C53030' },
  { id: 'south-asia',      name: 'South Asia',      continent: 'asia',     countries: ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal'],          color: '#DD6B20' },
  { id: 'southeast-asia',  name: 'Southeast Asia',  continent: 'asia',     countries: ['Indonesia', 'Thailand', 'Vietnam', 'Philippines', 'Myanmar'],     color: '#D69E2E' },
  { id: 'central-asia',    name: 'Central Asia',    continent: 'asia',     countries: ['Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan'],         color: '#38A169' },
  { id: 'west-asia',       name: 'West Asia',       continent: 'asia',     countries: ['Turkey', 'Iran', 'Iraq', 'Saudi Arabia', 'Israel'],               color: '#3182CE' },
  { id: 'north-africa',    name: 'North Africa',    continent: 'africa',   countries: ['Egypt', 'Libya', 'Tunisia', 'Algeria', 'Morocco'],                color: '#805AD5' },
  { id: 'west-africa',     name: 'West Africa',     continent: 'africa',   countries: ['Nigeria', 'Ghana', 'Senegal', 'Mali', 'Côte d\'Ivoire'],          color: '#D53F8C' },
  { id: 'east-africa',     name: 'East Africa',     continent: 'africa',   countries: ['Kenya', 'Tanzania', 'Ethiopia', 'Uganda', 'Somalia'],             color: '#E53E3E' },
  { id: 'central-africa',  name: 'Central Africa',  continent: 'africa',   countries: ['DR Congo', 'Cameroon', 'Chad', 'Congo', 'CAR'],                  color: '#ED8936' },
  { id: 'southern-africa', name: 'Southern Africa', continent: 'africa',   countries: ['South Africa', 'Zimbabwe', 'Mozambique', 'Botswana', 'Namibia'], color: '#48BB78' },
  { id: 'western-europe',  name: 'Western Europe',  continent: 'europe',   countries: ['UK', 'France', 'Germany', 'Italy', 'Spain', 'Netherlands'],       color: '#4299E1' },
  { id: 'eastern-europe',  name: 'Eastern Europe',  continent: 'europe',   countries: ['Russia', 'Poland', 'Ukraine', 'Romania', 'Czech Republic'],       color: '#9F7AEA' },
  { id: 'americas',        name: 'Americas',        continent: 'americas', countries: ['USA', 'Brazil', 'Mexico', 'Canada', 'Argentina', 'Peru'],         color: '#F56565' },
  { id: 'oceania',         name: 'Oceania',         continent: 'oceania',  countries: ['Australia', 'New Zealand', 'Papua New Guinea', 'Fiji'],            color: '#38B2AC' },
]

export function getRegionById(id: string): Region | undefined {
  return REGIONS.find(r => r.id === id)
}

export function getRegionsByContinent(continent: string): Region[] {
  return REGIONS.filter(r => r.continent === continent)
}
