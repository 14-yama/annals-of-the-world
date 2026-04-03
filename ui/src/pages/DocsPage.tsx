import React, { useState, useMemo } from 'react'
import { Box, Flex, Text, SimpleGrid, Heading } from '@chakra-ui/react'
import {
  BookOpen, FileText, Network, Shield, Layers, Search,
  ChevronDown, ChevronUp, Users, Landmark, MapPin, Clock, Zap,
} from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'

/* ── Colour tokens ── */
const MARBLE_BG = '#FAFAF8'
const CARD_BG   = '#F5F4F0'
const BORDER    = '#E4E2DC'
const GOLD      = '#D4AF37'
const DARK_TEXT = '#2D2A24'
const MED_TEXT  = '#524E44'
const MUTED     = '#787469'

/* ═══════════════════════════════════════════════════════════════
   Edge / Relationship Verb Glossary
   ═══════════════════════════════════════════════════════════════ */

interface VerbEntry {
  verb: string
  semantics: string
  allowedPairs: string
  notes: string
  tier: 'Core' | 'Supplementary' | 'Corpus'
}

const VERB_GLOSSARY: VerbEntry[] = [
  // Corpus verbs
  { verb: 'CONTAINS', semantics: 'Corpus includes a text or sub-corpus', allowedPairs: 'C → T / C → C', notes: 'Structural membership within a corpus', tier: 'Corpus' },
  { verb: 'INCLUDES', semantics: 'Broader inclusion within corpus', allowedPairs: 'C → T', notes: 'Use CONTAINS for strict sub-part', tier: 'Corpus' },
  { verb: 'ORGANIZES', semantics: 'Corpus structures or arranges texts', allowedPairs: 'C → T', notes: '', tier: 'Corpus' },
  { verb: 'CANONIZES', semantics: 'Confers canonical status', allowedPairs: 'I/P → T/D / C → T', notes: 'Only when formal recognition documented', tier: 'Core' },
  { verb: 'SUBSUMES', semantics: 'Corpus absorbs another corpus', allowedPairs: 'C → C', notes: 'Use for corpus hierarchy', tier: 'Corpus' },
  { verb: 'SPLITS_INTO', semantics: 'Corpus divides into sub-corpora', allowedPairs: 'C → C', notes: '', tier: 'Corpus' },
  { verb: 'IS_PART_OF', semantics: 'Part–whole structural membership', allowedPairs: 'C/E/T → C/E/T', notes: 'Not for causality or loose association', tier: 'Core' },

  // Core canon (high-frequency)
  { verb: 'FRAMES', semantics: 'Lenses an interpretation through a framework', allowedPairs: 'Any → F', notes: 'Only with explicit interpretive layer', tier: 'Core' },
  { verb: 'OCCURS_IN', semantics: 'Event/process location anchor', allowedPairs: 'E → L', notes: 'Single primary place per edge', tier: 'Core' },
  { verb: 'CAUSES', semantics: 'Direct causal contribution', allowedPairs: 'E/T/D/M → E/D', notes: 'Not for weak correlation', tier: 'Core' },
  { verb: 'TRANSFORMS', semantics: 'Deep structural change', allowedPairs: 'E/T/M → D/I/T', notes: 'Provide before/after note', tier: 'Core' },
  { verb: 'STANDARDIZES', semantics: 'Imposes uniform practice/text', allowedPairs: 'I/P → D/T', notes: 'Distinct from CANONIZES', tier: 'Core' },
  { verb: 'PRESERVES', semantics: 'Actively conserves text/practice', allowedPairs: 'I/P → T/D', notes: 'When continuity risk documented', tier: 'Core' },
  { verb: 'DEFINES', semantics: 'Establishes doctrinal/textual definition', allowedPairs: 'I/P/T → D/T', notes: 'Councils, doctrinal formulae', tier: 'Core' },
  { verb: 'SCHISMS_FROM', semantics: 'Formal separation or split', allowedPairs: 'M/I → M/I', notes: 'Must have structural rupture', tier: 'Core' },
  { verb: 'RECONCILES_WITH', semantics: 'Restores communion/unity', allowedPairs: 'M/I/P → M/I/P', notes: 'Reciprocal edge optional', tier: 'Core' },
  { verb: 'DIFFUSES', semantics: 'Spreads across geography/traditions', allowedPairs: 'M/P/I → L/M/D/T', notes: 'Must show transmission vector', tier: 'Core' },
  { verb: 'COMMENTATES_ON', semantics: 'Writes formal commentary', allowedPairs: 'P → T/D', notes: 'More specific than INTERPRETS', tier: 'Core' },
  { verb: 'DECLARES', semantics: 'Announces formal status/event', allowedPairs: 'P/I → E/D', notes: 'Public proclamation', tier: 'Core' },
  { verb: 'ORGANIZES', semantics: 'Coordinates congress/campaign/event', allowedPairs: 'P/I → E/M', notes: 'Event node must exist', tier: 'Core' },
  { verb: 'ESTABLISHES', semantics: 'Founds institution/practice', allowedPairs: 'P/I → I/D', notes: 'Not for minor reforms', tier: 'Core' },
  { verb: 'TRANSLATES', semantics: 'Renders text into another language', allowedPairs: 'P/I → T', notes: 'Requires linguistic shift', tier: 'Core' },
  { verb: 'AUTHORS', semantics: 'Creates an original text/work', allowedPairs: 'P/I → T', notes: 'Alias: WRITES', tier: 'Core' },
  { verb: 'PUBLISHES', semantics: 'Issues a work publicly', allowedPairs: 'P/I → T', notes: 'First issuance only', tier: 'Core' },
  { verb: 'EDITS', semantics: 'Produces edited/redacted form', allowedPairs: 'P/I → T', notes: 'Include edition descriptor', tier: 'Core' },
  { verb: 'ADOPTS', semantics: 'Takes up doctrine/practice', allowedPairs: 'P/I/M → D/T', notes: 'Distinct from STANDARDIZES', tier: 'Core' },
  { verb: 'REJECTS', semantics: 'Formally repudiates', allowedPairs: 'P/I/M → D/T', notes: 'Needs explicit rejection evidence', tier: 'Core' },
  { verb: 'INFLUENCES', semantics: 'Non-mechanical intellectual impact', allowedPairs: 'P/I/T/D/M → P/I/T/D/M', notes: 'Prefer a more specific verb if possible', tier: 'Core' },
  { verb: 'INTERPRETS', semantics: 'Provides exegesis/theological reading', allowedPairs: 'P/T → T/D', notes: 'Commentary/exegesis broadly', tier: 'Core' },
  { verb: 'ENABLES', semantics: 'Necessary precondition (indirect)', allowedPairs: 'T/I/P/E → T/D/M/E', notes: 'Distinguish from CAUSES', tier: 'Core' },
  { verb: 'TRANSMITS', semantics: 'Conveys textual/ritual content', allowedPairs: 'T/P/I → T/D/M', notes: 'Copying/translation chains', tier: 'Core' },

  // Supplementary
  { verb: 'MEETS_WITH', semantics: 'In-person encounter', allowedPairs: 'P ↔ P', notes: 'Neutral; use COLLABORATES_WITH for joint work', tier: 'Supplementary' },
  { verb: 'BLESSES', semantics: 'Confers religious blessing', allowedPairs: 'P → P', notes: 'Distinct from ORDAINS', tier: 'Supplementary' },
  { verb: 'SERVES_IN', semantics: 'Member/official serving in institution', allowedPairs: 'P → I', notes: 'Include role/tenure', tier: 'Supplementary' },
  { verb: 'PETITIONS', semantics: 'Files formal request', allowedPairs: 'P → I', notes: '', tier: 'Supplementary' },
  { verb: 'AWARDS', semantics: 'Grants prize/decoration', allowedPairs: 'I → P', notes: 'Include award name/date', tier: 'Supplementary' },
  { verb: 'CENSURES', semantics: 'Formal reprimand without removal', allowedPairs: 'I → P', notes: 'Distinct from DISMISSES', tier: 'Supplementary' },
  { verb: 'SUMMONS', semantics: 'Orders person to appear', allowedPairs: 'I → P', notes: 'Provide writ/citation', tier: 'Supplementary' },
  { verb: 'ANNOTATES', semantics: 'Adds notes/marginalia', allowedPairs: 'P → T', notes: 'Distinct from COMMENTATES_ON', tier: 'Supplementary' },
  { verb: 'REDACTS', semantics: 'Shapes/restructures content', allowedPairs: 'P/I → T', notes: 'Use EDITS for edition work', tier: 'Supplementary' },
  { verb: 'CENSORS', semantics: 'Removes/modifies content under authority', allowedPairs: 'I → T', notes: 'Distinct from BANS', tier: 'Supplementary' },
  { verb: 'BANS', semantics: 'Prohibits circulation/possession', allowedPairs: 'I → T/D/M/P', notes: 'Provide decree reference', tier: 'Supplementary' },
  { verb: 'CITES', semantics: 'References another text', allowedPairs: 'T → T', notes: 'Distinct from QUOTES', tier: 'Supplementary' },
  { verb: 'ADAPTS', semantics: 'Transforms text for new context', allowedPairs: 'T → T', notes: '', tier: 'Supplementary' },
  { verb: 'RECRUITS', semantics: 'Enlists person into movement', allowedPairs: 'M → P', notes: '', tier: 'Supplementary' },
  { verb: 'EXPELS', semantics: 'Removes person from movement', allowedPairs: 'M → P', notes: '', tier: 'Supplementary' },
  { verb: 'INCITES', semantics: 'Agitates to spark event', allowedPairs: 'M → E', notes: 'Use CAUSES for direct causation', tier: 'Supplementary' },
  { verb: 'WITNESSES', semantics: 'Observes/records an event', allowedPairs: 'P → E', notes: 'Provide evidence source', tier: 'Supplementary' },
  { verb: 'PARTNERS_WITH', semantics: 'Institutional partnership', allowedPairs: 'I ↔ I', notes: 'Reciprocal optional', tier: 'Supplementary' },
  { verb: 'COMPETES_WITH', semantics: 'Institutional competition', allowedPairs: 'I ↔ I/M', notes: '', tier: 'Supplementary' },
  { verb: 'PRESIDES_OVER', semantics: 'Chairs or formally oversees', allowedPairs: 'I → E/P', notes: 'Councils, courts', tier: 'Supplementary' },
  { verb: 'REGULATES', semantics: 'Regulatory oversight', allowedPairs: 'I → I/M/P/T', notes: '', tier: 'Supplementary' },
  { verb: 'ORDERS', semantics: 'Issues binding instruction', allowedPairs: 'I → P/E', notes: 'Distinct from DECLARES', tier: 'Supplementary' },
  { verb: 'TEACHES', semantics: 'Instructs person or school of thought', allowedPairs: 'P → P/I', notes: 'Pedagogical relationship', tier: 'Supplementary' },
  { verb: 'LEADS', semantics: 'Commands or directs', allowedPairs: 'P → I/E/M', notes: 'Include role/period', tier: 'Supplementary' },
  { verb: 'COLLABORATES_WITH', semantics: 'Joint work or shared enterprise', allowedPairs: 'P ↔ P', notes: 'More specific than MEETS_WITH', tier: 'Supplementary' },
  { verb: 'PARENT_OF', semantics: 'Biological or adoptive parentage', allowedPairs: 'P → P', notes: 'Genealogical edge', tier: 'Supplementary' },
  { verb: 'APPOINTS', semantics: 'Places person in office', allowedPairs: 'P/I → P', notes: '', tier: 'Supplementary' },
  { verb: 'DOCUMENTS', semantics: 'Evidence records a corpus or claim', allowedPairs: 'C/V ↔ C/V', notes: '', tier: 'Corpus' },

  // Expanded Division verbs (v0.3 — Class 3 Institutions & Class 4 Places)
  { verb: 'GOVERNS', semantics: 'Exercises sovereign or administrative authority', allowedPairs: 'I/P → L/I', notes: 'Prefer over INFLUENCES for political control', tier: 'Supplementary' },
  { verb: 'LEGISLATES', semantics: 'Enacts law, statute, or regulation', allowedPairs: 'I → D/T', notes: 'For parliaments/legislatures (311)', tier: 'Supplementary' },
  { verb: 'ADMINISTERS', semantics: 'Manages or oversees operations', allowedPairs: 'I → L/I', notes: 'For colonial (314), regulatory (323); distinct from GOVERNS', tier: 'Supplementary' },
  { verb: 'ADJUDICATES', semantics: 'Renders judicial decision', allowedPairs: 'I → E/P', notes: 'For courts/tribunals (321)', tier: 'Supplementary' },
  { verb: 'FUNDS', semantics: 'Provides financial resources', allowedPairs: 'I/P → I/E/T', notes: 'For development banks (334), central banks (331)', tier: 'Supplementary' },
  { verb: 'TRAINS', semantics: 'Provides formal training/education', allowedPairs: 'I → P', notes: 'For educational (380–384), military (390); distinct from TEACHES', tier: 'Supplementary' },
  { verb: 'COMMANDS', semantics: 'Military command authority', allowedPairs: 'P/I → I/P', notes: 'For military organizations (390–394)', tier: 'Supplementary' },
  { verb: 'PATROLS', semantics: 'Exercises surveillance/security over area', allowedPairs: 'I → L', notes: 'For navies (392), intelligence agencies (393)', tier: 'Supplementary' },
  { verb: 'CURATES', semantics: 'Selects, organizes, and presents artifacts', allowedPairs: 'I/P → T', notes: 'For museums (361), libraries (362)', tier: 'Supplementary' },
  { verb: 'EXHIBITS', semantics: 'Publicly displays artifacts/artworks', allowedPairs: 'I → T', notes: 'For museums & galleries (361)', tier: 'Supplementary' },
  { verb: 'BROADCASTS', semantics: 'Transmits media content', allowedPairs: 'I → T/E', notes: 'For media & publishing (364)', tier: 'Supplementary' },
  { verb: 'ENROLLS', semantics: 'Registers a person as student/member', allowedPairs: 'I → P', notes: 'For universities (381), schools (382)', tier: 'Supplementary' },
  { verb: 'WORSHIPS_AT', semantics: 'Regular religious practice at a site', allowedPairs: 'P → I/L', notes: 'For religious institutions (340–345)', tier: 'Supplementary' },
  { verb: 'ALLIES_WITH', semantics: 'Forms military or political alliance', allowedPairs: 'I ↔ I', notes: 'For military alliances (394), regional blocs (372)', tier: 'Supplementary' },
  { verb: 'TRADES_WITH', semantics: 'Engages in commercial exchange', allowedPairs: 'I ↔ I/L', notes: 'For economic institutions (330–334)', tier: 'Supplementary' },
  { verb: 'OCCUPIES', semantics: 'Military or administrative occupation', allowedPairs: 'I → L', notes: 'Contested control; distinct from GOVERNS', tier: 'Supplementary' },
  { verb: 'CONTAINS', semantics: 'Geographic or structural containment', allowedPairs: 'L → L/I / C → T/C', notes: 'Continents→regions→countries→cities', tier: 'Core' },
  { verb: 'BORDERS', semantics: 'Geographic adjacency', allowedPairs: 'L ↔ L', notes: 'Reciprocal; countries, regions', tier: 'Supplementary' },
  { verb: 'SITUATED_IN', semantics: 'Entity located within a place', allowedPairs: 'I/E → L', notes: 'Prefer OCCURS_IN for events', tier: 'Supplementary' },
  { verb: 'CAPITAL_OF', semantics: 'Serves as administrative capital', allowedPairs: 'L → L/I', notes: 'Include period if historical', tier: 'Supplementary' },
  { verb: 'SACRED_TO', semantics: 'Place holds sacred significance', allowedPairs: 'L → D/M', notes: 'For holy cities (443), pilgrimage sites', tier: 'Supplementary' },
  { verb: 'CONTROLS', semantics: 'Exercises control over territory', allowedPairs: 'I/P → L', notes: 'For empires (450), polities; include period', tier: 'Supplementary' },
]

