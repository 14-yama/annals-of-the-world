import React, { useState, useEffect } from 'react'
import { Outlet, Link as RouterLink, useLocation, useNavigate } from 'react-router-dom'
import { Box, Flex, Text, Stack, IconButton, Input } from '@chakra-ui/react'
import type { CSSProperties } from 'react'
import { useGlobalCounts } from '../hooks/useGlobalCounts'
import {
  BookOpen,
  Globe,
  Clock,
  Orbit,
  Menu,
  X,
  Network,
  Brain,
  Map,
  Waves,
  Mountain,
  Scroll,
  Swords,
  Lightbulb,
  Library,
  Landmark,
  Users,
  FileText,
  Search,
  Layers,
  ChevronDown,
  ChevronRight,
  Heart,
  Building2,
  Wheat,
  Compass,
  MapPin,
  Shirt,
  TrainFront,
  Gavel,
  Crown,
  BarChart3,
  AlertTriangle,
  ClipboardList,
  Cpu,
} from 'lucide-react'

/* ── Top-level domain navigation (horizontal) ── */
const TOP_NAV = [
  { path: '/explore',      label: 'Eras',           icon: Clock },
  { path: '/topics',       label: 'Topics',         icon: Layers },
  { path: '/corpus',       label: 'Corpuses',       icon: Library },
  { path: '/graph',        label: 'Graph',          icon: Network },
  { path: '/catalog',      label: 'Catalog',        icon: BookOpen },
]

/* ── Sidebar item type ── */
interface NavItem {
  path: string
  label: string
  icon: React.ElementType
}

interface NavSection {
  id: string
  label: string
  collapsible: boolean
  items: NavItem[]
}

/* ── Era sections with sub-divisions (from callNumbers.ts class 9) ── */
interface EraSection {
  id: string
  label: string
  eraId: string
  color: string
  icon: React.ElementType
  divisions: { path: string; label: string; code: string }[]
}

const ERA_SECTIONS: EraSection[] = [
  {
    id: 'era-prehistoric', label: 'Prehistoric', eraId: 'prehistory', color: '#6B4D1B', icon: Mountain,
    divisions: [
      { path: '/catalog?eraDivision=911', label: 'Paleolithic & Mesolithic', code: '911' },
      { path: '/catalog?eraDivision=912', label: 'Neolithic & Chalcolithic', code: '912' },
      { path: '/catalog?eraDivision=913', label: 'Bronze Age', code: '913' },
    ],
  },
  {
    id: 'era-classical', label: 'Classical', eraId: 'ancient', color: '#8B4513', icon: Landmark,
    divisions: [
      { path: '/catalog?eraDivision=921', label: 'Archaic Period', code: '921' },
      { path: '/catalog?eraDivision=922', label: 'Hellenistic Period', code: '922' },
      { path: '/catalog?eraDivision=923', label: 'Roman Period', code: '923' },
      { path: '/catalog?eraDivision=924', label: 'Late Antiquity', code: '924' },
    ],
  },
  {
    id: 'era-medieval', label: 'Medieval', eraId: 'medieval', color: '#A67C2E', icon: Crown,
    divisions: [
      { path: '/catalog?eraDivision=931', label: 'Early Medieval / Dark Ages', code: '931' },
      { path: '/catalog?eraDivision=932', label: 'High Medieval', code: '932' },
      { path: '/catalog?eraDivision=933', label: 'Late Medieval', code: '933' },
    ],
  },
  {
    id: 'era-early-modern', label: 'Early Modern', eraId: 'early-modern', color: '#C5963A', icon: Compass,
    divisions: [
      { path: '/catalog?eraDivision=941', label: 'Age of Exploration', code: '941' },
      { path: '/catalog?eraDivision=942', label: 'Renaissance Period', code: '942' },
      { path: '/catalog?eraDivision=943', label: 'Reformation Era', code: '943' },
      { path: '/catalog?eraDivision=944', label: 'Age of Enlightenment', code: '944' },
    ],
  },
  {
    id: 'era-modern', label: 'Modern', eraId: 'modern', color: '#4A90D9', icon: Globe,
    divisions: [
      { path: '/catalog?eraDivision=951', label: 'Industrial Age', code: '951' },
      { path: '/catalog?eraDivision=952', label: 'Age of Empire', code: '952' },
      { path: '/catalog?eraDivision=953', label: 'Interwar Period', code: '953' },
      { path: '/catalog?eraDivision=954', label: 'World War II Era', code: '954' },
    ],
  },
  {
    id: 'era-contemporary', label: 'Contemporary', eraId: 'contemporary', color: '#6B3FA0', icon: Orbit,
    divisions: [
      { path: '/catalog?eraDivision=961', label: 'Cold War Era', code: '961' },
      { path: '/catalog?eraDivision=962', label: 'Post-Cold War', code: '962' },
      { path: '/catalog?eraDivision=963', label: 'Digital Age', code: '963' },
    ],
  },
]

