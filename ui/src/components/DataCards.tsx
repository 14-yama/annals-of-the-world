import React from 'react'
import { Box, Text, SimpleGrid, Flex, Heading } from '@chakra-ui/react'

interface StatCardProps {
  value: string
  label: string
  detail?: string
  color?: string
}

export function StatCard({ value, label, detail, color = '#D4AF37' }: StatCardProps) {
  return (
    <Box
      bg="#FAFAF8"
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
        w="3px"
        h="100%"
        bg={color}
      />
      <Text
        fontFamily='"Cinzel", serif'
        fontSize="2xl"
        fontWeight={700}
        color={color}
        lineHeight={1}
        letterSpacing="0.02em"
      >
        {value}
      </Text>
      <Text
        fontFamily='"Inter", sans-serif'
        fontSize="sm"
        fontWeight={600}
        color="#2D2A24"
        mt={1}
      >
        {label}
      </Text>
      {detail && (
        <Text fontSize="xs" color="#9E9A90" mt={1}>
          {detail}
        </Text>
      )}
    </Box>
  )
}

interface InsightCardProps {
  title: string
  insight: string
  source?: string
  accent?: string
}

export function InsightCard({ title, insight, source, accent = '#8B3A3A' }: InsightCardProps) {
  return (
    <Box
      bg="#FAFAF8"
      border="1px solid"
      borderColor="#E4E2DC"
      borderRadius="lg"
      p={5}
      boxShadow="0 1px 3px rgba(45,42,36,0.04)"
    >
      <Flex align="center" gap={2} mb={2}>
        <Box w="8px" h="8px" borderRadius="full" bg={accent} />
        <Text
          fontFamily='"Cormorant Garamond", serif'
          fontSize="lg"
          fontWeight={700}
          color="#2D2A24"
        >
          {title}
        </Text>
      </Flex>
      <Text fontSize="sm" color="#524E44" lineHeight={1.6}>
        {insight}
      </Text>
      {source && (
        <Text fontSize="xs" color="#B8B2A4" mt={2} fontStyle="italic">
          {source}
        </Text>
      )}
    </Box>
  )
}

interface DataTableProps {
  title: string
  headers: string[]
  rows: string[][]
}

export function DataTable({ title, headers, rows }: DataTableProps) {
  return (
    <Box
      bg="#FAFAF8"
      border="1px solid"
      borderColor="#E4E2DC"
      borderRadius="lg"
      overflow="hidden"
    >
      <Box bg="#2D2A24" px={4} py={3}>
        <Text
          fontFamily='"Cinzel", serif'
          fontSize="md"
          fontWeight={700}
          color="#D4AF37"
          letterSpacing="0.06em"
        >
          {title}
        </Text>
      </Box>
      <Box overflowX="auto">
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              {headers.map((h, i) => (
                <th
                  key={i}
                  style={{
                    padding: '10px 16px',
                    textAlign: 'left',
                    fontSize: '11px',
                    fontWeight: 700,
                    color: '#9E9A90',
                    borderBottom: '2px solid #E4E2DC',
                    fontFamily: '"Cinzel", serif',
                    textTransform: 'uppercase',
                    letterSpacing: '0.1em',
                  }}
                >
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, ri) => (
              <tr
                key={ri}
                style={{
                  backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0',
                }}
              >
                {row.map((cell, ci) => (
                  <td
                    key={ci}
                    style={{
                      padding: '8px 16px',
                      fontSize: '13px',
                      color: '#2D2A24',
                      borderBottom: '1px solid #EEEDEA',
                      fontFamily: '"Inter", sans-serif',
                    }}
                  >
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </Box>
    </Box>
  )
}

interface SectionHeadingProps {
  title: string
  subtitle?: string
}

export function SectionHeading({ title, subtitle }: SectionHeadingProps) {
  return (
    <Box mb={6}>
      <Heading
        fontFamily='"Cinzel", serif'
        fontSize="xl"
        fontWeight={700}
        color="#2D2A24"
        letterSpacing="0.08em"
        textTransform="uppercase"
      >
        {title}
      </Heading>
      {subtitle && (
        <Text
          fontSize="sm"
          color="#9E9A90"
          mt={1}
          fontFamily='"Inter", sans-serif'
        >
          {subtitle}
        </Text>
      )}
      <Box h="2px" bg="#D4AF37" w="60px" mt={3} />
    </Box>
  )
}
