#!/usr/bin/env python3
"""
VS Code Enrichment Batch 63 — 4 Final Entities
Pope John Paul II, Queen Elizabeth II,
Artaxiad Dynasty of Armenia, Wright Brothers

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-63-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-63-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Pope John Paul II ─────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/250-Class-250/250pope-john-paul-ii.json",
        "slug": "pope-john-paul-ii",
        "era_correction": None,
        "data": {
            "summary": (
                "Pope John Paul II (1920–2005), born Karol Józef Wojtyła in Wadowice, Poland, was the 264th Pope of the Catholic Church (1978–2005) — the first non-Italian pope in 455 years and the first Polish pope ever. His 26-year pontificate was the third longest in history, during which he traveled to 129 countries (more than any previous pope), met with more world leaders than any figure in history, and played a central role in the collapse of communism in Eastern Europe.\n\n"
                "Growing up under Nazi occupation and Soviet communism, Wojtyła was ordained a priest in 1946, became Archbishop of Kraków (1964), and was elected pope in 1978 at 58. His first words from the balcony — 'Be not afraid!' — established his signature message. His 1979 visit to Poland drew 13 million people in nine days, electrifying Solidarity's resistance and, as Mikhail Gorbachev later acknowledged, helping bring down the Iron Curtain.\n\n"
                "He survived an assassination attempt in St Peter's Square (May 13, 1981 — the feast of Our Lady of Fatima), shot twice by Mehmet Ali Ağca. He later visited Ağca in prison and publicly forgave him. His pontificate defined conservative Catholic moral positions: opposing abortion, contraception, women's ordination, and married clergy — while simultaneously being the most progressive pope on social justice, interfaith dialogue (visiting synagogues and mosques), and human rights advocacy.\n\n"
                "He was canonized a saint by Pope Francis in April 2014, just nine years after his death — one of the fastest canonizations in modern Catholic history."
            ),
            "causes": [
                "Polish Catholic identity forged under Nazi and Soviet occupation requiring fearless leadership",
                "Vatican II (1962–65) opening space for episcopal initiative Wojtyła exercised fully",
                "Cold War competition between Christianity and Soviet atheism making a Polish pope politically explosive",
                "John Paul I's sudden death (33-day papacy) requiring emergency conclave in 1978",
            ],
            "effects": [
                "Solidarity movement in Poland (1980) energized by his 1979 visit — 13 million witnesses",
                "Fall of communism in Eastern Europe (1989) — he and Reagan/Thatcher acknowledged as key figures",
                "World Youth Day established — global Catholic youth gatherings in 100+ cities",
                "Catholic-Jewish reconciliation: visited Rome's Great Synagogue (1986), called Jews 'elder brothers'",
                "Apologies for Church's historical sins — Inquisition, Crusades, treatment of Galileo",
                "Beatification of 1,338 people, canonization of 482 saints — more than all previous popes combined",
                "Canonized a saint (2014) — among fastest canonizations in history",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Solidarity movement", "targetSlug": "solidarity-movement-poland", "note": "His 1979 Poland visit galvanized Solidarity's anti-communist resistance"},
                {"type": "INFLUENCES", "target": "Mikhail Gorbachev", "targetSlug": "mikhail-gorbachev", "note": "Gorbachev credited John Paul II with helping end communism"},
                {"type": "INFLUENCES", "target": "Ronald Reagan", "targetSlug": "ronald-reagan", "note": "Reagan-JPII alliance against Soviet communism"},
                {"type": "INFLUENCES", "target": "Fall of communism (1989)", "targetSlug": "fall-of-communism-1989", "note": "His moral authority key in Eastern European liberation"},
                {"type": "INFLUENCES", "target": "Mehmet Ali Ağca", "targetSlug": "mehmet-ali-agca", "note": "Shot JPII in 1981; JPII publicly forgave him in prison"},
                {"type": "INFLUENCES", "target": "Mother Teresa", "targetSlug": "mother-teresa", "note": "Beatified her (2003); close allies in charitable mission"},
                {"type": "INFLUENCES", "target": "Vatican II", "targetSlug": "second-vatican-council", "note": "He participated in Vatican II as bishop; implemented its spirit"},
                {"type": "INFLUENCES", "target": "Catholic-Jewish reconciliation", "targetSlug": "catholic-jewish-relations", "note": "First pope to visit a synagogue; called Jews 'elder brothers in faith'"},
                {"type": "INFLUENCES", "target": "Lech Wałęsa", "targetSlug": "lech-walesa", "note": "Solidarity leader whose movement JPII's visit electrified"},
                {"type": "OCCURS_IN", "target": "Vatican City", "targetSlug": "vatican-city", "note": "Pope — head of Catholic Church and Vatican state"},
                {"type": "OCCURS_IN", "target": "Poland", "targetSlug": "poland", "note": "Born and raised; his 1979 return transformed Polish history"},
                {"type": "INFLUENCES", "target": "World Youth Day", "targetSlug": "world-youth-day", "note": "He established WYD in 1984; now draws millions globally"},
                {"type": "INFLUENCES", "target": "Pope Francis", "targetSlug": "pope-francis", "note": "Francis canonized John Paul II in 2014"},
                {"type": "INFLUENCES", "target": "Roman Catholicism", "targetSlug": "roman-catholicism", "note": "1.2 billion Catholics — he was their pope for 26 years"},
                {"type": "INFLUENCES", "target": "Dalai Lama", "targetSlug": "dalai-lama", "note": "Historic interfaith meetings with Buddhist, Muslim, Jewish leaders"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Pope John Paul II played a central role in the fall of communism in Eastern Europe through moral authority and his electrifying 1979 Poland visit, was the most widely traveled head of state in history, and defined Catholic Christianity for a generation of 1.2 billion believers — canonized a saint just nine years after his death."
            },
            "quote": "'Be not afraid.' — Pope John Paul II, first papal address from St Peter's Balcony (October 22, 1978)",
            "places": ["Vatican City (pontificate)", "Wadowice, Poland (birthplace)", "Rome, Italy (Gemelli Hospital — shooting)", "Kraków, Poland (archbishop)"],
            "subjectHeadings": "Pope John Paul II — Religious Leaders and Popes — Poland/Vatican — Contemporary",
            "subjects": ["Vatican", "Poland", "Catholic Church", "Christianity", "Cold War", "communism", "interfaith", "20th century", "pope", "canonization"],
            "frameworks": ["religious-thought", "cold-war", "human-rights"],
        }
    },

    # ── 2. Queen Elizabeth II ────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221queen-elizabeth-ii.json",
        "slug": "queen-elizabeth-ii",
        "era_correction": None,
        "data": {
            "summary": (
                "Queen Elizabeth II (1926–2022) was the longest-reigning British monarch in history — serving for 70 years and 214 days from her accession on February 6, 1952, until her death at Balmoral on September 8, 2022, at age 96. As head of state of the United Kingdom and 14 other Commonwealth realms, she witnessed and personified the transformation of the British Empire into the Commonwealth of Nations — one of history's most significant transitions from imperial to postcolonial order.\n\n"
                "Born Princess Elizabeth Alexandra Mary, she came to the throne unexpectedly after her uncle's abdication (Edward VIII, 1936) made her father King George VI. She trained as an ATS mechanic and military driver in World War II, her BBC broadcasts during the war establishing her as a unifying national figure. Her coronation (June 2, 1953) was the first British coronation broadcast on television, watched by 27 million in the UK alone.\n\n"
                "She served with 15 different Prime Ministers from Winston Churchill (born 1874) to Liz Truss (born 1975), navigating decolonization, the 'wind of change,' the Troubles, Princess Diana's death and the subsequent constitutional crisis, the Scottish independence referendum (2014), Brexit, and COVID-19 — modeling calm continuity through extraordinary change. Her weekly audience with each Prime Minister was constitutionally central; she was acknowledged as uniquely well-briefed on global affairs.\n\n"
                "'In the words of Shakespeare's Henry V: We few, we happy few,' she quoted in her Diamond Jubilee address — and the millions mourning her death in September 2022 demonstrated the depth of attachment her 70-year reign had generated."
            ),
            "causes": [
                "Edward VIII's abdication (1936) making her father King and her heir presumptive",
                "George VI's death (February 6, 1952) making her queen at age 25",
                "Constitutional monarchy tradition in which personal popularity rests on political neutrality",
                "WWII service and wartime broadcasts establishing her as a national symbol",
            ],
            "effects": [
                "70-year reign (1952–2022) — longest in British history",
                "Transformation of British Empire into Commonwealth — 54 member nations",
                "15 Prime Ministers served under her — Churchill to Truss",
                "Coronation (1953) first broadcast on TV — mass media era of monarchy",
                "Global mourning at death (2022) — extraordinary outpouring demonstrating her impact",
                "Model of constitutional monarchy maintaining national unity through radical change",
                "Commonwealth as postcolonial international institution she sustained for 70 years",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Winston Churchill", "targetSlug": "winston-churchill", "note": "First PM she served with; he served her for 3 years"},
                {"type": "INFLUENCES", "target": "Philip, Duke of Edinburgh", "targetSlug": "prince-philip", "note": "Husband of 73 years; died April 2021"},
                {"type": "INFLUENCES", "target": "Margaret Thatcher", "targetSlug": "margaret-thatcher", "note": "Often reportedly tense relationship; 11 years together"},
                {"type": "INFLUENCES", "target": "Charles III", "targetSlug": "charles-iii", "note": "Son and successor — became king at her death"},
                {"type": "INFLUENCES", "target": "Princess Diana", "targetSlug": "princess-diana", "note": "Death in 1997 and public criticism of royal response"},
                {"type": "INFLUENCES", "target": "Commonwealth of Nations", "targetSlug": "commonwealth-of-nations", "note": "Head of Commonwealth — 54 member nations"},
                {"type": "INFLUENCES", "target": "George VI", "targetSlug": "george-vi", "note": "Father whose death made her queen at 25"},
                {"type": "INFLUENCES", "target": "Edward VIII", "targetSlug": "edward-viii", "note": "Uncle whose abdication (1936) made her heir"},
                {"type": "INFLUENCES", "target": "Brexit", "targetSlug": "brexit", "note": "Navigated constitutional crisis of UK's EU departure"},
                {"type": "OCCURS_IN", "target": "United Kingdom", "targetSlug": "united-kingdom", "note": "Head of state for 70 years"},
                {"type": "INFLUENCES", "target": "Tony Blair", "targetSlug": "tony-blair", "note": "PM during Diana's death — acute public test of monarchy"},
                {"type": "INFLUENCES", "target": "Nelson Mandela", "targetSlug": "nelson-mandela", "note": "Warm Commonwealth relationship after South Africa's return"},
                {"type": "INFLUENCES", "target": "Decolonization", "targetSlug": "decolonization", "note": "Presided over dissolution of British Empire into Commonwealth"},
                {"type": "INFLUENCES", "target": "COVID-19 pandemic", "targetSlug": "covid-19-pandemic", "note": "'We will meet again' speech — wartime echo resonated globally"},
                {"type": "INFLUENCES", "target": "Scottish independence referendum", "targetSlug": "scottish-independence-referendum-2014", "note": "Her role carefully neutral during UK's constitutional test"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Queen Elizabeth II reigned for 70 years through the transformation of the British Empire into the Commonwealth, served 15 Prime Ministers, and modeled constitutional monarchy as a unifying national institution through decolonization, Diana's death, Brexit, and COVID — her death in 2022 prompted global mourning on an extraordinary scale."
            },
            "quote": "'I cannot lead you into battle. I do not give you laws or administer justice but I can do something else — I can give my heart and my devotion to these old islands and to all the peoples of our brotherhood of nations.' — Queen Elizabeth II, 1957",
            "places": ["Windsor Castle, England (home)", "Buckingham Palace, London (official residence)", "Balmoral Castle, Scotland (death)", "Westminster Abbey, London (coronation)"],
            "subjectHeadings": "Queen Elizabeth II — Monarchs and Heads of State — United Kingdom — Contemporary",
            "subjects": ["United Kingdom", "monarchy", "Commonwealth", "British history", "decolonization", "20th century", "constitutional government", "Europe", "colonialism", "21st century"],
            "frameworks": ["state-formation", "empire-building", "political-philosophy"],
        }
    },

    # ── 3. Artaxiad Dynasty of Armenia ───────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/523-Class-523/523artaxiad-dynasty-of-armenia.json",
        "slug": "artaxiad-dynasty-of-armenia",
        "era_correction": None,
        "data": {
            "summary": (
                "The Artaxiad Dynasty (189 BCE – 12 CE) was the first native Armenian royal dynasty to rule a unified Armenian kingdom, founded by Artaxias I after breaking from Seleucid control following the defeat of Antiochus III at the Battle of Magnesia (190 BCE). Under the Artaxiads, Greater Armenia emerged as an independent state for the first time, ultimately reaching its greatest territorial extent under Tigranes the Great (95–55 BCE) — who for a brief period created an empire stretching from the Mediterranean to the Caspian Sea.\n\n"
                "Tigranes II 'the Great' is the dynasty's defining figure: he conquered Cappadocia, Cilicia, Pontus, Syria, and parts of Mesopotamia — creating an empire of approximately 3 million km², making it temporarily one of the largest states in Western Asia. He founded Tigranocerta as his capital, settled Hellenistic artisans there, and made his court a center of Greek and Armenian culture. His ambitions brought him into conflict with Rome: Pompey defeated him in 66 BCE, and Tigranes surrendered, becoming a Roman client king.\n\n"
                "The Artaxiad period was formative for Armenian national identity: the Armenian language was developed as a literary medium, the kingdom's borders roughly corresponded to historical Armenia, and the conflict between Roman and Parthian power established Armenia's enduring geopolitical role as the buffer state between competing empires.\n\n"
                "The dynasty ended in 12 CE when the last Artaxiad king, Tiganes V, was removed by Rome, making Armenia a province. Its memory survived as the precedent for Armenian sovereignty through the Arsacid dynasty that followed."
            ),
            "causes": [
                "Rome's defeat of Seleucid Antiochus III at Magnesia (190 BCE) breaking Seleucid power",
                "Artaxias I's military service under Antiochus III enabling his bid for independence",
                "Armenian upland geography providing strategic defensibility against great powers",
                "Parthian and Roman expansion creating power vacuum Tigranes the Great exploited",
            ],
            "effects": [
                "Greater Armenia as independent kingdom (189 BCE – 12 CE) — first native Armenian state",
                "Tigranes II's empire (95–55 BCE) reaching 3 million km² at its height",
                "Tigranocerta as major Hellenistic-Armenian capital",
                "Armenia as strategic buffer between Rome and Parthia — geopolitical role lasting 2,000 years",
                "Artaxiad dynasty establishing Armenian royal tradition continued by Arsacids",
                "Armenian cultural identity and language developed during period",
                "Roman-Parthian treaty framework making Armenia a formally contested borderland",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Tigranes the Great", "targetSlug": "tigranes-the-great", "note": "Greatest Artaxiad king; empire reached 3 million km²"},
                {"type": "INFLUENCES", "target": "Artaxias I", "targetSlug": "artaxias-i", "note": "Founder of the dynasty (189 BCE)"},
                {"type": "INFLUENCES", "target": "Pompey", "targetSlug": "pompey", "note": "Defeated Tigranes in 66 BCE; established Roman client relationship"},
                {"type": "INFLUENCES", "target": "Seleucid Empire", "targetSlug": "seleucid-empire", "note": "Former overlords; Artaxias I broke away after Magnesia"},
                {"type": "INFLUENCES", "target": "Roman Republic", "targetSlug": "roman-republic", "note": "Rome's eastern expansion eventually subordinated Armenia"},
                {"type": "INFLUENCES", "target": "Parthian Empire", "targetSlug": "parthian-empire", "note": "Eastern rival whose pressure shaped Armenia's geopolitics"},
                {"type": "INFLUENCES", "target": "Tigranocerta", "targetSlug": "tigranocerta", "note": "Capital founded by Tigranes — major Hellenistic-Armenian city"},
                {"type": "INFLUENCES", "target": "Arsacid dynasty of Armenia", "targetSlug": "arsacid-dynasty-of-armenia", "note": "Succeeding dynasty that continued Armenian independence"},
                {"type": "INFLUENCES", "target": "Lucullus", "targetSlug": "lucullus", "note": "Roman general who sacked Tigranocerta (69 BCE)"},
                {"type": "OCCURS_IN", "target": "Armenia", "targetSlug": "armenia", "note": "Ruled Greater Armenia"},
                {"type": "INFLUENCES", "target": "Hellenistic culture", "targetSlug": "hellenistic-culture", "note": "Greek culture flourished at Tigranocerta court"},
                {"type": "INFLUENCES", "target": "Mithridates VI of Pontus", "targetSlug": "mithridates-vi", "note": "Son-in-law and military ally in wars against Rome"},
                {"type": "INFLUENCES", "target": "Antiochus III", "targetSlug": "antiochus-iii", "note": "Seleucid king whose defeat at Magnesia triggered Armenian independence"},
                {"type": "INFLUENCES", "target": "Cappadocia", "targetSlug": "cappadocia", "note": "Conquered by Tigranes II during imperial expansion"},
                {"type": "INFLUENCES", "target": "Syria", "targetSlug": "syria", "note": "Tigranes controlled Syria during his peak expansionism"},
            ],
            "historicalSignificance": {
                "significanceScore": 7,
                "significanceCategory": "regional",
                "significanceNarrative": "The Artaxiad Dynasty created the first unified Armenian kingdom and under Tigranes the Great briefly built one of the ancient world's largest empires — establishing Armenia's enduring geopolitical identity as the pivot state between Rome and Parthia, a role that defined the region for two millennia."
            },
            "quote": "'King of Kings, and King of Armenia' — Tigranes the Great's royal title at the height of his empire (c. 83 BCE)",
            "places": ["Artaxata (modern Artashat), Armenia (capital)", "Tigranocerta (modern Turkey)", "Yerevan region, Armenia"],
            "subjectHeadings": "Artaxiad Dynasty — Royal Dynasties — Armenia — Classical",
            "subjects": ["Armenia", "ancient history", "Classical era", "Hellenistic period", "Rome", "Parthia", "monarchy", "Central Asia", "empire", "1st century BCE"],
            "frameworks": ["empire-building", "state-formation", "military-history"],
        }
    },

    # ── 4. Wright Brothers ───────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/630-Class-630/63036-wright-brothers.json",
        "slug": "wright-brothers",
        "era_correction": None,
        "data": {
            "summary": (
                "The Wright Brothers — Orville (1871–1948) and Wilbur (1867–1912) Wright — were American aviation pioneers from Dayton, Ohio, who on December 17, 1903, at Kitty Hawk, North Carolina, achieved the first sustained, controlled, powered heavier-than-air flight in history. The first flight lasted 12 seconds and covered 120 feet; the fourth flight that day lasted 59 seconds and covered 852 feet. In achieving this, two bicycle mechanics without university degrees solved a problem that had defeated the most eminent engineers in the world.\n\n"
                "The Wright Brothers' key innovation was not the engine (though they designed a remarkable 12-horsepower engine) but three-axis flight control — their 'wing warping' mechanism (later replaced by ailerons) allowed the pilot to control roll, pitch, and yaw simultaneously. Their methodical approach was distinctive: they first studied aerodynamics systematically (using a wind tunnel they built), then worked through hundreds of glider flights before adding an engine. Their 1902 glider was already the most capable aircraft ever built.\n\n"
                "By 1905, their Flyer III could fly over 24 miles in 38 minutes — a practical aircraft. Wilbur died of typhoid in 1912; Orville lived to see jet aircraft, nuclear bombs, and rockets. Their 1906 patent on flight control mechanisms was so broadly written it allowed them to dominate early US aviation for a decade.\n\n"
                "The invention of the airplane compressed the world, made mass transport possible, transformed warfare (within 11 years of Kitty Hawk there were aerial dogfights in WWI), and ultimately enabled the global civilization of the 20th century."
            ),
            "causes": [
                "Otto Lilienthal's glider research (died 1896) providing crucial aerodynamic baseline",
                "Langley's failed Aerodrome (1903) demonstrating that brute force without control fails",
                "Systematic scientific approach — wind tunnel testing solving lift calculations",
                "Kitty Hawk's sand dunes and steady winds providing ideal testing conditions",
            ],
            "effects": [
                "First powered heavier-than-air flight (December 17, 1903) — 12 seconds, 120 feet",
                "Flyer III (1905) — first practical airplane; 24-mile continuous flight",
                "Wright Company (1909) — commercializing aviation",
                "WWI aerial combat (1914–18) — airpower within 11 years of Kitty Hawk",
                "Commercial aviation industry — Boeing, Airbus — tracing directly to Wright patents",
                "Air travel compressing global distances and enabling modern globalization",
                "Military aviation — from biplanes to stealth bombers — all rooted in their control system",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Otto Lilienthal", "targetSlug": "otto-lilienthal", "note": "German glider pioneer whose fatal crash inspired Wright Brothers"},
                {"type": "INFLUENCES", "target": "Samuel Langley", "targetSlug": "samuel-langley", "note": "Competitor whose Aerodrome failed days before Kitty Hawk"},
                {"type": "INFLUENCES", "target": "Kitty Hawk", "targetSlug": "kitty-hawk", "note": "Site of first flight — chose for wind, sand, and privacy"},
                {"type": "INFLUENCES", "target": "Boeing", "targetSlug": "boeing", "note": "Aviation giant whose lineage traces to Wright Brothers"},
                {"type": "INFLUENCES", "target": "World War I aviation", "targetSlug": "world-war-i-aviation", "note": "Aerial combat emerged within 11 years of first flight"},
                {"type": "INFLUENCES", "target": "Glenn Curtiss", "targetSlug": "glenn-curtiss", "note": "Rival who fought Wright patent — ailerons vs. wing warping"},
                {"type": "INFLUENCES", "target": "Charles Lindbergh", "targetSlug": "charles-lindbergh", "note": "First transatlantic flight (1927) — 24 years after Kitty Hawk"},
                {"type": "INFLUENCES", "target": "Neil Armstrong", "targetSlug": "neil-armstrong", "note": "Armstrong carried a piece of Kitty Hawk fabric to the Moon"},
                {"type": "INFLUENCES", "target": "Commercial aviation", "targetSlug": "commercial-aviation", "note": "All modern air travel traces to Wright control system"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "American inventors from Dayton, Ohio"},
                {"type": "INFLUENCES", "target": "NASA", "targetSlug": "nasa", "note": "Aerospace tradition Wrights began culminated in NASA"},
                {"type": "INFLUENCES", "target": "Military aviation", "targetSlug": "military-aviation", "note": "All modern warplanes trace to Wright control innovations"},
                {"type": "INFLUENCES", "target": "Globalization", "targetSlug": "globalization", "note": "Air travel compressing global distance enabling modern globalization"},
                {"type": "INFLUENCES", "target": "Smithsonian Institution", "targetSlug": "smithsonian-institution", "note": "Original Flyer displayed in National Air and Space Museum"},
                {"type": "INFLUENCES", "target": "Internal combustion engine", "targetSlug": "internal-combustion-engine", "note": "Their 12 HP engine was the smallest viable powerplant available"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "The Wright Brothers achieved the first powered controlled flight in 1903, solving through systematic experimentation a problem that had defeated the world's best engineers — their invention of the airplane transformed warfare, commerce, and human movement, compressing the globe and making 20th-century civilization possible."
            },
            "quote": "'The desire to fly is an idea handed down to us by our ancestors who, in their grueling travels across trackless lands in prehistoric times, looked enviously on the birds soaring freely through space, at full speed, above all obstacles, on the infinite highway of the air.' — Wilbur Wright",
            "places": ["Kitty Hawk, North Carolina (first flights)", "Dayton, Ohio (home and workshop)", "Huffman Prairie, Ohio (Flyer III testing)"],
            "subjectHeadings": "Wright Brothers — Inventors and Aviation Pioneers — United States — Modern",
            "subjects": ["United States", "aviation", "invention", "flight", "technology", "20th century", "Industrial Revolution", "military history", "transport", "globalization"],
            "frameworks": ["technological-change", "scientific-revolution", "industrial-history"],
        }
    },
]


# ── Core writer ──────────────────────────────────────────────────────────────

def enrich_entity(file_path, slug, data, era_correction, dry_run=False):
    if not os.path.exists(file_path):
        return f"FILE NOT FOUND: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entities = doc.get("entities", [])
    target = next((e for e in entities if e.get("slug") == slug), None)
    if not target:
        return f"SLUG NOT FOUND: {slug} in {file_path}"

    dj = target.get("detailsJson")
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    current_summary = (dj or {}).get("summary", "")
    new_summary = data["summary"]

    if len(current_summary) >= SKIP_THRESHOLD:
        return f"SKIP {slug} (already {len(current_summary)}c)"

    if dry_run:
        return f"→ Enriching {slug}  (was {len(current_summary)}c → {len(new_summary)}c)"

    if "detailsJson" not in target or target["detailsJson"] is None or isinstance(target["detailsJson"], str):
        target["detailsJson"] = {}

    dj = target["detailsJson"]
    now = datetime.now(timezone.utc).isoformat()

    edit_log = dj.get("_editLog", [])
    for field in ["summary", "causes", "effects", "relationships", "historicalSignificance",
                  "quote", "places", "subjectHeadings", "subjects", "frameworks"]:
        if field in data:
            old_val = dj.get(field, None)
            new_val = data[field]
            if old_val != new_val:
                edit_log.append({
                    "field": field,
                    "oldValue": old_val,
                    "newValue": new_val if len(str(new_val)) < 200 else str(new_val)[:200] + "…",
                    "editorId": EDITOR_ID,
                    "sessionId": SESSION_ID,
                    "timestamp": now,
                })

    for field, value in data.items():
        dj[field] = value

    dj["_editLog"] = edit_log

    if era_correction:
        target["era"] = era_correction

    target["_unsyncedEdits"] = True

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    return f"✓ Saved {file_path}"


def main():
    if DRY_RUN:
        print("=== DRY RUN — no files will be written ===\n")

    print(f"Batch 63 enrichment — {len(ENRICHMENTS)} entities\n")

    enriched, skipped, failed = 0, 0, 0
    for item in ENRICHMENTS:
        slug = item["slug"]
        print(f"[{slug}]")
        result = enrich_entity(
            item["file"], slug, item["data"],
            item.get("era_correction"), dry_run=DRY_RUN
        )
        print(f"  {result}")
        if "SKIP" in result:
            skipped += 1
        elif result.startswith("✓") or result.startswith("→"):
            enriched += 1
        else:
            failed += 1

    tag = "DRY RUN" if DRY_RUN else "DONE"
    print(f"\n{tag}: {enriched} enriched, {skipped} skipped, {failed} failed")
    if not DRY_RUN and enriched > 0:
        print("\nNext step: env $(cat .env | xargs) npx tsx scripts/sync_gateway.ts --local")


if __name__ == "__main__":
    main()
