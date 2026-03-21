/* ─── World Language Families — Annals of the World ─── */
/* Primary language family by country (ISO_A3 → language family) */

export interface LanguageFamilyInfo {
  id: string
  name: string
  color: string
  speakers: string
  originRegion: string
  examples: string[]
}

export const LANGUAGE_FAMILIES: LanguageFamilyInfo[] = [
  { id: 'indo-european', name: 'Indo-European', color: '#4A90D9', speakers: '3.2 billion', originRegion: 'Pontic Steppe', examples: ['English', 'Spanish', 'Hindi', 'Russian', 'Portuguese'] },
  { id: 'sino-tibetan', name: 'Sino-Tibetan', color: '#E53E3E', speakers: '1.3 billion', originRegion: 'Yellow River Basin', examples: ['Mandarin', 'Cantonese', 'Burmese', 'Tibetan'] },
  { id: 'afro-asiatic', name: 'Afro-Asiatic', color: '#D4AF37', speakers: '500 million', originRegion: 'Horn of Africa / Levant', examples: ['Arabic', 'Amharic', 'Hausa', 'Hebrew', 'Somali'] },
  { id: 'niger-congo', name: 'Niger-Congo', color: '#38A169', speakers: '700 million', originRegion: 'West Africa', examples: ['Swahili', 'Yoruba', 'Zulu', 'Igbo', 'Shona'] },
  { id: 'austronesian', name: 'Austronesian', color: '#805AD5', speakers: '400 million', originRegion: 'Taiwan', examples: ['Malay', 'Tagalog', 'Javanese', 'Malagasy', 'Hawaiian'] },
  { id: 'dravidian', name: 'Dravidian', color: '#DD6B20', speakers: '250 million', originRegion: 'Indian Subcontinent', examples: ['Tamil', 'Telugu', 'Kannada', 'Malayalam'] },
  { id: 'turkic', name: 'Turkic', color: '#D69E2E', speakers: '200 million', originRegion: 'Central Asia', examples: ['Turkish', 'Uzbek', 'Kazakh', 'Azerbaijani'] },
  { id: 'japonic', name: 'Japonic', color: '#ED64A6', speakers: '128 million', originRegion: 'Japan', examples: ['Japanese', 'Ryukyuan'] },
  { id: 'koreanic', name: 'Koreanic', color: '#319795', speakers: '80 million', originRegion: 'Korean Peninsula', examples: ['Korean'] },
  { id: 'tai-kadai', name: 'Tai-Kadai', color: '#9F7AEA', speakers: '95 million', originRegion: 'Southern China', examples: ['Thai', 'Lao'] },
  { id: 'austroasiatic', name: 'Austroasiatic', color: '#667EEA', speakers: '117 million', originRegion: 'Southeast Asia', examples: ['Vietnamese', 'Khmer', 'Mon'] },
  { id: 'uralic', name: 'Uralic', color: '#63B3ED', speakers: '25 million', originRegion: 'Ural Mountains', examples: ['Finnish', 'Hungarian', 'Estonian'] },
  { id: 'other', name: 'Other / Isolate', color: '#A0AEC0', speakers: 'Varies', originRegion: 'Various', examples: ['Basque', 'Georgian', 'Ainu'] },
]

export const LANGUAGE_FAMILY_MAP = Object.fromEntries(LANGUAGE_FAMILIES.map(f => [f.id, f]))

