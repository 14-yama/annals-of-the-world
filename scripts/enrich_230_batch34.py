#!/usr/bin/env python3
"""
Batch 34 — 8 entities: Jesse B. Thomas, John Taylor of Caroline, George Jones,
Charles A. Wickliffe, William Pope Duval, James Burrill Jr.,
Augustus Baldwin Longstreet, Truman Smith
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

    # 1 — Jesse B. Thomas
    ("jesse-b-thomas", {
        "summary": (
            "Jesse Burgess Thomas (1777–1853) was an American lawyer, judge, "
            "and politician best known as the author of the Missouri Compromise "
            "line — the 36°30' parallel that divided free and slave territory "
            "in the Louisiana Purchase and that defined the geography of American "
            "slavery from 1820 to 1854. Thomas served as a delegate from Indiana "
            "Territory to the 10th Congress, as president of Illinois's "
            "Constitutional Convention (1818) that admitted Illinois to the Union, "
            "and as one of Illinois's first two United States Senators (1818–1829).\n\n"
            "The Missouri Compromise of 1820 was the first great congressional "
            "attempt to resolve the question of slavery's expansion — triggered "
            "by Missouri's application for statehood as a slave state, which "
            "threatened to break the Senate's equal balance of free and slave "
            "states. Thomas's amendment — admitting Missouri as a slave state "
            "while admitting Maine as a free state, and prohibiting slavery "
            "north of 36°30' in the remaining Louisiana Purchase territory — "
            "was the legislative formula that resolved the immediate crisis. "
            "Henry Clay later took much of the political credit, but Thomas's "
            "amendment was the actual mechanism of compromise.\n\n"
            "Thomas Jefferson called the Missouri Crisis 'a fire bell in the night' "
            "and predicted it would eventually destroy the Union — a prediction "
            "the Thomas Compromise line delayed for 34 years, until the Kansas-Nebraska "
            "Act of 1854 repealed it.\n\n"
            "Thomas retired from the Senate in 1829 and largely withdrew from "
            "public life, but his legislative contribution — the 36°30' line — "
            "shaped the political geography of the United States for a generation."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Author of the Missouri Compromise line (36°30' parallel) — the legislative formula that divided free and slave territory in the Louisiana Purchase and defined the geography of American slavery from 1820 to 1854; first Illinois US Senator (1818–1829); president of Illinois's 1818 Constitutional Convention.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Missouri's application for statehood as a slave state — which threatened to break the Senate's equal balance of free and slave states — created the sectional crisis that required the compromise formula Thomas provided",
            "Thomas's position as an Illinois senator — from the most recently admitted free state — made him a credible broker for a compromise that balanced free and slave state interests",
            "The political necessity of preserving the Senate's free-slave balance while allowing continued western settlement created the structural problem that Thomas's 36°30' line solved — a geographic solution to a political impasse"
        ],
        "effects": [
            "The Missouri Compromise line (36°30') defined the political geography of American slavery for 34 years — preserving sectional peace by creating a clear geographic boundary between free and slave territory in the Louisiana Purchase",
            "The Kansas-Nebraska Act of 1854 — which repealed the Thomas line by establishing popular sovereignty — shattered this 34-year peace and directly triggered the sectional crisis that produced the Civil War",
            "Jefferson's famous 'fire bell in the night' letter — warning that the Missouri Crisis revealed the existential threat slavery posed to the Union — was motivated by the crisis that Thomas's compromise temporarily resolved",
            "His 36°30' line became the reference point for all subsequent territorial slavery debates — California's latitude, the Mexican Cession, the Gadsden Purchase — making it one of the most consequential lines drawn in American political history"
        ],
        "relationships": [
            {"entity": "Missouri Compromise (1820)", "relationship": "AUTHOR_OF_COMPROMISE_LINE_IN", "note": "Author of the 36°30' amendment — the legislative mechanism that resolved the Missouri Crisis by dividing Louisiana Purchase territory between free and slave"},
            {"entity": "Kansas-Nebraska Act (1854)", "relationship": "36°30'_LINE_REPEALED_BY", "note": "His Missouri Compromise line (36°30') was repealed by the Kansas-Nebraska Act — shattering 34 years of sectional peace and triggering the crisis that produced the Civil War"},
            {"entity": "Illinois Constitutional Convention (1818)", "relationship": "PRESIDENT_OF", "note": "Presided over Illinois's 1818 Constitutional Convention — helping draft the state constitution that admitted Illinois to the Union"},
            {"entity": "Illinois (US Senate, 1818–1829)", "relationship": "FOUNDING_SENATOR", "note": "One of Illinois's first two US Senators (1818–1829) — representing the most recently admitted free state during the Missouri Compromise crisis"},
            {"entity": "Thomas Jefferson ('fire bell in the night' letter)", "relationship": "COMPROMISE_THAT_MOTIVATED_WARNING_OF", "note": "Jefferson's famous 'fire bell in the night' letter was motivated by the Missouri Crisis — which Thomas's compromise temporarily resolved but which Jefferson predicted would eventually destroy the Union"}
        ]
    }),

    # 2 — John Taylor of Caroline
    ("john-taylor-of-caroline", {
        "summary": (
            "John Taylor of Caroline (1753–1824) — so named to distinguish him "
            "from the many other John Taylors in American politics — was a "
            "Virginia planter, politician, and political philosopher who was "
            "one of the most intellectually rigorous theorists of Jeffersonian "
            "agrarian republicanism and states' rights in the early republic. "
            "He served multiple terms in the Virginia House of Delegates and "
            "as a US Senator (1792–1794, 1803, 1822–1824) — though he repeatedly "
            "resigned because he found legislative life disagreeable — but it "
            "was through his books and pamphlets that he exercised his most "
            "lasting influence on American political thought.\n\n"
            "His major works — 'An Inquiry into the Principles and Policy of "
            "the Government of the United States' (1814) and 'Tyranny Unmasked' "
            "(1822) — provided the most systematic intellectual defense of agrarian "
            "republicanism, states' rights, and anti-bank, anti-tariff economic "
            "policies that any founding-era American produced. He was a fierce "
            "critic of John Adams, Alexander Hamilton's financial program, the "
            "national bank, and the emerging capitalist economy that he believed "
            "was corrupting the republic's agrarian foundations.\n\n"
            "Taylor was Thomas Jefferson's most trusted political ally and "
            "intellectual companion — a friendship sustained through decades "
            "of correspondence. Jefferson called Taylor's 'Inquiry' 'the most "
            "logical retraction of our principles that I have ever seen' — "
            "and Taylor's agrarian vision was the philosophical foundation "
            "of Jeffersonian Democracy in its purest form.\n\n"
            "His writings influenced John C. Calhoun, the states' rights "
            "tradition, and Southern political thought into the Civil War era."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Virginia Jeffersonian Republican political philosopher and US Senator; author of 'Inquiry into the Principles and Policy of the Government of the United States' (1814) and 'Tyranny Unmasked' (1822); Thomas Jefferson's closest intellectual ally; the most systematic theorist of agrarian republicanism and states' rights in the early republic.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Virginia's agrarian planter culture — and its tradition of educated gentlemen-farmers who combined plantation management with political theory — created the intellectual environment in which Taylor developed his agrarian republican philosophy",
            "Hamilton's financial program — the national bank, protective tariffs, funded debt, and the commercial-manufacturing vision of America's future — created the target against which Taylor's most systematic critiques were directed",
            "His close friendship with Jefferson — and their shared vision of an agrarian republic of independent farmers rather than a commercial-industrial republic of merchants and manufacturers — created the intellectual partnership that shaped both men's political philosophy"
        ],
        "effects": [
            "His 'Inquiry' and 'Tyranny Unmasked' provided the most systematic intellectual defense of agrarian republicanism and states' rights — influencing Southern political thought for decades and shaping the ideological tradition that Calhoun would develop into nullification doctrine",
            "His anti-bank writings contributed to the intellectual foundation of the Jacksonian Bank War — Andrew Jackson's destruction of the Second Bank of the United States drew heavily on the tradition Taylor had established",
            "His influence on Jefferson was mutual and profound — Taylor's systematic political philosophy gave Jeffersonian Democracy its most rigorous theoretical foundation and helped define the opposition between agrarian and commercial visions of America's future",
            "His states' rights theory became one of the foundational intellectual sources of Southern sectionalism — the ideas he developed in the 1810s and 1820s were invoked by Southern secessionists in the 1860s"
        ],
        "relationships": [
            {"entity": "Thomas Jefferson (political ally)", "relationship": "CLOSEST_INTELLECTUAL_ALLY_AND_CORRESPONDENT_OF", "note": "Jefferson's most trusted political ally — Jefferson called Taylor's 'Inquiry' 'the most logical retraction of our principles that I have ever seen'"},
            {"entity": "'Inquiry into Principles and Policy of Government' (1814)", "relationship": "AUTHOR_OF", "note": "His systematic defense of agrarian republicanism and states' rights — the most rigorous theoretical foundation of Jeffersonian Democracy"},
            {"entity": "Alexander Hamilton's financial program (national bank, tariffs)", "relationship": "MOST_SYSTEMATIC_CRITIC_OF", "note": "His political philosophy was organized around the critique of Hamilton's national bank, protective tariffs, and commercial vision — opposing every element of Hamilton's economic program"},
            {"entity": "John C. Calhoun / Southern states' rights tradition", "relationship": "INTELLECTUAL_PREDECESSOR_OF", "note": "His states' rights theory was the foundational intellectual source for Calhoun's nullification doctrine and the broader Southern sectionalist tradition"},
            {"entity": "Agrarian republicanism (Jeffersonian political tradition)", "relationship": "MOST_SYSTEMATIC_THEORIST_OF", "note": "The most rigorous theoretical defender of agrarian republicanism — the vision of America as a republic of independent farmers rather than merchants and manufacturers"}
        ]
    }),

    # 3 — George Jones
    ("george-jones", {
        "summary": (
            "George Jones (1766–1838) was an American Revolutionary War veteran, "
            "physician, and politician from Savannah, Georgia, who served as a "
            "United States Senator from Georgia (1807–1813). A native of Savannah "
            "who trained in medicine under his father and practiced for years "
            "before entering politics, Jones had served in the Continental Army "
            "during the Revolutionary War — including being captured by the "
            "British — before returning to Georgia as part of the physician-politician "
            "class that dominated the founding-era Southern states.\n\n"
            "His Senate career (1807–1813) coincided with one of the most "
            "consequential periods in early American history: the Chesapeake-Leopard "
            "Affair (1807) that inflamed American-British relations, Jefferson's "
            "Embargo Act (1807–1809) that devastated coastal trade, Madison's "
            "movement toward war with Britain, and the early months of the War "
            "of 1812. Georgia's maritime and commercial interests gave Jones "
            "a distinct perspective on these British-American crises — Georgia's "
            "coast and Savannah's port were directly affected by British "
            "impressment and trade restrictions.\n\n"
            "He was part of the Democratic-Republican political tradition that "
            "dominated Georgia's early national politics — a state with strong "
            "planter and commercial interests tied to the Atlantic economy. "
            "His Revolutionary War credentials and his medical standing gave "
            "him the social capital necessary for Georgia's Senate seat.\n\n"
            "After his Senate career, Jones returned to Savannah and medical "
            "practice — ending a career that reflected the physician-statesman "
            "tradition of founding-era Southern politics."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Georgia US Senator (1807–1813) and Revolutionary War veteran; physician-politician from Savannah; served during the Chesapeake-Leopard Affair, Jefferson's Embargo, and the lead-up to the War of 1812.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His Revolutionary War service — including capture by the British — established the patriot credentials that gave him standing in Georgia's post-revolutionary political community",
            "Savannah's position as a major Atlantic port — and Georgia's commercial ties to Britain — made the British-American crisis of 1807-1812 directly relevant to his senatorial constituency",
            "Georgia's Democratic-Republican political culture and its planter-commercial elite created the political environment in which a physician with strong Revolutionary War credentials could rise to the Senate"
        ],
        "effects": [
            "His Senate service provided Georgia's representation in Washington during the critical period of the Chesapeake crisis, the Embargo Act, and the lead-up to the War of 1812 — when the nation's relationship with Britain was rapidly deteriorating",
            "His advocacy as a Georgian senator — representing a state with major Atlantic coast interests — contributed to the sectional nuances of the debate over Jefferson's Embargo and Madison's war policy",
            "His career demonstrated the physician-statesman tradition of the founding era — in which medical training provided the intellectual foundation for political service in the early republic",
            "His return to Savannah after his Senate career reflected the pattern of early American politicians who alternated between professional practice and legislative service"
        ],
        "relationships": [
            {"entity": "US Senate from Georgia (1807–1813)", "relationship": "SENATOR", "note": "Served as US Senator from Georgia (1807–1813) during the critical period of the Chesapeake crisis, Jefferson's Embargo, and the lead-up to the War of 1812"},
            {"entity": "Revolutionary War / Continental Army (Georgia)", "relationship": "VETERAN_CAPTURED_BY_BRITISH_IN", "note": "Served in the Continental Army during the Revolutionary War — including being captured by the British — establishing his patriot credentials for Georgia politics"},
            {"entity": "Jefferson's Embargo Act (1807–1809)", "relationship": "SENATOR_DURING_DEBATE_OVER", "note": "Served in the Senate during Jefferson's Embargo Act — which devastated Savannah's maritime trade and directly affected his Georgia constituency"},
            {"entity": "Savannah, Georgia (Patriot/physician/political community)", "relationship": "LEADING_FIGURE_OF", "note": "A native of Savannah whose medical practice and Revolutionary War service gave him the social standing for Georgia's Senate seat"},
            {"entity": "Chesapeake-Leopard Affair (1807) / War of 1812 lead-up", "relationship": "SENATOR_DURING", "note": "His Senate career coincided with the Chesapeake crisis and the British-American tensions that led to the War of 1812"}
        ]
    }),

    # 4 — Charles A. Wickliffe
    ("charles-a-wickliffe", {
        "summary": (
            "Charles Anderson Wickliffe (1788–1869) was a Kentucky lawyer and "
            "Whig politician who served as the 11th United States Postmaster "
            "General (1841–1845) under Presidents Tyler and Fillmore, as the "
            "14th Governor of Kentucky (1839–1840), and as a US Representative "
            "from Kentucky across multiple non-consecutive terms (1823–1833, "
            "1861–1863). His career illustrated the staying power of the "
            "Kentucky Whig political tradition — surviving the Whig Party's "
            "collapse to extend into the Civil War era.\n\n"
            "Wickliffe was a significant figure in Kentucky's complex Civil War "
            "politics: as a border state that stayed in the Union while harboring "
            "strong Confederate sympathies and a substantial slaveholder population, "
            "Kentucky's politics during the war was a constant balancing act between "
            "Union loyalty and Southern rights. Wickliffe's late congressional "
            "career (1861–1863) placed him in this difficult position — he was "
            "a Unionist who was deeply skeptical of Lincoln's emancipation "
            "policies.\n\n"
            "Before the Civil War, his postmaster generalship (1841–1845) was one "
            "of the most consequential positions in the federal government: the "
            "Post Office was the largest federal employer and the primary vehicle "
            "for federal presence across the country. Managing it across the "
            "Tyler administration — which had broken with the Whig Party — "
            "required significant political skill.\n\n"
            "He also served as Speaker of the Kentucky House of Representatives "
            "and as a Lieutenant Governor — building a career that touched every "
            "level of Kentucky's political institutions."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky Whig Postmaster General (1841–1845); Governor of Kentucky (1839–1840); multi-term US Representative; Speaker of Kentucky House; a significant border-state figure in Kentucky's complex Civil War politics — Unionist but deeply skeptical of Lincoln's emancipation policies.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Kentucky's unique Whig political culture — descended from Henry Clay's tradition — created the political environment for Wickliffe's long career across multiple offices",
            "The Tyler administration's break with the Whig Party — Tyler's vetoes of Whig legislation — created the unusual political context in which Wickliffe served as Postmaster General under a president without a party",
            "Kentucky's border-state position in the Civil War — balancing Union loyalty with slaveholder interests — created the complex political environment of Wickliffe's late congressional career"
        ],
        "effects": [
            "His postmaster generalship contributed to the management of the federal government's largest employer during the critical Tyler administration period — when the Whig Party's normal governance structure had broken down",
            "His Civil War congressional service contributed to the Kentucky Unionist bloc that kept the state formally in the Union — while resisting Lincoln's emancipation policies from within that Unionist framework",
            "His governorship contributed to Kentucky's political development in the critical period between the Bank War's resolution and the emergence of the slavery expansion controversy",
            "His long legislative career — spanning from the 1820s to the 1860s — made him one of the most experienced politicians in Kentucky's history, connecting the Whig era to the Civil War"
        ],
        "relationships": [
            {"entity": "US Postmaster General (1841–1845)", "relationship": "SERVED_AS", "note": "Served as 11th US Postmaster General under Tyler — managing the federal government's largest employer during the unusual period of a president without a party"},
            {"entity": "Kentucky governorship (1839–1840)", "relationship": "14TH_GOVERNOR", "note": "Served as 14th Governor of Kentucky (1839–1840) — the executive position in one of the most important border states"},
            {"entity": "John Tyler administration (Whig-to-no-party president)", "relationship": "POSTMASTER_GENERAL_DURING_UNUSUAL_POLITICS_OF", "note": "Served under Tyler — who had broken with the Whig Party — navigating the unusual political landscape of a president without congressional party support"},
            {"entity": "Kentucky Civil War border-state politics", "relationship": "CONGRESSIONAL_REPRESENTATIVE_IN", "note": "His 1861–1863 House term placed him in Kentucky's complex border-state politics — Unionist but skeptical of Lincoln's emancipation policies"},
            {"entity": "Henry Clay / Kentucky Whig tradition", "relationship": "POLITICAL_INHERITOR_OF", "note": "Part of the Kentucky Whig tradition descended from Henry Clay — maintaining that political identity across the Whig era and into the Civil War period"}
        ]
    }),

    # 5 — William Pope Duval
    ("william-pope-duval", {
        "summary": (
            "William Pope Duval (1784–1854) was an American lawyer, politician, "
            "and territorial governor who served as the first civilian Governor "
            "of Florida Territory (1822–1834) — the longest-serving governor "
            "in Florida's territorial history, leading the territory for twelve "
            "consecutive years through its critical early period of American "
            "governance. He succeeded Andrew Jackson, who had served as the "
            "brief military governor, and built the civilian government of "
            "Florida from almost nothing: establishing courts, a legislature, "
            "a legal system, and the machinery of territorial administration.\n\n"
            "Duval's Florida governorship was complicated by the ongoing "
            "tensions with the Seminole people, who occupied much of the "
            "territory's interior and who would eventually resist removal "
            "in the Second Seminole War (1835–1842). During his tenure, "
            "he negotiated the Treaty of Moultrie Creek (1823) — which "
            "confined the Seminoles to a reservation in central Florida "
            "in exchange for peace — a treaty that was eventually repudiated "
            "when the federal government demanded full removal to the West.\n\n"
            "He was a colorful frontier figure whose exploits captured the "
            "imagination of Washington Irving — the author of 'The Legend of "
            "Sleepy Hollow' and 'Rip Van Winkle' — who modeled his literary "
            "character Ralph Ringwood after Duval and celebrated him in "
            "multiple essays. Duval was also a Kentucky Congressman (1813–1815) "
            "and a US District Judge before his Florida appointment.\n\n"
            "Duval County, Florida — the county in which Jacksonville is located "
            "— is named in his honor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First civilian Governor of Florida Territory (1822–1834) — 12 years; built Florida's civilian government from scratch; negotiated Treaty of Moultrie Creek (1823) with Seminoles; the basis for Washington Irving's literary character Ralph Ringwood; Duval County (Jacksonville) named for him.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Adams-Onís Treaty (1819) that transferred Florida from Spain to the United States created the territorial governance requirement — and Duval's legal and political experience (Kentucky congressman, federal judge) made him a suitable appointment for the first civilian governor",
            "The Seminole people's continued presence in Florida — and the federal government's demand for their confinement and eventual removal — created the most challenging governance problem of Duval's long territorial tenure",
            "The almost complete absence of American civilian institutions in Florida at the start of his governorship — the territory having been under Spanish and then military governance — created the institution-building challenge that defined his twelve years"
        ],
        "effects": [
            "His twelve-year governorship built Florida's civilian government from nearly nothing — establishing courts, a legislature, county governments, and the administrative machinery of territorial governance",
            "The Treaty of Moultrie Creek (1823) — which he negotiated — temporarily confined the Seminoles to a central Florida reservation, providing a decade of relative peace before the Second Seminole War began in 1835",
            "Duval County — containing Jacksonville, Florida's largest city — preserves his memory as the most consequential single contribution to Florida's political geography",
            "Washington Irving's literary portrayal of Duval as Ralph Ringwood gave the frontier governor a cultural legacy that extended well beyond Florida's political history"
        ],
        "relationships": [
            {"entity": "Florida Territory governorship (1822–1834)", "relationship": "FIRST_CIVILIAN_AND_LONGEST-SERVING_GOVERNOR", "note": "Served as first civilian Governor of Florida Territory for 12 years — building the territory's civilian institutions from almost nothing after Jackson's brief military governorship"},
            {"entity": "Treaty of Moultrie Creek (1823)", "relationship": "NEGOTIATOR_OF", "note": "Negotiated the Treaty of Moultrie Creek — which confined the Seminoles to a central Florida reservation in exchange for peace — providing a decade of relative peace before the Second Seminole War"},
            {"entity": "Washington Irving (author)", "relationship": "LITERARY_MODEL_FOR_RALPH_RINGWOOD_CHARACTER_OF", "note": "Irving modeled his literary character Ralph Ringwood after Duval — celebrating the frontier governor's colorful exploits in multiple essays"},
            {"entity": "Seminole people / Seminole removal crisis", "relationship": "FLORIDA_GOVERNOR_MANAGING_TENSIONS_WITH", "note": "His governorship was complicated by ongoing tensions with the Seminoles — whom he tried to manage through the Moultrie Creek Treaty before the removal pressure escalated"},
            {"entity": "Duval County, Florida (Jacksonville)", "relationship": "NAMESAKE_OF", "note": "Duval County — containing Jacksonville, Florida's largest city — is named in his honor, preserving his memory as the territory's founding civilian governor"}
        ]
    }),

    # 6 — James Burrill Jr.
    ("james-burrill-jr", {
        "summary": (
            "James Burrill Jr. (1772–1820) was a Rhode Island Federalist lawyer, "
            "jurist, and senator who served as Chief Justice of the Rhode Island "
            "Supreme Court (1816–1817) and as a United States Senator (1817–1820) "
            "— dying in office after less than three years in the Senate. A Brown "
            "University graduate and a distinguished Rhode Island attorney, "
            "Burrill was known for his scholarly legal mind and his eloquent "
            "advocacy — building a reputation as one of the leading lawyers "
            "in New England before his elevation to the Senate.\n\n"
            "His brief Senate career was marked by a significant anti-slavery "
            "position: he was one of the most outspoken opponents of Missouri's "
            "admission as a slave state in the debates that preceded the Missouri "
            "Compromise of 1820. In his Senate speeches against slavery's expansion, "
            "Burrill argued with unusual force for a Federalist — combining "
            "moral condemnation of slavery with constitutional arguments against "
            "Congress's power to admit new slave states without restriction.\n\n"
            "Burrill's death in December 1820 — just as the Missouri Compromise "
            "was being finalized — came at the very moment when his anti-slavery "
            "voice would have been most consequential. He died before the "
            "Compromise was enacted, and his Senate seat passed to a less "
            "outspoken successor.\n\n"
            "His career reflected the Federalist intellectual tradition — "
            "scholarly, principled, and increasingly isolated in the "
            "Democratic-Republican era — that found one of its final expressions "
            "in the Missouri debates."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Rhode Island Federalist senator (1817–1820) who was one of the most outspoken anti-slavery voices in the Missouri Compromise debates; Chief Justice of the Rhode Island Supreme Court (1816–1817); Brown University graduate; died in office December 1820.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's Federalist legal culture — and its tradition of educated, scholarly attorneys — created the professional environment in which Burrill's legal reputation was built",
            "Missouri's application for statehood as a slave state — creating the Missouri Crisis of 1820 — provided the Senate moment in which Burrill's anti-slavery position found its most consequential expression",
            "The Federalist Party's gradual decline — and its increasing alignment with anti-slavery positions in the late 1810s — created the political context for Burrill's unusually outspoken anti-slavery advocacy"
        ],
        "effects": [
            "His anti-slavery Senate speeches in the Missouri debates contributed to the intellectual and moral case against slavery's expansion — even as the eventual Compromise allowed Missouri to enter as a slave state",
            "His death in December 1820 — at the precise moment when his voice was most consequential — removed one of the most articulate anti-slavery Senate voices just as the final Missouri Compromise terms were being agreed",
            "His Rhode Island Chief Justice tenure contributed to the development of Rhode Island's legal system during the critical post-War of 1812 period",
            "His career illustrated the final phase of Federalist legal culture — scholarly, morally principled, increasingly outnumbered — that found in the Missouri debates its most eloquent expression before the party's effective dissolution"
        ],
        "relationships": [
            {"entity": "Missouri Compromise debates (1820)", "relationship": "MOST_OUTSPOKEN_SENATE_OPPONENT_OF_SLAVERY_EXPANSION_IN", "note": "One of the most outspoken Federalist anti-slavery voices in the Missouri Compromise debates — arguing against Missouri's admission as a slave state"},
            {"entity": "Rhode Island Supreme Court (Chief Justice, 1816–1817)", "relationship": "CHIEF_JUSTICE", "note": "Served as Chief Justice of the Rhode Island Supreme Court (1816–1817) before his Senate elevation"},
            {"entity": "US Senate from Rhode Island (1817–1820)", "relationship": "SENATOR_WHO_DIED_IN_OFFICE", "note": "Served as US Senator from Rhode Island (1817–1820) — dying in office in December 1820, just as the Missouri Compromise was being finalized"},
            {"entity": "Brown University (Providence, RI)", "relationship": "ALUMNUS_OF", "note": "Brown University graduate whose legal scholarship gave him the intellectual foundation for his distinguished Rhode Island legal career"},
            {"entity": "Federalist legal tradition (late period)", "relationship": "FINAL_REPRESENTATIVE_OF_IN_SENATE", "note": "His career illustrated the final expression of Federalist legal culture — scholarly, principled, increasingly isolated — in the Missouri debate before the party's effective dissolution"}
        ]
    }),

    # 7 — Augustus Baldwin Longstreet
    ("augustus-baldwin-longstreet", {
        "summary": (
            "Augustus Baldwin Longstreet (1790–1870) was a Georgia lawyer, minister, "
            "journalist, educator, and humorist whose book 'Georgia Scenes, Characters, "
            "Incidents, etc. in the First Half Century of the Republic' (1835) was "
            "one of the foundational texts of American frontier humor and regionalist "
            "literature — the direct predecessor of the Southwestern Humor tradition "
            "that influenced Mark Twain, Bret Harte, and the broader tradition of "
            "American vernacular comedy. Edgar Allan Poe praised 'Georgia Scenes' "
            "extravagantly, calling it 'a sure omen of better days for the Southern "
            "literature' and a work of 'much merit and much popularity.'\n\n"
            "Longstreet's remarkable career combined his literary achievement with "
            "service as a Georgia Superior Court judge (1822–1825), a Methodist "
            "minister, a newspaper editor (the Augusta State Rights Sentinel), "
            "and the president of four colleges: Emory College (1839–1848), "
            "Centenary College (1849), University of Mississippi (1849–1856), "
            "and the University of South Carolina (1857–1865). This extraordinary "
            "range of roles — lawyer, judge, minister, author, journalist, college "
            "president — illustrated the multiple identities that educated "
            "antebellum Southerners could inhabit.\n\n"
            "He was also a fierce defender of slavery and Southern secessionism: "
            "he publicly advocated for secession and opposed abolitionism throughout "
            "his later career, and he supported the Confederacy during the Civil War "
            "— a political alignment that cast a dark shadow over his literary legacy.\n\n"
            "His humor, however, preserved the voices and characters of the "
            "early Georgia frontier with remarkable specificity — making 'Georgia "
            "Scenes' an irreplaceable record of antebellum Southern folk culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Author of 'Georgia Scenes' (1835) — the foundational text of American Southwestern Humor and a direct influence on Mark Twain; Georgia Superior Court judge; Methodist minister; president of Emory, Centenary, Mississippi, and South Carolina colleges; fierce pro-slavery and secessionist advocate.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The distinctive oral culture of early Georgia's frontier communities — the horse races, militia musters, gander-pulling, and vernacular characters that Longstreet observed — provided the raw material for 'Georgia Scenes'",
            "Edgar Allan Poe's enthusiastic review — calling 'Georgia Scenes' an omen of better Southern literature — contributed to the book's national reputation and its influence on subsequent American humor writers",
            "The antebellum Southern educational establishment's need for institution-builders who could combine intellectual prestige with doctrinal reliability — Longstreet's combination of literary reputation, Methodist ministry, and pro-slavery orthodoxy made him an ideal college president for Southern institutions"
        ],
        "effects": [
            "His 'Georgia Scenes' established the Southwestern Humor tradition that directly influenced Mark Twain and the broader American vernacular comedy tradition — making Longstreet the foundational figure for American literary regionalism",
            "His four college presidencies contributed to the development of Southern higher education in the antebellum period — building institutions that shaped generations of Southern professional men",
            "His pro-slavery and secessionist advocacy — particularly in his Augusta State Rights Sentinel editorials — contributed to the intellectual foundation of Southern secessionism",
            "His literary legacy created an irreconcilable tension between his contribution to American literature and his defense of slavery — making him one of the most complex figures in antebellum Southern cultural history"
        ],
        "relationships": [
            {"entity": "'Georgia Scenes' (1835)", "relationship": "AUTHOR_OF", "note": "Author of 'Georgia Scenes' — the foundational text of American Southwestern Humor and a direct predecessor of Mark Twain's vernacular comedy tradition"},
            {"entity": "Mark Twain / Southwestern Humor tradition", "relationship": "LITERARY_PREDECESSOR_OF", "note": "His 'Georgia Scenes' established the Southwestern Humor tradition that directly influenced Mark Twain, Bret Harte, and American vernacular comedy"},
            {"entity": "Emory College / University of Mississippi / South Carolina colleges", "relationship": "PRESIDENT_OF_FOUR", "note": "Served as president of Emory College, Centenary College, University of Mississippi, and University of South Carolina — contributing to Southern higher education"},
            {"entity": "Edgar Allan Poe", "relationship": "ENTHUSIASTICALLY_REVIEWED_BY", "note": "Poe praised 'Georgia Scenes' as 'a sure omen of better days for Southern literature' — contributing to Longstreet's national literary reputation"},
            {"entity": "Southern secessionism / pro-slavery advocacy", "relationship": "PUBLIC_CHAMPION_OF", "note": "A fierce defender of slavery and Southern secession — his Augusta State Rights Sentinel editorials contributed to the intellectual foundation of Southern secessionism"}
        ]
    }),

    # 8 — Truman Smith
    ("truman-smith", {
        "summary": (
            "Truman Smith (1791–1884) was a Connecticut Whig lawyer and politician "
            "who served as a US Representative (1839–1843, 1845–1849) and as a "
            "US Senator (1849–1854) — and who is historically notable as one "
            "of the most effective Whig Party political organizers of the "
            "mid-19th century and as an early opponent of slavery's expansion "
            "whose political evolution helped pave the way for the Republican "
            "Party's formation in Connecticut. He is also notable for his "
            "extraordinary longevity — living to 93, one of the oldest "
            "19th-century American politicians — and dying in 1884 after "
            "witnessing the Civil War, Reconstruction, and the Gilded Age.\n\n"
            "Smith was one of the Whig Party's most skilled national organizers — "
            "serving as a de facto Whig campaign manager during the 1840s and "
            "contributing to the party's organizational infrastructure. He "
            "was deeply involved in the political debates over slavery's "
            "expansion that consumed the late Whig Party and eventually "
            "produced its collapse and the Republican Party's rise.\n\n"
            "His Senate career (1849–1854) coincided with the Compromise of "
            "1850 and the debates that defined the Whig Party's final years "
            "— as Northern and Southern Whigs increasingly split over slavery "
            "questions. His resignation from the Senate in 1854 — after the "
            "Kansas-Nebraska Act repealed the Missouri Compromise line — "
            "reflected the collapse of the Whig framework that had sustained "
            "his political career.\n\n"
            "He subsequently became a federal judge in New York."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Whig US Representative and Senator (1849–1854); one of the Whig Party's most effective national political organizers; resigned from the Senate after the Kansas-Nebraska Act (1854) destroyed the Whig framework; lived to 93 — one of the oldest 19th-century American politicians.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Whig political culture — and the party's need for skilled organizers who could manage national campaigns — created the political role that made Smith one of the most effective Whig political operatives of the 1840s",
            "The slavery expansion crisis — the Compromise of 1850, the Kansas-Nebraska Act, and the subsequent Whig collapse — created the political earthquake that ended Smith's Senate career and pushed him toward the emerging Republican coalition",
            "The Whig Party's organizational needs for the Harrison, Taylor, and Fillmore campaigns required skilled political managers whose work shaped the party's national strategy"
        ],
        "effects": [
            "His Whig organizational work contributed to the party's campaign infrastructure during the 1840s — one of the Whig Party's most successful electoral decades",
            "His resignation from the Senate after the Kansas-Nebraska Act (1854) contributed to the narrative of Northern Whig collapse — illustrating how the Act destroyed the Northern Whig political framework",
            "His subsequent federal judgeship contributed to New York's federal legal system — extending his public career beyond the end of his political party",
            "His extraordinary longevity — surviving to 1884, living through the entire antebellum, Civil War, Reconstruction, and Gilded Age periods — made him one of the most historically continuous observers of 19th-century American political change"
        ],
        "relationships": [
            {"entity": "Whig Party (national organizational infrastructure)", "relationship": "MOST_EFFECTIVE_POLITICAL_ORGANIZER_OF", "note": "One of the Whig Party's most skilled national political organizers — serving as de facto campaign manager for Whig presidential campaigns in the 1840s"},
            {"entity": "Kansas-Nebraska Act (1854)", "relationship": "RESIGNED_FROM_SENATE_AFTER_REPEAL_OF_COMPROMISE_BY", "note": "Resigned from the Senate in 1854 after the Kansas-Nebraska Act repealed the Missouri Compromise line — reflecting the collapse of the Whig framework"},
            {"entity": "Compromise of 1850", "relationship": "SENATOR_DURING_DEBATE_OVER", "note": "His Senate career (1849–1854) coincided with the Compromise of 1850 and the debates that defined the Whig Party's final years"},
            {"entity": "US Senate from Connecticut (1849–1854)", "relationship": "SENATOR", "note": "Served as Connecticut's US Senator (1849–1854) during the last years of the Whig Party's existence"},
            {"entity": "Republican Party formation (1854–1856)", "relationship": "EARLY_PROPONENT_AND_TRANSITION_FIGURE_TOWARD", "note": "His resignation from the Senate in 1854 and his anti-slavery evolution made him part of the Northern Whig transition toward the emerging Republican Party"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 34)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
