import React, { useMemo } from 'react'
import { useParams, Link as RouterLink, useNavigate } from 'react-router-dom'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import {
  Clock, ChevronLeft, ChevronRight, Globe, BookOpen, Star, Home,
  Users, Landmark, MapPin, Layers, FileText, Shield, Zap, Compass,
} from 'lucide-react'
import { getEraById, ERAS as ALL_ERAS } from '../constants/eras'
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

/* Reverse mapping: catalog eraSlug → eras.ts id */
const SLUG_TO_ERA_ID: Record<string, string> = Object.fromEntries(
  Object.entries(ERA_ID_TO_SLUG).map(([k, v]) => [v, k])
)

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

  // Era ordering for prev/next navigation
  const eraIndex = ALL_ERAS.findIndex(e => e.id === eraId)
  const prevEra = eraIndex > 0 ? ALL_ERAS[eraIndex - 1] : undefined
  const nextEra = eraIndex < ALL_ERAS.length - 1 ? ALL_ERAS[eraIndex + 1] : undefined

  // Key figures: up to 6 notable Persons for the spotlight
  const keyFigures = useMemo(() =>
    (entityGroups.get('Person') || []).slice(0, 6),
  [entityGroups])

  // Key Institutions
  const keyInstitutions = useMemo(() =>
    (entityGroups.get('Institution') || []).slice(0, 6),
  [entityGroups])

  // Key Texts
  const keyTexts = useMemo(() =>
    (entityGroups.get('Text') || []).slice(0, 6),
  [entityGroups])

  // Key Movements
  const keyMovements = useMemo(() =>
    (entityGroups.get('Movement') || []).slice(0, 4),
  [entityGroups])

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
      {/* ── Enhanced Breadcrumb ── */}
      <Flex align="center" gap={1.5} mb={4} flexWrap="wrap">
        <RouterLink to="/" style={{ display: 'flex', alignItems: 'center', gap: 4, color: '#9E9A90', textDecoration: 'none' }}>
          <Home size={14} />
          <Text fontSize="xs" _hover={{ color: '#D4AF37' }}>Home</Text>
        </RouterLink>
        <ChevronRight size={12} color="#D6D3CC" />
        <RouterLink to="/explore" style={{ color: '#9E9A90', textDecoration: 'none' }}>
          <Text fontSize="xs" _hover={{ color: '#D4AF37' }}>Eras</Text>
        </RouterLink>
        <ChevronRight size={12} color="#D6D3CC" />
        <Text fontSize="xs" color={era.color} fontWeight={600}>{era.name}</Text>
      </Flex>

      {/* ── Era quick-nav pills ── */}
      <Flex gap={2} mb={6} flexWrap="wrap">
        {ALL_ERAS.map(e => {
          const isActive = e.id === eraId
          return (
            <RouterLink key={e.id} to={`/explore/${e.id}`} style={{ textDecoration: 'none' }}>
              <Box
                px={3} py={1.5} borderRadius="full" fontSize="xs" fontWeight={600}
                fontFamily="'Inter', sans-serif"
                bg={isActive ? e.color : `${e.color}10`}
                color={isActive ? 'white' : e.color}
                border="1px solid"
                borderColor={isActive ? e.color : `${e.color}30`}
                _hover={{ bg: isActive ? e.color : `${e.color}20` }}
                cursor="pointer" transition="all 0.15s"
              >
                {e.name}
              </Box>
            </RouterLink>
          )
        })}
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

      {/* ── Key Figures Spotlight ── */}
      {keyFigures.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Key Figures"
            subtitle={`Notable people of the ${era.name} era`}
          />
          <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={3}>
            {keyFigures.map(p => (
              <Box key={p.slug} bg="white" border="1px solid" borderColor="#E4E2DC"
                borderRadius="8px" overflow="hidden" cursor="pointer"
                onClick={() => navigate(`/entity/${p.slug}`)}
                _hover={{ borderColor: '#3A7D44', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
                transition="all 0.15s">
                <Box h="3px" bg="#3A7D44" />
                <Box p={3}>
                  <Flex align="center" gap={2} mb={1}>
                    <Users size={14} color="#3A7D44" />
                    <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
                      color="#2D2A24" flex={1} lineClamp={1}>{p.name}</Text>
                  </Flex>
                  <Text fontSize="xs" color="#787469" fontFamily="'JetBrains Mono', monospace" mb={1}>
                    {p.period || p.born || ''}</Text>
                  <Text fontSize="xs" color="#524E44" lineClamp={2}>{p.summary}</Text>
                </Box>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ── Key Institutions ── */}
      {keyInstitutions.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Institutions"
            subtitle={`Major institutions of the ${era.name} era`}
          />
          <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={3}>
            {keyInstitutions.map(inst => (
              <Box key={inst.slug} bg="white" border="1px solid" borderColor="#E4E2DC"
                borderRadius="8px" overflow="hidden" cursor="pointer"
                onClick={() => navigate(`/entity/${inst.slug}`)}
                _hover={{ borderColor: '#8B3A3A', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
                transition="all 0.15s">
                <Box h="3px" bg="#8B3A3A" />
                <Box p={3}>
                  <Flex align="center" gap={2} mb={1}>
                    <Landmark size={14} color="#8B3A3A" />
                    <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
                      color="#2D2A24" flex={1} lineClamp={1}>{inst.name}</Text>
                  </Flex>
                  <Text fontSize="xs" color="#787469" fontFamily="'JetBrains Mono', monospace" mb={1}>
                    {inst.founded || inst.period || ''}</Text>
                  <Text fontSize="xs" color="#524E44" lineClamp={2}>{inst.summary}</Text>
                </Box>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      {/* ── Key Movements ── */}
      {keyMovements.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Movements & Currents"
            subtitle={`Defining movements of the ${era.name} era`}
          />
          <Flex gap={3} flexWrap="wrap">
            {keyMovements.map(m => (
              <Box key={m.slug} bg="white" border="1px solid" borderColor="#E4E2DC"
                borderRadius="8px" overflow="hidden" cursor="pointer" flex="1" minW="220px"
                onClick={() => navigate(`/entity/${m.slug}`)}
                _hover={{ borderColor: '#6B3FA0', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
                transition="all 0.15s">
                <Box h="3px" bg="#6B3FA0" />
                <Box p={3}>
                  <Flex align="center" gap={2} mb={1}>
                    <Layers size={14} color="#6B3FA0" />
                    <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
                      color="#2D2A24">{m.name}</Text>
                  </Flex>
                  <Text fontSize="xs" color="#524E44" lineClamp={2}>{m.summary}</Text>
                </Box>
              </Box>
            ))}
          </Flex>
        </Box>
      )}

      {/* ── Key Texts ── */}
      {keyTexts.length > 0 && (
        <Box mb={8}>
          <SectionHeading
            title="Defining Texts"
            subtitle={`Seminal writings of the ${era.name} era`}
          />
          <SimpleGrid columns={{ base: 1, sm: 2 }} gap={3}>
            {keyTexts.map(t => (
              <Flex key={t.slug} bg="white" border="1px solid" borderColor="#E4E2DC"
                borderRadius="8px" overflow="hidden" cursor="pointer"
                onClick={() => navigate(`/entity/${t.slug}`)}
                _hover={{ borderColor: '#5A2222', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}
                transition="all 0.15s" align="center" gap={3} p={3}>
                <FileText size={20} color="#5A2222" style={{ flexShrink: 0 }} />
                <Box>
                  <Text fontFamily="'Cormorant Garamond', serif" fontSize="md" fontWeight={700}
                    color="#2D2A24" lineClamp={1}>{t.name}</Text>
                  <Text fontSize="xs" color="#787469" fontFamily="'JetBrains Mono', monospace">
                    {t.period || t.born || ''}</Text>
                </Box>
              </Flex>
            ))}
          </SimpleGrid>
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

      {/* Navigation Footer — prev/next era + links */}
      <Flex justify="space-between" align="center" mt={8} pt={6} borderTop="1px solid" borderColor="#E4E2DC">
        {prevEra ? (
          <RouterLink to={`/explore/${prevEra.id}`} style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: prevEra.color }}>
              <ChevronLeft size={18} />
              <Box>
                <Text fontSize="xs" color="#B8B2A4">Previous Era</Text>
                <Text fontSize="sm" fontWeight={600}>{prevEra.name}</Text>
              </Box>
            </Flex>
          </RouterLink>
        ) : (
          <RouterLink to="/explore" style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: '#D4AF37' }}>
              <ChevronLeft size={18} />
              <Text fontSize="sm">All Eras</Text>
            </Flex>
          </RouterLink>
        )}
        <RouterLink to={`/catalog?era=${catalogSlug}`} style={{ textDecoration: 'none' }}>
          <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: '#D4AF37' }}>
            <Compass size={14} />
            <Text fontSize="sm">Full Catalog</Text>
          </Flex>
        </RouterLink>
        {nextEra ? (
          <RouterLink to={`/explore/${nextEra.id}`} style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: nextEra.color }}>
              <Box textAlign="right">
                <Text fontSize="xs" color="#B8B2A4">Next Era</Text>
                <Text fontSize="sm" fontWeight={600}>{nextEra.name}</Text>
              </Box>
              <ChevronRight size={18} />
            </Flex>
          </RouterLink>
        ) : (
          <RouterLink to="/graph" style={{ textDecoration: 'none' }}>
            <Flex align="center" gap={2} color="#9E9A90" _hover={{ color: '#D4AF37' }}>
              <Text fontSize="sm">Knowledge Graph</Text>
              <Star size={14} />
            </Flex>
          </RouterLink>
        )}
      </Flex>
    </Box>
  )
}
