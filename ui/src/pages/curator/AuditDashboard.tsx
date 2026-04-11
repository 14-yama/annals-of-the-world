import React, { useEffect, useState, useMemo, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner, Progress, Input } from '@chakra-ui/react'
import { Link as RouterLink } from 'react-router-dom'
import {
  BarChart3,
  AlertTriangle,
  CheckCircle2,
  Image,
  Link as LinkIcon,
  BookOpen,
  Users,
  Globe,
  Clock,
  Layers,
  TrendingUp,
  Search,
  Download,
  Star,
  Zap,
  Shield,
} from 'lucide-react'
import { Query, type Models } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { StatCard, SectionHeading } from '../../components/DataCards'
import { CLASSES, DIVISIONS } from '../../constants/callNumbers'
import { useGlobalCounts } from '../../hooks/useGlobalCounts'

/* ─── Constants ─── */

const LABELS = ['Person', 'Idea', 'Institution', 'Place', 'EventWindow', 'Movement', 'Text', 'Evidence', 'Timeframe']
const ERAS = ['Prehistoric', 'Classical', 'Medieval', 'Early Modern', 'Modern', 'Contemporary']
const CONTINENTS = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']

const QUALITY_DIMS = [
  'relationships', 'causes', 'effects', 'frameworks',
  'places', 'texts', 'image', 'wikidata', 'summary',
] as const

const LABEL_COLORS: Record<string, string> = {
  Person: '#4A90D9', Idea: '#6B3FA0', Institution: '#8B4513', Place: '#2E8B57',
  EventWindow: '#C5963A', Movement: '#D35400', Text: '#6B4D1B', Evidence: '#7D8C6C',
  Timeframe: '#9E9A90',
}

const ERA_COLORS: Record<string, string> = {
  Prehistoric: '#6B4D1B', Classical: '#8B4513', Medieval: '#A67C2E',
  'Early Modern': '#C5963A', Modern: '#4A90D9', Contemporary: '#6B3FA0',
}

/* ─── Types ─── */

interface Stats {
  total: number
  byLabel: Record<string, number>
  byEra: Record<string, number>
  byContinent: Record<string, number>
}

interface CompletenessRow {
  slug: string
  name: string
  label: string
  era: string
  importance: number
  relCount: number
  missing: string[]
  score: number // 0-9 based on how many QUALITY_DIMS are satisfied
}

/* ─── Main Component ─── */

