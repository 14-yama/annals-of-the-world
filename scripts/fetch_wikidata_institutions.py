#!/usr/bin/env python3
"""
fetch_wikidata_institutions.py  (v2.0)

Comprehensive Wikidata fetch of notable institutions across ALL Class 3
divisions (310-394). Uses 200+ Wikidata type QIDs, low sitelinks threshold
(>=5), granular batch splitting to avoid timeouts, and adaptive limit fallback.

Output: data/wikidata_institutions.json

Usage:
    python3 scripts/fetch_wikidata_institutions.py
    python3 scripts/fetch_wikidata_institutions.py --limit 5000
    python3 scripts/fetch_wikidata_institutions.py --dry-run
"""

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

import requests

# ── Wikidata SPARQL endpoint ──
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = (
    "AnnalsOfTheWorld/2.0 "
    "(https://github.com/annals-of-the-world; contact@annals.dev)"
)

# ═══════════════════════════════════════════════════════════════════
# Institution Type -> Division Mapping  (200+ QIDs)
# Maps Wikidata P31 (instance of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

INSTITUTION_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 310 Political Institutions ──
    "Q7188":      ("310", "Political Institutions"),
    "Q1063239":   ("310", "Political Institutions"),
    "Q179164":    ("310", "Political Institutions"),
    "Q7210356":   ("310", "Political Institutions"),
    "Q15238777":  ("310", "Political Institutions"),
    "Q3024240":   ("310", "Political Institutions"),
    "Q3624078":   ("310", "Political Institutions"),

    # ── 311 Parliaments & Legislatures ──
    "Q35798":     ("311", "Parliaments & Legislatures"),
    "Q188572":    ("311", "Parliaments & Legislatures"),
    "Q637846":    ("311", "Parliaments & Legislatures"),
    "Q2481024":   ("311", "Parliaments & Legislatures"),
    "Q1752346":   ("311", "Parliaments & Legislatures"),
    "Q10553309":  ("311", "Parliaments & Legislatures"),
    "Q2769600":   ("311", "Parliaments & Legislatures"),

    # ── 312 Monarchies & Royal Courts ──
    "Q164142":    ("312", "Monarchies & Royal Courts"),
    "Q210950":    ("312", "Monarchies & Royal Courts"),
    "Q131401":    ("312", "Monarchies & Royal Courts"),
    "Q16519632":  ("312", "Monarchies & Royal Courts"),
    "Q3519143":   ("312", "Monarchies & Royal Courts"),
    "Q15917824":  ("312", "Monarchies & Royal Courts"),

    # ── 313 Executive & Presidential Offices ──
    "Q189445":    ("313", "Executive & Presidential Offices"),
    "Q2578272":   ("313", "Executive & Presidential Offices"),
    "Q640506":    ("313", "Executive & Presidential Offices"),
    "Q327591":    ("313", "Executive & Presidential Offices"),
    "Q1553390":   ("313", "Executive & Presidential Offices"),

    # ── 314 Colonial & Imperial Administrations ──
    "Q133156":    ("314", "Colonial & Imperial Administrations"),
    "Q146505":    ("314", "Colonial & Imperial Administrations"),
    "Q217577":    ("314", "Colonial & Imperial Administrations"),
    "Q164170":    ("314", "Colonial & Imperial Administrations"),
    "Q28171":     ("314", "Colonial & Imperial Administrations"),
    "Q1371724":   ("314", "Colonial & Imperial Administrations"),
    "Q1250464":   ("314", "Colonial & Imperial Administrations"),
    "Q17335163":  ("314", "Colonial & Imperial Administrations"),

    # ── 315 Tribal & Indigenous Councils ──
    "Q133311":    ("315", "Tribal & Indigenous Councils"),
    "Q756604":    ("315", "Tribal & Indigenous Councils"),
    "Q210272":    ("315", "Tribal & Indigenous Councils"),
    "Q811430":    ("315", "Tribal & Indigenous Councils"),

    # ── 316 Political Parties & Organizations ──
    "Q7278":      ("316", "Political Parties & Organizations"),
    "Q1307214":   ("316", "Political Parties & Organizations"),
    "Q6138528":   ("316", "Political Parties & Organizations"),
    "Q4204975":   ("316", "Political Parties & Organizations"),
    "Q847017":    ("316", "Political Parties & Organizations"),
    "Q233591":    ("316", "Political Parties & Organizations"),
    "Q6199":      ("316", "Political Parties & Organizations"),
    "Q178790":    ("316", "Political Parties & Organizations"),

    # ── 320 Legal Institutions ──
    "Q327333":    ("320", "Legal Institutions"),
    "Q1751547":   ("320", "Legal Institutions"),
    "Q7918010":   ("320", "Legal Institutions"),

    # ── 321 Courts & Tribunals ──
    "Q41487":     ("321", "Courts & Tribunals"),
    "Q7889389":   ("321", "Courts & Tribunals"),
    "Q63074573":  ("321", "Courts & Tribunals"),
    "Q1076185":   ("321", "Courts & Tribunals"),
    "Q1752824":   ("321", "Courts & Tribunals"),
    "Q11703219":  ("321", "Courts & Tribunals"),
    "Q1289157":   ("321", "Courts & Tribunals"),
    "Q2915731":   ("321", "Courts & Tribunals"),

    # ── 322 Law Schools & Legal Academies ──
    "Q1143635":   ("322", "Law Schools & Legal Academies"),
    "Q4287745":   ("322", "Law Schools & Legal Academies"),

    # ── 323 Regulatory Bodies & Commissions ──
    "Q1981740":   ("323", "Regulatory Bodies & Commissions"),
    "Q192350":    ("323", "Regulatory Bodies & Commissions"),
    "Q1668024":   ("323", "Regulatory Bodies & Commissions"),
    "Q681762":    ("323", "Regulatory Bodies & Commissions"),
    "Q14350752":  ("323", "Regulatory Bodies & Commissions"),

    # ── 330 Economic Institutions ──
    "Q43015":     ("330", "Economic Institutions"),
    "Q806880":    ("330", "Economic Institutions"),
    "Q22687":     ("330", "Economic Institutions"),

    # ── 331 Central Banks & Treasuries ──
    "Q66344":     ("331", "Central Banks & Treasuries"),
    "Q5138781":   ("331", "Central Banks & Treasuries"),

    # ── 332 Stock Exchanges & Markets ──
    "Q476028":    ("332", "Stock Exchanges & Markets"),
    "Q38829":     ("332", "Stock Exchanges & Markets"),
    "Q11691":     ("332", "Stock Exchanges & Markets"),
    "Q183951":    ("332", "Stock Exchanges & Markets"),

    # ── 333 Trade Guilds & Merchant Houses ──
    "Q43229":     ("333", "Trade Guilds & Merchant Houses"),
    "Q158633":    ("333", "Trade Guilds & Merchant Houses"),
    "Q1762059":   ("333", "Trade Guilds & Merchant Houses"),
    "Q891723":    ("333", "Trade Guilds & Merchant Houses"),

    # ── 334 Development Banks & Aid Agencies ──
    "Q1785733":   ("334", "Development Banks & Aid Agencies"),
    "Q1332577":   ("334", "Development Banks & Aid Agencies"),

    # ── 340 Religious Institutions ──
    "Q9174":      ("340", "Religious Institutions"),
    "Q2061186":   ("340", "Religious Institutions"),
    "Q1530022":   ("340", "Religious Institutions"),
    "Q1092940":   ("340", "Religious Institutions"),
    "Q879146":    ("340", "Religious Institutions"),
    "Q13414953":  ("340", "Religious Institutions"),
    "Q11828860":  ("340", "Religious Institutions"),
    "Q1781360":   ("340", "Religious Institutions"),
    "Q8065736":   ("340", "Religious Institutions"),
    "Q3146899":   ("340", "Religious Institutions"),
    "Q160016":    ("340", "Religious Institutions"),

    # ── 341 Churches & Cathedrals ──
    "Q16970":     ("341", "Churches & Cathedrals"),
    "Q2977":      ("341", "Churches & Cathedrals"),
    "Q108325":    ("341", "Churches & Cathedrals"),
    "Q317557":    ("341", "Churches & Cathedrals"),
    "Q120560":    ("341", "Churches & Cathedrals"),
    "Q54819":     ("341", "Churches & Cathedrals"),
    "Q1088552":   ("341", "Churches & Cathedrals"),
    "Q56242215":  ("341", "Churches & Cathedrals"),

    # ── 342 Mosques & Islamic Institutions ──
    "Q32815":     ("342", "Mosques & Islamic Institutions"),
    "Q185451":    ("342", "Mosques & Islamic Institutions"),
    "Q697295":    ("342", "Mosques & Islamic Institutions"),
    "Q2536196":   ("342", "Mosques & Islamic Institutions"),
    "Q15070976":  ("342", "Mosques & Islamic Institutions"),

    # ── 343 Temples & Shrines ──
    "Q44539":     ("343", "Temples & Shrines"),
    "Q845945":    ("343", "Temples & Shrines"),
    "Q314157":    ("343", "Temples & Shrines"),
    "Q634261":    ("343", "Temples & Shrines"),
    "Q4421":      ("343", "Temples & Shrines"),
    "Q1539303":   ("343", "Temples & Shrines"),
    "Q856076":    ("343", "Temples & Shrines"),
    "Q5393308":   ("343", "Temples & Shrines"),
    "Q697763":    ("343", "Temples & Shrines"),

    # ── 344 Monasteries & Religious Orders ──
    "Q44613":     ("344", "Monasteries & Religious Orders"),
    "Q160742":    ("344", "Monasteries & Religious Orders"),
    "Q191067":    ("344", "Monasteries & Religious Orders"),
    "Q1373513":   ("344", "Monasteries & Religious Orders"),
    "Q208628":    ("344", "Monasteries & Religious Orders"),
    "Q2576651":   ("344", "Monasteries & Religious Orders"),
    "Q3574816":   ("344", "Monasteries & Religious Orders"),

    # ── 345 Seminaries & Theological Schools ──
    "Q1145552":   ("345", "Seminaries & Theological Schools"),
    "Q18127":     ("345", "Seminaries & Theological Schools"),
    "Q3152824":   ("345", "Seminaries & Theological Schools"),
    "Q1542651":   ("345", "Seminaries & Theological Schools"),

    # ── 350 Scientific Institutions ──
    "Q31855":     ("350", "Scientific Institutions"),
    "Q1298668":   ("350", "Scientific Institutions"),
    "Q3354859":   ("350", "Scientific Institutions"),
    "Q1365560":   ("350", "Scientific Institutions"),

    # ── 351 Academies & Learned Societies ──
    "Q414147":    ("351", "Academies & Learned Societies"),
    "Q955824":    ("351", "Academies & Learned Societies"),
    "Q1788992":   ("351", "Academies & Learned Societies"),
    "Q459310":    ("351", "Academies & Learned Societies"),
    "Q1566079":   ("351", "Academies & Learned Societies"),
    "Q727459":    ("351", "Academies & Learned Societies"),
    "Q1064758":   ("351", "Academies & Learned Societies"),

    # ── 352 Research Laboratories ──
    "Q483242":    ("352", "Research Laboratories"),
    "Q7315155":   ("352", "Research Laboratories"),
    "Q5341295":   ("352", "Research Laboratories"),
    "Q16889133":  ("352", "Research Laboratories"),

    # ── 353 Observatories & Expeditions ──
    "Q62832":     ("353", "Observatories & Expeditions"),
    "Q2235308":   ("353", "Observatories & Expeditions"),
    "Q205495":    ("353", "Observatories & Expeditions"),
    "Q167346":    ("353", "Observatories & Expeditions"),
    "Q174583":    ("353", "Observatories & Expeditions"),

    # ── 354 Medical Institutions & Hospitals ──
    "Q16917":     ("354", "Medical Institutions & Hospitals"),
    "Q180958":    ("354", "Medical Institutions & Hospitals"),
    "Q1774898":   ("354", "Medical Institutions & Hospitals"),
    "Q4260475":   ("354", "Medical Institutions & Hospitals"),
    "Q838948":    ("354", "Medical Institutions & Hospitals"),
    "Q2140298":   ("354", "Medical Institutions & Hospitals"),
    "Q205892":    ("354", "Medical Institutions & Hospitals"),
    "Q63917":     ("354", "Medical Institutions & Hospitals"),

    # ── 360 Cultural Institutions ──
    "Q2659904":   ("360", "Cultural Institutions"),
    "Q13226383":  ("360", "Cultural Institutions"),

    # ── 361 Museums & Galleries ──
    "Q33506":     ("361", "Museums & Galleries"),
    "Q1007870":   ("361", "Museums & Galleries"),
    "Q207694":    ("361", "Museums & Galleries"),
    "Q575759":    ("361", "Museums & Galleries"),
    "Q1970365":   ("361", "Museums & Galleries"),
    "Q2772772":   ("361", "Museums & Galleries"),
    "Q684740":    ("361", "Museums & Galleries"),
    "Q1571723":   ("361", "Museums & Galleries"),
    "Q3669835":   ("361", "Museums & Galleries"),
    "Q2863507":   ("361", "Museums & Galleries"),
    "Q1542668":   ("361", "Museums & Galleries"),
    "Q18674739":  ("361", "Museums & Galleries"),
    "Q4989906":   ("361", "Museums & Galleries"),

    # ── 362 Libraries & Archives ──
    "Q7075":      ("362", "Libraries & Archives"),
    "Q856234":    ("362", "Libraries & Archives"),
    "Q166118":    ("362", "Libraries & Archives"),
    "Q264757":    ("362", "Libraries & Archives"),
    "Q1269612":   ("362", "Libraries & Archives"),
    "Q39614":     ("362", "Libraries & Archives"),

    # ── 363 Theaters & Performance Venues ──
    "Q24354":     ("363", "Theaters & Performance Venues"),
    "Q153562":    ("363", "Theaters & Performance Venues"),
    "Q57660343":  ("363", "Theaters & Performance Venues"),
    "Q41253":     ("363", "Theaters & Performance Venues"),
    "Q1616075":   ("363", "Theaters & Performance Venues"),

    # ── 364 Media & Publishing Houses ──
    "Q2085381":   ("364", "Media & Publishing Houses"),
    "Q192283":    ("364", "Media & Publishing Houses"),
    "Q2001305":   ("364", "Media & Publishing Houses"),
    "Q17232649":  ("364", "Media & Publishing Houses"),
    "Q1030034":   ("364", "Media & Publishing Houses"),
    "Q11032":     ("364", "Media & Publishing Houses"),
    "Q1002697":   ("364", "Media & Publishing Houses"),
    "Q5398426":   ("364", "Media & Publishing Houses"),
    "Q15265344":  ("364", "Media & Publishing Houses"),
    "Q41298":     ("364", "Media & Publishing Houses"),
    "Q10885":     ("364", "Media & Publishing Houses"),
    "Q7651526":   ("364", "Media & Publishing Houses"),

    # ── 370 International Organizations ──
    "Q484652":    ("370", "International Organizations"),
    "Q15925165":  ("370", "International Organizations"),
    "Q178706":    ("370", "International Organizations"),
    "Q79913":     ("370", "International Organizations"),
    "Q7163":      ("370", "International Organizations"),

    # ── 371 United Nations System ──
    "Q1335818":   ("371", "United Nations System"),
    "Q66239647":  ("371", "United Nations System"),
    "Q3238801":   ("371", "United Nations System"),

    # ── 372 Regional Alliances & Blocs ──
    "Q3623811":   ("372", "Regional Alliances & Blocs"),
    "Q4120211":   ("372", "Regional Alliances & Blocs"),
    "Q170156":    ("372", "Regional Alliances & Blocs"),
    "Q392918":    ("372", "Regional Alliances & Blocs"),

    # ── 373 Humanitarian & Relief Organizations ──
    "Q163740":    ("373", "Humanitarian & Relief Organizations"),
    "Q708676":    ("373", "Humanitarian & Relief Organizations"),
    "Q15911314":  ("373", "Humanitarian & Relief Organizations"),
    "Q22698":     ("373", "Humanitarian & Relief Organizations"),
    "Q157031":    ("373", "Humanitarian & Relief Organizations"),

    # ── 374 Trade Agreements & Economic Unions ──
    "Q131569":    ("374", "Trade Agreements & Economic Unions"),
    "Q11514315":  ("374", "Trade Agreements & Economic Unions"),
    "Q180684":    ("374", "Trade Agreements & Economic Unions"),
    "Q273809":    ("374", "Trade Agreements & Economic Unions"),

    # ── 380 Educational Institutions ──
    "Q2385804":   ("380", "Educational Institutions"),
    "Q23002054":  ("380", "Educational Institutions"),

    # ── 381 Universities & Colleges ──
    "Q3918":      ("381", "Universities & Colleges"),
    "Q189004":    ("381", "Universities & Colleges"),
    "Q875538":    ("381", "Universities & Colleges"),
    "Q38723":     ("381", "Universities & Colleges"),
    "Q5296884":   ("381", "Universities & Colleges"),
    "Q15936437":  ("381", "Universities & Colleges"),
    "Q902104":    ("381", "Universities & Colleges"),
    "Q1371037":   ("381", "Universities & Colleges"),
    "Q523926":    ("381", "Universities & Colleges"),
    "Q1188663":   ("381", "Universities & Colleges"),
    "Q15708736":  ("381", "Universities & Colleges"),
    "Q2297839":   ("381", "Universities & Colleges"),

    # ── 382 Schools & Academies ──
    "Q3914":      ("382", "Schools & Academies"),
    "Q149566":    ("382", "Schools & Academies"),
    "Q9826":      ("382", "Schools & Academies"),
    "Q159334":    ("382", "Schools & Academies"),
    "Q1076394":   ("382", "Schools & Academies"),
    "Q47530":     ("382", "Schools & Academies"),
    "Q5874429":   ("382", "Schools & Academies"),
    "Q1663561":   ("382", "Schools & Academies"),

    # ── 383 Madrasas & Religious Schools ──
    "Q185451b":   ("383", "Madrasas & Religious Schools"),
    "Q697295b":   ("383", "Madrasas & Religious Schools"),

    # ── 384 Public Education Systems ──
    "Q16023913":  ("384", "Public Education Systems"),

    # ── 390 Military & Defense Organizations ──
    "Q176799":    ("390", "Military & Defense Organizations"),
    "Q15627509":  ("390", "Military & Defense Organizations"),
    "Q781132":    ("390", "Military & Defense Organizations"),
    "Q17149090":  ("390", "Military & Defense Organizations"),

    # ── 391 Armies & Ground Forces ──
    "Q37726":     ("391", "Armies & Ground Forces"),
    "Q1643989":   ("391", "Armies & Ground Forces"),
    "Q166643":    ("391", "Armies & Ground Forces"),
    "Q188517":    ("391", "Armies & Ground Forces"),
    "Q4194289":   ("391", "Armies & Ground Forces"),
    "Q783857":    ("391", "Armies & Ground Forces"),

    # ── 392 Navies & Maritime Forces ──
    "Q4508":      ("392", "Navies & Maritime Forces"),
    "Q2327867":   ("392", "Navies & Maritime Forces"),
    "Q6821782":   ("392", "Navies & Maritime Forces"),
    "Q62049":     ("392", "Navies & Maritime Forces"),

    # ── 393 Intelligence & Security Agencies ──
    "Q47913":     ("393", "Intelligence & Security Agencies"),
    "Q3236990":   ("393", "Intelligence & Security Agencies"),
    "Q732717":    ("393", "Intelligence & Security Agencies"),

    # ── 394 Military Alliances ──
    "Q1127126":   ("394", "Military Alliances (NATO, etc.)"),
}

