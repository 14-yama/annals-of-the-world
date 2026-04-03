/**
 * EntityTimeline — Chronological lifeline for an entity
 *
 * Renders a vertical timeline from causes → born/startDate → effects → died/endDate.
 * Uses existing entity data (no Appwrite dependency for now).
 */
import React from 'react'
import { Box, Flex, Text } from '@chakra-ui/react'
import { Clock, ArrowRight, Zap } from 'lucide-react'
import type { Entity } from '../data/entityTypes'

interface Props {
  entity: Entity
}

interface TimelineNode {
  year: string
  label: string
  detail: string
  type: 'birth' | 'cause' | 'event' | 'effect' | 'death' | 'milestone'
}

function buildTimeline(entity: Entity): TimelineNode[] {
  const nodes: TimelineNode[] = []

  // Birth / founding / start
  if (entity.born)      nodes.push({ year: extractYear(entity.born), label: 'Born', detail: entity.born, type: 'birth' })
  if (entity.founded)   nodes.push({ year: extractYear(entity.founded), label: 'Founded', detail: entity.founded, type: 'birth' })
  if (entity.startDate) nodes.push({ year: entity.startDate, label: 'Begins', detail: `${entity.name} begins`, type: 'birth' })

  // Causes (antecedents)
  entity.causes.forEach(c => {
    nodes.push({ year: c.year, label: c.title, detail: `${c.type} — ${c.title}`, type: 'cause' })
  })

  // Effects (consequences)
  entity.effects.forEach(e => {
    nodes.push({ year: e.year, label: e.title, detail: `${e.type} — ${e.title}`, type: 'effect' })
  })

  // Death / end
  if (entity.died)    nodes.push({ year: extractYear(entity.died), label: 'Died', detail: entity.died, type: 'death' })
  if (entity.endDate) nodes.push({ year: entity.endDate, label: 'Ends', detail: `${entity.name} ends`, type: 'death' })

  // Sort by year (numeric extraction)
  return nodes.sort((a, b) => parseNumericYear(a.year) - parseNumericYear(b.year))
}

function extractYear(s: string): string {
  const match = s.match(/\d{1,4}\s*(BCE|CE|BC|AD)?/i)
  return match ? match[0] : s.split(',')[0].trim()
}

function parseNumericYear(s: string): number {
  const cleaned = s.replace(/[^0-9BCE-]/gi, '')
  const match = cleaned.match(/(\d+)\s*(BCE|BC)?/i)
  if (!match) return 0
  const num = parseInt(match[1])
  return match[2] ? -num : num
}

const TYPE_COLORS: Record<string, string> = {
  birth: '#3A7D44',
  cause: '#C5963A',
  event: '#3B6BC2',
  effect: '#6B3FA0',
  death: '#8B3A3A',
  milestone: '#D4AF37',
}

const EntityTimeline: React.FC<Props> = ({ entity }) => {
  const timeline = buildTimeline(entity)

  if (timeline.length === 0) {
    return (
      <Flex direction="column" align="center" justify="center" minH="250px" gap={4}>
        <Clock size={48} color="#D6D3CC" />
        <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
          letterSpacing="0.1em" textTransform="uppercase">No Timeline Data</Text>
        <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
          Add birth/death dates, causes, and effects to populate the timeline.
        </Text>
      </Flex>
    )
  }

  return (
    <Box py={4}>
      <Flex align="center" gap={2} mb={6}>
        <Clock size={16} color="#D4AF37" />
        <Text fontFamily='"Cinzel", serif' fontSize="xs" color="#9E9A90"
          letterSpacing="0.12em" textTransform="uppercase">Chronological Lifeline</Text>
        <Box flex={1} h="1px" bg="#E4E2DC" />
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#B8B2A4">
          {timeline.length} events
        </Text>
      </Flex>

      {/* Vertical timeline */}
      <Box position="relative" pl={8}>
        {/* Vertical line */}
        <Box position="absolute" left="15px" top="0" bottom="0" w="2px" bg="#E4E2DC" />

        {timeline.map((node, i) => (
          <Flex key={i} position="relative" mb={6} align="flex-start">
            {/* Dot */}
            <Box
              position="absolute"
              left="-25px"
              top="6px"
              w="12px"
              h="12px"
              borderRadius="full"
              bg={TYPE_COLORS[node.type] || '#9E9A90'}
              border="2px solid #FAF3E8"
              boxShadow={`0 0 0 2px ${TYPE_COLORS[node.type] || '#9E9A90'}33`}
            />

            {/* Content */}
            <Box
              bg="#FAFAF8"
              border="1px solid #E4E2DC"
              borderRadius="lg"
              p={4}
              flex={1}
              ml={2}
              transition="all 0.2s"
              _hover={{ borderColor: TYPE_COLORS[node.type] || '#D4AF37', bg: 'rgba(212,175,55,0.02)' }}
            >
              <Flex align="center" gap={2} mb={1}>
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="11px" fontWeight={700}
                  color={TYPE_COLORS[node.type] || '#9E9A90'}>
                  {node.year}
                </Text>
                <Box bg={`${TYPE_COLORS[node.type]}15`} border={`1px solid ${TYPE_COLORS[node.type]}30`}
                  borderRadius="4px" px={2} py={0.5}>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" fontWeight={600}
                    color={TYPE_COLORS[node.type]} letterSpacing="0.05em" textTransform="uppercase">
                    {node.type}
                  </Text>
                </Box>
                {node.type === 'effect' && <ArrowRight size={10} color="#6B3FA0" />}
                {node.type === 'cause' && <Zap size={10} color="#C5963A" />}
              </Flex>
              <Text fontSize="sm" fontWeight={600} color="#2D2A24">{node.label}</Text>
              {node.detail !== node.label && (
                <Text fontSize="xs" color="#9E9A90" mt={1}>{node.detail}</Text>
              )}
            </Box>
          </Flex>
        ))}
      </Box>
    </Box>
  )
}

export default EntityTimeline
