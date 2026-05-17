/**
 * GeminiBotMonitor — Real-time dashboard for Gemini (and all cloud) bots.
 *
 * Data sources (all proxied / symlinked via Vite dev server):
 *   /local-bots/github/status  → local_bot_server reads last_github_runs.json
 *   /governance/budget.json    → monthly write cap state
 *   /governance/last_sync.json → last sync gateway run
 *   /enrichment/last_run.json  → last AI enrichment run
 *   /enrichment/significance_run.json → last significance run
 *   Appwrite audit_log         → count cloud-tagged edits today / this week
 *
 * Shown on /curator/audit/log
 */
import React, { useEffect, useState, useCallback, useRef } from 'react'
import { Box, Flex, Text, Spinner, SimpleGrid } from '@chakra-ui/react'
import {
  Cloud, CloudOff, Zap, Activity, TrendingUp,
  Clock, CheckCircle2, AlertTriangle, XCircle,
  RefreshCw, ExternalLink, BarChart2, Cpu, GitBranch,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'

// ─── Types ────────────────────────────────────────────────────────────────────

interface GHRun {
  name: string
  status: string
  conclusion: string | null
  runId: number
  startedAt: string | null
  updatedAt: string | null
  htmlUrl: string
  triggeredBy: string
}

interface BudgetData {
  monthlyWriteCap: number
  perRunWriteCap: number
  hardStopPercent: number
  resetDay: number
  current: {
    cycleStart: string
    writesUsed: number
    lastUpdated: string
  }
  manualPause: boolean
}

interface LastSync {
  lastSyncedCommit?: string
  lastRunAt?: string
  lastRunStatus?: string
  lastRunStats?: {
    filesChanged?: number
    entitiesUpserted?: number
    auditRowsEmitted?: number
    writesPerformed?: number
  }
}

interface EnrichRun {
  timestamp?: string
  model?: string
  count_requested?: number
  enriched?: number
  failed?: number
  entities?: Array<{ slug: string; status: string; old_len: number; new_len: number }>
}

interface SigRun {
  generatedAt?: string
  summary?: { entities_scored?: number; failed?: number }
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function relTime(iso?: string | null): string {
  if (!iso) return 'never'
  const d = new Date(iso).getTime()
  if (isNaN(d)) return 'never'
  const s = Math.max(0, (Date.now() - d) / 1000)
  if (s < 60) return `${Math.floor(s)}s ago`
  if (s < 3600) return `${Math.floor(s / 60)}m ago`
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`
  return `${Math.floor(s / 86400)}d ago`
}

function ageSecs(iso?: string | null): number {
  if (!iso) return Infinity
  const d = new Date(iso).getTime()
  if (isNaN(d)) return Infinity
  return (Date.now() - d) / 1000
}

async function fetchJSON<T>(url: string): Promise<T | null> {
  try {
    const r = await fetch(url, { cache: 'no-store' })
    if (!r.ok) return null
    return (await r.json()) as T
  } catch { return null }
}

// ─── Workflow status config ────────────────────────────────────────────────────

const CLOUD_WORKFLOWS = [
  {
    key: 'ai-enrichment',
    name: 'AI Entity Enrichment (git-first)',
    label: 'Gemini Enrichment',
    color: '#4285F4',
    icon: Zap,
    cronDesc: 'every 2h',
    maxIdleHours: 3,   // ONLINE if ran within 3h (cron is 2h)
  },
  {
    key: 'sync-gateway',
    name: 'Sync Gateway — git → Appwrite',
    label: 'Sync Gateway',
    color: '#27AE60',
    icon: GitBranch,
    cronDesc: 'daily 07:00 UTC + auto after enrichment',
    maxIdleHours: 26,
  },
  {
    key: 'significance',
    name: 'Significance Backfill Bot',
    label: 'Significance Backfill',
    color: '#8E44AD',
    icon: TrendingUp,
    cronDesc: 'daily 06:00 UTC',
    maxIdleHours: 26,
  },
  {
    key: 'keepalive',
    name: 'Bot Keepalive & Retry',
    label: 'Keepalive',
    color: '#E67E22',
    icon: Activity,
    cronDesc: 'every 4h if idle > 20h',
    maxIdleHours: 25,
  },
]

// ─── WorkflowCard ─────────────────────────────────────────────────────────────

function WorkflowCard({ wf, run }: {
  wf: typeof CLOUD_WORKFLOWS[0]
  run: GHRun | undefined
}) {
  const Icon = wf.icon
  const age = ageSecs(run?.updatedAt)
  const maxIdle = wf.maxIdleHours * 3600

  let bStatus: 'online' | 'degraded' | 'offline' | 'unknown' = 'unknown'
  if (!run) {
    bStatus = 'unknown'
  } else if (run.conclusion === 'failure' || run.conclusion === 'cancelled') {
    bStatus = 'offline'
  } else if (run.status === 'in_progress' || run.status === 'queued') {
    bStatus = 'online'
  } else if (run.conclusion === 'success') {
    bStatus = age < maxIdle ? 'online' : age < maxIdle * 2 ? 'degraded' : 'offline'
  }

  const statusColor = {
    online: '#27AE60',
    degraded: '#E67E22',
    offline: '#C0392B',
    unknown: '#9E9A90',
  }[bStatus]

  const statusBg = {
    online: '#27AE6012',
    degraded: '#E67E2212',
    offline: '#C0392B12',
    unknown: '#F5F4F0',
  }[bStatus]

  const statusLabel = {
    online: '● ONLINE',
    degraded: '◐ DEGRADED',
    offline: '○ OFFLINE',
    unknown: '? UNKNOWN',
  }[bStatus]

  return (
    <Box p={3} borderRadius="md" bg="white"
      border={`1px solid ${wf.color}30`}
      borderLeft={`3px solid ${wf.color}`}
      transition="all 0.15s">
      {/* Header */}
      <Flex align="center" gap={2} mb={2}>
        <Box p={1} borderRadius="sm" bg={`${wf.color}18`}>
          <Icon size={12} color={wf.color} />
        </Box>
        <Text fontSize="10px" fontWeight={700} color="#787469"
          letterSpacing="0.06em" textTransform="uppercase" flex={1}
          lineClamp={1}>
          {wf.label}
        </Text>
        <Box px={2} py={0.5} borderRadius="full" fontSize="8px" fontWeight={700}
          bg={statusBg} color={statusColor}
          animation={bStatus === 'online' && run?.status !== 'in_progress'
            ? undefined : bStatus === 'online' ? 'pulse 1.6s infinite' : undefined}>
          {run?.status === 'in_progress' ? '⟳ RUNNING' : statusLabel}
        </Box>
      </Flex>

      {/* KPI values */}
      {run ? (
        <>
          <Flex align="baseline" gap={1} mb={1}>
            <Text fontSize="16px" fontWeight={700}
              fontFamily='"Cormorant Garamond", serif' color="#2D2A24">
              {run.conclusion === 'success' ? '✓' : run.conclusion === 'failure' ? '✗' : '…'}
            </Text>
            <Text fontSize="11px" color="#524E44" fontWeight={500}>
              {run.conclusion ?? run.status}
            </Text>
          </Flex>
          <Flex align="center" gap={1}>
            <Clock size={9} color="#9E9A90" />
            <Text fontSize="9px" color="#9E9A90">
              {relTime(run.updatedAt)} · {run.triggeredBy || 'schedule'}
            </Text>
          </Flex>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>
            {wf.cronDesc}
          </Text>
          {run.htmlUrl && (
            <Box as="a" href={run.htmlUrl} target="_blank" rel="noopener noreferrer"
              display="flex" alignItems="center" gap={1} mt={1}
              fontSize="8px" color={wf.color} _hover={{ textDecoration: 'underline' }}>
              <ExternalLink size={8} />
              Run #{run.runId}
            </Box>
          )}
        </>
      ) : (
        <Flex align="center" gap={1} mt={1}>
          <AlertTriangle size={10} color="#9E9A90" />
          <Text fontSize="10px" color="#9E9A90">no run recorded yet</Text>
        </Flex>
      )}
    </Box>
  )
}

// ─── Main Component ───────────────────────────────────────────────────────────

interface Props {
  /** optional Appwrite query results for today's cloud entries */
  cloudEditsToday?: number
}

const GeminiBotMonitor: React.FC<Props> = ({ cloudEditsToday = 0 }) => {
  const [runs, setRuns] = useState<GHRun[]>([])
  const [budget, setBudget] = useState<BudgetData | null>(null)
  const [lastSync, setLastSync] = useState<LastSync | null>(null)
  const [enrichRun, setEnrichRun] = useState<EnrichRun | null>(null)
  const [sigRun, setSigRun] = useState<SigRun | null>(null)
  const [cloudTotal, setCloudTotal] = useState(cloudEditsToday)
  const [cloudWeek, setCloudWeek] = useState(0)
  const [cloudMonth, setCloudMonth] = useState(0)
  const [loadingCloud, setLoadingCloud] = useState(true)
  const [lastRefresh, setLastRefresh] = useState(new Date())
  const [refreshing, setRefreshing] = useState(false)
  const mountedRef = useRef(true)

  // Identify "cloud bot" audit entries by editorId pattern
  const CLOUD_PATTERN = /gemini|gpt|openai|cloud|AI Entity/i

  async function queryCloudEdits(sinceISO: string): Promise<number> {
    try {
      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, [
        Query.greaterThan('timestamp', sinceISO),
        Query.limit(1),
      ])
      // We have total count — but filter by cloud editorId needs a different approach
      // Use the total as an upper bound; refined in batch counts below
      return res.total
    } catch { return 0 }
  }

  const loadAll = useCallback(async (quiet = false) => {
    if (!quiet) setRefreshing(true)

    const now = new Date()
    const todayISO = new Date(now.getFullYear(), now.getMonth(), now.getDate()).toISOString()
    const weekISO = new Date(now.getTime() - 7 * 86400_000).toISOString()
    const monthISO = new Date(now.getTime() - 30 * 86400_000).toISOString()

    const [ghStatus, bgt, sync, enrich, sig] = await Promise.all([
      fetchJSON<GHRun[]>('/local-bots/github/status').then(d => {
        // local_bot_server returns {runs:[...]} or [...] directly
        if (Array.isArray(d)) return d
        if (d && Array.isArray((d as Record<string, unknown>).runs)) {
          return (d as { runs: GHRun[] }).runs
        }
        return []
      }),
      fetchJSON<BudgetData>('/governance/budget.json'),
      fetchJSON<LastSync>('/governance/last_sync.json'),
      fetchJSON<EnrichRun>('/enrichment/last_run.json'),
      fetchJSON<SigRun>('/audit-reports/significance_run.json'),
    ])

    if (!mountedRef.current) return

    if (ghStatus) setRuns(ghStatus)
    if (bgt) setBudget(bgt)
    if (sync) setLastSync(sync)
    if (enrich) setEnrichRun(enrich)
    if (sig) setSigRun(sig)
    setLastRefresh(new Date())

    // Lightweight Appwrite counts — today / week / month (cloud-tagged edits)
    // We query by timestamp ranges; editorId filter would need a full-text index.
    // Instead we count all audit rows per window as proxy for activity.
    setLoadingCloud(true)
    const [today, week, month] = await Promise.all([
      queryCloudEdits(todayISO),
      queryCloudEdits(weekISO),
      queryCloudEdits(monthISO),
    ])
    if (!mountedRef.current) return
    setCloudTotal(today)
    setCloudWeek(week)
    setCloudMonth(month)
    setLoadingCloud(false)
    if (!quiet) setRefreshing(false)
  }, [])

  useEffect(() => {
    mountedRef.current = true
    loadAll()
    const id = setInterval(() => loadAll(true), 15_000)
    return () => {
      mountedRef.current = false
      clearInterval(id)
    }
  }, [loadAll])

  // ── Derive overall Gemini bot status ──────────────────────────────────────
  const enrichmentRun = runs.find(r => r.name.includes('Enrichment'))
  const enrichAge = ageSecs(enrichmentRun?.updatedAt)
  const geminiOnline = enrichmentRun?.status === 'in_progress'
    || (enrichmentRun?.conclusion === 'success' && enrichAge < 3 * 3600)
  const geminiDegraded = !geminiOnline
    && enrichmentRun?.conclusion === 'success'
    && enrichAge < 12 * 3600

  let overallStatus: 'ONLINE' | 'DEGRADED' | 'OFFLINE' | 'UNKNOWN' = 'UNKNOWN'
  let statusColor = '#9E9A90'
  let statusBg = '#F5F4F0'
  let StatusIcon = CloudOff

  if (runs.length === 0) {
    overallStatus = 'UNKNOWN'
    statusColor = '#9E9A90'; statusBg = '#F5F4F0'; StatusIcon = CloudOff
  } else if (geminiOnline) {
    overallStatus = 'ONLINE'
    statusColor = '#27AE60'; statusBg = '#27AE6012'; StatusIcon = Cloud
  } else if (geminiDegraded) {
    overallStatus = 'DEGRADED'
    statusColor = '#E67E22'; statusBg = '#E67E2212'; StatusIcon = AlertTriangle
  } else {
    overallStatus = 'OFFLINE'
    statusColor = '#C0392B'; statusBg = '#C0392B12'; StatusIcon = CloudOff
  }

  // ── Budget maths ──────────────────────────────────────────────────────────
  const writesUsed = budget?.current.writesUsed ?? 0
  const writeCap = budget?.monthlyWriteCap ?? 300_000
  const budgetPct = Math.min(100, Math.round((writesUsed / Math.max(1, writeCap)) * 100))
  const hardStop = budget?.hardStopPercent ?? 95

  // ── Last enrichment entity list (most recent 6) ───────────────────────────
  const recentEntities = (enrichRun?.entities ?? []).slice(0, 6)

  // ── Next scheduled estimate ───────────────────────────────────────────────
  function nextScheduled(): string {
    if (!enrichmentRun?.updatedAt) return 'unknown'
    const nextMs = new Date(enrichmentRun.updatedAt).getTime() + 2 * 3600 * 1000
    const diffMin = Math.max(0, (nextMs - Date.now()) / 60_000)
    if (diffMin < 1) return 'imminent'
    if (diffMin < 60) return `~${Math.round(diffMin)}m`
    return `~${Math.round(diffMin / 60)}h`
  }

  return (
    <Box p={4} bg="#F8FBFF" border="1px solid #4285F430"
      borderRadius="lg" position="relative">
      {/* ── Header ─────────────────────────────────────────────────────── */}
      <Flex align="center" gap={3} mb={4} flexWrap="wrap">
        <Box p={2} borderRadius="md" bg={statusBg} border={`1px solid ${statusColor}30`}>
          <StatusIcon size={20} color={statusColor} />
        </Box>
        <Box flex={1}>
          <Flex align="center" gap={2}>
            <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
              color="#2D2A24" letterSpacing="0.1em" textTransform="uppercase">
              Gemini Cloud Bot Monitor
            </Text>
            {/* Pulsing status badge */}
            <Box px={3} py={1} borderRadius="full" fontSize="10px" fontWeight={700}
              bg={statusBg} color={statusColor}
              border={`1px solid ${statusColor}40`}
              animation={overallStatus === 'ONLINE' ? 'pulse 2s ease-in-out infinite' : undefined}>
              {overallStatus === 'ONLINE' && <span>● </span>}
              {overallStatus === 'DEGRADED' && <span>◐ </span>}
              {overallStatus === 'OFFLINE' && <span>○ </span>}
              {overallStatus}
            </Box>
          </Flex>
          <Text fontSize="11px" color="#787469">
            GitHub Actions · ai-enrichment.yml cron every 2h ·{' '}
            refreshed {relTime(lastRefresh.toISOString())}
          </Text>
        </Box>
        {/* Refresh button */}
        <Box as="button" onClick={() => loadAll()}
          px={3} py={1.5} borderRadius="md" fontSize="10px" fontWeight={700}
          bg="#F5F4F0" border="1px solid #E4E2DC" color="#787469" cursor="pointer"
          display="flex" alignItems="center" gap={1.5}
          _hover={{ bg: '#E4E2DC' }}>
          {refreshing ? <Spinner size="xs" /> : <RefreshCw size={11} />}
          REFRESH
        </Box>
      </Flex>

      {/* ── KPI Row ────────────────────────────────────────────────────── */}
      <SimpleGrid columns={{ base: 2, sm: 3, md: 6 }} gap={3} mb={4}>
        {/* Entities enriched — last run */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop="2px solid #4285F4">
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Last Run
          </Text>
          <Text fontSize="20px" fontWeight={700} color="#4285F4"
            fontFamily='"Cormorant Garamond", serif'>
            {enrichRun?.enriched ?? '—'}
          </Text>
          <Text fontSize="9px" color="#9E9A90">entities enriched</Text>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>
            {relTime(enrichRun?.timestamp)}
          </Text>
        </Box>

        {/* Success rate */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop="2px solid #27AE60">
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Success Rate
          </Text>
          <Text fontSize="20px" fontWeight={700} color="#27AE60"
            fontFamily='"Cormorant Garamond", serif'>
            {enrichRun?.count_requested
              ? `${Math.round(((enrichRun.enriched ?? 0) / enrichRun.count_requested) * 100)}%`
              : '—'}
          </Text>
          <Text fontSize="9px" color="#9E9A90">
            {enrichRun?.enriched ?? 0}/{enrichRun?.count_requested ?? 0} req
          </Text>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>
            {enrichRun?.failed ?? 0} failed
          </Text>
        </Box>

        {/* Significance scored */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop="2px solid #8E44AD">
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Significance
          </Text>
          <Text fontSize="20px" fontWeight={700} color="#8E44AD"
            fontFamily='"Cormorant Garamond", serif'>
            {sigRun?.summary?.entities_scored ?? '—'}
          </Text>
          <Text fontSize="9px" color="#9E9A90">entities scored</Text>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>
            {relTime(sigRun?.generatedAt)}
          </Text>
        </Box>

        {/* Audit rows today */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop="2px solid #D4AF37">
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Edits Today
          </Text>
          <Text fontSize="20px" fontWeight={700} color="#D4AF37"
            fontFamily='"Cormorant Garamond", serif'>
            {loadingCloud ? '…' : cloudTotal.toLocaleString()}
          </Text>
          <Text fontSize="9px" color="#9E9A90">audit rows (all bots)</Text>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>
            7d: {loadingCloud ? '…' : cloudWeek.toLocaleString()}
          </Text>
        </Box>

        {/* Budget used */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop={`2px solid ${budgetPct >= hardStop ? '#C0392B' : '#4A90D9'}`}>
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Budget
          </Text>
          <Text fontSize="20px" fontWeight={700}
            color={budgetPct >= hardStop ? '#C0392B' : '#4A90D9'}
            fontFamily='"Cormorant Garamond", serif'>
            {budgetPct}%
          </Text>
          <Box h="4px" bg="#F5F4F0" borderRadius="full" overflow="hidden" mb={0.5}>
            <Box h="100%" borderRadius="full" transition="width 0.4s"
              bg={budgetPct >= hardStop ? '#C0392B' : '#4A90D9'}
              w={`${budgetPct}%`} />
          </Box>
          <Text fontSize="8px" color="#9E9A90">
            {writesUsed.toLocaleString()}/{writeCap.toLocaleString()} writes
          </Text>
        </Box>

        {/* Next scheduled run */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #E4E2DC"
          borderTop="2px solid #E67E22">
          <Text fontSize="9px" fontWeight={700} color="#787469" mb={1}
            textTransform="uppercase" letterSpacing="0.07em">
            Next Run
          </Text>
          <Text fontSize="20px" fontWeight={700} color="#E67E22"
            fontFamily='"Cormorant Garamond", serif'>
            {nextScheduled()}
          </Text>
          <Text fontSize="9px" color="#9E9A90">estimated</Text>
          <Text fontSize="8px" color="#B8C9D9" mt={0.5}>cron every 2h</Text>
        </Box>
      </SimpleGrid>

      {/* ── Workflow status grid ────────────────────────────────────────── */}
      <Box mb={4}>
        <Flex align="center" gap={2} mb={2}>
          <BarChart2 size={13} color="#787469" />
          <Text fontSize="10px" fontWeight={700} color="#787469"
            textTransform="uppercase" letterSpacing="0.07em">
            GitHub Actions Workflows
          </Text>
        </Flex>
        <SimpleGrid columns={{ base: 2, md: 4 }} gap={3}>
          {CLOUD_WORKFLOWS.map(wf => {
            const run = runs.find(r => r.name === wf.name)
            return <WorkflowCard key={wf.key} wf={wf} run={run} />
          })}
        </SimpleGrid>
        {runs.length === 0 && (
          <Box mt={3} p={3} bg="#FEF9E7" border="1px solid #F1C40F30" borderRadius="md">
            <Flex align="center" gap={2}>
              <AlertTriangle size={13} color="#E67E22" />
              <Text fontSize="11px" color="#2D2A24">
                No cloud run data yet — workflows write to{' '}
                <Text as="span" fontFamily='"JetBrains Mono", monospace' fontSize="10px"
                  color="#C5963A">
                  data/governance/last_github_runs.json
                </Text>{' '}
                on each successful run. Check back after the next cron cycle (every 2h).
              </Text>
            </Flex>
          </Box>
        )}
      </Box>

      {/* ── Last sync gateway KPIs ──────────────────────────────────────── */}
      <Flex gap={3} mb={4} flexWrap="wrap">
        <Box p={3} bg="white" borderRadius="md" border="1px solid #27AE6020"
          flex={1} minW="200px">
          <Flex align="center" gap={1.5} mb={2}>
            <GitBranch size={12} color="#27AE60" />
            <Text fontSize="10px" fontWeight={700} color="#787469"
              textTransform="uppercase" letterSpacing="0.06em">
              Last Sync Gateway
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="8px" fontWeight={700}
              borderRadius="sm"
              bg={lastSync?.lastRunStatus === 'ok' ? '#27AE6015' : '#C0392B15'}
              color={lastSync?.lastRunStatus === 'ok' ? '#27AE60' : '#C0392B'}>
              {(lastSync?.lastRunStatus ?? 'idle').toUpperCase()}
            </Box>
          </Flex>
          <SimpleGrid columns={3} gap={2}>
            {[
              { label: 'Files', val: lastSync?.lastRunStats?.filesChanged ?? 0 },
              { label: 'Upserted', val: lastSync?.lastRunStats?.entitiesUpserted ?? 0 },
              { label: 'Writes', val: lastSync?.lastRunStats?.writesPerformed ?? 0 },
            ].map(kv => (
              <Box key={kv.label} textAlign="center">
                <Text fontSize="14px" fontWeight={700} color="#2D2A24"
                  fontFamily='"Cormorant Garamond", serif'>
                  {kv.val.toLocaleString()}
                </Text>
                <Text fontSize="8px" color="#9E9A90">{kv.label}</Text>
              </Box>
            ))}
          </SimpleGrid>
          <Flex align="center" gap={1} mt={2}>
            <Clock size={9} color="#9E9A90" />
            <Text fontSize="9px" color="#9E9A90">
              {relTime(lastSync?.lastRunAt)} ·{' '}
              commit {lastSync?.lastSyncedCommit?.slice(0, 8) ?? '—'}
            </Text>
          </Flex>
        </Box>

        {/* Monthly totals audit */}
        <Box p={3} bg="white" borderRadius="md" border="1px solid #D4AF3720"
          flex={1} minW="200px">
          <Flex align="center" gap={1.5} mb={2}>
            <Activity size={12} color="#D4AF37" />
            <Text fontSize="10px" fontWeight={700} color="#787469"
              textTransform="uppercase" letterSpacing="0.06em">
              Audit Activity
            </Text>
          </Flex>
          {loadingCloud ? (
            <Flex justify="center" py={4}><Spinner size="sm" color="#D4AF37" /></Flex>
          ) : (
            <SimpleGrid columns={3} gap={2}>
              {[
                { label: 'Today', val: cloudTotal },
                { label: 'This Week', val: cloudWeek },
                { label: '30 Days', val: cloudMonth },
              ].map(kv => (
                <Box key={kv.label} textAlign="center">
                  <Text fontSize="14px" fontWeight={700} color="#2D2A24"
                    fontFamily='"Cormorant Garamond", serif'>
                    {kv.val.toLocaleString()}
                  </Text>
                  <Text fontSize="8px" color="#9E9A90">{kv.label}</Text>
                </Box>
              ))}
            </SimpleGrid>
          )}
          <Text fontSize="8px" color="#B8C9D9" mt={2}>
            All bots (cloud + local) · via Appwrite audit_log
          </Text>
        </Box>
      </Flex>

      {/* ── Recent enriched entities (last run) ────────────────────────── */}
      {recentEntities.length > 0 && (
        <Box>
          <Flex align="center" gap={2} mb={2}>
            <Cpu size={13} color="#4285F4" />
            <Text fontSize="10px" fontWeight={700} color="#787469"
              textTransform="uppercase" letterSpacing="0.07em">
              Recent Enrichments — Last Run
              <Text as="span" fontSize="9px" color="#9E9A90" ml={2} fontWeight={400}
                textTransform="none" letterSpacing="normal">
                ({enrichRun?.model?.toUpperCase() ?? 'unknown model'})
              </Text>
            </Text>
          </Flex>
          <Flex gap={2} flexWrap="wrap">
            {recentEntities.map((e, i) => (
              <Box key={i} px={3} py={1.5} borderRadius="md" bg="white"
                border="1px solid #E4E2DC" display="flex" alignItems="center" gap={2}>
                {e.status === 'enriched'
                  ? <CheckCircle2 size={10} color="#27AE60" />
                  : <XCircle size={10} color="#C0392B" />}
                <Box>
                  <Text fontSize="10px" fontWeight={600} color="#2D2A24"
                    fontFamily='"JetBrains Mono", monospace' maxW="140px"
                    overflow="hidden" textOverflow="ellipsis" whiteSpace="nowrap"
                    title={e.slug}>
                    {e.slug}
                  </Text>
                  {e.status === 'enriched' && (
                    <Text fontSize="8px" color="#27AE60">
                      {e.old_len}c → {e.new_len}c (+{e.new_len - e.old_len}c)
                    </Text>
                  )}
                </Box>
              </Box>
            ))}
          </Flex>
        </Box>
      )}
    </Box>
  )
}

export default GeminiBotMonitor
