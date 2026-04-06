#!/usr/bin/env python3
"""
Unified fast concurrent enrichment for ALL wikidata entity types.
Uses asyncio + aiohttp for parallel Wikipedia fetches.

Supports: artifacts, events, evidence, ideas, institutions, movements, timeframes
(Places and People have their own dedicated scripts.)

Usage:
    python3 scripts/enrich_wikidata_fast.py institutions
    python3 scripts/enrich_wikidata_fast.py ideas --batch-size 5000
    python3 scripts/enrich_wikidata_fast.py events --start 1000
    python3 scripts/enrich_wikidata_fast.py movements --concurrency 15
    python3 scripts/enrich_wikidata_fast.py --dry-run artifacts

Output: Updates data/wikidata_{type}.json in place after each batch.
Adds 'enrichedSummary' boolean field to every entity.
"""

import json
import time
import sys
import os
import re
import argparse
import asyncio
import urllib.parse
from typing import Optional

import aiohttp

# ─── Configuration ───
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
BATCH_SIZE = 5_000
CONCURRENCY = 20
REQUEST_TIMEOUT = 15
USER_AGENT = ('AnnalsOfTheWorld/1.0 '
              '(https://github.com/14-yama/annals-of-the-world; research project)')

ENTITY_TYPES = {
    'artifacts':    'wikidata_artifacts.json',
    'events':       'wikidata_events.json',
    'evidence':     'wikidata_evidence.json',
    'ideas':        'wikidata_ideas.json',
    'institutions': 'wikidata_institutions.json',
    'movements':    'wikidata_movements.json',
    'timeframes':   'wikidata_timeframes.json',
}

ERA_CONTEXT = {
    'Prehistoric': 'the prehistoric era, before written records',
    'Classical': 'the Classical era of empires and foundational civilizations',
    'Medieval': 'the Medieval period of feudalism and cultural exchange',
    'Early Modern': 'the Early Modern period of exploration and nation-building',
    'Modern': 'the Modern era of industrialization and global conflict',
    'Contemporary': 'the Contemporary era of technology and globalization',
}


# ─── Helpers ───

def extract_title_from_url(url: str) -> Optional[str]:
    """Extract the Wikipedia article title from a URL."""
    if not url:
        return None
    match = re.search(r'/wiki/(.+?)(?:\?|#|$)', url)
    if match:
        return urllib.parse.unquote(match.group(1))
    return None


def is_generic_summary(summary: str) -> bool:
    """Check if a summary is a short generic template rather than unique content."""
    s = summary.lower().strip()
    if len(s) < 60:
        return True
    # Generic "located in" one-liners
    if 'located in' in s and len(s) < 150:
        return True
    # Boilerplate patterns
    boilerplate = [
        'founded/began:', 'from the', 'dating to',
        'associated with the', 'classified under',
    ]
    pattern_hits = sum(1 for b in boilerplate if b in s)
    # If summary is short and mostly boilerplate, flag it
    if len(s) < 120 and pattern_hits >= 2:
        return True
    return False


def clean_wikipedia_extract(extract: str) -> str:
    """Post-process Wikipedia extract to ensure quality."""
    extract = re.sub(r'\[\d+\]', '', extract)
    extract = re.sub(r'\s*\([^)]*pronunciation[^)]*\)', '', extract)
    extract = re.sub(r'\s*\([^)]*listen[^)]*\)', '', extract)
    if len(extract) > 600:
        for end in range(500, min(len(extract), 700)):
            if extract[end] in '.!?' and (end + 1 >= len(extract) or extract[end + 1] == ' '):
                extract = extract[:end + 1]
                break
        else:
            extract = extract[:600].rsplit('.', 1)[0] + '.'
    return extract.strip()


# ─── Type-specific fallback builders ───

def _get_country(entity: dict) -> str:
    """Extract country from relationships or subjects."""
    for rel in entity.get('relationships', []):
        if rel.get('verb') in ('SITUATED_IN', 'OCCURS_IN', 'PART_OF',
                                'LOCATED_IN', 'HEADQUARTERED_IN'):
            return rel.get('targetName', '')
    subs = entity.get('subjects', [])
    label = entity.get('label', '')
    era = entity.get('era', '')
    for s in subs:
        if s and s not in (label, era, 'Place', entity.get('continent', ''),
                           entity.get('region', '')):
            return s
    return entity.get('region', '') or entity.get('continent', '')


