#!/usr/bin/env python3
"""
Batch 52 — 8 entities: Jacques-Antoine Manuel, Philippe-François-Joseph Le Bas,
Caleb Smith Woodhull, Enevold De Falsen, Henry St. George Tucker Sr.,
Henry Dutton, Manuel Silvela y García de Aragón, Modesto Cortázar
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

    # 1 — Jacques-Antoine Manuel
    ("jacques-antoine-manuel", {
        "summary": (
            "Jacques-Antoine Manuel (1775–1827) was a French "
            "liberal lawyer and politician who became one of "
            "the most celebrated parliamentary orators of "
            "the Bourbon Restoration — famous above all for "
            "his dramatic expulsion from the Chamber of "
            "Deputies in 1823 for defending the French "
            "Revolution's regicide, an act of parliamentary "
            "courage that made him a liberal hero and "
            "a symbol of free speech under the Restoration.\n\n"
            "Born in Barcelonnette (Hautes-Alpes), Manuel "
            "was a self-made lawyer whose republican "
            "sympathies brought him into alliance with "
            "the liberal opposition under the Restoration. "
            "Elected repeatedly to the Chamber of Deputies, "
            "he became the voice of the constitutionalist "
            "liberal left — defending civil liberties, "
            "press freedom, and the achievements of "
            "the Revolution against Ultraroyalist reaction. "
            "His oratory was renowned for its clarity, "
            "force, and moral conviction.\n\n"
            "In February 1823, during a debate on France's "
            "military intervention in Spain to restore "
            "Ferdinand VII, Manuel delivered a speech "
            "defending the principle — however controversial "
            "— that revolutionary France's execution of "
            "Louis XVI had historical justification. "
            "The Chamber voted to expel him, and when "
            "the National Guard sergeant refused to "
            "physically remove him (a famous act of "
            "solidarity), gendarmes had to do so. "
            "The episode became a defining liberal cause célèbre.\n\n"
            "His early death in 1827 deprived the liberal "
            "opposition of its finest parliamentary voice "
            "just before the 1830 Revolution that toppled "
            "Charles X."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French liberal orator and deputy under the Bourbon Restoration; expelled from the Chamber of Deputies in 1823 for defending revolutionary principles — an act that made him a liberal hero and symbol of free speech; among the finest parliamentary orators of the Restoration era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Bourbon Restoration's Ultraroyalist political culture — which sought to suppress the memory of the Revolution and prosecute those who defended it — created the confrontational parliamentary environment in which Manuel's liberal oratory became an act of political resistance and eventual martyrdom",
            "Manuel's legal training and republican formation during the revolutionary and Napoleonic periods equipped him with the intellectual tools and political commitments that drove his parliamentary career as the foremost voice of Restoration liberal constitutionalism",
            "France's military intervention in Spain (1823) to restore Ferdinand VII — which the liberal opposition viewed as the Restoration monarchy's most flagrant repudiation of constitutional government — provided the specific occasion for Manuel's controversial speech defending revolutionary regicide as historical precedent"
        ],
        "effects": [
            "His expulsion from the Chamber of Deputies in 1823 became a celebrated liberal cause célèbre — publicized across Europe, transforming Manuel into a martyr for free speech and helping consolidate the liberal opposition's identity and resolve in the years leading to the 1830 Revolution",
            "The National Guard sergeant's refusal to physically remove him — a famous moment of popular solidarity — became an iconic image of the tension between official authority and liberal public opinion in Restoration France",
            "His parliamentary oratory established a rhetorical template for the Restoration liberal opposition — combining constitutional arguments with appeals to revolutionary principle — that influenced the parliamentary left through the 1820s and into the July Monarchy",
            "His early death in 1827 was mourned as a national loss by the liberal movement, and his funeral became a large political demonstration that foreshadowed the popular mobilization of 1830"
        ],
        "relationships": [
            {"target": "bourbon-restoration", "verb": "OPPOSES", "note": "Leader of liberal parliamentary opposition"},
            {"target": "chamber-of-deputies-france", "verb": "SERVES_IN", "note": "Deputy repeatedly elected under the Restoration"},
            {"target": "french-liberal-movement", "verb": "LEADS", "note": "Foremost parliamentary voice of Restoration liberalism"},
            {"target": "french-revolution", "verb": "DEFENDS", "note": "Expelled for defending revolutionary principles including regicide"},
            {"target": "july-revolution-1830", "verb": "PRECEDES", "note": "His martyrdom helped build liberal momentum for 1830"}
        ]
    }),

    # 2 — Philippe-François-Joseph Le Bas
    ("philippe-françois-joseph-le-bas", {
        "summary": (
            "Philippe-François-Joseph Le Bas (1794–1860) was "
            "a French classicist, archaeologist, and philologist "
            "whose monumental epigraphic and antiquarian "
            "surveys of Greece and the eastern Mediterranean "
            "contributed substantially to the development "
            "of classical archaeology and Greek epigraphy "
            "in the nineteenth century. He combined a "
            "career as a librarian and professor with "
            "major fieldwork expeditions that produced "
            "foundational corpora of ancient inscriptions.\n\n"
            "Son of the Terrorist-era revolutionary "
            "Philippe Le Bas (1765–1794) — Robespierre's "
            "close associate who died by suicide on "
            "9 Thermidor — Philippe-François-Joseph bore "
            "a remarkable family legacy. His own career "
            "followed a very different path: scholarly, "
            "systematic, and apolitical. He was educated "
            "at the École Normale Supérieure and became "
            "a professor of Greek and Latin at the "
            "Collège de France.\n\n"
            "His epigraphic expeditions to Greece, Asia Minor, "
            "and Syria (1842–1844), conducted under the "
            "auspices of the French government, produced "
            "the monumental Voyage archéologique en Grèce "
            "et en Asie Mineure — a multi-volume corpus "
            "of ancient inscriptions, coins, and monuments "
            "that became a standard reference for classical "
            "scholars. This work contributed directly to "
            "the corpus of inscriptions that would later "
            "be systematized in the Corpus Inscriptionum "
            "Graecarum.\n\n"
            "His scholarly output bridged the Romantic "
            "enthusiasm for ancient Greece and the emerging "
            "scientific discipline of classical archaeology."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French classicist and epigraphist whose archaeological expeditions to Greece and Asia Minor (1842–1844) produced the Voyage archéologique en Grèce et en Asie Mineure — a foundational corpus of ancient Greek inscriptions; Collège de France professor; son of Robespierre's associate Philippe Le Bas.",
            "significanceCategory": "regional"
        },
        "causes": [
            "France's growing scholarly and political investment in classical Greece — driven by Philhellenism after the Greek War of Independence (1821–1829) and the desire to document ancient civilization before Ottoman-era development destroyed it — created the institutional support and funding for Le Bas's epigraphic expeditions to Greece and Asia Minor",
            "The development of scientific classical archaeology as a discipline in early nineteenth-century Europe — moving beyond Winckelmann's aesthetic appreciation to systematic fieldwork, epigraphy, and numismatics — provided the scholarly framework within which Le Bas's inscription-collection missions operated",
            "The Collège de France's tradition of combining advanced research with public teaching gave Le Bas the institutional platform from which to organize major fieldwork expeditions while maintaining his scholarly base in Paris"
        ],
        "effects": [
            "His Voyage archéologique en Grèce et en Asie Mineure became a foundational reference for classical scholars studying ancient Greek inscriptions, contributing to the systematic epigraphic record that underpins modern understanding of Greek history, religion, and administration",
            "His epigraphic work contributed data that fed into the Corpus Inscriptionum Graecarum — the attempt to compile all known ancient Greek inscriptions that was the major scholarly project of nineteenth-century classical studies",
            "His expeditions trained a generation of French classical archaeologists in the methods of systematic field epigraphy, helping establish the professional standards of French classical scholarship in the eastern Mediterranean",
            "His career demonstrated the French state's investment in classical scholarship as a form of cultural prestige — using government-funded expeditions to position France as a leader in recovering and interpreting the ancient world"
        ],
        "relationships": [
            {"target": "college-de-france", "verb": "TEACHES_AT", "note": "Professor of Greek and Latin"},
            {"target": "greek-epigraphy", "verb": "ADVANCES", "note": "Voyage archéologique foundational inscription corpus"},
            {"target": "corpus-inscriptionum-graecarum", "verb": "CONTRIBUTES_TO", "note": "Epigraphic data fed the Greek inscription corpus project"},
            {"target": "french-classical-archaeology", "verb": "PIONEERS", "note": "Government-sponsored expeditions to Greece and Asia Minor"},
            {"target": "philippe-le-bas-revolutionary", "verb": "CHILD_OF", "note": "Son of Robespierre's associate Philippe Le Bas"}
        ]
    }),

    # 3 — Caleb Smith Woodhull
    ("caleb-smith-woodhull", {
        "summary": (
            "Caleb Smith Woodhull (1792–1866) was an American "
            "lawyer and public official who served as Mayor "
            "of New York City (1849–1851) during a critical "
            "period of rapid urban growth and the onset of "
            "major public health challenges. His mayoralty "
            "coincided with the cholera epidemic of 1849 — "
            "one of the deadliest disease events in New "
            "York's history — making his administration "
            "responsible for emergency public health "
            "responses to a catastrophe that killed over "
            "five thousand New Yorkers.\n\n"
            "Woodhull came from a distinguished New York "
            "legal family and built a successful legal "
            "career before entering civic politics as a "
            "Whig. His mayoral tenure (1849–1851) saw "
            "New York grappling with the consequences "
            "of the enormous Irish and German immigration "
            "waves of the 1840s, which had packed the "
            "city's tenement districts to crisis density. "
            "The 1849 cholera epidemic struck these "
            "overcrowded neighborhoods with particular "
            "ferocity, killing thousands within weeks.\n\n"
            "His response to the epidemic, while limited "
            "by contemporary medical understanding (germ "
            "theory was decades away), involved deploying "
            "the Board of Health's resources and attempting "
            "to clean the worst tenement conditions. "
            "His administration also dealt with rapid "
            "physical expansion — the period saw major "
            "construction projects and the pressures "
            "of governing a city already becoming one "
            "of the world's largest.\n\n"
            "His mayoral career captured the challenge "
            "facing American urban government in the "
            "mid-nineteenth century: managing explosive "
            "growth, immigration, and public health "
            "crises with administrative tools built "
            "for a much smaller city."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Mayor of New York City (1849–1851) during the devastating cholera epidemic of 1849; his administration managed the city's public health response to a disease event that killed over 5,000 New Yorkers and confronted the consequences of mass immigration and rapid urban growth.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's explosive mid-nineteenth-century growth — driven by the mass immigration of Irish and German refugees from the famine and revolutions of the 1840s — created the overcrowded tenement conditions that made the 1849 cholera epidemic so catastrophic and placed enormous pressure on the city's inadequate public health infrastructure",
            "The cholera pandemic of 1849 — the second major epidemic wave to strike North America — spread rapidly through contaminated water supplies in overcrowded urban areas, confronting New York's mayor with a public health emergency that overwhelmed existing administrative capacity",
            "The Whig Party's urban reform tradition — which emphasized civic improvement, public order, and the active management of growing cities — provided the political framework through which Woodhull approached the challenges of governing a rapidly expanding metropolis"
        ],
        "effects": [
            "His administration's response to the 1849 cholera epidemic — however limited by contemporary medical ignorance — helped establish the principle that municipal government had a responsibility to intervene in public health crises, contributing to the long-term development of New York's public health infrastructure",
            "His mayoral tenure coincided with New York City's emergence as the largest city in North America, and his experience managing cholera, immigration, and rapid growth contributed to the institutional learning that shaped subsequent New York City administrations",
            "The 1849 cholera epidemic during his watch accelerated public demand for improved water and sanitation infrastructure — demands that eventually produced the Croton water system improvements that reduced New York's vulnerability to waterborne disease",
            "His career as a Whig mayor captured the Whig Party's urban civic management tradition at its moment of historical transition — the Whig Party would collapse in the 1850s over slavery, and Woodhull's brand of urban Whiggery would give way to the emerging Republican Party"
        ],
        "relationships": [
            {"target": "new-york-city", "verb": "GOVERNS", "note": "Mayor of New York City 1849–1851"},
            {"target": "cholera-epidemic-1849", "verb": "RESPONDS_TO", "note": "Mayor during devastating 1849 cholera outbreak"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Whig politician in New York City"},
            {"target": "irish-immigration-1840s", "verb": "GOVERNS_DURING", "note": "Mayoralty coincided with peak Irish and German immigration wave"},
            {"target": "new-york-board-of-health", "verb": "DIRECTS", "note": "Deployed Board of Health resources during cholera emergency"}
        ]
    }),

    # 4 — Enevold De Falsen
    ("enevold-de-falsen", {
        "summary": (
            "Enevold De Falsen (1755–1808) was a Norwegian "
            "lawyer, judge, and public official who served "
            "as a prominent legal figure in the Danish-Norwegian "
            "state during the late eighteenth century. "
            "Father of Christian Magnus Falsen — one of "
            "the principal authors of the Norwegian "
            "Constitution of 1814 — Enevold De Falsen's "
            "legal career and civic example directly "
            "influenced his son's constitutional work, "
            "making his family legacy inseparable from "
            "Norwegian constitutional history.\n\n"
            "Born in Copenhagen, Enevold De Falsen served "
            "in the Danish legal system as a county "
            "governor (amtmann) in Norway, where he "
            "exercised administrative authority in the "
            "Norwegian provinces of the dual monarchy. "
            "His career embodied the Danish-Norwegian "
            "governing class of the Enlightenment era — "
            "educated in the civil law tradition, committed "
            "to rational administration, and shaped by "
            "the reforming absolutism of the Danish crown.\n\n"
            "His writings included legal and philosophical "
            "essays that engaged with Enlightenment ideas "
            "on natural law, governance, and civil society. "
            "He died in 1808, six years before Norway's "
            "constitutional revolution, but his intellectual "
            "formation and legal example shaped the younger "
            "generation of Norwegian constitutional thinkers "
            "that included his son Christian Magnus.\n\n"
            "His significance lies primarily in his role "
            "as the intellectual progenitor of a constitutional "
            "family dynasty — a father whose legal career "
            "and Enlightenment thought prepared the ground "
            "for his son's constitutional achievement."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian lawyer and county governor in the Danish-Norwegian state; father of Christian Magnus Falsen, principal drafter of the Norwegian Constitution of 1814; Enlightenment legal thinker whose intellectual legacy shaped Norway's constitutional generation.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Danish-Norwegian Enlightenment administrative tradition — which trained lawyers and officials in natural law theory, rational governance, and civil law — formed Enevold De Falsen as both a legal practitioner and a philosophical thinker whose writings engaged with Enlightenment questions about governance and civil society",
            "The dual Danish-Norwegian monarchy's need for educated legal officials to govern its Norwegian provinces created the administrative career in which Enevold De Falsen served as county governor, giving him both practical governmental experience and the prestige that made his example influential for his son",
            "The intellectual environment of late-eighteenth-century Scandinavia — in which Enlightenment natural law theory was actively debated and applied to questions of governance — shaped Enevold De Falsen's legal philosophy and provided the intellectual inheritance he passed to his constitutional son"
        ],
        "effects": [
            "His legal career and philosophical writings provided the intellectual and professional model that shaped his son Christian Magnus Falsen's formation as a lawyer-constitutional thinker — making Enevold's legacy inseparable from the Norwegian Constitution of 1814",
            "His service as county governor in Norway gave him direct experience of the gap between Danish administrative practice and Norwegian needs — an experience that may have influenced his son's constitutional thinking about Norwegian self-governance",
            "His engagement with Enlightenment natural law theory contributed to the intellectual culture from which the Norwegian constitutional generation of 1814 emerged — a culture that blended legal training with philosophical reflection on the foundations of legitimate government",
            "His family's legal tradition made the Falsen name one of the most distinguished in Norwegian legal and constitutional history — a dynasty whose impact on Norwegian public life extended well beyond Enevold himself"
        ],
        "relationships": [
            {"target": "christian-magnus-falsen", "verb": "PARENT_OF", "note": "Father of the principal drafter of the Norwegian Constitution"},
            {"target": "norwegian-constitution-1814", "verb": "INFLUENCES", "note": "His legal legacy shaped his son's constitutional work"},
            {"target": "danish-norwegian-monarchy", "verb": "SERVES", "note": "County governor (amtmann) in Norwegian provinces"},
            {"target": "norwegian-enlightenment", "verb": "PARTICIPATES_IN", "note": "Legal philosopher engaging with natural law and governance"},
            {"target": "norway", "verb": "GOVERNS_IN", "note": "Administrative official in Norwegian provinces"}
        ]
    }),

    # 5 — Henry St. George Tucker Sr.
    ("henry-st-george-tucker-sr", {
        "summary": (
            "Henry St. George Tucker Sr. (1780–1848) was a "
            "Virginia lawyer, judge, and legal educator who "
            "served on the Virginia Court of Appeals and as "
            "a Chancellor of Virginia, while also writing "
            "important legal commentaries that helped "
            "codify Virginia's common law tradition. "
            "Son of the jurist St. George Tucker and "
            "member of one of Virginia's most distinguished "
            "legal dynasties, he inherited and extended "
            "a family tradition of legal scholarship "
            "that shaped Virginia law across three generations.\n\n"
            "Tucker was educated at the College of William "
            "and Mary and read law under his father's "
            "guidance — absorbing both the technical "
            "common law tradition and the broader "
            "Whig constitutionalist political philosophy "
            "that characterized Virginia's legal culture. "
            "He built a career as a practicing lawyer "
            "before ascending to the Virginia Court of "
            "Appeals, where he served as a respected judge.\n\n"
            "He also served briefly in the United States "
            "Congress (1815–1819), representing Virginia "
            "as a Democratic-Republican. His congressional "
            "career was notable for his opposition to "
            "federal internal improvements — a states'-rights "
            "position consistent with the Virginia school "
            "of constitutional interpretation.\n\n"
            "His legal writings, including commentaries "
            "on Virginia law, continued the Tucker family "
            "tradition of systematic legal exposition "
            "that his father St. George Tucker had "
            "established with his edition of Blackstone's "
            "Commentaries — making the Tuckers a true "
            "dynasty of American legal scholarship."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia judge, legal commentator, and Congressman; son of St. George Tucker and member of Virginia's most distinguished legal dynasty; served on Virginia Court of Appeals and as Chancellor; continued the Tucker family tradition of legal scholarship that shaped Virginia common law across three generations.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Tucker family legal dynasty — founded by St. George Tucker's landmark edition of Blackstone's Commentaries (1803) with its American constitutional annotations — gave Henry St. George Tucker both an intellectual inheritance and a family tradition of systematic legal scholarship to continue and build upon",
            "Virginia's dominance of early American legal and political culture — producing figures like Jefferson, Madison, Marshall, and the Tucker jurists — created an environment of legal excellence in which Henry St. George Tucker could rise to prominence in state judicial and political life",
            "The Virginia states'-rights constitutional tradition — which interpreted federal power narrowly and emphasized state legislative and judicial sovereignty — shaped Tucker's political career in Congress and his judicial philosophy on the Virginia Court of Appeals"
        ],
        "effects": [
            "His judicial service on the Virginia Court of Appeals contributed to the development of Virginia common law doctrine in the early nineteenth century, helping shape the legal rules governing property, contracts, and civil liability in the Commonwealth",
            "His legal commentaries extended the Tucker family tradition of systematic legal exposition into the middle decades of the nineteenth century, maintaining Virginia's reputation as a center of American legal scholarship",
            "His congressional career (1815–1819) added political experience to his legal resume and demonstrated the Virginia legal dynasty's capacity to move between judicial, legislative, and academic roles — a versatility characteristic of the Virginia gentry class",
            "His career helped train the next generation of Tucker lawyers — his son John Randolph Tucker also became a distinguished Virginia jurist — sustaining a legal dynasty whose influence on Virginia and American law extended across a full century"
        ],
        "relationships": [
            {"target": "st-george-tucker", "verb": "CHILD_OF", "note": "Son of America's first systematic legal commentator"},
            {"target": "virginia-court-of-appeals", "verb": "SERVES_ON", "note": "Judge on Virginia's highest court"},
            {"target": "us-congress", "verb": "SERVES_IN", "note": "Virginia Congressman 1815–1819"},
            {"target": "virginia-law", "verb": "COMMENTATES", "note": "Legal writings on Virginia common law"},
            {"target": "tucker-legal-dynasty", "verb": "CONTINUES", "note": "Extended three-generation Tucker tradition of legal scholarship"}
        ]
    }),

    # 6 — Henry Dutton
    ("henry-dutton", {
        "summary": (
            "Henry Dutton (1796–1869) was a Connecticut "
            "lawyer, judge, and politician who served as "
            "Governor of Connecticut (1854–1855) and as "
            "a Justice of the Connecticut Supreme Court "
            "of Errors. A Whig and later Republican, "
            "Dutton built his career at the intersection "
            "of legal practice, judicial service, and "
            "academic teaching — serving as a professor "
            "of law at Yale Law School, one of America's "
            "oldest law schools.\n\n"
            "Educated at Yale College and admitted to "
            "the Connecticut bar, Dutton established "
            "himself as a leading Connecticut lawyer "
            "before ascending to judicial office. His "
            "appointment to the Connecticut Supreme "
            "Court of Errors placed him among the "
            "state's highest legal authorities, where "
            "his opinions contributed to Connecticut's "
            "jurisprudence in the antebellum period.\n\n"
            "His governorship (1854–1855) came at a "
            "politically turbulent moment — the Whig "
            "Party was collapsing over the Kansas-Nebraska "
            "Act (1854), which reopened the slavery "
            "question and shattered the party system "
            "that Dutton had operated within. His "
            "single term as governor bridged the "
            "Whig-to-Republican transition in Connecticut "
            "politics.\n\n"
            "His professorship at Yale Law School gave "
            "him an academic platform to shape legal "
            "education in Connecticut, training future "
            "lawyers in the methods and traditions "
            "of American common law practice."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Connecticut (1854–1855), Connecticut Supreme Court Justice, and Yale Law School professor; Whig and early Republican who navigated the collapse of the Whig Party over the Kansas-Nebraska Act; contributed to Connecticut jurisprudence and legal education.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's tradition of Yale-educated lawyer-politicians — in which legal training, judicial service, and political office were routinely combined — shaped Dutton's career trajectory from law professor to Supreme Court justice to governor",
            "The Whig Party's political dominance in New England during the 1840s and its subsequent collapse over the Kansas-Nebraska Act (1854) defined the partisan environment of Dutton's political career, making his governorship an episode in the turbulent transition from Whig to Republican politics",
            "The expansion of American legal education in the antebellum period — with Yale Law School, Harvard Law School, and other institutions professionalizing legal training — created the academic platform from which Dutton could exercise influence over Connecticut's legal culture beyond his judicial role"
        ],
        "effects": [
            "His service on the Connecticut Supreme Court of Errors contributed to Connecticut's common law jurisprudence in the antebellum decades, helping develop the legal rules governing commercial, property, and civil matters in the state",
            "His governorship contributed to the management of Connecticut's political transition from Whiggery to Republicanism during the tumultuous 1854–1855 period — helping stabilize Connecticut's governance during the party system's crisis",
            "His professorship at Yale Law School contributed to the training of Connecticut lawyers in the antebellum era, sustaining Yale's role as the primary institution for legal education in New England",
            "His career exemplified the pattern of the antebellum New England lawyer-jurist-politician — whose simultaneous commitments to legal practice, judicial service, academic teaching, and electoral politics embodied the civic ideal of the learned professional in American public life"
        ],
        "relationships": [
            {"target": "connecticut", "verb": "GOVERNS", "note": "Governor of Connecticut 1854–1855"},
            {"target": "connecticut-supreme-court", "verb": "SERVES_ON", "note": "Justice of the Supreme Court of Errors"},
            {"target": "yale-law-school", "verb": "TEACHES_AT", "note": "Professor of law at Yale"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Whig politician transitioning to Republican Party"},
            {"target": "kansas-nebraska-act-1854", "verb": "GOVERNS_DURING", "note": "Governorship coincided with Whig collapse over slavery question"}
        ]
    }),

    # 7 — Manuel Silvela y García de Aragón
    ("manuel-silvela-y-garcía-de-aragón", {
        "summary": (
            "Manuel Silvela y García de Aragón (1781–1832) "
            "was a Spanish liberal lawyer, politician, and "
            "diplomat who navigated the turbulent politics "
            "of the early Spanish liberal constitutional "
            "era. A supporter of the Constitution of Cádiz "
            "(1812), he served in various governmental "
            "capacities under the constitutional and "
            "absolutist regimes that alternated in "
            "Spain during the 1810s–1820s, embodying "
            "the dangerous position of the Spanish liberal "
            "who lived between constitutionalism and "
            "Fernandine reaction.\n\n"
            "Silvela was born in Segovia into a distinguished "
            "family that would produce several generations "
            "of Spanish politicians — the Silvela political "
            "dynasty remained influential in Spanish "
            "politics through the nineteenth century "
            "and into the Restoration era. Manuel was "
            "trained as a jurist and became an advocate "
            "at the Spanish courts before being drawn "
            "into the constitutional politics unleashed "
            "by Napoleon's 1808 invasion.\n\n"
            "The Constitution of Cádiz (1812) — drafted "
            "by the liberal Cortes while most of Spain "
            "was under French occupation — represented "
            "the culmination of Spanish constitutional "
            "liberalism. Silvela's support for this "
            "document placed him among the Spanish liberals "
            "who faced persecution under Ferdinand VII's "
            "absolutist reaction after 1814 and again "
            "after 1823.\n\n"
            "His diplomatic service included representation "
            "of Spanish interests abroad during the "
            "constitutional trienio (1820–1823), before "
            "Ferdinand's final absolutist restoration "
            "drove Spanish liberals into exile."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish liberal lawyer and diplomat who supported the Constitution of Cádiz (1812); navigated the dangerous alternation between constitutionalism and Fernandine absolutism in early nineteenth-century Spain; patriarch of the Silvela political dynasty that remained influential through the Spanish Restoration era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's 1808 invasion of Spain and the collapse of the Bourbon monarchy — which triggered the Peninsular War and the convening of the liberal Cortes of Cádiz — created the constitutional crisis in which Spanish liberals like Silvela committed to the Constitution of 1812 as the template for a reformed Spanish state",
            "Ferdinand VII's repeated absolutist restorations (1814, 1823) — which persecuted, imprisoned, and exiled the liberals who had supported the Constitution of Cádiz — defined the dangerous political environment in which Silvela had to navigate between constitutional principle and personal safety",
            "The Silvela family's position in Spanish legal and political culture — as a distinguished dynasty of lawyers and public officials — gave Manuel the social capital and professional training to operate at the intersection of law, diplomacy, and liberal politics"
        ],
        "effects": [
            "His support for the Constitution of Cádiz aligned him with the generation of Spanish liberals who established the constitutional tradition that shaped Spanish politics through the nineteenth century, even as Fernandine reaction repeatedly suppressed it",
            "His diplomatic service during the constitutional trienio (1820–1823) contributed to the international representation of Spain's brief constitutional government before Ferdinand VII's restoration ended the experiment",
            "The Silvela political dynasty he helped establish went on to produce significant Spanish politicians — most notably Francisco Silvela (1843–1905), Conservative prime minister under the Restoration — demonstrating the multi-generational impact of his family's political engagement",
            "His career exemplified the fate of the Spanish constitutional liberal in the early nineteenth century — committed to rational governance and constitutional order, repeatedly victimized by absolutist reaction, and forced to operate in the dangerous gap between constitutional idealism and royal power"
        ],
        "relationships": [
            {"target": "constitution-of-cadiz-1812", "verb": "SUPPORTS", "note": "Liberal supporter of Spain's first constitutional document"},
            {"target": "ferdinand-vii-of-spain", "verb": "OPPOSES", "note": "Liberal opposed to Fernandine absolutist reaction"},
            {"target": "silvela-political-dynasty", "verb": "FOUNDS", "note": "Patriarch of the Silvela political family"},
            {"target": "spanish-liberal-movement", "verb": "PARTICIPATES_IN", "note": "Liberal constitutional politician in early 19th-century Spain"},
            {"target": "cortes-of-cadiz", "verb": "SUPPORTS", "note": "Backed the liberal constitutional Cortes"}
        ]
    }),

    # 8 — Modesto Cortázar
    ("modesto-cortázar", {
        "summary": (
            "Modesto Cortázar (1806–1868) was a Spanish "
            "engineer, cartographer, and geodesist whose "
            "technical surveys contributed to the development "
            "of modern Spanish cartography and the precise "
            "measurement of Spain's territory in the "
            "mid-nineteenth century. His work on the "
            "triangulation surveys that underpinned "
            "Spain's first scientific topographic maps "
            "was part of the broader European effort to "
            "apply the new precision sciences to national "
            "territorial documentation.\n\n"
            "Cortázar was trained as a military engineer "
            "— the branch of the Spanish army responsible "
            "for the technical sciences of fortification, "
            "surveying, and territorial mapping. Military "
            "engineers were the primary agents of "
            "scientific cartography in nineteenth-century "
            "Europe, combining mathematical precision "
            "with the logistical capacity to conduct "
            "surveys across large national territories.\n\n"
            "His geodetic work contributed to establishing "
            "the precise coordinates of Spanish territory "
            "through triangulation networks — the method "
            "by which surveyors measured large distances "
            "and elevations with precision by building "
            "geometric chains of triangles across the "
            "landscape. This work fed into the Spanish "
            "General Staff's efforts to produce accurate "
            "military and civil maps of the peninsula.\n\n"
            "His technical career exemplified the "
            "nineteenth-century integration of science, "
            "military technology, and state administration "
            "in the project of accurately documenting "
            "national territory — a project that had "
            "both military and civil governance applications."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Spanish military engineer and geodesist whose triangulation surveys contributed to the development of modern Spanish scientific cartography in the mid-nineteenth century; technical practitioner in the European project of applying precision geodesy to national territorial documentation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The European scientific revolution in geodesy and cartography — driven by improvements in triangulation methods, precision instruments, and mathematical computation — created the technical capacity for national territorial surveys that governments across Europe undertook in the nineteenth century",
            "Spain's military and civil governance needs for accurate maps — for military planning, tax assessment, land registration, and infrastructure development — drove the Spanish state's investment in geodetic surveys and the training of military engineers in precision surveying methods",
            "The Spanish Corps of Engineers' role as the primary institution for technical sciences in the Spanish army — responsible for fortification, surveying, and applied mathematics — provided Cortázar with both his technical training and the institutional resources to conduct large-scale geodetic operations"
        ],
        "effects": [
            "His geodetic triangulation surveys contributed to the scientific foundation for Spain's first accurate topographic maps — work that had both military strategic value and civil administrative utility for a state attempting to govern its territory with greater precision",
            "His technical work helped establish the geodetic reference framework for Spanish cartography — the network of precisely measured points from which subsequent mapping surveys could be referenced — contributing to the long-term accuracy of Spanish geographical documentation",
            "His career contributed to the development of the Spanish technical military culture that combined rigorous mathematical training with practical fieldwork — a culture that produced Spain's most sophisticated scientists and engineers in the nineteenth century",
            "His surveys contributed data to the European geodetic networks that sought to determine the exact shape of the Earth — one of the great scientific projects of the nineteenth century that required international coordination of national geodetic surveys"
        ],
        "relationships": [
            {"target": "spanish-corps-of-engineers", "verb": "SERVES_IN", "note": "Military engineer trained in precision surveying"},
            {"target": "spanish-cartography", "verb": "ADVANCES", "note": "Triangulation surveys for Spain's first scientific maps"},
            {"target": "geodesy", "verb": "PRACTICES", "note": "Geodetic triangulation networks across Spanish territory"},
            {"target": "spain", "verb": "SERVES", "note": "Technical surveys for Spanish military and civil administration"},
            {"target": "european-geodetic-science", "verb": "CONTRIBUTES_TO", "note": "Spanish geodesy connected to European precision science networks"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 52 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