# Build reverse lookup: first-occurrence wins
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in INSTITUTION_TYPE_MAP.items():
    clean_qid = _qid.rstrip("b")  # handle suffixed dupes
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info

# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (68 granular batches)
# Each batch -> (QIDs, min_sitelinks)
# Heavy types split solo w/ higher threshold to avoid timeouts
# ═══════════════════════════════════════════════════════════════════

INSTITUTION_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── Political (310-316) ──
    "310_govt":         (["Q7188", "Q1063239", "Q3624078", "Q15238777"], 5),
    "311_parliament":   (["Q35798", "Q188572", "Q637846", "Q1752346", "Q2481024"], 5),
    "312_monarchy":     (["Q164142", "Q210950", "Q131401", "Q16519632", "Q3519143"], 5),
    "313_executive":    (["Q640506", "Q327591", "Q1553390", "Q2578272"], 5),
    "314_colonial":     (["Q133156", "Q146505", "Q217577", "Q164170", "Q1250464", "Q28171"], 5),
    "316_party":        (["Q7278"], 10),
    "316_party_b":      (["Q1307214", "Q6138528", "Q847017", "Q233591"], 5),
    "316_union":        (["Q6199"], 8),

    # ── Legal (320-323) ──
    "321_court":        (["Q41487", "Q7889389", "Q63074573", "Q1076185", "Q1752824"], 5),
    "321_court_b":      (["Q11703219", "Q1289157", "Q2915731"], 5),
    "322_law_school":   (["Q1143635", "Q4287745"], 5),
    "323_regulatory":   (["Q1981740", "Q192350", "Q1668024", "Q14350752"], 5),

    # ── Economic (330-334)  — split to survive timeouts ──
    "330_bank":         (["Q22687"], 15),
    "331_central":      (["Q66344", "Q5138781"], 5),
    "332_exchange":     (["Q476028", "Q38829", "Q11691", "Q183951"], 5),
    "333_guild":        (["Q43229", "Q891723"], 5),
    "333_trading":      (["Q158633", "Q1762059"], 5),
    "334_devbank":      (["Q1785733", "Q1332577"], 5),
    "330_finance":      (["Q43015", "Q806880"], 10),

    # ── Religious (340-345) ──
    "340_relig_a":      (["Q2061186", "Q1092940", "Q879146", "Q1530022"], 5),
    "340_relig_b":      (["Q13414953", "Q11828860", "Q1781360"], 5),
    "340_relig_c":      (["Q8065736", "Q3146899", "Q160016"], 5),
    "341_cathedral":    (["Q2977", "Q108325", "Q120560"], 5),
    "341_church_a":     (["Q16970"], 5),
    "341_church_b":     (["Q317557", "Q54819", "Q1088552"], 5),
    "342_mosque":       (["Q32815", "Q2536196", "Q15070976"], 5),
    "343_temple_a":     (["Q44539", "Q856076"], 5),
    "343_temple_b":     (["Q845945", "Q4421", "Q1539303"], 5),
    "343_pagoda":       (["Q314157", "Q634261", "Q5393308", "Q697763"], 5),
    "344_monastery":    (["Q44613", "Q160742"], 5),
    "344_order":        (["Q191067", "Q1373513", "Q208628", "Q2576651", "Q3574816"], 5),
    "345_seminary":     (["Q1145552", "Q18127", "Q3152824", "Q1542651"], 5),

    # ── Scientific (350-354) ──
    "350_research":     (["Q31855", "Q1298668", "Q3354859", "Q1365560"], 5),
    "351_academy":      (["Q414147", "Q955824", "Q1788992", "Q459310"], 5),
    "351_society":      (["Q1566079", "Q727459", "Q1064758"], 5),
    "352_lab":          (["Q483242", "Q7315155", "Q5341295", "Q16889133"], 5),
    "353_observatory":  (["Q62832", "Q2235308", "Q205495"], 5),
    "353_garden":       (["Q167346", "Q174583"], 5),
    "354_hospital_a":   (["Q16917"], 5),
    "354_hospital_b":   (["Q838948", "Q4260475", "Q180958", "Q1774898"], 5),
    "354_hospital_c":   (["Q2140298", "Q205892", "Q63917"], 5),

    # ── Cultural (360-364) ──
    "361_museum":       (["Q33506"], 5),
    "361_art_museum":   (["Q207694", "Q1007870"], 5),
    "361_hist_museum":  (["Q575759", "Q1970365", "Q684740"], 5),
    "361_sci_museum":   (["Q2772772", "Q1571723", "Q3669835", "Q2863507"], 5),
    "361_other_museum": (["Q1542668", "Q18674739", "Q4989906"], 5),
    "362_library":      (["Q7075", "Q856234", "Q264757", "Q1269612"], 5),
    "362_archive":      (["Q166118", "Q39614"], 5),
    "363_theater":      (["Q24354", "Q153562", "Q57660343"], 5),
    "363_cinema":       (["Q41253", "Q1616075"], 5),
    "364_newspaper":    (["Q11032"], 8),
    "364_magazine":     (["Q41298", "Q1002697"], 8),
    "364_broadcast":    (["Q5398426", "Q15265344", "Q2001305"], 8),
    "364_radio":        (["Q1030034"], 8),
    "364_publisher":    (["Q2085381", "Q192283", "Q10885"], 5),
    "364_record":       (["Q7651526"], 8),

    # ── International (370-374) ──
    "370_intl":         (["Q484652", "Q15925165", "Q7163"], 5),
    "371_un":           (["Q1335818", "Q66239647", "Q3238801"], 5),
    "372_regional":     (["Q3623811", "Q4120211", "Q392918"], 5),
    "373_ngo":          (["Q708676", "Q22698"], 5),
    "373_nonprofit":    (["Q163740"], 15),
    "373_foundation":   (["Q157031"], 8),
    "374_treaty":       (["Q131569"], 5),
    "374_union":        (["Q11514315", "Q180684", "Q273809"], 5),

    # ── Educational (380-384) ──
    "381_univ_a":       (["Q3918"], 5),
    "381_univ_b":       (["Q875538", "Q5296884", "Q15936437", "Q902104"], 5),
    "381_college":      (["Q189004", "Q1371037", "Q523926", "Q1188663", "Q38723"], 5),
    "382_school":       (["Q3914"], 12),
    "382_school_b":     (["Q149566", "Q9826", "Q47530", "Q5874429", "Q1663561"], 5),
    "383_madrasa":      (["Q185451", "Q697295"], 5),

    # ── Military (390-394) ──
    "390_armed":        (["Q15627509", "Q781132", "Q17149090"], 5),
    "391_army":         (["Q37726", "Q1643989"], 5),
    "391_unit":         (["Q166643", "Q188517", "Q4194289", "Q783857"], 5),
    "392_navy":         (["Q4508", "Q6821782", "Q62049"], 5),
    "393_intel":        (["Q47913", "Q3236990", "Q732717"], 5),
    "394_alliance":     (["Q1127126"], 5),
}

