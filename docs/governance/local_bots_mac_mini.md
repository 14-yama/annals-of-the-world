# Annals Local Bots — Mac Mini Roster

> Source of truth: [`data/governance/platform-local-bots.json`](../../data/governance/platform-local-bots.json)
>
> Host: 24 GB Mac Mini · Timezone: `America/Port_of_Spain` (AST)
> LaunchAgent prefix: `com.annals.*` (never touches Superstack `com.caricom.*`)

## Mental model

Many bot **definitions** are fine. **Concurrency** is gated so they share 24 GB RAM and mostly do not run at once. While Superstack is quiet, Annals should maximize useful pool use — without colliding with the two daily media-house scrapers.

## Protected Superstack scrapers (do not interrupt)

| Bot | LaunchAgent | Schedule (AST) | Ollama? | Role |
|-----|-------------|----------------|---------|------|
| Daily new-article bot | `com.caricom.media-daily-new-articles` | `10 18 * * *` (18:10) | No | Fresh media-house harvest |
| Archive backfill (listing) | `com.caricom.media-archive-backfill-listing` | `35 20 * * *` (20:35) | No | One shallow house backfill |

**Blackout windows** (Annals heavy/LLM/network bots skip) — narrowed because Superstack scrapers do **not** use Ollama `:11434`:

| Window | Local time (AST) | Protects |
|--------|------------------|----------|
| `daily-harvest` | 18:05–18:50 | media-daily-new-articles |
| `listing-backfill` | 20:30–21:05 | media-archive-backfill-listing |

Bots also **yield immediately** if a protected scraper process / LaunchAgent is actively running, even outside those clocks.

## Throughput targets (Ollama lane)

| Metric | Target |
|--------|--------|
| Combined enrich + significance | **140–220 entities/hour** when Mini is quiet (3× llama3.2:3b) |
| Floor (with Cursor + scrapers) | ~80 entities/hour |
| Cadence | KeepAlive waiters (ThrottleInterval 5–8s) |
| Batch | `--count 32` per fire; `max_concurrent_llm=3` / `OLLAMA_NUM_PARALLEL=3` |
| Sync | every 5 min, `--max=400` (network_write lock) |
| KPI | every 5 min |
| stats_cache | twice hourly (`:15` / `:45` AST) — full facet scan is heavy on MariaDB |

Single LLM lane on `:11434`. Gemini stays out of the Mini track.

## Roster (definitions)

| ID | Cadence | Lane | Role |
|----|---------|------|------|
| `bot-server` | KeepAlive | always_on | HTTP API `:7474` for Curator UI |
| `healthcheck` | every 5 min (`StartInterval`) | always_on | Ollama + bot-server keepalive |
| `enrich` | every 2 min (`StartInterval`) | ollama | `ai_enrich_autonomous.py` via Ollama |
| `significance` | every 2 min (`StartInterval`) | ollama | `backfill_significance.py` (serialized vs enrich) |
| `queue` | every 30 min | light/heavy_scan | Regenerate enrichment queue |
| `kpi` | every 10 min (`StartInterval`) | light | Local KPI rollup → `ui/public/governance` |
| `stats-cache` | `:15`/`:45` hourly (calendar) | light | Live entity counts → Appwrite `stats_cache` (must select `$id` for cursorAfter) |
| `push` | :55 hourly | light | Git commit + push pending enrichments |
| `sync` | every 5 min (`StartInterval`) | network_write | `sync_gateway.ts --local` → Appwrite |
| `edges-extract` | 11:00 daily | heavy_scan | Promote relationships → edges (no LLM) |
| `seed-local` | every 20 min | network_write | Staged git → local Appwrite create-if-missing |
| `merge-cloud` | every 25 min | network_write | Cloud → local entities create-if-missing |
| `merge-cloud-audit` | every 20 min | network_write | Cloud → local `audit_log` create-if-missing |
| `audit-stats` | 01:00 daily | heavy_scan | Corpus stats |
| `audit-completeness` | 02:00 daily | heavy_scan | Completeness audit |
| `audit-orphans` | 03:00 daily | heavy_scan | Zero-relationship entities |
| `orphan-triage` | 03:30 daily | heavy_scan | Orphan CSV/HTML helper |
| `audit-consistency` | 04:00 daily | heavy_scan | Consistency audit |
| `audit-duplicates` | Sun 05:00 | heavy_scan | Fuzzy duplicates |
| `audit-classification` | Sun 06:00 | heavy_scan | Classification validation |

