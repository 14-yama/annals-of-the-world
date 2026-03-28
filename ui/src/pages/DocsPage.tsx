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
          </SimpleGrid>
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
