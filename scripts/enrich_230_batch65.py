#!/usr/bin/env python3
"""
Batch 65 — 8 entities: Julián Álvarez, Mathias Sommerhielm, Michael Helding,
Peter Vivian Daniel, Reuel Williams, Robert Hodgson, Chauncey Fitch Cleveland,
David J. Baker
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

    ("julián-álvarez", {
        "summary": (
            "Julián Álvarez (1788–1843) was "
            "an Argentine lawyer and politician "
            "who played an important role "
            "in the early political history "
            "of the Río de la Plata region "
            "during the Wars of Independence "
            "and the turbulent decades of "
            "state-building that followed. "
            "As a member of the patriot "
            "cause from the early days "
            "of the May Revolution (1810), "
            "he contributed to the legal "
            "and political institutions "
            "of what would become Argentina, "
            "navigating the complex factional "
            "politics of Buenos Aires "
            "during the independence era.\n\n"
            "The Argentine independence "
            "process — from the May Revolution "
            "of 1810 through the formal "
            "Declaration of Independence "
            "in 1816 and the chaotic "
            "decades of civil conflict "
            "that followed — produced "
            "a generation of lawyers "
            "and political figures who "
            "had to construct republican "
            "institutions in the absence "
            "of any stable political "
            "tradition, with competing "
            "Federalist and Unitarian "
            "visions of what Argentina "
            "should become.\n\n"
            "Álvarez contributed to "
            "the legal and governmental "
            "culture of Buenos Aires "
            "during this formative period, "
            "working within the institutions "
            "of the emerging Argentine "
            "state.\n\n"
            "He died in 1843, before "
            "the eventual Argentine "
            "constitutional settlement "
            "of 1853."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Argentine lawyer and politician active from the May Revolution (1810); contributed to the legal and institutional development of Buenos Aires during the independence era and chaotic post-independence decades; part of the generation that tried to build Argentine republican institutions amid Federalist-Unitarian civil conflict.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The May Revolution of 1810 — Buenos Aires's revolutionary junta's rejection of Spanish colonial authority following Napoleon's invasion of Spain — created the political rupture that launched the independence process and mobilized Álvarez and his generation of patriot lawyers",
            "The Argentine independence movement's need for trained lawyers to staff the new republican institutions — the courts, legislative assemblies, and administrative bodies that the patriot government was building in competition with Spanish royalist forces — created the demand for Álvarez's legal expertise",
            "The Federalist-Unitarian conflict — the deep structural disagreement between those who wanted a strong central Buenos Aires government and those who wanted provincial autonomy — defined the political environment in which Álvarez's career developed"
        ],
        "effects": [
            "His legal and political service contributed to the institutional development of Buenos Aires during the critical independence and early post-independence period — helping staff the governmental and judicial institutions that the new Argentine state required",
            "His career contributed to the development of Argentine legal and political culture in the period before the 1853 Constitution — the formative decades when the basic patterns of Argentine political life were being established",
            "His participation in the May Revolution generation's political project illustrated the role of trained lawyers in Latin American independence — the legal professionals whose expertise in institutional design, constitutional theory, and administrative management was essential for state-building",
            "His death in 1843 placed him among the independence generation who did not live to see Argentina's eventual constitutional settlement — the lawyers and politicians who built the foundations but did not reach the stable republic that the 1853 Constitution created"
        ],
        "relationships": [
            {"target": "may-revolution-1810", "verb": "PARTICIPATES_IN", "note": "Part of the Argentine independence movement from its outset"},
            {"target": "buenos-aires", "verb": "SERVES_IN", "note": "Lawyer and politician in Buenos Aires"},
            {"target": "argentina", "verb": "CONTRIBUTES_TO", "note": "Part of the Argentine state-building generation"},
            {"target": "federalist-unitarian-conflict", "verb": "NAVIGATES", "note": "Worked within the Federalist-Unitarian political struggle"},
            {"target": "rio-de-la-plata", "verb": "PART_OF", "note": "Argentine independence-era political figure"}
        ]
    }),

    ("mathias-sommerhielm", {
        "summary": (
            "Mathias Sommerhielm (1769–1824) "
            "was a Norwegian jurist and "
            "statesman who served as Minister "
            "of Justice of Norway (1814–1822) "
            "— one of the most critical "
            "offices in the new Norwegian "
            "constitutional state created "
            "by the Eidsvoll Constitution "
            "of May 1814. As the first "
            "Minister of Justice, he helped "
            "build the judicial and legal "
            "administrative infrastructure "
            "of the newly constitutional "
            "Norwegian state during the "
            "most formative years of "
            "Norwegian self-governance.\n\n"
            "The Norwegian Constitution "
            "of 1814 — created in response "
            "to the dissolution of the "
            "Danish-Norwegian union following "
            "Napoleon's defeat and Denmark's "
            "cession of Norway to Sweden "
            "— was one of the most liberal "
            "constitutions in early "
            "nineteenth-century Europe. "
            "Despite the subsequent forced "
            "union with Sweden, Norway "
            "retained its constitution "
            "and Storting (parliament), "
            "and its national institutions "
            "— including the Ministry "
            "of Justice that Sommerhielm "
            "led — had genuine autonomy.\n\n"
            "His eight-year ministerial "
            "tenure (1814–1822) covered "
            "the entire critical first "
            "phase of Norwegian self-governance "
            "under the new constitutional "
            "order.\n\n"
            "He was among the most "
            "important architects of "
            "modern Norwegian governance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Norwegian Minister of Justice (1814–1822); helped build the judicial and legal administrative infrastructure of the newly constitutional Norwegian state; served through the entire critical first phase of Norwegian self-governance after the 1814 Eidsvoll Constitution; key architect of modern Norwegian governance.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — created at Eidsvoll in the wake of Napoleon's defeat and Denmark's cession of Norway to Sweden — established the constitutional framework that created the Ministry of Justice and other national institutions that Sommerhielm would lead",
            "Norway's forced union with Sweden (1814) despite the constitution — the Swedish conquest that compelled Norway to accept Swedish king while retaining its constitution — created the political reality within which Sommerhielm's ministerial career operated, maintaining Norwegian judicial autonomy within a Swedish-Norwegian union",
            "Norway's need for experienced jurists to build its new national institutions from scratch — the Eidsvoll Constitution had created a constitutional order that required trained legal administrators to staff its courts, draft its laws, and build its legal infrastructure — made Sommerhielm's appointment as Minister of Justice essential"
        ],
        "effects": [
            "His eight-year Ministry of Justice leadership built the foundational legal and judicial institutions of the Norwegian constitutional state — establishing the administrative patterns and legal infrastructure that Norway's governance rested on through the nineteenth century",
            "His ministry contributed to the development of Norwegian law as distinct from Danish colonial law — part of the broader Norwegian nation-building project of developing distinctively Norwegian institutions",
            "His tenure contributed to the stability of Norwegian governance during the most vulnerable phase of constitutional self-rule — maintaining effective governance during the years when the new institutions were most fragile and most dependent on capable leadership",
            "His career illustrated the crucial role of the first generation of Norwegian constitutional officeholders — the jurists and administrators who translated the Eidsvoll Constitution's ideals into functioning institutions"
        ],
        "relationships": [
            {"target": "norway", "verb": "SERVES_AS_MINISTER", "note": "First Norwegian Minister of Justice 1814–1822"},
            {"target": "norwegian-constitution-1814", "verb": "IMPLEMENTS", "note": "Built institutions under the Eidsvoll Constitution"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_DURING", "note": "Minister during the forced union with Sweden"},
            {"target": "norwegian-ministry-of-justice", "verb": "FOUNDS", "note": "First holder of the Justice Ministry office"},
            {"target": "storting", "verb": "WORKS_WITH", "note": "Part of Norwegian constitutional governance"}
        ]
    }),

    ("michael-helding", {
        "summary": (
            "Michael Helding (1506–1561) was "
            "a German Catholic theologian "
            "and bishop who played a "
            "significant role in the "
            "negotiations and controversies "
            "of the German Reformation era. "
            "As a Catholic participant in "
            "the Augsburg Interim (1548) "
            "— the temporary religious "
            "settlement that Emperor "
            "Charles V imposed on Germany "
            "after his military victory "
            "over the Protestant princes "
            "at the Battle of Mühlberg "
            "— Helding was one of the "
            "theologians who drafted "
            "the compromise formula that "
            "attempted to impose Catholic "
            "doctrine while making limited "
            "concessions to Protestant "
            "practice.\n\n"
            "Helding served as Bishop "
            "of Merseburg (1549–1561) "
            "and was known for his "
            "commitment to genuine "
            "Catholic reform — not "
            "the mechanical defense "
            "of abuses, but the "
            "authentic renewal of "
            "Catholic spirituality "
            "and theological education "
            "that the Council of "
            "Trent was beginning "
            "to articulate.\n\n"
            "His involvement in the "
            "Augsburg Interim and "
            "its successor the "
            "Leipzig Interim (1548) "
            "placed him at the center "
            "of the most intense "
            "theological-political "
            "negotiations of the "
            "Reformation's mid-century "
            "crisis in Germany.\n\n"
            "He was a genuine Catholic "
            "reformer in the Tridentine tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "German Catholic theologian and Bishop of Merseburg who co-drafted the Augsburg Interim (1548); central to the mid-century German Reformation crisis negotiations; committed Catholic reformer in the Tridentine tradition; worked at the intersection of imperial politics and religious settlement during the most intense phase of the Reformation conflict.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Emperor Charles V's military victory at Mühlberg (1547) — the decisive Schmalkaldic War battle that crushed the Protestant princes' military resistance — gave Charles the political leverage to impose the Augsburg Interim as a temporary settlement, creating the context for Helding's theological drafting role",
            "The Catholic reform movement's need for theologians who could engage seriously with Protestant critiques while maintaining Catholic doctrinal integrity — the Erasmian and Tridentine Catholic reformers who sought genuine renewal rather than mere polemical defense — provided the theological framework for Helding's irenical approach",
            "The German Empire's structural religious pluralism — the impossibility of simply imposing religious uniformity on a population deeply divided between Lutheranism and Catholicism — created the political necessity for compromise formulas like the Interims that Helding helped draft"
        ],
        "effects": [
            "His co-authorship of the Augsburg Interim — the attempted compromise religious settlement imposed after Mühlberg — contributed to one of the most controversial episodes of the Reformation era, a document that satisfied neither committed Catholics nor Lutherans and ultimately failed to resolve the religious division",
            "His bishop of Merseburg ministry contributed to the Catholic pastoral renewal in the German church — the diocesan reform that genuine Catholic reformers like Helding attempted to achieve alongside the political negotiations",
            "His Tridentine reformist approach contributed to the developing Catholic reform tradition that the Council of Trent was systematizing — the Catholic response to Protestantism that eventually produced the Counter-Reformation's Catholic renewal",
            "His participation in the failed Interims contributed to the eventual Peace of Augsburg (1555) — the settlement that acknowledged Lutheran Christianity's permanent legitimacy in Germany and ended the attempt to restore religious unity through imperial force"
        ],
        "relationships": [
            {"target": "augsburg-interim-1548", "verb": "DRAFTS", "note": "Catholic theologian who co-drafted the temporary religious settlement"},
            {"target": "bishop-of-merseburg", "verb": "SERVES_AS", "note": "Bishop of Merseburg 1549–1561"},
            {"target": "charles-v-holy-roman-emperor", "verb": "SERVES", "note": "Catholic theologian serving imperial religious policy"},
            {"target": "council-of-trent", "verb": "ALIGNS_WITH", "note": "Tridentine Catholic reformer"},
            {"target": "german-reformation", "verb": "NEGOTIATES", "note": "Catholic participant in Reformation-era religious negotiations"}
        ]
    }),

    ("peter-vivian-daniel", {
        "summary": (
            "Peter Vivian Daniel (1784–1860) "
            "was an American Democratic "
            "politician and jurist from "
            "Virginia who served as an "
            "Associate Justice of the "
            "U.S. Supreme Court (1841–1860) "
            "— appointed by President "
            "Martin Van Buren in one of "
            "the last acts of his "
            "administration. Daniel was "
            "one of the most rigid "
            "states'-rights advocates "
            "ever to sit on the "
            "Supreme Court — an "
            "uncompromising Jeffersonian "
            "who consistently opposed "
            "federal power, corporate "
            "privileges, and any "
            "interpretation of the "
            "Constitution that expanded "
            "national authority at "
            "the expense of the states.\n\n"
            "Daniel served on the "
            "Virginia Privy Council "
            "before his Supreme Court "
            "appointment — a position "
            "that reflected his deep "
            "roots in the Virginia "
            "Democratic-Republican "
            "political culture of "
            "strict construction and "
            "states' rights. He had "
            "been a close ally of "
            "Andrew Jackson and "
            "Martin Van Buren.\n\n"
            "His nineteen years on "
            "the Court coincided "
            "with the deepening "
            "sectional crisis over "
            "slavery — and Daniel "
            "became one of the "
            "most vocal defenders "
            "of Southern slave "
            "property rights, "
            "contributing extreme "
            "pro-slavery opinions "
            "in cases including "
            "Dred Scott (1857).\n\n"
            "He was the Court's "
            "most doctrinaire states'-rights justice."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Supreme Court Associate Justice (1841–1860); most doctrinaire states'-rights advocate on the antebellum Court; contributed extreme pro-slavery opinions including in Dred Scott (1857); close Jackson-Van Buren ally; embodied the Virginia strict construction tradition at the height of the slavery crisis.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's Jeffersonian strict construction tradition — the states'-rights political culture that had produced Jefferson's and Madison's Virginia and Kentucky Resolutions and that Daniel had imbibed through his long career in Virginia Democratic politics — formed the constitutional philosophy that he carried onto the Supreme Court",
            "President Van Buren's appointment strategy — seeking to place a loyal Jacksonian Democrat with strong states'-rights credentials on the Court in one of his final acts as president — created the appointment that gave Daniel his Court seat despite his extreme doctrinal positions",
            "The deepening sectional crisis over slavery — which intensified the Southern political demand for constitutional protections of slave property and states' rights against federal interference — created the political environment in which Daniel's extreme positions were not just tolerated but celebrated in the South"
        ],
        "effects": [
            "His nineteen-year Court tenure contributed some of the most extreme states'-rights and pro-slavery constitutional jurisprudence in American history — opinions that went further even than his more famous colleague Roger Taney in defending Southern constitutional positions",
            "His Dred Scott concurrence (1857) — going further than Taney's majority opinion by arguing that Congress had never had power to regulate slavery in territories — contributed to the most consequential and disastrous Supreme Court decision in American history",
            "His consistent opposition to corporate privileges and national bank power — reflecting his Jeffersonian anti-monopoly philosophy — placed him in a small but doctrinally important minority that challenged the Marshall and Taney Courts' generally pro-corporate jurisprudence",
            "His career illustrated the increasing dominance of pro-slavery states'-rights jurisprudence on the antebellum Supreme Court — the judicial philosophy that eventually produced Dred Scott and contributed to the conditions that made the Civil War inevitable"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1841–1860"},
            {"target": "dred-scott-case", "verb": "CONTRIBUTES_OPINION", "note": "Extreme pro-slavery concurrence in 1857"},
            {"target": "martin-van-buren", "verb": "APPOINTED_BY", "note": "Van Buren's final Supreme Court appointment"},
            {"target": "virginia-states-rights-tradition", "verb": "EMBODIES", "note": "Most doctrinaire states'-rights justice on the Court"},
            {"target": "slavery-constitutional-law", "verb": "DEFENDS", "note": "Consistent defender of slave property rights"}
        ]
    }),

    ("reuel-williams", {
        "summary": (
            "Reuel Williams (1783–1862) was "
            "an American Democratic politician "
            "and lawyer from Maine who served "
            "as a U.S. Senator (1837–1843) "
            "during the Van Buren administration "
            "and the early years of the "
            "Whig opposition. One of Maine's "
            "most prominent lawyers, he "
            "had a distinguished legal "
            "career before his Senate "
            "service and was known as "
            "one of the most capable "
            "attorneys in New England.\n\n"
            "His Senate tenure coincided "
            "with the Panic of 1837 "
            "— the severe economic "
            "depression triggered by "
            "Jackson's Specie Circular "
            "and the collapse of the "
            "land speculation bubble "
            "that had been inflated "
            "by the Second Bank's "
            "destruction. The panic "
            "devastated Van Buren's "
            "presidency and produced "
            "the Whig victory of 1840 "
            "that brought William "
            "Henry Harrison to power.\n\n"
            "Williams also served "
            "as a trustee of "
            "Bowdoin College — "
            "the distinguished "
            "Maine liberal arts "
            "institution that "
            "counted Nathaniel "
            "Hawthorne and "
            "Henry Wadsworth "
            "Longfellow among "
            "its alumni — reflecting "
            "his prominence in "
            "Maine intellectual "
            "and civic life.\n\n"
            "His legal career "
            "made him one of "
            "antebellum Maine's "
            "most distinguished citizens."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maine Democratic Senator (1837–1843) during the Panic of 1837 and Van Buren administration; one of New England's most distinguished antebellum lawyers; Bowdoin College trustee; served through the economic crisis that produced the Whig revolution of 1840.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maine's Democratic political tradition — the state's farmers, workers, and maritime communities' alignment with Jacksonian Democratic politics — provided the political constituency for Williams's Senate election",
            "The Panic of 1837 — the severe economic depression triggered by the destruction of the Second Bank, the Specie Circular's deflationary shock, and the collapse of the credit bubble — defined the major challenge of Williams's Senate tenure as he tried to defend Van Buren's economic policies",
            "Maine's legal community's prominence in state politics — the pattern by which successful lawyers translated their professional reputations into political careers — created the pathway through which Williams moved from legal practice to Senate service"
        ],
        "effects": [
            "His Senate service contributed Maine's Democratic vote to the critical debates of the Van Buren years — the Independent Treasury debates, the Panic's policy response, and the Jacksonian Democrats' defense of hard-money financial policy",
            "His Bowdoin College trusteeship contributed to the development of one of New England's most distinguished liberal arts institutions — linking Maine's political leadership to its educational institutions",
            "His legal career contributed to the development of Maine's legal tradition and professional culture — building the bar and legal institutions of a new state that had achieved independence only in 1820",
            "His career illustrated the close connection between legal distinction and political leadership in early Maine — the pattern by which the state's most capable lawyers were drawn into political service as senators, judges, and governors"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maine Senator 1837–1843"},
            {"target": "panic-of-1837", "verb": "GOVERNS_DURING", "note": "Senator during the economic depression"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Democratic senator during Van Buren's presidency"},
            {"target": "bowdoin-college", "verb": "SERVES_AS_TRUSTEE", "note": "Trustee of the distinguished Maine college"},
            {"target": "maine", "verb": "REPRESENTS", "note": "Maine Democratic senator and prominent lawyer"}
        ]
    }),

    ("robert-hodgson", {
        "summary": (
            "Robert Hodgson (1798–1880) was "
            "a British colonial official "
            "who served as the Colonial "
            "Secretary of the Bahamas "
            "and subsequently as Governor "
            "of Dominica (1865–1869) "
            "and Acting Governor of "
            "various British Caribbean "
            "territories during the "
            "mid-nineteenth century. "
            "His career represented "
            "the professional colonial "
            "civil service that Britain "
            "developed to administer "
            "its Caribbean possessions "
            "through the transformative "
            "decades after emancipation "
            "(1834/1838) — when the "
            "plantation societies of "
            "the British West Indies "
            "had to be rebuilt on "
            "a free-labor basis.\n\n"
            "The post-emancipation "
            "Caribbean was one of the "
            "most challenging administrative "
            "environments in the British "
            "empire — the formerly enslaved "
            "population demanding land "
            "and autonomy, the planters "
            "seeking to recreate "
            "plantation labor through "
            "indenture and coercion, "
            "and the colonial government "
            "trying to mediate between "
            "these competing interests "
            "while maintaining order "
            "and economic productivity.\n\n"
            "His Dominica governorship "
            "came during the period "
            "of crown colony governance "
            "— the post-1865 centralization "
            "following the Morant Bay "
            "Rebellion in Jamaica.\n\n"
            "He represented the professional "
            "British colonial administrator."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "British colonial official and Governor of Dominica (1865–1869); career in post-emancipation British Caribbean administration; served during the Morant Bay Rebellion's aftermath and the shift to crown colony governance; represented the professional colonial civil service managing the difficult transition from slavery to free labor.",
            "significanceCategory": "local"
        },
        "causes": [
            "British emancipation (1834/1838) — the abolition of slavery throughout the British Empire that fundamentally transformed the Caribbean colonies — created the massive administrative challenges of post-emancipation governance that colonial officials like Hodgson had to manage",
            "The Morant Bay Rebellion (1865) in Jamaica — the uprising that led to Governor Eyre's brutal suppression and the subsequent shift to direct crown colony governance across the British Caribbean — created the post-rebellion political context for Hodgson's Dominica governorship",
            "The development of the British colonial civil service as a professional career — the emergence of a cadre of trained colonial administrators who moved between postings across the empire — created the institutional framework for Hodgson's career across multiple Caribbean territories"
        ],
        "effects": [
            "His Dominica governorship managed one of the smaller British Caribbean colonies during the most difficult phase of post-emancipation adjustment — maintaining colonial order while managing the competing pressures of free labor transition",
            "His career contributed to the development of British Caribbean colonial administration — the governing practices, legal frameworks, and institutional routines that managed the post-emancipation societies",
            "His service during the crown colony period contributed to the centralization of British Caribbean governance — the shift away from representative assemblies toward direct crown control that followed Morant Bay",
            "His career illustrated the professional colonial civil service's management of Britain's most challenging post-emancipation territories — the small Caribbean islands whose plantation economies had been fundamentally disrupted by emancipation"
        ],
        "relationships": [
            {"target": "dominica", "verb": "GOVERNS", "note": "Governor of Dominica 1865–1869"},
            {"target": "british-caribbean", "verb": "ADMINISTERS", "note": "Colonial official across multiple Caribbean territories"},
            {"target": "british-emancipation-1834", "verb": "ADMINISTERS_AFTER", "note": "Career in post-emancipation British Caribbean"},
            {"target": "morant-bay-rebellion", "verb": "SERVES_AFTER", "note": "Governor during post-Morant Bay crown colony period"},
            {"target": "british-colonial-service", "verb": "SERVES_IN", "note": "Professional British colonial administrator"}
        ]
    }),

    ("chauncey-fitch-cleveland", {
        "summary": (
            "Chauncey Fitch Cleveland (1799–1887) "
            "was an American Democratic "
            "politician from Connecticut who "
            "served as Governor of Connecticut "
            "(1842–1844) and as a U.S. "
            "Representative (1849–1853). "
            "His governorship came during "
            "the years of Whig national "
            "dominance — the Tyler administration's "
            "political chaos following "
            "William Henry Harrison's death "
            "and the complex political "
            "situation produced by Tyler's "
            "break with the Whig Party "
            "— while his congressional "
            "service came during the "
            "critical years of the "
            "Mexican Cession debates "
            "and the Compromise of 1850.\n\n"
            "Connecticut was politically "
            "competitive in this era "
            "— a state where Democrats "
            "and Whigs genuinely contested "
            "elections, and where "
            "Cleveland's two gubernatorial "
            "terms represented the "
            "Democratic Party's ability "
            "to win even in a "
            "commercially oriented "
            "New England state.\n\n"
            "His congressional service "
            "(1849–1853) coincided with "
            "the Compromise of 1850's "
            "passage — the complex "
            "set of measures that "
            "temporarily resolved "
            "the sectional crisis "
            "over California statehood "
            "and slavery in the "
            "Mexican Cession territories.\n\n"
            "He was a long-lived figure "
            "who survived to 1887."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut Democratic Governor (1842–1844) and Congressman (1849–1853); served during Tyler's political chaos and then during the Compromise of 1850; represented Democratic competitiveness in commercially oriented Connecticut; long-lived political figure (1799–1887) spanning antebellum to post-Civil War era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's competitive two-party politics — the state where Democrats could win despite the commercial elite's Whig preferences — created the political opportunity for Cleveland's gubernatorial victories",
            "The Tyler administration's political chaos (1841–1845) — President Tyler's break with the Whig Party after vetoing Whig banking legislation, which left him without a party and the Democrats able to exploit Whig disunity — created favorable conditions for Democratic gubernatorial victories like Cleveland's in 1842–1844",
            "The Mexican Cession and Compromise of 1850 debates — the congressional crisis over what to do with the territories acquired from Mexico, resolved by Clay's compromise that admitted California as free, organized other territories without slavery restrictions, and strengthened the Fugitive Slave Law — defined the major challenge of Cleveland's congressional service"
        ],
        "effects": [
            "His governorship managed Connecticut's affairs during the Tyler administration's political chaos — maintaining Democratic governance in a competitive New England state during the unusual circumstances of a president without a party",
            "His congressional service contributed Connecticut's Democratic vote to the Compromise of 1850 debates — representing a free-state perspective from a state that had commercial interests in maintaining sectional harmony",
            "His career illustrated the Democratic Party's ability to compete successfully in commercially oriented New England — demonstrating that Jacksonian populism's appeal extended beyond the agrarian South and West to manufacturing and commercial states like Connecticut",
            "His long life (1799–1887) made him a witness to the full transformation of American politics from Jacksonian Democracy through the Civil War, Reconstruction, and the Gilded Age"
        ],
        "relationships": [
            {"target": "connecticut", "verb": "GOVERNS", "note": "Governor of Connecticut 1842–1844"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1849–1853"},
            {"target": "compromise-of-1850", "verb": "VOTES_ON", "note": "Congressman during the critical compromise debates"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Connecticut Democratic politician"},
            {"target": "john-tyler", "verb": "GOVERNS_DURING", "note": "Governor during Tyler's political chaos"}
        ]
    }),

    ("david-j-baker", {
        "summary": (
            "David Jewett Baker (1792–1869) "
            "was an American Democratic "
            "politician from Illinois who "
            "served briefly as a U.S. "
            "Senator (1830) — filling a "
            "vacancy for less than two "
            "months — and subsequently "
            "had a long career as a "
            "federal district judge "
            "in Illinois (1839–1869). "
            "His brief Senate tenure "
            "was significant mainly as "
            "a biographical footnote, "
            "but his thirty-year federal "
            "judgeship made him one "
            "of the most important "
            "figures in the development "
            "of Illinois federal law.\n\n"
            "Illinois in the 1830s "
            "was one of the rapidly "
            "growing frontier states "
            "of the American West — "
            "settled primarily by "
            "migrants from the "
            "Ohio Valley and Upper "
            "South, with a political "
            "culture that was "
            "strongly Jacksonian "
            "Democratic and that "
            "produced Abraham Lincoln's "
            "early political career "
            "in opposition to the "
            "Democratic establishment.\n\n"
            "Baker's long district "
            "court tenure (1839–1869) "
            "placed him on the "
            "federal bench during "
            "the most consequential "
            "decades of Illinois "
            "history — from the "
            "frontier state's rapid "
            "development through "
            "the Civil War and its "
            "aftermath.\n\n"
            "He was a foundational "
            "figure in Illinois "
            "federal jurisprudence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Illinois Democratic Senator (1830, briefly) and federal district judge (1839–1869); thirty-year judgeship made him foundational to Illinois federal jurisprudence; served through the frontier state's development, the Civil War, and Reconstruction; part of the Jacksonian Democratic establishment that produced early Illinois political culture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Illinois's rapid frontier development — the state's explosive growth in the 1820s–1830s as migrants from the Ohio Valley and Upper South created a rapidly developing agricultural and commercial economy — created the expanding political and legal institutions that required Baker's service",
            "The Jacksonian Democratic political culture of frontier Illinois — the state's strongly Democratic population of Southern-descended farmers who supported Jackson's populism and anti-aristocratic rhetoric — created the political environment for Baker's brief Senate appointment",
            "The federal district court system's establishment and development in the growing western states — the expansion of federal judicial infrastructure to serve the rapidly growing population of the old Northwest — created the institutional framework for Baker's thirty-year judgeship"
        ],
        "effects": [
            "His thirty-year federal district judgeship (1839–1869) contributed foundational jurisprudence to Illinois's federal legal tradition — establishing legal precedents and judicial practices that shaped the state's federal law through its most transformative decades",
            "His court managed Illinois's federal legal affairs through the Civil War — a period when federal courts in the border and western states dealt with unprecedented legal questions about loyalty, treason, confiscation, and military jurisdiction",
            "His judicial career contributed to the development of federal district court institutions in the American West — part of the pattern by which the federal judiciary extended its reach into the rapidly developing frontier states",
            "His career illustrated the dual path of antebellum Illinois lawyers — the brief political careers and longer judicial tenures that characterized many of the state's most important legal figures during its formative decades"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Illinois Senator briefly in 1830"},
            {"target": "us-federal-district-court-illinois", "verb": "SERVES_AS_JUDGE", "note": "Federal judge 1839–1869"},
            {"target": "illinois", "verb": "SERVES", "note": "Foundational figure in Illinois federal law"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat in frontier Illinois"},
            {"target": "civil-war", "verb": "JUDGES_DURING", "note": "Federal judge through the Civil War era"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 65 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
