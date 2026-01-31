#!/usr/bin/env python3
"""
Add comprehensive relationships to the English Reformation cluster.

This script adds historically accurate relationships for:
- All Person nodes (especially those with 0 edges like John Foxe)
- All orphaned Events, Texts, Institutions, and Movements
- Cross-connections between key actors of the reformation

Usage:
    python scripts/admin/add_comprehensive_relationships.py --cluster English_Reformation
"""

import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

# ============================================================================
# COMPREHENSIVE RELATIONSHIP ADDITIONS
# ============================================================================

# Format: (start_slug, type, end_slug, description)

PERSON_RELATIONSHIPS = [
    # === JOHN FOXE (martyrologist, key figure) ===
    ("John_Foxe", "WRITES", "Acts_and_Monuments_1563", 
     "John Foxe authored Acts and Monuments (Book of Martyrs), documenting Protestant martyrs."),
    ("John_Foxe", "DOCUMENTS", "Marian_Persecutions", 
     "John Foxe documented the Marian persecutions, creating enduring Protestant martyrology."),
    ("John_Foxe", "ENDORSES", "Protestant_Doctrine_in_England", 
     "John Foxe promoted Protestant doctrine through his martyrological writings."),
    ("John_Foxe", "CORRESPONDS_WITH", "Edmund_Grindal", 
     "John Foxe corresponded with Archbishop Grindal on church matters."),
    
    # === HUGH LATIMER (preacher, martyr) ===
    ("Hugh_Latimer", "ENDORSES", "Protestant_Doctrine_in_England", 
     "Hugh Latimer championed Protestant doctrine through powerful preaching."),
    ("Hugh_Latimer", "OPPOSES", "Catholic_Restoration", 
     "Hugh Latimer opposed Mary I's Catholic restoration, refusing to recant."),
    ("Hugh_Latimer", "DIES_IN", "Oxford_Martyrs_1555_1556", 
     "Hugh Latimer was burned at the stake at Oxford alongside Nicholas Ridley in 1555."),
    ("Hugh_Latimer", "PREACHES_AT", "Royal_Court", 
     "Hugh Latimer served as court preacher under Edward VI."),
    
    # === NICHOLAS RIDLEY (bishop, martyr) ===
    ("Nicholas_Ridley", "ENDORSES", "Protestant_Doctrine_in_England", 
     "Nicholas Ridley promoted Protestant doctrine as Bishop of London."),
    ("Nicholas_Ridley", "COLLABORATES_WITH", "Thomas_Cranmer", 
     "Nicholas Ridley collaborated with Cranmer on liturgical reforms."),
    ("Nicholas_Ridley", "DIES_IN", "Oxford_Martyrs_1555_1556", 
     "Nicholas Ridley was martyred at Oxford in 1555."),
    ("Nicholas_Ridley", "OPPOSES", "Catholic_Restoration", 
     "Nicholas Ridley opposed Marian Catholic restoration, leading to his martyrdom."),
    
    # === EDMUND CAMPION (Jesuit martyr) ===
    ("Edmund_Campion", "PARTICIPATES_IN", "Jesuit_Mission_1580s", 
     "Edmund Campion led the Jesuit mission to England in 1580."),
    ("Edmund_Campion", "MEMBER_OF", "Society_of_Jesus", 
     "Edmund Campion was a Jesuit priest sent to minister to English Catholics."),
    ("Edmund_Campion", "OPPOSES", "Act_of_Supremacy_1559", 
     "Edmund Campion rejected royal supremacy, defending papal authority."),
    ("Edmund_Campion", "EXECUTED_BY", "Elizabeth_I", 
     "Edmund Campion was executed for treason in 1581 under Elizabethan recusancy laws."),
    
    # === ROBERT PARSONS (Jesuit organizer) ===
    ("Robert_Parsons", "PARTICIPATES_IN", "Jesuit_Mission_1580s", 
     "Robert Parsons co-led the Jesuit mission to England with Campion."),
    ("Robert_Parsons", "MEMBER_OF", "Society_of_Jesus", 
     "Robert Parsons was a leading Jesuit organizer of the English mission."),
    ("Robert_Parsons", "ORGANIZES", "English_Seminaries_Douai_Rheims", 
     "Robert Parsons helped establish and administer seminaries for English clergy."),
    ("Robert_Parsons", "ENDORSES", "Recusant_Catholicism", 
     "Robert Parsons supported the recusant Catholic cause through writing and organization."),
    
    # === JOHN HOOPER (reformer, martyr) ===
    ("John_Hooper", "ENDORSES", "Protestant_Doctrine_in_England", 
     "John Hooper advocated for further Protestant reforms beyond Cranmer's program."),
    ("John_Hooper", "DISPUTES", "Vestiarian_Controversy_1566", 
     "John Hooper's earlier resistance to vestments prefigured the Vestiarian controversy."),
    ("John_Hooper", "DIES_IN", "Heresy_Persecutions", 
     "John Hooper was martyred during the Marian heresy persecutions in 1555."),
    ("John_Hooper", "OPPOSES", "Catholic_Restoration", 
     "John Hooper refused to recant during Mary I's Catholic restoration."),
    
    # === MARY QUEEN OF SCOTS ===
    ("Mary_Queen_of_Scots", "CLAIMS", "English_Realm", 
     "Mary Queen of Scots claimed the English throne as great-granddaughter of Henry VII."),
    ("Mary_Queen_of_Scots", "SYMBOLIZES", "Recusant_Catholicism", 
     "Mary Queen of Scots became a focal point for Catholic hopes in England."),
    ("Mary_Queen_of_Scots", "DIES_IN", "Execution_of_Mary_Queen_of_Scots_1587", 
     "Mary Queen of Scots was executed at Fotheringhay Castle in 1587."),
    ("Mary_Queen_of_Scots", "THREATENED_BY", "Elizabeth_I", 
     "Mary Queen of Scots posed a dynastic threat to Elizabeth I's Protestant regime."),
    
    # === POPE CLEMENT VII ===
    ("Pope_Clement_VII", "REFUSES", "Annulment_Proceedings", 
     "Pope Clement VII refused to grant Henry VIII's annulment, fearing Habsburg reprisal."),
    ("Pope_Clement_VII", "LEADS", "Papacy", 
     "Pope Clement VII headed the Roman curia during the annulment crisis."),
    ("Pope_Clement_VII", "DISPUTES", "Henry_VIII", 
     "Pope Clement VII's refusal of the annulment precipitated the break with Rome."),
    
    # === WILLIAM CECIL (Lord Burghley) ===
    ("William_Cecil", "ADVISES", "Elizabeth_I", 
     "William Cecil served as Elizabeth I's principal secretary and chief advisor."),
    ("William_Cecil", "ORGANIZES", "Recusancy_Fines_Regime", 
     "William Cecil helped implement enforcement against Catholic recusants."),
    ("William_Cecil", "ENDORSES", "Via_Media", 
     "William Cecil supported the Elizabethan religious settlement."),
    ("William_Cecil", "OPPOSES", "Mary_Queen_of_Scots", 
     "William Cecil advocated for Mary Queen of Scots' execution."),
    
    # === ADDITIONAL EDGES FOR EXISTING PERSONS WITH FEW EDGES ===
    
    # Thomas Cranmer (already has 3 edges, add more)
    ("Thomas_Cranmer", "WRITES", "Book_of_Common_Prayer_1549", 
     "Thomas Cranmer authored the first Book of Common Prayer."),
    ("Thomas_Cranmer", "WRITES", "Book_of_Common_Prayer_1552", 
     "Thomas Cranmer authored the revised Book of Common Prayer."),
    ("Thomas_Cranmer", "WRITES", "Forty-Two_Articles_1553", 
     "Thomas Cranmer drafted the Forty-Two Articles of religion."),
    ("Thomas_Cranmer", "DIES_IN", "Oxford_Martyrs_1555_1556", 
     "Thomas Cranmer was burned at the stake at Oxford in 1556."),
    
    # Henry VIII (add more connections)
    ("Henry_VIII", "DECLARES", "Break_with_Rome", 
     "Henry VIII declared the break with Rome to secure his annulment and supremacy."),
    ("Henry_VIII", "PROMULGATES", "Act_of_Supremacy_1534", 
     "Henry VIII promulgated the Act of Supremacy establishing royal headship of the church."),
    ("Henry_VIII", "ORGANIZES", "Dissolution_of_the_Monasteries", 
     "Henry VIII ordered the dissolution of English monasteries."),
    
    # Edward VI
    ("Edward_VI", "PROMULGATES", "Book_of_Common_Prayer_1549", 
     "Edward VI's regime promulgated the first Book of Common Prayer."),
    ("Edward_VI", "PROMULGATES", "Book_of_Common_Prayer_1552", 
     "Edward VI's regime promulgated the revised Book of Common Prayer."),
    
    # Mary I (add more)
    ("Mary_I", "ORGANIZES", "Heresy_Persecutions", 
     "Mary I organized heresy persecutions against Protestants."),
    ("Mary_I", "RESTORES", "Papal_Supremacy", 
     "Mary I restored papal supremacy in England."),
    ("Mary_I", "REPEALS", "Act_of_Supremacy_1534", 
     "Mary I repealed Henrician and Edwardian religious legislation."),
    
    # Elizabeth I (add more)
    ("Elizabeth_I", "PROMULGATES", "Act_of_Supremacy_1559", 
     "Elizabeth I promulgated the Act of Supremacy restoring royal headship."),
    ("Elizabeth_I", "PROMULGATES", "Act_of_Uniformity_1559", 
     "Elizabeth I promulgated the Act of Uniformity establishing the prayer book."),
    ("Elizabeth_I", "APPOINTS", "Matthew_Parker", 
     "Elizabeth I appointed Matthew Parker as Archbishop of Canterbury."),
    ("Elizabeth_I", "OPPOSES", "Recusant_Catholicism", 
     "Elizabeth I's regime prosecuted Catholic recusants."),
    
    # Reginald Pole
    ("Reginald_Pole", "ENDORSES", "Catholic_Restoration", 
     "Reginald Pole promoted the Marian Catholic restoration as papal legate."),
    ("Reginald_Pole", "WRITES", "Pole_Reconciliation_Decrees", 
     "Reginald Pole issued decrees facilitating reconciliation with Rome."),
    
    # Richard Hooker (add more)
    ("Richard_Hooker", "WRITES", "Of_the_Laws_of_Ecclesiastical_Polity", 
     "Richard Hooker authored Of the Laws of Ecclesiastical Polity defending the settlement."),
    ("Richard_Hooker", "DEFENDS", "Church_of_England", 
     "Richard Hooker provided theological defense of the Church of England's via media."),
    
    # William Tyndale (add more)
    ("William_Tyndale", "TRANSLATES", "Great_Bible_1539", 
     "William Tyndale's translation work formed the basis of the Great Bible."),
    ("William_Tyndale", "MARTYRED_FOR", "English_Bible_Translation", 
     "William Tyndale was executed in 1536 for his Bible translation work."),
    
    # Miles Coverdale
    ("Miles_Coverdale", "EDITS", "Great_Bible_1539", 
     "Miles Coverdale edited and supervised the Great Bible production."),
    ("Miles_Coverdale", "TRANSLATES", "Geneva_Bible_1560", 
     "Miles Coverdale contributed to the Geneva Bible translation effort."),
    
    # Matthew Parker
    ("Matthew_Parker", "SUPERVISES", "Bishops_Bible_1568", 
     "Matthew Parker supervised production of the Bishops' Bible."),
    ("Matthew_Parker", "ENFORCES", "Act_of_Uniformity_1559", 
     "Matthew Parker enforced the Elizabethan religious settlement."),
    
    # John Whitgift
    ("John_Whitgift", "OPPOSES", "Puritan_Movement", 
     "John Whitgift vigorously opposed Puritan challenges to the settlement."),
    ("John_Whitgift", "ENFORCES", "Thirty-Nine_Articles_1563", 
     "John Whitgift enforced subscription to the Thirty-Nine Articles."),
    
    # Edmund Grindal
    ("Edmund_Grindal", "TOLERATES", "Puritan_Movement", 
     "Edmund Grindal showed tolerance toward Puritan prophesyings."),
    ("Edmund_Grindal", "SUSPENDED_BY", "Elizabeth_I", 
     "Edmund Grindal was suspended by Elizabeth I for refusing to suppress prophesyings."),
]

