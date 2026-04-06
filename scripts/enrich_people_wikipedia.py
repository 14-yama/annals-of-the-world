#!/usr/bin/env python3
"""
Enrich wikidata_people.json with unique summaries from Wikipedia.

Uses the Wikipedia REST API (/api/rest_v1/page/summary/) to fetch the intro
paragraph for each entity that has a Wikipedia URL. Processes in configurable
batches, writes progress after each batch, and can resume from where it left off.

Usage:
    python3 scripts/enrich_people_wikipedia.py                # Run all batches
    python3 scripts/enrich_people_wikipedia.py --batch-size 5000
    python3 scripts/enrich_people_wikipedia.py --dry-run      # Preview without writing
    python3 scripts/enrich_people_wikipedia.py --start 50000  # Resume from index 50000

Output: Updates data/wikidata_people.json in place after each batch.
Adds 'enrichedSummary' boolean field to every entity.
"""

import json
import time
import sys
import os
import re
import argparse
import urllib.request
import urllib.error
import urllib.parse
from typing import Optional

# ─── Configuration ───
INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'wikidata_people.json')
BATCH_SIZE = 5000
REQUEST_DELAY = 0.05  # 50ms between requests (≈20 req/s, well within Wikipedia limits)
MAX_RETRIES = 3
USER_AGENT = 'AnnalsOfTheWorld/1.0 (https://github.com/14-yama/annals-of-the-world; research project)'

# ─── Division role descriptions for fallback enrichment ───
DIVISION_ROLES = {
    '200': 'historical figure',
    '201': 'monarch or head of state',
    '202': 'military leader or commander',
    '203': 'athlete or sports figure',
    '204': 'religious figure or clergy',
    '205': 'political leader or statesperson',
    '210': 'philosopher or thinker',
    '211': 'scientist or inventor',
    '212': 'ethicist or moral philosopher',
    '220': 'explorer or navigator',
    '221': 'economist or social scientist',
    '222': 'legal scholar or jurist',
    '223': 'linguist or translator',
    '230': 'educator or academic',
    '231': 'medical practitioner or physician',
    '240': 'artist, musician, or performer',
    '241': 'entertainer or media figure',
    '242': 'architect or urban planner',
    '243': 'designer or craftsperson',
    '250': 'entrepreneur or business leader',
    '251': 'agriculturalist or land steward',
    '252': 'technologist or engineer',
    '253': 'industrialist or manufacturer',
    '260': 'artist or writer',
    '261': 'author or novelist',
    '262': 'journalist or media commentator',
    '263': 'visual artist or sculptor',
    '264': 'musician or composer',
    '265': 'filmmaker or theatre director',
    '270': 'social reformer or activist',
    '271': 'humanitarian or philanthropist',
    '272': 'environmentalist or conservationist',
    '273': 'civil rights leader or advocate',
    '280': 'public servant or civil administrator',
    '281': 'diplomat or ambassador',
    '282': 'intelligence officer or spy',
    '283': 'tribal leader or indigenous chief',
    '290': 'criminal or outlaw',
    '291': 'pirate or privateer',
    '292': 'revolutionary or insurgent',
    '293': 'controversial or contested figure',
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
    # Handle URLs like https://en.wikipedia.org/wiki/Albert_Einstein
    match = re.search(r'/wiki/(.+?)(?:\?|#|$)', url)
    if match:
        return urllib.parse.unquote(match.group(1))
    return None


def fetch_wikipedia_summary(title: str) -> Optional[str]:
    """Fetch the intro paragraph from Wikipedia REST API."""
    encoded = urllib.parse.quote(title, safe='')
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}'

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': USER_AGENT,
                'Accept': 'application/json',
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                extract = data.get('extract', '')
                if extract and len(extract) > 30:
                    return extract
                return None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # Page doesn't exist
            if e.code == 429:
                time.sleep(2 ** attempt)  # Rate limited — back off
                continue
            return None
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt < MAX_RETRIES - 1:
                time.sleep(1)
                continue
            return None
    return None


def is_template_summary(summary: str) -> bool:
    """Check if a summary is a generic template rather than unique content."""
    s = summary.lower()
    patterns = [
        'distinguished' in s and 'who was active during' in s,
        'noted figure among' in s and 'active during' in s,
        'was a noted figure' in s and 'their legacy endures' in s,
        'their work contributed to' in s and 'their legacy endures' in s,
    ]
    return any(patterns)


def has_template_tail(summary: str) -> bool:
    """Check if a real summary has an appended template tail that should be removed."""
    tail_markers = [
        'Active during the',
        'Their legacy endures in the domain of',
        'Their work contributed to',
    ]
    for marker in tail_markers:
        idx = summary.find(marker)
        if idx > 50:  # Only if marker appears after real content
            return True
    return False


