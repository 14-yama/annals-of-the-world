# Refactor/asia_periods_patch.py

import os
import sys
from typing import Dict, Any, List

# --- ensure we can import db.get_neo4j_driver() from project root ---
THIS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(THIS_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from db import get_neo4j_driver  # noqa: E402


# ---------------------------
# Data
# ---------------------------

PERIOD_ROWS: List[Dict[str, Any]] = [
    # Tibet / Himalaya
    {"slug": "tibetan-empire",               "name": "Tibetan Empire",                          "region": "East Asia",               "civilization": "Tibet/Himalaya"},
    {"slug": "phagmodrupa-tsang",            "name": "Phagmodrupa/Tsang",                       "region": "East Asia",               "civilization": "Tibet/Himalaya"},
    {"slug": "ganden-phodrang",              "name": "Ganden Phodrang (Dalai Lama govt)",       "region": "East Asia",               "civilization": "Tibet/Himalaya"},
    {"slug": "qing-protectorate-tibet",      "name": "Qing Protectorate in Tibet",              "region": "East Asia",               "civilization": "Tibet/Himalaya"},
    {"slug": "prc-tibet-autonomous-region",  "name": "PRC Tibet Autonomous Region",             "region": "East Asia",               "civilization": "Tibet/Himalaya"},

    # Xinjiang / Tarim Basin
    {"slug": "karakhanid-tarim",             "name": "Kara-Khanid in Tarim",                    "region": "Central Asia",            "civilization": "Xinjiang/Tarim"},
    {"slug": "chagatai-khanate",             "name": "Chagatai Khanate",                        "region": "Central Asia",            "civilization": "Xinjiang/Tarim"},
    {"slug": "moghulistan",                  "name": "Moghulistan",                              "region": "Central Asia",            "civilization": "Xinjiang/Tarim"},
    {"slug": "yarkent-khanate",              "name": "Yarkent Khanate",                          "region": "Central Asia",            "civilization": "Xinjiang/Tarim"},
    {"slug": "dzungar-khanate",              "name": "Dzungar Khanate",                          "region": "Central Asia",            "civilization": "Xinjiang/Tarim"},
    {"slug": "qing-xinjiang",                "name": "Qing Xinjiang",                            "region": "North Asia / Siberia",    "civilization": "Xinjiang/Tarim"},
    {"slug": "roc-prc-xinjiang",             "name": "ROC/PRC Xinjiang",                         "region": "North Asia / Siberia",    "civilization": "Xinjiang/Tarim"},

    # Arabian Peninsula (modern lines)
    {"slug": "oman",                         "name": "Oman",                                     "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "uae",                          "name": "United Arab Emirates",                     "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "qatar",                        "name": "Qatar",                                    "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "bahrain",                      "name": "Bahrain",                                  "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "kuwait",                       "name": "Kuwait",                                   "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "mutawakkilite-yemen",          "name": "Mutawakkilite Kingdom of Yemen",           "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "north-yemen-yar",              "name": "Yemen Arab Republic (North Yemen)",        "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "south-yemen-pdry",             "name": "People’s Democratic Republic of Yemen",    "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},
    {"slug": "republic-of-yemen",            "name": "Republic of Yemen",                        "region": "West Asia / Middle East", "civilization": "Arabian Peninsula"},

    # Sri Lanka full arc
    {"slug": "anuradhapura",                 "name": "Anuradhapura",                             "region": "South Asia",              "civilization": "Sri Lanka"},
    {"slug": "polonnaruwa",                  "name": "Polonnaruwa",                              "region": "South Asia",              "civilization": "Sri Lanka"},
    {"slug": "kotte-kandy",                  "name": "Kotte/Kandy Kingdoms",                     "region": "South Asia",              "civilization": "Sri Lanka"},
    {"slug": "ceylon-colonial",              "name": "Ceylon (Portuguese/Dutch/British)",        "region": "South Asia",              "civilization": "Sri Lanka"},
    {"slug": "sri-lanka",                    "name": "Sri Lanka",                                "region": "South Asia",              "civilization": "Sri Lanka"},
]

CHAINS = [
    ["tibetan-empire", "phagmodrupa-tsang", "ganden-phodrang", "qing-protectorate-tibet", "prc-tibet-autonomous-region"],
    ["karakhanid-tarim", "chagatai-khanate", "moghulistan", "yarkent-khanate", "dzungar-khanate", "qing-xinjiang", "roc-prc-xinjiang"],
    ["anuradhapura", "polonnaruwa", "kotte-kandy", "ceylon-colonial", "sri-lanka"],
]
YEMEN_NORTH = ["mutawakkilite-yemen", "north-yemen-yar", "republic-of-yemen"]
YEMEN_SOUTH = ["south-yemen-pdry", "republic-of-yemen"]

EVENT_WINDOWS = [
    {"slug": "mongol-conquests-asia", "name": "Mongol Conquests (Asia)"},
    {"slug": "black-death-asia",      "name": "Black Death in Asia"},
    {"slug": "ww1-asia",              "name": "World War I — Asia-Pacific"},
    {"slug": "ww2-asia",              "name": "World War II — Asia-Pacific"},
    {"slug": "asian-decolonization",  "name": "Decolonization in Asia"},
]
WINDOW_PERIOD_MAP = [
    # (window, [periods...]) — missing periods are safely skipped via OPTIONAL MATCH
    ("mongol-conquests-asia", ["song", "jin-jurchen", "western-xia", "goryeo", "chagatai-khanate", "yarkent-khanate"]),
    ("black-death-asia",      ["yuan", "goryeo", "delhi-sultanate"]),
    ("ww1-asia",              ["republic-of-china", "japanese-empire", "british-raj", "french-colonial-vietnam"]),
    ("ww2-asia",              ["republic-of-china", "japanese-empire", "nguyen-dynasty", "dutch-east-indies"]),
    ("asian-decolonization",  ["ceylon-colonial", "sri-lanka", "republic-of-indonesia", "lao-pdr", "kingdom-of-cambodia-modern"]),
]

SANITY_TIBET     = ["tibetan-empire", "phagmodrupa-tsang", "ganden-phodrang", "qing-protectorate-tibet", "prc-tibet-autonomous-region"]
SANITY_XINJIANG  = ["karakhanid-tarim", "chagatai-khanate", "moghulistan", "yarkent-khanate", "dzungar-khanate", "qing-xinjiang", "roc-prc-xinjiang"]
SANITY_SRILANKA  = ["anuradhapura", "polonnaruwa", "kotte-kandy", "ceylon-colonial", "sri-lanka"]


# ---------------------------
# Cypher helpers
# ---------------------------

def upsert_periods(tx, rows):
    q = """
    UNWIND $rows AS p
    MERGE (n:Period {slug:p.slug})
    SET n.name = p.name,
        n.region = p.region,
        n.civilization = p.civilization
    RETURN count(n) AS upserted
    """
    return tx.run(q, rows=rows).single()["upserted"]


def wire_chains(tx, chains):
    q = """
    UNWIND $chains AS chain
    UNWIND range(0, size(chain)-2) AS i
    MATCH (a:Period {slug:chain[i]}),
          (b:Period {slug:chain[i+1]})
    MERGE (a)-[r:PRECEDES]->(b)
    ON CREATE SET r.framework = 'Temporal Linkage'
    RETURN count(r) AS linked
    """
    return tx.run(q, chains=chains).single()["linked"]


def wire_linear(tx, slugs):
    q = """
    UNWIND range(0, size($lst)-2) AS i
    MATCH (a:Period {slug:$lst[i]}), (b:Period {slug:$lst[i+1]})
    MERGE (a)-[r:PRECEDES]->(b)
    ON CREATE SET r.framework = 'Temporal Linkage'
    RETURN count(r) AS linked
    """
    return tx.run(q, lst=slugs).single()["linked"]


def upsert_windows(tx, windows):
    q = """
    UNWIND $rows AS e
    MERGE (w:EventWindow {slug:e.slug})
    SET w.name = e.name, w.region = 'Asia'
    RETURN count(w) AS upserted
    """
    return tx.run(q, rows=windows).single()["upserted"]


def tie_windows(tx, pairs):
    q = """
    UNWIND $pairs AS pair
    MATCH (w:EventWindow {slug:pair.win})
    UNWIND pair.periods AS ps
    OPTIONAL MATCH (p:Period {slug:ps})
    FOREACH (_ IN CASE WHEN p IS NULL THEN [] ELSE [1] END |
      MERGE (w)-[rd:OCCURS_DURING]->(p)
      ON CREATE SET rd.framework = 'Event Context'
    )
    RETURN count(*) AS processed
    """
    shaped = [{"win": w, "periods": plist} for (w, plist) in pairs]
    return tx.run(q, pairs=shaped).single()["processed"]


def sanity_check(tx):
    q = """
    WITH $tibet AS tibet, $xinjiang AS xinjiang, $srilanka AS srilanka
    RETURN
      reduce(ok=0, s IN tibet    | ok + CASE WHEN EXISTS { MATCH (:Period {slug:s}) } THEN 1 ELSE 0 END) AS tibet_nodes_ok,
      reduce(ok=0, s IN xinjiang | ok + CASE WHEN EXISTS { MATCH (:Period {slug:s}) } THEN 1 ELSE 0 END) AS xinjiang_nodes_ok,
      reduce(ok=0, s IN srilanka | ok + CASE WHEN EXISTS { MATCH (:Period {slug:s}) } THEN 1 ELSE 0 END) AS srilanka_nodes_ok,

      reduce(cnt=0, i IN range(0, size(tibet)-2)
             | cnt + coalesce(size([( :Period {slug:tibet[i]})-[:PRECEDES]->(:Period {slug:tibet[i+1]}) | 1]), 0)
      ) AS tibet_precedes,

      reduce(cnt=0, i IN range(0, size(xinjiang)-2)
             | cnt + coalesce(size([( :Period {slug:xinjiang[i]})-[:PRECEDES]->(:Period {slug:xinjiang[i+1]}) | 1]), 0)
      ) AS xinjiang_precedes,

      reduce(cnt=0, i IN range(0, size(srilanka)-2)
             | cnt + coalesce(size([( :Period {slug:srilanka[i]})-[:PRECEDES]->(:Period {slug:srilanka[i+1]}) | 1]), 0)
      ) AS srilanka_precedes
    """
    rec = tx.run(q, tibet=SANITY_TIBET, xinjiang=SANITY_XINJIANG, srilanka=SANITY_SRILANKA).single()
    return {k: rec[k] for k in rec.keys()}


def apply_asia_patch(driver):
    out = {}
    with driver.session() as session:
        out["periods_upserted"] = session.execute_write(upsert_periods, PERIOD_ROWS)
        out["chains_linked"]    = session.execute_write(wire_chains, CHAINS)
        out["yemen_north"]      = session.execute_write(wire_linear, YEMEN_NORTH)
        out["yemen_south"]      = session.execute_write(wire_linear, YEMEN_SOUTH)
        out["windows_upserted"] = session.execute_write(upsert_windows, EVENT_WINDOWS)
        out["window_links"]     = session.execute_write(tie_windows, WINDOW_PERIOD_MAP)
        out["sanity"]           = session.execute_write(sanity_check)
    return out


if __name__ == "__main__":
    driver = get_neo4j_driver()
    print("🚀 Applying Asia Period/Epoch/EventWindow patch…")
    summary = apply_asia_patch(driver)

    print("\n✅ Done.\n")
    print("Upserted Period nodes:      ", summary["periods_upserted"])
    print("Linked PRECEDES (chains):   ", summary["chains_linked"])
    print("Linked Yemen (north):       ", summary["yemen_north"])
    print("Linked Yemen (south):       ", summary["yemen_south"])
    print("Upserted EventWindows:      ", summary["windows_upserted"])
    print("Window→Period links tried:  ", summary["window_links"])

    s = summary["sanity"]
    print("\n— Sanity —")
    print(f" Tibet:    nodes {s['tibet_nodes_ok']}/{len(SANITY_TIBET)}; PRECEDES in chain = {s['tibet_precedes']}")
    print(f" Xinjiang: nodes {s['xinjiang_nodes_ok']}/{len(SANITY_XINJIANG)}; PRECEDES in chain = {s['xinjiang_precedes']}")
    print(f" SriLanka: nodes {s['srilanka_nodes_ok']}/{len(SANITY_SRILANKA)}; PRECEDES in chain = {s['srilanka_precedes']}")
