import React from 'react'
import { Box, SimpleGrid, Text, Flex, Heading } from '@chakra-ui/react'
import { BookOpen, Users, Globe, Scroll, Network, Clock } from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'

const TIMELINE = [
  { year: '1581', event: 'Born in Dublin, Ireland', detail: 'Son of Arland Ussher, clerk of chancery' },
  { year: '1594', event: 'Entered Trinity College Dublin', detail: 'At age 13, one of the first students' },
  { year: '1602', event: 'Ordained as priest', detail: 'Church of Ireland (Anglican)' },
  { year: '1607', event: 'Professor of Theological Controversies', detail: 'Trinity College Dublin' },
  { year: '1625', event: 'Archbishop of Armagh', detail: 'Primate of All Ireland — highest office' },
  { year: '1632', event: 'Began Annales Veteris Testamenti', detail: '18 years of research across European libraries' },
  { year: '1650', event: 'Published Annales (Part I)', detail: '1,600 pages synthesizing Biblical, Babylonian, Greek, and Roman chronologies' },
  { year: '1654', event: 'Published Part II', detail: 'Extended chronology from Hebrew kings to 70 AD' },
  { year: '1656', event: 'Died in Reigate, England', detail: 'Buried in Westminster Abbey by order of Oliver Cromwell' },
]

const ROADMAP = [
  {
    phase: 'Phase 1',
    title: 'Core Infrastructure',
    status: 'Active',
    items: ['Schema v4 + 11 core labels', 'File-first pipeline (JSON seed files)', 'English Reformation cluster (186 nodes)', '55 African country profiles (319 data points each)', '180 Asian event windows'],
    color: '#2F855A',
  },
  {
    phase: 'Phase 2',
    title: 'Scale & API',
    status: 'Next',
    items: ['100,000 nodes target', 'MCP service layer for Neo4j', 'Curator dashboard', 'Provenance logging', 'Country deep-dive pages'],
    color: '#4A90D9',
  },
  {
    phase: 'Phase 3',
    title: 'Community Growth',
    status: 'Planned',
    items: ['50+ contributors', 'Governance board', 'Wikidata crosswalk pilot', 'Contributor programs', 'Multilingual support'],
    color: '#D4AF37',
  },
  {
    phase: 'Phase 4',
    title: '1 Million Nodes',
    status: 'Vision',
    items: ['1,000,000 knowledge nodes', 'Wikimedia integration', 'JSON-LD / RDF exports', 'Academic partnerships', 'Self-sustaining ecosystem'],
    color: '#8B3A3A',
  },
]

