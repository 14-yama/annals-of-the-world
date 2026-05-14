#!/usr/bin/env python3
"""
Batch 51 — 8 entities: Justo Figuerola, Jacques Lacombe, Peter Collett,
Søren Anton Wilhelm Sørenssen, Charles James McDonald, Feliciano Chiclana,
Joseph Lainé, Faustin Hélie
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

    # 1 — Justo Figuerola
    ("justo-figuerola", {
        "summary": (
            "Justo Figuerola (1819–1882) was a Spanish liberal "
            "economist, politician, and journalist whose most "
            "enduring legacy is the introduction of the peseta "
            "as Spain's national currency — the monetary reform "
            "that unified the country's chaotic coinage system "
            "and anchored Spain to the Latin Monetary Union. "
            "Serving as Minister of Finance (1869–1871) under "
            "the government of General Prim after the Glorious "
            "Revolution of 1868 toppled Queen Isabella II, "
            "Figuerola enacted the Decree of 19 October 1868 "
            "that created the peseta, which remained Spain's "
            "currency for 133 years until the euro's arrival "
            "in 2002.\n\n"
            "Born in Calaf (Catalonia), Figuerola trained as "
            "a jurist and economist, becoming a professor of "
            "political economy at the University of Madrid. "
            "He was a committed free-trader who believed "
            "monetary reform and tariff reduction were "
            "inseparable. His peseta reform consolidated the "
            "reales, escudos, and maravedís into a single "
            "decimal system aligned with the French franc "
            "standard, enabling Spain to join the Latin "
            "Monetary Union alongside France, Belgium, Italy, "
            "and Switzerland.\n\n"
            "Beyond the peseta, Figuerola pushed for free-trade "
            "tariff reform (the Arancel Figuerola of 1869) "
            "that progressively lowered Spanish import duties, "
            "seeking to integrate Spain's economy into the "
            "liberal European commercial order. Though the "
            "Restoration of 1874 reversed many of his liberal "
            "economic policies, the peseta endured.\n\n"
            "'The best tribute to a statesman is a currency "
            "that outlives him by a century.' Figuerola's "
            "monetary reform proved exactly that — the peseta "
            "long outlasted the revolution that created it."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish liberal economist who created the peseta as Spain's national currency in 1868 — a monetary reform that unified Spain's coinage system and anchored the country to the Latin Monetary Union; the peseta endured until 2002; also authored the Arancel Figuerola free-trade tariff reform of 1869.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Glorious Revolution of 1868 (La Gloriosa) — which overthrew Queen Isabella II and installed a progressive liberal government under General Prim — created the political opening for sweeping economic reforms that conservative Bourbon governments had blocked, placing free-trade economists like Figuerola in positions of ministerial authority",
            "Spain's pre-1868 monetary chaos — with multiple overlapping currencies (reales, escudos, maravedís) of varying regional standards making commerce and accounting cumbersome — demanded the monetary unification that Figuerola's peseta reform achieved through the Decree of October 1868",
            "The international momentum of the Latin Monetary Union (1865) — in which France, Belgium, Italy, and Switzerland had already standardized their currencies to a silver/gold bimetallic franc standard — provided Figuerola with the template and the incentive to align Spain's new peseta to the same system, facilitating cross-border trade"
        ],
        "effects": [
            "The peseta became Spain's national currency for 133 years (1868–2002), surviving the Restoration, the Republic, the Civil War, Francoism, and democracy before being superseded by the euro — an extraordinary durability that made Figuerola's monetary reform one of the most long-lasting acts of any Spanish minister",
            "The Arancel Figuerola (1869) established a free-trade tariff schedule that, though partially reversed by the Restoration (1874) and later protectionism, shaped the terms of Spain's economic debate between free-traders and protectionists for decades",
            "Spain's integration into the Latin Monetary Union standard aligned its commercial and financial infrastructure with Western Europe, reducing transaction costs for Spanish international trade during the critical late-nineteenth-century export expansion",
            "Figuerola's career as a political economy professor at the University of Madrid helped establish economics as a serious academic discipline in Spain, training a generation of Spanish liberals in free-market theory"
        ],
        "relationships": [
            {"target": "spanish-glorious-revolution-1868", "verb": "SERVES_IN", "note": "Finance Minister in the post-1868 liberal government"},
            {"target": "latin-monetary-union", "verb": "ALIGNS_WITH", "note": "Peseta anchored to LMU franc standard"},
            {"target": "free-trade-movement", "verb": "CHAMPIONS", "note": "Arancel Figuerola 1869 free-trade tariff reform"},
            {"target": "university-of-madrid", "verb": "TEACHES_AT", "note": "Professor of political economy"},
            {"target": "isabella-ii-of-spain", "verb": "SUCCEEDS_GOVERNMENT_OF", "note": "Liberal minister after Isabella II's overthrow"}
        ]
    }),

    # 2 — Jacques Lacombe
    ("jacques-lacombe", {
        "summary": (
            "Jacques Lacombe (1724–1811) was a French bookseller, "
            "lexicographer, and encyclopedist who contributed "
            "substantially to the diffusion of Enlightenment "
            "knowledge through the compilation of practical "
            "reference works — dictionaries and encyclopedias "
            "that brought systematic knowledge within reach "
            "of educated but non-specialist readers in "
            "eighteenth-century France. His career embodied "
            "the Enlightenment ideal of knowledge organization "
            "and dissemination through the book trade.\n\n"
            "Operating from Paris as both a publisher and "
            "compiler, Lacombe produced multi-volume reference "
            "works including the Dictionnaire encyclopédique "
            "des amusements des sciences mathématiques "
            "et physiques (1792) and contributed to the vast "
            "Encyclopédie méthodique project initiated by "
            "Charles-Joseph Panckoucke — the successor "
            "enterprise to the original Encyclopédie of "
            "Diderot and d'Alembert. He also compiled "
            "dictionaries covering the arts, sciences, "
            "and history for the general reading public.\n\n"
            "His role was that of an intellectual entrepreneur "
            "of the book trade — identifying gaps in available "
            "reference literature and systematically filling "
            "them through compilations that synthesized "
            "existing scholarship into accessible formats. "
            "This function was essential to the Enlightenment's "
            "practical goal of spreading useful knowledge "
            "beyond the academy into literate civil society.\n\n"
            "Lacombe's long life (1724–1811) spanned the "
            "entire Enlightenment, the Revolution, and the "
            "Napoleonic era, and his productive career "
            "as a bookseller-encyclopedist made him a "
            "representative figure of the vast publication "
            "infrastructure that the Age of Reason required."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French Enlightenment bookseller and encyclopedist who compiled multi-volume reference dictionaries and contributed to the Encyclopédie méthodique; a representative figure of the knowledge-dissemination function of the eighteenth-century Paris book trade.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Enlightenment demand for systematic, accessible reference works — driven by the success of Diderot and d'Alembert's Encyclopédie (1751–1772) and Panckoucke's Encyclopédie méthodique — created a sustained market for lexicographers and compilers like Lacombe who could organize knowledge into practical dictionary formats for educated general readers",
            "The Paris book trade's commercialization of knowledge — which transformed encyclopedic compilation from a scholarly project into a viable commercial enterprise — enabled figures like Lacombe to sustain careers as professional reference-book producers operating at the intersection of scholarship and publishing",
            "The French reading public's expansion in the eighteenth century — as literacy grew and the bourgeoisie sought self-education through reference works — created the demand for the accessible, multi-volume encyclopedic dictionaries that Lacombe specialized in producing"
        ],
        "effects": [
            "His reference works contributed to the diffusion of Enlightenment knowledge among educated but non-specialist French readers who could not afford the complete Encyclopédie or access academic libraries — spreading systematic knowledge through the commercial book trade",
            "His involvement in the Encyclopédie méthodique helped sustain the most ambitious publishing project of the late Enlightenment — Panckoucke's multi-decade effort to reorganize all human knowledge by subject discipline",
            "His career as a bookseller-encyclopedist exemplified the model of the intellectual entrepreneur that characterized the Paris book trade, demonstrating how commercial publishing could serve Enlightenment goals of knowledge democratization",
            "His long productive career spanning the Ancien Régime, Revolution, and Empire showed the resilience of the reference-book market across political upheavals, as the demand for practical knowledge dictionaries proved independent of regime changes"
        ],
        "relationships": [
            {"target": "encyclopedie-methodique", "verb": "CONTRIBUTES_TO", "note": "Compiled entries for Panckoucke's Encyclopédie méthodique"},
            {"target": "charles-joseph-panckoucke", "verb": "COLLABORATES_WITH", "note": "Publisher partner in encyclopedic projects"},
            {"target": "french-enlightenment", "verb": "PARTICIPATES_IN", "note": "Bookseller-encyclopedist in Enlightenment knowledge diffusion"},
            {"target": "paris-book-trade", "verb": "OPERATES_IN", "note": "Professional bookseller and compiler in Paris"},
            {"target": "encyclopedie", "verb": "SUCCEEDS", "note": "His works continued the encyclopedic tradition after Diderot's Encyclopédie"}
        ]
    }),

    # 3 — Peter Collett
    ("peter-collett", {
        "summary": (
            "Peter Collett (1749–1818) was a Norwegian merchant, "
            "landowner, judge, and politician who came from "
            "one of the most influential mercantile dynasties "
            "in Norwegian history — the Collett family of "
            "Christiania (Oslo), whose trading networks "
            "dominated Norwegian commerce for generations. "
            "His career combined commercial enterprise with "
            "civic and judicial service, embodying the "
            "intertwined mercantile and political leadership "
            "of Norway's urban patriciate.\n\n"
            "The Collett family had risen to prominence "
            "through the Norwegian timber and fish trade "
            "with Britain and the Netherlands, accumulating "
            "substantial landed estates alongside their "
            "commercial wealth. Peter Collett managed this "
            "family inheritance during a period of upheaval "
            "— the Napoleonic Wars disrupted Norwegian "
            "commerce severely, as the British blockade "
            "and Danish foreign policy (Norway was under "
            "Danish rule until 1814) wreaked havoc on the "
            "export economy.\n\n"
            "In the political sphere, the dissolution of the "
            "Danish-Norwegian union in 1814 and the "
            "adoption of the Norwegian Constitution created "
            "new civic roles. Men of Collett's standing "
            "— property-owning merchants and landowners "
            "— constituted the natural governing class of "
            "the new constitutional order, serving as "
            "judges, magistrates, and representatives "
            "in the emerging Norwegian parliamentary system.\n\n"
            "His legacy is partly genealogical: the Collett "
            "family produced several generations of Norwegian "
            "civic leaders, and their estates became "
            "cultural landmarks in the Oslo region."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian merchant, landowner, and judge from the prominent Collett mercantile dynasty of Christiania; a representative of the Norwegian urban patriciate who exercised civic and commercial leadership during the tumultuous Napoleonic and post-1814 constitutional period.",
            "significanceCategory": "local"
        },
        "causes": [
            "The rise of the Collett mercantile dynasty — built on the Norwegian timber and fish trade with Britain and the Netherlands over multiple generations — created the family wealth and social capital that gave Peter Collett his position as a leading figure in Christiania's civic life",
            "The Napoleonic Wars' disruption of Norwegian commerce — through the British blockade and Denmark's forced alliance with France — tested the resilience of merchant families like the Colletts who depended on the North Sea trade routes, reshaping how they managed their commercial and landed interests",
            "Norway's constitutional revolution of 1814 — which created a new parliamentary system requiring property-owning merchants and landowners to take on formal civic roles as judges, magistrates, and representatives — drew figures like Collett into institutional public service"
        ],
        "effects": [
            "His stewardship of the Collett family commercial interests helped sustain one of Norway's leading mercantile dynasties through the severe disruptions of the Napoleonic era, preserving the family's position in Norwegian civic life",
            "His judicial and civic service contributed to the formation of the new Norwegian constitutional order after 1814, as the property-owning patriciate supplied the institutional personnel needed to operate the new courts and representative assemblies",
            "The Collett family estates and networks became cultural and social landmarks in the Christiania (Oslo) region, contributing to the development of Norwegian bourgeois culture in the early nineteenth century",
            "His life documented the transition of a leading Norwegian merchant family from the Ancien Régime Danish-Norwegian monarchy to the new Norwegian constitutional state — a social history of continuity through political rupture"
        ],
        "relationships": [
            {"target": "norwegian-constitution-1814", "verb": "OPERATES_UNDER", "note": "Civic service in the new constitutional order"},
            {"target": "collett-family", "verb": "LEADS", "note": "Head of the prominent Collett mercantile dynasty"},
            {"target": "christiania", "verb": "BASED_IN", "note": "Merchant and civic leader in Christiania (Oslo)"},
            {"target": "napoleonic-wars", "verb": "AFFECTED_BY", "note": "Norwegian commerce disrupted by blockade and war"},
            {"target": "norway", "verb": "SERVES", "note": "Judge and property owner in Norwegian civic administration"}
        ]
    }),

    # 4 — Søren Anton Wilhelm Sørenssen
    ("søren-anton-wilhelm-sørenssen", {
        "summary": (
            "Søren Anton Wilhelm Sørenssen (1793–1875) was a "
            "Norwegian jurist and legal scholar who served as "
            "a professor of law at the University of Christiania "
            "(now the University of Oslo) and as a judge on "
            "Norway's highest courts. His academic career "
            "contributed to the systematization of Norwegian "
            "private law during the formative decades after "
            "the Constitution of 1814 established Norway's "
            "independent legal order — a period when Norwegian "
            "legal scholarship had to develop an indigenous "
            "jurisprudence distinct from Danish legal traditions.\n\n"
            "Educated at a time when Norwegian universities "
            "were still in their infancy — the University of "
            "Christiania had only been founded in 1811 — "
            "Sørenssen became part of the first generation "
            "of Norwegian legal academics who built a "
            "national legal science after independence. "
            "His teaching and writing addressed Norwegian "
            "commercial law and civil procedure, drawing on "
            "both the inherited Danish legal framework and "
            "the new constitutional provisions to construct "
            "a coherent body of Norwegian private law.\n\n"
            "The challenge facing Norwegian jurists of his "
            "generation was immense: 1814 had created a new "
            "constitutional state but had not yet produced "
            "a comprehensive codified civil law — Norwegian "
            "courts operated under a patchwork of old Danish "
            "ordinances and constitutional principles that "
            "required learned jurisprudence to interpret "
            "coherently. Sørenssen's academic work contributed "
            "to that interpretive project.\n\n"
            "He was also a practical figure in Norwegian "
            "judicial life, serving on courts that applied "
            "the emerging body of Norwegian law to concrete "
            "commercial and civil disputes."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian jurist and law professor at the University of Christiania; part of the first generation of Norwegian legal academics who built an indigenous Norwegian jurisprudence after independence in 1814; contributed to systematizing Norwegian private and commercial law in the formative post-constitutional decades.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — which created an independent Norwegian state but left intact a patchwork of Danish ordinances as the operating civil law — created the urgent need for a generation of Norwegian legal scholars who could build an indigenous jurisprudence to serve the new constitutional order",
            "The founding of the University of Christiania in 1811 — the first Norwegian university — provided the institutional home for developing Norwegian legal scholarship, making Sørenssen's career as a law professor possible for the first time in Norwegian history",
            "The separation of Norway from Denmark (1814) and the subsequent Swedish-Norwegian union required Norwegian courts to develop legal doctrines that drew on the old Danish legal heritage while adapting it to new constitutional realities — an interpretive challenge that demanded precisely the kind of scholarly jurisprudence that Sørenssen provided"
        ],
        "effects": [
            "His professorial career at the University of Christiania helped establish legal scholarship as an academic discipline in Norway, training generations of Norwegian lawyers in systematized legal doctrine at a time when the country lacked a codified civil code",
            "His contributions to Norwegian commercial and private law jurisprudence provided the interpretive framework that Norwegian courts applied to commercial disputes during the critical decades of Norwegian economic expansion in the nineteenth century",
            "His judicial service on Norway's higher courts helped set binding precedents that shaped Norwegian private law for decades, translating scholarly jurisprudence into enforceable doctrine",
            "His career exemplified the close integration of legal academia and the judiciary in Norwegian institutional culture — a pattern that gave academic jurists direct influence over the development of living law"
        ],
        "relationships": [
            {"target": "university-of-christiania", "verb": "TEACHES_AT", "note": "Professor of law at Norway's first university"},
            {"target": "norwegian-constitution-1814", "verb": "INTERPRETS", "note": "Jurisprudence addressed new constitutional legal order"},
            {"target": "norwegian-supreme-court", "verb": "SERVES_ON", "note": "Judge on Norway's higher courts"},
            {"target": "norwegian-commercial-law", "verb": "SYSTEMATIZES", "note": "Scholarly works on Norwegian private and commercial law"},
            {"target": "norway", "verb": "SERVES", "note": "Legal scholar in the formative post-1814 Norwegian state"}
        ]
    }),

    # 5 — Charles James McDonald
    ("charles-james-mcdonald", {
        "summary": (
            "Charles James McDonald (1793–1860) was an American "
            "lawyer, judge, and politician who served as "
            "Governor of Georgia (1839–1843) and later as "
            "a Justice of the Georgia Supreme Court. A "
            "conservative Democrat and firm defender of "
            "states' rights and Southern interests, McDonald "
            "became a leading voice for Southern resistance "
            "to federal encroachment during the intensifying "
            "sectional crisis of the antebellum era.\n\n"
            "Born in Laurens County, Georgia, McDonald read "
            "law and built a successful legal career before "
            "entering politics as a Democrat in the era of "
            "Andrew Jackson. As Governor, he presided over "
            "Georgia's continued resistance to abolitionist "
            "agitation from the North and oversaw state "
            "affairs during a period of economic depression "
            "following the Panic of 1837. His administration "
            "took a hard states'-rights line on federal "
            "authority, consistent with the dominant "
            "political culture of antebellum Georgia.\n\n"
            "After leaving the governorship, McDonald "
            "continued his judicial career, serving on "
            "the Georgia Supreme Court from 1853 to 1859. "
            "His legal opinions contributed to the body "
            "of Georgia state jurisprudence in the "
            "antebellum period. He later became a prominent "
            "cooperationist who resisted immediate secession "
            "but ultimately supported Georgia's departure "
            "from the Union once secession was voted.\n\n"
            "His career traced the trajectory of a Southern "
            "conservative leader — Jacksonian Democrat, "
            "states'-rights advocate, reluctant secessionist "
            "— through the decades that led to the Civil War."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Governor of Georgia (1839–1843) and Georgia Supreme Court Justice; conservative Democrat and states'-rights advocate in the antebellum South; a leading voice for Southern resistance to abolitionist agitation who later became a reluctant secessionist; his career traced the arc of Southern conservative politics from Jacksonian Democracy to the Civil War.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Jacksonian Democratic political tradition — with its emphasis on states' rights, limited federal government, and agrarian Southern interests — shaped McDonald's political ideology and gave him the partisan framework through which he rose to the Georgia governorship",
            "The intensifying sectional crisis over slavery and abolitionism in the 1830s–1850s — as Northern antislavery movements challenged the Southern slave economy — created the political environment in which McDonald's states'-rights conservatism resonated with Georgia voters and made him a prominent defender of Southern interests",
            "The Panic of 1837 and its prolonged economic depression — which devastated Georgia's cotton economy — defined the domestic challenges of McDonald's governorship and demanded practical responses to financial distress at the state level"
        ],
        "effects": [
            "His governorship consolidated Georgia's political culture of states'-rights conservatism, reinforcing the institutional and rhetorical framework through which the state resisted federal authority on slavery-related questions during the antebellum decades",
            "His Georgia Supreme Court service (1853–1859) contributed to the development of Georgia state jurisprudence in property, contract, and slavery law — legal areas of critical importance to the antebellum Southern economy",
            "His cooperationist position during the secession debate of 1860–1861 represented a significant strand of Southern conservative thinking — reluctant secession motivated by constitutional principle rather than enthusiasm — that characterized many of the older Jacksonian Democrats",
            "His career illustrated the political sociology of the antebellum Southern lawyer-politician: reading law, judicial service, gubernatorial office, and continued judicial involvement in an era when law and politics were inseparable in Southern public life"
        ],
        "relationships": [
            {"target": "georgia", "verb": "GOVERNS", "note": "Governor of Georgia 1839–1843"},
            {"target": "georgia-supreme-court", "verb": "SERVES_ON", "note": "Justice 1853–1859"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Conservative Jacksonian Democrat"},
            {"target": "states-rights-movement", "verb": "CHAMPIONS", "note": "Firm defender of states' rights against federal encroachment"},
            {"target": "american-civil-war", "verb": "PRECEDES", "note": "Cooperationist who supported secession once voted"}
        ]
    }),

    # 6 — Feliciano Chiclana
    ("feliciano-chiclana", {
        "summary": (
            "Feliciano Antonio Chiclana (1761–1826) was an "
            "Argentine independence leader, lawyer, and "
            "politician who served as one of the three members "
            "of the First Triumvirate — the governing body "
            "that led the Río de la Plata provinces after the "
            "May Revolution of 1810 expelled Spanish viceregal "
            "authority. He also served as Governor of the "
            "Buenos Aires Intendancy (1811–1812), placing him "
            "among the founding generation of Argentine "
            "republican governance.\n\n"
            "Born in Buenos Aires, Chiclana trained as a "
            "lawyer and became involved in the cabildo abierto "
            "(open town council) politics that drove the "
            "independence movement. The May Revolution of "
            "1810 — triggered by Napoleon's invasion of "
            "Spain and the collapse of the Bourbon monarchy "
            "— created the Junta Grande that first governed "
            "in the name of King Ferdinand VII. The First "
            "Triumvirate (September 1811) replaced the Junta "
            "and concentrated executive power in three men, "
            "with Chiclana serving alongside Bernardino "
            "Rivadavia and Manuel de Sarratea.\n\n"
            "As a triumvir, Chiclana participated in the "
            "critical decisions of the early independence "
            "period: organizing military resistance to "
            "Spanish royalist forces, managing the "
            "fractious politics of the Río de la Plata "
            "provinces, and navigating the tensions between "
            "Buenos Aires and the interior regions.\n\n"
            "His career embodied the lawyerly, urban "
            "professional class that led the Argentine "
            "independence movement — educated in colonial "
            "institutions, committed to liberal principles, "
            "and capable of operating within the novel "
            "republican institutions that the revolution created."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Member of the First Triumvirate (1811) and Governor of Buenos Aires (1811–1812) in the Argentine independence era; one of the founding leaders of the Río de la Plata government that emerged from the May Revolution of 1810; part of the lawyerly urban class that drove Argentine republican independence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The May Revolution of 1810 — triggered by Napoleon's seizure of the Spanish throne and the collapse of Bourbon authority, which created a power vacuum in the Río de la Plata viceroyalty — opened the political space in which Chiclana and his colleagues could establish autonomous governance bodies claiming to act in the name of Ferdinand VII",
            "The political culture of Buenos Aires' educated lawyer-professional class — shaped by Bourbon reformism, Enlightenment ideas, and awareness of the American and French revolutions — produced the ideological commitment to liberal republican government that Chiclana and his triumviral colleagues embodied",
            "The military pressure from Spanish royalist forces in the interior (Upper Peru, Montevideo) that threatened the Buenos Aires revolution required the consolidation of executive authority in the triumvirate structure, giving Chiclana his moment of highest political responsibility"
        ],
        "effects": [
            "The First Triumvirate established the institutional template for republican executive government in the Río de la Plata — a collegial executive body with defined powers — that influenced subsequent governmental experiments as Argentina moved toward independence and constitutionalism",
            "His service as Governor of Buenos Aires Intendancy (1811–1812) helped maintain the administrative continuity of Argentina's most important province during the turbulent early independence period, when the risk of political collapse was real",
            "His participation in the founding generation of Argentine governance contributed to the political culture and institutional memory that shaped the Argentine state-building project of the 1810s–1820s",
            "His career as a lawyer-politician demonstrated the critical role that legally trained professionals played in translating revolutionary ideals into workable republican institutions across Spanish America's independence movements"
        ],
        "relationships": [
            {"target": "first-triumvirate-argentina", "verb": "LEADS", "note": "Member of the First Triumvirate 1811"},
            {"target": "may-revolution-1810", "verb": "PARTICIPATES_IN", "note": "Involved in Buenos Aires independence movement"},
            {"target": "buenos-aires", "verb": "GOVERNS", "note": "Governor of Buenos Aires Intendancy 1811–1812"},
            {"target": "bernardino-rivadavia", "verb": "SERVES_WITH", "note": "Fellow triumvir"},
            {"target": "argentine-independence", "verb": "CHAMPIONS", "note": "Founding leader of Río de la Plata self-governance"}
        ]
    }),

    # 7 — Joseph Lainé
    ("joseph-lainé", {
        "summary": (
            "Joseph-Henri-Joachim Lainé (1767–1835), Viscount "
            "Lainé, was a French lawyer, orator, and politician "
            "whose courageous report to Napoleon's Legislative "
            "Body in December 1813 — frankly depicting the "
            "exhaustion and suffering caused by the Emperor's "
            "wars — made him briefly a national hero and "
            "contributed to the political atmosphere that "
            "facilitated Napoleon's first abdication in April "
            "1814. His subsequent career under the Bourbon "
            "Restoration, including service as Minister of "
            "the Interior (1816–1818) and President of the "
            "Chamber of Deputies (1813–1814, 1816), cemented "
            "his reputation as one of the Restoration's "
            "leading constitutional monarchists.\n\n"
            "Born in Bordeaux, Lainé trained as a lawyer "
            "and entered the Legislative Body (Corps législatif) "
            "as a deputy. When Napoleon's wars had brought "
            "France to the brink of military collapse in "
            "late 1813, Lainé was the rapporteur for the "
            "committee charged with advising the Emperor "
            "on peace. His report — which detailed the "
            "miseries of the French people and called "
            "for an honorable peace — was suppressed by "
            "Napoleon but circulated widely and established "
            "Lainé's moral authority.\n\n"
            "Under the Restoration, Louis XVIII rewarded "
            "Lainé with ministerial office and the presidency "
            "of the Chamber. As Interior Minister, he "
            "navigated the delicate balance between the "
            "Ultraroyalist right and the liberal constitutional "
            "center, attempting to make the Charter of 1814 "
            "a workable constitutional instrument.\n\n"
            "'One must dare to tell the truth to kings' — "
            "Lainé's reported maxim captured the moral "
            "courage that distinguished his 1813 report "
            "and defined his political reputation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French lawyer-politician whose 1813 report to Napoleon's Legislative Body honestly depicted French war exhaustion and contributed to the political climate enabling Napoleon's first abdication; President of the Chamber of Deputies and Interior Minister under the Bourbon Restoration; a leading constitutional monarchist of the post-Napoleonic order.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's military overextension by 1813 — with the Grande Armée shattered in Russia (1812) and the Coalition closing in from all directions — created a political crisis in which even Napoleon's controlled Legislative Body felt compelled to confront the Emperor with the reality of French exhaustion, giving Lainé the opportunity to deliver his historic report",
            "The French legal and parliamentary tradition of the rapporteur — a committee spokesman who presented formal recommendations to the legislative assembly — provided the procedural role through which Lainé could deliver his condemnation of Napoleon's war policy under a veneer of constitutional regularity",
            "The Bourbon Restoration's need for credible constitutional politicians who could legitimize the Charter of 1814 and govern through parliamentary procedures — rather than simply relying on Ultraroyalist reactionaries — made figures like Lainé, whose liberal monarchism straddled the Ancien Régime and the Revolution, indispensable to the Restoration project"
        ],
        "effects": [
            "His 1813 report to Napoleon's Legislative Body became a famous act of political courage — circulating as a clandestine pamphlet and contributing to the political disillusionment with the Empire that made Napoleon's first abdication (April 1814) politically feasible",
            "His tenure as President of the Chamber of Deputies (1813–1814, 1816) helped establish the procedural norms and institutional culture of France's early constitutional parliamentary life under the Restoration Charter of 1814",
            "As Interior Minister (1816–1818), he managed the administrative machinery of the Restoration state during the sensitive period of the Ultraroyalist chambre introuvable and the subsequent moderate constitutional ministry, helping maintain civil order during post-Napoleonic political turbulence",
            "His career demonstrated the viability of the constitutional monarchist center in post-Napoleonic France — a tradition that sought to honor both the revolutionary gains of 1789 and the legitimacy of Bourbon monarchy, and which shaped French politics through the July Monarchy of Louis-Philippe"
        ],
        "relationships": [
            {"target": "napoleon-i", "verb": "OPPOSES", "note": "1813 report to Legislative Body challenged Napoleon's war policy"},
            {"target": "bourbon-restoration", "verb": "SERVES", "note": "President of Chamber of Deputies and Interior Minister"},
            {"target": "chamber-of-deputies-france", "verb": "PRESIDES_OVER", "note": "President 1813–1814, 1816"},
            {"target": "louis-xviii", "verb": "SERVES_UNDER", "note": "Interior Minister under Louis XVIII"},
            {"target": "charter-of-1814", "verb": "UPHOLDS", "note": "Constitutional monarchist implementing the Restoration Charter"}
        ]
    }),

    # 8 — Faustin Hélie
    ("faustin-hélie", {
        "summary": (
            "Faustin Hélie (1799–1884) was a French jurist "
            "and legal scholar whose eight-volume Traité de "
            "l'instruction criminelle (1845–1860) became the "
            "definitive systematic treatise on French criminal "
            "procedure — a foundational work that shaped "
            "French criminal justice for decades and remains "
            "a landmark in the history of French legal "
            "scholarship. Hélie combined an academic career "
            "with high judicial and administrative service, "
            "ending his career as Vice-President of the "
            "Conseil d'État and a member of the Académie "
            "des Sciences Morales et Politiques.\n\n"
            "Born in Château-Gontier (Mayenne), Hélie studied "
            "law in Paris and entered the legal profession "
            "during the July Monarchy. His scholarly ambitions "
            "focused on systematizing French criminal law "
            "at a moment when the Code d'instruction criminelle "
            "of 1808 — Napoleon's criminal procedure code — "
            "had been in operation for decades but lacked "
            "a comprehensive scholarly commentary. Hélie "
            "supplied this need through his monumental "
            "Traité, which analyzed every aspect of French "
            "criminal procedure with exhaustive erudition.\n\n"
            "He also produced an annotated edition of "
            "Beccaria's Dei delitti e delle pene in "
            "collaboration with François Hélie, and "
            "contributed to the great Encyclopédie du droit "
            "edited by Adolphe Chauveau. These works made "
            "him the central figure in the French criminal "
            "law scholarship of the Second Empire and early "
            "Third Republic.\n\n"
            "His judicial career at the Conseil d'État "
            "combined with his academic output exemplified "
            "the French tradition of the juriste-fonctionnaire "
            "— the scholar-official who simultaneously "
            "theorized and administered the law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French criminal law jurist whose eight-volume Traité de l'instruction criminelle (1845–1860) was the definitive systematic commentary on French criminal procedure under the Code d'instruction criminelle of 1808; Vice-President of the Conseil d'État and member of the Académie des Sciences Morales et Politiques; central figure in French criminal law scholarship of the Second Empire era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's Code d'instruction criminelle (1808) — which codified French criminal procedure but left the profession without a comprehensive scholarly commentary — created the scholarly gap that Hélie's eight-volume Traité filled, making a systematic legal treatise both possible and professionally essential",
            "The growth of French legal scholarship in the nineteenth century — driven by the professionalization of the legal academy and the proliferation of legal journals and encyclopedias — created the publishing infrastructure and readership that made a monumental multi-volume treatise on criminal procedure commercially and intellectually viable",
            "The French tradition of the juriste-fonctionnaire — combining scholarly production with senior government service in the Conseil d'État or magistrature — provided Hélie with the institutional position from which to combine high-level legal practice with sustained academic output"
        ],
        "effects": [
            "His Traité de l'instruction criminelle (1845–1860) became the authoritative commentary on French criminal procedure for generations of lawyers, judges, and prosecutors — shaping how French courts interpreted and applied the Code d'instruction criminelle throughout the Second Empire and the early Third Republic",
            "His scholarly synthesis of French criminal procedure contributed to the coherence and predictability of French criminal justice by providing judges and advocates with a systematic doctrinal framework for resolving procedural questions",
            "His annotated edition of Beccaria's Dei delitti e delle pene helped sustain the influence of Enlightenment criminal law reform thinking in French legal culture, connecting nineteenth-century French procedure to its eighteenth-century humanitarian roots",
            "His career as Vice-President of the Conseil d'État demonstrated how legal scholarship could translate into the highest levels of French administrative and judicial governance, modeling the integration of academic and practical legal authority"
        ],
        "relationships": [
            {"target": "code-dintstruction-criminelle-1808", "verb": "COMMENTATES", "note": "Eight-volume Traité systematized French criminal procedure"},
            {"target": "conseil-detat-france", "verb": "SERVES_ON", "note": "Vice-President of the Conseil d'État"},
            {"target": "academie-des-sciences-morales-et-politiques", "verb": "MEMBER_OF", "note": "Academic recognition of legal scholarship"},
            {"target": "cesare-beccaria", "verb": "EDITS", "note": "Annotated edition of Dei delitti e delle pene"},
            {"target": "french-criminal-law", "verb": "SYSTEMATIZES", "note": "Traité de l'instruction criminelle — definitive treatise on criminal procedure"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 51 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
