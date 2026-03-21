/* ─── Ideas That Transformed the World ─── */
/* The crown jewel of Annals — demonstrating that IDEAS are the key actor in history. */
import React, { useState, useMemo, useRef, useEffect } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Input } from '@chakra-ui/react'
import { SectionHeading, StatCard, InsightCard } from '../components/DataCards'
import {
  Brain, Lightbulb, Search, ChevronDown, ChevronUp, Network,
  Globe, Clock, Sparkles, ArrowRight, Users, Landmark, BookOpen,
} from 'lucide-react'
import {
  IDEAS, IDEA_DOMAINS, TOTAL_IDEAS, IDEAS_BY_ERA, IDEAS_BY_DOMAIN,
  type HistoricalIdea,
} from '../data/ideas'

/* ─── Era color map ─── */
const ERA_COLORS: Record<string, { bg: string; fg: string; label: string }> = {
  prehistoric:  { bg: '#645E52', fg: '#FFF5EB', label: 'Prehistoric' },
  ancient:      { bg: '#8B3A3A', fg: '#FFF5EB', label: 'Classical / Ancient' },
  medieval:     { bg: '#96770B', fg: '#FFF5EB', label: 'Medieval' },
  earlyModern:  { bg: '#D4AF37', fg: '#2D2A24', label: 'Early Modern' },
  modern:       { bg: '#4A90D9', fg: '#FFFFFF', label: 'Modern (1800–1945)' },
  contemporary: { bg: '#6B3FA0', fg: '#FFFFFF', label: 'Contemporary' },
}

const ERA_ORDER = ['prehistoric', 'ancient', 'medieval', 'earlyModern', 'modern', 'contemporary']

/* ─── Domain color map from data ─── */
const domainColorMap = Object.fromEntries(IDEA_DOMAINS.map(d => [d.id, d.color]))

