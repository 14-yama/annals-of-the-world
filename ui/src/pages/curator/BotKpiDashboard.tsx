import React, { useEffect, useState, useCallback, useMemo } from 'react'
import { Box, Flex, Text, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, Activity, GitBranch, AlertTriangle, CheckCircle2, Clock, Pause,
  Cpu, Swords, Zap, StopCircle, RefreshCw, Server, CloudOff, Cloud,
  TrendingUp, Bot, Gauge, Layers,
} from 'lucide-react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import GeminiBotMonitor from '../../components/GeminiBotMonitor'

/* ─────────────────────────────────────────────────────────────────────────────
   Types
   ────────────────────────────────────────────────────────────────────────── */

interface BudgetState {
  monthlyReadCap: number
  monthlyWriteCap: number
  perRunWriteCap: number
  hardStopPercent: number
  current: { readsUsed: number; writesUsed: number; lastUpdated: string; cycleStart: string }
  manualPause: boolean
  manualPauseReason?: string
}

interface LastSync {
  lastSyncedCommit?: string
  lastRunAt?: string
  lastRunStatus?: string
  lastRunStats?: Record<string, number | string>
}

interface AuditReport {
  generatedAt?: string
  summary?: Record<string, number | string>
  [k: string]: unknown
}

interface EnrichmentLastRun {
  generatedAt?: string
  timestamp?: string
  model?: string
  attempted?: number
  count_requested?: number
  succeeded?: number
  enriched?: number
  failed?: number
  rejected?: number
  results?: Array<{ slug: string; status: string; reason?: string }>
  entities?: Array<{ slug: string; status: string }>
}

interface LocalJob {
  job_id: string
  bot: string
  status: 'queued' | 'running' | 'done' | 'error' | 'stopped'
  model: string
  count: number
  pid: number | null
  started: string
  finished: string | null
  log: string[]
  exitCode: number | null
}

interface LocalHealth {
  status: string
  ollama: { running: boolean; models: string[]; error?: string }
  activeJobs: number
}

interface GhRunsStatus {
  workflow?: string
  run_id?: string
  status?: string
  completedAt?: string
  queue?: string
}

interface ModelRunStatus {
  workflow?: string
  model?: string
  class?: string
  run_id?: string
  status?: string
  completedAt?: string
}

/* ─────────────────────────────────────────────────────────────────────────────
   Bot Roster (online + local)
   ────────────────────────────────────────────────────────────────────────── */

interface BotEntry {
  key: string
  label: string
  channel: 'online' | 'local'
  family: 'enrichment' | 'audit' | 'sync' | 'edge'
  color: string
  description: string
  /** Source file under /audit-reports for audit-style bots */
  reportFile?: string
  /** Local bot endpoint (for assist button) */
  localEndpoint?: string
  defaultCount?: number
  defaultModel?: string
  /** Editor-id needle to count Appwrite audit_log rows */
  editorMatch?: RegExp
  /** Free-tier hard limit per calendar day (0 = unlimited) */
  dailyCap?: number
  /** Expected seconds between cron runs — used to detect STALE state */
  cronIntervalS?: number
}

const BOT_ROSTER: BotEntry[] = [
  // ── Online (cloud) enrichment bots ─────────────────────────────────────────
  {
    key: 'gemini', label: 'Gemini 2.5 Flash', channel: 'online', family: 'enrichment',
    color: '#4285F4',
    description: 'Free · 1,500 RPD · 60/run × 24 runs/day. All entity classes.',
    editorMatch: /gemini/i,
    dailyCap: 1500, cronIntervalS: 3600,
  },
  {
    key: 'github-models', label: 'GH Models · gpt-4o-mini', channel: 'online', family: 'enrichment',
    color: '#6B3FA0',
    description: 'Free · 150 RPD (separate bucket) · Class 3 (Institutions) + Class 7 (Texts).',
    editorMatch: /gpt-4o-mini/i,
    dailyCap: 150, cronIntervalS: 14400,
  },
  {
    key: 'gh-phi4', label: 'GH Models · Phi-4-mini', channel: 'online', family: 'enrichment',
    color: '#0078D4',
    description: 'Free · 150 RPD (separate bucket) · Class 2 (People) stubs.',
    editorMatch: /phi.?4/i,
    dailyCap: 150, cronIntervalS: 14400,
  },
  {
    key: 'gh-llama', label: 'GH Models · Llama-3.1-8B', channel: 'online', family: 'enrichment',
    color: '#4267B2',
    description: 'Free · 150 RPD (separate bucket) · Class 5 (Places) stubs.',
    editorMatch: /llama/i,
    dailyCap: 150, cronIntervalS: 14400,
  },
  {
    key: 'gh-mistral', label: 'GH Models · Mistral-Nemo', channel: 'online', family: 'enrichment',
    color: '#F97316',
    description: 'Free · 150 RPD (separate bucket) · Class 6 (Events). 12B — best GH Models quality.',
    editorMatch: /mistral/i,
    dailyCap: 150, cronIntervalS: 14400,
  },
  {
    key: 'openai', label: 'OpenAI GPT-4o-mini', channel: 'online', family: 'enrichment',
    color: '#10A37F',
    description: 'Paid fallback ($0.15/1M tokens) · activates when Gemini exhausts quota.',
    editorMatch: /openai/i,
    dailyCap: 0,
  },
  // ── Local enrichment bots ──────────────────────────────────────────────────
  {
    key: 'ollama-enrich', label: 'Ollama llama3.2:3b', channel: 'local', family: 'enrichment',
    color: '#27AE60',
    description: 'Local CPU inference. Free, unlimited, on-device.',
    localEndpoint: '/bots/enrich', defaultCount: 20, defaultModel: 'ollama',
    editorMatch: /ollama/i,
  },
  {
    key: 'ollama-significance', label: 'Ollama — Significance', channel: 'local', family: 'audit',
    color: '#8E44AD',
    description: 'Local backfill of historicalSignificance ratings.',
    localEndpoint: '/bots/significance', defaultCount: 50, defaultModel: 'ollama',
    reportFile: 'significance_run.json',
  },
  {
    key: 'ollama-edges', label: 'Ollama — Edge Bot', channel: 'local', family: 'edge',
    color: '#1ABC9C',
    description: 'Generates relationship edges for under-connected entities.',
    localEndpoint: '/bots/enrich', defaultCount: 20, defaultModel: 'ollama',
    reportFile: 'edge_run.json',
  },
  // ── Cloud audit bots (Appwrite Functions) ──────────────────────────────────
  {
    key: 'completeness', label: 'Completeness Audit', channel: 'online', family: 'audit',
    color: '#27AE60',
    description: 'Scores entities on 9 quality dimensions (daily 02:00 UTC).',
    reportFile: 'completeness.json',
  },
  {
    key: 'orphans', label: 'Orphan Detector', channel: 'online', family: 'audit',
    color: '#E67E22',
    description: 'Finds entities with zero relationships (daily 03:00 UTC).',
    reportFile: 'orphans.json',
  },
  {
    key: 'consistency', label: 'Consistency Audit', channel: 'online', family: 'audit',
    color: '#6B3FA0',
    description: 'Validates era/division, callNumber, slugs (daily 05:00 UTC).',
    reportFile: 'consistency.json',
  },
  {
    key: 'duplicates', label: 'Duplicate Finder', channel: 'online', family: 'audit',
    color: '#C0392B',
    description: 'Levenshtein fuzzy duplicate detection (weekly).',
    reportFile: 'duplicates.json',
  },
  {
    key: 'classification', label: 'Classification Audit', channel: 'online', family: 'audit',
    color: '#D4AF37',
    description: 'Verifies Dewey call-number classifications.',
    reportFile: 'classification.json',
  },
  {
    key: 'stats', label: 'Stats Counter', channel: 'online', family: 'audit',
    color: '#4A90D9',
    description: 'Recounts entity totals & dashboard metrics.',
    reportFile: 'stats.json',
  },
  // ── Sync ───────────────────────────────────────────────────────────────────
  {
    key: 'sync-gateway', label: 'Sync Gateway', channel: 'online', family: 'sync',
    color: '#9E9A90',
    description: 'Single Appwrite writer — pushes enriched files to backend.',
    editorMatch: /sync-gateway/i,
  },
]

