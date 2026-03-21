import React, { useState } from 'react'
import { Box, Flex, Text, SimpleGrid, Heading } from '@chakra-ui/react'
import {
  BookOpen, Users, MapPin, FileText, Network, ArrowRight,
  ArrowLeft, Clock, Scroll, Shield,
} from 'lucide-react'

/* ── Demo entity: a well-known node already in the data ── */
const entity = {
  slug: 'henry_viii',
  name: 'Henry VIII',
  label: 'Person',
  callNumber: 'P-940-ENG-001',
  subjects: ['Tudor Dynasty', 'English Reformation', 'Monarchy', 'Church of England'],
  summary:
    'King of England from 1509 to 1547. Henry VIII broke with the authority of the Pope and the Roman Catholic Church, establishing the Church of England and initiating the English Reformation. His six marriages and their political consequences reshaped European diplomacy.',
  born: '28 June 1491, Greenwich Palace',
  died: '28 January 1547, Palace of Whitehall',
  era: 'Early Modern',
  region: 'Western Europe',
  status: 'Published',
}

const CAUSES = [
  { title: 'Papal Authority over English Crown', type: 'Idea', year: 'c. 1200–1530' },
  { title: 'Desire for Male Heir', type: 'Event', year: '1525–1533' },
  { title: 'Catherine of Aragon\'s Marriage Annulment Denied', type: 'Event', year: '1527–1533' },
  { title: 'Rise of Protestant Theology in Europe', type: 'Idea', year: 'c. 1517' },
]

const EFFECTS = [
  { title: 'Act of Supremacy', type: 'Text', year: '1534' },
  { title: 'Dissolution of the Monasteries', type: 'Event', year: '1536–1541' },
  { title: 'Church of England Established', type: 'Institution', year: '1534' },
  { title: 'English Reformation', type: 'Movement', year: '1534–1603' },
]

const PEOPLE = [
  { name: 'Thomas Cromwell', role: 'Chief Minister', relation: 'ADVISES' },
  { name: 'Thomas More', role: 'Lord Chancellor', relation: 'OPPOSES' },
  { name: 'Anne Boleyn', role: 'Queen Consort', relation: 'MARRIES' },
  { name: 'Thomas Cranmer', role: 'Archbishop of Canterbury', relation: 'SUPPORTS' },
]

const PLACES = [
  { name: 'Greenwich Palace', role: 'Birthplace' },
  { name: 'Hampton Court Palace', role: 'Primary Residence' },
  { name: 'Tower of London', role: 'Imprisonment / Execution site' },
  { name: 'Westminster', role: 'Parliamentary seat' },
]

const TEXTS = [
  { title: 'Act of Supremacy (1534)', type: 'Legal document' },
  { title: 'Assertio Septem Sacramentorum (1521)', type: 'Theological treatise' },
  { title: 'Six Articles (1539)', type: 'Doctrinal code' },
]

const TABS = [
  { id: 'overview', label: 'Overview', icon: BookOpen },
  { id: 'causes', label: 'Causes', icon: ArrowLeft },
  { id: 'effects', label: 'Effects', icon: ArrowRight },
  { id: 'people', label: 'People', icon: Users },
  { id: 'places', label: 'Places', icon: MapPin },
  { id: 'texts', label: 'Texts', icon: FileText },
  { id: 'graph', label: 'Graph', icon: Network },
]

