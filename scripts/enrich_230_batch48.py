#!/usr/bin/env python3
"""
Batch 48 — 8 entities: Alexander J. Dallas, José de Gálvez, St. George Tucker,
Gabriel Duvall, Christopher Greenup, Thaddeus Betts,
John Mathews, Antoine Barnave
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

    # 1 — Alexander J. Dallas
    ("alexander-j-dallas", {
        "summary": (
            "Alexander James Dallas (1759–1817) was a "
            "Jamaica-born Pennsylvania lawyer, journalist, "
            "and statesman who served in three pivotal "
            "federal roles: as the 1st Reporter of "
            "Decisions of the US Supreme Court "
            "(1790–1800, producing 4 volumes of "
            "'Dallas Reports'), as US Attorney for "
            "the Eastern District of Pennsylvania "
            "(1801–1814), and as the 6th Secretary "
            "of the Treasury (1814–1816) under "
            "President James Madison — his most "
            "consequential posting, during which "
            "he rebuilt the nation's finances "
            "following the War of 1812.\n\n"
            "His Treasury secretaryship came at "
            "the most acute fiscal crisis of the "
            "early republic: the War of 1812 had "
            "left the United States nearly bankrupt, "
            "the First Bank of the United States "
            "had been allowed to expire, and "
            "the government could barely meet "
            "its obligations. Dallas developed "
            "the financial plan that included "
            "a new national bank — the Second "
            "Bank of the United States, chartered "
            "in 1816 — and restructured the "
            "government's revenue and debt "
            "management to place federal "
            "finances on a sustainable footing.\n\n"
            "His four volumes of Dallas Reports — "
            "produced during his decade as the "
            "Court's first Reporter of Decisions — "
            "constituted the first published "
            "record of US Supreme Court decisions, "
            "giving American lawyers and judges "
            "their first systematic access "
            "to federal constitutional jurisprudence. "
            "They remain cited in modern law.\n\n"
            "His son, George Mifflin Dallas, "
            "subsequently served as Vice "
            "President of the United States "
            "(1845–1849) under Polk — "
            "the city of Dallas, Texas "
            "bearing the family name."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "1st Reporter of Decisions, US Supreme Court (1790–1800, 4 volumes 'Dallas Reports' — first published SCOTUS decisions); 6th Secretary of the Treasury (1814–1816, designed the Second Bank of the US chartered 1816 and rebuilt post-War of 1812 finances); US Attorney Eastern District PA; Jamaica-born Pennsylvania lawyer; father of VP George Mifflin Dallas (namesake of Dallas, Texas).",
            "significanceCategory": "regional"
        },
        "causes": [
            "The new federal judiciary's need for systematic documentation of US Supreme Court decisions — in an era before official federal publication — created the Reporter of Decisions position that Dallas filled for a decade, his four volumes providing American lawyers with their first organized access to constitutional jurisprudence",
            "The War of 1812's catastrophic fiscal consequences — leaving the United States nearly bankrupt, the First Bank of the United States expired, and federal finances unable to meet basic obligations — created the emergency that required Dallas's Treasury secretaryship and his comprehensive financial reconstruction plan",
            "Madison's recognition that the fiscal crisis demanded a capable financial technician rather than a purely political appointment — and Dallas's reputation as the most able financial lawyer in Philadelphia, the nation's commercial center — made him the natural choice for the Treasury post at its most critical moment"
        ],
        "effects": [
            "His design of the Second Bank of the United States — chartered in 1816 — contributed to stabilizing American federal finances after the War of 1812 and establishing a national banking architecture that would govern American monetary policy for the next two decades until Andrew Jackson's destruction of the Bank in the 1830s",
            "His Dallas Reports (4 volumes, 1790–1800) constituted the first published record of US Supreme Court decisions — giving American lawyers and judges systematic access to federal constitutional jurisprudence for the first time and establishing the precedent of regular court reporting that became the standard for all subsequent volumes",
            "His Treasury secretaryship's post-war fiscal reconstruction contributed to the United States' recovery from the War of 1812's financial devastation — developing the revenue and debt management framework that placed federal finances on a sustainable footing for the Era of Good Feelings' economic expansion",
            "His family's legacy through his son George Mifflin Dallas — Vice President under Polk (1845–1849) and namesake of Dallas, Texas — extended the Dallas name's historical significance beyond his own career into the geography and politics of the expanding American West"
        ],
        "relationships": [
            {"entity": "1st Reporter of Decisions, US Supreme Court (1790–1800, Dallas Reports)", "relationship": "FIRST_REPORTER_OF_DECISIONS", "note": "Served as the first Reporter of Decisions of the US Supreme Court (1790–1800) — producing four volumes of Dallas Reports that constituted the first published record of American constitutional jurisprudence"},
            {"entity": "6th Secretary of the Treasury (1814–1816, Madison administration)", "relationship": "SECRETARY_OF_THE_TREASURY", "note": "Served as Madison's Secretary of the Treasury (1814–1816) — designing the Second Bank of the US and rebuilding federal finances after the War of 1812's catastrophic fiscal consequences"},
            {"entity": "Second Bank of the United States (chartered 1816, Dallas's design)", "relationship": "DESIGNER_AND_ARCHITECT_OF", "note": "Designed the legislative and financial plan for the Second Bank of the United States (chartered 1816) — the national banking architecture that stabilized American monetary policy after the War of 1812"},
            {"entity": "War of 1812 fiscal crisis / US Treasury Department reconstruction", "relationship": "TREASURY_SECRETARY_WHO_REBUILT_FINANCES_AFTER", "note": "The Treasury Secretary who rebuilt federal finances after the War of 1812 — America's most acute fiscal crisis since the Revolution, which had left the government nearly bankrupt"},
            {"entity": "George Mifflin Dallas (son, US Vice President 1845–1849, namesake of Dallas TX)", "relationship": "FATHER_OF", "note": "Father of George Mifflin Dallas — Vice President under Polk (1845–1849) and the figure for whom Dallas, Texas is named, extending the family's historical significance into American geography"}
        ]
    }),

    # 2 — José de Gálvez
    ("josé-de-gálvez", {
        "summary": (
            "José de Gálvez y Gallardo, 1st Marquess "
            "of Sonora (1720–1787), was a Spanish "
            "lawyer and colonial administrator who "
            "served as Visitador General of New Spain "
            "(1764–1772) and as Minister of the Indies "
            "(1775–1787) — the two roles that made "
            "him the principal architect of Spain's "
            "18th-century Bourbon Reforms in "
            "the Americas, the most ambitious "
            "restructuring of Spanish colonial "
            "governance since the conquest.\n\n"
            "His Visitaduría of New Spain transformed "
            "the colonial administration: he reorganized "
            "the tax collection system to dramatically "
            "increase revenue, expelled the Jesuit "
            "order from the entire Spanish colonial "
            "world (1767, executing the crown's "
            "order throughout New Spain), militarized "
            "the northern frontier by creating the "
            "Comandancia General of the Provincias "
            "Internas (covering present-day northern "
            "Mexico and the American Southwest), "
            "and drove the settlement of Alta "
            "California — sending the Portolá "
            "expedition (1769) that established "
            "the first Spanish missions and "
            "presidios in California.\n\n"
            "As Minister of the Indies — effectively "
            "Spain's colonial minister for all "
            "of Spanish America — he extended "
            "the Bourbon Reforms across the "
            "entire empire, creating new "
            "intendancy systems, reorganizing "
            "commercial regulations, and "
            "attempting to make the colonies "
            "more profitable and defensible. "
            "He came from a politically powerful "
            "family: his brother Matías governed "
            "Guatemala and New Spain; his nephew "
            "Bernardo de Gálvez, Governor of "
            "Louisiana, fought the British "
            "during the American Revolution.\n\n"
            "'The greatest achievement of "
            "18th-century Spanish colonial "
            "reform' — historians have "
            "described his Bourbon "
            "administrative revolution as "
            "transforming Spain's imperial "
            "capacity, even if it arrived "
            "too late to prevent eventual "
            "independence movements."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Visitador General of New Spain (1764–1772); Minister of the Indies (1775–1787); principal architect of Spain's Bourbon Reforms in the Americas; expelled the Jesuits from New Spain (1767); created the Comandancia General of the Provincias Internas; drove the settlement of Alta California (Portolá expedition 1769); from the prominent Gálvez political family including nephew Bernardo de Gálvez; his reforms represented the most ambitious restructuring of Spanish colonial governance in two centuries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Spain's mid-18th-century imperial crisis — the Seven Years' War's demonstration that the British Empire had surpassed Spanish colonial power in both military capacity and commercial organization — created the urgency for the Bourbon Reforms that Gálvez implemented, as the Spanish crown recognized that its colonial system needed fundamental restructuring to remain competitive",
            "The Bourbon dynasty's determination to extend the French model of rational, centralized absolutist administration to the Spanish colonial system — replacing the older Habsburg administrative framework with a more efficient, revenue-maximizing structure — created the ideological framework for the reforms Gálvez drove as Visitador and Minister",
            "The specific threats to Spain's northern colonial frontier — British expansion from the east, Russian exploration from the north (Alaska), and the need to secure California and the Mississippi Valley — created the strategic imperatives that shaped Gálvez's militarization of the Provincias Internas and the California settlement program"
        ],
        "effects": [
            "His expulsion of the Jesuits from New Spain (1767) contributed to one of the most dramatic institutional transformations in Spanish colonial history — removing the most powerful independent religious order from the Americas, seizing their missions and properties, and dramatically altering the religious and educational landscape of colonial Spanish America",
            "His creation of the Comandancia General of the Provincias Internas contributed to the militarization and administrative reorganization of Spain's northern frontier — establishing the governing structure for the vast territories of northern Mexico and the American Southwest that would shape the region's political development for decades",
            "The Portolá expedition he organized (1769) contributed to Spain's settlement of Alta California — establishing the first missions, presidios, and pueblos in present-day California and creating the Spanish colonial framework that persisted until California's admission to the United States in 1850",
            "His Minister of the Indies tenure contributed to the most comprehensive restructuring of Spain's American imperial administration since the conquest — the intendancy reforms, commercial reorganizations, and military upgrades that temporarily strengthened Spanish colonial governance, even as they generated the resentments that contributed to the independence movements of the early 19th century"
        ],
        "relationships": [
            {"entity": "Visitador General of New Spain (1764–1772, Bourbon Reforms in New Spain)", "relationship": "VISITADOR_GENERAL", "note": "Served as Visitador General of New Spain (1764–1772) — the principal architect of Spain's Bourbon Reforms in the most important colonial territory, reorganizing taxation, expelling the Jesuits, and militarizing the northern frontier"},
            {"entity": "Minister of the Indies (1775–1787) / Bourbon Reforms across Spanish America", "relationship": "MINISTER_OF_THE_INDIES", "note": "Served as Spain's Minister of the Indies (1775–1787) — extending the Bourbon Reforms across all of Spanish America, creating intendancy systems and commercial reorganizations that transformed imperial governance"},
            {"entity": "Jesuit expulsion from New Spain (1767) / suppression of Jesuit order in Spanish colonies", "relationship": "EXECUTOR_OF", "note": "Executed the crown's order expelling the Jesuits from New Spain in 1767 — one of the most dramatic institutional transformations in Spanish colonial history, removing the most powerful independent religious order from the Americas"},
            {"entity": "Portolá expedition (1769) / Alta California settlement program", "relationship": "ORGANIZER_OF", "note": "Organized the Portolá expedition (1769) that established Spain's first missions and presidios in Alta California — the founding event of California's Spanish colonial period"},
            {"entity": "Bernardo de Gálvez (nephew, Louisiana governor, fought British in American Revolution)", "relationship": "UNCLE_OF", "note": "Uncle of Bernardo de Gálvez — Louisiana's governor who fought the British during the American Revolution, the prominent Gálvez family's contribution to both colonial reform and American independence"}
        ]
    }),

    # 3 — St. George Tucker
    ("st-george-tucker", {
        "summary": (
            "St. George Tucker (1752–1827) was a "
            "Bermuda-born Virginia lawyer, jurist, "
            "law professor, and legal commentator "
            "whose most enduring contribution "
            "to American law was his annotated "
            "edition of Blackstone's Commentaries "
            "(1803) — 'Tucker's Blackstone' — "
            "the first major American commentary "
            "on English common law adapted for "
            "the new constitutional republic, "
            "and the leading American legal "
            "treatise of the early 19th century. "
            "Born in Bermuda to a merchant family, "
            "he studied law at the College of "
            "William & Mary and settled in Virginia.\n\n"
            "He taught law at William & Mary "
            "(1790–1804), where he trained "
            "a generation of Virginia lawyers "
            "and jurists — including Chief "
            "Justice John Marshall's law "
            "students — and systematically "
            "raised the academic standards "
            "for law degrees. His lectures "
            "formed the basis of his "
            "Blackstone commentaries.\n\n"
            "His judicial career included "
            "service on the Virginia Court "
            "of Appeals and as US District "
            "Judge for Virginia (1813–1825). "
            "His 1796 dissertation on "
            "slavery — appended to his "
            "Blackstone — was one of the "
            "earliest systematic constitutional "
            "arguments against slavery in "
            "the United States, arguing "
            "that slavery was irreconcilable "
            "with the natural rights principles "
            "of the Declaration of Independence.\n\n"
            "His stepson Henry St. George Tucker "
            "and grandson John Randolph Tucker "
            "continued the family's Virginia "
            "legal and political tradition — "
            "the Tucker family becoming one "
            "of Virginia's most distinguished "
            "legal dynasties."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Bermuda-born Virginia jurist; professor of law at College of William & Mary (1790–1804); author of Tucker's Blackstone (1803) — the first major American commentary on English common law for the new republic and the leading American legal treatise of the early 19th century; Virginia Court of Appeals; US District Judge for Virginia; early constitutional abolitionist argument in 1796 dissertation; trained a generation of Virginia lawyers including Marshall Court figures.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The new American republic's need for a legal treatise that could adapt English common law to the new constitutional framework — Blackstone's Commentaries, the standard English legal textbook, needed systematic annotation to show where American constitutional principles departed from English precedent — created the intellectual demand for Tucker's annotated edition",
            "Tucker's unique position as both a practicing lawyer, a law professor with direct teaching experience, and a jurist with court service gave him the combined theoretical and practical perspective needed to produce a comprehensive American legal commentary rather than simply reprinting the English original with minor notes",
            "Virginia's position as the early republic's most intellectually active legal community — with William & Mary's law program, the Virginia Court of Appeals, and the proximity to the federal courts — created the institutional environment from which Tucker's legal scholarship could emerge and influence American legal education nationally"
        ],
        "effects": [
            "His Tucker's Blackstone (1803) contributed to the systematic Americanization of English common law — providing American lawyers, judges, and legal students with the first comprehensive guide to how English legal principles applied, needed adaptation, or were superseded in the new constitutional republic",
            "His 1796 dissertation on slavery contributed to early American constitutional abolitionist thought — one of the first systematic arguments that slavery was irreconcilable with the natural rights principles of the Declaration of Independence, influencing antislavery legal arguments in the decades that followed",
            "His William & Mary law professorship contributed to the professional formation of a generation of Virginia lawyers — elevating the standards of legal education at a critical institution and training the judges and legislators who would shape Virginia's and America's legal development in the early 19th century",
            "His family's legal dynasty — extending through his stepson and grandson Tucker — contributed to the continuity of Virginia's legal tradition across multiple generations, making the Tucker family one of the most significant families in American legal history"
        ],
        "relationships": [
            {"entity": "Tucker's Blackstone (1803) — first American commentary on English common law", "relationship": "AUTHOR_OF", "note": "Authored Tucker's Blackstone (1803) — the annotated edition of Blackstone's Commentaries adapted for the American constitutional republic, the leading American legal treatise of the early 19th century"},
            {"entity": "College of William & Mary law program (professor and reformer, 1790–1804)", "relationship": "PROFESSOR_AND_REFORMER_AT", "note": "Taught law at William & Mary (1790–1804) — training a generation of Virginia lawyers and raising academic standards for law degrees, with his lectures forming the basis of his Blackstone commentaries"},
            {"entity": "Virginia Court of Appeals / US District Court Virginia (judge, 1813–1825)", "relationship": "JUDGE", "note": "Served as a judge on the Virginia Court of Appeals and as US District Judge for Virginia (1813–1825) — his combined judicial experience informing his legal scholarship"},
            {"entity": "1796 Dissertation on Slavery / early American constitutional abolitionism", "relationship": "AUTHOR_OF_EARLY_ANTISLAVERY_ARGUMENT", "note": "Wrote a 1796 dissertation on slavery appended to his Blackstone — one of the earliest systematic constitutional arguments that slavery was irreconcilable with the Declaration of Independence's natural rights principles"},
            {"entity": "Virginia legal dynasty (Tucker family — stepson Henry St. George Tucker, grandson John Randolph Tucker)", "relationship": "FOUNDING_FIGURE_OF", "note": "The founding figure of Virginia's Tucker legal dynasty — his stepson and grandson extending the family's legal and political tradition across multiple generations"}
        ]
    }),

    # 4 — Gabriel Duvall
    ("gabriel-duvall", {
        "summary": (
            "Gabriel Duvall (1752–1844) was a Maryland "
            "lawyer, politician, and jurist who served "
            "as an Associate Justice of the United "
            "States Supreme Court for 24 years "
            "(1811–1835) during the Marshall Court — "
            "one of the longest tenures on the Court "
            "in that era, and extraordinary for "
            "having ended when Duvall was 82 years "
            "old. His nearly 92-year lifespan made "
            "him one of the longest-lived figures "
            "in American constitutional history.\n\n"
            "Before his Supreme Court appointment "
            "by President Madison, he had a substantial "
            "political career: he served in the "
            "Maryland state legislature, as a "
            "Maryland state court judge, as a "
            "US Representative from Maryland "
            "(1794–1796), and as Comptroller "
            "of the Treasury (1802–1811) — "
            "a nine-year tenure managing federal "
            "financial oversight during the "
            "Jefferson and Madison administrations.\n\n"
            "On the Supreme Court, he served "
            "alongside Chief Justice John Marshall "
            "through the Court's foundational "
            "period of constitutional development — "
            "though he wrote relatively few opinions "
            "and is not remembered as a particularly "
            "independent doctrinal voice. His most "
            "notable individual position was his "
            "consistent support for the rights "
            "of free Black people in property "
            "and manumission cases — a "
            "distinctly progressive stance "
            "for a Maryland slaveholder.\n\n"
            "His 24-year Supreme Court tenure "
            "and his extraordinary longevity "
            "gave him a career arc spanning "
            "the full breadth of the early "
            "American republic — from the "
            "American Revolution through "
            "the Age of Jackson."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Associate Justice of the US Supreme Court (1811–1835, 24 years, Marshall Court); Comptroller of the Treasury (1802–1811); Maryland US Representative; Maryland state judge and legislator; nearly 92-year lifespan; progressive in manumission/free Black rights cases despite being a Maryland slaveholder; his 24-year Marshall Court tenure made him a consistent if quiet presence during American constitutional law's foundational period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "President Madison's need for Supreme Court appointments that would support the Marshall Court's constitutional direction — and Duvall's record as a loyal Democratic-Republican with legal experience in both state courts and federal financial administration — made him the natural candidate for the 1811 Court vacancy",
            "Duvall's combination of Maryland legal experience, congressional service, and nine years managing federal financial oversight as Comptroller gave him the institutional standing and multi-faceted government experience that qualified him for the Court appointment",
            "The Marshall Court's foundational position in American constitutional development — establishing the precedents for federal judicial review, interstate commerce regulation, and contract law during its 34-year tenure — created the institutional environment in which Duvall's 24-year presence contributed to constitutional stability even without prolific opinion writing"
        ],
        "effects": [
            "His 24-year Supreme Court tenure contributed to the constitutional stability of the Marshall Court era — his consistent presence and reliable votes supporting Marshall Court jurisprudence providing institutional continuity through the most formative period of American constitutional law",
            "His consistent support for free Black rights in manumission and property cases contributed to the small body of early Supreme Court jurisprudence that recognized the legal standing of free Black Americans — a distinctly progressive stance that distinguished him from other Southern slaveholder justices",
            "His nine-year Comptrollership of the Treasury contributed to federal financial oversight during the Jefferson and Madison administrations — managing the auditing and accountability functions of the Treasury during the period of federal fiscal development",
            "His extraordinary 92-year lifespan — spanning from the American Revolution to the age of Jackson — gave him a personal historical perspective that connected the founding generation's lived experience to the Jacksonian era, making him one of the few individuals whose life bridged the full arc of the early republic"
        ],
        "relationships": [
            {"entity": "Associate Justice, US Supreme Court (1811–1835, 24 years, Marshall Court)", "relationship": "ASSOCIATE_JUSTICE", "note": "Served as Associate Justice of the US Supreme Court for 24 years (1811–1835) — during the Marshall Court's foundational period, retiring at age 82"},
            {"entity": "Comptroller of the Treasury (1802–1811, 9 years, Jefferson-Madison administrations)", "relationship": "COMPTROLLER_OF_THE_TREASURY", "note": "Served as Comptroller of the Treasury (1802–1811) — managing federal financial oversight for 9 years during the Jefferson and Madison administrations before his Court appointment"},
            {"entity": "Marshall Court / John Marshall (Chief Justice, 1801–1835)", "relationship": "ASSOCIATE_JUSTICE_UNDER", "note": "Served as Associate Justice alongside Chief Justice John Marshall during the Court's most formative period — 24 years of Marshall Court constitutional development"},
            {"entity": "Free Black rights / manumission cases (progressive position on Maryland Supreme Court)", "relationship": "PROGRESSIVE_VOICE_FOR", "note": "Maintained a consistently progressive position in manumission and free Black rights cases — supporting the legal standing of free Black Americans despite being himself a Maryland slaveholder"},
            {"entity": "Maryland legislature, courts, and US Congress (pre-Court career)", "relationship": "POLITICIAN_AND_JUDGE_BEFORE_SCOTUS", "note": "Served in the Maryland legislature, as a Maryland state court judge, and as a US Representative (1794–1796) before his Supreme Court appointment — a multi-faceted political and judicial career that preceded his 24-year Court tenure"}
        ]
    }),

    # 5 — Christopher Greenup
    ("christopher-greenup", {
        "summary": (
            "Christopher Greenup (c. 1750–1818) was "
            "a Virginia-born soldier, lawyer, and "
            "politician who served as the 3rd "
            "Governor of Kentucky (1804–1808) — "
            "presiding over the state during one "
            "of the most turbulent episodes in "
            "early American Western history, "
            "including Aaron Burr's western "
            "conspiracy. He previously served "
            "as Kentucky's first US Representative "
            "(1792–1797, with his colleague "
            "Alexander D. Orr), as clerk of "
            "the Kentucky Court of Appeals, "
            "and was a participant in the "
            "Virginia constitutional convention.\n\n"
            "Greenup County, Kentucky (established "
            "1803) was named in his honor during "
            "his gubernatorial tenure — reflecting "
            "his standing in the state's "
            "Democratic-Republican community "
            "at a time when the county "
            "was still being organized "
            "from the frontier lands of "
            "northeastern Kentucky.\n\n"
            "His Revolutionary War service "
            "— as a lieutenant in the "
            "Continental Army and colonel "
            "in the Virginia militia — "
            "established his credentials "
            "as part of the founding "
            "generation that settled "
            "Kentucky and built its "
            "governmental institutions "
            "after statehood in 1792. "
            "He was among the early "
            "prominent figures who helped "
            "transform Kentucky from "
            "Virginia's western frontier "
            "into an independent state.\n\n"
            "His governorship coincided "
            "with the Burr Conspiracy "
            "(1806–1807) — Aaron Burr's "
            "unclear western scheme "
            "that may have involved "
            "separating western states "
            "from the Union or "
            "invading Mexico — which "
            "Greenup as governor was "
            "called upon to monitor "
            "and report to Jefferson."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "3rd Governor of Kentucky (1804–1808); Kentucky's first US Representative (1792–1797); Revolutionary War Continental Army lieutenant and Virginia militia colonel; Greenup County Kentucky (est. 1803) named in his honor; presided over Kentucky during the Burr Conspiracy; participant in the founding generation that built Kentucky's governmental institutions after statehood in 1792.",
            "significanceCategory": "local"
        },
        "causes": [
            "Kentucky's rapid transformation from Virginia's western frontier to independent statehood (1792) — and the state's need to build its governmental institutions from scratch in the absence of established political traditions — created the demand for Revolutionary War veterans and lawyers who could fill the legislative, executive, and judicial roles that the new state required",
            "The Democratic-Republican political dominance in early Kentucky — fueled by opposition to Federalist policies and the state's frontier egalitarianism — created the political environment in which Greenup's Democratic-Republican credentials made him a credible candidate for both congressional and gubernatorial offices",
            "The Burr Conspiracy's (1806–1807) particular relevance to Kentucky — whose western geography made it a potential staging ground for Burr's western scheme, and whose political community was divided about how to respond — created the challenge that defined the middle years of Greenup's governorship"
        ],
        "effects": [
            "His governorship contributed to Kentucky's institutional development during a critical decade — managing the state's governance during the Burr Conspiracy, reporting to Jefferson on Burr's activities, and maintaining the state's commitment to the Union during a period when western separatism was a genuine possibility",
            "His congressional service as one of Kentucky's first US Representatives contributed to the state's initial national representation — building Kentucky's presence in the early House of Representatives and establishing the Democratic-Republican political tradition that would dominate the state",
            "Greenup County's naming in his honor contributed to the geographic memorialization of his contributions to Kentucky's development — one of many Kentucky counties named for early governors and statesmen that preserve the memory of the founding generation",
            "His participation in the founding generation's transformation of Kentucky from frontier to state contributed to the institutional building that created one of the early republic's most distinctive political communities — combining Virginia legal traditions with the democratic culture of the western frontier"
        ],
        "relationships": [
            {"entity": "3rd Governor of Kentucky (1804–1808)", "relationship": "GOVERNOR", "note": "Served as Kentucky's 3rd Governor (1804–1808) — managing the state during the Burr Conspiracy and contributing to Kentucky's institutional development"},
            {"entity": "Kentucky first US Representative (1792–1797)", "relationship": "FIRST_US_REPRESENTATIVE", "note": "Served as one of Kentucky's first US Representatives (1792–1797) — among the earliest congressional representatives of the new western state"},
            {"entity": "Greenup County, Kentucky (est. 1803, named in his honor)", "relationship": "NAMESAKE_OF", "note": "Greenup County, Kentucky (established 1803) was named in his honor — one of the geographic memorials that preserve the founding generation's contributions to Kentucky's development"},
            {"entity": "Aaron Burr Conspiracy (1806–1807) / western separatism concern", "relationship": "GOVERNOR_DURING_AND_MONITORING", "note": "Governed Kentucky during the Burr Conspiracy (1806–1807) — reporting to Jefferson on Burr's western activities and maintaining the state's commitment to the Union when western separatism was a genuine concern"},
            {"entity": "Revolutionary War / Virginia militia and Continental Army (lieutenant and colonel)", "relationship": "VETERAN_OF", "note": "Served as a Continental Army lieutenant and Virginia militia colonel during the Revolutionary War — the military service that established his credentials as part of the founding generation that settled and built Kentucky"}
        ]
    }),

    # 6 — Thaddeus Betts
    ("thaddeus-betts", {
        "summary": (
            "Thaddeus Laddins Betts (1797–1840) was "
            "a Connecticut lawyer and politician who "
            "served as Lieutenant Governor of "
            "Connecticut (1832–1833 and 1834–1835) "
            "and as a US Senator from Connecticut "
            "(1839–1840), dying in office before "
            "completing his term. Born in Norwalk, "
            "Connecticut, he served in the "
            "Connecticut House of Representatives "
            "and the Connecticut Senate before "
            "his rise to the state's "
            "second executive office.\n\n"
            "His senatorial career was tragically "
            "brief: appointed to fill the vacancy "
            "created by the resignation of "
            "Thaddeus Wallingford, Betts served "
            "just over a year before his death "
            "in 1840 at age 43. His Senate "
            "tenure fell during the crucial "
            "period of Whig Party formation "
            "— the years when anti-Jackson "
            "and anti-Van Buren sentiment "
            "was consolidating the Whig "
            "coalition that would elect "
            "William Henry Harrison in 1840.\n\n"
            "His two separate terms as "
            "Connecticut's Lieutenant Governor "
            "— with a one-year gap between "
            "them — reflected the competitive "
            "politics of a small state "
            "where the National Republican "
            "and Whig parties alternated "
            "with the Democrats in state "
            "governance. Connecticut was "
            "one of the Whigs' strongest "
            "New England states.\n\n"
            "His career, though cut short "
            "by early death, illustrated "
            "the pattern of Connecticut "
            "Whig political advancement — "
            "from state legislature through "
            "the Lieutenant Governorship "
            "to federal Senate service."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Connecticut Lieutenant Governor (1832–1833, 1834–1835); US Senator from Connecticut (1839–1840, died in office); Norwalk Connecticut legislator; National Republican/Whig; his brief Senate tenure fell during the Whig Party's consolidating phase that led to Harrison's 1840 election; his death in office at 43 cut short a promising Connecticut political career.",
            "significanceCategory": "local"
        },
        "causes": [
            "Connecticut's Whig political tradition — rooted in New England's commercial and legal culture, Calvinist social conservatism, and opposition to Jacksonian Democratic populism — created the political environment in which Betts's National Republican and Whig affiliations could sustain a career from state legislature to Lieutenant Governor to US Senate",
            "The vacancy created by the resignation of US Senator Thaddeus Wallingford created the appointment opportunity that elevated Betts to the Senate — the constitutional appointment mechanism that bypassed the normal electoral process and placed him in the national legislature",
            "Connecticut's competitive two-party politics — with Whigs and Democrats alternating in state offices — created the fluid political environment in which Betts could serve two non-consecutive terms as Lieutenant Governor, reflecting the electoral volatility of a small competitive state"
        ],
        "effects": [
            "His brief Senate tenure contributed to Connecticut's representation during the critical Whig consolidation period of 1839–1840 — the years when the anti-Jackson coalition was organizing for the 1840 Harrison campaign that would give the Whigs their first presidential victory",
            "His two terms as Connecticut Lieutenant Governor contributed to the state's executive administration during the early Whig period — providing the second executive voice in a state where Whig governance reflected New England's commercial and conservative values",
            "His death in office contributed to the political process of senatorial succession — creating a vacancy that required another appointment and illustrating the recurring challenge of early senatorial death that frequently disrupted the Senate's composition",
            "His career trajectory — from Norwalk local politics through state legislature to Lieutenant Governor to Senate — illustrated the standard advancement path of Connecticut Whig politicians, building their careers through the state's institutional hierarchy toward national office"
        ],
        "relationships": [
            {"entity": "Connecticut Lieutenant Governor (1832–1833 and 1834–1835)", "relationship": "LIEUTENANT_GOVERNOR", "note": "Served as Connecticut's Lieutenant Governor in two separate terms — reflecting the competitive alternation of Whig and Democratic governance in the state"},
            {"entity": "US Senate from Connecticut (1839–1840, died in office)", "relationship": "SENATOR_DIED_IN_OFFICE", "note": "Served as US Senator from Connecticut (1839–1840) — appointed to a vacancy, serving just over a year before his death at age 43"},
            {"entity": "Whig Party / National Republican Party in Connecticut", "relationship": "MEMBER_AND_REPRESENTATIVE_OF", "note": "A National Republican then Whig politician — his career embodying Connecticut's Whig tradition of commercial conservatism and anti-Jacksonian politics"},
            {"entity": "Connecticut state legislature (House and Senate, Norwalk representative)", "relationship": "LEGISLATOR", "note": "Served in both the Connecticut House and Senate — the state legislative experience that built his political career before his Lieutenant Governor and Senate service"},
            {"entity": "Whig Party consolidation / 1840 Harrison presidential campaign", "relationship": "SENATOR_DURING", "note": "Served in the Senate during the Whig Party's critical consolidating phase (1839–1840) — the period when anti-Jackson and anti-Van Buren sentiment was organizing for the Harrison campaign"}
        ]
    }),

    # 7 — John Mathews
    ("john-mathews", {
        "summary": (
            "John Mathews (1744–1802) was a South "
            "Carolina Founding Father, lawyer, and "
            "statesman who served as a delegate "
            "to the Continental Congress (1778–1781) "
            "— endorsing the Articles of Confederation "
            "on behalf of South Carolina — and as "
            "the 33rd Governor of South Carolina "
            "(1782–1783), governing the state "
            "during the critical final phase of "
            "the Revolutionary War when British "
            "forces were withdrawing from Charleston "
            "after three years of occupation.\n\n"
            "His Continental Congress service "
            "came during the most desperate "
            "years of the Revolution — when "
            "South Carolina had been overrun "
            "by British forces (Charleston "
            "surrendered May 1780), much of "
            "the state's Patriot leadership "
            "was captured or exiled, and the "
            "southern theatre of the war was "
            "being fought as a brutal partisan "
            "conflict between Patriot and Loyalist "
            "militias. His congressional service "
            "while his home state was under "
            "occupation gave his delegation "
            "particular political urgency.\n\n"
            "His governorship (1782–1783) "
            "coincided with the British "
            "evacuation of Charleston in "
            "December 1782 — one of the "
            "concluding acts of the "
            "American Revolutionary War "
            "in the South. He presided "
            "over the complex political "
            "transition from British "
            "occupation to restored "
            "Patriot governance, managing "
            "the competing claims of "
            "returning exiles, those who "
            "had remained and accommodated "
            "the British, and those who "
            "had actively collaborated.\n\n"
            "Born in Charleston, he returned "
            "to legal practice after his "
            "governorship, contributing "
            "to the rebuilding of South "
            "Carolina's legal institutions "
            "after the war's devastation."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "South Carolina Founding Father; Continental Congress delegate (1778–1781) and Articles of Confederation signatory; 33rd Governor of South Carolina (1782–1783, during the British evacuation of Charleston); his governorship presided over the critical transition from British occupation to restored Patriot governance in South Carolina's most devastated Revolutionary theater.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The British capture of Charleston (May 1780) and their occupation of South Carolina — which captured or exiled most Patriot leadership and reduced the state to a brutal partisan guerrilla conflict between Patriot and Loyalist militias — created the context in which Mathews's Continental Congress service represented South Carolina during the state's most desperate military situation",
            "The Patriot partisan resistance in South Carolina's backcountry — led by Francis Marion, Thomas Sumter, and Andrew Pickens — which gradually reversed the British military position, leading to the British evacuation of Charleston in December 1782 — created the political situation that Mathews's governorship managed: the transition from occupation to restoration",
            "The post-occupation political challenge of managing the divided loyalties of a state population that had lived under British occupation for three years — with some having accommodated, some having collaborated, and some having resisted — created the governance challenge that defined Mathews's brief governorship"
        ],
        "effects": [
            "His Continental Congress service contributed to South Carolina's national representation during the most desperate phase of its Revolutionary experience — providing a congressional voice for a state under military occupation and ensuring that the southern theatre's interests were represented in the Continental deliberations",
            "His governorship's management of the British evacuation contributed to the reconstruction of Patriot governance in South Carolina — navigating the politically explosive question of how to treat those who had remained in Charleston during the occupation, and restoring state institutions after three years of British control",
            "His endorsement of the Articles of Confederation on South Carolina's behalf contributed to the ratification of the new nation's first governing document — one of the formal acts that created the political architecture of the new United States",
            "His post-war legal career contributed to the rebuilding of South Carolina's legal institutions after the war's devastation — restoring the professional legal community that the British occupation had disrupted and establishing the legal framework for the state's post-Revolutionary development"
        ],
        "relationships": [
            {"entity": "33rd Governor of South Carolina (1782–1783, British evacuation period)", "relationship": "GOVERNOR", "note": "Served as South Carolina's 33rd Governor (1782–1783) — presiding over the critical transition from British occupation to restored Patriot governance, coinciding with the British evacuation of Charleston in December 1782"},
            {"entity": "Continental Congress (South Carolina delegate, 1778–1781)", "relationship": "DELEGATE", "note": "Served as a Continental Congress delegate (1778–1781) — representing South Carolina in the national deliberative body while his home state was under British military occupation"},
            {"entity": "Articles of Confederation (signatory on behalf of South Carolina)", "relationship": "SIGNATORY_ON_BEHALF_OF_SC", "note": "Endorsed the Articles of Confederation on behalf of South Carolina — one of the formal acts that ratified the new nation's first governing document"},
            {"entity": "British occupation of South Carolina (1780–1782) / Charleston surrender", "relationship": "GOVERNOR_MANAGING_AFTERMATH_OF", "note": "Governed South Carolina during and after the British evacuation — managing the complex political transition from three years of British occupation to restored Patriot governance"},
            {"entity": "South Carolina Patriot resistance / partisan war (Marion, Sumter, Pickens)", "relationship": "POLITICAL_LEADER_ALONGSIDE_MILITARY_LEADERS_OF", "note": "Served as a political leader alongside the military leaders of South Carolina's partisan resistance — his congressional and gubernatorial service complementing the guerrilla campaigns of Marion, Sumter, and Pickens"}
        ]
    }),

    # 8 — Antoine Barnave
    ("antoine-barnave", {
        "summary": (
            "Antoine Pierre Joseph Marie Barnave "
            "(1761–1793) was a French lawyer and "
            "politician from Grenoble who became "
            "one of the most powerful orators "
            "of the early French Revolution — "
            "alongside Honoré Mirabeau — and "
            "a founding member of the Feuillants, "
            "the constitutional monarchist "
            "faction that sought to stabilize "
            "the Revolution around a limited "
            "monarchy before the Republic "
            "was proclaimed. He was guillotined "
            "in November 1793 after his secret "
            "correspondence with Marie Antoinette "
            "was discovered.\n\n"
            "His Revolutionary career began "
            "brilliantly: elected to the "
            "Estates-General in 1789, he became "
            "one of the Third Estate's most "
            "compelling advocates, contributing "
            "to the Tennis Court Oath and "
            "the Declaration of the Rights "
            "of Man. His oratorical skill "
            "made him a dominant figure "
            "in the National Constituent "
            "Assembly alongside Mirabeau.\n\n"
            "The turning point came with the "
            "Flight to Varennes (June 1791) "
            "— the royal family's failed attempt "
            "to flee France. Barnave escorted "
            "the royal family back to Paris "
            "and, in conversation with "
            "Marie Antoinette during the "
            "journey, became convinced that "
            "a constitutional monarchy "
            "was France's only stable path "
            "forward. He subsequently engaged "
            "in secret correspondence with "
            "the Queen, advising her on "
            "constitutional politics — "
            "a treasonous collaboration "
            "that was later discovered.\n\n"
            "'Was the blood shed at the Trocadéro "
            "so pure?' — Barnave's notorious "
            "defense of the killing of protesters "
            "in 1791 became one of the Revolution's "
            "most shocking statements, illustrating "
            "the moral compromises of "
            "even the most eloquent "
            "constitutional moderates."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Leading French Revolutionary orator alongside Mirabeau; co-founder of the Feuillants (constitutional monarchist faction); member of the National Constituent Assembly; secret correspondence with Marie Antoinette after Flight to Varennes (1791); guillotined November 1793; his arc from radical Third Estate advocate to constitutional monarchist to executed traitor traced the full tragedy of France's moderate revolutionary path.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Revolution's initial phase — the Estates-General's transformation into a National Assembly, the Tennis Court Oath, and the Declaration of the Rights of Man — created the political arena in which Barnave's oratorical brilliance made him one of the most powerful voices in the Third Estate's revolution against the Old Regime",
            "The Flight to Varennes (June 1791) — the royal family's failed attempt to flee France — was the transformative personal experience that converted Barnave from a radical reformer to a constitutional monarchist: his encounter with Marie Antoinette during the return journey convinced him that a constitutional monarchy was France's only path to stability",
            "The Revolution's radicalization — as the Jacobins displaced the constitutional monarchists, the Republic was proclaimed in September 1792, and the Terror began in 1793 — created the fatal political environment in which Barnave's secret royalist correspondence made him a traitor subject to the revolutionary tribunal's death sentence"
        ],
        "effects": [
            "His founding of the Feuillants — the constitutional monarchist faction that split from the Jacobins in 1791 — contributed to the attempt to stabilize the French Revolution around a limited constitutional monarchy, a political project that ultimately failed when the radicalized Jacobins and the war crisis overwhelmed the moderate position",
            "His secret correspondence with Marie Antoinette contributed to the Queen's political strategy during the constitutional monarchy period — advising her on how to work within the constitution while seeking counter-revolutionary support, advice that the Queen ultimately found inadequate and that Barnave paid for with his life",
            "His guillotining in November 1793 contributed to the Terror's destruction of the Revolution's moderate constitutional faction — the elimination of the Feuillant tradition that had sought to reconcile the Revolution's principles with constitutional monarchy, leaving France's political field to the Jacobin radicals",
            "His career arc — from brilliant Third Estate advocate to constitutional monarchist to executed traitor — became one of the most instructive case studies in the Revolution's internal logic, illustrating how the Revolution's radicalization destroyed even its most eloquent moderate voices"
        ],
        "relationships": [
            {"entity": "Feuillants (constitutional monarchist faction, co-founder, 1791)", "relationship": "CO-FOUNDER_OF", "note": "Co-founded the Feuillants — the constitutional monarchist faction that split from the Jacobins in 1791 and sought to stabilize the Revolution around a limited monarchy"},
            {"entity": "National Constituent Assembly (1789–1791, leading orator alongside Mirabeau)", "relationship": "LEADING_ORATOR_IN", "note": "Served as one of the National Constituent Assembly's most powerful orators (1789–1791) — alongside Mirabeau, the dominant voice of the Third Estate's revolutionary transformation of France's political system"},
            {"entity": "Flight to Varennes (June 1791) / Marie Antoinette (secret correspondence)", "relationship": "ESCORT_AND_SECRET_CORRESPONDENT_WITH", "note": "Escorted the royal family back to Paris after the Flight to Varennes (1791) and subsequently engaged in secret correspondence with Marie Antoinette — advising on constitutional politics in a treasonous collaboration that led to his execution"},
            {"entity": "French Revolutionary Terror (guillotined November 1793)", "relationship": "EXECUTED_BY", "note": "Guillotined in November 1793 after his secret royalist correspondence was discovered — one of the Terror's most significant executions, eliminating France's leading constitutional monarchist voice"},
            {"entity": "Tennis Court Oath / Declaration of Rights of Man (1789)", "relationship": "CONTRIBUTOR_TO", "note": "Contributed to the Tennis Court Oath and the Declaration of the Rights of Man in 1789 — the founding acts of the French Revolution's constitutional phase that Barnave helped drive as a leading Third Estate advocate"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 48)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
