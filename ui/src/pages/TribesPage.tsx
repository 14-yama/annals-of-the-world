/* ─── Tribes & Peoples — Every major tribal group across time and space ─── */
import React, { useState, useMemo } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Input } from '@chakra-ui/react'
import { StatCard } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import {
  Tent, TreePine, Swords, Ship, Wind, Wheat, Crown, Globe,
  Search, ChevronDown, ChevronUp,
} from 'lucide-react'
import { TRIBES, TRIBE_CATEGORIES, ERA_LABELS, type Tribe } from '../data/tribes'

const CATEGORY_ICONS: Record<string, React.ElementType> = {
  nomadic: Tent, indigenous: TreePine, warrior: Swords, maritime: Ship,
  steppe: Wind, agricultural: Wheat, kingdom: Crown, modern: Globe,
}

export default function TribesPage() {
  const [search, setSearch] = useState('')
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [expandedItem, setExpandedItem] = useState<string | null>(null)

  const filtered = useMemo(() => {
    let items = TRIBES
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
    const map = new Map<string, Map<string, Tribe[]>>()
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
    for (const item of TRIBES) {
      byEra[item.era] = (byEra[item.era] || 0) + 1
      byCat[item.category] = (byCat[item.category] || 0) + 1
      civs.add(item.civilization)
    }
    return { total: TRIBES.length, byEra, byCat, civilizations: civs.size }
  }, [])

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Tribes & Peoples' }]} />
      <Box mb={8} textAlign="center" py={8}
        bg="linear-gradient(135deg, #2D2A24 0%, #3A2A1A 40%, #8B6914 70%, #D69E2E 100%)"
        borderRadius="2xl" border="1px solid #8B6914">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }} fontWeight={700}
          color="#FAFAF8" mb={3}>
          Tribes & Peoples of the World
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#E4E2DC" maxW="750px" mx="auto" lineHeight={1.8} mb={3}>
          From the San Bushmen to the Mongol hordes — every tribe,
          confederation, and indigenous nation that shaped human history.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#D69E2E">
          {stats.total} peoples · {stats.civilizations} civilizations · 72,000 years
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
            <Input placeholder="Search tribes, peoples, civilizations..."
              value={search}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearch(e.target.value)}
              pl={9} size="sm" bg="white" border="1px solid #E4E2DC" borderRadius="lg"
              fontFamily='"Inter", sans-serif' fontSize="sm"
              _focus={{ borderColor: '#8B6914', boxShadow: '0 0 0 1px #8B6914' }} />
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
          {TRIBE_CATEGORIES.map(cat => {
            const isActive = selectedCategory === cat.id
            const Icon = CATEGORY_ICONS[cat.id] || Globe
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
          Showing {filtered.length} of {stats.total} tribal peoples
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
              const catInfo = TRIBE_CATEGORIES.find(c => c.id === catId)
              const CatIcon = CATEGORY_ICONS[catId] || Globe
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
                          _hover={{ shadow: 'md', borderColor: '#8B6914' }}>
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
                              bg="#FFF5EB" px={1.5} py={0.5} borderRadius="md" color="#7B341E">{item.origin}</Text>
                          </Flex>
                          {isExpanded && (
                            <Box mt={3} pt={3} borderTop="1px solid #E4E2DC">
                              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44"
                                lineHeight={1.7} mb={3}>{item.description}</Text>
                              <Box bg="#FFF5EB" p={3} borderRadius="lg" border="1px solid #FEEBC8">
                                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                                  color="#7B341E" textTransform="uppercase" mb={1}>Historical Impact</Text>
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
        <Heading fontFamily='"Cinzel", serif' fontSize="xl" color="#D69E2E" mb={4} textAlign="center">
          Turning Points in Tribal History
        </Heading>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
          {[
            { title: 'Out of Africa', period: '~70,000 BCE', detail: 'Small bands of Homo sapiens migrated from Africa, eventually reaching every continent. Every human tribe descends from these original African pioneers.', color: '#6B4D1B' },
            { title: 'The Indo-European Expansion', period: '~3,300 BCE', detail: 'Yamnaya pastoralists spread from the Pontic Steppe into Europe and Asia, seeding the language family spoken by 3 billion people today.', color: '#8B4513' },
            { title: 'The Steppe Masters', period: '~1206 CE', detail: 'From Scythians to Mongols — mounted nomadic tribes repeatedly reshaped Eurasian power politics. Genghis Khan created the largest contiguous land empire.', color: '#A67C2E' },
            { title: 'The Columbian Catastrophe', period: '1492 CE', detail: 'European contact killed 90% of indigenous Americans through disease. Thousands of tribes, languages, and cultures were lost forever.', color: '#C5963A' },
            { title: 'The Scramble for Africa', period: '~1884 CE', detail: 'European powers drew borders through tribal territories, splitting nations and forcing enemies together. The consequences still drive African conflicts.', color: '#4A90D9' },
            { title: 'Indigenous Renaissance', period: '2007 CE', detail: 'The UN Declaration on Indigenous Rights marked a global shift. From Māori to Sámi, tribal peoples are reclaiming languages, lands, and sovereignty.', color: '#6B3FA0' },
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
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: 'lg', md: 'xl' }} color="#D69E2E" mb={3}>
          "A people without the knowledge of their past history,<br />
          origin and culture is like a tree without roots."
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#E4E2DC" mb={2}>— Marcus Garvey</Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" mt={3}>
          {stats.total} tribal peoples documented · {stats.civilizations} civilizations represented · CC0 Public Domain
        </Text>
      </Box>
    </Box>
  )
}