export default function About() {
  return (
    <Box>
      <Breadcrumb items={[{ label: 'About' }]} />
      {/* Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <BookOpen size={28} color="#8B3A3A" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="3xl"
            fontWeight={700}
            color="#2D2A24"
          >
            About the Project
          </Heading>
        </Flex>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#524E44"
          maxW="700px"
        >
          Honoring James Ussher (1581–1656), Archbishop of Armagh, whose{' '}
          <Text as="span" fontStyle="italic">Annales Veteris Testamenti</Text> was
          the first serious attempt to unify world chronology. We modernize his vision
          with 21st-century data science.
        </Text>
        <Box h="3px" bg="#8B3A3A" w="80px" mt={4} />
      </Box>

      {/* Ussher Bio */}
      <SectionHeading
        title="James Ussher — The Chronologist"
        subtitle="Archbishop of Armagh and Primate of All Ireland"
      />
      <Box
        bg="white"
        border="1px solid"
        borderColor="#E4E2DC"
        borderRadius="lg"
        p={6}
        mb={8}
      >
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="md"
          color="#524E44"
          lineHeight={1.8}
        >
          James Ussher published his <em>Annales Veteris Testamenti, a prima mundi origine deducti</em>{' '}
          (Annals of the Old Testament, deduced from the first origins of the world) in 1650 — a
          monumental 1,600-page work that synchronized Biblical, Babylonian, Persian, Greek, and
          Roman timelines into a single coherent chronology.
        </Text>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="md"
          color="#524E44"
          lineHeight={1.8}
          mt={3}
        >
          While modern scholarship has moved beyond his specific dating (he famously placed creation
          at Sunday, October 23, 4004 BC), his <em>methodology</em> — cross-referencing multiple
          civilizations' records to construct a unified timeline — was revolutionary. He visited
          every major European library, corresponded with scholars across the continent, and spent
          18 years on the project.
        </Text>
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="md"
          color="#524E44"
          lineHeight={1.8}
          mt={3}
        >
          Our project honors his ambition while extending it: from Biblical antiquity to the
          algorithmic age, from Europe to every continent, from 1,600 pages to a living knowledge
          graph targeting 1,000,000 nodes.
        </Text>
      </Box>

      {/* Ussher Timeline */}
      <SectionHeading title="Life Timeline" subtitle="Key dates in Ussher's life and work" />
      <Box mb={8}>
        {TIMELINE.map((t, i) => (
          <Flex
            key={t.year}
            gap={4}
            mb={i < TIMELINE.length - 1 ? 0 : 0}
            position="relative"
          >
            {/* Timeline line */}
            <Flex direction="column" align="center" minW="80px">
              <Box
                w="10px"
                h="10px"
                borderRadius="full"
                bg="#D4AF37"
                border="2px solid"
                borderColor="#8B3A3A"
                zIndex={1}
              />
              {i < TIMELINE.length - 1 && (
                <Box w="2px" bg="#E4E2DC" flex={1} minH="40px" />
              )}
            </Flex>
            <Box pb={4}>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="md"
                fontWeight={700}
                color="#8B3A3A"
              >
                {t.year}
              </Text>
              <Text fontSize="sm" fontWeight={600} color="#2D2A24">
                {t.event}
              </Text>
              <Text fontSize="xs" color="#9E9A90">
                {t.detail}
              </Text>
            </Box>
          </Flex>
        ))}
      </Box>

      {/* Project Mission */}
      <SectionHeading
        title="Our Mission"
        subtitle="What we're building and why"
      />
      <Box
        bg="#2D2A24"
        borderRadius="lg"
        p={6}
        mb={8}
      >
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#D6D3CC"
          lineHeight={1.7}
          fontStyle="italic"
        >
          "To build a scholarly, auditable, multilingual historical knowledge graph
          that modernizes Ussher's chronological synthesis — extending it to every
          continent, every era, and every civilization he could never have known."
        </Text>
        <SimpleGrid columns={{ base: 1, md: 3 }} gap={4} mt={6}>
          {[
            { icon: Globe, label: '199 Countries', desc: '~319 data points per country profile' },
            { icon: Network, label: 'Neo4j Graph', desc: '11 core labels, evidence-first methodology' },
            { icon: Scroll, label: 'Chicago 17', desc: 'Every claim backed by auditable citations' },
          ].map((item) => {
            const Icon = item.icon
            return (
              <Flex key={item.label} align="center" gap={3}>
                <Icon size={20} color="#D4AF37" />
                <Box>
                  <Text fontSize="sm" fontWeight={600} color="#D4AF37">
                    {item.label}
                  </Text>
                  <Text fontSize="xs" color="#B8B2A4">
                    {item.desc}
                  </Text>
                </Box>
              </Flex>
            )
          })}
        </SimpleGrid>
      </Box>

      {/* Roadmap */}
      <SectionHeading
        title="Roadmap to 1 Million Nodes"
        subtitle="From Ussher's 1,600 pages to a living knowledge graph"
      />
      <SimpleGrid columns={{ base: 1, md: 2 }} gap={4} mb={8}>
        {ROADMAP.map((phase) => (
          <Box
            key={phase.phase}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="lg"
            p={5}
            position="relative"
            overflow="hidden"
          >
            <Box
              position="absolute"
              top={0}
              left={0}
              w="100%"
              h="4px"
              bg={phase.color}
            />
            <Flex justify="space-between" align="center" mt={1} mb={2}>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="lg"
                fontWeight={700}
                color={phase.color}
              >
                {phase.phase}: {phase.title}
              </Text>
              <Text
                fontSize="xs"
                fontWeight={700}
                color={phase.color}
                bg={`${phase.color}15`}
                px={2}
                py={0.5}
                borderRadius="full"
              >
                {phase.status}
              </Text>
            </Flex>
            {phase.items.map((item, i) => (
              <Text key={i} fontSize="sm" color="#524E44" mt={1}>
                • {item}
              </Text>
            ))}
          </Box>
        ))}
      </SimpleGrid>

      {/* Graph Schema */}
      <SectionHeading
        title="Knowledge Graph Schema"
        subtitle="11 core labels powering the knowledge graph"
      />
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={3} mb={8}>
        {[
          { label: 'Person', desc: 'Historical figures', color: '#4A90D9' },
          { label: 'Idea', desc: 'Concepts, theories', color: '#D4AF37' },
          { label: 'Institution', desc: 'Organizations, states', color: '#8B3A3A' },
          { label: 'Place', desc: 'Locations, territories', color: '#2F855A' },
          { label: 'Event', desc: 'Discrete occurrences', color: '#D44' },
          { label: 'Movement', desc: 'Cultural, political waves', color: '#6B3FA0' },
          { label: 'Artifact / Text', desc: 'Physical & written objects', color: '#DD6B20' },
          { label: 'Evidence', desc: 'Source citations', color: '#2563A0' },
          { label: 'Corpus', desc: 'Collections of texts', color: '#B83280' },
          { label: 'Timeframe', desc: 'Temporal boundaries', color: '#38A169' },
          { label: 'Framework', desc: 'Analytical lenses', color: '#876322' },
          { label: 'EventWindow', desc: 'Multi-year spans', color: '#5B21B6' },
        ].map((node) => (
          <Box
            key={node.label}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="md"
            p={3}
            textAlign="center"
          >
            <Box
              w="12px"
              h="12px"
              borderRadius="full"
              bg={node.color}
              mx="auto"
              mb={2}
            />
            <Text fontSize="sm" fontWeight={600} color="#2D2A24">
              {node.label}
            </Text>
            <Text fontSize="xs" color="#9E9A90">
              {node.desc}
            </Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Quote Footer */}
      <Box
        bg="#F5F4F0"
        borderRadius="lg"
        p={6}
        border="1px solid"
        borderColor="#E4E2DC"
        textAlign="center"
      >
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          color="#524E44"
          fontStyle="italic"
        >
          "The past is never dead. It's not even past."
        </Text>
        <Text fontSize="sm" color="#96770B" mt={2}>
          — William Faulkner
        </Text>
      </Box>
    </Box>
  )
}
