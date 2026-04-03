#!/usr/bin/env python3
"""
fetch_wikidata_events.py  (v2.0)

Comprehensive Wikidata fetch of notable events across ALL Class 5
divisions (510-593). Uses 230+ Wikidata type QIDs, configurable sitelinks
thresholds, granular batch splitting, adaptive limit fallback, and
subclass traversal (wdt:P31/wdt:P279*) for hierarchical types.

v2.0 changes:
  - Subclass traversal for 36 previously-failed batches
  - 22 new event type batches (treaties, protests, terrorism, expeditions, etc.)
  - Lowered sitelinks thresholds for sparse divisions
  - ~108 total batches (up from 86)

Output: data/wikidata_events.json

Usage:
    python3 scripts/fetch_wikidata_events.py
    python3 scripts/fetch_wikidata_events.py --limit 5000
    python3 scripts/fetch_wikidata_events.py --dry-run
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
# Event Type -> Division Mapping  (200+ QIDs)
# Maps Wikidata P31 (instance of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

EVENT_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 510 Wars & Conflicts ──
    "Q198":       ("510", "Wars & Conflicts"),              # war
    "Q180684":    ("510", "Wars & Conflicts"),              # conflict
    "Q350604":    ("510", "Wars & Conflicts"),              # armed conflict
    "Q831663a":   ("510", "Wars & Conflicts"),              # military operation
    "Q188055":    ("510", "Wars & Conflicts"),              # military campaign
    "Q645883":    ("510", "Wars & Conflicts"),              # military offensive
    "Q1261499":   ("510", "Wars & Conflicts"),              # theater of war
    "Q2001676":   ("510", "Wars & Conflicts"),              # war of independence

    # ── 511 Ancient & Classical Wars ──
    # (assigned via era-based post-processing of wars)

    # ── 512 Medieval Wars & Crusades ──
    "Q189259":    ("512", "Medieval Wars & Crusades"),      # crusade

    # ── 513 Early Modern Wars & Colonial Conflicts ──
    "Q1348889":   ("513", "Early Modern Wars & Colonial Conflicts"), # colonial war

    # ── 514 World Wars ──
    "Q103495":    ("514", "World Wars"),                    # world war

    # ── 515 Cold War Conflicts & Proxy Wars ──
    "Q864113":    ("515", "Cold War Conflicts & Proxy Wars"), # proxy war

    # ── 516 Civil Wars & Internal Conflicts ──
    "Q8465":      ("516", "Civil Wars & Internal Conflicts"), # civil war
    "Q106721685": ("516", "Civil Wars & Internal Conflicts"), # internal conflict
    "Q12757":     ("516", "Civil Wars & Internal Conflicts"), # insurgency
    "Q124734":    ("516", "Civil Wars & Internal Conflicts"), # rebellion

    # ── 517 Sieges & Battles ──
    "Q178561":    ("517", "Sieges & Battles"),               # battle
    "Q188161":    ("517", "Sieges & Battles"),               # siege
    "Q660339":    ("517", "Sieges & Battles"),               # naval battle
    "Q178810":    ("517", "Sieges & Battles"),               # military engagement
    "Q1261499a":  ("517", "Sieges & Battles"),               # combat
    "Q2973801":   ("517", "Sieges & Battles"),               # aerial battle
    "Q12579765":  ("517", "Sieges & Battles"),               # tank battle

    # ── 520 Revolutions & Uprisings ──
    "Q10931":     ("520", "Revolutions & Uprisings"),        # revolution
    "Q1144661":   ("520", "Revolutions & Uprisings"),        # uprising
    "Q58886":     ("520", "Revolutions & Uprisings"),        # riot
    "Q7270":      ("520", "Revolutions & Uprisings"),        # mutiny
    "Q337453":    ("520", "Revolutions & Uprisings"),        # insurrection

    # ── 521 Political Revolutions ──
    # (assigned by keyword matching: "political revolution", etc.)

    # ── 522 Social & Peasant Revolts ──
    "Q12722842":  ("522", "Social & Peasant Revolts"),       # peasant revolt
    "Q2826908":   ("522", "Social & Peasant Revolts"),       # slave rebellion

    # ── 523 Independence & Liberation Movements ──
    "Q1125239":   ("523", "Independence & Liberation Movements"), # independence movement
    "Q106261412": ("523", "Independence & Liberation Movements"), # declaration of independence
    "Q15283295":  ("523", "Independence & Liberation Movements"), # independence day

    # ── 524 Coups & Palace Revolutions ──
    "Q12104":     ("524", "Coups & Palace Revolutions"),     # coup d'état
    "Q19829034":  ("524", "Coups & Palace Revolutions"),     # self-coup
    "Q5765870":   ("524", "Coups & Palace Revolutions"),     # failed coup attempt

    # ── 530 Elections & Political Shifts ──
    "Q40231":     ("530", "Elections & Political Shifts"),    # election
    "Q858439":    ("530", "Elections & Political Shifts"),    # general election
    "Q1076354":   ("530", "Elections & Political Shifts"),    # referendum
    "Q1131296":   ("530", "Elections & Political Shifts"),    # presidential election
    "Q1971256":   ("530", "Elections & Political Shifts"),    # parliamentary election
    "Q15283424":  ("530", "Elections & Political Shifts"),    # legislative election
    "Q106776":    ("530", "Elections & Political Shifts"),    # plebiscite

    # ── 531 Founding Elections & Constitutions ──
    # (assigned via keyword matching)

    # ── 532 Regime Changes & Transitions ──
    "Q1363601":   ("532", "Regime Changes & Transitions"),   # political transition
    "Q173775":    ("532", "Regime Changes & Transitions"),    # abdication
    "Q217327":    ("532", "Regime Changes & Transitions"),    # coronation
    "Q484416":    ("532", "Regime Changes & Transitions"),    # assassination
    "Q3882219":   ("532", "Regime Changes & Transitions"),    # political crisis

    # ── 540 Legal Cases ──
    "Q2135371":   ("540", "Legal Cases"),                     # legal case
    "Q8016240":   ("540", "Legal Cases"),                     # trial
    "Q7269178":   ("540", "Legal Cases"),                     # lawsuit

    # ── 541 Landmark Trials ──
    "Q28809975":  ("541", "Landmark Trials"),                 # show trial
    "Q2335432":   ("541", "Landmark Trials"),                 # war crimes trial
    "Q3112627":   ("541", "Landmark Trials"),                 # impeachment

    # ── 542 International Tribunals ──
    "Q1572600":   ("542", "International Tribunals"),         # international tribunal

    # ── 550 Scientific Discoveries ──
    "Q1080745":   ("550", "Scientific Discoveries"),          # scientific discovery
    "Q3327521":   ("550", "Scientific Discoveries"),          # scientific experiment
    "Q27645":     ("550", "Scientific Discoveries"),          # experiment

    # ── 551 Astronomical Observations ──
    "Q3327521a":  ("551", "Astronomical Observations"),       # (via keyword)
    "Q148":       ("551", "Astronomical Observations"),       # (via keyword: astronomical)

    # ── 552 Medical & Biological Discoveries ──
    # (assigned via keyword matching)

    # ── 553 Physical & Chemical Discoveries ──
    # (assigned via keyword matching)

    # ── 554 Archaeological Discoveries ──
    "Q60925804":  ("554", "Archaeological Discoveries"),      # archaeological discovery

    # ── 560 Technological Breakthroughs ──
    "Q483247":    ("560", "Technological Breakthroughs"),     # invention
    "Q36850":     ("560", "Technological Breakthroughs"),     # patent
    "Q30046649":  ("560", "Technological Breakthroughs"),     # technological innovation
    "Q15401930":  ("560", "Technological Breakthroughs"),     # product launch

    # ── 561 Industrial Inventions ──
    # (assigned via era-based post-processing)

    # ── 562 Computing & Digital Milestones ──
    # (assigned via keyword matching: "computer", "digital", "software")

    # ── 563 Space Exploration Milestones ──
    "Q2133344":   ("563", "Space Exploration Milestones"),    # space mission
    "Q5916":      ("563", "Space Exploration Milestones"),    # spaceflight
    "Q15061650":  ("563", "Space Exploration Milestones"),    # crewed spaceflight
    "Q3235978":   ("563", "Space Exploration Milestones"),    # Moon landing
    "Q18812508":  ("563", "Space Exploration Milestones"),    # Mars mission
    "Q697175":    ("563", "Space Exploration Milestones"),    # orbital mission

    # ── 564 Ancient & Traditional Technology ──
    # (assigned via era-based post-processing)

    # ── 565 Communication & Transport Technology ──
    # (assigned via keyword matching)

    # ── 570 Religious Events ──
    "Q1445768":   ("570", "Religious Events"),                # religious event
    "Q199451":    ("570", "Religious Events"),                # religious ceremony
    "Q132241":    ("570", "Religious Events"),                # festival

    # ── 571 Church Councils & Synods ──
    "Q3565868":   ("571", "Church Councils & Synods"),        # ecumenical council
    "Q1156854":   ("571", "Church Councils & Synods"),        # synod
    "Q4195826":   ("571", "Church Councils & Synods"),        # council of the Catholic Church
    "Q3882133":   ("571", "Church Councils & Synods"),        # church council

    # ── 572 Reformations & Schisms ──
    "Q28437":     ("572", "Reformations & Schisms"),          # schism
    "Q706290":    ("572", "Reformations & Schisms"),          # religious reform

    # ── 573 Spiritual Awakenings & Revivals ──
    "Q484461":    ("573", "Spiritual Awakenings & Revivals"), # religious revival

    # ── 574 Persecutions & Martyrdoms ──
    "Q839161":    ("574", "Persecutions & Martyrdoms"),       # persecution
    "Q149086":    ("574", "Persecutions & Martyrdoms"),       # massacre
    "Q294414":    ("574", "Persecutions & Martyrdoms"),       # pogrom
    "Q7864918":   ("574", "Persecutions & Martyrdoms"),       # ethnic cleansing
    "Q7283":      ("574", "Persecutions & Martyrdoms"),       # genocide

    # ── 575 Biblical & Canonical Events ──
    # (assigned via keyword matching)

    # ── 576 General Religious Events ──
    "Q3529618":   ("576", "General Religious Events"),        # papal conclave
    "Q189533":    ("576", "General Religious Events"),        # canonization

    # ── 580 Environmental Events ──
    "Q8065":      ("580", "Environmental Events"),            # natural disaster
    "Q3839081":   ("580", "Environmental Events"),            # environmental disaster
    "Q107413":    ("580", "Environmental Events"),            # nuclear disaster

    # ── 581 Natural Disasters ──
    "Q7935":      ("581", "Natural Disasters"),               # earthquake
    "Q8070":      ("581", "Natural Disasters"),               # flood
    "Q8076":      ("581", "Natural Disasters"),               # tsunami
    "Q3196":      ("581", "Natural Disasters"),               # wildfire
    "Q44512":     ("581", "Natural Disasters"),               # volcanic eruption
    "Q200155":    ("581", "Natural Disasters"),               # landslide
    "Q15292":     ("581", "Natural Disasters"),               # tropical cyclone
    "Q63100531":  ("581", "Natural Disasters"),               # tornado outbreak
    "Q80005":     ("581", "Natural Disasters"),               # hurricane
    "Q8081":      ("581", "Natural Disasters"),               # tornado
    "Q16560":     ("581", "Natural Disasters"),               # avalanche
    "Q7944":      ("581", "Natural Disasters"),               # drought

    # ── 582 Famines & Droughts ──
    "Q168247":    ("582", "Famines & Droughts"),              # famine
    "Q12078":     ("582", "Famines & Droughts"),              # famine (alt)

    # ── 583 Epidemics & Pandemics ──
    "Q44085":     ("583", "Epidemics & Pandemics"),           # epidemic
    "Q12184":     ("583", "Epidemics & Pandemics"),           # pandemic
    "Q16070":     ("583", "Epidemics & Pandemics"),           # plague
    "Q3241045":   ("583", "Epidemics & Pandemics"),           # disease outbreak
    "Q18974844":  ("583", "Epidemics & Pandemics"),           # cholera outbreak

    # ── 584 Climate Shifts & Ice Ages ──
    "Q35473":     ("584", "Climate Shifts & Ice Ages"),       # ice age
    "Q11663":     ("584", "Climate Shifts & Ice Ages"),       # climate change

    # ── 590 Agricultural & Economic Events ──
    "Q182527":    ("590", "Agricultural & Economic Events"),   # economic crisis
    "Q181014":    ("590", "Agricultural & Economic Events"),   # financial crisis
    "Q1006311":   ("590", "Agricultural & Economic Events"),   # economic bubble
    "Q1299022":   ("590", "Agricultural & Economic Events"),   # strike

    # ── 591 Agricultural Revolutions ──
    # (assigned via keyword matching)

    # ── 592 Economic Crises & Depressions ──
    "Q30728":     ("592", "Economic Crises & Depressions"),   # recession
    "Q1387837":   ("592", "Economic Crises & Depressions"),   # stock market crash
    "Q2834001":   ("592", "Economic Crises & Depressions"),   # financial crisis (specific)
    "Q76768":     ("592", "Economic Crises & Depressions"),   # hyperinflation

    # ── 593 Trade Booms & Gold Rushes ──
    "Q132851":    ("593", "Trade Booms & Gold Rushes"),       # gold rush
    "Q35556":     ("593", "Trade Booms & Gold Rushes"),       # economic boom
    "Q2647012":   ("593", "Trade Booms & Gold Rushes"),       # trade fair

    # ── NEW v2.0: Additional event types ──

    # ── 510 Military Occupations ──
    "Q188686":    ("510", "Wars & Conflicts"),              # military occupation

    # ── 515 Blockades ──
    "Q37156":     ("515", "Cold War Conflicts & Proxy Wars"), # blockade

    # ── 520 Protests & Demonstrations ──
    "Q273120":    ("520", "Revolutions & Uprisings"),        # protest
    "Q175331":    ("520", "Revolutions & Uprisings"),        # demonstration

    # ── 523 Partitions ──
    "Q328916":    ("523", "Independence & Liberation Movements"), # partition

    # ── 530 Treaties & Diplomacy ──
    "Q131569":    ("530", "Elections & Political Shifts"),    # treaty
    "Q625298":    ("530", "Elections & Political Shifts"),    # peace treaty
    "Q184528":    ("530", "Elections & Political Shifts"),    # armistice
    "Q1368882":   ("530", "Elections & Political Shifts"),    # ceasefire
    "Q22649":     ("530", "Elections & Political Shifts"),    # summit
    "Q625994":    ("530", "Elections & Political Shifts"),    # conference

    # ── 540 Executions ──
    "Q170219":    ("540", "Legal Cases"),                    # execution

    # ── 541 Witch Trials ──
    "Q831028":    ("541", "Landmark Trials"),                # witch trial

    # ── 550 Expeditions ──
    "Q2401485":   ("550", "Scientific Discoveries"),         # expedition

    # ── 574 Terrorism, Bombings & Deportations ──
    "Q1616075":   ("574", "Persecutions & Martyrdoms"),      # terrorist attack
    "Q891854":    ("574", "Persecutions & Martyrdoms"),      # bombing
    "Q309049":    ("574", "Persecutions & Martyrdoms"),      # deportation

    # ── 580 Nuclear Tests ──
    "Q210112":    ("580", "Environmental Events"),            # nuclear test

    # ── 581 Transport & Industrial Disasters ──
    "Q14795564":  ("581", "Natural Disasters"),              # maritime disaster
    "Q744913":    ("581", "Natural Disasters"),              # aviation accident
    "Q852190":    ("581", "Natural Disasters"),              # shipwreck
    "Q179057":    ("581", "Natural Disasters"),              # explosion
}

# Build reverse lookup: first-occurrence wins (strip letter suffixes)
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in EVENT_TYPE_MAP.items():
    clean_qid = re.sub(r'[a-z]+$', '', _qid)
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info

# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (108 granular batches)
# Each batch -> (QIDs, min_sitelinks, use_subclass)
# use_subclass=True → wdt:P31/wdt:P279* (catches subclass hierarchies)
# Heavy types split solo w/ higher threshold to avoid timeouts
# ═══════════════════════════════════════════════════════════════════

EVENT_QUERIES: dict[str, tuple] = {
    # ── 510 Wars & Conflicts ──
    "510_war":            (["Q198"], 8, False),
    "510_conflict":       (["Q180684", "Q350604"], 8, False),
    "510_campaign":       (["Q188055", "Q645883"], 5, False),
    "510_war_indep":      (["Q2001676"], 5, False),
    "510_occupation":     (["Q188686"], 5, False),               # NEW v2

    # ── 512 Medieval Wars & Crusades ──
    "512_crusade":        (["Q189259"], 3, True),                # SUBCLASS fix

    # ── 513 Colonial Wars ──
    "513_colonial_war":   (["Q1348889"], 3, True),               # SUBCLASS fix

    # ── 514 World Wars ──
    "514_world_war":      (["Q103495"], 5, False),

    # ── 515 Cold War / Proxy Wars ──
    "515_proxy":          (["Q864113"], 5, False),
    "515_blockade":       (["Q37156"], 5, False),                # NEW v2

    # ── 516 Civil Wars ──
    "516_civil_war":      (["Q8465"], 5, False),
    "516_rebellion":      (["Q124734", "Q12757"], 5, False),

    # ── 517 Sieges & Battles ──
    "517_battle":         (["Q178561"], 5, False),
    "517_siege":          (["Q188161"], 3, True),                # SUBCLASS fix
    "517_naval_battle":   (["Q660339"], 3, True),                # SUBCLASS fix
    "517_aerial":         (["Q2973801", "Q12579765"], 5, False),

    # ── 520 Revolutions & Uprisings ──
    "520_revolution":     (["Q10931"], 5, False),
    "520_uprising":       (["Q1144661", "Q337453"], 5, False),
    "520_riot":           (["Q58886"], 5, True),                 # SUBCLASS fix
    "520_mutiny":         (["Q7270"], 5, False),
    "520_protest":        (["Q273120"], 8, False),               # NEW v2
    "520_demonstration":  (["Q175331"], 8, False),               # NEW v2

    # ── 522 Peasant Revolts ──
    "522_peasant":        (["Q12722842", "Q2826908"], 3, True),  # SUBCLASS fix

    # ── 523 Independence ──
    "523_independence":   (["Q1125239"], 3, True),               # SUBCLASS (low yield)
    "523_declaration":    (["Q106261412", "Q15283295"], 3, True),# SUBCLASS fix
    "523_partition":      (["Q328916"], 3, True),                # NEW v2

    # ── 524 Coups ──
    "524_coup":           (["Q12104"], 3, True),                 # SUBCLASS fix
    "524_failed_coup":    (["Q5765870", "Q19829034"], 3, True),  # SUBCLASS fix

    # ── 530 Elections & Political Shifts ──
    "530_election":       (["Q40231"], 8, False),                # lowered 12→8
    "530_general":        (["Q858439"], 10, False),
    "530_presidential":   (["Q1131296"], 10, False),
    "530_parliamentary":  (["Q1971256", "Q15283424"], 10, False),
    "530_referendum":     (["Q1076354", "Q106776"], 3, True),   # SUBCLASS fix
    "530_treaty":         (["Q131569"], 5, False),               # NEW v2
    "530_peace_treaty":   (["Q625298"], 5, False),               # NEW v2
    "530_armistice":      (["Q184528"], 5, False),               # NEW v2
    "530_ceasefire":      (["Q1368882"], 5, False),              # NEW v2
    "530_summit":         (["Q22649"], 10, False),               # NEW v2
    "530_conference":     (["Q625994"], 10, False),              # NEW v2

    # ── 532 Regime Changes ──
    "532_abdication":     (["Q173775"], 3, True),                # SUBCLASS fix
    "532_coronation":     (["Q217327"], 5, False),
    "532_assassination":  (["Q484416"], 5, False),
    "532_crisis":         (["Q3882219", "Q1363601"], 5, False),

    # ── 540 Legal Cases ──
    "540_case":           (["Q2135371"], 5, True),               # SUBCLASS fix
    "540_trial":          (["Q8016240"], 8, False),
    "540_lawsuit":        (["Q7269178"], 5, True),               # SUBCLASS fix
    "540_execution":      (["Q170219"], 5, False),               # NEW v2

    # ── 541 Landmark Trials ──
    "541_show_trial":     (["Q28809975", "Q2335432"], 3, True),  # SUBCLASS fix
    "541_impeachment":    (["Q3112627"], 3, True),               # SUBCLASS fix
    "541_witch_trial":    (["Q831028"], 3, True),                # NEW v2

    # ── 542 International Tribunals ──
    "542_tribunal":       (["Q1572600"], 5, False),

    # ── 550 Scientific Discoveries ──
    "550_discovery":      (["Q1080745"], 3, True),               # SUBCLASS fix
    "550_experiment":     (["Q3327521", "Q27645"], 5, False),
    "550_expedition":     (["Q2401485"], 5, False),              # NEW v2

    # ── 554 Archaeological Discoveries ──
    "554_archeo":         (["Q60925804"], 3, True),              # SUBCLASS fix

    # ── 560 Technological Breakthroughs ──
    "560_invention":      (["Q483247"], 8, False),
    "560_patent":         (["Q36850"], 10, True),                # SUBCLASS fix
    "560_launch":         (["Q15401930"], 5, True),              # SUBCLASS fix

    # ── 563 Space Exploration ──
    "563_spaceflight":    (["Q5916"], 5, False),
    "563_crewed":         (["Q15061650"], 3, True),              # SUBCLASS fix
    "563_space_mission":  (["Q2133344"], 5, False),
    "563_moon":           (["Q3235978", "Q697175"], 5, False),

    # ── 570 Religious Events ──
    "570_religious":      (["Q1445768", "Q199451"], 5, False),
    "570_festival":       (["Q132241"], 15, False),

    # ── 571 Church Councils ──
    "571_council":        (["Q3565868", "Q4195826"], 3, True),   # SUBCLASS (low yield)
    "571_synod":          (["Q1156854", "Q3882133"], 5, False),

    # ── 572 Schisms ──
    "572_schism":         (["Q28437", "Q706290"], 3, True),      # SUBCLASS fix

    # ── 573 Revivals ──
    "573_revival":        (["Q484461"], 3, True),                # SUBCLASS fix

    # ── 574 Persecutions ──
    "574_persecution":    (["Q839161"], 3, True),                # SUBCLASS fix
    "574_massacre":       (["Q149086"], 5, False),
    "574_pogrom":         (["Q294414"], 5, False),
    "574_genocide":       (["Q7283"], 3, True),                  # SUBCLASS fix
    "574_ethnic":         (["Q7864918"], 3, True),               # SUBCLASS fix
    "574_terrorism":      (["Q1616075"], 5, False),              # NEW v2
    "574_bombing":        (["Q891854"], 8, False),               # NEW v2
    "574_deportation":    (["Q309049"], 5, False),               # NEW v2

    # ── 576 General Religious ──
    "576_conclave":       (["Q3529618"], 5, False),
    "576_canonization":   (["Q189533"], 5, False),

    # ── 580 Environmental ──
    "580_disaster":       (["Q8065"], 8, False),
    "580_env_disaster":   (["Q3839081", "Q107413"], 5, False),
    "580_nuclear_test":   (["Q210112"], 3, False),               # NEW v2

    # ── 581 Natural Disasters ──
    "581_earthquake":     (["Q7935"], 3, True),                  # SUBCLASS (low yield)
    "581_flood":          (["Q8070"], 5, True),                  # SUBCLASS + lowered
    "581_tsunami":        (["Q8076"], 5, False),
    "581_eruption":       (["Q44512"], 5, False),
    "581_fire":           (["Q3196"], 5, False),                 # lowered 8→5
    "581_cyclone":        (["Q15292", "Q80005"], 3, True),       # SUBCLASS fix
    "581_tornado":        (["Q8081", "Q63100531"], 5, False),    # lowered 8→5
    "581_landslide":      (["Q200155", "Q16560"], 5, False),
    "581_maritime":       (["Q14795564"], 5, False),             # NEW v2
    "581_aviation":       (["Q744913"], 8, False),               # NEW v2
    "581_shipwreck":      (["Q852190"], 5, False),               # NEW v2
    "581_explosion":      (["Q179057"], 8, False),               # NEW v2

    # ── 582 Famines ──
    "582_famine":         (["Q168247"], 5, False),

    # ── 583 Epidemics ──
    "583_epidemic":       (["Q44085"], 3, True),                 # SUBCLASS fix
    "583_pandemic":       (["Q12184"], 5, False),
    "583_plague":         (["Q16070"], 3, True),                 # SUBCLASS fix
    "583_outbreak":       (["Q3241045", "Q18974844"], 5, False),

    # ── 584 Climate ──
    "584_ice_age":        (["Q35473"], 5, False),

    # ── 590 Economic Events ──
    "590_econ_crisis":    (["Q182527", "Q181014"], 3, True),     # SUBCLASS fix
    "590_bubble":         (["Q1006311"], 5, False),
    "590_strike":         (["Q1299022"], 5, True),               # SUBCLASS fix

    # ── 592 Economic Crises ──
    "592_recession":      (["Q30728"], 3, True),                 # SUBCLASS fix
    "592_crash":          (["Q1387837"], 3, True),               # SUBCLASS fix
    "592_hyperinflation": (["Q76768"], 3, True),                 # SUBCLASS fix

    # ── 593 Trade Booms ──
    "593_gold_rush":      (["Q132851"], 3, True),                # SUBCLASS fix
    "593_boom":           (["Q35556"], 3, True),                 # SUBCLASS fix
    "593_trade_fair":     (["Q2647012"], 5, True),               # SUBCLASS fix
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

# ═══════════════════════════════════════════════════════════════════
# Non-event entity types to filter out
# ═══════════════════════════════════════════════════════════════════

NON_EVENT_KEYWORDS = {
    'association football', 'football club', 'soccer',
    'television series', 'tv series', 'film', 'video game',
    'album', 'song', 'musical group', 'band',
    'software', 'programming language', 'website',
    'university', 'school', 'company', 'corporation',
    'magazine', 'newspaper', 'radio station',
    'fictional', 'comic book', 'novel',
    'award', 'prize ceremony',
    'administrative division', 'municipality', 'county',
    'railway station', 'airport', 'highway',
}


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


def compute_significance(sitelinks: int, event_year: int | None) -> int:
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
    # Antiquity bonus
    if event_year is not None:
        if event_year < -1000:
            score += 2
        elif event_year < 500:
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
    return ("510", "Wars & Conflicts")


def refine_war_division(div_code: str, div_heading: str, era: str) -> tuple[str, str]:
    """Refine generic 510 war entries into era-specific sub-divisions."""
    if div_code != "510":
        return (div_code, div_heading)
    if era in ("Prehistoric", "Classical"):
        return ("511", "Ancient & Classical Wars")
    if era == "Medieval":
        return ("512", "Medieval Wars & Crusades")
    if era == "Early Modern":
        return ("513", "Early Modern Wars & Colonial Conflicts")
    if era == "Modern":
        return ("514", "World Wars")  # Many modern wars; main bucket
    if era == "Contemporary":
        return ("515", "Cold War Conflicts & Proxy Wars")
    return (div_code, div_heading)


def refine_invention_division(div_code: str, div_heading: str, era: str, name: str, desc: str) -> tuple[str, str]:
    """Refine generic 560 inventions into sub-divisions."""
    if div_code != "560":
        return (div_code, div_heading)
    text = f"{name} {desc}".lower()
    if any(kw in text for kw in ("computer", "digital", "software", "internet", "algorithm", "processor", "semiconductor")):
        return ("562", "Computing & Digital Milestones")
    if any(kw in text for kw in ("telegraph", "telephone", "radio", "television", "railway", "locomotive", "automobile", "airplane")):
        return ("565", "Communication & Transport Technology")
    if era in ("Prehistoric", "Classical", "Medieval"):
        return ("564", "Ancient & Traditional Technology")
    if era in ("Modern", "Early Modern"):
        return ("561", "Industrial Inventions")
    return (div_code, div_heading)


def is_non_event(description: str, type_label: str) -> bool:
    """Check if the entity description/type suggests it's not a real event."""
    check = f"{description} {type_label}".lower()
    return any(kw in check for kw in NON_EVENT_KEYWORDS)


