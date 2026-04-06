import React, { useEffect, useState, useMemo } from 'react'
import { Box, Flex, Text, SimpleGrid, Spinner, Input } from '@chakra-ui/react'
import { Link as RouterLink } from 'react-router-dom'
import {
  AlertTriangle,
  CheckCircle2,
  Clock,
  Filter,
  RefreshCw,
  ChevronRight,
} from 'lucide-react'
import { Query, type Models } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../../lib/appwrite'
import { StatCard, SectionHeading } from '../../components/DataCards'

/* ─── Types ─── */

type TaskStatus = 'pending' | 'in-progress' | 'resolved' | 'deferred'
type TaskPriority = 'critical' | 'high' | 'medium' | 'low'

interface AuditTask {
  id: string
  title: string
  description: string
  category: string
  priority: TaskPriority
  status: TaskStatus
  affectedCount: number
  affectedSlugs: string[]
}

/* ─── Priority & Status Config ─── */

const PRIORITY_COLORS: Record<TaskPriority, { bg: string; fg: string }> = {
  critical: { bg: '#FADBD8', fg: '#922B21' },
  high:     { bg: '#FDEBD0', fg: '#B9770E' },
  medium:   { bg: '#FEF9E7', fg: '#7D6608' },
  low:      { bg: '#EAFAF1', fg: '#1E8449' },
}

const STATUS_LABELS: Record<TaskStatus, { label: string; color: string }> = {
  'pending':     { label: 'Pending', color: '#E67E22' },
  'in-progress': { label: 'In Progress', color: '#3498DB' },
  'resolved':    { label: 'Resolved', color: '#27AE60' },
  'deferred':    { label: 'Deferred', color: '#95A5A6' },
}

/* ─── Main Component ─── */