def strip_template_tail(summary: str) -> str:
    """Remove appended template text from an otherwise real summary."""
    tail_markers = [
        'Active during the',
        ' Their legacy endures in the domain of',
        ' Their work contributed to',
    ]
    for marker in tail_markers:
        idx = summary.find(marker)
        if idx > 50:
            # Keep everything before the template tail
            cleaned = summary[:idx].rstrip()
            # Ensure it ends with proper punctuation
            if cleaned and cleaned[-1] not in '.!?':
                cleaned += '.'
            return cleaned
    return summary


def build_fallback_summary(entity: dict) -> str:
    """Build a rich summary without Wikipedia, using entity metadata."""
    name = entity['name']
    born = entity.get('born', '')
    div_code = entity.get('divisionCode', '')
    role = DIVISION_ROLES.get(div_code, 'historical figure')
    era = entity.get('era', 'Unknown')
    era_ctx = ERA_CONTEXT.get(era, f'the {era} era')
    region = entity.get('region', '')
    continent = entity.get('continent', '')
    subjects = entity.get('subjects', [])
    places = entity.get('places', [])

    # Build birth info
    birth_part = ''
    if born:
        birth_part = f' (b. {born})'

    # Build location context
    location_parts = []
    if places:
        place_names = [p['name'] if isinstance(p, dict) else str(p) for p in places[:2]]
        location_parts = place_names
    elif region:
        location_parts = [region]

    location = ''
    if location_parts:
        location = f', active in {" and ".join(location_parts)}'

    # Build subject context
    domain = ''
    if subjects:
        domain = f' Known in the fields of {", ".join(subjects[:3]).lower()}.'

    summary = (
        f'{name}{birth_part} was a {role} of {era_ctx}{location}.{domain}'
    )
    return summary.strip()


def clean_wikipedia_extract(extract: str, entity: dict) -> str:
    """Post-process Wikipedia extract to ensure quality."""
    # Remove references like [1], [2], etc.
    extract = re.sub(r'\[\d+\]', '', extract)
    # Remove parenthetical pronunciation guides
    extract = re.sub(r'\s*\([^)]*pronunciation[^)]*\)', '', extract)
    extract = re.sub(r'\s*\([^)]*listen[^)]*\)', '', extract)
    # Strip any template tail that might have been mixed in
    extract = strip_template_tail(extract)
    # Trim to reasonable length (aim for 1-3 sentences, max ~500 chars)
    if len(extract) > 600:
        # Find a sentence break near 500 chars
        for end in range(500, min(len(extract), 700)):
            if extract[end] in '.!?' and (end + 1 >= len(extract) or extract[end + 1] == ' '):
                extract = extract[:end + 1]
                break
        else:
            extract = extract[:600].rsplit('.', 1)[0] + '.'

    return extract.strip()


def load_data() -> dict:
    """Load the people JSON file."""
    print(f'Loading {INPUT_FILE}...', flush=True)
    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)
    print(f'  Loaded {len(data["entities"]):,} entities', flush=True)
    return data


