import React, { useState, useEffect, useCallback } from 'react'
import { useParams, Link as RouterLink, useNavigate } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import {
  BookOpen, Users, MapPin, FileText, Network, ArrowRight,
  ArrowLeft, Clock, Scroll, Shield, ChevronRight, ChevronLeft, ExternalLink,
  Landmark, Layers, Library, Compass, Zap,
} from 'lucide-react'
import {
  getEntity, getAllEntities, getShelfNeighbors,
  type Entity, type EntityRelationship,
} from '../data/catalog'
import {
  parseCallNumber, getCallNumberBreadcrumbs, getCallNumberColor,
  getDivisionHeading, DIVISIONS,
} from '../constants/callNumbers'

/* ── Era breadcrumb data ── */
const ERAS = [
  { slug: 'prehistoric',   eraId: 'prehistory',    label: 'Prehistoric',   period: 'Before 3000 BCE', color: '#6B4D1B' },
  { slug: 'classical',     eraId: 'ancient',       label: 'Classical',     period: '3000 BCE – 500 CE', color: '#8B4513' },
  { slug: 'medieval',      eraId: 'medieval',      label: 'Medieval',      period: '500 – 1500 CE',   color: '#A67C2E' },
  { slug: 'early-modern',  eraId: 'early-modern',  label: 'Early Modern',  period: '1500 – 1800 CE',  color: '#C5963A' },
  { slug: 'modern',        eraId: 'modern',        label: 'Modern',        period: '1800 – 1945 CE',  color: '#4A90D9' },
  { slug: 'contemporary',  eraId: 'contemporary',  label: 'Contemporary',  period: '1945 – Present',  color: '#6B3FA0' },
]

/* ── Catalog eraSlug → eras.ts route ID mapping ── */
const SLUG_TO_ERA_ID: Record<string, string> = {
  prehistoric: 'prehistory', classical: 'ancient', medieval: 'medieval',
  'early-modern': 'early-modern', modern: 'modern', contemporary: 'contemporary',
}

const TABS = [
  { id: 'overview',  label: 'Overview',          icon: BookOpen },
  { id: 'causes',    label: 'Causes & Effects',  icon: ArrowRight },
  { id: 'people',    label: 'Relationships',     icon: Users },
  { id: 'places',    label: 'Places',            icon: MapPin },
  { id: 'texts',     label: 'Texts',             icon: FileText },
  { id: 'graph',     label: 'Graph',             icon: Network },
]

/* ── Label colors (Golden Markers from Alexandria schema) ── */
const LABEL_COLORS: Record<string, string> = {
  Person: '#3A7D44',
  Idea: '#D4AF37',
  Institution: '#8B3A3A',
  Movement: '#6B3FA0',
  Place: '#3B6BC2',
  EventWindow: '#C5963A',
  Text: '#5A2222',
  Evidence: '#787469',
}

/* ── Relationship direction rendering ── */
function RelationshipRow({ rel, currentSlug }: { rel: EntityRelationship; currentSlug: string }) {
  const isSource = rel.sourceSlug === currentSlug
  const otherSlug = isSource ? rel.targetSlug : rel.sourceSlug
  const otherEntity = getEntity(otherSlug)
  const hasPage = !!otherEntity

  return (
    <Box py={3} borderBottom="1px solid #EEEDEA">
      <Flex align="center" gap={2} flexWrap="wrap">
        {isSource ? (
          <Text fontFamily='"Cinzel", serif' fontSize="12px" fontWeight={600} color="#9E9A90">
            {rel.sourceName}
          </Text>
        ) : hasPage ? (
          <RouterLink to={`/entity/${rel.sourceSlug}`} style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={1}>
              <Text fontFamily='"Inter", sans-serif' fontSize="13px" fontWeight={600} color="#3B6BC2" style={{ cursor: 'pointer' }}>
                {rel.sourceName}
              </Text>
              <ExternalLink size={10} color="#3B6BC2" />
            </Flex>
          </RouterLink>
        ) : (
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">{rel.sourceName}</Text>
        )}

        <Flex align="center" gap={1}>
          <Box w="20px" h="1px" bg="#D4AF37" />
          <Box bg="rgba(212,175,55,0.10)" border="1px solid rgba(212,175,55,0.25)" borderRadius="4px" px={2} py={0.5}>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={600} color="#96770B" letterSpacing="0.05em">
              {rel.verb}
            </Text>
          </Box>
          <Box display="flex" alignItems="center">
            <Box w="12px" h="1px" bg="#D4AF37" />
            <Box w={0} h={0} borderTop="4px solid transparent" borderBottom="4px solid transparent" borderLeft="6px solid #D4AF37" />
          </Box>
        </Flex>

        {!isSource ? (
          <Text fontFamily='"Cinzel", serif' fontSize="12px" fontWeight={600} color="#9E9A90">
            {rel.targetName}
          </Text>
        ) : hasPage ? (
          <RouterLink to={`/entity/${rel.targetSlug}`} style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={1}>
              <Text fontFamily='"Inter", sans-serif' fontSize="13px" fontWeight={600} color="#3B6BC2" style={{ cursor: 'pointer' }}>
                {rel.targetName}
              </Text>
              <ExternalLink size={10} color="#3B6BC2" />
            </Flex>
          </RouterLink>
        ) : (
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">{rel.targetName}</Text>
        )}
      </Flex>
      {rel.context && (
        <Text fontSize="xs" color="#9E9A90" mt={1} ml={1}>{rel.context}</Text>
      )}
    </Box>
  )
}

