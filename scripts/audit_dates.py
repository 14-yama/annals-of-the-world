"""Audit biblical.ts for entities missing date fields."""
import re

with open('ui/src/data/catalog/biblical.ts', 'r') as f:
    lines = f.readlines()

missing = []
current_slug = None
current_line = None
has_date = False

for i, line in enumerate(lines):
    stripped = line.strip()
    # Top-level entity slug
    if stripped.startswith('slug:'):
        if current_slug and not has_date:
            missing.append((current_slug, current_line))
        m = re.search(r"'([^']+)'", stripped)
        current_slug = m.group(1) if m else None
        current_line = i + 1
        has_date = False
    if current_slug:
        for field in ['period:', 'startDate:', 'born:', 'died:', 'founded:']:
            if field in stripped:
                has_date = True

if current_slug and not has_date:
    missing.append((current_slug, current_line))

for slug, line in missing:
    print(f'{line}: {slug}')
print(f'\nTotal missing: {len(missing)}')
