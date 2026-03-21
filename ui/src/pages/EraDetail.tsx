import React, { useMemo } from 'react'
import { useParams, Link as RouterLink } from 'react-router-dom'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { Clock, ChevronLeft, Globe, BookOpen, Star } from 'lucide-react'
import { getEraById } from '../constants/eras'
import { TIMELINE_EVENTS } from '../data/timeline-events'
import { SectionHeading } from '../components/DataCards'
import Timeline from '../components/Timeline'
import CivilizationGallery from '../components/CivilizationGallery'

export default function EraDetail() {
  const { eraId } = useParams<{ eraId: string }>()
  const era = eraId ? getEraById(eraId) : undefined

  const eraEvents = useMemo(
    () => TIMELINE_EVENTS.filter(ev => ev.era === eraId),
    [eraId],
  )

  if (!era) {
    return (
      <Box>
        <Flex align="center" gap={2} mb={4}>
          <RouterLink to="/explore" style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#9E9A90', textDecoration: 'none' }}>
            <ChevronLeft size={18} />
            <Text fontSize="sm">Back to Era Explorer</Text>
          </RouterLink>
        </Flex>
        <Heading fontFamily='"Cinzel", serif' fontSize="2xl" color="#2D2A24">Era not found</Heading>
        <Text color="#524E44" mt={2}>The era "{eraId}" does not exist. Return to the Era Explorer to choose a valid era.</Text>
      </Box>
    )
  }

  return (
    <Box>
      {/* Breadcrumb */}
      <Flex align="center" gap={2} mb={6}>
        <RouterLink to="/explore" style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#9E9A90', textDecoration: 'none' }}>
          <ChevronLeft size={18} />
          <Text fontSize="sm" _hover={{ color: '#D4AF37' }}>Era Explorer</Text>
        </RouterLink>
        <Text fontSize="sm" color="#D6D3CC">/</Text>
        <Text fontSize="sm" color={era.color} fontWeight={600}>{era.name}</Text>
      </Flex>

      {/* Hero Section */}
      <Box
        mb={8} borderRadius="xl" overflow="hidden" position="relative"
        h={{ base: '200px', md: '280px' }}
      >
        <img
          src={era.heroImage}
          alt={era.name}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <Box
          position="absolute" top={0} left={0} right={0} bottom={0}
          bg={`linear-gradient(transparent 30%, ${era.color}CC 100%)`}
        />
        <Box position="absolute" bottom={0} left={0} right={0} p={6}>
          <Flex align="center" gap={2} mb={1}>
            <Clock size={16} color="white" />
            <Text fontSize="sm" color="rgba(255,255,255,0.8)">{era.years}</Text>
          </Flex>
          <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '3xl' }} fontWeight={700} color="white">
            {era.name}
          </Heading>
          <Text fontSize="md" color="rgba(255,255,255,0.9)" mt={1} maxW="600px">
            {era.description}
          </Text>
        </Box>
      </Box>

      {/* Key Metrics */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={8}>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4}>
          <Text fontSize="2xl" fontWeight={700} color={era.color} fontFamily='"Cinzel", serif'>{era.events}</Text>
          <Text fontSize="sm" color="#524E44">Event Windows</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4}>
          <Text fontSize="2xl" fontWeight={700} color={era.color} fontFamily='"Cinzel", serif'>{era.civilizations.length}</Text>
          <Text fontSize="sm" color="#524E44">Civilizations</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4}>
          <Text fontSize="2xl" fontWeight={700} color={era.color} fontFamily='"Cinzel", serif'>{era.regions.length}</Text>
          <Text fontSize="sm" color="#524E44">Regions</Text>
        </Box>
        <Box bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4}>
          <Text fontSize="2xl" fontWeight={700} color={era.color} fontFamily='"Cinzel", serif'>{eraEvents.length}</Text>
          <Text fontSize="sm" color="#524E44">Timeline Events</Text>
        </Box>
      </SimpleGrid>

      {/* Regions Pills */}
      <Box mb={8}>
        <Text fontSize="xs" fontWeight={700} color="#96770B" mb={2} textTransform="uppercase" letterSpacing="0.05em">Active Regions</Text>
        <Flex gap={2} flexWrap="wrap">
          {era.regions.map(r => (
            <Box
              key={r} bg="white" border="1px solid" borderColor="#E4E2DC"
              px={3} py={1.5} borderRadius="full" fontSize="sm" color="#524E44"
            >
              <Flex align="center" gap={1.5}>
                <Globe size={12} color={era.color} />
                {r}
              </Flex>
            </Box>
          ))}
        </Flex>
      </Box>

      {/* Civilizations Gallery */}
      {era.civilizations.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Civilizations & Cultures"
            subtitle={`${era.civilizations.length} civilizations that defined this era`}
          />
          <CivilizationGallery civilizations={era.civilizations} eraColor={era.color} />
        </Box>
      )}

      {era.civilizations.length === 0 && (
        <Box mb={8} bg="#F5F4F0" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={6} textAlign="center">
          <BookOpen size={32} color="#96770B" style={{ margin: '0 auto 12px' }} />
          <Text fontFamily='"Cinzel", serif' fontSize="lg" color="#2D2A24" fontWeight={600}>
            Civilization Profiles Coming Soon
          </Text>
          <Text fontSize="sm" color="#524E44" mt={2} maxW="400px" mx="auto">
            Detailed civilization profiles for the {era.name} era are being researched and curated.
            Check back as our knowledge graph expands.
          </Text>
        </Box>
      )}

      {/* Timeline Section */}
      {eraEvents.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Timeline"
            subtitle={`${eraEvents.length} key events in the ${era.name} era`}
          />
          <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" overflow="hidden">
            <Timeline events={eraEvents} />
          </Box>
        </Box>
      )}

      {/* Navigation Footer */}
      <Flex justify="space-between" align="center" mt={8} pt={6} borderTop="1px solid" borderColor="#E4E2DC">
        <RouterLink to="/explore" style={{ textDecoration: 'none' }}>
          <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: '#D4AF37' }}>
            <ChevronLeft size={18} />
            <Text fontSize="sm">Back to Era Explorer</Text>
          </Flex>
        </RouterLink>
        <RouterLink to="/graph" style={{ textDecoration: 'none' }}>
          <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: '#D4AF37' }}>
            <Text fontSize="sm">Explore Knowledge Graph</Text>
            <Star size={14} />
          </Flex>
        </RouterLink>
      </Flex>
    </Box>
  )
}
