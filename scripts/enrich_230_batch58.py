#!/usr/bin/env python3
"""
Batch 58 — 8 entities: Joseph Kerr, Juan José Alvarado,
Mihály Vörösmarty, Nathaniel S. Berry, Samuel C. Crafts,
William McWillie, Hernando de Lerma, Joaquín Mora Fernández
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

    ("joseph-kerr", {
        "summary": (
            "Joseph Kerr (1765–1837) was an American "
            "politician from Ohio who served in the "
            "U.S. Senate (1814–1815) and as a member "
            "of the Ohio General Assembly. Born in "
            "Pennsylvania, he was among the early "
            "settlers of Ohio — a state that was "
            "only admitted to the Union in 1803 and "
            "was still rapidly developing its "
            "governmental institutions during "
            "the period of Kerr's political activity.\n\n"
            "Ohio's early statehood made it one of "
            "the most politically dynamic states "
            "in the early republic — a rapidly "
            "growing frontier community drawing "
            "settlers from Virginia, Kentucky, "
            "Pennsylvania, and New England, with "
            "diverse political traditions being "
            "forged into a new state political "
            "culture. The Northwest Ordinance's "
            "prohibition of slavery made Ohio "
            "free soil, distinguishing it from "
            "the neighboring Kentucky and Virginia "
            "from which many settlers came.\n\n"
            "His Senate service (1814–1815) came "
            "during the final phases of the War "
            "of 1812 — including the British "
            "burning of Washington in August 1814 "
            "and the negotiations that produced "
            "the Treaty of Ghent in December 1814. "
            "Ohio's Lake Erie frontier was a direct "
            "theater of the war, with Perry's "
            "victory at the Battle of Lake Erie "
            "(1813) occurring within Ohio's sphere.\n\n"
            "His career represented Ohio's formative "
            "Democratic-Republican political tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Early Ohio settler and Democratic-Republican politician who served as U.S. Senator (1814–1815) during the final phase of the War of 1812; representative of Ohio's formative political culture as a frontier state building its institutions in the early republic.",
            "significanceCategory": "local"
        },
        "causes": [
            "Ohio's recent statehood (1803) and rapid settlement — drawing thousands of migrants from the East and South into the Northwest Territory's fertile lands — created a rapidly growing political community that needed to build state and federal institutions quickly, providing opportunities for early political leaders like Kerr",
            "The War of 1812 and Ohio's role as a frontier theater of the conflict — with Lake Erie a contested waterway and Ohio's settlements threatened by British-allied Native American forces — created the urgent political environment in which Kerr's Senate service took place",
            "The Northwest Ordinance's free-soil provisions — which prohibited slavery in the Northwest Territory and thus in Ohio — shaped Ohio's distinctive political culture as a free-labor state neighboring the slaveholding states of Kentucky and Virginia, creating the unique political tensions that Ohio Congressmen had to navigate"
        ],
        "effects": [
            "His Senate service contributed to Ohio's representation in the federal government during the War of 1812's final year — ensuring that Ohio's frontier interests and Lake Erie security concerns were represented in the wartime Senate",
            "His early political career contributed to the development of Ohio's Democratic-Republican tradition — establishing the patterns of Jeffersonian politics in a new free-soil state that would eventually become important in the second American party system",
            "His career illustrated the rapid political development of new American frontier states — Ohio's ability to generate capable federal legislators within just over a decade of statehood demonstrated the vitality of American democratic institution-building",
            "His participation in Ohio's early political culture contributed to the development of the Northwestern states' distinctive political tradition — combining free-soil values with democratic populism in a combination that would later produce the Republican Party's core geographic base"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Ohio Senator 1814–1815"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Early Ohio settler and state politician"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Senator during the War of 1812's final phase"},
            {"target": "treaty-of-ghent-1814", "verb": "SERVES_DURING", "note": "Senator during the peace negotiations ending War of 1812"},
            {"target": "northwest-ordinance", "verb": "LIVES_UNDER", "note": "Ohio politician shaped by Northwest Ordinance's free-soil legacy"}
        ]
    }),

    ("juan-josé-alvarado", {
        "summary": (
            "Juan Bautista Alvarado (1809–1882) was "
            "a California-born politician who served "
            "as Governor of Alta California under "
            "Mexican rule (1836–1842) — making him "
            "one of the few native Californio leaders "
            "to achieve the governorship through "
            "political skill rather than appointment "
            "from Mexico City. His governorship "
            "coincided with a critical period in "
            "California's history: the collapse "
            "of the Franciscan mission system, "
            "the redistribution of mission lands "
            "to the great ranchos, and the "
            "increasing penetration of foreign "
            "American and Russian traders that "
            "foreshadowed California's eventual "
            "incorporation into the United States.\n\n"
            "Born in Monterey to a Californio "
            "family with deep roots in Alta "
            "California, Alvarado was educated "
            "at the Monterey Presidio and built "
            "a political career in the provincial "
            "diputación — the territorial legislature. "
            "His 1836 revolt against the appointed "
            "Mexican governor established him "
            "as the effective ruler of California, "
            "which he governed for six years.\n\n"
            "His administration saw the secularization "
            "of the Franciscan missions — converting "
            "the missions from church-controlled "
            "institutions to secular towns and "
            "redistributing their vast lands "
            "to Californio ranching families.\n\n"
            "He lived to see California's American "
            "conquest and the Gold Rush transform "
            "the world he had governed."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Governor of Alta California under Mexico (1836–1842); California-born Californio leader who achieved power through revolt and governed during the crucial secularization of the Franciscan missions and the redistribution of mission lands; witnessed the American conquest and Gold Rush that transformed his former territory.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the Franciscan mission system and Mexican government secularization policies — which converted the missions from church-controlled agricultural institutions to civilian settlements and redistributed their enormous California landholdings — created the political and economic transformation that defined Alvarado's gubernatorial era",
            "The weakness of Mexico City's authority over distant Alta California — demonstrated by the chronic instability of appointed governors and the inability of the central government to defend the territory from foreign settlement — created the conditions in which Alvarado's 1836 revolt against the incumbent Mexican governor could succeed",
            "The increasing penetration of Alta California by American and Russian traders and settlers — whose economic importance to California's hide-and-tallow economy gave them leverage over Californio politics — shaped the external pressures that Alvarado had to manage during his governorship"
        ],
        "effects": [
            "His secularization of the Franciscan missions during his governorship transformed California's social and economic structure — redistributing the missions' enormous landholdings to Californio ranching families and effectively ending the paternalistic mission system that had organized California's indigenous labor",
            "His six-year governorship established the precedent that native Californios could exercise effective autonomous governance — temporarily reducing Mexico City's control over California affairs and building Californio political consciousness",
            "His administration's encouragement of foreign — especially American — settlement and trade contributed to the demographic and economic transformation that made California increasingly oriented toward the United States",
            "His lifetime — from Mexican governor to witness of American conquest, Gold Rush, and California statehood — made him a living embodiment of the transformation from Spanish/Mexican California to American California, a transition he documented in memoirs that became important historical sources"
        ],
        "relationships": [
            {"target": "alta-california", "verb": "GOVERNS", "note": "Governor of Alta California under Mexico 1836–1842"},
            {"target": "franciscan-missions-california", "verb": "SECULARIZES", "note": "Carried out secularization of California missions"},
            {"target": "mexican-republic", "verb": "PART_OF", "note": "Californio politician within the Mexican federal system"},
            {"target": "california-ranchos", "verb": "ENABLES", "note": "Mission land redistribution created the rancho era"},
            {"target": "american-conquest-of-california", "verb": "PRECEDES", "note": "Californio governor whose territory was conquered by the U.S."}
        ]
    }),

    ("mihály-vörösmarty", {
        "summary": (
            "Mihály Vörösmarty (1800–1855) was the "
            "greatest Hungarian poet of the Reform "
            "Era — the period of national awakening "
            "between the 1820s and the 1848 Revolution "
            "when Hungarian national consciousness, "
            "language reform, and constitutional "
            "demands for independence transformed "
            "the Kingdom of Hungary within the "
            "Habsburg Empire. His epic poem Zalán "
            "futása (The Flight of Zalán, 1825) — "
            "evoking the Magyar conquest of the "
            "Carpathian Basin in the ninth century — "
            "electrified the Hungarian nobility "
            "and public, establishing him as the "
            "national poet. His Szózat (Appeal, 1836) "
            "became the second Hungarian national "
            "anthem alongside the Himnusz.\n\n"
            "Born in the Fejér County of Hungary "
            "to a modest family, Vörösmarty "
            "achieved recognition through his "
            "poetry before he was thirty. His "
            "epic Zalán futása appeared in 1825 — "
            "the year the Hungarian Reform Era "
            "began in earnest with István Széchenyi's "
            "famous gift of a year's income to found "
            "the Hungarian Academy of Sciences.\n\n"
            "Vörösmarty became one of the central "
            "figures of the Hungarian linguistic "
            "and national revival — a close "
            "associate of Széchenyi, Deák, and "
            "the reformers who sought to modernize "
            "Hungary within the Habsburg framework.\n\n"
            "After the defeat of the 1848 Revolution "
            "he fell into deep despair, dying "
            "in 1855 after years of suffering."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Hungary's greatest Reform Era poet; author of Zalán futása (1825) and Szózat (1836) — effectively Hungary's second national anthem; central figure of the Hungarian national awakening who defined the literary and emotional vocabulary of Magyar nationalism; close associate of the Reform Era's leading statesmen.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Hungarian Reform Era (1825–1848) — the period of intensive national cultural, linguistic, and political revival driven by the Hungarian nobility's determination to assert national distinctiveness against Habsburg German cultural domination — created the cultural moment in which Vörösmarty's romantic nationalist poetry found its enormous audience",
            "The Hungarian language reform movement — the systematic modernization and standardization of the Magyar language led by Ferenc Kazinczy and his circle — prepared the linguistic tools that Vörösmarty used to create the elevated, emotional, patriotic literary Hungarian that became the standard for the national literary tradition",
            "The romantic nationalist movement in European literature — the use of medieval epics, folk traditions, and national mythologies to construct national cultural identity — provided the literary model that Vörösmarty adapted to the Hungarian national awakening, producing historical epics and lyric poetry that defined Magyar national consciousness"
        ],
        "effects": [
            "His Zalán futása (1825) electrified the Hungarian public with its romantic evocation of the Magyar conquest of the Carpathian Basin — establishing him as Hungary's national poet and providing the emotional and literary vocabulary for the Reform Era's national consciousness",
            "His Szózat (Appeal, 1836) became effectively Hungary's second national anthem — its opening line ('To your homeland unwaveringly, O Magyar') expressing the absolute commitment to the Hungarian nation that became the emotional keynote of the 1848 Revolution",
            "His poetic career established Hungarian romantic literature as a mature and sophisticated national literary tradition — demonstrating that the Magyar language, despite its marginal position in the Habsburg Empire's German-Latin high culture, could produce great literature",
            "His close association with the Reform Era's political leaders — Széchenyi, Deák, and later Kossuth — connected poetry directly to political action in the Hungarian national awakening, making literary culture and political reform mutually reinforcing components of a single national movement"
        ],
        "relationships": [
            {"target": "hungarian-reform-era", "verb": "DEFINES", "note": "Greatest poet of Hungary's national awakening"},
            {"target": "szozat", "verb": "AUTHORS", "note": "Wrote Hungary's second national anthem (1836)"},
            {"target": "zalan-futasa", "verb": "AUTHORS", "note": "Authored the epic poem that launched his national fame (1825)"},
            {"target": "hungarian-academy-of-sciences", "verb": "MEMBER_OF", "note": "Member of the Academy founded in the same year as Zalán futása"},
            {"target": "hungarian-revolution-1848", "verb": "INSPIRES", "note": "Poet of the national consciousness that drove the 1848 Revolution"}
        ]
    }),

    ("nathaniel-s-berry", {
        "summary": (
            "Nathaniel Springer Berry (1796–1894) was "
            "an American Free Soil and Republican "
            "politician from New Hampshire who served "
            "as Governor of New Hampshire (1861–1863) — "
            "the only Free Soiler ever elected governor "
            "of New Hampshire — and whose remarkable "
            "longevity (he lived to 97) made him the "
            "last surviving governor of any state "
            "to have served during the Civil War era. "
            "His anti-slavery convictions and "
            "Free Soil political career represented "
            "the moral reform tradition in "
            "New Hampshire politics that contributed "
            "to the formation of the Republican Party.\n\n"
            "Berry was born in Bath, New Hampshire "
            "and built a career as a tanner before "
            "entering politics. His political "
            "career traced the trajectory of "
            "Northern anti-slavery politics — "
            "from the anti-slavery wing of "
            "the Democratic Party through the "
            "Free Soil Party (1848) to the "
            "Republican Party's emergence in the "
            "mid-1850s as the vehicle for the "
            "Northern anti-slavery coalition.\n\n"
            "His governorship (1861–1863) coincided "
            "with the Civil War's first two years "
            "— when New Hampshire, like all Northern "
            "states, had to mobilize men, money, "
            "and resources for the war effort "
            "while maintaining civilian governance "
            "during an unprecedented national crisis.\n\n"
            "His extraordinary longevity made him "
            "a living historical witness to American "
            "history from the early republic through "
            "the Gilded Age."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Free Soil and Republican Governor of New Hampshire (1861–1863) during the Civil War; the only Free Soiler elected governor of New Hampshire; lived to 97 as the last surviving Civil War era governor; his career traced the anti-slavery movement from Free Soil through the Republican Party.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Free Soil movement's emergence in 1848 — organizing Northern opposition to the extension of slavery into the territories won from Mexico — created the political coalition and moral framework within which Berry built his anti-slavery political identity before the Republican Party absorbed the Free Soilers in the mid-1850s",
            "The sectional crisis of the 1850s — the Kansas-Nebraska Act's repeal of the Missouri Compromise, the Bleeding Kansas violence, and John Brown's raids — intensified Northern anti-slavery feeling in states like New Hampshire and created the electoral conditions for an anti-slavery Republican to win the governorship",
            "The Civil War's outbreak (1861) and the Northern states' need for wartime governors capable of mobilizing state resources for the Union war effort — organizing volunteer regiments, managing the draft, maintaining civilian order, and sustaining public support — made Berry's governorship a critical management challenge"
        ],
        "effects": [
            "His governorship managed New Hampshire's Civil War mobilization — organizing the state's contribution of soldiers, supplies, and financial resources to the Union war effort during the war's first two critical years",
            "His election as the only Free Soil governor in New Hampshire's history demonstrated the penetration of anti-slavery politics into a traditionally Democratic New England state — contributing to New Hampshire's alignment with the Republican Party that would dominate its politics for decades",
            "His extraordinary lifespan — surviving into the 1890s — made him a living historical witness who could connect the personal memories of the antebellum republic to audiences in the Gilded Age",
            "His political career illustrated the moral reform tradition in New England politics — the combination of religious nonconformism, anti-slavery conviction, and democratic populism that created the Free Soil and Republican movements"
        ],
        "relationships": [
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor of New Hampshire 1861–1863"},
            {"target": "free-soil-party", "verb": "MEMBER_OF", "note": "Only Free Soil governor of New Hampshire"},
            {"target": "republican-party-united-states", "verb": "MEMBER_OF", "note": "Free Soiler who aligned with the emerging Republican Party"},
            {"target": "american-civil-war", "verb": "GOVERNS_DURING", "note": "Wartime governor managing New Hampshire's Civil War mobilization"},
            {"target": "anti-slavery-movement", "verb": "REPRESENTS", "note": "Moral reform anti-slavery politician from New England"}
        ]
    }),

    ("samuel-c-crafts", {
        "summary": (
            "Samuel Chandler Crafts (1768–1853) was "
            "an American Federalist and National "
            "Republican politician from Vermont who "
            "served as Governor of Vermont (1828–1831) "
            "and as a member of the U.S. House of "
            "Representatives (1817–1825). His political "
            "career represented Vermont's Federalist "
            "and anti-Jacksonian tradition — a state "
            "that resisted the Jacksonian Democratic "
            "tide and became one of the most strongly "
            "Whig and later Republican states in "
            "the antebellum period.\n\n"
            "Crafts was born in Craftsbury, Vermont — "
            "a town founded by his family — and "
            "built his career in Vermont's legal "
            "and political life. Vermont's political "
            "culture combined Green Mountain "
            "independence with a strong Federalist "
            "tradition rooted in the state's "
            "New England heritage and its commercial "
            "connections to Quebec and New York.\n\n"
            "His House service (1817–1825) spanned "
            "the Era of Good Feelings and the "
            "beginning of the Adams-Clay National "
            "Republican coalition that represented "
            "the alternative to Jacksonian populism. "
            "His governorship (1828–1831) came "
            "during the peak of Jacksonian political "
            "mobilization — the years when Vermont's "
            "resistance to Jackson's coalition "
            "was most politically significant.\n\n"
            "Vermont's anti-Jacksonian tradition "
            "that Crafts embodied would persist "
            "until Vermont became a Republican "
            "stronghold."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont National Republican Governor (1828–1831) and Congressman (1817–1825); representative of Vermont's anti-Jacksonian political tradition; Federalist to National Republican to Whig trajectory; governor during the height of Jacksonian political mobilization in a state that resisted it most strongly.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's strong Federalist political tradition — rooted in New England commercial interests, suspicion of Southern slave-power domination, and the Green Mountain state's cultural orientation toward New England rather than the frontier West — created the anti-Jacksonian constituency that Crafts represented",
            "The breakdown of the Democratic-Republican Party and the emergence of the Adams-Clay National Republican coalition — which appealed to commercial interests, manufacturing protection, and federal internal improvements — provided the political home for Vermont's anti-Jacksonian politicians including Crafts",
            "Andrew Jackson's 1828 election and the Jacksonian Democrats' populist mobilization — which swept most of the country but met sustained resistance in New England, including Vermont — defined the political environment of Crafts's governorship"
        ],
        "effects": [
            "His governorship maintained Vermont's resistance to Jacksonian Democratic dominance during the critical years of the second American party system's formation — helping sustain Vermont's National Republican tradition that would eventually produce the state's strong Whig identity",
            "His House service contributed to the National Republican legislative program under Adams — supporting the American System of tariff protection, internal improvements, and federal banking that represented the alternative to Jacksonian laissez-faire states'-rights politics",
            "His career illustrated Vermont's distinctive anti-Jacksonian political tradition — a tradition so strong that Vermont became one of only two states to vote against Jackson in 1832 and one of the few states that consistently resisted Democratic majorities throughout the antebellum period",
            "His political trajectory — from Federalist through National Republican to eventual Whig alignment — illustrated the partisan evolution of New England's conservative political culture through the party realignments of the 1820s and 1830s"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1828–1831"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Representative 1817–1825"},
            {"target": "national-republican-party", "verb": "MEMBER_OF", "note": "National Republican opposing Jacksonian Democracy"},
            {"target": "andrew-jackson", "verb": "OPPOSES", "note": "Anti-Jacksonian governor during peak of Jackson's popularity"},
            {"target": "american-system-clay", "verb": "SUPPORTS", "note": "Supporter of Clay's tariff and internal improvements program"}
        ]
    }),

    ("william-mcwillie", {
        "summary": (
            "William McWillie (1795–1869) was a "
            "South Carolina–born lawyer and "
            "Democratic politician who served "
            "as Governor of Mississippi (1857–1859) "
            "and as a U.S. Representative "
            "(1849–1851). His political career "
            "represented the Southern Democratic "
            "tradition in Mississippi — a state "
            "that was a center of the cotton "
            "plantation economy and whose politics "
            "were increasingly dominated by the "
            "defense of slavery and Southern "
            "rights against Northern antislavery "
            "pressure.\n\n"
            "McWillie was born in South Carolina "
            "and migrated to Mississippi — a pattern "
            "typical of Southern migrants who moved "
            "westward to exploit Mississippi's "
            "fertile cotton lands. Mississippi's "
            "rapid growth as a cotton state after "
            "the 1830s made it one of the most "
            "prosperous and politically assertive "
            "Southern states.\n\n"
            "His governorship (1857–1859) came "
            "during the increasingly tense "
            "sectional crisis of the late 1850s "
            "— after the Kansas-Nebraska Act, "
            "Bleeding Kansas, and the Dred Scott "
            "decision had made sectional conflict "
            "the dominant fact of American political "
            "life. Mississippi's politics were "
            "consumed by the defense of slavery "
            "and the state's rights to carry "
            "slave property into the territories.\n\n"
            "He lived to see Mississippi's secession "
            "from the Union and the Civil War's "
            "destruction of the slave-based "
            "society he had governed."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Governor of Mississippi (1857–1859) and U.S. Representative (1849–1851); Southern Democratic politician representing the cotton state's increasingly assertive pro-slavery politics during the sectional crisis of the 1850s; presided over Mississippi during the Dred Scott decision and Kansas bleeding crises.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mississippi's development as a major cotton-producing state — with an economy dependent on enslaved labor on the fertile Black Belt plantations — created the social and economic foundation for the pro-slavery political culture that McWillie represented and perpetuated",
            "The sectional crisis of the 1850s — the Kansas-Nebraska Act's reopening of the slavery extension question, Bleeding Kansas, the Dred Scott decision, and John Brown's Harper's Ferry raid — intensified Southern demands for federal protection of slavery and states' rights in the territories, making pro-slavery politics the central issue of McWillie's governorship",
            "The Democratic Party's Southern wing's domination of Mississippi politics — providing the single-party framework within which Southern politicians competed for advancement through loyalty to pro-slavery positions — shaped the political environment in which McWillie built his career"
        ],
        "effects": [
            "His governorship managed Mississippi's political affairs during the most volatile years of the antebellum sectional crisis — maintaining Democratic unity in support of the Buchanan administration's pro-Southern policies while the country moved toward secession",
            "His support for Southern rights during his governorship contributed to Mississippi's eventual secession from the Union — the state's political culture of militant pro-slavery politics that his career exemplified led directly to secession in January 1861",
            "His career illustrated the Southern Democratic political model — the combination of personal ambition, ideological commitment to states' rights and slavery, and hostility to federal antislavery action that characterized the Southern Democratic politicians who led their states into the Confederacy",
            "His post-war survival in a transformed Mississippi — stripped of slavery, economically devastated by the Civil War, and subject to Reconstruction — made him a figure of the Old South's destroyed world, living through the consequences of the pro-slavery politics he had championed"
        ],
        "relationships": [
            {"target": "mississippi", "verb": "GOVERNS", "note": "Governor of Mississippi 1857–1859"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Mississippi Representative 1849–1851"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Southern Democrat defending slavery and states' rights"},
            {"target": "sectional-crisis-1850s", "verb": "SERVES_DURING", "note": "Governor during the Kansas-Nebraska Act and Dred Scott era"},
            {"target": "antebellum-south", "verb": "REPRESENTS", "note": "Political representative of Mississippi's cotton plantation society"}
        ]
    }),

    ("hernando-de-lerma", {
        "summary": (
            "Hernando de Lerma (c. 1540–c. 1590) was "
            "a Spanish colonial administrator who "
            "served as the first Governor of the "
            "Gobernación of Tucumán — the Spanish "
            "colonial province encompassing much "
            "of northwestern Argentina — from 1577 "
            "to 1584. His most lasting legacy was "
            "the foundation of the city of Salta "
            "in 1582 — today the capital of Argentina's "
            "Salta Province and one of the best-"
            "preserved colonial cities in South America.\n\n"
            "Lerma arrived in South America as part "
            "of the Spanish colonial expansion "
            "into the interior of the Río de la "
            "Plata region — the vast territory "
            "encompassing modern Argentina, "
            "Bolivia, Paraguay, and Uruguay. "
            "The Spanish Crown's strategy in this "
            "region combined silver extraction "
            "(the great Potosí mines in Upper Peru "
            "were the richest in the world), "
            "Christian evangelization, and the "
            "subjugation of the indigenous "
            "Diaguita, Omaguaca, and other "
            "Andean peoples.\n\n"
            "The foundation of Salta in 1582 — "
            "named San Felipe de Lerma in the "
            "fertile Lerma Valley — established "
            "a permanent Spanish settlement that "
            "became a critical waypoint on the "
            "road connecting Potosí's silver "
            "to Buenos Aires and the Atlantic.\n\n"
            "Lerma was eventually recalled to Spain "
            "on charges of corruption and abuse "
            "of his authority — a common fate "
            "for colonial administrators in "
            "the Spanish Empire."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Governor of the Gobernación of Tucumán (1577–1584) and founder of Salta (1582) — one of Argentina's most important colonial cities and today the capital of Salta Province; his governorship established Spanish colonial authority in northwestern Argentina; recalled to Spain on corruption charges.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Spanish colonial expansion into the Río de la Plata interior — driven by the need to connect the Potosí silver mines to Atlantic ports, subjugate indigenous populations, and establish permanent Spanish settlements — created the administrative need for a governor of the Tucumán region that Lerma filled",
            "The Potosí silver economy's importance to the Spanish Empire — the mines' output financed the entire Spanish imperial system — made the Tucumán road connecting Potosí to Buenos Aires strategically critical, requiring permanent fortified settlements like Salta as waypoints and supply bases",
            "The Spanish colonial system's use of appointed governors with broad military, judicial, and administrative authority — the encomienda system that granted governors and conquistadors authority over indigenous labor — provided the institutional framework within which Lerma exercised the arbitrary power that eventually led to his recall"
        ],
        "effects": [
            "His foundation of Salta (1582) established one of Argentina's most enduring and historically significant cities — the 'Lerma Valley' city that became a critical node in the Potosí-Buenos Aires trade route and remains one of the best-preserved Spanish colonial cities in South America",
            "His governorship established Spanish colonial authority over the Tucumán region — subjugating indigenous populations, granting encomiendas to Spanish settlers, and building the administrative framework that integrated northwestern Argentina into the Spanish colonial system",
            "His recall on corruption charges illustrated the chronic problems of the Spanish colonial administrative system — the enormous distance from Spain, the governors' arbitrary power over colonists and indigenous people, and the corruption and abuse that the imperial government struggled to control through inspection and recall",
            "The city of Salta became one of Argentina's most important cities — today the capital of Salta Province and a cultural center whose preserved colonial architecture makes it Argentina's most 'colonial' city, carrying Lerma's foundation forward across four centuries"
        ],
        "relationships": [
            {"target": "gobernacion-de-tucuman", "verb": "GOVERNS", "note": "First Governor of the Tucumán colonial province 1577–1584"},
            {"target": "salta-argentina", "verb": "FOUNDS", "note": "Founded the city of Salta in 1582"},
            {"target": "spanish-colonial-empire", "verb": "SERVES", "note": "Spanish colonial administrator in Río de la Plata"},
            {"target": "potosi-silver-mines", "verb": "SERVES_ECONOMY_OF", "note": "Governorship protected the Potosí trade route"},
            {"target": "rio-de-la-plata", "verb": "ADMINISTERS", "note": "Governor in the interior of the Río de la Plata region"}
        ]
    }),

    ("joaquín-mora-fernández", {
        "summary": (
            "Juan Mora Fernández (1784–1854) was "
            "a Costa Rican statesman who served "
            "as the first Head of State of "
            "Costa Rica (1824–1833) — the leader "
            "who guided the newly independent "
            "nation through its formative first "
            "decade as a self-governing republic "
            "after the dissolution of the "
            "Central American Federation. His "
            "decade in power established the "
            "basic institutions of the Costa "
            "Rican state, promoted education, "
            "and pursued the coffee cultivation "
            "that would transform Costa Rica's "
            "economy and social structure "
            "in the mid-nineteenth century.\n\n"
            "Mora Fernández was born in San José "
            "during the Spanish colonial period "
            "and built a career as a lawyer "
            "and public official. Costa Rica's "
            "independence came as part of the "
            "broader Central American independence "
            "from Spain in 1821, and the region's "
            "subsequent political turmoil — the "
            "brief annexation to Mexico and then "
            "the formation of the Central American "
            "Federation — left Costa Rica's "
            "specific institutional future "
            "unresolved until the 1824 constitution.\n\n"
            "His most important economic legacy "
            "was the promotion of coffee cultivation — "
            "distributing free coffee seedlings "
            "to Costa Rican farmers, a decision "
            "that within decades transformed "
            "Costa Rica into a coffee-exporting "
            "economy and reshaped its society.\n\n"
            "He is remembered as the founder "
            "of the Costa Rican state."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First Head of State of Costa Rica (1824–1833); founding statesman who established Costa Rican institutions and promoted coffee cultivation — the economic transformation that shaped Costa Rican society for generations; guided Costa Rica through its first decade of self-governance after Central American independence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Central American independence from Spain (1821) and the subsequent dissolution of the Central American Federation — which left Costa Rica as an independent republic without established governing institutions — created the founding moment in which Mora Fernández's decade of leadership built the basic structures of the Costa Rican state",
            "Costa Rica's geographic isolation, small population, and lack of a large indigenous labor force — which prevented the development of the large plantation economy typical of other Central American regions — created the social conditions for the smallholder farming society that Mora Fernández's land and coffee policies encouraged",
            "The global coffee economy's expansion in the early nineteenth century — as European demand for coffee increased and as tropical American producers recognized the commodity's economic potential — provided the economic opportunity that Mora Fernández's distribution of free coffee seedlings was designed to exploit"
        ],
        "effects": [
            "His promotion of coffee cultivation — distributing free seedlings and encouraging farmers to plant coffee — launched the coffee economy that within decades transformed Costa Rica from a subsistence farming society to a coffee-exporting nation, funding education, infrastructure, and the development of San José as a modern city",
            "His decade as Head of State established Costa Rica's basic republican institutions — the constitutional framework, judicial system, and administrative structures that distinguished Costa Rica from its more turbulent Central American neighbors",
            "His educational initiatives — establishing schools and promoting literacy — contributed to Costa Rica's development of the relatively high education levels that distinguished it from other Central American countries and became a source of national pride",
            "His legacy as Costa Rica's founding statesman established the national narrative of Costa Rican exceptionalism — the idea of Costa Rica as a uniquely peaceful, democratic, and educationally advanced country — that has shaped Costa Rican national identity since independence"
        ],
        "relationships": [
            {"target": "costa-rica", "verb": "FOUNDS", "note": "First Head of State of Costa Rica 1824–1833"},
            {"target": "central-american-federation", "verb": "PART_OF", "note": "Costa Rican leader within and after the Central American Federation"},
            {"target": "costa-rica-coffee-economy", "verb": "INITIATES", "note": "Promoted coffee cultivation that transformed Costa Rica"},
            {"target": "central-american-independence-1821", "verb": "FOLLOWS_FROM", "note": "Led Costa Rica in the immediate post-independence period"},
            {"target": "san-jose-costa-rica", "verb": "GOVERNS", "note": "Head of State based in San José"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 58 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
