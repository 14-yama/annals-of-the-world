/**
 * Entity Type Definitions
 *
 * Shared interfaces for the entity/catalog data layer.
 * Extracted to avoid circular dependencies between catalog data files and entities.ts.
 */

export interface EntityRelationship {
  sourceSlug: string
  sourceName: string
  verb: string
  targetSlug: string
  targetName: string
  context?: string
}

export interface EntityCause {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityEffect {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityPlace {
  name: string
  role: string
  slug?: string
}

export interface EntityText {
  title: string
  type: string
  year?: string
  slug?: string
}

export type NodeLabel =
  | 'Person'
  | 'Idea'
  | 'Institution'
  | 'Place'
  | 'EventWindow'
  | 'Movement'
  | 'Text'
  | 'Evidence'

export interface Entity {
  slug: string
  name: string
  label: NodeLabel
  callNumber: string
  subjectHeadings: string[]
  subjects: string[]
  summary: string
  born?: string
  died?: string
  founded?: string
  period?: string
  startDate?: string
  endDate?: string
  era: string
  eraSlug: string
  eraDivision?: string      // Specific sub-period (e.g. "Age of Enlightenment")
  eraDivisionCode?: string  // Dewey code (e.g. "944")
  region: string
  continent: string
  status: string
  frameworks?: string[]
  causes: EntityCause[]
  effects: EntityEffect[]
  relationships: EntityRelationship[]
  places: EntityPlace[]
  texts: EntityText[]

  /* ── v2 attributes (Appwrite backend + enrichment) ── */
  wikidataQid?: string
  wikipediaUrl?: string
  imageUrl?: string
  thumbnailUrl?: string
  importanceScore?: number
  altNames?: string[]
  externalLinks?: string[]
  tags?: string[]
  quote?: string
  legacySummary?: string
}
