import React, { useState, useEffect, useCallback } from 'react'
import { useParams, Link as RouterLink, useNavigate } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import {
  BookOpen, Users, MapPin, FileText, Network, ArrowRight,
  ArrowLeft, Clock, Scroll, Shield, ChevronRight, ChevronLeft, ExternalLink,
  Landmark, Layers, Library, Compass, Zap, Image, Sparkles,
} from 'lucide-react'
import {
  getEntity, getAllEntities, parseSortYear,
  type Entity, type EntityRelationship,
} from '../data/catalog'
import { fetchEntity, fetchShelfNeighbors } from '../services/entityService'
import {
  parseCallNumber, getCallNumberBreadcrumbs, getCallNumberColor,
  getDivisionHeading, DIVISIONS,
} from '../constants/callNumbers'
import { FRAMEWORK_MAP } from '../constants/frameworks'
import type { Framework } from '../types'
import EntityTimeline from '../components/EntityTimeline'
import EntityGallery from '../components/EntityGallery'
import EntityLegacy from '../components/EntityLegacy'

/* ── Framework contextual analysis generator ── */
function generateFrameworkContext(entity: Entity, fw: Framework): { analysis: string; evidence: string[]; relatedRels: EntityRelationship[] } {
  const name = entity.name
  const label = entity.label
  const subjects = entity.subjects.map(s => s.toLowerCase())
  const summaryLower = (entity.summary || '').toLowerCase()
  const fwId = fw.id as string

  // Find relationships that use verbs from this framework
  const relatedRels = entity.relationships.filter(r =>
    fw.verbs.some(v => r.verb.toUpperCase().includes(v) || v.includes(r.verb.toUpperCase()))
  ).slice(0, 3)

  // Build evidence bullets from entity data
  const evidence: string[] = []

  // Check causes/effects for causal frameworks
  if (fwId === 'CAUSE_AND_EFFECT') {
    if (entity.causes.length > 0) evidence.push(`${entity.causes.length} documented antecedent${entity.causes.length > 1 ? 's' : ''} led to this ${label.toLowerCase()}`)
    if (entity.effects.length > 0) evidence.push(`${entity.effects.length} documented consequence${entity.effects.length > 1 ? 's' : ''} resulted from it`)
  }

  // Check places for geo-related frameworks
  if (fwId === 'GEOPOLITICAL_LINKAGE' || fwId === 'CULTURAL_DIFFUSION' || fwId === 'EMPIRE_AND_COLONIALISM') {
    const placeCount = entity.places.length
    if (placeCount > 1) evidence.push(`Spans ${placeCount} geographic locations, indicating cross-regional influence`)
    const occursIn = entity.relationships.filter(r => r.verb === 'OCCURS_IN')
    if (occursIn.length > 1) evidence.push(`Active across ${occursIn.length} distinct places`)
  }

  // Check texts for textual frameworks
  if (fwId === 'TEXTUAL_TRANSMISSION') {
    if (entity.texts.length > 0) evidence.push(`${entity.texts.length} associated text${entity.texts.length > 1 ? 's' : ''} documenting transmission and preservation`)
  }

  // Check relationships for institutional/political frameworks
  if (['POLITICAL_SYSTEMS', 'LEGAL_INTERPRETATION'].includes(fwId)) {
    const instRels = entity.relationships.filter(r => ['LEADS', 'ADMINISTERS', 'GOVERNS', 'LEGISLATES', 'AFFILIATES_WITH', 'REFORMS'].includes(r.verb))
    if (instRels.length > 0) evidence.push(`${instRels.length} institutional relationship${instRels.length > 1 ? 's' : ''} (${instRels.map(r => r.verb.replace(/_/g, ' ').toLowerCase()).slice(0, 3).join(', ')})`)
  }

  if (fwId === 'CONFLICT_AND_RESOLUTION') {
    const conflictRels = entity.relationships.filter(r => ['CAUSES', 'RESOLVES', 'PARTICIPATES_IN', 'OPPOSES'].includes(r.verb))
    if (conflictRels.length > 0) evidence.push(`${conflictRels.length} conflict-related relationship${conflictRels.length > 1 ? 's' : ''}`)
  }

  if (fwId === 'COMPARATIVE_RELIGION') {
    const relKeywords = ['religion', 'faith', 'doctrine', 'theology', 'church', 'mosque', 'temple', 'prophet', 'scripture', 'worship', 'ritual', 'divine']
    const hits = relKeywords.filter(k => summaryLower.includes(k) || subjects.some(s => s.includes(k)))
    if (hits.length > 0) evidence.push(`Religious dimensions: ${hits.join(', ')}`)
  }

  if (fwId === 'INNOVATION_AND_TECHNOLOGY') {
    const techKeywords = ['invention', 'technology', 'science', 'engineering', 'discovery', 'industrial', 'mechanical', 'innovation']
    const hits = techKeywords.filter(k => summaryLower.includes(k) || subjects.some(s => s.includes(k)))
    if (hits.length > 0) evidence.push(`Technological dimensions: ${hits.join(', ')}`)
  }

  if (fwId === 'ECONOMIC_SYSTEMS') {
    const econKeywords = ['trade', 'commerce', 'economy', 'market', 'currency', 'tax', 'labor', 'guild', 'merchant']
    const hits = econKeywords.filter(k => summaryLower.includes(k) || subjects.some(s => s.includes(k)))
    if (hits.length > 0) evidence.push(`Economic dimensions: ${hits.join(', ')}`)
  }

  if (fwId === 'ENVIRONMENTAL_HISTORY') {
    const envKeywords = ['agriculture', 'climate', 'famine', 'plague', 'ecology', 'irrigation', 'deforestation', 'drought', 'flood', 'crop']
    const hits = envKeywords.filter(k => summaryLower.includes(k) || subjects.some(s => s.includes(k)))
    if (hits.length > 0) evidence.push(`Environmental dimensions: ${hits.join(', ')}`)
  }

  // Add relationship evidence
  if (relatedRels.length > 0) {
    evidence.push(`${relatedRels.length} relationship${relatedRels.length > 1 ? 's' : ''} using framework verbs (${relatedRels.map(r => r.verb).join(', ')})`)
  }

  // Generate the contextual analysis sentence
  const analysis = buildAnalysis(entity, fw)

  return { analysis, evidence, relatedRels }
}

