#!/usr/bin/env python3
"""
Batch 95 — 8 entities: Joseph Christopher Yates, William Lowndes,
Manuel Arredondo y Pelegrín, Dwight Foster, Erastus Root,
Gabriel Holmes, Miguel Núñez de Sanabria, William M. Meredith
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP: {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    dj = entity.get("detailsJson", "{}")
    det = json.loads(dj) if isinstance(dj, str) else dj
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} e={len(det.get('effects',[]))}")


ENTITIES = [

    ("joseph-christopher-yates", {
        "summary": (
            "Joseph Christopher Yates (1768–1837) was an American Democratic-Republican "
            "and Democratic politician from New York who served as a justice of the "
            "New York Supreme Court (1808–1822) and as Governor of New York (1823–1824). "
            "His single one-year governorship came at a moment of intense New York "
            "factional politics — the state's Democratic-Republican Party was "
            "fragmenting into the factions that would produce the 1824 presidential "
            "contest's multiple candidates. The Albany Regency — Martin Van Buren's "
            "political machine — was just consolidating its control of New York "
            "politics, and Yates's brief term reflected the transitional uncertainty "
            "before Van Buren's faction achieved dominance.\n\n"
            "His fourteen years on the New York Supreme Court was the most "
            "substantial part of his public career — a long judicial tenure "
            "that shaped New York's common law development.\n\n"
            "He was a Schenectady New York lawyer.\n\n"
            "He was a transitional figure in New York's early Jacksonian politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Supreme Court justice (1808–1822) and Governor (1823–1824); fourteen-year judicial career shaping New York common law; brief governorship during the fractured 1824 presidential contest; served as Albany Regency consolidated power; Schenectady New York lawyer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's factional Democratic-Republican politics — the state party's fragmentation into competing factions after the Federalist collapse — created the political environment for Yates's brief governorship",
            "The Albany Regency's emergence — Van Buren's political machine consolidating control of New York — created the factional pressure around Yates's one-year term",
            "New York's judicial development — the state's need for experienced common law jurists — created the institutional role for Yates's fourteen-year Supreme Court career"
        ],
        "effects": [
            "His fourteen-year judicial career contributed to New York's common law development — the foundational jurisprudence of the state's supreme court",
            "His brief governorship contributed to the documentation of New York's transitional politics before Jacksonian consolidation",
            "His career contributed to the historical record of New York's pre-Albany Regency political culture",
            "His Schenectady base contributed to the documentation of upstate New York's political representation"
        ],
        "relationships": [
            {"target": "new-york", "verb": "GOVERNS", "note": "Governor of New York 1823–1824"},
            {"target": "new-york-supreme-court", "verb": "SERVES_ON", "note": "Justice of New York Supreme Court 1808–1822"},
            {"target": "martin-van-buren", "verb": "CONTEMPORANEOUS_WITH", "note": "Governor during Van Buren's Albany Regency consolidation"},
            {"target": "election-of-1824", "verb": "GOVERNS_DURING", "note": "Governor during the fractured presidential contest"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New York Democratic-Republican"}
        ]
    }),

    ("william-lowndes", {
        "summary": (
            "William Lowndes (1782–1822) was an American Democratic-Republican "
            "politician from South Carolina who served in the U.S. House (1811–1822) "
            "and was one of the leading members of the War Hawks — the congressional "
            "faction that pushed for war with Britain in 1812. Along with Henry Clay "
            "and John C. Calhoun, Lowndes was among the most important voices for "
            "the War of 1812 in Congress. He later became a strong advocate for "
            "internal improvements and a moderate nationalist — positions that placed "
            "him at the center of the post-war debate over American economic development. "
            "He was seriously considered as a presidential candidate for the 1824 "
            "election — South Carolina nominated him — but he died at sea at forty.\n\n"
            "His death robbed American politics of one of its most promising figures. "
            "His contemporaries — including John Quincy Adams — ranked him among "
            "the ablest men in Congress.\n\n"
            "'He was the ablest man in Congress' — John Quincy Adams.\n\n"
            "He was one of the great unfulfilled political talents of the founding generation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "South Carolina War Hawk congressman (1811–1822) who pushed for the War of 1812 alongside Clay and Calhoun; moderate nationalist and internal improvements advocate; South Carolina's 1824 presidential candidate who died at sea at forty; rated by John Quincy Adams as 'the ablest man in Congress'; one of the great unfulfilled political talents of the era.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The War Hawks' western and southern nationalism — the congressional faction's belief that British trade interference and Indian alliances required military confrontation — created the political movement that Lowndes helped lead",
            "South Carolina's nationalist phase — the state's post-War of 1812 embrace of tariffs, internal improvements, and national economic development before its later states' rights turn — created the ideological context for Lowndes's moderate nationalism",
            "Lowndes's political talent — his recognized intelligence, eloquence, and legislative skill — created the personal reputation that made him a presidential possibility"
        ],
        "effects": [
            "His War Hawk advocacy contributed to the passage of the 1812 war declaration — the congressional push that overcame Madison's reluctance",
            "His internal improvements advocacy contributed to the post-war American System debate — the vision of federal investment in canals, roads, and industry",
            "His death contributed to the fragmented 1824 presidential contest — the loss of the Carolinian moderate nationalist whose nomination had suggested a different post-Monroe political path",
            "His reputation contributed to the historical record of congressional talent — the measure against which subsequent legislators have been compared"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "South Carolina Congressman 1811–1822"},
            {"target": "war-of-1812", "verb": "ADVOCATES_FOR", "note": "War Hawk who pushed for war with Britain"},
            {"target": "henry-clay", "verb": "ALLIES_WITH", "note": "Fellow War Hawk and internal improvements advocate"},
            {"target": "john-c-calhoun", "verb": "ALLIES_WITH", "note": "South Carolina colleague in War Hawk faction"},
            {"target": "election-of-1824", "verb": "NOMINATED_FOR", "note": "South Carolina's presidential candidate who died before the election"}
        ]
    }),

    ("manuel-arredondo-y-pelegrín", {
        "summary": (
            "Manuel de Arredondo y Pelegrín (1779–1832) was a Spanish military "
            "officer who served in the Americas during the independence era and "
            "was the Governor of Buenos Aires (1820). A royalist commander during "
            "the South American independence wars, Arredondo served in the Río "
            "de la Plata region during the final years of Spanish colonial "
            "authority in the region. Buenos Aires by 1810 was already effectively "
            "independent under the May Revolution, and Spanish royalist authority "
            "in the region was contested. His brief tenure as governor represents "
            "the last gasps of Spanish colonial administration in the southern "
            "cone of South America.\n\n"
            "He was a professional Spanish military officer whose career ended "
            "with the collapse of Spanish colonial authority in the Americas.\n\n"
            "He witnessed the final dissolution of Spanish power in the Río de "
            "la Plata region.\n\n"
            "He was a royalist officer in the era of South American independence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish royalist Governor of Buenos Aires (1820) and military officer during South American independence wars; represented last gasps of Spanish colonial administration in the Río de la Plata; witnessed collapse of Spanish authority in the southern cone; professional military officer whose career ended with Spanish colonial defeat.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Spanish colonial system in the Americas — the network of governors, military commanders, and administrators that Spain maintained across South America — created the institutional role that Arredondo filled",
            "South American independence movements — the patriot forces that were dismantling Spanish colonial authority across the continent — created the military and political context that ultimately ended Arredondo's role",
            "The Río de la Plata's May Revolution of 1810 — the Buenos Aires patriots' establishment of a governing junta — created the political reality that made Spanish royalist governance increasingly nominal"
        ],
        "effects": [
            "His Buenos Aires governorship contributed to the historical documentation of Spanish colonial administration's final years in the Río de la Plata",
            "His royalist military service contributed to the record of Spanish colonial resistance — the last defenders of an empire that was collapsing",
            "His career contributed to the historical record of the transition from Spanish colonial authority to Argentine independence",
            "His governorship contributed to Buenos Aires's political history — the documentation of its governance during the independence era"
        ],
        "relationships": [
            {"target": "buenos-aires", "verb": "GOVERNS", "note": "Governor of Buenos Aires 1820"},
            {"target": "spanish-empire", "verb": "SERVES_IN", "note": "Royalist military officer defending Spanish colonial authority"},
            {"target": "south-american-independence", "verb": "OPPOSES", "note": "Royalist commander during independence wars"},
            {"target": "río-de-la-plata", "verb": "COMMANDS_IN", "note": "Military officer in the Río de la Plata region"},
            {"target": "may-revolution", "verb": "SERVES_AFTER", "note": "Governor during post-1810 contested colonial authority"}
        ]
    }),

    ("dwight-foster", {
        "summary": (
            "Dwight Foster (1757–1823) was an American Federalist politician and "
            "jurist from Massachusetts who served in the U.S. House (1793–1800) "
            "and briefly in the U.S. Senate (1800–1803). His congressional career "
            "placed him in the heart of the Federalist era — the Adams "
            "administration's confrontations with France, the XYZ Affair, the "
            "Alien and Sedition Acts, and the political crisis of 1798–1800 that "
            "ended with Jefferson's victory. Massachusetts was the Federalist "
            "Party's strongest bastion, and Foster represented the state's "
            "commercial and legal elite that most consistently supported "
            "Hamilton's financial program and Adams's foreign policy.\n\n"
            "He later served as a justice of the Massachusetts Supreme Judicial Court.\n\n"
            "He was a Brookfield Massachusetts lawyer who served both branches "
            "of the federal legislature during the Federalist era.\n\n"
            "He was part of the Federalist generation that lost the Revolution of 1800."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts Federalist congressman and senator (1793–1803) during the Adams era; XYZ Affair and Alien and Sedition Acts era; Massachusetts Supreme Judicial Court justice; Brookfield Massachusetts lawyer representing the Federalist commercial elite; part of the Federalist generation that lost the 1800 Revolution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts Federalist political culture — the state's deep commercial and legal elite commitment to Federalist principles — created the political base for Foster's congressional career",
            "The Adams administration's political crises — the XYZ Affair, the quasi-war with France, and the Alien and Sedition Acts — created the defining issues of Foster's congressional years",
            "The Revolution of 1800 — Jefferson's election that ended Federalist national dominance — created the political transformation that ended Foster's congressional career"
        ],
        "effects": [
            "His congressional service contributed Massachusetts's Federalist perspective to the Adams administration's political battles",
            "His judicial career contributed to Massachusetts's legal development — the Supreme Judicial Court's jurisprudence from an experienced congressman",
            "His career contributed to the documentation of the Federalist generation — the politicians who built the first federal institutions and then lost to Jeffersonian Republicanism",
            "His Senate service contributed to Massachusetts's representation during the transitional period from Federalist dominance to Republican challenge"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Massachusetts Congressman 1793–1800"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Massachusetts Senator 1800–1803"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Massachusetts Federalist politician"},
            {"target": "massachusetts-supreme-judicial-court", "verb": "SERVES_ON", "note": "Massachusetts Supreme Judicial Court justice"},
            {"target": "john-adams", "verb": "SUPPORTS", "note": "Federalist supporter of the Adams administration"}
        ]
    }),

    ("erastus-root", {
        "summary": (
            "Erastus Root (1773–1846) was an American Democratic-Republican "
            "and Democratic politician from New York who served multiple terms "
            "in the U.S. House (1803–1805, 1809–1811, 1815–1817, 1831–1833) "
            "and in the New York state legislature, where he was an influential "
            "member. His most significant contribution was in the New York "
            "Constitutional Convention of 1821 — the landmark convention that "
            "dramatically expanded suffrage by removing property requirements "
            "for white male voters, transforming New York into a more democratic "
            "state and influencing democratic reform across the nation.\n\n"
            "Root was a leading advocate for democratic suffrage expansion at "
            "the convention — pushing for the broadest possible elimination of "
            "property qualifications. The 1821 convention was one of the most "
            "significant moments in early American democratic development.\n\n"
            "He was a Delhi New York lawyer who championed popular democracy.\n\n"
            "He was a founding figure of New York's democratic reform movement."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "New York Democratic-Republican congressman (multiple terms 1803–1833) and key delegate to the 1821 New York Constitutional Convention; leading advocate for universal white male suffrage at the 1821 convention — one of America's most significant democratic reforms; Delhi New York lawyer; founding figure of New York's democratic suffrage expansion movement.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New York's property qualification system — the land-ownership requirement that restricted voting to the propertied class — created the democratic reform target that Root and the 1821 convention addressed",
            "The Jeffersonian democratic tradition — the Republican ideology that championed popular self-governance and resisted aristocratic property qualifications — created the ideological framework for Root's suffrage advocacy",
            "New York's growing urban and rural working population — the farmers, laborers, and mechanics who could not meet property requirements — created the political constituency that Root represented"
        ],
        "effects": [
            "His 1821 convention advocacy contributed to New York's dramatic suffrage expansion — the elimination of property requirements that enfranchised working-class white men",
            "New York's 1821 democratization contributed to national democratic reform — the precedent that influenced other states to expand suffrage",
            "His congressional career contributed New York's democratic-Republican perspective to national legislation",
            "His suffrage expansion work contributed to the Jacksonian democratic movement — the popular democratic politics that the 1821 reforms helped create"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman multiple terms 1803–1833"},
            {"target": "new-york-constitutional-convention-1821", "verb": "DELEGATES_TO", "note": "Leading suffrage expansion advocate"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "Delhi New York lawyer-politician"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New York Jeffersonian Republican"},
            {"target": "universal-male-suffrage", "verb": "ADVOCATES_FOR", "note": "Champion of eliminating property qualifications for voting"}
        ]
    }),

    ("gabriel-holmes", {
        "summary": (
            "Gabriel Holmes (1769–1829) was an American Democratic-Republican "
            "politician from North Carolina who served as Governor of North Carolina "
            "(1821–1824) and as U.S. Representative (1825–1829). North Carolina "
            "in this era was a politically transitional state — the post-war "
            "expansion of cotton culture into the piedmont and western counties "
            "was reshaping the state's economy and politics. Holmes's governorship "
            "coincided with the Era of Good Feelings fusion politics and the "
            "beginning of the contested 1824 presidential election that fractured "
            "the Democratic-Republican Party.\n\n"
            "His move from the governorship to a House seat represented the "
            "common antebellum pattern of state-level politicians seeking "
            "federal representation after executive service.\n\n"
            "He was a Clinton North Carolina planter-lawyer.\n\n"
            "He represented North Carolina's transition from the early republic "
            "to Jacksonian Democratic politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "North Carolina Governor (1821–1824) and Congressman (1825–1829); Era of Good Feelings governorship and early Jacksonian-era congressional service; Clinton North Carolina planter-lawyer; represented North Carolina's transition from the early republic to Jacksonian Democratic politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's transitional political economy — the expansion of cotton culture and the state's transformation from tobacco-oriented to cotton piedmont — created the political environment of Holmes's career",
            "The Era of Good Feelings fusion politics — the one-party competition during Monroe's presidency — created the relatively uncontested gubernatorial environment of Holmes's term",
            "North Carolina's Democratic-Republican tradition — the state's alignment with Jeffersonian Republicanism — provided the political culture of Holmes's career"
        ],
        "effects": [
            "His governorship contributed to North Carolina's institutional governance during the Era of Good Feelings",
            "His congressional service contributed North Carolina's early Jacksonian perspective to the House",
            "His combined career contributed to the documentation of North Carolina's political transition from early republic to Jacksonian era",
            "His planter-lawyer background contributed to the historical record of North Carolina's antebellum political elite"
        ],
        "relationships": [
            {"target": "north-carolina", "verb": "GOVERNS", "note": "Governor of North Carolina 1821–1824"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "North Carolina Congressman 1825–1829"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democratic-Republican"},
            {"target": "election-of-1824", "verb": "GOVERNS_DURING", "note": "Governor during the fractured 1824 presidential contest"},
            {"target": "north-carolina-planter-class", "verb": "REPRESENTS", "note": "Clinton North Carolina planter-lawyer"}
        ]
    }),

    ("miguel-núñez-de-sanabria", {
        "summary": (
            "Miguel Núñez de Sanabria (fl. 17th century) was a Spanish colonial "
            "administrator and governor who served as Governor of Cumaná "
            "(Venezuela) in the mid-17th century. Venezuela in this period "
            "was one of Spain's lesser-populated American provinces — its "
            "pearl fisheries, cacao production, and cattle trade formed the "
            "economic base, while the ongoing conflict with Dutch traders, "
            "pirates, and indigenous resistance made governance challenging. "
            "The 17th century saw repeated Dutch and English incursions into "
            "the Caribbean, and governors like Núñez de Sanabria were "
            "responsible for both civil administration and coastal defense.\n\n"
            "Cumaná was one of the oldest continuously inhabited European "
            "settlements in South America — founded in 1521 — making its "
            "governance historically significant.\n\n"
            "He represented the Spanish colonial administrative system at its "
            "mid-17th century peak.\n\n"
            "He was part of the colonial administrative apparatus that governed Venezuela."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Spanish colonial Governor of Cumaná (Venezuela) in the 17th century; administered one of South America's oldest European settlements (founded 1521); governed during ongoing Dutch and English Caribbean incursions; part of the Spanish colonial administrative apparatus at its mid-17th century peak.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Spanish colonial administrative system — the network of governors, audiencias, and viceroys that Spain used to govern its American empire — created the institutional role that Núñez de Sanabria filled",
            "The 17th-century Caribbean conflict — the Dutch, English, and French challenges to Spanish Caribbean dominance through trade, piracy, and settlement — created the military context of his governance",
            "Cumaná's strategic position — Venezuela's oldest European settlement and its position on the Caribbean coast — created the administrative and defensive importance of the governorship"
        ],
        "effects": [
            "His governorship contributed to Cumaná's continuous colonial administration — the governance of one of South America's oldest European settlements",
            "His defensive role contributed to Spanish coastal security against Dutch and English incursions",
            "His career contributed to the historical record of Spanish colonial governance in Venezuela during the 17th century",
            "His administration contributed to the documentation of Venezuela's colonial history before the independence era"
        ],
        "relationships": [
            {"target": "cumaná", "verb": "GOVERNS", "note": "Governor of Cumaná, Venezuela"},
            {"target": "spanish-empire", "verb": "SERVES_IN", "note": "Spanish colonial administrator"},
            {"target": "venezuela", "verb": "ADMINISTERS", "note": "Colonial official in Venezuela"},
            {"target": "dutch-west-india-company", "verb": "DEFENDS_AGAINST", "note": "Governor during Dutch Caribbean incursions"},
            {"target": "spanish-colonial-system", "verb": "REPRESENTS", "note": "Part of the colonial administrative apparatus"}
        ]
    }),

    ("william-m-meredith", {
        "summary": (
            "William Morris Meredith (1799–1873) was an American Whig politician "
            "and lawyer from Pennsylvania who served as Secretary of the Treasury "
            "under President Zachary Taylor (1849–1850) and as a prominent "
            "Pennsylvania Whig leader. His Treasury tenure was brief — Taylor's "
            "sudden death in July 1850 ended the administration — but it coincided "
            "with the most intense debate over the Compromise of 1850 and the "
            "California statehood question. Meredith was a Philadelphia lawyer "
            "and one of the most distinguished members of the Pennsylvania bar.\n\n"
            "After his Treasury service he continued as a leading Pennsylvania "
            "lawyer and was state Attorney General (1861–1867) during the "
            "Civil War — managing Pennsylvania's legal affairs during the war.\n\n"
            "He was the founding president of the Union League of Philadelphia.\n\n"
            "He was one of Philadelphia's most eminent antebellum lawyers and civic leaders."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Secretary of the Treasury under Zachary Taylor (1849–1850); Pennsylvania state Attorney General during the Civil War (1861–1867); founding president of the Union League of Philadelphia; leading Pennsylvania Whig and Philadelphia lawyer; served during the Compromise of 1850 debates.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Pennsylvania's Whig political culture — the state's commercial and financial community's support for Whig economic nationalism — created the political base for Meredith's Treasury appointment",
            "The Taylor administration's brief presidency — Zachary Taylor's sixteen months in office before his sudden death — created the Treasury position that Meredith briefly occupied",
            "Philadelphia's legal and civic culture — the city's pre-eminent bar and its tradition of civic institution-building — created the professional and institutional base for Meredith's long post-Treasury career"
        ],
        "effects": [
            "His Treasury secretaryship contributed to the Taylor administration's fiscal management during the Compromise of 1850 debates",
            "His Civil War Attorney General service contributed to Pennsylvania's legal administration during the war — the largest state's legal apparatus supporting the Union cause",
            "His Union League founding contributed to Philadelphia's Civil War civic mobilization — the institution that supported the war effort and Union Republican politics",
            "His Philadelphia legal career contributed to the development of Pennsylvania's legal institutions — decades of distinguished bar service"
        ],
        "relationships": [
            {"target": "zachary-taylor", "verb": "SERVES_UNDER", "note": "Secretary of the Treasury under Taylor 1849–1850"},
            {"target": "us-department-of-treasury", "verb": "LEADS", "note": "Secretary of the Treasury"},
            {"target": "pennsylvania", "verb": "SERVES_AS_ATTORNEY_GENERAL_OF", "note": "Pennsylvania Attorney General 1861–1867"},
            {"target": "union-league-of-philadelphia", "verb": "FOUNDS", "note": "Founding president of the Union League"},
            {"target": "compromise-of-1850", "verb": "SERVES_DURING", "note": "Treasury Secretary during the sectional compromise debates"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 95 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
