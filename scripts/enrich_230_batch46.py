#!/usr/bin/env python3
"""
Batch 46 — 8 entities: Meshech Weare, Hubert de Burgh 1st Earl of Kent,
José Ignacio de Márquez, Josiah Quincy III, Frederick Bates,
Samuel Lewis Southard, Joseph Anderson, James Turner Morehead
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

    # 1 — Meshech Weare
    ("meshech-weare", {
        "summary": (
            "Meshech Weare (1713–1786) was a New Hampshire "
            "farmer, lawyer, and statesman who served as "
            "the first President (Governor) of the State "
            "of New Hampshire from 1776 to 1785 — guiding "
            "the state through the entire Revolutionary "
            "War period and becoming known as the 'Father "
            "of New Hampshire.' As Chairman of the New "
            "Hampshire Committee of Safety — the executive "
            "body that governed the state during the "
            "emergency period when the legislature was "
            "not in session — he managed the state's war "
            "effort, directed troop mobilization, oversaw "
            "finances, and coordinated with Continental "
            "Army commanders.\n\n"
            "Born in Hampton Falls, he was educated at "
            "Harvard, read law, and built a local career "
            "as a justice of the peace, judge, and "
            "colonial legislator before the Revolution. "
            "His modest personal character, legal "
            "experience, and credibility with both "
            "radical and moderate revolutionary factions "
            "made him New Hampshire's consensus "
            "choice for executive leadership when "
            "the colonial governor was removed.\n\n"
            "New Hampshire's 1776 constitution — one "
            "of the first state constitutions adopted "
            "after independence — used the title "
            "'President' rather than 'Governor' for "
            "the state's chief executive, a terminological "
            "choice that persisted until the 1784 "
            "constitution. Weare filled this office "
            "with quiet effectiveness, subordinating "
            "personal ambition to the demands of "
            "wartime emergency governance.\n\n"
            "'He loved his country too well to make "
            "himself indispensable to it' — a tribute "
            "that captured the self-effacing competence "
            "of one of the Revolution's most reliable "
            "state-level administrators."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First President/Governor of New Hampshire (1776–1785); Chairman of the New Hampshire Committee of Safety throughout the Revolutionary War; 'Father of New Hampshire'; Harvard-educated lawyer; managed NH's entire war effort and transition to independent statehood; his nine-year presidency spanning the complete Revolutionary period made him the most important figure in NH's founding era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution's dismantling of colonial governance — which removed the royal governor and created the need for a new state executive — created the position that Weare filled as New Hampshire's first post-colonial chief executive, with his prior credibility as a colonial lawyer and judge making him the consensus choice for the emergency leadership role",
            "New Hampshire's 1776 constitution — one of the earliest state constitutions adopted following independence — established the 'President' executive role (rather than 'Governor') and the Committee of Safety as the state's primary emergency governing body, creating the institutional framework within which Weare exercised his decade of leadership",
            "The Revolutionary War's severe demands on state governments — requiring coordination of troop mobilization, wartime finances, supply procurement, and inter-colonial cooperation — created the administrative challenges that Weare navigated as Committee of Safety chair, making his steady and reliable leadership essential to New Hampshire's war effort"
        ],
        "effects": [
            "His nine-year presidency (1776–1785) provided New Hampshire with exceptional executive continuity through the entire Revolutionary War period — steering the state from colonial status through independence, wartime emergency governance, and the early republican period, a record of sustained leadership that earned him the 'Father of New Hampshire' title",
            "His management of the New Hampshire Committee of Safety contributed to the state's effective mobilization of troops, resources, and supplies for the Continental Army — one of the quieter but essential dimensions of the Revolution's success, as state-level administrative competence determined whether the Continental cause received the manpower and material it required",
            "His chairmanship during the constitutional transition period contributed to New Hampshire's institutional development — presiding over the state's adoption of its 1776 and 1784 constitutions and the implementation of post-colonial governmental structures that would govern the state for decades",
            "His self-effacing leadership style contributed to the republican constitutional culture of the founding era — embodying the ideal of civic virtue that placed public service above personal ambition, providing a model of disinterested administration that contrasted with the more self-promoting politicians of the period"
        ],
        "relationships": [
            {"entity": "First President of New Hampshire (1776–1785, under 1776 and 1784 constitutions)", "relationship": "FIRST_PRESIDENT_GOVERNOR", "note": "Served as New Hampshire's first chief executive (1776–1785) — guiding the state through the entire Revolutionary War period and earning the title 'Father of New Hampshire'"},
            {"entity": "New Hampshire Committee of Safety (Revolutionary War emergency governing body, chair)", "relationship": "CHAIRMAN_OF", "note": "Served as Chairman of New Hampshire's Committee of Safety — the emergency executive body that governed the state when the legislature was not in session, managing all dimensions of the wartime state government"},
            {"entity": "New Hampshire 1776 Constitution (first state constitution, 'President' title)", "relationship": "FIRST_HOLDER_OF_EXECUTIVE_OFFICE_UNDER", "note": "First holder of the executive office created by New Hampshire's 1776 constitution — one of the earliest state constitutions adopted after independence, which used 'President' rather than 'Governor' for the chief executive"},
            {"entity": "American Revolutionary War / Continental Army (New Hampshire troops)", "relationship": "MANAGED_NH_CONTRIBUTION_TO", "note": "Managed New Hampshire's military contribution to the Revolutionary War — coordinating troop mobilization, supply, and finances as Committee of Safety chairman"},
            {"entity": "New Hampshire founding era (1776–1785, constitutional development)", "relationship": "CENTRAL_FIGURE_OF", "note": "The central figure of New Hampshire's founding era — his decade of leadership presiding over the state's transition from colonial to independent republican governance earning him the 'Father of New Hampshire' designation"}
        ]
    }),

    # 2 — Hubert de Burgh, 1st Earl of Kent
    ("hubert-de-burgh-1st-earl-of-kent", {
        "summary": (
            "Hubert de Burgh, 1st Earl of Kent "
            "(c. 1170–1243) was an English nobleman "
            "and royal official who served as Chief "
            "Justiciar of England (1215–1232) and "
            "as the effective Regent of England "
            "(1219–1227) during the minority of "
            "King Henry III — making him one of "
            "the most powerful figures in 13th-century "
            "English government. He served under "
            "both King John and his son Henry III, "
            "navigating the turbulent years of "
            "Magna Carta, the First Barons' War, "
            "and the French invasion led by "
            "Prince Louis of France.\n\n"
            "His most celebrated military achievement "
            "was the defense of Dover Castle (1216) "
            "against the French forces supporting "
            "the baronial rebellion — holding the "
            "'key to England' through a sustained "
            "siege at the moment when the kingdom "
            "seemed on the verge of conquest. "
            "He followed this with a decisive "
            "naval victory at the Battle of "
            "Sandwich (1217) — defeating the "
            "French supply fleet and effectively "
            "ending the French invasion.\n\n"
            "As Regent during Henry III's minority, "
            "he was the de facto ruler of England — "
            "managing foreign policy, the barons, "
            "and the ongoing tensions over the "
            "Magna Carta settlement. He accumulated "
            "vast wealth and influence but was "
            "ultimately overthrown in 1232 when "
            "Henry III came to personal rule, "
            "stripped of his offices, and "
            "twice imprisoned.\n\n"
            "His career traced the classic arc of "
            "the medieval royal servant elevated "
            "beyond his birth to the height of "
            "power — and then cast down when "
            "royal favor withdrew. 'He deserves "
            "the gratitude of every Englishman,' "
            "wrote Roger of Wendover, 'for "
            "saving the kingdom by his valor.'"
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Chief Justiciar of England (1215–1232); Regent during Henry III's minority (1219–1227); defended Dover Castle (1216) against French invasion; naval victory at Battle of Sandwich (1217) ending French conquest attempt; one of the most powerful figures in 13th-century English government; his fall from power in 1232 was one of medieval England's most dramatic political reversals.",
            "significanceCategory": "regional"
        },
        "causes": [
            "King John's political failures — his loss of Normandy (1204), the Interdict crisis with the papacy, and the baronial revolt that led to Magna Carta (1215) — created the political turmoil that elevated Hubert de Burgh from capable royal servant to the most important figure in English government, as his defense of Dover became critical to the Crown's survival",
            "Henry III's accession as a nine-year-old king in 1216 — in the midst of the French invasion and baronial civil war — created the regency vacuum that Hubert de Burgh filled as the adult official capable of managing both the military emergency and the political settlement that would end the First Barons' War",
            "The institutional role of the Chief Justiciar — the medieval English equivalent of a prime minister, responsible for judicial, financial, and administrative functions — gave Hubert de Burgh a governmental power base that elevated his personal authority and concentrated English royal power in his hands during the regency period"
        ],
        "effects": [
            "His defense of Dover Castle and naval victory at Sandwich (1217) contributed to preventing the French conquest of England — ending Prince Louis's invasion and preserving the Plantagenet dynasty on the English throne, which his contemporary Roger of Wendover credited as saving the kingdom",
            "His regency (1219–1227) contributed to the consolidation of Henry III's government during the minority — managing the baronial tensions, the papacy's claims, and the ongoing Magna Carta disputes that had disrupted England's governance since 1215",
            "His fall from power in 1232 contributed to the political history of medieval royal service — illustrating the precariousness of power held entirely at royal favor, as Henry III stripped him of offices and imprisoned him once he chose to rule personally, making de Burgh's fall one of medieval England's most dramatic reversals of fortune",
            "His Chief Justiciarship contributed to the institutional development of English royal government — as one of the last great Chief Justiciars before the office was divided among multiple officeholders, his career marked the end of the medieval system in which a single official could exercise quasi-regal power"
        ],
        "relationships": [
            {"entity": "Chief Justiciar of England (1215–1232) / de facto regent (1219–1227)", "relationship": "CHIEF_JUSTICIAR_AND_REGENT", "note": "Served as Chief Justiciar (1215–1232) and de facto regent (1219–1227) during Henry III's minority — the most powerful figure in English government and effectively its prime minister"},
            {"entity": "Defense of Dover Castle (1216) / Battle of Sandwich (1217)", "relationship": "DEFENDER_AND_VICTOR_AT", "note": "Defended Dover Castle (1216) against the French invasion and defeated the French supply fleet at the Battle of Sandwich (1217) — the military achievements that prevented the French conquest of England"},
            {"entity": "Henry III of England (minority, 1216–1227; personal rule, 1227–1272)", "relationship": "REGENT_THEN_DISMISSED_BY", "note": "Served as regent during Henry III's minority (1219–1227) then was dismissed, stripped of offices, and imprisoned when Henry III began personal rule in 1232 — a classic arc of elevation and fall by royal favor"},
            {"entity": "First Barons' War (1215–1217) / French invasion of England", "relationship": "DECISIVE_DEFENDER_AGAINST", "note": "Played the decisive military role in ending both the French invasion and the First Barons' War — his defense of Dover and victory at Sandwich turning the military situation and enabling the peace settlement"},
            {"entity": "Magna Carta settlement / 13th-century English constitutional development", "relationship": "ADMINISTRATOR_OF_IN_REGENCY_PERIOD", "note": "Administered the Magna Carta settlement during the regency period — managing the baronial tensions and royal-barons relationship that shaped England's constitutional development in the years after Runnymede"}
        ]
    }),

    # 3 — José Ignacio de Márquez
    ("josé-ignacio-de-márquez", {
        "summary": (
            "José Ignacio de Márquez Barreto (1793–1880) "
            "was a Colombian lawyer, professor, and "
            "statesman who served as Vice President "
            "(1832–1833) and President of the Republic "
            "of New Granada (1837–1841) — governing "
            "Colombia during one of the most violent "
            "episodes of its early independent history: "
            "the War of the Supremes (1839–1842), "
            "a federalist-liberal uprising against "
            "his centralizing conservative government. "
            "Born in Ramiriquí, Boyacá, he was a "
            "distinguished professor and Rector of "
            "the Colegio de San Bartolomé in Bogotá "
            "before entering national politics.\n\n"
            "His presidency came after the creation "
            "of the Republic of New Granada — the "
            "successor state to Gran Colombia after "
            "Bolívar's unification project dissolved "
            "in 1830. He served under Francisco de "
            "Paula Santander as Vice President, then "
            "succeeded him as president through "
            "election, representing the Conservative-"
            "oriented 'ministerial' faction that "
            "favored centralized government and "
            "strong institutional order over the "
            "liberals' federalist demands.\n\n"
            "The War of the Supremes — which broke "
            "out in 1839 partly over his government's "
            "suppression of small convents in Pasto "
            "— became a general revolt of liberal "
            "regional commanders ('the Supremes') "
            "against his administration. Despite "
            "the rebellion's severity, Márquez's "
            "government survived, but the war "
            "left the country deeply fractured "
            "and contributed to the polarization "
            "between liberal federalists and "
            "conservative centralists that would "
            "define Colombian politics for decades.\n\n"
            "As both a distinguished academic and "
            "the president who governed during "
            "New Granada's most severe early "
            "civil conflict, Márquez occupied "
            "a central position in Colombia's "
            "troubled post-independence consolidation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President of the Republic of New Granada (1837–1841); Vice President under Santander (1832–1833); presided over the War of the Supremes (1839–1842) — Colombia's most severe early civil conflict; professor and Rector of Colegio de San Bartolomé; conservative centralist in the defining liberal-conservative conflict of Colombian politics; his presidency's survival of the war shaped New Granada's institutional development.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The dissolution of Gran Colombia in 1830 — Bolívar's failed unification project — and the formation of the Republic of New Granada as an independent state created the political framework within which Márquez's presidency operated, with the new republic's institutional instability and the unresolved tensions between centralists and federalists providing the conditions for the War of the Supremes",
            "The conflict between Colombian Conservative-centralist and Liberal-federalist factions over the structure of the new republic's government — whether Colombia should be governed by a strong central authority in Bogotá or by autonomous regional authorities — created the political polarization that made Márquez's government a target for liberal regional revolt",
            "The specific trigger of the War of the Supremes — his government's order closing small convents in Pasto in 1839, which provoked religious conservative opposition in the south — combined with broader liberal grievances against his centralist administration to produce the multi-regional revolt that tested the new republic's institutional resilience"
        ],
        "effects": [
            "His presidency's survival of the War of the Supremes contributed to the survival of the centralizing New Granadan constitutional framework — defeating the federalist revolt, though at the cost of deep polarization between liberal and conservative factions that would define Colombian political conflict for decades",
            "The War of the Supremes that his administration triggered and survived contributed to the hardening of the liberal-conservative divide in Colombian politics — contributing to the political framework that would produce multiple subsequent civil wars throughout the 19th century",
            "His academic career as professor and Rector of the Colegio de San Bartolomé contributed to the formation of the Colombian intellectual and professional class — the educational institution that trained lawyers, politicians, and public servants who built the new republic's institutions",
            "His vice-presidential service under Santander contributed to the constitutional consolidation of the Republic of New Granada — the two-year period in which the new state's institutions were being built and the Bolivarian unification project was finally being set aside"
        ],
        "relationships": [
            {"entity": "President of the Republic of New Granada (1837–1841)", "relationship": "PRESIDENT", "note": "Served as President of New Granada (1837–1841) — governing Colombia during the War of the Supremes (1839–1842), the country's most severe early civil conflict, which his centralizing policies had helped trigger"},
            {"entity": "War of the Supremes (1839–1842, liberal-federalist revolt against Márquez government)", "relationship": "PRESIDENT_DURING_AND_SURVIVED", "note": "Presided over and survived the War of the Supremes (1839–1842) — a multi-regional liberal revolt against his conservative-centralist administration that left Colombia deeply fractured"},
            {"entity": "Francisco de Paula Santander (predecessor president, Márquez served as VP)", "relationship": "VICE_PRESIDENT_UNDER_THEN_SUCCESSOR_OF", "note": "Served as Vice President under Santander (1832–1833) then succeeded him as president — the transition from Santander's Liberal leadership to Márquez's Conservative orientation"},
            {"entity": "Republic of New Granada (successor to Gran Colombia, 1830–1858)", "relationship": "PRESIDENT_AND_BUILDER_OF_INSTITUTIONS_OF", "note": "Served as Vice President and President during the critical early years of New Granada — the successor state to Bolívar's Gran Colombia, whose institutional consolidation Márquez's conservative government sought to achieve"},
            {"entity": "Colegio de San Bartolomé, Bogotá (professor and Rector)", "relationship": "PROFESSOR_AND_RECTOR_OF", "note": "Served as professor and Rector of the Colegio de San Bartolomé — Colombia's most prestigious educational institution, which trained the republic's professional class"}
        ]
    }),

    # 4 — Josiah Quincy III
    ("josiah-quincy-iii", {
        "summary": (
            "Josiah Quincy III (1772–1864) was a Massachusetts "
            "lawyer, politician, and educational administrator "
            "whose 65-year public career spanned from "
            "Federalist congressman to Mayor of Boston "
            "to President of Harvard — making him one "
            "of the longest-serving and most multi-faceted "
            "public figures of the early American republic. "
            "He served in the US House of Representatives "
            "(1805–1813) as a leading Federalist voice, "
            "as Mayor of Boston (1823–1828) where he "
            "transformed the city's public health and "
            "infrastructure, and as President of Harvard "
            "University (1829–1845) where he modernized "
            "the institution.\n\n"
            "His congressional career made him one of "
            "the most vocal opponents of the War of 1812 "
            "— his 1811 speech suggesting that New "
            "England would feel justified in secession "
            "if Louisiana was admitted as a state "
            "was one of the most controversial "
            "statements in early congressional history. "
            "He remained an unapologetic Federalist "
            "throughout the era's political shifts.\n\n"
            "His mayoral career was transformative: "
            "he built the Quincy Market complex (1826), "
            "reorganized Boston's public schools, "
            "established a night watch, and improved "
            "the city's sewage and water systems — "
            "a panel of 69 historians in 1993 "
            "ranked him among the ten best mayors "
            "in American history. As Harvard's "
            "president, he built academic "
            "departments, added a law school, "
            "and modernized governance.\n\n"
            "His longevity — he died at 92 — "
            "gave him a career arc connecting "
            "the revolutionary generation to "
            "the Civil War era, and his History "
            "of Harvard University (1840) "
            "provided the institution's "
            "definitive early account."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Massachusetts Federalist US Congressman (1805–1813); Mayor of Boston (1823–1828); President of Harvard University (1829–1845); builder of Quincy Market (1826); ranked among the ten best mayors in American history by historians; vocal War of 1812 opponent; 92-year career spanning Federalist era to Civil War; his 65-year public career made him one of the early republic's most impactful multi-role public figures.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Federalist political tradition in Massachusetts — rooted in Harvard, Boston's commercial class, and New England's cultural conservatism — created the political identity that shaped Quincy's congressional career as one of the most vocal Federalist critics of Jeffersonian-Republican policies, including the Louisiana Purchase and the War of 1812",
            "Boston's rapid growth in the early 19th century — expanding population, inadequate infrastructure, public health crises, and the need for systematic urban governance — created the demand for transformative mayoral leadership that Quincy provided through the Quincy Market, public school reform, and infrastructure improvements",
            "Harvard's institutional challenges in the early 19th century — outdated governance, inadequate facilities, and the need for academic modernization to match the university's aspirations as the nation's leading educational institution — created the demand for an energetic reforming president that Quincy's sixteen-year tenure provided"
        ],
        "effects": [
            "His Quincy Market complex (1826) transformed downtown Boston's commercial district — creating an enduring urban landmark that remained in use through the 20th century and was renovated as the famous Faneuil Hall Marketplace in 1976, extending Quincy's urban legacy nearly 200 years after its construction",
            "His mayoral governance reforms contributed to the transformation of Boston's urban infrastructure — his public school reorganization, night watch establishment, and public health improvements helping Boston manage the challenges of early 19th-century urban growth and setting administrative precedents for American city government",
            "His 16-year Harvard presidency contributed to the modernization of American higher education's leading institution — building departments, adding professional schools, and improving governance in ways that positioned Harvard for its 19th-century growth into one of the world's great research universities",
            "His congressional opposition to the War of 1812 contributed to the political debate over the war's legitimacy — his secession suggestion (controversial enough to nearly result in a censure vote) becoming one of the most extreme expressions of New England Federalist dissent against Jeffersonian foreign policy"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Massachusetts (Federalist, 1805–1813)", "relationship": "CONGRESSMAN", "note": "Served as a leading Federalist US Representative (1805–1813) — one of the most vocal opponents of Jeffersonian policy including the War of 1812, whose secession comments made him one of the era's most controversial congressional voices"},
            {"entity": "Mayor of Boston (1823–1828) / Quincy Market (built 1826)", "relationship": "MAYOR_AND_BUILDER_OF", "note": "Served as Mayor of Boston (1823–1828) and built the Quincy Market complex (1826) — his transformative administration ranked among the ten best in American mayoral history by historians"},
            {"entity": "Harvard University (President, 1829–1845, 16-year tenure)", "relationship": "PRESIDENT_OF", "note": "Served as Harvard's president for 16 years (1829–1845) — modernizing the institution, building departments and professional schools, and positioning it for its 19th-century growth"},
            {"entity": "War of 1812 / Federalist opposition to Jeffersonian foreign policy", "relationship": "LEADING_OPPONENT_OF", "note": "One of the most vocal congressional opponents of the War of 1812 — whose 1811 secession suggestion became one of the most controversial statements in early congressional history"},
            {"entity": "Federalist Party / New England Federalist tradition", "relationship": "LEADING_REPRESENTATIVE_OF", "note": "One of Massachusetts Federalism's most prominent voices — an unapologetic Federalist throughout the era's political shifts, representing the New England commercial and intellectual elite's political tradition"}
        ]
    }),

    # 5 — Frederick Bates
    ("frederick-bates", {
        "summary": (
            "Frederick Bates (1777–1825) was a Virginia-born "
            "lawyer and government administrator who served "
            "as Secretary of the Louisiana Territory (1807–1812) "
            "under Thomas Jefferson's appointment, as a "
            "justice of the Michigan Territory Supreme "
            "Court, and finally as the second elected "
            "Governor of Missouri (1824) — dying in office "
            "in 1825, less than a year into his term. "
            "His career traced the expansion of American "
            "territorial governance in the early republic's "
            "western territories.\n\n"
            "His most significant posting was as Secretary "
            "of Louisiana Territory — the administrative "
            "number-two to the territorial governor — where "
            "he became embroiled in a notorious personal "
            "conflict with Meriwether Lewis, the "
            "Lewis-and-Clark expedition leader who "
            "served briefly as Louisiana's governor (1808–1809). "
            "Bates and Lewis clashed repeatedly over "
            "administrative authority and policy, with "
            "Bates sending critical reports to Washington "
            "that undermined Lewis's gubernatorial standing "
            "— a feud that some historians believe "
            "contributed to Lewis's severe depression "
            "and death in 1809.\n\n"
            "His subsequent career included a second "
            "stint as territorial secretary and his "
            "election as Missouri's second governor "
            "in 1824 — following Missouri's admission "
            "to statehood in 1821. His death in office "
            "only eleven months after his election "
            "cut short a political career that might "
            "have extended further.\n\n"
            "His conflict with Meriwether Lewis "
            "ensured that his name would be "
            "permanently associated with one of "
            "the most dramatic and tragic episodes "
            "in the history of the American frontier."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Secretary of Louisiana Territory (1807–1812, Jefferson appointee); Michigan Territory Supreme Court justice; second Governor of Missouri (1824, died in office 1825); his notorious conflict with Meriwether Lewis — whose depression and death he may have contributed to — made him a significant figure in the history of the early American frontier; his career traced early US territorial administration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Thomas Jefferson's Louisiana Purchase (1803) and the need to establish American governance over the newly acquired western territory — creating the Secretaryship of Louisiana Territory that Bates was appointed to fill, drawing him from Virginia into the heart of the early American territorial expansion system",
            "The inherent tensions of the American territorial governance system — in which the Secretary (a civilian administrator appointed by the President) and the Governor (often a military figure or political appointee) might have different visions of policy and different relationships with Washington — created the structural conditions for the conflict between Bates and Meriwether Lewis",
            "Missouri's admission to statehood (1821) — creating a new elected governorship in the region where Bates had spent his administrative career — provided the political opportunity for his election as the state's second governor, translating his territorial administrative experience into electoral success"
        ],
        "effects": [
            "His conflict with Meriwether Lewis contributed to one of the most studied and debated deaths in American frontier history — as Bates's critical reports to Washington, which undermined Lewis's gubernatorial standing, are among the factors historians have examined in analyzing Lewis's severe depression and apparent suicide at Grinder's Stand in 1809",
            "His Missouri governorship — though cut short by his death in office — contributed to the state's institutional development in its early years following admission to statehood, as Missouri navigated the political challenges of a slave state's governance in the antebellum republic",
            "His career as Secretary of Louisiana Territory contributed to the early American territorial governance system — building the administrative infrastructure of the vast Louisiana Purchase territory and demonstrating both the system's effectiveness and its vulnerability to inter-official conflict",
            "His death in office contributed to the institutional challenge of gubernatorial succession in a new state — raising questions about Missouri's succession mechanisms and executive continuity that were resolved through constitutional provisions"
        ],
        "relationships": [
            {"entity": "Second Governor of Missouri (1824, died in office 1825)", "relationship": "SECOND_GOVERNOR_DIED_IN_OFFICE", "note": "Elected as Missouri's second governor in 1824 — following the state's 1821 admission — and died in office in 1825, less than a year into his term"},
            {"entity": "Secretary of Louisiana Territory (1807–1812, Jefferson appointee)", "relationship": "TERRITORIAL_SECRETARY", "note": "Served as Secretary of Louisiana Territory (1807–1812) under Jefferson's appointment — the number-two administrator in the vast territory acquired through the Louisiana Purchase"},
            {"entity": "Meriwether Lewis (Louisiana Territory Governor, 1808–1809, conflict with Bates)", "relationship": "CONFLICTED_WITH_UNDERMINED", "note": "Had a notorious personal and administrative conflict with Meriwether Lewis — sending critical reports to Washington that undermined Lewis's gubernatorial standing and may have contributed to Lewis's depression and death in 1809"},
            {"entity": "Louisiana Purchase (1803) / US territorial expansion in the early republic", "relationship": "ADMINISTRATOR_OF_TERRITORY_CREATED_BY", "note": "Built his career as an administrator of the territory created by Jefferson's Louisiana Purchase — one of the government officials who actually implemented US governance over the newly acquired western lands"},
            {"entity": "Michigan Territory Supreme Court (justice) / early US territorial judiciary", "relationship": "JUSTICE_OF", "note": "Served as a justice of the Michigan Territory Supreme Court — one of several territorial judicial appointments that built his experience in American frontier governance"}
        ]
    }),

    # 6 — Samuel Lewis Southard
    ("samuel-lewis-southard", {
        "summary": (
            "Samuel Lewis Southard (1787–1842) was a New "
            "Jersey lawyer and statesman who served as "
            "a US Senator from New Jersey (1821–1823, "
            "1833–1842), as Secretary of the Navy "
            "(1823–1829) under Presidents Monroe and "
            "Adams, as the 10th Governor of New Jersey "
            "(1832–1833), and as President pro tempore "
            "of the Senate (1841–1842) — making him "
            "one of the most versatile multi-role public "
            "figures of the Era of Good Feelings and "
            "the early Whig period.\n\n"
            "His Navy secretaryship was his most "
            "consequential federal role: serving six "
            "years across two administrations during "
            "the Navy's critical post-War of 1812 "
            "development period, he oversaw naval "
            "expansion, shore establishment construction, "
            "and the Navy's institutional modernization. "
            "He also served briefly as Acting Secretary "
            "of War, Treasury, and State during various "
            "cabinet vacancies.\n\n"
            "One of the more unusual distinctions "
            "of his career came from constitutional "
            "circumstance: when both the vice presidency "
            "and the speakership of the House were "
            "simultaneously vacant, his position as "
            "Senate President pro tempore made him "
            "briefly first in the presidential line "
            "of succession — a constitutional edge "
            "case that would have been significant "
            "if President Tyler had died during "
            "that period.\n\n"
            "As a Whig Party stalwart in the Senate "
            "during the early 1840s, he served "
            "alongside Henry Clay, Daniel Webster, "
            "and other Whig leaders who opposed "
            "President Tyler's vetoes — contributing "
            "to the Senate debates that shaped "
            "Whig political strategy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator from New Jersey (1821–1823, 1833–1842); Secretary of the Navy (1823–1829, under Monroe and Adams); 10th Governor of New Jersey (1832–1833); Senate President pro tempore (1841–1842); briefly first in presidential succession when VP and Speaker simultaneously vacant; versatile Era of Good Feelings and early Whig statesman across legislative, executive, and gubernatorial roles.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Era of Good Feelings' political culture — in which the collapse of Federalism and the one-party dominance of the Democratic-Republicans created fluid political competition among faction leaders rather than party discipline — created the environment in which versatile multi-role figures like Southard could hold a succession of appointments across cabinet, Senate, and gubernatorial positions",
            "The post-War of 1812 Navy Department's expansion and institutionalization — as the United States sought to build a professional naval establishment capable of defending its growing commercial and maritime interests — created the demand for a sustained and capable Navy Secretary, which Southard filled across Monroe's and Adams's administrations",
            "New Jersey's Whig political culture and the state's role as a competitive battleground between Whigs and Democrats — requiring prominent figures to hold both federal and state offices — created the multi-role political career in which Southard served as senator, governor, and cabinet member across different phases of his career"
        ],
        "effects": [
            "His six-year Navy secretaryship contributed to the institutional development of the US Navy in the critical post-War of 1812 period — overseeing shore establishment construction, naval expansion, and the professionalization of the Navy's officer corps during the era when the service was transitioning from wartime improvisation to peacetime professional institution",
            "His Senate President pro tempore status contributing him briefly to the top of the presidential succession illustrates the constitutional architecture of the antebellum succession system — before the Presidential Succession Act of 1947 established a more systematic line of succession, simultaneous vacancies in the vice presidency and speakership created scenarios where the Senate president pro tem would have exercised presidential power",
            "His multi-role career across legislative, executive (cabinet), and gubernatorial positions illustrated the career pattern of Era of Good Feelings politicians — fluid movement between different institutional roles in an era when party discipline was weak and individual political reputation could secure appointments across branches",
            "His Whig Senate service during the Tyler administration contributed to the congressional opposition to Tyler's policy vetoes — the Senate debates in which Clay, Webster, and Southard defined Whig legislative strategy in the period when the party's relationship with its own President had collapsed"
        ],
        "relationships": [
            {"entity": "Secretary of the Navy (1823–1829, under Monroe and Adams administrations)", "relationship": "SECRETARY_OF_THE_NAVY", "note": "Served as Secretary of the Navy for six years across two administrations (Monroe and Adams, 1823–1829) — overseeing the Navy's post-War of 1812 expansion and institutionalization"},
            {"entity": "US Senate from New Jersey (1821–1823 and 1833–1842, Whig)", "relationship": "SENATOR", "note": "Served as US Senator from New Jersey in two separate stints (1821–1823 and 1833–1842) — one of the Era of Good Feelings' and Whig period's most versatile multi-role statesmen"},
            {"entity": "10th Governor of New Jersey (1832–1833)", "relationship": "GOVERNOR", "note": "Served as New Jersey's 10th Governor (1832–1833) — transitioning between his Senate terms and Navy secretaryship as part of a multi-role political career"},
            {"entity": "Senate President pro tempore (1841–1842) / presidential succession (briefly first in line)", "relationship": "PRESIDENT_PRO_TEMPORE_BRIEFLY_FIRST_IN_LINE", "note": "Served as Senate President pro tempore (1841–1842) and was briefly first in the presidential succession when both the vice presidency and House speakership were simultaneously vacant — an unusual constitutional circumstance"},
            {"entity": "Era of Good Feelings / early Whig Party (versatile multi-role statesman)", "relationship": "REPRESENTATIVE_FIGURE_OF", "note": "A representative figure of the Era of Good Feelings' and early Whig period's political culture — fluid movement between legislative, executive, and gubernatorial roles in an era of weak party discipline and individual reputation-based appointment"}
        ]
    }),

    # 7 — Joseph Anderson
    ("joseph-anderson", {
        "summary": (
            "Joseph Inslee Anderson (1757–1837) was a "
            "New Jersey-born soldier, judge, and "
            "politician who served as one of the "
            "United States' earliest and longest-serving "
            "senators — representing Tennessee in the "
            "US Senate from 1797 to 1815, a tenure "
            "of eighteen years that made him one of "
            "the longest-serving senators of his "
            "era — and subsequently as the first "
            "Comptroller of the United States Treasury "
            "(1815–1836), a twenty-one-year tenure "
            "managing federal financial accounting.\n\n"
            "Before his Senate career, he served as "
            "a captain in the Continental Army during "
            "the Revolutionary War and as one of "
            "three judges of the Southwest Territory "
            "in the 1790s — the territorial predecessor "
            "to Tennessee, Kentucky, and parts of "
            "Alabama and Mississippi. He was a "
            "delegate to the Tennessee constitutional "
            "convention of 1796 that drafted the "
            "state's founding document and prepared "
            "Tennessee for admission to statehood.\n\n"
            "His eighteen-year Senate tenure — during "
            "which he served under six presidents, "
            "through the Adams-Jefferson partisan "
            "battles, the Jefferson and Madison "
            "administrations, the War of 1812, "
            "and the Era of Good Feelings — gave "
            "him an unusual continuity of "
            "institutional memory.\n\n"
            "His twenty-one-year Comptrollership "
            "of the Treasury contributed to the "
            "standardization of federal financial "
            "accounting procedures during the "
            "early republic's critical period "
            "of fiscal institution-building."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator from Tennessee (1797–1815, 18 years); Southwest Territory judge (1790s); Tennessee constitutional convention delegate (1796); first Comptroller of the US Treasury (1815–1836, 21 years); Revolutionary War Continental Army captain; his combined 39 years of continuous federal service across Senate and Treasury made him one of the early republic's most sustained institutional figures.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Tennessee's admission to statehood in 1796 — as the first state carved from the Southwest Territory — created the Senate seats that Anderson was elected to fill in 1797, with his prior service as a territorial judge and constitutional convention delegate establishing him as the new state's obvious choice for Senate representation",
            "The early republic's need for experienced, institutionally reliable politicians to build the new federal government's capacity — the demand for senators who could serve through the turbulent Adams-Jefferson partisan battles and maintain functional governance — created the conditions for Anderson's unusually long Senate tenure",
            "The Treasury Department's need for a long-serving Comptroller to develop and standardize federal financial accounting procedures during the early republic's fiscal institution-building period — creating the demand for the 21-year Comptrollership that Anderson filled"
        ],
        "effects": [
            "His 18-year Senate tenure contributed to Tennessee's representation through the most formative period of the early American republic — from Tennessee's first years as a state through the War of 1812 — providing the state with stable and experienced Senate presence during a critical era",
            "His Tennessee constitutional convention delegate service contributed to the drafting of Tennessee's founding constitutional document — one of the foundational institutional acts that prepared the state for admission and established its governmental framework",
            "His 21-year Comptrollership of the Treasury contributed to the standardization and institutionalization of federal financial accounting — building the procedural framework for federal fiscal oversight during the period when the Treasury Department was developing its permanent administrative practices",
            "His combined 39 years of federal service — 18 as senator, 21 as Comptroller — contributed to the institutional memory and continuity of early American governance, providing a rare example of consistent federal engagement across the full sweep of the early republic from Washington's administration to Jackson's second term"
        ],
        "relationships": [
            {"entity": "US Senate from Tennessee (1797–1815, 18-year tenure)", "relationship": "SENATOR", "note": "Served as US Senator from Tennessee for 18 years (1797–1815) — one of the longest-serving senators of his era, providing stable representation through six presidential administrations"},
            {"entity": "First Comptroller of the US Treasury (1815–1836, 21-year tenure)", "relationship": "FIRST_COMPTROLLER", "note": "Served as the first Comptroller of the United States Treasury for 21 years (1815–1836) — developing federal financial accounting procedures during the early republic's critical fiscal institution-building period"},
            {"entity": "Southwest Territory (one of three territorial judges, 1790s)", "relationship": "TERRITORIAL_JUDGE", "note": "Served as one of three judges of the Southwest Territory in the 1790s — the territorial predecessor to Tennessee and other states, building the judicial infrastructure of the early western frontier"},
            {"entity": "Tennessee constitutional convention of 1796 (delegate)", "relationship": "DELEGATE_TO", "note": "Served as a delegate to Tennessee's constitutional convention of 1796 — contributing to the drafting of the state's founding document that prepared it for admission to statehood"},
            {"entity": "Continental Army / American Revolutionary War (captain)", "relationship": "CAPTAIN_DURING", "note": "Served as a captain in the Continental Army during the Revolutionary War — the military service that established his credentials for the post-war political and judicial career that followed"}
        ]
    }),

    # 8 — James Turner Morehead
    ("james-turner-morehead", {
        "summary": (
            "James Turner Morehead (1797–1854) was a "
            "Kentucky lawyer, politician, and orator "
            "who served as the 12th Governor of "
            "Kentucky (1834–1836) — the first native-born "
            "Kentuckian to hold the governorship — "
            "and subsequently as US Senator from "
            "Kentucky (1841–1847), representing the "
            "Whig political tradition of his mentor "
            "Henry Clay. Born in Pittsylvania County, "
            "Virginia, his family moved to Kentucky "
            "when he was a child, making him the "
            "first governor born in the state "
            "rather than migrated from elsewhere.\n\n"
            "His governorship came during a period "
            "of intense political competition in "
            "Kentucky between the National Republican "
            "and Democratic parties — the Kentucky "
            "theatre of the Jackson Wars, in which "
            "Henry Clay's allies challenged the "
            "Jacksonian Democrats for control of "
            "the state government. Morehead's "
            "election as governor represented a "
            "Whig (then National Republican) "
            "triumph in this competition.\n\n"
            "His gubernatorial tenure focused on "
            "internal improvements — the road, "
            "canal, and railroad infrastructure "
            "development that Clay's 'American "
            "System' advocated — and on the "
            "development of Kentucky's educational "
            "institutions. He subsequently served "
            "as a Whig senator during the "
            "most contested years of the "
            "party's history.\n\n"
            "His reputation as an orator — in "
            "a Kentucky political culture that "
            "deeply valued oratorical skill — "
            "was one of his most noted "
            "attributes, contributing to "
            "the Whig tradition of eloquent "
            "political advocacy in a state "
            "dominated by Clay's example."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "12th Governor of Kentucky (1834–1836); first native-born Kentuckian to hold the governorship; US Senator from Kentucky (1841–1847); Whig Party ally of Henry Clay; contributed to Kentucky's internal improvements program and educational development; his career traced the Whig Party's rise and decline in Clay's home state.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Jackson Wars' Kentucky theatre — the intense political competition between Henry Clay's National Republican/Whig allies and the Jacksonian Democrats for control of Kentucky's state government — created the electoral environment in which Morehead's gubernatorial election represented a Whig triumph in Clay's home state",
            "Kentucky's status as a new state still building its institutional infrastructure — requiring internal improvements (roads, canals, railroads) and educational development that the Whig American System advocated — created the policy agenda for Morehead's governorship",
            "Morehead's own Kentucky nativity — the circumstance of being born in the state rather than migrated from Virginia or elsewhere — created the symbolic distinction that made him the 'first native-born Kentuckian governor,' a marker of the state's maturation from frontier territory to established state"
        ],
        "effects": [
            "His governorship contributed to Kentucky's internal improvements program — advancing the road, canal, and railroad infrastructure development that Clay's American System advocated, and contributing to the state's economic connectivity and development",
            "His status as the first native-born Kentuckian governor contributed symbolically to the state's identity as a mature community — a marker that Kentucky had produced its own political leadership class rather than relying entirely on migrants from older states",
            "His Senate service during the Tyler administration contributed to the Whig legislative opposition to Tyler's policy vetoes — the congressional battles in which Clay and the Whig senators attempted to define their party's agenda against a president who had effectively abandoned Whig principles",
            "His career as a Clay ally in Kentucky illustrated the geographic and political reach of Clay's influence — Morehead being one of many Kentucky politicians who built careers within the political framework that Clay's national reputation and state organization had created"
        ],
        "relationships": [
            {"entity": "12th Governor of Kentucky (1834–1836, first native-born Kentuckian governor)", "relationship": "GOVERNOR", "note": "Served as Kentucky's 12th Governor (1834–1836) — the first native-born Kentuckian to hold the governorship, a symbolic marker of the state's maturation"},
            {"entity": "US Senate from Kentucky (Whig, 1841–1847)", "relationship": "SENATOR", "note": "Served as Whig US Senator from Kentucky (1841–1847) — contributing to the Senate debates during the Tyler administration when the Whig Party was defining its legislative strategy"},
            {"entity": "Henry Clay / Whig Party / Kentucky Whig political tradition", "relationship": "ALLY_AND_REPRESENTATIVE_FIGURE_OF", "note": "A close ally of Henry Clay and representative figure of Kentucky's Whig political tradition — his career built within the political framework that Clay's national reputation and state organization had created"},
            {"entity": "Kentucky internal improvements program / American System", "relationship": "GUBERNATORIAL_ADVOCATE_OF", "note": "Advanced Kentucky's internal improvements program during his governorship — road, canal, and railroad infrastructure development consistent with Clay's American System"},
            {"entity": "Jackson Wars / National Republican–Democratic competition in Kentucky", "relationship": "GUBERNATORIAL_VICTOR_IN", "note": "His gubernatorial election represented a Whig/National Republican triumph in the Kentucky theatre of the Jackson Wars — the intense competition between Clay's allies and Jacksonian Democrats for control of the state"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 46)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
