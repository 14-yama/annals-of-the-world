# Refactor/fix_placeholders.py
from neo4j import GraphDatabase
import sys, os

# import db.py from project root
ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from db import get_neo4j_driver

PLACEHOLDER = "'+m[1]+'"

# --------- PASS 2 mapping (same as we agreed) ----------
MAPPINGS = {
    "CONTRASTS": {"pairs": [("right-wing-politics","left-wing-politics")], "framework":"Conflict and Resolution"},
    "ENABLES": {"pairs":[("ballot-initiative","citizen-participation"),
                         ("political-capital","policy-initiatives"),
                         ("political-neutrality","nonpartisan-governance")],
                "framework":"Policy Implementation"},
    "EMPOWERS": {"pairs":[("recall-election","voters")]},
    "ENFORCES": {"pairs":[("transparency-legislation","campaign-ethics"),
                          ("transparency-legislation","government-accountability"),
                          ("oversight-committees","government-accountability"),
                          ("legislative-oversight","government-accountability"),
                          ("state-audit","accountability")],
                 "framework":"Legal Foundation"},
    "ADVOCATES": {"pairs":[("transparency-international","anti-corruption")], "framework":"Cultural Transmission"},
    "TYPE_OF": {"pairs":[("centrism","political-moderation")], "framework":"Classification"},
    "PROMOTES": {"pairs":[("youth-parliament","political-socialization")], "framework":"Cultural Transmission"},
    "STRENGTHENS": {"pairs":[("civic-engagement","democracy"),
                              ("whistleblower-protection","government-accountability")],
                    "framework":"Cultural Transmission"},
    "RESPONDS": {"pairs":[("campaign-strategy","political-climate")], "framework":"Policy Implementation"},
    "CONTRIBUTES_TO": {"pairs":[("public-expenditure","federal-budget"),
                                ("electioneering","political-campaign")],
                       "framework":"Policy Implementation"},
    "LEADS_TO": {"pairs":[("nationalism","nation-state"),
                          ("factionalism","multi-party-system")],
                 "framework":"Idea Evolution"},
    "RESULTS_FROM": {"pairs":[("state-of-emergency","crisis"),
                              ("spoiler-effect","plurality-voting")]},
    "HINDERS": {"pairs":[("legislative-deadlock","policy-passage"),
                         ("political-gridlock","legislative-process")],
                "framework":"Conflict and Resolution"},
    "OCCURS_DURING": {"pairs":[("martial-law","state-of-emergency"),
                               ("transitional-government","political-transition"),
                               ("interim-government","political-transition"),
                               ("caretaker-government","political-transition"),
                               ("election-day","electoral-cycle"),
                               ("policy-window","favorable-political-moments"),
                               ("national-unity-government","political-crisis")]},
    "OCCURS_IN": {"pairs":[("shadow-vote","legislative-caucus"),
                           ("protest-vote","elections"),
                           ("cross-voting","multi-party-system")]},
    "DERIVES_FROM": {"pairs":[("succession-plan","constitutional-framework")]},
    "PRIORITIZES": {"pairs":[("political-realism","national-interest")]},
    "EMBODIES": {"pairs":[("deliberative-assembly","deliberative-democracy")]},
    "REQUIRES": {"pairs":[("rotating-presidency","coalition-partners")]},
    "SHARES_FEATURES_WITH": {"pairs":[("technocracy","authoritarianism")], "framework":"Classification"},
    "PROTECTS": {"pairs":[("political-immunity","public-officials")], "framework":"Legal Foundation"},
    "ESTABLISHES": {"pairs":[("home-rule","local-government")]},
    "OVERSEES": {"pairs":[("state-legislature","state-governor")]},
    "CHECKS": {"pairs":[("executive-branch","legislative-branch")], "framework":"Legal Foundation"},
    "PERFORMS": {"pairs":[("interim-government","caretaker-functions")]},
    "CATEGORIZES_INTO": {"pairs":[("electoral-system","majoritarian-or-proportional"),
                                  ("political-spectrum","classify-political-ideologies")],
                         "framework":"Classification"},
    "INDICATES": {"pairs":[("vote-share","political-party")]},
    "LEADS": {"pairs":[("caretaker-prime-minister","caretaker-government")]},
    "SUSPENDED_DURING": {"pairs":[("habeas-corpus","state-of-emergency")]},
    "INSPIRES": {"pairs":[("labor-movements","syndicalism")]},
    "TRIGGERS": {"pairs":[("election-results","electoral-dispute"),
                          ("no-confidence-motion","government-collapse")],
                 "framework":"Conflict and Resolution"},
    "PRODUCES": {"pairs":[("judicial-inquiry","policy-recommendations")]},
    "INCLUDES": {"pairs":[("initiative","ballot-initiative")], "framework":"Classification"},
    "EQUIVALENT_TO": {"pairs":[("first-past-the-post","winner-takes-all")], "symmetric": True},
    "ASSOCIATED_WITH": {"pairs":[("voting-machine","electronic-fraud")]},
    "LIMITS": {"pairs":[("electoral-threshold","limit-fragmentation")]},
    "PARTICIPATES_IN": {"pairs":[("political-party","elections")]},
    "FACES": {"pairs":[("incumbent","challenger")], "framework":"Conflict and Resolution"},
    "CREATES": {"pairs":[("feudalism","class-system")]},
    "LEGITIMIZES": {"pairs":[("citizen-consent","political-legitimacy")]},
    "FACILITATES": {"pairs":[("non-governmental-organization","policy-discussion")]},
}