# Marriage is modeled as an Event + participation edges (not P↔P).
# Format: (spouse_a_slug, spouse_b_slug, description)
MARRIAGES = [
    ("Henry_VIII", "Anne_Boleyn",
     "Henry VIII married Anne Boleyn after the annulment of his first marriage."),
]

TEXT_RELATIONSHIPS = [
    # Catholic_Restoration_Decrees (0 edges)
    ("Catholic_Restoration_Decrees", "ENABLES", "Catholic_Restoration", 
     "Catholic Restoration Decrees provided legal framework for Marian restoration."),
    ("Mary_I", "PROMULGATES", "Catholic_Restoration_Decrees", 
     "Mary I promulgated decrees restoring Catholic practices."),
    
    # More text connections
    ("Heresy_Acts", "FRAMES", "Heresy_Persecutions", 
     "Heresy Acts provided the legal basis for Marian persecutions."),
    ("Geneva_Bible_1560", "INFLUENCES", "Puritan_Movement", 
     "The Geneva Bible with its marginal notes influenced Puritan thought."),
    ("Rheims_New_Testament_1582", "COUNTERS", "Protestant_Doctrine_in_England", 
     "The Rheims New Testament provided a Catholic counter to Protestant translations."),
]

EVENT_RELATIONSHIPS = [
    # Articles_Promulgation (0 edges)
    ("Church_of_England", "ORGANIZES", "Articles_Promulgation", 
     "The Church of England organized promulgation of the Thirty-Nine Articles."),
    ("Articles_Promulgation", "ESTABLISHES", "Thirty-Nine_Articles_1563", 
     "The Articles Promulgation formally established the Thirty-Nine Articles."),
    
    # More event connections
    ("Execution_of_Mary_Queen_of_Scots_1587", "TRIGGERS", "Spanish_Armada_1588", 
     "Mary's execution contributed to Philip II's decision to launch the Armada."),
    ("Spanish_Armada_1588", "THREATENS", "Elizabeth_I", 
     "The Spanish Armada threatened Elizabeth I's Protestant regime."),
    ("Northern_Rebellion_1569", "SUPPORTS", "Mary_Queen_of_Scots", 
     "The Northern Rebellion sought to place Mary Queen of Scots on the English throne."),
    ("Pilgrimage_of_Grace_1536", "OPPOSES", "Dissolution_of_the_Monasteries", 
     "The Pilgrimage of Grace opposed Henry VIII's dissolution policies."),
    ("Western_Rebellion_1549", "OPPOSES", "Book_of_Common_Prayer_1549", 
     "The Western Rebellion opposed imposition of the English Prayer Book."),
    ("Ketts_Rebellion_1549", "COINCIDES_WITH", "Western_Rebellion_1549", 
     "Kett's Rebellion in Norfolk coincided with the Western Rebellion."),
    ("Wyatts_Rebellion_1554", "OPPOSES", "Mary_I", 
     "Wyatt's Rebellion opposed Mary I's Spanish marriage."),
    ("Vestiarian_Controversy_1566", "CHALLENGES", "Via_Media", 
     "The Vestiarian Controversy challenged the Elizabethan settlement's compromises."),
    ("Martin_Marprelate_Controversy_1588_1589", "ATTACKS", "Church_of_England", 
     "The Marprelate tracts satirically attacked the episcopal establishment."),
]

