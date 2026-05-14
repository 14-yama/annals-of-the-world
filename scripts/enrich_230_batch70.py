#!/usr/bin/env python3
"""
Batch 70 — 8 entities: Archibald Henderson, Benjamin Hardin,
José de la Torre Ugarte y Alarcón, Louis Michel le Peletier Marquis de Saint-Fargeau,
William Bradford, Henry Woods, Jean-Marc Mousson, John Rutherfurd
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

    ("archibald-henderson", {
        "summary": (
            "Archibald Henderson (1783–1859) "
            "was an American military officer "
            "who served as Commandant of "
            "the United States Marine Corps "
            "for an extraordinary 38 years "
            "(1820–1859) — the longest "
            "tenure in Marine Corps history, "
            "earning him the nickname "
            "'Grand Old Man of the Marine "
            "Corps.' His tenure transformed "
            "the Marines from a marginal "
            "naval adjunct into a "
            "professional military force "
            "with a distinctive identity, "
            "doctrine, and esprit de corps.\n\n"
            "Henderson led the Marines "
            "through an extraordinary "
            "range of conflicts — the "
            "Second Seminole War (1835–1842), "
            "the Mexican-American War "
            "(1846–1848), and numerous "
            "other expeditions — personally "
            "leading a Marine brigade "
            "in the Seminole campaign "
            "and leaving a note on his "
            "office door reading 'Gone "
            "to Florida to fight the "
            "Indians; will be back when "
            "the war is over.'\n\n"
            "His 38-year commandancy "
            "spanned the presidencies "
            "from Monroe to Buchanan "
            "— a remarkable institutional "
            "continuity through the "
            "most politically turbulent "
            "era of the early republic.\n\n"
            "He established the Marine "
            "Corps' professional identity."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Longest-serving Commandant of the Marine Corps (1820–1859, 38 years); 'Grand Old Man of the Marine Corps'; personally led Marines in the Second Seminole War and Mexican-American War; transformed the Corps from a naval adjunct into a professional military force; spanned the presidencies of Monroe through Buchanan.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Marine Corps' institutional weakness in the early republic — its ambiguous status between the Army and Navy, its chronic underfunding, and the questions about its proper role — created the institutional challenge that Henderson's long commandancy addressed through sustained professional leadership",
            "The Second Seminole War (1835–1842) — the long, costly guerrilla conflict in Florida that required significant Marine ground forces — gave Henderson the opportunity to demonstrate the Corps' value as a ground-combat force and personally lead Marines in the field",
            "The Mexican-American War (1846–1848) — the conquest of Mexican territory that required Marine amphibious operations, the assault on Chapultepec, and the occupation of Mexico City — further demonstrated the Corps' military capability and established traditions that the Corps still honors"
        ],
        "effects": [
            "His 38-year commandancy transformed the Marine Corps from an organization of uncertain purpose and marginal status into a professional military institution with a distinctive culture, doctrine, and esprit de corps that persisted through the Civil War and beyond",
            "His personal leadership in combat — at Seminole campaigns and Mexican-American War operations — established the tradition of Marine Corps commandants as fighting leaders rather than purely administrative officers",
            "His institutional leadership created the Marine Corps' distinctive identity — the proud culture of professionalism and warrior ethos that made the Corps resistant to proposals for its abolition and gave it a unique place in American military life",
            "His tenure's extraordinary length created institutional continuity through the most politically volatile period in American history — maintaining the Corps' professionalism through presidential transitions, political crises, and budget battles"
        ],
        "relationships": [
            {"target": "united-states-marine-corps", "verb": "COMMANDS", "note": "Commandant 1820–1859 — longest in Corps history"},
            {"target": "second-seminole-war", "verb": "COMMANDS_DURING", "note": "Personally led Marine brigade in Florida"},
            {"target": "mexican-american-war", "verb": "COMMANDS_DURING", "note": "Marines under his command at Chapultepec"},
            {"target": "us-navy", "verb": "SERVES_IN", "note": "Marine Corps as naval service component"},
            {"target": "american-military-professionalization", "verb": "ADVANCES", "note": "Transformed Marines into a professional fighting force"}
        ]
    }),

    ("benjamin-hardin", {
        "summary": (
            "Benjamin Hardin (1784–1852) "
            "was an American Democratic-Republican "
            "and later Whig politician "
            "from Kentucky who served "
            "in the U.S. House of "
            "Representatives (1815–1823 "
            "and 1833–1837) and as "
            "Kentucky Secretary of State "
            "(1844–1847). One of Kentucky's "
            "most prominent antebellum "
            "lawyers and orators, Hardin "
            "was known as one of the "
            "best trial lawyers in "
            "the state — a reputation "
            "earned in the Kentucky "
            "courts alongside legal "
            "luminaries like Henry "
            "Clay and John J. Crittenden.\n\n"
            "Hardin's political career "
            "traced Kentucky's partisan "
            "evolution from Democratic-Republican "
            "to the National Republican "
            "and Whig tradition — "
            "the path followed by "
            "Kentucky's commercial "
            "and professional elite "
            "who supported Clay's "
            "American System of "
            "protective tariffs, "
            "a national bank, and "
            "internal improvements.\n\n"
            "Kentucky in this era "
            "was one of the most "
            "politically competitive "
            "states — the birthplace "
            "of both Henry Clay "
            "and Abraham Lincoln, "
            "and a critical swing "
            "state in antebellum "
            "presidential elections.\n\n"
            "He was a major figure "
            "in Kentucky law and politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky Whig Congressman (1815–1823 and 1833–1837) and Secretary of State; one of Kentucky's most prominent trial lawyers alongside Henry Clay and Crittenden; represented the Clay Whig tradition in a critical swing state; Kentucky law and political figure across the antebellum era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Kentucky's legal frontier culture — the state's rapid development from frontier territory into a major agricultural and commercial state that generated complex legal disputes requiring skilled lawyers — created the demand for the trial lawyering that made Hardin's reputation",
            "Henry Clay's political and cultural dominance of Kentucky — the state's identification with the American System, protective tariffs, national bank, and internal improvements that Clay championed — created the political framework for Hardin's Whig career",
            "Kentucky's political competitiveness — the state's roughly even balance between Democratic and Whig sentiment that made it a genuine swing state — created both the opportunities and challenges of Hardin's political career"
        ],
        "effects": [
            "His two House stints contributed Kentucky's Whig perspective to the major debates of the 1815–1823 and 1833–1837 periods — from the post-War of 1812 national development debates through the Nullification Crisis and Jacksonian economic policy fights",
            "His legal career contributed to Kentucky jurisprudence — the common law and equity decisions from Kentucky courts that helped develop the legal framework of the American West",
            "His Kentucky Secretary of State service contributed to state governance during the Polk era — managing the administrative functions of one of the most important border states during the Mexican-American War period",
            "His career alongside Clay, Crittenden, and other Kentucky legal-political luminaries contributed to the state's distinctive legal culture — the combination of Southern common law, frontier pragmatism, and Whig commercial progressivism"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Kentucky Congressman 1815–1823 and 1833–1837"},
            {"target": "henry-clay", "verb": "ASSOCIATES_WITH", "note": "Contemporary in Kentucky's Whig legal-political world"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Kentucky Whig in the Clay tradition"},
            {"target": "kentucky", "verb": "SERVES", "note": "Kentucky Secretary of State 1844–1847"},
            {"target": "american-system", "verb": "SUPPORTS", "note": "Whig supporter of Clay's economic program"}
        ]
    }),

    ("josé-de-la-torre-ugarte-y-alarcón", {
        "summary": (
            "José de la Torre Ugarte y "
            "Alarcón (1786–1831) was a "
            "Peruvian poet, lawyer, and "
            "patriot who wrote the lyrics "
            "to the national anthem of "
            "Peru — 'Himno Nacional del "
            "Perú' — upon independence. "
            "The anthem was composed "
            "in 1821 to a melody by "
            "José Bernardo Alcedo following "
            "San Martín's proclamation "
            "of Peruvian independence, "
            "and Torre Ugarte's words "
            "have been sung by Peruvians "
            "ever since as one of "
            "the most recognized "
            "national symbols of "
            "the republic.\n\n"
            "Torre Ugarte was a "
            "criollo intellectual "
            "and patriot — part "
            "of the educated "
            "colonial-born elite "
            "that embraced independence "
            "from Spain and sought "
            "to create a new "
            "Peruvian national "
            "identity distinct "
            "from the colonial past.\n\n"
            "San Martín's liberation "
            "of Lima (July 1821) "
            "created the immediate "
            "context for the anthem's "
            "composition — the new "
            "republic needed symbols "
            "of national identity "
            "to crystallize "
            "independence sentiment "
            "into patriotic loyalty.\n\n"
            "His anthem remains "
            "central to Peruvian identity."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Author of Peru's national anthem 'Himno Nacional del Perú' (1821); criollo patriot and poet who gave independent Peru one of its founding national symbols; worked with composer Bernardo Alcedo following San Martín's independence proclamation; his words have defined Peruvian national identity for two centuries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "San Martín's liberation of Lima and proclamation of Peruvian independence (July 28, 1821) — the military and political event that required the new republic to establish national symbols and institutions — created the immediate context for Torre Ugarte's anthem commission",
            "The criollo intellectual class's role in independence movements — the educated colonial-born elite who provided the ideological frameworks and cultural symbols for Latin American independence — created the social environment from which Torre Ugarte emerged as the anthem's author",
            "The Enlightenment's influence on Latin American independence ideology — the idea that new nations required founding documents, national symbols, and cultural expressions of distinctive identity — created the cultural imperative for a national anthem"
        ],
        "effects": [
            "His anthem lyrics created one of the most enduring national symbols of Peru — the words that have defined Peruvian national identity, been sung at national ceremonies, and expressed Peruvian patriotism for two centuries",
            "His work contributed to the cultural project of Peruvian national identity construction — the effort to create a distinctly Peruvian cultural identity that could unite criollos, mestizos, and indigenous peoples under a common national symbol",
            "The anthem's creation contributed to the legitimacy and emotional consolidation of Peruvian independence — giving the new republic a cultural symbol that could inspire loyalty and distinguish Peru from both Spain and other newly independent Latin American states",
            "His career illustrated the role of criollo intellectuals in Latin American independence — the lawyers, poets, and journalists whose cultural production helped give political independence its emotional and symbolic content"
        ],
        "relationships": [
            {"target": "peru", "verb": "CREATES_ANTHEM_OF", "note": "Wrote the words to Peru's national anthem"},
            {"target": "josé-de-san-martín", "verb": "SERVES_UNDER", "note": "Patriot serving under San Martín's independence proclamation"},
            {"target": "peruvian-independence", "verb": "CELEBRATES", "note": "Anthem written to mark independence in 1821"},
            {"target": "josé-bernardo-alcedo", "verb": "COLLABORATES_WITH", "note": "Lyricist for Alcedo's anthem melody"},
            {"target": "latin-american-independence", "verb": "PARTICIPATES_IN", "note": "Criollo patriot in the independence movement"}
        ]
    }),

    ("louis-michel-le-peletier-marquis-de-saint-fargeau", {
        "summary": (
            "Louis Michel le Peletier, "
            "Marquis de Saint-Fargeau "
            "(1760–1793) was a French "
            "aristocrat and revolutionary "
            "politician who voted for "
            "the execution of King Louis XVI "
            "and was assassinated the "
            "following day by a royalist "
            "guard — becoming one of "
            "the first martyrs of the "
            "French Revolution. His "
            "death on the eve of "
            "Louis XVI's execution "
            "(January 20, 1793) made "
            "him a revolutionary icon "
            "— the Convention voted "
            "to give him a state "
            "funeral in the Panthéon "
            "and his portrait was "
            "painted by Jacques-Louis "
            "David as a revolutionary "
            "martyr.\n\n"
            "Le Peletier's path from "
            "aristocrat to revolutionary "
            "— from Marquis to regicide "
            "— was representative of "
            "the small but significant "
            "group of French nobility "
            "who embraced the Revolution "
            "and used their aristocratic "
            "status to help destroy "
            "the system that had "
            "privileged them.\n\n"
            "He had also proposed "
            "a radical educational "
            "reform — a plan for "
            "universal state boarding "
            "schools that Robespierre "
            "later championed — that "
            "influenced revolutionary "
            "education theory.\n\n"
            "His martyrdom amplified "
            "the Revolution's emotional power."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French aristocrat-turned-revolutionary who voted for Louis XVI's execution and was assassinated the next day (January 20, 1793); became one of the Revolution's first martyrs; state funeral in the Panthéon; portrait by David; also proposed radical universal education reforms; emblematic of the nobility who embraced and enabled the Revolution.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radical phase — the Convention's vote to try and execute Louis XVI and the revolutionary transformation of French politics from constitutional monarchy to republic — created the political context for Le Peletier's vote and his assassination",
            "Le Peletier's own aristocratic radicalization — his rejection of his noble privilege in favor of revolutionary principles — made him one of the most dramatic examples of the noblesse libérale who embraced the Revolution against their own class interests",
            "The royalist reaction to the regicide vote — the rage of former royal guards and royalist sympathizers at the Convention members who voted for Louis XVI's execution — created the conditions for Le Peletier's assassination the night before the king's death"
        ],
        "effects": [
            "His assassination and martyrdom — dying the day before Louis XVI's execution — created one of the Revolution's most powerful symbolic moments and the first major martyr of the radical phase",
            "His Panthéon funeral and David's martyr portrait transformed Le Peletier into a revolutionary icon — a visual and symbolic representation of noble sacrifice for the revolutionary cause that the Convention used to consolidate support for the regicide",
            "His educational reform proposals — the plan for universal state boarding schools that Robespierre championed — contributed to the revolutionary tradition of radical educational reform that sought to create new republican citizens from birth",
            "His career trajectory from aristocrat to regicide to martyr illustrated one of the French Revolution's most compelling narratives — the self-destructive logic of noble radicalism that saw members of the privileged class helping to dismantle their own social order"
        ],
        "relationships": [
            {"target": "french-revolution", "verb": "MARTYRED_IN", "note": "First major martyr of the radical revolutionary phase"},
            {"target": "louis-xvi-france", "verb": "VOTES_FOR_EXECUTION_OF", "note": "Voted for regicide in the Convention"},
            {"target": "national-convention-france", "verb": "SERVES_IN", "note": "Convention member and revolutionary politician"},
            {"target": "jacques-louis-david", "verb": "PORTRAYED_BY", "note": "David painted him as a revolutionary martyr"},
            {"target": "pantheon-paris", "verb": "ENTOMBED_IN", "note": "Revolutionary state funeral in the Panthéon"}
        ]
    }),

    ("william-bradford", {
        "summary": (
            "William Bradford (1755–1795) "
            "was an American lawyer and "
            "jurist who served as the "
            "second Attorney General "
            "of the United States "
            "(1794–1795) under President "
            "Washington — appointed to "
            "succeed Edmund Randolph "
            "when Randolph became "
            "Secretary of State. Bradford "
            "served in one of the most "
            "legally complex periods "
            "of the early republic: "
            "the Jay Treaty controversy, "
            "the Whiskey Rebellion, "
            "and the question of "
            "American neutrality "
            "in the war between "
            "Revolutionary France "
            "and Britain.\n\n"
            "Bradford had previously "
            "served as Attorney General "
            "of Pennsylvania — "
            "the state's chief legal "
            "officer — and was "
            "one of the Philadelphia "
            "Bar's most respected "
            "members, part of the "
            "same legal world as "
            "James Wilson, James "
            "Iredell, and the other "
            "founding generation "
            "lawyers who built "
            "American constitutional "
            "law from the ground up.\n\n"
            "His death in office "
            "(1795) at age 40 "
            "cut short what would "
            "likely have been a "
            "distinguished career.\n\n"
            "He was a significant "
            "figure in early American "
            "constitutional development."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Second U.S. Attorney General (1794–1795) under Washington; served during the Whiskey Rebellion and Jay Treaty controversy; previously Pennsylvania Attorney General; part of the Philadelphia founding-generation legal circle; died at 40 in office — his premature death cut short a career that was shaping early American constitutional law.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Washington's need for a reliable Attorney General after Randolph's elevation to Secretary of State — the search for a lawyer of proven ability and Federalist sympathies to fill the constitutional officer role — led to Bradford's appointment from among Philadelphia's legal elite",
            "The Whiskey Rebellion (1794) — the armed uprising against the federal excise tax on whiskey in western Pennsylvania that Washington suppressed by calling out the militia — created the immediate legal and constitutional challenge of Bradford's early tenure",
            "The Jay Treaty controversy — Washington's determination to maintain American neutrality between Revolutionary France and Britain through a compromise commercial treaty with Britain — created the politically explosive legal and diplomatic context for Bradford's Attorney General work"
        ],
        "effects": [
            "His Attorney General service contributed to the legal framework of the early executive branch — providing constitutional advice on the Whiskey Rebellion's suppression, the Jay Treaty's legality, and other foundational questions of executive power",
            "His opinions on American neutrality law helped define the legal obligations of a neutral nation — the framework that Bradford and Randolph before him developed for managing American legal obligations in a world of European wars",
            "His death at 40 created a vacancy in one of the executive branch's most important constitutional advisory roles during a critical period — requiring Washington to find another replacement just as the Jay Treaty controversy was reaching its peak",
            "His career contributed to the development of the Attorney General's institutional role — the early shaping of what would eventually become the Justice Department and the senior legal officer of the United States government"
        ],
        "relationships": [
            {"target": "us-department-of-justice", "verb": "LEADS", "note": "Second U.S. Attorney General 1794–1795"},
            {"target": "george-washington", "verb": "SERVES_UNDER", "note": "Washington's Attorney General appointment"},
            {"target": "whiskey-rebellion", "verb": "ADVISES_ON", "note": "Attorney General during 1794 uprising suppression"},
            {"target": "jay-treaty", "verb": "ADVISES_ON", "note": "AG providing legal counsel during treaty controversy"},
            {"target": "pennsylvania", "verb": "SERVES", "note": "Previously Pennsylvania Attorney General"}
        ]
    }),

    ("henry-woods", {
        "summary": (
            "Henry Woods (1764–1826) was "
            "an American politician from "
            "Pennsylvania who served in "
            "the U.S. House of Representatives "
            "(1799–1801) during the Adams "
            "administration's final years "
            "and the Jeffersonian Revolution "
            "of 1800. A Democratic-Republican "
            "from Pennsylvania, Woods "
            "was part of the majority "
            "coalition that defeated "
            "John Adams and the Federalists "
            "in the election of 1800 "
            "— one of the most consequential "
            "transfers of political power "
            "in American history.\n\n"
            "Pennsylvania in this "
            "era was one of the "
            "most politically "
            "important states — "
            "a large, diverse, "
            "religiously varied "
            "state with significant "
            "German-American and "
            "Scots-Irish populations "
            "whose Democratic-Republican "
            "sympathies made it "
            "critical to Jefferson's "
            "electoral coalition.\n\n"
            "His brief House tenure "
            "coincided with the "
            "Alien and Sedition Acts' "
            "passage and the "
            "Virginia and Kentucky "
            "Resolutions — the "
            "Democratic-Republican "
            "response that escalated "
            "partisan tensions "
            "toward the 1800 election.\n\n"
            "He was among the many "
            "one-term Pennsylvania "
            "representatives of "
            "the early republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Pennsylvania Democratic-Republican Congressman (1799–1801); part of the coalition that defeated Adams in 1800; served during the Alien and Sedition Acts controversy; one of Pennsylvania's many representatives in the early republic during the first party system's defining contest.",
            "significanceCategory": "local"
        },
        "causes": [
            "Pennsylvania's Democratic-Republican political culture — the state's diverse population of German-American farmers, Scots-Irish frontier settlers, and urban artisans whose sympathies lay with Jefferson's agrarian-republican ideology rather than the Federalists' commercial nationalism — created the constituency for Woods's election",
            "The Alien and Sedition Acts controversy — the Adams administration's press restrictions and alien deportation powers that Democratic-Republicans attacked as unconstitutional tyranny — created the political mobilization that drove the 1800 election",
            "Jefferson's broad coalition-building — the political organization that identified Democratic-Republican candidates across states to challenge Federalist incumbents — created the national electoral strategy within which Woods's campaign was part"
        ],
        "effects": [
            "His House service contributed Pennsylvania's Democratic-Republican votes to the final years of the Federalist era — opposing the Adams administration and contributing to the political coalition that produced the 1800 election sweep",
            "His participation in the 6th Congress's partisan battles contributed to the Democratic-Republican majority that made the transition to Jefferson's administration smoother",
            "His brief career illustrated the pattern of Pennsylvania's many one-term representatives — the state's large size and political diversity generating many congressional careers that reflected local political shifts rather than sustained national prominence",
            "His death in 1826 placed him among the revolutionary generation who witnessed the full arc from the republic's founding through the Era of Good Feelings and the onset of the Jacksonian transformation"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1799–1801"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Pennsylvania Democratic-Republican in the first party system"},
            {"target": "alien-and-sedition-acts", "verb": "OPPOSES", "note": "Democratic-Republican opposing the Adams measures"},
            {"target": "revolution-of-1800", "verb": "PARTICIPATES_IN", "note": "Part of the coalition that defeated Adams"},
            {"target": "pennsylvania", "verb": "REPRESENTS", "note": "Pennsylvania representative in the early republic"}
        ]
    }),

    ("jean-marc-mousson", {
        "summary": (
            "Jean-Marc Mousson (1780–1855) "
            "was a Swiss naturalist and "
            "zoologist from Zurich who "
            "made significant contributions "
            "to the study of mollusks "
            "(malacology) and the natural "
            "history of the eastern "
            "Mediterranean and Middle "
            "East. His major work was "
            "a comprehensive study of "
            "the land and freshwater "
            "mollusks of the Holy Land "
            "and Syria — a pioneering "
            "work of 19th-century "
            "natural history that "
            "documented species that "
            "had never been systematically "
            "described.\n\n"
            "Mousson worked within "
            "the 19th-century Swiss "
            "natural history tradition "
            "— Zurich's scientific "
            "community produced a "
            "remarkable generation "
            "of naturalists who "
            "contributed to the "
            "global cataloguing "
            "of natural species "
            "that characterized "
            "the scientific enterprise "
            "of the 1820s–1850s.\n\n"
            "His malacological work "
            "contributed specimens "
            "and systematic descriptions "
            "that were used by "
            "subsequent taxonomists "
            "in building the "
            "systematic classification "
            "of mollusks.\n\n"
            "He also studied "
            "the Canary Islands' "
            "land mollusks."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Swiss malacologist from Zurich (1780–1855); pioneering study of land and freshwater mollusks of the Holy Land and Syria; worked in the great 19th-century tradition of natural history species cataloguing; contributed systematic descriptions used by subsequent taxonomists; part of Zurich's distinguished natural history tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 19th-century natural history revolution — the systematic global effort to catalogue, describe, and classify the earth's biological species that dominated scientific activity from Linnaeus through Darwin — created the intellectual context for Mousson's malacological work",
            "European interest in the Holy Land's natural history — the combination of religious significance and scientific curiosity that made the eastern Mediterranean and Middle East a focus of 19th-century natural history expeditions — created the opportunity for Mousson's geographic specialization",
            "Zurich's scientific community — the Swiss natural history tradition of careful observation, systematic description, and specimen collection that produced a remarkable generation of naturalists in the early 19th century — provided Mousson's intellectual environment"
        ],
        "effects": [
            "His systematic descriptions of Holy Land and Syrian mollusks contributed to the taxonomic knowledge base that subsequent malacologists used in building the comprehensive classification of the world's mollusk species",
            "His work contributed to the natural history of the eastern Mediterranean region — an area of considerable scientific interest whose biodiversity was being documented for the first time by European naturalists in this period",
            "His specimen collections and descriptions contributed to the natural history museums of Europe — the collections that formed the basis of systematic biological research in the 19th century",
            "His career contributed to the Swiss natural history tradition — the Zurich scientific community's reputation for careful, systematic natural history work that placed Swiss science at the forefront of European natural history"
        ],
        "relationships": [
            {"target": "malacology", "verb": "ADVANCES", "note": "Systematic study of land and freshwater mollusks"},
            {"target": "holy-land-natural-history", "verb": "DOCUMENTS", "note": "Pioneer of eastern Mediterranean mollusk taxonomy"},
            {"target": "zurich", "verb": "WORKS_IN", "note": "Part of Zurich's 19th-century natural history tradition"},
            {"target": "19th-century-natural-history", "verb": "CONTRIBUTES_TO", "note": "Part of the global species cataloguing enterprise"},
            {"target": "canary-islands", "verb": "STUDIES", "note": "Also documented Canary Islands land mollusks"}
        ]
    }),

    ("john-rutherfurd", {
        "summary": (
            "John Rutherfurd (1760–1840) "
            "was an American Federalist "
            "politician from New Jersey "
            "who served as a U.S. Senator "
            "(1791–1798) during the first "
            "decade of the new constitutional "
            "government. A New Jersey "
            "Federalist, Rutherfurd "
            "supported the Hamiltonian "
            "financial program — the "
            "national bank, assumption "
            "of state debts, and protective "
            "commercial policy — that "
            "defined the early Federalist "
            "economic agenda.\n\n"
            "Rutherfurd's Senate service "
            "coincided with the most "
            "formative years of the "
            "new government — the "
            "establishment of the "
            "executive departments, "
            "the Hamiltonian financial "
            "system, the Jay Treaty "
            "controversy, the Whiskey "
            "Rebellion, and the "
            "opening of the "
            "Federalist-Democratic-Republican "
            "partisan conflict.\n\n"
            "New Jersey in this "
            "era was a Federalist "
            "stronghold — its "
            "commercial connections "
            "to New York and "
            "Philadelphia, its "
            "mixed farming and "
            "manufacturing economy, "
            "and its social structure "
            "of prosperous farmers "
            "and merchants aligned "
            "with Federalist policies.\n\n"
            "He was an important "
            "figure in New Jersey's "
            "Federalist establishment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Jersey Federalist U.S. Senator (1791–1798) during the republic's formative first decade; supported Hamilton's financial program; served through the Jay Treaty, Whiskey Rebellion, and onset of the first party system; part of New Jersey's Federalist establishment during the critical period of constitutional government's establishment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Constitution's ratification and the new federal government's establishment — the creation of the Senate as a new institution requiring members who would define its practices, procedures, and role in the constitutional system — created the opportunity for Rutherfurd's Senate service",
            "New Jersey's Federalist commercial culture — the state's commercial connections to New York and Philadelphia, its prosperous farming economy, and its merchant class whose interests aligned with Hamilton's commercial nationalism — provided the political support for Rutherfurd's Federalist Senate career",
            "Hamilton's financial program — the national bank, assumption of state debts, and funding of the national debt that created the framework for American commercial capitalism — created the major legislative agenda that Rutherfurd supported during his Senate tenure"
        ],
        "effects": [
            "His Senate service contributed New Jersey's Federalist votes to the formative legislation of the 1790s — Hamilton's financial acts, the Jay Treaty, and the other measures that shaped the new government's character",
            "His tenure as one of New Jersey's first senators contributed to the Senate's institutional development — the establishment of practices, procedures, and norms during the period when the Senate was defining its own constitutional role",
            "His career contributed to New Jersey's Federalist political tradition — the state's commercial elite's commitment to Hamiltonian economics that persisted through the Federalist era",
            "His Senate service during the Jay Treaty fight placed him at one of the most consequential constitutional and partisan moments of the early republic — the controversy that crystallized the Federalist-Democratic-Republican divide"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1791–1798"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New Jersey Federalist in the first party system"},
            {"target": "alexander-hamilton", "verb": "SUPPORTS", "note": "Senator supporting Hamilton's financial program"},
            {"target": "jay-treaty", "verb": "VOTES_ON", "note": "Senator during the Jay Treaty controversy"},
            {"target": "new-jersey", "verb": "REPRESENTS", "note": "New Jersey's Federalist senatorial representative"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 70 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