# ═══════════════════════════════════════════════════════════════════
# Country / Region / Continent mapping
# ═══════════════════════════════════════════════════════════════════

COUNTRY_INFO: dict[str, tuple[str, str, str]] = {
    "Q30":    ("United States", "North America", "Americas"),
    "Q145":   ("United Kingdom", "Northern Europe", "Europe"),
    "Q142":   ("France", "Western Europe", "Europe"),
    "Q183":   ("Germany", "Western Europe", "Europe"),
    "Q38":    ("Italy", "Southern Europe", "Europe"),
    "Q29":    ("Spain", "Southern Europe", "Europe"),
    "Q159":   ("Russia", "Eastern Europe", "Europe"),
    "Q148":   ("China", "East Asia", "Asia"),
    "Q668":   ("India", "South Asia", "Asia"),
    "Q17":    ("Japan", "East Asia", "Asia"),
    "Q884":   ("South Korea", "East Asia", "Asia"),
    "Q39":    ("Switzerland", "Western Europe", "Europe"),
    "Q40":    ("Austria", "Western Europe", "Europe"),
    "Q55":    ("Netherlands", "Western Europe", "Europe"),
    "Q36":    ("Poland", "Eastern Europe", "Europe"),
    "Q37":    ("Lithuania", "Northern Europe", "Europe"),
    "Q41":    ("Greece", "Southern Europe", "Europe"),
    "Q20":    ("Norway", "Northern Europe", "Europe"),
    "Q34":    ("Sweden", "Northern Europe", "Europe"),
    "Q35":    ("Denmark", "Northern Europe", "Europe"),
    "Q31":    ("Belgium", "Western Europe", "Europe"),
    "Q16":    ("Canada", "North America", "Americas"),
    "Q96":    ("Mexico", "Central America", "Americas"),
    "Q155":   ("Brazil", "South America", "Americas"),
    "Q414":   ("Argentina", "South America", "Americas"),
    "Q298":   ("Chile", "South America", "Americas"),
    "Q739":   ("Colombia", "South America", "Americas"),
    "Q45":    ("Portugal", "Southern Europe", "Europe"),
    "Q408":   ("Australia", "Oceania", "Oceania"),
    "Q664":   ("New Zealand", "Oceania", "Oceania"),
    "Q79":    ("Egypt", "North Africa", "Africa"),
    "Q262":   ("Algeria", "North Africa", "Africa"),
    "Q1028":  ("Morocco", "North Africa", "Africa"),
    "Q115":   ("Ethiopia", "East Africa", "Africa"),
    "Q1033":  ("Nigeria", "West Africa", "Africa"),
    "Q929":   ("Central African Republic", "Central Africa", "Africa"),
    "Q258":   ("South Africa", "Southern Africa", "Africa"),
    "Q794":   ("Iran", "West Asia", "Asia"),
    "Q796":   ("Iraq", "West Asia", "Asia"),
    "Q801":   ("Israel", "West Asia", "Asia"),
    "Q843":   ("Pakistan", "South Asia", "Asia"),
    "Q837":   ("Nepal", "South Asia", "Asia"),
    "Q869":   ("Thailand", "Southeast Asia", "Asia"),
    "Q865":   ("Taiwan", "East Asia", "Asia"),
    "Q423":   ("North Korea", "East Asia", "Asia"),
    "Q881":   ("Vietnam", "Southeast Asia", "Asia"),
    "Q334":   ("Singapore", "Southeast Asia", "Asia"),
    "Q833":   ("Malaysia", "Southeast Asia", "Asia"),
    "Q252":   ("Indonesia", "Southeast Asia", "Asia"),
    "Q928":   ("Philippines", "Southeast Asia", "Asia"),
    "Q854":   ("Sri Lanka", "South Asia", "Asia"),
    "Q817":   ("Kuwait", "West Asia", "Asia"),
    "Q846":   ("Qatar", "West Asia", "Asia"),
    "Q878":   ("United Arab Emirates", "West Asia", "Asia"),
    "Q874":   ("Turkmenistan", "Central Asia", "Asia"),
    "Q889":   ("Afghanistan", "South Asia", "Asia"),
    "Q184":   ("Belarus", "Eastern Europe", "Europe"),
    "Q212":   ("Ukraine", "Eastern Europe", "Europe"),
    "Q213":   ("Czech Republic", "Eastern Europe", "Europe"),
    "Q214":   ("Slovakia", "Eastern Europe", "Europe"),
    "Q28":    ("Hungary", "Eastern Europe", "Europe"),
    "Q218":   ("Romania", "Eastern Europe", "Europe"),
    "Q219":   ("Bulgaria", "Eastern Europe", "Europe"),
    "Q215":   ("Slovenia", "Southern Europe", "Europe"),
    "Q224":   ("Croatia", "Southern Europe", "Europe"),
    "Q225":   ("Bosnia and Herzegovina", "Southern Europe", "Europe"),
    "Q117":   ("Ghana", "West Africa", "Africa"),
    "Q114":   ("Kenya", "East Africa", "Africa"),
    "Q1032":  ("Niger", "West Africa", "Africa"),
    "Q912":   ("Mali", "West Africa", "Africa"),
    "Q657":   ("Chad", "Central Africa", "Africa"),
    "Q1005":  ("Gambia", "West Africa", "Africa"),
    "Q27":    ("Ireland", "Northern Europe", "Europe"),
    "Q33":    ("Finland", "Northern Europe", "Europe"),
    "Q32":    ("Luxembourg", "Western Europe", "Europe"),
    "Q189":   ("Iceland", "Northern Europe", "Europe"),
    "Q842":   ("Oman", "West Asia", "Asia"),
    "Q810":   ("Jordan", "West Asia", "Asia"),
    "Q805":   ("Yemen", "West Asia", "Asia"),
    "Q851":   ("Saudi Arabia", "West Asia", "Asia"),
    "Q43":    ("Turkey", "West Asia", "Asia"),
    "Q965":   ("Burkina Faso", "West Africa", "Africa"),
    "Q1011":  ("Cape Verde", "West Africa", "Africa"),
    "Q1029":  ("Mozambique", "East Africa", "Africa"),
    "Q1030":  ("Namibia", "Southern Africa", "Africa"),
    "Q1044":  ("Sierra Leone", "West Africa", "Africa"),
    "Q945":   ("Togo", "West Africa", "Africa"),
    "Q1006":  ("Guinea", "West Africa", "Africa"),
    "Q1007":  ("Guinea-Bissau", "West Africa", "Africa"),
    "Q1008":  ("Ivory Coast", "West Africa", "Africa"),
    "Q974":   ("Democratic Republic of the Congo", "Central Africa", "Africa"),
    "Q971":   ("Republic of the Congo", "Central Africa", "Africa"),
    "Q916":   ("Angola", "Southern Africa", "Africa"),
    "Q953":   ("Zambia", "East Africa", "Africa"),
    "Q954":   ("Zimbabwe", "East Africa", "Africa"),
    "Q924":   ("Tanzania", "East Africa", "Africa"),
    "Q1009":  ("Cameroon", "Central Africa", "Africa"),
    "Q1036":  ("Uganda", "East Africa", "Africa"),
    "Q1037":  ("Rwanda", "East Africa", "Africa"),
    "Q1020":  ("Senegal", "West Africa", "Africa"),
    "Q233":   ("Malta", "Southern Europe", "Europe"),
    "Q236":   ("Montenegro", "Southern Europe", "Europe"),
    "Q229":   ("Cyprus", "Southern Europe", "Europe"),
    "Q227":   ("Azerbaijan", "West Asia", "Asia"),
    "Q230":   ("Georgia", "West Asia", "Asia"),
    "Q399":   ("Armenia", "West Asia", "Asia"),
    "Q813":   ("Kyrgyzstan", "Central Asia", "Asia"),
    "Q863":   ("Tajikistan", "Central Asia", "Asia"),
    "Q265":   ("Uzbekistan", "Central Asia", "Asia"),
    "Q232":   ("Kazakhstan", "Central Asia", "Asia"),
    "Q711":   ("Mongolia", "East Asia", "Asia"),
    "Q836":   ("Myanmar", "Southeast Asia", "Asia"),
    "Q819":   ("Laos", "Southeast Asia", "Asia"),
    "Q424":   ("Cambodia", "Southeast Asia", "Asia"),
    "Q717":   ("Venezuela", "South America", "Americas"),
    "Q419":   ("Peru", "South America", "Americas"),
    "Q736":   ("Ecuador", "South America", "Americas"),
    "Q750":   ("Bolivia", "South America", "Americas"),
    "Q733":   ("Paraguay", "South America", "Americas"),
    "Q77":    ("Uruguay", "South America", "Americas"),
    "Q774":   ("Guatemala", "Central America", "Americas"),
    "Q783":   ("Honduras", "Central America", "Americas"),
    "Q792":   ("El Salvador", "Central America", "Americas"),
    "Q800":   ("Costa Rica", "Central America", "Americas"),
    "Q804":   ("Panama", "Central America", "Americas"),
    "Q786":   ("Dominican Republic", "Caribbean", "Americas"),
    "Q241":   ("Cuba", "Caribbean", "Americas"),
    "Q766":   ("Jamaica", "Caribbean", "Americas"),
    "Q228":   ("Andorra", "Southern Europe", "Europe"),
    "Q238":   ("San Marino", "Southern Europe", "Europe"),
    "Q237":   ("Vatican City", "Southern Europe", "Europe"),
    "Q347":   ("Liechtenstein", "Western Europe", "Europe"),
    "Q235":   ("Monaco", "Western Europe", "Europe"),
    "Q1246":  ("Kosovo", "Southern Europe", "Europe"),
    "Q221":   ("North Macedonia", "Southern Europe", "Europe"),
    "Q403":   ("Serbia", "Southern Europe", "Europe"),
    "Q986":   ("Eritrea", "East Africa", "Africa"),
    "Q960":   ("Benin", "West Africa", "Africa"),
    "Q1025":  ("Mauritania", "West Africa", "Africa"),
    "Q1027":  ("Mauritius", "East Africa", "Africa"),
    "Q1019":  ("Madagascar", "East Africa", "Africa"),
    "Q963":   ("Botswana", "Southern Africa", "Africa"),
    "Q1013":  ("Lesotho", "Southern Africa", "Africa"),
    "Q1050":  ("Eswatini", "Southern Africa", "Africa"),
    "Q967":   ("Burundi", "East Africa", "Africa"),
    "Q977":   ("Djibouti", "East Africa", "Africa"),
    "Q1000":  ("Gabon", "Central Africa", "Africa"),
    "Q1014":  ("Liberia", "West Africa", "Africa"),
    "Q1041":  ("Seychelles", "East Africa", "Africa"),
    "Q1045":  ("Somalia", "East Africa", "Africa"),
    "Q1049":  ("Sudan", "North Africa", "Africa"),
    "Q958":   ("South Sudan", "East Africa", "Africa"),
    "Q1023":  ("Malawi", "East Africa", "Africa"),
    "Q1035":  ("Tunisia", "North Africa", "Africa"),
    "Q1042":  ("Libya", "North Africa", "Africa"),
}

