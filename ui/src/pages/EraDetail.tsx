import React, { useMemo } from 'react'
import { useParams, Link as RouterLink, useNavigate } from 'react-router-dom'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import {
  Clock, ChevronLeft, Globe, BookOpen, Star,
  Users, Landmark, MapPin, Layers, FileText, Shield, Zap,
} from 'lucide-react'
import { getEraById } from '../constants/eras'
import { TIMELINE_EVENTS } from '../data/timeline-events'
import { SectionHeading } from '../components/DataCards'
import Timeline from '../components/Timeline'
import CivilizationGallery from '../components/CivilizationGallery'
import { getEntitiesByEra, type Entity } from '../data/catalog'

/* Era slug mapping: eras.ts ids → catalog eraSlug */
const ERA_ID_TO_SLUG: Record<string, string> = {
  prehistory: 'prehistoric',
  ancient: 'classical',
  medieval: 'medieval',
  'early-modern': 'early-modern',
  modern: 'modern',
  contemporary: 'contemporary',
}

const LABEL_ORDER = ['Person', 'Institution', 'EventWindow', 'Movement', 'Text', 'Idea', 'Place', 'Evidence']

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
  Idea: <Zap size={16} />,
  Person: <Users size={16} />,
  Institution: <Landmark size={16} />,
  Place: <MapPin size={16} />,
  EventWindow: <Clock size={16} />,
  Movement: <Layers size={16} />,
  Text: <FileText size={16} />,
  Evidence: <Shield size={16} />,
}

export default function EraDetail() {
  const { eraId } = useParams<{ eraId: string }>()
  const navigate = useNavigate()
  const era = eraId ? getEraById(eraId) : undefined

  const eraEvents = useMemo(
    () => TIMELINE_EVENTS.filter(ev => ev.era === eraId),
    [eraId],
  )

  // Get catalog entities for this era, grouped by actor type
  const catalogSlug = eraId ? (ERA_ID_TO_SLUG[eraId] || eraId) : ''
  const eraEntities = useMemo(() => getEntitiesByEra(catalogSlug), [catalogSlug])
  const entityGroups = useMemo(() => {
    const map = new Map<string, Entity[]>()
    for (const e of eraEntities) {
      const arr = map.get(e.label) || []
      arr.push(e)
      map.set(e.label, arr)
    }
    return map
  }, [eraEntities])

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

      {/* ── Catalog Entities Section (grouped by actor type) ── */}
      {eraEntities.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Catalog Actors"
            subtitle={`${eraEntities.length} actors in the ${era.name} era — grouped by type`}
          />
          {/* Type summary pills */}
          <Flex gap={2} mb={4} flexWrap="wrap">
            {LABEL_ORDER.filter(l => entityGroups.has(l)).map(l => {
              const color = LABEL_COLORS[l] || '#787469'
              const count = entityGroups.get(l)?.length || 0
              return (
                <Box key={l} display="flex" alignItems="center" gap={1.5}
                  px={2.5} py={1} borderRadius="6px" fontSize="xs" fontWeight={600}
                  fontFamily="'JetBrains Mono', monospace"
                  bg={`${color}10`} color={color}
                  border="1px solid" borderColor={`${color}30`}>
                  {LABEL_ICONS[l]}
                  {LABEL_DISPLAY[l] || l}: {count}
                </Box>
              )
            })}
          </Flex>

          {/* Grouped actor sections */}
          {LABEL_ORDER.filter(l => entityGroups.has(l)).map((labelKey, idx) => {
            const entities = entityGroups.get(labelKey) || []
            const color = LABEL_COLORS[labelKey] || '#787469'
            return (
              <Box key={labelKey} mb={6}>
                {idx > 0 && (
                  <Box h="1px" bg="linear-gradient(to right, transparent, #E4E2DC, transparent)" mb={4} />
                )}
                <Flex align="center" gap={2} mb={3} pb={2}
                  borderBottom="2px solid" borderColor={`${color}40`}>
                  <Box color={color}>{LABEL_ICONS[labelKey]}</Box>
                  <Text fontFamily="'Cormorant Garamond', serif" fontSize="lg" fontWeight={700}
                    color={color}>{LABEL_DISPLAY[labelKey] || labelKey}</Text>
                  <Box px={2} py={0.5} borderRadius="full" fontSize="10px" fontWeight={700}
                    fontFamily="'JetBrains Mono', monospace"
                    bg={`${color}12`} color={color}>
                    {entities.length}
                  </Box>
                </Flex>
                <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={3}>
                  {entities.map(e => (
                    <Box key={e.slug} bg="white" border="1px solid" borderColor="#E4E2DC"
                      borderRadius="8px" overflow="hidden" cursor="pointer"
                      onClick={() => navigate(`/entity/${e.slug}`)}
                      _hover={{ borderColor: color, boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
                      transition="all 0.15s">
                      <Box h="3px" bg={color} />
                      <Box p={3}>
                        <Flex align="center" gap={2} mb={1}>
                          <Text fontFamily="'JetBrains Mono', monospace" fontSize="xs" fontWeight={700}
                            color={color}>{e.callNumber.split('-')[0]}</Text>
                          <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
                            color="#2D2A24" flex={1} lineClamp={1}>{e.name}</Text>
                        </Flex>
                        <Text fontSize="xs" color="#787469" fontFamily="'JetBrains Mono', monospace" mb={1}>
                          {e.period || e.born || e.founded || e.startDate || ''}</Text>
                        <Text fontSize="xs" color="#524E44" lineClamp={2} fontFamily="'Inter', sans-serif"
                          lineHeight="1.5">{e.summary}</Text>
                      </Box>
                    </Box>
                  ))}
                </SimpleGrid>
              </Box>
            )
          })}

          {/* Link to full catalog filtered by era */}
          <Flex justify="center" mt={4}>
            <RouterLink to={`/catalog?era=${catalogSlug}`} style={{ textDecoration: 'none' }}>
              <Text fontSize="sm" color="#D4AF37" fontWeight={600}
                fontFamily="'Inter', sans-serif" _hover={{ textDecoration: 'underline' }}>
                View all {eraEntities.length} actors in the full Catalog →
              </Text>
            </RouterLink>
          </Flex>
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
