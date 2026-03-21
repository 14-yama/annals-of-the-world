import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Orbit, Clock, Globe, Zap, ChevronRight } from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'

const ERAS = [
  {
    id: 'prehistory',
    name: 'Prehistory',
    years: '70,000 BCE – 3,500 BCE',
    description: 'The peopling of continents, neolithic transitions, domestication of plants and animals, first settlements.',
    color: '#645E52',
    events: 8,
    regions: ['Asia', 'Africa', 'Europe'],
  },
  {
    id: 'ancient',
    name: 'Ancient World',
    years: '3,500 BCE – 500 CE',
    description: 'Bronze and iron ages, first empires, axial age philosophies, birth of major religions, classical civilizations.',
    color: '#8B3A3A',
    events: 18,
    regions: ['Mesopotamia', 'Egypt', 'Indus Valley', 'China', 'Greece', 'Rome'],
  },
  {
    id: 'medieval',
    name: 'Medieval Period',
    years: '500 – 1500 CE',
    description: 'Silk Road integration, Islamic Golden Age, Mongol empire, maritime trade networks, gunpowder revolution.',
    color: '#96770B',
    events: 24,
    regions: ['Asia', 'Europe', 'Middle East', 'Africa'],
  },
  {
    id: 'early-modern',
    name: 'Early Modern',
    years: '1500 – 1800 CE',
    description: 'European maritime encounters, Reformation, Enlightenment, colonial empires, global silver flows.',
    color: '#D4AF37',
    events: 15,
    regions: ['Europe', 'Americas', 'Asia', 'Africa'],
  },
  {
    id: 'modern',
    name: 'Modern',
    years: '1800 – 1945 CE',
    description: 'Industrial revolution, colonialism at peak, two world wars, nationalist movements, decolonization seeds.',
    color: '#4A90D9',
    events: 20,
    regions: ['Europe', 'Asia', 'Africa', 'Americas', 'Global'],
  },
  {
    id: 'contemporary',
    name: 'Contemporary',
    years: '1945 CE – Present',
    description: 'Decolonization, Cold War, internet revolution, AI adoption, climate crisis, fintech, semiconductor wars.',
    color: '#6B3FA0',
    events: 65,
    regions: ['Global'],
  },
]

const REGIONS = [
  'East Asia', 'South Asia', 'Southeast Asia', 'Central Asia', 'West Asia',
  'North Africa', 'West Africa', 'East Africa', 'Central Africa', 'Southern Africa',
  'Western Europe', 'Eastern Europe', 'Americas', 'Oceania',
]

export default function EraExplorer() {
  const [selectedEra, setSelectedEra] = useState<string | null>(null)
  const [selectedRegion, setSelectedRegion] = useState<string | null>(null)
  const navigate = useNavigate()

  const handleEnterPortal = () => {
    if (selectedEra) {
      navigate(`/explore/${selectedEra}`)
    }
  }

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Eras' }]} />
      {/* Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Orbit size={28} color="#D4AF37" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="3xl"
            fontWeight={700}
            color="#2D2A24"
          >
            Era Explorer
          </Heading>
        </Flex>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#524E44"
          maxW="600px"
        >
          Choose an era and geographic region to enter the temporal portal.
          Travel through time and space to explore the forces that shaped our world.
        </Text>
        <Box h="3px" bg="#D4AF37" w="80px" mt={4} />
      </Box>

      {/* Era Selection */}
      <SectionHeading
        title="Select an Era"
        subtitle="8 epochs spanning 72,000 years of human history"
      />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} gap={4} mb={8}>
        {ERAS.map((era) => (
          <Box
            key={era.id}
            bg={selectedEra === era.id ? era.color : 'white'}
            color={selectedEra === era.id ? 'white' : '#2D2A24'}
            border="1px solid"
            borderColor={selectedEra === era.id ? era.color : '#E4E2DC'}
            borderRadius="lg"
            p={5}
            cursor="pointer"
            transition="all 0.3s"
            onClick={() => setSelectedEra(era.id)}
            _hover={{
              borderColor: era.color,
              transform: 'translateY(-2px)',
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
            }}
          >
            <Flex justify="space-between" align="flex-start" mb={2}>
              <Clock size={18} color={selectedEra === era.id ? 'white' : era.color} />
              <Text
                fontSize="xs"
                fontWeight={700}
                color={selectedEra === era.id ? 'rgba(255,255,255,0.8)' : era.color}
              >
                {era.events} events
              </Text>
            </Flex>
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="md"
              fontWeight={700}
              lineHeight={1.2}
            >
              {era.name}
            </Text>
            <Text
              fontSize="xs"
              mt={1}
              color={selectedEra === era.id ? 'rgba(255,255,255,0.7)' : '#9E9A90'}
            >
              {era.years}
            </Text>
            <Text
              fontSize="xs"
              mt={2}
              lineHeight={1.4}
              color={selectedEra === era.id ? 'rgba(255,255,255,0.9)' : '#524E44'}
            >
              {era.description}
            </Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Region Selection */}
      <SectionHeading
        title="Select a Region"
        subtitle="14 geographic regions across all continents"
      />
      <Flex gap={2} wrap="wrap" mb={8}>
        {REGIONS.map((region) => (
          <Box
            key={region}
            bg={selectedRegion === region ? '#2D2A24' : 'white'}
            color={selectedRegion === region ? '#D4AF37' : '#524E44'}
            border="1px solid"
            borderColor={selectedRegion === region ? '#2D2A24' : '#E4E2DC'}
            borderRadius="full"
            px={4}
            py={2}
            cursor="pointer"
            fontSize="sm"
            fontWeight={selectedRegion === region ? 600 : 400}
            transition="all 0.2s"
            onClick={() => setSelectedRegion(region)}
            _hover={{
              borderColor: '#2D2A24',
              bg: selectedRegion === region ? '#2D2A24' : '#F5F4F0',
            }}
          >
            {region}
          </Box>
        ))}
      </Flex>

      {/* Portal Entry */}
      {selectedEra && (
        <Box textAlign="center" mb={8}>
          <Box
            display="inline-block"
            bg="#2D2A24"
            color="#D4AF37"
            px={8}
            py={4}
            borderRadius="xl"
            cursor="pointer"
            transition="all 0.3s"
            onClick={handleEnterPortal}
            _hover={{
              transform: 'scale(1.05)',
              boxShadow: '0 0 30px rgba(197,150,58,0.3)',
            }}
          >
            <Flex align="center" gap={3}>
              <Orbit size={24} />
              <Box textAlign="left">
                <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700}>
                  Enter the Portal
                </Text>
                <Text fontSize="xs" color="#D6D3CC">
                  {ERAS.find((e) => e.id === selectedEra)?.name}{selectedRegion ? ` · ${selectedRegion}` : ''}
                </Text>
              </Box>
              <ChevronRight size={20} />
            </Flex>
          </Box>
        </Box>
      )}

      {/* Info Card */}
      <Box
        bg="#F5F4F0"
        borderRadius="lg"
        p={6}
        border="1px solid"
        borderColor="#E4E2DC"
      >
        <Text fontSize="sm" color="#524E44" fontWeight={600}>
          How it works
        </Text>
        <Text fontSize="sm" color="#524E44" mt={2} lineHeight={1.6}>
          Select a time period and optionally a region, then enter the portal to explore
          civilizations, timeline events, stock photos, and key facts from that era — drawn
          from our Neo4j knowledge graph of 199 countries and 1,000+ nodes.
        </Text>
      </Box>
    </Box>
  )
}