/* ══════════════════════════════════════════════════════
   Shelf Sidebar — left rail: "On This Shelf"
   Groups neighbors by era for temporal context
   ══════════════════════════════════════════════════════ */
const ERA_ORDER = ['prehistoric', 'classical', 'medieval', 'early-modern', 'modern', 'contemporary']
const ERA_LABELS: Record<string, string> = {
  prehistoric: 'Prehistoric', classical: 'Classical', medieval: 'Medieval',
  'early-modern': 'Early Modern', modern: 'Modern', contemporary: 'Contemporary',
}
const ERA_COLORS: Record<string, string> = {
  prehistoric: '#6B4D1B', classical: '#8B4513', medieval: '#A67C2E',
  'early-modern': '#C5963A', modern: '#4A90D9', contemporary: '#6B3FA0',
}

function ShelfSidebar({ entity, neighbors }: { entity: Entity; neighbors: Entity[] }) {
  const divHeading = getDivisionHeading(entity.callNumber)

  // Group neighbors by era, maintain era order
  const eraGroups = ERA_ORDER
    .map(slug => ({
      slug,
      label: ERA_LABELS[slug] || slug,
      color: ERA_COLORS[slug] || '#787469',
      items: neighbors.filter(n => n.eraSlug === slug),
    }))
    .filter(g => g.items.length > 0)

  return (
    <Box
      w="220px"
      flexShrink={0}
      bg="#FAFAF8"
      border="1px solid #E4E2DC"
      borderRadius="lg"
      p={4}
      position="sticky"
      top="80px"
      maxH="calc(100vh - 100px)"
      overflowY="auto"
      display={{ base: 'none', lg: 'block' }}
      css={{
        '&::-webkit-scrollbar': { width: '3px' },
        '&::-webkit-scrollbar-thumb': { background: '#D6D3CC', borderRadius: '3px' },
      }}
    >
      <Flex align="center" gap={2} mb={3}>
        <Library size={14} color="#96770B" />
        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#96770B"
          letterSpacing="0.15em" textTransform="uppercase" fontWeight={600}>
          On This Shelf
        </Text>
      </Flex>
      {divHeading && (
        <Text fontFamily='"Inter", sans-serif' fontSize="11px" color="#787469" mb={3}>
          {divHeading}
        </Text>
      )}
      {eraGroups.map((group) => (
        <Box key={group.slug} mb={3}>
          {/* Era sub-header */}
          <Flex align="center" gap={1.5} mb={1.5} mt={1}>
            <Box w="8px" h="8px" borderRadius="full" bg={group.color} flexShrink={0} />
            <Text fontFamily='"Inter", sans-serif' fontSize="9px" color={group.color}
              fontWeight={700} textTransform="uppercase" letterSpacing="0.08em">
              {group.label}
            </Text>
            <Box flex={1} h="1px" bg={`${group.color}25`} />
          </Flex>
          {group.items.map((n) => {
            const isCurrent = n.slug === entity.slug
            const color = getCallNumberColor(n.callNumber)
            return (
              <RouterLink key={n.slug} to={`/entity/${n.slug}`} style={{ textDecoration: 'none' }}>
                <Flex
                  align="center" gap={2} py={2} px={2} mb={1} borderRadius="6px"
                  bg={isCurrent ? 'rgba(212,175,55,0.08)' : 'transparent'}
                  borderLeft={isCurrent ? '3px solid #D4AF37' : '3px solid transparent'}
                  _hover={{ bg: 'rgba(212,175,55,0.05)' }}
                  transition="all 0.15s" cursor="pointer"
                >
                  <Box w="6px" h="6px" borderRadius="full" bg={color} flexShrink={0} />
                  <Box flex={1} overflow="hidden">
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4">
                      {n.callNumber.split('-')[0]}
                    </Text>
                    <Text fontFamily='"Inter", sans-serif' fontSize="12px"
                      fontWeight={isCurrent ? 700 : 400}
                      color={isCurrent ? '#2D2A24' : '#524E44'}>
                      {n.name}
                    </Text>
                  </Box>
                </Flex>
              </RouterLink>
            )
          })}
        </Box>
      ))}
    </Box>
  )
}

