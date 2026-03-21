/* ─── Civilization Gallery — Stock photos for eras/civilizations ─── */
import React, { useState } from 'react'
import { Box, Text, Flex, SimpleGrid, Heading } from '@chakra-ui/react'
import { Image, ChevronRight, MapPin, Clock, Star } from 'lucide-react'
import type { Civilization, StockImage } from '../types'

interface CivilizationGalleryProps {
  civilizations: Civilization[]
  eraColor?: string
}

export default function CivilizationGallery({ civilizations, eraColor = '#D4AF37' }: CivilizationGalleryProps) {
  const [selected, setSelected] = useState<Civilization | null>(null)
  const [lightboxImage, setLightboxImage] = useState<StockImage | null>(null)

  return (
    <Box>
      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={5}>
        {civilizations.map(civ => (
          <Box
            key={civ.id}
            bg="white"
            border="1px solid"
            borderColor={selected?.id === civ.id ? eraColor : '#E4E2DC'}
            borderRadius="lg"
            overflow="hidden"
            cursor="pointer"
            transition="all 0.3s"
            _hover={{ borderColor: eraColor, transform: 'translateY(-3px)', boxShadow: '0 8px 24px rgba(0,0,0,0.1)' }}
            onClick={() => setSelected(selected?.id === civ.id ? null : civ)}
          >
            {/* Hero image */}
            {civ.images[0] && (
              <Box h="180px" overflow="hidden" position="relative">
                <img
                  src={civ.images[0].url}
                  alt={civ.images[0].alt}
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                  loading="lazy"
                />
                <Box
                  position="absolute" bottom={0} left={0} right={0}
                  bg="linear-gradient(transparent, rgba(44,24,16,0.8))"
                  p={3}
                >
                  <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color="white">
                    {civ.name}
                  </Text>
                </Box>
              </Box>
            )}

            {!civ.images[0] && (
              <Box h="140px" bg="#F5F4F0" display="flex" alignItems="center" justifyContent="center">
                <Image size={40} color="#D6D3CC" />
                <Box ml={3}>
                  <Text fontFamily='"Cinzel", serif' fontSize="md" fontWeight={700} color="#2D2A24">{civ.name}</Text>
                </Box>
              </Box>
            )}

            {/* Info */}
            <Box p={4}>
              <Flex gap={2} mb={2} flexWrap="wrap">
                <Flex align="center" gap={1}>
                  <MapPin size={12} color={eraColor} />
                  <Text fontSize="xs" color="#9E9A90">{civ.region}</Text>
                </Flex>
                <Flex align="center" gap={1}>
                  <Clock size={12} color={eraColor} />
                  <Text fontSize="xs" color="#9E9A90">{civ.period}</Text>
                </Flex>
              </Flex>
              <Text fontSize="sm" color="#524E44" lineHeight={1.5} lineClamp={3}>
                {civ.description}
              </Text>
              {civ.images.length > 1 && (
                <Text fontSize="xs" color={eraColor} mt={2} fontWeight={600}>
                  {civ.images.length} photos · Click to explore
                </Text>
              )}
            </Box>
          </Box>
        ))}
      </SimpleGrid>

      {/* Expanded Detail View */}
      {selected && (
        <Box mt={6} bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="xl" p={6}>
          <Flex justify="space-between" align="flex-start" mb={4}>
            <Box>
              <Heading fontFamily='"Cinzel", serif' fontSize="xl" color="#2D2A24">{selected.name}</Heading>
              <Flex gap={3} mt={1}>
                <Text fontSize="sm" color="#9E9A90">{selected.region}</Text>
                <Text fontSize="sm" color="#96770B">·</Text>
                <Text fontSize="sm" color="#9E9A90">{selected.period}</Text>
              </Flex>
            </Box>
            <Box cursor="pointer" onClick={() => setSelected(null)} color="#9E9A90" _hover={{ color: '#C53030' }}>✕</Box>
          </Flex>

          <Text fontSize="sm" color="#524E44" lineHeight={1.7} mb={4}>{selected.description}</Text>

          {/* Key Facts */}
          <Box mb={4}>
            <Text fontSize="xs" fontWeight={700} color="#96770B" mb={2} textTransform="uppercase" letterSpacing="0.05em">Key Facts</Text>
            {selected.keyFacts.map((fact, i) => (
              <Flex key={i} align="flex-start" gap={2} mb={1.5}>
                <Star size={10} color={eraColor} style={{ marginTop: 4, flexShrink: 0 }} />
                <Text fontSize="sm" color="#2D2A24">{fact}</Text>
              </Flex>
            ))}
          </Box>

          {/* Image Gallery */}
          {selected.images.length > 0 && (
            <Box>
              <Text fontSize="xs" fontWeight={700} color="#96770B" mb={2} textTransform="uppercase" letterSpacing="0.05em">
                Gallery ({selected.images.length} images)
              </Text>
              <SimpleGrid columns={{ base: 2, md: 3, lg: 4 }} gap={3}>
                {selected.images.map(img => (
                  <Box
                    key={img.id}
                    borderRadius="lg" overflow="hidden" cursor="pointer"
                    border="2px solid transparent"
                    _hover={{ borderColor: eraColor, transform: 'scale(1.02)' }}
                    transition="all 0.2s"
                    onClick={() => setLightboxImage(img)}
                  >
                    <img
                      src={img.url}
                      alt={img.alt}
                      style={{ width: '100%', height: '120px', objectFit: 'cover' }}
                      loading="lazy"
                    />
                    <Box p={2} bg="#FAFAF8">
                      <Text fontSize="xs" color="#524E44" lineClamp={1}>{img.alt}</Text>
                      <Text fontSize="xs" color="#96770B">{img.category}</Text>
                    </Box>
                  </Box>
                ))}
              </SimpleGrid>
            </Box>
          )}
        </Box>
      )}

      {/* Lightbox */}
      {lightboxImage && (
        <Flex
          position="fixed" top={0} left={0} right={0} bottom={0}
          bg="rgba(0,0,0,0.9)" zIndex={2000}
          align="center" justify="center"
          onClick={() => setLightboxImage(null)}
          cursor="pointer"
        >
          <Box maxW="90vw" maxH="90vh" position="relative">
            <img
              src={lightboxImage.url}
              alt={lightboxImage.alt}
              style={{ maxWidth: '100%', maxHeight: '85vh', objectFit: 'contain', borderRadius: '8px' }}
            />
            <Box position="absolute" bottom={-8} left={0} right={0} textAlign="center">
              <Text color="white" fontSize="sm" fontWeight={600}>{lightboxImage.alt}</Text>
              <Text color="#D6D3CC" fontSize="xs">{lightboxImage.credit}</Text>
            </Box>
          </Box>
        </Flex>
      )}
    </Box>
  )
}
