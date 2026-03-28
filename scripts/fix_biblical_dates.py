"""Fix biblical.ts: remove misplaced period fields and add them correctly."""
import re

with open('ui/src/data/catalog/biblical.ts', 'r') as f:
    content = f.read()

# First, remove all period lines that were inserted by the previous script
# (they are the ones matching our specific date strings)
ADDED_PERIODS = [
    "Traditional dating, c. 4004 BCE",
    "c. 1750–1650 BCE",
    "c. 1393–1273 BCE",
    "c. 1355–1245 BCE",
    "c. 1118–1078 BCE",
    "c. 1070–1012 BCE",
    "c. 900–849 BCE",
    "c. 860–795 BCE",
    "c. 622–570 BCE",
    "c. 620–530 BCE",
    "c. 750–715 BCE",
    "c. 480–440 BCE",
    "c. 475–420 BCE",
    "c. 492–460 BCE",
    "Unknown, traditionally pre-Mosaic era",
    "c. 18 BCE – c. 41 CE",
    "c. 10–84 CE",
    "c. 1200–1000 BCE",
    "c. 1050–900 BCE",
    "c. 970–700 BCE",
    "c. 450–200 BCE",
    "c. 960–300 BCE",
    "c. 586 BCE",
    "c. 593–571 BCE",
    "c. 530–165 BCE",
    "c. 200 BCE – 425 CE",
    "Traditional dating, c. 2348 BCE",
    "c. 3000 BCE – present",
    "c. 3100 BCE – present",
    "c. 2000 BCE",
    "c. 250 BCE – 68 CE",
]

lines = content.split('\n')
cleaned_lines = []
removed = 0
for line in lines:
    stripped = line.strip()
    is_added = False
    for p in ADDED_PERIODS:
        if stripped == f"period: '{p}',":
            is_added = True
            break
    if is_added:
        removed += 1
    else:
        cleaned_lines.append(line)

content = '\n'.join(cleaned_lines)
print(f"Removed {removed} misplaced period lines")

# Now add periods correctly: find each slug, then find the era: line for that entity
# and insert period right before era:
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
    'hosea_prophet': 'c. 750–715 BCE',
    'ezra_scribe': 'c. 480–440 BCE',
    'nehemiah': 'c. 475–420 BCE',
    'esther_queen': 'c. 492–460 BCE',
    'job_biblical': 'Unknown, traditionally pre-Mosaic era',
    'mary_mother_of_jesus': 'c. 18 BCE – c. 41 CE',
    'luke_evangelist': 'c. 10–84 CE',
    'leviticus': 'Composition: c. 1400–400 BCE',
    'numbers_book': 'Composition: c. 1400–400 BCE',
    'deuteronomy': 'Composition: c. 1400–621 BCE',
    'joshua_book': 'Composition: c. 1400–1000 BCE',
    'judges_book': 'Composition: c. 1200–1000 BCE',
    'first_samuel': 'Composition: c. 1050–900 BCE',
    'second_samuel': 'Composition: c. 1010–900 BCE',
    'first_kings': 'Composition: c. 970–560 BCE',
    'psalms': 'Composition: c. 1000–400 BCE',
    'proverbs': 'Composition: c. 970–700 BCE',
    'ecclesiastes': 'Composition: c. 450–200 BCE',
    'song_of_solomon': 'Composition: c. 960–300 BCE',
    'job_book': 'Composition: c. 600–400 BCE',
    'lamentations': 'Composition: c. 586 BCE',
    'ezekiel_book': 'Composition: c. 593–571 BCE',
    'daniel_book': 'Composition: c. 530–165 BCE',
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

lines = content.split('\n')
added = 0

for slug, period in DATES.items():
    # Find the line index with this slug
    slug_line = f"slug: '{slug}',"
    slug_idx = None
    for i, line in enumerate(lines):
        if slug_line in line.strip():
            slug_idx = i
            break
    
    if slug_idx is None:
        print(f"  NOT FOUND: {slug}")
        continue
    
    # Check if this entity already has a period field before its era: line
    # Find the era: line for this entity (should be within ~10 lines of slug)
    era_idx = None
    has_period = False
    for j in range(slug_idx + 1, min(slug_idx + 15, len(lines))):
        if 'period:' in lines[j].strip():
            has_period = True
            break
        if lines[j].strip().startswith("era:"):
            era_idx = j
            break
    
    if has_period:
        # Already has period, skip
        continue
    
    if era_idx is None:
        print(f"  NO ERA LINE: {slug}")
        continue
    
    # Insert period line before the era line
    period_line = f"    period: '{period}',"
    lines.insert(era_idx, period_line)
    added += 1
    print(f"  ADDED: {slug} -> {period}")

content = '\n'.join(lines)

with open('ui/src/data/catalog/biblical.ts', 'w') as f:
    f.write(content)

print(f"\nRemoved {removed} misplaced, added {added} correct period fields")
