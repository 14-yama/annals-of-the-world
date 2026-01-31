#!/usr/bin/env python3
"""
Assign `kind` property to all Event nodes across seed files.

This script reads Event nodes from data/Nodes/*.json, assigns an appropriate
`kind` based on slug patterns and keywords, and writes back the updated files.

Usage:
    python scripts/admin/assign_event_kinds.py --dry-run   # Preview changes
    python scripts/admin/assign_event_kinds.py             # Apply changes
"""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Canonical event kinds (from docs/schema/event-kinds.md)
KINDS = [
    "Battle", "Council", "Controversy", "Covenant", "Debate", "Decree",
    "Execution", "Exile", "Founding", "Legislative", "Marriage", "Martyrdom",
    "Migration", "Mission", "Persecution", "Plot", "Publication", "Rebellion",
    "Reform", "Reign", "Rite", "Sacred", "Siege", "Trial", "War"
]

# Pattern-based classification rules (checked in order)
# Format: (regex_pattern, kind)
PATTERN_RULES: List[Tuple[str, str]] = [
    # Explicit markers in slug
    (r"^Marriage_", "Marriage"),
    (r"^Execution_|_Execution_|Execution$", "Execution"),
    (r"^Battle_|_Battle_|Battle$", "Battle"),
    (r"^Council_|_Council_|Council$", "Council"),
    (r"^Synod_|_Synod_|Synod$", "Council"),
    (r"^Diet_|_Diet_|Diet$", "Council"),
    (r"^Assembly_|_Assembly_|Assembly$", "Council"),
    (r"^Disputation_|_Disputation_|Disputation$", "Debate"),
    (r"^Colloquy_|_Colloquy_|Colloquy$", "Debate"),
    (r"^Debate_|_Debate_|Debate$", "Debate"),
    (r"^Edict_|_Edict_|Edict$", "Decree"),
    (r"^Decree_|_Decrees_|Decrees$", "Decree"),
    (r"^Mandate_|_Mandates_|Mandates$", "Decree"),
    (r"^Act_of_|_Act_|Act$", "Legislative"),
    (r"_Passage_|Passage$", "Legislative"),
    (r"^Trial_|_Trial_|Trial$", "Trial"),
    (r"^Siege_|_Siege_|Siege$", "Siege"),
    (r"^War_|_War_|War$|_Wars_", "War"),
    (r"^Rebellion_|_Rebellion_|Rebellion$", "Rebellion"),
    (r"^Revolt_|_Revolt_|Revolt$", "Rebellion"),
    (r"^Uprising_|_Uprising_|Uprising$", "Rebellion"),
    (r"^Persecution_|_Persecution_|Persecution$|_Persecutions_", "Persecution"),
    (r"^Pogrom_|_Pogroms_|Pogroms$", "Persecution"),
    (r"^Martyrdom_|_Martyrdom_|Martyrdom$|_Martyrs_|Martyrs$", "Martyrdom"),
    (r"^Plot_|_Plot_|Plot$", "Plot"),
    (r"^Conspiracy_|_Conspiracy_|Conspiracy$", "Plot"),
    (r"^Founding_|_Founding_|Founding$|Founded$", "Founding"),
    (r"^Establishment_|_Establishment_|Establishment$", "Founding"),
    (r"^Mission_|_Mission_|Mission$|_Missions_|Missions$", "Mission"),
    (r"^Exile_|_Exile_|Exile$|^Expulsion_|_Expulsion_|Expulsion$", "Exile"),
    (r"^Migration_|_Migration_|Migration$|_Migrations_", "Migration"),
    (r"^Covenant_|_Covenant_|Covenant$", "Covenant"),
    (r"^Reform_|_Reform_|Reform$|_Reforms_|Reforms$", "Reform"),
    (r"^Controversy_|_Controversy_|Controversy$", "Controversy"),
    (r"^Publication_|_Publication_|Publication$", "Publication"),
    (r"^Translation_|_Translation_|Translation$", "Publication"),
    (r"^Printing_|_Printing_|Printing$", "Publication"),
    (r"^Reign_|_Reign_|Reign$", "Reign"),
    (r"_Baptisms_|Baptisms$|^Abolition_of_the_Mass|_Mass_|_Rite_|_Rituals_|Rituals$", "Rite"),
]

