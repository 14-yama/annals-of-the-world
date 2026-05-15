#!/usr/bin/env python3
"""
Batch 88 — 8 entities: Jean de Lauson, John Williams Walker,
William A. Whittlesey, Philemon Dickerson, William W. Ellsworth,
Silas Hemenway Jennison, Alexandre-François Vivien, John Motley Morehead
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

    ("jean-de-lauson", {
        "summary": (
            "Jean de Lauson (c.1584–1666) "
            "was a French colonial "
            "administrator who "
            "served as Governor-General "
            "of New France (1651–1657) "
            "at the most dangerous "
            "moment in the colony's "
            "history — the height "
            "of the Iroquois "
            "wars that nearly "
            "destroyed the "
            "French colonial "
            "enterprise in "
            "North America. "
            "Lauson had been "
            "involved in "
            "New France for "
            "decades before "
            "his governorship "
            "— as a member "
            "of the Company "
            "of New France "
            "(the Hundred Associates) "
            "and as a landowner "
            "in the colony. "
            "His governorship "
            "was marked by "
            "the Iroquois Confederacy's "
            "devastating raids "
            "that killed or "
            "captured missionaries, "
            "destroyed Huron "
            "villages, and "
            "threatened Quebec "
            "and Montreal "
            "themselves.\n\n"
            "The Lauson era "
            "was the nadir "
            "of French colonial "
            "power — the period "
            "when New France's "
            "survival was "
            "genuinely in doubt.\n\n"
            "He was widely "
            "criticized for "
            "his ineffective "
            "defense of the colony.\n\n"
            "He is remembered "
            "in the place name "
            "Lauzon, Quebec."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Governor-General of New France (1651–1657) during the height of the Iroquois wars that nearly destroyed the colony; Company of New France (Hundred Associates) member for decades; his ineffective defense left New France at its most vulnerable; the Lauson era was the nadir of French North American colonization.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Iroquois Confederacy's military power — the Five Nations' determination to control the fur trade and eliminate competing tribes allied with the French — created the existential military threat that defined Lauson's governorship",
            "The Company of New France's failure to adequately support the colony — the Hundred Associates' inability to provide sufficient settlers, soldiers, and resources to enable effective defense — created the structural weakness that Lauson's governorship could not overcome",
            "The collapse of the Huron nation — the Iroquois destruction of the Huron Confederacy in 1649–1650 that eliminated France's most important ally — created the strategic crisis that immediately preceded Lauson's governorship"
        ],
        "effects": [
            "His governorship's failures contributed to the eventual decision to establish the Carignan-Salières Regiment's deployment — the military solution that the French crown ultimately adopted to save the colony after Lauson's term",
            "The near-collapse of New France during his tenure contributed to the French crown's decision to take the colony directly under royal administration in 1663 — replacing the Company of New France with direct royal governance",
            "His era's devastation contributed to the permanent reshaping of New France's indigenous alliances — the post-Huron strategic landscape in which the French sought new indigenous partners",
            "His criticism and recall contributed to the historical pattern of inadequate colonial governors whose failures prompted metropolitan intervention — the cycle that shaped New France's governance"
        ],
        "relationships": [
            {"target": "new-france", "verb": "GOVERNS", "note": "Governor-General 1651–1657"},
            {"target": "iroquois-confederacy", "verb": "FAILS_TO_DEFEND_AGAINST", "note": "Governor during devastating Iroquois attacks"},
            {"target": "company-of-new-france", "verb": "MEMBER_OF", "note": "Hundred Associates member for decades"},
            {"target": "huron-nation", "verb": "GOVERNS_AFTER_DESTRUCTION_OF", "note": "Governor after Huron Confederacy's elimination"},
            {"target": "french-colonialism-north-america", "verb": "ADMINISTERS", "note": "Colonial governor at the nadir of French power"}
        ]
    }),

    ("john-williams-walker", {
        "summary": (
            "John Williams Walker (1783–1823) "
            "was an American "
            "Democratic-Republican "
            "politician from Alabama "
            "who served as "
            "one of Alabama's "
            "first U.S. Senators "
            "(1819–1822) after "
            "statehood. Alabama's "
            "admission as the "
            "22nd state in "
            "December 1819 — "
            "part of the "
            "same sectional "
            "crisis that produced "
            "the Missouri Compromise — "
            "made Walker and "
            "his Senate colleague "
            "among the first "
            "voices of the "
            "new Deep South "
            "cotton state. "
            "Alabama in this "
            "era was one of "
            "the fastest-growing "
            "states in the "
            "Union — the "
            "cotton boom "
            "transforming it "
            "from frontier "
            "territory to "
            "major slave state "
            "within a decade. "
            "Walker died young "
            "at forty — "
            "his brief Senate "
            "career cutting "
            "short what might "
            "have been a "
            "significant political career.\n\n"
            "Alabama's rapid "
            "cotton economy "
            "growth made it "
            "a bellwether "
            "of the antebellum "
            "Deep South.\n\n"
            "He died in office "
            "from tuberculosis.\n\n"
            "He was a Huntsville "
            "Alabama planter-lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "One of Alabama's first U.S. Senators (1819–1822); served during Alabama's early statehood — one of the fastest-growing cotton states; period of the Missouri Compromise sectional crisis; died at forty from tuberculosis cutting short a promising career; Huntsville planter-lawyer representing the Deep South cotton boom.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Alabama's statehood — the 1819 admission of Alabama as the 22nd state in the same congressional session as the Missouri Compromise sectional crisis — created Walker's opportunity to be one of the new state's founding senators",
            "The cotton boom — Alabama's explosive agricultural development driven by cotton's profitability and the forced labor of enslaved people — created the economic foundation of Walker's planter class and the political interests he represented",
            "The Missouri Compromise crisis — the national sectional debate over slavery's expansion that Alabama's statehood was embedded in — created the political context of Walker's brief Senate service"
        ],
        "effects": [
            "His early Senate service established Alabama's initial congressional presence — the first representation of the new cotton state in the federal Senate",
            "His brief career contributed to Alabama's early political culture — the planters and lawyers who dominated the new state's politics from its founding",
            "His death at forty contributed to the pattern of political succession in Alabama's early years — the rapid turnover that characterized a new state building its political institutions",
            "His career illustrated the antebellum Deep South pattern — the rapid transformation of frontier territory into slave-economy cotton states within a single generation"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "One of Alabama's first Senators 1819–1822"},
            {"target": "alabama", "verb": "REPRESENTS", "note": "Founding senator of the new cotton state"},
            {"target": "missouri-compromise", "verb": "SERVES_DURING", "note": "Senator during the sectional crisis of 1820"},
            {"target": "cotton-economy", "verb": "REPRESENTS", "note": "Planter-senator of the Deep South cotton boom"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democratic-Republican"}
        ]
    }),

    ("william-a-whittlesey", {
        "summary": (
            "William Augustus Whittlesey "
            "(1796–1866) was an "
            "American Democratic "
            "politician from Ohio "
            "who served in the "
            "U.S. House (1843–1845) "
            "during the Tyler "
            "administration's "
            "final years and "
            "the beginning of "
            "the Polk era. "
            "Ohio was among "
            "the most politically "
            "competitive states "
            "in antebellum America "
            "— the large northwestern "
            "state where "
            "Democrats and Whigs "
            "contested vigorously "
            "and where the "
            "Liberty Party's "
            "antislavery challenge "
            "was beginning "
            "to complicate the "
            "two-party system. "
            "His House term "
            "coincided with "
            "the Texas annexation "
            "controversy and "
            "the Oregon question "
            "— the territorial "
            "expansion debates "
            "that drove "
            "American foreign "
            "policy in "
            "the mid-1840s.\n\n"
            "Ohio's Democratic "
            "congressional delegation "
            "in this era "
            "was part of "
            "the western Democratic "
            "coalition that "
            "supported Manifest Destiny.\n\n"
            "He was a Canfield "
            "Ohio lawyer.\n\n"
            "He served during "
            "the territorial "
            "expansion decade."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Ohio Democratic Congressman (1843–1845); served during the Texas annexation and Oregon debates; Ohio's competitive antebellum politics; Manifest Destiny-era congressman; Canfield Ohio lawyer representing the northwestern Democratic coalition.",
            "significanceCategory": "local"
        },
        "causes": [
            "Ohio's competitive Democratic-Whig politics — the large northwestern state's contested political environment where both parties had genuine strength and margins were narrow — created the opportunity for Whittlesey's House election",
            "The Manifest Destiny momentum of the early 1840s — the expansionist enthusiasm that drove Texas annexation and Oregon boundary disputes — created the territorial controversies that dominated Whittlesey's congressional term",
            "Ohio's western Democratic culture — the frontier-descended agricultural communities that aligned with Democratic Manifest Destiny expansionism over Whig cautious development — provided Whittlesey's political base"
        ],
        "effects": [
            "His House service contributed Ohio's Democratic vote to the Texas annexation and Oregon debates — the Manifest Destiny-era territorial expansion decisions",
            "His career contributed to the Democratic coalition in the key northwestern swing state of Ohio",
            "His brief term illustrated the competitive nature of Ohio politics — the narrow margins that made Ohio a battleground state in every antebellum election",
            "His service contributed to the western Democratic coalition that supported Polk's expansionist agenda"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Ohio Congressman 1843–1845"},
            {"target": "james-k-polk", "verb": "SERVES_DURING", "note": "Congressman in the Manifest Destiny era"},
            {"target": "texas-annexation", "verb": "VOTES_ON", "note": "Congressman during the Texas annexation debate"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio Democratic congressman"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Western Democratic Manifest Destiny supporter"}
        ]
    }),

    ("philemon-dickerson", {
        "summary": (
            "Philemon Dickerson "
            "(1788–1862) was "
            "an American Democratic "
            "politician from "
            "New Jersey who "
            "served as Governor "
            "of New Jersey "
            "(1836–1837), U.S. "
            "Senator (1836), "
            "and U.S. Representative "
            "(1833–1836 and "
            "1839–1841). "
            "His overlapping "
            "offices — the "
            "brief Senate appointment "
            "and the governorship "
            "that followed — "
            "illustrated the "
            "complex patronage "
            "rotation of "
            "Jacksonian-era "
            "New Jersey politics. "
            "New Jersey in "
            "this era was "
            "a closely contested "
            "state — its "
            "mixed commercial "
            "and agricultural "
            "economy, its "
            "Quaker and Protestant "
            "communities, "
            "and its proximity "
            "to both New York "
            "and Philadelphia "
            "creating a "
            "genuinely competitive "
            "political arena. "
            "His brother Daniel "
            "Dickerson also "
            "served in Congress "
            "— the family "
            "representing "
            "New Jersey's "
            "Democratic tradition.\n\n"
            "He later served "
            "as a federal "
            "district judge "
            "in New Jersey.\n\n"
            "He was a Paterson "
            "New Jersey lawyer.\n\n"
            "He was a figure "
            "of Jacksonian "
            "New Jersey Democracy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Jersey Democratic Governor (1836–1837), Senator (1836), and Congressman (1833–1836 and 1839–1841); multiple overlapping Jacksonian-era offices; New Jersey's competitive antebellum politics; later federal judge; Paterson lawyer representing New Jersey's Democratic tradition; brother of Congressman Daniel Dickerson.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's competitive Jacksonian politics — the state's balanced Democratic-Whig competition that made it a genuine swing state — created the contested elections that Dickerson won for multiple offices",
            "The Jacksonian Democratic machine's patronage system — the rotation of offices and the use of political loyalty to distribute gubernatorial and senatorial appointments — created the overlapping career pattern of Dickerson's multiple offices",
            "Dickerson's legal reputation and Paterson community standing — his professional prominence in one of New Jersey's major industrial cities — provided the personal basis for his political career"
        ],
        "effects": [
            "His governorship contributed to New Jersey's Democratic governance during the height of the Jacksonian era — the state executive experience that complemented his legislative career",
            "His multiple offices contributed to the Democratic organizational strength in New Jersey — the machine-building that kept the state competitive against Whig challenges",
            "His federal judgeship contributed to the development of New Jersey's federal judiciary — the judicial appointments that shaped federal court practice in the state",
            "His career contributed to the political documentation of New Jersey's antebellum Democracy — the Jacksonian tradition in a state that remained genuinely competitive"
        ],
        "relationships": [
            {"target": "new-jersey", "verb": "GOVERNS", "note": "Governor of New Jersey 1836–1837"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1836"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Congressman 1833–1836 and 1839–1841"},
            {"target": "andrew-jackson", "verb": "SERVES_UNDER", "note": "Jacksonian-era New Jersey Democrat"},
            {"target": "federal-judiciary", "verb": "SERVES_IN", "note": "Later federal district judge in New Jersey"}
        ]
    }),

    ("william-w-ellsworth", {
        "summary": (
            "William Wolcott Ellsworth "
            "(1791–1868) was an "
            "American Whig "
            "politician and jurist "
            "from Connecticut "
            "who served in "
            "the U.S. House "
            "(1829–1834) and "
            "as Governor of "
            "Connecticut (1838–1842). "
            "He was the son-in-law "
            "of Noah Webster — "
            "America's great "
            "lexicographer — "
            "which placed him "
            "in Connecticut's "
            "elite Federalist "
            "and later Whig "
            "intellectual and "
            "political establishment. "
            "His House years "
            "spanned the Adams-Jackson "
            "transition — "
            "serving during "
            "the Bank War's "
            "beginnings and "
            "the nullification "
            "crisis. His "
            "four-year governorship "
            "covered the "
            "crucial period "
            "of Connecticut's "
            "constitutional "
            "reform — the "
            "state's transition "
            "from its original "
            "colonial charter "
            "to a modern constitution "
            "adopted in 1818.\n\n"
            "He later served "
            "as a Connecticut "
            "Supreme Court judge "
            "— combining the "
            "judicial and "
            "executive roles "
            "typical of "
            "antebellum New "
            "England lawyers.\n\n"
            "His connection "
            "to Noah Webster "
            "linked him to "
            "Connecticut's "
            "most celebrated intellectual.\n\n"
            "He was a Hartford "
            "Connecticut lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Whig Congressman (1829–1834) and Governor (1838–1842); son-in-law of Noah Webster; governorship during Connecticut's 1818 constitutional transition; Bank War-era congressman; later Connecticut Supreme Court judge; Hartford lawyer representing Connecticut's Whig intellectual establishment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Whig intellectual establishment — the Yale-educated lawyers, clergy, and professionals who formed New England's most cohesive elite — created the political and social environment of Ellsworth's career",
            "His Noah Webster family connection — his marriage into the family of America's greatest lexicographer — gave him access to Connecticut's Federalist-Whig intellectual network and added prestige to his political profile",
            "Connecticut's constitutional transition — the state's adoption of its first modern constitution in 1818, replacing the colonial charter — created the institutional context that shaped Connecticut's governance during Ellsworth's political career"
        ],
        "effects": [
            "His governorship contributed to Connecticut's governance during and after the 1818 constitutional transition — the executive management of the new constitutional order",
            "His House service contributed Connecticut's Whig perspective to the Adams-Jackson era debates — the Bank War, nullification, and internal improvements",
            "His Connecticut Supreme Court service contributed to the development of Connecticut's legal traditions — the judicial interpretation of the new state constitution",
            "His Webster family connection contributed to the documentation of Connecticut's interconnected political and intellectual elite — the network that shaped New England's cultural and political life"
        ],
        "relationships": [
            {"target": "connecticut", "verb": "GOVERNS", "note": "Governor of Connecticut 1838–1842"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1829–1834"},
            {"target": "noah-webster", "verb": "SON_IN_LAW_OF", "note": "Son-in-law of the American lexicographer"},
            {"target": "connecticut-supreme-court", "verb": "SERVES_ON", "note": "Connecticut Supreme Court judge"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Connecticut Whig politician"}
        ]
    }),

    ("silas-hemenway-jennison", {
        "summary": (
            "Silas Hemenway Jennison "
            "(1791–1849) was an "
            "American Whig "
            "politician from Vermont "
            "who served as "
            "Governor of Vermont "
            "(1835–1841) — a "
            "six-year governorship "
            "making him one "
            "of Vermont's "
            "longest-serving "
            "antebellum governors. "
            "Vermont in the "
            "1830s was transforming "
            "from a Federalist "
            "holdout into one "
            "of the nation's "
            "most reliably Whig "
            "and later Republican "
            "states — the Green "
            "Mountain State "
            "whose antislavery "
            "tradition and "
            "Congregationalist "
            "moral culture "
            "aligned naturally "
            "with Whig economic "
            "and reform principles. "
            "His governorship "
            "spanned the "
            "Bank War's peak, "
            "the Panic of 1837's "
            "economic depression, "
            "and Vermont's "
            "mounting antislavery "
            "sentiment — the "
            "state that had "
            "abolished slavery "
            "constitutionally "
            "in 1777.\n\n"
            "Vermont's economic "
            "depression during "
            "the Panic of 1837 "
            "was severe — "
            "the state's farmers "
            "and woolen manufacturers "
            "hit hard.\n\n"
            "He was a Windsor "
            "County Vermont "
            "businessman and politician.\n\n"
            "He was Vermont's "
            "longest-serving "
            "Whig governor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont Whig Governor (1835–1841); one of Vermont's longest-serving antebellum governors at six years; governorship during the Bank War, Panic of 1837, and growing Vermont antislavery movement; Vermont's transformation from Federalist to Whig dominance; Windsor County businessman representing Vermont's Whig values.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Whig political dominance — the state's Protestant agricultural communities and antislavery commitments that made it one of the most reliably Whig states from the 1830s onward — created the environment for Jennison's long governorship",
            "The Panic of 1837 — the economic depression that struck Vermont's farming and manufacturing communities and that created both the policy challenges and political opportunities of Jennison's extended tenure — created the governing crisis he managed",
            "Vermont's antislavery tradition — the state's constitutional abolition of slavery in 1777 and its growing moral reform culture — created the political climate that aligned Vermont with the most progressive Whig positions on slavery and reform"
        ],
        "effects": [
            "His six-year governorship contributed to Vermont's stable Whig governance through the Bank War and Panic of 1837 — managing the economic crisis from the governor's office",
            "His long tenure contributed to Vermont's Whig institutional development — the executive traditions that made Vermont a model of antislavery Whig governance",
            "His administration contributed to Vermont's growing antislavery political culture — the state executive who served during the decade when Vermont's abolitionist movement was strengthening",
            "His career contributed to Vermont's tradition of consecutive Whig and Republican governors that made the state one of the most consistently non-Democratic states in American history"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1835–1841"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig governor"},
            {"target": "panic-of-1837", "verb": "GOVERNS_DURING", "note": "Governor during economic depression"},
            {"target": "bank-war", "verb": "GOVERNS_DURING", "note": "Governor during Bank War's peak"},
            {"target": "vermont-antislavery-movement", "verb": "SERVES_DURING", "note": "Governor during Vermont's growing abolitionism"}
        ]
    }),

    ("alexandre-français-vivien", {
        "summary": (
            "Alexandre-François Vivien "
            "(1799–1854) was a "
            "French lawyer, "
            "legal scholar, "
            "and politician who "
            "served as Minister "
            "of the Interior "
            "(1848) and made "
            "important contributions "
            "to the development "
            "of French administrative law. "
            "His 'Études administratives' "
            "(1845) was one "
            "of the founding "
            "texts of modern "
            "French administrative "
            "law — the field "
            "that governs "
            "relations between "
            "the state and citizens. "
            "Vivien served "
            "during the turbulent "
            "year of 1848 — "
            "the February Revolution "
            "that overthrew "
            "Louis-Philippe, "
            "the proclamation "
            "of the Second Republic, "
            "and the June Days "
            "uprising that "
            "ended the democratic "
            "experiment. His "
            "Interior Ministry "
            "service placed "
            "him at the center "
            "of the Second "
            "Republic's early "
            "governance.\n\n"
            "Administrative law "
            "— the French system "
            "of separate courts "
            "to adjudicate "
            "state-citizen disputes "
            "— is one of France's "
            "most distinctive "
            "legal contributions "
            "to global governance.\n\n"
            "He was also "
            "a Councillor "
            "of State.\n\n"
            "He was a founding "
            "figure of "
            "French administrative "
            "law scholarship."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Minister of the Interior (1848) and founding administrative law scholar; his 'Études administratives' (1845) was a founding text of French administrative law; served during the 1848 Revolution and early Second Republic; Councillor of State; France's administrative law tradition is one of its most distinctive global contributions.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The development of French administrative law — the legal tradition separating judicial review of state action from ordinary civil courts that France pioneered — created the scholarly field to which Vivien contributed foundational texts",
            "The 1848 Revolution's political upheaval — the February Revolution, Second Republic, and June Days that created the political context for Vivien's Interior Ministry appointment — placed the administrative law scholar at the center of executive governance",
            "Vivien's Conseil d'État expertise — his deep knowledge of the administrative court system that adjudicated state-citizen disputes — gave him both the scholarly tools for his treatise and the practical experience for ministerial service"
        ],
        "effects": [
            "His 'Études administratives' contributed to the intellectual foundations of French administrative law — providing the systematic theoretical framework for a distinctive French legal tradition",
            "His Interior Ministry service contributed to the governance of the Second Republic's critical early months — managing the state apparatus during the revolutionary transition",
            "His administrative law scholarship influenced subsequent generations of French legal scholars — the tradition of systematic analysis of the administrative state that shaped comparative administrative law globally",
            "France's administrative law tradition that Vivien helped establish contributed to the global model — the system adopted or adapted by many countries as an alternative to common-law judicial review"
        ],
        "relationships": [
            {"target": "french-ministry-of-interior", "verb": "LEADS", "note": "Minister of the Interior 1848"},
            {"target": "french-second-republic", "verb": "SERVES_IN", "note": "Minister during the 1848 revolutionary republic"},
            {"target": "french-administrative-law", "verb": "FOUNDS", "note": "Author of 'Études administratives' — founding administrative law text"},
            {"target": "conseil-detat-france", "verb": "SERVES_IN", "note": "Councillor of State with administrative court expertise"},
            {"target": "revolution-of-1848-france", "verb": "SERVES_DURING", "note": "Interior Minister during the February Revolution"}
        ]
    }),

    ("john-motley-morehead", {
        "summary": (
            "John Motley Morehead "
            "(1796–1866) was an "
            "American Whig "
            "politician and businessman "
            "from North Carolina "
            "who served as "
            "Governor of North "
            "Carolina (1841–1845) "
            "and in the U.S. "
            "House (1847–1851). "
            "One of North Carolina's "
            "most important "
            "antebellum governors, "
            "Morehead was a "
            "champion of "
            "internal improvements "
            "— advocating railroad "
            "construction, public "
            "education expansion, "
            "and industrial "
            "development in "
            "a state that "
            "lagged behind "
            "Virginia and "
            "South Carolina "
            "in economic development. "
            "He helped build "
            "the North Carolina "
            "Railroad — the "
            "crucial infrastructure "
            "connecting the "
            "state's interior "
            "to the coast. "
            "His commitment "
            "to public education "
            "included supporting "
            "common schools "
            "and the "
            "North Carolina Institution "
            "for the Deaf and Dumb.\n\n"
            "Morehead City, North "
            "Carolina is named "
            "for him — "
            "the port city "
            "that his railroad "
            "initiatives helped "
            "develop.\n\n"
            "His industrial "
            "vision made him "
            "among North Carolina's "
            "most progressive "
            "antebellum governors.\n\n"
            "'A state that "
            "invests in its "
            "roads and schools "
            "invests in its future.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "North Carolina Whig Governor (1841–1845) and Congressman (1847–1851); champion of internal improvements, railroad construction, and public education in antebellum North Carolina; helped build the North Carolina Railroad; supporter of schools for the deaf; Morehead City named in his honor; one of the most development-oriented governors of the antebellum South.",
            "significanceCategory": "continental"
        },
        "causes": [
            "North Carolina's economic underdevelopment — the state's lagging infrastructure and public services compared to Virginia and South Carolina — created the urgent need for the internal improvement advocacy that defined Morehead's governorship",
            "The Whig Party's internal improvement ideology — the Whig conviction that government investment in transportation, education, and infrastructure created economic prosperity — aligned with Morehead's developmental vision for North Carolina",
            "The railroad revolution — the transformation of American internal transportation by steam railroads in the 1830s and 1840s — created the technological opportunity that Morehead recognized as essential for connecting North Carolina's interior to markets"
        ],
        "effects": [
            "His gubernatorial advocacy contributed to North Carolina's railroad development — the construction of the North Carolina Railroad that transformed the state's internal transportation and economic integration",
            "His public education support contributed to North Carolina's school system — the common schools and specialized institutions that his administration backed",
            "His industrial development vision contributed to North Carolina's economic modernization — pushing the state toward the infrastructure investment that economic development required",
            "Morehead City — the port city named for him — became a lasting monument to his developmental legacy, the transportation infrastructure that his railroad vision created"
        ],
        "relationships": [
            {"target": "north-carolina", "verb": "GOVERNS", "note": "Governor of North Carolina 1841–1845"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "North Carolina Congressman 1847–1851"},
            {"target": "north-carolina-railroad", "verb": "BUILDS", "note": "Champion of North Carolina railroad construction"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "North Carolina Whig internal improvements advocate"},
            {"target": "morehead-city-nc", "verb": "NAMESAKE_OF", "note": "Port city named in his honor for railroad development"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 88 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
