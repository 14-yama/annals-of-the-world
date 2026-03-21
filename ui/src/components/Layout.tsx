import React, { useState } from 'react'
import { Outlet, Link as RouterLink, useLocation } from 'react-router-dom'
import { Box, Flex, Text, Stack, IconButton } from '@chakra-ui/react'
import type { CSSProperties } from 'react'
import {
  BookOpen,
  Globe,
  Clock,
  Orbit,
  Info,
  Menu,
  X,
  Home,
  Network,
  Brain,
  Map,
  Waves,
  Mountain,
  Scroll,
  Swords,
  Lightbulb,
  Library,
  Columns3,
  Landmark,
  Users,
  FileText,
  MapPin,
  Building2,
} from 'lucide-react'
import { getAllEntities } from '../data/catalog'

/* ── Top-level domain navigation (horizontal) ── */
const TOP_NAV = [
  { path: '/ideas',     label: 'Ideas',        icon: Lightbulb },
  { path: '/graph',     label: 'Knowledge Graph', icon: Network },
  { path: '/explore',   label: 'Eras',         icon: Clock },
  { path: '/human-story', label: 'Human Story', icon: Users },
  { path: '/case-studies', label: 'Frameworks', icon: Orbit },
]

/* ── Shelf navigation (left panel — contextual "stacks") ── */
const SHELF_ITEMS = [
  { path: '/',                    label: 'The Great Hall',   icon: Landmark,  section: '' },
  { path: '/continents/africa',   label: 'Africa',           icon: Globe,     section: 'Continents' },
  { path: '/continents/asia',     label: 'Asia',             icon: Globe,     section: 'Continents' },
  { path: '/continents/europe',   label: 'Europe',           icon: Map,       section: 'Continents' },
  { path: '/continents/americas', label: 'Americas',         icon: Mountain,  section: 'Continents' },
  { path: '/continents/oceania',  label: 'Oceania',          icon: Waves,     section: 'Continents' },
  { path: '/explore',             label: 'Era Explorer',     icon: Orbit,     section: 'Time' },
  { path: '/graph',               label: 'Knowledge Graph',  icon: Network,   section: 'Collections' },
  { path: '/weapons',             label: 'Arms & Warfare',   icon: Swords,    section: 'Collections' },
  { path: '/ideas',               label: 'Ideas',            icon: Lightbulb, section: 'Collections' },
  { path: '/human-story',         label: 'Human Story',      icon: Users,     section: 'Collections' },
  { path: '/case-studies',        label: 'Frameworks',       icon: FileText,  section: 'Collections' },
  { path: '/curator',             label: 'The Curator',      icon: Scroll,    section: 'Tools' },
  { path: '/quiz',                label: 'Examination Hall', icon: Brain,     section: 'Tools' },
  { path: '/about',               label: 'About the Annals', icon: BookOpen,  section: 'About' },
]

/* Group shelf items by section */
function groupBySection(items: typeof SHELF_ITEMS) {
  const groups: { section: string; items: typeof SHELF_ITEMS }[] = []
  let current: string | null = null
  for (const item of items) {
    if (item.section !== current) {
      current = item.section
      groups.push({ section: current, items: [] })
    }
    groups[groups.length - 1].items.push(item)
  }
  return groups
}

