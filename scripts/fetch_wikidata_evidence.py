#!/usr/bin/env python3
"""
fetch_wikidata_evidence.py  (v1.0)

Comprehensive Wikidata fetch of documented evidence across ALL Class 8
divisions (810-853). Uses 90+ Wikidata type QIDs, adaptive limit fallback,
keyword-based sub-division refinement, and progressive saving.

Covers: Inscriptions & Epigraphy, Letters & Correspondence, Official Records,
Diaries & Memoirs, Eyewitness Accounts, Academic Monographs, Scholarly
Articles, Encyclopedias, Archaeological Evidence, Quantitative Data,
Oral Traditions, Folklore, Genealogies.

Output: data/wikidata_evidence.json

Usage:
    python3 scripts/fetch_wikidata_evidence.py
    python3 scripts/fetch_wikidata_evidence.py --limit 5000
    python3 scripts/fetch_wikidata_evidence.py --dry-run
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
# Evidence Type -> Division Mapping  (90+ QIDs)
# Maps Wikidata P31 (instance of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

EVIDENCE_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 810 Primary Sources (general) ──
    "Q49848":     ("810", "Primary Sources"),                       # document
    "Q87167":     ("810", "Primary Sources"),                       # manuscript

    # ── 811 Inscriptions & Epigraphy ──
    "Q47721":     ("811", "Inscriptions & Epigraphy"),              # inscription
    "Q4523831":   ("811", "Inscriptions & Epigraphy"),              # cuneiform inscription
    "Q2078983":   ("811", "Inscriptions & Epigraphy"),              # clay tablet
    "Q105320460": ("811", "Inscriptions & Epigraphy"),              # ostracon
    "Q378436":    ("811", "Inscriptions & Epigraphy"),              # rubbing / epigraph copy
    "Q928357":    ("811", "Inscriptions & Epigraphy"),              # stele (epigraphic)
    "Q193977":    ("811", "Inscriptions & Epigraphy"),              # seal (official)
    "Q28935506":  ("811", "Inscriptions & Epigraphy"),              # stone inscription
    "Q4884":      ("811", "Inscriptions & Epigraphy"),              # coin (numismatic evidence)
    "Q217164":    ("811", "Inscriptions & Epigraphy"),              # medallion

    # ── 812 Letters & Correspondence ──
    "Q133492":    ("812", "Letters & Correspondence"),              # letter
    "Q749711":    ("812", "Letters & Correspondence"),              # encyclical
    "Q1269656":   ("812", "Letters & Correspondence"),              # papal bull
    "Q12045845":  ("812", "Letters & Correspondence"),              # epistle
    "Q37219":     ("812", "Letters & Correspondence"),              # petition
    "Q1144661":   ("812", "Letters & Correspondence"),              # diplomatic note
    "Q17376908":  ("812", "Letters & Correspondence"),              # personal letter

    # ── 813 Official Records & Archives ──
    "Q820655":    ("813", "Official Records & Archives"),           # decree
    "Q835327":    ("813", "Official Records & Archives"),           # edict
    "Q47577":     ("813", "Official Records & Archives"),           # deed / charter
    "Q3514032":   ("813", "Official Records & Archives"),           # patent (letters patent)
    "Q166118":    ("813", "Official Records & Archives"),           # archive
    "Q39614":     ("813", "Official Records & Archives"),           # national archive
    "Q1457376":   ("813", "Official Records & Archives"),           # written document
    "Q245196":    ("813", "Official Records & Archives"),           # official gazette
    "Q590788":    ("813", "Official Records & Archives"),           # administrative record
    "Q15916867":  ("813", "Official Records & Archives"),           # public record

    # ── 814 Diaries & Memoirs ──
    "Q185598":    ("814", "Diaries & Memoirs"),                     # diary
    "Q234460":    ("814", "Diaries & Memoirs"),                     # autobiography
    "Q1269192":   ("814", "Diaries & Memoirs"),                     # memoir
    "Q30461":     ("814", "Diaries & Memoirs"),                     # personal narrative
    "Q193495":    ("814", "Diaries & Memoirs"),                     # monograph (biographical)

    # ── 815 Eyewitness Accounts ──
    "Q35831":     ("815", "Eyewitness Accounts"),                   # chronicle
    "Q846224":    ("815", "Eyewitness Accounts"),                   # history (historical work)
    "Q3621491":   ("815", "Eyewitness Accounts"),                   # travel writing
    "Q1457669":   ("815", "Eyewitness Accounts"),                   # correspondence collection
    "Q4573":      ("815", "Eyewitness Accounts"),                   # war diary
    "Q187685":    ("815", "Eyewitness Accounts"),                   # doctoral thesis

    # ── 820 Secondary Sources (general) ──
    "Q213051":    ("820", "Secondary Sources"),                     # non-fiction book
    "Q5633421":   ("820", "Secondary Sources"),                     # scientific book

    # ── 821 Academic Monographs ──
    "Q10870555":  ("821", "Academic Monographs"),                   # academic monograph
    "Q36279":     ("821", "Academic Monographs"),                   # biography
    "Q15839592":  ("821", "Academic Monographs"),                   # historical source edition
    "Q860626":    ("821", "Academic Monographs"),                   # tome / volume
    "Q571":       ("821", "Academic Monographs"),                   # book (catch-all, high filter)

    # ── 822 Peer-Reviewed Journal Articles ──
    "Q13442814":  ("822", "Peer-Reviewed Journal Articles"),        # scholarly article
    "Q5633421a":  ("822", "Peer-Reviewed Journal Articles"),        # scientific paper (alias)
    "Q191067":    ("822", "Peer-Reviewed Journal Articles"),        # journal article
    "Q7318358":   ("822", "Peer-Reviewed Journal Articles"),        # review article
    "Q749711a":   ("822", "Peer-Reviewed Journal Articles"),        # academic journal (alias)
    "Q5292654":   ("822", "Peer-Reviewed Journal Articles"),        # scientific journal
    "Q737498":    ("822", "Peer-Reviewed Journal Articles"),        # academic journal

    # ── 823 Encyclopedias & Reference Works ──
    "Q5292":      ("823", "Encyclopedias & Reference Works"),       # encyclopedia
    "Q13136":     ("823", "Encyclopedias & Reference Works"),       # reference work
    "Q23622":     ("823", "Encyclopedias & Reference Works"),       # dictionary
    "Q50823":     ("823", "Encyclopedias & Reference Works"),       # glossary
    "Q1580166":   ("823", "Encyclopedias & Reference Works"),       # bibliographical dictionary
    "Q1181865":   ("823", "Encyclopedias & Reference Works"),       # biographical dictionary
    "Q2352616":   ("823", "Encyclopedias & Reference Works"),       # thesaurus
    "Q622521":    ("823", "Encyclopedias & Reference Works"),       # handbook

    # ── 830 Archaeological Evidence (general) ──
    "Q839954":    ("830", "Archaeological Evidence"),               # archaeological site
    "Q15583442":  ("830", "Archaeological Evidence"),               # archaeological artifact

    # ── 831 Excavation Reports ──
    "Q848441":    ("831", "Excavation Reports"),                    # archaeological excavation
    "Q208452":    ("831", "Excavation Reports"),                    # excavation

    # ── 832 Artifact Analysis ──
    "Q220659":    ("832", "Artifact Analysis"),                     # bust (artifact)
    "Q56768911":  ("832", "Artifact Analysis"),                     # archaeological find
    "Q96585650":  ("832", "Artifact Analysis"),                     # ancient artifact
    "Q210272":    ("832", "Artifact Analysis"),                     # cultural property

    # ── 833 Radiocarbon & Dating Evidence ──
    # (No direct P31 instances — will be populated via keyword refinement)

    # ── 840 Quantitative Data ──
    "Q2145480":   ("840", "Quantitative Data"),                     # statistical survey

    # ── 841 Census & Demographic Data ──
    "Q39825":     ("841", "Census & Demographic Data"),             # census

    # ── 842 Economic & Trade Statistics ──
    "Q1172284":   ("842", "Economic & Trade Statistics"),           # economic data / dataset
    "Q2635894":   ("842", "Economic & Trade Statistics"),           # financial report

    # ── 843 Geospatial & Mapping Data ──
    "Q4006":      ("843", "Geospatial & Mapping Data"),             # map
    "Q210450":    ("843", "Geospatial & Mapping Data"),             # geographic map
    "Q18789":     ("843", "Geospatial & Mapping Data"),             # digital map
    "Q107022389": ("843", "Geospatial & Mapping Data"),             # cartographic work
    "Q728937":    ("843", "Geospatial & Mapping Data"),             # globe

    # ── 850 Oral Traditions (general) ──
    "Q184587":    ("850", "Oral Traditions"),                       # oral literature

    # ── 851 Oral Histories & Interviews ──
    "Q178651":    ("851", "Oral Histories & Interviews"),           # oral history
    "Q592946":    ("851", "Oral Histories & Interviews"),           # interview

    # ── 852 Folklore & Mythological Traditions ──
    "Q132311":    ("852", "Folklore & Mythological Traditions"),    # folk tale
    "Q44342":     ("852", "Folklore & Mythological Traditions"),    # myth
    "Q44559":     ("852", "Folklore & Mythological Traditions"),    # legend
    "Q699":       ("852", "Folklore & Mythological Traditions"),    # fairy tale
    "Q19353744":  ("852", "Folklore & Mythological Traditions"),    # fable
    "Q36279":     ("852", "Folklore & Mythological Traditions"),    # folklore
    "Q860861a":   ("852", "Folklore & Mythological Traditions"),    # folksong (alias)
    "Q8261":      ("852", "Folklore & Mythological Traditions"),    # proverb
    "Q1395219":   ("852", "Folklore & Mythological Traditions"),    # anecdote / parable

    # ── 853 Genealogies & Lineage Records ──
    "Q845788":    ("853", "Genealogies & Lineage Records"),        # genealogy
    "Q22811662":  ("853", "Genealogies & Lineage Records"),        # pedigree chart
}

# Build reverse lookup: first-occurrence wins
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in EVIDENCE_TYPE_MAP.items():
    clean_qid = _qid.rstrip("a")  # handle suffixed dupes
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info


# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (72 granular batches)
# Each batch -> (QIDs, min_sitelinks)
# Heavy types split solo w/ higher threshold to avoid timeouts
# Order: specific types FIRST, broad catch-alls LAST
# ═══════════════════════════════════════════════════════════════════

EVIDENCE_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── 811 Inscriptions & Epigraphy ──
    "811_inscription":    (["Q47721"], 5),
    "811_cuneiform":      (["Q4523831", "Q2078983"], 5),
    "811_ostracon":       (["Q105320460"], 5),
    "811_stele":          (["Q928357"], 5),
    "811_seal":           (["Q193977"], 5),
    "811_coin":           (["Q4884"], 20),                # HUGE type — high threshold
    "811_medallion":      (["Q217164"], 5),
    "811_stone_inscr":    (["Q28935506", "Q378436"], 5),

    # ── 812 Letters & Correspondence ──
    "812_letter":         (["Q133492"], 5),
    "812_encyclical":     (["Q749711"], 5),
    "812_papal_bull":     (["Q1269656"], 5),
    "812_epistle":        (["Q12045845"], 5),
    "812_petition":       (["Q37219"], 5),
    "812_diplomatic":     (["Q1144661", "Q17376908"], 5),

    # ── 813 Official Records & Archives ──
    "813_decree":         (["Q820655"], 5),
    "813_edict":          (["Q835327"], 5),
    "813_deed":           (["Q47577"], 5),
    "813_patent":         (["Q3514032"], 5),
    "813_archive":        (["Q166118", "Q39614"], 5),
    "813_gazette":        (["Q245196"], 5),
    "813_public_rec":     (["Q590788", "Q15916867"], 5),

    # ── 814 Diaries & Memoirs ──
    "814_diary":          (["Q185598"], 5),
    "814_autobiography":  (["Q234460"], 5),
    "814_memoir":         (["Q1269192"], 5),

    # ── 815 Eyewitness Accounts ──
    "815_chronicle":      (["Q35831"], 5),
    "815_history_work":   (["Q846224"], 5),
    "815_travel_acc":     (["Q3621491"], 5),
    "815_war_diary":      (["Q4573"], 5),
    "815_thesis":         (["Q187685"], 15),              # HUGE type — high threshold

    # ── 820-821 Secondary Sources / Academic Monographs ──
    "821_monograph":      (["Q10870555"], 5),
    "821_biography":      (["Q36279"], 10),
    "821_source_ed":      (["Q15839592"], 5),

    # ── 822 Peer-Reviewed Journal Articles ──
    "822_journal":        (["Q737498"], 10),
    "822_sci_journal":    (["Q5292654"], 10),

    # ── 823 Encyclopedias & Reference Works ──
    "823_encyclopedia":   (["Q5292"], 5),
    "823_dictionary":     (["Q23622"], 5),
    "823_reference":      (["Q13136"], 5),
    "823_bio_dict":       (["Q1580166", "Q1181865"], 5),
    "823_handbook":       (["Q622521"], 5),
    "823_thesaurus":      (["Q2352616", "Q50823"], 5),

    # ── 830-832 Archaeological Evidence ──
    "830_arch_site":      (["Q839954"], 5),
    "830_arch_artifact":  (["Q15583442"], 5),
    "831_excavation":     (["Q848441", "Q208452"], 5),
    "832_ancient_art":    (["Q56768911", "Q96585650"], 5),
    "832_cultural_prop":  (["Q210272"], 8),

    # ── 841 Census & Demographic Data ──
    "841_census":         (["Q39825"], 5),

    # ── 842 Economic & Trade Statistics ──
    "842_survey":         (["Q2145480"], 5),
    "842_fin_report":     (["Q2635894", "Q1172284"], 5),

    # ── 843 Geospatial & Mapping Data ──
    "843_map":            (["Q4006"], 10),
    "843_globe":          (["Q728937"], 5),

    # ── 850-851 Oral Traditions & Histories ──
    "850_oral_lit":       (["Q184587"], 5),
    "851_oral_hist":      (["Q178651"], 5),
    "851_interview":      (["Q592946"], 10),

    # ── 852 Folklore & Mythological Traditions ──
    "852_folk_tale":      (["Q132311"], 5),
    "852_myth":           (["Q44342"], 5),
    "852_legend":         (["Q44559"], 5),
    "852_fairy_tale":     (["Q699"], 5),
    "852_fable":          (["Q19353744"], 5),
    "852_proverb":        (["Q8261"], 10),

    # ── 853 Genealogies & Lineage Records ──
    "853_genealogy":      (["Q845788", "Q22811662"], 5),

    # ── 810 Primary Sources (broad catch-all — LAST) ──
    "810_manuscript":     (["Q87167"], 8),
    "810_document":       (["Q49848"], 20),               # ENORMOUS — only notable docs

    # ── 820 Secondary Sources (broad — LAST) ──
    "820_nonfiction":     (["Q213051"], 30),              # HUGE — only most notable
    "820_sci_book":       (["Q5633421"], 15),

    # ── 821 Book (broadest catch-all — VERY LAST) ──
    "821_book":           (["Q571"], 50),                 # ENORMOUS — only landmark books
}


# ═══════════════════════════════════════════════════════════════════
# Non-evidence keyword filter
# ═══════════════════════════════════════════════════════════════════

NON_EVIDENCE_KEYWORDS = {
    'wikimedia', 'disambiguation', 'template', 'category',
    'fictional character', 'video game', 'software', 'mobile app',
    'taxon', 'species', 'genus', 'protein', 'gene',
    'television series', 'tv series', 'podcast', 'album',
    'association football', 'football club', 'sports club',
    'political party', 'administrative unit', 'municipality',
    'railway station', 'metro station', 'bus route',
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


def compute_significance(sitelinks: int, creation_year: int | None) -> int:
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
    if creation_year is not None:
        if creation_year < -1000:
            score += 2
        elif creation_year < 500:
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
    return ("810", "Primary Sources")


# ═══════════════════════════════════════════════════════════════════
# Sub-division refinement
# ═══════════════════════════════════════════════════════════════════

def refine_division(
    div_code: str,
    div_heading: str,
    era: str,
    type_label: str,
    name: str,
    description: str,
) -> tuple[str, str]:
    text = f"{name} {description} {type_label}".lower()

    # 810 → 811-815
    if div_code == "810":
        if any(w in text for w in ("inscription", "epigraph", "cuneiform", "tablet", "stele", "seal", "coin")):
            return ("811", "Inscriptions & Epigraphy")
        if any(w in text for w in ("letter", "correspondence", "epistle", "encyclical", "bull")):
            return ("812", "Letters & Correspondence")
        if any(w in text for w in ("record", "archive", "decree", "edict", "gazette", "charter", "deed")):
            return ("813", "Official Records & Archives")
        if any(w in text for w in ("diary", "memoir", "autobiography", "personal")):
            return ("814", "Diaries & Memoirs")
        if any(w in text for w in ("eyewitness", "chronicle", "account", "testimony", "travel")):
            return ("815", "Eyewitness Accounts")
        return div_code, div_heading

    # 820 → 821-823
    if div_code == "820":
        if any(w in text for w in ("encyclopedia", "dictionary", "reference", "glossary", "handbook")):
            return ("823", "Encyclopedias & Reference Works")
        if any(w in text for w in ("journal", "article", "peer-review", "paper")):
            return ("822", "Peer-Reviewed Journal Articles")
        return ("821", "Academic Monographs")

    # 830 → 831-833
    if div_code == "830":
        if any(w in text for w in ("excavation", "dig ", "digging")):
            return ("831", "Excavation Reports")
        if any(w in text for w in ("radiocarbon", "dating", "carbon-14", "dendrochronolog", "thermoluminescen")):
            return ("833", "Radiocarbon & Dating Evidence")
        if any(w in text for w in ("artifact", "artefact", "analysis", "pottery", "ceramic", "tool")):
            return ("832", "Artifact Analysis")
        return div_code, div_heading

    # 840 → 841-843
    if div_code == "840":
        if any(w in text for w in ("census", "demographic", "population")):
            return ("841", "Census & Demographic Data")
        if any(w in text for w in ("economic", "trade", "financial", "gdp", "market")):
            return ("842", "Economic & Trade Statistics")
        if any(w in text for w in ("map", "geospatial", "geographic", "cartograph", "atlas")):
            return ("843", "Geospatial & Mapping Data")
        return div_code, div_heading

    # 850 → 851-853
    if div_code == "850":
        if any(w in text for w in ("interview", "oral history", "testimony")):
            return ("851", "Oral Histories & Interviews")
        if any(w in text for w in ("folk", "myth", "legend", "fairy", "fable", "proverb")):
            return ("852", "Folklore & Mythological Traditions")
        if any(w in text for w in ("genealog", "lineage", "pedigree", "ancestry")):
            return ("853", "Genealogies & Lineage Records")
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
       ?authorLabel
       ?publisherLabel
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
  OPTIONAL {{ ?item wdt:P50  ?author . }}
  OPTIONAL {{ ?item wdt:P123 ?publisher . }}
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


# ═══════════════════════════════════════════════════════════════════
# Transform: SPARQL row -> Annals entity
# ═══════════════════════════════════════════════════════════════════

def transform_evidence(row: dict) -> dict[str, Any] | None:
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
    author_name = binding_val(row, "authorLabel") or ""
    publisher_name = binding_val(row, "publisherLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    # Filter non-evidence entities
    desc_lower = description.lower()
    if any(kw in desc_lower for kw in NON_EVIDENCE_KEYWORDS):
        return None
    # Filter raw QIDs in author/publisher
    if author_name and re.match(r'^Q\d+$', author_name):
        author_name = ""
    if publisher_name and re.match(r'^Q\d+$', publisher_name):
        publisher_name = ""

    creation_year = parse_year(inception_raw)
    created_display = format_date_display(inception_raw)
    era, era_slug = year_to_era(creation_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine parent divisions to sub-divisions
    div_code, div_heading = refine_division(div_code, div_heading, era, type_label, name, description)

    slug = make_slug(name)

    # Build summary
    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if author_name:
        summary += f" By {author_name}."
    if publisher_name:
        summary += f" Published by {publisher_name}."
    if country_name != "Global":
        summary += f" From {country_name}."
    if creation_year:
        if creation_year < 0:
            summary += f" Dating to c. {abs(creation_year)} BCE."
        else:
            summary += f" Created c. {creation_year}."

    sig_score = compute_significance(sitelinks, creation_year)

    # Choose evidence tier based on division
    div_int = int(div_code)
    if 810 <= div_int <= 815:
        evidence_tier = "A"
        tier_label = "Primary Source"
    elif 820 <= div_int <= 823:
        evidence_tier = "B"
        tier_label = "Secondary Source"
    elif 830 <= div_int <= 833:
        evidence_tier = "C"
        tier_label = "Archaeological"
    elif 840 <= div_int <= 843:
        evidence_tier = "D"
        tier_label = "Quantitative"
    elif 850 <= div_int <= 853:
        evidence_tier = "E"
        tier_label = "Oral Tradition"
    else:
        evidence_tier = "F"
        tier_label = "Other"

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Evidence",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Evidence -- {div_heading} -- {country_name} -- {era}"],
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
            "context": f"{name} from {country_name}",
        }],
        "places": [],
        "texts": [],
        "evidenceType": type_label,
        "evidenceTier": evidence_tier,
        "evidenceTierLabel": tier_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if created_display:
        entity["created"] = created_display
    if creation_year:
        entity["createdYear"] = creation_year
    if author_name:
        entity["author"] = author_name
    if publisher_name:
        entity["publisher"] = publisher_name
    if country_name and country_name != "Global":
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
    parser = argparse.ArgumentParser(description="Fetch evidence from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_evidence.json"

    total_qids = len(set(qid for qids, _ in EVIDENCE_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Evidence Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(EVIDENCE_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   810-853 (all Class 8 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print(f"  Progressive save:    Every 5 batches")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}
    batch_idx = 0

    for batch_name, (type_qids, min_sl) in EVIDENCE_QUERIES.items():
        batch_idx += 1
        print(f"[{batch_idx}/{len(EVIDENCE_QUERIES)}] {batch_name}  "
              f"{len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_evidence(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} unique (total: {len(all_entities)})")

        # Progressive save every 5 batches
        if batch_idx % 5 == 0:
            save_progress(all_entities, output_path, total_raw)

        time.sleep(2)

    if args.dry_run:
        print("\nDry run complete.")
        print(f"  Would query {len(EVIDENCE_QUERIES)} batches with {total_qids} unique QIDs")
        return

    # Sort by era, then name
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # Compute statistics
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    sig_dist: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    tier_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        sig_dist[e["historicalSignificance"]["label"]] = sig_dist.get(e["historicalSignificance"]["label"], 0) + 1
        ct = e.get("continent", "Global")
        continent_counts[ct] = continent_counts.get(ct, 0) + 1
        tier = e.get("evidenceTier", "F")
        tier_counts[tier] = tier_counts.get(tier, 0) + 1

    # Write final output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "1.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Evidence",
            "classCode": 8,
            "classHeading": "Evidence",
            "type_qids_queried": total_qids,
            "batches_queried": len(EVIDENCE_QUERIES),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "evidence_tier_counts": dict(sorted(tier_counts.items())),
            "evidence_tiers": {
                "A": "Primary Source — inscriptions, letters, records, diaries, eyewitness accounts",
                "B": "Secondary Source — academic monographs, journal articles, encyclopedias",
                "C": "Archaeological — sites, excavations, artifact analysis, dating evidence",
                "D": "Quantitative — census data, economic statistics, geospatial data",
                "E": "Oral Tradition — oral histories, folklore, myths, genealogies",
                "F": "Other — unclassified evidence",
            },
            "significance_scale": {
                "1-2": "Minor -- documented but limited scholarly impact",
                "3-4": "Moderate -- nationally significant source",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized evidence",
                "9-10": "Landmark -- world-defining documentary source",
            },
            "inAppwrite_note": "All entities have inAppwrite=false. Use historicalSignificance.score to prioritize for Appwrite seeding.",
            "note": "Comprehensive Wikidata evidence fetch v1.0 covering all Class 8 divisions (810-853).",
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
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    print("  By evidence tier:")
    tier_names = {"A": "Primary", "B": "Secondary", "C": "Archaeological",
                  "D": "Quantitative", "E": "Oral", "F": "Other"}
    for tier, count in sorted(tier_counts.items()):
        print(f"    Tier {tier} ({tier_names.get(tier, '?')}): {count}")
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
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] {e['name']} ({e['evidenceTierLabel']})")


if __name__ == "__main__":
    main()
