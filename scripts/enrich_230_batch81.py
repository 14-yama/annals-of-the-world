#!/usr/bin/env python3
"""
Batch 81 — 8 entities: Thomas Burr Osborne, Freeman Walker, James A. Bayard Jr.,
John Church Hamilton, Pierre-Antoine Berryer, John Sloss Hobart, Josef Franz Karl Amrhyn,
Braulio Carrillo Colina
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

    ("thomas-burr-osborne", {
        "summary": (
            "Thomas Burr Osborne (1798–1869) "
            "was an American Whig "
            "politician from Connecticut "
            "who served in the U.S. "
            "House of Representatives "
            "(1839–1843) during the "
            "Harrison-Tyler era. "
            "A Connecticut Whig, "
            "Osborne served during "
            "the most politically "
            "chaotic Whig administration "
            "in American history — "
            "Harrison's death after "
            "one month, Tyler's "
            "expulsion from the "
            "Whig Party, and the "
            "complete collapse "
            "of the Whig legislative "
            "program created "
            "a two-year period "
            "of political crisis. "
            "Connecticut in this "
            "era was a competitive "
            "state where Whigs "
            "and Democrats genuinely "
            "contested elections "
            "— unlike the solid "
            "regions of both North "
            "and South.\n\n"
            "His House service "
            "placed him in the "
            "chamber during the "
            "Bank of the United "
            "States rechartering "
            "controversy — "
            "the issue that split "
            "Tyler from the Whigs "
            "and caused the "
            "historic cabinet purge.\n\n"
            "Connecticut's commercial "
            "and manufacturing "
            "economy made its "
            "delegation generally "
            "supportive of "
            "Whig economic policies.\n\n"
            "He was a New Haven "
            "lawyer and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Connecticut Whig Congressman (1839–1843); served during the Harrison-Tyler crisis; witnessed Tyler's expulsion from the Whig Party and the collapse of the Whig legislative program; Connecticut's competitive political environment; New Haven lawyer serving during a defining constitutional and political crisis.",
            "significanceCategory": "local"
        },
        "causes": [
            "The 1838 Whig electoral success — the Whig wave that swept Whig candidates across the Northeast including Connecticut — created Osborne's political opportunity",
            "Harrison's death and Tyler's Whig break — the extraordinary sequence of presidential death and the successor's party expulsion — created the chaotic political environment of Osborne's entire House term",
            "Connecticut's manufacturing and commercial economy — the state's Whig-leaning business interests who supported the American System and a national bank — created the political constituency that aligned with Osborne's Whig affiliation"
        ],
        "effects": [
            "His House service contributed Connecticut's Whig votes during the Tyler administration's chaos — participating in the attempt to override Tyler's vetoes and restore the Whig program",
            "His congressional term witnessed the Bank rechartering controversy — one of the most consequential executive-legislative confrontations in American history",
            "His career contributed to Connecticut's Whig political tradition — the manufacturing-state Whiggery that would eventually flow into the Republican Party",
            "His term illustrated the limits of partisan electoral success — the Whigs' 1840 landslide producing a two-year administrative disaster when the president died and his successor rejected the party program"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1839–1843"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Connecticut Whig congressman"},
            {"target": "john-tyler", "verb": "SERVES_DURING", "note": "Congressman during Tyler's break with the Whigs"},
            {"target": "bank-of-the-united-states", "verb": "DEBATES", "note": "House member during the bank rechartering controversy"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "New Haven Connecticut Whig congressman"}
        ]
    }),

    ("freeman-walker", {
        "summary": (
            "Freeman Walker (1780–1827) "
            "was an American Democratic-Republican "
            "politician from Georgia "
            "who served in the U.S. "
            "Senate (1819–1821) — "
            "serving during the "
            "Missouri Compromise "
            "crisis before resigning "
            "due to ill health. "
            "His Senate service "
            "coincided with the "
            "most divisive national "
            "debate since the "
            "Constitution's ratification "
            "— the question of "
            "whether Missouri "
            "would be admitted "
            "as a slave state "
            "and whether Congress "
            "had authority to "
            "restrict slavery's "
            "expansion in the "
            "western territories. "
            "As a Georgia senator, "
            "Walker represented "
            "a deep slave state "
            "whose political interests "
            "were closely aligned "
            "with the pro-slavery "
            "Southern position "
            "in the Missouri debates.\n\n"
            "His resignation from "
            "the Senate — attributed "
            "to poor health — "
            "shortened what "
            "might have been "
            "a longer career "
            "during a consequential period.\n\n"
            "He was previously "
            "the Mayor of Augusta, "
            "Georgia — one of "
            "the state's most "
            "important commercial cities.\n\n"
            "He died in 1827 "
            "during the period "
            "of the Jacksonian revolution."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Georgia Democratic-Republican Senator (1819–1821); served during the Missouri Compromise crisis representing Georgia's pro-slavery position; resigned due to ill health; previously Mayor of Augusta; career cut short before the Jacksonian era he would have helped shape.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's slaveholder political interests — the state's plantation economy and its deep commitment to the constitutional protection of slavery — created the political perspective from which Walker represented Georgia in the Missouri Compromise debates",
            "The Missouri Compromise crisis — the national crisis over slavery extension that nearly destroyed the Union in 1819–1821 — created the defining political controversy of Walker's brief Senate career",
            "Walker's Augusta civic career — his service as Augusta's mayor and his standing in Georgia's commercial community — provided the political base for his Senate appointment"
        ],
        "effects": [
            "His Senate service contributed Georgia's pro-slavery vote to the Missouri Compromise debates — adding one more Southern voice to the defense of slavery extension",
            "His resignation due to ill health opened his Senate seat during the critical Era of Good Feelings — the political transition period when the Missouri Compromise was reshaping American politics",
            "His Augusta mayoral career contributed to the commercial development of one of Georgia's most important cities — the civic leadership that preceded his Senate service",
            "His early death in 1827 prevented him from participating in the Jacksonian revolution that reshaped Georgia politics"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Georgia Senator 1819–1821"},
            {"target": "missouri-compromise", "verb": "VOTES_DURING", "note": "Senator during the Missouri crisis"},
            {"target": "georgia", "verb": "REPRESENTS", "note": "Georgia Democratic-Republican senator"},
            {"target": "augusta-georgia", "verb": "SERVES_AS_MAYOR_OF", "note": "Mayor of Augusta before Senate service"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Georgia Democratic-Republican senator"}
        ]
    }),

    ("james-a-bayard-jr", {
        "summary": (
            "James Asheton Bayard Jr. "
            "(1799–1880) was an American "
            "Democratic politician "
            "from Delaware who "
            "served in the U.S. "
            "Senate (1851–1864 "
            "and 1867–1869) — one "
            "of the most dramatic "
            "Senate careers of "
            "the Civil War era. "
            "A Delaware Democrat "
            "and the son of James A. "
            "Bayard Sr. (himself a "
            "senator), the younger "
            "Bayard was one of "
            "the most prominent "
            "Peace Democrats (Copperheads) "
            "in the Senate — "
            "opposing the Civil War, "
            "criticizing Lincoln's "
            "suspension of habeas corpus, "
            "and refusing to vote "
            "for war measures. "
            "He resigned from the "
            "Senate in January 1864 "
            "rather than take "
            "a loyalty oath.\n\n"
            "His resignation over "
            "the loyalty oath "
            "was one of the "
            "most dramatic acts "
            "of principled opposition "
            "to wartime loyalty "
            "requirements — "
            "Bayard refusing to "
            "swear that he had "
            "never given 'aid "
            "or comfort' to enemies "
            "of the United States.\n\n"
            "He returned to the "
            "Senate in 1867 "
            "after the war.\n\n"
            "He was the father "
            "of Thomas F. Bayard, "
            "Secretary of State."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Delaware Democratic Senator (1851–1864 and 1867–1869); leading Peace Democrat (Copperhead) who opposed the Civil War and Lincoln's suspension of habeas corpus; resigned from the Senate rather than take the loyalty oath (1864) — one of the most dramatic acts of principled wartime opposition; son of Senator James A. Bayard Sr.; father of Secretary of State Thomas F. Bayard.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Delaware's border state Democratic conservatism — the state's slaveholder-friendly Democratic tradition that opposed both abolitionism and the Republican Party's antislavery politics — created the political environment for Bayard's Peace Democrat stance",
            "Lincoln's wartime emergency powers — the suspension of habeas corpus and the loyalty oath requirements that Lincoln's administration imposed — created the constitutional issues that Bayard opposed on civil liberties grounds",
            "The Bayard family's Delaware political dynasty — the senior Bayard's Senate career and the family's deep roots in Delaware's legal and political elite — provided the standing for the younger Bayard's Senate career"
        ],
        "effects": [
            "His Peace Democrat Senate leadership contributed to the organized wartime opposition — the Democrats who argued that the war could be ended by negotiation and that Lincoln's emergency powers violated the Constitution",
            "His resignation over the loyalty oath created one of the most dramatic examples of principled opposition to wartime loyalty requirements — contributing to the legal and political debate over civil liberties in wartime",
            "His post-war Senate return contributed to the Democratic Party's effort to re-establish itself after the Civil War — the 'Bourbon Democrat' tradition of fiscal conservatism and constitutional restraint",
            "His family's political dynasty — father senator, son secretary of state — contributed to Delaware's distinctive political culture of aristocratic Democratic leadership"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Delaware Senator 1851–1864 and 1867–1869"},
            {"target": "peace-democrats", "verb": "LEADS", "note": "Prominent Copperhead Senator opposing the Civil War"},
            {"target": "loyalty-oath-controversy", "verb": "RESIGNS_OVER", "note": "Resigned Senate rather than take loyalty oath"},
            {"target": "james-a-bayard-sr", "verb": "SON_OF", "note": "Son of Delaware Senator James A. Bayard Sr."},
            {"target": "thomas-f-bayard", "verb": "FATHER_OF", "note": "Father of Secretary of State Thomas F. Bayard"}
        ]
    }),

    ("john-church-hamilton", {
        "summary": (
            "John Church Hamilton (1792–1882) "
            "was an American lawyer "
            "and historian who "
            "is primarily known "
            "as the son of Alexander "
            "Hamilton and as "
            "the author of a "
            "major biography "
            "of his father. "
            "His seven-volume "
            "'History of the "
            "Republic of the "
            "United States as "
            "traced in the "
            "writings of Alexander "
            "Hamilton and his "
            "contemporaries' "
            "(1857–1864) was "
            "a massive biographical "
            "and historical work "
            "that championed "
            "his father's legacy "
            "and presented "
            "the Federalist perspective "
            "on the founding era "
            "in exhaustive detail.\n\n"
            "Hamilton served "
            "briefly in the "
            "War of 1812 and "
            "had a legal career "
            "in New York City, "
            "but his most significant "
            "contribution was "
            "historical — "
            "preserving, editing, "
            "and defending his "
            "father's legacy "
            "during the Jacksonian "
            "era when Democratic "
            "politics had largely "
            "displaced Federalism.\n\n"
            "His editorial work "
            "on his father's "
            "papers contributed "
            "to the preservation "
            "of primary sources "
            "for American founding-era history.\n\n"
            "'My father built "
            "the republic I am "
            "determined to document.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Son of Alexander Hamilton and author of a seven-volume 'History of the Republic' (1857–1864); champion of his father's Federalist legacy during the Jacksonian era; edited and preserved Hamilton's papers; War of 1812 veteran; his historical work contributed primary source preservation for the founding era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Alexander Hamilton's political legacy — the Federalist founder's enormous but contested significance in American history, his assassination by Aaron Burr, and the Democratic-Republican vilification of Hamiltonism — created both the importance of defending Hamilton's legacy and the adversarial context in which John Church Hamilton worked",
            "The Jacksonian era's anti-Federalist culture — the political revolution that had largely displaced Federalism and elevated Jeffersonian and Jacksonian principles — created the hostile intellectual environment against which Hamilton's son marshaled the seven-volume defense",
            "The 19th-century American biographical tradition — the genre of massive multi-volume 'Lives' that used biography as a vehicle for political and historical argument — created the form within which John Church Hamilton's historical defense operated"
        ],
        "effects": [
            "His seven-volume history contributed to the preservation of Alexander Hamilton's documentary legacy — editing and publishing his father's papers and correspondence in an era before systematic archival institutions existed",
            "His biographical championing contributed to the counter-narrative against Jeffersonian and Jacksonian disparagement of Hamiltonian Federalism — keeping the Federalist perspective in the historical conversation",
            "His editorial work contributed primary sources for subsequent generations of American historians — the Hamilton papers and correspondence he preserved being essential resources for the study of the founding era",
            "His long life (1792–1882) — from Alexander Hamilton's death through the Civil War and into the Gilded Age — placed him as a living link between the founding generation and the modern American state"
        ],
        "relationships": [
            {"target": "alexander-hamilton", "verb": "SON_OF", "note": "Son of the Federalist founder"},
            {"target": "history-of-the-republic", "verb": "AUTHORS", "note": "Seven-volume historical defense of Hamilton's legacy"},
            {"target": "federalist-tradition", "verb": "DEFENDS", "note": "Biographer championing Hamiltonism in the Jacksonian era"},
            {"target": "war-of-1812", "verb": "SERVES_IN", "note": "Brief military service"},
            {"target": "american-founding-history", "verb": "DOCUMENTS", "note": "Preserved primary sources for the founding era"}
        ]
    }),

    ("pierre-antoine-berryer", {
        "summary": (
            "Pierre-Antoine Berryer "
            "(1790–1868) was a French "
            "lawyer and Legitimist "
            "politician who was "
            "considered the greatest "
            "forensic orator "
            "of 19th-century France "
            "— his courtroom speeches "
            "defending Legitimist "
            "political defendants "
            "being compared to "
            "Cicero and Demosthenes. "
            "A devoted Legitimist "
            "who championed "
            "the Bourbon royal "
            "cause through "
            "three French regimes, "
            "Berryer defended "
            "clients including "
            "Marshal Ney (1815), "
            "the Duchess of Berry "
            "after her failed "
            "royalist insurrection "
            "(1832), and Louis-Napoleon "
            "Bonaparte after "
            "the Strasbourg coup "
            "attempt (1836).\n\n"
            "His defense of Marshal "
            "Ney — Napoleon's "
            "'Bravest of the Brave' "
            "who was executed "
            "for treason after "
            "the Hundred Days "
            "— was one of "
            "the most famous "
            "and tragic forensic "
            "performances in "
            "French legal history.\n\n"
            "He also served "
            "as a deputy in "
            "the Chamber for "
            "decades, representing "
            "the Legitimist "
            "cause in the legislature.\n\n"
            "He was elected "
            "to the Académie française."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Greatest forensic orator of 19th-century France (1790–1868); Legitimist politician and lawyer who defended Marshal Ney (1815), the Duchess of Berry (1832), and Louis-Napoleon Bonaparte (1836); Académie française member; deputy across multiple regimes; compared to Cicero and Demosthenes for his courtroom eloquence; dedicated Bourbon royalist across all French political changes.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Bourbon Restoration's political culture — the return of the Legitimist monarchy and the passionate royalist politics that it inspired among the French upper classes — created the political cause that animated Berryer's lifetime commitment to the Bourbon royal family",
            "Berryer's extraordinary forensic gifts — his natural eloquence and his rigorous legal training that made him the Paris bar's unquestioned master of courtroom advocacy — created the means through which his Legitimist politics expressed itself in landmark criminal defenses",
            "The dramatic political trials that 19th-century France generated — from Marshal Ney's treason prosecution to the Duchess of Berry's insurrection case to Louis-Napoleon's Strasbourg coup attempt — created the opportunities for Berryer's most celebrated forensic performances"
        ],
        "effects": [
            "His defense of Marshal Ney contributed to one of the most discussed forensic contests in French legal history — the case that raised fundamental questions about military loyalty, the law of nations, and the restoration's vindictiveness",
            "His defense of Louis-Napoleon contributed paradoxically to the future Napoleon III's political rehabilitation — the eloquent defense that helped position Louis-Napoleon as a romantic martyr rather than a criminal conspirator",
            "His long chamber career contributed the Legitimist perspective to three French legislative assemblies — maintaining the Bourbon royalist voice in the representative bodies that Louis-Philippe and the Third Republic established",
            "His Académie française membership contributed to the crossover between political and cultural life in 19th-century France — the great orator recognized as much for his literary eloquence as his political advocacy"
        ],
        "relationships": [
            {"target": "marshal-ney", "verb": "DEFENDS", "note": "Defense lawyer in Ney's 1815 treason trial"},
            {"target": "duchess-of-berry", "verb": "DEFENDS", "note": "Defended after 1832 Legitimist insurrection"},
            {"target": "napoleon-iii", "verb": "DEFENDS", "note": "Defended Louis-Napoleon after 1836 Strasbourg coup"},
            {"target": "legitimist-movement", "verb": "LEADS", "note": "Political champion of the Bourbon Legitimist cause"},
            {"target": "académie-française", "verb": "MEMBER_OF", "note": "Académie française member for oratorical genius"}
        ]
    }),

    ("john-sloss-hobart", {
        "summary": (
            "John Sloss Hobart (1738–1805) "
            "was an American Federalist "
            "jurist and politician "
            "from New York who "
            "served as an Associate "
            "Justice of the New "
            "York Supreme Court "
            "(1777–1798) and briefly "
            "in the U.S. Senate "
            "(1798). A member "
            "of New York's founding "
            "generation, Hobart "
            "participated in the "
            "Revolutionary-era "
            "politics that created "
            "the new state of "
            "New York — including "
            "service on the "
            "Committee of One Hundred "
            "that governed New "
            "York City before "
            "the British occupation.\n\n"
            "His two-decade "
            "New York Supreme "
            "Court service made "
            "him one of the "
            "foundational figures "
            "in New York's "
            "early legal development "
            "— the period when "
            "New York was "
            "building its "
            "judicial institutions "
            "from the foundations "
            "of colonial law.\n\n"
            "Hobart College "
            "in Geneva, New York "
            "was named in "
            "his honor — a "
            "lasting memorial "
            "to his distinguished "
            "public service.\n\n"
            "He was a leading "
            "figure in New York's "
            "founding legal culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New York Supreme Court Justice (1777–1798) and briefly U.S. Senator (1798); founding-era New York jurist building the state's legal institutions; participated in Revolutionary-era governance; Hobart College named in his honor; twenty-year judicial service during New York's foundational legal period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Revolutionary political transformation — the colony's transformation into a republic and its need to build new judicial institutions — created the opportunity for Hobart's two-decade Supreme Court service",
            "The founding era's legal vacuum — the need to replace colonial legal institutions with republican ones that balanced continuity with common law and innovation with republican principles — created the judicial work of Hobart's generation",
            "New York's Federalist legal culture — the state's Federalist political tradition under Hamilton and Jay that placed legal order and institutional development at the center of political concerns — created the environment for Hobart's distinguished judicial career"
        ],
        "effects": [
            "His twenty-year Supreme Court service contributed to New York's foundational legal development — the decisions and legal precedents that shaped the law of America's most populous and commercially important state",
            "His participation in Revolutionary-era governance contributed to New York's transition from colony to state — the political work of creating republican institutions from the ruins of royal government",
            "Hobart College's naming preserved his memory — the educational institution that still bears his name as a permanent memorial to his service",
            "His career contributed to the tradition of Federalist legal culture in New York — the institutional building that Hamilton, Jay, and their contemporaries like Hobart undertook as the foundation of the American republic"
        ],
        "relationships": [
            {"target": "new-york-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1777–1798"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New York Senator briefly in 1798"},
            {"target": "hobart-college", "verb": "MEMORIALIZED_IN", "note": "College named in his honor"},
            {"target": "new-york", "verb": "SERVES", "note": "Founding-era New York jurist and statesman"},
            {"target": "american-revolution", "verb": "SERVES_DURING", "note": "Revolutionary-era politician and jurist"}
        ]
    }),

    ("josef-franz-karl-amrhyn", {
        "summary": (
            "Josef Franz Karl Amrhyn "
            "(1777–1848) was a Swiss "
            "politician from the "
            "canton of Lucerne "
            "who served in Swiss "
            "federal and cantonal "
            "politics during the "
            "turbulent period of "
            "Swiss political transformation "
            "from the Helvetic Republic "
            "through the Restoration "
            "and the Regeneration "
            "movement that led to "
            "the modern Swiss "
            "federal state. "
            "Lucerne in this era "
            "was a predominantly "
            "Catholic conservative "
            "canton that often "
            "found itself in "
            "political opposition "
            "to the more liberal "
            "Protestant cantons — "
            "a division that would "
            "eventually produce "
            "the Sonderbund War "
            "of 1847, just months "
            "before Amrhyn died.\n\n"
            "Swiss cantonal politics "
            "in this era were "
            "characterized by "
            "the tension between "
            "the conservative Catholic "
            "cantons' desire to "
            "preserve cantonal "
            "sovereignty and "
            "the liberal Protestant "
            "cantons' push for "
            "a stronger federal "
            "constitution.\n\n"
            "The Sonderbund War's "
            "outcome — the liberal "
            "cantons' victory "
            "and the 1848 federal "
            "constitution — "
            "transformed Switzerland.\n\n"
            "He was a significant "
            "Lucerne conservative Catholic figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Swiss Lucerne politician (1777–1848); active during the transformation from Helvetic Republic through Restoration to the modern federal state; represented Catholic conservative Lucerne's cantonal sovereignty against liberal Protestant cantons; active during the period leading to the Sonderbund War (1847) and the 1848 Swiss federal constitution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Lucerne's Catholic conservative political culture — the canton's deep Catholicism, its defense of cantonal sovereignty, and its resistance to liberal Protestant-dominated federal reforms — created the political environment from which Amrhyn's career emerged",
            "The Swiss Regeneration movement — the 1830s liberal constitutional reform movement in several cantons that pushed for more democratic and federal governance — created the political challenge to which conservative Lucerne politicians like Amrhyn responded",
            "The Sonderbund formation — the Catholic conservative cantons' defensive alliance against the liberal Protestant majority's push for stronger federal government — created the political crisis that defined the final years of Amrhyn's life"
        ],
        "effects": [
            "His Lucerne political career contributed to the conservative Catholic cantonal tradition — the defense of cantonal sovereignty and Catholic religious governance against liberal centralization",
            "His political generation's confrontation with the Regeneration movement contributed to the polarization that eventually produced the Sonderbund War and the 1848 federal constitution",
            "His death in 1848 coincided with the transformation his career had resisted — the very year the liberal cantons' victory produced the modern Swiss federal constitution",
            "His career illustrated the conservative Catholic Switzerland that the 1848 transformation displaced — the older cantonal sovereignty tradition giving way to a more integrated federal state"
        ],
        "relationships": [
            {"target": "lucerne", "verb": "SERVES", "note": "Lucerne cantonal politician"},
            {"target": "sonderbund", "verb": "ASSOCIATED_WITH", "note": "Catholic conservative cantonal alliance"},
            {"target": "swiss-federal-constitution-1848", "verb": "PRECEDES", "note": "Conservative opponent of the liberal federal transformation"},
            {"target": "swiss-regeneration-movement", "verb": "OPPOSES", "note": "Conservative resistance to liberal cantonal reform"},
            {"target": "switzerland", "verb": "SERVES", "note": "Swiss federal and cantonal politician"}
        ]
    }),

    ("braulio-carrillo-colina", {
        "summary": (
            "Braulio Carrillo Colina "
            "(1800–1845) was a Costa "
            "Rican politician and "
            "jurist who served as "
            "Chief of State of "
            "Costa Rica (1835–1837 "
            "and 1838–1842) — one "
            "of the most consequential "
            "figures in Costa Rican "
            "nation-building. Carrillo "
            "is credited with "
            "separating Costa Rica "
            "definitively from "
            "the Central American "
            "Federation and declaring "
            "Costa Rica's independent "
            "sovereignty in 1838 "
            "— an act that created "
            "the modern Costa "
            "Rican state. He also "
            "instituted the Law "
            "of Basis and Guarantees "
            "(1841) — a quasi-constitutional "
            "document that organized "
            "Costa Rican governance "
            "— and promoted the "
            "coffee economy that "
            "would transform the country.\n\n"
            "His authoritarian "
            "governance — he ruled "
            "by decree — provoked "
            "resistance from "
            "other Costa Rican "
            "political figures, "
            "leading to the "
            "conspiracy that "
            "brought Francisco "
            "Morazán to overthrow "
            "him in 1842.\n\n"
            "He was subsequently "
            "exiled and assassinated "
            "in El Salvador in 1845.\n\n"
            "He is considered one "
            "of Costa Rica's "
            "founding fathers."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Costa Rican Chief of State (1835–1837 and 1838–1842); declared Costa Rica's independence from the Central American Federation (1838) — creating the modern Costa Rican state; instituted the Law of Basis and Guarantees (1841); promoted the coffee economy; overthrown by Francisco Morazán (1842) and assassinated in El Salvador (1845); considered one of Costa Rica's founding fathers.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Central American Federation's dysfunction — the federal union's political instability and its inability to govern the diverse Central American states — created the context in which Carrillo's declaration of Costa Rican independence became viable",
            "Costa Rica's geographic isolation — the country's separation from the more turbulent northern Central American states by mountains and distance — created the conditions in which an independent Costa Rica was geographically and economically viable",
            "Carrillo's political ambition and administrative vision — his determination to build a functioning Costa Rican state through authoritarian governance and economic development — created the decisive political will that drove the independence declaration"
        ],
        "effects": [
            "His independence declaration created the modern Costa Rican state — the formal separation from the Central American Federation that established Costa Rica as a sovereign independent nation",
            "His promotion of the coffee economy helped establish the agricultural foundation that would make Costa Rica prosperous — the coffee cultivation in the Central Valley that generated the commercial wealth funding the country's development",
            "His Law of Basis and Guarantees provided Costa Rica's first quasi-constitutional framework — organizing governance in ways that established precedents for subsequent constitutions",
            "His overthrow and assassination illustrated the violence of Central American founding-era politics — the personal costs of the political conflicts that attended the establishment of the post-colonial states"
        ],
        "relationships": [
            {"target": "costa-rica", "verb": "LEADS_AND_FOUNDS", "note": "Chief of State and independence declarant"},
            {"target": "central-american-federation", "verb": "SEPARATES_FROM", "note": "Declared Costa Rican independence 1838"},
            {"target": "law-of-basis-and-guarantees", "verb": "INSTITUTES", "note": "Costa Rica's quasi-constitutional document 1841"},
            {"target": "costa-rican-coffee-economy", "verb": "PROMOTES", "note": "Encouraged coffee cultivation transforming the economy"},
            {"target": "francisco-morazán", "verb": "OVERTHROWN_BY", "note": "Morazán's coup ended Carrillo's rule in 1842"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 81 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