INSTITUTION_RELATIONSHIPS = [
    # Marian_Episcopate (0 edges)
    ("Marian_Episcopate", "ADMINISTERS", "Church_of_England", 
     "The Marian Episcopate administered the church during Mary I's reign."),
    ("Marian_Episcopate", "IMPLEMENTS", "Catholic_Restoration", 
     "The Marian Episcopate implemented Catholic restoration measures."),
    ("Mary_I", "APPOINTS", "Marian_Episcopate", 
     "Mary I appointed bishops sympathetic to Catholic restoration."),
    
    # University_of_Oxford (0 edges)
    ("University_of_Oxford", "EDUCATES", "Thomas_Cranmer", 
     "Thomas Cranmer was educated at Cambridge but Oxford was site of his martyrdom."),
    ("University_of_Oxford", "HOSTS", "Oxford_Martyrs_1555_1556", 
     "Oxford was the site of the martyrdoms of Cranmer, Latimer, and Ridley."),
    ("University_of_Oxford", "PRODUCES", "Richard_Hooker", 
     "Richard Hooker was educated at Oxford."),
    
    # University_of_Cambridge (0 edges)
    ("University_of_Cambridge", "EDUCATES", "Thomas_Cranmer", 
     "Thomas Cranmer was educated at Cambridge where reformation ideas spread early."),
    ("University_of_Cambridge", "PRODUCES", "William_Tyndale", 
     "William Tyndale studied at Cambridge."),
    ("University_of_Cambridge", "HOSTS", "Protestant_Doctrine_in_England", 
     "Cambridge was a center of early Protestant thought in England."),
    
    # More institutional connections
    ("English_Seminaries_Douai_Rheims", "PRODUCES", "Seminary_Priests_Mission_1580s", 
     "English seminaries abroad trained priests for the English mission."),
    ("Society_of_Jesus", "ORGANIZES", "Edmund_Campion", 
     "The Society of Jesus organized Edmund Campion's mission."),
    ("Court_of_High_Commission", "PROSECUTES", "Recusant_Catholicism", 
     "The Court of High Commission prosecuted Catholic recusants."),
    ("Star_Chamber", "PROSECUTES", "Martin_Marprelate_Controversy_1588_1589", 
     "The Star Chamber prosecuted those involved in the Marprelate tracts."),
]

