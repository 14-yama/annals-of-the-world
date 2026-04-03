/**
 * EntityLegacy — Legacy & Influence tab for an entity
 *
 * Shows downstream impact: expanded effects, reverse-lookup of entities
 * that cite this entity in their causes, and a "named after" section.
 */
import React, { useMemo } from 'react'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import { Link as RouterLink } from 'react-router-dom'
import { Sparkles, ArrowRight, ExternalLink, TrendingUp } from 'lucide-react'
import { getAllEntities } from '../data/catalog'
import type { Entity } from '../data/entityTypes'

interface Props {
  entity: Entity
}

const EntityLegacy: React.FC<Props> = ({ entity }) => {
  // Build reverse-lookup: entities whose causes reference this entity
  const influencedEntities = useMemo(() => {
    const all = getAllEntities()
    return all.filter(e =>
      e.slug !== entity.slug &&
      e.causes.some(c => c.slug === entity.slug || c.title.toLowerCase().includes(entity.name.toLowerCase()))
    ).slice(0, 20)
  }, [entity.slug, entity.name])

  // Entities referenced in our effects
  const effectEntities = useMemo(() => {
    const all = getAllEntities()
    const effectSlugs = entity.effects.filter(e => e.slug).map(e => e.slug!)
    return all.filter(e => effectSlugs.includes(e.slug))
  }, [entity.effects])

  const hasContent = entity.effects.length > 0 || influencedEntities.length > 0 || entity.legacySummary

  if (!hasContent) {
    return (
      <Flex direction="column" align="center" justify="center" minH="250px" gap={4}>
        <Sparkles size={48} color="#D6D3CC" />
        <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
          letterSpacing="0.1em" textTransform="uppercase">Legacy Not Yet Documented</Text>
        <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
          Add effects and causal links to other entities to populate this view.
        </Text>
      </Flex>
    )
  }

  return (
    <Box py={4}>
      {/* Header */}
      <Flex align="center" gap={2} mb={6}>
        <Sparkles size={16} color="#D4AF37" />
        <Text fontFamily='"Cinzel", serif' fontSize="xs" color="#9E9A90"
          letterSpacing="0.12em" textTransform="uppercase">Legacy &amp; Influence</Text>
        <Box flex={1} h="1px" bg="#E4E2DC" />
      </Flex>

      {/* Legacy summary */}
      {entity.legacySummary && (
        <Box bg="rgba(212,175,55,0.04)" border="1px solid rgba(212,175,55,0.15)"
          borderRadius="lg" p={5} mb={6}>
          <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" color="#2D2A24"
            lineHeight="1.7" fontStyle="italic">
            {entity.legacySummary}
          </Text>
        </Box>
      )}

      {/* Quote */}
      {entity.quote && (
        <Box borderLeft="3px solid #D4AF37" pl={5} mb={6} py={2}>
          <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" color="#2D2A24"
            lineHeight="1.6" fontStyle="italic">
            &ldquo;{entity.quote}&rdquo;
          </Text>
          <Text fontSize="xs" color="#9E9A90" mt={2}>— {entity.name}</Text>
        </Box>
      )}

      {/* Direct Effects */}
      {entity.effects.length > 0 && (
        <Box mb={6}>
          <Flex align="center" gap={2} mb={3}>
            <TrendingUp size={14} color="#6B3FA0" />
            <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#9E9A90"
              letterSpacing="0.12em" textTransform="uppercase">
              Consequences &amp; Outcomes ({entity.effects.length})
            </Text>
          </Flex>
          {entity.effects.map((effect, i) => {
            const linkedEntity = effectEntities.find(e => e.slug === effect.slug)
            return (
              <Flex key={i} align="center" gap={3} py={3} borderBottom="1px solid #EEEDEA">
                <Box w="8px" h="8px" borderRadius="full" bg="#6B3FA0" flexShrink={0} />
                <Box flex={1}>
                  <Flex align="center" gap={2}>
                    {linkedEntity ? (
                      <RouterLink to={`/entity/${linkedEntity.slug}`} style={{ textDecoration: 'none' }}>
                        <Flex align="center" gap={1}>
                          <Text fontSize="sm" fontWeight={600} color="#3B6BC2" cursor="pointer">
                            {effect.title}
                          </Text>
                          <ExternalLink size={10} color="#3B6BC2" />
                        </Flex>
                      </RouterLink>
                    ) : (
                      <Text fontSize="sm" fontWeight={600} color="#2D2A24">{effect.title}</Text>
                    )}
                    <Box bg="rgba(107,63,160,0.1)" border="1px solid rgba(107,63,160,0.25)"
                      borderRadius="4px" px={2} py={0.5}>
                      <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" fontWeight={600}
                        color="#6B3FA0" letterSpacing="0.05em">{effect.type}</Text>
                    </Box>
                  </Flex>
                  <Text fontSize="xs" color="#9E9A90" mt={0.5}>{effect.year}</Text>
                </Box>
                <ArrowRight size={12} color="#D6D3CC" />
              </Flex>
            )
          })}
        </Box>
      )}

      {/* Influenced Entities (reverse-lookup) */}
      {influencedEntities.length > 0 && (
        <Box>
          <Flex align="center" gap={2} mb={3}>
            <Sparkles size={14} color="#D4AF37" />
            <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#9E9A90"
              letterSpacing="0.12em" textTransform="uppercase">
              Entities Influenced by {entity.name} ({influencedEntities.length})
            </Text>
          </Flex>
          <SimpleGrid columns={{ base: 1, sm: 2 }} gap={3}>
            {influencedEntities.map(e => (
              <RouterLink key={e.slug} to={`/entity/${e.slug}`} style={{ textDecoration: 'none' }}>
                <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={4}
                  cursor="pointer" transition="all 0.2s"
                  _hover={{ borderColor: '#D4AF37', bg: 'rgba(212,175,55,0.03)' }}>
                  <Flex align="center" gap={2} mb={1}>
                    <Box w="6px" h="6px" borderRadius="full"
                      bg={e.label === 'Person' ? '#3A7D44' : e.label === 'EventWindow' ? '#C5963A' : '#9E9A90'} />
                    <Text fontFamily='"Cinzel", serif' fontSize="10px" color="#9E9A90"
                      letterSpacing="0.08em" textTransform="uppercase">{e.label}</Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4" ml="auto">
                      {e.callNumber.split('-')[0]}
                    </Text>
                  </Flex>
                  <Text fontSize="sm" fontWeight={600} color="#2D2A24">{e.name}</Text>
                  <Text fontSize="xs" color="#9E9A90" mt={1} lineClamp={2}>
                    {e.summary.slice(0, 100)}…
                  </Text>
                </Box>
              </RouterLink>
            ))}
          </SimpleGrid>
        </Box>
      )}
    </Box>
  )
}

export default EntityLegacy
