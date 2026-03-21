/* ─── Human Story Dashboard — Annals of the World ─── */
/* Interactive data visualizations: world languages, global diet, ancient trade routes */
import React, { useState, useCallback, useMemo } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Badge } from '@chakra-ui/react'
import Breadcrumb from '../components/Breadcrumb'
import {
  ComposableMap, Geographies, Geography, ZoomableGroup, Line, Marker,
} from 'react-simple-maps'
import { Languages, Utensils, Route, Globe2, ChevronDown, ChevronUp } from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import { LANGUAGE_FAMILIES, LANGUAGE_FAMILY_MAP, COUNTRY_LANGUAGE_FAMILY } from '../data/world-languages'
import { PROTEIN_TYPES, PROTEIN_MAP, COUNTRY_PROTEIN } from '../data/world-diet'
import { TRADE_ROUTES } from '../data/trade-routes'
import { ISO_NUMERIC_TO_A3 } from '../data/iso-numeric-map'

const GEO_URL = 'https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json'

type ActiveLayer = 'languages' | 'diet' | 'trade'

export default function HumanStory() {
  const [activeLayer, setActiveLayer] = useState<ActiveLayer>('languages')
  const [hoveredGeo, setHoveredGeo] = useState<string | null>(null)
  const [hoveredRoute, setHoveredRoute] = useState<string | null>(null)
  const [expandedSection, setExpandedSection] = useState<string | null>(null)

  const getGeoFill = useCallback((geo: { id?: string; properties: { ISO_A3?: string } }) => {
    const iso = geo.properties.ISO_A3 || ISO_NUMERIC_TO_A3[geo.id || ''] || ''
    if (!iso) return '#E2D6C6'
    if (activeLayer === 'languages') {
      const familyId = COUNTRY_LANGUAGE_FAMILY[iso]
      return familyId ? (LANGUAGE_FAMILY_MAP[familyId]?.color || '#E2D6C6') : '#E2D6C6'
    }
    if (activeLayer === 'diet') {
      const proteinId = COUNTRY_PROTEIN[iso]
      return proteinId ? (PROTEIN_MAP[proteinId]?.color || '#E2D6C6') : '#E2D6C6'
    }
    return '#E2D6C6'
  }, [activeLayer])

  const legendItems = useMemo(() => {
    if (activeLayer === 'languages') return LANGUAGE_FAMILIES.map(f => ({ color: f.color, label: f.name, detail: f.speakers }))
    if (activeLayer === 'diet') return PROTEIN_TYPES.map(p => ({ color: p.color, label: `${p.icon} ${p.name}`, detail: '' }))
    return TRADE_ROUTES.map(r => ({ color: r.color, label: r.name, detail: r.period }))
  }, [activeLayer])

  const geoTooltipInfo = useCallback((iso: string) => {
    if (activeLayer === 'languages') {
      const fId = COUNTRY_LANGUAGE_FAMILY[iso]
      const f = fId ? LANGUAGE_FAMILY_MAP[fId] : null
      return f ? `${f.name} (${f.speakers} speakers)` : 'No data'
    }
    if (activeLayer === 'diet') {
      const pId = COUNTRY_PROTEIN[iso]
      const p = pId ? PROTEIN_MAP[pId] : null
      return p ? `${p.icon} ${p.name}` : 'No data'
    }
    return ''
  }, [activeLayer])

  return (
    <Box>
      <Breadcrumb items={[{ label: 'The Human Story' }]} />
      {/* Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Globe2 size={28} color="#D4AF37" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            The Human Story
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="750px">
          How language shaped us. How diet defined us. How trade connected us.
          Explore the patterns that make us human — from the first words spoken to global supply chains.
        </Text>
      </Box>

      {/* Layer Selector */}
      <Flex gap={3} mb={6} flexWrap="wrap">
        {([
          { id: 'languages' as const, icon: <Languages size={18} />, label: 'World Languages', color: '#4A90D9' },
          { id: 'diet' as const, icon: <Utensils size={18} />, label: 'Global Diet', color: '#C53030' },
          { id: 'trade' as const, icon: <Route size={18} />, label: 'Trade Routes', color: '#D4AF37' },
        ]).map(layer => (
          <Box
            key={layer.id}
            px={5} py={3}
            bg={activeLayer === layer.id ? layer.color : '#FDFAF5'}
            color={activeLayer === layer.id ? '#fff' : '#2D2A24'}
            border="2px solid"
            borderColor={activeLayer === layer.id ? layer.color : '#E4E2DC'}
            borderRadius="full"
            cursor="pointer"
            onClick={() => setActiveLayer(layer.id)}
            transition="all 0.2s"
            _hover={{ borderColor: layer.color, transform: 'translateY(-1px)' }}
          >
            <Flex align="center" gap={2}>
              {layer.icon}
              <Text fontFamily='"Inter", sans-serif' fontWeight={600} fontSize="sm">{layer.label}</Text>
            </Flex>
          </Box>
        ))}
      </Flex>

      {/* Map + Legend */}
      <Box bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl" overflow="hidden" mb={8}>
        {/* Tooltip bar */}
        {hoveredGeo && activeLayer !== 'trade' && (
          <Box px={4} py={2} bg="#FDF8ED" borderBottom="1px solid #E4E2DC">
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={600} color="#2D2A24">
              {hoveredGeo}
            </Text>
          </Box>
        )}
        {hoveredRoute && activeLayer === 'trade' && (
          <Box px={4} py={2} bg="#FDF8ED" borderBottom="1px solid #E4E2DC">
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={600} color="#2D2A24">
              {hoveredRoute}
            </Text>
          </Box>
        )}

        <ComposableMap
          projectionConfig={{ rotate: [-10, 0, 0], scale: 147 }}
          style={{ width: '100%', height: 'auto' }}
        >
          <ZoomableGroup>
            <Geographies geography={GEO_URL}>
              {({ geographies }) =>
                geographies.map(geo => {
                  const iso = geo.properties.ISO_A3 || ISO_NUMERIC_TO_A3[geo.id || ''] || ''
                  const name = geo.properties.name || geo.properties.NAME || 'Unknown'
                  return (
                    <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      fill={getGeoFill(geo)}
                      stroke="#FAFAF8"
                      strokeWidth={0.5}
                      style={{
                        default: { outline: 'none', fillOpacity: activeLayer === 'trade' ? 0.3 : 0.85 },
                        hover: { outline: 'none', fillOpacity: 1, stroke: '#2D2A24', strokeWidth: 1.5 },
                        pressed: { outline: 'none' },
                      }}
                      onMouseEnter={() => {
                        const info = geoTooltipInfo(iso)
                        setHoveredGeo(`${name} — ${info}`)
                      }}
                      onMouseLeave={() => setHoveredGeo(null)}
                    />
                  )
                })
              }
            </Geographies>

            {/* Trade route lines */}
            {activeLayer === 'trade' && TRADE_ROUTES.map(route => (
              <React.Fragment key={route.id}>
                <Line
                  from={route.coordinates[0]}
                  to={route.coordinates[route.coordinates.length - 1]}
                  coordinates={route.coordinates}
                  stroke={route.color}
                  strokeWidth={3}
                  strokeLinecap="round"
                  fill="none"
                  cursor="pointer"
                  onMouseEnter={() => setHoveredRoute(`${route.name} (${route.period}) — ${route.goods.join(', ')}`)}
                  onMouseLeave={() => setHoveredRoute(null)}
                />
                {/* Start/End markers */}
                {[route.coordinates[0], route.coordinates[route.coordinates.length - 1]].map((coord, i) => (
                  <Marker key={`${route.id}-${i}`} coordinates={coord}>
                    <circle r={3} fill={route.color} stroke="#fff" strokeWidth={1} />
                  </Marker>
                ))}
              </React.Fragment>
            ))}
          </ZoomableGroup>
        </ComposableMap>
      </Box>

      {/* Legend */}
      <Box mb={8}>
        <SectionHeading
          title={activeLayer === 'languages' ? 'Language Families of the World' : activeLayer === 'diet' ? 'Dominant Protein by Country' : 'Ancient & Medieval Trade Routes'}
          subtitle={activeLayer === 'languages' ? '13 major families spanning 7,000+ living languages' : activeLayer === 'diet' ? 'What the world eats: primary protein sources' : '7 trade networks that shaped civilizations'}
        />
        <SimpleGrid columns={{ base: 2, sm: 3, md: 4, lg: activeLayer === 'trade' ? 3 : 5 }} gap={3} mt={4}>
          {legendItems.map(item => (
            <Flex key={item.label} align="center" gap={2} p={2} bg="#FDFAF5" borderRadius="md" border="1px solid #E4E2DC">
              <Box w="14px" h="14px" borderRadius="sm" bg={item.color} flexShrink={0} />
              <Box>
                <Text fontSize="xs" fontWeight={600} color="#2D2A24" fontFamily='"Inter", sans-serif' lineHeight={1.3}>
                  {item.label}
                </Text>
                {item.detail && (
                  <Text fontSize="10px" color="#9E9A90" fontFamily='"JetBrains Mono", monospace'>
                    {item.detail}
                  </Text>
                )}
              </Box>
            </Flex>
          ))}
        </SimpleGrid>
      </Box>

      {/* ─── LANGUAGE INSIGHTS ─── */}
      {activeLayer === 'languages' && (
        <Box mb={8}>
          <Box
            cursor="pointer" onClick={() => setExpandedSection(expandedSection === 'lang' ? null : 'lang')}
            mb={expandedSection === 'lang' ? 4 : 0}
          >
            <Flex align="center" gap={2}>
              <SectionHeading title="How Language Shaped Humanity" subtitle="Language isn't just communication — it's the operating system of civilization" />
              {expandedSection === 'lang' ? <ChevronUp size={20} color="#9E9A90" /> : <ChevronDown size={20} color="#9E9A90" />}
            </Flex>
          </Box>
          {expandedSection === 'lang' && (
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              {[
                { title: 'Abstract Thought', body: 'Language enabled humans to think about things that don\'t physically exist — gods, laws, credit, nations, human rights. Without language, no civilization could form beyond a few dozen individuals.', year: '~70,000 BCE', source: 'Harari, Sapiens (2014)' },
                { title: 'Collective Memory', body: 'Oral tradition allowed knowledge to survive beyond a single lifetime. Stories, genealogies, and navigation instructions were transmitted across generations. Writing (3400 BCE) made this permanent.', year: '~40,000 BCE', source: 'Ong, Orality and Literacy (1982)' },
                { title: 'Social Coordination', body: 'Language allowed groups of 150+ to cooperate through shared myths and institutional narratives. "The nation," "the company," "the religion" — all exist only because language sustains them.', year: '~30,000 BCE', source: 'Dunbar, Grooming, Gossip and Language (1996)' },
                { title: 'Cultural Divergence', body: 'As human groups separated and languages diverged, distinct worldviews formed. The Sapir-Whorf hypothesis suggests language doesn\'t just describe reality — it shapes perception. Time, color, kinship — all vary by language.', year: 'Ongoing', source: 'Boroditsky, "How Language Shapes Thought" (2011)' },
              ].map(insight => (
                <Box key={insight.title} p={5} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="lg">
                  <Badge bg="#4A90D9" color="#fff" fontSize="10px" mb={2}>{insight.year}</Badge>
                  <Heading fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#2D2A24" mb={2}>
                    {insight.title}
                  </Heading>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7} mb={2}>
                    {insight.body}
                  </Text>
                  <Text fontFamily='"Inter", sans-serif' fontSize="10px" color="#9E9A90" fontStyle="italic">
                    {insight.source}
                  </Text>
                </Box>
              ))}
            </SimpleGrid>
          )}
        </Box>
      )}

      {/* ─── DIET INSIGHTS ─── */}
      {activeLayer === 'diet' && (
        <Box mb={8}>
          <Box
            cursor="pointer" onClick={() => setExpandedSection(expandedSection === 'diet' ? null : 'diet')}
            mb={expandedSection === 'diet' ? 4 : 0}
          >
            <Flex align="center" gap={2}>
              <SectionHeading title="How Diet Shaped Civilizations" subtitle="You are what your ancestors ate — agriculture determined empire" />
              {expandedSection === 'diet' ? <ChevronUp size={20} color="#9E9A90" /> : <ChevronDown size={20} color="#9E9A90" />}
            </Flex>
          </Box>
          {expandedSection === 'diet' && (
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              {[
                { title: 'Grain Empires', body: 'Wheat (Middle East), rice (Asia), and maize (Americas) enabled population density. States formed where grain grew: grain is taxable, storable, and visible — unlike tubers or fish. Empires are built on cereal agriculture.', source: 'Scott, Against the Grain (2017)' },
                { title: 'Protein Geography', body: 'Coastal nations eat fish. Grassland nations raise cattle. Arid nations herd goats. Tropical nations eat chicken. This isn\'t random — geography determines which protein sources are viable. Diet is destiny.', source: 'Diamond, Guns, Germs, and Steel (1997)' },
                { title: 'Religious Diet Laws', body: 'Judaism, Islam, and Hinduism all encode dietary restrictions that shaped millions of lives. Pork taboos in the Middle East, beef taboos in India, and alcohol restrictions in Islam — religion codified ecological wisdom into sacred law.', source: 'Harris, Good to Eat (1985)' },
                { title: 'The Columbian Exchange', body: 'Before 1492, no Italian had eaten a tomato, no Irishman a potato, no Thai a chili pepper, and no American a chicken. The post-Columbus food exchange was the greatest dietary revolution in human history.', source: 'Crosby, The Columbian Exchange (2003)' },
              ].map(insight => (
                <Box key={insight.title} p={5} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="lg">
                  <Heading fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#2D2A24" mb={2}>
                    {insight.title}
                  </Heading>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7} mb={2}>
                    {insight.body}
                  </Text>
                  <Text fontFamily='"Inter", sans-serif' fontSize="10px" color="#9E9A90" fontStyle="italic">
                    {insight.source}
                  </Text>
                </Box>
              ))}
            </SimpleGrid>
          )}
        </Box>
      )}

      {/* ─── TRADE INSIGHTS ─── */}
      {activeLayer === 'trade' && (
        <Box mb={8}>
          <Box
            cursor="pointer" onClick={() => setExpandedSection(expandedSection === 'trade' ? null : 'trade')}
            mb={expandedSection === 'trade' ? 4 : 0}
          >
            <Flex align="center" gap={2}>
              <SectionHeading title="How Trade Built the World" subtitle="Follow the goods, and you find the history" />
              {expandedSection === 'trade' ? <ChevronUp size={20} color="#9E9A90" /> : <ChevronDown size={20} color="#9E9A90" />}
            </Flex>
          </Box>
          {expandedSection === 'trade' && (
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              {TRADE_ROUTES.map(route => (
                <Box key={route.id} p={5} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="lg">
                  <Flex align="center" gap={2} mb={2}>
                    <Box w="12px" h="12px" borderRadius="full" bg={route.color} />
                    <Heading fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#2D2A24">
                      {route.name}
                    </Heading>
                    <Badge bg={route.color} color="#fff" fontSize="10px" ml="auto">{route.period}</Badge>
                  </Flex>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.7} mb={2}>
                    {route.description}
                  </Text>
                  <Flex gap={2} flexWrap="wrap">
                    {route.goods.map(g => (
                      <Badge key={g} variant="subtle" fontSize="10px" fontFamily='"JetBrains Mono", monospace' bg="#FDF8ED" color="#9E9A90">
                        {g}
                      </Badge>
                    ))}
                  </Flex>
                </Box>
              ))}
            </SimpleGrid>
          )}
        </Box>
      )}

      {/* Footer insight */}
      <Box bg="#FDF8ED" border="1px solid #D4AF37" borderRadius="xl" p={6} mb={8}>
        <Flex align="center" gap={2} mb={3}>
          <Globe2 size={20} color="#D4AF37" />
          <Heading fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#4A310D">
            The Annals Thesis
          </Heading>
        </Flex>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8}>
          Humans are the only species that tell stories about the future. Language gave us abstract thought.
          Agriculture gave us surplus. Surplus gave us hierarchy. Hierarchy gave us law. Law gave us institutions.
          Institutions gave us trade. Trade gave us the world. Every map on this page is a chapter in the same story —
          how 300,000 years of accumulated culture turned a vulnerable primate into the dominant force on Earth.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" color="#9E9A90" mt={3}>
          "We are our stories." — Annals of the World
        </Text>
      </Box>
    </Box>
  )
}