/* ─── Small Idea Card ─── */
function IdeaCard({ idea, onExpand, isExpanded }: { idea: HistoricalIdea; onExpand: () => void; isExpanded: boolean }) {
  const eraInfo = ERA_COLORS[idea.era] || ERA_COLORS.ancient
  const domainColor = domainColorMap[idea.domain] || '#8B3A3A'

  return (
    <Box
      bg="white" border="1px solid" borderColor={isExpanded ? domainColor : '#E4E2DC'}
      borderRadius="xl" overflow="hidden"
      boxShadow={isExpanded ? `0 4px 20px ${domainColor}20` : '0 1px 3px rgba(44,24,16,0.08)'}
      transition="all 0.3s"
    >
      {/* Header */}
      <Box
        p={4} cursor="pointer" onClick={onExpand}
        _hover={{ bg: '#FDFAF5' }}
      >
        <Flex justify="space-between" align="flex-start">
          <Box flex={1}>
            <Flex align="center" gap={2} mb={1} flexWrap="wrap">
              <Text
                fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={700}
                color={eraInfo.fg} bg={eraInfo.bg} px={2} py={0.5} borderRadius="md"
              >
                {eraInfo.label}
              </Text>
              <Text
                fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={600}
                color={domainColor} bg={`${domainColor}15`} px={2} py={0.5} borderRadius="md"
              >
                {idea.subdomain}
              </Text>
            </Flex>
            <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
              {idea.name}
            </Text>
            <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#9E9A90" mt={0.5}>
              {idea.yearLabel} · {idea.originator}
            </Text>
          </Box>
          <Flex direction="column" align="center" gap={1}>
            {/* Transformative Score */}
            <Box
              w="36px" h="36px" borderRadius="full"
              bg={`linear-gradient(135deg, ${domainColor}, ${domainColor}99)`}
              display="flex" alignItems="center" justifyContent="center"
            >
              <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700} color="white">
                {idea.transformativeScore}
              </Text>
            </Box>
            {isExpanded ? <ChevronUp size={14} color="#9E9A90" /> : <ChevronDown size={14} color="#9E9A90" />}
          </Flex>
        </Flex>
      </Box>

      {/* Expanded Detail */}
      {isExpanded && (
        <Box px={4} pb={4} borderTop="1px solid #F5F4F0">
          <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mt={3}>
            <Box>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={700}
                color="#9E9A90" textTransform="uppercase" mb={1}>
                The Idea
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7}>
                {idea.description}
              </Text>
            </Box>
            <Box>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={700}
                color="#C53030" textTransform="uppercase" mb={1}>
                Why It Matters
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7}>
                {idea.impact}
              </Text>
            </Box>
          </SimpleGrid>

          {/* Provenance */}
          <Box mt={3} p={3} bg="#FAFAF8" borderRadius="lg">
            <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" fontWeight={700}
              color="#2D2A24" textTransform="uppercase" mb={2}>
              Origin & Lineage
            </Text>
            <SimpleGrid columns={{ base: 2, md: 4 }} gap={3}>
              <Box>
                <Text fontSize="10px" color="#9E9A90" fontWeight={600}>ORIGINATOR</Text>
                <Text fontSize="sm" color="#2D2A24" fontWeight={600}>{idea.originator}</Text>
                <Text fontSize="10px" color="#9E9A90">{idea.originatorType}</Text>
              </Box>
              <Box>
                <Text fontSize="10px" color="#9E9A90" fontWeight={600}>ORIGIN PLACE</Text>
                <Text fontSize="sm" color="#2D2A24" fontWeight={600}>{idea.originPlace}</Text>
                <Text fontSize="10px" color="#9E9A90">{idea.region}</Text>
              </Box>
              <Box>
                <Text fontSize="10px" color="#9E9A90" fontWeight={600}>PARENT IDEAS</Text>
                {idea.parentIdeas.length > 0 ? (
                  <Flex gap={1} flexWrap="wrap" mt={0.5}>
                    {idea.parentIdeas.map(p => {
                      const parent = IDEAS.find(i => i.slug === p)
                      return (
                        <Text key={p} fontSize="10px" color={domainColor} bg={`${domainColor}12`}
                          px={1.5} py={0.5} borderRadius="md" fontWeight={600}>
                          {parent?.name || p}
                        </Text>
                      )
                    })}
                  </Flex>
                ) : (
                  <Text fontSize="11px" color="#9E9A90" fontStyle="italic">First Principle</Text>
                )}
              </Box>
              <Box>
                <Text fontSize="10px" color="#9E9A90" fontWeight={600}>CHILD IDEAS</Text>
                {idea.childIdeas.length > 0 ? (
                  <Flex gap={1} flexWrap="wrap" mt={0.5}>
                    {idea.childIdeas.slice(0, 3).map(c => {
                      const child = IDEAS.find(i => i.slug === c)
                      return (
                        <Text key={c} fontSize="10px" color="#4A90D9" bg="#E8F0FE"
                          px={1.5} py={0.5} borderRadius="md" fontWeight={600}>
                          {child?.name || c}
                        </Text>
                      )
                    })}
                    {idea.childIdeas.length > 3 && (
                      <Text fontSize="10px" color="#9E9A90">+{idea.childIdeas.length - 3} more</Text>
                    )}
                  </Flex>
                ) : (
                  <Text fontSize="11px" color="#9E9A90" fontStyle="italic">Frontier Idea</Text>
                )}
              </Box>
            </SimpleGrid>
          </Box>
        </Box>
      )}
    </Box>
  )
}

/* ─── Era Timeline River ─── */
function EraRiver() {
  const grouped = useMemo(() => {
    return ERA_ORDER.map(era => ({
      era,
      info: ERA_COLORS[era],
      ideas: IDEAS.filter(i => i.era === era).sort((a, b) => a.yearOrigin - b.yearOrigin),
    }))
  }, [])

  return (
    <Box>
      {grouped.map(({ era, info, ideas }) => (
        <Box key={era} mb={6}>
          <Flex align="center" gap={3} mb={3}>
            <Box w="40px" h="40px" borderRadius="full" bg={info.bg}
              display="flex" alignItems="center" justifyContent="center">
              <Clock size={18} color={info.fg} />
            </Box>
            <Box>
              <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color={info.bg}>
                {info.label}
              </Text>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#9E9A90">
                {ideas.length} transformative ideas
              </Text>
            </Box>
          </Flex>
          <Flex gap={2} flexWrap="wrap" ml="52px">
            {ideas.map(idea => (
              <Box key={idea.slug} px={3} py={1.5} bg={`${info.bg}15`} borderRadius="lg"
                border="1px solid" borderColor={`${info.bg}30`}>
                <Text fontFamily='"Inter", sans-serif' fontSize="xs" fontWeight={600} color={info.bg}>
                  {idea.name}
                </Text>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">
                  {idea.yearLabel}
                </Text>
              </Box>
            ))}
          </Flex>
        </Box>
      ))}
    </Box>
  )
}

