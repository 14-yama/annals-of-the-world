#!/usr/bin/env python3
"""
Batch 76 — 8 entities: Isaac Tichenor, John C. Spencer, Joseph Bloomfield,
Gideon Granger, Jacques-Guillaume Thouret, John M. Berrien, Selah B. Strong,
François-Louis Bourdon
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

    ("isaac-tichenor", {
        "summary": (
            "Isaac Tichenor (1754–1838) "
            "was an American Federalist "
            "politician from Vermont "
            "who served as Governor "
            "of Vermont (1797–1807 and "
            "1808–1809) and as U.S. "
            "Senator (1796–1797 and "
            "1815–1821). One of "
            "Vermont's most durable "
            "political figures, "
            "Tichenor governed "
            "the state across "
            "a remarkable ten-year "
            "period spanning the "
            "Adams and Jefferson "
            "administrations — "
            "an era when Federalism "
            "was declining nationally "
            "but Vermont maintained "
            "significant Federalist "
            "support.\n\n"
            "His governorship "
            "covered the Jay Treaty "
            "controversy, the "
            "quasi-war with France, "
            "the XYZ Affair, "
            "the Alien and Sedition "
            "Acts, the Jefferson "
            "revolution of 1800, "
            "and the Embargo Act "
            "crisis — the most "
            "contentious political "
            "decade in the early "
            "republic's history.\n\n"
            "His second Senate "
            "term (1815–1821) "
            "came after the "
            "War of 1812 and "
            "during the Era "
            "of Good Feelings.\n\n"
            "He was nicknamed "
            "'Jersey Slick' for "
            "his political skills."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vermont Federalist Governor (1797–1807, 1808–1809) and Senator (1796–1797, 1815–1821); governed Vermont through the Adams-Jefferson political transition, the Embargo Act crisis, and the War of 1812 era; one of Vermont's most durable political figures; served during some of the most contentious decades in early American history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's distinctive Federalist tradition — the state's combination of New England Congregationalism, commercial interests, and the Standing Order's influence created significant Federalist support even as the party declined nationally",
            "The Adams-Jefferson political transition — the end of Federalist national dominance and the Jeffersonian revolution of 1800 — created the politically turbulent decade that Tichenor's long governorship navigated",
            "The Embargo Act crisis — Jefferson's economic warfare against Britain and France that was devastating to New England's commercial economy — created the defining controversy of Tichenor's late governorship and contributed to Vermont's resistance"
        ],
        "effects": [
            "His decade-long governorship contributed to Vermont's institutional development — ten years of consistent executive leadership across one of the most politically turbulent periods in early American history",
            "His resistance to the Embargo Act during his governorship contributed to the New England Federalist opposition that was one of the most significant challenges to Jeffersonian policy",
            "His career contributed to the durability of Vermont Federalism — the maintenance of Federalist politics in Vermont longer than in most other states, reflecting the state's distinctive political culture",
            "His two Senate terms contributed Vermont's voice to both the founding era's contentious debates and the post-war Era of Good Feelings consolidation"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor 1797–1807 and 1808–1809"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1796–1797 and 1815–1821"},
            {"target": "federalist-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Federalist maintaining the party in New England"},
            {"target": "embargo-act", "verb": "RESISTS", "note": "Governor opposing Jefferson's Embargo as harmful to Vermont"},
            {"target": "john-adams", "verb": "SERVES_DURING", "note": "Governor during Adams administration's controversies"}
        ]
    }),

    ("john-c-spencer", {
        "summary": (
            "John Canfield Spencer (1788–1855) "
            "was an American Whig politician "
            "from New York who served "
            "as Secretary of War (1841–1843) "
            "and Secretary of the "
            "Treasury (1843–1844) "
            "under President John Tyler "
            "— making him one of the "
            "few men to hold two "
            "different cabinet positions "
            "in a single administration. "
            "He is best known for "
            "the tragic Somers Affair "
            "(1842) — the mutiny "
            "execution aboard the "
            "USS Somers in which "
            "his son Midshipman "
            "Philip Spencer was "
            "executed for alleged "
            "mutiny by Commander "
            "Alexander Mackenzie.\n\n"
            "The Somers Affair "
            "was one of the most "
            "controversial episodes "
            "in American naval "
            "history — the only "
            "time the U.S. Navy "
            "executed a mutineer "
            "at sea — and Spencer's "
            "personal grief over "
            "his son's death "
            "combined with his "
            "War Department role "
            "overseeing the naval "
            "court of inquiry "
            "created an extraordinary "
            "conflict of interest.\n\n"
            "His Treasury service "
            "also included the "
            "rejection of his "
            "nomination to the "
            "Supreme Court — "
            "the Senate blocked "
            "his appointment.\n\n"
            "He was a prominent "
            "New York lawyer "
            "and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Secretary of War (1841–1843) and Treasury (1843–1844) under Tyler; personally involved in the Somers Affair (1842) when his son was executed for alleged mutiny — the only naval execution for mutiny in U.S. history; Supreme Court nomination blocked by Senate; one of the few men to hold two cabinet positions in one administration.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Tyler's political isolation — the president expelled from the Whig Party who needed competent administrators regardless of factional alignment — created the appointments through which Spencer served in two cabinet positions",
            "The Somers Affair — the alleged mutiny conspiracy aboard the USS Somers and Commander Mackenzie's decision to execute the alleged mutineers including Spencer's son — created the most personally devastating and publicly controversial event of Spencer's cabinet career",
            "Spencer's New York Whig connections and administrative reputation — his established standing as a prominent New York lawyer and politician — provided the qualifications for Tyler's cabinet appointments"
        ],
        "effects": [
            "His War Department oversight of the Somers Affair court of inquiry — while personally bereaved over his son's execution — created one of the most complex conflict-of-interest situations in American cabinet history",
            "The Somers Affair that occurred during his War Secretaryship contributed to the founding of the U.S. Naval Academy at Annapolis (1845) — the case demonstrating that naval officers needed better professional education than the chaotic midshipmen apprenticeship system",
            "His Treasury Secretaryship contributed to managing federal finances during the most politically chaotic period of a chaotic administration — navigating Tyler's inability to get congressional support for any coherent fiscal policy",
            "His Senate-blocked Supreme Court nomination illustrated Tyler's complete political isolation — even his qualified cabinet nominees were being rejected by the Whig Senate"
        ],
        "relationships": [
            {"target": "us-department-of-war", "verb": "LEADS", "note": "Secretary of War 1841–1843 under Tyler"},
            {"target": "us-department-of-treasury", "verb": "LEADS", "note": "Secretary of Treasury 1843–1844 under Tyler"},
            {"target": "somers-affair", "verb": "INVOLVED_IN", "note": "War Secretary during son's naval execution"},
            {"target": "us-naval-academy", "verb": "CONTRIBUTES_TO_FOUNDING_OF", "note": "Somers Affair during his tenure led to Naval Academy"},
            {"target": "john-tyler", "verb": "SERVES_UNDER", "note": "Tyler's two-portfolio cabinet officer"}
        ]
    }),

    ("joseph-bloomfield", {
        "summary": (
            "Joseph Bloomfield (1753–1823) "
            "was an American Democratic-Republican "
            "politician from New Jersey "
            "who served as Governor "
            "of New Jersey (1801–1802 "
            "and 1803–1812) and as "
            "a U.S. Representative "
            "(1817–1821). He had "
            "previously served as "
            "a captain in the Continental "
            "Army during the Revolutionary "
            "War and as New Jersey's "
            "Attorney General. His "
            "long governorship — "
            "spanning the Jefferson "
            "and Madison administrations "
            "— made him one of "
            "the most significant "
            "figures in New Jersey's "
            "early republican politics.\n\n"
            "Bloomfield served as "
            "Brigadier General "
            "of the New Jersey "
            "militia and commanded "
            "troops in the War "
            "of 1812 — a significant "
            "military role for "
            "a governor in his "
            "60s.\n\n"
            "The town of Bloomfield, "
            "New Jersey is named "
            "after him — a lasting "
            "geographical memorial "
            "to his long service "
            "to the state.\n\n"
            "He was one of "
            "New Jersey's "
            "founding-era political "
            "giants."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New Jersey Revolutionary War captain, Governor (1801–1812), and Congressman (1817–1821); commanded New Jersey militia in the War of 1812; Bloomfield, New Jersey is named after him; one of the most significant figures in New Jersey's early republican politics spanning the Jefferson and Madison administrations.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's Democratic-Republican political transformation — the Jeffersonian revolution of 1800 that swept Federalists from power and elevated Democratic-Republicans like Bloomfield to New Jersey's governorship — created the opportunity for his decade-long governorship",
            "Bloomfield's Revolutionary War service — his Continental Army captaincy and established military credentials — provided the patriotic prestige that underpinned his political career and later his War of 1812 militia command",
            "New Jersey's strategic importance in the Early Republic — the state's commercial position between Philadelphia and New York, its large agricultural population, and its importance to both parties — created the significance of Bloomfield's long gubernatorial tenure"
        ],
        "effects": [
            "His decade-long governorship contributed to New Jersey's institutional development — ten years of executive leadership during the formative period of American republican governance",
            "His War of 1812 militia command contributed to New Jersey's defense — organizing and leading the state's military forces during a war that brought British naval activity close to the New Jersey coast",
            "His geographical memorialization in Bloomfield, New Jersey confirmed his lasting legacy — the town named after him standing as a permanent reminder of his service to the state",
            "His career contributed to the Democratic-Republican dominance of New Jersey politics in the Jefferson-Madison era — displacing the Federalism that had characterized the state in the Washington-Adams period"
        ],
        "relationships": [
            {"target": "new-jersey", "verb": "GOVERNS", "note": "Governor of New Jersey 1801–1812"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Jersey Congressman 1817–1821"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Revolutionary War captain"},
            {"target": "war-of-1812", "verb": "COMMANDS_MILITIA_IN", "note": "New Jersey militia general"},
            {"target": "bloomfield-new-jersey", "verb": "MEMORIALIZED_IN", "note": "Town named after him"}
        ]
    }),

    ("gideon-granger", {
        "summary": (
            "Gideon Granger (1767–1822) "
            "was an American Democratic-Republican "
            "politician from Connecticut "
            "who served as U.S. Postmaster "
            "General (1801–1814) — "
            "one of the longest-serving "
            "Postmasters General in "
            "American history, spanning "
            "the entire Jefferson "
            "administration and most "
            "of Madison's. He was "
            "appointed by Jefferson "
            "as part of the Democratic-Republican "
            "takeover of the patronage "
            "system after the Federalist "
            "decade, and his long "
            "tenure made him the "
            "man most responsible "
            "for building the "
            "postal system of the "
            "early 19th century.\n\n"
            "Under Granger's leadership, "
            "the postal system "
            "expanded dramatically "
            "— post offices and "
            "post roads multiplied "
            "as the American population "
            "spread westward and "
            "the demand for reliable "
            "communication grew.\n\n"
            "He was also one of "
            "the earliest white "
            "American politicians "
            "to publicly oppose "
            "slavery — his "
            "Connecticut antislavery "
            "background informed "
            "his political positions.\n\n"
            "He served both Jefferson "
            "and Madison as Postmaster."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "U.S. Postmaster General (1801–1814) under Jefferson and Madison; oversaw dramatic expansion of American postal service as population spread westward; one of the earliest white politicians to publicly oppose slavery; longest-serving Postmaster General of the early Republic; built the postal infrastructure of the early 19th century.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Jefferson's Democratic-Republican patronage revolution — the systematic replacement of Federalist officeholders with Democratic-Republicans after 1800, including the crucial Postmaster Generalship — created Granger's appointment",
            "The westward expansion of the American population — the rapid growth of settlements beyond the Appalachians that required reliable postal communication — created the demand for the postal expansion that Granger managed",
            "Connecticut's Democratic-Republican minority — the unusual position of a Connecticut politician aligned with Jefferson's party in the most Federalist state in New England — gave Granger his political identity and his appointment value to Jefferson"
        ],
        "effects": [
            "His thirteen-year Postmaster Generalship built the postal infrastructure of the early American Republic — dramatically expanding post offices and post roads to connect an expanding nation's communities",
            "His postal expansion contributed to American national integration — the post roads and post offices that connected the seaboard to the interior and facilitated the communication and commerce that held the growing republic together",
            "His early antislavery positions contributed to the emerging antislavery political tradition — among the first white politicians to articulate public opposition to slavery in the context of national political office",
            "His patronage management — the systematic appointment of Democratic-Republicans to postal positions across the country — helped build the Democratic-Republican party organization that sustained Jeffersonian and Madisonian governance"
        ],
        "relationships": [
            {"target": "us-postal-service", "verb": "LEADS", "note": "Postmaster General 1801–1814"},
            {"target": "thomas-jefferson", "verb": "SERVES_UNDER", "note": "Jefferson's Postmaster General"},
            {"target": "james-madison", "verb": "SERVES_UNDER", "note": "Also Madison's Postmaster General"},
            {"target": "american-postal-expansion", "verb": "DIRECTS", "note": "Built early 19th-century postal infrastructure"},
            {"target": "antislavery-movement", "verb": "CONTRIBUTES_TO", "note": "Early white political opponent of slavery"}
        ]
    }),

    ("jacques-guillaume-thouret", {
        "summary": (
            "Jacques-Guillaume Thouret "
            "(1746–1794) was a French "
            "lawyer and Revolutionary "
            "politician who was one "
            "of the most important "
            "constitutional architects "
            "of the French Revolution — "
            "serving as president "
            "of the National Constituent "
            "Assembly and playing "
            "a major role in drafting "
            "the French Constitution "
            "of 1791 and in the "
            "Revolutionary reorganization "
            "of France's administrative "
            "divisions into the "
            "modern département "
            "system. He was executed "
            "during the Terror "
            "in 1794.\n\n"
            "The department system "
            "he helped create — "
            "replacing the old "
            "provinces, parlements, "
            "and feudal jurisdictions "
            "with rational, geometric "
            "administrative units "
            "— was one of the most "
            "enduring achievements "
            "of the Revolution, "
            "still governing France's "
            "administrative geography.\n\n"
            "His presidency of "
            "the National Assembly "
            "placed him at the "
            "apex of Revolutionary "
            "constitutional politics "
            "during the drafting "
            "of France's first "
            "written constitution.\n\n"
            "He was guillotined "
            "in 1794 as the "
            "Terror consumed him."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "French Revolutionary constitutional architect (1746–1794); president of the National Constituent Assembly; major role in drafting the Constitution of 1791; created the modern département administrative system that still governs France; executed during the Terror — his enduring legacy is the departmental system that France still uses today.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The French Revolution's constitutional crisis — the Old Regime's collapse and the need to replace the entire administrative and constitutional structure of France with rational, modern institutions — created the extraordinary opportunity for constitutional architects like Thouret",
            "Thouret's Norman lawyer background and constitutional expertise — his training and legal experience as a Normandy lawyer who came to Paris as a Third Estate deputy — provided the technical skills for drafting both constitutional and administrative legislation",
            "The Constituent Assembly's administrative reform mandate — the revolutionary assembly's determination to abolish the old provinces and parlements and replace them with a rational administrative system — created the specific project that Thouret led"
        ],
        "effects": [
            "His department system — the division of France into approximately 83 departments of roughly equal size, named after geographic features rather than historical provinces — created the administrative structure that France still uses, one of the most enduring institutional achievements of the Revolution",
            "His Constitution of 1791 contributions helped create the framework of the first French constitutional monarchy — the document that attempted to transform absolute monarchy into constitutional governance",
            "His execution during the Terror illustrated the tragic pattern of moderate Revolutionary leaders consumed by the radicalization they helped enable — Thouret's constitutionalism and moderation made him a target when Robespierre's Terror sought enemies",
            "His administrative legacy outlasted his political career by over two centuries — the département system he created in 1790 still organizing French governance, one of the most lasting concrete achievements of any revolutionary administrator"
        ],
        "relationships": [
            {"target": "national-constituent-assembly", "verb": "PRESIDES_OVER", "note": "President of the Revolutionary constitutional assembly"},
            {"target": "french-constitution-1791", "verb": "DRAFTS", "note": "Major drafter of France's first constitution"},
            {"target": "departement-system", "verb": "CREATES", "note": "Architect of the department administrative system still in use"},
            {"target": "the-terror", "verb": "EXECUTED_BY", "note": "Guillotined 1794"},
            {"target": "french-revolution", "verb": "ARCHITECTS", "note": "Constitutional and administrative architect of the Revolution"}
        ]
    }),

    ("john-m-berrien", {
        "summary": (
            "John Macpherson Berrien "
            "(1781–1856) was an American "
            "Democratic and later Whig "
            "politician from Georgia "
            "who served as U.S. Attorney "
            "General (1829–1831) under "
            "President Jackson and as "
            "U.S. Senator (1825–1829, "
            "1841–1852) — serving "
            "three separate Senate "
            "terms across more than "
            "a quarter century. He "
            "resigned as Attorney "
            "General during the "
            "Petticoat Affair — "
            "the social crisis in "
            "Jackson's cabinet "
            "over the social status "
            "of Peggy Eaton, "
            "Secretary of War "
            "Eaton's wife — a "
            "seemingly trivial "
            "scandal that caused "
            "a genuine cabinet "
            "purge.\n\n"
            "The Petticoat Affair "
            "was politically "
            "significant because "
            "it revealed Jackson's "
            "personal loyalty "
            "dynamics — his "
            "determination to "
            "defend Peggy Eaton "
            "caused his entire "
            "original cabinet "
            "to resign.\n\n"
            "Berrien subsequently "
            "became a Whig and "
            "returned to the "
            "Senate where he "
            "served for over "
            "a decade.\n\n"
            "He was a Georgia "
            "lawyer and senator "
            "for most of his adult life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Attorney General (1829–1831) and three-term Senator (1825–1829, 1841–1852); resigned as Attorney General in the Petticoat Affair that caused Jackson's cabinet purge; subsequently became a Whig; served in the Senate for over a quarter century; significant figure in Georgia and national antebellum politics.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Jackson's appointment — his selection of Georgia's Berrien as Attorney General as part of building his Jacksonian cabinet — created the role from which Berrien would resign in the Petticoat Affair",
            "The Petticoat Affair — the social crisis over Peggy Eaton's social acceptance in Washington that Jackson turned into a loyalty test for his cabinet — created the extraordinary situation in which Berrien resigned over a social controversy",
            "Berrien's shift to the Whig Party — his break with Jacksonian Democracy after the cabinet purge and his subsequent alignment with the anti-Jackson coalition — created the Whig identity that characterized his subsequent Senate career"
        ],
        "effects": [
            "His Attorney General resignation in the Petticoat Affair contributed to one of the most extraordinary cabinet purges in American history — the resignation of virtually the entire original Jackson cabinet over what began as a social dispute",
            "His subsequent Whig Senate career contributed Georgia's Whig perspective — the relatively small but real Georgia Whig tradition among the planter elite who preferred Clay's American System to Jackson's agrarian populism",
            "His three-term Senate tenure made him one of the most experienced Senate voices of the antebellum era — contributing Georgia's perspective to the Bank War debates, the nullification crisis, the Texas annexation, and the Compromise of 1850",
            "His career illustrated the fluidity of antebellum party allegiances — the way personal political breaks like the Petticoat Affair could permanently realign a politician's party identification"
        ],
        "relationships": [
            {"target": "us-department-of-justice", "verb": "LEADS", "note": "U.S. Attorney General 1829–1831"},
            {"target": "andrew-jackson", "verb": "SERVES_UNDER_THEN_BREAKS_WITH", "note": "Jackson's AG who resigned in the Petticoat Affair"},
            {"target": "petticoat-affair", "verb": "RESIGNED_OVER", "note": "Cabinet resignation catalyst"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Georgia Senator 1825–1829 and 1841–1852"},
            {"target": "whig-party-united-states", "verb": "JOINS", "note": "Became Whig after break with Jackson"}
        ]
    }),

    ("selah-b-strong", {
        "summary": (
            "Selah Brewster Strong (1792–1872) "
            "was an American Democratic "
            "politician and jurist from "
            "New York who served as "
            "a U.S. Representative "
            "(1839–1841) and as a "
            "justice of the New York "
            "Supreme Court. Strong "
            "had a dual career that "
            "combined relatively "
            "brief national political "
            "service with a much "
            "longer and more distinguished "
            "judicial career — a "
            "pattern common among "
            "the lawyer-politicians "
            "of the antebellum era "
            "who found the judiciary "
            "more professionally "
            "satisfying than the "
            "rough-and-tumble of "
            "machine politics.\n\n"
            "His House term coincided "
            "with the Tyler "
            "administration's "
            "political chaos — "
            "the Whig collapse "
            "and the beginning "
            "of the Texas annexation "
            "controversy — and "
            "he served as part "
            "of the New York "
            "Democratic delegation "
            "during one of the "
            "most politically "
            "complex periods "
            "of New York politics.\n\n"
            "His New York Supreme "
            "Court service — "
            "which lasted far "
            "longer than his "
            "congressional term "
            "— was his more "
            "significant professional "
            "achievement.\n\n"
            "He was a prominent "
            "Long Island lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New York Democratic Congressman (1839–1841) and New York Supreme Court Justice; brief congressional service during the Tyler era followed by longer judicial career; navigated New York's complex Democratic machine politics; Long Island lawyer whose judicial career was more significant than his political tenure.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Democratic machine politics — the Van Buren-aligned organization that coordinated Democratic Party activity across the state — created the political structure within which Strong's brief congressional career operated",
            "New York's complex factional politics — the Barnburner-Hunker division beginning to develop within the Democratic party — created the challenging environment that many New York Democrats preferred to leave for the more stable judicial branch",
            "Strong's legal expertise and Long Island professional standing — his established reputation as a lawyer in the Long Island region — provided both the qualifications for his judicial appointment and likely the professional alternative that drew him away from congressional politics"
        ],
        "effects": [
            "His House service contributed New York's Democratic perspective to the Tyler era's congressional chaos — voting on the issues of the day as the Whig Party collapsed and the Texas annexation question opened",
            "His New York Supreme Court service contributed to New York's legal development — the state court decisions that helped develop New York's legal system during the antebellum and Civil War eras",
            "His career illustrated the pattern of lawyer-politicians who found the judiciary more professionally rewarding than electoral politics — contributing to both the legislature and the bench in the antebellum era",
            "His long life (1792–1872) allowed him to witness the entire arc from the early Jacksonian era through the Civil War and into Reconstruction — an extraordinary span of American history"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1839–1841"},
            {"target": "new-york-supreme-court", "verb": "SERVES_ON", "note": "New York Supreme Court Justice"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "New York Democratic machine politician"},
            {"target": "john-tyler", "verb": "SERVES_DURING", "note": "Congressman during Tyler's chaotic presidency"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "Long Island Democratic congressman and jurist"}
        ]
    }),

    ("françois-louis-bourdon", {
        "summary": (
            "François-Louis Bourdon "
            "(1758–1798) was a French "
            "Revolutionary politician "
            "who served as a radical "
            "Jacobin deputy in the "
            "National Convention — "
            "the Revolutionary assembly "
            "that governed France "
            "during the Terror (1793–1794) "
            "and the subsequent Thermidorian "
            "Reaction. Known as "
            "'Bourdon de l'Oise' "
            "from his department, "
            "he was one of the "
            "Montagnard (Mountain) "
            "faction who supported "
            "radical Revolutionary "
            "policies.\n\n"
            "Bourdon played a "
            "role in the Thermidorian "
            "Reaction — the overthrow "
            "of Robespierre on "
            "9 Thermidor (July 27, 1794) "
            "that ended the Terror "
            "— though his precise "
            "role in the conspiracies "
            "that brought Robespierre "
            "down was complex.\n\n"
            "He subsequently served "
            "in the Council of Five "
            "Hundred — the lower "
            "house of the Directory's "
            "legislature — before "
            "dying young in 1798 "
            "during the Santo Domingo "
            "mission.\n\n"
            "His career illustrated "
            "the rapid political "
            "changes of the "
            "Revolutionary decade."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Revolutionary Jacobin deputy (1758–1798); National Convention Montagnard member during the Terror; involved in the Thermidorian Reaction that overthrew Robespierre (9 Thermidor, July 1794); served in the Council of Five Hundred; died in 1798 on the Santo Domingo mission; career illustrated the Revolutionary decade's rapid political transformations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radicalization — the movement from moderate constitutional monarchy to Jacobin radical democracy to the Terror — created the political environment in which Bourdon's radical politics found institutional expression",
            "The Montagnard-Girondin conflict — the struggle within the National Convention between the radical Mountain faction and the moderate Girondins — created the political alignment that defined Bourdon's Revolutionary career",
            "The Thermidorian conspiracy — the coalition of Montagnards, Thermidorians, and others who feared they would be the next victims of the Terror and united to overthrow Robespierre — created the political crisis that Bourdon was involved in"
        ],
        "effects": [
            "His involvement in the Thermidorian Reaction contributed to one of the most important turning points of the French Revolution — the overthrow of Robespierre that ended the Terror and began the more moderate Thermidorian phase",
            "His National Convention service contributed to the legislative work of the Terror era — the extraordinary body of laws, decrees, and administrative decisions that reorganized French society during the most radical phase of the Revolution",
            "His Council of Five Hundred service contributed to the Directory era's legislative governance — the post-Terror attempt to stabilize Revolutionary France under a more moderate constitutional framework",
            "His death in 1798 on the Santo Domingo mission illustrated the continuing dangers of Revolutionary service — even after the Terror, French Revolutionary politicians faced extraordinary personal risks"
        ],
        "relationships": [
            {"target": "national-convention", "verb": "SERVES_IN", "note": "Montagnard deputy during the Terror"},
            {"target": "council-of-five-hundred", "verb": "SERVES_IN", "note": "Directory-era legislative service"},
            {"target": "thermidorian-reaction", "verb": "PARTICIPATES_IN", "note": "Involved in the overthrow of Robespierre"},
            {"target": "maximilien-robespierre", "verb": "OPPOSES", "note": "Thermidorian opponent of Robespierre's Terror"},
            {"target": "french-revolution", "verb": "SERVES_IN", "note": "Jacobin Revolutionary politician across Terror and Directory"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 76 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
