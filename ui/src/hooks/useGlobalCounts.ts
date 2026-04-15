/**
 * useGlobalCounts — Shared hook for fast, cached entity counts.
 *
 * Reads pre-computed stats from the `stats_cache` collection (populated every
 * 10 min by the audit-consistency Appwrite function). Falls back to a single
 * function execution if the cache document is missing or stale.
 *
 * Single document read → ~50ms (vs 30s+ with cursor pagination).
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
}

// Cache TTL: 60 minutes (stats are now on-demand, not scheduled)
const CACHE_TTL = 60 * 60 * 1000

const LOCALSTORAGE_KEY = 'annals_global_counts'

const cache: CountCache = {
  total: 0,
  byLabel: {},
  byEra: {},
  byContinent: {},
  byClass: {},
  lastUpdated: null,
  promise: null,
}

// Hydrate from localStorage on module load
try {
  const stored = localStorage.getItem(LOCALSTORAGE_KEY)
  if (stored) {
    const parsed = JSON.parse(stored)
    if (parsed.ts && (Date.now() - parsed.ts) < CACHE_TTL) {
      cache.total = parsed.total || 0
      cache.byLabel = parsed.byLabel || {}
      cache.byEra = parsed.byEra || {}
      cache.byContinent = parsed.byContinent || {}
      cache.byClass = parsed.byClass || {}
      cache.lastUpdated = parsed.ts
    }
  }
} catch { /* localStorage may not be available */ }

// Listeners for reactive updates
const listeners = new Set<() => void>()
function notify() { listeners.forEach(fn => fn()) }

/**
 * Read the most recent pre-computed stats row from stats_cache.
 * Queries by updatedAt descending, takes the latest row.
 */
async function fetchFromStatsCache(): Promise<boolean> {
  try {
    const result = await databases.listDocuments(
      DATABASE_ID,
      COLLECTIONS.STATS_CACHE,
      [Query.orderDesc('updatedAt'), Query.limit(1)]
    )

    if (result.documents.length === 0) return false
    const doc = result.documents[0]

    cache.total = doc.total || 0
    cache.byLabel = typeof doc.byLabel === 'string' ? JSON.parse(doc.byLabel) : (doc.byLabel || {})
    cache.byEra = typeof doc.byEra === 'string' ? JSON.parse(doc.byEra) : (doc.byEra || {})
    cache.byContinent = typeof doc.byContinent === 'string' ? JSON.parse(doc.byContinent) : (doc.byContinent || {})
    cache.byClass = typeof doc.byClass === 'string' ? JSON.parse(doc.byClass) : (doc.byClass || {})
    cache.lastUpdated = Date.now()

    // Persist to localStorage to survive page refreshes
    try {
      localStorage.setItem(LOCALSTORAGE_KEY, JSON.stringify({
        total: cache.total, byLabel: cache.byLabel, byEra: cache.byEra,
        byContinent: cache.byContinent, byClass: cache.byClass, ts: cache.lastUpdated,
      }))
    } catch { /* non-fatal */ }

    return true
  } catch {
    return false
  }
}

/**
 * Fallback: trigger the stats function ASYNC and use its response.
 * Fire-and-forget — don't block the UI waiting 30s+ for a recount.
 */
async function fetchViaFunction(): Promise<boolean> {
  try {
    // Trigger async (fire-and-forget) — it will write stats_cache when done
    await functions.createExecution(
      'audit-consistency',
      JSON.stringify({}),
      true, // async = true — DON'T block the UI
      undefined,
      ExecutionMethod.POST,
    )
    // We can't read the result immediately, but stats_cache will be updated
    // within ~60s. Mark cache as "partially loaded" so UI shows what it has.
    return false
  } catch {
    return false
  }
}

/**
 * Fetches global counts — tries stats_cache first, fires async fallback if empty.
 * Never blocks the UI for 30s+ waiting for a full recount.
 */
async function fetchAllCounts(): Promise<void> {
  const ok = await fetchFromStatsCache()
  if (!ok) {
    // Fire-and-forget: trigger async stats recount, but don't block
    fetchViaFunction()
    // Set a short TTL so we retry reading stats_cache soon
    cache.lastUpdated = Date.now() - CACHE_TTL + 30_000 // retry in 30s
  }
  cache.promise = null
  notify()
}

/**
 * Ensure counts are loaded. Returns existing promise if one is in flight.
 */
function ensureCounts(): Promise<void> {
  if (cache.lastUpdated && (Date.now() - cache.lastUpdated) < CACHE_TTL) {
    return Promise.resolve()
  }
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
    ensureCounts()
  }, [])

  useEffect(() => {
    const listener = () => setTick(t => t + 1)
    listeners.add(listener)

    ensureCounts()

    return () => { listeners.delete(listener) }
  }, [])

  return {
    total: cache.total,
    byLabel: cache.byLabel,
    byEra: cache.byEra,
    byContinent: cache.byContinent,
    byClass: cache.byClass,
    loading: cache.promise !== null && cache.lastUpdated === null,
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