MOVEMENT_RELATIONSHIPS = [
    # Iconoclasm_Waves (0 edges)
    ("Iconoclasm_Waves", "ACCOMPANIES", "Prayer_Book_Reform", 
     "Iconoclasm accompanied Edwardian liturgical reforms."),
    ("Lord_Protectorate", "PERMITS", "Iconoclasm_Waves", 
     "The Lord Protectorate permitted or encouraged iconoclastic actions."),
    ("Iconoclasm_Waves", "DESTROYS", "Church_of_England", 
     "Iconoclasm destroyed religious imagery in English churches."),
    
    # Papal_Supremacy (0 edges)
    ("Papal_Supremacy", "ASSERTED_BY", "Papacy", 
     "Papal supremacy was the foundational claim of Roman authority."),
    ("Royal_Supremacy", "REPLACES", "Papal_Supremacy", 
     "Royal supremacy replaced papal supremacy in England."),
    ("Papal_Supremacy", "DEFENDED_BY", "Thomas_More", 
     "Thomas More defended papal supremacy and was executed for it."),
    
    # Separatist_Movement (0 edges)
    ("Separatist_Movement", "EMERGES_FROM", "Puritan_Movement", 
     "Separatism emerged from more radical elements of the Puritan movement."),
    ("Separatist_Movement", "REJECTS", "Church_of_England", 
     "Separatists rejected the established Church of England entirely."),
    ("John_Whitgift", "OPPOSES", "Separatist_Movement", 
     "John Whitgift opposed separatist congregations."),
    
    # More movement connections
    ("Puritan_Movement", "CRITIQUES", "Book_of_Common_Prayer_1552", 
     "Puritans critiqued the Prayer Book as insufficiently reformed."),
    ("Presbyterian_Reform_in_England", "CHALLENGES", "Church_of_England", 
     "Presbyterian reformers challenged episcopal church polity."),
    ("Jesuit_Mission_in_England", "OPPOSES", "Via_Media", 
     "The Jesuit mission opposed the Elizabethan religious settlement."),
    ("Recusant_Catholicism", "SUPPORTED_BY", "Society_of_Jesus", 
     "Recusant Catholics were supported by Jesuit missionary activity."),
    ("Marian_Persecutions", "TARGETS", "Protestant_Doctrine_in_England", 
     "Marian persecutions targeted adherents of Protestant doctrine."),
]

