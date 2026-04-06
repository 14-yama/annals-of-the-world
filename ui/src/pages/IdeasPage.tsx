/* ─── Ideas That Transformed the World ─── */
/* Matches the standard topic page format (WeaponsPage structure). */
import React, { useState, useMemo } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Input } from '@chakra-ui/react'
import { StatCard } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import {
  Brain, Search, ChevronDown, ChevronUp,
} from 'lucide-react'
import {
  IDEAS, IDEA_DOMAINS,
  type HistoricalIdea,
} from '../data/ideas'

/* ─── Era labels matching topic page convention ─── */
const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',             color: '#645E52', period: 'Before 3000 BCE' },
  ancient:      { label: 'Classical / Ancient',     color: '#8B3A3A', period: '3000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',                color: '#96770B', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',            color: '#D4AF37', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',                  color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',            color: '#6B3FA0', period: '1945 – Present' },
}

const ERA_ORDER = ['prehistoric', 'ancient', 'medieval', 'earlyModern', 'modern', 'contemporary']

/* ─── Domain color map from data ─── */
const domainColorMap = Object.fromEntries(IDEA_DOMAINS.map(d => [d.id, d.color]))

export default function IdeasPage() {
  const [search, setSearch] = useState('')
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [selectedDomain, setSelectedDomain] = useState<string | null>(null)
  const [expandedIdea, setExpandedIdea] = useState<string | null>(null)

  const filtered = useMemo(() => {
    let ideas = IDEAS
    if (selectedEra) ideas = ideas.filter(i => i.era === selectedEra)
    if (selectedDomain) ideas = ideas.filter(i => i.domain === selectedDomain)
    if (search.trim()) {
      const q = search.toLowerCase()
      ideas = ideas.filter(i =>
        i.name.toLowerCase().includes(q) ||
        i.originator.toLowerCase().includes(q) ||
        i.originPlace.toLowerCase().includes(q) ||
        i.description.toLowerCase().includes(q) ||
        i.domain.toLowerCase().includes(q)
      )
    }
    return ideas
  }, [selectedEra, selectedDomain, search])

  /* Group by era then domain */
  const grouped = useMemo(() => {
    const map = new Map<string, Map<string, HistoricalIdea[]>>()
    for (const idea of filtered) {
      if (!map.has(idea.era)) map.set(idea.era, new Map())
      const domMap = map.get(idea.era)!
      if (!domMap.has(idea.domain)) domMap.set(idea.domain, [])
      domMap.get(idea.domain)!.push(idea)
    }
    return map
  }, [filtered])

  const stats = useMemo(() => {
    const byEra: Record<string, number> = {}
    const byDomain: Record<string, number> = {}
    const originators = new Set<string>()
    for (const idea of IDEAS) {
      byEra[idea.era] = (byEra[idea.era] || 0) + 1
      byDomain[idea.domain] = (byDomain[idea.domain] || 0) + 1
      originators.add(idea.originator)
    }
    return { total: IDEAS.length, byEra, byDomain, originators: originators.size }
  }, [])

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Ideas & Thought' }]} />

      {/* ─── Hero ─── */}
      <Box mb={8} textAlign="center" py={8}
        bg="linear-gradient(135deg, #2D2A24 0%, #3A2A1A 40%, #6B3FA0 70%, #D4AF37 100%)"
        borderRadius="2xl" border="1px solid #D4AF37">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }} fontWeight={700}
          color="#FAFAF8" mb={3}>
          Ideas That Transformed the World
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#E4E2DC" maxW="750px" mx="auto" lineHeight={1.8} mb={3}>
          People die. Institutions crumble. Events pass.<br />
          But Ideas propagate, mutate, merge, and compound across millennia.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#D4AF37">
          {stats.total} ideas · {stats.originators} originators · 2,500,000 years of thought
        </Text>
      </Box>

      {/* ─── Summary Stats ─── */}
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={3} mb={8}>
        {ERA_ORDER.map(era => {
          const info = ERA_LABELS[era]
          return (
            <StatCard key={era} value={String(stats.byEra[era] || 0)}
              label={info.label} color={info.color} />
          )
        })}
      </SimpleGrid>

      {/* ─── Filters ─── */}
      <Box mb={8} p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
        <Flex gap={4} flexWrap="wrap" align="center" mb={4}>
          <Box position="relative" flex={1} minW="200px">
            <Box position="absolute" left={3} top="50%" transform="translateY(-50%)" zIndex={1}>
              <Search size={16} color="#9E9A90" />
            </Box>
            <Input
              placeholder="Search ideas, originators, places..."
              value={search}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearch(e.target.value)}
              pl={9} size="sm" bg="white" border="1px solid #E4E2DC" borderRadius="lg"
              fontFamily='"Inter", sans-serif' fontSize="sm"
              _focus={{ borderColor: '#D4AF37', boxShadow: '0 0 0 1px #D4AF37' }}
            />
          </Box>
        </Flex>

        {/* Era filter pills */}
        <Flex gap={2} flexWrap="wrap" mb={3}>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90"
            textTransform="uppercase" mr={2} lineHeight="28px">
            Era:
          </Text>
          {ERA_ORDER.map(era => {
            const info = ERA_LABELS[era]
            const isActive = selectedEra === era
            return (
              <Box key={era} as="button" px={3} py={1} borderRadius="full" fontSize="xs"
                fontFamily='"Inter", sans-serif' fontWeight={600} cursor="pointer"
                bg={isActive ? info.color : 'white'} color={isActive ? 'white' : '#524E44'}
                border="1px solid" borderColor={isActive ? info.color : '#E4E2DC'}
                onClick={() => setSelectedEra(isActive ? null : era)}
                _hover={{ bg: isActive ? info.color : '#FDF8ED' }}>
                {info.label} ({stats.byEra[era] || 0})
              </Box>
            )
          })}
        </Flex>

        {/* Domain filter pills */}
        <Flex gap={2} flexWrap="wrap">
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90"
            textTransform="uppercase" mr={2} lineHeight="28px">
            Domain:
          </Text>
          {IDEA_DOMAINS.map(dom => {
            const isActive = selectedDomain === dom.id
            return (
              <Box key={dom.id} as="button" px={3} py={1} borderRadius="full" fontSize="xs"
                fontFamily='"Inter", sans-serif' fontWeight={600} cursor="pointer"
                bg={isActive ? dom.color : 'white'} color={isActive ? 'white' : '#524E44'}
                border="1px solid" borderColor={isActive ? dom.color : '#E4E2DC'}
                onClick={() => setSelectedDomain(isActive ? null : dom.id)}
                _hover={{ bg: isActive ? dom.color : '#FDF8ED' }}>
                <Flex align="center" gap={1}>
                  <Brain size={12} />
                  {dom.label} ({stats.byDomain[dom.id] || 0})
                </Flex>
              </Box>
            )
          })}
        </Flex>
      </Box>

      {/* ─── Results Count ─── */}
      <Flex justify="space-between" align="center" mb={4}>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
          Showing {filtered.length} of {stats.total} ideas
        </Text>
        {(selectedEra || selectedDomain || search) && (
          <Box as="button" fontSize="xs" fontFamily='"Inter", sans-serif' color="#4A90D9"
            cursor="pointer" onClick={() => { setSelectedEra(null); setSelectedDomain(null); setSearch('') }}
            _hover={{ textDecoration: 'underline' }}>
            Clear filters
          </Box>
        )}
      </Flex>

      {/* ─── Grouped Ideas Display ─── */}
      {ERA_ORDER.filter(era => grouped.has(era)).map(era => {
        const eraInfo = ERA_LABELS[era]
        const domMap = grouped.get(era)!

        return (
          <Box key={era} mb={10}>
            {/* Era Header */}
            <Box mb={4} pb={2} borderBottom="3px solid" borderColor={eraInfo.color}>
              <Flex align="center" gap={3}>
                <Box w="8px" h="8px" borderRadius="full" bg={eraInfo.color} />
                <Heading fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
                  {eraInfo.label}
                </Heading>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
                  {eraInfo.period}
                </Text>
              </Flex>
            </Box>

            {Array.from(domMap.entries()).map(([domainId, ideas]) => {
              const domInfo = IDEA_DOMAINS.find(d => d.id === domainId)
              const domColor = domInfo?.color || '#524E44'

              return (
                <Box key={domainId} mb={6}>
                  <Flex align="center" gap={2} mb={3}>
                    <Brain size={16} color={domColor} />
                    <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700} color={domColor}>
                      {domInfo?.label || domainId}
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">
                      ({ideas.length})
                    </Text>
                  </Flex>

                  <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3}>
                    {ideas.map(idea => {
                      const isExpanded = expandedIdea === idea.slug
                      return (
                        <Box key={idea.slug} p={4} bg="white" border="1px solid #E4E2DC"
                          borderRadius="xl" borderTop="3px solid" borderTopColor={eraInfo.color}
                          cursor="pointer" transition="all 0.15s"
                          onClick={() => setExpandedIdea(isExpanded ? null : idea.slug)}
                          _hover={{ shadow: 'md', borderColor: '#D4AF37' }}>
                          {/* Header */}
                          <Flex justify="space-between" align="flex-start" mb={2}>
                            <Box flex={1}>
                              <Text fontFamily='"Cormorant Garamond", serif' fontSize="md"
                                fontWeight={700} color="#2D2A24" lineHeight={1.3}>
                                {idea.name}
                              </Text>
                              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                                color="#9E9A90" mt={0.5}>
                                {idea.subdomain}
                              </Text>
                            </Box>
                            {isExpanded ? <ChevronUp size={14} color="#9E9A90" /> : <ChevronDown size={14} color="#9E9A90" />}
                          </Flex>

                          {/* Quick info */}
                          <Flex gap={2} flexWrap="wrap" mb={2}>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#FDF8ED" px={1.5} py={0.5} borderRadius="md" color="#524E44">
                              {idea.yearLabel}
                            </Text>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#E8F0FE" px={1.5} py={0.5} borderRadius="md" color="#082340">
                              {idea.originator}
                            </Text>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#F0FFF4" px={1.5} py={0.5} borderRadius="md" color="#22543D">
                              {idea.originPlace}
                            </Text>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg={`${domColor}15`} px={1.5} py={0.5} borderRadius="md" color={domColor}>
                              ★ {idea.transformativeScore}/10
                            </Text>
                          </Flex>

                          {/* Expanded details */}
                          {isExpanded && (
                            <Box mt={3} pt={3} borderTop="1px solid #E4E2DC">
                              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44"
                                lineHeight={1.7} mb={3}>
                                {idea.description}
                              </Text>
                              <Box bg="#FDF8ED" p={3} borderRadius="lg" border="1px solid #E4E2DC">
                                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                                  color="#D4AF37" textTransform="uppercase" mb={1}>
                                  Historical Impact
                                </Text>
                                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#2D2A24"
                                  lineHeight={1.6} fontWeight={500}>
                                  {idea.impact}
                                </Text>
                              </Box>
                            </Box>
                          )}
                        </Box>
                      )
                    })}
                  </SimpleGrid>
                </Box>
              )
            })}
          </Box>
        )
      })}

      {/* ─── Timeline of Intellectual Milestones ─── */}
      <Box mb={8} p={6} bg="#082340" borderRadius="2xl">
        <Heading fontFamily='"Cinzel", serif' fontSize="xl" color="#D4AF37" mb={4} textAlign="center">
          The Arc of Human Thought
        </Heading>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
          {[
            { title: 'Language & Symbol', period: '~100,000 BCE', detail: 'Symbolic thought and spoken language gave Homo sapiens the ability to share ideas across generations.', color: '#645E52' },
            { title: 'Writing & Record', period: '~3400 BCE', detail: 'Cuneiform and hieroglyphics turned ephemeral speech into permanent knowledge — civilization could accumulate.', color: '#8B3A3A' },
            { title: 'Greek Rationalism', period: '~500 BCE', detail: 'Philosophy, logic, and democracy: the radical notion that reason, not gods, could explain the world.', color: '#96770B' },
            { title: 'Monotheism', period: '~1350 BCE', detail: 'One God, one moral law. Judaism, Christianity, and Islam built civilizations on this foundation.', color: '#805AD5' },
            { title: 'The Scientific Method', period: '~1620 CE', detail: 'Bacon and Galileo: observe, hypothesize, test, repeat. The most powerful idea engine ever invented.', color: '#D4AF37' },
            { title: 'Enlightenment & Rights', period: '~1689 CE', detail: 'Locke, Voltaire, Paine: natural rights, consent of the governed. The intellectual fuel of revolutions.', color: '#C5963A' },
            { title: 'Evolution by Selection', period: '1859 CE', detail: 'Darwin showed that complexity needs no designer. Biology, medicine, and philosophy were never the same.', color: '#38B2AC' },
            { title: 'Information Theory', period: '1948 CE', detail: 'Shannon quantified information. Computers, the internet, AI — all flow from bits and entropy.', color: '#3182CE' },
            { title: 'Artificial Intelligence', period: '1956 – Present', detail: 'From Turing to LLMs: machines that learn, reason, and create. The latest chapter in the story of ideas.', color: '#6B3FA0' },
          ].map(m => (
            <Box key={m.title} p={4} bg="rgba(255,255,255,0.05)" borderRadius="lg" borderLeft="3px solid" borderLeftColor={m.color}>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color={m.color} mb={1}>
                {m.period}
              </Text>
              <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#FAFAF8" mb={1}>
                {m.title}
              </Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#B8D4FE" lineHeight={1.6}>
                {m.detail}
              </Text>
            </Box>
          ))}
        </SimpleGrid>
      </Box>

      {/* ─── Closing ─── */}
      <Box bg="#2D2A24" borderRadius="2xl" p={8} textAlign="center" mb={8}>
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'lg', md: 'xl' }} color="#D4AF37" mb={3}>
          "An idea that is not dangerous is unworthy of being called an idea at all."
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E4E2DC" mb={2}>
          — Oscar Wilde
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" mt={3}>
          {stats.total} ideas documented · {stats.originators} originators · CC0 Public Domain
        </Text>
      </Box>
    </Box>
  )
}
