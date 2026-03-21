import React, { useState, useMemo, useCallback, useEffect } from 'react'
import { useParams, useNavigate, Navigate, useSearchParams } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import {
  Search, Library, ChevronDown,
  Users, Landmark, MapPin, Layers, Shield,
  FileText, Clock, Zap,
} from 'lucide-react'
import {
  getAllEntities, getEntityByCallNumber,
  type Entity,
} from '../data/catalog'
import { CLASS_COLORS, parseCallNumber } from '../constants/callNumbers'
import AdvancedSearch, { type ActiveFilters } from '../components/AdvancedSearch'

/* ── Constants ── */
const MARBLE_BG = '#FAFAF8'
const CARD_BG = '#F5F4F0'
const BORDER = '#E4E2DC'
const GOLD = '#D4AF37'
const DARK_TEXT = '#2D2A24'
const MED_TEXT = '#524E44'
const MUTED = '#787469'
const LIGHT_MUTED = '#9E9A90'

const LABEL_ICONS: Record<string, React.ReactNode> = {
  Idea: <Zap size={14} />,
  Person: <Users size={14} />,
  Institution: <Landmark size={14} />,
  Place: <MapPin size={14} />,
  EventWindow: <Clock size={14} />,
  Movement: <Layers size={14} />,
  Text: <FileText size={14} />,
  Evidence: <Shield size={14} />,
}

const LABEL_COLORS: Record<string, string> = {
  Person: '#3A7D44',
  Idea: '#D4AF37',
  Institution: '#8B3A3A',
  Place: '#3B6BC2',
  EventWindow: '#C5963A',
  Movement: '#6B3FA0',
  Text: '#5A2222',
  Evidence: '#787469',
}

const LABEL_DISPLAY: Record<string, string> = {
  Person: 'People',
  Idea: 'Ideas',
  Institution: 'Institutions',
  Place: 'Places',
  EventWindow: 'Events',
  Movement: 'Movements',
  Text: 'Texts',
  Evidence: 'Evidence',
}

const ERA_ORDER = ['prehistoric', 'classical', 'medieval', 'early-modern', 'modern', 'contemporary']
const ERA_LABELS: Record<string, string> = {
  prehistoric: 'Prehistoric',
  classical: 'Classical',
  medieval: 'Medieval',
  'early-modern': 'Early Modern',
  modern: 'Modern',
  contemporary: 'Contemporary',
}
const ERA_COLORS: Record<string, string> = {
  prehistoric: '#6B4D1B',
  classical: '#8B4513',
  medieval: '#A67C2E',
  'early-modern': '#C5963A',
  modern: '#4A90D9',
  contemporary: '#6B3FA0',
}

/* ── Chronological sorting ── */
const PREVIEW_COUNT = 12

function getEntityYear(e: Entity): number {
  const raw = e.born || e.founded || e.startDate || e.period || ''
  const dateStr = raw.replace(/,/g, '')
  const match = dateStr.match(/(\d{3,7})\s*(BCE|BC)?/i)
  if (!match) return 9999
  let year = parseInt(match[1])
  if (match[2]) year = -year
  return year
}

