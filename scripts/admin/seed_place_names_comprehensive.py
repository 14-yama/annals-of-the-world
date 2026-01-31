#!/usr/bin/env python3
"""
Comprehensive PlaceName examples covering all naming change categories.

Categories seeded:
1. Conquest — Jebus → Jerusalem, Constantinople → Istanbul
2. Regime change — St. Petersburg → Petrograd → Leningrad → St. Petersburg
3. Decolonization — Bombay → Mumbai, Ceylon → Sri Lanka
4. Exonyms vs endonyms — Deutschland vs Germany
5. Script variants — 北京 vs Beijing vs Peking
6. Extinct places — Babylon, Troy, Carthage (linked to modern containers)
7. Border changes — Alsace (France ↔ Germany), Lviv (multiple countries)
8. City mergers — Greater London, New York City consolidation

Usage:
    python scripts/admin/seed_place_names_comprehensive.py           # dry-run
    python scripts/admin/seed_place_names_comprehensive.py --run     # execute
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from db import get_neo4j_driver

# ============================================================================
# All Cypher statements (one statement per list item)
# ============================================================================

STATEMENTS = [
    # ========================================================================
    # 1. CONQUEST: Jebus → Jerusalem
    # ========================================================================
    """MERGE (p:Place {slug:"jerusalem"})
       SET p.name="Jerusalem", p.kind="city", p.wikidata_id="Q1218",
           p.lat=31.7683, p.lon=35.2137""",

    """MERGE (n:PlaceName {slug:"jebus"})
       SET n.name="Jebus", n.lang="und", n.script="Latn",
           n.startYear=-3000, n.endYear=-1000,
           n.source_note="Pre-Davidic Canaanite name" """,

    """MERGE (n:PlaceName {slug:"jerusalem-hebrew"})
       SET n.name="Jerusalem", n.lang="he", n.script="Latn",
           n.startYear=-1000, n.endYear=135,
           n.source_note="Davidic to Hadrian period" """,

    """MERGE (n:PlaceName {slug:"aelia-capitolina"})
       SET n.name="Aelia Capitolina", n.lang="la", n.script="Latn",
           n.startYear=135, n.endYear=638,
           n.source_note="Roman renaming by Hadrian" """,

    """MERGE (n:PlaceName {slug:"jerusalem-modern"})
       SET n.name="Jerusalem", n.lang="en", n.script="Latn",
           n.startYear=638, n.is_primary=true,
           n.source_note="Post-Islamic conquest to present" """,

    # Link names to place
    """MATCH (p:Place {slug:"jerusalem"}), (n:PlaceName {slug:"jebus"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"jerusalem"}), (n:PlaceName {slug:"jerusalem-hebrew"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"jerusalem"}), (n:PlaceName {slug:"aelia-capitolina"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"jerusalem"}), (n:PlaceName {slug:"jerusalem-modern"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.is_primary=true""",

    # Events and participants for Jerusalem
    """MERGE (d:Person {slug:"david"})
       SET d.name="King David", d.description="Israelite king who captured Jebus" """,

    """MERGE (h:Person {slug:"hadrian"})
       SET h.name="Emperor Hadrian", h.description="Roman emperor who renamed Jerusalem" """,

    """MERGE (k:Institution {slug:"kingdom-of-israel"})
       SET k.name="Kingdom of Israel" """,

    """MERGE (re:Institution {slug:"roman-empire"})
       SET re.name="Roman Empire" """,

    """MERGE (e:Event {slug:"david-captures-jebus"})
       SET e.name="David captures Jebus", e.kind="Conquest", e.startYear=-1000,
           e.description="King David conquers Jebusite city, renames it Jerusalem" """,

    """MERGE (e:Event {slug:"hadrian-renames-jerusalem"})
       SET e.name="Hadrian renames Jerusalem to Aelia Capitolina", e.kind="Decree", e.startYear=135,
           e.description="Roman emperor Hadrian renames the city after crushing Bar Kokhba revolt" """,

    """MATCH (e:Event {slug:"david-captures-jebus"}), (p:Place {slug:"jerusalem"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    """MATCH (e:Event {slug:"hadrian-renames-jerusalem"}), (p:Place {slug:"jerusalem"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    """MATCH (d:Person {slug:"david"}), (e:Event {slug:"david-captures-jebus"})
       MERGE (d)-[:PARTICIPATES_IN {role:"conqueror"}]->(e)""",

    """MATCH (h:Person {slug:"hadrian"}), (e:Event {slug:"hadrian-renames-jerusalem"})
       MERGE (h)-[:PARTICIPATES_IN {role:"emperor"}]->(e)""",

    """MATCH (d:Person {slug:"david"}), (k:Institution {slug:"kingdom-of-israel"})
       MERGE (d)-[:LEADS]->(k)""",

    """MATCH (h:Person {slug:"hadrian"}), (re:Institution {slug:"roman-empire"})
       MERGE (h)-[:LEADS]->(re)""",

    # ========================================================================
    # 1b. CONQUEST: Constantinople → Istanbul
    # ========================================================================
    """MERGE (p:Place {slug:"istanbul"})
       SET p.name="Istanbul", p.kind="city", p.wikidata_id="Q406",
           p.lat=41.0082, p.lon=28.9784""",

    """MERGE (n:PlaceName {slug:"byzantium"})
       SET n.name="Byzantium", n.lang="grc", n.script="Latn",
           n.startYear=-700, n.endYear=330,
           n.source_note="Ancient Greek colony" """,

    """MERGE (n:PlaceName {slug:"constantinople"})
       SET n.name="Constantinople", n.lang="la", n.script="Latn",
           n.startYear=330, n.endYear=1930,
           n.source_note="Constantine's refounding" """,

    """MERGE (n:PlaceName {slug:"istanbul-name"})
       SET n.name="Istanbul", n.lang="tr", n.script="Latn",
           n.startYear=1930, n.is_primary=true,
           n.source_note="Official Turkish name from 1930" """,

    """MATCH (p:Place {slug:"istanbul"}), (n:PlaceName {slug:"byzantium"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"istanbul"}), (n:PlaceName {slug:"constantinople"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"istanbul"}), (n:PlaceName {slug:"istanbul-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.is_primary=true""",

    """MERGE (c:Person {slug:"constantine-i"})
       SET c.name="Constantine I", c.description="Roman emperor who refounded Byzantium as Constantinople" """,

    """MERGE (e:Event {slug:"constantine-refounds-byzantium"})
       SET e.name="Constantine refounds Byzantium as Constantinople", e.kind="Founding", e.startYear=330""",

    """MATCH (e:Event {slug:"constantine-refounds-byzantium"}), (p:Place {slug:"istanbul"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    """MATCH (c:Person {slug:"constantine-i"}), (e:Event {slug:"constantine-refounds-byzantium"})
       MERGE (c)-[:PARTICIPATES_IN {role:"founder"}]->(e)""",

    # ========================================================================
    # 2. REGIME CHANGE: St. Petersburg → Petrograd → Leningrad → St. Petersburg
    # ========================================================================
    """MERGE (p:Place {slug:"saint-petersburg"})
       SET p.name="Saint Petersburg", p.kind="city", p.wikidata_id="Q656",
           p.lat=59.9343, p.lon=30.3351""",

    """MERGE (n:PlaceName {slug:"saint-petersburg-1703"})
       SET n.name="Saint Petersburg", n.lang="ru", n.script="Latn",
           n.startYear=1703, n.endYear=1914,
           n.source_note="Founded by Peter the Great" """,

    """MERGE (n:PlaceName {slug:"petrograd"})
       SET n.name="Petrograd", n.lang="ru", n.script="Latn",
           n.startYear=1914, n.endYear=1924,
           n.source_note="WWI anti-German sentiment" """,

    """MERGE (n:PlaceName {slug:"leningrad"})
       SET n.name="Leningrad", n.lang="ru", n.script="Latn",
           n.startYear=1924, n.endYear=1991,
           n.source_note="Soviet era, named after Lenin" """,

    """MERGE (n:PlaceName {slug:"saint-petersburg-1991"})
       SET n.name="Saint Petersburg", n.lang="ru", n.script="Latn",
           n.startYear=1991, n.is_primary=true,
           n.source_note="Post-Soviet restoration" """,

    """MATCH (p:Place {slug:"saint-petersburg"}), (n:PlaceName {slug:"saint-petersburg-1703"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"saint-petersburg"}), (n:PlaceName {slug:"petrograd"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"saint-petersburg"}), (n:PlaceName {slug:"leningrad"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"saint-petersburg"}), (n:PlaceName {slug:"saint-petersburg-1991"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.is_primary=true""",

    """MERGE (e:Event {slug:"siege-of-leningrad"})
       SET e.name="Siege of Leningrad", e.kind="War", e.startYear=1941, e.endYear=1944,
           e.description="Nazi siege during WWII, one of history's most destructive" """,

    """MATCH (e:Event {slug:"siege-of-leningrad"}), (p:Place {slug:"saint-petersburg"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    # ========================================================================
    # 3. DECOLONIZATION: Bombay → Mumbai
    # ========================================================================
    """MERGE (p:Place {slug:"mumbai"})
       SET p.name="Mumbai", p.kind="city", p.wikidata_id="Q1156",
           p.lat=19.0760, p.lon=72.8777""",

    """MERGE (n:PlaceName {slug:"bombay"})
       SET n.name="Bombay", n.lang="en", n.script="Latn",
           n.startYear=1661, n.endYear=1995, n.is_endonym=false,
           n.source_note="British colonial name" """,

    """MERGE (n:PlaceName {slug:"mumbai-name"})
       SET n.name="Mumbai", n.lang="mr", n.script="Latn",
           n.startYear=1995, n.is_primary=true, n.is_endonym=true,
           n.source_note="Marathi restoration" """,

    """MATCH (p:Place {slug:"mumbai"}), (n:PlaceName {slug:"bombay"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"mumbai"}), (n:PlaceName {slug:"mumbai-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.is_primary=true""",

    """MERGE (e:Event {slug:"quit-india-movement-bombay"})
       SET e.name="Quit India Movement launched in Bombay", e.kind="Protest", e.startYear=1942,
           e.description="Gandhi's call for British withdrawal" """,

    """MATCH (e:Event {slug:"quit-india-movement-bombay"}), (p:Place {slug:"mumbai"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    # 3b. Ceylon → Sri Lanka
    """MERGE (p:Place {slug:"sri-lanka"})
       ON CREATE SET p.name="Sri Lanka", p.kind="country", p.wikidata_id="Q854" """,

    """MERGE (n:PlaceName {slug:"ceylon"})
       SET n.name="Ceylon", n.lang="en", n.script="Latn",
           n.startYear=1505, n.endYear=1972, n.is_endonym=false,
           n.source_note="Colonial name (Portuguese, Dutch, British)" """,

    """MERGE (n:PlaceName {slug:"sri-lanka-name"})
       SET n.name="Sri Lanka", n.lang="si", n.script="Latn",
           n.startYear=1972, n.is_primary=true, n.is_endonym=true,
           n.source_note="Independence naming" """,

    """MATCH (p:Place {slug:"sri-lanka"}), (n:PlaceName {slug:"ceylon"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    """MATCH (p:Place {slug:"sri-lanka"}), (n:PlaceName {slug:"sri-lanka-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.is_primary=true""",

    # ========================================================================
    # 4. EXONYMS VS ENDONYMS: Deutschland vs Germany
    # ========================================================================
    """MERGE (p:Place {slug:"germany"})
       ON CREATE SET p.name="Germany", p.kind="country", p.wikidata_id="Q183" """,

    """MERGE (n:PlaceName {slug:"deutschland"})
       SET n.name="Deutschland", n.lang="de", n.script="Latn",
           n.is_endonym=true, n.is_primary=false,
           n.source_note="German endonym" """,

    """MERGE (n:PlaceName {slug:"germany-exonym"})
       SET n.name="Germany", n.lang="en", n.script="Latn",
           n.is_endonym=false, n.is_primary=true,
           n.source_note="English exonym" """,

    """MERGE (n:PlaceName {slug:"allemagne"})
       SET n.name="Allemagne", n.lang="fr", n.script="Latn",
           n.is_endonym=false,
           n.source_note="French exonym" """,

    """MERGE (n:PlaceName {slug:"alemania"})
       SET n.name="Alemania", n.lang="es", n.script="Latn",
           n.is_endonym=false,
           n.source_note="Spanish exonym" """,

    """MATCH (p:Place {slug:"germany"}), (n:PlaceName {slug:"deutschland"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"germany"}), (n:PlaceName {slug:"germany-exonym"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.is_primary=true""",

    """MATCH (p:Place {slug:"germany"}), (n:PlaceName {slug:"allemagne"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"germany"}), (n:PlaceName {slug:"alemania"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    # ========================================================================
    # 5. SCRIPT VARIANTS: 北京 vs Beijing vs Peking
    # ========================================================================
    """MERGE (p:Place {slug:"beijing"})
       SET p.name="Beijing", p.kind="city", p.wikidata_id="Q956",
           p.lat=39.9042, p.lon=116.4074""",

    """MERGE (n:PlaceName {slug:"beijing-hanzi"})
       SET n.name="北京", n.lang="zh", n.script="Hani",
           n.is_endonym=true, n.is_primary=false,
           n.source_note="Chinese characters" """,

    """MERGE (n:PlaceName {slug:"beijing-pinyin"})
       SET n.name="Beijing", n.lang="zh", n.script="Latn",
           n.is_endonym=true, n.is_primary=true,
           n.source_note="Pinyin romanization (current standard)" """,

    """MERGE (n:PlaceName {slug:"peking"})
       SET n.name="Peking", n.lang="en", n.script="Latn",
           n.is_endonym=false,
           n.source_note="Postal romanization (historical)" """,

    """MERGE (n:PlaceName {slug:"peiping"})
       SET n.name="Peiping", n.lang="zh", n.script="Latn",
           n.startYear=1928, n.endYear=1949,
           n.source_note="Northern Peace - name during Nanjing capital period" """,

    """MATCH (p:Place {slug:"beijing"}), (n:PlaceName {slug:"beijing-hanzi"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"beijing"}), (n:PlaceName {slug:"beijing-pinyin"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.is_primary=true""",

    """MATCH (p:Place {slug:"beijing"}), (n:PlaceName {slug:"peking"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"beijing"}), (n:PlaceName {slug:"peiping"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    # ========================================================================
    # 6. EXTINCT PLACES: Babylon, Troy, Carthage (linked to modern containers)
    # ========================================================================
    """MERGE (iraq:Place {slug:"iraq"})
       ON CREATE SET iraq.name="Iraq", iraq.kind="country", iraq.wikidata_id="Q796" """,

    """MERGE (p:Place {slug:"babylon"})
       SET p.name="Babylon", p.kind="site", p.status="EXTINCT",
           p.wikidata_id="Q5684", p.pleiades_id="893951",
           p.lat=32.5355, p.lon=44.4275,
           p.description="Ancient Mesopotamian city, now ruins near Hillah" """,

    """MATCH (p:Place {slug:"babylon"}), (c:Place {slug:"iraq"})
       MERGE (p)-[:LOCATED_IN]->(c)""",

    """MERGE (n:PlaceName {slug:"babylon-name"})
       SET n.name="Babylon", n.lang="akk", n.script="Latn",
           n.startYear=-2300, n.endYear=650,
           n.source_note="Akkadian Bābilim, Gate of God" """,

    """MATCH (p:Place {slug:"babylon"}), (n:PlaceName {slug:"babylon-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.startYear=n.startYear, r.endYear=n.endYear""",

    # Troy - use existing country if already seeded by geo registry
    """MERGE (turkiye:Place {slug:"türkiye"})
       ON CREATE SET turkiye.name="Türkiye", turkiye.kind="country", turkiye.wikidata_id="Q43" """,

    """MERGE (p:Place {slug:"troy"})
       SET p.name="Troy", p.kind="site", p.status="EXTINCT",
           p.wikidata_id="Q18845", p.pleiades_id="550595",
           p.lat=39.9575, p.lon=26.2389,
           p.description="Ancient city, site of Trojan War, now Hisarlik" """,

    """MATCH (p:Place {slug:"troy"}), (c:Place {slug:"türkiye"})
       MERGE (p)-[:LOCATED_IN]->(c)""",

    """MERGE (n:PlaceName {slug:"ilion"})
       SET n.name="Ilion", n.lang="grc", n.script="Latn",
           n.source_note="Greek name (Ἴλιον)" """,

    """MERGE (n:PlaceName {slug:"troy-name"})
       SET n.name="Troy", n.lang="en", n.script="Latn", n.is_primary=true,
           n.source_note="English name from Latin Troia" """,

    """MATCH (p:Place {slug:"troy"}), (n:PlaceName {slug:"ilion"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"troy"}), (n:PlaceName {slug:"troy-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.is_primary=true""",

    # Carthage
    """MERGE (tunisia:Place {slug:"tunisia"})
       ON CREATE SET tunisia.name="Tunisia", tunisia.kind="country", tunisia.wikidata_id="Q948" """,

    """MERGE (p:Place {slug:"carthage"})
       SET p.name="Carthage", p.kind="site", p.status="EXTINCT",
           p.wikidata_id="Q6386", p.pleiades_id="314921",
           p.lat=36.8528, p.lon=10.3233,
           p.description="Ancient Phoenician city-state, destroyed by Rome 146 BCE" """,

    """MATCH (p:Place {slug:"carthage"}), (c:Place {slug:"tunisia"})
       MERGE (p)-[:LOCATED_IN]->(c)""",

    """MERGE (n:PlaceName {slug:"qart-hadasht"})
       SET n.name="Qart Ḥadašt", n.lang="phn", n.script="Latn",
           n.is_endonym=true,
           n.source_note="Phoenician: New City" """,

    """MERGE (n:PlaceName {slug:"carthage-name"})
       SET n.name="Carthage", n.lang="en", n.script="Latn", n.is_primary=true,
           n.source_note="From Latin Carthago" """,

    """MATCH (p:Place {slug:"carthage"}), (n:PlaceName {slug:"qart-hadasht"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"carthage"}), (n:PlaceName {slug:"carthage-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.is_primary=true""",

    """MERGE (e:Event {slug:"destruction-of-carthage"})
       SET e.name="Destruction of Carthage", e.kind="War", e.startYear=-146,
           e.description="Third Punic War ends with Rome destroying Carthage" """,

    """MATCH (e:Event {slug:"destruction-of-carthage"}), (p:Place {slug:"carthage"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    # ========================================================================
    # 7. BORDER CHANGES: Alsace, Lviv
    # ========================================================================
    """MERGE (p:Place {slug:"alsace"})
       SET p.name="Alsace", p.kind="region", p.wikidata_id="Q1142" """,

    """MERGE (fr:Polity {slug:"france"})
       SET fr.name="France" """,

    """MERGE (ge:Polity {slug:"german-empire"})
       SET ge.name="German Empire" """,

    """MERGE (nz:Polity {slug:"nazi-germany"})
       SET nz.name="Nazi Germany" """,

    """MATCH (p:Place {slug:"alsace"}), (pol:Polity {slug:"france"})
       MERGE (p)-[r1:GOVERNED_BY {startYear:1648, endYear:1871}]->(pol)""",

    """MATCH (p:Place {slug:"alsace"}), (pol:Polity {slug:"german-empire"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1871, endYear:1918}]->(pol)""",

    """MATCH (p:Place {slug:"alsace"}), (pol:Polity {slug:"france"})
       MERGE (p)-[r2:GOVERNED_BY {startYear:1918, endYear:1940}]->(pol)""",

    """MATCH (p:Place {slug:"alsace"}), (pol:Polity {slug:"nazi-germany"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1940, endYear:1944}]->(pol)""",

    """MATCH (p:Place {slug:"alsace"}), (pol:Polity {slug:"france"})
       MERGE (p)-[r3:GOVERNED_BY {startYear:1944}]->(pol)""",

    # Lviv
    """MERGE (p:Place {slug:"lviv"})
       SET p.name="Lviv", p.kind="city", p.wikidata_id="Q36036",
           p.lat=49.8397, p.lon=24.0297""",

    """MERGE (n:PlaceName {slug:"lwow"})
       SET n.name="Lwów", n.lang="pl", n.script="Latn",
           n.source_note="Polish name" """,

    """MERGE (n:PlaceName {slug:"lemberg"})
       SET n.name="Lemberg", n.lang="de", n.script="Latn",
           n.source_note="German/Austrian name" """,

    """MERGE (n:PlaceName {slug:"lvov"})
       SET n.name="Lvov", n.lang="ru", n.script="Latn",
           n.source_note="Russian name" """,

    """MERGE (n:PlaceName {slug:"lviv-name"})
       SET n.name="Lviv", n.lang="uk", n.script="Latn",
           n.is_endonym=true, n.is_primary=true,
           n.source_note="Ukrainian name (current)" """,

    """MATCH (p:Place {slug:"lviv"}), (n:PlaceName {slug:"lwow"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"lviv"}), (n:PlaceName {slug:"lemberg"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"lviv"}), (n:PlaceName {slug:"lvov"})
       MERGE (p)-[r:HAS_NAME]->(n)""",

    """MATCH (p:Place {slug:"lviv"}), (n:PlaceName {slug:"lviv-name"})
       MERGE (p)-[r:HAS_NAME]->(n)
       SET r.is_primary=true""",

    """MERGE (hab:Polity {slug:"habsburg-empire"})
       SET hab.name="Habsburg Empire" """,

    """MERGE (pol:Polity {slug:"poland-second-republic"})
       SET pol.name="Second Polish Republic" """,

    """MERGE (ussr:Polity {slug:"soviet-union"})
       SET ussr.name="Soviet Union" """,

    """MERGE (ukr:Polity {slug:"ukraine"})
       SET ukr.name="Ukraine" """,

    """MATCH (p:Place {slug:"lviv"}), (pol:Polity {slug:"habsburg-empire"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1772, endYear:1918}]->(pol)""",

    """MATCH (p:Place {slug:"lviv"}), (pol:Polity {slug:"poland-second-republic"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1918, endYear:1939}]->(pol)""",

    """MATCH (p:Place {slug:"lviv"}), (pol:Polity {slug:"soviet-union"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1939, endYear:1991}]->(pol)""",

    """MATCH (p:Place {slug:"lviv"}), (pol:Polity {slug:"ukraine"})
       MERGE (p)-[r:GOVERNED_BY {startYear:1991}]->(pol)""",

    # ========================================================================
    # 8. CITY MERGERS: Greater London, New York City
    # ========================================================================
    """MERGE (p:Place {slug:"greater-london"})
       SET p.name="Greater London", p.kind="city", p.wikidata_id="Q84",
           p.lat=51.5074, p.lon=-0.1278""",

    """MERGE (c:Place {slug:"city-of-london"})
       SET c.name="City of London", c.kind="district", c.wikidata_id="Q23311",
           c.description="Historic core, the Square Mile" """,

    """MERGE (w:Place {slug:"westminster-district"})
       SET w.name="City of Westminster", w.kind="district", w.wikidata_id="Q170201" """,

    """MATCH (p:Place {slug:"greater-london"}), (c:Place {slug:"city-of-london"})
       MERGE (p)-[r:CONTAINS {startYear:1965}]->(c)""",

    """MATCH (p:Place {slug:"greater-london"}), (w:Place {slug:"westminster-district"})
       MERGE (p)-[r:CONTAINS {startYear:1965}]->(w)""",

    """MERGE (e:Event {slug:"creation-of-greater-london"})
       SET e.name="Creation of Greater London", e.kind="Administrative", e.startYear=1965,
           e.description="London Government Act 1963 merged the County of London and parts of surrounding counties" """,

    """MATCH (e:Event {slug:"creation-of-greater-london"}), (p:Place {slug:"greater-london"})
       MERGE (e)-[:OCCURS_IN]->(p)""",

    # New York City
    """MERGE (p:Place {slug:"new-york-city"})
       SET p.name="New York City", p.kind="city", p.wikidata_id="Q60",
           p.lat=40.7128, p.lon=-74.0060""",

    """MERGE (m:Place {slug:"manhattan"})
       SET m.name="Manhattan", m.kind="borough", m.wikidata_id="Q11299" """,

    """MERGE (b:Place {slug:"brooklyn"})
       SET b.name="Brooklyn", b.kind="borough", b.wikidata_id="Q18419",
           b.description="Formerly independent City of Brooklyn" """,

    """MERGE (q:Place {slug:"queens"})
       SET q.name="Queens", q.kind="borough", q.wikidata_id="Q18424" """,

    """MERGE (bx:Place {slug:"the-bronx"})
       SET bx.name="The Bronx", bx.kind="borough", bx.wikidata_id="Q18426" """,

    """MERGE (si:Place {slug:"staten-island"})
       SET si.name="Staten Island", si.kind="borough", si.wikidata_id="Q18437" """,

    """MATCH (p:Place {slug:"new-york-city"}), (m:Place {slug:"manhattan"})
       MERGE (p)-[r:CONTAINS {startYear:1898}]->(m)""",

    """MATCH (p:Place {slug:"new-york-city"}), (b:Place {slug:"brooklyn"})
       MERGE (p)-[r:CONTAINS {startYear:1898}]->(b)""",

    """MATCH (p:Place {slug:"new-york-city"}), (q:Place {slug:"queens"})
       MERGE (p)-[r:CONTAINS {startYear:1898}]->(q)""",

    """MATCH (p:Place {slug:"new-york-city"}), (bx:Place {slug:"the-bronx"})
       MERGE (p)-[r:CONTAINS {startYear:1898}]->(bx)""",

    """MATCH (p:Place {slug:"new-york-city"}), (si:Place {slug:"staten-island"})
       MERGE (p)-[r:CONTAINS {startYear:1898}]->(si)""",

    """MERGE (e:Event {slug:"nyc-consolidation-1898"})
       SET e.name="Consolidation of New York City", e.kind="Administrative", e.startYear=1898,
           e.description="Five boroughs consolidated into Greater New York" """,

    """MATCH (e:Event {slug:"nyc-consolidation-1898"}), (p:Place {slug:"new-york-city"})
       MERGE (e)-[:OCCURS_IN]->(p)""",
]


# ============================================================================
# Queries for verification
# ============================================================================

Q_SUMMARY = """
MATCH (p:Place)-[:HAS_NAME]->(n:PlaceName)
WITH p, count(n) AS names
RETURN p.slug AS place, p.name AS current_name, names
ORDER BY names DESC
"""

Q_JEBUS = """
MATCH (pn:PlaceName {name:"Jebus"})<-[:HAS_NAME]-(p:Place)
MATCH (e:Event)-[:OCCURS_IN]->(p)
OPTIONAL MATCH (person:Person)-[:PARTICIPATES_IN]->(e)
RETURN pn.name AS historic_name, e.name AS event, e.startYear AS year, person.name AS participant
"""

Q_EXTINCT = """
MATCH (p:Place {status:"EXTINCT"})-[:LOCATED_IN]->(country:Place)
RETURN p.slug, p.name, country.name AS modern_container
"""

Q_BORDER_CHANGES = """
MATCH (p:Place {slug:"alsace"})-[r:GOVERNED_BY]->(pol:Polity)
RETURN p.name AS place, pol.name AS polity, r.startYear AS from_year, r.endYear AS to_year
ORDER BY r.startYear
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed comprehensive PlaceName examples.")
    parser.add_argument("--run", action="store_true", help="Execute against Neo4j (default is dry-run)")
    args = parser.parse_args()

    print("\n" + "=" * 70)
    print("COMPREHENSIVE PLACE NAME EXAMPLES SEEDER")
    print("=" * 70)

    if not args.run:
        print("\n[DRY-RUN] Would execute", len(STATEMENTS), "Cypher statements.\n")
        print("Categories covered:")
        print("  1. Conquest: Jerusalem (Jebus → Aelia Capitolina), Istanbul (Byzantium → Constantinople)")
        print("  2. Regime change: St. Petersburg ↔ Petrograd ↔ Leningrad")
        print("  3. Decolonization: Mumbai (Bombay), Sri Lanka (Ceylon)")
        print("  4. Exonyms: Deutschland vs Germany vs Allemagne")
        print("  5. Script variants: 北京 / Beijing / Peking")
        print("  6. Extinct places: Babylon, Troy, Carthage (linked to modern countries)")
        print("  7. Border changes: Alsace, Lviv (GOVERNED_BY with time ranges)")
        print("  8. City mergers: Greater London, NYC boroughs")
        print("\nRe-run with --run to execute against Neo4j.\n")
        return 0

    driver = get_neo4j_driver()
    try:
        with driver.session() as session:
            print(f"\nExecuting {len(STATEMENTS)} statements...")
            for i, stmt in enumerate(STATEMENTS, 1):
                session.run(stmt)
                if i % 20 == 0:
                    print(f"  ... {i}/{len(STATEMENTS)}")
            print(f"  ... {len(STATEMENTS)}/{len(STATEMENTS)} ✓")

            print("\n--- Summary: Places with name variants ---")
            for row in session.run(Q_SUMMARY):
                print(f"  {row['place']:25} ({row['current_name']:20}) — {row['names']} name(s)")

            print("\n--- Query: Events resolved from 'Jebus' ---")
            for row in session.run(Q_JEBUS):
                print(f"  {row['historic_name']} → {row['event']} ({row['year']}) — {row['participant']}")

            print("\n--- Query: Extinct places linked to modern containers ---")
            for row in session.run(Q_EXTINCT):
                print(f"  {row['p.name']:15} → {row['modern_container']}")

            print("\n--- Query: Alsace sovereignty changes ---")
            for row in session.run(Q_BORDER_CHANGES):
                end = row['to_year'] or 'present'
                print(f"  {row['place']} governed by {row['polity']:20} ({row['from_year']} – {end})")

        print("\n✓ All data seeded successfully.\n")
        return 0
    finally:
        driver.close()


if __name__ == "__main__":
    raise SystemExit(main())
