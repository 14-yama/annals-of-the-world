#!/usr/bin/env python3
"""Generate a README.md in this folder listing countries grouped by continent
and reporting presence of common JSON files (index.json, artifacts.json, etc.).

Run:
    python3 generate_countries_readme.py
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import unicodedata
from datetime import datetime, timezone
from typing import Optional, Union


def get_HIER_from_file(repo_root: Path):
    """Extract the HIER mapping from geo_registry.py without importing dependencies."""
    p = repo_root / 'geo_registry.py'
    txt = p.read_text(encoding='utf-8')
    start = txt.find('HIER')
    if start == -1:
        return {}
    start = txt.find('=', start)
    if start == -1:
        return {}
    # find opening brace
    brace = txt.find('{', start)
    if brace == -1:
        return {}
    i = brace
    depth = 0
    end = None
    while i < len(txt):
        if txt[i] == '{':
            depth += 1
        elif txt[i] == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
        i += 1
    if end is None:
        return {}
    dict_text = txt[brace:end]
    # evaluate dict_text in restricted namespace
    data = {}
    try:
        data = eval(dict_text, {}, {})
    except Exception:
        data = {}
    return data


def find_repo_root(start: Path) -> Path:
    p = start
    for _ in range(8):
        if (p / 'geo_registry.py').exists():
            return p
        if p.parent == p:
            break
        p = p.parent
    raise FileNotFoundError('Could not find repo root containing geo_registry.py')


def slugify_loose(text: str) -> str:
    """Slugify with best-effort ASCII folding.

    Country folder slugs in this repo appear to be ASCII-only and hyphen-separated.
    The HIER registry includes names with accents and punctuation (e.g., Côte d’Ivoire),
    so we normalize aggressively to map those names to folder slugs.
    """
    t = (text or "").strip().lower()
    t = t.replace("&", " and ")
    t = t.replace("’", "'")
    t = t.replace("'", "")
    t = unicodedata.normalize("NFKD", t)
    t = t.encode("ascii", "ignore").decode("ascii")
    t = re.sub(r"[^a-z0-9]+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t


def title_from_slug(slug: str) -> str:
    words = re.split(r"[-_]+", slug.strip())
    return " ".join(w.capitalize() for w in words if w)


def safe_load_json(path: Path) -> Optional[Union[dict, list]]:
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def count_nodes(obj) -> int:
    """Best-effort count of curated nodes in a country JSON file.

    Supports both shapes currently in this repo:
    - {"nodes": [...]} (empty placeholders or flat lists)
    - {"thematic_clusters": {"910": [...], ...}} (clustered by timeframe)
    """
    if obj is None:
        return 0
    if isinstance(obj, list):
        return len(obj)
    if not isinstance(obj, dict):
        return 0

    nodes = obj.get('nodes')
    if isinstance(nodes, list):
        return len(nodes)

    clusters = obj.get('thematic_clusters')
    if isinstance(clusters, dict):
        total = 0
        for v in clusters.values():
            if isinstance(v, list):
                total += len(v)
        return total

    return 0


def main():
    here = Path(__file__).resolve().parent
    repo_root = find_repo_root(here)
    countries_dir = here

    HIER = get_HIER_from_file(repo_root)

    # expected JSON filenames commonly present per country
    expected = [
        'artifacts.json', 'events.json', 'evidence.json', 'frameworks.json',
        'index.json', 'institutions.json', 'movements.json', 'people.json',
        'texts.json', 'timeframes.json', 'places.json'
    ]
    core_expected = [fn for fn in expected if fn != 'index.json']

    # Build slug -> (continent, region, canonical_name) from HIER.
    slug_to_meta: dict[str, dict[str, str]] = {}
    for continent, regions in HIER.items():
        for region, countries in (regions or {}).items():
            for cname in countries:
                slug_norm = slugify_loose(cname)
                if slug_norm:
                    slug_to_meta[slug_norm] = {
                        'continent': continent,
                        'region': region,
                        'name': cname,
                    }

    # Gather country folders (ignore templates/hidden)
    all_dirs = [p for p in countries_dir.iterdir() if p.is_dir()]
    country_dirs = [p for p in all_dirs if not p.name.startswith('_') and not p.name.startswith('.')]
    template_dirs = [p for p in all_dirs if p.name.startswith('_') or p.name.startswith('.')]

    rows: list[dict] = []
    for d in sorted(country_dirs, key=lambda p: p.name):
        slug = d.name
        slug_norm = slugify_loose(slug)

        idxf = d / 'index.json'
        continent_from_index = None
        if idxf.exists():
            try:
                with idxf.open('r', encoding='utf-8') as f:
                    j = json.load(f)
                continent_from_index = j.get('_meta', {}).get('continent') or j.get('continent')
            except Exception:
                continent_from_index = None

        meta = slug_to_meta.get(slug) or slug_to_meta.get(slug_norm) or {}
        continent = meta.get('continent') or continent_from_index or 'Unknown'
        region = meta.get('region') or 'Unknown'
        display_name = meta.get('name') or title_from_slug(slug)

        files_present = [fn for fn in expected if (d / fn).exists()]
        core_present = [fn for fn in core_expected if fn in files_present]
        core_missing = [fn for fn in core_expected if fn not in files_present]

        # Track whether each core JSON is actually populated with meaningful node data.
        kind_counts: dict[str, int] = {}
        for fn in core_expected:
            fp = d / fn
            obj = safe_load_json(fp) if fp.exists() else None
            kind = fn[:-5] if fn.endswith('.json') else fn
            kind_counts[kind] = count_nodes(obj)
        core_nodes_total = sum(kind_counts.values())
        populated_kinds = sorted([k for k, v in kind_counts.items() if v > 0])

        rows.append({
            'slug': slug,
            'slug_norm': slug_norm,
            'name': display_name,
            'continent': continent,
            'region': region,
            'index': idxf.exists(),
            'files_present': files_present,
            'core_present': core_present,
            'core_missing': core_missing,
            'kind_counts': kind_counts,
            'core_nodes_total': core_nodes_total,
            'populated_kinds': populated_kinds,
        })

    # Summary counts
    total_countries = len(rows)
    with_index = sum(1 for r in rows if r['index'])
    full_core = sum(1 for r in rows if not r.get('core_missing'))
    missing_any_core = total_countries - full_core

    curated_any = sum(1 for r in rows if (r.get('core_nodes_total') or 0) > 0)
    curated_none = total_countries - curated_any

    index_slugs = sorted(r['slug'] for r in rows if r.get('index'))

    unmapped = sorted({r['slug'] for r in rows if r.get('continent') == 'Unknown' or r.get('region') == 'Unknown'})

    continent_order = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania', 'Antarctica', 'Unknown']

    continent_counts: dict[str, dict[str, int]] = {}
    region_counts: dict[str, dict[str, dict[str, int]]] = {}
    for r in rows:
        cont = r['continent']
        reg = r['region']
        continent_counts.setdefault(cont, {'countries': 0, 'with_index': 0, 'regions': 0})
        continent_counts[cont]['countries'] += 1
        continent_counts[cont]['with_index'] += 1 if r['index'] else 0

        region_counts.setdefault(cont, {})
        region_counts[cont].setdefault(reg, {'countries': 0, 'with_index': 0})
        region_counts[cont][reg]['countries'] += 1
        region_counts[cont][reg]['with_index'] += 1 if r['index'] else 0

    for cont, regs in region_counts.items():
        continent_counts.setdefault(cont, {'countries': 0, 'with_index': 0, 'regions': 0})
        continent_counts[cont]['regions'] = len(regs)

    # Write markdown
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    md_lines: list[str] = []
    md_lines.append('# Countries — registry summary')
    md_lines.append('')
    md_lines.append(f'_Generated by `generate_countries_readme.py` on {ts}._')
    md_lines.append('')
    md_lines.append('This report is based on country folders under `geo-registry/places/countries/` and the continent/region hierarchy in `geo_registry.py` (`HIER`).')
    md_lines.append('')

    def idx_mark(r: dict) -> str:
        return '✅' if r.get('index') else '—'

    md_lines.append('## Quick counts')
    md_lines.append('')
    md_lines.append(f'- Total country folders: **{total_countries}**')
    md_lines.append('- Counts reflect folders in this repo (may include territories/regions present in `HIER`, e.g., Hong Kong, Macau).')
    md_lines.append(f'- Countries with `index.json`: **{with_index}**')
    if index_slugs:
        md_lines.append(f"  - Currently: {', '.join(index_slugs)}")
    md_lines.append(f"- Core per-country JSON files expected ({len(core_expected)}): {', '.join(core_expected)}")
    md_lines.append(f"- Core completeness: **{full_core}** complete, **{missing_any_core}** missing ≥1 core file")
    md_lines.append("- `index.json` is tracked separately (see tables below).")
    if template_dirs:
        md_lines.append(f"- Non-country folders ignored (templates/hidden): {', '.join(sorted(p.name for p in template_dirs))}")
    if unmapped:
        preview = ', '.join(unmapped[:20])
        suffix = '' if len(unmapped) <= 20 else f" (+{len(unmapped) - 20} more)"
        md_lines.append(f"- Not mapped to a HIER continent/region: {preview}{suffix}")
    md_lines.append('')

    md_lines.append('## Curation coverage (meaningful node data)')
    md_lines.append('')
    md_lines.append('A country is considered **curated** if any core JSON file has one or more nodes (supports both `nodes: []` and `thematic_clusters`).')
    md_lines.append('')
    md_lines.append(f'- Curated countries (any nodes): **{curated_any}**')
    md_lines.append(f'- Not yet curated (all core files empty): **{curated_none}**')
    md_lines.append('')

    curated_rows = [r for r in rows if (r.get('core_nodes_total') or 0) > 0]
    curated_rows_sorted = sorted(
        curated_rows,
        key=lambda r: (-(r.get('core_nodes_total') or 0), r.get('continent') or '', r.get('region') or '', r.get('slug') or ''),
    )

    md_lines.append('### Curated countries (detail)')
    md_lines.append('')
    md_lines.append('| Country | Slug | Continent | Region | Core nodes | Populated kinds | index.json |')
    md_lines.append('|---|---|---|---|---:|---|:--:|')

    def populated_kinds_disp(r: dict) -> str:
        kinds = r.get('populated_kinds') or []
        if not kinds:
            return '—'
        counts = r.get('kind_counts') or {}
        return ', '.join(f"{k}({counts.get(k, 0)})" for k in kinds)

    for r in curated_rows_sorted:
        md_lines.append(
            f"| {r['name']} | {r['slug']} | {r['continent']} | {r['region']} | {r.get('core_nodes_total', 0)} | {populated_kinds_disp(r)} | {idx_mark(r)} |"
        )
    md_lines.append('')

    continent_cur: dict[str, dict[str, int]] = {}
    region_cur: dict[str, dict[str, dict[str, int]]] = {}
    for r in rows:
        cont = r['continent']
        reg = r['region']
        is_curated = 1 if (r.get('core_nodes_total') or 0) > 0 else 0
        continent_cur.setdefault(cont, {'curated': 0, 'not_yet': 0})
        continent_cur[cont]['curated'] += is_curated
        continent_cur[cont]['not_yet'] += (1 - is_curated)
        region_cur.setdefault(cont, {})
        region_cur[cont].setdefault(reg, {'curated': 0, 'not_yet': 0})
        region_cur[cont][reg]['curated'] += is_curated
        region_cur[cont][reg]['not_yet'] += (1 - is_curated)

    md_lines.append('### Curated by continent')
    md_lines.append('')
    md_lines.append('| Continent | Curated | Not yet |')
    md_lines.append('|---|---:|---:|')
    for cont in continent_order:
        if cont not in continent_cur:
            continue
        c = continent_cur[cont]
        md_lines.append(f"| {cont} | {c['curated']} | {c['not_yet']} |")
    md_lines.append('')

    md_lines.append('### Curated by region')
    md_lines.append('')
    for cont in continent_order:
        regs = region_cur.get(cont)
        if not regs:
            continue
        md_lines.append(f'#### {cont}')
        md_lines.append('')
        md_lines.append('| Region | Curated | Not yet |')
        md_lines.append('|---|---:|---:|')
        for reg in sorted(regs.keys()):
            rc = regs[reg]
            md_lines.append(f"| {reg} | {rc['curated']} | {rc['not_yet']} |")
        md_lines.append('')

    md_lines.append('## Countries by continent')
    md_lines.append('')
    md_lines.append('| Continent | Regions | Countries | With index.json |')
    md_lines.append('|---|---:|---:|---:|')
    for cont in continent_order:
        if cont not in continent_counts:
            continue
        c = continent_counts[cont]
        md_lines.append(f"| {cont} | {c.get('regions', 0)} | {c.get('countries', 0)} | {c.get('with_index', 0)} |")
    md_lines.append('')

    md_lines.append('## Countries by region')
    md_lines.append('')
    for cont in continent_order:
        regs = region_counts.get(cont)
        if not regs:
            continue
        md_lines.append(f'### {cont}')
        md_lines.append('')
        md_lines.append('| Region | Countries | With index.json |')
        md_lines.append('|---|---:|---:|')
        for reg in sorted(regs.keys()):
            rc = regs[reg]
            md_lines.append(f"| {reg} | {rc['countries']} | {rc['with_index']} |")
        md_lines.append('')

    md_lines.append('## Country files (at-a-glance)')
    md_lines.append('')
    md_lines.append('| Country | Slug | Continent | Region | Curated | Core nodes | Populated kinds | index.json |')
    md_lines.append('|---|---|---|---|:--:|---:|---|:--:|')

    def curated_mark(r: dict) -> str:
        return '✅' if (r.get('core_nodes_total') or 0) > 0 else '—'

    for r in sorted(rows, key=lambda x: (x.get('continent') or '', x.get('region') or '', x.get('slug') or '')):
        md_lines.append(
            f"| {r['name']} | {r['slug']} | {r['continent']} | {r['region']} | {curated_mark(r)} | {r.get('core_nodes_total', 0)} | {populated_kinds_disp(r)} | {idx_mark(r)} |"
        )

    md_lines.append('')
    md_lines.append('**Legend:** “Curated” ✅ means at least one core JSON has ≥1 node. “Core nodes” is the sum across the 10 core JSON files (excludes `index.json`).')

    readme_path = countries_dir / 'README.md'
    readme_text = '\n'.join(md_lines)
    readme_path.write_text(readme_text, encoding='utf-8')
    print(f'Wrote {readme_path}')


if __name__ == '__main__':
    main()
