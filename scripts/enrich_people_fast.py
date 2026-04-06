#!/usr/bin/env python3
"""
Fast concurrent enrichment of wikidata_people.json using Wikipedia REST API.

Uses asyncio + aiohttp for parallel Wikipedia fetches (50 concurrent requests).
Processes in configurable batches, writes progress after each batch, and can
resume from where it left off using the enrichedSummary flag.

Usage:
    python3 scripts/enrich_people_fast.py                    # Run all
    python3 scripts/enrich_people_fast.py --batch-size 10000
    python3 scripts/enrich_people_fast.py --start 50000      # Resume from index
    python3 scripts/enrich_people_fast.py --concurrency 30   # Fewer parallel requests
    python3 scripts/enrich_people_fast.py --dry-run

Output: Updates data/wikidata_people.json in place after each batch.
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
INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'wikidata_people.json')
BATCH_SIZE = 10_000
CONCURRENCY = 20       # Max concurrent HTTP requests
REQUEST_TIMEOUT = 15   # Seconds per request
USER_AGENT = 'AnnalsOfTheWorld/1.0 (https://github.com/14-yama/annals-of-the-world; research project)'

# ─── Division role descriptions for fallback enrichment ───
DIVISION_ROLES = {
    '200': 'historical figure', '201': 'monarch or head of state',
    '202': 'military leader or commander', '203': 'athlete or sports figure',
    '204': 'religious figure or clergy', '205': 'political leader or statesperson',
    '210': 'philosopher or thinker', '211': 'scientist or inventor',
    '212': 'ethicist or moral philosopher',
    '220': 'explorer or navigator', '221': 'economist or social scientist',
    '222': 'legal scholar or jurist', '223': 'linguist or translator',
    '230': 'educator or academic', '231': 'medical practitioner or physician',
    '240': 'artist, musician, or performer', '241': 'entertainer or media figure',
    '242': 'architect or urban planner', '243': 'designer or craftsperson',
    '250': 'entrepreneur or business leader', '251': 'agriculturalist or land steward',
    '252': 'technologist or engineer', '253': 'industrialist or manufacturer',
    '260': 'artist or writer', '261': 'author or novelist',
    '262': 'journalist or media commentator', '263': 'visual artist or sculptor',
    '264': 'musician or composer', '265': 'filmmaker or theatre director',
    '270': 'social reformer or activist', '271': 'humanitarian or philanthropist',
    '272': 'environmentalist or conservationist', '273': 'civil rights leader or advocate',
    '280': 'public servant or civil administrator', '281': 'diplomat or ambassador',
    '282': 'intelligence officer or spy', '283': 'tribal leader or indigenous chief',
    '290': 'criminal or outlaw', '291': 'pirate or privateer',
    '292': 'revolutionary or insurgent', '293': 'controversial or contested figure',
}

ERA_CONTEXT = {
    'Prehistoric': 'the prehistoric era, before the emergence of writing and recorded civilizations',
    'Classical': 'the Classical era, an age of empires, philosophical inquiry, and foundational civilizations',
    'Medieval': 'the Medieval period, shaped by feudalism, religious institutions, and cultural exchange',
    'Early Modern': 'the Early Modern period, marked by exploration, reformation, and the rise of nation-states',
    'Modern': 'the Modern era, defined by industrialization, revolution, and global conflict',
    'Contemporary': 'the Contemporary era, characterized by technology, globalization, and rapid social change',
}


def extract_title_from_url(url: str) -> Optional[str]:
    """Extract the Wikipedia article title from a URL."""
    if not url:
        return None
    match = re.search(r'/wiki/(.+?)(?:\?|#|$)', url)
    if match:
        return urllib.parse.unquote(match.group(1))
    return None


def is_template_summary(summary: str) -> bool:
    """Check if a summary is a generic template rather than unique content."""
    s = summary.lower()
    return any([
        'distinguished' in s and 'who was active during' in s,
        'noted figure among' in s and 'active during' in s,
        'was a noted figure' in s and 'their legacy endures' in s,
        'their work contributed to' in s and 'their legacy endures' in s,
    ])


def strip_template_tail(summary: str) -> str:
    """Remove appended template text from an otherwise real summary."""
    for marker in ['Active during the', ' Their legacy endures in the domain of', ' Their work contributed to']:
        idx = summary.find(marker)
        if idx > 50:
            cleaned = summary[:idx].rstrip()
            if cleaned and cleaned[-1] not in '.!?':
                cleaned += '.'
            return cleaned
    return summary


def has_template_tail(summary: str) -> bool:
    """Check if a real summary has an appended template tail."""
    for marker in ['Active during the', 'Their legacy endures in the domain of']:
        idx = summary.find(marker)
        if idx > 50:
            return True
    return False


def clean_wikipedia_extract(extract: str) -> str:
    """Post-process Wikipedia extract to ensure quality."""
    extract = re.sub(r'\[\d+\]', '', extract)
    extract = re.sub(r'\s*\([^)]*pronunciation[^)]*\)', '', extract)
    extract = re.sub(r'\s*\([^)]*listen[^)]*\)', '', extract)
    extract = strip_template_tail(extract)
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
    born = entity.get('born', '')
    div_code = entity.get('divisionCode', '')
    role = DIVISION_ROLES.get(div_code, 'historical figure')
    era = entity.get('era', 'Unknown')
    era_ctx = ERA_CONTEXT.get(era, f'the {era} era')
    region = entity.get('region', '')
    places = entity.get('places', [])

    birth_part = f' (b. {born})' if born else ''
    location_parts = []
    if places:
        location_parts = [p['name'] if isinstance(p, dict) else str(p) for p in places[:2]]
    elif region:
        location_parts = [region]
    location = f', active in {" and ".join(location_parts)}' if location_parts else ''
    subjects = entity.get('subjects', [])
    domain = f' Known in the fields of {", ".join(subjects[:3]).lower()}.' if subjects else ''

    return f'{name}{birth_part} was a {role} of {era_ctx}{location}.{domain}'.strip()


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
        # Add small delay between requests to avoid burst
        await asyncio.sleep(0.05)
    return None


async def process_batch_async(entities: list, start: int, end: int, concurrency: int = 20) -> dict:
    """Process a batch of entities with concurrent Wikipedia fetches."""
    end = min(end, len(entities))
    batch = entities[start:end]

    stats = {'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
             'already_enriched': 0, 'skipped_real': 0, 'batch_size': end - start}

    # Separate entities into categories
    to_fetch = []  # (index_in_batch, entity, wiki_title)
    for i, entity in enumerate(batch):
        if entity.get('enrichedSummary') is True:
            stats['already_enriched'] += 1
            continue
        # enrichedSummary=False means fallback was used — retry wiki fetch
        is_retry = entity.get('enrichedSummary') is False
        if not is_retry and not is_template_summary(entity.get('summary', '')):
            if has_template_tail(entity.get('summary', '')):
                entity['summary'] = strip_template_tail(entity['summary'])
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

    # Fetch Wikipedia summaries in sub-batches to avoid overwhelming the API
    SUB_BATCH = concurrency * 5  # Process 100 at a time with 20 concurrency
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
            if total_to_fetch > 100:
                global_idx = start + done
                print(f'    [{global_idx:>7,}/{len(entities):,}] '
                      f'sub-batch {done}/{total_to_fetch} '
                      f'wiki:{stats["wiki_fetched"]} fail:{stats["wiki_failed"]}',
                      flush=True)

    return stats


def load_data() -> dict:
    """Load the people JSON file."""
    print(f'Loading {INPUT_FILE}...', flush=True)
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
    print(f'  Loaded {len(data["entities"]):,} entities', flush=True)
    return data


def save_data(data: dict) -> None:
    """Save the people JSON file."""
    print(f'  Saving...', flush=True)
    with open(INPUT_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    size_mb = os.path.getsize(INPUT_FILE) / 1024 / 1024
    print(f'  Saved ({size_mb:.1f} MB)', flush=True)


async def main_async():
    parser = argparse.ArgumentParser(description='Fast concurrent Wikipedia enrichment')
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
    template_count = sum(1 for e in data['entities'] if is_template_summary(e.get('summary', '')))
    print(f'  Already enriched: {enriched_count:,}', flush=True)
    print(f'  Template summaries needing enrichment: {template_count:,}', flush=True)
    print(f'  Range: [{args.start:,} → {end:,}]', flush=True)
    print(f'  Batch size: {args.batch_size:,} | Concurrency: {CONCURRENCY}', flush=True)
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
