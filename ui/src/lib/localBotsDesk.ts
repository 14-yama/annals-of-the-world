/**
 * Shared facts for Annals local-bot KPI + timetable (Superstack schedule UX pattern).
 * Roster SoT: /governance/platform-local-bots.json (mirrored from data/governance).
 */
import { useEffect, useMemo, useState } from 'react'

export type AnnalsBot = {
  id: string
  name: string
  status: string
  lane?: string
  role: string
  uses_ollama?: boolean
  uses_grok?: boolean
  schedule?: {
    cron?: string
    kind?: string
    throttle_seconds?: number
    enabled?: boolean
    note?: string
    timezone?: string
  }
  launchd?: { label?: string; KeepAlive?: boolean; RunAtLoad?: boolean; ThrottleInterval?: number }
  respect_blackout?: boolean
}

export type Lane = { id: string; label: string }

export type LocalJob = {
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

export type LocalKpiRosterRow = {
  id: string
  name?: string
  status?: string
  lane?: string
  cron?: string
  scheduleEnabled?: boolean
  lastJobStatus?: string
  lastJobStarted?: string
  lastJobFinished?: string
  lastLogAt?: string
}

export type ProcessedVolumeWindow = {
  id: string
  label: string
  kind?: string
  recorded: boolean
  processed: number
  jobs: number
  enrichmentProcessed?: number
  enrichmentJobs?: number
  opsProcessed?: number
  opsJobs?: number
  doneJobs?: number
  errorJobs?: number
  successRate?: number
  byTask: Record<string, number>
  jobsByTask?: Record<string, number>
  byCategory?: Record<string, number>
  metric?: string
  metricNote?: string
  windowStart?: string
  windowEnd?: string
  timezone?: string
}

export type ProcessedVolume = {
  firstEntryDate?: string | null
  oldestEventAt?: string | null
  historyNote?: string | null
  metric?: string
  totalProcessedAllTime?: number
  totalOpsProcessedAllTime?: number
  totalEvents?: number
  windows?: ProcessedVolumeWindow[]
  byId?: Record<string, ProcessedVolumeWindow>
}

export type EnrichLiveBot = {
  id: string
  label?: string
  shard?: string | null
  status?: string
  inflightEnriched?: number
  lastBatchEnriched?: number | null
  lastBatchFailed?: number | null
  lastBatchAt?: string | null
  dispatchStartedAt?: string | null
}

export type EnrichLive = {
  updatedAt?: string
  updatedAtAst?: string
  timezone?: string
  enrichBotsConfigured?: number
  enrichBotsLive?: number
  enrichBotsWaiting?: number
  enrichBotsTotal?: number
  liveLabels?: string[]
  waitingLabels?: string[]
  live?: EnrichLiveBot[]
  waiting?: EnrichLiveBot[]
  ratePerHour?: number
  rateLookbackMinutes?: number
  rateFormula?: string
  enrichedInLookback?: number
  failedInLookback?: number
  lastBatches?: Array<{
    id: string
    enriched?: number | null
    failed?: number | null
    at?: string | null
    ok?: boolean
  }>
  significanceStatus?: string
  significanceInflight?: boolean
  significanceLastAt?: string | null
  queueBacklog?: number | null
  queueGeneratedAt?: string | null
  shardsLive?: string[]
}

export type ParallelLane = {
  description?: string
  activeBots?: string[]
  activeCount?: number
  maxParallel?: number
}

export type ParallelCapacity = {
  maxConcurrentLlm?: number
  maxConcurrentGrok?: number
  ollamaNumParallel?: number | null
  effectiveLlmParallel?: number
  effectiveNote?: string
  enrichWaitersConfigured?: number
  enrichWaitersLive?: number
  serializeEnrichVsSignificance?: boolean
  maxConcurrentHeavyScan?: number
  lanes?: Record<string, ParallelLane>
  laneNotes?: string[]
}

export type LocalKpi = {
  updatedAt?: string
  updatedAtAst?: string
  rosterCount?: number
  roster?: LocalKpiRosterRow[]
  firstEntryDate?: string | null
  processedVolume?: ProcessedVolume
  enrichLive?: EnrichLive
  parallelCapacity?: ParallelCapacity
  last24h?: {
    totalJobs: number
    doneJobs: number
    errorJobs: number
    successRate: number
    processed?: number
    byTask: Record<string, number>
    processedByTask?: Record<string, number>
  }
  last7d?: {
    totalJobs: number
    doneJobs: number
    errorJobs: number
    successRate: number
    processed?: number
    byTask: Record<string, number>
    processedByTask?: Record<string, number>
  }
  last30d?: {
    totalJobs: number
    doneJobs: number
    errorJobs: number
    successRate: number
    processed?: number
    byTask: Record<string, number>
    processedByTask?: Record<string, number>
  }
}

export type BotsSot = {
  bots: AnnalsBot[]
  concurrency?: {
    lanes?: Record<string, string>
    max_concurrent_llm?: number
    max_concurrent_grok?: number
    max_concurrent_heavy_scan?: number
    serialize_enrich_vs_significance?: boolean
  }
  meta?: { timezone?: string; label_prefix?: string }
}

export const timezone = 'America/Port_of_Spain'
export const labelPrefix = 'com.annals.'

const WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

function clock(hour: number, minute: number): string {
  const suffix = hour >= 12 ? 'pm' : 'am'
  const hour12 = hour % 12 === 0 ? 12 : hour % 12
  return `${hour12}:${String(minute).padStart(2, '0')}${suffix}`
}

function partOfDay(hour: number): string {
  if (hour >= 5 && hour < 12) return 'morning'
  if (hour >= 12 && hour < 17) return 'afternoon'
  return 'night'
}

export function describeCron(expr: string): { sort: number; headline: string; utcNote: string } {
  if (!expr || expr === 'keepalive') {
    return {
      sort: -1,
      headline: 'Always on (KeepAlive)',
      utcNote: 'Not a cron job. LaunchAgent KeepAlive + RunAtLoad.',
    }
  }
  if (expr.startsWith('worker:')) {
    const secs = expr.slice('worker:'.length)
    return {
      sort: -1,
      headline: `KeepAlive worker (~${secs} throttle)`,
      utcNote: 'Relaunches after each batch. Soft-skips when lane lock is held.',
    }
  }
  const [minField, hourField, dayField, , dowField] = expr.split(/\s+/)
  if (!minField || !hourField) {
    return { sort: 9999, headline: expr, utcNote: 'Port of Spain does not change clocks.' }
  }

  if (minField.startsWith('*/') && (hourField === '*' || hourField.startsWith('*/'))) {
    const step = Number(minField.slice(2))
    return {
      sort: 0,
      headline: `Every ${Number.isFinite(step) ? step : 5} minutes`,
      utcNote: 'Port of Spain does not change clocks.',
    }
  }

  const minute = minField.startsWith('*/') ? 0 : Number(minField)
  const monthNote = dayField && dayField !== '*' ? `, on day ${dayField} of the month` : ''

  if (minField.includes(',') && (hourField === '*' || !hourField.includes(','))) {
    const mins = minField.split(',').map((v) => Number(v)).filter((m) => m >= 0 && m < 60)
    if (hourField === '*') {
      return {
        sort: mins[0] ?? 0,
        headline: `Hourly at ${mins.map((m) => `:${String(m).padStart(2, '0')}`).join(' and ')}`,
        utcNote: 'Port of Spain does not change clocks.',
      }
    }
  }

  if (hourField.includes(',')) {
    const hours = hourField.split(',').map((v) => Number(v)).filter((h) => h >= 0 && h < 24)
    const spoken = hours.map((h) => clock(h, Number.isFinite(minute) ? minute : 0)).join(', ')
    return {
      sort: (hours[0] ?? 0) * 60 + (Number.isFinite(minute) ? minute : 0),
      headline: `At ${spoken}${monthNote}`,
      utcNote: 'Same local minute in America/Port_of_Spain (AST, no DST).',
    }
  }

  if (hourField === '*' || hourField.startsWith('*/')) {
    const every = hourField === '*' ? 'Every hour' : `Every ${hourField.slice(2)} hours`
    const at = `at ${minute === 0 ? 'the top of the hour' : `:${String(minute).padStart(2, '0')}`}`
    return {
      sort: Number.isFinite(minute) ? minute : 0,
      headline: `${every} ${at}${monthNote}`,
      utcNote: 'Port of Spain does not change clocks.',
    }
  }

  const hour = Number(hourField)
  const spoken = clock(hour, Number.isFinite(minute) ? minute : 0)
  let headline = `Every ${partOfDay(hour)} at ${spoken}`
  if (dowField && dowField !== '*') {
    headline = `Every ${WEEKDAYS[Number(dowField)] ?? 'scheduled day'} at ${spoken}`
  }
  headline += monthNote

  const utcHour = (hour + 4) % 24
  const nextDay = hour + 4 >= 24 ? ' the next UTC day' : ''
  return {
    sort: hour * 60 + (Number.isFinite(minute) ? minute : 0),
    headline,
    utcNote: `Same moment is ${clock(utcHour, Number.isFinite(minute) ? minute : 0)} UTC${nextDay}.`,
  }
}

export function hoursForCron(expr: string | undefined): number[] {
  if (!expr || expr === 'keepalive') return Array.from({ length: 24 }, (_, h) => h)
  const parts = expr.trim().split(/\s+/)
  const hourField = parts[1] ?? '*'
  if (hourField === '*') return Array.from({ length: 24 }, (_, hour) => hour)
  if (hourField.startsWith('*/')) {
    const step = Number(hourField.slice(2))
    if (!Number.isFinite(step) || step <= 0) return []
    const hours: number[] = []
    for (let hour = 0; hour < 24; hour += step) hours.push(hour)
    return hours
  }
  if (hourField.includes('-')) {
    const [start, end] = hourField.split('-').map((value) => Number(value))
    if (!Number.isFinite(start) || !Number.isFinite(end)) return []
    const hours: number[] = []
    for (let hour = start; hour <= end && hour < 24; hour += 1) hours.push(hour)
    return hours
  }
  if (hourField.includes(',')) {
    return hourField.split(',').map((value) => Number(value)).filter((hour) => hour >= 0 && hour < 24)
  }
  const hour = Number(hourField)
  return hour >= 0 && hour < 24 ? [hour] : []
}

export function cronOf(bot: AnnalsBot): string {
  const s = bot.schedule
  if (!s) return ''
  if (s.kind === 'keepalive' || s.kind === 'worker') {
    const throttle = s.throttle_seconds ?? bot.launchd?.ThrottleInterval
    if (typeof throttle === 'number' && throttle > 0) return `worker:${throttle}s`
    return 'keepalive'
  }
  return s.cron ?? ''
}

export function hourLabel(hour: number): string {
  if (hour === 0) return '12a'
  if (hour === 12) return '12p'
  return hour < 12 ? `${hour}a` : `${hour - 12}p`
}

export function portOfSpainHour(): number {
  const fmt = new Intl.DateTimeFormat('en-US', {
    timeZone: timezone,
    hour: '2-digit',
    hourCycle: 'h23',
  })
  const hour = fmt.formatToParts(new Date()).find((part) => part.type === 'hour')?.value ?? '0'
  return hour === '24' ? 0 : Number(hour)
}

export function statusWords(status: string): string {
  if (status === 'active') return 'Active'
  if (status === 'proposed') return 'Proposed'
  if (status === 'paused') return 'Paused'
  return 'Planned'
}

export function posTime(iso: string | null | undefined): string {
  if (!iso) return 'time not recorded'
  const time = new Date(iso)
  if (Number.isNaN(time.getTime())) return 'time not recorded'
  return time.toLocaleString('en-US', {
    timeZone: timezone,
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  })
}

/** Full Trinidad (America/Port_of_Spain / AST) stamp for audit tables. */
export function formatTrinidadTimestamp(iso: string | null | undefined): string {
  if (!iso) return '—'
  const time = new Date(iso)
  if (Number.isNaN(time.getTime())) return '—'
  const formatted = time.toLocaleString('en-US', {
    timeZone: timezone,
    month: 'long',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
    second: '2-digit',
    hour12: true,
  })
  return `${formatted} AST`
}

/** Date-only Trinidad stamp (e.g. Latest Edit card). */
export function formatTrinidadDate(iso: string | null | undefined): string {
  if (!iso) return '—'
  const time = new Date(iso)
  if (Number.isNaN(time.getTime())) return '—'
  return time.toLocaleDateString('en-US', {
    timeZone: timezone,
    month: 'long',
    day: 'numeric',
    year: 'numeric',
  })
}

export function timetableChip(enabled: boolean, running: boolean, hasReport: boolean): string {
  if (!enabled) return 'Waiting'
  if (running) return 'Active now'
  if (hasReport) return 'Last run finished'
  return 'Scheduled'
}

/** Hex tones matching Annals curator palette (Superstack semantic roles). */
export function chipTone(label: string): { bg: string; color: string; border: string } {
  if (label === 'Active now') return { bg: '#FFF5EB', color: '#E67E22', border: '#E67E22' }
  if (label === 'Last run finished') return { bg: '#F0FFF4', color: '#27AE60', border: '#27AE60' }
  if (label === 'Idle') return { bg: '#EEF6FF', color: '#4A90D9', border: '#4A90D9' }
  if (label === 'Scheduled') return { bg: '#F5F0FF', color: '#6B3FA0', border: '#6B3FA0' }
  return { bg: '#F5F4F0', color: '#9E9A90', border: '#9E9A90' }
}

export function lanesFromSot(sot: BotsSot | null): Lane[] {
  return Object.entries(sot?.concurrency?.lanes ?? {}).map(([id, label]) => ({
    id,
    label: String(label).split('—')[0]?.trim() || id,
  }))
}

export function laneLabel(lanes: Lane[], lane: string | undefined): string {
  if (!lane) return 'unassigned'
  return lanes.find((l) => l.id === lane)?.label ?? lane
}

async function localGet<T>(endpoint: string): Promise<T | null> {
  try {
    const r = await fetch(`/local-bots${endpoint}`, { cache: 'no-store' })
    if (!r.ok) return null
    return (await r.json()) as T
  } catch {
    return null
  }
}

export function useLocalBotDesk() {
  const [sot, setSot] = useState<BotsSot | null>(null)
  const [jobs, setJobs] = useState<Record<string, LocalJob>>({})
  const [kpi, setKpi] = useState<LocalKpi | null>(null)
  const [activityError, setActivityError] = useState(false)

  useEffect(() => {
    let seq = 0
    const load = () => {
      const id = ++seq
      fetch('/governance/platform-local-bots.json', { cache: 'no-store' })
        .then((res) => (res.ok ? res.json() : Promise.reject(new Error(String(res.status)))))
        .then((body: BotsSot) => {
          if (id === seq) setSot(body)
        })
        .catch(() => { /* keep prior */ })

      localGet<Record<string, LocalJob>>('/bots/status')
        .then((body) => {
          if (id !== seq) return
          setJobs(body ?? {})
          setActivityError(false)
        })
        .catch(() => {
          if (id === seq) setActivityError(true)
        })

      fetch('/governance/bot_kpi/local_kpi.json', { cache: 'no-store' })
        .then((res) => (res.ok ? res.json() : Promise.reject(new Error(String(res.status)))))
        .then((body: LocalKpi) => {
          if (id === seq) setKpi(body)
        })
        .catch(() => { /* keep prior */ })
    }
    load()
    // Match Bot KPI cadence so timetable chips / processed volume track live enrich
    const timer = window.setInterval(load, 5_000)
    const onFocus = () => load()
    const onVis = () => {
      if (document.visibilityState === 'visible') load()
    }
    window.addEventListener('focus', onFocus)
    document.addEventListener('visibilitychange', onVis)
    return () => {
      seq += 1
      window.clearInterval(timer)
      window.removeEventListener('focus', onFocus)
      document.removeEventListener('visibilitychange', onVis)
    }
  }, [])

  const bots = sot?.bots ?? []
  const lanes = useMemo(() => lanesFromSot(sot), [sot])

  const jobsList = useMemo(
    () => Object.values(jobs).sort((a, b) => b.started.localeCompare(a.started)),
    [jobs],
  )

  const runningByBot = useMemo(() => {
    const map = new Map<string, LocalJob>()
    for (const job of jobsList) {
      if (job.status === 'running' && !map.has(job.bot)) map.set(job.bot, job)
    }
    return map
  }, [jobsList])

  const lastFinishedByBot = useMemo(() => {
    const map = new Map<string, LocalJob>()
    for (const job of jobsList) {
      if (job.status === 'running') continue
      const prev = map.get(job.bot)
      if (!prev || (job.finished ?? job.started) > (prev.finished ?? prev.started)) {
        map.set(job.bot, job)
      }
    }
    return map
  }, [jobsList])

  const kpiByBot = useMemo(() => {
    const map = new Map<string, LocalKpiRosterRow>()
    for (const row of kpi?.roster ?? []) map.set(row.id, row)
    return map
  }, [kpi])

  return {
    sot,
    bots,
    lanes,
    jobs: jobsList,
    runningByBot,
    lastFinishedByBot,
    kpi,
    kpiByBot,
    activityError,
  }
}
