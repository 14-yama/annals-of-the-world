import React, { useEffect, useState, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, Cpu, Activity, CheckCircle2, AlertTriangle, Clock,
  Swords, StopCircle, RefreshCw, Zap, BookOpen, Brain, GitBranch,
  List, BarChart3, Server, Upload, Cloud, GitCommit, ExternalLink,
  PlayCircle, XCircle, MinusCircle,
} from 'lucide-react'

/* ─── Types ─────────────────────────────────────────────────────────────── */

interface OllamaModel {
  name: string
  size?: number
  digest?: string
  details?: { family?: string; parameter_size?: string; quantization_level?: string }
}

interface OllamaPsModel {
  name: string
  size?: number
  size_vram?: number
  expires_at?: string
  details?: { family?: string; parameter_size?: string }
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

interface SprintStats {
  // New rich structure
  windows?: {
    last_24h: WindowStats
    last_7d: WindowStats
    last_30d: WindowStats
  }
  byDay?: Record<string, Record<string, number>>
  topPerformers?: Array<{ bot: string; total: number }>
  activeEditors?: Array<{ editorId: string; bot: string; status: string; since: string; env: string }>
  // Legacy compat
  window: string
  totalEntitiesProcessed: number
  byBot: Record<string, number>
  completedJobs: number
}

interface WindowStats {
  totalEntities: number
  byBot: Record<string, number>
  byAction: Record<string, number>
  completedJobs: number
  failedJobs: number
}

interface GitPending {
  total: number
  entities: number
  edges: number
  hasPending: boolean
}

interface GHRun {
  name: string
  status: string        // queued | in_progress | completed
  conclusion: string | null  // success | failure | cancelled | null
  runId: number
  startedAt: string | null
  updatedAt: string | null
  htmlUrl: string
  triggeredBy: string
  error?: string
}

/* ─── What Ollama does for this project ─────────────────────────────────── */

const OLLAMA_TASKS = [
  {
    icon: BookOpen,
    color: '#27AE60',
    title: 'Entity Enrichment',
    script: 'ai_enrich_autonomous.py --model ollama',
    description: 'Generates full scholarly summaries (800–2,000 chars), 3 causes, 3 effects, 5 relationships, 3 places, 8–10 subjects, 3 interpretive frameworks per entity. Targets stubs and low-quality entries.',
    volume: '~20 entities/hr (CPU) · ~200/hr (GPU)',
    quality: 'Good — llama3.2:3b handles structured JSON well; high-significance entities benefit from Gemini/Claude',
    cost: '£0 — unlimited local inference',
  },
  {
    icon: BarChart3,
    color: '#8E44AD',
    title: 'Significance Backfill',
    script: 'backfill_significance.py --model ollama',
    description: 'Rates every enriched entity (summary ≥600c) with a significanceScore (1–10), significanceNarrative (1–2 sentences), and significanceCategory (world-changing/continental/regional/local). Short structured task — ideal for small models.',
    volume: '~60 entities/hr (CPU) · ~400/hr (GPU)',
    quality: 'Excellent — short structured output, high accuracy even at 3b scale',
    cost: '£0 — unlimited local inference',
  },
  {
    icon: GitBranch,
    color: '#E67E22',
    title: 'Queue Scanning',
    script: 'enrichment_queue.py',
    description: 'Scans all 40,000+ entities, scores weakness (summary length, missing fields, stub patterns, edge gaps), and outputs a priority-sorted queue. No LLM needed — pure Python scoring logic.',
    volume: 'Full scan in ~2 min (no LLM)',
    quality: 'Perfect — deterministic ranking',
    cost: '£0 — no model calls',
  },
  {
    icon: Brain,
    color: '#4A90D9',
    title: 'What Else Ollama Could Do',
    script: '(planned expansions)',
    description: 'Future tasks: relationship extraction from Wikipedia text, place geocoding from entity context, era/division classification for newly imported nodes, generating sub-headings for long summaries, deduplication fuzzy matching at scale.',
    volume: 'Unlimited — schedule overnight',
    quality: 'Varies by task complexity; 8b model recommended for extraction',
    cost: '£0 — run 24/7 on local hardware',
  },
]

/* ─── Helpers ────────────────────────────────────────────────────────────── */

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
    return r.ok ? (await r.json()) as Record<string, unknown> : null
  } catch { return null }
}

function fmtBytes(b?: number): string {
  if (!b) return '—'
  if (b < 1e6) return `${(b / 1e3).toFixed(1)} KB`
  if (b < 1e9) return `${(b / 1e6).toFixed(0)} MB`
  return `${(b / 1e9).toFixed(1)} GB`
}