export default function Demo() {
  const [activeTab, setActiveTab] = useState('overview')

  return (
    <Box>
      {/* ─── Entity Header — "Library Card" ─── */}
      <Box
        bg="#FAFAF8"
        border="1px solid"
        borderColor="#E4E2DC"
        borderRadius="lg"
        p={6}
        mb={6}
        position="relative"
        overflow="hidden"
      >
        <Box
          position="absolute"
          top={0}
          left={0}
          right={0}
          h="3px"
          bg="linear-gradient(90deg, #D4AF37 0%, transparent 100%)"
        />
        <Flex justify="space-between" align="flex-start" flexWrap="wrap" gap={4}>
          <Box>
            <Flex align="center" gap={2} mb={2}>
              <Box
                bg="#F5F4F0"
                border="1px solid #E4E2DC"
                borderRadius="4px"
                px={2}
                py={0.5}
              >
                <Text
                  fontFamily='"Cinzel", serif'
                  fontSize="10px"
                  color="#9E9A90"
                  letterSpacing="0.1em"
                  textTransform="uppercase"
                >
                  {entity.label}
                </Text>
              </Box>
              <Text
                fontFamily='"JetBrains Mono", monospace'
                fontSize="10px"
                color="#B8B2A4"
              >
                {entity.callNumber}
              </Text>
            </Flex>
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="2xl"
              fontWeight={700}
              color="#2D2A24"
              letterSpacing="0.04em"
            >
              {entity.name}
            </Text>
            <Flex gap={2} mt={2} flexWrap="wrap">
              {entity.subjects.map((s) => (
                <Box
                  key={s}
                  bg="#F5F4F0"
                  border="1px solid #EEEDEA"
                  borderRadius="full"
                  px={3}
                  py={0.5}
                >
                  <Text
                    fontFamily='"Inter", sans-serif'
                    fontSize="11px"
                    color="#787469"
                  >
                    {s}
                  </Text>
                </Box>
              ))}
            </Flex>
          </Box>
          <Flex align="center" gap={2}>
            <Shield size={14} color="#96770B" />
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="10px"
              color="#96770B"
              letterSpacing="0.1em"
              textTransform="uppercase"
            >
              {entity.status}
            </Text>
          </Flex>
        </Flex>
      </Box>

      {/* ─── Tab Navigation ─── */}
      <Flex
        bg="#FAFAF8"
        border="1px solid"
        borderColor="#E4E2DC"
        borderRadius="lg"
        overflow="hidden"
        mb={6}
      >
        {TABS.map((tab) => {
          const Icon = tab.icon
          const isActive = activeTab === tab.id
          return (
            <Box
              key={tab.id}
              as="button"
              onClick={() => setActiveTab(tab.id)}
              flex={1}
              py={3}
              px={2}
              bg={isActive ? 'rgba(212,175,55,0.06)' : 'transparent'}
              borderBottom="2px solid"
              borderColor={isActive ? '#D4AF37' : 'transparent'}
              cursor="pointer"
              transition="all 0.2s"
              _hover={{ bg: 'rgba(212,175,55,0.04)' }}
              display="flex"
              alignItems="center"
              justifyContent="center"
              gap="6px"
            >
              <Icon size={14} color={isActive ? '#2D2A24' : '#B8B2A4'} />
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="10px"
                fontWeight={isActive ? 700 : 400}
                color={isActive ? '#2D2A24' : '#9E9A90'}
                letterSpacing="0.1em"
                textTransform="uppercase"
              >
                {tab.label}
              </Text>
            </Box>
          )
        })}
      </Flex>

      {/* ─── Tab Content ─── */}
      <Box
        bg="#FAFAF8"
        border="1px solid"
        borderColor="#E4E2DC"
        borderRadius="lg"
        p={6}
        minH="300px"
      >
        {/* OVERVIEW */}
        {activeTab === 'overview' && (
          <Box>
            <Text fontSize="sm" color="#524E44" lineHeight={1.8} mb={4}>
              {entity.summary}
            </Text>
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mt={4}>
              <Flex gap={3} align="center">
                <Clock size={14} color="#B8B2A4" />
                <Box>
                  <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Born</Text>
                  <Text fontSize="sm" color="#2D2A24">{entity.born}</Text>
                </Box>
              </Flex>
              <Flex gap={3} align="center">
                <Clock size={14} color="#B8B2A4" />
                <Box>
                  <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Died</Text>
                  <Text fontSize="sm" color="#2D2A24">{entity.died}</Text>
                </Box>
              </Flex>
              <Flex gap={3} align="center">
                <Scroll size={14} color="#B8B2A4" />
                <Box>
                  <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Era</Text>
                  <Text fontSize="sm" color="#2D2A24">{entity.era}</Text>
                </Box>
              </Flex>
              <Flex gap={3} align="center">
                <MapPin size={14} color="#B8B2A4" />
                <Box>
                  <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.1em" textTransform="uppercase">Region</Text>
                  <Text fontSize="sm" color="#2D2A24">{entity.region}</Text>
                </Box>
              </Flex>
            </SimpleGrid>
          </Box>
        )}

        {/* CAUSES */}
        {activeTab === 'causes' && (
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.15em" textTransform="uppercase" mb={4}>
              What led to this entity
            </Text>
            {CAUSES.map((c, i) => (
              <Flex
                key={i}
                align="center"
                gap={4}
                py={3}
                borderBottom={i < CAUSES.length - 1 ? '1px solid #EEEDEA' : 'none'}
              >
                <ArrowRight size={14} color="#D4AF37" />
                <Box flex={1}>
                  <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{c.title}</Text>
                  <Text fontSize="xs" color="#9E9A90">{c.type} &middot; {c.year}</Text>
                </Box>
              </Flex>
            ))}
          </Box>
        )}

        {/* EFFECTS */}
        {activeTab === 'effects' && (
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.15em" textTransform="uppercase" mb={4}>
              Consequences and results
            </Text>
            {EFFECTS.map((e, i) => (
              <Flex
                key={i}
                align="center"
                gap={4}
                py={3}
                borderBottom={i < EFFECTS.length - 1 ? '1px solid #EEEDEA' : 'none'}
              >
                <ArrowLeft size={14} color="#8B3A3A" />
                <Box flex={1}>
                  <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{e.title}</Text>
                  <Text fontSize="xs" color="#9E9A90">{e.type} &middot; {e.year}</Text>
                </Box>
              </Flex>
            ))}
          </Box>
        )}

        {/* PEOPLE */}
        {activeTab === 'people' && (
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.15em" textTransform="uppercase" mb={4}>
              Key actors and associates
            </Text>
            {PEOPLE.map((p, i) => (
              <Flex
                key={i}
                align="center"
                gap={4}
                py={3}
                borderBottom={i < PEOPLE.length - 1 ? '1px solid #EEEDEA' : 'none'}
              >
                <Users size={14} color="#3B6BC2" />
                <Box flex={1}>
                  <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{p.name}</Text>
                  <Text fontSize="xs" color="#9E9A90">{p.role}</Text>
                </Box>
                <Box bg="#F5F4F0" border="1px solid #EEEDEA" borderRadius="full" px={2} py={0.5}>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">
                    {p.relation}
                  </Text>
                </Box>
              </Flex>
            ))}
          </Box>
        )}

        {/* PLACES */}
        {activeTab === 'places' && (
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.15em" textTransform="uppercase" mb={4}>
              Geographic footprint
            </Text>
            {PLACES.map((p, i) => (
              <Flex
                key={i}
                align="center"
                gap={4}
                py={3}
                borderBottom={i < PLACES.length - 1 ? '1px solid #EEEDEA' : 'none'}
              >
                <MapPin size={14} color="#96770B" />
                <Box flex={1}>
                  <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{p.name}</Text>
                  <Text fontSize="xs" color="#9E9A90">{p.role}</Text>
                </Box>
              </Flex>
            ))}
          </Box>
        )}

        {/* TEXTS */}
        {activeTab === 'texts' && (
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="9px" color="#B8B2A4" letterSpacing="0.15em" textTransform="uppercase" mb={4}>
              Documents, treaties, and artifacts
            </Text>
            {TEXTS.map((t, i) => (
              <Flex
                key={i}
                align="center"
                gap={4}
                py={3}
                borderBottom={i < TEXTS.length - 1 ? '1px solid #EEEDEA' : 'none'}
              >
                <FileText size={14} color="#5A2222" />
                <Box flex={1}>
                  <Text fontSize="sm" color="#2D2A24" fontWeight={500}>{t.title}</Text>
                  <Text fontSize="xs" color="#9E9A90">{t.type}</Text>
                </Box>
              </Flex>
            ))}
          </Box>
        )}

        {/* GRAPH */}
        {activeTab === 'graph' && (
          <Flex
            direction="column"
            align="center"
            justify="center"
            minH="250px"
            gap={4}
          >
            <Network size={48} color="#D6D3CC" />
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="sm"
              color="#9E9A90"
              letterSpacing="0.1em"
              textTransform="uppercase"
            >
              Knowledge Graph Visualization
            </Text>
            <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
              The full relationship web for this entity — causes, influences, and connections rendered as a force-directed graph.
              Connect to Neo4j to activate live queries.
            </Text>
          </Flex>
        )}
      </Box>
    </Box>
  )
}
