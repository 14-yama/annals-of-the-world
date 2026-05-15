#!/usr/bin/env python3
"""
Batch 80 — 8 entities: Nathaniel Pitcher, Thomas Fitzgerald 7th Earl of Kildare,
William Upham, André-Marie-Jean-Jacques Dupin, Peter Early, Richard Spencer,
William Beach Lawrence, Antoine Loysel
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

    ("nathaniel-pitcher", {
        "summary": (
            "Nathaniel Pitcher (1777–1836) "
            "was an American Democratic-Republican "
            "and Democratic politician "
            "from New York who served "
            "in the U.S. House "
            "(1819–1823 and 1825–1829), "
            "as Acting Governor "
            "of New York (1828), "
            "and as Lieutenant "
            "Governor (1827–1828). "
            "His acting governorship "
            "came when Governor "
            "DeWitt Clinton was "
            "away — a brief executive "
            "tenure during the "
            "crucial 1828 election "
            "year when Andrew Jackson "
            "was mobilizing his "
            "presidential campaign "
            "against John Quincy Adams. "
            "New York's electoral "
            "votes were decisive "
            "in this election, "
            "and the state's "
            "political maneuvering "
            "around Jackson and "
            "Van Buren's emerging "
            "alliance was politically "
            "consequential.\n\n"
            "Pitcher served as "
            "a Congressman during "
            "the Era of Good Feelings, "
            "the Missouri Compromise "
            "debates, and the "
            "opening of the "
            "Jacksonian political revolution.\n\n"
            "His career represented "
            "the transition from "
            "Democratic-Republican "
            "to Jacksonian Democratic "
            "politics in New York.\n\n"
            "He was a St. Lawrence "
            "County farmer and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Democratic Congressman (1819–1823 and 1825–1829), Lieutenant Governor (1827–1828), and Acting Governor (1828); served during the pivotal 1828 Jackson election; participated in the transition from Democratic-Republican to Jacksonian Democratic politics in New York; north country congressman during the Era of Good Feelings and Missouri Compromise debates.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Jacksonian political realignment — the Van Buren-Jackson alliance building that transformed New York's Democratic-Republican into the Jacksonian Democratic machine — created the political transition that Pitcher navigated",
            "DeWitt Clinton's death and gubernatorial absences — Clinton's dominance of New York politics and the circumstances that created Pitcher's acting governorship — placed Pitcher briefly in the executive office during the decisive 1828 election year",
            "The Missouri Compromise crisis — the national debate over slavery extension that dominated Pitcher's first House terms — created the major policy controversy of his early congressional career"
        ],
        "effects": [
            "His acting governorship contributed New York's executive voice to the 1828 election year — managing the state's government during the pivotal presidential campaign",
            "His four congressional terms contributed New York's north country perspective to the Era of Good Feelings and Jacksonian transition debates",
            "His career contributed to the Jacksonian Democratic organization in New York — the political machine that Van Buren built and that would dominate state politics",
            "His career illustrated the political transition that many Democratic-Republicans made — shifting from the founding era's consensual politics to the more organized, competitive Jacksonian Democratic party system"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1819–1823 and 1825–1829"},
            {"target": "new-york", "verb": "SERVES_AS_ACTING_GOVERNOR_OF", "note": "Acting Governor 1828"},
            {"target": "dewitt-clinton", "verb": "SERVES_UNDER", "note": "Lieutenant Governor under DeWitt Clinton"},
            {"target": "election-of-1828", "verb": "GOVERNS_DURING", "note": "Acting Governor during the Jackson-Adams contest"},
            {"target": "missouri-compromise", "verb": "SERVES_DURING", "note": "Congressman during the compromise debates"}
        ]
    }),

    ("thomas-fitzgerald-7th-earl-of-kildare", {
        "summary": (
            "Thomas FitzGerald, 7th Earl "
            "of Kildare (c.1426–1478) "
            "was an Anglo-Irish nobleman "
            "and the most powerful "
            "figure in 15th-century "
            "Ireland — the head "
            "of the FitzGerald dynasty "
            "that dominated the "
            "island as the 'Geraldines.' "
            "Known as the 'Great Earl,' "
            "Thomas FitzGerald was "
            "the father of Gearóid Mór "
            "(Gerald Mór FitzGerald, "
            "8th Earl), who became "
            "even more powerful — "
            "but Thomas himself "
            "established the Kildare "
            "earls' control over "
            "the Dublin administration "
            "and their supremacy "
            "over the other Anglo-Irish "
            "magnates and Gaelic "
            "Irish chiefs.\n\n"
            "The FitzGerald earls "
            "of Kildare in this "
            "period were effectively "
            "autonomous rulers "
            "of Ireland — operating "
            "within the nominal "
            "framework of English "
            "lordship but exercising "
            "real power that even "
            "the English crown "
            "found difficult to challenge.\n\n"
            "The Kildare supremacy "
            "he helped establish "
            "would continue under "
            "his son Gearóid Mór "
            "and grandson 'Silken Thomas' "
            "until the Kildare rebellion "
            "and the Tudor conquest.\n\n"
            "He was the founding "
            "figure of the Kildare supremacy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "7th Earl of Kildare (c.1426–1478); established the Kildare FitzGerald dynasty's dominance over Anglo-Irish administration; father of the 'Great Earl' Gearóid Mór; helped create the Kildare supremacy that made the earls effectively autonomous rulers of Ireland until the Tudor conquest; one of the founding figures of Ireland's most powerful medieval dynasty.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Wars of the Roses — the English dynastic conflict that diverted the English crown's attention from Ireland and created the power vacuum that enabled the FitzGerald earls to establish autonomous control over the Dublin administration",
            "The Kildare FitzGeralds' strategic position — their control of the Pale's eastern border, their alliances with both Gaelic Irish chiefs and Anglo-Irish magnates, and their military strength — gave them the practical power to dominate Ireland",
            "The weakness of direct English rule in Ireland — the Dublin administration's limited resources and the Crown's inability to project effective power into Ireland during the Wars of the Roses period — created the conditions in which the Kildare earls could become effectively autonomous"
        ],
        "effects": [
            "His establishment of Kildare supremacy created the dynastic foundations that his son Gearóid Mór would build into the most powerful Anglo-Irish position in history — the Kildare earls effectively ruling Ireland for nearly a century",
            "The Kildare dynasty he consolidated would eventually provoke the Tudor response — Henry VIII's determination to reassert direct English control in Ireland, leading to the Tudor conquest and the Reformation in Ireland",
            "His dynasty's power created the context for the Kildare rebellion under 'Silken Thomas' (1534–1535) — the FitzGerald challenge to Henry VIII that ended the Kildare supremacy and began the direct Tudor administration of Ireland",
            "His career illustrated the reality of 15th-century Anglo-Irish lordship — nominal English sovereignty combined with practical local autonomy that made the Pale's magnates effectively independent rulers"
        ],
        "relationships": [
            {"target": "earldom-of-kildare", "verb": "HOLDS", "note": "7th Earl of Kildare"},
            {"target": "gerald-mor-fitzgerald", "verb": "FATHER_OF", "note": "Father of the Great Earl, 8th Earl of Kildare"},
            {"target": "lordship-of-ireland", "verb": "DOMINATES", "note": "Effective ruler of Anglo-Irish administration"},
            {"target": "fitzgerald-dynasty", "verb": "LEADS", "note": "Head of the Geraldine dynasty"},
            {"target": "wars-of-the-roses", "verb": "BENEFITS_FROM", "note": "English civil war created Irish power vacuum"}
        ]
    }),

    ("william-upham", {
        "summary": (
            "William Upham (1792–1853) "
            "was an American Whig "
            "politician from Vermont "
            "who served in the U.S. "
            "Senate (1843–1853) — "
            "dying in office after "
            "a decade of Senate "
            "service. As a Vermont "
            "Whig senator, Upham "
            "represented one of "
            "the most reliably "
            "antislavery states "
            "in the Union during "
            "the antebellum slavery "
            "debates. His Senate "
            "career spanned the "
            "Tyler administration's "
            "chaos, the Polk presidency's "
            "Mexican-American War, "
            "the California gold rush, "
            "and the Compromise "
            "of 1850 — a decade "
            "of escalating sectional "
            "conflict over slavery "
            "extension.\n\n"
            "Vermont's antislavery "
            "tradition made its "
            "senators among the "
            "most consistent "
            "opponents of slavery "
            "extension in the Senate "
            "— Upham's votes reflected "
            "his state's deep "
            "commitment to the "
            "Free Soil principle.\n\n"
            "His decade in the "
            "Senate contributed "
            "Vermont's voice "
            "to the most "
            "consequential "
            "antebellum debates.\n\n"
            "He was previously "
            "a Vermont newspaper "
            "editor and lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont Whig Senator (1843–1853); died in office; represented Vermont's consistently antislavery Senate voice during the Mexican-American War, Wilmot Proviso debates, and Compromise of 1850; ten-year Senate career spanning the Tyler through Fillmore administrations; Vermont newspaper editor and lawyer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's antislavery political culture — the state's deep Protestant moral reform tradition and its early history as the first state to prohibit slavery in its constitution — created the political constituency that elected and sustained Upham's antislavery Senate career",
            "The Mexican-American War's territorial consequences — the massive new territories that the war added and the immediate question of whether they would be slave or free — created the defining controversy of Upham's Senate career",
            "The Whig Party's antislavery wing — the Conscience Whig faction that opposed slavery extension — provided the political identity within which Upham's Vermont Senate career was organized"
        ],
        "effects": [
            "His decade-long Senate service contributed Vermont's antislavery votes to the Wilmot Proviso debates, the Compromise of 1850 negotiations, and the other major slavery controversies of the era",
            "His consistent antislavery positioning contributed to Vermont's reputation as the most reliably antislavery state — a tradition that would help Vermont become one of the first and most solid Republican states after 1854",
            "His death in office in 1853 — just before the Kansas-Nebraska Act destroyed the compromise — prevented him from witnessing the catastrophic unraveling of the Compromise of 1850 that he had participated in debating",
            "His career contributed to the Whig Party's antislavery wing's strength — the Conscience Whig tradition that would feed directly into the Republican Party's founding coalition"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1843–1853"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig antislavery senator"},
            {"target": "compromise-of-1850", "verb": "VOTES_ON", "note": "Senator during the compromise debates"},
            {"target": "mexican-american-war", "verb": "SERVES_DURING", "note": "Senator during the war and territorial debates"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Vermont's antislavery Senate voice"}
        ]
    }),

    ("andré-marie-jean-jacques-dupin", {
        "summary": (
            "André-Marie-Jean-Jacques "
            "Dupin, called Dupin Aîné "
            "(1783–1865), was a French "
            "lawyer and politician "
            "who served as President "
            "of the French Chamber "
            "of Deputies (1832–1840) "
            "and as Procureur Général "
            "(Attorney General) "
            "of the Court of Cassation "
            "under three French "
            "regimes — making him "
            "one of the most "
            "durable figures in "
            "French political and "
            "legal life across "
            "the Restoration, "
            "the July Monarchy, "
            "the Second Republic, "
            "and the Second Empire. "
            "He was also a "
            "distinguished legal "
            "scholar whose writings "
            "on French constitutional "
            "and ecclesiastical "
            "law — especially "
            "his Gallican defense "
            "of the French Church's "
            "independence from Rome "
            "— were widely influential.\n\n"
            "As Chamber president "
            "under Louis-Philippe, "
            "Dupin presided over "
            "the July Monarchy's "
            "parliamentary debates "
            "during the full Orleanist "
            "constitutional experiment.\n\n"
            "His Gallicanism — "
            "the French Catholic "
            "tradition of Church "
            "independence from "
            "papal authority — "
            "made him a significant "
            "figure in the "
            "Church-state debates "
            "of 19th-century France.\n\n"
            "He survived five "
            "French regimes."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Chamber of Deputies President (1832–1840) under Louis-Philippe; Procureur Général of the Court of Cassation across multiple regimes; distinguished Gallican legal scholar defending French Church independence from Rome; survived five French political regimes (Restoration through Second Empire); pivotal figure in July Monarchy parliamentary life and 19th-century French jurisprudence.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The July Monarchy's constitutional culture — Louis-Philippe's bourgeois monarchy with its parliamentary constitution and the 'juste milieu' politics that Dupin exemplified — created the political framework for his long Chamber presidency",
            "The Gallican tradition in French Catholicism — the centuries-old tradition of French Church independence from Rome that informed Dupin's legal scholarship and political positions on Church-state relations",
            "French legal professionalism — the Paris bar's preeminent position in French public life and the tradition of lawyer-politicians who combined legal practice with parliamentary careers — created the institutional pathway for Dupin's combined legal and political prominence"
        ],
        "effects": [
            "His eight-year Chamber presidency contributed to the July Monarchy's parliamentary development — presiding over the Orleanist legislature during the full constitutional experiment that ended with the 1848 revolution",
            "His Gallican legal scholarship contributed to the French constitutional tradition — defending the French Church's independence from ultramontane papal authority in a way that shaped the Church-state debates of 19th-century France",
            "His survival through five regimes — from the Restoration through the Second Empire — illustrated his legal professionalism's political utility across ideological shifts",
            "His Court of Cassation service contributed to French jurisprudence — as France's highest court's chief prosecutor across multiple regimes, his legal arguments shaped the development of French national law"
        ],
        "relationships": [
            {"target": "chamber-of-deputies-france", "verb": "PRESIDES_OVER", "note": "President of the Chamber 1832–1840"},
            {"target": "court-of-cassation", "verb": "SERVES_AS_PROCUREUR_OF", "note": "Attorney General of France's highest court"},
            {"target": "july-monarchy", "verb": "SERVES_IN", "note": "Parliamentary president under Louis-Philippe"},
            {"target": "gallicanism", "verb": "DEFENDS", "note": "Gallican legal scholar defending French Church autonomy"},
            {"target": "louis-philippe-i", "verb": "SERVES_UNDER", "note": "Chamber president under the July Monarchy"}
        ]
    }),

    ("peter-early", {
        "summary": (
            "Peter Early (1773–1817) "
            "was an American Democratic-Republican "
            "politician from Georgia "
            "who served in the U.S. "
            "House of Representatives "
            "(1803–1807) and as Governor "
            "of Georgia (1813–1815) — "
            "dying young at age 44. "
            "His governorship coincided "
            "with the War of 1812's "
            "most dangerous year "
            "for the Southern frontier "
            "— the Creek War of "
            "1813–1814 in which "
            "the Red Stick Creek "
            "warriors allied with "
            "the British and attacked "
            "American settlements "
            "in the Mississippi Territory, "
            "creating a military "
            "crisis that affected "
            "Georgia's southern border "
            "and required state "
            "executive coordination.\n\n"
            "Early's county — "
            "Early County, Georgia "
            "— was named in his "
            "honor, a lasting "
            "geographical memorial "
            "to his service.\n\n"
            "His death at 44 "
            "cut short what "
            "might have been "
            "a longer political career.\n\n"
            "He was a Hancock "
            "County planter-lawyer "
            "who served Georgia "
            "in both Washington "
            "and Atlanta."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Georgia Democratic-Republican Congressman (1803–1807) and Governor (1813–1815); governed during the Creek War (1813–1814) that threatened Georgia's southern border; died at 44; Early County, Georgia named in his honor; served Georgia in both federal and state capacities during the War of 1812 era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's frontier position — the state's southern border with Spanish Florida and the Creek Nation created a security challenge that was amplified during the War of 1812 when the Red Stick Creeks allied with the British",
            "The Creek War — the Red Stick Creek warriors' attacks on American settlements in the Mississippi Territory in 1813–1814, part of the broader War of 1812 conflict — created the military emergency of Early's governorship",
            "Georgia's Democratic-Republican political dominance — the party's control of the state government and its organization of the planter elite — created the political structure within which Early's career developed"
        ],
        "effects": [
            "His governorship contributed to Georgia's defense during the Creek War — coordinating state resources and militia for the military crisis on the southern frontier",
            "Early County, Georgia named after him preserved his memory geographically — the county that still bears his name as a permanent memorial to his service",
            "His death at 44 removed a political figure at the height of his career — preventing him from participating in the post-war Era of Good Feelings that would have been the political context for a mature career",
            "His career contributed to Georgia's political tradition — the planter-lawyer politicians who served the state in both Washington and Georgia's own government"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Georgia Congressman 1803–1807"},
            {"target": "georgia", "verb": "GOVERNS", "note": "Governor of Georgia 1813–1815"},
            {"target": "creek-war", "verb": "GOVERNS_DURING", "note": "Governor during the Creek War crisis"},
            {"target": "war-of-1812", "verb": "GOVERNS_DURING", "note": "Governor during the War of 1812 southern theater"},
            {"target": "early-county-georgia", "verb": "MEMORIALIZED_IN", "note": "County named in his honor"}
        ]
    }),

    ("richard-spencer", {
        "summary": (
            "Richard Spencer (1796–1868) "
            "was an American Democratic "
            "politician from Maryland "
            "who served in the U.S. "
            "House of Representatives "
            "(1829–1833) during the "
            "early Jacksonian era. "
            "A Maryland Democrat, "
            "Spencer served during "
            "the Bank War's opening "
            "battles and the nullification "
            "crisis — the defining "
            "controversies of "
            "Jackson's first term. "
            "Maryland's political "
            "position as a border "
            "state with both "
            "commercial Baltimore "
            "interests and slaveholding "
            "Eastern Shore agricultural "
            "economy created a "
            "complex political "
            "environment that "
            "Maryland's congressional "
            "delegation navigated "
            "between Northern "
            "commercial interests "
            "and Southern agricultural "
            "and slavery concerns.\n\n"
            "His two-term House "
            "service represented "
            "the Jacksonian wave "
            "that swept Democratic "
            "candidates into Congress "
            "across the country "
            "after Jackson's "
            "1828 landslide.\n\n"
            "Maryland's competitive "
            "political tradition "
            "— unlike the solid "
            "one-party South — "
            "made its congressional "
            "seats genuinely contested.\n\n"
            "He was a Maryland "
            "lawyer and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Maryland Democratic Congressman (1829–1833); served during the Bank War and nullification crisis; represented Maryland's complex border-state position between commercial Baltimore and slaveholding Eastern Shore interests; two-term Jacksonian-era congressman in a genuinely competitive state.",
            "significanceCategory": "local"
        },
        "causes": [
            "Jackson's 1828 electoral landslide — the political revolution that swept Democratic candidates into congressional seats across the country and enabled Spencer's House service — created the political opportunity for his career",
            "Maryland's border state position — the state's economic and cultural position between North and South, combining Baltimore's commercial interests with the Eastern Shore's slave agriculture — created the complex political constituency Spencer represented",
            "The Bank War and nullification crisis — the defining controversies of Jackson's first term that dominated Spencer's congressional service — created the major policy questions he voted on"
        ],
        "effects": [
            "His House service contributed Maryland's Jacksonian Democratic votes to the Bank War's initial battles — supporting Jackson's economic war against the national bank",
            "His congressional votes contributed to the Jacksonian coalition's House majority during one of the most politically consequential periods",
            "His career illustrated Maryland's competitive politics — a border state where both Democrats and Whigs could win, unlike the solid South",
            "His two terms reflected the Jacksonian wave election pattern — many congressmen swept in on Jackson's coattails serving brief terms before the political tide shifted"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Congressman 1829–1833"},
            {"target": "bank-war", "verb": "VOTES_DURING", "note": "Congressman during Jackson's Bank War opening"},
            {"target": "nullification-crisis", "verb": "SERVES_DURING", "note": "Congressman during the South Carolina confrontation"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat congressman"},
            {"target": "maryland", "verb": "REPRESENTS", "note": "Maryland border-state Democratic congressman"}
        ]
    }),

    ("william-beach-lawrence", {
        "summary": (
            "William Beach Lawrence (1800–1881) "
            "was an American diplomat, "
            "legal scholar, and politician "
            "from New York who served "
            "as U.S. Chargé d'Affaires "
            "in London (1826–1828) "
            "and as Lieutenant Governor "
            "of Rhode Island (1851–1852). "
            "He is primarily known "
            "as a distinguished "
            "international law scholar "
            "— his annotated editions "
            "of Wheaton's 'Elements "
            "of International Law' "
            "were the authoritative "
            "American reference "
            "works on the subject "
            "for decades, and his "
            "dispute with Richard "
            "Henry Dana Jr. over "
            "the copyright of "
            "Wheaton's treatise "
            "produced a landmark "
            "American copyright case.\n\n"
            "The Lawrence v. Dana "
            "copyright case (1869) "
            "established important "
            "precedents in American "
            "intellectual property law.\n\n"
            "His Chargé d'Affaires "
            "role in London placed "
            "him in British diplomatic "
            "circles during the "
            "critical period of "
            "Anglo-American relations "
            "in the late 1820s.\n\n"
            "He was a New York "
            "lawyer and legal "
            "scholar of international standing."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Chargé d'Affaires in London (1826–1828), Rhode Island Lieutenant Governor (1851–1852), and preeminent American international law scholar; annotated Wheaton's 'Elements of International Law'; Lawrence v. Dana copyright case (1869) established intellectual property precedents; diplomat, jurist, and legal scholar of international standing.",
            "significanceCategory": "continental"
        },
        "causes": [
            "American international law's development — the early Republic's need to establish its standing in international legal relations and to produce authoritative American commentary on the law of nations — created the demand for the international law scholarship that Lawrence supplied",
            "Wheaton's international law — Henry Wheaton's authoritative 1836 'Elements of International Law' created the canonical American text that Lawrence's annotations and editions built upon and extended",
            "The copyright dispute — Dana's competing edition of Wheaton's treatise and the question of whether Lawrence's annotations could be protected by copyright — created the legal controversy that produced the landmark Lawrence v. Dana case"
        ],
        "effects": [
            "His annotated Wheaton editions contributed to the development of American international law — providing the authoritative reference works that American diplomats, lawyers, and courts used for the law of nations",
            "The Lawrence v. Dana copyright case contributed to American intellectual property law — establishing precedents about the copyrightability of legal annotations and editorial contributions",
            "His London diplomatic service contributed to Anglo-American relations — representing American interests in Britain during the crucial period of post-War of 1812 normalization",
            "His career illustrated the emerging American tradition of diplomat-scholar — combining government service with serious legal scholarship in a way that strengthened both American diplomacy and American law"
        ],
        "relationships": [
            {"target": "us-chargé-daffaires-london", "verb": "SERVES_AS", "note": "U.S. Chargé d'Affaires in London 1826–1828"},
            {"target": "rhode-island", "verb": "SERVES_AS_LIEUTENANT_GOVERNOR_OF", "note": "Rhode Island Lt. Governor 1851–1852"},
            {"target": "elements-of-international-law", "verb": "ANNOTATES", "note": "Authoritative annotated editions of Wheaton's treatise"},
            {"target": "lawrence-v-dana", "verb": "PARTICIPANT_IN", "note": "Landmark copyright case over Wheaton annotations"},
            {"target": "american-international-law", "verb": "DEVELOPS", "note": "Preeminent American international law scholar"}
        ]
    }),

    ("antoine-loysel", {
        "summary": (
            "Antoine Loysel (1536–1617) "
            "was a French jurist "
            "and legal scholar of "
            "the 16th and early "
            "17th centuries who "
            "is best known for "
            "his 'Institutes coutumières' "
            "(1607) — a celebrated "
            "collection of maxims "
            "summarizing French "
            "customary law in "
            "memorable, pithy "
            "phrases that became "
            "one of the most "
            "cited legal texts "
            "in French jurisprudence. "
            "He was a student "
            "of the great humanist "
            "legal scholars Cujas "
            "and Hotman — "
            "the founders of "
            "the mos gallicus "
            "tradition that "
            "treated Roman law "
            "historically — and "
            "he applied their "
            "humanist methods "
            "to French customary "
            "law.\n\n"
            "The 'Institutes "
            "coutumières' was "
            "unusual in being "
            "written in French "
            "rather than Latin "
            "— making French "
            "law accessible "
            "to practicing "
            "lawyers and judges "
            "rather than just "
            "academic scholars.\n\n"
            "His aphoristic "
            "summaries of "
            "French legal principles "
            "were still being "
            "cited centuries "
            "later.\n\n"
            "He was a distinguished "
            "member of the "
            "Paris bar and "
            "a royal advocate-general."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French jurist and author of the 'Institutes coutumières' (1607) — a celebrated collection of French customary law maxims; student of humanist legal scholars Cujas and Hotman; wrote in French rather than Latin to make law accessible; his aphorisms were cited for centuries; member of the Paris bar and royal advocate-general; significant figure in the development of French national law.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French humanist legal revolution — the mos gallicus tradition of Cujas and Hotman that treated Roman law historically and applied humanist methods to legal scholarship — created the intellectual background from which Loysel's approach to French customary law developed",
            "The French legal vernacularization movement — the shift from Latin to French in legal documents and scholarship following the Ordinance of Villers-Cotterêts (1539) that required official documents in French — created the linguistic context for Loysel's French-language 'Institutes coutumières'",
            "French customary law's complexity — the dozens of regional customs that governed different parts of France, requiring codification and synthesis — created the practical demand for the kind of accessible legal summary that Loysel supplied"
        ],
        "effects": [
            "His 'Institutes coutumières' contributed a canonical reference to French legal scholarship — the aphoristic summaries of French customary law that were cited by judges and lawyers for centuries",
            "His French-language legal writing contributed to the democratization of French legal knowledge — making legal principles accessible beyond Latin-trained scholars to the broader legal profession",
            "His humanist method applied to French customary law contributed to the long-term project of French legal unification — the synthesis that eventually led to the Napoleonic Code's codification of French law",
            "His student relationship with Cujas and Hotman contributed to the transmission of humanist legal scholarship across generations — carrying the founders' methods into the late 16th and early 17th-century legal practice"
        ],
        "relationships": [
            {"target": "french-customary-law", "verb": "CODIFIES", "note": "Author of the authoritative 'Institutes coutumières'"},
            {"target": "jacques-cujas", "verb": "STUDIES_UNDER", "note": "Student of the humanist legal scholar"},
            {"target": "francois-hotman", "verb": "STUDIES_UNDER", "note": "Student of the Huguenot legal humanist"},
            {"target": "paris-bar", "verb": "PRACTICES_IN", "note": "Distinguished Paris advocate and royal advocate-general"},
            {"target": "french-jurisprudence", "verb": "CONTRIBUTES_TO", "note": "Canonical legal scholar of French customary law"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 80 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