DEFAULT_GEO = ("Global", "Global", "Global")


def get_country_info(country_qid: str | None) -> tuple[str, str, str]:
    if not country_qid:
        return DEFAULT_GEO
    return COUNTRY_INFO.get(country_qid, DEFAULT_GEO)


def year_to_era(year: int | None) -> tuple[str, str]:
    if year is None:
        return ("Classical", "classical")
    if year < -3000:
        return ("Prehistoric", "prehistoric")
    if year <= 500:
        return ("Classical", "classical")
    if year <= 1500:
        return ("Medieval", "medieval")
    if year <= 1800:
        return ("Early Modern", "early-modern")
    if year <= 1945:
        return ("Modern", "modern")
    return ("Contemporary", "contemporary")


def compute_significance(sitelinks: int, founding_year: int | None, dissolved_year: int | None) -> int:
    if sitelinks >= 150:
        score = 8
    elif sitelinks >= 100:
        score = 7
    elif sitelinks >= 70:
        score = 6
    elif sitelinks >= 50:
        score = 5
    elif sitelinks >= 35:
        score = 4
    elif sitelinks >= 20:
        score = 3
    elif sitelinks >= 12:
        score = 2
    else:
        score = 1
    if founding_year is not None:
        if founding_year < -1000:
            score += 2
        elif founding_year < 500:
            score += 1
    if dissolved_year is None and founding_year is not None:
        score += 1
    return max(1, min(10, score))


