/* ─── Navigation & Exploration — Charting the Unknown Page ─── */
import React, { useState, useMemo } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Input } from '@chakra-ui/react'
import { StatCard } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import {
  Compass, Ship, Route, Map as MapIcon, Flag, Rocket,
  Search, ChevronDown, ChevronUp,
} from 'lucide-react'
import { NAVIGATION, NAVIGATION_CATEGORIES, ERA_LABELS, type Navigation } from '../data/navigation'

const CATEGORY_ICONS: Record<string, React.ElementType> = {
  instruments: Compass, ships: Ship, routes: Route, cartography: MapIcon,
  expeditions: Flag, aerospace: Rocket,
}

export default function NavigationPage() {
  const [search, setSearch] = useState('')
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [expandedItem, setExpandedItem] = useState<string | null>(null)

  const filtered = useMemo(() => {
    let items = NAVIGATION
    if (selectedEra) items = items.filter(x => x.era === selectedEra)
    if (selectedCategory) items = items.filter(x => x.category === selectedCategory)
    if (search.trim()) {
      const q = search.toLowerCase()
      items = items.filter(x =>
        x.name.toLowerCase().includes(q) ||
        x.civilization.toLowerCase().includes(q) ||
        x.subcategory.toLowerCase().includes(q) ||
        x.origin.toLowerCase().includes(q) ||
        x.description.toLowerCase().includes(q)
      )
    }
    return items
  }, [selectedEra, selectedCategory, search])

  const grouped = useMemo(() => {
    const map = new Map<string, Map<string, Navigation[]>>()
    for (const item of filtered) {
      if (!map.has(item.era)) map.set(item.era, new Map())
      const catMap = map.get(item.era)!
      if (!catMap.has(item.category)) catMap.set(item.category, [])
      catMap.get(item.category)!.push(item)
    }
    return map
  }, [filtered])

  const eraOrder = ['prehistoric', 'ancient', 'medieval', 'earlyModern', 'modern', 'contemporary']
  const stats = useMemo(() => {
    const byEra: Record<string, number> = {}
    const byCat: Record<string, number> = {}
    const civs = new Set<string>()
    for (const item of NAVIGATION) {
      byEra[item.era] = (byEra[item.era] || 0) + 1
      byCat[item.category] = (byCat[item.category] || 0) + 1
      civs.add(item.civilization)
    }
    return { total: NAVIGATION.length, byEra, byCat, civilizations: civs.size }
  }, [])

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Navigation & Exploration' }]} />
      <Box mb={8} textAlign="center" py={8}
        bg="linear-gradient(135deg, #082340 0%, #1A365D 40%, #2B6CB0 70%, #3182CE 100%)"
        borderRadius="2xl" border="1px solid #3182CE">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }} fontWeight={700}
          color="#FAFAF8" mb={3}>
          Navigation & Exploration
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#E4E2DC" maxW="750px" mx="auto" lineHeight={1.8} mb={3}>
          From star-guided canoes to Mars rovers — the instruments, ships,
          and voyages that mapped the Earth and reached for the stars.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#90CDF4">
          {stats.total} navigation milestones · {stats.civilizations} civilizations · 10,000 years
        </Text>
      </Box>

      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={3} mb={8}>
        {eraOrder.map(era => {
          const info = ERA_LABELS[era]
          return <StatCard key={era} value={String(stats.byEra[era] || 0)} label={info.label} color={info.color} />
        })}
      </SimpleGrid>

      <Box mb={8} p={5} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="xl">
        <Flex gap={4} flexWrap="wrap" align="center" mb={4}>
          <Box position="relative" flex={1} minW="200px">
            <Box position="absolute" left={3} top="50%" transform="translateY(-50%)" zIndex={1}>
              <Search size={16} color="#9E9A90" />
            </Box>
            <Input placeholder="Search instruments, ships, voyages, routes..."
              value={search}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearch(e.target.value)}
              pl={9} size="sm" bg="white" border="1px solid #E4E2DC" borderRadius="lg"
              fontFamily='"Inter", sans-serif' fontSize="sm"
              _focus={{ borderColor: '#3182CE', boxShadow: '0 0 0 1px #3182CE' }} />
          </Box>
        </Flex>
        <Flex gap={2} flexWrap="wrap" mb={3}>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90"
            textTransform="uppercase" mr={2} lineHeight="28px">Era:</Text>
          {eraOrder.map(era => {
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
        <Flex gap={2} flexWrap="wrap">
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90"
            textTransform="uppercase" mr={2} lineHeight="28px">Type:</Text>
          {NAVIGATION_CATEGORIES.map(cat => {
            const isActive = selectedCategory === cat.id
            const Icon = CATEGORY_ICONS[cat.id] || Compass
            return (
              <Box key={cat.id} as="button" px={3} py={1} borderRadius="full" fontSize="xs"
                fontFamily='"Inter", sans-serif' fontWeight={600} cursor="pointer"
                bg={isActive ? cat.color : 'white'} color={isActive ? 'white' : '#524E44'}
                border="1px solid" borderColor={isActive ? cat.color : '#E4E2DC'}
                onClick={() => setSelectedCategory(isActive ? null : cat.id)}
                _hover={{ bg: isActive ? cat.color : '#FDF8ED' }}>
                <Flex align="center" gap={1}>
                  <Icon size={12} />
                  {cat.label} ({stats.byCat[cat.id] || 0})
                </Flex>
              </Box>
            )
          })}
        </Flex>
      </Box>

      <Flex justify="space-between" align="center" mb={4}>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">
          Showing {filtered.length} of {stats.total} navigation milestones
        </Text>
        {(selectedEra || selectedCategory || search) && (
          <Box as="button" fontSize="xs" fontFamily='"Inter", sans-serif' color="#4A90D9"
            cursor="pointer" onClick={() => { setSelectedEra(null); setSelectedCategory(null); setSearch('') }}
            _hover={{ textDecoration: 'underline' }}>Clear filters</Box>
        )}
      </Flex>

      {eraOrder.filter(era => grouped.has(era)).map(era => {
        const eraInfo = ERA_LABELS[era]
        const catMap = grouped.get(era)!
        return (
          <Box key={era} mb={10}>
            <Box mb={4} pb={2} borderBottom="3px solid" borderColor={eraInfo.color}>
              <Flex align="center" gap={3}>
                <Box w="8px" h="8px" borderRadius="full" bg={eraInfo.color} />
                <Heading fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">{eraInfo.label}</Heading>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90">{eraInfo.period}</Text>
              </Flex>
            </Box>
            {Array.from(catMap.entries()).map(([catId, items]) => {
              const catInfo = NAVIGATION_CATEGORIES.find(c => c.id === catId)
              const CatIcon = CATEGORY_ICONS[catId] || Compass
              return (
                <Box key={catId} mb={6}>
                  <Flex align="center" gap={2} mb={3}>
                    <CatIcon size={16} color={catInfo?.color || '#524E44'} />
                    <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={700}
                      color={catInfo?.color || '#524E44'}>{catInfo?.label || catId}</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">({items.length})</Text>
                  </Flex>
                  <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3}>
                    {items.map(item => {
                      const isExpanded = expandedItem === item.slug
                      return (
                        <Box key={item.slug} p={4} bg="white" border="1px solid #E4E2DC"
                          borderRadius="xl" borderTop="3px solid" borderTopColor={eraInfo.color}
                          cursor="pointer" transition="all 0.15s"
                          onClick={() => setExpandedItem(isExpanded ? null : item.slug)}
                          _hover={{ shadow: 'md', borderColor: '#3182CE' }}>
                          <Flex justify="space-between" align="flex-start" mb={2}>
                            <Box flex={1}>
                              <Text fontFamily='"Cormorant Garamond", serif' fontSize="md"
                                fontWeight={700} color="#2D2A24" lineHeight={1.3}>{item.name}</Text>
                              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                                color="#9E9A90" mt={0.5}>{item.subcategory}</Text>
                            </Box>
                            {isExpanded ? <ChevronUp size={14} color="#9E9A90" /> : <ChevronDown size={14} color="#9E9A90" />}
                          </Flex>
                          <Flex gap={2} flexWrap="wrap" mb={2}>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#FDF8ED" px={1.5} py={0.5} borderRadius="md" color="#524E44">{item.yearIntroduced}</Text>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#E8F0FE" px={1.5} py={0.5} borderRadius="md" color="#082340">{item.civilization}</Text>
                            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                              bg="#EBF8FF" px={1.5} py={0.5} borderRadius="md" color="#2A4365">{item.origin}</Text>
                          </Flex>
                          {isExpanded && (
                            <Box mt={3} pt={3} borderTop="1px solid #E4E2DC">
                              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44"
                                lineHeight={1.7} mb={3}>{item.description}</Text>
                              <Box bg="#EBF8FF" p={3} borderRadius="lg" border="1px solid #BEE3F8">
                                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                                  color="#2B6CB0" textTransform="uppercase" mb={1}>Historical Impact</Text>
                                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#2D2A24"
                                  lineHeight={1.6} fontWeight={500}>{item.impact}</Text>
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

      <Box mb={8} p={6} bg="#082340" borderRadius="2xl">
        <Heading fontFamily='"Cinzel", serif' fontSize="xl" color="#90CDF4" mb={4} textAlign="center">
          The Arc of Human Exploration
        </Heading>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
          {[
            { title: 'Across the Pacific', period: '~3,000 BCE', detail: 'Polynesian navigators crossed 2,500 miles of open ocean using only stars, waves, and birds. The greatest feat of navigation before modern instruments.', color: '#6B4D1B' },
            { title: 'The Silk Road Opens', period: '~130 BCE', detail: 'A 4,000-mile trade network connected China to Rome. Silk, ideas, religions, and diseases traveled along it. The backbone of Eurasian civilization.', color: '#8B4513' },
            { title: 'The Compass Points North', period: '~1040 CE', detail: 'A magnetized needle floating in water changed everything. Reliable ocean navigation became possible in any weather. The most important navigation tool ever invented.', color: '#A67C2E' },
            { title: 'Age of Exploration', period: '1492 CE', detail: 'Columbus crossed the Atlantic. Magellan circled the globe. Da Gama reached India. In 30 years, Europeans connected every continent by sea.', color: '#C5963A' },
            { title: 'The Longitude Problem Solved', period: '1761 CE', detail: 'Harrison\'s chronometer finally allowed sailors to know where they were east-west. The deadliest navigation problem in history, solved by a self-taught clockmaker.', color: '#D69E2E' },
            { title: 'The Wright Brothers', period: '1903 CE', detail: '12 seconds of powered flight at Kitty Hawk. 66 years later, humans walked on the moon. The compression of exploration achievement is staggering.', color: '#4A90D9' },
            { title: 'One Small Step', period: '1969 CE', detail: 'Armstrong and Aldrin walked on the moon with a navigation computer less powerful than a calculator. The greatest exploration achievement in human history.', color: '#3182CE' },
            { title: 'GPS in Every Pocket', period: '1978 CE', detail: '24 satellites provide location accuracy within 3 feet. Every smartphone user is a navigator. The 5,000-year quest to answer "where am I?" is solved.', color: '#6B3FA0' },
            { title: 'Beyond the Solar System', period: '1977 CE', detail: 'Voyager 1 is 15 billion miles from Earth and still transmitting. Carrying a Golden Record message for alien civilizations. Exploration has no end.', color: '#9B2C2C' },
          ].map(m => (
            <Box key={m.title} p={4} bg="rgba(255,255,255,0.05)" borderRadius="lg" borderLeft="3px solid" borderLeftColor={m.color}>
              <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color={m.color} mb={1}>{m.period}</Text>
              <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#FAFAF8" mb={1}>{m.title}</Text>
              <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#B8D4FE" lineHeight={1.6}>{m.detail}</Text>
            </Box>
          ))}
        </SimpleGrid>
      </Box>

      <Box bg="#2D2A24" borderRadius="2xl" p={8} textAlign="center" mb={8}>
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'lg', md: 'xl' }} color="#90CDF4" mb={3}>
          "The real voyage of discovery consists not in seeking<br />
          new landscapes, but in having new eyes."
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E4E2DC" mb={2}>— Marcel Proust</Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" mt={3}>
          {stats.total} navigation milestones documented · {stats.civilizations} civilizations represented · CC0 Public Domain
        </Text>
      </Box>
    </Box>
  )
}
