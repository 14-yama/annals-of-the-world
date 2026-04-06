/**
 * Era Division Constants — Shared across curator tools and entity pages
 *
 * Maps the 6 canonical eras to their sub-period divisions (codes 911–963).
 * Used for dropdowns, validation, and display throughout the app.
 */

export interface EraDivision {
  code: string
  heading: string
  parentEra: string      // Display name: 'Prehistoric', 'Classical', etc.
  parentEraSlug: string  // URL slug: 'prehistoric', 'classical', etc.
  color: string
}

/** Canonical era names as stored in the Appwrite backend */
export const ERA_NAMES = [
  'Prehistoric',
  'Classical',
  'Medieval',
  'Early Modern',
  'Modern',
  'Contemporary',
] as const

export type EraName = (typeof ERA_NAMES)[number]

/** Map from era name → slug used in routes/URLs */
export const ERA_SLUG_MAP: Record<EraName, string> = {
  Prehistoric: 'prehistoric',
  Classical: 'classical',
  Medieval: 'medieval',
  'Early Modern': 'early-modern',
  Modern: 'modern',
  Contemporary: 'contemporary',
}

/** Map from era name → theme color */
export const ERA_COLOR_MAP: Record<EraName, string> = {
  Prehistoric: '#6B4D1B',
  Classical: '#8B4513',
  Medieval: '#A67C2E',
  'Early Modern': '#C5963A',
  Modern: '#4A90D9',
  Contemporary: '#6B3FA0',
}

/** All 21 era sub-divisions with parent era linkage */
export const ERA_DIVISIONS: EraDivision[] = [
  // Prehistoric (910 range)
  { code: '911', heading: 'Paleolithic & Mesolithic',  parentEra: 'Prehistoric',    parentEraSlug: 'prehistoric',  color: '#6B4D1B' },
  { code: '912', heading: 'Neolithic & Chalcolithic',  parentEra: 'Prehistoric',    parentEraSlug: 'prehistoric',  color: '#6B4D1B' },
  { code: '913', heading: 'Bronze Age',                parentEra: 'Prehistoric',    parentEraSlug: 'prehistoric',  color: '#6B4D1B' },

  // Classical (920 range)
  { code: '921', heading: 'Archaic Period',            parentEra: 'Classical',      parentEraSlug: 'classical',    color: '#8B4513' },
  { code: '922', heading: 'Hellenistic Period',        parentEra: 'Classical',      parentEraSlug: 'classical',    color: '#8B4513' },
  { code: '923', heading: 'Roman Period',              parentEra: 'Classical',      parentEraSlug: 'classical',    color: '#8B4513' },
  { code: '924', heading: 'Late Antiquity',            parentEra: 'Classical',      parentEraSlug: 'classical',    color: '#8B4513' },

  // Medieval (930 range)
  { code: '931', heading: 'Early Medieval / Dark Ages', parentEra: 'Medieval',      parentEraSlug: 'medieval',     color: '#A67C2E' },
  { code: '932', heading: 'High Medieval',             parentEra: 'Medieval',       parentEraSlug: 'medieval',     color: '#A67C2E' },
  { code: '933', heading: 'Late Medieval',             parentEra: 'Medieval',       parentEraSlug: 'medieval',     color: '#A67C2E' },

  // Early Modern (940 range)
  { code: '941', heading: 'Age of Exploration',        parentEra: 'Early Modern',   parentEraSlug: 'early-modern', color: '#C5963A' },
  { code: '942', heading: 'Renaissance Period',        parentEra: 'Early Modern',   parentEraSlug: 'early-modern', color: '#C5963A' },
  { code: '943', heading: 'Reformation Era',           parentEra: 'Early Modern',   parentEraSlug: 'early-modern', color: '#C5963A' },
  { code: '944', heading: 'Age of Enlightenment',      parentEra: 'Early Modern',   parentEraSlug: 'early-modern', color: '#C5963A' },

  // Modern (950 range)
  { code: '951', heading: 'Industrial Age',            parentEra: 'Modern',         parentEraSlug: 'modern',       color: '#4A90D9' },
  { code: '952', heading: 'Age of Empire',             parentEra: 'Modern',         parentEraSlug: 'modern',       color: '#4A90D9' },
  { code: '953', heading: 'Interwar Period',           parentEra: 'Modern',         parentEraSlug: 'modern',       color: '#4A90D9' },
  { code: '954', heading: 'World War II Era',          parentEra: 'Modern',         parentEraSlug: 'modern',       color: '#4A90D9' },

  // Contemporary (960 range)
  { code: '961', heading: 'Cold War Era',              parentEra: 'Contemporary',   parentEraSlug: 'contemporary', color: '#6B3FA0' },
  { code: '962', heading: 'Post-Cold War',             parentEra: 'Contemporary',   parentEraSlug: 'contemporary', color: '#6B3FA0' },
  { code: '963', heading: 'Digital Age',               parentEra: 'Contemporary',   parentEraSlug: 'contemporary', color: '#6B3FA0' },
]

/** Get divisions for a specific era name */
export function getDivisionsForEra(era: string): EraDivision[] {
  return ERA_DIVISIONS.filter(d => d.parentEra === era)
}

/** Validate that an era division code matches the given era */
export function isValidEraDivision(era: string, divisionCode: string): boolean {
  const div = ERA_DIVISIONS.find(d => d.code === divisionCode)
  return div ? div.parentEra === era : false
}

/** Get the parent era for a division code */
export function getEraForDivision(divisionCode: string): string | null {
  const div = ERA_DIVISIONS.find(d => d.code === divisionCode)
  return div?.parentEra ?? null
}