export default function AuditDashboard() {
  const globalCounts = useGlobalCounts()
  const [sampleRows, setSampleRows] = useState<CompletenessRow[]>([])
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState<'all' | 'critical' | 'quickwin' | 'orphan' | 'topimportance'>('all')
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState<CompletenessRow[]>([])
  const [searching, setSearching] = useState(false)
  const [topEntities, setTopEntities] = useState<CompletenessRow[]>([])

  // Use global counts for stats
  const stats: Stats | null = globalCounts.total > 0 ? {
    total: globalCounts.total,
    byLabel: globalCounts.byLabel,
    byEra: globalCounts.byEra,
    byContinent: globalCounts.byContinent,
  } : null
  const classCounts = globalCounts.byClass

  useEffect(() => {
    loadDashboard()
  }, [])

  async function loadDashboard() {
    setLoading(true)
    try {
      // Fetch sample for completeness analysis + top importance entities
      const [sample, topImportance] = await Promise.all([
        databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(200)]),
        databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
          Query.orderDesc('importanceScore'), Query.limit(30),
        ]),
      ])
      setSampleRows(sample.documents.map(analyzeDoc))
      setTopEntities(topImportance.documents.map(analyzeDoc))
    } catch (err) {
      console.error('Audit load failed:', err)
    }
    setLoading(false)
  }

  // Search entities by name
  const handleSearch = useCallback(async () => {
    if (!searchQuery.trim()) { setSearchResults([]); return }
    setSearching(true)
    try {
      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.search('name', searchQuery.trim()),
        Query.limit(20),
      ])
      setSearchResults(res.documents.map(analyzeDoc))
    } catch { setSearchResults([]) }
    setSearching(false)
  }, [searchQuery])

  const criticalEntities = useMemo(
    () => sampleRows.filter((r) => r.importance >= 5 && r.score < 5).sort((a, b) => b.importance - a.importance),
    [sampleRows],
  )
  const quickWins = useMemo(
    () => sampleRows.filter((r) => r.score >= 7 && r.missing.length <= 2).sort((a, b) => b.importance - a.importance),
    [sampleRows],
  )
  const orphans = useMemo(() => sampleRows.filter((r) => r.relCount === 0), [sampleRows])

  const filteredRows = useMemo(() => {
    if (filter === 'critical') return criticalEntities
    if (filter === 'quickwin') return quickWins
    if (filter === 'orphan') return orphans
    if (filter === 'topimportance') return topEntities
    return sampleRows.sort((a, b) => a.score - b.score)
  }, [filter, sampleRows, criticalEntities, quickWins, orphans, topEntities])

  // Export CSV
  function exportCSV() {
    const header = 'Name,Slug,Label,Era,Importance,Score,Rels,Missing\n'
    const rows = filteredRows.map((r) =>
      `"${r.name}","${r.slug}","${r.label}","${r.era}",${r.importance},${r.score},${r.relCount},"${r.missing.join(', ')}"`
    ).join('\n')
    const blob = new Blob([header + rows], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `audit-${filter}-${new Date().toISOString().slice(0, 10)}.csv`
    a.click()
    URL.revokeObjectURL(url)
  }

  // Relationship density stats
  const relDensity = useMemo(() => {
    if (sampleRows.length === 0) return { avg: 0, max: 0, zero: 0, pctWithRels: 0 }
    const rels = sampleRows.map((r) => r.relCount)
    const total = rels.reduce((a, b) => a + b, 0)
    return {
      avg: Math.round(total / sampleRows.length * 10) / 10,
      max: Math.max(...rels),
      zero: rels.filter((r) => r === 0).length,
      pctWithRels: Math.round((rels.filter((r) => r > 0).length / sampleRows.length) * 100),
    }
  }, [sampleRows])

  // Completeness heatmap data: label × dimension → percentage
  const heatmap = useMemo(() => {
    const map: Record<string, Record<string, number>> = {}
    for (const label of LABELS) {
      const rows = sampleRows.filter((r) => r.label === label)
      if (rows.length === 0) continue
      map[label] = {}
      for (const dim of QUALITY_DIMS) {
        const count = rows.filter((r) => !r.missing.includes(dim === 'wikidata' ? 'wikidataQid' : dim)).length
        map[label][dim] = Math.round((count / rows.length) * 100)
      }
    }
    return map
  }, [sampleRows])

  if (loading) {
    return (
      <Flex justify="center" align="center" minH="60vh">
        <Spinner size="xl" color="#D4AF37" />
        <Text ml={4} color="#787469">Loading audit data from Appwrite…</Text>
      </Flex>
    )
  }

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      {/* Hero */}
      <Box mb={8}>
        <Text
          fontFamily='"Cinzel", serif'
          fontSize="2xl"
          fontWeight={700}
          color="#2D2A24"
          letterSpacing="0.08em"
        >
          BACKEND AUDIT DASHBOARD
        </Text>
        <Text color="#787469" fontSize="sm" mt={1}>
          Birds-eye view of {stats?.total?.toLocaleString() ?? '…'} entities in Appwrite
        </Text>
      </Box>

      {/* Section 1: Overview Stats */}
      <SectionHeading title="Overview" subtitle="Live counts from Appwrite backend" />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={10}>
        <StatCard value={stats?.total?.toLocaleString() ?? '—'} label="Total Entities" color="#D4AF37" />
        <StatCard value={Object.keys(stats?.byLabel ?? {}).filter((k) => (stats?.byLabel[k] ?? 0) > 0).length.toString()} label="Entity Types" color="#4A90D9" />
        <StatCard value={ERAS.length.toString()} label="Eras" color="#8B4513" />
        <StatCard value={orphans.length.toString()} label="Orphans (sample)" detail="0 relationships" color="#C0392B" />
        <StatCard value={quickWins.length.toString()} label="Quick Wins (sample)" detail="Score 7+ missing ≤2" color="#27AE60" />
        <StatCard value={criticalEntities.length.toString()} label="Critical (sample)" detail="Important but low score" color="#E67E22" />
      </SimpleGrid>

      {/* Section 2: Label Distribution */}
      <SectionHeading title="Entity Distribution" subtitle="Count by label type" />
      <SimpleGrid columns={{ base: 3, md: 5, lg: 9 }} gap={3} mb={10}>
        {LABELS.map((label) => (
          <Box
            key={label}
            bg="#FAFAF8"
            border="1px solid #E4E2DC"
            borderRadius="lg"
            p={4}
            textAlign="center"
            position="relative"
            overflow="hidden"
          >
            <Box position="absolute" top={0} left={0} w="100%" h="3px" bg={LABEL_COLORS[label] ?? '#9E9A90'} />
            <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color={LABEL_COLORS[label]}>
              {(stats?.byLabel[label] ?? 0).toLocaleString()}
            </Text>
            <Text fontSize="xs" color="#787469" mt={1}>{label}</Text>
          </Box>
        ))}
      </SimpleGrid>

      {/* Section 3: Era Distribution */}
      <SectionHeading title="Era Coverage" subtitle="Entity count per canonical era" />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={10}>
        {ERAS.map((era) => {
          const count = stats?.byEra[era] ?? 0
          const maxCount = Math.max(...Object.values(stats?.byEra ?? { '': 1 }))
          const pct = maxCount > 0 ? (count / maxCount) * 100 : 0
          return (
            <Box key={era} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={4}>
              <Flex justify="space-between" align="center" mb={2}>
                <Text fontFamily='"Cormorant Garamond", serif' fontSize="md" fontWeight={700} color="#2D2A24">
                  {era}
                </Text>
                <Text fontSize="sm" fontWeight={600} color={ERA_COLORS[era]}>{count.toLocaleString()}</Text>
              </Flex>
              <Box bg="#E4E2DC" borderRadius="full" h="6px" overflow="hidden">
                <Box bg={ERA_COLORS[era]} h="100%" w={`${pct}%`} borderRadius="full" transition="width 0.5s" />
              </Box>
            </Box>
          )
        })}
      </SimpleGrid>

      {/* Section 4: Continent Distribution */}
      <SectionHeading title="Geographic Coverage" subtitle="Entity count per continent" />
      <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={10}>
        {CONTINENTS.map((c) => (
          <StatCard
            key={c}
            value={(stats?.byContinent[c] ?? 0).toLocaleString()}
            label={c}
            color="#2E8B57"
          />
        ))}
      </SimpleGrid>

      {/* Section 4b: Quick Entity Lookup */}
      <SectionHeading title="Quick Entity Lookup" subtitle="Search entities by name for instant audit" />
      <Flex gap={3} mb={4} align="center">
        <Box position="relative" flex={1} maxW="500px">
          <Input
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
            placeholder="Search entities by name…"
            bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg"
            fontSize="sm" _focus={{ borderColor: '#D4AF37' }}
          />
        </Box>
        <Box as="button" onClick={handleSearch} px={4} py={2} borderRadius="lg"
          bg="#2D2A24" color="#D4AF37" fontSize="sm" fontWeight={600} cursor="pointer"
          display="flex" alignItems="center" gap={2} _hover={{ bg: '#3D3A34' }}
          opacity={searching ? 0.6 : 1}>
          <Search size={14} /> {searching ? 'Searching…' : 'Search'}
        </Box>
      </Flex>
      {searchResults.length > 0 && (
        <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto" mb={10}>
          <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '700px' }}>
            <thead>
              <tr>
                {['Name', 'Label', 'Era', 'Importance', 'Score', 'Rels', 'Missing'].map((h) => (
                  <th key={h} style={thStyle}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {searchResults.map((row, ri) => (
                <tr key={row.slug} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                  <td style={tdStyle}>
                    <RouterLink to={`/entity/${row.slug}`} style={{ color: '#4A90D9', textDecoration: 'none' }}>
                      {row.name}
                    </RouterLink>
                  </td>
                  <td style={tdStyle}>
                    <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={600}
                      bg={LABEL_COLORS[row.label] + '20'} color={LABEL_COLORS[row.label]}>{row.label}</Box>
                  </td>
                  <td style={tdStyle}>{row.era}</td>
                  <td style={{ ...tdStyle, textAlign: 'center' }}>{row.importance}</td>
                  <td style={{ ...tdStyle, textAlign: 'center' }}>
                    <ScoreBadge score={row.score} />
                  </td>
                  <td style={{ ...tdStyle, textAlign: 'center' }}>{row.relCount}</td>
                  <td style={tdStyle}>
                    <Flex gap={1} flexWrap="wrap">
                      {row.missing.slice(0, 3).map((m) => (
                        <Box key={m} as="span" px={1.5} py={0.5} borderRadius="sm" fontSize="10px"
                          bg="#FADBD8" color="#922B21">{m}</Box>
                      ))}
                      {row.missing.length > 3 && (
                        <Box as="span" fontSize="10px" color="#922B21">+{row.missing.length - 3}</Box>
                      )}
                    </Flex>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Box>
      )}
      {searchResults.length === 0 && searchQuery && !searching && (
        <Text fontSize="sm" color="#9E9A90" mb={10}>No results for "{searchQuery}"</Text>
      )}

      {/* Section 4c: Relationship Density */}
      <SectionHeading title="Relationship Density" subtitle="How connected are entities? (from 200-entity sample)" />
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={10}>
        <StatCard value={relDensity.avg.toString()} label="Avg Rels/Entity" color="#4A90D9" />
        <StatCard value={relDensity.max.toString()} label="Max Relationships" color="#27AE60" />
        <StatCard value={relDensity.zero.toString()} label="Zero Rels (Orphans)" color="#C0392B" />
        <StatCard value={`${relDensity.pctWithRels}%`} label="Connected" detail="≥1 relationship" color="#D4AF37" />
      </SimpleGrid>

      {/* Section 4d: Class Distribution */}
      <SectionHeading title="Class Distribution" subtitle="Entity count per Dewey classification class" />
      <SimpleGrid columns={{ base: 2, md: 5 }} gap={3} mb={10}>
        {CLASSES.map((cls) => {
          const count = classCounts[cls.code] ?? 0
          return (
            <RouterLink key={cls.code} to={`/curator/classes/${cls.code}`} style={{ textDecoration: 'none' }}>
              <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" p={3} textAlign="center"
                position="relative" overflow="hidden" transition="all 0.2s"
                _hover={{ transform: 'translateY(-1px)', shadow: 'sm', borderColor: '#D4AF37' }} cursor="pointer">
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#9E9A90" fontWeight={600}>
                  Class {cls.code}
                </Text>
                <Text fontFamily='"Cinzel", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
                  {count.toLocaleString()}
                </Text>
                <Text fontSize="10px" color="#787469" overflow="hidden" textOverflow="ellipsis" whiteSpace="nowrap">{cls.heading}</Text>
              </Box>
            </RouterLink>
          )
        })}
      </SimpleGrid>

      {/* Section 4e: Top Entities by Importance */}
      <SectionHeading title="Top Entities by Importance" subtitle="Highest importance-scored entities in the backend" />
      <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto" mb={10}>
        <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '600px' }}>
          <thead>
            <tr>
              <th style={thStyle}>#</th>
              {['Name', 'Label', 'Era', 'Importance', 'Score', 'Missing'].map((h) => (
                <th key={h} style={thStyle}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {topEntities.slice(0, 15).map((row, ri) => (
              <tr key={row.slug} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                <td style={{ ...tdStyle, textAlign: 'center', fontWeight: 600 }}>{ri + 1}</td>
                <td style={tdStyle}>
                  <RouterLink to={`/entity/${row.slug}`} style={{ color: '#4A90D9', textDecoration: 'none' }}>
                    {row.name}
                  </RouterLink>
                </td>
                <td style={tdStyle}>
                  <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={600}
                    bg={LABEL_COLORS[row.label] + '20'} color={LABEL_COLORS[row.label]}>{row.label}</Box>
                </td>
                <td style={tdStyle}>{row.era}</td>
                <td style={{ ...tdStyle, textAlign: 'center' }}>
                  <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={700}
                    bg="#FDF8ED" color="#96770B">{row.importance}</Box>
                </td>
                <td style={{ ...tdStyle, textAlign: 'center' }}>
                  <ScoreBadge score={row.score} />
                </td>
                <td style={tdStyle}>
                  <Flex gap={1} flexWrap="wrap">
                    {row.missing.slice(0, 3).map((m) => (
                      <Box key={m} as="span" px={1.5} py={0.5} borderRadius="sm" fontSize="10px"
                        bg="#FADBD8" color="#922B21">{m}</Box>
                    ))}
                  </Flex>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Box>

      {/* Section 5: Completeness Heatmap */}
      <SectionHeading title="Completeness Heatmap" subtitle="Percentage of entities with each quality dimension (from 200-entity sample)" />
      <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto" mb={10}>
        <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '700px' }}>
          <thead>
            <tr>
              <th style={thStyle}>Label</th>
              {QUALITY_DIMS.map((d) => <th key={d} style={thStyle}>{d}</th>)}
            </tr>
          </thead>
          <tbody>
            {Object.entries(heatmap).map(([label, dims], ri) => (
              <tr key={label} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                <td style={{ ...tdStyle, fontWeight: 600 }}>{label}</td>
                {QUALITY_DIMS.map((d) => {
                  const pct = dims[d] ?? 0
                  return (
                    <td key={d} style={{ ...tdStyle, textAlign: 'center' }}>
                      <Box
                        display="inline-block"
                        px={2}
                        py={0.5}
                        borderRadius="md"
                        fontSize="xs"
                        fontWeight={600}
                        bg={pct >= 80 ? '#D5F5E3' : pct >= 40 ? '#FEF9E7' : '#FADBD8'}
                        color={pct >= 80 ? '#196F3D' : pct >= 40 ? '#7D6608' : '#922B21'}
                      >
                        {pct}%
                      </Box>
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </Box>

      {/* Section 6: Entity Audit Table */}
      <SectionHeading title="Entity Audit Queue" subtitle="Entities needing attention — sorted by completeness score" />
      <Flex gap={3} mb={4} flexWrap="wrap" justify="space-between" align="center">
        <Flex gap={2} flexWrap="wrap">
          {([
            { key: 'all' as const, label: `All (${sampleRows.length})` },
            { key: 'critical' as const, label: `Critical (${criticalEntities.length})` },
            { key: 'quickwin' as const, label: `Quick Wins (${quickWins.length})` },
            { key: 'orphan' as const, label: `Orphans (${orphans.length})` },
            { key: 'topimportance' as const, label: `Top Importance (${topEntities.length})` },
          ]).map((f) => (
            <Box
              key={f.key}
              as="button"
              onClick={() => setFilter(f.key)}
              px={4}
              py={2}
              borderRadius="full"
              fontSize="sm"
              fontWeight={600}
              bg={filter === f.key ? '#2D2A24' : '#F5F4F0'}
              color={filter === f.key ? '#D4AF37' : '#787469'}
              border="1px solid"
              borderColor={filter === f.key ? '#2D2A24' : '#E4E2DC'}
              cursor="pointer"
              transition="all 0.2s"
            >
              {f.label}
            </Box>
          ))}
        </Flex>
        <Box as="button" onClick={exportCSV} px={4} py={2} borderRadius="lg"
          bg="#F5F4F0" color="#787469" fontSize="sm" fontWeight={600} cursor="pointer"
          display="flex" alignItems="center" gap={2} border="1px solid #E4E2DC"
          _hover={{ bg: '#E4E2DC' }}>
          <Download size={14} /> Export CSV
        </Box>
      </Flex>

      <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto" mb={10}>
        <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '800px' }}>
          <thead>
            <tr>
              {['Name', 'Label', 'Era', 'Importance', 'Score', 'Rels', 'Missing Fields'].map((h) => (
                <th key={h} style={thStyle}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filteredRows.slice(0, 50).map((row, ri) => (
              <tr key={row.slug} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                <td style={tdStyle}>
                  <RouterLink to={`/entity/${row.slug}`} style={{ color: '#4A90D9', textDecoration: 'none' }}>
                    {row.name}
                  </RouterLink>
                </td>
                <td style={tdStyle}>
                  <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={600}
                    bg={LABEL_COLORS[row.label] + '20'} color={LABEL_COLORS[row.label]}>
                    {row.label}
                  </Box>
                </td>
                <td style={tdStyle}>{row.era}</td>
                <td style={{ ...tdStyle, textAlign: 'center' }}>{row.importance}</td>
                <td style={{ ...tdStyle, textAlign: 'center' }}>
                  <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={700}
                    bg={row.score >= 7 ? '#D5F5E3' : row.score >= 4 ? '#FEF9E7' : '#FADBD8'}
                    color={row.score >= 7 ? '#196F3D' : row.score >= 4 ? '#7D6608' : '#922B21'}>
                    {row.score}/9
                  </Box>
                </td>
                <td style={{ ...tdStyle, textAlign: 'center' }}>{row.relCount}</td>
                <td style={tdStyle}>
                  <Flex gap={1} flexWrap="wrap">
                    {row.missing.map((m) => (
                      <Box key={m} as="span" px={1.5} py={0.5} borderRadius="sm" fontSize="10px"
                        bg="#FADBD8" color="#922B21">
                        {m}
                      </Box>
                    ))}
                    {row.missing.length === 0 && (
                      <Box as="span" fontSize="10px" color="#27AE60" fontWeight={600}>✓ Complete</Box>
                    )}
                  </Flex>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Box>

      {/* Section 7: Quick Navigation */}
      <SectionHeading title="Curator Tools" subtitle="Navigate to specialized audit views" />
      <SimpleGrid columns={{ base: 1, md: 2, lg: 5 }} gap={4}>
        <NavCard to="/curator/triage" icon={AlertTriangle} label="Triage System" desc="Automated audit tasks & priorities" color="#E67E22" />
        <NavCard to="/curator/classes" icon={Layers} label="Class Browser" desc="All 10 Dewey classes & divisions" color="#D4AF37" />
        <NavCard to="/curator/people" icon={Users} label="People Hub" desc="Browse & edit Class 2 divisions" color="#4A90D9" />
        <NavCard to="/curator/audit/guide" icon={BookOpen} label="Audit Guide" desc="Quality rubric & conventions" color="#27AE60" />
        <NavCard to="/catalog" icon={Globe} label="Full Catalog" desc="Browse all 392K+ entities" color="#6B3FA0" />
      </SimpleGrid>
    </Box>
  )
}

/* ─── Sub-components ─── */

function ScoreBadge({ score }: { score: number }) {
  return (
    <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={700}
      bg={score >= 7 ? '#D5F5E3' : score >= 4 ? '#FEF9E7' : '#FADBD8'}
      color={score >= 7 ? '#196F3D' : score >= 4 ? '#7D6608' : '#922B21'}>
      {score}/9
    </Box>
  )
}

function NavCard({ to, icon: Icon, label, desc, color }: {
  to: string; icon: React.ElementType; label: string; desc: string; color: string
}) {
  return (
    <RouterLink to={to} style={{ textDecoration: 'none' }}>
      <Box
        bg="#FAFAF8"
        border="1px solid #E4E2DC"
        borderRadius="lg"
        p={5}
        transition="all 0.2s"
        _hover={{ transform: 'translateY(-2px)', shadow: 'md', borderColor: color }}
        cursor="pointer"
      >
        <Flex align="center" gap={3} mb={2}>
          <Box p={2} borderRadius="md" bg={color + '15'}>
            <Icon size={20} color={color} />
          </Box>
          <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
            {label}
          </Text>
        </Flex>
        <Text fontSize="sm" color="#787469">{desc}</Text>
      </Box>
    </RouterLink>
  )
}

/* ─── Helpers ─── */

function analyzeDoc(doc: Models.Document): CompletenessRow {
  const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
  const rels = details.relationships ?? []
  const missing: string[] = []

  if (rels.length === 0) missing.push('relationships')
  if ((details.causes ?? []).length === 0) missing.push('causes')
  if ((details.effects ?? []).length === 0) missing.push('effects')
  if (((doc.frameworks as string[]) ?? []).length === 0) missing.push('frameworks')
  if ((details.places ?? []).length === 0) missing.push('places')
  if ((details.texts ?? []).length === 0) missing.push('texts')
  if (!doc.imageUrl) missing.push('image')
  if (!doc.wikidataQid) missing.push('wikidataQid')
  if (((doc.summary as string) ?? '').length < 50) missing.push('summary')

  return {
    slug: doc.slug as string,
    name: doc.name as string,
    label: doc.label as string,
    era: doc.era as string,
    importance: (doc.importanceScore as number) ?? 0,
    relCount: rels.length,
    missing,
    score: QUALITY_DIMS.length - missing.length,
  }
}

const thStyle: React.CSSProperties = {
  padding: '10px 12px',
  textAlign: 'left',
  fontSize: '11px',
  fontWeight: 700,
  color: '#9E9A90',
  borderBottom: '2px solid #E4E2DC',
  fontFamily: '"Cinzel", serif',
  textTransform: 'uppercase',
  letterSpacing: '0.08em',
  whiteSpace: 'nowrap',
}

const tdStyle: React.CSSProperties = {
  padding: '8px 12px',
  fontSize: '13px',
  color: '#2D2A24',
  borderBottom: '1px solid #EEEDEA',
  fontFamily: '"Inter", sans-serif',
}