/* ═══════════════════════════════════════════════════════════════
   Node Type Descriptions
   ═══════════════════════════════════════════════════════════════ */

interface NodeTypeEntry {
  label: string
  icon: React.ReactNode
  color: string
  abbrev: string
  description: string
}

const NODE_TYPES: NodeTypeEntry[] = [
  { label: 'Person', icon: <Users size={16} />, color: '#3A7D44', abbrev: 'P', description: 'Individual historical or cultural figure. Includes rulers, thinkers, prophets, and artists.' },
  { label: 'Idea', icon: <Zap size={16} />, color: '#D4AF37', abbrev: 'D', description: 'Abstract concept, doctrine, or intellectual tradition. Includes philosophical systems and theological doctrines.' },
  { label: 'Institution', icon: <Landmark size={16} />, color: '#8B3A3A', abbrev: 'I', description: 'Organization, school, governing body, religious order, or formal social structure.' },
  { label: 'Place', icon: <MapPin size={16} />, color: '#3B6BC2', abbrev: 'L', description: 'Geographic location — city, region, sacred site, country, or archaeological site.' },
  { label: 'EventWindow', icon: <Clock size={16} />, color: '#C5963A', abbrev: 'E', description: 'Historical occurrence or temporally bounded window. Wars, treaties, discoveries, crises.' },
  { label: 'Movement', icon: <Layers size={16} />, color: '#6B3FA0', abbrev: 'M', description: 'Social, political, religious, or intellectual movement spanning time and geography.' },
  { label: 'Text', icon: <FileText size={16} />, color: '#5A2222', abbrev: 'T', description: 'Written work, artifact, or textual tradition. Includes books, scrolls, codices, and inscriptions.' },
  { label: 'Evidence', icon: <Shield size={16} />, color: '#787469', abbrev: 'V', description: 'Primary source, archaeological find, manuscript, or citation node used for auditability.' },
  { label: 'Corpus', icon: <BookOpen size={16} />, color: '#4A6741', abbrev: 'C', description: 'Canonical grouping of texts, traditions, or cultural artifacts (e.g., Biblical Corpus, Vedic Corpus).' },
  { label: 'Framework', icon: <Network size={16} />, color: '#2A5AA0', abbrev: 'F', description: 'Interpretive lens or analytical schema (e.g., DOCTRINE_DEVELOPMENT, CULTURAL_DIFFUSION).' },
]