export default function CatalogPage() {
  const { callNumber } = useParams<{ callNumber: string }>()
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()

  // If we have a callNumber param, redirect to entity
  if (callNumber) {
    const entity = getEntityByCallNumber(callNumber)
    if (entity) return <Navigate to={`/entity/${entity.slug}`} replace />
  }

  const allEntities = useMemo(() => getAllEntities(), [])

  // Filters state — initialized from URL params
  const [filters, setFilters] = useState<ActiveFilters>(() => ({
    search: searchParams.get('search') || '',
    eras: searchParams.get('era') ? [searchParams.get('era')!] : [],
    labels: searchParams.get('label') ? [searchParams.get('label')!] : [],
    continents: searchParams.get('continent') ? [searchParams.get('continent')!] : [],
    frameworks: [],
  }))

  // Sync from URL params when navigating to catalog with different params
  useEffect(() => {
    setFilters({
      search: searchParams.get('search') || '',
      eras: searchParams.get('era') ? [searchParams.get('era')!] : [],
      labels: searchParams.get('label') ? [searchParams.get('label')!] : [],
      continents: searchParams.get('continent') ? [searchParams.get('continent')!] : [],
      frameworks: searchParams.get('framework') ? [searchParams.get('framework')!] : [],
    })
  }, [searchParams])

  // Track which eras are fully expanded
  const [expandedEras, setExpandedEras] = useState<Set<string>>(new Set())

  const toggleEra = useCallback((slug: string) => {
    setExpandedEras(prev => {
      const next = new Set(prev)
      if (next.has(slug)) next.delete(slug)
      else next.add(slug)
      return next
    })
  }, [])

  // Apply all filters
  const filtered = useMemo(() => {
    let result = allEntities
    if (filters.search.trim()) {
      const q = filters.search.toLowerCase()
      result = result.filter(e =>
        e.name.toLowerCase().includes(q) ||
        e.callNumber.toLowerCase().includes(q) ||
        e.subjects.some(s => s.toLowerCase().includes(q)) ||
        e.summary.toLowerCase().includes(q) ||
        e.era.toLowerCase().includes(q) ||
        e.label.toLowerCase().includes(q) ||
        e.continent.toLowerCase().includes(q) ||
        e.region.toLowerCase().includes(q)
      )
    }
    if (filters.eras.length > 0) {
      result = result.filter(e => filters.eras.includes(e.eraSlug))
    }
    if (filters.labels.length > 0) {
      result = result.filter(e => filters.labels.includes(e.label))
    }
    if (filters.continents.length > 0) {
      result = result.filter(e => filters.continents.includes(e.continent))
    }
    if (filters.frameworks.length > 0) {
      result = result.filter(e =>
        e.frameworks?.some(f => filters.frameworks.includes(f))
      )
    }
    return result
  }, [allEntities, filters])

  // Group by era, sorted chronologically within each era
  const byEra = useMemo(() => {
    const map = new Map<string, Entity[]>()
    for (const e of filtered) {
      const arr = map.get(e.eraSlug) || []
      arr.push(e)
      map.set(e.eraSlug, arr)
    }
    for (const [, arr] of map) {
      arr.sort((a, b) => getEntityYear(a) - getEntityYear(b))
    }
    return map
  }, [filtered])

  const hasActiveFilters = !!(
    filters.search || filters.eras.length || filters.labels.length ||
    filters.continents.length || filters.frameworks.length
  )

  const handleEntityClick = useCallback((e: Entity) => {
    navigate(`/entity/${e.slug}`)
  }, [navigate])

  return (
    <Box minH="100vh" bg={MARBLE_BG} p={{ base: 4, md: 6 }}>
      {/* Header */}
      <Flex align="center" gap={3} mb={4}>
        <Library size={28} color={GOLD} />
        <Box>
          <Text fontFamily="'Cinzel', serif" fontSize="2xl" color={DARK_TEXT} fontWeight={700}>
            The Catalog
          </Text>
          <Text fontSize="sm" color={MUTED}>
            {allEntities.length} actors across {new Set(allEntities.map(e => e.eraSlug)).size} eras
            {filtered.length !== allEntities.length && ` \u2022 ${filtered.length} shown`}
          </Text>
        </Box>
      </Flex>

      {/* Advanced Search + Filters (expanded by default) */}
      <AdvancedSearch allEntities={allEntities} filters={filters} onFiltersChange={setFilters} />

      {/* Stats Row — Type count badges */}
      <Flex gap={2} mb={5} flexWrap="wrap">
        {Object.entries(LABEL_COLORS).map(([label, color]) => {
          const count = filtered.filter(e => e.label === label).length
          if (count === 0) return null
          return (
            <Box key={label} px={2} py={1} borderRadius="5px" fontSize="10px" fontWeight={600}
              fontFamily="'JetBrains Mono', monospace"
              bg={`${color}10`} color={color} border="1px solid" borderColor={`${color}30`}>
              {LABEL_DISPLAY[label] || label}: {count}
            </Box>
          )
        })}
        <Box px={2} py={1} borderRadius="5px" fontSize="10px" fontWeight={700}
          fontFamily="'JetBrains Mono', monospace"
          bg={`${GOLD}15`} color={GOLD} border="1px solid" borderColor={`${GOLD}40`}>
          Total: {filtered.length}
        </Box>
      </Flex>

      {/* Results — Grouped by Era (chronological order) */}
      {ERA_ORDER.map(slug => {
        const entities = byEra.get(slug) || []
        if (entities.length === 0) return null
        const color = ERA_COLORS[slug] || MUTED
        const isExpanded = expandedEras.has(slug) || hasActiveFilters || entities.length <= PREVIEW_COUNT
        const shown = isExpanded ? entities : entities.slice(0, PREVIEW_COUNT)

        return (
          <Box key={slug} mb={8}>
            {/* Era section header */}
            <Flex align="center" gap={2} mb={3} pb={2}
              borderBottom="2px solid" borderColor={`${color}40`}>
              <Text fontFamily="'Cinzel', serif" fontSize="lg" fontWeight={700} color={color}>
                {ERA_LABELS[slug]}
              </Text>
              <Box px={2} py={0.5} borderRadius="full" fontSize="10px" fontWeight={700}
                fontFamily="'JetBrains Mono', monospace" bg={`${color}12`} color={color}>
                {entities.length}
              </Box>
            </Flex>

            {/* Entity Cards */}
            <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={3}>
              {shown.map(e => (
                <EntityCard key={e.slug} entity={e} onClick={handleEntityClick} />
              ))}
            </SimpleGrid>

            {/* Show more */}
            {!isExpanded && (
              <Flex justify="center" mt={3}>
                <Box as="button" onClick={() => toggleEra(slug)}
                  px={4} py={2} borderRadius="8px" fontSize="sm" fontWeight={600}
                  fontFamily="'Inter', sans-serif" color={color}
                  bg={`${color}08`} border="1px solid" borderColor={`${color}20`}
                  cursor="pointer"
                  _hover={{ bg: `${color}15` }}
                  display="flex" alignItems="center" gap={2}>
                  <ChevronDown size={14} />
                  Show all {entities.length} entries
                </Box>
              </Flex>
            )}
          </Box>
        )
      })}

      {/* Empty state */}
      {filtered.length === 0 && (
        <Flex direction="column" align="center" py={12} gap={2}>
          <Search size={32} color={LIGHT_MUTED} />
          <Text fontSize="md" color={MUTED} fontFamily="'Inter', sans-serif">
            No results found
          </Text>
          <Text fontSize="sm" color={LIGHT_MUTED} fontFamily="'Inter', sans-serif">
            Try adjusting your search or filters.
          </Text>
        </Flex>
      )}
    </Box>
  )
}

