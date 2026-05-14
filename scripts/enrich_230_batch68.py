#!/usr/bin/env python3
"""
Batch 68 — 8 entities: Gideon Tomlinson, Jonas Platt, Joseph Webber Jackson,
Archibald Campbell 2nd Earl of Argyll, John Reynolds, Jonathan G. Hunton,
Smith Thompson, Adam W. Snyder
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

    ("gideon-tomlinson", {
        "summary": (
            "Gideon Tomlinson (1780–1854) "
            "was an American Democratic-Republican "
            "and Jacksonian Democratic politician "
            "from Connecticut who served as "
            "a U.S. Representative (1819–1827), "
            "Governor of Connecticut (1827–1831), "
            "and U.S. Senator (1831–1837). "
            "His career traced the full "
            "trajectory of the early "
            "national period's political "
            "transformation — from "
            "the Era of Good Feelings "
            "through the Jacksonian "
            "revolution — serving "
            "in all three levels of "
            "major elective office "
            "(House, Governor, Senate) "
            "during the most politically "
            "turbulent decades of the "
            "early republic.\n\n"
            "Connecticut was a competitive "
            "state in this era — "
            "gradually transitioning "
            "from its old Federalist "
            "dominance through the "
            "Democratic-Republican "
            "era and into the "
            "Jacksonian bifurcation "
            "between Jackson Democrats "
            "and National Republicans "
            "(later Whigs). Tomlinson "
            "navigated this transition.\n\n"
            "His Senate service "
            "(1831–1837) coincided "
            "with the Bank War — "
            "Jackson's destruction "
            "of the Second Bank "
            "of the United States "
            "— and the emergence "
            "of the Whig Party "
            "in opposition to "
            "Jacksonian policies.\n\n"
            "He was among Connecticut's "
            "most prominent antebellum politicians."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut politician serving as Congressman (1819–1827), Governor (1827–1831), and Senator (1831–1837); traced the full political transformation from Era of Good Feelings through Jacksonian democracy; served during the Bank War and emergence of the Whig Party; among the few antebellum politicians to hold all three major elective offices.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's political transformation from Federalist to Democratic-Republican dominance — the gradual erosion of Federalist control as the national party collapsed and the Democratic-Republicans reorganized — created the political opportunity structure that Tomlinson's career exploited",
            "The Era of Good Feelings' false unity — the apparently nonpartisan political consensus that masked deep factional tensions within the Democratic-Republican Party — created the political context for Tomlinson's House and gubernatorial career before the Jacksonian fracturing",
            "The Jacksonian political revolution — Andrew Jackson's transformation of Democratic politics, the Bank War, and the emergence of the Democrat-Whig party system — shaped the context of Tomlinson's Senate service and his navigation of the new political alignments"
        ],
        "effects": [
            "His three-level political career contributed to Connecticut's governance at all levels — House, governor, and Senate — during the critical political transition from the Era of Good Feelings to the Jacksonian Democracy",
            "His gubernatorial service contributed to Connecticut's institutional development — managing state affairs through the political transition period when Connecticut was gradually reforming its old colonial constitutional structures",
            "His Senate service contributed to the Bank War debates — representing Connecticut's perspective in one of the most consequential domestic policy fights of the antebellum era",
            "His career illustrated the political career trajectories available in the early republic — the pathway from House to governorship to Senate that represented ambition and the accumulation of political capital across multiple offices"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1819–1827"},
            {"target": "connecticut", "verb": "GOVERNS", "note": "Governor of Connecticut 1827–1831"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1831–1837"},
            {"target": "bank-war", "verb": "SERVES_DURING", "note": "Senator during Jackson's Bank War"},
            {"target": "jacksonian-democracy", "verb": "PARTICIPATES_IN", "note": "Jacksonian Democratic politician"}
        ]
    }),

    ("jonas-platt", {
        "summary": (
            "Jonas Platt (1769–1834) was "
            "an American Federalist politician "
            "and jurist from New York who "
            "served in the U.S. House of "
            "Representatives (1799–1801) "
            "and had a distinguished career "
            "as a New York Supreme Court "
            "Justice (1814–1821). He "
            "was closely associated with "
            "the Federalist tradition "
            "in New York — a tradition "
            "represented by figures like "
            "Alexander Hamilton, John Jay, "
            "and Gouverneur Morris, who "
            "dominated New York's commercial "
            "and professional elite.\n\n"
            "Platt's law career was closely "
            "intertwined with some of "
            "the most important legal "
            "developments in early New "
            "York jurisprudence — he "
            "was an associate and "
            "contemporary of James Kent, "
            "whose 'Commentaries on "
            "American Law' became one "
            "of the foundational texts "
            "of American common law.\n\n"
            "New York in this period "
            "was the most commercially "
            "important state in the "
            "Union — the center of "
            "American trade, finance, "
            "and commerce — and its "
            "legal system was being "
            "developed by jurists like "
            "Platt and Kent whose "
            "work shaped the legal "
            "framework of American "
            "commercial capitalism.\n\n"
            "He contributed significantly "
            "to New York jurisprudence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Federalist Congressman (1799–1801) and Supreme Court Justice (1814–1821); part of the Hamilton-Jay-Kent Federalist legal tradition; contributed to early New York jurisprudence during the state's development as America's commercial center; contemporary and associate of James Kent whose Commentaries shaped American common law.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Federalist commercial elite — the merchants, lawyers, and financiers who had supported Hamilton's economic program and whose commercial interests aligned with Federalist trade and banking policy — created the political and social environment for Platt's Federalist career",
            "New York's legal development as the commercial capital of the early republic — the need for sophisticated commercial jurisprudence to govern the complex transactions of America's largest trading center — created the demand for the legal expertise that Platt and his contemporaries like James Kent provided",
            "The Federalist tradition's dominance in New York's legal elite — Hamilton's Constitution ratification fight, Jay's governorship, and the development of New York's legal institutions under Federalist leadership — created the network within which Platt's career developed"
        ],
        "effects": [
            "His New York Supreme Court service contributed to the development of New York commercial law — the jurisprudence that governed the complex transactions of America's most important commercial state",
            "His association with James Kent contributed to the development of New York's Federalist legal tradition — the classical common law jurisprudence that Kent systematized in his Commentaries and that shaped American law throughout the nineteenth century",
            "His House service contributed the Federalist perspective during the Adams administration's final year and the beginning of the Jeffersonian Revolution of 1800 — representing the Federalist commercial establishment's interests in the new government",
            "His career illustrated the close connection between Federalist politics and New York's commercial legal elite — the lawyers who served both as political representatives of Federalist interests and as the architects of the commercial jurisprudence those interests required"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1799–1801"},
            {"target": "new-york-supreme-court", "verb": "SERVES_AS_JUSTICE", "note": "Justice 1814–1821"},
            {"target": "james-kent", "verb": "ASSOCIATES_WITH", "note": "Contemporary in New York's Federalist legal tradition"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New York Federalist in the Hamilton tradition"},
            {"target": "new-york", "verb": "SERVES", "note": "New York lawyer and jurist shaping commercial jurisprudence"}
        ]
    }),

    ("joseph-webber-jackson", {
        "summary": (
            "Joseph Webber Jackson (1796–1854) "
            "was an American Democratic "
            "politician from Georgia who "
            "served in the U.S. House "
            "of Representatives (1847–1849) "
            "during the critical period "
            "of the Mexican-American War "
            "and the Wilmot Proviso debate "
            "— the explosive congressional "
            "fight over whether slavery "
            "should be prohibited in "
            "the territories acquired "
            "from Mexico. As a Georgia "
            "Democrat, Jackson represented "
            "the Southern perspective "
            "that opposed any restriction "
            "on slavery's expansion "
            "into the new territories.\n\n"
            "Georgia in this era "
            "was a rapidly developing "
            "cotton-economy state — "
            "still in the process of "
            "building its plantation "
            "agriculture westward "
            "into the fertile lands "
            "of the interior — and "
            "its political class "
            "was deeply invested in "
            "the protection of "
            "slaveholder rights and "
            "the expansion of "
            "slave-based agriculture.\n\n"
            "His one term in Congress "
            "coincided with the "
            "opening phase of the "
            "sectional crisis that "
            "would eventually produce "
            "the Compromise of 1850 "
            "and, ultimately, the "
            "Civil War.\n\n"
            "He died in 1854, before "
            "the Kansas-Nebraska Act."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Georgia Democratic Congressman (1847–1849); served during the Mexican-American War and Wilmot Proviso debates; represented Georgia's pro-slavery cotton-economy perspective in the opening phase of the sectional crisis; died in 1854 before the Kansas-Nebraska Act intensified the conflict he had witnessed beginning.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Mexican-American War (1846–1848) — the U.S. conquest of vast territories from Mexico that immediately raised the question of slavery's status in the new territories — created the political crisis that defined Jackson's entire congressional career",
            "The Wilmot Proviso (1846) — the proposal to prohibit slavery in all territories acquired from Mexico, which passed the House but failed in the Senate — created the defining sectional divide of the late 1840s and the political controversy that Jackson had to navigate as a Southern Democrat",
            "Georgia's cotton economy and plantation agriculture — the state's deep material and ideological investment in slavery as the foundation of its economic and social order — created the political constituency that sent Jackson to Congress as a defender of Southern rights"
        ],
        "effects": [
            "His House service contributed Georgia's Democratic vote to the critical Wilmot Proviso fights — opposing the antislavery restriction and defending Southern rights to bring enslaved people into any new territory",
            "His brief congressional career contributed to the Southern Democratic bloc that ultimately prevented the Wilmot Proviso from becoming law — ensuring that the territories' status remained unresolved and requiring the Compromise of 1850's more complex settlement",
            "His career illustrated the pattern of Georgia's antebellum congressional delegation — the one-term representatives who defended slavery and Southern rights during the escalating sectional crisis",
            "His death in 1854 — the year the Kansas-Nebraska Act opened the territorial question again with even more explosive results — placed him among the Southern politicians who witnessed the sectional crisis's beginnings but not its climax"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Georgia Congressman 1847–1849"},
            {"target": "wilmot-proviso", "verb": "OPPOSES", "note": "Southern Democrat opposing slavery restriction"},
            {"target": "mexican-american-war", "verb": "SERVES_DURING", "note": "Congressman during the war and territorial debates"},
            {"target": "georgia", "verb": "REPRESENTS", "note": "Georgia cotton-economy Democratic congressman"},
            {"target": "slavery-expansion-debate", "verb": "PARTICIPATES_IN", "note": "Part of the antebellum slavery extension controversy"}
        ]
    }),

    ("archibald-campbell-2nd-earl-of-argyll", {
        "summary": (
            "Archibald Campbell, 2nd Earl of "
            "Argyll (c. 1458–1513) was a "
            "Scottish nobleman, royal "
            "administrator, and military "
            "commander who served as "
            "Lord High Chancellor of "
            "Scotland under James IV "
            "— one of the highest offices "
            "in the Scottish kingdom. "
            "He was killed at the "
            "Battle of Flodden (1513) "
            "— the catastrophic Scottish "
            "defeat at the hands of "
            "the English in which "
            "King James IV himself "
            "was killed along with "
            "a devastating proportion "
            "of the Scottish nobility "
            "and army.\n\n"
            "Flodden was one of the "
            "worst military defeats "
            "in Scottish history — "
            "Scotland's invasion of "
            "England in support of "
            "France (the Auld Alliance) "
            "while Henry VIII was "
            "campaigning in France "
            "ended in total disaster, "
            "killing the king and "
            "a disproportionate "
            "share of Scotland's "
            "political and military "
            "leadership.\n\n"
            "As Lord High Chancellor, "
            "Argyll was the head "
            "of Scotland's judicial "
            "and administrative "
            "system — the king's "
            "chief minister with "
            "oversight of the "
            "courts and executive "
            "governance.\n\n"
            "His death at Flodden "
            "was part of Scotland's "
            "national catastrophe."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Scottish Lord High Chancellor under James IV; killed at Flodden (1513) — one of Scotland's worst military catastrophes; part of the devastating Scottish nobility loss when King James IV and a generation of Scottish leaders died in the English victory; representative of the Auld Alliance's catastrophic consequences.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Auld Alliance between Scotland and France — the centuries-old diplomatic and military alliance that committed Scotland to support France against England — obligated Scotland to invade England in 1513 while Henry VIII was campaigning in France, creating the conditions for Flodden",
            "James IV's ambition and military confidence — the king's determination to take personal command of the invasion force and his underestimation of the English force under Surrey — created the conditions for the catastrophic Scottish defeat",
            "The Campbell family's dominance of Scottish Highland politics — the earls of Argyll's control of western Highland territories and their role as the Scottish crown's key intermediaries with the Highland clans — provided Argyll the political base and military resources that made the chancellorship a natural culmination"
        ],
        "effects": [
            "His death at Flodden — along with the king and an extraordinary proportion of the Scottish nobility — created a massive leadership vacuum in Scotland, requiring the regency of the young James V and fundamentally weakening Scottish governance for years",
            "His chancellorship built on the institutional development of the Scottish crown's administrative capacity — the development of Scottish royal government under James IV that was advancing Scotland toward more effective governance before Flodden's catastrophe interrupted it",
            "The Flodden disaster — in which Argyll and so many other Scottish leaders died — contributed to the long-term weakening of Scottish power relative to England and to the eventual conditions that made union with England more plausible",
            "His career illustrated the dual role of Scotland's great magnates as both regional power-holders and national royal administrators — the way the earls of Argyll combined Highland territorial power with service to the Scottish crown"
        ],
        "relationships": [
            {"target": "james-iv-scotland", "verb": "SERVES", "note": "Lord High Chancellor under James IV"},
            {"target": "battle-of-flodden-1513", "verb": "KILLED_AT", "note": "Died in the catastrophic Scottish defeat"},
            {"target": "scotland", "verb": "GOVERNS", "note": "Lord High Chancellor of Scotland"},
            {"target": "auld-alliance", "verb": "UPHOLDS", "note": "Died serving the French alliance commitment"},
            {"target": "campbell-family", "verb": "LEADS", "note": "Head of the Campbell earl of Argyll dynasty"}
        ]
    }),

    ("john-reynolds", {
        "summary": (
            "John Reynolds (1788–1865) was "
            "an American Democratic politician "
            "and jurist from Illinois who "
            "served as Governor of Illinois "
            "(1830–1834) and as a U.S. "
            "Representative (1834–1837 "
            "and 1839–1843). As governor, "
            "he oversaw the Black Hawk "
            "War (1832) — the last Native "
            "American conflict in the "
            "Old Northwest, in which "
            "Sauk and Fox people led "
            "by Black Hawk crossed "
            "back into Illinois "
            "seeking to reclaim ceded "
            "lands, leading to a "
            "brutal military campaign "
            "that ended their resistance "
            "and opened the upper "
            "Mississippi valley to "
            "white settlement.\n\n"
            "Reynolds led the state "
            "militia call-up during "
            "the Black Hawk War "
            "and worked closely "
            "with federal military "
            "forces — including "
            "young Abraham Lincoln, "
            "who served briefly "
            "in the Illinois militia "
            "during the conflict.\n\n"
            "Illinois was in this "
            "period a rapidly developing "
            "frontier state — growing "
            "explosively as the "
            "Black Hawk War's "
            "conclusion opened "
            "northern Illinois "
            "to settlement.\n\n"
            "He also wrote historical "
            "accounts of early Illinois."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Governor of Illinois (1830–1834) who oversaw the Black Hawk War (1832) — the last Native American conflict in the Old Northwest; led the militia call-up that included young Abraham Lincoln; his governorship opened northern Illinois to white settlement; also served as Congressman (1834–1837, 1839–1843) and wrote early Illinois history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Black Hawk War (1832) — the Sauk leader Black Hawk's return across the Mississippi with a band seeking to reclaim ceded Illinois lands — created the military crisis that defined Reynolds's governorship and required the mobilization of the Illinois state militia",
            "Illinois's frontier development and the pressure for Native American removal — the rapidly growing settler population's demand for the rich agricultural lands of northern Illinois that Native American communities still occupied — created the political context for the aggressive state response to Black Hawk's return",
            "Illinois's explosive population growth — the state's rapid transformation from frontier territory to developing agricultural state in the 1820s–1830s — created both the political ambition for a governorship and the complex governance challenges that Reynolds had to manage"
        ],
        "effects": [
            "His governorship's management of the Black Hawk War contributed to the final expulsion of Native Americans from Illinois — the military campaign that ended Native American resistance in the Old Northwest and opened northern Illinois to the white settlement that rapidly followed",
            "The Black Hawk War's military mobilization — in which Abraham Lincoln served his brief Illinois militia stint — contributed to the veterans' political network and cultural memory that shaped Illinois politics for decades",
            "His congressional service contributed Illinois's Democratic perspective to the Jacksonian era's major debates — the Bank War, the emerging sectional conflicts, and the frontier states' development interests",
            "His historical writings contributed to the early documentation of Illinois history — preserving accounts of the frontier state's development that subsequent historians have relied upon"
        ],
        "relationships": [
            {"target": "illinois", "verb": "GOVERNS", "note": "Governor of Illinois 1830–1834"},
            {"target": "black-hawk-war", "verb": "COMMANDS_DURING", "note": "Oversaw the Illinois response to the 1832 conflict"},
            {"target": "abraham-lincoln", "verb": "MOBILIZES_MILITIA_WITH", "note": "Lincoln served in the militia Reynolds called up"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Illinois Congressman 1834–1837 and 1839–1843"},
            {"target": "native-american-removal", "verb": "IMPLEMENTS", "note": "Governorship opened northern Illinois through Native removal"}
        ]
    }),

    ("jonathan-g-hunton", {
        "summary": (
            "Jonathan Goodhue Hunton "
            "(1780–1851) was an American "
            "politician from Maine who "
            "served as Governor of Maine "
            "(1830–1831) — a brief "
            "one-year term that represented "
            "the National Republican "
            "(proto-Whig) Party's hold "
            "on the governorship during "
            "the Jacksonian era's "
            "political transformation. "
            "Maine, admitted to the "
            "Union in 1820 as part "
            "of the Missouri Compromise "
            "settlement, was still "
            "building its state institutions "
            "and political culture "
            "through this period.\n\n"
            "Hunton's governorship "
            "was brief — he served "
            "only about a year "
            "before the Democrats "
            "regained the governorship "
            "— but his National "
            "Republican affiliation "
            "placed him in the "
            "anti-Jacksonian tradition "
            "that would develop "
            "into the Whig Party "
            "later in the 1830s.\n\n"
            "Maine in this era "
            "was one of the newest "
            "states — separated "
            "from Massachusetts "
            "only in 1820 — and "
            "was building its "
            "political institutions "
            "while managing the "
            "challenges of a "
            "maritime and timber "
            "economy.\n\n"
            "He was a lawyer and "
            "businessman before "
            "his political career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Governor of Maine (1830–1831); National Republican in the anti-Jacksonian tradition; from one of the newest states (separated from Massachusetts 1820); brief governorship during the Jacksonian transformation that swept National Republicans from office; part of Maine's foundational political development.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maine's separation from Massachusetts (1820) as part of the Missouri Compromise — the new state's need to build its political institutions from scratch — created the competitive political environment that produced Hunton's gubernatorial election",
            "The National Republican political tradition — the anti-Jacksonian coalition that defended the American System of internal improvements, protective tariffs, and national bank that Jackson opposed — provided the political identity for Hunton's governorship",
            "Maine's maritime and timber economy — the state's commercial interests in tariff protection, infrastructure development, and stable banking — aligned naturally with the National Republican-Whig political tradition that Hunton represented"
        ],
        "effects": [
            "His gubernatorial year contributed to Maine's governance during a critical period of state development — managing the affairs of a young state still building its institutions during the political turbulence of the Jacksonian transition",
            "His National Republican governorship represented the anti-Jacksonian tradition's brief hold on Maine governance before the Democrats reasserted their dominance — illustrating Maine's political competitiveness in the early 1830s",
            "His career contributed to the development of Maine's anti-Jacksonian political tradition — the National Republican-Whig heritage that would eventually give rise to Maine's strong Whig and then Republican Party in subsequent decades",
            "His brief tenure illustrated the volatility of Maine politics during the Jacksonian realignment — the rapid succession of partisan control that characterized politically contested states during the great political transformation of the 1820s–1830s"
        ],
        "relationships": [
            {"target": "maine", "verb": "GOVERNS", "note": "Governor of Maine 1830–1831"},
            {"target": "national-republican-party", "verb": "MEMBER_OF", "note": "National Republican in the anti-Jackson tradition"},
            {"target": "whig-party-united-states", "verb": "PRECEDES", "note": "National Republican who preceded Whig formation"},
            {"target": "maine-statehood-1820", "verb": "GOVERNS_AFTER", "note": "Governor of the young state separated from Massachusetts"},
            {"target": "jacksonian-democracy", "verb": "OPPOSES", "note": "Anti-Jacksonian governor during the Jacksonian transformation"}
        ]
    }),

    ("smith-thompson", {
        "summary": (
            "Smith Thompson (1768–1843) was "
            "an American lawyer and jurist "
            "from New York who served as "
            "U.S. Secretary of the Navy "
            "(1818–1823) under President "
            "Monroe and as an Associate "
            "Justice of the U.S. Supreme "
            "Court (1823–1843) — appointed "
            "by Monroe and serving on "
            "the Court for twenty years. "
            "His Court tenure coincided "
            "with the transition from "
            "the Marshall Court's broad "
            "nationalism to the Taney "
            "Court's states'-rights "
            "Democratic jurisprudence — "
            "Thompson occupying a "
            "middle position that "
            "sometimes sided with "
            "Marshall and sometimes "
            "with the states'-rights camp.\n\n"
            "Thompson had previously "
            "served as Chief Justice "
            "of the New York Supreme "
            "Court (1814–1818) under "
            "Governor Tompkins — "
            "a position that gave "
            "him substantial judicial "
            "experience before his "
            "federal appointment.\n\n"
            "He ran against Martin "
            "Van Buren for the "
            "New York governorship "
            "in 1828 while sitting "
            "as a Supreme Court "
            "Justice — an extraordinary "
            "action by modern standards "
            "but not unusual in the "
            "early republic.\n\n"
            "He was a substantial "
            "figure in American law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Secretary of the Navy (1818–1823) and Supreme Court Associate Justice (1823–1843); Chief Justice of New York Supreme Court; twenty-year Court tenure spanning Marshall-to-Taney transition; ran for New York Governor while a sitting Justice (1828) — unusual even by early republic standards; substantial figure in American constitutional development.",
            "significanceCategory": "regional"
        },
        "causes": [
            "President Monroe's court appointment strategy — seeking a senior New York Republican with judicial experience and national policy background for the Court vacancy — created the appointment that elevated Thompson from Navy Secretary to Supreme Court Justice",
            "Thompson's New York judicial career — his Chief Justice tenure on New York's Supreme Court that gave him substantial experience in the common law, equity, and constitutional questions that federal courts addressed — provided the qualification for his Supreme Court appointment",
            "The Marshall Court's nationalism versus states'-rights tension — the ongoing constitutional debate over federal versus state power that defined the Marshall era — created the intellectual environment within which Thompson developed his middle-position jurisprudence"
        ],
        "effects": [
            "His twenty-year Supreme Court tenure contributed to the Court's jurisprudence during the critical Marshall-to-Taney transition — providing a moderating voice between the extreme nationalism of Story and the extreme states'-rights position of Taney-era Democrats",
            "His gubernatorial campaign in 1828 while a sitting Justice — one of the only instances of an active Supreme Court member running for major elective office — raised important questions about judicial independence that contributed to evolving norms of judicial conduct",
            "His Navy Secretaryship contributed to the development of the U.S. Navy during the post-War of 1812 buildup — the department's expansion and professionalization during Monroe's presidency",
            "His career trajectory — New York judge to Navy Secretary to Supreme Court Justice — illustrated the fluid career paths of early republic elite lawyers who moved between judicial, executive, and elective roles"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1823–1843"},
            {"target": "james-monroe", "verb": "SERVES_UNDER", "note": "Navy Secretary and Monroe's Court appointment"},
            {"target": "new-york-supreme-court", "verb": "PRESIDES_OVER", "note": "Chief Justice 1814–1818"},
            {"target": "martin-van-buren", "verb": "OPPOSES", "note": "Ran against Van Buren for New York governor in 1828"},
            {"target": "marshall-court", "verb": "SERVES_ON", "note": "Justice during the Marshall era's final decade"}
        ]
    }),

    ("adam-w-snyder", {
        "summary": (
            "Adam Wilson Snyder (1799–1842) "
            "was an American Democratic "
            "politician from Illinois who "
            "was nominated as the Democratic "
            "candidate for Governor of "
            "Illinois in 1842 — but died "
            "before the election, becoming "
            "one of those political figures "
            "whose potential was cut short "
            "by premature death. He "
            "had previously served in "
            "the Illinois state legislature "
            "and as a U.S. Representative "
            "(1837–1839).\n\n"
            "His congressional service "
            "coincided with the Van "
            "Buren administration and "
            "the Panic of 1837 — "
            "the economic depression "
            "that devastated Van Buren's "
            "presidency. As an Illinois "
            "Democrat, Snyder supported "
            "the hard-money, Independent "
            "Treasury policies that "
            "Democrats advocated "
            "in response to the panic.\n\n"
            "Illinois in this era "
            "was in the midst of "
            "explosive development "
            "— the Black Hawk War "
            "(1832) had cleared "
            "northern Illinois for "
            "settlement, the state's "
            "population was growing "
            "rapidly, and the "
            "economic opportunities "
            "of the developing "
            "prairie state were "
            "attracting settlers.\n\n"
            "His death at 43 before "
            "the election cut short "
            "a promising political career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Illinois Democratic Congressman (1837–1839) and 1842 gubernatorial nominee who died before the election; served during the Panic of 1837; part of the Jacksonian Democratic machine in a rapidly developing frontier Illinois; death at 43 cut short what may have been a significant gubernatorial career.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Illinois's rapid frontier development after the Black Hawk War — the explosive settlement of northern Illinois in the 1830s that created a rapidly growing state with expanding political institutions and ambitions — created the political environment for Snyder's rising career",
            "The Jacksonian Democratic machine's dominance in frontier Illinois — the state's strongly Democratic population of Ohio Valley and Upper South migrants whose Jacksonian instincts shaped state politics — provided the political organization that supported Snyder's congressional career and gubernatorial nomination",
            "The Panic of 1837 and the hard-money debate — the economic crisis and the Democratic response (Independent Treasury) versus the Whig alternative (re-chartered national bank) — defined the major policy debate of Snyder's congressional career"
        ],
        "effects": [
            "His congressional service contributed Illinois's Democratic vote to the Van Buren era's critical economic policy debates — the Independent Treasury debates, the Panic's policy responses, and the Jacksonian hard-money tradition",
            "His gubernatorial nomination illustrated the Illinois Democratic Party's confidence in his political abilities — the party's selection of him as their candidate for the state's top office reflected his standing in Illinois Democratic circles",
            "His death before the election — forcing the Democratic Party to replace him on the ticket — disrupted the 1842 Illinois Democratic campaign and contributed to a political transition in state leadership",
            "His career illustrated the trajectory of young ambitious Illinois Democrats in the Jacksonian era — the lawyers and politicians who built careers in the rapidly developing frontier state and whose premature deaths sometimes cut short what might have been more consequential careers"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Illinois Congressman 1837–1839"},
            {"target": "illinois", "verb": "REPRESENTS", "note": "Illinois Democratic politician and gubernatorial nominee"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Congressman during the economic depression"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Democrat during Van Buren's presidency"},
            {"target": "jacksonian-democracy", "verb": "PARTICIPATES_IN", "note": "Part of the Illinois Jacksonian Democratic machine"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 68 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
