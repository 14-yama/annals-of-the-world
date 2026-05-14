#!/usr/bin/env python3
"""
Batch 67 — 8 entities: Robert Goldsborough, Vũ Trinh, William Giffard,
Étienne de Sauvage, George Dent, Isaac Wilbour, Pedro Nolasco Vergara Albano,
Frederik Motzfeldt
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

    ("robert-goldsborough", {
        "summary": (
            "Robert Goldsborough (1765–1836) "
            "was an American Federalist "
            "politician and lawyer from "
            "Maryland who served as a "
            "U.S. Senator (1813–1819) "
            "during the critical years "
            "of the War of 1812 and "
            "its aftermath. A member "
            "of the prominent Maryland "
            "Goldsborough family — one "
            "of the Eastern Shore's "
            "leading planter dynasties "
            "— he represented the "
            "Federalist tradition of "
            "Maryland's tidewater "
            "gentry class through "
            "the Federalist Party's "
            "final years of significant "
            "political influence.\n\n"
            "His Senate service during "
            "the War of 1812 placed "
            "him in the Federalist "
            "minority that opposed "
            "the war — 'Mr. Madison's War' "
            "as Federalists called it "
            "— viewing it as an "
            "unnecessary and commercially "
            "ruinous conflict driven "
            "by Democratic-Republican "
            "agrarian and expansionist "
            "interests that damaged "
            "the commercial and "
            "maritime interests of "
            "New England and the "
            "Mid-Atlantic states.\n\n"
            "The Federalists' opposition "
            "to the War of 1812 "
            "culminated in the "
            "Hartford Convention "
            "fiasco (1814–1815) "
            "that destroyed the "
            "party's national "
            "credibility.\n\n"
            "He represented Maryland's "
            "conservative planter "
            "Federalism through "
            "the party's extinction."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Federalist Senator (1813–1819); opposed the War of 1812 as a Federalist minority voice; from the prominent Eastern Shore Goldsborough planter family; represented Maryland's tidewater gentry Federalism through the party's final years; served through the Hartford Convention debacle that destroyed Federalist national credibility.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's Eastern Shore planter class's Federalist tradition — the tidewater gentry's commercial and social ties to Britain and their opposition to Jeffersonian agrarianism — created the political constituency for Goldsborough's Federalist Senate career",
            "The War of 1812's political polarization — the Democratic-Republicans' war declaration splitting Congress along party lines, with Federalists seeing the war as a commercial disaster driven by agrarian and expansionist interests — created the political context for Goldsborough's Senate opposition",
            "The Goldsborough family's prominence on Maryland's Eastern Shore — one of the tidewater region's leading planter dynasties with generations of political service — provided the social foundation for Robert's political career"
        ],
        "effects": [
            "His Senate opposition to the War of 1812 contributed the Federalist minority's voice to the war debates — arguing for the commercial and maritime interests that the war damaged and the Federalist foreign policy principles that opposed military conflict with Britain",
            "His career illustrated the survival of Federalist politics in Maryland's tidewater Eastern Shore long after the party had collapsed elsewhere — the persistence of planter-class Federalism in a region with deep commercial ties to Britain",
            "His senatorial service through the Federalist Party's final national significance — through the Hartford Convention's humiliation and the Era of Good Feelings that followed the war — illustrated the party's graceless decline",
            "His career contributed to the Maryland Goldsborough family's multigenerational political tradition — the Eastern Shore dynasty that produced senators and governors through the nineteenth century"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maryland Senator 1813–1819"},
            {"target": "war-of-1812", "verb": "OPPOSES", "note": "Federalist opponent of Mr. Madison's War"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Maryland Federalist through the party's extinction"},
            {"target": "hartford-convention", "verb": "SERVES_DURING", "note": "Senator during the Federalist Hartford Convention debacle"},
            {"target": "maryland-eastern-shore", "verb": "REPRESENTS", "note": "Tidewater planter gentry Federalist"}
        ]
    }),

    ("vũ-trinh", {
        "summary": (
            "Vũ Trinh (1759–1828) was a "
            "Vietnamese Confucian scholar, "
            "mandarin, and author who "
            "served the Nguyễn lords "
            "and then the Nguyễn dynasty "
            "in various administrative "
            "capacities. He is best "
            "known today as the author "
            "of 'Lan Trì kiến văn lục' "
            "(Records of What I Heard "
            "and Saw at the Orchid Pond, "
            "c. 1800) — a collection "
            "of tales mixing supernatural "
            "stories, moral exempla, "
            "and social observations "
            "written in literary "
            "Chinese (chữ Nôm).\n\n"
            "Vũ Trinh lived through "
            "the most turbulent period "
            "in Vietnamese history — "
            "the Tây Sơn rebellion "
            "that overthrew both "
            "the Nguyễn lords in "
            "the south and the Trịnh "
            "lords in the north, "
            "the brief Tây Sơn "
            "dynasty, and then "
            "the restoration of "
            "Nguyễn power under "
            "Emperor Gia Long (1802) "
            "who unified Vietnam "
            "for the first time "
            "under a single dynasty.\n\n"
            "His literary work "
            "reflects the Confucian "
            "scholarly tradition "
            "while incorporating "
            "popular supernatural "
            "and folk elements "
            "into a genre that "
            "blended high and "
            "popular culture.\n\n"
            "He died under Emperor "
            "Minh Mạng's reign."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vietnamese Confucian scholar-mandarin and author of 'Lan Trì kiến văn lục' (c.1800); lived through the Tây Sơn rebellion, the fall of both Nguyễn and Trịnh lords, and Gia Long's unification of Vietnam (1802); his tale collection blends Confucian moral exempla with supernatural folk elements; significant figure in Vietnamese literary history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Tây Sơn rebellion (1771–1802) — the massive peasant uprising that overthrew both the Nguyễn lords in the south and the Trịnh lords in the north, briefly unifying Vietnam under the Tây Sơn brothers — created the political upheaval through which Vũ Trinh navigated his career",
            "The Confucian mandarin tradition — the Vietnamese state's use of Chinese-educated Confucian scholars to staff its bureaucracy, conducting examinations in literary Chinese and requiring mastery of the classical canon — provided Vũ Trinh his intellectual formation and his official career",
            "The Vietnamese literary tradition of miscellany writing — the genre of collections mixing supernatural tales, moral anecdotes, historical records, and social observations that Vietnamese scholar-officials had been producing since the medieval period — provided the literary framework for Vũ Trinh's 'Lan Trì kiến văn lục'"
        ],
        "effects": [
            "'Lan Trì kiến văn lục' contributed to the Vietnamese literary tradition of miscellany writing — a collection that blended Confucian moral seriousness with popular supernatural and folk elements, preserving both elite and popular cultural material",
            "His survival through the Tây Sơn upheaval and his service under both Tây Sơn and Nguyễn governments illustrated the pragmatic accommodation that mandarin scholars had to make during dynastic transitions — the survival strategies of the scholar-official class",
            "His literary work contributed to Vietnamese cultural memory — preserving stories, observations, and moral exempla from the turbulent late eighteenth century in a form that subsequent generations could access",
            "His career illustrated the continuity of Confucian scholarly culture through Vietnam's most dramatic political upheaval — the persistence of the mandarin tradition even when the dynasties it served collapsed and were replaced"
        ],
        "relationships": [
            {"target": "nguyen-dynasty-vietnam", "verb": "SERVES", "note": "Mandarin serving the Nguyễn dynasty"},
            {"target": "lan-tri-kien-van-luc", "verb": "WRITES", "note": "Author of the famous tale collection c.1800"},
            {"target": "tay-son-rebellion", "verb": "LIVES_THROUGH", "note": "Survived the revolutionary upheaval"},
            {"target": "gia-long-emperor", "verb": "SERVES_UNDER", "note": "Mandarin under the Vietnamese unifier"},
            {"target": "confucian-literary-tradition-vietnam", "verb": "CONTRIBUTES_TO", "note": "Part of the Vietnamese Confucian scholar tradition"}
        ]
    }),

    ("william-giffard", {
        "summary": (
            "William Giffard (d. 1129) was "
            "a Norman ecclesiastic who "
            "served as Chancellor of England "
            "under King William II (Rufus) "
            "and then as Bishop of Winchester "
            "(1100–1129) under Henry I. "
            "As one of the most powerful "
            "sees in England — Winchester "
            "was traditionally the "
            "wealthiest bishopric in "
            "the kingdom — and as a "
            "senior royal administrator, "
            "Giffard was a central "
            "figure in the transition "
            "from the Conqueror's "
            "Norman settlement to "
            "the more stable Henrician "
            "monarchy.\n\n"
            "Giffard's career spanned "
            "the most turbulent decades "
            "of post-Conquest England "
            "— the Rufus reign's "
            "corrupt and erratic "
            "rule, the succession "
            "crisis of 1100 when "
            "Henry I seized the "
            "throne on William II's "
            "death (hunting accident "
            "or murder), and the "
            "subsequent consolidation "
            "of Henrician rule.\n\n"
            "He was involved in "
            "the Investiture Controversy "
            "— the conflict between "
            "pope and king over "
            "the right to invest "
            "bishops — and initially "
            "refused consecration "
            "from the archbishop "
            "of Canterbury in "
            "defiance of papal authority.\n\n"
            "He was a key figure "
            "in Henrician church "
            "and state relations."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Norman Chancellor of England under William II and Bishop of Winchester (1100–1129) under Henry I; bishop of the wealthiest English see; involved in the Investiture Controversy; served through the turbulent transition from Rufus's corrupt rule to Henrician consolidation; central figure in early twelfth-century English church-state relations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Norman Conquest's creation of a new ecclesiastical-political elite — the replacement of English bishops with Norman clergy loyal to the king, who used church offices as rewards for royal service — provided the framework for Giffard's career as both royal administrator and bishop",
            "The Investiture Controversy — the papacy's challenge to secular rulers' right to appoint and invest bishops with temporal authority — created the constitutional conflict that shaped Giffard's episcopal career and his complex position between royal and papal authority",
            "The succession crisis of 1100 — Henry I's seizure of the throne on William II's death — created a new political order in which loyal ecclesiastics like Giffard who supported Henry's accession were rewarded with high church offices"
        ],
        "effects": [
            "His Bishop of Winchester tenure built up the see's wealth and administrative capacity — the Winchester episcopate under Giffard contributing to the development of one of England's most powerful ecclesiastical institutions",
            "His involvement in the Investiture Controversy contributed to the eventual English settlement of the church-state conflict — the compromise reached under Henry I (the Concordat of London, 1107) that resolved the investiture dispute on terms favorable to royal power while respecting papal spiritual authority",
            "His career contributed to the Henrician church settlement — the accommodation between royal and ecclesiastical authority that Henry I's government achieved, making England more stable than the Continental church-state conflicts",
            "His chancellorship under William II contributed to the development of the English royal administration — the chancery as a professional royal secretariat that was developing into the institutional heart of royal government"
        ],
        "relationships": [
            {"target": "henry-i-england", "verb": "SERVES", "note": "Bishop under Henry I"},
            {"target": "william-ii-england", "verb": "SERVES_AS_CHANCELLOR", "note": "Chancellor under William Rufus"},
            {"target": "bishopric-of-winchester", "verb": "SERVES_AS", "note": "Bishop of Winchester 1100–1129"},
            {"target": "investiture-controversy", "verb": "INVOLVED_IN", "note": "Part of the church-state investiture conflict"},
            {"target": "norman-england", "verb": "SERVES_IN", "note": "Norman ecclesiastic in post-Conquest England"}
        ]
    }),

    ("étienne-de-sauvage", {
        "summary": (
            "Étienne de Sauvage (1703–1762) "
            "was a French botanist and "
            "naturalist from Nîmes who "
            "contributed to the development "
            "of botanical classification "
            "and natural history in "
            "eighteenth-century France. "
            "He was a close correspondent "
            "of Carl Linnaeus — the "
            "Swedish naturalist who "
            "established the binomial "
            "nomenclature system that "
            "is the foundation of "
            "modern biological taxonomy "
            "— and contributed to "
            "the development and "
            "application of the "
            "Linnaean system in France.\n\n"
            "De Sauvage's botanical "
            "work contributed to "
            "the Flora of southern "
            "France — the documentation "
            "and classification of "
            "Mediterranean plants "
            "that was one of the "
            "core projects of "
            "eighteenth-century European "
            "natural history. His "
            "correspondence with "
            "Linnaeus made him part "
            "of the international "
            "network of naturalists "
            "who collectively built "
            "the Linnaean taxonomy.\n\n"
            "The plant genus Sauvagesia "
            "was named in his honor "
            "by Linnaeus — the "
            "standard recognition "
            "that Linnaeus gave "
            "to his most valued "
            "botanical correspondents.\n\n"
            "He contributed to the "
            "naturalist republic of "
            "letters that advanced "
            "eighteenth-century science."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French botanist from Nîmes and Linnaeus correspondent; contributed to Mediterranean botanical documentation and the application of Linnaean taxonomy in France; honored by Linnaeus with the plant genus Sauvagesia; part of the international network of naturalists who collectively built eighteenth-century biological classification.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Linnaean revolution in natural history — Carl Linnaeus's development of binomial nomenclature and systematic taxonomy, which created a universal language for natural history — created both the framework and the motivation for naturalists like de Sauvage to document and classify their local flora within the new system",
            "The eighteenth-century naturalist republic of letters — the international network of scholars who corresponded across national boundaries, exchanged specimens and descriptions, and collectively built the natural history knowledge base — provided the institutional framework for de Sauvage's collaboration with Linnaeus",
            "The Mediterranean biodiversity of southern France — the rich flora of Languedoc and Provence that botanical collectors had been documenting since the Renaissance — provided de Sauvage the biological material for his contributions to European botanical classification"
        ],
        "effects": [
            "His botanical documentation of southern French flora contributed to the Linnaean taxonomy's European coverage — providing described specimens and local knowledge that the international natural history network required for comprehensive classification",
            "His correspondence with Linnaeus contributed to the development and refinement of Linnaean taxonomy — the kind of critical engagement with specific regional flora that allowed Linnaeus to improve and extend his system",
            "The naming of genus Sauvagesia in his honor — Linnaeus's standard recognition of valued correspondents — ensured that de Sauvage's contribution to natural history was permanently encoded in the biological nomenclature",
            "His career illustrated the French regional naturalist tradition — the provincial scholars who contributed to national and international natural history by documenting the biodiversity of their localities and connecting with the broader republic of letters"
        ],
        "relationships": [
            {"target": "carl-linnaeus", "verb": "CORRESPONDS_WITH", "note": "Close correspondent who contributed to Linnaean taxonomy"},
            {"target": "sauvagesia-genus", "verb": "HONORED_BY", "note": "Genus named by Linnaeus in his honor"},
            {"target": "french-natural-history", "verb": "CONTRIBUTES_TO", "note": "Botanist documenting southern French flora"},
            {"target": "linnaean-taxonomy", "verb": "APPLIES", "note": "Applied Linnaean system to Mediterranean plants"},
            {"target": "naturalist-republic-of-letters", "verb": "PARTICIPATES_IN", "note": "Member of the international naturalist network"}
        ]
    }),

    ("george-dent", {
        "summary": (
            "George Dent (1756–1813) was "
            "an American Democratic-Republican "
            "politician from Maryland who "
            "served in the U.S. House of "
            "Representatives (1793–1801) "
            "during the critical years "
            "of the young republic's "
            "first party battles — the "
            "fierce conflict between "
            "Federalists and Democratic-Republicans "
            "over the Jay Treaty, the "
            "Quasi-War with France, "
            "the Alien and Sedition Acts, "
            "and ultimately the 'Revolution "
            "of 1800' that brought "
            "Jefferson to power.\n\n"
            "Maryland was one of the "
            "more politically divided "
            "states in this era — "
            "its Eastern Shore planters "
            "inclined toward Federalism "
            "while its western counties "
            "and many of its poorer "
            "farmers supported "
            "Jeffersonian Democratic-Republicanism. "
            "Dent represented this "
            "latter constituency.\n\n"
            "His eight years in "
            "Congress (1793–1801) "
            "covered the most "
            "dramatic and consequential "
            "period of the early "
            "republic — from the "
            "French Revolution's "
            "impact on American "
            "politics through "
            "the first successful "
            "peaceful transfer "
            "of power between "
            "opposing parties.\n\n"
            "He served as a Maryland "
            "state court judge "
            "after his House service."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Democratic-Republican Congressman (1793–1801); served through the Jay Treaty, Quasi-War, Alien and Sedition Acts, and Revolution of 1800; represented the Jeffersonian tradition in politically divided Maryland; subsequent state court judge; witnessed the entire formative decade of the first party system.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's political division between Eastern Shore Federalist planters and Democratic-Republican farmers and western county residents — the social and geographic fault lines that created competitive two-party politics in the state — created the constituency for Dent's Democratic-Republican career",
            "The Federalist-Democratic-Republican political conflict's intensification — the Jay Treaty (1795), the XYZ Affair (1797–1798), the Quasi-War, and the Alien and Sedition Acts — created the political polarization that mobilized Democratic-Republican voters and gave Dent's congressional career its national significance",
            "The French Revolution's impact on American politics — the way the revolutionary upheaval in France forced Americans to choose sides between Federalist caution about popular democracy and Democratic-Republican enthusiasm for French republicanism — framed the major political debates of Dent's congressional career"
        ],
        "effects": [
            "His House service contributed Maryland's Democratic-Republican votes to the critical battles of the early republic — the Jay Treaty ratification fights, the Alien and Sedition Act opposition, and the 1800 electoral crisis",
            "His participation in the 1800 electoral crisis — the House vote on the Jefferson-Burr tie — placed him in one of the most consequential moments in American electoral history",
            "His subsequent state court service contributed to Maryland's judicial tradition — transitioning from legislative to judicial service in the pattern common among early republic lawyers",
            "His career illustrated the pattern of Maryland Democratic-Republican politics — the Jeffersonian tradition that coexisted with the Federalist Eastern Shore planter class in a politically contested state"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Congressman 1793–1801"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian in politically divided Maryland"},
            {"target": "alien-and-sedition-acts", "verb": "OPPOSES", "note": "Democratic-Republican opponent of the acts"},
            {"target": "revolution-of-1800", "verb": "PARTICIPATES_IN", "note": "House member during the Jefferson-Burr crisis"},
            {"target": "jay-treaty", "verb": "VOTES_ON", "note": "Congressman during the Jay Treaty fight"}
        ]
    }),

    ("isaac-wilbour", {
        "summary": (
            "Isaac Wilbour (1763–1837) was "
            "an American Democratic-Republican "
            "politician from Rhode Island "
            "who served in the U.S. House "
            "of Representatives (1807–1809) "
            "during the Jefferson administration's "
            "final years. His brief House "
            "tenure coincided with one "
            "of the most controversial "
            "episodes of Jefferson's "
            "presidency: the Embargo Act "
            "of 1807 — Jefferson's "
            "attempt to coerce Britain "
            "and France into respecting "
            "American neutral rights "
            "by prohibiting American "
            "commercial vessels from "
            "trading with foreign ports.\n\n"
            "Rhode Island was one of "
            "the states most severely "
            "damaged by the Embargo — "
            "its economy was deeply "
            "dependent on maritime "
            "commerce, and the Embargo's "
            "near-total prohibition "
            "of foreign trade devastated "
            "Rhode Island merchants, "
            "sailors, and port workers. "
            "The Embargo was deeply "
            "unpopular in New England.\n\n"
            "Rhode Island in this "
            "period still operated "
            "under its 1663 colonial "
            "charter — it had no "
            "state constitution "
            "and its voting franchise "
            "was restricted to "
            "freeholders, making "
            "it constitutionally "
            "anomalous.\n\n"
            "He lived to seventy-four."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Rhode Island Democratic-Republican Congressman (1807–1809); served during the Jefferson Embargo that devastated Rhode Island's maritime economy; from the most constitutionally anomalous state in the early republic (still under 1663 colonial charter); represented the tension between Jeffersonian politics and New England commercial interests.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Jefferson Embargo Act (1807) — the trade prohibition that was the defining policy controversy of Jefferson's final year in office — created the political crisis that defined Wilbour's brief House tenure, forcing him to either support the party line or defend Rhode Island's devastated maritime economy",
            "Rhode Island's maritime commercial economy — the state's deep dependence on trade with Britain and the West Indies — created the tension between Wilbour's Democratic-Republican party loyalty and his constituents' economic interests during the Embargo crisis",
            "Rhode Island's unusual political situation under the 1663 colonial charter — the restricted franchise and unusual constitutional arrangements — created the distinctive political environment that produced Rhode Island's Democratic-Republican minority in a generally Federalist state"
        ],
        "effects": [
            "His House service during the Embargo Crisis contributed Rhode Island's Democratic-Republican voice to the debates over Jefferson's trade policy — representing one of the states most severely damaged by the Embargo while nominally supporting the president's party",
            "His career illustrated the tension between Democratic-Republican party loyalty and constituency interests in New England — the way the Embargo forced Democratic-Republican representatives from commercial states to choose between principle and political survival",
            "His one-term House service ended as the Embargo's unpopularity contributed to Democratic-Republican losses in New England — the policy disaster that eventually led Jefferson to repeal the Embargo days before leaving office",
            "His career contributed to Rhode Island's Democratic-Republican minority — the Jeffersonian tradition in a state where commercial interests generally favored Federalism"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Rhode Island Congressman 1807–1809"},
            {"target": "embargo-act-1807", "verb": "SERVES_DURING", "note": "Congressman during the devastating trade embargo"},
            {"target": "rhode-island", "verb": "REPRESENTS", "note": "From the most constitutionally anomalous early republic state"},
            {"target": "thomas-jefferson", "verb": "SUPPORTS", "note": "Democratic-Republican during Jefferson's final term"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian in Federalist New England"}
        ]
    }),

    ("pedro-nolasco-vergara-albano", {
        "summary": (
            "Pedro Nolasco Vergara Albano "
            "(1777–1833) was a Chilean "
            "lawyer and politician who "
            "contributed to the early "
            "institutional and legal "
            "development of independent "
            "Chile. Active during the "
            "Wars of Independence and "
            "the tumultuous first decades "
            "of Chilean self-governance, "
            "he served in various legal "
            "and governmental capacities "
            "as Chile worked to build "
            "republican institutions "
            "from the ground up.\n\n"
            "Chile's independence process "
            "— from the First National "
            "Government Junta of 1810 "
            "through the Reconquista "
            "(Spanish reoccupation, "
            "1814–1817), the Battle of "
            "Chacabuco (1817), and "
            "O'Higgins's independence "
            "regime — required trained "
            "lawyers and administrators "
            "to staff the emerging "
            "national institutions "
            "in the face of royalist "
            "opposition and the "
            "profound challenges of "
            "state-building ex nihilo.\n\n"
            "His career navigated "
            "the dramatic swings "
            "of Chilean politics "
            "in the 1810s–1820s "
            "— from colonial law "
            "to patriot governance, "
            "through the royalist "
            "Reconquista, and back "
            "to patriot rule under "
            "O'Higgins and then "
            "the conservative-liberal "
            "conflicts of the 1820s.\n\n"
            "He died in 1833, the "
            "year the conservative "
            "constitution took effect."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Chilean lawyer and politician contributing to early republican institution-building; navigated the Wars of Independence, the Reconquista, O'Higgins's independence regime, and the conservative-liberal constitutional conflicts of the 1820s; died in 1833, the year the conservative constitution took effect; part of the generation that built Chilean independence from the ground up.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Chilean independence movement — the 1810 junta's break with colonial authority, the subsequent wars against royalist forces, and the final liberation under O'Higgins and San Martín — created the political transformation within which Vergara Albano's career developed",
            "Chile's need for trained lawyers to build republican institutions — the courts, legislative bodies, and administrative systems that the independence movement had to create while simultaneously fighting for survival — created the demand for Vergara Albano's legal expertise",
            "The dramatic instability of Chilean politics in the 1810s–1820s — the oscillation between patriot and royalist control, O'Higgins's authoritarian republic, and the subsequent liberal-conservative conflict — created the challenging political environment within which Vergara Albano's career was situated"
        ],
        "effects": [
            "His legal and governmental service contributed to the institutional development of independent Chile — helping staff the courts, legal system, and administrative bodies of the new republic",
            "His career navigating the turbulent first independence decades contributed to the continuity of legal and administrative practice across political changes — the kind of professional continuity that state-building required regardless of which faction was politically dominant",
            "His death in 1833 — the year Mariano Egaña's conservative constitution took effect — placed him as a witness to the founding generation's entire struggle and ultimate constitutional settlement",
            "His career illustrated the experience of the Chilean lawyer class during independence — the trained professionals who had to navigate between colonial law and republican institutions while political control oscillated between patriots and royalists"
        ],
        "relationships": [
            {"target": "chile", "verb": "SERVES", "note": "Chilean lawyer and republican institution-builder"},
            {"target": "chilean-independence", "verb": "CONTRIBUTES_TO", "note": "Part of the Chilean independence movement"},
            {"target": "bernardo-ohiggins", "verb": "SERVES_UNDER", "note": "Lawyer during O'Higgins's independence regime"},
            {"target": "chilean-reconquista", "verb": "SURVIVES", "note": "Navigated the Spanish reoccupation period 1814–1817"},
            {"target": "chilean-constitution-1833", "verb": "PRECEDES", "note": "Died in the year the conservative constitution took effect"}
        ]
    }),

    ("frederik-motzfeldt", {
        "summary": (
            "Frederik Motzfeldt (1777–1854) "
            "was a Norwegian jurist and "
            "statesman who served as "
            "President of the Norwegian "
            "Supreme Court (Norges Høyesterett) "
            "and as a member of the "
            "Norwegian Council of State "
            "(Statsråd) during the critical "
            "decades of Norwegian "
            "constitutional development "
            "after the 1814 Eidsvoll "
            "Constitution. As President "
            "of the Supreme Court, "
            "he was the highest judicial "
            "officer in Norway — a "
            "position of enormous "
            "importance in building "
            "the jurisprudence and "
            "institutional authority "
            "of the new constitutional "
            "order.\n\n"
            "Motzfeldt's legal career "
            "contributed to the development "
            "of Norwegian constitutional "
            "jurisprudence during the "
            "most formative period "
            "of the nation's independent "
            "legal tradition — the "
            "decades when the Norwegian "
            "Supreme Court was establishing "
            "its authority and developing "
            "its distinctive constitutional "
            "role within the Swedish-Norwegian "
            "union.\n\n"
            "His long career spanned "
            "the entire constitutional "
            "construction period from "
            "1814 through the mid-nineteenth "
            "century — from the revolutionary "
            "constitutional moment "
            "to the stable constitutional "
            "monarchy that the 1814 "
            "framework eventually produced.\n\n"
            "He was a foundational "
            "figure in Norwegian constitutional law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "President of the Norwegian Supreme Court and Council of State member; contributed to the foundational development of Norwegian constitutional jurisprudence after the 1814 Eidsvoll Constitution; highest judicial officer in Norway during the most formative decades of the constitutional order; key figure in building the Supreme Court's institutional authority.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — the Eidsvoll Constitution that established the Supreme Court as the highest judicial body in Norway — created both the institutional framework and the urgent need for capable jurists like Motzfeldt to build the court's jurisprudence from scratch",
            "The Swedish-Norwegian union (1814) and the constitutional tension it created — Norway's determination to maintain its constitutional autonomy within the forced union with Sweden — gave the Norwegian Supreme Court an important role in protecting Norwegian legal independence against Swedish encroachment",
            "Norway's need to develop a distinctively Norwegian legal tradition — moving away from Danish colonial law toward an independent Norwegian jurisprudence appropriate to the new constitutional state — created the intellectual and institutional challenge that Supreme Court leadership like Motzfeldt's had to address"
        ],
        "effects": [
            "His Supreme Court presidency contributed to the development of Norwegian constitutional jurisprudence — building the case law, judicial culture, and institutional authority that made the Supreme Court the cornerstone of Norwegian constitutional order",
            "His Council of State service contributed to the executive governance of Norway — providing legal expertise to the executive branch and helping develop the constitutional conventions that governed the Norwegian-Swedish union",
            "His long career's bridge from the 1814 constitutional moment through the mid-nineteenth century provided continuity to Norwegian legal development — the institutional memory and jurisprudential consistency that courts require to develop coherent legal doctrine",
            "His career contributed to the Norwegian nation-building project's legal dimension — the development of distinctively Norwegian legal institutions that expressed Norwegian national identity within the Swedish-Norwegian union"
        ],
        "relationships": [
            {"target": "norwegian-supreme-court", "verb": "PRESIDES_OVER", "note": "President of Norges Høyesterett"},
            {"target": "norwegian-council-of-state", "verb": "SERVES_ON", "note": "Member of the Norwegian Statsråd"},
            {"target": "norwegian-constitution-1814", "verb": "IMPLEMENTS", "note": "Jurist building jurisprudence under the Eidsvoll Constitution"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_DURING", "note": "Career within the forced union with Sweden"},
            {"target": "norwegian-legal-tradition", "verb": "FOUNDS", "note": "Foundational figure in Norwegian constitutional law"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 67 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
