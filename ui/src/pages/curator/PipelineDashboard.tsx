import React, { useEffect, useState, useCallback, useRef } from 'react'
import { Box, Flex, Text, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, RefreshCw, CheckCircle2, AlertTriangle, Clock, Filter,
  Zap, Activity, TrendingUp, Database, ArrowRight, GitMerge,
} from 'lucide-react'
import { databases, DATABASE_ID } from '../../lib/appwrite'

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Types                                                                       */
/* ─────────────────────────────────────────────────────────────────────────── */

interface PipelineStatus {
  generatedAt: string
  cleanCount: number
  rejectedCount: number
  pendingCount: number
  inFlightCount: number
  triagedCount: number
  validatedCount: number
  triageReport: string | null
  validateReport: string | null
  enrichReport: string | null
}

interface TriageReport {
  scanned: number
  uniqueSlugs: number
  counts: { triaged: number; rejected: number }
  byReason: Record<string, number>
  elapsedSec: number
  generatedAt: string
}

interface ValidateReport {
  processed: number
  counts: { validated: number; triaged: number; rejected: number }
  byReason: Record<string, number>
  elapsedSec: number
  generatedAt: string
}

interface EnrichReport {
  selected: number
  model: string
  enricherExitCode: number
  elapsedSec: number
  generatedAt: string
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Small reusable components                                                   */
/* ─────────────────────────────────────────────────────────────────────────── */

function KpiCard({
  label, value, sub, color, icon,
}: {
  label: string; value: React.ReactNode; sub?: string; color: string; icon: React.ReactNode
}) {
  return (
    <Box
      bg="rgba(255,255,255,0.04)"
      border="1px solid rgba(255,255,255,0.1)"
      borderRadius="12px"
      p="20px"
      position="relative"
      overflow="hidden"
    >
      <Box
        position="absolute" top={0} left={0}
        w="4px" h="100%" bg={color} borderRadius="12px 0 0 12px"
      />
      <Flex align="center" gap="10px" mb="12px">
        <Box color={color}>{icon}</Box>
        <Text fontSize="11px" fontWeight={600} color="rgba(255,255,255,0.5)"
              textTransform="uppercase" letterSpacing="0.08em">{label}</Text>
      </Flex>
      <Text fontSize="32px" fontWeight={700} color="#FAF3E8" lineHeight={1}>{value}</Text>
      {sub && <Text fontSize="11px" color="rgba(255,255,255,0.4)" mt="6px">{sub}</Text>}
    </Box>
  )
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Stadium exit SVG                                                            */
/* ─────────────────────────────────────────────────────────────────────────── */

function StadiumDiagram({ total, triaged, validated, rejected, inFlight }: {
  total: number; triaged: number; validated: number; rejected: number; inFlight: number
}) {
  const t = total || 1
  const triPct  = Math.round((triaged   / t) * 100)
  const valPct  = Math.round((validated / t) * 100)
  const rejPct  = Math.round((rejected  / t) * 100)
  const infPct  = Math.round((inFlight  / t) * 100)
  const pendPct = Math.max(0, 100 - triPct - rejPct)

  const lanes = [
    { label: 'Source',     pct: 100,    color: '#6B7280', count: total },
    { label: 'Triaged',    pct: triPct,  color: '#3B82F6', count: triaged },
    { label: 'In-Flight',  pct: infPct,  color: '#F59E0B', count: inFlight },
    { label: 'Validated',  pct: valPct,  color: '#10B981', count: validated },
    { label: 'Rejected',   pct: rejPct,  color: '#EF4444', count: rejected },
    { label: 'Pending',    pct: pendPct, color: '#8B5CF6', count: Math.max(0, triaged - validated - inFlight) },
  ]

  return (
    <Box
      bg="rgba(255,255,255,0.03)"
      border="1px solid rgba(255,255,255,0.08)"
      borderRadius="12px"
      p="24px"
    >
      <Text fontSize="13px" fontWeight={600} color="rgba(255,255,255,0.6)"
            textTransform="uppercase" letterSpacing="0.08em" mb="20px">
        Stadium Exits — Entity Flow
      </Text>

      {/* Funnel bars */}
      <Box>
        {lanes.map((lane, i) => (
          <Box key={lane.label} mb={i < lanes.length - 1 ? '14px' : 0}>
            <Flex justify="space-between" mb="5px">
              <Flex align="center" gap="8px">
                <Box w="8px" h="8px" borderRadius="50%" bg={lane.color} flexShrink={0} />
                <Text fontSize="12px" fontWeight={500} color="rgba(255,255,255,0.7)">{lane.label}</Text>
              </Flex>
              <Flex gap="12px" align="center">
                <Text fontSize="12px" color="rgba(255,255,255,0.4)">{lane.count.toLocaleString()}</Text>
                <Text fontSize="11px" fontWeight={600} color={lane.color} w="36px" textAlign="right">
                  {lane.pct}%
                </Text>
              </Flex>
            </Flex>
            <Box bg="rgba(255,255,255,0.07)" borderRadius="4px" h="8px" overflow="hidden">
              <Box
                h="100%"
                w={`${lane.pct}%`}
                bg={lane.color}
                borderRadius="4px"
                transition="width 0.8s cubic-bezier(.23,1,.32,1)"
                opacity={0.85}
              />
            </Box>
          </Box>
        ))}
      </Box>

      {/* Flow arrows */}
      <Flex
        mt="28px"
        align="center"
        justify="space-between"
        gap="4px"
        px="8px"
        py="14px"
        bg="rgba(0,0,0,0.2)"
        borderRadius="8px"
        flexWrap="wrap"
      >
        {[
          { label: 'Source', sub: total.toLocaleString(), color: '#6B7280' },
          { icon: <ArrowRight size={14} />, color: '#374151' },
          { label: 'Triage', sub: triaged.toLocaleString(), color: '#3B82F6' },
          { icon: <ArrowRight size={14} />, color: '#374151' },
          { label: 'Enrich', sub: inFlight.toLocaleString() + ' active', color: '#F59E0B' },
          { icon: <ArrowRight size={14} />, color: '#374151' },
          { label: 'Validate', sub: validated.toLocaleString(), color: '#10B981' },
          { icon: <GitMerge size={14} />, color: '#374151' },
          { label: 'Clean', sub: validated.toLocaleString(), color: '#10B981' },
        ].map((item, i) =>
          'icon' in item ? (
            <Box key={i} color={item.color}>{item.icon}</Box>
          ) : (
            <Box key={i} textAlign="center">
              <Text fontSize="11px" fontWeight={700} color={item.color}>{item.label}</Text>
              <Text fontSize="10px" color="rgba(255,255,255,0.3)">{item.sub}</Text>
            </Box>
          )
        )}
      </Flex>
    </Box>
  )
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Reason breakdown table                                                      */
/* ─────────────────────────────────────────────────────────────────────────── */

function ReasonTable({ title, data, total, color }: {
  title: string; data: Record<string, number>; total: number; color: string
}) {
  const sorted = Object.entries(data).sort((a, b) => b[1] - a[1])
  return (
    <Box
      bg="rgba(255,255,255,0.03)"
      border="1px solid rgba(255,255,255,0.08)"
      borderRadius="12px"
      p="20px"
    >
      <Text fontSize="12px" fontWeight={600} color="rgba(255,255,255,0.6)"
            textTransform="uppercase" letterSpacing="0.08em" mb="16px">{title}</Text>
      {sorted.map(([reason, count]) => {
        const pct = total > 0 ? Math.round((count / total) * 100) : 0
        return (
          <Box key={reason} mb="10px">
            <Flex justify="space-between" mb="3px">
              <Text fontSize="11px" color="rgba(255,255,255,0.6)" fontFamily="'JetBrains Mono',monospace">
                {reason}
              </Text>
              <Text fontSize="11px" color="rgba(255,255,255,0.4)">{count.toLocaleString()} ({pct}%)</Text>
            </Flex>
            <Box bg="rgba(255,255,255,0.06)" borderRadius="3px" h="4px">
              <Box h="100%" w={`${pct}%`} bg={color} borderRadius="3px" opacity={0.7} />
            </Box>
          </Box>
        )
      })}
    </Box>
  )
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Animated counter                                                            */
/* ─────────────────────────────────────────────────────────────────────────── */

function AnimatedCounter({ target }: { target: number }) {
  const [display, setDisplay] = useState(target)
  const prev = useRef(target)
  useEffect(() => {
    if (target === prev.current) return
    const diff = target - prev.current
    const steps = 30
    const step = diff / steps
    let i = 0
    const interval = setInterval(() => {
      i++
      setDisplay(Math.round(prev.current + step * i))
      if (i >= steps) { setDisplay(target); prev.current = target; clearInterval(interval) }
    }, 20)
    return () => clearInterval(interval)
  }, [target])
  return <>{display.toLocaleString()}</>
}

/* ─────────────────────────────────────────────────────────────────────────── */
/*  Main page                                                                   */
/* ─────────────────────────────────────────────────────────────────────────── */

const POLL_MS = 30_000

export default function PipelineDashboard() {
  const nav = useNavigate()
  const [status, setStatus] = useState<PipelineStatus | null>(null)
  const [triage, setTriage] = useState<TriageReport | null>(null)
  const [validate, setValidate] = useState<ValidateReport | null>(null)
  const [enrich, setEnrich] = useState<EnrichReport | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [lastRefresh, setLastRefresh] = useState(new Date())

  const fetchStatus = useCallback(async () => {
    try {
      const doc = await databases.getDocument(DATABASE_ID, 'pipeline_status', 'global') as unknown as PipelineStatus
      setStatus(doc)
      if (doc.triageReport)   setTriage(JSON.parse(doc.triageReport) as TriageReport)
      if (doc.validateReport) setValidate(JSON.parse(doc.validateReport) as ValidateReport)
      if (doc.enrichReport)   setEnrich(JSON.parse(doc.enrichReport) as EnrichReport)
      setError(null)
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e))
    } finally {
      setLoading(false)
      setLastRefresh(new Date())
    }
  }, [])

  useEffect(() => {
    fetchStatus()
    const t = setInterval(fetchStatus, POLL_MS)
    return () => clearInterval(t)
  }, [fetchStatus])

  function fmt(iso?: string | null) {
    if (!iso) return '—'
    return new Date(iso).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
  }

  const total = triage?.scanned ?? 392078
  const triaged = status?.triagedCount ?? 0
  const validated = status?.validatedCount ?? 0
  const clean = status?.cleanCount ?? 0
  const rejected = status?.rejectedCount ?? 0
  const inFlight = status?.inFlightCount ?? 0
  const pending = Math.max(0, triaged - validated - inFlight)

  return (
    <Box minH="100vh" bg="#0F0A05" color="#FAF3E8">
      {/* Header */}
      <Flex
        align="center" justify="space-between"
        px={{ base: '16px', md: '32px' }} py="16px"
        borderBottom="1px solid rgba(255,255,255,0.08)"
        position="sticky" top={0} zIndex={10}
        bg="rgba(15,10,5,0.95)"
        backdropFilter="blur(12px)"
      >
        <Flex align="center" gap="12px">
          <Box
            as="button"
            onClick={() => nav('/curator')}
            display="flex" alignItems="center" gap="6px"
            px="12px" py="6px" borderRadius="8px"
            bg="rgba(255,255,255,0.06)"
            color="rgba(255,255,255,0.7)"
            fontSize="13px"
            cursor="pointer"
            _hover={{ bg: 'rgba(255,255,255,0.1)' }}
          >
            <ChevronLeft size={14} /> Curator
          </Box>
          <Box w="1px" h="20px" bg="rgba(255,255,255,0.1)" />
          <Flex align="center" gap="8px">
            <Box w="8px" h="8px" borderRadius="50%" bg="#10B981"
                 style={{ animation: 'pulse 2s infinite' }} />
            <Text fontSize="15px" fontWeight={700} color="#FAF3E8"
                  fontFamily="'Cormorant Garamond',serif" letterSpacing="0.02em">
              Pipeline Dashboard
            </Text>
          </Flex>
        </Flex>
        <Flex align="center" gap="12px">
          <Text fontSize="11px" color="rgba(255,255,255,0.3)">
            Updated {lastRefresh.toLocaleTimeString()}
          </Text>
          <Box
            as="button"
            onClick={fetchStatus}
            display="flex" alignItems="center" gap="5px"
            px="12px" py="6px" borderRadius="8px"
            bg="rgba(255,255,255,0.06)"
            color="rgba(255,255,255,0.6)"
            fontSize="12px"
            cursor="pointer"
            _hover={{ bg: 'rgba(255,255,255,0.1)' }}
          >
            <RefreshCw size={13} /> Refresh
          </Box>
        </Flex>
      </Flex>

      {/* Body */}
      <Box maxW="1400px" mx="auto" px={{ base: '16px', md: '32px' }} py="32px">

        {loading && (
          <Flex justify="center" py="80px">
            <Spinner color="#10B981" />
          </Flex>
        )}

        {error && !loading && (
          <Box
            bg="rgba(239,68,68,0.1)"
            border="1px solid rgba(239,68,68,0.3)"
            borderRadius="10px"
            p="20px" mb="28px"
          >
            <Flex align="center" gap="8px" mb="6px">
              <AlertTriangle size={16} color="#EF4444" />
              <Text fontWeight={600} color="#EF4444" fontSize="13px">Cannot load pipeline_status from Appwrite</Text>
            </Flex>
            <Text fontSize="12px" color="rgba(255,255,255,0.5)" fontFamily="monospace">{error}</Text>
            <Text fontSize="11px" color="rgba(255,255,255,0.35)" mt="8px">
              Run: <code>env $(cat .env | xargs) npx tsx scripts/push_pipeline_collections.ts</code>
            </Text>
          </Box>
        )}

        {!loading && (
          <>
            {/* KPI row */}
            <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap="16px" mb="28px">
              <KpiCard
                label="Source" value={total}
                color="#6B7280" icon={<Database size={16} />}
                sub="Total entities"
              />
              <KpiCard
                label="Triaged" value={<AnimatedCounter target={triaged} />}
                color="#3B82F6" icon={<Filter size={16} />}
                sub={`${triage ? Math.round((triaged/total)*100) : 0}% of source`}
              />
              <KpiCard
                label="In-Flight" value={<AnimatedCounter target={inFlight} />}
                color="#F59E0B" icon={<Zap size={16} />}
                sub="Enriching now"
              />
              <KpiCard
                label="Clean" value={<AnimatedCounter target={clean} />}
                color="#10B981" icon={<CheckCircle2 size={16} />}
                sub="Validated + promoted"
              />
              <KpiCard
                label="Pending" value={<AnimatedCounter target={pending} />}
                color="#8B5CF6" icon={<Clock size={16} />}
                sub="Awaiting LLM"
              />
              <KpiCard
                label="Rejected" value={<AnimatedCounter target={rejected} />}
                color="#EF4444" icon={<AlertTriangle size={16} />}
                sub="Failed gates"
              />
            </SimpleGrid>

            {/* Stadium diagram */}
            <Box mb="28px">
              <StadiumDiagram
                total={total}
                triaged={triaged}
                validated={validated}
                rejected={rejected}
                inFlight={inFlight}
              />
            </Box>

            {/* Enrichment info bar */}
            {enrich && (
              <Box
                bg="rgba(245,158,11,0.08)"
                border="1px solid rgba(245,158,11,0.2)"
                borderRadius="10px"
                p="16px" mb="28px"
              >
                <Flex align="center" gap="16px" flexWrap="wrap">
                  <Flex align="center" gap="8px">
                    <Activity size={14} color="#F59E0B" />
                    <Text fontSize="12px" fontWeight={600} color="#F59E0B">Last Enrichment Run</Text>
                  </Flex>
                  <Text fontSize="12px" color="rgba(255,255,255,0.5)">
                    {enrich.selected} entities via <strong style={{ color: '#FAF3E8' }}>{enrich.model}</strong>
                  </Text>
                  <Text fontSize="12px" color="rgba(255,255,255,0.5)">
                    {enrich.elapsedSec}s · exit {enrich.enricherExitCode === 0 ? '✓ 0' : `✗ ${enrich.enricherExitCode}`}
                  </Text>
                  <Text fontSize="12px" color="rgba(255,255,255,0.35)">
                    {fmt(enrich.generatedAt)}
                  </Text>
                </Flex>
              </Box>
            )}

            {/* Reason breakdowns */}
            <SimpleGrid columns={{ base: 1, lg: 2 }} gap="20px" mb="28px">
              {validate && (
                <ReasonTable
                  title="Validate Gate — Deferral Reasons"
                  data={validate.byReason}
                  total={validate.processed}
                  color="#10B981"
                />
              )}
              {triage && (
                <ReasonTable
                  title="Triage Gate — Rejection Reasons"
                  data={triage.byReason}
                  total={triage.scanned}
                  color="#3B82F6"
                />
              )}
            </SimpleGrid>

            {/* Last run timestamps */}
            <Box
              bg="rgba(255,255,255,0.02)"
              border="1px solid rgba(255,255,255,0.07)"
              borderRadius="10px"
              p="20px"
            >
              <Text fontSize="12px" fontWeight={600} color="rgba(255,255,255,0.4)"
                    textTransform="uppercase" letterSpacing="0.08em" mb="14px">
                Gate Run History
              </Text>
              <SimpleGrid columns={{ base: 1, sm: 3 }} gap="16px">
                {[
                  { gate: 'Triage',   time: triage?.generatedAt,   elapsed: triage?.elapsedSec, icon: <Filter size={14} />, color: '#3B82F6' },
                  { gate: 'Validate', time: validate?.generatedAt, elapsed: validate?.elapsedSec, icon: <CheckCircle2 size={14} />, color: '#10B981' },
                  { gate: 'Enrich',   time: enrich?.generatedAt,   elapsed: enrich?.elapsedSec, icon: <TrendingUp size={14} />, color: '#F59E0B' },
                ].map(row => (
                  <Flex key={row.gate} align="flex-start" gap="10px">
                    <Box color={row.color} mt="2px">{row.icon}</Box>
                    <Box>
                      <Text fontSize="12px" fontWeight={600} color="rgba(255,255,255,0.7)">{row.gate}</Text>
                      <Text fontSize="11px" color="rgba(255,255,255,0.35)">{fmt(row.time)}</Text>
                      {row.elapsed != null && (
                        <Text fontSize="10px" color="rgba(255,255,255,0.25)">{row.elapsed}s</Text>
                      )}
                    </Box>
                  </Flex>
                ))}
              </SimpleGrid>
            </Box>

            {/* CLI quick-reference */}
            <Box
              mt="28px"
              bg="rgba(0,0,0,0.3)"
              border="1px solid rgba(255,255,255,0.07)"
              borderRadius="10px"
              p="20px"
            >
              <Text fontSize="12px" fontWeight={600} color="rgba(255,255,255,0.4)"
                    textTransform="uppercase" letterSpacing="0.08em" mb="12px">
                CLI Commands
              </Text>
              {[
                { cmd: 'python3 scripts/pipeline/run_pipeline.py status', desc: 'Print KPI snapshot' },
                { cmd: 'python3 scripts/pipeline/run_pipeline.py full --count 25 --model gemini', desc: 'One full cycle (triage→enrich→validate)' },
                { cmd: 'python3 scripts/pipeline/run_pipeline.py loop --cycles 10 --count 50', desc: '10 repeated cycles, 50 entities each' },
                { cmd: 'npx tsx scripts/push_pipeline_collections.ts', desc: 'Sync clean/rejected files → Appwrite' },
              ].map(row => (
                <Box key={row.cmd} mb="8px">
                  <Text
                    fontSize="11px" fontFamily="'JetBrains Mono',monospace"
                    color="#10B981" display="inline"
                  >
                    {row.cmd}
                  </Text>
                  <Text fontSize="11px" color="rgba(255,255,255,0.3)" display="inline" ml="12px">
                    # {row.desc}
                  </Text>
                </Box>
              ))}
            </Box>
          </>
        )}
      </Box>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; transform: scale(1); }
          50% { opacity: 0.5; transform: scale(1.4); }
        }
      `}</style>
    </Box>
  )
}