/* Country → Primary language family (ISO_A3 codes) */
export const COUNTRY_LANGUAGE_FAMILY: Record<string, string> = {
  // Europe
  GBR: 'indo-european', FRA: 'indo-european', DEU: 'indo-european', ESP: 'indo-european',
  ITA: 'indo-european', PRT: 'indo-european', NLD: 'indo-european', BEL: 'indo-european',
  AUT: 'indo-european', CHE: 'indo-european', POL: 'indo-european', CZE: 'indo-european',
  SVK: 'indo-european', HUN: 'uralic', ROU: 'indo-european', BGR: 'indo-european',
  GRC: 'indo-european', SRB: 'indo-european', HRV: 'indo-european', SVN: 'indo-european',
  BIH: 'indo-european', MNE: 'indo-european', MKD: 'indo-european', ALB: 'indo-european',
  UKR: 'indo-european', BLR: 'indo-european', MDA: 'indo-european', LTU: 'indo-european',
  LVA: 'indo-european', EST: 'uralic', FIN: 'uralic', SWE: 'indo-european',
  NOR: 'indo-european', DNK: 'indo-european', ISL: 'indo-european', IRL: 'indo-european',
  RUS: 'indo-european', LUX: 'indo-european',
  // Asia
  CHN: 'sino-tibetan', JPN: 'japonic', KOR: 'koreanic', PRK: 'koreanic',
  IND: 'indo-european', PAK: 'indo-european', BGD: 'indo-european', LKA: 'indo-european',
  NPL: 'indo-european', BTN: 'sino-tibetan', MMR: 'sino-tibetan',
  THA: 'tai-kadai', VNM: 'austroasiatic', KHM: 'austroasiatic', LAO: 'tai-kadai',
  MYS: 'austronesian', IDN: 'austronesian', PHL: 'austronesian', SGP: 'sino-tibetan',
  TUR: 'turkic', IRN: 'indo-european', IRQ: 'afro-asiatic', SYR: 'afro-asiatic',
  SAU: 'afro-asiatic', YEM: 'afro-asiatic', OMN: 'afro-asiatic', ARE: 'afro-asiatic',
  QAT: 'afro-asiatic', BHR: 'afro-asiatic', KWT: 'afro-asiatic', JOR: 'afro-asiatic',
  LBN: 'afro-asiatic', ISR: 'afro-asiatic', PSE: 'afro-asiatic',
  AFG: 'indo-european', UZB: 'turkic', KAZ: 'turkic', TKM: 'turkic',
  KGZ: 'turkic', TJK: 'indo-european', AZE: 'turkic', GEO: 'other', ARM: 'indo-european',
  MNG: 'other', TWN: 'sino-tibetan',
  // Africa
  EGY: 'afro-asiatic', LBY: 'afro-asiatic', TUN: 'afro-asiatic', DZA: 'afro-asiatic',
  MAR: 'afro-asiatic', MRT: 'afro-asiatic', SDN: 'afro-asiatic', SSD: 'niger-congo',
  ETH: 'afro-asiatic', SOM: 'afro-asiatic', DJI: 'afro-asiatic', ERI: 'afro-asiatic',
  NGA: 'niger-congo', GHA: 'niger-congo', CMR: 'niger-congo', SEN: 'niger-congo',
  MLI: 'niger-congo', BFA: 'niger-congo', NER: 'niger-congo', TCD: 'afro-asiatic',
  GIN: 'niger-congo', CIV: 'niger-congo', TGO: 'niger-congo', BEN: 'niger-congo',
  SLE: 'niger-congo', LBR: 'niger-congo', GMB: 'niger-congo', GNB: 'niger-congo',
  GAB: 'niger-congo', COG: 'niger-congo', COD: 'niger-congo', AGO: 'niger-congo',
  CAF: 'niger-congo', GNQ: 'niger-congo',
  KEN: 'niger-congo', TZA: 'niger-congo', UGA: 'niger-congo', RWA: 'niger-congo',
  BDI: 'niger-congo', MOZ: 'niger-congo', MWI: 'niger-congo', ZMB: 'niger-congo',
  ZWE: 'niger-congo', BWA: 'niger-congo', NAM: 'niger-congo', ZAF: 'niger-congo',
  SWZ: 'niger-congo', LSO: 'niger-congo', MDG: 'austronesian',
  // Americas
  USA: 'indo-european', CAN: 'indo-european', MEX: 'indo-european',
  BRA: 'indo-european', ARG: 'indo-european', COL: 'indo-european', VEN: 'indo-european',
  PER: 'indo-european', CHL: 'indo-european', ECU: 'indo-european', BOL: 'indo-european',
  PRY: 'indo-european', URY: 'indo-european', GUY: 'indo-european', SUR: 'indo-european',
  GTM: 'indo-european', HND: 'indo-european', SLV: 'indo-european', NIC: 'indo-european',
  CRI: 'indo-european', PAN: 'indo-european', CUB: 'indo-european', HTI: 'indo-european',
  DOM: 'indo-european', JAM: 'indo-european', TTO: 'indo-european',
  // Oceania
  AUS: 'indo-european', NZL: 'indo-european', PNG: 'other', FJI: 'austronesian',
  SLB: 'austronesian', VUT: 'austronesian', WSM: 'austronesian', TON: 'austronesian',
}
