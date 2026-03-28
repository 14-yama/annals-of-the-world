"""Add period fields to biblical entities that are missing dates."""
import re

# Map slug -> period value for biblical entities
DATES = {
    'adam_biblical': 'Traditional dating, c. 4004 BCE',
    'eve_biblical': 'Traditional dating, c. 4004 BCE',
    'noah_biblical': 'Traditional dating, c. 2900 BCE',
    'joseph_biblical': 'c. 1750–1650 BCE',
    'aaron': 'c. 1393–1273 BCE',
    'miriam_biblical': 'c. 1400–1274 BCE',
    'joshua_biblical': 'c. 1355–1245 BCE',
    'deborah_judge': 'c. 1200–1125 BCE',
    'samson': 'c. 1118–1078 BCE',
    'samuel_biblical': 'c. 1070–1012 BCE',
    'elijah_prophet': 'c. 900–849 BCE',
    'elisha_prophet': 'c. 860–795 BCE',
    'ezekiel_prophet': 'c. 622–570 BCE',
    'daniel_prophet': 'c. 620–530 BCE',
    'amos_prophet': 'c. 760–750 BCE',
    'hosea_prophet': 'c. 750–715 BCE',
    'jonah_prophet': 'c. 780–740 BCE',
    'malachi_prophet': 'c. 460–430 BCE',
    'ezra_scribe': 'c. 480–440 BCE',
    'nehemiah': 'c. 475–420 BCE',
    'esther_queen': 'c. 492–460 BCE',
    'ruth_biblical': 'c. 1100 BCE',
    'job_biblical': 'Unknown, traditionally pre-Mosaic era',
    'mary_mother_of_jesus': 'c. 18 BCE – c. 41 CE',
    'luke_evangelist': 'c. 10–84 CE',
    'leviticus': 'c. 1400–400 BCE',
    'numbers_book': 'c. 1400–400 BCE',
    'deuteronomy': 'c. 1400–621 BCE',
    'joshua_book': 'c. 1400–1000 BCE',
    'judges_book': 'c. 1200–1000 BCE',
    'first_samuel': 'c. 1050–900 BCE',
    'second_samuel': 'c. 1010–900 BCE',
    'first_kings': 'c. 970–560 BCE',
    'psalms': 'c. 1000–400 BCE',
    'proverbs': 'c. 970–700 BCE',
    'ecclesiastes': 'c. 450–200 BCE',
    'song_of_solomon': 'c. 960–300 BCE',
    'job_book': 'c. 600–400 BCE',
    'lamentations': 'c. 586 BCE',
    'ezekiel_book': 'c. 593–571 BCE',
    'daniel_book': 'c. 530–165 BCE',
    'sanhedrin': 'c. 200 BCE – 425 CE',
    'great_flood': 'Traditional dating, c. 2348 BCE',
    'jerusalem': 'c. 3000 BCE – present',
    'babylon': 'c. 2300 BCE – 275 BCE',
    'egypt': 'c. 3100 BCE – present',
    'mount_sinai': 'c. 1313 BCE (Exodus narrative)',
    'abrahamic_covenant': 'c. 2000 BCE',
    'sinai_covenant': 'c. 1313 BCE',
    'davidic_covenant': 'c. 1000 BCE',
    'new_covenant': 'c. 30 CE',
    'ten_commandments': 'c. 1313 BCE',
    'dead_sea_scrolls': 'c. 250 BCE – 68 CE',
    'codex_sinaiticus': 'c. 330–360 CE',
}

with open('ui/src/data/catalog/biblical.ts', 'r') as f:
    content = f.read()

count = 0
for slug, period in DATES.items():
    # Find the line with this slug and add period after the summary line
    # Pattern: slug: '<slug>',
    slug_pattern = f"slug: '{slug}',"
    if slug_pattern not in content:
        print(f"  SKIP (not found): {slug}")
        continue

    # Find the entity block. After the 'summary:' line, add 'period:' line
    # We need to find the summary line for this entity
    idx = content.index(slug_pattern)
    # Find the next 'summary:' line after this slug
    summary_match = re.search(r"(    summary: '[^']*'(?:\n        \+ '[^']*')*,)\n", content[idx:])
    if not summary_match:
        # Try double-quote summaries
        summary_match = re.search(r'(    summary: "[^"]*",)\n', content[idx:])
    if not summary_match:
        # Try template literal
        summary_match = re.search(r"(    summary: `[^`]*`,)\n", content[idx:])
    if not summary_match:
        print(f"  SKIP (no summary): {slug}")
        continue

    insert_pos = idx + summary_match.end()
    # Check if period already exists in the next few chars
    next_chunk = content[insert_pos:insert_pos+100]
    if 'period:' in next_chunk.split('\n')[0] or 'period:' in next_chunk.split('\n')[1] if len(next_chunk.split('\n')) > 1 else False:
        print(f"  SKIP (already has period): {slug}")
        continue

    period_line = f"    period: '{period}',\n"
    content = content[:insert_pos] + period_line + content[insert_pos:]
    count += 1
    print(f"  ADDED: {slug} -> {period}")

with open('ui/src/data/catalog/biblical.ts', 'w') as f:
    f.write(content)

print(f"\nTotal added: {count}")
