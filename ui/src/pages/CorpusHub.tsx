/**
 * CorpusHub — landing page listing all corpus collections.
 * Fetches entity counts from the Appwrite backend.
 */
import React, { useState, useEffect } from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { Box, Flex, Text, SimpleGrid, Heading, Spinner } from '@chakra-ui/react'
import { Library, ChevronRight } from 'lucide-react'
import Breadcrumb from '../components/Breadcrumb'
import { CORPUS_META } from '../constants/corpusMeta'
import { fetchTotalCount } from '../services/entityService'

export default function CorpusHub() {
  const [totalEntities, setTotalEntities] = useState(0)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchTotalCount().then(n => {
      setTotalEntities(n)
      setLoading(false)
    })
  }, [])

  return (
    <Box>
      <Breadcrumb items={[{ label: 'Corpus Collections' }]} />

      {/* Hero */}
      <Box mb={8} textAlign="center" py={8}
        bg="linear-gradient(135deg, #2D2A24 0%, #3A2A1A 40%, #8B3A3A 70%, #D4AF37 100%)"
        borderRadius="2xl" border="1px solid #D4AF37">
        <Heading fontFamily='"Cinzel", serif' fontSize={{ base: '2xl', md: '4xl' }}
          fontWeight={700} color="#FAFAF8" mb={3}>
          The World's Corpuses
        </Heading>
        <Text fontFamily='"Cormorant Garamond", serif' fontSize={{ base: 'lg', md: 'xl' }}
          color="#E4E2DC" maxW="700px" mx="auto" lineHeight={1.8} mb={3}>
          Fourteen textual traditions spanning every civilization — from cuneiform
          tablets to scientific treatises. Each corpus is a window into a culture's soul.
        </Text>
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#D4AF37">
          {CORPUS_META.length} corpuses · {loading ? '…' : totalEntities.toLocaleString()} entities in the Annals backend
        </Text>
      </Box>

      {/* Loading */}
      {loading && (
        <Flex justify="center" py={8}>
          <Spinner color="#D4AF37" size="lg" />
        </Flex>
      )}

      {/* Corpus Cards */}
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={5}>
        {CORPUS_META.map(corpus => (
          <RouterLink key={corpus.slug} to={`/corpus/${corpus.slug}`} style={{ textDecoration: 'none' }}>
            <Box
              bg="white" border="1px solid #E4E2DC" borderRadius="xl"
              p={5} h="100%" cursor="pointer" transition="all 0.2s"
              borderTop="4px solid" borderTopColor={corpus.color}
              _hover={{ shadow: 'lg', borderColor: '#D4AF37', transform: 'translateY(-2px)' }}
            >
              <Flex align="center" gap={3} mb={3}>
                <Box p={2} borderRadius="lg" bg={`${corpus.color}15`}>
                  <Library size={20} color={corpus.color} />
                </Box>
                <Box flex={1}>
                  <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color="#2D2A24">
                    {corpus.shortName}
                  </Text>
                  <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90">
                    {corpus.zone}
                  </Text>
                </Box>
                <ChevronRight size={16} color="#9E9A90" />
              </Flex>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.6}>
                {corpus.description}
              </Text>
            </Box>
          </RouterLink>
        ))}
      </SimpleGrid>
    </Box>
  )
}
