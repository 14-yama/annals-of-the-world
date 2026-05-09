import React, { useEffect, useState, useMemo, useCallback } from 'react'
import { Box, Flex, Text, Input, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, History, Download, Filter, User, Calendar, FileText,
  Activity, GitBranch, AlertTriangle, CheckCircle2, Clock, Pause,
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

const BOT_REPORTS: Array<{ key: string; label: string; file: string; color: string }> = [
  { key: 'stats',          label: 'Stats Counter',  file: 'stats.json',          color: '#4A90D9' },
  { key: 'completeness',   label: 'Completeness',   file: 'completeness.json',   color: '#27AE60' },
  { key: 'orphans',        label: 'Orphans',        file: 'orphans.json',        color: '#E67E22' },
  { key: 'consistency',    label: 'Consistency',    file: 'consistency.json',    color: '#6B3FA0' },
  { key: 'duplicates',     label: 'Duplicates',     file: 'duplicates.json',     color: '#C0392B' },
  { key: 'classification', label: 'Classification', file: 'classification.json', color: '#D4AF37' },
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

  const PAGE_SIZE = 50

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
            border="1px solid #E4E2DC" cursor="pointer">
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

        {/* Bot reports grid */}
        <SimpleGrid columns={{ base: 2, md: 3, lg: 6 }} gap={3}>
          {BOT_REPORTS.map(b => {
            const r = reports[b.key]
            const summary = (r?.summary ?? {}) as Record<string, number | string>
            const headline = Object.entries(summary)[0]
            return (
              <Box key={b.key} p={3} bg="white" border="1px solid #E4E2DC"
                borderLeft={`3px solid ${b.color}`} borderRadius="md">
                <Text fontSize="10px" fontWeight={700} color="#787469"
                  letterSpacing="0.06em" textTransform="uppercase">
                  {b.label}
                </Text>
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
              </Box>
            )
          })}
        </SimpleGrid>
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
          value={logs.length > 0 ? new Date(logs[0].timestamp).toLocaleDateString() : '—'}
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
                        {new Date(row.timestamp).toLocaleString()}
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
                      <Text fontSize="xs" color="#787469">
                        {row.editorId}
                      </Text>
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