# Explicit overrides for specific slugs
SLUG_OVERRIDES: Dict[str, str] = {
    # Sacred/miraculous events
    "Exodus": "Sacred",
    "Crucifixion": "Sacred",
    "Resurrection_Proclamations": "Sacred",
    "Pentecost": "Sacred",
    "Binding_of_Isaac": "Sacred",
    "Jacob_Bethel_Vision": "Sacred",
    "Wilderness_Wanderings": "Sacred",
    "Conquest_of_Canaan": "Sacred",
    "Joseph_in_Egypt": "Sacred",
    "Torah_Public_Reading": "Rite",
    "Temple_Dedication": "Rite",
    "Temple_Rituals": "Rite",
    "Sectarian_Practices": "Rite",
    
    # Councils/Synods
    "Brethren_Synods_15c": "Council",
    "Early_Regional_Synods": "Council",
    "Convocation_of_1563": "Council",
    "Reformation_Parliament_1560": "Council",
    "First_General_Assembly_1560": "Council",
    "Uppsala_Synod_1593": "Council",
    
    # Debates/Disputations
    "Zurich_Disputations_1523": "Debate",
    "Bern_Disputation_1528": "Debate",
    "Leipzig_Debate_1519": "Debate",
    "Marburg_Colloquy_1529": "Debate",
    
    # Wars/Battles
    "Hussite_Wars_1419_1434": "War",
    "Schmalkaldic_War_1546_1547": "War",
    "Counts_War_1534_1536": "War",
    "First_War_of_Religion_1562_1563": "War",
    "Kappel_Wars_1529_1531": "War",
    "Maccabean_Revolt": "Rebellion",
    "Great_Jewish_Revolt_66_70": "Rebellion",
    "Bar_Kokhba_Revolt": "Rebellion",
    "Pilgrimage_of_Grace_1536": "Rebellion",
    "Munster_Rebellion_1534_1535": "Rebellion",
    "Northern_Rebellion_1569": "Rebellion",
    "Western_Rebellion_1549": "Rebellion",
    "Ketts_Rebellion_1549": "Rebellion",
    "Wyatts_Rebellion_1554": "Rebellion",
    "Congregation_Risings_1559": "Rebellion",
    "Iconoclastic_Fury_1566": "Rebellion",
    "Hedge_Preachings_1560s": "Rebellion",
    
    # Sieges
    "Assyrian_Siege_of_Jerusalem_701_BCE": "Siege",
    "Babylonian_Siege_597_BCE": "Siege",
    "Siege_of_St_Andrews_Castle_1546_1547": "Siege",
    "Fall_of_Antwerp_1585": "Siege",
    "Fall_of_Samaria_722_BCE": "Siege",
    
    # Persecutions/Massacres
    "Decian_Persecution_250": "Persecution",
    "Diocletianic_Persecution_303": "Persecution",
    "Neronian_Persecution_64": "Persecution",
    "Heresy_Persecutions": "Persecution",
    "Black_Death_Persecutions_1348_1351": "Persecution",
    "St_Bartholomews_Day_Massacre_1572": "Persecution",
    "Granada_Massacre_1066": "Persecution",
    "Russian_Pogroms_1881_1884": "Persecution",
    "Shoah": "Persecution",
    "Spanish_Inquisition_1478": "Persecution",
    "First_Crusade_1096": "Persecution",
    
    # Martyrdoms
    "Oxford_Martyrs_1555_1556": "Martyrdom",
    "Ignatian_Martyrdom": "Martyrdom",
    "Martyrdoms_in_Lyons_177": "Martyrdom",
    "Burning_of_William_Tyndale_1536": "Martyrdom",
    "Wishart_Execution_1546": "Martyrdom",
    "Manz_Execution_1527": "Martyrdom",
    
    # Executions (state killings, not martyrdom)
    "Hus_Execution_1415": "Execution",
    "Servetus_Execution_1553": "Execution",
    "Oldenbarnevelt_Execution_1619": "Execution",
    
    # Exiles/Expulsions
    "Babylonian_Exile": "Exile",
    "Expulsion_from_Spain_1492": "Exile",
    "Expulsion_from_Portugal_1497": "Exile",
    "Expulsion_from_England_1290": "Exile",
    "Exile_of_Socinians_1658": "Exile",
    "Almohad_Pressures_and_Migration": "Migration",
    "Hutterite_Migrations_16c": "Migration",
    "Mennonite_Organizing_1550s_1570s": "Migration",
    
    # Founding/Establishment
    "Founding_of_Society_of_Jesus_1540": "Founding",
    "Founding_of_Unitas_Fratrum_1457": "Founding",
    "Founding_of_Reformed_Congregations": "Founding",
    "Academy_Founding_1559": "Founding",
    "Rakow_Academy_Founding_1602": "Founding",
    "State_of_Israel_Founding": "Founding",
    "Formation_of_French_Consistories": "Founding",
    "Building_of_First_Temple": "Founding",
    "Second_Temple_Dedication_515_BCE": "Founding",
    "Herodian_Temple_Renovation": "Founding",
    
    # Missions
    "Jesuit_Mission_1580s": "Mission",
    "Seminary_Priests_Mission_1580s": "Mission",
    "Pauline_Mission_Journeys": "Mission",
    "Jesuit_Missions_India_China": "Mission",
    "Jesuit_Expansion": "Mission",
    
    # Publications/Translations
    "Kralice_Bible_Publication_1579_1593": "Publication",
    "Wartburg_Translation_1521_1522": "Publication",
    "Printing_Revolution": "Publication",
    "Parish_Bible_Installations": "Publication",
    "Judeo_Arabic_Bible_Translation_Phase": "Publication",
    "Abbasid_Translation_Movement": "Publication",
    "Toledo_Translation_Phase": "Publication",
    "Cairo_Geniza_Document_Accumulation": "Publication",
    
    # Decrees/Edicts
    "Edict_of_Milan_313": "Decree",
    "Edict_of_Toleration_311": "Decree",
    "Cyrus_Edict": "Decree",
    "Antiochus_IV_Decrees": "Decree",
    "Hadrianic_Decrees": "Decree",
    "Zurich_Edicts_Against_Anabaptists_1526": "Decree",
    "Augsburg_Mandates_1528": "Decree",
    "Letter_of_Majesty_1609": "Decree",
    "Regnans_in_Excelsis_1570": "Decree",
    "Balfour_Declaration_1917": "Decree",
    "Nuremberg_Laws_1935": "Decree",
    "Law_of_Return_1950": "Decree",
    "UN_Partition_Plan_1947": "Decree",
    
    # Legislative
    "Act_of_Supremacy_1534": "Legislative",
    "Act_of_Succession_1534": "Legislative",
    "Act_of_Supremacy_Passage": "Legislative",
    "Settlement_Passage": "Legislative",
    "Black_Acts_Passage_1584": "Legislative",
    "Golden_Act_Passage_1592": "Legislative",
    "Edict_of_Nantes_Passage_1598": "Legislative",
    "Edict_of_Saint-Germain_Passage_1562": "Legislative",
    "Union_of_Brest_Passage_1596": "Legislative",
    "Union_of_Utrecht_1579": "Legislative",
    "Compacts_of_Basel_1436": "Legislative",
    "Submission_of_the_Clergy_1532": "Legislative",
    "Recusancy_Fines_Regime": "Legislative",
    "Dissolution_of_the_Monasteries": "Legislative",
    "Standardization_of_Roman_Rite_1570": "Legislative",
    "Doctrinal_Articles_Promulgation": "Legislative",
    "Articles_Promulgation": "Legislative",
    "Ratification_of_Scots_Confession_1560": "Legislative",
    "Emancipation": "Legislative",
    
    # Trials
    "Trial_of_Mary_Queen_of_Scots_1586": "Trial",
    "Eichmann_Trial_1961": "Trial",
    "Annulment_Proceedings": "Trial",
    
    # Plots
    "Babington_Plot_1586": "Plot",
    "Ridolfi_Plot_1571": "Plot",
    "Throckmorton_Plot_1583": "Plot",
    "Ruthven_Raid_1582": "Plot",
    
    # Controversies
    "Arminius_Controversy_1603_1609": "Controversy",
    "Vestiarian_Controversy_1566": "Controversy",
    "Martin_Marprelate_Controversy_1588_1589": "Controversy",
    "Prophesyings_Controversy_1576": "Controversy",
    "Rabbanite_Karaite_Polemics_Baghdad": "Controversy",
    
    # Reform programs
    "Basel_Reform_1529": "Reform",
    "Hezekiah_Reforms": "Reform",
    "Josiah_Reforms": "Reform",
    "Yavneh_Reform": "Reform",
    "Post_70_Reconfiguration": "Reform",
    "Prayer_Book_Reform": "Reform",
    "Early_Curial_Committees_for_Reform": "Reform",
    "Visitations_and_Implementations_1540s": "Reform",
    "Reduction_Policies_1540s": "Reform",
    "Seminaries_Proliferation": "Reform",
    "Jerusalem_Rebuilding": "Reform",
    "Return_to_Zion": "Reform",
    "Canon_and_Masorah_Development": "Reform",
    "Mishnah_Codification": "Reform",
    "Talmud_Redactions": "Reform",
    "Legal_Decisions": "Reform",
    "Geonic_Responsa_Network_Expansion": "Reform",
    
    # Reigns
    "Lady_Jane_Grey_Reign_1553": "Reign",
    "Mary_Queen_of_Scots_Deposition_1567": "Reign",
    "Hasmonean_Expansion": "Reign",
    "Division_of_the_Kingdom": "Reign",
    
    # Conquests (as War or Sacred depending on context)
    "Assyrian_Conquest_of_Israel": "War",
    "Roman_Conquest": "War",
    "Pompey_Annexation_63_BCE": "War",
    "Reconquista_of_Toledo_1085": "War",
    "Six_Day_War_1967": "War",
    "Yom_Kippur_War_1973": "War",
    
    # Temple events
    "Temple_Destruction_70_CE": "War",
    "Destruction_of_First_Temple_586_BCE": "War",
    "Paris_Talmud_Burning_1242": "Persecution",
    
    # Covenants
    "Abrahamic_Covenant": "Covenant",
    "Sinai_Covenant": "Covenant",
    
    # Misc assignments
    "Break_with_Rome": "Legislative",
    "Reconciliation_with_Rome": "Legislative",
    "Fall_of_Wolsey_1529": "Reign",
    "Calvin_Return_to_Geneva_1541": "Reform",
    "First_Adult_Baptisms_Zurich_1525": "Rite",
    "Abolition_of_the_Mass_Zurich_1525": "Reform",
    "Posting_of_Theses_1517": "Reform",
    "Affair_of_the_Placards_1534": "Controversy",
    "Affair_of_the_Sausages_1522": "Controversy",
    "Evangelical_Preachings_Meaux": "Reform",
    "Pliny_Trajan_Correspondence": "Decree",
    "Spanish_Armada_1588": "War",
    "Rakow_Academy_Closure_1638": "Legislative",
    "Taifa_Fragmentation": "Reign",
    "Court_Patronage_Phases": "Reign",
    "Ayyubid_Patronage_Phases": "Reign",
    "Royal_Toleration_Phases": "Legislative",
    "Maimonidean_Dissemination_Phases": "Publication",
    "Dreyfus_Affair_1894_1906": "Trial",
    "Diet_of_Vaesteras_1527": "Council",
    "Establishment_of_Lutheranism_Denmark_1536": "Reform",
    "Princes_Protest_of_Speyer_1529": "Legislative",
}


