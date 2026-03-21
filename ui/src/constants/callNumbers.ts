/**
 * Call Number Classification System
 *
 * Dewey-style "shelf address" for every node: Class.Division.Slug
 * Designed after the Library of Alexandria navigation metaphor.
 *
 * Classes 0–9 map to top-level node families:
 *   0 = Ideas (Core: Political, Ethical, Legal)
 *   1 = Ideas (Other: Economic, Scientific, Technological, Religious, Cultural, etc.)
 *   2 = People
 *   3 = Institutions
 *   4 = Places
 *   5 = Events
 *   6 = Movements
 *   7 = Artifacts & Texts
 *   8 = Evidence
 *   9 = Timeframes
 */

export interface ClassEntry {
  code: number
  heading: string
  nodeTypes: string[]
}

export interface DivisionEntry {
  code: string   // e.g. "010", "220", "510"
  heading: string
  parentClass: number
}

/* ── Top-Level Classes (the 10 shelves) ── */
export const CLASSES: ClassEntry[] = [
  { code: 0, heading: 'Ideas – Core Categories', nodeTypes: ['Political', 'Ethical', 'Legal'] },
  { code: 1, heading: 'Ideas – Other Theories', nodeTypes: ['Economic', 'Scientific', 'Technological', 'Religious', 'Cultural', 'Environmental', 'Artistic'] },
  { code: 2, heading: 'People', nodeTypes: ['Philosophers', 'Leaders', 'Scientists', 'Activists', 'Artists'] },
  { code: 3, heading: 'Institutions', nodeTypes: ['Political', 'Legal', 'Economic', 'Religious', 'Scientific', 'Cultural', 'International'] },
  { code: 4, heading: 'Places', nodeTypes: ['Continent', 'Region', 'Country', 'City', 'Empire', 'Civilization'] },
  { code: 5, heading: 'Events', nodeTypes: ['Wars', 'Revolutions', 'Elections', 'Scientific Discoveries', 'Environmental Crises'] },
  { code: 6, heading: 'Movements', nodeTypes: ['Political', 'Social', 'Religious', 'Cultural', 'Scientific', 'Technological', 'Environmental'] },
  { code: 7, heading: 'Artifacts & Texts', nodeTypes: ['Constitutions', 'Codes', 'Scriptures', 'Scientific Works', 'Artworks', 'Technologies'] },
  { code: 8, heading: 'Evidence', nodeTypes: ['Primary', 'Secondary', 'Archaeological', 'Quantitative', 'Oral'] },
  { code: 9, heading: 'Timeframes', nodeTypes: ['Period', 'Era', 'Epoch'] },
]

