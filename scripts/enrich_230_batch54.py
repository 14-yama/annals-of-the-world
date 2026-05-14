#!/usr/bin/env python3
"""
Batch 54 — 8 entities: Cândido José de Araújo Viana (Marquis of Sapucaí),
Nicolas Catinat, Nathan Cutler, Patrick Noble, Andrés Narvarte,
Buckner Stith Morris, Pierre Daubenton, György Mailáth
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

    # 1 — Cândido José de Araújo Viana, Marquis of Sapucaí
    ("cândido-josé-de-araújo-viana-marquis-of-sapucaí", {
        "summary": (
            "Cândido José de Araújo Viana, Marquis of "
            "Sapucaí (1793–1875), was a Brazilian statesman, "
            "senator, and Conservative Party leader who "
            "served as one of the most important political "
            "figures of the Brazilian Empire under Pedro II. "
            "Repeatedly a cabinet minister and president "
            "of the Council of Ministers (prime minister), "
            "he was a pillar of the Conservative establishment "
            "that governed Brazil through the system "
            "of rotismo — the alternating Conservative "
            "and Liberal governments overseen by the "
            "emperor's moderating power.\n\n"
            "Born in Minas Gerais and educated at Coimbra, "
            "Araújo Viana returned to Brazil with a "
            "law degree and entered political life during "
            "the turbulent period of Pedro I's reign "
            "and the Regency (1831–1840). He emerged "
            "as a Conservative leader during the consolidation "
            "of Pedro II's personal reign — the reign "
            "that stabilized Brazil after the revolutionary "
            "threats of the Regency period — and became "
            "one of the emperor's most trusted advisers.\n\n"
            "As president of the Council of Ministers, "
            "he directed Brazilian policy on the great "
            "questions of the Second Empire: fiscal "
            "management, infrastructure development, "
            "provincial administration, and the gradual "
            "management of the slavery question. His "
            "Conservative approach favored stability "
            "over rapid reform, centralizing authority "
            "against provincial challenges.\n\n"
            "The marquessate of Sapucaí — granted by "
            "Pedro II as recognition of his long service "
            "— was among the most distinguished titles "
            "of the Brazilian imperial nobility, cementing "
            "his place as a founding figure of the "
            "Conservative order."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Brazilian Conservative Party statesman and Marquis of Sapucaí who served as president of the Council of Ministers and senator during Pedro II's reign; pillar of the imperial Conservative establishment and one of the most trusted political figures of the Brazilian Empire; educated at Coimbra, formed in the Conservative tradition of imperial stability.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pedro II's establishment of the rotismo system — in which Conservative and Liberal governments alternated under the emperor's moderating power — created the political framework within which Araújo Viana rose to become the principal leader of the Conservative faction that governed Brazil through extended ministerial tenures",
            "The post-Regency consolidation of the Brazilian Empire under Pedro II — which required experienced, reliable statesmen to build stable institutions after the revolutionary turbulence of the 1831–1840 Regency period — made Araújo Viana's legal training, political loyalty, and administrative capacity essential assets that the emperor rewarded with repeated ministerial appointments",
            "Brazil's emergence as an independent empire under the House of Braganza — requiring the construction of a distinctive Brazilian political class educated at European universities who could run a sovereign government — shaped Araújo Viana's trajectory from Coimbra law student to imperial senator and prime minister"
        ],
        "effects": [
            "His repeated service as president of the Council of Ministers shaped Brazilian policy on fiscal administration, provincial governance, and the maintenance of the imperial constitutional order during the crucial mid-nineteenth century decades when Brazil established itself as a stable constitutional monarchy",
            "His leadership of the Conservative Party helped define Brazilian Conservatism as a governing philosophy emphasizing centralization, institutional stability, and gradual managed change — in contrast to the Liberal Party's more decentralizing impulses",
            "His senatorial career contributed to the Brazilian Senate's role as the Conservative bulwark of the imperial order — the institution from which experienced politicians provided continuity and checked the volatility of lower house politics",
            "His elevation to the Marquessate of Sapucaí represented the Brazilian imperial system's capacity to create a native aristocracy of merit and service — Brazilian-born statesmen honored with titles that gave the Empire the social hierarchy of a European monarchy"
        ],
        "relationships": [
            {"target": "pedro-ii-of-brazil", "verb": "SERVES_UNDER", "note": "Trusted Conservative statesman and repeated minister under Pedro II"},
            {"target": "brazilian-conservative-party", "verb": "LEADS", "note": "Leader of Conservative Party in imperial Brazil"},
            {"target": "council-of-ministers-brazil", "verb": "PRESIDES_OVER", "note": "President of the Council of Ministers (prime minister)"},
            {"target": "senate-of-brazil", "verb": "SERVES_IN", "note": "Imperial senator for life"},
            {"target": "brazilian-empire", "verb": "SERVES", "note": "Pillar of Conservative imperial establishment"}
        ]
    }),

    # 2 — Nicolas Catinat
    ("nicolas-catinat", {
        "summary": (
            "Nicolas Catinat (1637–1712) was a French "
            "military commander who rose from humble "
            "origins to become one of Louis XIV's most "
            "capable marshals — remarkable in an era "
            "when the highest military commands were "
            "almost exclusively the preserve of the "
            "great aristocratic houses. Self-made and "
            "professionally talented, he is remembered "
            "for his victories in Savoy and Italy during "
            "the Nine Years' War (1688–1697) and for his "
            "personal probity — a contrast to the "
            "court-connected generals who surrounded him.\n\n"
            "Born to a bourgeois Parisian family (his "
            "father was an attorney), Catinat began his "
            "military career as a private soldier — "
            "an exceptional origin for someone who would "
            "attain a marshal's baton. His military "
            "talent rapidly brought him to the attention "
            "of Louvois, Louis XIV's great war minister, "
            "who promoted him through the ranks on merit.\n\n"
            "His greatest triumphs came in the Alpine "
            "theater: his victories at Staffarda (1690) "
            "and Marsaglia (1693) against the Duke of "
            "Savoy secured French dominance over the "
            "western Alpine passes and protected "
            "France's southeastern frontier during "
            "the Nine Years' War. He was promoted to "
            "Marshal of France in 1693.\n\n"
            "In the War of the Spanish Succession he was "
            "outmaneuvered by Prince Eugene of Savoy "
            "at Carpi and Chiari (1701) — a defeat "
            "that ended his active command, though "
            "his earlier record secured his historical "
            "reputation as one of the most capable "
            "commanders of Louis XIV's wars."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Marshal under Louis XIV who rose from bourgeois origins to command armies — exceptional in an aristocratic military culture; victories at Staffarda (1690) and Marsaglia (1693) secured French control of the Alpine frontier during the Nine Years' War; promoted to Marshal of France 1693; known for personal probity in contrast to court-connected rivals.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Louis XIV's systematic transformation of the French army under Louvois — which professionalized military command, standardized training and logistics, and created space for talented officers of non-noble origin to rise through demonstrated competence — allowed Catinat to advance from private soldier to marshal on pure military merit",
            "The Nine Years' War (1688–1697) and its Italian/Alpine theater — where France faced the Duke of Savoy as a major opponent threatening its southeastern frontier — created the military context in which Catinat's particular skills of mountain warfare, siege management, and combined arms operations could win decisive victories",
            "France's strategic need to secure the Alpine passes against Savoyard and Habsburg attack — protecting Provence and the southeastern frontier from invasion — made Catinat's Italian campaigns strategically vital, earning him the marshal's baton that his bourgeois origins would otherwise have made nearly unattainable"
        ],
        "effects": [
            "His victories at Staffarda (1690) and Marsaglia (1693) secured French control over Savoy and the western Alpine frontier, protecting France's southeastern flank during the Nine Years' War and demonstrating that French military power could project effectively into the Italian theater",
            "His Marshal of France promotion (1693) established a precedent — however limited — that professional military talent could earn the highest French military honors regardless of birth, in an era when aristocratic blood was normally required for the highest commands",
            "His defeat by Prince Eugene at Carpi and Chiari (1701) contributed to the early French reverses in the War of the Spanish Succession that ultimately required the great commanders of the next generation — Villars, Vendôme — to rescue French arms",
            "His personal reputation for probity and simplicity — an officer who neither sought court favor nor enriched himself from military service — made him a figure of admiration among military historians as the antithesis of the corrupt court generals of the Ancien Régime"
        ],
        "relationships": [
            {"target": "louis-xiv", "verb": "SERVES_UNDER", "note": "Marshal under the Sun King"},
            {"target": "nine-years-war", "verb": "COMMANDS_IN", "note": "Led French forces in Alpine theater 1688–1697"},
            {"target": "battle-of-staffarda-1690", "verb": "WINS", "note": "Victory over Duke of Savoy securing Alpine frontier"},
            {"target": "battle-of-marsaglia-1693", "verb": "WINS", "note": "Decisive French victory over Savoyard-Allied army"},
            {"target": "prince-eugene-of-savoy", "verb": "DEFEATED_BY", "note": "Lost at Carpi and Chiari 1701 ending his active command"}
        ]
    }),

    # 3 — Nathan Cutler
    ("nathan-cutler", {
        "summary": (
            "Nathan Cutler (1775–1861) was an American "
            "politician from Maine who served as Acting "
            "Governor of Maine (1829–1830) and as a "
            "Democratic politician in a state whose "
            "early political culture was shaped by its "
            "recent separation from Massachusetts (1820) "
            "and by the dynamics of the Jacksonian "
            "Democratic revolution. His brief governorship "
            "came at a moment of transition in Maine "
            "politics as the Era of Good Feelings "
            "collapsed into the competitive Jacksonian "
            "two-party system.\n\n"
            "Maine had achieved statehood in 1820 as "
            "part of the Missouri Compromise — its "
            "admission as a free state balancing "
            "Missouri's admission as a slave state "
            "— making it one of the youngest states "
            "in the Union at the time of Cutler's "
            "political career. Maine's early governance "
            "was characterized by the transition "
            "from Massachusetts-era institutions to "
            "distinctly Maine political identity.\n\n"
            "Cutler's acting governorship (1829–1830) "
            "came through his position as president "
            "of the Maine Senate — he succeeded to "
            "the governorship when elected Governor "
            "Enoch Lincoln died in office. His brief "
            "tenure managed the ordinary business "
            "of state government during a period of "
            "rapid Maine population growth and economic "
            "development driven by the timber and "
            "maritime industries.\n\n"
            "His political career illustrated the "
            "pattern of Maine's early state politicians: "
            "local professional men who built careers "
            "in state legislative service and rose "
            "through the constitutional succession "
            "rather than electoral landslides."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Acting Governor of Maine (1829–1830) who succeeded to the governorship upon the death of Governor Enoch Lincoln; Democratic politician in one of America's newest states; his brief tenure illustrated the constitutional succession mechanisms of early American state governance.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maine's achievement of statehood in 1820 as part of the Missouri Compromise — separating from Massachusetts to provide a free-state counterbalance to Missouri's slave-state admission — created the new political environment in which Cutler built his career as an early Maine state politician",
            "Governor Enoch Lincoln's death in office in 1829 — activating the constitutional succession that elevated Cutler from Maine Senate president to acting governor — was the direct proximate cause of Cutler's brief gubernatorial tenure",
            "The Jacksonian Democratic political revolution of 1828–1832 — which reorganized American party politics around Andrew Jackson's populist coalition — shaped the partisan environment of Cutler's political career as the Era of Good Feelings dissolved into competitive two-party politics"
        ],
        "effects": [
            "His acting governorship provided continuity in Maine's executive government during the sudden vacancy created by Lincoln's death, maintaining the stability of the new state's administrative functions during a period of rapid economic and population growth",
            "His constitutional succession from Senate president to governor demonstrated the functioning of Maine's new constitutional mechanisms — showing that the state's governance structures could manage unexpected transitions without political crisis",
            "His political career contributed to Maine's emerging Democratic Party organization in the Jacksonian era, helping build the partisan infrastructure that would make Maine a competitive two-party state through the antebellum decades",
            "His career as an early Maine state politician exemplified the type of locally-rooted professional politician who built state-level careers in America's newest states — men whose significance was primarily local but whose service was essential to the functioning of democratic state governance"
        ],
        "relationships": [
            {"target": "maine", "verb": "GOVERNS", "note": "Acting Governor of Maine 1829–1830"},
            {"target": "enoch-lincoln", "verb": "SUCCEEDS", "note": "Became acting governor upon Lincoln's death in office"},
            {"target": "maine-senate", "verb": "PRESIDES_OVER", "note": "President of the Maine Senate before succession"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Jacksonian Democrat in early Maine politics"},
            {"target": "missouri-compromise-1820", "verb": "BENEFITS_FROM", "note": "Maine statehood created by Missouri Compromise enabled his career"}
        ]
    }),

    # 4 — Patrick Noble
    ("patrick-noble", {
        "summary": (
            "Patrick Noble (1787–1840) was an American "
            "lawyer and Democratic politician who served "
            "as Governor of South Carolina (1838–1840) "
            "— dying in office from tuberculosis, making "
            "his governorship one of the shortest in "
            "South Carolina history. A member of one "
            "of South Carolina's prominent up-country "
            "planter families, Noble represented the "
            "Abbeville District — the western Carolina "
            "upcountry that had been a hotbed of "
            "nullification sentiment — during a "
            "period of post-Nullification Crisis "
            "consolidation in South Carolina politics.\n\n"
            "Noble studied law at South Carolina College "
            "(now the University of South Carolina) "
            "and was admitted to the bar, building "
            "a legal and planter career in Abbeville "
            "County. His political career began in "
            "the South Carolina state legislature, "
            "where he served before winning the "
            "governorship in 1838.\n\n"
            "His governorship came in the aftermath "
            "of the Nullification Crisis (1832–1833) "
            "— South Carolina's confrontation with "
            "the federal government over protective "
            "tariffs, which had nearly led to "
            "armed secession before Henry Clay's "
            "compromise tariff resolved the immediate "
            "crisis. The post-nullification period "
            "saw South Carolina's politics settle "
            "into a Southern Democratic consensus "
            "that stressed states' rights and the "
            "defense of slavery.\n\n"
            "His death in office in 1840 cut short "
            "a governorship that had barely begun, "
            "leaving his administration's full impact "
            "difficult to assess."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of South Carolina (1838–1840) who died in office from tuberculosis; Abbeville District planter-lawyer and Jacksonian Democrat governing in the post-Nullification Crisis era; representative of South Carolina's up-country planter political class.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's planter-lawyer political culture — in which the state's governing class combined large-scale slave agriculture with legal education and legislative service — shaped Noble's trajectory as an Abbeville County planter who built a political career through the South Carolina state legislature to the governorship",
            "The Nullification Crisis (1832–1833) and its aftermath — which left South Carolina with a hardened states'-rights political consensus and a Democratic Party identity built around the defense of slavery and opposition to federal tariff power — defined the political environment in which Noble governed as a post-nullification Democratic politician",
            "The South Carolina College network — through which the state's planter families educated their sons in law and the classics as preparation for political careers — connected Noble to the governing class that dominated South Carolina's antebellum political life"
        ],
        "effects": [
            "His death in office in 1840 created a sudden gubernatorial vacancy that activated South Carolina's constitutional succession — demonstrating the resilience of the state's governance mechanisms while ending a governorship that had barely begun to establish policy direction",
            "His brief governorship contributed to the post-Nullification Crisis consolidation of South Carolina's Southern Democratic identity — governing the state as it settled into the hardened pro-slavery, states'-rights political consensus that would characterize it through the Civil War",
            "His career represented the Abbeville District's importance in South Carolina politics — the upcountry's aggressive nullification tradition made its political leaders influential in the state's post-crisis Democratic establishment",
            "His story — a governor whose death in office cut short his administration — became a minor but poignant episode in South Carolina's antebellum political history, illustrating how tuberculosis and early death could abruptly end the careers of the planter class"
        ],
        "relationships": [
            {"target": "south-carolina", "verb": "GOVERNS", "note": "Governor of South Carolina 1838–1840"},
            {"target": "nullification-crisis", "verb": "GOVERNS_AFTER", "note": "Post-Nullification Crisis Democratic governor"},
            {"target": "south-carolina-legislature", "verb": "SERVES_IN", "note": "State legislator before winning governorship"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Jacksonian Democrat in South Carolina politics"},
            {"target": "abbeville-district-sc", "verb": "REPRESENTS", "note": "Planter-politician from the South Carolina upcountry"}
        ]
    }),

    # 5 — Andrés Narvarte
    ("andrés-narvarte", {
        "summary": (
            "Andrés Narvarte (1760–1830) was a Venezuelan "
            "ecclesiastic and educator who served as the "
            "Bishop of Mérida de Maracaibo — one of "
            "Venezuela's most important colonial and "
            "early republican dioceses — during the "
            "tumultuous period of Venezuelan independence "
            "and the wars of liberation. His episcopate "
            "spanned the critical transition from Spanish "
            "colonial rule to the Venezuelan Republic, "
            "making him a churchman who had to navigate "
            "between colonial ecclesiastical authority "
            "and the new republican order.\n\n"
            "Narvarte was born in Venezuela and received "
            "his ecclesiastical education and ordination "
            "within the colonial church hierarchy. "
            "His appointment as Bishop of Mérida gave "
            "him authority over a vast Andean diocese "
            "that encompassed the highland regions "
            "of western Venezuela — an area of strategic "
            "importance in the independence wars as "
            "royalist and patriot forces contested "
            "control of the Andes.\n\n"
            "During the independence period, the Venezuelan "
            "church was deeply divided between those "
            "who supported the royalist cause and those "
            "who accommodated or supported independence. "
            "Narvarte's position as a bishop during this "
            "transition required careful navigation "
            "of these competing loyalties — the church's "
            "institutional survival depended on its "
            "ability to adapt to the new republican "
            "political reality without destroying its "
            "colonial institutional inheritance.\n\n"
            "His educational interests contributed to "
            "the development of ecclesiastical institutions "
            "in the Andes region of Venezuela."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Venezuelan Bishop of Mérida de Maracaibo during the independence era; churchman who navigated the transition from colonial to republican authority in the Andean diocese; represents the ecclesiastical dimension of Venezuelan independence and the church's adaptation to the new republican order.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Venezuelan independence movement (1810–1821) and the wars of liberation — which shattered Spanish colonial authority and created a new republican state — forced the Venezuelan Catholic Church and its bishops like Narvarte to navigate between colonial loyalties and republican realities during a period of intense political violence",
            "The Spanish colonial church's deep integration into Venezuelan colonial society — through educational institutions, hospital networks, land tenure, and social authority — meant that bishops like Narvarte controlled institutions that were vital to both sides in the independence conflict",
            "The Mérida diocese's Andean location — in the highland regions where royalist and patriot forces repeatedly contested control — placed Narvarte at the intersection of military conflict and ecclesiastical administration, requiring him to manage his diocese under conditions of war"
        ],
        "effects": [
            "His episcopate contributed to the survival and continuity of the Catholic Church's institutional presence in western Venezuela through the independence wars — maintaining the diocese's administrative functions even as political authority shifted from Spanish colonial to Venezuelan republican hands",
            "His navigation of the colonial-to-republican transition helped establish the pattern by which the Venezuelan church adapted to the new political order — accommodating republican authority while preserving ecclesiastical independence and institutional continuity",
            "His educational contributions to the Mérida region — where the church's schools and seminaries were the primary educational institutions — helped maintain the cultural and intellectual infrastructure of the Andean highlands during the disruptions of the independence wars",
            "His career illustrated the difficult position of colonial churchmen during independence — loyal to an institution that straddled the divide between the old colonial order and the new republican reality, seeking institutional survival through careful navigation of political change"
        ],
        "relationships": [
            {"target": "diocese-of-merida-maracaibo", "verb": "LEADS", "note": "Bishop of Mérida de Maracaibo"},
            {"target": "venezuelan-independence", "verb": "LIVES_THROUGH", "note": "Bishop during the wars of Venezuelan independence"},
            {"target": "catholic-church-venezuela", "verb": "LEADS", "note": "Senior Catholic hierarch in western Venezuela"},
            {"target": "spanish-colonial-church", "verb": "TRANSITIONS_FROM", "note": "Colonial bishop adapting to republican order"},
            {"target": "venezuela", "verb": "SERVES_IN", "note": "Venezuelan ecclesiastic in Andean diocese"}
        ]
    }),

    # 6 — Buckner Stith Morris
    ("buckner-stith-morris", {
        "summary": (
            "Buckner Stith Morris (1800–1879) was an "
            "American lawyer and politician who served "
            "as Mayor of Chicago (1838–1839) — one of "
            "the earliest mayors of a city that had "
            "been incorporated only in 1837. His "
            "mayoralty came during Chicago's extraordinary "
            "initial growth phase, when the city was "
            "transforming from a frontier trading post "
            "into a major commercial hub anchored by "
            "its position at the southern tip of "
            "Lake Michigan and its connections to "
            "the interior via the Illinois and "
            "Michigan Canal.\n\n"
            "Morris was born in Kentucky and moved "
            "to Illinois as a young lawyer, settling "
            "in the rapidly growing town of Chicago "
            "where legal talent was scarce and "
            "opportunity abundant. Chicago had been "
            "incorporated as a town in 1833 and as "
            "a city in 1837 — Morris served as its "
            "second mayor, governing a city of only "
            "a few thousand residents that was already "
            "becoming one of the great speculative "
            "frontiers of Jacksonian America.\n\n"
            "The land speculation mania and the Panic "
            "of 1837 — one of the most severe "
            "depressions in American history — "
            "struck Chicago during Morris's "
            "mayoral term, devastating the speculative "
            "property market that had been driving "
            "the city's explosive growth. His "
            "administration had to manage Chicago's "
            "civic institutions through the economic "
            "collapse.\n\n"
            "His later legal career in Chicago made "
            "him a figure in the city's antebellum "
            "bar."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Second Mayor of Chicago (1838–1839) during the city's initial incorporation period; Whig lawyer who governed a frontier boomtown of a few thousand residents that would become America's fastest-growing city; administered Chicago through the Panic of 1837's economic devastation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Chicago's incorporation as a city in 1837 — the product of the extraordinary land speculation boom that saw the settlement at the southern tip of Lake Michigan transform from a frontier fort into a speculative real estate market in less than a decade — created the new municipal government that Morris was elected to lead as its second mayor",
            "The Panic of 1837 — triggered by Jacksonian banking and credit policies and the withdrawal of British capital from American land speculation — struck Chicago with particular severity as the speculative boom that had driven the city's explosive growth instantly collapsed, requiring Morris's administration to manage economic crisis in a barely-established city",
            "The Illinois and Michigan Canal project — which promised to connect Lake Michigan to the Illinois River and thus the entire Mississippi Valley, making Chicago the great commercial gateway between the Great Lakes and the interior — was the infrastructure investment that drove Chicago's growth and shaped the commercial ambitions that Morris's mayoral administration served"
        ],
        "effects": [
            "His mayoral administration contributed to the establishment of Chicago's initial civic institutions — building the administrative framework, public order mechanisms, and governance structures that a newly incorporated city required even in the depths of an economic depression",
            "His governance through the Panic of 1837 helped Chicago survive its first major economic crisis — demonstrating that the new city's municipal institutions could function through severe economic disruption and maintain the basic civic services a growing population required",
            "His career as an early Chicago mayor placed him among the founding civic figures of what would become America's second-largest city — men who built municipal government for a frontier boomtown that few in 1838 could have imagined growing to the metropolis it became",
            "His post-mayoral legal career contributed to the development of Chicago's antebellum legal profession — a bar that grew rapidly alongside the city's commercial economy and whose members were essential to the property transactions, commercial disputes, and corporate formations that Chicago's growth generated"
        ],
        "relationships": [
            {"target": "chicago", "verb": "GOVERNS", "note": "Second Mayor of Chicago 1838–1839"},
            {"target": "panic-of-1837", "verb": "GOVERNS_DURING", "note": "Mayor during the severe economic depression that struck Chicago"},
            {"target": "illinois-michigan-canal", "verb": "SUPPORTS", "note": "Mayor during the canal project that drove Chicago's growth"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Whig politician in Jacksonian-era Chicago"},
            {"target": "illinois", "verb": "SERVES", "note": "Kentucky-born lawyer who settled in Illinois frontier"}
        ]
    }),

    # 7 — Pierre Daubenton
    ("pierre-daubenton", {
        "summary": (
            "Pierre Daubenton (1703–1776) was a French "
            "Jesuit theologian and controversialist who "
            "became known for his theological writings "
            "during the period of the Jesuit Order's "
            "peak influence and subsequent suppression "
            "in France. He was the brother of the "
            "naturalist Louis-Jean-Marie Daubenton — "
            "collaborator of Buffon on the great "
            "Histoire naturelle — making him a member "
            "of one of France's most scientifically "
            "distinguished families, though his own "
            "work lay entirely in the theological sphere.\n\n"
            "Pierre Daubenton was born in Montbard "
            "(Burgundy) — the same town that produced "
            "the naturalist Buffon — into a family "
            "that would contribute both religious and "
            "scientific figures to French intellectual "
            "life. He entered the Society of Jesus "
            "and pursued a theological and preaching "
            "career within the order.\n\n"
            "His theological writings were part of "
            "the Jesuit intellectual tradition that "
            "defended the Society's approach to "
            "moral theology, casuistry, and religious "
            "controversy — positions that made the "
            "Jesuits targets of both Jansenist "
            "criticism and Enlightenment anticlericalism. "
            "The suppression of the Jesuits in France "
            "(1762) — driven by philosophical, political, "
            "and ecclesiastical opponents — ended "
            "his order's institutional life in France "
            "and affected the context of his later career.\n\n"
            "His family connection to Louis-Jean-Marie "
            "Daubenton places him in the broader "
            "intellectual world of Enlightenment France."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "French Jesuit theologian and controversialist; brother of naturalist Louis-Jean-Marie Daubenton (Buffon's collaborator); member of a family that produced both religious and scientific intellectual figures; his career encompassed the period of Jesuit peak influence and the Suppression in France (1762).",
            "significanceCategory": "local"
        },
        "causes": [
            "The Society of Jesus's institutional structure — which trained its members in theology, rhetoric, and philosophical controversy as weapons in the Church's intellectual defense against heresy and skepticism — shaped Pierre Daubenton as a theological controversialist whose work served the order's apologetic mission",
            "The Jansenist-Jesuit controversy that consumed much of French theological debate in the seventeenth and early eighteenth centuries — a bitter dispute over grace, free will, and moral theology that polarized the French church — provided the polemical context in which Daubenton's theological writings engaged",
            "The Enlightenment's growing anticlericalism and the political attacks on the Jesuits orchestrated by philosophes, Jansenists, and Gallican lawyers in the 1750s–1760s — which culminated in the French Suppression of the Jesuits in 1762 — defined the institutional threat that shaped the last phase of Daubenton's Jesuit career"
        ],
        "effects": [
            "His theological writings contributed to the Jesuit intellectual tradition of moral theology and controversialist apologetics — a tradition that defended the Society's approaches to casuistry, probabilism, and the accommodation of Christian practice to worldly life",
            "His family connection to his brother Louis-Jean-Marie Daubenton — Buffon's principal collaborator and one of the founders of comparative anatomy — placed Pierre within a family whose total intellectual output spanned both religious controversy and natural science, illustrating the breadth of French Enlightenment intellectual culture",
            "The Suppression of the Jesuits in France (1762) that affected Daubenton's order was a landmark event in the decline of traditional religious authority in France — one step in the long process by which the Church's institutional power was reduced before the Revolution eliminated it entirely",
            "His career illustrated the parallel intellectual worlds of Enlightenment France — where the same family could produce a Jesuit controversialist defending traditional theology and a naturalist collaborating on the great secular natural history that was itself a challenge to received religious accounts of nature"
        ],
        "relationships": [
            {"target": "louis-jean-marie-daubenton", "verb": "SIBLING_OF", "note": "Brother of Buffon's naturalist collaborator"},
            {"target": "society-of-jesus", "verb": "MEMBER_OF", "note": "Jesuit theologian and controversialist"},
            {"target": "suppression-of-jesuits-france-1762", "verb": "AFFECTED_BY", "note": "Jesuit whose order was suppressed in France"},
            {"target": "jansenist-jesuit-controversy", "verb": "PARTICIPATES_IN", "note": "Theological controversialist in Jansenist-Jesuit debates"},
            {"target": "french-catholic-church", "verb": "SERVES", "note": "Jesuit preacher and theologian in French church"}
        ]
    }),

    # 8 — György Mailáth
    ("györgy-mailáth", {
        "summary": (
            "György Mailáth (1786–1861) was a Hungarian "
            "nobleman, historian, and literary figure "
            "who contributed to the early development "
            "of Hungarian historical scholarship and "
            "to the international dissemination of "
            "Hungarian literature during the Hungarian "
            "national awakening (Magyar Nemzeti Ébredés). "
            "His Geschichte der Magyaren (History of the "
            "Magyars), published in German, was one of "
            "the first systematic histories of Hungary "
            "available to a European audience unfamiliar "
            "with the Hungarian language.\n\n"
            "Born into the Hungarian nobility, Mailáth "
            "was educated in the tradition of Habsburg "
            "aristocratic culture and wrote primarily "
            "in German — the language of educated "
            "Central European discourse — even as he "
            "celebrated Hungarian history and culture. "
            "This was characteristic of the first "
            "generation of the Hungarian national "
            "awakening, in which many of the movement's "
            "advocates were nobles who had to communicate "
            "Hungarian identity to a European audience "
            "through German before Hungarian could serve "
            "as a full literary and scholarly language.\n\n"
            "His anthology of Hungarian folk poetry "
            "and his German translations of Hungarian "
            "literary works introduced Hungarian folklore "
            "and Romantic literature to German-speaking "
            "audiences — contributing to the broader "
            "European Romantic interest in folk culture "
            "and national literatures that characterized "
            "the early nineteenth century.\n\n"
            "His later life was marked by personal "
            "tragedy — he drowned in Lake Starnberg "
            "in Bavaria in 1861 under circumstances "
            "that suggested suicide."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Hungarian nobleman and historian who wrote the Geschichte der Magyaren (History of the Magyars) in German — one of the first systematic accounts of Hungarian history accessible to European audiences; contributor to the Hungarian national awakening through German-language promotion of Hungarian literature, history, and folk culture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Hungarian national awakening (Magyar Nemzeti Ébredés) of the early nineteenth century — in which Hungarian nobles and intellectuals sought to assert a distinct Hungarian national identity within the Habsburg Empire through the revival of Hungarian language, history, and literature — motivated Mailáth's historical and literary work",
            "The European Romantic movement's enthusiasm for national literatures, folk cultures, and historical origins — exemplified by Herder's philosophy of national character and the Brothers Grimm's folk collection — provided the intellectual framework and the receptive audience for Mailáth's German-language presentations of Hungarian history and folklore",
            "The linguistic reality of early nineteenth-century Central European scholarship — in which German was the primary language of educated discourse across the Habsburg lands — required Hungarian national advocates like Mailáth to communicate their nation's claims to European audiences through German even as they worked to elevate Hungarian itself"
        ],
        "effects": [
            "His Geschichte der Magyaren introduced the narrative of Hungarian history to a German-reading European audience — giving educated Europeans their first systematic account of the Magyar nation's origins, medieval kingdom, and early modern history in an accessible scholarly form",
            "His anthologies and translations of Hungarian folk poetry contributed to the European Romantic interest in national literatures — presenting Hungarian folklore to German audiences who received it within the same framework of Romantic cultural nationalism that they applied to German, Slavic, and Scandinavian folk traditions",
            "His work contributed to the international legitimization of Hungarian national claims within the Habsburg Empire — demonstrating to European scholarly opinion that the Hungarians possessed a rich historical tradition and literary culture worthy of equal treatment within the Empire",
            "His tragic death by drowning in Lake Starnberg (1861) — possibly by suicide, in circumstances suggesting financial ruin and personal despair — added a poignant ending to a career that had spent its energies celebrating a national vitality that his own life's end contradicted"
        ],
        "relationships": [
            {"target": "hungarian-national-awakening", "verb": "CONTRIBUTES_TO", "note": "Historian and literary figure promoting Hungarian national identity"},
            {"target": "geschichte-der-magyaren", "verb": "WRITES", "note": "German-language history of the Magyar nation"},
            {"target": "habsburg-empire", "verb": "LIVES_IN", "note": "Hungarian noble in the Habsburg cultural sphere"},
            {"target": "european-romanticism", "verb": "PARTICIPATES_IN", "note": "Hungarian Romantic presenting folk culture and history to German audiences"},
            {"target": "hungary", "verb": "SERVES", "note": "Hungarian nobleman promoting national history and literature"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 54 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
