/**
 * EntityGallery — Media & image gallery for an entity
 *
 * Shows images from Appwrite Storage (when available) or placeholder state.
 * Supports lightbox viewing and Wikimedia Commons integration.
 */
import React, { useState, useEffect } from 'react'
import { Box, Flex, Text, SimpleGrid } from '@chakra-ui/react'
import { Image, Camera, ExternalLink, X } from 'lucide-react'
import { fetchMedia, type MediaRecord } from '../services/entityService'
import type { Entity } from '../data/entityTypes'

interface Props {
  entity: Entity
}

const CATEGORY_LABELS: Record<string, string> = {
  portrait:     'Portrait',
  artifact:     'Artifact',
  map:          'Map',
  architecture: 'Architecture',
  landscape:    'Landscape',
  art:          'Artwork',
}

const EntityGallery: React.FC<Props> = ({ entity }) => {
  const [media, setMedia] = useState<MediaRecord[]>([])
  const [loading, setLoading] = useState(true)
  const [lightbox, setLightbox] = useState<MediaRecord | null>(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    fetchMedia(entity.slug).then(items => {
      if (!cancelled) {
        setMedia(items)
        setLoading(false)
      }
    })
    return () => { cancelled = true }
  }, [entity.slug])

  // If entity has an imageUrl, use it as a fallback hero image
  const heroImage = entity.imageUrl
  const hasContent = media.length > 0 || heroImage

  if (!loading && !hasContent) {
    return (
      <Flex direction="column" align="center" justify="center" minH="250px" gap={4}>
        <Camera size={48} color="#D6D3CC" />
        <Text fontFamily='"Cinzel", serif' fontSize="sm" color="#9E9A90"
          letterSpacing="0.1em" textTransform="uppercase">No Media Available</Text>
        <Text fontSize="xs" color="#B8B2A4" textAlign="center" maxW="400px">
          Images, maps, and artifacts will appear here once curated.
          {entity.wikidataQid && (
            <> Check <a
              href={`https://commons.wikimedia.org/wiki/Special:Search?search=${encodeURIComponent(entity.name)}`}
              target="_blank" rel="noopener noreferrer"
              style={{ color: '#3B6BC2', textDecoration: 'underline' }}
            >Wikimedia Commons</a> for potential media.</>
          )}
        </Text>
      </Flex>
    )
  }

  return (
    <Box py={4}>
      <Flex align="center" gap={2} mb={6}>
        <Image size={16} color="#D4AF37" />
        <Text fontFamily='"Cinzel", serif' fontSize="xs" color="#9E9A90"
          letterSpacing="0.12em" textTransform="uppercase">Media &amp; Gallery</Text>
        <Box flex={1} h="1px" bg="#E4E2DC" />
        <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#B8B2A4">
          {media.length + (heroImage ? 1 : 0)} items
        </Text>
      </Flex>

      {loading ? (
        <Flex justify="center" py={8}>
          <Text fontSize="xs" color="#B8B2A4">Loading media…</Text>
        </Flex>
      ) : (
        <SimpleGrid columns={{ base: 1, sm: 2, md: 3 }} gap={4}>
          {/* Hero image from entity */}
          {heroImage && (
            <Box
              borderRadius="lg" overflow="hidden" border="1px solid #E4E2DC"
              cursor="pointer" transition="all 0.2s"
              _hover={{ borderColor: '#D4AF37', transform: 'scale(1.02)' }}
              onClick={() => setLightbox({ id: 'hero', entitySlug: entity.slug, url: heroImage, alt: entity.name, category: 'portrait' })}
            >
              <img src={heroImage} alt={entity.name}
                style={{ width: '100%', height: '200px', objectFit: 'cover' }}
              />
              <Box p={3} bg="#FAFAF8">
                <Text fontSize="sm" fontWeight={600} color="#2D2A24">{entity.name}</Text>
                <Text fontSize="xs" color="#9E9A90">Primary image</Text>
              </Box>
            </Box>
          )}

          {/* Appwrite media records */}
          {media.map(item => (
            <Box
              key={item.id}
              borderRadius="lg" overflow="hidden" border="1px solid #E4E2DC"
              cursor="pointer" transition="all 0.2s"
              _hover={{ borderColor: '#D4AF37', transform: 'scale(1.02)' }}
              onClick={() => setLightbox(item)}
            >
              <img src={item.url} alt={item.alt}
                style={{ width: '100%', height: '200px', objectFit: 'cover' }}
              />
              <Box p={3} bg="#FAFAF8">
                <Flex align="center" gap={2} mb={1}>
                  <Box bg="rgba(212,175,55,0.1)" border="1px solid rgba(212,175,55,0.25)"
                    borderRadius="4px" px={2} py={0.5}>
                    <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" fontWeight={600}
                      color="#96770B" letterSpacing="0.05em" textTransform="uppercase">
                      {CATEGORY_LABELS[item.category] || item.category}
                    </Text>
                  </Box>
                </Flex>
                <Text fontSize="sm" fontWeight={600} color="#2D2A24">{item.alt}</Text>
                {item.credit && (
                  <Text fontSize="xs" color="#9E9A90" mt={1}>© {item.credit}</Text>
                )}
              </Box>
            </Box>
          ))}
        </SimpleGrid>
      )}

      {/* Lightbox overlay */}
      {lightbox && (
        <Box
          position="fixed" top={0} left={0} right={0} bottom={0}
          bg="rgba(0,0,0,0.85)" zIndex={9999}
          display="flex" alignItems="center" justifyContent="center"
          onClick={() => setLightbox(null)}
        >
          <Box position="relative" maxW="90vw" maxH="90vh">
            <Box
              as="button" position="absolute" top={-10} right={-10}
              bg="rgba(255,255,255,0.15)" borderRadius="full" p={2}
              cursor="pointer" onClick={() => setLightbox(null)}
              _hover={{ bg: 'rgba(255,255,255,0.3)' }}
            >
              <X size={20} color="#fff" />
            </Box>
            <img src={lightbox.url} alt={lightbox.alt}
              style={{ maxWidth: '90vw', maxHeight: '80vh', objectFit: 'contain', borderRadius: '12px' }}
            />
            <Box mt={3} textAlign="center">
              <Text color="#fff" fontSize="sm" fontWeight={600}>{lightbox.alt}</Text>
              {lightbox.caption && <Text color="rgba(255,255,255,0.7)" fontSize="xs" mt={1}>{lightbox.caption}</Text>}
              {lightbox.credit && <Text color="rgba(255,255,255,0.5)" fontSize="xs" mt={1}>© {lightbox.credit}</Text>}
            </Box>
          </Box>
        </Box>
      )}
    </Box>
  )
}

export default EntityGallery