/* ─── Canvas Genealogy Diagram ─── */
function IdeaGenealogy() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const [hoveredIdea, setHoveredIdea] = useState<string | null>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    const container = containerRef.current
    if (!canvas || !container) return

    const width = container.clientWidth
    const height = 600
    canvas.width = width * 2
    canvas.height = height * 2
    canvas.style.width = `${width}px`
    canvas.style.height = `${height}px`

    const ctx = canvas.getContext('2d')
    if (!ctx) return
    ctx.scale(2, 2)
    ctx.clearRect(0, 0, width, height)

    // Position ideas by era (y) and domain (x)
    const domainList = IDEA_DOMAINS.map(d => d.id)
    const positions = new Map<string, { x: number; y: number; color: string }>()

    const eraYMap: Record<string, number> = {
      prehistoric: 50, ancient: 140, medieval: 230,
      earlyModern: 320, modern: 410, contemporary: 500,
    }

    // Track x positions per era to avoid overlap
    const eraXCounter: Record<string, number> = {}
    ERA_ORDER.forEach(e => { eraXCounter[e] = 0 })

    IDEAS.forEach(idea => {
      const domIdx = domainList.indexOf(idea.domain)
      const domainX = domIdx >= 0 ? domIdx : 0
      const baseY = eraYMap[idea.era] || 300
      const eraCount = eraXCounter[idea.era]
      const itemsPerRow = Math.floor((width - 80) / 20)
      const row = Math.floor(eraCount / itemsPerRow)
      const col = eraCount % itemsPerRow
      const x = 40 + col * 20
      const y = baseY + row * 18
      eraXCounter[idea.era]++
      const dColor = domainColorMap[idea.domain] || '#8B3A3A'
      positions.set(idea.slug, { x, y, color: dColor })
    })

    // Draw edges first (light)
    ctx.lineWidth = 0.5
    ctx.globalAlpha = 0.2
    IDEAS.forEach(idea => {
      const from = positions.get(idea.slug)
      if (!from) return
      idea.childIdeas.forEach(childSlug => {
        const to = positions.get(childSlug)
        if (!to) return
        ctx.strokeStyle = from.color
        ctx.beginPath()
        ctx.moveTo(from.x, from.y)
        const midY = (from.y + to.y) / 2
        ctx.bezierCurveTo(from.x, midY, to.x, midY, to.x, to.y)
        ctx.stroke()
      })
    })
    ctx.globalAlpha = 1

    // Draw nodes
    IDEAS.forEach(idea => {
      const pos = positions.get(idea.slug)
      if (!pos) return
      const isHovered = hoveredIdea === idea.slug
      const radius = 3 + idea.transformativeScore * 0.5
      ctx.beginPath()
      ctx.arc(pos.x, pos.y, isHovered ? radius + 2 : radius, 0, Math.PI * 2)
      ctx.fillStyle = pos.color
      ctx.globalAlpha = isHovered ? 1 : 0.7
      ctx.fill()
      ctx.globalAlpha = 1
    })

    // Era labels on the right
    ctx.font = '11px "JetBrains Mono", monospace'
    ctx.textAlign = 'right'
    ERA_ORDER.forEach(era => {
      const y = eraYMap[era]
      const info = ERA_COLORS[era]
      ctx.fillStyle = info.bg
      ctx.fillText(info.label, width - 10, y + 4)
    })
  }, [hoveredIdea])

  return (
    <Box ref={containerRef} w="100%" overflow="hidden" position="relative">
      <canvas ref={canvasRef} style={{ display: 'block' }} />
    </Box>
  )
}

