/**
 * useGlobalCounts — Shared hook for fast, cached entity counts.
 *
 * Reads pre-computed stats from the public mirror
 * (`/governance/stats_cache.json`) first, then Appwrite `stats_cache`.
 *
 * localStorage is for instant paint only — it never blocks a background
 * revalidation against the mirror (fixes stale Browse All counts like 100258
 * stuck for the full 10m TTL).
 *
 * Usage:
 *   const { total, byLabel, byEra, byContinent, byClass, loading } = useGlobalCounts()
 */
import { useEffect, useState, useCallback } from 'react'
import { databases, functions, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'
import { ExecutionMethod, Query } from 'appwrite'

/* ─── Types ─── */

export interface GlobalCounts {
  total: number
  byLabel: Record<string, number>
  byEra: Record<string, number>
  byContinent: Record<string, number>
  byClass: Record<string, number>
  loading: boolean
  lastUpdated: number | null
  refresh: () => void
}

/* ─── Module-level cache (shared across all hook consumers) ─── */

interface CountCache {
  total: number
  byLabel: Record<string, number>
  byEra: Record<string, number>
  byContinent: Record<string, number>
  byClass: Record<string, number>
  lastUpdated: number | null
  promise: Promise<void> | null
  /** ISO updatedAt from last successful mirror/Appwrite read */
  sourceUpdatedAt: string | null
}

// Soft TTL: skip network only if we already revalidated this session recently
const SOFT_TTL = 60 * 1000
// localStorage paint window (does NOT suppress revalidation)
const PAINT_TTL = 10 * 60 * 1000

const LOCALSTORAGE_KEY = 'annals_global_counts'

/** Appwrite listDocuments `.total` hard-caps around this — never treat as truth. */
const APPWRITE_TOTAL_CAP = 5000

const cache: CountCache = {
  total: 0,
  byLabel: {},
  byEra: {},
  byContinent: {},
  byClass: {},
  lastUpdated: null,
  promise: null,
  sourceUpdatedAt: null,
}

function isCappedTotal(n: number | undefined | null): boolean {
  return typeof n === 'number' && n > 0 && n <= APPWRITE_TOTAL_CAP
}

function persistCache() {
  try {
    localStorage.setItem(LOCALSTORAGE_KEY, JSON.stringify({
      total: cache.total,
      byLabel: cache.byLabel,
      byEra: cache.byEra,
      byContinent: cache.byContinent,
      byClass: cache.byClass,
      ts: cache.lastUpdated,
      sourceUpdatedAt: cache.sourceUpdatedAt,
    }))
  } catch { /* non-fatal */ }
}

function applyCounts(
  total: number,
  byLabel: Record<string, number>,
  byEra: Record<string, number>,
  byContinent: Record<string, number>,
  byClass: Record<string, number>,
  sourceUpdatedAt?: string | null,
) {
  // Never overwrite a good catalog total with a capped/placeholder value
  if (isCappedTotal(total) && cache.total > APPWRITE_TOTAL_CAP) {
    return false
  }
  cache.total = total
  cache.byLabel = byLabel
  cache.byEra = byEra
  cache.byContinent = byContinent
  cache.byClass = byClass
  cache.lastUpdated = Date.now()
  if (sourceUpdatedAt) cache.sourceUpdatedAt = sourceUpdatedAt
  persistCache()
  return true
}

// Hydrate from localStorage for instant paint only (never blocks revalidation)
try {
  const stored = localStorage.getItem(LOCALSTORAGE_KEY)
  if (stored) {
    const parsed = JSON.parse(stored)
    if (parsed.ts && (Date.now() - parsed.ts) < PAINT_TTL && !isCappedTotal(parsed.total)) {
      cache.total = parsed.total || 0
      cache.byLabel = parsed.byLabel || {}
      cache.byEra = parsed.byEra || {}
      cache.byContinent = parsed.byContinent || {}
      cache.byClass = parsed.byClass || {}
      // Intentionally do NOT set lastUpdated from localStorage — forces
      // ensureCounts() to revalidate against the public mirror every load.
      cache.sourceUpdatedAt = parsed.sourceUpdatedAt || null
    } else if (isCappedTotal(parsed?.total)) {
      localStorage.removeItem(LOCALSTORAGE_KEY)
    }
  }
} catch { /* localStorage may not be available */ }

const listeners = new Set<() => void>()
function notify() { listeners.forEach(fn => fn()) }

async function fetchFromStatsCache(): Promise<boolean> {
  try {
    const result = await databases.listDocuments(
      DATABASE_ID,
      COLLECTIONS.STATS_CACHE,
      [Query.orderDesc('updatedAt'), Query.limit(1)]
    )

    if (result.documents.length === 0) return false
    const doc = result.documents[0]
    const total = Number(doc.total || 0)
    if (isCappedTotal(total)) return false

    return applyCounts(
      total,
      typeof doc.byLabel === 'string' ? JSON.parse(doc.byLabel) : (doc.byLabel || {}),
      typeof doc.byEra === 'string' ? JSON.parse(doc.byEra) : (doc.byEra || {}),
      typeof doc.byContinent === 'string' ? JSON.parse(doc.byContinent) : (doc.byContinent || {}),
      typeof doc.byClass === 'string' ? JSON.parse(doc.byClass) : (doc.byClass || {}),
      typeof doc.updatedAt === 'string' ? doc.updatedAt : null,
    )
  } catch {
    return false
  }
}

async function fetchLiveTotals(): Promise<boolean> {
  try {
    let mirrored: {
      total?: number
      byLabel?: Record<string, number>
      byEra?: Record<string, number>
      byContinent?: Record<string, number>
      byClass?: Record<string, number>
      updatedAt?: string
    } | null = null
    try {
      const r = await fetch(`/governance/stats_cache.json?t=${Date.now()}`, { cache: 'no-store' })
      if (r.ok) mirrored = await r.json()
    } catch { /* optional */ }

    if (mirrored && typeof mirrored.total === 'number' && !isCappedTotal(mirrored.total)) {
      return applyCounts(
        mirrored.total,
        mirrored.byLabel || {},
        mirrored.byEra || {},
        mirrored.byContinent || {},
        mirrored.byClass || {},
        mirrored.updatedAt || null,
      )
    }

    // Last resort: sum uncapped label queries (still useless above 5k each)
    const labels = ['Person', 'Idea', 'Institution', 'Place', 'EventWindow', 'Movement', 'Text', 'Evidence']
    const byLabel: Record<string, number> = {}
    await Promise.all(labels.map(async (label) => {
      try {
        const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
          Query.equal('label', label),
          Query.limit(1),
        ])
        if (res.total > 0 && res.total < APPWRITE_TOTAL_CAP) byLabel[label] = res.total
      } catch { /* skip */ }
    }))
    const labelSum = Object.values(byLabel).reduce((a, b) => a + b, 0)
    if (labelSum > 0 && labelSum < APPWRITE_TOTAL_CAP) {
      return applyCounts(labelSum, byLabel, {}, {}, {})
    }
    return false
  } catch {
    return false
  }
}