function buildAnalysis(entity: Entity, fw: Framework): string {
  const n = entity.name
  const era = entity.era
  const label = entity.label
  const places = entity.places.map(p => p.name).filter(Boolean)
  const placeStr = places.length > 0 ? places.slice(0, 2).join(' and ') : entity.region || 'its region'

  const templates: Record<string, Record<string, string>> = {
    CAUSE_AND_EFFECT: {
      Person: `${n} is analyzed through cause-and-effect to trace how their actions in ${placeStr} during the ${era} era triggered specific historical outcomes and were themselves shaped by prior developments.`,
      EventWindow: `This event is examined as both a consequence of prior conditions and a catalyst for subsequent developments in ${placeStr} during the ${era} era.`,
      Movement: `${n} is studied as a chain reaction — its emergence was caused by specific historical conditions, and it in turn triggered transformative changes across ${placeStr}.`,
      Idea: `${n} is traced through its causal lineage — what intellectual or social conditions gave rise to it, and what concrete changes it triggered in ${placeStr} and beyond.`,
      Institution: `${n} is examined as both a product of historical forces and an agent of change, analyzing what conditions created it and what outcomes it produced.`,
      Text: `${n} is analyzed for its causal role — what prompted its creation, and how it shaped thought and action in the ${era} era.`,
      Place: `${placeStr} is examined through the lens of cause and effect — what historical forces shaped this place, and what developments originated here.`,
      Evidence: `This evidence is analyzed for the causal claims it supports or challenges about developments in the ${era} era.`,
    },
    CULTURAL_DIFFUSION: {
      Person: `${n} is analyzed as an agent of cultural transmission — carrying, adapting, or introducing practices and ideas across ${placeStr} during the ${era} era.`,
      EventWindow: `This event is studied for how it accelerated or disrupted the spread of cultural practices, technologies, or ideas across regional boundaries.`,
      Movement: `${n} is examined as a vehicle of cultural diffusion — spreading ideas, practices, and institutions from ${placeStr} to new territories and populations.`,
      Idea: `${n} is traced through its routes of transmission — how it spread from its origin in ${placeStr} to other cultures, and how it was adapted along the way.`,
      Institution: `${n} is studied as a channel for cultural exchange — facilitating the spread of practices, knowledge, and traditions across ${placeStr}.`,
      Text: `${n} is examined as a medium of cultural transmission — carrying ideas across linguistic, geographic, and temporal boundaries.`,
      Place: `${placeStr} is analyzed as a crossroads of cultural exchange — a site where diverse traditions met, merged, and were transmitted onward.`,
      Evidence: `This evidence illuminates cultural exchange and the transmission of practices or ideas during the ${era} era.`,
    },
    TEXTUAL_TRANSMISSION: {
      Person: `${n} is analyzed for their role in the copying, translation, editing, or preservation of texts during the ${era} era.`,
      EventWindow: `This event is studied for how it affected the survival, translation, or dissemination of key texts.`,
      Movement: `${n} is examined for how it shaped the preservation, canonization, or destruction of textual traditions.`,
      Idea: `${n} is traced through the texts that carried it — how copying, translation, and editorial choices shaped its transmission across the ${era} era.`,
      Institution: `${n} is studied as a center of textual production, preservation, or dissemination during the ${era} era.`,
      Text: `${n} is analyzed through its transmission history — its copying lineage, translations, editorial revisions, and the institutions that preserved it.`,
      Place: `${placeStr} is examined as a site of textual production or preservation — libraries, scriptoria, or printing centers that shaped the written record.`,
      Evidence: `This evidence documents the transmission, copying, or translation of texts during the ${era} era.`,
    },
    GEOPOLITICAL_LINKAGE: {
      Person: `${n} is analyzed for how their political, diplomatic, or military actions reshaped territorial boundaries and authority structures in ${placeStr} during the ${era} era.`,
      EventWindow: `This event is examined for how it reconfigured political boundaries, diplomatic relationships, or power hierarchies in ${placeStr}.`,
      Movement: `${n} is studied for how it challenged, reinforced, or transformed geopolitical arrangements across ${placeStr} during the ${era} era.`,
      Idea: `${n} is analyzed for how it justified, challenged, or reshaped political authority and territorial claims in ${placeStr}.`,
      Institution: `${n} is examined as an instrument of geopolitical organization — shaping territorial governance and diplomatic relationships in ${placeStr}.`,
      Text: `${n} is analyzed for how it articulated, influenced, or documented geopolitical arrangements and imperial ideology in the ${era} era.`,
      Place: `${placeStr} is examined as a node in geopolitical networks — shaped by imperial, diplomatic, and territorial forces.`,
      Evidence: `This evidence illuminates the geopolitical dynamics and territorial reorganizations of the ${era} era.`,
    },
    CONFLICT_AND_RESOLUTION: {
      Person: `${n} is analyzed through the lens of conflict — their role in wars, schisms, negotiations, or reconciliations that reshaped ${placeStr} during the ${era} era.`,
      EventWindow: `This event is studied as a moment of rupture and resolution — a conflict that transformed social, political, or religious structures.`,
      Movement: `${n} is examined for the conflicts it provoked, mediated, or resolved during the ${era} era.`,
      Idea: `${n} is analyzed for the intellectual or social conflicts it generated or attempted to resolve.`,
      Institution: `${n} is studied for its role in mediating, escalating, or resolving conflicts during the ${era} era.`,
      Text: `${n} is analyzed for how it documented, justified, or attempted to resolve conflicts in the ${era} era.`,
      Place: `${placeStr} is examined as a site of conflict and resolution — battles, treaties, and negotiations that shaped its history.`,
      Evidence: `This evidence documents the dynamics of conflict and resolution during the ${era} era.`,
    },
    DOCTRINE_DEVELOPMENT: {
      Person: `${n} is analyzed for their role in formalizing, systematizing, or reinterpreting doctrines during the ${era} era.`,
      EventWindow: `This event is examined as a moment of doctrinal crystallization — when ideas were formalized into canonical positions.`,
      Movement: `${n} is studied for how it drove doctrinal systematization, canonization, or reformation.`,
      Idea: `${n} is traced through its doctrinal evolution — how it was formalized, debated, and canonized within intellectual or religious traditions.`,
      Institution: `${n} is examined as a body that defined, enforced, or reformed doctrinal standards.`,
      Text: `${n} is analyzed as a vehicle of doctrine — its role in formalizing, transmitting, or challenging canonical positions.`,
      Place: `${placeStr} is examined as a center of doctrinal development — councils, schools, or communities where ideas were canonized.`,
      Evidence: `This evidence documents the development or contestation of doctrines during the ${era} era.`,
    },
    ADAPTATION: {
      Person: `${n} is analyzed for how they reinterpreted or adapted imported practices and ideas to local conditions in ${placeStr}.`,
      EventWindow: `This event is studied as a moment of contextual adaptation — when practices or ideas were reworked to fit new circumstances.`,
      Movement: `${n} is examined for how it adapted to local contexts, transforming imported ideas into distinctly regional expressions.`,
      Idea: `${n} is traced through its local adaptations — how it was reinterpreted, transformed, and reworked in different cultural settings.`,
      Institution: `${n} is studied for how it adapted its structures and practices to the local context of ${placeStr}.`,
      Text: `${n} is analyzed for how it adapted its source material to new audiences, contexts, or cultural expectations.`,
      Place: `${placeStr} is examined as a site of cultural adaptation — where imported ideas were transformed into local expressions.`,
      Evidence: `This evidence documents the adaptation and reinterpretation of traditions in the ${era} era.`,
    },
    TEMPORAL_LINKAGE: {
      _default: `${n} is analyzed through temporal connections — how it relates to events, ideas, or movements across different periods, revealing patterns of continuity and change through the ${era} era.`,
    },
    ECONOMIC_SYSTEMS: {
      _default: `${n} is examined through economic analysis — trade networks, production systems, labor organization, and material flows that shaped ${placeStr} in the ${era} era.`,
    },
    POLITICAL_SYSTEMS: {
      _default: `${n} is analyzed through the lens of governance — sovereignty, statecraft, constitutional development, and the evolution of political authority in ${placeStr} during the ${era} era.`,
    },
    COMPARATIVE_RELIGION: {
      _default: `${n} is examined through comparative religion — analyzing shared patterns and distinctive features across religious traditions in ${placeStr} during the ${era} era.`,
    },
    EMPIRE_AND_COLONIALISM: {
      _default: `${n} is analyzed through imperial and colonial dynamics — expansion, extraction, resistance, and the postcolonial legacies that reshaped ${placeStr} in the ${era} era.`,
    },
    ENVIRONMENTAL_HISTORY: {
      _default: `${n} is examined through environmental history — the interaction between human societies and the natural world in ${placeStr} during the ${era} era.`,
    },
    INNOVATION_AND_TECHNOLOGY: {
      _default: `${n} is analyzed through the lens of innovation — scientific breakthroughs, technological inventions, and their transformative impact on societies in ${placeStr} during the ${era} era.`,
    },
    LEGAL_INTERPRETATION: {
      _default: `${n} is examined through legal analysis — jurisprudential decisions, codification efforts, and administrative rulings that shaped governance in ${placeStr} during the ${era} era.`,
    },
    RITUAL_STANDARDIZATION: {
      _default: `${n} is analyzed through ritual standardization — the formalization and institutional adoption of ceremonial practices across communities in the ${era} era.`,
    },
  }

  const fwTemplates = templates[fw.id as string]
  if (!fwTemplates) return `${n} is analyzed through the ${fw.name} lens during the ${era} era in ${placeStr}.`
  return fwTemplates[label] || fwTemplates._default || `${n} is analyzed through the ${fw.name} lens during the ${era} era in ${placeStr}.`
}

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
  { id: 'overview',    label: 'Overview',        icon: BookOpen },
  { id: 'frameworks',  label: 'Frameworks',      icon: Layers },
  { id: 'people',      label: 'Relationships',   icon: Users },
  { id: 'places',      label: 'Places',          icon: MapPin },
  { id: 'texts',       label: 'Texts',           icon: FileText },
  { id: 'timeline',    label: 'Timeline',        icon: Clock },
  { id: 'evidence',    label: 'Evidence',        icon: Shield },
  { id: 'media',       label: 'Media',           icon: Image },
  { id: 'legacy',      label: 'Legacy',          icon: Sparkles },
  { id: 'graph',       label: 'Graph',           icon: Network },
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
  const parsed = parseCallNumber(entity.callNumber)
  const divHeading = getDivisionHeading(entity.callNumber)
  // Show parent division heading if this is a sub-division (e.g. 581 → parent 580)
  const parentCode = parsed ? parsed.division.slice(0, 2) + '0' : ''
  const isSubDivision = parsed && parentCode !== parsed.division
  const parentDiv = isSubDivision ? DIVISIONS.find(d => d.code === parentCode) : null

  // Group neighbors by era, maintain era order, sort chronologically within each group
  const eraGroups = ERA_ORDER
    .map(slug => ({
      slug,
      label: ERA_LABELS[slug] || slug,
      color: ERA_COLORS[slug] || '#787469',
      items: neighbors
        .filter(n => n.eraSlug === slug)
        .sort((a, b) => parseSortYear(a) - parseSortYear(b)),
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
        <Box mb={3}>
          {parentDiv && (
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4" mb={0.5}>
              {parentDiv.heading}
            </Text>
          )}
          <Text fontFamily='"Inter", sans-serif' fontSize="11px" color="#787469">
            {divHeading}
          </Text>
        </Box>
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
  const navigate = useNavigate()
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
          onClick={() => navigate(`/catalog?division=${j.prefix}`)}
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
  const [entity, setEntity] = useState<Entity | null>(null)
  const [neighbors, setNeighbors] = useState<Entity[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    fetchEntity(entitySlug).then(e => {
      if (cancelled) return
      const ent = e || null
      setEntity(ent)
      setNeighbors(ent ? fetchShelfNeighbors(ent.callNumber, 5) : [])
      setLoading(false)
    })
    return () => { cancelled = true }
  }, [entitySlug])

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

  if (loading) {
    return (
      <Box p={10} textAlign="center">
        <Library size={48} color="#D6D3CC" style={{ margin: '0 auto 16px' }} />
        <Text fontFamily='"Cinzel", serif' fontSize="xl" color="#2D2A24" mb={2}>Loading Entity…</Text>
        <Text fontSize="sm" color="#9E9A90">Fetching record for &ldquo;{entitySlug}&rdquo;</Text>
      </Box>
    )
  }

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
            <RouterLink to={i === 0 ? `/catalog?class=${crumb.prefix}` : `/catalog?class=${crumb.prefix.charAt(0)}&division=${crumb.prefix}`} style={{ textDecoration: 'none' }}>
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

                {/* v2 enrichment: alt names, quote, external links */}
                {entity.altNames && entity.altNames.length > 0 && (
                  <Flex gap={2} flexWrap="wrap" mb={3}>
                    <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                      letterSpacing="0.1em" textTransform="uppercase" alignSelf="center">Also known as</Text>
                    {entity.altNames.map((n, i) => (
                      <Box key={i} bg="#F5F4F0" border="1px solid #E4E2DC" borderRadius="full" px={3} py={0.5}>
                        <Text fontSize="12px" color="#524E44" fontStyle="italic">{n}</Text>
                      </Box>
                    ))}
                  </Flex>
                )}

                {entity.quote && (
                  <Box borderLeft="3px solid #D4AF37" pl={5} mb={4} py={2}>
                    <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" color="#2D2A24"
                      lineHeight="1.6" fontStyle="italic">
                      &ldquo;{entity.quote}&rdquo;
                    </Text>
                    <Text fontSize="xs" color="#9E9A90" mt={1}>— {entity.name}</Text>
                  </Box>
                )}

                {/* External links: Wikidata, Wikipedia */}
                {(entity.wikidataQid || entity.wikipediaUrl || (entity.externalLinks && entity.externalLinks.length > 0)) && (
                  <Flex gap={2} flexWrap="wrap" mb={4}>
                    {entity.wikidataQid && (
                      <a href={`https://www.wikidata.org/wiki/${entity.wikidataQid}`}
                        target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}>
                        <Flex align="center" gap={1} bg="rgba(59,107,194,0.06)" border="1px solid rgba(59,107,194,0.2)"
                          borderRadius="full" px={3} py={1} cursor="pointer" transition="all 0.2s"
                          _hover={{ bg: 'rgba(59,107,194,0.12)' }}>
                          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={600} color="#3B6BC2">
                            {entity.wikidataQid}
                          </Text>
                          <ExternalLink size={10} color="#3B6BC2" />
                        </Flex>
                      </a>
                    )}
                    {entity.wikipediaUrl && (
                      <a href={entity.wikipediaUrl} target="_blank" rel="noopener noreferrer"
                        style={{ textDecoration: 'none' }}>
                        <Flex align="center" gap={1} bg="rgba(59,107,194,0.06)" border="1px solid rgba(59,107,194,0.2)"
                          borderRadius="full" px={3} py={1} cursor="pointer" transition="all 0.2s"
                          _hover={{ bg: 'rgba(59,107,194,0.12)' }}>
                          <Text fontSize="11px" fontWeight={500} color="#3B6BC2">Wikipedia</Text>
                          <ExternalLink size={10} color="#3B6BC2" />
                        </Flex>
                      </a>
                    )}
                    {entity.externalLinks?.map((url, i) => (
                      <a key={i} href={url} target="_blank" rel="noopener noreferrer"
                        style={{ textDecoration: 'none' }}>
                        <Flex align="center" gap={1} bg="#F5F4F0" border="1px solid #E4E2DC"
                          borderRadius="full" px={3} py={1} cursor="pointer" transition="all 0.2s"
                          _hover={{ bg: '#EEEDEA' }}>
                          <Text fontSize="11px" fontWeight={500} color="#524E44">
                            {new URL(url).hostname.replace('www.', '')}
                          </Text>
                          <ExternalLink size={10} color="#9E9A90" />
                        </Flex>
                      </a>
                    ))}
                  </Flex>
                )}

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

            {/* FRAMEWORKS */}
            {activeTab === 'frameworks' && (
              <Box>
                {/* ── Active Frameworks ── */}
                {(entity.frameworks && entity.frameworks.length > 0) ? (
                  <Box mb={6}>
                    <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                      letterSpacing="0.15em" textTransform="uppercase" mb={2}>
                      Historical Analysis — Interpretive Frameworks
                    </Text>
                    <Text fontSize="xs" color="#9E9A90" mb={1}>
                      Each framework below is a scholarly lens used to analyze <Text as="span" fontWeight={600} color="#524E44">{entity.name}</Text>. The analysis explains how this specific actor connects to each interpretive dimension, supported by evidence from its relationships, places, and causal chains.
                    </Text>
                    <Flex align="center" gap={2} mb={4}>
                      <Box w="8px" h="2px" bg="#D4AF37" borderRadius="full" />
                      <Text fontSize="10px" color="#B8B2A4">
                        {entity.frameworks.length} framework{entity.frameworks.length > 1 ? 's' : ''} assigned — {entity.label} · {entity.era} era
                      </Text>
                    </Flex>

                    <Box display="flex" flexDirection="column" gap={4}>
                      {entity.frameworks.map((fwId) => {
                        const fw = FRAMEWORK_MAP[fwId]
                        if (!fw) return (
                          <Box key={fwId} p={4} bg="#FAFAF8" border="1px solid #EEEDEA" borderRadius="lg">
                            <Text fontSize="sm" fontWeight={600} color="#2D2A24">{fwId.replace(/_/g, ' ')}</Text>
                          </Box>
                        )
                        const ctx = generateFrameworkContext(entity, fw)
                        return (
                          <Box key={fwId} bg="#FAFAF8" border="1px solid #EEEDEA" borderRadius="lg"
                            borderLeft="4px solid" borderLeftColor={fw.color} overflow="hidden">
                            {/* Header */}
                            <Box px={5} pt={4} pb={2}>
                              <Flex align="center" gap={2} mb={1}>
                                <Box w="10px" h="10px" borderRadius="full" bg={fw.color} flexShrink={0} />
                                <Text fontSize="md" fontWeight={700} color="#2D2A24" fontFamily='"Cormorant Garamond", serif'>
                                  {fw.name}
                                </Text>
                              </Flex>
                              <Text fontSize="10px" color="#9E9A90" fontStyle="italic" mb={3}>
                                {fw.description}
                              </Text>
                            </Box>

                            {/* Contextual Analysis */}
                            <Box px={5} pb={3}>
                              <Text fontFamily='"Cinzel", serif' fontSize="9px" color={fw.color}
                                letterSpacing="0.12em" textTransform="uppercase" mb={2}>
                                How This Applies to {entity.name}
                              </Text>
                              <Text fontSize="sm" color="#2D2A24" lineHeight={1.7}>
                                {ctx.analysis}
                              </Text>
                            </Box>

                            {/* Evidence Bullets */}
                            {ctx.evidence.length > 0 && (
                              <Box px={5} pb={3}>
                                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                                  letterSpacing="0.12em" textTransform="uppercase" mb={2}>
                                  Supporting Evidence
                                </Text>
                                <Box display="flex" flexDirection="column" gap={1}>
                                  {ctx.evidence.map((ev, i) => (
                                    <Flex key={i} align="flex-start" gap={2}>
                                      <Box mt="6px" w="5px" h="5px" borderRadius="full" bg={fw.color} opacity={0.6} flexShrink={0} />
                                      <Text fontSize="xs" color="#524E44" lineHeight={1.5}>{ev}</Text>
                                    </Flex>
                                  ))}
                                </Box>
                              </Box>
                            )}

                            {/* Related Relationships */}
                            {ctx.relatedRels.length > 0 && (
                              <Box px={5} pb={3}>
                                <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                                  letterSpacing="0.12em" textTransform="uppercase" mb={2}>
                                  Relationships Through This Lens
                                </Text>
                                <Box display="flex" flexDirection="column" gap={1}>
                                  {ctx.relatedRels.map((r, i) => (
                                    <Flex key={i} align="center" gap={2} py={1}>
                                      <ArrowRight size={10} color={fw.color} />
                                      <RouterLink to={`/entity/${r.targetSlug}`} style={{ textDecoration: 'none' }}>
                                        <Text fontSize="xs" color="#3B6BC2" fontWeight={500}>{r.sourceName}</Text>
                                      </RouterLink>
                                      <Box bg={`${fw.color}18`} border={`1px solid ${fw.color}40`} borderRadius="3px" px={1.5} py={0.5}>
                                        <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color={fw.color}>{r.verb}</Text>
                                      </Box>
                                      <RouterLink to={`/entity/${r.targetSlug}`} style={{ textDecoration: 'none' }}>
                                        <Text fontSize="xs" color="#3B6BC2" fontWeight={500}>{r.targetName}</Text>
                                      </RouterLink>
                                    </Flex>
                                  ))}
                                </Box>
                              </Box>
                            )}

                            {/* Framework Verbs Footer */}
                            <Box px={5} pb={4} pt={1} borderTop="1px solid #EEEDEA" mt={1}>
                              <Flex align="center" gap={2} mb={2}>
                                <Text fontSize="9px" color="#B8B2A4" letterSpacing="0.05em" textTransform="uppercase">
                                  Analytical Verbs
                                </Text>
                              </Flex>
                              <Flex gap={1} flexWrap="wrap">
                                {fw.verbs.map((v) => (
                                  <Box key={v} bg={`${fw.color}12`} border={`1px solid ${fw.color}30`}
                                    borderRadius="4px" px={2} py={0.5}>
                                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px"
                                      color={fw.color} letterSpacing="0.05em">{v}</Text>
                                  </Box>
                                ))}
                              </Flex>
                            </Box>
                          </Box>
                        )
                      })}
                    </Box>
                  </Box>
                ) : (
                  <Box mb={6}>
                    <Flex direction="column" align="center" justify="center" minH="100px" gap={2}>
                      <Layers size={24} color="#D6D3CC" />
                      <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                        No interpretive frameworks have been assigned to this actor yet.
                      </Text>
                    </Flex>
                  </Box>
                )}

                {/* ── Causes & Effects Chain ── */}
                {(entity.causes.length > 0 || entity.effects.length > 0) && (
                  <Box mt={2} pt={4} borderTop="1px solid #EEEDEA">
                    <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4"
                      letterSpacing="0.15em" textTransform="uppercase" mb={4}>
                      Causal Chain — Antecedents &amp; Consequences
                    </Text>

                    {entity.causes.length > 0 && (
                      <Box mb={4}>
                        <Text fontSize="xs" fontWeight={600} color="#96770B" mb={2}>
                          What led to this
                        </Text>
                        {entity.causes.map((c, i) => (
                          <Flex key={i} align="flex-start" gap={4} py={3}
                            borderBottom={i < entity.causes.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                            <Box mt="3px" flexShrink={0}><ArrowRight size={14} color="#D4AF37" /></Box>
                            <Box flex={1}>
                              {c.slug ? (
                                <RouterLink to={`/entity/${c.slug}`} style={{ textDecoration: 'none' }}>
                                  <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{c.title}</Text>
                                </RouterLink>
                              ) : (
                                <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{c.title}</Text>
                              )}
                              <Flex gap={2} mt={1} align="center">
                                <Box bg="#F5F4F0" border="1px solid #EEEDEA" borderRadius="full" px={2} py={0.5}>
                                  <Text fontSize="10px" color="#787469">{c.type}</Text>
                                </Box>
                                {c.year && <Text fontSize="xs" color="#9E9A90">{c.year}</Text>}
                              </Flex>
                            </Box>
                          </Flex>
                        ))}
                      </Box>
                    )}

                    {entity.effects.length > 0 && (
                      <Box mt={2} pt={3} borderTop="1px solid #EEEDEA">
                        <Text fontSize="xs" fontWeight={600} color="#8B3A3A" mb={2}>
                          Consequences and results
                        </Text>
                        {entity.effects.map((ef, i) => (
                          <Flex key={i} align="flex-start" gap={4} py={3}
                            borderBottom={i < entity.effects.length - 1 ? '1px solid #EEEDEA' : 'none'}>
                            <Box mt="3px" flexShrink={0}><ArrowLeft size={14} color="#8B3A3A" /></Box>
                            <Box flex={1}>
                              {ef.slug ? (
                                <RouterLink to={`/entity/${ef.slug}`} style={{ textDecoration: 'none' }}>
                                  <Text fontSize="sm" color="#3B6BC2" fontWeight={500}>{ef.title}</Text>
                                </RouterLink>
                              ) : (
                                <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{ef.title}</Text>
                              )}
                              <Flex gap={2} mt={1} align="center">
                                <Box bg="#F5F4F0" border="1px solid #EEEDEA" borderRadius="full" px={2} py={0.5}>
                                  <Text fontSize="10px" color="#787469">{ef.type}</Text>
                                </Box>
                                {ef.year && <Text fontSize="xs" color="#9E9A90">{ef.year}</Text>}
                              </Flex>
                            </Box>
                          </Flex>
                        ))}
                      </Box>
                    )}
                  </Box>
                )}
              </Box>
            )}

            {/* RELATIONSHIPS */}
            {activeTab === 'people' && (
              <Box>
                {entity.relationships.length === 0 ? (
                  <Flex direction="column" align="center" justify="center" minH="200px" gap={3}>
                    <Users size={36} color="#D6D3CC" />
                    <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
                      letterSpacing="0.1em" textTransform="uppercase">No relationships yet</Text>
                    <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                      No directed edges have been documented for this entity. Relationship data will be added in future enrichment batches.
                    </Text>
                  </Flex>
                ) : (
                  <>
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
                  </>
                )}
              </Box>
            )}

            {/* PLACES */}
            {activeTab === 'places' && (
              <Box>
                {entity.places.length === 0 ? (
                  <Flex direction="column" align="center" justify="center" minH="200px" gap={3}>
                    <MapPin size={36} color="#D6D3CC" />
                    <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
                      letterSpacing="0.1em" textTransform="uppercase">No places documented</Text>
                    <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                      Geographic associations for this entity are not yet recorded. Location data will be added in future enrichment batches.
                    </Text>
                  </Flex>
                ) : (
                  <>
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
                  </>
                )}
              </Box>
            )}

            {/* TEXTS */}
            {activeTab === 'texts' && (
              <Box>
                {entity.texts.length === 0 ? (
                  <Flex direction="column" align="center" justify="center" minH="200px" gap={3}>
                    <FileText size={36} color="#D6D3CC" />
                    <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
                      letterSpacing="0.1em" textTransform="uppercase">No texts documented</Text>
                    <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                      Texts, treaties, and artifacts associated with this entity are not yet recorded.
                    </Text>
                  </Flex>
                ) : (
                  <>
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
                  </>
                )}
              </Box>
            )}

            {/* TIMELINE */}
            {activeTab === 'timeline' && (
              <EntityTimeline entity={entity} />
            )}

            {/* EVIDENCE & SOURCES */}
            {activeTab === 'evidence' && (
              <Flex direction="column" align="center" justify="center" minH="250px" gap={4}>
                <Shield size={48} color="#D6D3CC" />
                <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
                  letterSpacing="0.1em" textTransform="uppercase">Evidence &amp; Sources</Text>
                <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
                  Scholarly citations, primary sources, and evidence tiers (A–F) for this entity.
                  Connect to Appwrite to manage evidence records.
                </Text>
              </Flex>
            )}

            {/* MEDIA & GALLERY */}
            {activeTab === 'media' && (
              <EntityGallery entity={entity} />
            )}

            {/* LEGACY & INFLUENCE */}
            {activeTab === 'legacy' && (
              <EntityLegacy entity={entity} />
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