def build_fallback_event(entity: dict) -> str:
    name = entity['name']
    event_type = entity.get('eventType', 'historical event')
    era = entity.get('era', '')
    era_ctx = ERA_CONTEXT.get(era, f'the {era} era') if era else ''
    country = _get_country(entity)
    parts = [f'{name} is a {event_type}']
    if country:
        parts[0] += f' in {country}'
    parts[0] += '.'
    if era_ctx:
        parts.append(f'Occurred during {era_ctx}.')
    causes = entity.get('causes', [])
    if causes:
        parts.append(f'Caused by: {causes[0]}.')
    effects = entity.get('effects', [])
    if effects:
        parts.append(f'Led to: {effects[0]}.')
    return ' '.join(parts)


def build_fallback_institution(entity: dict) -> str:
    name = entity['name']
    inst_type = entity.get('institutionType', 'institution')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is a {inst_type}']
    if country:
        parts[0] += f' based in {country}'
    parts[0] += '.'
    if era:
        parts.append(f'Active during the {era} era.')
    return ' '.join(parts)


def build_fallback_idea(entity: dict) -> str:
    name = entity['name']
    idea_type = entity.get('ideaType', 'idea')
    idea_class = entity.get('ideaClass', '')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is a {idea_type}']
    if idea_class:
        parts[0] += f' in the field of {idea_class}'
    parts[0] += '.'
    if country:
        parts.append(f'Originated in {country}.')
    if era:
        parts.append(f'Emerged during the {era} era.')
    return ' '.join(parts)


def build_fallback_artifact(entity: dict) -> str:
    name = entity['name']
    artifact_type = entity.get('artifactType', 'artifact')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is a {artifact_type}']
    if country:
        parts[0] += f' from {country}'
    parts[0] += '.'
    if era:
        parts.append(f'Dating to the {era} era.')
    return ' '.join(parts)


def build_fallback_movement(entity: dict) -> str:
    name = entity['name']
    move_type = entity.get('movementType', 'movement')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is a {move_type}']
    if country:
        parts[0] += f' originating in {country}'
    parts[0] += '.'
    if era:
        parts.append(f'Active during the {era} era.')
    causes = entity.get('causes', [])
    if causes:
        parts.append(f'Rooted in: {causes[0]}.')
    return ' '.join(parts)


def build_fallback_evidence(entity: dict) -> str:
    name = entity['name']
    ev_type = entity.get('evidenceType', 'evidence')
    tier = entity.get('evidenceTier', '')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is {ev_type}']
    if country:
        parts[0] += f' from {country}'
    parts[0] += '.'
    if tier:
        parts.append(f'Evidence tier: {tier}.')
    if era:
        parts.append(f'Dating to the {era} era.')
    return ' '.join(parts)


def build_fallback_timeframe(entity: dict) -> str:
    name = entity['name']
    tf_type = entity.get('timeframeType', 'time period')
    era = entity.get('era', '')
    country = _get_country(entity)
    parts = [f'{name} is a {tf_type}']
    if country:
        parts[0] += f' in {country}'
    parts[0] += '.'
    if era:
        parts.append(f'Part of the {era} era.')
    return ' '.join(parts)


FALLBACK_BUILDERS = {
    'artifacts':    build_fallback_artifact,
    'events':       build_fallback_event,
    'evidence':     build_fallback_evidence,
    'ideas':        build_fallback_idea,
    'institutions': build_fallback_institution,
    'movements':    build_fallback_movement,
    'timeframes':   build_fallback_timeframe,
}


# ─── Wikipedia fetch ───

