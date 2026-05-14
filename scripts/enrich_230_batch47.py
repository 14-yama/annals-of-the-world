#!/usr/bin/env python3
"""
Batch 47 — 8 entities: George W. Crawford, David Brearley, Sarah Bush Lincoln,
Joaquín María López y López, Jean-Nicolas Bouilly, Nathaniel P. Tallmadge,
John Milledge, Samuel Dexter
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

    # 1 — George W. Crawford
    ("george-w-crawford", {
        "summary": (
            "George Walker Crawford (1798–1872) was a "
            "Georgia lawyer and Whig politician who "
            "served as Georgia's Attorney General "
            "(1827–1831), as a US Representative "
            "(1843, appointed), as Governor of "
            "Georgia (1843–1847), and as US "
            "Secretary of War (1849–1850) under "
            "President Zachary Taylor — one of "
            "Georgia's most prominent antebellum "
            "political figures and a leading voice "
            "of Southern Whiggery in the pre-secession "
            "era. He also served in the Georgia "
            "General Assembly for five years.\n\n"
            "His gubernatorial term (1843–1847) was "
            "the most significant of his state-level "
            "career: he presided over a period of "
            "Georgia's economic development and "
            "managed the political tensions of "
            "the pre-Mexican War era, building "
            "the Whig organization in a state "
            "where Democrats had historically "
            "dominated. His administration "
            "advanced railroad development and "
            "public education.\n\n"
            "His appointment as Taylor's Secretary "
            "of War elevated him to the national "
            "cabinet during the critical year "
            "of the Compromise of 1850 debate — "
            "the sectional crisis over the "
            "status of territories acquired from "
            "Mexico in which Southern Whigs like "
            "Crawford attempted to balance "
            "Southern interests with Unionist "
            "commitment. He resigned when Taylor "
            "died in 1850.\n\n"
            "His career illustrated the trajectory "
            "of Georgia Whiggery — from "
            "states'-rights conservatism in "
            "the 1820s to national Whig alliance "
            "in the 1840s, ultimately unable to "
            "survive the slavery crisis that "
            "destroyed the party after 1852."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia Governor (1843–1847); US Secretary of War under Zachary Taylor (1849–1850); Georgia Attorney General (1827–1831); Georgia US Representative; leading Southern Whig; resigned from Taylor's cabinet when Taylor died during the Compromise of 1850 debate; his career traced the arc of Georgia Whiggery from states'-rights conservatism to national party alliance and collapse.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's Whig political tradition — rooted in opposition to Jacksonian Democratic policies and the states'-rights doctrine of Georgia's planter elite — created the political identity that shaped Crawford's career, as he emerged as one of Georgia's leading Whig voices during the era when that party briefly challenged Democratic dominance in the South",
            "The Mexican-American War's territorial acquisitions and the resulting Compromise of 1850 debate — which forced Southern politicians to take positions on the extension of slavery into newly acquired territories — created the sectional crisis that dominated Crawford's national cabinet service as Taylor's Secretary of War",
            "Crawford's combination of legal expertise, gubernatorial experience, and Georgia Whig organizational leadership made him the natural choice for Taylor's cabinet appointment — as Taylor sought Southern Whig voices to balance his administration's regional representation"
        ],
        "effects": [
            "His Georgia gubernatorial administration contributed to the state's railroad development and public education — advancing the infrastructure and educational programs that were essential to Georgia's antebellum economic development during the 1840s",
            "His service as Taylor's Secretary of War contributed to the administration's management of the post-Mexican War military transition — overseeing the Army during the period when the Compromise of 1850 debate was determining the political future of the newly acquired territories",
            "His resignation following Taylor's death in 1850 contributed to the political transition from the Taylor administration to Millard Fillmore's — as Southern Whigs who had been appointed by Taylor departed alongside his presidency, and Fillmore's more compromise-oriented cabinet took over",
            "His career as a Georgia Whig leader contributed to the attempt to build a viable Southern Whig organization — a political project that ultimately failed as slavery politics dissolved the Whig Party after 1852 and forced Southern Whig politicians to choose between the Democrats and the emerging Republican Party"
        ],
        "relationships": [
            {"entity": "Governor of Georgia (1843–1847, Whig)", "relationship": "GOVERNOR", "note": "Served as Georgia's Governor (1843–1847) — advancing railroad development and public education while building the Whig organization in a state where Democrats had historically dominated"},
            {"entity": "US Secretary of War under Zachary Taylor (1849–1850)", "relationship": "SECRETARY_OF_WAR", "note": "Served as Taylor's Secretary of War (1849–1850) — overseeing the Army during the critical Compromise of 1850 debate; resigned when Taylor died"},
            {"entity": "Georgia Attorney General (1827–1831, appointed by Governor Forsyth)", "relationship": "ATTORNEY_GENERAL", "note": "Served as Georgia's Attorney General (1827–1831) — his first major state office, appointed by Governor John Forsyth"},
            {"entity": "Compromise of 1850 debate / Zachary Taylor administration", "relationship": "SECRETARY_OF_WAR_DURING", "note": "Served as Secretary of War during the Compromise of 1850 debate — the sectional crisis over slavery in territories acquired from Mexico that defined the Taylor administration's political landscape"},
            {"entity": "Georgia Whig Party / Southern Whiggery (pre-Civil War)", "relationship": "LEADING_FIGURE_OF", "note": "One of Georgia's leading Whig politicians — building the state party organization and representing Southern Whiggery's attempt to balance states'-rights conservatism with national party alliance"}
        ]
    }),

    # 2 — David Brearley
    ("david-brearley", {
        "summary": (
            "David Brearley (1745–1790) was a New Jersey "
            "lawyer and jurist who served as Chief "
            "Justice of New Jersey's Supreme Court "
            "(1779–1789), as a delegate from New Jersey "
            "to the Constitutional Convention of 1787 "
            "— signing the United States Constitution "
            "— and as the first United States District "
            "Judge for the District of New Jersey, "
            "appointed by President Washington in 1789. "
            "He is also notable for having chaired "
            "the Convention's Committee on Postponed "
            "Matters, which finalized several key "
            "constitutional provisions.\n\n"
            "His Revolutionary War service began "
            "dramatically: arrested for treason by "
            "the British-aligned colonial authorities "
            "in 1776 for organizing a militia company, "
            "he was freed by a crowd of patriots — "
            "an episode that established his "
            "Revolutionary credentials. He served "
            "as a Continental Army colonel and "
            "helped organize New Jersey's military "
            "contribution to the war effort.\n\n"
            "At the Constitutional Convention, "
            "he was among the small-state delegates "
            "who supported equal representation "
            "for all states in the Senate — the "
            "position that produced the Connecticut "
            "Compromise granting every state two "
            "senators regardless of population. "
            "As chairman of the Committee on "
            "Postponed Matters (also called the "
            "Committee of Eleven), he helped "
            "finalize the Electoral College "
            "provisions, the presidential term "
            "length, and several other "
            "constitutional details.\n\n"
            "His early death at 44 cut short "
            "what might have been a distinguished "
            "federal judicial career, but his "
            "constitutional contributions — "
            "particularly the small-state "
            "compromise and the Electoral "
            "College provisions — gave him "
            "a permanent place in the founding."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New Jersey Founding Father; Chief Justice of New Jersey (1779–1789); delegate to and signer of the US Constitution at the 1787 Constitutional Convention; chairman of the Committee on Postponed Matters that finalized Electoral College provisions; first US District Judge for New Jersey; small-state advocate whose position helped produce the Senate's equal representation compromise.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's status as a small state with legitimate concerns about proportional representation — and the Constitutional Convention's deadlock between large-state and small-state delegates over whether Congress should represent population or states — created the political context for Brearley's advocacy of equal Senate representation that contributed to the Connecticut Compromise",
            "The Constitutional Convention's practical need to resolve dozens of specific constitutional provisions through committee work — including the Electoral College mechanism, presidential term length, and other contested details that full-convention debate had left unresolved — created the Committee on Postponed Matters that Brearley chaired",
            "Brearley's combined credentials as Chief Justice of New Jersey, Continental Army colonel, and Revolutionary activist made him the obvious choice for New Jersey's Constitutional Convention delegation — and his legal expertise made him suitable for the Committee on Postponed Matters' technical legal drafting work"
        ],
        "effects": [
            "His small-state advocacy at the Constitutional Convention contributed to the Connecticut Compromise — the agreement that gave each state equal representation in the Senate regardless of population, a foundational structural decision that has shaped American politics for 235 years",
            "His chairmanship of the Committee on Postponed Matters contributed to the finalization of the Electoral College provisions — the presidential selection mechanism that the Convention had struggled to resolve, and whose details the Committee worked out in the Convention's final weeks",
            "His appointment as the first US District Judge for New Jersey contributed to the establishment of the federal judiciary in New Jersey — one of the early appointments that gave concrete institutional form to the new Constitution's judicial branch in the states",
            "His Committee on Postponed Matters work contributed to the finalization of several constitutional provisions that had been left unresolved in full-convention debate — including the presidential eligibility requirements, the commander-in-chief clause details, and the pardoning power — making his committee among the most practically significant in the Convention's final weeks"
        ],
        "relationships": [
            {"entity": "US Constitutional Convention of 1787 (delegate from New Jersey, signer)", "relationship": "DELEGATE_AND_SIGNER", "note": "Served as a New Jersey delegate to the Constitutional Convention of 1787 and signed the Constitution — one of 39 signers who ratified the founding document"},
            {"entity": "Committee on Postponed Matters / Committee of Eleven (chairman)", "relationship": "CHAIRMAN_OF", "note": "Chaired the Constitutional Convention's Committee on Postponed Matters — the committee that finalized Electoral College provisions, presidential term length, and other contested constitutional details"},
            {"entity": "Chief Justice of New Jersey Supreme Court (1779–1789)", "relationship": "CHIEF_JUSTICE", "note": "Served as Chief Justice of New Jersey's Supreme Court (1779–1789) — the ten-year judicial tenure that established his legal credentials before the Constitutional Convention and his federal appointment"},
            {"entity": "First US District Judge, District of New Jersey (1789–1790, Washington appointee)", "relationship": "FIRST_FEDERAL_DISTRICT_JUDGE_FOR_NJ", "note": "Appointed by Washington as the first US District Judge for New Jersey in 1789 — giving institutional form to the new Constitution's federal judicial branch in the state"},
            {"entity": "Connecticut Compromise / small-state equal Senate representation", "relationship": "SMALL-STATE_ADVOCATE_CONTRIBUTING_TO", "note": "A key small-state advocate at the Convention whose position contributed to the Connecticut Compromise — the agreement giving each state equal representation in the Senate that resolved the Convention's most dangerous deadlock"}
        ]
    }),

    # 3 — Sarah Bush Lincoln
    ("sarah-bush-lincoln", {
        "summary": (
            "Sarah Bush Lincoln (1788–1869) was an "
            "American frontier woman from Kentucky "
            "who became the stepmother of Abraham "
            "Lincoln after marrying his widowed "
            "father Thomas Lincoln in 1819. Born "
            "Sarah Bush in Hardin County, Kentucky, "
            "she first married Daniel Johnston in "
            "1806 and bore three children before "
            "his death in 1816. When Thomas Lincoln "
            "sought her out following the death "
            "of his first wife Nancy Hanks Lincoln, "
            "she joined his household on the "
            "Indiana frontier along with her "
            "three children and her furniture.\n\n"
            "She is credited by Lincoln biographers "
            "and by Lincoln himself with being a "
            "transformative influence on young "
            "Abraham's development: she reportedly "
            "encouraged his reading and education "
            "at a time when his father valued "
            "practical farm labor over book "
            "learning, kept his interest in "
            "learning alive in the intellectually "
            "sparse frontier environment, and "
            "formed an exceptionally warm bond "
            "with her stepson that lasted "
            "throughout his life.\n\n"
            "Lincoln called her 'my angel mother' "
            "and visited her at her Illinois home "
            "in January 1861, just before his "
            "departure for Washington as "
            "President-elect — telling her "
            "goodbye with the presentiment "
            "that he might not return alive. "
            "She survived him, dying in "
            "1869, four years after "
            "his assassination.\n\n"
            "Her role in Lincoln's formation — "
            "sustaining the young future president's "
            "intellectual curiosity in a household "
            "that otherwise offered little "
            "encouragement — made her one of "
            "the most historically significant "
            "maternal figures of the 19th century."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Stepmother of Abraham Lincoln; credited with nurturing Lincoln's love of learning in the Indiana frontier household; Lincoln called her 'my angel mother'; visited her as President-elect in January 1861; outlived Lincoln, dying 1869; her encouragement of young Lincoln's education is consistently cited by biographers as a crucial influence on the formation of one of history's most consequential political leaders.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The death of Nancy Hanks Lincoln in 1818 — leaving Thomas Lincoln with two young children on the Indiana frontier in a dirty, windowless cabin — created the domestic crisis that led Thomas to seek a second wife, and his selection of the capable Sarah Bush transformed the Lincoln household from neglect to nurture",
            "The Indiana frontier's intellectual scarcity — where formal schooling was sporadic, books were rare, and most settlers valued physical labor over learning — created the environment in which Sarah's sympathetic encouragement of Abraham's reading and curiosity was particularly valuable, counterbalancing the dominant frontier culture that might otherwise have extinguished his intellectual development",
            "Sarah's own character — her warmth, competence, and evident appreciation of Abraham's unusual intelligence — created the emotional bond that Lincoln cherished throughout his adult life, visiting her as President-elect and acknowledging her influence as formative to his development"
        ],
        "effects": [
            "Her encouragement of Abraham Lincoln's reading and education contributed to the intellectual formation of one of history's most consequential political leaders — sustaining his curiosity and love of learning through the years when he had almost no formal schooling and his father saw little value in book learning over farm work",
            "Her emotionally warm presence as a stepmother contributed to Lincoln's psychological development on the frontier — providing the nurturing stability that his mother's early death had removed, and creating the family attachment that Lincoln acknowledged with the 'angel mother' tribute",
            "Lincoln's January 1861 farewell visit to her — when he told her he feared he might not return — contributed to the historical record of the Lincoln family's emotional bonds and the sense of foreboding with which he approached the presidency, a detail that biographers have found significant in understanding his psychological state at the eve of the Civil War",
            "Her survival to 1869 — four years after Lincoln's assassination — contributed to the historical preservation of memories and testimonies about Lincoln's childhood and youth, as witnesses sought out figures who had known the young Lincoln and could describe his formation on the Indiana frontier"
        ],
        "relationships": [
            {"entity": "Abraham Lincoln (stepson, 16th President of the United States)", "relationship": "STEPMOTHER_OF", "note": "Stepmother of Abraham Lincoln — credited by Lincoln himself and by biographers as a transformative nurturing influence who encouraged his education and formed the warmest family bond of his frontier childhood"},
            {"entity": "Thomas Lincoln (second husband, father of Abraham Lincoln)", "relationship": "SECOND_WIFE_OF", "note": "Second wife of Thomas Lincoln — whom she married in 1819 after his first wife Nancy Hanks Lincoln died, joining his Indiana frontier household with her three children from her first marriage"},
            {"entity": "Indiana frontier (Lincoln family, 1819–1830)", "relationship": "STEPMOTHER_IN_HOUSEHOLD_ON", "note": "Managed the Lincoln household on the Indiana frontier (1819–1830) — where her nurturing of Abraham's education counterbalanced the intellectual scarcity of frontier life"},
            {"entity": "Lincoln's 'angel mother' farewell visit (January 1861, President-elect visit)", "relationship": "RECEIVED_FAREWELL_VISIT_FROM", "note": "Received Lincoln's farewell visit in January 1861 when he departed for Washington as President-elect — the visit in which he told her goodbye with the presentiment he might not return alive, she calling him 'her Abe'"},
            {"entity": "Lincoln family formation / frontier childhood / intellectual development of Lincoln", "relationship": "CRUCIAL_NURTURING_INFLUENCE_ON", "note": "A crucial nurturing influence on Lincoln's intellectual formation — her encouragement of his reading and education in a household and environment that otherwise offered little support for book learning"}
        ]
    }),

    # 4 — Joaquín María López y López
    ("joaquín-maría-lópez-y-lópez", {
        "summary": (
            "Joaquín María López y López (1798–1855) "
            "was a Spanish lawyer, journalist, "
            "and liberal politician who served "
            "twice as Prime Minister of Spain "
            "in 1843 during the reign of "
            "Queen Isabella II — the year in "
            "which the constitutional crisis "
            "surrounding Isabella's declared "
            "majority of age (at thirteen, "
            "to end the regency of Espartero) "
            "transformed Spanish politics. "
            "He also served as Minister of "
            "the Interior (1836–1837) and "
            "as Mayor of Madrid in 1840.\n\n"
            "His political career unfolded "
            "against the backdrop of Spain's "
            "turbulent transition from "
            "Bourbon absolutism to constitutional "
            "monarchy — the Carlist Wars, "
            "the progressive and moderate "
            "liberal factions' competition "
            "over the constitutional framework, "
            "and the military-political "
            "interventionism that characterized "
            "Isabella II's reign. He aligned "
            "with the Progresista (Progressive) "
            "liberal faction.\n\n"
            "His two prime ministerial terms "
            "in 1843 — both brief — occurred "
            "during the political maneuvers "
            "that ended Espartero's regency "
            "and established Isabella's "
            "personal rule: first from "
            "May to July, then again for "
            "a few weeks in November. "
            "The instability of his tenures "
            "reflected the volatility of "
            "Spanish constitutional politics "
            "in the mid-19th century, "
            "when ministries rose and fell "
            "within months.\n\n"
            "As a writer and journalist, "
            "he contributed to Spanish "
            "liberal political culture — "
            "the press tradition that "
            "sustained progressive "
            "constitutional arguments "
            "through the alternating "
            "periods of political "
            "freedom and repression."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish Prime Minister twice in 1843 (during Queen Isabella II's declared majority of age ending Espartero's regency); Minister of the Interior (1836–1837); Mayor of Madrid (1840); Progressive liberal politician; journalist and writer; his brief but significant premierships occurred at a pivotal constitutional moment in Spain's turbulent mid-19th-century political history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Spain's turbulent transition from absolutism to constitutional monarchy — the First Carlist War (1833–1840), the competing liberal factions' constitutional battles, and the military's repeated intervention in politics — created the unstable political environment in which López's rapid succession of offices and his two brief prime ministerial terms occurred",
            "The crisis of Espartero's regency (1840–1843) — which had alienated both progressive and moderate liberals and prompted a military-political coalition to end it — created the political vacuum in which López served as prime minister during the transition to Isabella II's personal rule",
            "López's Progressive liberal credentials — his journalism, his political alignment with the Progresista faction, and his earlier ministerial experience — made him one of the natural candidates for the brief transition governments that managed the constitutional moment of Isabella's declared majority"
        ],
        "effects": [
            "His prime ministerial tenures in 1843 contributed to the management of Spain's critical constitutional transition — the declaration of Isabella II's majority of age at thirteen and the end of Espartero's regency, which established the framework for the subsequent decade of Isabella's contested personal rule",
            "His Ministry of the Interior service (1836–1837) contributed to Spanish domestic governance during the First Carlist War — managing internal security, administration, and the liberal constitutional program during the most dangerous years of the Carlist threat to the constitutional monarchy",
            "His journalistic and literary work contributed to Spain's Progressive liberal political culture — building the press and intellectual infrastructure that sustained constitutional liberal arguments through the alternating periods of freedom and repression that characterized Isabella II's reign",
            "His career illustrated the characteristic pattern of Spanish moderate and progressive liberal politics in the mid-19th century — fluid factional alignments, frequent ministerial changes, and the perpetual tension between civilian liberal programs and military-political interventionism that prevented stable constitutional governance"
        ],
        "relationships": [
            {"entity": "Prime Minister of Spain (twice in 1843, Queen Isabella II's reign)", "relationship": "PRIME_MINISTER", "note": "Served twice as Spanish Prime Minister in 1843 — brief tenures during the critical constitutional transition that ended Espartero's regency and established Isabella II's personal rule"},
            {"entity": "Queen Isabella II of Spain / Espartero regency (1840–1843)", "relationship": "PRIME_MINISTER_DURING_END_OF_REGENCY_OF", "note": "Served as prime minister during the political maneuvers that ended Espartero's regency and declared Isabella II's majority of age — a pivotal constitutional moment in mid-19th-century Spanish history"},
            {"entity": "Minister of the Interior, Spain (1836–1837)", "relationship": "MINISTER_OF_THE_INTERIOR", "note": "Served as Spain's Minister of the Interior (1836–1837) — managing domestic governance and security during the First Carlist War"},
            {"entity": "Mayor of Madrid (1840)", "relationship": "MAYOR_OF", "note": "Served as Mayor of Madrid in 1840 — one of several political offices spanning national and municipal governance during Spain's turbulent constitutional period"},
            {"entity": "Progresista (Progressive) liberal faction / Spanish constitutional liberalism", "relationship": "ALIGNED_WITH_AND_REPRESENTATIVE_OF", "note": "Aligned with Spain's Progressive liberal faction — contributing through both political office and journalism to the constitutional liberal tradition that sought to establish parliamentary government against absolutist and military opposition"}
        ]
    }),

    # 5 — Jean-Nicolas Bouilly
    ("jean-nicolas-bouilly", {
        "summary": (
            "Jean-Nicolas Bouilly (1763–1842) was a "
            "French playwright, librettist, children's "
            "author, and Revolutionary-era official "
            "whose most enduring legacy was his 1798 "
            "libretto Léonore, ou L'amour conjugal — "
            "a drama about a woman who disguises "
            "herself as a man to rescue her unjustly "
            "imprisoned husband — which became "
            "the source text for Beethoven's "
            "opera Fidelio (1805/1814), one of "
            "the most celebrated works in the "
            "operatic canon. The same story was "
            "also set by Pierre Gaveaux (1798) "
            "and Fernando Paër (1804).\n\n"
            "Bouilly claimed the story was based "
            "on a true incident from his time "
            "as an official in the Tours region "
            "during the Terror (1793–1794), when "
            "a wife's heroic intervention freed "
            "her husband from a revolutionary "
            "tribunal's unjust imprisonment — "
            "though historians have been unable "
            "to verify the specific case. Whether "
            "true or invented, the story encapsulated "
            "the Revolutionary ideal of heroic "
            "conjugal loyalty triumphing over "
            "political tyranny.\n\n"
            "His broader literary career included "
            "extensive children's writing — "
            "his Contes moraux et nouvelles (1802) "
            "and similar collections were "
            "widely read and translated, "
            "contributing to the 19th-century "
            "development of moral didactic "
            "children's literature in France.\n\n"
            "His political career during the "
            "Revolution included service as "
            "a civil administrator in the "
            "Indre-et-Loire department, "
            "where his claimed story of "
            "heroic conjugal rescue "
            "reportedly originated."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French playwright; wrote Léonore, ou L'amour conjugal (1798) — the source libretto for Beethoven's Fidelio (1805/1814), one of opera's most celebrated works; also set by Gaveaux and Paër; French Revolutionary-era administrator; prolific children's author; his single libretto's connection to Beethoven secured his place in cultural history despite the modest scale of his other literary output.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Revolutionary Terror's culture of arbitrary imprisonment and denunciation — which created genuine human stories of heroic intervention, resistance, and family loyalty amid political persecution — provided both the claimed real-world incident and the emotional framework that made Bouilly's story of conjugal rescue compelling to Revolutionary and post-Revolutionary audiences",
            "The early 19th-century opera world's appetite for heroic, politically resonant narratives — particularly stories of liberty, tyranny, and human courage — made Bouilly's libretto attractive to multiple composers; its theme of the individual's resistance to political tyranny had obvious resonance in the Napoleonic era",
            "Beethoven's unique artistic ambition — his desire to create a heroic opera that expressed the ideals of human freedom, conjugal devotion, and resistance to tyranny — found its perfect vehicle in Bouilly's story, and Beethoven's three revisions of the opera (1805, 1806, 1814) transformed it from a competent rescue opera into one of the canonical works of the repertoire"
        ],
        "effects": [
            "His Léonore libretto provided the source text for Beethoven's Fidelio — ensuring that his story of heroic conjugal rescue became permanently embedded in the operatic canon as the narrative vehicle for one of Beethoven's greatest works, performed in major opera houses continuously since its premiere",
            "His multiple-composer setting contributed to the early 19th-century rescue opera genre — Gaveaux's (1798), Paër's (1804), and Beethoven's (1805/1814) settings of his story making Léonore the most multiply-set dramatic narrative of the period and establishing the rescue opera as a major 19th-century operatic form",
            "His children's writing contributed to the development of moral didactic children's literature in France — his Contes moraux collections being widely read and translated, contributing to the 19th-century tradition of instructional fiction for young readers",
            "His claimed origin story of a real rescue during the Terror — whether historically accurate or not — contributed to the Revolutionary narrative tradition in which individual heroism and conjugal love were positioned as the moral counter-forces to political tyranny, a narrative framework that resonated deeply with post-Thermidor audiences seeking to process the Terror's moral legacy"
        ],
        "relationships": [
            {"entity": "Léonore, ou L'amour conjugal (libretto, 1798) — source of Beethoven's Fidelio", "relationship": "AUTHOR_OF", "note": "Wrote Léonore, ou L'amour conjugal (1798) — the source libretto that became the basis for Beethoven's Fidelio (1805/1814), one of the most celebrated operas in the canon"},
            {"entity": "Beethoven's Fidelio (1805/1814, based on Bouilly's libretto)", "relationship": "LIBRETTO_SOURCE_FOR", "note": "His Léonore libretto was the source text for Beethoven's Fidelio — the composer's only opera, whose three revisions (1805, 1806, 1814) transformed Bouilly's rescue opera story into a canonical work of operatic and musical history"},
            {"entity": "French Revolutionary Terror / Indre-et-Loire civil administration (claimed rescue incident)", "relationship": "ADMINISTRATOR_WHO_CLAIMED_SOURCE_STORY_FROM", "note": "Served as a civil administrator in Indre-et-Loire during the Terror — claiming that a real incident of conjugal rescue he witnessed inspired the Léonore story, though historians have not verified the specific case"},
            {"entity": "Rescue opera genre (early 19th-century, Gaveaux, Paër, Beethoven settings)", "relationship": "FOUNDATIONAL_LIBRETTIST_OF", "note": "Provided the foundational narrative for the early 19th-century rescue opera genre — his Léonore story being set three times (Gaveaux 1798, Paër 1804, Beethoven 1805/1814)"},
            {"entity": "French children's literature / moral didactic fiction (Contes moraux)", "relationship": "CONTRIBUTOR_TO", "note": "A prolific contributor to 19th-century French children's literature — his Contes moraux and similar collections contributing to the moral didactic children's fiction tradition"}
        ]
    }),

    # 6 — Nathaniel P. Tallmadge
    ("nathaniel-p-tallmadge", {
        "summary": (
            "Nathaniel P. Tallmadge (1795–1864) was a "
            "New York lawyer and politician who served "
            "as a US Senator from New York "
            "(1833–1844) and as the 3rd Governor "
            "of the Wisconsin Territory (1844–1845). "
            "Originally a Jacksonian Democrat who "
            "won his Senate seat with Democratic "
            "support, he broke with the party "
            "during the presidency of Martin Van "
            "Buren — opposing the Independent "
            "Treasury proposal and aligning "
            "with the conservative Democrats "
            "who eventually became Whigs.\n\n"
            "His most significant Senate contribution "
            "came during the Bank War debates: "
            "he was among the most vocal "
            "Democratic senators who opposed "
            "Van Buren's Independent Treasury "
            "scheme — which would have divorced "
            "the federal government from all "
            "banks and required government "
            "revenues to be held in hard "
            "currency — arguing that the "
            "proposal was economically "
            "dangerous and politically "
            "destructive to the Democratic Party.\n\n"
            "After leaving the Senate, his "
            "appointment as Wisconsin Territory "
            "Governor represented a transition "
            "from national politics to frontier "
            "administration — though the "
            "territory had not yet achieved "
            "statehood (Wisconsin was admitted "
            "in 1848). He later became a "
            "committed Spiritualist, writing "
            "extensively on spirit communication "
            "and serving as a prominent "
            "advocate of the movement in "
            "the 1850s–60s.\n\n"
            "His career traced the fracturing "
            "of Jacksonian Democracy as "
            "economic policy debates "
            "split its coalition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "US Senator from New York (1833–1844); 3rd Governor of Wisconsin Territory (1844–1845); Jacksonian Democrat who broke with Van Buren over the Independent Treasury; became a Whig; later a prominent American Spiritualist; his career traced the fracturing of Jacksonian Democracy as economic policy divided its coalition between hard-money Democrats and bank-friendly conservatives.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Jacksonian Democracy coalition's economic fractures — particularly the debate over the Independent Treasury scheme that would have divorced the federal government from all banks — created the political crisis in which Tallmadge was among the most prominent Democratic senators who broke with Van Buren's economic program",
            "New York's competitive Democratic politics and the state's position as the center of Jacksonian political organization — requiring senators who could navigate the competing factions within the Democratic coalition — created the political environment from which Tallmadge emerged as a Senate voice",
            "The Wisconsin Territory's frontier administrative needs — as the territory was developing its governmental infrastructure in preparation for eventual statehood — created the gubernatorial post that represented a transition from Tallmadge's national political career to regional administrative service"
        ],
        "effects": [
            "His Senate opposition to the Independent Treasury contributed to the conservative Democratic fracture that weakened Van Buren's presidency — the breaking away of conservative and bank-friendly Democrats who could not accept hard-money fiscal policy and who eventually drifted toward the Whig Party",
            "His Wisconsin Territory governorship contributed to the territorial development of what would become a key Midwestern state — administering the territory during its pre-statehood period as Wisconsin built the institutions that would govern it after admission in 1848",
            "His later Spiritualist advocacy contributed to the development of the American Spiritualism movement in the 1850s–1860s — when the movement attracted significant middle-class participation and generated extensive public debate about the possibility of communication with the dead",
            "His career trajectory — from Jacksonian Democrat to conservative anti-Independent Treasury dissenter to Whig to Spiritualist — illustrated the fluidity of American political identity in the Jacksonian era, when party alignments were being reshuffled by economic policy debates"
        ],
        "relationships": [
            {"entity": "US Senate from New York (Jacksonian Democrat then Whig, 1833–1844)", "relationship": "SENATOR", "note": "Served as US Senator from New York (1833–1844) — originally a Jacksonian Democrat who broke with Van Buren over the Independent Treasury and aligned with conservative Democrats turned Whigs"},
            {"entity": "Independent Treasury debate / Martin Van Buren administration", "relationship": "VOCAL_OPPONENT_IN_SENATE_OF", "note": "Among the most vocal Democratic Senate opponents of Van Buren's Independent Treasury scheme — his opposition contributing to the conservative Democratic fracture that weakened Van Buren's presidency"},
            {"entity": "3rd Governor of Wisconsin Territory (1844–1845)", "relationship": "TERRITORIAL_GOVERNOR", "note": "Served as 3rd Governor of the Wisconsin Territory (1844–1845) — administering the pre-statehood territory as it built institutions toward eventual admission as a state in 1848"},
            {"entity": "American Spiritualism movement (prominent advocate, 1850s–1860s)", "relationship": "PROMINENT_ADVOCATE_OF", "note": "Became a committed and prominent advocate of American Spiritualism in the 1850s–1860s — writing extensively on spirit communication and contributing to the movement's middle-class respectability"},
            {"entity": "Jacksonian Democracy / conservative Democratic fracture (Bank War era)", "relationship": "REPRESENTATIVE_FIGURE_OF_FRACTURE_IN", "note": "A representative figure of the conservative Democratic fracture during the Bank War era — his break with Van Buren illustrating the economic policy divisions that eventually split the Jacksonian coalition"}
        ]
    }),

    # 7 — John Milledge
    ("john-milledge", {
        "summary": (
            "John Milledge (1757–1818) was a Georgia "
            "planter, Revolutionary War veteran, "
            "and statesman who served as a US "
            "Representative (1792–1802, with intervals), "
            "as the 26th Governor of Georgia "
            "(1802–1806), and as a US Senator "
            "(1806–1809), briefly serving as "
            "Senate President pro tempore in 1809. "
            "Born in Savannah, he was raised in "
            "colonial Georgia's planter culture "
            "and participated in the Revolutionary "
            "War as an active Georgia patriot "
            "before building his post-war "
            "political career.\n\n"
            "His most enduring legacy was the "
            "founding of Athens, Georgia, and "
            "the University of Georgia: in 1801, "
            "as Governor-elect (before his formal "
            "inauguration), he donated the land "
            "on which the University of Georgia "
            "would be built — the tract on the "
            "Oconee River that became the campus "
            "of the nation's first state-chartered "
            "university. The city of Athens, "
            "Georgia grew around this campus "
            "and is named for the ancient "
            "Greek cultural center.\n\n"
            "His governorship focused on Georgia's "
            "rapid territorial expansion — the "
            "state was acquiring vast new lands "
            "from Native American tribes during "
            "this period — and on building "
            "the institutional infrastructure "
            "of an expanding frontier state. "
            "He subsequently served in the "
            "US Senate before declining health "
            "led him to resign.\n\n"
            "Milledgeville, Georgia — which "
            "served as the state capital from "
            "1804 to 1868 — was named in "
            "his honor, further cementing "
            "his place in Georgia's "
            "geographic and institutional history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "26th Governor of Georgia (1802–1806); US Representative (multiple terms); US Senator (1806–1809); Senate President pro tempore (1809); co-founder of Athens, Georgia and the University of Georgia (donated the founding land grant); Revolutionary War veteran; Milledgeville, Georgia (state capital 1804–1868) named in his honor; his land grant for UGA made him one of American higher education's most consequential patrons.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's rapid post-Revolutionary territorial expansion — with the state acquiring vast new lands from Native American tribes and requiring new governmental institutions for the expanding population — created the political context for Milledge's governorship and his focus on building Georgia's institutional infrastructure",
            "The early American movement to establish state universities and public higher education — in which Georgia had chartered the first state university (1785) but needed a permanent campus — created the opportunity for Milledge's land donation that provided the University of Georgia with its founding campus",
            "Milledge's personal wealth and his position as Georgia's governor-elect gave him both the resources and the civic prestige to make the significant land donation that established the University of Georgia campus — an act of philanthropy that combined personal wealth with political vision"
        ],
        "effects": [
            "His land donation in 1801 for the University of Georgia campus contributed to the establishment of the nation's first state-chartered university on a permanent site — a founding act that shaped American higher education's public university tradition and created one of the South's major research universities",
            "The founding of Athens, Georgia — the city that grew around the University campus he helped establish — contributed to the creation of one of the South's most significant university towns, which would become a major cultural and educational center",
            "Milledgeville's naming in his honor — as Georgia's state capital from 1804 to 1868 — gave him a lasting geographic memorial and reflected his contemporaries' recognition of his contributions to the state's institutional development",
            "His multiple terms in Congress and his governorship contributed to Georgia's representation and governance during the critical decades of the early republic — managing the state's territorial expansion, institutional development, and navigation of the national political conflicts of the Jefferson and Madison eras"
        ],
        "relationships": [
            {"entity": "26th Governor of Georgia (1802–1806)", "relationship": "GOVERNOR", "note": "Served as Georgia's 26th Governor (1802–1806) — managing the state's rapid territorial expansion and institutional development during a critical period of early American frontier growth"},
            {"entity": "University of Georgia (co-founder, donated founding campus land, 1801)", "relationship": "CO-FOUNDER_AND_LAND_DONOR", "note": "Donated the land on the Oconee River that became the University of Georgia campus in 1801 — a founding act that established the nation's first state-chartered university on a permanent site"},
            {"entity": "Athens, Georgia (founded around UGA campus named for Greek cultural center)", "relationship": "FOUNDING_CONTRIBUTOR_TO", "note": "Contributed to the founding of Athens, Georgia — the university town that grew around the campus he helped establish, becoming one of the South's major cultural and educational centers"},
            {"entity": "US Senate from Georgia (1806–1809) / Senate President pro tempore (1809)", "relationship": "SENATOR_AND_PRESIDENT_PRO_TEMPORE", "note": "Served as US Senator from Georgia (1806–1809) and briefly as Senate President pro tempore — contributing to Georgia's national representation before declining health forced his resignation"},
            {"entity": "Milledgeville, Georgia (state capital 1804–1868, named in his honor)", "relationship": "NAMESAKE_OF", "note": "The city of Milledgeville — Georgia's state capital from 1804 to 1868 — was named in his honor, one of the state's most significant geographic memorials to his contributions"}
        ]
    }),

    # 8 — Samuel Dexter
    ("samuel-dexter", {
        "summary": (
            "Samuel Dexter (1761–1816) was a Massachusetts "
            "lawyer and statesman who served in both "
            "houses of Congress, as Secretary of War "
            "(1800) and Secretary of the Treasury "
            "(1801) under President John Adams, and "
            "briefly continued as Treasury Secretary "
            "under President Thomas Jefferson — making "
            "him one of the few officials to serve "
            "in the cabinets of both the Federalist "
            "Adams and the Democratic-Republican "
            "Jefferson. A Harvard graduate (1781) "
            "and Boston attorney, he was one of "
            "Massachusetts's most distinguished "
            "lawyers of the early republic.\n\n"
            "His congressional career included "
            "service as US Representative (1793–1795) "
            "and US Senator (1799–1800) from "
            "Massachusetts — representing the "
            "Massachusetts Federalist tradition "
            "in the most competitive decade "
            "of the party's national dominance. "
            "His Senate term was cut short by "
            "Adams's appointment of him to "
            "the War Department.\n\n"
            "His cabinet service came during "
            "the chaotic final year of the "
            "Adams administration — the XYZ "
            "Affair's aftermath, the Quasi-War "
            "with France, and the partisan "
            "battles of the 1800 election "
            "that brought Jefferson to power. "
            "Adams's appointment of him as "
            "Treasury Secretary near the end "
            "of the administration, and "
            "Jefferson's decision to retain "
            "him briefly, reflected Dexter's "
            "reputation for competence and "
            "relative non-partisanship.\n\n"
            "After leaving federal office, "
            "he returned to Boston's legal "
            "practice and argued several "
            "significant early Supreme "
            "Court cases — his legal career "
            "outlasting his political one."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts US Representative (1793–1795) and Senator (1799–1800); Secretary of War under Adams (1800); Secretary of the Treasury under Adams and briefly under Jefferson (1801) — one of the few officials to serve in both Federalist and Democratic-Republican administrations; Harvard 1781; distinguished Boston lawyer who argued significant early Supreme Court cases; his bi-partisan retention illustrated the early republic's pragmatic approach to administrative expertise.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Adams administration's need for capable and relatively non-partisan cabinet officers during the chaotic final year of Federalist rule — with the Quasi-War, the XYZ Affair's political aftermath, and the 1800 election crisis all demanding competent executive management — created the demand for officials like Dexter who were respected for legal and administrative ability beyond partisan loyalty",
            "Massachusetts's Federalist political tradition — rooted in Harvard, Boston's commercial elite, and New England's conservative legal culture — created the political identity and professional network from which Dexter emerged as one of the state's most distinguished lawyers and politicians",
            "Jefferson's decision to retain Dexter as Treasury Secretary briefly during the transition reflected the practical need for administrative continuity — and Dexter's reputation for competence over partisan zeal made him acceptable to the Democratic-Republicans, at least temporarily, in a way that more ideological Federalists would not have been"
        ],
        "effects": [
            "His bi-partisan cabinet service — serving both Adams and Jefferson — contributed to the early republic's precedent of valuing administrative competence alongside political loyalty in executive appointments, illustrating a pragmatic approach to government that later partisan intensification would reduce",
            "His War Department service during the Quasi-War contributed to the management of the United States' first undeclared naval conflict — the naval war with France (1798–1800) that tested the early republic's military capacity and diplomatic strategy",
            "His Treasury Department service during the administration transition contributed to the fiscal management of one of the most consequential political moments in American history — the peaceful transfer of power from Federalists to Democratic-Republicans that set a critical constitutional precedent",
            "His post-cabinet Supreme Court legal practice contributed to the development of American constitutional and commercial law — his arguments in significant early Supreme Court cases extending his public contribution beyond his political career into the legal foundations of the early republic"
        ],
        "relationships": [
            {"entity": "Secretary of War and Secretary of the Treasury (Adams administration, 1800–1801)", "relationship": "SECRETARY_OF_WAR_THEN_TREASURY", "note": "Served as Adams's Secretary of War (1800) then Secretary of the Treasury (1801) — two cabinet positions in the final year of the Federalist administration"},
            {"entity": "Secretary of the Treasury retained briefly by Jefferson (1801, bi-partisan service)", "relationship": "BRIEFLY_RETAINED_BY_AS_TREASURY_SECRETARY", "note": "Briefly retained as Treasury Secretary by Jefferson after Adams's departure — one of the few Federalists to serve in both administrations, reflecting his reputation for competence over partisanship"},
            {"entity": "US House and Senate from Massachusetts (Representative 1793–1795, Senator 1799–1800)", "relationship": "CONGRESSMAN_AND_SENATOR", "note": "Served as US Representative (1793–1795) and Senator (1799–1800) from Massachusetts — representing the Massachusetts Federalist tradition before cabinet appointments cut short his Senate term"},
            {"entity": "Quasi-War with France (1798–1800) / Adams foreign and military policy", "relationship": "WAR_SECRETARY_DURING", "note": "Served as War Secretary during the Quasi-War with France — the undeclared naval conflict that was the Adams administration's most significant military challenge"},
            {"entity": "Harvard College (1781 graduate) / Boston legal community", "relationship": "GRADUATE_AND_DISTINGUISHED_MEMBER_OF", "note": "Harvard graduate (1781) and leading member of Boston's legal community — his legal career spanning congressional, cabinet, and Supreme Court practice and outlasting his political career"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 47)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
