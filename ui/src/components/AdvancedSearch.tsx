/**
 * AdvancedSearch — Autocomplete typeahead search + multi-filter component
 *
 * Features:
 * - Debounced fuzzy search with dropdown showing top-N matching entities
 * - Each result shows: name, call number badge, label badge, era pill
 * - Multi-select filters: Era, Label/Type, Continent, Framework
 * - Keyboard navigation (arrow keys, Enter, Escape)
 * - Click-away dismiss
 */
import React, { useState, useRef, useEffect, useMemo, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import { Box, Flex, Text, Input } from '@chakra-ui/react'
import {
  Search, X, ChevronDown, ChevronUp,
  Users, Landmark, MapPin, Layers, Clock, FileText, Shield, Zap,
} from 'lucide-react'
import type { Entity } from '../data/entityTypes'

/* ── Design tokens ── */
const CARD_BG = '#F5F4F0'
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

const LABEL_ICONS: Record<string, React.ReactNode> = {
  Idea: <Zap size={12} />,
  Person: <Users size={12} />,
  Institution: <Landmark size={12} />,
  Place: <MapPin size={12} />,
  EventWindow: <Clock size={12} />,
  Movement: <Layers size={12} />,
  Text: <FileText size={12} />,
  Evidence: <Shield size={12} />,
}

const ERA_COLORS: Record<string, string> = {
  prehistoric: '#6B4D1B',
  classical: '#8B4513',
  medieval: '#A67C2E',
  'early-modern': '#C5963A',
  modern: '#4A90D9',
  contemporary: '#6B3FA0',
}

const ERA_LABELS: Record<string, string> = {
  prehistoric: 'Prehistoric',
  classical: 'Classical',
  medieval: 'Medieval',
  'early-modern': 'Early Modern',
  modern: 'Modern',
  contemporary: 'Contemporary',
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

const CONTINENTS = ['Africa', 'Asia', 'Europe', 'Americas', 'Oceania']

const FRAMEWORKS = [
  'CAUSE_AND_EFFECT',
  'CULTURAL_DIFFUSION',
  'DOCTRINE_DEVELOPMENT',
  'TEXTUAL_TRANSMISSION',
  'LEGAL_INTERPRETATION',
  'RITUAL_STANDARDIZATION',
  'GEOPOLITICAL_LINKAGE',
  'CONFLICT_AND_RESOLUTION',
  'ADAPTATION',
  'TEMPORAL_LINKAGE',
  'ECONOMIC_SYSTEMS',
  'POLITICAL_SYSTEMS',
  'COMPARATIVE_RELIGION',
  'EMPIRE_AND_COLONIALISM',
  'ENVIRONMENTAL_HISTORY',
  'INNOVATION_AND_TECHNOLOGY',
]

const MAX_AUTOCOMPLETE = 8

/* ── Helper: score a search hit ── */
function scoreMatch(entity: Entity, query: string): number {
  const q = query.toLowerCase()
  const name = entity.name.toLowerCase()
  // Exact name match → highest
  if (name === q) return 100
  // Name starts with query
  if (name.startsWith(q)) return 90
  // Name contains query
  if (name.includes(q)) return 80
  // Call number match
  if (entity.callNumber.toLowerCase().includes(q)) return 70
  // Subject match
  if (entity.subjects.some(s => s.toLowerCase().includes(q))) return 60
  // Summary match
  if (entity.summary.toLowerCase().includes(q)) return 40
  // Era / label match
  if (entity.era.toLowerCase().includes(q) || entity.label.toLowerCase().includes(q)) return 30
  return 0
}

/* ── Types ── */
export interface ActiveFilters {
  search: string
  eras: string[]
  labels: string[]
  continents: string[]
  frameworks: string[]
}

interface AdvancedSearchProps {
  allEntities: Entity[]
  filters: ActiveFilters
  onFiltersChange: (f: ActiveFilters) => void
}

/* ── Component ── */
export default function AdvancedSearch({ allEntities, filters, onFiltersChange }: AdvancedSearchProps) {
  const navigate = useNavigate()
  const inputRef = useRef<HTMLInputElement>(null)
  const dropdownRef = useRef<HTMLDivElement>(null)
  const [showDropdown, setShowDropdown] = useState(false)
  const [highlightIdx, setHighlightIdx] = useState(-1)
  const [showFilters, setShowFilters] = useState(true)

  // Autocomplete results
  const suggestions = useMemo(() => {
    const q = filters.search.trim()
    if (!q || q.length < 2) return []
    return allEntities
      .map(e => ({ entity: e, score: scoreMatch(e, q) }))
      .filter(r => r.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, MAX_AUTOCOMPLETE)
      .map(r => r.entity)
  }, [allEntities, filters.search])

  // Active filter count (not counting search)
  const activeFilterCount = filters.eras.length + filters.labels.length
    + filters.continents.length + filters.frameworks.length

  // Close dropdown on click-away
  useEffect(() => {
    function handleClick(ev: MouseEvent) {
      if (
        dropdownRef.current && !dropdownRef.current.contains(ev.target as Node) &&
        inputRef.current && !inputRef.current.contains(ev.target as Node)
      ) {
        setShowDropdown(false)
      }
    }
    document.addEventListener('mousedown', handleClick)
    return () => document.removeEventListener('mousedown', handleClick)
  }, [])

  // Keyboard nav
  const handleKeyDown = useCallback((ev: React.KeyboardEvent) => {
    if (!showDropdown || suggestions.length === 0) {
      if (ev.key === 'Escape') {
        setShowDropdown(false)
        inputRef.current?.blur()
      }
      return
    }
    switch (ev.key) {
      case 'ArrowDown':
        ev.preventDefault()
        setHighlightIdx(prev => Math.min(prev + 1, suggestions.length - 1))
        break
      case 'ArrowUp':
        ev.preventDefault()
        setHighlightIdx(prev => Math.max(prev - 1, 0))
        break
      case 'Enter':
        ev.preventDefault()
        if (highlightIdx >= 0 && highlightIdx < suggestions.length) {
          navigate(`/entity/${suggestions[highlightIdx].slug}`)
          setShowDropdown(false)
        }
        break
      case 'Escape':
        setShowDropdown(false)
        break
    }
  }, [showDropdown, suggestions, highlightIdx, navigate])

  const handleSearchChange = (ev: React.ChangeEvent<HTMLInputElement>) => {
    const val = ev.target.value
    onFiltersChange({ ...filters, search: val })
    setShowDropdown(val.trim().length >= 2)
    setHighlightIdx(-1)
  }

  const clearSearch = () => {
    onFiltersChange({ ...filters, search: '' })
    setShowDropdown(false)
    inputRef.current?.focus()
  }

  const toggleFilter = (key: 'eras' | 'labels' | 'continents' | 'frameworks', value: string) => {
    const current = filters[key]
    const next = current.includes(value)
      ? current.filter(v => v !== value)
      : [...current, value]
    onFiltersChange({ ...filters, [key]: next })
  }

  const clearAllFilters = () => {
    onFiltersChange({ search: '', eras: [], labels: [], continents: [], frameworks: [] })
    setShowFilters(false)
  }

  return (
    <Box mb={5}>
      {/* Search bar row */}
      <Flex gap={3} direction={{ base: 'column', md: 'row' }} align={{ md: 'center' }}>
        <Box position="relative" flex={1} maxW={{ md: '560px' }}>
          <Box position="absolute" left={3} top="50%" transform="translateY(-50%)" zIndex={2}>
            <Search size={16} color={MUTED} />
          </Box>
          <Input
            ref={inputRef}
            pl={10}
            pr={filters.search ? 10 : 4}
            value={filters.search}
            onChange={handleSearchChange}
            onFocus={() => { if (filters.search.trim().length >= 2) setShowDropdown(true) }}
            onKeyDown={handleKeyDown}
            placeholder="Search actors by name, call number, subject, era..."
            bg={CARD_BG}
            border="1px solid"
            borderColor={showDropdown && suggestions.length > 0 ? GOLD : BORDER}
            borderRadius="8px"
            fontSize="sm"
            fontFamily="'Inter', sans-serif"
            _focus={{ borderColor: GOLD, boxShadow: `0 0 0 1px ${GOLD}` }}
            _placeholder={{ color: LIGHT_MUTED }}
          />
          {filters.search && (
            <Box position="absolute" right={3} top="50%" transform="translateY(-50%)" zIndex={2}
              cursor="pointer" onClick={clearSearch} color={MUTED} _hover={{ color: DARK_TEXT }}>
              <X size={14} />
            </Box>
          )}

          {/* Autocomplete Dropdown */}
          {showDropdown && suggestions.length > 0 && (
            <Box ref={dropdownRef}
              position="absolute" top="calc(100% + 4px)" left={0} right={0}
              bg="white" border="1px solid" borderColor={GOLD}
              borderRadius="8px" boxShadow="0 8px 24px rgba(0,0,0,0.12)"
              zIndex={100} maxH="400px" overflowY="auto">
              <Box px={3} py={2} borderBottom="1px solid" borderColor={BORDER}>
                <Text fontSize="10px" fontWeight={700} color={LIGHT_MUTED}
                  fontFamily="'JetBrains Mono', monospace" textTransform="uppercase"
                  letterSpacing="0.05em">
                  {suggestions.length} result{suggestions.length !== 1 ? 's' : ''}
                </Text>
              </Box>
              {suggestions.map((entity, idx) => {
                const color = LABEL_COLORS[entity.label] || MUTED
                const eraColor = ERA_COLORS[entity.eraSlug] || MUTED
                return (
                  <Box
                    key={entity.slug}
                    px={3} py={2.5}
                    cursor="pointer"
                    bg={idx === highlightIdx ? `${GOLD}10` : 'transparent'}
                    _hover={{ bg: `${GOLD}10` }}
                    borderBottom={idx < suggestions.length - 1 ? '1px solid' : 'none'}
                    borderColor={`${BORDER}80`}
                    onClick={() => {
                      navigate(`/entity/${entity.slug}`)
                      setShowDropdown(false)
                    }}
                    onMouseEnter={() => setHighlightIdx(idx)}
                  >
                    <Flex align="center" gap={2}>
                      <Box color={color}>{LABEL_ICONS[entity.label]}</Box>
                      <Text fontFamily="'Cormorant Garamond', serif" fontSize="sm" fontWeight={700}
                        color={DARK_TEXT} flex={1} lineClamp={1}>{entity.name}</Text>
                      <Text fontFamily="'JetBrains Mono', monospace" fontSize="10px" fontWeight={600}
                        color={MUTED}>{entity.callNumber.split('-')[0]}</Text>
                    </Flex>
                    <Flex align="center" gap={2} mt={1}>
                      <Box px={1.5} py={0.5} borderRadius="3px" fontSize="9px" fontWeight={700}
                        fontFamily="'JetBrains Mono', monospace"
                        bg={`${color}12`} color={color}>
                        {entity.label === 'EventWindow' ? 'EVENT' : entity.label.toUpperCase()}
                      </Box>
                      <Box px={1.5} py={0.5} borderRadius="3px" fontSize="9px" fontWeight={600}
                        fontFamily="'JetBrains Mono', monospace"
                        bg={`${eraColor}12`} color={eraColor}>
                        {entity.era}
                      </Box>
                      {entity.continent && (
                        <Text fontSize="9px" color={LIGHT_MUTED}
                          fontFamily="'Inter', sans-serif">{entity.continent}</Text>
                      )}
                    </Flex>
                  </Box>
                )
              })}
              <Box px={3} py={2} borderTop="1px solid" borderColor={BORDER}
                bg={`${GOLD}05`} cursor="pointer"
                _hover={{ bg: `${GOLD}10` }}
                onClick={() => setShowDropdown(false)}>
                <Text fontSize="xs" color={GOLD} fontWeight={600}
                  fontFamily="'Inter', sans-serif" textAlign="center">
                  Press Enter to search all results
                </Text>
              </Box>
            </Box>
          )}
        </Box>

        {/* Filter toggle button */}
        <Box
          as="button"
          onClick={() => setShowFilters(!showFilters)}
          px={4} py={2} borderRadius="8px" fontSize="sm" fontWeight={600}
          fontFamily="'Inter', sans-serif"
          bg={activeFilterCount > 0 ? GOLD : CARD_BG}
          color={activeFilterCount > 0 ? '#fff' : MED_TEXT}
          border="1px solid"
          borderColor={activeFilterCount > 0 ? GOLD : BORDER}
          cursor="pointer"
          display="flex" alignItems="center" gap={2}
          _hover={{ bg: activeFilterCount > 0 ? '#C5963A' : BORDER }}
        >
          {showFilters ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
          Filters
          {activeFilterCount > 0 && (
            <Box bg="white" color={GOLD} borderRadius="full" w="18px" h="18px"
              display="flex" alignItems="center" justifyContent="center" fontSize="10px" fontWeight={800}>
              {activeFilterCount}
            </Box>
          )}
        </Box>

        {/* Clear all */}
        {(activeFilterCount > 0 || filters.search) && (
          <Box as="button" onClick={clearAllFilters}
            px={3} py={2} borderRadius="8px" fontSize="xs" fontWeight={600}
            fontFamily="'Inter', sans-serif" color={MUTED} cursor="pointer"
            _hover={{ color: DARK_TEXT }}>
            Clear all
          </Box>
        )}
      </Flex>

      {/* Filter Panel */}
      {showFilters && (
        <Box mt={3} p={4} bg={CARD_BG} border="1px solid" borderColor={BORDER}
          borderRadius="10px">
          {/* Eras */}
          <Box mb={4}>
            <Text fontSize="10px" fontWeight={700} color={LIGHT_MUTED} mb={2}
              fontFamily="'JetBrains Mono', monospace" textTransform="uppercase"
              letterSpacing="0.05em">Era</Text>
            <Flex gap={2} flexWrap="wrap">
              {Object.entries(ERA_LABELS).map(([slug, label]) => {
                const active = filters.eras.includes(slug)
                const color = ERA_COLORS[slug] || MUTED
                return (
                  <FilterChip key={slug} label={label} active={active} color={color}
                    onClick={() => toggleFilter('eras', slug)} />
                )
              })}
            </Flex>
          </Box>

          {/* Labels / Types */}
          <Box mb={4}>
            <Text fontSize="10px" fontWeight={700} color={LIGHT_MUTED} mb={2}
              fontFamily="'JetBrains Mono', monospace" textTransform="uppercase"
              letterSpacing="0.05em">Type</Text>
            <Flex gap={2} flexWrap="wrap">
              {Object.entries(LABEL_DISPLAY).map(([label, display]) => {
                const active = filters.labels.includes(label)
                const color = LABEL_COLORS[label] || MUTED
                return (
                  <FilterChip key={label} label={display} active={active} color={color}
                    icon={LABEL_ICONS[label]}
                    onClick={() => toggleFilter('labels', label)} />
                )
              })}
            </Flex>
          </Box>

          {/* Continents */}
          <Box mb={4}>
            <Text fontSize="10px" fontWeight={700} color={LIGHT_MUTED} mb={2}
              fontFamily="'JetBrains Mono', monospace" textTransform="uppercase"
              letterSpacing="0.05em">Continent</Text>
            <Flex gap={2} flexWrap="wrap">
              {CONTINENTS.map(c => {
                const active = filters.continents.includes(c)
                return (
                  <FilterChip key={c} label={c} active={active} color="#3B6BC2"
                    onClick={() => toggleFilter('continents', c)} />
                )
              })}
            </Flex>
          </Box>

          {/* Frameworks */}
          <Box>
            <Text fontSize="10px" fontWeight={700} color={LIGHT_MUTED} mb={2}
              fontFamily="'JetBrains Mono', monospace" textTransform="uppercase"
              letterSpacing="0.05em">Framework</Text>
            <Flex gap={2} flexWrap="wrap">
              {FRAMEWORKS.map(f => {
                const active = filters.frameworks.includes(f)
                return (
                  <FilterChip key={f} label={f.replace(/_/g, ' ')} active={active} color={GOLD}
                    onClick={() => toggleFilter('frameworks', f)} />
                )
              })}
            </Flex>
          </Box>
        </Box>
      )}

      {/* Active filter tags */}
      {activeFilterCount > 0 && !showFilters && (
        <Flex gap={2} mt={3} flexWrap="wrap" align="center">
          <Text fontSize="10px" color={LIGHT_MUTED} fontFamily="'JetBrains Mono', monospace">
            ACTIVE:</Text>
          {filters.eras.map(s => (
            <ActiveTag key={s} label={ERA_LABELS[s] || s} color={ERA_COLORS[s] || MUTED}
              onRemove={() => toggleFilter('eras', s)} />
          ))}
          {filters.labels.map(l => (
            <ActiveTag key={l} label={LABEL_DISPLAY[l] || l} color={LABEL_COLORS[l] || MUTED}
              onRemove={() => toggleFilter('labels', l)} />
          ))}
          {filters.continents.map(c => (
            <ActiveTag key={c} label={c} color="#3B6BC2"
              onRemove={() => toggleFilter('continents', c)} />
          ))}
          {filters.frameworks.map(f => (
            <ActiveTag key={f} label={f.replace(/_/g, ' ')} color={GOLD}
              onRemove={() => toggleFilter('frameworks', f)} />
          ))}
        </Flex>
      )}
    </Box>
  )
}

/* ── Filter Chip ── */
function FilterChip({ label, active, color, icon, onClick }: {
  label: string; active: boolean; color: string; icon?: React.ReactNode; onClick: () => void
}) {
  return (
    <Box
      as="button" onClick={onClick}
      px={2.5} py={1} borderRadius="6px" fontSize="xs" fontWeight={600}
      fontFamily="'Inter', sans-serif"
      bg={active ? color : 'white'}
      color={active ? '#fff' : MED_TEXT}
      border="1px solid"
      borderColor={active ? color : BORDER}
      cursor="pointer"
      display="flex" alignItems="center" gap={1.5}
      _hover={{ borderColor: color, bg: active ? color : `${color}08` }}
      transition="all 0.15s"
    >
      {icon} {label}
    </Box>
  )
}

/* ── Active Tag (removable) ── */
function ActiveTag({ label, color, onRemove }: {
  label: string; color: string; onRemove: () => void
}) {
  return (
    <Box display="flex" alignItems="center" gap={1}
      px={2} py={0.5} borderRadius="4px" fontSize="10px" fontWeight={600}
      fontFamily="'JetBrains Mono', monospace"
      bg={`${color}15`} color={color}>
      {label}
      <Box as="button" onClick={onRemove} cursor="pointer" ml={0.5}
        _hover={{ opacity: 0.7 }}>
        <X size={10} />
      </Box>
    </Box>
  )
}

export type { ActiveFilters as SearchFilters }
