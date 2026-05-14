#!/usr/bin/env python3
"""
Batch 66 — 8 entities: Henry Baldwin, Roger of Salisbury, Daniel S. Dickinson,
Hippolyte Metdepenningen, Samuel J. Potter, Waller Taylor, James Fisk,
Mariano Egaña
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

    ("henry-baldwin", {
        "summary": (
            "Henry Baldwin (1780–1844) was "
            "an American lawyer, Congressman, "
            "and jurist who served as "
            "Associate Justice of the "
            "U.S. Supreme Court (1830–1844) "
            "— appointed by President "
            "Andrew Jackson. A Pennsylvania "
            "Federalist-turned-Jacksonian, "
            "Baldwin brought a complex "
            "and sometimes erratic "
            "jurisprudence to the Court "
            "— he was personally close "
            "to Jackson but often disagreed "
            "with the Democratic Party's "
            "constitutional positions, "
            "producing opinions that "
            "defied easy categorization.\n\n"
            "Baldwin had been a prominent "
            "Pittsburgh lawyer and "
            "Congressman (1817–1822) "
            "before his Court appointment. "
            "His industrial Pittsburgh "
            "perspective — representing "
            "a manufacturing district "
            "with interests in protective "
            "tariffs and internal improvements "
            "— sometimes put him at "
            "odds with the Southern "
            "Jacksonian mainstream.\n\n"
            "His mental health was "
            "unstable — he suffered "
            "breakdowns that intermittently "
            "prevented him from sitting "
            "— and he died in poverty "
            "despite his high office, "
            "an unusual fate for a "
            "Supreme Court Justice.\n\n"
            "He wrote a significant "
            "constitutional law treatise "
            "('A General View of the "
            "Origin and Nature of the "
            "Constitution') in 1837."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Supreme Court Associate Justice (1830–1844); Andrew Jackson appointee; Pennsylvania Congressman and Pittsburgh industrialist whose complex jurisprudence defied Jacksonian categorization; author of constitutional treatise (1837); suffered mental breakdowns during service and died in poverty — unusual trajectory for a Supreme Court Justice.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Andrew Jackson's court-building strategy — his determination to appoint loyal Jacksonian Democrats to the Supreme Court to secure its alignment with Democratic constitutional principles — created the appointment that elevated Baldwin from Pennsylvania politics to the Court",
            "Baldwin's Pittsburgh base in the manufacturing economy — his representation of an industrial district with strong tariff and internal improvement interests — gave him an economic perspective that complicated his Jacksonian jurisprudence with pro-development instincts",
            "The Jacksonian era's constitutional conflicts — the bank war, states' rights debates, Native American removal, and commerce clause controversies — created the substantive constitutional issues on which Baldwin's jurisprudence developed"
        ],
        "effects": [
            "His fourteen-year tenure contributed a complex and distinctive voice to the Taney Court's jurisprudence — neither a pure states'-rights Democrat nor a Whig nationalist, Baldwin forced the Court to grapple with positions that challenged easy categorization",
            "His 1837 constitutional treatise contributed to antebellum constitutional scholarship — providing a written analysis of constitutional origins and structure from a serving Supreme Court Justice's perspective",
            "His mental illness and financial difficulties during Court service illustrated the inadequate institutional support structure for Supreme Court Justices in the early republic — the lack of pension, adequate salary, and institutional support that made Baldwin's situation so difficult",
            "His Pittsburgh industrial background contributed a manufacturing perspective to the antebellum Supreme Court — a contrast to the Southern planter and New England commercial lawyer backgrounds that dominated most of his colleagues' formations"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1830–1844"},
            {"target": "andrew-jackson", "verb": "APPOINTED_BY", "note": "Jackson's 1830 Supreme Court appointment"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1817–1822"},
            {"target": "pittsburgh", "verb": "REPRESENTS", "note": "Pittsburgh lawyer and manufacturing interests"},
            {"target": "taney-court", "verb": "SERVES_ON", "note": "Member of the Taney Court era"}
        ]
    }),

    ("roger-of-salisbury", {
        "summary": (
            "Roger of Salisbury (d. 1139) "
            "was a Norman ecclesiastic "
            "and royal administrator who "
            "served as Chancellor and "
            "then as Chief Justiciar "
            "of England under King Henry I "
            "(r. 1100–1135) — effectively "
            "the second most powerful "
            "person in the realm and "
            "the architect of the "
            "Henrician administrative "
            "system that made England "
            "the best-governed kingdom "
            "in twelfth-century Europe. "
            "Roger built the Exchequer "
            "— England's sophisticated "
            "royal financial accounting "
            "system — into its definitive "
            "form, creating the "
            "institutional machinery "
            "that Henry I used to "
            "extract unprecedented "
            "revenue from England "
            "and that became the "
            "model for medieval "
            "royal finance.\n\n"
            "Roger's administrative "
            "genius transformed English "
            "royal government — creating "
            "systematic record-keeping, "
            "regularized auditing of "
            "sheriffs' accounts, and "
            "a professional royal "
            "bureaucracy staffed by "
            "trained clerks.\n\n"
            "After Henry I's death (1135), "
            "Roger initially supported "
            "King Stephen but was "
            "arrested and humiliated "
            "by Stephen in 1139 — "
            "an event that shocked "
            "the church and contributed "
            "to the civil war known "
            "as the Anarchy.\n\n"
            "He is one of the most "
            "important administrators "
            "in English medieval history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Chief Justiciar of England under Henry I; built the Exchequer into its definitive institutional form; architect of the Henrician administrative revolution that made England the best-governed kingdom in twelfth-century Europe; his arrest by King Stephen (1139) contributed to the Anarchy civil war; one of the most consequential medieval administrators in English history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Henry I's determination to build effective royal government — the king's need for systematic revenue extraction, reliable administration, and control over the feudal magnates — created the demand for Roger's administrative genius and elevated him to the Chief Justiciar's office",
            "The Norman administrative tradition — the sophisticated governance practices that the Normans had developed in Normandy and that they brought to England — provided the institutional framework that Roger systematized and extended into the definitive Henrician administrative system",
            "Roger's ecclesiastical position as Bishop of Salisbury — the church's role as the source of literate clerks who staffed royal administration, which gave Roger both his training in record-keeping and accounting and his institutional network of trained subordinates"
        ],
        "effects": [
            "His construction of the Exchequer system — the regular biannual accounting of royal revenues using the abacus-like exchequer cloth and producing the Pipe Rolls — created the institutional infrastructure for medieval English royal finance that remained in use for centuries",
            "His administrative revolution under Henry I created the first professional royal bureaucracy in medieval England — the system of trained royal clerks, regularized record-keeping, and systematized royal justice that made Henry I's government so effective",
            "His arrest by King Stephen (1139) — the humiliation of the most powerful ecclesiastical administrator in England — contributed to the alienation of the church and baronage from Stephen's government and helped produce the conditions for the Anarchy civil war",
            "His model of ecclesiastical-royal administration — the bishop-administrator who combined church wealth and influence with royal service — became the dominant model of English royal governance through the twelfth and into the thirteenth century"
        ],
        "relationships": [
            {"target": "henry-i-england", "verb": "SERVES", "note": "Chief Justiciar and Chancellor under Henry I"},
            {"target": "exchequer-england", "verb": "BUILDS", "note": "Built the Exchequer into its definitive institutional form"},
            {"target": "king-stephen-england", "verb": "ARRESTED_BY", "note": "Arrested and humiliated by Stephen in 1139"},
            {"target": "the-anarchy", "verb": "CONTRIBUTES_TO", "note": "His arrest contributed to the civil war's causes"},
            {"target": "bishopric-of-salisbury", "verb": "SERVES_AS", "note": "Bishop of Salisbury while serving as royal administrator"}
        ]
    }),

    ("daniel-s-dickinson", {
        "summary": (
            "Daniel Stevens Dickinson (1800–1866) "
            "was an American Democratic "
            "politician from New York who "
            "served as U.S. Senator (1844–1851) "
            "and became one of the most "
            "prominent 'Hunker' Democrats "
            "— the conservative wing of "
            "New York Democracy that "
            "supported the Compromise "
            "of 1850 and opposed the "
            "antislavery 'Barnburner' "
            "faction that followed "
            "Martin Van Buren into the "
            "Free Soil Party. His "
            "controversial 'Dickinson "
            "Resolutions' (1847) — "
            "which endorsed the extension "
            "of the Missouri Compromise "
            "line to the Pacific — "
            "were an attempt to resolve "
            "the slavery-in-the-territories "
            "crisis that deeply divided "
            "New York Democrats.\n\n"
            "Dickinson was a consummate "
            "New York political infighter "
            "— an expert at the Democratic "
            "machine politics of "
            "Tammany Hall and Albany "
            "Regency — who navigated "
            "the treacherous factional "
            "waters of antebellum "
            "New York politics with "
            "considerable skill.\n\n"
            "After the Democratic Party "
            "split in 1860, Dickinson "
            "became a War Democrat — "
            "supporting Lincoln's "
            "suppression of the rebellion "
            "— and was considered for "
            "Lincoln's 1864 running mate.\n\n"
            "He was one of antebellum "
            "New York's most powerful Democrats."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York Democratic Senator (1844–1851); Hunker Democrat leader who opposed Free Soil antislavery; proposed the Dickinson Resolutions (1847) on slavery extension; War Democrat supporting Lincoln after 1861; considered as Lincoln's 1864 running mate; master of New York machine politics through the most divisive antebellum decades.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Barnburner-Hunker split in New York Democracy — the deep factional divide between antislavery Van Buren Democrats and conservative Hunker Democrats over slavery extension — placed Dickinson as the leading Hunker voice and shaped his entire political career",
            "The Wilmot Proviso controversy (1846–1850) — the explosive debate over whether slavery should be excluded from territories acquired from Mexico — created the political crisis that Dickinson's resolutions attempted to resolve and that ultimately destroyed the Democratic consensus",
            "New York's central importance in national Democratic politics — the largest state's electoral votes and the Albany Regency's organizational sophistication — made New York Democratic leaders like Dickinson nationally important figures whose positions on slavery shaped the national party's direction"
        ],
        "effects": [
            "His Dickinson Resolutions (1847) contributed to the national debate over slavery extension — offering the Missouri Compromise line extension as a compromise formula that was ultimately rejected in favor of popular sovereignty in the Compromise of 1850",
            "His Hunker leadership contributed to the destruction of the Democratic coalition in New York — the Barnburner-Hunker split that sent Van Buren to the Free Soil Party in 1848 and fractured New York Democracy for years",
            "His War Democrat stance after 1861 contributed to the bipartisan Union coalition — the collaboration of loyal Democrats with Republicans that Lincoln needed to prosecute the Civil War with maximum political support",
            "His consideration as Lincoln's 1864 running mate — ultimately losing to Andrew Johnson — illustrated the Union Party's strategy of broadening its coalition by selecting a Southern war Democrat"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New York Senator 1844–1851"},
            {"target": "hunker-democrats", "verb": "LEADS", "note": "Leading Hunker Democrat in New York"},
            {"target": "free-soil-party", "verb": "OPPOSES", "note": "Opposed Barnburner antislavery Democrats"},
            {"target": "compromise-of-1850", "verb": "SUPPORTS", "note": "Supported the sectional compromise"},
            {"target": "abraham-lincoln", "verb": "SUPPORTS", "note": "War Democrat who supported Lincoln's war effort"}
        ]
    }),

    ("hippolyte-metdepenningen", {
        "summary": (
            "Hippolyte Metdepenningen (1799–1881) "
            "was a Belgian liberal lawyer "
            "and politician who played "
            "a significant role in Belgian "
            "constitutional and political "
            "life during the mid-nineteenth "
            "century. As one of the "
            "prominent lawyers and "
            "political figures of the "
            "young Belgian state created "
            "by the 1830 Revolution, "
            "he contributed to the "
            "development of Belgian "
            "liberal political culture "
            "and jurisprudence.\n\n"
            "The 1830 Belgian Revolution "
            "— which separated Belgium "
            "from the Kingdom of the "
            "Netherlands and created "
            "an independent constitutional "
            "monarchy with one of the "
            "most liberal constitutions "
            "in Europe — produced a "
            "generation of liberal "
            "lawyers and politicians "
            "who built the Belgian "
            "state's institutions and "
            "defined its distinctive "
            "political character.\n\n"
            "Metdepenningen was associated "
            "with the Belgian Liberal "
            "Party — the anticlerical "
            "liberalism that competed "
            "with Catholic conservatism "
            "in Belgian politics through "
            "the nineteenth century "
            "in what became the 'school "
            "war' over education.\n\n"
            "His long career (d. 1881) "
            "made him a witness to "
            "Belgium's entire formative "
            "period from revolutionary "
            "independence to industrial "
            "nation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Belgian liberal lawyer and politician active from the 1830 Revolution through the 1870s; contributed to Belgian liberal political culture and jurisprudence; associated with the Liberal Party in the Catholic-Liberal 'school war'; part of the generation that built Belgium's constitutional institutions after independence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Belgian Revolution of 1830 — the uprising that separated Belgium from the Netherlands and created an independent constitutional monarchy — launched the Belgian state-building project and created the political context for Metdepenningen's career",
            "The Belgian Constitution of 1831 — one of the most liberal constitutions in Europe, guaranteeing freedom of press, assembly, religion, and education — provided the constitutional framework within which Belgian liberal politics developed",
            "The Catholic-Liberal polarization of Belgian politics — the structural divide between the Catholic Party defending church schools and religious influence and the Liberal Party's anticlerical program — defined the political conflict within which Metdepenningen's liberal career was situated"
        ],
        "effects": [
            "His legal and political career contributed to the development of Belgian liberal jurisprudence and political culture — part of the generation that translated the 1831 Constitution's liberal principles into governing practice",
            "His association with the Liberal Party contributed to Belgian liberalism's development as a political force — the anticlerical liberal tradition that competed with Catholicism for control of Belgian education and civic institutions",
            "His long career bridged Belgium's revolutionary origins and its developed industrial-state maturity — providing institutional memory and legal expertise across Belgium's most formative decades",
            "His career illustrated the pattern of Belgian liberal lawyer-politicians who combined legal practice with political engagement in the young constitutional state — the professional class that built Belgium's civic institutions"
        ],
        "relationships": [
            {"target": "belgium", "verb": "SERVES", "note": "Belgian lawyer and politician"},
            {"target": "belgian-revolution-1830", "verb": "PARTICIPATES_IN_AFTERMATH", "note": "Career built on the revolutionary constitutional settlement"},
            {"target": "belgian-liberal-party", "verb": "ASSOCIATED_WITH", "note": "Liberal politician in Catholic-Liberal political conflict"},
            {"target": "belgian-constitution-1831", "verb": "WORKS_UNDER", "note": "Career within the liberal 1831 constitutional framework"},
            {"target": "school-war-belgium", "verb": "PARTICIPATES_IN", "note": "Liberal participant in Catholic-Liberal education conflict"}
        ]
    }),

    ("samuel-j-potter", {
        "summary": (
            "Samuel John Potter (1753–1804) "
            "was an American lawyer and "
            "politician from Rhode Island "
            "who served as a U.S. Senator "
            "(1803–1804) — but died "
            "after only one year in office. "
            "Before his brief Senate "
            "service, he had a long "
            "career in Rhode Island "
            "politics and law, serving "
            "in various state offices "
            "and as a Rhode Island "
            "Superior Court Justice.\n\n"
            "Rhode Island in this period "
            "was the most unusual state "
            "in the Union — still operating "
            "under its 1663 colonial charter "
            "(it did not adopt a state "
            "constitution until 1842), "
            "with an extremely limited "
            "franchise restricted to "
            "freeholders that excluded "
            "most of the growing industrial "
            "workforce. This constitutional "
            "anomaly made Rhode Island "
            "a political outlier and "
            "eventually produced the "
            "Dorr Rebellion (1842), "
            "which Potter did not "
            "live to see.\n\n"
            "His Rhode Island Superior "
            "Court service contributed "
            "to the development of "
            "Rhode Island jurisprudence "
            "during the early republic — "
            "a state that had been "
            "the most resistant to "
            "the Constitution's ratification "
            "(it was last to ratify, "
            "in 1790, only under "
            "economic pressure).\n\n"
            "He died in office in 1804."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Rhode Island Senator (1803–1804, died in office) and Superior Court Justice; career in the most constitutionally anomalous state in the early republic — Rhode Island still operated under its 1663 colonial charter; last state to ratify the Constitution (1790); representative of the early republic's legal and political development in a resistant founding state.",
            "significanceCategory": "local"
        },
        "causes": [
            "Rhode Island's unique political anomaly — its continued operation under the 1663 colonial charter, which restricted voting to freeholders and made it the most conservative constitutional outlier in the early republic — shaped the political environment within which Potter's career developed",
            "Rhode Island's belated and reluctant Constitution ratification (1790) — the last state to ratify, only under economic pressure from the federal tariff — created the political culture of Rhode Island exceptionalism and resistance within which Potter's legal and political career was situated",
            "The early republic's need for trained lawyers to staff state court systems — the Superior Courts and other judicial institutions that the new states required — created the demand for Potter's judicial service"
        ],
        "effects": [
            "His Rhode Island Superior Court service contributed to the development of Rhode Island law during the critical early republic period — establishing precedents and judicial practices in a state that was operating under a seventeenth-century colonial charter",
            "His brief Senate service represented Rhode Island in the federal government during the final years of Federalist dominance and the beginning of the Jeffersonian Revolution of 1800's full effects",
            "His death in office (1804) created a Rhode Island Senate vacancy that required another appointment — one of several deaths in office that characterized the high mortality of early republic political life",
            "His career illustrated Rhode Island's distinctive political culture — the state that had been most resistant to both the Constitution and federal authority, operating under its anachronistic colonial charter while the rest of the nation built modern state institutions"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Rhode Island Senator 1803–1804"},
            {"target": "rhode-island", "verb": "SERVES", "note": "Long career in Rhode Island politics and law"},
            {"target": "rhode-island-superior-court", "verb": "SERVES_AS_JUSTICE", "note": "Rhode Island Superior Court Justice"},
            {"target": "rhode-island-colonial-charter", "verb": "WORKS_UNDER", "note": "Career under the anomalous 1663 colonial charter"},
            {"target": "us-constitution-ratification", "verb": "REPRESENTS", "note": "From last state to ratify the Constitution (1790)"}
        ]
    }),

    ("waller-taylor", {
        "summary": (
            "Waller Taylor (1786–1826) was "
            "an American Democratic-Republican "
            "politician and military officer "
            "from Indiana who served as "
            "a U.S. Senator (1816–1825) "
            "— one of Indiana's first "
            "senators after statehood "
            "(1816). His Senate service "
            "coincided with the Era "
            "of Good Feelings — the "
            "brief period of apparent "
            "national political unity "
            "following the War of 1812 "
            "and the collapse of the "
            "Federalist Party, when "
            "the Democratic-Republican "
            "Party briefly monopolized "
            "national politics before "
            "fracturing into the Jacksonian "
            "and National Republican "
            "wings in the 1820s.\n\n"
            "Indiana was one of the "
            "newest states in the Union "
            "when Taylor was elected "
            "— admitted in 1816 as "
            "the nineteenth state, "
            "carved out of the old "
            "Northwest Territory. "
            "Its early senators were "
            "foundational figures "
            "in the young state's "
            "development, helping "
            "to define Indiana's "
            "relationship with the "
            "federal government "
            "and its political culture.\n\n"
            "Taylor had served in "
            "the War of 1812 before "
            "his political career "
            "— part of the "
            "generation of veterans "
            "who moved into politics "
            "after the war.\n\n"
            "He died in office in 1826."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "One of Indiana's first senators (1816–1825, died in office); served during the Era of Good Feelings as Indiana — admitted in 1816 — built its federal relationship; War of 1812 veteran; foundational figure in Indiana's early political development as the state transitioned from Northwest Territory to statehood.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Indiana statehood (1816) — the admission of Indiana as the nineteenth state, carved from the Northwest Territory — created the Senate seats that Taylor filled as one of the state's foundational senators",
            "The Era of Good Feelings political environment — the collapse of the Federalist Party after 1815 and the Democratic-Republican monopoly on national politics — created the nonpartisan (or single-party) political atmosphere within which Taylor's Senate service took place",
            "The War of 1812's role in generating political careers — the pattern by which military service in the war created reputations and networks that translated into political success — contributed to Taylor's political ascent in the new Indiana state"
        ],
        "effects": [
            "His Senate service helped establish Indiana's relationship with the federal government during the state's most formative years — representing a rapidly developing frontier state as it built its institutions and defined its political culture",
            "His service as one of Indiana's first senators contributed to the development of Indiana's political traditions — setting patterns of federal representation that the state's subsequent political culture built upon",
            "His death in office (1826) — during the political transition from the Era of Good Feelings to the Jacksonian fracturing of Democratic-Republicanism — meant he did not participate in the fundamental political realignment of the late 1820s",
            "His career illustrated the pattern of War of 1812 veteran politicians who shaped the frontier states of the old Northwest during the Era of Good Feelings — the military-to-political pipeline that produced much of Indiana's early leadership"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Indiana Senator 1816–1825"},
            {"target": "indiana", "verb": "REPRESENTS", "note": "One of Indiana's first senators after statehood"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Senator during the Era of Good Feelings"},
            {"target": "war-of-1812", "verb": "SERVES_IN", "note": "War of 1812 veteran before political career"},
            {"target": "northwest-territory", "verb": "SETTLES", "note": "From the former Northwest Territory — Indiana"}
        ]
    }),

    ("james-fisk", {
        "summary": (
            "James Fisk (1763–1844) was "
            "an American Democratic-Republican "
            "politician from Vermont who "
            "served in both the U.S. House "
            "of Representatives (1805–1809) "
            "and the U.S. Senate (1817–1818) "
            "— a relatively rare accomplishment "
            "of serving in both chambers. "
            "He was associated with the "
            "Green Mountain Boys tradition "
            "of Vermont politics — the "
            "independent, fiercely "
            "egalitarian political culture "
            "of a state that had been "
            "an independent republic "
            "before joining the Union "
            "in 1791.\n\n"
            "Vermont in this period "
            "was a strongly Federalist "
            "state — the only New England "
            "state where Federalists "
            "maintained significant "
            "strength into the 1810s "
            "— and Fisk's Democratic-Republican "
            "politics made him a minority "
            "voice within Vermont's "
            "political mainstream, "
            "though the Jeffersonian "
            "Republicans made consistent "
            "gains throughout the region.\n\n"
            "His House service coincided "
            "with Jefferson's and "
            "Madison's administrations "
            "— the Embargo Act, "
            "the lead-up to the "
            "War of 1812 — while "
            "his brief Senate service "
            "came in the immediate "
            "post-war period.\n\n"
            "He lived to eighty-one."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Democratic-Republican Congressman (1805–1809) and Senator (1817–1818); Democratic-Republican voice in Federalist-dominated Vermont; served through Jefferson's Embargo and Madison's War of 1812; part of the independent Vermont political tradition descended from the Green Mountain Boys republic.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's political transition from independence — the former Republic of Vermont's 1791 admission as the fourteenth state brought an independent-minded political culture that contained both Federalist commercial and Democratic-Republican agrarian currents — created the environment for Fisk's Democratic-Republican political career in a predominantly Federalist state",
            "Jefferson's political mobilization — the Jeffersonian Democratic-Republicans' organization of opposition to Federalist policies throughout New England — created the political network within which Vermont Democratic-Republicans like Fisk operated",
            "The Embargo Act controversy (1807–1809) — Jefferson's attempt to coerce Britain and France through economic embargo, which devastated New England commerce and massively increased anti-Federalist sentiment — created the political crisis during Fisk's House service"
        ],
        "effects": [
            "His House service contributed Vermont's Democratic-Republican voice to the Embargo Act debates — representing a minority perspective in a Federalist-dominated state where the Embargo's commercial damage was felt acutely",
            "His congressional career contributed to the gradual erosion of Federalist dominance in Vermont — the slow Democratic-Republican gains that eventually made Vermont more competitive as the Federalist Party collapsed nationally",
            "His brief Senate service contributed Vermont's perspective to the immediate post-War of 1812 reconstruction of national policy — the Era of Good Feelings transition period",
            "His career illustrated the Democratic-Republican minority position in Federalist New England — the small but persistent Jeffersonian presence even in the most commercially oriented states that eventually grew into the Jacksonian movement"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1805–1809"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1817–1818"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Democratic-Republican politician in Federalist Vermont"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian in Federalist New England"},
            {"target": "embargo-act-1807", "verb": "SERVES_DURING", "note": "Congressman during the Jefferson Embargo controversy"}
        ]
    }),

    ("mariano-egaña", {
        "summary": (
            "Mariano Egaña (1793–1846) was "
            "a Chilean jurist, statesman, "
            "and constitutional theorist "
            "who was the principal drafter "
            "of the Chilean Constitution "
            "of 1833 — the conservative "
            "constitution that provided "
            "Chile with the political "
            "stability that made it the "
            "most successfully governed "
            "republic in nineteenth-century "
            "Latin America. The 1833 "
            "Constitution, which concentrated "
            "executive power in a strong "
            "president while establishing "
            "representative institutions, "
            "remained in effect until "
            "1925 — ninety-two years "
            "— an extraordinary longevity "
            "for a Latin American "
            "constitutional document.\n\n"
            "Egaña was the son of Juan "
            "Egaña — one of the founders "
            "of Chilean independence — "
            "and had been educated in "
            "Spain before returning to "
            "Chile during the independence "
            "process. He served in "
            "multiple high offices "
            "including as Minister of "
            "Justice and Foreign Affairs.\n\n"
            "The 1833 Constitution "
            "reflected Egaña's conservative "
            "constitutionalism — his "
            "belief that strong executive "
            "authority, Catholicism "
            "as state religion, and "
            "limited suffrage were "
            "necessary for political "
            "stability in the chaotic "
            "post-independence conditions "
            "of Latin America.\n\n"
            "He is a foundational "
            "figure in Chilean legal "
            "and constitutional history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Principal drafter of the Chilean Constitution of 1833 — the conservative charter that gave Chile ninety-two years of constitutional stability (1833–1925) and made it the best-governed republic in nineteenth-century Latin America; son of independence founder Juan Egaña; Minister of Justice and Foreign Affairs; foundational figure in Chilean constitutional history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Chile's post-independence political instability — the chaotic years of competing liberal and conservative political projects, military coups, and factional violence that plagued early Chilean republicanism — created the political demand for the stable constitutional order that Egaña's 1833 Constitution provided",
            "The conservative triumph of 1830 — the military victory of the conservative pelucón faction led by Diego Portales over the liberal pipiolo faction — created the political conditions for the conservative constitutional project that Egaña led",
            "Egaña's legal training and constitutional theory — his Spanish legal education, his reading of conservative European constitutional thought, and his analysis of the failures of liberal Latin American constitutions — provided the intellectual framework for his conservative constitutional design"
        ],
        "effects": [
            "The Chilean Constitution of 1833 — which concentrated executive power in a president elected for five-year renewable terms, established Catholicism as state religion, limited suffrage to literate property-owners, and created a professional judiciary — provided Chile with ninety-two years of constitutional stability unmatched in Latin America",
            "The 1833 Constitution's success made Chile the model of Latin American constitutionalism — the proof that conservative constitutional design could create stable republican governance, in contrast to the liberal constitutions' repeated failures elsewhere in the region",
            "His Ministry of Justice work contributed to the development of Chilean law — including work toward the civil code that would eventually be completed by Andrés Bello — building the legal infrastructure for Chile's stable governance",
            "His conservative constitutionalism influenced subsequent Latin American constitutional thought — the argument for strong executive power and limited democracy as prerequisites for stable governance that influenced constitutional debates across the region"
        ],
        "relationships": [
            {"target": "chilean-constitution-1833", "verb": "DRAFTS", "note": "Principal drafter of the foundational Chilean constitution"},
            {"target": "chile", "verb": "SERVES_AS_MINISTER", "note": "Minister of Justice and Foreign Affairs"},
            {"target": "juan-egaña", "verb": "SON_OF", "note": "Son of Chilean independence founder Juan Egaña"},
            {"target": "diego-portales", "verb": "SERVES_UNDER", "note": "Conservative constitutionalist under Portales's political project"},
            {"target": "latin-american-constitutionalism", "verb": "INFLUENCES", "note": "Model of conservative constitutional design for the region"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 66 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