# -------- PASS 1: `'+m[1]+'` -> RELATES_TO -----------
def convert_placeholders_to_relates_to(tx, batch=10000):
    q = f"""
    MATCH (a)-[r:`{PLACEHOLDER}`]->(b)
    WITH a,b,r LIMIT $batch
    CREATE (a)-[nr:RELATES_TO]->(b)
    SET nr += properties(r)
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        row = tx.run(q, batch=batch).single()
        c = row["changed"] if row else 0
        total += c
        if c == 0:
            break
    return total

# -------- PASS 2: RELATES_TO -> canonical -----------
def migrate_pair(tx, rel_type, src_slug, dst_slug, framework=None, symmetric=False):
    q = f"""
    MATCH (a:Idea {{slug:$src}}), (b:Idea {{slug:$dst}})
    OPTIONAL MATCH (a)-[r:RELATES_TO]->(b)
    WITH a,b,r
    WHERE r IS NOT NULL
    MERGE (a)-[nr:{rel_type}]->(b)
    SET nr += properties(r)
    {"SET nr.framework = coalesce(nr.framework, $fw)" if framework else ""}
    DELETE r
    RETURN count(nr) AS changed
    """
    params = {"src": src_slug, "dst": dst_slug}
    if framework:
        params["fw"] = framework
    row = tx.run(q, **params).single()
    changed = row["changed"] if row else 0
    if symmetric and changed > 0:
        tx.run(f"""
            MATCH (:Idea {{slug:$src}})-[nr:{rel_type}]->(:Idea {{slug:$dst}})
            SET nr.symmetric = true
        """, src=src_slug, dst=dst_slug)
    return changed

def migrate_all(driver):
    with driver.session() as s:
        c1 = s.execute_write(convert_placeholders_to_relates_to)
        results = [("`'+m[1]+'` → RELATES_TO", c1)]
        for rel_type, cfg in MAPPINGS.items():
            total = 0
            for src, dst in cfg.get("pairs", []):
                total += s.execute_write(
                    migrate_pair, rel_type, src, dst,
                    cfg.get("framework"), cfg.get("symmetric", False)
                )
            results.append((f"RELATES_TO → {rel_type}", total))
    return results

# -------- Diagnostics ----------
def count_placeholder(tx):
    return tx.run(f"MATCH ()-[r:`{PLACEHOLDER}`]->() RETURN count(r) AS c").single()["c"]

def count_relates_to(tx):
    return tx.run("MATCH ()-[r:RELATES_TO]->() RETURN count(r) AS c").single()["c"]

if __name__ == "__main__":
    driver = get_neo4j_driver()

    with driver.session() as s:
        before_ph = s.execute_read(count_placeholder)
        print(f"Before: `'+m[1]+'` edges = {before_ph}")

    print("⏳ Migrating…")
    for label, cnt in migrate_all(driver):
        print(f" - {label}: {cnt} edges changed")

    with driver.session() as s:
        after_ph = s.execute_read(count_placeholder)
        after_rel = s.execute_read(count_relates_to)
        print(f"\nAfter:  `'+m[1]+'` edges = {after_ph}")
        print(f"After:  RELATES_TO edges = {after_rel}")
