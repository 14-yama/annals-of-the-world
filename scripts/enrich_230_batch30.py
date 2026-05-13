#!/usr/bin/env python3
"""
Batch 30 — 8 entities: John J. Crittenden, Edmund Pendleton, George Catlin,
Thomas Beaufort Duke of Exeter, Francis Granger, Ninian Edwards,
Josiah S. Johnston, Thomas Lowndes
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

    # 1 — John J. Crittenden
    ("john-j-crittenden", {
        "summary": (
            "John Jordan Crittenden (1787–1863) was one of the most experienced "
            "American statesmen of the 19th century — a Kentucky lawyer who served "
            "multiple terms in the US Senate, as US Attorney General under three "
            "presidents (William Henry Harrison, John Tyler, and Millard Fillmore), "
            "as Governor of Kentucky, and as a US Representative — and who is "
            "best remembered for his final great act: the Crittenden Compromise "
            "of December 1860, the last major legislative attempt to prevent the "
            "Civil War by extending the Missouri Compromise line to the Pacific "
            "and guaranteeing slavery's constitutional protection in states where "
            "it existed. The Compromise failed, rejected by Republican senators "
            "on Lincoln's instructions — and the war followed.\n\n"
            "Crittenden's career was built on the border-state Whig tradition of "
            "Henry Clay — he was one of Clay's closest political allies and heirs "
            "in Kentucky. Like Clay, he sought to find compromises that would preserve "
            "the Union while accommodating Southern slaveholder interests — the "
            "quintessential border-state political philosophy. His multiple tenures "
            "as Attorney General reflected his reputation for legal competence and "
            "trustworthiness across party lines — he served under a Whig (Harrison), "
            "a states' rights Democrat masquerading as a Whig (Tyler), and a moderate "
            "Whig (Fillmore).\n\n"
            "His personal tragedy was that both of his sons chose opposite sides "
            "in the Civil War he had tried to prevent: one became a Union general "
            "and the other a Confederate general — a microcosm of the border-state "
            "family divisions the Civil War created.\n\n"
            "He served in the US House in his final years (1861–1863), dying in "
            "office during the war he had failed to stop."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Kentucky statesman who proposed the Crittenden Compromise (December 1860) — the last major legislative attempt to prevent the Civil War; US AG under three presidents; multiple times US Senator and Governor of Kentucky; Henry Clay's political heir; both sons fought on opposite sides of the Civil War.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Kentucky's border-state political culture — deeply invested in Union preservation but also in the protection of slaveholder interests — created the political environment that shaped Crittenden's Unionist compromise philosophy",
            "Henry Clay's legacy of compromise — the Missouri Compromise (1820), the Compromise of 1850 — created the tradition within which Crittenden positioned himself as Clay's heir and the champion of a final compromise to prevent secession",
            "The secession crisis of 1860–1861 — triggered by Lincoln's election — created the desperate political urgency that drove Crittenden's last compromise proposal: extending the Missouri Compromise line to the Pacific"
        ],
        "effects": [
            "The failure of the Crittenden Compromise — rejected by Republicans on Lincoln's instructions — marked the last realistic legislative opportunity to prevent the Civil War; its rejection effectively made armed conflict inevitable",
            "His personal tragedy — sons fighting on opposite sides — became emblematic of the Civil War's destruction of border-state family unity and a widely cited symbol of the war's fratricidal nature",
            "His multiple AG tenures contributed to the development of the Attorney General's office across three administrations — helping establish the office's non-partisan legal advisory function",
            "His position as Clay's political heir kept the border-state Whig tradition of Union preservation and compromise alive in Kentucky politics through the sectional crisis"
        ],
        "relationships": [
            {"entity": "Crittenden Compromise (December 1860)", "relationship": "AUTHOR_OF", "note": "Proposed the Crittenden Compromise — extending the Missouri Compromise line to the Pacific — the last major legislative attempt to prevent the Civil War"},
            {"entity": "Henry Clay (Kentucky statesman)", "relationship": "POLITICAL_HEIR_AND_ALLY_OF", "note": "One of Clay's closest political allies and his heir as Kentucky's leading Whig statesman — continuing Clay's tradition of Union-preserving compromise"},
            {"entity": "US Attorney General (office)", "relationship": "SERVED_THREE_TIMES_AS", "note": "US AG under William Henry Harrison (1841), John Tyler (1841), and Millard Fillmore (1850–1853) — one of the few men to serve as AG under three presidents"},
            {"entity": "Abraham Lincoln / Republican Party", "relationship": "COMPROMISE_REJECTED_BY", "note": "His Crittenden Compromise was rejected by Republican senators on Lincoln's instructions — the failure that made the Civil War effectively inevitable"},
            {"entity": "Civil War (border-state family divisions)", "relationship": "PERSONAL_SYMBOL_OF", "note": "Both his sons fought on opposite sides — one Union general, one Confederate general — making his family a microcosm of the border-state divisions the war created"}
        ]
    }),

    # 2 — Edmund Pendleton
    ("edmund-pendleton", {
        "summary": (
            "Edmund Pendleton (1721–1803) was a Virginia planter, lawyer, judge, "
            "and statesman who played foundational roles at every stage of Virginia's "
            "Revolutionary and constitutional history — from the colonial legislature "
            "through the creation of the American republic. He was the first Speaker "
            "of the Virginia House of Delegates (the renamed colonial legislature) "
            "after independence, president of the Virginia Committee of Safety during "
            "the Revolution's most critical early phase, a delegate to the First "
            "Continental Congress, and president of Virginia's 1788 ratification "
            "convention — where he presided over the most consequential constitutional "
            "debate in American history, as Virginia's delegates argued over whether "
            "to adopt the federal Constitution.\n\n"
            "Virginia's 1788 ratification convention was the great constitutional "
            "drama of the founding era: it pitted James Madison and John Marshall "
            "for the Constitution against Patrick Henry, George Mason, and Richard "
            "Henry Lee against it. Pendleton, as president of the convention, "
            "provided the institutional framework for that debate — and as a moderate "
            "Federalist, he supported ratification. Virginia's narrow vote for "
            "ratification (89 to 79) secured the Constitution's survival, as "
            "Virginia was the most populous state and its rejection might have "
            "doomed the new framework.\n\n"
            "In Virginia's legal system, Pendleton served as president of the "
            "Virginia Court of Appeals — effectively the state's chief justice — "
            "for the final two decades of his life (1779–1803). He was one of "
            "the primary architects of the post-colonial Virginia legal system, "
            "working alongside Thomas Jefferson and George Wythe on the revision "
            "of Virginia's laws after independence.\n\n"
            "Patrick Henry called him 'the ablest man I ever met with in debate' — "
            "a remarkable tribute from the era's greatest orator."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Virginia's first Speaker of the House of Delegates; president of the Virginia Committee of Safety; delegate to the First Continental Congress; presided over Virginia's 1788 Constitutional ratification convention; president of the Virginia Court of Appeals (1779–1803); Patrick Henry called him 'the ablest man I ever met with in debate.'",
            "significanceCategory": "continental"
        },
        "causes": [
            "Virginia's central importance in American revolutionary politics — as the most populous colony and the home of Washington, Jefferson, Madison, and Marshall — created the political environment in which Pendleton's long leadership was essential to revolutionary organization",
            "The Constitutional Convention's debates and the subsequent ratification struggle created the constitutional moment in which Pendleton's role as president of Virginia's ratification convention placed him at the center of the most consequential debate in American history",
            "Virginia's need to rebuild its legal system from colonial to republican foundations — working alongside Jefferson and Wythe — created the institutional reform work that defined Pendleton's final decades"
        ],
        "effects": [
            "His presidency of Virginia's 1788 ratification convention — and his support for the Constitution — contributed to Virginia's narrow vote for ratification (89 to 79), which was critical to the Constitution's adoption",
            "His 24-year presidency of the Virginia Court of Appeals contributed to the development of Virginia's post-colonial legal system — working alongside Jefferson and Wythe to reshape Virginia's laws on republican principles",
            "His role as first Speaker of the Virginia House of Delegates helped establish the institutional continuity of Virginia's legislature through the revolutionary transition from colonial to republican governance",
            "Patrick Henry's tribute — 'the ablest man I ever met with in debate' — reflects Pendleton's standing as one of the great legal minds of the founding generation, a recognition that shaped his lasting historical reputation"
        ],
        "relationships": [
            {"entity": "Virginia's Constitutional Ratification Convention (1788)", "relationship": "PRESIDED_OVER_AS_PRESIDENT", "note": "Presided over Virginia's 1788 ratification convention — the most consequential constitutional debate of the founding era, where Virginia's narrow vote secured the Constitution"},
            {"entity": "Virginia Court of Appeals", "relationship": "PRESIDENT_FOR_24_YEARS", "note": "Served as president (chief justice) of the Virginia Court of Appeals (1779–1803) — Virginia's highest court — for the final decades of his career"},
            {"entity": "Virginia Committee of Safety (Revolutionary War)", "relationship": "PRESIDENT_OF", "note": "Presided over Virginia's Committee of Safety during the Revolution's critical early phase — the executive body that governed Virginia before a formal state government was established"},
            {"entity": "Thomas Jefferson / George Wythe", "relationship": "CO-REVISORS_OF_VIRGINIA_LAW_WITH", "note": "Worked alongside Jefferson and Wythe on the revision of Virginia's laws after independence — helping reshape the colonial legal system on republican principles"},
            {"entity": "Patrick Henry (Virginia orator)", "relationship": "PRAISED_AS_ABLEST_DEBATER_BY", "note": "Patrick Henry — Virginia's greatest orator — called Pendleton 'the ablest man I ever met with in debate,' a tribute that cemented his historical reputation"}
        ]
    }),

    # 3 — George Catlin
    ("george-catlin", {
        "summary": (
            "George Catlin (1796–1872) was an American lawyer turned painter, author, "
            "and traveler who dedicated his life to documenting the cultures, portraits, "
            "and lifeways of the Native American peoples of the American West — "
            "producing one of the largest and most historically significant visual "
            "records of pre-reservation Plains Indian life ever created. Trained as "
            "a lawyer and admitted to the Pennsylvania bar, Catlin abandoned the law "
            "in 1821 to pursue painting — and after seeing a delegation of Plains "
            "Indians visiting Philadelphia, he resolved to create a definitive "
            "documentary record of Native American peoples before their cultures "
            "were permanently destroyed by American westward expansion.\n\n"
            "Between 1830 and 1836, Catlin traveled to the American West five times, "
            "visiting approximately 50 different tribes and painting more than 500 "
            "portraits and scenes of Native American life. His subjects included "
            "Lakota, Mandan, Osage, Crow, Blackfeet, and dozens of other nations — "
            "recorded with remarkable ethnographic detail at a critical historical "
            "moment, as many of these cultures were being rapidly disrupted by "
            "disease, dispossession, and forced relocation. His portraits of Mandan "
            "leaders proved particularly valuable — the Mandan nation was nearly "
            "destroyed by a smallpox epidemic in 1837-1838, shortly after Catlin "
            "had documented their culture.\n\n"
            "He published 'Letters and Notes on the Manners, Customs, and Conditions "
            "of the North American Indians' (1841) — the most comprehensive "
            "ethnographic account of Plains Indian cultures yet produced — and "
            "toured 'Catlin's Indian Gallery' as a traveling exhibition in the "
            "United States and Europe. He also proposed the creation of a 'nation's "
            "park' to preserve wilderness and indigenous peoples — an idea that "
            "prefigured the national parks movement.\n\n"
            "His legacy is complex: a genuine champion of indigenous cultures who "
            "also romanticized and exoticized them for Western audiences."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Lawyer turned painter who created the largest visual documentary record of pre-reservation Plains Indian life — 500+ paintings of ~50 tribes (1830–1836); author of 'Letters and Notes on the North American Indians' (1841); proposed the concept of national parks; documented the Mandan nation just before its near-destruction by smallpox (1837–1838).",
            "significanceCategory": "continental"
        },
        "causes": [
            "His encounter with a delegation of Plains Indians visiting Philadelphia — which struck him with the beauty and fragility of their cultures — motivated his radical career change from law to the documentary painting project that consumed his life",
            "American westward expansion's catastrophic effect on Native American cultures — through disease, dispossession, and forced relocation — created both the urgency and the historical tragedy that defined Catlin's documentation mission",
            "The emerging American cultural nationalism of the early republic — which sought distinctly American subjects for art — created a receptive audience for Catlin's Native American portraits as both artistic and documentary achievements"
        ],
        "effects": [
            "His 500+ paintings of approximately 50 different Native American nations created an irreplaceable visual and ethnographic record of pre-reservation Plains Indian life — documenting cultures that were being rapidly destroyed by disease and dispossession",
            "His documentation of the Mandan nation (1832) proved especially precious: the Mandan were nearly wiped out by smallpox in 1837–1838 — shortly after Catlin's visit — making his portraits the primary surviving visual record of their culture",
            "His 'Letters and Notes' (1841) was the most comprehensive English-language ethnographic account of Plains Indian cultures yet produced — shaping European and American understanding of Native American life for decades",
            "His proposal for a 'nation's park' — to preserve wilderness and indigenous peoples — prefigured the national parks concept that Yellowstone (1872) would inaugurate, making him an intellectual precursor to the conservation movement"
        ],
        "relationships": [
            {"entity": "Plains Indian nations (Lakota, Mandan, Crow, Blackfeet, etc.)", "relationship": "PRIMARY_DOCUMENTER_OF", "note": "Visited approximately 50 different nations and painted 500+ portraits and scenes of Plains Indian life — creating the most comprehensive visual record of pre-reservation Native American cultures"},
            {"entity": "Mandan nation", "relationship": "DOCUMENTED_JUST_BEFORE_NEAR-DESTRUCTION_OF", "note": "His 1832 paintings of the Mandan became the primary surviving visual record of their culture — the nation was nearly destroyed by smallpox in 1837–1838"},
            {"entity": "'Letters and Notes on the North American Indians' (1841)", "relationship": "AUTHOR_OF", "note": "Published the most comprehensive ethnographic account of Plains Indian cultures in English — shaping understanding of Native American life for decades"},
            {"entity": "National parks concept", "relationship": "INTELLECTUAL_PRECURSOR_OF", "note": "Proposed a 'nation's park' to preserve wilderness and indigenous peoples — prefiguring the national parks movement that created Yellowstone in 1872"},
            {"entity": "Pennsylvania bar / legal career", "relationship": "ABANDONED_TO_PURSUE_PAINTING", "note": "Trained as a lawyer and admitted to the Pennsylvania bar — abandoned the law in 1821 to pursue the documentary painting mission that defined his career"}
        ]
    }),

    # 4 — Thomas Beaufort, Duke of Exeter
    ("thomas-beaufort-duke-of-exeter", {
        "summary": (
            "Thomas Beaufort, Duke of Exeter (c.1377–1426), was a prominent English "
            "military commander and royal administrator during the Hundred Years' War "
            "whose career was shaped by his exceptional but legally complicated "
            "origins: he was the third child of John of Gaunt, Duke of Lancaster, "
            "and his mistress (later wife) Katherine Swynford — making him a half-brother "
            "of King Henry IV and a half-uncle of King Henry V. His illegitimate "
            "birth was a political liability that Parliament later resolved by "
            "retroactively legitimizing the Beaufort children, though with the "
            "stipulation that they were excluded from royal succession — a limitation "
            "whose full consequences would be felt by the next Beaufort generation.\n\n"
            "Beaufort's career combined military command and high royal office: he "
            "served as Admiral of England (1407–1412), as Chancellor of England "
            "(1410–1412) — the kingdom's chief administrative officer — and as "
            "Captain-General of Normandy during the crucial phase of Henry V's "
            "reconquest of France. He was a distinguished battlefield commander "
            "who participated in the siege of Harfleur (1415) and in the Agincourt "
            "campaign, and who subsequently played a major role in Henry V's "
            "consolidation of the Normandy conquest after Agincourt.\n\n"
            "He was also a trusted guardian of the young Henry VI after Henry V's "
            "premature death in 1422, serving on the regency council that governed "
            "England while the infant king came of age. His standing as both a "
            "senior royal relative and an experienced military commander made him "
            "one of the most important figures in the regency government.\n\n"
            "The Beaufort family's complicated legacy — powerful, legitimate enough "
            "to govern but excluded from direct succession — would eventually "
            "contribute to the Wars of the Roses."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Illegitimate son of John of Gaunt (legitimized but excluded from succession); half-brother of Henry IV, half-uncle of Henry V; Chancellor of England (1410–1412); Admiral of England; commanded forces in Henry V's Normandy campaign including Agincourt; guardian of young Henry VI.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His birth as the illegitimate son of John of Gaunt — and his subsequent legitimization by Parliament but exclusion from royal succession — created the complex political status that defined his career and the Beaufort family's position",
            "Henry V's reconquest of France — the Hundred Years' War's greatest English military campaign — created the military operations in which Beaufort's command experience was deployed as Captain-General of Normandy",
            "Henry V's premature death in 1422 and the accession of the infant Henry VI created the regency crisis that placed Beaufort on the regency council as a senior royal relative with military credibility"
        ],
        "effects": [
            "His service as Chancellor of England contributed to the administrative governance of the kingdom during the critical years of Henry V's French campaigns — managing domestic affairs while the king campaigned abroad",
            "His military service in the Agincourt campaign and Normandy consolidation contributed to the English occupation of Normandy that was at its height during the 1420s",
            "His role on the regency council for Henry VI contributed to the governance of England during the critical minority — though the regency period also planted the seeds of the factional conflicts that would become the Wars of the Roses",
            "The Beaufort family's exclusion from royal succession — established for Thomas and his siblings — became a source of future dynastic conflict as the Beauforts' descendants later pressed claims during the Wars of the Roses"
        ],
        "relationships": [
            {"entity": "John of Gaunt, Duke of Lancaster", "relationship": "ILLEGITIMATE_SON_OF", "note": "Born the illegitimate son of John of Gaunt and Katherine Swynford — later legitimized by Parliament but excluded from royal succession"},
            {"entity": "King Henry V of England", "relationship": "HALF-UNCLE_AND_MILITARY_COMMANDER_UNDER", "note": "Half-uncle of Henry V and served as Captain-General of Normandy during Henry V's reconquest of France — including the Agincourt campaign"},
            {"entity": "Hundred Years' War (English conquest of Normandy)", "relationship": "MILITARY_COMMANDER_IN", "note": "Participated in the Agincourt campaign (1415) and served as Captain-General of Normandy during the consolidation of the English conquest"},
            {"entity": "Chancellor of England (1410–1412)", "relationship": "SERVED_AS", "note": "Served as Chancellor of England (1410–1412) — the kingdom's chief administrative officer — during the critical period of Henry V's rise to power"},
            {"entity": "Henry VI regency council", "relationship": "MEMBER_OF", "note": "Served on the regency council for the infant Henry VI after Henry V's premature death in 1422 — a trusted senior royal figure and military veteran"}
        ]
    }),

    # 5 — Francis Granger
    ("francis-granger", {
        "summary": (
            "Francis Granger (1792–1868) was a New York lawyer and politician who "
            "was a leading figure in both the Anti-Masonic Party and the Whig Party "
            "— serving multiple terms in the US House of Representatives and holding "
            "the position of US Postmaster General under President William Henry "
            "Harrison (briefly, in 1841, before Harrison's death and Tyler's ascension). "
            "His career encapsulated the political trajectory of anti-Jacksonian "
            "reform politics in New York — from the Anti-Masonic movement of the "
            "late 1820s and early 1830s through the formation of the Whig coalition "
            "that dominated American politics in the 1840s.\n\n"
            "The Anti-Masonic movement was one of the most distinctive episodes in "
            "American political history: triggered by the 1826 disappearance and "
            "presumed murder of William Morgan (who had threatened to expose "
            "Masonic secrets in New York) and the subsequent public outrage over "
            "what was seen as Masonic influence protecting the perpetrators, it "
            "grew into the first significant third party in American politics — "
            "running its own presidential candidates and winning several state "
            "governorships before being absorbed into the Whig Party. Granger "
            "was a prominent New York Anti-Masonic leader who helped build "
            "the party's organizational infrastructure.\n\n"
            "In the 1836 presidential election, Granger was one of multiple Whig "
            "vice-presidential candidates running under the unusual Whig strategy "
            "of running different regional candidates — he received 77 electoral "
            "votes for vice president, but the election was thrown to the Senate "
            "(which selected Richard Mentor Johnson) — one of only two times the "
            "Senate has chosen a VP.\n\n"
            "He later served as postmaster general in the extremely brief Harrison "
            "administration before Tyler's succession changed the political character "
            "of the government."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Leading New York Anti-Masonic and Whig politician; US Postmaster General under Harrison (1841); received 77 VP electoral votes in 1836 — the election thrown to the Senate (which chose Richard Mentor Johnson) — one of only two Senate VP selections in American history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Anti-Masonic movement — triggered by the Morgan Affair in 1826 — created the political wave in New York that launched Granger's career as one of the movement's leading organizers and candidates",
            "New York's central importance in American electoral politics — as the most populous state with the largest electoral vote — made Granger's leadership of the state's Anti-Masonic and Whig organizations politically significant",
            "The Whig strategy of running multiple regional VP candidates in 1836 — designed to deny Martin Van Buren an electoral majority and throw the election to the House — created the unusual situation where Granger received 77 VP electoral votes without being elected"
        ],
        "effects": [
            "His leadership of the Anti-Masonic Party in New York contributed to the party's organizational infrastructure and its eventual absorption into the Whig coalition — helping build the anti-Jacksonian political network",
            "His 77 electoral votes for vice president in 1836 — sending the VP election to the Senate — produced one of only two instances in American history of the Senate selecting a VP, establishing an unusual constitutional precedent",
            "His brief Postmaster General tenure under Harrison (March–April 1841) — ended by Tyler's ascension and the subsequent Whig cabinet resignations — reflected the political disruption that Tyler's accession caused to the Harrison Whig agenda",
            "His long congressional career contributed to the Whig Party's congressional presence in New York — one of the anti-Jacksonian party's most important state delegations"
        ],
        "relationships": [
            {"entity": "Anti-Masonic Party (New York)", "relationship": "LEADING_FIGURE_OF", "note": "A leading New York Anti-Masonic Party organizer and politician — helping build one of the first significant third parties in American history"},
            {"entity": "1836 Vice Presidential election (Senate selection)", "relationship": "VP_CANDIDATE_WHO_TRIGGERED", "note": "Received 77 VP electoral votes in 1836 — the election was thrown to the Senate (which selected Johnson) — one of only two Senate VP selections in American history"},
            {"entity": "US Postmaster General (office)", "relationship": "BRIEFLY_SERVED_AS", "note": "Served as US Postmaster General under Harrison (1841) — before Harrison's death and Tyler's ascension ended the Harrison Whig administration"},
            {"entity": "William Henry Harrison (US President)", "relationship": "POSTMASTER_GENERAL_UNDER", "note": "Harrison's choice as Postmaster General — part of the Whig cabinet that was disrupted by Harrison's death after one month in office"},
            {"entity": "Whig Party (New York)", "relationship": "LEADING_MEMBER_OF", "note": "A leading New York Whig politician after the Anti-Masonic movement merged into the Whig coalition — contributing to the Whig Party's dominant New York organization"}
        ]
    }),

    # 6 — Ninian Edwards
    ("ninian-edwards", {
        "summary": (
            "Ninian Edwards (1775–1833) was an American politician and jurist who "
            "served as the first and only Governor of Illinois Territory (1809–1818) "
            "— the entire duration of Illinois's territorial period — and then as "
            "one of the first two United States Senators from the new State of "
            "Illinois (1818–1824), making him the single individual who dominated "
            "Illinois's political leadership from territorial organization through "
            "early statehood. He later served as Governor of the State of Illinois "
            "(1826–1830), completing a career that made him the most prominent "
            "figure in Illinois's founding political generation.\n\n"
            "Edwards came to Illinois from Kentucky, where he had served as a judge, "
            "and he brought with him the Kentucky-Virginia political culture of "
            "frontier Democratic-Republicanism that shaped the early Illinois "
            "political establishment. His territorial governorship coincided with "
            "the War of 1812 — during which he had to manage Illinois Territory's "
            "security against Native American raids associated with the British "
            "alliance — and with the rapid settlement of Illinois's fertile lands.\n\n"
            "His personal connection to the Lincoln family is historically notable: "
            "his son Ninian Wirt Edwards married Elizabeth Todd — Mary Todd's "
            "sister — and it was at the Edwards house in Springfield that Abraham "
            "Lincoln and Mary Todd first met and courted. The Edwardses were thus "
            "part of the extended family network of the Lincoln household.\n\n"
            "His political career ended in controversy: he was implicated in the "
            "'A.B. Plot' — a controversy over Treasury Department misconduct — "
            "which damaged his reputation and contributed to the end of his "
            "political influence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First and only Governor of Illinois Territory (1809–1818); one of Illinois's first two US Senators (1818–1824); Governor of Illinois (1826–1830); father-in-law of Elizabeth Todd (Mary Todd's sister) — his house was where Lincoln and Mary Todd first met.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Illinois Territory's organization in 1809 — carved from Indiana Territory — required a territorial governor, and Edwards's judicial and political experience in Kentucky made him an appropriate choice for the appointment",
            "Illinois's rapid settlement during the early 19th century — driven by the fertility of its prairie lands and the post-1815 peace — created the demographic pressure for statehood that his territorial governorship had to manage",
            "The extended Todd family network — which connected Edwards through his son's marriage to Elizabeth Todd — linked the Edwards political dynasty to the Lincoln family in ways that had lasting personal significance"
        ],
        "effects": [
            "His 9-year territorial governorship provided the political continuity and leadership that Illinois needed during its transition from frontier territory to established state — managing the War of 1812 security crisis and the pre-statehood settlement surge",
            "His first Senate term contributed to Illinois's representation in Congress during the critical early statehood period — establishing the state's legislative presence in Washington",
            "His family's connection to the Todd household — through his son's marriage to Elizabeth Todd — made the Edwards house in Springfield a social nexus of Illinois politics where Lincoln and Mary Todd met and courted",
            "His implication in the A.B. Plot controversy and the resulting political damage illustrated the vulnerability of frontier political careers to factional attacks and corruption allegations in the competitive patronage politics of the Jacksonian era"
        ],
        "relationships": [
            {"entity": "Illinois Territory", "relationship": "FIRST_AND_ONLY_GOVERNOR_OF", "note": "Served as the first and only Governor of Illinois Territory (1809–1818) — the entire duration of the territory's existence"},
            {"entity": "Illinois (early statehood)", "relationship": "FOUNDING_SENATOR_AND_GOVERNOR", "note": "One of Illinois's first two US Senators (1818–1824) and later Governor of the State of Illinois (1826–1830)"},
            {"entity": "Abraham Lincoln / Mary Todd courtship", "relationship": "FAMILIAL_CONTEXT_FOR", "note": "His son Ninian Wirt Edwards married Elizabeth Todd (Mary Todd's sister) — making the Edwards house in Springfield the setting where Lincoln and Mary Todd met and courted"},
            {"entity": "War of 1812 (Illinois frontier security)", "relationship": "TERRITORIAL_GOVERNOR_DURING", "note": "Managed Illinois Territory's frontier security during the War of 1812 — when Native American raids associated with the British alliance threatened frontier settlements"},
            {"entity": "A.B. Plot controversy", "relationship": "DAMAGED_BY", "note": "Implicated in the A.B. Plot — a Treasury Department misconduct controversy — which damaged his reputation and contributed to the end of his political influence"}
        ]
    }),

    # 7 — Josiah S. Johnston
    ("josiah-s-johnston", {
        "summary": (
            "Josiah Stoddard Johnston (1784–1833) was an American lawyer and "
            "Democratic-Republican/National Republican politician who represented "
            "Louisiana in both the US House of Representatives and the US Senate "
            "— serving as US Representative (1821–1823) and then as US Senator "
            "(1824–1833), where he was a close ally of Henry Clay and a leading "
            "proponent of the American System — Clay's economic program of "
            "protective tariffs, a national bank, and internal improvements — "
            "that sought to promote American industrial and economic development. "
            "Johnston was one of the most articulate congressional defenders of "
            "the protective tariff in the Senate debates of the late 1820s.\n\n"
            "Louisiana's political culture presented Johnston with particular "
            "challenges: it was a state with a large Creole population, a "
            "distinctive legal system (based on French and Spanish civil law "
            "rather than English common law), an overwhelmingly agricultural "
            "economy based on sugar and cotton, and strong Jacksonian Democratic "
            "tendencies that conflicted with Johnston's National Republican "
            "alignment. His advocacy for Clay's American System represented "
            "an economic vision — protective tariffs for American manufacturers "
            "— that was deeply unpopular in an export-oriented Southern state "
            "that relied on free trade.\n\n"
            "Johnston's life and career ended violently on June 14, 1833, when "
            "the steamboat Lioness — on which he was traveling on the Red River "
            "in Louisiana — exploded and sank. His death was one of the earliest "
            "and most prominent casualties of the steamboat disaster epidemic "
            "that was claiming hundreds of lives annually on American rivers "
            "as steamboat technology spread faster than safety regulations.\n\n"
            "He had been a close friend of Henry Clay throughout his Senate career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Louisiana US Representative and US Senator (1824–1833); close ally of Henry Clay and proponent of the American System in the Senate; articulate defender of protective tariffs; killed in the 1833 steamboat Lioness explosion — one of the first prominent American officials killed in a steamboat disaster.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louisiana's admission to the Union (1812) and its distinctive Creole legal and cultural character created the unusual political environment in which Johnston — a Kentucky-born National Republican — represented a Southern state as an advocate of Henry Clay's American System",
            "Henry Clay's American System's promotion of protective tariffs, a national bank, and internal improvements created the economic program that Johnston advocated in the Senate — a program that was deeply unpopular in export-oriented Louisiana",
            "The rapid spread of steamboat technology on American rivers — which dramatically accelerated commerce and transportation but also created serious explosion hazards due to high-pressure boilers — created the danger that ultimately killed Johnston"
        ],
        "effects": [
            "His Senate advocacy for the American System contributed to the political debate over protective tariffs and national economic development during the crucial period of the Tariff of Abominations (1828) and the nullification crisis",
            "His death in the Lioness explosion (1833) made him one of the first prominent American public officials killed in a steamboat disaster — contributing to growing public awareness of steamboat safety hazards that eventually drove Congressional regulation",
            "His close alliance with Henry Clay contributed to Louisiana's National Republican political minority — maintaining a pro-Clay faction in a state that was otherwise moving rapidly toward Jacksonian Democracy",
            "His premature death removed one of the Senate's most articulate American System defenders at a critical moment — when the tariff debates were intensifying and the nullification crisis was approaching its climax"
        ],
        "relationships": [
            {"entity": "Henry Clay (Kentucky statesman)", "relationship": "CLOSE_ALLY_AND_AMERICAN_SYSTEM_ADVOCATE_WITH", "note": "A close personal friend and political ally of Henry Clay — one of the Senate's most articulate defenders of Clay's American System"},
            {"entity": "Louisiana (US Senate representation)", "relationship": "SENATOR_1824-1833", "note": "US Senator from Louisiana (1824–1833) — representing a Southern state while advocating the National Republican/American System economic program"},
            {"entity": "American System (Clay's economic program)", "relationship": "SENATE_ADVOCATE_OF", "note": "Defended protective tariffs, the national bank, and internal improvements in the Senate debates of the late 1820s and early 1830s"},
            {"entity": "Steamboat Lioness explosion (1833)", "relationship": "KILLED_IN", "note": "Killed when the steamboat Lioness exploded on the Red River (June 14, 1833) — one of the first prominent American officials killed in a steamboat disaster"},
            {"entity": "Louisiana Creole/civil law tradition", "relationship": "NATIONAL_REPUBLICAN_VOICE_WITHIN", "note": "A National Republican outsider in Louisiana's Creole, Francophone, civil-law political culture — representing a minority economic vision in an export-oriented slave state"}
        ]
    }),

    # 8 — Thomas Lowndes
    ("thomas-lowndes", {
        "summary": (
            "Thomas Lowndes (1766–1843) was a South Carolina planter, lawyer, and "
            "politician from Charleston who represented one of the distinguished "
            "Lowndes political family — the son of Rawlins Lowndes, who had served "
            "as Governor of South Carolina during the Revolutionary War (1778–1779), "
            "and half-brother of William Lowndes, who served in the US House "
            "and whose friends championed him (unsuccessfully) as a presidential "
            "candidate before his early death. Thomas served in the South Carolina "
            "state legislature and as a US Representative from South Carolina "
            "(1801–1805), maintaining the family's political presence across "
            "the Federalist and Democratic-Republican eras.\n\n"
            "The Lowndes family was one of South Carolina's most politically "
            "distinguished — a tidewater planter dynasty whose members served "
            "in colonial, revolutionary, and early federal governance. Thomas's "
            "career was less spectacular than his father's or half-brother's, "
            "but it reflected the continuity of South Carolina's planter-class "
            "political dominance into the early republic.\n\n"
            "South Carolina's early republic politics was characterized by intense "
            "factional competition between Federalist coastal planters (like the "
            "Lowndes family) and Democratic-Republican upcountry farmers — a "
            "divide that mapped onto economic interests, class, and geographic "
            "identity. Thomas navigated this divide as a congressman during the "
            "Jefferson administration's first term — a period of significant "
            "policy change from the Federalist era.\n\n"
            "His career represents the second generation of the Lowndes political "
            "dynasty — maintaining family influence through state and federal "
            "legislative service."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "South Carolina Federalist politician and US Representative (1801–1805); son of Revolutionary War Governor Rawlins Lowndes and half-brother of US Representative William Lowndes; second generation of one of South Carolina's most distinguished political dynasties.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Lowndes family's establishment as one of South Carolina's leading tidewater planter dynasties — with his father Rawlins Lowndes as Governor — created the social and political capital that made Thomas's congressional career possible",
            "South Carolina's Federalist coastal planter political culture created the partisan context in which the Lowndes family's political identity was rooted — though the Democratic-Republican era required adaptation",
            "The transition from the Federalist to the Democratic-Republican era during Jefferson's presidency created the political context of Thomas's congressional service — requiring Federalist gentry families to navigate a changing political landscape"
        ],
        "effects": [
            "His congressional service (1801–1805) contributed to South Carolina's representation in the US House during Jefferson's first term — maintaining the Lowndes family's federal political presence",
            "The Lowndes family's multi-generational political service — Rawlins as governor, Thomas in Congress, and William Lowndes as a significant congressional figure — made them a model of South Carolina tidewater planter political dynasticism",
            "His career demonstrated the ability of Federalist tidewater families to maintain political relevance into the Democratic-Republican era through state and federal legislative service",
            "The Lowndes family connection — through the elder Rawlins's Revolutionary War governorship — linked Thomas's career to the foundational history of South Carolina statehood"
        ],
        "relationships": [
            {"entity": "Rawlins Lowndes (SC Governor)", "relationship": "SON_OF", "note": "Son of Rawlins Lowndes — Governor of South Carolina during the Revolutionary War (1778–1779) and the most prominent South Carolina Anti-Federalist"},
            {"entity": "William Lowndes (SC Congressman)", "relationship": "HALF-BROTHER_OF", "note": "Half-brother of William Lowndes — who helped secure the declaration of the War of 1812 and was championed for the presidency before his early death"},
            {"entity": "South Carolina (US House representation)", "relationship": "REPRESENTATIVE_1801-1805", "note": "Served as US Representative from South Carolina (1801–1805) during Jefferson's first presidential term"},
            {"entity": "South Carolina tidewater planter political dynasty", "relationship": "SECOND-GENERATION_MEMBER_OF", "note": "The second generation of the Lowndes political dynasty — maintaining the family's political presence through state and federal legislative service"},
            {"entity": "Jefferson administration (1801–1805)", "relationship": "CONGRESSMAN_DURING", "note": "Served in the US House during Jefferson's first term — a period of significant policy transition from the Federalist to Democratic-Republican era"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 30)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
