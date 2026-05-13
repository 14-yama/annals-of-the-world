#!/usr/bin/env python3
"""
Batch 29 — 8 entities: James B. Ray, William Hendricks, Marcus Morton, Luther Martin,
Caleb Strong, Hamilton Rowan Gamble, Royall Tyler, John Sullivan
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

    # 1 — James B. Ray
    ("james-b-ray", {
        "summary": (
            "James Brown Ray (1794–1848) was an Indiana lawyer and politician who "
            "holds the distinction of being the only Indiana Senate president pro "
            "tempore ever elevated directly to the governorship — a constitutional "
            "succession that occurred in 1825 when both Governor William Hendricks "
            "(who had been elected to the US Senate) and Lieutenant Governor Ratliff "
            "Boon (who briefly succeeded) vacated the office, leaving the Senate "
            "president pro tempore — Ray — as the next in line under Indiana's "
            "constitutional succession rules. He became governor one week before "
            "his 31st birthday, making him one of the youngest governors in "
            "Indiana's history.\n\n"
            "Ray served as governor from 1825 to 1831 — a period that coincided "
            "with the transformation of American politics from the Era of Good "
            "Feelings' non-partisan politics into the partisan realignment that "
            "produced the Democratic and Whig parties. Remarkably, Ray never joined "
            "a political party — he governed as an independent during the formation "
            "of the Second Party System, an unusual posture during a period of "
            "intense partisan organization. His independence made him politically "
            "difficult to categorize and alienated factions on multiple sides.\n\n"
            "His governorship was marked by his advocacy for internal improvements — "
            "roads, canals, and infrastructure development — that would connect "
            "Indiana's frontier agricultural communities to eastern markets. He "
            "supported the construction of roads and the beginnings of Indiana's "
            "canal era, which accelerated after his tenure. He also oversaw "
            "Indiana's early development of public education systems.\n\n"
            "His unusual path to power — through constitutional succession rather "
            "than election — and his refusal to align with emerging parties made "
            "him one of the more unusual figures in Indiana's early political history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Only Indiana Senate president pro tempore elevated directly to governor; became governor at 30 through constitutional succession in 1825; governed 1825–1831; refused to join any political party during the formation of the Second Party System; advocated for infrastructure improvements in early Indiana.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Indiana's constitutional succession rule — placing the Senate president pro tempore next in line after the Lieutenant Governor — created the unusual constitutional pathway through which Ray reached the governorship",
            "The departure of Governor Hendricks to the US Senate and Lieutenant Governor Boon's brief succession created the specific vacancy that triggered Ray's elevation",
            "Indiana's rapid frontier development and demand for internal improvements — roads, canals, and infrastructure to connect frontier agricultural communities to markets — created the primary policy challenges of his governorship"
        ],
        "effects": [
            "His six-year governorship (1825–1831) provided political leadership for Indiana during its most critical early development period — as the state transitioned from frontier territory to established agricultural state",
            "His advocacy for internal improvements — roads and canals — contributed to Indiana's infrastructure development program that accelerated under his successors and connected frontier communities to eastern markets",
            "His refusal to join any political party during the formation of the Second Party System made him an anomaly in Indiana politics — a symbol of the old Era of Good Feelings non-partisan ideal that was being swept away by partisan organization",
            "His unusual constitutional succession — as Senate president pro tempore directly ascending to governor — established a constitutional precedent in Indiana's succession rules"
        ],
        "relationships": [
            {"entity": "Indiana (early statehood)", "relationship": "GOVERNOR_OF_1825-1831", "note": "Governor of Indiana (1825–1831) — ascending through constitutional succession as Senate president pro tempore"},
            {"entity": "William Hendricks (Indiana Governor)", "relationship": "SUCCEEDED_IN_OFFICE", "note": "Governor Hendricks's departure for the US Senate created the succession chain that elevated Ray to the governorship"},
            {"entity": "Second Party System (Democratic-Whig formation)", "relationship": "GOVERNED_INDEPENDENTLY_DURING", "note": "Refused to join any party during the formation of the Second Party System — governing as an independent anomaly amid intense partisan realignment"},
            {"entity": "Indiana internal improvements movement", "relationship": "ADVOCATE_FOR", "note": "Championed roads, canals, and infrastructure improvements that laid the groundwork for Indiana's canal era"},
            {"entity": "Indiana constitutional succession (Senate pro tempore)", "relationship": "ONLY_EXAMPLE_OF", "note": "The only Indiana Senate president pro tempore ever elevated directly to governor — a unique constitutional succession in Indiana's history"}
        ]
    }),

    # 2 — William Hendricks
    ("william-hendricks", {
        "summary": (
            "William Hendricks (1782–1850) was an Indiana lawyer and Democratic-Republican "
            "statesman who held successive positions at the highest levels of Indiana's "
            "early political institutions — serving as US Representative (1816–1822), "
            "3rd Governor of Indiana (1822–1825), and US Senator from Indiana "
            "(1825–1837) — an unbroken 21-year career in high office that made him "
            "one of the most continuously powerful political figures in Indiana's "
            "founding generation. His family political legacy was even more enduring: "
            "he is the uncle of Thomas Andrews Hendricks, who served as Vice President "
            "of the United States under Grover Cleveland (1885–1886) — making the "
            "Hendricks family one of the most politically significant in Indiana's "
            "history.\n\n"
            "Hendricks arrived in Indiana in the territorial period and quickly "
            "established himself as a lawyer and politician — winning election to "
            "Congress as a Democratic-Republican as the territory transitioned to "
            "statehood. His congressional career (1816–1822) coincided with the "
            "Era of Good Feelings — the period of apparent single-party governance "
            "that preceded the emergence of the Second Party System — and he was "
            "associated with the Jeffersonian tradition of states' rights and "
            "agrarian democracy.\n\n"
            "As Indiana's governor (1822–1825), he oversaw the state's rapid "
            "demographic expansion — Indiana's population was doubling in each "
            "decade of the 1820s — and advocated for public education, internal "
            "improvements, and the legal infrastructure of an expanding frontier "
            "state. He departed the governorship to become a US Senator, triggering "
            "the unusual constitutional succession that elevated James B. Ray to "
            "the governorship.\n\n"
            "In the Senate (1825–1837), he positioned himself as an Anti-Jacksonian — "
            "a National Republican and then Whig — opposing Jackson's policies "
            "on the Bank, Indian removal, and federal authority."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "3rd Governor of Indiana (1822–1825); US Representative (1816–1822) and US Senator (1825–1837) — a 21-year career in high office; uncle of Vice President Thomas A. Hendricks; Anti-Jacksonian/Whig in the Senate; a founding figure of Indiana's political establishment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Indiana's transition from territorial to statehood politics created the opportunities in which Hendricks established his political career — arriving during the territorial period and growing with the new state's institutions",
            "The Era of Good Feelings' Democratic-Republican dominance created the political context for his early congressional career, while the subsequent partisan realignment positioned him as an Anti-Jacksonian/Whig",
            "His founding of a politically prominent family — whose most famous member, his nephew Thomas Hendricks, became Vice President — reflected the family networks that sustained political dynasties in 19th-century Indiana"
        ],
        "effects": [
            "His 21-year unbroken career in high office (1816–1837) provided significant political continuity during Indiana's most formative decades — from early statehood through the Jacksonian era",
            "His departure from the governorship to the Senate triggered the constitutional succession that elevated James B. Ray to the governorship — a unique moment in Indiana constitutional history",
            "His Anti-Jacksonian/Whig opposition in the Senate contributed to Indiana's political pluralism during the Jacksonian era — helping establish an alternative political tradition to Democratic dominance in the state",
            "The Hendricks family political dynasty he founded culminated in his nephew Thomas Hendricks's Vice Presidency — making the Hendricks the most politically distinguished family in Indiana history"
        ],
        "relationships": [
            {"entity": "Indiana (early statehood)", "relationship": "GOVERNOR_AND_SENATOR", "note": "3rd Governor of Indiana (1822–1825); US Representative (1816–1822) and US Senator (1825–1837) — 21 consecutive years in high office"},
            {"entity": "Thomas Andrews Hendricks (Vice President)", "relationship": "UNCLE_OF", "note": "Uncle of Thomas Andrews Hendricks — who served as VP under Grover Cleveland — founding the most politically significant family in Indiana history"},
            {"entity": "James B. Ray (Indiana Governor)", "relationship": "PREDECESSOR_WHOSE_DEPARTURE_ELEVATED", "note": "His departure from the governorship to the Senate triggered the constitutional succession that elevated Senate president pro tempore James B. Ray to the governorship"},
            {"entity": "Andrew Jackson / Jacksonian Democracy", "relationship": "ANTI-JACKSONIAN_SENATE_OPPONENT_OF", "note": "Positioned himself as an Anti-Jacksonian in the Senate — opposing Jackson's Bank veto, Indian removal, and federal authority policies"},
            {"entity": "Indiana Democratic-Republican / Whig tradition", "relationship": "FOUNDING_FIGURE_OF", "note": "A founding figure of Indiana's National Republican and Whig political tradition — the alternative to Democratic dominance in the state"}
        ]
    }),

    # 3 — Marcus Morton
    ("marcus-morton", {
        "summary": (
            "Marcus Morton (1784–1864) was an American lawyer, jurist, and Democratic "
            "politician from Massachusetts who is best remembered for two facts about "
            "his political career that together form one of the most remarkable stories "
            "in American political history: he ran for Governor of Massachusetts "
            "eleven times before finally winning — and when he finally won (in 1839), "
            "he won by exactly one vote. The combination of a politician's singular "
            "determination and the narrowest possible margin of democratic victory "
            "made Morton a figure of both admiration and political legend.\n\n"
            "Morton's persistence was a product of his unusual political positioning: "
            "he was one of the very few committed Massachusetts Democrats in an era "
            "when the state was dominated first by Federalists and then overwhelmingly "
            "by the Whig Party. Massachusetts was the heartland of Whig politics in "
            "America — Daniel Webster's home state, the capital of New England "
            "commercial Federalism, and a state where Democrats were a consistent "
            "minority. Morton kept the Democratic Party alive in Massachusetts "
            "through his repeated candidacies — year after year building a minority "
            "coalition against Whig dominance.\n\n"
            "Beyond his governorship campaigns, Morton had a distinguished legal "
            "and judicial career: he served for 15 years as an Associate Justice of "
            "the Massachusetts Supreme Judicial Court (1825–1840) — the most "
            "respected common law court in New England — and he was later appointed "
            "Collector of the Port of Boston by President James K. Polk (1845–1849). "
            "He also served briefly as Acting Governor following the death of Governor "
            "William Eustis in 1825.\n\n"
            "His 1839 governorship — won by one vote — was followed by a second term "
            "(1843), making him the only Democrat to twice win the Massachusetts "
            "governorship in the Whig era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts Democratic governor who ran eleven times before winning — winning his 1839 election by exactly one vote; 15-year Associate Justice of the Massachusetts Supreme Judicial Court; kept the Democratic Party alive in heavily Whig Massachusetts through persistent candidacy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts's overwhelming Whig political dominance — the legacy of Federalist commercial culture and Daniel Webster's leadership — created the hostile political environment in which Morton's repeated Democratic candidacies were political acts of persistence against structural opposition",
            "His genuine commitment to Jacksonian Democratic principles — states' rights, agrarian democracy, opposition to privileged banking interests — sustained his candidacies through repeated defeats in a state where those principles were deeply unpopular",
            "The Massachusetts constitutional requirement of an absolute majority (not a plurality) in gubernatorial elections — which sent close elections to the legislature — created the specific mathematical mechanism that allowed Morton to finally win in 1839"
        ],
        "effects": [
            "His eleven gubernatorial campaigns — spanning decades — kept the Massachusetts Democratic Party organizationally alive during the long Whig dominance, providing the organizational continuity that later Democratic candidates could build on",
            "His victory by one vote in 1839 became one of the most celebrated examples of democratic persistence in American political folklore — a story that demonstrated that electoral persistence could ultimately overcome structural disadvantage",
            "His 15-year tenure on the Massachusetts Supreme Judicial Court contributed to the development of New England's most influential common law institution during the 1820s and 1830s",
            "His 1843 second term as governor demonstrated that his 1839 victory was not a fluke — that Massachusetts Democrats, though a permanent minority, could occasionally achieve gubernatorial power through coalition and Whig fragmentation"
        ],
        "relationships": [
            {"entity": "Massachusetts Democratic Party (Jacksonian era)", "relationship": "PERSISTENT_LEADER_OF", "note": "Kept the Massachusetts Democratic Party alive through eleven gubernatorial campaigns in a state overwhelmingly dominated by Federalists and then Whigs"},
            {"entity": "Massachusetts Supreme Judicial Court", "relationship": "ASSOCIATE_JUSTICE_FOR_15_YEARS", "note": "Served as Associate Justice of the Massachusetts Supreme Judicial Court (1825–1840) — one of the most respected common law courts in the United States"},
            {"entity": "Massachusetts governorship (1839 election)", "relationship": "WON_BY_ONE_VOTE_AFTER_11_ATTEMPTS", "note": "Won the governorship by exactly one vote in his 11th attempt — one of the narrowest and most celebrated gubernatorial victories in American history"},
            {"entity": "Whig Party (Massachusetts)", "relationship": "PERSISTENT_DEMOCRATIC_OPPONENT_OF", "note": "His repeated candidacies against Whig dominance in Massachusetts made him the defining Democratic opposition figure in the most Whig state in the nation"},
            {"entity": "President James K. Polk", "relationship": "APPOINTED_BY_AS_BOSTON_PORT_COLLECTOR", "note": "Appointed Collector of the Port of Boston by President Polk (1845–1849) — a federal patronage appointment rewarding his Democratic loyalty"}
        ]
    }),

    # 4 — Luther Martin
    ("luther-martin", {
        "summary": (
            "Luther Martin (1748–1826) was one of the most formidable lawyers of "
            "the American founding era — serving as Maryland's Attorney General for "
            "nearly three decades, standing as one of the most prominent Anti-Federalists "
            "at the Constitutional Convention of 1787, and building a reputation as "
            "the most feared trial lawyer at the American bar in the early republic. "
            "His career combined legal brilliance with political courage: he walked "
            "out of the Constitutional Convention because he believed the document "
            "being created dangerously concentrated power in the federal government "
            "at the expense of the states, and he spent years afterwards campaigning "
            "against its ratification.\n\n"
            "At the Constitutional Convention (1787), Martin was one of the most "
            "vocal delegates — speaking at length, often exhaustingly, against "
            "the emerging nationalist consensus. He objected to the large-state "
            "advantage in the proposed legislature, to the weakening of state "
            "sovereignty, and to the compromise over slavery. He left the Convention "
            "before the Constitution was signed and returned to Maryland to fight "
            "its ratification — publishing his influential 'Genuine Information' "
            "(1788), a detailed account of the Convention's proceedings from "
            "an Anti-Federalist perspective.\n\n"
            "His greatest legal triumph came in two of the most famous trials in "
            "early American history: he served as defense counsel in the impeachment "
            "trial of Supreme Court Justice Samuel Chase (1805) — successfully "
            "defending Chase and establishing the precedent that political disagreement "
            "was not grounds for impeachment — and as Aaron Burr's lead defense "
            "counsel in Burr's treason trial (1807), which resulted in Burr's "
            "acquittal under Chief Justice Marshall's narrow definition of treason.\n\n"
            "By the end of his career his alcoholism had severely impaired his "
            "faculties, but his earlier reputation as the American bar's most "
            "formidable advocate was secure."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Maryland's Attorney General for nearly 30 years; major Anti-Federalist at the 1787 Constitutional Convention — walked out and published influential Anti-Federalist account; defense counsel in Samuel Chase's impeachment trial (1805) and Aaron Burr's treason trial (1807); regarded as the most formidable trial lawyer of the early republic.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Constitutional Convention's debates over federal versus state power — and specifically the large-state advantage and the erosion of state sovereignty — created the political conflict that drove Martin to leave and publish his influential Anti-Federalist critique",
            "Maryland's legal and political culture — where Martin served as attorney general for nearly 30 years — provided the institutional base for his combined legal and political career",
            "The high-stakes political prosecutions of the early republic — the Chase impeachment and the Burr treason trial — created the constitutional moments in which Martin's skills as a trial advocate were brought to bear on the most significant cases in early American law"
        ],
        "effects": [
            "His successful defense of Samuel Chase in the 1805 impeachment trial established the precedent that political disagreement was not an impeachable offense — a landmark constitutional protection for judicial independence",
            "His defense of Aaron Burr in the 1807 treason trial contributed to the narrow definition of treason in American law under Chief Justice Marshall's ruling — protecting civil liberties against politically motivated treason prosecutions",
            "His 'Genuine Information' (1788) — a detailed Anti-Federalist account of the Constitutional Convention — provided one of the most detailed contemporary accounts of the Convention's proceedings and articulated the case against constitutional ratification",
            "His Anti-Federalist arguments at the Convention and in his published writings contributed to the demand for a Bill of Rights — the Anti-Federalist critique's most enduring constitutional legacy"
        ],
        "relationships": [
            {"entity": "Constitutional Convention (1787)", "relationship": "ANTI-FEDERALIST_DELEGATE_WHO_LEFT", "note": "A major delegate to the Constitutional Convention who left before the signing — believing the Constitution dangerously concentrated power in the federal government"},
            {"entity": "Aaron Burr treason trial (1807)", "relationship": "LEAD_DEFENSE_COUNSEL_IN", "note": "Served as Aaron Burr's lead defense attorney in his 1807 treason trial — which ended in acquittal under Marshall's narrow treason definition"},
            {"entity": "Samuel Chase impeachment trial (1805)", "relationship": "DEFENSE_COUNSEL_IN", "note": "Successfully defended Supreme Court Justice Samuel Chase in his 1805 impeachment trial — establishing that political disagreement was not grounds for impeachment"},
            {"entity": "Maryland Attorney General (office)", "relationship": "HOLDER_FOR_NEARLY_30_YEARS", "note": "Served as Maryland's Attorney General for nearly three decades — the institutional base of his combined legal and political career"},
            {"entity": "'Genuine Information' (1788) / Anti-Federalist Papers", "relationship": "AUTHOR_OF_INFLUENTIAL", "note": "Published 'Genuine Information' (1788) — a detailed Anti-Federalist account of the Constitutional Convention and argument against ratification"}
        ]
    }),

    # 5 — Caleb Strong
    ("caleb-strong", {
        "summary": (
            "Caleb Strong (1745–1819) was a Massachusetts Federalist lawyer and "
            "politician who was a delegate to the Constitutional Convention of 1787 "
            "— though illness forced him to leave before the Constitution was signed "
            "— and who served as the sixth and tenth Governor of Massachusetts "
            "(1800–1807 and 1812–1816), making him one of the few Federalists to "
            "win multiple governorships after the party's national collapse. His "
            "second gubernatorial term coincided with the War of 1812 and produced "
            "one of the most significant acts of Federalist state resistance in "
            "American history: Strong refused to call up the Massachusetts militia "
            "for federal service, challenging the constitutionality of federal "
            "authority over state militias and asserting Massachusetts's right to "
            "determine when its militia would be deployed.\n\n"
            "Strong's early career placed him at the center of American constitutional "
            "founding: he had helped draft the Massachusetts State Constitution of "
            "1779 — one of the most influential state constitutions, which provided "
            "a model for the federal Constitution — and his Constitutional Convention "
            "participation (before his illness-forced departure) contributed to the "
            "debates on federal structure. He was also a US Senator from Massachusetts "
            "(1789–1796) in the First through Fourth Congresses.\n\n"
            "His refusal to mobilize the Massachusetts militia for the War of 1812 "
            "was a constitutionally significant act of state resistance — going beyond "
            "political opposition to active constitutional confrontation with federal "
            "authority. The New England states' opposition to the War of 1812 climaxed "
            "in the Hartford Convention (1814–1815) — a Federalist conclave that "
            "discussed constitutional amendments and, some feared, potential secession — "
            "which occurred during Strong's second term.\n\n"
            "His career illustrates both the constitutional founding tradition "
            "and the Federalist resistance to executive war power."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Constitutional Convention delegate (1787); helped draft the Massachusetts Constitution (1779); US Senator (1789–1796); twice Governor of Massachusetts (1800–1807, 1812–1816); refused to mobilize the Massachusetts militia for the War of 1812 — one of the most significant acts of Federalist state resistance in American history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "His central role in Massachusetts constitutional politics — helping draft the 1779 Massachusetts Constitution and attending the Constitutional Convention — positioned him as a trusted Federalist statesman whose multiple governorships were grounded in constitutional legitimacy",
            "The War of 1812's deep unpopularity in New England — where it disrupted maritime commerce and was seen as unnecessary and unconstitutional — created the political mandate for Strong's refusal to mobilize the Massachusetts militia",
            "The constitutional ambiguity over federal versus state control of state militias created the legal grounds for Strong's refusal — he was not merely being politically obstructionist but was making a genuine constitutional argument about militia sovereignty"
        ],
        "effects": [
            "His refusal to mobilize the Massachusetts militia for the War of 1812 challenged the constitutionality of federal militia authority in a way that foreshadowed later federalism debates — including nullification — about the limits of federal power over state forces",
            "The Hartford Convention — which occurred during his second term — was the climax of New England's constitutional resistance to the War of 1812, and Strong's gubernatorial support gave it official state-level legitimacy",
            "His constitutional arguments about militia authority contributed to the developing jurisprudence of federal-state power sharing — the Supreme Court eventually addressed militia questions in Martin v. Mott (1827) after Strong's era",
            "His help in drafting the Massachusetts Constitution of 1779 — an influential document that combined the separation of powers, bicameralism, and judicial independence — contributed to the model that informed the federal Constitution"
        ],
        "relationships": [
            {"entity": "Constitutional Convention (1787)", "relationship": "DELEGATE_TO", "note": "A delegate to the Constitutional Convention — left before signing due to illness, but participated in the debates on federal structure"},
            {"entity": "Massachusetts Constitution (1779)", "relationship": "CO-DRAFTER_OF", "note": "Helped draft the Massachusetts Constitution of 1779 — one of the most influential state constitutions and a model for the federal Constitution"},
            {"entity": "War of 1812 militia refusal", "relationship": "STATE_RESISTANCE_LEADER_DURING", "note": "Refused to mobilize the Massachusetts militia for federal service during the War of 1812 — one of the most significant acts of Federalist state constitutional resistance"},
            {"entity": "Hartford Convention (1814–1815)", "relationship": "GOVERNOR_DURING", "note": "The Hartford Convention — the climax of New England's War of 1812 resistance — occurred during his second governorship; he gave it official state-level political legitimacy"},
            {"entity": "US Senate from Massachusetts (1789–1796)", "relationship": "EARLY_MEMBER_OF", "note": "Served as US Senator from Massachusetts (1789–1796) — in the First through Fourth Congresses — during the critical formative period of the federal government"}
        ]
    }),

    # 6 — Hamilton Rowan Gamble
    ("hamilton-rowan-gamble", {
        "summary": (
            "Hamilton Rowan Gamble (1798–1864) was an American jurist and politician "
            "from Missouri whose career bridged the antebellum slavery debates and "
            "the Civil War border-state crisis. As Chief Justice of the Missouri "
            "Supreme Court (1851–1852), he wrote a memorable dissent when his "
            "colleagues reversed the Missouri court's 28-year precedent of 'once "
            "free, always free' — which had been the legal basis for Dred Scott's "
            "own state court litigation — thereby helping propel the Dred Scott "
            "case to the federal courts. When Missouri's state government fractured "
            "under the secession crisis in 1861, Gamble emerged as the leader of "
            "the Unionist faction and was appointed Provisional Governor of Missouri "
            "(1861–1864) — serving as the political head of Missouri's continued "
            "adherence to the Union during the entire Civil War until his death.\n\n"
            "Missouri was one of the most contested border states in the Civil War — "
            "a slave state that remained formally in the Union but was deeply divided, "
            "with a secessionist-leaning governor (Claiborne Fox Jackson) who attempted "
            "to align Missouri with the Confederacy. When Jackson's government was "
            "forced out by Union forces, a state convention dominated by Unionists "
            "declared the governorship vacant and appointed Gamble — a moderate "
            "Unionist who had opposed Missouri's secession but also opposed the "
            "more radical abolitionist agenda of Missouri's Radical Republicans.\n\n"
            "Gamble's provisional governorship navigated the impossible politics "
            "of a Civil War border state — balancing the demands of the Lincoln "
            "administration, the Union military, radical Missouri Republicans, and "
            "the state's substantial pro-Confederate population. He resisted both "
            "Confederate secession and radical Republican policies, positioning "
            "Missouri as a conservative Unionist state.\n\n"
            "He died in office in January 1864 — having successfully kept Missouri "
            "in the Union throughout the war."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Provisional Governor of Missouri (1861–1864) who kept Missouri in the Union during the Civil War; as Chief Justice of the Missouri Supreme Court, wrote the dissent when the court reversed the 'once free, always free' precedent that had underpinned Dred Scott's state court case; died in office.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Missouri's precarious border-state position — a slave state with a divided population and a secessionist-leaning governor — created the political crisis that required a moderate Unionist leader to maintain the state's loyalty to the Union",
            "The Missouri Supreme Court's 1852 reversal of the 'once free, always free' precedent — which Gamble dissented from — helped propel the Dred Scott case to the federal courts and ultimately to the US Supreme Court",
            "Lincoln's need for moderate Unionist leaders in border states — who could maintain state loyalty without triggering pro-Confederate backlash — created the political demand for Gamble's moderate Unionism as provisional governor"
        ],
        "effects": [
            "His provisional governorship (1861–1864) successfully kept Missouri in the Union throughout the Civil War — a critical strategic achievement, as Missouri's loss would have severely threatened Union control of the Mississippi River",
            "His dissent in the 1852 Missouri Supreme Court case that reversed 'once free, always free' provided an early warning of the legal trajectory of the Dred Scott controversy — and his opinion was cited in the debates over the case",
            "His moderate Unionism — resisting both Confederate secession and radical Republican abolitionism — shaped Missouri's Civil War political identity as a conservative Unionist state rather than an abolitionist one",
            "His death in office (January 1864) left Missouri without its provisional governor at a critical moment — his successor Willard P. Hall had to manage the final year of war and the difficult transition to Reconstruction"
        ],
        "relationships": [
            {"entity": "Missouri (Civil War provisional governorship)", "relationship": "PROVISIONAL_GOVERNOR_1861-1864", "note": "Appointed Provisional Governor of Missouri by the state's Unionist convention — kept Missouri in the Union throughout the Civil War until his death in 1864"},
            {"entity": "Dred Scott case (state court precedent)", "relationship": "DISSENTED_FROM_COURT_REVERSAL_THAT_PROPELLED", "note": "His dissent from the Missouri Supreme Court's 1852 reversal of 'once free, always free' helped propel the Dred Scott case to the federal courts"},
            {"entity": "Abraham Lincoln (US President)", "relationship": "MODERATE_UNIONIST_PARTNER_OF", "note": "His moderate Unionist provisional governorship was the political partnership Lincoln needed to keep Missouri in the Union without triggering pro-Confederate backlash"},
            {"entity": "Governor Claiborne Fox Jackson (Confederate)", "relationship": "REPLACED_AS_GOVERNOR", "note": "His Unionist provisional government replaced the secessionist government of Governor Jackson — who had attempted to align Missouri with the Confederacy"},
            {"entity": "Missouri Radical Republicans", "relationship": "MODERATE_UNIONIST_IN_TENSION_WITH", "note": "His conservative Unionism placed him in ongoing tension with Missouri's Radical Republicans — who pushed for more aggressive abolitionist policies"}
        ]
    }),

    # 7 — Royall Tyler
    ("royall-tyler", {
        "summary": (
            "Royall Tyler (1757–1826) was an American lawyer, jurist, teacher, and "
            "playwright who holds a unique place in American cultural history as the "
            "author of The Contrast (1787) — the first American comedy to be "
            "professionally performed on the American stage. Born in Boston and a "
            "Harvard graduate (1776), Tyler served in the Massachusetts militia "
            "during the American Revolution and played a minor role in the suppression "
            "of Shays' Rebellion (1787) — an experience that brought him to "
            "New York, where he wrote The Contrast in a matter of weeks and saw "
            "it performed at the John Street Theatre in April 1787.\n\n"
            "The Contrast was a cultural landmark: it introduced the archetypal "
            "American character of Jonathan the Yankee — the plain-spoken, honest "
            "American countryman contrasted with the affected, Anglophile manners "
            "of the play's villain — and asserted an American theatrical identity "
            "distinct from British theatrical culture. Written at the moment of the "
            "Constitutional Convention, The Contrast's cultural nationalism paralleled "
            "the political nationalism being debated in Philadelphia.\n\n"
            "Tyler's legal career was equally distinguished: after relocating to "
            "Vermont, he served as State's Attorney for Windham County, was a "
            "professor of jurisprudence at the University of Vermont, and in 1801 "
            "was appointed a Justice of the Vermont Supreme Court — serving as "
            "Chief Justice from 1807 to 1813. His legal career in Vermont's formative "
            "legal period contributed to the development of Vermont's common law "
            "tradition.\n\n"
            "He was one of the very few American founders who was simultaneously "
            "a distinguished legal professional and a significant literary figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Author of The Contrast (1787) — the first American comedy professionally performed on stage; Harvard graduate, Revolutionary War militiaman, Vermont Supreme Court Justice (1801–1813) and Chief Justice (1807–1813); professor of jurisprudence at UVM; a rare founder who was both legal professional and literary pioneer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution's assertion of cultural as well as political independence — and the desire for an American theatrical identity distinct from British theatrical culture — created the cultural demand that Tyler's The Contrast fulfilled",
            "Shays' Rebellion (1787) — which brought Tyler to New York as part of the Massachusetts militia response — provided the immediate circumstance in which he encountered New York theatrical culture and wrote The Contrast in weeks",
            "Vermont's early statehood period (admitted 1791) required the development of legal institutions — including courts and legal education — creating the professional opportunities that anchored Tyler's legal career in the state"
        ],
        "effects": [
            "The Contrast (1787) established the 'Yankee' as an American theatrical archetype — the plain-spoken, honest American contrasted with Anglophile affectation — and inaugurated the tradition of American comedy on the professional stage",
            "His Vermont Supreme Court tenure (1801–1813) and Chief Justiceship (1807–1813) contributed to the development of Vermont's common law tradition during the state's formative legal period",
            "His professorship of jurisprudence at the University of Vermont contributed to the institutionalization of legal education in New England — helping establish law as an academic discipline in the region",
            "His dual legacy as lawyer-jurist and playwright established a model of the cultivated American professional who contributed to both legal and cultural life — a combination unusual in the specialized professions of the 19th century"
        ],
        "relationships": [
            {"entity": "The Contrast (play, 1787)", "relationship": "AUTHOR_OF", "note": "Author of The Contrast (1787) — the first American comedy professionally performed on stage, at the John Street Theatre, New York"},
            {"entity": "Vermont Supreme Court", "relationship": "CHIEF_JUSTICE_OF_1807-1813", "note": "Served as Vermont Supreme Court Justice (1801–1813) and Chief Justice (1807–1813) — contributing to Vermont's formative common law development"},
            {"entity": "Shays' Rebellion (1787)", "relationship": "MILITIA_PARTICIPANT_IN", "note": "Served in the Massachusetts militia response to Shays' Rebellion — an experience that brought him to New York and led to The Contrast's creation"},
            {"entity": "University of Vermont", "relationship": "PROFESSOR_OF_JURISPRUDENCE_AT", "note": "Professor of jurisprudence at the University of Vermont — helping establish legal education in New England as an academic discipline"},
            {"entity": "American theatrical tradition", "relationship": "PIONEER_OF", "note": "The Contrast established the first professionally performed American comedy and the 'Yankee' theatrical archetype — launching the American stage theatrical tradition"}
        ]
    }),

    # 8 — John Sullivan
    ("john-sullivan", {
        "summary": (
            "Major General John Sullivan (1740–1795) was an American Continental Army "
            "officer, lawyer, and politician from New Hampshire who participated in "
            "many of the most consequential events of the American Revolutionary War "
            "— and whose mixed military record was nevertheless distinguished by "
            "two historically significant operations: his presence at George Washington's "
            "famous crossing of the Delaware River (December 26, 1776) and the "
            "subsequent battles of Trenton and Princeton, and his command of the "
            "Sullivan-Clinton Campaign of 1779 — one of the most controversial "
            "military operations of the Revolutionary War.\n\n"
            "Sullivan was one of the Continental Army's major generals from its "
            "earliest formation — appointed by the Continental Congress in 1775 — "
            "and he participated in the siege of Boston, the failed Quebec Expedition, "
            "the Battle of Long Island (where he was captured and briefly held by "
            "the British), and Washington's critical New Jersey campaigns. His "
            "military career was marked by personal courage and tactical energy "
            "but also by controversies — he feuded with the Marquis de Lafayette "
            "during the failed Franco-American assault on Newport (1778).\n\n"
            "The Sullivan-Clinton Campaign (1779) — ordered by Washington to destroy "
            "the Iroquois Confederacy's power — sent Sullivan's forces through the "
            "Iroquois heartland in western New York, burning forty Iroquois towns, "
            "destroying crops and orchards, and forcing a massive displacement of "
            "Iroquois peoples. The campaign's strategic objective was to end Iroquois "
            "raids on the New York and Pennsylvania frontier, but it also caused "
            "catastrophic suffering among the Iroquois nations.\n\n"
            "Sullivan retired from the army in 1779 and resumed his New Hampshire "
            "political career — serving three terms as governor and as one of "
            "New Hampshire's founding federal figures."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Continental Army Major General; present at the crossing of the Delaware (1776) and the battles of Trenton and Princeton; commanded the Sullivan-Clinton Campaign (1779) that devastated the Iroquois Confederacy; three times Governor of New Hampshire; delegate to the Continental Congress.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Continental Congress's need for experienced military commanders in 1775 — and Sullivan's prior legal and political career in New Hampshire — led to his appointment as one of the Continental Army's original major generals",
            "The Iroquois Confederacy's continued raids on the New York and Pennsylvania frontier — conducted in alliance with British forces and Loyalists — created the military justification for Washington's order of the Sullivan-Clinton Campaign",
            "New Hampshire's prominent role in the Revolutionary War — as one of the most committed Patriot states — created the political base for Sullivan's post-war gubernatorial career"
        ],
        "effects": [
            "The Sullivan-Clinton Campaign (1779) devastated the Iroquois Confederacy's heartland — burning forty towns and forcing massive population displacement — weakening the Confederacy's military capacity but also causing catastrophic suffering among the Iroquois nations",
            "His presence at Washington's Delaware crossing and the battles of Trenton and Princeton contributed to one of the most critical military turnarounds of the Revolutionary War — the victories that revived Continental Army morale in the winter of 1776–1777",
            "His three terms as Governor of New Hampshire contributed to the state's political development during the formative period of American federal and state governance",
            "The Sullivan-Clinton Campaign's destruction of the Iroquois heartland accelerated post-war American settlement of western New York — the cleared territory was rapidly occupied by American settlers after the Revolution"
        ],
        "relationships": [
            {"entity": "George Washington (Continental Army commander)", "relationship": "MAJOR_GENERAL_UNDER", "note": "One of the Continental Army's original major generals — served under Washington at the Delaware crossing, Trenton, Princeton, and later campaigns"},
            {"entity": "Sullivan-Clinton Campaign (1779)", "relationship": "COMMANDING_GENERAL_OF", "note": "Commanded the Sullivan-Clinton Campaign — ordered by Washington to destroy Iroquois military power — which burned forty towns in the Iroquois heartland"},
            {"entity": "Iroquois Confederacy (Six Nations)", "relationship": "MILITARY_CAMPAIGN_AGAINST", "note": "His campaign devastated the Iroquois Confederacy's heartland — burning towns, destroying crops, and forcing massive population displacement"},
            {"entity": "Battle of Trenton / Crossing of the Delaware (1776)", "relationship": "PARTICIPANT_IN", "note": "Present at Washington's famous crossing of the Delaware (December 1776) and the subsequent victories at Trenton and Princeton"},
            {"entity": "New Hampshire (governorship)", "relationship": "THREE_TERM_GOVERNOR_OF", "note": "Served three terms as Governor of New Hampshire — a major post-war political career that established him as the state's most prominent Revolutionary War figure"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 29)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
