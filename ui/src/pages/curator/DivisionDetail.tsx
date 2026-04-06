import React, { useEffect, useState, useMemo, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner, Input, Textarea } from '@chakra-ui/react'
import { Link as RouterLink, useParams, useNavigate } from 'react-router-dom'
import {
  ChevronLeft,
  Pencil,
  ExternalLink,
  Save,
  X,
  ChevronDown,
  ChevronUp,
} from 'lucide-react'
import { Query, type Models } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { SectionHeading, StatCard } from '../../components/DataCards'
import { DIVISIONS } from '../../constants/callNumbers'

/* ─── Types ─── */

interface EntityRow {
  $id: string
  slug: string
  name: string
  era: string
  eraDivisionCode: string
  importanceScore: number
  summary: string
  imageUrl: string
  wikidataQid: string
  relCount: number
  causeCount: number
  effectCount: number
  frameworks: string[]
  score: number
}

type SortField = 'name' | 'era' | 'importanceScore' | 'score' | 'relCount'
type SortDir = 'asc' | 'desc'

/* ─── Main Component ─── */

export default function DivisionDetail() {
  const { div } = useParams<{ div: string }>()
  const navigate = useNavigate()

  const [entities, setEntities] = useState<EntityRow[]>([])
  const [total, setTotal] = useState(0)
  const [loading, setLoading] = useState(true)
  const [page, setPage] = useState(0)
  const [sortField, setSortField] = useState<SortField>('importanceScore')
  const [sortDir, setSortDir] = useState<SortDir>('desc')

  // Quick edit state
  const [editingId, setEditingId] = useState<string | null>(null)
  const [editSlug, setEditSlug] = useState('')
  const [editSummary, setEditSummary] = useState('')
  const [saving, setSaving] = useState(false)

  const divisionInfo = useMemo(
    () => DIVISIONS.find((d) => d.code === div),
    [div],
  )

  const PAGE_SIZE = 50

  useEffect(() => {
    loadEntities()
  }, [div, page])

  async function loadEntities() {
    if (!div) return
    setLoading(true)
    try {
      const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.startsWith('callNumber', div + '.'),
        Query.limit(PAGE_SIZE),
        Query.offset(page * PAGE_SIZE),
      ])
      setTotal(res.total)
      setEntities(res.documents.map(mapToRow))
    } catch (err) {
      console.error('Division load failed:', err)
    }
    setLoading(false)
  }

  function mapToRow(doc: Models.Document): EntityRow {
    const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
    const rels = details.relationships ?? []
    const causes = details.causes ?? []
    const effects = details.effects ?? []
    let score = 0
    if (rels.length > 0) score++
    if (causes.length > 0) score++
    if (effects.length > 0) score++
    if (((doc.frameworks as string[]) ?? []).length > 0) score++
    if ((details.places ?? []).length > 0) score++
    if ((details.texts ?? []).length > 0) score++
    if (doc.imageUrl) score++
    if (doc.wikidataQid) score++
    if (((doc.summary as string) ?? '').length >= 50) score++
    return {
      $id: doc.$id,
      slug: doc.slug as string,
      name: doc.name as string,
      era: doc.era as string,
      eraDivisionCode: doc.eraDivisionCode as string,
      importanceScore: (doc.importanceScore as number) ?? 0,
      summary: (doc.summary as string) ?? '',
      imageUrl: (doc.imageUrl as string) ?? '',
      wikidataQid: (doc.wikidataQid as string) ?? '',
      relCount: rels.length,
      causeCount: causes.length,
      effectCount: effects.length,
      frameworks: (doc.frameworks as string[]) ?? [],
      score,
    }
  }

  const sorted = useMemo(() => {
    return [...entities].sort((a, b) => {
      const av = a[sortField]
      const bv = b[sortField]
      if (typeof av === 'string' && typeof bv === 'string') {
        return sortDir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av)
      }
      return sortDir === 'asc' ? (av as number) - (bv as number) : (bv as number) - (av as number)
    })
  }, [entities, sortField, sortDir])

  function toggleSort(field: SortField) {
    if (sortField === field) {
      setSortDir((d) => (d === 'asc' ? 'desc' : 'asc'))
    } else {
      setSortField(field)
      setSortDir('desc')
    }
  }

  function startEdit(row: EntityRow) {
    setEditingId(row.$id)
    setEditSlug(row.slug)
    setEditSummary(row.summary)
  }

  async function saveEdit() {
    if (!editingId) return
    setSaving(true)
    try {
      await databases.updateDocument(DATABASE_ID, COLLECTIONS.ENTITIES, editingId, {
        summary: editSummary,
      })
      setEntities((prev) =>
        prev.map((e) => (e.$id === editingId ? { ...e, summary: editSummary } : e)),
      )
      setEditingId(null)
    } catch (err) {
      console.error('Save failed:', err)
    }
    setSaving(false)
  }

  const pageCount = Math.ceil(total / PAGE_SIZE)

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      {/* Header */}
      <Flex align="center" gap={3} mb={6}>
        <Box
          as="button"
          onClick={() => navigate('/curator/people')}
          p={2}
          borderRadius="md"
          bg="#F5F4F0"
          cursor="pointer"
          _hover={{ bg: '#E4E2DC' }}
        >
          <ChevronLeft size={18} color="#787469" />
        </Box>
        <Box>
          <Text fontFamily='"JetBrains Mono", monospace' fontSize="sm" color="#D4AF37" fontWeight={600}>
            Division {div}
          </Text>
          <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#2D2A24">
            {divisionInfo?.heading ?? `Division ${div}`}
          </Text>
          <Text fontSize="sm" color="#787469">
            {total.toLocaleString()} entities
          </Text>
        </Box>
      </Flex>

      {/* Quick stats */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={6}>
        <StatCard value={total.toLocaleString()} label="Total" color="#4A90D9" />
        <StatCard
          value={entities.filter((e) => e.score >= 7).length.toString()}
          label="High Quality"
          detail="Score 7+"
          color="#27AE60"
        />
        <StatCard
          value={entities.filter((e) => e.relCount === 0).length.toString()}
          label="Orphans"
          detail="0 relationships"
          color="#C0392B"
        />
        <StatCard
          value={entities.filter((e) => !e.imageUrl).length.toString()}
          label="No Image"
          color="#E67E22"
        />
      </SimpleGrid>

      {/* Inline edit drawer */}
      {editingId && (
        <Box bg="#FEF9E7" border="1px solid #F1C40F" borderRadius="lg" p={5} mb={6}>
          <Flex justify="space-between" align="center" mb={3}>
            <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
              Quick Edit — {editSlug}
            </Text>
            <Flex gap={2}>
              <Box as="button" onClick={saveEdit} px={3} py={1.5} borderRadius="md" bg="#27AE60" color="white"
                fontSize="xs" fontWeight={600} display="flex" alignItems="center" gap={1} cursor="pointer"
                opacity={saving ? 0.6 : 1}>
                <Save size={12} /> Save
              </Box>
              <Box as="button" onClick={() => setEditingId(null)} px={3} py={1.5} borderRadius="md"
                bg="#F5F4F0" color="#787469" fontSize="xs" fontWeight={600} display="flex" alignItems="center"
                gap={1} cursor="pointer">
                <X size={12} /> Cancel
              </Box>
            </Flex>
          </Flex>
          <Text fontSize="xs" color="#787469" mb={1} fontWeight={600}>Summary</Text>
          <Textarea
            value={editSummary}
            onChange={(e) => setEditSummary(e.target.value)}
            rows={4}
            bg="white"
            borderColor="#E4E2DC"
            fontSize="sm"
            _focus={{ borderColor: '#D4AF37' }}
          />
          <Flex mt={2} gap={2}>
            <RouterLink to={`/entity/${editSlug}`} style={{ textDecoration: 'none' }}>
              <Box as="span" fontSize="xs" color="#4A90D9" display="flex" alignItems="center" gap={1}>
                <ExternalLink size={10} /> View Entity Page
              </Box>
            </RouterLink>
          </Flex>
        </Box>
      )}

      {/* Table */}
      {loading ? (
        <Flex justify="center" py={12}>
          <Spinner size="lg" color="#D4AF37" />
        </Flex>
      ) : (
        <>
          <Box bg="#FAFAF8" border="1px solid #E4E2DC" borderRadius="lg" overflow="auto">
            <table style={{ width: '100%', borderCollapse: 'collapse', minWidth: '900px' }}>
              <thead>
                <tr>
                  <SortTh label="Name" field="name" current={sortField} dir={sortDir} onSort={toggleSort} />
                  <SortTh label="Era" field="era" current={sortField} dir={sortDir} onSort={toggleSort} />
                  <SortTh label="Importance" field="importanceScore" current={sortField} dir={sortDir} onSort={toggleSort} />
                  <SortTh label="Score" field="score" current={sortField} dir={sortDir} onSort={toggleSort} />
                  <SortTh label="Rels" field="relCount" current={sortField} dir={sortDir} onSort={toggleSort} />
                  <th style={thStyle}>Image</th>
                  <th style={thStyle}>Wikidata</th>
                  <th style={thStyle}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {sorted.map((row, ri) => (
                  <tr key={row.$id} style={{ backgroundColor: ri % 2 === 0 ? '#FAFAF8' : '#F5F4F0' }}>
                    <td style={tdStyle}>
                      <RouterLink to={`/entity/${row.slug}`} style={{ color: '#4A90D9', textDecoration: 'none' }}>
                        {row.name}
                      </RouterLink>
                    </td>
                    <td style={tdStyle}>{row.era}</td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>{row.importanceScore}</td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>
                      <ScoreBadge score={row.score} />
                    </td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>{row.relCount}</td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>
                      {row.imageUrl ? '✓' : <Text as="span" color="#C0392B">✗</Text>}
                    </td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>
                      {row.wikidataQid ? (
                        <Text as="span" fontFamily='"JetBrains Mono", monospace' fontSize="10px" color="#4A90D9">
                          {row.wikidataQid}
                        </Text>
                      ) : (
                        <Text as="span" color="#C0392B">—</Text>
                      )}
                    </td>
                    <td style={{ ...tdStyle, textAlign: 'center' }}>
                      <Flex gap={1} justify="center">
                        <Box as="button" p={1} borderRadius="sm" _hover={{ bg: '#F5F4F0' }}
                          cursor="pointer" onClick={() => startEdit(row)}>
                          <Pencil size={14} color="#787469" />
                        </Box>
                      </Flex>
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
                  key={i}
                  as="button"
                  onClick={() => setPage(i)}
                  px={3}
                  py={1.5}
                  borderRadius="md"
                  fontSize="sm"
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

/* ─── Sub-components ─── */

function SortTh({ label, field, current, dir, onSort }: {
  label: string; field: SortField; current: SortField; dir: SortDir; onSort: (f: SortField) => void
}) {
  const active = current === field
  return (
    <th style={{ ...thStyle, cursor: 'pointer', userSelect: 'none' }} onClick={() => onSort(field)}>
      <Flex align="center" gap={1} display="inline-flex">
        {label}
        {active && (dir === 'asc' ? <ChevronUp size={12} /> : <ChevronDown size={12} />)}
      </Flex>
    </th>
  )
}

function ScoreBadge({ score }: { score: number }) {
  return (
    <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="xs" fontWeight={700}
      bg={score >= 7 ? '#D5F5E3' : score >= 4 ? '#FEF9E7' : '#FADBD8'}
      color={score >= 7 ? '#196F3D' : score >= 4 ? '#7D6608' : '#922B21'}>
      {score}/9
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
