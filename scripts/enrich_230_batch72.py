#!/usr/bin/env python3
"""
Batch 72 — 8 entities: José Joaquim Carneiro de Campos, Lars Johannes Irgens,
Richard D. Davis, Diego Núñez de Avendaño, George Neville, James Madison Porter,
Robert Cooper Grier, Robert Strange
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

    ("josé-joaquim-carneiro-de-campos", {
        "summary": (
            "José Joaquim Carneiro de "
            "Campos, Marquis of Caravelas "
            "(1768–1836) was a Brazilian "
            "statesman and jurist who "
            "was one of the principal "
            "drafters of the Brazilian "
            "Constitution of 1824 — "
            "the first and only "
            "constitution of the "
            "Brazilian Empire, which "
            "remained in effect until "
            "the monarchy's fall in "
            "1889. As the leading "
            "constitutional drafter, "
            "he shaped the document "
            "that gave Brazil its "
            "distinctive four-power "
            "constitutional structure "
            "— executive, legislative, "
            "judicial, and the "
            "'Moderating Power' "
            "held by the emperor "
            "that was unique in "
            "world constitutional law.\n\n"
            "The Moderating Power "
            "(Poder Moderador) — "
            "derived from Benjamin "
            "Constant's constitutional "
            "theory — gave Emperor "
            "Pedro I the authority "
            "to balance and moderate "
            "the other three powers, "
            "appointing senators, "
            "dissolving the Chamber, "
            "and appointing ministers.\n\n"
            "He had served as "
            "Pedro I's Minister "
            "of Foreign Affairs "
            "and was a founding "
            "figure of the Brazilian "
            "state after independence "
            "(September 7, 1822).\n\n"
            "His constitutional work "
            "shaped Brazil for "
            "65 years."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Principal drafter of the Brazilian Constitution of 1824 — in effect until 1889; created the unique four-power constitutional structure including the 'Moderating Power' (Poder Moderador) derived from Benjamin Constant; Pedro I's Foreign Minister; founding figure of the Brazilian Empire; his constitutional work shaped Brazil for 65 years.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Brazilian independence (September 7, 1822) — Pedro I's declaration of independence from Portugal and the establishment of the Brazilian Empire — created the constitutional void that required a founding document to give the new state its legal framework",
            "The dissolution of the 1823 Constituent Assembly — Pedro I's forcible closure of the first assembly that was drafting a too-liberal constitution — created the need for a new drafting process that Carneiro de Campos led as part of a smaller committee",
            "Benjamin Constant's constitutional theory — the French philosopher's concept of a 'neutral' or moderating power that could balance the executive, legislative, and judicial powers — provided the theoretical foundation for the Moderating Power that was the 1824 constitution's most distinctive feature"
        ],
        "effects": [
            "His constitutional drafting created the Brazilian Constitution of 1824 — a document of world-historical significance as the foundational law of the largest nation in Latin America that governed the Brazilian Empire for 65 years and shaped the country's political development",
            "The Moderating Power he incorporated into the constitution gave the Brazilian emperor extraordinary constitutional authority — the power to appoint senators, dissolve the Chamber, and appoint ministers that concentrated substantial power in the monarch while maintaining parliamentary forms",
            "His Foreign Ministry work contributed to establishing Brazil's international position — securing recognition from European powers and the United States for the new empire's sovereignty",
            "His constitutional legacy shaped Brazil's distinctive political culture — the centralized, moderating-power tradition that created a different political development path from the federal, republican constitutionalism of Spanish America"
        ],
        "relationships": [
            {"target": "brazil", "verb": "FOUNDS_CONSTITUTION_OF", "note": "Principal drafter of the 1824 Brazilian Constitution"},
            {"target": "pedro-i-brazil", "verb": "SERVES", "note": "Pedro I's Foreign Minister and constitutional drafter"},
            {"target": "brazilian-empire", "verb": "ESTABLISHES_INSTITUTIONS_OF", "note": "Founding figure of the Brazilian imperial state"},
            {"target": "moderating-power", "verb": "CREATES", "note": "Architect of the Poder Moderador in Brazilian constitution"},
            {"target": "benjamin-constant-philosopher", "verb": "APPLIES_THEORY_OF", "note": "Applied Constant's constitutional theory to Brazil"}
        ]
    }),

    ("lars-johannes-irgens", {
        "summary": (
            "Lars Johannes Irgens "
            "(1763–1831) was a Norwegian "
            "jurist and politician who "
            "played a significant role "
            "in the Norwegian independence "
            "movement of 1814 — "
            "the remarkable period "
            "when Norway, briefly "
            "freed from Danish rule "
            "when Denmark ceded Norway "
            "to Sweden after Napoleonic "
            "defeats, convened a "
            "constitutional assembly "
            "at Eidsvoll and drafted "
            "one of the most liberal "
            "constitutions in 19th-century "
            "Europe before being "
            "forced into union "
            "with Sweden.\n\n"
            "Irgens participated "
            "in the Eidsvoll "
            "assembly (April–May "
            "1814) — one of the "
            "112 delegates who "
            "drafted the Norwegian "
            "Constitution of May 17, "
            "1814, a date still "
            "celebrated as Norway's "
            "National Day. The "
            "constitution established "
            "a constitutional "
            "monarchy with a "
            "powerful Storting "
            "(parliament) that "
            "was remarkably democratic "
            "for its era.\n\n"
            "Though Norway was "
            "subsequently forced "
            "into union with "
            "Sweden, the 1814 "
            "constitution survived "
            "and governed Norway "
            "until 1905 independence.\n\n"
            "He was a founding "
            "figure of the Norwegian state."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Norwegian delegate to the Eidsvoll Constitutional Assembly (1814); participated in drafting the Norwegian Constitution of May 17, 1814 — still celebrated as Norway's National Day; the constitution survived Swedish union and governed Norway until 1905; founding figure of the Norwegian constitutional state.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Napoleonic Wars' disruption of Scandinavian politics — Denmark's alliance with Napoleon and defeat led to the Treaty of Kiel (January 1814) ceding Norway to Sweden, creating the political vacuum that the Norwegian independence movement filled",
            "The brief Norwegian independence window (January–November 1814) — the period between Denmark's cession and Sweden's military pressure that forced union — provided the opportunity for the Eidsvoll assembly to draft a constitution",
            "Norwegian national consciousness — the educated elite's sense of Norwegian cultural and historical distinctiveness from both Denmark (the previous ruler) and Sweden (the prospective new ruler) — created the political will to draft a liberal constitution rather than simply accepting Swedish terms"
        ],
        "effects": [
            "His participation in the Eidsvoll assembly contributed to drafting one of the most significant constitutional documents of the 19th century — a liberal constitution that gave Norway a powerful parliament and constitutional monarchy before most European countries had achieved either",
            "The Norwegian Constitution of 1814 that he helped draft survived Swedish union and continued to govern Norway — the document's resilience across 91 years of union with Sweden until Norway's independence in 1905 testifying to its fundamental soundness",
            "His constitutional work contributed to establishing Norway's distinctive political identity — the parliamentary democracy tradition that would eventually produce full independence and one of the world's most advanced social democracies",
            "His career contributed to the Norwegian legal tradition — the jurisprudence of a country that had been governed under Danish law and was now building its own national legal institutions"
        ],
        "relationships": [
            {"target": "eidsvoll-constitutional-assembly", "verb": "SERVES_IN", "note": "Delegate to the 1814 constitutional assembly"},
            {"target": "norwegian-constitution-1814", "verb": "DRAFTS", "note": "Participant in drafting May 17, 1814 constitution"},
            {"target": "norway", "verb": "HELPS_FOUND", "note": "Founding figure of the Norwegian constitutional state"},
            {"target": "norwegian-independence-1814", "verb": "PARTICIPATES_IN", "note": "Part of the brief independence movement"},
            {"target": "storting", "verb": "ESTABLISHES", "note": "Constitutional author of the Norwegian parliament"}
        ]
    }),

    ("richard-d-davis", {
        "summary": (
            "Richard D. Davis (1799–1871) "
            "was an American Democratic "
            "politician from New York "
            "who served in the U.S. "
            "House of Representatives "
            "(1841–1845) during the "
            "critical final years of "
            "the Van Buren-Tyler "
            "political transition "
            "and the opening of the "
            "Polk era. As a New York "
            "Democrat during one of "
            "the most factionally "
            "divided periods of New "
            "York Democratic politics, "
            "Davis navigated the "
            "complex divisions between "
            "the Barnburners (anti-slavery "
            "expansion, hard money) "
            "and the Hunkers (pro-slavery "
            "accommodation, soft money) "
            "that were tearing New "
            "York's Democratic Party apart.\n\n"
            "His House service "
            "coincided with the "
            "Tyler administration's "
            "political chaos — "
            "the accidental president "
            "who vetoed the Whig "
            "economic program and "
            "was expelled from "
            "his own party — and "
            "the beginning of "
            "the Texas annexation "
            "controversy.\n\n"
            "New York was America's "
            "most politically "
            "important state in "
            "this era — a large "
            "electoral prize whose "
            "complex Democratic "
            "factional politics "
            "had national implications.\n\n"
            "He was a lawyer and "
            "businessman before politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New York Democratic Congressman (1841–1845); navigated the Barnburner-Hunker factional split in New York's Democratic Party; served during the Tyler administration's political chaos and the Texas annexation controversy opening; part of New York's complex antebellum Democratic politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Democratic factional split — the Barnburner-Hunker division over slavery extension, banking policy, and patronage that made New York's Democratic politics among the most complex in the nation — created the challenging political environment that Davis had to navigate",
            "The Tyler administration's political chaos — the Whig president who vetoed the Whig program and was expelled from his party — created the extraordinary congressional environment of Davis's House tenure",
            "New York's commercial and economic diversity — the state's combination of merchant interests, farmers, workers, and immigrants whose competing economic interests generated complex political coalitions — created the political landscape for Davis's career"
        ],
        "effects": [
            "His House service contributed New York's Democratic perspective to the Tyler era's chaotic congressional politics — navigating the Whig collapse and the uncertain direction of national policy",
            "His navigation of the Barnburner-Hunker split contributed to the factional dynamics that would eventually produce the Free Soil Party split of 1848 — the New York Democratic division that cost Van Buren New York and gave the presidency to Zachary Taylor",
            "His career illustrated the complexity of New York Democratic politics — the multi-factional machine politics that made the Empire State simultaneously the most important and most internally divided state in the antebellum party system",
            "His death in 1871 placed him among the antebellum Democratic politicians who survived the Civil War and witnessed the Republican Party's dominance of the subsequent Gilded Age"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1841–1845"},
            {"target": "barnburners-democrats", "verb": "NAVIGATES", "note": "New York Democrat during Barnburner-Hunker split"},
            {"target": "john-tyler", "verb": "SERVES_DURING", "note": "Congressman during Tyler's chaotic presidency"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "New York Democratic politician"},
            {"target": "texas-annexation", "verb": "SERVES_DURING", "note": "Congressman as Texas annexation controversy opened"}
        ]
    }),

    ("diego-núñez-de-avendaño", {
        "summary": (
            "Diego Núñez de Avendaño "
            "(1512–c. 1595) was a "
            "Spanish jurist and legal "
            "scholar who made significant "
            "contributions to colonial "
            "law — the legal system "
            "governing Spain's American "
            "empire. His major work "
            "was a treatise on the "
            "authority and jurisdiction "
            "of Spanish colonial "
            "officials — the visitadores "
            "and other royal inspectors "
            "— that became a standard "
            "reference for understanding "
            "the legal framework "
            "of colonial governance.\n\n"
            "The Spanish colonial "
            "legal system was one "
            "of the most elaborate "
            "in history — a complex "
            "body of law combining "
            "Castilian law, Roman "
            "law, canon law, and "
            "specifically American "
            "decrees that governed "
            "the relationship between "
            "the Crown, colonial "
            "officials, settlers, "
            "indigenous people, "
            "and the Church.\n\n"
            "Núñez de Avendaño "
            "worked within the "
            "tradition of Spanish "
            "scholastic jurisprudence "
            "— the legal scholars "
            "who combined Thomist "
            "theology, Roman law, "
            "and royal decrees "
            "into a comprehensive "
            "system of colonial governance.\n\n"
            "He contributed to "
            "the development of "
            "Spanish colonial law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish colonial jurist (1512–c.1595); authority on the jurisdiction of colonial visitadores and royal inspectors; worked in the tradition of Spanish scholastic jurisprudence combining Roman law, canon law, and colonial decrees; contributed to the elaborate legal framework governing Spain's American empire.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Spain's need for systematic colonial legal governance — the challenge of administering a vast empire across the Atlantic required a coherent legal framework that scholars like Núñez de Avendaño helped provide by systematizing the complex body of colonial law",
            "The Spanish scholastic legal tradition — the combination of Thomist philosophy, Roman law, and royal decrees that Spanish universities produced and that governed both metropolitan and colonial governance — created the intellectual framework for Núñez de Avendaño's jurisprudence",
            "The colonial visitador system's complexity — the elaborate system of royal inspections and oversight that attempted to manage colonial officials from Spain — required scholarly analysis of jurisdiction, authority, and procedures that Núñez de Avendaño provided"
        ],
        "effects": [
            "His treatise on colonial visitadores and royal inspectors became a standard reference for understanding the legal framework of Spanish colonial governance — used by colonial officials, lawyers, and subsequent legal scholars",
            "His scholarship contributed to the systematization of Spanish colonial law — the gradual development of a coherent legal system for the Americas that colonial administrators could apply",
            "His work contributed to the intellectual tradition of Spanish colonial jurisprudence — the body of legal scholarship that justified and organized Spanish rule in America and that subsequent critics (like Las Casas) also had to engage",
            "His career illustrated the Spanish colonial legal tradition's sophistication — the way Spain deployed elaborate legal frameworks to govern its empire and the scholarly infrastructure that supported those frameworks"
        ],
        "relationships": [
            {"target": "spanish-colonial-law", "verb": "DEVELOPS", "note": "Authority on colonial visitador jurisdiction"},
            {"target": "spanish-empire", "verb": "SERVES", "note": "Jurist serving the Spanish colonial legal system"},
            {"target": "visitadores", "verb": "ANALYZES", "note": "Major treatise on royal inspectors' authority"},
            {"target": "scholastic-jurisprudence", "verb": "WORKS_IN", "note": "Part of the Spanish scholastic legal tradition"},
            {"target": "roman-law", "verb": "APPLIES", "note": "Combined Roman law with colonial governance frameworks"}
        ]
    }),

    ("george-neville", {
        "summary": (
            "George Neville (c. 1432–1476) "
            "was a powerful English "
            "churchman and politician "
            "who served as Archbishop "
            "of York (1465–1476) and "
            "Lord Chancellor of England "
            "— one of the most powerful "
            "secular positions in "
            "the kingdom — during "
            "the Wars of the Roses. "
            "He was the brother of "
            "Richard Neville, Earl "
            "of Warwick — 'the Kingmaker' "
            "— whose political maneuvers "
            "dominated the middle "
            "phase of the Wars of "
            "the Roses as he twice "
            "made and unmade English kings.\n\n"
            "George Neville's career "
            "was intimately bound "
            "to his family's political "
            "fortunes — he rose "
            "to the chancellorship "
            "when Warwick controlled "
            "Edward IV's government "
            "and fell from power "
            "when Warwick's rebellion "
            "against Edward IV "
            "failed and Warwick "
            "was killed at the "
            "Battle of Barnet (1471).\n\n"
            "His famous banquet "
            "at the enthronement "
            "ceremony for his "
            "York archbishopric "
            "(1465) was one of "
            "the most spectacular "
            "medieval English feasts "
            "recorded — thousands "
            "of guests, hundreds "
            "of cattle, thousands "
            "of sheep.\n\n"
            "He died in 1476 under "
            "Edward IV's displeasure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Archbishop of York (1465–1476) and Lord Chancellor during the Wars of the Roses; brother of Warwick 'the Kingmaker'; his career followed his family's political fortunes through the making and unmaking of English kings; fell from power after Barnet (1471); his enthronement banquet was one of the most spectacular medieval English feasts recorded.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Wars of the Roses — the dynastic civil war between Yorkists and Lancastrians that tore English political society apart and made loyalty to the correct faction the key to political survival — created the unstable political environment within which George Neville's career rose and fell",
            "The Neville family's political dominance — the Earls of Warwick's extraordinary political and military power that made Richard Neville 'the Kingmaker' — provided George Neville the political patronage and family connection that elevated him to the archbishopric and chancellorship",
            "The medieval church-state connection — the tradition of senior churchmen serving in high secular offices as the most literate and politically sophisticated administrators available — created the institutional framework within which an archbishop could simultaneously hold the Lord Chancellorship"
        ],
        "effects": [
            "His Lord Chancellorship under Warwick's Yorkist dominance contributed to the governance of England during one of its most politically turbulent periods — the administration of the realm while his brother remade the political landscape",
            "His fall from power after Barnet (1471) — Edward IV's reassertion of personal control after Warwick's death — illustrated the vulnerability of churchmen who had too closely identified their careers with a specific political faction",
            "His famous enthronement banquet (1465) contributed to the historical record of late medieval English conspicuous consumption — the spectacular display of wealth and power that characterized the highest reaches of English society",
            "His career illustrated the political role of the medieval church — the way senior ecclesiastical positions were distributed as political rewards and how churchmen wielded secular power alongside their spiritual authority"
        ],
        "relationships": [
            {"target": "archbishop-of-york", "verb": "SERVES_AS", "note": "Archbishop 1465–1476"},
            {"target": "richard-neville-earl-of-warwick", "verb": "FAMILY_OF", "note": "Brother of 'the Kingmaker'"},
            {"target": "lord-chancellor-england", "verb": "SERVES_AS", "note": "Lord Chancellor during Warwick's ascendancy"},
            {"target": "wars-of-the-roses", "verb": "SERVES_DURING", "note": "Career defined by the Yorkist-Lancastrian conflict"},
            {"target": "battle-of-barnet-1471", "verb": "FALLS_FROM_POWER_AFTER", "note": "Lost influence after Warwick's death at Barnet"}
        ]
    }),

    ("james-madison-porter", {
        "summary": (
            "James Madison Porter (1793–1862) "
            "was an American lawyer, educator, "
            "and politician from Pennsylvania "
            "who briefly served as U.S. "
            "Secretary of War (1843–1844) "
            "under President John Tyler "
            "— one of the briefest and "
            "most contested cabinet "
            "appointments in American "
            "history, as the Senate "
            "refused to confirm him "
            "and he served only on "
            "recess appointment. "
            "Porter was a co-founder "
            "of Lafayette College "
            "in Easton, Pennsylvania "
            "(1826) — a Presbyterian-affiliated "
            "liberal arts college "
            "that became one of "
            "the important educational "
            "institutions of the "
            "mid-Atlantic region.\n\n"
            "Tyler's presidency was "
            "politically disastrous "
            "— the accidental president "
            "who vetoed the Whig "
            "program and was expelled "
            "from the Whig Party "
            "could not get his "
            "cabinet appointments "
            "confirmed by the "
            "Whig-dominated Senate.\n\n"
            "Porter's War Department "
            "tenure was significant "
            "in one respect: he "
            "presided over early "
            "discussions of Texas "
            "annexation's military "
            "implications.\n\n"
            "His Lafayette College "
            "co-founding left a "
            "more lasting legacy "
            "than his cabinet service."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "U.S. Secretary of War (recess appointment 1843–1844) under Tyler — Senate refused to confirm; co-founder of Lafayette College (1826); served during early Texas annexation military discussions; his cabinet appointment illustrated Tyler's political isolation; Lafayette College became his more lasting legacy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Tyler's political isolation — the Whig president who had been expelled from his own party after vetoing the Whig economic program and who could not get confirmations from the Whig-controlled Senate — created the circumstances of Porter's unconfirmed War Department appointment",
            "Porter's Pennsylvania Democratic-Tyler alignment — his connection to the Pennsylvania political network that Tyler was cultivating as he tried to build a third-party or Democratic political future — provided the basis for his appointment",
            "The Texas annexation question's military dimension — Tyler's determination to annex Texas and the War Department's role in evaluating the military implications — created the policy context for Porter's brief tenure"
        ],
        "effects": [
            "His War Department tenure — though brief and unconfirmed — contributed to the early discussions of Texas annexation's military planning, helping lay groundwork for the eventual annexation and Mexican-American War",
            "The Senate's refusal to confirm him illustrated Tyler's complete political isolation — the extraordinary situation of a president whose cabinet nominations were systematically rejected by his nominal party",
            "His Lafayette College co-founding (1826) contributed to Pennsylvania education — the college that became a significant liberal arts institution in the Lehigh Valley and trained generations of American professionals",
            "His career illustrated the instability of Tyler's presidency — the political chaos of an administration without a congressional majority, partisan support, or reliable cabinet that characterized John Tyler's four years in office"
        ],
        "relationships": [
            {"target": "us-department-of-war", "verb": "LEADS", "note": "Secretary of War on recess appointment 1843–1844"},
            {"target": "john-tyler", "verb": "SERVES_UNDER", "note": "Tyler's unconfirmed War Secretary"},
            {"target": "lafayette-college", "verb": "CO-FOUNDS", "note": "Co-founder of Lafayette College 1826"},
            {"target": "texas-annexation", "verb": "ADVISES_ON", "note": "War Secretary during early annexation military discussions"},
            {"target": "us-senate", "verb": "REJECTED_BY", "note": "Senate refused to confirm his appointment"}
        ]
    }),

    ("robert-cooper-grier", {
        "summary": (
            "Robert Cooper Grier (1794–1870) "
            "was an American jurist "
            "who served as an Associate "
            "Justice of the U.S. Supreme "
            "Court (1846–1870) — appointed "
            "by President Polk and "
            "serving 24 years through "
            "the most consequential "
            "period in American legal "
            "history: the antebellum "
            "sectional crisis, the "
            "Civil War, and Reconstruction. "
            "He is best known for "
            "his role in the Dred "
            "Scott decision (1857) "
            "— in which he voted "
            "with the majority to "
            "deny Dred Scott's "
            "freedom, learning "
            "beforehand of Taney's "
            "intended opinion and "
            "sharing that information "
            "with President-elect "
            "Buchanan — a serious "
            "breach of judicial "
            "propriety.\n\n"
            "Grier's Dred Scott vote "
            "and his pre-decision "
            "communication with "
            "Buchanan was one of "
            "the first major judicial "
            "ethics scandals in "
            "Supreme Court history.\n\n"
            "His Civil War-era "
            "service contributed "
            "to sustaining the "
            "Lincoln administration's "
            "war powers — he was "
            "in the majority in "
            "the Prize Cases (1863) "
            "upholding Lincoln's "
            "blockade of the South.\n\n"
            "He retired in 1870 "
            "under pressure from "
            "colleagues due to "
            "mental incapacity."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Supreme Court Justice (1846–1870); voted with the majority in Dred Scott (1857) and breached judicial ethics by sharing the outcome with Buchanan before announcement; supported Lincoln's blockade in the Prize Cases (1863); retired under pressure for mental incapacity (1870) — one of the few forced judicial retirements in Supreme Court history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Polk's Supreme Court appointment — seeking a Pennsylvania Democrat with judicial experience for the Court vacancy — created Grier's elevation from the Pennsylvania bench to the Supreme Court",
            "The Dred Scott case — the long-running freedom suit that the Taney Court decided to use for a comprehensive ruling on slavery's constitutional status — created the major judicial controversy of Grier's most consequential moment",
            "Grier's mental decline in his final years — the cognitive deterioration that made his continued service increasingly problematic — created the extraordinary situation of colleagues discussing his removal, ultimately leading to the first instance of formal pressure on a Justice to retire"
        ],
        "effects": [
            "His Dred Scott vote and the breach of judicial propriety in communicating with Buchanan contributed to one of the most criticized decisions in Supreme Court history — helping to invalidate the Missouri Compromise and deny constitutional personhood to enslaved people",
            "His Prize Cases vote upholding Lincoln's naval blockade contributed to sustaining the Union's war powers during the Civil War's critical early phase — one of the most important constitutional decisions of the war",
            "His forced retirement in 1870 contributed to the development of judicial retirement norms — establishing that severe mental incapacity was grounds for colleagues to request a Justice's departure",
            "His 24-year tenure across the antebellum, Civil War, and Reconstruction eras gave him one of the most consequentially positioned Supreme Court careers in American history — serving through the country's most existential constitutional crises"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1846–1870"},
            {"target": "james-k-polk", "verb": "APPOINTED_BY", "note": "Polk's Supreme Court appointment"},
            {"target": "dred-scott-v-sandford", "verb": "VOTES_IN", "note": "Majority vote and pre-decision communication with Buchanan"},
            {"target": "prize-cases-1863", "verb": "DECIDES", "note": "Majority upholding Lincoln's naval blockade"},
            {"target": "taney-court", "verb": "SERVES_ON", "note": "Taney Court member during Dred Scott decision"}
        ]
    }),

    ("robert-strange", {
        "summary": (
            "Robert Strange (1796–1854) "
            "was an American Democratic "
            "politician and jurist from "
            "North Carolina who served "
            "as a U.S. Senator (1836–1840) "
            "and as a North Carolina "
            "Supreme Court justice. "
            "A prominent figure in "
            "North Carolina's Democratic "
            "Party during the Jacksonian "
            "era, Strange navigated "
            "the complex politics "
            "of a Southern state "
            "that maintained significant "
            "Whig competition despite "
            "its strong Democratic "
            "tradition.\n\n"
            "His Senate tenure "
            "coincided with the "
            "Van Buren administration "
            "and the Panic of 1837 "
            "— the economic depression "
            "that devastated Van "
            "Buren's presidency "
            "and made the Democrats "
            "politically vulnerable. "
            "Strange's hard-money "
            "Independent Treasury "
            "position aligned "
            "with the mainstream "
            "Democratic response "
            "to the Panic.\n\n"
            "He was also a novelist "
            "— his historical "
            "novel 'Eoneguski, or "
            "The Cherokee Chief' "
            "(1839) was one of "
            "the early American "
            "novels about Native "
            "American life.\n\n"
            "He was a significant "
            "figure in antebellum "
            "North Carolina letters "
            "and politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "North Carolina Democratic Senator (1836–1840) and Supreme Court justice; Van Buren era Democrat during the Panic of 1837; also a novelist — 'Eoneguski, or The Cherokee Chief' (1839) was one of the earliest American novels about Native American life; significant figure in antebellum North Carolina letters and Jacksonian politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's Democratic tradition — the state's Jacksonian Democratic political culture, shaped by its large Scots-Irish and German farming population whose egalitarian instincts aligned with Jacksonian democracy — provided the political support for Strange's Senate career",
            "The Van Buren administration's political challenges — the Panic of 1837's economic devastation and the debate over the Independent Treasury as the Democratic response — created the major policy context for Strange's Senate tenure",
            "Strange's literary interests — his engagement with North Carolina's frontier history and Native American culture, informed by the recent Cherokee Removal that had expelled the Cherokee from North Carolina — inspired his historical novel about Cherokee life"
        ],
        "effects": [
            "His Senate service contributed North Carolina's Democratic perspective to the Van Buren era's economic policy debates — supporting the hard-money, Independent Treasury approach to the Panic of 1837",
            "His novel 'Eoneguski' (1839) contributed to the early American literary tradition of Native American subjects — one of the first serious fictional treatments of Cherokee life, written while the Trail of Tears was still living memory",
            "His judicial career contributed to North Carolina jurisprudence — the state court decisions that helped develop North Carolina's legal system during the antebellum era",
            "His career as both a senator and novelist illustrated the antebellum South's gentleman-scholar tradition — the lawyers and politicians who combined public service with literary or intellectual pursuits"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "North Carolina Senator 1836–1840"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Democratic senator during Van Buren's presidency"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Senator during the economic depression"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "North Carolina Democratic politician and jurist"},
            {"target": "cherokee-removal", "verb": "RESPONDS_TO", "note": "Novel about Cherokee life written during removal era"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 72 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
