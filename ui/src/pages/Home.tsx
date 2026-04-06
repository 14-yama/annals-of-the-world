import React, { useState, useEffect } from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Heading } from '@chakra-ui/react'
import {
  Globe, BookOpen, Clock, Orbit, Users, Scroll, Network, BarChart3,
  Lightbulb, Swords, Brain, MapPin, Library, Landmark, Columns3,
} from 'lucide-react'
import { fetchTotalCount, fetchLabelCounts } from '../services/entityService'

const DEFAULT_HERO_STATS = [
  { value: '199', label: 'Nations Catalogued', icon: Globe },
  { value: '16,505', label: 'Knowledge Nodes', icon: Network },
  { value: '72,000', label: 'Years Chronicled', icon: Clock },
  { value: '6', label: 'Epochs Mapped', icon: Orbit },
]

const WINGS = [
  {
    path: '/continents/africa',
    name: 'Africa Wing',
    subtitle: '55 nations — the cradle of humanity, 30% of the world\'s minerals',
    stat: '319 data points per nation',
    icon: Globe,
    accent: '#8B3A3A',
  },
  {
    path: '/continents/asia',
    name: 'Asia Wing',
    subtitle: '48 nations — 60% of humanity, 180 event windows catalogued',
    stat: 'Prehistory to present',
    icon: Globe,
    accent: '#3B6BC2',
  },
  {
    path: '/continents/europe',
    name: 'Europe Wing',
    subtitle: '44 nations — empires, revolutions, and the Enlightenment',
    stat: 'Classical through contemporary',
    icon: Landmark,
    accent: '#96770B',
  },
  {
    path: '/continents/americas',
    name: 'Americas Wing',
    subtitle: '35 nations — from Mesoamerican empires to modern republics',
    stat: 'Two hemispheres united',
    icon: Columns3,
    accent: '#5A2222',
  },
  {
    path: '/continents/oceania',
    name: 'Oceania Wing',
    subtitle: '14 nations — Pacific navigators and island civilizations',
    stat: 'The last frontier settled',
    icon: MapPin,
    accent: '#23417A',
  },
]

const COLLECTIONS = [
  {
    path: '/explore',
    name: 'Era Explorer',
    desc: 'Navigate through six epochs of human history',
    icon: Clock,
  },
  {
    path: '/ideas',
    name: 'Hall of Ideas',
    desc: '67 transformative ideas that shaped civilization',
    icon: Lightbulb,
  },
  {
    path: '/graph',
    name: 'Knowledge Graph',
    desc: 'Visualize the web of connections between entities',
    icon: Network,
  },
  {
    path: '/weapons',
    name: 'Arms & Warfare',
    desc: '127 weapons catalogued across all eras',
    icon: Swords,
  },
  {
    path: '/case-studies',
    name: 'Frameworks',
    desc: 'Interpretive lenses: cause, diffusion, conflict',
    icon: Orbit,
  },
  {
    path: '/quiz',
    name: 'Examination Hall',
    desc: 'Test your knowledge across eras and regions',
    icon: Brain,
  },
]