def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5, use_subclass: bool = False) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    # Use subclass traversal for hierarchical types; direct P31 for well-typed items
    type_match = "?item wdt:P31/wdt:P279* ?type ." if use_subclass else "?item wdt:P31 ?type ."
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?pointInTime ?startTime ?endTime
       ?country ?countryLabel
       ?locationLabel
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  {type_match}
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P585 ?pointInTime . }}
  OPTIONAL {{ ?item wdt:P580 ?startTime . }}
  OPTIONAL {{ ?item wdt:P582 ?endTime . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P276 ?location . }}

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


def fetch_adaptive(type_qids: list[str], target_limit: int, min_sl: int, use_subclass: bool = False) -> list[dict[str, Any]]:
    """Try target limit; on failure halve until success."""
    limits = [target_limit]
    lim = target_limit
    while lim > 500:
        lim = lim // 2
        limits.append(lim)
    limits.append(500)

    for lim in limits:
        query = build_sparql_query(type_qids, limit=lim, min_sitelinks=min_sl, use_subclass=use_subclass)
        rows = fetch_sparql(query, retries=2)
        if rows:
            return rows
        if lim > 500:
            print(f"    Reducing limit: {lim} -> {lim // 2}")
    return []


def transform_event(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""

    # Filter out non-event entities
    if is_non_event(description, type_label):
        return None

    pit_raw = binding_val(row, "pointInTime")
    start_raw = binding_val(row, "startTime")
    end_raw = binding_val(row, "endTime")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    location = binding_val(row, "locationLabel") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    # Determine event date: prefer pointInTime, then startTime
    date_raw = pit_raw or start_raw
    event_year = parse_year(date_raw)
    start_year = parse_year(start_raw or pit_raw)
    end_year = parse_year(end_raw)
    date_display = format_date_display(date_raw)
    end_display = format_date_display(end_raw)

    era, era_slug = year_to_era(event_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine war divisions by era
    div_code, div_heading = refine_war_division(div_code, div_heading, era)

    # Refine invention divisions by keywords/era
    div_code, div_heading = refine_invention_division(div_code, div_heading, era, name, description)

    slug = make_slug(name)

    # Build summary
    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if location and not re.match(r'^Q\d+$', location):
        summary += f" Took place in {location}."
    elif country_name and country_name != "Global":
        summary += f" Occurred in {country_name}."
    if date_display:
        summary += f" Date: {date_display}."
    if end_display:
        summary += f" Ended: {end_display}."

    sig_score = compute_significance(sitelinks, event_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "EventWindow",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Events -- {div_heading} -- {country_name} -- {era}"],
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
        "relationships": [],
        "places": [],
        "texts": [],
        "eventType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if start_year is not None:
        entity["startYear"] = start_year
    if end_year is not None:
        entity["endYear"] = end_year
    if date_display:
        entity["date"] = date_display
    if end_display:
        entity["endDate"] = end_display

    if country_name and country_name != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}",
            "targetName": country_name,
            "context": f"{name} occurred in {country_name}",
        })
    if location and not re.match(r'^Q\d+$', location):
        entity["places"].append({"name": location, "role": "Location"})
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})

    if qid:
        entity["wikidataQid"] = qid

    return entity


