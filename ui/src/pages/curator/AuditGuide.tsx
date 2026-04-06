import React from 'react'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import {
  CheckCircle2,
  AlertTriangle,
  Info,
  Star,
  Layers,
  BookOpen,
  Target,
  Clock,
} from 'lucide-react'
import { SectionHeading } from '../../components/DataCards'

/* ─── Data ─── */

const QUALITY_RUBRIC = [
  { dim: 'relationships', label: 'Relationships', desc: 'At least 1 OCCURS_IN + contextual edges', icon: Layers, weight: 'Required' },
  { dim: 'causes', label: 'Causes', desc: 'At least 1 causal antecedent linking to prior events/ideas', icon: Target, weight: 'Required' },
  { dim: 'effects', label: 'Effects', desc: 'At least 1 consequent outcome showing impact', icon: Target, weight: 'Required' },
  { dim: 'frameworks', label: 'Frameworks', desc: 'At least 1 of 16 interpretive frameworks assigned', icon: BookOpen, weight: 'Required' },
  { dim: 'places', label: 'Places', desc: 'At least 1 geographic reference with role', icon: Star, weight: 'Required' },
  { dim: 'texts', label: 'Texts', desc: 'References to source texts where applicable', icon: BookOpen, weight: 'Recommended' },
  { dim: 'image', label: 'Image', desc: 'Thumbnail or hero image URL for visual identity', icon: Star, weight: 'Recommended' },
  { dim: 'wikidata', label: 'Wikidata QID', desc: 'Q-identifier for cross-referencing', icon: Info, weight: 'Recommended' },
  { dim: 'summary', label: 'Summary', desc: 'Descriptive paragraph ≥ 50 characters — not a slug or placeholder', icon: CheckCircle2, weight: 'Required' },
]

const AUDIT_SCHEDULE = [
  {
    period: 'Daily',
    tasks: [
      'Run completeness audit on 500-entity sample',
      'Review orphan queue (entities with 0 relationships)',
      'Check newly-seeded entities for quality compliance',
      'Verify subject headings match Label — Cluster — Country — Era pattern',
    ],
  },
  {
    period: 'Weekly',
    tasks: [
      'Full duplicate check across slugs and names',
      'Era/division consistency audit (no empty eraDivisionCodes)',
      'Subject heading verification across all entities',
      'Image coverage check — prioritize Person entities',
      'Wikidata QID enrichment batch for entities without QIDs',
      'Relationship density analysis — identify underconnected important entities',
    ],
  },
  {
    period: 'Monthly',
    tasks: [
      'Full population audit — all entities scored 0-9',
      'Taxonomy consistency review (callNumber classes and divisions)',
      'Cross-corpus relationship verification',
      'Data source freshness check (Wikidata updates)',
      'Entity consolidation/deduplication batch',
    ],
  },
]

const NAMING_CONVENTIONS = [
  { field: 'slug', rule: 'Lowercase, hyphen-separated, no special characters. E.g. julius-caesar, battle-of-marathon' },
  { field: 'callNumber', rule: 'Format: Class.Division.Slug. E.g. 220.06-julius-caesar' },
  { field: 'subjectHeadings', rule: 'Array of hierarchical headings: "Label — Cluster — Country — Era"' },
  { field: 'subjects', rule: 'Array of tags: [countryName, topicTag1, topicTag2]' },
  { field: 'era', rule: 'One of: Prehistoric, Classical, Medieval, Early Modern, Modern, Contemporary' },
  { field: 'eraDivisionCode', rule: '3-digit code from 910-963 mapping to specific sub-period' },
  { field: 'frameworks', rule: 'Array from 16 predefined frameworks (e.g. "Political", "Religious", "Economic")' },
  { field: 'relationships', rule: 'Active voice verbs only: CAUSES, INFLUENCES, FRAMES, OCCURS_IN, etc.' },
]

const EVIDENCE_TIERS = [
  { tier: 'A', label: 'Primary Source', desc: 'Direct historical document, inscription, artifact' },
  { tier: 'B', label: 'Secondary Scholarly', desc: 'Peer-reviewed journal article, monograph' },
  { tier: 'C', label: 'Reference Work', desc: 'Encyclopedia, handbook, authoritative reference' },
  { tier: 'D', label: 'Tertiary/Popular', desc: 'Textbook, popular history, documentary' },
  { tier: 'E', label: 'Digital/Online', desc: 'Wikipedia, Wikidata, reputable web source' },
  { tier: 'F', label: 'Oral/Quantitative', desc: 'Oral tradition, statistical dataset, AI-assisted' },
]

/* ─── Main Component ─── */

