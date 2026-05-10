import React, { useEffect, useState, useMemo, useCallback } from 'react'
import { Box, Flex, Text, Input, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, History, Download, Filter, User, FileText,
  Activity, GitBranch, AlertTriangle, CheckCircle2, Clock, Pause,
  Cpu, Swords, Zap, StopCircle, RefreshCw, Server, CloudOff,
} from 'lucide-react'
import { Query, type Models } from 'appwrite'
import client, { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { StatCard } from '../../components/DataCards'

/* ─── Types ─── */

interface AuditRow {
  $id: string
  entityId: string
  entitySlug: string
  entityName: string
  action: string
  field: string
  oldValue: string
  newValue: string
  editorId: string
  editorNote: string
  timestamp: string
  sessionId: string
}

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
  model?: string
  attempted?: number
  succeeded?: number
  failed?: number
  rejected?: number
  results?: Array<{ slug: string; status: string; reason?: string }>
}

const ACTION_COLORS: Record<string, string> = {
  update: '#4A90D9',
  create: '#27AE60',
  delete: '#C0392B',
  batch_update: '#E67E22',
}

/* ─── EditorBadge — parses editorId into a coloured pill ─── */
// Formats produced by the bots:
//   ollama/llama3.2:3b·local·hostname   → green LOCAL badge
//   gemini-2.5-flash·cloud·GH#12345     → blue CLOUD badge
//   gpt-4o-mini·cloud·GH#12345          → blue CLOUD badge
//   ai-enrichment-bot:gemini-2.5-flash  → legacy yellow badge
//   sync-gateway·local·...              → grey SYNC badge
//   system / curator / empty            → grey badge
function EditorBadge({ editorId }: { editorId: string }) {
  if (!editorId) return <Text fontSize="xs" color="#9E9A90">—</Text>

  const isOllama = editorId.startsWith('ollama/')
  const isCloud = editorId.includes('·cloud·') || editorId.includes('GH#')
  const isLocal = editorId.includes('·local·') && !isOllama
  const isSync = editorId.includes('sync-gateway')
  const isLegacy = editorId.includes('ai-enrichment-bot') || editorId.includes('backfill-significance-bot')

  // Parse the structured format: "model·env·context"
  const parts = editorId.split('·')
  const modelPart = parts[0] || editorId
  const envPart = parts[1] || ''
  const ctxPart = parts[2] || ''

  let color = '#787469'
  let bg = 'rgba(120,116,105,0.1)'
  let label = ''
  let detail = ''

  if (isOllama) {
    color = '#27AE60'; bg = 'rgba(39,174,96,0.12)'
    // "ollama/llama3.2:3b·local·hostname" → "🟢 LOCAL · llama3.2:3b @ hostname"
    const model = modelPart.replace('ollama/', '')
    label = '🟢 LOCAL'
    detail = `${model}${ctxPart ? ` @ ${ctxPart}` : ''}`
  } else if (isCloud) {
    color = '#2471A3'; bg = 'rgba(36,113,163,0.12)'
    label = '☁️ CLOUD'
    detail = `${modelPart}${ctxPart ? ` · ${ctxPart}` : ''}`
  } else if (isLocal) {
    color = '#E67E22'; bg = 'rgba(230,126,34,0.12)'
    label = '🟡 LOCAL'
    detail = `${modelPart}${ctxPart ? ` @ ${ctxPart}` : ''}`
  } else if (isSync) {
    color = '#9E9A90'; bg = 'rgba(158,154,144,0.1)'
    label = '⚙️ SYNC'
    detail = ctxPart || modelPart
  } else if (isLegacy) {
    color = '#C27B21'; bg = 'rgba(194,123,33,0.1)'
    label = isCloud ? '☁️ CLOUD' : '🤖 BOT'
    detail = editorId.replace('ai-enrichment-bot:', '').replace('backfill-significance-bot:', '')
  } else {
    label = '👤'
    detail = editorId
  }

  return (
    <Box>
      <Box display="inline-flex" alignItems="center" gap="3px"
        px="5px" py="1px" borderRadius="4px" bg={bg}
        border={`1px solid ${color}30`} mb="1px">
        <Text fontSize="9px" fontWeight={700} color={color} letterSpacing="0.05em">
          {label}
        </Text>
      </Box>
      <Text fontSize="10px" color={color} lineClamp={2} title={editorId} maxW="130px">
        {detail}
      </Text>
    </Box>
  )
}

/* ─── Local Bot Types ─── */

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

