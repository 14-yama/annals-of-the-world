#!/usr/bin/env python3
"""
Batch 35 — 8 entities (Class 345): Cultural Institutions
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/345-Class-345"
FILE_PREFIX = "345"


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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("british-council", {
        "summary": (
            "The British Council (est. 1934, London — incorporated by Royal Charter 1940) is the United Kingdom's international organisation for cultural relations and educational opportunities — the primary instrument of British soft power, operating in over 100 countries with 12,000 staff and reaching over 100 million people annually through English language teaching, cultural programmes, educational exchanges, and arts promotion. The British Council's mission — 'to create friendly knowledge and understanding between the people of the UK and the wider world' — makes it the model for cultural diplomacy that most other national cultural institutions (Goethe-Institut, Confucius Institutes, Alliance Française) have sought to replicate.\n\n"
            "The British Council was founded in 1934 — during the rise of Fascism in Europe — as a response to German and Italian cultural propaganda abroad: the Nazi Reichsministry of Propaganda and the Italian Istituto Fascista di Cultura were using cultural programmes to build international sympathy for Fascism, and Britain needed an equivalent institution to promote British culture and values. The Council was given a Royal Charter (1940) and became Britain's primary cultural diplomacy institution through WWII and the Cold War — promoting British values, English language teaching, and the arts in countries ranging from the Soviet bloc to South Asia and the Middle East.\n\n"
            "The British Council's English language teaching — producing the IELTS examination (International English Language Testing System) jointly with Cambridge Assessment — has made it the world's leading English language assessment organisation, with 3.5 million+ IELTS tests administered annually."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "UK's primary international cultural diplomacy organisation (est. 1934, Royal Charter 1940); operating in 100+ countries, 12,000 staff, 100 million people annually; founded in response to Nazi/Italian cultural propaganda; primary British soft power instrument; IELTS examination (3.5 million+ tests/year) — world's leading English language assessment; Cold War cultural diplomacy; model for Goethe-Institut, Confucius Institutes, Alliance Française.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The rise of Fascist cultural propaganda abroad — Nazi Reichsministry of Propaganda and Italian Istituto Fascista di Cultura building international sympathy for Fascism through cultural programmes — created the political urgency for a British institution to promote British culture and democratic values",
            "The British government's recognition that English language teaching, cultural exchange, and arts promotion were effective instruments of international influence — at lower cost and greater long-term impact than traditional diplomacy — drove the founding and funding of the British Council",
            "The dissolution of the British Empire — and the transition from formal imperial control to 'soft power' influence through language, education, and culture — made the British Council increasingly important as the primary instrument of post-imperial British international influence"
        ],
        "effects": [
            "The British Council's global English language teaching network — reaching 600 million English learners worldwide — has made English the primary language of international science, commerce, diplomacy, and culture, with the British Council as one of the principal institutional forces driving this globalisation of English",
            "The IELTS examination (developed jointly with Cambridge Assessment and IDP Australia) — with 3.5 million+ tests administered annually in 140 countries — is the world's most widely taken English language proficiency test, used for immigration to the UK, Australia, and New Zealand and for university admission worldwide",
            "The British Council's Cold War cultural diplomacy — promoting British values, democratic culture, and arts in Communist bloc countries, the Middle East, and Asia — provided a model of cultural diplomacy that other democracies adopted, and contributed to the long-term influence of British culture in countries that were decolonising from British rule",
            "The British Council's arts and culture programmes — including touring exhibitions, literary festivals, and the Shakespeare festival — have made British literature, theatre, and visual art globally accessible, reinforcing the UK's position as one of the world's leading cultural producers"
        ],
        "relationships": [
            {"entity": "Nazi cultural propaganda (Reichsministry, 1930s)", "relationship": "FOUNDED_IN_RESPONSE_TO_THE_THREAT_OF", "note": "The British Council (1934) was founded specifically in response to the threat of Nazi and Italian Fascist cultural propaganda — as Britain's democratic cultural diplomacy counter-measure"},
            {"entity": "IELTS examination (3.5 million tests/year)", "relationship": "CO-DEVELOPS_AND_ADMINISTERS_THE", "note": "The British Council co-develops and administers IELTS (with Cambridge Assessment and IDP Australia) — the world's most widely taken English language proficiency test"},
            {"entity": "Goethe-Institut (German cultural diplomacy)", "relationship": "DIRECT_MODEL_FOR_THE", "note": "The British Council's cultural diplomacy model was directly emulated by the Goethe-Institut, Confucius Institutes, Alliance Française, and other national cultural bodies"},
            {"entity": "Cold War (British cultural diplomacy)", "relationship": "PRIMARY_INSTRUMENT_OF_BRITISH_CULTURAL_DIPLOMACY_DURING_THE", "note": "The British Council's Cold War operations — promoting British values in Communist bloc countries, the Middle East, and Asia — were a primary instrument of British soft power"},
            {"entity": "English as global language (600 million learners)", "relationship": "ONE_OF_THE_PRIMARY_INSTITUTIONAL_FORCES_DRIVING_THE_GLOBALISATION_OF", "note": "The British Council's global English teaching network has been one of the principal institutional forces driving the globalisation of English as the world's primary international language"}
        ],
    }),

    ("austrian-national-library", {
        "summary": (
            "The Austrian National Library (Österreichische Nationalbibliothek, est. c.1368, Vienna — one of the oldest libraries in the world, developed from the Habsburg imperial library) is Austria's national library and one of the greatest libraries in the world — holding 12 million+ objects including the papyrus collection (the world's second largest, with 180,000 papyri), the globe collection (the world's largest, with 260+ historical globes), the music collection, and the Habsburg court archives. The library's Baroque State Hall (designed by Johann Bernhard Fischer von Erlach, completed 1726) is one of the most magnificent library interiors in the world.\n\n"
            "The library developed from the collection of Rudolf IV of Habsburg (c.1368) and was built into one of Europe's great scholarly collections by successive Habsburg emperors — especially the book-loving Maximilian I and Charles VI (who ordered the Baroque State Hall). The collection includes Gutenberg Bibles, medieval illuminated manuscripts, the Beatus Map (1086), Turkish war trophies from the Siege of Vienna (1683), and the largest collection of Mozart's musical manuscripts. The library's papyrus collection — acquired from Egyptian and Sudanese archaeological excavations — makes it a primary resource for the study of ancient Egypt, Roman Egypt, and early Christianity.\n\n"
            "The Austrian National Library's Digital Library Programme — digitising its unique collections for global access — has made it one of the leading digital humanities institutions in Europe, with 750,000+ digitised objects including the world's largest collection of digitised historical globes."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "One of world's oldest and greatest libraries (est. c.1368, Habsburg imperial collection); 12 million+ objects; world's second largest papyrus collection (180,000 papyri); world's largest globe collection (260+ historical globes); Baroque State Hall (Fischer von Erlach, 1726) — one of world's finest library interiors; Gutenberg Bibles, Mozart manuscripts, medieval illuminated manuscripts, Turkish war trophies from Siege of Vienna (1683); leading digital humanities institution (750,000+ digitised objects).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Rudolf IV of Habsburg's collection (c.1368) and successive Habsburg emperors' book-collecting ambitions — as expressions of imperial prestige, scholarly patronage, and the Counter-Reformation programme — built the library into one of Europe's great collections",
            "Emperor Charles VI's commissioning of Johann Bernhard Fischer von Erlach to design the Baroque State Hall (completed 1726) — as a monument to Habsburg imperial power through the medium of knowledge — was the defining architectural achievement that gave the library its magnificent physical presence",
            "The Habsburg Empire's position at the centre of European and Mediterranean diplomacy — and the acquisition of trophies, manuscripts, and collections through conquest, marriage alliances, and purchase — brought extraordinary objects to Vienna, from Turkish war trophies to Egyptian papyri"
        ],
        "effects": [
            "The Austrian National Library's papyrus collection — 180,000 papyri from Egyptian and Sudanese archaeological excavations — is the primary source for the study of ancient Egyptian, Greek, and Roman administration, early Christianity's spread in Egypt, and everyday life in Roman Egypt",
            "The Baroque State Hall — with its frescoed ceiling by Daniel Gran, 16 marble columns, and two levels of bookshelves — has been the model for baroque library design across Europe and is considered one of the most beautiful interiors in the world, visited by 800,000+ people annually",
            "The library's globe collection (260+ historical globes, including the oldest surviving pair by Martin Behaim, 1492–1493) — preserved as a record of how humanity understood the world's geography across five centuries — makes Vienna the primary centre for the history of cartography and geographical knowledge",
            "The Austrian National Library's Digital Library Programme — making 750,000+ unique objects freely accessible online — has democratised access to Habsburg cultural heritage and established it as a model for digital preservation of analogue cultural collections"
        ],
        "relationships": [
            {"entity": "Habsburg Dynasty (imperial patrons)", "relationship": "BUILT_AND_DEVELOPED_AS_IMPERIAL_LIBRARY_BY_THE", "note": "The Habsburg emperors — from Rudolf IV through Charles VI — built the library into one of Europe's greatest collections as an expression of imperial prestige and scholarly patronage"},
            {"entity": "Baroque State Hall (Fischer von Erlach, 1726)", "relationship": "CONTAINS_THE_MAGNIFICENT", "note": "The Baroque State Hall — designed by Fischer von Erlach and completed 1726 — is one of the most magnificent library interiors in the world and the library's defining architectural achievement"},
            {"entity": "Papyrus collection (180,000 papyri, world's second largest)", "relationship": "CUSTODIAN_OF_THE_WORLD'S_SECOND_LARGEST", "note": "The 180,000 papyri — acquired from Egyptian and Sudanese excavations — make the library a primary resource for ancient Egypt, Roman Egypt, and early Christianity studies"},
            {"entity": "Globe collection (260+ globes, world's largest)", "relationship": "CUSTODIAN_OF_THE_WORLD'S_LARGEST", "note": "The 260+ historical globes — including Martin Behaim's 1492–1493 globes — make Vienna the primary centre for the history of cartography and geographical knowledge"},
            {"entity": "Mozart musical manuscripts", "relationship": "CUSTODIAN_OF_THE_LARGEST_COLLECTION_OF", "note": "The library holds the largest collection of Mozart's musical manuscripts — making it an essential resource for Mozart scholarship and the history of classical music"}
        ],
    }),

    ("casa-de-las-am\u00e9ricas", {
        "summary": (
            "Casa de las Américas (est. 1959, Havana, Cuba — founded by the Cuban Revolutionary Government) is the most important cultural institution of the Latin American Left — the Cuban government's flagship cultural organisation that has promoted Latin American and Caribbean literature, art, music, and thought since the Cuban Revolution, awarding the Premio Casa de las Américas (the most prestigious literary prize for Latin American writing), publishing books and the journal Casa, and serving as the cultural embassy of the Cuban Revolutionary project to the world's progressive intelligentsia.\n\n"
            "Casa de las Américas was founded on 28 April 1959 — less than four months after Fidel Castro's victory — as an expression of the Revolution's commitment to Latin American cultural solidarity. Under the long directorship of Haydée Santamaría (1959–1980), Casa became the intellectual and artistic centre of the Latin American cultural revolution of the 1960s–1970s — the Boom in Latin American literature (García Márquez, Vargas Llosa, Cortázar, Fuentes), the nueva canción musical movement (Silvio Rodríguez, Pablo Milanés), and the revolutionary visual arts movement all passed through Casa's programmes.\n\n"
            "Casa de las Américas's relationship with intellectual freedom has been complex: it was simultaneously the institution that made Latin American writers famous and the one that enforced the Revolution's cultural limits — the Padilla affair (1971), in which the imprisonment of poet Heberto Padilla broke the relationship between the Cuban Revolution and many European and Latin American intellectuals (Sartre, Vargas Llosa, Fuentes), centred on Casa's cultural authority."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most important cultural institution of Latin American Left (est. 28 April 1959, 4 months after Cuban Revolution); Premio Casa de las Américas — most prestigious Latin American literary prize; Haydée Santamaría directorship (1959–1980); Latin American Boom literature (García Márquez, Vargas Llosa, Cortázar, Fuentes); nueva canción (Silvio Rodríguez, Pablo Milanés); Padilla affair (1971) — broke Revolution-intellectual alliance; journal Casa; cultural embassy of Cuban Revolution to global Left.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Cuban Revolution's commitment to Latin American cultural solidarity — and Fidel Castro's belief that cultural production was a key instrument of revolutionary politics — drove the founding of Casa as the Revolution's flagship cultural institution, four months after the revolutionary victory",
            "The Latin American cultural revolution of the 1960s — the Boom in literature, the nueva canción musical movement, the new cinema — created the regional cultural energy that Casa channelled, promoted, and in some cases directly enabled through its publications, prizes, and residencies",
            "The Cold War context — in which the US and the USSR were both using cultural institutions as instruments of ideological competition (the CIA's Congress for Cultural Freedom; the Soviet writers' unions) — drove the Cuban Revolution to create its own cultural diplomacy institution as a counter-offer to the progressive intelligentsia"
        ],
        "effects": [
            "The Premio Casa de las Américas — awarded annually since 1960 for literature in Spanish, Portuguese, French, and Creole — became the most prestigious literary prize for Latin American and Caribbean writing, launching or affirming the careers of writers including José Donoso, Reinaldo Arenas, and many others across 60+ years",
            "Casa's promotion of the Latin American Boom — publishing García Márquez, Vargas Llosa, Cortázar, and Fuentes in its journal and through its prize — was one of the institutional forces that gave the Boom its regional coherence and international visibility, contributing to the global recognition of Latin American literature as a distinct and major literary tradition",
            "The Padilla affair (1971) — in which Heberto Padilla's imprisonment for 'counter-revolutionary' poetry broke the relationship between the Cuban Revolution and many European and Latin American intellectuals — demonstrated the limits of revolutionary cultural freedom and permanently fractured the alliance between the Latin American Left and the Castro government",
            "The nueva canción movement — Silvio Rodríguez, Pablo Milanés, and Victor Jara — promoted and sustained by Casa's cultural programmes, became the most politically influential popular music movement in Latin American history, with consequences for Chile, Argentina, Nicaragua, and the cultural politics of the Latin American Left"
        ],
        "relationships": [
            {"entity": "Cuban Revolution (1959)", "relationship": "FOUNDED_BY_THE_REVOLUTIONARY_GOVERNMENT_FOUR_MONTHS_AFTER_THE", "note": "Casa was founded (28 April 1959) as the Revolution's flagship cultural institution — an expression of the Revolution's commitment to Latin American cultural solidarity"},
            {"entity": "Premio Casa de las Américas (most prestigious Latin American literary prize)", "relationship": "AWARDS_THE_ANNUAL", "note": "The Premio Casa — awarded since 1960 in Spanish, Portuguese, French, and Creole — is the most prestigious literary prize for Latin American and Caribbean writing"},
            {"entity": "Latin American Boom (García Márquez, Vargas Llosa, Cortázar)", "relationship": "ONE_OF_THE_PRIMARY_INSTITUTIONAL_PROMOTERS_OF_THE", "note": "Casa's publications and prize helped give the Latin American Boom its regional coherence and international visibility"},
            {"entity": "Padilla affair (1971, Heberto Padilla)", "relationship": "CENTRE_OF_THE_CULTURAL_FREEDOM_CRISIS_OF_THE", "note": "The Padilla affair (1971) — centred on Casa's cultural authority — broke the alliance between the Cuban Revolution and the Latin American/European Left intelligentsia"},
            {"entity": "Nueva canción movement (Silvio Rodríguez, Pablo Milanés)", "relationship": "PROMOTED_AND_SUSTAINED_THE", "note": "Casa's cultural programmes promoted the nueva canción movement — the most politically influential popular music movement in Latin American history"}
        ],
    }),

    ("banff-centre-for-arts-and-creativity", {
        "summary": (
            "The Banff Centre for Arts and Creativity (est. 1933, Banff, Alberta, Canada — founded as the Banff School of Drama) is Canada's premier arts institution and one of the world's leading residential arts and leadership development centres — a unique institution combining professional artistic training, artist residencies, leadership development, and mountain wilderness setting in the Canadian Rockies. Over 90 years, the Banff Centre has trained generations of Canadian and international artists, musicians, writers, and theatre makers, and hosted the world premiere presentations of major artistic works.\n\n"
            "The Banff Centre was founded in 1933 during the Great Depression by Elizabeth Sterling Haynes — a drama teacher who believed that arts education was essential for community health and Canadian national identity. From its origins as a summer drama school, it expanded into music, visual arts, writing, and leadership development — always maintaining its distinctive residential mountain setting, where artists from around the world live and work together in creative community. The Centre's location in Banff National Park (Canada's first national park) and its Arts and Mountain Culture programme have established an enduring connection between artistic creation and wilderness.\n\n"
            "The Banff Centre's international reputation rests on its artist residency programmes, its annual Banff International String Quartet Competition, the Banff World Media Festival, and its leadership development programmes for executives and public sector leaders — an unusual combination that reflects the Banff Centre's belief that artistic creativity and leadership excellence emerge from the same human capacities."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Canada's premier arts institution (est. 1933, Great Depression, Elizabeth Sterling Haynes); unique residential arts centre in Canadian Rockies; Banff International String Quartet Competition; Banff World Media Festival; artist residency programmes; combines professional artistic training with leadership development; 90+ years training Canadian and international artists; Banff National Park — arts and mountain culture connection.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Elizabeth Sterling Haynes's founding vision — that arts education was essential for community health and Canadian national identity during the Great Depression — drove the establishment of the Banff School of Drama (1933) as a summer programme for drama teachers",
            "The University of Alberta's partnership with the Banff Centre — which provided the academic and institutional support for the Centre's early development — and the Canadian federal government's recognition of arts education as a national priority drove the Centre's expansion beyond drama",
            "The Banff Centre's unique setting in Banff National Park — a UNESCO World Heritage Site — created a physically distinctive environment for artistic creation that distinguished it from urban arts institutions and attracted artists seeking the combination of creative community and wilderness inspiration"
        ],
        "effects": [
            "The Banff Centre's training programmes — which have served over 100,000 artists, leaders, and thinkers from 100+ countries over 90 years — have had a formative influence on Canadian and international artistic practice across music, theatre, visual arts, writing, and film",
            "The Banff International String Quartet Competition — one of the world's leading chamber music competitions — has launched the careers of internationally renowned ensembles and established Banff as a primary site for classical music excellence",
            "The Banff Centre's leadership development programmes — combining artistic creativity and outdoor wilderness challenges — have influenced thousands of Canadian and international business, government, and non-profit leaders, contributing to a distinctive Canadian approach to leadership development",
            "The Banff World Media Festival — one of the world's leading media industry conferences, bringing together TV, film, and digital media executives — has made Banff a significant hub for the global media industry, connecting Canada's arts ecology to international media production"
        ],
        "relationships": [
            {"entity": "Elizabeth Sterling Haynes (founding figure)", "relationship": "FOUNDED_BY", "note": "Haynes founded the Banff School of Drama (1933) — driven by her belief that arts education was essential for community health during the Great Depression"},
            {"entity": "Banff National Park (UNESCO World Heritage Site)", "relationship": "SITUATED_WITHIN_AND_CREATIVELY_SHAPED_BY", "note": "The Banff Centre's location in Banff National Park — Canada's first national park — has defined its distinctive arts-and-wilderness identity"},
            {"entity": "Banff International String Quartet Competition", "relationship": "HOSTS_THE_ANNUAL", "note": "The BISQC — one of the world's leading chamber music competitions — has launched the careers of internationally renowned ensembles"},
            {"entity": "Banff World Media Festival", "relationship": "HOSTS_THE_ANNUAL", "note": "The Banff World Media Festival — a leading global media industry conference — connects Canada's arts ecology to international TV, film, and digital media production"},
            {"entity": "Canadian arts and cultural identity", "relationship": "PRIMARY_PROFESSIONAL_TRAINING_INSTITUTION_FOR", "note": "The Banff Centre's 90+ year training of Canadian artists and leaders has given it a formative influence on Canadian cultural and artistic identity"}
        ],
    }),

    ("international-theatre-institute", {
        "summary": (
            "The International Theatre Institute (ITI, est. 1948, Prague — founded by UNESCO and the International Theatre community) is the world's leading international organisation for theatre arts — the UNESCO partner body that promotes international theatrical exchange, the performing arts as an instrument of peace and cultural dialogue, and the rights of theatre practitioners worldwide. ITI is the world's largest theatre network, with centres in 90+ countries and a history spanning from post-WWII reconstruction through the Cold War to the contemporary global arts ecology.\n\n"
            "ITI was founded in 1948 by UNESCO and the International Theatre community — immediately after WWII, when theatre was seen as a primary instrument for rebuilding cultural bridges between nations that had been at war. The founding congress was held in Prague — a symbolically significant choice: Czechoslovakia was in the process of becoming a Communist state (the Communist coup occurred in February 1948), but the ITI's founding in Prague reflected the brief post-war moment of cultural optimism before the Cold War divided Europe. Julian Huxley (UNESCO Director-General) and J.B. Priestley (playwright) were key founding figures.\n\n"
            "ITI's most significant annual event is World Theatre Day (27 March) — established in 1961 — when a leading international figure delivers the World Theatre Day Message. The day is celebrated by theatre communities in 100+ countries and is the single most important annual event in global theatre culture. ITI's World Theatre Education Congress and international competitions for theatre schools have shaped theatre education standards worldwide."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "World's largest theatre network (est. 1948, Prague, UNESCO and J.B. Priestley); founded immediately post-WWII as instrument for rebuilding cultural bridges; 90+ national centres; World Theatre Day (27 March, since 1961) — celebrated in 100+ countries; Julian Huxley (UNESCO Director-General), J.B. Priestley (founding figures); Cold War cultural bridge; UNESCO partner body; World Theatre Education Congress; shaped theatre education standards worldwide.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The post-WWII conviction — shared by UNESCO's founders — that cultural exchange, including theatre, was essential for preventing the conditions that led to war: that contact between peoples through arts and culture was one of the fundamental instruments of peace-building",
            "J.B. Priestley's vision of theatre as a universal humanising force — and his belief that theatre practitioners worldwide shared a common professional identity that transcended national politics — drove the founding of an international organisation that could facilitate the exchange of theatrical knowledge across national borders",
            "The Cold War's division of the world into ideological blocs — which restricted cultural exchange between East and West — gave the ITI a unique diplomatic function as one of the few cultural organisations where theatre practitioners from NATO and Warsaw Pact countries could meet and collaborate"
        ],
        "effects": [
            "World Theatre Day (27 March, established 1961) — when a leading international figure delivers the World Theatre Day Message — has created the single most important annual occasion for global theatre culture, promoting theatre as an art form to 100+ countries simultaneously",
            "ITI's Cold War bridging function — facilitating cultural exchange between East and West European theatre communities at a time when all other contact was restricted — contributed to the long-term cultural convergence that made European cultural integration possible after the Cold War ended",
            "ITI's work on the rights of theatre practitioners — including the development of international standards for theatre education, intellectual property rights for playwrights, and the safety of artists in conflict zones — has contributed to the international legal framework for the performing arts",
            "The World Theatre Education Congress — bringing together theatre schools from 90+ countries to establish shared standards — has raised the quality of theatre education worldwide and created the shared professional vocabulary that enables international theatre collaboration"
        ],
        "relationships": [
            {"entity": "UNESCO (founding partner)", "relationship": "FOUNDED_WITH_AND_REMAINS_PARTNER_OF", "note": "ITI was co-founded by UNESCO (1948) — and remains UNESCO's partner body for theatre and the performing arts worldwide"},
            {"entity": "J.B. Priestley (playwright, founding figure)", "relationship": "CO-FOUNDED_BY", "note": "J.B. Priestley's vision of theatre as a universal humanising force was central to ITI's founding mission"},
            {"entity": "World Theatre Day (27 March, since 1961)", "relationship": "ESTABLISHES_AND_ORGANISES_THE_ANNUAL", "note": "World Theatre Day — celebrated in 100+ countries — is ITI's most significant annual event and the most important occasion in global theatre culture"},
            {"entity": "Cold War (East-West cultural exchange)", "relationship": "ONE_OF_THE_FEW_CULTURAL_BRIDGES_BETWEEN_EAST_AND_WEST_DURING_THE", "note": "ITI's function as a cultural bridge between NATO and Warsaw Pact theatre communities gave it a unique diplomatic role during the Cold War"},
            {"entity": "Post-WWII cultural reconstruction (1948)", "relationship": "FOUNDED_AS_INSTRUMENT_OF", "note": "ITI was founded in 1948 as an instrument for rebuilding cultural bridges between nations that had been at war — the theatre world's contribution to post-WWII peace-building"}
        ],
    }),

    ("auschwitz-jewish-center", {
        "summary": (
            "The Auschwitz Jewish Center (AJC, est. 2000, Oświęcim, Poland — founded by the Museum of Jewish Heritage, New York) is a museum, cultural centre, and memorial institution dedicated to the Jewish history of Oświęcim (Yiddish: Oyshnits) — the Polish town whose Jewish community was destroyed in the Holocaust — and to Holocaust education, memory, and dialogue. The Centre operates in the only surviving pre-war synagogue in Oświęcim, the Chevra Lomdei Mishnayot synagogue, restored after decades of Communist neglect.\n\n"
            "The Auschwitz Jewish Center was established to tell the story of Oświęcim's Jewish community — which numbered 8,000 before WWII (60% of the town's population) and was entirely annihilated — and to counterbalance the narrative of Auschwitz as purely a site of German crimes against humanity with the prior story of the living Jewish community that existed there for centuries before the Nazis arrived. The Centre's mission is to teach visitors about the full life cycle of the Oświęcim Jewish community: birth, education, community, religious life, and culture — not only death.\n\n"
            "The Auschwitz Jewish Center is the only institution in the world physically located in Oświęcim (as distinct from the Auschwitz-Birkenau State Museum) dedicated to Jewish life rather than Nazi death — a distinction that makes it a unique site of both memorial witnessing and life-affirming cultural renewal, challenging the reduction of Jewish identity to victimhood."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Holocaust memorial and Jewish cultural institution (est. 2000, Oświęcim/Yiddish: Oyshnits, Poland); founded by Museum of Jewish Heritage, New York; Oświęcim Jewish community — 8,000 before WWII (60% of town), entirely annihilated; operates in only surviving pre-war synagogue (Chevra Lomdei Mishnayot, restored); unique mission: Jewish life not only Jewish death; challenges reduction of Jewish identity to victimhood; Holocaust education and memory.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The post-1989 opening of Poland to Jewish heritage tourism — and the discovery that Oświęcim's Jewish community history had been entirely erased by Communist neglect — created the imperative for a dedicated institution to preserve, research, and teach the pre-war Jewish history of Oświęcim",
            "The Museum of Jewish Heritage New York's recognition that Auschwitz's overwhelming association with Nazi genocide had erased the memory of the Jewish community that had lived there for centuries — and that a new institution was needed to tell the story of Jewish life, not only Jewish death — drove the founding of the AJC",
            "The discovery and restoration of the Chevra Lomdei Mishnayot synagogue — the only surviving pre-war synagogue in Oświęcim, which had been used as a carpet warehouse during the Communist period — provided the physical site that made the Centre possible"
        ],
        "effects": [
            "The Auschwitz Jewish Center's educational programmes — reaching thousands of young Poles, Israelis, Americans, and Europeans annually — have shifted the narrative of Auschwitz from purely a site of Nazi crimes to a site of a vibrant pre-war Jewish community, changing how visitors understand the Holocaust's destruction of Jewish life",
            "The Centre's model of 'Jewish life, not only Jewish death' — combining memorial witnessing with cultural renewal — has influenced Holocaust memorial institutions worldwide, establishing a template for how sites of genocide can honour victims without reducing their entire identity to victimhood",
            "The restoration of the Chevra Lomdei Mishnayot synagogue — and its operation as a functioning Jewish cultural space in Oświęcim — represents one of the most significant acts of post-Communist Jewish cultural renewal in Poland, demonstrating that Jewish life can coexist with Holocaust memory",
            "The Auschwitz Jewish Center's dialogue programmes — bringing together Polish and Jewish youth, and building connections between Oświęcim's contemporary Polish community and the Jewish diaspora — have contributed to the Polish-Jewish reconciliation process that has been one of the most significant developments in post-Communist Central European culture"
        ],
        "relationships": [
            {"entity": "Oświęcim Jewish community (8,000 members, annihilated)", "relationship": "DEDICATED_TO_THE_MEMORY_AND_LIFE_OF_THE", "note": "The Centre tells the story of Oświęcim's Jewish community — 8,000 people, 60% of the town's population before WWII — entirely destroyed in the Holocaust"},
            {"entity": "Museum of Jewish Heritage, New York (founding institution)", "relationship": "FOUNDED_BY_THE", "note": "The Museum of Jewish Heritage (New York) founded the Auschwitz Jewish Center (2000) to tell the story of Jewish life in Oświęcim beyond Nazi genocide"},
            {"entity": "Chevra Lomdei Mishnayot synagogue (only surviving pre-war synagogue)", "relationship": "OPERATES_IN_THE", "note": "The Centre operates in the only surviving pre-war synagogue in Oświęcim — restored from Communist-era use as a carpet warehouse"},
            {"entity": "Auschwitz-Birkenau State Museum (adjacent site)", "relationship": "UNIQUE_COMPLEMENT_TO_THE", "note": "The AJC is the only institution in Oświęcim dedicated to Jewish life rather than Nazi death — providing a unique counterbalance to the Auschwitz-Birkenau State Museum"},
            {"entity": "Polish-Jewish reconciliation (post-1989)", "relationship": "INSTITUTIONAL_CONTRIBUTION_TO", "note": "The Centre's dialogue programmes have contributed to the Polish-Jewish reconciliation process — one of the most significant developments in post-Communist Central European culture"}
        ],
    }),

    ("academy-of-arts-berlin", {
        "summary": (
            "The Academy of Arts, Berlin (Akademie der Künste, est. 1696 — founded by Elector Frederick III of Brandenburg as the 'Königliche Academie der Maler, Bildhauer und Architecten') is Germany's supreme artistic institution — the oldest cultural academy in Germany and one of the oldest in the world, founded 327 years ago by the future King Frederick I of Prussia to make Berlin a centre of European art. The Berlin Academy has survived the Holy Roman Empire, the Kingdom of Prussia, the German Empire, the Weimar Republic, Nazi suppression, division between East and West Berlin, and reunification — making its history a mirror of German political history since the 17th century.\n\n"
            "The Academy was founded by Elector Frederick III in 1696 — modelled on the French Académie royale de peinture et de sculpture (1648) — as part of his programme to transform Brandenburg-Prussia from a minor German electorate into a major European power. Andreas Schlüter (sculptor of the Equestrian Statue of Frederick William I) was the Academy's first director, and its founding reflected Frederick's ambition to make Berlin a cultural capital comparable to Paris or Vienna.\n\n"
            "The Academy's most significant modern period was the Weimar Republic (1919–1933) — when it became the centre of German Expressionism, modernist architecture, and the avant-garde, with members including Max Liebermann, Heinrich Mann, Käthe Kollwitz, Arnold Schoenberg, and Bertolt Brecht — and its subsequent transformation under Nazi rule, when 'degenerate' modernist members were expelled."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Germany's supreme artistic institution (est. 1696, 327 years); oldest cultural academy in Germany; founded by Elector Frederick III (future King Frederick I of Prussia); modelled on French Académie royale; Andreas Schlüter first director; survived Holy Roman Empire, Prussia, German Empire, Weimar Republic, Nazi suppression, Berlin division, reunification; Weimar Republic members: Liebermann, Heinrich Mann, Käthe Kollwitz, Schoenberg, Brecht; Nazi expulsion of 'degenerate' members.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Elector Frederick III's ambition to transform Brandenburg-Prussia from a minor German electorate into a major European power — and his use of arts patronage to create the cultural infrastructure of a great capital — drove the founding of the Academy (1696) modelled on the French Académie royale",
            "The French Académie royale de peinture et de sculpture's model — which demonstrated that a royal academy could both train artists and legitimise an absolutist ruler's cultural patronage — provided the blueprint that Frederick III adopted for Berlin",
            "The Weimar Republic's commitment to the arts and modernism — and the Academy's opening to the German avant-garde under Max Liebermann's presidency — transformed it from a conservative academic institution into a centre of European modernism, before Nazi censorship reversed this transformation"
        ],
        "effects": [
            "The Academy's Weimar Republic membership — Käthe Kollwitz (first female member), Arnold Schoenberg, Bertolt Brecht, Heinrich Mann — represented the highest concentration of German modernist talent in any institution of the period, making the Academy's history a record of Weimar Germany's artistic golden age",
            "The Nazi 'Gleichschaltung' of the Academy (1933) — forcing the expulsion or resignation of all modernist, Jewish, and politically unacceptable members — destroyed the Weimar Academy's extraordinary membership and represented the Nazi state's most dramatic act of cultural censorship against German modernism",
            "The Academy's Cold War division — operating in West Berlin (as the Akademie der Künste West) and East Berlin (as the Deutsche Akademie der Künste) simultaneously — made it a unique institution in German cultural life: a single historical institution divided along the Iron Curtain, reunified after 1990",
            "The reunified Academy's role in contemporary German cultural policy — maintaining its tradition of defending artistic freedom, supporting politically engaged art, and serving as the institutional voice of German artistic life — has given it a continuing significance as Germany's premier arts institution in the 21st century"
        ],
        "relationships": [
            {"entity": "Elector Frederick III (later King Frederick I of Prussia, founder)", "relationship": "FOUNDED_BY", "note": "Frederick III founded the Academy (1696) as part of his programme to make Berlin a European cultural capital — modelled on the French Académie royale"},
            {"entity": "Weimar Republic (1919–1933, modernist golden age)", "relationship": "REACHED_MODERNIST_PEAK_DURING_THE", "note": "The Weimar Republic period — with members Liebermann, Kollwitz, Schoenberg, Brecht, Mann — represented the Academy as the centre of German modernism"},
            {"entity": "Nazi Gleichschaltung (1933, expulsion of modernists)", "relationship": "PURGED_OF_MODERNIST_MEMBERS_BY_THE_NAZI", "note": "The 1933 Nazi Gleichschaltung forced the expulsion of all Jewish, modernist, and politically unacceptable members — destroying the Weimar Academy's extraordinary membership"},
            {"entity": "Cold War Berlin division (Academy divided East/West)", "relationship": "DIVIDED_INTO_EAST_AND_WEST_INSTITUTIONS_DURING_THE", "note": "The Academy operated as two separate institutions during the Cold War — West Berlin's Akademie der Künste and East Berlin's Deutsche Akademie der Künste — reunified after 1990"},
            {"entity": "Käthe Kollwitz (first female member)", "relationship": "ELECTED_AS_FIRST_FEMALE_MEMBER_OF_THE", "note": "Käthe Kollwitz's election as the Academy's first female member (Weimar period) was a landmark in German arts institutional history"}
        ],
    }),

    ("book-institute", {
        "summary": (
            "The Book Institute (Instytut Książki, est. 2004, Kraków, Poland — founded by the Polish Ministry of Culture) is Poland's national institution for book culture and the primary instrument of Polish literary diplomacy — the organisation responsible for promoting Polish literature internationally, funding translations of Polish literature into foreign languages, and connecting Polish authors with international publishers, festivals, and readers. The Book Institute's Translation Programme has funded the translation of Polish literature into 50+ languages, making it one of the most successful national literary translation programmes in the world.\n\n"
            "The Book Institute was established in 2004 — as Poland joined the European Union — with the explicit mission of promoting Polish literary culture internationally at the moment when Poland was entering the mainstream of European cultural life. The Institute quickly became known for its©Poland Translation Programme, which provides financial subsidies to foreign publishers to translate Polish literature — a model that has been adopted by other Central European countries seeking to make their national literatures accessible to international audiences.\n\n"
            "The Book Institute's most visible international platform is its presence at major book fairs — Frankfurt, London, Bologna — where it presents Polish literature to international publishers and agents, and its administration of the Warsaw Book Fair. The Institute has played a significant role in the international recognition of Polish literature, contributing to the Nobel Prize in Literature recognition of Olga Tokarczuk (2018) and the international success of authors including Ryszard Kapuściński, Wisława Szymborska, and Andrzej Sapkowski."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Poland's national institution for book culture and literary diplomacy (est. 2004, Kraków, Ministry of Culture); ©Poland Translation Programme — translations of Polish literature into 50+ languages, one of world's most successful national literary translation programmes; founded when Poland joined EU (2004); Frankfurt/London/Bologna book fair presence; contributed to Olga Tokarczuk's Nobel Prize in Literature (2018); Warsaw Book Fair administration; model for Central European literary diplomacy.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Poland's accession to the European Union (1 May 2004) — and the Polish government's recognition that full participation in European cultural life required active promotion of Polish literature internationally — drove the founding of the Book Institute at the moment of EU membership",
            "The recognition that Polish literature — including Nobel laureates Czesław Miłosz (1980) and Wisława Szymborska (1996) — was poorly known internationally because of the limited availability of Polish literary translations, creating the imperative for a dedicated translation funding programme",
            "The Polish Ministry of Culture's understanding that cultural diplomacy — promoting Polish literature, history, and culture internationally — was an essential complement to political and economic diplomacy, particularly given Poland's complex relationships with Germany and Russia"
        ],
        "effects": [
            "The ©Poland Translation Programme — which has funded translations of Polish literature into 50+ languages, resulting in 3,000+ translation publications over 20 years — has made Polish literature accessible to international readers on a scale not previously possible, transforming Poland's position in world literature",
            "The Book Institute's promotional work contributed to the international recognition that culminated in Olga Tokarczuk's Nobel Prize in Literature (2018) — the first Polish Nobel in Literature since Szymborska (1996) — demonstrating the long-term value of systematic literary diplomacy",
            "The Book Institute's model — a national institution specifically dedicated to funding translations and promoting literature internationally — has been adopted by other Central and Eastern European countries seeking to make their national literatures accessible, establishing Poland as the pioneer of systematic post-Communist literary diplomacy",
            "The Book Institute's promotion of Ryszard Kapuściński (considered for the Nobel), Andrzej Sapkowski (The Witcher series), and contemporary Polish authors has diversified the international image of Polish culture beyond Holocaust memory and Solidarity politics to include literary achievement and cultural creativity"
        ],
        "relationships": [
            {"entity": "Polish Ministry of Culture (founding body)", "relationship": "FOUNDED_AND_FUNDED_BY_THE", "note": "The Book Institute was established by the Polish Ministry of Culture (2004) as Poland's national instrument of literary diplomacy"},
            {"entity": "©Poland Translation Programme (50+ languages)", "relationship": "ADMINISTERS_THE_FLAGSHIP", "note": "The ©Poland Translation Programme — funding translations into 50+ languages — is the Book Institute's primary instrument for making Polish literature internationally accessible"},
            {"entity": "Olga Tokarczuk (Nobel Prize in Literature 2018)", "relationship": "CONTRIBUTED_TO_THE_INTERNATIONAL_RECOGNITION_CULMINATING_IN", "note": "The Book Institute's promotional work contributed to the international recognition that culminated in Tokarczuk's Nobel Prize (2018)"},
            {"entity": "EU accession of Poland (1 May 2004)", "relationship": "FOUNDED_AT_THE_MOMENT_OF_POLAND'S", "note": "The Book Institute's founding (2004) was explicitly timed to coincide with Poland's EU accession — as the cultural diplomacy instrument for Poland's full entry into European cultural life"},
            {"entity": "Frankfurt Book Fair (annual, world's largest)", "relationship": "MAINTAINS_PROMINENT_ANNUAL_PRESENCE_AT_THE", "note": "The Book Institute's Frankfurt Book Fair presence — presenting Polish literature to international publishers and agents — is its primary annual international platform"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 35 — {len(ENTITIES)} entities (Class 345: Cultural Institutions)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
