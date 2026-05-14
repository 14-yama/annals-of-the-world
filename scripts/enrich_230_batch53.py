#!/usr/bin/env python3
"""
Batch 53 — 8 entities: Jacques de Tourreil, Thomas L. Hamer, Ephraim King Wilson,
James Armstrong, Barthélemy Faujas de Saint-Fond, John Murphy,
Marcus Gjøe Rosenkrantz, Vasile Aaron
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

    # 1 — Jacques de Tourreil
    ("jacques-de-tourreil", {
        "summary": (
            "Jacques de Tourreil (1656–1714) was a French "
            "humanist scholar, translator, and member of "
            "the Académie française best known for his "
            "translations of the speeches of Demosthenes "
            "and Cicero — translations that became standard "
            "French renderings of these classical orators "
            "in the late seventeenth and early eighteenth "
            "centuries. His work embodied the ideals of "
            "the French classical tradition: precision, "
            "elegance, and fidelity to the spirit of "
            "ancient eloquence.\n\n"
            "Born in Castelnaudary (Languedoc), Tourreil "
            "received a thorough classical education and "
            "came to Paris where he attracted the "
            "patronage of eminent figures. He was elected "
            "to the Académie française in 1692, becoming "
            "part of the prestigious literary institution "
            "that set the standards of French language "
            "and letters under Louis XIV. His translation "
            "work placed him within the querelle des anciens "
            "et des modernes as a firm partisan of the "
            "Ancients — those who believed classical "
            "literature set an unsurpassable standard.\n\n"
            "His translations of Demosthenes were particularly "
            "admired: the Philippics and Olynthiacs rendered "
            "into clear, powerful French prose that captured "
            "the urgency and rhetorical force of the "
            "original Greek. His Cicero translations "
            "similarly sought to convey the architectural "
            "grandeur of Latin oratory in French.\n\n"
            "He later served as royal historian (historiographe "
            "du roi), the official position for documenting "
            "the reign of Louis XIV — combining his "
            "scholarly prestige with royal patronage."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French humanist scholar, Académie française member, and translator of Demosthenes and Cicero whose renderings became standard French versions of these classical orators; royal historian under Louis XIV; partisan of the Ancients in the querelle des anciens et des modernes.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French classical tradition's reverence for Greco-Roman oratory — which under Louis XIV elevated Demosthenes and Cicero as models of eloquence and civic virtue — created the scholarly demand for authoritative French translations that Tourreil supplied",
            "The Académie française's role as the arbiter of French literary standards and language — and its members' obligation to contribute to classical learning — provided the institutional framework within which Tourreil's translation project gained prestige and patronage",
            "The querelle des anciens et des modernes — the great French literary debate over whether ancient or modern literature was superior — aligned Tourreil with the Ancients whose position required demonstrating the living relevance of classical texts through translations that made them accessible to French readers"
        ],
        "effects": [
            "His translations of Demosthenes' Philippics and Olynthiacs became the standard French versions through which educated French readers encountered the great Athenian orator's political speeches — shaping the French reception of Demosthenes for generations",
            "His Cicero translations contributed to the enormous prestige of Ciceronian rhetoric in French literary and legal culture, reinforcing the classical oratorical model that dominated French public speaking from the court to the bar",
            "His election to the Académie française and service as royal historian confirmed his place in the Ancien Régime's prestige hierarchy of scholars — demonstrating how humanist classical scholarship could earn both academic honors and royal patronage",
            "His work contributed to the long French tradition of making the classical world accessible through translation — a tradition that shaped French education, rhetoric, and literary culture from the Grand Siècle through the Revolution"
        ],
        "relationships": [
            {"target": "academie-francaise", "verb": "MEMBER_OF", "note": "Elected member from 1692"},
            {"target": "demosthenes", "verb": "TRANSLATES", "note": "Standard French translations of Philippics and Olynthiacs"},
            {"target": "cicero", "verb": "TRANSLATES", "note": "French translations of Ciceronian orations"},
            {"target": "louis-xiv", "verb": "SERVES_UNDER", "note": "Royal historian (historiographe du roi)"},
            {"target": "querelle-des-anciens-et-des-modernes", "verb": "PARTICIPATES_IN", "note": "Partisan of the Ancients"}
        ]
    }),

    # 2 — Thomas L. Hamer
    ("thomas-l-hamer", {
        "summary": (
            "Thomas L. Hamer (1800–1846) was an American "
            "lawyer and Democratic Congressman from Ohio "
            "who is remembered in American history for "
            "two remarkable connections: he nominated "
            "Ulysses S. Grant to West Point in 1839, "
            "and he died of disease during the Mexican-American "
            "War at Monterrey — the very war in which "
            "the West Point cadet he had nominated "
            "first distinguished himself. His brief "
            "but consequential career traced the arc "
            "from frontier Ohio politics to the battlefield "
            "of Mexico.\n\n"
            "Born in Pennsylvania and raised in Ohio, "
            "Hamer was admitted to the bar and entered "
            "Democratic politics in the early Jacksonian "
            "era. He served three terms in the U.S. House "
            "of Representatives (1833–1839) where he "
            "was a reliable Jacksonian Democrat, supporting "
            "the independent treasury, opposing abolitionist "
            "petitions, and championing Ohio's interests "
            "in federal policy.\n\n"
            "His nomination of Ulysses Grant to West Point "
            "in 1839 — securing the appointment for his "
            "Georgetown, Ohio neighbor — was one of the "
            "most consequential acts of congressional "
            "patronage in American history, as it set "
            "Grant on the path to military command, "
            "and ultimately to the presidency.\n\n"
            "When the Mexican-American War broke out in "
            "1846, Hamer volunteered and received a "
            "brigadier general's commission. He died "
            "of dysentery at Monterrey, mourned as a "
            "capable commander whose potential went "
            "unfulfilled."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Ohio Democratic Congressman who nominated Ulysses S. Grant to West Point in 1839 — one of the most consequential acts of congressional patronage in American history; served three terms in Congress and died as a brigadier general in the Mexican-American War (1846); a pivotal though largely indirect figure in the story of Grant's rise.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Jacksonian Democratic political system's use of congressional patronage — in which congressmen controlled West Point nominations for their districts — placed Hamer in a position to nominate his neighbor Ulysses Grant to the military academy, exercising a routine act of political patronage that happened to have extraordinary historical consequences",
            "The Mexican-American War (1846–1848) — triggered by the US annexation of Texas and the disputed Texas-Mexico border — provided the military theater in which both Hamer and the young Grant he had nominated would test themselves, bringing Hamer's congressional and military careers to a simultaneous culmination and end",
            "Ohio frontier politics of the Jacksonian era — with its competitive Democratic-Whig contests, expansion of federal patronage, and strong military-civic culture — shaped Hamer's political career and his role as a community leader who dispensed federal appointments"
        ],
        "effects": [
            "His nomination of Ulysses Grant to West Point (1839) set in motion the military career that led to Grant's command of Union armies in the Civil War, his presidency of the United States (1869–1877), and his permanent place in American history — making Hamer's act of patronage among the most consequential nominations in congressional history",
            "His congressional service (1833–1839) represented the Jacksonian Democratic tradition in frontier Ohio — supporting the independent treasury, opposing abolitionism, and defending Ohio interests — contributing to the political culture that shaped Ohio's antebellum political development",
            "His death at Monterrey in 1846 contributed to the political mythology of the Mexican-American War — a conflict that killed numerous promising public figures and produced the military leaders who would face each other in the Civil War fifteen years later",
            "His story — the patron who died in the war made possible partly by the cadet he nominated — became a minor but evocative footnote in the American historical tradition, illustrating how individual acts of patronage could have unforeseeable historical consequences"
        ],
        "relationships": [
            {"target": "ulysses-s-grant", "verb": "NOMINATES", "note": "Nominated Grant to West Point in 1839"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Democratic Congressman from Ohio 1833–1839"},
            {"target": "mexican-american-war", "verb": "SERVES_IN", "note": "Died as brigadier general at Monterrey 1846"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Jacksonian Democrat in Ohio"},
            {"target": "west-point", "verb": "NOMINATES_TO", "note": "Congressional patron who secured Grant's West Point appointment"}
        ]
    }),

    # 3 — Ephraim King Wilson
    ("ephraim-king-wilson", {
        "summary": (
            "Ephraim King Wilson (1771–1834) was an American "
            "lawyer and Democratic-Republican politician "
            "from Maryland who served in the United States "
            "House of Representatives (1827–1833) and as "
            "a member of the Maryland state legislature. "
            "A representative of Maryland's Eastern Shore "
            "political culture, Wilson's career embodied "
            "the transition from the Jeffersonian "
            "Democratic-Republican tradition through "
            "the Jacksonian era that reshaped American "
            "party politics in the late 1820s.\n\n"
            "Maryland's Eastern Shore — the Chesapeake "
            "peninsula that had deep roots in tobacco "
            "agriculture, slavery, and the planter "
            "gentry culture — produced a distinctive "
            "political type: conservative, states'-rights "
            "oriented, suspicious of federal overreach, "
            "and deeply committed to the social order "
            "anchored by slave agriculture. Wilson "
            "represented this constituency in Congress "
            "during the contentious years of the "
            "Adams and Jackson administrations.\n\n"
            "His congressional service (1827–1833) "
            "coincided with the transition from the "
            "Era of Good Feelings to the two-party "
            "Jacksonian system — a political realignment "
            "in which the old Democratic-Republican "
            "coalition fractured into the Jacksonian "
            "Democrats and the Adams-Clay National Republicans. "
            "Wilson navigated this transition as a "
            "supporter of Jackson's states'-rights "
            "populism.\n\n"
            "His son, also Ephraim King Wilson, later "
            "served as a U.S. Senator from Maryland, "
            "extending the family's political presence "
            "in Maryland public life into the post-Civil "
            "War era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Maryland Democratic-Republican Congressman (1827–1833) representing the Eastern Shore's planter culture; navigated the transition from the Era of Good Feelings to Jacksonian party politics; patriarch of the Wilson political family whose son became a U.S. Senator.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maryland's Eastern Shore planter culture — rooted in tobacco agriculture, slave labor, and Chesapeake gentry traditions — shaped Wilson's political identity as a states'-rights conservative Democratic-Republican who represented the agricultural interests of his coastal constituency",
            "The collapse of the Era of Good Feelings and the fracturing of the Democratic-Republican Party in the 1824 presidential election — which split into Adams and Jackson factions — defined the political realignment through which Wilson had to navigate as he chose to align with Jacksonian populism over Adams nationalism",
            "The congressional politics of the late 1820s — with debates over the tariff, federal internal improvements, and states' rights — provided the policy substance through which Wilson's votes expressed Maryland Eastern Shore's conservative agrarian priorities"
        ],
        "effects": [
            "His congressional service contributed to the Jacksonian Democratic coalition in Maryland, helping consolidate the partisan alignment between Eastern Shore agricultural interests and Jackson's states'-rights populism that shaped Maryland politics through the antebellum era",
            "His political career helped maintain the Eastern Shore gentry's political representation in Congress — ensuring that the region's distinctive conservative agrarian interests were heard in federal legislative debates over tariffs, internal improvements, and slavery",
            "The Wilson political dynasty he founded — his son Ephraim King Wilson Jr. later became a U.S. Senator — demonstrated the multi-generational political engagement of Maryland's Eastern Shore legal-planter class",
            "His career illustrated the political sociology of the early American republic's transitional period — when the first generation of Jeffersonian politicians had to adapt to or resist the new mass-democratic Jacksonian political style"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Congressman 1827–1833"},
            {"target": "maryland", "verb": "REPRESENTS", "note": "Eastern Shore Maryland constituency"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian Democrat transitioning to Jacksonian Democrat"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Aligned with Jacksonian states'-rights populism"},
            {"target": "ephraim-king-wilson-jr", "verb": "PARENT_OF", "note": "Father of U.S. Senator Ephraim King Wilson Jr."}
        ]
    }),

    # 4 — James Armstrong
    ("james-armstrong", {
        "summary": (
            "James Armstrong (1748–1828) was an American "
            "physician, Revolutionary War officer, and "
            "Pennsylvania politician who served in the "
            "U.S. House of Representatives (1793–1795) "
            "and was a leading figure in Carlisle, "
            "Pennsylvania's civic life from the "
            "Revolutionary era through the early republic. "
            "His combined career as a doctor, soldier, "
            "and legislator exemplified the multi-role "
            "civic leadership expected of educated "
            "men in early American frontier communities.\n\n"
            "Armstrong served as a military surgeon during "
            "the Revolutionary War — one of the many "
            "physicians who combined medical service "
            "with military duty in the Continental Army. "
            "After the war he settled in Carlisle, "
            "Pennsylvania, where he practiced medicine "
            "and became involved in the civic institutions "
            "of a growing frontier town that had been "
            "established as the county seat of Cumberland "
            "County and the site of Dickinson College.\n\n"
            "His congressional service in the Third "
            "Congress (1793–1795) placed him in "
            "Washington during the Washington administration's "
            "second term — a period of intense debate "
            "over the Jay Treaty, the Whiskey Rebellion, "
            "and the emerging partisan divisions between "
            "Federalists and Democratic-Republicans. "
            "Armstrong was a Democratic-Republican who "
            "reflected the western Pennsylvania tradition "
            "of suspicion toward eastern financial "
            "interests and British commercial policy.\n\n"
            "His medical practice in Carlisle made him "
            "one of the early republic's frontier physician-citizens."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "American physician, Revolutionary War surgeon, and Pennsylvania Democratic-Republican Congressman (1793–1795); civic leader in Carlisle, Pennsylvania during the early republic; representative figure of the physician-citizen who combined medical practice with military service and legislative office in frontier American communities.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Revolutionary War's need for military surgeons — who combined medical training with military service to care for Continental Army soldiers — placed Armstrong in the role of physician-officer, establishing both his professional reputation and his patriot credentials that enabled his subsequent political career",
            "Pennsylvania's western frontier civic culture — in which small-town professional men like physicians, lawyers, and clergymen were expected to take on multiple roles as civic leaders, military officers, and legislators — shaped Armstrong's multi-role career in Carlisle",
            "The early republic's Democratic-Republican political tradition — with its western Pennsylvania base of farmers and frontiersmen suspicious of Federalist banking, British trade, and eastern aristocratic influence — provided the partisan environment in which Armstrong's congressional career operated"
        ],
        "effects": [
            "His congressional service contributed the Democratic-Republican perspective from western Pennsylvania to the Third Congress's debates over the Jay Treaty and domestic policy — representing the agricultural and frontier interests of Cumberland County in the constitutional machinery of the new republic",
            "His medical practice in Carlisle contributed to the healthcare infrastructure of a growing Pennsylvania frontier community — providing professional medical care to a region where trained physicians were scarce and the population was expanding rapidly through immigration",
            "His career as a physician-Revolutionary War surgeon-congressman exemplified the civic versatility that the early republic required of its educated men — demonstrating how professional expertise in medicine could translate naturally into military and political leadership",
            "His service in the Continental Army helped build the veteran community that shaped the civic culture of post-Revolutionary Pennsylvania — as veterans like Armstrong carried their wartime networks and democratic commitments into the political institutions of the new state"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman in Third Congress 1793–1795"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Military surgeon during the Revolutionary War"},
            {"target": "carlisle-pennsylvania", "verb": "PRACTICES_IN", "note": "Physician and civic leader in Carlisle"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Western Pennsylvania Democratic-Republican"},
            {"target": "american-revolutionary-war", "verb": "SERVES_IN", "note": "Continental Army physician during the war"}
        ]
    }),

    # 5 — Barthélemy Faujas de Saint-Fond
    ("barthélemy-faujas-de-saint-fond", {
        "summary": (
            "Barthélemy Faujas de Saint-Fond (1741–1819) "
            "was a French geologist, volcanologist, and "
            "naturalist who made significant contributions "
            "to the early development of geology as a "
            "science — particularly through his studies "
            "of volcanic phenomena, basaltic geology, "
            "and the stratigraphy of the Paris Basin. "
            "A professor of geology at the Muséum "
            "national d'Histoire naturelle, he was among "
            "the founders of systematic geological "
            "inquiry in France.\n\n"
            "Born in Montélimar (Drôme), Faujas de Saint-Fond "
            "was drawn to natural history through his "
            "study of the volcanic landscapes of the "
            "Vivarais — the ancient volcanic region of "
            "southern France whose extinct volcanoes "
            "he documented in his Recherches sur les "
            "volcans éteints du Vivarais et du Velay (1778). "
            "This work placed him at the center of the "
            "great eighteenth-century debate between "
            "Neptunists (who believed basalt was a "
            "sedimentary deposit) and Vulcanists (who "
            "correctly argued it was volcanic in origin) "
            "— Faujas was a pioneering Vulcanist.\n\n"
            "He also traveled to Scotland and England, "
            "visiting the volcanic basalt columns of "
            "Fingal's Cave and the Giant's Causeway, "
            "which he described in his Voyage en Angleterre, "
            "en Écosse et aux îles Hébrides (1797). "
            "He witnessed and described the first "
            "hydrogen balloon flight in Paris (1783).\n\n"
            "His professorship at the Muséum d'Histoire "
            "naturelle made him a founding figure of "
            "French academic geology."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French geologist and volcanologist who pioneered Vulcanist interpretation of basalt's volcanic origin; studied extinct volcanoes of the Vivarais; professor of geology at the Muséum national d'Histoire naturelle; visited and described Fingal's Cave and the Giant's Causeway; witnessed the first hydrogen balloon flight (1783).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The great eighteenth-century geological debate between Neptunists (Abraham Gottlob Werner's school holding that all rocks including basalt were sedimentary water deposits) and Vulcanists (who argued basalt was volcanic) — created the intellectual context in which Faujas's study of French extinct volcanoes and basalt formations became a significant contribution to the Vulcanist position",
            "The Enlightenment's transformation of natural history from collecting curiosities to systematic scientific investigation — applied to the geological features of France's landscapes — provided the intellectual framework within which Faujas pursued his volcanic studies in Vivarais and his wider geological travels",
            "The establishment of the Muséum national d'Histoire naturelle (1793) — which replaced the old Jardin du Roi as France's premier natural history institution — created the academic platform from which Faujas taught and published as one of France's first professors of geology"
        ],
        "effects": [
            "His Vulcanist studies of the Vivarais extinct volcanoes contributed evidence that basalt was volcanic in origin — an argument that ultimately triumphed over Neptunism and became one of the foundational principles of igneous petrology and modern geology",
            "His Voyage en Angleterre descriptions of Fingal's Cave and the Giant's Causeway helped popularize these extraordinary basalt formations across educated European audiences, contributing to both geological science and the Romantic appreciation of natural sublime landscapes",
            "His professorship at the Muséum d'Histoire naturelle established geology as an academic discipline in French higher education — training a generation of French geologists and contributing to the institutionalization of geological science",
            "His eyewitness account of the first hydrogen balloon flight in Paris (1783) contributed to the historical record of one of the eighteenth century's most dramatic technological achievements"
        ],
        "relationships": [
            {"target": "museum-national-dhistoire-naturelle", "verb": "TEACHES_AT", "note": "Professor of geology at France's premier natural history institution"},
            {"target": "vulcanism-vs-neptunism-debate", "verb": "PARTICIPATES_IN", "note": "Pioneer Vulcanist studying French extinct volcanoes"},
            {"target": "french-geology", "verb": "FOUNDS", "note": "Early systematic geological study of French volcanic landscapes"},
            {"target": "fingals-cave", "verb": "DOCUMENTS", "note": "Described basalt formations in Voyage en Angleterre"},
            {"target": "montgolfier-balloon-1783", "verb": "WITNESSES", "note": "Eyewitness to first hydrogen balloon flight in Paris"}
        ]
    }),

    # 6 — John Murphy
    ("john-murphy", {
        "summary": (
            "John Murphy (1786–1841) was an Irish-born "
            "American politician who served as Governor "
            "of Alabama (1825–1829) during the formative "
            "period of Alabama statehood, following the "
            "state's admission to the Union in 1819. "
            "A Democratic-Republican and later Jacksonian "
            "Democrat, Murphy's governorship coincided "
            "with Alabama's rapid transformation from "
            "frontier territory to an established "
            "cotton-producing slave state — a transformation "
            "driven by the forced removal of Native "
            "American populations and the rapid "
            "expansion of plantation agriculture.\n\n"
            "Born in Waxhaw, South Carolina (near "
            "Andrew Jackson's birthplace), Murphy moved "
            "to Alabama and built a legal and political "
            "career in the new state. He served in "
            "the Alabama Territorial Legislature and "
            "the early state legislature before winning "
            "the governorship. His political associations "
            "with Andrew Jackson were natural given "
            "their shared South Carolina roots and "
            "frontier Democratic sensibilities.\n\n"
            "As governor, Murphy oversaw Alabama during "
            "a period of intense Creek and Cherokee "
            "presence in the state — the Creek "
            "Nation controlled large portions of Alabama "
            "until the forced removal policies of "
            "the 1830s cleared the land for cotton "
            "cultivation. His administration operated "
            "within the framework of expanding "
            "plantation agriculture and the racial "
            "hierarchy it required.\n\n"
            "He also served in the U.S. House of "
            "Representatives (1833–1835), extending "
            "his political career at the federal level."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Alabama (1825–1829) during the formative period of Alabama statehood; Irish-born Jacksonian Democrat who governed during Alabama's rapid transformation from frontier territory to cotton-producing slave state; later U.S. Congressman; associated with Andrew Jackson's political circle.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Alabama's admission to the Union in 1819 — as the rapid settlement of the Old Southwest created new states from territories acquired from Native American nations — established the governmental framework within which Murphy's political career could flourish as a founding-era Alabama politician",
            "The Jacksonian Democratic political culture of the Old Southwest — with its frontier populism, hostility to Native American land tenure, enthusiasm for slave-based plantation agriculture, and alignment with Andrew Jackson's political movement — shaped Murphy's political identity and electoral success",
            "The rapid transformation of Alabama from Cherokee and Creek territory into cotton plantation land — driven by federal land sales, speculator activity, and forced removal policies — created the economic boom that populated the state with settlers whose political interests Murphy's governorship served"
        ],
        "effects": [
            "His governorship helped consolidate Alabama's governmental institutions during the critical early years of statehood — building administrative capacity, establishing state courts and legislative procedures, and managing the political integration of a rapidly growing immigrant population",
            "His administration governed during the period when Alabama's plantation-slave economy was establishing itself as the dominant social and economic system — contributing to the political framework that protected and extended that system",
            "His congressional service (1833–1835) extended Alabama's representation in federal policy debates over tariffs, Indian removal, and the national bank — issues on which Murphy's Jacksonian positions aligned with the dominant Southern Democratic consensus",
            "His career as an Irish immigrant who rose to the Alabama governorship illustrated the social mobility available in the early American Southwest to white settlers regardless of immigrant origin"
        ],
        "relationships": [
            {"target": "alabama", "verb": "GOVERNS", "note": "Governor of Alabama 1825–1829"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Alabama Congressman 1833–1835"},
            {"target": "andrew-jackson", "verb": "ALLIED_WITH", "note": "Jacksonian Democrat aligned with Jackson's political movement"},
            {"target": "creek-nation", "verb": "GOVERNS_DURING_REMOVAL_OF", "note": "Governor during period of Creek presence and displacement in Alabama"},
            {"target": "alabama-cotton-economy", "verb": "SUPPORTS", "note": "Governorship served the expanding plantation agriculture system"}
        ]
    }),

    # 7 — Marcus Gjøe Rosenkrantz
    ("marcus-gjøe-rosenkrantz", {
        "summary": (
            "Marcus Gjøe Rosenkrantz (1762–1838) was a "
            "Norwegian noble, lawyer, and public official "
            "who served as a member of the Norwegian "
            "Constituent Assembly at Eidsvoll in 1814 — "
            "the founding constitutional convention that "
            "drafted the Norwegian Constitution of 17 May "
            "1814, one of the most liberal constitutions "
            "in the world at that time. His participation "
            "in the Eidsvoll Assembly placed him among "
            "the 112 men who created Norway's foundational "
            "constitutional document.\n\n"
            "Rosenkrantz came from one of the Danish-Norwegian "
            "nobility's most distinguished families — the "
            "Rosenkrantz name had deep roots in Scandinavian "
            "aristocratic history (inspiring the fictional "
            "character Rosencrantz in Shakespeare's Hamlet). "
            "His legal training and official service in "
            "the Norwegian provincial administration made "
            "him a natural participant in the constitutional "
            "assembly that the Norwegian patriot movement "
            "convened after Denmark's cession of Norway "
            "to Sweden in the Treaty of Kiel (January 1814).\n\n"
            "The Eidsvoll Assembly met from April to May "
            "1814 and produced a constitution inspired "
            "by American (1787) and French (1791) "
            "constitutional models — establishing "
            "a constitutional monarchy with a "
            "sovereign parliament (Storting), "
            "popular representation, and civil liberties "
            "that were genuinely advanced for the era.\n\n"
            "His noble family background made him "
            "representative of the Norwegian nobility's "
            "participation in a constitutional revolution "
            "that actually limited aristocratic privilege."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norwegian noble and member of the Eidsvoll Constituent Assembly (1814) that drafted the Norwegian Constitution — one of the most liberal constitutions of the nineteenth century; from the distinguished Rosenkrantz noble family; representative of the Norwegian aristocracy's participation in Norway's constitutional revolution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Treaty of Kiel (January 1814) — in which Denmark ceded Norway to Sweden following Denmark's defeat in the Napoleonic Wars — created the political crisis that triggered Norway's constitutional revolution, as Norwegian patriots refused the transfer and convened the Eidsvoll Assembly to establish an independent constitutional government",
            "The Norwegian patriot movement's need for educated legal and administrative figures to draft a sophisticated constitutional document — one that could draw on American, French, and existing constitutional models — made legally trained officials like Rosenkrantz essential participants in the Eidsvoll Assembly",
            "The global constitutional moment of the 1810s — in which the American Constitution of 1787 and the French constitutional experiments of 1791–1795 had demonstrated that sovereign peoples could create written constitutional charters — provided the intellectual models from which the Eidsvoll Assembly drew its constitutional provisions"
        ],
        "effects": [
            "His participation in the Eidsvoll Assembly contributed to the drafting of the Norwegian Constitution of 17 May 1814 — a document that established constitutional monarchy, parliamentary sovereignty, civil liberties, and popular representation in Norway and endured as Norway's fundamental law",
            "The Norwegian Constitution that he helped create became a model for liberal constitutionalism in Europe, inspiring constitutional movements in Sweden, Germany, and elsewhere as a working example of popular sovereignty and limited government",
            "His presence as a noble at the Eidsvoll Assembly represented the Norwegian aristocracy's acceptance of constitutional limitations on noble privilege — a significant concession that helped give the new constitutional order broad social legitimacy",
            "The Constitution of 17 May 1814 that the Eidsvoll Assembly produced became Norway's National Day — celebrated annually on 17 May as Norway's most important national holiday — making the Assembly's participants permanent historical figures"
        ],
        "relationships": [
            {"target": "norwegian-constitution-1814", "verb": "DRAFTS", "note": "Member of the Eidsvoll Constituent Assembly"},
            {"target": "eidsvoll-assembly-1814", "verb": "PARTICIPATES_IN", "note": "One of 112 delegates to the constitutional convention"},
            {"target": "rosenkrantz-family", "verb": "MEMBER_OF", "note": "From the distinguished Danish-Norwegian noble family"},
            {"target": "treaty-of-kiel-1814", "verb": "RESPONDS_TO", "note": "Constitutional assembly convened after Danish cession of Norway"},
            {"target": "norway", "verb": "SERVES", "note": "Norwegian official and constitutional founder"}
        ]
    }),

    # 8 — Vasile Aaron
    ("vasile-aaron", {
        "summary": (
            "Vasile Aaron (1770–1822) was a Romanian "
            "lawyer, poet, and intellectual from "
            "Transylvania who contributed to the "
            "Romanian national awakening (Şcoala Ardeleană — "
            "the Transylvanian School) through his "
            "literary and legal work. Writing during "
            "the period of Habsburg rule over Transylvania, "
            "Aaron combined legal practice with "
            "Romanian-language poetry and prose that "
            "affirmed the historical identity and "
            "linguistic dignity of the Romanian-speaking "
            "population of the region.\n\n"
            "Transylvania's Romanians — who constituted "
            "the largest ethnic group in the province "
            "but lacked equal political status with "
            "Hungarians, Saxons, and Szeklers under "
            "the established nations (nationes) system "
            "— developed in the late eighteenth century "
            "the Şcoala Ardeleană (Transylvanian School), "
            "an intellectual movement that used "
            "historical, linguistic, and literary "
            "arguments to assert Romanian identity "
            "and claim equal rights. Aaron participated "
            "in this movement through his writings.\n\n"
            "His legal career was conducted within "
            "the Habsburg administrative system, where "
            "Romanian professionals of his generation "
            "operated in a political environment that "
            "did not recognize Romanians as a distinct "
            "political nation. His poetry — written in "
            "Romanian and celebrating Romanian history "
            "and folk traditions — was an assertion "
            "of cultural dignity against this political "
            "marginalization.\n\n"
            "He represents the generation of Transylvanian "
            "Romanian intellectuals who laid the cultural "
            "foundations for the eventual unification "
            "of all Romanian lands in 1918."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Transylvanian Romanian lawyer, poet, and intellectual associated with the Şcoala Ardeleană (Transylvanian School) — the Romanian national awakening movement; combined legal practice with Romanian-language literary work that affirmed Romanian cultural identity under Habsburg rule; contributed to the intellectual foundations of Romanian nationalism.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Habsburg rule over Transylvania — which classified Romanians as a tolerated population outside the formal political 'nationes' of Hungarians, Saxons, and Szeklers — created the political marginalization that drove Romanian intellectuals of Aaron's generation to develop the Şcoala Ardeleană's cultural and historical arguments for Romanian identity and rights",
            "The Enlightenment's influence on Transylvanian Romanian intellectuals — who encountered its ideas about natural rights, national identity, and linguistic pride through contact with Western European thought — provided the intellectual framework within which Aaron and the Şcoala Ardeleană developed their arguments for Romanian cultural dignity",
            "The growth of Romanian-language literacy and printing in the late eighteenth century — as Uniate (Greek Catholic) and Orthodox Church schools educated Romanian professionals — created the audience for Aaron's Romanian-language poetry and the Şcoala Ardeleană's cultural-historical publications"
        ],
        "effects": [
            "His Romanian-language poetry contributed to the cultural self-assertion of the Transylvanian Romanian community — affirming the richness of Romanian linguistic tradition and folk culture at a time when Romanian was denied official recognition in Transylvanian public life",
            "His participation in the Şcoala Ardeleană movement helped build the intellectual foundations for Romanian national identity — arguments about Romanian historical continuity from the Dacian-Roman past, linguistic unity, and cultural distinctiveness — that sustained Romanian nationalism through the nineteenth century",
            "His combined legal and literary career modeled the possibility of a Romanian professional class that could operate within Habsburg administrative structures while maintaining and asserting its Romanian cultural identity — a model for subsequent generations",
            "His generation's Transylvanian School movement ultimately contributed to the political and cultural forces that led to the unification of Transylvania with Romania in 1918 — though this outcome lay a century beyond Aaron's own lifetime"
        ],
        "relationships": [
            {"target": "scoala-ardeleana", "verb": "PARTICIPATES_IN", "note": "Romanian Transylvanian School national awakening movement"},
            {"target": "transylvania", "verb": "BORN_IN", "note": "Romanian intellectual active in Habsburg Transylvania"},
            {"target": "romanian-language-literature", "verb": "CONTRIBUTES_TO", "note": "Romanian-language poetry asserting Romanian cultural identity"},
            {"target": "habsburg-empire", "verb": "LIVES_UNDER", "note": "Romanian professional operating within Habsburg administrative system"},
            {"target": "romanian-national-awakening", "verb": "ADVANCES", "note": "Intellectual contributor to Romanian national identity movement"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 53 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
