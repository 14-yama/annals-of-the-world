import React from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { Box, Flex, Text } from '@chakra-ui/react'
import { Home, ChevronRight } from 'lucide-react'

export interface BreadcrumbItem {
  label: string
  to?: string
}

interface BreadcrumbProps {
  items: BreadcrumbItem[]
}

/**
 * Breadcrumb — consistent navigation trail across all pages.
 * Pattern: Home > [Section] > [Page]
 */
export default function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <Flex align="center" gap={1.5} mb={5} flexWrap="wrap">
      <RouterLink to="/" style={{ display: 'flex', alignItems: 'center', gap: 4, color: '#9E9A90', textDecoration: 'none' }}>
        <Home size={14} />
        <Text fontSize="xs" _hover={{ color: '#D4AF37' }}>Home</Text>
      </RouterLink>
      {items.map((item, i) => {
        const isLast = i === items.length - 1
        return (
          <React.Fragment key={i}>
            <ChevronRight size={12} color="#D6D3CC" />
            {isLast || !item.to ? (
              <Text fontSize="xs" color="#2D2A24" fontWeight={600}>{item.label}</Text>
            ) : (
              <RouterLink to={item.to} style={{ textDecoration: 'none' }}>
                <Text fontSize="xs" color="#9E9A90" _hover={{ color: '#D4AF37' }}>{item.label}</Text>
              </RouterLink>
            )}
          </React.Fragment>
        )
      })}
    </Flex>
  )
}