/* ══════════════════════════════════════════════════════
   Jump Rail — right rail: teleport to related shelves
   ══════════════════════════════════════════════════════ */
function JumpRail({ entity }: { entity: Entity }) {
  const parsed = parseCallNumber(entity.callNumber)
  if (!parsed) return null

  const jumpTargets: { label: string; prefix: string }[] = []
  const seenPrefixes = new Set<string>()

  // Own division
  const ownDiv = DIVISIONS.find(d => d.code === parsed.division)
  if (ownDiv) {
    jumpTargets.push({ label: ownDiv.heading, prefix: parsed.division })
    seenPrefixes.add(parsed.division)
  }

  // Divisions discovered from relationships
  for (const rel of entity.relationships) {
    const otherSlug = rel.sourceSlug === entity.slug ? rel.targetSlug : rel.sourceSlug
    const otherEntity = getEntity(otherSlug)
    if (otherEntity) {
      const otherParsed = parseCallNumber(otherEntity.callNumber)
      if (otherParsed && !seenPrefixes.has(otherParsed.division)) {
        const div = DIVISIONS.find(d => d.code === otherParsed.division)
        if (div) {
          jumpTargets.push({ label: div.heading, prefix: otherParsed.division })
          seenPrefixes.add(otherParsed.division)
        }
      }
    }
  }

  return (
    <Box
      w="180px"
      flexShrink={0}
      bg="#FAFAF8"
      border="1px solid #E4E2DC"
      borderRadius="lg"
      p={4}
      position="sticky"
      top="80px"
      display={{ base: 'none', xl: 'block' }}
    >
      <Flex align="center" gap={2} mb={3}>
        <Zap size={14} color="#D4AF37" />
        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#D4AF37"
          letterSpacing="0.15em" textTransform="uppercase" fontWeight={600}>
          Jump To
        </Text>
      </Flex>
      {jumpTargets.slice(0, 8).map((j, i) => (
        <Box
          key={i}
          as="button"
          display="flex" alignItems="center" gap={2} w="100%"
          py={2} px={2} mb={1} borderRadius="6px" bg="transparent"
          _hover={{ bg: 'rgba(212,175,55,0.06)' }}
          transition="all 0.15s" cursor="pointer" textAlign="left"
        >
          <Compass size={12} color="#B8B2A4" />
          <Box>
            <Text fontFamily='"Inter", sans-serif' fontSize="11px" color="#524E44">{j.label}</Text>
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4">{j.prefix}.</Text>
          </Box>
        </Box>
      ))}

      {/* Call Number Badge */}
      <Box mt={4} pt={3} borderTop="1px solid #EEEDEA">
        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
          letterSpacing="0.1em" textTransform="uppercase" mb={2}>Call Number</Text>
        <Box bg="#F5F4F0" border="1px solid #E4E2DC" borderRadius="6px" p={3}>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="13px" fontWeight={700} color="#2D2A24">
            {entity.callNumber.split('-')[0]}
          </Text>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90" mt={1}>
            {entity.callNumber}
          </Text>
        </Box>
      </Box>
    </Box>
  )
}

