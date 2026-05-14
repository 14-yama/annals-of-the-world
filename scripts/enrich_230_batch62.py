#!/usr/bin/env python3
"""
Batch 62 — 8 entities: Richard Skinner, Elias Petty Seeley, Godfrey Giffard,
Joseph Burns, Christian Ernst von Bentzel-Sternau, Hugh Henry Brackenridge,
John Morin Scott, José Tomás Ovalle
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

    ("richard-skinner", {
        "summary": (
            "Richard Skinner (1778–1833) was "
            "an American Democratic-Republican "
            "politician from Vermont who served "
            "as Governor of Vermont (1820–1823) "
            "and as a U.S. Representative (1813–1815). "
            "His governorship coincided with "
            "the Era of Good Feelings and the "
            "Missouri Crisis — the apparently "
            "harmonious surface of American "
            "politics under Monroe masking "
            "the deep sectional tensions "
            "over slavery's expansion that "
            "the Missouri Compromise temporarily "
            "resolved.\n\n"
            "Vermont was a distinctive state "
            "in this era — admitted in 1791 "
            "as the fourteenth state, it had "
            "developed a strong anti-slavery "
            "tradition rooted in its Puritan "
            "and Congregationalist culture, "
            "its free-labor farming economy, "
            "and its New England moral reform "
            "heritage. Vermont was one of "
            "the states most opposed to "
            "Missouri's admission as a slave "
            "state during the Missouri Crisis.\n\n"
            "Skinner served as a Vermont "
            "congressman during the War of "
            "1812 — a conflict that New "
            "England states like Vermont "
            "had opposed as 'Mr. Madison's War,' "
            "reflecting the region's commercial "
            "ties to Britain and its Federalist "
            "political sympathies even as "
            "Vermont's government was "
            "controlled by Democratic-Republicans.\n\n"
            "His career reflected Vermont's "
            "early antislavery political tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Governor (1820–1823) during the Missouri Crisis and Era of Good Feelings; Congressman during the War of 1812; governed a strongly antislavery New England state through the first major congressional debate over slavery's expansion.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's strongly anti-slavery political tradition — rooted in the state's Puritan heritage, free-labor farming economy, and New England moral culture — created the political environment in which Skinner governed, making Vermont one of the most consistent opponents of slavery's expansion in the Missouri Crisis debates",
            "The Era of Good Feelings' surface political consensus — the collapse of Federalist opposition that left Democratic-Republicans as the only organized party — reduced political competition and created relatively easy pathways to gubernatorial office for connected figures like Skinner",
            "The War of 1812's divisive impact on New England — the region's commercial and cultural ties to Britain, its Federalist political sympathies, and the Hartford Convention's near-secessionist response — created the political backdrop for Skinner's wartime congressional service as a Democratic-Republican in an ambivalent state"
        ],
        "effects": [
            "His governorship managed Vermont's affairs during the Missouri Crisis — governing one of the most strongly antislavery states through the congressional debate that produced the Missouri Compromise of 1820",
            "His Vermont administration contributed to the state's institutional development during the post-War of 1812 years — managing the economic dislocations and political transitions of the Era of Good Feelings in a small New England state",
            "His career contributed to Vermont's Democratic-Republican political tradition — helping maintain the party's dominance in a state where Federalist sentiment remained strong among the commercial classes",
            "His career illustrated Vermont's early political identity as a distinctively antislavery northern state — one that would become even more strongly antislavery as the antebellum period deepened and eventually become one of the most reliable Republican states after the party's 1854 founding"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1820–1823"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1813–1815"},
            {"target": "missouri-compromise", "verb": "GOVERNS_DURING", "note": "Governor during Missouri Crisis 1820–1821"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Governed during the Monroe era"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Congressman during the War of 1812"}
        ]
    }),

    ("elias-petty-seeley", {
        "summary": (
            "Elias Petty Seeley (1791–1846) was "
            "an American Democratic politician "
            "from New Jersey who served in the "
            "U.S. House of Representatives "
            "(1833–1835). His brief congressional "
            "career placed him in the House "
            "during the height of Jackson's "
            "second term — the Bank War's "
            "denouement with the removal of "
            "federal deposits from the Second "
            "Bank of the United States, the "
            "Senate's censure of Jackson, "
            "and the consolidation of the "
            "Democratic and Whig parties "
            "as the second American party "
            "system.\n\n"
            "New Jersey in this period was "
            "one of the more politically "
            "competitive states in the "
            "mid-Atlantic region — a state "
            "where Jacksonian Democrats "
            "and Whigs competed closely "
            "for voters, reflecting the "
            "state's mixed economy of "
            "manufacturing, commerce, "
            "and farming.\n\n"
            "Seeley's single congressional "
            "term contributed New Jersey's "
            "Democratic voice to the "
            "House's deliberations during "
            "the climactic years of the "
            "Bank War controversy — one "
            "of the defining political "
            "struggles of Jacksonian "
            "America.\n\n"
            "He is one of the more obscure "
            "figures of Jacksonian congressional politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 3,
            "significanceNarrative": "New Jersey Democratic Congressman (1833–1835) during the Bank War's climax; served as Jackson removed federal deposits from the Second Bank; part of the competitive mid-Atlantic Democratic congressional bloc in the second American party system.",
            "significanceCategory": "local"
        },
        "causes": [
            "Andrew Jackson's Democratic coalition in New Jersey — the state's working-class, small-farmer, and artisan constituencies that aligned with Jacksonian populism against the 'money power' — provided the voter base that elected Seeley to Congress",
            "The Bank War's political mobilization — Jackson's campaign to destroy the Second Bank of the United States that galvanized Democratic voters against what Jacksonians portrayed as a corrupt financial monopoly — provided the defining issue of Seeley's congressional term",
            "New Jersey's competitive two-party politics — where Democrats and Whigs competed closely, making congressional seats genuinely contestable — created the political environment in which Seeley won his single term"
        ],
        "effects": [
            "His House service contributed New Jersey's Democratic vote to the House deliberations during the Bank War's climax — supporting Jackson's removal of federal deposits and the Democratic program against the Second Bank",
            "His single-term career illustrated the competitive nature of mid-Atlantic Democratic politics — where seats were won and lost in close elections reflecting the genuine competition between Democratic and Whig coalitions",
            "His career contributed to New Jersey's Democratic representation during the formation of the second American party system — when Democrats and Whigs were consolidating as the two dominant national parties",
            "His career illustrated the type of reliable but obscure Jacksonian Democratic backbencher who made up the bulk of Jackson's congressional majorities — loyal supporters of the president's agenda who served single or short terms without rising to national prominence"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Jersey Congressman 1833–1835"},
            {"target": "bank-war", "verb": "VOTES_DURING", "note": "In House during Bank War's climax"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat in House"},
            {"target": "new-jersey", "verb": "REPRESENTS", "note": "New Jersey Democratic congressman"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Member of the Jacksonian Democratic coalition"}
        ]
    }),

    ("godfrey-giffard", {
        "summary": (
            "Godfrey Giffard (c. 1235–1302) was "
            "an English medieval churchman and "
            "royal administrator who served as "
            "Bishop of Worcester (1268–1302) and "
            "as Lord Chancellor of England "
            "(1266–1268) under Henry III and "
            "the early years of Edward I. "
            "His career exemplified the dual "
            "role of senior ecclesiastic and "
            "royal administrator that "
            "characterized the high-medieval "
            "English church — bishops who "
            "served simultaneously as princes "
            "of the Church and as the king's "
            "chief ministers.\n\n"
            "Giffard rose through the royal "
            "administration during the "
            "turbulent reign of Henry III "
            "— the period of baronial opposition, "
            "Simon de Montfort's rebellion, "
            "and the second Barons' War "
            "(1264–1267) that ended with "
            "the royal victory at Evesham "
            "(1265). His chancellorship "
            "came in the war's immediate "
            "aftermath — the crucial period "
            "of restoration and reconciliation "
            "following the barons' defeat.\n\n"
            "His long Worcester bishopric "
            "(34 years) made him one of the "
            "most enduring prelates of "
            "the later thirteenth century "
            "— overseeing the diocese through "
            "the administrative transformations "
            "of Edward I's reforming reign.\n\n"
            "His brother Walter Giffard "
            "was Archbishop of York."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lord Chancellor of England (1266–1268) and Bishop of Worcester (1268–1302); administered England in the aftermath of Simon de Montfort's rebellion; long episcopate spanning Henry III and Edward I; brother of Archbishop of York Walter Giffard; key figure in post-baronial-war restoration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry III's need for capable royal administrators in the aftermath of the second Barons' War — the devastation of de Montfort's rebellion and the Dictum of Kenilworth's delicate reconciliation process required experienced royal ministers like Giffard to restore royal governance",
            "The medieval English church-state synthesis that used bishops as royal administrators — providing the king with literate, legally trained, administratively experienced clergymen whose ecclesiastical income the Crown did not have to pay while benefiting from their governmental service",
            "The Giffard family's prominence in English ecclesiastical and royal circles — the brothers Godfrey and Walter Giffard both achieving senior positions in the English church and royal administration illustrated the importance of family networks in thirteenth-century English political culture"
        ],
        "effects": [
            "His chancellorship contributed to the restoration of royal governance in the aftermath of the second Barons' War — helping Henry III and the young Edward manage the delicate reconciliation process after Evesham",
            "His long Worcester bishopric (1268–1302) contributed to diocesan governance through one of the most transformative periods in English ecclesiastical history — the administrative reforms, legal developments, and church-state negotiations of Edward I's reign",
            "His contribution to the Edwardian administrative achievement — Edward I's systematization of English law, governance, and royal power that laid the foundations of the later medieval English state — represented the ecclesiastical administrative expertise that made such transformation possible",
            "His career illustrated the crucial link between senior churchmen and royal administration in medieval England — the network of bishop-administrators without whom the English government could not have functioned"
        ],
        "relationships": [
            {"target": "bishop-of-worcester", "verb": "SERVES_AS", "note": "Bishop of Worcester 1268–1302"},
            {"target": "lord-chancellor-england", "verb": "SERVES_AS", "note": "Lord Chancellor 1266–1268"},
            {"target": "henry-iii-england", "verb": "SERVES", "note": "Royal administrator under Henry III"},
            {"target": "edward-i-england", "verb": "SERVES", "note": "Bishop during Edward I's reforming reign"},
            {"target": "walter-giffard", "verb": "SIBLING_OF", "note": "Brother was Archbishop of York"}
        ]
    }),

    ("joseph-burns", {
        "summary": (
            "Joseph Burns (1779–1844) was an "
            "American politician from Ohio who "
            "served in the U.S. House of "
            "Representatives (1833–1835) during "
            "the Jacksonian era. Ohio by the "
            "1830s had become one of the "
            "most populous states in the "
            "American West — its rapid settlement, "
            "agricultural productivity, and "
            "access to the Ohio River and "
            "Great Lakes trade routes had "
            "made it a major political force "
            "in national politics. Ohio's "
            "large congressional delegation "
            "made it a key prize in the "
            "competitions between Jacksonian "
            "Democrats and Whigs.\n\n"
            "Burns served during the height "
            "of the Jacksonian era — the "
            "Bank War's climax, with Jackson's "
            "removal of federal deposits from "
            "the Second Bank and the Senate's "
            "extraordinary censure of the "
            "president. These controversies "
            "defined the political atmosphere "
            "of the 23rd Congress in which "
            "Burns served.\n\n"
            "Ohio's complex political landscape "
            "— divided between Jacksonian "
            "Democrats in the southern "
            "counties settled by Virginians "
            "and Kentuckians, and more "
            "Whig-leaning northern counties "
            "settled by New Englanders "
            "— made it a genuinely competitive "
            "state throughout the Jacksonian era.\n\n"
            "Burns represented Ohio's Democratic tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 3,
            "significanceNarrative": "Ohio Democratic Congressman (1833–1835) during the Jacksonian Bank War; served during the 23rd Congress as Jackson removed federal deposits from the Second Bank; part of Ohio's growing congressional delegation in the rapidly developing Northwest.",
            "significanceCategory": "local"
        },
        "causes": [
            "Ohio's rapid population growth and increasing political weight — the state's explosive settlement in the early nineteenth century made it one of the most important states in the West, creating a large congressional delegation that included Democratic members like Burns",
            "The Bank War's political mobilization — Jackson's campaign against the Second Bank of the United States that galvanized Jacksonian Democrats across the country — provided the defining issue of Burns's congressional term",
            "Ohio's mixed political landscape — the state's division between Democratic-leaning southern counties and Whig-leaning northern counties — created competitive congressional races that Burns won in his district"
        ],
        "effects": [
            "His House service contributed Ohio's Democratic vote to the 23rd Congress's deliberations during the Bank War's climax — participating in the legislative battles over bank recharter, deposit removal, and the Senate's censure of Jackson",
            "His career contributed to Ohio's Democratic representation in the Jacksonian era — one of many Ohio Democrats who helped give Jackson reliable majorities in the House during his second term",
            "His career illustrated Ohio's growing political importance — as the state's population and congressional delegation grew, its role in national politics expanded, making Ohio's House members part of the crucial Democratic majority that sustained Jackson's program",
            "His single-term career illustrated the competitive nature of Ohio politics — where Jacksonian Democrats and Whigs competed closely, making many House seats genuinely contestable rather than safe"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Ohio Congressman 1833–1835"},
            {"target": "bank-war", "verb": "VOTES_DURING", "note": "In House during Bank War climax"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio Democratic congressman"},
            {"target": "23rd-us-congress", "verb": "SERVES_IN", "note": "Member of the 23rd Congress"}
        ]
    }),

    ("christian-ernst-von-bentzel-sternau", {
        "summary": (
            "Christian Ernst von Bentzel-Sternau "
            "(1767–1849) was a German jurist, "
            "statesman, and writer who served "
            "as a senior official in the "
            "Confederation of the Rhine — "
            "Napoleon's reorganization of "
            "German territories into a "
            "French satellite state system "
            "— and subsequently in the "
            "Grand Duchy of Frankfurt. "
            "His career bridged the old "
            "Holy Roman Empire, the Napoleonic "
            "reorganization of Germany, and "
            "the post-1815 Restoration era, "
            "making him one of the German "
            "administrative professionals "
            "who helped construct the "
            "new political entities that "
            "Napoleon created out of the "
            "fragments of the collapsed empire.\n\n"
            "Von Bentzel-Sternau was also "
            "a literary figure — writing "
            "satirical and philosophical "
            "works in the tradition of "
            "German Enlightenment literature. "
            "His dual career as jurist-administrator "
            "and man of letters placed him "
            "in the tradition of German "
            "Enlightenment figures who "
            "combined governmental service "
            "with intellectual production.\n\n"
            "His Confederation of the Rhine "
            "service contributed to the "
            "administrative transformation "
            "of the German territories "
            "under Napoleonic influence "
            "— the rationalization of law, "
            "the abolition of feudal institutions, "
            "and the introduction of the "
            "Napoleonic Code that left "
            "lasting marks on German legal culture.\n\n"
            "He lived to 82, witnessing the "
            "Restoration, the 1848 revolution, "
            "and German liberalism's rise."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "German jurist, statesman, and writer who served in Napoleon's Confederation of the Rhine; contributed to the administrative transformation of Germany under Napoleonic influence; dual career as administrator and Enlightenment-era literary figure; witnessed events from the Holy Roman Empire's collapse to the 1848 revolution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's dissolution of the Holy Roman Empire (1806) and creation of the Confederation of the Rhine — the reorganization of German territories into French satellite states — created the new administrative entities that required trained German jurists like Bentzel-Sternau to staff them",
            "The German Enlightenment's tradition of jurist-administrators who combined legal service with philosophical and literary production — figures like Goethe, Schiller, and Herder who served princes while producing intellectual work — provided the cultural model for Bentzel-Sternau's dual career",
            "The Napoleonic Code's extension into the Confederation of the Rhine territories — replacing the chaos of local customary laws with a rationalized legal code — created the administrative transformation that Bentzel-Sternau helped implement"
        ],
        "effects": [
            "His Confederation of the Rhine service contributed to the Napoleonic administrative transformation of Germany — implementing the legal and administrative reforms that rationalized German governance and left lasting marks on German legal culture even after Napoleon's defeat",
            "His literary output contributed to the German Enlightenment and early Romantic traditions — the intellectual culture of the German-speaking world that was simultaneously engaging with French revolutionary ideas and developing distinctively German cultural forms",
            "His survival through the 1815 Restoration — when the Confederation of the Rhine was dissolved and the German Confederation replaced it — illustrated the career continuity that trained German administrators achieved by adapting their expertise to successive regimes",
            "His long life (1767–1849) made him a witness to the full arc of German political transformation — from the Holy Roman Empire through Napoleon, the Restoration, and the 1848 revolutions that his Enlightenment generation had helped make intellectually possible"
        ],
        "relationships": [
            {"target": "confederation-of-the-rhine", "verb": "SERVES_IN", "note": "Senior official in Napoleon's German satellite state"},
            {"target": "grand-duchy-of-frankfurt", "verb": "SERVES_IN", "note": "Administrator in Napoleonic Frankfurt"},
            {"target": "napoleonic-code", "verb": "IMPLEMENTS", "note": "Helped implement French legal reforms in Germany"},
            {"target": "holy-roman-empire", "verb": "BORN_INTO", "note": "Formed under the old Empire before its dissolution"},
            {"target": "german-enlightenment", "verb": "PART_OF", "note": "Jurist-writer in the German Enlightenment tradition"}
        ]
    }),

    ("hugh-henry-brackenridge", {
        "summary": (
            "Hugh Henry Brackenridge (1748–1816) "
            "was a Scottish-born American "
            "writer, jurist, and politician "
            "who became one of the most "
            "significant literary figures "
            "of the early American republic. "
            "His novel 'Modern Chivalry' "
            "(published in multiple installments "
            "1792–1815) — a picaresque satire "
            "of American democracy modeled "
            "on Don Quixote — is considered "
            "the first American novel to engage "
            "seriously with the problems "
            "of democratic governance and "
            "the social contradictions of "
            "the new republic.\n\n"
            "Brackenridge graduated from "
            "Princeton (1771) with classmates "
            "Philip Freneau and James Madison. "
            "He was a Revolutionary War chaplain, "
            "frontier lawyer in Pittsburgh, "
            "founder of the Pittsburgh Gazette "
            "(the city's first newspaper), "
            "and eventually a Justice of "
            "the Pennsylvania Supreme Court.\n\n"
            "His political career included "
            "a brief stint in the Pennsylvania "
            "legislature, where he supported "
            "the Whiskey Rebellion "
            "moderates' position in 1794 "
            "— arguing against the tax "
            "while opposing violent resistance. "
            "His nuanced position during "
            "the Whiskey Rebellion "
            "illustrated his characteristic "
            "independence.\n\n"
            "'Modern Chivalry' remains his "
            "most lasting contribution — "
            "a prescient critique of populist democracy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Scottish-born American writer, jurist, and politician; author of 'Modern Chivalry' (1792–1815) — the first American novel to seriously engage democratic governance's problems; Princeton classmate of Madison and Freneau; Revolutionary War chaplain, Pittsburgh frontier lawyer, founder of the Pittsburgh Gazette, Pennsylvania Supreme Court Justice.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Princeton's revolutionary-era intellectual culture — the College of New Jersey's vigorous training in rhetoric, political philosophy, and classical literature that Brackenridge shared with classmates Madison and Freneau — formed the literary and political sensibility that made Modern Chivalry possible",
            "The early American republic's democratic experiment — the tension between the Founders' ideals of enlightened republican governance and the messy realities of populist democracy, demagoguery, and the manipulation of uneducated voters — provided the subject matter for Modern Chivalry's satirical critique",
            "The Pittsburgh frontier's social diversity — lawyers, farmers, Scots-Irish settlers, Native Americans, and newly arrived immigrants creating a genuinely pluralistic society with rough democratic habits — provided Brackenridge the characters, settings, and social observations that populated Modern Chivalry"
        ],
        "effects": [
            "Modern Chivalry's long publication (1792–1815) established one of the first sustained American literary engagements with democracy's contradictions — the novel's satire of voter manipulation, demagoguery, and the gap between democratic ideals and populist realities anticipated issues that American democracy would grapple with for centuries",
            "His founding of the Pittsburgh Gazette (1786) — the first newspaper in what would become western Pennsylvania — contributed to the development of frontier civic culture and the free press tradition in the American West",
            "His Pennsylvania Supreme Court service contributed to the development of Pennsylvania's legal tradition — his judicial opinions and legal culture contributed to the Common Law development of one of America's most legally complex states",
            "His moderated position during the Whiskey Rebellion — opposing the whiskey tax while opposing violent resistance — illustrated the intellectual independence that characterized his career and contributed to the peaceful resolution of the crisis"
        ],
        "relationships": [
            {"target": "modern-chivalry", "verb": "WRITES", "note": "First major American democratic novel (1792–1815)"},
            {"target": "pennsylvania-supreme-court", "verb": "SERVES_AS_JUSTICE", "note": "Justice of the Pennsylvania Supreme Court"},
            {"target": "whiskey-rebellion", "verb": "MODERATES", "note": "Argued against the tax while opposing violent resistance"},
            {"target": "james-madison", "verb": "CLASSMATE_OF", "note": "Princeton classmate of the future president"},
            {"target": "pittsburgh-gazette", "verb": "FOUNDS", "note": "Founded Pittsburgh's first newspaper in 1786"}
        ]
    }),

    ("john-morin-scott", {
        "summary": (
            "John Morin Scott (1730–1784) was "
            "an American lawyer, politician, "
            "and Revolutionary War general "
            "from New York who was one of "
            "the leading figures of New York "
            "City's patriot movement. A member "
            "of the triumvirate of New York "
            "lawyers (with William Livingston "
            "and William Smith Jr.) who dominated "
            "the colonial legal culture and "
            "political opposition in the 1750s "
            "and 1760s, Scott helped lay the "
            "intellectual and organizational "
            "foundations of New York's "
            "Revolutionary movement.\n\n"
            "Scott was educated at Yale and "
            "built a successful legal practice "
            "in New York City before becoming "
            "politically active in opposition "
            "to British colonial policies. "
            "His essays in the Independent "
            "Reflector (1752–1753) — the "
            "influential opposition journal "
            "he co-edited with Livingston "
            "and Smith — established him "
            "as one of colonial New York's "
            "leading public intellectuals.\n\n"
            "During the Revolution, Scott "
            "served as a brigadier general "
            "in the New York militia and "
            "participated in the disastrous "
            "Battle of Long Island (1776). "
            "After the war, he served in "
            "the Continental Congress and "
            "as New York Secretary of State.\n\n"
            "His death in 1784 cut short "
            "his role in the new republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York Revolutionary War general and patriot leader; co-editor of the Independent Reflector (1752–1753); member of the influential legal triumvirate with Livingston and Smith; participated in the Battle of Long Island (1776); served in Continental Congress and as New York Secretary of State.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's colonial legal culture — the thriving legal profession that gave ambitious lawyers like Scott, Livingston, and Smith the intellectual training, public platform, and social connections to become influential political figures — provided the base for Scott's political career",
            "The Independent Reflector's opposition journalism (1752–1753) — the influential journal that the triumvirate used to argue against Anglican establishment of a New York college (which became King's College/Columbia), for civil liberties, and against arbitrary government — established Scott's reputation as a defender of colonial liberties",
            "The American Revolution's radicalization of New York's patriot movement — the conflicts over taxation, the Stamp Act, the Townshend duties, and ultimately independence — transformed Scott from a colonial opposition lawyer into a revolutionary general and political leader"
        ],
        "effects": [
            "His co-editorship of the Independent Reflector contributed to New York's pre-Revolutionary intellectual culture — establishing a tradition of principled opposition to British colonial policy and defense of civil liberties that influenced the patriot movement",
            "His Revolutionary War generalship contributed to the patriot military effort in the disastrous New York campaign of 1776 — the Battle of Long Island and the loss of New York City to the British that tested the Continental Army's survival",
            "His Continental Congress service and New York Secretary of State role contributed to the development of the new American state's institutions — the post-war political work of building representative government on the Revolution's foundations",
            "His legal triumvirate with Livingston and Smith — New York's most influential legal-intellectual partnership of the colonial era — shaped the legal culture and political thought of New York's revolutionary generation"
        ],
        "relationships": [
            {"target": "independent-reflector", "verb": "CO-EDITS", "note": "Co-editor of the influential colonial opposition journal 1752–1753"},
            {"target": "american-revolution", "verb": "FIGHTS_IN", "note": "Brigadier general in New York Revolutionary forces"},
            {"target": "battle-of-long-island", "verb": "PARTICIPATES_IN", "note": "Fought in the disastrous 1776 New York campaign"},
            {"target": "continental-congress", "verb": "SERVES_IN", "note": "New York delegate to Continental Congress"},
            {"target": "william-livingston", "verb": "COLLABORATES_WITH", "note": "Member of the influential New York legal triumvirate"}
        ]
    }),

    ("josé-tomás-ovalle", {
        "summary": (
            "José Tomás Ovalle (1788–1831) was "
            "a Chilean lawyer and politician "
            "who served as President of Chile "
            "from July 1830 to March 1831 "
            "— technically as 'acting President' "
            "— during the critical period "
            "following the Conservative "
            "victory in the Battle of Lircay "
            "(April 1830). His presidency "
            "was a transitional administration "
            "that bridged the chaos of "
            "Chile's Liberal period and "
            "the long Conservative dominance "
            "that the 1833 constitution "
            "would institutionalize.\n\n"
            "Ovalle came to power as part "
            "of the Conservative faction's "
            "victory that defeated the "
            "Liberals in the Chilean civil "
            "war of 1829–1830. His administration "
            "was dominated by the real "
            "political power behind the "
            "Conservative triumph — Diego "
            "Portales, the conservative "
            "statesman who served as Ovalle's "
            "minister and effectively "
            "controlled the government.\n\n"
            "His death in office in March "
            "1831 from illness ended "
            "his brief presidency, but "
            "his administration had set "
            "in motion the constitutional "
            "drafting process that produced "
            "the 1833 Constitution — "
            "the conservative charter "
            "that governed Chile for "
            "over ninety years.\n\n"
            "He was a transitional figure "
            "in Chile's Conservative consolidation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Acting President of Chile (1830–1831) during the Conservative consolidation after the Battle of Lircay; nominal head of state while Diego Portales controlled real power; set in motion the constitutional drafting process that produced Chile's 1833 Constitution governing the country for over ninety years; died in office.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Conservative victory at the Battle of Lircay (April 1830) — the decisive battle of the Chilean civil war of 1829–1830 that defeated the Liberal-'pipiolo' faction and gave the Conservative-'pelucón' coalition control of the Chilean government — created the political context for Ovalle's assumption of power",
            "Diego Portales's political genius and Conservative ideology — his vision of a strong, centralized Chilean state governed by an elite of conservative landowners, merchants, and clergy — provided the intellectual and practical direction that Ovalle's administration nominally led",
            "Chile's post-independence constitutional instability — the failure of multiple liberal constitutions in the 1820s that had produced political chaos — created the Conservative argument for a stronger, more authoritarian constitutional order that Ovalle's administration began to construct"
        ],
        "effects": [
            "His administration initiated the drafting process for the 1833 Chilean Constitution — the conservative charter that created a strong presidency, preserved traditional social hierarchies, and provided Chile with exceptional political stability for over ninety years",
            "His presidency consolidated the Conservative faction's control of Chilean governance — establishing the political dominance that the Portales-era Conservatives would maintain for decades through the 1833 constitution's strong presidential system",
            "His death in office (March 1831) contributed to the political continuity of the Conservative project — rather than destabilizing it, his death allowed the process of constitutional drafting to continue under Conservative control",
            "His transitional presidency illustrated the pattern of Latin American post-independence politics — the oscillation between liberal and conservative factions that the region's new republics experienced as they sought stable constitutional forms"
        ],
        "relationships": [
            {"target": "chile", "verb": "GOVERNS", "note": "Acting President of Chile 1830–1831"},
            {"target": "diego-portales", "verb": "GOVERNED_ALONGSIDE", "note": "Nominal president while Portales controlled real power"},
            {"target": "chilean-constitution-1833", "verb": "INITIATES", "note": "Administration began drafting process for the 1833 constitution"},
            {"target": "battle-of-lircay", "verb": "EMPOWERED_BY", "note": "Rose to power following Conservative victory"},
            {"target": "conservative-chile", "verb": "REPRESENTS", "note": "Transitional figure in Chilean Conservative consolidation"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 62 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
