import React, { useEffect, useState, useMemo, useRef } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { Link as RouterLink, useParams, useNavigate } from 'react-router-dom'
import {
  Lightbulb, Beaker, Users, Landmark, Globe, Zap, Flame, BookOpen, Shield, Clock,
  ChevronLeft, Layers,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { countAllDocuments } from '../../services/adminService'
import { SectionHeading } from '../../components/DataCards'
import { CLASSES, DIVISIONS } from '../../constants/callNumbers'

/* ─── Class Icon Map ─── */

const CLASS_ICONS: Record<number, React.ElementType> = {
  0: Lightbulb,   // Ideas (Core)
  1: Beaker,      // Ideas (Other)
  2: Users,       // People
  3: Landmark,    // Institutions
  4: Globe,       // Places
  5: Zap,         // Events
  6: Flame,       // Movements
  7: BookOpen,    // Artifacts & Texts
  8: Shield,      // Evidence
  9: Clock,       // Timeframes
}

const CLASS_COLORS: Record<number, string> = {
  0: '#6B3FA0', 1: '#D35400', 2: '#4A90D9', 3: '#8B4513', 4: '#2E8B57',
  5: '#C5963A', 6: '#E74C3C', 7: '#6B4D1B', 8: '#7D8C6C', 9: '#9E9A90',
}

/* ─── All Classes Overview ─── */

function AllClassesView() {
  const [classCounts, setClassCounts] = useState<Record<number, number>>({})
  const [totalEntities, setTotalEntities] = useState(0)
  const [loading, setLoading] = useState(true)
  const cacheRef = useRef<Record<number, number> | null>(null)

  useEffect(() => { loadCounts() }, [])

  async function loadCounts() {
    // Use cache if available (avoid expensive re-counts on every mount)
    if (cacheRef.current) {
      setClassCounts(cacheRef.current)
      setTotalEntities(Object.values(cacheRef.current).reduce((a, b) => a + b, 0))
      setLoading(false)
      return
    }

    setLoading(true)
    try {
      const counts: Record<number, number> = {}
      // Count each class using cursor-based pagination (accurate beyond 5000)
      for (const cls of CLASSES) {
        try {
          const n = await countAllDocuments([Query.startsWith('callNumber', `${cls.code}`)])
          counts[cls.code] = n
          // Progressive update: show counts as they come in
          setClassCounts((prev) => ({ ...prev, [cls.code]: n }))
        } catch { counts[cls.code] = 0 }
      }

      const total = Object.values(counts).reduce((a, b) => a + b, 0)
      setTotalEntities(total)
      setClassCounts(counts)
      cacheRef.current = counts
    } catch (err) {
      console.error('ClassHub load failed:', err)
    }
    setLoading(false)
  }

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      <Box mb={8}>
        <Flex align="center" gap={3} mb={2}>
          <Box p={2} borderRadius="md" bg="#D4AF3720">
            <Layers size={24} color="#D4AF37" />
          </Box>
          <Box>
            <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color="#2D2A24" letterSpacing="0.08em">
              DEWEY CLASS BROWSER
            </Text>
            <Text color="#787469" fontSize="sm">
              {totalEntities.toLocaleString()} entities across {CLASSES.length} classes, {DIVISIONS.length} divisions
            </Text>
          </Box>
        </Flex>
        <Text fontSize="sm" color="#524E44" maxW="800px" mt={2}>
          Browse entities by Dewey-style classification. Each class groups related divisions for auditing,
          editing, and quality control. Click a class to explore its divisions.
        </Text>
      </Box>

      <SimpleGrid columns={{ base: 1, sm: 2, lg: 3 }} gap={5}>
        {CLASSES.map((cls) => {
          const Icon = CLASS_ICONS[cls.code] ?? Layers
          const color = CLASS_COLORS[cls.code] ?? '#9E9A90'
          const divCount = DIVISIONS.filter((d) => d.parentClass === cls.code).length
          const count = classCounts[cls.code] ?? 0
          return (
            <RouterLink key={cls.code} to={`/curator/classes/${cls.code}`} style={{ textDecoration: 'none' }}>
              <Box
                bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={5}
                transition="all 0.2s" cursor="pointer" position="relative" overflow="hidden"
                _hover={{ transform: 'translateY(-2px)', shadow: 'lg', borderColor: color }}
              >
                <Box position="absolute" top={0} left={0} w="100%" h="4px" bg={color} />
                <Flex justify="space-between" align="start" mb={3}>
                  <Flex align="center" gap={3}>
                    <Box p={2} borderRadius="md" bg={`${color}15`}>
                      <Icon size={22} color={color} />
                    </Box>
                    <Box>
                      <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" fontWeight={600}>
                        Class {cls.code}
                      </Text>
                      <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24" lineHeight={1.3}>
                        {cls.heading}
                      </Text>
                    </Box>
                  </Flex>
                </Flex>
                <Flex justify="space-between" align="center">
                  <Text fontSize="xs" color="#787469">{divCount} divisions</Text>
                  <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color={color}>
                    {loading ? '…' : count.toLocaleString()}
                  </Text>
                </Flex>
                <Flex mt={2} gap={1} flexWrap="wrap">
                  {cls.nodeTypes.slice(0, 4).map((t) => (
                    <Box key={t} px={2} py={0.5} borderRadius="sm" bg="#F5F4F0" fontSize="10px" color="#787469">
                      {t}
                    </Box>
                  ))}
                  {cls.nodeTypes.length > 4 && (
                    <Box px={2} py={0.5} borderRadius="sm" bg="#F5F4F0" fontSize="10px" color="#9E9A90">
                      +{cls.nodeTypes.length - 4}
                    </Box>
                  )}
                </Flex>
              </Box>
            </RouterLink>
          )
        })}
      </SimpleGrid>
    </Box>
  )
}

