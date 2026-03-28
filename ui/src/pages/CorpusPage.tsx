/**
 * CorpusPage — Generic corpus viewer.
 * Reads :corpusSlug from the URL and renders the matching corpus entity set.
 */
import React, { useState, useMemo } from 'react'
import { useParams, Link as RouterLink } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Heading } from '@chakra-ui/react'
import {
  BookOpen, Users, Landmark, MapPin, Clock, Layers, FileText,
  Shield, Zap, Search, ChevronDown, ChevronUp, Library,
} from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import { getCorpusBySlug, CORPUS_REGISTRY } from '../data/catalog/corpuses/registry'
import type { Entity } from '../data/catalog'

/* ── Colour tokens ── */
const MARBLE_BG = '#FAFAF8'
const BORDER    = '#E4E2DC'
const GOLD      = '#D4AF37'
const DARK_TEXT = '#2D2A24'
const MED_TEXT  = '#524E44'
const MUTED     = '#787469'

const LABEL_ICONS: Record<string, React.ReactNode> = {
  Idea:        <Zap size={14} />,
  Person:      <Users size={14} />,
  Institution: <Landmark size={14} />,
  Place:       <MapPin size={14} />,
  EventWindow: <Clock size={14} />,
  Movement:    <Layers size={14} />,
  Text:        <FileText size={14} />,
  Evidence:    <Shield size={14} />,
}

const LABEL_COLORS: Record<string, string> = {
  Person:      '#3A7D44',
  Idea:        '#D4AF37',
  Institution: '#8B3A3A',
  Place:       '#3B6BC2',
  EventWindow: '#C5963A',
  Movement:    '#6B3FA0',
  Text:        '#5A2222',
  Evidence:    '#787469',
}

const LABEL_DISPLAY: Record<string, string> = {
  Person:      'People',
  Idea:        'Ideas & Concepts',
  Institution: 'Institutions',
  Place:       'Places',
  EventWindow: 'Events',
  Movement:    'Movements',
  Text:        'Texts & Books',
  Evidence:    'Evidence & Manuscripts',
}

function groupByLabel(entities: Entity[]): { label: string; items: Entity[] }[] {
  const order = ['Text', 'Person', 'Institution', 'EventWindow', 'Movement', 'Place', 'Idea', 'Evidence']
  const map = new Map<string, Entity[]>()
  for (const e of entities) {
    const list = map.get(e.label) ?? []
    list.push(e)
    map.set(e.label, list)
  }
  return order
    .filter(l => map.has(l))
    .map(l => ({ label: l, items: map.get(l)! }))
}

/* ── Stat card ── */
function StatCard({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <Box bg="white" border="1px solid" borderColor={BORDER} borderRadius="lg" p={4} position="relative">
      <Box position="absolute" top={0} left={0} w="4px" h="100%" bg={color} borderRadius="lg 0 0 lg" />
      <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color={DARK_TEXT} pl={3}>
        {value}
      </Text>
      <Text fontSize="sm" color={MUTED} pl={3}>{label}</Text>
    </Box>
  )
}

/* ── Entity card ── */
function EntityCard({ entity }: { entity: Entity }) {
  const color = LABEL_COLORS[entity.label] ?? MUTED
  return (
    <RouterLink to={`/entity/${entity.slug}`} style={{ textDecoration: 'none' }}>
      <Box
        bg="white" border="1px solid" borderColor={BORDER}
        borderRadius="lg" p={4}
        _hover={{ borderColor: GOLD, boxShadow: '0 2px 8px rgba(212,175,55,0.15)' }}
        transition="all 0.2s" cursor="pointer" h="100%"
      >
        <Flex align="center" gap={2} mb={2}>
          <Box color={color}>{LABEL_ICONS[entity.label]}</Box>
          <Text fontSize="xs" color={color} fontWeight={600} textTransform="uppercase" letterSpacing="0.05em">
            {entity.label}
          </Text>
          <Text fontSize="xs" color={MUTED} ml="auto" fontFamily="mono">
            {entity.callNumber}
          </Text>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={600} color={DARK_TEXT} mb={1}>
          {entity.name}
        </Text>
        <Text fontSize="sm" color={MED_TEXT} lineHeight={1.5} lineClamp={3}>
          {entity.summary}
        </Text>
        {entity.period && (
          <Text fontSize="xs" color={MUTED} mt={2}>{entity.period}</Text>
        )}
      </Box>
    </RouterLink>
  )
}

