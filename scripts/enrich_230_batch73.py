#!/usr/bin/env python3
"""
Batch 73 — 8 entities: Samuel S. Phelps, André Joseph Abrial, John Hastings,
Ralph Metcalf, John Bell, John Mattocks, François Damboise, Thomas B. Jackson
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

    ("samuel-s-phelps", {
        "summary": (
            "Samuel Shethar Phelps "
            "(1793–1855) was an American "
            "Whig politician and jurist "
            "from Vermont who served "
            "as a U.S. Senator (1839–1851) "
            "and as a Vermont Supreme "
            "Court Justice. One of "
            "Vermont's most distinguished "
            "antebellum senators, "
            "Phelps served through "
            "the entire period from "
            "the Van Buren administration "
            "through the Compromise "
            "of 1850 — a twelve-year "
            "Senate tenure that spanned "
            "the Tyler administration's "
            "chaos, the Polk-era "
            "expansionism, and the "
            "slavery sectional crisis's "
            "escalation to the "
            "Compromise of 1850.\n\n"
            "As a Vermont Whig, "
            "Phelps represented "
            "one of the most reliably "
            "antislavery constituencies "
            "in the Senate — "
            "Vermont's granite "
            "Whig tradition was "
            "among the most "
            "consistently hostile "
            "to slavery extension "
            "of any state.\n\n"
            "His Vermont Supreme "
            "Court service contributed "
            "to the development "
            "of Vermont's distinguished "
            "legal tradition — "
            "the state that produced "
            "some of the clearest "
            "antislavery judicial "
            "decisions in antebellum "
            "America.\n\n"
            "He was a significant "
            "figure in Vermont "
            "law and politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vermont Whig Senator (1839–1851) and Supreme Court Justice; twelve-year Senate tenure through Van Buren, Tyler, Polk, and Taylor administrations; represented Vermont's reliably antislavery Whig constituency; served through the Compromise of 1850; significant figure in Vermont's antebellum law and politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Whig political tradition — the state's overwhelming identification with the American System, moral antislavery sentiment, and Protestant evangelical reform culture that made Vermont one of the most reliably Whig and antislavery states in the Union — created the political foundation for Phelps's twelve-year Senate career",
            "The escalating slavery sectional crisis — the series of controversies from the Texas annexation through the Mexican-American War and the Compromise of 1850 that dominated American politics during Phelps's Senate tenure — created the major political challenges that his career navigated",
            "Vermont's legal culture — the state's tradition of clear legal thinking and antislavery judicial decisions that made Vermont courts among the most hostile to slavery's legal claims — provided the judicial environment for Phelps's Supreme Court service"
        ],
        "effects": [
            "His twelve-year Senate tenure contributed Vermont's consistently antislavery Whig perspective to the most consequential debates of the antebellum era — the Texas annexation, Mexican-American War, Wilmot Proviso, and Compromise of 1850",
            "His Vermont Supreme Court service contributed to the development of Vermont's distinguished legal tradition — the antislavery jurisprudence that made Vermont courts among the most willing to protect fugitive slaves and challenge the Fugitive Slave Act",
            "His career contributed to the Vermont Whig tradition that would eventually produce Vermont's rock-solid Republicanism — the political culture that made Vermont the most reliably Republican state from 1856 through the twentieth century",
            "His long Senate tenure made him one of Vermont's most influential antebellum political voices — contributing the state's moral weight to the Senate debates that preceded the Civil War"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1839–1851"},
            {"target": "vermont-supreme-court", "verb": "SERVES_ON", "note": "Vermont Supreme Court Justice"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig in the antislavery tradition"},
            {"target": "compromise-of-1850", "verb": "SERVES_THROUGH", "note": "Senator through the compromise settlement"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Vermont's granite Whig senatorial voice"}
        ]
    }),

    ("andré-joseph-abrial", {
        "summary": (
            "André Joseph Abrial "
            "(1750–1828) was a French "
            "jurist and administrator "
            "who served as France's "
            "Grand Judge and Minister "
            "of Justice (1799–1802) "
            "during the critical "
            "early Consulate period "
            "— the years when Napoleon "
            "was consolidating power "
            "and rewriting France's "
            "legal system. Abrial "
            "played a significant "
            "role in the development "
            "of the Napoleonic "
            "legal reforms — the "
            "process that produced "
            "the Civil Code (Code "
            "Napoléon, 1804) and "
            "transformed French "
            "and European law.\n\n"
            "His Ministership coincided "
            "with the Council of "
            "State's early work "
            "drafting the Civil Code "
            "— the committee process "
            "led by Portalis, Tronchet, "
            "Bigot de Préameneu, "
            "and Maleville that "
            "codified French private "
            "law into the most "
            "influential legal "
            "document of the "
            "modern era.\n\n"
            "Abrial had also "
            "served as French "
            "commissioner in "
            "the Cisalpine Republic "
            "(1799) — contributing "
            "to the spread of "
            "French revolutionary "
            "legal norms in Italy.\n\n"
            "He was a significant "
            "figure in early "
            "Napoleonic administration."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Grand Judge and Minister of Justice (1799–1802) during the critical early Consulate; served during the drafting process that produced the Civil Code (1804); French commissioner in the Cisalpine Republic spreading revolutionary legal norms to Italy; significant figure in the Napoleonic legal revolution that transformed European law.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's coup of 18 Brumaire (November 1799) — the seizure of power that established the Consulate and created the institutional framework within which Abrial's ministership operated — created the political context for his appointment",
            "The need for systematic legal reform — France's chaotic legal system, combining pre-revolutionary law with revolutionary legislation, required the systematic codification that the Consulate undertook — creating the major institutional project of Abrial's ministry",
            "Abrial's revolutionary credentials and legal expertise — his service through the revolutionary period and his established reputation in French law — provided the qualifications for Napoleon's justice ministerial appointment"
        ],
        "effects": [
            "His Ministry of Justice tenure contributed to the institutional conditions for drafting the Civil Code — the administrative environment within which Portalis's drafting committee worked and which Abrial's ministry supported",
            "His Cisalpine Republic service contributed to spreading French legal norms and revolutionary legal reforms to northern Italy — an important step in the broader Napoleonic project of imposing French legal culture across Europe",
            "His early Consulate service contributed to the consolidation of French legal administration after the revolutionary chaos — establishing the institutional foundations for the orderly system of justice that the Napoleonic codes required",
            "His career contributed to the development of the French Ministry of Justice as the institutional home of the new codified legal system — the ministry that would administer the Napoleonic codes throughout France and its satellites"
        ],
        "relationships": [
            {"target": "french-ministry-of-justice", "verb": "LEADS", "note": "Grand Judge and Minister of Justice 1799–1802"},
            {"target": "napoleon-bonaprte", "verb": "SERVES_UNDER", "note": "Consulate-era justice minister"},
            {"target": "code-napoleon", "verb": "CONTRIBUTES_TO", "note": "Minister during Civil Code's drafting process"},
            {"target": "cisalpine-republic", "verb": "SERVES_IN", "note": "French commissioner spreading revolutionary law to Italy"},
            {"target": "french-legal-revolution", "verb": "ADVANCES", "note": "Administrator of France's Napoleonic legal transformation"}
        ]
    }),

    ("john-hastings", {
        "summary": (
            "John Hastings (1778–1854) "
            "was an American Democratic "
            "politician from Ohio who "
            "served in the U.S. House "
            "of Representatives (1839–1843) "
            "during the Tyler administration "
            "and the opening controversies "
            "over Texas annexation "
            "and the slavery extension "
            "question. An Ohio Democrat, "
            "Hastings represented "
            "the Western frontier "
            "perspective — Ohio had "
            "been organized as a "
            "territory in 1787 and "
            "admitted as the first "
            "state from the "
            "Northwest Territory "
            "(1803) — in a state "
            "that was politically "
            "competitive between "
            "Whigs and Democrats.\n\n"
            "Ohio's political significance "
            "in the antebellum era "
            "was enormous — a "
            "large, competitive "
            "state that both parties "
            "had to win, with "
            "a complex population "
            "of New England migrants "
            "(Whig), Scots-Irish "
            "and Virginia migrants "
            "(Democratic), and "
            "German-American farmers "
            "whose allegiances "
            "were divided.\n\n"
            "His congressional "
            "service contributed "
            "Ohio's Democratic "
            "perspective to the "
            "major debates of "
            "the early 1840s.\n\n"
            "He was a farmer "
            "and businessman "
            "before politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Ohio Democratic Congressman (1839–1843); served during Tyler administration and Texas annexation opening; represented Ohio's frontier Democratic perspective; part of the competitive two-party politics of a key swing state in the antebellum era.",
            "significanceCategory": "local"
        },
        "causes": [
            "Ohio's competitive political geography — the state's complex population of New England Whigs, Virginia-heritage Democrats, and German-American farmers created genuine two-party competition — created both the challenge and opportunity for Hastings's Democratic congressional career",
            "The Tyler administration's political chaos — the Whig president expelled from his own party and unable to govern effectively — created the congressional environment of Hastings's House tenure",
            "Ohio's frontier Democratic tradition — the Jacksonian instincts of the state's Scots-Irish and Southern migrant population who settled the Ohio River valley and brought their Democratic political culture with them — provided the political base for Hastings's election"
        ],
        "effects": [
            "His House service contributed Ohio's Democratic votes to the Tyler era's congressional chaos — navigating the collapse of Whig unity and the beginning of the Texas annexation controversy",
            "His career contributed to Ohio's Democratic political tradition — the party infrastructure that would eventually support Van Buren's Free Soil movement and ultimately Lincoln's Republican coalition from the same Ohio political networks",
            "His service illustrated the pattern of Ohio Democratic politics in the Tyler era — the short congressional careers that reflected genuine party competition rather than one-party dominance",
            "His death in 1854 placed him among the Jacksonian generation who witnessed the opening of the slavery extension crisis but not the Civil War that resulted"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Ohio Congressman 1839–1843"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Ohio Jacksonian Democrat"},
            {"target": "john-tyler", "verb": "SERVES_DURING", "note": "Congressman during Tyler's chaotic presidency"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio frontier Democrat"},
            {"target": "texas-annexation", "verb": "SERVES_DURING", "note": "Congressman as Texas annexation controversy opened"}
        ]
    }),

    ("ralph-metcalf", {
        "summary": (
            "Ralph Metcalf (1798–1858) "
            "was an American Whig "
            "politician from New Hampshire "
            "who served as Governor "
            "of New Hampshire (1855–1857) "
            "during the politically "
            "turbulent aftermath of "
            "the Kansas-Nebraska Act "
            "(1854) — the legislation "
            "that repealed the Missouri "
            "Compromise, opened the "
            "territories to slavery "
            "by popular sovereignty, "
            "and shattered the Whig "
            "Party while giving birth "
            "to the Republican Party.\n\n"
            "Metcalf's governorship "
            "came at the moment "
            "of the Whig Party's "
            "final disintegration "
            "and the Republican "
            "Party's formation — "
            "he was the last Whig "
            "governor of New Hampshire "
            "as the party collapsed "
            "into the Republican "
            "coalition.\n\n"
            "New Hampshire's "
            "political history "
            "in this era was "
            "dominated by the "
            "Franklin Pierce "
            "connection — Pierce "
            "was a New Hampshire "
            "Democrat whose presidency "
            "(1853–1857) signed "
            "the Kansas-Nebraska "
            "Act and whose decisions "
            "drove the political "
            "realignment.\n\n"
            "Metcalf's Whig-to-Republican "
            "transition represented "
            "the path most Northern "
            "Whigs took in the "
            "mid-1850s realignment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of New Hampshire (1855–1857); last Whig governor as the party disintegrated after the Kansas-Nebraska Act; served during the founding of the Republican Party; represented the Whig-to-Republican transition of Northern antislavery Whigs; governed during the most politically turbulent period of the antebellum era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Kansas-Nebraska Act (1854) — the legislation that repealed the Missouri Compromise and opened the territories to slavery by popular sovereignty — created the political earthquake that destroyed the Whig Party and created the Republican Party",
            "New Hampshire's anti-slavery Whig tradition — the state's Protestant evangelical reform culture and its hostility to slavery extension — created the political constituency for a last Whig governor who would transition to Republicanism",
            "Franklin Pierce's Kansas-Nebraska Act signing — New Hampshire's own Democratic president signing the most divisive legislation of the antebellum era — created the political reaction in New Hampshire that helped Metcalf's anti-Nebraska Whig candidacy succeed"
        ],
        "effects": [
            "His governorship marked the transition moment in New Hampshire politics — the last Whig gubernatorial tenure before the state's antislavery Whigs merged with Free Soilers and anti-Nebraska Democrats to form the Republican coalition",
            "His term governed New Hampshire through the Bleeding Kansas crisis — the guerrilla violence between proslavery and antislavery settlers in Kansas that dramatized the Kansas-Nebraska Act's consequences",
            "His career illustrated the political transition that thousands of Northern Whigs made in the mid-1850s — the movement from Whig to Republican that created the new party's electoral base",
            "His death in 1858 — before the Lincoln-Douglas debates and the 1860 election — placed him among those who witnessed the political realignment's beginnings but not the Civil War it precipitated"
        ],
        "relationships": [
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor 1855–1857"},
            {"target": "whig-party-united-states", "verb": "REPRESENTS_LAST", "note": "Last Whig governor of New Hampshire"},
            {"target": "republican-party-united-states", "verb": "TRANSITIONS_TO", "note": "Whig-to-Republican transition figure"},
            {"target": "kansas-nebraska-act", "verb": "GOVERNS_DURING", "note": "Governor during the political earthquake of 1854"},
            {"target": "bleeding-kansas", "verb": "GOVERNS_DURING", "note": "Governor during Kansas territory violence"}
        ]
    }),

    ("john-bell", {
        "summary": (
            "John Bell (1796–1869) was "
            "an American politician from "
            "Tennessee who had one of "
            "the most consequential "
            "political careers of the "
            "antebellum era — serving "
            "as Speaker of the U.S. "
            "House (1834–1835), Secretary "
            "of War (1841) under Harrison "
            "and Tyler, U.S. Senator "
            "(1847–1859), and the "
            "Constitutional Union Party's "
            "presidential candidate "
            "in 1860 — receiving 39 "
            "electoral votes (Virginia, "
            "Kentucky, Tennessee) "
            "in the four-way election "
            "that sent Lincoln to the "
            "presidency and the "
            "South to secession.\n\n"
            "Bell was a Southern "
            "Unionist who opposed "
            "both secession and "
            "the coercion of the "
            "South — the Constitutional "
            "Union Party's middle "
            "ground between Northern "
            "Republicans and Southern "
            "secessionists that the "
            "1860 election demonstrated "
            "was no longer viable.\n\n"
            "He had opposed the "
            "Kansas-Nebraska Act "
            "(1854) and opposed "
            "secession in 1861 "
            "— but eventually "
            "supported Tennessee's "
            "secession after "
            "Fort Sumter.\n\n"
            "His career traced "
            "the Southern Unionist "
            "tradition's tragic arc."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Speaker of the House (1834–1835), Secretary of War (1841), Senator (1847–1859), and Constitutional Union presidential candidate (1860) — won Virginia, Kentucky, and Tennessee's 39 electoral votes; Southern Unionist who opposed both secession and Northern coercion; opposed the Kansas-Nebraska Act; eventually supported Tennessee's secession after Fort Sumter; his career traced the Southern Unionist tradition's tragic arc.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Tennessee's complex political geography — the state's division between East Tennessee's Unionist Appalachian culture, Middle Tennessee's Whig commercial elite, and West Tennessee's plantation slavery — created the political environment for Bell's moderate, Union-preserving political career",
            "The disintegration of the second party system — the collapse of the Whig Party after the Kansas-Nebraska Act and the failure to find a middle ground between Northern antislavery and Southern pro-slavery politics — created the political vacuum that Bell's Constitutional Union Party attempted to fill in 1860",
            "The 1860 election's four-way fragmentation — Lincoln (Republican), Douglas (Northern Democrat), Breckinridge (Southern Democrat), and Bell (Constitutional Union) — created the electoral map within which Bell won the three border Upper South states by appealing to conditional Unionists"
        ],
        "effects": [
            "His 1860 presidential campaign — winning Virginia, Kentucky, and Tennessee — demonstrated that a meaningful portion of the Upper South was still committed to Union preservation over secession, a political reality that Lincoln's administration would try to exploit",
            "His Constitutional Union Party's 39 electoral votes illustrated the fatal weakness of the middle position — there were not enough conditional Unionists in enough states to prevent Lincoln's election or block secession",
            "His eventual support for Tennessee's secession after Fort Sumter — despite his Unionist record — illustrated the tragic dilemma of Southern Unionists when forced to choose between Union and Southern solidarity",
            "His House Speakership and War Secretaryship contributed to the institutional development of the antebellum federal government — including a key role in the development of the West Point military curriculum during his War Department tenure"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_AS_SPEAKER_OF", "note": "Speaker 1834–1835"},
            {"target": "us-department-of-war", "verb": "LEADS", "note": "Secretary of War 1841 under Harrison/Tyler"},
            {"target": "constitutional-union-party", "verb": "LEADS", "note": "1860 presidential candidate"},
            {"target": "election-of-1860", "verb": "PARTICIPATES_IN", "note": "Won 39 electoral votes in four-way race"},
            {"target": "tennessee", "verb": "REPRESENTS", "note": "Tennessee Senator and Southern Unionist"}
        ]
    }),

    ("john-mattocks", {
        "summary": (
            "John Mattocks (1777–1847) "
            "was an American Whig politician "
            "from Vermont who served "
            "as a U.S. Representative "
            "(1821–1823 and 1841–1843) "
            "and briefly as Governor "
            "of Vermont (1843). "
            "His two non-consecutive "
            "House stints bracket "
            "a twenty-year gap "
            "— representing a political "
            "career interrupted by "
            "professional legal work "
            "and civic activity "
            "before returning to "
            "national politics in "
            "his mid-60s.\n\n"
            "Vermont's Whig tradition "
            "— the state's identification "
            "with the American System, "
            "antislavery sentiment, "
            "and Protestant reform "
            "culture — provided "
            "the political environment "
            "for Mattocks's career. "
            "His brief governorship "
            "came as the Whigs "
            "were at the height "
            "of their national "
            "influence following "
            "Harrison's 1840 "
            "election victory.\n\n"
            "His first House stint "
            "(1821–1823) coincided "
            "with the Missouri "
            "Compromise era and "
            "the Era of Good "
            "Feelings' political "
            "consensus.\n\n"
            "He was a prominent "
            "Vermont lawyer and "
            "community leader "
            "across his long career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Whig Congressman (1821–1823 and 1841–1843) and Governor (1843); two non-consecutive House stints bracketing twenty years of professional legal work; served during Missouri Compromise era and the Tyler era; representative of Vermont's Whig tradition; prominent Vermont lawyer across a long career.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Whig political culture — the state's Protestant evangelical reform tradition, its antislavery sentiment, and its support for Henry Clay's American System — created the political environment for Mattocks's Whig career",
            "The Whig Party's 1840 electoral triumph — the 'Tippecanoe and Tyler Too' campaign that swept Harrison to victory and gave the Whigs their first presidential success — created the high-water moment for the Whig Party that defined Mattocks's second House term and gubernatorial service",
            "Vermont's legal culture — the state's tradition of prominent local lawyers participating in civic and political life — provided the framework for Mattocks's combination of legal career and political service"
        ],
        "effects": [
            "His gubernatorial tenure contributed to Vermont's governance at the height of Whig power — managing state affairs during the politically turbulent Tyler administration",
            "His two House stints contributed Vermont's Whig perspective across two different eras — the Monroe era's Missouri Compromise debates and the Tyler era's Texas annexation and slavery extension controversies",
            "His career illustrated Vermont's distinctive political tradition — the combination of antislavery Whiggery, Protestant moral reform, and New England civic culture that made Vermont the most consistently principled antislavery state in the antebellum Union",
            "His long legal career contributed to Vermont's legal tradition — the jurisprudence of one of the most intellectually distinguished small states in the Union"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1821–1823 and 1841–1843"},
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1843"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig politician"},
            {"target": "missouri-compromise", "verb": "SERVES_DURING", "note": "Congressman during the compromise era"},
            {"target": "william-henry-harrison", "verb": "SERVES_AFTER", "note": "Congressman and governor during Whig ascendancy"}
        ]
    }),

    ("françois-damboise", {
        "summary": (
            "François Damboise (dates "
            "uncertain, fl. 16th c.) "
            "was a French jurist and "
            "legal scholar of the "
            "Renaissance era who "
            "contributed to the "
            "development of French "
            "customary law through "
            "his commentaries and "
            "legal treatises. He "
            "worked within the "
            "tradition of French "
            "humanist jurisprudence "
            "— the movement associated "
            "with figures like "
            "Charles Dumoulin and "
            "François Hotman who "
            "sought to systematize "
            "and rationalize French "
            "customary law through "
            "humanist philological "
            "methods.\n\n"
            "French customary law "
            "in the 16th century "
            "was a patchwork of "
            "regional customs — "
            "the coutumes of "
            "different provinces "
            "that varied widely "
            "and required scholarly "
            "commentary to make "
            "accessible and coherent. "
            "The royal government's "
            "efforts to codify "
            "and standardize these "
            "customs created the "
            "demand for the scholarly "
            "work that Damboise "
            "and his contemporaries "
            "provided.\n\n"
            "His legal scholarship "
            "contributed to the "
            "gradual rationalization "
            "of French private law "
            "that would eventually "
            "produce the Code Napoléon.\n\n"
            "He is a minor but "
            "real figure in French "
            "legal history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French Renaissance jurist (fl. 16th c.) contributing to French customary law through humanist jurisprudence; worked in the tradition of Dumoulin and Hotman systematizing regional coutumes; part of the scholarly movement rationalizing French private law that would eventually produce the Code Napoléon.",
            "significanceCategory": "regional"
        },
        "causes": [
            "French customary law's regional fragmentation — the patchwork of provincial coutumes that governed different parts of France and required scholarly commentary to make coherent — created the scholarly demand that Damboise's legal work addressed",
            "The French humanist jurisprudence movement — the application of Renaissance philological methods to legal texts, exemplified by Dumoulin's Coutumes de Paris commentary and Hotman's legal historicism — provided the intellectual framework for Damboise's scholarly approach",
            "The French royal government's customary law codification efforts — the Ordonnance of Villers-Cotterêts (1539) and subsequent royal efforts to standardize French law — created the institutional context for scholarly work on the coutumes"
        ],
        "effects": [
            "His legal commentaries contributed to the accumulating body of French customary law scholarship that successive generations of jurists used to understand, apply, and gradually harmonize regional customs",
            "His work contributed to the broader project of rationalizing French private law — the long-term process that, through many generations of legal scholarship, eventually produced the systematic private law that the Code Napoléon codified",
            "His scholarship contributed to the transmission of humanist jurisprudence — the application of classical learning and philological method to legal texts that was transforming European legal education",
            "His career illustrated the pattern of 16th-century French legal scholarship — the university-trained jurists whose commentaries, treatises, and codification efforts gradually built the scholarly infrastructure of French law"
        ],
        "relationships": [
            {"target": "french-customary-law", "verb": "DEVELOPS", "note": "Contributed to systematizing regional coutumes"},
            {"target": "french-humanist-jurisprudence", "verb": "WORKS_IN", "note": "Part of the Dumoulin-Hotman humanist legal tradition"},
            {"target": "charles-dumoulin", "verb": "CONTEMPORANEOUS_WITH", "note": "Contemporary in the French humanist legal tradition"},
            {"target": "french-renaissance", "verb": "CONTRIBUTES_TO", "note": "Renaissance-era legal scholar"},
            {"target": "code-napoleon", "verb": "PRECEDES", "note": "Early contributor to the scholarship that led to codification"}
        ]
    }),

    ("thomas-b-jackson", {
        "summary": (
            "Thomas Bickerton Jackson "
            "(1797–1881) was an American "
            "Democratic politician from "
            "New York who served in "
            "the U.S. House of Representatives "
            "(1837–1841) during the "
            "Van Buren administration "
            "and the Panic of 1837. "
            "A New York Democrat "
            "during one of the "
            "most politically complex "
            "periods of the state's "
            "history — the Barnburner-Hunker "
            "factional division was "
            "developing, the economic "
            "panic was devastating "
            "Van Buren's presidency, "
            "and the anti-slavery "
            "movement was becoming "
            "a significant political "
            "force — Jackson navigated "
            "the complex terrain "
            "of New York Democratic "
            "machine politics.\n\n"
            "New York's 1837 Panic "
            "was catastrophic — "
            "the state's commercial "
            "center, particularly "
            "New York City, was "
            "at the heart of the "
            "banking and credit "
            "crisis that the "
            "Jackson administration's "
            "Specie Circular had "
            "helped precipitate.\n\n"
            "His four-year House "
            "tenure made him part "
            "of the significant "
            "New York Democratic "
            "delegation during "
            "this critical period.\n\n"
            "He was a lawyer "
            "and businessman "
            "before politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "New York Democratic Congressman (1837–1841); served during the Panic of 1837 and Van Buren presidency; navigated New York's complex Barnburner-Hunker factional politics; part of the significant New York Democratic delegation during the transition from Jacksonian to Van Buren era.",
            "significanceCategory": "local"
        },
        "causes": [
            "New York's Democratic machine politics — the Van Buren-aligned Albany Regency organization that coordinated Democratic Party activities across the state — created the political structure within which Jackson's congressional candidacy operated",
            "The Panic of 1837 — the severe economic depression triggered by the Specie Circular and bank credit contraction — created the major political crisis of Jackson's House tenure and the vulnerability of Van Buren's presidency",
            "New York's importance as America's most commercially significant state — the state whose banking and commercial crisis was most dramatic during the Panic, and whose large congressional delegation made it a major force in national politics — created the significance of Jackson's seat"
        ],
        "effects": [
            "His House service contributed New York's Democratic votes to the Van Buren administration's economic policy responses — the Independent Treasury debates and the hard-money policies that Democrats advocated in response to the Panic",
            "His career contributed to the pattern of New York Democratic politics in the Van Buren era — the machine politics that would eventually fracture into Barnburners and Hunkers",
            "His four-year tenure illustrated the competitive nature of New York Democratic politics — the regular turnover of congressional seats in a state where both Whig and Democratic competition was intense",
            "His death in 1881 placed him among the extraordinarily long-lived antebellum politicians who witnessed the full arc from Jacksonian Democracy through the Civil War and into the Gilded Age"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1837–1841"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Democratic congressman during Van Buren presidency"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Congressman during the economic crisis"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "New York Democratic machine politician"},
            {"target": "albany-regency", "verb": "ASSOCIATED_WITH", "note": "Part of the Van Buren New York Democratic organization"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 73 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
