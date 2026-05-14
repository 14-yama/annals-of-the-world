#!/usr/bin/env python3
"""
Batch 64 — 8 entities: Lewis R. Morris, Paul Hentzner, Solomon Sibley,
Jean-Charles Gervaise de Latouche, Friedrich Christian August Hasse,
Georg Adam Struve, Henry Marie Brackenridge, Théophile Berlier
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

    ("lewis-r-morris", {
        "summary": (
            "Lewis Robert Morris (1760–1825) "
            "was an American Federalist politician "
            "from Vermont who served in the "
            "U.S. House of Representatives "
            "(1797–1803) during the tumultuous "
            "years of the Adams and early "
            "Jefferson administrations. "
            "He was a nephew of Gouverneur "
            "Morris — the Constitutional "
            "Convention delegate who "
            "drafted the final language "
            "of the U.S. Constitution "
            "and one of the most colorful "
            "figures of the Founding era.\n\n"
            "Lewis Morris served during "
            "the most politically charged "
            "years of the early republic: "
            "the Quasi-War with France, "
            "the XYZ Affair, the Alien "
            "and Sedition Acts, the "
            "political crisis of 1798–1800, "
            "and the 'Revolution of 1800' "
            "that brought Jefferson to power.\n\n"
            "He was also one of the "
            "House members involved in "
            "the famous Electoral College "
            "deadlock of 1800 — the "
            "tie between Jefferson and "
            "Burr that sent the election "
            "to the House, where 36 "
            "ballots were required before "
            "Jefferson was finally chosen.\n\n"
            "Vermont in this period "
            "was one of the more "
            "reliably Federalist New "
            "England states, and "
            "Lewis Morris represented "
            "that tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Federalist Congressman (1797–1803); nephew of Gouverneur Morris; served through the Quasi-War, Alien and Sedition Acts, and the 1800 Jefferson-Burr Electoral College deadlock; represented Vermont's Federalist tradition during the party's final years of national power.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Federalist political tradition — the state's New England commercial culture, its Congregationalist religious heritage, and its distrust of French revolutionary radicalism — created the political constituency for Morris's Federalist congressional service",
            "The Morris family's prominent role in American politics — Gouverneur Morris's Constitutional Convention leadership and his subsequent diplomacy — provided Lewis with the family connections and social prominence that supported his political career",
            "The 1800 electoral crisis — the Jefferson-Burr tie in the Electoral College that sent the decision to the House of Representatives — placed Lewis Morris in one of the most dramatic moments in American electoral history, when Federalist House members had to decide whether to accept Jefferson or continue backing Burr"
        ],
        "effects": [
            "His House participation in the 1800 Electoral College deadlock resolution — one of 36 House ballots before Jefferson was chosen — contributed to one of the most consequential decisions in American electoral history",
            "His congressional service contributed to the Federalist caucus's management of the Adams administration's controversial foreign and domestic policy — the Quasi-War, the Army expansion, and the Alien and Sedition Acts",
            "His defeat in 1803 — as Jeffersonian Democratic-Republicans swept Federalists out of Congress across the North — illustrated the scale of the political transformation that the Revolution of 1800 produced",
            "His family connection to Gouverneur Morris linked Vermont's congressional representation to the Constitutional Convention's intellectual legacy — one of the several family networks that connected the founding generation's achievements to the next generation's political careers"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1797–1803"},
            {"target": "gouverneur-morris", "verb": "NEPHEW_OF", "note": "Nephew of the Constitutional Convention drafter"},
            {"target": "election-of-1800", "verb": "VOTES_IN", "note": "House member during the Jefferson-Burr deadlock"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Vermont Federalist congressman"},
            {"target": "alien-and-sedition-acts", "verb": "SERVES_DURING", "note": "In Congress during the controversial acts' passage"}
        ]
    }),

    ("paul-hentzner", {
        "summary": (
            "Paul Hentzner (1558–1623) was a "
            "German jurist and humanist scholar "
            "who is best known today for his "
            "'Itinerarium' (1598) — a Latin "
            "travel account of his journey "
            "through Europe including England, "
            "which contains one of the most "
            "vivid contemporary descriptions "
            "of Queen Elizabeth I and the "
            "English court. His observation "
            "of the aged queen at Greenwich "
            "in 1598 — describing her white "
            "complexion, her red wig, her "
            "decaying teeth, and her elaborate "
            "ceremonial magnificence — became "
            "one of the most-quoted primary "
            "sources for Elizabethan court culture.\n\n"
            "Hentzner was a Silesian jurist "
            "from Crossen who traveled "
            "through France, Italy, England, "
            "and other European countries "
            "as tutor to a young Silesian "
            "nobleman. His 'Itinerarium' "
            "recorded his observations "
            "with the precision and curiosity "
            "of a trained humanist scholar.\n\n"
            "Beyond his England observations, "
            "the 'Itinerarium' provided "
            "valuable descriptions of "
            "other European courts and "
            "cities — Venice, Paris, "
            "the German states — "
            "making it a significant "
            "document of late Renaissance "
            "European travel literature.\n\n"
            "His account was later translated "
            "and republished by Horace Walpole."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "German humanist jurist whose 'Itinerarium' (1598) contains the most vivid contemporary description of Queen Elizabeth I; key primary source for Elizabethan court culture; his observation of the aged queen at Greenwich became one of the most-quoted documents in Tudor scholarship; Horace Walpole later translated and republished his account.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The humanist tradition of learned European travel — in which educated scholars accompanied young noblemen on educational tours of European courts and cities, recording their observations in Latin travel accounts — created the genre within which Hentzner's 'Itinerarium' appeared",
            "Elizabeth I's elaborate ceremonial court culture — the Elizabethan court's theatrical display of royal magnificence, the queen's carefully managed public image, and the ceremonial grandeur that greeted foreign visitors — provided Hentzner the spectacular subject matter for his most famous observations",
            "The European humanist republic of letters — the network of learned men who communicated in Latin, shared intellectual interests across national boundaries, and valued the precise observation and recording of both classical texts and contemporary phenomena — provided the audience and purpose for Hentzner's travel account"
        ],
        "effects": [
            "His 'Itinerarium' provided one of the most valuable primary source descriptions of Elizabeth I in her final years — the 1598 portrait of the aging queen at Greenwich became indispensable to historians of Tudor England and Elizabethan court culture",
            "His travel account contributed to the tradition of humanist European travel literature — the genre of learned observation that informed educated European readers about foreign courts, cities, and customs",
            "Horace Walpole's eighteenth-century translation and republication of the 'Itinerarium' — part of Walpole's Strawberry Hill Press's antiquarian publishing program — ensured that Hentzner's account reached a much wider English readership and became part of the canon of Tudor historical sources",
            "His description of Elizabethan England — its court ceremonies, its theatrical performances, the Tower of London, the tennis courts at Windsor — provided a uniquely detailed foreign observer's account that complements English sources of the period"
        ],
        "relationships": [
            {"target": "itinerarium-1598", "verb": "WRITES", "note": "Author of the famous European travel account"},
            {"target": "elizabeth-i-england", "verb": "OBSERVES", "note": "Described the queen at Greenwich in 1598"},
            {"target": "elizabethan-court", "verb": "DESCRIBES", "note": "Key primary source for Elizabethan court culture"},
            {"target": "horace-walpole", "verb": "TRANSLATED_BY", "note": "Walpole translated and published his account in English"},
            {"target": "humanist-travel-literature", "verb": "CONTRIBUTES_TO", "note": "Part of the European humanist travel writing tradition"}
        ]
    }),

    ("solomon-sibley", {
        "summary": (
            "Solomon Sibley (1769–1846) was "
            "an American lawyer, judge, and "
            "politician who was one of the "
            "founding fathers of Michigan. "
            "As one of the first residents "
            "of Detroit after American control, "
            "he helped build the legal and "
            "political institutions of the "
            "Michigan Territory — serving "
            "as a U.S. Representative "
            "from the Territory of Michigan "
            "(1820–1823) and as a justice "
            "of the Michigan Territorial "
            "Supreme Court.\n\n"
            "Sibley arrived in Detroit in "
            "1797 — just a few years after "
            "the Jay Treaty's implementation "
            "finally compelled the British "
            "to withdraw from Detroit "
            "(which they had illegally "
            "held since 1796) and established "
            "American control over the "
            "Northwest Territory. He became "
            "one of the first American "
            "lawyers to practice in Detroit.\n\n"
            "His long legal career — from "
            "the territorial period through "
            "Michigan's statehood (1837) "
            "— made him one of the "
            "most important figures in "
            "the development of Michigan's "
            "legal and political culture. "
            "He served as Detroit's first "
            "American mayor (1806) and "
            "contributed to virtually "
            "every aspect of the city's "
            "institutional development.\n\n"
            "He is one of Michigan's "
            "true founding figures."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Michigan Territory founding figure; Detroit's first American lawyer (1797) and first American mayor (1806); Michigan Territorial Supreme Court Justice; U.S. Representative for Michigan Territory (1820–1823); helped build Michigan's legal and political institutions from the ground up through statehood.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Jay Treaty's implementation (1796) — which finally compelled British withdrawal from Detroit (held illegally since the 1783 Treaty of Paris) and established American control over the Northwest Territory — created the opportunity for American lawyers like Sibley to establish themselves in the newly American city",
            "The Northwest Ordinance (1787) and its promise of eventual statehood for the territories — which created the legal and institutional framework for the gradual development of self-governance in the old Northwest — provided the constitutional structure within which Sibley's territorial legal and political career developed",
            "The enormous practical need for lawyers in frontier territories — where land claims, commercial transactions, criminal cases, and civil disputes all required legal resolution and where there were almost no trained lawyers initially — gave Sibley's legal skills a value and influence that translated into political leadership"
        ],
        "effects": [
            "His Detroit legal practice — as the city's first American lawyer — contributed to the development of Michigan's legal tradition and the establishment of American common law in a territory that had previously operated under French and then British colonial law",
            "His service as Detroit's first American mayor (1806) contributed to the development of urban governance in one of the frontier West's most strategically important cities",
            "His Territorial Congress service contributed Michigan's perspective to the House of Representatives during the critical years of Missouri Crisis and Era of Good Feelings — representing a frontier territory that was building its institutions toward eventual statehood",
            "His Supreme Court service contributed to the development of Michigan's jurisprudence — establishing legal precedents and judicial culture that Michigan's new state courts built upon when Michigan achieved statehood in 1837"
        ],
        "relationships": [
            {"target": "michigan-territory", "verb": "SERVES_IN", "note": "U.S. Representative for Michigan Territory 1820–1823"},
            {"target": "detroit", "verb": "GOVERNS", "note": "First American mayor of Detroit 1806"},
            {"target": "michigan-supreme-court", "verb": "SERVES_ON", "note": "Michigan Territorial Supreme Court Justice"},
            {"target": "northwest-territory", "verb": "SETTLES", "note": "One of the first American lawyers in Detroit from 1797"},
            {"target": "jay-treaty", "verb": "ARRIVES_AFTER", "note": "Came to Detroit after British withdrawal under Jay Treaty"}
        ]
    }),

    ("jean-charles-gervaise-de-latouche", {
        "summary": (
            "Jean-Charles Gervaise de Latouche "
            "(1715–1782) was a French writer "
            "and libertine novelist who is "
            "best known today as the author "
            "of 'Dom Bougre, portier des Chartreux' "
            "(c. 1741) — one of the most "
            "notorious erotic novels of "
            "eighteenth-century France. "
            "Published clandestinely and "
            "immediately banned, it was "
            "one of the most widely "
            "circulated underground "
            "books of the French Enlightenment "
            "era — part of the vast "
            "trade in 'livres philosophiques' "
            "and pornographic literature "
            "that the clandestine book "
            "trade supplied to an "
            "eager reading public.\n\n"
            "De Latouche wrote under "
            "the shadow of the Ancien "
            "Régime's censorship system "
            "— the royal permission "
            "required to publish, the "
            "book police, and the Bastille "
            "as the ultimate sanction "
            "for unauthorized publications. "
            "Clandestine erotic literature "
            "served both as entertainment "
            "and as a vehicle for social "
            "satire — often attacking "
            "the Church, the aristocracy, "
            "and royal power under "
            "the cover of sexual content.\n\n"
            "His novel remained in "
            "circulation throughout "
            "the eighteenth century "
            "and beyond, becoming "
            "a canonical text of "
            "Enlightenment-era libertine literature.\n\n"
            "He also wrote plays and "
            "other literary works."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French libertine novelist and author of 'Dom Bougre, portier des Chartreux' (c.1741) — one of the most notorious and widely circulated erotic novels of eighteenth-century France; part of the clandestine Enlightenment-era book trade that used sexual content as a vehicle for social satire and anticlericalism.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Ancien Régime's censorship system — the royal permission required to publish legal books, the book police's enforcement, and the Bastille's ultimate sanction — created the conditions for the vast clandestine trade in banned books that De Latouche's novel entered",
            "The Enlightenment's challenge to traditional religious and social authority — the philosophical movement that questioned church doctrine, royal absolutism, and aristocratic privilege — used clandestine libertine literature as a vehicle for social satire, anticlerical attack, and philosophical materialism",
            "The French reading public's enormous appetite for clandestine literature — the growing literate population's demand for books that the royal censorship prohibited — created the commercial market that sustained the clandestine book trade and made De Latouche's novel a commercial success despite its illegality"
        ],
        "effects": [
            "His novel's wide clandestine circulation — across France and throughout Europe — contributed to the Enlightenment's challenge to religious authority, presenting a profoundly anticlerical satire through the vehicle of erotic fiction",
            "His contribution to the genre of French libertine literature — the tradition that would culminate in the Marquis de Sade's radical philosophical pornography — placed him in the lineage of writers who used sexual transgression as a vehicle for philosophical and social challenge",
            "The novel's continued republication through the eighteenth century — surviving censorship and seizures to remain in circulation — demonstrated the limits of the Ancien Régime's censorship system and contributed to the undermining of religious and royal authority",
            "His work contributed to the history of censorship and freedom of expression — the tension between Ancien Régime control of printed material and the reading public's demand for banned books that the clandestine trade mediated"
        ],
        "relationships": [
            {"target": "dom-bougre-portier-des-chartreux", "verb": "WRITES", "note": "Author of the notorious erotic novel c.1741"},
            {"target": "french-clandestine-book-trade", "verb": "CONTRIBUTES_TO", "note": "Part of the Enlightenment-era underground publishing"},
            {"target": "ancien-regime-censorship", "verb": "EVADES", "note": "Published banned works under royal censorship"},
            {"target": "french-libertine-literature", "verb": "PART_OF", "note": "Eighteenth-century French libertine literary tradition"},
            {"target": "french-enlightenment", "verb": "PARTICIPATES_IN", "note": "Used erotic fiction as vehicle for anticlerical satire"}
        ]
    }),

    ("friedrich-christian-august-hasse", {
        "summary": (
            "Friedrich Christian August Hasse "
            "(1773–1848) was a German theologian, "
            "church historian, and professor "
            "at the University of Leipzig "
            "who made significant contributions "
            "to the history of medieval "
            "theology and the study of "
            "Anselm of Canterbury. His "
            "scholarly work on Anselm "
            "— particularly his biography "
            "and edition of Anselm's works "
            "— contributed to the revival "
            "of interest in medieval "
            "scholastic theology during "
            "the nineteenth century, "
            "a period when German Protestant "
            "scholars were reconsidering "
            "the medieval church's "
            "intellectual achievements.\n\n"
            "Hasse was trained in the "
            "German Protestant theological "
            "tradition at Leipzig — one "
            "of Germany's great universities "
            "and a center of Lutheran "
            "theological scholarship. "
            "His career coincided with "
            "the great transformation "
            "of German theology in "
            "the early nineteenth century "
            "— the encounter with Kantian "
            "philosophy, the rise of "
            "historical-critical biblical "
            "scholarship, and the "
            "development of systematic "
            "Protestant theology.\n\n"
            "His Anselm scholarship "
            "contributed to the critical "
            "study of medieval theology "
            "at a time when the Protestant "
            "tradition was reevaluating "
            "its relationship to "
            "pre-Reformation Christianity.\n\n"
            "He also contributed to "
            "the study of church history "
            "more broadly."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "German Protestant theologian and church historian at Leipzig; contributed to the critical study of Anselm of Canterbury and medieval scholastic theology; worked during the great transformation of German theology under Kantian influence and the rise of historical-critical scholarship.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The German Protestant theological tradition at Leipzig — the Lutheran scholarly culture that balanced confessional theology with critical historical scholarship — provided the intellectual formation for Hasse's career as both theologian and church historian",
            "The nineteenth-century German theological transformation — the encounter with Kantian philosophy, the development of historical-critical methodology, and the challenge of Schleiermacher's experiential theology — created the intellectual context in which Hasse's historical work on medieval theology occupied a distinctive place",
            "The romantic revival of interest in the medieval past — the early nineteenth century's rediscovery of medieval culture, philosophy, and theology that both romantics and confessional theologians participated in — provided the intellectual atmosphere for renewed scholarly attention to figures like Anselm"
        ],
        "effects": [
            "His Anselm scholarship contributed to the critical study of medieval theology — providing reliable biographical and textual resources for a figure whose ontological argument for God's existence and theory of atonement were of enduring philosophical and theological interest",
            "His work contributed to the Protestant theological tradition's engagement with the pre-Reformation medieval church — demonstrating that German Lutherans could study the scholastic tradition critically and find valuable resources in it",
            "His Leipzig professorship contributed to the training of the next generation of German Protestant theologians — the academic theology factory that Germany's universities were developing in the early nineteenth century",
            "His career illustrated the German academic theological tradition's commitment to historical scholarship — the distinctive combination of confessional commitment and critical historical methodology that characterized nineteenth-century German Protestant theology"
        ],
        "relationships": [
            {"target": "university-of-leipzig", "verb": "TEACHES_AT", "note": "Professor of theology at Leipzig"},
            {"target": "anselm-of-canterbury", "verb": "STUDIES", "note": "Contributed to critical scholarship on Anselm"},
            {"target": "german-protestant-theology", "verb": "CONTRIBUTES_TO", "note": "Part of the nineteenth-century German theological tradition"},
            {"target": "lutheranism", "verb": "REPRESENTS", "note": "Lutheran theological scholar at a center of Lutheran learning"},
            {"target": "medieval-scholasticism", "verb": "INVESTIGATES", "note": "Historian of medieval scholastic theology"}
        ]
    }),

    ("georg-adam-struve", {
        "summary": (
            "Georg Adam Struve (1619–1692) was "
            "a German jurist and legal scholar "
            "who served as a professor of "
            "law at the University of Jena "
            "and was one of the most prolific "
            "and influential teachers of "
            "German civil and public law "
            "in the seventeenth century. "
            "His comprehensive legal textbooks "
            "— particularly his 'Syntagma "
            "Juris Civilis' and his works "
            "on the law of the Holy Roman "
            "Empire — became standard "
            "teaching texts in German "
            "universities, shaping the "
            "legal education of generations "
            "of German lawyers and officials.\n\n"
            "Struve worked in the tradition "
            "of the usus modernus Pandectarum "
            "— the German legal school that "
            "adapted Roman law (the Pandects "
            "or Digest of Justinian) to "
            "current German legal practice, "
            "creating a practical synthesis "
            "of Roman law and German "
            "customary law that served "
            "the needs of the Holy Roman "
            "Empire's incredibly complex "
            "legal pluralism.\n\n"
            "His career at Jena coincided "
            "with the aftermath of the "
            "Thirty Years' War — the "
            "reconstruction of the "
            "Empire's legal and political "
            "order under the Peace of "
            "Westphalia's new constitutional "
            "arrangements.\n\n"
            "He was among the most "
            "important systematizers of "
            "seventeenth-century German law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "German jurist and Jena law professor whose textbooks shaped legal education across German universities; central figure in the usus modernus Pandectarum tradition adapting Roman law to German practice; prolific systematizer of seventeenth-century German civil and public law in the post-Westphalia reconstruction period.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The usus modernus Pandectarum tradition — the German legal school that synthesized Roman Pandects law with German customary practice to create a working legal system for the Holy Roman Empire's complex pluralism — provided the intellectual framework for Struve's comprehensive legal systematization",
            "The post-Thirty Years' War reconstruction of the Empire's legal order — the Peace of Westphalia's new constitutional arrangements that defined religious peace, territorial sovereignty, and imperial governance — created the political context for Struve's public law work at Jena",
            "The University of Jena's development as a major center of Protestant German legal scholarship — the university founded in 1558 that became one of the leading German legal faculties — provided Struve the institutional base for his prolific scholarly output and his influence on German legal education"
        ],
        "effects": [
            "His legal textbooks' adoption across German universities — the 'Syntagma Juris Civilis' and his other works becoming standard teaching texts — shaped the legal education of the German officials, lawyers, and judges who administered the Holy Roman Empire's courts and territories",
            "His systematization of usus modernus legal doctrine contributed to the development of German civil law as a practical synthesis of Roman and German law — a contribution to the legal tradition that German jurists built upon through the eighteenth century",
            "His public law works contributed to the constitutional jurisprudence of the Holy Roman Empire — the complex body of imperial law that governed the relations between emperor, princes, estates, and subjects in the post-Westphalia constitutional order",
            "His career at Jena contributed to the university's development as a leading German legal faculty — part of the network of German universities that trained the bureaucratic and legal elite of the Empire's many states and territories"
        ],
        "relationships": [
            {"target": "university-of-jena", "verb": "TEACHES_AT", "note": "Professor of law at Jena for decades"},
            {"target": "usus-modernus-pandectarum", "verb": "CONTRIBUTES_TO", "note": "Central figure in the German Roman-law adaptation tradition"},
            {"target": "holy-roman-empire", "verb": "SERVES", "note": "Legal scholar systematizing imperial constitutional law"},
            {"target": "peace-of-westphalia", "verb": "WORKS_AFTER", "note": "Career in post-Westphalia legal reconstruction"},
            {"target": "german-civil-law", "verb": "SYSTEMATIZES", "note": "Prolific textbook author shaping German legal education"}
        ]
    }),

    ("henry-marie-brackenridge", {
        "summary": (
            "Henry Marie Brackenridge (1786–1871) "
            "was an American lawyer, author, "
            "and diplomat — the son of Hugh "
            "Henry Brackenridge, the author "
            "of Modern Chivalry. He became "
            "notable in his own right as "
            "a writer and explorer, authoring "
            "'Views of Louisiana' (1814) "
            "— one of the first systematic "
            "accounts of the trans-Mississippi "
            "West — and 'Journal of a "
            "Voyage up the Missouri River "
            "in 1811' (1816), which recorded "
            "his journey with Manuel Lisa's "
            "fur-trading expedition and "
            "is a primary source for "
            "early Missouri River exploration.\n\n"
            "Brackenridge traveled extensively "
            "in the American West and "
            "Latin America — his 'Voyage "
            "to South America' (1820) "
            "recorded his observations "
            "of the Spanish colonial "
            "world as it was moving "
            "toward independence. He "
            "served as a secretary to "
            "the U.S. diplomatic mission "
            "to South America (1817–1818) "
            "that assessed the independence "
            "movements, and his reports "
            "contributed to the political "
            "debate over U.S. recognition "
            "of Latin American independence.\n\n"
            "His writings contributed "
            "significantly to American "
            "geographic knowledge and "
            "to the early literature "
            "of western exploration.\n\n"
            "He was also a lawyer who "
            "practiced in Louisiana and Maryland."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "American explorer-writer and son of Hugh Henry Brackenridge; author of 'Views of Louisiana' (1814) and 'Journal of a Voyage up the Missouri' (1816) — key primary sources for early trans-Mississippi exploration; diplomatic mission secretary to South America (1817–1818) whose reports contributed to U.S. Latin American recognition debates.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Louisiana Purchase (1803) and the consequent American need to understand and document the vast trans-Mississippi West — the enormous territory that Jefferson acquired from France and that American explorers, traders, and writers like Brackenridge immediately began exploring and describing — created the context for his western writings",
            "The fur trading expeditions up the Missouri River — Manuel Lisa's Missouri Fur Company that Brackenridge joined in 1811, which was pushing American commercial expansion into Native American territories — provided the direct experience for his Missouri River journal",
            "The Latin American independence movements and U.S. foreign policy debate over recognition — whether and when to recognize the new Spanish American republics — created the context for Brackenridge's diplomatic service and his influential writings on South America's political situation"
        ],
        "effects": [
            "'Views of Louisiana' (1814) and the Missouri River journal (1816) contributed to American geographic knowledge of the trans-Mississippi West — providing systematic descriptions of the landscape, Native peoples, flora, fauna, and commercial potential of territories most Americans knew nothing about",
            "His South American diplomatic service and writings contributed to the U.S. debate over recognizing Latin American independence — providing firsthand observations about the political situation that informed Monroe's eventual recognition decisions and contributed to the intellectual foundations of the Monroe Doctrine",
            "His literary career — following his famous father's — contributed to the development of American western and travel literature, the genre of exploration and discovery writing that would eventually culminate in the great nineteenth-century western narratives",
            "His career illustrated the borderland between literary production and political service in the early republic — the writer-diplomat-lawyer who contributed simultaneously to American letters, geographic knowledge, and foreign policy"
        ],
        "relationships": [
            {"target": "views-of-louisiana", "verb": "WRITES", "note": "Author of the key 1814 trans-Mississippi account"},
            {"target": "missouri-river-exploration", "verb": "CONTRIBUTES_TO", "note": "Joined Manuel Lisa's 1811 Missouri expedition"},
            {"target": "latin-american-independence", "verb": "REPORTS_ON", "note": "Diplomatic secretary observing independence movements"},
            {"target": "hugh-henry-brackenridge", "verb": "SON_OF", "note": "Son of the Modern Chivalry author"},
            {"target": "monroe-doctrine", "verb": "CONTRIBUTES_CONTEXT_TO", "note": "Reports contributed to U.S. Latin American policy debates"}
        ]
    }),

    ("théophile-berlier", {
        "summary": (
            "Théophile Berlier (1761–1844) was "
            "a French lawyer, revolutionary "
            "politician, and legal architect "
            "who played a significant role "
            "in the codification of French "
            "law under Napoleon. A member "
            "of the National Convention "
            "who survived the Terror, "
            "he served on the Council "
            "of Five Hundred and then "
            "as a member of the Council "
            "of State — Napoleon's elite "
            "legislative-judicial body "
            "— where he contributed to "
            "the drafting of the Napoleonic "
            "Code Civile (1804), the Penal "
            "Code, and other major "
            "legislative codifications "
            "that transformed French law.\n\n"
            "Berlier was born in Dijon "
            "and trained as a lawyer "
            "before the Revolution — "
            "part of the generation of "
            "provincial lawyers who "
            "entered revolutionary politics "
            "through the Third Estate "
            "and brought their legal "
            "expertise to the new republican "
            "institutions.\n\n"
            "His Council of State service "
            "placed him at the center "
            "of the most significant "
            "legal reform project in "
            "modern European history "
            "— the Napoleonic codification "
            "that replaced the chaos "
            "of regional customary laws "
            "with a unified national "
            "legal system that spread "
            "across Europe and the world.\n\n"
            "He survived the Restoration "
            "and lived to 83."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French revolutionary lawyer and Napoleon's Council of State member; contributed to drafting the Napoleonic Code Civile (1804) and the Penal Code; National Convention survivor who brought legal expertise through Revolution into Napoleonic codification; participated in the most significant legal reform project of modern European history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's destruction of the Ancien Régime legal order — the abolition of feudal law, regional customary laws, and the old parlement system — created the blank slate on which the Napoleonic codification could be written, and Berlier's Revolutionary Convention experience placed him in the generation that had both destroyed the old system and was needed to build the new",
            "Napoleon's codification project — his determination to replace France's chaotic multiplicity of regional customary laws with a unified national code — created the Council of State's drafting commission on which Berlier served alongside Portalis, Tronchet, Bigot de Préameneu, and Cambacérès",
            "The provincial lawyer class's rise to political prominence through the Revolution — the Third Estate lawyers who entered the National Assembly and subsequently took over the Republic's legal institutions — created the cadre of trained jurists who could actually draft the complex technical provisions of a comprehensive civil code"
        ],
        "effects": [
            "His contribution to the Napoleonic Code Civile (1804) — one of the most influential legal documents in history, spreading across Europe in Napoleon's wake and eventually influencing the civil law systems of Quebec, Louisiana, Latin America, and much of Asia and Africa — placed Berlier among the architects of the modern world's legal infrastructure",
            "His contribution to the Penal Code — the comprehensive criminal code that replaced the random mixture of Ancien Régime punishments with a systematic, rationalized system of proportional penalties — contributed to one of the great penal reform achievements of the Enlightenment era",
            "His survival through the Convention, Directory, Consulate, Empire, and Restoration illustrated the career adaptability of the Revolution's lawyer-politicians — those who combined revolutionary credentials with legal expertise could find a place under successive regimes",
            "His Council of State service contributed to the institutionalization of the conseil d'état as a key French governmental body — the administrative-judicial institution that reviewed legislation, advised on governance, and became one of France's most enduring constitutional organs"
        ],
        "relationships": [
            {"target": "napoleonic-code", "verb": "DRAFTS", "note": "Council of State member contributing to Code Civile 1804"},
            {"target": "conseil-detat-france", "verb": "SERVES_ON", "note": "Napoleon's Council of State legal drafter"},
            {"target": "national-convention", "verb": "SERVES_IN", "note": "Revolutionary Convention member who survived the Terror"},
            {"target": "french-penal-code", "verb": "CONTRIBUTES_TO", "note": "Contributed to the Napoleonic Penal Code drafting"},
            {"target": "jean-étienne-marie-portalis", "verb": "COLLABORATES_WITH", "note": "Fellow Council of State codification collaborator"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 64 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