export default function Layout() {
  const location = useLocation()
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const groups = groupBySection(SHELF_ITEMS)

  return (
    <Flex minH="100vh" bg="#FAFAF8">
      {/* ─── Left Panel: Shelf Navigation ─── */}
      <Box
        as="nav"
        w={sidebarOpen ? '270px' : '60px'}
        bg="linear-gradient(180deg, #FAFAF8 0%, #F0EDE6 100%)"
        borderRight="1px solid"
        borderColor="#D6D3CC"
        transition="width 0.3s"
        flexShrink={0}
        position="sticky"
        top={0}
        h="100vh"
        overflowY="auto"
        overflowX="hidden"
        css={{
          '&::-webkit-scrollbar': { width: '4px' },
          '&::-webkit-scrollbar-thumb': { background: '#D6D3CC', borderRadius: '4px' },
        }}
      >
        {/* Library Header */}
        <Flex
          align="center"
          justify={sidebarOpen ? 'space-between' : 'center'}
          p={4}
          borderBottom="1px solid"
          borderColor="#D6D3CC"
          bg="rgba(250,250,248,0.9)"
        >
          {sidebarOpen && (
            <Box>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="lg"
                fontWeight={700}
                color="#2D2A24"
                letterSpacing="0.12em"
                textTransform="uppercase"
                lineHeight={1.2}
              >
                ANNALS
              </Text>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="10px"
                color="#9E9A90"
                letterSpacing="0.25em"
                textTransform="uppercase"
                mt={0.5}
              >
                OF THE WORLD
              </Text>
            </Box>
          )}
          <IconButton
            aria-label="Toggle sidebar"
            variant="ghost"
            color="#9E9A90"
            size="sm"
            onClick={() => setSidebarOpen(!sidebarOpen)}
            _hover={{ color: '#2D2A24', bg: 'rgba(212,175,55,0.08)' }}
          >
            {sidebarOpen ? <X size={18} /> : <Menu size={18} />}
          </IconButton>
        </Flex>

        {/* Shelf Items grouped by section */}
        <Stack gap={0} p={2} mt={1}>
          {groups.map((group) => (
            <Box key={group.section || 'root'}>
              {sidebarOpen && group.section && (
                <Text
                  fontFamily='"Cinzel", serif'
                  fontSize="9px"
                  fontWeight={700}
                  color="#B8B2A4"
                  letterSpacing="0.2em"
                  textTransform="uppercase"
                  px={3}
                  pt={4}
                  pb={1}
                >
                  {group.section}
                </Text>
              )}
              {group.items.map((item) => {
                const isActive = location.pathname === item.path
                const Icon = item.icon
                return (
                  <RouterLink
                    to={item.path}
                    key={item.path}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '10px',
                      padding: '9px 12px',
                      borderRadius: '6px',
                      backgroundColor: isActive ? 'rgba(212,175,55,0.10)' : 'transparent',
                      borderLeft: isActive ? '3px solid #D4AF37' : '3px solid transparent',
                      color: isActive ? '#2D2A24' : '#787469',
                      fontWeight: isActive ? 600 : 400,
                      fontSize: '13px',
                      fontFamily: '"Inter", sans-serif',
                      textDecoration: 'none',
                      transition: 'all 0.2s',
                      letterSpacing: '0.02em',
                    }}
                  >
                    <Icon size={16} />
                    {sidebarOpen && <Text>{item.label}</Text>}
                  </RouterLink>
                )
              })}
            </Box>
          ))}

          {/* Catalog Link — browse all entities */}
          {sidebarOpen && (
            <Box>
              <Text
                fontFamily='"Cinzel", serif'
                fontSize="9px"
                fontWeight={700}
                color="#B8B2A4"
                letterSpacing="0.2em"
                textTransform="uppercase"
                px={3}
                pt={4}
                pb={1}
              >
                Catalog
              </Text>
              <RouterLink
                to="/catalog"
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '10px',
                  padding: '9px 12px',
                  borderRadius: '6px',
                  backgroundColor: location.pathname === '/catalog' ? 'rgba(212,175,55,0.10)' : 'transparent',
                  borderLeft: location.pathname === '/catalog' ? '3px solid #D4AF37' : '3px solid transparent',
                  color: location.pathname === '/catalog' ? '#2D2A24' : '#787469',
                  fontWeight: location.pathname === '/catalog' ? 600 : 400,
                  fontSize: '13px',
                  fontFamily: '"Inter", sans-serif',
                  textDecoration: 'none',
                  transition: 'all 0.2s',
                  letterSpacing: '0.02em',
                }}
              >
                <Library size={16} />
                <span>Browse All ({getAllEntities().length})</span>
              </RouterLink>
            </Box>
          )}
        </Stack>

        {/* Footer — Dedication */}
        {sidebarOpen && (
          <Box
            position="absolute"
            bottom={0}
            left={0}
            right={0}
            p={4}
            borderTop="1px solid"
            borderColor="#D6D3CC"
            bg="rgba(250,250,248,0.95)"
          >
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="9px"
              color="#B8B2A4"
              textAlign="center"
              letterSpacing="0.15em"
              textTransform="uppercase"
            >
              Honoring James Ussher
            </Text>
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="9px"
              color="#D6D3CC"
              textAlign="center"
              letterSpacing="0.2em"
              mt={0.5}
            >
              MDLXXXI — MDCLVI
            </Text>
          </Box>
        )}
      </Box>

      {/* ─── Main Content Area ─── */}
      <Box flex={1} overflowY="auto" id="main-content">
        {/* Top Navigation Bar — Domain-level navigation */}
        <Flex
          as="header"
          bg="rgba(250,250,248,0.97)"
          borderBottom="1px solid"
          borderColor="#D6D3CC"
          px={6}
          py={0}
          align="center"
          justify="space-between"
          position="sticky"
          top={0}
          zIndex={10}
          backdropFilter="blur(12px)"
        >
          {/* Domain Navigation */}
          <Flex align="center" gap={0}>
            {TOP_NAV.map((item) => {
              const isActive = location.pathname === item.path ||
                location.pathname.startsWith(item.path + '/')
              const Icon = item.icon
              return (
                <RouterLink
                  to={item.path}
                  key={item.path}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '14px 16px',
                    color: isActive ? '#2D2A24' : '#9E9A90',
                    fontFamily: '"Cinzel", serif',
                    fontSize: '11px',
                    fontWeight: isActive ? 700 : 400,
                    letterSpacing: '0.12em',
                    textTransform: 'uppercase',
                    textDecoration: 'none',
                    borderBottom: isActive ? '2px solid #D4AF37' : '2px solid transparent',
                    transition: 'all 0.2s',
                  }}
                >
                  <Icon size={14} />
                  {item.label}
                </RouterLink>
              )
            })}
          </Flex>

          {/* Right: Status */}
          <Flex align="center" gap={3}>
            <Text
              fontFamily='"Cinzel", serif'
              fontSize="10px"
              color="#B8B2A4"
              letterSpacing="0.15em"
              textTransform="uppercase"
            >
              199 Nations &middot; 72,000 Years
            </Text>
          </Flex>
        </Flex>

        {/* Page Content */}
        <Box p={6} maxW="1400px" mx="auto">
          <Outlet />
        </Box>
      </Box>
    </Flex>
  )
}