/* ── Main ── */
export default function CorpusPage() {
  const { corpusSlug } = useParams<{ corpusSlug: string }>()

  const corpus = corpusSlug ? getCorpusBySlug(corpusSlug) : undefined

  const [searchTerm, setSearchTerm] = useState('')
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set(['Text', 'Person']))

  const allEntities = corpus?.entities ?? []

  const filtered = useMemo(() => {
    if (!searchTerm.trim()) return allEntities
    const q = searchTerm.toLowerCase()
    return allEntities.filter(e =>
      e.name.toLowerCase().includes(q)
      || e.summary.toLowerCase().includes(q)
      || e.subjects.some(s => s.toLowerCase().includes(q))
      || e.callNumber.toLowerCase().includes(q)
    )
  }, [searchTerm, allEntities])

  const groups = useMemo(() => groupByLabel(filtered), [filtered])

  const toggleSection = (label: string) => {
    setExpandedSections(prev => {
      const next = new Set(prev)
      next.has(label) ? next.delete(label) : next.add(label)
      return next
    })
  }

  const stats = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const e of allEntities) {
      counts[e.label] = (counts[e.label] ?? 0) + 1
    }
    return counts
  }, [allEntities])

  if (!corpus) {
    return (
      <Box p={10} textAlign="center">
        <Library size={48} color="#D6D3CC" style={{ margin: '0 auto 16px' }} />
        <Text fontFamily='"Cinzel", serif' fontSize="xl" color={DARK_TEXT} mb={2}>Corpus Not Found</Text>
        <Text fontSize="sm" color={MUTED}>
          No corpus registered for &ldquo;{corpusSlug}&rdquo;.
        </Text>
        <Flex gap={3} mt={6} justify="center" flexWrap="wrap">
          {CORPUS_REGISTRY.map(c => (
            <RouterLink key={c.slug} to={`/corpus/${c.slug}`} style={{ textDecoration: 'none' }}>
              <Box bg={MARBLE_BG} border="1px solid" borderColor={BORDER} borderRadius="lg" px={4} py={2}
                _hover={{ borderColor: GOLD }} transition="all 0.2s" cursor="pointer">
                <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{c.shortName}</Text>
              </Box>
            </RouterLink>
          ))}
        </Flex>
      </Box>
    )
  }

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Catalog', to: '/catalog' }, { label: corpus.name }]} />

      {/* ── Header ── */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <BookOpen size={28} color={corpus.color} />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color={DARK_TEXT}>
            {corpus.name}
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color={MED_TEXT} maxW="780px">
          {corpus.description}
        </Text>
        <Flex align="center" gap={2} mt={2}>
          <Box bg={`${corpus.color}15`} border={`1px solid ${corpus.color}30`} borderRadius="full" px={3} py={0.5}>
            <Text fontFamily='"Cinzel", serif' fontSize="10px" color={corpus.color}
              fontWeight={600} letterSpacing="0.08em" textTransform="uppercase">
              {corpus.zone}
            </Text>
          </Box>
        </Flex>
        <Box h="3px" bg={corpus.color} w="80px" mt={4} />
      </Box>

      {/* ── Stats ── */}
      <SimpleGrid columns={{ base: 2, md: 4, lg: 6 }} gap={4} mb={8}>
        <StatCard label="Total Nodes" value={allEntities.length} color={GOLD} />
        {(['Person', 'Text', 'Institution', 'EventWindow', 'Place', 'Movement', 'Idea', 'Evidence'] as const)
          .filter(l => stats[l])
          .map(l => (
            <StatCard key={l} label={LABEL_DISPLAY[l] ?? l} value={stats[l]} color={LABEL_COLORS[l] ?? MUTED} />
          ))
        }
      </SimpleGrid>

      {/* ── Search ── */}
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
          placeholder={`Search ${corpus.shortName} entities…`}
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
        />
      </Flex>

      {/* ── Grouped Sections ── */}
      {groups.map(({ label, items }) => {
        const isExpanded = expandedSections.has(label)
        const color = LABEL_COLORS[label] ?? MUTED
        return (
          <Box key={label} mb={8}>
            <Flex
              align="center" gap={2} cursor="pointer"
              onClick={() => toggleSection(label)}
              mb={isExpanded ? 4 : 0} pb={2}
              borderBottom="1px solid" borderColor={BORDER}
            >
              <Box color={color}>{LABEL_ICONS[label]}</Box>
              <Text fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={600} color={DARK_TEXT}>
                {LABEL_DISPLAY[label] ?? label}
              </Text>
              <Text fontSize="sm" color={MUTED} ml={1}>({items.length})</Text>
              <Box ml="auto" color={MUTED}>
                {isExpanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
              </Box>
            </Flex>
            {isExpanded && (
              <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
                {items.map(e => <EntityCard key={e.slug} entity={e} />)}
              </SimpleGrid>
            )}
          </Box>
        )
      })}

      {filtered.length === 0 && (
        <Box textAlign="center" py={12}>
          <Text color={MUTED} fontSize="lg">No entities match &ldquo;{searchTerm}&rdquo;</Text>
        </Box>
      )}
    </Box>
  )
}