export default function Home() {
  const [heroStats, setHeroStats] = useState(DEFAULT_HERO_STATS)

  useEffect(() => {
    let cancelled = false
    async function loadStats() {
      try {
        const [total, counts] = await Promise.all([fetchTotalCount(), fetchLabelCounts()])
        if (cancelled) return
        const peopleCount = counts['Person'] || 0
        setHeroStats([
          { value: '199', label: 'Nations Catalogued', icon: Globe },
          { value: total.toLocaleString(), label: 'Knowledge Nodes', icon: Network },
          { value: peopleCount.toLocaleString(), label: 'Historical Figures', icon: Users },
          { value: '72,000', label: 'Years Chronicled', icon: Clock },
        ])
      } catch { /* keep defaults */ }
    }
    loadStats()
    return () => { cancelled = true }
  }, [])

  return (
    <Box>
      {/* ─── Hero: The Great Hall ─── */}
      <Box
        bg="linear-gradient(135deg, #2D2A24 0%, #3D3930 50%, #2D2A24 100%)"
        borderRadius="xl"
        p={12}
        mb={10}
        position="relative"
        overflow="hidden"
      >
        {/* Decorative column lines */}
        {[0, 1, 2, 3, 4].map((i) => (
          <Box
            key={i}
            position="absolute"
            top={0}
            bottom={0}
            left={`${18 + i * 18}%`}
            w="1px"
            bg="rgba(212,175,55,0.06)"
          />
        ))}

        {/* Corner ornament */}
        <Box
          position="absolute"
          top={6}
          right={6}
          fontFamily='"Cinzel", serif'
          fontSize="80px"
          fontWeight={700}
          color="rgba(212,175,55,0.04)"
          lineHeight={1}
          userSelect="none"
        >
          A
        </Box>

        <Box position="relative" zIndex={1} maxW="700px">
          <Text
            fontFamily='"Cinzel", serif'
            fontSize="11px"
            fontWeight={700}
            color="#D4AF37"
            letterSpacing="0.35em"
            textTransform="uppercase"
            mb={4}
          >
            A Modern Library of Alexandria
          </Text>
          <Text
            fontFamily='"Cinzel", serif'
            fontSize={{ base: '2xl', md: '4xl' }}
            fontWeight={700}
            color="#FAFAF8"
            lineHeight={1.15}
            letterSpacing="0.04em"
          >
            ANNALS OF THE WORLD
          </Text>
          <Box w="60px" h="2px" bg="#D4AF37" mt={4} mb={4} />
          <Text
            fontFamily='"Cormorant Garamond", serif'
            fontSize={{ base: 'md', md: 'lg' }}
            color="#D6D3CC"
            lineHeight={1.7}
          >
            A scholarly knowledge graph spanning all continents, all eras,
            and all civilizations — structured as relationships between entities,
            not stored as documents.
          </Text>
          <Text
            fontFamily='"Cormorant Garamond", serif'
            fontSize="sm"
            color="#9E9A90"
            mt={5}
            fontStyle="italic"
            lineHeight={1.6}
          >
            "The creation of the world happened upon the entrance of the night
            preceding the 23rd day of October, in the year 4004 BC."
          </Text>
          <Text
            fontFamily='"Cinzel", serif'
            fontSize="9px"
            color="#787469"
            mt={1}
            letterSpacing="0.15em"
            textTransform="uppercase"
          >
            James Ussher &middot; Annales Veteris Testamenti &middot; MDCL
          </Text>
        </Box>
      </Box>

      {/* ─── Key Statistics — Marble Tablets ─── */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={10}>
        {heroStats.map((s) => {
          const Icon = s.icon
          return (
            <Box
              key={s.label}
              bg="#FAFAF8"
              border="1px solid"
              borderColor="#E4E2DC"
              borderRadius="lg"
              p={5}
              textAlign="center"
              position="relative"
              overflow="hidden"
              _hover={{ borderColor: '#D4AF37', boxShadow: '0 2px 8px rgba(212,175,55,0.1)' }}
              transition="all 0.2s"
            >
              <Box
                position="absolute"
                top={0}
                left="50%"
                transform="translateX(-50%)"
                w="40px"
                h="2px"
                bg="#D4AF37"
              />
              <Flex justify="center" mb={2} mt={2}>
                <Icon size={20} color="#B8B2A4" />
              </Flex>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="2xl"
                fontWeight={700}
                color="#2D2A24"
                letterSpacing="0.04em"
              >
                {s.value}
              </Text>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="9px"
                color="#9E9A90"
                fontWeight={600}
                letterSpacing="0.15em"
                textTransform="uppercase"
                mt={1}
              >
                {s.label}
              </Text>
            </Box>
          )
        })}
      </SimpleGrid>

      {/* ─── Continental Wings ─── */}
      <Box mb={10}>
        <Flex align="center" gap={3} mb={5}>
          <Box w="40px" h="1px" bg="#D4AF37" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="sm"
            color="#2D2A24"
            letterSpacing="0.2em"
            textTransform="uppercase"
            fontWeight={700}
          >
            Continental Wings
          </Heading>
          <Box flex={1} h="1px" bg="#E4E2DC" />
        </Flex>

        <SimpleGrid columns={{ base: 1, md: 3, lg: 5 }} gap={4}>
          {WINGS.map((w) => {
            const Icon = w.icon
            return (
              <RouterLink
                to={w.path}
                key={w.path}
                style={{ textDecoration: 'none' }}
              >
                <Box
                  bg="#FAFAF8"
                  border="1px solid"
                  borderColor="#E4E2DC"
                  borderRadius="lg"
                  p={5}
                  h="100%"
                  cursor="pointer"
                  transition="all 0.25s"
                  position="relative"
                  overflow="hidden"
                  _hover={{
                    borderColor: w.accent,
                    boxShadow: `0 4px 16px rgba(0,0,0,0.06)`,
                    transform: 'translateY(-2px)',
                  }}
                >
                  {/* Accent top bar */}
                  <Box
                    position="absolute"
                    top={0}
                    left={0}
                    right={0}
                    h="3px"
                    bg={w.accent}
                    opacity={0.7}
                  />
                  <Flex align="center" gap={2} mb={2} mt={1}>
                    <Icon size={16} color={w.accent} />
                    <Text
                      fontFamily='"Cinzel", serif'
                      fontSize="sm"
                      fontWeight={700}
                      color="#2D2A24"
                      letterSpacing="0.06em"
                    >
                      {w.name}
                    </Text>
                  </Flex>
                  <Text fontSize="xs" color="#787469" lineHeight={1.5}>
                    {w.subtitle}
                  </Text>
                  <Text
                    fontFamily='"Cinzel", serif'
                    fontSize="9px"
                    color="#B8B2A4"
                    mt={3}
                    letterSpacing="0.1em"
                    textTransform="uppercase"
                  >
                    {w.stat}
                  </Text>
                </Box>
              </RouterLink>
            )
          })}
        </SimpleGrid>
      </Box>

      {/* ─── Collections & Galleries ─── */}
      <Box mb={10}>
        <Flex align="center" gap={3} mb={5}>
          <Box w="40px" h="1px" bg="#D4AF37" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="sm"
            color="#2D2A24"
            letterSpacing="0.2em"
            textTransform="uppercase"
            fontWeight={700}
          >
            Collections &amp; Galleries
          </Heading>
          <Box flex={1} h="1px" bg="#E4E2DC" />
        </Flex>

        <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4}>
          {COLLECTIONS.map((c) => {
            const Icon = c.icon
            return (
              <RouterLink
                to={c.path}
                key={c.path}
                style={{ textDecoration: 'none' }}
              >
                <Flex
                  bg="#FAFAF8"
                  border="1px solid"
                  borderColor="#E4E2DC"
                  borderRadius="lg"
                  p={5}
                  align="flex-start"
                  gap={4}
                  cursor="pointer"
                  transition="all 0.2s"
                  _hover={{
                    borderColor: '#D4AF37',
                    boxShadow: '0 2px 12px rgba(212,175,55,0.08)',
                  }}
                >
                  <Flex
                    w="40px"
                    h="40px"
                    bg="#F5F4F0"
                    borderRadius="8px"
                    align="center"
                    justify="center"
                    flexShrink={0}
                    border="1px solid #E4E2DC"
                  >
                    <Icon size={18} color="#9E9A90" />
                  </Flex>
                  <Box>
                    <Text
                      fontFamily='"Cinzel", serif'
                      fontSize="sm"
                      fontWeight={700}
                      color="#2D2A24"
                      letterSpacing="0.04em"
                    >
                      {c.name}
                    </Text>
                    <Text fontSize="xs" color="#787469" mt={1} lineHeight={1.5}>
                      {c.desc}
                    </Text>
                  </Box>
                </Flex>
              </RouterLink>
            )
          })}
        </SimpleGrid>
      </Box>

      {/* ─── The Numbers That Astound — Stone Tablet ─── */}
      <Box
        bg="#F5F4F0"
        borderRadius="lg"
        p={8}
        border="1px solid"
        borderColor="#E4E2DC"
        position="relative"
        overflow="hidden"
      >
        {/* Subtle corner inscription */}
        <Box
          position="absolute"
          top={4}
          right={6}
          fontFamily='"Cinzel", serif'
          fontSize="60px"
          fontWeight={700}
          color="rgba(212,175,55,0.04)"
          lineHeight={1}
          userSelect="none"
        >
          §
        </Box>

        <Flex align="center" gap={3} mb={5}>
          <Box w="40px" h="1px" bg="#D4AF37" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="sm"
            color="#2D2A24"
            letterSpacing="0.2em"
            textTransform="uppercase"
            fontWeight={700}
          >
            Inscriptions of Note
          </Heading>
          <Box flex={1} h="1px" bg="#D6D3CC" />
        </Flex>

        <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
          {[
            { stat: '1,029 : 1', desc: 'The wealth gap — Monaco ($242k/capita) to Burundi ($236/capita)' },
            { stat: '84%', desc: 'of African borders are straight lines drawn at the 1884 Berlin Conference' },
            { stat: '14', desc: 'African currencies still controlled by the French Treasury (CFA franc)' },
            { stat: '7 of 55', desc: 'African countries rated "Free" — yet Cabo Verde scores higher than France' },
            { stat: '60%', desc: 'of the world\'s uncultivated arable land is in Africa' },
            { stat: '19.7 yrs', desc: 'Africa\'s median age — youngest continent, growing younger while all others age' },
          ].map((item, i) => (
            <Flex key={i} gap={3} align="flex-start">
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="md"
                fontWeight={700}
                color="#D4AF37"
                minW="80px"
                letterSpacing="0.02em"
              >
                {item.stat}
              </Text>
              <Text fontSize="sm" color="#524E44" lineHeight={1.5}>
                {item.desc}
              </Text>
            </Flex>
          ))}
        </SimpleGrid>
      </Box>
    </Box>
  )
}