/* ─── Main Page ─── */
export default function IdeasPage() {
  const [search, setSearch] = useState('')
  const [selectedDomain, setSelectedDomain] = useState<string | null>(null)
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [expandedSlug, setExpandedSlug] = useState<string | null>(null)

  const filtered = useMemo(() => {
    return IDEAS.filter(idea => {
      if (selectedDomain && idea.domain !== selectedDomain) return false
      if (selectedEra && idea.era !== selectedEra) return false
      if (search) {
        const q = search.toLowerCase()
        return idea.name.toLowerCase().includes(q) ||
          idea.originator.toLowerCase().includes(q) ||
          idea.description.toLowerCase().includes(q) ||
          idea.originPlace.toLowerCase().includes(q) ||
          idea.domain.toLowerCase().includes(q)
      }
      return true
    })
  }, [search, selectedDomain, selectedEra])

  const score10Ideas = IDEAS.filter(i => i.transformativeScore === 10)
  const originatorTypes = IDEAS.reduce<Record<string, number>>((acc, i) => {
    acc[i.originatorType] = (acc[i.originatorType] || 0) + 1; return acc
  }, {})

  return (
    <Box>
      {/* ─── Hero ─── */}
      <Box mb={10} textAlign="center" py={10}
        bg="linear-gradient(135deg, #6B3FA015 0%, #E8F0FE 30%, #FAFAF8 70%, #FFF5EB 100%)"
        borderRadius="2xl" border="1px solid #E4E2DC" position="relative" overflow="hidden"
      >
        <Box position="absolute" top={0} left={0} right={0} h="3px"
          bg="linear-gradient(90deg, #6B3FA0, #4A90D9, #D4AF37, #2F855A, #C53030)" />
        <Flex justify="center" mb={4}>
          <Box p={3} bg="linear-gradient(135deg, #6B3FA0, #4A90D9)" borderRadius="2xl">
            <Lightbulb size={36} color="white" />
          </Box>
        </Flex>
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }} fontWeight={700}
          color="#2D2A24" mb={3}>
          Ideas That Transformed the World
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#524E44" maxW="750px" mx="auto" lineHeight={1.8} mb={2}>
          People die. Institutions crumble. Events pass.<br />
          But Ideas propagate, mutate, merge, and compound across millennia.
        </Text>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#9E9A90" maxW="600px" mx="auto">
          Every Person is a vessel for Ideas. Every Institution is a structure to propagate Ideas.
          Every Event is a collision of Ideas. Every Movement is an Idea that found legs.
        </Text>
      </Box>

      {/* ─── Why Ideas Are THE Key Actor ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Why Ideas Are the Key Actor"
          subtitle="In the Annals knowledge graph, Ideas outlast every other actor — and they compound"
        />
        <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} gap={4} mt={6}>
          <Box p={5} bg="white" border="1px solid #E4E2DC" borderRadius="xl"
            borderLeft="4px solid #C53030">
            <Flex align="center" gap={2} mb={2}>
              <Users size={18} color="#C53030" />
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                People
              </Text>
            </Flex>
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#C53030" mb={1}>~80 yr</Heading>
            <Text fontSize="xs" color="#524E44" lineHeight={1.6}>
              Alexander: 32 years. Newton: 84 years. Einstein: 76 years.
              People are <strong>mortal vessels</strong> — carriers of ideas who eventually expire.
            </Text>
          </Box>
          <Box p={5} bg="white" border="1px solid #E4E2DC" borderRadius="xl"
            borderLeft="4px solid #DD6B20">
            <Flex align="center" gap={2} mb={2}>
              <Landmark size={18} color="#DD6B20" />
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                Institutions
              </Text>
            </Flex>
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#DD6B20" mb={1}>~500 yr</Heading>
            <Text fontSize="xs" color="#524E44" lineHeight={1.6}>
              Rome: 1,000 years (exceptional). Most empires: 250 years.
              Institutions are <strong>organized structures</strong> that propagate ideas — until they collapse.
            </Text>
          </Box>
          <Box p={5} bg="white" border="1px solid #E4E2DC" borderRadius="xl"
            borderLeft="4px solid #4A90D9">
            <Flex align="center" gap={2} mb={2}>
              <Clock size={18} color="#4A90D9" />
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                Events
              </Text>
            </Flex>
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#4A90D9" mb={1}>~1–50 yr</Heading>
            <Text fontSize="xs" color="#524E44" lineHeight={1.6}>
              Wars end. Treaties are signed. Battles last hours.
              Events are <strong>collisions of ideas</strong> — they pass, but the ideas endure.
            </Text>
          </Box>
          <Box p={5} bg="white" border="1px solid #E4E2DC" borderRadius="xl"
            borderLeft="4px solid #6B3FA0" position="relative" overflow="hidden">
            <Box position="absolute" top={0} left={0} right={0} h="2px"
              bg="linear-gradient(90deg, #6B3FA0, #D4AF37)" />
            <Flex align="center" gap={2} mb={2}>
              <Lightbulb size={18} color="#6B3FA0" />
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color="#2D2A24">
                Ideas
              </Text>
            </Flex>
            <Heading fontFamily='"Cinzel", serif' fontSize="3xl" color="#6B3FA0" mb={1}>∞</Heading>
            <Text fontSize="xs" color="#524E44" lineHeight={1.6}>
              Democracy: 2,500 years. Scientific Method: 400 years. Monotheism: 3,400 years.
              Ideas <strong>never die</strong> — they evolve, merge, and compound forever.
            </Text>
          </Box>
        </SimpleGrid>

        {/* Thesis Statement */}
        <Box mt={6} p={6} bg="#082340" borderRadius="xl" textAlign="center">
          <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'lg', md: '2xl' }} color="#D4AF37" mb={3}>
            Ideas Are the DNA of Civilization
          </Heading>
          <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E8F0FE" lineHeight={1.8} maxW="700px" mx="auto">
            In the Annals knowledge graph, <strong>Idea is the largest node label</strong> — 923 in the backend alone.
            More than People (202), Events (222), or Institutions (160). This is not an accident.
            Every other actor exists to <em>generate, propagate, or collide</em> ideas.
            When you trace any historical transformation to its root, you find an Idea.
          </Text>
          <Flex justify="center" gap={6} mt={4} flexWrap="wrap">
            <StatCard value={String(TOTAL_IDEAS)} label="Ideas Catalogued" detail="With full provenance" color="#6B3FA0" />
            <StatCard value={String(score10Ideas.length)} label="Score 10/10" detail="Civilizational impact" color="#D4AF37" />
            <StatCard value={String(IDEA_DOMAINS.length)} label="Domains" detail="Cross-disciplinary" color="#4A90D9" />
          </Flex>
        </Box>
      </Box>

      {/* ─── Evolution Timeline ─── */}
      <Box mb={10}>
        <SectionHeading
          title="The River of Ideas Across Time"
          subtitle="How ideas flow from era to era — each building on what came before"
        />
        <EraRiver />
      </Box>

      {/* ─── Genealogy Canvas ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Idea Genealogy — The Web of Influence"
          subtitle="Every idea connects to its ancestors and descendants, forming a living genealogy of thought"
        />
        <Box bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl" p={4} overflow="hidden">
          <IdeaGenealogy />
          <Flex justify="center" gap={4} mt={3} flexWrap="wrap">
            {IDEA_DOMAINS.slice(0, 8).map(d => (
              <Flex key={d.id} align="center" gap={1}>
                <Box w="10px" h="10px" borderRadius="full" bg={d.color} />
                <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#9E9A90">
                  {d.label}
                </Text>
              </Flex>
            ))}
          </Flex>
        </Box>
      </Box>

      {/* ─── Domain Distribution ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Ideas by Domain"
          subtitle="The distribution of transformative ideas across fields of human thought"
        />
        <SimpleGrid columns={{ base: 2, md: 3, lg: 5 }} gap={3}>
          {IDEA_DOMAINS.filter(d => IDEAS_BY_DOMAIN[d.id]).map(d => (
            <Box key={d.id} p={4} bg="white" border="1px solid #E4E2DC" borderRadius="xl"
              borderTop="3px solid" borderTopColor={d.color}
              cursor="pointer" onClick={() => setSelectedDomain(selectedDomain === d.id ? null : d.id)}
              opacity={selectedDomain && selectedDomain !== d.id ? 0.5 : 1}
              transition="all 0.2s"
              _hover={{ transform: 'translateY(-2px)', boxShadow: '0 4px 12px rgba(0,0,0,0.08)' }}
            >
              <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color={d.color}>
                {IDEAS_BY_DOMAIN[d.id]}
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" fontWeight={600} color="#2D2A24">
                {d.label}
              </Text>
            </Box>
          ))}
        </SimpleGrid>
      </Box>

      {/* ─── Originator Breakdown ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Who Creates Ideas?"
          subtitle="Ideas emerge from individual geniuses, collective wisdom, institutional programs, and movements"
        />
        <SimpleGrid columns={{ base: 2, md: 5 }} gap={4}>
          {Object.entries(originatorTypes).sort((a, b) => b[1] - a[1]).map(([type, count]) => (
            <StatCard
              key={type}
              value={String(count)}
              label={type}
              detail={
                type === 'Person' ? 'Named individuals' :
                type === 'Collective' ? 'Civilizations & groups' :
                type === 'Institution' ? 'Organizations & labs' :
                type === 'Movement' ? 'Intellectual movements' :
                'Ancient peoples'
              }
              color={
                type === 'Person' ? '#4A90D9' :
                type === 'Collective' ? '#6B3FA0' :
                type === 'Institution' ? '#2F855A' :
                type === 'Movement' ? '#D4AF37' :
                '#8B3A3A'
              }
            />
          ))}
        </SimpleGrid>
      </Box>

      {/* ─── Filterable Ideas Catalog ─── */}
      <Box mb={10}>
        <SectionHeading
          title="Complete Ideas Catalog"
          subtitle={`${TOTAL_IDEAS} ideas with full provenance — search, filter, and explore`}
        />

        {/* Search & Filters */}
        <Flex gap={3} mb={4} flexWrap="wrap" align="center">
          <Box position="relative" flex={1} minW="200px">
            <Box position="absolute" left={3} top="50%" transform="translateY(-50%)" zIndex={1}>
              <Search size={16} color="#9E9A90" />
            </Box>
            <Input
              placeholder="Search ideas, people, places..."
              value={search}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearch(e.target.value)}
              pl={10}
              bg="white" border="1px solid #E4E2DC" borderRadius="lg"
              fontFamily='"Inter", sans-serif' fontSize="sm"
              _placeholder={{ color: '#D6D3CC' }}
            />
          </Box>

          {/* Era filter toggles */}
          {ERA_ORDER.map(era => {
            const info = ERA_COLORS[era]
            const active = selectedEra === era
            return (
              <Box
                key={era} px={3} py={1.5} borderRadius="lg" cursor="pointer"
                bg={active ? info.bg : 'white'}
                color={active ? info.fg : info.bg}
                border="1px solid" borderColor={info.bg}
                fontSize="xs" fontWeight={600} fontFamily='"JetBrains Mono", monospace'
                onClick={() => setSelectedEra(active ? null : era)}
                transition="all 0.2s"
              >
                {info.label}
              </Box>
            )
          })}
        </Flex>

        {/* Clear filters hint */}
        {(search || selectedDomain || selectedEra) && (
          <Flex mb={3} align="center" gap={2}>
            <Text fontSize="xs" color="#9E9A90">
              Showing {filtered.length} of {TOTAL_IDEAS} ideas
            </Text>
            <Text fontSize="xs" color="#4A90D9" cursor="pointer" fontWeight={600}
              onClick={() => { setSearch(''); setSelectedDomain(null); setSelectedEra(null) }}>
              Clear all filters
            </Text>
          </Flex>
        )}

        {/* Ideas list */}
        <SimpleGrid columns={{ base: 1, lg: 2 }} gap={3}>
          {filtered.map(idea => (
            <IdeaCard
              key={idea.slug}
              idea={idea}
              isExpanded={expandedSlug === idea.slug}
              onExpand={() => setExpandedSlug(expandedSlug === idea.slug ? null : idea.slug)}
            />
          ))}
        </SimpleGrid>

        {filtered.length === 0 && (
          <Box textAlign="center" py={10}>
            <Text fontFamily='"Cormorant Garamond", serif' fontSize="xl" color="#9E9A90">
              No ideas match your search
            </Text>
            <Text fontSize="sm" color="#D6D3CC" mt={1}>
              Try adjusting your search terms or clearing filters
            </Text>
          </Box>
        )}
      </Box>

      {/* ─── The Idea Thesis ─── */}
      <Box bg="#082340" borderRadius="2xl" p={8} textAlign="center" mb={8}>
        <Sparkles size={28} color="#D4AF37" style={{ margin: '0 auto 16px' }} />
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'xl', md: '2xl' }} color="#D4AF37" mb={4}>
          "The most powerful force in the universe is not gravity,<br />
          not nuclear fission, not even love — it is an Idea<br />
          whose time has come."
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E8F0FE" mb={4} lineHeight={1.8}
          maxW="650px" mx="auto">
          From the first time a human carved a tally mark on bone, to the machine learning models
          that now predict protein structures — every step is an Idea building on the last.
          Ideas are the true protagonists of human history. Everything else is stage and scenery.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#4A90D9">
          Annals of the World · {TOTAL_IDEAS} Ideas Catalogued · From 2,500,000 BCE to Present
        </Text>
      </Box>
    </Box>
  )
}