async def fetch_wikipedia_summary(session: aiohttp.ClientSession, title: str,
                                   semaphore: asyncio.Semaphore) -> Optional[str]:
    """Fetch the intro paragraph from Wikipedia REST API."""
    encoded = urllib.parse.quote(title, safe='')
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}'

    async with semaphore:
        for attempt in range(3):
            try:
                async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
                ) as resp:
                    if resp.status == 404:
                        return None
                    if resp.status == 429:
                        wait = min(5 * (2 ** attempt), 30)
                        await asyncio.sleep(wait)
                        continue
                    if resp.status != 200:
                        if attempt < 2:
                            await asyncio.sleep(2)
                            continue
                        return None
                    data = await resp.json()
                    extract = data.get('extract', '')
                    if extract and len(extract) > 30:
                        return extract
                    return None
            except (aiohttp.ClientError, asyncio.TimeoutError, OSError):
                if attempt < 2:
                    await asyncio.sleep(2 * (attempt + 1))
                    continue
                return None
        await asyncio.sleep(0.05)
    return None


async def search_wikipedia_title(session: aiohttp.ClientSession, name: str,
                                  semaphore: asyncio.Semaphore) -> Optional[str]:
    """Search Wikipedia for an entity name when no URL is available.
    Returns the best-match article title or None."""
    query = urllib.parse.quote(name, safe='')
    url = (f'https://en.wikipedia.org/w/api.php?action=query&list=search'
           f'&srsearch={query}&srlimit=1&format=json')

    async with semaphore:
        for attempt in range(3):
            try:
                async with session.get(
                    url,
                    timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
                ) as resp:
                    if resp.status == 429:
                        wait = min(5 * (2 ** attempt), 30)
                        await asyncio.sleep(wait)
                        continue
                    if resp.status != 200:
                        if attempt < 2:
                            await asyncio.sleep(2)
                            continue
                        return None
                    data = await resp.json()
                    results = data.get('query', {}).get('search', [])
                    if results:
                        return results[0].get('title')
                    return None
            except (aiohttp.ClientError, asyncio.TimeoutError, OSError):
                if attempt < 2:
                    await asyncio.sleep(2 * (attempt + 1))
                    continue
                return None
        return None


# ─── Batch processing ───

