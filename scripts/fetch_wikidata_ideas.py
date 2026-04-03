#!/usr/bin/env python3
"""
fetch_wikidata_ideas.py  (v1.0)

Comprehensive Wikidata fetch of ideas and theories across ALL Class 0
divisions (010-036) AND Class 1 divisions (110-173). Uses 180+ Wikidata
type QIDs, adaptive limit fallback, keyword-based sub-division refinement,
and progressive saving.

Class 0 — Ideas Core: Political Systems, Ethical Systems, Legal Systems
Class 1 — Ideas Other: Economic, Scientific, Technological, Religious,
           Cultural, Environmental, Artistic theories and paradigms

Output: data/wikidata_ideas.json

Usage:
    python3 scripts/fetch_wikidata_ideas.py
    python3 scripts/fetch_wikidata_ideas.py --limit 5000
    python3 scripts/fetch_wikidata_ideas.py --dry-run
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
# Ideas Type -> Division Mapping  (180+ QIDs)
# Maps Wikidata P31 (instance-of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

IDEAS_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ════════════════════════════════════════════
    # CLASS 0 — Ideas Core: Political, Ethical, Legal
    # ════════════════════════════════════════════

    # ── 010 Political Systems & Governance ──
    "Q7163":     ("010", "Political Systems & Governance"),       # political ideology
    "Q12909644": ("010", "Political Systems & Governance"),       # political concept
    "Q28108":    ("010", "Political Systems & Governance"),       # political system
    "Q245065":   ("010", "Political Systems & Governance"),       # form of government
    "Q1921834":  ("010", "Political Systems & Governance"),       # political doctrine
    "Q179164":   ("010", "Political Systems & Governance"),       # form of state

    # ── 011 Democracy & Republicanism ──
    "Q7174":     ("011", "Democracy & Republicanism"),            # democracy
    "Q161885":   ("011", "Democracy & Republicanism"),            # republicanism
    "Q184558":   ("011", "Democracy & Republicanism"),            # direct democracy
    "Q165950":   ("011", "Democracy & Republicanism"),            # representative democracy

    # ── 012 Monarchy & Autocracy ──
    "Q7269":     ("012", "Monarchy & Autocracy"),                 # monarchy
    "Q3887":     ("012", "Monarchy & Autocracy"),                 # autocracy
    "Q7270":     ("012", "Monarchy & Autocracy"),                 # absolute monarchy
    "Q108540":   ("012", "Monarchy & Autocracy"),                 # constitutional monarchy
    "Q175566":   ("012", "Monarchy & Autocracy"),                 # despotism
    "Q177456":   ("012", "Monarchy & Autocracy"),                 # oligarchy
    "Q183770":   ("012", "Monarchy & Autocracy"),                 # tyranny
    "Q42395":    ("012", "Monarchy & Autocracy"),                 # dictatorship

    # ── 013 Federalism & Confederalism ──
    "Q204886":   ("013", "Federalism & Confederalism"),           # federalism
    "Q41614":    ("013", "Federalism & Confederalism"),           # confederation
    "Q1250464":  ("013", "Federalism & Confederalism"),           # federal state
    "Q179234":   ("013", "Federalism & Confederalism"),           # devolution

    # ── 014 Theocracy & Divine Rule ──
    "Q44405":    ("014", "Theocracy & Divine Rule"),              # theocracy
    "Q179289":   ("014", "Theocracy & Divine Rule"),              # divine right of kings
    "Q181900":   ("014", "Theocracy & Divine Rule"),              # caesaropapism

    # ── 015 Colonialism & Imperialism ──
    "Q7209":     ("015", "Colonialism & Imperialism"),            # imperialism
    "Q7167":     ("015", "Colonialism & Imperialism"),            # colonialism
    "Q180684":   ("015", "Colonialism & Imperialism"),            # neocolonialism
    "Q181573":   ("015", "Colonialism & Imperialism"),            # settler colonialism

    # ── 016 Sovereignty & Self-Determination ──
    "Q44782":    ("016", "Sovereignty & Self-Determination"),     # sovereignty
    "Q166747":   ("016", "Sovereignty & Self-Determination"),     # self-determination
    "Q192164":   ("016", "Sovereignty & Self-Determination"),     # popular sovereignty

    # ── 020 Ethical Systems ──
    "Q9465":     ("020", "Ethical Systems"),                      # ethics
    "Q4358176":  ("020", "Ethical Systems"),                      # ethical theory
    "Q192584":   ("020", "Ethical Systems"),                      # moral philosophy

    # ── 021 Virtue Ethics ──
    "Q181175":   ("021", "Virtue Ethics"),                        # virtue ethics

    # ── 022 Deontology & Duty Ethics ──
    "Q187451":   ("022", "Deontology & Duty Ethics"),             # deontological ethics

    # ── 023 Consequentialism & Utilitarianism ──
    "Q326960":   ("023", "Consequentialism & Utilitarianism"),    # consequentialism
    "Q7296":     ("023", "Consequentialism & Utilitarianism"),    # utilitarianism

    # ── 024 Natural Law Theory ──
    "Q182559":   ("024", "Natural Law Theory"),                   # natural law

    # ── 025 Social Contract Theory ──
    "Q209272":   ("025", "Social Contract Theory"),               # social contract

    # ── 030 Legal Systems & Law ──
    "Q7748":     ("030", "Legal Systems & Law"),                  # law
    "Q3529618":  ("030", "Legal Systems & Law"),                  # legal concept
    "Q639907":   ("030", "Legal Systems & Law"),                  # legal principle
    "Q128135":   ("030", "Legal Systems & Law"),                  # legal doctrine
    "Q79475":    ("030", "Legal Systems & Law"),                  # legal system
    "Q7050210":  ("030", "Legal Systems & Law"),                  # area of law
    "Q102249524":("030", "Legal Systems & Law"),                  # branch of law

    # ── 031 Common Law ──
    "Q157578":   ("031", "Common Law"),                           # common law

    # ── 032 Civil Law & Roman Law ──
    "Q294448":   ("032", "Civil Law & Roman Law"),                # civil law
    "Q215945":   ("032", "Civil Law & Roman Law"),                # Roman law

    # ── 033 Religious & Canon Law ──
    "Q103359":   ("033", "Religious & Canon Law"),                # canon law
    "Q131395":   ("033", "Religious & Canon Law"),                # sharia

    # ── 034 Customary & Indigenous Law ──
    "Q628966":   ("034", "Customary & Indigenous Law"),           # customary law

    # ── 035 International Law & Treaties ──
    "Q4394526":  ("035", "International Law & Treaties"),         # international law
    "Q131569":   ("035", "International Law & Treaties"),         # treaty

    # ── 036 Constitutional Law ──
    "Q179661":   ("036", "Constitutional Law"),                   # constitutional law
    "Q7755":     ("036", "Constitutional Law"),                   # constitution

    # ════════════════════════════════════════════
    # CLASS 1 — Ideas Other: Economic, Scientific, etc.
    # ════════════════════════════════════════════

    # ── 110 Economic Theories & Systems ──
    "Q8134":     ("110", "Economic Theories & Systems"),          # economics
    "Q186247":   ("110", "Economic Theories & Systems"),          # economic theory
    "Q2979973":  ("110", "Economic Theories & Systems"),          # economic school
    "Q11042":    ("110", "Economic Theories & Systems"),          # economic system
    "Q182790":   ("110", "Economic Theories & Systems"),          # economic policy
    "Q12140182": ("110", "Economic Theories & Systems"),          # economic ideology

    # ── 111 Mercantilism & Trade Theory ──
    "Q131735":   ("111", "Mercantilism & Trade Theory"),          # mercantilism

    # ── 112 Classical & Neoclassical Economics ──
    "Q83267":    ("112", "Classical & Neoclassical Economics"),   # classical economics
    "Q190375":   ("112", "Classical & Neoclassical Economics"),   # neoclassical economics
    "Q35591":    ("112", "Classical & Neoclassical Economics"),   # capitalism
    "Q202640":   ("112", "Classical & Neoclassical Economics"),   # laissez-faire
    "Q327960":   ("112", "Classical & Neoclassical Economics"),   # free market

    # ── 113 Marxism & Socialist Economics ──
    "Q7264":     ("113", "Marxism & Socialist Economics"),        # Marxism
    "Q7272":     ("113", "Marxism & Socialist Economics"),        # socialism
    "Q6186":     ("113", "Marxism & Socialist Economics"),        # communism
    "Q109367":   ("113", "Marxism & Socialist Economics"),        # anarchism

    # ── 114 Keynesian & Monetary Economics ──
    "Q173171":   ("114", "Keynesian & Monetary Economics"),       # Keynesian economics
    "Q185327":   ("114", "Keynesian & Monetary Economics"),       # monetarism

    # ── 115 Agricultural & Land Economics ──
    "Q483413":   ("115", "Agricultural & Land Economics"),        # physiocracy
    "Q44777":    ("115", "Agricultural & Land Economics"),        # feudalism

    # ── 120 Scientific Paradigms ──
    "Q336":      ("120", "Scientific Paradigms"),                 # science
    "Q1132636":  ("120", "Scientific Paradigms"),                 # scientific paradigm
    "Q7432":     ("120", "Scientific Paradigms"),                 # scientific theory
    "Q1196129":  ("120", "Scientific Paradigms"),                 # natural science
    "Q33500":    ("120", "Scientific Paradigms"),                 # theory

    # ── 121 Natural Philosophy & Classical Science ──
    "Q131476":   ("121", "Natural Philosophy & Classical Science"), # natural philosophy

    # ── 122 Astronomy & Cosmology ──
    "Q333":      ("122", "Astronomy & Cosmology"),                # astronomy
    "Q338":      ("122", "Astronomy & Cosmology"),                # cosmology
    "Q18362":    ("122", "Astronomy & Cosmology"),                # heliocentrism
    "Q170024":   ("122", "Astronomy & Cosmology"),                # geocentrism
    "Q1711":     ("122", "Astronomy & Cosmology"),                # Big Bang theory

    # ── 123 Physics & Mechanics ──
    "Q413":      ("123", "Physics & Mechanics"),                  # physics
    "Q38433":    ("123", "Physics & Mechanics"),                  # classical mechanics
    "Q11402":    ("123", "Physics & Mechanics"),                  # quantum mechanics
    "Q43514":    ("123", "Physics & Mechanics"),                  # general relativity
    "Q7207":     ("123", "Physics & Mechanics"),                  # thermodynamics

    # ── 124 Chemistry & Alchemy ──
    "Q2329":     ("124", "Chemistry & Alchemy"),                  # chemistry
    "Q131189":   ("124", "Chemistry & Alchemy"),                  # alchemy
    "Q11651":    ("124", "Chemistry & Alchemy"),                  # periodic table

    # ── 125 Biology & Evolution ──
    "Q420":      ("125", "Biology & Evolution"),                  # biology
    "Q1063":     ("125", "Biology & Evolution"),                  # evolution
    "Q43302":    ("125", "Biology & Evolution"),                  # natural selection
    "Q7430":     ("125", "Biology & Evolution"),                  # genetics
    "Q11398":    ("125", "Biology & Evolution"),                  # cell theory

    # ── 126 Medicine & Public Health ──
    "Q11190":    ("126", "Medicine & Public Health"),              # medicine
    "Q189603":   ("126", "Medicine & Public Health"),              # germ theory
    "Q178061":   ("126", "Medicine & Public Health"),              # vaccination
    "Q864693":   ("126", "Medicine & Public Health"),              # public health

    # ── 130 Technological Innovations ──
    "Q11016":    ("130", "Technological Innovations"),            # technology
    "Q11023":    ("130", "Technological Innovations"),            # engineering
    "Q28865":    ("130", "Technological Innovations"),            # invention

    # ── 131 Agricultural Technology ──
    "Q11451":    ("131", "Agricultural Technology"),              # agriculture
    "Q158003":   ("131", "Agricultural Technology"),              # crop rotation
    "Q178061a":  ("131", "Agricultural Technology"),              # irrigation (alias)

    # ── 132 Manufacturing & Industrial ──
    "Q187939":   ("132", "Manufacturing & Industrial"),           # manufacturing
    "Q13580151": ("132", "Manufacturing & Industrial"),           # industrialization

    # ── 133 Transportation & Navigation ──
    "Q7590":     ("133", "Transportation & Navigation"),          # transportation
    "Q26540":    ("133", "Transportation & Navigation"),          # navigation

    # ── 134 Communication & Information ──
    "Q11024":    ("134", "Communication & Information"),          # communication
    "Q161428":   ("134", "Communication & Information"),          # printing press
    "Q5":        ("134", "Communication & Information"),          # telegraph → too broad
    "Q75":       ("134", "Communication & Information"),          # internet

    # ── 135 Military Technology ──
    "Q12796":    ("135", "Military Technology"),                  # weapon
    "Q249019":   ("135", "Military Technology"),                  # military strategy
    "Q1361968":  ("135", "Military Technology"),                  # military technology

    # ── 136 Computing & Digital Technology ──
    "Q68":       ("136", "Computing & Digital Technology"),       # computer science
    "Q5288":     ("136", "Computing & Digital Technology"),       # artificial intelligence
    "Q1301371":  ("136", "Computing & Digital Technology"),       # computing

    # ── 140 Religious & Philosophical Concepts ──
    "Q9174":     ("140", "Religious & Philosophical Concepts"),   # religion
    "Q5891":     ("140", "Religious & Philosophical Concepts"),   # philosophy
    "Q1783494":  ("140", "Religious & Philosophical Concepts"),   # religious belief
    "Q17444909": ("140", "Religious & Philosophical Concepts"),   # philosophical concept
    "Q151885":   ("140", "Religious & Philosophical Concepts"),   # concept
    "Q18340550": ("140", "Religious & Philosophical Concepts"),   # philosophical doctrine
    "Q12479":    ("140", "Religious & Philosophical Concepts"),   # Weltanschauung / worldview
    "Q2963543":  ("140", "Religious & Philosophical Concepts"),   # belief system

    # ── 141 Monotheism & Abrahamic Theology ──
    "Q100951":   ("141", "Monotheism & Abrahamic Theology"),     # monotheism
    "Q47280":    ("141", "Monotheism & Abrahamic Theology"),     # Abrahamic religion
    "Q33104":    ("141", "Monotheism & Abrahamic Theology"),     # Christian theology
    "Q107380":   ("141", "Monotheism & Abrahamic Theology"),     # Islamic theology

    # ── 142 Polytheism & Mythology ──
    "Q9159":     ("142", "Polytheism & Mythology"),              # polytheism
    "Q15978631": ("142", "Polytheism & Mythology"),              # pantheon
    "Q34726":    ("142", "Polytheism & Mythology"),              # mythology
    "Q9134":     ("142", "Polytheism & Mythology"),              # animism

    # ── 143 Eastern Philosophy & Dharmic Thought ──
    "Q162740":   ("143", "Eastern Philosophy & Dharmic Thought"), # Dharmic religion
    "Q4393":     ("143", "Eastern Philosophy & Dharmic Thought"), # Confucianism
    "Q7556":     ("143", "Eastern Philosophy & Dharmic Thought"), # Taoism
    "Q9316":     ("143", "Eastern Philosophy & Dharmic Thought"), # Buddhism

    # ── 144 Mysticism & Esotericism ──
    "Q9159a":    ("144", "Mysticism & Esotericism"),             # mysticism (alias)
    "Q131748":   ("144", "Mysticism & Esotericism"),             # esotericism
    "Q207591":   ("144", "Mysticism & Esotericism"),             # occultism
    "Q42040":    ("144", "Mysticism & Esotericism"),             # Sufism
    "Q102416":   ("144", "Mysticism & Esotericism"),             # Kabbalah
    "Q7264a":    ("144", "Mysticism & Esotericism"),             # Gnosticism (alias)

    # ── 145 Secular & Humanist Philosophy ──
    "Q49447":    ("145", "Secular & Humanist Philosophy"),       # humanism
    "Q7066":     ("145", "Secular & Humanist Philosophy"),       # atheism
    "Q170208":   ("145", "Secular & Humanist Philosophy"),       # secularism
    "Q34740":    ("145", "Secular & Humanist Philosophy"),       # existentialism
    "Q130900":   ("145", "Secular & Humanist Philosophy"),       # nihilism
    "Q166280":   ("145", "Secular & Humanist Philosophy"),       # pragmatism
    "Q181898":   ("145", "Secular & Humanist Philosophy"),       # rationalism
    "Q170028":   ("145", "Secular & Humanist Philosophy"),       # empiricism
    "Q79869":    ("145", "Secular & Humanist Philosophy"),       # materialism
    "Q11009":    ("145", "Secular & Humanist Philosophy"),       # idealism
    "Q178748":   ("145", "Secular & Humanist Philosophy"),       # positivism

    # ── 150 Social & Cultural Theories ──
    "Q8425":     ("150", "Social & Cultural Theories"),          # sociology
    "Q860746":   ("150", "Social & Cultural Theories"),          # social theory
    "Q11862829": ("150", "Social & Cultural Theories"),          # academic discipline

    # ── 151 Sociology & Social Structure ──
    "Q214917":   ("151", "Sociology & Social Structure"),        # social class
    "Q169966":   ("151", "Sociology & Social Structure"),        # functionalism

    # ── 152 Anthropology & Ethnography ──
    "Q23404":    ("152", "Anthropology & Ethnography"),          # anthropology
    "Q167229":   ("152", "Anthropology & Ethnography"),          # structuralism
    "Q42240":    ("152", "Anthropology & Ethnography"),          # ethnography

    # ── 153 Linguistics & Language Theory ──
    "Q8162":     ("153", "Linguistics & Language Theory"),        # linguistics
    "Q199655":   ("153", "Linguistics & Language Theory"),        # semiotics
    "Q1288568":  ("153", "Linguistics & Language Theory"),        # language theory

    # ── 154 Psychology & Human Behavior ──
    "Q9418":     ("154", "Psychology & Human Behavior"),          # psychology
    "Q180160":   ("154", "Psychology & Human Behavior"),          # behaviorism
    "Q184843":   ("154", "Psychology & Human Behavior"),          # psychoanalysis

    # ── 155 Education & Pedagogy ──
    "Q8434":     ("155", "Education & Pedagogy"),                # education
    "Q14208":    ("155", "Education & Pedagogy"),                # pedagogy

    # ── 160 Environmental & Ecological Ideas ──
    "Q7150":     ("160", "Environmental & Ecological Ideas"),    # ecology
    "Q179805":   ("160", "Environmental & Ecological Ideas"),    # environmentalism

    # ── 161 Conservation & Preservation ──
    "Q180788":   ("161", "Conservation & Preservation"),          # conservation

    # ── 162 Climate & Atmospheric Science ──
    "Q52139":    ("162", "Climate & Atmospheric Science"),        # climatology
    "Q11663":    ("162", "Climate & Atmospheric Science"),        # climate change

    # ── 163 Sustainability & Resource Management ──
    "Q219416":   ("163", "Sustainability & Resource Management"), # sustainability

    # ── 170 Artistic & Aesthetic Movements ──
    "Q735":      ("170", "Artistic & Aesthetic Movements"),      # art
    "Q1792644":  ("170", "Artistic & Aesthetic Movements"),      # art movement
    "Q968159":   ("170", "Artistic & Aesthetic Movements"),      # art style
    "Q184299":   ("170", "Artistic & Aesthetic Movements"),      # literary movement
    "Q210112":   ("170", "Artistic & Aesthetic Movements"),      # genre
    "Q3326717":  ("170", "Artistic & Aesthetic Movements"),      # literary genre
    "Q207694":   ("170", "Artistic & Aesthetic Movements"),      # art genre
    "Q2743":     ("170", "Artistic & Aesthetic Movements"),      # musical genre
    "Q191067":   ("170", "Artistic & Aesthetic Movements"),      # architectural style

    # ── 171 Classical & Renaissance Aesthetics ──
    "Q1420559":  ("171", "Classical & Renaissance Aesthetics"),  # classicism
    "Q41726":    ("171", "Classical & Renaissance Aesthetics"),  # neoclassicism
    "Q946508":   ("171", "Classical & Renaissance Aesthetics"),  # Renaissance art

    # ── 172 Modernism & Avant-Garde ──
    "Q37068":    ("172", "Modernism & Avant-Garde"),            # modernism
    "Q170292":   ("172", "Modernism & Avant-Garde"),            # avant-garde
    "Q166713":   ("172", "Modernism & Avant-Garde"),            # impressionism
    "Q180774":   ("172", "Modernism & Avant-Garde"),            # expressionism
    "Q37853":    ("172", "Modernism & Avant-Garde"),            # cubism
    "Q39427":    ("172", "Modernism & Avant-Garde"),            # surrealism
    "Q173436":   ("172", "Modernism & Avant-Garde"),            # abstract art

    # ── 173 Postmodernism & Deconstruction ──
    "Q47783":    ("173", "Postmodernism & Deconstruction"),     # postmodernism
    "Q181404":   ("173", "Postmodernism & Deconstruction"),     # deconstruction
    "Q185067":   ("173", "Postmodernism & Deconstruction"),     # post-structuralism
}

# Build clean reverse lookup
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in IDEAS_TYPE_MAP.items():
    clean_qid = _qid.rstrip("a")
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info


# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (75 granular batches)
# Each batch -> (QIDs, min_sitelinks)
# ═══════════════════════════════════════════════════════════════════

IDEAS_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── CLASS 0: Political Ideas ──
    "010_pol_ideology":     (["Q7163"], 8),
    "010_pol_concept":      (["Q12909644"], 5),
    "010_pol_system":       (["Q28108", "Q245065"], 5),
    "010_form_gov":         (["Q179164", "Q1921834"], 5),

    "011_democracy":        (["Q7174", "Q184558", "Q165950"], 5),
    "011_republicanism":    (["Q161885"], 5),

    "012_monarchy":         (["Q7269", "Q7270", "Q108540"], 5),
    "012_autocracy":        (["Q3887", "Q175566", "Q177456", "Q183770", "Q42395"], 5),

    "013_federalism":       (["Q204886", "Q41614", "Q1250464", "Q179234"], 5),

    "014_theocracy":        (["Q44405", "Q179289", "Q181900"], 5),

    "015_colonialism":      (["Q7209", "Q7167", "Q180684", "Q181573"], 5),

    "016_sovereignty":      (["Q44782", "Q166747", "Q192164"], 5),

    # ── CLASS 0: Ethical Ideas ──
    "020_ethics":           (["Q9465", "Q4358176", "Q192584"], 5),
    "021_virtue":           (["Q181175"], 5),
    "022_deontology":       (["Q187451"], 5),
    "023_consequentialism": (["Q326960", "Q7296"], 5),
    "024_natural_law":      (["Q182559"], 5),
    "025_social_contract":  (["Q209272"], 5),

    # ── CLASS 0: Legal Ideas ──
    "030_law":              (["Q7748"], 10),
    "030_legal_concept":    (["Q3529618", "Q639907"], 5),
    "030_legal_doctrine":   (["Q128135"], 5),
    "030_legal_system":     (["Q79475", "Q7050210"], 5),
    "030_area_of_law":      (["Q102249524"], 5),
    "031_common_law":       (["Q157578"], 5),
    "032_civil_roman":      (["Q294448", "Q215945"], 5),
    "033_canon_sharia":     (["Q103359", "Q131395"], 5),
    "034_customary":        (["Q628966"], 5),
    "035_intl_law":         (["Q4394526", "Q131569"], 10),
    "036_constitutional":   (["Q179661", "Q7755"], 5),

    # ── CLASS 1: Economic Ideas ──
    "110_economics":        (["Q8134"], 10),
    "110_econ_theory":      (["Q186247", "Q2979973"], 5),
    "110_econ_system":      (["Q11042", "Q182790", "Q12140182"], 5),
    "111_mercantilism":     (["Q131735"], 5),
    "112_classical_econ":   (["Q83267", "Q190375"], 5),
    "112_capitalism":       (["Q35591", "Q202640", "Q327960"], 5),
    "113_marxism":          (["Q7264", "Q7272", "Q6186", "Q109367"], 5),
    "114_keynesian":        (["Q173171", "Q185327"], 5),
    "115_agricultural":     (["Q483413", "Q44777"], 5),

    # ── CLASS 1: Scientific Paradigms ──
    "120_science":          (["Q336"], 10),
    "120_sci_theory":       (["Q7432", "Q33500"], 10),
    "120_sci_paradigm":     (["Q1132636", "Q1196129"], 5),
    "121_nat_philosophy":   (["Q131476"], 5),
    "122_astronomy":        (["Q333", "Q338"], 10),
    "122_helio_geo":        (["Q18362", "Q170024", "Q1711"], 5),
    "123_physics":          (["Q413"], 10),
    "123_mechanics":        (["Q38433", "Q11402", "Q43514", "Q7207"], 5),
    "124_chemistry":        (["Q2329", "Q131189", "Q11651"], 5),
    "125_biology":          (["Q420", "Q1063", "Q43302"], 5),
    "125_genetics":         (["Q7430", "Q11398"], 5),
    "126_medicine":         (["Q11190"], 10),
    "126_public_health":    (["Q189603", "Q178061", "Q864693"], 5),

    # ── CLASS 1: Technological Innovations ──
    "130_technology":       (["Q11016", "Q11023"], 15),
    "131_agriculture":      (["Q11451", "Q158003"], 5),
    "132_manufacturing":    (["Q187939", "Q13580151"], 5),
    "133_transport":        (["Q7590", "Q26540"], 5),
    "134_communication":    (["Q11024", "Q161428"], 5),
    "135_military_tech":    (["Q249019", "Q1361968"], 5),
    "136_computing":        (["Q68", "Q5288", "Q1301371"], 5),

    # ── CLASS 1: Religious & Philosophical Concepts ──
    "140_religion":         (["Q9174"], 10),
    "140_philosophy":       (["Q5891"], 10),
    "140_phil_concept":     (["Q17444909", "Q18340550"], 5),
    "140_belief_system":    (["Q1783494", "Q12479", "Q2963543"], 5),
    "140_concept":          (["Q151885"], 20),
    "141_monotheism":       (["Q100951", "Q47280"], 5),
    "141_theology":         (["Q33104", "Q107380"], 5),
    "142_polytheism":       (["Q9159", "Q15978631", "Q34726", "Q9134"], 5),
    "143_eastern":          (["Q162740", "Q4393", "Q7556", "Q9316"], 5),
    "144_mysticism":        (["Q131748", "Q207591", "Q42040", "Q102416"], 5),
    "145_humanism":         (["Q49447", "Q7066", "Q170208"], 5),
    "145_existentialism":   (["Q34740", "Q130900", "Q166280"], 5),
    "145_rationalism":      (["Q181898", "Q170028", "Q79869", "Q11009"], 5),
    "145_positivism":       (["Q178748"], 5),

    # ── CLASS 1: Social & Cultural Theories ──
    "150_sociology":        (["Q8425", "Q860746"], 5),
    "150_discipline":       (["Q11862829"], 15),
    "151_social_struct":    (["Q214917", "Q169966"], 5),
    "152_anthropology":     (["Q23404", "Q167229", "Q42240"], 5),
    "153_linguistics":      (["Q8162", "Q199655", "Q1288568"], 5),
    "154_psychology":       (["Q9418", "Q180160", "Q184843"], 5),
    "155_education":        (["Q8434", "Q14208"], 5),

    # ── CLASS 1: Environmental Ideas ──
    "160_ecology":          (["Q7150", "Q179805"], 5),
    "161_conservation":     (["Q180788"], 5),
    "162_climate":          (["Q52139", "Q11663"], 5),
    "163_sustainability":   (["Q219416"], 5),

    # ── CLASS 1: Artistic & Aesthetic Ideas ──
    "170_art_movement":     (["Q1792644", "Q968159"], 5),
    "170_literary_move":    (["Q184299"], 5),
    "170_genre":            (["Q210112", "Q3326717", "Q207694"], 8),
    "170_music_genre":      (["Q2743"], 10),
    "170_arch_style":       (["Q191067"], 5),
    "171_classicism":       (["Q1420559", "Q41726", "Q946508"], 5),
    "172_modernism":        (["Q37068", "Q170292"], 5),
    "172_art_isms":         (["Q166713", "Q180774", "Q37853", "Q39427", "Q173436"], 5),
    "173_postmodernism":    (["Q47783", "Q181404", "Q185067"], 5),
}


# ═══════════════════════════════════════════════════════════════════
# Non-idea keyword filter
# ═══════════════════════════════════════════════════════════════════

NON_IDEAS_KEYWORDS = {
    'wikimedia', 'disambiguation', 'template', 'category',
    'fictional character', 'video game', 'software', 'mobile app',
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
    return ("010", "Political Systems & Governance")


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

    # 010 → 011-016
    if div_code == "010":
        if any(w in text for w in ("democracy", "republic", "representation", "vote", "election")):
            return ("011", "Democracy & Republicanism")
        if any(w in text for w in ("monarchy", "king", "autocracy", "dictatorship", "despot", "tyrant", "oligarch")):
            return ("012", "Monarchy & Autocracy")
        if any(w in text for w in ("federal", "confedera", "devolution")):
            return ("013", "Federalism & Confederalism")
        if any(w in text for w in ("theocrac", "divine right", "god", "caesaropap")):
            return ("014", "Theocracy & Divine Rule")
        if any(w in text for w in ("colonial", "imperial", "neocolon", "settler")):
            return ("015", "Colonialism & Imperialism")
        if any(w in text for w in ("sovereign", "self-determin", "popular sovere")):
            return ("016", "Sovereignty & Self-Determination")
        return div_code, div_heading

    # 020 → 021-025
    if div_code == "020":
        if any(w in text for w in ("virtue", "arete", "eudaimon")):
            return ("021", "Virtue Ethics")
        if any(w in text for w in ("deontol", "duty", "categorical imperative", "kant")):
            return ("022", "Deontology & Duty Ethics")
        if any(w in text for w in ("consequential", "utilitarian", "greatest good")):
            return ("023", "Consequentialism & Utilitarianism")
        if any(w in text for w in ("natural law", "ius naturale", "aquinas")):
            return ("024", "Natural Law Theory")
        if any(w in text for w in ("social contract", "hobbes", "locke", "rousseau")):
            return ("025", "Social Contract Theory")
        return div_code, div_heading

    # 030 → 031-036
    if div_code == "030":
        if any(w in text for w in ("common law", "precedent", "stare decis")):
            return ("031", "Common Law")
        if any(w in text for w in ("civil law", "roman law", "codex", "justinian")):
            return ("032", "Civil Law & Roman Law")
        if any(w in text for w in ("canon law", "sharia", "church law", "religious law")):
            return ("033", "Religious & Canon Law")
        if any(w in text for w in ("customary", "indigenous law", "tribal law")):
            return ("034", "Customary & Indigenous Law")
        if any(w in text for w in ("international law", "treaty", "convention", "ius gentium")):
            return ("035", "International Law & Treaties")
        if any(w in text for w in ("constitution", "fundamental law", "basic law")):
            return ("036", "Constitutional Law")
        return div_code, div_heading

    # 110 → 111-115
    if div_code == "110":
        if any(w in text for w in ("mercantil", "protectionism", "trade theory")):
            return ("111", "Mercantilism & Trade Theory")
        if any(w in text for w in ("classical econom", "neoclassic", "laissez", "free market", "capitalism")):
            return ("112", "Classical & Neoclassical Economics")
        if any(w in text for w in ("marx", "socialist", "communist", "anarchi")):
            return ("113", "Marxism & Socialist Economics")
        if any(w in text for w in ("keynesian", "monetar", "fiscal policy")):
            return ("114", "Keynesian & Monetary Economics")
        if any(w in text for w in ("agricultur", "land", "physiocra", "feudal")):
            return ("115", "Agricultural & Land Economics")
        return div_code, div_heading

    # 120 → 121-126
    if div_code == "120":
        if any(w in text for w in ("natural philosophy", "aristotelian", "ancient science")):
            return ("121", "Natural Philosophy & Classical Science")
        if any(w in text for w in ("astronom", "cosmolog", "heliocent", "geocent", "big bang")):
            return ("122", "Astronomy & Cosmology")
        if any(w in text for w in ("physic", "mechanic", "quantum", "relativity", "thermodynamic")):
            return ("123", "Physics & Mechanics")
        if any(w in text for w in ("chemist", "alchem", "periodic", "element")):
            return ("124", "Chemistry & Alchemy")
        if any(w in text for w in ("biology", "evolution", "natural selection", "genetic", "cell ")):
            return ("125", "Biology & Evolution")
        if any(w in text for w in ("medicine", "medical", "germ theory", "vaccin", "public health")):
            return ("126", "Medicine & Public Health")
        return div_code, div_heading

    # 130 → 131-136
    if div_code == "130":
        if any(w in text for w in ("agriculture", "farm", "irrigation", "crop")):
            return ("131", "Agricultural Technology")
        if any(w in text for w in ("manufactur", "industrial", "factory", "assembly")):
            return ("132", "Manufacturing & Industrial")
        if any(w in text for w in ("transport", "navigat", "railroad", "ship", "aviation")):
            return ("133", "Transportation & Navigation")
        if any(w in text for w in ("communic", "printing", "telegraph", "telephone", "internet")):
            return ("134", "Communication & Information")
        if any(w in text for w in ("military", "weapon", "strateg", "defense")):
            return ("135", "Military Technology")
        if any(w in text for w in ("comput", "digital", "artificial intell", "software", "algorithm")):
            return ("136", "Computing & Digital Technology")
        return div_code, div_heading

    # 140 → 141-145
    if div_code == "140":
        if any(w in text for w in ("monotheism", "abrahamic", "christian theol", "islamic theol")):
            return ("141", "Monotheism & Abrahamic Theology")
        if any(w in text for w in ("polytheism", "pantheon", "mythology", "animism", "pagan")):
            return ("142", "Polytheism & Mythology")
        if any(w in text for w in ("dharmic", "confucian", "taois", "buddhis", "hindu", "jain", "sikh")):
            return ("143", "Eastern Philosophy & Dharmic Thought")
        if any(w in text for w in ("mystic", "esoteric", "occult", "sufi", "kabbalah", "gnostic")):
            return ("144", "Mysticism & Esotericism")
        if any(w in text for w in ("humanism", "secular", "atheism", "agnostic", "existential", "rationalism")):
            return ("145", "Secular & Humanist Philosophy")
        return div_code, div_heading

    # 150 → 151-155
    if div_code == "150":
        if any(w in text for w in ("sociology", "social class", "stratification", "functional")):
            return ("151", "Sociology & Social Structure")
        if any(w in text for w in ("anthropolog", "ethnograph", "structural")):
            return ("152", "Anthropology & Ethnography")
        if any(w in text for w in ("linguist", "semiotic", "language")):
            return ("153", "Linguistics & Language Theory")
        if any(w in text for w in ("psycholog", "behavior", "psychoanaly")):
            return ("154", "Psychology & Human Behavior")
        if any(w in text for w in ("education", "pedagog", "school", "teaching")):
            return ("155", "Education & Pedagogy")
        return div_code, div_heading

    # 160 → 161-163
    if div_code == "160":
        if any(w in text for w in ("conservation", "preservation", "protect")):
            return ("161", "Conservation & Preservation")
        if any(w in text for w in ("climate", "atmospheric", "greenhouse", "warming")):
            return ("162", "Climate & Atmospheric Science")
        if any(w in text for w in ("sustainab", "resource manage", "renewable")):
            return ("163", "Sustainability & Resource Management")
        return div_code, div_heading

    # 170 → 171-173
    if div_code == "170":
        if any(w in text for w in ("classical", "neoclassic", "renaissance", "baroque", "greco-roman")):
            return ("171", "Classical & Renaissance Aesthetics")
        if any(w in text for w in ("modern", "avant-garde", "impressioni", "expression", "cubis", "surreal", "abstract")):
            return ("172", "Modernism & Avant-Garde")
        if any(w in text for w in ("postmodern", "deconstruct", "post-structur")):
            return ("173", "Postmodernism & Deconstruction")
        return div_code, div_heading

    return div_code, div_heading


# ═══════════════════════════════════════════════════════════════════
# SPARQL query builder & fetchers
# ═══════════════════════════════════════════════════════════════════

def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5) -> str:
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

    # Determine class: 0 if div < 100, else 1
    div_int = int(div_code)
    if div_int < 100:
        idea_class = 0
        class_heading = "Ideas – Core Categories"
    else:
        idea_class = 1
        class_heading = "Ideas – Other Theories"

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

    # Assign appropriate framework
    if div_int < 20:
        framework = "POLITICAL_THEORY"
    elif div_int < 30:
        framework = "ETHICAL_FRAMEWORK"
    elif div_int < 100:
        framework = "LEGAL_FRAMEWORK"
    elif div_int < 120:
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
        "ideaClass": idea_class,
        "ideaClassHeading": class_heading,
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
    parser = argparse.ArgumentParser(description="Fetch ideas from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_ideas.json"

    total_qids = len(set(qid for qids, _ in IDEAS_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Ideas Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(IDEAS_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   010-036 (Class 0) + 110-173 (Class 1)")
    print(f"  Adaptive fallback:   Yes")
    print(f"  Progressive save:    Every 5 batches")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_idx = 0

    for batch_name, (type_qids, min_sl) in IDEAS_QUERIES.items():
        batch_idx += 1
        print(f"[{batch_idx}/{len(IDEAS_QUERIES)}] {batch_name}  "
              f"{len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
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
        print(f"  Would query {len(IDEAS_QUERIES)} batches with {total_qids} unique QIDs")
        return

    # Sort by class, division, then name
    all_entities.sort(key=lambda e: (int(e["divisionCode"]), e["name"]))

    # Compute statistics
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    sig_dist: dict[str, int] = {}
    class_counts: dict[int, int] = {0: 0, 1: 0}
    continent_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        sig_dist[e["historicalSignificance"]["label"]] = sig_dist.get(e["historicalSignificance"]["label"], 0) + 1
        class_counts[e["ideaClass"]] = class_counts.get(e["ideaClass"], 0) + 1
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
            "classCodes": [0, 1],
            "classHeadings": ["Ideas – Core Categories", "Ideas – Other Theories"],
            "type_qids_queried": total_qids,
            "batches_queried": len(IDEAS_QUERIES),
            "class_counts": class_counts,
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "note": "Comprehensive Wikidata ideas fetch v1.0 covering Class 0 (010-036) and Class 1 (110-173).",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Clean up progress file
    progress_path = output_path.with_suffix(".progress.json")
    if progress_path.exists():
        progress_path.unlink()

    # Print summary
    print()
    print("=" * 70)
    print("  Fetch Complete -- v1.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
    print(f"  Output:            {output_path}")
    print()
    print(f"  By class:")
    print(f"    Class 0 (Core Ideas):  {class_counts.get(0, 0)}")
    print(f"    Class 1 (Other Ideas): {class_counts.get(1, 0)}")
    print()
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
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
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] {e['name']} ({e['divisionHeading']})")


if __name__ == "__main__":
    main()