/* ══════════════════════════════════════════════════════
   EntityPage — Main Component
   ══════════════════════════════════════════════════════ */
export default function EntityPage() {
  const { slug } = useParams<{ slug: string }>()
  const navigate = useNavigate()
  const [activeTab, setActiveTab] = useState('overview')

  const entitySlug = slug || 'henry_viii'
  const entity = getEntity(entitySlug)
  const neighbors = entity ? getShelfNeighbors(entity.callNumber, 5) : []

  // Keyboard shelf navigation: ← / → within same division
  const handleKeyNav = useCallback((e: KeyboardEvent) => {
    if (!entity || !neighbors.length) return
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return
    const tag = (e.target as HTMLElement).tagName
    if (tag === 'INPUT' || tag === 'TEXTAREA') return
    const idx = neighbors.findIndex(n => n.slug === entity.slug)
    if (idx === -1) return
    const next = e.key === 'ArrowRight' ? idx + 1 : idx - 1
    if (next >= 0 && next < neighbors.length) {
      navigate(`/entity/${neighbors[next].slug}`)
    }
  }, [entity, neighbors, navigate])

  useEffect(() => {
    document.addEventListener('keydown', handleKeyNav)
    return () => document.removeEventListener('keydown', handleKeyNav)
  }, [handleKeyNav])

  if (!entity) {
    return (
      <Box p={10} textAlign="center">
        <Landmark size={48} color="#D6D3CC" style={{ margin: '0 auto 16px' }} />
        <Text fontFamily='"Cinzel", serif' fontSize="xl" color="#2D2A24" mb={2}>Entity Not Found</Text>
        <Text fontSize="sm" color="#9E9A90">No record for &ldquo;{entitySlug}&rdquo;.</Text>
        <RouterLink to="/" style={{ color: '#3B6BC2', fontSize: '14px', marginTop: '16px', display: 'inline-block' }}>
          Return to The Great Hall
        </RouterLink>
      </Box>
    )
  }

  const currentEra = ERAS.find((e) => e.slug === entity.eraSlug)
  const crumbs = getCallNumberBreadcrumbs(entity.callNumber)
  const cnColor = getCallNumberColor(entity.callNumber)

  return (
    <Box>
      {/* ─── Call Number Breadcrumbs (clickable → catalog) ─── */}
      <Flex bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" mb={3}
        align="center" px={3} py={2} flexWrap="wrap">
        <RouterLink to="/catalog" style={{ display: 'flex', alignItems: 'center', textDecoration: 'none' }}>
          <Compass size={14} color="#B8B2A4" style={{ marginRight: '8px', flexShrink: 0 }} />
        </RouterLink>
        {crumbs.map((crumb, i) => (
          <React.Fragment key={i}>
            {i > 0 && <ChevronRight size={12} color="#D6D3CC" style={{ margin: '0 4px' }} />}
            <RouterLink to={`/catalog?class=${crumb.prefix}`} style={{ textDecoration: 'none' }}>
              <Flex align="center" gap={1} _hover={{ color: '#D4AF37' }} cursor="pointer">
                <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#787469" letterSpacing="0.08em"
                  _hover={{ color: '#D4AF37' }}>
                  {crumb.label}
                </Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4">
                  ({crumb.prefix})
                </Text>
              </Flex>
            </RouterLink>
          </React.Fragment>
        ))}
        <ChevronRight size={12} color="#D6D3CC" style={{ margin: '0 4px' }} />
        <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#2D2A24" fontWeight={600} letterSpacing="0.08em">
          {entity.name}
        </Text>
      </Flex>

      {/* ─── Era Breadcrumb Bar ─── */}
      <Flex bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="hidden" mb={4}
        align="center" px={2}>
        <Layers size={14} color="#B8B2A4" style={{ marginRight: '8px', flexShrink: 0 }} />
        {ERAS.map((era) => {
          const isActive = era.slug === entity.eraSlug
          return (
            <RouterLink key={era.slug} to={`/explore/${era.eraId}`} style={{
              display: 'flex', alignItems: 'center', gap: '4px',
              padding: '10px 12px', fontSize: '10px', fontFamily: '"Cinzel", serif',
              fontWeight: isActive ? 700 : 400,
              color: isActive ? era.color : '#B8B2A4',
              letterSpacing: '0.08em', textTransform: 'uppercase' as const,
              textDecoration: 'none',
              borderBottom: isActive ? `2px solid ${era.color}` : '2px solid transparent',
              transition: 'all 0.2s', whiteSpace: 'nowrap' as const,
            }}>
              {era.label}
            </RouterLink>
          )
        })}
        <Flex align="center" gap={1} ml="auto" flexShrink={0} pr={2}>
          <ChevronRight size={12} color="#D6D3CC" />
          <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#9E9A90" letterSpacing="0.05em">{entity.continent}</Text>
          <ChevronRight size={12} color="#D6D3CC" />
          <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#2D2A24" fontWeight={600} letterSpacing="0.05em">{entity.name}</Text>
        </Flex>
      </Flex>

      {/* ─── Three-Column Layout: Shelf │ Content │ Jump Rail ─── */}
      <Flex gap={4} align="flex-start">
        {/* LEFT: Shelf Navigation */}
        <ShelfSidebar entity={entity} neighbors={neighbors} />

        {/* CENTER: Entity Content */}
        <Box flex={1} minW={0}>
          {/* ─── Entity Header — "Library Card" ─── */}
          <Box bg="#FAFAF8" border="1px solid" borderColor="#E4E2DC" borderRadius="lg"
            p={6} mb={4} position="relative" overflow="hidden">
            <Box position="absolute" top={0} left={0} right={0} h="3px"
              bg={`linear-gradient(90deg, ${cnColor} 0%, transparent 100%)`} />
            <Flex justify="space-between" align="flex-start" flexWrap="wrap" gap={4}>
              <Box>
                <Flex align="center" gap={2} mb={2}>
                  <Box bg="#F5F4F0" border="1px solid #E4E2DC" borderRadius="4px" px={2} py={0.5}>
                    <Text fontFamily='"Cinzel", serif' fontSize="10px"
                      color={LABEL_COLORS[entity.label] || '#9E9A90'}
                      letterSpacing="0.1em" textTransform="uppercase">
                      {entity.label}
                    </Text>
                  </Box>
                  <Box bg="rgba(212,175,55,0.08)" border="1px solid rgba(212,175,55,0.20)"
                    borderRadius="4px" px={2} py={0.5}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                      color="#96770B" fontWeight={600}>
                      {entity.callNumber.split('-')[0]}
                    </Text>
                  </Box>
                </Flex>
                <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700}
                  color="#2D2A24" letterSpacing="0.04em">
                  {entity.name}
                </Text>
                {/* Subject Headings */}
                <Flex gap={2} mt={2} flexWrap="wrap">
                  {entity.subjectHeadings.map((sh) => (
                    <Box key={sh} bg="rgba(212,175,55,0.06)" border="1px solid rgba(212,175,55,0.15)"
                      borderRadius="full" px={3} py={0.5}>
                      <Text fontFamily='"Inter", sans-serif' fontSize="10px" color="#96770B" fontStyle="italic">{sh}</Text>
                    </Box>
                  ))}
                </Flex>
                {/* Subject tags */}
                <Flex gap={2} mt={2} flexWrap="wrap">
                  {entity.subjects.map((s) => (
                    <Box key={s} bg="#F5F4F0" border="1px solid #EEEDEA" borderRadius="full" px={3} py={0.5}>
                      <Text fontFamily='"Inter", sans-serif' fontSize="11px" color="#787469">{s}</Text>
                    </Box>
                  ))}
                </Flex>
              </Box>
              <Flex direction="column" align="flex-end" gap={2}>
                <Flex align="center" gap={2}>
                  <Shield size={14} color="#96770B" />
                  <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#96770B"
                    letterSpacing="0.1em" textTransform="uppercase">
                    {entity.status}
                  </Text>
                </Flex>
                {currentEra && (
                  <RouterLink to={`/explore/${currentEra.eraId}`} style={{ textDecoration: 'none' }}>
                    <Flex align="center" gap={1} bg={`${currentEra.color}10`}
                      border={`1px solid ${currentEra.color}30`} borderRadius="full" px={3} py={1}>
                      <Clock size={11} color={currentEra.color} />
                      <Text fontFamily='"Cinzel", serif' fontSize="10px" color={currentEra.color}
                        fontWeight={600} letterSpacing="0.08em">{currentEra.label}</Text>
                    </Flex>
                  </RouterLink>
                )}
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4" mt={1}>
                  ← → shelf nav
                </Text>
              </Flex>
            </Flex>
          </Box>

          {/* ─── Tab Navigation ─── */}
          <Flex bg="#FAFAF8" border="1px solid" borderColor="#E4E2DC" borderRadius="lg"
            overflow="hidden" mb={4}>
            {TABS.map((tab) => {
              const Icon = tab.icon
              const isActive = activeTab === tab.id
              return (
                <Box key={tab.id} as="button" onClick={() => setActiveTab(tab.id)}
                  flex={1} py={3} px={2}
                  bg={isActive ? 'rgba(212,175,55,0.06)' : 'transparent'}
                  borderBottom="2px solid"
                  borderColor={isActive ? '#D4AF37' : 'transparent'}
                  cursor="pointer" transition="all 0.2s"
                  _hover={{ bg: 'rgba(212,175,55,0.04)' }}
                  display="flex" alignItems="center" justifyContent="center" gap="6px">
                  <Icon size={14} color={isActive ? '#2D2A24' : '#B8B2A4'} />
                  <Text fontFamily='"Cinzel", serif' fontSize="10px"
                    fontWeight={isActive ? 700 : 400}
                    color={isActive ? '#2D2A24' : '#9E9A90'}
                    letterSpacing="0.1em" textTransform="uppercase">
                    {tab.label}
                  </Text>
                </Box>
              )
            })}
          </Flex>

          {/* ─── Tab Content ─── */}
          <Box bg="#FAFAF8" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={6} minH="300px">
            {/* OVERVIEW */}
            {activeTab === 'overview' && (
              <Box>
                <Text fontSize="sm" color="#524E44" lineHeight={1.8} mb={4}>{entity.summary}</Text>
                <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mt={4}>
                  {entity.born && (
                    <Flex gap={3} align="center">
                      <Clock size={14} color="#B8B2A4" />
                      <Box>
                        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Born</Text>
                        <Text fontSize="sm" color="#2D2A24">{entity.born}</Text>
                      </Box>
                    </Flex>
                  )}
                  {entity.died && (
                    <Flex gap={3} align="center">
                      <Clock size={14} color="#B8B2A4" />
                      <Box>
                        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Died</Text>
                        <Text fontSize="sm" color="#2D2A24">{entity.died}</Text>
                      </Box>
                    </Flex>
                  )}
                  {entity.founded && (
                    <Flex gap={3} align="center">
                      <Landmark size={14} color="#B8B2A4" />
                      <Box>
                        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Founded</Text>
                        <Text fontSize="sm" color="#2D2A24">{entity.founded}</Text>
                      </Box>
                    </Flex>
                  )}
                  {entity.period && (
                    <Flex gap={3} align="center">
                      <Clock size={14} color="#B8B2A4" />
                      <Box>
                        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Period</Text>
                        <Text fontSize="sm" color="#2D2A24">{entity.period}</Text>
                      </Box>
                    </Flex>
                  )}
                  {entity.startDate && (
                    <Flex gap={3} align="center">
                      <Clock size={14} color="#B8B2A4" />
                      <Box>
                        <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Dates</Text>
                        <Text fontSize="sm" color="#2D2A24">{entity.startDate} — {entity.endDate}</Text>
                      </Box>
                    </Flex>
                  )}
                  <Flex gap={3} align="center">
                    <Scroll size={14} color="#B8B2A4" />
                    <Box>
                      <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Era</Text>
                      <RouterLink to={`/explore/${SLUG_TO_ERA_ID[entity.eraSlug] || entity.eraSlug}`} style={{ textDecoration: 'none' }}>
                        <Text fontSize="sm" color="#3B6BC2">{entity.era}</Text>
                      </RouterLink>
                    </Box>
                  </Flex>
                  <Flex gap={3} align="center">
                    <MapPin size={14} color="#B8B2A4" />
                    <Box>
                      <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Region</Text>
                      <Text fontSize="sm" color="#2D2A24">{entity.region}</Text>
                    </Box>
                  </Flex>
                </SimpleGrid>

                {/* Connected Entities */}
                {entity.relationships.length > 0 && (
                  <Box mt={6} pt={4} borderTop="1px solid #EEEDEA">
                    <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                      letterSpacing="0.15em" textTransform="uppercase" mb={3}>Connected Entities</Text>
                    <Flex gap={2} flexWrap="wrap">
                      {Array.from(new Set(
                        entity.relationships.map(r =>
                          r.sourceSlug === entitySlug
                            ? JSON.stringify({ slug: r.targetSlug, name: r.targetName })
                            : JSON.stringify({ slug: r.sourceSlug, name: r.sourceName })
                        )
                      )).map((json) => {
                        const { slug: s, name } = JSON.parse(json)
                        const linked = getEntity(s)
                        return linked ? (
                          <RouterLink key={s} to={`/entity/${s}`} style={{ textDecoration: 'none' }}>
                            <Flex align="center" gap={1} bg="#F5F4F0" border="1px solid #E4E2DC"
                              borderRadius="full" px={3} py={1}
                              _hover={{ bg: 'rgba(59,107,194,0.08)', borderColor: '#3B6BC2' }}
                              transition="all 0.2s" cursor="pointer">
                              <Box w="5px" h="5px" borderRadius="full" bg={LABEL_COLORS[linked.label] || '#9E9A90'} />
                              <Text fontSize="12px" color="#3B6BC2" fontWeight={500}>{name}</Text>
                            </Flex>
                          </RouterLink>
                        ) : (
                          <Box key={s} bg="#F5F4F0" border="1px solid #EEEDEA" borderRadius="full" px={3} py={1}>
                            <Text fontSize="12px" color="#787469">{name}</Text>
                          </Box>
                        )
                      })}
                    </Flex>
                  </Box>
                )}
              </Box>
            )}

            {/* CAUSES & EFFECTS */}
            {activeTab === 'causes' && (
              <Box>
                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                  letterSpacing="0.15em" textTransform="uppercase" mb={4}>
                  Causes — What led to this
                </Text>
                {entity.causes.map((c, i) => (
                  <Flex key={i} align="center" gap={4} py={3}
                    borderBottom={i < entity.causes.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                    <ArrowRight size={14} color="#D4AF37" />
                    <Box flex={1}>
                      {c.slug ? (
                        <RouterLink to={`/entity/${c.slug}`} style={{ textDecoration: 'none' }}>
                          <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{c.title}</Text>
                        </RouterLink>
                      ) : (
                        <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{c.title}</Text>
                      )}
                      <Text fontSize="xs" color="#9E9A90">{c.type} &middot; {c.year}</Text>
                    </Box>
                  </Flex>
                ))}

                {entity.effects.length > 0 && (
                  <Box mt={6} pt={4} borderTop="1px solid #EEEDEA">
                    <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                      letterSpacing="0.15em" textTransform="uppercase" mb={4}>
                      Effects — Consequences and results
                    </Text>
                    {entity.effects.map((ef, i) => (
                      <Flex key={i} align="center" gap={4} py={3}
                        borderBottom={i < entity.effects.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                        <ArrowLeft size={14} color="#8B3A3A" />
                        <Box flex={1}>
                          {ef.slug ? (
                            <RouterLink to={`/entity/${ef.slug}`} style={{ textDecoration: 'none' }}>
                              <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{ef.title}</Text>
                            </RouterLink>
                          ) : (
                            <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{ef.title}</Text>
                          )}
                          <Text fontSize="xs" color="#9E9A90">{ef.type} &middot; {ef.year}</Text>
                        </Box>
                      </Flex>
                    ))}
                  </Box>
                )}
              </Box>
            )}

            {/* RELATIONSHIPS */}
            {activeTab === 'people' && (
              <Box>
                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                  letterSpacing="0.15em" textTransform="uppercase" mb={2}>
                  Relationships — directed edges
                </Text>
                <Text fontSize="xs" color="#9E9A90" mb={4}>
                  Each edge reads left-to-right: <strong>Source</strong> → <em>VERB</em> → <strong>Target</strong>. The current entity is shown in gray; linked actors are blue and clickable.
                </Text>
                {entity.relationships.map((rel, i) => (
                  <RelationshipRow key={i} rel={rel} currentSlug={entitySlug} />
                ))}
              </Box>
            )}

            {/* PLACES */}
            {activeTab === 'places' && (
              <Box>
                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                  letterSpacing="0.15em" textTransform="uppercase" mb={4}>Geographic footprint</Text>
                {entity.places.map((p, i) => (
                  <Flex key={i} align="center" gap={4} py={3}
                    borderBottom={i < entity.places.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                    <MapPin size={14} color="#96770B" />
                    <Box flex={1}>
                      {p.slug ? (
                        <RouterLink to={`/entity/${p.slug}`} style={{ textDecoration: 'none' }}>
                          <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{p.name}</Text>
                        </RouterLink>
                      ) : (
                        <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{p.name}</Text>
                      )}
                      <Text fontSize="xs" color="#9E9A90">{p.role}</Text>
                    </Box>
                  </Flex>
                ))}
              </Box>
            )}

            {/* TEXTS */}
            {activeTab === 'texts' && (
              <Box>
                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                  letterSpacing="0.15em" textTransform="uppercase" mb={4}>Documents, treaties, and artifacts</Text>
                {entity.texts.map((t, i) => (
                  <Flex key={i} align="center" gap={4} py={3}
                    borderBottom={i < entity.texts.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                    <FileText size={14} color="#5A2222" />
                    <Box flex={1}>
                      {t.slug ? (
                        <RouterLink to={`/entity/${t.slug}`} style={{ textDecoration: 'none' }}>
                          <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{t.title}</Text>
                        </RouterLink>
                      ) : (
                        <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{t.title}</Text>
                      )}
                      <Text fontSize="xs" color="#9E9A90">{t.type}{t.year ? ` · ${t.year}` : ''}</Text>
                    </Box>
                  </Flex>
                ))}
              </Box>
            )}

            {/* GRAPH */}
            {activeTab === 'graph' && (
              <Flex direction="column" align="center" justify="center" minH="250px" gap={4}>
                <Network size={48} color="#D6D3CC" />
                <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
                  letterSpacing="0.1em" textTransform="uppercase">Knowledge Graph Visualization</Text>
                <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                  The full relationship web — causes, influences, and connections rendered as a force-directed graph. Connect to Neo4j to activate live queries.
                </Text>
              </Flex>
            )}
          </Box>

          {/* ─── Related Entities from Same Era ─── */}
          {(() => {
            const siblings = getAllEntities().filter(
              (e) => e.eraSlug === entity.eraSlug && e.slug !== entity.slug
            )
            if (siblings.length === 0) return null
            return (
              <Box mt={4}>
                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                  letterSpacing="0.15em" textTransform="uppercase" mb={3}>Also in {entity.era}</Text>
                <Flex gap={3} flexWrap="wrap">
                  {siblings.slice(0, 8).map((s) => (
                    <RouterLink key={s.slug} to={`/entity/${s.slug}`} style={{ textDecoration: 'none' }}>
                      <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg"
                        p={4} minW="200px" maxW="260px" cursor="pointer" transition="all 0.2s"
                        _hover={{ borderColor: '#D4AF37', bg: 'rgba(212,175,55,0.03)' }}>
                        <Flex align="center" gap={2} mb={1}>
                          <Box w="6px" h="6px" borderRadius="full" bg={LABEL_COLORS[s.label] || '#9E9A90'} />
                          <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#9E9A90"
                            letterSpacing="0.08em" textTransform="uppercase">{s.label}</Text>
                          <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4" ml="auto">
                            {s.callNumber.split('-')[0]}
                          </Text>
                        </Flex>
                        <Text fontSize="sm" fontWeight={600} color="#2D2A24">{s.name}</Text>
                        <Text fontSize="xs" color="#9E9A90" mt={1} lineClamp={2}>
                          {s.summary.slice(0, 80)}…
                        </Text>
                      </Box>
                    </RouterLink>
                  ))}
                </Flex>
              </Box>
            )
          })()}
        </Box>

        {/* RIGHT: Jump/Teleport Rail */}
        <JumpRail entity={entity} />
      </Flex>
    </Box>
  )
}
