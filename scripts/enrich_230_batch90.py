#!/usr/bin/env python3
"""
Batch 90 — 8 entities: Marc-Guillaume-Alexis Vadier, William Sharpe,
Obadiah German, Théodore Vernier, William Paulding Jr, Jacob Hveding,
Aimé Paris, James Woodson Bates
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP: {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    dj = entity.get("detailsJson", "{}")
    det = json.loads(dj) if isinstance(dj, str) else dj
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} e={len(det.get('effects',[]))}")


ENTITIES = [

    ("marc-guillaume-alexis-vadier", {
        "summary": (
            "Marc-Guillaume Alexis Vadier (1736–1828) was a French Revolutionary "
            "politician who served as President of the Committee of General Security — "
            "one of the two great governing committees of the Terror — and was one of "
            "the most feared figures of Jacobin repression. The Committee of General "
            "Security was responsible for political policing, revolutionary tribunals, "
            "and the surveillance apparatus that drove the Terror. Vadier was its "
            "dominant personality — nicknamed 'the Inquisitor' for his relentless "
            "pursuit of enemies real and imagined.\n\n"
            "He survived the Thermidorean Reaction that killed Robespierre in 1794, "
            "and was subsequently accused of complicity in the Terror. He escaped "
            "execution and deportation through various political maneuvers, living to "
            "the remarkable age of ninety-two.\n\n"
            "His long survival despite his Terror-era role made him one of the most "
            "remarkable figures of French Revolutionary survivor politics.\n\n"
            "He was an Ariège lawyer who rose to national prominence through radical Jacobinism."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "President of the Committee of General Security during the Terror; one of the most feared Jacobin figures; 'the Inquisitor' — dominated political policing and the surveillance apparatus; survived the Thermidorean Reaction and lived to ninety-two; Ariège lawyer who rose through radical Jacobinism.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radical phase — the Jacobin seizure of power, the war emergency, and the mass mobilization that justified the Terror — created the institutional and ideological context for Vadier's Committee role",
            "The Committee of General Security's security mandate — the committee's responsibility for political policing, denunciations, and revolutionary tribunals — created the instrument through which Vadier exercised his feared power",
            "The provincial Jacobin networks — the radical clubs and local committees that provided the grass-roots surveillance apparatus the Committee depended on — created the infrastructure that Vadier commanded"
        ],
        "effects": [
            "His Committee leadership contributed to the institutional machinery of the Terror — the political policing apparatus that sent thousands to the guillotine",
            "His survival of the Thermidorean Reaction contributed to the post-Terror political landscape — demonstrating that some Terror architects could escape punishment through political maneuvering",
            "His long life contributed to the historical memory of the Terror — as a living witness to Revolutionary repression who survived into the Restoration era",
            "His career contributed to the institutional model of political policing — the Committee of General Security becoming a reference point for later authoritarian surveillance systems"
        ],
        "relationships": [
            {"target": "committee-of-general-security", "verb": "LEADS", "note": "President of the Committee during the Terror"},
            {"target": "reign-of-terror", "verb": "ADMINISTERS", "note": "One of the most feared figures of Jacobin repression"},
            {"target": "maximilien-robespierre", "verb": "SERVES_WITH", "note": "Fellow Jacobin during the Terror"},
            {"target": "thermidorean-reaction", "verb": "SURVIVES", "note": "Escaped execution after Robespierre's fall"},
            {"target": "jacobin-club", "verb": "MEMBER_OF", "note": "Radical Jacobin politician from Ariège"}
        ]
    }),

    ("william-sharpe", {
        "summary": (
            "William Sharpe (1742–1818) was an American patriot politician from North "
            "Carolina who served in the Continental Congress (1779–1782) during the "
            "most critical years of the Revolutionary War in the South. North Carolina's "
            "role in the southern theater was crucial — the state was the site of "
            "major battles including Guilford Court House (1781), where Nathanael Greene's "
            "army wore down Cornwallis's forces before the British general's fateful "
            "march to Virginia and Yorktown. Sharpe served in Congress during the "
            "darkest southern period — after the fall of Charleston and Camden — "
            "through to the final victory.\n\n"
            "He was a Rowan County North Carolina lawyer who represented the Piedmont "
            "Presbyterian Scots-Irish community that formed North Carolina's backbone "
            "of Revolutionary resistance.\n\n"
            "The Continental Congress years were the republic's most desperate — "
            "the challenge of financing and supplying Washington's army while managing "
            "the British southern campaign.\n\n"
            "He contributed to North Carolina's Revolutionary political legacy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "North Carolina delegate to the Continental Congress (1779–1782) during the critical southern theater of the Revolution; served during the fall of Charleston, Battle of Guilford Court House, and Yorktown victory; Rowan County Piedmont lawyer representing the Scots-Irish Revolutionary community.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's Revolutionary mobilization — the state's substantial Piedmont and backcountry Presbyterian community whose resistance to British authority provided crucial military and political support — created the basis for Sharpe's Continental Congress service",
            "The southern theater's critical phase — the British southern campaign that culminated in the fall of Charleston, the battles of Camden and Guilford Court House, and Cornwallis's retreat to Yorktown — created the war emergency during Sharpe's congressional years",
            "The Continental Congress's governance challenges — the difficulty of financing the war, managing interstate rivalries, and coordinating with Washington's army — created the institutional demands that required North Carolina's full congressional participation"
        ],
        "effects": [
            "His Continental Congress service contributed North Carolina's voice to the Revolutionary government during the war's most critical phase",
            "His representation of the Rowan County Piedmont contributed to the political documentation of North Carolina's Scots-Irish Revolutionary community",
            "His congressional years contributed to the governance legacy that North Carolina brought to the Constitutional ratification debate",
            "His career contributed to North Carolina's tradition of lawyer-politicians who bridged local community leadership and national governance"
        ],
        "relationships": [
            {"target": "continental-congress", "verb": "SERVES_IN", "note": "North Carolina delegate 1779–1782"},
            {"target": "american-revolutionary-war", "verb": "SERVES_DURING", "note": "Congressman during the critical southern theater"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "Rowan County North Carolina lawyer-politician"},
            {"target": "battle-of-guilford-court-house", "verb": "SERVES_DURING", "note": "Congressman during the decisive southern battle"},
            {"target": "nathanael-greene", "verb": "SUPPORTS", "note": "Continental Congress supporter of Greene's southern campaign"}
        ]
    }),

    ("obadiah-german", {
        "summary": (
            "Obadiah German (1766–1842) was an American Democratic-Republican "
            "politician from New York who served as U.S. Senator (1809–1815). "
            "His Senate years covered the most dramatic period in early American "
            "foreign policy — the collapse of the Embargo, the Non-Intercourse Act, "
            "Macon's Bill No. 2, the drift toward war, and the War of 1812 itself. "
            "New York in this era was the most populous state in the Union and its "
            "political dynamics — the Clinton-Tammany rivalry, the Federalist-Republican "
            "contest — made it the key prize in national electoral politics.\n\n"
            "German supported the Republican war policy — voting for the War of 1812 "
            "declaration in one of the most consequential Senate votes of the era. "
            "His Senate term ended just as the war was concluding.\n\n"
            "He was a Norwich New York farmer-politician representing the rural "
            "Chenango County Republican constituency.\n\n"
            "His Senate career reflected New York's Republican dominance during the "
            "Madison years."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Democratic-Republican Senator (1809–1815); served during the drift toward war and the War of 1812; voted for war declaration; New York's Clinton-Tammany factional politics; Norwich New York farmer-politician representing rural Chenango County.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Democratic-Republican dominance — the state's shift from Federalist to Republican politics under DeWitt Clinton and the Tammany organization — created the political environment for German's Senate election",
            "The War of 1812's political origins — the maritime grievances, frontier pressures, and nationalist sentiment that drove the Republican majority toward war — created the policy context of German's Senate years",
            "New York's rural Republican base — the farming communities of central and western New York whose Jeffersonian agrarianism aligned with Republican anti-commercial foreign policy — provided German's political foundation"
        ],
        "effects": [
            "His war vote contributed New York's Republican support to the War of 1812 declaration — one of the most consequential Senate votes",
            "His Senate service contributed to New York's Democratic-Republican organization during the transition from Federalist competition to Republican dominance",
            "His career contributed to the documentation of New York's rural Republican constituency — the farming communities that balanced New York City's commercial Federalism",
            "His Senate term contributed to the governance record of the Madison years — the war congress that managed American foreign policy's most dangerous transformation"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New York Senator 1809–1815"},
            {"target": "war-of-1812", "verb": "VOTES_FOR", "note": "Supported the war declaration"},
            {"target": "james-madison", "verb": "SERVES_UNDER", "note": "Republican senator during the Madison administration"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "Chenango County New York farmer-politician"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New York Republican senator"}
        ]
    }),

    ("théodore-vernier", {
        "summary": (
            "Théodore Vernier (1731–1818) was a French jurist and politician who "
            "served in the Estates-General and National Constituent Assembly (1789–1791) "
            "and was one of the lawyers who helped draft the early Revolutionary "
            "legal reforms. A Jura magistrate with expertise in French customary law, "
            "Vernier was among the legal professionals who dominated the Constituent "
            "Assembly's law reform committees. The Assembly's legal revolution — "
            "abolishing feudalism, codifying civil law, reforming the judiciary — "
            "was the greatest transformation of French law since Justinian.\n\n"
            "He contributed to the foundational legal work that preceded the Napoleonic "
            "Code — the Revolutionary dismantling of the Old Regime's complex legal "
            "pluralism and its replacement with uniform national law.\n\n"
            "He was a Lons-le-Saunier magistrate representing the Jura in the "
            "Estates-General as a Third Estate delegate.\n\n"
            "He contributed to the legal revolution of 1789–1791."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Jura magistrate and National Constituent Assembly delegate (1789–1791); contributed to Revolutionary legal reforms that abolished feudalism and reformed the judiciary; Lons-le-Saunier lawyer who helped lay groundwork for the Napoleonic Code's legal uniformity; Third Estate delegate.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Estates-General's convocation in 1789 — Louis XVI's desperate response to France's fiscal crisis — created the political opening that transformed into the Revolutionary legal overthrow of the Old Regime",
            "The legal profession's role in the Revolution — the trained lawyers and magistrates who dominated the Third Estate and provided the technical expertise for the Assembly's law reform agenda — created Vernier's institutional role",
            "The Old Regime's legal complexity — France's patchwork of customary laws, royal ordinances, and ecclesiastical law that varied by province — created both the problem and the demand for the uniform national law the Assembly created"
        ],
        "effects": [
            "His Assembly legal work contributed to the Revolutionary abolition of feudal law — the dismantling of the Old Regime's legal foundations",
            "His legal reform contributions contributed to the groundwork for the Napoleonic Code — the uniform national civil law that France eventually adopted",
            "His Jura representation contributed to the documentation of provincial legal traditions in the Revolutionary debates",
            "His career contributed to the transformation of French law from regional customary pluralism to national uniformity — one of the most significant legal changes in European history"
        ],
        "relationships": [
            {"target": "estates-general-1789", "verb": "SERVES_IN", "note": "Third Estate Jura delegate"},
            {"target": "national-constituent-assembly", "verb": "SERVES_IN", "note": "Assembly member contributing to legal reforms"},
            {"target": "french-revolution", "verb": "PARTICIPATES_IN", "note": "Revolutionary legal reformer"},
            {"target": "napoleonic-code", "verb": "PRECEDES", "note": "Revolutionary legal work that laid groundwork for the Code"},
            {"target": "abolition-of-feudalism", "verb": "CONTRIBUTES_TO", "note": "Assembly lawyer supporting feudal abolition"}
        ]
    }),

    ("william-paulding-jr", {
        "summary": (
            "William Paulding Jr. (1770–1854) was an American Democratic politician "
            "from New York who served as Mayor of New York City (1825–1826 and 1827–1829) "
            "and as U.S. Representative (1811–1813). His mayoralty spanned the "
            "transformative years when New York City was emerging as the nation's "
            "commercial capital — the completion of the Erie Canal (1825) and the "
            "explosive growth driven by the opening of the interior markets creating "
            "the conditions for New York's permanent commercial dominance. As mayor "
            "he managed the growing demands of a rapidly urbanizing city.\n\n"
            "His congressional career during the War of 1812 placed him among the "
            "Republican war supporters — the New York delegation that backed Madison's "
            "war policy.\n\n"
            "His brother James Kirke Paulding was a famous American author and later "
            "Secretary of the Navy — making the Paulding family a notable New York "
            "political-literary dynasty.\n\n"
            "He was a Tarrytown New York lawyer-politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York City Mayor (1825–1826, 1827–1829) during Erie Canal completion and urban growth; U.S. Congressman (1811–1813) during War of 1812; brother of author/Navy Secretary James Kirke Paulding; Tarrytown New York politician managing the city's emergence as America's commercial capital.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's commercial rise — the city's explosive growth driven by the Erie Canal, Atlantic trade, and the opening of western markets — created the urban governance challenges that Paulding's mayoralty managed",
            "The Erie Canal's completion (1825) — the infrastructure project that made New York City the gateway to the American interior — created the transformative moment in New York's commercial history that coincided with Paulding's mayoralty",
            "New York's Democratic political machine — the Tammany Hall organization and its rivalry with the Clinton Whig faction — created the partisan environment of Paulding's political career"
        ],
        "effects": [
            "His mayoralty contributed to New York City's governance during the Erie Canal boom — managing the growth pressures of America's most rapidly expanding city",
            "His congressional War of 1812 service contributed to New York's Republican support for the war declaration",
            "His family connection to James Kirke Paulding contributed to the documentation of New York's political-literary elite — the overlapping worlds of politics and letters in the early republic",
            "His career contributed to the institutional development of New York City's mayor's office — the transformation from colonial appointment to elected democratic governance"
        ],
        "relationships": [
            {"target": "new-york-city", "verb": "GOVERNS", "note": "Mayor of New York City 1825–1826 and 1827–1829"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1811–1813"},
            {"target": "erie-canal", "verb": "GOVERNS_DURING_COMPLETION_OF", "note": "Mayor when Erie Canal opened 1825"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Republican congressman during the War of 1812"},
            {"target": "james-kirke-paulding", "verb": "SIBLING_OF", "note": "Brother of the American author and Navy Secretary"}
        ]
    }),

    ("jacob-hveding", {
        "summary": (
            "Jacob Hveding (1827–1906) was a Norwegian lawyer and politician who "
            "served in the Storting and contributed to Norwegian legal and political "
            "life during the critical decades of Norwegian constitutional development "
            "and the growing conflict with Sweden over Norwegian autonomy. Norway's "
            "constitutional order — the 1814 Eidsvoll Constitution, one of the most "
            "liberal documents of its era — provided the framework within which "
            "Norwegian politicians like Hveding worked to expand parliamentary "
            "governance and reduce Swedish royal prerogative. The 1880s–1890s saw "
            "the decisive struggle between the Storting's parliamentary majority and "
            "the Swedish-Norwegian king's ministers — a conflict resolved in 1884 "
            "when parliamentary government was established.\n\n"
            "Norwegian legal culture in this era was deeply influenced by Danish "
            "legal traditions but was developing its own distinctive character "
            "through codification and constitutional interpretation.\n\n"
            "He was a Nordland region lawyer representing Norway's northern coastal communities.\n\n"
            "He contributed to Norwegian parliamentary governance during its formative decades."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian Storting member and lawyer during Norway's constitutional development; served during the 1880s struggle for parliamentary government; Nordland region representative; Norwegian legal development under the 1814 Eidsvoll Constitution; parliamentary governance established 1884.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Norway's 1814 Eidsvoll Constitution — one of Europe's most liberal constitutional documents — created the parliamentary framework within which Hveding and other Storting members worked to expand Norwegian self-governance",
            "The Swedish-Norwegian union's constitutional tension — the conflict between Norwegian parliamentary majority and Swedish royal prerogative — created the political struggle that defined Norwegian politics in Hveding's years",
            "Norway's legal development — the gradual creation of a distinctive Norwegian legal culture separate from Danish traditions — created the professional context for Norwegian lawyers in Storting service"
        ],
        "effects": [
            "His Storting service contributed to Norwegian parliamentary development — the gradual expansion of legislative power over royal prerogative",
            "His Nordland representation contributed to the political documentation of Norway's northern coastal communities — the fishing and maritime economy that was central to Norwegian identity",
            "His legal career contributed to Norwegian law's development during the critical decades of constitutional interpretation",
            "His parliamentary career contributed to the institutional framework that made the 1884 parliamentary government establishment possible"
        ],
        "relationships": [
            {"target": "storting", "verb": "SERVES_IN", "note": "Norwegian parliament member"},
            {"target": "norway", "verb": "REPRESENTS", "note": "Nordland region Norwegian lawyer-politician"},
            {"target": "eidsvoll-constitution", "verb": "UPHOLDS", "note": "Works within the 1814 constitutional framework"},
            {"target": "parliamentary-government-norway-1884", "verb": "CONTRIBUTES_TO", "note": "Storting member during the constitutional struggle"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_DURING", "note": "Norwegian parliamentarian during union constitutional tensions"}
        ]
    }),

    ("aimé-paris", {
        "summary": (
            "Aimé Paris (1798–1866) was a French music theorist and pedagogue who "
            "developed the Galin-Paris-Chevé method — a revolutionary approach to "
            "musical notation and education that used numbers instead of conventional "
            "musical notation to make music accessible to non-musicians. The "
            "Galin-Paris-Chevé system — named for Pierre Galin who originated it, "
            "Paris who developed it, and Nanine Chevé who popularized it — became "
            "the foundation for the modern tonic sol-fa system and influenced "
            "music education globally.\n\n"
            "The numeric notation system allowed ordinary workers and children to "
            "learn to sing and read music without years of specialized training — "
            "democratizing musical literacy in a way that aligned with the "
            "progressive educational movements of 19th-century France.\n\n"
            "The system influenced John Curwen's English tonic sol-fa (1840s) "
            "and ultimately the Kodály method — making Paris a key figure in "
            "the global spread of music education.\n\n"
            "He was a Paris music educator whose method changed how millions learned music."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French music educator who developed the Galin-Paris-Chevé numeric notation system; foundation for tonic sol-fa and the Kodály method; democratized musical literacy for workers and children; influenced John Curwen's English tonic sol-fa; Paris educator whose method changed how millions globally learned music.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Pierre Galin's original numeric notation concept — the idea of replacing conventional musical notation with numbers to simplify music reading — created the intellectual foundation that Paris developed into a complete pedagogical system",
            "The 19th-century progressive education movement — the Pestalozzian and Lancastrian approaches to popular education that aimed to bring learning to the working classes — created the demand for accessible music education that Galin-Paris-Chevé addressed",
            "The French choral movement — the effort to improve congregational and choral singing among ordinary people — created the practical application that drove the adoption of accessible notation systems"
        ],
        "effects": [
            "The Galin-Paris-Chevé system contributed to the democratization of musical literacy — making it possible for ordinary workers and children to read and sing music without specialized training",
            "His pedagogical system contributed to John Curwen's English tonic sol-fa — the British adaptation that spread music education across the English-speaking world",
            "His work contributed to the Kodály method — the 20th-century Hungarian music education system that drew on the accessible notation tradition",
            "The Galin-Paris-Chevé system contributed to the global spread of choral singing and community music-making in the 19th and 20th centuries"
        ],
        "relationships": [
            {"target": "galin-paris-cheve-method", "verb": "DEVELOPS", "note": "Co-developer of the numeric music notation system"},
            {"target": "pierre-galin", "verb": "EXTENDS_WORK_OF", "note": "Developed Galin's original numeric notation concept"},
            {"target": "tonic-sol-fa", "verb": "PRECEDES", "note": "System influenced Curwen's tonic sol-fa method"},
            {"target": "music-education", "verb": "TRANSFORMS", "note": "Democratized musical literacy for the working classes"},
            {"target": "kodaly-method", "verb": "INFLUENCES", "note": "Galin-Paris-Chevé tradition influenced the Kodály approach"}
        ]
    }),

    ("james-woodson-bates", {
        "summary": (
            "James Woodson Bates (1788–1846) was an American Democratic-Republican "
            "politician from Arkansas Territory who served as the territory's first "
            "Delegate to Congress (1819–1821). Arkansas Territory was created in 1819 "
            "from the southern portion of Missouri Territory — the sectional division "
            "that anticipated the Missouri Compromise crisis of 1820. Bates thus "
            "represented a new frontier territory at the exact moment that the question "
            "of whether territories would be slave or free became the defining "
            "constitutional crisis of the era.\n\n"
            "As the first delegate from Arkansas Territory, Bates established the "
            "initial congressional presence of what would become a major southern "
            "slave state in 1836. His service coincided with the Missouri Compromise "
            "debates — the foundational sectional settlement that Arkansas's future "
            "statehood would eventually help upset.\n\n"
            "He was a lawyer who helped organize Arkansas Territory's early government.\n\n"
            "He was Arkansas's founding congressional voice."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Arkansas Territory's first Delegate to Congress (1819–1821); served during Missouri Compromise crisis; established Arkansas's initial congressional presence; Arkansas Territory created from Missouri Territory in 1819; lawyer who helped organize the new territory's government.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Arkansas Territory's creation in 1819 — the separation from Missouri Territory that created a new territorial unit requiring congressional representation — created Bates's opportunity as the first delegate",
            "The Missouri Compromise crisis of 1820 — the national debate over slavery's extension into new territories that Arkansas Territory was embedded in — created the sectional context of Bates's congressional service",
            "The frontier settlement pressure — the rapid migration of settlers into the Arkansas and Red River valleys that required territorial organization and federal governance — created the urgent need for congressional representation"
        ],
        "effects": [
            "His first delegate service established Arkansas Territory's congressional presence — the foundational representation of what would become a major southern state",
            "His service during the Missouri Compromise contributed Arkansas Territory's southern perspective to the sectional crisis",
            "His territorial organizational work contributed to Arkansas's governmental infrastructure — the early legal and administrative framework",
            "His career contributed to the historical documentation of Arkansas's founding — the transition from wilderness to organized territory to eventual statehood in 1836"
        ],
        "relationships": [
            {"target": "arkansas-territory", "verb": "REPRESENTS", "note": "First Delegate to Congress from Arkansas Territory 1819–1821"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Territorial delegate"},
            {"target": "missouri-compromise", "verb": "SERVES_DURING", "note": "Delegate during the foundational sectional crisis"},
            {"target": "arkansas", "verb": "FOUNDS_GOVERNANCE_OF", "note": "Helped organize Arkansas Territory's early government"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democratic-Republican"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 90 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
