import React, { useState, useMemo, useCallback, useEffect } from 'react'
import { useParams, useNavigate, useSearchParams } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import {
  Search, Library, ChevronDown,
} from 'lucide-react'
import type { Entity } from '../data/entityTypes'
import { CLASS_COLORS, DIVISIONS, parseCallNumber } from '../constants/callNumbers'
import AdvancedSearch, { type ActiveFilters } from '../components/AdvancedSearch'
import { fetchEntitiesWithTotal, fetchLabelCounts, fetchTotalCount, fetchEntity } from '../services/entityService'

/* ── Era Division date ranges (from callNumbers.ts class 9) ── */
const ERA_DIVISION_RANGES: Record<string, { start: number; end: number; broadEra: string }> = {
  '911': { start: -70000, end: -10000, broadEra: 'prehistoric' },
  '912': { start: -10000, end: -3300, broadEra: 'prehistoric' },
  '913': { start: -3300, end: -1200, broadEra: 'prehistoric' },
  '921': { start: -800, end: -480, broadEra: 'classical' },
  '922': { start: -323, end: -31, broadEra: 'classical' },
  '923': { start: -31, end: 476, broadEra: 'classical' },
  '924': { start: 250, end: 600, broadEra: 'classical' },
  '931': { start: 500, end: 1000, broadEra: 'medieval' },
  '932': { start: 1000, end: 1300, broadEra: 'medieval' },
  '933': { start: 1300, end: 1500, broadEra: 'medieval' },
  '941': { start: 1400, end: 1600, broadEra: 'early-modern' },
  '942': { start: 1300, end: 1600, broadEra: 'early-modern' },
  '943': { start: 1517, end: 1648, broadEra: 'early-modern' },
  '944': { start: 1685, end: 1815, broadEra: 'early-modern' },
  '951': { start: 1760, end: 1840, broadEra: 'modern' },
  '952': { start: 1870, end: 1914, broadEra: 'modern' },
  '953': { start: 1918, end: 1939, broadEra: 'modern' },
  '954': { start: 1939, end: 1945, broadEra: 'modern' },
  '961': { start: 1947, end: 1991, broadEra: 'contemporary' },
  '962': { start: 1991, end: 2001, broadEra: 'contemporary' },
  '963': { start: 2001, end: 2100, broadEra: 'contemporary' },
}
const ERA_DIVISION_LABELS: Record<string, string> = {
  '911': 'Paleolithic & Mesolithic', '912': 'Neolithic & Chalcolithic', '913': 'Bronze Age',
  '921': 'Archaic Period', '922': 'Hellenistic Period', '923': 'Roman Period', '924': 'Late Antiquity',
  '931': 'Early Medieval / Dark Ages', '932': 'High Medieval', '933': 'Late Medieval',
  '941': 'Age of Exploration', '942': 'Renaissance Period', '943': 'Reformation Era', '944': 'Age of Enlightenment',
  '951': 'Industrial Age', '952': 'Age of Empire', '953': 'Interwar Period', '954': 'World War II Era',
  '961': 'Cold War Era', '962': 'Post-Cold War & Globalization', '963': 'Digital Age',
}

/* ── Constants ── */
const MARBLE_BG = '#FAFAF8'
const BORDER = '#E4E2DC'
const GOLD = '#D4AF37'
const DARK_TEXT = '#2D2A24'
const MED_TEXT = '#524E44'
const MUTED = '#787469'
const LIGHT_MUTED = '#9E9A90'

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

const PAGE_SIZE = 100