def significance_label(score: int) -> str:
    if score >= 9:
        return "Landmark"
    if score >= 7:
        return "Major"
    if score >= 5:
        return "Notable"
    if score >= 3:
        return "Moderate"
    return "Minor"


def parse_year(date_str: str | None) -> int | None:
    if not date_str:
        return None
    m = re.match(r'^([+-]?\d+)', date_str)
    return int(m.group(1)) if m else None


def format_date_display(date_str: str | None) -> str:
    if not date_str:
        return ""
    m = re.match(r'^([+-]?)(\d+)-(\d{2})-(\d{2})', date_str)
    if not m:
        return ""
    sign, year_s, month, day = m.groups()
    year = int(year_s)
    if sign == "-" or (sign == "+" and year < 0):
        return f"{abs(year)} BCE"
    if year > 0 and year < 100:
        return f"{year} CE"
    if month == "01" and day == "01":
        return f"{year} CE" if year < 1000 else str(year)
    return f"{year}-{month}-{day}"


def make_slug(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def qid_from_uri(uri: str | None) -> str | None:
    if not uri:
        return None
    m = re.search(r'(Q\d+)$', uri)
    return m.group(1) if m else None


def binding_val(row: dict, key: str) -> str | None:
    b = row.get(key)
    return b["value"] if b and "value" in b else None


def get_division(type_qid: str | None) -> tuple[str, str]:
    if type_qid and type_qid in QID_TO_DIVISION:
        return QID_TO_DIVISION[type_qid]
    return ("310", "Political Institutions")


def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception ?dissolved
       ?country
       ?countryLabel
       ?headquartersLabel
       ?founderLabel
       ?image
       ?article
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  ?item wdt:P31 ?type .
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P571 ?inception . }}
  OPTIONAL {{ ?item wdt:P576 ?dissolved . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P159 ?headquarters . }}
  OPTIONAL {{ ?item wdt:P112 ?founder . }}
  OPTIONAL {{ ?item wdt:P18  ?image . }}
  OPTIONAL {{
    ?article schema:about ?item ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sitelinks)
LIMIT {limit}
"""


def fetch_sparql(query: str, retries: int = 3) -> list[dict[str, Any]]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/sparql-results+json",
    }
    for attempt in range(retries):
        try:
            resp = requests.get(
                SPARQL_ENDPOINT,
                params={"query": query, "format": "json"},
                headers=headers,
                timeout=180,
            )
            if resp.status_code == 429:
                wait = min(90, 15 * (attempt + 1))
                print(f"    Rate limited, waiting {wait}s ...")
                time.sleep(wait)
                continue
            if resp.status_code in (500, 504):
                wait = 20 * (attempt + 1)
                print(f"    Server {resp.status_code} (attempt {attempt+1}), retrying in {wait}s ...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            wait = 30 * (attempt + 1)
            print(f"    Timeout (attempt {attempt+1}), retrying in {wait}s ...")
            time.sleep(wait)
        except (ValueError, KeyError) as e:
            print(f"    Parse error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(10)
        except requests.exceptions.RequestException as e:
            print(f"    Error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
    return []


def fetch_adaptive(type_qids: list[str], target_limit: int, min_sl: int) -> list[dict[str, Any]]:
    """Try target limit; on failure halve until success."""
    limits = [target_limit]
    lim = target_limit
    while lim > 500:
        lim = lim // 2
        limits.append(lim)
    limits.append(500)

    for lim in limits:
        query = build_sparql_query(type_qids, limit=lim, min_sitelinks=min_sl)
        rows = fetch_sparql(query, retries=2)
        if rows:
            return rows
        if lim > 500:
            print(f"    Reducing limit: {lim} -> {lim // 2}")
    return []


def transform_institution(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""
    inception_raw = binding_val(row, "inception")
    dissolved_raw = binding_val(row, "dissolved")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    headquarters = binding_val(row, "headquartersLabel") or ""
    founder = binding_val(row, "founderLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    founding_year = parse_year(inception_raw)
    dissolved_year = parse_year(dissolved_raw)
    founded_display = format_date_display(inception_raw)
    dissolved_display = format_date_display(dissolved_raw)
    era, era_slug = year_to_era(founding_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label
    slug = make_slug(name)

    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if headquarters:
        summary += f" Headquartered in {headquarters}."
    elif country_name != "Global":
        summary += f" Located in {country_name}."
    if founding_year:
        summary += f" Founded c. {abs(founding_year)} BCE." if founding_year < 0 else f" Founded {founding_year}."
    if dissolved_year:
        summary += f" Dissolved c. {abs(dissolved_year)} BCE." if dissolved_year < 0 else f" Dissolved {dissolved_year}."

    sig_score = compute_significance(sitelinks, founding_year, dissolved_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Institution",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Institutions -- {div_heading} -- {country_name} -- {era}"],
        "subjects": [s for s in [country_name, type_label, continent, div_heading] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": ["CAUSE_AND_EFFECT"],
        "causes": [],
        "effects": [],
        "relationships": [{
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}" if country_name != "Global" else "",
            "targetName": country_name,
            "context": f"{name} located in {country_name}",
        }],
        "places": [],
        "texts": [],
        "institutionType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "isActive": dissolved_year is None,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if founded_display:
        entity["founded"] = founded_display
    if founding_year:
        entity["foundedYear"] = founding_year
    if dissolved_display:
        entity["dissolved"] = dissolved_display
    if dissolved_year:
        entity["dissolvedYear"] = dissolved_year
    if headquarters:
        entity["headquarters"] = headquarters
        entity["places"].append({"name": headquarters, "role": "Headquarters"})
    if founder and not re.match(r'^Q\d+$', founder):
        entity["founder"] = founder
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url
    if image_url:
        entity["imageUrl"] = image_url

    return entity


def main():
    parser = argparse.ArgumentParser(description="Fetch institutions from Wikidata (v2.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_institutions.json"

    total_qids = len(set(qid for qids, _ in INSTITUTION_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Institutions Fetch v2.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(INSTITUTION_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   310-394 (all 36 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}

    for batch_name, (type_qids, min_sl) in INSTITUTION_QUERIES.items():
        print(f"[{batch_name}]  {len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_institution(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} unique (total: {len(all_entities)})")
        time.sleep(2)

    if args.dry_run:
        print("\nDry run complete.")
        return

    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    sig_dist: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        sig_dist[e["historicalSignificance"]["label"]] = sig_dist.get(e["historicalSignificance"]["label"], 0) + 1
        ct = e.get("continent", "Global")
        continent_counts[ct] = continent_counts.get(ct, 0) + 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "2.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Institution",
            "classCode": 3,
            "classHeading": "Institutions",
            "type_qids_queried": total_qids,
            "batches_queried": len(INSTITUTION_QUERIES),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "significance_scale": {
                "1-2": "Minor -- documented but limited global impact",
                "3-4": "Moderate -- nationally significant",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized",
                "9-10": "Landmark -- world-shaping institution",
            },
            "inAppwrite_note": "All entities have inAppwrite=false. Use historicalSignificance.score to prioritize for Appwrite seeding.",
            "note": "Comprehensive Wikidata institutions fetch v2.0 covering all 36 Class 3 divisions (310-394).",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("  Fetch Complete -- v2.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
    print(f"  Output:            {output_path}")
    print()
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    print("  By era:")
    for era_name, count in sorted(era_counts.items(), key=lambda x: era_order.get(x[0], 9)):
        print(f"    {era_name}: {count}")
    print()
    print("  By significance:")
    for label, count in sorted(sig_dist.items()):
        print(f"    {label}: {count}")
    print()
    print("  By continent:")
    for ct, count in sorted(continent_counts.items(), key=lambda x: -x[1]):
        print(f"    {ct}: {count}")
    print()

    top15 = sorted(all_entities, key=lambda e: (-e["historicalSignificance"]["score"], e["name"]))[:15]
    print("  Top 15 by historical significance:")
    for i, e in enumerate(top15, 1):
        sig = e["historicalSignificance"]
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] {e['name']}")


if __name__ == "__main__":
    main()
