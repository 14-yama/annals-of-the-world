#!/usr/bin/env python3
"""
Batch 38 — 8 entities: George Bryan, Robert Treat Paine, Cornelius Harnett,
John Pickering, John Anthony Quitman, Geoffrey (of York), Anosazad,
Gunning Bedford (Sr.)
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

    # 1 — George Bryan
    ("george-bryan", {
        "summary": (
            "George Bryan (1731–1791) was an Irish-born Pennsylvania "
            "businessman, judge, and statesman who was one of the key "
            "architects of the Pennsylvania Constitution of 1776 — the "
            "most radically democratic state constitution of the Revolutionary "
            "era — and the principal sponsor of the Pennsylvania Gradual "
            "Abolition Act of 1780, the first gradual abolition law enacted "
            "in American history. Born in Dublin, Bryan emigrated to "
            "Philadelphia in 1752, built a successful merchant career, "
            "and became deeply embedded in Pennsylvania's Presbyterian "
            "and reform-minded political culture.\n\n"
            "Bryan served as Vice-President of Pennsylvania's Supreme "
            "Executive Council (1776–1777) and then as the state's "
            "acting President (governor) from 1777 to 1779. During "
            "this period he was the driving force behind the Pennsylvania "
            "Abolition Act of 1780 — legislation that established gradual "
            "emancipation for Pennsylvania's enslaved population and "
            "served as the model for subsequent abolition acts in New "
            "England and the mid-Atlantic states. He also championed "
            "Quaker affirmation rights and opposed the property "
            "requirements that limited democratic participation.\n\n"
            "His authorship of the Pennsylvania Constitution of 1776 — "
            "with its unicameral legislature, absence of property "
            "requirements for voting, and strong democratic populist "
            "character — made Pennsylvania the most radical of the "
            "founding state constitutions, inspiring democrats elsewhere "
            "while horrifying conservatives like John Adams.\n\n"
            "Bryan's career embodied the fusion of evangelical Protestant "
            "conviction, Irish immigrant democratic instinct, and "
            "Enlightenment republicanism that made Pennsylvania the "
            "most progressive founding state."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Irish-born Pennsylvania statesman; key architect of the Pennsylvania Constitution of 1776 (most democratic founding state constitution — unicameral, no property requirements); principal sponsor of the Pennsylvania Gradual Abolition Act of 1780 — the first gradual abolition law in American history; acting President (governor) of Pennsylvania 1777–1779.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pennsylvania's unique multicultural and religiously diverse political culture — with its Quaker, Presbyterian, and German immigrant communities suspicious of aristocratic power — created the receptive environment for Bryan's democratic and abolitionist initiatives",
            "Bryan's Irish immigrant background — and the colonial Irish experience of subordination to English aristocratic power — gave him a distinctive democratic instinct that aligned with Pennsylvania's Dissenter tradition against property-based restrictions on political participation",
            "The Revolutionary crisis's demand for a new state constitutional order — and Pennsylvania's particular need to mobilize a broad popular coalition against loyalists and moderate conservatives — created the political opening for the radical democratic Pennsylvania Constitution of 1776"
        ],
        "effects": [
            "The Pennsylvania Gradual Abolition Act of 1780 — which Bryan sponsored — was the first gradual abolition law in American history, establishing the legal model that Vermont, Massachusetts, Rhode Island, Connecticut, New York, and New Jersey subsequently adopted in their own emancipation legislation",
            "The Pennsylvania Constitution of 1776 — which Bryan helped draft — with its unicameral legislature and minimal property requirements was the most democratic state constitution of the era, inspiring democratic movements across the Atlantic world while alarming conservatives who saw it as dangerously leveling",
            "His defense of Quaker affirmation rights — allowing Quakers to affirm rather than swear oaths — contributed to Pennsylvania's tradition of religious accommodation and legal pluralism that distinguished it from most other colonial jurisdictions",
            "His career demonstrated the path of Irish Protestant immigrant integration into American revolutionary politics — the fusion of European Dissenter traditions with American democratic republicanism that characterized Pennsylvania's founding generation"
        ],
        "relationships": [
            {"entity": "Pennsylvania Gradual Abolition Act (1780) — first in American history", "relationship": "PRINCIPAL_SPONSOR_OF", "note": "Sponsored the Pennsylvania Gradual Abolition Act of 1780 — the first gradual abolition law in American history, establishing the legal model for subsequent New England and mid-Atlantic emancipation acts"},
            {"entity": "Pennsylvania Constitution of 1776 (most democratic founding state constitution)", "relationship": "KEY_ARCHITECT_OF", "note": "Key architect of the Pennsylvania Constitution of 1776 — the most radically democratic founding state constitution, with a unicameral legislature and minimal property requirements"},
            {"entity": "Pennsylvania Supreme Executive Council (Vice-President and acting President, 1776–1779)", "relationship": "VICE-PRESIDENT_AND_ACTING_PRESIDENT_OF", "note": "Served as Vice-President and then acting President (governor) of Pennsylvania's Supreme Executive Council (1776–1779) — governing the state during the Revolutionary War's most critical years"},
            {"entity": "Quaker affirmation rights / religious pluralism (Pennsylvania)", "relationship": "CHAMPION_OF", "note": "Championed legislation allowing Quakers to affirm rather than swear oaths — contributing to Pennsylvania's tradition of religious accommodation and legal pluralism"},
            {"entity": "Irish immigrant democratic tradition in American politics", "relationship": "REPRESENTATIVE_FIGURE_OF", "note": "Irish-born emigrant whose democratic instinct — rooted in the colonial Irish experience of aristocratic subordination — aligned with Pennsylvania's Dissenter tradition against property-based political exclusion"}
        ]
    }),

    # 2 — Robert Treat Paine
    ("robert-treat-paine", {
        "summary": (
            "Robert Treat Paine (1731–1814) was a Massachusetts lawyer, "
            "Founding Father, and signer of the Declaration of Independence "
            "(1776) who also served as Massachusetts's first Attorney General "
            "(1777–1790) and as a justice of the Massachusetts Supreme "
            "Judicial Court (1790–1804). Born in Boston and educated "
            "at Harvard, he began his legal career in Taunton, Massachusetts "
            "and quickly became a significant figure in the colonial "
            "opposition to British taxation.\n\n"
            "Paine is particularly notable for his role in the Boston "
            "Massacre trial of 1770 — he served as one of the prosecution "
            "attorneys seeking conviction of the British soldiers who "
            "killed five colonists, in the same trial where John Adams "
            "served as defense attorney for the soldiers. Both Adams "
            "and Paine were committed patriots, but their opposing "
            "roles in the same trial illustrated the colonial legal "
            "community's genuine commitment to rule of law even at a "
            "moment of extreme political tension.\n\n"
            "He was elected to the Continental Congress, signed the "
            "Continental Association (1774), and signed the Declaration "
            "of Independence as a Massachusetts representative in 1776. "
            "He also served on the committee that drafted Massachusetts's "
            "Articles of War — establishing the legal framework for the "
            "Continental Army.\n\n"
            "His long tenure as Massachusetts's first Attorney General "
            "(1777–1790) and subsequent judicial career contributed "
            "to the institutional architecture of Massachusetts's legal "
            "system in the crucial post-Revolutionary decades."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts Founding Father; signer of the Declaration of Independence (1776) and Continental Association (1774); one of the prosecution attorneys in the Boston Massacre trial (1770) — the same trial where John Adams defended the soldiers; Massachusetts's first Attorney General (1777–1790); SJC justice (1790–1804).",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Boston Massacre (March 5, 1770) — the killing of five colonists by British soldiers — created the immediate political crisis that demanded the legal response in which Paine served as prosecution attorney, making him a prominent figure in the colonial resistance",
            "Massachusetts's leading role in the colonial resistance movement — and its need for credentialed Harvard-educated lawyers willing to risk their careers advocating colonial rights — created the political environment in which Paine's legal career intersected with the founding movement",
            "The Continental Congress's need for experienced colonial lawyers who could draft the Articles of War and organize the legal framework for the Continental Army — creating the committee work that Paine contributed to"
        ],
        "effects": [
            "His prosecution role in the Boston Massacre trial contributed to the legal accountability process that attempted to hold British military power responsible under colonial law — even though the soldiers were ultimately acquitted by Adams's defense",
            "His signature on the Declaration of Independence (1776) contributed to Massachusetts's unanimous delegation support for independence — ensuring the colony's unambiguous commitment to the revolutionary cause",
            "His tenure as Massachusetts's first Attorney General (1777–1790) established the office's institutional framework — defining the scope, powers, and practices of the state attorney general role in the critical post-Revolutionary decades",
            "The Boston Massacre trial's dual legacy — Adams defending, Paine prosecuting, with both remaining patriots — illustrated to the colonial world that commitment to legal principle and commitment to independence were not mutually exclusive, strengthening the revolutionary cause's moral legitimacy"
        ],
        "relationships": [
            {"entity": "Declaration of Independence (Massachusetts, 1776)", "relationship": "SIGNER", "note": "Signed the Declaration of Independence as a Massachusetts delegate — one of five Massachusetts signers"},
            {"entity": "Boston Massacre trial (1770) — prosecution", "relationship": "PROSECUTION_ATTORNEY_IN", "note": "Served as prosecution attorney in the Boston Massacre trial — seeking conviction of the British soldiers while John Adams served as their defense attorney"},
            {"entity": "John Adams (opposing counsel in Boston Massacre trial)", "relationship": "OPPOSING_COUNSEL_TO_IN_BOSTON_MASSACRE_TRIAL", "note": "He and Adams argued opposing sides of the Boston Massacre trial — both remained patriots, illustrating that legal principle and revolutionary commitment were compatible"},
            {"entity": "Massachusetts Attorney General (first, 1777–1790)", "relationship": "FIRST_ATTORNEY_GENERAL", "note": "Served as Massachusetts's first Attorney General (1777–1790) — establishing the institutional framework of the office in the post-Revolutionary decades"},
            {"entity": "Massachusetts Supreme Judicial Court (1790–1804)", "relationship": "ASSOCIATE_JUSTICE", "note": "Served as SJC justice (1790–1804) — contributing to Massachusetts's legal jurisprudence in the early republican period"}
        ]
    }),

    # 3 — Cornelius Harnett
    ("cornelius-harnett", {
        "summary": (
            "Cornelius Harnett (1723–1781) was a North Carolina merchant, "
            "plantation owner, and one of the most significant American "
            "Revolutionary statesmen of the Cape Fear region — called "
            "the 'Pride of the Cape Fear' and 'the Samuel Adams of "
            "North Carolina' by his contemporaries. A leading organizer "
            "of resistance to the Stamp Act and Townshend Acts in "
            "Wilmington, North Carolina, Harnett was one of the most "
            "consequential Revolutionary activists in the South — "
            "a man who committed his merchant wealth, his political "
            "career, and ultimately his life to the independence cause.\n\n"
            "Harnett served in the North Carolina Provincial Congress, "
            "chaired the Cape Fear Committee of Safety, and was elected "
            "as a delegate to the Continental Congress (1777–1779) — "
            "where he served on the committee that drafted the Articles "
            "of Confederation and was elected president of the Congress "
            "in 1778. His congressional service came during one of the "
            "most difficult periods of the Revolutionary War, when "
            "British victories in the South threatened to collapse the "
            "colonial resistance in the Carolinas.\n\n"
            "His end was tragic and heroic: when British forces captured "
            "Wilmington during their 1781 southern campaign, Harnett — "
            "already ill with gout — was captured and imprisoned. He "
            "died in British captivity on April 28, 1781, at 58 — "
            "one of the few Founding Fathers to die as a direct result "
            "of British military action, making him a martyr to the "
            "cause he had championed for two decades.\n\n"
            "'He was the last man in America who ought to die,' "
            "wrote William Hooper of his death — a testament to "
            "his irreplaceable presence in North Carolina's founding generation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "'Pride of the Cape Fear' — 'the Samuel Adams of North Carolina'; leading organizer of Stamp Act resistance in Wilmington; Continental Congress delegate (1777–1779); president of Congress (1778); died in British captivity April 28, 1781 — one of the few Founding Fathers to die as a direct result of British military action.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Wilmington, North Carolina's position as a major Cape Fear port town — and its exposure to British customs enforcement and parliamentary taxation — made it a natural center of colonial resistance that Harnett's merchant wealth and political connections helped organize",
            "North Carolina's distinctive patriot tradition — less studied than Massachusetts or Virginia but no less committed — created the environment that elevated Harnett to the Continental Congress and to the presidency of Congress in 1778",
            "The British southern campaign of 1780–1781 — which captured Charleston, devastated the Carolinas, and briefly occupied Wilmington — created the military situation that led directly to Harnett's capture and death in captivity"
        ],
        "effects": [
            "His death in British captivity (April 1781) made him one of the most poignant martyrs of the American Revolution — a Founding Father whose commitment to independence cost him his life, strengthening the moral narrative of the colonial cause",
            "His chairmanship of the Cape Fear Committee of Safety contributed to North Carolina's organized resistance infrastructure — the provincial governance that sustained the state's war effort during the most difficult periods of British military pressure",
            "His Continental Congress service (1777–1779) and presidential term (1778) maintained North Carolina's representation at the national level during the most critical period of the war — ensuring the state's voice in Articles of Confederation debates",
            "His legacy as 'the Samuel Adams of North Carolina' established him as the archetype of the Southern Revolutionary activist — the merchant-patriot who committed personal wealth to the colonial cause and paid the ultimate price for it"
        ],
        "relationships": [
            {"entity": "Continental Congress (NC delegate 1777–1779, President 1778)", "relationship": "DELEGATE_AND_PRESIDENT", "note": "Served as North Carolina's Continental Congress delegate (1777–1779) and was elected president of Congress in 1778 — representing NC during the war's most difficult period"},
            {"entity": "Stamp Act resistance / Wilmington NC (1765–1766)", "relationship": "LEADING_ORGANIZER_OF", "note": "Led resistance to the Stamp Act in Wilmington, North Carolina — earning the title 'the Samuel Adams of North Carolina' and 'Pride of the Cape Fear'"},
            {"entity": "Cape Fear Committee of Safety (Revolutionary governance)", "relationship": "CHAIRMAN", "note": "Chaired the Cape Fear Committee of Safety — the provincial governance structure that organized North Carolina's Revolutionary resistance"},
            {"entity": "British captivity / death April 28, 1781 (Wilmington)", "relationship": "DIED_IN", "note": "Captured during the British occupation of Wilmington in 1781 — died in British captivity on April 28, 1781, one of the few Founding Fathers to die as a direct result of British military action"},
            {"entity": "Articles of Confederation drafting committee", "relationship": "CONTINENTAL_CONGRESS_MEMBER_WHO_SERVED_ON", "note": "Served on the Continental Congress committee that drafted the Articles of Confederation — contributing to the first American national constitutional framework"}
        ]
    }),

    # 4 — John Pickering
    ("john-pickering", {
        "summary": (
            "John Pickering (1737/1738–1805) was a New Hampshire "
            "lawyer, jurist, and politician who served as President "
            "(governor) of New Hampshire (1790–1791) and as Chief "
            "Justice of the New Hampshire Superior Court before his "
            "appointment as a US District Court judge for New Hampshire "
            "in 1795 — a position he held until his impeachment, "
            "conviction, and removal from office in 1804. His removal "
            "was the first successful judicial impeachment in American "
            "history — a watershed moment for judicial independence, "
            "constitutional law, and the boundaries of congressional "
            "power over the federal judiciary.\n\n"
            "By the time of his impeachment, Pickering was clearly "
            "incapacitated — suffering from severe alcoholism and "
            "what contemporaries described as insanity, which prevented "
            "him from appearing in his own defense. His Republican "
            "enemies in Congress recognized that his condition provided "
            "a pretext for removing a Federalist judge, but the "
            "constitutional procedure required impeachment for high "
            "crimes and misdemeanors — not incapacity. His conviction "
            "by the Senate on March 12, 1804 set the precedent that "
            "Congress could remove a judge for behavior falling short "
            "of conventional criminality.\n\n"
            "His removal — politically timed to coincide with Jefferson's "
            "Republican assault on the Federalist judiciary — alarmed "
            "John Marshall and the Supreme Court, contributing to "
            "Marshall's careful navigation of the confrontation with "
            "the Jefferson administration. The precedent Pickering's "
            "case set shaped every subsequent judicial impeachment debate.\n\n"
            "His personal tragedy — an accomplished jurist destroyed "
            "by mental illness — was weaponized for partisan ends."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President (governor) of New Hampshire (1790–1791); Chief Justice of NH Superior Court; US District Court judge (1795–1804); first judge successfully impeached and removed in American history (Senate conviction March 12, 1804) — a watershed for judicial independence; his removal alarmed John Marshall and shaped all subsequent judicial impeachment precedent.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Jefferson administration's confrontation with the Federalist-dominated federal judiciary — and the Republican majority's desire to replace Federalist judges with Republican appointees — created the political motive for Pickering's impeachment despite the constitutional difficulties",
            "Pickering's severe alcoholism and mental incapacity — which prevented him from conducting judicial business properly or appearing in his own defense — provided the behavioral pretext for impeachment even though his condition was not clearly a 'high crime or misdemeanor' as the Constitution required",
            "The constitutional ambiguity about whether federal judges could be removed for incapacity rather than criminality — a gap in the impeachment mechanism that Pickering's case exposed — created the legal challenge that the Republican Congress resolved by simply convicting him on the charges as stated"
        ],
        "effects": [
            "His Senate conviction on March 12, 1804 established the first precedent for successful judicial impeachment and removal in American history — demonstrating that the mechanism could work even for behavior falling short of conventional criminality",
            "His removal alarmed John Marshall and the Federalist judiciary — contributing to Marshall's strategic caution in the confrontation with Jefferson and to Marshall's careful development of judicial review as a constitutional principle that transcended the partisan moment",
            "The impeachment debate over whether 'high crimes and misdemeanors' encompassed incapacity — as opposed to criminality — generated constitutional arguments that influenced all subsequent judicial impeachment proceedings",
            "His political removal by a Republican Congress demonstrated the partisan nature of the early impeachment mechanism — confirming Federalist fears that the Jefferson Republicans intended to remake the judiciary through impeachment, fears that Marshall took seriously in calibrating his own behavior"
        ],
        "relationships": [
            {"entity": "First judicial impeachment and removal (Senate, March 12, 1804)", "relationship": "SUBJECT_OF_FIRST_SUCCESSFUL", "note": "Senate convicted and removed him on March 12, 1804 — the first successful judicial impeachment in American history, establishing the precedent for all subsequent removals"},
            {"entity": "Jefferson administration's assault on Federalist judiciary", "relationship": "POLITICALLY_CONVENIENT_TARGET_OF", "note": "His incapacity provided a pretext for the Jefferson Republican Congress to remove a Federalist judge — part of the broader Republican confrontation with the Federalist judiciary"},
            {"entity": "John Marshall / Federalist judiciary independence", "relationship": "REMOVAL_CASE_THAT_ALARMED_AND_INFLUENCED_STRATEGY_OF", "note": "His removal alarmed Marshall — contributing to Marshall's strategic caution in the Jefferson confrontation and his development of judicial review as a principle transcending partisan pressure"},
            {"entity": "New Hampshire governorship / NH Superior Court Chief Justice (1790s)", "relationship": "FORMER_GOVERNOR_AND_CHIEF_JUSTICE_BEFORE_FEDERAL_APPOINTMENT", "note": "Served as NH governor (1790–1791) and Chief Justice of the NH Superior Court before Washington appointed him to the federal district court in 1795"},
            {"entity": "Constitutional definition of 'high crimes and misdemeanors'", "relationship": "IMPEACHMENT_CASE_THAT_TESTED_LIMITS_OF", "note": "His impeachment tested whether incapacity constituted a 'high crime or misdemeanor' — the constitutional ambiguity his case exposed influenced all subsequent judicial impeachment debates"}
        ]
    }),

    # 5 — John Anthony Quitman
    ("john-anthony-quitman", {
        "summary": (
            "John Anthony Quitman (1798–1858) was a New York-born "
            "Mississippi politician, military officer, and fire-eater "
            "secessionist who served as acting Governor of Mississippi "
            "(1835–1836), Governor of Mississippi (1850–1851), and "
            "US Representative (1855–1858) — and who commanded the "
            "first American troops to enter Mexico City on September 14, "
            "1847, becoming the military governor of Mexico City "
            "during the Mexican-American War. Born in Rhinebeck, "
            "New York, he migrated to Mississippi in the 1820s, built "
            "a plantation and law practice, and became a leading figure "
            "in Mississippi's antebellum political world.\n\n"
            "Quitman's military career was his most remarkable achievement: "
            "promoted to major general during the Mexican-American War, "
            "he commanded the storming of Chapultepec and led his division "
            "through the gates of Mexico City on September 14, 1847 — "
            "entering the Hall of Montezuma in a moment that became "
            "one of the war's most celebrated scenes. He was the "
            "military governor of Mexico City for the first days of "
            "American occupation.\n\n"
            "His subsequent political career reflected his fire-eater "
            "convictions: he became deeply involved in organizing "
            "filibuster expeditions to Cuba in the early 1850s — "
            "seeking to annex Cuba as a slave state — was indicted "
            "by a federal grand jury for violating the Neutrality Act, "
            "resigned the governorship under that pressure in 1851, "
            "and was eventually elected to Congress where he remained "
            "a secessionist hardliner until his death in 1858.\n\n"
            "'From the halls of Montezuma' — a line in the Marines' Hymn — "
            "commemorates the action he led."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York-born Mississippi politician and fire-eater; commanded the first American troops to enter Mexico City (September 14, 1847) — the 'halls of Montezuma' celebrated in the Marines' Hymn; acting governor (1835–36) and elected governor (1850–51) of Mississippi; organized Cuban filibuster expeditions; US congressman (1855–1858).",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mississippi's frontier plantation culture — and its dependence on the cotton economy and enslaved labor — created the political environment that elevated Quitman from New York migrant to fire-eater governor and secessionist hardliner",
            "The Mexican-American War's military opportunities — and Zachary Taylor and Winfield Scott's campaigns — created the theater in which Quitman's military talent earned him a major generalship and command of the Mexico City assault",
            "The antebellum Cuba annexation movement — rooted in the desire to add another slave state to the Union and to prevent Spanish abolition from creating a free-Black republic near US shores — created the filibuster movement that Quitman helped organize and lead"
        ],
        "effects": [
            "His command of the Mexico City assault on September 14, 1847 — and his military governorship of the Mexican capital — made him one of the most celebrated American military heroes of the Mexican-American War, directly contributing to the Marines' Hymn's immortal opening line",
            "His organization of Cuban filibuster expeditions in the early 1850s — and his federal indictment under the Neutrality Act — demonstrated the lengths to which Southern politicians would go to expand slavery's geographic reach before the Civil War",
            "His resignation from the governorship under federal indictment pressure (1851) illustrated the collision between fire-eater expansionism and federal law enforcement — a collision that foreshadowed the larger constitutional confrontation over slavery and federal authority",
            "His congressional career (1855–1858) as a secessionist hardliner contributed to the radicalization of Southern congressional opinion in the critical decade preceding secession — he died in 1858, just two years before the crisis he had long predicted materialized"
        ],
        "relationships": [
            {"entity": "Mexico City assault / Mexican-American War (September 14, 1847)", "relationship": "COMMANDED_FIRST_AMERICAN_TROOPS_TO_ENTER", "note": "Led his division into Mexico City on September 14, 1847 — commanding the first American troops through the Mexican capital's gates and serving as military governor during the initial occupation"},
            {"entity": "Marines' Hymn ('From the halls of Montezuma')", "relationship": "MILITARY_COMMANDER_WHOSE_ACTION_IMMORTALIZED_IN", "note": "His assault on the Hall of Montezuma (Chapultepec/Mexico City) is commemorated in the Marines' Hymn's opening line — 'From the halls of Montezuma'"},
            {"entity": "Mississippi governorship (acting 1835–36, elected 1850–51)", "relationship": "GOVERNOR_TWICE", "note": "Served as acting governor of Mississippi (1835–36) and elected governor (1850–51) — resigning in 1851 under federal indictment for organizing Cuban filibuster expeditions"},
            {"entity": "Cuban filibuster expeditions (early 1850s) / Neutrality Act indictment", "relationship": "ORGANIZER_INDICTED_FOR", "note": "Organized and supported filibuster expeditions to Cuba seeking annexation as a slave state — federally indicted under the Neutrality Act, forcing his gubernatorial resignation"},
            {"entity": "Mississippi fire-eater secessionism (antebellum)", "relationship": "LEADING_FIGURE_OF", "note": "One of Mississippi's leading fire-eater secessionists — a New York migrant who became one of the Deep South's most radical advocates for Southern rights and eventual secession"}
        ]
    }),

    # 6 — Geoffrey of York
    ("geoffrey", {
        "summary": (
            "Geoffrey (c. 1151–1212), also known as Geoffrey of York, "
            "was an illegitimate son of King Henry II of England and "
            "the Archbishop of York (1189–1212) whose turbulent tenure "
            "defined some of the most contentious church-crown-Canterbury "
            "disputes of the Angevin period. The identity of his mother "
            "is uncertain (possibly named Ykenai), but his royal "
            "paternity was unambiguous — he was Henry II's acknowledged "
            "illegitimate son, educated and advanced by the king "
            "despite canonical obstacles to his ecclesiastical career.\n\n"
            "Henry II appointed Geoffrey bishop-elect of Lincoln in "
            "1173, though Geoffrey was never consecrated to that see "
            "and resigned it in 1182. His real ecclesiastical ambition "
            "was realized when his half-brother Richard I — immediately "
            "upon his accession in 1189 — appointed him Archbishop of York, "
            "fulfilling a promise Henry II had made. This appointment "
            "placed Geoffrey at the center of the prolonged dispute "
            "between York and Canterbury over primacy in the English church — "
            "a dispute that had already destroyed Thomas Becket.\n\n"
            "Geoffrey's archiepiscopate was characterized by sustained "
            "conflict: with his cathedral chapter, with Archbishop Hubert "
            "Walter of Canterbury, with Pope Innocent III, and with "
            "King John (his half-brother) who was his most persistent "
            "antagonist. John blocked Geoffrey's revenues, expelled "
            "him from England at least twice, and finally drove him "
            "into permanent exile in Normandy, where Geoffrey died "
            "in 1212.\n\n"
            "He remained loyal to Richard I when others wavered — "
            "a loyalty that Richard rewarded and that John ultimately "
            "destroyed."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Illegitimate son of Henry II of England; Archbishop of York (1189–1212); his turbulent archiepiscopate defined the York-Canterbury primacy dispute and the church-crown conflict in the Angevin period; loyal to Richard I; repeatedly exiled by King John; died in Normandy exile (1212).",
            "significanceCategory": "regional"
        },
        "causes": [
            "His royal Plantagenet paternity — as Henry II's acknowledged illegitimate son — gave him the political sponsorship and royal patronage that elevated him into the English church hierarchy despite canonical obstacles, creating a career trajectory that depended entirely on royal favor",
            "The York-Canterbury primacy dispute — which had been intensifying throughout the 12th century and which the Becket crisis had not resolved — created the institutional context in which Geoffrey's archiepiscopate became a flashpoint for competing jurisdictional claims",
            "The Angevin succession crisis — Richard I's crusade absence, John's regency, and the turbulent transition from Richard to John — created the political instability in which Geoffrey's church-crown conflicts intensified into permanent exile"
        ],
        "effects": [
            "His prolonged conflict with Archbishop Hubert Walter of Canterbury — over the York-Canterbury primacy dispute — contributed to the ongoing institutional rivalry between the two English archbishoprics that would continue for centuries",
            "King John's expulsion of Geoffrey from England and his confiscation of Geoffrey's archiepiscopal revenues demonstrated the crown's capacity to weaponize financial and administrative pressure against a church that resisted royal control",
            "His loyalty to Richard I during periods when other barons wavered — and the contrast with John's subsequent treatment of him — illustrated the Angevin family's internal fractures and the personal political calculations that shaped loyalty in Plantagenet England",
            "His forced exile in Normandy — dying there in 1212 without recovering his see — illustrated the fate of ecclesiastical figures who relied on royal patronage in a period of dynastic instability: the same royal connection that elevated them could destroy them when the dynasty changed"
        ],
        "relationships": [
            {"entity": "Henry II of England (father)", "relationship": "ILLEGITIMATE_SON_OF", "note": "Acknowledged illegitimate son of Henry II of England — his royal paternity was the foundation of his entire ecclesiastical career"},
            {"entity": "Archbishop of York (1189–1212)", "relationship": "ARCHBISHOP", "note": "Served as Archbishop of York (1189–1212) — appointed by his half-brother Richard I, who fulfilled Henry II's promise of the see"},
            {"entity": "York-Canterbury primacy dispute (12th–13th century)", "relationship": "ARCHBISHOP_AT_CENTER_OF", "note": "His archiepiscopate was dominated by the sustained conflict between York and Canterbury over English church primacy — one of the most contentious disputes in medieval English ecclesiastical history"},
            {"entity": "King John (half-brother, antagonist)", "relationship": "HALF-BROTHER_REPEATEDLY_EXILED_BY", "note": "Repeatedly exiled by King John — his half-brother and persistent antagonist — who confiscated his revenues and eventually drove him to permanent exile in Normandy"},
            {"entity": "Richard I of England (half-brother, patron)", "relationship": "LOYAL_TO_AND_ELEVATED_BY", "note": "Remained loyal to Richard I — who rewarded his loyalty with the York archbishopric — in contrast to his subsequent treatment by John"}
        ]
    }),

    # 7 — Anosazad
    ("anosazad", {
        "summary": (
            "Anōshazād (died c. 541–542 CE), known in Ferdowsi's "
            "Shahnameh as Nōshzād, was a Sasanian prince — the eldest "
            "son of the great Persian king Khosrow I (Anushirvan, "
            "r. 531–579 CE) — who led a failed revolt in the "
            "southwestern province of Khuzistan in the 540s CE, "
            "one of the few recorded internal challenges to Khosrow I's "
            "long and celebrated reign. His mother was a Christian "
            "woman, the daughter of a judge (dadwar) of Ray, giving "
            "him personal and maternal connections to the large "
            "Christian minority within the Sasanian Empire.\n\n"
            "The revolt — which Anōshazād led while his father was "
            "campaigning against Byzantium — was suppressed by Khosrow's "
            "general Bahram Arslan (or Bahram Chubin in some accounts), "
            "who defeated the rebel prince in battle. Anōshazād was "
            "reportedly captured and may have been blinded as punishment — "
            "the standard Sasanian penalty for princes who posed "
            "succession threats — though sources differ on whether "
            "he survived this punishment.\n\n"
            "The revolt may have had a Christian dimension: given his "
            "mother's faith and his possible sympathy for the Persian "
            "Christian community, some historians suggest Anōshazād "
            "may have hoped to promote a more tolerant policy toward "
            "Christians — though the evidence for this interpretation "
            "is fragmentary. He appears in the Shahnameh as Nōshzād, "
            "a sympathetically portrayed rebel whose story illustrates "
            "the tensions between royal sons and great monarchs.\n\n"
            "His revolt is one of the few windows into the Sasanian "
            "court's internal succession politics during Khosrow I's reign."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Eldest son of Khosrow I (the Great) of the Sasanian Empire; led a revolt in Khuzistan in the 540s CE — one of the few internal challenges to Khosrow I's reign; his mother was Christian; possibly had sympathies for the Persian Christian minority; appears as Nōshzād in Ferdowsi's Shahnameh.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His mother's Christian identity — as the daughter of a Ray judge — gave him personal and family connections to the Sasanian Empire's substantial Christian minority, possibly creating the religious and political motivations for a revolt during his father's absence",
            "Khosrow I's prolonged Byzantine campaigns in the 540s CE — which kept the king away from the Persian heartland — created the political opening that Anōshazād's revolt attempted to exploit",
            "The Sasanian succession system's inherent instability — in which royal sons by different mothers competed for succession claims, often through military rebellion — created the structural incentive for princely revolts like Anōshazād's"
        ],
        "effects": [
            "His defeat and likely blinding — the standard Sasanian punishment for royal succession threats — removed him as a succession competitor for Khosrow I's throne, contributing to the political stability of Khosrow's subsequent long reign",
            "The revolt's suppression demonstrated Khosrow I's military and administrative capacity to manage internal rebellion even while campaigning against Byzantium — a demonstration of the Sasanian state's institutional resilience",
            "His story's preservation in Ferdowsi's Shahnameh as Nōshzād — written five centuries later — illustrates how the revolt became part of the Persian literary tradition's archive of royal sons' tragic conflicts with great fathers",
            "The possible Christian dimension of his revolt — if genuine — illustrates the complex religious politics of the Sasanian court, where Christian minorities navigated carefully between Zoroastrian orthodoxy and the opportunities created by royal family divisions"
        ],
        "relationships": [
            {"entity": "Khosrow I (Anushirvan) of the Sasanian Empire (father)", "relationship": "ELDEST_SON_AND_REBEL_AGAINST", "note": "Eldest son of Khosrow I 'the Great' — led a revolt against his father's authority in Khuzistan in the 540s CE while Khosrow was campaigning against Byzantium"},
            {"entity": "Sasanian Empire / Khuzistan revolt (540s CE)", "relationship": "LED_SUPPRESSED_REVOLT_IN", "note": "Led a revolt in Khuzistan (southwestern Persia) in the 540s CE — one of the few recorded internal challenges to Khosrow I's long reign"},
            {"entity": "Ferdowsi's Shahnameh (as Nōshzād)", "relationship": "COMMEMORATED_AS_IN", "note": "Appears in Ferdowsi's Shahnameh as Nōshzād — sympathetically portrayed as a rebel whose story illustrates the tragic tensions between royal sons and great monarchs"},
            {"entity": "Persian Christian minority (Sasanian Empire)", "relationship": "PRINCE_WITH_POSSIBLE_SYMPATHIES_FOR", "note": "His Christian mother — daughter of a Ray judge — gave him family connections to the Sasanian Christian minority, possibly motivating his revolt's Christian religious dimension"},
            {"entity": "Sasanian succession politics / royal blinding punishment", "relationship": "SUBJECT_OF_STANDARD_SUCCESSION_PENALTY_IN", "note": "Reportedly blinded after his revolt's suppression — the standard Sasanian punishment for princes posing succession threats — removing him from future contention"}
        ]
    }),

    # 8 — Gunning Bedford Sr.
    ("gunning-bedford", {
        "summary": (
            "Gunning Bedford Sr. (1742–1797) was a Delaware lawyer, "
            "Continental Army officer, and Federalist politician who "
            "served as Governor of Delaware from 1796 to 1797 — dying "
            "in office after less than a year in the position. A native "
            "of Philadelphia who settled in Delaware, he served as "
            "an officer during the Revolutionary War, built a legal "
            "and political career in New Castle, and was elected "
            "to the Delaware General Assembly before his gubernatorial "
            "election.\n\n"
            "Bedford is often confused with his more famous cousin "
            "Gunning Bedford Jr. — the Delaware delegate to the "
            "Constitutional Convention of 1787 who famously threatened "
            "that small states would seek foreign alliances if the "
            "large states did not accept equal Senate representation. "
            "Gunning Bedford Sr. was a different person: he did not "
            "attend the Constitutional Convention and his career was "
            "entirely at the state level, culminating in Delaware's "
            "governorship.\n\n"
            "His gubernatorial tenure (1796–1797) was too brief — "
            "truncated by his death in office — to produce significant "
            "legislative achievements. He governed during the Federalist "
            "era of the Adams presidency, maintaining Delaware's "
            "Federalist political alignment in a period of "
            "intense partisan competition between Federalists "
            "and Jeffersonian Republicans.\n\n"
            "His legacy is modest — primarily as a representative of "
            "Delaware's Federalist founding generation and as "
            "the inevitably-confused senior member of the "
            "notable Bedford family."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Governor (1796–1797, died in office); Continental Army officer; Federalist politician from New Castle County; frequently confused with his more famous cousin Gunning Bedford Jr. — the Constitutional Convention delegate who threatened small states would seek foreign alliances.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's small-state political culture — in which a relatively small pool of Federalist lawyer-politicians rotated through the state's highest offices — created the environment in which Bedford's Revolutionary War service and New Castle legal career translated into gubernatorial election",
            "Delaware's strong Federalist political alignment in the 1790s — rooted in its commercial connections to Philadelphia and its proximity to the financial infrastructure that Hamilton's program supported — created the partisan context in which Bedford's Federalist credentials were valuable",
            "His Continental Army service — a credential that remained politically significant throughout the founding era — contributed to the personal authority and public standing that supported his election to the Delaware General Assembly and ultimately the governorship"
        ],
        "effects": [
            "His death in office (1797) after less than a year as governor contributed to Delaware's gubernatorial instability in the 1790s — one of several brief or interrupted terms that characterized the state's early republican governance",
            "His governorship maintained Delaware's Federalist political alignment during the Adams presidency — contributing to the state's resistance to Jeffersonian political pressure in the period immediately before the 1800 Republican Revolution",
            "His legacy was largely overshadowed by his cousin Gunning Bedford Jr.'s Constitutional Convention fame — illustrating how a family name's association with one dramatic historical moment can dominate the collective memory at the expense of other family members' distinct contributions",
            "His Continental Army service contributed to the founding-era political cohort that defined Delaware's Federalist leadership in the 1790s — the military generation that translated Revolutionary War service into post-war political authority"
        ],
        "relationships": [
            {"entity": "Delaware governorship (1796–1797, died in office)", "relationship": "GOVERNOR", "note": "Served as Governor of Delaware (1796–1797) — dying in office after less than a year, one of Delaware's briefest gubernatorial tenures"},
            {"entity": "Gunning Bedford Jr. (Constitutional Convention delegate, cousin)", "relationship": "COUSIN_OFTEN_CONFUSED_WITH", "note": "Frequently confused with his more famous cousin Gunning Bedford Jr. — the Delaware Constitutional Convention delegate who threatened small states would seek foreign alliances if denied equal Senate representation"},
            {"entity": "Delaware Continental Army service / Revolutionary War", "relationship": "OFFICER_IN", "note": "Served as a Continental Army officer during the Revolutionary War — the military credential that remained politically significant throughout the founding era"},
            {"entity": "Delaware Federalist Party (1790s)", "relationship": "FEDERALIST_GOVERNOR_AND_POLITICIAN", "note": "Federated politician who maintained Delaware's strong Federalist alignment during the Adams presidency — the partisan context in which his governorship served"},
            {"entity": "Delaware General Assembly / New Castle County politics", "relationship": "POLITICIAN_AND_LEGISLATOR_IN", "note": "Built his political career in the Delaware General Assembly and New Castle County — the state-level experience that led to his gubernatorial election"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 38)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
