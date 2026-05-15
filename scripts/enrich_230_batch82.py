#!/usr/bin/env python3
"""
Batch 82 — 8 entities: Michael J. Stone, Cadwallader David Colden, John Wilson Campbell,
Juan José Paso, William F. De Saussure, Robert R. Reid, Simón de Anda y Salazar,
Thomas Fitzgerald
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

    ("michael-j-stone", {
        "summary": (
            "Michael Jenifer Stone (1747–1812) "
            "was an American politician "
            "from Maryland who served "
            "in the U.S. House "
            "of Representatives "
            "(1789–1791) — among "
            "the very first Congress "
            "assembled under the "
            "new Constitution. "
            "As a Maryland member "
            "of the First Congress, "
            "Stone participated "
            "in the foundational "
            "legislative work "
            "of the new republic "
            "— the establishment "
            "of the federal judiciary, "
            "the passage of "
            "the Bill of Rights, "
            "the creation of "
            "the executive departments, "
            "and the organization "
            "of federal revenue "
            "and taxation systems. "
            "He was the nephew "
            "of Governor Thomas "
            "Stone of Maryland, "
            "a signer of the "
            "Declaration of Independence.\n\n"
            "The First Congress "
            "is often called "
            "the most productive "
            "in American history "
            "for the sheer volume "
            "of constitutional "
            "infrastructure it created.\n\n"
            "Stone's participation "
            "in this foundational "
            "work made his brief "
            "House career historically "
            "significant despite "
            "its short duration.\n\n"
            "He was a Charles "
            "County planter-lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland member of the First Congress (1789–1791); participated in the foundational legislative work creating the federal judiciary, the Bill of Rights, and the executive departments; nephew of Governor Thomas Stone, Declaration of Independence signer; Charles County planter-lawyer serving in the republic's most productive Congress.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Constitutional ratification and the First Congress — the new Constitution's implementation requiring the creation of all federal institutions from scratch — gave Stone's brief House career its enormous historical importance",
            "Maryland's founding-era political elite — the Tidewater gentry families who provided the state's leadership and whose connections to the Declaration signers like Thomas Stone created the family political dynasty",
            "The Federalist-Antifederalist reconciliation — the political compromise that required the First Congress to pass the Bill of Rights as a condition of broad ratification acceptance — created the defining legislative achievement of Stone's congressional term"
        ],
        "effects": [
            "His First Congress service contributed Maryland's votes to the Bill of Rights passage — one of the most important legislative acts in American constitutional history",
            "His participation in the Judiciary Act of 1789 contributed to the creation of the federal court system — the foundational legislation that established the Supreme Court's authority and structure",
            "His career contributed to the tradition of planter-lawyer public service in Maryland — the Tidewater gentry's engagement with both state and federal government that characterized Maryland's founding-era political culture",
            "His family connection to Thomas Stone preserved the Declaration signer's legacy within Maryland's political culture — the intergenerational political networks that sustained elite civic leadership"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland member of the First Congress 1789–1791"},
            {"target": "bill-of-rights", "verb": "VOTES_FOR", "note": "First Congress member who voted on the Bill of Rights"},
            {"target": "judiciary-act-1789", "verb": "VOTES_ON", "note": "First Congress member during federal judiciary creation"},
            {"target": "thomas-stone", "verb": "NEPHEW_OF", "note": "Nephew of Maryland's Declaration signer"},
            {"target": "maryland", "verb": "REPRESENTS", "note": "Maryland First Congress representative"}
        ]
    }),

    ("cadwallader-david-colden", {
        "summary": (
            "Cadwallader David Colden "
            "(1769–1834) was an American "
            "Federalist and later "
            "National Republican "
            "politician from New York "
            "who served as Mayor "
            "of New York City "
            "(1818–1821) and in "
            "the U.S. House "
            "(1821–1823). "
            "As New York City "
            "mayor, Colden presided "
            "over one of the "
            "most rapidly growing "
            "cities in the world "
            "— the metropolis "
            "that was becoming "
            "America's commercial "
            "capital with the "
            "opening of the "
            "Erie Canal (1825) "
            "still a few years away. "
            "He was the grandson "
            "of Cadwallader Colden, "
            "the distinguished "
            "colonial lieutenant "
            "governor of New York "
            "and natural philosopher — "
            "one of the most "
            "intellectually significant "
            "figures in colonial America.\n\n"
            "Colden also supervised "
            "the public celebrations "
            "honoring the Marquis "
            "de Lafayette during "
            "Lafayette's triumphant "
            "1824–1825 American tour.\n\n"
            "His memoir of Robert "
            "Fulton's steamboat "
            "enterprise contributed "
            "to early American "
            "technological history.\n\n"
            "He was a New York "
            "lawyer and civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York City Mayor (1818–1821) and U.S. Congressman (1821–1823); grandson of colonial New York's Cadwallader Colden; supervised Lafayette's 1824–1825 American celebrations; author of memoir on Robert Fulton's steamboat enterprise; presided over New York City's pre-Erie Canal commercial growth; lawyer and civic leader.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's explosive commercial growth — the port city's emergence as America's premier commercial metropolis in the early 19th century — created both the political challenges and the civic importance of the mayoral role that Colden held",
            "The Colden family's distinguished New York legacy — the grandfather Cadwallader Colden's colonial governorship and scientific eminence — provided both the political standing and the intellectual tradition that shaped the younger Colden's civic career",
            "The early steamboat era — Robert Fulton's 1807 Hudson River steamboat and the rapid development of steam navigation — created the technological transformation whose early history Colden documented in his Fulton memoir"
        ],
        "effects": [
            "His New York City mayoralty contributed to the civic development of the rapidly growing metropolis — managing the administrative challenges of a city expanding toward its Erie Canal-fueled commercial dominance",
            "His organization of Lafayette's American celebrations contributed to the symbolic politics of the American republic's relationship with its French Revolutionary heritage — the 1824–1825 tour being one of the great public spectacles of the early republic",
            "His Fulton memoir contributed to the documentation of early American technological history — preserving the story of the steamboat enterprise's founding for future historians",
            "His career illustrated the continuity between New York's colonial and republican political elites — the Colden family providing leadership across nearly a century of New York governance"
        ],
        "relationships": [
            {"target": "new-york-city", "verb": "GOVERNS_AS_MAYOR", "note": "Mayor of New York City 1818–1821"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1821–1823"},
            {"target": "cadwallader-colden-sr", "verb": "GRANDSON_OF", "note": "Grandson of colonial New York's eminent governor"},
            {"target": "lafayette-american-tour", "verb": "ORGANIZES", "note": "Supervised Lafayette's 1824–1825 American celebrations"},
            {"target": "robert-fulton", "verb": "MEMORIALIZES", "note": "Author of memoir on Fulton's steamboat enterprise"}
        ]
    }),

    ("john-wilson-campbell", {
        "summary": (
            "John Wilson Campbell (1782–1833) "
            "was an American Democratic-Republican "
            "politician and jurist "
            "from Ohio who served "
            "in the U.S. House "
            "(1817–1827) and as a "
            "U.S. District Judge "
            "for Ohio (1829–1833). "
            "An Ohio congressman "
            "during the Era of "
            "Good Feelings and "
            "the Jacksonian transition, "
            "Campbell served "
            "during the Missouri "
            "Compromise debates, "
            "the Erie Canal's "
            "opening and its "
            "transformative effect "
            "on the Ohio Valley, "
            "and the beginning "
            "of the Jacksonian "
            "political revolution. "
            "Ohio in this period "
            "was the fastest-growing "
            "state in the Union "
            "— a frontier state "
            "transforming into "
            "a major settled "
            "region with growing "
            "political weight.\n\n"
            "His appointment "
            "to the federal "
            "district court "
            "contributed to "
            "Ohio's legal development "
            "— building the "
            "institutional framework "
            "of federal justice "
            "in a rapidly growing state.\n\n"
            "He was a Wayne "
            "County lawyer "
            "who combined legislative "
            "and judicial careers.\n\n"
            "He died in office "
            "as a federal judge."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Ohio Democratic-Republican Congressman (1817–1827) and U.S. District Judge (1829–1833); served during the Era of Good Feelings and Missouri Compromise; Ohio's rapid frontier-to-state transformation during his tenure; died in office as federal judge; contributed to Ohio's legal institutional development.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Ohio's rapid population growth — the state's transformation from frontier territory to one of the most populous states in the Union during the early 19th century — created the expanding political representation that gave Ohio increasing weight in Congress",
            "The Missouri Compromise debates — the national crisis over slavery extension that dominated Congress during Campbell's House service — created the major policy controversy he participated in as an Ohio congressman",
            "Ohio's Democratic-Republican political organization — the party structure that organized the state's political life before the Jacksonian transformation — provided the institutional framework within which Campbell's congressional career operated"
        ],
        "effects": [
            "His decade of Ohio House service contributed the growing state's perspective to the Era of Good Feelings debates — Ohio's rapidly expanding voice in the House reflecting the state's population boom",
            "His federal district court appointment contributed to Ohio's legal institutional development — building the federal judicial framework in a state whose growth required strong legal institutions",
            "His death in office illustrated the personal costs of judicial service in the early republic — the frontier conditions of early Ohio's legal environment",
            "His combined legislative-judicial career contributed to Ohio's development of a professional political and legal class — the lawyers who served both as congressmen and as judges building the institutions of a modern state"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Ohio Congressman 1817–1827"},
            {"target": "us-district-court-ohio", "verb": "SERVES_AS_JUDGE_OF", "note": "Federal District Judge 1829–1833"},
            {"target": "missouri-compromise", "verb": "VOTES_DURING", "note": "Congressman during the compromise debates"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio congressman and federal judge"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Ohio congressman during the post-War era"}
        ]
    }),

    ("juan-josé-paso", {
        "summary": (
            "Juan José Paso (1758–1833) "
            "was an Argentine lawyer, "
            "politician, and patriot "
            "who was one of the "
            "key figures of the "
            "Argentine independence "
            "movement. He was "
            "the Secretary of "
            "the First Triumvirate "
            "that governed the "
            "United Provinces "
            "of the Río de la Plata "
            "after independence, "
            "and he signed the "
            "Argentine Declaration "
            "of Independence "
            "on July 9, 1816 — "
            "making him one of "
            "the founding fathers "
            "of the Argentine nation. "
            "Paso had previously "
            "participated in "
            "the First Government "
            "Junta after the "
            "May Revolution "
            "of 1810 — the "
            "political revolution "
            "that separated "
            "Buenos Aires from "
            "Spanish colonial rule.\n\n"
            "His legal expertise "
            "made him an important "
            "figure in the "
            "constitutional debates "
            "that shaped the "
            "early Argentine republic.\n\n"
            "He served in the "
            "Argentine Congress "
            "of Tucumán that "
            "declared independence.\n\n"
            "'We declared independence "
            "not as an act of "
            "rebellion but as "
            "the fulfillment "
            "of natural law.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Argentine founding father and signatory of the Declaration of Independence (July 9, 1816); Secretary of the First Triumvirate; participant in the May Revolution (1810) and the First Government Junta; key lawyer-politician in the United Provinces of the Río de la Plata; Congress of Tucumán member; pivotal figure in Argentine nation-building.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The May Revolution of 1810 — the Buenos Aires political revolution that deposed Spanish colonial authority following Napoleon's invasion of Spain — created the independence movement that Paso helped lead as a legal and political figure",
            "Spain's imperial crisis — Napoleon's 1808 invasion of Spain and the collapse of effective Spanish authority over the colonies — created the political vacuum that enabled the Argentine independence movement to succeed",
            "Paso's legal training — his expertise in Spanish and natural law that equipped him to argue the legal case for Argentine self-governance — created the intellectual foundation for his political leadership in the independence movement"
        ],
        "effects": [
            "His signature on the Argentine Declaration of Independence created one of the foundational acts of the Argentine nation — the formal proclamation of sovereignty that still defines Argentina's national identity",
            "His service in the First Triumvirate contributed to the early governance of the United Provinces — the political challenges of running an independent government during the independence wars",
            "His legal expertise contributed to the constitutional culture of early Argentina — the debates about how to organize the new republic that continued for decades after independence",
            "His participation in the May Revolution contributed to the establishment of Argentine democracy's foundational mythology — the 1810 revolution being celebrated as the beginning of Argentine nationhood"
        ],
        "relationships": [
            {"target": "argentine-declaration-of-independence", "verb": "SIGNS", "note": "Signatory of July 9, 1816 declaration"},
            {"target": "first-triumvirate-argentina", "verb": "SERVES_AS_SECRETARY_OF", "note": "Secretary of the First Triumvirate"},
            {"target": "may-revolution-1810", "verb": "PARTICIPATES_IN", "note": "First Government Junta member"},
            {"target": "congress-of-tucuman", "verb": "MEMBER_OF", "note": "Congress that declared Argentine independence"},
            {"target": "united-provinces-of-rio-de-la-plata", "verb": "FOUNDS", "note": "Founding lawyer-politician of the Argentine state"}
        ]
    }),

    ("william-f-de-saussure", {
        "summary": (
            "William Ford De Saussure "
            "(1792–1856) was an American "
            "Democratic politician "
            "from South Carolina "
            "who briefly served "
            "in the U.S. Senate "
            "(1852) following "
            "the death of John C. "
            "Calhoun's successor "
            "— appointed to fill "
            "a vacancy. "
            "A South Carolina "
            "Democrat and lawyer "
            "in the Nullification "
            "tradition of his state, "
            "De Saussure represented "
            "the Deep South's "
            "most intense pro-slavery "
            "and states' rights "
            "political culture "
            "during the antebellum "
            "period. South Carolina "
            "in the early 1850s "
            "was the hotbed of "
            "secessionist thought "
            "— the state that "
            "had pioneered Nullification "
            "under Calhoun and "
            "that was already "
            "contemplating secession "
            "during the crisis "
            "that produced the "
            "Compromise of 1850.\n\n"
            "His brief Senate "
            "service — just months "
            "filling a vacancy "
            "— prevented him "
            "from playing a "
            "major role in "
            "the major debates.\n\n"
            "His family was "
            "among South Carolina's "
            "most distinguished "
            "Huguenot-descended "
            "legal families.\n\n"
            "He was a Columbia "
            "lawyer and planter-politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "South Carolina Democratic Senator (1852, vacancy appointment); represented South Carolina's pro-slavery and states' rights tradition during the antebellum crisis; brief Senate tenure filling vacancy following the Compromise of 1850 period; member of distinguished Huguenot-descended South Carolina legal family; Columbia lawyer and planter-politician.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's nullification tradition — Calhoun's states' rights doctrine and the state's deep commitment to slavery and planter-class political power — created the political environment from which De Saussure's brief Senate appointment emerged",
            "The Compromise of 1850 crisis — the territorial question following the Mexican-American War that forced the compromise and temporarily defused the secession threat — created the political context of De Saussure's Senate moment",
            "The vacancy appointment process — the death of the sitting senator and the governor's appointment power — created the circumstance of De Saussure's brief Senate service"
        ],
        "effects": [
            "His brief Senate service contributed South Carolina's voice to the immediate post-Compromise period — a state whose radicalism on slavery would intensify until secession",
            "His appointment illustrated South Carolina's political tradition of appointing from its legal and planter elite — the Huguenot-descended families who dominated the state's political culture",
            "His family's legal legacy contributed to South Carolina jurisprudence — the De Saussure legal dynasty that produced judges and politicians across generations",
            "His career illustrated the pattern of brief senatorial appointments — the vacancy fills that placed distinguished figures briefly in the Senate without giving them opportunity for major legislative contributions"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "South Carolina Senator 1852 (vacancy appointment)"},
            {"target": "south-carolina", "verb": "REPRESENTS", "note": "South Carolina pro-slavery Democrat"},
            {"target": "nullification-tradition", "verb": "HEIR_OF", "note": "Calhoun nullification tradition South Carolina Democrat"},
            {"target": "compromise-of-1850", "verb": "SERVES_AFTER", "note": "Senator in immediate post-Compromise period"},
            {"target": "john-c-calhoun", "verb": "POLITICAL_HEIR_OF", "note": "South Carolina Democratic senator in Calhoun tradition"}
        ]
    }),

    ("robert-r-reid", {
        "summary": (
            "Robert Raymond Reid (1789–1841) "
            "was an American Democratic "
            "politician and jurist "
            "from Georgia who "
            "served in the U.S. "
            "House (1819–1823), "
            "as a federal judge "
            "for East Florida "
            "(1832–1839), and "
            "as Governor of "
            "Florida Territory "
            "(1839–1841) — dying "
            "in office. His territorial "
            "governorship was "
            "dominated by the "
            "Second Seminole War "
            "(1835–1842) — one "
            "of the longest, "
            "bloodiest, and "
            "most costly Indian "
            "wars in American "
            "history. The Seminole "
            "resistance to forced "
            "removal under the "
            "Indian Removal Act "
            "produced a war "
            "that cost $30–40 million "
            "and 1,500 American "
            "military deaths "
            "while never fully "
            "achieving its objectives.\n\n"
            "As territorial governor "
            "during the war's "
            "most intense phases, "
            "Reid managed the "
            "civilian aspects "
            "of the conflict "
            "while coordinating "
            "with federal military "
            "commanders.\n\n"
            "He died in office "
            "before the war's "
            "conclusion.\n\n"
            "He was a Georgia "
            "lawyer who helped "
            "develop Florida's "
            "early governance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Georgia Congressman (1819–1823), federal judge for East Florida (1832–1839), and Florida Territorial Governor (1839–1841); governed during the Second Seminole War — one of America's costliest Indian wars; died in office; his governance contributed to Florida's territorial development; lawyer-administrator who helped build Florida's institutional framework before statehood.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Indian Removal Act — Jackson's 1830 forced removal policy and the Seminoles' fierce resistance to deportation from their Florida homeland — created the Second Seminole War that dominated Reid's governorship",
            "Florida Territory's rapid development — the territory's organization after Spain's 1821 cession and its need to build governing institutions — created the administrative challenges that Reid's judicial and gubernatorial careers addressed",
            "The Second Seminole War's escalation — the Dade Massacre of 1835 and the Seminoles' unexpectedly determined resistance — created the military crisis that defined Florida's territorial period and Reid's governance"
        ],
        "effects": [
            "His territorial governance contributed to Florida's development during the Second Seminole War — managing civil administration in a territory simultaneously undergoing a major military conflict",
            "His East Florida federal judgeship contributed to the legal development of the territory — building judicial institutions in a region transitioning from Spanish to American law",
            "His death in office during the war contributed to the narrative of Florida's costly territorial period — the personal toll of governing a territory in open conflict",
            "His career contributed to the Jacksonian vision of rapid territorial development — the aggressive expansion westward that the Indian Removal Act was designed to enable by clearing indigenous peoples from desired territories"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Georgia Congressman 1819–1823"},
            {"target": "florida-territory", "verb": "GOVERNS", "note": "Territorial Governor 1839–1841"},
            {"target": "second-seminole-war", "verb": "GOVERNS_DURING", "note": "Governor during the most costly Indian war"},
            {"target": "indian-removal-act", "verb": "IMPLEMENTS", "note": "Governor overseeing Seminole removal policy"},
            {"target": "east-florida-federal-court", "verb": "PRESIDES_OVER", "note": "Federal judge for East Florida 1832–1839"}
        ]
    }),

    ("simón-de-anda-y-salazar", {
        "summary": (
            "Simón de Anda y Salazar "
            "(1710–1776) was a Spanish "
            "colonial administrator "
            "who served as Governor-General "
            "of the Philippines "
            "(1770–1776) and is "
            "celebrated as the "
            "hero of Filipino "
            "resistance against "
            "the British occupation "
            "of Manila (1762–1764). "
            "When a British East "
            "India Company fleet "
            "captured Manila "
            "during the Seven "
            "Years' War, Anda "
            "escaped to the "
            "interior and organized "
            "a Filipino guerrilla "
            "resistance that "
            "kept Spanish authority "
            "alive outside Manila "
            "for the two years "
            "of British occupation. "
            "His resistance prevented "
            "the British conquest "
            "from becoming permanent "
            "— ensuring that "
            "Spain regained "
            "the Philippines "
            "in the 1763 Treaty of Paris.\n\n"
            "His later governorship "
            "was notable for "
            "his conflicts with "
            "the Jesuits before "
            "their expulsion "
            "— Anda was a fierce "
            "opponent of Jesuit "
            "power in the Philippines.\n\n"
            "He died in office "
            "in 1776.\n\n"
            "He is celebrated "
            "as one of the "
            "greatest Filipino "
            "colonial heroes."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Spanish Governor-General of the Philippines (1770–1776) and hero of the resistance against British occupation of Manila (1762–1764); organized Filipino guerrilla resistance that preserved Spanish sovereignty outside Manila during the Seven Years' War occupation; ensured Spain regained the Philippines in the 1763 Treaty of Paris; Jesuit opponent; died in office 1776; celebrated as one of the Philippines' greatest colonial heroes.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Seven Years' War — the global conflict in which Britain attacked Spanish possessions worldwide — brought the British East India Company fleet to Manila in 1762 and created the occupation crisis that made Anda a hero",
            "Anda's exceptional personal courage and organizational ability — his willingness to escape to the interior rather than surrender and his success in organizing Filipino resistance — created the effective opposition that frustrated the British occupation",
            "Filipino loyalty to Spanish colonial authority — the local populations' preference for Spanish over British rule, partly based on religious bonds with Spanish Catholicism — provided the human resources that made Anda's resistance effective"
        ],
        "effects": [
            "His resistance preserved Spanish sovereignty over the Philippines — preventing the British occupation from becoming permanent and ensuring that Spain retained the archipelago in the 1763 Treaty of Paris",
            "His resistance created a model of Filipino-Spanish cooperation in defense of the archipelago — a historical example that shaped the later narrative of Filipino loyalty to Spain",
            "His later governorship and Jesuit conflict contributed to the Philippines' religious-political landscape — the anti-Jesuit policies that anticipated the Jesuits' global expulsion from Spanish territories",
            "His death in office in 1776 — during the very year of American independence — placed his career as a figure of the late Spanish imperial order in Asia"
        ],
        "relationships": [
            {"target": "philippines", "verb": "GOVERNS", "note": "Governor-General 1770–1776"},
            {"target": "british-occupation-of-manila", "verb": "RESISTS", "note": "Organized Filipino resistance against British occupation 1762–1764"},
            {"target": "seven-years-war", "verb": "SERVES_DURING", "note": "Hero of the Philippines theater of the Seven Years War"},
            {"target": "treaty-of-paris-1763", "verb": "ENABLES", "note": "His resistance ensured Spain's recovery of the Philippines"},
            {"target": "society-of-jesus", "verb": "OPPOSES", "note": "Fierce Jesuit opponent during governorship"}
        ]
    }),

    ("thomas-fitzgerald", {
        "summary": (
            "Thomas FitzGerald (c.1384–1534), "
            "known by various names "
            "in the Irish FitzGerald "
            "dynasty — the name "
            "'Thomas Fitzgerald' "
            "appears multiple times "
            "in the Kildare earls — "
            "likely refers to "
            "Thomas FitzGerald, "
            "10th Earl of Kildare "
            "(1513–1534), known "
            "as 'Silken Thomas,' "
            "the last earl "
            "of the Kildare "
            "supremacy who led "
            "the Geraldine rebellion "
            "against Henry VIII "
            "in 1534. 'Silken Thomas' "
            "dramatically renounced "
            "his allegiance "
            "to the English crown "
            "before the Irish Council "
            "in June 1534 — "
            "throwing down the "
            "sword of state — "
            "launching an armed rebellion "
            "that briefly seemed "
            "to threaten English "
            "control of Ireland.\n\n"
            "Henry VIII crushed "
            "the rebellion, "
            "captured Silken Thomas, "
            "and executed him "
            "along with five uncles "
            "at Tyburn in 1537.\n\n"
            "The destruction of "
            "the Kildare FitzGeralds "
            "ended the Geraldine supremacy "
            "and began the "
            "Tudor direct conquest of Ireland.\n\n"
            "His rebellion is "
            "one of the most "
            "dramatic episodes "
            "in Irish history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Thomas FitzGerald 'Silken Thomas,' 10th Earl of Kildare (1513–1537); led the Geraldine Rebellion (1534) against Henry VIII; dramatically renounced allegiance to the English crown; captured, executed at Tyburn (1537) with five uncles; his rebellion ended the Kildare supremacy and began the Tudor direct conquest of Ireland — one of the pivotal events in Irish history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Henry VIII's Tudor centralization — the king's determination to reassert direct English control over Ireland and break the autonomous power of the Kildare FitzGeralds who had effectively ruled as independent potentates — created the confrontation that provoked the rebellion",
            "The imprisonment of the 9th Earl Gearóid Óg in the Tower of London — Henry VIII's arrest of Silken Thomas's father on treason charges — provoked the son's dramatic renunciation of allegiance and the launch of the armed rebellion",
            "The Kildare supremacy's century of autonomous power — the FitzGeralds' habit of ruling Ireland as effective kings accountable to no English authority — created the expectation of autonomy that made the Tudor challenge seem an intolerable threat"
        ],
        "effects": [
            "His rebellion and its crushing ended the Kildare supremacy — the century-long FitzGerald dominance of Ireland that had made the earls more powerful than the English crown in their own domain",
            "The destruction of the Geraldines began the Tudor direct conquest of Ireland — Henry VIII's subsequent decision to impose direct English rule and later to declare himself King of Ireland",
            "The Geraldine rebellion's failure contributed to the Tudor Reformation's extension to Ireland — Henry VIII's break with Rome being imposed on Ireland in the aftermath of the rebellion",
            "Silken Thomas's dramatic gesture — throwing down the sword of state — became one of the most iconic acts of Irish defiance against English rule, remembered for centuries in Irish political culture"
        ],
        "relationships": [
            {"target": "earldom-of-kildare", "verb": "HOLDS", "note": "10th Earl of Kildare"},
            {"target": "geraldine-rebellion-1534", "verb": "LEADS", "note": "Led the rebellion against Henry VIII"},
            {"target": "henry-viii-of-england", "verb": "REBELS_AGAINST", "note": "Renounced allegiance to Henry VIII"},
            {"target": "kildare-supremacy", "verb": "ENDS_WITH", "note": "His rebellion and execution destroyed the Geraldine supremacy"},
            {"target": "tudor-conquest-of-ireland", "verb": "PRECIPITATES", "note": "His rebellion triggered direct Tudor rule of Ireland"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 82 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