export default function CatalogPage() {
  const { callNumber } = useParams<{ callNumber: string }>()
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()

  // Backend data state
  const [entities, setEntities] = useState<Entity[]>([])
  const [totalCount, setTotalCount] = useState<number>(0)
  const [backendTotal, setBackendTotal] = useState<number>(0)
  const [labelCounts, setLabelCounts] = useState<Record<string, number>>({})
  const [loading, setLoading] = useState(true)
  const [loadingMore, setLoadingMore] = useState(false)

  // If we have a callNumber param, look up entity from backend and redirect
  useEffect(() => {
    if (!callNumber) return
    let cancelled = false
    async function lookupByCallNumber() {
      // Try to find entity by searching the call number
      const res = await fetchEntitiesWithTotal({ search: callNumber, limit: 1 })
      if (!cancelled && res.entities.length > 0) {
        navigate(`/entity/${res.entities[0].slug}`, { replace: true })
      }
    }
    lookupByCallNumber()
    return () => { cancelled = true }
  }, [callNumber, navigate])

  // Filters state — initialized from URL params
  const [filters, setFilters] = useState<ActiveFilters>(() => ({
    search: searchParams.get('search') || '',
    eras: searchParams.get('era') ? [searchParams.get('era')!] : [],
    labels: searchParams.get('label') ? [searchParams.get('label')!] : [],
    continents: searchParams.get('continent') ? [searchParams.get('continent')!] : [],
    frameworks: [],
    classes: searchParams.get('class') ? [parseInt(searchParams.get('class')!)] : [],
    divisions: searchParams.get('division') ? [searchParams.get('division')!] : [],
  }))

  const eraDivision = searchParams.get('eraDivision') || ''

  // Sync from URL params
  useEffect(() => {
    setFilters({
      search: searchParams.get('search') || '',
      eras: searchParams.get('era') ? [searchParams.get('era')!] : [],
      labels: searchParams.get('label') ? [searchParams.get('label')!] : [],
      continents: searchParams.get('continent') ? [searchParams.get('continent')!] : [],
      frameworks: searchParams.get('framework') ? [searchParams.get('framework')!] : [],
      classes: searchParams.get('class') ? [parseInt(searchParams.get('class')!)] : [],
      divisions: searchParams.get('division') ? [searchParams.get('division')!] : [],
    })
  }, [searchParams])

  // Fetch backend total + label counts on mount
  useEffect(() => {
    let cancelled = false
    async function fetchMeta() {
      const [total, counts] = await Promise.all([fetchTotalCount(), fetchLabelCounts()])
      if (!cancelled) {
        setBackendTotal(total)
        setLabelCounts(counts)
      }
    }
    fetchMeta()
    return () => { cancelled = true }
  }, [])

  // Fetch entities from backend when filters change
  useEffect(() => {
    let cancelled = false
    async function loadEntities() {
      setLoading(true)
      setEntities([])

      const opts: Parameters<typeof fetchEntitiesWithTotal>[0] = {
        limit: PAGE_SIZE,
        offset: 0,
      }
      if (filters.eras.length === 1) opts.era = filters.eras[0]
      if (filters.labels.length === 1) opts.label = filters.labels[0]
      if (filters.continents.length === 1) opts.continent = filters.continents[0]
      if (eraDivision) opts.eraDivision = eraDivision
      if (filters.search.trim()) opts.search = filters.search.trim()

      const result = await fetchEntitiesWithTotal(opts)
      if (!cancelled) {
        let filtered = result.entities
        if (filters.eras.length > 1) filtered = filtered.filter(e => filters.eras.includes(e.eraSlug))
        if (filters.labels.length > 1) filtered = filtered.filter(e => filters.labels.includes(e.label))
        if (filters.continents.length > 1) filtered = filtered.filter(e => filters.continents.includes(e.continent))
        if (filters.frameworks.length > 0) {
          filtered = filtered.filter(e => e.frameworks?.some(f => filters.frameworks.includes(f)))
        }
        if (filters.classes.length > 0) {
          filtered = filtered.filter(e => {
            const p = parseCallNumber(e.callNumber)
            return p ? filters.classes.includes(p.classCode) : false
          })
        }
        if (filters.divisions.length > 0) {
          filtered = filtered.filter(e => {
            const p = parseCallNumber(e.callNumber)
            return p ? filters.divisions.includes(p.division) : false
          })
        }
        setEntities(filtered)
        setTotalCount(result.total)
        setLoading(false)
      }
    }
    loadEntities()
    return () => { cancelled = true }
  }, [filters, eraDivision])

  // Load more
  const loadMore = useCallback(async () => {
    setLoadingMore(true)
    const opts: Parameters<typeof fetchEntitiesWithTotal>[0] = {
      limit: PAGE_SIZE,
      offset: entities.length,
    }
    if (filters.eras.length === 1) opts.era = filters.eras[0]
    if (filters.labels.length === 1) opts.label = filters.labels[0]
    if (filters.continents.length === 1) opts.continent = filters.continents[0]
    if (eraDivision) opts.eraDivision = eraDivision
    if (filters.search.trim()) opts.search = filters.search.trim()

    const result = await fetchEntitiesWithTotal(opts)
    setEntities(prev => [...prev, ...result.entities])
    setTotalCount(result.total)
    setLoadingMore(false)
  }, [entities.length, filters, eraDivision])

  // Group by era
  const byEra = useMemo(() => {
    const map = new Map<string, Entity[]>()
    for (const e of entities) {
      const arr = map.get(e.eraSlug) || []
      arr.push(e)
      map.set(e.eraSlug, arr)
    }
    return map
  }, [entities])

  const handleEntityClick = useCallback((e: Entity) => {
    navigate(`/entity/${e.slug}`)
  }, [navigate])

  const hasMore = entities.length < totalCount

  return (
    <Box minH="100vh" bg={MARBLE_BG} p={{ base: 4, md: 6 }}>
      {/* Header */}
      <Flex align="center" gap={3} mb={4}>
        <Library size={28} color={GOLD} />
        <Box>
          <Text fontFamily="'Cinzel', serif" fontSize="2xl" color={DARK_TEXT} fontWeight={700}>
            {eraDivision && ERA_DIVISION_LABELS[eraDivision]
              ? `${eraDivision} ${ERA_DIVISION_LABELS[eraDivision]}`
              : filters.divisions.length === 1
              ? (DIVISIONS.find(d => d.code === filters.divisions[0])?.heading || 'The Catalog')
              : 'The Catalog'}
          </Text>
          <Text fontSize="sm" color={MUTED}>
            {backendTotal.toLocaleString()} actors in the Annals backend
            {totalCount > 0 && totalCount !== backendTotal && ` \u2022 ${totalCount.toLocaleString()} matching`}
            {entities.length > 0 && entities.length < totalCount && ` \u2022 ${entities.length.toLocaleString()} loaded`}
          </Text>
        </Box>
      </Flex>

      {/* Advanced Search + Filters */}
      <AdvancedSearch filters={filters} onFiltersChange={setFilters} />

      {/* Stats Row — Type count badges from backend */}
      <Flex gap={2} mb={5} flexWrap="wrap">
        {Object.entries(LABEL_COLORS).map(([label, color]) => {
          const count = labelCounts[label] || 0
          if (count === 0) return null
          return (
            <Box key={label} px={2} py={1} borderRadius="5px" fontSize="10px" fontWeight={600}
              fontFamily="'JetBrains Mono', monospace"
              bg={`${color}10`} color={color} border="1px solid" borderColor={`${color}30`}
              cursor="pointer"
              onClick={() => setFilters(f => ({ ...f, labels: [label] }))}
              _hover={{ bg: `${color}20` }}>
              {LABEL_DISPLAY[label] || label}: {count.toLocaleString()}
            </Box>
          )
        })}
        <Box px={2} py={1} borderRadius="5px" fontSize="10px" fontWeight={700}
          fontFamily="'JetBrains Mono', monospace"
          bg={`${GOLD}15`} color={GOLD} border="1px solid" borderColor={`${GOLD}40`}>
          Total: {backendTotal.toLocaleString()}
        </Box>
      </Flex>

      {/* Loading State */}
      {loading && (
        <Flex justify="center" align="center" py={12} gap={3}>
          <Spinner color={GOLD} size="lg" />
          <Text fontFamily="'JetBrains Mono', monospace" fontSize="sm" color={MUTED}>
            Fetching from Annals backend…
          </Text>
        </Flex>
      )}

      {/* Results — Grouped by Era */}
      {!loading && ERA_ORDER.map(slug => {
        const eraEntities = byEra.get(slug) || []
        if (eraEntities.length === 0) return null
        const color = ERA_COLORS[slug] || MUTED

        return (
          <Box key={slug} mb={8}>
            <Flex align="center" gap={2} mb={3} pb={2}
              borderBottom="2px solid" borderColor={`${color}40`}>
              <Text fontFamily="'Cinzel', serif" fontSize="lg" fontWeight={700} color={color}>
                {ERA_LABELS[slug]}
              </Text>
              <Box px={2} py={0.5} borderRadius="full" fontSize="10px" fontWeight={700}
                fontFamily="'JetBrains Mono', monospace" bg={`${color}12`} color={color}>
                {eraEntities.length}
              </Box>
            </Flex>

            <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={3}>
              {eraEntities.map(e => (
                <EntityCard key={e.slug} entity={e} onClick={handleEntityClick} />
              ))}
            </SimpleGrid>
          </Box>
        )
      })}

      {/* Load More */}
      {!loading && hasMore && (
        <Flex justify="center" mt={4} mb={8}>
          <Box as="button" onClick={loadMore}
            px={6} py={3} borderRadius="xl" fontSize="sm" fontWeight={700}
            fontFamily="'Cinzel', serif" color={GOLD}
            bg={`${GOLD}08`} border="1px solid" borderColor={`${GOLD}30`}
            cursor={loadingMore ? 'wait' : 'pointer'}
            _hover={{ bg: `${GOLD}15` }}
            display="flex" alignItems="center" gap={2}
            letterSpacing="0.08em"
            textTransform="uppercase">
            {loadingMore ? (
              <><Spinner size="sm" color={GOLD} /> Loading…</>
            ) : (
              <><ChevronDown size={16} /> Load More ({Math.min(PAGE_SIZE, totalCount - entities.length).toLocaleString()} of {(totalCount - entities.length).toLocaleString()} remaining)</>
            )}
          </Box>
        </Flex>
      )}

      {/* Empty state */}
      {!loading && entities.length === 0 && (
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