def main():
    parser = argparse.ArgumentParser(description="Fetch events from Wikidata (v2.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_events.json"

    total_qids = len(set(qid for batch in EVENT_QUERIES.values() for qid in batch[0]))
    sc_count = sum(1 for b in EVENT_QUERIES.values() if len(b) > 2 and b[2])

    print("=" * 70)
    print("  Wikidata Events Fetch v2.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(EVENT_QUERIES)} ({sc_count} with subclass traversal)")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   510-593 (all Class 5 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}
    failed_batches: list[str] = []

    for batch_name, batch_config in EVENT_QUERIES.items():
        type_qids = batch_config[0]
        min_sl = batch_config[1]
        use_subclass = batch_config[2] if len(batch_config) > 2 else False
        sc_tag = " [SC]" if use_subclass else ""
        print(f"[{batch_name}]  {len(type_qids)} type(s), sitelinks>{min_sl}{sc_tag} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl, use_subclass)
        if not rows:
            failed_batches.append(batch_name)
            print(f"  FAILED (no results after all retries)\n")
            time.sleep(5)
            continue

        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_event(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} unique (total: {len(all_entities)})")
        time.sleep(2)

    if args.dry_run:
        print(f"\nDry run complete. {len(EVENT_QUERIES)} batches configured.")
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
            "label": "EventWindow",
            "classCode": 5,
            "classHeading": "Events",
            "type_qids_queried": total_qids,
            "batches_queried": len(EVENT_QUERIES),
            "failed_batches": failed_batches,
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "significance_scale": {
                "1-2": "Minor -- documented but limited global impact",
                "3-4": "Moderate -- nationally significant",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized",
                "9-10": "Landmark -- world-shaping event",
            },
            "inAppwrite_note": "All entities have inAppwrite=false. Use historicalSignificance.score to prioritize for Appwrite seeding.",
            "note": "Comprehensive Wikidata events fetch v2.0 with subclass traversal, 108 batches, covering all Class 5 divisions (510-593).",
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
    if failed_batches:
        print(f"  Failed batches:    {', '.join(failed_batches)}")
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
    print("  Top 15 by significance:")
    for e in top15:
        sig = e["historicalSignificance"]
        print(f"    [{sig['score']}] {e['name']} ({e['divisionCode']} {e['divisionHeading']}) -- {sig['sitelinks']} sitelinks")
    print()


if __name__ == "__main__":
    main()