/* ── Sidebar sections ── */
const NAV_SECTIONS: NavSection[] = [
  {
    id: 'home', label: '', collapsible: false,
    items: [
      { path: '/',        label: 'The Great Hall', icon: Landmark },
    ],
  },
  {
    id: 'browse', label: 'Browse', collapsible: true,
    items: [
      { path: '/catalog?label=Person',      label: 'People',            icon: Users },
      { path: '/catalog?label=Idea',        label: 'Ideas',             icon: Lightbulb },
      { path: '/catalog?label=Institution', label: 'Institutions',      icon: Building2 },
      { path: '/catalog?label=Place',       label: 'Places',            icon: MapPin },
      { path: '/catalog?label=EventWindow', label: 'Events',            icon: Clock },
      { path: '/catalog?label=Movement',    label: 'Movements',         icon: Layers },
      { path: '/catalog?label=Text',        label: 'Texts & Artifacts', icon: FileText },
    ],
  },
  {
    id: 'continents', label: 'Continents', collapsible: true,
    items: [
      { path: '/continents/africa',   label: 'Africa',   icon: Globe },
      { path: '/continents/asia',     label: 'Asia',     icon: Globe },
      { path: '/continents/europe',   label: 'Europe',   icon: Map },
      { path: '/continents/americas', label: 'Americas', icon: Mountain },
      { path: '/continents/oceania',  label: 'Oceania',  icon: Waves },
    ],
  },
  {
    id: 'explore', label: 'Explore', collapsible: false,
    items: [
      { path: '/explore',      label: 'Era Explorer',     icon: Orbit },
      { path: '/graph',        label: 'Knowledge Graph',  icon: Network },
      { path: '/human-story',  label: 'Human Story',      icon: Users },
      { path: '/case-studies', label: 'Frameworks',       icon: FileText },
    ],
  },
  {
    id: 'topics', label: 'Topics', collapsible: true,
    items: [
      { path: '/topics',       label: 'All Topics',       icon: Layers },
      { path: '/weapons',      label: 'Arms & Warfare',   icon: Swords },
      { path: '/medicine',     label: 'Medicine',         icon: Heart },
      { path: '/architecture', label: 'Architecture',     icon: Building2 },
      { path: '/agriculture',  label: 'Agriculture',      icon: Wheat },
      { path: '/navigation',   label: 'Navigation',       icon: Compass },
      { path: '/languages',    label: 'Languages',        icon: BookOpen },
      { path: '/tribes',         label: 'Tribes & Peoples', icon: Users },
      { path: '/transportation', label: 'Transportation',   icon: TrainFront },
      { path: '/clothing',       label: 'Clothing',         icon: Shirt },
      { path: '/marriage',       label: 'Marriage',         icon: Heart },
      { path: '/customs',        label: 'Customs',          icon: Crown },
      { path: '/punishment',     label: 'Punishment',       icon: Gavel },
      { path: '/ideas',          label: 'Ideas',            icon: Lightbulb },
    ],
  },
  {
    id: 'corpus', label: 'Corpus', collapsible: true,
    items: [
      { path: '/corpus',          label: 'All Corpuses',  icon: Library },
      { path: '/corpus/biblical', label: 'Biblical',      icon: Library },
    ],
  },
  {
    id: 'tools', label: 'Tools', collapsible: false,
    items: [
      { path: '/curator',         label: 'The Curator',      icon: Scroll },
      { path: '/curator/audit',   label: 'Audit Dashboard',  icon: BarChart3 },
      { path: '/curator/audit/log', label: 'Audit Log',      icon: ClipboardList },
      { path: '/curator/triage',  label: 'Triage System',    icon: AlertTriangle },
      { path: '/curator/classes', label: 'Class Browser',    icon: Layers },
      { path: '/curator/people',  label: 'People Hub',       icon: Users },
      { path: '/curator/ollama',  label: 'Ollama Monitor',   icon: Cpu },
      { path: '/quiz',           label: 'Examination Hall', icon: Brain },
    ],
  },
  {
    id: 'about', label: 'About', collapsible: false,
    items: [
      { path: '/about', label: 'About the Annals', icon: BookOpen },
      { path: '/docs',  label: 'Documentation',    icon: FileText },
    ],
  },
]