/* ── Entity Card ── */
function EntityCard({ entity, onClick }: { entity: Entity; onClick: (e: Entity) => void }) {
  const color = LABEL_COLORS[entity.label] || MUTED
  const parsed = parseCallNumber(entity.callNumber)
  const classColor = parsed ? CLASS_COLORS[parsed.classCode] || MUTED : MUTED

  return (
    <Box bg="#fff" border="1px solid" borderColor={BORDER} borderRadius="8px"
      overflow="hidden" cursor="pointer" onClick={() => onClick(entity)}
      _hover={{ borderColor: classColor, boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
      transition="all 0.15s">
      <Box h="3px" bg={classColor} />
      <Box p={3}>
        <Flex align="center" gap={2} mb={1.5}>
          <Text fontFamily="'JetBrains Mono', monospace" fontSize="xs" fontWeight={700}
            color={classColor}>{entity.callNumber.split('-')[0]}</Text>
          <Box px={2} py={0.5} borderRadius="4px" fontSize="10px" fontWeight={700}
            fontFamily="'JetBrains Mono', monospace" bg={`${color}12`} color={color}>
            {entity.label === 'EventWindow' ? 'EVENT' : entity.label.toUpperCase()}</Box>
          <Box ml="auto" px={2} py={0.5} borderRadius="4px" fontSize="10px" fontWeight={600}
            fontFamily="'JetBrains Mono', monospace"
            bg={`${ERA_COLORS[entity.eraSlug] || MUTED}12`}
            color={ERA_COLORS[entity.eraSlug] || MUTED}>
            {entity.era}</Box>
        </Flex>
        <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
          color={DARK_TEXT} lineClamp={1} mb={1}>{entity.name}</Text>
        <Text fontSize="xs" color={MUTED} fontFamily="'JetBrains Mono', monospace" mb={1.5}>
          {entity.period || entity.born || entity.founded || entity.startDate || ''}
          {entity.died ? ` \u2014 ${entity.died}` : entity.endDate ? ` \u2014 ${entity.endDate}` : ''}</Text>
        <Text fontSize="xs" color={MED_TEXT} lineClamp={2} fontFamily="'Inter', sans-serif"
          lineHeight="1.5">{entity.summary}</Text>
        <Flex gap={1} mt={2} flexWrap="wrap">
          {entity.subjects.slice(0, 3).map(s => (
            <Text key={s} fontSize="10px" px={1.5} py={0.5} bg={`${GOLD}08`} color={MUTED}
              borderRadius="3px" fontFamily="'Inter', sans-serif">{s}</Text>
          ))}
        </Flex>
        {entity.frameworks && entity.frameworks.length > 0 && (
          <Flex gap={1} mt={1.5} flexWrap="wrap">
            {entity.frameworks.slice(0, 2).map(f => (
              <Text key={f} fontSize="9px" px={1.5} py={0.5}
                bg={`${GOLD}12`} color={GOLD}
                borderRadius="3px" fontFamily="'JetBrains Mono', monospace" fontWeight={600}>
                {f.replace(/_/g, ' ')}</Text>
            ))}
          </Flex>
        )}
      </Box>
    </Box>
  )
}
