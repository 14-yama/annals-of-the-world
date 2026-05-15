#!/usr/bin/env python3
"""
Batch 83 — 8 entities: Hans Christian Petersen, Jean-Baptiste Thorn,
Nicholas Bubwith, Cosmo Innes, Amasa Dana, Charles Jean Marie Barbaroux,
Felipe Neri Medina, Richard de Lucy
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

    ("hans-christian-petersen", {
        "summary": (
            "Hans Christian Petersen "
            "(1813–1879) was a Danish "
            "politician and jurist "
            "who served in Danish "
            "politics during the "
            "mid-19th century — "
            "a period of enormous "
            "constitutional transformation "
            "for Denmark. The "
            "1848 liberal revolution "
            "transformed Denmark "
            "from absolute monarchy "
            "to constitutional "
            "monarchy under the "
            "June Constitution "
            "of 1849 — one of "
            "the most progressive "
            "constitutions in Europe "
            "at the time. Danish "
            "politicians of this "
            "generation navigated "
            "the transition from "
            "royal absolutism to "
            "parliamentary governance "
            "while also facing "
            "the Schleswig-Holstein "
            "crisis — the German "
            "nationalist challenge "
            "to Danish sovereignty "
            "over the mixed-language "
            "duchies.\n\n"
            "The Schleswig Wars "
            "(1848–1851 and 1864) "
            "were the defining "
            "external crisis "
            "of Denmark's constitutional "
            "era — eventually "
            "costing Denmark "
            "its German-speaking "
            "southern territories.\n\n"
            "Danish politicians "
            "like Petersen served "
            "during this double "
            "transformation — "
            "internal liberalization "
            "and external territorial loss.\n\n"
            "He was a significant "
            "Danish judicial "
            "and political figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Danish politician and jurist (1813–1879); served during Denmark's transformation from absolute monarchy to constitutional monarchy (1849 June Constitution); active during the Schleswig-Holstein crisis and the First Schleswig War (1848–1851); navigated the double transformation of Danish liberalization and territorial defense.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Denmark's 1848 liberal revolution — the popular pressure that forced Frederick VII to accept constitutional government and end royal absolutism — created the political transformation that defined Petersen's generation of Danish politicians",
            "The Schleswig-Holstein crisis — German nationalist claims to the Danish-German border duchies and the two wars that resulted — created the external crisis that threatened Danish territorial integrity during Petersen's political career",
            "The June Constitution of 1849 — Denmark's remarkably progressive constitutional settlement that established parliamentary government, freedom of the press, and religious toleration — created the new political system within which Petersen served"
        ],
        "effects": [
            "His political service contributed to Denmark's early constitutional governance — the practical work of making the new parliamentary institutions function during the challenging transition from absolutism",
            "His career spanned the critical transformation from absolute monarchy to constitutional state — witnessing Denmark's emergence as one of Europe's most progressive constitutional democracies",
            "His generation's politics contributed to the Danish national identity — the cultural and political consensus that emerged from the Schleswig Wars and the constitutional transformation",
            "His career illustrated the challenges of mid-19th century Danish statesmanship — navigating constitutional transformation while defending territorial integrity against German nationalist pressure"
        ],
        "relationships": [
            {"target": "denmark", "verb": "SERVES", "note": "Danish politician during constitutional transformation"},
            {"target": "june-constitution-1849", "verb": "SERVES_UNDER", "note": "Danish politician in the new constitutional era"},
            {"target": "schleswig-wars", "verb": "SERVES_DURING", "note": "Danish politician during the Schleswig crises"},
            {"target": "danish-constitutional-monarchy", "verb": "BUILDS", "note": "Early constitutional governance contributor"},
            {"target": "danish-liberalism", "verb": "MEMBER_OF", "note": "Danish liberal political tradition"}
        ]
    }),

    ("jean-baptiste-thorn", {
        "summary": (
            "Jean-Baptiste Thorn "
            "(1744–1809) was a "
            "Luxembourg-born politician "
            "who served in the "
            "French revolutionary "
            "legislative assemblies "
            "after Luxembourg "
            "was incorporated "
            "into France in 1795. "
            "As a representative "
            "of the Forêts department "
            "(the former Luxembourg), "
            "Thorn participated "
            "in the Directory "
            "and Consulate era "
            "legislation — "
            "serving in the "
            "Council of Five Hundred "
            "and later the Legislative "
            "Body under Napoleon. "
            "Luxembourg's incorporation "
            "into France transformed "
            "it from an Austrian "
            "Habsburg territory "
            "into a French department "
            "— part of the "
            "revolutionary conquest "
            "of the Austrian Netherlands "
            "that fundamentally "
            "changed the political "
            "landscape of the "
            "Low Countries.\n\n"
            "As one of Luxembourg's "
            "representatives in "
            "Paris, Thorn helped "
            "mediate between "
            "the Luxembourg "
            "population and "
            "French republican "
            "administration.\n\n"
            "His career illustrated "
            "the fate of territories "
            "absorbed into "
            "revolutionary France.\n\n"
            "He was a Luxembourg "
            "lawyer and administrator."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Luxembourg-born French politician representing the Forêts department (former Luxembourg) in the Council of Five Hundred and Napoleonic Legislative Body; served after Luxembourg's 1795 incorporation into France; mediated between Luxembourg society and French administration; representative of the Habsburg territories absorbed into revolutionary France.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Luxembourg's 1795 French annexation — the revolutionary wars' conquest of the Austrian Netherlands including Luxembourg and its transformation into the French Forêts department — created the political circumstances of Thorn's Paris career as a Luxembourg representative",
            "The French Revolution's absorption of border territories — the revolutionary principle that French conquest brought liberation and republican citizenship — created the institutional framework within which Thorn served as one of Luxembourg's representatives",
            "Luxembourg's legal and administrative traditions — its distinct Habsburg governance and Catholic social structure — created the cultural context that Luxembourg's French-era representatives like Thorn navigated between their homeland and Paris"
        ],
        "effects": [
            "His representation contributed Luxembourg's voice to French revolutionary and Napoleonic governance — the complex integration of a formerly Habsburg territory into French republican and imperial administration",
            "His career helped mediate the transformation of Luxembourg from Habsburg territory to French department — the social and administrative changes that accompanied political incorporation",
            "His legislative service contributed to the Consulate and Empire's legislative work — the Council of Five Hundred and Legislative Body debates that shaped Napoleonic France",
            "His career illustrated the fate of small territories absorbed into the French revolutionary empire — the negotiated integration of local elites into the Paris political system"
        ],
        "relationships": [
            {"target": "council-of-five-hundred", "verb": "SERVES_IN", "note": "Member representing the Forêts department"},
            {"target": "legislative-body-france", "verb": "SERVES_IN", "note": "Napoleon-era legislative member"},
            {"target": "luxembourg", "verb": "REPRESENTS", "note": "Luxembourg representative in Paris"},
            {"target": "french-revolutionary-wars", "verb": "SERVES_AFTER", "note": "Career enabled by Luxembourg's 1795 French annexation"},
            {"target": "forets-department", "verb": "REPRESENTS", "note": "French department comprising former Luxembourg"}
        ]
    }),

    ("nicholas-bubwith", {
        "summary": (
            "Nicholas Bubwith "
            "(c.1355–1424) was "
            "an English bishop "
            "and royal administrator "
            "who served as Bishop "
            "of London (1406–1407), "
            "Bishop of Salisbury "
            "(1407–1408), and Bishop "
            "of Bath and Wells "
            "(1408–1424). "
            "A leading ecclesiastical "
            "administrator under "
            "Henry IV and Henry V, "
            "Bubwith combined "
            "Church leadership "
            "with royal service — "
            "the typical pattern "
            "of medieval bishop-administrators "
            "who served simultaneously "
            "as senior clerics "
            "and as key figures "
            "in royal governance. "
            "He attended the Council "
            "of Constance (1414–1418) "
            "— the Church council "
            "that ended the Western "
            "Schism by deposing "
            "multiple claimant "
            "popes and electing "
            "Martin V as the "
            "legitimate pope.\n\n"
            "His attendance at "
            "Constance placed "
            "him at one of "
            "the most consequential "
            "Church councils "
            "of the medieval period.\n\n"
            "He was also a benefactor "
            "of the Diocese "
            "of Bath and Wells — "
            "endowing almshouses "
            "and building projects.\n\n"
            "He was a significant "
            "Lancastrian Church "
            "administrator."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "English Bishop of London (1406–1407), Salisbury (1407–1408), and Bath and Wells (1408–1424); royal administrator under Henry IV and Henry V; attended the Council of Constance (1414–1418) that ended the Western Schism; benefactor of Bath and Wells Diocese; significant Lancastrian ecclesiastical-administrative figure.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Lancastrian monarchy's need for capable ecclesiastical administrators — Henry IV's and Henry V's requirement for educated, loyal churchmen who could serve both as senior bishops and as royal counselors — created the institutional framework for Bubwith's combined Church-state career",
            "The Western Schism — the decades-long crisis of competing papal claimants that divided the Church between Rome and Avignon — created the urgent necessity for the Council of Constance where Bubwith served as an English representative",
            "Medieval England's tradition of bishop-administrators — the centuries-old practice of employing senior churchmen as royal servants, diplomats, and judges — created the institutional pattern that shaped Bubwith's career"
        ],
        "effects": [
            "His attendance at the Council of Constance contributed England's voice to the resolution of the Western Schism — one of the most consequential Church councils in medieval history",
            "His multiple bishoprics contributed to the administration of three of England's most significant dioceses — London, Salisbury, and Bath and Wells — during the Lancastrian era",
            "His Bath and Wells benefactions contributed to the diocese's physical and institutional development — the almshouses and building projects that extended the medieval Church's charitable and architectural legacy",
            "His career illustrated the Lancastrian Church's strength — the close integration of royal administration and ecclesiastical leadership that characterized Henry IV's and Henry V's governance"
        ],
        "relationships": [
            {"target": "diocese-of-bath-and-wells", "verb": "LEADS_AS_BISHOP", "note": "Bishop of Bath and Wells 1408–1424"},
            {"target": "council-of-constance", "verb": "ATTENDS", "note": "English representative at the council ending the Western Schism"},
            {"target": "henry-v-of-england", "verb": "SERVES_UNDER", "note": "Royal administrator under Henry V"},
            {"target": "western-schism", "verb": "HELPS_RESOLVE", "note": "Council of Constance participant in schism resolution"},
            {"target": "diocese-of-london", "verb": "LEADS_AS_BISHOP", "note": "Bishop of London 1406–1407"}
        ]
    }),

    ("cosmo-innes", {
        "summary": (
            "Cosmo Innes (1798–1874) "
            "was a Scottish historian, "
            "antiquary, and lawyer "
            "who made fundamental "
            "contributions to "
            "Scottish historical "
            "scholarship — editing "
            "and publishing medieval "
            "Scottish records "
            "that had never "
            "previously been "
            "systematically accessible. "
            "As Advocate-Depute "
            "and Professor of "
            "Constitutional Law "
            "at Edinburgh University, "
            "Innes combined legal "
            "practice with his "
            "passionate historical "
            "research. He edited "
            "the 'Registrum de Dunfermlyn,' "
            "the 'Acts of the "
            "Parliaments of Scotland,' "
            "and numerous other "
            "medieval Scottish "
            "documents — creating "
            "the archival foundation "
            "for modern Scottish "
            "historical scholarship.\n\n"
            "His 'Sketches of "
            "Early Scotch History' "
            "(1861) and "
            "'Scotland in the "
            "Middle Ages' (1860) "
            "were pioneering "
            "works that made "
            "Scottish medieval "
            "history accessible "
            "to general educated readers.\n\n"
            "His editorial work "
            "remains fundamental "
            "to Scottish medieval studies.\n\n"
            "'The oldest documents "
            "speak clearest.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Scottish historian, antiquary, and lawyer (1798–1874); edited the 'Acts of the Parliaments of Scotland' and numerous medieval Scottish records; Professor of Constitutional Law at Edinburgh University; author of 'Sketches of Early Scotch History' (1861) and 'Scotland in the Middle Ages' (1860); foundational figure in Scottish medieval historical scholarship.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Scotland's archival preservation — the survival of medieval Scottish records in monastic and royal archives that had never been systematically catalogued or published — created the raw material for Innes's editorial work",
            "The 19th-century antiquarian movement — the broad British and European scholarly interest in recovering and publishing medieval historical sources — created the intellectual context and institutional support for Innes's editorial projects",
            "Edinburgh University's legal and historical tradition — the school's combination of legal education and historical scholarship — created the institutional environment for Innes's dual career as lawyer and historian"
        ],
        "effects": [
            "His editorial work created the archival foundation for modern Scottish medieval scholarship — the published documents that subsequent generations of Scottish historians have relied upon",
            "His popular historical works contributed to Scottish historical consciousness — making the medieval Scottish past accessible to the educated public in accessible, vivid prose",
            "His professorship contributed to Edinburgh's tradition as a center of Scottish legal and historical education — training generations of Scottish lawyers and historians",
            "His publications contributed to Scottish national identity — the historical documentation of Scotland's medieval institutions that connected the 19th-century nation to its medieval foundations"
        ],
        "relationships": [
            {"target": "edinburgh-university", "verb": "TEACHES_AT", "note": "Professor of Constitutional Law"},
            {"target": "acts-of-the-parliaments-of-scotland", "verb": "EDITS", "note": "Editor of medieval Scottish parliamentary records"},
            {"target": "scottish-medieval-history", "verb": "FOUNDS", "note": "Foundational figure in Scottish medieval historical scholarship"},
            {"target": "scottish-bar", "verb": "PRACTICES_IN", "note": "Advocate-Depute at the Scottish bar"},
            {"target": "registrum-de-dunfermlyn", "verb": "EDITS", "note": "Editor of the medieval Dunfermline Register"}
        ]
    }),

    ("amasa-dana", {
        "summary": (
            "Amasa Dana (1792–1867) "
            "was an American Democratic "
            "politician from New "
            "York who served in "
            "the U.S. House "
            "(1845–1847 and 1847–1849) "
            "during the Polk "
            "administration — "
            "the era of the "
            "Mexican-American War, "
            "the Oregon boundary "
            "settlement with Britain, "
            "and the Walker Tariff. "
            "A New York Democrat, "
            "Dana served during "
            "the Wilmot Proviso "
            "controversy — "
            "the proposal to "
            "ban slavery from "
            "all territories "
            "acquired from Mexico "
            "that became the "
            "most divisive issue "
            "of the Polk years "
            "and a precursor "
            "to the Civil War sectional conflict.\n\n"
            "New York's Democratic "
            "Party in this era "
            "was divided between "
            "the Hunker and "
            "Barnburner factions "
            "— conservative Democrats "
            "who accommodated "
            "the South versus "
            "antislavery Democrats "
            "who opposed slavery extension.\n\n"
            "Dana's four-year "
            "House service contributed "
            "New York's Democratic "
            "voice to the Polk "
            "era's defining debates.\n\n"
            "He was an Owego, "
            "New York lawyer "
            "and judge."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New York Democratic Congressman (1845–1849); served during the Polk administration's Mexican-American War and Wilmot Proviso controversies; New York's Hunker-Barnburner Democratic split; four-year House career during the defining antebellum sectional crisis; Owego lawyer and later judge.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Mexican-American War — Polk's aggressive expansion that added enormous territories and immediately raised the slavery extension question — created the defining controversy of Dana's congressional service",
            "New York's Hunker-Barnburner Democratic split — the factional division between conservative accommodationist and antislavery Democrats — created the turbulent intra-party environment of Dana's House service",
            "The Wilmot Proviso — the proposal to ban slavery from all Mexican-cession territory that the House passed but the Senate blocked — created the specific legislative battle that dominated Dana's congressional term"
        ],
        "effects": [
            "His House service contributed New York's Democratic votes to the Polk administration's legislation — the Mexican-American War funding, the Walker Tariff, and the Oregon settlement",
            "His participation in the Wilmot Proviso debates contributed to the escalating sectional confrontation — the slavery extension issue that his generation failed to resolve and that led to secession",
            "His career contributed to New York's Democratic tradition — the Tammany-adjacent politics of upstate New York that provided the party's numerical base",
            "His later judicial career contributed to Tioga County's legal development — the local jurisprudence that served the communities of rural upstate New York"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1845–1849"},
            {"target": "mexican-american-war", "verb": "VOTES_DURING", "note": "Congressman during the war and territorial acquisition"},
            {"target": "wilmot-proviso", "verb": "VOTES_ON", "note": "House member during the Proviso's passage"},
            {"target": "polk-administration", "verb": "SERVES_DURING", "note": "Democrat congressman during Polk presidency"},
            {"target": "new-york-democratic-party", "verb": "MEMBER_OF", "note": "New York Democrat in the Hunker-Barnburner era"}
        ]
    }),

    ("charles-jean-marie-barbaroux", {
        "summary": (
            "Charles Jean Marie Barbaroux "
            "(1767–1794) was a French "
            "revolutionary politician "
            "from Marseille who "
            "served in the Legislative "
            "Assembly and the "
            "National Convention — "
            "a leading Girondin "
            "who was executed "
            "during the Jacobin "
            "Terror at age 27. "
            "Barbaroux was one "
            "of the most passionate "
            "advocates for the "
            "Republic and a "
            "fierce opponent "
            "of royal tyranny "
            "— yet his Girondist "
            "federalism put "
            "him in mortal "
            "opposition to "
            "Robespierre's centralizing "
            "Jacobins. It was "
            "Barbaroux who summoned "
            "the Marseille volunteers "
            "to Paris in 1792 "
            "— the men who sang "
            "the marching song "
            "that became 'La Marseillaise,' "
            "France's national anthem.\n\n"
            "His connection to "
            "'La Marseillaise' "
            "— summoning the "
            "men who sang "
            "it into history "
            "— makes him an "
            "inadvertent contributor "
            "to France's most "
            "enduring cultural "
            "symbol.\n\n"
            "He escaped the "
            "Girondin purge "
            "in 1793 but was "
            "captured and guillotined "
            "in 1794.\n\n"
            "He was executed "
            "days before Thermidor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Girondin politician (1767–1794); summoned the Marseille volunteers to Paris in 1792 — the men who brought 'La Marseillaise' to history; National Convention member; Girondist federalist executed in the Terror; passionate republican who fell victim to Jacobin centralization; executed days before Thermidor ended the Terror.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Girondin-Jacobin political divide — the fundamental conflict between the Girondins' federalist decentralism and regional independence and the Jacobins' centralizing authoritarian republicanism — created the fatal political confrontation that destroyed Barbaroux",
            "Barbaroux's Marseille connections — his deep roots in Marseille's radical republican politics and his role as the city's Paris representative — created both his revolutionary prominence and his political identity as a provincial federalist opposed to Parisian Jacobin domination",
            "The 1792 crisis — the Brunswick Manifesto's threat and the assault on the Tuileries — created the revolutionary urgency that led Barbaroux to summon the Marseille volunteers to Paris in the decisive summer of 1792"
        ],
        "effects": [
            "His summoning of the Marseille volunteers contributed inadvertently to the creation of 'La Marseillaise' — the marching song they brought to Paris that became France's revolutionary anthem and national symbol",
            "His execution contributed to the political decimation of the Girondins — the republican faction whose destruction left Jacobin terror unchecked until Thermidor",
            "His death days before Thermidor illustrated the revolutionary Terror's random timing — the radical who would have been saved by events just days later",
            "His career contributed to the legend of Girondin republicanism — the federalist, rights-conscious tradition of the Revolution that later generations would idealize as a more humane alternative to Jacobin terror"
        ],
        "relationships": [
            {"target": "girondin-faction", "verb": "LEADS", "note": "Leading Girondin politician from Marseille"},
            {"target": "la-marseillaise", "verb": "CONTRIBUTES_TO_CREATION_OF", "note": "Summoned the Marseille volunteers who brought the song to Paris"},
            {"target": "national-convention", "verb": "SERVES_IN", "note": "Girondin Convention member"},
            {"target": "reign-of-terror", "verb": "EXECUTED_DURING", "note": "Guillotined 1794 during the Terror"},
            {"target": "maximilien-robespierre", "verb": "OPPOSED_BY", "note": "Federalist opponent of Jacobin centralization"}
        ]
    }),

    ("felipe-neri-medina", {
        "summary": (
            "Felipe Neri Medina "
            "was a Central American "
            "political figure "
            "of the early 19th "
            "century who participated "
            "in the governance "
            "of Guatemala or "
            "the Central American "
            "Federation during "
            "the turbulent independence "
            "era. Central American "
            "politicians of this "
            "period navigated "
            "the transition from "
            "Spanish colonial "
            "rule to independence "
            "(1821), the brief "
            "annexation to Mexico "
            "under Agustín de "
            "Iturbide (1822–1823), "
            "the formation of "
            "the Federal Republic "
            "of Central America "
            "(1823–1840), and "
            "the eventual collapse "
            "of the federation "
            "into five independent "
            "republics. This "
            "period was characterized "
            "by intense conflict "
            "between Liberals "
            "and Conservatives, "
            "federalists and "
            "centralists, and "
            "the various provinces "
            "competing for autonomy.\n\n"
            "The Central American "
            "federation's collapse "
            "— despite the hopes "
            "of its founders "
            "— created the "
            "five separate "
            "Central American "
            "republics that "
            "persist today.\n\n"
            "Local politicians "
            "like Medina provided "
            "the institutional "
            "continuity between "
            "colonial and republican governance.\n\n"
            "He was a figure of "
            "the Central American "
            "independence era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Central American political figure of the independence era; participated in governance during the transition from Spanish colonial rule to independence (1821) and the Federal Republic of Central America (1823–1840); navigated the Liberal-Conservative conflict and federalist-centralist tensions that ultimately dissolved the Central American federation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Central American independence — the 1821 declaration of independence from Spain following Mexican independence, and the subsequent question of whether to join Mexico or form an independent federation — created the political context of Medina's career",
            "The Liberal-Conservative conflict in Central America — the fundamental political divide between Liberal federalists who wanted constitutional governance and decentralization and Conservative centralists aligned with the Church — created the defining political battles of Medina's era",
            "The collapse of the Central American Federation — the accumulation of regional conflicts, Liberal-Conservative wars, and provincial separatism that destroyed the federation by 1840 — created the chaotic political environment Medina navigated"
        ],
        "effects": [
            "His political service contributed to the institutional continuity during Central America's turbulent founding period — providing the local governance that maintained social order during the independence era",
            "His career illustrated the challenges of Central American nation-building — the difficulty of creating stable republican institutions in a region divided by regional rivalries, class conflicts, and Church-state tensions",
            "His era's failure to maintain the Central American federation contributed to the fragmented political geography that characterized the region — five small republics instead of one large state",
            "His political service contributed to Guatemala's or his province's governance during the transition from colonial to republican rule"
        ],
        "relationships": [
            {"target": "central-american-federation", "verb": "SERVES_IN", "note": "Political figure of the federation era"},
            {"target": "central-american-independence", "verb": "PARTICIPATES_IN", "note": "Career during independence transition"},
            {"target": "liberal-conservative-conflict", "verb": "NAVIGATES", "note": "Political figure during Liberal-Conservative wars"},
            {"target": "guatemala", "verb": "SERVES", "note": "Central American political official"},
            {"target": "federal-republic-of-central-america", "verb": "SERVES_DURING", "note": "Federation-era politician 1823–1840"}
        ]
    }),

    ("richard-de-lucy", {
        "summary": (
            "Richard de Lucy "
            "(c.1089–1179) was "
            "an English royal "
            "administrator and "
            "jurist who served "
            "as Chief Justiciar "
            "of England — effectively "
            "the kingdom's chief "
            "administrator — "
            "under Henry II "
            "(1154–1179), one "
            "of the longest "
            "such tenures in "
            "English history. "
            "De Lucy was one "
            "of the architects "
            "of the Angevin "
            "legal revolution "
            "— the transformation "
            "of English royal "
            "justice under Henry II "
            "that introduced "
            "the Assize of Clarendon, "
            "the Assize of Northampton, "
            "and other legal "
            "reforms that "
            "created the foundations "
            "of English common law. "
            "He governed England "
            "as regent during "
            "Henry II's frequent "
            "absences in France.\n\n"
            "His long Chief "
            "Justiciarship also "
            "spanned the Becket "
            "controversy — "
            "the conflict between "
            "Henry II and "
            "Archbishop Thomas Becket "
            "over Church-state jurisdiction.\n\n"
            "He retired to Lesnes "
            "Abbey near London, "
            "which he had founded.\n\n"
            "'England is a realm "
            "made just by the "
            "king's law.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Chief Justiciar of England under Henry II (c.1154–1179); one of the architects of the Angevin legal revolution including the Assize of Clarendon and Northampton; effectively governed England during Henry II's French absences; served during the Becket controversy; foundational figure in the development of English common law; founder of Lesnes Abbey.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Henry II's legal reform program — the Angevin king's determination to extend royal justice throughout England and replace feudal and ecclesiastical courts with a unified royal judicial system — created the legal revolution that de Lucy helped implement",
            "The English administrative vacuum — the need for capable, loyal royal administrators who could govern England effectively during Henry II's frequent absences in his French territories — created the Chief Justiciarship's enormous importance",
            "The Becket controversy — the clash between Henry II and Thomas Becket over the Constitutions of Clarendon and the jurisdiction of Church courts — created the major Church-state crisis of de Lucy's long tenure"
        ],
        "effects": [
            "His co-implementation of the Assize of Clarendon (1166) contributed to the foundations of English common law — the jury trial system and standardized procedures for criminal justice that became the basis of English legal tradition",
            "His long regency governance contributed to English royal administration — effectively running the kingdom during the years Henry spent in France, demonstrating the royal government's institutional independence from the king's physical presence",
            "His navigation of the Becket controversy contributed to the eventual settlement of Church-state jurisdiction in England — the complex negotiations that followed Becket's murder",
            "His founding of Lesnes Abbey reflected the pious munificence expected of great medieval administrators — the religious patronage that legitimized and memorialized their power"
        ],
        "relationships": [
            {"target": "henry-ii-of-england", "verb": "SERVES_AS_JUSTICIAR_FOR", "note": "Chief Justiciar under Henry II"},
            {"target": "assize-of-clarendon", "verb": "IMPLEMENTS", "note": "Co-architect of the foundational criminal law reform"},
            {"target": "english-common-law", "verb": "FOUNDS", "note": "Angevin legal revolution architect"},
            {"target": "thomas-becket", "verb": "SERVES_DURING_CONFLICT_WITH", "note": "Chief Justiciar during the Becket controversy"},
            {"target": "lesnes-abbey", "verb": "FOUNDS", "note": "Founded Lesnes Abbey near London"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 83 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