PLACE_RELATIONSHIPS = [
    # Cambridge (0 edges)
    ("University_of_Cambridge", "LOCATED_IN", "Cambridge", 
     "Cambridge University was located in Cambridge."),
    ("Cambridge", "HOSTS", "Protestant_Doctrine_in_England", 
     "Cambridge was an early center of Protestant thought in England."),
]

# ============================================================================
# SCRIPT LOGIC
# ============================================================================

def load_json(path: Path) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path: Path, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_next_id(relationships: list) -> int:
    """Get the next available relationship ID."""
    if not relationships:
        return 1
    return max(r.get('id', 0) for r in relationships) + 1

def relationship_exists(relationships: list, start: str, rel_type: str, end: str) -> bool:
    """Check if relationship already exists."""
    for r in relationships:
        if (r.get('start_slug') == start and 
            r.get('type') == rel_type and 
            r.get('end_slug') == end):
            return True
    return False

def get_existing_nodes(nodes_path: Path) -> set:
    """Get set of existing node slugs."""
    data = load_json(nodes_path)
    return {n['slug'] for n in data.get('nodes', [])}

def get_next_node_slug_set(nodes_data: dict) -> set:
    return {n['slug'] for n in nodes_data.get('nodes', [])}

def get_or_create_marriage_event(nodes_data: dict, cluster: str, spouse_a: str, spouse_b: str, description: str):
    a, b = sorted([spouse_a, spouse_b])
    event_slug = f"Marriage_{a}_{b}"
    existing = get_next_node_slug_set(nodes_data)
    if event_slug in existing:
        return event_slug, False

    nodes_data.setdefault('nodes', []).append({
        "slug": event_slug,
        "name": f"Marriage: {a} × {b}",
        "label": "Event",
        "kind": "Marriage",
        "cluster": cluster,
        "status": "PROPOSED",
        "workflow_stage": "PROPOSED",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "created_by": "add_comprehensive_relationships.py",
        "description": description,
    })
    return event_slug, True

