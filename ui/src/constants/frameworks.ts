/* ─── Interpretive Frameworks — Annals of the World ─── */
/* Source of truth: docs/guidelines/framework_matrix.md */
import type { Framework } from '../types'

export const FRAMEWORKS: Framework[] = [
  {
    id: 'CAUSE_AND_EFFECT',
    name: 'Cause & Effect',
    description: 'Foregrounds causal chains, technological or institutional drivers, and immediate impacts.',
    verbs: ['CAUSES', 'ENABLES', 'TRIGGERS', 'TRANSFORMS'],
    relatedFrameworks: ['CULTURAL_DIFFUSION', 'ADAPTATION', 'CONFLICT_AND_RESOLUTION'],
    color: '#E53E3E',
    icon: 'Zap',
  },
  {
    id: 'CULTURAL_DIFFUSION',
    name: 'Cultural Diffusion',
    description: 'Transmission, borrowing, and spread of practices or ideas across regions and groups.',
    verbs: ['DIFFUSES', 'INTRODUCES', 'ADAPTS', 'ADOPTS'],
    relatedFrameworks: ['CAUSE_AND_EFFECT', 'TEXTUAL_TRANSMISSION', 'ADAPTATION'],
    color: '#38A169',
    icon: 'Globe',
  },
  {
    id: 'DOCTRINE_DEVELOPMENT',
    name: 'Doctrine Development',
    description: 'Formalization, systematization, and canonical consolidation within traditions.',
    verbs: ['CANONIZES', 'SYSTEMATIZES', 'STANDARDIZES', 'INTERPRETS'],
    relatedFrameworks: ['TEXTUAL_TRANSMISSION', 'LEGAL_INTERPRETATION'],
    color: '#805AD5',
    icon: 'BookOpen',
  },
  {
    id: 'TEXTUAL_TRANSMISSION',
    name: 'Textual Transmission',
    description: 'Copying, translation, editorial history, and preservation of texts.',
    verbs: ['TRANSMITS', 'TRANSLATES', 'PRESERVES', 'EDITS'],
    relatedFrameworks: ['DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    color: '#D69E2E',
    icon: 'Scroll',
  },
  {
    id: 'LEGAL_INTERPRETATION',
    name: 'Legal Interpretation',
    description: 'Jurisprudential, canonical, or administrative rulings and their reform.',
    verbs: ['INTERPRETS', 'CODIFIES', 'REFORMS', 'REJECTS'],
    relatedFrameworks: ['DOCTRINE_DEVELOPMENT', 'RITUAL_STANDARDIZATION'],
    color: '#2B6CB0',
    icon: 'Scale',
  },
  {
    id: 'RITUAL_STANDARDIZATION',
    name: 'Ritual Standardization',
    description: 'Formalization and institutional adoption of ritual practice across communities.',
    verbs: ['STANDARDIZES', 'INSTITUTES', 'REGULATES'],
    relatedFrameworks: ['LEGAL_INTERPRETATION', 'DOCTRINE_DEVELOPMENT'],
    color: '#B7791F',
    icon: 'Flame',
  },
  {
    id: 'GEOPOLITICAL_LINKAGE',
    name: 'Geopolitical Linkage',
    description: 'Imperial, diplomatic, and territorial relationships that reorganize authority.',
    verbs: ['LINKS', 'CONNECTS', 'RECONFIGURES'],
    relatedFrameworks: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION'],
    color: '#C53030',
    icon: 'Map',
  },
  {
    id: 'CONFLICT_AND_RESOLUTION',
    name: 'Conflict & Resolution',
    description: 'Schisms, wars, negotiations, reconciliations and their effects.',
    verbs: ['CAUSES', 'RESOLVES', 'RADICALIZES', 'RECONCILES_WITH'],
    relatedFrameworks: ['GEOPOLITICAL_LINKAGE', 'ADAPTATION'],
    color: '#9B2C2C',
    icon: 'Swords',
  },
  {
    id: 'ADAPTATION',
    name: 'Adaptation',
    description: 'Contextual reinterpretation and local reworking of imported practices or ideas.',
    verbs: ['ADAPTS', 'TRANSFORMS', 'REINTERPRETS'],
    relatedFrameworks: ['CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT'],
    color: '#2F855A',
    icon: 'RefreshCw',
  },
  {
    id: 'TEMPORAL_LINKAGE',
    name: 'Temporal Linkage',
    description: 'Ordering and periodization claims connecting events across time.',
    verbs: ['PRECEDES', 'FOLLOWS', 'IS_ANTECEDENT_TO'],
    relatedFrameworks: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION'],
    color: '#4A5568',
    icon: 'Clock',
  },
]

export const FRAMEWORK_MAP = Object.fromEntries(
  FRAMEWORKS.map(f => [f.id, f])
) as Record<string, Framework>
