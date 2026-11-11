import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { Box, Flex, Text, Input, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, ChevronRight, History, Download, Filter, User, FileText, Bot,
} from 'lucide-react'
import type { Models } from 'appwrite'
import client, { DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { StatCard } from '../../components/DataCards'
import { formatTrinidadDate, formatTrinidadTimestamp } from '../../lib/localBotsDesk'
import {
  APPWRITE_TOTAL_CAP,
  fetchAuditLogPage,
  fetchAuditLogTotal,
  mapAuditDoc,
  type AuditLogRow,
  type AuditLogTotal,
} from '../../services/auditLogService'

const ACTION_COLORS: Record<string, string> = {
  update: '#4A90D9',
  create: '#27AE60',
  delete: '#C0392B',
  batch_update: '#E67E22',
}

/* ─── EditorBadge — parses editorId into a coloured pill ─── */
function EditorBadge({ editorId }: { editorId: string }) {
  if (!editorId) return <Text fontSize="xs" color="#9E9A90">—</Text>

  const isOllama = editorId.startsWith('ollama/')
  const isCloud = editorId.includes('·cloud·') || editorId.includes('GH#')
  const isLocal = editorId.includes('·local·') && !isOllama
  const isSync = editorId.includes('sync-gateway')
  const isLegacy = editorId.includes('ai-enrichment-bot') || editorId.includes('backfill-significance-bot')
  const isComposer = editorId.startsWith('composer')

  const parts = editorId.split('·')
  const modelPart = parts[0] || editorId
  const ctxPart = parts[2] || ''

  let color = '#787469'
  let bg = 'rgba(120,116,105,0.1)'
  let label = ''
  let detail = ''

  if (isOllama) {
    color = '#27AE60'; bg = 'rgba(39,174,96,0.12)'
    const model = modelPart.replace('ollama/', '')
    label = '🟢 LOCAL'
    detail = `${model}${ctxPart ? ` @ ${ctxPart}` : ''}`
  } else if (isComposer) {
    color = '#E67E22'; bg = 'rgba(230,126,34,0.12)'
    label = '🟡 COMPOSER'
    detail = `${modelPart}${ctxPart ? ` @ ${ctxPart}` : ''}`
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

function formatTotalLabel(info: AuditLogTotal): string {
  const n = info.total.toLocaleString()
  if (info.capped) return `${n}+`
  if (!info.exact) return `≈${n}`
  return n
}

/* ─── Main Component ─── */

export default function AuditLogViewer() {
  const navigate = useNavigate()
  const [logs, setLogs] = useState<AuditLogRow[]>([])
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  const [totalInfo, setTotalInfo] = useState<AuditLogTotal>({
    total: 0, exact: false, capped: false, source: 'unknown', updatedAt: null,
  })
  const [autoRefresh, setAutoRefresh] = useState(true)
  const [hasMore, setHasMore] = useState(false)
  const [cursorStack, setCursorStack] = useState<(string | null)[]>([null])
  const [pageIdx, setPageIdx] = useState(0)

  // Filters
  const [filterEntity, setFilterEntity] = useState('')
  const [filterEditor, setFilterEditor] = useState('')
  const [filterAction, setFilterAction] = useState('')

  const PAGE_SIZE = 50
  const seenIdsRef = useRef<Set<string>>(new Set())
  const pageIdxRef = useRef(0)
  pageIdxRef.current = pageIdx

  const filters = useMemo(() => ({
    entitySlug: filterEntity.trim() || undefined,
    editorId: filterEditor.trim() || undefined,
    action: filterAction || undefined,
  }), [filterEntity, filterEditor, filterAction])

  const loadTotals = useCallback(async () => {
    const info = await fetchAuditLogTotal(filters)
    setTotalInfo(info)
  }, [filters])

  const loadPage = useCallback(async (opts?: { silent?: boolean; cursor?: string | null }) => {
    const silent = opts?.silent ?? false
    if (silent) setRefreshing(true)
    else setLoading(true)
    try {
      const cursor = opts?.cursor ?? null
      const page = await fetchAuditLogPage({
        limit: PAGE_SIZE,
        cursorAfter: cursor,
        ...filters,
      })
      setLogs(page.rows)
      setHasMore(!!page.nextCursor)
      seenIdsRef.current = new Set(page.rows.map(r => r.$id))

      // Filtered views: use query total when uncapped; otherwise keep corpus cache.
      if (filters.entitySlug || filters.editorId || filters.action) {
        setTotalInfo({
          total: page.queryTotal,
          exact: !page.queryCapped,
          capped: page.queryCapped,
          source: 'listDocuments',
          updatedAt: null,
        })
      }
    } catch (err) {
      console.error('Audit log load failed:', err)
      if (!silent) {
        setLogs([])
        setHasMore(false)
      }
    }
    setLoading(false)
    setRefreshing(false)
  }, [filters])

  // Reset cursor stack when filters change
  useEffect(() => {
    setCursorStack([null])
    setPageIdx(0)
    void loadTotals()
    void loadPage({ cursor: null })
  }, [filters, loadTotals, loadPage])

  // Appwrite Realtime — new rows appear instantly on the newest page
  useEffect(() => {
    if (!autoRefresh) return
    const channel = `databases.${DATABASE_ID}.collections.${COLLECTIONS.AUDIT_LOG}.documents`
    const unsubscribe = client.subscribe(channel, (response) => {
      const isCreate = response.events.some((e: string) => e.endsWith('.create'))
      if (!isCreate) return
      const row = mapAuditDoc(response.payload as Models.Document)

      // Respect active filters
      if (filters.entitySlug && !row.entitySlug.toLowerCase().includes(filters.entitySlug.toLowerCase())) return
      if (filters.editorId && row.editorId !== filters.editorId) return
      if (filters.action && row.action !== filters.action) return

      setTotalInfo(prev => ({
        ...prev,
        total: prev.total + 1,
        source: prev.source === 'unknown' ? 'realtime' : prev.source,
      }))

      // Only prepend on the newest page (idx 0)
      if (pageIdxRef.current !== 0) return
      if (seenIdsRef.current.has(row.$id)) return
      seenIdsRef.current.add(row.$id)
      setLogs(prev => [row, ...prev].slice(0, PAGE_SIZE))
    })
    return () => unsubscribe()
  }, [autoRefresh, filters])

  // Backup poll — catches dropped realtime; silent so UI doesn't flash spinner
  useEffect(() => {
    if (!autoRefresh) return
    const id = setInterval(() => {
      if (pageIdxRef.current !== 0) return
      void loadPage({ silent: true, cursor: null })
      void loadTotals()
    }, 8_000)
    return () => clearInterval(id)
  }, [autoRefresh, loadPage, loadTotals])

  function goNext() {
    const last = logs[logs.length - 1]
    if (!last || !hasMore) return
    const nextCursor = last.$id
    const nextStack = cursorStack.slice(0, pageIdx + 1).concat(nextCursor)
    setCursorStack(nextStack)
    setPageIdx(pageIdx + 1)
    void loadPage({ cursor: nextCursor })
  }

  function goPrev() {
    if (pageIdx <= 0) return
    const prevIdx = pageIdx - 1
    const cursor = cursorStack[prevIdx] ?? null
    setPageIdx(prevIdx)
    void loadPage({ cursor })
  }

  const uniqueEditors = useMemo(
    () => [...new Set(logs.map(l => l.editorId).filter(Boolean))],
    [logs],
  )

  function exportCSV() {
    const headers = ['Timestamp (AST)', 'Entity', 'Action', 'Field', 'Old Value', 'New Value', 'Editor', 'Note']
    const rows = logs.map(l => [
      formatTrinidadTimestamp(l.timestamp), l.entitySlug, l.action, l.field,
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

  const totalLabel = formatTotalLabel(totalInfo)
  const totalHint = totalInfo.capped
    ? `Appwrite listDocuments.total caps at ${APPWRITE_TOTAL_CAP.toLocaleString()} (server APP_LIMIT_COUNT) — stats_cache.auditTotal missing; run audit recount`
    : totalInfo.source === 'stats_cache'
      ? `stats_cache.auditTotal (cursor count of audit_log docs)${totalInfo.updatedAt ? ` · ${new Date(totalInfo.updatedAt).toLocaleString()}` : ''}`
      : totalInfo.exact
        ? 'exact filtered count'
        : 'approximate'

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
            {totalLabel} field-level audit rows — not unique entities · America/Port_of_Spain (AST)
            {refreshing ? ' · refreshing…' : ''}
          </Text>
          <Text fontSize="xs" color="#9E9A90" mt={0.5}>
            {totalHint}
            {' · '}one enrich often writes ~5–7 rows (summary + details fields)
          </Text>
        </Box>
        <Box
          as="button" onClick={() => navigate('/curator/bots')}
          px={3} py={2} borderRadius="md" bg="#D4AF3715" border="1px solid #D4AF3740"
          cursor="pointer" display="flex" alignItems="center" gap={2}
          _hover={{ bg: '#D4AF3725' }}
        >
          <Bot size={14} color="#C5963A" />
          <Text fontSize="xs" fontWeight={700} color="#C5963A">Bot KPIs →</Text>
        </Box>
        <Box
          as="button" onClick={() => setAutoRefresh(v => !v)}
          px={3} py={2} borderRadius="md"
          bg={autoRefresh ? '#27AE6020' : '#F5F4F0'}
          color={autoRefresh ? '#27AE60' : '#787469'}
          border="1px solid #E4E2DC" cursor="pointer"
          fontSize="xs" fontWeight={600}
        >
          {autoRefresh ? '● LIVE' : '○ PAUSED'}
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

      {/* Quick Stats — audit_log rows (field-level), not unique entities */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
        <StatCard
          value={totalLabel}
          label={totalInfo.capped ? 'Entries (capped)' : 'Audit rows (field-level)'}
          color="#4A90D9"
        />
        <StatCard
          value={logs.filter(l => l.action === 'update').length.toString()}
          label="Updates (page)" color="#E67E22"
        />
        <StatCard
          value={uniqueEditors.length.toString()}
          label="Active Editors (page)" color="#27AE60"
        />
        <StatCard
          value={logs.length > 0 ? formatTrinidadDate(logs[0].timestamp) : '—'}
          label="Latest Edit (AST)" color="#6B3FA0"
        />
      </SimpleGrid>

      {/* Filters */}
      <Flex gap={3} mb={4} flexWrap="wrap">
        <Flex align="center" gap={2} flex={1} minW="200px">
          <Filter size={14} color="#787469" />
          <Input
            value={filterEntity} onChange={(e) => setFilterEntity(e.target.value)}
            placeholder="Search entity slug…" size="sm"
            bg="white" borderColor="#E4E2DC" _focus={{ borderColor: '#D4AF37' }}
          />
        </Flex>
        <Flex align="center" gap={2} minW="150px">
          <User size={14} color="#787469" />
          <Input
            value={filterEditor} onChange={(e) => setFilterEditor(e.target.value)}
            placeholder="Editor…" size="sm"
            bg="white" borderColor="#E4E2DC" _focus={{ borderColor: '#D4AF37' }}
          />
        </Flex>
        <Flex align="center" gap={2} minW="140px">
          <FileText size={14} color="#787469" />
          <select
            value={filterAction}
            onChange={(e) => setFilterAction(e.target.value)}
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
                      <Text fontSize="xs" fontFamily='"JetBrains Mono", monospace' color="#787469" title={row.timestamp}>
                        {formatTrinidadTimestamp(row.timestamp)}
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

          {/* Cursor pagination — avoids Appwrite offset/total 5k traps */}
          <Flex justify="center" align="center" gap={3} mt={4}>
            <Box
              as="button" onClick={goPrev} disabled={pageIdx <= 0}
              px={3} py={1.5} borderRadius="md" fontSize="sm"
              bg={pageIdx <= 0 ? '#F5F4F0' : '#2D2A24'}
              color={pageIdx <= 0 ? '#9E9A90' : '#D4AF37'}
              cursor={pageIdx <= 0 ? 'default' : 'pointer'}
              display="flex" alignItems="center" gap={1}
              opacity={pageIdx <= 0 ? 0.5 : 1}
            >
              <ChevronLeft size={14} /> Prev
            </Box>
            <Text fontSize="sm" color="#787469">
              Page {pageIdx + 1} · newest-first
            </Text>
            <Box
              as="button" onClick={goNext} disabled={!hasMore}
              px={3} py={1.5} borderRadius="md" fontSize="sm"
              bg={!hasMore ? '#F5F4F0' : '#2D2A24'}
              color={!hasMore ? '#9E9A90' : '#D4AF37'}
              cursor={!hasMore ? 'default' : 'pointer'}
              display="flex" alignItems="center" gap={1}
              opacity={!hasMore ? 0.5 : 1}
            >
              Next <ChevronRight size={14} />
            </Box>
          </Flex>
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