def add_relationships(cluster: str, dry_run: bool = False):
    """Add comprehensive relationships to the cluster."""
    base = Path('data')
    nodes_path = base / 'Nodes' / f'nodes.{cluster}.json'
    rels_path = base / 'Relationships' / f'relationships.{cluster}.json'
    
    if not nodes_path.exists():
        print(f"Error: Nodes file not found: {nodes_path}")
        return
    if not rels_path.exists():
        print(f"Error: Relationships file not found: {rels_path}")
        return
    
    # Load existing data
    nodes_data = load_json(nodes_path)
    existing_nodes = {n['slug'] for n in nodes_data.get('nodes', [])}
    rels_data = load_json(rels_path)
    relationships = rels_data.get('relationships', [])
    
    print(f"Existing nodes: {len(existing_nodes)}")
    print(f"Existing relationships: {len(relationships)}")
    
    # Combine all new relationships
    all_new = (PERSON_RELATIONSHIPS + TEXT_RELATIONSHIPS + EVENT_RELATIONSHIPS + 
               INSTITUTION_RELATIONSHIPS + MOVEMENT_RELATIONSHIPS + PLACE_RELATIONSHIPS)
    
    added = 0
    skipped_exists = 0
    skipped_missing = 0
    missing_nodes = set()
    
    next_id = get_next_id(relationships)
    
    for start, rel_type, end, desc in all_new:
        # Check if nodes exist
        if start not in existing_nodes:
            missing_nodes.add(start)
            skipped_missing += 1
            continue
        if end not in existing_nodes:
            missing_nodes.add(end)
            skipped_missing += 1
            continue
        
        # Check if relationship already exists
        if relationship_exists(relationships, start, rel_type, end):
            skipped_exists += 1
            continue
        
        # Add new relationship
        new_rel = {
            "id": next_id,
            "start_slug": start,
            "end_slug": end,
            "type": rel_type,
            "description": desc,
            "status": "PROPOSED",
            "evidence_url": None,
            "citation_style": "Chicago 17",
            "page_refs": None,
            "source_note": "curator:comprehensive_edges_2025",
            "inline_evidence": False
        }
        relationships.append(new_rel)
        next_id += 1
        added += 1
        print(f"  + ({start})-[{rel_type}]->({end})")

    # Add marriage-as-event modeling
    marriage_events_added = 0
    marriage_edges_added = 0
    for spouse_a, spouse_b, desc in MARRIAGES:
        if spouse_a not in existing_nodes:
            missing_nodes.add(spouse_a)
            continue
        if spouse_b not in existing_nodes:
            missing_nodes.add(spouse_b)
            continue

        marriage_slug, created = get_or_create_marriage_event(nodes_data, cluster, spouse_a, spouse_b, desc)
        if created:
            existing_nodes.add(marriage_slug)
            marriage_events_added += 1
            print(f"  + Node: {marriage_slug} (Event/Marriage)")

        for spouse in (spouse_a, spouse_b):
            if relationship_exists(relationships, spouse, "PARTICIPATES_IN", marriage_slug):
                continue
            new_rel = {
                "id": next_id,
                "start_slug": spouse,
                "end_slug": marriage_slug,
                "type": "PARTICIPATES_IN",
                "role": "spouse",
                "description": f"{spouse} participated as a spouse in {marriage_slug}.",
                "status": "PROPOSED",
                "evidence_url": None,
                "citation_style": "Chicago 17",
                "page_refs": None,
                "source_note": "curator:comprehensive_edges_2025",
                "inline_evidence": False,
            }
            relationships.append(new_rel)
            next_id += 1
            marriage_edges_added += 1
            print(f"  + ({spouse})-[PARTICIPATES_IN {{role:spouse}}]->({marriage_slug})")
    
    if missing_nodes:
        print(f"\nMissing nodes (relationships skipped): {sorted(missing_nodes)}")
    
    print(f"\n=== Summary ===")
    print(f"  Added: {added}")
    print(f"  Marriage event nodes added: {marriage_events_added}")
    print(f"  Marriage participation edges added: {marriage_edges_added}")
    print(f"  Skipped (already exists): {skipped_exists}")
    print(f"  Skipped (missing nodes): {skipped_missing}")
    print(f"  Total relationships now: {len(relationships)}")
    
    if not dry_run and (added > 0 or marriage_events_added > 0 or marriage_edges_added > 0):
        # Update metadata
        rels_data['relationships'] = relationships
        rels_data['_meta']['last_updated'] = datetime.now(timezone.utc).isoformat()
        rels_data['_meta']['comprehensive_edges_added'] = datetime.now(timezone.utc).isoformat()

        nodes_data.setdefault('_meta', {})['last_updated'] = datetime.now(timezone.utc).isoformat()

        save_json(nodes_path, nodes_data)
        save_json(rels_path, rels_data)
        print(f"\nSaved to {rels_path}")
    elif dry_run:
        print("\n[DRY RUN - no changes saved]")

def main():
    parser = argparse.ArgumentParser(description='Add comprehensive relationships to cluster')
    parser.add_argument('--cluster', required=True, help='Cluster name (e.g., English_Reformation)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without saving')
    args = parser.parse_args()
    
    add_relationships(args.cluster, args.dry_run)

if __name__ == '__main__':
    main()
