import React, { useEffect, useState, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, RefreshCw, Database, CheckCircle2, Clock,
  TrendingUp, AlertTriangle, Layers, Zap,
  ChevronDown, ChevronRight, Activity, Server, Cloud,
  FileText, MapPin, Network, Brain, Shield,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { CLASSES, DIVISIONS } from '../../constants/callNumbers'

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Types                                                                       */
/* ─────────────────────────────────────────────────────────────────────────── */

interface ClassStats {
  classCode: number
  heading: string
  total: number
  enriched: number
  highQuality: number
  stubs: number
  loaded: boolean
  divisions?: DivisionStats[]
  fieldBreakdown?: FieldBreakdown
}

interface DivisionStats {
  code: string
  heading: string
  total: number
  enriched: number
}

interface FieldBreakdown {
  hasSummary: number
  hasCauses: number
  hasEffects: number
  hasEdges: number
  hasPlaces: number
  hasFrameworks: number
  hasSignificance: number
  total: number
}

interface LocalJob {
  job_id: string; bot: string; status: string; model: string
  count: number; started: string; finished: string | null
  log: string[]; pid: number | null
}

interface GHRun {
  name: string; status: string; conclusion: string | null
  runId: number; startedAt: string | null; updatedAt: string | null; htmlUrl: string
}

interface BotStatus {
  serverOnline: boolean; ollamaRunning: boolean
  activeJobs: LocalJob[]; ghRuns: GHRun[]
}

interface OverallStats {
  total: number; enriched: number; highQuality: number; stubs: number
}

interface RecentEntity {
  $id: string; name: string; slug: string; era: string
  importanceScore: number; $updatedAt: string
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Theme                                                                       */
/* ─────────────────────────────────────────────────────────────────────────── */

const BG      = '#0B1120'
const CARD_BG = '#111827'
const BORDER  = 'rgba(99,102,241,0.15)'
const ACCENT  = '#6366F1'
const GREEN   = '#10B981'
const ORANGE  = '#F59E0B'
const RED     = '#EF4444'
const MUTED   = '#6B7280'
const TEXT    = '#F1F5F9'
const TEXT_DIM = '#94A3B8'

const CLASS_COLORS: Record<number, string> = {
  0: '#8B5CF6', 1: '#6366F1', 2: '#3B82F6', 3: '#06B6D4',
  4: '#10B981', 5: '#F59E0B', 6: '#F97316', 7: '#EF4444',
  8: '#EC4899', 9: '#A855F7',
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Helpers                                                                     */
/* ─────────────────────────────────────────────────────────────────────────── */

async function localGet<T>(endpoint: string): Promise<T | null> {
  try {
    const r = await fetch(`/local-bots${endpoint}`, { cache: 'no-store' })
    if (!r.ok) return null
    return (await r.json()) as T
  } catch { return null }
}

function pct(n: number, d: number) { return d > 0 ? ((n / d) * 100).toFixed(1) : '0.0' }

function relTime(iso?: string | null): string {
  if (!iso) return 'never'
  const s = Math.max(0, (Date.now() - new Date(iso).getTime()) / 1000)
  if (s < 60) return `${Math.floor(s)}s ago`
  if (s < 3600) return `${Math.floor(s / 60)}m ago`
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`
  return `${Math.floor(s / 86400)}d ago`
}

function ProgressBar({ value, max, color = ACCENT, height = 8 }: {
  value: number; max: number; color?: string; height?: number
}) {
  const p = max > 0 ? Math.min(100, (value / max) * 100) : 0
  return (
    <Box bg="rgba(255,255,255,0.05)" borderRadius="full" overflow="hidden" h={`${height}px`}>
      <Box h="100%" w={`${p}%`} bg={color} borderRadius="full"
        transition="width 0.6s ease" style={{ minWidth: p > 0 ? '3px' : '0' }} />
    </Box>
  )
}

function ScoreBadge({ score }: { score: number }) {
  const c = score >= 7 ? GREEN : score >= 4 ? ORANGE : score > 0 ? RED : MUTED
  return (
    <Box display="inline-block" px="5px" py="1px" borderRadius="4px" bg={`${c}20`} border={`1px solid ${c}40`}>
      <Text fontSize="10px" fontWeight={700} color={c}>{score}</Text>
    </Box>
  )
}

function EraBadge({ era }: { era: string }) {
  const map: Record<string, string> = {
    prehistoric: '#6B4D1B', classical: '#8B4513', medieval: '#A67C2E',
    'early modern': '#C5963A', modern: '#4A90D9', contemporary: '#6B3FA0',
  }
  const c = map[(era || '').toLowerCase()] ?? MUTED
  return (
    <Box display="inline-block" px="5px" py="1px" borderRadius="4px" bg={`${c}20`}>
      <Text fontSize="9px" fontWeight={600} color={c} textTransform="capitalize">{era || '—'}</Text>
    </Box>
  )
}

function StatusDot({ online }: { online: boolean }) {
  return <Box w="8px" h="8px" borderRadius="full" bg={online ? GREEN : RED}
    style={{ boxShadow: online ? `0 0 6px ${GREEN}` : 'none' }} />
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  ClassRow — expandable class row                                             */
/* ─────────────────────────────────────────────────────────────────────────── */

function ClassRow({ cs, onExpand }: { cs: ClassStats; onExpand: (code: number) => void }) {
  const [open, setOpen] = useState(false)
  const color = CLASS_COLORS[cs.classCode] ?? ACCENT

  return (
    <Box border="1px solid" borderColor={open ? `${color}40` : BORDER}
      borderRadius="10px" overflow="hidden" bg={open ? `${color}06` : CARD_BG} transition="all 0.2s">
      {/* Header */}
      <Flex as="button" w="100%" align="center" gap={3} p={4} cursor="pointer"
        onClick={() => { const next = !open; setOpen(next); if (next && !cs.fieldBreakdown) onExpand(cs.classCode) }}
        _hover={{ bg: `${color}0A` }} bg="transparent" border="none" textAlign="left">
        <Box w="4px" h="32px" borderRadius="full" bg={color} flexShrink={0} />
        <Box flex={1} minW={0}>
          <Flex align="center" gap={2} mb={1}>
            <Text fontSize="11px" fontFamily='"JetBrains Mono", monospace'
              color={color} fontWeight={700} letterSpacing="0.1em">Class {cs.classCode}</Text>
            <Text fontSize="12px" fontWeight={600} color={TEXT} noOfLines={1}>{cs.heading}</Text>
          </Flex>
          <Flex align="center" gap={3}>
            <Box flex={1}>
              <ProgressBar value={cs.enriched} max={cs.total} color={color} height={5} />
            </Box>
            <Text fontSize="11px" color={color} fontWeight={700} minW="40px" textAlign="right">
              {pct(cs.enriched, cs.total)}%
            </Text>
          </Flex>
        </Box>
        <SimpleGrid columns={3} gap={3} minW="200px">
          {[
            { val: cs.total, label: 'total', col: TEXT },
            { val: cs.enriched, label: 'enriched', col: GREEN },
            { val: cs.stubs, label: 'stubs', col: ORANGE },
          ].map(({ val, label, col }) => (
            <Box key={label} textAlign="center">
              <Text fontSize="15px" fontWeight={800} color={col}>{val.toLocaleString()}</Text>
              <Text fontSize="9px" color={MUTED} textTransform="uppercase" letterSpacing="0.05em">{label}</Text>
            </Box>
          ))}
        </SimpleGrid>
        <Box textAlign="center" minW="60px">
          <Text fontSize="14px" fontWeight={800} color={TEXT}>{cs.highQuality.toLocaleString()}</Text>
          <Text fontSize="9px" color={MUTED}>HQ ({pct(cs.highQuality, cs.total)}%)</Text>
        </Box>
        {open ? <ChevronDown size={16} color={MUTED} /> : <ChevronRight size={16} color={MUTED} />}
      </Flex>

      {/* Expanded */}
      {open && (
        <Box px={4} pb={4} borderTop={`1px solid ${color}20`}>
          {/* Field breakdown */}
          {cs.fieldBreakdown ? (
            <Box mb={4} pt={3}>
              <Text fontSize="10px" color={MUTED} letterSpacing="0.1em"
                textTransform="uppercase" fontFamily='"Cinzel", serif' mb={2}>
                Field Coverage — {cs.fieldBreakdown.total} entities sampled
              </Text>
              <SimpleGrid columns={{ base: 2, md: 4, lg: 7 }} gap={2}>
                {[
                  { label: 'Summary', val: cs.fieldBreakdown.hasSummary, icon: FileText, c: '#6366F1' },
                  { label: 'Causes', val: cs.fieldBreakdown.hasCauses, icon: TrendingUp, c: '#8B5CF6' },
                  { label: 'Effects', val: cs.fieldBreakdown.hasEffects, icon: Activity, c: '#06B6D4' },
                  { label: 'Edges', val: cs.fieldBreakdown.hasEdges, icon: Network, c: '#3B82F6' },
                  { label: 'Places', val: cs.fieldBreakdown.hasPlaces, icon: MapPin, c: '#10B981' },
                  { label: 'Frameworks', val: cs.fieldBreakdown.hasFrameworks, icon: Brain, c: '#F97316' },
                  { label: 'Significance', val: cs.fieldBreakdown.hasSignificance, icon: Shield, c: '#EF4444' },
                ].map(({ label, val, icon: Icon, c }) => {
                  const t = cs.fieldBreakdown!.total
                  return (
                    <Box key={label} p={2} bg={`${c}0A`} borderRadius="8px" border={`1px solid ${c}20`}>
                      <Flex align="center" gap={1} mb={1}>
                        <Icon size={10} color={c} />
                        <Text fontSize="9px" color={c} fontWeight={600}>{label}</Text>
                      </Flex>
                      <Text fontSize="14px" fontWeight={800} color={TEXT}>{val.toLocaleString()}</Text>
                      <ProgressBar value={val} max={t} color={c} height={3} />
                      <Text fontSize="9px" color={MUTED} mt="2px">{pct(val, t)}%</Text>
                    </Box>
                  )
                })}
              </SimpleGrid>
            </Box>
          ) : (
            <Flex align="center" gap={2} pt={3} mb={4}>
              <Spinner size="sm" color={color} />
              <Text fontSize="12px" color={MUTED}>Loading field breakdown…</Text>
            </Flex>
          )}
          {/* Division list */}
          {cs.divisions && cs.divisions.filter(d => d.total > 0).length > 0 && (
            <Box>
              <Text fontSize="10px" color={MUTED} letterSpacing="0.1em"
                textTransform="uppercase" fontFamily='"Cinzel", serif' mb={2}>Divisions</Text>
              <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={2}>
                {cs.divisions.filter(d => d.total > 0).map(div => (
                  <Flex key={div.code} align="center" gap={2} p={2}
                    bg="rgba(255,255,255,0.02)" borderRadius="6px" border={`1px solid ${color}15`}>
                    <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                      color={color} fontWeight={700} minW="32px">{div.code}</Text>
                    <Box flex={1} minW={0}>
                      <Text fontSize="10px" color={TEXT_DIM} noOfLines={1}>{div.heading}</Text>
                      <Flex align="center" gap={1} mt="2px">
                        <Box flex={1}><ProgressBar value={div.enriched} max={div.total} color={color} height={3} /></Box>
                        <Text fontSize="9px" color={MUTED} minW="28px">{pct(div.enriched, div.total)}%</Text>
                      </Flex>
                    </Box>
                    <Box textAlign="right">
                      <Text fontSize="11px" fontWeight={700} color={GREEN}>{div.enriched}</Text>
                      <Text fontSize="9px" color={MUTED}>/{div.total}</Text>
                    </Box>
                  </Flex>
                ))}
              </SimpleGrid>
            </Box>
          )}
        </Box>
      )}
    </Box>
  )
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Main Component                                                              */
/* ─────────────────────────────────────────────────────────────────────────── */

export default function EnrichmentProgress() {
  const navigate = useNavigate()
  const [overall, setOverall] = useState<OverallStats | null>(null)
  const [classes, setClasses] = useState<ClassStats[]>([])
  const [recent, setRecent] = useState<RecentEntity[]>([])
  const [bots, setBots] = useState<BotStatus>({ serverOnline: false, ollamaRunning: false, activeJobs: [], ghRuns: [] })
  const [loading, setLoading] = useState(true)
  const [lastRefresh, setLastRefresh] = useState<Date | null>(null)
  const [error, setError] = useState<string | null>(null)

  const load = useCallback(async () => {
    setLoading(true); setError(null)
    try {
      const [totalRes, enrichedRes, hqRes] = await Promise.all([
        databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.limit(1)]),
        databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.greaterThanEqual('importanceScore', 4), Query.limit(1)]),
        databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.greaterThanEqual('importanceScore', 7), Query.limit(1)]),
      ])
      const total = totalRes.total, enriched = enrichedRes.total, hq = hqRes.total
      setOverall({ total, enriched, highQuality: hq, stubs: total - enriched })

      const classPairs = await Promise.all(
        CLASSES.map(async cls => {
          const prefix = cls.code.toString()
          const [ct, ce, ch] = await Promise.all([
            databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.startsWith('callNumber', prefix), Query.limit(1)]),
            databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.startsWith('callNumber', prefix), Query.greaterThanEqual('importanceScore', 4), Query.limit(1)]),
            databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.startsWith('callNumber', prefix), Query.greaterThanEqual('importanceScore', 7), Query.limit(1)]),
          ])
          return { classCode: cls.code, heading: cls.heading, total: ct.total, enriched: ce.total, highQuality: ch.total, stubs: ct.total - ce.total, loaded: true } as ClassStats
        })
      )
      setClasses(classPairs)

      const recentRes = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.greaterThanEqual('importanceScore', 4), Query.orderDesc('$updatedAt'),
        Query.limit(25), Query.select(['$id', 'name', 'slug', 'era', 'importanceScore', '$updatedAt']),
      ])
      setRecent(recentRes.documents.map(d => ({
        $id: d.$id as string, name: (d.name as string) ?? '—', slug: (d.slug as string) ?? '',
        era: (d.era as string) ?? '', importanceScore: (d.importanceScore as number) ?? 0,
        $updatedAt: (d.$updatedAt as string) ?? '',
      })))
      setLastRefresh(new Date())
    } catch (err) { setError(err instanceof Error ? err.message : 'Failed to load stats') }
    setLoading(false)
  }, [])

  const loadBots = useCallback(async () => {
    const [health, allJobs, ghStatus] = await Promise.all([
      localGet<{ ollama: { running: boolean }; activeJobs: number }>('/health'),
      localGet<Record<string, LocalJob>>('/bots/status'),
      localGet<{ runs: GHRun[] }>('/github/status'),
    ])
    const activeJobs = allJobs
      ? Object.values(allJobs).filter(j => j.status === 'running' || j.status === 'queued')
      : []
    setBots({
      serverOnline: !!health, ollamaRunning: health?.ollama?.running ?? false,
      activeJobs,
      ghRuns: (ghStatus?.runs ?? []).filter((r: GHRun & { error?: string }) => !r.error),
    })
  }, [])

  const expandClass = useCallback(async (classCode: number) => {
    const prefix = classCode.toString()
    const classDivisions = DIVISIONS.filter(d => d.parentClass === classCode)
    const divStats = await Promise.all(
      classDivisions.map(async div => {
        const [dt, de] = await Promise.all([
          databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.startsWith('callNumber', div.code), Query.limit(1)]),
          databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [Query.startsWith('callNumber', div.code), Query.greaterThanEqual('importanceScore', 4), Query.limit(1)]),
        ])
        return { code: div.code, heading: div.heading, total: dt.total, enriched: de.total }
      })
    )
    let fieldBreakdown: FieldBreakdown | undefined
    try {
      const sample = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.startsWith('callNumber', prefix), Query.limit(500),
        Query.select(['$id', 'summary', 'importanceScore', 'historicalSignificance', 'frameworks', 'detailsJson']),
      ])
      let hasSummary = 0, hasCauses = 0, hasEffects = 0, hasEdges = 0, hasPlaces = 0, hasFrameworks = 0, hasSignificance = 0
      for (const doc of sample.documents) {
        const summary = (doc.summary as string) ?? ''
        if (summary.length >= 600) hasSummary++
        if (doc.historicalSignificance) hasSignificance++
        if (((doc.frameworks as string[]) ?? []).length > 0) hasFrameworks++
        try {
          const dj = doc.detailsJson as string
          if (dj) {
            const details = JSON.parse(dj)
            if ((details.causes ?? []).length > 0) hasCauses++
            if ((details.effects ?? []).length > 0) hasEffects++
            if ((details.relationships ?? []).length > 0) hasEdges++
            if ((details.places ?? []).length > 0) hasPlaces++
          }
        } catch { /* ignore */ }
      }
      fieldBreakdown = { hasSummary, hasCauses, hasEffects, hasEdges, hasPlaces, hasFrameworks, hasSignificance, total: sample.documents.length }
    } catch { /* best effort */ }
    setClasses(prev => prev.map(cs => cs.classCode === classCode ? { ...cs, divisions: divStats, fieldBreakdown } : cs))
  }, [])

  useEffect(() => { load(); loadBots() }, [load, loadBots])
  useEffect(() => { const id = setInterval(load, 60_000); return () => clearInterval(id) }, [load])
  useEffect(() => { const id = setInterval(loadBots, 5_000); return () => clearInterval(id) }, [loadBots])

  const enrichPct = overall ? parseFloat(pct(overall.enriched, overall.total)) : 0

  return (
    <Box minH="100vh" bg={BG} color={TEXT} fontFamily="Inter, sans-serif">
      {/* ── Header ── */}
      <Box bg="rgba(17,24,39,0.95)" borderBottom={`1px solid ${BORDER}`}
        backdropFilter="blur(8px)" px={8} py={5} position="sticky" top={0} zIndex={10}>
        <Flex align="center" justify="space-between" maxW="1400px" mx="auto">
          <Flex align="center" gap={4}>
            <Box as="button" onClick={() => navigate('/curator')} display="flex"
              alignItems="center" gap={2} color={MUTED} fontSize="13px"
              cursor="pointer" _hover={{ color: TEXT }} bg="transparent" border="none" p={0}>
              <ChevronLeft size={16} /> Curator
            </Box>
            <Text color="rgba(99,102,241,0.4)" fontSize="12px">›</Text>
            <Flex align="center" gap={2}>
              <TrendingUp size={18} color={ACCENT} />
              <Text fontSize="18px" fontWeight={700} color={TEXT}
                fontFamily="'Cinzel', serif" letterSpacing="0.04em">Enrichment Progress</Text>
            </Flex>
          </Flex>
          <Flex align="center" gap={3}>
            {lastRefresh && <Text fontSize="11px" color={MUTED}>Updated {lastRefresh.toLocaleTimeString()}</Text>}
            <Box as="button" onClick={() => { load(); loadBots() }} display="flex"
              alignItems="center" gap="6px" px={3} py="6px" borderRadius="6px"
              bg={`${ACCENT}15`} border={`1px solid ${ACCENT}40`} color={ACCENT}
              fontSize="12px" fontWeight={600} cursor="pointer" _hover={{ bg: `${ACCENT}25` }}>
              <RefreshCw size={12} /> Refresh
            </Box>
          </Flex>
        </Flex>
      </Box>

      <Box maxW="1400px" mx="auto" px={8} py={8}>
        {error && (
          <Flex align="center" gap={3} p={4} mb={6}
            bg="rgba(239,68,68,0.08)" border="1px solid rgba(239,68,68,0.25)" borderRadius="8px">
            <AlertTriangle size={16} color={RED} />
            <Text fontSize="13px" color={RED}>{error}</Text>
          </Flex>
        )}

        {loading && !overall ? <Flex justify="center" py={16}><Spinner color={ACCENT} size="lg" /></Flex> : (
          <>
            {/* ── Hero Stats ── */}
            <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
              {[
                { label: 'Total Entities', value: overall?.total ?? 0, icon: Database, color: '#6366F1' },
                { label: 'Enriched', value: overall?.enriched ?? 0, icon: CheckCircle2, color: GREEN },
                { label: 'Stubs Remaining', value: overall?.stubs ?? 0, icon: AlertTriangle, color: ORANGE },
                { label: 'High Quality (7–10)', value: overall?.highQuality ?? 0, icon: Zap, color: '#F59E0B' },
              ].map(({ label, value, icon: Icon, color }) => (
                <Box key={label} p={4} bg={CARD_BG} border="1px solid" borderColor={`${color}25`}
                  borderRadius="10px" position="relative" overflow="hidden">
                  <Box position="absolute" top={0} left={0} right={0} h="2px"
                    bg={`linear-gradient(90deg, ${color} 0%, transparent 100%)`} />
                  <Flex align="center" justify="space-between" mb={2}>
                    <Text fontSize="11px" color={MUTED} textTransform="uppercase" letterSpacing="0.08em">{label}</Text>
                    <Icon size={14} color={color} />
                  </Flex>
                  <Text fontSize="26px" fontWeight={800} color={TEXT}>{value.toLocaleString()}</Text>
                </Box>
              ))}
            </SimpleGrid>

            {/* ── Overall Progress Bar ── */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
              <Flex align="center" justify="space-between" mb={3}>
                <Flex align="center" gap={2}>
                  <TrendingUp size={16} color={ACCENT} />
                  <Text fontSize="14px" fontWeight={700} color={TEXT}>Overall Enrichment Progress</Text>
                </Flex>
                <Text fontSize="28px" fontWeight={800} color={ACCENT}>{enrichPct.toFixed(1)}%</Text>
              </Flex>
              <ProgressBar value={overall?.enriched ?? 0} max={overall?.total ?? 1} color={ACCENT} height={14} />
              <Flex justify="space-between" mt={2}>
                <Text fontSize="11px" color={MUTED}>{overall?.enriched.toLocaleString()} enriched of {overall?.total.toLocaleString()} total</Text>
                <Text fontSize="11px" color={ORANGE} fontWeight={600}>{overall?.stubs.toLocaleString()} stubs remaining</Text>
              </Flex>
              <Flex gap={0} mt={3} borderRadius="6px" overflow="hidden" h="8px">
                <Box h="100%" style={{ width: `${pct(overall?.highQuality ?? 0, overall?.total ?? 1)}%` }} bg={GREEN} />
                <Box h="100%" style={{ width: `${pct((overall?.enriched ?? 0) - (overall?.highQuality ?? 0), overall?.total ?? 1)}%` }} bg={ORANGE} />
                <Box h="100%" flex={1} bg="rgba(255,255,255,0.05)" />
              </Flex>
              <Flex gap={4} mt="6px">
                {[{ c: GREEN, label: `Score 7–10: ${overall?.highQuality.toLocaleString()}` },
                  { c: ORANGE, label: `Score 4–6: ${((overall?.enriched ?? 0) - (overall?.highQuality ?? 0)).toLocaleString()}` },
                  { c: 'rgba(255,255,255,0.1)', label: `Score 0–3: ${overall?.stubs.toLocaleString()}` }].map(({ c, label }) => (
                  <Flex key={label} align="center" gap="6px">
                    <Box w="8px" h="8px" borderRadius="full" bg={c} />
                    <Text fontSize="10px" color={MUTED}>{label}</Text>
                  </Flex>
                ))}
              </Flex>
            </Box>

            {/* ── Bot Status ── */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
              <Flex align="center" gap={2} mb={4}>
                <Activity size={16} color={ACCENT} />
                <Text fontSize="14px" fontWeight={700} color={TEXT}>Active Bot Status</Text>
                <Box ml={2} px={2} py="2px" borderRadius="4px"
                  bg={bots.serverOnline ? `${GREEN}15` : `${RED}15`}
                  border={`1px solid ${bots.serverOnline ? GREEN : RED}40`}>
                  <Text fontSize="9px" fontWeight={700} color={bots.serverOnline ? GREEN : RED}>
                    {bots.serverOnline ? 'BOT SERVER ONLINE' : 'BOT SERVER OFFLINE'}
                  </Text>
                </Box>
              </Flex>
              <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
                {/* Local */}
                <Box p={3} bg="rgba(255,255,255,0.02)" borderRadius="8px"
                  border={`1px solid ${bots.ollamaRunning ? `${GREEN}30` : `${MUTED}20`}`}>
                  <Flex align="center" gap={2} mb={2}>
                    <Server size={14} color={bots.ollamaRunning ? GREEN : MUTED} />
                    <Text fontSize="12px" fontWeight={700} color={TEXT}>Local Ollama (port 11434)</Text>
                    <StatusDot online={bots.ollamaRunning} />
                  </Flex>
                  {bots.activeJobs.length === 0
                    ? <Text fontSize="11px" color={MUTED}>No active local jobs</Text>
                    : bots.activeJobs.slice(0, 5).map(job => (
                      <Flex key={job.job_id} align="center" gap={2} py={1} px={2}
                        bg="rgba(16,185,129,0.05)" borderRadius="6px" mb={1}>
                        <Box w="6px" h="6px" borderRadius="full" bg={GREEN}
                          style={{ boxShadow: `0 0 4px ${GREEN}` }} flexShrink={0} />
                        <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                          color={TEXT_DIM} noOfLines={1} flex={1}>{job.job_id}</Text>
                        <Text fontSize="10px" color={GREEN} fontWeight={600}>{job.model}</Text>
                        <Text fontSize="9px" color={MUTED}>{relTime(job.started)}</Text>
                      </Flex>
                    ))
                  }
                </Box>
                {/* Cloud */}
                <Box p={3} bg="rgba(255,255,255,0.02)" borderRadius="8px"
                  border={`1px solid ${bots.ghRuns.some(r => r.status === 'in_progress') ? `${ACCENT}30` : `${MUTED}20`}`}>
                  <Flex align="center" gap={2} mb={2}>
                    <Cloud size={14} color={ACCENT} />
                    <Text fontSize="12px" fontWeight={700} color={TEXT}>Cloud Bots (GitHub Actions)</Text>
                    <StatusDot online={bots.ghRuns.some(r => r.status === 'in_progress')} />
                  </Flex>
                  {bots.ghRuns.length === 0
                    ? <Text fontSize="11px" color={MUTED}>No recent cloud runs available</Text>
                    : bots.ghRuns.slice(0, 5).map((run, i) => {
                        const isRunning = run.status === 'in_progress'
                        const dotColor = isRunning ? ACCENT : run.conclusion === 'success' ? GREEN : run.conclusion === 'failure' ? RED : MUTED
                        return (
                          <Flex key={i} align="center" gap={2} py={1} px={2} bg={`${dotColor}08`} borderRadius="6px" mb={1}>
                            <Box w="6px" h="6px" borderRadius="full" bg={dotColor}
                              style={isRunning ? { boxShadow: `0 0 4px ${dotColor}` } : {}} flexShrink={0} />
                            <Text fontSize="10px" color={TEXT_DIM} noOfLines={1} flex={1}>{run.name}</Text>
                            <Text fontSize="9px" color={MUTED}>{relTime(run.updatedAt)}</Text>
                          </Flex>
                        )
                      })
                  }
                </Box>
              </SimpleGrid>
            </Box>

            {/* ── Per-Class Breakdown ── */}
            <Box mb={6}>
              <Flex align="center" gap={2} mb={4}>
                <Layers size={16} color={ACCENT} />
                <Text fontSize="16px" fontWeight={700} color={TEXT}>Per-Class Breakdown</Text>
                <Text fontSize="12px" color={MUTED}>— click any class to expand divisions &amp; field coverage</Text>
              </Flex>
              <Flex direction="column" gap={3}>
                {classes.map(cs => <ClassRow key={cs.classCode} cs={cs} onExpand={expandClass} />)}
              </Flex>
            </Box>

            {/* ── Recently Enriched ── */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" overflow="hidden" mb={4}>
              <Box px={5} py={3} bg="rgba(255,255,255,0.02)" borderBottom={`1px solid ${BORDER}`}>
                <Flex align="center" gap={2}>
                  <Clock size={14} color={ACCENT} />
                  <Text fontSize="13px" fontWeight={700} color={TEXT}>Recently Enriched</Text>
                  <Text fontSize="11px" color={MUTED}>(last 25 by update time)</Text>
                </Flex>
              </Box>
              {recent.length === 0 ? (
                <Box py={8} textAlign="center"><Text fontSize="13px" color={MUTED}>No enriched entities found</Text></Box>
              ) : (
                <Box overflowX="auto">
                  <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px' }}>
                    <thead>
                      <tr style={{ background: 'rgba(0,0,0,0.2)' }}>
                        {['Name', 'Slug', 'Era', 'Score', 'Updated'].map((h, i) => (
                          <th key={h} style={{ padding: '8px 14px', textAlign: i === 3 ? 'center' : i === 4 ? 'right' : 'left',
                            color: MUTED, fontWeight: 600, fontSize: '10px', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {recent.map((e, i) => (
                        <tr key={e.$id} style={{ background: i % 2 === 0 ? 'transparent' : 'rgba(255,255,255,0.015)', borderTop: '1px solid rgba(255,255,255,0.04)' }}>
                          <td style={{ padding: '7px 14px', color: TEXT, fontWeight: 500 }}>
                            <span style={{ cursor: 'pointer' }} onClick={() => navigate(`/entity/${e.slug}`)}>
                              {e.name}
                            </span>
                          </td>
                          <td style={{ padding: '7px 14px', color: MUTED, fontFamily: 'JetBrains Mono, monospace', fontSize: '10px' }}>{e.slug}</td>
                          <td style={{ padding: '7px 14px' }}><EraBadge era={e.era} /></td>
                          <td style={{ padding: '7px 14px', textAlign: 'center' }}><ScoreBadge score={e.importanceScore} /></td>
                          <td style={{ padding: '7px 14px', color: MUTED, textAlign: 'right', fontSize: '11px' }}>
                            {new Date(e.$updatedAt).toLocaleDateString()}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </Box>
              )}
            </Box>

            <Text fontSize="11px" color="#374151" textAlign="center">
              Data from Appwrite · per-class uses prefix queries · field breakdown samples ≤500 per class · auto-refreshes every 60s
            </Text>
          </>
        )}
      </Box>
    </Box>
  )
}
