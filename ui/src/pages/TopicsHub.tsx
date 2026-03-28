/**
 * TopicsHub — landing page listing all civilization-shaping topics.
 * Each card links to its dedicated topic explorer page.
 */
import React from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Heading } from '@chakra-ui/react'
import {
  Swords, Heart, Building2, Wheat, Compass, BookOpen, ChevronRight,
} from 'lucide-react'
import Breadcrumb from '../components/Breadcrumb'
import { TOPIC_REGISTRY } from '../data/catalog/topicRegistry'

const ICONS: Record<string, React.ElementType> = {
  Swords, Heart, Building2, Wheat, Compass, BookOpen,
}

export default function TopicsHub() {
  const total = TOPIC_REGISTRY.reduce((n, t) => n + t.entities.length, 0)

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Civilization Topics' }]} />

      {/* Hero */}
      <Box mb={8} textAlign="center" py={8}
        bg="linear-gradient(135deg, #082340 0%, #1A365D 40%, #2B6CB0 70%, #D4AF37 100%)"
        borderRadius="2xl" border="1px solid #D4AF37">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }}
          fontWeight={700} color="#FAFAF8" mb={3}>
          Forces That Shaped Civilization
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#E4E2DC" maxW="700px" mx="auto" lineHeight={1.8} mb={3}>
          Six dimensions of human ingenuity — each one an axis on which civilization turns.
          Explore them by era, by category, or dive into the catalog.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#90CDF4">
          {TOPIC_REGISTRY.length} topics · {total} milestones · Every era of human history
        </Text>
      </Box>

      {/* Topic Cards */}
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={5}>
        {TOPIC_REGISTRY.map(topic => {
          const Icon = ICONS[topic.icon] || BookOpen
          return (
            <RouterLink key={topic.slug} to={topic.route} style={{ textDecoration: 'none' }}>
              <Box
                bg="white" border="1px solid #E4E2DC" borderRadius="xl"
                p={5} h="100%" cursor="pointer" transition="all 0.2s"
                borderTop="4px solid" borderTopColor={topic.color}
                _hover={{ shadow: 'lg', borderColor: '#D4AF37', transform: 'translateY(-2px)' }}
              >
                <Flex align="center" gap={3} mb={3}>
                  <Box p={2} borderRadius="lg" bg={`${topic.color}15`}>
                    <Icon size={20} color={topic.color} />
                  </Box>
                  <Box flex={1}>
                    <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color="#2D2A24">
                      {topic.name}
                    </Text>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">
                      {topic.entities.length} milestones · All eras
                    </Text>
                  </Box>
                  <ChevronRight size={16} color="#9E9A90" />
                </Flex>
                <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.6}>
                  {topic.description}
                </Text>
              </Box>
            </RouterLink>
          )
        })}
      </SimpleGrid>
    </Box>
  )
}
