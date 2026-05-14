#!/usr/bin/env python3
"""
Batch 49 — 8 entities: Jacques-Joseph Haus, John Leeds Kerr, Jean Palaprat,
Bernard-Joseph Saurin, Louis Racine, François Just Marie Raynouard,
Paul Pálffy de Erdőd, Joachim-Jean-Xavier d'Isoard
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

    # 1 — Jacques-Joseph Haus
    ("jacques-joseph-haus", {
        "summary": (
            "Jacques-Joseph Haus (1796–1881) was "
            "a Belgian legal scholar and professor "
            "whose comprehensive treatise "
            "'Principes généraux du droit pénal belge' "
            "(2 volumes, 1869) became the foundational "
            "scientific work of Belgian criminal law — "
            "the first systematic doctrinal analysis "
            "of the Belgian Penal Code of 1867 and "
            "the standard authority for Belgian "
            "criminal law throughout the late "
            "19th century. A professor at the "
            "University of Ghent for decades, "
            "he trained the generation of Belgian "
            "lawyers and judges who built the "
            "new kingdom's legal institutions "
            "after independence in 1830.\n\n"
            "His scholarly career spanned the "
            "entire first half-century of "
            "Belgian independence — from 1830, "
            "when the Belgian revolution "
            "established a new constitutional "
            "monarchy, through the great "
            "legislative reforms of the 1860s "
            "that produced the Penal Code and "
            "the Code of Criminal Procedure. "
            "His treatise arrived at the "
            "precise moment when these "
            "codes needed doctrinal commentary "
            "to guide their application.\n\n"
            "Beyond his criminal law treatise, "
            "he also contributed to the "
            "theory of criminal procedure and "
            "the philosophical foundations "
            "of penal policy — engaging "
            "with the contemporary debates "
            "between classical and utilitarian "
            "theories of punishment that "
            "dominated 19th-century European "
            "jurisprudence. His work drew on "
            "both French legal doctrine and "
            "the German legal science of "
            "the historical school.\n\n"
            "His 85-year lifespan allowed him "
            "to witness the complete arc of "
            "Belgian legal development from "
            "the revolutionary moment of "
            "1830 to the mature constitutional "
            "order of the 1880s — making "
            "him one of the most important "
            "scholarly bridges between "
            "Belgian legal origins and "
            "its 19th-century codification."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Belgian criminal law professor at University of Ghent; author of 'Principes généraux du droit pénal belge' (1869) — the foundational scientific treatise of Belgian criminal law and authoritative commentary on the Belgian Penal Code of 1867; his scholarship bridged Belgian legal independence (1830) and the mature 19th-century codification; trained a generation of Belgian lawyers and judges.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Belgian independence (1830) and the new kingdom's need to build its own legal institutions — including a distinctive Belgian legal scholarship that could interpret the new criminal codes — created the institutional demand for systematic doctrinal treatises that Haus's career supplied through his professorship and publications",
            "The Belgian Penal Code of 1867 — a major legislative codification that required authoritative scientific commentary to guide its application by Belgian courts — created the specific scholarly opportunity that Haus's 'Principes généraux' addressed, arriving at the precise moment when the code's doctrinal framework needed systematic analysis",
            "The 19th-century European debate between classical and utilitarian theories of punishment — Beccaria's proportionality principles versus Bentham's utilitarian calculus — created the theoretical context in which Haus positioned Belgian criminal law doctrine, drawing on both French legal scholarship and German legal science"
        ],
        "effects": [
            "His 'Principes généraux du droit pénal belge' (1869) contributed to the systematic doctrinal development of Belgian criminal law — establishing the scientific framework for interpreting the Penal Code of 1867 and becoming the standard authority that Belgian lawyers, judges, and professors relied on throughout the late 19th century",
            "His University of Ghent professorship contributed to the training of a generation of Belgian legal practitioners — the lawyers, prosecutors, and judges who applied the new criminal codes in the courts of the newly independent kingdom",
            "His engagement with comparative criminal law theory contributed to Belgium's participation in the broader European jurisprudential debates of the 19th century — connecting Belgian legal scholarship to the French, German, and Italian currents of criminal law doctrine that were reshaping European penal systems",
            "His 85-year scholarly career contributed to the continuity of Belgian legal development across the full arc from revolutionary independence to mature constitutional order — making him a living institutional connection between 1830 and the legal establishment of the 1880s"
        ],
        "relationships": [
            {"entity": "'Principes généraux du droit pénal belge' (1869, foundational Belgian criminal law treatise)", "relationship": "AUTHOR_OF", "note": "Authored the 'Principes généraux du droit pénal belge' (2 volumes, 1869) — the foundational scientific treatise of Belgian criminal law and authoritative commentary on the Belgian Penal Code of 1867"},
            {"entity": "University of Ghent / Belgian legal education (professor, 19th century)", "relationship": "PROFESSOR_AT", "note": "Taught criminal law at the University of Ghent — training the generation of Belgian lawyers and judges who built the new kingdom's legal institutions after independence"},
            {"entity": "Belgian Penal Code of 1867 / Belgian legal codification", "relationship": "PRINCIPAL_SCIENTIFIC_COMMENTATOR_ON", "note": "Provided the authoritative scientific commentary on the Belgian Penal Code of 1867 — the work that gave the code its doctrinal framework for application in Belgian courts"},
            {"entity": "Belgian independence (1830) / Belgian constitutional order", "relationship": "LEGAL_SCHOLAR_OF", "note": "A legal scholar whose career spanned the entire first half-century of Belgian independence — from 1830 revolutionary moment to the mature constitutional order of the 1880s"},
            {"entity": "Classical and utilitarian penal theory / 19th-century European criminal law debate", "relationship": "CONTRIBUTOR_TO", "note": "Contributed to the 19th-century European debate between classical and utilitarian theories of punishment — positioning Belgian criminal law within the broader jurisprudential currents reshaping European penal systems"}
        ]
    }),

    # 2 — John Leeds Kerr
    ("john-leeds-kerr", {
        "summary": (
            "John Leeds Kerr (1780–1844) was a "
            "Maryland lawyer and politician who "
            "served both as a US Representative "
            "from Maryland (1823–1829, four "
            "terms in the Eighteenth through "
            "Twenty-first Congresses) and as "
            "a US Senator from Maryland "
            "(1841–1843), providing him "
            "a lengthy combined career in "
            "both houses of Congress. "
            "He also served as a Maryland "
            "state court judge between "
            "his congressional stints — "
            "a career pattern of alternating "
            "judicial and legislative "
            "service characteristic of "
            "the early American bar.\n\n"
            "His House service fell during "
            "the Era of Good Feelings' "
            "disintegration and the rise "
            "of Jacksonian Democracy — "
            "the years when the old "
            "Democratic-Republican Party "
            "fragmented into Adams-Clay "
            "National Republicans and "
            "Jackson Democrats. His Senate "
            "service fell during the Whig "
            "Party's brief ascendancy under "
            "Tyler — a turbulent period "
            "when Tyler's break with the "
            "Whigs left the party politically "
            "paralyzed in the Senate.\n\n"
            "Maryland's politics in this "
            "era were shaped by the state's "
            "unusual social geography: "
            "a slaveholding border state "
            "with both tidewater planter "
            "aristocracy and a large "
            "Baltimore commercial class "
            "— the tensions between these "
            "constituencies defining the "
            "state's congressional delegations. "
            "Kerr represented Maryland's "
            "Eastern Shore, the tidewater "
            "plantation region.\n\n"
            "His combined House and Senate "
            "service of nearly a decade gave "
            "him a perspective across both "
            "chambers of Congress during "
            "one of the most politically "
            "volatile periods of the early republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland US Representative (1823–1829, four terms); US Senator from Maryland (1841–1843); Maryland state court judge; represented Maryland's Eastern Shore tidewater planter constituency; career spanned the Era of Good Feelings, Jacksonian Democracy, and Whig ascendancy — the politically volatile decades of the 1820s–1840s.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maryland's political evolution from the Era of Good Feelings' one-party consensus through the Jacksonian realignment — the fragmentation of the Democratic-Republican party into National Republicans and Democrats — created the fluid political environment in which Kerr built his congressional career through the Eastern Shore's planter constituency",
            "The Maryland Eastern Shore's tidewater planter social structure — which produced politically conservative, slavery-defending representatives whose interests diverged from Baltimore's commercial interests — created the specific constituency that Kerr's congressional career represented across both House and Senate service",
            "The alternating pattern of judicial and legislative service characteristic of the early American bar — in which lawyers moved between court appointments and elective office depending on opportunity and political circumstances — shaped the career arc that took Kerr from Congress to the Maryland bench and back to the Senate"
        ],
        "effects": [
            "His decade of combined House and Senate service contributed to Maryland's congressional representation during three distinct political eras — the Era of Good Feelings, Jacksonian Democracy's rise, and the Whig period — providing the Eastern Shore with a consistent congressional voice across the most volatile decades of early American politics",
            "His Maryland judgeship contributed to the state's judicial system — providing professional legal adjudication in a state whose courts were navigating the tensions between tidewater planter law and the commercial law demands of Baltimore's growing economy",
            "His Senate service during the Tyler administration contributed to the political environment of a Whig Senate facing a president who had broken with the Whigs — the congressional experience of partisan fragmentation that characterized the early 1840s political crisis",
            "His career trajectory — from Maryland Eastern Shore lawyer to multiple congressional terms and state judgeship — illustrated the career pattern of the early American legal-political class that staffed both the legislative and judicial institutions of the early republic"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Maryland (1823–1829, four terms)", "relationship": "REPRESENTATIVE", "note": "Served four terms in the US House from Maryland (1823–1829) — representing the Eastern Shore tidewater constituency during the Era of Good Feelings' disintegration and Jacksonian Democracy's rise"},
            {"entity": "US Senate from Maryland (1841–1843)", "relationship": "SENATOR", "note": "Served as US Senator from Maryland (1841–1843) — during the Tyler administration's Whig crisis, providing Maryland's Senate representation during a politically turbulent period"},
            {"entity": "Maryland state court judiciary (judge between congressional terms)", "relationship": "JUDGE", "note": "Served as a Maryland state court judge between his congressional stints — the judicial service that characterized the alternating legislative-judicial career pattern of the early American bar"},
            {"entity": "Maryland Eastern Shore / tidewater planter constituency", "relationship": "REPRESENTATIVE_OF", "note": "Represented Maryland's Eastern Shore tidewater planter constituency — a socially conservative, slaveholding region whose interests diverged from Baltimore's commercial class"},
            {"entity": "Jacksonian era / Whig Party / Tyler administration political crisis", "relationship": "POLITICIAN_DURING", "note": "A politician whose career spanned the Jacksonian realignment, Whig ascendancy, and Tyler crisis — his combined House and Senate service providing a perspective across three distinct political eras"}
        ]
    }),

    # 3 — Jean Palaprat
    ("jean-palaprat", {
        "summary": (
            "Jean de Palaprat (1650–1721) was a "
            "Toulouse-born French lawyer and "
            "playwright who achieved lasting "
            "theatrical fame through his "
            "collaboration with David Augustin "
            "de Brueys — particularly for "
            "their comedy 'Le Grondeur' "
            "(The Grumbler, 1691), one of "
            "the most performed comedies "
            "of 17th and early 18th-century "
            "France and a staple of the "
            "Comédie-Française repertory "
            "well into the 18th century. "
            "Their partnership produced "
            "several successful comedies "
            "that combined precise social "
            "observation with theatrical "
            "craft.\n\n"
            "Palaprat maintained his legal "
            "career alongside his theatrical "
            "work — a dual professional life "
            "characteristic of the legal-literary "
            "culture of 17th-century France, "
            "in which the provincial bar "
            "was often a nursery of literary "
            "talent. His Toulouse origins "
            "connected him to the tradition "
            "of southern French humanism "
            "and the Académie des Jeux "
            "Floraux, the oldest literary "
            "academy in France.\n\n"
            "The Palaprat-Brueys comedies "
            "occupied a significant niche "
            "in the transition from Molière's "
            "dominance — arriving in the "
            "decade after Molière's death "
            "(1673) when the Comédie-Française "
            "was building its repertory "
            "of new French comedies to "
            "complement the Molière canon. "
            "'Le Grondeur' in particular "
            "was praised for its observation "
            "of domestic comic types — "
            "the irascible husband as "
            "social archetype — that "
            "connected it to the Molièresque "
            "tradition of character comedy.\n\n"
            "He is also associated with "
            "a mysterious episode in "
            "Languedoc occultism — his "
            "involvement with a claimed "
            "medieval manuscript purporting "
            "to document the survival of "
            "the Knights Templar — though "
            "historians consider this "
            "document a 17th-century forgery."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Toulouse lawyer and playwright; co-author (with David Augustin de Brueys) of 'Le Grondeur' (1691) — a major French comedy of the post-Molière era, a Comédie-Française staple for decades; the Palaprat-Brueys partnership filled the gap in the French comic repertory after Molière's death; also associated with a mysterious Knights Templar manuscript episode.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Molière's death in 1673 and the resulting gap in the French comic theater's repertory — the Comédie-Française needed new French comedies to complement the Molière canon — created the theatrical opportunity that Palaprat and Brueys's collaboration filled in the 1680s–1690s with a series of successful character comedies",
            "The 17th-century French legal-literary culture — in which provincial lawyers combined legal practice with literary production, using the bar's classical education and social observation as the raw material for theatrical and literary work — created the social environment from which Palaprat's dual career as lawyer and playwright emerged",
            "The post-Molière tradition of character comedy — focused on recognizable social types (the miser, the hypocrite, the grumbler) as the vehicle for both theatrical entertainment and social criticism — provided the aesthetic framework within which Palaprat and Brueys developed their comedies to fit the tastes of the Comédie-Française audience"
        ],
        "effects": [
            "His collaboration with Brueys on 'Le Grondeur' and other comedies contributed to the post-Molière French comic repertory — providing the Comédie-Française with successful new plays that could hold the stage alongside the Molière canon and attract audiences in the decades after the great playwright's death",
            "'Le Grondeur' (1691) contributed to the French theatrical tradition of domestic character comedy — the irascible husband as social archetype representing a type that recurred in French theatrical culture through the 18th century, connecting Molièresque character observation to the Enlightenment's social criticism",
            "His legal-literary career contributed to the tradition of the provincial French lawyer as literary figure — the bar-to-theater pipeline that characterized French intellectual life in the 17th and 18th centuries and produced many of the period's most significant playwrights and writers",
            "The Palaprat-Brueys theatrical partnership contributed to the Comédie-Française's institutional development in the decades after Molière — their comedies helping to establish the new theater's repertory identity and demonstrating that successful new French comedy could be written in the Molière tradition"
        ],
        "relationships": [
            {"entity": "'Le Grondeur' (The Grumbler, 1691) — major French comedy, co-authored with Brueys", "relationship": "CO-AUTHOR_OF", "note": "Co-authored 'Le Grondeur' (1691) with David Augustin de Brueys — one of the most performed comedies of post-Molière France and a long-running Comédie-Française staple"},
            {"entity": "David Augustin de Brueys (theatrical collaborator)", "relationship": "THEATRICAL_COLLABORATOR_WITH", "note": "Collaborated with David Augustin de Brueys on a series of comedies — the Palaprat-Brueys partnership filling the post-Molière gap in the French comic theater's repertory"},
            {"entity": "Comédie-Française / post-Molière French comic theater", "relationship": "PLAYWRIGHT_FOR", "note": "Wrote comedies performed at the Comédie-Française — contributing to the theater's post-Molière repertory in the decades after the great playwright's death in 1673"},
            {"entity": "Toulouse bar / provincial French legal-literary culture", "relationship": "MEMBER_OF", "note": "A Toulouse lawyer who combined legal practice with theatrical writing — characteristic of the 17th-century French legal-literary culture in which the provincial bar was a nursery of literary talent"},
            {"entity": "Knights Templar manuscript episode / Languedoc occultism (17th century forgery)", "relationship": "ASSOCIATED_WITH", "note": "Associated with a mysterious episode involving a claimed medieval manuscript purporting to document Templar survival — historians consider it a 17th-century forgery connected to Languedoc occultist traditions"}
        ]
    }),

    # 4 — Bernard-Joseph Saurin
    ("bernard-joseph-saurin", {
        "summary": (
            "Bernard-Joseph Saurin (1706–1781) "
            "was a French playwright and "
            "lawyer who achieved considerable "
            "success on the Parisian stage "
            "with a series of tragedies and "
            "dramas — most notably 'Spartacus' "
            "(1760), a tragedy on the slave "
            "rebellion leader, and 'Béverlei' "
            "(1768), a drame bourgeois "
            "adapted from Edward Moore's "
            "English 'The Gamester' (1753) — "
            "and was elected to the Académie "
            "française in 1761. The son of "
            "the Protestant theologian "
            "Joseph Saurin, he was a close "
            "friend of Voltaire, who warmly "
            "admired his work.\n\n"
            "'Béverlei' was his greatest "
            "theatrical success — a "
            "sentimental drame about a "
            "ruined gambler and the "
            "suffering of his family, "
            "translated into German by "
            "Schiller under the title "
            "'Der Spieler' and influential "
            "on the emerging genre of "
            "bourgeois domestic tragedy "
            "that shaped 18th-century "
            "German theater. 'Spartacus' "
            "(1760), performed at the "
            "Comédie-Française, dealt "
            "with the great slave "
            "rebellion leader in a "
            "way that resonated with "
            "Enlightenment discussions "
            "of freedom and tyranny.\n\n"
            "His friendship with Voltaire "
            "placed him at the center "
            "of the Parisian Enlightenment "
            "literary world — though he "
            "was a more conservative "
            "figure than Voltaire, "
            "maintaining his formal "
            "legal career alongside "
            "his theatrical writing "
            "and Académie activities.\n\n"
            "His Protestant background — "
            "son of the converted "
            "Protestant pastor Joseph "
            "Saurin — gave him a complex "
            "personal history in an era "
            "when French Protestantism "
            "remained legally marginalized "
            "despite Enlightenment pressures "
            "for toleration."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Enlightenment playwright; Académie française (elected 1761); author of 'Spartacus' (1760) and 'Béverlei' (1768, adapted from Edward Moore's English 'The Gamester') — the latter influencing Schiller and German bourgeois drama; friend of Voltaire; his 'Béverlei' contributed to the drame bourgeois genre that transformed 18th-century European theater.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 18th-century Enlightenment's transformation of theatrical aesthetics — moving from classical tragedy toward the drame bourgeois (bourgeois domestic drama) that placed ordinary families and their emotional struggles at the center of theatrical experience — created the cultural shift that made Saurin's 'Béverlei' possible and successful",
            "The European cross-cultural theatrical exchange of the 18th century — in which English plays were adapted for French and German audiences, and French plays influenced German theater — created the transmission chain through which Saurin adapted Moore's English 'The Gamester' into 'Béverlei' and which Schiller subsequently adapted into German",
            "Voltaire's Enlightenment circle — the network of Parisian writers, philosophes, and theater-makers who gathered around Voltaire — created the intellectual and social environment in which Saurin's career developed, giving him access to the most influential theatrical and literary world in 18th-century Europe"
        ],
        "effects": [
            "His 'Béverlei' (1768) contributed to the development of the drame bourgeois genre — the sentimental domestic drama that displaced neoclassical tragedy as the dominant theatrical form of the late 18th century, its influence extending through Schiller's German adaptation to the emerging tradition of bourgeois domestic theater",
            "His 'Spartacus' (1760) contributed to the Enlightenment theatrical engagement with themes of freedom, slavery, and tyranny — the Comédie-Française performance of a play about the great slave rebellion leader resonating with the philosophes' arguments about natural freedom and the illegitimacy of political despotism",
            "His Académie française membership contributed to the institutionalization of his literary reputation — his election in 1761 placing him among the recognized authorities of French letters and connecting him to the formal institution that defined literary culture in 18th-century France",
            "His friendship with Voltaire contributed to the network of Enlightenment literary connections — his relationship with France's most influential philosophe linking him to the broadest currents of 18th-century European intellectual life and giving his work a wider audience than his stage success alone might have produced"
        ],
        "relationships": [
            {"entity": "'Béverlei' (1768, drame bourgeois adapted from Edward Moore's 'The Gamester')", "relationship": "AUTHOR_OF", "note": "Wrote 'Béverlei' (1768) — a drame bourgeois adapted from Edward Moore's English 'The Gamester', Saurin's greatest theatrical success and an influence on Schiller and German bourgeois domestic drama"},
            {"entity": "'Spartacus' (1760, tragedy at Comédie-Française)", "relationship": "AUTHOR_OF", "note": "Wrote 'Spartacus' (1760) — a tragedy on the slave rebellion leader performed at the Comédie-Française, resonating with Enlightenment themes of freedom and tyranny"},
            {"entity": "Académie française (elected 1761)", "relationship": "MEMBER_OF", "note": "Elected to the Académie française in 1761 — his membership placing him among the recognized authorities of French letters"},
            {"entity": "Voltaire / Parisian Enlightenment literary circle", "relationship": "CLOSE_FRIEND_AND_ASSOCIATE_OF", "note": "A close friend of Voltaire — his connection to France's most influential philosophe linking him to the broader currents of 18th-century European Enlightenment literary life"},
            {"entity": "Friedrich Schiller / German drame bourgeois tradition (influence via 'Béverlei')", "relationship": "INDIRECT_INFLUENCE_ON", "note": "Indirectly influenced Schiller — who translated 'Béverlei' as 'Der Spieler' — and the German bourgeois domestic drama tradition that transformed 18th-century European theater"}
        ]
    }),

    # 5 — Louis Racine
    ("louis-racine", {
        "summary": (
            "Louis Racine (1692–1763) was a French "
            "poet of the Enlightenment era — the "
            "son of the great dramatist Jean Racine "
            "— whose most celebrated works were "
            "two epic poems: 'La Grâce' (1720), "
            "a philosophical poem on divine grace "
            "reflecting his Jansenist sympathies, "
            "and 'La Religion' (1742), his masterpiece, "
            "a six-canto didactic epic defending "
            "Christian faith against Enlightenment "
            "skepticism that won the Prix de "
            "poésie of the Académie française "
            "and was widely praised as "
            "the finest French religious epic "
            "of the century. He also wrote "
            "'Mémoires sur la vie de Jean Racine' "
            "(1747), a biographical account "
            "of his father that remains an "
            "important historical source.\n\n"
            "His position as a Jansenist sympathizer "
            "in the age of Voltaire made him "
            "a distinctly counter-cultural figure "
            "in the French literary world: "
            "a poet who used the grandeur "
            "of the epic form to defend "
            "Christian theology against "
            "the rationalist and materialist "
            "currents that were reshaping "
            "educated French opinion. "
            "'La Religion' was his answer "
            "to the philosophes.\n\n"
            "The most poignant event of his "
            "life was the loss of his son "
            "in the Lisbon earthquake "
            "of November 1755 — one of "
            "the 18th century's most "
            "catastrophic natural disasters "
            "that killed perhaps 40,000 people "
            "and became one of the Enlightenment's "
            "central theological controversies "
            "(inspiring Voltaire's 'Candide'). "
            "Racine's personal tragedy "
            "deepened the religious themes "
            "of his later work.\n\n"
            "His legacy as Jean Racine's "
            "son inevitably overshadowed "
            "his own achievements — "
            "he was consistently judged "
            "against an impossible standard "
            "— but his religious epic "
            "tradition filled a genuine "
            "role in 18th-century French "
            "literary culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Enlightenment poet; son of dramatist Jean Racine; author of 'La Religion' (1742) — the finest French religious epic of the 18th century, Prix de poésie Académie française; 'La Grâce' (1720, Jansenist theological poem); 'Mémoires sur la vie de Jean Racine' (1747, important biographical source); lost a son in the Lisbon earthquake (1755); a counter-Enlightenment voice defending Christian theology against Voltaire's rationalism.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Enlightenment's assault on Christian theology — the philosophes' rationalism, deism, and materialist skepticism that were reshaping educated French opinion — created the cultural challenge to which Racine's epic poems 'La Grâce' and 'La Religion' responded, making him a prominent voice in the 18th-century debate between faith and reason",
            "His Jansenist sympathies — inherited from his father Jean Racine's late-life Jansenism and the Port-Royal theological tradition — gave him the theological framework from which he engaged the Enlightenment's religious debates, positioning him as a rigorous Christian apologist rather than a conventional orthodox voice",
            "The Lisbon earthquake of 1755 — which killed his son and became one of the century's most discussed theological crises — personally intensified the religious themes that had always characterized his poetry, making his own grief a lived counterpart to the theological arguments he had long made in verse"
        ],
        "effects": [
            "His 'La Religion' (1742) contributed to 18th-century French religious poetry — as the most praised French religious epic of its era, it demonstrated that the grandeur of the epic form could be turned to theological defense, providing a counter-cultural alternative to the Enlightenment's dominant skeptical current",
            "His 'Mémoires sur la vie de Jean Racine' (1747) contributed to knowledge of his father's life — an important biographical source that preserved first-hand and family-tradition accounts of Jean Racine's career, personality, and late Jansenist conversion that would otherwise have been lost",
            "His Jansenist-inflected poetry contributed to the survival of a theological-literary tradition in France that the Enlightenment was otherwise marginalizing — the Port-Royal legacy maintaining its intellectual presence through figures like Louis Racine even as the philosophes dominated public discourse",
            "The personal theology deepened by his son's death in the Lisbon earthquake contributed to his status as a living witness to the 18th century's most dramatic collision between natural catastrophe and religious faith — his poetic response to the earthquake representing a different answer to the theodicy problem than Voltaire's 'Candide'"
        ],
        "relationships": [
            {"entity": "'La Religion' (1742, Prix de poésie Académie française, six-canto religious epic)", "relationship": "AUTHOR_OF", "note": "Wrote 'La Religion' (1742) — widely praised as the finest French religious epic of the 18th century, awarded the Prix de poésie of the Académie française, defending Christian faith against Enlightenment skepticism"},
            {"entity": "'La Grâce' (1720, Jansenist theological poem) and 'Mémoires sur la vie de Jean Racine' (1747)", "relationship": "AUTHOR_OF", "note": "Wrote 'La Grâce' (1720) — a philosophical poem on divine grace reflecting Jansenist theology — and 'Mémoires sur la vie de Jean Racine' (1747), an important biographical source on his father"},
            {"entity": "Jean Racine (father, greatest French dramatist of the 17th century)", "relationship": "SON_OF", "note": "Son of Jean Racine — the greatest French dramatist of the 17th century, a paternal legacy that inevitably overshadowed Louis Racine's own literary achievements even as it opened doors"},
            {"entity": "Lisbon earthquake (1755) / son lost in the disaster", "relationship": "PERSONAL_TRAGEDY_SHAPED_BY", "note": "Lost a son in the Lisbon earthquake of 1755 — one of the 18th century's most catastrophic disasters that became the era's central theological controversy and deepened the religious themes of his later work"},
            {"entity": "Voltaire / Enlightenment rationalism (counter-cultural opponent)", "relationship": "COUNTER-CULTURAL_VOICE_AGAINST", "note": "A counter-Enlightenment voice defending Christian theology against Voltaire's rationalism — his religious epic poetry explicitly answering the philosophes' skeptical assault on faith"}
        ]
    }),

    # 6 — François Just Marie Raynouard
    ("françois-just-marie-raynouard", {
        "summary": (
            "François Just Marie Raynouard "
            "(1761–1836) was a French playwright, "
            "lawyer, and linguist from Provence "
            "whose career combined theatrical "
            "success with pioneering linguistic "
            "scholarship. His tragedy 'Les Templiers' "
            "(The Knights Templar, 1805) was one "
            "of the most celebrated French plays "
            "of the Napoleonic era — praised by "
            "Napoleon himself, repeatedly performed "
            "at the Comédie-Française, and a landmark "
            "of early Romantic drama in France. "
            "He was elected to the Académie "
            "française in 1807 and served as "
            "its permanent secretary (1817–1826).\n\n"
            "His linguistic scholarship was "
            "equally significant. His systematic "
            "study of Occitan/Provençal language "
            "and troubadour poetry — culminating "
            "in the posthumous six-volume "
            "'Lexique roman' (1838–1844) — "
            "established him as a founder of "
            "Romance linguistics, providing "
            "the first comprehensive historical "
            "dictionary of the Occitan-Romance "
            "language family and influencing "
            "comparative linguists including "
            "Friedrich Diez, the acknowledged "
            "father of Romance philology.\n\n"
            "His career bridged the Ancien "
            "Régime and the revolutionary "
            "period: he practiced law before "
            "the Revolution and served "
            "briefly in Napoleon's legislative "
            "bodies before devoting himself "
            "primarily to scholarship and "
            "the Académie. His Provençal "
            "origins — from Brignoles, "
            "in the heart of troubadour "
            "country — gave him personal "
            "cultural connections to the "
            "linguistic material he studied.\n\n"
            "His dual legacy — theatrical "
            "and scholarly — makes him one "
            "of the most versatile figures "
            "of early 19th-century French "
            "intellectual life: both a "
            "successful playwright and "
            "a foundational linguist."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French playwright and Romance linguist; author of 'Les Templiers' (1805) — a celebrated Napoleonic-era tragedy praised by Napoleon and a landmark of early French Romanticism; Académie française (1807), permanent secretary (1817–1826); his 'Lexique roman' (6 vols, posthumous 1838–1844) founded Romance linguistics and directly influenced Friedrich Diez; from Brignoles, Provence; bridged Ancien Régime law, revolutionary politics, and 19th-century scholarship.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's cultural project of promoting French theatrical prestige — using the Comédie-Française as an instrument of national cultural policy and rewarding dramatists who addressed historical subjects with grandeur and patriotic resonance — created the cultural environment in which Raynouard's 'Les Templiers' found its famous imperial patron",
            "The early Romantic movement's fascination with medieval subjects — the Knights Templar's dramatic history of power, persecution, and destruction providing exactly the kind of grand historical material that early Romantic drama required — positioned Raynouard's Templar tragedy as a pioneering work of the new historical drama",
            "The 18th-century rediscovery of troubadour poetry and Occitan literature — the growing scholarly and Romantic interest in the medieval vernacular literature of southern France — created both the cultural context and the institutional support for Raynouard's systematic linguistic scholarship on the Provençal language"
        ],
        "effects": [
            "His 'Les Templiers' (1805) contributed to the emergence of French Romantic historical drama — a landmark work that demonstrated the theatrical possibilities of medieval historical subjects and influenced the generation of dramatists who would fully develop French Romanticism in the 1820s–1830s",
            "His 'Lexique roman' and Provençal linguistic scholarship contributed to the founding of Romance linguistics — providing the first comprehensive historical dictionary of the Occitan-Romance language family that directly influenced Friedrich Diez's 'Grammatik der romanischen Sprachen' (1836–1844), the canonical founding work of the discipline",
            "His Académie française secretaryship contributed to the institutionalization of early 19th-century French literary culture — his decade of leadership (1817–1826) shaping the Académie's activities during the period when French Romanticism was emerging to challenge the classical tradition",
            "His dual theatrical-linguistic career contributed to demonstrating that the study of troubadour poetry and Occitan literature could be pursued with both scholarly rigor and literary sensibility — his personal connection to Provence giving his linguistic work the cultural authenticity that purely philological approaches lacked"
        ],
        "relationships": [
            {"entity": "'Les Templiers' (1805, Napoleonic tragedy, Comédie-Française)", "relationship": "AUTHOR_OF", "note": "Wrote 'Les Templiers' (1805) — one of the most celebrated French plays of the Napoleonic era, praised by Napoleon and a landmark of early French Romantic historical drama"},
            {"entity": "'Lexique roman' (6 vols, posthumous 1838–1844) / founding of Romance linguistics", "relationship": "PIONEERING_SCHOLAR_AND_AUTHOR_OF", "note": "Authored the 'Lexique roman' — the first comprehensive historical dictionary of the Occitan-Romance language family, a foundational work of Romance linguistics"},
            {"entity": "Friedrich Diez / Romance philology (directly influenced by Raynouard's linguistic work)", "relationship": "DIRECT_INFLUENCE_ON", "note": "Directly influenced Friedrich Diez — the acknowledged father of Romance philology, whose 'Grammatik der romanischen Sprachen' (1836–1844) built on Raynouard's Provençal scholarship"},
            {"entity": "Académie française (member 1807, permanent secretary 1817–1826)", "relationship": "MEMBER_AND_PERMANENT_SECRETARY_OF", "note": "Elected to the Académie française in 1807 and served as its permanent secretary (1817–1826) — shaping the institution during the emergence of French Romanticism"},
            {"entity": "Napoleon / Napoleonic cultural policy / Comédie-Française", "relationship": "PLAYWRIGHT_CELEBRATED_BY", "note": "Praised by Napoleon and supported by the imperial cultural apparatus — his 'Les Templiers' fitting Napoleon's project of promoting French theatrical prestige through grand historical drama"}
        ]
    }),

    # 7 — Paul Pálffy de Erdőd
    ("paul-pálffy-de-erdöd", {
        "summary": (
            "Pál Pálffy ab Erdőd (1592–1653) was "
            "a Hungarian Catholic magnate and "
            "military commander who served as "
            "Palatine of Hungary (1645–1653) — "
            "the highest office in the Kingdom "
            "of Hungary under Habsburg rule, "
            "equivalent to the viceroy and the "
            "representative of Hungarian "
            "constitutional autonomy. He was "
            "the son of the legendary military "
            "commander Miklós Pálffy, who had "
            "defended the Hungarian frontier "
            "against the Ottomans in the late "
            "16th century, and he continued "
            "the family's tradition of military-political "
            "leadership in Royal Hungary.\n\n"
            "His palatinate (1645–1653) came "
            "after a decade of particularly "
            "intense political and military "
            "crisis in the Hungarian kingdom: "
            "the Thirty Years' War had been "
            "raging across Central Europe; "
            "Transylvanian princes György "
            "Rákóczi I and II threatened "
            "Royal Hungary's stability; "
            "and the Ottoman-Habsburg frontier "
            "remained a permanent source "
            "of military pressure. As Palatine, "
            "he was responsible for "
            "managing the Hungarian diet, "
            "mediating between the estates "
            "and the Habsburg court, and "
            "coordinating military defense.\n\n"
            "The Pálffy family was one of "
            "the most powerful Catholic "
            "magnate dynasties in Royal "
            "Hungary — consistently loyal "
            "to the Habsburgs while "
            "maintaining the Hungarian "
            "constitutional tradition's "
            "institutional independence. "
            "Their loyalty was rewarded "
            "with the highest offices "
            "of the Hungarian kingdom "
            "across multiple generations.\n\n"
            "His palatinate bridged the "
            "end of the Thirty Years' "
            "War (Peace of Westphalia, 1648) "
            "and the post-war reorganization "
            "of Central European power — "
            "a transitional period "
            "when Hungary's constitutional "
            "relationship with the "
            "Habsburg court was being "
            "renegotiated."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Palatine of Hungary (1645–1653), the highest office in the Kingdom of Hungary under Habsburg rule; son of the legendary frontier commander Miklós Pálffy; managed Hungarian constitutional institutions during the Thirty Years' War's final phase and post-Westphalia reorganization; the Pálffy family was one of the most powerful Catholic magnate dynasties in Royal Hungary across multiple generations.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Habsburg-Ottoman frontier conflict and the Thirty Years' War's simultaneous pressure on Royal Hungary — threatening the kingdom's military security from Ottoman advances in the south and Transylvanian princely ambitions in the east — created the military-political environment in which the Palatine's role as both constitutional guardian and military coordinator was essential",
            "The Hungarian constitutional tradition's insistence on the Palatine office as the guarantor of Hungarian autonomy within the Habsburg system — mediating between the Hungarian estates and the imperial court — created the institutional framework that gave Pálffy's palatinate its constitutional significance beyond military service",
            "The Pálffy family's multigenerational tradition of frontier military command and Catholic magnate loyalty to the Habsburgs — established by his father Miklós Pálffy's famous defense of Győr — created the dynastic prestige and political credibility that made Pál Pálffy a natural candidate for the kingdom's highest office"
        ],
        "effects": [
            "His palatinate contributed to Royal Hungary's constitutional stability during the most turbulent phase of the Thirty Years' War — managing the Hungarian diet and the magnate-court relationship at a time when Central Europe's political order was being fundamentally reshaped by the war's outcomes",
            "His role in navigating the post-Westphalia (1648) reorganization contributed to the redefinition of Hungary's constitutional relationship with the Habsburg court — the palatinate's institutional function of mediating between Hungarian estates and imperial authority being tested by the war's aftermath",
            "His continuation of the Pálffy family's frontier defense tradition contributed to the institutional capacity of Royal Hungary to maintain military resistance against Ottoman pressure — the family's military prestige reinforcing the political authority of the palatinate",
            "The Pálffy family's multigenerational palatinate presence contributed to the preservation of Hungarian constitutional institutions during the 17th century's most destructive phase — their consistent advocacy for Hungarian autonomy within the Habsburg framework providing a degree of institutional continuity"
        ],
        "relationships": [
            {"entity": "Palatine of Hungary (1645–1653, highest constitutional office under Habsburg rule)", "relationship": "PALATINE", "note": "Served as Palatine of Hungary (1645–1653) — the highest office in the Kingdom of Hungary, equivalent to viceroy and representative of Hungarian constitutional autonomy under Habsburg rule"},
            {"entity": "Miklós Pálffy (father, legendary Ottoman frontier commander)", "relationship": "SON_OF", "note": "Son of Miklós Pálffy — the legendary military commander who defended Hungary's Ottoman frontier in the late 16th century, whose prestige shaped the family dynasty that Pál continued"},
            {"entity": "Habsburg-Ottoman frontier conflict / Thirty Years' War (military-political context)", "relationship": "PALATINE_DURING", "note": "Served as Palatine during the Thirty Years' War's final phase — managing Hungary's constitutional institutions under simultaneous pressure from Ottoman frontier conflict and Transylvanian princely ambitions"},
            {"entity": "Hungarian diet / Hungarian constitutional tradition (mediator between estates and court)", "relationship": "CONSTITUTIONAL_MEDIATOR_OF", "note": "Served as the constitutional mediator between the Hungarian estates and the Habsburg imperial court — the Palatine's role as guarantor of Hungarian autonomy within the Habsburg system"},
            {"entity": "Peace of Westphalia (1648) / post-war Central European reorganization", "relationship": "PALATINE_DURING_AND_AFTER", "note": "His palatinate bridged the end of the Thirty Years' War (Peace of Westphalia, 1648) and the post-war reorganization of Central European power — a transitional period in Hungarian-Habsburg constitutional relations"}
        ]
    }),

    # 8 — Joachim-Jean-Xavier d'Isoard
    ("joachim-jean-xavier-disoard", {
        "summary": (
            "Joachim-Jean-Xavier d'Isoard (1766–1836) "
            "was a French Catholic bishop and cardinal "
            "from Apt in Provence who served as "
            "Bishop of Auch (1820–1836) and was "
            "created cardinal by Pope Gregory XVI "
            "in 1832. His ecclesiastical career "
            "was shaped by the French Revolutionary "
            "upheaval: he emigrated during the "
            "Revolution, returned under Napoleon's "
            "Concordat (1801), and rebuilt his "
            "ecclesiastical career across the "
            "Restoration and early Orleanist "
            "periods — a career arc characteristic "
            "of royalist French clergy who "
            "navigated the Revolution's "
            "destruction of the old "
            "Church establishment.\n\n"
            "His elevation to the cardinalate "
            "came at the end of a long "
            "episcopal career — after more "
            "than a decade as Bishop of "
            "Auch — and represented Rome's "
            "recognition of his service "
            "to the French Church during "
            "a generation of revolutionary "
            "disruption and post-Concordat "
            "reconstruction. Gregory XVI's "
            "pontificate (1831–1846) was "
            "itself shaped by conservative "
            "reaction to the liberal "
            "revolutions of 1830.\n\n"
            "Auch, the see he governed, "
            "was a major archdiocese in "
            "southwestern France — the "
            "seat of the archbishops "
            "of Gascony since late "
            "antiquity, and an important "
            "center of French Catholic "
            "life in the Restoration era. "
            "His episcopal governance "
            "contributed to the French "
            "Church's restoration of "
            "its institutional presence "
            "in southwestern France "
            "after the revolutionary "
            "disruption.\n\n"
            "His Provençal origins "
            "connected him to the "
            "rich Catholic culture "
            "of southern France — "
            "the region that had "
            "produced both the "
            "troubadour tradition "
            "and some of the "
            "Counter-Reformation's "
            "most significant figures."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French bishop and cardinal; Bishop of Auch (1820–1836); cardinal created by Pope Gregory XVI (1832); emigrated during the Revolution, returned under Napoleon's Concordat (1801); his career arc — émigré clergy returning to rebuild the French Church — characterized the Restoration ecclesiastical reconstruction; from Apt, Provence; his cardinalate recognized long episcopal service during France's most turbulent religious period.",
            "significanceCategory": "local"
        },
        "causes": [
            "The French Revolution's destruction of the old Church establishment — closing churches, expelling clergy, and forcing royalist priests into emigration — created the disruption from which d'Isoard, like hundreds of French clergy, had to rebuild his career under Napoleon's Concordat and the subsequent Restoration",
            "Napoleon's Concordat of 1801 — which normalized relations between the French state and the papacy, reopened churches, and created the legal framework for rebuilding the French Church's institutional presence — created the opportunity for returning émigré clergy like d'Isoard to resume their ecclesiastical careers",
            "The Restoration monarchy's (1814–1830) active promotion of the French Church's institutional recovery — including the appointment of royalist bishops to rebuild dioceses disrupted by the revolutionary period — created the political environment in which d'Isoard's episcopal career could develop to eventual cardinalate recognition"
        ],
        "effects": [
            "His Bishop of Auch tenure contributed to the French Church's institutional restoration in southwestern France — governing one of the major archdioceses of Gascony during the Restoration and early Orleanist periods and rebuilding episcopal governance after the revolutionary disruption",
            "His cardinalate (1832) contributed to French Catholic representation in the College of Cardinals during Gregory XVI's conservative pontificate — his elevation reflecting Rome's desire to honor French bishops who had remained loyal through the revolutionary upheaval and Restoration",
            "His career arc — émigré clergy returning under the Concordat and rebuilding their careers across three regimes (Consulate, Restoration, July Monarchy) — contributed to the pattern of French Church restoration that characterized the post-revolutionary generation of ecclesiastics",
            "His episcopal governance contributed to the preservation of Catholic institutional life in southwestern France across a generation of political instability — the Church's presence in Auch persisting through the Revolution's aftermath, Napoleonic reorganization, and Restoration recovery"
        ],
        "relationships": [
            {"entity": "Bishop of Auch (1820–1836, major Gascon archdiocese)", "relationship": "BISHOP_OF", "note": "Served as Bishop of Auch (1820–1836) — governing one of the major archdioceses of southwestern France during the Restoration and early Orleanist periods"},
            {"entity": "Cardinal created by Pope Gregory XVI (1832)", "relationship": "CARDINAL_CREATED_BY", "note": "Created cardinal by Pope Gregory XVI in 1832 — his elevation recognizing long episcopal service during France's most turbulent religious generation"},
            {"entity": "French Revolution / émigré clergy / Napoleon's Concordat (1801)", "relationship": "CAREER_SHAPED_BY", "note": "Career fundamentally shaped by the Revolution — emigrating during the disruption, returning under Napoleon's Concordat (1801), and rebuilding his ecclesiastical career across three regimes"},
            {"entity": "Restoration French Church / post-revolutionary ecclesiastical reconstruction", "relationship": "EPISCOPAL_CONTRIBUTOR_TO", "note": "Contributed to the French Church's post-revolutionary institutional restoration — his Auch episcopate representing the rebuilding of episcopal governance that characterized the Restoration's ecclesiastical recovery"},
            {"entity": "Pope Gregory XVI's pontificate (1831–1846, conservative reaction to 1830 revolutions)", "relationship": "CARDINAL_UNDER", "note": "A cardinal of Gregory XVI's pontificate (1831–1846) — a pontificate shaped by conservative reaction to the liberal revolutions of 1830, in which d'Isoard's royalist credentials made him a natural honoree"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 49)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
