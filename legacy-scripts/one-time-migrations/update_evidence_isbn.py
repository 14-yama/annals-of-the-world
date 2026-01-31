#!/usr/bin/env python3
"""Add `isbn` attributes where known and set `evidence_url` to null for all Evidence JSON files."""
import json
import os
import re

EVIDENCE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "Evidence")

# ISBN mapping researched earlier
ISBN_MAP = {
    "Bernard_2005": "9780300122718",
    "Black_2008": "9780521843898",
    "Bossy_1975": "9780232513851",
    "Bray_1994": "9780227679203",
    "Brook_1962": "9780198212928",
    "Cameron_2012": "9780199547852",
    "Collinson_1967": "9780198227809",
    "Collinson_1979": "9780224015622",
    "Daniell_2003": "9780300099300",
    "Doran_1994": "9780415073974",
    "Duffy_2009": "9780300152166",
    "Elton_1982": "9780521287579",
    "Fletcher_2004": "9780582772854",
    "Freeman_2011": "9780754656890",
    "Guy_2000": "9780340731390",
    "Guy_2004": "9780007156580",
    "Haigh_1993": "9780198221623",
    "Helmholz_1990": "9780521385626",
    "Hoyle_2001": "9780199243563",
    "Ives_2004": "9780631234791",
    "Jones_1982": "9780391026490",
    "Jones_2002": "9780631211686",
    "Kreider_1979": "9780674256095",
    "Lake_1988": "9780049422001",
    "Land_1977": "9780850331349",
    "Loades_1965": "9780521088992",
    "Loades_1987": "9780713455052",
    "MacCulloch_1996": "9780300074482",
    "Marshall_2017": "9780300170627",
    "Martin_1999": "9780719037191",
    "McCoog_1996": "9789004103535",
    "McGrade_1997": "9780521584135",
    "Richardson_1961": "9780807104187",
    "Scarisbrick_1968": "9780300071580",
    "Tremlett_2010": "9780571235117",
    "Youings_1971": "9780049420960",
}

def get_key_from_filename(filename):
    m = re.search(r'evidence[._]([A-Za-z]+_\d{4})', filename)
    return m.group(1) if m else None

def main():
    updated = []
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.json'):
            continue
        path = os.path.join(EVIDENCE_DIR, fname)
        with open(path, 'r') as f:
            data = json.load(f)

        # set evidence_url to null (None in Python -> null in JSON)
        changed = False
        if data.get('evidence_url') is not None:
            data['evidence_url'] = None
            changed = True

        key = get_key_from_filename(fname)
        if key and key in ISBN_MAP:
            isbn_val = ISBN_MAP[key]
            if data.get('isbn') != isbn_val:
                data['isbn'] = isbn_val
                changed = True

        if changed:
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)
                f.write('\n')
            updated.append(fname)

    print(f"Updated {len(updated)} files")
    for u in updated:
        print(f" - {u}")

if __name__ == '__main__':
    main()
