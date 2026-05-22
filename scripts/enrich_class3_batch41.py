#!/usr/bin/env python3
"""
Batch 41 — 8 entities (Class 363): Famous Opera Houses & Theatres
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/363-Class-363"
FILE_PREFIX = "363"


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"{FILE_PREFIX}{slug}.json")
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
    print(f"  \u2713 {entity['name']} \u2014 sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("globe-theatre", {
        "summary": (
            "The Globe Theatre (est. 1599, Southwark, London — built by the Lord Chamberlain's Men using the timber from The Theatre, Shoreditch) is the most historically significant theatre in the English-speaking world — the performance venue where William Shakespeare's greatest plays, including Hamlet, Othello, King Lear, Macbeth, and Antony and Cleopatra, were first performed, and the physical embodiment of the Elizabethan theatrical revolution that created modern drama. The Globe was a collaborative enterprise in which Shakespeare held a 12.5% share, making him simultaneously playwright, performer, and co-owner of the theatre.\n\n"
            "The Globe was built in 1599 by Peter Street using the oak timbers of The Theatre (London's first purpose-built public playhouse, 1576) — which had been dismantled after a lease dispute — carried across the frozen Thames and re-erected in Southwark. The original Globe burned to the ground in 1613 when a stage cannon misfired during a performance of Henry VIII; a second Globe was built on the same site (1614) and closed by the Puritans in 1642. The modern reconstruction (Shakespeare's Globe, 1997), built 200 metres from the original site by Sam Wanamaker, is the primary living museum of Elizabethan theatrical practice.\n\n"
            "The Globe's open-air, thrust-stage design — with a yard for standing groundlings and tiered galleries for seated spectators, accommodating 1,500–3,000 people — was the physical form that shaped Shakespeare's dramatic technique: the soliloquy, the aside, the intimate address to the audience, and the rapid scene-changes that characterise Elizabethan drama were all responses to this specific architectural form."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most historically significant theatre in the English-speaking world (est. 1599, Southwark London); Lord Chamberlain's Men, Shakespeare 12.5% share; first performances of Hamlet, Othello, King Lear, Macbeth, Antony and Cleopatra; built from timbers of The Theatre (1576, London's first purpose-built playhouse); burned 1613 (stage cannon, Henry VIII); rebuilt 1614, closed by Puritans 1642; modern reconstruction (Shakespeare's Globe, 1997, Sam Wanamaker); thrust-stage design shaped Shakespeare's dramatic technique — soliloquy, aside, audience address.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The lease dispute at The Theatre in Shoreditch (1598) — in which the landlord Giles Allen refused to renew the lease — forced the Lord Chamberlain's Men to dismantle the building and move to Southwark, where they built the Globe using the original timbers, creating the most consequential act of theatrical recycling in history",
            "The Elizabethan theatrical boom — driven by the growth of London's population, the patronage of the Earl of Leicester and Lord Chamberlain, and the development of a professional acting tradition — created both the audience and the institutional support that made a permanent large-capacity playhouse commercially viable",
            "William Shakespeare's emergence as the dominant playwright of the Lord Chamberlain's Men — writing at least 36 plays between 1590 and 1613 — provided the literary content that made the Globe the pre-eminent theatrical venue, as audiences specifically sought his new works"
        ],
        "effects": [
            "The Globe's open-air thrust-stage design — which placed audiences on three sides of the stage and required actors to address multiple sight-lines simultaneously — shaped Shakespeare's dramatic techniques: the soliloquy (a character thinking aloud for a large public audience), the direct address, and the rapid scene-change, which have become the foundational conventions of Western drama",
            "The Shakespeare canon's first performances at the Globe — Hamlet (c.1600), Othello (c.1603), King Lear (c.1606), Macbeth (c.1606) — established the plays in the context of the specific architecture, performance conventions, and audience culture of the Globe, giving them the dramatic shape they have retained through 400 years of subsequent performance",
            "The Puritan closure of the Globe (1642) — as part of the Parliamentary closure of all London theatres during the English Civil War — ended a 43-year theatrical tradition and forced English drama into a long hibernation, from which it re-emerged after the Restoration (1660) in a fundamentally different indoor, proscenium-arch form",
            "The modern Shakespeare's Globe (1997) — the first thatched roof building constructed in London since the Great Fire (1666) — has become the world's primary centre for research into original Elizabethan staging practices, demonstrating how architectural reconstruction can recover lost theatrical knowledge"
        ],
        "relationships": [
            {"entity": "William Shakespeare (playwright, co-owner 12.5% share)", "relationship": "PRIMARY_PERFORMANCE_VENUE_OF_THE_WORKS_OF", "note": "Shakespeare's 12.5% ownership and prolific playwriting for the Globe made it the site of the first performances of his greatest works"},
            {"entity": "Lord Chamberlain's Men (acting company, Globe owners)", "relationship": "BUILT_AND_OPERATED_BY_THE", "note": "The Lord Chamberlain's Men — Shakespeare's company — built the Globe from The Theatre's timbers in 1599 and performed there until the 1613 fire"},
            {"entity": "The Theatre, Shoreditch (1576, London's first purpose-built playhouse)", "relationship": "BUILT_FROM_THE_RECYCLED_TIMBERS_OF_THE", "note": "The Globe's very timbers came from The Theatre — London's first purpose-built playhouse — making it a literal continuation of the English theatrical tradition"},
            {"entity": "Hamlet, Othello, King Lear, Macbeth (first Globe performances)", "relationship": "SITE_OF_THE_FIRST_PERFORMANCES_OF", "note": "Shakespeare's greatest tragedies were first performed at the Globe, shaped by its specific architectural form and performance conventions"},
            {"entity": "Shakespeare's Globe (modern reconstruction, Sam Wanamaker, 1997)", "relationship": "ORIGINAL_BUILDING_RECREATED_AS_THE", "note": "The 1997 Shakespeare's Globe — built 200 metres from the original site — is the primary living museum of Elizabethan theatrical practice"}
        ],
    }),

    ("la-scala", {
        "summary": (
            "Teatro alla Scala (La Scala, est. 1778, Milan — commissioned by Empress Maria Theresa of Austria, designed by Giuseppe Piermarini, built on the site of the demolished church of Santa Maria alla Scala) is the world's most prestigious opera house — the stage on which Italian opera's greatest composers, including Verdi, Puccini, Bellini, Donizetti, and Boito, premiered their most important works, and the institutional benchmark against which all other opera houses measure themselves. La Scala has been the primary forum for the Italian operatic tradition for 246 years.\n\n"
            "La Scala was built in 1776–1778 after the fire destroyed the Ducal Theatre — Milan's previous opera house — and was financed by the boxes' holders (the Milan nobility) in exchange for permanent ownership of their boxes. The neoclassical interior — horseshoe-shaped auditorium, four tiers of boxes, a fifth tier of galleries — became the template for the European opera house that was replicated from Naples to St. Petersburg. La Scala's premieres include Verdi's Otello (1887), Falstaff (1893), Puccini's Madama Butterfly revised version (1904), and Boito's Mefistofele.\n\n"
            "La Scala's roster of musical directors has been the most distinguished in opera history — Arturo Toscanini (1898–1908, 1921–1929), who imposed a new standard of rehearsal discipline; Claudio Abbado (1968–1986); Riccardo Muti (1986–2005); and Daniel Barenboim — making La Scala the primary institutional vehicle for the evolution of operatic performance practice throughout the 20th century."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most prestigious opera house (est. 1778, Milan, designed by Giuseppe Piermarini, commissioned by Empress Maria Theresa); neoclassical horseshoe auditorium — template for European opera house; world premieres: Verdi's Otello (1887), Falstaff (1893), Puccini's Madama Butterfly revised (1904), Boito's Mefistofele; Toscanini (1898–1908, 1921–1929) — new rehearsal discipline standard; Abbado, Muti, Barenboim; primary forum for Italian operatic tradition; primary institutional vehicle for operatic performance practice.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The fire that destroyed the Ducal Theatre (1776) — which had been Milan's primary opera house since 1717 — created the political and practical need for a new large opera house, and Empress Maria Theresa's patronage provided the imperial authority to commission Piermarini's design and to demolish Santa Maria alla Scala church to clear the site",
            "The Italian operatic tradition's concentration in Milan — which became the primary commercial centre for opera publishing, impresarios, and composers in the 19th century — gave La Scala a structural advantage as the venue where composers most needed to have their works premiered to achieve international success",
            "Arturo Toscanini's revolutions in performance practice (1898–1929) — demanding complete orchestral scores, darkening the auditorium during performances (breaking the social tradition of opera as a background to conversation), and imposing strict rehearsal discipline — transformed La Scala from a distinguished opera house into the global standard for operatic performance"
        ],
        "effects": [
            "La Scala's neoclassical horseshoe-shaped auditorium design — four tiers of boxes, fifth tier of galleries, a deep stage — became the template for opera house architecture across Europe and the Americas in the 19th century, replicated from the Teatro San Carlo in Naples to the Bolshoi in Moscow to the Metropolitan Opera in New York",
            "Verdi's world premieres at La Scala — Otello (1887) and Falstaff (1893), the composer's final two operas and his greatest achievements — were the culmination of 19th-century Italian opera and the defining event in the transition from Romantic opera to the 20th-century repertoire, with both works remaining central to the global repertoire",
            "Toscanini's introduction of darkened-auditorium, complete-score, disciplined-rehearsal performance standards at La Scala — which he then carried to the Metropolitan Opera, the New York Philharmonic, and the NBC Symphony Orchestra — transformed performance standards globally, establishing the conductor as the primary interpretive authority in operatic performance",
            "La Scala's role as the primary arbiter of operatic careers — singers who succeeded at La Scala were internationally recognised; those who failed faced a major career setback — made it the most powerful institutional gatekeeper in the operatic world, concentrating enormous power in the hands of La Scala's music director and administration"
        ],
        "relationships": [
            {"entity": "Giuseppe Verdi (world premieres of Otello 1887, Falstaff 1893)", "relationship": "SITE_OF_THE_WORLD_PREMIERES_OF_THE_FINAL_MASTERWORKS_OF", "note": "Verdi's La Scala premieres of Otello and Falstaff — his greatest operas — are the defining events in the history of Italian opera"},
            {"entity": "Arturo Toscanini (music director 1898–1908, 1921–1929)", "relationship": "PERFORMANCE_STANDARDS_TRANSFORMED_BY_THE_MUSIC_DIRECTORSHIP_OF", "note": "Toscanini's La Scala tenure — darkened auditorium, complete scores, strict rehearsal discipline — set the global standard for operatic performance"},
            {"entity": "Empress Maria Theresa (commissioner 1776, imperial patron)", "relationship": "COMMISSIONED_BY_THE_IMPERIAL_PATRONAGE_OF", "note": "Maria Theresa's patronage provided the imperial authority to build La Scala on the site of Santa Maria alla Scala church"},
            {"entity": "Giuseppe Piermarini (architect, neoclassical design)", "relationship": "DESIGNED_BY", "note": "Piermarini's neoclassical horseshoe auditorium design became the template for European opera house architecture"},
            {"entity": "Giacomo Puccini (Madama Butterfly revised premiere 1904)", "relationship": "SITE_OF_THE_DEFINITIVE_PREMIERE_OF_MADAMA_BUTTERFLY_BY", "note": "Puccini's revised Madama Butterfly — now one of the most performed operas in the world — premiered at La Scala in its definitive form in 1904"}
        ],
    }),

    ("mariinsky-theatre", {
        "summary": (
            "The Mariinsky Theatre (est. 1860, St. Petersburg — named after Empress Maria Alexandrovna, built on the site of an earlier circus, designed by Alberto Cavos) is Russia's most prestigious opera and ballet house — the stage on which Marius Petipa and Lev Ivanov created the classical ballet canon (Swan Lake, Sleeping Beauty, The Nutcracker), on which Tchaikovsky, Mussorgsky, and Rimsky-Korsakov premiered their most important operas, and on which Nijinsky, Pavlova, Karsavina, and Nureyev danced. The Mariinsky's ballet company — the Imperial Ballet, now the Mariinsky Ballet — is the oldest and most influential ballet company in the world.\n\n"
            "The Mariinsky was built in 1860 on the site of the earlier Bolshoi Kamenny Theatre, which had been Russia's primary opera house. Under the artistic directorship of Marius Petipa (1869–1903), the Mariinsky's Imperial Ballet became the primary vehicle for the creation of the classical ballet canon: Sleeping Beauty (1890), The Nutcracker (1892), and Swan Lake (revised 1895) — all with Tchaikovsky's scores — established the vocabulary, technique, and narrative conventions of classical ballet that remain the foundation of all subsequent ballet worldwide.\n\n"
            "The Mariinsky in the 20th century — under Kirov-era Soviet management (1935–1992) — produced Natalia Dudinskaya, Rudolf Nureyev, Mikhail Baryshnikov, and Natalia Makarova, whose defections to the West transferred the Mariinsky's technical tradition to Western companies. Under Valery Gergiev's direction (1988–2022), the Mariinsky expanded to three stages (the original, a new concert hall, and a second stage) and became Russia's primary cultural diplomacy instrument."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Russia's most prestigious opera and ballet house (est. 1860, St. Petersburg, named after Empress Maria Alexandrovna); Imperial Ballet (oldest most influential ballet company in world); Marius Petipa (1869–1903) — Sleeping Beauty (1890), Nutcracker (1892), Swan Lake (revised 1895) with Tchaikovsky; world premieres of Mussorgsky's Boris Godunov, Rimsky-Korsakov operas; Nijinsky, Pavlova, Karsavina, Nureyev, Baryshnikov, Makarova — defections transferred Mariinsky technique to Western companies; Gergiev direction (1988–2022) — expanded to 3 stages.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Tsar Alexander II's commissioning of the Mariinsky (1860) — and the Imperial Ballet's established position at the Russian court — created the institutional and financial framework in which Petipa could spend 34 years developing the classical ballet canon without commercial pressures, producing a body of work impossible in any commercially operated theatre",
            "Marius Petipa's appointment as chief ballet master (1869) — and his subsequent 34-year tenure, working with Tchaikovsky on three consecutive masterpieces — created the unique artistic partnership that produced the classical ballet canon, establishing Swan Lake, Sleeping Beauty, and The Nutcracker as the permanent core of the global ballet repertoire",
            "The Soviet state's transformation of the Imperial Ballet into the Kirov Ballet (1935) — maintaining the company's technical tradition while ideologically rebranding it — paradoxically preserved the Imperial Ballet's technique through the Soviet period, and then exported it through the defections of Nureyev (1961), Makarova (1970), and Baryshnikov (1974)"
        ],
        "effects": [
            "The Petipa-Tchaikovsky classical ballet canon — Swan Lake, Sleeping Beauty, The Nutcracker — is the foundation of the global ballet repertoire: every major ballet company in the world performs these works, and the Mariinsky's training methods have shaped ballet technique globally through the dispersal of its dancers and teachers",
            "The defections of Rudolf Nureyev (1961), Natalia Makarova (1970), and Mikhail Baryshnikov (1974) to the West transferred the Mariinsky's technical tradition to Western ballet companies — the Royal Ballet, American Ballet Theatre, and others — transforming Western ballet technique and demonstrating that artistic traditions can be exported through the movement of individual practitioners",
            "The Mariinsky's world premieres of Mussorgsky's Boris Godunov (1874), Rimsky-Korsakov's The Snow Maiden, and Tchaikovsky's operas established the Russian operatic tradition as the primary alternative to Italian opera in the 19th-century repertoire, expanding the global canon beyond the Italian-German axis",
            "Valery Gergiev's 34-year directorship (1988–2022) — which expanded the Mariinsky to three stages, established it as a touring company, and made it Russia's primary cultural diplomacy instrument — demonstrated both the potential and the political risks of using a major cultural institution as a state diplomatic tool"
        ],
        "relationships": [
            {"entity": "Marius Petipa (chief ballet master 1869–1903, classical ballet canon)", "relationship": "STAGE_ON_WHICH_THE_CLASSICAL_BALLET_CANON_WAS_CREATED_BY", "note": "Petipa's 34-year tenure at the Mariinsky — creating Swan Lake, Sleeping Beauty, The Nutcracker with Tchaikovsky — produced the foundation of the global ballet repertoire"},
            {"entity": "Pyotr Tchaikovsky (Swan Lake, Sleeping Beauty, Nutcracker composer)", "relationship": "SITE_OF_THE_FIRST_PERFORMANCES_OF_THE_THREE_GREAT_BALLETS_OF", "note": "Tchaikovsky's three great ballets — all premiered or definitively staged at the Mariinsky — established the permanent core of the global ballet repertoire"},
            {"entity": "Rudolf Nureyev (defection 1961, technical tradition transfer)", "relationship": "TRAINING_GROUND_OF", "note": "Nureyev's defection (1961) from the Mariinsky to the West transferred the Imperial Ballet's technical tradition to Western companies — one of the most consequential defections in cultural history"},
            {"entity": "Empress Maria Alexandrovna (namesake, Tsar Alexander II patron)", "relationship": "NAMED_AFTER_AND_PATRONISED_BY_THE_IMPERIAL_COURT_OF", "note": "The Mariinsky's naming after Empress Maria Alexandrovna reflected the Imperial Ballet's position as the primary cultural institution of the Russian court"},
            {"entity": "Valery Gergiev (general director 1988–2022, Russian cultural diplomacy)", "relationship": "EXPANDED_AND_INTERNATIONALISED_UNDER_THE_DIRECTION_OF", "note": "Gergiev's 34-year directorship made the Mariinsky Russia's primary cultural diplomacy instrument — with the political tensions this entailed"}
        ],
    }),

    ("hamburg-state-opera", {
        "summary": (
            "The Hamburg State Opera (Hamburgische Staatsoper, est. 1678, Hamburg — the first publicly funded opera house in the German-speaking world, opened on the Gänsemarkt as the Theater am Gänsemarkt) is one of Europe's most historically significant and artistically distinguished opera houses — the oldest continuously operating public opera house in the world, the stage on which Handel composed and premiered his earliest operas (Almira, 1705), and one of the leading houses of the 20th and 21st centuries under Rolf Liebermann's transformative management (1959–1973, 1985–1988).\n\n"
            "Hamburg's 1678 opera house — the Theater am Gänsemarkt — was the first German opera house opened to the general public (not restricted to court audiences), reflecting Hamburg's status as a free imperial city with a wealthy merchant class capable of supporting public cultural institutions. The young Handel served as violinist and harpsichordist at the Hamburg opera (1703–1706) before moving to Italy; his Hamburg operas were the earliest examples of Italian-style opera composed by a German-speaking composer.\n\n"
            "Rolf Liebermann's management of the Hamburg State Opera (1959–1973, 1985–1988) was the most productive period in the house's modern history — commissioning new operas from Henze, Dallapiccola, Penderecki, Searle, and others, and establishing Hamburg as the primary European centre for contemporary opera, a role it has maintained through the 21st century under Simone Young (2005–2015) and Kent Nagano (2015–present)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest continuously operating public opera house in the world (est. 1678, Hamburg, Theater am Gänsemarkt); first publicly funded opera house in the German-speaking world — opened to general public (not court); George Frideric Handel's earliest operas (Almira 1705) premiered here; Rolf Liebermann management (1959–1973, 1985–1988) — commissions from Henze, Dallapiccola, Penderecki — primary European centre for contemporary opera; Simone Young (2005–2015), Kent Nagano (2015–present).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Hamburg's status as a free imperial city with an independent merchant oligarchy — rather than a ducal court — drove the founding of the Theater am Gänsemarkt (1678) as a publicly funded institution serving the merchant class, creating the first German-speaking model of opera as a civic rather than a courtly cultural institution",
            "The Italian opera craze that swept through Central Europe in the late 17th century — following the model of Venice's San Cassiano (1637, the first public opera house in history) — created the demand for German-language and German-based opera houses, with Hamburg's merchant wealth providing the resources to be the first in the German-speaking world",
            "Rolf Liebermann's appointment as intendant (1959) — with a mandate to make Hamburg an international artistic force — coincided with the postwar revival of European cultural life and the availability of significant public subsidy for the arts, enabling him to commission more new operas in 14 years than any other European opera house director"
        ],
        "effects": [
            "The Theater am Gänsemarkt's model of civic, publicly-funded opera — as distinct from the court opera that dominated the German-speaking world — became the template for the civic opera house that was replicated across the German states in the 18th and 19th centuries, establishing the tradition of publicly-subsidised opera that remains the dominant model in German-speaking countries",
            "Handel's Hamburg years (1703–1706) — during which he composed his first four operas, including Almira (premiered 1705) — were the formative period of his compositional development, and Hamburg's opera tradition shaped the operatic style he carried first to Italy and then to London, where he transformed English musical life",
            "Liebermann's Hamburg commissions (1959–1973) — which produced Henze's The Bassarids, Penderecki's The Devils of Loudun, and works by Dallapiccola, Searle, and others — established contemporary opera commissioning as a central function of major opera houses, a model adopted by Covent Garden, the Met, and others in the subsequent decades",
            "Hamburg's position as a consistently top-ranked opera house outside the traditional Italian-Austrian axis has demonstrated that German civic opera — with substantial public subsidy and a commitment to both the standard repertoire and contemporary commissions — can sustain world-class artistic standards across three and a half centuries"
        ],
        "relationships": [
            {"entity": "George Frideric Handel (violinist 1703–1706, Almira 1705 premiere)", "relationship": "SITE_OF_THE_EARLIEST_OPERATIC_COMPOSITIONS_AND_PROFESSIONAL_FORMATION_OF", "note": "Handel's Hamburg years — composing Almira and three other operas — were the formative period that shaped his style before his Italian and London careers"},
            {"entity": "Theater am Gänsemarkt (1678, first public opera house in German-speaking world)", "relationship": "SUCCESSOR_INSTITUTION_TO_THE", "note": "The Hamburg State Opera is the direct institutional successor to the 1678 Theater am Gänsemarkt — the first publicly-funded opera house in the German-speaking world"},
            {"entity": "Rolf Liebermann (intendant 1959–1973, 1985–1988, contemporary opera commissions)", "relationship": "PRIMARY_ARTISTIC_VISION_DEFINED_IN_MODERN_ERA_BY_THE_MANAGEMENT_OF", "note": "Liebermann's 14-year management made Hamburg the primary European centre for contemporary opera through unprecedented commissioning activity"},
            {"entity": "Hans Werner Henze (The Bassarids, Hamburg commission)", "relationship": "PREMIER_VENUE_FOR_MAJOR_COMMISSIONS_FROM", "note": "Henze's The Bassarids — Hamburg commission — exemplifies Liebermann's policy of commissioning leading contemporary composers"},
            {"entity": "Hamburg free city (civic opera model, merchant patron)", "relationship": "FOUNDED_AS_CIVIC_INSTITUTION_OF_THE", "note": "Hamburg's status as a free imperial city with a merchant oligarchy drove the founding of a civic opera house — the template for German publicly-subsidised opera"}
        ],
    }),

    ("copenhagen-opera-house", {
        "summary": (
            "The Copenhagen Opera House (Operaen, est. 2005, Holmen, Copenhagen — designed by Henning Larsen, funded by the A.P. Møller Foundation's DKK 2.8 billion gift, the largest private donation in Danish history) is the primary opera house of Scandinavia and the home of the Royal Danish Opera — the oldest national opera company in the world (est. 1703). The building's distinctive architectural profile — a massive floating roof canopy suspended over the main auditorium on Holmen island, directly across the water from the royal palace of Amalienborg — has made it one of the most iconic cultural buildings of the early 21st century.\n\n"
            "The Royal Danish Opera was founded in 1703 under King Frederik IV — making it the oldest national opera company in continuous operation in the world, predating the Royal Opera House, Covent Garden (1732) and Vienna's Burgtheater opera by decades. For most of its history the company performed in the Royal Theatre (Det Kongelige Teater) on Kongens Nytorv; the 2005 Operaen building was the first purpose-built opera house in Denmark's history.\n\n"
            "The A.P. Møller Foundation's DKK 2.8 billion gift — from the shipping and oil empire of Mærsk McKinney Møller — was both the largest private donation in Danish history and a controversial act: critics noted that the foundation's gift came with significant conditions about the building's design and location that effectively substituted private philanthropy for democratic public decision-making, raising questions about the appropriate role of concentrated private wealth in cultural infrastructure."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Primary opera house of Scandinavia (est. 2005, Holmen Copenhagen); designed by Henning Larsen; A.P. Møller Foundation DKK 2.8 billion gift (largest private donation in Danish history); Royal Danish Opera (est. 1703, oldest national opera company in continuous operation in the world); first purpose-built opera house in Danish history; floating roof canopy architecture — iconic 21st-century cultural building; controversy over private philanthropy conditions vs democratic public decision-making.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Royal Danish Opera's need for a purpose-built home — after 300 years of performing in the Royal Theatre, which was not purpose-designed for opera — drove the advocacy for a new opera house, which was ultimately funded by the A.P. Møller Foundation's extraordinary private donation rather than government funding",
            "Mærsk McKinney Møller's personal commitment to Danish cultural life — driven by his sense of obligation to the country that had made his shipping and oil empire possible — motivated the A.P. Møller Foundation's gift, which was the single largest private cultural donation in Danish history",
            "Copenhagen's ambition to assert itself as a world-class cultural capital — alongside its Nordic rivals Oslo, Stockholm, and Helsinki — drove the political will to accept the A.P. Møller Foundation's gift despite the conditions attached, reflecting the broader competition among Nordic capitals for cultural prestige"
        ],
        "effects": [
            "The Copenhagen Opera House's Henning Larsen design — the floating roof canopy suspended over the main auditorium, facing Amalienborg Palace across the water — became one of the defining cultural buildings of the early 21st century, establishing Larsen and Danish architecture as internationally recognised forces in cultural building design",
            "The Royal Danish Opera's new home has enabled it to maintain its position as the oldest national opera company in continuous operation while competing with more lavishly funded companies in Vienna, London, and New York, demonstrating how architectural investment can revitalise institutional ambition",
            "The controversy over the A.P. Møller Foundation's conditions — which gave a private funder significant control over a national cultural building — became a case study in the ethics of private philanthropy and democratic governance, raising questions that have influenced cultural policy debates across Europe",
            "The opera house's location on Holmen — a former naval base that was being converted to cultural and residential uses — was the catalyst for one of the most significant urban regeneration projects in Copenhagen's history, transforming the waterfront opposite Nyhavn into a cultural quarter"
        ],
        "relationships": [
            {"entity": "Royal Danish Opera (est. 1703, oldest national opera company)", "relationship": "PURPOSE-BUILT_HOME_OF_THE_WORLD'S", "note": "The Royal Danish Opera — founded 1703 by King Frederik IV — is the oldest national opera company in continuous operation; the 2005 building is its first purpose-built home"},
            {"entity": "A.P. Møller Foundation / Mærsk McKinney Møller (DKK 2.8 billion donor)", "relationship": "FUNDED_BY_THE_LARGEST_PRIVATE_DONATION_IN_DANISH_HISTORY_FROM_THE", "note": "The A.P. Møller Foundation's gift was both the largest private cultural donation in Danish history and a controversial model of private philanthropy with conditions"},
            {"entity": "Henning Larsen (architect, floating roof canopy design)", "relationship": "DESIGNED_BY", "note": "Larsen's floating roof canopy design made the Copenhagen Opera House one of the defining cultural buildings of the early 21st century"},
            {"entity": "Holmen urban regeneration (former naval base, cultural quarter)", "relationship": "CATALYST_FOR_THE", "note": "The opera house's Holmen location catalysed one of Copenhagen's most significant urban regeneration projects"},
            {"entity": "King Frederik IV (Royal Danish Opera founder, 1703)", "relationship": "PERMANENT_HOME_OF_THE_COMPANY_FOUNDED_BY", "note": "The opera house gives permanent purpose-built home to the company founded by Frederik IV in 1703 — 300 years before the building's opening"}
        ],
    }),

    ("metropolitan-opera-house", {
        "summary": (
            "The Metropolitan Opera House (the Met, est. 1883, New York City — originally at Broadway and 39th Street, current home at Lincoln Center since 1966) is North America's largest and most prestigious opera house — with a seating capacity of 3,800 (the largest opera house by capacity in the world), an annual budget of $300+ million, and a radio broadcast tradition (the Saturday afternoon broadcasts, running continuously since 1931) that has given opera its largest regular audience in the English-speaking world. The Met has been the primary vehicle for bringing European opera to the Americas for 140 years.\n\n"
            "The Metropolitan Opera was founded in 1883 by a group of New York business magnates — including the Vanderbilts, Roosevelts, and Morgans — who could not obtain boxes at the older Academy of Music and built their own opera house. The Met's history has been marked by a succession of transformative general managers: Giulio Gatti-Casazza (1908–1935, who brought Toscanini and introduced the Italian repertoire), Rudolf Bing (1950–1972, who racially integrated the company), and Peter Gelb (2006–present, who introduced the Live in HD cinema transmissions).\n\n"
            "The Met's Live in HD programme (est. 2006) — transmitting live performances simultaneously to 2,000+ cinemas in 70+ countries, reaching 3+ million viewers per season — has been the most consequential innovation in opera's audience development since radio broadcasting, fundamentally changing the economics and cultural reach of the opera industry worldwide."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "North America's largest and most prestigious opera house (est. 1883, New York City; current Lincoln Center home 1966); 3,800 seats (largest opera house by capacity in world); $300+ million annual budget; Saturday afternoon radio broadcasts (1931–present, largest regular opera audience in English-speaking world); founded by Vanderbilts, Roosevelts, Morgans; Toscanini (Gatti-Casazza era); racial integration (Rudolf Bing 1952 — Marian Anderson); Live in HD (2006, 2,000+ cinemas, 70+ countries, 3+ million viewers); primary vehicle for European opera in Americas.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The New York business magnates' exclusion from the Academy of Music's box holders (who refused to sell boxes to the new rich) drove the founding of the Metropolitan Opera (1883) as a parallel institution — a commercial rivalry that produced the world's largest opera company as a byproduct of social competition among New York's Gilded Age elite",
            "Giulio Gatti-Casazza's appointment as general manager (1908) — bringing with him Arturo Toscanini — transformed the Met from a commercially-driven entertainment venue into an artistic institution, establishing the Italian repertoire as the Met's core identity and the standards of musical preparation that shaped American opera",
            "Peter Gelb's introduction of Live in HD (2006) — broadcasting Met performances simultaneously to cinemas worldwide — responded to the crisis of opera's declining audience by creating an entirely new distribution model that reached millions of viewers who would never attend a live opera performance"
        ],
        "effects": [
            "The Met's Saturday afternoon radio broadcasts (running continuously since 1931) — the longest-running regular radio programme in American history — created the largest regular opera audience in the English-speaking world, introducing millions of Americans to opera and establishing the Met as the primary cultural voice of opera in the United States",
            "Rudolf Bing's racial integration of the Met (1952, with Marian Anderson's debut as the first Black singer to perform at the Met) — and his subsequent commitment to casting Black singers in principal roles — was one of the most significant acts of cultural desegregation in the history of American arts institutions",
            "Live in HD's global reach (3+ million viewers per season, 70+ countries, 2,000+ cinemas) has made the Met the primary vehicle for opera's survival as a cultural form in the digital age — demonstrating that opera can attract large audiences if distributed in accessible formats, and creating a new revenue stream that has influenced opera houses worldwide",
            "The Met's scale — $300+ million annual budget, 900 full-time employees, productions with budgets of $5–20 million — has made it the model for the grand opera house as a major cultural institution, but also the test case for the financial sustainability of large-scale opera in an era of declining audiences and rising costs"
        ],
        "relationships": [
            {"entity": "Arturo Toscanini (Met principal conductor 1908–1915, Gatti-Casazza era)", "relationship": "ARTISTIC_STANDARDS_TRANSFORMED_BY_THE_CONDUCTORSHIP_OF", "note": "Toscanini's Met tenure — brought by Gatti-Casazza — transformed the house from a commercially-driven venue into an artistic institution"},
            {"entity": "Saturday afternoon radio broadcasts (1931–present, longest-running American radio programme)", "relationship": "CREATOR_OF_THE_LARGEST_REGULAR_OPERA_AUDIENCE_IN_THE_ENGLISH-SPEAKING_WORLD_THROUGH_THE", "note": "The Met's radio broadcasts — running since 1931 — created the largest regular opera audience in the English-speaking world"},
            {"entity": "Marian Anderson (first Black singer at Met, 1952 racial integration)", "relationship": "SITE_OF_THE_RACIAL_INTEGRATION_OF_THE_AMERICAN_OPERA_WORLD_THROUGH_THE_DEBUT_OF", "note": "Bing's casting of Marian Anderson as the first Black singer at the Met was one of the most significant acts of cultural desegregation in American arts history"},
            {"entity": "Live in HD (2006, 2,000+ cinemas, 70+ countries, 3+ million viewers)", "relationship": "PIONEER_OF_OPERA'S_DIGITAL_AGE_DISTRIBUTION_THROUGH_THE", "note": "Live in HD — reaching 3+ million viewers per season — is the most consequential innovation in opera's audience development since radio"},
            {"entity": "Vanderbilts, Roosevelts, Morgans (Gilded Age founders, 1883)", "relationship": "FOUNDED_BY_THE_SOCIAL_COMPETITION_AMONG_THE", "note": "The Met's founding by Gilded Age magnates excluded from the Academy of Music produced the world's largest opera company as a byproduct of social rivalry"}
        ],
    }),

    ("bolshoi-kamenny-theatre", {
        "summary": (
            "The Bolshoi Kamenny Theatre (Grand Stone Theatre, est. 1783, St. Petersburg — designed by Antonio Rinaldi, later rebuilt by Thomas de Thomon in 1802) was Russia's first and most prestigious imperial opera house for over a century — the primary venue for opera and ballet in St. Petersburg before the Mariinsky Theatre's opening (1860), the stage where Glinka's A Life for the Tsar (1836, the first Russian national opera) and Ruslan and Lyudmila (1842) were premiered, and the institutional ancestor of the Conservatory of St. Petersburg that now stands on its site.\n\n"
            "The Bolshoi Kamenny was built in 1783 as the first stone theatre in St. Petersburg — 'kamenny' meaning 'stone' to distinguish it from the wooden structures that preceded it and from the risk of fire that had destroyed multiple earlier Russian theatres. Under Catherine the Great's patronage, the theatre was the primary vehicle for introducing Italian opera to the Russian court and aristocracy, hosting the leading Italian and German composers and performers of the late 18th and early 19th centuries.\n\n"
            "The Bolshoi Kamenny's closure in 1886 — and its replacement by the St. Petersburg Conservatory building (now the Rimsky-Korsakov Conservatory) — was a telling moment in the shift of Russia's cultural priorities from court opera toward professional music education, reflecting the broader transformation of Russian musical life in the second half of the 19th century."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Russia's first and most prestigious imperial opera house (est. 1783, St. Petersburg, Antonio Rinaldi; rebuilt 1802, Thomas de Thomon); first stone theatre in St. Petersburg; Catherine the Great patronage — introduced Italian opera to Russian court; Glinka's A Life for the Tsar (1836, first Russian national opera) and Ruslan and Lyudmila (1842) world premieres; closed 1886, replaced by St. Petersburg Conservatory building (Rimsky-Korsakov Conservatory); institutional predecessor to Mariinsky Theatre.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Catherine the Great's ambition to make St. Petersburg a European cultural capital — which drove her patronage of architecture, art, theatre, and music on an unprecedented scale — motivated the construction of the Bolshoi Kamenny as a permanent stone opera house worthy of Russia's imperial pretensions",
            "The risk of fire that had destroyed multiple earlier Russian wooden theatres — including the first Court Theatre — drove the decision to build the Bolshoi Kamenny in stone (kamenny), creating Russia's first fireproof public entertainment building",
            "Mikhail Glinka's composition of A Life for the Tsar (1836) — written specifically for the Bolshoi Kamenny and intended as a Russian national opera responding to the dominance of Italian and German opera — was motivated by the theatre's position as the primary venue for Russian musical culture and the desire to create a Russian operatic tradition"
        ],
        "effects": [
            "Glinka's A Life for the Tsar (1836, world premiere at the Bolshoi Kamenny) — the first Russian opera on a Russian historical subject, using Russian folk melodies and harmonies within a Western operatic framework — is universally acknowledged as the foundation of the Russian national opera tradition, which produced Mussorgsky, Tchaikovsky, and Rimsky-Korsakov in the following generation",
            "The Bolshoi Kamenny's 103-year role as Russia's primary opera house — hosting Italian, German, and Russian opera for court, aristocratic, and mercantile audiences — introduced Western operatic culture to the Russian professional and upper classes, creating the educated audience that would support the Mariinsky's subsequent artistic programme",
            "The theatre's conversion to the St. Petersburg Conservatory (1886) — the institution where Rimsky-Korsakov, Glazunov, Stravinsky, and Prokofiev were trained — was one of the most consequential conversions of a performance venue into an educational institution in musical history, transforming the site of Russian opera's birth into the primary training ground for its greatest composers",
            "The Bolshoi Kamenny's name — the 'Grand Stone Theatre' — was adopted metaphorically by the Moscow Bolshoi Theatre, creating a linguistic and institutional connection between Russia's two primary opera venues that reflects the parallel development of Russian operatic culture in St. Petersburg and Moscow"
        ],
        "relationships": [
            {"entity": "Mikhail Glinka (A Life for the Tsar 1836, Ruslan and Lyudmila 1842)", "relationship": "SITE_OF_THE_WORLD_PREMIERES_OF_THE_FOUNDING_WORKS_OF_THE_RUSSIAN_NATIONAL_OPERA_BY", "note": "Glinka's two premieres at the Bolshoi Kamenny — the first Russian national operas — are the foundation of the Russian operatic tradition"},
            {"entity": "Catherine the Great (imperial patron, Italian opera introduction)", "relationship": "BUILT_UNDER_THE_CULTURAL_PATRONAGE_OF", "note": "Catherine's patronage made the Bolshoi Kamenny the primary vehicle for introducing Italian opera to the Russian court and aristocracy"},
            {"entity": "St. Petersburg Conservatory / Rimsky-Korsakov Conservatory (successor institution)", "relationship": "PREDECESSOR_INSTITUTION_ON_THE_SAME_SITE_AS_THE", "note": "The Bolshoi Kamenny's 1886 conversion to the Conservatory — where Rimsky-Korsakov and Stravinsky were trained — transformed the site from opera venue to music education institution"},
            {"entity": "Mariinsky Theatre (successor as St. Petersburg's primary opera house, 1860)", "relationship": "PREDECESSOR_INSTITUTION_OF_THE", "note": "The Mariinsky replaced the Bolshoi Kamenny as St. Petersburg's primary opera house in 1860, inheriting the Imperial Ballet and opera tradition"},
            {"entity": "Antonio Rinaldi / Thomas de Thomon (architects 1783, 1802)", "relationship": "DESIGNED_BY", "note": "Rinaldi's original 1783 building and de Thomon's 1802 rebuild created the neoclassical stone opera house that was the template for Imperial Russian theatrical architecture"}
        ],
    }),

    ("royal-opera-house", {
        "summary": (
            "The Royal Opera House (Covent Garden, est. 1732, London — the current building is the third on the site, opened 1858, designed by Edward M. Barry) is the United Kingdom's most prestigious performing arts institution — the permanent home of the Royal Opera and the Royal Ballet, both of which are among the world's leading companies. The site has housed three successive theatres since 1732, all associated with the central tradition of British performing arts: John Rich's 1732 theatre was a comedy and pantomime house; the second (1809) housed Handel's oratorio premieres; the current third building (1858) has been the home of opera and ballet since its reconstruction after the fire of 1856.\n\n"
            "The Royal Opera House's modern identity was established in the post-Second World War period under David Webster's directorship (1945–1970), when the Sadler's Wells Ballet (renamed the Royal Ballet, 1956) and the Covent Garden Opera Company (renamed the Royal Opera, 1968) were established as permanent resident companies with public subsidy. Under Georg Solti's music directorship (1961–1971) and subsequently Carlo Maria Giulini, Colin Davis, Bernard Haitink, and Antonio Pappano, the Royal Opera developed one of the world's finest permanent ensembles.\n\n"
            "Covent Garden's history as a site of public entertainment — from the 1732 theatre through the 1858 opera house — reflects 290 years of London's cultural life, including the Handel connection (his oratorios were premiered here, and he conducted at the second theatre), the Victorian heyday of Italian opera, and the 21st-century democratisation of opera through the ROH's free screenings and online streaming."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "UK's most prestigious performing arts institution (est. 1732, Covent Garden London; current building 1858, Edward M. Barry); permanent home of Royal Opera and Royal Ballet; John Rich's 1732 comedy house; Handel oratorio premieres (second theatre 1809); third building 1858; David Webster directorship (1945–1970) — Royal Ballet (1956), Royal Opera (1968); Georg Solti music directorship (1961–1971); Haitink, Pappano; 290 years of London cultural life; ROH free screenings and online streaming — democratisation of opera.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "John Rich's patent for a new theatre at Covent Garden (1728) — granted by King George II as one of only two London theatres licensed to perform 'legitimate' drama — established the Covent Garden site as one of London's two primary theatrical venues (the other being Drury Lane), creating the institutional foundation that eventually became the Royal Opera House",
            "The 1856 fire that destroyed the second Covent Garden theatre — and the reconstruction by Edward M. Barry (opened 1858) — produced the current building, which was designed as a modern opera house with the technical infrastructure required by the large-scale productions of the Victorian operatic tradition",
            "The post-WWII Arts Council's decision to provide permanent public subsidy for opera and ballet at Covent Garden — making the UK the last major European country to establish a publicly-subsidised national opera company — created the financial basis for the Royal Opera and Royal Ballet as permanent, internationally competitive companies"
        ],
        "effects": [
            "The Royal Ballet's development at Covent Garden — from the Sadler's Wells Ballet (founded by Ninette de Valois, 1931) through its establishment as the national company (1956) — created the British ballet tradition: de Valois, Frederick Ashton, and Kenneth MacMillan built a choreographic school that challenged the Mariinsky's dominance and produced Margot Fonteyn, Rudolf Nureyev's British partner, and later Darcey Bussell and Carlos Acosta",
            "Georg Solti's music directorship (1961–1971) — which raised the Royal Opera's musical standards to international competition with Vienna, Milan, and New York — established the ROH as one of the world's top five opera houses, attracting the leading singers, conductors, and directors of the postwar era",
            "The ROH's digital strategy — free screenings in public spaces, streaming via ROH on Air, and the BP Big Screens programme (reaching 400,000+ people annually) — has been one of opera's most successful audience development programmes, demonstrating that free access can expand the audience for classical music without cannibalising live attendance",
            "Handel's association with the second Covent Garden theatre — where his oratorios Messiah (London premiere, 1743), Samson, and Judas Maccabaeus were performed — established Covent Garden as the primary venue for the English choral tradition that Handel invented, a connection maintained through the ROH's continuing performance of the Handel oratorio tradition"
        ],
        "relationships": [
            {"entity": "Royal Ballet (permanent resident company, est. 1956, successor to Sadler's Wells Ballet)", "relationship": "PERMANENT_HOME_OF_THE", "note": "The Royal Ballet — established at Covent Garden by Ninette de Valois — developed the British ballet tradition that challenged Mariinsky dominance"},
            {"entity": "George Frideric Handel (Messiah London premiere 1743, oratorio premieres)", "relationship": "SITE_OF_THE_LONDON_PREMIERES_OF_THE_ORATORIOS_OF", "note": "Handel's oratorio premieres at the second Covent Garden theatre established the house as the primary venue for the English choral tradition"},
            {"entity": "Georg Solti (music director 1961–1971, international standard)", "relationship": "RAISED_TO_INTERNATIONAL_COMPETITIVE_STANDARD_BY_THE_MUSIC_DIRECTORSHIP_OF", "note": "Solti's tenure established the ROH as one of the world's top five opera houses, attracting leading postwar singers and conductors"},
            {"entity": "John Rich (patent holder 1728, Covent Garden theatre founder)", "relationship": "SITE_ESTABLISHED_AS_LONDON'S_PRIMARY_THEATRICAL_VENUE_BY_THE_PATENT_OF", "note": "Rich's 1728 royal patent for a Covent Garden theatre established the site's 290-year role as one of London's primary performance spaces"},
            {"entity": "BP Big Screens / ROH on Air (free screenings, 400,000+ annually)", "relationship": "PIONEER_OF_OPERA_AUDIENCE_DEMOCRATISATION_THROUGH_THE", "note": "The ROH's free screening and streaming programme has been one of opera's most successful audience development models"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 41 — {len(ENTITIES)} entities (Class 363: Famous Opera Houses & Theatres)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