/* ═══════════════════════════════════════════════════════════════
   Evidence Tiers
   ═══════════════════════════════════════════════════════════════ */

const EVIDENCE_TIERS = [
  { tier: 'A', name: 'Primary', description: 'Direct texts or sources (Bible, Vedas, Avesta, inscriptions, autographs).' },
  { tier: 'B', name: 'Peer-Reviewed', description: 'Modern academic studies in peer-reviewed journals.' },
  { tier: 'C', name: 'Scholarly', description: 'Books from academic publishers (Oxford UP, Cambridge UP, Brill).' },
  { tier: 'D', name: 'Institutional', description: 'Reports from organizations (UNESCO, IMF, World Bank).' },
  { tier: 'E', name: 'Archaeological', description: 'Excavation records, stratigraphic evidence, inscriptions, material culture.' },
  { tier: 'F', name: 'Oral / Quantitative', description: 'Documented oral histories, statistical data series.' },
]

/* ═══════════════════════════════════════════════════════════════
   Framework Matrix (from docs/guidelines/framework_matrix.md)
   ═══════════════════════════════════════════════════════════════ */

const FRAMEWORK_ENTRIES = [
  { name: 'CAUSE_AND_EFFECT', description: 'Lens that foregrounds causal chains, technological or institutional drivers, and immediate impacts; used when asserting a mechanism or causal pathway.', verbs: ['CAUSES', 'ENABLES', 'TRIGGERS', 'TRANSFORMS'], related: ['CULTURAL_DIFFUSION', 'ADAPTATION', 'CONFLICT_AND_RESOLUTION'], color: '#C53030' },
  { name: 'CULTURAL_DIFFUSION', description: 'Focuses on transmission, borrowing, and the spread of practices or ideas across regions and groups; emphasizes routes and agents of transmission.', verbs: ['DIFFUSES', 'INTRODUCES', 'ADAPTS', 'ADOPTS'], related: ['CAUSE_AND_EFFECT', 'TEXTUAL_TRANSMISSION', 'ADAPTATION'], color: '#38A169' },
  { name: 'DOCTRINE_DEVELOPMENT', description: 'Emphasizes processes of formalization, systematization, and canonical consolidation within religious or intellectual traditions.', verbs: ['CANONIZES', 'SYSTEMATIZES', 'STANDARDIZES', 'INTERPRETS'], related: ['TEXTUAL_TRANSMISSION', 'LEGAL_INTERPRETATION'], color: '#D4AF37' },
  { name: 'TEXTUAL_TRANSMISSION', description: 'Tracks the copying, translation, editorial history, and preservation of texts and textual families.', verbs: ['TRANSMITS', 'TRANSLATES', 'PRESERVES', 'EDITS'], related: ['DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'], color: '#5A2222' },
  { name: 'LEGAL_INTERPRETATION', description: 'Applies to jurisprudential, canonical, or administrative rulings and their implementation or reform.', verbs: ['INTERPRETS', 'CODIFIES', 'REFORMS', 'REJECTS'], related: ['DOCTRINE_DEVELOPMENT', 'RITUAL_STANDARDIZATION'], color: '#3B6BC2' },
  { name: 'RITUAL_STANDARDIZATION', description: 'Focuses on the formalization and institutional adoption of ritual practice across communities.', verbs: ['STANDARDIZES', 'INSTITUTES', 'REGULATES'], related: ['LEGAL_INTERPRETATION', 'DOCTRINE_DEVELOPMENT'], color: '#805AD5' },
  { name: 'GEOPOLITICAL_LINKAGE', description: 'Centers on imperial, diplomatic, and territorial relationships that reorganize institutions, mobility, or authority.', verbs: ['LINKS', 'CONNECTS', 'RECONFIGURES'], related: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION'], color: '#4A90D9' },
  { name: 'CONFLICT_AND_RESOLUTION', description: 'Captures schisms, wars, negotiations, reconciliations and the social/political effects of conflict.', verbs: ['CAUSES', 'RESOLVES', 'RADICALIZES', 'RECONCILES_WITH'], related: ['GEOPOLITICAL_LINKAGE', 'ADAPTATION'], color: '#8B3A3A' },
  { name: 'ADAPTATION', description: 'Emphasizes contextual reinterpretation, transformation, and local reworking of imported practices or ideas.', verbs: ['ADAPTS', 'TRANSFORMS', 'REINTERPRETS'], related: ['CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT'], color: '#C5963A' },
  { name: 'TEMPORAL_LINKAGE', description: 'Used for ordering and periodization claims that connect events, reforms, or transitions across time.', verbs: ['PRECEDES', 'FOLLOWS', 'IS_ANTECEDENT_TO'], related: ['CAUSE_AND_EFFECT', 'CONFLICT_AND_RESOLUTION'], color: '#6B3FA0' },
  { name: 'ECONOMIC_SYSTEMS', description: 'Analyzes modes of production, trade networks, fiscal policy, monetary systems, and the material basis of civilizations.', verbs: ['TRADES_WITH', 'PRODUCES', 'FINANCES', 'DISTRIBUTES'], related: ['CAUSE_AND_EFFECT', 'POLITICAL_SYSTEMS', 'INNOVATION_AND_TECHNOLOGY'], color: '#2F855A' },
  { name: 'POLITICAL_SYSTEMS', description: 'Examines structures of governance, sovereignty, statecraft, constitutionalism, and the evolution of political authority.', verbs: ['GOVERNS', 'LEGISLATES', 'ADMINISTERS', 'DELEGATES'], related: ['LEGAL_INTERPRETATION', 'CONFLICT_AND_RESOLUTION', 'ECONOMIC_SYSTEMS'], color: '#2B6CB0' },
  { name: 'COMPARATIVE_RELIGION', description: 'Compares doctrines, practices, institutions, and histories across religious traditions to reveal shared patterns and distinct trajectories.', verbs: ['COMPARES', 'SYNCRETIZES', 'DIFFERENTIATES', 'CONVERTS'], related: ['DOCTRINE_DEVELOPMENT', 'RITUAL_STANDARDIZATION', 'CULTURAL_DIFFUSION'], color: '#9B2C2C' },
  { name: 'EMPIRE_AND_COLONIALISM', description: 'Focuses on imperial expansion, colonial administration, resistance movements, decolonization, and postcolonial legacies.', verbs: ['COLONIZES', 'ADMINISTERS', 'RESISTS', 'DECOLONIZES'], related: ['GEOPOLITICAL_LINKAGE', 'CONFLICT_AND_RESOLUTION', 'ECONOMIC_SYSTEMS'], color: '#744210' },
  { name: 'ENVIRONMENTAL_HISTORY', description: 'Examines the interaction between human societies and the natural environment: climate, ecology, resource use, and environmental change.', verbs: ['EXPLOITS', 'CONSERVES', 'DEPLETES', 'ADAPTS_TO'], related: ['ADAPTATION', 'ECONOMIC_SYSTEMS', 'INNOVATION_AND_TECHNOLOGY'], color: '#276749' },
  { name: 'INNOVATION_AND_TECHNOLOGY', description: 'Tracks invention, diffusion, and impact of technologies, engineering achievements, and scientific breakthroughs on societies.', verbs: ['INVENTS', 'INNOVATES', 'DISRUPTS', 'MECHANIZES'], related: ['CAUSE_AND_EFFECT', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], color: '#4A5568' },
]

/* ═══════════════════════════════════════════════════════════════
   Classification System (from docs/guidelines/classification.md)
   ═══════════════════════════════════════════════════════════════ */

const CLASSIFICATION_ENTRIES = [
  { classNum: '0', name: 'Ideas (Core)', heading: 'Political, Ethical, Legal', color: '#D4AF37', divisions: ['010 Political Systems & Governance', '020 Ethical Systems', '030 Legal Systems & Law'] },
  { classNum: '1', name: 'Ideas (Other)', heading: 'Economic, Scientific, Technological, Religious, Cultural', color: '#C5963A', divisions: ['110 Economic Theories', '120 Scientific Paradigms', '130 Technological Innovations', '140 Religious & Philosophical Concepts', '150 Social & Cultural Theories', '160 Environmental Ideas', '170 Artistic Movements'] },
  { classNum: '2', name: 'People', heading: 'Historical figures across all domains', color: '#3A7D44', divisions: ['210 Philosophers', '220 Political Leaders', '230 Legal Figures', '240 Scientists & Inventors', '250 Religious Figures', '260 Artists & Writers', '270 Activists & Reformers', '280 Military Leaders & Commanders', '290 Explorers & Navigators'] },
  { classNum: '3', name: 'Institutions', heading: 'Organizations, councils, governing bodies', color: '#8B3A3A', divisions: ['310 Political Institutions', '320 Legal Institutions', '330 Economic Institutions', '340 Religious Institutions', '350 Scientific Institutions', '360 Cultural Institutions', '370 International Organizations', '380 Educational Institutions', '390 Military & Defense Organizations'] },
  { classNum: '4', name: 'Places', heading: 'Geographic locations at all scales', color: '#3B6BC2', divisions: ['410 Continents', '420 Regions', '430 Countries / Polities', '440 Cities', '450 Empires / Dynasties', '460 Civilizations', '470 Culture Areas & Trade Routes'] },
  { classNum: '5', name: 'Events', heading: 'Historical occurrences & event windows', color: '#C53030', divisions: ['510 Wars & Conflicts', '520 Revolutions & Uprisings', '530 Elections & Political Shifts', '540 Legal Cases', '550 Scientific Discoveries', '560 Technological Breakthroughs', '570 Religious Events', '580 Environmental Events', '590 Agricultural & Economic Events'] },
  { classNum: '6', name: 'Movements', heading: 'Social, political, religious movements', color: '#6B3FA0', divisions: ['610 Political Movements', '620 Social Movements', '630 Religious Movements', '640 Cultural Movements', '650 Scientific Movements', '660 Technological Movements', '670 Environmental Movements', '680 Trade & Navigation Movements'] },
  { classNum: '7', name: 'Texts & Artifacts', heading: 'Written works, codices, constitutions', color: '#5A2222', divisions: ['710 Constitutions & Charters', '720 Legal Codes', '730 Religious Texts', '740 Philosophical Works', '750 Scientific Texts', '760 Artworks', '770 Technological Artifacts', '780 Historical & Literary Texts'] },
  { classNum: '8', name: 'Evidence', heading: 'Primary sources, archaeological finds', color: '#787469', divisions: ['810 Primary Sources', '820 Secondary Sources', '830 Archaeological Evidence', '840 Quantitative Data', '850 Oral Histories'] },
  { classNum: '9', name: 'Timeframes', heading: 'Periods, eras, epochs', color: '#4A90D9', divisions: ['910 Prehistoric', '920 Classical/Ancient', '930 Medieval', '940 Early Modern', '950 Modern', '960 Contemporary'] },
]

/* ═══════════════════════════════════════════════════════════════
   Event Kinds (from docs/schema/event-kinds.md)
   ═══════════════════════════════════════════════════════════════ */

const EVENT_KIND_ENTRIES = [
  { kind: 'Battle', description: 'Armed military engagement', examples: 'Battle of White Mountain 1620, Kappel Wars' },
  { kind: 'Council', description: 'Ecclesiastical or political assembly/synod', examples: 'Council of Trent, Council of Constance, Synod of Dordt' },
  { kind: 'Controversy', description: 'Theological or political dispute/debate', examples: 'Arminius Controversy, Vestiarian Controversy' },
  { kind: 'Covenant', description: 'Divine/legal covenant or treaty', examples: 'Abrahamic Covenant, Sinai Covenant' },
  { kind: 'Debate', description: 'Formal theological disputation', examples: 'Leipzig Debate 1519, Marburg Colloquy 1529' },
  { kind: 'Decree', description: 'Official proclamation, edict, or law', examples: 'Edict of Milan 313, Edict of Nantes 1598' },
  { kind: 'Execution', description: 'State-sanctioned killing of an individual', examples: 'Execution of Anne Boleyn, Hus Execution 1415' },
  { kind: 'Exile', description: 'Forced displacement of a population', examples: 'Babylonian Exile, Expulsion from Spain 1492' },
  { kind: 'Founding', description: 'Establishment of an institution', examples: 'Founding of Society of Jesus 1540, Unitas Fratrum 1457' },
  { kind: 'Legislative', description: 'Parliamentary passage of laws', examples: 'Act of Supremacy 1534, Golden Act 1592' },
  { kind: 'Marriage', description: 'Union of two persons', examples: 'Henry VIII & Anne Boleyn, Mary I & Philip II' },
  { kind: 'Martyrdom', description: 'Death for religious beliefs', examples: 'Oxford Martyrs 1555, Ignatian Martyrdom' },
  { kind: 'Migration', description: 'Mass movement of peoples', examples: 'Hutterite Migrations, Mennonite Organizing' },
  { kind: 'Mission', description: 'Evangelistic or diplomatic mission', examples: 'Jesuit Mission 1580s, Pauline Mission Journeys' },
  { kind: 'Persecution', description: 'Systematic oppression of a group', examples: 'Decian Persecution 250, Diocletianic Persecution' },
  { kind: 'Plot', description: 'Conspiracy or failed coup', examples: 'Babington Plot 1586, Ridolfi Plot 1571' },
  { kind: 'Publication', description: 'Major text publication or translation', examples: 'Kralice Bible 1579, Wartburg Translation 1521' },
  { kind: 'Rebellion', description: 'Armed uprising against authority', examples: 'Pilgrimage of Grace 1536, Munster Rebellion' },
  { kind: 'Reform', description: 'Religious or institutional reform program', examples: 'Basel Reform 1529, Hezekiah Reforms, Josiah Reforms' },
  { kind: 'Reign', description: 'Period of rule or regency', examples: 'Lady Jane Grey Reign 1553' },
  { kind: 'Rite', description: 'Religious ceremony or ritual practice', examples: 'Temple Rituals, First Adult Baptisms Zurich 1525' },
  { kind: 'Sacred', description: 'Miraculous/divine event in religious narrative', examples: 'Exodus, Crucifixion, Pentecost, Binding of Isaac' },
  { kind: 'Siege', description: 'Military encirclement of a place', examples: 'Assyrian Siege of Jerusalem, Babylonian Siege 597 BCE' },
  { kind: 'Trial', description: 'Legal proceeding against an individual', examples: 'Trial of Mary Queen of Scots, Eichmann Trial 1961' },
  { kind: 'War', description: 'Extended military conflict', examples: 'Hussite Wars, Schmalkaldic War, Counts War' },
]

/* ═══════════════════════════════════════════════════════════════
   Curator Workflow Stages (from docs/guidelines/curator_runbook.md)
   ═══════════════════════════════════════════════════════════════ */

const WORKFLOW_STAGES = [
  { stage: 'Propose', description: 'Create node draft with status: "PROPOSED" and a brief editor_note explaining the addition.', checklist: 'Set status to PROPOSED, add editor_note, assign call number', color: '#4A90D9' },
  { stage: 'Cite', description: 'Attach at least one Evidence node (A-tier preferred) or inline citation on the relationship.', checklist: 'Attach Evidence node, verify A-tier source if possible, add Chicago 17 citation', color: '#3A7D44' },
  { stage: 'Frame', description: 'Add FRAMED_BY edge to a Framework node with citation_style, evidence_url, page_refs, source_note.', checklist: 'Link to Framework, populate all FRAMED_BY properties', color: '#D4AF37' },
  { stage: 'Place', description: 'Assign Timeframe and anchor to Place nodes with active spatial verbs (HAPPENS_IN, OCCURS_IN).', checklist: 'Set startYear/endYear, link to Place node, verify temporal sanity', color: '#C5963A' },
  { stage: 'Review', description: 'Run audit_queries.md checks: missing FRAMED_BY, temporal sanity, orphan nodes, passive verbs.', checklist: 'Run all QA queries, fix violations, verify no orphans', color: '#805AD5' },
  { stage: 'Publish', description: 'Set status to "REVIEWED" and add provenance (actor, timestamp, change_reason).', checklist: 'Update status, create Provenance node, link with HAS_PROVENANCE', color: '#8B3A3A' },
]

/* ═══════════════════════════════════════════════════════════════
   Comprehensive Project Glossary (from docs/guidelines/glossary.md
   + docs/guidelines/schema.md + docs/guidelines/classification.md
   + docs/nodes/ + docs/governance/)
   ═══════════════════════════════════════════════════════════════ */

interface GlossaryEntry { term: string; definition: string; category: string }

const GLOSSARY_ENTRIES: GlossaryEntry[] = [
  // Node Types
  { term: 'Node', category: 'Node Types', definition: 'A graph entity representing a person, place, event, idea, institution, artifact, evidence, corpus, or framework.' },
  { term: 'Person', category: 'Node Types', definition: 'Individual historical or cultural figure. Includes rulers, thinkers, prophets, artists, and activists.' },
  { term: 'Place', category: 'Node Types', definition: 'Geographic location — city, region, sacred site, country, empire, or archaeological site. Uses stable physical identity.' },
  { term: 'EventWindow', category: 'Node Types', definition: 'Historical occurrence or temporally bounded window. Wars, treaties, discoveries, crises. Must have startYear/endYear and a kind property.' },
  { term: 'Idea', category: 'Node Types', definition: 'Abstract concept, doctrine, or intellectual tradition. The generative core of the classification system — ideas drive everything.' },
  { term: 'Institution', category: 'Node Types', definition: 'Organization, school, governing body, religious order, or formal social structure.' },
  { term: 'Movement', category: 'Node Types', definition: 'Social, political, religious, or intellectual movement spanning time and geography.' },
  { term: 'Text', category: 'Node Types', definition: 'Written work, artifact, or textual tradition. Books, scrolls, codices, inscriptions, and constitutions.' },
  { term: 'Evidence', category: 'Node Types', definition: 'Primary source, archaeological find, manuscript, or citation node used for scholarly auditability.' },
  { term: 'Corpus', category: 'Node Types', definition: 'Canonical grouping of texts, traditions, or cultural artifacts (e.g., Biblical Corpus, Vedic Corpus). Top-level class 10.' },
  { term: 'Framework', category: 'Node Types', definition: 'Interpretive lens or analytical schema (e.g., DOCTRINE_DEVELOPMENT, CULTURAL_DIFFUSION). First-class nodes since v4.' },
  { term: 'Timeframe', category: 'Node Types', definition: 'Period, era, or epoch used for temporal anchoring. Division 9 in classification (910–960).' },
  { term: 'Polity', category: 'Node Types', definition: 'Political entity with territorial sovereignty — kingdom, empire, republic, city-state.' },

  // Relationships & Properties
  { term: 'Relationship (Edge)', category: 'Relationships', definition: 'Connection between two nodes defined by an active-voice verb. Every edge has a verb, source, and target.' },
  { term: 'Active-Voice Relationship', category: 'Relationships', definition: 'Edge verb with subject → object directionality (e.g., Person AUTHORS Text, not Text IS_AUTHORED_BY Person).' },
  { term: 'FRAMED_BY', category: 'Relationships', definition: 'Interpretive edge linking any node to a Framework. Must include citation_style, evidence_url, page_refs, source_note.' },
  { term: 'OCCURS_IN', category: 'Relationships', definition: 'Spatial anchor — links Event to Place. Single primary place per edge.' },
  { term: 'OCCURS_DURING', category: 'Relationships', definition: 'Temporal anchor — links Event to Timeframe/Era/Epoch.' },
  { term: 'PREVIOUSLY_KNOWN_AS', category: 'Relationships', definition: 'Links Place to time-scoped PlaceName nodes for historical, endonym, and exonym variants.' },

  // Classification
  { term: 'Call Number', category: 'Classification', definition: 'Dewey-style numeric code: Class.Division-Slug (e.g., 220.06-julius-caesar). 10 classes (0–9), 81 divisions.' },
  { term: 'Slug', category: 'Classification', definition: 'Lowercase-snake_case canonical identifier, unique per label. Primary lookup key in catalog and graph.' },
  { term: 'Subject Heading', category: 'Classification', definition: 'Topical label for classification within a call number class.' },
  { term: 'Division', category: 'Classification', definition: 'Second-level subdivision within a class (e.g., 210 = Philosophers, 510 = Wars).' },
  { term: 'Class', category: 'Classification', definition: 'Top-level category (0–9): Ideas, Theories, People, Institutions, Places, Events, Movements, Texts, Evidence, Timeframes.' },

  // Data & Schema
  { term: 'Generic Node', category: 'Schema', definition: 'Atemporal, non-contextual hub (e.g., Rome as a Place, Democracy as an Idea). Never changes.' },
  { term: 'Contextual Node', category: 'Schema', definition: 'Instance with time/place specificity (e.g., Roman Empire 27 BCE–476 CE as an Institution).' },
  { term: 'Provenance', category: 'Schema', definition: 'Metadata recording source, creator, modification history. Links via HAS_PROVENANCE to Provenance nodes.' },
  { term: 'Tier', category: 'Schema', definition: 'Evidence reliability level (A–F): Primary, Peer-Reviewed, Scholarly, Institutional, Archaeological, Oral/Quantitative.' },
  { term: 'chron_key', category: 'Schema', definition: 'Numeric key for deterministic chronological ordering. Negative integers for BCE years.' },

  // Project Structure
  { term: 'Cluster', category: 'Project Structure', definition: 'Thematic or civilizational grouping of nodes (e.g., English Reformation, Hebrew Tradition, Early Christianity).' },
  { term: 'Zone', category: 'Project Structure', definition: 'Civilizational area (Ancient Near East, East Asia, Americas, etc.) used for organizing clusters geographically.' },
  { term: 'Corpus Registry', category: 'Project Structure', definition: 'Canonical list of recognized corpus nodes. 14 corpus files in ui/src/data/catalog/corpuses/.' },
  { term: 'Cluster Registry', category: 'Project Structure', definition: 'Master list of all clusters with status (active/planned) and coverage metrics. See docs/registry/.' },
  { term: 'Geo-Registry', category: 'Project Structure', definition: '199 country profiles in geo-registry/places/countries/ with demographic, economic, and governance data.' },

  // Workflow
  { term: 'Curator', category: 'Workflow', definition: 'Senior contributor responsible for governance, audits, normalization, and publishing nodes to REVIEWED status.' },
  { term: 'Contributor', category: 'Workflow', definition: 'Project participant who seeds, curates, or expands nodes and relationships.' },
  { term: 'Historian', category: 'Workflow', definition: 'Contributor focused on historical accuracy, contextual node descriptions, and evidence sourcing.' },
  { term: 'Workflow Stage', category: 'Workflow', definition: 'One of 6 stages: Propose → Cite → Frame → Place → Review → Publish.' },
  { term: 'PROPOSED', category: 'Workflow', definition: 'Initial node status — draft awaiting evidence and framework links.' },
  { term: 'REVIEWED', category: 'Workflow', definition: 'Published status — node has passed all QA checks and has provenance.' },
  { term: 'Audit Query', category: 'Workflow', definition: 'Cypher query that validates graph integrity: missing FRAMED_BY, temporal sanity, orphans, passive verbs, duplicates.' },

  // Technology
  { term: 'Cypher', category: 'Technology', definition: 'Neo4j query language for creating, reading, updating, and deleting graph data.' },
  { term: 'APOC', category: 'Technology', definition: 'Awesome Procedures on Cypher — Neo4j plugin for triggers, periodic commits, and utility functions.' },
  { term: 'MERGE', category: 'Technology', definition: 'Cypher command that creates a node/edge only if it does not already exist. Prevents duplicates.' },
  { term: 'Chakra UI', category: 'Technology', definition: 'React component library (v3) used for the Papyrus & Cosmos design system.' },
  { term: 'D3.js', category: 'Technology', definition: 'JavaScript library for force-directed graph visualization in GraphExplorer.' },
  { term: 'Pydantic', category: 'Technology', definition: 'Python data validation library. All backend models use Pydantic BaseModel.' },

  // Standards
  { term: 'CIDOC CRM', category: 'Standards', definition: 'International standard for cultural heritage data modeling. Used as crosswalk reference for node attributes.' },
  { term: 'Chicago 17', category: 'Standards', definition: 'Chicago Manual of Style 17th edition — the required citation style for all FRAMED_BY edges.' },
  { term: 'ISO 3166', category: 'Standards', definition: 'International standard for country codes (alpha-2, alpha-3, numeric). Used in geo-registry.' },
  { term: 'UNESCO', category: 'Standards', definition: 'UN agency; used for region/style normalization and cultural heritage classification.' },
  { term: 'W3C PROV', category: 'Standards', definition: 'W3C Provenance standard. Used as crosswalk reference for provenance modeling.' },

  // Design System
  { term: 'Papyrus & Cosmos', category: 'Design System', definition: 'Project theme — papyrus tones (#FAF3E8) for backgrounds, cosmos blues (#E8F0FE) for interactive elements, gold (#D4AF37) for accents.' },
  { term: 'Cormorant Garamond', category: 'Design System', definition: 'Serif font used for section headings throughout the application.' },
  { term: 'Cinzel', category: 'Design System', definition: 'Display font used for hero titles, logos, and emphasis headings.' },
  { term: 'Inter', category: 'Design System', definition: 'Body text font used for paragraph content and UI elements.' },
  { term: 'JetBrains Mono', category: 'Design System', definition: 'Monospace font used for code, slugs, and call numbers.' },
  { term: 'StatCard', category: 'Design System', definition: 'UI component: colored accent bar + large value + label. Used in all continent dashboards.' },
  { term: 'InsightCard', category: 'Design System', definition: 'UI component: dot indicator + title + narrative insight + source attribution.' },
  { term: 'DataTable', category: 'Design System', definition: 'UI component: dark header + striped rows + scrollable. For comparative data.' },
  { term: 'SectionHeading', category: 'Design System', definition: 'UI component: serif title + muted subtitle + golden underline bar.' },

  // Eras
  { term: 'Prehistoric', category: 'Eras', definition: 'Before 3000 BCE. Division 910. Color: #6B4D1B. Earliest human activity through proto-civilization.' },
  { term: 'Classical / Ancient', category: 'Eras', definition: '3000 BCE – 500 CE. Division 920. Color: #8B4513. Great civilizations, empires, and philosophical traditions.' },
  { term: 'Medieval', category: 'Eras', definition: '500 – 1500 CE. Division 930. Color: #A67C2E. Byzantine, Islamic, and European feudal societies.' },
  { term: 'Early Modern', category: 'Eras', definition: '1500 – 1800 CE. Division 940. Color: #C5963A. Reformation, colonialism, scientific revolution.' },
  { term: 'Modern', category: 'Eras', definition: '1800 – 1945 CE. Division 950. Color: #4A90D9. Industrialization, world wars, nationalism.' },
  { term: 'Contemporary', category: 'Eras', definition: '1945 CE – Present. Division 960. Color: #6B3FA0. Cold War, globalization, digital age.' },
]

/* ═══════════════════════════════════════════════════════════════
   TIER COLOURS for verb cards
   ═══════════════════════════════════════════════════════════════ */

const TIER_COLORS: Record<string, string> = {
  Core: '#3A7D44',
  Supplementary: '#4A90D9',
  Corpus: '#6B3FA0',
}

/* ═══════════════════════════════════════════════════════════════
   COMPONENT
   ═══════════════════════════════════════════════════════════════ */

export default function DocsPage() {
  const [searchTerm, setSearchTerm] = useState('')
  const [activeSection, setActiveSection] = useState<string>('glossary')

  const filteredVerbs = useMemo(() => {
    if (!searchTerm.trim()) return VERB_GLOSSARY
    const q = searchTerm.toLowerCase()
    return VERB_GLOSSARY.filter(v =>
      v.verb.toLowerCase().includes(q)
      || v.semantics.toLowerCase().includes(q)
      || v.allowedPairs.toLowerCase().includes(q)
      || v.notes.toLowerCase().includes(q)
    )
  }, [searchTerm])

  const sections = [
    { id: 'glossary', label: 'Edge Glossary', icon: <Network size={16} /> },
    { id: 'nodetypes', label: 'Node Types', icon: <Layers size={16} /> },
    { id: 'evidence', label: 'Evidence Tiers', icon: <Shield size={16} /> },
    { id: 'conventions', label: 'Conventions', icon: <FileText size={16} /> },
    { id: 'frameworks', label: 'Frameworks', icon: <Layers size={16} /> },
    { id: 'classification', label: 'Classification', icon: <BookOpen size={16} /> },
    { id: 'eventkinds', label: 'Event Kinds', icon: <Clock size={16} /> },
    { id: 'workflow', label: 'Curator Workflow', icon: <Users size={16} /> },
    { id: 'projectglossary', label: 'Project Glossary', icon: <Search size={16} /> },
  ]

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Documentation' }]} />

      {/* Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <BookOpen size={28} color="#8B3A3A" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color={DARK_TEXT}>
            Documentation
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color={MED_TEXT} maxW="760px">
          Reference documentation for the Annals of the World knowledge graph —
          relationship verbs, node types, evidence tiers, and project conventions.
        </Text>
        <Box h="3px" bg="#8B3A3A" w="80px" mt={4} />
      </Box>

      {/* Section Tabs */}
      <Flex gap={2} mb={6} flexWrap="wrap">
        {sections.map(s => (
          <Box
            key={s.id}
            as="button"
            onClick={() => setActiveSection(s.id)}
            px={4} py={2}
            borderRadius="lg"
            fontSize="sm"
            fontWeight={600}
            bg={activeSection === s.id ? DARK_TEXT : 'white'}
            color={activeSection === s.id ? 'white' : MED_TEXT}
            border="1px solid"
            borderColor={activeSection === s.id ? DARK_TEXT : BORDER}
            cursor="pointer"
            display="flex"
            alignItems="center"
            gap={2}
            transition="all 0.15s"
            _hover={{ borderColor: GOLD }}
          >
            {s.icon}
            {s.label}
          </Box>
        ))}
      </Flex>

      {/* ═══════ EDGE GLOSSARY ═══════ */}
      {activeSection === 'glossary' && (
        <Box>
          <SectionHeading
            title="Relationship Verb Glossary"
            subtitle="Canonical active-voice edge verbs — the single source of truth for all relationship types"
          />

          {/* Search */}
          <Flex mb={6} maxW="480px" position="relative">
            <Box position="absolute" left="12px" top="50%" transform="translateY(-50%)" color={MUTED} zIndex={1}>
              <Search size={16} />
            </Box>
            <input
              style={{
                width: '100%',
                padding: '10px 12px 10px 36px',
                fontSize: '14px',
                borderRadius: '8px',
                border: `1px solid ${BORDER}`,
                background: 'white',
                outline: 'none',
                fontFamily: 'Inter, sans-serif',
              }}
              placeholder="Search verbs…"
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
            />
          </Flex>

          {/* Legend */}
          <Flex gap={4} mb={4} flexWrap="wrap">
            {(['Core', 'Supplementary', 'Corpus'] as const).map(t => (
              <Flex key={t} align="center" gap={2}>
                <Box w="10px" h="10px" borderRadius="full" bg={TIER_COLORS[t]} />
                <Text fontSize="xs" color={MUTED} fontWeight={600}>{t} ({filteredVerbs.filter(v => v.tier === t).length})</Text>
              </Flex>
            ))}
          </Flex>

          {/* Verb Cards */}
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
            {filteredVerbs.map(v => (
              <Box
                key={`${v.verb}-${v.tier}`}
                bg="white"
                border="1px solid"
                borderColor={BORDER}
                borderRadius="lg"
                p={4}
                position="relative"
                overflow="hidden"
              >
                <Box position="absolute" top={0} left={0} w="4px" h="100%" bg={TIER_COLORS[v.tier]} />
                <Flex align="center" gap={2} mb={2} pl={3}>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700} color={DARK_TEXT}>
                    {v.verb}
                  </Text>
                  <Text fontSize="xs" color={TIER_COLORS[v.tier]} fontWeight={600} ml="auto">
                    {v.tier}
                  </Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} pl={3} mb={2}>{v.semantics}</Text>
                <Flex pl={3} gap={4} flexWrap="wrap">
                  <Text fontSize="xs" color={MUTED}>
                    <Text as="span" fontWeight={600}>Pairs:</Text> {v.allowedPairs}
                  </Text>
                </Flex>
                {v.notes && (
                  <Text fontSize="xs" color={MUTED} pl={3} mt={1} fontStyle="italic">{v.notes}</Text>
                )}
              </Box>
            ))}
          </SimpleGrid>

          {filteredVerbs.length === 0 && (
            <Box textAlign="center" py={8}>
              <Text color={MUTED}>No verbs match "{searchTerm}"</Text>
            </Box>
          )}

          {/* Abbreviation Key */}
          <Box mt={8} p={4} bg={CARD_BG} borderRadius="lg" border="1px solid" borderColor={BORDER}>
            <Text fontSize="sm" fontWeight={600} color={DARK_TEXT} mb={2}>Node Type Abbreviation Key</Text>
            <Text fontSize="xs" color={MED_TEXT} lineHeight={1.8}>
              P = Person · I = Institution · T = Text/Artifact · D = Doctrine/Idea · M = Movement · E = Event · L = Place · F = Framework · V = Evidence · C = Corpus
            </Text>
          </Box>
        </Box>
      )}

      {/* ═══════ NODE TYPES ═══════ */}
      {activeSection === 'nodetypes' && (
        <Box>
          <SectionHeading
            title="Node Types"
            subtitle="The 10 core labels that make up the knowledge graph"
          />
          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
            {NODE_TYPES.map(nt => (
              <Box
                key={nt.label}
                bg="white"
                border="1px solid"
                borderColor={BORDER}
                borderRadius="lg"
                p={4}
                position="relative"
              >
                <Box position="absolute" top={0} left={0} w="4px" h="100%" bg={nt.color} borderRadius="lg 0 0 lg" />
                <Flex align="center" gap={2} mb={2} pl={3}>
                  <Box color={nt.color}>{nt.icon}</Box>
                  <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={600} color={DARK_TEXT}>
                    {nt.label}
                  </Text>
                  <Text fontSize="xs" fontFamily="mono" color={MUTED} ml="auto">
                    Abbrev: {nt.abbrev}
                  </Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} pl={3} lineHeight={1.6}>{nt.description}</Text>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ EVIDENCE TIERS ═══════ */}
      {activeSection === 'evidence' && (
        <Box>
          <SectionHeading
            title="Evidence Tiers"
            subtitle="Hierarchy of source reliability used for scholarly auditability"
          />
          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
            {EVIDENCE_TIERS.map(et => (
              <Box key={et.tier} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4}>
                <Flex align="center" gap={3} mb={2}>
                  <Box
                    w="32px" h="32px" borderRadius="full"
                    bg={GOLD} color="white"
                    display="flex" alignItems="center" justifyContent="center"
                    fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
                  >
                    {et.tier}
                  </Box>
                  <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={600} color={DARK_TEXT}>
                    {et.name}
                  </Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} lineHeight={1.6}>{et.description}</Text>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ CONVENTIONS ═══════ */}
      {activeSection === 'conventions' && (
        <Box>
          <SectionHeading
            title="Project Conventions"
            subtitle="Standards and naming conventions used across the knowledge graph"
          />

          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
            <ConventionCard
              title="Edge Labels"
              content="UPPER_SNAKE_CASE (preferred). Verbs express a single semantic action with no tense inflection. Property 'verb' must equal the relationship type label."
            />
            <ConventionCard
              title="Call Numbers"
              content="Dewey-style classification: Class.Division-Slug (e.g., 220.06-julius-caesar). 10 classes (0–9): Ideas, Theories, People, Institutions, Places, Events, Movements, Texts, Evidence, Timeframes."
            />
            <ConventionCard
              title="Slugs"
              content="Lowercase-snake_case canonical identifiers, unique per label. Used as the primary lookup key throughout the catalog and graph."
            />
            <ConventionCard
              title="Active Voice"
              content="All relationships use active voice — subject → verb → object (e.g., 'Person AUTHORS Text', not 'Text IS_AUTHORED_BY Person')."
            />
            <ConventionCard
              title="Evidence Required"
              content="All interpretive edges must include FRAMED_BY with citation_style, evidence_url, page_refs, and source_note."
            />
            <ConventionCard
              title="Era Framework"
              content="Six eras: Prehistoric (before 3000 BCE), Classical (3000 BCE – 500 CE), Medieval (500–1500), Early Modern (1500–1800), Modern (1800–1945), Contemporary (1945–present)."
            />
            <ConventionCard
              title="Chronology"
              content="Use negative integers for BCE years (e.g., -753 for 753 BCE). Use chron_key for deterministic ordering. Prefer numeric comparisons and range queries."
            />
            <ConventionCard
              title="Place Naming"
              content="Stable physical location identity (Place node never changes). Time-scoped PlaceName nodes connected via PREVIOUSLY_KNOWN_AS. Endonyms (local names), exonyms (foreign names), and historical names are all modeled."
            />
            <ConventionCard
              title="Generic vs Contextual Nodes"
              content="Generic nodes are atemporal hubs (e.g., Rome as a Place). Contextual nodes have time/place specificity (e.g., Roman Empire 27 BCE–476 CE as an Institution)."
            />
            <ConventionCard
              title="Citation Style"
              content="Chicago Manual of Style 17th edition. All FRAMED_BY edges must include citation_style, evidence_url, page_refs, and source_note properties."
            />
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ FRAMEWORKS ═══════ */}
      {activeSection === 'frameworks' && (
        <Box>
          <SectionHeading
            title="Interpretive Frameworks"
            subtitle="16 analytical lenses for examining historical relationships — from docs/guidelines/framework_matrix.md"
          />
          <SimpleGrid columns={{ base: 1 }} gap={4}>
            {FRAMEWORK_ENTRIES.map(fw => (
              <Box key={fw.name} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={5} position="relative" overflow="hidden">
                <Box position="absolute" top={0} left={0} w="4px" h="100%" bg={fw.color} />
                <Flex align="center" gap={2} mb={2} pl={3}>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700} color={DARK_TEXT}>{fw.name}</Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} pl={3} mb={3}>{fw.description}</Text>
                <Flex pl={3} gap={2} flexWrap="wrap" mb={2}>
                  <Text fontSize="xs" color={MUTED} fontWeight={600}>Recommended verbs:</Text>
                  {fw.verbs.map(v => (
                    <Text key={v} fontSize="xs" fontFamily="mono" color="#3A7D44" bg="#F0FFF4" px={2} py={0.5} borderRadius="md">{v}</Text>
                  ))}
                </Flex>
                <Flex pl={3} gap={2} flexWrap="wrap">
                  <Text fontSize="xs" color={MUTED} fontWeight={600}>Related:</Text>
                  {fw.related.map(r => (
                    <Text key={r} fontSize="xs" color={MUTED} fontStyle="italic">{r}</Text>
                  ))}
                </Flex>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ CLASSIFICATION ═══════ */}
      {activeSection === 'classification' && (
        <Box>
          <SectionHeading
            title="Call Number Classification System"
            subtitle="Dewey-inspired taxonomy — 10 classes, 48+ divisions — from docs/guidelines/classification.md"
          />
          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
            {CLASSIFICATION_ENTRIES.map(cls => (
              <Box key={cls.classNum} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4}>
                <Flex align="center" gap={2} mb={2}>
                  <Box w="32px" h="32px" borderRadius="full" bg={cls.color} color="white" display="flex" alignItems="center" justifyContent="center" fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}>
                    {cls.classNum}
                  </Box>
                  <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={600} color={DARK_TEXT}>{cls.name}</Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} mb={2}>{cls.heading}</Text>
                {cls.divisions.map(d => (
                  <Text key={d} fontSize="xs" color={MUTED} fontFamily="mono" lineHeight={1.8}>  {d}</Text>
                ))}
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ EVENT KINDS ═══════ */}
      {activeSection === 'eventkinds' && (
        <Box>
          <SectionHeading
            title="Event Kind Vocabulary"
            subtitle="Canonical 'kind' property values for EventWindow nodes — from docs/schema/event-kinds.md"
          />
          <Text fontSize="sm" color={MED_TEXT} mb={4} maxW="700px">
            Every EventWindow node must have a <code>kind</code> property. Prefer specificity (Execution over Persecution), use one kind per event, and match to established examples.
          </Text>
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
            {EVENT_KIND_ENTRIES.map(ek => (
              <Box key={ek.kind} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4}>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700} color={DARK_TEXT} mb={1}>{ek.kind}</Text>
                <Text fontSize="sm" color={MED_TEXT} mb={2}>{ek.description}</Text>
                <Text fontSize="xs" color={MUTED} fontStyle="italic">{ek.examples}</Text>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ CURATOR WORKFLOW ═══════ */}
      {activeSection === 'workflow' && (
        <Box>
          <SectionHeading
            title="Curator Workflow"
            subtitle="6-stage pipeline for adding data to the knowledge graph — from docs/guidelines/curator_runbook.md"
          />
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
            {WORKFLOW_STAGES.map((ws, i) => (
              <Box key={ws.stage} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={5} position="relative" overflow="hidden">
                <Box position="absolute" top={0} left={0} w="100%" h="4px" bg={ws.color} />
                <Flex align="center" gap={2} mb={2}>
                  <Box w="28px" h="28px" borderRadius="full" bg={ws.color} color="white" display="flex" alignItems="center" justifyContent="center" fontSize="sm" fontWeight={700}>{i + 1}</Box>
                  <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={600} color={DARK_TEXT}>{ws.stage}</Text>
                </Flex>
                <Text fontSize="sm" color={MED_TEXT} mb={2}>{ws.description}</Text>
                <Text fontSize="xs" color={MUTED} fontStyle="italic">{ws.checklist}</Text>
              </Box>
            ))}
          </SimpleGrid>

          <SectionHeading title="Escalation Rules" subtitle="When to escalate to governance board" />
          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
            <ConventionCard title="Missing Primary Evidence" content="If no primary or peer-reviewed source can be found for an interpretive claim, escalate via RFC." />
            <ConventionCard title="Major Temporal Contradictions" content="If start/end year conflicts span multiple nodes, escalate to governance board." />
            <ConventionCard title="Network Fragmentation" content="If a change would disconnect >10 nodes from the main graph, escalate for review." />
            <ConventionCard title="Competing Frameworks" content="If two frameworks yield contradictory interpretations of the same event, model both with separate FRAMED_BY edges and source notes." />
          </SimpleGrid>
        </Box>
      )}

      {/* ═══════ PROJECT GLOSSARY ═══════ */}
      {activeSection === 'projectglossary' && (
        <Box>
          <SectionHeading
            title="Project Glossary"
            subtitle="Comprehensive definitions for all project terms — migrated from docs/guidelines/glossary.md"
          />

          {/* Search */}
          <Flex mb={6} maxW="480px" position="relative">
            <Box position="absolute" left="12px" top="50%" transform="translateY(-50%)" color={MUTED} zIndex={1}>
              <Search size={16} />
            </Box>
            <input
              style={{
                width: '100%',
                padding: '10px 12px 10px 36px',
                fontSize: '14px',
                borderRadius: '8px',
                border: `1px solid ${BORDER}`,
                background: 'white',
                outline: 'none',
                fontFamily: 'Inter, sans-serif',
              }}
              placeholder="Search glossary terms…"
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
            />
          </Flex>

          {(() => {
            const q = searchTerm.toLowerCase()
            const filtered = q
              ? GLOSSARY_ENTRIES.filter(g => g.term.toLowerCase().includes(q) || g.definition.toLowerCase().includes(q) || g.category.toLowerCase().includes(q))
              : GLOSSARY_ENTRIES

            const categories = [...new Set(filtered.map(g => g.category))]

            return (
              <>
                {categories.map(cat => (
                  <Box key={cat} mb={6}>
                    <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color={GOLD} mb={3} textTransform="uppercase" letterSpacing="wider">{cat}</Text>
                    <SimpleGrid columns={{ base: 1, md: 2 }} gap={3}>
                      {filtered.filter(g => g.category === cat).map(g => (
                        <Box key={g.term} bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4}>
                          <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" fontWeight={700} color={DARK_TEXT} mb={1}>{g.term}</Text>
                          <Text fontSize="sm" color={MED_TEXT} lineHeight={1.6}>{g.definition}</Text>
                        </Box>
                      ))}
                    </SimpleGrid>
                  </Box>
                ))}
                {filtered.length === 0 && (
                  <Box textAlign="center" py={8}><Text color={MUTED}>No terms match "{searchTerm}"</Text></Box>
                )}
              </>
            )
          })()}
        </Box>
      )}
    </Box>
  )
}

function ConventionCard({ title, content }: { title: string; content: string }) {
  return (
    <Box bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4}>
      <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={600} color={DARK_TEXT} mb={2}>
        {title}
      </Text>
      <Text fontSize="sm" color={MED_TEXT} lineHeight={1.6}>{content}</Text>
    </Box>
  )
}
