import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from db import get_neo4j_driver


# refactor_relationships.py
from neo4j import GraphDatabase

# --- helpers ---------------------------------------------------------------

SAME_DIRECTION_MAP = {
    # general normalization
    "CONTRASTED_WITH": "CONTRASTS",
    "ADVOCATES_FOR": "ADVOCATES",
    "RESPONDS_TO": "RESPONDS",
    "EVOLVED_INTO": "EVOLVES_INTO",
    "EVOLVED_FROM": "EVOLVES_FROM",
    "BASED_ON": "DERIVES_FROM",
    "BUILT_ON": "BUILDS_ON",
    "OCCURS_AFTER": "FOLLOWS",
    "HELD_DURING": "OCCURS_DURING",
    # consolidate to OPPOSES (active voice)
    "CRITICIZED_FOR": "OPPOSES",
    "CRITICIZES": "OPPOSES",
    "CRITIQUES": "OPPOSES",
    "OPPOSED_TO": "OPPOSES",
    # policy verb
    "IMPLEMENTED_IN": "IMPLEMENTS",
}

# relationship types that should add/ensure a framework tag when converted
FRAMEWORK_FOR_OPPOSES = "Conflict and Resolution"
FRAMEWORK_FOR_IMPLEMENTS = "Policy Implementation"

def run(tx, cypher, **params):
    return tx.run(cypher, **params).data()

def rename_same_direction(tx, old_type, new_type):
    """
    Create new rel with same direction + copy properties, then delete old.
    Returns count of changed relationships.
    """
    cypher = f"""
    MATCH (a)-[r:`{old_type}`]->(b)
    WITH a,b,r LIMIT 10000
    CREATE (a)-[nr:`{new_type}`]->(b)
    SET nr += r
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        rows = run(tx, cypher)
        changed = rows[0]["changed"] if rows else 0
        total += changed
        if changed == 0:
            break
    return total

def rename_same_direction_with_framework(tx, old_type, new_type, framework_value):
    cypher = f"""
    MATCH (a)-[r:`{old_type}`]->(b)
    WITH a,b,r LIMIT 10000
    CREATE (a)-[nr:`{new_type}`]->(b)
    SET nr += r,
        nr.framework = coalesce(r.framework, $fw)
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        rows = run(tx, cypher, fw=framework_value)
        changed = rows[0]["changed"] if rows else 0
        total += changed
        if changed == 0:
            break
    return total

def flip_direction(tx, old_type, new_type, framework_value=None):
    """
    Flip (a)-[:OLD]->(b) into (b)-[:NEW]->(a), copy properties, optionally set framework.
    """
    set_fw = ", nr.framework = coalesce(r.framework, $fw)" if framework_value else ""
    cypher = f"""
    MATCH (a)-[r:`{old_type}`]->(b)
    WITH a,b,r LIMIT 10000
    CREATE (b)-[nr:`{new_type}`]->(a)
    SET nr += r{set_fw}
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        rows = run(tx, cypher, fw=framework_value) if framework_value else run(tx, cypher)
        changed = rows[0]["changed"] if rows else 0
        total += changed
        if changed == 0:
            break
    return total

def conflict_lowercase_to_opposes(tx):
    """
    Convert lowercase noun 'conflict' to OPPOSES and ensure framework tagging.
    """
    cypher = """
    MATCH (a)-[r:conflict]->(b)
    WITH a,b,r LIMIT 10000
    CREATE (a)-[nr:OPPOSES]->(b)
    SET nr += r,
        nr.framework = coalesce(r.framework, $fw)
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        rows = run(tx, cypher, fw=FRAMEWORK_FOR_OPPOSES)
        changed = rows[0]["changed"] if rows else 0
        total += changed
        if changed == 0:
            break
    return total

def implemented_in_to_implements(tx):
    """
    IMPLEMENTED_IN -> IMPLEMENTS (same direction), and when the target is a :Place,
    persist context as a property. Also tag framework:'Policy Implementation' by default.
    """
    # Case 1: target is a Place
    cypher_place = """
    MATCH (a)-[r:IMPLEMENTED_IN]->(p:Place)
    WITH a,p,r LIMIT 10000
    CREATE (a)-[nr:IMPLEMENTS]->(p)
    SET nr += r,
        nr.framework = coalesce(r.framework, $fw),
        nr.context_place = coalesce(r.context_place, p.slug, p.name)
    DELETE r
    RETURN count(nr) AS changed
    """
    # Case 2: target is NOT a Place (leave as-is but still rename + framework)
    cypher_other = """
    MATCH (a)-[r:IMPLEMENTED_IN]->(b)
    WHERE NOT b:Place
    WITH a,b,r LIMIT 10000
    CREATE (a)-[nr:IMPLEMENTS]->(b)
    SET nr += r,
        nr.framework = coalesce(r.framework, $fw)
    DELETE r
    RETURN count(nr) AS changed
    """
    total = 0
    while True:
        rows = run(tx, cypher_place, fw=FRAMEWORK_FOR_IMPLEMENTS)
        c1 = rows[0]["changed"] if rows else 0
        total += c1
        rows = run(tx, cypher_other, fw=FRAMEWORK_FOR_IMPLEMENTS)
        c2 = rows[0]["changed"] if rows else 0
        total += c2
        if c1 == 0 and c2 == 0:
            break
    return total

# --- driver task -----------------------------------------------------------

def refactor_all(driver):
    results = []

    with driver.session() as session:
        # 1) special cases first
        changed = session.execute_write(conflict_lowercase_to_opposes)
        results.append(("conflict → OPPOSES (+framework)", changed))

        changed = session.execute_write(flip_direction, "OPPOSED_BY", "OPPOSES", FRAMEWORK_FOR_OPPOSES)
        results.append(("OPPOSED_BY → (flip) OPPOSES (+framework)", changed))

        changed = session.execute_write(implemented_in_to_implements)
        results.append(("IMPLEMENTED_IN → IMPLEMENTS (+context_place when target is :Place)", changed))

        # 2) consolidate critiques to OPPOSES (ensure framework)
        for t in ["CRITICIZED_FOR", "CRITICIZES", "CRITIQUES", "OPPOSED_TO"]:
            changed = session.execute_write(rename_same_direction_with_framework, t, "OPPOSES", FRAMEWORK_FOR_OPPOSES)
            results.append((f"{t} → OPPOSES (+framework)", changed))

        # 3) general same-direction renames
        general = [
            ("CONTRASTED_WITH", "CONTRASTS"),
            ("ADVOCATES_FOR", "ADVOCATES"),
            ("RESPONDS_TO", "RESPONDS"),
            ("EVOLVED_INTO", "EVOLVES_INTO"),
            ("EVOLVED_FROM", "EVOLVES_FROM"),
            ("BASED_ON", "DERIVES_FROM"),
            ("BUILT_ON", "BUILDS_ON"),
            ("OCCURS_AFTER", "FOLLOWS"),
            ("HELD_DURING", "OCCURS_DURING"),
        ]
        for old_t, new_t in general:
            changed = session.execute_write(rename_same_direction, old_t, new_t)
            results.append((f"{old_t} → {new_t}", changed))

    return results

# --- run -------------------------------------------------------------------

if __name__ == "__main__":
    driver = get_neo4j_driver()
    summary = refactor_all(driver)

    print("✅ Refactor complete. Summary:")
    for label, count in summary:
        print(f" - {label}: {count} edges updated")