/* ─────────────────────────────────────────────────────────────────────────────
   Helpers
   ────────────────────────────────────────────────────────────────────────── */

async function fetchJSON<T>(url: string): Promise<T | null> {
  try {
    const r = await fetch(url, { cache: 'no-store' })
    if (!r.ok) return null
    return (await r.json()) as T
  } catch { return null }
}

function relTime(iso?: string): string {
  if (!iso) return 'never'
  const d = new Date(iso).getTime()
  if (isNaN(d)) return 'never'
  const s = Math.max(0, (Date.now() - d) / 1000)
  if (s < 60) return `${Math.floor(s)}s ago`
  if (s < 3600) return `${Math.floor(s / 60)}m ago`
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`
  return `${Math.floor(s / 86400)}d ago`
}

/* ─── Bot state ─────────────────────────────────────────────────────────── */

type BotState = 'running' | 'idle' | 'stale' | 'error' | 'pending'

const BOT_STATE_CFG: Record<BotState, { label: string; color: string; bg: string; border: string }> = {
  running: { label: 'RUNNING', color: '#E67E22', bg: '#FFF5EB', border: '#E67E2260' },
  idle:    { label: 'IDLE',    color: '#27AE60', bg: '#F0FFF4', border: '#27AE6060' },
  stale:   { label: 'STALE',  color: '#C5963A', bg: '#FFFBEB', border: '#C5963A60' },
  error:   { label: 'ERROR',  color: '#C0392B', bg: '#FFF5F5', border: '#C0392B60' },
  pending: { label: 'PENDING', color: '#9E9A90', bg: '#F5F4F0', border: '#D4D0C8'  },
}

function deriveBotState(
  lastStatus?: string,
  completedAt?: string,
  cronIntervalS?: number,
  activeJob?: LocalJob,
): BotState {
  if (activeJob?.status === 'running') return 'running'
  if (!lastStatus && !completedAt) return 'pending'
  if (lastStatus === 'failure') return 'error'
  if (lastStatus === 'success' || completedAt) {
    if (cronIntervalS && completedAt) {
      const elapsed = (Date.now() - new Date(completedAt).getTime()) / 1000
      // Overdue if 2.5× cron interval has passed without a new run
      if (elapsed > cronIntervalS * 2.5) return 'stale'
    }
    return 'idle'
  }
  return 'pending'
}

function quotaPctColor(pct: number): string {
  if (pct >= 90) return '#C0392B'
  if (pct >= 75) return '#E67E22'
  if (pct >= 50) return '#D4AF37'
  return '#27AE60'
}

/* ─────────────────────────────────────────────────────────────────────────────
   Component
   ────────────────────────────────────────────────────────────────────────── */

export default function BotKpiDashboard() {
  const navigate = useNavigate()

  // Telemetry state
  const [budget, setBudget] = useState<BudgetState | null>(null)
  const [lastSync, setLastSync] = useState<LastSync | null>(null)
  const [enrichRun, setEnrichRun] = useState<EnrichmentLastRun | null>(null)
  const [ghRuns, setGhRuns] = useState<GhRunsStatus | null>(null)
  const [modelRuns, setModelRuns] = useState<Record<string, ModelRunStatus | null>>({})
  const [reports, setReports] = useState<Record<string, AuditReport | null>>({})
  const [localHealth, setLocalHealth] = useState<LocalHealth | null>(null)
  const [localJobs, setLocalJobs] = useState<Record<string, LocalJob>>({})

  // Editor-id activity counts (from Appwrite audit_log)
  const [editorCounts, setEditorCounts] = useState<Record<string, number>>({})
  const [totalAuditRows, setTotalAuditRows] = useState<number>(0)
  const [last24hRows, setLast24hRows] = useState<number>(0)
  const [last1hRows, setLast1hRows] = useState<number>(0)

  // UI state
  const [autoRefresh, setAutoRefresh] = useState(true)
  const [lastRefresh, setLastRefresh] = useState<Date>(new Date())
  const [assistingBot, setAssistingBot] = useState<Record<string, boolean>>({})
  const [assistAllActive, setAssistAllActive] = useState(false)
  const [showLocalLog, setShowLocalLog] = useState<string | null>(null)

  /* ── Local Bot API ─────────────────────────────────────────────────────── */

  const localGet = useCallback(async <T,>(endpoint: string): Promise<T | null> => {
    try {
      const r = await fetch(`/local-bots${endpoint}`, { cache: 'no-store' })
      if (!r.ok) return null
      return (await r.json()) as T
    } catch { return null }
  }, [])

  const localPost = useCallback(async (endpoint: string, body: Record<string, unknown> = {}): Promise<Record<string, unknown> | null> => {
    try {
      const r = await fetch(`/local-bots${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      })
      if (!r.ok) return null
      return (await r.json()) as Record<string, unknown>
    } catch { return null }
  }, [])

  const pollLocalStatus = useCallback(async () => {
    const [health, jobs] = await Promise.all([
      localGet<LocalHealth>('/health'),
      localGet<Record<string, LocalJob>>('/bots/status'),
    ])
    if (health) setLocalHealth(health)
    if (jobs) setLocalJobs(jobs)
  }, [localGet])

  async function assistBot(bot: BotEntry) {
    if (!bot.localEndpoint) return
    setAssistingBot(p => ({ ...p, [bot.key]: true }))
    const body: Record<string, unknown> = {}
    if (bot.defaultCount && bot.defaultCount > 0) body.count = bot.defaultCount
    if (bot.localEndpoint === '/bots/enrich') body.model = bot.defaultModel
    await localPost(bot.localEndpoint, body)
    await pollLocalStatus()
    setAssistingBot(p => ({ ...p, [bot.key]: false }))
  }

  async function assistAll() {
    setAssistAllActive(true)
    await localPost('/bots/all', { enrichCount: 20, sigCount: 50 })
    await pollLocalStatus()
    setAssistAllActive(false)
  }

  async function stopAllBots() {
    await localPost('/bots/stop', {})
    await pollLocalStatus()
  }

  /* ── Telemetry loader ──────────────────────────────────────────────────── */

  const loadTelemetry = useCallback(async () => {
    const reportFiles = BOT_ROSTER.filter(b => b.reportFile).map(b => b.reportFile!)
    const [b, ls, er, gh, phi4, llama, mistral, ...rs] = await Promise.all([
      fetchJSON<BudgetState>('/governance/budget.json'),
      fetchJSON<LastSync>('/governance/last_sync.json'),
      fetchJSON<EnrichmentLastRun>('/enrichment/last_run.json'),
      fetchJSON<GhRunsStatus>('/governance/last_github_runs.json'),
      fetchJSON<ModelRunStatus>('/governance/last_phi4_run.json'),
      fetchJSON<ModelRunStatus>('/governance/last_llama_run.json'),
      fetchJSON<ModelRunStatus>('/governance/last_mistral_run.json'),
      ...reportFiles.map(f => fetchJSON<AuditReport>(`/audit-reports/${f}`)),
    ])
    setBudget(b)
    setLastSync(ls)
    setEnrichRun(er)
    setGhRuns(gh)
    setModelRuns({ 'gh-phi4': phi4, 'gh-llama': llama, 'gh-mistral': mistral })
    const next: Record<string, AuditReport | null> = {}
    let i = 0
    for (const bot of BOT_ROSTER) {
      if (bot.reportFile) { next[bot.key] = rs[i] ?? null; i++ }
    }
    setReports(next)
    setLastRefresh(new Date())
  }, [])

  /* ── Appwrite audit_log activity scan ──────────────────────────────────── */

  const loadAuditActivity = useCallback(async () => {
    try {
      // Total count (head)
      const totalRes = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG,
        [Query.limit(1)])
      setTotalAuditRows(totalRes.total)

      // Last 24h sample for per-bot breakdown
      const dayAgo = new Date(Date.now() - 24 * 3600 * 1000).toISOString()
      const sample = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, [
        Query.greaterThan('timestamp', dayAgo),
        Query.orderDesc('timestamp'),
        Query.limit(500),
      ])
      setLast24hRows(sample.total)

      // Last hour count
      const hourAgo = new Date(Date.now() - 3600 * 1000).toISOString()
      const hour = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, [
        Query.greaterThan('timestamp', hourAgo),
        Query.limit(1),
      ])
      setLast1hRows(hour.total)

      // Per-bot counts (from the 500-row sample)
      const counts: Record<string, number> = {}
      for (const doc of sample.documents) {
        const eid = (doc.editorId as string) ?? ''
        for (const bot of BOT_ROSTER) {
          if (bot.editorMatch && bot.editorMatch.test(eid)) {
            counts[bot.key] = (counts[bot.key] ?? 0) + 1
          }
        }
      }
      setEditorCounts(counts)
    } catch (err) {
      console.warn('Audit activity scan failed:', err)
    }
  }, [])

  /* ── Polling ───────────────────────────────────────────────────────────── */

  useEffect(() => {
    loadTelemetry()
    loadAuditActivity()
    pollLocalStatus()
    if (!autoRefresh) return
    const t1 = setInterval(loadTelemetry, 5000)
    const t2 = setInterval(pollLocalStatus, 3000)
    const t3 = setInterval(loadAuditActivity, 15000)
    return () => { clearInterval(t1); clearInterval(t2); clearInterval(t3) }
  }, [autoRefresh, loadTelemetry, loadAuditActivity, pollLocalStatus])

  /* ── Derived KPIs ──────────────────────────────────────────────────────── */

  const onlineEnrichBots = BOT_ROSTER.filter(b => b.channel === 'online' && b.family === 'enrichment')
  const localBots        = BOT_ROSTER.filter(b => b.channel === 'local')

  const totals = useMemo(() => {
    const sum = (keys: string[]) => keys.reduce((s, k) => s + (editorCounts[k] ?? 0), 0)
    const onlineEnrichEdits = sum(onlineEnrichBots.map(b => b.key))
    const localEdits        = sum(localBots.map(b => b.key))
    const totalEdits24h     = onlineEnrichEdits + localEdits
    const localShare = totalEdits24h > 0
      ? Math.round((localEdits / totalEdits24h) * 100) : 0
    const onlineShare = totalEdits24h > 0
      ? Math.round((onlineEnrichEdits / totalEdits24h) * 100) : 0
    return { onlineEnrichEdits, localEdits, totalEdits24h, localShare, onlineShare }
  }, [editorCounts, onlineEnrichBots, localBots])

  // Active local jobs count
  const activeLocalJobs = useMemo(
    () => Object.values(localJobs).filter(j => j.status === 'running').length,
    [localJobs],
  )

  /* ── Render ────────────────────────────────────────────────────────────── */

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      {/* Header */}
      <Flex align="center" gap={3} mb={6}>
        <Box
          as="button" onClick={() => navigate('/curator/audit')}
          p={2} borderRadius="md" bg="#F5F4F0" cursor="pointer" _hover={{ bg: '#E4E2DC' }}
        >
          <ChevronLeft size={18} color="#787469" />
        </Box>
        <Box p={2} borderRadius="md" bg="#D4AF3720">
          <Bot size={24} color="#D4AF37" />
        </Box>
        <Box flex={1}>
          <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
            BOT KPI COMMAND POST
          </Text>
          <Text fontSize="sm" color="#787469">
            Combined telemetry across online & local enrichment bots — see who is doing the heavy lifting
          </Text>
        </Box>
        <Box
          as="button" onClick={() => setAutoRefresh(v => !v)}
          px={3} py={2} borderRadius="md"
          bg={autoRefresh ? '#27AE6020' : '#F5F4F0'}
          color={autoRefresh ? '#27AE60' : '#787469'}
          border="1px solid #E4E2DC"
          cursor="pointer" fontSize="xs" fontWeight={600}
        >
          {autoRefresh ? '● LIVE — pause' : '○ PAUSED — resume'}
        </Box>
        <Text fontSize="11px" color="#9E9A90">
          updated {relTime(lastRefresh.toISOString())}
        </Text>
      </Flex>

      {/* ════════════════════════════════════════════════════════════════════
          GRAND SUMMARY — TOTAL OF ALL BOTS
          ════════════════════════════════════════════════════════════════ */}
      <Box mb={6} p={5} borderRadius="lg"
        bg="linear-gradient(135deg, #FAF3E8 0%, #F5F4F0 100%)"
        border="1px solid #D4AF3740">
        <Flex align="center" gap={2} mb={4}>
          <Gauge size={16} color="#D4AF37" />
          <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
            color="#2D2A24" letterSpacing="0.1em" textTransform="uppercase">
            Combined Bot KPIs — All Fronts
          </Text>
        </Flex>

        <SimpleGrid columns={{ base: 2, md: 4, lg: 6 }} gap={4}>
          <KpiCell
            icon={<Activity size={14} color="#D4AF37" />}
            label="Audit log total"
            value={totalAuditRows.toLocaleString()}
            sub="all-time edits in Appwrite"
            color="#D4AF37"
          />
          <KpiCell
            icon={<Clock size={14} color="#4A90D9" />}
            label="Edits last 24h"
            value={last24hRows.toLocaleString()}
            sub="all editors combined"
            color="#4A90D9"
          />
          <KpiCell
            icon={<Zap size={14} color="#E67E22" />}
            label="Edits last 1h"
            value={last1hRows.toLocaleString()}
            sub="active right now"
            color="#E67E22"
          />
          <KpiCell
            icon={<Cloud size={14} color="#2471A3" />}
            label="Online bots (24h)"
            value={totals.onlineEnrichEdits.toLocaleString()}
            sub={`${totals.onlineShare}% of work`}
            color="#2471A3"
          />
          <KpiCell
            icon={<Cpu size={14} color="#27AE60" />}
            label="Local bots (24h)"
            value={totals.localEdits.toLocaleString()}
            sub={`${totals.localShare}% of work`}
            color="#27AE60"
          />
          <KpiCell
            icon={<Bot size={14} color="#6B3FA0" />}
            label="Active local jobs"
            value={String(activeLocalJobs)}
            sub={localHealth?.ollama.running ? 'Ollama online' : 'Ollama offline'}
            color={localHealth?.ollama.running ? '#27AE60' : '#9E9A90'}
          />
        </SimpleGrid>

        {/* Heavy-lifter bar */}
        <Box mt={4}>
          <Flex align="center" gap={2} mb={2}>
            <TrendingUp size={12} color="#787469" />
            <Text fontSize="10px" color="#787469" fontWeight={700}
              letterSpacing="0.08em" textTransform="uppercase">
              Heavy-Lifter Split (last 24h)
            </Text>
          </Flex>
          <Box h="14px" borderRadius="full" overflow="hidden"
            bg="#E4E2DC" position="relative" display="flex">
            <Box w={`${totals.onlineShare}%`} bg="#2471A3"
              transition="width 0.6s ease" />
            <Box w={`${totals.localShare}%`} bg="#27AE60"
              transition="width 0.6s ease" />
            <Box flex={1} bg="#E4E2DC" />
          </Box>
          <Flex justify="space-between" mt={1}>
            <Text fontSize="10px" color="#2471A3" fontWeight={600}>
              ☁ Online · {totals.onlineEnrichEdits} edits ({totals.onlineShare}%)
            </Text>
            <Text fontSize="10px" color="#27AE60" fontWeight={600}>
              💻 Local · {totals.localEdits} edits ({totals.localShare}%)
            </Text>
          </Flex>
        </Box>
      </Box>

      {/* ════════════════════════════════════════════════════════════════════
          INFRA STATE — Budget · Sync · Last Enrichment · GH Actions
          ════════════════════════════════════════════════════════════════ */}
      <SimpleGrid columns={{ base: 1, md: 4 }} gap={3} mb={6}>
        {/* Budget */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            {budget?.manualPause
              ? <Pause size={14} color="#C0392B" />
              : <CheckCircle2 size={14} color="#27AE60" />}
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              Cost Budget
            </Text>
            {budget?.manualPause && (
              <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
                bg="#C0392B20" color="#C0392B" borderRadius="md">
                PAUSED
              </Box>
            )}
          </Flex>
          {budget ? (
            <>
              <Text fontSize="13px" fontWeight={600} color="#2D2A24">
                {budget.current.writesUsed.toLocaleString()} / {budget.monthlyWriteCap.toLocaleString()} writes
              </Text>
              <Box mt={1} h="6px" bg="#F5F4F0" borderRadius="full" overflow="hidden">
                <Box h="100%" w={`${Math.min(100,
                  (budget.current.writesUsed / Math.max(1, budget.monthlyWriteCap)) * 100)}%`}
                  bg={
                    (budget.current.writesUsed / Math.max(1, budget.monthlyWriteCap)) * 100
                      >= budget.hardStopPercent ? '#C0392B' : '#27AE60'
                  } />
              </Box>
              <Text mt={1} fontSize="10px" color="#9E9A90">
                hard-stop at {budget.hardStopPercent}% · cycle from {budget.current.cycleStart}
              </Text>
            </>
          ) : <Text fontSize="12px" color="#9E9A90">no budget.json</Text>}
        </Box>

        {/* Sync */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <GitBranch size={14} color="#4A90D9" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              Sync Gateway
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg={lastSync?.lastRunStatus === 'ok' ? '#27AE6020' :
                lastSync?.lastRunStatus === 'budget_exceeded' ? '#C0392B20' : '#F5F4F0'}
              color={lastSync?.lastRunStatus === 'ok' ? '#27AE60' :
                lastSync?.lastRunStatus === 'budget_exceeded' ? '#C0392B' : '#9E9A90'}
              borderRadius="md">
              {(lastSync?.lastRunStatus ?? 'idle').toUpperCase()}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {lastSync?.lastRunStats
              ? `${lastSync.lastRunStats.writes ?? 0} writes · ${lastSync.lastRunStats.changed ?? 0} files`
              : 'never run'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90" fontFamily='"JetBrains Mono", monospace'>
            commit {lastSync?.lastSyncedCommit?.slice(0, 8) ?? '—'} · {relTime(lastSync?.lastRunAt)}
          </Text>
        </Box>

        {/* Last enrichment run */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <Activity size={14} color="#D4AF37" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              Last Enrich Run
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg="#D4AF3720" color="#D4AF37" borderRadius="md">
              {enrichRun?.model?.toUpperCase() ?? 'IDLE'}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {enrichRun
              ? `${enrichRun.enriched ?? enrichRun.succeeded ?? 0} ok · ${enrichRun.failed ?? 0} fail`
              : 'never run'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90">
            {enrichRun?.count_requested || enrichRun?.attempted
              ? `${enrichRun.count_requested ?? enrichRun.attempted} attempted · ${relTime(enrichRun.timestamp ?? enrichRun.generatedAt)}`
              : 'awaiting run'}
          </Text>
        </Box>

        {/* GitHub Actions latest */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <Cloud size={14} color="#6B3FA0" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              GH Models — gpt-4o-mini
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg={ghRuns?.status === 'success' ? '#27AE6020' :
                ghRuns?.status === 'failure' ? '#C0392B20' : '#F5F4F0'}
              color={ghRuns?.status === 'success' ? '#27AE60' :
                ghRuns?.status === 'failure' ? '#C0392B' : '#9E9A90'}
              borderRadius="md">
              {(ghRuns?.status ?? 'unknown').toUpperCase()}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {ghRuns?.workflow ?? '—'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90">
            run #{ghRuns?.run_id ?? '—'} · {relTime(ghRuns?.completedAt)}
          </Text>
        </Box>

        {/* Phi-4-mini latest */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <Cloud size={14} color="#0078D4" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              GH Models — Phi-4-mini
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg={modelRuns['gh-phi4']?.status === 'success' ? '#27AE6020' :
                modelRuns['gh-phi4']?.status === 'failure' ? '#C0392B20' : '#F5F4F0'}
              color={modelRuns['gh-phi4']?.status === 'success' ? '#27AE60' :
                modelRuns['gh-phi4']?.status === 'failure' ? '#C0392B' : '#9E9A90'}
              borderRadius="md">
              {(modelRuns['gh-phi4']?.status ?? 'pending').toUpperCase()}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {modelRuns['gh-phi4']?.class ?? 'Class 2 · People'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90">
            {relTime(modelRuns['gh-phi4']?.completedAt)}
          </Text>
        </Box>

        {/* Llama-3.1-8B latest */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <Cloud size={14} color="#4267B2" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              GH Models — Llama-3.1-8B
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg={modelRuns['gh-llama']?.status === 'success' ? '#27AE6020' :
                modelRuns['gh-llama']?.status === 'failure' ? '#C0392B20' : '#F5F4F0'}
              color={modelRuns['gh-llama']?.status === 'success' ? '#27AE60' :
                modelRuns['gh-llama']?.status === 'failure' ? '#C0392B' : '#9E9A90'}
              borderRadius="md">
              {(modelRuns['gh-llama']?.status ?? 'pending').toUpperCase()}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {modelRuns['gh-llama']?.class ?? 'Class 5 · Places'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90">
            {relTime(modelRuns['gh-llama']?.completedAt)}
          </Text>
        </Box>

        {/* Mistral-Nemo latest */}
        <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
          <Flex align="center" gap={2} mb={2}>
            <Cloud size={14} color="#F97316" />
            <Text fontSize="11px" fontWeight={700} color="#787469"
              letterSpacing="0.06em" textTransform="uppercase">
              GH Models — Mistral-Nemo
            </Text>
            <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
              bg={modelRuns['gh-mistral']?.status === 'success' ? '#27AE6020' :
                modelRuns['gh-mistral']?.status === 'failure' ? '#C0392B20' : '#F5F4F0'}
              color={modelRuns['gh-mistral']?.status === 'success' ? '#27AE60' :
                modelRuns['gh-mistral']?.status === 'failure' ? '#C0392B' : '#9E9A90'}
              borderRadius="md">
              {(modelRuns['gh-mistral']?.status ?? 'pending').toUpperCase()}
            </Box>
          </Flex>
          <Text fontSize="13px" fontWeight={600} color="#2D2A24">
            {modelRuns['gh-mistral']?.class ?? 'Class 6 · Events'}
          </Text>
          <Text mt={1} fontSize="10px" color="#9E9A90">
            {relTime(modelRuns['gh-mistral']?.completedAt)}
          </Text>
        </Box>
      </SimpleGrid>

      {/* ════════════════════════════════════════════════════════════════════
          ONLINE BOTS — cloud enrichment
          ════════════════════════════════════════════════════════════════ */}
      <SectionHeader icon={<Cloud size={16} color="#2471A3" />}
        title="Online Bots — Cloud" subtitle="5 enrichment bots · Gemini 1,440/day + 4× GH Models 120/day = ~1,920/day free tier · Appwrite audit Functions" />

      {/* Free-tier quota health strip */}
      <Box mb={4} p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
        <Text fontSize="10px" fontWeight={700} color="#787469" mb={3}
          letterSpacing="0.08em" textTransform="uppercase">
          Free Tier Quota — Today's Usage
        </Text>
        <Flex gap={3} flexWrap="wrap">
          {BOT_ROSTER.filter(b => (b.dailyCap ?? 0) > 0).map(b => {
            const used = editorCounts[b.key] ?? 0
            const cap  = b.dailyCap!
            const pct  = Math.min(100, Math.round(used / cap * 100))
            const col  = quotaPctColor(pct)
            const runInfo = b.key === 'gemini'
              ? { status: enrichRun ? 'success' : undefined, completedAt: enrichRun?.timestamp ?? enrichRun?.generatedAt }
              : b.key === 'github-models' ? (ghRuns ?? {})
              : (modelRuns[b.key] ?? {})
            const st = deriveBotState(runInfo.status, runInfo.completedAt, b.cronIntervalS)
            const sc = BOT_STATE_CFG[st]
            return (
              <Box key={b.key} flex="1" minW="120px">
                <Flex align="center" justify="space-between" mb={1}>
                  <Text fontSize="9px" fontWeight={700} color="#2D2A24" noOfLines={1}>
                    {b.label.replace('GH Models · ', '')}
                  </Text>
                  <Box px={1.5} py={0} fontSize="8px" fontWeight={700}
                    bg={sc.bg} color={sc.color} borderRadius="sm"
                    border={`1px solid ${sc.border}`}>
                    {sc.label}
                  </Box>
                </Flex>
                <Box h="6px" bg="#F5F4F0" borderRadius="full" overflow="hidden">
                  <Box h="100%" w={`${pct}%`} bg={col}
                    transition="width 0.5s ease" borderRadius="full" />
                </Box>
                <Flex justify="space-between" mt={0.5}>
                  <Text fontSize="9px" color="#9E9A90">{used} / {cap.toLocaleString()} RPD</Text>
                  <Text fontSize="9px" fontWeight={700} color={col}>{pct}%</Text>
                </Flex>
              </Box>
            )
          })}
        </Flex>
        <Flex gap={3} mt={2} pt={2} borderTop="1px solid #F5F4F0">
          {([['#27AE60','< 50% — Safe'],['#D4AF37','50–74% — Moderate'],['#E67E22','75–89% — High'],['#C0392B','≥ 90% — Critical']] as const).map(([c,l]) => (
            <Flex key={l} align="center" gap={1}>
              <Box w={2} h={2} borderRadius="full" bg={c} />
              <Text fontSize="9px" color="#787469">{l}</Text>
            </Flex>
          ))}
        </Flex>
      </Box>

      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3} mb={6}>
        {BOT_ROSTER.filter(b => b.channel === 'online').map(b => {
          const runInfo = b.key === 'gemini'
            ? { status: enrichRun ? 'success' : undefined, completedAt: enrichRun?.timestamp ?? enrichRun?.generatedAt }
            : b.key === 'github-models' ? (ghRuns ?? {})
            : (modelRuns[b.key] ?? {})
          return (
            <BotCard key={b.key}
              bot={b}
              editsLast24h={editorCounts[b.key] ?? 0}
              report={reports[b.key] ?? null}
              lastRunStatus={runInfo.status}
              lastRunTime={runInfo.completedAt}
            />
          )
        })}
      </SimpleGrid>

      {/* ════════════════════════════════════════════════════════════════════
          LOCAL BOTS — on-device
          ════════════════════════════════════════════════════════════════ */}
      <SectionHeader icon={<Cpu size={16} color="#27AE60" />}
        title="Local Bots — On-Device" subtitle="Ollama llama3.2:3b · runs only while your machine is powered on" />

      {/* Local control bar */}
      <Box mb={3} p={3} borderRadius="md"
        bg={localHealth?.ollama.running ? '#FAF3E8' : '#F5F4F0'}
        border={`1px solid ${localHealth?.ollama.running ? '#C5963A40' : '#E4E2DC'}`}>
        <Flex align="center" gap={2} flexWrap="wrap">
          <Box px={2} py={0.5} borderRadius="full" fontSize="9px" fontWeight={700}
            bg={localHealth?.ollama.running ? '#27AE6015' : '#C0392B15'}
            border={`1px solid ${localHealth?.ollama.running ? '#27AE6040' : '#C0392B40'}`}
            color={localHealth?.ollama.running ? '#27AE60' : '#C0392B'}>
            {localHealth?.ollama.running
              ? `OLLAMA ONLINE · ${localHealth.ollama.models?.length ?? 0} model(s)`
              : 'OLLAMA OFFLINE'}
          </Box>
          {(localHealth?.activeJobs ?? 0) > 0 && (
            <Box px={2} py={0.5} borderRadius="full" fontSize="9px" fontWeight={700}
              bg="#E67E2215" border="1px solid #E67E2240" color="#E67E22">
              {localHealth!.activeJobs} JOB(S) RUNNING
            </Box>
          )}
          <Box flex={1} />
          <Box as="button" onClick={() => !assistAllActive && localHealth?.ollama.running && assistAll()}
            px={3} py={1.5} borderRadius="md" fontSize="11px" fontWeight={700}
            cursor={localHealth?.ollama.running ? 'pointer' : 'not-allowed'}
            bg={localHealth?.ollama.running ? '#C5963A' : '#E4E2DC'}
            color={localHealth?.ollama.running ? 'white' : '#9E9A90'}
            display="flex" alignItems="center" gap={1}>
            {assistAllActive ? <Spinner size="xs" /> : <Swords size={12} />}
            <span>{assistAllActive ? 'DEPLOYING ALL…' : '⚔ ASSIST ALL'}</span>
          </Box>
          <Box as="button" onClick={stopAllBots}
            px={3} py={1.5} borderRadius="md" fontSize="11px" fontWeight={700}
            bg="#C0392B10" border="1px solid #C0392B30" color="#C0392B"
            display="flex" alignItems="center" gap={1} cursor="pointer">
            <StopCircle size={12} /><span>STOP ALL</span>
          </Box>
          <Box as="button" onClick={pollLocalStatus}
            px={3} py={1.5} borderRadius="md" fontSize="11px" fontWeight={700}
            bg="#F5F4F0" border="1px solid #E4E2DC" color="#787469"
            display="flex" alignItems="center" gap={1} cursor="pointer">
            <RefreshCw size={12} /><span>REFRESH</span>
          </Box>
        </Flex>

        {!localHealth?.ollama.running && (
          <Box mt={3} p={2} bg="#FEF9E7" border="1px solid #F1C40F40" borderRadius="md">
            <Flex align="center" gap={2}>
              <CloudOff size={13} color="#E67E22" />
              <Text fontSize="11px" color="#2D2A24" fontWeight={600}>
                Local bot server is offline. Start:
              </Text>
              <Text fontSize="11px" fontFamily='"JetBrains Mono", monospace'
                color="#C5963A" bg="#2D2A24" px={2} py={1} borderRadius="sm">
                python3 scripts/local_bot_server.py
              </Text>
            </Flex>
          </Box>
        )}
      </Box>

      <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={3} mb={4}>
        {BOT_ROSTER.filter(b => b.channel === 'local').map(b => {
          const isAssisting = assistingBot[b.key]
          const activeJob = Object.values(localJobs).find(
            j => j.bot === b.localEndpoint?.replace('/bots/', '') && j.status === 'running'
          )
          // Derive last run state from most recent completed local job
          const lastJob = Object.values(localJobs)
            .filter(j => j.bot === b.localEndpoint?.replace('/bots/', '') && j.status !== 'running')
            .sort((a, c) => (c.finished ?? '').localeCompare(a.finished ?? ''))
            .at(0)
          const lastRunStatus = lastJob
            ? (lastJob.status === 'done' ? 'success' : 'failure')
            : undefined
          return (
            <BotCard key={b.key}
              bot={b}
              editsLast24h={editorCounts[b.key] ?? 0}
              report={reports[b.key] ?? null}
              isAssisting={isAssisting}
              activeJob={activeJob}
              onAssist={() => assistBot(b)}
              ollamaOnline={!!localHealth?.ollama.running}
              lastRunStatus={lastRunStatus}
              lastRunTime={lastJob?.finished ?? undefined}
            />
          )
        })}
      </SimpleGrid>

      {/* Running jobs */}
      {Object.keys(localJobs).length > 0 && (
        <Box mb={6}>
          <Text fontSize="10px" fontWeight={700} color="#787469" mb={2}
            letterSpacing="0.08em" textTransform="uppercase">
            Recent Local Jobs
          </Text>
          <Flex gap={2} flexWrap="wrap">
            {Object.values(localJobs)
              .sort((a, b) => b.started.localeCompare(a.started))
              .slice(0, 12)
              .map(job => (
                <Box key={job.job_id} as="button"
                  onClick={() => setShowLocalLog(showLocalLog === job.job_id ? null : job.job_id)}
                  px={3} py={2} borderRadius="md" cursor="pointer"
                  bg={
                    job.status === 'running' ? '#FFF5EB'
                      : job.status === 'done' ? '#F0FAF0'
                      : job.status === 'error' ? '#FEF0EE'
                      : '#F5F4F0'
                  }
                  border={`1px solid ${
                    job.status === 'running' ? '#E67E2260'
                      : job.status === 'done' ? '#27AE6060'
                      : job.status === 'error' ? '#C0392B60'
                      : '#E4E2DC'
                  }`}>
                  <Flex align="center" gap={2}>
                    {job.status === 'running' && <Spinner size="xs" color="#E67E22" />}
                    {job.status === 'done' && <CheckCircle2 size={11} color="#27AE60" />}
                    {job.status === 'error' && <AlertTriangle size={11} color="#C0392B" />}
                    <Box>
                      <Text fontSize="10px" fontWeight={700} color="#2D2A24">
                        {job.bot.toUpperCase()}
                      </Text>
                      <Text fontSize="9px" color="#787469">
                        {job.model} · {job.status} · {relTime(job.started)}
                      </Text>
                    </Box>
                  </Flex>
                  {showLocalLog === job.job_id && job.log.length > 0 && (
                    <Box mt={2} maxH="120px" overflow="auto"
                      bg="#2D2A24" p={2} borderRadius="sm" textAlign="left">
                      {job.log.slice(-30).map((line, i) => (
                        <Text key={i} fontSize="9px" color="#D4D0C8"
                          fontFamily='"JetBrains Mono", monospace' lineHeight="1.6">
                          {line}
                        </Text>
                      ))}
                    </Box>
                  )}
                </Box>
              ))}
          </Flex>
        </Box>
      )}

      {/* Gemini detailed monitor */}
      <SectionHeader icon={<Layers size={16} color="#4285F4" />}
        title="Gemini Detailed Monitor" subtitle="Cloud bot deep-dive · quota · request log" />
      <Box mb={6}>
        <GeminiBotMonitor cloudEditsToday={totals.onlineEnrichEdits} />
      </Box>
    </Box>
  )
}

/* ─────────────────────────────────────────────────────────────────────────────
   Sub-components
   ────────────────────────────────────────────────────────────────────────── */

function KpiCell({ icon, label, value, sub, color }: {
  icon: React.ReactNode; label: string; value: string; sub: string; color: string
}) {
  return (
    <Box p={3} bg="white" borderRadius="md"
      borderLeft={`3px solid ${color}`} border="1px solid #E4E2DC">
      <Flex align="center" gap={1.5} mb={1}>
        {icon}
        <Text fontSize="9px" fontWeight={700} color="#787469"
          letterSpacing="0.06em" textTransform="uppercase">
          {label}
        </Text>
      </Flex>
      <Text fontSize="22px" fontWeight={700} color={color}
        fontFamily='"Cormorant Garamond", serif' lineHeight="1.1">
        {value}
      </Text>
      <Text fontSize="10px" color="#9E9A90" mt={0.5}>
        {sub}
      </Text>
    </Box>
  )
}

function SectionHeader({ icon, title, subtitle }: {
  icon: React.ReactNode; title: string; subtitle?: string
}) {
  return (
    <Flex align="center" gap={2} mb={3} mt={2}>
      {icon}
      <Box>
        <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
          color="#2D2A24" letterSpacing="0.1em" textTransform="uppercase">
          {title}
        </Text>
        {subtitle && (
          <Text fontSize="10px" color="#9E9A90">
            {subtitle}
          </Text>
        )}
      </Box>
    </Flex>
  )
}

function BotCard({ bot, editsLast24h, report, isAssisting, activeJob, onAssist, ollamaOnline,
  lastRunStatus, lastRunTime,
}: {
  bot: BotEntry
  editsLast24h: number
  report: AuditReport | null
  isAssisting?: boolean
  activeJob?: LocalJob
  onAssist?: () => void
  ollamaOnline?: boolean
  lastRunStatus?: string
  lastRunTime?: string
}) {
  const headline = report?.summary ? Object.entries(report.summary)[0] : null

  // State derivation
  const botState = deriveBotState(lastRunStatus, lastRunTime, bot.cronIntervalS, activeJob)
  const sc = BOT_STATE_CFG[botState]

  // Quota
  const cap = bot.dailyCap ?? 0
  const quotaUsed = editsLast24h
  const quotaPct  = cap > 0 ? Math.min(100, Math.round(quotaUsed / cap * 100)) : 0
  const qColor    = quotaPctColor(quotaPct)

  // Warn if near limit
  const nearLimit = cap > 0 && quotaPct >= 75

  return (
    <Box p={3} bg="white"
      border={nearLimit ? `1px solid ${qColor}60` : '1px solid #E4E2DC'}
      borderLeft={`3px solid ${bot.color}`}
      borderRadius="md"
      position="relative">

      {/* Row 1: label + channel + state */}
      <Flex align="center" gap={2} mb={2}>
        <Text fontSize="11px" fontWeight={700} color="#2D2A24" flex={1} lineHeight="1.3">
          {bot.label}
        </Text>
        <Box px={1.5} py={0.5} fontSize="8px" fontWeight={700}
          bg={bot.channel === 'online' ? '#2471A320' : '#27AE6020'}
          color={bot.channel === 'online' ? '#2471A3' : '#27AE60'}
          borderRadius="sm">
          {bot.channel === 'online' ? '☁' : '💻'}
        </Box>
        {/* State pill */}
        <Flex align="center" gap={1} px={1.5} py={0.5} borderRadius="sm"
          bg={sc.bg} border={`1px solid ${sc.border}`}>
          {botState === 'running' && <Spinner size="xs" color={sc.color} />}
          {botState === 'idle'    && <CheckCircle2 size={8} color={sc.color} />}
          {botState === 'stale'   && <AlertTriangle size={8} color={sc.color} />}
          {botState === 'error'   && <AlertTriangle size={8} color={sc.color} />}
          {botState === 'pending' && <Clock size={8} color={sc.color} />}
          <Text fontSize="8px" fontWeight={700} color={sc.color} lineHeight="1">
            {sc.label}
          </Text>
        </Flex>
      </Flex>

      {/* Row 2: edits count */}
      <Flex align="baseline" gap={2}>
        <Text fontSize="22px" fontWeight={700} color={bot.color}
          fontFamily='"Cormorant Garamond", serif' lineHeight="1">
          {editsLast24h}
        </Text>
        <Text fontSize="10px" color="#9E9A90">edits / 24h</Text>
        {lastRunTime && (
          <Text fontSize="9px" color="#9E9A90" ml="auto">
            last: {relTime(lastRunTime)}
          </Text>
        )}
      </Flex>

      {/* Quota bar (enrichment bots only) */}
      {cap > 0 && (
        <Box mt={2}>
          <Flex justify="space-between" align="center" mb={0.5}>
            <Text fontSize="9px" fontWeight={700} color="#787469"
              letterSpacing="0.05em" textTransform="uppercase">
              Free Tier Quota
            </Text>
            <Flex align="center" gap={1}>
              {nearLimit && <AlertTriangle size={8} color={qColor} />}
              <Text fontSize="9px" fontWeight={700} color={qColor}>
                {quotaPct}% · {quotaUsed}/{cap.toLocaleString()}
              </Text>
            </Flex>
          </Flex>
          <Box h="5px" bg="#F5F4F0" borderRadius="full" overflow="hidden">
            <Box h="100%" w={`${quotaPct}%`} bg={qColor}
              transition="width 0.5s ease" borderRadius="full" />
          </Box>
          {nearLimit && (
            <Text fontSize="9px" color={qColor} mt={0.5} fontWeight={600}>
              {quotaPct >= 90 ? '⚠ Approaching daily limit' : '↑ Usage elevated'}
            </Text>
          )}
        </Box>
      )}

      {/* Audit report headline */}
      {report && headline && (
        <Flex align="center" gap={1} mt={2}>
          <Text fontSize="10px" color="#787469">
            {headline[0].replace(/_/g, ' ')}: <strong>{String(headline[1])}</strong>
          </Text>
          <Box ml="auto" />
          <Clock size={9} color="#9E9A90" />
          <Text fontSize="9px" color="#9E9A90">{relTime(report.generatedAt)}</Text>
        </Flex>
      )}

      <Text fontSize="10px" color="#9E9A90" mt={2} lineHeight="1.4">
        {bot.description}
      </Text>

      {/* Assist button (local bots) */}
      {bot.channel === 'local' && onAssist && (
        <Box as="button"
          onClick={() => !isAssisting && ollamaOnline && onAssist()}
          mt={2} w="100%" px={2} py={1} borderRadius="sm"
          fontSize="9px" fontWeight={700} letterSpacing="0.05em"
          border="1px solid"
          cursor={ollamaOnline ? 'pointer' : 'not-allowed'}
          bg={activeJob ? '#E67E2220'
            : ollamaOnline ? `${bot.color}18` : '#F5F4F0'}
          borderColor={activeJob ? '#E67E22'
            : ollamaOnline ? bot.color : '#E4E2DC'}
          color={activeJob ? '#E67E22'
            : ollamaOnline ? bot.color : '#9E9A90'}
          display="flex" alignItems="center" justifyContent="center" gap={1}
          title={ollamaOnline
            ? `Deploy ${bot.defaultModel ?? 'local'} bot`
            : 'Start local_bot_server.py to enable'}>
          {isAssisting
            ? <><Spinner size="xs" /><span>DEPLOYING…</span></>
            : activeJob
              ? <><Zap size={9} /><span>RUNNING</span></>
              : <><Swords size={9} /><span>⚔ ASSIST</span></>}
        </Box>
      )}
    </Box>
  )
}