async def process_batch_async(entities: list, start: int, end: int,
                               entity_type: str, concurrency: int = 20,
                               search_missing: bool = True) -> dict:
    """Process a batch of entities with concurrent Wikipedia fetches."""
    end = min(end, len(entities))
    batch = entities[start:end]
    fallback_fn = FALLBACK_BUILDERS[entity_type]

    stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
             'already_enriched': 0, 'skipped_real': 0,
             'search_found': 0, 'search_miss': 0,
             'batch_size': end - start}

    to_fetch = []       # (idx, entity, title) — have Wikipedia URLs
    to_search = []      # (idx, entity) — need name-based search

    for i, entity in enumerate(batch):
        if entity.get('enrichedSummary') is True:
            stats['already_enriched'] += 1
            continue

        summary = entity.get('summary', '')
        is_retry = entity.get('enrichedSummary') is False

        if not is_retry and not is_generic_summary(summary):
            entity['enrichedSummary'] = True
            stats['skipped_real'] += 1
            continue

        wiki_url = entity.get('wikipediaUrl', '')
        title = extract_title_from_url(wiki_url) if wiki_url else None
        if title:
            to_fetch.append((i, entity, title))
        elif search_missing:
            to_search.append((i, entity))
        else:
            entity['summary'] = fallback_fn(entity)
            entity['enrichedSummary'] = False
            stats['fallback_used'] += 1

    SUB_BATCH = concurrency * 5
    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency,
                                      ttl_dns_cache=300, enable_cleanup_closed=True)
    headers = {'User-Agent': USER_AGENT, 'Accept': 'application/json'}

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        # Phase 1: Fetch by URL
        for chunk_start in range(0, len(to_fetch), SUB_BATCH):
            chunk = to_fetch[chunk_start:chunk_start + SUB_BATCH]
            tasks = [fetch_wikipedia_summary(session, title, semaphore)
                     for _, _, title in chunk]
            results = await asyncio.gather(*tasks)

            for (_, entity, _), result in zip(chunk, results):
                if result:
                    entity['summary'] = clean_wikipedia_extract(result)
                    entity['enrichedSummary'] = True
                    stats['wiki_fetched'] += 1
                else:
                    entity['summary'] = fallback_fn(entity)
                    entity['enrichedSummary'] = False
                    stats['wiki_failed'] += 1

            done = chunk_start + len(chunk)
            total_items = len(to_fetch) + len(to_search)
            if total_items > 50:
                global_idx = start + done
                print(f'    [{global_idx:>7,}/{len(entities):,}] '
                      f'url-fetch {done}/{len(to_fetch)} '
                      f'wiki:{stats["wiki_fetched"]} fail:{stats["wiki_failed"]}',
                      flush=True)

        # Phase 2: Search by name (for entities without Wikipedia URLs)
        if to_search:
            # First: search for Wikipedia titles
            search_semaphore = asyncio.Semaphore(max(concurrency // 2, 5))
            for chunk_start in range(0, len(to_search), SUB_BATCH):
                chunk = to_search[chunk_start:chunk_start + SUB_BATCH]
                search_tasks = [
                    search_wikipedia_title(session, entity['name'], search_semaphore)
                    for _, entity in chunk
                ]
                search_results = await asyncio.gather(*search_tasks)

                # Now fetch summaries for found titles
                found_pairs = []
                for (idx, entity), title in zip(chunk, search_results):
                    if title:
                        found_pairs.append((idx, entity, title))
                    else:
                        entity['summary'] = fallback_fn(entity)
                        entity['enrichedSummary'] = False
                        stats['search_miss'] += 1
                        stats['fallback_used'] += 1

                if found_pairs:
                    fetch_tasks = [
                        fetch_wikipedia_summary(session, title, semaphore)
                        for _, _, title in found_pairs
                    ]
                    fetch_results = await asyncio.gather(*fetch_tasks)

                    for (_, entity, _), result in zip(found_pairs, fetch_results):
                        if result:
                            entity['summary'] = clean_wikipedia_extract(result)
                            entity['enrichedSummary'] = True
                            stats['wiki_fetched'] += 1
                            stats['search_found'] += 1
                        else:
                            entity['summary'] = fallback_fn(entity)
                            entity['enrichedSummary'] = False
                            stats['wiki_failed'] += 1

                done_search = chunk_start + len(chunk)
                global_idx = start + len(to_fetch) + done_search
                print(f'    [{global_idx:>7,}/{len(entities):,}] '
                      f'name-search {done_search}/{len(to_search)} '
                      f'found:{stats["search_found"]} miss:{stats["search_miss"]}',
                      flush=True)

    return stats


def load_data(entity_type: str) -> dict:
    """Load the entity JSON file."""
    fpath = os.path.join(DATA_DIR, ENTITY_TYPES[entity_type])
    print(f'Loading {fpath}...', flush=True)
    with open(fpath, 'r') as f:
        data = json.load(f)
    print(f'  Loaded {len(data["entities"]):,} entities', flush=True)
    return data


def save_data(data: dict, entity_type: str) -> None:
    """Save the entity JSON file."""
    fpath = os.path.join(DATA_DIR, ENTITY_TYPES[entity_type])
    print(f'  Saving {fpath}...', flush=True)
    with open(fpath, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    size_mb = os.path.getsize(fpath) / 1024 / 1024
    print(f'  Saved ({size_mb:.1f} MB)', flush=True)


async def main_async():
    parser = argparse.ArgumentParser(
        description='Fast concurrent Wikipedia enrichment for wikidata entity files')
    parser.add_argument('type', choices=sorted(ENTITY_TYPES.keys()),
                        help='Entity type to enrich')
    parser.add_argument('--batch-size', type=int, default=BATCH_SIZE)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=None)
    parser.add_argument('--concurrency', type=int, default=CONCURRENCY)
    parser.add_argument('--no-search', action='store_true',
                        help='Skip name-based Wikipedia search for entities without URLs')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    entity_type = args.type
    search_missing = not args.no_search

    data = load_data(entity_type)
    total = len(data['entities'])
    end = args.end or total

    enriched_count = sum(1 for e in data['entities'] if e.get('enrichedSummary'))
    generic_count = sum(1 for e in data['entities']
                        if is_generic_summary(e.get('summary', '')))
    no_wiki_url = sum(1 for e in data['entities'] if not e.get('wikipediaUrl'))
    print(f'  Already enriched: {enriched_count:,}', flush=True)
    print(f'  Generic summaries needing enrichment: {generic_count:,}', flush=True)
    print(f'  Entities without Wikipedia URL: {no_wiki_url:,}', flush=True)
    print(f'  Range: [{args.start:,} → {end:,}]', flush=True)
    print(f'  Batch size: {args.batch_size:,} | Concurrency: {args.concurrency}',
          flush=True)
    print(f'  Name-based search: {"ON" if search_missing else "OFF"}', flush=True)
    print(flush=True)

    grand_stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
                   'already_enriched': 0, 'skipped_real': 0,
                   'search_found': 0, 'search_miss': 0}
    batch_num = 0
    cursor = args.start
    start_time = time.time()

    while cursor < end:
        batch_end = min(cursor + args.batch_size, end)
        batch_num += 1
        print(f'═══ Batch {batch_num}: [{cursor:,} → {batch_end:,}] ═══', flush=True)

        batch_start = time.time()
        if args.dry_run:
            stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
                     'already_enriched': 0, 'skipped_real': 0,
                     'search_found': 0, 'search_miss': 0,
                     'batch_size': batch_end - cursor}
        else:
            stats = await process_batch_async(
                data['entities'], cursor, batch_end,
                entity_type, args.concurrency, search_missing)
        batch_elapsed = time.time() - batch_start

        for k in grand_stats:
            grand_stats[k] += stats.get(k, 0)

        print(f'  {batch_elapsed:.1f}s — wiki:{stats["wiki_fetched"]} '
              f'fail:{stats["wiki_failed"]} fallback:{stats["fallback_used"]} '
              f'real:{stats["skipped_real"]} skip:{stats["already_enriched"]}'
              + (f' search-found:{stats["search_found"]} '
                 f'search-miss:{stats["search_miss"]}'
                 if stats.get('search_found') or stats.get('search_miss') else ''),
              flush=True)

        if not args.dry_run:
            if '_meta' not in data:
                data['_meta'] = {}
            data['_meta']['enrichment_progress'] = {
                'type': entity_type,
                'last_batch_end': batch_end,
                'total_wiki_fetched': grand_stats['wiki_fetched'],
                'total_enriched': sum(1 for e in data['entities']
                                      if e.get('enrichedSummary')),
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            }
            save_data(data, entity_type)

        cursor = batch_end
        elapsed = time.time() - start_time
        processed = cursor - args.start
        if processed > 0:
            rate = processed / elapsed
            remaining = end - cursor
            eta = remaining / rate if rate > 0 else 0
            print(f'  [{cursor:,}/{end:,}] {cursor / end * 100:.1f}% '
                  f'| {rate:.0f}/s | ETA: {eta / 60:.0f}m', flush=True)
        print(flush=True)

    elapsed = time.time() - start_time
    print(f'{"=" * 60}', flush=True)
    print(f'ENRICHMENT COMPLETE — {entity_type.upper()}', flush=True)
    print(f'  Processed: {end - args.start:,}', flush=True)
    print(f'  Wikipedia fetched: {grand_stats["wiki_fetched"]:,}', flush=True)
    print(f'  Wikipedia failed:  {grand_stats["wiki_failed"]:,}', flush=True)
    print(f'  Search found:      {grand_stats["search_found"]:,}', flush=True)
    print(f'  Search missed:     {grand_stats["search_miss"]:,}', flush=True)
    print(f'  Fallback (no URL): {grand_stats["fallback_used"]:,}', flush=True)
    print(f'  Already real:      {grand_stats["skipped_real"]:,}', flush=True)
    print(f'  Already enriched:  {grand_stats["already_enriched"]:,}', flush=True)
    print(f'  Elapsed: {elapsed / 60:.1f}m ({elapsed / 3600:.1f}h)', flush=True)


def main():
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