async function fetchViaFunction(): Promise<boolean> {
  try {
    await functions.createExecution(
      'audit-consistency',
      JSON.stringify({}),
      true,
      undefined,
      ExecutionMethod.POST,
    )
    return false
  } catch {
    return false
  }
}

async function fetchFromPublicMirror(): Promise<boolean> {
  try {
    const r = await fetch(`/governance/stats_cache.json?t=${Date.now()}`, { cache: 'no-store' })
    if (!r.ok) return false
    const mirrored = await r.json() as {
      total?: number
      byLabel?: Record<string, number>
      byEra?: Record<string, number>
      byContinent?: Record<string, number>
      byClass?: Record<string, number>
      updatedAt?: string
    }
    if (!mirrored || typeof mirrored.total !== 'number' || isCappedTotal(mirrored.total)) {
      return false
    }
    return applyCounts(
      mirrored.total,
      mirrored.byLabel || {},
      mirrored.byEra || {},
      mirrored.byContinent || {},
      mirrored.byClass || {},
      mirrored.updatedAt || null,
    )
  } catch {
    return false
  }
}

async function fetchAllCounts(): Promise<void> {
  const mirrored = await fetchFromPublicMirror()
  if (!mirrored) {
    const ok = await fetchFromStatsCache()
    if (!ok) {
      const live = await fetchLiveTotals()
      if (!live) {
        fetchViaFunction()
        // Retry soon — do not paint a capped total
        cache.lastUpdated = Date.now() - SOFT_TTL + 15_000
      }
    }
  }
  cache.promise = null
  notify()
}

/**
 * Ensure counts are loaded. localStorage paint never suppresses revalidation;
 * Soft TTL only avoids hammering the mirror within the same minute.
 */
function ensureCounts(opts?: { force?: boolean }): Promise<void> {
  const fresh =
    !opts?.force &&
    cache.lastUpdated != null &&
    (Date.now() - cache.lastUpdated) < SOFT_TTL &&
    cache.total > APPWRITE_TOTAL_CAP

  if (fresh) return Promise.resolve()

  if (!cache.promise) {
    cache.promise = fetchAllCounts().catch((err) => {
      console.error('Global count fetch failed:', err)
      cache.promise = null
    })
  }
  return cache.promise
}

/* ─── React Hook ─── */

export function useGlobalCounts(): GlobalCounts {
  const [, setTick] = useState(0)

  const refresh = useCallback(() => {
    cache.lastUpdated = null
    cache.promise = null
    ensureCounts({ force: true })
  }, [])

  useEffect(() => {
    const listener = () => setTick(t => t + 1)
    listeners.add(listener)

    // Always revalidate on mount — clears stale localStorage paint (e.g. 100258)
    ensureCounts({ force: true })

    // Keep catalog/curator totals in sync with stats-cache + enrich progress
    const pollId = window.setInterval(() => ensureCounts({ force: true }), 60_000)
    const onFocus = () => ensureCounts({ force: true })
    const onVis = () => {
      if (document.visibilityState === 'visible') ensureCounts({ force: true })
    }
    window.addEventListener('focus', onFocus)
    document.addEventListener('visibilitychange', onVis)

    return () => {
      listeners.delete(listener)
      window.clearInterval(pollId)
      window.removeEventListener('focus', onFocus)
      document.removeEventListener('visibilitychange', onVis)
    }
  }, [])

  return {
    total: cache.total,
    byLabel: cache.byLabel,
    byEra: cache.byEra,
    byContinent: cache.byContinent,
    byClass: cache.byClass,
    loading: cache.promise !== null && cache.total === 0,
    lastUpdated: cache.lastUpdated,
    refresh,
  }
}

/* ─── Direct access (for non-React contexts) ─── */

export function getGlobalCounts() {
  ensureCounts()
  return {
    total: cache.total,
    byLabel: cache.byLabel,
    byEra: cache.byEra,
    byContinent: cache.byContinent,
    byClass: cache.byClass,
    lastUpdated: cache.lastUpdated,
  }
}
