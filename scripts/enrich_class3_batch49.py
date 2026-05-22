#!/usr/bin/env python3
"""
Batch 49 — 8 entities (Class 380): Famous Educational & Cultural Institutions
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/380-Class-380"
FILE_PREFIX = "380"


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

    ("american-film-institute", {
        "summary": (
            "The American Film Institute (AFI — est. 1967, Washington D.C., by the National Endowment for the Arts — relocated to Los Angeles 1969, with its primary campus at the AFI Conservatory in Los Feliz) is the preeminent American institution for film education, preservation, and recognition — operating the AFI Conservatory (one of the world's leading film schools), the AFI Catalogue of Feature Films (the most comprehensive scholarly database of American cinema), and the AFI 100 Years series of cultural lists that have become the standard popular reference for American film heritage. The AFI was created by executive order of President Lyndon B. Johnson in 1967 following the National Endowment for the Arts' founding.\n\n"
            "The AFI's dual mission — training the next generation of filmmakers (through the Conservatory's graduate programmes in directing, cinematography, editing, production design, producing, and screenwriting) and preserving the heritage of American cinema (through the restoration programme that has saved 3,000+ at-risk films from deterioration) — makes it simultaneously the leading film education institution and the primary custodian of American cinematic heritage.\n\n"
            "The AFI 100 Years series (1998–present) — with its ranked lists of the 100 greatest American films, greatest heroes and villains, most memorable movie quotes, and other categories — has shaped American popular culture's understanding of film history, with 'Citizen Kane' as the #1 film on the first list becoming the standard measure of cinematic achievement and the lists themselves becoming reference points for film criticism, education, and cultural discourse."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Preeminent American film education and preservation institution (est. 1967 by President LBJ/NEA); AFI Conservatory (graduate programmes in directing, cinematography, editing, production design, producing, screenwriting); AFI Catalogue of Feature Films (most comprehensive American cinema database); AFI 100 Years series (1998–present, 'Citizen Kane' #1, standard cultural reference); 3,000+ at-risk films restored; Los Feliz Los Angeles campus; film education and heritage dual mission.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The National Foundation on the Arts and Humanities Act (1965) — which created both the National Endowment for the Arts (NEA) and the National Endowment for the Humanities — provided the legislative and financial basis for the federal government's investment in film preservation and education, leading directly to President Johnson's creation of the AFI in 1967",
            "The film preservation crisis of the 1960s–1970s — when film industry historians recognised that a large proportion of silent-era and early sound-era American films were deteriorating or had already been lost (approximately 70% of all silent films are now lost) — created the urgency for a national institution with the resources to identify, restore, and preserve the American cinematic heritage",
            "The film industry's recognition that film schools were producing the next generation of American filmmakers (USC, UCLA, NYU already active) — and that a national institution would both support these schools and provide a coordinating body for American film education — drove the AFI's educational mission"
        ],
        "effects": [
            "The AFI Conservatory's graduate programmes — which have produced directors including David Lynch, Darren Aronofsky, and Matthew Libatique — have made it one of the three or four most important film schools in the world, with AFI Conservatory alumni working at the highest levels of American cinema and television production",
            "The AFI's film restoration programme — saving 3,000+ at-risk films from nitrate deterioration and making them available to scholars and the public — has preserved a crucial portion of American cinematic heritage that would otherwise have been lost, making it the primary custodian of the early American cinema that is the foundation of global screen culture",
            "The AFI 100 Years lists — particularly the AFI 100 Greatest American Films (1998, 2007) — have shaped American cultural consciousness of film history, with the lists' rankings becoming reference points for film education, popular criticism, and cultural discourse, and 'Citizen Kane's' #1 ranking cementing it as the popular standard of cinematic achievement",
            "The AFI Life Achievement Award (est. 1973) — given annually to a figure who has made a 'distinguished contribution to the American film heritage' — has become the industry's most prestigious lifetime recognition, with recipients including John Ford, Orson Welles, James Cagney, Bette Davis, and Steven Spielberg, and AFI ceremonies serving as the primary venue for Hollywood's celebration of its own history"
        ],
        "relationships": [
            {"entity": "President Lyndon B. Johnson (created AFI 1967 by executive order, NEA founding)", "relationship": "CREATED_BY_EXECUTIVE_ORDER_OF", "note": "Johnson's 1967 executive order — following the NEA's founding — created the AFI as the federal institution for American film education and preservation"},
            {"entity": "AFI 100 Years Greatest American Films (1998, Citizen Kane #1, cultural standard)", "relationship": "ORIGINATOR_AND_PRODUCER_OF_THE", "note": "The AFI 100 Years lists — with Citizen Kane at #1 — shaped popular understanding of American film history and became the standard cultural reference"},
            {"entity": "Film preservation crisis (70% of silent films lost, nitrate deterioration, 3,000+ saved by AFI)", "relationship": "FOUNDED_PARTLY_IN_RESPONSE_TO_THE", "note": "The recognition that most early American films were deteriorating or lost drove the AFI's preservation mission — which has saved 3,000+ at-risk films"},
            {"entity": "AFI Conservatory (graduate film programmes, directing/cinematography/editing/screenwriting)", "relationship": "OPERATES_THE", "note": "The AFI Conservatory's graduate programmes have produced major American filmmakers including David Lynch and Darren Aronofsky"},
            {"entity": "National Endowment for the Arts (legislative and financial basis, 1965)", "relationship": "CREATED_BY_AND_RECEIVES_FUNDING_FROM_THE", "note": "The NEA's founding — and the National Foundation on the Arts and Humanities Act (1965) — provided the legislative basis for the AFI's creation"}
        ],
    }),

    ("calouste-gulbenkian-foundation", {
        "summary": (
            "The Calouste Gulbenkian Foundation (Fundação Calouste Gulbenkian — est. 1956, Lisbon, Portugal — created by the will of Calouste Sarkis Gulbenkian, the Armenian-British oil magnate who brokered the Turkish Petroleum Company concession and was known as 'Mr Five Percent' for his 5% stake in the Iraq Petroleum Company) is one of the world's most important cultural foundations — with an endowment of €3 billion+, an art collection of 6,000+ objects (one of the world's finest collections of Persian art, Islamic art, and European old masters), and an annual expenditure of €200 million+ on arts, education, science, and social welfare in Portugal, the UK, France, and internationally.\n\n"
            "The Gulbenkian Foundation was created from the estate of Calouste Gulbenkian — whose personal fortune, assembled through his 5% stake in the Iraq Petroleum Company (the largest oil concession in history at its 1925 signing), allowed him to assemble one of the finest private art collections of the 20th century, with works by Rembrandt, Rubens, Turner, Monet, Lalique, and comprehensive collections of Islamic art and ancient Egyptian artefacts. Gulbenkian spent the last years of his life in Lisbon (having obtained Portuguese citizenship as a neutral country during WWII), and his will left his entire estate to a foundation in Portugal.\n\n"
            "The Gulbenkian Foundation's Lisbon complex — including the Gulbenkian Museum, the Gulbenkian Concert Hall, and the Gulbenkian Garden — is one of the finest 20th-century cultural complexes in the world, and the Foundation's support for Portuguese culture, music (including the Gulbenkian Orchestra and Choir), and social welfare has made it the most important cultural institution in Portugal."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "One of world's most important cultural foundations (est. 1956 Lisbon Portugal, Calouste Sarkis Gulbenkian will); €3B+ endowment, €200M+ annual expenditure; 6,000+ art objects (finest Persian/Islamic art and European old masters in private collection); Calouste Gulbenkian 'Mr Five Percent' (5% stake Iraq Petroleum Company, 1925, largest oil concession in history); Gulbenkian Museum, Gulbenkian Concert Hall, Garden; Gulbenkian Orchestra and Choir; primary cultural institution of Portugal; arts, education, science, social welfare in Portugal/UK/France.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Calouste Gulbenkian's extraordinary wealth — accumulated through his 5% stake in the Iraq Petroleum Company (IPC), negotiated when Gulbenkian brokered the Turkish Petroleum Company concession in 1914 and confirmed in the 1925 IPC agreement — provided the financial basis for a cultural foundation of exceptional endowment",
            "Gulbenkian's lifelong art collecting — driven by his Armenian cultural heritage, his diplomatic connections, and his personal aesthetic education — assembled one of the finest private art collections of the 20th century, including works acquired from the Hermitage during Soviet Russia's cash crisis of the 1930s",
            "Gulbenkian's decision to spend his final years in Lisbon — obtaining Portuguese citizenship as a neutral country during WWII — and to establish his foundation in Portugal rather than the UK or France (where he had also lived) created the institutional and national connection that made the foundation the primary cultural institution of Portugal"
        ],
        "effects": [
            "The Gulbenkian Foundation's role as Portugal's primary cultural institution — funding the arts, music, science, and social welfare on a scale that the Portuguese state alone could not match — has made it the decisive factor in the quality of cultural and intellectual life in Portugal, particularly in the post-Salazar period when democratic Portugal needed to rebuild its cultural institutions",
            "The Gulbenkian Museum's collection — particularly its Persian art, Islamic art, and European old masters — is one of the finest permanently accessible collections in Europe, making Lisbon one of the most important cultural destinations for art scholarship in the world",
            "The Gulbenkian Foundation's international programme — funding arts, education, and social welfare in the UK, France, and globally — has made it one of the most influential non-state actors in European cultural policy, with the Gulbenkian name associated with a distinctive tradition of enlightened cultural philanthropy",
            "Calouste Gulbenkian's acquisition of Hermitage works from Soviet Russia (1930–1931) — when the Soviet government sold masterpieces to finance industrialisation — saved important artworks for public accessibility that might otherwise have disappeared into permanent state storage, making the Gulbenkian collection the custodian of some of the most important works that left the Hermitage"
        ],
        "relationships": [
            {"entity": "Calouste Sarkis Gulbenkian ('Mr Five Percent', Iraq Petroleum Company 5% stake, Armenian-British oil magnate)", "relationship": "CREATED_BY_THE_WILL_OF", "note": "Gulbenkian's IPC 5% stake — accumulated through his brokering of the 1925 Iraq Petroleum Company concession — created the fortune that funds the world's most important cultural foundation"},
            {"entity": "Iraq Petroleum Company (IPC, 1925, largest oil concession in history, 5% Gulbenkian stake)", "relationship": "ENDOWMENT_FUNDED_BY_THE_5%_STAKE_IN_THE", "note": "Gulbenkian's 5% IPC stake — the 'Mr Five Percent' arrangement — generated the extraordinary wealth that built the foundation's €3B+ endowment"},
            {"entity": "Gulbenkian Museum (6,000+ art objects, Persian art, Islamic art, European old masters)", "relationship": "OPERATES_THE", "note": "The Gulbenkian Museum — with one of the world's finest Persian and Islamic art collections — makes Lisbon a major global destination for art scholarship"},
            {"entity": "Soviet Hermitage sales (1930–1931, Soviet industrialisation, Gulbenkian acquisitions)", "relationship": "ACQUIRED_MAJOR_ARTWORKS_FROM_THE_SOVIET_HERMITAGE_DURING_THE", "note": "Gulbenkian's acquisition of Hermitage masterpieces during the Soviet cash crisis saved important artworks that might otherwise have disappeared into storage"},
            {"entity": "Portuguese cultural life (primary cultural institution, post-Salazar democratic Portugal)", "relationship": "PRIMARY_CULTURAL_AND_PHILANTHROPIC_INSTITUTION_OF", "note": "The Gulbenkian Foundation's scale of arts and education funding makes it the decisive factor in Portuguese cultural life"}
        ],
    }),

    ("royal-college-of-music", {
        "summary": (
            "The Royal College of Music (RCM — est. 1882, London, by Royal Charter of Queen Victoria — opened at its present site in Prince Consort Road, South Kensington, in 1894) is one of the world's leading conservatoires of music — training professional musicians at the highest level since 1882, holding the Royal Charter that establishes it as a national institution, and alumni who include Gustav Holst, Ralph Vaughan Williams, Benjamin Britten, Peter Maxwell Davies, and in contemporary performance, alumni in leading orchestras and opera companies worldwide. The RCM's physical setting — the Blomfield and Waterhouse buildings in the heart of London's cultural quarter, adjacent to the Royal Albert Hall — reflects its status as a Victorian national institution.\n\n"
            "The Royal College of Music was founded on the initiative of the Prince of Wales (the future Edward VII) — who recognised that Britain, despite its wealth, had no conservatoire comparable to the Conservatoire de Paris or the Leipzig Gewandhaus — with George Grove (author of Grove's Dictionary of Music and Musicians, 1879) as its first Director. The RCM's founding was part of the broader Victorian cultural ambition that created the South Kensington museums complex (the V&A, Science Museum, Natural History Museum) and the Royal Albert Hall.\n\n"
            "The RCM Museum of Instruments — holding 7,000+ historical instruments from the 15th century to the present — is one of the most important collections of musical instruments in the world, providing researchers with direct access to the instruments on which the Western classical tradition was created and performed."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Leading world conservatoire (est. 1882 London, Royal Charter Queen Victoria, Prince of Wales initiative); Gustav Holst, Ralph Vaughan Williams, Benjamin Britten, Peter Maxwell Davies alumni; Prince Consort Road South Kensington 1894; George Grove (Grove's Dictionary) first Director; South Kensington cultural quarter (V&A, Science Museum, Royal Albert Hall); Museum of Instruments (7,000+ historical instruments from 15th century); Victorian cultural ambition context; national conservatoire status.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Britain's Victorian cultural ambition — exemplified by the South Kensington museums complex and the Great Exhibition's legacy — drove the recognition that Britain, the world's wealthiest nation, lacked a national conservatoire comparable to Continental institutions, creating the political and philanthropic momentum for the RCM's founding",
            "The Prince of Wales's personal initiative — and the involvement of George Grove (whose Dictionary of Music and Musicians was the foundation of English-language musicology) as the first Director — gave the RCM both royal patronage and intellectual leadership, ensuring both social prestige and academic quality from its founding",
            "The South Kensington cultural complex's creation — with the V&A, Science Museum, Natural History Museum, and Royal Albert Hall all within walking distance — provided the cultural neighbourhood that made the RCM's Prince Consort Road site the natural location for the national conservatoire"
        ],
        "effects": [
            "The RCM's training of Holst, Vaughan Williams, and Britten — three of the four composers most responsible for the 20th-century revival of English music — made it the institutional home of the English Musical Renaissance that transformed Britain from a nation perceived as 'das Land ohne Musik' (the land without music) into one of the 20th century's great musical cultures",
            "The RCM's alumni's presence in leading orchestras, opera companies, and conservatoires worldwide — and its training of a disproportionate share of British orchestral musicians — makes it the primary institution through which the British professional music industry reproduces itself, with RCM graduates performing in virtually every major British orchestral and operatic institution",
            "The RCM Museum of Instruments — providing scholars and students with access to historical instruments — supports the historically informed performance practice that has transformed the performance of early music, making the RCM a centre for the scholarship-performance intersection that defines contemporary early music revival",
            "The RCM's research programmes — in performance science, music psychology, and historical musicology — have made it a leading research institution as well as a performance conservatoire, contributing to the academic knowledge base of music education and professional musical practice"
        ],
        "relationships": [
            {"entity": "Ralph Vaughan Williams (English Musical Renaissance, RCM student and teacher)", "relationship": "INSTITUTIONAL_TRAINING_AND_TEACHING_HOME_OF_THE_MOST_IMPORTANT_FIGURE_IN_THE_ENGLISH_MUSICAL_RENAISSANCE", "note": "Vaughan Williams's RCM training — under Parry and Stanford — and subsequent teaching at the RCM made it the institutional home of the English Musical Renaissance"},
            {"entity": "Benjamin Britten (Peter Grimes, War Requiem, 20th-century British opera)", "relationship": "INSTITUTIONAL_TRAINING_HOME_OF", "note": "Britten's RCM training produced the composer most responsible for the establishment of British opera as a serious international art form"},
            {"entity": "Gustav Holst (The Planets, English Music, RCM student and teacher)", "relationship": "INSTITUTIONAL_TRAINING_HOME_OF", "note": "Holst's RCM connection — as both student and teacher — made the institution central to his compositional development"},
            {"entity": "George Grove (Grove's Dictionary of Music and Musicians 1879, first RCM Director)", "relationship": "FIRST_DIRECTOR_AND_INTELLECTUAL_FOUNDER_WAS", "note": "Grove's Dictionary — the foundation of English musicology — and his directorship defined the RCM's intellectual character from its founding"},
            {"entity": "South Kensington cultural quarter (V&A, Science Museum, Natural History Museum, Royal Albert Hall)", "relationship": "COMPONENT_INSTITUTION_OF_THE", "note": "The RCM's location in the South Kensington cultural quarter — adjacent to the Royal Albert Hall — reflects its Victorian founding as a national cultural institution"}
        ],
    }),

    ("royal-academy-of-music", {
        "summary": (
            "The Royal Academy of Music (RAM — est. 1822, London — the oldest conservatoire in the United Kingdom, founded under the patronage of King George IV and granted its Royal Charter in 1830, located in Marylebone Road since 1912) is the UK's oldest degree-granting music institution — training professional musicians since 1822 and alumning Sir Arthur Sullivan, Charles Hallé, Annie Fischer, Simon Rattle, and thousands of professional performers who have formed the backbone of British and international orchestral, operatic, and chamber music. The RAM Museum holds 17,000+ objects including the world's most important collection of Stradivari instruments in daily use.\n\n"
            "The Royal Academy of Music was founded by Lord Burghersh (the 11th Earl of Westmorland) — a diplomat, soldier, and amateur composer who recognised that Britain lacked institutional music education — with the ambition of creating a London equivalent to the Paris Conservatoire. The founding was supported by King George IV's patronage and, from 1830, a Royal Charter, making it the first British institution with the authority to grant degrees in music.\n\n"
            "The RAM's Museum — holding instruments formerly owned by Haydn, Paganini, Liszt, Menuhin, and others, alongside the historical archive of the British music profession — makes it simultaneously a world-leading teaching institution and a major museum of musical heritage. Sir Simon Rattle (Berlin Philharmonic and London Symphony Orchestra principal conductor) is among the RAM's most celebrated alumni, and Elton John attended before commercial success diverted him from classical training."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "UK's oldest conservatoire and degree-granting music institution (est. 1822 London, Lord Burghersh founder, King George IV patronage, Royal Charter 1830); Sir Arthur Sullivan, Charles Hallé, Annie Fischer, Sir Simon Rattle alumni; RAM Museum (17,000+ objects, world's most important Stradivari collection in daily use, instruments of Haydn/Paganini/Liszt/Menuhin); Marylebone Road location since 1912; oldest British institution with authority to grant music degrees; Elton John attended.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Lord Burghersh's recognition — shared by the musical patronage circles of Regency London — that Britain lacked any institutional music education comparable to the Conservatoire de Paris, and that British musicians were consequently trained abroad or self-taught, drove his campaign to found a national music school",
            "King George IV's patronage — and the Royal Charter of 1830 — gave the institution the social prestige and legal standing necessary to attract students, faculty, and supporters, establishing it as the premier British music education institution",
            "The growth of London's professional music market in the early 19th century — with the expansion of concert halls, opera seasons, and the middle-class piano-owning culture that required professional music teachers — created the commercial demand for trained musicians that the RAM was designed to supply"
        ],
        "effects": [
            "The RAM's 200+ years of continuous professional music training — producing successive generations of orchestral musicians, opera singers, and chamber performers — has been the primary mechanism through which the British professional music industry has reproduced itself, with RAM graduates in leading positions in virtually every major British and many international musical institutions",
            "Sir Simon Rattle's training at the RAM — and his subsequent career at the Berlin Philharmonic and London Symphony Orchestra — exemplifies the institution's role in producing conductors and performers of international significance, demonstrating that British musical training can produce world-class orchestral leadership",
            "The RAM Museum's Stradivari collection — instruments in daily use by students and faculty — represents both a preservation achievement and an educational resource of extraordinary value, with students performing on instruments that are both world-class musical tools and irreplaceable cultural heritage objects",
            "The RAM's role as the oldest degree-granting music institution in Britain — establishing the principle that music education was an academic discipline worthy of university-level qualifications — created the institutional precedent for the expansion of music education in British universities and the subsequent democratisation of professional music training"
        ],
        "relationships": [
            {"entity": "Sir Simon Rattle (Berlin Philharmonic, London Symphony Orchestra, most celebrated living alumnus)", "relationship": "TRAINING_INSTITUTION_OF_ITS_MOST_CELEBRATED_CONTEMPORARY_ALUMNUS", "note": "Rattle's RAM training and subsequent career at the Berlin Philharmonic exemplify the institution's role in producing world-class orchestral leadership"},
            {"entity": "RAM Museum (17,000+ objects, world's most important Stradivari in daily use, Haydn/Paganini/Liszt instruments)", "relationship": "HOLDS_AND_OPERATES_THE", "note": "The RAM Museum's Stradivari collection — in daily use by students — combines musical heritage preservation with exceptional educational resource"},
            {"entity": "Lord Burghersh / 11th Earl of Westmorland (founder, Paris Conservatoire ambition)", "relationship": "FOUNDED_BY", "note": "Lord Burghersh's campaign — recognising the absence of British institutional music education — created the oldest UK conservatoire"},
            {"entity": "King George IV (patron, Royal Charter 1830, social prestige establishment)", "relationship": "RECEIVED_ROYAL_CHARTER_FROM", "note": "George IV's patronage and 1830 Royal Charter gave the RAM the social prestige and legal standing to attract students and faculty"},
            {"entity": "Sir Arthur Sullivan (HMS Pinafore, The Mikado, most commercially successful British composer 1880s)", "relationship": "TRAINED_ITS_MOST_COMMERCIALLY_SUCCESSFUL_VICTORIAN_ALUMNUS", "note": "Sullivan's RAM training produced the most commercially successful British composer of the Victorian era"}
        ],
    }),

    ("cambridge-assessment-international-education", {
        "summary": (
            "Cambridge Assessment International Education (CAIE — est. 1858 as the Cambridge Local Examinations Syndicate, operating as Cambridge Assessment International Education since 2017) is the world's largest provider of international education programmes and qualifications — serving 10,000+ schools in 160 countries, examining 1 million+ students annually, and operating the Cambridge International AS & A Level and IGCSE (International General Certificate of Secondary Education) programmes that are the primary international qualification pathway for university entrance worldwide. CAIE is a department of the University of Cambridge.\n\n"
            "Cambridge Assessment International Education's origins lie in the Cambridge Local Examinations Syndicate's 1858 decision to extend Cambridge University's examination system to schools outside Cambridge — initially providing examinations for schools that could not send students to the universities, and gradually developing into a global qualification system. The IGCSE (est. 1988) — providing a globally recognised secondary school leaving qualification — has been the primary vehicle for CAIE's international expansion, adopted by international schools, British schools abroad, and national education systems from Singapore to Kenya.\n\n"
            "CAIE's global reach — and the prestige of the Cambridge brand — has created a de facto international educational standard, with Cambridge qualifications recognised by universities in 160+ countries for university entrance, and Cambridge curricula shaping the educational content taught to millions of students from Singapore to South Africa. The 'Cambridge standard' has become a benchmark for educational quality worldwide."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "World's largest international education qualification provider (est. 1858 Cambridge Local Examinations Syndicate; CAIE name since 2017); 10,000+ schools in 160 countries; 1M+ students annually; IGCSE (est. 1988, primary international secondary qualification); Cambridge International AS & A Levels; University of Cambridge department; de facto global educational standard — 'Cambridge standard' benchmark; qualifications recognised by 160+ country universities; Singapore, Kenya, global international school adoption.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Cambridge University's 1858 decision to extend its examination system to schools outside Cambridge — driven by the demand from schools that wanted a prestigious external measure of their students' achievement — created the institutional basis for the world's first university-linked external examination body",
            "The British Empire's educational policy — which used Cambridge examinations as the quality benchmark for colonial education systems, making Cambridge qualifications the passport to colonial professional careers — drove the adoption of Cambridge examinations across Asia, Africa, and the Caribbean, creating the colonial educational infrastructure that became CAIE's global reach",
            "The IGCSE's creation (1988) — providing a globally recognised, non-national secondary leaving qualification suitable for internationally mobile students — created the specific qualification vehicle that drove CAIE's post-Cold War international expansion, as international schooling grew with economic globalisation"
        ],
        "effects": [
            "CAIE's global qualification network — serving 10,000+ schools in 160 countries — has created a de facto international educational standard that shapes the curriculum and pedagogical approach of millions of students worldwide, embedding Cambridge University's educational values (emphasis on analysis, critical thinking, and extended writing) in educational systems from Singapore to Kenya",
            "The IGCSE's role as the primary qualification for internationally mobile families — whose children attend international schools in multiple countries and need qualifications recognised everywhere — has made CAIE an essential component of economic globalisation, providing the educational infrastructure for the professional class that operates the global economy",
            "CAIE's adoption by national education systems — Singapore, Malaysia, Bangladesh, Kenya, and others use Cambridge qualifications as part of their national secondary systems — has extended Cambridge's educational influence far beyond the international school market, shaping the education of millions of students in national schools",
            "The 'Cambridge standard' benchmark — with schools marketing their Cambridge affiliation as a quality indicator and national education systems adopting Cambridge curricula as a development aspiration — has made Cambridge one of the most globally influential brands in education, extending the University of Cambridge's soft power far beyond its direct alumni network"
        ],
        "relationships": [
            {"entity": "University of Cambridge (institutional parent, examination system origins 1858, global brand)", "relationship": "DEPARTMENT_OF_THE", "note": "CAIE's University of Cambridge connection provides the institutional prestige and brand recognition that drives global adoption of Cambridge qualifications"},
            {"entity": "IGCSE (International General Certificate of Secondary Education, est. 1988, primary vehicle for global expansion)", "relationship": "ORIGINATOR_AND_ADMINISTRATOR_OF_THE", "note": "The IGCSE — recognised by 160+ country universities — is the primary qualification vehicle driving CAIE's global expansion"},
            {"entity": "British Empire educational policy (colonial qualification standard, Asia/Africa/Caribbean adoption)", "relationship": "GLOBAL_REACH_ESTABLISHED_THROUGH_THE", "note": "The British Empire's use of Cambridge examinations as colonial education benchmarks created the infrastructure for CAIE's post-colonial global reach"},
            {"entity": "International schools global network (10,000+ schools, 160 countries, internationally mobile families)", "relationship": "PRIMARY_QUALIFICATION_PROVIDER_FOR_THE", "note": "CAIE's global network of 10,000+ international schools provides the educational infrastructure for the internationally mobile professional class"},
            {"entity": "Singapore national education system (CAIE integration, national secondary system adoption)", "relationship": "CURRICULUM_INTEGRATED_INTO_THE", "note": "Singapore's adoption of Cambridge qualifications as part of its national secondary system exemplifies CAIE's influence beyond the international school market"}
        ],
    }),

    ("trinity-laban-conservatoire-of-music-and-dance", {
        "summary": (
            "Trinity Laban Conservatoire of Music and Dance (TL — formed 2005 by the merger of Trinity College of Music (est. 1872) and Laban (est. 1946, the Laban Centre for Movement and Dance) — based in London, across two campuses: the Faculty of Music in King Charles Court, Old Royal Naval College Greenwich, and the Faculty of Dance in the purpose-built Laban Building (2003, Herzog & de Meuron architects, Turner Prize shortlisted)) is the UK's only institution combining conservatoire music education with conservatoire-level contemporary dance training at the same degree level.\n\n"
            "Trinity College of Music's origins (1872 — founded as the London Philharmonic Society's educational arm) gave the music faculty a 150-year professional training tradition, while the Laban Centre's origins in the teaching of Rudolf Laban's movement theory — brought to London by Sigurd Leeder and Lisa Ullmann after fleeing Nazi Germany in the 1930s — gave the dance faculty a theoretical foundation in movement analysis (Labanotation) that has become the standard international system for dance notation.\n\n"
            "The Laban Building (2003) — designed by Herzog & de Meuron, the architects of the Tate Modern, and shortlisted for the Turner Prize — is one of the most architecturally celebrated contemporary performance buildings in the world, with its translucent polycarbonate façade, irregular geometric plan, and integration of rehearsal studios, performance spaces, and social areas demonstrating the architectural potential of purpose-built dance facilities."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "UK's only institution combining conservatoire music and contemporary dance (formed 2005, merger Trinity College of Music est. 1872 and Laban Centre est. 1946); Laban Building (2003, Herzog & de Meuron, Turner Prize shortlisted, Old Royal Naval College Greenwich location); Rudolf Laban movement theory (Labanotation — standard international dance notation system); Lisa Ullmann and Sigurd Leeder brought Laban to UK fleeing Nazi Germany; Old Royal Naval College King Charles Court (Faculty of Music).",
            "significanceCategory": "regional"
        },
        "causes": [
            "The strategic case for merging Trinity College of Music and the Laban Centre — recognised by both institutions' governing bodies and supported by Arts Council England funding — argued that the combination of music and dance conservatoire training would create a more complete performing arts institution and generate the economies of scale needed to maintain world-class facilities in London's expensive cultural landscape",
            "Rudolf Laban's flight from Nazi Germany (1930s) — bringing his movement analysis system and its pedagogical tradition to Britain through Leeder and Ullmann — created the theoretical foundation that made the Laban Centre's approach to dance education internationally distinctive and the basis for the Laban's global influence through Labanotation",
            "Arts Council England's 2003 investment in the purpose-built Laban Building — with Herzog & de Meuron producing one of London's most celebrated contemporary buildings — created the world-class facility that enabled the Laban Centre to compete at the highest international level for both students and faculty"
        ],
        "effects": [
            "The Laban Building's architectural celebration — Herzog & de Meuron's Turner Prize shortlisting and the building's role as one of London's most acclaimed contemporary architectural achievements — has made Trinity Laban's dance facility a model for purpose-built performing arts architecture, demonstrating how ambitious contemporary architecture can transform an institution's educational culture and public profile",
            "Labanotation's role as the international standard for dance notation — developed from Rudolf Laban's movement analysis system — has made Trinity Laban the institutional home of the global language for recording and transmitting dance, with Labanotation scores held in the institution's archive providing the primary record of 20th-century dance works",
            "Trinity Laban's combination of conservatoire music and dance training — unique in the UK — has created collaborative opportunities between musicians and dancers that are not available in single-discipline conservatoires, producing graduates with cross-disciplinary performance skills increasingly valued in contemporary performance arts",
            "The institution's location at the Old Royal Naval College Greenwich — one of the finest Baroque complexes in Britain — and the Laban Building's architectural celebration have made Trinity Laban one of the most visually distinctive performing arts institutions in Europe, contributing to Greenwich's transformation into a major London cultural destination"
        ],
        "relationships": [
            {"entity": "Rudolf Laban (movement theory, Labanotation, Nazi Germany exile, brought to UK)", "relationship": "DANCE_FACULTY_FOUNDED_ON_THE_MOVEMENT_THEORY_OF", "note": "Laban's movement analysis system — brought to Britain by Leeder and Ullmann fleeing Nazi Germany — is the theoretical foundation of the dance faculty's educational approach"},
            {"entity": "Laban Building (2003, Herzog & de Meuron, Turner Prize shortlisted, translucent polycarbonate)", "relationship": "DANCE_FACULTY_HOUSED_IN_THE_ARCHITECTURALLY_CELEBRATED", "note": "Herzog & de Meuron's Laban Building — Turner Prize shortlisted — is one of London's most celebrated contemporary architectural achievements"},
            {"entity": "Old Royal Naval College Greenwich (King Charles Court, Faculty of Music, Wren architecture)", "relationship": "MUSIC_FACULTY_LOCATED_IN_THE", "note": "The Old Royal Naval College's King Charles Court — one of Britain's finest Baroque complexes — provides the architectural setting for the music faculty"},
            {"entity": "Labanotation (international standard dance notation system, global dance score archive)", "relationship": "INSTITUTIONAL_CUSTODIAN_OF_THE_ARCHIVE_OF_THE", "note": "Labanotation scores — the primary record of 20th-century dance works — are held in Trinity Laban's archive, making it the custodian of the global language for recording dance"},
            {"entity": "Trinity College of Music (est. 1872, London Philharmonic Society origins, music faculty predecessor)", "relationship": "FORMED_BY_THE_MERGER_OF_LABAN_CENTRE_WITH", "note": "Trinity College of Music's 150-year professional training tradition forms the music faculty of the merged institution"}
        ],
    }),

    ("asean-university-network", {
        "summary": (
            "The ASEAN University Network (AUN — est. 1995, Bangkok, Thailand — the academic cooperation network of the Association of Southeast Asian Nations, connecting 30 member universities from the 10 ASEAN member states) is the primary framework for higher education cooperation in Southeast Asia — implementing quality assurance standards (AUN-QA), facilitating student and faculty exchange, harmonising credit transfer, and coordinating research collaboration across the region's leading universities as Southeast Asia has emerged as one of the world's most dynamic economic regions.\n\n"
            "AUN was established in 1995 — the same year as the ASEAN Framework Agreement on Services and one year after ASEAN's admission of Vietnam — as part of ASEAN's post-Cold War strategy of deepening regional integration across economic, social, and cultural dimensions. The network's 30 member universities include the National University of Singapore, Universiti Malaya, Chulalongkorn University, Universitas Indonesia, Ateneo de Manila University, and other leading Southeast Asian institutions.\n\n"
            "The AUN Quality Assurance (AUN-QA) framework — which sets minimum standards for curriculum design, programme assessment, and student support across member universities — has become the primary regional quality benchmark for Southeast Asian higher education, recognised by European and American universities for credit transfer purposes and driving the harmonisation of higher education standards across the region."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Primary higher education cooperation framework for Southeast Asia (est. 1995 Bangkok, 30 member universities from 10 ASEAN states); AUN-QA quality assurance framework (primary regional HE quality benchmark); NUS, Universiti Malaya, Chulalongkorn University, Universitas Indonesia, Ateneo de Manila; ASEAN post-Cold War regional integration context (1995); student/faculty exchange, credit transfer harmonisation, research collaboration; European/American university credit transfer recognition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "ASEAN's post-Cold War strategy of deepening regional integration — expanding from its original security and economic cooperation focus to include social, cultural, and educational dimensions — drove the creation of AUN as the institutional vehicle for higher education cooperation, reflecting the recognition that regional integration required shared educational standards and workforce mobility",
            "The rise of Southeast Asian universities — particularly the National University of Singapore and Universiti Malaya — to regional and global prominence created the institutional basis for a quality academic network, with leading universities providing the standards against which other member institutions could benchmark",
            "The globalisation of higher education from the 1990s — with the growth of international student mobility, the expansion of English-language degree programmes, and the increasing international comparability of qualifications — created pressure on Southeast Asian universities to harmonise their standards and ensure their qualifications were recognisable to international institutions"
        ],
        "effects": [
            "The AUN-QA framework's adoption as the regional quality standard — with European and American universities recognising AUN-QA certification for credit transfer purposes — has driven the harmonisation of Southeast Asian higher education standards, reducing the barriers to student mobility across the region and with global partner universities",
            "AUN's student and faculty exchange programmes — facilitating the movement of students and researchers across the region's leading universities — have created the academic networks that support ASEAN's research collaboration and the development of a shared regional intellectual culture",
            "The AUN framework's contribution to ASEAN's regional integration — complementing the ASEAN Economic Community (AEC) with educational mobility and shared standards — has supported the development of the regional professional workforce that the AEC's economic integration requires, with AUN alumni contributing to ASEAN's growing role in the global economy",
            "AUN's quality assurance influence on member universities — driving curriculum reform, teaching quality improvement, and student support enhancement — has contributed to the overall improvement of Southeast Asian higher education quality, supporting the region's ambition to develop world-class universities capable of competing with East Asian and Western institutions"
        ],
        "relationships": [
            {"entity": "Association of Southeast Asian Nations (ASEAN, founding organisational context, 10 member states)", "relationship": "ACADEMIC_COOPERATION_NETWORK_OF_THE", "note": "AUN is the higher education arm of ASEAN, implementing the educational dimension of ASEAN's regional integration strategy"},
            {"entity": "National University of Singapore (founding member, regional leading university)", "relationship": "NETWORK_INCLUDING_THE_REGION'S_LEADING_UNIVERSITIES_INCLUDING_THE", "note": "NUS's membership provides AUN with institutional prestige and the standard against which other member universities benchmark"},
            {"entity": "AUN-QA Quality Assurance framework (regional HE quality standard, European/American recognition)", "relationship": "ORIGINATOR_AND_IMPLEMENTER_OF_THE", "note": "The AUN-QA framework — recognised internationally for credit transfer — is the primary vehicle for harmonising Southeast Asian higher education standards"},
            {"entity": "ASEAN Economic Community (AEC, regional professional workforce development context)", "relationship": "EDUCATIONAL_COMPLEMENT_TO_THE", "note": "AUN's educational cooperation complements the AEC's economic integration by developing the regional professional workforce the integrated economy requires"},
            {"entity": "Chulalongkorn University (Bangkok founding location, Thai member institution)", "relationship": "NETWORK_MEMBER_AND_HOST_COUNTRY_INSTITUTION", "note": "Chulalongkorn University's Bangkok location — and Thailand's hosting of AUN headquarters — reflects Thailand's central role in ASEAN's educational cooperation"}
        ],
    }),

]


if __name__ == "__main__":
    print(f"Batch 49 \u2014 {len(ENTITIES)} entities (Class 380: Famous Educational & Cultural Institutions)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
