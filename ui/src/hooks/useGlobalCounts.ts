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
import { ExecutionMethod } from 'appwrite'

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

// Cache TTL: 10 minutes (matches function schedule)
const CACHE_TTL = 10 * 60 * 1000

const cache: CountCache = {
  total: 0,
  byLabel: {},
  byEra: {},
  byContinent: {},
  byClass: {},
  lastUpdated: null,
  promise: null,
}

// Listeners for reactive updates
const listeners = new Set<() => void>()
function notify() { listeners.forEach(fn => fn()) }

/**
 * Read pre-computed stats from the stats_cache collection.
 * Single document read — ~50ms.
 */
async function fetchFromStatsCache(): Promise<boolean> {
  try {
    const doc = await databases.getDocument(
      DATABASE_ID,
      COLLECTIONS.STATS_CACHE,
      'global'
    )

    cache.total = doc.total || 0
    cache.byLabel = typeof doc.byLabel === 'string' ? JSON.parse(doc.byLabel) : (doc.byLabel || {})
    cache.byEra = typeof doc.byEra === 'string' ? JSON.parse(doc.byEra) : (doc.byEra || {})
    cache.byContinent = typeof doc.byContinent === 'string' ? JSON.parse(doc.byContinent) : (doc.byContinent || {})
    cache.byClass = typeof doc.byClass === 'string' ? JSON.parse(doc.byClass) : (doc.byClass || {})
    cache.lastUpdated = Date.now()
    return true
  } catch {
    return false
  }
}

/**
 * Fallback: trigger the stats function and use its response.
 */
async function fetchViaFunction(): Promise<boolean> {
  try {
    const execution = await functions.createExecution(
      'audit-consistency',
      JSON.stringify({}),
      false, // async = false (wait for result)
      undefined,
      ExecutionMethod.POST,
    )

    if (execution.responseStatusCode === 200 && execution.responseBody) {
      const data = JSON.parse(execution.responseBody)
      cache.total = data.total || 0
      cache.byLabel = data.byLabel || {}
      cache.byEra = data.byEra || {}
      cache.byContinent = data.byContinent || {}
      cache.byClass = data.byClass || {}
      cache.lastUpdated = Date.now()
      return true
    }
    return false
  } catch {
    return false
  }
}

/**
 * Fetches global counts — tries stats_cache first, falls back to function.
 */
async function fetchAllCounts(): Promise<void> {
  const ok = await fetchFromStatsCache()
  if (!ok) {
    await fetchViaFunction()
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
