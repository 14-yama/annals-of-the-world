#!/usr/bin/env python3
"""
Batch 45 — 8 entities: Magnus Gabriel De la Gardie, William C. Preston,
Denis-Benjamin Viger, David Emanuel, Benjamin Taliaferro,
José Damián Villacorta, Benjamin Chew Howard, Jean-Baptiste Robert Lindet
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

    # 1 — Magnus Gabriel De la Gardie
    ("magnus-gabriel-de-la-gardie", {
        "summary": (
            "Count Magnus Gabriel De la Gardie (1622–1686) was "
            "a Swedish nobleman and statesman who became the "
            "most powerful figure in Sweden's government during "
            "the regency for King Charles XI (1660–1672) — "
            "holding three of the five Great Offices of the "
            "Realm simultaneously (Lord High Treasurer, Lord "
            "High Chancellor, and Lord High Steward) and "
            "serving as the Privy Council's dominant voice. "
            "Born to a French-origin noble family that had "
            "settled in Sweden, he was the son of Field Marshal "
            "Jacob De la Gardie and a close friend and favorite "
            "of Queen Christina.\n\n"
            "His political dominance during the regency period "
            "was accompanied by extraordinary cultural patronage: "
            "he built several of Sweden's most magnificent Baroque "
            "palaces, assembled a vast library, and patronized "
            "artists and scholars — making him a central figure "
            "of Sweden's 17th-century cultural Golden Age. "
            "He served as Governor-General of Livonia "
            "(the Swedish Baltic province of present-day "
            "Latvia and Estonia) — one of Sweden's most "
            "strategically important imperial possessions.\n\n"
            "His career ended in spectacular humiliation: "
            "King Charles XI, having assumed direct rule, "
            "implemented the Great Reduction (Reduktion) of 1680 — "
            "a massive crown reclamation of noble estates "
            "that had been alienated to the nobility during "
            "the regency period. De la Gardie, who had "
            "accumulated one of Sweden's largest noble fortunes, "
            "lost the majority of his estates and was ruined "
            "financially — reduced from one of Europe's "
            "wealthiest nobles to relative poverty in his "
            "final years.\n\n"
            "His rise and fall traced the full arc of "
            "Sweden's Age of Greatness and its contradictions "
            "— imperial expansion built on noble privilege "
            "that the monarchy eventually reclaimed."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Swedish statesman; held three of five Great Offices of the Realm during the Charles XI regency (1660–1672) — Lord High Treasurer, Lord High Chancellor, Lord High Steward; de facto regent of Sweden; Governor-General of Livonia; extraordinary Baroque cultural patron; ruined by Charles XI's Great Reduction (Reduktion) of 1680; his career traced the full arc of Sweden's Age of Greatness and its noble-monarchy contradictions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The death of King Charles X Gustav in 1660 — leaving a four-year-old heir (Charles XI) — created the regency vacuum that De la Gardie filled, as the most prominent and court-connected noble of the era, becoming de facto head of Sweden's government during the twelve-year minority",
            "Sweden's Age of Greatness (Stormaktstiden) — in which the Swedish Empire had expanded across the Baltic through military conquest — created both the imperial administrative roles (like the Livonia Governor-Generalship) and the noble landholding culture that accumulated in De la Gardie's hands and made him one of Europe's wealthiest men",
            "Charles XI's determination to reassert royal authority over the Swedish nobility — and his conviction that the regency period had allowed excessive alienation of crown lands to noble families — created the political will for the Great Reduction of 1680 that destroyed De la Gardie's fortune and ended his political influence"
        ],
        "effects": [
            "His twelve-year de facto regency contributed to Sweden's governance during a critical period of the Swedish Empire — managing foreign policy, military affairs, and domestic administration at the apex of Sweden's imperial power in the late 17th century",
            "His cultural patronage contributed to Sweden's 17th-century cultural Golden Age — his library, palace-building program, and support for scholars and artists making him one of the most significant cultural patrons in Scandinavian history",
            "His ruin by the Great Reduction of 1680 contributed to the most significant redistribution of noble property in Swedish history — becoming the most emblematic example of the consequences of Charles XI's reassertion of royal authority over the nobility, demonstrating that even Sweden's most powerful nobleman was not immune to royal reclamation",
            "His Governor-Generalship of Livonia contributed to Swedish imperial administration of the Baltic provinces — managing one of the empire's most economically and strategically important territories during the peak of Sweden's Baltic hegemony"
        ],
        "relationships": [
            {"entity": "Charles XI regency (1660–1672, de facto regent as head of Privy Council)", "relationship": "DE_FACTO_REGENT_DURING", "note": "Served as de facto regent of Sweden during the twelve-year minority of Charles XI — holding three of the five Great Offices and dominating the Privy Council"},
            {"entity": "Great Reduction / Reduktion of 1680 (Charles XI's estate reclamation)", "relationship": "RUINED_BY", "note": "Ruined by Charles XI's Great Reduction of 1680 — losing the majority of his vast noble estates and reduced from one of Europe's wealthiest men to relative poverty"},
            {"entity": "Swedish Livonia / Baltic imperial provinces (Governor-General)", "relationship": "GOVERNOR-GENERAL_OF", "note": "Served as Governor-General of Livonia — Sweden's Baltic province of present-day Latvia and Estonia, one of the empire's most strategically important possessions"},
            {"entity": "Queen Christina of Sweden (close friend and court favorite)", "relationship": "CLOSE_FRIEND_AND_FAVORITE_OF", "note": "A close friend and favorite of Queen Christina — his early career built on his connection to the Swedish court's most intellectually and politically dynamic figure"},
            {"entity": "Swedish Age of Greatness / Stormaktstiden (17th-century Swedish Empire)", "relationship": "REPRESENTATIVE_FIGURE_AND_CASUALTY_OF", "note": "A representative figure and ultimate casualty of Sweden's Age of Greatness — his career traced its full arc from imperial expansion and noble enrichment to royal reclamation and personal ruin"}
        ]
    }),

    # 2 — William C. Preston
    ("william-c-preston", {
        "summary": (
            "William Campbell Preston (1794–1860) was a South "
            "Carolina lawyer, orator, and politician who served "
            "as US Senator from South Carolina (1833–1842) — "
            "affiliating first with the Nullifier party during "
            "the Nullification Crisis, then transitioning to "
            "the Whig party — and later as President of South "
            "Carolina College (1845–1851). Educated in Virginia, "
            "Edinburgh, and at the Litchfield Law School, "
            "he was known as one of the most accomplished "
            "orators in the antebellum Senate.\n\n"
            "His Senate career began in the immediate aftermath "
            "of the Nullification Crisis (1832–1833) — the "
            "confrontation in which South Carolina declared "
            "federal tariff laws unconstitutional and Andrew "
            "Jackson threatened military force. Preston entered "
            "the Senate as a Nullifier, representing South "
            "Carolina's most assertive states'-rights tradition, "
            "and eventually aligned with the Whig opposition "
            "to Jacksonian democracy.\n\n"
            "His most vocal Senate positions were on slavery "
            "and abolitionism: he was among the most aggressive "
            "defenders of slavery in the antebellum Senate, "
            "arguing that abolitionists' petitions should not "
            "even be received by Congress — contributing to "
            "the debate over the 'gag rule' that suppressed "
            "antislavery petitions in the House and Senate "
            "from 1836 to 1844.\n\n"
            "His presidency of South Carolina College — "
            "the state's flagship educational institution — "
            "continued his public service after his Senate "
            "resignation, and his reputation as an orator "
            "outlasted his political career as one of the "
            "more eloquent defenders of the antebellum "
            "South's proslavery intellectual tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "South Carolina US Senator (1833–1842, Nullifier then Whig); vocal proslavery Senate orator; contributor to the 'gag rule' debate suppressing antislavery petitions; President of South Carolina College (1845–1851); one of the antebellum Senate's most accomplished orators; his career traces South Carolina's political trajectory from Nullification through Whig alignment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's Nullification Crisis (1832–1833) — in which the state declared federal tariff laws unconstitutional — created the political context for Preston's Senate career as a Nullifier, representing the state's most assertive states'-rights constitutional tradition",
            "The antebellum debate over slavery and the reception of abolitionists' petitions — which created the 'gag rule' controversy when southern senators insisted antislavery petitions not be received or debated — created the political arena for Preston's most vocal Senate contributions",
            "Preston's exceptional oratorical training — combined with his Edinburgh education, Litchfield legal training, and the South Carolina tradition of cultivating orator-politicians for the Senate — created the personal attributes that made him one of the Senate's most prominent voices despite representing a small state"
        ],
        "effects": [
            "His Senate advocacy contributed to the imposition of the gag rule that suppressed antislavery petitions in Congress from 1836 to 1844 — one of the most constitutionally contentious actions of the antebellum period, opposed by John Quincy Adams as a violation of the First Amendment right of petition",
            "His transition from Nullifier to Whig illustrated South Carolina's complex relationship with national party politics — a state whose distinctive constitutional doctrine (nullification) could not be fully accommodated within either Jacksonian Democrats or anti-Jackson Whigs, forcing its politicians into awkward alignments",
            "His presidency of South Carolina College contributed to the intellectual formation of the state's antebellum leadership class — presiding over the institution that trained the lawyers, politicians, and planters who would lead South Carolina into the secession crisis of 1860–1861",
            "His reputation as an orator contributed to the antebellum South's self-image as a culture of eloquence and classical learning — the tradition of planter-politician-scholar that distinguished the South Carolina Senate delegation from the more commercially oriented politicians of other states"
        ],
        "relationships": [
            {"entity": "US Senate from South Carolina (Nullifier then Whig, 1833–1842)", "relationship": "SENATOR", "note": "Served as US Senator from South Carolina (1833–1842) — affiliating with the Nullifier party then Whig, one of the Senate's most prominent orators and proslavery voices"},
            {"entity": "Nullification Crisis (1832–1833) / South Carolina Nullifier party", "relationship": "SENATOR_REPRESENTING_NULLIFIER_POSITION", "note": "Entered the Senate as a Nullifier in the aftermath of the Nullification Crisis — representing South Carolina's most assertive states'-rights constitutional tradition"},
            {"entity": "Gag rule debate (1836–1844, suppression of antislavery petitions in Congress)", "relationship": "CONTRIBUTED_TO_PASSAGE_OF", "note": "Among the most vocal Senate advocates for suppressing antislavery petitions — contributing to the gag rule that prevented Congress from receiving or debating abolitionists' petitions 1836–1844"},
            {"entity": "South Carolina College (President, 1845–1851)", "relationship": "PRESIDENT_OF", "note": "Served as President of South Carolina College (1845–1851) — the state's flagship educational institution, training the antebellum leadership class that would guide South Carolina into secession"},
            {"entity": "Antebellum proslavery Senate tradition / South Carolina oratory", "relationship": "LEADING_VOICE_OF", "note": "One of the antebellum Senate's most accomplished orators and vocal proslavery voices — embodying South Carolina's tradition of cultivating eloquent planter-politician-scholars for the Senate"}
        ]
    }),

    # 3 — Denis-Benjamin Viger
    ("denis-benjamin-viger", {
        "summary": (
            "Denis-Benjamin Viger (1774–1861) was a Lower Canadian "
            "lawyer, journalist, politician, and French-Canadian "
            "nationalist who served as co-premier of the Province "
            "of Canada (1843–1844) and was a leading figure "
            "in the Patriote movement of the 1830s. Born into "
            "an established Montreal Patriote family — his "
            "cousin was Louis-Joseph Papineau — he built a "
            "legal practice, founded influential newspapers, "
            "and became one of Lower Canada's most effective "
            "political lobbyists in both Quebec City and London.\n\n"
            "His most dramatic political experience came during "
            "the Rebellion of Lower Canada (1837–1838): though "
            "he personally opposed armed rebellion and supported "
            "constitutional agitation, he was arrested by the "
            "British colonial authorities in 1838 and held "
            "without trial for twenty-nine months — a prolonged "
            "imprisonment without charge that he transformed "
            "into a cause célèbre for the constitutional rights "
            "of French Canadians.\n\n"
            "His appointment as co-premier (with William Henry "
            "Draper) in 1843 was politically controversial: "
            "most French-Canadian reformers backed the "
            "Baldwin-Lafontaine Reform coalition, and Viger's "
            "willingness to serve in the Conservative-allied "
            "government was seen as a betrayal by many former "
            "Patriote colleagues. The government quickly lost "
            "confidence and fell.\n\n"
            "Despite his conservatism on social questions — "
            "he defended the seigneurial system and the "
            "Catholic Church's role — his record of imprisonment "
            "and his decades of political activism made him "
            "a significant, if complex, figure in French "
            "Canada's constitutional history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lower Canadian Patriote leader; co-premier of the Province of Canada (1843–1844); imprisoned without trial for 29 months (1838–1840) after the Lower Canada Rebellion; cousin of Louis-Joseph Papineau; French-Canadian nationalist and constitutional agitator; newspaper founder; his contested co-premiership illustrates the fragmentation of French-Canadian reform politics after the Rebellion.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The political and constitutional conflict between Lower Canada's French-Canadian majority and the British colonial administration — over control of the assembly's budget, the Executive Council's accountability, and the broader question of French-Canadian political autonomy — created the Patriote movement that shaped Viger's career and led to the 1837–1838 rebellions",
            "The British colonial response to the Lower Canada Rebellion — which suspended the constitution, imprisoned political figures without trial, and eventually merged Upper and Lower Canada under the Act of Union (1840) — created both Viger's 29-month imprisonment and the new political landscape in which his controversial co-premiership became possible",
            "The fracturing of French-Canadian reform politics after the Rebellion — as the Baldwin-Lafontaine Reform coalition adopted 'Responsible Government' as the central demand, while conservative French Canadians like Viger remained willing to work within alternative political frameworks — created the conditions for his collaboration with the Conservative government in 1843"
        ],
        "effects": [
            "His 29-month imprisonment without trial contributed to the political debate about British colonial governance in Canada — making him a martyr figure for French-Canadian constitutional rights and generating political pressure that contributed to the Act of Union's eventual reform",
            "His co-premiership (1843–1844), though brief and controversial, contributed to the constitutional evolution of the Province of Canada — demonstrating the instability of governments that lacked French-Canadian reform support and accelerating the move toward genuine Responsible Government",
            "His newspaper founding and political journalism contributed to the development of French-Canadian political media as a vehicle for nationalist argument — building the press infrastructure that helped sustain French-Canadian political consciousness through the difficult post-Rebellion period",
            "His complex legacy — Patriote activist, political prisoner, social conservative, and controversial premier — contributed to the nuanced historiography of French-Canadian politics in the transition from colonial status to responsible government, illustrating the internal divisions within the francophone political community"
        ],
        "relationships": [
            {"entity": "Co-premier of the Province of Canada (with William Henry Draper, 1843–1844)", "relationship": "CO-PREMIER", "note": "Served as co-premier of the Province of Canada with William Henry Draper (1843–1844) — a controversial and short-lived government that most French-Canadian reformers opposed"},
            {"entity": "Lower Canada Rebellion (1837–1838) / imprisonment without trial (1838–1840, 29 months)", "relationship": "IMPRISONED_WITHOUT_TRIAL_FOLLOWING", "note": "Imprisoned without trial for 29 months (1838–1840) by British colonial authorities following the Lower Canada Rebellion — though he personally opposed armed rebellion, his Patriote connections made him a target"},
            {"entity": "Patriote movement / French-Canadian nationalism (Lower Canada, 1820s–1840s)", "relationship": "LEADING_FIGURE_OF", "note": "A leading figure of the Patriote movement — French-Canadian constitutional nationalism that demanded legislative control of the executive and French-Canadian political autonomy"},
            {"entity": "Louis-Joseph Papineau (cousin, Patriote leader and rebel)", "relationship": "COUSIN_OF", "note": "Cousin of Louis-Joseph Papineau — the leader of the Lower Canada Rebellion — though Viger himself opposed armed rebellion in favor of constitutional agitation"},
            {"entity": "Act of Union (1840) / Province of Canada (French-English merged parliament)", "relationship": "POLITICIAN_IN_THE_POLITICAL_LANDSCAPE_CREATED_BY", "note": "His co-premiership and post-Rebellion political career took place within the political landscape created by the Act of Union — the British-imposed merger of Upper and Lower Canada that the Patriote movement had resisted"}
        ]
    }),

    # 4 — David Emanuel
    ("david-emanuel", {
        "summary": (
            "David Emanuel (1744–1808) was a Georgia planter, "
            "militia officer, and politician who served as the "
            "24th Governor of Georgia in 1801 — briefly "
            "completing the remainder of James Jackson's "
            "gubernatorial term when Jackson resigned to accept "
            "a US Senate seat. Born in Pennsylvania, he moved "
            "to Georgia, served as a captain in the American "
            "Revolutionary War, and built a planting career "
            "in the Georgia backcountry that established "
            "his standing in the state's Democratic-Republican "
            "political establishment.\n\n"
            "He served as a member of the Georgia legislature "
            "and as President of the Georgia Senate — the "
            "position that, under the state's 1789 constitution, "
            "made him next in line for the governorship when "
            "Jackson vacated the office. His eight-month "
            "governorship (March–November 1801) was a "
            "caretaker administration during the transition "
            "to a new Georgia executive — he did not seek "
            "election to a full term.\n\n"
            "Emanuel County, Georgia — established in 1812 "
            "in the middle of the state — was named in his "
            "honor, providing a permanent geographic memorial "
            "to a figure who was briefly elevated to the "
            "governorship through constitutional succession "
            "rather than political ambition.\n\n"
            "His Revolutionary War service — which included "
            "combat in the difficult partisan warfare of the "
            "Georgia backcountry — was typical of the "
            "generation of Georgia militia officers who built "
            "the state's post-war planting economy and "
            "populated its political institutions."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "24th Governor of Georgia (1801, caretaker term); succeeded James Jackson who resigned to become US Senator; President of the Georgia Senate; Revolutionary War militia captain; Emanuel County Georgia named in his honor; his brief governorship illustrates the constitutional succession mechanisms of early Georgia state government.",
            "significanceCategory": "local"
        },
        "causes": [
            "James Jackson's decision to resign as Georgia's Governor in 1801 to accept a US Senate seat — creating the constitutional vacancy — triggered the succession mechanism that elevated Emanuel from Georgia Senate President to Governor under the state's 1789 constitution",
            "Georgia's post-Revolutionary War backcountry political culture — in which militia service, planting success, and Democratic-Republican affiliation were the standard credentials for political advancement — created the career path that brought Emanuel through the Georgia legislature to the Senate presidency",
            "Georgia's rapid institutional development in the early republic — with new counties, legislative positions, and constitutional offices being created to govern an expanding population — created the multiple institutional roles that figures like Emanuel filled in building the state's early governmental structure"
        ],
        "effects": [
            "His caretaker governorship contributed to the continuity of Georgia's executive administration during the transition from Jackson's elected term to a new governor — maintaining the state's institutional function during an eight-month period of constitutional succession",
            "Emanuel County's naming in his honor gave him a lasting geographic memorial — a county established in 1812 that bears his name in the middle of Georgia, extending his recognition to later generations who might otherwise have had no reason to remember his brief governorship",
            "His Revolutionary War service as a Georgia militia captain contributed to the partisan warfare that secured Georgia's independence from British occupation in the backcountry — the difficult and violent guerrilla conflict that was distinct from the regular Continental Army campaign",
            "His career as a Georgia Senate President who became governor through constitutional succession illustrated the functioning of Georgia's early constitutional succession mechanisms — one of the practical tests of the state constitution's provisions for filling executive vacancies"
        ],
        "relationships": [
            {"entity": "24th Governor of Georgia (1801, caretaker, March–November)", "relationship": "24TH_GOVERNOR_BRIEF_CARETAKER_TERM", "note": "Served as Georgia's 24th Governor (March–November 1801) — completing the remainder of James Jackson's term when Jackson resigned to become US Senator"},
            {"entity": "James Jackson (predecessor governor, resigned to US Senate)", "relationship": "SUCCEEDED_AS_GOVERNOR_WHEN_RESIGNED", "note": "Succeeded James Jackson as Georgia's governor when Jackson resigned to accept a US Senate seat — the constitutional succession mechanism elevating Emanuel from Georgia Senate President"},
            {"entity": "President of the Georgia Senate (constitutional successor position)", "relationship": "PRESIDENT_OF", "note": "Served as President of the Georgia Senate — the constitutional position that made him next in line for the governorship under Georgia's 1789 constitution"},
            {"entity": "American Revolutionary War / Georgia militia (captain, backcountry campaign)", "relationship": "MILITIA_CAPTAIN_DURING", "note": "Served as a captain in Georgia's Revolutionary War militia — participating in the difficult partisan warfare of the Georgia backcountry"},
            {"entity": "Emanuel County, Georgia (named in his honor, est. 1812)", "relationship": "NAMESAKE_OF", "note": "Emanuel County, Georgia — established in 1812 — was named in his honor, providing a lasting geographic memorial to his brief governorship and public service"}
        ]
    }),

    # 5 — Benjamin Taliaferro
    ("benjamin-taliaferro", {
        "summary": (
            "Benjamin Taliaferro (1750–1821) was a Virginia-born "
            "Revolutionary War veteran, lawyer, and Georgia "
            "politician who served as US Representative from "
            "Georgia (1799–1802), as a Georgia Superior Court "
            "judge, and as a delegate to Georgia's "
            "constitutional convention of 1798. Born in "
            "Virginia, he served as a captain during the "
            "American Revolutionary War and subsequently "
            "moved to Georgia, where he built a law practice "
            "and established himself in the state's "
            "Democratic-Republican political community.\n\n"
            "His congressional service (1799–1802) placed "
            "him in Washington during one of the most "
            "consequential transitions in American political "
            "history: the contested 1800 election that "
            "ended the Adams administration and brought "
            "Jefferson to power — the first peaceful transfer "
            "of power between opposing parties. As a "
            "Georgia Democratic-Republican, he was part "
            "of the Jeffersonian majority that swept into "
            "Congress with the 'Revolution of 1800.'\n\n"
            "His service as a delegate to Georgia's "
            "constitutional convention of 1798 contributed "
            "to the drafting of the state's second "
            "constitution — a document that reorganized "
            "Georgia's government and established the "
            "institutional framework for the state's "
            "19th-century governance. His Georgia Senate "
            "service further contributed to the legislative "
            "development of the early state.\n\n"
            "His career illustrated the pattern of Virginia-born "
            "Revolutionary veterans who migrated to Georgia "
            "after the war — bringing Virginia's legal "
            "and political traditions to a state that "
            "was still building its institutional infrastructure "
            "in the post-Revolutionary decades."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Revolutionary War captain; US Representative from Georgia (1799–1802) during the 'Revolution of 1800'; Georgia Superior Court judge; Georgia Senate; delegate to Georgia's 1798 constitutional convention; Virginia-born migrant who brought Virginia's legal traditions to Georgia's post-Revolutionary institutional development.",
            "significanceCategory": "local"
        },
        "causes": [
            "The post-Revolutionary migration of Virginia-born lawyers and veterans to Georgia — attracted by the availability of land and the need for legal professionals in a state whose institutional infrastructure was underdeveloped — created the demographic movement that brought Taliaferro from Virginia to Georgia",
            "Georgia's rapid post-Revolutionary political institutionalization — with new counties, courts, and legislative positions being created to govern an expanding population — created the demand for experienced lawyers and veterans who could fill the judicial and legislative roles that the state required",
            "The Jefferson electoral coalition's Georgia component — the Democratic-Republican dominance that swept the state's congressional delegation with the 'Revolution of 1800' — created the political context for Taliaferro's congressional election and his alignment with the Jeffersonian majority"
        ],
        "effects": [
            "His congressional service (1799–1802) contributed to Georgia's representation in the House during the most consequential transition in early American politics — the 1800 election and the Jeffersonian 'Revolution' that replaced Federalist dominance with Democratic-Republican control",
            "His delegate service at Georgia's 1798 constitutional convention contributed to the drafting of the state's second constitution — establishing the institutional framework for Georgia's 19th-century governance and the reorganization of its governmental structure",
            "His Georgia Superior Court service contributed to the development of Georgia's judicial system — applying the state's law in the judicial circuits that were building Georgia's common law tradition during the early republic period",
            "His career as part of the Virginia-origin migration to Georgia contributed to the transfer of Virginia's legal and political traditions to a state whose professional class was still being assembled — one of many Virginia-born lawyers who helped shape Georgia's institutional character in the post-Revolutionary decades"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Georgia (1799–1802)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from Georgia (1799–1802) — present during the 'Revolution of 1800' that brought Jefferson to power and ended the Federalist era"},
            {"entity": "Georgia constitutional convention of 1798 (delegate)", "relationship": "DELEGATE_TO", "note": "Served as a delegate to Georgia's constitutional convention of 1798 — contributing to the drafting of the state's second constitution that reorganized Georgia's governmental structure"},
            {"entity": "Georgia Superior Court (judge)", "relationship": "JUDGE", "note": "Served as a Georgia Superior Court judge — contributing to the development of Georgia's common law tradition in the early republic period"},
            {"entity": "American Revolutionary War (captain, Virginia forces)", "relationship": "CAPTAIN_DURING", "note": "Served as a captain during the Revolutionary War — part of the Virginia military tradition that he carried with him when he subsequently migrated to Georgia"},
            {"entity": "Virginia-Georgia migration / post-Revolutionary frontier migration", "relationship": "PARTICIPANT_IN", "note": "Part of the post-Revolutionary migration of Virginia-born lawyers and veterans to Georgia — contributing to the transfer of Virginia's legal and political traditions to the frontier state"}
        ]
    }),

    # 6 — José Damián Villacorta
    ("josé-damián-villacorta", {
        "summary": (
            "José Damián Villacorta Cañas (1798–1859) was a "
            "Salvadoran lawyer and politician who played a "
            "central role in El Salvador's early political "
            "history within the Federal Republic of Central "
            "America — serving as head of state of El Salvador "
            "in 1830, as vice head of state from 1829 to 1832, "
            "as president of the National Assembly in 1835, "
            "and as president of the Supreme Court of Justice "
            "from 1851 to 1857. His career spanned the "
            "turbulent first three decades of Central "
            "American independence.\n\n"
            "El Salvador's post-independence history was "
            "characterized by intense political conflict "
            "between liberals and conservatives, between "
            "the Central American federation and "
            "independence-minded states, and between "
            "competing elite factions. Villacorta's career "
            "— spanning executive, legislative, and judicial "
            "positions — placed him at the center of this "
            "turbulent institutional development, navigating "
            "the multiple constitutional crises that "
            "accompanied Central America's transition "
            "from Spanish colonial governance to "
            "independent statehood.\n\n"
            "The Federal Republic of Central America, "
            "which had declared independence from Spain "
            "and Mexico in 1823, was plagued by "
            "inter-state conflicts and the tension "
            "between federalists and centralists throughout "
            "the 1820s–1830s — eventually dissolving "
            "into five separate states by 1838–1841. "
            "Villacorta's 1830 head-of-state term and "
            "subsequent careers occurred within this "
            "dissolving federal framework.\n\n"
            "His Supreme Court presidency (1851–1857) "
            "contributed to the consolidation of El Salvador's "
            "independent judicial institutions — building "
            "the legal framework of a newly sovereign "
            "state that had only formally separated from "
            "the Central American federation in the 1840s."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Salvadoran head of state (1830); vice head of state (1829–1832); president of El Salvador's National Assembly (1835); president of Supreme Court of Justice (1851–1857); career spanning the Federal Republic of Central America's dissolution and El Salvador's emergence as an independent state; one of El Salvador's early institution-builders across executive, legislative, and judicial branches.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Central America's independence from Spain (1821) and from Mexico (1823) — and the subsequent formation of the Federal Republic of Central America — created the unstable new political framework within which Villacorta's career developed, requiring lawyers and politicians to build entirely new governmental institutions from scratch",
            "El Salvador's recurring political crises within the Federal Republic — conflicts with Guatemala over the federation's governance, liberal-conservative battles over constitutional structure, and the tensions of state sovereignty versus federal authority — created the political volatility that produced the multiple executive successions in which Villacorta served",
            "The dissolution of the Central American federation by 1838–1841 and El Salvador's emergence as a fully independent state created the new institutional context in which Villacorta's Supreme Court presidency contributed to building El Salvador's independent judicial system"
        ],
        "effects": [
            "His 1830 head-of-state term contributed to El Salvador's executive governance during one of the most turbulent periods of the Federal Republic's existence — managing the state's affairs as the federation was beginning to fracture under the contradictions of liberal-conservative and federal-state conflicts",
            "His National Assembly presidency (1835) contributed to El Salvador's legislative development within the still-operating federal framework — providing legislative leadership during the period just before the federation's final dissolution",
            "His Supreme Court presidency (1851–1857) contributed to the consolidation of El Salvador's independent judicial institutions in the years after the country's formal separation from the Central American federation — building the legal infrastructure of the newly sovereign state",
            "His career across executive, legislative, and judicial positions illustrated the characteristic pattern of early Central American politics — in which the same small elite of lawyers and politicians filled multiple institutional roles across decades of constitutional upheaval, building state institutions through personal continuity in the absence of established precedents"
        ],
        "relationships": [
            {"entity": "Head of state of El Salvador (1830, Federal Republic of Central America)", "relationship": "HEAD_OF_STATE", "note": "Served as head of state of El Salvador in 1830 — within the Federal Republic of Central America framework — during one of the most turbulent periods of the federation's existence"},
            {"entity": "Vice head of state of El Salvador (1829–1832)", "relationship": "VICE_HEAD_OF_STATE", "note": "Served as vice head of state of El Salvador (1829–1832) — the period surrounding his brief head-of-state term, contributing to executive continuity during constitutional crises"},
            {"entity": "El Salvador National Assembly (president, 1835)", "relationship": "PRESIDENT_OF", "note": "Served as president of El Salvador's National Assembly in 1835 — contributing to legislative leadership during the period just before the Central American federation's final dissolution"},
            {"entity": "Supreme Court of Justice of El Salvador (president, 1851–1857)", "relationship": "PRESIDENT_OF_SUPREME_COURT", "note": "Served as president of El Salvador's Supreme Court of Justice (1851–1857) — contributing to the consolidation of independent judicial institutions in the newly sovereign state"},
            {"entity": "Federal Republic of Central America (1823–1838/1841, dissolution)", "relationship": "POLITICIAN_DURING_DISSOLUTION_OF", "note": "His political career spanned the Federal Republic of Central America's formation and dissolution — his executive and legislative service occurring within its framework, his judicial service in the independent El Salvador that emerged after"}
        ]
    }),

    # 7 — Benjamin Chew Howard
    ("benjamin-chew-howard", {
        "summary": (
            "Benjamin Chew Howard (1791–1872) was a Maryland "
            "lawyer, politician, and legal reporter whose most "
            "enduring contribution to American legal history "
            "was his 17-year service as the 5th Reporter of "
            "Decisions of the United States Supreme Court "
            "(1843–1860) — producing 24 volumes of 'Howard's "
            "Reports' that documented the Court's decisions "
            "during one of the most consequential periods "
            "in American constitutional history, including "
            "the Dred Scott decision (1857).\n\n"
            "Before his Supreme Court reporter appointment, "
            "he had a substantial political career: he served "
            "on Baltimore's city council (1820), in both "
            "houses of the Maryland legislature, and as "
            "US Representative from Maryland across two "
            "separate terms (1829–1833 and 1835–1839). "
            "Born in Baltimore to a distinguished family — "
            "his father General John Eager Howard was a "
            "Revolutionary War hero — he studied law and "
            "became a respected Baltimore attorney.\n\n"
            "His 17 years as Supreme Court reporter coincided "
            "with the Court's most politically explosive "
            "era: the period of escalating sectional crisis "
            "over slavery that culminated in the Dred Scott "
            "decision (1857) — in which Chief Justice "
            "Taney declared that Congress had no authority "
            "to restrict slavery in the territories and "
            "that Black Americans had no constitutional "
            "citizenship rights. Howard's careful reporting "
            "of these decisions preserved the official "
            "record of the Court's most controversial "
            "rulings for posterity.\n\n"
            "The 'Howard Reports' (24 volumes, 1843–1860) "
            "remained the standard citation source for "
            "Supreme Court decisions of this period in "
            "American legal scholarship."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "5th Reporter of Decisions of the US Supreme Court (1843–1860, 24 volumes of 'Howard's Reports'); Maryland US Representative (1829–1833, 1835–1839); Baltimore city council; Maryland legislator; son of Revolutionary War hero General John Eager Howard; his 17-year Court reporter tenure documented the most constitutionally explosive period in American legal history including the Dred Scott decision (1857).",
            "significanceCategory": "regional"
        },
        "causes": [
            "The US Supreme Court's need for systematic, authoritative documentation of its decisions — in an era before official federal publication — created the position of Reporter of Decisions that Howard filled for 17 years, producing the standard citation source for the Court's antebellum jurisprudence",
            "His legal training, Baltimore family connections, and congressional experience — combined with his father General John Eager Howard's reputation as a Revolutionary War hero — gave him the professional standing and social capital that made him a credible candidate for the Supreme Court reporter appointment",
            "The antebellum sectional crisis's legal dimension — in which the Supreme Court was repeatedly asked to rule on the constitutional status of slavery, the rights of enslaved people, and the limits of congressional authority over the territories — created the high-stakes context in which Howard's reporting work took on historical significance"
        ],
        "effects": [
            "His 24 volumes of Howard's Reports provided the authoritative record of Supreme Court decisions from 1843 to 1860 — the standard citation source for this period's jurisprudence that has been used by lawyers and legal historians ever since",
            "His reporting of the Dred Scott decision (1857) preserved the official record of one of the most consequential and controversial Supreme Court rulings in American history — Chief Justice Taney's declaration that Congress had no authority to restrict slavery in the territories and that Black Americans had no constitutional citizenship rights",
            "His two-term congressional career contributed to Maryland's House representation during the Jacksonian and early Whig periods — serving during the Bank War, the Nullification Crisis, and the beginning of the antislavery agitation that would dominate subsequent decades",
            "His career connecting Maryland's Revolutionary-era military elite (through his father General Howard) to the legal and political institutions of the antebellum republic illustrated the generational transmission of social capital and institutional participation that characterized the American founding generation's descendants"
        ],
        "relationships": [
            {"entity": "5th Reporter of Decisions, US Supreme Court (1843–1860, 24 volumes)", "relationship": "REPORTER_OF_DECISIONS", "note": "Served as the 5th Reporter of Decisions of the US Supreme Court (1843–1860) — producing 24 volumes of 'Howard's Reports' that documented the Court's decisions during the most constitutionally explosive antebellum period"},
            {"entity": "Dred Scott decision (1857, Taney opinion, Howard's Reports citation)", "relationship": "DOCUMENTED_AND_PUBLISHED", "note": "Documented and published the Dred Scott decision (1857) — Chief Justice Taney's ruling that Congress had no authority to restrict slavery in the territories — preserving the official record of the most controversial Supreme Court decision of the antebellum era"},
            {"entity": "US House of Representatives from Maryland (1829–1833 and 1835–1839)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from Maryland in two separate terms (1829–1833, 1835–1839) — contributing to Maryland's congressional representation during the Jacksonian and early Whig periods"},
            {"entity": "General John Eager Howard (father, Revolutionary War hero)", "relationship": "SON_OF", "note": "Son of General John Eager Howard — one of Maryland's Revolutionary War heroes and namesake of Howard County — whose reputation gave Benjamin the social standing and family connections that supported his career"},
            {"entity": "Howard's Reports (24 volumes, 1843–1860, standard antebellum Supreme Court citation)", "relationship": "COMPILER_AND_PUBLISHER_OF", "note": "The compiler and publisher of Howard's Reports — the 24-volume standard citation source for US Supreme Court decisions from 1843 to 1860 — his most enduring contribution to American legal history"}
        ]
    }),

    # 8 — Jean-Baptiste Robert Lindet
    ("jean-baptiste-robert-lindet", {
        "summary": (
            "Jean-Baptiste Robert Lindet (1746–1825) was a "
            "French lawyer and politician of the Revolutionary "
            "period who served on the Committee of Public "
            "Safety (1793–1794) as the member responsible "
            "for provisioning — managing France's food "
            "supply, war production, and logistics during "
            "the most critical and violent phase of the "
            "Revolution. The brother of constitutional "
            "bishop Robert Thomas Lindet, he represented "
            "the rising middle class that dominated the "
            "Revolution's governing institutions.\n\n"
            "His role on the Committee of Public Safety "
            "was distinctive: unlike Robespierre, "
            "Saint-Just, and Billaud-Varenne — who drove "
            "the Terror's ideological purge — Lindet "
            "focused on the practical work of sustaining "
            "the Republic's material survival. His "
            "provisioning work was essential to maintaining "
            "the armies fighting on France's frontiers "
            "and feeding the population of Paris and "
            "other cities through the economic disruption "
            "of revolutionary war.\n\n"
            "He survived Thermidor — unlike Robespierre "
            "and many other Committee members — and was "
            "notably one of the few members who refused "
            "to vote for Robespierre's arrest, arguing "
            "that the Committee should not turn on itself. "
            "He was subsequently accused of Jacobin "
            "sympathies during the Thermidorian reaction "
            "and the White Terror but was acquitted.\n\n"
            "He later served under the Directory and "
            "became a minister of finances, before "
            "returning to private legal practice. "
            "His career represented the administrative "
            "dimension of the Revolution — the "
            "practical governance work that sustained "
            "the Republic while the ideologues "
            "struggled for dominance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Revolutionary politician; Committee of Public Safety member (1793–1794) responsible for provisioning — food supply, war production, logistics; refused to vote for Robespierre's arrest at Thermidor; survived the Terror and Thermidorian reaction; Directory minister of finances; his administrative role represented the practical governance dimension of the Revolution distinct from its ideological purge.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Republic's existential crisis in 1793 — facing simultaneous war with the First Coalition on multiple frontiers, the Vendée counter-revolution internally, and the federalist revolts in major cities — created the demand for a Committee of Public Safety member capable of managing France's provisioning and logistics under extreme wartime pressure",
            "The Committee of Public Safety's functional division of labor — in which different members took primary responsibility for different sectors of the Republic's governance — created the provisioning role that Lindet filled, allowing the Committee to simultaneously manage military strategy, political purges, and material supply",
            "Lindet's legal and administrative background — and his representation of the provincial bourgeoisie rather than the more radical Paris sans-culottes — shaped his Committee role as a practical administrator focused on keeping France fed and the armies equipped rather than driving the Terror's ideological escalation"
        ],
        "effects": [
            "His provisioning work on the Committee of Public Safety contributed to France's capacity to sustain the revolutionary armies fighting on multiple fronts in 1793–1794 — a logistical achievement without which the Republic's military survival would have been far more precarious",
            "His refusal to vote for Robespierre's arrest at Thermidor — while ultimately not preventing Robespierre's fall — contributed to the historical record of the Thermidorian coup as an event with internal dissent, and protected his own political survival by demonstrating consistency rather than opportunism",
            "His survival of both the Terror and the Thermidorian reaction — as one of the few Committee members to successfully navigate both phases — contributed to his subsequent Directory career as minister of finances, demonstrating the administrative continuity that the Revolution's practical governance required",
            "His career embodied the administrative dimension of the French Revolution — the provisioning, financing, and logistics work that sustained the Republic's survival — providing historians with evidence that the Revolution's governance included practical problem-solving alongside ideological purge, and that these two dimensions were managed by different personality types within the same institutions"
        ],
        "relationships": [
            {"entity": "Committee of Public Safety (1793–1794, provisioning and logistics role)", "relationship": "MEMBER_RESPONSIBLE_FOR_PROVISIONING", "note": "Served on the Committee of Public Safety (1793–1794) as the member responsible for provisioning — managing France's food supply, war production, and logistics during the Republic's most critical phase"},
            {"entity": "Thermidorian reaction (9 Thermidor Year II, refused to vote for Robespierre's arrest)", "relationship": "REFUSED_TO_VOTE_FOR_ROBESPIERRE_AT", "note": "Refused to vote for Robespierre's arrest during the Thermidorian coup — one of the few Committee members who maintained consistency rather than turning on a colleague — while nonetheless surviving the subsequent reaction"},
            {"entity": "French Directory (minister of finances, post-Thermidor)", "relationship": "MINISTER_OF_FINANCES_UNDER", "note": "Served as minister of finances under the Directory — continuing his administrative career after surviving the Terror and Thermidorian reaction, demonstrating the practical governance continuity the Revolution required"},
            {"entity": "Robert Thomas Lindet (brother, constitutional bishop and National Convention member)", "relationship": "BROTHER_OF", "note": "Brother of Robert Thomas Lindet — a constitutional bishop and member of the National Convention — the Lindet family's dual contribution to the Revolution's religious and political dimensions"},
            {"entity": "French bourgeoisie / middle class (Revolutionary governing class)", "relationship": "REPRESENTATIVE_FIGURE_OF", "note": "A representative figure of the French middle class that dominated the Revolution's governing institutions — his administrative focus on provisioning and practical governance embodying the bourgeoisie's contribution alongside the more ideological roles of other Committee members"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 45)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
