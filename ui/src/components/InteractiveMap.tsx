/* ─── Interactive World Map — Annals of the World ─── */
import React, { useState } from 'react'
import { Box, Text, Flex, Heading } from '@chakra-ui/react'
import {
  ComposableMap,
  Geographies,
  Geography,
  Marker,
  ZoomableGroup,
} from 'react-simple-maps'
import type { MapMarker } from '../types'

const GEO_URL = 'https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json'

const CONTINENT_COLORS: Record<string, string> = {
  africa: '#DD6B20', asia: '#C53030', europe: '#3182CE',
  americas: '#38A169', oceania: '#38B2AC',
}

interface InteractiveMapProps {
  markers?: MapMarker[]
  title?: string
  highlightContinent?: string
  height?: number
  center?: [number, number]
  zoom?: number
}

export default function InteractiveMap({
  markers = [],
  title,
  highlightContinent,
  height = 500,
  center = [20, 10],
  zoom = 1,
}: InteractiveMapProps) {
  const [tooltip, setTooltip] = useState<MapMarker | null>(null)
  const [hoveredGeo, setHoveredGeo] = useState<string>('')

  const CONTINENT_COUNTRY_MAP: Record<string, string[]> = {
    africa: ['DZA','AGO','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG','COD','CIV','DJI','EGY','GNQ','ERI','SWZ','ETH','GAB','GMB','GHA','GIN','GNB','KEN','LSO','LBR','LBY','MDG','MWI','MLI','MRT','MUS','MAR','MOZ','NAM','NER','NGA','RWA','STP','SEN','SYC','SLE','SOM','ZAF','SSD','SDN','TZA','TGO','TUN','UGA','ZMB','ZWE'],
    asia: ['AFG','ARM','AZE','BHR','BGD','BTN','BRN','KHM','CHN','CYP','GEO','IND','IDN','IRN','IRQ','ISR','JPN','JOR','KAZ','KWT','KGZ','LAO','LBN','MYS','MDV','MNG','MMR','NPL','PRK','OMN','PAK','PSE','PHL','QAT','SAU','SGP','KOR','LKA','SYR','TWN','TJK','THA','TLS','TUR','TKM','ARE','UZB','VNM','YEM'],
    europe: ['ALB','AND','AUT','BLR','BEL','BIH','BGR','HRV','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ITA','XKX','LVA','LIE','LTU','LUX','MLT','MDA','MCO','MNE','NLD','MKD','NOR','POL','PRT','ROU','RUS','SMR','SRB','SVK','SVN','ESP','SWE','CHE','UKR','GBR','VAT'],
    americas: ['ATG','ARG','BHS','BRB','BLZ','BOL','BRA','CAN','CHL','COL','CRI','CUB','DMA','DOM','ECU','SLV','GRD','GTM','GUY','HTI','HND','JAM','MEX','NIC','PAN','PRY','PER','KNA','LCA','VCT','SUR','TTO','USA','URY','VEN'],
    oceania: ['AUS','FJI','KIR','MHL','FSM','NRU','NZL','PLW','PNG','WSM','SLB','TON','TUV','VUT'],
  }

  return (
    <Box>
      {title && (
        <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#2D2A24" mb={3}>
          {title}
        </Heading>
      )}
      <Box
        bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg"
        overflow="hidden" position="relative"
        h={`${height}px`}
      >
        <ComposableMap
          projection="geoMercator"
          projectionConfig={{ scale: 120 * zoom, center }}
          width={800}
          height={height}
          style={{ width: '100%', height: '100%' }}
        >
          <ZoomableGroup center={center} zoom={zoom} minZoom={0.5} maxZoom={8}>
            <Geographies geography={GEO_URL}>
              {({ geographies }) =>
                geographies.map((geo) => {
                  const isoA3 = geo.properties?.['ISO_A3'] || geo.id
                  const isHighlighted = highlightContinent &&
                    CONTINENT_COUNTRY_MAP[highlightContinent]?.includes(isoA3)
                  const isHovered = hoveredGeo === isoA3

                  return (
                    <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      fill={
                        isHighlighted
                          ? (CONTINENT_COLORS[highlightContinent!] || '#D6D3CC')
                          : isHovered ? '#E4E2DC' : '#F5F4F0'
                      }
                      stroke="#D6D3CC"
                      strokeWidth={0.5}
                      style={{
                        default: { outline: 'none' },
                        hover: { outline: 'none', fill: isHighlighted ? (CONTINENT_COLORS[highlightContinent!] || '#D6D3CC') : '#E4E2DC' },
                        pressed: { outline: 'none' },
                      }}
                      onMouseEnter={() => setHoveredGeo(isoA3)}
                      onMouseLeave={() => setHoveredGeo('')}
                    />
                  )
                })
              }
            </Geographies>

            {/* Markers */}
            {markers.map(marker => (
              <Marker key={marker.id} coordinates={[marker.lng, marker.lat]}>
                <circle
                  r={5}
                  fill={marker.color}
                  stroke="#fff"
                  strokeWidth={1.5}
                  cursor="pointer"
                  onMouseEnter={() => setTooltip(marker)}
                  onMouseLeave={() => setTooltip(null)}
                />
                <text
                  textAnchor="middle"
                  y={-10}
                  style={{ fontFamily: 'Inter', fontSize: '8px', fill: '#2D2A24', fontWeight: 500 }}
                >
                  {marker.name}
                </text>
              </Marker>
            ))}
          </ZoomableGroup>
        </ComposableMap>

        {/* Tooltip */}
        {tooltip && (
          <Box
            position="absolute" bottom={3} left={3}
            bg="rgba(250,243,232,0.97)" border="1px solid" borderColor="#E4E2DC"
            borderRadius="md" p={3} maxW="240px"
          >
            <Flex align="center" gap={2} mb={1}>
              <Box w="8px" h="8px" borderRadius="full" bg={tooltip.color} />
              <Text fontSize="sm" fontWeight={600} color="#2D2A24">{tooltip.name}</Text>
            </Flex>
            <Text fontSize="xs" color="#524E44" lineHeight={1.5}>{tooltip.description}</Text>
          </Box>
        )}
      </Box>
    </Box>
  )
}
