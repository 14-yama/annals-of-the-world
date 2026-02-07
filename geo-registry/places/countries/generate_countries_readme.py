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


def iter_node_dicts(obj):
    """Yield node-like dicts from a country JSON payload.

    Supports the same shapes as count_nodes():
    - {"nodes": [...]} where each entry is expected to be a dict
    - {"thematic_clusters": {"910": [...], ...}} where each entry is expected to be a dict
    """
    if obj is None:
        return
    if isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                yield item
        return
    if not isinstance(obj, dict):
        return

    nodes = obj.get('nodes')
    if isinstance(nodes, list):
        for item in nodes:
            if isinstance(item, dict):
                yield item
        return

    clusters = obj.get('thematic_clusters')
    if isinstance(clusters, dict):
        for v in clusters.values():
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        yield item


def fmt_int(n: int) -> str:
    return f"{n:,}"

def count_key_event_refs(obj) -> int:
    if not isinstance(obj, dict):
        return 0
    ke = obj.get('key_events')
    if isinstance(ke, list):
        return sum(1 for x in ke if isinstance(x, str) and x.strip())
    return 0

def summarize_index(index_obj: object) -> dict[str, int]:
    """Summarize potential node counts from a country index.json.

    Treats Level-4 clusters and Level-5 sub-clusters as potential :Cluster nodes
    (per docs/guidelines/global_cluster_management.md).
    """
    l4 = 0
    l5 = 0
    key_event_refs = 0
    unassigned_refs = 0
    cross_interfaces = 0
    l4_by_timeframe: dict[str, int] = {}

    if not isinstance(index_obj, dict):
        return {
            'l4': 0,
            'l5': 0,
            'cluster_nodes_total': 0,
            'key_event_refs': 0,
            'unassigned_refs': 0,
            'event_refs_total': 0,
            'cross_interfaces': 0,
            'l4_910': 0,
            'l4_920': 0,
            'l4_930': 0,
            'l4_940': 0,
            'l4_950': 0,
            'l4_960': 0,
        }

    clusters = index_obj.get('thematic_clusters')
    if isinstance(clusters, dict):
        for tf, cluster_list in clusters.items():
            if not isinstance(cluster_list, list):
                continue
            tf_key = str(tf)
            l4_by_timeframe[tf_key] = l4_by_timeframe.get(tf_key, 0) + len(cluster_list)
            for c in cluster_list:
                if not isinstance(c, dict):
                    continue
                l4 += 1
                key_event_refs += count_key_event_refs(c)

                subs = c.get('sub_clusters')
                if isinstance(subs, list):
                    for sc in subs:
                        if isinstance(sc, dict):
                            l5 += 1
                            key_event_refs += count_key_event_refs(sc)

    ue = index_obj.get('unassigned_events')
    if isinstance(ue, dict):
        slugs = ue.get('slugs')
        if isinstance(slugs, list):
            unassigned_refs += sum(1 for x in slugs if isinstance(x, str) and x.strip())
        cnt = ue.get('count')
        if isinstance(cnt, int) and cnt > unassigned_refs:
            # Prefer explicit slugs when present; fall back to count.
            unassigned_refs = cnt

    cci = index_obj.get('cross_cluster_interfaces')
    if isinstance(cci, list):
        cross_interfaces = sum(1 for x in cci if isinstance(x, dict))

    # Normalize timeframe keys we commonly use.
    for tf in ['910', '920', '930', '940', '950', '960']:
        l4_by_timeframe.setdefault(tf, 0)

    return {
        'l4': l4,
        'l5': l5,
        'cluster_nodes_total': l4 + l5,
        'key_event_refs': key_event_refs,
        'unassigned_refs': unassigned_refs,
        'event_refs_total': key_event_refs + unassigned_refs,
        'cross_interfaces': cross_interfaces,
        'l4_910': l4_by_timeframe['910'],
        'l4_920': l4_by_timeframe['920'],
        'l4_930': l4_by_timeframe['930'],
        'l4_940': l4_by_timeframe['940'],
        'l4_950': l4_by_timeframe['950'],
        'l4_960': l4_by_timeframe['960'],
    }

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

    # Aggregate counts across the entire countries registry.
    kinds = [fn[:-5] for fn in core_expected]
    total_nodes_by_kind: dict[str, int] = {k: 0 for k in kinds}
    countries_with_nodes_by_kind: dict[str, int] = {k: 0 for k in kinds}
    for r in rows:
        kind_counts = r.get('kind_counts') or {}
        for k in kinds:
            v = int(kind_counts.get(k) or 0)
            total_nodes_by_kind[k] += v
            if v > 0:
                countries_with_nodes_by_kind[k] += 1
    total_core_nodes = sum(total_nodes_by_kind.values())

    # Aggregate potential nodes from index.json files.
    index_summaries: list[dict[str, int]] = []
    for r in rows:
        if not r.get('index'):
            continue
        idx_path = countries_dir / r['slug'] / 'index.json'
        idx_obj = safe_load_json(idx_path)
        index_summaries.append(summarize_index(idx_obj))

    index_cluster_l4 = sum(s.get('l4', 0) for s in index_summaries)
    index_cluster_l5 = sum(s.get('l5', 0) for s in index_summaries)
    index_cluster_total = index_cluster_l4 + index_cluster_l5
    index_event_refs_total = sum(s.get('event_refs_total', 0) for s in index_summaries)
    index_key_event_refs = sum(s.get('key_event_refs', 0) for s in index_summaries)
    index_unassigned_refs = sum(s.get('unassigned_refs', 0) for s in index_summaries)
    index_cross_interfaces = sum(s.get('cross_interfaces', 0) for s in index_summaries)
    index_l4_by_tf = {
        '910': sum(s.get('l4_910', 0) for s in index_summaries),
        '920': sum(s.get('l4_920', 0) for s in index_summaries),
        '930': sum(s.get('l4_930', 0) for s in index_summaries),
        '940': sum(s.get('l4_940', 0) for s in index_summaries),
        '950': sum(s.get('l4_950', 0) for s in index_summaries),
        '960': sum(s.get('l4_960', 0) for s in index_summaries),
    }
    # Optional: breakdown of Event nodes by their schema `kind` property.
    event_kind_counts: dict[str, int] = {}
    event_kind_missing = 0
    for r in rows:
        d = countries_dir / r['slug']
        fp = d / 'events.json'
        if not fp.exists():
            continue
        obj = safe_load_json(fp)
        for node in iter_node_dicts(obj):
            ek = node.get('kind')
            if isinstance(ek, str) and ek.strip():
                event_kind_counts[ek.strip()] = event_kind_counts.get(ek.strip(), 0) + 1
            else:
                event_kind_missing += 1

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
    md_lines.append('## Index-derived potential nodes')
    md_lines.append('')
    md_lines.append('These counts are derived from country `index.json` files (thematic cluster catalogs). They represent what could be generated as graph nodes from the index structure alone.')
    md_lines.append('')
    md_lines.append(f'- Countries with `index.json`: **{with_index}**')
    md_lines.append(f'- Potential `:Cluster` nodes from indexes: **{fmt_int(index_cluster_total)}** (L4 clusters: {fmt_int(index_cluster_l4)}, L5 sub-clusters: {fmt_int(index_cluster_l5)})')
    md_lines.append(f'- Potential `:Event` references from indexes: **{fmt_int(index_event_refs_total)}** (key_events refs: {fmt_int(index_key_event_refs)}, unassigned refs/count: {fmt_int(index_unassigned_refs)})')
    md_lines.append(f'- Cross-cluster interface entries: **{fmt_int(index_cross_interfaces)}**')
    md_lines.append('')
    md_lines.append('| Timeframe | L4 clusters |')
    md_lines.append('|---|---:|')
    for tf in ['910', '920', '930', '940', '950', '960']:
        md_lines.append(f'| {tf} | {fmt_int(index_l4_by_tf.get(tf, 0))} |')
    md_lines.append('')
    md_lines.append('Note: People/Institutions/Texts/Artifacts are not enumerated in `index.json`; those nodes are counted from core country JSON files in the next sections.')
    md_lines.append('')

    md_lines.append('## Curation coverage (meaningful node data)')
    md_lines.append('')
    md_lines.append('A country is considered **curated** if any core JSON file has one or more nodes (supports both `nodes: []` and `thematic_clusters`).')
    md_lines.append('')
    md_lines.append(f'- Curated countries (any nodes): **{curated_any}**')
    md_lines.append(f'- Not yet curated (all core files empty): **{curated_none}**')

    md_lines.append('')
    md_lines.append('## Node inventory (core JSON only)')
    md_lines.append('')
    md_lines.append('Counts below are the total number of nodes currently present in country core JSON files under `geo-registry/places/countries/*/` (excludes `index.json`).')
    md_lines.append('')
    md_lines.append(f'- Total core nodes across all countries: **{fmt_int(total_core_nodes)}**')
    md_lines.append('')
    md_lines.append('| Kind | Total nodes | Countries with ≥1 | File |')
    md_lines.append('|---|---:|---:|---|')
    for k in kinds:
        md_lines.append(f'| {k} | {fmt_int(total_nodes_by_kind.get(k, 0))} | {countries_with_nodes_by_kind.get(k, 0)} | {k}.json |')

    if event_kind_counts or event_kind_missing:
        md_lines.append('')
        md_lines.append('### Events by kind')
        md_lines.append('')
        md_lines.append('Event nodes should include a `kind` property per `docs/schema/event-kinds.md`.')
        md_lines.append('')
        md_lines.append('| Event kind | Count |')
        md_lines.append('|---|---:|')
        for ek, n in sorted(event_kind_counts.items(), key=lambda kv: (-kv[1], kv[0])):
            md_lines.append(f'| {ek} | {fmt_int(n)} |')
        if event_kind_missing:
            md_lines.append(f'| (missing/blank) | {fmt_int(event_kind_missing)} |')
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
