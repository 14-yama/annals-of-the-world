#!/usr/bin/env python3
"""
Batch 61 — 8 entities: Samuel Sprigg, Denis Godefroy, John Lansing Jr,
William A. Trimble, Arthur P. Hayne, Bedford Brown, Caleb Tompkins, Jesse Wharton
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

    ("samuel-sprigg", {
        "summary": (
            "Samuel Sprigg (1786–1855) was an "
            "American Democratic-Republican and "
            "subsequently Jacksonian Democrat "
            "politician from Maryland who served "
            "as Governor of Maryland (1819–1822) "
            "during the critical transitional "
            "years of the Era of Good Feelings — "
            "the apparent post-War of 1812 "
            "political consensus that masked "
            "the deep sectional and economic "
            "tensions that would rupture in "
            "the Missouri Crisis of 1819–1821 "
            "and the political realignment "
            "of the 1820s.\n\n"
            "Sprigg came from a prominent "
            "Maryland political family — the "
            "Spriggs had been active in "
            "Maryland politics since the "
            "colonial era. His gubernatorial "
            "career coincided exactly with "
            "the Missouri Compromise debate "
            "— the congressional crisis over "
            "the admission of Missouri as a "
            "slave or free state that exposed "
            "the sectional fault lines in "
            "American politics and that Thomas "
            "Jefferson famously compared to "
            "'a firebell in the night.'\n\n"
            "As governor of a slave state "
            "in this moment of sectional crisis, "
            "Sprigg managed Maryland's state "
            "government through one of the "
            "most politically charged debates "
            "in early American history.\n\n"
            "His career reflected Maryland's "
            "position as a border state — "
            "a slave state with significant "
            "northern commercial connections, "
            "navigating between sectional extremes."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Maryland (1819–1822) during the Missouri Crisis and Era of Good Feelings; came from a prominent Maryland political family; governed a border slave state through the sectional crisis that exposed America's deepening fault lines over slavery's expansion.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Era of Good Feelings' apparent political consensus — the post-War of 1812 period of single-party Democratic-Republican governance that produced Sprigg's governorship in the absence of meaningful party competition — created the political environment of his election",
            "The Missouri Crisis (1819–1821) — the congressional debate over Missouri's admission as a slave state that exposed the sectional tensions between the North and South over slavery's expansion into new territories — defined the major political crisis of Sprigg's gubernatorial tenure",
            "Maryland's border-state position — a slave state with strong commercial and geographic ties to the free North — created the political balancing act that Maryland governors like Sprigg had to perform, representing slaveholding interests while maintaining Maryland's broader national connections"
        ],
        "effects": [
            "His governorship maintained Maryland's state government during the Missouri Crisis — managing the administration of a border slave state through the first major sectional crisis of the nineteenth century",
            "His term coincided with the beginning of the political realignment that would produce Jacksonian Democracy — the transformation of the Democratic-Republican Party into competing Adams and Jackson factions that reshaped American politics in the 1820s",
            "His career contributed to Maryland's political tradition of border-state governance — the distinctive political culture of states that sat between the free North and the slave South and had to navigate between the competing sectional demands",
            "His family's political prominence illustrated the continuing importance of dynastic political networks in early American state politics — the prominent Maryland families whose social connections translated across generations into political office"
        ],
        "relationships": [
            {"target": "maryland", "verb": "GOVERNS", "note": "Governor of Maryland 1819–1822"},
            {"target": "missouri-compromise", "verb": "GOVERNS_DURING", "note": "Governor during the Missouri Crisis 1819–1821"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Governed during the single-party Democratic-Republican era"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Democratic-Republican politician of the Era of Good Feelings"},
            {"target": "maryland-political-tradition", "verb": "PART_OF", "note": "Member of prominent Maryland political family"}
        ]
    }),

    ("denis-godefroy", {
        "summary": (
            "Denis Godefroy (1549–1621) was a "
            "French humanist jurist and legal "
            "scholar who became one of the most "
            "important editors and commentators "
            "on Roman law in the late sixteenth "
            "and early seventeenth centuries. "
            "His critical edition of the Corpus "
            "Juris Civilis — Justinian's sixth-century "
            "codification of Roman law — became "
            "the standard scholarly edition "
            "used by European lawyers and "
            "legal scholars for generations, "
            "establishing the textual foundations "
            "of the ius commune legal tradition "
            "that governed educated legal "
            "practice across Europe.\n\n"
            "Godefroy was trained in the "
            "humanist legal tradition — the "
            "mos gallicus approach to Roman law "
            "that combined rigorous philological "
            "analysis, historical method, and "
            "classical learning with legal "
            "scholarship. His work placed "
            "him among the great French humanist "
            "jurists of the sixteenth century "
            "— Budé, Cujas, Hotman — who "
            "transformed European legal "
            "scholarship.\n\n"
            "His edition of the Corpus Juris "
            "Civilis (1583) with its extensive "
            "annotations and apparatus became "
            "the authoritative scholarly "
            "text — used by students and "
            "scholars throughout Europe to "
            "study the Roman law that "
            "underpinned the civil law tradition.\n\n"
            "His son Jacques Godefroy (1587–1652) "
            "continued his scholarly tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French humanist jurist and Corpus Juris Civilis editor (1583 edition became the European standard); central figure in the mos gallicus tradition of historical Roman law scholarship; his critical edition shaped the ius commune legal tradition used across Europe for generations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The humanist mos gallicus legal tradition — the French school of Roman law scholarship pioneered by Guillaume Budé and Jacobus Cujas that combined classical philology with legal analysis — provided the intellectual framework and scholarly method for Godefroy's critical textual work on Justinian's Corpus",
            "The printing revolution and the growth of European legal education — the expansion of universities, the proliferation of printed legal texts, and the demand for reliable scholarly editions of the Corpus Juris Civilis from law students and practitioners across Europe — created the market and motivation for Godefroy's editorial work",
            "The Protestant Reformation's disruption of the medieval ius commune consensus — which forced a re-examination of Roman law's sources, authority, and interpretation across Europe — intensified scholarly interest in the textual foundations of civil law, creating demand for Godefroy's historically rigorous edition"
        ],
        "effects": [
            "His 1583 Corpus Juris Civilis edition with its scholarly apparatus became the standard European reference — the edition that law students, professors, and practitioners across the continent used to study Roman law, shaping legal education for generations",
            "His textual scholarship contributed to the development of the ius commune legal tradition — the shared Roman-canonical law that educated lawyers across Europe used, providing the textual foundations for the civil law scholarship that shaped European jurisprudence",
            "His humanist method — applying historical and philological analysis to legal texts — established a scholarly standard for Roman law scholarship that his successors including his son Jacques Godefroy built upon and extended",
            "His work contributed to the French humanist legal tradition's European influence — French legal scholarship's dominance in sixteenth-century Europe, transmitted through authoritative editions like Godefroy's, shaped legal education and practice across Catholic and Protestant Europe alike"
        ],
        "relationships": [
            {"target": "corpus-juris-civilis", "verb": "EDITS", "note": "Critical edition (1583) that became the European standard"},
            {"target": "roman-law", "verb": "SCHOLAR_OF", "note": "Central figure in humanist Roman law scholarship"},
            {"target": "mos-gallicus", "verb": "REPRESENTS", "note": "French humanist legal tradition"},
            {"target": "ius-commune", "verb": "CONTRIBUTES_TO", "note": "Textual foundations for European common law tradition"},
            {"target": "jacques-godefroy", "verb": "FATHER_OF", "note": "Son continued his scholarly tradition"}
        ]
    }),

    ("john-lansing-jr", {
        "summary": (
            "John Lansing Jr. (1754–c.1829) was "
            "an American politician and jurist "
            "from New York who played a significant "
            "role in the debates over the U.S. "
            "Constitution. As a delegate to "
            "the Constitutional Convention of "
            "1787, he was one of only three "
            "delegates who refused to sign "
            "the Constitution — leaving the "
            "convention early with Robert Yates "
            "because they believed it exceeded "
            "the mandate to merely revise "
            "the Articles of Confederation "
            "and threatened the sovereignty "
            "of the states.\n\n"
            "Lansing was a leading Anti-Federalist "
            "who opposed ratification in New York "
            "— a state where the Anti-Federalist "
            "cause was particularly strong "
            "under the leadership of Governor "
            "George Clinton. He later became "
            "a Chief Justice of the New York "
            "Supreme Court (1798–1804) and "
            "Chancellor of New York (1801–1814) "
            "— the state's most prestigious "
            "judicial office, occupied earlier "
            "by Robert Livingston.\n\n"
            "His mysterious disappearance "
            "in New York City in December "
            "1829 — after leaving his hotel "
            "to mail letters, never to return "
            "— became one of the famous "
            "unsolved mysteries of early "
            "American history.\n\n"
            "He remains the most prominent "
            "figure among the Constitution's non-signers."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York delegate who walked out of the Constitutional Convention (1787) and refused to sign the Constitution; leading Anti-Federalist opposing New York ratification; later Chancellor of New York (1801–1814); mysteriously disappeared in 1829 — one of early America's most famous unsolved mysteries.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Constitutional Convention's expansion beyond its mandate — Lansing and Yates were sent to Philadelphia to revise the Articles of Confederation, not to create an entirely new national government, and their departure reflected their conviction that the convention had exceeded its legitimate authority",
            "New York's strong Anti-Federalist tradition under Governor George Clinton — which reflected the state's large landowners' and farmers' suspicion of centralized power, fear of federal taxation, and preference for state sovereignty — provided the political context for Lansing's opposition to ratification",
            "New York's political elite's interest in maintaining state power — Lansing's political world was one where New York's distinct political culture and its control over its own affairs represented real interests that a strong national government threatened to subordinate"
        ],
        "effects": [
            "His walkout from the Constitutional Convention — one of only three delegates to leave without signing — became historically significant as the most prominent and articulate statement of Anti-Federalist opposition to the new constitution from within the convention itself",
            "His leadership of Anti-Federalist opposition in New York — a state that ratified only narrowly (30–27) after Hamilton, Madison, and Jay published The Federalist Papers — demonstrated that Anti-Federalist resistance came close to preventing ratification in a crucial large state",
            "His long judicial career as Chancellor of New York (1801–1814) contributed to the development of New York's equity jurisprudence — the legal tradition that his predecessor Livingston and successor Kent developed into one of the most significant bodies of American law",
            "His mysterious 1829 disappearance — never explained, presumed murdered — added a legendary quality to his historical profile, making him one of the most discussed of the founding generation's obscure figures"
        ],
        "relationships": [
            {"target": "constitutional-convention-1787", "verb": "ATTENDS_AND_LEAVES", "note": "Left before signing; refused to endorse the new Constitution"},
            {"target": "anti-federalists", "verb": "LEADS", "note": "Leading Anti-Federalist in New York ratification debates"},
            {"target": "new-york-supreme-court", "verb": "SERVES_AS_CHIEF_JUSTICE", "note": "Chief Justice 1798–1804"},
            {"target": "chancellor-of-new-york", "verb": "SERVES_AS", "note": "Chancellor 1801–1814"},
            {"target": "george-clinton", "verb": "ALLIES_WITH", "note": "Allied with Anti-Federalist governor George Clinton"}
        ]
    }),

    ("william-a-trimble", {
        "summary": (
            "William Allen Trimble (1786–1821) "
            "was an American military officer and "
            "politician from Ohio who served as "
            "a U.S. Senator from Ohio (1819–1821) "
            "and as a general in the War of 1812. "
            "His brief Senate career — cut short "
            "by his death at only 35 — came during "
            "the critical years of the Missouri "
            "Crisis and the Era of Good Feelings, "
            "when Ohio was emerging as one of "
            "the most populous states in the "
            "rapidly growing American West.\n\n"
            "Trimble served in the War of 1812 "
            "under General William Henry Harrison "
            "— the northwestern theater campaigns "
            "against the British and their Native "
            "American allies in the Great Lakes "
            "region. He rose to the rank of "
            "brevet brigadier general, gaining "
            "the military reputation that "
            "helped launch his political career "
            "in the post-war years.\n\n"
            "His Senate career was consumed "
            "by the Missouri Crisis debates "
            "— the congressional confrontation "
            "over Missouri's admission as "
            "a slave state that Thomas Jefferson "
            "compared to a 'firebell in the night.' "
            "As an Ohio senator representing "
            "a free state in the Northwest Territory, "
            "he participated in this defining "
            "sectional debate.\n\n"
            "His early death prevented a "
            "potentially significant political career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Ohio Senator (1819–1821) and War of 1812 general; served under William Henry Harrison in the Northwest; participated in Missouri Crisis debates as a free-state senator; died at 35 before a potentially significant political career could develop.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The War of 1812's northwestern theater — the campaigns under William Henry Harrison against British forces and Native American confederates in the Great Lakes region — provided Trimble the military service and brevet generalship that launched his political career in post-war Ohio",
            "Ohio's rapid growth as one of the most populous western states — driven by migration from the Northeast and the Ohio River valley's agricultural potential — created the expanding political institutions that needed representatives like Trimble in the U.S. Senate",
            "The Era of Good Feelings' political culture of military hero advancement — in which War of 1812 veterans and generals leveraged their military reputations into political careers in the post-war years — provided the pathway through which Trimble moved from general to senator"
        ],
        "effects": [
            "His Senate participation in the Missouri Crisis debates contributed Ohio's free-state perspective to the congressional debates that produced the Missouri Compromise — the territorial compromise that admitted Missouri as slave and Maine as free state",
            "His military service under Harrison contributed to the northwestern campaigns that secured the American position in the Great Lakes region and provided the military foundation for post-war American expansion",
            "His early death at 35 deprived Ohio of a potentially significant political voice at a crucial moment in the state's development — illustrating the high mortality that cut short many careers in the early American republic",
            "His career illustrated the War of 1812's political legacy — the generation of military officers who translated their wartime service into political careers in the post-war years, particularly in the rapidly growing western states"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Ohio Senator 1819–1821"},
            {"target": "war-of-1812", "verb": "FIGHTS_IN", "note": "Brevet brigadier general in the northwestern theater"},
            {"target": "william-henry-harrison", "verb": "SERVES_UNDER", "note": "Served under Harrison in the Great Lakes campaigns"},
            {"target": "missouri-compromise", "verb": "DEBATES", "note": "Free-state senator during the Missouri Crisis"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "U.S. Senator from the rapidly growing state of Ohio"}
        ]
    }),

    ("arthur-p-hayne", {
        "summary": (
            "Arthur Peronneau Hayne (1788–1867) "
            "was an American politician and "
            "soldier from South Carolina who "
            "served briefly as a U.S. Senator "
            "(1823) and as a general in the "
            "South Carolina militia. He was "
            "the younger brother of Robert Y. "
            "Hayne — the South Carolina senator "
            "whose famous debates with Daniel "
            "Webster in 1830 on the nature "
            "of the Union and states' rights "
            "became one of the most celebrated "
            "rhetorical confrontations in "
            "American political history.\n\n"
            "Arthur Hayne served as an officer "
            "in the War of 1812, gaining the "
            "military experience that characterized "
            "his generation's political biography. "
            "His brief Senate appointment in "
            "1823 — filling a vacancy — gave "
            "him a taste of national politics "
            "but did not develop into a "
            "significant legislative career.\n\n"
            "The Hayne family's prominence "
            "in South Carolina politics "
            "— both brothers serving in "
            "the Senate and in state offices "
            "— illustrated the dynastic "
            "political networks that dominated "
            "antebellum South Carolina, "
            "where a small planter aristocracy "
            "controlled state politics through "
            "family connections, social prestige, "
            "and the deferential political "
            "culture of the slave South.\n\n"
            "He lived until 1867, witnessing "
            "the Confederacy's defeat."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "South Carolina U.S. Senator (1823) and militia general; younger brother of the more famous Robert Y. Hayne; member of the prominent South Carolina Hayne political dynasty; War of 1812 veteran who lived to see the Confederacy's defeat.",
            "significanceCategory": "local"
        },
        "causes": [
            "South Carolina's planter aristocracy's dynastic political culture — in which prominent families like the Haynes maintained political positions across generations through social networks, wealth, and the deferential culture of the slave South — created the political world in which Arthur Hayne's brief Senate appointment occurred",
            "The War of 1812's political legacy — which gave a generation of South Carolina officers the military credentials that supplemented their social standing in post-war politics — contributed to Hayne's public profile as a militia general",
            "The Senate vacancy-appointment system — in which state legislatures appointed senators to fill vacancies, often choosing prominent local figures with the right family and social connections — created the mechanism for Hayne's brief Senate service"
        ],
        "effects": [
            "His brief Senate service contributed South Carolina's states'-rights perspective to the Senate's deliberations during the brief period of his appointment — even if his individual contribution was limited by the brevity of his tenure",
            "His family connection to Robert Y. Hayne — whose 1830 debates with Daniel Webster became the most celebrated statement of Southern states'-rights doctrine — linked Arthur Hayne to the most significant ideological confrontation of the antebellum period",
            "His long life (1788–1867) meant that he witnessed the full arc of the political ideology he and his brother represented — from the nullification crisis to secession to Confederacy defeat — living through the catastrophe of Southern political culture's ultimate failure",
            "His career illustrated the South Carolina political culture of the antebellum era — the small planter aristocracy's monopolization of political office, the military credentials supplementing social standing, and the states'-rights ideology that defined South Carolina's political identity"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "U.S. Senator from South Carolina 1823"},
            {"target": "robert-y-hayne", "verb": "SIBLING_OF", "note": "Brother of the more famous South Carolina senator"},
            {"target": "south-carolina", "verb": "REPRESENTS", "note": "South Carolina politician and militia general"},
            {"target": "war-of-1812", "verb": "SERVES_IN", "note": "War of 1812 officer gaining military credentials"},
            {"target": "south-carolina-states-rights-tradition", "verb": "PART_OF", "note": "Member of the South Carolina states-rights political aristocracy"}
        ]
    }),

    ("bedford-brown", {
        "summary": (
            "Bedford Brown (1795–1870) was an "
            "American Democratic politician "
            "from North Carolina who served as "
            "a U.S. Senator (1829–1840) during "
            "the height of the Jacksonian "
            "Democracy era. A devoted supporter "
            "of Andrew Jackson and Martin Van "
            "Buren, he was one of the most "
            "reliable Jacksonian Democrats "
            "in the Senate during the "
            "confrontational years of the "
            "Bank War, the nullification crisis, "
            "and the beginnings of the slavery "
            "controversy's penetration of "
            "national politics.\n\n"
            "Brown was born in Caswell County, "
            "North Carolina and built his "
            "political career in the state's "
            "Democratic tradition — the "
            "yeoman farmer and small planter "
            "constituencies that made North "
            "Carolina one of Jackson's most "
            "reliable states. His eleven-year "
            "Senate career placed him at the "
            "center of the Jacksonian era's "
            "defining political battles.\n\n"
            "His Senate tenure encompassed "
            "the Bank War — Jackson's campaign "
            "to destroy the Second Bank of "
            "the United States — the nullification "
            "crisis with South Carolina, and "
            "the early debates over the "
            "abolitionist petition controversy "
            "that began to drive slavery "
            "into congressional politics.\n\n"
            "He resigned in 1840 and later "
            "briefly served again (1858–1860)."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "North Carolina Democratic Senator (1829–1840); loyal Jacksonian Democrat through the Bank War, nullification crisis, and early slavery debates; served eleven years at the Senate's core Jacksonian coalition; briefly returned to Senate 1858–1860.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Andrew Jackson's political coalition — which united Southern yeoman farmers, small planters, and urban workers against the 'money power' of the Eastern financial establishment — provided the political identity and voter base that sustained Brown's long Senate career",
            "North Carolina's Democratic political tradition — rooted in the Piedmont's yeoman farmer culture and its distrust of Eastern financial institutions — made it one of the most reliable Jacksonian states, creating the political constituency for Brown's repeated electoral success",
            "The Bank War's mobilizing energy — Jackson's campaign against the Second Bank of the United States that became the defining political struggle of the 1830s, galvanizing Jacksonian Democrats against what they saw as a corrupt financial monopoly — provided the issue around which Brown's Senate career was organized"
        ],
        "effects": [
            "His eleven-year Senate tenure contributed to the Jacksonian coalition's legislative agenda — supporting Jackson's Bank War, opposing the nullifiers, and maintaining the Democratic Party's position on the major issues of the 1830s",
            "His consistent Jacksonian loyalty helped cement North Carolina as one of the reliable Southern Democratic states — contributing to the regional political alignment that made the Democratic Party the dominant force in the antebellum South",
            "His Senate service during the early abolitionist petition controversy — when Northern abolitionists began flooding Congress with antislavery petitions in the 1830s — placed him in the Senate debates that produced the gag rule controversy and began the process of politicizing slavery nationally",
            "His return to the Senate in 1858–1860 — the eve of secession — linked his long political career to the final crisis of the Union that the Jacksonian coalition's political culture had both sustained and ultimately failed to prevent"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "North Carolina Senator 1829–1840, briefly 1858–1860"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Devoted Jacksonian Democrat"},
            {"target": "bank-war", "verb": "SUPPORTS_JACKSON_IN", "note": "Supported destruction of Second Bank of the United States"},
            {"target": "nullification-crisis", "verb": "OPPOSES", "note": "Opposed South Carolina nullifiers alongside Jackson"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "Longtime North Carolina Democratic senator"}
        ]
    }),

    ("caleb-tompkins", {
        "summary": (
            "Caleb Tompkins (1759–1846) was an "
            "American politician from New York "
            "who served in the U.S. House of "
            "Representatives (1817–1821) during "
            "the Era of Good Feelings. He was "
            "the brother of Daniel D. Tompkins "
            "— a significantly more prominent "
            "figure who served as Governor "
            "of New York (1807–1817) and as "
            "Vice President of the United "
            "States under James Monroe (1817–1825). "
            "Caleb's congressional career "
            "coincided with his brother's "
            "vice-presidency — making his "
            "time in the House concurrent "
            "with Daniel's tenure in the "
            "second-highest office in the land.\n\n"
            "Caleb Tompkins served a single "
            "term in the House during one "
            "of the quieter periods in "
            "American congressional history "
            "— the Era of Good Feelings "
            "under Monroe, when the collapse "
            "of organized Federalist opposition "
            "produced a surface unity in "
            "Democratic-Republican politics "
            "that masked growing factional "
            "tensions.\n\n"
            "His long life (1759–1846) meant "
            "that he outlived his more "
            "famous brother and witnessed "
            "the full transformation of "
            "American politics from the "
            "Founding era through the "
            "Jacksonian period and the "
            "beginnings of the sectional crisis.\n\n"
            "He is primarily notable today "
            "for his family connection to the Vice Presidency."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 3,
            "significanceNarrative": "New York Congressman (1817–1821) during the Era of Good Feelings; brother of Vice President Daniel D. Tompkins; his congressional service coincided with his brother's vice-presidency; long-lived figure (1759–1846) spanning the Founding to Jacksonian eras.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Tompkins family's political prominence in New York — Daniel D. Tompkins's success as a popular governor and eventual Vice President reflected the family's standing in New York's Democratic-Republican political culture — created the social and political context for Caleb's congressional career",
            "The Era of Good Feelings' single-party political culture — the absence of meaningful Federalist competition in 1817–1821 that made Democratic-Republican nominees essentially uncontested in many districts — reduced the barriers to congressional service for connected figures like Caleb Tompkins",
            "New York's growing political importance in the early republic — as the most populous state, New York's congressional delegation was both large and influential, creating multiple slots for the state's political families to fill"
        ],
        "effects": [
            "His single congressional term contributed New York's vote to the House's deliberations during the final years of the Era of Good Feelings — a period of surface political unity before the sectional tensions of the Missouri Crisis and the 1824 election fragmented the Democratic-Republican consensus",
            "His career illustrated the family-network dimension of early American congressional politics — the prominent political families whose multiple members simultaneously occupied offices at different levels of government",
            "His longevity (87 years, dying in 1846) made him a living connection between the founding era and the antebellum period — one of the last survivors of the generation that had known the founding generation personally",
            "His family relationship to Vice President Daniel D. Tompkins provided him whatever influence and access he had in national politics — illustrating the importance of family connections in the social world of early American political life"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1817–1821"},
            {"target": "daniel-d-tompkins", "verb": "SIBLING_OF", "note": "Brother of Vice President Daniel D. Tompkins"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Congressional service during the Monroe era"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "New York Democratic-Republican congressman"},
            {"target": "james-monroe", "verb": "SERVES_UNDER", "note": "Congressman during Monroe's presidency"}
        ]
    }),

    ("jesse-wharton", {
        "summary": (
            "Jesse Wharton (1782–1833) was an "
            "American politician from Tennessee "
            "who served in the U.S. House of "
            "Representatives (1807–1809, 1813–1815) "
            "and briefly as a U.S. Senator "
            "from Tennessee (1814–1815). His "
            "political career reflected the "
            "early development of Tennessee "
            "as a state — admitted to the Union "
            "only in 1796, Tennessee was still "
            "building its political institutions "
            "and establishing its congressional "
            "representation in the first decade "
            "of the nineteenth century.\n\n"
            "Tennessee in this period was "
            "dominated by a culture of "
            "military leadership and frontier "
            "politics — the world that produced "
            "Andrew Jackson, who was already "
            "the dominant figure in Tennessee "
            "politics as Wharton served in "
            "Congress. The state's politics "
            "revolved around the Nashville "
            "legal and planter elite — the "
            "social world from which Wharton "
            "and his congressional contemporaries "
            "emerged.\n\n"
            "His Senate tenure (filling a "
            "vacancy from November 1814 to "
            "October 1815) was brief but "
            "placed him in the Senate during "
            "the War of 1812's final months "
            "— including the negotiations "
            "that produced the Treaty of "
            "Ghent and the famous Battle "
            "of New Orleans.\n\n"
            "He represented Tennessee's "
            "early Jeffersonian Republican "
            "frontier political tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Tennessee Congressman (1807–1809, 1813–1815) and brief U.S. Senator (1814–1815); served during the War of 1812's final months including the Battle of New Orleans period; part of Tennessee's early Jeffersonian Republican political elite in Andrew Jackson's political world.",
            "significanceCategory": "local"
        },
        "causes": [
            "Tennessee's rapid political development as a frontier state admitted in 1796 — the building of congressional institutions, legal culture, and political networks in a frontier society that was simultaneously settling its territory and establishing representative government — created the political world in which Wharton's career developed",
            "The War of 1812's political mobilization of the South and West — which made Tennessee a central theater both militarily (Jackson's campaigns) and politically (the western states' enthusiastic support for the war) — provided the political context for Wharton's Senate appointment during the conflict's final months",
            "The Nashville planter and legal elite's political dominance in early Tennessee — the small social world of prominent Tennessee families whose connections to each other and to Andrew Jackson determined access to political office — created the network through which Wharton's political career advanced"
        ],
        "effects": [
            "His brief Senate service during the War of 1812's final months placed him in the Senate during the Treaty of Ghent negotiations and the Battle of New Orleans — the famous American victory that transformed Andrew Jackson into a national hero",
            "His House service contributed Tennessee's frontier Republican perspective to congressional deliberations in the pre-War of 1812 years — representing a state that was among the most enthusiastic for westward expansion and resistance to British impressment",
            "His career contributed to the development of Tennessee's congressional tradition — the state's growing presence in national politics that would culminate in Andrew Jackson's national political domination in the 1820s–1830s",
            "His political career illustrated the early Tennessee political world — the frontier elite that Andrew Jackson had helped create and that provided the social and political base for Jacksonian Democracy's eventual national triumph"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Tennessee Congressman 1807–1809 and 1813–1815"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Tennessee Senator filling vacancy 1814–1815"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Senator during the war's final months"},
            {"target": "battle-of-new-orleans", "verb": "SENATOR_DURING", "note": "In Senate during Jackson's famous victory"},
            {"target": "tennessee", "verb": "REPRESENTS", "note": "Early Tennessee frontier Republican politician"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 61 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