export default function TriageSystem() {
  const [tasks, setTasks] = useState<AuditTask[]>([])
  const [loading, setLoading] = useState(true)
  const [running, setRunning] = useState(false)
  const [filterStatus, setFilterStatus] = useState<TaskStatus | 'all'>('all')
  const [filterPriority, setFilterPriority] = useState<TaskPriority | 'all'>('all')

  useEffect(() => { runAudit() }, [])

  async function runAudit() {
    setRunning(true)
    setLoading(true)
    try {
      const generatedTasks: AuditTask[] = []
      let taskId = 0

      // ── Audit 1: Orphan Entities (0 relationships) ──
      const orphanSample = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.limit(200),
      ])
      const orphanSlugs: string[] = []
      for (const doc of orphanSample.documents) {
        const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
        if ((details.relationships ?? []).length === 0) {
          orphanSlugs.push(doc.slug as string)
        }
      }
      if (orphanSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Orphan Entities — No Relationships',
          description: `${orphanSlugs.length} entities (from 200 sample) have zero relationship edges. These are disconnected from the knowledge graph.`,
          category: 'relationships',
          priority: 'critical',
          status: 'pending',
          affectedCount: orphanSlugs.length,
          affectedSlugs: orphanSlugs.slice(0, 20),
        })
      }

      // ── Audit 2: Missing Images ──
      const noImage = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.equal('label', 'Person'),
        Query.limit(200),
      ])
      const noImageSlugs = noImage.documents
        .filter((d) => !d.imageUrl)
        .map((d) => d.slug as string)
      if (noImageSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'People Missing Images',
          description: `${noImageSlugs.length} Person entities (from 200 sample) have no imageUrl. Visual representation enhances entity pages.`,
          category: 'image',
          priority: 'high',
          status: 'pending',
          affectedCount: noImageSlugs.length,
          affectedSlugs: noImageSlugs.slice(0, 20),
        })
      }

      // ── Audit 3: Low Quality Score ──
      const lowScoreSlugs: string[] = []
      for (const doc of orphanSample.documents) {
        const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
        const rels = (details.relationships ?? []).length
        const causes = (details.causes ?? []).length
        const effects = (details.effects ?? []).length
        const frameworks = ((doc.frameworks as string[]) ?? []).length
        const total = (rels > 0 ? 1 : 0) + (causes > 0 ? 1 : 0) + (effects > 0 ? 1 : 0) + (frameworks > 0 ? 1 : 0)
        if (total <= 1 && (doc.importanceScore as number ?? 0) >= 3) {
          lowScoreSlugs.push(doc.slug as string)
        }
      }
      if (lowScoreSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Important Entities — Very Low Completeness',
          description: `${lowScoreSlugs.length} entities have importanceScore ≥ 3 but fewer than 2 quality dimensions populated.`,
          category: 'completeness',
          priority: 'high',
          status: 'pending',
          affectedCount: lowScoreSlugs.length,
          affectedSlugs: lowScoreSlugs.slice(0, 20),
        })
      }

      // ── Audit 4: Short Summaries ──
      const shortSumSlugs = orphanSample.documents
        .filter((d) => ((d.summary as string) ?? '').length < 50)
        .map((d) => d.slug as string)
      if (shortSumSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Entities with Short/Missing Summaries',
          description: `${shortSumSlugs.length} entities have summaries shorter than 50 characters. Enriched summaries improve entity pages.`,
          category: 'summary',
          priority: 'medium',
          status: 'pending',
          affectedCount: shortSumSlugs.length,
          affectedSlugs: shortSumSlugs.slice(0, 20),
        })
      }

      // ── Audit 5: Missing Wikidata QID ──
      const noQidSlugs = orphanSample.documents
        .filter((d) => !d.wikidataQid)
        .map((d) => d.slug as string)
      if (noQidSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Entities Missing Wikidata QID',
          description: `${noQidSlugs.length} entities have no wikidataQid. Wikidata linkage enables future verification.`,
          category: 'wikidata',
          priority: 'low',
          status: 'pending',
          affectedCount: noQidSlugs.length,
          affectedSlugs: noQidSlugs.slice(0, 20),
        })
      }

      // ── Audit 6: Empty Frameworks ──
      const noFwSlugs = orphanSample.documents
        .filter((d) => ((d.frameworks as string[]) ?? []).length === 0)
        .map((d) => d.slug as string)
      if (noFwSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Entities Missing Interpretive Frameworks',
          description: `${noFwSlugs.length} entities have no assigned frameworks. Every entity should have at least one.`,
          category: 'frameworks',
          priority: 'medium',
          status: 'pending',
          affectedCount: noFwSlugs.length,
          affectedSlugs: noFwSlugs.slice(0, 20),
        })
      }

      // ── Audit 7: Era/Division Consistency ──
      const noDiv = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
        Query.equal('eraDivisionCode', ''),
        Query.limit(1),
      ])
      if (noDiv.total > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Entities Missing Era Division Code',
          description: `${noDiv.total} entities have an empty eraDivisionCode. All entities must be assigned to a division.`,
          category: 'era',
          priority: 'critical',
          status: 'pending',
          affectedCount: noDiv.total,
          affectedSlugs: noDiv.documents.map((d) => d.slug as string),
        })
      }

      // ── Audit 8: Missing Causes/Effects ──
      const noCausesSlugs: string[] = []
      for (const doc of orphanSample.documents) {
        const details = doc.detailsJson ? JSON.parse(doc.detailsJson as string) : {}
        if ((details.causes ?? []).length === 0 && (details.effects ?? []).length === 0) {
          noCausesSlugs.push(doc.slug as string)
        }
      }
      if (noCausesSlugs.length > 0) {
        generatedTasks.push({
          id: `task-${++taskId}`,
          title: 'Entities with No Causal Chain',
          description: `${noCausesSlugs.length} entities have neither causes nor effects. The causal chain is a core differentiator.`,
          category: 'causality',
          priority: 'medium',
          status: 'pending',
          affectedCount: noCausesSlugs.length,
          affectedSlugs: noCausesSlugs.slice(0, 20),
        })
      }

      setTasks(generatedTasks)
    } catch (err) {
      console.error('Triage audit failed:', err)
    }
    setLoading(false)
    setRunning(false)
  }

  const filteredTasks = useMemo(() => {
    return tasks.filter((t) => {
      if (filterStatus !== 'all' && t.status !== filterStatus) return false
      if (filterPriority !== 'all' && t.priority !== filterPriority) return false
      return true
    })
  }, [tasks, filterStatus, filterPriority])

  const totalAffected = useMemo(() => tasks.reduce((s, t) => s + t.affectedCount, 0), [tasks])

  function updateTaskStatus(taskId: string, status: TaskStatus) {
    setTasks((prev) => prev.map((t) => (t.id === taskId ? { ...t, status } : t)))
  }

  if (loading) {
    return (
      <Flex justify="center" align="center" minH="60vh">
        <Spinner size="xl" color="#D4AF37" />
        <Text ml={4} color="#787469">Running automated audit checks…</Text>
      </Flex>
    )
  }

  return (
    <Box maxW="1400px" mx="auto" p={6}>
      {/* Hero */}
      <Flex justify="space-between" align="center" mb={8}>
        <Box>
          <Text fontFamily='"Cinzel", serif' fontSize="2xl" fontWeight={700} color="#2D2A24" letterSpacing="0.08em">
            TRIAGE SYSTEM
          </Text>
          <Text color="#787469" fontSize="sm" mt={1}>
            Automated audit checks — {tasks.length} tasks, {totalAffected} affected entities
          </Text>
        </Box>
        <Box
          as="button"
          onClick={runAudit}
          px={4}
          py={2}
          borderRadius="md"
          bg="#2D2A24"
          color="#D4AF37"
          fontSize="sm"
          fontWeight={600}
          display="flex"
          alignItems="center"
          gap={2}
          cursor="pointer"
          opacity={running ? 0.6 : 1}
          _hover={{ opacity: 0.8 }}
        >
          <RefreshCw size={14} className={running ? 'animate-spin' : ''} />
          Re-run Audit
        </Box>
      </Flex>

      {/* Summary Stats */}
      <SimpleGrid columns={{ base: 2, md: 4 }} gap={4} mb={8}>
        <StatCard value={tasks.filter((t) => t.priority === 'critical').length.toString()} label="Critical" color="#C0392B" />
        <StatCard value={tasks.filter((t) => t.priority === 'high').length.toString()} label="High Priority" color="#E67E22" />
        <StatCard value={tasks.filter((t) => t.priority === 'medium').length.toString()} label="Medium" color="#F1C40F" />
        <StatCard value={tasks.filter((t) => t.status === 'resolved').length.toString()} label="Resolved" color="#27AE60" />
      </SimpleGrid>

      {/* Filters */}
      <Flex gap={3} mb={6} flexWrap="wrap">
        <Text fontSize="sm" color="#787469" fontWeight={600} alignSelf="center">Filter:</Text>
        {(['all', 'pending', 'in-progress', 'resolved', 'deferred'] as const).map((s) => (
          <FilterChip key={s} active={filterStatus === s} onClick={() => setFilterStatus(s)} label={s === 'all' ? 'All Status' : STATUS_LABELS[s as TaskStatus]?.label ?? s} />
        ))}
        <Box w="1px" bg="#E4E2DC" mx={1} />
        {(['all', 'critical', 'high', 'medium', 'low'] as const).map((p) => (
          <FilterChip key={p} active={filterPriority === p} onClick={() => setFilterPriority(p)} label={p === 'all' ? 'All Priority' : p.charAt(0).toUpperCase() + p.slice(1)} />
        ))}
      </Flex>

      {/* Task List */}
      {filteredTasks.map((task) => (
        <Box
          key={task.id}
          bg="#FAFAF8"
          border="1px solid #E4E2DC"
          borderRadius="lg"
          p={5}
          mb={3}
          position="relative"
          overflow="hidden"
          transition="all 0.2s"
          _hover={{ borderColor: '#D4AF37' }}
        >
          <Box
            position="absolute"
            top={0}
            left={0}
            w="4px"
            h="100%"
            bg={PRIORITY_COLORS[task.priority].fg}
          />

          <Flex justify="space-between" align="start" mb={3}>
            <Box flex={1}>
              <Flex align="center" gap={2} mb={1}>
                <Box px={2} py={0.5} borderRadius="md" fontSize="10px" fontWeight={700}
                  bg={PRIORITY_COLORS[task.priority].bg} color={PRIORITY_COLORS[task.priority].fg}
                  textTransform="uppercase" letterSpacing="0.08em">
                  {task.priority}
                </Box>
                <Box px={2} py={0.5} borderRadius="md" fontSize="10px" fontWeight={600}
                  bg={STATUS_LABELS[task.status].color + '20'} color={STATUS_LABELS[task.status].color}>
                  {STATUS_LABELS[task.status].label}
                </Box>
                <Text fontSize="xs" color="#9E9A90">{task.category}</Text>
              </Flex>
              <Text fontFamily='"Cormorant Garamond", serif' fontSize="lg" fontWeight={700} color="#2D2A24">
                {task.title}
              </Text>
              <Text fontSize="sm" color="#787469" mt={1}>{task.description}</Text>
            </Box>
            <Text fontFamily='"Cinzel", serif' fontSize="xl" fontWeight={700} color="#C0392B" ml={4}>
              {task.affectedCount}
            </Text>
          </Flex>

          {/* Affected entities sample */}
          {task.affectedSlugs.length > 0 && (
            <Box mt={3} pt={3} borderTop="1px solid #EEEDEA">
              <Text fontSize="xs" color="#9E9A90" mb={2} fontWeight={600}>
                Affected entities (sample):
              </Text>
              <Flex gap={2} flexWrap="wrap">
                {task.affectedSlugs.map((slug) => (
                  <RouterLink key={slug} to={`/entity/${slug}`} style={{ textDecoration: 'none' }}>
                    <Box as="span" px={2} py={0.5} borderRadius="md" fontSize="11px"
                      bg="#E8F0FE" color="#1A5276" cursor="pointer"
                      _hover={{ bg: '#D4E6F1' }}
                      transition="all 0.2s">
                      {slug}
                    </Box>
                  </RouterLink>
                ))}
              </Flex>
            </Box>
          )}

          {/* Status actions */}
          <Flex gap={2} mt={3} pt={3} borderTop="1px solid #EEEDEA">
            {task.status !== 'resolved' && (
              <ActionBtn label="Mark Resolved" color="#27AE60" onClick={() => updateTaskStatus(task.id, 'resolved')} />
            )}
            {task.status === 'pending' && (
              <ActionBtn label="Start Working" color="#3498DB" onClick={() => updateTaskStatus(task.id, 'in-progress')} />
            )}
            {task.status !== 'deferred' && task.status !== 'resolved' && (
              <ActionBtn label="Defer" color="#95A5A6" onClick={() => updateTaskStatus(task.id, 'deferred')} />
            )}
            {task.status === 'resolved' && (
              <ActionBtn label="Reopen" color="#E67E22" onClick={() => updateTaskStatus(task.id, 'pending')} />
            )}
          </Flex>
        </Box>
      ))}

      {filteredTasks.length === 0 && (
        <Flex direction="column" align="center" justify="center" py={12} color="#9E9A90">
          <CheckCircle2 size={48} />
          <Text mt={4} fontSize="lg" fontWeight={600}>All clear!</Text>
          <Text fontSize="sm">No tasks match your filter criteria.</Text>
        </Flex>
      )}
    </Box>
  )
}

/* ─── Sub-components ─── */

function FilterChip({ active, onClick, label }: { active: boolean; onClick: () => void; label: string }) {
  return (
    <Box
      as="button"
      onClick={onClick}
      px={3}
      py={1.5}
      borderRadius="full"
      fontSize="xs"
      fontWeight={600}
      bg={active ? '#2D2A24' : '#F5F4F0'}
      color={active ? '#D4AF37' : '#787469'}
      border="1px solid"
      borderColor={active ? '#2D2A24' : '#E4E2DC'}
      cursor="pointer"
      transition="all 0.2s"
      _hover={{ borderColor: '#D4AF37' }}
    >
      {label}
    </Box>
  )
}

function ActionBtn({ label, color, onClick }: { label: string; color: string; onClick: () => void }) {
  return (
    <Box
      as="button"
      onClick={onClick}
      px={3}
      py={1}
      borderRadius="md"
      fontSize="xs"
      fontWeight={600}
      bg={color + '15'}
      color={color}
      cursor="pointer"
      transition="all 0.2s"
      _hover={{ bg: color + '25' }}
    >
      {label}
    </Box>
  )
}