/* ─── Single Class Detail ─── */

function ClassDetail({ classCode }: { classCode: number }) {
  const navigate = useNavigate()
  const [counts, setCounts] = useState<Record<string, number>>({})
  const [totalClass, setTotalClass] = useState(0)
  const [loading, setLoading] = useState(true)

  const classInfo = useMemo(() => CLASSES.find((c) => c.code === classCode), [classCode])
  const divisions = useMemo(() => DIVISIONS.filter((d) => d.parentClass === classCode), [classCode])
  const Icon = CLASS_ICONS[classCode] ?? Layers
  const color = CLASS_COLORS[classCode] ?? '#9E9A90'

  useEffect(() => { loadCounts() }, [classCode])

  async function loadCounts() {
    setLoading(true)
    try {
      const totalN = await countAllDocuments([Query.startsWith('callNumber', `${classCode}`)])
      setTotalClass(totalN)

      const newCounts: Record<string, number> = {}
      for (let i = 0; i < divisions.length; i += 10) {
        const batch = divisions.slice(i, i + 10)
        const results = await Promise.all(
          batch.map(async (div) => {
            try {
              const n = await countAllDocuments([Query.startsWith('callNumber', div.code + '.')])
              return { code: div.code, count: n }
            } catch { return { code: div.code, count: 0 } }
          }),
        )
        for (const r of results) newCounts[r.code] = r.count
        setCounts((prev) => ({ ...prev, ...Object.fromEntries(results.map((r) => [r.code, r.count])) }))
      }
    } catch (err) {
      console.error('ClassDetail load failed:', err)
    }
    setLoading(false)
  }

  // Group divisions by first two digits (sub-groups)
  const groups = useMemo(() => {
    const map = new Map<string, typeof divisions>()
    for (const d of divisions) {
      const prefix = d.code.slice(0, 2)
      if (!map.has(prefix)) map.set(prefix, [])
      map.get(prefix)!.push(d)
    }
    return Array.from(map.entries()).map(([prefix, divs]) => ({
      prefix,
      heading: divs[0].heading.split('&')[0].trim(),
      divisions: divs,
    }))
  }, [divisions])

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      <Flex align="center" gap={3} mb={6}>
        <Box
          as="button"
          onClick={() => navigate('/curator/classes')}
          p={2} borderRadius="md" bg="#F5F4F0" cursor="pointer" _hover={{ bg: '#E4E2DC' }}
        >
          <ChevronLeft size={18} color="#787469" />
        </Box>
        <Box p={2} borderRadius="md" bg={`${color}20`}>
          <Icon size={24} color={color} />
        </Box>
        <Box>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color={color} fontWeight={600}>
            Class {classCode}
          </Text>
          <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
            {classInfo?.heading ?? `Class ${classCode}`}
          </Text>
          <Text fontSize="sm" color="#787469">
            {totalClass.toLocaleString()} entities · {divisions.length} divisions
          </Text>
        </Box>
      </Flex>

      {loading && divisions.length > 0 && Object.keys(counts).length === 0 ? (
        <Flex justify="center" py={12}>
          <Spinner size="lg" color={color} />
          <Text ml={3} color="#787469">Counting divisions…</Text>
        </Flex>
      ) : (
        groups.map((group) => (
          <Box key={group.prefix} mb={8}>
            <SectionHeading title={group.heading} subtitle={`${group.divisions.length} divisions`} />
            <SimpleGrid columns={{ base: 1, sm: 2, md: 3, lg: 4 }} gap={4}>
              {group.divisions.map((div) => {
                const count = counts[div.code] ?? 0
                const isZero = count === 0
                return (
                  <RouterLink key={div.code} to={`/curator/classes/${classCode}/${div.code}`} style={{ textDecoration: 'none' }}>
                    <Box
                      bg="#FAFAF8" border="1px solid" borderColor={isZero ? '#FADBD8' : '#E4E2DC'}
                      borderRadius="lg" p={4} transition="all 0.2s" cursor="pointer"
                      position="relative" overflow="hidden"
                      _hover={{ transform: 'translateY(-2px)', shadow: 'md', borderColor: color }}
                    >
                      <Box position="absolute" top={0} left={0} w="100%" h="3px"
                        bg={isZero ? '#E74C3C' : count > 100 ? '#27AE60' : count > 10 ? '#F1C40F' : '#E67E22'} />
                      <Flex justify="space-between" align="start">
                        <Box>
                          <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" color="#9E9A90" fontWeight={600}>
                            {div.code}
                          </Text>
                          <Text fontFamily='"Inter", sans-serif' fontSize="sm" fontWeight={600} color="#2D2A24" lineHeight={1.3}>
                            {div.heading}
                          </Text>
                        </Box>
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
        ))
      )}
    </Box>
  )
}

/* ─── Router Wrapper ─── */

export default function ClassHub() {
  const { classCode } = useParams<{ classCode: string }>()

  if (classCode !== undefined) {
    return <ClassDetail classCode={Number(classCode)} />
  }
  return <AllClassesView />
}
