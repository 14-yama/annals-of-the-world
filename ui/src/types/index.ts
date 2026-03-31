/* ─── Core Domain Types — Annals of the World ─── */

/* === Node Labels (matches Neo4j schema v4) === */
export type NodeLabel =
  | 'Person' | 'Place' | 'Institution' | 'Text' | 'Event'
  | 'Idea' | 'Movement' | 'Evidence' | 'Corpus' | 'Framework'
  | 'Timeframe' | 'Polity' | 'EventWindow'

/* === Eras === */
export interface Era {
  id: string
  name: string
  years: string
  startYear: number
  endYear: number
  description: string
  color: string
  events: number
  regions: string[]
  heroImage: string
  civilizations: Civilization[]
}

/* === Civilizations / Cultures within an Era === */
export interface Civilization {
  id: string
  name: string
  region: string
  period: string
  description: string
  images: StockImage[]
  keyFacts: string[]
}

/* === Stock imagery metadata === */
export interface StockImage {
  id: string
  alt: string
  url: string          // Unsplash/Pexels URL or local asset
  credit: string
  category: 'artifact' | 'architecture' | 'landscape' | 'portrait' | 'map' | 'art'
}

/* === Geographic Region === */
export interface Region {
  id: string
  name: string
  continent: ContinentId
  countries: string[]
  color: string
}

/* === Continent === */
export type ContinentId = 'africa' | 'asia' | 'europe' | 'americas' | 'oceania'

export interface Continent {
  id: ContinentId
  name: string
  description: string
  countries: number
  color: string
  icon: string
  heroImage: string
  highlights: ContinentHighlight[]
  stats: ContinentStat[]
}

export interface ContinentHighlight {
  title: string
  value: string
  detail: string
}

export interface ContinentStat {
  label: string
  value: string
  color: string
}

/* === Country Profile (simplified for skeleton data) === */
export interface CountryProfile {
  slug: string
  name: string
  capital: string
  region: string
  continent: ContinentId
  population: string
  area: string
  independence: string
  currency: string
  languages: string[]
  description: string
}

/* === Knowledge Graph Types === */
export interface GraphNode {
  slug: string
  name: string
  label: NodeLabel
  cluster: string
  description: string
  key?: string
  x: number
  y: number
  vx: number
  vy: number
  edgeCount: number
  radius: number
  visible: boolean
}

export interface GraphEdge {
  source: string
  target: string
  type: string
  cluster: string
  weight: number
}

/* === Quiz Types === */
export type QuizDifficulty = 'beginner' | 'intermediate' | 'advanced' | 'expert'

export interface QuizQuestion {
  id: string
  question: string
  options: string[]
  correctIndex: number
  explanation: string
  era?: string
  region?: string
  difficulty: QuizDifficulty
  category: 'people' | 'events' | 'places' | 'ideas' | 'artifacts' | 'movements'
}

export interface QuizSession {
  id: string
  title: string
  description: string
  difficulty: QuizDifficulty
  questions: QuizQuestion[]
  era?: string
  region?: string
}

export interface QuizResult {
  sessionId: string
  score: number
  total: number
  answers: { questionId: string; selectedIndex: number; correct: boolean }[]
  completedAt: Date
}

/* === Timeline Types === */
export interface TimelineEvent {
  id: string
  title: string
  year: number
  endYear?: number
  description: string
  era: string
  region: string
  category: NodeLabel
  significance: 'low' | 'medium' | 'high' | 'critical'
  imageUrl?: string
}

/* === Map Types === */
export interface MapMarker {
  id: string
  name: string
  lat: number
  lng: number
  type: NodeLabel
  era?: string
  description: string
  color: string
}

/* === Interpretive Framework Types === */
export type FrameworkId =
  | 'CAUSE_AND_EFFECT' | 'CULTURAL_DIFFUSION' | 'DOCTRINE_DEVELOPMENT'
  | 'TEXTUAL_TRANSMISSION' | 'LEGAL_INTERPRETATION' | 'RITUAL_STANDARDIZATION'
  | 'GEOPOLITICAL_LINKAGE' | 'CONFLICT_AND_RESOLUTION' | 'ADAPTATION'
  | 'TEMPORAL_LINKAGE' | 'ECONOMIC_SYSTEMS' | 'POLITICAL_SYSTEMS'
  | 'COMPARATIVE_RELIGION' | 'EMPIRE_AND_COLONIALISM' | 'ENVIRONMENTAL_HISTORY'
  | 'INNOVATION_AND_TECHNOLOGY'

export interface Framework {
  id: FrameworkId
  name: string
  description: string
  verbs: string[]
  relatedFrameworks: FrameworkId[]
  color: string
  icon: string
}

/* === Causal Chain Types (for case studies) === */
export interface CausalNode {
  id: string
  title: string
  year: number
  description: string
  era: string
  region: string
  framework: FrameworkId
}

export interface CausalEdge {
  source: string
  target: string
  verb: string
  framework: FrameworkId
  evidence: string
  description: string
}

export interface CaseStudy {
  id: string
  title: string
  subtitle: string
  description: string
  era: string
  region: string
  frameworks: FrameworkId[]
  nodes: CausalNode[]
  edges: CausalEdge[]
  keyInsight: string
}
