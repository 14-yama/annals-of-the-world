import React, { useEffect, useState, useMemo } from 'react'
import { Box, Flex, Text, Input, Spinner, SimpleGrid } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import {
  ChevronLeft, History, Download, Filter, User, FileText, Bot,
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

/* ─── Main Component ─── */

export default function AuditLogViewer() {
  const navigate = useNavigate()
  const [logs, setLogs] = useState<AuditRow[]>([])
  const [loading, setLoading] = useState(true)
  const [total, setTotal] = useState(0)
  const [page, setPage] = useState(0)
  const [autoRefresh, setAutoRefresh] = useState(true)

  // Filters
  const [filterEntity, setFilterEntity] = useState('')
  const [filterEditor, setFilterEditor] = useState('')
  const [filterAction, setFilterAction] = useState('')

  const PAGE_SIZE = 50

  useEffect(() => { loadLogs() }, [page, filterEntity, filterEditor, filterAction])

  // Appwrite Realtime — new rows appear instantly
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

  // Backup poll — catches dropped realtime connection
  useEffect(() => {
    if (!autoRefresh) return
    const id = setInterval(loadLogs, 30_000)
    return () => clearInterval(id)
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

  const uniqueEditors = useMemo(
    () => [...new Set(logs.map(l => l.editorId).filter(Boolean))],
    [logs],
  )

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

      {/* Quick Stats — only about the audit log itself */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
        <StatCard value={total.toLocaleString()} label="Total Entries" color="#4A90D9" />
        <StatCard
          value={logs.filter(l => l.action === 'update').length.toString()}
          label="Updates (page)" color="#E67E22"
        />
        <StatCard
          value={uniqueEditors.length.toString()}
          label="Active Editors (page)" color="#27AE60"
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
