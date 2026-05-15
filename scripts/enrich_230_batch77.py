#!/usr/bin/env python3
"""
Batch 77 — 8 entities: Johan Michael Lund, William Seymour, Benjamin Tappan,
Isaac Halstead Williamson, John Nicholas, Ogden Hoffman, James Pleasants, Jean Barbier d'Aucour
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

    ("johan-michael-lund", {
        "summary": (
            "Johan Michael Lund (1777–1833) "
            "was a Norwegian jurist and "
            "politician who participated "
            "in Norway's independence "
            "movement of 1814 — serving "
            "as a member of the Eidsvoll "
            "Constitutional Assembly "
            "that drafted the Norwegian "
            "Constitution of May 17, "
            "1814. As one of the 112 "
            "delegates who gathered "
            "at Eidsvoll manor to draft "
            "Norway's founding document, "
            "Lund participated in creating "
            "one of the most liberal "
            "constitutions in 19th-century "
            "Europe — establishing a "
            "constitutional monarchy "
            "with a powerful Storting "
            "(parliament) that was "
            "remarkably democratic "
            "for its era.\n\n"
            "The 1814 constitutional "
            "moment was brief — "
            "Sweden's military pressure "
            "forced Norway into union "
            "with Sweden by November "
            "1814 — but the constitution "
            "survived and governed "
            "Norway through the "
            "union period until "
            "full independence in 1905.\n\n"
            "Lund's subsequent "
            "career as a jurist "
            "contributed to "
            "Norwegian legal "
            "development in "
            "the early national period.\n\n"
            "He was a founding figure "
            "of the Norwegian state."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Norwegian Eidsvoll Assembly delegate (1814); participated in drafting the Norwegian Constitution of May 17, 1814 — still celebrated as Norway's National Day; the constitution survived Swedish union and governed Norway until 1905 independence; jurist contributing to Norwegian legal development; founding figure of the Norwegian constitutional state.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Napoleonic Wars' disruption of Scandinavian politics — Denmark's cession of Norway to Sweden via the Treaty of Kiel (January 1814) created the brief independence window in which the Eidsvoll assembly was called",
            "Norwegian national consciousness — the educated elite's sense of Norwegian cultural distinctiveness from both Denmark and Sweden — created the political will to draft a liberal constitution rather than simply accepting Swedish terms",
            "The 1814 constitutional moment's urgency — the brief window between Denmark's cession and Sweden's military assertion — created the pressure under which the Eidsvoll delegates drafted Norway's constitution in just six weeks"
        ],
        "effects": [
            "His Eidsvoll participation contributed to drafting one of the most significant constitutional documents of the 19th century — a liberal constitution with a powerful parliament that influenced subsequent European constitutionalism",
            "The Norwegian Constitution of 1814 that he helped draft survived Swedish union and continued to govern Norway — testifying to its fundamental soundness and the assembly delegates' achievement",
            "His subsequent legal career contributed to Norwegian jurisprudence — the developing legal system of a country building its own national legal institutions after centuries of Danish and then Swedish domination",
            "His career contributed to Norway's founding generation — the administrators, lawyers, and politicians who built the institutional infrastructure of a new constitutional state"
        ],
        "relationships": [
            {"target": "eidsvoll-constitutional-assembly", "verb": "SERVES_IN", "note": "Delegate to 1814 constitutional assembly"},
            {"target": "norwegian-constitution-1814", "verb": "DRAFTS", "note": "Participant in May 17, 1814 constitution"},
            {"target": "norway", "verb": "HELPS_FOUND", "note": "Founding figure of Norwegian constitutional state"},
            {"target": "storting", "verb": "ESTABLISHES", "note": "Constitutional author of the Norwegian parliament"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_DURING", "note": "Constitutionalist during forced union with Sweden"}
        ]
    }),

    ("william-seymour", {
        "summary": (
            "William Seymour (1771–1848) "
            "was an American Democratic-Republican "
            "politician from Vermont who "
            "served in the U.S. House "
            "of Representatives (1821–1823) "
            "during the final years "
            "of the Era of Good Feelings "
            "— the brief period of "
            "American political consensus "
            "under President Monroe "
            "when the Federalist Party "
            "had dissolved and the "
            "Democratic-Republicans "
            "were the only national "
            "party. Vermont's political "
            "culture in this era "
            "was characterized by "
            "the gradual transition "
            "from Federalist to "
            "Democratic-Republican "
            "dominance, with strong "
            "Protestant moral reform "
            "and antislavery sentiment "
            "running through both "
            "parties.\n\n"
            "His House service "
            "coincided with the "
            "Missouri Compromise "
            "era — the settlement "
            "of 1820 that admitted "
            "Missouri as a slave "
            "state and Maine as "
            "a free state while "
            "prohibiting slavery "
            "north of the 36°30' "
            "parallel in the "
            "Louisiana Purchase territory.\n\n"
            "Vermont's antislavery "
            "tradition made its "
            "congressional delegation "
            "among the most hostile "
            "to the Missouri "
            "Compromise's slavery "
            "extension provisions.\n\n"
            "He was a Vermont "
            "lawyer and civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Vermont Democratic-Republican Congressman (1821–1823); served during the Missouri Compromise era and the final years of the Era of Good Feelings; part of Vermont's antislavery congressional tradition; brief national service during the transition from one-party consensus to Jacksonian political realignment.",
            "significanceCategory": "local"
        },
        "causes": [
            "Vermont's political transition from Federalism to Democratic-Republicanism — the shift in partisan alignment that characterized New England states as the Federalist Party collapsed — created the political context for Seymour's Democratic-Republican career",
            "The Missouri Compromise crisis — the national debate over slavery extension that briefly threatened the Union's cohesion — created the major political controversy of Seymour's congressional term",
            "Vermont's antislavery civic culture — the Protestant moral reform tradition that made Vermont one of the most antislavery states in the Union — informed Seymour's political perspective on the Missouri controversy"
        ],
        "effects": [
            "His House service contributed Vermont's perspective to the Missouri Compromise debates — adding the antislavery New England voice to the congressional controversy",
            "His brief term contributed to the transition period between the Era of Good Feelings and the Jacksonian realignment — the political moment when one-party consensus was breaking down",
            "His career contributed to Vermont's political tradition — the antislavery Democratic-Republican and then Whig and Republican alignment that made Vermont the most consistently principled antislavery state",
            "His death in 1848 placed him among the founders-era generation who lived through the Missouri crisis and the subsequent decades of slavery extension controversy"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1821–1823"},
            {"target": "missouri-compromise", "verb": "SERVES_DURING", "note": "Congressman during the Missouri Compromise controversy"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Congressman during Monroe's political consensus"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Vermont Democratic-Republican congressman"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Vermont Democratic-Republican politician"}
        ]
    }),

    ("benjamin-tappan", {
        "summary": (
            "Benjamin Tappan (1773–1857) "
            "was an American Democratic "
            "politician from Ohio who "
            "served as a U.S. Senator "
            "(1839–1845) and is best "
            "known for the extraordinary "
            "episode in which he leaked "
            "the secret text of the "
            "Texas annexation treaty "
            "(1844) to the press — "
            "a breach of Senate secrecy "
            "that caused a political "
            "scandal but also demonstrated "
            "his fierce opposition "
            "to the annexation of Texas "
            "as a slave state. He "
            "was the brother of the "
            "more famous abolitionists "
            "Lewis and Arthur Tappan "
            "— the New York merchants "
            "who financed the abolitionist "
            "movement.\n\n"
            "The Texas annexation "
            "treaty leak was one "
            "of the most dramatic "
            "Senate breaches in "
            "American history — "
            "Tappan leaked the "
            "secret treaty to "
            "the New York Evening "
            "Post as a deliberate "
            "act of political "
            "resistance to what "
            "he saw as a pro-slavery "
            "conspiracy.\n\n"
            "He was also a "
            "significant Ohio "
            "judge and natural "
            "history enthusiast "
            "who contributed "
            "paleontological specimens "
            "to the scientific literature.\n\n"
            "His family represented "
            "New England abolitionism's "
            "national reach."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ohio Democratic Senator (1839–1845); leaked the secret Texas annexation treaty to the press (1844) in an extraordinary act of political resistance to slavery extension; brother of abolitionists Lewis and Arthur Tappan; also an Ohio judge and natural history contributor; his treaty leak was one of the most dramatic Senate secrecy breaches in American history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Texas annexation's pro-slavery character — the political reality that Texas's annexation would add a massive new slave state to the Union — created the issue that drove Tappan to the extraordinary step of leaking the secret annexation treaty",
            "Tappan family abolitionism — his brothers Lewis and Arthur Tappan's role as the primary financiers of the American abolitionist movement, including the American Anti-Slavery Society — created the family background of fierce anti-slavery commitment",
            "Ohio's Free Soil political tradition — the state's large antislavery constituency that would produce the Giddings-Chase-Wade antislavery political tradition — created the political environment that supported Tappan's antislavery Senate stance"
        ],
        "effects": [
            "His Texas annexation treaty leak contributed to the public debate over annexation — releasing the secret treaty text allowed opponents to organize resistance and contributed to the treaty's defeat in the Senate",
            "His breach of Senate secrecy established a significant precedent — the political reality that senators with principled objections to secret proceedings might use press leaks as political weapons, a tactic with a long subsequent history",
            "His family's abolitionist network contributed to the broader antislavery movement — the Tappan brothers' financial and political connections linking Ohio political antislavery with New York merchant abolitionism",
            "His natural history contributions contributed to Ohio's scientific culture — the paleontological specimens and observations that contributed to the developing American scientific tradition"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Ohio Senator 1839–1845"},
            {"target": "texas-annexation-treaty", "verb": "LEAKS", "note": "Leaked secret treaty text to the New York Evening Post"},
            {"target": "lewis-tappan", "verb": "FAMILY_OF", "note": "Brother of abolitionist financier"},
            {"target": "arthur-tappan", "verb": "FAMILY_OF", "note": "Brother of abolitionist movement financier"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio antislavery Democratic senator"}
        ]
    }),

    ("isaac-halstead-williamson", {
        "summary": (
            "Isaac Halstead Williamson "
            "(1767–1844) was an American "
            "Democratic-Republican "
            "politician from New Jersey "
            "who served as Governor "
            "of New Jersey (1817–1829) "
            "— an extraordinary twelve-year "
            "gubernatorial tenure that "
            "made him one of the longest-serving "
            "governors in New Jersey "
            "history. His governorship "
            "spanned the transition "
            "from the Era of Good "
            "Feelings through the "
            "opening of the Jacksonian "
            "era — a period of rapid "
            "change in American "
            "political culture.\n\n"
            "As a twelve-year governor, "
            "Williamson presided over "
            "New Jersey through the "
            "Monroe administration's "
            "relative political "
            "consensus, the contested "
            "1824 election that "
            "shattered Democratic-Republican "
            "unity, and the opening "
            "of the Jacksonian "
            "democratic revolution.\n\n"
            "New Jersey's political "
            "significance was "
            "substantial — a "
            "competitive state "
            "between Philadelphia "
            "and New York whose "
            "gubernatorial politics "
            "reflected national trends.\n\n"
            "He was previously "
            "New Jersey's Attorney "
            "General and a "
            "prominent lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Jersey Governor (1817–1829) — twelve-year tenure making him one of the longest-serving in New Jersey history; spanned the Era of Good Feelings through the Jacksonian opening; also served as New Jersey Attorney General; presided over New Jersey's transition from Monroe-era consensus to Jacksonian democratic politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's Democratic-Republican political dominance — the party organization that controlled the state government and created the conditions for Williamson's repeated re-election to the governorship",
            "The Era of Good Feelings' political consensus — Monroe's one-party politics that reduced partisan competition and made long gubernatorial tenures more feasible",
            "New Jersey's commercial and geographic significance — the state's position between Philadelphia and New York, its manufacturing and agricultural economy, and its competitive political tradition — created the importance of the gubernatorial office that Williamson held for twelve years"
        ],
        "effects": [
            "His twelve-year governorship contributed to New Jersey's institutional continuity — a decade of consistent executive leadership during one of the most important transitions in American political history",
            "His tenure presided over New Jersey's transition from the Era of Good Feelings to the Jacksonian era — managing the state through the political revolution that democratized American politics",
            "His long governorship contributed to the development of New Jersey's state institutions — the executive practices and governmental traditions that would guide the state through the antebellum period",
            "His career as governor and attorney general contributed to New Jersey's legal and political tradition — the distinguished public service record of a major mid-Atlantic state"
        ],
        "relationships": [
            {"target": "new-jersey", "verb": "GOVERNS", "note": "Governor of New Jersey 1817–1829"},
            {"target": "new-jersey-attorney-general", "verb": "SERVES_AS", "note": "Previous Attorney General of New Jersey"},
            {"target": "era-of-good-feelings", "verb": "GOVERNS_DURING", "note": "Governor during Monroe's political consensus"},
            {"target": "andrew-jackson", "verb": "GOVERNS_DURING", "note": "Governor at the opening of the Jacksonian era"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New Jersey Democratic-Republican governor"}
        ]
    }),

    ("john-nicholas", {
        "summary": (
            "John Nicholas (1764–1819) "
            "was an American Democratic-Republican "
            "politician from Virginia "
            "who served in the U.S. "
            "House of Representatives "
            "(1793–1801) during the "
            "critical first decade "
            "of the new constitutional "
            "republic. A Virginia "
            "Democratic-Republican "
            "and a close ally of "
            "Thomas Jefferson, Nicholas "
            "was one of the leading "
            "Jeffersonian voices "
            "in the House during "
            "the most contentious "
            "years of American "
            "founding politics — "
            "the Jay Treaty controversy, "
            "the quasi-war with France, "
            "the Alien and Sedition "
            "Acts, and the election "
            "of 1800 that brought "
            "Jefferson to power.\n\n"
            "Nicholas was a member "
            "of the prominent "
            "Virginia Nicholas family "
            "— brothers Robert Carter "
            "Nicholas (constitutional "
            "figure) and John Nicholas "
            "were part of the Virginia "
            "gentry that dominated "
            "the early Republic.\n\n"
            "He later moved to "
            "New York, where he "
            "served as a federal "
            "judge — one of the "
            "relatively few Virginia "
            "Democratic-Republicans "
            "who relocated to "
            "the North.\n\n"
            "He was a significant "
            "Jeffersonian congressional voice."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Democratic-Republican Congressman (1793–1801); close Jefferson ally in the House during the Jay Treaty controversy, quasi-war, Alien and Sedition Acts, and the election of 1800; member of the prominent Virginia Nicholas family; later a New York federal judge; significant Jeffersonian voice during the founding republic's most contentious years.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's Jeffersonian political dominance — the state's overwhelming identification with Jefferson's Democratic-Republican party and its opposition to Hamilton's Federalist program — created the political context for Nicholas's eight-year House career",
            "The Alien and Sedition Acts controversy — the Federalist legislation targeting Democratic-Republican opposition that provoked Jefferson and Madison's Virginia and Kentucky Resolutions — created the defining political crisis of Nicholas's House tenure",
            "Jefferson's political organization — the emerging Democratic-Republican party structure that Jefferson was building against the Adams administration's Federalism — provided the political network within which Nicholas operated as a key House ally"
        ],
        "effects": [
            "His eight-year House tenure contributed Virginia's Jeffersonian votes to the founding era's defining battles — the Jay Treaty, the quasi-war, the Alien and Sedition Acts, and the election of 1800",
            "His alliance with Jefferson contributed to the Jeffersonian opposition's parliamentary effectiveness — helping coordinate the Democratic-Republican House minority that eventually became the majority",
            "His relocation to New York and subsequent federal judgeship contributed to the spread of Jeffersonian political and legal culture beyond Virginia — one of the ways Virginia's founding-era political tradition influenced other regions",
            "His career illustrated Virginia's political dominance in the early Republic — the state whose gentry produced so many of the founding generation's most significant political figures"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1793–1801"},
            {"target": "thomas-jefferson", "verb": "ALLIES_WITH", "note": "Key Jefferson ally in the House"},
            {"target": "alien-and-sedition-acts", "verb": "OPPOSES", "note": "Democratic-Republican opponent of Federalist legislation"},
            {"target": "election-of-1800", "verb": "SERVES_DURING", "note": "Congressman during the Jefferson-Adams contest"},
            {"target": "virginia", "verb": "REPRESENTS", "note": "Virginia gentry Democratic-Republican politician"}
        ]
    }),

    ("ogden-hoffman", {
        "summary": (
            "Ogden Hoffman (1793–1856) "
            "was an American Whig "
            "politician and lawyer "
            "from New York who served "
            "as a U.S. Representative "
            "(1837–1841) and as "
            "U.S. Attorney for the "
            "Southern District of "
            "New York (1829–1838) "
            "— one of the most "
            "important federal "
            "prosecutorial positions "
            "in the country, covering "
            "America's commercial "
            "capital. As U.S. Attorney "
            "in New York City during "
            "the Jacksonian era, "
            "Hoffman prosecuted "
            "significant commercial "
            "and federal cases in "
            "a city that was "
            "rapidly becoming the "
            "nation's dominant "
            "financial and commercial center.\n\n"
            "His House service "
            "(1837–1841) coincided "
            "with the Panic of 1837 "
            "and the Van Buren "
            "administration's "
            "political weakness "
            "— as a Whig he "
            "represented the "
            "opposition perspective "
            "on the Democratic "
            "economic policies.\n\n"
            "He was a prominent "
            "New York City "
            "lawyer whose courtroom "
            "skills made him "
            "one of the most "
            "distinguished trial "
            "advocates of his era.\n\n"
            "He was the son of "
            "the eminent jurist "
            "Josiah Ogden Hoffman."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "U.S. Attorney for the Southern District of New York (1829–1838) and Whig Congressman (1837–1841); prosecuted significant cases in America's commercial capital; served during the Panic of 1837 as Whig opponent of Democratic economic policies; son of eminent jurist Josiah Ogden Hoffman; prominent New York City trial advocate.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's commercial dominance — the city's emergence as America's leading financial and commercial center created the significance of the Southern District U.S. Attorney position that Hoffman held for nearly a decade",
            "The Jacksonian patronage system — the rotation-in-office principle that brought capable Whig lawyers like Hoffman into federal prosecutorial positions when the political winds shifted — created the institutional pathway for his U.S. Attorney appointment",
            "His family's legal standing — the son of eminent jurist Josiah Ogden Hoffman, with access to the top tier of New York legal circles — provided the professional connections and reputation that underpinned Hoffman's prosecutorial and political career"
        ],
        "effects": [
            "His U.S. Attorney tenure contributed to federal law enforcement in America's commercial capital — prosecuting the smuggling, fraud, and federal law violations that were inevitable in the nation's largest port and financial center",
            "His House service contributed New York's Whig perspective to the Van Buren era's economic debates — opposing the Independent Treasury and supporting commercial banking as the Whig alternative",
            "His trial advocacy contributed to New York's legal culture — the courtroom skills and legal arguments that shaped New York commercial and federal law in an era of rapid economic development",
            "His career illustrated the pattern of New York Whig legal culture — the high-society lawyers who combined federal service, congressional stints, and distinguished trial practice in the commercial bar"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1837–1841"},
            {"target": "us-attorneys-office-sdny", "verb": "LEADS", "note": "U.S. Attorney Southern District NY 1829–1838"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "New York Whig congressman"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Whig congressman opposing Democratic economic response"},
            {"target": "new-york-city", "verb": "SERVES", "note": "Federal prosecutor in America's commercial capital"}
        ]
    }),

    ("james-pleasants", {
        "summary": (
            "James Pleasants (1769–1836) "
            "was an American Democratic-Republican "
            "politician from Virginia "
            "who served in the U.S. "
            "House (1811–1819), U.S. "
            "Senate (1819–1822), and "
            "as Governor of Virginia "
            "(1822–1825) — a comprehensive "
            "career that moved through "
            "all three levels of federal "
            "and state service. "
            "His congressional career "
            "spanned the War of 1812, "
            "the Era of Good Feelings, "
            "and the opening of the "
            "Missouri Compromise crisis "
            "— some of the most "
            "consequential years "
            "of early American political history.\n\n"
            "As a Virginia governor "
            "during the Monroe "
            "administration, Pleasants "
            "presided over the "
            "state that was "
            "still the most "
            "politically powerful "
            "in the Union — "
            "the Mother of Presidents "
            "from which four "
            "of the first five "
            "presidents had come.\n\n"
            "Virginia's internal "
            "politics in this "
            "era was beginning "
            "to generate tensions "
            "between the Tidewater "
            "planter elite and "
            "the western Virginia "
            "farmers that would "
            "eventually produce "
            "the constitutional "
            "reform movement.\n\n"
            "He died in 1836 "
            "during the Jacksonian era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Democratic-Republican Congressman (1811–1819), Senator (1819–1822), and Governor (1822–1825); career spanning War of 1812, Era of Good Feelings, and Missouri Compromise opening; presided over Virginia during Monroe's presidency; comprehensive service through all three levels of Virginia's political system.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's political dominance in the early Republic — the state's extraordinary concentration of political talent and national leadership that produced the Virginia Dynasty of presidents — created the significance of Pleasants's comprehensive career",
            "The War of 1812 — the conflict that dominated Pleasants's early House career and tested the new republic's military and diplomatic capacity — created the major policy context for his congressional service",
            "Virginia's internal political tensions — the growing rift between Tidewater planters and western Virginia farmers that was beginning to challenge the established political order — created the governing challenge of Pleasants's gubernatorial term"
        ],
        "effects": [
            "His comprehensive career — House, Senate, and governorship — contributed Virginia's leadership to three different institutional arenas during the most important transitional years of early American politics",
            "His War of 1812 congressional service contributed Virginia's voice to the war debates — supporting the conflict that most Virginia Democratic-Republicans saw as a necessary defense of national honor and commerce",
            "His governorship contributed to Virginia's administration during Monroe's Era of Good Feelings — managing the politically dominant state when national consensus was high but internal tensions were developing",
            "His career illustrated the pattern of Virginia gentry political service — the comprehensive participation in federal and state offices that characterized the Virginia Dynasty era's political culture"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1811–1819"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Virginia Senator 1819–1822"},
            {"target": "virginia", "verb": "GOVERNS", "note": "Governor of Virginia 1822–1825"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Congressman supporting the war"},
            {"target": "james-monroe", "verb": "SERVES_DURING", "note": "Governor during Monroe's presidency"}
        ]
    }),

    ("jean-barbier-daucour", {
        "summary": (
            "Jean Barbier d'Aucour "
            "(1641–1694) was a French "
            "lawyer and writer of "
            "the classical era who "
            "is best known for his "
            "satirical work 'Sentiments "
            "de Cléante sur les "
            "entretiens d'Ariste et "
            "d'Eugène' (1671) — a "
            "sharp literary satire "
            "targeting the Jesuit "
            "Father Dominique Bouhours's "
            "celebrated literary "
            "dialogues 'Les entretiens "
            "d'Ariste et d'Eugène.' "
            "Barbier d'Aucour's "
            "attack contributed "
            "to one of the liveliest "
            "literary controversies "
            "of Louis XIV's France "
            "— the debates over "
            "French literary style, "
            "the proper use of "
            "the French language, "
            "and the competing "
            "claims of classical "
            "rules versus Jesuit "
            "refinement.\n\n"
            "He was also a "
            "lawyer at the "
            "Paris Parlement "
            "— the judicial "
            "institution that "
            "was simultaneously "
            "a court of law "
            "and a major "
            "political actor "
            "in Ancien Régime France.\n\n"
            "His Jansenist sympathies "
            "informed his anti-Jesuit "
            "satire — the "
            "Paris Parlement's "
            "legal elite was "
            "often aligned with "
            "Jansenist religious "
            "culture.\n\n"
            "He was a minor "
            "but real figure "
            "in French classical literature."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French lawyer and literary satirist (1641–1694); his 'Sentiments de Cléante' (1671) satirized Bouhours's Jesuit literary dialogues; contributed to Louis XIV-era literary controversies over French style and language; Paris Parlement lawyer with Jansenist sympathies; minor but real figure in French classical literary culture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Louis XIV literary culture — the king's patronage of letters and the intense debates over proper French literary style, the role of classical rules, and the emerging French Academy's authority — created the cultural environment for Barbier d'Aucour's satirical engagement",
            "The Jesuit-Jansenist conflict — the bitter theological and cultural struggle between the Jesuit order's accommodationist Catholicism and the Jansenist emphasis on Augustinian rigorism — created the religious subtext for Barbier d'Aucour's attack on Bouhours's Jesuit dialogues",
            "Bouhours's literary provocation — Father Bouhours's witty, sophisticated literary dialogues that presented Jesuit aesthetic refinement as the model for proper French culture — created the specific literary target that Barbier d'Aucour's satire attacked"
        ],
        "effects": [
            "His literary satire contributed to the literary controversies of Louis XIV's France — the debates over French prose style and the competing claims of classical authority and Jesuit sophistication",
            "His attack on Bouhours contributed to the Jansenist intellectual tradition's engagement with literary culture — the Jansenist lawyers of the Paris Parlement frequently used literary and rhetorical weapons in their conflict with Jesuit influence",
            "His career as a Paris Parlement lawyer contributed to the legal culture of Ancien Régime France — the influential institution that combined judicial, administrative, and political functions",
            "His literary work illustrated the connection between legal culture and literary production in Ancien Régime France — the lawyers of the Paris Parlement were among the most educated and culturally active members of French society"
        ],
        "relationships": [
            {"target": "paris-parlement", "verb": "SERVES_IN", "note": "Lawyer at the Paris judicial-political institution"},
            {"target": "dominique-bouhours", "verb": "SATIRIZES", "note": "Attacked Bouhours's Jesuit literary dialogues"},
            {"target": "jesuit-order", "verb": "OPPOSES", "note": "Jansenist opponent of Jesuit cultural influence"},
            {"target": "jansenism", "verb": "ASSOCIATED_WITH", "note": "Jansenist sympathies informing anti-Jesuit satire"},
            {"target": "french-classical-literature", "verb": "CONTRIBUTES_TO", "note": "Contributor to Louis XIV-era literary controversies"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 77 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
