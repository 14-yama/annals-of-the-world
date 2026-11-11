/**
 * Schedule view for Annals com.annals.* bots — mirrors Caricom Superstack
 * LocalBotsTimetablePage: color legend, status/lane filters, 24-hour bars, one card per bot.
 */
import { useMemo, useState } from 'react'
import { Box, Button, Flex, Heading, HStack, Text, VStack } from '@chakra-ui/react'
import { useNavigate } from 'react-router-dom'
import { ChevronLeft, CalendarClock } from 'lucide-react'
import {
  chipTone,
  cronOf,
  describeCron,
  hourLabel,
  hoursForCron,
  laneLabel,
  portOfSpainHour,
  posTime,
  statusWords,
  timetableChip,
  useLocalBotDesk,
  type AnnalsBot,
} from '../../lib/localBotsDesk'

export default function LocalBotsTimetable() {
  const navigate = useNavigate()
  const [statusFilter, setStatusFilter] = useState('all')
  const [laneFilter, setLaneFilter] = useState('all')
  const [selectedHour, setSelectedHour] = useState(portOfSpainHour)
  const {
    bots, lanes, runningByBot, lastFinishedByBot, kpiByBot, kpi, activityError,
  } = useLocalBotDesk()

  const visible = bots.filter((bot) => {
    if (statusFilter !== 'all' && bot.status !== statusFilter) return false
    if (laneFilter !== 'all' && bot.lane !== laneFilter) return false
    return true
  })

  const timetable = [...visible].sort((a, b) => {
    const aCron = cronOf(a)
    const bCron = cronOf(b)
    return describeCron(aCron).sort - describeCron(bCron).sort
  })

  const dayBars = useMemo(() => {
    const slots = Array.from({ length: 24 }, (_, hour) => ({
      hour,
      enabled: [] as string[],
      waiting: [] as string[],
    }))
    for (const bot of timetable) {
      const cron = cronOf(bot)
      if (!cron) continue
      const on = bot.schedule?.enabled !== false
      for (const hour of hoursForCron(cron)) {
        const names = on ? slots[hour].enabled : slots[hour].waiting
        if (!names.includes(bot.name)) names.push(bot.name)
      }
    }
    return slots
  }, [timetable])

  const busiest = dayBars.reduce((max, slot) => Math.max(max, slot.enabled.length + slot.waiting.length), 1)
  const selected = dayBars[selectedHour] ?? dayBars[0]
  const nowHour = portOfSpainHour()

  function chipFor(bot: AnnalsBot): string {
    const cron = cronOf(bot)
    const enabled = bot.schedule?.enabled !== false && Boolean(cron || bot.schedule?.kind === 'keepalive')
    const running = runningByBot.has(bot.id) || runningByBot.has(bot.id === 'push' ? 'git-push' : bot.id)
    const kpiRow = kpiByBot.get(bot.id)
    const last = lastFinishedByBot.get(bot.id) || lastFinishedByBot.get(bot.id === 'push' ? 'git-push' : bot.id)
    const hasReport = Boolean(last || kpiRow?.lastJobFinished || kpiRow?.lastLogAt)
    return timetableChip(enabled, running, hasReport)
  }

  return (
    <Box maxW="1100px" mx="auto" p={6} minH="100vh" bg="#FAF9F6">
      <VStack align="stretch" gap={8}>
        <Flex align="center" gap={3}>
          <Box
            as="button" onClick={() => navigate('/curator/bots')}
            p={2} borderRadius="md" bg="#F5F4F0" cursor="pointer" _hover={{ bg: '#E4E2DC' }}
          >
            <ChevronLeft size={18} color="#787469" />
          </Box>
          <Box p={2} borderRadius="md" bg="#6B3FA020">
            <CalendarClock size={22} color="#6B3FA0" />
          </Box>
          <Box flex={1}>
            <Text fontSize="xs" letterSpacing="0.14em" textTransform="uppercase" color="#787469">
              Curator desk
            </Text>
            <Heading size="lg" color="#2D2A24" mt={1} fontFamily='"Cinzel", serif'>
              Bot timetable
            </Heading>
            <Text color="#787469" mt={2} maxW="720px" fontSize="sm">
              Times are Port of Spain. Each card is one <Text as="span" fontFamily="mono" fontSize="xs">com.annals.*</Text> bot
              and the clock it keeps. Live assist stays on Bot KPI / Ollama Monitor.
            </Text>
          </Box>
          <HStack gap={2}>
            <Button size="sm" variant="outline" onClick={() => navigate('/curator/bots')}>KPI</Button>
            <Button size="sm" variant="outline" onClick={() => navigate('/curator/ollama')}>Ollama</Button>
          </HStack>
        </Flex>

        <Box bg="white" borderWidth="1px" borderColor="#E4E2DC" borderRadius="xl" p={4}>
          <Heading size="sm" color="#2D2A24" mb={3}>How to read a card</Heading>
          <VStack align="stretch" gap={2}>
            {[
              ['#E67E22', 'Active now.', 'A visit is running. The card names the job.'],
              ['#27AE60', 'Last run finished.', 'A report is on disk. The bot is not running at this moment.'],
              ['#6B3FA0', 'Scheduled.', 'The job is turned on. Nothing is running at this moment.'],
              ['#9E9A90', 'Waiting.', 'The bot is declared, and the job is turned off.'],
            ].map(([color, title, body]) => (
              <HStack key={title} align="start" gap={3}>
                <Box w="10px" h="10px" mt="6px" borderRadius="full" bg={color} flexShrink={0} />
                <Text color="#2D2A24" fontSize="sm">
                  <Text as="span" fontWeight="bold">{title}</Text> {body}
                </Text>
              </HStack>
            ))}
          </VStack>
          {kpi?.updatedAt ? (
            <Text mt={3} fontSize="xs" color="#9E9A90">
              Local KPI roster updated {posTime(kpi.updatedAt)} · {bots.length} bots in arsenal
              {activityError ? ' · live job feed offline' : ''}
            </Text>
          ) : null}
        </Box>

        {kpi?.enrichLive || kpi?.parallelCapacity ? (
          <Box bg="white" borderWidth="1px" borderColor="#E4E2DC" borderRadius="xl" p={4}>
            <Heading size="sm" color="#2D2A24" mb={1}>Enrichment desk</Heading>
            <Text color="#787469" fontSize="sm" mb={3}>
              {kpi.enrichLive?.enrichBotsLive ?? 0} live / {kpi.enrichLive?.enrichBotsConfigured ?? 0} configured
              {' · '}
              {(kpi.enrichLive?.ratePerHour ?? 0).toLocaleString()} entities/hr
              {' · '}
              max LLM parallel {kpi.parallelCapacity?.effectiveLlmParallel
                ?? kpi.parallelCapacity?.maxConcurrentLlm
                ?? '—'}
              {kpi.parallelCapacity?.ollamaNumParallel != null
                ? ` (SoT ${kpi.parallelCapacity.maxConcurrentLlm} · OLLAMA_NUM_PARALLEL ${kpi.parallelCapacity.ollamaNumParallel})`
                : ''}
              {kpi.updatedAtAst ? ` · KPI ${kpi.updatedAtAst}` : kpi.updatedAt ? ` · KPI ${posTime(kpi.updatedAt)}` : ''}
            </Text>
            <HStack gap={2} wrap="wrap">
              {(kpi.enrichLive?.live || []).map((bot) => (
                <Box key={bot.id} px={2} py={1} bg="#FFF5EB" borderWidth="1px" borderColor="#E67E2260" borderRadius="md">
                  <Text fontSize="xs" fontWeight="bold" color="#E67E22">{bot.id} live</Text>
                  <Text fontSize="xs" color="#787469">{bot.inflightEnriched ?? 0} mid-batch</Text>
                </Box>
              ))}
              {(kpi.enrichLive?.waiting || []).slice(0, 5).map((bot) => (
                <Box key={bot.id} px={2} py={1} bg="#F5F4F0" borderWidth="1px" borderColor="#E4E2DC" borderRadius="md">
                  <Text fontSize="xs" color="#9E9A90">{bot.id} waiting</Text>
                </Box>
              ))}
              {kpi.enrichLive?.queueBacklog != null ? (
                <Box px={2} py={1} bg="#EEF6FF" borderWidth="1px" borderColor="#4A90D960" borderRadius="md">
                  <Text fontSize="xs" color="#4A90D9">queue {kpi.enrichLive.queueBacklog.toLocaleString()}</Text>
                </Box>
              ) : null}
            </HStack>
          </Box>
        ) : null}

        {kpi?.processedVolume?.windows && kpi.processedVolume.windows.length > 0 ? (
          <Box>
            <Heading size="sm" color="#2D2A24" mb={1}>Processed volume</Heading>
            <Text color="#787469" fontSize="sm" mb={3}>
              Enrich + significance successes only (sync/merge shown as ops) — from first entry
              {kpi.processedVolume.firstEntryDate
                ? ` ${kpi.processedVolume.firstEntryDate.slice(0, 10)}`
                : ''}
              .
            </Text>
            <Flex gap={3} wrap="wrap">
              {kpi.processedVolume.windows.map((window) => (
                <Box
                  key={window.id}
                  bg="white"
                  borderWidth="1px"
                  borderColor="#E4E2DC"
                  borderRadius="xl"
                  p={4}
                  minW="180px"
                  flex="1"
                >
                  <Text fontSize="xs" letterSpacing="0.1em" textTransform="uppercase" color="#787469">
                    {window.label}
                  </Text>
                  <Text fontSize="3xl" fontWeight="bold" color="#2D2A24" mt={1} lineHeight="1.1">
                    {window.recorded ? window.processed.toLocaleString() : '—'}
                  </Text>
                  <Text fontSize="sm" color="#9E9A90">enrich + significance</Text>
                  {window.recorded ? (
                    <>
                      <Text fontSize="sm" color="#2D2A24" mt={2}>
                        {window.jobs} {window.jobs === 1 ? 'job' : 'jobs'}
                      </Text>
                      {(window.opsProcessed ?? 0) > 0 || (window.opsJobs ?? 0) > 0 ? (
                        <Text fontSize="xs" color="#787469" mt={1}>
                          ops {(window.opsProcessed ?? 0).toLocaleString()} · {window.opsJobs ?? 0} jobs
                        </Text>
                      ) : null}
                    </>
                  ) : (
                    <Text fontSize="sm" color="#2D2A24" mt={2}>None recorded</Text>
                  )}
                </Box>
              ))}
            </Flex>
          </Box>
        ) : null}

        <HStack gap={2} wrap="wrap">
          {[
            ['all', 'All statuses'],
            ['active', 'Active'],
            ['proposed', 'Proposed'],
            ['paused', 'Paused'],
          ].map(([status, label]) => (
            <Button
              key={status}
              size="sm"
              minH="44px"
              borderRadius="full"
              bg={statusFilter === status ? '#C5963A' : 'white'}
              color={statusFilter === status ? 'white' : '#2D2A24'}
              borderWidth="1px"
              borderColor="#E4E2DC"
              onClick={() => setStatusFilter(status)}
              aria-pressed={statusFilter === status}
            >
              {label}
            </Button>
          ))}
        </HStack>

        <HStack gap={2} wrap="wrap">
          <Button
            size="sm"
            minH="44px"
            borderRadius="full"
            bg={laneFilter === 'all' ? '#2D2A24' : 'white'}
            color={laneFilter === 'all' ? 'white' : '#2D2A24'}
            borderWidth="1px"
            borderColor="#E4E2DC"
            onClick={() => setLaneFilter('all')}
            aria-pressed={laneFilter === 'all'}
          >
            All lanes
          </Button>
          {lanes.map((lane) => (
            <Button
              key={lane.id}
              size="sm"
              minH="44px"
              borderRadius="full"
              bg={laneFilter === lane.id ? '#2D2A24' : 'white'}
              color={laneFilter === lane.id ? 'white' : '#2D2A24'}
              borderWidth="1px"
              borderColor="#E4E2DC"
              onClick={() => setLaneFilter(lane.id)}
              aria-pressed={laneFilter === lane.id}
            >
              {lane.id}
            </Button>
          ))}
        </HStack>

        <Box bg="white" borderWidth="1px" borderColor="#E4E2DC" borderRadius="xl" p={4}>
          <Heading size="md" color="#2D2A24">24 hours</Heading>
          <Text color="#787469" mt={2} fontSize="sm">
            Each bar is one hour in Port of Spain. Taller means more bots are allotted to that hour.
            The lower color is turned on. The upper color is written down but turned off.
          </Text>
          <HStack gap={4} mt={3}>
            <HStack gap={2}>
              <Box w="12px" h="12px" borderRadius="sm" bg="#6B3FA0" />
              <Text color="#787469" fontSize="sm">Turned on</Text>
            </HStack>
            <HStack gap={2}>
              <Box w="12px" h="12px" borderRadius="sm" bg="#C8C4BC" />
              <Text color="#787469" fontSize="sm">Waiting</Text>
            </HStack>
          </HStack>
          <Flex mt={4} align="flex-end" gap={1} h="160px" role="group" aria-label="Bots allotted across 24 hours">
            {dayBars.map((slot) => {
              const total = slot.enabled.length + slot.waiting.length
              const height = total === 0 ? 4 : Math.max(12, Math.round((total / busiest) * 140))
              const enabledHeight = total === 0 ? 0 : Math.round((slot.enabled.length / total) * height)
              const waitingHeight = height - enabledHeight
              const current = slot.hour === nowHour
              return (
                <Button
                  key={slot.hour}
                  variant="ghost"
                  flex="1"
                  minW="0"
                  h="160px"
                  p={0}
                  display="flex"
                  flexDirection="column"
                  justifyContent="flex-end"
                  alignItems="stretch"
                  borderRadius="md"
                  borderWidth={current || selectedHour === slot.hour ? '2px' : '1px'}
                  borderColor={selectedHour === slot.hour ? '#C5963A' : '#E4E2DC'}
                  bg={current ? '#FAF3E8' : '#FAF9F6'}
                  aria-pressed={selectedHour === slot.hour}
                  aria-label={`${hourLabel(slot.hour)}, ${slot.enabled.length} turned on, ${slot.waiting.length} waiting`}
                  onClick={() => setSelectedHour(slot.hour)}
                >
                  <Box h={`${waitingHeight}px`} bg={slot.waiting.length ? '#C8C4BC' : 'transparent'} borderTopRadius="sm" />
                  <Box h={`${enabledHeight}px`} bg={slot.enabled.length ? '#6B3FA0' : 'transparent'} />
                  <Text color="#9E9A90" fontSize="10px" textAlign="center" lineHeight="1.2" py={1}>
                    {slot.hour % 3 === 0 ? hourLabel(slot.hour) : '·'}
                  </Text>
                </Button>
              )
            })}
          </Flex>
          <Box mt={3}>
            <Text color="#2D2A24" fontWeight="semibold">{hourLabel(selected.hour)} Port of Spain</Text>
            <Text color="#2D2A24" mt={1} fontSize="sm">
              {selected.enabled.length ? selected.enabled.join(', ') : 'No bot is turned on this hour.'}
            </Text>
            {selected.waiting.length ? (
              <Text color="#787469" mt={1} fontSize="sm">Waiting: {selected.waiting.join(', ')}</Text>
            ) : null}
          </Box>
        </Box>

        <Heading size="md" color="#2D2A24">Through the day</Heading>
        <VStack align="stretch" gap={3}>
          {timetable.map((bot) => {
            const cron = cronOf(bot)
            const enabled = bot.schedule?.enabled !== false
            const when = cron ? describeCron(cron) : null
            const chip = chipFor(bot)
            const tone = chipTone(chip)
            const last = lastFinishedByBot.get(bot.id) || lastFinishedByBot.get(bot.id === 'push' ? 'git-push' : bot.id)
            const kpiRow = kpiByBot.get(bot.id)
            const running = runningByBot.get(bot.id) || runningByBot.get(bot.id === 'push' ? 'git-push' : bot.id)
            const finishedAt = last?.finished || kpiRow?.lastJobFinished || kpiRow?.lastLogAt
            return (
              <Flex
                key={bot.id}
                bg="white"
                borderWidth="1px"
                borderColor="#E4E2DC"
                borderLeftWidth="6px"
                borderLeftColor={tone.border}
                borderRadius="xl"
                overflow="hidden"
                direction={{ base: 'column', md: 'row' }}
              >
                <Box bg={tone.bg} color={tone.color} px={4} py={4} minW={{ base: '100%', md: '240px' }}>
                  <Text fontWeight="bold" fontSize="lg">{when?.headline ?? 'No schedule yet'}</Text>
                  <Text fontSize="sm" mt={2}>{chip}</Text>
                </Box>
                <Box p={4} flex="1">
                  <Flex justify="space-between" gap={3} wrap="wrap">
                    <Heading size="sm" color="#2D2A24">{bot.name}</Heading>
                    <Box px={3} py={1} borderRadius="full" bg="#F5F4F0" color="#2D2A24" borderWidth="1px" borderColor="#E4E2DC" fontSize="sm">
                      {statusWords(bot.status)}
                    </Box>
                  </Flex>
                  <Text mt={2} color="#2D2A24" fontSize="sm">{bot.role}</Text>
                  <Text mt={2} fontSize="sm" color="#787469">
                    Lane: {laneLabel(lanes, bot.lane)} · Label: com.annals.{bot.id}
                    {bot.uses_ollama ? ' · Ollama' : ''}
                    {bot.uses_grok ? ' · Grok' : ''}
                  </Text>
                  <Text mt={2} color="#2D2A24" fontSize="sm">
                    {chip === 'Active now'
                      ? `Running now${running ? ` (job ${running.job_id})` : ''}.`
                      : chip === 'Last run finished'
                        ? 'The last run finished. The job stays turned on for the next time on the left.'
                        : chip === 'Scheduled'
                          ? 'This job is turned on. It is not running at this moment.'
                          : 'This bot is declared, and the job is not turned on.'}
                  </Text>
                  <Text mt={2} color="#2D2A24" fontSize="sm">
                    {finishedAt
                      ? `Last signal ${posTime(finishedAt)}${last?.status ? `: ${last.status}` : kpiRow?.lastJobStatus ? `: ${kpiRow.lastJobStatus}` : ''}.`
                      : `Has not run yet. The first run will do this: ${bot.role}`}
                  </Text>
                  {bot.schedule?.note ? <Text mt={2} fontSize="sm" color="#787469">{bot.schedule.note}</Text> : null}
                  <Text mt={3} fontSize="sm" color="#9E9A90">
                    Cron: {cron || (enabled ? 'keepalive' : 'none declared')}
                  </Text>
                  {when ? <Text fontSize="sm" color="#9E9A90">{when.utcNote}</Text> : null}
                </Box>
              </Flex>
            )
          })}
          {timetable.length === 0 ? (
            <Text color="#787469">No bots match these filters. Load platform-local-bots.json under /governance/.</Text>
          ) : null}
        </VStack>
      </VStack>
    </Box>
  )
}
