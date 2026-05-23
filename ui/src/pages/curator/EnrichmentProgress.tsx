import React, { useEffect, useState, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, RefreshCw, Database, CheckCircle2, Clock,
  TrendingUp, AlertTriangle, Layers, Zap,
  ChevronDown, ChevronRight, Activity, Server, Cloud,
  FileText, MapPin, Network, Brain, Shield, Target,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { CLASSES, DIVISIONS } from '../../constants/callNumbers'

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Types                                                                       */
/* ─────────────────────────────────────────────────────────────────────────── */

interface ClassBucket {
  total: number; enriched: number; highQuality: number
  stubs: number; weak: number; lowEdges: number
  hasSummary: number; hasCauses: number; hasEffects: number
  hasEdges: number; hasPlaces: number; hasFrameworks: number; hasSignificance: number
}

interface AuditDoc {
  generatedAt: string; computeTimeMs: number; filesScanned: number
  total: number; enriched: number; highQuality: number
  stubs: number; weak: number; lowEdges: number
  fieldCoverage: {
    hasSummary: number; hasCauses: number; hasEffects: number
    hasEdges: number; hasPlaces: number; hasFrameworks: number; hasSignificance: number
  }
  byLabel: Record<string, ClassBucket>
  byClass: Record<string, ClassBucket>
  byDivision: Record<string, ClassBucket>
  significanceDist: Record<string, number>
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

const CLASS_COLORS: Record<string, string> = {
  '0': '#8B5CF6', '1': '#6366F1', '2': '#3B82F6', '3': '#06B6D4',
  '4': '#10B981', '5': '#F59E0B', '6': '#F97316', '7': '#EF4444',
  '8': '#EC4899', '9': '#A855F7',
}

const LABEL_COLORS: Record<string, string> = {
  Person: '#3B82F6', Place: '#10B981', Institution: '#F59E0B',
  Idea: '#8B5CF6', Text: '#06B6D4', EventWindow: '#F97316',
  Movement: '#EC4899', Evidence: '#A855F7', Timeframe: '#6B7280',
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

function parseJsonField<T>(raw: string | T | undefined): T {
  if (typeof raw === 'string') {
    try { return JSON.parse(raw) as T } catch { /* ignore */ }
  }
  return (raw ?? {}) as T
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
/*  ClassRow — uses pre-computed audit data; no live Appwrite queries          */
/* ─────────────────────────────────────────────────────────────────────────── */

function ClassRow({ classCode, bucket, divisionMap }: {
  classCode: string
  bucket: ClassBucket
  divisionMap: Record<string, ClassBucket>
}) {
  const [open, setOpen] = useState(false)
  const color = CLASS_COLORS[classCode] ?? ACCENT
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const cls = CLASSES.find((c: any) => c.code.toString() === classCode)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const heading = (cls as any)?.heading ?? `Class ${classCode}`

  const classDivisions = DIVISIONS
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    .filter((d: any) => d.parentClass?.toString() === classCode)
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    .map((d: any) => ({ code: d.code as string, heading: d.heading as string, bucket: divisionMap[d.code as string] }))
    .filter(d => d.bucket && d.bucket.total > 0)
    .sort((a, b) => (b.bucket?.total ?? 0) - (a.bucket?.total ?? 0))

  return (
    <Box border="1px solid" borderColor={open ? `${color}40` : BORDER}
      borderRadius="10px" overflow="hidden" bg={open ? `${color}06` : CARD_BG} transition="all 0.2s">
      <Flex as="button" w="100%" align="center" gap={3} p={4} cursor="pointer"
        onClick={() => setOpen(o => !o)}
        _hover={{ bg: `${color}0A` }} bg="transparent" border="none" textAlign="left">
        <Box w="4px" h="32px" borderRadius="full" bg={color} flexShrink={0} />
        <Box flex={1} minW={0}>
          <Flex align="center" gap={2} mb={1}>
            <Text fontSize="11px" fontFamily='"JetBrains Mono", monospace'
              color={color} fontWeight={700} letterSpacing="0.1em">Class {classCode}</Text>
            <Text fontSize="12px" fontWeight={600} color={TEXT} noOfLines={1}>{heading}</Text>
          </Flex>
          <Flex align="center" gap={3}>
            <Box flex={1}><ProgressBar value={bucket.enriched} max={bucket.total} color={color} height={5} /></Box>
            <Text fontSize="11px" color={color} fontWeight={700} minW="40px" textAlign="right">
              {pct(bucket.enriched, bucket.total)}%
            </Text>
          </Flex>
        </Box>
        <SimpleGrid columns={4} gap={3} minW="260px">
          {[
            { val: bucket.total,    label: 'total',   col: TEXT },
            { val: bucket.enriched, label: 'enriched',col: GREEN },
            { val: bucket.weak,     label: 'weak',    col: ORANGE },
            { val: bucket.stubs,    label: 'stubs',   col: RED },
          ].map(({ val, label, col }) => (
            <Box key={label} textAlign="center">
              <Text fontSize="14px" fontWeight={800} color={col}>{val.toLocaleString()}</Text>
              <Text fontSize="9px" color={MUTED} textTransform="uppercase" letterSpacing="0.05em">{label}</Text>
            </Box>
          ))}
        </SimpleGrid>
        {open ? <ChevronDown size={16} color={MUTED} /> : <ChevronRight size={16} color={MUTED} />}
      </Flex>

      {open && (
        <Box px={4} pb={4} borderTop={`1px solid ${color}20`}>
          <Box mb={4} pt={3}>
            <Text fontSize="10px" color={MUTED} letterSpacing="0.1em"
              textTransform="uppercase" fontFamily='"Cinzel", serif' mb={2}>
              Field Coverage — {bucket.total.toLocaleString()} entities (pre-computed)
            </Text>
            <SimpleGrid columns={{ base: 2, md: 4, lg: 7 }} gap={2}>
              {[
                { label: 'Summary≥600', val: bucket.hasSummary,      icon: FileText,   c: '#6366F1' },
                { label: 'Causes',      val: bucket.hasCauses,       icon: TrendingUp, c: '#8B5CF6' },
                { label: 'Effects',     val: bucket.hasEffects,      icon: Activity,   c: '#06B6D4' },
                { label: 'Edges',       val: bucket.hasEdges,        icon: Network,    c: '#3B82F6' },
                { label: 'Places',      val: bucket.hasPlaces,       icon: MapPin,     c: '#10B981' },
                { label: 'Frameworks',  val: bucket.hasFrameworks,   icon: Brain,      c: '#F97316' },
                { label: 'Significance',val: bucket.hasSignificance, icon: Shield,     c: '#EF4444' },
              ].map(({ label, val, icon: Icon, c }) => (
                <Box key={label} p={2} bg={`${c}0A`} borderRadius="8px" border={`1px solid ${c}20`}>
                  <Flex align="center" gap={1} mb={1}>
                    <Icon size={10} color={c} />
                    <Text fontSize="9px" color={c} fontWeight={600}>{label}</Text>
                  </Flex>
                  <Text fontSize="14px" fontWeight={800} color={TEXT}>{val.toLocaleString()}</Text>
                  <ProgressBar value={val} max={bucket.total} color={c} height={3} />
                  <Text fontSize="9px" color={MUTED} mt="2px">{pct(val, bucket.total)}%</Text>
                </Box>
              ))}
            </SimpleGrid>
          </Box>
          {classDivisions.length > 0 && (
            <Box>
              <Text fontSize="10px" color={MUTED} letterSpacing="0.1em"
                textTransform="uppercase" fontFamily='"Cinzel", serif' mb={2}>
                Divisions ({classDivisions.length})
              </Text>
              <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={2}>
                {classDivisions.map(div => (
                  <Flex key={div.code} align="center" gap={2} p={2}
                    bg="rgba(255,255,255,0.02)" borderRadius="6px" border={`1px solid ${color}15`}>
                    <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                      color={color} fontWeight={700} minW="32px">{div.code}</Text>
                    <Box flex={1} minW={0}>
                      <Text fontSize="10px" color={TEXT_DIM} noOfLines={1}>{div.heading}</Text>
                      <Flex align="center" gap={1} mt="2px">
                        <Box flex={1}>
                          <ProgressBar value={div.bucket?.enriched ?? 0} max={div.bucket?.total ?? 1} color={color} height={3} />
                        </Box>
                        <Text fontSize="9px" color={MUTED} minW="28px">{pct(div.bucket?.enriched ?? 0, div.bucket?.total ?? 1)}%</Text>
                      </Flex>
                    </Box>
                    <Box textAlign="right">
                      <Text fontSize="11px" fontWeight={700} color={GREEN}>{(div.bucket?.enriched ?? 0).toLocaleString()}</Text>
                      <Text fontSize="9px" color={MUTED}>/{(div.bucket?.total ?? 0).toLocaleString()}</Text>
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
  const [audit, setAudit] = useState<AuditDoc | null>(null)
  const [auditMissing, setAuditMissing] = useState(false)
  const [recent, setRecent] = useState<RecentEntity[]>([])
  const [bots, setBots] = useState<BotStatus>({
    serverOnline: false, ollamaRunning: false, activeJobs: [], ghRuns: [],
  })
  const [loading, setLoading] = useState(true)
  const [lastRefresh, setLastRefresh] = useState<Date | null>(null)
  const [error, setError] = useState<string | null>(null)

  const load = useCallback(async () => {
    setLoading(true); setError(null)
    try {
      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENRICHMENT_AUDIT, [
        Query.limit(1),
      ])
      if (res.documents.length > 0) {
        const raw = res.documents[0] as Record<string, unknown>
        setAudit({
          generatedAt:      raw.generatedAt as string,
          computeTimeMs:    raw.computeTimeMs as number,
          filesScanned:     raw.filesScanned as number,
          total:            raw.total as number,
          enriched:         raw.enriched as number,
          highQuality:      raw.highQuality as number,
          stubs:            raw.stubs as number,
          weak:             raw.weak as number,
          lowEdges:         raw.lowEdges as number,
          fieldCoverage:    parseJsonField(raw.fieldCoverage as string),
          byLabel:          parseJsonField(raw.byLabel as string),
          byClass:          parseJsonField(raw.byClass as string),
          byDivision:       parseJsonField(raw.byDivision as string),
          significanceDist: parseJsonField(raw.significanceDist as string),
        })
        setAuditMissing(false)
      } else {
        setAuditMissing(true)
      }
      const recentRes = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.greaterThanEqual('importanceScore', 4),
        Query.orderDesc('$updatedAt'),
        Query.limit(25),
        Query.select(['$id', 'name', 'slug', 'era', 'importanceScore', '$updatedAt']),
      ])
      setRecent(recentRes.documents.map(d => ({
        $id: d.$id as string, name: (d.name as string) ?? '\u2014',
        slug: (d.slug as string) ?? '', era: (d.era as string) ?? '',
        importanceScore: (d.importanceScore as number) ?? 0,
        $updatedAt: (d.$updatedAt as string) ?? '',
      })))
      setLastRefresh(new Date())
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load stats')
    }
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

  useEffect(() => { load(); loadBots() }, [load, loadBots])
  useEffect(() => { const id = setInterval(load, 120_000); return () => clearInterval(id) }, [load])
  useEffect(() => { const id = setInterval(loadBots, 5_000); return () => clearInterval(id) }, [loadBots])

  const enrichPct = audit ? parseFloat(pct(audit.enriched, audit.total)) : 0
  const totalLeft  = audit ? audit.stubs + audit.weak : 0

  const classEntries = audit
    ? Object.entries(audit.byClass).sort((a, b) => Number(a[0]) - Number(b[0]))
    : []
  const labelEntries = audit
    ? Object.entries(audit.byLabel).sort((a, b) => b[1].total - a[1].total)
    : []
  const sigEntries = audit
    ? Object.entries(audit.significanceDist)
        .map(([k, v]) => [Number(k), v] as [number, number])
        .sort((a, b) => b[0] - a[0])
    : []
  const sigMax = sigEntries.length > 0 ? Math.max(...sigEntries.map(([, v]) => v)) : 1

  return (
    <Box minH="100vh" bg={BG} color={TEXT} fontFamily="Inter, sans-serif">
      {/* Header */}
      <Box bg="rgba(17,24,39,0.95)" borderBottom={`1px solid ${BORDER}`}
        backdropFilter="blur(8px)" px={8} py={5} position="sticky" top={0} zIndex={10}>
        <Flex align="center" justify="space-between" maxW="1400px" mx="auto">
          <Flex align="center" gap={4}>
            <Box as="button" onClick={() => navigate('/curator')} display="flex"
              alignItems="center" gap={2} color={MUTED} fontSize="13px"
              cursor="pointer" _hover={{ color: TEXT }} bg="transparent" border="none" p={0}>
              <ChevronLeft size={16} /> Curator
            </Box>
            <Text color="rgba(99,102,241,0.4)" fontSize="12px">&rsaquo;</Text>
            <Flex align="center" gap={2}>
              <TrendingUp size={18} color={ACCENT} />
              <Text fontSize="18px" fontWeight={700} color={TEXT}
                fontFamily="'Cinzel', serif" letterSpacing="0.04em">Enrichment Progress</Text>
            </Flex>
          </Flex>
          <Flex align="center" gap={3}>
            {lastRefresh && <Text fontSize="11px" color={MUTED}>Updated {lastRefresh.toLocaleTimeString()}</Text>}
            {audit && <Text fontSize="11px" color={MUTED}>Audit: {relTime(audit.generatedAt)}</Text>}
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

        {auditMissing && !loading && (
          <Box p={6} mb={6} bg={CARD_BG} border={`1px solid ${ORANGE}40`} borderRadius="10px">
            <Flex align="center" gap={2} mb={2}>
              <AlertTriangle size={16} color={ORANGE} />
              <Text fontSize="14px" fontWeight={700} color={ORANGE}>No audit data yet</Text>
            </Flex>
            <Text fontSize="13px" color={TEXT_DIM} mb={3}>
              The <code>enrichment_audit</code> collection is empty.
              Run the audit script to populate it:
            </Text>
            <Box p={3} bg="rgba(0,0,0,0.3)" borderRadius="6px"
              fontFamily='"JetBrains Mono", monospace' fontSize="12px" color={GREEN}>
              <div>python3 scripts/audit_enrichment.py</div>
              <div>env $(cat .env | grep -v &apos;^#&apos; | xargs) npx tsx scripts/push_enrichment_audit.ts</div>
            </Box>
            <Text fontSize="11px" color={MUTED} mt={2}>
              GitHub Action <code>.github/workflows/enrichment-audit.yml</code> runs daily at 06:00 UTC.
            </Text>
          </Box>
        )}

        {loading && !audit ? (
          <Flex justify="center" py={16}><Spinner color={ACCENT} size="lg" /></Flex>
        ) : audit ? (
          <>
            {/* Hero Stats */}
            <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={4} mb={6}>
              {[
                { label: 'Total Entities',  value: audit.total,       icon: Database,      color: '#6366F1' },
                { label: 'Enriched >=600c', value: audit.enriched,    icon: CheckCircle2,  color: GREEN },
                { label: 'High Quality',    value: audit.highQuality, icon: Zap,           color: '#F59E0B' },
                { label: 'Weak (100-599c)', value: audit.weak,        icon: AlertTriangle, color: ORANGE },
                { label: 'Stubs (<100c)',   value: audit.stubs,       icon: Target,        color: RED },
                { label: 'Low Edges',       value: audit.lowEdges,    icon: Network,       color: '#8B5CF6' },
              ].map(({ label, value, icon: Icon, color }) => (
                <Box key={label} p={4} bg={CARD_BG} border="1px solid" borderColor={`${color}25`}
                  borderRadius="10px" position="relative" overflow="hidden">
                  <Box position="absolute" top={0} left={0} right={0} h="2px"
                    bg={`linear-gradient(90deg, ${color} 0%, transparent 100%)`} />
                  <Flex align="center" justify="space-between" mb={2}>
                    <Text fontSize="10px" color={MUTED} textTransform="uppercase" letterSpacing="0.08em">{label}</Text>
                    <Icon size={13} color={color} />
                  </Flex>
                  <Text fontSize="24px" fontWeight={800} color={TEXT}>{value.toLocaleString()}</Text>
                  <Text fontSize="10px" color={MUTED}>{pct(value, audit.total)}% of total</Text>
                </Box>
              ))}
            </SimpleGrid>

            {/* Countdown Progress */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
              <Flex align="center" justify="space-between" mb={1}>
                <Flex align="center" gap={2}>
                  <TrendingUp size={16} color={ACCENT} />
                  <Text fontSize="14px" fontWeight={700} color={TEXT}>Enrichment Countdown</Text>
                </Flex>
                <Flex align="center" gap={4}>
                  <Text fontSize="28px" fontWeight={800} color={ACCENT}>{enrichPct}%</Text>
                  <Box textAlign="right">
                    <Text fontSize="20px" fontWeight={800} color={RED}>{totalLeft.toLocaleString()}</Text>
                    <Text fontSize="10px" color={MUTED}>remaining</Text>
                  </Box>
                </Flex>
              </Flex>
              <Text fontSize="11px" color={MUTED} mb={3}>
                {audit.enriched.toLocaleString()} enriched &middot; {audit.weak.toLocaleString()} weak &middot; {audit.stubs.toLocaleString()} stubs &middot; of {audit.total.toLocaleString()} total
              </Text>
              <Flex gap={0} borderRadius="6px" overflow="hidden" h="16px">
                <Box h="100%" bg={GREEN}
                  style={{ width: `${pct(audit.highQuality, audit.total)}%`, minWidth: audit.highQuality > 0 ? '2px' : '0' }} />
                <Box h="100%" bg={ORANGE}
                  style={{ width: `${pct(audit.enriched - audit.highQuality, audit.total)}%`, minWidth: (audit.enriched - audit.highQuality) > 0 ? '2px' : '0' }} />
                <Box h="100%" bg="#374151"
                  style={{ width: `${pct(audit.weak, audit.total)}%`, minWidth: audit.weak > 0 ? '2px' : '0' }} />
                <Box h="100%" flex={1} bg="rgba(239,68,68,0.15)" />
              </Flex>
              <Flex gap={5} mt={2} flexWrap="wrap">
                {[
                  { c: GREEN,   label: `High Quality: ${audit.highQuality.toLocaleString()} (${pct(audit.highQuality, audit.total)}%)` },
                  { c: ORANGE,  label: `Enriched-only: ${(audit.enriched - audit.highQuality).toLocaleString()} (${pct(audit.enriched - audit.highQuality, audit.total)}%)` },
                  { c: '#374151', label: `Weak: ${audit.weak.toLocaleString()} (${pct(audit.weak, audit.total)}%)` },
                  { c: 'rgba(239,68,68,0.4)', label: `Stubs: ${audit.stubs.toLocaleString()} (${pct(audit.stubs, audit.total)}%)` },
                ].map(({ c, label }) => (
                  <Flex key={label} align="center" gap="6px">
                    <Box w="10px" h="10px" borderRadius="2px" bg={c} flexShrink={0} />
                    <Text fontSize="10px" color={MUTED}>{label}</Text>
                  </Flex>
                ))}
              </Flex>
            </Box>

            {/* Global Field Coverage */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
              <Flex align="center" gap={2} mb={4}>
                <Shield size={16} color={ACCENT} />
                <Text fontSize="14px" fontWeight={700} color={TEXT}>Field Coverage - Global</Text>
                <Text fontSize="11px" color={MUTED}>(all {audit.total.toLocaleString()} entities)</Text>
              </Flex>
              <SimpleGrid columns={{ base: 2, md: 4, lg: 7 }} gap={3}>
                {[
                  { label: 'Summary>=600', val: audit.fieldCoverage.hasSummary,      icon: FileText,   c: '#6366F1' },
                  { label: 'Causes',       val: audit.fieldCoverage.hasCauses,       icon: TrendingUp, c: '#8B5CF6' },
                  { label: 'Effects',      val: audit.fieldCoverage.hasEffects,      icon: Activity,   c: '#06B6D4' },
                  { label: 'Edges',        val: audit.fieldCoverage.hasEdges,        icon: Network,    c: '#3B82F6' },
                  { label: 'Places',       val: audit.fieldCoverage.hasPlaces,       icon: MapPin,     c: '#10B981' },
                  { label: 'Frameworks',   val: audit.fieldCoverage.hasFrameworks,   icon: Brain,      c: '#F97316' },
                  { label: 'Significance', val: audit.fieldCoverage.hasSignificance, icon: Shield,     c: '#EF4444' },
                ].map(({ label, val, icon: Icon, c }) => (
                  <Box key={label} p={3} bg={`${c}0A`} borderRadius="8px" border={`1px solid ${c}20`}>
                    <Flex align="center" gap={2} mb={2}>
                      <Icon size={12} color={c} />
                      <Text fontSize="10px" color={c} fontWeight={600}>{label}</Text>
                    </Flex>
                    <Text fontSize="18px" fontWeight={800} color={TEXT}>{val.toLocaleString()}</Text>
                    <ProgressBar value={val} max={audit.total} color={c} height={4} />
                    <Text fontSize="10px" color={MUTED} mt="3px">{pct(val, audit.total)}%</Text>
                  </Box>
                ))}
              </SimpleGrid>
            </Box>

            {/* By Entity Type */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
              <Flex align="center" gap={2} mb={4}>
                <Database size={16} color={ACCENT} />
                <Text fontSize="14px" fontWeight={700} color={TEXT}>By Entity Type</Text>
              </Flex>
              <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3}>
                {labelEntries.map(([label, b]) => {
                  const color = LABEL_COLORS[label] ?? MUTED
                  return (
                    <Box key={label} p={3} bg={`${color}08`} borderRadius="8px" border={`1px solid ${color}25`}>
                      <Flex align="center" justify="space-between" mb={2}>
                        <Flex align="center" gap={2}>
                          <Box w="8px" h="8px" borderRadius="full" bg={color} />
                          <Text fontSize="12px" fontWeight={700} color={TEXT}>{label}</Text>
                        </Flex>
                        <Text fontSize="11px" color={MUTED}>{b.total.toLocaleString()} total</Text>
                      </Flex>
                      <ProgressBar value={b.enriched} max={b.total} color={color} height={6} />
                      <Flex justify="space-between" mt={1}>
                        <Text fontSize="10px" color={GREEN}>{b.enriched.toLocaleString()} enriched ({pct(b.enriched, b.total)}%)</Text>
                        <Text fontSize="10px" color={RED}>{b.stubs.toLocaleString()} stubs</Text>
                      </Flex>
                      <Flex gap={2} mt={1} flexWrap="wrap">
                        <Text fontSize="9px" color={ORANGE}>{b.weak.toLocaleString()} weak</Text>
                        <Text fontSize="9px" color={MUTED}>&middot;</Text>
                        <Text fontSize="9px" color={TEXT_DIM}>{b.highQuality.toLocaleString()} HQ</Text>
                        {b.lowEdges > 0 && (
                          <>
                            <Text fontSize="9px" color={MUTED}>&middot;</Text>
                            <Text fontSize="9px" color="#8B5CF6">{b.lowEdges.toLocaleString()} low-edge</Text>
                          </>
                        )}
                      </Flex>
                    </Box>
                  )
                })}
              </SimpleGrid>
            </Box>

            {/* Significance Distribution */}
            {sigEntries.length > 0 && (
              <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" p={5} mb={6}>
                <Flex align="center" gap={2} mb={4}>
                  <Zap size={16} color={ACCENT} />
                  <Text fontSize="14px" fontWeight={700} color={TEXT}>Significance Score Distribution</Text>
                  <Text fontSize="11px" color={MUTED}>(enriched entities with historicalSignificance)</Text>
                </Flex>
                <Flex align="end" gap={2} h="80px" mb={2}>
                  {Array.from({ length: 10 }, (_, i) => {
                    const score = 10 - i
                    const count = audit.significanceDist[score.toString()] ?? 0
                    const barH = sigMax > 0 ? Math.max(4, (count / sigMax) * 72) : 4
                    const col = score >= 9 ? GREEN : score >= 7 ? ACCENT : score >= 5 ? ORANGE : score >= 3 ? RED : MUTED
                    return (
                      <Box key={score} flex={1} display="flex" flexDir="column" align="center" gap={1}>
                        <Text fontSize="8px" color={MUTED}>{count > 0 ? count.toLocaleString() : ''}</Text>
                        <Box w="100%" bg={col} borderRadius="3px 3px 0 0" opacity={0.85}
                          style={{ height: `${barH}px` }} title={`Score ${score}: ${count.toLocaleString()}`} />
                        <Text fontSize="9px" color={col} fontWeight={700}>{score}</Text>
                      </Box>
                    )
                  })}
                </Flex>
                <Flex gap={4} flexWrap="wrap">
                  {[
                    { range: '9-10', label: 'World-changing', c: GREEN },
                    { range: '7-8',  label: 'Continental',    c: ACCENT },
                    { range: '5-6',  label: 'Regional',       c: ORANGE },
                    { range: '3-4',  label: 'Local',          c: RED },
                    { range: '1-2',  label: 'Minor',          c: MUTED },
                  ].map(({ range, label, c }) => (
                    <Flex key={range} align="center" gap="5px">
                      <Box w="8px" h="8px" borderRadius="2px" bg={c} />
                      <Text fontSize="9px" color={MUTED}>{range}: {label}</Text>
                    </Flex>
                  ))}
                </Flex>
              </Box>
            )}

            {/* Bot Status */}
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

            {/* Per-Class Breakdown */}
            <Box mb={6}>
              <Flex align="center" gap={2} mb={4}>
                <Layers size={16} color={ACCENT} />
                <Text fontSize="16px" fontWeight={700} color={TEXT}>Per-Class Breakdown</Text>
                <Text fontSize="12px" color={MUTED}> click to expand divisions &amp; field coverage</Text>
                <Text fontSize="11px" color={MUTED}>({audit.filesScanned.toLocaleString()} files pre-computed, no 5K limit)</Text>
              </Flex>
              <Flex direction="column" gap={3}>
                {classEntries.map(([code, bucket]) => (
                  <ClassRow key={code} classCode={code} bucket={bucket} divisionMap={audit.byDivision} />
                ))}
              </Flex>
            </Box>

            {/* Recently Enriched */}
            <Box bg={CARD_BG} border={`1px solid ${BORDER}`} borderRadius="10px" overflow="hidden" mb={4}>
              <Box px={5} py={3} bg="rgba(255,255,255,0.02)" borderBottom={`1px solid ${BORDER}`}>
                <Flex align="center" gap={2}>
                  <Clock size={14} color={ACCENT} />
                  <Text fontSize="13px" fontWeight={700} color={TEXT}>Recently Enriched</Text>
                  <Text fontSize="11px" color={MUTED}>(last 25, live from Appwrite)</Text>
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
                          <th key={h} style={{
                            padding: '8px 14px',
                            textAlign: i === 3 ? 'center' : i === 4 ? 'right' : 'left',
                            color: MUTED, fontWeight: 600, fontSize: '10px',
                            textTransform: 'uppercase', letterSpacing: '0.08em',
                          }}>{h}</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {recent.map((e, i) => (
                        <tr key={e.$id} style={{
                          background: i % 2 === 0 ? 'transparent' : 'rgba(255,255,255,0.015)',
                          borderTop: '1px solid rgba(255,255,255,0.04)',
                        }}>
                          <td style={{ padding: '7px 14px', color: TEXT, fontWeight: 500, cursor: 'pointer' }}
                            onClick={() => navigate(`/entity/${e.slug}`)}>
                            {e.name}
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

            {/* Footer */}
            <Flex align="center" justify="center" gap={3} mt={2} flexWrap="wrap">
              <Text fontSize="11px" color="#374151">
                Audit: {new Date(audit.generatedAt).toLocaleString()} in {audit.computeTimeMs.toLocaleString()}ms
              </Text>
              <Text fontSize="11px" color="#374151">&middot;</Text>
              <Text fontSize="11px" color="#374151">
                {audit.filesScanned.toLocaleString()} files scanned, no Appwrite 5K limit
              </Text>
              <Text fontSize="11px" color="#374151">&middot;</Text>
              <Text fontSize="11px" color="#374151">
                Runs daily: .github/workflows/enrichment-audit.yml
              </Text>
            </Flex>
          </>
        ) : null}
      </Box>
    </Box>
  )
}