/** Monthly capacity for each source. Used in the capacity planning table. */
const CAPACITY_TABLE = [
  {
    source: 'Gemini 2.5 Flash',
    tier: 'Cloud — Free',
    color: '#4285F4',
    models: 'gemini-2.5-flash',
    rate: '500 req/day',
    monthly: 15_000,
    unit: 'entities',
    bestFor: 'Bulk stubs, all scores',
    notes: '1M tokens/day free; 15 RPM; primary cloud bot',
  },
  {
    source: 'GitHub Copilot Premium',
    tier: 'Cloud — Subscription',
    color: '#6B3FA0',
    models: 'Claude Sonnet 4.6, o1, GPT-4o',
    rate: '1,500 req/mo',
    monthly: 1_500,
    unit: 'entities',
    bestFor: 'High-significance (score 8–10)',
    notes: 'Via IDE / GitHub Models API; best quality for world-changing entities',
  },
  {
    source: 'GPT-4o-mini',
    tier: 'Cloud — Paid',
    color: '#10A37F',
    models: 'gpt-4o-mini',
    rate: '$0.15/1M in',
    monthly: 5_000,
    unit: 'entities (~$7.50)',
    bestFor: 'Overflow when Gemini hits quota',
    notes: '$0.15/1M input · $0.60/1M output; ~1,500 tokens/entity',
  },
  {
    source: 'Ollama llama3.2:3b (CPU)',
    tier: 'Local — Free',
    color: '#E67E22',
    models: 'llama3.2:3b',
    rate: '~20 entities/hr',
    monthly: 4_800,
    unit: 'entities (8h/day)',
    bestFor: 'Overnight batch, stubs, significance',
    notes: 'No quota · no cost · runs on-device; speed scales with CPU cores',
  },
  {
    source: 'Ollama llama3.2:3b (GPU)',
    tier: 'Local — Free (if available)',
    color: '#27AE60',
    models: 'llama3.2:3b',
    rate: '~200 entities/hr',
    monthly: 48_000,
    unit: 'entities (8h/day)',
    bestFor: 'Everything — max throughput',
    notes: 'GPU VRAM ≥4 GB; replaces cloud bots entirely for bulk work',
  },
]

const TOTAL_CLOUD_MONTHLY = 15_000 + 1_500 + 5_000   // 21,500
const TOTAL_LOCAL_CPU_MONTHLY = 4_800
const TOTAL_COMBINED_MONTHLY = TOTAL_CLOUD_MONTHLY + TOTAL_LOCAL_CPU_MONTHLY  // 26,300

/* ─── Bot Definitions ─── */

const BOT_REPORTS: Array<{
  key: string; label: string; file: string; color: string
  localEndpoint: string; defaultCount: number; defaultModel: string
  description: string
}> = [
  {
    key: 'stats', label: 'Stats Counter', file: 'stats.json', color: '#4A90D9',
    localEndpoint: '/bots/sync', defaultCount: 50, defaultModel: 'none',
    description: 'Recount entity totals & update stats dashboard',
  },
  {
    key: 'completeness', label: 'Completeness', file: 'completeness.json', color: '#27AE60',
    localEndpoint: '/bots/significance', defaultCount: 50, defaultModel: 'ollama',
    description: 'Score entities on 9 quality dimensions',
  },
  {
    key: 'orphans', label: 'Orphans', file: 'orphans.json', color: '#E67E22',
    localEndpoint: '/bots/queue', defaultCount: 0, defaultModel: 'none',
    description: 'Find entities with zero relationships',
  },
  {
    key: 'consistency', label: 'Consistency', file: 'consistency.json', color: '#6B3FA0',
    localEndpoint: '/bots/queue', defaultCount: 0, defaultModel: 'none',
    description: 'Validate era/division, callNumber, slugs',
  },
  {
    key: 'duplicates', label: 'Duplicates', file: 'duplicates.json', color: '#C0392B',
    localEndpoint: '/bots/queue', defaultCount: 0, defaultModel: 'none',
    description: 'Fuzzy duplicate detection across catalog',
  },
  {
    key: 'classification', label: 'Classification', file: 'classification.json', color: '#D4AF37',
    localEndpoint: '/bots/queue', defaultCount: 0, defaultModel: 'none',
    description: 'Verify call number classifications',
  },
  {
    key: 'edges', label: 'Edge Bot', file: 'edge_run.json', color: '#1ABC9C',
    localEndpoint: '/bots/enrich', defaultCount: 20, defaultModel: 'ollama',
    description: 'Generate missing graph edges for high-significance entities',
  },
  {
    key: 'significance', label: 'Significance', file: 'significance_run.json', color: '#8E44AD',
    localEndpoint: '/bots/significance', defaultCount: 50, defaultModel: 'ollama',
    description: 'Rate & backfill historicalSignificance on enriched entities',
  },
]

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

/* ─── Main Component ─── */

