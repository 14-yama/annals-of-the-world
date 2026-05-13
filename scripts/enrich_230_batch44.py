#!/usr/bin/env python3
"""
Batch 44 — 8 entities: Christian Heinrich Postel, Thomas W. Cobb, Andrew Adams,
Joseph Hemphill, William Livingston, Njáll Þorgeirsson, Joshua Baker, David Plant
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

    # 1 — Christian Heinrich Postel
    ("christian-heinrich-postel", {
        "summary": (
            "Christian Heinrich Postel (1658–1705) was a German "
            "jurist, epic poet, and opera librettist who became "
            "one of the founding figures of German Baroque opera "
            "through his prolific work for the Oper am Gänsemarkt "
            "in Hamburg — the first public opera house in the "
            "German-speaking world, opened in 1678. He wrote "
            "28 libretti for the Hamburg company, set by the "
            "leading composers of the north German Baroque "
            "tradition including Johann Philipp Förtsch, "
            "Reinhard Keiser, and Georg Philipp Telemann.\n\n"
            "Born in Freiburg im Breisgau, he studied law and "
            "built a parallel career as a Hamburg city official "
            "alongside his literary work. His Hamburg context "
            "was culturally distinctive: as a major commercial "
            "city and Lutheran center, Hamburg developed a "
            "Protestant Baroque opera tradition that was "
            "simultaneously cosmopolitan (drawing on Italian "
            "opera models) and vernacular (adapting them to "
            "German-language texts and northern Protestant culture).\n\n"
            "His most historically significant literary contribution "
            "was his St John Passion libretto — a setting of "
            "the Gospel of John's crucifixion narrative for "
            "oratorio performance — which became one of the "
            "most influential passion libretto texts of the "
            "early 18th century. Johann Sebastian Bach used "
            "a version of Postel's text for his own St John "
            "Passion (BWV 245, 1724) — though Bach extensively "
            "revised and supplemented it — connecting Postel's "
            "Hamburg Baroque world directly to the greatest "
            "choral work of the German Lutheran tradition.\n\n"
            "His 28 Hamburg libretti made him one of the most "
            "prolific and consequential figures in the development "
            "of German-language opera in the critical foundational "
            "decade of the 1680s–1700s."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "German Baroque jurist, epic poet, and opera librettist; wrote 28 libretti for the Oper am Gänsemarkt in Hamburg (first public German-language opera house); St John Passion libretto text used by J.S. Bach for BWV 245 (1724); worked with Keiser, Förtsch, and Telemann; one of the founding figures of German Baroque opera's Hamburg tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The founding of the Oper am Gänsemarkt in Hamburg in 1678 — the first permanent public opera house in the German-speaking world — created the institutional context for Postel's prolific libretto writing, as the company needed a continuous supply of new German-language texts to sustain its annual opera season",
            "Hamburg's cultural position as a cosmopolitan Lutheran commercial city — simultaneously open to Italian opera's formal innovations and committed to German-language vernacular culture — created the distinctive Protestant Baroque opera tradition that Postel's libretti helped to define and populate",
            "The development of the German-language passion oratorio tradition — in which Lutheran composers adapted the liturgical commemoration of Christ's death for theatrical performance — created the demand for textual models like Postel's St John Passion libretto that provided composers with structured poetic texts combining biblical narrative with devotional poetry"
        ],
        "effects": [
            "His 28 Hamburg libretti contributed to the establishment of German-language opera as a viable and culturally significant art form — demonstrating that German texts could sustain the full range of Baroque operatic genres (heroic, pastoral, biblical) that Italian opera had established",
            "His St John Passion libretto text — set by Bach as BWV 245 in 1724 — contributed directly to the creation of one of the masterworks of Western choral music, connecting the Hamburg Baroque opera world to the peak of Lutheran church music through Bach's use and transformation of his textual framework",
            "His collaboration with Reinhard Keiser — the dominant composer of the Hamburg opera in its formative years — contributed to establishing the Hamburg Baroque opera's distinctive musical and textual aesthetic, which influenced later German composers including Handel, who worked in Hamburg (1703–1706) and absorbed the local tradition",
            "His dual career as a Hamburg city official and opera librettist contributed to the institutional model of Hamburg's early modern cultural life — in which legal and civic officeholders simultaneously participated in the city's literary and musical culture as patrons, writers, and artistic figures"
        ],
        "relationships": [
            {"entity": "Oper am Gänsemarkt Hamburg (28 libretti, 1680s–1700s)", "relationship": "PRIMARY_LIBRETTIST_OF", "note": "Wrote 28 libretti for the Oper am Gänsemarkt — the first permanent public opera house in the German-speaking world — making him one of the most prolific contributors to its founding repertoire"},
            {"entity": "J.S. Bach / St John Passion BWV 245 (1724, Postel libretto adapted)", "relationship": "PROVIDED_SOURCE_LIBRETTO_FOR", "note": "Provided the source libretto text that J.S. Bach adapted for his St John Passion (BWV 245, 1724) — the greatest choral work of the German Lutheran tradition, directly connecting Postel's Hamburg Baroque world to Bach"},
            {"entity": "Reinhard Keiser (Hamburg opera composer, set multiple Postel libretti)", "relationship": "COLLABORATED_WITH", "note": "Collaborated with Reinhard Keiser — the dominant composer of the Hamburg Baroque opera — who set multiple Postel libretti, establishing the Hamburg opera's foundational aesthetic"},
            {"entity": "Georg Philipp Telemann / Johann Philipp Förtsch (composers of Postel texts)", "relationship": "LIBRETTIST_FOR", "note": "Provided libretti set by Telemann and Förtsch — contributors to the Hamburg Baroque opera tradition whose works were built on Postel's textual foundations"},
            {"entity": "Hamburg Protestant Baroque opera tradition (German-language, Lutheran, 1678–1750s)", "relationship": "FOUNDING_LITERARY_FIGURE_OF", "note": "One of the founding literary figures of the Hamburg Protestant Baroque opera tradition — demonstrating the viability of German-language operatic texts and shaping the aesthetic of the tradition's critical formative decades"}
        ]
    }),

    # 2 — Thomas W. Cobb
    ("thomas-w-cobb", {
        "summary": (
            "Thomas Willis Cobb (1784–1830) was a Georgia lawyer, "
            "politician, and judge who served as US Representative "
            "from Georgia (1817–1821) and US Senator (1824–1828) "
            "before his appointment as a Georgia Superior Court "
            "judge — a career that made him one of the more "
            "significant figures in Georgia's post-Revolutionary "
            "political development. Cobb County, Georgia, was "
            "named in his honor.\n\n"
            "His congressional career coincided with some of the "
            "most significant legislative moments of the early "
            "republic: as a US Representative he was present "
            "during the Missouri Compromise debates of 1819–1821, "
            "and as a Senator he served during the critical "
            "years of the Adams-Jackson contest and the "
            "Jacksonian political transformation. A Georgia "
            "Democrat, he represented the state's planter-class "
            "political establishment during the transition "
            "from the Era of Good Feelings to Jacksonian democracy.\n\n"
            "His legal career was the foundation of his public "
            "life: he practiced law in Athens, Georgia, and his "
            "Superior Court appointment completed a public "
            "career that spanned the executive, legislative, "
            "and judicial branches. Georgia's early political "
            "culture — dominated by planter-lawyer combinations "
            "drawn from Piedmont and coastal communities — "
            "produced the pattern of career that Cobb exemplified.\n\n"
            "He died in 1830 — the year Georgia's Indian "
            "Removal Act politics were reaching their crisis "
            "point — leaving Cobb County as his most enduring "
            "memorial in a state whose history he had helped "
            "to build."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia US Representative (1817–1821) and US Senator (1824–1828); Georgia Superior Court judge; Cobb County (Georgia) named in his honor; present during Missouri Compromise debates and the Jacksonian political transition; representative figure of Georgia's post-Revolutionary planter-lawyer political establishment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's post-Revolutionary planter-lawyer political establishment — which produced the combination of legal training, plantation management, and political ambition that characterized the state's congressional delegation in the early 19th century — created the career pattern that Cobb followed from lawyer to congressman to senator to judge",
            "The Missouri Compromise crisis (1819–1821) — in which Congress debated whether to admit Missouri as a slave state and whether to restrict slavery in the Louisiana Purchase territories — created the political context for Cobb's most significant congressional engagement, as a Georgia Democrat defending the South's position on the slavery-in-the-territories question",
            "Georgia's rapid post-Revolutionary population growth and political institutionalization — with new counties, Superior Courts, and congressional districts being created throughout the first decades of statehood — created the expanding institutional framework of judicial and legislative positions that supported careers like Cobb's"
        ],
        "effects": [
            "His House and Senate service contributed to Georgia's representation during the Missouri Compromise debates and the Jacksonian political transformation — articulating Georgia's planter-class perspective on the most contested political questions of the era",
            "His Superior Court service contributed to the development of Georgia's judicial system — applying the state's evolving legal code in one of the judicial circuits that were building Georgia's common law tradition in the antebellum period",
            "Cobb County's naming in his honor gave him a permanent geographic memorial in Georgia — a county that grew to become one of the most populous and economically significant in the state, extending his name recognition far beyond his own lifetime",
            "His career as a Georgia planter-lawyer congressman-senator-judge exemplified the institutional pattern by which Georgia's antebellum political class managed the state's multiple governing institutions — a pattern that would shape Georgia politics until the Civil War fundamentally transformed it"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Georgia (1817–1821)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from Georgia (1817–1821) — present during the Missouri Compromise debates and the transition from the Era of Good Feelings"},
            {"entity": "US Senate from Georgia (1824–1828)", "relationship": "SENATOR", "note": "Served as US Senator from Georgia (1824–1828) — representing the state during the critical Adams-Jackson contest and the emergence of Jacksonian democracy"},
            {"entity": "Georgia Superior Court (judge, appointed)", "relationship": "JUDGE", "note": "Served as a Georgia Superior Court judge — completing a trifecta of legislative, executive, and judicial service characteristic of Georgia's antebellum political establishment"},
            {"entity": "Missouri Compromise (1819–1821) / slavery in territories debates", "relationship": "CONGRESSMAN_DURING", "note": "Present in the House during the Missouri Compromise debates (1819–1821) — as a Georgia Democrat, representing the South's position on the slavery-in-the-territories question"},
            {"entity": "Cobb County, Georgia (named in his honor)", "relationship": "NAMESAKE_OF", "note": "Cobb County, Georgia — one of the state's most populous counties — was named in his honor, providing a lasting geographic memorial to his contribution to Georgia's political development"}
        ]
    }),

    # 3 — Andrew Adams
    ("andrew-adams", {
        "summary": (
            "Andrew Adams (1736–1797) was a Connecticut Founding "
            "Father — a lawyer, judge, and political leader who "
            "served as a delegate to the Second Continental "
            "Congress and signed the Articles of Confederation "
            "in 1778, and later as Chief Justice of the Connecticut "
            "Supreme Court (1793–1797). Born in Stratford, "
            "Connecticut, he graduated from Yale College in 1760, "
            "studied law, and built a legal practice in Litchfield, "
            "Connecticut — establishing himself in one of the "
            "state's most legally distinguished communities.\n\n"
            "His Continental Congress service (1778) placed him "
            "in Philadelphia at the moment of the Articles of "
            "Confederation's completion — the first framework "
            "of American federal governance, which he signed "
            "as part of Connecticut's delegation. His signing "
            "committed Connecticut formally to the confederated "
            "union that would govern the new nation through "
            "the Revolutionary War's conclusion.\n\n"
            "His post-war judicial career culminated in his "
            "appointment as Chief Justice of Connecticut's "
            "Supreme Court in 1793 — the state's highest "
            "judicial office — where he served until his "
            "death in 1797. His four-year tenure on the "
            "state's highest bench contributed to Connecticut's "
            "early post-Revolutionary legal development, "
            "building on the strong common law tradition "
            "that the state's Yale-educated lawyers had "
            "inherited from colonial practice.\n\n"
            "His career exemplified the pattern of Connecticut's "
            "revolutionary generation: Yale education, "
            "legal training, Continental Congress service, "
            "and post-war judicial appointment — the "
            "institutional path that built the early republic's "
            "legal establishment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Founding Father; Yale 1760; Continental Congress delegate; signed the Articles of Confederation (1778); Chief Justice of the Connecticut Supreme Court (1793–1797); his career exemplifies Connecticut's revolutionary legal-political establishment pattern of Yale education, Continental Congress service, and post-war judicial appointment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's strong legal tradition — rooted in Yale College education, Litchfield Law School training, and the state's established common law practice — created the professional foundation for Adams's career and positioned him within the network of Connecticut lawyers who dominated the state's Revolutionary-era political institutions",
            "The Articles of Confederation's completion in 1778 — after more than a year of negotiation and revision — created the occasion for Adams's signing as a Connecticut delegate, connecting him permanently to the founding document of American federal governance",
            "Connecticut's post-Revolutionary need for experienced and senior lawyers to fill its new state Supreme Court positions — as the court system was reconstituted on American constitutional foundations after the war — created the demand for Adams's Chief Justice appointment in 1793"
        ],
        "effects": [
            "His signing of the Articles of Confederation contributed to Connecticut's formal commitment to the confederated American union — helping to ratify the first framework of American federal governance that governed the nation through the Revolution's conclusion and the Confederation period",
            "His Chief Justice service on the Connecticut Supreme Court contributed to the development of Connecticut's post-Revolutionary jurisprudence — building on the state's colonial legal tradition and adapting it to the new constitutional framework of the post-Independence era",
            "His career illustrated and reinforced the institutional pattern of Connecticut's founding generation — Yale education, legal training, Continental service, judicial appointment — a pattern that produced the lawyers and judges who built New England's legal institutions in the early republic",
            "Connecticut's delegation to the Continental Congress — of which Adams was a part during the Articles' completion — contributed to the consensus that made the first American federal union possible, establishing the precedent for interstate cooperation that would be extended and strengthened under the subsequent Constitution"
        ],
        "relationships": [
            {"entity": "Articles of Confederation (signed as Connecticut delegate, 1778)", "relationship": "SIGNER", "note": "Signed the Articles of Confederation in 1778 as a Connecticut Continental Congress delegate — committing the state to the first framework of American federal governance"},
            {"entity": "Second Continental Congress (Connecticut delegate, 1778)", "relationship": "DELEGATE", "note": "Served as a Connecticut delegate to the Second Continental Congress in 1778 — present at the completion and signing of the Articles of Confederation"},
            {"entity": "Chief Justice of the Connecticut Supreme Court (1793–1797)", "relationship": "CHIEF_JUSTICE", "note": "Served as Chief Justice of the Connecticut Supreme Court (1793–1797) — the state's highest judicial office — until his death, contributing to Connecticut's early post-Revolutionary jurisprudence"},
            {"entity": "Yale College (graduated 1760)", "relationship": "EDUCATED_AT", "note": "Graduated from Yale College in 1760 — part of the Yale-educated cohort of Connecticut lawyers who dominated the state's Revolutionary-era political and judicial institutions"},
            {"entity": "Connecticut founding generation / Litchfield legal community", "relationship": "MEMBER_AND_REPRESENTATIVE_OF", "note": "A member of Connecticut's founding generation of Yale-educated lawyers — practicing in Litchfield and contributing to the legal community that produced the state's Revolutionary-era political and judicial leadership"}
        ]
    }),

    # 4 — Joseph Hemphill
    ("joseph-hemphill", {
        "summary": (
            "Joseph Hemphill (1770–1842) was a Pennsylvania lawyer "
            "and politician whose long and varied congressional "
            "career spanned four decades across three distinct "
            "political alignments — serving as a Federalist "
            "US Representative (1801–1803), a Jackson Federalist "
            "representative (1819–1823), and a Jacksonian "
            "representative (1829–1831). Born in Thornbury, "
            "Pennsylvania, he attended college, studied law, "
            "and practiced in Philadelphia, building the legal "
            "standing that underpinned his political career.\n\n"
            "His most historically significant legislative act "
            "came during the Missouri Compromise debates: he "
            "opposed the admission of Missouri as a slave state "
            "and supported the Tallmadge Amendment, which would "
            "have required the gradual emancipation of enslaved "
            "people in Missouri as a condition of statehood. "
            "His opposition placed him among the minority of "
            "northern congressmen who were willing to resist "
            "the South's demands on the slavery-in-the-territories "
            "question — a position that anticipated the antislavery "
            "politics that would eventually produce the Republican Party.\n\n"
            "He later served as president judge of Philadelphia's "
            "District Court — completing a judicial career that "
            "paralleled his multiple legislative terms. "
            "His political trajectory — from Federalist to "
            "Jacksonian — illustrated the fragmentation and "
            "realignment of the first American party system "
            "across the 1800–1830 period.\n\n"
            "He was also a co-founder and early benefactor "
            "of Franklin Institute in Philadelphia — the "
            "technical and scientific institution founded "
            "in 1824 that became central to American industrial "
            "and engineering education."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania congressman across three political alignments (Federalist 1801–1803; Jackson Federalist 1819–1823; Jacksonian 1829–1831); opposed Missouri's admission as slave state and supported Tallmadge Amendment; Philadelphia District Court president judge; co-founder of the Franklin Institute (1824); his career illustrates the first American party system's fragmentation and realignment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Philadelphia's position as the center of Pennsylvania's legal and political life — combined with its status as the largest American city and the seat of the early federal government — created the institutional environment in which Hemphill could build both a legal practice and a multi-decade political career",
            "The Missouri Compromise crisis (1819–1821) and the Tallmadge Amendment debate created the occasion for Hemphill's most significant congressional moment — his opposition to Missouri's admission as a slave state placed him among the minority of northern congressmen willing to resist Southern demands on the slavery question at a critical moment in American political history",
            "The collapse and realignment of the first American party system — with Federalism dying, the Democratic-Republican coalition fragmenting, and the Jacksonian movement emerging — created the fluid political environment in which Hemphill's multiple shifts of party alignment were both possible and characteristic of his era"
        ],
        "effects": [
            "His support for the Tallmadge Amendment contributed to the northern congressional position in the Missouri Compromise debates — one of the minority voices arguing that the expansion of slavery into new states should be restricted, anticipating the antislavery politics that would emerge more powerfully in the 1840s–1850s",
            "His co-founding of the Franklin Institute (1824) contributed to the establishment of one of America's most important technical and scientific institutions — which provided engineering education and promoted industrial innovation in the critical decades of American industrialization",
            "His three-phase congressional career illustrating Federalist → Jackson Federalist → Jacksonian evolution contributed evidence for historians studying the first American party system's disintegration and the emergence of the second party system",
            "His Philadelphia District Court judicial service contributed to the development of Pennsylvania's federal judicial tradition — building the institutional capacity of the District Court system in the nation's largest urban center"
        ],
        "relationships": [
            {"entity": "US House from Pennsylvania (Federalist 1801–03; Jackson Federalist 1819–23; Jacksonian 1829–31)", "relationship": "THREE-PHASE_CONGRESSMAN", "note": "Served three separate congressional terms across four decades and three political alignments — Federalist, Jackson Federalist, and Jacksonian — illustrating the first party system's fragmentation"},
            {"entity": "Tallmadge Amendment / Missouri Compromise (supported anti-slavery admission terms)", "relationship": "SUPPORTED_ANTISLAVERY_POSITION_DURING", "note": "Supported the Tallmadge Amendment during Missouri Compromise debates — opposing Missouri's admission as a slave state and representing the minority northern congressional position on the slavery-in-territories question"},
            {"entity": "Franklin Institute, Philadelphia (co-founder, 1824)", "relationship": "CO-FOUNDED", "note": "Co-founded the Franklin Institute in Philadelphia in 1824 — the technical and scientific institution that became central to American industrial and engineering education"},
            {"entity": "Philadelphia District Court (president judge)", "relationship": "PRESIDENT_JUDGE", "note": "Served as president judge of Philadelphia's District Court — completing a judicial career alongside his multiple congressional terms"},
            {"entity": "First American party system (Federalist to Jacksonian, 1800–1831)", "relationship": "POLITICAL_TRAJECTORY_ILLUSTRATES_REALIGNMENT_OF", "note": "His three-phase partisan evolution from Federalist through Jackson Federalist to Jacksonian illustrated the first American party system's collapse and the formation of the Jacksonian coalition"}
        ]
    }),

    # 5 — William Livingston
    ("william-livingston", {
        "summary": (
            "William Livingston (1723–1790) was a New York-born "
            "lawyer, essayist, and statesman who became the "
            "first Governor of New Jersey (1776–1790) — "
            "serving for fourteen years, the entire duration "
            "of his state's Revolutionary War and early "
            "constitutional history. Born into one of New York's "
            "most powerful colonial families, he graduated from "
            "Yale in 1741, studied law under James Alexander, "
            "and became one of colonial New York's most prominent "
            "political and literary figures before moving to "
            "New Jersey.\n\n"
            "He represented New Jersey in the Continental Congress "
            "(1774–1776) and signed the Continental Association — "
            "the colonies' agreement to boycott British goods — "
            "before being commissioned as New Jersey's militia "
            "general at the outbreak of the Revolution. "
            "New Jersey's strategic position — between the "
            "two great Patriot cities of Philadelphia and "
            "New York — made it the site of more Revolutionary "
            "War engagements than any other state, and Livingston's "
            "fourteen-year governorship was spent managing "
            "a state under near-constant military threat.\n\n"
            "He represented New Jersey at the Constitutional "
            "Convention of 1787 and signed the United States "
            "Constitution — one of only six men to sign both "
            "the Continental Association and the Constitution, "
            "and one of the Convention's elder statesmen at 64.\n\n"
            "His pre-war career as a New York journalist and "
            "political pamphleteer — producing the Independent "
            "Reflector (1752–1753) and other polemical writings "
            "against Anglican establishment — made him one of "
            "the colonial era's most significant political writers "
            "alongside Franklin, Hamilton, and Jefferson."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Governor of New Jersey (1776–1790, 14 years — entire Revolutionary War period); Constitutional Convention delegate and signer of the US Constitution; Continental Congress delegate and Continental Association signer; New Jersey militia general; Yale 1741; prominent colonial New York journalist and political pamphleteer (Independent Reflector); one of only six men to sign both the Continental Association and the Constitution; one of the significant second-tier Founding Fathers.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New Jersey's strategically critical position between Philadelphia and New York — making it the most militarily contested state during the Revolutionary War — required a governor of Livingston's energy, political skill, and public stature to sustain New Jersey's Revolutionary government through fourteen years of near-continuous military crisis",
            "His Livingston family connections — one of the great colonial New York dynasties, allied with the DeLancey, Morris, and other leading families — gave him the social capital, political networks, and intellectual formation that enabled his career as both a political writer and a governing figure of the founding era",
            "The Constitutional Convention's need for experienced elder statesmen who could bridge the gap between the Revolutionary generation's commitments and the practical requirements of the new constitutional framework — and who had the state-level governing experience that younger delegates lacked — created a significant role for Livingston at Philadelphia in 1787"
        ],
        "effects": [
            "His fourteen-year New Jersey governorship contributed to sustaining New Jersey's Revolutionary government through the most militarily dangerous period in any American state's history — managing a state that hosted more battles than any other while maintaining the political and administrative continuity of Patriot governance",
            "His signing of the US Constitution as one of New Jersey's three delegates contributed to that state's ratification — New Jersey was one of the first states to ratify — and his presence as one of the elder statesmen of the Convention gave the document credibility with the Revolutionary generation's leadership",
            "His pre-war journalistic career — particularly the Independent Reflector (1752–1753), which he co-founded with William Smith Jr. and John Morin Scott — contributed to the development of colonial American political journalism as a vehicle for Whig political argument and anti-establishment polemic",
            "The Livingston family's broader contribution to the founding era — through William's governorship and Constitutional Convention service, his brother Philip's signing of the Declaration, and the family's networks with the Hamilton and Jay families — represented one of the most sustained dynastic contributions to the founding generation's institutional work"
        ],
        "relationships": [
            {"entity": "First Governor of New Jersey (1776–1790, 14 years, entire Revolutionary War)", "relationship": "14-YEAR_FIRST_GOVERNOR", "note": "Served as New Jersey's first Governor (1776–1790) — fourteen consecutive years through the entire Revolutionary War and early constitutional period — managing the most militarily contested state in America"},
            {"entity": "US Constitution (signer, Constitutional Convention 1787, New Jersey delegate)", "relationship": "SIGNER_AND_CONVENTION_DELEGATE", "note": "Represented New Jersey at the Constitutional Convention of 1787 and signed the US Constitution — one of only six men to sign both the Continental Association and the Constitution"},
            {"entity": "Continental Association (signer) / Continental Congress (New Jersey delegate, 1774–1776)", "relationship": "CONTINENTAL_CONGRESS_DELEGATE_AND_ASSOCIATION_SIGNER", "note": "Represented New Jersey in the Continental Congress (1774–1776) and signed the Continental Association — the colonial boycott agreement that preceded independence"},
            {"entity": "Independent Reflector (1752–1753, New York colonial political journal, co-founder)", "relationship": "CO-FOUNDED_AND_EDITED", "note": "Co-founded and edited the Independent Reflector (1752–1753) — one of colonial America's most significant political journals — making him a major figure in pre-Revolutionary American political journalism"},
            {"entity": "Livingston family dynasty (New York/New Jersey colonial elite, Founding generation)", "relationship": "LEADING_MEMBER_OF", "note": "Leading member of the Livingston family — one of colonial New York's great dynasties — whose family networks connected the governing elites of New York, New Jersey, and the early federal government"}
        ]
    }),

    # 6 — Njáll Þorgeirsson
    ("njáll-þorgeirsson", {
        "summary": (
            "Njáll Þorgeirsson (c.940–c.1011) was a 10th and "
            "early 11th-century Icelandic lawyer and farmer "
            "who lived at Bergþórshvoll in the Landeyjar region "
            "of southern Iceland, and who is the central "
            "protagonist of Njáls saga — one of the great "
            "Icelandic family sagas and one of the masterworks "
            "of medieval European prose fiction. While the "
            "historical Njáll certainly existed, the Njáll of "
            "the saga — his wisdom, his legal genius, his "
            "prophetic abilities, and the tragic arc of his "
            "family's destruction — is a literary construction "
            "of a 13th-century anonymous author working from "
            "oral and documentary sources roughly two centuries "
            "after the events described.\n\n"
            "In the saga, Njáll is portrayed as the greatest "
            "lawyer of his era — a man of extraordinary legal "
            "acuity who understands that law is the foundation "
            "of society and who dedicates his life to using "
            "the legal system to mediate the blood feuds that "
            "threaten Iceland's social fabric. His legal "
            "wisdom is juxtaposed with his personal inability "
            "to prevent the feud cycles from escalating — "
            "a tragic irony that gives the saga its distinctive "
            "moral weight.\n\n"
            "The saga's climax — Njáll, his wife Bergþóra, "
            "and their household's burning to death in their "
            "farm at Bergþórshvoll by their enemies — is one "
            "of the most famous scenes in Old Norse literature, "
            "and Njáll's calm acceptance of death became an "
            "emblem of the saga's Christian-pagan synthesis "
            "at the transition from the old Icelandic order.\n\n"
            "Njáls saga itself (c.1280) is considered the "
            "longest and most complex of the Íslendingasögur, "
            "and Njáll's character is among the most fully "
            "realized in medieval European literature."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Historical 10th–11th century Icelandic lawyer and farmer; central protagonist of Njáls saga (c.1280) — one of the great Icelandic family sagas; portrayed as the greatest Icelandic lawyer of his era; burned to death with his family at Bergþórshvoll — the saga's climactic scene; Njáls saga is the longest and most complex Íslendingasaga and Njáll's character one of the most fully realized in medieval European literature.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Iceland's unique legal-political system — the Althing, the goðorð system of chieftaincy, and the reliance on law and negotiation rather than executive authority to manage social conflict — created both the conditions for the blood feud cycles that the saga describes and the role of the great lawyer as the figure who tries to contain them",
            "The Christianization of Iceland (999–1000 CE) and the transition from the old Icelandic pagan-legal order to Christian ethics created the historical and cultural moment that Njáls saga captures — Njáll himself converting to Christianity, his calm acceptance of death representing the synthesis of old heroic values and new Christian resignation",
            "The saga writing tradition of 13th-century Iceland — in which anonymous authors retrospectively constructed narrative accounts of the 10th and 11th-century settlement and feud period — created the literary form that transformed the historical Njáll Þorgeirsson into the legendary figure of Njáls saga"
        ],
        "effects": [
            "Njáls saga (c.1280) contributed to the Icelandic saga tradition as its longest and most structurally complex example — demonstrating the genre's full capacity for social analysis, legal detail, psychological portraiture, and tragic narrative that no other saga achieved to the same degree",
            "Njáll's portrayal as the greatest Icelandic lawyer contributed to the cultural memory of the early Icelandic legal tradition — encoding the Althing's legal culture, the role of the lawspeaker, and the quasi-judicial processes of the 10th-century Icelandic commonwealth into one of medieval Europe's most widely read literary works",
            "The burning scene at Bergþórshvoll became one of Old Norse literature's most resonant set-pieces — Njáll's calm acceptance of death alongside his wife and household contributing to the saga's thematic synthesis of heroic stoicism and Christian martyrdom that defined the sagas' literary-theological vision",
            "The historical Njáll's documented existence — confirmed through independent Icelandic records — contributed to the ongoing scholarly debate about the relationship between saga literature and historical reality, making him one of the best-attested saga figures and a primary test case for the historiography of the Íslendingasögur"
        ],
        "relationships": [
            {"entity": "Njáls saga (c.1280, central protagonist, Icelandic family saga)", "relationship": "CENTRAL_PROTAGONIST_OF", "note": "Central protagonist of Njáls saga (c.1280) — the longest and most complex Icelandic family saga and one of the masterworks of medieval European prose fiction"},
            {"entity": "Bergþórshvoll (farm, Landeyjar, Iceland — burned with family c.1011)", "relationship": "LIVED_AND_BURNED_TO_DEATH_AT", "note": "Lived at Bergþórshvoll in southern Iceland and was burned to death there with his wife Bergþóra and household by their enemies — the saga's climactic and most famous scene"},
            {"entity": "Icelandic Althing / Commonwealth legal system (10th–11th century)", "relationship": "PRACTITIONER_OF_AS_LAWYER", "note": "The greatest lawyer of his era within the 10th–11th century Icelandic Althing system — dedicated to using legal process to mediate the blood feuds threatening Iceland's social fabric"},
            {"entity": "Christianization of Iceland (999–1000 CE)", "relationship": "CONTEMPORARY_AND_CONVERT", "note": "A contemporary of Iceland's Christianization (999–1000 CE) and himself a convert — his calm acceptance of death in the burning represents the saga's synthesis of heroic stoicism and Christian resignation"},
            {"entity": "Íslendingasögur / Icelandic family saga tradition (13th-century literary genre)", "relationship": "HISTORICAL_SUBJECT_AND_LITERARY_PROTAGONIST_OF", "note": "Both the historical subject of 13th-century saga writing and the literary protagonist of Njáls saga — the most fully realized figure in the Íslendingasögur tradition"}
        ]
    }),

    # 7 — Joshua Baker
    ("joshua-baker", {
        "summary": (
            "Joshua Gabriel Baker (1799–1885) was a Louisiana "
            "lawyer, engineer, and planter who served as "
            "military governor of Louisiana during "
            "Reconstruction from January to July 1868 — "
            "appointed by General Winfield Scott Hancock, "
            "commander of the Fifth Military District, "
            "as the military authority's civilian administrative "
            "head during the most contested phase of "
            "Louisiana's Reconstruction governance.\n\n"
            "Baker was among the relatively small group "
            "of Louisiana planters who had opposed secession "
            "and remained loyal to the Union during the "
            "Civil War — a position that made him acceptable "
            "to the Union military command as an administrative "
            "figure, while his planter background and Louisiana "
            "roots made him more palatable to the state's "
            "white political establishment than the Radical "
            "Republican alternatives.\n\n"
            "His brief seven-month tenure as military governor "
            "coincided with Louisiana's preparation for "
            "readmission to the Union — the state ratified "
            "the 14th Amendment and held elections for a "
            "new state government in 1868. The congressional "
            "Reconstruction Acts had placed Louisiana under "
            "military rule in 1867, and Baker's appointment "
            "was part of Hancock's effort to manage the "
            "transition with minimal confrontation.\n\n"
            "His Unionism and professional engineering background "
            "— alongside his legal and planting career — "
            "made him one of the more unusual figures of "
            "Louisiana's Reconstruction era, a planter-class "
            "Unionist navigating the explosive politics of "
            "a state that had been among the Confederacy's "
            "most committed members."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Military Governor of Louisiana during Reconstruction (January–July 1868); appointed by General Winfield Scott Hancock; Unionist Louisiana planter who opposed secession; presided over Louisiana's preparation for readmission — 14th Amendment ratification and 1868 state elections; Louisiana lawyer, engineer, and planter; his appointment illustrates the Union military's management of the transition from Reconstruction military rule to civil government.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The congressional Reconstruction Acts (1867) — which divided the former Confederate states into military districts under Union Army command — created the institutional framework that placed Louisiana under the Fifth Military District and created the position of military governor that Baker was appointed to fill",
            "Baker's Unionist position during the Civil War — his opposition to secession despite being a Louisiana planter — created his acceptability to General Hancock as a civilian administrative figure: he combined the social standing of the planter class with the political loyalty that the military command required",
            "The political pressure of Louisiana's 1868 readmission process — which required ratifying the 14th Amendment, holding elections for a new state government, and managing the competing claims of freedmen voters, Radical Republicans, and the white Democratic establishment — created the unstable political environment that Baker's brief governorship was meant to stabilize"
        ],
        "effects": [
            "His seven-month military governorship contributed to Louisiana's administrative management during the critical 1868 readmission process — overseeing the state's ratification of the 14th Amendment and the preparation of elections that would restore civilian governance",
            "His appointment by General Hancock contributed to the debate about the character of Reconstruction military rule in Louisiana — Hancock's 'soft' Reconstruction approach (which Baker embodied) was controversial among Radical Republicans who wanted more vigorous protection of freedmen's rights",
            "Louisiana's readmission to the Union in 1868 — which Baker's governorship helped to prepare — contributed to the constitutional extension of the 14th Amendment's citizenship provisions to the former Confederate states, though Louisiana's subsequent history demonstrated the limitations of Reconstruction's achievements",
            "His career as a Unionist Louisiana planter navigating Reconstruction politics contributed to the complex history of Southern Unionism — demonstrating both the existence and the political limitations of the minority of Southern planters who had opposed secession"
        ],
        "relationships": [
            {"entity": "Military Governor of Louisiana during Reconstruction (January–July 1868)", "relationship": "MILITARY_GOVERNOR", "note": "Served as military governor of Louisiana from January to July 1868 — appointed by General Winfield Scott Hancock to administer Louisiana during the critical readmission preparation phase"},
            {"entity": "General Winfield Scott Hancock / Fifth Military District (appointing authority)", "relationship": "APPOINTED_BY", "note": "Appointed by General Winfield Scott Hancock — commander of the Fifth Military District — as Louisiana's civilian military governor during the most contested phase of Reconstruction"},
            {"entity": "Louisiana Reconstruction / 14th Amendment ratification (1868)", "relationship": "GOVERNOR_DURING_READMISSION_PROCESS", "note": "Presided over Louisiana's preparation for readmission — including the state's ratification of the 14th Amendment and the 1868 elections for new civil government"},
            {"entity": "Louisiana Unionism / anti-secession planters (Civil War)", "relationship": "MEMBER_OF", "note": "A member of Louisiana's small Unionist planter minority — opposing secession despite his planter background — making him acceptable to Union military command as an administrative figure"},
            {"entity": "Congressional Reconstruction Acts (1867) / Fifth Military District", "relationship": "GOVERNED_UNDER_AUTHORITY_OF", "note": "His military governorship was created and authorized by the Congressional Reconstruction Acts (1867) that placed the former Confederate states under military district command"}
        ]
    }),

    # 8 — David Plant
    ("david-plant", {
        "summary": (
            "David Plant (1783–1851) was a Connecticut lawyer, "
            "judge, and politician who served as US Representative "
            "from Connecticut (1821–1823) — completing one "
            "congressional term during the Era of Good Feelings "
            "— after a legal career in Stratford that included "
            "service as a judge of the Fairfield County "
            "probate court. Born in Stratford, Connecticut, "
            "he attended Episcopal Academy in Cheshire and "
            "graduated from Yale College in 1804, then "
            "studied law at the Litchfield Law School — "
            "one of America's first and most influential "
            "legal academies — before being admitted to the bar.\n\n"
            "His congressional term (1821–1823) placed him "
            "in Washington during the final phase of the "
            "Era of Good Feelings and the beginning of "
            "the political realignment that would produce "
            "Jacksonian democracy. Connecticut's federal "
            "delegation in this period was composed primarily "
            "of Federalist-leaning lawyers who struggled "
            "to maintain relevance as the Democratic-Republican "
            "coalition fragmented and Federalism collapsed.\n\n"
            "He returned to Stratford after his congressional "
            "term and continued his legal and judicial career, "
            "serving as a Fairfield County judge. His career "
            "exemplifies the standard path of Connecticut's "
            "Yale-educated Litchfield-trained lawyers — "
            "the legal cohort that dominated the state's "
            "judicial and political institutions in the "
            "first four decades of the 19th century.\n\n"
            "The Litchfield Law School connection — where Plant "
            "trained alongside future politicians, lawyers, "
            "and judges from across the United States and "
            "the Caribbean — placed him within one of the "
            "most remarkable professional networks of the "
            "early American republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut US Representative (1821–1823); Yale 1804; Litchfield Law School graduate; Stratford lawyer and Fairfield County probate judge; his career exemplifies the Yale-Litchfield-trained Connecticut legal cohort that dominated the state's early 19th-century political and judicial institutions.",
            "significanceCategory": "local"
        },
        "causes": [
            "Connecticut's Yale-Litchfield legal education pipeline — which produced the lawyers who dominated the state's political and judicial institutions in the early 19th century — created the professional formation and network connections that supported Plant's career as a lawyer, judge, and congressman",
            "The Era of Good Feelings' political landscape — in which the collapse of Federalism created temporary openings for Federalist-leaning lawyers in Connecticut to win congressional seats before the full Jacksonian realignment arrived — created the political opportunity for Plant's single congressional term",
            "Stratford's position within Fairfield County's established legal community — one of Connecticut's most prosperous and professionally developed counties — provided the institutional base for Plant's legal practice and probate court service"
        ],
        "effects": [
            "His congressional term (1821–1823) contributed to Connecticut's federal representation during the Era of Good Feelings — providing one voice in the House during the transition period between the first and second American party systems",
            "His Fairfield County probate court service contributed to Connecticut's judicial administration — managing the estate proceedings and property transfers of one of the state's most prosperous counties",
            "His education at both Yale and Litchfield placed him within the professional networks of two of America's most influential educational institutions of the early republic — the Yale-Litchfield pipeline that supplied lawyers, judges, and politicians to Connecticut and beyond",
            "His career illustrated the institutional reproduction of Connecticut's early 19th-century legal establishment — demonstrating how Yale graduation, Litchfield law training, and Stratford practice combined to produce the standard career path of the state's governing professional class"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Connecticut (1821–1823)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from Connecticut (1821–1823) — one term during the Era of Good Feelings and the beginning of the Jacksonian political realignment"},
            {"entity": "Litchfield Law School (trained at, early 19th century)", "relationship": "TRAINED_AT", "note": "Studied law at the Litchfield Law School — one of America's first and most influential legal academies — placing him within the remarkable professional network of America's early trained lawyers"},
            {"entity": "Yale College (graduated 1804)", "relationship": "EDUCATED_AT", "note": "Graduated from Yale College in 1804 — the Yale-Litchfield pipeline that dominated Connecticut's early 19th-century political and judicial institutions"},
            {"entity": "Fairfield County probate court (judge)", "relationship": "JUDGE", "note": "Served as a judge of the Fairfield County probate court — contributing to Connecticut's judicial administration in one of the state's most prosperous counties"},
            {"entity": "Stratford, Connecticut legal community / Yale-Litchfield lawyer cohort", "relationship": "MEMBER_OF", "note": "Member of Stratford's legal community and the broader Yale-Litchfield cohort of Connecticut lawyers — the professional class that dominated the state's early 19th-century political and judicial institutions"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 44)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