/* ── Second-Level Divisions ── */
export const DIVISIONS: DivisionEntry[] = [
  // 0 – Ideas (Core)
  { code: '010', heading: 'Political Systems & Governance', parentClass: 0 },
  { code: '020', heading: 'Ethical Systems', parentClass: 0 },
  { code: '030', heading: 'Legal Systems & Law', parentClass: 0 },

  // 1 – Ideas (Other)
  { code: '110', heading: 'Economic Theories & Systems', parentClass: 1 },
  { code: '120', heading: 'Scientific Paradigms', parentClass: 1 },
  { code: '130', heading: 'Technological Innovations', parentClass: 1 },
  { code: '140', heading: 'Religious & Philosophical Concepts', parentClass: 1 },
  { code: '150', heading: 'Social & Cultural Theories', parentClass: 1 },
  { code: '160', heading: 'Environmental & Ecological Ideas', parentClass: 1 },
  { code: '170', heading: 'Artistic & Aesthetic Movements', parentClass: 1 },

  // 2 – People
  { code: '210', heading: 'Philosophers & Thinkers', parentClass: 2 },
  { code: '220', heading: 'Political Leaders', parentClass: 2 },
  { code: '230', heading: 'Legal Figures', parentClass: 2 },
  { code: '240', heading: 'Scientists & Inventors', parentClass: 2 },
  { code: '250', heading: 'Religious Figures', parentClass: 2 },
  { code: '260', heading: 'Artists & Writers', parentClass: 2 },
  { code: '270', heading: 'Activists & Reformers', parentClass: 2 },

  // 3 – Institutions
  { code: '310', heading: 'Political Institutions', parentClass: 3 },
  { code: '320', heading: 'Legal Institutions', parentClass: 3 },
  { code: '330', heading: 'Economic Institutions', parentClass: 3 },
  { code: '340', heading: 'Religious Institutions', parentClass: 3 },
  { code: '350', heading: 'Scientific Institutions', parentClass: 3 },
  { code: '360', heading: 'Cultural Institutions', parentClass: 3 },
  { code: '370', heading: 'International Organizations', parentClass: 3 },
  { code: '390', heading: 'Military & Defense Organizations', parentClass: 3 },

  // 4 – Places
  { code: '410', heading: 'Continents', parentClass: 4 },
  { code: '420', heading: 'Regions', parentClass: 4 },
  { code: '430', heading: 'Countries / Polities', parentClass: 4 },
  { code: '440', heading: 'Cities', parentClass: 4 },
  { code: '450', heading: 'Empires / Dynasties', parentClass: 4 },
  { code: '460', heading: 'Civilizations', parentClass: 4 },
  { code: '470', heading: 'Culture Areas', parentClass: 4 },

  // 5 – Events
  { code: '510', heading: 'Wars & Conflicts', parentClass: 5 },
  { code: '520', heading: 'Revolutions & Uprisings', parentClass: 5 },
  { code: '530', heading: 'Elections & Political Shifts', parentClass: 5 },
  { code: '540', heading: 'Legal Cases', parentClass: 5 },
  { code: '550', heading: 'Scientific Discoveries', parentClass: 5 },
  { code: '560', heading: 'Technological Breakthroughs', parentClass: 5 },
  { code: '570', heading: 'Religious Events', parentClass: 5 },
  { code: '580', heading: 'Environmental Events', parentClass: 5 },

  // 6 – Movements
  { code: '610', heading: 'Political Movements', parentClass: 6 },
  { code: '620', heading: 'Social Movements', parentClass: 6 },
  { code: '630', heading: 'Religious Movements', parentClass: 6 },
  { code: '640', heading: 'Cultural Movements', parentClass: 6 },
  { code: '650', heading: 'Scientific Movements', parentClass: 6 },
  { code: '660', heading: 'Technological Movements', parentClass: 6 },
  { code: '670', heading: 'Environmental Movements', parentClass: 6 },

  // 7 – Artifacts & Texts
  { code: '710', heading: 'Constitutions & Charters', parentClass: 7 },
  { code: '720', heading: 'Legal Codes', parentClass: 7 },
  { code: '730', heading: 'Religious Texts', parentClass: 7 },
  { code: '740', heading: 'Philosophical Works', parentClass: 7 },
  { code: '750', heading: 'Scientific Texts', parentClass: 7 },
  { code: '760', heading: 'Artworks', parentClass: 7 },
  { code: '770', heading: 'Technological Artifacts', parentClass: 7 },

  // 8 – Evidence
  { code: '810', heading: 'Primary Sources', parentClass: 8 },
  { code: '820', heading: 'Secondary Sources', parentClass: 8 },
  { code: '830', heading: 'Archaeological Evidence', parentClass: 8 },
  { code: '840', heading: 'Quantitative Data', parentClass: 8 },
  { code: '850', heading: 'Oral Traditions', parentClass: 8 },

  // 9 – Timeframes
  { code: '910', heading: 'Prehistoric', parentClass: 9 },
  { code: '920', heading: 'Classical', parentClass: 9 },
  { code: '930', heading: 'Medieval', parentClass: 9 },
  { code: '940', heading: 'Early Modern', parentClass: 9 },
  { code: '950', heading: 'Modern', parentClass: 9 },
  { code: '960', heading: 'Contemporary', parentClass: 9 },
]

/* ── Color scheme by class (Golden Markers) ── */
export const CLASS_COLORS: Record<number, string> = {
  0: '#D4AF37', // Gold — Core Ideas
  1: '#C5963A', // Amber — Other Ideas
  2: '#3A7D44', // Green — People
  3: '#8B3A3A', // Empire Red — Institutions
  4: '#3B6BC2', // Blue — Places
  5: '#C5963A', // Amber — Events
  6: '#6B3FA0', // Purple — Movements
  7: '#5A2222', // Dark — Artifacts & Texts
  8: '#787469', // Stone — Evidence
  9: '#96770B', // Dark Gold — Timeframes
}

/* ── Helpers ── */

/** Parse components from a call number like "220.01-henry-viii" */
export function parseCallNumber(cn: string): { classCode: number; division: string; slug: string } | null {
  const match = cn.match(/^(\d)(\d{2})\.(\d+)-(.+)$/)
  if (!match) return null
  return {
    classCode: parseInt(match[1]),
    division: match[1] + match[2],          // e.g. "220"
    slug: match[4],                          // e.g. "henry-viii"
  }
}

/** Get the class heading from a call number */
export function getClassHeading(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return ''
  const cls = CLASSES.find(c => c.code === parsed.classCode)
  return cls?.heading || ''
}

/** Get the division heading from a call number */
export function getDivisionHeading(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return ''
  const div = DIVISIONS.find(d => d.code === parsed.division)
  return div?.heading || ''
}

/** Build breadcrumb trail from call number */
export function getCallNumberBreadcrumbs(cn: string): { label: string; prefix: string }[] {
  const parsed = parseCallNumber(cn)
  if (!parsed) return []
  const cls = CLASSES.find(c => c.code === parsed.classCode)
  const div = DIVISIONS.find(d => d.code === parsed.division)
  return [
    { label: cls?.heading || `Class ${parsed.classCode}`, prefix: `${parsed.classCode}` },
    { label: div?.heading || `Division ${parsed.division}`, prefix: parsed.division },
  ]
}

/** Get color for a call number based on its class */
export function getCallNumberColor(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return '#9E9A90'
  return CLASS_COLORS[parsed.classCode] || '#9E9A90'
}