export default function Layout() {
  const location = useLocation()
  const navigate = useNavigate()
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [globalSearch, setGlobalSearch] = useState('')
  const { total: catalogCount } = useGlobalCounts()
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({
    browse: true,
    continents: true,
    topics: true,
    corpus: true,
    ...Object.fromEntries(ERA_SECTIONS.map(e => [e.id, true])),
  })

  const toggleSection = (id: string) => {
    setCollapsed(prev => ({ ...prev, [id]: !prev[id] }))
  }

  /** Check if any item in a section is active (to auto-expand) */
  const isSectionActive = (section: NavSection) => {
    return section.items.some(item => {
      const hasQuery = item.path.includes('?')
      const fullUrl = location.pathname + location.search
      return hasQuery ? fullUrl === item.path : location.pathname === item.path
    })
  }

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
          {NAV_SECTIONS.map((section) => {
            const isOpen = !section.collapsible || !collapsed[section.id] || isSectionActive(section)
            return (
              <Box key={section.id}>
                {sidebarOpen && section.label && (
                  <Flex
                    align="center"
                    justify="space-between"
                    px={3}
                    pt={4}
                    pb={1}
                    cursor={section.collapsible ? 'pointer' : 'default'}
                    onClick={() => section.collapsible && toggleSection(section.id)}
                    _hover={section.collapsible ? { color: '#787469' } : {}}
                    role={section.collapsible ? 'button' : undefined}
                  >
                    <Text
                      fontFamily='"Cinzel", serif'
                      fontSize="9px"
                      fontWeight={700}
                      color="#B8B2A4"
                      letterSpacing="0.2em"
                      textTransform="uppercase"
                    >
                      {section.label}
                    </Text>
                    {section.collapsible && (
                      <Box color="#B8B2A4" transition="transform 0.2s">
                        {isOpen ? <ChevronDown size={12} /> : <ChevronRight size={12} />}
                      </Box>
                    )}
                  </Flex>
                )}
                {isOpen && section.items.map((item) => {
                  const hasQuery = item.path.includes('?')
                  const fullUrl = location.pathname + location.search
                  const isActive = hasQuery
                    ? fullUrl === item.path
                    : location.pathname === item.path
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
            )
          })}

          {/* ─── Era Sub-Divisions (Shelf Nav) ─── */}
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
                Eras
              </Text>
              {ERA_SECTIONS.map((era) => {
                const isEraOpen = !collapsed[era.id] ||
                  location.pathname === `/explore/${era.eraId}` ||
                  era.divisions.some(d => location.pathname + location.search === d.path)
                const EraIcon = era.icon
                return (
                  <Box key={era.id}>
                    <Flex
                      align="center"
                      gap="8px"
                      px={3}
                      py="7px"
                      cursor="pointer"
                      onClick={() => toggleSection(era.id)}
                      borderRadius="6px"
                      _hover={{ bg: `${era.color}08` }}
                      transition="all 0.2s"
                    >
                      <Box w="8px" h="8px" borderRadius="full" bg={era.color} flexShrink={0} />
                      <EraIcon size={14} color={era.color} />
                      <Text
                        flex={1}
                        fontFamily='"Inter", sans-serif'
                        fontSize="13px"
                        fontWeight={location.pathname === `/explore/${era.eraId}` ? 600 : 400}
                        color={location.pathname === `/explore/${era.eraId}` ? '#2D2A24' : '#787469'}
                        letterSpacing="0.02em"
                      >
                        {era.label}
                      </Text>
                      <Box color="#B8B2A4" transition="transform 0.2s">
                        {isEraOpen ? <ChevronDown size={11} /> : <ChevronRight size={11} />}
                      </Box>
                    </Flex>
                    {isEraOpen && (
                      <Box pl={6}>
                        {/* Link to era overview */}
                        <RouterLink
                          to={`/explore/${era.eraId}`}
                          style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: '8px',
                            padding: '5px 12px',
                            borderRadius: '4px',
                            fontSize: '11px',
                            fontFamily: '"Inter", sans-serif',
                            color: location.pathname === `/explore/${era.eraId}` ? era.color : '#9E9A90',
                            fontWeight: location.pathname === `/explore/${era.eraId}` ? 600 : 400,
                            textDecoration: 'none',
                            transition: 'all 0.2s',
                          }}
                        >
                          Overview
                        </RouterLink>
                        {/* Sub-division links */}
                        {era.divisions.map((div) => {
                          const fullUrl = location.pathname + location.search
                          const isDivActive = fullUrl === div.path
                          return (
                            <RouterLink
                              key={div.code}
                              to={div.path}
                              style={{
                                display: 'flex',
                                alignItems: 'center',
                                gap: '6px',
                                padding: '5px 12px',
                                borderRadius: '4px',
                                fontSize: '11px',
                                fontFamily: '"Inter", sans-serif',
                                color: isDivActive ? era.color : '#9E9A90',
                                fontWeight: isDivActive ? 600 : 400,
                                borderLeft: isDivActive ? `2px solid ${era.color}` : '2px solid transparent',
                                textDecoration: 'none',
                                transition: 'all 0.2s',
                                letterSpacing: '0.01em',
                              }}
                            >
                              <Text fontFamily='"JetBrains Mono", monospace' fontSize="9px" color="#B8B2A4">{div.code}</Text>
                              {div.label}
                            </RouterLink>
                          )
                        })}
                      </Box>
                    )}
                  </Box>
                )
              })}
            </Box>
          )}

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
                <span>Browse All ({catalogCount.toLocaleString()})</span>
              </RouterLink>
            </Box>
          )}
        </Stack>


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

          {/* Right: Global Search + Status */}
          <Flex align="center" gap={3}>
            <Box position="relative" w="240px">
              <Box position="absolute" left="10px" top="50%" transform="translateY(-50%)" zIndex={1}>
                <Search size={14} color="#9E9A90" />
              </Box>
              <Input
                value={globalSearch}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setGlobalSearch(e.target.value)}
                onKeyDown={(e: React.KeyboardEvent) => {
                  if (e.key === 'Enter' && globalSearch.trim()) {
                    navigate(`/catalog?search=${encodeURIComponent(globalSearch.trim())}`)
                    setGlobalSearch('')
                  }
                }}
                placeholder="Search the library..."
                pl="32px"
                h="32px"
                fontSize="12px"
                fontFamily='"Inter", sans-serif'
                bg="transparent"
                border="1px solid"
                borderColor="#D6D3CC"
                borderRadius="6px"
                _focus={{ borderColor: '#D4AF37', boxShadow: '0 0 0 1px #D4AF37' }}
                _placeholder={{ color: '#B8B2A4' }}
              />
            </Box>
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
