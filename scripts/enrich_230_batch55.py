#!/usr/bin/env python3
"""
Batch 55 — 8 entities: Christopher Frimann Omsen, Jasper Ewing Brady,
Francisco Ferrera, George K. Kunowsky, José Santiago Bueso,
Pierre-Stanislas Bédard, William Duhurst Merrick, Eli P. Ashmun
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

    # 1 — Christopher Frimann Omsen
    ("christopher-frimann-omsen", {
        "summary": (
            "Christopher Frimann Omsen (1762–1840) was "
            "a Norwegian lawyer and judge who participated "
            "in the Eidsvoll Constituent Assembly of "
            "1814 — the founding constitutional convention "
            "that created the Norwegian Constitution of "
            "17 May 1814. As one of the 112 delegates "
            "who gathered at Eidsvoll following Norway's "
            "separation from Denmark, Omsen contributed "
            "to the deliberations that produced one of "
            "the most liberal constitutions in the world "
            "at that time.\n\n"
            "Norway's constitutional moment in 1814 "
            "was triggered by the Treaty of Kiel "
            "(January 1814), in which Denmark ceded "
            "Norway to Sweden as part of the post-Napoleonic "
            "settlement. Norwegian patriots, led by "
            "Prince Christian Frederik, refused this "
            "transfer and convened a constituent assembly "
            "at Eidsvoll to draft an independent "
            "constitution. The assembly drew heavily "
            "on American (1787), French (1791), and "
            "existing European constitutional models.\n\n"
            "Omsen represented the legal-administrative "
            "class that formed a significant portion "
            "of the Eidsvoll delegates — the trained "
            "lawyers and officials who could translate "
            "constitutional theory into workable legal "
            "text. His participation placed him "
            "among the founding generation of the "
            "Norwegian constitutional state.\n\n"
            "The Constitution of 17 May 1814 he helped "
            "draft established a constitutional monarchy "
            "with a sovereign Storting (parliament), "
            "civil liberties, and popular representation "
            "— and endured, with amendments, as "
            "Norway's fundamental law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norwegian lawyer and member of the Eidsvoll Constituent Assembly (1814) that drafted the Norwegian Constitution; one of the 112 delegates who created one of the world's most liberal constitutions; representative of the legal-administrative class that gave the Eidsvoll constitution its technical precision.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Treaty of Kiel (January 1814) — in which Denmark ceded Norway to Sweden following Denmark's defeat in the Napoleonic Wars — created the political crisis that triggered Norway's constitutional revolution, as Norwegian patriots refused the transfer and convened the Eidsvoll Assembly",
            "Norway's legal-administrative class's accumulated expertise — lawyers and officials trained in Danish-Norwegian civil law and Enlightenment political philosophy — provided the technical capacity to draft a sophisticated constitutional document at Eidsvoll",
            "The global constitutional moment of the 1810s — following the American Constitution of 1787 and the French constitutional experiments — provided intellectual models and practical templates from which the Eidsvoll delegates constructed Norway's constitution"
        ],
        "effects": [
            "His participation in the Eidsvoll Assembly contributed to the drafting of the Norwegian Constitution of 17 May 1814 — a document that established Norway's parliamentary democracy and endured as the nation's fundamental law",
            "The Constitution he helped create became Norway's National Day holiday (17 May), making Eidsvoll delegates like Omsen permanent figures in Norwegian national memory",
            "His career as a lawyer-constitutional founder illustrated the role of legal professionals in the creation of early modern constitutional states — translating Enlightenment political theory into enforceable constitutional text",
            "Norway's constitution became an influential model for European liberal constitutionalism in the nineteenth century, making Omsen's contribution part of a document with continental impact beyond Norway's borders"
        ],
        "relationships": [
            {"target": "norwegian-constitution-1814", "verb": "DRAFTS", "note": "Member of the Eidsvoll Constituent Assembly"},
            {"target": "eidsvoll-assembly-1814", "verb": "PARTICIPATES_IN", "note": "One of 112 delegates to the constitutional convention"},
            {"target": "treaty-of-kiel-1814", "verb": "RESPONDS_TO", "note": "Constitutional assembly convened after Danish cession of Norway"},
            {"target": "norway", "verb": "SERVES", "note": "Norwegian lawyer and constitutional founder"},
            {"target": "norwegian-law", "verb": "PRACTICES", "note": "Lawyer in the Danish-Norwegian legal tradition"}
        ]
    }),

    # 2 — Jasper Ewing Brady
    ("jasper-ewing-brady", {
        "summary": (
            "Jasper Ewing Brady (1797–1871) was an American "
            "lawyer and Democratic politician from "
            "Pennsylvania who served in the U.S. House "
            "of Representatives (1847–1849) representing "
            "the Pittsburgh district. His congressional "
            "term coincided with one of the most "
            "momentous periods in American history: "
            "the Mexican-American War (1846–1848), "
            "the Wilmot Proviso debates over the "
            "extension of slavery into new territories, "
            "and the opening of the great sectional "
            "crisis that would culminate in the Civil War.\n\n"
            "Brady built his legal career in Pittsburgh — "
            "a rapidly growing industrial city at the "
            "confluence of the Allegheny, Monongahela, "
            "and Ohio rivers that was becoming the "
            "center of American iron and steel production. "
            "His Democratic Party affiliation placed "
            "him within the Pennsylvania Democratic "
            "tradition that balanced strong support "
            "for tariff protection (essential to "
            "Pittsburgh's iron industry) with the "
            "national Democratic Party's pro-slavery "
            "southern wing.\n\n"
            "His single congressional term (1847–1849) "
            "placed him in the midst of the Wilmot "
            "Proviso debates — the proposal to ban "
            "slavery from any territory acquired from "
            "Mexico — a controversy that split the "
            "Democratic Party along sectional lines "
            "and foreshadowed the party realignments "
            "of the 1850s.\n\n"
            "His Pittsburgh-area career exemplified "
            "the industrial Democrat of the antebellum "
            "North — a type pulled between party "
            "loyalty and sectional conviction."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Pennsylvania Democratic Congressman (1847–1849) from Pittsburgh; served during the Mexican-American War and Wilmot Proviso debates; representative of the industrial Democratic tradition that balanced Pittsburgh's tariff interests with the national Democratic Party's southern wing.",
            "significanceCategory": "local"
        },
        "causes": [
            "Pittsburgh's emergence as America's premier iron-producing city in the antebellum decades — driven by its access to coal, its river transportation network, and its proximity to iron ore — created the industrial Democratic political culture in which Brady's career flourished",
            "The Mexican-American War (1846–1848) and the resulting acquisition of vast new territories from Mexico — which immediately raised the explosive question of whether slavery would be permitted in those territories — defined the congressional debates of Brady's single term and placed every Democratic congressman in the impossible position of the Wilmot Proviso",
            "Pennsylvania's Democratic Party's complex position — needing to balance the tariff protection demands of Pittsburgh's iron interests with the free-trade preferences of the party's Southern wing — shaped the political dilemmas that Pennsylvania Democratic Congressmen like Brady had to navigate"
        ],
        "effects": [
            "His congressional vote on the Wilmot Proviso and related slavery-extension questions contributed to the record of Northern Democratic responses to the sectional crisis — a record that documented the growing impossibility of maintaining the Democratic coalition across the slavery divide",
            "His representation of Pittsburgh's industrial district in Congress ensured that the iron industry's tariff concerns were heard in the debates over trade and economic policy during a period when protective tariffs were central to Pennsylvania politics",
            "His single-term career illustrated the political volatility of the antebellum congressional environment — where the slavery question was increasingly disrupting the normal partisan loyalties that had organized American politics since the Jacksonian era",
            "His career in Pittsburgh's Democratic legal-political world contributed to the development of the city's antebellum Democratic Party organization — a party that would fracture over slavery in the 1850s and be replaced by the Republicans as Pittsburgh's dominant political force"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1847–1849"},
            {"target": "wilmot-proviso", "verb": "VOTES_ON", "note": "Congressman during the slavery-extension debates"},
            {"target": "mexican-american-war", "verb": "GOVERNS_DURING", "note": "Congressman during the war and its territorial consequences"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Pennsylvania Democrat aligned with party's industrial wing"},
            {"target": "pittsburgh", "verb": "REPRESENTS", "note": "Lawyer and politician from Pittsburgh's industrial district"}
        ]
    }),

    # 3 — Francisco Ferrera
    ("francisco-ferrera", {
        "summary": (
            "Francisco Ferrera (1794–1851) was a "
            "Honduran military commander and politician "
            "who served as President of Honduras "
            "multiple times during the turbulent "
            "years following Central American "
            "independence (1821) and the collapse "
            "of the Central American Federation "
            "(1838–1839). A conservative caudillo "
            "who opposed liberal federalist movements, "
            "Ferrera was one of the dominant political "
            "and military figures of Honduras in "
            "the 1830s–1840s — an era of near-continuous "
            "civil war, regional fragmentation, and "
            "the violent competition between conservative "
            "and liberal factions that characterized "
            "Central American politics after federation's end.\n\n"
            "Ferrera's political career began in the "
            "independence period and accelerated with "
            "the collapse of the Central American "
            "Federation, whose dissolution left "
            "Honduras as one of five independent "
            "Central American states competing for "
            "stability and sovereignty. He served "
            "as president (1841–1845, 1847–1848) "
            "and as a dominant military force "
            "in Honduras for most of the 1840s.\n\n"
            "His conservatism aligned him with "
            "the Church, large landowners, and "
            "those who preferred local autonomy "
            "over the liberal federalist project "
            "of recreating the Central American "
            "union. He repeatedly fought against "
            "liberal opponents — including "
            "Francisco Morazán, the greatest "
            "liberal caudillo of Central America "
            "— defending Honduran sovereignty "
            "against liberal federalist intervention.\n\n"
            "His career embodied the early republican "
            "struggle for order and sovereignty "
            "in post-independence Central America."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President of Honduras multiple times (1841–1845, 1847–1848) and conservative military caudillo; dominant political figure in Honduras during the turbulent post-federation era; opponent of liberal federalism and Francisco Morazán; shaped Honduran politics during the critical decades of early independence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the Central American Federation (1838–1839) — which left Honduras as a newly independent state without established institutions, recurring civil wars, and competing factions — created the political vacuum in which military caudillos like Ferrera could seize power through force of arms and personal loyalty networks",
            "The liberal-conservative conflict that dominated Central American politics in the 1830s–1840s — between liberal federalists who wanted to recreate the Central American Union under liberal governance and conservatives who preferred local church authority and traditional social hierarchies — positioned Ferrera as the leading conservative military figure in Honduras",
            "Francisco Morazán's liberal federalist project — which sought to unite Central America under a liberal constitutional government — directly threatened the conservative order that Ferrera represented, making opposition to Morazán the defining military and political mission of Ferrera's career"
        ],
        "effects": [
            "His conservative presidencies (1841–1845, 1847–1848) helped establish Honduras as an independent conservative-oriented state that resisted reintegration into a liberal Central American federation — contributing to the permanent fragmentation of Central America into five separate republics",
            "His military opposition to liberal federalism — including campaigns against Morazán's forces — reinforced the conservative order in Honduras and demonstrated that the liberal federalist project could not be reimposed on states that had already established separate conservative governments",
            "His repeated return to power illustrated the caudillo pattern of post-independence Central American politics — in which personal military leadership, regional loyalty networks, and conservative Church alliances gave individual strongmen the capacity to dominate state politics across multiple terms",
            "His career established patterns of conservative governance in Honduras — aligned with the Catholic Church and large landowners — that shaped Honduran political culture through the nineteenth century"
        ],
        "relationships": [
            {"target": "honduras", "verb": "GOVERNS", "note": "President of Honduras multiple terms 1841–1845, 1847–1848"},
            {"target": "francisco-morazan", "verb": "OPPOSES", "note": "Conservative opponent of liberal federalist Morazán"},
            {"target": "central-american-federation", "verb": "SUCCEEDS_AFTER", "note": "Post-federation Honduran caudillo"},
            {"target": "central-american-conservatism", "verb": "LEADS", "note": "Leading conservative military figure in Honduras"},
            {"target": "central-american-independence", "verb": "FOLLOWS_FROM", "note": "Career built in aftermath of 1821 independence"}
        ]
    }),

    # 4 — George K. Kunowsky
    ("george-k-kunowsky", {
        "summary": (
            "Georg Karl Kunowsky (1786–1846) was a "
            "German astronomer and legal official whose "
            "astronomical observations contributed to "
            "early nineteenth-century celestial mechanics — "
            "particularly his independent discovery "
            "of Encke's Comet (the comet that German "
            "astronomer Johann Franz Encke would "
            "later calculate the orbit of and identify "
            "as a short-period comet, demonstrating "
            "the existence of non-parabolic cometary "
            "orbits). Kunowsky was a Berlin-based "
            "amateur astronomer whose careful observations "
            "intersected with the professional "
            "astronomical work of his era.\n\n"
            "Kunowsky held a position in the Prussian "
            "legal administration — a pattern common "
            "among early nineteenth-century German "
            "astronomers who combined professional "
            "careers in law, medicine, or government "
            "with serious scientific observation. "
            "His telescope and observational skills "
            "were sufficient to detect cometary "
            "appearances that professional observatories "
            "were simultaneously tracking.\n\n"
            "His independent observation of what became "
            "known as Encke's Comet — the comet with "
            "the shortest known orbital period (3.3 years) "
            "— contributed to the data pool from which "
            "Encke constructed his landmark orbital "
            "calculations. The identification of Encke's "
            "Comet as a periodic comet with a short "
            "orbit (the second periodic comet identified "
            "after Halley's) was a landmark in cometary "
            "astronomy.\n\n"
            "His career exemplified the German tradition "
            "of serious amateur astronomy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "German astronomer and Prussian legal official who independently observed what became Encke's Comet; Berlin-based amateur astronomer whose careful observations contributed to the data underpinning Encke's landmark orbital calculations identifying the second known periodic comet; exemplar of the serious German amateur astronomical tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The proliferation of telescope technology in the early nineteenth century — making quality instruments available to serious amateurs as well as professional observatories — enabled Kunowsky to conduct the systematic sky surveys that allowed him to independently observe the comet that Encke would calculate the orbit of",
            "The German culture of serious amateur science — in which government officials, physicians, lawyers, and clergy pursued rigorous scientific observation alongside their professional careers — created the social environment in which Kunowsky's astronomical hobby could achieve scientifically significant results",
            "The early nineteenth century's focus on cometary astronomy — driven by the success of Halley's Comet predictions and the active search for additional periodic comets — made systematic comet observation a priority that drew both professional and amateur astronomers into competitive sky sweeps"
        ],
        "effects": [
            "His independent observation of Encke's Comet contributed to the dataset from which Encke calculated the short orbital period that identified it as the second known periodic comet — a landmark in cometary astronomy that demonstrated the existence of comets with very short orbital periods bound tightly within the inner solar system",
            "His career contributed to the German tradition of productive amateur astronomy — demonstrating that systematic observations from private observatories could make scientifically meaningful contributions to professional astronomy",
            "The identification of Encke's Comet's short orbital period eventually contributed to understanding of the inner solar system's structure — and Encke's Comet later became important in the study of the Taurid meteor stream and debates about near-Earth object populations",
            "His example of combining Prussian legal administration with serious astronomical observation illustrated the breadth of German scientific culture — in which the same educated professional class that ran the state also conducted the science"
        ],
        "relationships": [
            {"target": "enckes-comet", "verb": "OBSERVES", "note": "Independent observer of the comet Encke calculated the orbit of"},
            {"target": "johann-franz-encke", "verb": "CONTRIBUTES_DATA_TO", "note": "His observations complemented Encke's orbital calculations"},
            {"target": "prussian-astronomy", "verb": "CONTRIBUTES_TO", "note": "Berlin-based amateur astronomer"},
            {"target": "berlin", "verb": "PRACTICES_IN", "note": "Berlin-based astronomer and legal official"},
            {"target": "cometary-astronomy", "verb": "ADVANCES", "note": "Observer contributing to early periodic comet identification"}
        ]
    }),

    # 5 — José Santiago Bueso
    ("josé-santiago-bueso", {
        "summary": (
            "José Santiago Bueso (1780–1852) was a "
            "Honduran lawyer and politician who served "
            "as President of Honduras (1852) — a "
            "brief tenure during the chronically "
            "unstable post-independence period when "
            "Honduras was cycling through executives "
            "at a rate that reflected the absence "
            "of stable constitutional governance. "
            "His career was embedded in the "
            "conservative political tradition that "
            "competed with liberal federalist movements "
            "for control of the Central American "
            "republics in the 1830s–1850s.\n\n"
            "Honduras after the collapse of the "
            "Central American Federation (1838–1839) "
            "experienced rapid turnover of political "
            "leadership — caudillos, lawyers, and "
            "military commanders succeeded one another "
            "in rapid succession as factional conflict, "
            "foreign intervention, and the absence "
            "of strong institutional structures "
            "prevented stable governance. Bueso "
            "was one of numerous figures who held "
            "executive authority briefly during "
            "this turbulent period.\n\n"
            "His legal training gave him professional "
            "credentials that distinguished him from "
            "purely military caudillos — he represented "
            "the emerging class of trained lawyers "
            "who sought to build civilian governmental "
            "institutions in the post-independence "
            "Central American states.\n\n"
            "His brief presidency in 1852 came "
            "as Honduras struggled to establish "
            "stable governance amid the chronic "
            "regional conflicts and internal "
            "factional divisions that characterized "
            "Central American politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "President of Honduras (1852) during the chronically unstable post-federation period; Honduran lawyer and politician representative of the civilian professional class that sought to build stable constitutional governance in post-independence Central America.",
            "significanceCategory": "local"
        },
        "causes": [
            "The collapse of the Central American Federation (1838–1839) and the subsequent fragmentation of Central America into five competing republics — each experiencing rapid executive turnover, factional conflict, and the absence of stable institutional frameworks — created the political environment in which figures like Bueso held executive power briefly before being displaced",
            "Honduras's chronic political instability in the 1840s–1850s — driven by competition between conservative and liberal factions, military caudillos, and external interference from neighboring republics — produced the rapid succession of executives that brought Bueso to power in 1852",
            "The emergence of a professional legal class in post-independence Central America — trained lawyers who sought to establish civilian constitutional governance as an alternative to military caudillismo — provided the political type that Bueso represented as a lawyer-politician seeking executive authority"
        ],
        "effects": [
            "His brief presidency contributed to the continuity of Honduran executive authority during a period of rapid leadership transition — maintaining the formal functioning of the state even as political instability prevented sustained policy development",
            "His tenure illustrated the pattern of civilian lawyer-politicians attempting to exercise executive authority in Central American states where military caudillos like Francisco Ferrera ultimately dominated — a competition between civilian and military approaches to governance that shaped Central American political development",
            "His career as a Honduran lawyer-politician contributed to the development of the legal profession and civilian political institutions in a country where such institutions were fragile and frequently displaced by military force",
            "His story — a brief president in a period of chronic instability — was representative of the wider Central American experience of multiple executive tenures and frequent political transitions that reflected the absence of consolidated state power"
        ],
        "relationships": [
            {"target": "honduras", "verb": "GOVERNS", "note": "President of Honduras 1852"},
            {"target": "central-american-federation", "verb": "SUCCEEDS_AFTER", "note": "Post-federation Honduran politician"},
            {"target": "francisco-ferrera", "verb": "CONTEMPORANEOUS_WITH", "note": "Fellow Honduran political figure of the same era"},
            {"target": "honduran-conservative-party", "verb": "MEMBER_OF", "note": "Conservative political tradition in post-independence Honduras"},
            {"target": "central-american-independence", "verb": "FOLLOWS_FROM", "note": "Career built in aftermath of 1821 independence"}
        ]
    }),

    # 6 — Pierre-Stanislas Bédard
    ("pierre-stanislas-bédard", {
        "summary": (
            "Pierre-Stanislas Bédard (1762–1829) was a "
            "Canadian lawyer, judge, journalist, and "
            "politician who became one of the most "
            "important figures in early French-Canadian "
            "constitutional and journalistic history. "
            "Founder of Le Canadien — the first French-language "
            "political newspaper in Canada (1806) — "
            "and a leader of the Parti canadien in "
            "the Legislative Assembly of Lower Canada, "
            "he championed responsible government "
            "and French-Canadian political rights "
            "against British colonial administration "
            "decades before these goals were achieved.\n\n"
            "Born in Charlesbourg (Quebec), Bédard "
            "trained as a lawyer and entered the "
            "Legislative Assembly of Lower Canada, "
            "where he quickly became the intellectual "
            "leader of the Parti canadien — the "
            "assembly-based movement that sought "
            "to assert the elected assembly's "
            "authority over the appointed executive "
            "council and advance French-Canadian "
            "cultural and political rights within "
            "the British constitutional framework.\n\n"
            "His founding of Le Canadien in 1806 "
            "gave the Parti canadien a political "
            "voice that could reach a popular "
            "audience — the newspaper became a "
            "vehicle for constitutional argument "
            "and political mobilization. In 1810, "
            "British Governor James Craig shut down "
            "the paper and imprisoned Bédard without "
            "trial — an act that made Bédard a "
            "martyr for press freedom and responsible "
            "government.\n\n"
            "He later served as a judge of the "
            "Superior Court of Lower Canada."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Canadian lawyer, judge, and journalist who founded Le Canadien (1806) — the first French-language political newspaper in Canada; leader of the Parti canadien in Lower Canada's Assembly; championed responsible government and French-Canadian rights; imprisoned without trial in 1810 by Governor Craig, becoming a martyr for press freedom; intellectual forerunner of the 1837 Rebellion.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Constitutional Act of 1791 — which created a Legislative Assembly in Lower Canada with an elected majority — gave French Canadians a constitutional arena within which to assert political authority against the British-appointed executive council, creating the institutional foundation for the Parti canadien's constitutional campaign",
            "The British colonial administration's systematic subordination of the elected Assembly to the appointed executive and legislative councils — denying responsible government and treating French-Canadian political claims with contempt — motivated Bédard's constitutional argument that the Assembly should control public finance and executive accountability",
            "The Napoleonic Wars' disruption of the transatlantic relationship — which made Britain politically sensitive to colonial loyalty and thus more willing to deploy repressive measures against colonial critics like Bédard — contributed to Governor Craig's decision to suppress Le Canadien and imprison Bédard in 1810"
        ],
        "effects": [
            "His founding of Le Canadien (1806) established French-language political journalism in Canada — creating a media platform for French-Canadian political argument that inspired subsequent generations of French-Canadian journalists and helped sustain the political consciousness that eventually produced the Patriotes movement",
            "His imprisonment without trial in 1810 — and his principled refusal of offers of release conditioned on abandoning politics — made him a symbol of press freedom and the injustice of colonial governance, galvanizing French-Canadian political opinion and strengthening the Parti canadien",
            "His constitutional arguments for responsible government — that the executive must be accountable to the elected assembly — anticipated the arguments that led to the achievement of responsible government in Canada in 1848, making him an intellectual forerunner of Canada's constitutional development",
            "His career helped establish the Parti canadien as the first organized French-Canadian political movement, laying the groundwork for the Patriotes movement of the 1830s and the constitutional struggles that culminated in the Rebellion of 1837–1838"
        ],
        "relationships": [
            {"target": "le-canadien", "verb": "FOUNDS", "note": "First French-language political newspaper in Canada (1806)"},
            {"target": "parti-canadien", "verb": "LEADS", "note": "Leader of the French-Canadian assembly movement"},
            {"target": "lower-canada-legislative-assembly", "verb": "SERVES_IN", "note": "Member of the elected Assembly of Lower Canada"},
            {"target": "james-craig", "verb": "IMPRISONED_BY", "note": "Imprisoned without trial by British Governor Craig in 1810"},
            {"target": "responsible-government-canada", "verb": "CHAMPIONS", "note": "Early advocate for executive accountability to elected assembly"}
        ]
    }),

    # 7 — William Duhurst Merrick
    ("william-duhurst-merrick", {
        "summary": (
            "William Duhurst Merrick (1793–1857) was an "
            "American lawyer and Whig politician from "
            "Maryland who served in the United States "
            "Senate (1838–1845), representing Maryland's "
            "Whig tradition during the pivotal years "
            "of the Tyler presidency and the congressional "
            "battles over banking, tariffs, and "
            "the emerging sectional conflict. A "
            "member of Maryland's established legal "
            "and political class, Merrick served "
            "during one of the most turbulent "
            "periods in antebellum political history.\n\n"
            "Merrick was born into a Maryland family "
            "with legal and political connections "
            "and built a successful law practice "
            "before entering the Senate. His Whig "
            "affiliation placed him in the party "
            "that had united behind Henry Clay's "
            "American System — protective tariffs, "
            "a national bank, and federal internal "
            "improvements — in opposition to Jacksonian "
            "Democratic states'-rights policies.\n\n"
            "His Senate service (1838–1845) coincided "
            "with the extraordinary political drama "
            "of John Tyler's presidency (1841–1845) "
            "— Tyler vetoed the Whig Party's signature "
            "banking legislation, was expelled from "
            "the party, and paralyzed the Whig "
            "legislative agenda. Merrick was "
            "among the Senate Whigs navigating "
            "this crisis of party loyalty and "
            "constitutional conflict.\n\n"
            "His Maryland legal career before and "
            "after his Senate service made him "
            "a significant figure in the state's "
            "antebellum bar."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Whig Senator (1838–1845) who served during the Tyler presidency crisis; Henry Clay Whig representing Maryland's interests in the Senate debates over banking, tariffs, and the American System; practiced law in Maryland before and after his Senate service.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Whig Party's rise as the principal opposition to Jacksonian Democracy — built around Henry Clay's American System and the coalition of northeastern manufacturers, western infrastructure advocates, and Southern conservatives — created the partisan framework within which Merrick's Senate career operated",
            "Maryland's economic position as a border state with significant commercial interests in both Northern manufacturing and Southern agriculture — and its strategic location between the North and South — made its Senate representation politically significant and shaped Merrick's navigation of sectional issues",
            "The John Tyler constitutional crisis (1841–1845) — in which the Whig president vetoed the party's banking legislation and was expelled from the party — created the political turmoil that defined Merrick's Senate service and tested the loyalty and constitutional principles of every Whig Senator"
        ],
        "effects": [
            "His Senate votes during the Tyler crisis contributed to the record of Whig resistance to Tyler's bank vetoes — documenting the Whig Party's unsuccessful struggle to implement the American System against a renegade president of their own party",
            "His representation of Maryland in the Senate during the 1838–1845 period helped articulate Maryland's interests in federal economic policy — particularly regarding tariff rates critical to Baltimore's commercial economy and the balance between Northern manufacturing and Southern agricultural interests",
            "His career illustrated the political dilemmas of border-state Whiggery — pulled between the party's Northern manufacturing wing and the Southern planter class that shared many Maryland interests — dilemmas that would intensify as slavery moved to the center of American political debate",
            "His post-Senate legal career contributed to Maryland's antebellum legal culture, as former senators with federal experience often brought valuable constitutional and legislative expertise back to their state bars"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maryland Senator 1838–1845"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Henry Clay Whig in the Senate"},
            {"target": "john-tyler", "verb": "OPPOSES", "note": "Whig Senator opposed to Tyler's bank vetoes"},
            {"target": "maryland", "verb": "REPRESENTS", "note": "Maryland Whig Senator"},
            {"target": "american-system-henry-clay", "verb": "SUPPORTS", "note": "Whig advocate for protective tariffs and national banking"}
        ]
    }),

    # 8 — Eli P. Ashmun
    ("eli-p-ashmun", {
        "summary": (
            "Eli P. Ashmun (1770–1819) was an American "
            "lawyer and Democratic-Republican politician "
            "from Massachusetts who served in the United "
            "States Senate (1816–1819) and in the "
            "U.S. House of Representatives, representing "
            "the political culture of western Massachusetts "
            "during the Era of Good Feelings. His "
            "Senate career was brief — he died in office "
            "in 1819 — but it placed him in the "
            "Senate during the final years of the "
            "first American party system and the "
            "beginning of the great political realignment "
            "that would reshape American party politics "
            "in the 1820s.\n\n"
            "Ashmun was born and educated in Massachusetts, "
            "where he built a legal career and became "
            "involved in Democratic-Republican politics. "
            "He served in the Massachusetts state "
            "legislature before winning his Congressional "
            "and Senate seats. His western Massachusetts "
            "constituency represented the agricultural "
            "hinterland of a state that was rapidly "
            "industrializing — a region with different "
            "economic interests from Boston's commercial "
            "and manufacturing elite.\n\n"
            "The Era of Good Feelings (roughly 1816–1820) "
            "during which he served was a period of "
            "unusual political consensus — the Federalist "
            "Party had collapsed after the Hartford "
            "Convention's perceived disloyalty during "
            "the War of 1812, leaving the Democratic-Republicans "
            "without organized opposition. Ashmun's "
            "Senate service embodied this moment of "
            "political calm before the storm of "
            "the 1824 election that shattered the "
            "Democratic-Republican consensus.\n\n"
            "His father Jehudi Ashmun later became "
            "a founder of Liberia."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Massachusetts Democratic-Republican Senator (1816–1819) who served during the Era of Good Feelings; died in office; father of Jehudi Ashmun, a founder of Liberia; represented western Massachusetts agricultural interests in the final years of the first party system.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Era of Good Feelings and the collapse of the Federalist Party after the Hartford Convention's perceived disloyalty during the War of 1812 — which left the Democratic-Republicans without organized opposition — created the unusual political environment in which Ashmun served as an essentially uncontested party member in the Senate",
            "Western Massachusetts's agricultural political culture — distinct from Boston's commercial and manufacturing elite — shaped Ashmun's political identity and the regional interests he represented in the Massachusetts legislature and Senate",
            "The War of 1812 and its aftermath — including the establishment of American manufacturing capacity to replace British goods blocked by the war — shaped the economic debates of Ashmun's Senate years and the emerging question of tariff protection for American industry"
        ],
        "effects": [
            "His Senate service contributed the perspective of western Massachusetts agricultural interests to the debates of the Era of Good Feelings — a period when national policy on tariffs, banking, and internal improvements was being actively constructed with long-term consequences",
            "His death in office in 1819 created a Senate vacancy that contributed to the Massachusetts political succession — the appointment or election of a replacement at a moment when the Era of Good Feelings was about to give way to the factional competition of the 1820s",
            "His son Jehudi Ashmun's later career as a key figure in the founding of Liberia — the American Colonization Society's West African settlement for freed slaves — gave the Ashmun family legacy an unexpected historical dimension extending beyond Eli's own Senate service",
            "His career illustrated the political sociology of the Era of Good Feelings — when the absence of organized partisan competition meant that political careers were built on personal reputation, legal standing, and local networks rather than party organization"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Massachusetts Senator 1816–1819"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democrat-Republican"},
            {"target": "massachusetts", "verb": "REPRESENTS", "note": "Western Massachusetts Senator"},
            {"target": "jehudi-ashmun", "verb": "PARENT_OF", "note": "Father of the founder of Liberia"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Senator during the period of Federalist collapse and one-party dominance"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 55 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
