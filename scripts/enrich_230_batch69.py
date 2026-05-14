#!/usr/bin/env python3
"""
Batch 69 — 8 entities: Peter Buell Porter, William Craik, George Watterston,
Julius Converse, Claude Alphonse Delangle, John W. Taylor, Nicolas-René Berryer,
Warren R. Davis
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

    ("peter-buell-porter", {
        "summary": (
            "Peter Buell Porter (1773–1844) "
            "was an American Democratic-Republican "
            "politician and military officer "
            "from New York who served as a "
            "U.S. Representative (1809–1813 "
            "and 1815–1816), as U.S. Secretary "
            "of War (1828–1829) under President "
            "Adams, and as a major general "
            "in the War of 1812. Porter "
            "was a 'War Hawk' — one of "
            "the congressional faction "
            "that pushed for war with "
            "Britain in 1812, arguing "
            "that British impressment "
            "of American sailors, "
            "interference with American "
            "trade, and support for "
            "Native American resistance "
            "required a military response.\n\n"
            "Porter served on the "
            "Niagara frontier during "
            "the War of 1812 — "
            "the critical northern "
            "border that was one "
            "of the war's main "
            "theaters of operation "
            "— commanding militia "
            "and regular forces "
            "in engagements including "
            "the Battle of Chippawa "
            "and Lundy's Lane (1814).\n\n"
            "His War Secretaryship "
            "under Adams contributed "
            "to the development "
            "of American military "
            "professionalization "
            "in the post-War of "
            "1812 era.\n\n"
            "He was a leading figure "
            "in western New York's "
            "commercial and political life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York War Hawk Congressman who pushed for the War of 1812; major general on the Niagara frontier at Chippawa and Lundy's Lane; U.S. Secretary of War under Adams (1828–1829); led western New York commercial and political life; one of the architects of the War of 1812 declaration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "British impressment of American sailors and interference with American trade — the systematic violations of American neutral rights that the War Hawks like Porter argued required a military response — created the political case for war that Porter championed in Congress",
            "Western New York's frontier perspective on British-supported Native American resistance — the region's experience of British encouragement of Tecumseh's confederation and the threat this posed to westward expansion — gave Porter and other frontier congressmen their strongest arguments for war",
            "The Democratic-Republican War Hawks' congressional coalition — the younger generation of Democratic-Republicans from the South and West who wanted a more assertive American foreign policy — created the political organization that pushed the Madison administration into the war declaration"
        ],
        "effects": [
            "His War Hawk advocacy contributed to the War of 1812 declaration — one of the most consequential votes in early American history, launching the war that would define the character of the young nation and its relationship with Britain",
            "His Niagara frontier service contributed to the American military's performance in one of the war's most contested theaters — the Canadian-American border where American forces achieved some of their most significant tactical successes",
            "His War Secretaryship under Adams contributed to the post-war professionalization of the American military — the development of the army's institutional capacity in the period between the War of 1812 and the Mexican-American War",
            "His western New York leadership contributed to the region's development as one of the most commercially dynamic parts of the early republic — the Erie Canal corridor that was transforming American economic geography"
        ],
        "relationships": [
            {"target": "war-of-1812", "verb": "ADVOCATES_FOR", "note": "War Hawk who pushed for the 1812 declaration"},
            {"target": "niagara-frontier", "verb": "COMMANDS_ON", "note": "Major general in Niagara frontier campaigns"},
            {"target": "us-department-of-war", "verb": "LEADS", "note": "Secretary of War 1828–1829 under Adams"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1809–1813 and 1815–1816"},
            {"target": "battle-of-lundys-lane", "verb": "FIGHTS_AT", "note": "Commander at the 1814 Niagara battle"}
        ]
    }),

    ("william-craik", {
        "summary": (
            "William Craik (1761–1814) was "
            "an American Federalist politician "
            "from Maryland who served in "
            "the U.S. House of Representatives "
            "(1796–1801) during the height "
            "of the Federalist-Democratic-Republican "
            "conflict — the Jay Treaty "
            "controversy, the XYZ Affair "
            "and Quasi-War with France, "
            "the Alien and Sedition Acts, "
            "and the Revolution of 1800 "
            "that ended Federalist national "
            "political dominance. As a "
            "Maryland Federalist, he "
            "represented the commercial "
            "and planter interests "
            "of a politically divided "
            "state during the "
            "party system's most "
            "dramatic early conflicts.\n\n"
            "Maryland's Federalism "
            "was rooted in the "
            "commercial interests "
            "of Baltimore's merchants "
            "and the Eastern Shore's "
            "planter gentry who "
            "had close commercial "
            "ties to Britain and "
            "opposed the Jacobin "
            "enthusiasm that many "
            "Democratic-Republicans "
            "showed for the French "
            "Revolution.\n\n"
            "His House service "
            "during the Adams "
            "administration placed "
            "him at the center "
            "of the Quasi-War's "
            "policy debates — "
            "the naval conflict "
            "with France, the "
            "army expansion, "
            "and the Alien and "
            "Sedition Acts' passage.\n\n"
            "He died in 1814, "
            "during the War of 1812."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Federalist Congressman (1796–1801); served through the Jay Treaty, XYZ Affair, Alien and Sedition Acts, and Revolution of 1800; represented Maryland's commercial Federalism during the party's final years of national dominance; died in 1814 during the War of 1812.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's commercial Federalism — the Eastern Shore planters' and Baltimore merchants' close ties to Britain, their opposition to French revolutionary radicalism, and their support for Hamilton's financial system — created the political constituency for Craik's Federalist congressional career",
            "The Jay Treaty controversy (1795–1796) — the deeply unpopular compromise treaty with Britain that Democratic-Republicans attacked as a capitulation to British interests but Federalists defended as necessary for commercial stability — created the political polarization that defined Craik's early House service",
            "The Quasi-War with France (1798–1800) and the Alien and Sedition Acts — the Adams administration's military buildup, naval conflict with France, and controversial press restrictions — created the major domestic and foreign policy crises of Craik's House tenure"
        ],
        "effects": [
            "His House service contributed Maryland's Federalist votes to the Adams administration's controversial foreign and domestic policies — the Quasi-War authorization, the army expansion, and the Alien and Sedition Acts",
            "His participation in the Revolution of 1800's House phase — the Jefferson-Burr electoral tie that was resolved by the House — placed him in one of the most consequential moments in American electoral history",
            "His career illustrated the pattern of Maryland Federalism — the commercial and planter class politics that maintained Federalist representation from a state where Democratic-Republicans were also competitive",
            "His death during the War of 1812 — the war that Federalists had generally opposed as a product of Democratic-Republican agrarianism and hostility to Britain — placed him among the Federalist generation who did not survive to see the party's final collapse"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Congressman 1796–1801"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Maryland Federalist in the first party system"},
            {"target": "alien-and-sedition-acts", "verb": "SUPPORTS", "note": "Federalist voting for the controversial acts"},
            {"target": "quasi-war", "verb": "SERVES_DURING", "note": "Congressman during the naval conflict with France"},
            {"target": "revolution-of-1800", "verb": "PARTICIPATES_IN", "note": "House member during the Jefferson-Burr electoral crisis"}
        ]
    }),

    ("george-watterston", {
        "summary": (
            "George Watterston (1783–1854) "
            "was an American author, novelist, "
            "and the third Librarian of "
            "Congress (1815–1829) who played "
            "a crucial role in developing "
            "the Library of Congress in "
            "its formative years. Appointed "
            "by James Madison, Watterston "
            "was the first Librarian to "
            "treat the position as a "
            "professional literary role "
            "rather than merely a clerical "
            "appointment, and he worked "
            "to build the collection "
            "that had been devastated "
            "when the British burned "
            "Washington in August 1814.\n\n"
            "The Library's reconstruction "
            "after the British burning "
            "began with Congress's "
            "purchase of Thomas Jefferson's "
            "personal library (6,487 volumes) "
            "in 1815 — one of the "
            "largest private libraries "
            "in America — which Watterston "
            "oversaw and catalogued, "
            "transforming the Library "
            "from a congressional "
            "reference collection "
            "into a genuinely national "
            "library.\n\n"
            "Watterston was also a "
            "novelist and journalist "
            "— one of the early "
            "practitioners of American "
            "fiction — who wrote "
            "Washington society novels "
            "and political commentary.\n\n"
            "His removal by Andrew "
            "Jackson in 1829 — "
            "as a spoils system "
            "casualty — was controversial."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Third Librarian of Congress (1815–1829); oversaw the acquisition and cataloguing of Jefferson's library (6,487 volumes) that rebuilt the collection after the British burned Washington; first to treat the position as a professional literary role; also a novelist; removed by Jackson as spoils system casualty — contributed foundationally to the Library of Congress.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The British burning of Washington (August 1814) — the destruction of the original Library of Congress when British forces burned the Capitol — created both the crisis and the opportunity for the Library's reconstruction that defined Watterston's tenure",
            "Congress's purchase of Jefferson's library (1815) — the acquisition of one of America's largest private collections to replace the destroyed books — gave Watterston the task of cataloguing and organizing a collection that transformed the Library's scope and character",
            "James Madison's appointment philosophy — choosing a literary man of professional inclination for the Librarian position rather than a purely clerical appointment — created the institutional approach that made Watterston's tenure significant"
        ],
        "effects": [
            "His organization and cataloguing of the Jefferson collection transformed the Library of Congress from a congressional reference library into the foundation of a genuine national library — establishing the institutional trajectory that eventually made the Library the world's largest",
            "His professional approach to the Librarian position helped establish the expectation that the Library of Congress should be a significant cultural institution rather than merely a legislative convenience",
            "His removal by Jackson in 1829 — as part of the spoils system's application to what had been a professional appointment — contributed to the debate about the proper role of merit versus political patronage in federal appointments",
            "His novelistic work contributed to the development of early American fiction — the Washington society novels that documented the social world of the early republic's capital with an insider's perspective"
        ],
        "relationships": [
            {"target": "library-of-congress", "verb": "LEADS", "note": "Third Librarian of Congress 1815–1829"},
            {"target": "thomas-jefferson-library", "verb": "CATALOGUES", "note": "Organized the Jefferson collection purchase"},
            {"target": "james-madison", "verb": "APPOINTED_BY", "note": "Madison's Librarian appointment"},
            {"target": "andrew-jackson", "verb": "REMOVED_BY", "note": "Spoils system casualty in 1829"},
            {"target": "burning-of-washington-1814", "verb": "REBUILDS_AFTER", "note": "Rebuilt Library collection after British burning"}
        ]
    }),

    ("julius-converse", {
        "summary": (
            "Julius Converse (1798–1885) "
            "was an American Whig and "
            "Republican politician from "
            "Vermont who served as Governor "
            "of Vermont (1872–1874). "
            "His gubernatorial tenure "
            "came during the Grant "
            "administration's second "
            "term — the period of "
            "the Liberal Republican "
            "movement, the Credit Mobilier "
            "scandal, and the deepening "
            "economic crisis that "
            "would culminate in the "
            "Panic of 1873.\n\n"
            "Vermont was one of "
            "the most reliably "
            "Republican states in "
            "the Union — the state's "
            "granite Republicanism "
            "had made it a Whig "
            "stronghold before "
            "the Civil War and "
            "a Republican bastion "
            "after. Converse's "
            "governorship represented "
            "this tradition.\n\n"
            "His long life (1798–1885) "
            "made him one of the "
            "most remarkable witnesses "
            "to American political "
            "history — born during "
            "John Adams's presidency "
            "and dying a generation "
            "after the Civil War, "
            "he had lived through "
            "the entire transformation "
            "of American politics "
            "from the Federalist "
            "era through Reconstruction.\n\n"
            "He was primarily a "
            "businessman and "
            "entrepreneur before "
            "his political career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Governor of Vermont (1872–1874) during the Grant era's scandals and Panic of 1873; represented Vermont's granite Republicanism; extraordinarily long life (1798–1885) spanning from Adams's presidency through Reconstruction; businessman-politician from reliably Republican Vermont.",
            "significanceCategory": "local"
        },
        "causes": [
            "Vermont's Republican political tradition — the state's overwhelming commitment to the Republican Party that made it one of the most reliably one-party states in the nation — provided the political environment for Converse's gubernatorial election",
            "The Grant administration's political environment (1872–1876) — the Liberal Republican movement's challenge to regular Republicanism, the Credit Mobilier and Whiskey Ring scandals, and the economic crisis of 1873 — created the political context for Converse's governorship",
            "Converse's business success — his entrepreneurial career in Vermont's economy — provided the financial resources and social prominence that facilitated his entry into political life"
        ],
        "effects": [
            "His governorship managed Vermont's affairs during the economic crisis of the Panic of 1873 — the sharp depression that followed Jay Cooke's railroad investment collapse and affected even Vermont's granite economy",
            "His tenure contributed to Vermont's Republican governance tradition — maintaining the state's characteristic Republicanism through the Reconstruction era",
            "His extraordinary longevity made him a witness to American political history from the Adams era to the Gilded Age — providing lived memory across decades that few people could match",
            "His career illustrated the pattern of Vermont business-politician governors — the successful entrepreneurs who entered politics in a one-party state where Republican nomination was tantamount to election"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1872–1874"},
            {"target": "republican-party-united-states", "verb": "MEMBER_OF", "note": "Embodiment of Vermont's granite Republicanism"},
            {"target": "panic-of-1873", "verb": "GOVERNS_DURING", "note": "Governor during the economic depression"},
            {"target": "ulysses-s-grant", "verb": "SERVES_DURING", "note": "Governor during Grant's second term"},
            {"target": "reconstruction-era", "verb": "PARTICIPATES_IN", "note": "Republican governor during Reconstruction"}
        ]
    }),

    ("claude-alphonse-delangle", {
        "summary": (
            "Claude Alphonse Delangle "
            "(1797–1869) was a French "
            "lawyer, politician, and "
            "magistrate who served as "
            "Minister of Justice of "
            "France (1858–1859) under "
            "Napoleon III and as President "
            "of the French Senate. "
            "A distinguished career "
            "jurist who rose through "
            "the French legal hierarchy "
            "under both the July Monarchy "
            "and the Second Empire, "
            "Delangle represented "
            "the career magistracy "
            "that Napoleon III's "
            "authoritarian government "
            "used to ensure judicial "
            "compliance with imperial "
            "policies.\n\n"
            "The Second Empire's "
            "judicial system was "
            "subordinated to imperial "
            "authority — judges "
            "served at the emperor's "
            "pleasure, political "
            "trials were carefully "
            "managed, and the "
            "Ministry of Justice "
            "was a key instrument "
            "of imperial social "
            "control. Delangle's "
            "ministerial tenure "
            "coincided with the "
            "height of Napoleon III's "
            "authoritarian phase.\n\n"
            "His Senate presidency "
            "— the Corps législatif "
            "under Napoleon III "
            "being largely decorative "
            "— placed him at "
            "the symbolic head "
            "of the imperial "
            "legislative system.\n\n"
            "He was a significant "
            "figure in the Second "
            "Empire's legal establishment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Minister of Justice (1858–1859) under Napoleon III and President of the French Senate; career magistrate who rose under July Monarchy and Second Empire; administered justice under Napoleon III's authoritarian phase; significant figure in the Second Empire's legal establishment.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon III's Second Empire — the authoritarian government established after the 1851 coup that reorganized French political and judicial institutions to serve imperial authority — created the institutional environment within which Delangle rose to ministerial and senatorial prominence",
            "The French career magistracy's development — the professional judiciary that successive French governments had been building since the Napoleonic legal reforms, which produced a class of trained career jurists who served whichever government held power — provided Delangle's professional pathway",
            "Napoleon III's need for reliable ministerial servants — the emperor's preference for career professionals who could administer the government's legal and judicial functions without challenging imperial authority — created the demand for officials like Delangle"
        ],
        "effects": [
            "His Justice Ministry tenure administered French law during the height of Napoleon III's authoritarian governance — overseeing the judicial system that managed political prosecutions, press censorship enforcement, and the legal apparatus of imperial control",
            "His Senate presidency contributed to the Second Empire's legislative institutions — the ceremonial function of heading a body that had little genuine legislative power under Napoleon III's constitution",
            "His career contributed to the continuity of the French legal system across regime changes — the professional judiciary's survival through July Monarchy and Second Empire that maintained institutional coherence despite political upheavals",
            "His ministerial service contributed to the development of French administrative law — the body of law governing the relationship between citizens and the state that French jurists continued to elaborate under every regime"
        ],
        "relationships": [
            {"target": "napoleon-iii", "verb": "SERVES", "note": "Minister of Justice under Napoleon III"},
            {"target": "french-ministry-of-justice", "verb": "LEADS", "note": "Minister of Justice 1858–1859"},
            {"target": "french-senate", "verb": "PRESIDES_OVER", "note": "President of the French Senate under Second Empire"},
            {"target": "second-empire-france", "verb": "SERVES_IN", "note": "Senior official in Napoleon III's government"},
            {"target": "july-monarchy-france", "verb": "SERVES_UNDER", "note": "Career magistrate rising under the July Monarchy"}
        ]
    }),

    ("john-w-taylor", {
        "summary": (
            "John W. Taylor (1784–1854) "
            "was an American Democratic-Republican "
            "and later National Republican "
            "politician from New York who "
            "served in the U.S. House of "
            "Representatives (1813–1833) "
            "and was twice elected Speaker "
            "of the House (1820–1821 and "
            "1825–1827). His first "
            "speakership came during "
            "the Missouri Crisis — "
            "the explosive debate over "
            "Missouri's admission as "
            "a slave state that nearly "
            "destroyed the Union — "
            "and his second during the "
            "contested 1824 election's "
            "aftermath, when he was "
            "the anti-Crawford, anti-Jackson "
            "candidate's choice for Speaker.\n\n"
            "Taylor was one of the "
            "earliest congressional "
            "leaders to take a strong "
            "antislavery position — "
            "he supported the Tallmadge "
            "Amendment that would "
            "have required Missouri "
            "to adopt gradual emancipation "
            "as a condition of statehood, "
            "and his antislavery "
            "stance made him a "
            "controversial figure "
            "in the sectional politics "
            "of the 1820s.\n\n"
            "His two non-consecutive "
            "speakerships reflect "
            "the contested nature "
            "of this era's House "
            "politics.\n\n"
            "He was eventually defeated "
            "for reelection as Jacksonian "
            "Democrats swept New York."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Two-time Speaker of the U.S. House (1820–1821 and 1825–1827); presided during the Missouri Crisis and the contested 1824 election aftermath; one of the earliest prominent congressional antislavery voices supporting the Tallmadge Amendment; his two non-consecutive speakerships reflect the political turbulence of the 1820s sectional crisis.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Missouri Crisis (1819–1821) — the explosive debate over Missouri's admission as a slave state and whether Congress could impose conditions on slavery in new states — created the political controversy that defined Taylor's first speakership and his emerging antislavery political identity",
            "The 1824 election's four-way fragmentation of the Democratic-Republican Party — the competition among Crawford, Adams, Jackson, and Clay that sent the election to the House and produced the 'corrupt bargain' — created the complex factional environment for Taylor's second speakership election",
            "New York's antislavery political tradition — the state's gradual emancipation movement (New York had abolished slavery by 1827) and the significant political constituency for restricting slavery's expansion — provided Taylor his antislavery political base"
        ],
        "effects": [
            "His support for the Tallmadge Amendment during the Missouri Crisis contributed to the most significant antislavery congressional effort before the 1840s — an attempt to make gradual emancipation a condition of Missouri statehood that passed the House but was defeated in the Senate",
            "His two speakerships presided over some of the most politically turbulent years of the early republic — the Missouri compromise, the Erie Canal's economic impact on New York politics, and the 1824 election's aftermath",
            "His eventual defeat by Jacksonian Democrats illustrated the political costs of antislavery politics in the 1820s–1830s — the way Jacksonian majority-building required subordinating antislavery sentiment to Southern and Western coalition maintenance",
            "His career contributed to the development of an antislavery political tradition in New York that would eventually feed into the Liberty Party, Free Soil, and Republican movements of the 1840s–1850s"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1813–1833"},
            {"target": "speaker-of-the-house", "verb": "SERVES_AS", "note": "Speaker 1820–1821 and 1825–1827"},
            {"target": "missouri-compromise", "verb": "PRESIDES_DURING", "note": "Speaker during the Missouri Crisis"},
            {"target": "tallmadge-amendment", "verb": "SUPPORTS", "note": "Backed gradual emancipation as Missouri condition"},
            {"target": "election-of-1824", "verb": "SERVES_DURING", "note": "Speaker during the contested election's House phase"}
        ]
    }),

    ("nicolas-rené-berryer", {
        "summary": (
            "Nicolas-René Berryer (1703–1762) "
            "was a French royal official "
            "who served as Lieutenant "
            "General of Police of Paris "
            "(1747–1757) — one of the "
            "most powerful administrative "
            "posts in the Ancien Régime "
            "— and subsequently as "
            "Secretary of State for "
            "the Navy (1758–1762) during "
            "the Seven Years' War. "
            "His police tenure coincided "
            "with the height of the "
            "Enlightenment and the "
            "philosophes' challenge "
            "to royal authority — "
            "and as Paris's chief "
            "law enforcement officer, "
            "he was responsible for "
            "surveilling the Enlightenment's "
            "radical writers and "
            "managing the explosive "
            "political tensions of "
            "mid-century Paris.\n\n"
            "Berryer's police administration "
            "involved monitoring the "
            "clandestine book trade, "
            "managing the Paris "
            "prison system, "
            "overseeing the city's "
            "complex social order "
            "— from aristocratic "
            "debauchery to criminal "
            "underworld — and "
            "managing the political "
            "surveillance that "
            "protected royal authority.\n\n"
            "His Navy Secretaryship "
            "during the Seven Years' "
            "War was a disaster — "
            "France lost its navy "
            "and its American and "
            "Indian empire during "
            "his tenure.\n\n"
            "He is a significant "
            "figure in Ancien Régime "
            "administrative history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Lieutenant General of Police of Paris (1747–1757) during the Enlightenment's peak; responsible for surveilling philosophes and managing the clandestine book trade; Navy Secretary during the Seven Years' War (1758–1762) when France lost its naval power and American empire; significant figure in Ancien Régime administrative history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Ancien Régime police system's central role in managing Paris's complex social order — the Lieutenant General of Police's extraordinary jurisdiction over virtually every aspect of Parisian life from markets and morals to political surveillance — created the institutional framework for Berryer's powerful role",
            "The Enlightenment's challenge to royal and ecclesiastical authority — the philosophes' radical writings, the clandestine book trade, and the growing public sphere that royal authority could not fully control — created the political surveillance challenge that Berryer's police administration had to manage",
            "The Seven Years' War's outbreak (1756) — the global conflict that pitted France against Britain and Prussia across Europe, North America, India, and the Caribbean — created the military-naval crisis that required a Navy Secretary to manage France's catastrophic strategic situation"
        ],
        "effects": [
            "His police administration contributed to the surveillance and management of the Enlightenment's radical intellectual community — the monitoring of philosophes, the clandestine book trade, and the political opposition that would eventually produce the French Revolution",
            "His Navy Secretaryship during the Seven Years' War contributed to one of France's greatest strategic disasters — the loss of the French navy's effectiveness, the fall of New France, and the dismemberment of France's Indian empire that was sealed by the Treaty of Paris (1763)",
            "His career illustrated the Ancien Régime's administrative structure — the way royal service moved skilled administrators between completely different roles (police, then navy) based on royal favor rather than specialized expertise",
            "The failures of his Navy Secretaryship contributed to France's strategic humiliation that would eventually fuel the French desire for revenge against Britain — contributing indirectly to French support for the American Revolution"
        ],
        "relationships": [
            {"target": "paris-police-lieutenant-general", "verb": "SERVES_AS", "note": "Lieutenant General of Police 1747–1757"},
            {"target": "french-navy", "verb": "LEADS", "note": "Secretary of State for the Navy 1758–1762"},
            {"target": "seven-years-war", "verb": "MANAGES_NAVY_DURING", "note": "Navy head during France's catastrophic war"},
            {"target": "french-enlightenment", "verb": "SURVEILS", "note": "Police chief monitoring philosophes and clandestine books"},
            {"target": "new-france", "verb": "OVERSEES_LOSS_OF", "note": "Navy Secretary during the fall of New France"}
        ]
    }),

    ("warren-r-davis", {
        "summary": (
            "Warren R. Davis (1793–1835) "
            "was an American Democratic "
            "politician from South Carolina "
            "who served in the U.S. House "
            "of Representatives (1827–1835) "
            "during the Nullification "
            "Crisis era. As a South "
            "Carolina congressman during "
            "one of the most dangerous "
            "constitutional crises of "
            "the antebellum period, "
            "Davis represented a state "
            "that had declared federal "
            "protective tariffs "
            "unconstitutional and "
            "threatened to secede "
            "if the federal government "
            "attempted to enforce them.\n\n"
            "The Nullification Crisis "
            "(1832–1833) — South "
            "Carolina's attempt under "
            "John C. Calhoun's theoretical "
            "leadership to 'nullify' "
            "the Tariff of Abominations "
            "— was the most serious "
            "constitutional challenge "
            "to federal authority "
            "before the Civil War. "
            "President Jackson's "
            "forceful response — "
            "the Proclamation to "
            "South Carolina and "
            "the Force Bill — "
            "combined with Clay's "
            "compromise tariff "
            "to defuse the crisis.\n\n"
            "Davis served through "
            "this entire crisis "
            "as a South Carolina "
            "congressman who navigated "
            "between Calhoun's "
            "nullification position "
            "and Unionist opposition.\n\n"
            "He died in office in 1835."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "South Carolina Congressman (1827–1835) through the Nullification Crisis; represented the state that threatened secession over federal tariffs; served through Calhoun's nullification doctrine, Jackson's Force Bill, and Clay's compromise tariff that resolved the crisis; died in office in 1835.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's economic grievances against protective tariffs — the state's plantation economy's vulnerability to high import tariffs that raised the cost of manufactured goods while the cotton planters' export market was not protected — created the political conditions for Calhoun's nullification doctrine and Davis's congressional career in a nullification-era state",
            "John C. Calhoun's constitutional theory of nullification — the argument that states could declare federal laws unconstitutional and refuse to enforce them within their borders — provided the theoretical framework for the South Carolina Nullification Crisis that defined Davis's congressional era",
            "Jackson's political split with Calhoun — the personal and political break between the president and his vice president that transformed the nullification fight from an academic constitutional debate into a direct confrontation between federal and state authority — created the crisis that Davis's South Carolina delegation had to navigate"
        ],
        "effects": [
            "His congressional service during the Nullification Crisis represented South Carolina's defiant position — contributing the state's congressional voice to the most dangerous constitutional confrontation of the antebellum period",
            "His navigation of the nullification controversy — between Calhoun's radical nullifiers and the Unionist minority within South Carolina — illustrated the difficult position of South Carolina congressmen during the crisis",
            "His death in office (1835) placed him among the South Carolina political leadership that saw the Nullification Crisis through to its compromise resolution but did not live to see the subsequent developments that built toward the Civil War",
            "His career contributed to the pattern of South Carolina politics — the state's particular combination of plantation economy, Calhounite political theory, and states'-rights constitutionalism that made it the most consistently radical defender of Southern interests"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "South Carolina Congressman 1827–1835"},
            {"target": "nullification-crisis", "verb": "SERVES_DURING", "note": "Congressman during South Carolina's constitutional challenge"},
            {"target": "john-c-calhoun", "verb": "REPRESENTS_STATE_OF", "note": "South Carolina congressman during Calhoun's nullification"},
            {"target": "andrew-jackson", "verb": "OPPOSES_FORCE_BILL", "note": "South Carolina congressman during Jackson's Force Bill"},
            {"target": "tariff-of-abominations", "verb": "SERVES_DURING", "note": "Congressman during the tariff controversy"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 69 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