def classify_event(slug: str) -> Optional[str]:
    """Determine the kind for an event based on slug."""
    # Check explicit overrides first
    if slug in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[slug]
    
    # Check pattern rules
    for pattern, kind in PATTERN_RULES:
        if re.search(pattern, slug, re.IGNORECASE):
            return kind
    
    return None


def process_nodes_file(filepath: Path, dry_run: bool) -> Dict[str, Any]:
    """Process a single nodes file and assign kinds to Events."""
    stats = {
        "file": filepath.name,
        "events_total": 0,
        "events_updated": 0,
        "events_already_had_kind": 0,
        "events_unclassified": [],
    }
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        return stats
    
    nodes = data.get("nodes", [])
    if not isinstance(nodes, list):
        return stats
    
    modified = False
    for node in nodes:
        if not isinstance(node, dict):
            continue
        if node.get("label") != "Event":
            continue
        
        stats["events_total"] += 1
        slug = node.get("slug", "")
        
        if node.get("kind"):
            stats["events_already_had_kind"] += 1
            continue
        
        kind = classify_event(slug)
        if kind:
            node["kind"] = kind
            stats["events_updated"] += 1
            modified = True
        else:
            stats["events_unclassified"].append(slug)
    
    if modified and not dry_run:
        data.setdefault("_meta", {})["event_kinds_assigned_at"] = datetime.now(timezone.utc).isoformat()
        data["_meta"]["event_kinds_script"] = "scripts/admin/assign_event_kinds.py"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    return stats


