import React, { useState, useMemo, useCallback } from 'react'
import { useParams, useNavigate, Navigate } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Input } from '@chakra-ui/react'
import {
  Search, Library, ChevronRight, Filter, BookOpen,
  Users, Landmark, MapPin, Layers, Scroll, Shield,
  FileText, Clock, Zap,
} from 'lucide-react'
import {
  getAllEntities, getEntityByCallNumber,
  type Entity,
} from '../data/catalog'
import {
  CLASSES, DIVISIONS, CLASS_COLORS,
  parseCallNumber,
} from '../constants/callNumbers'

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

type ViewMode = 'class' | 'era' | 'label'

export default function CatalogPage() {
  const { callNumber } = useParams<{ callNumber: string }>()
  const navigate = useNavigate()

  // If we have a callNumber param, redirect to entity
  if (callNumber) {
    const entity = getEntityByCallNumber(callNumber)
    if (entity) return <Navigate to={`/entity/${entity.slug}`} replace />
  }

  const allEntities = useMemo(() => getAllEntities(), [])
  const [search, setSearch] = useState('')
  const [viewMode, setViewMode] = useState<ViewMode>('class')
  const [selectedClass, setSelectedClass] = useState<number | null>(null)
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [selectedLabel, setSelectedLabel] = useState<string | null>(null)

  const filtered = useMemo(() => {
    if (!search.trim()) return allEntities
    const q = search.toLowerCase()
    return allEntities.filter(e =>
      e.name.toLowerCase().includes(q) ||
      e.callNumber.toLowerCase().includes(q) ||
      e.subjects.some(s => s.toLowerCase().includes(q)) ||
      e.summary.toLowerCase().includes(q) ||
      e.era.toLowerCase().includes(q) ||
      e.label.toLowerCase().includes(q)
    )
  }, [allEntities, search])

  const byClass = useMemo(() => {
    const map = new Map<number, Entity[]>()
    for (const e of filtered) {
      const parsed = parseCallNumber(e.callNumber)
      if (!parsed) continue
      const arr = map.get(parsed.classCode) || []
      arr.push(e)
      map.set(parsed.classCode, arr)
    }
    for (const [, arr] of map) arr.sort((a, b) => a.callNumber.localeCompare(b.callNumber))
    return map
  }, [filtered])

  const byEra = useMemo(() => {
    const map = new Map<string, Entity[]>()
    for (const e of filtered) {
      const arr = map.get(e.eraSlug) || []
      arr.push(e)
      map.set(e.eraSlug, arr)
    }
    for (const [, arr] of map) arr.sort((a, b) => a.callNumber.localeCompare(b.callNumber))
    return map
  }, [filtered])

  const byLabel = useMemo(() => {
    const map = new Map<string, Entity[]>()
    for (const e of filtered) {
      const arr = map.get(e.label) || []
      arr.push(e)
      map.set(e.label, arr)
    }
    for (const [, arr] of map) arr.sort((a, b) => a.callNumber.localeCompare(b.callNumber))
    return map
  }, [filtered])

  const divisionGroups = useMemo(() => {
    if (selectedClass === null) return new Map<string, Entity[]>()
    const entities = byClass.get(selectedClass) || []
    const map = new Map<string, Entity[]>()
    for (const e of entities) {
      const parsed = parseCallNumber(e.callNumber)
      if (!parsed) continue
      const arr = map.get(parsed.division) || []
      arr.push(e)
      map.set(parsed.division, arr)
    }
    return map
  }, [byClass, selectedClass])

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
          </Text>
        </Box>
      </Flex>

      {/* Search + View Toggle */}
      <Flex gap={3} mb={5} direction={{ base: 'column', md: 'row' }} align={{ md: 'center' }}>
        <Box position="relative" flex={1} maxW={{ md: '480px' }}>
          <Box position="absolute" left={3} top="50%" transform="translateY(-50%)" zIndex={1}>
            <Search size={16} color={MUTED} />
          </Box>
          <Input
            pl={10}
            value={search}
            onChange={(ev: React.ChangeEvent<HTMLInputElement>) => setSearch(ev.target.value)}
            placeholder="Search by name, call number, subject, era..."
            bg={CARD_BG}
            border="1px solid"
            borderColor={BORDER}
            borderRadius="8px"
            fontSize="sm"
            fontFamily="'Inter', sans-serif"
            _focus={{ borderColor: GOLD, boxShadow: `0 0 0 1px ${GOLD}` }}
            _placeholder={{ color: LIGHT_MUTED }}
          />
        </Box>
        <Flex gap={2}>
          {([
            ['class', 'By Class', <BookOpen size={14} key="c" />],
            ['era', 'By Era', <Clock size={14} key="e" />],
            ['label', 'By Type', <Filter size={14} key="l" />],
          ] as [ViewMode, string, React.ReactNode][]).map(([mode, label, icon]) => (
            <Box
              key={mode}
              as="button"
              onClick={() => { setViewMode(mode); setSelectedClass(null); setSelectedEra(null); setSelectedLabel(null) }}
              px={3} py={1.5} borderRadius="6px" fontSize="xs" fontWeight={600}
              fontFamily="'Inter', sans-serif"
              bg={viewMode === mode ? GOLD : CARD_BG}
              color={viewMode === mode ? '#fff' : MED_TEXT}
              border="1px solid"
              borderColor={viewMode === mode ? GOLD : BORDER}
              cursor="pointer"
              display="flex" alignItems="center" gap={1.5}
              _hover={{ bg: viewMode === mode ? GOLD : BORDER }}
            >
              {icon} {label}
            </Box>
          ))}
        </Flex>
      </Flex>

      {/* Stats Row */}
      <Flex gap={3} mb={5} flexWrap="wrap">
        {Object.entries(LABEL_COLORS).map(([label, color]) => {
          const count = allEntities.filter(e => e.label === label).length
          if (count === 0) return null
          return (
            <Box key={label} px={3} py={1.5} borderRadius="6px" fontSize="xs" fontWeight={600}
              fontFamily="'JetBrains Mono', monospace"
              bg={`${color}10`} color={color} border="1px solid" borderColor={`${color}30`}>
              {label === 'EventWindow' ? 'Event' : label}s: {count}
            </Box>
          )
        })}
        <Box px={3} py={1.5} borderRadius="6px" fontSize="xs" fontWeight={700}
          fontFamily="'JetBrains Mono', monospace"
          bg={`${GOLD}15`} color={GOLD} border="1px solid" borderColor={`${GOLD}40`}>
          Total: {allEntities.length}
        </Box>
      </Flex>

      {/* By Class — Overview Cards */}
      {viewMode === 'class' && selectedClass === null && (
        <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={4}>
          {CLASSES.map(cls => {
            const entities = byClass.get(cls.code) || []
            if (entities.length === 0 && !search) return null
            return (
              <Box key={cls.code} bg={CARD_BG} border="1px solid" borderColor={BORDER}
                borderRadius="10px" overflow="hidden" cursor="pointer"
                onClick={() => setSelectedClass(cls.code)}
                _hover={{ borderColor: CLASS_COLORS[cls.code] || GOLD, transform: 'translateY(-2px)' }}
                transition="all 0.2s">
                <Box h="4px" bg={CLASS_COLORS[cls.code] || GOLD} />
                <Box p={4}>
                  <Flex align="center" justify="space-between" mb={2}>
                    <Text fontFamily="'JetBrains Mono', monospace" fontSize="2xl" fontWeight={700}
                      color={CLASS_COLORS[cls.code] || GOLD}>{cls.code}</Text>
                    <Text fontFamily="'JetBrains Mono', monospace" fontSize="xs" color={MUTED}>
                      {entities.length} entries</Text>
                  </Flex>
                  <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={600}
                    color={DARK_TEXT} mb={2}>{cls.heading}</Text>
                  <Flex gap={1} flexWrap="wrap">
                    {entities.slice(0, 4).map((e, i) => (
                      <Text key={e.slug} fontSize="xs" color={MUTED} fontFamily="'Inter', sans-serif">
                        {e.name}{i < 3 && entities.length > 1 ? ' \u00b7 ' : ''}</Text>
                    ))}
                    {entities.length > 4 && (
                      <Text fontSize="xs" color={LIGHT_MUTED}>+{entities.length - 4} more</Text>
                    )}
                  </Flex>
                </Box>
              </Box>
            )
          })}
        </SimpleGrid>
      )}

      {/* Class Drill-Down */}
      {viewMode === 'class' && selectedClass !== null && (
        <Box>
          <Flex align="center" gap={2} mb={4}>
            <Box as="button" onClick={() => setSelectedClass(null)} fontSize="sm"
              color={GOLD} fontFamily="'Inter', sans-serif" cursor="pointer"
              _hover={{ textDecoration: 'underline' }}>
              {"\u2190"} All Classes</Box>
            <ChevronRight size={14} color={MUTED} />
            <Text fontFamily="'JetBrains Mono', monospace" fontSize="sm" fontWeight={700}
              color={CLASS_COLORS[selectedClass] || GOLD}>{selectedClass}</Text>
            <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={600} color={DARK_TEXT}>
              {CLASSES.find(c => c.code === selectedClass)?.heading}</Text>
            <Text fontSize="xs" color={MUTED} ml="auto" fontFamily="'JetBrains Mono', monospace">
              {(byClass.get(selectedClass) || []).length} entries</Text>
          </Flex>
          {Array.from(divisionGroups.entries())
            .sort(([a], [b]) => a.localeCompare(b))
            .map(([divCode, entities]) => {
              const divHeading = DIVISIONS.find(d => d.code === divCode)?.heading || divCode
              return (
                <Box key={divCode} mb={5}>
                  <Flex align="center" gap={2} mb={2} pb={1} borderBottom="1px solid" borderColor={BORDER}>
                    <Text fontFamily="'JetBrains Mono', monospace" fontSize="sm" fontWeight={700}
                      color={CLASS_COLORS[selectedClass] || GOLD}>{divCode}</Text>
                    <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={600}
                      color={DARK_TEXT}>{divHeading}</Text>
                    <Text fontSize="xs" color={MUTED} ml="auto">{entities.length}</Text>
                  </Flex>
                  <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={3}>
                    {entities.map(e => (
                      <EntityCard key={e.slug} entity={e} onClick={handleEntityClick} />
                    ))}
                  </SimpleGrid>
                </Box>
              )
            })}
        </Box>
      )}

      {/* By Era — Overview */}
      {viewMode === 'era' && selectedEra === null && (
        <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={4}>
          {ERA_ORDER.map(slug => {
            const entities = byEra.get(slug) || []
            if (entities.length === 0 && !search) return null
            const color = ERA_COLORS[slug] || MUTED
            return (
              <Box key={slug} bg={CARD_BG} border="1px solid" borderColor={BORDER}
                borderRadius="10px" overflow="hidden" cursor="pointer"
                onClick={() => setSelectedEra(slug)}
                _hover={{ borderColor: color, transform: 'translateY(-2px)' }}
                transition="all 0.2s">
                <Box h="4px" bg={color} />
                <Box p={4}>
                  <Flex align="center" justify="space-between" mb={2}>
                    <Text fontFamily="'Cinzel', serif" fontSize="lg" fontWeight={700} color={color}>
                      {ERA_LABELS[slug] || slug}</Text>
                    <Text fontFamily="'JetBrains Mono', monospace" fontSize="xs" color={MUTED}>
                      {entities.length} entries</Text>
                  </Flex>
                  <Flex gap={1} flexWrap="wrap">
                    {entities.slice(0, 5).map((e, i) => (
                      <Text key={e.slug} fontSize="xs" color={MUTED}>
                        {e.name}{i < 4 && entities.length > 1 ? ' \u00b7 ' : ''}</Text>
                    ))}
                    {entities.length > 5 && (
                      <Text fontSize="xs" color={LIGHT_MUTED}>+{entities.length - 5} more</Text>
                    )}
                  </Flex>
                </Box>
              </Box>
            )
          })}
        </SimpleGrid>
      )}

      {/* Era Drill-Down */}
      {viewMode === 'era' && selectedEra !== null && (
        <Box>
          <Flex align="center" gap={2} mb={4}>
            <Box as="button" onClick={() => setSelectedEra(null)} fontSize="sm"
              color={GOLD} fontFamily="'Inter', sans-serif" cursor="pointer"
              _hover={{ textDecoration: 'underline' }}>
              {"\u2190"} All Eras</Box>
            <ChevronRight size={14} color={MUTED} />
            <Text fontFamily="'Cinzel', serif" fontSize="lg" fontWeight={700}
              color={ERA_COLORS[selectedEra] || MUTED}>{ERA_LABELS[selectedEra] || selectedEra}</Text>
            <Text fontSize="xs" color={MUTED} ml="auto" fontFamily="'JetBrains Mono', monospace">
              {(byEra.get(selectedEra) || []).length} entries</Text>
          </Flex>
          <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={3}>
            {(byEra.get(selectedEra) || []).map(e => (
              <EntityCard key={e.slug} entity={e} onClick={handleEntityClick} />
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* By Type — Overview */}
      {viewMode === 'label' && selectedLabel === null && (
        <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={4}>
          {Object.entries(LABEL_COLORS).map(([label, color]) => {
            const entities = byLabel.get(label) || []
            if (entities.length === 0 && !search) return null
            return (
              <Box key={label} bg={CARD_BG} border="1px solid" borderColor={BORDER}
                borderRadius="10px" overflow="hidden" cursor="pointer"
                onClick={() => setSelectedLabel(label)}
                _hover={{ borderColor: color, transform: 'translateY(-2px)' }}
                transition="all 0.2s">
                <Box h="4px" bg={color} />
                <Box p={4}>
                  <Flex align="center" gap={2} mb={2}>
                    {LABEL_ICONS[label]}
                    <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={600}
                      color={DARK_TEXT}>{label === 'EventWindow' ? 'Event' : label}s</Text>
                    <Text fontSize="xs" color={MUTED} ml="auto" fontFamily="'JetBrains Mono', monospace">
                      {entities.length}</Text>
                  </Flex>
                  <Flex gap={1} flexWrap="wrap">
                    {entities.slice(0, 4).map((e, i) => (
                      <Text key={e.slug} fontSize="xs" color={MUTED}>
                        {e.name}{i < 3 && entities.length > 1 ? ' \u00b7 ' : ''}</Text>
                    ))}
                    {entities.length > 4 && (
                      <Text fontSize="xs" color={LIGHT_MUTED}>+{entities.length - 4} more</Text>
                    )}
                  </Flex>
                </Box>
              </Box>
            )
          })}
        </SimpleGrid>
      )}

      {/* Label Drill-Down */}
      {viewMode === 'label' && selectedLabel !== null && (
        <Box>
          <Flex align="center" gap={2} mb={4}>
            <Box as="button" onClick={() => setSelectedLabel(null)} fontSize="sm"
              color={GOLD} fontFamily="'Inter', sans-serif" cursor="pointer"
              _hover={{ textDecoration: 'underline' }}>
              {"\u2190"} All Types</Box>
            <ChevronRight size={14} color={MUTED} />
            {LABEL_ICONS[selectedLabel]}
            <Text fontFamily="'Cormorant Garamond', serif" fontSize="lg" fontWeight={600}
              color={LABEL_COLORS[selectedLabel] || MUTED}>
              {selectedLabel === 'EventWindow' ? 'Event' : selectedLabel}s</Text>
            <Text fontSize="xs" color={MUTED} ml="auto" fontFamily="'JetBrains Mono', monospace">
              {(byLabel.get(selectedLabel) || []).length} entries</Text>
          </Flex>
          <SimpleGrid columns={{ base: 1, sm: 2, lg: 3, xl: 4 }} gap={3}>
            {(byLabel.get(selectedLabel) || []).map(e => (
              <EntityCard key={e.slug} entity={e} onClick={handleEntityClick} />
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* Empty search */}
      {search.trim() && filtered.length === 0 && (
        <Flex direction="column" align="center" py={12} gap={2}>
          <Search size={32} color={LIGHT_MUTED} />
          <Text fontSize="md" color={MUTED} fontFamily="'Inter', sans-serif">
            No results for &quot;{search}&quot;</Text>
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
