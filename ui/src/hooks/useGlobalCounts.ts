/**
 * useGlobalCounts — Shared hook for accurate, cached entity counts.
 *
 * Uses cursor-based pagination (countAllDocuments) to bypass Appwrite's
 * 5,000 res.total cap. Counts are cached in memory and shared across
 * components via a module-level singleton.
 *
 * Usage:
 *   const { total, byLabel, byEra, byContinent, byClass, loading } = useGlobalCounts()
 */
import { useEffect, useState, useCallback } from 'react'
import { Query } from 'appwrite'
import { databases, DATABASE_ID, COLLECTIONS } from '../lib/appwrite'

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

const LABELS = ['Person', 'Idea', 'Institution', 'Place', 'EventWindow', 'Movement', 'Text', 'Evidence', 'Timeframe']
const ERAS = ['Prehistoric', 'Classical', 'Medieval', 'Early Modern', 'Modern', 'Contemporary']
const CONTINENTS = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Multiple Regions']
const CLASSES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

// Cache TTL: 5 minutes
const CACHE_TTL = 5 * 60 * 1000

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
 * Accurate count via cursor-based pagination.
 * Selects only $id to minimise payload.
 */
async function accurateCount(extraQueries: string[] = []): Promise<number> {
  const PAGE = 100
  let count = 0
  let cursor: string | undefined

  while (true) {
    const q: string[] = [
      ...extraQueries,
      Query.select(['$id']),
      Query.limit(PAGE),
    ]
    if (cursor) q.push(Query.cursorAfter(cursor))

    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, q)
    count += res.documents.length

    if (res.documents.length < PAGE) break
    cursor = res.documents[res.documents.length - 1].$id
  }

  return count
}

/**
 * Count by field value using res.total (fast single query).
 * For values with <5000 entities per group, res.total is accurate.
 * For larger groups, falls back to cursor pagination.
 */
async function countByFieldValue(field: string, value: string): Promise<number> {
  const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
    Query.equal(field, value),
    Query.limit(1),
  ])
  // If total is exactly 5000, it's likely capped — use accurate count
  if (res.total >= 5000) {
    return accurateCount([Query.equal(field, value)])
  }
  return res.total
}

/**
 * Fetches all global counts. Deduplicates concurrent calls.
 */
async function fetchAllCounts(): Promise<void> {
  // Fetch total accurately
  const totalPromise = accurateCount()

  // Fetch per-label counts (parallel)
  const labelPromises = LABELS.map(async (label) => ({
    label,
    count: await countByFieldValue('label', label),
  }))

  // Fetch per-era counts (parallel)
  const eraPromises = ERAS.map(async (era) => ({
    era,
    count: await countByFieldValue('era', era),
  }))

  // Fetch per-continent counts (parallel)
  const continentPromises = CONTINENTS.map(async (continent) => ({
    continent,
    count: await countByFieldValue('continent', continent),
  }))

  // Fetch per-class counts (parallel)
  const classPromises = CLASSES.map(async (cls) => {
    const res = await databases.listDocuments(DATABASE_ID, COLLECTIONS.ENTITIES, [
      Query.startsWith('callNumber', cls),
      Query.limit(1),
    ])
    const count = res.total >= 5000
      ? await accurateCount([Query.startsWith('callNumber', cls)])
      : res.total
    return { cls, count }
  })

  const [total, labelResults, eraResults, continentResults, classResults] = await Promise.all([
    totalPromise,
    Promise.all(labelPromises),
    Promise.all(eraPromises),
    Promise.all(continentPromises),
    Promise.all(classPromises),
  ])

  cache.total = total
  cache.byLabel = Object.fromEntries(labelResults.map(r => [r.label, r.count]))
  cache.byEra = Object.fromEntries(eraResults.map(r => [r.era, r.count]))
  cache.byContinent = Object.fromEntries(continentResults.map(r => [r.continent, r.count]))
  cache.byClass = Object.fromEntries(classResults.map(r => [r.cls, r.count]))
  cache.lastUpdated = Date.now()
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