function relTime(iso?: string | null): string {
  if (!iso) return 'never'
  const s = Math.max(0, (Date.now() - new Date(iso).getTime()) / 1000)
  if (s < 60) return `${Math.floor(s)}s ago`
  if (s < 3600) return `${Math.floor(s / 60)}m ago`
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`
  return `${Math.floor(s / 86400)}d ago`
}

const STATUS_COLOR: Record<string, string> = {
  running: '#E67E22',
  done: '#27AE60',
  error: '#C0392B',
  queued: '#4A90D9',
  stopped: '#9E9A90',
}

/* ─── Component ─────────────────────────────────────────────────────────── */

export default function OllamaMonitor() {
  const navigate = useNavigate()

  const [serverOnline, setServerOnline] = useState<boolean | null>(null)
  const [models, setModels] = useState<OllamaModel[]>([])
  const [ps, setPs] = useState<OllamaPsModel[]>([])
  const [jobs, setJobs] = useState<LocalJob[]>([])
  const [sprint, setSprint] = useState<SprintStats | null>(null)
  const [pending, setPending] = useState<GitPending | null>(null)
  const [ghRuns, setGhRuns] = useState<GHRun[]>([])
  const [openLog, setOpenLog] = useState<string | null>(null)
  const [launching, setLaunching] = useState<string | null>(null)
  const [lastPoll, setLastPoll] = useState<Date>(new Date())
  const [historyOpen, setHistoryOpen] = useState(false)
  const [statsWindow, setStatsWindow] = useState<'last_24h' | 'last_7d' | 'last_30d'>('last_24h')

  const poll = useCallback(async () => {
    const [health, ps, allJobs, stats, gitPending, ghStatus] = await Promise.all([
      localGet<{ ollama: { running: boolean; models: OllamaModel[] } }>('/health'),
      localGet<{ models: OllamaPsModel[] }>('/ollama/ps'),
      localGet<Record<string, LocalJob>>('/bots/status'),
      localGet<SprintStats>('/stats'),
      localGet<GitPending>('/git/pending'),
      localGet<{ runs: GHRun[] }>('/github/status'),
    ])

    if (health) {
      setServerOnline(health.ollama.running)
      setModels(health.ollama.models as OllamaModel[] ?? [])
    } else {
      setServerOnline(false)
    }

    setPs(ps?.models ?? [])

    if (allJobs) {
      setJobs(
        Object.values(allJobs).sort((a, b) => b.started.localeCompare(a.started))
      )
    }

    if (stats) setSprint(stats)
    if (gitPending) setPending(gitPending)
    if (ghStatus?.runs) setGhRuns(ghStatus.runs.filter(r => !r.error))
    setLastPoll(new Date())
  }, [])

  useEffect(() => {
    poll()
    const id = setInterval(poll, 3000)
    return () => clearInterval(id)
  }, [poll])

  async function launch(endpoint: string, body: Record<string, unknown> = {}, label: string) {
    setLaunching(label)
    await localPost(endpoint, body)
    await poll()
    setLaunching(null)
  }

  const activeJobs = jobs.filter(j => j.status === 'running')
  const recentJobs = jobs.slice(0, 20)

  return (
    <Box maxW="1300px" mx="auto" p={6}>

      {/* Header */}
      <Flex align="center" gap={3} mb={6}>
        <Box as="button" onClick={() => navigate('/curator/audit')}
          p={2} borderRadius="md" bg="#F5F4F0" cursor="pointer" _hover={{ bg: '#E4E2DC' }}>
          <ChevronLeft size={18} color="#787469" />
        </Box>
        <Box p={2} borderRadius="md" bg="#27AE6015">
          <Cpu size={24} color="#27AE60" />
        </Box>
        <Box flex={1}>
          <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
            OLLAMA MONITOR
          </Text>
          <Text fontSize="sm" color="#787469">
            Local AI Engine — unlimited inference, zero cost, 24/7 sprint
          </Text>
        </Box>
        {/* Live pulse */}
        <Flex align="center" gap={2} px={3} py={1.5} borderRadius="md"
          bg={serverOnline ? '#27AE6012' : '#C0392B12'}
          border={`1px solid ${serverOnline ? '#27AE6040' : '#C0392B40'}`}>
          <Box w="7px" h="7px" borderRadius="full"
            bg={serverOnline ? '#27AE60' : '#C0392B'}
            style={{ animation: serverOnline ? 'pulse 1.6s ease-in-out infinite' : undefined }} />
          <Text fontSize="11px" fontWeight={700}
            color={serverOnline ? '#27AE60' : '#C0392B'}>
            {serverOnline ? 'OLLAMA ONLINE' : 'OLLAMA OFFLINE'}
          </Text>
        </Flex>
        <Box as="button" onClick={poll}
          p={2} borderRadius="md" bg="#F5F4F0" cursor="pointer" _hover={{ bg: '#E4E2DC' }}
          title="Refresh now">
          <RefreshCw size={15} color="#787469" />
        </Box>
        <Text fontSize="10px" color="#9E9A90">
          updated {relTime(lastPoll.toISOString())}
        </Text>
      </Flex>

      {/* Offline warning */}
      {serverOnline === false && (
        <Box mb={6} p={4} bg="#FEF9E7" border="1px solid #F1C40F" borderRadius="lg">
          <Flex align="center" gap={2} mb={2}>
            <AlertTriangle size={16} color="#E67E22" />
            <Text fontWeight={700} color="#2D2A24">Local bot server is not running</Text>
          </Flex>
          <Text fontSize="sm" color="#787469" mb={2}>
            Start both the Ollama engine and the local bot server:
          </Text>
          <Box p={3} bg="#2D2A24" borderRadius="md">
            <Text fontSize="12px" fontFamily='"JetBrains Mono", monospace' color="#D4AF37">
              # Terminal 1 — start Ollama<br />
              ollama serve<br /><br />
              # Terminal 2 — start bot server<br />
              python3 scripts/local_bot_server.py
            </Text>
          </Box>
        </Box>
      )}

      {/* Top stats */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
        <Box p={4} bg="white" border="1px solid #E4E2DC" borderRadius="lg"
          borderLeft="3px solid #27AE60">
          <Text fontSize="10px" fontWeight={700} color="#787469" mb={1}
            letterSpacing="0.06em" textTransform="uppercase">Active Inferences</Text>
          <Text fontSize="28px" fontWeight={700} color="#27AE60"
            fontFamily='"Cormorant Garamond", serif'>{ps.length}</Text>
          <Text fontSize="10px" color="#9E9A90">models loaded in VRAM/RAM</Text>
        </Box>
        <Box p={4} bg="white" border="1px solid #E4E2DC" borderRadius="lg"
          borderLeft="3px solid #E67E22">
          <Text fontSize="10px" fontWeight={700} color="#787469" mb={1}
            letterSpacing="0.06em" textTransform="uppercase">Running Jobs</Text>
          <Text fontSize="28px" fontWeight={700} color="#E67E22"
            fontFamily='"Cormorant Garamond", serif'>{activeJobs.length}</Text>
          <Text fontSize="10px" color="#9E9A90">bots currently processing</Text>
        </Box>
        <Box p={4} bg="white" border="1px solid #E4E2DC" borderRadius="lg"
          borderLeft="3px solid #4A90D9">
          <Text fontSize="10px" fontWeight={700} color="#787469" mb={1}
            letterSpacing="0.06em" textTransform="uppercase">24h Sprint</Text>
          <Text fontSize="28px" fontWeight={700} color="#4A90D9"
            fontFamily='"Cormorant Garamond", serif'>
            {(sprint?.totalEntitiesProcessed ?? 0).toLocaleString()}
          </Text>
          <Text fontSize="10px" color="#9E9A90">entities processed today</Text>
        </Box>
        <Box p={4} bg="white" border="1px solid #E4E2DC" borderRadius="lg"
          borderLeft="3px solid #8E44AD">
          <Text fontSize="10px" fontWeight={700} color="#787469" mb={1}
            letterSpacing="0.06em" textTransform="uppercase">Models Available</Text>
          <Text fontSize="28px" fontWeight={700} color="#8E44AD"
            fontFamily='"Cormorant Garamond", serif'>{models.length}</Text>
          <Text fontSize="10px" color="#9E9A90">
            {models.map(m => m.name).join(', ') || 'none pulled'}
          </Text>
        </Box>
      </SimpleGrid>

      {/* ── Live Bots Summary Card ── */}
      {(() => {
        const localRunning = jobs.filter(j => j.status === 'running')
        const cloudRunning = ghRuns.filter(r => r.status === 'in_progress')
        const total = localRunning.length + cloudRunning.length
        if (total === 0 && localRunning.length === 0 && cloudRunning.length === 0) {
          // Still show the card even when idle
        }
        const accentColor = total > 0 ? '#27AE60' : '#9E9A90'
        return (
          <Box mb={6} p={4} bg="white" border="1px solid #E4E2DC" borderRadius="lg"
            borderLeft={`4px solid ${accentColor}`}>
            <Flex align="center" justify="space-between" mb={total > 0 ? 3 : 0}>
              <Flex align="center" gap={2}>
                <Activity size={14} color={accentColor} />
                <Text fontSize="11px" fontWeight={700} color="#5D4E37" textTransform="uppercase"
                  letterSpacing="0.07em">
                  Live Bots
                </Text>
              </Flex>
              <Box px={2} py="1px" bg={total > 0 ? 'rgba(39,174,96,0.12)' : 'rgba(158,154,144,0.1)'}
                borderRadius="full">
                <Text fontSize="11px" fontWeight={700} color={accentColor}>
                  {total > 0
                    ? `${total} active (${localRunning.length} local · ${cloudRunning.length} cloud)`
                    : 'All idle'}
                </Text>
              </Box>
            </Flex>
            {total > 0 && (
              <Flex gap={2} flexWrap="wrap">
                {localRunning.map(job => {
                  const elapsed = Math.max(0, (Date.now() - new Date(job.started).getTime()) / 1000)
                  const elapsedStr = elapsed < 60 ? `${Math.floor(elapsed)}s`
                    : elapsed < 3600 ? `${Math.floor(elapsed / 60)}m`
                    : `${Math.floor(elapsed / 3600)}h`
                  return (
                    <Box key={job.job_id} px={3} py={2} borderRadius="md"
                      bg="rgba(39,174,96,0.07)" border="1px solid rgba(39,174,96,0.25)">
                      <Flex align="center" gap={2}>
                        <Box w="7px" h="7px" borderRadius="full" bg="#27AE60"
                          style={{ animation: 'pulse 1.5s ease-in-out infinite' }} />
                        <Box>
                          <Text fontSize="11px" fontWeight={700} color="#1D6A3A">{job.bot}</Text>
                          <Text fontSize="10px" color="#5D8A6A">
                            {job.model} · {elapsedStr} · pid {job.pid ?? '—'}
                          </Text>
                        </Box>
                      </Flex>
                    </Box>
                  )
                })}
                {cloudRunning.map(run => (
                  <Box key={run.runId ?? run.name} px={3} py={2} borderRadius="md"
                    bg="rgba(36,113,163,0.07)" border="1px solid rgba(36,113,163,0.25)">
                    <Flex align="center" gap={2}>
                      <Box w="7px" h="7px" borderRadius="full" bg="#2471A3"
                        style={{ animation: 'pulse 1.5s ease-in-out infinite' }} />
                      <Box>
                        <Text fontSize="11px" fontWeight={700} color="#154360">
                          {run.name}
                        </Text>
                        <Text fontSize="10px" color="#5D7A8A">
                          ☁️ cloud · {relTime(run.startedAt)}
                        </Text>
                      </Box>
                    </Flex>
                  </Box>
                ))}
              </Flex>
            )}
          </Box>
        )
      })()}

      <SimpleGrid columns={{ base: 1, lg: 2 }} gap={6} mb={6}>

        {/* Live Process Status (ollama ps) */}
        <Box p={4} bg="#F8F9FA" border="1px solid #E4E2DC" borderRadius="lg">
          <Flex align="center" gap={2} mb={3}>
            <Activity size={15} color="#27AE60" />
            <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
              color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
              Live Inference (ollama ps)
            </Text>
            <Box w="6px" h="6px" borderRadius="full" bg={ps.length > 0 ? '#27AE60' : '#9E9A90'}
              ml={1}
              style={{ animation: ps.length > 0 ? 'pulse 1.6s ease-in-out infinite' : undefined }} />
          </Flex>

          {ps.length === 0 ? (
            <Flex align="center" gap={2} py={6} justify="center">
              <Server size={20} color="#D6D3CC" />
              <Text fontSize="13px" color="#9E9A90">No active inferences — model idle</Text>
            </Flex>
          ) : (
            ps.map((m, i) => (
              <Box key={i} p={3} mb={2} bg="white" border="1px solid #E4E2DC"
                borderLeft="3px solid #27AE60" borderRadius="md">
                <Flex align="center" justify="space-between">
                  <Text fontSize="13px" fontWeight={700} color="#2D2A24"
                    fontFamily='"JetBrains Mono", monospace'>{m.name}</Text>
                  <Flex align="center" gap={1}>
                    <Spinner size="xs" color="#27AE60" />
                    <Text fontSize="10px" color="#27AE60" fontWeight={700}>RUNNING</Text>
                  </Flex>
                </Flex>
                <Flex gap={3} mt={1}>
                  <Text fontSize="10px" color="#787469">RAM: {fmtBytes(m.size)}</Text>
                  {m.size_vram ? (
                    <Text fontSize="10px" color="#4A90D9">VRAM: {fmtBytes(m.size_vram)}</Text>
                  ) : null}
                  {m.details?.parameter_size && (
                    <Text fontSize="10px" color="#9E9A90">{m.details.parameter_size}</Text>
                  )}
                  {m.expires_at && (
                    <Text fontSize="10px" color="#9E9A90">
                      expires {relTime(m.expires_at)}
                    </Text>
                  )}
                </Flex>
              </Box>
            ))
          )}
        </Box>

        {/* Available models + quick launch */}
        <Box p={4} bg="#F8F9FA" border="1px solid #E4E2DC" borderRadius="lg">
          <Flex align="center" gap={2} mb={3}>
            <List size={15} color="#4A90D9" />
            <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
              color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
              Available Models
            </Text>
          </Flex>

          {models.length === 0 ? (
            <Box py={6} textAlign="center">
              <Text fontSize="13px" color="#9E9A90">No models pulled yet.</Text>
              <Text fontSize="11px" color="#9E9A90" mt={1}
                fontFamily='"JetBrains Mono", monospace'>
                ollama pull llama3.2:3b
              </Text>
            </Box>
          ) : (
            models.map((m, i) => (
              <Box key={i} p={3} mb={2} bg="white" border="1px solid #E4E2DC" borderRadius="md">
                <Flex align="center" justify="space-between">
                  <Box>
                    <Text fontSize="13px" fontWeight={700} color="#2D2A24"
                      fontFamily='"JetBrains Mono", monospace'>{m.name}</Text>
                    <Flex gap={2} mt={0.5}>
                      {m.details?.parameter_size && (
                        <Box px={1.5} py={0.5} bg="#4A90D915" borderRadius="sm"
                          fontSize="9px" fontWeight={700} color="#4A90D9">
                          {m.details.parameter_size}
                        </Box>
                      )}
                      {m.details?.quantization_level && (
                        <Box px={1.5} py={0.5} bg="#E67E2215" borderRadius="sm"
                          fontSize="9px" fontWeight={700} color="#E67E22">
                          {m.details.quantization_level}
                        </Box>
                      )}
                      {m.size && (
                        <Text fontSize="10px" color="#9E9A90">{fmtBytes(m.size)}</Text>
                      )}
                    </Flex>
                  </Box>
                  <Box px={1.5} py={0.5} bg="#27AE6015" borderRadius="sm"
                    fontSize="9px" fontWeight={700} color="#27AE60">
                    READY
                  </Box>
                </Flex>
              </Box>
            ))
          )}

          {/* Pull hint */}
          <Box mt={3} p={3} bg="#E8F4FD" border="1px solid #BDE0F7" borderRadius="md">
            <Text fontSize="10px" fontWeight={700} color="#2D2A24" mb={1}>
              Upgrade for higher quality
            </Text>
            <Text fontSize="10px" fontFamily='"JetBrains Mono", monospace' color="#4A90D9">
              ollama pull llama3.1:8b
            </Text>
            <Text fontSize="9px" color="#787469" mt={0.5}>
              8b = better relationships & narratives; needs ~6 GB RAM
            </Text>
          </Box>
        </Box>
      </SimpleGrid>

      {/* ── Pending local changes banner ─────────────────────────────── */}
      {pending?.hasPending && (
        <Box mb={6} p={4} bg="#FEF9E7" border="1px solid #F1C40F" borderRadius="lg">
          <Flex align="center" justify="space-between" flexWrap="wrap" gap={3}>
            <Flex align="center" gap={2}>
              <GitCommit size={16} color="#C5963A" />
              <Box>
                <Text fontWeight={700} color="#2D2A24" fontSize="sm">
                  {pending.total} local files ready to push to Appwrite
                </Text>
                <Text fontSize="11px" color="#787469">
                  {pending.entities} entities · {pending.edges} edges — uncommitted on this machine
                </Text>
              </Box>
            </Flex>
            <Flex gap={2} flexWrap="wrap">
              <Box
                as="button"
                onClick={() => !launching && serverOnline && launch('/bots/push', {}, 'git-push')}
                px={4} py={2} borderRadius="md"
                bg="#4A90D915" border="1px solid #4A90D940" color="#4A90D9"
                cursor={serverOnline ? 'pointer' : 'not-allowed'}
                _hover={serverOnline ? { bg: '#4A90D925' } : {}}
                display="flex" alignItems="center" gap={1.5}
              >
                {launching === 'git-push' ? <Spinner size="xs" /> : <Upload size={13} />}
                <Text fontSize="11px" fontWeight={700}>
                  {launching === 'git-push' ? 'PUSHING…' : 'GIT COMMIT + PUSH'}
                </Text>
              </Box>
              <Box
                as="button"
                onClick={() => !launching && serverOnline && launch('/bots/sync-and-push', { max: 200 }, 'sync-push')}
                px={4} py={2} borderRadius="md"
                bg="#27AE6015" border="1px solid #27AE6040" color="#27AE60"
                cursor={serverOnline ? 'pointer' : 'not-allowed'}
                _hover={serverOnline ? { bg: '#27AE6025' } : {}}
                display="flex" alignItems="center" gap={1.5}
              >
                {launching === 'sync-push' ? <Spinner size="xs" /> : <Cloud size={13} />}
                <Text fontSize="11px" fontWeight={700}>
                  {launching === 'sync-push' ? 'SYNCING…' : 'SYNC TO APPWRITE + PUSH'}
                </Text>
              </Box>
            </Flex>
          </Flex>
        </Box>
      )}

      {/* ── GitHub Actions Status ─────────────────────────────────────── */}
      {ghRuns.length > 0 && (
        <Box mb={6} p={4} bg="#F8F9FA" border="1px solid #E4E2DC" borderRadius="lg">
          <Flex align="center" gap={2} mb={3}>
            <Cloud size={15} color="#4A90D9" />
            <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
              color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
              GitHub Actions — Cloud Bots
            </Text>
            <Box px={2} py={0.5} bg="#4A90D915" border="1px solid #4A90D940"
              borderRadius="md" fontSize="9px" fontWeight={700} color="#4A90D9">
              PARALLEL WITH LOCAL
            </Box>
          </Flex>
          <Text fontSize="11px" color="#787469" mb={3}>
            Cloud bots run on GitHub's servers concurrently with local Ollama bots — safe because each targets different entities.
            Local and cloud can run simultaneously for maximum throughput.
          </Text>
          <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }} gap={2}>
            {ghRuns.map((run, i) => {
              const isRunning = run.status === 'in_progress'
              const isSuccess = run.conclusion === 'success'
              const isFailure = run.conclusion === 'failure'
              const color = isRunning ? '#E67E22' : isSuccess ? '#27AE60' : isFailure ? '#C0392B' : '#9E9A90'
              return (
                <Box key={i} p={3} bg="white" border="1px solid #E4E2DC"
                  borderLeft={`3px solid ${color}`} borderRadius="md">
                  <Flex align="center" justify="space-between" mb={1}>
                    <Flex align="center" gap={1.5}>
                      {isRunning && <Spinner size="xs" color="#E67E22" />}
                      {isSuccess && <CheckCircle2 size={12} color="#27AE60" />}
                      {isFailure && <XCircle size={12} color="#C0392B" />}
                      {!isRunning && !isSuccess && !isFailure && <MinusCircle size={12} color="#9E9A90" />}
                      <Text fontSize="11px" fontWeight={700} color="#2D2A24" noOfLines={1}>
                        {run.name.replace(/\s*\(.*?\)\s*/g, '').replace('AI Entity Enrichment', 'AI Enrich').replace('Sync Gateway', 'Sync').replace('Significance Backfill', 'Significance')}
                      </Text>
                    </Flex>
                    {run.htmlUrl && (
                      <Box as="a" href={run.htmlUrl} target="_blank" rel="noopener noreferrer"
                        color="#9E9A90" _hover={{ color: '#4A90D9' }}>
                        <ExternalLink size={11} />
                      </Box>
                    )}
                  </Flex>
                  <Flex gap={2} align="center">
                    <Box px={1.5} py={0.5} borderRadius="sm" fontSize="9px" fontWeight={700}
                      bg={`${color}20`} color={color}>
                      {isRunning ? 'RUNNING' : (run.conclusion?.toUpperCase() ?? run.status.toUpperCase())}
                    </Box>
                    <Text fontSize="9px" color="#9E9A90">
                      {run.triggeredBy} · {relTime(run.updatedAt ?? run.startedAt)}
                    </Text>
                  </Flex>
                </Box>
              )
            })}
          </SimpleGrid>
        </Box>
      )}

      {/* Quick Launch Panel */}
      <Box mb={6} p={4} bg="#FAF3E8" border="1px solid #E8D5B0" borderRadius="lg">
        <Flex align="center" gap={2} mb={3}>
          <Swords size={15} color="#C5963A" />
          <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
            color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
            Quick Launch — Local Only (No Cloud Costs)
          </Text>
          <Box px={2} py={0.5} bg="#27AE6015" border="1px solid #27AE6040"
            borderRadius="md" fontSize="9px" fontWeight={700} color="#27AE60">
            OLLAMA ONLY · £0
          </Box>
        </Flex>
        <Flex gap={3} flexWrap="wrap">
          {[
            { label: 'Enrich 20', endpoint: '/bots/enrich', body: { count: 20 }, color: '#27AE60', icon: BookOpen, desc: '~1 hr CPU' },
            { label: 'Enrich 50', endpoint: '/bots/enrich', body: { count: 50 }, color: '#4A90D9', icon: BookOpen, desc: '~2.5 hr CPU' },
            { label: 'Significance 100', endpoint: '/bots/significance', body: { count: 100 }, color: '#8E44AD', icon: BarChart3, desc: '~1.5 hr CPU' },
            { label: 'Significance 200', endpoint: '/bots/significance', body: { count: 200 }, color: '#6B3FA0', icon: BarChart3, desc: '~3 hr CPU' },
            { label: 'Rebuild Queue', endpoint: '/bots/queue', body: {}, color: '#E67E22', icon: GitBranch, desc: '~2 min' },
            { label: 'Sync+Push', endpoint: '/bots/sync-and-push', body: { max: 150 }, color: '#4A90D9', icon: Upload, desc: 'Appwrite+git' },
            { label: 'Assist All', endpoint: '/bots/all', body: { enrichCount: 20, sigCount: 50, autoPush: true }, color: '#C5963A', icon: Zap, desc: 'All bots + push' },
          ].map(btn => {
            const Icon = btn.icon
            const busy = launching === btn.label
            return (
              <Box key={btn.label}
                as="button"
                onClick={() => !busy && serverOnline && launch(btn.endpoint, btn.body, btn.label)}
                px={4} py={2.5}
                borderRadius="md"
                bg={serverOnline ? `${btn.color}15` : '#F5F4F0'}
                border={`1px solid ${serverOnline ? btn.color + '40' : '#E4E2DC'}`}
                color={serverOnline ? btn.color : '#9E9A90'}
                cursor={serverOnline ? 'pointer' : 'not-allowed'}
                _hover={serverOnline ? { bg: `${btn.color}25` } : {}}
                display="flex" flexDirection="column" alignItems="center" gap={1}
                minW="110px"
              >
                <Flex align="center" gap={1.5}>
                  {busy ? <Spinner size="xs" /> : <Icon size={13} />}
                  <Text fontSize="11px" fontWeight={700}>{busy ? 'LAUNCHING…' : btn.label}</Text>
                </Flex>
                <Text fontSize="9px" color="#787469">{btn.desc}</Text>
              </Box>
            )
          })}
          {activeJobs.length > 0 && (
            <Box
              as="button"
              onClick={() => localPost('/bots/stop', {})}
              px={4} py={2.5}
              borderRadius="md"
              bg="#C0392B15" border="1px solid #C0392B40" color="#C0392B"
              cursor="pointer"
              display="flex" alignItems="center" gap={1.5}
            >
              <StopCircle size={13} />
              <Text fontSize="11px" fontWeight={700}>STOP ALL</Text>
            </Box>
          )}
        </Flex>
      </Box>

      {/* ── Comprehensive Bot Stats Card ── */}
      {sprint && (() => {
        const winKey = statsWindow
        const win = sprint.windows?.[winKey]
        const windowLabel: Record<string, string> = {
          last_24h: 'Today (24h)', last_7d: 'This Week (7d)', last_30d: 'This Month (30d)',
        }
        const actionLabel: Record<string, string> = {
          entity_enrich: 'Entity Enrichment',
          historicalSignificance: 'Significance Rating',
          queue_scan: 'Queue Scan',
          appwrite_sync: 'Appwrite Sync',
          git_push: 'Git Push',
          other: 'Other',
        }
        const actionColor: Record<string, string> = {
          entity_enrich: '#27AE60', historicalSignificance: '#8E44AD',
          appwrite_sync: '#2471A3', git_push: '#E67E22', queue_scan: '#4A90D9', other: '#9E9A90',
        }
        // Cloud bots from ghRuns
        const cloudTotal = ghRuns.filter(r => r.conclusion === 'success').length
        const cloudRunning = ghRuns.filter(r => r.status === 'in_progress').length

        return (
          <Box mb={6} p={5} bg="white" border="1px solid #E4E2DC" borderRadius="lg">
            {/* Header + window switcher */}
            <Flex align="center" justify="space-between" mb={4} flexWrap="wrap" gap={3}>
              <Flex align="center" gap={2}>
                <BarChart3 size={15} color="#C5963A" />
                <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
                  color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
                  Bot Performance Analytics
                </Text>
              </Flex>
              <Flex gap={1}>
                {(['last_24h', 'last_7d', 'last_30d'] as const).map(w => (
                  <Box key={w} as="button" onClick={() => setStatsWindow(w)}
                    px={3} py={1} borderRadius="md" cursor="pointer" fontSize="10px" fontWeight={700}
                    bg={statsWindow === w ? '#C5963A' : '#F5F4F0'}
                    color={statsWindow === w ? 'white' : '#787469'}
                    border={`1px solid ${statsWindow === w ? '#C5963A' : '#E4E2DC'}`}>
                    {windowLabel[w]}
                  </Box>
                ))}
              </Flex>
            </Flex>

            {/* Top-level KPIs */}
            <SimpleGrid columns={{ base: 2, md: 4 }} gap={3} mb={5}>
              <Box p={3} bg="#FAFAF8" borderRadius="md" borderLeft="3px solid #27AE60">
                <Text fontSize="9px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em">Entities Enriched</Text>
                <Text fontSize="22px" fontWeight={700} color="#27AE60"
                  fontFamily='"Cormorant Garamond", serif'>
                  {(win?.totalEntities ?? sprint.totalEntitiesProcessed).toLocaleString()}
                </Text>
                <Text fontSize="10px" color="#9E9A90">{windowLabel[winKey]}</Text>
              </Box>
              <Box p={3} bg="#FAFAF8" borderRadius="md" borderLeft="3px solid #4A90D9">
                <Text fontSize="9px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em">Jobs Completed</Text>
                <Text fontSize="22px" fontWeight={700} color="#4A90D9"
                  fontFamily='"Cormorant Garamond", serif'>
                  {(win?.completedJobs ?? sprint.completedJobs).toLocaleString()}
                </Text>
                <Text fontSize="10px" color="#9E9A90">{win?.failedJobs ?? 0} failed</Text>
              </Box>
              <Box p={3} bg="#FAFAF8" borderRadius="md" borderLeft="3px solid #8E44AD">
                <Text fontSize="9px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em">Cloud Runs (GH)</Text>
                <Text fontSize="22px" fontWeight={700} color="#8E44AD"
                  fontFamily='"Cormorant Garamond", serif'>{cloudTotal}</Text>
                <Text fontSize="10px" color="#9E9A90">{cloudRunning} in progress</Text>
              </Box>
              <Box p={3} bg="#FAFAF8" borderRadius="md" borderLeft="3px solid #E67E22">
                <Text fontSize="9px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em">Local Active</Text>
                <Text fontSize="22px" fontWeight={700} color="#E67E22"
                  fontFamily='"Cormorant Garamond", serif'>{activeJobs.length}</Text>
                <Text fontSize="10px" color="#9E9A90">
                  {serverOnline ? '🟢 server online' : '🔴 server offline'}
                </Text>
              </Box>
            </SimpleGrid>

            <SimpleGrid columns={{ base: 1, md: 3 }} gap={4}>
              {/* Action Breakdown */}
              <Box>
                <Text fontSize="10px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em" mb={2}>Action Breakdown</Text>
                {win && Object.keys(win.byAction).length > 0 ? (
                  Object.entries(win.byAction)
                    .sort((a, b) => b[1] - a[1])
                    .map(([action, count]) => {
                      const total = Object.values(win.byAction).reduce((a, b) => a + b, 0) || 1
                      const pct = Math.round((count / total) * 100)
                      const color = actionColor[action] ?? '#9E9A90'
                      return (
                        <Box key={action} mb={2}>
                          <Flex justify="space-between" mb={1}>
                            <Text fontSize="10px" color="#524E44">{actionLabel[action] ?? action}</Text>
                            <Text fontSize="10px" fontWeight={700} color={color}>{count} ({pct}%)</Text>
                          </Flex>
                          <Box h="4px" bg="#F0EDE8" borderRadius="full">
                            <Box h="4px" bg={color} borderRadius="full" w={`${pct}%`} />
                          </Box>
                        </Box>
                      )
                    })
                ) : (
                  <Text fontSize="11px" color="#9E9A90">No actions yet in this window.</Text>
                )}
              </Box>

              {/* Top Performers */}
              <Box>
                <Text fontSize="10px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em" mb={2}>Top Performers (all-time)</Text>
                {(sprint.topPerformers ?? []).length > 0 ? (
                  (sprint.topPerformers ?? []).slice(0, 6).map((p, i) => (
                    <Flex key={p.bot} align="center" gap={2} mb={1.5}>
                      <Text fontSize="10px" fontWeight={700} color="#B8B2A4" w="16px">#{i + 1}</Text>
                      <Box flex={1}>
                        <Text fontSize="11px" fontWeight={600} color="#2D2A24">{p.bot}</Text>
                      </Box>
                      <Box px={2} py={0.5} bg="#27AE6010" borderRadius="sm">
                        <Text fontSize="10px" fontWeight={700} color="#27AE60">
                          {p.total.toLocaleString()}
                        </Text>
                      </Box>
                    </Flex>
                  ))
                ) : (
                  <Text fontSize="11px" color="#9E9A90">No data yet.</Text>
                )}
              </Box>

              {/* Active Editors */}
              <Box>
                <Text fontSize="10px" fontWeight={700} color="#787469" textTransform="uppercase"
                  letterSpacing="0.06em" mb={2}>Active Editors (last hour)</Text>
                {/* Local editors from jobs */}
                {(sprint.activeEditors ?? []).length > 0 ? (
                  (sprint.activeEditors ?? []).slice(0, 5).map((ed, i) => (
                    <Flex key={i} align="center" gap={2} mb={2}>
                      <Box w="7px" h="7px" borderRadius="full" flexShrink={0}
                        bg={ed.status === 'running' ? '#27AE60' : '#9E9A90'} />
                      <Box flex={1}>
                        <Text fontSize="11px" fontWeight={600} color="#2D2A24">{ed.editorId}</Text>
                        <Text fontSize="9px" color="#9E9A90">
                          {ed.env === 'local' ? '⚙ Local Ollama' : '☁ Cloud GH Actions'} · {ed.status}
                        </Text>
                      </Box>
                    </Flex>
                  ))
                ) : (
                  <Text fontSize="11px" color="#9E9A90">No local editors active in last hour.</Text>
                )}
                {/* Cloud editors from ghRuns */}
                {ghRuns.filter(r => r.status === 'in_progress').map(r => (
                  <Flex key={r.runId} align="center" gap={2} mb={2}>
                    <Box w="7px" h="7px" borderRadius="full" flexShrink={0} bg="#2471A3" />
                    <Box flex={1}>
                      <Text fontSize="11px" fontWeight={600} color="#2D2A24">{r.name}</Text>
                      <Text fontSize="9px" color="#9E9A90">☁ Cloud · started {relTime(r.startedAt)}</Text>
                    </Box>
                  </Flex>
                ))}
                {(sprint.activeEditors ?? []).length === 0 && ghRuns.filter(r => r.status === 'in_progress').length === 0 && (
                  <Text fontSize="11px" color="#9E9A90">No editors active right now.</Text>
                )}
              </Box>
            </SimpleGrid>
          </Box>
        )
      })()}

      {/* Job History — collapsible */}
      <Box mb={6} border="1px solid #E4E2DC" borderRadius="lg" overflow="hidden">
        <Box
          as="button" w="100%"
          onClick={() => setHistoryOpen(!historyOpen)}
          p={4} bg="#FAFAF8" cursor="pointer"
          _hover={{ bg: '#F0EDE8' }}
          display="flex" alignItems="center" justifyContent="space-between"
        >
          <Flex align="center" gap={2}>
            <Clock size={15} color="#787469" />
            <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
              color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
              Job History
            </Text>
            {recentJobs.length > 0 && (
              <Box px={2} py={0.5} bg="#E4E2DC" borderRadius="full">
                <Text fontSize="10px" fontWeight={700} color="#787469">{recentJobs.length}</Text>
              </Box>
            )}
          </Flex>
          <Text fontSize="11px" color="#9E9A90">{historyOpen ? '▲ collapse' : '▼ expand'}</Text>
        </Box>

        {historyOpen && (
          <Box p={4}>
        {recentJobs.length === 0 ? (
          <Text fontSize="13px" color="#9E9A90" py={4} textAlign="center">
            No jobs run yet. Press a Launch button above.
          </Text>
        ) : (
          <Box>
            {recentJobs.map(job => (
              <Box key={job.job_id} mb={2}>
                <Box
                  as="button"
                  w="100%"
                  onClick={() => setOpenLog(openLog === job.job_id ? null : job.job_id)}
                  p={3} bg="white" border="1px solid #E4E2DC"
                  borderLeft={`3px solid ${STATUS_COLOR[job.status] ?? '#9E9A90'}`}
                  borderRadius="md" textAlign="left" cursor="pointer"
                  _hover={{ bg: '#F5F4F0' }}
                >
                  <Flex align="center" gap={3}>
                    {job.status === 'running' && <Spinner size="xs" color="#E67E22" />}
                    {job.status === 'done' && <CheckCircle2 size={13} color="#27AE60" />}
                    {job.status === 'error' && <AlertTriangle size={13} color="#C0392B" />}
                    {(job.status === 'queued' || job.status === 'stopped') && (
                      <Clock size={13} color="#9E9A90" />
                    )}
                    <Box flex={1}>
                      <Flex align="center" gap={2}>
                        <Text fontSize="12px" fontWeight={700} color="#2D2A24">
                          {job.bot.toUpperCase()}
                        </Text>
                        <Box px={1.5} py={0.5} borderRadius="sm" fontSize="9px" fontWeight={700}
                          bg={`${STATUS_COLOR[job.status]}20`}
                          color={STATUS_COLOR[job.status]}>
                          {job.status.toUpperCase()}
                        </Box>
                        <Box px={1.5} py={0.5} borderRadius="sm" fontSize="9px" fontWeight={700}
                          bg="#27AE6015" color="#27AE60">
                          {job.model}
                        </Box>
                      </Flex>
                      <Text fontSize="10px" color="#9E9A90" mt={0.5}>
                        {job.count > 0 ? `${job.count} entities · ` : ''}{relTime(job.started)}
                        {job.finished ? ` → finished ${relTime(job.finished)}` : ''}
                        {job.pid ? ` · PID ${job.pid}` : ''}
                      </Text>
                    </Box>
                    <Text fontSize="9px" color="#9E9A90">
                      {openLog === job.job_id ? '▲ hide log' : '▼ show log'}
                    </Text>
                  </Flex>
                </Box>

                {/* Log panel */}
                {openLog === job.job_id && (
                  <Box
                    p={3} bg="#2D2A24" borderRadius="md" mt={1}
                    maxH="300px" overflowY="auto"
                    css={{
                      '&::-webkit-scrollbar': { width: '4px' },
                      '&::-webkit-scrollbar-thumb': { background: '#555', borderRadius: '4px' },
                    }}
                  >
                    {job.log.length === 0 ? (
                      <Text fontSize="11px" color="#9E9A90"
                        fontFamily='"JetBrains Mono", monospace'>
                        (no output yet)
                      </Text>
                    ) : (
                      job.log.map((line, i) => {
                        // Colour-code log lines
                        const isOk = /✓|ok|succeeded|done/i.test(line)
                        const isErr = /✗|error|fail|except/i.test(line)
                        const isInfo = /^  ▸|^Processing|^\[/i.test(line)
                        const color = isErr ? '#FF6B6B' : isOk ? '#6EE7A0' : isInfo ? '#93C5FD' : '#D4D0C8'
                        return (
                          <Text key={i} fontSize="11px" color={color}
                            fontFamily='"JetBrains Mono", monospace' lineHeight="1.7">
                            {line || '\u00A0'}
                          </Text>
                        )
                      })
                    )}
                  </Box>
                )}
              </Box>
            ))}
          </Box>
        )}
          </Box>
        )}
      </Box>

      {/* What Ollama does for this project */}
      <Box p={4} bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg">
        <Flex align="center" gap={2} mb={4}>
          <Cpu size={15} color="#C5963A" />
          <Text fontFamily='"Cinzel", serif' fontSize="sm" fontWeight={700}
            color="#2D2A24" letterSpacing="0.08em" textTransform="uppercase">
            What Ollama Does for This Project
          </Text>
        </Flex>
        <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
          {OLLAMA_TASKS.map((task, i) => {
            const Icon = task.icon
            return (
              <Box key={i} p={4} bg="white" border="1px solid #E4E2DC"
                borderLeft={`3px solid ${task.color}`} borderRadius="md">
                <Flex align="center" gap={2} mb={2}>
                  <Box p={1.5} borderRadius="sm" bg={`${task.color}15`}>
                    <Icon size={14} color={task.color} />
                  </Box>
                  <Text fontSize="13px" fontWeight={700} color="#2D2A24">{task.title}</Text>
                </Flex>
                <Text fontSize="11px" fontFamily='"JetBrains Mono", monospace'
                  color="#4A90D9" mb={1.5}>{task.script}</Text>
                <Text fontSize="12px" color="#524E44" lineHeight="1.6" mb={2}>
                  {task.description}
                </Text>
                <Flex gap={2} flexWrap="wrap">
                  <Box px={2} py={1} bg="#F5F4F0" borderRadius="sm">
                    <Text fontSize="9px" fontWeight={700} color="#787469">VOLUME</Text>
                    <Text fontSize="10px" color="#2D2A24">{task.volume}</Text>
                  </Box>
                  <Box px={2} py={1} bg="#27AE6010" borderRadius="sm">
                    <Text fontSize="9px" fontWeight={700} color="#27AE60">COST</Text>
                    <Text fontSize="10px" color="#2D2A24" fontWeight={600}>{task.cost}</Text>
                  </Box>
                </Flex>
                <Text fontSize="10px" color="#9E9A90" mt={1.5} lineHeight="1.5">
                  <strong>Quality:</strong> {task.quality}
                </Text>
              </Box>
            )
          })}
        </SimpleGrid>
      </Box>
    </Box>
  )
}