export default function AuditGuide() {
  return (
    <Box maxW="1100px" mx="auto" p={6}>
      {/* Hero */}
      <Box mb={10}>
        <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color="#2D2A24" letterSpacing="0.08em">
          AUDIT GUIDELINES
        </Text>
        <Text color="#787469" fontSize="sm" mt={1}>
          Quality rubric, naming conventions, evidence tiers, and audit schedule
        </Text>
      </Box>

      {/* Section 1: Quality Rubric */}
      <SectionHeading title="Quality Rubric" subtitle="Every entity is scored 0–9 based on these dimensions" />
      <Box mb={10}>
        {QUALITY_RUBRIC.map((item, i) => {
          const Icon = item.icon
          const required = item.weight === 'Required'
          return (
            <Flex
              key={item.dim}
              align="center"
              gap={4}
              py={3}
              px={4}
              bg={i % 2 === 0 ? '#FAFAF8' : '#F5F4F0'}
              borderRadius={i === 0 ? 'lg lg 0 0' : i === QUALITY_RUBRIC.length - 1 ? '0 0 lg lg' : undefined}
              border="1px solid #E4E2DC"
              borderTop={i > 0 ? '0' : undefined}
            >
              <Box p={1.5} borderRadius="md" bg={required ? '#FADBD820' : '#D5F5E320'}>
                <Icon size={16} color={required ? '#922B21' : '#1E8449'} />
              </Box>
              <Box flex={1}>
                <Flex align="center" gap={2}>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                    {item.label}
                  </Text>
                  <Box as="span" px={1.5} py={0.5} borderRadius="sm" fontSize="9px" fontWeight={700}
                    bg={required ? '#FADBD8' : '#D5F5E3'} color={required ? '#922B21' : '#1E8449'}
                    textTransform="uppercase" letterSpacing="0.06em">
                    {item.weight}
                  </Box>
                </Flex>
                <Text fontSize="xs" color="#787469" mt={0.5}>{item.desc}</Text>
              </Box>
            </Flex>
          )
        })}
      </Box>

      {/* Section 2: Audit Schedule */}
      <SectionHeading title="Audit Schedule" subtitle="Systematic review cadence" />
      <SimpleGrid columns={{ base: 1, md: 3 }} gap={4} mb={10}>
        {AUDIT_SCHEDULE.map((sched) => (
          <Box key={sched.period} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={5}>
            <Flex align="center" gap={2} mb={3}>
              <Clock size={16} color="#D4AF37" />
              <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color="#2D2A24">
                {sched.period}
              </Text>
            </Flex>
            {sched.tasks.map((task, i) => (
              <Flex key={i} gap={2} mb={2}>
                <Box w={2} h={2} borderRadius="full" bg="#D4AF37" mt={1.5} flexShrink={0} />
                <Text fontSize="xs" color="#524E44" lineHeight={1.5}>{task}</Text>
              </Flex>
            ))}
          </Box>
        ))}
      </SimpleGrid>

      {/* Section 3: Naming Conventions */}
      <SectionHeading title="Naming & Field Conventions" subtitle="Standards for every entity field" />
      <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="hidden" mb={10}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th style={thStyle}>Field</th>
              <th style={thStyle}>Convention</th>
            </tr>
          </thead>
          <tbody>
            {NAMING_CONVENTIONS.map((item, ri) => (
              <tr key={item.field} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                <td style={{ ...tdStyle, fontFamily: '"JetBrains Mono", monospace', fontWeight: 600, fontSize: '12px', color: '#4A90D9', whiteSpace: 'nowrap' }}>
                  {item.field}
                </td>
                <td style={tdStyle}>{item.rule}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Box>

      {/* Section 4: Evidence Tiers */}
      <SectionHeading title="Evidence Tier Hierarchy" subtitle="6-tier evidence classification for all claims" />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={3} mb={10}>
        {EVIDENCE_TIERS.map((tier) => (
          <Box key={tier.tier} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={4}>
            <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#D4AF37" mb={1}>
              {tier.tier}
            </Text>
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24" mb={1}>
              {tier.label}
            </Text>
            <Text fontSize="xs" color="#787469">{tier.desc}</Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Section 5: Curator Workflow */}
      <SectionHeading title="Curator Workflow" subtitle="6-stage pipeline from proposal to publication" />
      <Flex gap={0} mb={10} overflowX="auto" pb={2}>
        {['Propose', 'Cite', 'Frame', 'Place', 'Review', 'Publish'].map((stage, i) => (
          <Flex key={stage} align="center">
            <Box bg="#2D2A24" px={4} py={3} borderRadius="lg" textAlign="center" minW="100px">
              <Text fontFamily='"Cinzel", serif' fontSize="xs" color="#D4AF37" fontWeight={700} mb={0.5}>
                Stage {i + 1}
              </Text>
              <Text fontSize="sm" color="white" fontWeight={600}>{stage}</Text>
            </Box>
            {i < 5 && (
              <Box w="24px" h="2px" bg="#D4AF37" flexShrink={0} />
            )}
          </Flex>
        ))}
      </Flex>
    </Box>
  )
}

/* ─── Styles ─── */

const thStyle: React.CSSProperties = {
  padding: '10px 12px',
  textAlign: 'left',
  fontSize: '11px',
  fontWeight: 700,
  color: '#9E9A90',
  borderBottom: '2px solid #E4E2DC',
  fontFamily: '"Cinzel", serif',
  textTransform: 'uppercase',
  letterSpacing: '0.08em',
}

const tdStyle: React.CSSProperties = {
  padding: '8px 12px',
  fontSize: '13px',
  color: '#2D2A24',
  borderBottom: '1px solid #EEEDEA',
  fontFamily: '"Inter", sans-serif',
}
