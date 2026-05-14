#!/usr/bin/env python3
"""
Batch 71 — 8 entities: John Watts Jr, Joseph R. Underwood, Juan Martínez de Rozas,
John McKinley, Chester Ashley, Félix de Mûelenaere, Johann Jacob Schütz, Jonathan Mason
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

    ("john-watts-jr", {
        "summary": (
            "John Watts Jr. (1749–1836) "
            "was an American Federalist "
            "politician from New York who "
            "served in the U.S. House of "
            "Representatives (1793–1795) "
            "and as a judge of the New "
            "York Supreme Court. A member "
            "of a prominent colonial "
            "New York family — his father "
            "John Watts Sr. had been "
            "a loyalist during the Revolution "
            "— Watts Jr. navigated "
            "the difficult transition "
            "from colonial elite to "
            "republican citizen, "
            "aligning with the Federalist "
            "tradition that best "
            "preserved the social "
            "world of New York's "
            "commercial establishment.\n\n"
            "His brief congressional "
            "service coincided with "
            "the establishment of "
            "the Jay Treaty negotiations "
            "— his fellow New Yorker "
            "John Jay was negotiating "
            "the treaty with Britain "
            "that would provoke intense "
            "controversy — and with "
            "Hamilton's Treasury "
            "system at its height.\n\n"
            "New York's Federalist "
            "elite — the merchants, "
            "lawyers, and landowners "
            "who had supported the "
            "Constitution's ratification "
            "at Poughkeepsie in 1788 "
            "— was the social world "
            "within which Watts moved.\n\n"
            "His long life (1749–1836) "
            "spanned from colonial "
            "New York to the Jacksonian era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New York Federalist Congressman (1793–1795) and Supreme Court judge; son of loyalist John Watts Sr.; navigated colonial elite to republican citizen transition; served during Jay Treaty negotiations; part of New York's Federalist commercial establishment; extraordinarily long life (1749–1836) spanning colonial era to Jacksonian period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Federalist commercial elite — the merchants, lawyers, and landowners whose commercial interests aligned with Hamilton's financial system and whose social world was being preserved through Federalist governance — created the political constituency for Watts's career",
            "The Watts family's navigation of Revolutionary loyalty — the family's transition from loyalism (his father's position) to republican citizenship (his own) required a careful alignment with the most conservative revolutionary faction — the Federalists",
            "The Jay Treaty's political context — John Jay's negotiation and the controversy it produced — created the major foreign policy issue that dominated Watts's brief congressional tenure"
        ],
        "effects": [
            "His House service contributed New York's Federalist perspective to the formative years of the new government — supporting Hamilton's economic program and the cautious, commercially-oriented foreign policy of the Washington administration",
            "His judicial career on the New York Supreme Court contributed to the development of New York's Federalist legal tradition — the common law and commercial jurisprudence of America's commercial center",
            "His career illustrated the successful navigation of the loyalist-to-republican transition — the social and political adjustment that children of loyalists made to become respected citizens of the new republic",
            "His extraordinarily long life made him one of the last living members of colonial New York's elite — carrying the memory of British New York through the Revolution, the Federalist era, and into the Jacksonian transformation"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1793–1795"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New York Federalist in Hamilton's tradition"},
            {"target": "new-york-supreme-court", "verb": "SERVES_ON", "note": "New York Supreme Court judge"},
            {"target": "jay-treaty", "verb": "SERVES_DURING", "note": "Congressman during the Jay Treaty negotiations"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "Part of New York's colonial-era commercial elite"}
        ]
    }),

    ("joseph-r-underwood", {
        "summary": (
            "Joseph Rogers Underwood "
            "(1791–876) was an American "
            "Whig politician from Kentucky "
            "who served in the U.S. House "
            "of Representatives (1835–1843) "
            "and the U.S. Senate (1847–1853). "
            "A prominent Kentucky Whig "
            "in the Clay tradition, "
            "Underwood was among the "
            "most active congressional "
            "opponents of the Mexican-American "
            "War — arguing that Polk's "
            "war was unconstitutional "
            "aggression against a "
            "peaceful neighbor and "
            "that the territory's "
            "acquisition would only "
            "intensify the slavery "
            "extension controversy.\n\n"
            "Underwood's opposition "
            "to the war illustrated "
            "the Whig foreign policy "
            "tradition — the party's "
            "skepticism about military "
            "adventure, its concern "
            "for constitutional "
            "process in war declarations, "
            "and its worry that "
            "territorial expansion "
            "would reignite the "
            "slavery sectional crisis.\n\n"
            "His Senate service "
            "coincided with the "
            "Compromise of 1850 "
            "— the complex bargain "
            "that temporarily settled "
            "the slavery-extension "
            "question raised by "
            "the Mexican war's "
            "territorial conquests.\n\n"
            "He was a Kentucky "
            "constitutional lawyer "
            "of the first rank."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Kentucky Whig Congressman (1835–1843) and Senator (1847–1853); prominent Clay Whig opponent of the Mexican-American War; warned that territorial expansion would intensify slavery sectional crisis; served through the Compromise of 1850; representative of the Whig constitutional foreign policy tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry Clay's Whig tradition in Kentucky — the state's identification with the American System, constitutional caution in foreign policy, and skepticism about territorial expansion through war — created the political identity for Underwood's congressional career",
            "The Mexican-American War controversy (1846–1848) — Polk's decision to send troops into disputed territory between the Nueces and Rio Grande rivers and the subsequent declaration of war — created the major foreign policy controversy that Underwood publicly opposed",
            "The Compromise of 1850's necessity — the crisis created by the vast territorial acquisitions from Mexico that required a new political settlement on slavery's extension — created the senatorial challenge that defined Underwood's Senate career"
        ],
        "effects": [
            "His congressional opposition to the Mexican-American War contributed to the significant Whig dissent voice — the 'Spot Resolutions' tradition that Abraham Lincoln also joined — that questioned the war's constitutionality and circumstances",
            "His Senate service during the Compromise of 1850 contributed to the compromise's elaborate passage — the series of measures that temporarily defused the territorial slavery crisis",
            "His career contributed to the Kentucky Whig tradition that Lincoln drew on — the political culture of constitutional caution, antislavery sentiment, and Unionism that Kentucky's Clay heritage produced",
            "His opposition to the war proved prescient — the territorial acquisitions did intensify the sectional crisis exactly as Whig opponents had warned, contributing to the Kansas-Nebraska Act crisis just two years after Underwood left the Senate"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Kentucky Congressman 1835–1843"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Kentucky Senator 1847–1853"},
            {"target": "mexican-american-war", "verb": "OPPOSES", "note": "Whig opponent of the unconstitutional war argument"},
            {"target": "henry-clay", "verb": "FOLLOWS", "note": "Kentucky Whig in the Clay tradition"},
            {"target": "compromise-of-1850", "verb": "SERVES_DURING", "note": "Senator through the compromise settlement"}
        ]
    }),

    ("juan-martínez-de-rozas", {
        "summary": (
            "Juan Martínez de Rozas "
            "(1759–1813) was a Chilean "
            "lawyer, intellectual, and "
            "independence leader who "
            "was one of the principal "
            "architects of Chile's "
            "first governing junta "
            "after the September 18, "
            "1810 revolution — the "
            "date now celebrated as "
            "Chilean Independence Day. "
            "As the most influential "
            "figure in the Concepción "
            "region and a dominant "
            "voice in the first "
            "national congress, "
            "Martínez de Rozas "
            "was a radical for "
            "complete independence "
            "who pushed against "
            "moderates who merely "
            "wanted autonomy within "
            "the Spanish empire.\n\n"
            "Martínez de Rozas had "
            "been educated at the "
            "University of San Felipe "
            "in Santiago and at "
            "Córdoba in Argentina "
            "— one of the creole "
            "intellectuals who "
            "absorbed Enlightenment "
            "political philosophy "
            "and applied it to "
            "the case for Spanish "
            "American independence.\n\n"
            "Political conflicts "
            "with more conservative "
            "independence leaders "
            "led to his exile "
            "to Mendoza, where "
            "he died in 1813 — "
            "before Chilean independence "
            "was finally secured.\n\n"
            "He is venerated as "
            "one of Chile's founding fathers."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Chilean founding father and architect of the September 18, 1810 independence junta; radical independence advocate pushing beyond mere autonomy; dominant Concepción leader and national congress figure; educated in Enlightenment political philosophy; died in exile in Mendoza (1813) before independence was secured; venerated as one of Chile's founding patriots.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's invasion of Spain (1808) and the resulting collapse of royal authority — the political crisis that created the space for Spanish American self-governance movements as the mother country's government became unable to maintain its colonial control — created the immediate opportunity for Martínez de Rozas's independence activism",
            "The Enlightenment's political philosophy — the ideas of natural rights, popular sovereignty, and constitutional government that educated creoles like Martínez de Rozas had absorbed from European intellectual sources — provided the theoretical framework for independence",
            "Chile's creole intellectual and commercial elite's growing frustration with Spanish mercantile restrictions and political exclusion — the economic and political grievances that drove the independence movement — created the constituency for Martínez de Rozas's radical independence position"
        ],
        "effects": [
            "His role in establishing Chile's first governing junta (September 18, 1810) created the institutional foundation for Chilean self-governance — the initial political structure that, despite its nominally royalist cover, began the practical process of independence",
            "His advocacy for complete independence — pushing beyond the moderate autonomy position — contributed to radicalizing the independence movement and pushing it toward the full break from Spain that eventually produced the Chilean republic",
            "His political conflicts and exile illustrated the tensions within independence movements between radical and moderate factions — the internal divisions that plagued Spanish American independence struggles and often determined whether the moderates or radicals would shape the new states",
            "His death in exile before Chilean independence was secured made him one of independence's many martyrs — the founding generation who paid for their patriotism with exile or death but whose contributions shaped the nations they helped create"
        ],
        "relationships": [
            {"target": "chile", "verb": "FOUNDS_JUNTA_OF", "note": "Principal architect of Chile's September 18, 1810 junta"},
            {"target": "chilean-independence", "verb": "ADVOCATES_FOR", "note": "Radical for complete independence from Spain"},
            {"target": "first-national-junta-chile", "verb": "LEADS", "note": "Dominant figure in the first governing junta"},
            {"target": "latin-american-independence", "verb": "PARTICIPATES_IN", "note": "Part of the Spanish American independence movement"},
            {"target": "enlightenment", "verb": "APPLIES_IDEAS_OF", "note": "Applied Enlightenment philosophy to independence cause"}
        ]
    }),

    ("john-mckinley", {
        "summary": (
            "John McKinley (1780–1852) "
            "was an American Democratic "
            "politician and jurist from "
            "Alabama who served in the "
            "U.S. Senate (1826–1831 and "
            "1837), the U.S. House "
            "(1833–1835), and as an "
            "Associate Justice of the "
            "U.S. Supreme Court (1838–1852). "
            "Appointed to the Supreme "
            "Court by Martin Van Buren, "
            "McKinley served during "
            "the Taney Court's critical "
            "decade — the period that "
            "saw the Court move from "
            "Marshall's nationalism "
            "to Taney's states'-rights "
            "jurisprudence that would "
            "culminate in the Dred Scott "
            "decision (1857).\n\n"
            "As an Alabama Democrat, "
            "McKinley represented "
            "the Deep South's "
            "plantation economy "
            "perspective — a "
            "states'-rights, "
            "slavery-protecting "
            "constitutionalism "
            "that Taney's Court "
            "increasingly embodied.\n\n"
            "Alabama was one of "
            "the newer cotton "
            "states — admitted "
            "to the Union in "
            "1819 — and its "
            "explosive growth "
            "made it one of "
            "the most dynamic "
            "and politically "
            "significant states "
            "of the antebellum "
            "Deep South.\n\n"
            "He died in office "
            "in 1852, five years "
            "before Dred Scott."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Alabama Democratic Senator (1826–1831, 1837) and Congressman (1833–1835), and Supreme Court Justice (1838–1852); Van Buren appointment to the Taney Court; served during the transition to states'-rights jurisprudence; represented the Deep South cotton-state perspective; died in 1852 five years before the Dred Scott decision he helped shape the Court toward.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Alabama's cotton boom and Deep South political development — the state's explosive growth as a cotton economy after 1819 and its emergence as one of the most politically significant Deep South states — created the political environment for McKinley's Alabama Democratic career",
            "Van Buren's Supreme Court appointment strategy — selecting a Jacksonian Democrat from the Deep South to continue the Taney Court's states'-rights jurisprudence — created the appointment that elevated McKinley from Alabama politics to national judicial significance",
            "The Taney Court's constitutional program — the Democratic majority's effort to shift the Court from Marshall's nationalism toward states'-rights jurisprudence more protective of Southern interests — created the judicial philosophy that McKinley embodied"
        ],
        "effects": [
            "His Supreme Court service contributed fourteen years of Deep South Democratic jurisprudence to the Taney Court — votes that moved the Court steadily toward the states'-rights, slavery-protecting constitutionalism of the Dred Scott era",
            "His combined Senate, House, and Supreme Court career gave Alabama a prominent national voice across all three branches — a significant achievement for a state that had been organized as a territory only in 1817",
            "His death in 1852 — before the Kansas-Nebraska Act and Dred Scott — placed him among the Taney Court members who helped lay the constitutional groundwork for those decisions without living to see their results",
            "His career contributed to the development of Alabama's political identity — the Deep South cotton-state combination of Jacksonian Democracy, states'-rights constitutionalism, and slavery protection that characterized Alabama's antebellum political culture"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1838–1852"},
            {"target": "martin-van-buren", "verb": "APPOINTED_BY", "note": "Van Buren's Supreme Court appointment"},
            {"target": "taney-court", "verb": "SERVES_ON", "note": "Part of the Taney Court's states'-rights jurisprudence"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Alabama Senator 1826–1831 and 1837"},
            {"target": "alabama", "verb": "REPRESENTS", "note": "Deep South cotton-state Democratic politician"}
        ]
    }),

    ("chester-ashley", {
        "summary": (
            "Chester Ashley (1790–1848) "
            "was an American Democratic "
            "politician from Arkansas "
            "who served as a U.S. Senator "
            "(1844–1848) — dying in "
            "office during the critical "
            "final year of the Mexican-American "
            "War. One of the political "
            "founders of Arkansas, "
            "Ashley had been instrumental "
            "in the territory's development "
            "and was one of the "
            "most influential figures "
            "in early Arkansas Democratic "
            "politics.\n\n"
            "Arkansas was the "
            "most recently admitted "
            "southern state (1836) "
            "— admitted as a slave "
            "state paired with "
            "Michigan's admission "
            "as a free state to "
            "maintain the sectional "
            "balance — and its "
            "political institutions "
            "were still being built "
            "during Ashley's "
            "senatorial tenure.\n\n"
            "His Senate service "
            "during the Polk administration "
            "coincided with the "
            "Oregon boundary settlement "
            "(1846) and the "
            "Mexican-American War's "
            "progression — the "
            "two great territorial "
            "expansions that defined "
            "Manifest Destiny's "
            "culminating phase.\n\n"
            "He died in Washington "
            "in 1848, "
            "during the Treaty of "
            "Guadalupe Hidalgo's ratification."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Arkansas Democratic Senator (1844–1848); one of Arkansas's political founders from its first decade of statehood; died in office during the Mexican-American War; served during the Oregon boundary settlement and the war's progression; significant figure in early Arkansas Democratic institution-building.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Arkansas's political founding and territorial development — the organization of the Arkansas Territory (1819) and its admission as a state (1836) created the political institutions and frontier society within which Ashley's career developed",
            "The slave state-free state pairing requirement — Arkansas's admission as the slave state paired with Michigan's admission as the free state to maintain Senate sectional balance — created the specific political context of Arkansas statehood that Ashley helped manage",
            "Manifest Destiny and Jacksonian expansionism — the political ideology that drove Democratic support for continental expansion through Oregon boundary settlement, Texas annexation, and the Mexican war — created the political context for Ashley's Senate tenure"
        ],
        "effects": [
            "His Senate service contributed Arkansas's Democratic vote to the Polk era's great expansionist decisions — the Oregon boundary settlement and the Mexican-American War that doubled the country's territory",
            "His role in Arkansas's political founding contributed to the development of a slave state whose political culture would eventually make it one of the Confederate states in the Civil War",
            "His death in 1848 during the Treaty of Guadalupe Hidalgo's ratification placed him among the senators who saw American territorial expansion reach its continental climax without living to manage the sectional crisis it intensified",
            "His career contributed to the establishment of Arkansas's Democratic political tradition — the Jacksonian Democracy that would dominate the state's politics through the antebellum era and, after Reconstruction, into the twentieth century"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Arkansas Senator 1844–1848"},
            {"target": "arkansas", "verb": "HELPS_FOUND", "note": "One of Arkansas's political founders from statehood"},
            {"target": "mexican-american-war", "verb": "SERVES_DURING", "note": "Senator during the war's progression"},
            {"target": "james-k-polk", "verb": "SUPPORTS", "note": "Democratic senator during Polk's presidency"},
            {"target": "manifest-destiny", "verb": "SUPPORTS", "note": "Arkansas Democrat supporting continental expansion"}
        ]
    }),

    ("félix-de-mûelenaere", {
        "summary": (
            "Félix de Mûelenaere (1793–1862) "
            "was a Belgian Catholic "
            "politician who served as "
            "Prime Minister of Belgium "
            "(1831–1832) and as Foreign "
            "Minister during the critical "
            "period of Belgian independence "
            "consolidation. He was "
            "one of the key architects "
            "of the newly independent "
            "Belgian state — Belgium "
            "having declared independence "
            "from the Netherlands "
            "in October 1830 following "
            "the Brussels revolution "
            "— and his diplomatic "
            "work secured international "
            "recognition for the "
            "new kingdom.\n\n"
            "As Foreign Minister, "
            "de Mûelenaere navigated "
            "the complex diplomacy "
            "of the London Conference "
            "(1830–1831) — the "
            "great powers' negotiations "
            "that produced the "
            "Treaty of London (1831) "
            "guaranteeing Belgian "
            "neutrality and sovereignty "
            "— a guarantee that would "
            "be violated by Germany "
            "in 1914 and trigger "
            "Britain's entry into "
            "the First World War.\n\n"
            "De Mûelenaere represented "
            "the Catholic conservative "
            "wing of Belgium's "
            "union of Catholics "
            "and Liberals that "
            "had achieved independence "
            "together in 1830.\n\n"
            "He was a founding "
            "figure of the Belgian state."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Belgian Prime Minister (1831–1832) and Foreign Minister during independence consolidation; key architect of the newly independent Belgian state; navigated the London Conference that produced Belgian neutrality guarantee (1831) — the guarantee violated by Germany in 1914 that triggered WWI; founding figure of modern Belgium.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Belgian Revolution (August–October 1830) — the Brussels uprising against Dutch rule that established Belgian independence — created the new state whose governance and international recognition de Mûelenaere had to manage",
            "The Concert of Europe's management of the Belgian Question — the great powers' determination to manage Belgian independence through diplomacy rather than allowing it to destabilize European order — created the London Conference context for de Mûelenaere's foreign ministerial work",
            "Belgium's unique religious-political alliance — the 'Unionism' of Catholics and Liberals who had cooperated to achieve independence despite their ideological differences — provided the political coalition that the early Belgian state navigated"
        ],
        "effects": [
            "His role in the London Conference diplomacy contributed to securing the Treaty of London (1831) — the great-power guarantee of Belgian neutrality that became one of the foundational documents of European international law and would have world-historical consequences in 1914",
            "His Prime Ministership contributed to establishing the foundational institutions of the Belgian state — the parliamentary monarchy whose constitution became one of the most admired liberal constitutions in 19th-century Europe",
            "His Catholic conservative leadership contributed to the development of Belgian political Catholicism — one of the major forces in Belgian politics that would organize into a major party and compete with Liberalism throughout the 19th century",
            "His diplomatic achievement in securing international recognition contributed to Belgium's survival as an independent state — by preventing Dutch reintegration and securing the great-power commitment that protected Belgian sovereignty"
        ],
        "relationships": [
            {"target": "belgium", "verb": "GOVERNS", "note": "Prime Minister 1831–1832 during independence consolidation"},
            {"target": "belgian-independence-1830", "verb": "CONSOLIDATES", "note": "Key architect of the new Belgian state"},
            {"target": "treaty-of-london-1831", "verb": "NEGOTIATES", "note": "Foreign Minister during the neutrality guarantee"},
            {"target": "london-conference-1830", "verb": "PARTICIPATES_IN", "note": "Belgian diplomat at the great powers' conference"},
            {"target": "belgian-catholicism", "verb": "REPRESENTS", "note": "Catholic conservative in Belgium's Union government"}
        ]
    }),

    ("johann-jacob-schütz", {
        "summary": (
            "Johann Jacob Schütz (1640–1690) "
            "was a German lawyer, poet, "
            "and one of the earliest "
            "and most important figures "
            "in the Pietist movement "
            "within German Lutheranism. "
            "A close friend and "
            "collaborator of Philipp "
            "Jakob Spener — the "
            "'father of Pietism' who "
            "launched the reform movement "
            "with his 'Pia Desideria' "
            "(1675) — Schütz was "
            "one of the foundational "
            "members of Frankfurt's "
            "collegium pietatis, "
            "the small prayer and "
            "Bible study group "
            "from which the Pietist "
            "movement emerged.\n\n"
            "Pietism was one of "
            "the most significant "
            "religious reform movements "
            "of early modern Europe "
            "— a reaction against "
            "Protestant orthodoxy's "
            "dry intellectualism "
            "that emphasized personal "
            "devotion, heartfelt "
            "faith, Bible study, "
            "and practical Christian "
            "living. From the Frankfurt "
            "collegium, Pietism "
            "spread to Halle, "
            "Württemberg, and "
            "eventually North America.\n\n"
            "Schütz also wrote "
            "influential devotional "
            "hymns that expressed "
            "Pietist religious "
            "experience.\n\n"
            "He was a founding "
            "figure of German Pietism."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Founding figure of German Pietism; close collaborator of Philipp Jakob Spener; foundational member of Frankfurt's collegium pietatis where Pietism emerged; lawyer, poet, and devotional hymnist; his role in launching Pietism contributed to one of the most significant religious reform movements in early modern Europe.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Lutheran orthodoxy's perceived spiritual aridity — the criticism that post-Reformation Lutheranism had become a system of correct doctrine and intellectual assent rather than living faith and personal devotion — created the spiritual hunger that Pietism addressed and that motivated Schütz's reform participation",
            "Philipp Jakob Spener's leadership and intellectual framework — Spener's Pia Desideria (1675) and his vision of 'ecclesiolae in ecclesia' (small groups within the church for intensive devotional life) — provided the theological and organizational framework within which Schütz's collegium participation operated",
            "Frankfurt's commercial and intellectual culture — the city's status as a major commercial and cultural center with a diverse educated population open to new religious ideas — created the social environment for the collegium pietatis's formation"
        ],
        "effects": [
            "His participation in founding the Frankfurt collegium pietatis contributed to launching one of the most significant Protestant religious movements of early modernity — Pietism's influence spread through Germany, Scandinavia, and the German diaspora in North America",
            "His devotional hymns contributed to Pietist religious culture — the emphasis on heartfelt expression of faith in music that Pietism developed and that influenced later Protestant hymnody including Wesley's Methodism",
            "His early support for Spener contributed to legitimizing the Pietist movement among Frankfurt's educated professional class — the lawyers, merchants, and professionals whose participation gave Pietism social credibility beyond the clergy",
            "His career illustrated the close connection between Pietism and Frankfurt's educated laity — the way the movement drew its early strength from devout professionals who wanted a more experiential faith than Lutheran orthodoxy offered"
        ],
        "relationships": [
            {"target": "pietism", "verb": "FOUNDS", "note": "Founding member of the Frankfurt collegium pietatis"},
            {"target": "philipp-jakob-spener", "verb": "COLLABORATES_WITH", "note": "Close collaborator of the father of Pietism"},
            {"target": "frankfurt-collegium-pietatis", "verb": "PARTICIPATES_IN", "note": "Foundational member of the Pietist prayer group"},
            {"target": "lutheranism", "verb": "REFORMS", "note": "Pietist reform of Lutheran spiritual life"},
            {"target": "german-protestantism", "verb": "INFLUENCES", "note": "Contributed to Pietism's spread through German Lutheranism"}
        ]
    }),

    ("jonathan-mason", {
        "summary": (
            "Jonathan Mason (1752–1831) "
            "was an American Federalist "
            "politician from Massachusetts "
            "who served in the U.S. Senate "
            "(1800–1803) and the U.S. "
            "House of Representatives "
            "(1817–1820). A Boston Federalist "
            "in the tradition of the "
            "commercial and legal elite "
            "that dominated Massachusetts "
            "politics, Mason's Senate "
            "service coincided with "
            "the Revolution of 1800 "
            "— the Jeffersonian "
            "Democratic-Republican "
            "sweep that ended Federalist "
            "national dominance "
            "and began the long "
            "process of Federalism's "
            "decline.\n\n"
            "Massachusetts Federalism "
            "was the most deeply "
            "entrenched in New England "
            "— the Boston commercial "
            "elite, the Harvard-educated "
            "professional class, "
            "and the Congregationalist "
            "church establishment "
            "all supported the "
            "Federalist tradition "
            "long after it had "
            "collapsed elsewhere.\n\n"
            "His later House service "
            "(1817–1820) came "
            "during the Era of "
            "Good Feelings — "
            "after the War of 1812 "
            "had finally discredited "
            "New England Federalism "
            "through the Hartford "
            "Convention's secessionist "
            "flirtation.\n\n"
            "He was a prominent "
            "Boston lawyer and "
            "civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts Federalist Senator (1800–1803) and Congressman (1817–1820); Boston commercial elite politician; served through the Revolution of 1800's Federalist collapse and the Era of Good Feelings; representative of Massachusetts's entrenched Federalism that survived longer than in any other state; prominent Boston lawyer and civic leader.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts Federalism's entrenched strength — the Boston commercial elite, Harvard-educated professional class, and Congregationalist church establishment that maintained Federalist political dominance in Massachusetts long after other states had shifted to Democratic-Republican majorities — created the political environment for Mason's Senate and House careers",
            "The Revolution of 1800 — the Jeffersonian sweep that ended Federalist national dominance while Massachusetts remained a Federalist stronghold — created the political contrast that defined Mason's Senate tenure",
            "The War of 1812 and the Hartford Convention — the New England Federalists' opposition to the war and their flirtation with secessionism at the Hartford Convention — created the political crisis that ultimately discredited New England Federalism and shaped the context for Mason's later House service"
        ],
        "effects": [
            "His Senate service contributed Massachusetts's Federalist perspective to the transition from Adams to Jefferson — supporting the Federalist position in the Senate during the Republican majority's first years",
            "His House service during the Era of Good Feelings contributed to the post-Federalist Massachusetts political scene — representing the remnant Federalist tradition as it merged into the National Republican coalition",
            "His career illustrated the durability of Massachusetts Federalism — the way New England's commercial and professional elite maintained Federalist politics long after the party had collapsed nationally",
            "His long civic career in Boston contributed to the cultural and legal life of America's most intellectually sophisticated city — the Boston that was simultaneously Federalist politically and culturally dynamic in its arts, letters, and institutions"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Massachusetts Senator 1800–1803"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Massachusetts Congressman 1817–1820"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Boston Federalist in the Massachusetts tradition"},
            {"target": "revolution-of-1800", "verb": "SERVES_THROUGH", "note": "Senator during Federalism's national collapse"},
            {"target": "massachusetts", "verb": "REPRESENTS", "note": "Boston commercial elite representative"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 71 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
