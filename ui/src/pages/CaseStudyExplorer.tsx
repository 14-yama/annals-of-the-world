/* ─── Case Study Explorer — Annals of the World ─── */
import React, { useState } from 'react'
import { Box, Flex, Heading, Text, SimpleGrid, Badge } from '@chakra-ui/react'
import { BookOpen, Zap, Globe, ArrowRight, ChevronDown, ChevronUp, Swords, Pyramid, Ship, Crown, Landmark, MapPin } from 'lucide-react'
import { SectionHeading } from '../components/DataCards'
import Breadcrumb from '../components/Breadcrumb'
import CausalChain from '../components/CausalChain'
import { CASE_STUDIES } from '../data/case-studies'
import { FRAMEWORKS, FRAMEWORK_MAP } from '../constants/frameworks'
import type { CaseStudy } from '../types'

export default function CaseStudyExplorer() {
  const [selectedStudy, setSelectedStudy] = useState<CaseStudy>(CASE_STUDIES[0])
  const [expandInsight, setExpandInsight] = useState(false)
  const [showFrameworks, setShowFrameworks] = useState(false)

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Frameworks' }]} />
      {/* Header */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Zap size={28} color="#E53E3E" />
          <Heading fontFamily='"Cinzel", serif' fontSize="3xl" fontWeight={700} color="#2D2A24">
            Frameworks in Action
          </Heading>
        </Flex>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#524E44" maxW="700px">
          Explore how historical events connect through cause-and-effect chains,
          cultural diffusion, geopolitical linkage, and 7 other interpretive frameworks
          from the Annals knowledge graph.
        </Text>
      </Box>

      {/* Case Study Selector */}
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={4} mb={8}>
        {CASE_STUDIES.map(cs => {
          const iconMap: Record<string, React.ReactNode> = {
            'route-to-india': <Globe size={20} color="#C53030" />,
            'singapore-rise': <Zap size={20} color="#4A90D9" />,
            'world-wars-origins': <Swords size={20} color="#C53030" />,
            'mesopotamian-stratification': <Pyramid size={20} color="#8B3A3A" />,
            'oceania-migration': <Ship size={20} color="#2B6CB0" />,
            'mansa-musa-effect': <Crown size={20} color="#D4AF37" />,
            'maya-collapse': <Landmark size={20} color="#2F855A" />,
            'silk-road-culture': <MapPin size={20} color="#DD6B20" />,
          }
          return (
            <Box
              key={cs.id}
              p={5}
              bg={selectedStudy.id === cs.id ? '#FAFAF8' : '#FDFAF5'}
              border="2px solid"
              borderColor={selectedStudy.id === cs.id ? '#D4AF37' : '#E4E2DC'}
              borderRadius="xl"
              cursor="pointer"
              onClick={() => setSelectedStudy(cs)}
              transition="all 0.2s"
              _hover={{ borderColor: '#D4AF37', transform: 'translateY(-2px)', boxShadow: 'md' }}
            >
              <Flex align="center" gap={2} mb={2}>
                {iconMap[cs.id] || <Zap size={20} color="#888" />}
                <Heading fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
                  {cs.title}
                </Heading>
              </Flex>
              <Text fontSize="sm" color="#9E9A90" fontFamily='"Inter", sans-serif' fontStyle="italic" mb={2}>
                {cs.subtitle}
              </Text>
              <Flex gap={2} flexWrap="wrap">
                {cs.frameworks.map(fId => {
                  const fw = FRAMEWORK_MAP[fId]
                  return (
                    <Badge
                      key={fId}
                      bg={fw?.color || '#888'}
                      color="white"
                      fontSize="10px"
                      px={2}
                      py={0.5}
                      borderRadius="full"
                    >
                      {fw?.name || fId}
                    </Badge>
                  )
                })}
              </Flex>
              <Text fontSize="xs" color="#6B5744" mt={2}>
                {cs.nodes.length} events · {cs.edges.length} connections
              </Text>
            </Box>
          )
        })}
      </SimpleGrid>

      {/* Selected Case Study */}
      <Box bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="xl" p={6} mb={8}>
        <Heading fontFamily='"Cormorant Garamond", serif' fontSize="2xl" fontWeight={700} color="#2D2A24" mb={2}>
          {selectedStudy.title}
        </Heading>
        <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" mb={4} lineHeight={1.7}>
          {selectedStudy.description}
        </Text>

        {/* Key Insight */}
        <Box
          bg="#FDF8ED"
          border="1px solid #D4AF37"
          borderRadius="lg"
          p={4}
          mb={6}
          cursor="pointer"
          onClick={() => setExpandInsight(!expandInsight)}
        >
          <Flex align="center" justify="space-between">
            <Flex align="center" gap={2}>
              <BookOpen size={16} color="#D4AF37" />
              <Text fontFamily='"Cormorant Garamond", serif' fontWeight={700} fontSize="md" color="#4A310D">
                Key Insight
              </Text>
            </Flex>
            {expandInsight ? <ChevronUp size={16} color="#9E9A90" /> : <ChevronDown size={16} color="#9E9A90" />}
          </Flex>
          {expandInsight && (
            <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" mt={3} lineHeight={1.7}>
              {selectedStudy.keyInsight}
            </Text>
          )}
        </Box>

        {/* Causal Chain Visualization */}
        <Box mb={6}>
          <SectionHeading title="Causal Chain" subtitle="Hover over nodes and edges for details and evidence." />
          <Box bg="#FFF" border="1px solid #E4E2DC" borderRadius="lg" overflow="hidden" mt={4}>
            <CausalChain caseStudy={selectedStudy} />
          </Box>
        </Box>

        {/* Event Timeline List */}
        <SectionHeading title="Event Sequence" subtitle="Chronological breakdown with framework lenses" />
        <Box mt={4}>
          {[...selectedStudy.nodes].sort((a, b) => a.year - b.year).map((node, i) => {
            const fw = FRAMEWORK_MAP[node.framework]
            const outEdges = selectedStudy.edges.filter(e => e.source === node.id)
            return (
              <Flex key={node.id} gap={4} mb={4} align="stretch">
                {/* Timeline spine */}
                <Flex direction="column" align="center" minW="50px">
                  <Box
                    w="12px" h="12px" borderRadius="full"
                    bg={fw?.color || '#888'} border="2px solid" borderColor={fw?.color || '#888'}
                  />
                  {i < selectedStudy.nodes.length - 1 && (
                    <Box w="2px" flex={1} bg="#E4E2DC" />
                  )}
                </Flex>

                {/* Content */}
                <Box pb={4} flex={1}>
                  <Flex align="center" gap={2} mb={1}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" fontWeight={600}>
                      {node.year < 0 ? `${Math.abs(node.year)} BCE` : `${node.year} CE`}
                    </Text>
                    <Badge bg={fw?.color || '#888'} color="white" fontSize="9px" px={2} py={0} borderRadius="full">
                      {fw?.name || node.framework}
                    </Badge>
                  </Flex>
                  <Text fontFamily='"Cormorant Garamond", serif' fontWeight={700} fontSize="md" color="#2D2A24">
                    {node.title}
                  </Text>
                  <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.6} mt={1}>
                    {node.description}
                  </Text>
                  {outEdges.length > 0 && (
                    <Flex gap={2} mt={2} flexWrap="wrap">
                      {outEdges.map(e => {
                        const tgtNode = selectedStudy.nodes.find(n => n.id === e.target)
                        return (
                          <Flex key={`${e.source}-${e.target}`} align="center" gap={1}>
                            <ArrowRight size={12} color={FRAMEWORK_MAP[e.framework]?.color || '#888'} />
                            <Text fontSize="xs" color="#9E9A90">
                              <Text as="span" fontWeight={700} fontFamily='"JetBrains Mono", monospace'>{e.verb}</Text>
                              {' → '}{tgtNode?.title || e.target}
                            </Text>
                          </Flex>
                        )
                      })}
                    </Flex>
                  )}
                </Box>
              </Flex>
            )
          })}
        </Box>
      </Box>

      {/* Framework Legend */}
      <Box mb={8}>
        <Box
          cursor="pointer"
          onClick={() => setShowFrameworks(!showFrameworks)}
          mb={4}
        >
          <Flex align="center" gap={2}>
            <SectionHeading title="16 Interpretive Frameworks" subtitle="The lenses used to analyze historical causation" />
            {showFrameworks ? <ChevronUp size={20} color="#9E9A90" /> : <ChevronDown size={20} color="#9E9A90" />}
          </Flex>
        </Box>
        {showFrameworks && (
          <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={4}>
            {FRAMEWORKS.map(fw => (
              <Box key={fw.id} p={4} bg="#FDFAF5" border="1px solid #E4E2DC" borderRadius="lg">
                <Flex align="center" gap={2} mb={2}>
                  <Box w="10px" h="10px" borderRadius="full" bg={fw.color} />
                  <Text fontFamily='"Cormorant Garamond", serif' fontWeight={700} fontSize="md" color="#2D2A24">
                    {fw.name}
                  </Text>
                </Flex>
                <Text fontFamily='"Inter", sans-serif' fontSize="xs" color="#524E44" lineHeight={1.5} mb={2}>
                  {fw.description}
                </Text>
                <Flex gap={1} flexWrap="wrap">
                  {fw.verbs.map(v => (
                    <Badge key={v} variant="subtle" fontSize="9px" fontFamily='"JetBrains Mono", monospace'>
                      {v}
                    </Badge>
                  ))}
                </Flex>
              </Box>
            ))}
          </SimpleGrid>
        )}
      </Box>
    </Box>
  )
}
