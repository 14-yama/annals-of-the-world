#!/usr/bin/env python3
"""
Batch 27 — 8 entities: Hugh de Neville, Richard Peters, Levi Lincoln Sr.,
Robert Goodloe Harper, William Greene, Andrew Moore, Jean Gabriel Marchand,
Gerard C. Brandon
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

    # 1 — Hugh de Neville
    ("hugh-de-neville", {
        "summary": (
            "Hugh de Neville (died c. 1234) was a powerful English royal administrator "
            "who served as Chief Forester of England under three successive Plantagenet "
            "kings — Richard I, King John, and Henry III — accumulating one of the "
            "most sustained careers in royal service of any medieval English official. "
            "His role as Chief Forester placed him at the head of the royal forest "
            "administration — one of the most lucrative and resented instruments of "
            "medieval English royal power, in which the crown reserved vast stretches "
            "of land as royal forest subject to forest law, with severe penalties "
            "for unauthorized hunting, cultivation, or settlement.\n\n"
            "Neville's career began in the household of Prince Richard, and he "
            "accompanied the Prince — soon to be Richard I — on the Third Crusade "
            "(1190–1192), participating in one of the great military campaigns of "
            "the medieval period and serving in the king's entourage during the "
            "siege of Acre, the march to Jaffa, and the failed attempts to take "
            "Jerusalem. His crusade service established his personal loyalty to "
            "Richard and secured his position in the royal administration.\n\n"
            "Under King John, Neville remained in royal service — serving simultaneously "
            "as Chief Forester and as sheriff for multiple counties — an accumulation "
            "of administrative positions that illustrates the concentrated nature of "
            "medieval English royal administration, in which a small group of loyal "
            "and capable officials managed enormous administrative responsibilities "
            "across multiple offices. John's reign was characterized by intensified "
            "exploitation of royal prerogatives — including the forest revenues that "
            "Neville administered — that contributed to the baronial resistance "
            "culminating in Magna Carta (1215).\n\n"
            "His career as Chief Forester made him an instrument of the royal forest "
            "system that the barons targeted in the Charter of the Forest (1217) — "
            "a companion document to Magna Carta that restricted royal forest "
            "administration."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Chief Forester of England under Richard I, King John, and Henry III; accompanied Richard on the Third Crusade; a key administrator of the royal forest system whose exploitation under John contributed to the Magna Carta crisis.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Plantagenet royal forest system — one of the most extensive and resented instruments of medieval English royal power — created the administrative role that defined his career as Chief Forester",
            "His personal loyalty to Prince Richard (established in the Prince's household) and his service on the Third Crusade secured his position in royal administration through Richard's reign and into John's",
            "The medieval English administrative system's concentration of multiple offices in reliable royal servants — sheriffs, foresters, justiciars — created the multi-office career that Neville accumulated"
        ],
        "effects": [
            "His administration of the royal forest system under John contributed to the baronial grievances about royal prerogative exploitation that culminated in Magna Carta (1215) and the Charter of the Forest (1217)",
            "His long career across three reigns — Richard I, John, and Henry III — provided remarkable administrative continuity in the royal forest administration during one of the most politically turbulent periods in English history",
            "The Charter of the Forest (1217) — a direct response to the abuses of the royal forest system that he administered — restricted the royal forest administration and provided a precedent for limiting royal prerogative",
            "His crusade service contributed to the Third Crusade's royal entourage — he was part of the English royal presence during the most famous military campaign of the medieval period"
        ],
        "relationships": [
            {"entity": "King Richard I of England", "relationship": "SERVED_AS_CHIEF_FORESTER_UNDER", "note": "Accompanied Richard as a member of his household and then served as Chief Forester under Richard I from 1189"},
            {"entity": "King John of England", "relationship": "SERVED_AS_CHIEF_FORESTER_UNDER", "note": "Continued as Chief Forester under King John — administering the forest system whose exploitation contributed to the Magna Carta crisis"},
            {"entity": "Third Crusade (1190–1192)", "relationship": "PARTICIPANT_IN", "note": "Accompanied Richard I on the Third Crusade as part of the royal entourage — present at Acre, Jaffa, and the failed Jerusalem campaigns"},
            {"entity": "Royal Forest system (medieval England)", "relationship": "CHIEF_ADMINISTRATOR_OF", "note": "Chief Forester of England — the head of the royal forest administration that controlled vast stretches of England under severe forest law"},
            {"entity": "Magna Carta (1215) / Charter of the Forest (1217)", "relationship": "ADMINISTERED_SYSTEM_THAT_PROVOKED", "note": "His administration of the forest system contributed to baronial grievances; the Charter of the Forest (1217) directly restricted the forest administration he had run"}
        ]
    }),

    # 2 — Richard Peters
    ("richard-peters", {
        "summary": (
            "Richard Peters (1744–1828) was a Pennsylvania lawyer, soldier, statesman, "
            "and judge whose career spanned the full arc of America's founding generation — "
            "from colonial Pennsylvania law through the Revolutionary War, the Articles "
            "of Confederation era, the Constitutional period, and into the early 19th "
            "century, when he served as a federal district judge for more than three decades. "
            "His combination of military service, legislative and administrative roles, "
            "and judicial tenure made him one of the most broadly experienced figures "
            "of the Pennsylvania founding generation.\n\n"
            "During the Revolutionary War, Peters served as Secretary of the Continental "
            "Board of War — the executive body responsible for organizing and supplying "
            "the Continental Army. Working alongside General George Washington's military "
            "operations, the Board of War was responsible for procurement, logistics, "
            "manpower, and strategic advice — and Peters's role in its administration "
            "placed him at the organizational center of the war effort. He also served "
            "as a delegate to the Congress of the Confederation (the government under "
            "the Articles) and in the Pennsylvania State Assembly — accumulating "
            "legislative experience at both state and national levels.\n\n"
            "His most enduring role was as a federal judge: he served as US District "
            "Judge for the Eastern District of Pennsylvania (1792–1828) — a 36-year "
            "tenure that made him one of the longest-serving federal judges of his "
            "generation. His judicial career included important rulings on admiralty, "
            "commercial law, and federal jurisdiction, and he wrote extensively about "
            "agricultural improvement — publishing works that made him an important "
            "figure in the early American agricultural improvement movement.\n\n"
            "The Peters v. United States case (1809) was one of his more significant "
            "judicial confrontations — involving a dispute between federal and "
            "Pennsylvania state court authority that reached the Supreme Court."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania Founding era lawyer, Secretary of the Continental Board of War, delegate to the Congress of the Confederation, and US District Judge for 36 years (1792–1828); also a significant agricultural improvement writer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution's need for an organizational body to manage the Continental Army — the Continental Board of War — created the administrative role that defined Peters's wartime service",
            "Pennsylvania's centrality to both the Continental Congress and the early federal government — as the location of Philadelphia, the revolutionary capital — placed Peters at the center of both state and national founding-era politics",
            "The Judiciary Act of 1789's creation of the federal district court system produced the judicial institution in which Peters served for 36 years"
        ],
        "effects": [
            "His 36-year tenure as US District Judge for Eastern Pennsylvania provided remarkable judicial continuity during the formative period of American federal law — helping establish the authority and procedures of the federal district courts",
            "His role as Secretary of the Continental Board of War contributed to the organizational capacity of the Revolutionary War effort — the administrative management of the Continental Army's logistics and supply",
            "His agricultural improvement writings contributed to the early American agricultural improvement movement — helping disseminate scientific farming techniques in the early republic",
            "The Peters v. United States case (1809) involving federal-state court authority contributed to the developing jurisprudence of federal judicial supremacy"
        ],
        "relationships": [
            {"entity": "Continental Board of War", "relationship": "SECRETARY_OF", "note": "Served as Secretary of the Continental Board of War — the executive body responsible for organizing and supplying the Continental Army during the Revolutionary War"},
            {"entity": "US District Court (Eastern District of Pennsylvania)", "relationship": "JUDGE_FOR_36_YEARS", "note": "Served as US District Judge for Eastern Pennsylvania (1792–1828) — one of the longest-serving federal judges of his generation"},
            {"entity": "Congress of the Confederation", "relationship": "DELEGATE_TO", "note": "Served as a delegate to the Congress of the Confederation — the national government under the Articles of Confederation"},
            {"entity": "General George Washington", "relationship": "COLLABORATED_WITH_AS_BOARD_OF_WAR_SECRETARY", "note": "As Secretary of the Board of War, worked alongside Washington's military operations to organize and supply the Continental Army"},
            {"entity": "Pennsylvania agricultural improvement movement", "relationship": "PROMINENT_CONTRIBUTOR_TO", "note": "Published significant agricultural improvement writings that contributed to the early American agricultural improvement movement"}
        ]
    }),

    # 3 — Levi Lincoln Sr.
    ("levi-lincoln-sr", {
        "summary": (
            "Levi Lincoln Sr. (1749–1820) was an American lawyer and Democratic-Republican "
            "statesman from Massachusetts who served as the first Attorney General of "
            "the United States under President Thomas Jefferson (1801–1805) — the "
            "nation's third Attorney General — and who played a significant role in "
            "the events that produced one of the most important cases in American "
            "constitutional history: Marbury v. Madison (1803). Lincoln was the acting "
            "Secretary of State during the critical transition between the Adams and "
            "Jefferson administrations when the disputed judicial commissions at the "
            "heart of Marbury were withheld from delivery — a decision whose consequences "
            "Lincoln could not have foreseen.\n\n"
            "Lincoln came from the Revolutionary generation: he had been active in "
            "Massachusetts politics and law through the Revolution and its aftermath, "
            "and he was a committed Democratic-Republican who aligned with Jefferson's "
            "vision of limited federal government, agrarian republicanism, and opposition "
            "to Federalist financial and judicial policies. His appointment as Jefferson's "
            "first Attorney General gave him responsibility for providing the administration's "
            "legal advice at the moment when the fundamental questions of federal judicial "
            "authority were being contested between the Jefferson executive and the "
            "Marshall Supreme Court.\n\n"
            "His Massachusetts career was long and distinguished: he served two terms "
            "as Lieutenant Governor of Massachusetts and acted as Governor during the "
            "remainder of Elbridge Gerry's term. His family produced another generation "
            "of Massachusetts political leaders — his son Levi Lincoln Jr. was also "
            "Governor of Massachusetts.\n\n"
            "His role in the events leading to Marbury v. Madison — specifically his "
            "withholding of the judicial commissions as acting Secretary of State — "
            "makes him an indirect participant in one of the most consequential moments "
            "in American constitutional history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Attorney General under Jefferson (1801–05); played a key role in the events that produced Marbury v. Madison — he withheld the disputed judicial commissions as acting Secretary of State; also Lt. Governor and acting Governor of Massachusetts.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Jefferson's election as president in 1800 — the 'Revolution of 1800' — brought Democratic-Republicans into power and created the new administration's need for an Attorney General who shared Jefferson's constitutional philosophy",
            "The Adams administration's last-minute judicial appointments — the 'midnight judges' — created the political conflict over the delivery of judicial commissions that Lincoln was directly involved in as acting Secretary of State",
            "Massachusetts's Democratic-Republican political culture, in which Lincoln had been a leading figure, created the political career that qualified him for the Jefferson AG appointment"
        ],
        "effects": [
            "His withholding of the Adams judicial commissions as acting Secretary of State directly created the factual predicate for Marbury v. Madison (1803) — one of the most important cases in American constitutional history, establishing judicial review",
            "His tenure as Jefferson's Attorney General helped establish the legal philosophy of the Democratic-Republican administration — providing constitutional advice during the administration's battles with the Federalist judiciary",
            "His Massachusetts career — as Lt. Governor and acting Governor — contributed to the Democratic-Republican political tradition in Massachusetts and helped shape his family's political dynasty",
            "His son Levi Lincoln Jr.'s governorship of Massachusetts reflected the family political tradition he established"
        ],
        "relationships": [
            {"entity": "Thomas Jefferson (US President)", "relationship": "FIRST_ATTORNEY_GENERAL_UNDER", "note": "Served as Jefferson's first Attorney General (1801–1805) — the administration's chief legal officer during its most consequential constitutional battles"},
            {"entity": "Marbury v. Madison (1803)", "relationship": "INDIRECT_CAUSE_OF", "note": "His withholding of the Adams judicial commissions as acting Secretary of State created the factual predicate for Marbury v. Madison — which established judicial review"},
            {"entity": "John Adams's 'midnight judges' appointments", "relationship": "WITHHELD_COMMISSIONS_OF", "note": "As acting Secretary of State in the transition period, withheld the judicial commissions that John Adams had signed for his last-minute appointments"},
            {"entity": "Massachusetts Democratic-Republican politics", "relationship": "LEADER_OF", "note": "A leading Democratic-Republican in Massachusetts — Lt. Governor, acting Governor, and Jefferson's AG choice from the state"},
            {"entity": "Levi Lincoln Jr. (Massachusetts Governor)", "relationship": "FATHER_OF", "note": "Father of Levi Lincoln Jr. — also Governor of Massachusetts — establishing a two-generation political family tradition"}
        ]
    }),

    # 4 — Robert Goodloe Harper
    ("robert-goodloe-harper", {
        "summary": (
            "Robert Goodloe Harper (1765–1825) was an American soldier, lawyer, and "
            "Federalist politician from Maryland — born in Virginia and later representing "
            "South Carolina and then Maryland — who is best remembered for two things: "
            "his aggressive Federalist leadership in the US House during the XYZ Affair "
            "and his coinage of the phrase 'Millions for defence, but not one cent for "
            "tribute' (misattributed to Charles Cotesworth Pinckney, but actually "
            "Harper's toast) — and his role in naming Liberia and its capital Monrovia. "
            "As a leader of the American Colonization Society, Harper proposed the names "
            "'Liberia' (from the Latin for freedom) for the African colony and 'Monrovia' "
            "(in honor of President James Monroe) for its capital — making him the "
            "inadvertent namer of a nation.\n\n"
            "His political career was characterized by fierce Federalism: as a "
            "congressman from South Carolina in the 1790s, he was one of the most "
            "aggressive Federalist voices demanding a strong response to France during "
            "the XYZ Affair (1797–1798), when French demands for bribes before "
            "diplomatic negotiations — exposed by the dispatches of American "
            "envoys — caused a political crisis. His memorable toast 'Millions for "
            "defence, but not one cent for tribute' became one of the most famous "
            "phrases of the early republic.\n\n"
            "After transitioning to Maryland — where he married the daughter of Charles "
            "Carroll of Carrollton, the last surviving signer of the Declaration of "
            "Independence — Harper served briefly in the US Senate (1816) and in the "
            "Maryland legislature, and continued as one of Baltimore's most prominent "
            "lawyers.\n\n"
            "His dual legacy — aggressive Federalist hawk and the man who named Liberia — "
            "captures the contradictions of a figure who championed both American national "
            "strength and the problematic solution of African colonization."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Federalist congressman who coined 'Millions for defence, but not one cent for tribute' during the XYZ Affair crisis; proposed the names 'Liberia' and 'Monrovia' for the African colony; son-in-law of Charles Carroll (last surviving Declaration signer); brief US Senator from Maryland (1816).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The XYZ Affair (1797–1798) — France's demands for bribes before diplomatic negotiations — created the political crisis that produced Harper's most famous rhetorical contribution and elevated him to Federalist leadership",
            "The American Colonization Society's project of 'resolving' slavery through the emigration of freed Black Americans to Africa — which Harper supported — created the context in which he proposed the names 'Liberia' and 'Monrovia'",
            "His marriage into the Carroll family — the family of Charles Carroll, the last surviving Declaration signer — gave him Maryland's most prestigious family connection and anchored his legal and political career in Baltimore"
        ],
        "effects": [
            "His coinage of 'Millions for defence, but not one cent for tribute' became one of the most famous phrases of the early American republic — though often misattributed to Pinckney — expressing the Federalist position on national honor and military preparedness",
            "His naming of 'Liberia' and 'Monrovia' — though the project of African colonization is now recognized as deeply problematic — gave permanent names to a West African nation that has existed as an independent state since 1847",
            "His Federalist leadership during the XYZ Affair contributed to the political momentum for the Quasi-War naval buildup and the strengthening of American national defense",
            "His legal career in Baltimore contributed to the development of Maryland's legal bar and to the political networks of the early republic's Federalist establishment"
        ],
        "relationships": [
            {"entity": "XYZ Affair (1797–1798)", "relationship": "FEDERALIST_LEADER_DURING", "note": "One of the most aggressive Federalist voices demanding strong response to France during the XYZ Affair — coined 'Millions for defence, but not one cent for tribute'"},
            {"entity": "Liberia (West Africa)", "relationship": "NAMED", "note": "Proposed the name 'Liberia' (from the Latin for freedom) for the American Colonization Society's African colony — and 'Monrovia' for its capital, after President Monroe"},
            {"entity": "American Colonization Society", "relationship": "LEADER_OF", "note": "A leader of the American Colonization Society — the organization that founded the Liberian colony as a destination for freed African Americans"},
            {"entity": "Charles Carroll of Carrollton", "relationship": "FATHER_IN_LAW_OF", "note": "Married the daughter of Charles Carroll of Carrollton — the last surviving signer of the Declaration of Independence"},
            {"entity": "US Federalist Party", "relationship": "LEADING_FIGURE_OF", "note": "A leading Federalist politician, first in South Carolina and then in Maryland — aggressive in championing national defense and opposing the Democratic-Republicans"}
        ]
    }),

    # 5 — William Greene
    ("william-greene", {
        "summary": (
            "William Greene Jr. (1731–1809) was an American statesman who served as "
            "the second Governor of Rhode Island — holding the office for eight years "
            "(1778–1786), five of which coincided with the American Revolutionary War. "
            "His governorship made him the principal political executive of Rhode Island "
            "during the most critical military and political crisis in the colony's "
            "history: the period of British occupation of Newport, the French alliance, "
            "and the transition from colony to state. He came from one of Rhode Island's "
            "most prominent families — his father, William Greene Sr., had served 11 "
            "terms as colonial governor, and his great-grandfather John Greene Jr. "
            "had also served as colonial governor — making him the third generation "
            "of his family to lead Rhode Island.\n\n"
            "Rhode Island's Revolutionary War experience was particularly difficult: "
            "the British occupied Newport (the colony's commercial hub) from December "
            "1776 to October 1779, cutting the colony economically and forcing its "
            "government to operate under wartime constraints. Greene's governorship "
            "navigated this occupation, the failed Franco-American attack on Newport "
            "in August 1778 (the Battle of Rhode Island), and the economic disruption "
            "of maritime commerce that had been the basis of Rhode Island's colonial "
            "prosperity.\n\n"
            "Rhode Island was also the most resistant of the thirteen states to the "
            "Constitution of 1787 — the last to ratify (May 1790) and the state that "
            "most consistently resisted federal authority in the 1780s. Greene's "
            "governorship predates the ratification controversy, but his tenure "
            "shaped the state's political culture during the critical transition "
            "from colonial to state governance.\n\n"
            "His family's three-generation governorship tradition made the Greenes "
            "Rhode Island's most sustained political dynasty of the colonial era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Rhode Island for 8 years (1778–1786) — 5 during the Revolutionary War — navigating British occupation of Newport and the French alliance; third generation of his family to govern Rhode Island.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution and British occupation of Newport — cutting Rhode Island's commercial lifeline — created the wartime political crisis that Greene's long governorship had to navigate",
            "His family's three-generation tradition of Rhode Island leadership — with father and great-grandfather both serving as colonial governors — placed him in the natural succession of the colony's political elite",
            "Rhode Island's distinctive political culture — emphasizing local autonomy and commercial independence — shaped the governing philosophy of his long governorship"
        ],
        "effects": [
            "His 8-year governorship (the longest of any early Rhode Island governor) provided political continuity for the state through the most disruptive period in its history — from British occupation through the Franco-American alliance and the end of the war",
            "His governance during the Battle of Rhode Island (August 1778) — the failed Franco-American attack on Newport — required coordination with both American military forces and France's new alliance partnership",
            "His tenure as governor contributed to the constitutional transition of Rhode Island from a colonial charter government to a state republican government — managing the legal and institutional changes of independence",
            "The Greene family's political tradition — sustained through three generations — shaped Rhode Island's colonial and early republican political culture"
        ],
        "relationships": [
            {"entity": "Rhode Island (Revolutionary War era)", "relationship": "GOVERNOR_OF", "note": "Governor of Rhode Island (1778–1786) — 8 years including 5 during the Revolutionary War; the state's longest-serving early governor"},
            {"entity": "British occupation of Newport (1776–1779)", "relationship": "GOVERNED_DURING", "note": "Governed Rhode Island while the British occupied Newport — the colony's commercial hub — from late 1776 to October 1779"},
            {"entity": "Battle of Rhode Island (August 1778)", "relationship": "POLITICAL_LEADER_DURING", "note": "Political leader of Rhode Island during the failed Franco-American attack on Newport — the first significant military operation involving the French alliance"},
            {"entity": "William Greene Sr. (colonial governor)", "relationship": "SON_OF", "note": "Son of William Greene Sr. — who had served 11 terms as colonial governor of Rhode Island — part of the family's three-generation governorship tradition"},
            {"entity": "French-American alliance (1778)", "relationship": "MANAGED_RHODE_ISLAND_ENGAGEMENT_WITH", "note": "His governorship was the political context within which Rhode Island engaged with the French alliance — including the Franco-American operation at Newport"}
        ]
    }),

    # 6 — Andrew Moore
    ("andrew-moore", {
        "summary": (
            "Andrew Moore (1752–1821) was a Virginia lawyer, Revolutionary War soldier, "
            "and statesman who studied law under the great Virginia jurist George Wythe — "
            "who also taught Thomas Jefferson, Henry Clay, and John Marshall — making "
            "Moore part of the extraordinary generation of lawyers produced by Wythe's "
            "Williamsburg teaching. He served as a captain in the Continental Army, "
            "fighting at the Battle of Saratoga (1777) — one of the most decisive "
            "American victories of the Revolutionary War, the engagement that convinced "
            "France to enter the war on the American side — before returning to "
            "Virginia to pursue his political and legal career.\n\n"
            "Moore's post-war career was long and varied: he served in the Virginia "
            "House of Delegates, was eventually commissioned a Major General in the "
            "Virginia militia (1803), served in the US House of Representatives, "
            "and eventually served in the US Senate from Virginia — accumulating a "
            "career that spanned from the Revolution through the Jeffersonian era. "
            "His congressional career made him a moderate Democratic-Republican voice "
            "in the Virginia tradition that dominated early American national politics.\n\n"
            "The significance of his legal education under George Wythe should not be "
            "understated: Wythe was the first law professor in America (at William and "
            "Mary), the leading American proponent of legal education as a systematic "
            "discipline, and the teacher of some of the most important legal and "
            "political minds of the founding generation. Moore's training in this "
            "tradition connected him to the broader Virginia legal culture that "
            "exercised an outsized influence on the new republic.\n\n"
            "His career bridged military service, legal practice, state politics, "
            "and federal legislative service — the multi-dimensional career pattern "
            "of the Virginia gentleman-politician of the founding era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Virginia Revolutionary War captain who fought at Saratoga; studied law under George Wythe (teacher of Jefferson, Marshall, Henry Clay); served in the Continental Army, Virginia House, US House, and US Senate — a figure of the Virginia founding-generation legal-political tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His legal education under George Wythe — America's first law professor and the teacher of Jefferson, Marshall, and Clay — placed him in the most distinguished tradition of American legal education of the founding era",
            "The Revolutionary War's demand for military service from Virginia's educated elite created the wartime service that defined his early career",
            "Virginia's dominant position in early American politics — supplying four of the first five presidents and dominating the Senate — created the political context in which his legislative career had national significance"
        ],
        "effects": [
            "His study under Wythe embedded him in the Virginia legal tradition that shaped early American jurisprudence — connecting him to the network of Wythe's students who dominated founding-era American law and politics",
            "His service at Saratoga contributed to one of the most decisive American victories of the Revolutionary War — the engagement that convinced France to enter on the American side and ultimately secured independence",
            "His long career in Virginia and federal politics contributed to the Democratic-Republican tradition that dominated the early republic — providing the political continuity between the Revolutionary War generation and the Jeffersonian era",
            "His eventual rank as Major General of the Virginia militia reflected the military tradition of the Virginia gentleman-politician class"
        ],
        "relationships": [
            {"entity": "George Wythe (America's first law professor)", "relationship": "STUDIED_LAW_UNDER", "note": "Studied law under George Wythe — the first law professor in America and teacher of Jefferson, Marshall, and Henry Clay"},
            {"entity": "Battle of Saratoga (1777)", "relationship": "FOUGHT_AT", "note": "Served as a Continental Army captain at the Battle of Saratoga — the decisive American victory that convinced France to enter the Revolutionary War"},
            {"entity": "Virginia Democratic-Republican political tradition", "relationship": "MEMBER_OF", "note": "A Virginia Democratic-Republican who served in the state House of Delegates, US House, and US Senate during the Jeffersonian era"},
            {"entity": "US Senate from Virginia", "relationship": "SERVED_IN", "note": "Served in the US Senate representing Virginia — part of Virginia's dominant position in early American federal politics"},
            {"entity": "Thomas Jefferson / John Marshall / Henry Clay", "relationship": "FELLOW_STUDENT_UNDER_WYTHE", "note": "A fellow student of George Wythe alongside Jefferson, Marshall, and Clay — part of the generation that Wythe's teaching produced"}
        ]
    }),

    # 7 — Jean Gabriel Marchand
    ("jean-gabriel-marchand", {
        "summary": (
            "Jean Gabriel Marchand (1765–1851), 1st Count Marchand, was a French "
            "general and administrator who exemplifies the career trajectory of the "
            "Napoleonic era — a man who began his professional life as an attorney, "
            "was swept into military service by the French Revolution, rose through "
            "the ranks of the Revolutionary and Napoleonic armies, and was rewarded "
            "by Napoleon with noble rank and administrative responsibilities. His "
            "career spanned the entire arc of the French Revolutionary and Napoleonic "
            "period, from the early Revolutionary armies of 1791 through the Restoration.\n\n"
            "Trained as a lawyer before the Revolution, Marchand was among the thousands "
            "of educated young Frenchmen whose professional trajectories were radically "
            "altered by the Revolution's demand for military manpower. He became a "
            "company commander in the army of the First French Republic in 1791, "
            "and his service was concentrated in Italy — the theater where Napoleon "
            "Bonaparte first made his military reputation. Marchand participated in "
            "Napoleon's celebrated Italian campaign of 1796–1797, one of the most "
            "brilliant military campaigns in European history, in which Napoleon's "
            "Army of Italy — outnumbered, undersupplied, and facing multiple Austrian "
            "and Piedmontese armies — transformed northern Italy through a series "
            "of innovative offensive operations.\n\n"
            "He continued his Italian service into 1799, was eventually created "
            "a Count of the Empire by Napoleon — one of the approximately 3,500 "
            "men ennobled by Napoleon to create a new imperial aristocracy of "
            "military achievement — and served in administrative roles as the "
            "Napoleonic Empire matured.\n\n"
            "His career — from attorney to republican soldier to imperial count — "
            "illustrates the social revolution that the Napoleonic meritocracy "
            "represented: a system in which talent and military service, not birth, "
            "determined advancement."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French general and Count of the Empire (1765–1851); trained as a lawyer before the Revolution; served in the French Revolutionary and Napoleonic armies in Italy; participant in Napoleon's Italian campaign of 1796–1797 — a figure of the Napoleonic meritocratic military nobility.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Revolution's demand for educated military leadership — and the collapse of the aristocratic officer corps that had dominated the royal army — created the conditions for Marchand's transformation from lawyer to republican general",
            "Napoleon's Italian campaign (1796–1797) — which required capable officers for its innovative combined-arms operations — created the military environment in which Marchand served and distinguished himself",
            "Napoleon's creation of a new imperial nobility based on military and administrative service — rather than aristocratic birth — created the mechanism through which Marchand was elevated to Count of the Empire"
        ],
        "effects": [
            "His participation in Napoleon's Italian campaign contributed to one of the most militarily consequential campaigns of the Revolutionary era — which transformed northern Italian politics, weakened Austria, and established Napoleon's military reputation",
            "His elevation to Count of the Empire made him part of Napoleon's new imperial aristocracy — the approximately 3,500 men Napoleon ennobled to replace the old aristocracy and reward military and administrative merit",
            "His career trajectory from lawyer to republican general to imperial count illustrated the social mobility that the Napoleonic meritocracy offered educated Frenchmen of the revolutionary generation",
            "His long life (surviving to 1851) meant that his career bridged the revolutionary, imperial, Restoration, and early July Monarchy periods — providing personal continuity across France's turbulent constitutional transitions"
        ],
        "relationships": [
            {"entity": "Napoleon Bonaparte", "relationship": "SERVED_UNDER_AND_ENNOBLED_BY", "note": "Served under Napoleon in the Italian campaign of 1796–97; was created Count of the Empire by Napoleon as part of the Napoleonic meritocratic nobility"},
            {"entity": "Napoleon's Italian campaign (1796–1797)", "relationship": "PARTICIPANT_IN", "note": "Served in Napoleon's celebrated Italian campaign — one of the most brilliant military operations of the Revolutionary era that transformed northern Italian politics"},
            {"entity": "French Revolutionary Army (First Republic)", "relationship": "OFFICER_IN", "note": "Became a company commander in the French Revolutionary Army in 1791 — transitioning from lawyer to republican military officer with the Revolution's demand for educated leadership"},
            {"entity": "Napoleonic Empire / Count of the Empire", "relationship": "COUNT_OF", "note": "Created 1st Count Marchand by Napoleon — part of the approximately 3,500 men Napoleon ennobled to create a new military-achievement-based imperial aristocracy"},
            {"entity": "French Revolutionary legal profession", "relationship": "TRAINED_AS", "note": "Trained as a lawyer before the Revolution — his legal training was the professional foundation from which the Revolution redirected him to military service"}
        ]
    }),

    # 8 — Gerard C. Brandon
    ("gerard-c-brandon", {
        "summary": (
            "Gerard Chittocque Brandon (1788–1850) was an American politician and "
            "lawyer who twice served as Governor of Mississippi — first as Lieutenant "
            "Governor who succeeded to the governorship upon Walter Leake's death in 1825, "
            "and then as elected Governor (1827–1832) — and who holds the distinction "
            "of being the first native-born Governor of Mississippi, reflecting the "
            "transition of the state's political leadership from transplanted "
            "easterners to Mississippi-born political figures. His career also included "
            "service as a delegate to the Mississippi constitutional conventions of "
            "1817 and 1832 — the constitutional assemblies that defined Mississippi's "
            "fundamental law at the moments of its statehood and early constitutional "
            "revision.\n\n"
            "Mississippi's early statehood period (admitted 1817) was characterized "
            "by rapid population growth, cotton cultivation, and the expansion of "
            "the slave plantation system into the fertile Delta and Black Belt "
            "regions — making Mississippi one of the centers of American antebellum "
            "slaveholder political culture. Brandon's political career was embedded "
            "in this slaveholder cotton republic, and his governorships occurred "
            "during the period of Mississippi's most rapid territorial expansion "
            "and economic development under the slave system.\n\n"
            "His participation in both the 1817 and 1832 constitutional conventions "
            "made him one of the most important constitutional architects of Mississippi's "
            "foundational political institutions. Constitutional conventions in the "
            "antebellum South were critical political moments when the structures "
            "of state power — including the distribution of representation, the "
            "extent of suffrage, and the protection of slave property — were debated "
            "and defined.\n\n"
            "His career as Mississippi's first native-born governor marked a generational "
            "transition in American frontier state politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "First native-born Governor of Mississippi; served as governor twice (1825, 1827–1832); delegate to the Mississippi constitutional conventions of 1817 and 1832 — a figure in the early development of Mississippi's state political institutions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mississippi's rapid settlement and statehood (1817) — driven by cotton cultivation and slave plantation expansion — created the political context in which Brandon's career developed",
            "His native Mississippi birth — at a time when most state political leaders were transplanted easterners — positioned him as the symbolic first of a new generation of Mississippi-born political leaders",
            "The Mississippi constitutional conventions of 1817 and 1832 — which defined the state's fundamental political structures — created the constitutional arena in which he served as a founding institutional architect"
        ],
        "effects": [
            "His two terms as governor provided political leadership for Mississippi during the period of its most rapid demographic and economic expansion — the cotton boom of the late 1820s and early 1830s",
            "His participation in both constitutional conventions (1817 and 1832) made him one of the key architects of Mississippi's constitutional foundations — shaping the fundamental political institutions of the state",
            "His status as the first native-born governor symbolized a generational transition in American frontier state politics — from transplanted eastern leadership to locally born political figures",
            "His career model — lawyer, legislator, lieutenant governor, governor — established the standard political pathway for antebellum Mississippi political leaders"
        ],
        "relationships": [
            {"entity": "Mississippi (early statehood)", "relationship": "FIRST_NATIVE-BORN_GOVERNOR_OF", "note": "The first native-born Governor of Mississippi — symbolizing the transition from transplanted eastern leadership to Mississippi-born political figures"},
            {"entity": "Mississippi Constitutional Convention (1817)", "relationship": "DELEGATE_TO", "note": "A delegate to the 1817 constitutional convention that defined Mississippi's foundational state constitution upon its admission to statehood"},
            {"entity": "Mississippi Constitutional Convention (1832)", "relationship": "DELEGATE_TO", "note": "A delegate to the 1832 constitutional convention that revised Mississippi's state constitution during the Jacksonian constitutional reform era"},
            {"entity": "Walter Leake (Mississippi Governor)", "relationship": "SUCCEEDED_UPON_DEATH_OF", "note": "First became governor upon the death of Governor Walter Leake in 1825 — ascending from Lieutenant Governor"},
            {"entity": "Mississippi antebellum slave-plantation economy", "relationship": "POLITICAL_LEADER_OF", "note": "His governorships occurred during Mississippi's period of most rapid cotton plantation expansion — he governed the antebellum slave-plantation political economy"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 27)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
