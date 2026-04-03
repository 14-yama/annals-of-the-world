#!/usr/bin/env python3
"""
fetch_wikidata_ideas_other.py  (v1.0)

Dedicated Wikidata fetch for Class 1 — Ideas (Other): Economic, Scientific,
Technological, Religious, Cultural, Environmental, Artistic theories and
paradigms. Covers ALL divisions 110-173 with 250+ Wikidata type QIDs,
P31 AND P279 (subclass) strategies, adaptive limit fallback, keyword-based
sub-division refinement, and progressive saving.

Enhanced over the combined ideas script with:
  - 120+ batches (vs ~60 Class 1 batches in combined script)
  - P279 subclass queries for thin divisions
  - Lower sitelink thresholds (>=2) for gap-filling
  - Additional discovery QIDs per division

Output: data/wikidata_ideas_other.json

Usage:
    python3 scripts/fetch_wikidata_ideas_other.py
    python3 scripts/fetch_wikidata_ideas_other.py --limit 5000
    python3 scripts/fetch_wikidata_ideas_other.py --dry-run
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
# Class 1 Ideas Type -> Division Mapping  (250+ QIDs)
# Maps Wikidata P31 (instance-of) QIDs to call-number divisions 110-173
# ═══════════════════════════════════════════════════════════════════

IDEAS_OTHER_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ════════════════════════════════════════════
    # 110 Economic Theories & Systems
    # ════════════════════════════════════════════
    "Q8134":       ("110", "Economic Theories & Systems"),          # economics
    "Q186247":     ("110", "Economic Theories & Systems"),          # economic theory
    "Q2979973":    ("110", "Economic Theories & Systems"),          # economic school of thought
    "Q11042":      ("110", "Economic Theories & Systems"),          # economic system
    "Q182790":     ("110", "Economic Theories & Systems"),          # economic policy
    "Q12140182":   ("110", "Economic Theories & Systems"),          # economic ideology
    "Q47495990":   ("110", "Economic Theories & Systems"),          # school of economic thought
    "Q188924":     ("110", "Economic Theories & Systems"),          # economic model
    "Q1778667":    ("110", "Economic Theories & Systems"),          # economic concept
    "Q170584":     ("110", "Economic Theories & Systems"),          # project/economic project

    # ── 111 Mercantilism & Trade Theory ──
    "Q131735":     ("111", "Mercantilism & Trade Theory"),          # mercantilism
    "Q846706":     ("111", "Mercantilism & Trade Theory"),          # trade policy
    "Q220338":     ("111", "Mercantilism & Trade Theory"),          # protectionism
    "Q208642":     ("111", "Mercantilism & Trade Theory"),          # commercial policy
    "Q17517":      ("111", "Mercantilism & Trade Theory"),          # trade
    "Q601401":     ("111", "Mercantilism & Trade Theory"),          # economic doctrine

    # ── 112 Classical & Neoclassical Economics ──
    "Q83267":      ("112", "Classical & Neoclassical Economics"),   # classical economics
    "Q190375":     ("112", "Classical & Neoclassical Economics"),   # neoclassical economics
    "Q35591":      ("112", "Classical & Neoclassical Economics"),   # capitalism
    "Q202640":     ("112", "Classical & Neoclassical Economics"),   # laissez-faire
    "Q327960":     ("112", "Classical & Neoclassical Economics"),   # free market
    "Q7366":       ("112", "Classical & Neoclassical Economics"),   # liberalism
    "Q2449949":    ("112", "Classical & Neoclassical Economics"),   # neoliberalism
    "Q42602":      ("112", "Classical & Neoclassical Economics"),   # Austrian School
    "Q273626":     ("112", "Classical & Neoclassical Economics"),   # supply-side economics

    # ── 113 Marxism & Socialist Economics ──
    "Q7264":       ("113", "Marxism & Socialist Economics"),        # Marxism
    "Q7272":       ("113", "Marxism & Socialist Economics"),        # socialism
    "Q6186":       ("113", "Marxism & Socialist Economics"),        # communism
    "Q109367":     ("113", "Marxism & Socialist Economics"),        # anarchism
    "Q168796":     ("113", "Marxism & Socialist Economics"),        # Leninism
    "Q180376":     ("113", "Marxism & Socialist Economics"),        # Trotskyism
    "Q179222":     ("113", "Marxism & Socialist Economics"),        # Maoism
    "Q179229":     ("113", "Marxism & Socialist Economics"),        # Stalinism
    "Q5389":       ("113", "Marxism & Socialist Economics"),        # democratic socialism
    "Q184211":     ("113", "Marxism & Socialist Economics"),        # Marxism-Leninism
    "Q185090":     ("113", "Marxism & Socialist Economics"),        # anarcho-communism
    "Q180394":     ("113", "Marxism & Socialist Economics"),        # anarcho-syndicalism
    "Q667661":     ("113", "Marxism & Socialist Economics"),        # market socialism
    "Q862292":     ("113", "Marxism & Socialist Economics"),        # socialist economics

    # ── 114 Keynesian & Monetary Economics ──
    "Q173171":     ("114", "Keynesian & Monetary Economics"),       # Keynesian economics
    "Q185327":     ("114", "Keynesian & Monetary Economics"),       # monetarism
    "Q1412429":    ("114", "Keynesian & Monetary Economics"),       # New Keynesian economics
    "Q1249474":    ("114", "Keynesian & Monetary Economics"),       # post-Keynesian economics
    "Q182919":     ("114", "Keynesian & Monetary Economics"),       # monetary policy
    "Q211503":     ("114", "Keynesian & Monetary Economics"),       # fiscal policy
    "Q177819":     ("114", "Keynesian & Monetary Economics"),       # central banking concept
    "Q1889":       ("114", "Keynesian & Monetary Economics"),       # macroeconomics
    "Q39680":      ("114", "Keynesian & Monetary Economics"),       # microeconomics

    # ── 115 Agricultural & Land Economics ──
    "Q483413":     ("115", "Agricultural & Land Economics"),        # physiocracy
    "Q44777":      ("115", "Agricultural & Land Economics"),        # feudalism
    "Q1194747":    ("115", "Agricultural & Land Economics"),        # land reform
    "Q12078":      ("115", "Agricultural & Land Economics"),        # agricultural economics
    "Q228885":     ("115", "Agricultural & Land Economics"),        # collectivization
    "Q1860143":    ("115", "Agricultural & Land Economics"),        # agrarian system
    "Q11451":      ("115", "Agricultural & Land Economics"),        # agriculture

    # ════════════════════════════════════════════
    # 120 Scientific Paradigms
    # ════════════════════════════════════════════
    "Q336":        ("120", "Scientific Paradigms"),                 # science
    "Q7432":       ("120", "Scientific Paradigms"),                 # scientific theory
    "Q33500":      ("120", "Scientific Paradigms"),                 # theory
    "Q1132636":    ("120", "Scientific Paradigms"),                 # scientific paradigm
    "Q1196129":    ("120", "Scientific Paradigms"),                 # natural science
    "Q170475":     ("120", "Scientific Paradigms"),                 # scientific hypothesis
    "Q18364511":   ("120", "Scientific Paradigms"),                 # scientific concept
    "Q7187":       ("120", "Scientific Paradigms"),                 # scientific method
    "Q4671286":    ("120", "Scientific Paradigms"),                 # academic major

    # ── 121 Natural Philosophy & Classical Science ──
    "Q131476":     ("121", "Natural Philosophy & Classical Science"), # natural philosophy
    "Q186588":     ("121", "Natural Philosophy & Classical Science"), # metaphysics
    "Q9471":       ("121", "Natural Philosophy & Classical Science"), # epistemology
    "Q7891":       ("121", "Natural Philosophy & Classical Science"), # ontology
    "Q500066":     ("121", "Natural Philosophy & Classical Science"), # formal science
    "Q12483":      ("121", "Natural Philosophy & Classical Science"), # statistics
    "Q12482":      ("121", "Natural Philosophy & Classical Science"), # logic
    "Q149972":     ("121", "Natural Philosophy & Classical Science"), # philosophy of science
    "Q33527":      ("121", "Natural Philosophy & Classical Science"), # philosophy of mind

    # ── 122 Astronomy & Cosmology ──
    "Q333":        ("122", "Astronomy & Cosmology"),                # astronomy
    "Q338":        ("122", "Astronomy & Cosmology"),                # cosmology
    "Q18362":      ("122", "Astronomy & Cosmology"),                # heliocentrism
    "Q170024":     ("122", "Astronomy & Cosmology"),                # geocentrism
    "Q1711":       ("122", "Astronomy & Cosmology"),                # Big Bang theory
    "Q184876":     ("122", "Astronomy & Cosmology"),                # astrophysics
    "Q13442814":   ("122", "Astronomy & Cosmology"),                # astronomical object type
    "Q42262":      ("122", "Astronomy & Cosmology"),                # exoplanet
    "Q395":        ("122", "Astronomy & Cosmology"),                # mathematics
    "Q211":        ("122", "Astronomy & Cosmology"),                # star system

    # ── 123 Physics & Mechanics ──
    "Q413":        ("123", "Physics & Mechanics"),                  # physics
    "Q38433":      ("123", "Physics & Mechanics"),                  # classical mechanics
    "Q11402":      ("123", "Physics & Mechanics"),                  # quantum mechanics
    "Q43514":      ("123", "Physics & Mechanics"),                  # general relativity
    "Q7207":       ("123", "Physics & Mechanics"),                  # thermodynamics
    "Q11476":      ("123", "Physics & Mechanics"),                  # electromagnetism
    "Q82264":      ("123", "Physics & Mechanics"),                  # optics
    "Q1328304":    ("123", "Physics & Mechanics"),                  # fluid mechanics
    "Q18343":      ("123", "Physics & Mechanics"),                  # nuclear physics
    "Q11412":      ("123", "Physics & Mechanics"),                  # particle physics
    "Q24398318":   ("123", "Physics & Mechanics"),                  # physical theory
    "Q24340":      ("123", "Physics & Mechanics"),                  # physical law
    "Q28457":      ("123", "Physics & Mechanics"),                  # special relativity
    "Q47475003":   ("123", "Physics & Mechanics"),                  # branch of physics

    # ── 124 Chemistry & Alchemy ──
    "Q2329":       ("124", "Chemistry & Alchemy"),                  # chemistry
    "Q131189":     ("124", "Chemistry & Alchemy"),                  # alchemy
    "Q11651":      ("124", "Chemistry & Alchemy"),                  # periodic table
    "Q83588":      ("124", "Chemistry & Alchemy"),                  # organic chemistry
    "Q160307":     ("124", "Chemistry & Alchemy"),                  # inorganic chemistry
    "Q185652":     ("124", "Chemistry & Alchemy"),                  # analytical chemistry
    "Q178546":     ("124", "Chemistry & Alchemy"),                  # biochemistry
    "Q173113":     ("124", "Chemistry & Alchemy"),                  # electrochemistry
    "Q850131":     ("124", "Chemistry & Alchemy"),                  # pharmacology
    "Q187078":     ("124", "Chemistry & Alchemy"),                  # chemical element

    # ── 125 Biology & Evolution ──
    "Q420":        ("125", "Biology & Evolution"),                  # biology
    "Q1063":       ("125", "Biology & Evolution"),                  # evolution
    "Q43302":      ("125", "Biology & Evolution"),                  # natural selection
    "Q7430":       ("125", "Biology & Evolution"),                  # genetics
    "Q11398":      ("125", "Biology & Evolution"),                  # cell theory
    "Q7162":       ("125", "Biology & Evolution"),                  # ecology
    "Q146481":     ("125", "Biology & Evolution"),                  # botany
    "Q431":        ("125", "Biology & Evolution"),                  # zoology
    "Q7205":       ("125", "Biology & Evolution"),                  # microbiology
    "Q7141":       ("125", "Biology & Evolution"),                  # molecular biology
    "Q162555":     ("125", "Biology & Evolution"),                  # paleontology
    "Q130901":     ("125", "Biology & Evolution"),                  # genomics
    "Q82642":      ("125", "Biology & Evolution"),                  # taxonomy

    # ── 126 Medicine & Public Health ──
    "Q11190":      ("126", "Medicine & Public Health"),              # medicine
    "Q189603":     ("126", "Medicine & Public Health"),              # germ theory
    "Q178061":     ("126", "Medicine & Public Health"),              # vaccination
    "Q864693":     ("126", "Medicine & Public Health"),              # public health
    "Q9430":       ("126", "Medicine & Public Health"),              # pathology
    "Q9329":       ("126", "Medicine & Public Health"),              # surgery
    "Q132689":     ("126", "Medicine & Public Health"),              # epidemiology
    "Q40821":      ("126", "Medicine & Public Health"),              # psychiatry
    "Q171516":     ("126", "Medicine & Public Health"),              # cardiology
    "Q162606":     ("126", "Medicine & Public Health"),              # pediatrics
    "Q181689":     ("126", "Medicine & Public Health"),              # pharmacology sci
    "Q101929":     ("126", "Medicine & Public Health"),              # immunology

    # ════════════════════════════════════════════
    # 130 Technological Innovations
    # ════════════════════════════════════════════
    "Q11016":      ("130", "Technological Innovations"),            # technology
    "Q11023":      ("130", "Technological Innovations"),            # engineering
    "Q28865":      ("130", "Technological Innovations"),            # invention
    "Q1914636":    ("130", "Technological Innovations"),            # activity (type)
    "Q4027615":    ("130", "Technological Innovations"),            # technical standard
    "Q11862829a":  ("130", "Technological Innovations"),            # academic discipline (tech)

    # ── 131 Agricultural Technology ──
    "Q11451a":     ("131", "Agricultural Technology"),              # agriculture (tech)
    "Q158003":     ("131", "Agricultural Technology"),              # crop rotation
    "Q7868":       ("131", "Agricultural Technology"),              # irrigation
    "Q21199":      ("131", "Agricultural Technology"),              # aquaculture
    "Q189004":     ("131", "Agricultural Technology"),              # agronomics
    "Q220028":     ("131", "Agricultural Technology"),              # horticulture
    "Q185264":     ("131", "Agricultural Technology"),              # fertilizer
    "Q41364":      ("131", "Agricultural Technology"),              # pesticide
    "Q121359":     ("131", "Agricultural Technology"),              # hydroponics

    # ── 132 Manufacturing & Industrial ──
    "Q187939":     ("132", "Manufacturing & Industrial"),           # manufacturing
    "Q13580151":   ("132", "Manufacturing & Industrial"),           # industrialization
    "Q39397":      ("132", "Manufacturing & Industrial"),           # metallurgy
    "Q180684a":    ("132", "Manufacturing & Industrial"),           # mass production
    "Q133855":     ("132", "Manufacturing & Industrial"),           # pottery
    "Q5456":       ("132", "Manufacturing & Industrial"),           # steel
    "Q1110684":    ("132", "Manufacturing & Industrial"),           # textile manufacturing
    "Q12967":      ("132", "Manufacturing & Industrial"),           # textile industry
    "Q28877":      ("132", "Manufacturing & Industrial"),           # mining

    # ── 133 Transportation & Navigation ──
    "Q7590":       ("133", "Transportation & Navigation"),          # transportation
    "Q26540":      ("133", "Transportation & Navigation"),          # navigation
    "Q3041792":    ("133", "Transportation & Navigation"),          # means of transport
    "Q178512":     ("133", "Transportation & Navigation"),          # shipbuilding
    "Q12876":      ("133", "Transportation & Navigation"),          # railroad
    "Q11436":      ("133", "Transportation & Navigation"),          # aircraft
    "Q1420":       ("133", "Transportation & Navigation"),          # automobile
    "Q1075826":    ("133", "Transportation & Navigation"),          # motorboat
    "Q697175":     ("133", "Transportation & Navigation"),          # cartography method

    # ── 134 Communication & Information ──
    "Q11024":      ("134", "Communication & Information"),          # communication
    "Q161428":     ("134", "Communication & Information"),          # printing press
    "Q17329":      ("134", "Communication & Information"),          # photography
    "Q11030":      ("134", "Communication & Information"),          # journalism
    "Q11034":      ("134", "Communication & Information"),          # publishing
    "Q166628":     ("134", "Communication & Information"),          # telecommunication
    "Q219683":     ("134", "Communication & Information"),          # broadcasting
    "Q40056":      ("134", "Communication & Information"),          # radio
    "Q289":        ("134", "Communication & Information"),          # television
    "Q75a":        ("134", "Communication & Information"),          # World Wide Web

    # ── 135 Military Technology ──
    "Q12796":      ("135", "Military Technology"),                  # weapon
    "Q249019":     ("135", "Military Technology"),                  # military strategy
    "Q1361968a":   ("135", "Military Technology"),                  # military technology
    "Q2571":       ("135", "Military Technology"),                  # fortification
    "Q1065":       ("135", "Military Technology"),                  # gunpowder
    "Q1338970":    ("135", "Military Technology"),                  # ballistics
    "Q154020":     ("135", "Military Technology"),                  # nuclear weapon
    "Q174174":     ("135", "Military Technology"),                  # missile
    "Q39546":      ("135", "Military Technology"),                  # tool (military)

    # ── 136 Computing & Digital Technology ──
    "Q68":         ("136", "Computing & Digital Technology"),       # computer science
    "Q5288":       ("136", "Computing & Digital Technology"),       # artificial intelligence
    "Q1301371":    ("136", "Computing & Digital Technology"),       # computing
    "Q80006":      ("136", "Computing & Digital Technology"),       # algorithm
    "Q2878974":    ("136", "Computing & Digital Technology"),       # programming paradigm
    "Q28923":      ("136", "Computing & Digital Technology"),       # encryption
    "Q8513":       ("136", "Computing & Digital Technology"),       # database
    "Q9135":       ("136", "Computing & Digital Technology"),       # operating system
    "Q9143":       ("136", "Computing & Digital Technology"),       # programming language
    "Q1668024":    ("136", "Computing & Digital Technology"),       # software engineering
    "Q3966":       ("136", "Computing & Digital Technology"),       # computer hardware
    "Q7397":       ("136", "Computing & Digital Technology"),       # software
    "Q141090":     ("136", "Computing & Digital Technology"),       # robotics
    "Q6212":       ("136", "Computing & Digital Technology"),       # machine learning

    # ════════════════════════════════════════════
    # 140 Religious & Philosophical Concepts
    # ════════════════════════════════════════════
    "Q9174":       ("140", "Religious & Philosophical Concepts"),   # religion
    "Q5891":       ("140", "Religious & Philosophical Concepts"),   # philosophy
    "Q1783494":    ("140", "Religious & Philosophical Concepts"),   # religious belief
    "Q17444909":   ("140", "Religious & Philosophical Concepts"),   # philosophical concept
    "Q151885":     ("140", "Religious & Philosophical Concepts"),   # concept
    "Q18340550":   ("140", "Religious & Philosophical Concepts"),   # philosophical doctrine
    "Q12479":      ("140", "Religious & Philosophical Concepts"),   # worldview
    "Q2963543":    ("140", "Religious & Philosophical Concepts"),   # belief system
    "Q474":        ("140", "Religious & Philosophical Concepts"),   # philosophical school
    "Q1151067":    ("140", "Religious & Philosophical Concepts"),   # school of thought
    "Q3356859":    ("140", "Religious & Philosophical Concepts"),   # branch of philosophy
    "Q23834":      ("140", "Religious & Philosophical Concepts"),   # denomination

    # ── 141 Monotheism & Abrahamic Theology ──
    "Q100951":     ("141", "Monotheism & Abrahamic Theology"),     # monotheism
    "Q47280":      ("141", "Monotheism & Abrahamic Theology"),     # Abrahamic religion
    "Q33104":      ("141", "Monotheism & Abrahamic Theology"),     # Christian theology
    "Q107380":     ("141", "Monotheism & Abrahamic Theology"),     # Islamic theology
    "Q5043":       ("141", "Monotheism & Abrahamic Theology"),     # Christianity
    "Q432":        ("141", "Monotheism & Abrahamic Theology"),     # Islam
    "Q9268":       ("141", "Monotheism & Abrahamic Theology"),     # Judaism
    "Q153232":     ("141", "Monotheism & Abrahamic Theology"),     # Christian denomination
    "Q2197012":    ("141", "Monotheism & Abrahamic Theology"),     # Christian theological concept
    "Q2529283":    ("141", "Monotheism & Abrahamic Theology"),     # Islamic denomination
    "Q171740":     ("141", "Monotheism & Abrahamic Theology"),     # soteriology

    # ── 142 Polytheism & Mythology ──
    "Q9159":       ("142", "Polytheism & Mythology"),              # polytheism
    "Q15978631":   ("142", "Polytheism & Mythology"),              # group of mythological characters
    "Q34726":      ("142", "Polytheism & Mythology"),              # mythology
    "Q9134":       ("142", "Polytheism & Mythology"),              # animism
    "Q11427":      ("142", "Polytheism & Mythology"),              # shamanism
    "Q132821":     ("142", "Polytheism & Mythology"),              # totemism
    "Q42042":      ("142", "Polytheism & Mythology"),              # pantheism
    "Q182978":     ("142", "Polytheism & Mythology"),              # panentheism
    "Q178150":     ("142", "Polytheism & Mythology"),              # paganism
    "Q37056":      ("142", "Polytheism & Mythology"),              # folk religion
    "Q63070":      ("142", "Polytheism & Mythology"),              # ancient religion

    # ── 143 Eastern Philosophy & Dharmic Thought ──
    "Q162740":     ("143", "Eastern Philosophy & Dharmic Thought"), # Dharmic religion
    "Q4393":       ("143", "Eastern Philosophy & Dharmic Thought"), # Confucianism
    "Q7556":       ("143", "Eastern Philosophy & Dharmic Thought"), # Taoism
    "Q9316":       ("143", "Eastern Philosophy & Dharmic Thought"), # Buddhism
    "Q9089":       ("143", "Eastern Philosophy & Dharmic Thought"), # Hinduism
    "Q9232":       ("143", "Eastern Philosophy & Dharmic Thought"), # Jainism
    "Q9288":       ("143", "Eastern Philosophy & Dharmic Thought"), # Sikhism
    "Q8777":       ("143", "Eastern Philosophy & Dharmic Thought"), # Shinto
    "Q18337":      ("143", "Eastern Philosophy & Dharmic Thought"), # Tibetan Buddhism
    "Q132265":     ("143", "Eastern Philosophy & Dharmic Thought"), # Zen Buddhism
    "Q484416":     ("143", "Eastern Philosophy & Dharmic Thought"), # Vedanta
    "Q316450":     ("143", "Eastern Philosophy & Dharmic Thought"), # Legalism

    # ── 144 Mysticism & Esotericism ──
    "Q46522":      ("144", "Mysticism & Esotericism"),             # mysticism
    "Q131748":     ("144", "Mysticism & Esotericism"),             # esotericism
    "Q207591":     ("144", "Mysticism & Esotericism"),             # occultism
    "Q42040":      ("144", "Mysticism & Esotericism"),             # Sufism
    "Q102416":     ("144", "Mysticism & Esotericism"),             # Kabbalah
    "Q9585":       ("144", "Mysticism & Esotericism"),             # Gnosticism
    "Q165125":     ("144", "Mysticism & Esotericism"),             # Hermeticism
    "Q193522":     ("144", "Mysticism & Esotericism"),             # Rosicrucianism
    "Q7066a":      ("144", "Mysticism & Esotericism"),             # Theosophy
    "Q41581":      ("144", "Mysticism & Esotericism"),             # Freemasonry
    "Q145490":     ("144", "Mysticism & Esotericism"),             # Neoplatonism
    "Q131395a":    ("144", "Mysticism & Esotericism"),             # Zoroastrianism

    # ── 145 Secular & Humanist Philosophy ──
    "Q49447":      ("145", "Secular & Humanist Philosophy"),       # humanism
    "Q7066":       ("145", "Secular & Humanist Philosophy"),       # atheism
    "Q170208":     ("145", "Secular & Humanist Philosophy"),       # secularism
    "Q34740":      ("145", "Secular & Humanist Philosophy"),       # existentialism
    "Q130900":     ("145", "Secular & Humanist Philosophy"),       # nihilism
    "Q166280":     ("145", "Secular & Humanist Philosophy"),       # pragmatism
    "Q181898":     ("145", "Secular & Humanist Philosophy"),       # rationalism
    "Q170028":     ("145", "Secular & Humanist Philosophy"),       # empiricism
    "Q79869":      ("145", "Secular & Humanist Philosophy"),       # materialism
    "Q11009":      ("145", "Secular & Humanist Philosophy"),       # idealism
    "Q178748":     ("145", "Secular & Humanist Philosophy"),       # positivism
    "Q37732":      ("145", "Secular & Humanist Philosophy"),       # phenomenology
    "Q131110":     ("145", "Secular & Humanist Philosophy"),       # utopia
    "Q483666":     ("145", "Secular & Humanist Philosophy"),       # stoicism
    "Q179060":     ("145", "Secular & Humanist Philosophy"),       # dialectic
    "Q131464":     ("145", "Secular & Humanist Philosophy"),       # skepticism
    "Q189539":     ("145", "Secular & Humanist Philosophy"),       # agnosticism
    "Q152388":     ("145", "Secular & Humanist Philosophy"),       # transhumanism
    "Q190535":     ("145", "Secular & Humanist Philosophy"),       # determinism
    "Q36484":      ("145", "Secular & Humanist Philosophy"),       # relativism

    # ════════════════════════════════════════════
    # 150 Social & Cultural Theories
    # ════════════════════════════════════════════
    "Q8425":       ("150", "Social & Cultural Theories"),          # sociology
    "Q860746":     ("150", "Social & Cultural Theories"),          # social theory
    "Q11862829":   ("150", "Social & Cultural Theories"),          # academic discipline
    "Q11634":      ("150", "Social & Cultural Theories"),          # political science
    "Q206049":     ("150", "Social & Cultural Theories"),          # social science

    # ── 151 Sociology & Social Structure ──
    "Q214917":     ("151", "Sociology & Social Structure"),        # social class
    "Q169966":     ("151", "Sociology & Social Structure"),        # functionalism
    "Q193353":     ("151", "Sociology & Social Structure"),        # social stratification
    "Q185329":     ("151", "Sociology & Social Structure"),        # demography
    "Q849680":     ("151", "Sociology & Social Structure"),        # social structure
    "Q146927":     ("151", "Sociology & Social Structure"),        # criminology
    "Q1151711":    ("151", "Sociology & Social Structure"),        # social norm
    "Q309391":     ("151", "Sociology & Social Structure"),        # social movement theory

    # ── 152 Anthropology & Ethnography ──
    "Q23404":      ("152", "Anthropology & Ethnography"),          # anthropology
    "Q167229":     ("152", "Anthropology & Ethnography"),          # structuralism
    "Q42240":      ("152", "Anthropology & Ethnography"),          # ethnography
    "Q1071":       ("152", "Anthropology & Ethnography"),          # geography
    "Q1620908":    ("152", "Anthropology & Ethnography"),          # cultural studies
    "Q43455":      ("152", "Anthropology & Ethnography"),          # cultural anthropology
    "Q5737":       ("152", "Anthropology & Ethnography"),          # archaeology
    "Q36442":      ("152", "Anthropology & Ethnography"),          # human geography

    # ── 153 Linguistics & Language Theory ──
    "Q8162":       ("153", "Linguistics & Language Theory"),        # linguistics
    "Q199655":     ("153", "Linguistics & Language Theory"),        # semiotics
    "Q1288568":    ("153", "Linguistics & Language Theory"),        # language theory
    "Q34770":      ("153", "Linguistics & Language Theory"),        # language
    "Q38848":      ("153", "Linguistics & Language Theory"),        # language family
    "Q315":        ("153", "Linguistics & Language Theory"),        # sign language
    "Q150":        ("153", "Linguistics & Language Theory"),        # language construct
    "Q661425":     ("153", "Linguistics & Language Theory"),        # philology
    "Q483242":     ("153", "Linguistics & Language Theory"),        # computational linguistics
    "Q47307":      ("153", "Linguistics & Language Theory"),        # sociolinguistics
    "Q2200417":    ("153", "Linguistics & Language Theory"),        # phonology
    "Q40998":      ("153", "Linguistics & Language Theory"),        # syntax
    "Q243998":     ("153", "Linguistics & Language Theory"),        # semantics

    # ── 154 Psychology & Human Behavior ──
    "Q9418":       ("154", "Psychology & Human Behavior"),          # psychology
    "Q180160":     ("154", "Psychology & Human Behavior"),          # behaviorism
    "Q184843":     ("154", "Psychology & Human Behavior"),          # psychoanalysis
    "Q147778":     ("154", "Psychology & Human Behavior"),          # cognitive psychology
    "Q199020":     ("154", "Psychology & Human Behavior"),          # social psychology
    "Q3958":       ("154", "Psychology & Human Behavior"),          # developmental psychology
    "Q207703":     ("154", "Psychology & Human Behavior"),          # neuropsychology
    "Q180123":     ("154", "Psychology & Human Behavior"),          # humanistic psychology
    "Q194078":     ("154", "Psychology & Human Behavior"),          # evolutionary psychology
    "Q11023a":     ("154", "Psychology & Human Behavior"),          # positive psychology
    "Q170384":     ("154", "Psychology & Human Behavior"),          # Gestalt psychology
    "Q177220":     ("154", "Psychology & Human Behavior"),          # neuroscience

    # ── 155 Education & Pedagogy ──
    "Q8434":       ("155", "Education & Pedagogy"),                # education
    "Q14208":      ("155", "Education & Pedagogy"),                # pedagogy
    "Q1391145":    ("155", "Education & Pedagogy"),                # educational theory
    "Q20702":      ("155", "Education & Pedagogy"),                # didactics
    "Q329737":     ("155", "Education & Pedagogy"),                # curriculum
    "Q80174a":     ("155", "Education & Pedagogy"),                # Montessori education (alias)
    "Q106226":     ("155", "Education & Pedagogy"),                # literacy

    # ════════════════════════════════════════════
    # 160 Environmental & Ecological Ideas
    # ════════════════════════════════════════════
    "Q7150":       ("160", "Environmental & Ecological Ideas"),    # ecology
    "Q179805a":    ("160", "Environmental & Ecological Ideas"),    # environmentalism
    "Q159943":     ("160", "Environmental & Ecological Ideas"),    # earth science
    "Q11386":      ("160", "Environmental & Ecological Ideas"),    # geophysics
    "Q1071a":      ("160", "Environmental & Ecological Ideas"),    # physical geography
    "Q41255":      ("160", "Environmental & Ecological Ideas"),    # environmental science
    "Q167523":     ("160", "Environmental & Ecological Ideas"),    # oceanography
    "Q175053":     ("160", "Environmental & Ecological Ideas"),    # hydrology

    # ── 161 Conservation & Preservation ──
    "Q180788":     ("161", "Conservation & Preservation"),          # conservation
    "Q107257":     ("161", "Conservation & Preservation"),          # biodiversity
    "Q7245":       ("161", "Conservation & Preservation"),          # protected area
    "Q44533":      ("161", "Conservation & Preservation"),          # national park
    "Q473972":     ("161", "Conservation & Preservation"),          # nature reserve
    "Q386120":     ("161", "Conservation & Preservation"),          # wildlife management
    "Q861609":     ("161", "Conservation & Preservation"),          # endangered species
    "Q3245252":    ("161", "Conservation & Preservation"),          # environmental protection

    # ── 162 Climate & Atmospheric Science ──
    "Q52139":      ("162", "Climate & Atmospheric Science"),        # climatology
    "Q11663":      ("162", "Climate & Atmospheric Science"),        # climate change
    "Q37132":      ("162", "Climate & Atmospheric Science"),        # meteorology
    "Q3827":       ("162", "Climate & Atmospheric Science"),        # atmosphere
    "Q179235":     ("162", "Climate & Atmospheric Science"),        # greenhouse effect
    "Q7942":       ("162", "Climate & Atmospheric Science"),        # global warming
    "Q82069":      ("162", "Climate & Atmospheric Science"),        # ozone depletion

    # ── 163 Sustainability & Resource Management ──
    "Q219416":     ("163", "Sustainability & Resource Management"), # sustainability
    "Q171995":     ("163", "Sustainability & Resource Management"), # renewable energy
    "Q12748":      ("163", "Sustainability & Resource Management"), # recycling
    "Q3920289":    ("163", "Sustainability & Resource Management"), # green building
    "Q842620":     ("163", "Sustainability & Resource Management"), # circular economy
    "Q113217":     ("163", "Sustainability & Resource Management"), # permaculture
    "Q180003":     ("163", "Sustainability & Resource Management"), # environmental policy
    "Q39614":      ("163", "Sustainability & Resource Management"), # water management

    # ════════════════════════════════════════════
    # 170 Artistic & Aesthetic Movements
    # ════════════════════════════════════════════
    "Q735":        ("170", "Artistic & Aesthetic Movements"),      # art
    "Q1792644":    ("170", "Artistic & Aesthetic Movements"),      # art movement
    "Q968159":     ("170", "Artistic & Aesthetic Movements"),      # art style
    "Q184299":     ("170", "Artistic & Aesthetic Movements"),      # literary movement
    "Q210112":     ("170", "Artistic & Aesthetic Movements"),      # genre
    "Q3326717":    ("170", "Artistic & Aesthetic Movements"),      # literary genre
    "Q207694":     ("170", "Artistic & Aesthetic Movements"),      # art genre
    "Q2743":       ("170", "Artistic & Aesthetic Movements"),      # musical genre
    "Q191067":     ("170", "Artistic & Aesthetic Movements"),      # architectural style
    "Q58415929":   ("170", "Artistic & Aesthetic Movements"),      # cultural movement
    "Q11019":      ("170", "Artistic & Aesthetic Movements"),      # machine/device
    "Q2135540":    ("170", "Artistic & Aesthetic Movements"),      # dance genre

    # ── 171 Classical & Renaissance Aesthetics ──
    "Q1420559":    ("171", "Classical & Renaissance Aesthetics"),  # classicism
    "Q41726":      ("171", "Classical & Renaissance Aesthetics"),  # neoclassicism
    "Q946508":     ("171", "Classical & Renaissance Aesthetics"),  # Renaissance art
    "Q47692":      ("171", "Classical & Renaissance Aesthetics"),  # baroque
    "Q132311":     ("171", "Classical & Renaissance Aesthetics"),  # mannerism
    "Q191113":     ("171", "Classical & Renaissance Aesthetics"),  # rococo
    "Q3055978":    ("171", "Classical & Renaissance Aesthetics"),  # Renaissance music

    # ── 172 Modernism & Avant-Garde ──
    "Q37068":      ("172", "Modernism & Avant-Garde"),            # modernism
    "Q170292":     ("172", "Modernism & Avant-Garde"),            # avant-garde
    "Q166713":     ("172", "Modernism & Avant-Garde"),            # impressionism
    "Q180774":     ("172", "Modernism & Avant-Garde"),            # expressionism
    "Q37853":      ("172", "Modernism & Avant-Garde"),            # cubism
    "Q39427":      ("172", "Modernism & Avant-Garde"),            # surrealism
    "Q173436":     ("172", "Modernism & Avant-Garde"),            # abstract art
    "Q170572":     ("172", "Modernism & Avant-Garde"),            # art nouveau
    "Q179993":     ("172", "Modernism & Avant-Garde"),            # art deco
    "Q41354":      ("172", "Modernism & Avant-Garde"),            # futurism
    "Q214917a":    ("172", "Modernism & Avant-Garde"),            # Dadaism
    "Q192993":     ("172", "Modernism & Avant-Garde"),            # Bauhaus
    "Q160236":     ("172", "Modernism & Avant-Garde"),            # constructivism
    "Q170583":     ("172", "Modernism & Avant-Garde"),            # symbolism
    "Q186030":     ("172", "Modernism & Avant-Garde"),            # realism (art)
    "Q40831a":     ("172", "Modernism & Avant-Garde"),            # romanticism
    "Q134307":     ("172", "Modernism & Avant-Garde"),            # naturalism
    "Q184872":     ("172", "Modernism & Avant-Garde"),            # fauvism
    "Q133654":     ("172", "Modernism & Avant-Garde"),            # pop art
    "Q162150":     ("172", "Modernism & Avant-Garde"),            # minimalism

    # ── 173 Postmodernism & Deconstruction ──
    "Q47783a":     ("173", "Postmodernism & Deconstruction"),     # postmodernism
    "Q181404":     ("173", "Postmodernism & Deconstruction"),     # deconstruction
    "Q185067":     ("173", "Postmodernism & Deconstruction"),     # post-structuralism
    "Q483394":     ("173", "Postmodernism & Deconstruction"),     # contemporary art
    "Q2291283":    ("173", "Postmodernism & Deconstruction"),     # conceptual art
    "Q187712":     ("173", "Postmodernism & Deconstruction"),     # street art
    "Q1756039":    ("173", "Postmodernism & Deconstruction"),     # installation art
    "Q213156":     ("173", "Postmodernism & Deconstruction"),     # critical theory
    "Q193544":     ("173", "Postmodernism & Deconstruction"),     # digital art
    "Q231218":     ("173", "Postmodernism & Deconstruction"),     # deconstructivism
}

# Build clean reverse lookup
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in IDEAS_OTHER_TYPE_MAP.items():
    clean_qid = _qid.rstrip("a")
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info


# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (120+ granular batches)
# Each batch -> (QIDs, min_sitelinks, use_subclass)
# use_subclass=True → UNION P31+P279 for broader coverage
# ═══════════════════════════════════════════════════════════════════

IDEAS_OTHER_QUERIES: dict[str, tuple[list[str], int, bool]] = {
    # ── 110 Economic Theories ──
    "110_econ_broad":      (["Q8134"], 10, False),
    "110_econ_theory":     (["Q186247", "Q2979973", "Q47495990"], 3, False),
    "110_econ_system":     (["Q11042", "Q182790", "Q12140182"], 3, False),
    "110_econ_concept":    (["Q1778667", "Q188924"], 3, False),

    # ── 111 Mercantilism ──
    "111_mercantil":       (["Q131735", "Q220338", "Q208642"], 2, False),
    "111_trade_theory":    (["Q846706", "Q601401"], 2, False),
    "111_trade":           (["Q17517"], 10, False),

    # ── 112 Classical/Neoclassical ──
    "112_classical":       (["Q83267", "Q190375"], 3, False),
    "112_capitalism":      (["Q35591", "Q202640", "Q327960"], 3, False),
    "112_liberalism":      (["Q7366", "Q2449949"], 5, False),
    "112_schools":         (["Q42602", "Q273626"], 3, False),

    # ── 113 Marxism/Socialist ──
    "113_marxism":         (["Q7264", "Q7272", "Q6186"], 3, False),
    "113_anarchism":       (["Q109367", "Q185090", "Q180394"], 3, False),
    "113_variants":        (["Q168796", "Q180376", "Q179222", "Q179229"], 3, False),
    "113_democratic":      (["Q5389", "Q184211", "Q667661", "Q862292"], 3, False),

    # ── 114 Keynesian/Monetary ──
    "114_keynesian":       (["Q173171", "Q1412429", "Q1249474"], 2, False),
    "114_monetary":        (["Q185327", "Q182919", "Q211503"], 2, False),
    "114_macro_micro":     (["Q1889", "Q39680"], 5, False),
    "114_subclass":        (["Q173171", "Q185327"], 2, True),

    # ── 115 Agricultural/Land ──
    "115_physiocracy":     (["Q483413", "Q44777"], 3, False),
    "115_land_reform":     (["Q1194747", "Q228885", "Q1860143"], 2, False),
    "115_ag_econ":         (["Q12078", "Q11451"], 5, False),

    # ── 120 Scientific Paradigms ──
    "120_science":         (["Q336"], 10, False),
    "120_theory":          (["Q7432", "Q33500"], 8, False),
    "120_paradigm":        (["Q1132636", "Q1196129"], 3, False),
    "120_concepts":        (["Q18364511", "Q170475", "Q7187"], 3, False),
    "120_discipline":      (["Q4671286"], 5, False),

    # ── 121 Natural Philosophy ──
    "121_nat_phil":        (["Q131476", "Q186588"], 3, False),
    "121_epistem":         (["Q9471", "Q7891"], 3, False),
    "121_formal":          (["Q500066", "Q12482", "Q12483"], 3, False),
    "121_phil_science":    (["Q149972", "Q33527"], 3, False),
    "121_subclass":        (["Q131476"], 2, True),

    # ── 122 Astronomy ──
    "122_astronomy":       (["Q333", "Q338"], 8, False),
    "122_models":          (["Q18362", "Q170024", "Q1711"], 3, False),
    "122_astrophysics":    (["Q184876"], 5, False),

    # ── 123 Physics ──
    "123_physics":         (["Q413"], 10, False),
    "123_branches":        (["Q11476", "Q82264", "Q18343", "Q11412"], 3, False),
    "123_mechanics":       (["Q38433", "Q11402", "Q1328304"], 3, False),
    "123_relativity":      (["Q43514", "Q28457"], 3, False),
    "123_theories":        (["Q24398318", "Q24340", "Q47475003"], 3, False),

    # ── 124 Chemistry ──
    "124_chemistry":       (["Q2329"], 8, False),
    "124_branches":        (["Q83588", "Q160307", "Q185652", "Q178546"], 3, False),
    "124_alchemy":         (["Q131189"], 3, False),
    "124_other":           (["Q173113", "Q850131", "Q187078"], 3, False),

    # ── 125 Biology ──
    "125_biology":         (["Q420", "Q1063"], 5, False),
    "125_branches":        (["Q7162", "Q146481", "Q431", "Q7205"], 3, False),
    "125_molecular":       (["Q7141", "Q130901", "Q82642"], 3, False),
    "125_evolution":       (["Q43302", "Q7430", "Q162555"], 3, False),

    # ── 126 Medicine ──
    "126_medicine":        (["Q11190"], 8, False),
    "126_theory":          (["Q189603", "Q178061", "Q864693"], 3, False),
    "126_specialties":     (["Q9430", "Q9329", "Q132689", "Q40821"], 3, False),
    "126_more":            (["Q171516", "Q162606", "Q181689", "Q101929"], 3, False),

    # ── 130 Technology ──
    "130_technology":      (["Q11016", "Q11023"], 12, False),
    "130_invention":       (["Q28865"], 5, False),

    # ── 131 Agriculture ──
    "131_methods":         (["Q158003", "Q7868", "Q21199"], 3, False),
    "131_science":         (["Q189004", "Q220028"], 3, False),
    "131_inputs":          (["Q185264", "Q41364", "Q121359"], 3, False),

    # ── 132 Manufacturing ──
    "132_industry":        (["Q187939", "Q13580151"], 3, False),
    "132_processes":       (["Q39397", "Q133855", "Q5456"], 3, False),
    "132_textile":         (["Q1110684", "Q12967", "Q28877"], 3, False),

    # ── 133 Transportation ──
    "133_transport":       (["Q7590", "Q26540"], 5, False),
    "133_means":           (["Q3041792", "Q178512"], 3, False),
    "133_vehicles":        (["Q12876", "Q11436", "Q1420"], 5, False),

    # ── 134 Communication ──
    "134_communication":   (["Q11024", "Q161428"], 3, False),
    "134_media":           (["Q17329", "Q11030", "Q11034"], 3, False),
    "134_telecom":         (["Q166628", "Q219683", "Q40056", "Q289"], 5, False),

    # ── 135 Military Technology ──
    "135_military":        (["Q249019", "Q12796"], 5, False),
    "135_fortification":   (["Q2571", "Q1065", "Q1338970"], 3, False),
    "135_modern":          (["Q154020", "Q174174"], 3, False),

    # ── 136 Computing ──
    "136_cs":              (["Q68", "Q5288"], 5, False),
    "136_foundations":     (["Q80006", "Q2878974", "Q28923"], 3, False),
    "136_systems":         (["Q8513", "Q9135", "Q9143"], 5, False),
    "136_software":        (["Q1668024", "Q3966", "Q7397"], 5, False),
    "136_ai":              (["Q141090", "Q6212", "Q1301371"], 3, False),

    # ── 140 Religious/Philosophical ──
    "140_religion":        (["Q9174"], 8, False),
    "140_philosophy":      (["Q5891"], 8, False),
    "140_phil_concept":    (["Q17444909", "Q18340550"], 3, False),
    "140_belief":          (["Q1783494", "Q12479", "Q2963543"], 3, False),
    "140_concept":         (["Q151885"], 18, False),
    "140_school":          (["Q474", "Q1151067", "Q3356859"], 3, False),
    "140_denomination":    (["Q23834"], 3, False),

    # ── 141 Monotheism ──
    "141_monotheism":      (["Q100951", "Q47280"], 3, False),
    "141_christianity":    (["Q5043", "Q33104", "Q153232"], 3, False),
    "141_islam":           (["Q432", "Q107380", "Q2529283"], 3, False),
    "141_theology":        (["Q2197012", "Q171740", "Q9268"], 3, False),

    # ── 142 Polytheism ──
    "142_polytheism":      (["Q9159", "Q34726", "Q9134"], 3, False),
    "142_animism":         (["Q11427", "Q132821", "Q42042", "Q182978"], 3, False),
    "142_pagan":           (["Q178150", "Q37056", "Q63070"], 3, False),

    # ── 143 Eastern ──
    "143_dharmic":         (["Q162740", "Q9089", "Q9316"], 3, False),
    "143_east_asian":      (["Q4393", "Q7556", "Q8777"], 3, False),
    "143_branches":        (["Q9232", "Q9288", "Q18337", "Q132265"], 3, False),
    "143_schools":         (["Q484416", "Q316450"], 3, False),

    # ── 144 Mysticism ──
    "144_mysticism":       (["Q46522", "Q131748", "Q207591"], 3, False),
    "144_traditions":      (["Q42040", "Q102416", "Q9585"], 3, False),
    "144_western":         (["Q165125", "Q193522", "Q41581"], 3, False),
    "144_neoplatonism":    (["Q145490"], 3, False),

    # ── 145 Secular/Humanist ──
    "145_secular":         (["Q49447", "Q7066", "Q170208", "Q189539"], 3, False),
    "145_existential":     (["Q34740", "Q130900", "Q166280"], 3, False),
    "145_rational":        (["Q181898", "Q170028", "Q79869", "Q11009"], 3, False),
    "145_more":            (["Q178748", "Q37732", "Q483666"], 3, False),
    "145_advanced":        (["Q179060", "Q131464", "Q152388", "Q190535", "Q36484"], 3, False),

    # ── 150 Social/Cultural ──
    "150_sociology":       (["Q8425", "Q860746"], 3, False),
    "150_polisci":         (["Q11634", "Q206049"], 5, False),
    "150_discipline":      (["Q11862829"], 12, False),

    # ── 151 Sociology ──
    "151_social":          (["Q214917", "Q193353", "Q849680"], 3, False),
    "151_fields":          (["Q185329", "Q146927", "Q1151711"], 3, False),
    "151_theory":          (["Q169966", "Q309391"], 3, False),

    # ── 152 Anthropology ──
    "152_anthro":          (["Q23404", "Q42240", "Q43455"], 3, False),
    "152_related":         (["Q1071", "Q1620908", "Q5737", "Q36442"], 3, False),
    "152_structural":      (["Q167229"], 3, False),

    # ── 153 Linguistics ──
    "153_linguistics":     (["Q8162"], 5, False),
    "153_semiotics":       (["Q199655", "Q1288568"], 3, False),
    "153_language":        (["Q34770"], 8, False),
    "153_families":        (["Q38848"], 5, False),
    "153_branches":        (["Q661425", "Q483242", "Q47307"], 3, False),
    "153_formal":          (["Q2200417", "Q40998", "Q243998"], 3, False),

    # ── 154 Psychology ──
    "154_psychology":      (["Q9418"], 5, False),
    "154_schools":         (["Q180160", "Q184843", "Q147778"], 3, False),
    "154_social":          (["Q199020", "Q3958", "Q207703"], 3, False),
    "154_modern":          (["Q180123", "Q194078", "Q170384", "Q177220"], 3, False),

    # ── 155 Education ──
    "155_education":       (["Q8434"], 5, False),
    "155_pedagogy":        (["Q14208", "Q1391145", "Q20702"], 3, False),
    "155_practice":        (["Q329737", "Q106226"], 3, False),

    # ── 160 Environmental ──
    "160_ecology":         (["Q7150"], 5, False),
    "160_earth_sci":       (["Q159943", "Q11386", "Q41255"], 3, False),
    "160_hydro":           (["Q167523", "Q175053"], 3, False),

    # ── 161 Conservation ──
    "161_conservation":    (["Q180788", "Q107257"], 3, False),
    "161_protected":       (["Q7245", "Q44533", "Q473972"], 3, False),
    "161_wildlife":        (["Q386120", "Q861609", "Q3245252"], 2, False),
    "161_subclass":        (["Q180788"], 2, True),

    # ── 162 Climate ──
    "162_climate":         (["Q52139", "Q11663"], 3, False),
    "162_atmospheric":     (["Q37132", "Q3827"], 5, False),
    "162_effects":         (["Q179235", "Q7942", "Q82069"], 3, False),

    # ── 163 Sustainability ──
    "163_sustainability":  (["Q219416", "Q171995", "Q12748"], 3, False),
    "163_practices":       (["Q3920289", "Q842620", "Q113217"], 2, False),
    "163_policy":          (["Q180003", "Q39614"], 3, False),
    "163_subclass":        (["Q219416"], 2, True),

    # ── 170 Artistic Movements ──
    "170_art_movement":    (["Q1792644", "Q968159"], 3, False),
    "170_literary":        (["Q184299"], 3, False),
    "170_genre":           (["Q210112", "Q3326717", "Q207694"], 5, False),
    "170_music_genre":     (["Q2743"], 8, False),
    "170_arch_style":      (["Q191067"], 3, False),
    "170_cultural":        (["Q58415929", "Q2135540"], 3, False),

    # ── 171 Classical Aesthetics ──
    "171_classical":       (["Q1420559", "Q41726"], 3, False),
    "171_renaissance":     (["Q946508", "Q3055978"], 3, False),
    "171_baroque":         (["Q47692", "Q132311", "Q191113"], 3, False),

    # ── 172 Modernism ──
    "172_modernism":       (["Q37068", "Q170292"], 3, False),
    "172_impress":         (["Q166713", "Q180774", "Q37853"], 3, False),
    "172_surreal":         (["Q39427", "Q173436", "Q41354"], 3, False),
    "172_nouveau":         (["Q170572", "Q179993", "Q192993"], 3, False),
    "172_construct":       (["Q160236", "Q170583", "Q186030"], 3, False),
    "172_romantic":        (["Q134307", "Q184872", "Q133654", "Q162150"], 3, False),

    # ── 173 Postmodernism ──
    "173_postmodern":      (["Q181404", "Q185067"], 3, False),
    "173_contemporary":    (["Q483394", "Q2291283", "Q187712"], 3, False),
    "173_digital":         (["Q1756039", "Q213156", "Q193544"], 3, False),
    "173_decon":           (["Q231218"], 2, False),
    "173_subclass":        (["Q181404", "Q185067"], 2, True),
}


# ═══════════════════════════════════════════════════════════════════
# Non-idea keyword filter
# ═══════════════════════════════════════════════════════════════════

NON_IDEAS_KEYWORDS = {
    'wikimedia', 'disambiguation', 'template', 'category',
    'fictional character', 'video game', 'mobile app',
    'taxon', 'species', 'genus', 'protein', 'gene',
    'television series', 'tv series', 'podcast', 'album', 'song',
    'association football', 'football club', 'sports club',
    'railway station', 'metro station', 'bus route',
    'municipality', 'village', 'commune of',
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
    "Q41":    ("Greece", "Southern Europe", "Europe"),
    "Q20":    ("Norway", "Northern Europe", "Europe"),
    "Q34":    ("Sweden", "Northern Europe", "Europe"),
    "Q35":    ("Denmark", "Northern Europe", "Europe"),
    "Q31":    ("Belgium", "Western Europe", "Europe"),
    "Q16":    ("Canada", "North America", "Americas"),
    "Q96":    ("Mexico", "Central America", "Americas"),
    "Q155":   ("Brazil", "South America", "Americas"),
    "Q45":    ("Portugal", "Southern Europe", "Europe"),
    "Q408":   ("Australia", "Oceania", "Oceania"),
    "Q79":    ("Egypt", "North Africa", "Africa"),
    "Q115":   ("Ethiopia", "East Africa", "Africa"),
    "Q1033":  ("Nigeria", "West Africa", "Africa"),
    "Q258":   ("South Africa", "Southern Africa", "Africa"),
    "Q794":   ("Iran", "West Asia", "Asia"),
    "Q796":   ("Iraq", "West Asia", "Asia"),
    "Q801":   ("Israel", "West Asia", "Asia"),
    "Q843":   ("Pakistan", "South Asia", "Asia"),
    "Q869":   ("Thailand", "Southeast Asia", "Asia"),
    "Q881":   ("Vietnam", "Southeast Asia", "Asia"),
    "Q252":   ("Indonesia", "Southeast Asia", "Asia"),
    "Q43":    ("Turkey", "West Asia", "Asia"),
    "Q212":   ("Ukraine", "Eastern Europe", "Europe"),
    "Q213":   ("Czech Republic", "Eastern Europe", "Europe"),
    "Q28":    ("Hungary", "Eastern Europe", "Europe"),
    "Q218":   ("Romania", "Eastern Europe", "Europe"),
    "Q27":    ("Ireland", "Northern Europe", "Europe"),
    "Q33":    ("Finland", "Northern Europe", "Europe"),
    "Q232":   ("Kazakhstan", "Central Asia", "Asia"),
    "Q419":   ("Peru", "South America", "Americas"),
    "Q241":   ("Cuba", "Caribbean", "Americas"),
    "Q114":   ("Kenya", "East Africa", "Africa"),
    "Q924":   ("Tanzania", "East Africa", "Africa"),
    "Q298":   ("Chile", "South America", "Americas"),
    "Q414":   ("Argentina", "South America", "Americas"),
    "Q717":   ("Venezuela", "South America", "Americas"),
    "Q739":   ("Colombia", "South America", "Americas"),
    "Q813":   ("Kyrgyzstan", "Central Asia", "Asia"),
    "Q865":   ("Taiwan", "East Asia", "Asia"),
    "Q928":   ("Philippines", "Southeast Asia", "Asia"),
    "Q854":   ("Sri Lanka", "South Asia", "Asia"),
    "Q837":   ("Nepal", "South Asia", "Asia"),
    "Q948":   ("Tunisia", "North Africa", "Africa"),
    "Q1028":  ("Morocco", "North Africa", "Africa"),
    "Q1030":  ("Senegal", "West Africa", "Africa"),
}

DEFAULT_GEO = ("Global", "Global", "Global")


# ═══════════════════════════════════════════════════════════════════
# Helper functions
# ═══════════════════════════════════════════════════════════════════

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


def compute_significance(sitelinks: int, year: int | None) -> int:
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
    if year is not None:
        if year < -1000:
            score += 2
        elif year < 500:
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
    year_val = int(year_s)
    if sign == "-" or (sign == "+" and year_val < 0):
        return f"{abs(year_val)} BCE"
    if year_val > 0 and year_val < 100:
        return f"{year_val} CE"
    if month == "01" and day == "01":
        return f"{year_val} CE" if year_val < 1000 else str(year_val)
    return f"{year_val}-{month}-{day}"


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
    return ("110", "Economic Theories & Systems")


# ═══════════════════════════════════════════════════════════════════
# Sub-division refinement
# ═══════════════════════════════════════════════════════════════════

def refine_division(
    div_code: str,
    div_heading: str,
    name: str,
    description: str,
    type_label: str,
) -> tuple[str, str]:
    text = f"{name} {description} {type_label}".lower()

    # 110 → 111-115
    if div_code == "110":
        if any(w in text for w in ("mercantil", "protectionism", "trade theory", "trade policy", "commercial")):
            return ("111", "Mercantilism & Trade Theory")
        if any(w in text for w in ("classical econom", "neoclassic", "laissez", "free market",
                                    "capitalism", "liberal", "austrian school", "supply-side")):
            return ("112", "Classical & Neoclassical Economics")
        if any(w in text for w in ("marx", "socialist", "communist", "anarchi", "trotskyism",
                                    "leninism", "maoism", "stalini")):
            return ("113", "Marxism & Socialist Economics")
        if any(w in text for w in ("keynesian", "monetar", "fiscal policy", "monetary policy",
                                    "macroeconomic", "central bank")):
            return ("114", "Keynesian & Monetary Economics")
        if any(w in text for w in ("agricultur", "land", "physiocra", "feudal", "agrarian",
                                    "collectiviz", "land reform")):
            return ("115", "Agricultural & Land Economics")
        return div_code, div_heading

    # 120 → 121-126
    if div_code == "120":
        if any(w in text for w in ("natural philosophy", "aristotelian", "metaphysic",
                                    "epistemolog", "ontolog", "logic", "philosophy of science")):
            return ("121", "Natural Philosophy & Classical Science")
        if any(w in text for w in ("astronom", "cosmolog", "heliocent", "geocent", "big bang",
                                    "astrophysic", "celestial")):
            return ("122", "Astronomy & Cosmology")
        if any(w in text for w in ("physic", "mechanic", "quantum", "relativity", "thermodynamic",
                                    "electromagnetic", "optic", "nuclear", "particle")):
            return ("123", "Physics & Mechanics")
        if any(w in text for w in ("chemist", "alchem", "periodic", "element", "organic chem",
                                    "biochem", "electrochemist", "pharmacolog")):
            return ("124", "Chemistry & Alchemy")
        if any(w in text for w in ("biology", "evolution", "natural selection", "genetic", "cell ",
                                    "ecolog", "botan", "zoolog", "microbiolog", "paleontolog")):
            return ("125", "Biology & Evolution")
        if any(w in text for w in ("medicine", "medical", "germ theory", "vaccin", "public health",
                                    "patholog", "surgery", "epidemiolog", "psychiatr", "immunolog")):
            return ("126", "Medicine & Public Health")
        return div_code, div_heading

    # 130 → 131-136
    if div_code == "130":
        if any(w in text for w in ("agriculture", "farm", "irrigation", "crop", "aquacultur",
                                    "horticult", "fertiliz", "pesticid")):
            return ("131", "Agricultural Technology")
        if any(w in text for w in ("manufactur", "industrial", "factory", "assembly", "metallurg",
                                    "pottery", "steel", "textile", "mining")):
            return ("132", "Manufacturing & Industrial")
        if any(w in text for w in ("transport", "navigat", "railroad", "ship", "aviation",
                                    "aircraft", "automobile", "shipbuild")):
            return ("133", "Transportation & Navigation")
        if any(w in text for w in ("communic", "printing", "telegraph", "telephone", "internet",
                                    "photograph", "journalism", "broadcast", "radio", "television")):
            return ("134", "Communication & Information")
        if any(w in text for w in ("military", "weapon", "strateg", "defense", "fortif",
                                    "gunpowder", "ballistic", "nuclear weapon", "missile")):
            return ("135", "Military Technology")
        if any(w in text for w in ("comput", "digital", "artificial intell", "software", "algorithm",
                                    "encrypt", "database", "operating system", "programming", "robot")):
            return ("136", "Computing & Digital Technology")
        return div_code, div_heading

    # 140 → 141-145
    if div_code == "140":
        if any(w in text for w in ("monotheism", "abrahamic", "christian", "islam", "judai",
                                    "protestant", "catholic", "orthodox", "evangelical", "quran",
                                    "bible", "torah", "church", "mosque", "synagogue")):
            return ("141", "Monotheism & Abrahamic Theology")
        if any(w in text for w in ("polytheism", "pantheon", "mythology", "animism", "pagan",
                                    "shamanis", "totemism", "pantheism", "folk religion")):
            return ("142", "Polytheism & Mythology")
        if any(w in text for w in ("dharmic", "confucian", "taois", "buddhis", "hindu", "jain",
                                    "sikh", "shinto", "vedanta", "zen", "tibetan")):
            return ("143", "Eastern Philosophy & Dharmic Thought")
        if any(w in text for w in ("mystic", "esoteric", "occult", "sufi", "kabbalah", "gnostic",
                                    "hermetic", "rosicrucian", "freemason", "neoplatoni", "theosophy")):
            return ("144", "Mysticism & Esotericism")
        if any(w in text for w in ("humanism", "secular", "atheism", "agnostic", "existential",
                                    "rationalism", "empiricism", "materialism", "idealism",
                                    "positivism", "phenomenol", "stoicism", "skepticism",
                                    "determinism", "nihilism", "pragmatis", "transhuman")):
            return ("145", "Secular & Humanist Philosophy")
        return div_code, div_heading

    # 150 → 151-155
    if div_code == "150":
        if any(w in text for w in ("sociology", "social class", "stratification", "functional",
                                    "demograph", "criminolog", "social norm")):
            return ("151", "Sociology & Social Structure")
        if any(w in text for w in ("anthropolog", "ethnograph", "structural", "cultural stud",
                                    "archaeolog", "human geograph")):
            return ("152", "Anthropology & Ethnography")
        if any(w in text for w in ("linguist", "semiotic", "language", "phonolog", "syntax",
                                    "semantic", "philolog", "sociolinguist")):
            return ("153", "Linguistics & Language Theory")
        if any(w in text for w in ("psycholog", "behavior", "psychoanaly", "cognitive",
                                    "neuropsych", "neuroscien")):
            return ("154", "Psychology & Human Behavior")
        if any(w in text for w in ("education", "pedagog", "school", "teaching", "didactic",
                                    "curriculum", "literacy")):
            return ("155", "Education & Pedagogy")
        return div_code, div_heading

    # 160 → 161-163
    if div_code == "160":
        if any(w in text for w in ("conservation", "preservation", "protect", "biodiversity",
                                    "national park", "nature reserve", "wildlife", "endangered")):
            return ("161", "Conservation & Preservation")
        if any(w in text for w in ("climate", "atmospheric", "greenhouse", "warming", "meteorolog",
                                    "ozone")):
            return ("162", "Climate & Atmospheric Science")
        if any(w in text for w in ("sustainab", "resource manage", "renewable", "recycl",
                                    "circular economy", "permaculture", "water manage")):
            return ("163", "Sustainability & Resource Management")
        return div_code, div_heading

    # 170 → 171-173
    if div_code == "170":
        if any(w in text for w in ("classical", "neoclassic", "renaissance", "baroque",
                                    "greco-roman", "manneris", "rococo")):
            return ("171", "Classical & Renaissance Aesthetics")
        if any(w in text for w in ("modern", "avant-garde", "impressioni", "expression", "cubis",
                                    "surreal", "abstract", "art nouveau", "art deco", "futuris",
                                    "dadais", "bauhaus", "constructivis", "symbolism", "realis",
                                    "romantic", "naturalis", "fauvis", "pop art", "minimal")):
            return ("172", "Modernism & Avant-Garde")
        if any(w in text for w in ("postmodern", "deconstruct", "post-structur", "contemporar",
                                    "conceptual art", "street art", "installation art", "digital art",
                                    "critical theory")):
            return ("173", "Postmodernism & Deconstruction")
        return div_code, div_heading

    return div_code, div_heading


# ═══════════════════════════════════════════════════════════════════
# SPARQL query builders
# ═══════════════════════════════════════════════════════════════════

def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5) -> str:
    """Standard P31 (instance-of) query."""
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception
       ?country ?countryLabel
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
  OPTIONAL {{ ?item wdt:P17  ?country . }}
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


def build_subclass_query(type_qids: list[str], limit: int, min_sitelinks: int = 2) -> str:
    """P31 UNION P279 (instance-of OR subclass-of) for broader coverage."""
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception
       ?country ?countryLabel
       ?founderLabel
       ?image
       ?article
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  {{ ?item wdt:P31 ?type . }}
  UNION
  {{ ?item wdt:P279 ?type . }}
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P571 ?inception . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
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


def fetch_adaptive(type_qids: list[str], target_limit: int,
                   min_sl: int, use_subclass: bool = False) -> list[dict[str, Any]]:
    limits = [target_limit]
    lim = target_limit
    while lim > 500:
        lim = lim // 2
        limits.append(lim)
    limits.append(500)

    for lim in limits:
        if use_subclass:
            query = build_subclass_query(type_qids, limit=lim, min_sitelinks=min_sl)
        else:
            query = build_sparql_query(type_qids, limit=lim, min_sitelinks=min_sl)
        rows = fetch_sparql(query, retries=2)
        if rows:
            return rows
        if lim > 500:
            print(f"    Reducing limit: {lim} -> {lim // 2}")
    return []


# ═══════════════════════════════════════════════════════════════════
# Transform: SPARQL row -> Annals entity
# ═══════════════════════════════════════════════════════════════════

def transform_idea(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""
    inception_raw = binding_val(row, "inception")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    founder_name = binding_val(row, "founderLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    # Filter non-ideas
    desc_lower = description.lower()
    if any(kw in desc_lower for kw in NON_IDEAS_KEYWORDS):
        return None
    if founder_name and re.match(r'^Q\d+$', founder_name):
        founder_name = ""

    origin_year = parse_year(inception_raw)
    origin_display = format_date_display(inception_raw)
    era, era_slug = year_to_era(origin_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine to sub-divisions
    div_code, div_heading = refine_division(div_code, div_heading, name, description, type_label)

    slug = make_slug(name)

    # Framework assignment by division range
    div_int = int(div_code)
    if div_int < 120:
        framework = "ECONOMIC_THEORY"
    elif div_int < 140:
        framework = "SCIENTIFIC_PARADIGM"
    elif div_int < 150:
        framework = "RELIGIOUS_STUDIES"
    elif div_int < 160:
        framework = "SOCIAL_THEORY"
    elif div_int < 170:
        framework = "ENVIRONMENTAL_THEORY"
    else:
        framework = "AESTHETIC_THEORY"

    # Build summary
    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if founder_name:
        summary += f" Founded by {founder_name}."
    if country_name != "Global":
        summary += f" Associated with {country_name}."
    if origin_year:
        if origin_year < 0:
            summary += f" Originating c. {abs(origin_year)} BCE."
        else:
            summary += f" Originating c. {origin_year} CE."

    sig_score = compute_significance(sitelinks, origin_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Idea",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Idea -- {div_heading} -- {country_name} -- {era}"],
        "subjects": [s for s in [country_name, type_label, continent, div_heading] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": [framework],
        "causes": [],
        "effects": [],
        "relationships": [],
        "places": [],
        "texts": [],
        "ideaType": type_label,
        "ideaClass": 1,
        "ideaClassHeading": "Ideas – Other Theories",
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if origin_display:
        entity["originDate"] = origin_display
    if origin_year is not None:
        entity["originYear"] = origin_year
    if founder_name:
        entity["founder"] = founder_name
    if country_name and country_name != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}",
            "targetName": country_name,
            "context": f"{name} from {country_name}",
        })
        entity["places"].append({"name": country_name, "role": "Country"})
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url
    if image_url:
        entity["imageUrl"] = image_url

    return entity


# ═══════════════════════════════════════════════════════════════════
# Progressive save helper
# ═══════════════════════════════════════════════════════════════════

def save_progress(entities: list[dict], output_path: Path, total_raw: int) -> None:
    progress_path = output_path.with_suffix(".progress.json")
    data = {
        "_meta": {
            "status": "in_progress",
            "total_raw_results": total_raw,
            "total_unique_entities": len(entities),
            "saved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "entities": entities,
    }
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [progress saved: {len(entities)} entities]")


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Fetch Class 1 Ideas (Other) from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = (Path(args.output) if args.output
                   else project_root / "data" / "wikidata_ideas_other.json")

    total_qids = len(set(
        qid for qids, _, _ in IDEAS_OTHER_QUERIES.values() for qid in qids
    ))

    print("=" * 70)
    print("  Wikidata Ideas (Other) Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Class:               1 — Ideas (Other: Economic, Scientific, etc.)")
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(IDEAS_OTHER_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   110-173 (all Class 1 sub-divisions)")
    print(f"  P279 subclass:       Yes (for gap-filling batches)")
    print(f"  Adaptive fallback:   Yes")
    print(f"  Progressive save:    Every 5 batches")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_idx = 0

    for batch_name, (type_qids, min_sl, use_subclass) in IDEAS_OTHER_QUERIES.items():
        batch_idx += 1
        sub_tag = " [P279]" if use_subclass else ""
        print(f"[{batch_idx}/{len(IDEAS_OTHER_QUERIES)}] {batch_name}  "
              f"{len(type_qids)} type(s), sitelinks>{min_sl}{sub_tag} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl, use_subclass)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_idea(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        print(f"  -> {batch_count} unique (total: {len(all_entities)})")

        if batch_idx % 5 == 0:
            save_progress(all_entities, output_path, total_raw)

        time.sleep(2)

    if args.dry_run:
        print("\nDry run complete.")
        print(f"  Would query {len(IDEAS_OTHER_QUERIES)} batches "
              f"with {total_qids} unique QIDs")
        return

    # Sort by division, then name
    all_entities.sort(key=lambda e: (int(e["divisionCode"]), e["name"]))

    # Compute statistics
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    sig_dist: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        sl = e["historicalSignificance"]["label"]
        sig_dist[sl] = sig_dist.get(sl, 0) + 1
        ct = e.get("continent", "Global")
        continent_counts[ct] = continent_counts.get(ct, 0) + 1

    # Write final output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "1.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Idea",
            "classCode": 1,
            "classHeading": "Ideas – Other Theories",
            "type_qids_queried": total_qids,
            "batches_queried": len(IDEAS_OTHER_QUERIES),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "note": (
                "Dedicated Class 1 Wikidata ideas fetch v1.0 covering "
                "divisions 110-173 with P31+P279 strategies."
            ),
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Clean up progress file
    progress_path = output_path.with_suffix(".progress.json")
    if progress_path.exists():
        progress_path.unlink()

    # ── Summary ──
    print()
    print("=" * 70)
    print("  Fetch Complete -- Class 1 Ideas (Other) v1.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
    print(f"  Output:            {output_path}")
    print()
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2,
                 "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    print("  By era:")
    for era_name, count in sorted(era_counts.items(),
                                   key=lambda x: era_order.get(x[0], 9)):
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

    top15 = sorted(all_entities,
                   key=lambda e: (-e["historicalSignificance"]["score"], e["name"]))[:15]
    print("  Top 15 by historical significance:")
    for i, e in enumerate(top15, 1):
        sig = e["historicalSignificance"]
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] "
              f"{e['name']} ({e['divisionHeading']})")


if __name__ == "__main__":
    main()
