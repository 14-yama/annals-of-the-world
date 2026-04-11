import React, { useEffect, useState } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { Link as RouterLink } from 'react-router-dom'
import {
  GraduationCap, Banknote, Medal, Hammer, PenLine,
  Brain, Calculator, Scale,
  Crown, Landmark, Flag, Users,
  Gavel, BookOpen,
  Atom, Stethoscope, Telescope, Leaf,
  Church, Star, Cross, Globe,
  Feather, BookText, Music, Paintbrush, Ruler,
  Megaphone, Heart, Handshake, HardHat,
  Swords, Anchor, Eye, Shield,
  Compass, Rocket, Waves, MapPin,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { SectionHeading } from '../../components/DataCards'
import { useGlobalCounts } from '../../hooks/useGlobalCounts'

/* ─── Division Definitions ─── */

interface Division {
  code: string
  heading: string
  icon: React.ElementType
  group: string
}

const PEOPLE_DIVISIONS: Division[] = [
  // Professional & Public Figures
  { code: '201', heading: 'Educators & Academics',        icon: GraduationCap, group: 'Professional' },
  { code: '202', heading: 'Merchants & Economists',       icon: Banknote,      group: 'Professional' },
  { code: '203', heading: 'Athletes & Competitors',       icon: Medal,         group: 'Professional' },
  { code: '204', heading: 'Architects & Engineers',        icon: Hammer,        group: 'Professional' },
  { code: '205', heading: 'Journalists & Chroniclers',     icon: PenLine,       group: 'Professional' },
  // Philosophers
  { code: '210', heading: 'Philosophers & Thinkers',       icon: Brain,         group: 'Thinkers' },
  { code: '211', heading: 'Logicians & Mathematicians',    icon: Calculator,    group: 'Thinkers' },
  { code: '212', heading: 'Ethicists & Moralists',         icon: Scale,         group: 'Thinkers' },
  // Political
  { code: '220', heading: 'Political Leaders',             icon: Crown,         group: 'Political' },
  { code: '221', heading: 'Monarchs & Rulers',             icon: Landmark,      group: 'Political' },
  { code: '222', heading: 'Heads of State & Government',   icon: Flag,          group: 'Political' },
  { code: '223', heading: 'Tribal & Indigenous Leaders',   icon: Users,         group: 'Political' },
  // Legal
  { code: '230', heading: 'Legal Figures',                 icon: Gavel,         group: 'Legal' },
  { code: '231', heading: 'Jurists & Legal Scholars',      icon: BookOpen,      group: 'Legal' },
  // Scientific
  { code: '240', heading: 'Scientists & Inventors',        icon: Atom,          group: 'Scientific' },
  { code: '241', heading: 'Physicians & Medical Pioneers', icon: Stethoscope,   group: 'Scientific' },
  { code: '242', heading: 'Astronomers & Cosmologists',    icon: Telescope,     group: 'Scientific' },
  { code: '243', heading: 'Naturalists & Biologists',      icon: Leaf,          group: 'Scientific' },
  // Religious
  { code: '250', heading: 'Religious Figures',             icon: Church,        group: 'Religious' },
  { code: '251', heading: 'Prophets & Founders',           icon: Star,          group: 'Religious' },
  { code: '252', heading: 'Theologians & Scholars',        icon: Cross,         group: 'Religious' },
  { code: '253', heading: 'Missionaries',                  icon: Globe,         group: 'Religious' },
  // Artists
  { code: '260', heading: 'Artists & Writers',             icon: Feather,       group: 'Creative' },
  { code: '261', heading: 'Authors & Novelists',           icon: BookText,      group: 'Creative' },
  { code: '262', heading: 'Poets & Playwrights',           icon: Music,         group: 'Creative' },
  { code: '263', heading: 'Composers & Musicians',         icon: Music,         group: 'Creative' },
  { code: '264', heading: 'Painters & Sculptors',          icon: Paintbrush,    group: 'Creative' },
  { code: '265', heading: 'Architects & Designers',        icon: Ruler,         group: 'Creative' },
  // Activists
  { code: '270', heading: 'Activists & Reformers',         icon: Megaphone,     group: 'Activist' },
  { code: '271', heading: 'Abolitionists',                 icon: Heart,         group: 'Activist' },
  { code: '272', heading: 'Suffragists & Feminists',       icon: Handshake,     group: 'Activist' },
  { code: '273', heading: 'Labor Organizers',              icon: HardHat,       group: 'Activist' },
  // Military
  { code: '280', heading: 'Military Leaders & Commanders', icon: Swords,        group: 'Military' },
  { code: '281', heading: 'Naval Commanders',              icon: Anchor,        group: 'Military' },
  { code: '282', heading: 'Intelligence & Espionage',      icon: Eye,           group: 'Military' },
  { code: '283', heading: 'Modern Military Commanders',    icon: Shield,        group: 'Military' },
  // Explorers
  { code: '290', heading: 'Explorers & Navigators',        icon: Compass,       group: 'Explorer' },
  { code: '291', heading: 'Space Explorers',               icon: Rocket,        group: 'Explorer' },
  { code: '292', heading: 'Deep-Sea Explorers',            icon: Waves,         group: 'Explorer' },
  { code: '293', heading: 'Cartographers',                 icon: MapPin,        group: 'Explorer' },
]

const GROUP_ORDER = ['Political', 'Military', 'Scientific', 'Religious', 'Creative', 'Thinkers', 'Professional', 'Legal', 'Activist', 'Explorer']

/* ─── Main Component ─── */

export default function PeopleHub() {
  const [counts, setCounts] = useState<Record<string, number>>({})
  const { byLabel } = useGlobalCounts()
  const totalPeople = byLabel['Person'] || 0
  const [loading, setLoading] = useState(true)

  useEffect(() => { loadCounts() }, [])

  async function loadCounts() {
    setLoading(true)
    try {
      // Count per division — batch 10 at a time
      const newCounts: Record<string, number> = {}
      for (let i = 0; i < PEOPLE_DIVISIONS.length; i += 10) {
        const batch = PEOPLE_DIVISIONS.slice(i, i + 10)
        const results = await Promise.all(
          batch.map(async (div) => {
            try {
              const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
                Query.startsWith('callNumber', div.code + '.'),
                Query.limit(1),
              ])
              return { code: div.code, count: res.total }
            } catch { return { code: div.code, count: 0 } }
          }),
        )
        for (const r of results) newCounts[r.code] = r.count
        setCounts((prev) => ({ ...prev, ...Object.fromEntries(results.map((r) => [r.code, r.count])) }))
      }
    } catch (err) {
      console.error('PeopleHub load failed:', err)
    }
    setLoading(false)
  }

  // Group divisions by category
  const groups = GROUP_ORDER.map((g) => ({
    name: g,
    divisions: PEOPLE_DIVISIONS.filter((d) => d.group === g),
  }))

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      {/* Hero */}
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Box p={2} borderRadius="md" bg="#4A90D920">
            <Users size={24} color="#4A90D9" />
          </Box>
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color="#2D2A24" letterSpacing="0.08em">
              CLASS 2 — PEOPLE
            </Text>
            <Text color="#787469" fontSize="sm">
              {totalPeople.toLocaleString()} Person entities across {PEOPLE_DIVISIONS.length} divisions
            </Text>
          </Box>
        </Flex>
        <Text fontSize="sm" color="#524E44" maxW="800px" mt={2}>
          Browse, audit, and edit Person entities organized by Dewey-style division codes.
          Click any division to view its entities with inline editing capabilities.
        </Text>
      </Box>

      {/* Division Groups */}
      {groups.map((group) => (
        <Box key={group.name} mb={8}>
          <SectionHeading title={group.name} subtitle={`${group.divisions.length} divisions`} />
          <SimpleGrid columns={{ base: 1, sm: 2, md: 3, lg: 4 }} gap={4}>
            {group.divisions.map((div) => {
              const count = counts[div.code] ?? 0
              const Icon = div.icon
              const isZero = count === 0
              return (
                <RouterLink key={div.code} to={`/curator/people/${div.code}`} style={{ textDecoration: 'none' }}>
                  <Box
                    bg="#FAFAF8"
                    border="1px solid"
                    borderColor={isZero ? '#FADBD8' : '#E4E2DC'}
                    borderRadius="lg"
                    p={4}
                    transition="all 0.2s"
                    _hover={{ transform: 'translateY(-2px)', shadow: 'md', borderColor: '#D4AF37' }}
                    cursor="pointer"
                    position="relative"
                    overflow="hidden"
                  >
                    <Box position="absolute" top={0} left={0} w="100%" h="3px"
                      bg={isZero ? '#E74C3C' : count > 100 ? '#27AE60' : count > 10 ? '#F1C40F' : '#E67E22'} />
                    <Flex justify="space-between" align="start">
                      <Flex align="center" gap={2}>
                        <Box p={1.5} borderRadius="md" bg="#F5F4F0">
                          <Icon size={16} color="#787469" />
                        </Box>
                        <Box>
                          <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" fontWeight={600}>
                            {div.code}
                          </Text>
                          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={600} color="#2D2A24" lineHeight={1.3}>
                            {div.heading}
                          </Text>
                        </Box>
                      </Flex>
                      <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700}
                        color={isZero ? '#E74C3C' : '#2D2A24'}>
                        {loading ? '…' : count.toLocaleString()}
                      </Text>
                    </Flex>
                  </Box>
                </RouterLink>
              )
            })}
          </SimpleGrid>
        </Box>
      ))}
    </Box>
  )
}
