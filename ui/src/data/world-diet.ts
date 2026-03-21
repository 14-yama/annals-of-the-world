/* ─── Global Diet Data — Annals of the World ─── */
/* Dominant protein source by country (simplified for visualization) */

export type ProteinType = 'fish' | 'poultry' | 'beef' | 'pork' | 'lamb' | 'vegetarian'

export interface ProteinInfo {
  id: ProteinType
  name: string
  color: string
  icon: string
}

export const PROTEIN_TYPES: ProteinInfo[] = [
  { id: 'fish', name: 'Fish & Seafood', color: '#3182CE', icon: '🐟' },
  { id: 'poultry', name: 'Poultry (Chicken)', color: '#D69E2E', icon: '🐔' },
  { id: 'beef', name: 'Beef & Cattle', color: '#C53030', icon: '🐄' },
  { id: 'pork', name: 'Pork', color: '#ED64A6', icon: '🐷' },
  { id: 'lamb', name: 'Lamb & Goat', color: '#805AD5', icon: '🐑' },
  { id: 'vegetarian', name: 'Primarily Vegetarian', color: '#38A169', icon: '🌿' },
]

export const PROTEIN_MAP = Object.fromEntries(PROTEIN_TYPES.map(p => [p.id, p]))

/* Country → Dominant protein source (ISO_A3) */
export const COUNTRY_PROTEIN: Record<string, ProteinType> = {
  // Asia
  JPN: 'fish', KOR: 'pork', CHN: 'pork', TWN: 'pork',
  IND: 'vegetarian', PAK: 'poultry', BGD: 'fish', LKA: 'fish',
  NPL: 'vegetarian', BTN: 'beef', MMR: 'fish',
  THA: 'pork', VNM: 'pork', KHM: 'fish', LAO: 'fish',
  MYS: 'poultry', IDN: 'poultry', PHL: 'pork', SGP: 'poultry',
  TUR: 'poultry', IRN: 'lamb', IRQ: 'lamb', SYR: 'lamb',
  SAU: 'lamb', YEM: 'lamb', OMN: 'lamb', ARE: 'poultry',
  QAT: 'poultry', BHR: 'poultry', KWT: 'poultry', JOR: 'poultry',
  LBN: 'poultry', ISR: 'poultry', PSE: 'poultry',
  AFG: 'lamb', UZB: 'lamb', KAZ: 'lamb', TKM: 'lamb',
  KGZ: 'lamb', TJK: 'lamb', AZE: 'lamb', GEO: 'pork', ARM: 'beef',
  MNG: 'lamb', PRK: 'pork',
  // Europe
  GBR: 'poultry', FRA: 'poultry', DEU: 'pork', ESP: 'pork',
  ITA: 'pork', PRT: 'fish', NLD: 'pork', BEL: 'pork',
  AUT: 'pork', CHE: 'pork', POL: 'pork', CZE: 'pork',
  SVK: 'pork', HUN: 'pork', ROU: 'pork', BGR: 'pork',
  GRC: 'lamb', SRB: 'pork', HRV: 'pork', SVN: 'pork',
  BIH: 'beef', MNE: 'lamb', MKD: 'pork', ALB: 'lamb',
  UKR: 'pork', BLR: 'pork', MDA: 'poultry', LTU: 'pork',
  LVA: 'pork', EST: 'pork', FIN: 'pork', SWE: 'pork',
  NOR: 'fish', DNK: 'pork', ISL: 'fish', IRL: 'beef',
  RUS: 'pork', LUX: 'pork',
  // Africa
  EGY: 'poultry', LBY: 'lamb', TUN: 'poultry', DZA: 'lamb',
  MAR: 'poultry', MRT: 'lamb', SDN: 'lamb', SSD: 'beef',
  ETH: 'beef', SOM: 'lamb', DJI: 'lamb', ERI: 'lamb',
  NGA: 'poultry', GHA: 'fish', CMR: 'fish', SEN: 'fish',
  MLI: 'fish', BFA: 'poultry', NER: 'lamb', TCD: 'beef',
  GIN: 'fish', CIV: 'fish', TGO: 'fish', BEN: 'fish',
  SLE: 'fish', LBR: 'fish', GMB: 'fish', GNB: 'fish',
  GAB: 'fish', COG: 'fish', COD: 'fish', AGO: 'fish',
  CAF: 'beef', GNQ: 'fish',
  KEN: 'beef', TZA: 'fish', UGA: 'beef', RWA: 'beef',
  BDI: 'beef', MOZ: 'fish', MWI: 'fish', ZMB: 'beef',
  ZWE: 'beef', BWA: 'beef', NAM: 'beef', ZAF: 'poultry',
  SWZ: 'beef', LSO: 'beef', MDG: 'fish',
  // Americas
  USA: 'poultry', CAN: 'poultry', MEX: 'poultry',
  BRA: 'poultry', ARG: 'beef', COL: 'poultry', VEN: 'poultry',
  PER: 'poultry', CHL: 'poultry', ECU: 'poultry', BOL: 'poultry',
  PRY: 'beef', URY: 'beef', GUY: 'poultry', SUR: 'poultry',
  GTM: 'poultry', HND: 'poultry', SLV: 'poultry', NIC: 'poultry',
  CRI: 'poultry', PAN: 'poultry', CUB: 'pork', HTI: 'poultry',
  DOM: 'poultry', JAM: 'poultry', TTO: 'poultry',
  // Oceania
  AUS: 'poultry', NZL: 'lamb', PNG: 'fish', FJI: 'fish',
  SLB: 'fish', VUT: 'fish', WSM: 'fish', TON: 'fish',
}