export default function AuditLogViewer() {
  const navigate = useNavigate()
  const [logs, setLogs] = useState<AuditRow[]>([])
  const [loading, setLoading] = useState(true)
  const [total, setTotal] = useState(0)
  const [page, setPage] = useState(0)

  // Filters
  const [filterEntity, setFilterEntity] = useState('')
  const [filterEditor, setFilterEditor] = useState('')
  const [filterAction, setFilterAction] = useState('')

  // Live bot telemetry (git-first)
  const [budget, setBudget] = useState<BudgetState | null>(null)
  const [lastSync, setLastSync] = useState<LastSync | null>(null)
  const [reports, setReports] = useState<Record<string, AuditReport | null>>({})
  const [enrichRun, setEnrichRun] = useState<EnrichmentLastRun | null>(null)
  const [autoRefresh, setAutoRefresh] = useState(true)
  const [lastRefresh, setLastRefresh] = useState<Date>(new Date())

  // ── Local Reinforcement State ──────────────────────────────────────────────
  const [localHealth, setLocalHealth] = useState<LocalHealth | null>(null)
  const [localJobs, setLocalJobs] = useState<Record<string, LocalJob>>({})
  const [assistingBot, setAssistingBot] = useState<Record<string, boolean>>({})
  const [assistAllActive, setAssistAllActive] = useState(false)
  const [showCapacity, setShowCapacity] = useState(false)
  const [showLocalLog, setShowLocalLog] = useState<string | null>(null)  // job_id

  const PAGE_SIZE = 50

  // ── Local Bot API Helpers ──────────────────────────────────────────────────

  async function localGet<T>(endpoint: string): Promise<T | null> {
    try {
      const r = await fetch(`/local-bots${endpoint}`, { cache: 'no-store' })
      if (!r.ok) return null
      return (await r.json()) as T
    } catch { return null }
  }

  async function localPost(endpoint: string, body: Record<string, unknown> = {}): Promise<Record<string, unknown> | null> {
    try {
      const r = await fetch(`/local-bots${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      })
      if (!r.ok) return null
      return (await r.json()) as Record<string, unknown>
    } catch { return null }
  }

  const pollLocalStatus = useCallback(async () => {
    const [health, jobs] = await Promise.all([
      localGet<LocalHealth>('/health'),
      localGet<Record<string, LocalJob>>('/bots/status'),
    ])
    if (health) setLocalHealth(health)
    if (jobs) setLocalJobs(jobs)
  }, [])

  async function assistBot(bot: typeof BOT_REPORTS[0]) {
    setAssistingBot(p => ({ ...p, [bot.key]: true }))
    const body: Record<string, unknown> = {}
    if (bot.defaultCount > 0) body.count = bot.defaultCount
    if (bot.localEndpoint === '/bots/enrich') body.model = bot.defaultModel
    const res = await localPost(bot.localEndpoint, body)
    if (res) await pollLocalStatus()
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

  const loadBotTelemetry = useCallback(async () => {
    const [b, ls, er, ...rs] = await Promise.all([
      fetchJSON<BudgetState>('/governance/budget.json'),
      fetchJSON<LastSync>('/governance/last_sync.json'),
      fetchJSON<EnrichmentLastRun>('/enrichment/last_run.json'),
      ...BOT_REPORTS.map(r => fetchJSON<AuditReport>(`/audit-reports/${r.file}`)),
    ])
    setBudget(b)
    setLastSync(ls)
    setEnrichRun(er)
    const next: Record<string, AuditReport | null> = {}
    BOT_REPORTS.forEach((r, i) => { next[r.key] = rs[i] })
    setReports(next)
    setLastRefresh(new Date())
  }, [])

  useEffect(() => { loadLogs() }, [page, filterEntity, filterEditor, filterAction])

  // Poll bot telemetry every 5s when auto-refresh is on
  useEffect(() => {
    loadBotTelemetry()
    if (!autoRefresh) return
    const id1 = setInterval(loadBotTelemetry, 5000)
    return () => clearInterval(id1)
  }, [autoRefresh, loadBotTelemetry])

  // Poll local bot server every 3s
  useEffect(() => {
    pollLocalStatus()
    const id = setInterval(pollLocalStatus, 3000)
    return () => clearInterval(id)
  }, [pollLocalStatus])

  // Appwrite Realtime subscription — new audit rows appear instantly (no polling reads)
  useEffect(() => {
    if (!autoRefresh) return
    const channel = `databases.${DATABASE_ID}.collections.${COLLECTIONS.AUDIT_LOG}.documents`
    const unsubscribe = client.subscribe(channel, (response) => {
      const isCreate = response.events.some((e: string) => e.endsWith('.create'))
      if (isCreate) {
        setLogs(prev => [mapToRow(response.payload as Models.Document), ...prev])
        setTotal(t => t + 1)
      }
    })
    return () => unsubscribe()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [autoRefresh])

  async function loadLogs() {
    setLoading(true)
    try {
      const queries: string[] = [
        Query.orderDesc('timestamp'),
        Query.limit(PAGE_SIZE),
        Query.offset(page * PAGE_SIZE),
      ]
      if (filterEntity) queries.push(Query.search('entitySlug', filterEntity))
      if (filterEditor) queries.push(Query.equal('editorId', filterEditor))
      if (filterAction) queries.push(Query.equal('action', filterAction))

      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.AUDIT_LOG, queries)
      setTotal(res.total)
      setLogs(res.documents.map(mapToRow))
    } catch (err) {
      console.error('Audit log load failed:', err)
      setLogs([])
      setTotal(0)
    }
    setLoading(false)
  }

  function mapToRow(doc: Models.Document): AuditRow {
    return {
      $id: doc.$id,
      entityId: (doc.entityId as string) ?? '',
      entitySlug: (doc.entitySlug as string) ?? '',
      entityName: (doc.entityName as string) ?? '',
      action: (doc.action as string) ?? '',
      field: (doc.field as string) ?? '',
      oldValue: (doc.oldValue as string) ?? '',
      newValue: (doc.newValue as string) ?? '',
      editorId: (doc.editorId as string) ?? '',
      editorNote: (doc.editorNote as string) ?? '',
      timestamp: (doc.timestamp as string) ?? '',
      sessionId: (doc.sessionId as string) ?? '',
    }
  }

  // Unique editors for filter dropdown
  const uniqueEditors = useMemo(
    () => [...new Set(logs.map(l => l.editorId).filter(Boolean))],
    [logs],
  )

  /** Export current filtered view as CSV */
  function exportCSV() {
    const headers = ['Timestamp', 'Entity', 'Action', 'Field', 'Old Value', 'New Value', 'Editor', 'Note']
    const rows = logs.map(l => [
      l.timestamp, l.entitySlug, l.action, l.field,
      `"${l.oldValue.replace(/"/g, '""')}"`,
      `"${l.newValue.replace(/"/g, '""')}"`,
      l.editorId, l.editorNote,
    ])
    const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n')
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `audit-log-${new Date().toISOString().slice(0, 10)}.csv`
    a.click()
    URL.revokeObjectURL(url)
  }

  const pageCount = Math.ceil(total / PAGE_SIZE)

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
          <History size={24} color="#D4AF37" />
        </Box>
        <Box flex={1}>
          <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
            EDIT AUDIT LOG
          </Text>
          <Text fontSize="sm" color="#787469">
            {total.toLocaleString()} audit entries — full history of all curator edits
          </Text>
        </Box>
        <Box
          as="button" onClick={exportCSV}
          px={3} py={2} borderRadius="md" bg="#F5F4F0" border="1px solid #E4E2DC"
          cursor="pointer" display="flex" alignItems="center" gap={2}
          _hover={{ bg: '#E4E2DC' }}
        >
          <Download size={14} color="#787469" />
          <Text fontSize="xs" fontWeight={600} color="#787469">Export CSV</Text>
        </Box>
      </Flex>

      {/* ── LIVE BOT ACTIVITY PANEL ───────────────────────────────────── */}
      <Box mb={6} p={4} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg">
        <Flex align="center" gap={2} mb={3}>
          <Activity size={16} color={autoRefresh ? '#27AE60' : '#9E9A90'} />
          <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
            color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
            Live Bot Activity
          </Text>
          <Box w="6px" h="6px" borderRadius="full" bg={autoRefresh ? '#27AE60' : '#9E9A90'}
            animation={autoRefresh ? 'pulse 1.6s ease-in-out infinite' : undefined} />
          <Text fontSize="xs" color="#9E9A90" ml={1}>
            updated {relTime(lastRefresh.toISOString())} · polling every 5s
          </Text>
          <Box flex={1} />
          <Box as="button" onClick={() => setAutoRefresh(v => !v)}
            px={2} py={1} fontSize="11px" fontWeight={600} borderRadius="md"
            bg={autoRefresh ? '#27AE6020' : '#F5F4F0'}
            color={autoRefresh ? '#27AE60' : '#787469'}
            border="1px solid #E4E2DC" cursor="pointer"
            title={autoRefresh ? 'Pause live dashboard updates (bots continue running in cloud)' : 'Resume live dashboard updates'}>
            {autoRefresh ? 'PAUSE' : 'RESUME'}
          </Box>
        </Flex>

        {/* Top row: budget, last sync, enrichment */}
        <SimpleGrid columns={{ base: 1, md: 3 }} gap={3} mb={3}>
          {/* Budget card */}
          <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
            <Flex align="center" gap={2} mb={2}>
              {budget?.manualPause ? <Pause size={14} color="#C0392B" /> :
                <CheckCircle2 size={14} color="#27AE60" />}
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

          {/* Last sync card */}
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

          {/* Enrichment card */}
          <Box p={3} bg="white" border="1px solid #E4E2DC" borderRadius="md">
            <Flex align="center" gap={2} mb={2}>
              <Activity size={14} color="#D4AF37" />
              <Text fontSize="11px" fontWeight={700} color="#787469"
                letterSpacing="0.06em" textTransform="uppercase">
                AI Enrichment
              </Text>
              <Box ml="auto" px={2} py={0.5} fontSize="9px" fontWeight={700}
                bg="#D4AF3720" color="#D4AF37" borderRadius="md">
                {enrichRun?.model?.toUpperCase() ?? 'IDLE'}
              </Box>
            </Flex>
            <Text fontSize="13px" fontWeight={600} color="#2D2A24">
              {enrichRun
                ? `${enrichRun.succeeded ?? 0} ok · ${enrichRun.rejected ?? 0} rej · ${enrichRun.failed ?? 0} fail`
                : 'never run'}
            </Text>
            <Text mt={1} fontSize="10px" color="#9E9A90">
              {enrichRun?.attempted
                ? `${enrichRun.attempted} attempted · ${relTime(enrichRun.generatedAt)}`
                : 'awaiting run'}
            </Text>
          </Box>
        </SimpleGrid>

        {/* Bot reports grid — with per-bot Assist button */}
        <SimpleGrid columns={{ base: 2, md: 3, lg: 4 }} gap={3}>
          {BOT_REPORTS.map(b => {
            const r = reports[b.key]
            const summary = (r?.summary ?? {}) as Record<string, number | string>
            const headline = Object.entries(summary)[0]
            const isAssisting = assistingBot[b.key]
            const activeJob = Object.values(localJobs).find(
              j => j.bot === b.localEndpoint.replace('/bots/', '') && j.status === 'running'
            )
            return (
              <Box key={b.key} p={3} bg="white" border="1px solid #E4E2DC"
                borderLeft={`3px solid ${b.color}`} borderRadius="md"
                position="relative">
                <Flex align="center" justify="space-between" mb={1}>
                  <Text fontSize="10px" fontWeight={700} color="#787469"
                    letterSpacing="0.06em" textTransform="uppercase">
                    {b.label}
                  </Text>
                  {/* Cloud status badge */}
                  {r && (
                    <Box px={1.5} py={0.5} fontSize="8px" fontWeight={700}
                      bg="#4A90D920" color="#4A90D9" borderRadius="sm">
                      CLOUD
                    </Box>
                  )}
                </Flex>
                {r ? (
                  <>
                    <Text mt={1} fontSize="16px" fontWeight={700} color="#2D2A24"
                      fontFamily='"Cormorant Garamond", serif'>
                      {headline ? String(headline[1]) : 'ok'}
                    </Text>
                    <Text fontSize="10px" color="#9E9A90">
                      {headline ? headline[0].replace(/_/g, ' ') : ''}
                    </Text>
                    <Flex align="center" gap={1} mt={1}>
                      <Clock size={9} color="#9E9A90" />
                      <Text fontSize="9px" color="#9E9A90">
                        {relTime(r.generatedAt)}
                      </Text>
                    </Flex>
                  </>
                ) : (
                  <Flex align="center" gap={1} mt={1}>
                    <AlertTriangle size={11} color="#9E9A90" />
                    <Text fontSize="11px" color="#9E9A90">no report</Text>
                  </Flex>
                )}

                {/* ⚔ Assist button — send local reinforcement to this bot */}
                <Box
                  as="button"
                  onClick={() => !isAssisting && assistBot(b)}
                  mt={2}
                  w="100%"
                  px={2} py={1}
                  borderRadius="sm"
                  fontSize="9px"
                  fontWeight={700}
                  letterSpacing="0.05em"
                  border="1px solid"
                  cursor={localHealth?.ollama.running ? 'pointer' : 'not-allowed'}
                  bg={activeJob ? '#E67E2220'
                    : localHealth?.ollama.running ? `${b.color}18` : '#F5F4F0'}
                  borderColor={activeJob ? '#E67E22'
                    : localHealth?.ollama.running ? b.color : '#E4E2DC'}
                  color={activeJob ? '#E67E22'
                    : localHealth?.ollama.running ? b.color : '#9E9A90'}
                  display="flex" alignItems="center" justifyContent="center" gap={1}
                  title={localHealth?.ollama.running
                    ? `Deploy local ${b.defaultModel} to assist ${b.label}`
                    : 'Start local_bot_server.py to enable local bots'}
                >
                  {isAssisting ? (
                    <><Spinner size="xs" /><span>DEPLOYING…</span></>
                  ) : activeJob ? (
                    <><Zap size={9} /><span>RUNNING LOCAL</span></>
                  ) : (
                    <><Swords size={9} /><span>⚔ ASSIST</span></>
                  )}
                </Box>
                <Text fontSize="8px" color="#9E9A90" mt={1} lineHeight="1.3">
                  {b.description}
                </Text>
              </Box>
            )
          })}
        </SimpleGrid>
      </Box>

      {/* ── LOCAL REINFORCEMENT COMMAND POST ─────────────────────────────── */}
      <Box mb={6} p={4} borderRadius="lg"
        bg={localHealth?.ollama.running ? '#FAF3E8' : '#F5F4F0'}
        border={`1px solid ${localHealth?.ollama.running ? '#C5963A40' : '#E4E2DC'}`}>

        {/* Header bar */}
        <Flex align="center" gap={2} mb={3} flexWrap="wrap">
          <Box p={1.5} borderRadius="md" bg="#C5963A15">
            <Cpu size={16} color="#C5963A" />
          </Box>
          <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
            color="#2D2A24" letterSpacing="0.1em" textTransform="uppercase">
            Local Reinforcement — Command Post
          </Text>
          {/* Ollama status pill */}
          <Box px={2} py={0.5} borderRadius="full" fontSize="9px" fontWeight={700}
            bg={localHealth?.ollama.running ? '#27AE6015' : '#C0392B15'}
            border={`1px solid ${localHealth?.ollama.running ? '#27AE6040' : '#C0392B40'}`}
            color={localHealth?.ollama.running ? '#27AE60' : '#C0392B'}>
            {localHealth?.ollama.running
              ? `OLLAMA ONLINE · ${localHealth.ollama.models?.length ?? 0} model(s)`
              : 'OLLAMA OFFLINE'}
          </Box>
          {/* Safety badge — always local only */}
          <Box px={2} py={0.5} borderRadius="full" fontSize="9px" fontWeight={700}
            bg="#27AE6015" border="1px solid #27AE6040" color="#27AE60">
            LOCAL ONLY · £0 · NO CLOUD
          </Box>
          {/* Active jobs count */}
          {(localHealth?.activeJobs ?? 0) > 0 && (
            <Box px={2} py={0.5} borderRadius="full" fontSize="9px" fontWeight={700}
              bg="#E67E2215" border="1px solid #E67E2240" color="#E67E22">
              {localHealth!.activeJobs} BOT(S) ACTIVE
            </Box>
          )}
          <Box flex={1} />
          {/* Ollama Monitor link */}
          <Box as="button" onClick={() => navigate('/curator/ollama')}
            px={3} py={1.5} borderRadius="md" fontSize="10px" fontWeight={700}
            bg="#C5963A15" border="1px solid #C5963A40" color="#C5963A"
            cursor="pointer" display="flex" alignItems="center" gap={1}>
            <Cpu size={11} />
            OLLAMA MONITOR ↗
          </Box>
          {/* Capacity table toggle */}
          <Box as="button" onClick={() => setShowCapacity(v => !v)}
            px={3} py={1.5} borderRadius="md" fontSize="10px" fontWeight={700}
            bg="#4A90D915" border="1px solid #4A90D940" color="#4A90D9"
            cursor="pointer" display="flex" alignItems="center" gap={1}>
            <Server size={11} />
            {showCapacity ? 'HIDE CAPACITY' : 'CAPACITY PLAN'}
          </Box>
        </Flex>

        {/* Offline warning */}
        {!localHealth?.ollama.running && (
          <Box mb={3} p={3} bg="#FEF9E7" border="1px solid #F1C40F40" borderRadius="md">
            <Flex align="center" gap={2}>
              <CloudOff size={14} color="#E67E22" />
              <Text fontSize="11px" color="#2D2A24" fontWeight={600}>
                Local bot server is offline. Start it with:
              </Text>
            </Flex>
            <Text mt={1} fontSize="11px" fontFamily='"JetBrains Mono", monospace'
              color="#C5963A" bg="#2D2A24" px={2} py={1} borderRadius="sm">
              python3 scripts/local_bot_server.py
            </Text>
          </Box>
        )}

        {/* Command buttons */}
        <Flex gap={3} mb={4} flexWrap="wrap" align="center">
          {/* ⚔ ASSIST ALL — the General's order */}
          <Box
            as="button"
            onClick={() => !assistAllActive && localHealth?.ollama.running && assistAll()}
            px={4} py={2.5}
            borderRadius="md"
            fontSize="12px"
            fontWeight={700}
            letterSpacing="0.08em"
            cursor={localHealth?.ollama.running ? 'pointer' : 'not-allowed'}
            bg={localHealth?.ollama.running
              ? assistAllActive ? '#E67E22' : '#C5963A'
              : '#E4E2DC'}
            color={localHealth?.ollama.running ? 'white' : '#9E9A90'}
            display="flex" alignItems="center" gap={2}
            title="Deploy ALL local bots concurrently — like a general sending reinforcements to every front"
          >
            {assistAllActive
              ? <><Spinner size="xs" /><span>DEPLOYING ALL BOTS…</span></>
              : <><Swords size={14} /><span>⚔ ASSIST ALL</span></>}
          </Box>

          {/* Stop all */}
          <Box
            as="button"
            onClick={stopAllBots}
            px={3} py={2.5}
            borderRadius="md"
            fontSize="11px"
            fontWeight={700}
            letterSpacing="0.06em"
            cursor="pointer"
            bg="#C0392B10" border="1px solid #C0392B30" color="#C0392B"
            display="flex" alignItems="center" gap={2}
          >
            <StopCircle size={13} /><span>STOP ALL</span>
          </Box>

          {/* Refresh status */}
          <Box
            as="button"
            onClick={pollLocalStatus}
            px={3} py={2.5}
            borderRadius="md"
            fontSize="11px"
            fontWeight={700}
            cursor="pointer"
            bg="#F5F4F0" border="1px solid #E4E2DC" color="#787469"
            display="flex" alignItems="center" gap={2}
          >
            <RefreshCw size={13} /><span>REFRESH</span>
          </Box>

          {/* Model indicators */}
          <Flex gap={2} ml="auto" flexWrap="wrap">
            {localHealth?.ollama.models?.map(m => (
              <Box key={m} px={2} py={1} borderRadius="sm" fontSize="9px" fontWeight={700}
                bg="#27AE6015" border="1px solid #27AE6030" color="#27AE60">
                {m}
              </Box>
            ))}
          </Flex>
        </Flex>

        {/* Running jobs list */}
        {Object.keys(localJobs).length > 0 && (
          <Box mb={4}>
            <Text fontSize="10px" fontWeight={700} color="#787469" mb={2}
              letterSpacing="0.08em" textTransform="uppercase">
              Active & Recent Jobs
            </Text>
            <Flex gap={2} flexWrap="wrap">
              {Object.values(localJobs)
                .sort((a, b) => b.started.localeCompare(a.started))
                .slice(0, 12)
                .map(job => (
                  <Box
                    key={job.job_id}
                    as="button"
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
                    }`}
                  >
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
                    {/* Inline log viewer */}
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

        {/* ── Capacity Planning Table ────────────────────────────────────── */}
        {showCapacity && (
          <Box mt={2}>
            <Flex align="center" gap={2} mb={3}>
              <Server size={14} color="#C5963A" />
              <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
                color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
                Monthly Capacity — Cloud + Local at Max Limits
              </Text>
            </Flex>

            <Box overflowX="auto" mb={3}>
              <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '820px' }}>
                <thead>
                  <tr>
                    {['Source', 'Tier', 'Model(s)', 'Rate', 'Monthly Capacity', 'Best For', 'Notes'].map(h => (
                      <th key={h} style={{
                        padding: '8px 10px', textAlign: 'left', fontSize: '9px',
                        fontWeight: 700, color: '#787469', borderBottom: '1px solid #E4E2DC',
                        fontFamily: '"Cinzel", serif', textTransform: 'uppercase',
                        letterSpacing: '0.08em', whiteSpace: 'nowrap',
                        backgroundColor: '#F5F4F0',
                      }}>{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {CAPACITY_TABLE.map((row, i) => (
                    <tr key={i} style={{ backgroundColor: i % 2 === 0 ? 'white' : '#FAFAF8' }}>
                      <td style={capTd}>
                        <Flex align="center" gap={1.5}>
                          <Box w="8px" h="8px" borderRadius="full" bg={row.color} flexShrink={0} />
                          <Text fontSize="11px" fontWeight={700} color="#2D2A24">{row.source}</Text>
                        </Flex>
                      </td>
                      <td style={capTd}>
                        <Text fontSize="10px" color="#787469">{row.tier}</Text>
                      </td>
                      <td style={capTd}>
                        <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace'
                          color="#4A90D9">{row.models}</Text>
                      </td>
                      <td style={capTd}>
                        <Text fontSize="10px" color="#C5963A" fontWeight={600}>{row.rate}</Text>
                      </td>
                      <td style={capTd}>
                        <Flex align="center" gap={2}>
                          <Text fontSize="12px" fontWeight={700} color={row.color}
                            fontFamily='"Cormorant Garamond", serif'>
                            {row.monthly.toLocaleString()}
                          </Text>
                          <Text fontSize="9px" color="#9E9A90">{row.unit}</Text>
                        </Flex>
                        {/* Mini bar */}
                        <Box mt={1} h="3px" bg="#E4E2DC" borderRadius="full" overflow="hidden">
                          <Box h="100%" borderRadius="full" bg={row.color}
                            w={`${Math.min(100, (row.monthly / 48_000) * 100)}%`} />
                        </Box>
                      </td>
                      <td style={capTd}>
                        <Text fontSize="10px" color="#524E44">{row.bestFor}</Text>
                      </td>
                      <td style={capTd}>
                        <Text fontSize="9px" color="#9E9A90" lineHeight="1.5">{row.notes}</Text>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </Box>

            {/* Summary totals */}
            <SimpleGrid columns={{ base: 1, md: 3 }} gap={3}>
              <Box p={3} bg="white" border="1px solid #4A90D930" borderRadius="md">
                <Text fontSize="9px" color="#787469" mb={1}
                  fontFamily='"Cinzel", serif' textTransform="uppercase" letterSpacing="0.08em">
                  Cloud Only (max)
                </Text>
                <Text fontSize="22px" fontWeight={700} color="#4A90D9"
                  fontFamily='"Cormorant Garamond", serif'>
                  {TOTAL_CLOUD_MONTHLY.toLocaleString()}
                </Text>
                <Text fontSize="10px" color="#9E9A90">entities/month</Text>
                <Text fontSize="9px" color="#787469" mt={1}>
                  Gemini 15k + Copilot 1.5k + GPT-4o-mini 5k
                </Text>
              </Box>
              <Box p={3} bg="white" border="1px solid #27AE6030" borderRadius="md">
                <Text fontSize="9px" color="#787469" mb={1}
                  fontFamily='"Cinzel", serif' textTransform="uppercase" letterSpacing="0.08em">
                  Local (CPU, 8h/day)
                </Text>
                <Text fontSize="22px" fontWeight={700} color="#27AE60"
                  fontFamily='"Cormorant Garamond", serif'>
                  {TOTAL_LOCAL_CPU_MONTHLY.toLocaleString()}
                </Text>
                <Text fontSize="10px" color="#9E9A90">entities/month</Text>
                <Text fontSize="9px" color="#787469" mt={1}>
                  Ollama llama3.2:3b · ~20/hr · free & unlimited
                </Text>
              </Box>
              <Box p={3} bg="white" border="1px solid #C5963A30" borderRadius="md">
                <Text fontSize="9px" color="#787469" mb={1}
                  fontFamily='"Cinzel", serif' textTransform="uppercase" letterSpacing="0.08em">
                  Combined Total
                </Text>
                <Text fontSize="22px" fontWeight={700} color="#C5963A"
                  fontFamily='"Cormorant Garamond", serif'>
                  {TOTAL_COMBINED_MONTHLY.toLocaleString()}+
                </Text>
                <Text fontSize="10px" color="#9E9A90">entities/month</Text>
                <Text fontSize="9px" color="#787469" mt={1}>
                  At current 40k catalog: full enrichment in ~2 months
                </Text>
              </Box>
            </SimpleGrid>

            <Box mt={3} p={3} bg="#FAF3E8" border="1px solid #E8D5B040" borderRadius="md">
              <Text fontSize="10px" fontWeight={700} color="#C5963A" mb={1}>
                General's Strategy
              </Text>
              <Text fontSize="11px" color="#524E44" lineHeight="1.8">
                • <strong style={{color:'#C5963A'}}>High-significance entities (score 8–10)</strong> → Copilot Sonnet 4.6 (1,500/mo) — maximum quality for world-changing nodes<br />
                • <strong style={{color:'#4A90D9'}}>Bulk enrichment (score &lt;8)</strong> → Gemini 2.5 Flash (15,000/mo) — free, fast, good quality<br />
                • <strong style={{color:'#10A37F'}}>Overflow / fallback</strong> → GPT-4o-mini when Gemini hits daily quota<br />
                • <strong style={{color:'#27AE60'}}>Local overnight runs</strong> → Ollama llama3.2:3b — zero cost, no quotas; run 8h/day for +4,800/mo<br />
                • <strong style={{color:'#E67E22'}}>Significance &amp; queue scans</strong> → Ollama preferred (short tasks, structured JSON, perfect fit for 3b)
              </Text>
            </Box>
          </Box>
        )}
      </Box>

      {/* Quick Stats */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
        <StatCard value={total.toLocaleString()} label="Total Entries" color="#4A90D9" />
        <StatCard
          value={logs.filter(l => l.action === 'update').length.toString()}
          label="Updates (page)" color="#E67E22"
        />
        <StatCard
          value={uniqueEditors.length.toString()}
          label="Active Editors" color="#27AE60"
        />
        <StatCard
          value={logs.length > 0 ? new Date(logs[0].timestamp).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }) : '—'}
          label="Latest Edit" color="#6B3FA0"
        />
      </SimpleGrid>

      {/* Filters */}
      <Flex gap={3} mb={4} flexWrap="wrap">
        <Flex align="center" gap={2} flex={1} minW="200px">
          <Filter size={14} color="#787469" />
          <Input
            value={filterEntity} onChange={(e) => { setFilterEntity(e.target.value); setPage(0) }}
            placeholder="Search entity slug…" size="sm"
            bg="white" borderColor="#E4E2DC" _focus={{ borderColor: '#D4AF37' }}
          />
        </Flex>
        <Flex align="center" gap={2} minW="150px">
          <User size={14} color="#787469" />
          <Input
            value={filterEditor} onChange={(e) => { setFilterEditor(e.target.value); setPage(0) }}
            placeholder="Editor…" size="sm"
            bg="white" borderColor="#E4E2DC" _focus={{ borderColor: '#D4AF37' }}
          />
        </Flex>
        <Flex align="center" gap={2} minW="140px">
          <FileText size={14} color="#787469" />
          <select
            value={filterAction}
            onChange={(e) => { setFilterAction(e.target.value); setPage(0) }}
            style={{
              padding: '4px 8px', fontSize: '13px', fontFamily: '"Inter", sans-serif',
              border: '1px solid #E4E2DC', borderRadius: '6px', background: 'white',
            }}
          >
            <option value="">All actions</option>
            <option value="update">Update</option>
            <option value="delete">Delete</option>
            <option value="create">Create</option>
            <option value="batch_update">Batch Update</option>
          </select>
        </Flex>
      </Flex>

      {/* Table */}
      {loading ? (
        <Flex justify="center" py={12}>
          <Spinner size="lg" color="#D4AF37" />
        </Flex>
      ) : logs.length === 0 ? (
        <Box bg="#FEF9E7" border="1px solid #F1C40F" borderRadius="lg" p={8} textAlign="center">
          <History size={36} color="#D4AF37" />
          <Text mt={3} fontSize="lg" fontWeight={600} color="#2D2A24">No audit entries yet</Text>
          <Text fontSize="sm" color="#787469" mt={1}>
            Edit an entity in the curator to start recording audit history.
          </Text>
        </Box>
      ) : (
        <>
          <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto">
            <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '1000px' }}>
              <thead>
                <tr>
                  <th style={thStyle}>Timestamp</th>
                  <th style={thStyle}>Entity</th>
                  <th style={thStyle}>Action</th>
                  <th style={thStyle}>Field</th>
                  <th style={thStyle}>Old Value</th>
                  <th style={thStyle}>New Value</th>
                  <th style={thStyle}>Editor</th>
                </tr>
              </thead>
              <tbody>
                {logs.map((row, ri) => (
                  <tr key={row.$id} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                    <td style={tdStyle}>
                      <Text fontSize="xs" fontFamily='"JetBrains Mono", monospace' color="#787469">
                        {new Date(row.timestamp).toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit', second: '2-digit' })}
                      </Text>
                    </td>
                    <td style={{ ...tdStyle, maxWidth: '180px', overflow: 'hidden' }}>
                      <Text fontSize="xs" fontWeight={600} color="#4A90D9" cursor="pointer"
                        overflow="hidden" textOverflow="ellipsis" whiteSpace="nowrap"
                        title={row.entityName || row.entitySlug}
                        onClick={() => navigate(`/entity/${row.entitySlug}`)}>  
                        {row.entityName || row.entitySlug}
                      </Text>
                    </td>
                    <td style={tdStyle}>
                      <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="10px" fontWeight={700}
                        bg={`${ACTION_COLORS[row.action] ?? '#9E9A90'}20`}
                        color={ACTION_COLORS[row.action] ?? '#9E9A90'}>
                        {row.action.toUpperCase()}
                      </Box>
                    </td>
                    <td style={tdStyle}>
                      <Text fontSize="xs" fontFamily='"JetBrains Mono", monospace' color="#524E44">
                        {row.field}
                      </Text>
                    </td>
                    <td style={{ ...tdStyle, maxWidth: '200px' }}>
                      <Text fontSize="xs" color="#922B21" lineClamp={2} title={row.oldValue}>
                        {row.oldValue || '—'}
                      </Text>
                    </td>
                    <td style={{ ...tdStyle, maxWidth: '200px' }}>
                      <Text fontSize="xs" color="#196F3D" lineClamp={2} title={row.newValue}>
                        {row.newValue || '—'}
                      </Text>
                    </td>
                    <td style={tdStyle}>
                      <EditorBadge editorId={row.editorId} />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Box>

          {/* Pagination */}
          {pageCount > 1 && (
            <Flex justify="center" gap={2} mt={4}>
              {Array.from({ length: Math.min(pageCount, 10) }, (_, i) => (
                <Box
                  key={i} as="button" onClick={() => setPage(i)}
                  px={3} py={1.5} borderRadius="md" fontSize="sm"
                  fontWeight={page === i ? 700 : 400}
                  bg={page === i ? '#2D2A24' : '#F5F4F0'}
                  color={page === i ? '#D4AF37' : '#787469'}
                  cursor="pointer"
                >
                  {i + 1}
                </Box>
              ))}
              {pageCount > 10 && <Text color="#9E9A90" alignSelf="center">…{pageCount}</Text>}
            </Flex>
          )}
        </>
      )}
    </Box>
  )
}

/* ─── Styles ─── */

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

const capTd: React.CSSProperties = {
  padding: '8px 10px',
  fontSize: '11px',
  color: '#B8C9D9',
  borderBottom: '1px solid #1A2A3A',
  fontFamily: '"Inter", sans-serif',
  verticalAlign: 'top',
}