**Concurrent vs defined:** ~20 definitions installed; typically bot-server always-on + up to **3** Ollama enrich/sig workers (`max_concurrent_llm=3`) plus light/network jobs. Local LLM is **Ollama only** (no Gemini on the Mini track).

## Concurrency enforcement

Implemented in `scripts/local_bots/concurrency_gate.py`, called by every scheduled dispatch:

1. **Calendar blackout** vs Superstack scrap windows
2. **Live scraper yield** (`ps` + `launchctl print` for protected labels)
3. **File locks** under `/tmp/annals-bot-locks/`:
   - `ollama` / `ollama_slot_0..2` — up to 3 parallel llama3.2:3b gens; enrich waiters soft-skip when full
   - `heavy_scan` — one audit/queue/edges/orphan job at a time
   - `network_write` / `git` — sync and push serialize lightly

`max_concurrent_llm=3` + `OLLAMA_NUM_PARALLEL=3` on M5 Pro 24 GB (3B model ~2.6 GB); leave headroom for Cursor/MariaDB/Appwrite.

## Install / start / stop / status (Mac Mini)

```bash
# One-shot install (writes ~/.config/annals/env if missing, installs LaunchAgents)
bash scripts/install_local_services.sh

# Or mac-only:
python3 scripts/local_bots/install_mac_launch_agents.py

# Control
bash scripts/local_bots/ctl.sh status
bash scripts/local_bots/ctl.sh start      # (re)install + load
bash scripts/local_bots/ctl.sh stop       # bootout all com.annals.*
bash scripts/local_bots/ctl.sh restart
bash scripts/local_bots/ctl.sh gate       # blackout + locks snapshot
bash scripts/local_bots/ctl.sh run enrich # manual one-shot (respects gate)
bash scripts/local_bots/ctl.sh logs enrich
```

Logs: `~/Library/Logs/annals-bots/<bot-id>.log`

## What we deliberately do **not** do on the Mini

- Do **not** run `scripts/local_bot_daemon.sh` alongside discrete LaunchAgents (would double-enrich).
- Do **not** install/modify any `com.caricom.*` agent from Annals scripts.
- Do **not** use systemd units as the primary path on macOS (kept for Linux hosts only).

## UI

| Page | Route | Count source |
|------|-------|--------------|
| Bot KPI | `http://localhost:5173/curator/bots` | `local_kpi.json` + live `audit_log` |
| Bot timetable (Superstack schedule UX) | `http://localhost:5173/curator/bots/schedule` | `platform-local-bots.json` |
| Ollama monitor | `http://localhost:5173/curator/ollama` | bot-server `:7474` |
| Audit log | `http://localhost:5173/curator/audit/log` | local Appwrite `audit_log` (local + cloud-merged); timestamps forced to **America/Port_of_Spain (AST)** |
| Catalog / ClassHub / Audit dashboard | `/catalog`, `/curator/classes`, `/curator/audit` | `stats_cache` (+ public mirror) |

Curator Ollama monitor talks to `http://localhost:7474` (`bot-server`). KPI aggregator + `stats-cache` bot mirror rollups to `ui/public/governance/`. Manual UI triggers remain on the HTTP API. Local Appwrite: `http://localhost:8080`.

```bash
# Manual KPI / stats refresh
python3 scripts/local_kpi_aggregator.py
npx tsx scripts/refresh_local_stats_cache.ts
```

### If entity pages hang while bots run

A past `stats-cache` bug omitted `$id` from `Query.select`, so `cursorAfter` never advanced and the facet pass re-scanned forever (multi‑GB log, MariaDB starved, UI stuck on “Loading Entity…”). Fixed in `scripts/refresh_local_stats_cache.ts`. If a runaway is still alive:

```bash
bash scripts/local_bots/stop_runaway_stats_cache.sh
```

That boots out only `stats-cache` (+ refreshes the `sync` plist), leaves enrich running, and installs the twice-hourly calendar schedule.

### UI auto-sync

| Surface | Refresh |
|---------|---------|
| `/curator/bots/schedule` | `useLocalBotDesk` polls KPI + `/local-bots/bots/status` every **5s** (+ focus) |
| `/curator/bots` | existing 3–15s intervals |
| `/entity/:slug` | soft revalidate every **25s** + focus (no loading flash) |
| Catalog / class counts | `useGlobalCounts` every **60s** + focus |
| Enrichment progress | audit/bots every **30s** / **5s** |
