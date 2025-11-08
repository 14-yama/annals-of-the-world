#!/usr/bin/env python3
"""Generate a static interactive HTML triage page from data/orphan_nodes.csv.

The script reads the CSV written by autogen and writes `data/orphan_triage.html`.
The HTML embeds the orphan rows as JSON and provides simple JS UI to mark
each orphan with `approve`, `ignore`, or `needs_review` and to download the
decisions as CSV for further processing.
"""
import csv
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
ORPHAN_CSV = os.path.join(DATA_DIR, 'orphan_nodes.csv')
OUT_HTML = os.path.join(DATA_DIR, 'orphan_triage.html')


def load_orphans(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as cf:
        r = csv.DictReader(cf)
        for row in r:
            # normalize fields
            rows.append({
                'cluster': row.get('cluster',''),
                'file': row.get('file',''),
                'id': row.get('id',''),
                'slug': row.get('slug',''),
                'suggested_action': row.get('suggested_action','')
            })
    return rows


def build_html(orphan_rows):
    # group by cluster
    clusters = {}
    for r in orphan_rows:
        clusters.setdefault(r['cluster'], []).append(r)

    data_json = json.dumps(clusters, ensure_ascii=False, indent=2)

    html_template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Orphan Nodes Triage</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 1100px; margin: 24px auto; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 18px; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; }}
    th {{ background: #f6f6f6; text-align: left; }}
    .actions select {{ width: 140px; }}
    .controls {{ margin-bottom: 16px; }}
    .cluster-title {{ margin-top: 28px; margin-bottom: 6px; font-size: 18px; }}
    .small {{ font-size: 13px; color: #666 }}
    button {{ margin-right: 8px; }}
  </style>
</head>
<body>
  <h1>Orphan Nodes Triage</h1>
  <p class="small">Generated from <code>data/orphan_nodes.csv</code>. Use the dropdowns to mark each orphan, then click <strong>Download decisions</strong> to export a CSV of reviewer choices.</p>

  <div class="controls">
    <button id="download">Download decisions (CSV)</button>
    <button id="mark_all_approve">Mark all approve</button>
    <button id="mark_all_ignore">Mark all ignore</button>
    <button id="reset_all">Reset all</button>
  </div>

  <div id="content"></div>

  <script>
  const CLUSTERS = __DATA_JSON__;

    function render() {{
      const container = document.getElementById('content');
      container.innerHTML = '';
      Object.keys(CLUSTERS).sort().forEach(cluster => {{
        const rows = CLUSTERS[cluster];
        const wrapper = document.createElement('div');
  const title = document.createElement('div');
  title.className = 'cluster-title';
  title.textContent = `Cluster: ${cluster} — orphan count: ${rows.length}`;
        wrapper.appendChild(title);

        const table = document.createElement('table');
        const thead = document.createElement('thead');
        thead.innerHTML = '<tr><th>id</th><th>slug</th><th>file</th><th>suggested</th><th>action</th><th>notes</th></tr>';
        table.appendChild(thead);
        const tb = document.createElement('tbody');
        rows.forEach((r, idx) => {{
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>${r.id}</td>
            <td><code>${r.slug}</code></td>
            <td>${r.file}</td>
            <td>${r.suggested_action || ''}</td>
            <td class="actions">
              <select data-cluster="${cluster}" data-idx="${idx}">
                <option value="">--</option>
                <option value="approve">Approve (add relationship)</option>
                <option value="ignore">Ignore</option>
                <option value="needs_review">Needs review</option>
              </select>
            </td>
            <td><input type="text" data-cluster="${cluster}" data-idx="${idx}" placeholder="notes (optional)" style="width:100%"></td>
          `;
          tb.appendChild(tr);
        }});
        table.appendChild(tb);
        wrapper.appendChild(table);
        container.appendChild(wrapper);
      }});
    }}

    function collectDecisions() {{
      const out = [];
      Object.keys(CLUSTERS).forEach(cluster => {{
        CLUSTERS[cluster].forEach((r, idx) => {{
          const sel = document.querySelector(`select[data-cluster="${cluster}"][data-idx="${idx}"]`);
          const note = document.querySelector(`input[data-cluster="${cluster}"][data-idx="${idx}"]`);
          out.push({
            cluster: cluster,
            id: r.id,
            slug: r.slug,
            file: r.file,
            suggested_action: r.suggested_action || '',
            decision: sel ? sel.value : '',
            notes: note ? note.value : ''
          });
        }});
      }});
      return out;
    }}

    function downloadCSV(rows) {{
      const headers = ['cluster','id','slug','file','suggested_action','decision','notes'];
      const lines = [headers.join(',')];
      rows.forEach(r => {{
        const esc = v => '"' + String(v || '').replace(/"/g, '""') + '"';
        lines.push([r.cluster, r.id, r.slug, r.file, r.suggested_action, r.decision, r.notes].map(esc).join(','));
      }});
      const blob = new Blob([lines.join('\n')], {{type: 'text/csv;charset=utf-8;'}});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'orphan_triage_decisions.csv';
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }}

    document.getElementById('download').addEventListener('click', () => {{
      const rows = collectDecisions();
      downloadCSV(rows);
    }});

    document.getElementById('mark_all_approve').addEventListener('click', () => {{
      document.querySelectorAll('select').forEach(s => s.value = 'approve');
    }});
    document.getElementById('mark_all_ignore').addEventListener('click', () => {{
      document.querySelectorAll('select').forEach(s => s.value = 'ignore');
    }});
    document.getElementById('reset_all').addEventListener('click', () => {{
      document.querySelectorAll('select').forEach(s => s.value = '');
      document.querySelectorAll('input[type=text]').forEach(i => i.value = '');
    }});

    // initial render
    render();
  </script>
</body>
</html>
"""
    # embed data JSON safely (not an f-string to avoid JS template conflicts)
    html = html_template.replace('__DATA_JSON__', data_json)
    return html


def main():
    if not os.path.exists(ORPHAN_CSV):
        print(f'No orphan CSV found at {ORPHAN_CSV}. Run autogen first.')
        return
    rows = load_orphans(ORPHAN_CSV)
    html = build_html(rows)
    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Wrote triage page to {OUT_HTML}')


if __name__ == '__main__':
    main()
