#!/usr/bin/env python3
"""
Batch 40 — 8 entities: Christian Cornelius Paus, José Justo Corro, José Ignacio Pavón,
Miguel Domínguez, Pedro de Viscarra, William Austin, James Fisher Robinson,
George Fletcher Moore
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    # 1 — Christian Cornelius Paus
    ("christian-cornelius-paus", {
        "summary": (
            "Christian Cornelius Paus (1806–1875) was a Norwegian "
            "lawyer and politician who combined multiple public roles "
            "in and around the city of Skien for nearly three decades — "
            "serving simultaneously as city judge, magistrate, chief "
            "of police, and city recorder from 1847 to 1874. "
            "He was also elected three times as Amtmann (Governor) "
            "of Bratsberg County — the mountainous inland county of "
            "southeastern Norway, now part of Telemark — serving "
            "terms between 1862 and 1869, and three times as a "
            "member of the Storting (Norwegian parliament), "
            "making him one of the most active provincial statesmen "
            "of mid-19th-century Norway.\n\n"
            "Paus's career exemplified the character of Norwegian "
            "provincial governance in the 1840s–1870s: in a country "
            "of small towns and dispersed rural populations, a single "
            "capable lawyer could simultaneously hold judicial, "
            "administrative, police, and legislative responsibilities. "
            "The Norwegian civil service of his era was an intimate, "
            "overlapping world in which legal training was the foundation "
            "of almost every public role.\n\n"
            "His service as Governor of Bratsberg County during the "
            "1860s placed him at the center of Norwegian provincial "
            "administration during a decade of rising political tension: "
            "the Venstre (Liberal) movement was building its campaign "
            "for greater Norwegian parliamentary sovereignty within "
            "the union with Sweden, and Bratsberg's timber and iron "
            "industries created distinctive social and economic "
            "pressures that Paus's administration had to manage.\n\n"
            "His three Storting terms gave him national political "
            "standing unusual for a provincial city judge — a career "
            "that illustrated Norway's tight integration of local and "
            "national governance in the age before mass democracy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norwegian lawyer and politician; city judge, magistrate, chief of police, and city recorder of Skien (1847–1874); three-term Governor (Amtmann) of Bratsberg County (1862–1869); three-term Storting (parliament) member; exemplar of Norwegian mid-19th-century provincial multi-role governance.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Norway's mid-19th-century provincial governance structure — in which small cities required a single capable lawyer to fill multiple overlapping judicial, administrative, and police roles simultaneously — created the institutional environment in which Paus's multi-role career was possible and expected",
            "The rise of Norway's constitutional nationalism in the 1860s — and the Storting's growing assertiveness against Swedish royal influence — provided the political context in which a provincial official like Paus could contribute to the national parliamentary debate alongside his local administrative duties",
            "Bratsberg County's timber and iron industries — key sectors in Norway's mid-19th-century economic development — created the economic and social administration challenges that Paus's gubernatorial service had to address"
        ],
        "effects": [
            "His 27-year multi-role service to the city of Skien (1847–1874) provided institutional continuity to one of Norway's most significant inland cities through the decades of industrialization and nationalist political mobilization",
            "His three terms as Governor of Bratsberg County contributed to the management of a key Norwegian county during the 1860s — a decade of national political transformation under the growing constitutional conflict between Storting and royal prerogative",
            "His three Storting terms gave Bratsberg County representation in national debates about Norwegian autonomy, parliamentary sovereignty, and the Liberal constitutional program that would eventually produce the ministerial reform of 1884",
            "His career illustrated the Norwegian civil service model — in which legal professionals served as the backbone of both local and regional governance — a model that contributed to Norway's exceptionally stable transition to constitutional democracy in the 19th century"
        ],
        "relationships": [
            {"entity": "Skien city governance (judge, magistrate, police chief, city recorder, 1847–1874)", "relationship": "MULTI-ROLE_CHIEF_ADMINISTRATOR_OF", "note": "Held all four key Skien civic roles simultaneously — city judge, magistrate, chief of police, and city recorder — for 27 years (1847–1874)"},
            {"entity": "Bratsberg County governorship (three terms, 1862–1869)", "relationship": "THREE-TERM_GOVERNOR", "note": "Served three terms as Amtmann (Governor) of Bratsberg County between 1862 and 1869 — the mountainous inland county now part of Telemark"},
            {"entity": "Norwegian Storting (three-term member)", "relationship": "THREE-TERM_MEMBER", "note": "Elected three times to the Storting (Norwegian parliament) — providing national political representation alongside his provincial administrative roles"},
            {"entity": "Norwegian constitutional nationalism / Venstre movement (1860s)", "relationship": "PROVINCIAL_OFFICIAL_DURING_RISE_OF", "note": "Served as provincial governor during the 1860s — the decade in which the Venstre (Liberal) movement built the political case for Norwegian parliamentary sovereignty"},
            {"entity": "Norwegian provincial governance model (multi-role lawyer-officials)", "relationship": "EXEMPLAR_OF", "note": "His career exemplified the Norwegian provincial governance model in which legal training qualified a single official for simultaneous judicial, administrative, police, and legislative roles"}
        ]
    }),

    # 2 — José Justo Corro
    ("josé-justo-corro", {
        "summary": (
            "José Justo Corro y Silva (1794–1864) was a Mexican "
            "lawyer and statesman who served as President of Mexico "
            "from March 2, 1836 to April 19, 1837 — appointed to "
            "complete the term of President Miguel Barragán, who "
            "had died suddenly in office. Unlike most Mexican "
            "presidents of the turbulent 1830s — who were generals — "
            "Corro was a civilian administrator whose legal background "
            "made him an unusual occupant of the executive chair "
            "during one of Mexico's most constitutionally consequential "
            "periods.\n\n"
            "His presidency was dominated by the sweeping "
            "constitutional transformation encoded in the Siete Leyes "
            "(Seven Laws) of 1836 — a new constitution that replaced "
            "the federalist Republic of 1824 with the Centralist "
            "Republic of Mexico. The Siete Leyes abolished the "
            "federalist structure of the states, concentrating power "
            "in the central government, and created the Supreme Power "
            "Conservadora — a fifth branch of government with the "
            "power to nullify acts of the other four branches — "
            "an institution with no close parallel in the world's "
            "constitutional history.\n\n"
            "His administration also coincided with the Texas "
            "Revolution: the Battle of the Alamo (March 6, 1836), "
            "the massacres at Goliad, and the Battle of San Jacinto "
            "(April 21, 1836) — where Santa Anna was captured and "
            "signed the Treaties of Velasco recognizing Texan "
            "independence — all occurred during Corro's presidency, "
            "though the military command was Santa Anna's.\n\n"
            "He served in various judicial and administrative roles "
            "before and after the presidency, but the Texas crisis "
            "and the Centralist transition defined his brief executive year."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President of Mexico (March 1836–April 1837); a civilian lawyer president who oversaw the Siete Leyes (Seven Laws) constitutional transformation replacing the federalist republic with the Centralist Republic of Mexico; his administration coincided with the Texas Revolution and the Battle of San Jacinto.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The sudden death of President Miguel Barragán in March 1836 — and the constitutional provision for succession — thrust Corro into the presidency at the most critical moment of Mexico's mid-1830s constitutional crisis, with the Siete Leyes transformation underway",
            "The centralist political movement — which had been building since 1834 under Santa Anna's influence and the conservative backlash against federalist radicalism — created the constitutional framework of the Siete Leyes that Corro oversaw as president",
            "The Texas Revolution's escalation to full-scale military conflict in 1836 — and Santa Anna's decision to lead the campaign in person — created the dual crisis of constitutional transformation and frontier military disaster that defined Corro's presidency"
        ],
        "effects": [
            "His presidency oversaw the implementation of the Siete Leyes (1836) — the constitutional framework that replaced the federalist Republic of 1824 with the Centralist Republic, concentrating power in Mexico City and abolishing state sovereignty, a change that provoked multiple subsequent uprisings",
            "The Texas Revolution's culmination during his presidency — the Alamo, Goliad, San Jacinto, and the Treaties of Velasco — resulted in the de facto independence of Texas that Mexico refused to recognize but could not reverse, setting the stage for the Mexican-American War a decade later",
            "The Supreme Power Conservadora created by the Siete Leyes — the fifth branch with power to nullify other branches' acts — proved unworkable in practice and was abolished by the Bases Orgánicas (1843), but its creation during Corro's administration was one of the most unusual constitutional experiments in Mexican history",
            "His brief, crisis-defined presidency illustrated a recurring pattern in early Mexican politics: the civilian lawyer-administrator who occupied the executive chair during the intervals between military leaders' campaigns, providing nominal institutional continuity without real political authority"
        ],
        "relationships": [
            {"entity": "Mexican presidency (March 2, 1836 – April 19, 1837, completing Barragán's term)", "relationship": "PRESIDENT", "note": "Served as President of Mexico (1836–1837) — appointed to complete the term of President Miguel Barragán who had died in office"},
            {"entity": "Siete Leyes (Seven Laws, 1836 Mexican constitution)", "relationship": "PRESIDENT_DURING_IMPLEMENTATION_OF", "note": "His presidency oversaw the Siete Leyes — the constitutional transformation from the federalist Republic of 1824 to the Centralist Republic of Mexico"},
            {"entity": "Texas Revolution / Battle of San Jacinto (April 1836)", "relationship": "PRESIDENT_DURING", "note": "The Alamo, Goliad massacres, and Battle of San Jacinto — where Santa Anna signed the Treaties of Velasco recognizing Texan independence — all occurred during Corro's presidency"},
            {"entity": "Supreme Power Conservadora (5th branch created by Siete Leyes)", "relationship": "CONSTITUTIONAL_EXPERIMENT_DURING_PRESIDENCY_OF", "note": "The unprecedented fifth branch of government — with power to nullify acts of all other branches — was created by the Siete Leyes during Corro's presidency"},
            {"entity": "President Miguel Barragán (predecessor, died in office)", "relationship": "SUCCESSOR_TO", "note": "Appointed to complete Barragán's term after Barragán's sudden death in March 1836 — the succession that brought Corro to the presidency"}
        ]
    }),

    # 3 — José Ignacio Pavón
    ("josé-ignacio-pavón", {
        "summary": (
            "José Ignacio Pavón (1791–1866) was a Mexican jurist "
            "and career civil servant who served as interim President "
            "of Mexico for just two days — August 13–15, 1860 — "
            "during the War of Reform, one of the shortest presidential "
            "tenures in any country's history. Born in Oaxaca, "
            "he spent his career in the Mexican judiciary, rising "
            "to senior positions on the Supreme Court of Justice, "
            "where his longevity in service under multiple regimes "
            "made him a symbol of Mexico's institutional continuity "
            "through decades of political chaos.\n\n"
            "His two-day presidency came at a moment of extreme "
            "constitutional crisis: the conservative general Miguel "
            "Miramón had temporarily abandoned Mexico City in August "
            "1860 as Liberal forces under Benito Juárez advanced, "
            "creating a power vacuum in the capital. Under the "
            "conservative constitutional framework in force, the "
            "presidency fell by default to the most senior justice "
            "of the Supreme Court — Pavón. He occupied the office "
            "for only two days before Miramón's forces returned "
            "and power was handed back to Miramón on August 15.\n\n"
            "Pavón's career spanned the Empire of Iturbide, the "
            "First Mexican Republic, the centralist republic, "
            "the French Intervention, and the restored republic — "
            "a continuous judicial presence across four constitutions, "
            "two empires, and multiple civil wars. His sardonic "
            "remark that he had served under more governments than "
            "he could remember became a widely-quoted emblem of "
            "Mexican political instability.\n\n"
            "'I have served so many governments,' he reportedly "
            "observed, 'that I can no longer count them.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Mexican interim president for two days (August 13–15, 1860) during the War of Reform — one of the shortest presidential tenures in history; career Supreme Court justice who served continuously across the Empire of Iturbide, multiple republics, and the French Intervention; his sardonic remark about serving too many governments became an emblem of Mexican political instability.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The War of Reform (1857–1861) — the three-year civil war between liberal Juaristas and conservative forces — created the military and political crisis in which Miramón's temporary abandonment of Mexico City in August 1860 triggered the constitutional succession that brought Pavón to the presidency",
            "The conservative constitutional framework in force during the War of Reform — which designated the senior Supreme Court justice as presidential successor in the absence of a military executive — created the mechanism through which Pavón's two-day presidency was constitutionally legitimate",
            "Pavón's decades of accumulated seniority on the Mexican Supreme Court — a court that maintained institutional continuity while the executive collapsed and reformed repeatedly — created the technical legal position that made him interim president in August 1860"
        ],
        "effects": [
            "His two-day presidency — legally valid under the conservative constitutional framework — contributed to the complex chain of succession events in the War of Reform that eventually ended with Juárez's liberal victory and the Reform constitution's consolidation",
            "His continuous judicial service across multiple regimes — from Iturbide's empire through the Restored Republic — contributed to the institutional memory of the Mexican judiciary in a period when most other political institutions collapsed and reformed repeatedly",
            "His sardonic observation about serving under innumerable governments became one of the most widely cited quotations about Mexican political instability in the 19th century — a single wit's phrase capturing the entire era's institutional chaos",
            "The precedent of the Supreme Court's senior justice becoming president by default during executive power vacuums — illustrated by Pavón's two-day tenure — contributed to the constitutional thinking about succession provisions in subsequent Mexican constitutions"
        ],
        "relationships": [
            {"entity": "Mexican interim presidency (August 13–15, 1860, two days)", "relationship": "TWO-DAY_INTERIM_PRESIDENT", "note": "Served as Mexican interim president for just two days (August 13–15, 1860) — one of the shortest presidential tenures in history — during Miramón's temporary abandonment of Mexico City"},
            {"entity": "War of Reform (1857–1861) / Liberal-Conservative civil war", "relationship": "INTERIM_EXECUTIVE_DURING", "note": "His two-day presidency occurred at a crisis moment of the War of Reform — Miramón's retreat creating the power vacuum that constitutional succession filled with Pavón"},
            {"entity": "Mexican Supreme Court of Justice (senior justice, long career)", "relationship": "CAREER_SENIOR_JUSTICE_OF", "note": "Spent his career on the Mexican Supreme Court — rising to senior justice and holding the position that made him president by default under conservative constitutional succession rules"},
            {"entity": "General Miguel Miramón (conservative War of Reform leader)", "relationship": "REPLACED_BY_ON_RETURN_AFTER_TWO_DAYS", "note": "Served as president only while Miramón temporarily retreated from Mexico City — power returned to Miramón on August 15, 1860 when his forces came back"},
            {"entity": "Mexican political instability (multiple regime changes)", "relationship": "CONTINUITY_FIGURE_ACROSS_AND_SYMBOL_OF", "note": "Served under the Empire of Iturbide, multiple republics, and the French Intervention — his continuous judicial presence making him an emblem of institutional continuity amid political chaos"}
        ]
    }),

    # 4 — Miguel Domínguez
    ("miguel-domínguez", {
        "summary": (
            "José Miguel Domínguez Alemán (1756–1830) was a "
            "Spanish-born lawyer who became Corregidor of Querétaro "
            "(1802–1810) and one of the most ambiguously heroic figures "
            "of Mexican independence — forever overshadowed by his "
            "wife, Josefa Ortiz de Domínguez, 'La Corregidora,' "
            "whose decisive act in September 1810 triggered the "
            "Mexican War of Independence.\n\n"
            "When the independence conspiracy of Querétaro was "
            "discovered in September 1810 and Miguel was ordered "
            "by the viceroy to arrest the conspirators — whom "
            "he knew personally — he locked his wife Josefa in "
            "their room to prevent her from warning them. "
            "But Josefa managed to pass word through a locked door "
            "to the alcalde Ignacio Pérez, who rode through the "
            "night to warn Ignacio Allende — who in turn warned "
            "Father Miguel Hidalgo in Dolores. On September 16, "
            "1810, Hidalgo rang the church bell and delivered "
            "the Grito de Dolores — launching the Mexican War "
            "of Independence. Miguel's act of locking the door "
            "was thus the mechanism by which the warning reached "
            "Hidalgo.\n\n"
            "After independence, Domínguez served on the "
            "Junta Soberana Provisional Gubernativa — the "
            "transitional committee that managed Mexico's affairs "
            "between Iturbide's abdication in 1823 and the "
            "installation of Guadalupe Victoria as the first "
            "President of Mexico.\n\n"
            "'My wife is bolder than I am,' Domínguez reportedly "
            "admitted — a judgment history has confirmed."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Corregidor of Querétaro (1802–1810); husband of La Corregidora (Josefa Ortiz de Domínguez); when ordered to arrest the independence conspirators he locked his wife up — but she got word through a locked door to Hidalgo's network, triggering the Grito de Dolores (September 16, 1810); member of the transitional Junta Soberana Provisional Gubernativa (1823).",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Querétaro conspiracy's exposure in September 1810 — and Miguel's position as the colonial official ordered to arrest the conspirators he had been hosting — created the impossible conflict between official duty and personal relationships that produced the famous locked-door episode",
            "Josefa Ortiz's determination to warn the conspirators despite her husband's attempt to contain her — and the human geography of Querétaro that allowed her to pass a message through a locked door to the alcalde next door — created the chain of communication that reached Hidalgo",
            "The broader context of New Spain's Bourbon reforms and the grievances of the criollo professional class — to which both Miguel and Josefa belonged — created the political sympathy that made them part of the Querétaro conspiracy in the first place"
        ],
        "effects": [
            "His locking of Josefa in their room — intended to prevent her from warning the conspirators — paradoxically created the dramatic crisis that motivated Josefa's urgent improvised warning through the locked door, which triggered the chain of communication that reached Hidalgo on September 15–16, 1810",
            "The Grito de Dolores on September 16, 1810 — triggered by Josefa's warning passing through the locked door — launched the Mexican War of Independence, making Miguel's act of containment one of the most consequential failed preventions in American history",
            "His post-independence service on the Junta Soberana Provisional Gubernativa (1823) contributed to Mexico's institutional transition from empire to republic — a transitional committee that managed the constitutional vacuum after Iturbide's abdication",
            "The historical memory of Miguel and Josefa Domínguez established a gendered narrative of the independence moment — in which Miguel's masculine authority failed to contain feminine courage — that became central to Mexican nationalist iconography and the memory of La Corregidora"
        ],
        "relationships": [
            {"entity": "Josefa Ortiz de Domínguez — 'La Corregidora' (wife)", "relationship": "HUSBAND_OF", "note": "Husband of Josefa Ortiz de Domínguez 'La Corregidora' — whom he locked in their room in September 1810 to prevent her warning the conspirators, but she passed the message through the door anyway"},
            {"entity": "Grito de Dolores (September 16, 1810) / Mexican War of Independence", "relationship": "INADVERTENT_ENABLER_OF", "note": "His failed attempt to contain Josefa — locking her in their room — created the crisis that triggered her improvised warning to Hidalgo's network, leading to the Grito de Dolores on September 16, 1810"},
            {"entity": "Corregidor of Querétaro (1802–1810)", "relationship": "COLONIAL_OFFICIAL", "note": "Served as Corregidor of Querétaro (1802–1810) — the royal judicial and administrative official of the city, and the position that placed him at the center of the conspiracy's exposure"},
            {"entity": "Junta Soberana Provisional Gubernativa (1823 transitional governing committee)", "relationship": "MEMBER_OF", "note": "Served on the transitional governing committee that managed Mexico's affairs between Iturbide's abdication in 1823 and the installation of Guadalupe Victoria as president"},
            {"entity": "Querétaro independence conspiracy (1810) / criollo professional class", "relationship": "COMPLICIT_MEMBER_AND_OFFICIAL_SUPPRESSOR_OF", "note": "A member of the conspiracy's social world — personally connected to the conspirators — while also being the official ordered to arrest them, creating the conflict that produced the locked-door episode"}
        ]
    }),

    # 5 — Pedro de Viscarra
    ("pedro-de-viscarra", {
        "summary": (
            "Pedro de Viscarra de la Barrera (c.1545–c.1600) was "
            "a Spanish colonial lawyer and official who served twice "
            "as acting Royal Governor of Chile during the late "
            "16th-century conquest era — making him one of the "
            "earliest known figures in Chilean colonial administrative "
            "history. He arrived in the Captaincy General of Chile "
            "from Spain around 1590 as a legal professional in "
            "the colonial administrative apparatus under Governor "
            "Alonso de Sotomayor.\n\n"
            "His acting governorships arose from the administrative "
            "reality of the conquest frontier: when Governor Sotomayor "
            "traveled to Peru in July 1592 to petition the viceroy "
            "of Peru for military reinforcements — urgently needed "
            "for the ongoing Arauco War against the Mapuche — "
            "he left Viscarra as his lieutenant governor with "
            "full acting authority. Viscarra thus had to manage "
            "the precarious military situation on the Araucanía "
            "frontier in Sotomayor's absence.\n\n"
            "The Arauco War — the centuries-long conflict between "
            "Spanish colonial forces and the Mapuche people of "
            "southern Chile — was at an intense phase in the 1590s. "
            "The Mapuche had mounted catastrophically effective "
            "resistance to Spanish expansion south of the Bío-Bío "
            "River, and the colonial frontier was chronically "
            "undermanned and militarily fragile. Managing Chile's "
            "garrison and civil administration during Sotomayor's "
            "absence placed Viscarra in effective command of one "
            "of the most militarily stressed frontiers in the "
            "Spanish colonial empire.\n\n"
            "His second term came under similar circumstances — "
            "reflecting the persistent shortage of senior officials "
            "in the remote Captaincy General of Chile."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Twice acting Royal Governor of Chile (1590s); Spanish colonial lawyer who managed the Arauco War frontier during Governor Sotomayor's absence to Peru; one of the earliest documented figures in Chilean colonial administrative history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Governor Sotomayor's need to travel to the Viceroyalty of Peru to petition for military reinforcements — created by the Arauco War's chronic military demands that exceeded Chile's garrison capacity — created the vacancy that Viscarra's acting governorship was designed to fill",
            "The Spanish colonial administrative structure's reliance on experienced lawyers (letrados) as substitutes for absent military governors — reflecting the blending of judicial and executive authority in colonial governance — created the institutional basis for Viscarra's appointment",
            "The Arauco War's intensity in the 1590s — the Mapuche's successful resistance south of the Bío-Bío having demonstrated the limits of Spanish military power in the region — created the military crisis that made Sotomayor's Peru mission urgent and Viscarra's caretaker role critical"
        ],
        "effects": [
            "His two acting governorships provided continuity to Chile's colonial administration during periods when the colony's appointed governor was absent — maintaining the institutional function of the Captaincy General during frontier military crises",
            "His management of the Arauco War frontier in Sotomayor's absence contributed to maintaining the Spanish colonial position in Chile's contested southern territories — though the Arauco War would continue for another two centuries without resolution",
            "His career as a colonial lawyer-turned-acting-governor illustrated the administrative versatility demanded of educated Spaniards on frontier colonial postings — a career pattern that shaped the development of Spanish colonial governance in South America",
            "His documentation in Chilean colonial records preserved a fragmentary but important trace of the administrative history of Chile's earliest colonial governors — a history that has been largely reconstructed from Spanish archival sources"
        ],
        "relationships": [
            {"entity": "Captaincy General of Chile acting governorship (twice, 1592)", "relationship": "TWICE_ACTING_GOVERNOR", "note": "Served twice as acting Royal Governor of Chile — appointed lieutenant governor when Sotomayor traveled to Peru and when other absences created administrative vacancies"},
            {"entity": "Governor Alonso de Sotomayor (superior who left him in charge)", "relationship": "ACTING_DEPUTY_FOR", "note": "Served as Sotomayor's lieutenant governor and successor when Sotomayor traveled to Peru in July 1592 to petition the viceroy for military reinforcements for the Arauco War"},
            {"entity": "Arauco War / Mapuche resistance (1590s Chile)", "relationship": "COLONIAL_ADMINISTRATOR_MANAGING_FRONTIER_OF", "note": "Managed the Arauco War frontier as acting governor — responsible for Chile's military and civil administration during the colony's most urgent requests for reinforcement"},
            {"entity": "Spanish colonial administration of Chile (Captaincy General, 16th century)", "relationship": "EARLY_OFFICIAL_OF", "note": "One of the earliest documented officials in Chilean colonial administrative history — arriving from Spain around 1590 as a lawyer in the colonial administrative apparatus"},
            {"entity": "Viceroyalty of Peru (military reinforcement requests, 1592)", "relationship": "COLONY_WHOSE_ACTING_GOVERNOR_REQUESTED_AID_FROM", "note": "Sotomayor's petition to the Viceroy of Peru for Arauco War reinforcements — leaving Viscarra in charge — was the act that created Viscarra's first acting governorship"}
        ]
    }),

    # 6 — William Austin
    ("william-austin", {
        "summary": (
            "William Austin (1778–1841) was an American author, "
            "lawyer, and Massachusetts politician — best remembered "
            "as the creator of the 'Peter Rugg' stories, published "
            "in the New England Galaxy from 1824 to 1827. "
            "The Peter Rugg stories — presented as epistolary "
            "letters signed by 'Jonathan Dunwell' — told the tale "
            "of a Boston merchant who, while driving home in a "
            "fierce storm, swore a blasphemous oath and was condemned "
            "to ride eternally through New England without ever "
            "reaching Boston, a ghost condemned to travel the "
            "familiar landscape of New England roads and towns forever.\n\n"
            "The Peter Rugg stories are among the earliest works "
            "of American supernatural fiction — standing alongside "
            "Washington Irving's 'Rip Van Winkle' and 'The Legend "
            "of Sleepy Hollow' as foundational texts of the American "
            "Gothic and supernatural narrative tradition. "
            "Austin's innovation was to set supernatural horror "
            "in the recognizable contemporary landscape of "
            "New England — with real places, recognizable social "
            "types, and the unmistakable atmosphere of the Boston "
            "region — establishing an approach to American Gothic "
            "that would be developed by Hawthorne, Poe, and "
            "subsequent generations.\n\n"
            "Austin also had a notable legal and political career: "
            "he studied law under John Adams, served in the "
            "Massachusetts legislature, and was appointed "
            "district attorney for Suffolk County. His literary "
            "output was small — primarily the Peter Rugg stories "
            "and a few other pieces — but their influence was "
            "disproportionate, with Hawthorne's notebooks showing "
            "familiarity with Austin's supernatural framework.\n\n"
            "He remains one of the most unjustly neglected figures "
            "in early American literature."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "American author and lawyer; creator of the 'Peter Rugg' stories (1824–1827 in the New England Galaxy) — among the earliest works of American supernatural fiction; studied law under John Adams; Massachusetts legislator; his Peter Rugg narrative influenced the American Gothic tradition developed by Hawthorne and Poe.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The early American literary marketplace's hunger for narrative fiction — and the New England Galaxy's willingness to publish extended supernatural narratives in epistolary form — created the publication vehicle that gave Austin's Peter Rugg stories their public reach",
            "New England's rich tradition of supernatural folklore — Puritan damnation narratives, spectral evidence from Salem, the pervasive culture of providential interpretation — provided the cultural substrate from which Austin drew Peter Rugg's condemned wanderer archetype",
            "Washington Irving's success with 'Rip Van Winkle' and 'The Legend of Sleepy Hollow' (1819–1820) demonstrated that American readers would embrace supernatural fiction set in distinctly American landscapes — creating the literary opportunity that Austin seized with Peter Rugg's New England setting"
        ],
        "effects": [
            "The Peter Rugg stories established one of the key archetypes of American supernatural fiction — the damned wanderer condemned to travel eternally without reaching his destination — that influenced subsequent American Gothic writers including Hawthorne and, indirectly, Poe",
            "His setting of supernatural horror in the recognizable contemporary landscape of New England — with real roads, towns, and social types — helped establish the specifically American approach to Gothic fiction that distinguished it from the European Gothic tradition",
            "His study under John Adams and subsequent district attorney career contributed to the Massachusetts legal tradition in the era immediately following the Revolution — though his literary legacy has proven more durable than his legal one",
            "The 'Peter Rugg' stories' persistence in American literary culture — republished, anthologized, and cited across two centuries — made Austin a minor but genuine contributor to the American literary tradition, especially the New England Gothic strand that Hawthorne and later regional writers developed"
        ],
        "relationships": [
            {"entity": "'Peter Rugg, the Missing Man' stories (New England Galaxy, 1824–1827)", "relationship": "CREATOR_OF", "note": "Created the Peter Rugg stories — among the earliest American supernatural fiction — presenting a Boston merchant condemned to ride eternally through New England without reaching home"},
            {"entity": "American Gothic / supernatural fiction tradition (early 19th century)", "relationship": "FOUNDING_CONTRIBUTOR_TO", "note": "Established one of the early archetypes of American supernatural fiction — the damned New England wanderer — that influenced Hawthorne, Poe, and the American Gothic tradition"},
            {"entity": "John Adams (Austin's law teacher)", "relationship": "STUDIED_LAW_UNDER", "note": "Studied law under John Adams — a connection that placed Austin within the most distinguished generation of New England legal and political culture"},
            {"entity": "Washington Irving / Rip Van Winkle tradition (contemporary influence)", "relationship": "PARALLEL_AMERICAN_SUPERNATURAL_TRADITION_WITH", "note": "Contemporary of Irving's Rip Van Winkle and Sleepy Hollow (1819–1820) — Austin's Peter Rugg standing alongside Irving's work as a foundational text of American supernatural narrative"},
            {"entity": "Massachusetts legislature / Suffolk County district attorney", "relationship": "LEGISLATOR_AND_PROSECUTOR", "note": "Served in the Massachusetts legislature and as district attorney for Suffolk County — a legal and political career that ran parallel to his small but influential literary output"}
        ]
    }),

    # 7 — James Fisher Robinson
    ("james-fisher-robinson", {
        "summary": (
            "James Fisher Robinson (1800–1882) was an American "
            "lawyer and politician who served as the 22nd Governor "
            "of Kentucky from 1862 to 1863 — completing the "
            "remainder of the term of Governor Beriah Magoffin, "
            "whose Confederate sympathies had rendered him "
            "politically ineffective after the Union supermajority "
            "won Kentucky's 1861 elections. Born in Scott County, "
            "Kentucky, Robinson was a Unionist Democrat who "
            "represented the pragmatic middle of Kentucky "
            "politics — unwilling to follow the Confederacy "
            "but also resistant to radical Republicanism.\n\n"
            "Robinson stepped into the governorship through "
            "the Kentucky Senate, where he served as Speaker, "
            "after the legislature's pro-Union supermajority "
            "effectively stripped Magoffin of real executive power. "
            "His tenure coincided with some of the most intense "
            "Civil War military activity in Kentucky: John Hunt "
            "Morgan's Confederate cavalry raids terrorized the "
            "state's interior, the Battle of Perryville (October "
            "8, 1862) — the largest Civil War battle in Kentucky "
            "— was fought while he was governor, and the Confederate "
            "Army of Tennessee under Bragg and Kirby Smith briefly "
            "established a Confederate government at Frankfort "
            "in September 1862.\n\n"
            "Robinson's firm maintenance of Kentucky's Union "
            "alignment during this period of Confederate invasion "
            "was crucial to keeping the state within the United States. "
            "He served approximately eight months — enough to "
            "stabilize the Union position before Thomas Bramlette "
            "won the next election.\n\n"
            "His post-gubernatorial career continued in law "
            "and local politics in Georgetown, Kentucky, "
            "where he lived until 1882."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "22nd Governor of Kentucky (1862–1863); Unionist Democrat who completed Beriah Magoffin's term after the Confederate-sympathizing governor became ineffective; governed during the Battle of Perryville (October 1862) and the Confederate invasion that briefly established a Confederate government at Frankfort; his tenure maintained Kentucky's Union alignment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Governor Beriah Magoffin's Confederate sympathies — and the pro-Union supermajority's effective seizure of Kentucky legislative power in 1861 — created the political vacuum that Robinson, as Speaker of the Kentucky Senate, was positioned to fill",
            "Kentucky's strategic importance to both Union and Confederacy — a border state whose loyalty Lincoln famously said would decide the war — created the context in which Robinson's firm Union alignment during the Confederate invasion was a decision of national consequence",
            "The Confederate Army of Tennessee's Kentucky campaign of autumn 1862 — Bragg's and Kirby Smith's invasion that briefly established a Confederate government at Frankfort — created the military crisis that Robinson's governorship had to manage"
        ],
        "effects": [
            "His maintenance of Kentucky's Union alignment during the Confederate invasion of autumn 1862 — including the Battle of Perryville and the brief Confederate government at Frankfort — contributed to Kentucky remaining a Union state through the war's most dangerous period for border-state loyalty",
            "His tenure provided the institutional continuity of Kentucky's state government during the period when Confederate forces briefly captured the state capital — a critical function in preserving the Union's claim to Kentucky's legal and administrative apparatus",
            "His completion of Magoffin's term without triggering a constitutional crisis — navigating the transition from a Confederate-sympathizing governor to full Union control through legal institutional means rather than military coup — established a precedent for managing political succession under wartime pressure",
            "The Battle of Perryville (October 8, 1862) — fought during his governorship — was the decisive action that drove the Confederate Army of Tennessee out of Kentucky permanently, securing the state's Union position for the remainder of the war"
        ],
        "relationships": [
            {"entity": "22nd Governor of Kentucky (1862–1863, completing Magoffin's term)", "relationship": "22ND_GOVERNOR", "note": "Served as 22nd Governor of Kentucky (1862–1863) — stepping up from Speaker of the Kentucky Senate to complete Beriah Magoffin's term after Magoffin's Confederate sympathies paralyzed his governorship"},
            {"entity": "Governor Beriah Magoffin (predecessor, Confederate sympathizer)", "relationship": "SUCCESSOR_COMPLETING_TERM_OF", "note": "Completed the term of Governor Beriah Magoffin — a Confederate sympathizer who had become ineffective after the 1861 Union supermajority effectively stripped him of real executive power"},
            {"entity": "Battle of Perryville (October 8, 1862) / Confederate Kentucky invasion", "relationship": "GOVERNOR_DURING", "note": "Governed Kentucky during the Confederate Army of Tennessee's Kentucky invasion — including the Battle of Perryville (the largest Civil War battle in Kentucky) that drove Confederate forces out permanently"},
            {"entity": "Confederate government at Frankfort, Kentucky (September 1862)", "relationship": "GOVERNOR_OPPOSING", "note": "Governed Kentucky when Confederate forces briefly occupied Frankfort and established a Confederate state government — maintaining the Union administration's claim to Kentucky's governmental legitimacy"},
            {"entity": "Kentucky's border-state Union alignment (Civil War)", "relationship": "MAINTAINED_DURING_CRITICAL_PERIOD", "note": "His firm Union alignment during the Confederate invasion maintained Kentucky's position as a Union state through the war's most dangerous period for border-state loyalty"}
        ]
    }),

    # 8 — George Fletcher Moore
    ("george-fletcher-moore", {
        "summary": (
            "George Fletcher Moore (1798–1886) was an Irish-born "
            "lawyer and colonial official who became one of the "
            "most prominent early settlers of the Swan River Colony "
            "(modern Western Australia) — arriving in 1830 just "
            "one year after the colony's founding and rapidly "
            "establishing himself as a key figure in its ruling "
            "elite. As a land commissioner, magistrate, and colonial "
            "administrator, he was deeply embedded in the colonial "
            "land system that dispossessed the Nyungar Aboriginal "
            "people of southwestern Australia.\n\n"
            "Moore conducted several significant exploring "
            "expeditions into the Western Australian interior, "
            "contributing to the European mapping and naming "
            "of the region's geography. He is most notable to "
            "historians for compiling the 'Descriptive Vocabulary "
            "of the Language in Common Use Amongst the Aborigines "
            "of Western Australia' (1842) — one of the earliest "
            "published records of the Nyungar language, the "
            "Aboriginal language family of the southwestern "
            "corner of the continent.\n\n"
            "His linguistic work, however imperfect by modern "
            "standards, preserves vocabulary and observations "
            "from the first-contact period of the colony that "
            "are still referenced by linguists and Nyungar "
            "communities engaged in language revival work today. "
            "His diary, 'Diary of Ten Years Eventful Life of an "
            "Early Settler in Western Australia' (published 1884), "
            "is also a primary source of the colony's founding decade.\n\n"
            "Moore's dual role — as both a linguistic recorder "
            "of Aboriginal culture and a beneficiary of the settler "
            "colonialism that was destroying it — makes him "
            "one of the most complex figures in Western "
            "Australian colonial history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Prominent early settler of the Swan River Colony (arrived 1830, one year after founding); colonial land commissioner and magistrate; compiled the 'Descriptive Vocabulary of the Language in Common Use Amongst the Aborigines of Western Australia' (1842) — one of the earliest published records of Nyungar; conducted exploring expeditions; his dual role as Aboriginal language recorder and colonial dispossessor makes him a complex figure in Western Australian history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The founding of the Swan River Colony in 1829 and the colonial land rush that followed — offering land grants to settlers willing to develop the new British colony in southwestern Australia — created the opportunity that brought Moore to Western Australia in 1830",
            "Moore's legal training and administrative skills — combined with the colony's critical shortage of qualified professional administrators in its first decades — created the conditions for his rapid rise to positions of influence in the colonial land commission and magistracy",
            "The early colonial period's intellectual culture — in which educated settlers like Moore combined administrative roles with naturalistic observation, geographic exploration, and linguistic documentation — created the framework within which his Nyungar vocabulary became possible"
        ],
        "effects": [
            "His 'Descriptive Vocabulary of the Language in Common Use Amongst the Aborigines of Western Australia' (1842) preserved one of the earliest substantial records of Nyungar vocabulary from the first-contact period — a primary source that continues to inform linguistic research and Nyungar language revival efforts",
            "His diary — published in 1884 as 'Diary of Ten Years Eventful Life of an Early Settler in Western Australia' — provided a detailed primary source of the Swan River Colony's founding decade that historians of Western Australia continue to use",
            "His exploring expeditions into the Western Australian interior contributed to the European geographical mapping and naming of the region — a colonizing knowledge-making that facilitated subsequent pastoral and agricultural expansion",
            "His career as land commissioner and magistrate contributed to the legal administration of the land dispossession system that stripped the Nyungar people of their southwestern Australian territories — making him simultaneously a cultural documentarian and an agent of cultural destruction"
        ],
        "relationships": [
            {"entity": "Swan River Colony / early Western Australia (arrived 1830)", "relationship": "PROMINENT_EARLY_SETTLER_AND_ADMINISTRATOR", "note": "Arrived in the Swan River Colony in 1830 — one year after its founding — and became one of the most prominent figures in its early ruling elite as land commissioner, magistrate, and explorer"},
            {"entity": "'Descriptive Vocabulary of the Language in Common Use Amongst the Aborigines of Western Australia' (1842)", "relationship": "COMPILER_OF", "note": "Compiled one of the earliest published records of the Nyungar language — a primary source still referenced by linguists and Nyungar language revival communities"},
            {"entity": "Nyungar Aboriginal people / language (southwestern Australia)", "relationship": "EARLIEST_LINGUISTIC_DOCUMENTER_AND_COLONIAL_DISPOSSESSOR_OF", "note": "His dual role — compiling one of the earliest records of the Nyungar language while administering the colonial land system that dispossessed Nyungar people — makes him one of the most complex figures in Western Australian colonial history"},
            {"entity": "Western Australian exploring expeditions (colonial interior mapping)", "relationship": "CONDUCTED_SEVERAL", "note": "Conducted several exploring expeditions into the Western Australian interior — contributing to European geographical knowledge and facilitating subsequent colonial expansion"},
            {"entity": "'Diary of Ten Years Eventful Life of an Early Settler in Western Australia' (published 1884)", "relationship": "AUTHOR_OF", "note": "Authored a primary source diary of the Swan River Colony's founding decade — published in 1884 and widely used by historians of early Western Australia"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 40)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
