#!/usr/bin/env python3
"""
Batch 43 — 8 entities: Alfred Moore, Moses Robinson, Muhammad al-Abdari al-Hihi,
John Gayle, Feargus O'Connor, William Grayson,
Jacques-Nicolas Billaud-Varenne, Dominique Bouligny
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

    # 1 — Alfred Moore
    ("alfred-moore", {
        "summary": (
            "Alfred Moore (1755–1810) was a North Carolina lawyer, "
            "planter, and Revolutionary War officer who served as "
            "an Associate Justice of the United States Supreme Court "
            "from 1799 to 1804 — appointed by President John Adams "
            "following a career as North Carolina's attorney general "
            "and a state superior court judge. Born in Brunswick "
            "County, North Carolina, he served as a militia captain "
            "during the Revolution and saw combat in the southern "
            "campaign.\n\n"
            "His appointment to the Supreme Court in 1799 was one "
            "of the last important judicial acts of the Adams "
            "administration before the Jeffersonian revolution in "
            "national politics. His tenure (1799–1804) was among "
            "the shortest of any Supreme Court justice — he wrote "
            "only one notable opinion, in the quasi-war prize case "
            "Bas v. Tingy (1800), which addressed the legal status "
            "of the undeclared naval war with France — and resigned "
            "in 1804 due to deteriorating health.\n\n"
            "His legal career in North Carolina was more substantial: "
            "as state attorney general he prosecuted Loyalists "
            "after the Revolution and contributed to North Carolina's "
            "post-war legal reconstruction. He was also a founder "
            "and trustee of the University of North Carolina at "
            "Chapel Hill — the first public university in the "
            "United States to open its doors (1795).\n\n"
            "Moore Square, a historic park in Raleigh, and Moore "
            "County, North Carolina, were named in his honor — "
            "testament to his standing in early North Carolina "
            "despite his brief and largely quiet Supreme Court tenure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Associate Justice of the US Supreme Court (1799–1804, appointed by John Adams); North Carolina attorney general; Revolutionary War militia officer; University of North Carolina co-founder/trustee; authored the opinion in Bas v. Tingy (1800) — the quasi-war prize case addressing the legal status of the undeclared naval war with France; one of the shortest-serving Supreme Court justices.",
            "significanceCategory": "regional"
        },
        "causes": [
            "John Adams's need for experienced Federalist lawyers to fill judicial vacancies — as the Adams administration worked to staff the federal judiciary with Federalists before the Jeffersonian transition — created the context for Moore's Supreme Court appointment in 1799",
            "North Carolina's post-Revolutionary need for legally trained attorney generals who could prosecute Loyalists and establish the state's legal authority — in a state where the Loyalist community had been large and the Revolutionary War's internal conflict particularly bitter — created the demand for Moore's prosecutorial career",
            "The quasi-war with France (1798–1800) and the legal questions it raised about prize cases, undeclared war, and the status of captured French vessels — questions that required the Supreme Court to address for the first time — created the occasion for Moore's one notable Supreme Court opinion in Bas v. Tingy"
        ],
        "effects": [
            "His opinion in Bas v. Tingy (1800) contributed to early American constitutional jurisprudence by establishing that the undeclared quasi-war with France was nonetheless a legally recognized state of limited war — a doctrine with implications for the president's authority to conduct naval operations without formal congressional declaration",
            "His co-founding and trusteeship of the University of North Carolina at Chapel Hill contributed to the establishment of the first state university in the United States to open its doors — an institution that became central to North Carolina's educational and cultural development",
            "His post-Revolutionary service as North Carolina attorney general contributed to the legal prosecution of Loyalists and the establishment of North Carolina's state legal authority in the difficult years of post-war reconstruction",
            "The naming of Moore Square in Raleigh and Moore County in his honor illustrated the high regard in which he was held by early North Carolina despite his brief Supreme Court tenure — reflecting his importance in the state's post-Revolutionary legal and political culture"
        ],
        "relationships": [
            {"entity": "US Supreme Court (Associate Justice, 1799–1804, Adams appointment)", "relationship": "ASSOCIATE_JUSTICE", "note": "Served as Associate Justice of the US Supreme Court (1799–1804) — one of the last major Adams judicial appointments before the Jeffersonian political transition"},
            {"entity": "Bas v. Tingy (1800, quasi-war prize case)", "relationship": "AUTHORED_OPINION_IN", "note": "Authored the opinion in Bas v. Tingy (1800) — the quasi-war case that established the legal status of the undeclared naval war with France and the doctrine of limited war"},
            {"entity": "University of North Carolina at Chapel Hill (co-founder and trustee)", "relationship": "CO-FOUNDED_AND_TRUSTEE_OF", "note": "Co-founder and trustee of the University of North Carolina at Chapel Hill — the first American public university to open its doors (1795)"},
            {"entity": "North Carolina attorney general (post-Revolutionary War)", "relationship": "ATTORNEY_GENERAL", "note": "Served as North Carolina attorney general after the Revolution — prosecuting Loyalists and contributing to the state's legal reconstruction"},
            {"entity": "American Revolutionary War / North Carolina militia (militia captain, southern campaign)", "relationship": "MILITIA_OFFICER_DURING", "note": "Served as a militia captain during the Revolutionary War — participating in the southern campaign that made North Carolina's war one of the most internally violent of any American state"}
        ]
    }),

    # 2 — Moses Robinson
    ("moses-robinson", {
        "summary": (
            "Moses Robinson (1742–1813) was a Vermont lawyer, judge, "
            "and politician who played a central role in Vermont's "
            "transition from an independent republic to a US state — "
            "serving as Vermont's first Chief Justice (1778–1782), "
            "as its Governor (1789–1790) when it was still technically "
            "an independent nation, and as one of Vermont's first "
            "two US Senators (1791–1796) after its admission to "
            "the Union as the fourteenth state.\n\n"
            "His gubernatorial term was historically significant: "
            "as governor of the independent Vermont Republic, "
            "he superintended the negotiations that led to Vermont's "
            "admission to the Union in 1791 — the first state "
            "admitted after the original thirteen. Vermont's path "
            "to statehood was uniquely complicated: it had been "
            "disputed by New York and New Hampshire, had fought "
            "its own internal conflicts with both states' land "
            "claimants, and had existed as an unrecognized republic "
            "for fourteen years before Congress accepted its admission.\n\n"
            "As a US Senator, Robinson was notably Anti-Federalist "
            "in orientation — one of the voices in the Senate "
            "that opposed the Federalist program of the 1790s, "
            "including the Jay Treaty with Britain. He opposed "
            "the treaty on the grounds that it was too favorable "
            "to British commercial interests and too dismissive "
            "of French grievances.\n\n"
            "His career bridged Vermont's entire political history "
            "from the founding of its Republic through its "
            "integration into the American federal system."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First Chief Justice of Vermont (1778–1782); Governor of the independent Vermont Republic (1789–1790); supervised negotiations for Vermont's admission to the Union as the 14th state (1791); one of Vermont's first two US Senators (1791–1796); Anti-Federalist who opposed the Jay Treaty; his career spans Vermont's full history from independent republic to US statehood.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's unique political status as an unrecognized independent republic — disputed by New York and New Hampshire and unrepresented in the Continental Congress — created the need for figures like Robinson with the legal and judicial standing to build state institutions from scratch and negotiate statehood terms",
            "The Vermont Republic's founding conflicts with New York and New Hampshire over the New Hampshire Grants land claims — and the Green Mountain Boys' assertion of Vermont's autonomy — created the political culture of independence that shaped Robinson's career as a judicial and political founder",
            "The Federalist constitutional settlement of 1787–1791 — and Vermont's desire for the economic benefits of membership in the new federal union while preserving its political autonomy — created the negotiation process that Robinson as governor managed to bring to successful conclusion"
        ],
        "effects": [
            "His gubernatorial supervision of Vermont's statehood negotiations contributed to the admission of Vermont as the 14th state in 1791 — the first expansion of the original thirteen-state union and a crucial test of the Constitution's procedure for admitting new states",
            "His four-year term as Vermont's first Chief Justice contributed to building Vermont's legal system from the ground up — establishing judicial precedents, procedures, and institutional structures for a state that had been operating outside the American constitutional framework",
            "His Anti-Federalist Senate votes — particularly his opposition to the Jay Treaty — contributed to the minority opposition to Federalist foreign policy in the 1790s, articulating the position that the Jay Treaty betrayed American democratic allies in France while favoring British commercial interests",
            "Vermont's unique institutional history — an independent republic for 14 years before statehood — provided a model and a cautionary tale for the admission of subsequent states, demonstrating both the viability and the costs of extra-constitutional state formation on the American frontier"
        ],
        "relationships": [
            {"entity": "Vermont Republic (first Chief Justice, 1778–1782)", "relationship": "FIRST_CHIEF_JUSTICE_OF", "note": "Served as Vermont's first Chief Justice (1778–1782) — building the legal institutions of the independent republic from the ground up"},
            {"entity": "Governor of Vermont Republic (1789–1790, supervised statehood negotiations)", "relationship": "GOVERNOR_DURING_STATEHOOD_NEGOTIATIONS", "note": "As Governor of the independent Vermont Republic (1789–1790), superintended the negotiations that led to Vermont's admission to the Union as the 14th state in 1791"},
            {"entity": "Vermont statehood (1791, 14th state admitted to the Union)", "relationship": "SUPERVISED_NEGOTIATIONS_FOR", "note": "Supervised the negotiations that resulted in Vermont's admission to the Union as the 14th state in 1791 — the first post-original expansion of the US"},
            {"entity": "US Senate from Vermont (one of first two senators, 1791–1796)", "relationship": "FIRST_SENATOR", "note": "Served as one of Vermont's first two US Senators (1791–1796) — representing a newly admitted state with strong Anti-Federalist political traditions"},
            {"entity": "Jay Treaty (1794–1795, opposed as Anti-Federalist)", "relationship": "OPPOSED_AS_ANTI-FEDERALIST", "note": "Opposed the Jay Treaty in the Senate as an Anti-Federalist — arguing it was too favorable to British commercial interests and betrayed American democratic allies in France"}
        ]
    }),

    # 3 — Muhammad al-Abdari al-Hihi
    ("muhammad-al-abdari-al-hihi", {
        "summary": (
            "Muhammad al-Abdari al-Hihi (fl. 1289–1295) was a "
            "Maghrebi Berber scholar and travel writer from the "
            "Haha tribe — a Berber community settled in southern "
            "present-day Morocco — who composed one of the most "
            "detailed medieval Arabic travel accounts of the "
            "pilgrimage route from the Maghreb to Mecca. "
            "His Rihlat al-Abdari (The Maghrebi Journey), composed "
            "after his 1289–1290 hajj, documented the full overland "
            "route from Morocco through Algeria, Tunisia, Libya, "
            "Egypt, the Sinai, and the Hijaz to Mecca.\n\n"
            "The rihla — the Arabic travel account — was one of "
            "the most important literary genres of medieval Islamic "
            "civilization, and al-Abdari's work sits in a tradition "
            "that includes Ibn Battuta's later and more famous "
            "Rihla. Al-Abdari's account is particularly valuable "
            "for its vivid social and ethnographic observations: "
            "he recorded the customs, scholarly life, religious "
            "practices, and physical conditions of the cities and "
            "communities he encountered along the pilgrimage road — "
            "providing historians with detailed evidence of late "
            "13th-century urban life across the Muslim western "
            "Mediterranean and North Africa.\n\n"
            "His account includes notable critical observations "
            "of Andalusian scholars and communities — reflecting "
            "the Moroccan perspective on the deteriorating Muslim "
            "political situation in al-Andalus in the decades "
            "before the final collapse of the Nasrid kingdom. "
            "His sharp critique of what he saw as lax religious "
            "practices in some communities makes his Rihla one "
            "of the more polemically interesting travel accounts "
            "of the medieval Islamic world.\n\n"
            "The text was published by Morocco's Ministry of "
            "Education in 1968, making it accessible to modern "
            "historians of medieval Maghrebi and Islamic history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Maghrebi Berber scholar from the Haha tribe (Morocco); author of Rihlat al-Abdari — a detailed 1289 hajj travel account documenting the overland route from Morocco to Mecca; important source for late 13th-century urban and social conditions across the Maghreb and North Africa; member of the Arabic rihla literary tradition; critical ethnographic observer of Andalusian Muslim communities; published 1968 by Morocco's Ministry of Education.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Islamic obligation of hajj — and the cultural tradition of the rihla (travel account) as both a religious and scholarly act — created the occasion and literary form for al-Abdari's journey and account: the Maghrebi pilgrimage route was a structured cultural institution that generated documentation across centuries",
            "The late 13th-century Maghrebi political landscape — with the Marinid dynasty consolidating power in Morocco and the deteriorating Reconquista threatening Andalusian Muslim communities — provided the political context for al-Abdari's observations about Moroccan, Algerian, Tunisian, and Andalusian communities along his route",
            "The rihla's established literary conventions — developed through earlier Maghrebi travel writers and formalized in the Arab-Islamic scholarly tradition — provided al-Abdari with the genre framework for organizing his observations into a coherent literary account that would preserve and transmit his journey"
        ],
        "effects": [
            "His Rihlat al-Abdari provided historians with one of the most detailed surviving accounts of the overland pilgrimage route from Morocco to Mecca in the late 13th century — documenting cities, institutions, scholars, and social conditions at a moment just before the major political transformations of the 14th century",
            "His ethnographic observations of Andalusian Muslim communities contributed evidence for historians studying the final centuries of Muslim political presence in the Iberian Peninsula — recording social and religious conditions in communities under increasing Reconquista pressure",
            "His place in the rihla literary tradition — before the far more famous Ibn Battuta (fl. 1325–1368) but after the earlier Maghrebi travelers — contributed to the genre's development as one of the primary forms of medieval Islamic geographical and cultural documentation",
            "The 1968 publication of the Rihlat al-Abdari by Morocco's Ministry of Education made his observations accessible to modern scholarship — contributing to the historiography of medieval Maghrebi society, the hajj route, and the Arabic travel-writing tradition"
        ],
        "relationships": [
            {"entity": "Rihlat al-Abdari / The Maghrebi Journey (1289–1290 hajj account)", "relationship": "AUTHOR_OF", "note": "Composed the Rihlat al-Abdari — a detailed account of his 1289–1290 hajj journey from Morocco overland to Mecca — one of the most important medieval Arabic travel accounts of the Maghreb-to-Mecca route"},
            {"entity": "Arabic rihla literary tradition (medieval Islamic travel writing genre)", "relationship": "PRACTITIONER_OF", "note": "A practitioner of the Arabic rihla — the literary travel-account genre that included Ibn Battuta's more famous work — contributing to its development as a vehicle for geographical and ethnographic documentation"},
            {"entity": "Haha Berber tribe / southern Morocco (origin community)", "relationship": "BORN_INTO", "note": "Born among the Haha — a Berber tribe settled in southern present-day Morocco — giving his Maghrebi perspective distinctive regional roots"},
            {"entity": "Hajj overland route (Morocco → Algeria → Tunisia → Libya → Egypt → Mecca, 1289)", "relationship": "DOCUMENTED_THE_ROUTE_OF", "note": "Documented the full overland hajj route from Morocco to Mecca in 1289 — recording cities, scholars, religious conditions, and social life across the late 13th-century Muslim western Mediterranean"},
            {"entity": "Andalusian Muslim communities (late 13th century, Reconquista period)", "relationship": "CRITICALLY_OBSERVED_AND_DOCUMENTED", "note": "Provided critical ethnographic observations of Andalusian Muslim communities in his Rihla — recording what he perceived as lax religious practices in communities under Reconquista pressure"}
        ]
    }),

    # 4 — John Gayle
    ("john-gayle", {
        "summary": (
            "John Gayle (1792–1859) was an Alabama lawyer, "
            "politician, and judge who held a remarkable range "
            "of offices across nearly three decades of public "
            "life — serving as the 7th Governor of Alabama "
            "(1831–1835), as a US Representative from Alabama "
            "(1847–1853), as a justice of the Alabama Supreme "
            "Court, and as a US district judge for three Alabama "
            "federal judicial districts. Born in Sumter County, "
            "South Carolina, he studied law and moved to Alabama "
            "territory before statehood.\n\n"
            "His governorship (1831–1835) coincided with the "
            "most contentious political moment of the Jacksonian "
            "era: the Nullification Crisis of 1832–1833, in which "
            "South Carolina formally declared federal tariff laws "
            "unconstitutional and threatened secession. Gayle "
            "navigated Alabama's response to the crisis — Alabama "
            "rejected nullification and affirmed federal authority, "
            "a position Gayle supported — while also managing "
            "the pressures of the Indian Removal Act's implementation "
            "in Alabama, including the forced removal of Creek "
            "Nation communities.\n\n"
            "His subsequent career on the Alabama Supreme Court "
            "and in Congress (1847–1853) contributed to Alabama's "
            "antebellum legal and political development, and "
            "his appointment as federal district judge in the "
            "1850s gave him judicial authority over Alabama's "
            "three federal districts simultaneously.\n\n"
            "His daughter Amelia Gayle married journalist and "
            "politician Josiah Gorgas — who became the Confederate "
            "Army's chief ordnance officer — extending the Gayle "
            "family's significance into the Civil War era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "7th Governor of Alabama (1831–1835); US Representative from Alabama (1847–1853); Alabama Supreme Court Justice; US District Judge for three Alabama federal districts; presided over Alabama's response to the Nullification Crisis and the Creek Nation removal; his daughter married Confederate ordnance chief Josiah Gorgas.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Alabama's early statehood development (1819) — and its rapid political institutionalization under Jacksonian Democratic governance — created the demand for experienced lawyers like Gayle who could fill the multiple overlapping judicial and executive positions of an expanding frontier state",
            "The Nullification Crisis (1832–1833) — Andrew Jackson's confrontation with South Carolina's assertion of the right to nullify federal law — forced Alabama's governor to take a public position on the most divisive constitutional question of the era, shaping Gayle's political legacy as a defender of federal authority",
            "The Indian Removal Act (1830) and its implementation in Alabama — forcing the Creek Nation's removal from Alabama lands — created the political and legal challenge that dominated Gayle's governorship, requiring him to manage federal policy, state interests, and the violent dispossession of indigenous communities simultaneously"
        ],
        "effects": [
            "His support for federal authority during the Nullification Crisis helped align Alabama with Andrew Jackson's position — refusing to support South Carolina's nullification doctrine and contributing to the political isolation of South Carolina's constitutional gambit",
            "His administration's management of Creek Nation removal contributed to the dispossession of the Alabama Creek communities and their forced relocation west of the Mississippi — one of the most consequential and destructive events in Alabama's early history",
            "His combined career as governor, congressman, and judge contributed to the development of Alabama's legal, judicial, and legislative institutions across the critical antebellum period (1831–1859) when the state was transitioning from frontier to established cotton-economy society",
            "His daughter's marriage to Confederate General Josiah Gorgas — who became the Confederate Army's indispensable ordnance chief — extended the Gayle family's historical significance into the Civil War, connecting antebellum Alabama political leadership to Confederate military administration"
        ],
        "relationships": [
            {"entity": "7th Governor of Alabama (1831–1835)", "relationship": "7TH_GOVERNOR", "note": "Served as Alabama's 7th Governor (1831–1835) — presiding over the state's response to the Nullification Crisis and the implementation of the Creek Nation removal"},
            {"entity": "Nullification Crisis (1832–1833) / Alabama's rejection of nullification", "relationship": "GOVERNOR_DURING_DEFENDED_FEDERAL_AUTHORITY", "note": "As governor during the Nullification Crisis, supported federal authority against South Carolina's nullification doctrine — contributing to Alabama's rejection of the constitutional position"},
            {"entity": "Creek Nation removal from Alabama (Indian Removal Act implementation)", "relationship": "GOVERNOR_DURING_MANAGED_IMPLEMENTATION_OF", "note": "Managed the implementation of the Indian Removal Act in Alabama during his governorship — presiding over the forced dispossession of Creek Nation communities"},
            {"entity": "US House of Representatives from Alabama (1847–1853)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from Alabama (1847–1853) — contributing to Alabama's congressional representation during the escalating antebellum sectional crisis"},
            {"entity": "Josiah Gorgas (son-in-law, Confederate Army ordnance chief)", "relationship": "FATHER-IN-LAW_OF", "note": "Father-in-law of Josiah Gorgas — the Confederate Army's chief ordnance officer, widely credited with keeping the Confederate war effort supplied — extending the Gayle family's significance into the Civil War"}
        ]
    }),

    # 5 — Feargus O'Connor
    ("feargus-oconnor", {
        "summary": (
            "Feargus Edward O'Connor (1796–1855) was an Irish "
            "radical politician and the most prominent leader of "
            "Chartism — the first mass working-class political "
            "movement in British history — whose energy, oratory, "
            "and journalism made him the movement's dominant "
            "personality from the late 1830s through the early "
            "1850s. Born into an Irish Protestant gentry family "
            "in County Cork, he was educated as a lawyer, entered "
            "Irish politics, and was elected to Westminster Parliament "
            "for Cork in 1832 — only to lose the seat in 1835 "
            "when his income qualifications were challenged.\n\n"
            "He founded the Northern Star in 1837 — the most widely "
            "read working-class newspaper in British history, "
            "with a peak circulation of around 50,000 — which "
            "became the primary vehicle for Chartist organization, "
            "agitation, and debate through its 15-year run "
            "(1837–1852). He was elected MP for Nottingham in 1847 — "
            "the first working-class constituency to elect a "
            "Chartist to Parliament — and organized the great "
            "Chartist petition campaign of 1848, which claimed "
            "nearly six million signatures.\n\n"
            "His Land Plan (1845–1848) was among the most ambitious "
            "radical social experiments of the 19th century: "
            "a cooperative land settlement scheme that aimed to "
            "resettle industrial workers on smallholdings — "
            "combining the Chartist demand for political rights "
            "with an agrarian alternative to industrial capitalism. "
            "The Land Company established several colonies before "
            "parliamentary investigation and financial difficulties "
            "ended the scheme.\n\n"
            "He died in 1855, having spent the last years of his "
            "life in deteriorating mental health — a figure "
            "admired for his charisma and criticized for his "
            "domineering personality, but undeniably the man "
            "who more than any other gave Chartism its mass energy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Irish Chartist leader; founding editor of the Northern Star (1837–1852) — the most widely-read working-class newspaper in British history; leader of the great 1848 Chartist petition campaign; MP for Nottingham (1847); architect of the Chartist Land Plan cooperative settlement scheme; the dominant personality of Britain's first mass working-class political movement; one of 19th-century Britain's most charismatic radical agitators.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The industrial revolution's transformation of the British working class — creating vast urban populations with no political representation under the restricted pre-Reform Act franchise — created the mass constituency for Chartism's demands for universal male suffrage, the ballot, and annual parliaments",
            "The failure of the 1832 Great Reform Act to extend the franchise to working-class voters — despite the popular agitation that had made reform politically irresistible — created the bitter sense of betrayal that fueled Chartism's emergence as an independent working-class movement demanding what the Whigs had refused to deliver",
            "O'Connor's personal attributes — his remarkable oratory, his Irish Protestant gentry's aristocratic confidence, his genuine connection to working-class audiences, and his journalistic ability through the Northern Star — created the personal leadership capacity that made him Chartism's dominant figure rather than any of the movement's more programmatically sophisticated leaders"
        ],
        "effects": [
            "The Northern Star (1837–1852) contributed to the political education and organization of the British working class on an unprecedented scale — giving Chartism a communication network that could coordinate agitation across the country's industrial regions simultaneously, creating the infrastructure for mass politics",
            "The great Chartist petition campaign of 1848 — the year of European revolutions — demonstrated both the mass scale of working-class democratic demands in Britain and the limits of peaceful pressure politics: Parliament rejected the petition, but the 1848 moment crystallized the political arguments that would eventually produce the parliamentary reform acts of 1867 and 1884",
            "The Chartist Land Plan, though it failed financially, introduced the idea of cooperative land settlement as an alternative to industrial capitalism — an idea that influenced subsequent cooperative movements, back-to-the-land schemes, and late 19th-century socialist agrarianism",
            "Chartism as a movement — despite failing to achieve its immediate demands — contributed to the long-term transformation of British political culture by demonstrating the existence and organizational capacity of working-class political demand, shifting the political terrain that eventually produced the Labour Party and the full democratic franchise"
        ],
        "relationships": [
            {"entity": "Northern Star newspaper (1837–1852, Chartist voice)", "relationship": "FOUNDED_AND_EDITED", "note": "Founded and edited the Northern Star (1837–1852) — the most widely-read working-class newspaper in British history and the primary communication vehicle of the Chartist movement"},
            {"entity": "Chartism / British working-class political movement (1838–1858)", "relationship": "DOMINANT_LEADER_OF", "note": "The dominant leader and most prominent personality of Chartism — Britain's first mass working-class political movement demanding universal male suffrage and democratic reform"},
            {"entity": "Chartist Land Plan / National Land Company (1845–1848)", "relationship": "ARCHITECT_OF", "note": "Architect of the Chartist Land Plan — a cooperative scheme to resettle industrial workers on smallholdings — one of the most ambitious radical social experiments of 19th-century Britain"},
            {"entity": "Great Chartist Petition of 1848 (six million signatures)", "relationship": "ORGANIZED", "note": "Organized the great Chartist petition campaign of 1848 — claiming nearly six million signatures — which Parliament rejected in the same year that European revolutions swept the continent"},
            {"entity": "MP for Nottingham (1847, first Chartist elected to Parliament)", "relationship": "ELECTED_MP", "note": "Elected MP for Nottingham in 1847 — the first working-class constituency to elect a Chartist to Parliament — giving the movement its first direct parliamentary representation"}
        ]
    }),

    # 6 — William Grayson
    ("william-grayson", {
        "summary": (
            "William Grayson (c.1736–1790) was a Virginia planter, "
            "lawyer, and statesman — a Revolutionary War colonel, "
            "Anti-Federalist leader at the Virginia ratifying "
            "convention, and one of Virginia's first two US Senators "
            "(1789–1790) — who holds the distinction of being "
            "the first member of the United States Congress to "
            "die while holding office. Born to a Virginia planting "
            "family, he was educated at Oxford and the Inner "
            "Temple, and returned to Virginia to practice law "
            "and manage his estate.\n\n"
            "His Revolutionary War service was distinguished: "
            "he commanded a Virginia Continental regiment at "
            "the Battle of Brandywine and Germantown, served "
            "on George Washington's personal staff, and was "
            "present at Valley Forge. He subsequently served "
            "in the Continental Congress (1784–1787).\n\n"
            "His most politically significant role was as a leader "
            "of Anti-Federalist opposition at Virginia's 1788 "
            "Constitutional ratifying convention — one of the most "
            "consequential of all the state ratifying debates. "
            "Alongside Patrick Henry and George Mason, he argued "
            "against ratification on the grounds that the "
            "Constitution gave excessive power to the federal "
            "government, lacked a bill of rights, and would "
            "threaten Virginia's political independence. "
            "Virginia ratified by 89–79 — the narrowest margin "
            "of any large state — before the Anti-Federalists "
            "extracted the promise of a bill of rights.\n\n"
            "He was elected US Senator in 1789 but died in "
            "March 1790 — becoming the first member of the new "
            "Congress to die in office — before he could see "
            "whether the promised Bill of Rights would be fulfilled."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Anti-Federalist leader at the 1788 Constitutional ratifying convention alongside Patrick Henry and George Mason; Continental Army colonel (Brandywine, Germantown, Valley Forge, Washington's staff); Continental Congress delegate (1784–1787); one of Virginia's first two US Senators (1789–1790); first member of the US Congress to die in office (March 1790); his opposition helped extract the promise of the Bill of Rights.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's powerful Anti-Federalist tradition — rooted in the state's large-planter political culture, its memory of colonial self-governance, and the leadership of Patrick Henry and George Mason — created the political environment for Grayson's Anti-Federalist leadership at the 1788 ratifying convention",
            "The Constitutional Convention's failure to include a bill of rights — which Madison had considered unnecessary but which the Anti-Federalists made the central demand of their opposition — created the political dynamic that made Grayson and his colleagues effective enough to extract the promise of constitutional amendments before Virginia ratified",
            "His Oxford and Inner Temple legal education — combined with his Continental Army service and Continental Congress experience — gave him the intellectual and institutional credentials to lead the Anti-Federalist legal argument at the Virginia convention alongside the politically formidable Patrick Henry"
        ],
        "effects": [
            "His leadership of the Anti-Federalist opposition at Virginia's 1788 ratifying convention contributed to the closest large-state ratification vote (89–79) and to the extraction of Madison's commitment to submit a bill of rights to the First Congress — directly contributing to the creation of the first ten constitutional amendments",
            "His death in March 1790 as the first member of Congress to die in office created a historical precedent for congressional succession and the management of Senate vacancies — a procedural moment that established practices followed throughout American congressional history",
            "His Continental Army service — on Washington's personal staff, at Brandywine and Germantown, and at Valley Forge — contributed to the military effort that secured independence, and his subsequent career linked Virginia's military contribution to its post-war political and constitutional debates",
            "Virginia's narrow 89–79 ratification margin — which Grayson and his Anti-Federalist colleagues nearly prevented — illustrated the depth of constitutional skepticism in the most populous state, and shaped the subsequent history of the Bill of Rights as the political price of ratification"
        ],
        "relationships": [
            {"entity": "Virginia Anti-Federalist opposition / 1788 Constitutional ratifying convention (leader alongside Henry and Mason)", "relationship": "LED_ALONGSIDE_HENRY_AND_MASON", "note": "Led the Anti-Federalist opposition at Virginia's 1788 Constitutional ratifying convention alongside Patrick Henry and George Mason — nearly preventing ratification and extracting the promise of a bill of rights"},
            {"entity": "Continental Army (colonel, Washington's staff, Brandywine/Germantown/Valley Forge)", "relationship": "COLONEL_AND_STAFF_OFFICER_OF", "note": "Served as a Continental Army colonel on Washington's personal staff — present at Brandywine, Germantown, and Valley Forge during the war's critical Philadelphia campaign"},
            {"entity": "US Senate from Virginia (one of first two senators, 1789–1790)", "relationship": "FIRST_SENATOR_DIED_IN_OFFICE", "note": "One of Virginia's first two US Senators (1789–1790) — the first member of the US Congress to die while holding office (March 1790)"},
            {"entity": "Continental Congress (Virginia delegate, 1784–1787)", "relationship": "DELEGATE", "note": "Served as a Virginia delegate to the Continental Congress (1784–1787) — connecting his Revolutionary War military service to the transition toward constitutional governance"},
            {"entity": "Bill of Rights (US Constitution, first ten amendments, 1791)", "relationship": "ANTI-FEDERALIST_WHOSE_OPPOSITION_CONTRIBUTED_TO_CREATION_OF", "note": "His Anti-Federalist leadership helped extract the promise of a bill of rights from Madison as the price of Virginia's ratification — directly contributing to the creation of the first ten constitutional amendments"}
        ]
    }),

    # 7 — Jacques-Nicolas Billaud-Varenne
    ("jacques-nicolas-billaud-varenne", {
        "summary": (
            "Jacques-Nicolas Billaud-Varenne (1756–1819) was a "
            "French revolutionary lawyer and radical politician — "
            "nicknamed 'the Tiger' and 'the Righteous Patriot' — "
            "who served on the Committee of Public Safety (1793–1794) "
            "and is considered one of the principal architects "
            "of the Reign of Terror. A close associate of Danton "
            "and Robespierre, he was among the most militant voices "
            "demanding the systematic elimination of the Revolution's "
            "enemies — real, suspected, and imagined.\n\n"
            "Born in La Rochelle to a bourgeois family, he was "
            "educated in Jesuit schools, then turned against the "
            "Church and aristocracy with the ideological ferocity "
            "that characterized the most radical Jacobins. "
            "He was among those who urged the September Massacres "
            "of 1792 — the prison killings of thousands of "
            "suspected counter-revolutionaries — and in 1793 "
            "became one of the driving forces behind the "
            "Committee of Public Safety's escalating use of "
            "the guillotine to purify the Republic.\n\n"
            "Remarkably, he survived Thermidor: he was among "
            "those who turned against Robespierre in the Thermidorian "
            "reaction of July 1794, voting for his arrest and "
            "execution. But the Thermidorians then prosecuted the "
            "Terror's survivors: Billaud-Varenne was arrested "
            "and deported to French Guiana (Cayenne) in 1795. "
            "He refused repatriation under Napoleon's amnesty "
            "and settled in independent Haiti, where he died "
            "in 1819 — a voluntary exile from the France he "
            "had helped to transform.\n\n"
            "His refusal to return to France — even when offered "
            "amnesty — stood as a final statement of unreconciled "
            "revolutionary conviction."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Revolutionary; Committee of Public Safety member (1793–1794); one of the principal architects of the Reign of Terror; nicknamed 'the Tiger'; urged the September Massacres (1792); turned on Robespierre at Thermidor; deported to French Guiana (1795); refused Napoleon's amnesty and settled in Haiti where he died (1819); one of the most uncompromising Jacobin radicals of the French Revolution.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolutionary radical ideology — with its Rousseauian demand for republican virtue and its logic that the Revolution must destroy all internal enemies to survive — provided the political-philosophical framework within which Billaud-Varenne's escalating advocacy for the Terror made ideological sense to his contemporaries",
            "The external military threats to the Republic in 1793 — the War of the First Coalition, the Vendée counter-revolutionary uprising, and the federalist revolts in Lyon and other cities — created the genuine emergency conditions that the Committee of Public Safety exploited to justify the Terror as an emergency measure of national survival",
            "Robespierre's domination of the Committee of Public Safety and his ability to use the logic of revolutionary virtue to destroy anyone who questioned the Terror — combined with the spiral of mutual denunciation that the Terror itself created — produced the unstable political dynamic that eventually turned Billaud-Varenne and others against Robespierre at Thermidor"
        ],
        "effects": [
            "His contributions to the Committee of Public Safety contributed to the design and execution of the Reign of Terror's systematic use of the Revolutionary Tribunal and the guillotine — a process that killed approximately 17,000 people officially and tens of thousands more in summary executions and prison conditions during 1793–1794",
            "His participation in the Thermidorian reaction — helping to orchestrate Robespierre's arrest and execution on 9 Thermidor Year II (July 27, 1794) — contributed to the end of the Terror and the Thermidorian dismantling of the most radical Jacobin institutions",
            "His deportation to French Guiana and subsequent Haitian exile made him one of the most symbolically significant post-Thermidor figures: a Terror architect who survived the Terror, was punished by its aftermath, and refused reconciliation with the post-revolutionary French state under Napoleon",
            "His voluntary exile and death in Haiti — refusing to return even under Napoleon's amnesty — contributed to Haiti's post-revolutionary significance as a refuge for European radicals and a symbol of republican principles that France itself had abandoned in the Napoleonic reaction"
        ],
        "relationships": [
            {"entity": "Committee of Public Safety (1793–1794, principal architect of the Terror)", "relationship": "MEMBER_AND_ARCHITECT_OF_TERROR", "note": "Served on the Committee of Public Safety (1793–1794) as one of the principal architects of the Reign of Terror — one of the most militant voices for the systematic elimination of the Revolution's enemies"},
            {"entity": "Reign of Terror (1793–1794, ~17,000 official executions)", "relationship": "ARCHITECT_OF", "note": "One of the principal architects of the Reign of Terror — contributing to the systematic use of the Revolutionary Tribunal and the guillotine that killed approximately 17,000 people officially during 1793–1794"},
            {"entity": "Thermidorian reaction (9 Thermidor Year II, July 27, 1794)", "relationship": "PARTICIPATED_IN_AGAINST_ROBESPIERRE", "note": "Participated in the Thermidorian reaction — helping to orchestrate Robespierre's arrest and execution on 9 Thermidor Year II — contributing to the end of the Terror despite his own role in creating it"},
            {"entity": "September Massacres (1792, Paris prison killings)", "relationship": "URGED_AND_FACILITATED", "note": "Among those who urged and facilitated the September Massacres of 1792 — the killing of thousands of suspected counter-revolutionaries in Paris prisons — one of the Revolution's most brutal early atrocities"},
            {"entity": "Haiti (exile and death, 1795–1819, refused Napoleon's amnesty)", "relationship": "DIED_IN_VOLUNTARY_EXILE_IN", "note": "Deported to French Guiana (1795), eventually settled in independent Haiti, and refused Napoleon's amnesty — dying in Haitian exile in 1819 as a symbol of unreconciled revolutionary conviction"}
        ]
    }),

    # 8 — Dominique Bouligny
    ("dominique-bouligny", {
        "summary": (
            "Charles Dominique Joseph Bouligny (1773–1833) was "
            "a Louisiana lawyer and politician of French and "
            "Spanish Creole descent who served as US Senator "
            "from Louisiana from 1824 to 1829 — representing "
            "the state's Creole political establishment during "
            "the transition from early statehood to the "
            "Jacksonian era. Born in New Orleans, he came "
            "from one of Louisiana's most prominent Creole "
            "families and was part of the cultural and "
            "commercial elite that had governed Louisiana "
            "under both French and Spanish colonial rule.\n\n"
            "He served earlier in Louisiana's territorial "
            "House of Representatives — contributing to "
            "the legislative institutions of a territory "
            "whose transition from Spanish to American "
            "governance required rebuilding virtually every "
            "political and legal institution to conform to "
            "American constitutional norms. Louisiana's "
            "admission in 1812 as the first state formed "
            "from the Louisiana Purchase represented a "
            "significant test of the US political system's "
            "capacity to absorb non-Anglophone populations.\n\n"
            "His Senate service (1824–1829) coincided with "
            "the collapse of the Era of Good Feelings and "
            "the emergence of Jacksonian democracy — a "
            "political transformation that presented "
            "particular challenges for Louisiana's Creole "
            "elite, which had dominated state politics "
            "but faced increasing pressure from the "
            "American-born settlers flooding into Louisiana.\n\n"
            "His brother Louis Bouligny served as a state "
            "representative and his nephew John Edward "
            "Bouligny later became a US Representative — "
            "illustrating the family's multigenerational "
            "contribution to Louisiana political life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator from Louisiana (1824–1829); Louisiana Creole political figure of French and Spanish descent; Louisiana territorial House of Representatives; member of one of Louisiana's most prominent Creole families; brother of state representative Louis Bouligny; uncle of US Representative John Edward Bouligny; his career illustrates Louisiana's Creole political establishment during the transition to Jacksonian America.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louisiana's Creole political establishment — rooted in the French and Spanish colonial elite that had governed the territory for more than a century before the Louisiana Purchase — created the social network and political culture from which Bouligny's career emerged, as one of the Creole families that sought to maintain political influence in American Louisiana",
            "Louisiana's admission to the Union in 1812 — as the first state carved from the Louisiana Purchase — created the new institutional framework of Senate seats, legislative positions, and judicial offices that the Creole elite competed to fill alongside the growing American-born settler population",
            "The Era of Good Feelings' political consensus — and its subsequent collapse into Jacksonian factional conflict in the mid-1820s — shaped Bouligny's Senate career, placing him in Washington during the most contested presidential election in American history (1824) and the emergence of the Jacksonian movement that would transform Louisiana's political culture"
        ],
        "effects": [
            "His Senate service (1824–1829) contributed to Louisiana's representation in Congress during the Era of Good Feelings' collapse and the emergence of Jacksonian democracy — a period of significant political realignment for a state whose Creole elite was navigating the transition from colonial to American governance",
            "His career as part of Louisiana's Creole political establishment contributed to the preservation of Creole political influence in a state that was being demographically transformed by American-born migration — demonstrating the Creole elite's capacity to compete successfully within American constitutional institutions",
            "The Bouligny family's multigenerational political contribution — through Dominique's senatorial career, Louis's state legislative service, and John Edward's subsequent congressional career — illustrated the pattern of Louisiana Creole family political dynasties in early American Louisiana",
            "His service in the Louisiana territorial House of Representatives before statehood contributed to the legislative institutions of a territory undergoing the most complex political transition in early American history — adapting French and Spanish legal traditions to American constitutional norms"
        ],
        "relationships": [
            {"entity": "US Senate from Louisiana (1824–1829)", "relationship": "SENATOR", "note": "Served as US Senator from Louisiana (1824–1829) — representing the state's Creole political establishment during the transition from the Era of Good Feelings to Jacksonian democracy"},
            {"entity": "Louisiana Creole political establishment (French and Spanish colonial elite)", "relationship": "MEMBER_OF", "note": "A member of Louisiana's French and Spanish Creole political establishment — one of the elite Creole families that sought to maintain political influence in American Louisiana after the Louisiana Purchase"},
            {"entity": "Louisiana territorial House of Representatives (pre-statehood, 1812)", "relationship": "MEMBER_OF", "note": "Served in Louisiana's territorial House of Representatives before statehood — contributing to the legislative institutions of the territory during its transition from Spanish to American governance"},
            {"entity": "Louis Bouligny (brother, Louisiana state representative)", "relationship": "BROTHER_OF", "note": "Brother of Louis Bouligny — a Louisiana state representative — the Bouligny family's multigenerational contribution to Louisiana political life beginning with their generation"},
            {"entity": "John Edward Bouligny (nephew, US Representative from Louisiana)", "relationship": "UNCLE_OF", "note": "Uncle of John Edward Bouligny — who later served as a US Representative from Louisiana — extending the Bouligny family's political presence into the mid-19th century"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 43)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
