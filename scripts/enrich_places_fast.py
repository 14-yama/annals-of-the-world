#!/usr/bin/env python3
"""
Fast concurrent enrichment of wikidata_places.json using Wikipedia REST API.

Uses asyncio + aiohttp for parallel Wikipedia fetches.
Processes in configurable batches, writes progress after each batch, and can
resume from where it left off using the enrichedSummary flag.

Usage:
    python3 scripts/enrich_places_fast.py                    # Run all
    python3 scripts/enrich_places_fast.py --batch-size 5000
    python3 scripts/enrich_places_fast.py --start 10000      # Resume from index
    python3 scripts/enrich_places_fast.py --concurrency 20
    python3 scripts/enrich_places_fast.py --dry-run

Output: Updates data/wikidata_places.json in place after each batch.
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
INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'wikidata_places.json')
BATCH_SIZE = 5_000
CONCURRENCY = 20       # Max concurrent HTTP requests
REQUEST_TIMEOUT = 15   # Seconds per request
USER_AGENT = 'AnnalsOfTheWorld/1.0 (https://github.com/14-yama/annals-of-the-world; research project)'

# ─── Division descriptions for places ───
DIVISION_LABELS = {
    '410': 'Continents & Supranational Regions',
    '420': 'Historical Empires & Kingdoms',
    '421': 'Ancient Empires',
    '422': 'Medieval Kingdoms & Caliphates',
    '423': 'Colonial Empires',
    '424': 'Modern Nation-States',
    '425': 'Autonomous Regions & Territories',
    '426': 'Disputed Territories',
    '430': 'Modern Countries & Sovereign States',
    '440': 'Cities & Urban Centers',
    '441': 'Capital Cities',
    '442': 'Religious & Pilgrimage Sites',
    '443': 'Trade & Port Cities',
    '444': 'Ancient & Ruined Cities',
    '450': 'Historical Empires',
    '451': 'Lost Civilizations',
    '452': 'Colonial Territories',
    '460': 'Geographic Features',
    '461': 'Mountain Ranges & Peaks',
    '462': 'Islands & Archipelagos',
    '463': 'Rivers & Waterways',
    '464': 'Deserts & Plains',
    '465': 'Forests & Ecological Zones',
    '470': 'Landmarks & Monuments',
    '471': 'Temples, Churches & Mosques',
    '472': 'Fortresses & Castles',
    '473': 'Palaces & Government Buildings',
    '480': 'Battlefields & Conflict Sites',
    '481': 'Treaty & Diplomatic Sites',
    '490': 'Routes & Networks',
    '491': 'Trade Routes',
    '492': 'Migration Paths',
}

ERA_CONTEXT = {
    'Prehistoric': 'the prehistoric era, before written records',
    'Classical': 'the Classical era of empires and foundational civilizations',
    'Medieval': 'the Medieval period of feudalism and cultural exchange',
    'Early Modern': 'the Early Modern period of exploration and nation-building',
    'Modern': 'the Modern era of industrialization and global conflict',
    'Contemporary': 'the Contemporary era of technology and globalization',
}


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
    # Typical pattern: "description Located in Country. Founded year. Population: N."
    if 'located in' in s and len(s) < 150:
        return True
    # Very short summaries with no real info
    if len(s) < 60:
        return True
    return False


def clean_wikipedia_extract(extract: str) -> str:
    """Post-process Wikipedia extract to ensure quality."""
    # Remove citation markers like [1], [2]
    extract = re.sub(r'\[\d+\]', '', extract)
    # Remove pronunciation guides
    extract = re.sub(r'\s*\([^)]*pronunciation[^)]*\)', '', extract)
    extract = re.sub(r'\s*\([^)]*listen[^)]*\)', '', extract)
    # Cap at 600 chars at sentence boundary
    if len(extract) > 600:
        for end in range(500, min(len(extract), 700)):
            if extract[end] in '.!?' and (end + 1 >= len(extract) or extract[end + 1] == ' '):
                extract = extract[:end + 1]
                break
        else:
            extract = extract[:600].rsplit('.', 1)[0] + '.'
    return extract.strip()


def build_fallback_summary(entity: dict) -> str:
    """Build a summary without Wikipedia, using entity metadata."""
    name = entity['name']
    place_type = entity.get('placeType', 'place')
    era = entity.get('era', '')
    era_ctx = ERA_CONTEXT.get(era, f'the {era} era') if era else ''
    region = entity.get('region', '')
    continent = entity.get('continent', '')
    founded = entity.get('founded', '')
    population = entity.get('population', '')
    div_heading = entity.get('divisionHeading', '')

    # Build location context
    country = ''
    for rel in entity.get('relationships', []):
        if rel.get('verb') in ('SITUATED_IN', 'OCCURS_IN', 'PART_OF'):
            country = rel.get('targetName', '')
            break
    if not country:
        subs = entity.get('subjects', [])
        for s in subs:
            if s not in (place_type, div_heading, continent, region, era, 'Place'):
                country = s
                break

    parts = [f'{name} is a {place_type}']
    if country:
        parts[0] += f' in {country}'
    elif region:
        parts[0] += f' in {region}'
    parts[0] += '.'

    if founded:
        parts.append(f'Founded {founded}.')
    if population:
        if isinstance(population, (int, float)):
            parts.append(f'Population: {population:,.0f}.')
        else:
            parts.append(f'Population: {population}.')
    if era_ctx:
        parts.append(f'Active during {era_ctx}.')
    if div_heading and div_heading != place_type:
        parts.append(f'Classified under {div_heading}.')

    return ' '.join(parts)


async def fetch_wikipedia_summary(session: aiohttp.ClientSession, title: str,
                                   semaphore: asyncio.Semaphore) -> Optional[str]:
    """Fetch the intro paragraph from Wikipedia REST API."""
    encoded = urllib.parse.quote(title, safe='')
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}'

    async with semaphore:
        for attempt in range(3):
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)) as resp:
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


async def process_batch_async(entities: list, start: int, end: int, concurrency: int = 20) -> dict:
    """Process a batch of entities with concurrent Wikipedia fetches."""
    end = min(end, len(entities))
    batch = entities[start:end]

    stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
             'already_enriched': 0, 'skipped_real': 0, 'batch_size': end - start}

    to_fetch = []
    for i, entity in enumerate(batch):
        if entity.get('enrichedSummary') is True:
            stats['already_enriched'] += 1
            continue

        summary = entity.get('summary', '')
        is_retry = entity.get('enrichedSummary') is False

        # If it has a real (non-generic) summary already, keep it
        if not is_retry and not is_generic_summary(summary):
            entity['enrichedSummary'] = True
            stats['skipped_real'] += 1
            continue

        wiki_url = entity.get('wikipediaUrl', '')
        title = extract_title_from_url(wiki_url) if wiki_url else None
        if title:
            to_fetch.append((i, entity, title))
        else:
            entity['summary'] = build_fallback_summary(entity)
            entity['enrichedSummary'] = False
            stats['fallback_used'] += 1

    # Fetch Wikipedia summaries in sub-batches
    SUB_BATCH = concurrency * 5  # 100 at a time with 20 concurrency
    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency,
                                      ttl_dns_cache=300, enable_cleanup_closed=True)
    headers = {'User-Agent': USER_AGENT, 'Accept': 'application/json'}

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
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
                    entity['summary'] = build_fallback_summary(entity)
                    entity['enrichedSummary'] = False
                    stats['wiki_failed'] += 1

            done = chunk_start + len(chunk)
            total_to_fetch = len(to_fetch)
            if total_to_fetch > 50:
                global_idx = start + done
                print(f'    [{global_idx:>7,}/{len(entities):,}] '
                      f'sub-batch {done}/{total_to_fetch} '
                      f'wiki:{stats["wiki_fetched"]} fail:{stats["wiki_failed"]}',
                      flush=True)

    return stats


def load_data() -> dict:
    """Load the places JSON file."""
    print(f'Loading {INPUT_FILE}...', flush=True)
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
    print(f'  Loaded {len(data["entities"]):,} entities', flush=True)
    return data


def save_data(data: dict) -> None:
    """Save the places JSON file."""
    print(f'  Saving...', flush=True)
    with open(INPUT_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    size_mb = os.path.getsize(INPUT_FILE) / 1024 / 1024
    print(f'  Saved ({size_mb:.1f} MB)', flush=True)


async def main_async():
    parser = argparse.ArgumentParser(description='Fast concurrent Wikipedia enrichment for places')
    parser.add_argument('--batch-size', type=int, default=BATCH_SIZE)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=None)
    parser.add_argument('--concurrency', type=int, default=CONCURRENCY)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    concurrency = args.concurrency

    data = load_data()
    total = len(data['entities'])
    end = args.end or total

    enriched_count = sum(1 for e in data['entities'] if e.get('enrichedSummary'))
    generic_count = sum(1 for e in data['entities'] if is_generic_summary(e.get('summary', '')))
    print(f'  Already enriched: {enriched_count:,}', flush=True)
    print(f'  Generic summaries needing enrichment: {generic_count:,}', flush=True)
    print(f'  Range: [{args.start:,} → {end:,}]', flush=True)
    print(f'  Batch size: {args.batch_size:,} | Concurrency: {concurrency}', flush=True)
    print(flush=True)

    grand_stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
                   'already_enriched': 0, 'skipped_real': 0}
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
                     'already_enriched': 0, 'skipped_real': 0, 'batch_size': batch_end - cursor}
        else:
            stats = await process_batch_async(data['entities'], cursor, batch_end, concurrency)
        batch_elapsed = time.time() - batch_start

        for k in grand_stats:
            grand_stats[k] += stats.get(k, 0)

        print(f'  {batch_elapsed:.1f}s — wiki:{stats["wiki_fetched"]} '
              f'fail:{stats["wiki_failed"]} fallback:{stats["fallback_used"]} '
              f'real:{stats["skipped_real"]} skip:{stats["already_enriched"]}', flush=True)

        if not args.dry_run:
            data['_meta']['enrichment_progress'] = {
                'last_batch_end': batch_end,
                'total_wiki_fetched': grand_stats['wiki_fetched'],
                'total_enriched': sum(1 for e in data['entities'] if e.get('enrichedSummary')),
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            }
            save_data(data)

        cursor = batch_end
        elapsed = time.time() - start_time
        processed = cursor - args.start
        if processed > 0:
            rate = processed / elapsed
            remaining = end - cursor
            eta = remaining / rate if rate > 0 else 0
            print(f'  [{cursor:,}/{end:,}] {cursor/end*100:.1f}% '
                  f'| {rate:.0f}/s | ETA: {eta/60:.0f}m', flush=True)
        print(flush=True)

    elapsed = time.time() - start_time
    print(f'{"=" * 60}', flush=True)
    print(f'ENRICHMENT COMPLETE', flush=True)
    print(f'  Processed: {end - args.start:,}', flush=True)
    print(f'  Wikipedia fetched: {grand_stats["wiki_fetched"]:,}', flush=True)
    print(f'  Wikipedia failed:  {grand_stats["wiki_failed"]:,}', flush=True)
    print(f'  Fallback (no URL): {grand_stats["fallback_used"]:,}', flush=True)
    print(f'  Already real:      {grand_stats["skipped_real"]:,}', flush=True)
    print(f'  Already enriched:  {grand_stats["already_enriched"]:,}', flush=True)
    print(f'  Elapsed: {elapsed/60:.1f}m ({elapsed/3600:.1f}h)', flush=True)


def main():
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