def main():
    parser = argparse.ArgumentParser(description="Assign kind to Event nodes")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()
    
    nodes_dir = Path(__file__).resolve().parent.parent.parent / "data" / "Nodes"
    
    all_stats = []
    all_unclassified = []
    
    for filepath in sorted(nodes_dir.glob("nodes.*.json")):
        stats = process_nodes_file(filepath, args.dry_run)
        all_stats.append(stats)
        all_unclassified.extend(stats["events_unclassified"])
        
        if stats["events_total"] > 0:
            print(f"{stats['file']}: {stats['events_updated']} updated, "
                  f"{stats['events_already_had_kind']} already had kind, "
                  f"{len(stats['events_unclassified'])} unclassified")
    
    total_events = sum(s["events_total"] for s in all_stats)
    total_updated = sum(s["events_updated"] for s in all_stats)
    total_had_kind = sum(s["events_already_had_kind"] for s in all_stats)
    
    print(f"\n=== Summary ===")
    print(f"Total Events: {total_events}")
    print(f"Updated: {total_updated}")
    print(f"Already had kind: {total_had_kind}")
    print(f"Unclassified: {len(all_unclassified)}")
    
    if all_unclassified:
        print(f"\nUnclassified events (add to SLUG_OVERRIDES):")
        for slug in sorted(set(all_unclassified)):
            print(f"  {slug}")
    
    if args.dry_run:
        print("\n[DRY RUN - no files modified]")


if __name__ == "__main__":
    main()