def save_data(data: dict) -> None:
    """Save the people JSON file."""
    print(f'  Saving to {INPUT_FILE}...', flush=True)
    with open(INPUT_FILE, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    size_mb = os.path.getsize(INPUT_FILE) / 1024 / 1024
    print(f'  Saved ({size_mb:.1f} MB)', flush=True)


def process_batch(data: dict, start: int, end: int, dry_run: bool = False) -> dict:
    """Process a batch of entities from start to end index."""
    entities = data['entities']
    end = min(end, len(entities))
    batch = entities[start:end]

    wiki_fetched = 0
    wiki_failed = 0
    fallback_used = 0
    already_enriched = 0
    skipped_real = 0

    for i, entity in enumerate(batch):
        idx = start + i
        # Skip already enriched
        if entity.get('enrichedSummary'):
            already_enriched += 1
            continue

        # Skip entities that already have real (non-template) summaries
        if not is_template_summary(entity.get('summary', '')):
            # Strip any template tail that may have been appended
            if has_template_tail(entity.get('summary', '')):
                entity['summary'] = strip_template_tail(entity['summary'])
            entity['enrichedSummary'] = True
            skipped_real += 1
            continue

        # Try Wikipedia
        wiki_url = entity.get('wikipediaUrl', '')
        title = extract_title_from_url(wiki_url) if wiki_url else None

        new_summary = None
        if title:
            if not dry_run:
                new_summary = fetch_wikipedia_summary(title)
                time.sleep(REQUEST_DELAY)

            if new_summary:
                entity['summary'] = clean_wikipedia_extract(new_summary, entity)
                entity['enrichedSummary'] = True
                wiki_fetched += 1
            else:
                # Wikipedia fetch failed — use fallback
                entity['summary'] = build_fallback_summary(entity)
                entity['enrichedSummary'] = False
                wiki_failed += 1
        else:
            # No Wikipedia URL — use fallback
            entity['summary'] = build_fallback_summary(entity)
            entity['enrichedSummary'] = False
            fallback_used += 1

        # Progress every 500
        if (i + 1) % 500 == 0:
            total_done = wiki_fetched + wiki_failed + fallback_used + skipped_real
            print(f'    [{idx + 1:>7,}/{len(entities):,}] '
                  f'wiki:{wiki_fetched} fail:{wiki_failed} fallback:{fallback_used} '
                  f'real:{skipped_real} skip:{already_enriched}', flush=True)

    stats = {
        'wiki_fetched': wiki_fetched,
        'wiki_failed': wiki_failed,
        'fallback_used': fallback_used,
        'already_enriched': already_enriched,
        'skipped_real': skipped_real,
        'batch_size': end - start,
    }
    return stats


def main():
    parser = argparse.ArgumentParser(description='Enrich people JSON with Wikipedia summaries')
    parser.add_argument('--batch-size', type=int, default=BATCH_SIZE, help='Entities per batch')
    parser.add_argument('--start', type=int, default=0, help='Start index (for resuming)')
    parser.add_argument('--end', type=int, default=None, help='End index (optional)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without fetching or writing')
    args = parser.parse_args()

    data = load_data()
    total = len(data['entities'])
    end = args.end or total

    # Count current state
    enriched_count = sum(1 for e in data['entities'] if e.get('enrichedSummary'))
    template_count = sum(1 for e in data['entities'] if is_template_summary(e.get('summary', '')))
    print(f'  Already enriched: {enriched_count:,}', flush=True)
    print(f'  Template summaries needing enrichment: {template_count:,}', flush=True)
    print(f'  Processing range: [{args.start:,} → {end:,}]', flush=True)
    print(f'  Batch size: {args.batch_size:,}', flush=True)
    if args.dry_run:
        print('  *** DRY RUN — no fetching or writing ***', flush=True)
    print(flush=True)

    grand_stats = {
        'wiki_fetched': 0, 'wiki_failed': 0, 'fallback_used': 0,
        'already_enriched': 0, 'skipped_real': 0,
    }

    batch_num = 0
    cursor = args.start
    start_time = time.time()

    while cursor < end:
        batch_end = min(cursor + args.batch_size, end)
        batch_num += 1
        print(f'═══ Batch {batch_num}: entities [{cursor:,} → {batch_end:,}] ═══', flush=True)

        batch_start_time = time.time()
        stats = process_batch(data, cursor, batch_end, dry_run=args.dry_run)
        batch_elapsed = time.time() - batch_start_time

        # Accumulate stats
        for k in grand_stats:
            grand_stats[k] += stats.get(k, 0)

        print(f'  Batch done in {batch_elapsed:.1f}s — '
              f'wiki:{stats["wiki_fetched"]} fail:{stats["wiki_failed"]} '
              f'fallback:{stats["fallback_used"]} real:{stats["skipped_real"]} '
              f'skip:{stats["already_enriched"]}', flush=True)

        # Save after each batch (unless dry run)
        if not args.dry_run:
            # Update _meta
            data['_meta']['enrichment_progress'] = {
                'last_batch_end': batch_end,
                'total_wiki_fetched': grand_stats['wiki_fetched'],
                'total_enriched': sum(1 for e in data['entities'] if e.get('enrichedSummary')),
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            }
            save_data(data)

        cursor = batch_end
        elapsed = time.time() - start_time
        remaining = end - cursor
        if cursor > args.start:
            rate = (cursor - args.start) / elapsed
            eta = remaining / rate if rate > 0 else 0
            print(f'  Progress: {cursor:,}/{end:,} ({cursor/end*100:.1f}%) '
                  f'| Rate: {rate:.0f} entities/s '
                  f'| ETA: {eta/60:.0f} min', flush=True)
        print(flush=True)

    # Final summary
    elapsed = time.time() - start_time
    print(f'{"=" * 60}', flush=True)
    print(f'ENRICHMENT COMPLETE', flush=True)
    print(f'  Total processed: {end - args.start:,}', flush=True)
    print(f'  Wikipedia fetched: {grand_stats["wiki_fetched"]:,}', flush=True)
    print(f'  Wikipedia failed: {grand_stats["wiki_failed"]:,}', flush=True)
    print(f'  Fallback (no URL): {grand_stats["fallback_used"]:,}', flush=True)
    print(f'  Already real summaries: {grand_stats["skipped_real"]:,}', flush=True)
    print(f'  Already enriched (skipped): {grand_stats["already_enriched"]:,}', flush=True)
    print(f'  Elapsed: {elapsed/60:.1f} min ({elapsed/3600:.1f} hr)', flush=True)
    if grand_stats['wiki_fetched'] > 0:
        print(f'  Avg fetch time: {elapsed/grand_stats["wiki_fetched"]*1000:.0f} ms/entity', flush=True)


if __name__ == '__main__':
    main()
