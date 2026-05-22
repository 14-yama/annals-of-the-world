#!/usr/bin/env python3
"""
Batch 36 — 8 entities (Class 361): World-Famous Museums
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/361-Class-361"
FILE_PREFIX = "361"


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

    ("smithsonian-institution", {
        "summary": (
            "The Smithsonian Institution (est. 1846, Washington, D.C. — founded by an Act of Congress using the bequest of British scientist James Smithson) is the world's largest museum, education, and research complex — 19 museums, 21 libraries, 9 research centres, 1 zoo, and 2 art galleries, housing 154 million objects, specimens, and works of art. The Smithsonian is the primary custodian of American national culture and natural history, operating entirely with federal and private funding and providing free admission — making it the most visited museum complex in the world (30 million visitors annually).\n\n"
            "The Smithsonian's founding is one of history's most improbable institutional origin stories: James Smithson (1765–1829) — an English chemist, Fellow of the Royal Society, and illegitimate son of the Duke of Northumberland — bequeathed his entire fortune to 'the United States of America, to found at Washington, under the name of the Smithsonian Institution, an Establishment for the increase and diffusion of knowledge.' Smithson had never visited America; his bequest was contested by his English relatives; and Congress debated for 8 years whether to accept foreign money before establishing the Institution in 1846.\n\n"
            "The Smithsonian's 19 museums include the National Air and Space Museum (the world's most visited museum), the National Museum of Natural History (the world's most visited natural history museum), the National Museum of American History, and the National Museum of African American History and Culture (opened 2016). Its research programme — including astrophysics, oceanography, and tropical biology — makes it one of the world's largest research complexes alongside its museum function."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest museum, education, and research complex (est. 1846, founded by bequest of British scientist James Smithson); 19 museums, 21 libraries, 9 research centres, 1 zoo, 154 million objects; world's most visited museum complex (30 million annually); free admission; National Air and Space Museum (world's most visited museum); National Museum of Natural History (world's most visited natural history museum); National Museum of African American History and Culture (2016); primary custodian of American national culture.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "James Smithson's unexpected bequest to the United States (1829) — of his entire fortune (£100,000 in gold sovereigns, equivalent to ~$11 million today) to found an institution 'for the increase and diffusion of knowledge' — was the singular act that created the Smithsonian, and the mystery of why a British scientist with no American connections chose to benefit the United States remains unsolved",
            "Congress's 8-year debate (1836–1846) over whether to accept foreign money for a public institution — and the eventual decision to use the Smithson bequest to create a national scientific and educational institution in Washington — reflected the new republic's ambivalence about public cultural institutions and its eventual commitment to science and education as national values",
            "The 19th-century American policy of building national cultural identity through public institutions — museums, libraries, universities — created the institutional context in which the Smithsonian grew from a single building to the world's largest museum complex"
        ],
        "effects": [
            "The Smithsonian's 19 museums and free admission policy — funded by Congress — established the American model of free public museum access that distinguishes the major American national museums from the largely fee-charging European model, making cultural access a democratic right rather than a commercial transaction",
            "The National Air and Space Museum — the world's most visited museum (9 million annually) — houses the Wright Brothers' Flyer, Charles Lindbergh's Spirit of St. Louis, John Glenn's Mercury capsule, and Apollo 11 command module Columbia, making it the physical archive of American aviation and space exploration achievement",
            "The National Museum of African American History and Culture (opened 2016) — the only national museum dedicated to documenting African American life, history, and culture — represents the Smithsonian's most significant recent expansion, and its 3-year waiting list upon opening reflected the long-suppressed demand for an institution that centred African American experience in American national history",
            "The Smithsonian's research programmes — including the Smithsonian Astrophysical Observatory (operating the Chandra X-ray Center), the Smithsonian Tropical Research Institute (Barro Colorado Island, Panama), and the Smithsonian Environmental Research Center — make it one of the world's largest multi-disciplinary research complexes alongside its public museum function"
        ],
        "relationships": [
            {"entity": "James Smithson (bequest founder)", "relationship": "FOUNDED_BY_THE_BEQUEST_OF", "note": "Smithson's bequest (1829) — of his entire fortune to the United States, a country he never visited — is the improbable origin story of the world's largest museum complex"},
            {"entity": "National Air and Space Museum (world's most visited museum)", "relationship": "INCLUDES_THE", "note": "The National Air and Space Museum — housing Wright Brothers' Flyer, Lindbergh's Spirit of St. Louis, Apollo 11 command module — is the world's most visited museum (9 million annually)"},
            {"entity": "National Museum of African American History and Culture (2016)", "relationship": "OPENED_THE", "note": "The NMAAHC (2016) — the only national museum dedicated to African American life — had a 3-year waiting list upon opening, reflecting long-suppressed demand"},
            {"entity": "U.S. Congress (annual funding)", "relationship": "FUNDED_BY_ACTS_OF", "note": "Congressional funding supports the Smithsonian's free admission policy — making cultural access a democratic right and distinguishing the American model from fee-charging European museums"},
            {"entity": "Smithsonian Astrophysical Observatory (Chandra X-ray Center)", "relationship": "OPERATES_THE_MAJOR_SCIENTIFIC_RESEARCH_PROGRAMME_OF_THE", "note": "The Smithsonian's research complex — including astrophysics, tropical biology, and oceanography — makes it one of the world's largest multi-disciplinary research organisations"}
        ],
    }),

    ("hermitage-museum", {
        "summary": (
            "The State Hermitage Museum (Государственный Эрмитаж, Gosudarstvennyy Ermitazh, est. 1764, St. Petersburg — founded by Empress Catherine the Great) is one of the world's greatest art museums — the largest art museum in the world by gallery space (322 rooms, 66,842 sq m), housing the most important collection of Western European art in Russia, the largest collection of Scythian gold in the world, and 3 million objects spanning all civilisations. The Hermitage occupies the Winter Palace (the former official residence of the Russian Tsars) — one of the most magnificent Baroque palaces in the world.\n\n"
            "Catherine the Great founded the Hermitage in 1764 — the name means 'place of solitude' — as a private repository for her art collection, initially purchasing 225 paintings from the Berlin merchant Johann Ernst Gotzkowski (originally assembled for Frederick the Great of Prussia, who declined to pay for them). Catherine's collection grew through systematic purchases of entire European collections: the Brühl collection (Dresden, 1769), the Crozat collection (Paris, 1772), the Walpole collection (Houghton Hall, England, 1779) — making the Hermitage the primary repository of European masterworks outside Western Europe.\n\n"
            "The Hermitage's collection of 3 million objects includes Rembrandt's most important late works, Leonardo da Vinci's Benois Madonna and Litta Madonna, Raphael's Holy Family, and Titian's Danaë — as well as the largest collection of Impressionist and Post-Impressionist art outside Paris (assembled by Russian merchants Shchukin and Morozov before WWI and nationalised by the Bolsheviks)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of world's greatest art museums (est. 1764, Catherine the Great); largest art museum by gallery space (322 rooms, 66,842 sq m); 3 million objects; Winter Palace (Baroque palace, former Tsarist residence); Rembrandt late works, Leonardo's Benois Madonna and Litta Madonna, Raphael's Holy Family, Titian's Danaë; largest Impressionist collection outside Paris (Shchukin/Morozov, nationalised by Bolsheviks); largest Scythian gold collection; primary repository of European masterworks outside Western Europe.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Catherine the Great's cultural ambition — to make Russia a equal participant in European civilisation through the acquisition of European art — drove the systematic purchase of entire European collections (Brühl, Crozat, Walpole) that created the Hermitage as a world-class institution",
            "The Bolshevik nationalisation of private art collections (1917) — especially the extraordinary Impressionist and Post-Impressionist collections of Sergei Shchukin and Ivan Morozov (Matisse, Picasso, Cézanne, Monet, Gauguin) — added a second great wave of masterworks to the Hermitage, transforming it from primarily an Old Master collection into one of the world's greatest repositories of modern art",
            "The Winter Palace's conversion from an imperial residence to a public museum (1917) — opening the Tsarist collection to the Soviet public — was the foundational act of Bolshevik cultural democratisation, even as it was combined with the destruction of private cultural ownership"
        ],
        "effects": [
            "The Hermitage's preservation of its collection during the 900-day Siege of Leningrad (1941–1944) — when museum staff evacuated 1.2 million objects to the Ural Mountains before the German encirclement and then lived in the empty display cases through the siege — is one of the most extraordinary stories of cultural preservation under existential threat in history",
            "The Hermitage's Impressionist and Post-Impressionist collection — the largest outside Paris — was assembled before WWI by Russian merchants who were among the first buyers of Matisse and Picasso; hidden from Western scholars during the Soviet period, it was revealed to the world after 1991, transforming art historians' understanding of early modernism's collector base",
            "The Hermitage's 3 million-object collection — of which only 60,000 objects are on display at any time — represents one of the world's greatest under-examined treasure troves, with entire floors of the Winter Palace storage accessible only to researchers",
            "The Winter Palace's architectural magnificence — the Baroque facade, the Jordan Staircase, the Malachite Room, the Gold Drawing Room — makes the Hermitage a masterwork of palatial architecture as well as an art repository, with the building itself as significant as its contents"
        ],
        "relationships": [
            {"entity": "Catherine the Great (founder 1764)", "relationship": "FOUNDED_BY", "note": "Catherine the Great founded the Hermitage (1764) through systematic purchase of European art collections — expressing her ambition to make Russia a full participant in European civilisation"},
            {"entity": "Winter Palace (St. Petersburg, Baroque Tsarist palace)", "relationship": "HOUSED_WITHIN_THE", "note": "The Hermitage occupies the Winter Palace — the former official residence of the Russian Tsars and one of the world's most magnificent Baroque palaces"},
            {"entity": "Shchukin and Morozov Impressionist collections (nationalised 1917)", "relationship": "HOLDINGS_TRANSFORMED_BY_BOLSHEVIK_NATIONALISATION_OF_THE", "note": "The Bolshevik nationalisation of Shchukin's and Morozov's Impressionist collections (1917) added the world's greatest collection of Matisse and Picasso outside Paris"},
            {"entity": "Siege of Leningrad (1941–1944, 900 days)", "relationship": "SURVIVED_WITH_ITS_COLLECTION_THROUGH_THE", "note": "The Hermitage's preservation during the 900-day Siege — with 1.2 million objects evacuated and staff living in empty display cases — is one of history's greatest acts of cultural preservation"},
            {"entity": "Leonardo da Vinci (Benois Madonna, Litta Madonna)", "relationship": "CUSTODIAN_OF_TWO_AUTHENTICATED_WORKS_BY", "note": "The Hermitage holds two authenticated Leonardo da Vinci paintings — the Benois Madonna and Litta Madonna — making it one of the few institutions outside Italy with authenticated Leonardo works"}
        ],
    }),

    ("acropolis-museum", {
        "summary": (
            "The Acropolis Museum (Μουσείο Ακρόπολης, est. 2009, Athens — designed by Bernard Tschumi Architects) is one of the world's greatest archaeology museums — built at the foot of the Acropolis rock to house and display the sculptures, artefacts, and architectural elements of the Acropolis of Athens (5th–4th century BCE), especially the Parthenon frieze sculptures, the Erechtheion Caryatids, and the Nike Temple parapet. The museum's purpose is explicitly political as well as cultural: it was designed to make a definitive case for the repatriation of the Elgin Marbles from the British Museum.\n\n"
            "The Acropolis Museum was opened on 20 June 2009 by Prime Minister Kostas Karamanlis — after three decades of architectural competitions, political disputes, and construction delays — as Greece's most significant cultural project since independence. The museum's design by Bernard Tschumi is architecturally brilliant: the top floor (the Parthenon Gallery) is aligned at exactly the same angle and orientation as the Parthenon itself, allowing natural light to fall on the frieze sculptures from the same direction as they would receive it if on the temple — and the glass walls provide a direct visual connection to the Parthenon on the Acropolis above.\n\n"
            "The museum's Parthenon Gallery displays the surviving frieze panels alongside plaster casts of the Elgin Marbles (held in the British Museum since 1816) — the juxtaposition of originals and casts making an inescapable argument for reunification. Greece's request for the return of the Elgin Marbles is the most significant ongoing cultural property dispute in the world."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of world's greatest archaeology museums (est. 2009, Bernard Tschumi design); houses Parthenon frieze sculptures, Erechtheion Caryatids, Nike Temple parapet; Parthenon Gallery aligned at exact angle/orientation as the Parthenon with glass walls to the hill; plaster casts of Elgin Marbles juxtaposed with originals — political argument for repatriation; world's most significant ongoing cultural property dispute (Elgin Marbles, British Museum since 1816); 4,000 objects from the Acropolis.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Greek government's need for a world-class museum to house the Acropolis sculptures — after decades of displaying them in inadequate facilities — and its strategic decision to use a new museum as evidence that Athens could properly care for the Elgin Marbles drove the long-delayed project",
            "Greece's decades-long campaign for the return of the Elgin Marbles — which had used the absence of adequate facilities as the primary British argument for retention — required a definitive rebuttal in the form of a world-class museum explicitly designed to reunite the Parthenon sculptures",
            "Bernard Tschumi's architectural concept — aligning the Parthenon Gallery at the exact angle and orientation of the Parthenon and providing glass walls for a direct visual connection to the temple — created an argument for repatriation embedded in the building's very design"
        ],
        "effects": [
            "The Acropolis Museum's opening (2009) — and the Parthenon Gallery's juxtaposition of original Parthenon sculptures with plaster casts of the Elgin Marbles — has intensified and reframed the repatriation debate, making the argument for reunification visually and intellectually irresistible to an increasing number of international museum professionals",
            "The museum's 4,000 objects — including all six Erechtheion Caryatids (one is in the British Museum), the Nike Temple parapet, and the finest Archaic Greek sculpture collection in the world — make it the primary destination for the study of 5th-century BCE Athenian art",
            "The Acropolis Museum has become the model for the 'contextual museum' movement — the argument that archaeological objects should be displayed in the landscape context in which they were created and found, rather than extracted to distant encyclopaedic museums — with implications for repatriation debates worldwide",
            "The museum's commercial success (2 million visitors annually) and critical acclaim have demonstrated that a purpose-built archaeological museum can be both a world-class cultural institution and a politically effective argument for repatriation, transforming the terms of the Elgin Marbles debate"
        ],
        "relationships": [
            {"entity": "Parthenon (Acropolis of Athens, 5th century BCE)", "relationship": "DISPLAYS_THE_SURVIVING_SCULPTURES_OF_THE", "note": "The museum was built specifically to house the Parthenon frieze sculptures and other Acropolis objects — and the Parthenon Gallery is architecturally aligned with the temple above"},
            {"entity": "Elgin Marbles (British Museum since 1816)", "relationship": "MAKES_THE_PRIMARY_VISUAL_ARGUMENT_FOR_THE_RETURN_OF_THE", "note": "The museum's juxtaposition of original Parthenon sculptures with plaster casts of the Elgin Marbles makes an inescapable argument for reunification"},
            {"entity": "Bernard Tschumi Architects (designer)", "relationship": "DESIGNED_BY", "note": "Bernard Tschumi's design — with the Parthenon Gallery aligned to the temple's exact angle and orientation — is itself an architectural argument for repatriation"},
            {"entity": "Erechtheion Caryatids (5 in museum, 1 in British Museum)", "relationship": "HOUSES_FIVE_OF_THE_SIX", "note": "The museum displays five of the six Erechtheion Caryatids — the sixth is in the British Museum, making their separation an ongoing symbol of the repatriation debate"},
            {"entity": "Greece (state patron and repatriation advocate)", "relationship": "STATE_INSTITUTION_OF", "note": "The Acropolis Museum is Greece's most significant cultural project since independence — and its primary instrument in the campaign for the Elgin Marbles' return"}
        ],
    }),

    ("palace-museum", {
        "summary": (
            "The Palace Museum (故宫博物院, Gùgōng Bówùyuàn, est. 1925, Beijing — established in the Forbidden City after the abdication of Emperor Puyi) is one of the world's most visited and historically significant museums — the repository of the Chinese imperial collections assembled over 600 years of Ming and Qing imperial patronage, housed in the Forbidden City (the world's largest palace complex, a UNESCO World Heritage Site). The Palace Museum's 1.86 million objects — including Chinese ceramics, paintings, bronzes, jades, calligraphy, and imperial artefacts — constitute the most comprehensive collection of Chinese imperial art in the world.\n\n"
            "The Palace Museum was established in 1925 after the Republic of China expelled Puyi from the Forbidden City — opening the imperial palace and its treasures to the public for the first time in its 500-year history. In 1933, anticipating Japanese invasion, the Palace Museum evacuated 13,491 boxes of treasures to southern China, then to Sichuan province — a journey of 10,000 miles over 12 years. After WWII, the Nationalist government removed 2,972 boxes to Taiwan (1949), where they became the core of the National Palace Museum in Taipei.\n\n"
            "The Palace Museum (Beijing) and the National Palace Museum (Taipei) thus both claim to represent the authentic imperial Chinese collection — a division that reflects the Chinese Civil War and continues to symbolise the political dispute between the People's Republic and the Republic of China."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of world's most visited and historically significant museums (est. 1925, Forbidden City, Beijing); 1.86 million objects — most comprehensive Chinese imperial art collection; Forbidden City (UNESCO World Heritage Site, world's largest palace complex); 13,491 boxes evacuated from Japanese invasion (1933); 2,972 boxes taken to Taiwan (1949) — became National Palace Museum Taipei; Beijing/Taipei split reflects Chinese Civil War; 17 million annual visitors (world's most visited museum); 600 years of Ming and Qing imperial patronage.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Republic of China's expulsion of Emperor Puyi from the Forbidden City (1924) — and the decision to open the imperial palace and its collections to the public as a national museum — was the foundational act that established the Palace Museum as a public institution and democratic inheritance of the imperial past",
            "The Japanese invasion of China (1931–1937) created the existential threat that drove the Palace Museum's extraordinary evacuation of 13,491 boxes of treasures — a logistical feat that preserved the imperial collection at the cost of 12 years of displacement",
            "The Chinese Civil War's outcome — the Nationalist (KMT) defeat and retreat to Taiwan (1949), taking 2,972 boxes of the most portable treasures — created the permanent division of the imperial collection between Beijing and Taipei that reflects the unresolved political status of Taiwan"
        ],
        "effects": [
            "The Palace Museum is the world's most visited museum (17 million visitors annually) — surpassing the Louvre — making the Forbidden City the world's most attended cultural site and Beijing's primary tourist attraction",
            "The evacuation of the imperial collection (1933) and its eventual return to Beijing (1950s) — and the parallel establishment of the National Palace Museum in Taipei — created a unique situation in world museum history: two institutions, both claiming to represent the authentic Chinese imperial tradition, reflecting a political dispute that has never been resolved",
            "The Palace Museum's programme of digital access — the Digital Palace Museum project, making 500,000 artefacts available online — has been one of the world's most ambitious digitisation efforts, democratising access to Chinese cultural heritage",
            "The Forbidden City's architectural complex — the world's largest palace, with 9,999 rooms in the traditional count — preserved intact after the Ming and Qing dynasties makes it the most complete surviving example of Chinese imperial architecture, and its inscription as a UNESCO World Heritage Site (1987) has protected it from urban development"
        ],
        "relationships": [
            {"entity": "Forbidden City (UNESCO World Heritage Site, world's largest palace)", "relationship": "HOUSED_WITHIN_THE", "note": "The Palace Museum occupies the Forbidden City — the world's largest palace complex and a UNESCO World Heritage Site — making the building itself as significant as the collection"},
            {"entity": "Emperor Puyi (expelled 1924)", "relationship": "ESTABLISHED_AFTER_EXPULSION_OF_THE_LAST_EMPEROR", "note": "The Republic of China's expulsion of Puyi (1924) and opening of the Forbidden City to the public established the Palace Museum as a democratic institution"},
            {"entity": "National Palace Museum, Taipei (2,972 boxes taken 1949)", "relationship": "COLLECTION_DIVIDED_BETWEEN_BEIJING_INSTITUTION_AND_THE", "note": "The KMT's removal of 2,972 boxes to Taiwan (1949) created the Taipei National Palace Museum — a permanent division reflecting the Chinese Civil War's unresolved political legacy"},
            {"entity": "Japanese invasion (1933, drove evacuation)", "relationship": "IMPERIAL_COLLECTION_EVACUATED_TO_PROTECT_IT_FROM_THE", "note": "The Japanese invasion threat drove the evacuation of 13,491 boxes of treasures (1933) — preserving the imperial collection at the cost of 12 years of displacement"},
            {"entity": "Chinese imperial ceramics (most comprehensive collection)", "relationship": "HOUSES_THE_WORLD'S_MOST_COMPREHENSIVE_COLLECTION_OF", "note": "The Palace Museum's 1.86 million objects — including the most comprehensive collection of Chinese imperial ceramics — constitute the world's primary repository of Chinese imperial artistic heritage"}
        ],
    }),

    ("national-museum-of-anthropology", {
        "summary": (
            "The National Museum of Anthropology (Museo Nacional de Antropología, est. 1964, Mexico City — designed by Pedro Ramírez Vázquez) is the most important museum in the Americas for pre-Columbian cultures — the world's largest anthropological museum, with 23 exhibition halls and 600,000+ objects covering 40 millennia of Mexican and Mesoamerican history. The museum's centrepiece is the Aztec Sun Stone (the 'Aztec Calendar'), but its collections span all major Mesoamerican civilisations: Olmec, Maya, Teotihuacan, Toltec, Mixtec, and Aztec.\n\n"
            "The museum was opened on 17 September 1964 by President Adolfo López Mateos in Chapultepec Park — one of the world's great park settings for a museum — in a building considered a masterpiece of modernist Mexican architecture. Pedro Ramírez Vázquez's design incorporates pre-Columbian architectural references in a modernist idiom — the central courtyard with its single giant mushroom-shaped column (the tlaloc pillar, 11 metres in diameter, supporting the roof of the entire courtyard) represents a uniquely Mexican fusion of indigenous cultural reference and modernist structural engineering.\n\n"
            "The museum's famous January 1985 theft — when five men broke in and removed 140 objects, including a jade Zapotec funeral mask and a Monte Albán funerary urn — and their recovery three years later (most objects intact) is considered one of the greatest art heist recoveries in Mexican cultural history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most important pre-Columbian cultures museum in the Americas (est. 1964, Mexico City); world's largest anthropological museum; 23 halls, 600,000+ objects, 40 millennia of Mesoamerican history; Aztec Sun Stone ('Aztec Calendar'); Olmec, Maya, Teotihuacan, Toltec, Mixtec, and Aztec collections; Pedro Ramírez Vázquez modernist design with pre-Columbian references; Chapultepec Park; 1985 theft of 140 objects — 3-year recovery; 2 million annual visitors.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Mexican government's post-Revolutionary programme of indigenismo — celebrating pre-Columbian civilisation as the authentic foundation of Mexican national identity — drove the creation of a world-class museum to honour the pre-Columbian past and assert Mexico's cultural depth",
            "The need to centralise and protect Mexico's dispersed pre-Columbian collections — many held in inadequate regional facilities or vulnerable to looting — drove the decision to build a new, purpose-designed institution in Mexico City",
            "Pedro Ramírez Vázquez's architectural genius — creating a building that was simultaneously modernist in structure and pre-Columbian in reference, with the tlaloc pillar as its structural and symbolic centrepiece — produced a building that has become an architectural icon in its own right"
        ],
        "effects": [
            "The National Museum of Anthropology has been the primary instrument of Mexican cultural nationalism — presenting pre-Columbian civilisation as the foundation of Mexican identity and the authentic heritage of the mestizo Mexican nation, shaping how Mexicans and the world understand pre-Columbian history",
            "The museum's Aztec Sun Stone — the most recognised object in Mexican cultural history, visited by millions annually — has made it the primary symbol of pre-Columbian civilisation in global popular consciousness, appearing on countless Mexican government seals, banknotes, and cultural products",
            "The museum's exhaustive ethnographic galleries — dedicated to Mexico's 62 living indigenous peoples — have made it a primary resource for cultural anthropology and indigenous rights advocacy, documenting cultures that are still actively endangered by linguistic and cultural assimilation",
            "The 1985 theft and recovery demonstrated both the vulnerability of archaeological museum collections to sophisticated heist and the persistence of the Mexican cultural community in recovering national heritage — becoming a model case study for museum security and cultural property recovery"
        ],
        "relationships": [
            {"entity": "Aztec Sun Stone ('Aztec Calendar', primary object)", "relationship": "HOUSES_THE_MOST_RECOGNISED_PRE-COLUMBIAN_OBJECT", "note": "The Aztec Sun Stone — the most recognised symbol of pre-Columbian civilisation — is the museum's centrepiece and Mexico's most famous cultural object"},
            {"entity": "Pedro Ramírez Vázquez (architect)", "relationship": "DESIGNED_BY", "note": "Ramírez Vázquez's design — with the tlaloc pillar supporting the entire courtyard roof — is a masterpiece of modernist Mexican architecture fusing pre-Columbian reference and structural innovation"},
            {"entity": "Mexican indigenismo (post-Revolutionary cultural nationalism)", "relationship": "PHYSICAL_EMBODIMENT_OF", "note": "The museum was built as the primary instrument of Mexican indigenismo — celebrating pre-Columbian civilisation as the authentic foundation of Mexican national identity"},
            {"entity": "Mesoamerican civilisations (Olmec, Maya, Teotihuacan, Aztec)", "relationship": "WORLD'S_MOST_COMPREHENSIVE_SINGLE-INSTITUTION_COVERAGE_OF_THE", "note": "The museum's 23 halls cover all major Mesoamerican civilisations — from Olmec (1500 BCE) through Maya to Aztec (1521 CE) — making it the primary repository of Mesoamerican cultural heritage"},
            {"entity": "1985 theft (140 objects, recovered 1988)", "relationship": "SUBJECT_OF_ONE_OF_LATIN_AMERICA'S_GREATEST_ART_HEIST_RECOVERIES", "note": "The 1985 theft of 140 objects — including a jade Zapotec funeral mask — and their recovery three years later is a landmark in Latin American cultural heritage recovery"}
        ],
    }),

    ("national-history-museum", {
        "summary": (
            "The National History Museum (Национален исторически музей, est. 1973, Sofia, Bulgaria) is Bulgaria's largest and most important historical museum — the primary custodian of Bulgarian national cultural heritage, with 700,000+ objects spanning 8,000 years of Bulgarian and Thracian history. The museum's most celebrated collection is the Thracian gold — some of the most spectacular ancient goldwork in the world, including the Panagyurishte Treasure (4th century BCE, 9 gold vessels, 6.164 kg of pure gold) and the Letnitsa and Lukovit Treasures, which represent the peak of Thracian metallurgical achievement.\n\n"
            "The National History Museum was established in 1973 in a Communist bloc context — the Bulgarian Communist government's programme of building national cultural institutions to strengthen Bulgarian identity. In 2000, it moved to its current location in the former Boyana Residence — the Communist party's Tsarist-era palace complex in the Boyana neighbourhood of Sofia, at the foot of Vitosha Mountain — creating one of the most dramatic museum settings in southeastern Europe.\n\n"
            "The museum's collection spans the Neolithic Varna culture (the world's oldest necropolis, 4569–4340 BCE, with the world's oldest gold artefacts), Thracian civilisation, the Bulgarian Empire, the Ottoman period, the Bulgarian national revival, and the modern state — making it the most comprehensive single source for the study of Bulgarian and Thracian civilisation."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Bulgaria's largest and most important historical museum (est. 1973, Sofia); 700,000+ objects, 8,000 years of Bulgarian and Thracian history; Panagyurishte Treasure (4th century BCE, 9 gold vessels, 6.164 kg pure gold) — one of world's most spectacular ancient goldwork collections; Neolithic Varna culture (world's oldest gold artefacts, 4569–4340 BCE); Bulgarian Empire artefacts; Ottoman period collection; national revival documentation; Boyana Residence (Communist palace complex, foot of Vitosha Mountain).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Bulgarian Communist government's programme (1973) of building national cultural institutions to strengthen Bulgarian national identity — and its decision to centralise the most important national artefacts from regional museums — drove the establishment of the National History Museum",
            "Bulgaria's extraordinary archaeological wealth — the Neolithic Varna culture, the Thracian civilisation, the Bulgarian Empire — had produced an unparalleled concentration of ancient gold and cultural objects that required a national-level institution to preserve and present",
            "The decision to move the museum to the former Boyana Residence (2000) — the Communist party palace in a dramatic mountain setting — gave it one of the most prestigious and visually distinctive settings of any museum in the Balkans"
        ],
        "effects": [
            "The Panagyurishte Treasure's display — 9 gold vessels, 6.164 kg of pure gold, 4th century BCE Thracian craftsmanship — has made Bulgaria internationally known for Thracian goldwork, attracting archaeologists, art historians, and tourists who come specifically to see the most spectacular ancient gold collection in southeastern Europe",
            "The National History Museum's documentation of the Bulgarian national revival (18th–19th century) — including revolutionary leader Vasil Levski's personal effects, the April Uprising of 1876, and the liberation from Ottoman rule (1878) — makes it the primary site of Bulgarian national memory and identity",
            "The museum's Neolithic Varna culture collection — including artefacts from the world's oldest known gold-working culture (4569–4340 BCE) — has positioned Bulgaria as the origin point of European gold metallurgy, fundamentally changing the understanding of prehistoric European cultural development",
            "The museum's location in the Boyana Residence — adjacent to the Boyana Church (a UNESCO World Heritage Site with 13th-century frescoes) — has created a cultural heritage cluster that is Sofia's most important cultural tourism destination"
        ],
        "relationships": [
            {"entity": "Panagyurishte Treasure (4th century BCE Thracian gold)", "relationship": "HOUSES_THE_MOST_SPECTACULAR_OBJECT_IN_ITS_COLLECTION", "note": "The Panagyurishte Treasure — 9 gold vessels, 6.164 kg of pure gold, 4th century BCE — is the most celebrated object in the museum and one of the world's greatest ancient gold collections"},
            {"entity": "Varna Neolithic culture (world's oldest gold artefacts, 4569–4340 BCE)", "relationship": "CUSTODIAN_OF_ARTEFACTS_FROM_THE", "note": "Artefacts from the Varna culture — the world's oldest gold-working civilisation — position Bulgaria as the origin point of European gold metallurgy"},
            {"entity": "Boyana Residence (former Communist party palace)", "relationship": "LOCATED_IN_THE", "note": "The museum's move to the Boyana Residence (2000) gave it one of the most prestigious and visually dramatic settings of any museum in southeastern Europe"},
            {"entity": "Bulgarian national revival (18th–19th century)", "relationship": "PRIMARY_DOCUMENTARY_REPOSITORY_FOR_THE", "note": "The museum's national revival collection — including Vasil Levski's personal effects and April Uprising artefacts — makes it the primary site of Bulgarian national memory"},
            {"entity": "Thracian civilisation (primary archaeological collection)", "relationship": "HOUSES_THE_MOST_COMPREHENSIVE_COLLECTION_OF", "note": "The museum's Thracian collection — gold treasures, bronzes, and pottery — makes it the world's primary repository of Thracian cultural heritage"}
        ],
    }),

    ("united-states-holocaust-memorial-museum", {
        "summary": (
            "The United States Holocaust Memorial Museum (USHMM, est. 1993, Washington, D.C. — located on the National Mall, adjacent to the Jefferson Memorial) is the primary Holocaust memorial and educational institution in the United States — a federal museum established by Congress in 1980 to document the Nazi genocide (1933–1945), honour the 6 million Jewish victims, and ensure the Holocaust's moral lessons inform civic life. With 2 million visitors annually and the world's most comprehensive Holocaust archive (85 million+ pages of documents, 80,000+ photographs), USHMM is the world's most influential Holocaust education institution.\n\n"
            "The museum was created by the President's Commission on the Holocaust (1978), established by President Carter in response to Holocaust survivor Elie Wiesel's advocacy. The commission's report — 'Remembering for the Future' — argued that the United States, as the liberator of the Nazi death camps, had a unique obligation to ensure the Holocaust was remembered and its lessons applied. James Freed (Pei Cobb Freed & Partners) designed the museum in a deliberately disorientating, fractured modernist style — triangular forms, skewed walls, industrial materials (brick, steel, glass) — to physically embody the disorientation of Holocaust experience.\n\n"
            "USHMM's 'Genocide Prevention Initiative' — alerting policymakers to emerging genocides worldwide (Rwanda 1994, Darfur 2003, Myanmar 2017) — has made it an active participant in genocide prevention, not merely a memorial institution, fulfilling the founders' intention that Holocaust memory should prevent future atrocities."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary Holocaust memorial and educational institution in the United States (est. 1993, Washington D.C. National Mall); established by Congress 1980, opened 1993; 2 million visitors annually; world's most comprehensive Holocaust archive (85 million+ pages, 80,000+ photographs); James Freed design (deliberately disorientating modernist style); Elie Wiesel advocacy central to founding; Genocide Prevention Initiative (Rwanda 1994, Darfur 2003, Myanmar 2017); world's most influential Holocaust education institution.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Elie Wiesel's advocacy — as a Holocaust survivor and Nobel Peace Prize laureate — with President Carter for a national Holocaust memorial was the primary personal force driving the museum's establishment, grounded in the conviction that bearing witness to the Holocaust was a moral obligation for survivors and a civic duty for nations",
            "The United States' historical role as liberator of the Nazi concentration camps (1945) — and the moral obligation that liberation implied — provided the institutional argument for a national Holocaust museum on the National Mall, adjacent to the memorials to American democratic founders",
            "Congress's recognition (1980) that the Holocaust's lessons for democratic governance, human rights, and genocide prevention needed an institutional home that could reach the millions of Americans who visit Washington annually"
        ],
        "effects": [
            "USHMM's Permanent Exhibition — which takes visitors through the chronological arc of the Holocaust from Nazi rise to power (1933) through the post-war Nuremberg trials — has educated 45 million visitors since opening (1993), making it the single most powerful Holocaust education experience available to the American public",
            "The museum's Genocide Prevention Initiative — which monitors and alerts policymakers to emerging genocides worldwide — has given USHMM an active policy role beyond memorial function, attempting to fulfill the founders' intention that 'Never Again' be a practical commitment rather than a rhetorical one",
            "USHMM's archive — 85 million+ pages of documents, 80,000+ photographs, 200,000+ survivor testimonies — is the world's most comprehensive Holocaust documentation resource, used by researchers worldwide and the primary scholarly foundation for Holocaust studies",
            "The museum's founding model — a federal institution on the National Mall, funded by Congress, dedicated to a specifically ethnic genocide — has been contested by other groups seeking equivalent recognition, generating ongoing debates about whose suffering qualifies for national memorial recognition that continue to shape American memory politics"
        ],
        "relationships": [
            {"entity": "Elie Wiesel (Holocaust survivor, Nobel Peace Prize, founding advocate)", "relationship": "FOUNDED_THROUGH_THE_ADVOCACY_OF", "note": "Wiesel's advocacy with President Carter — grounded in his experience as a Holocaust survivor — was the primary personal force driving the museum's establishment"},
            {"entity": "President Jimmy Carter (established commission 1978)", "relationship": "FOUNDING_COMMISSION_ESTABLISHED_BY", "note": "Carter established the President's Commission on the Holocaust (1978) in response to Wiesel's advocacy — beginning the political process that created the museum"},
            {"entity": "James Freed (Pei Cobb Freed & Partners, architect)", "relationship": "DESIGNED_BY", "note": "James Freed's deliberately disorientating design — triangular forms, skewed walls, industrial materials — physically embodies the disorientation of Holocaust experience"},
            {"entity": "Genocide Prevention Initiative (Rwanda, Darfur, Myanmar)", "relationship": "OPERATES_THE_ACTIVE", "note": "USHMM's Genocide Prevention Initiative — alerting policymakers to emerging genocides — makes it an active participant in prevention rather than merely a memorial institution"},
            {"entity": "National Mall, Washington D.C. (location alongside American democratic memorials)", "relationship": "SITED_ON_THE", "note": "The museum's location on the National Mall — adjacent to the Jefferson Memorial — makes a statement about Holocaust memory as a civic obligation of American democracy"}
        ],
    }),

    ("guggenheim-museum-bilbao", {
        "summary": (
            "The Guggenheim Museum Bilbao (est. 1997, Bilbao, Spain — designed by Frank Gehry) is the most architecturally celebrated museum of the 20th century and the most discussed example of the 'museum as urban regenerator' — the titanium-clad, sculptural building that transformed Bilbao from a declining Basque industrial city into one of Europe's premier cultural destinations and generated the concept of the 'Bilbao Effect': the idea that a single iconic cultural building can transform a city's economic and cultural fortunes.\n\n"
            "The Guggenheim Bilbao was built as part of the Basque government's post-industrial regeneration strategy — converting Bilbao's abandoned industrial waterfront into a cultural and commercial district. Frank Gehry's design (1991–1997) — using 3D modelling software (CATIA) that had never previously been applied to architectural design — created a building of unprecedented formal complexity: 33,000 titanium panels, each uniquely shaped, covering curved and folded forms that reference ships and fish (Gehry's acknowledged inspirations) and interact with the light and the Nervión River in constantly changing ways.\n\n"
            "The 'Bilbao Effect' has been claimed by dozens of cities and museums worldwide as a model for cultural regeneration — from Dundee (V&A Dundee) to Abu Dhabi (Louvre Abu Dhabi) — though critics note that the Bilbao model was unrepeatable: its success depended on Gehry's unrepeatable genius, the Guggenheim brand, and Bilbao's specific combination of post-industrial crisis and Basque political autonomy."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most architecturally celebrated museum of 20th century (est. 1997, Frank Gehry); 'Bilbao Effect' — iconic cultural building transformed declining industrial city into premier cultural destination; 33,000 uniquely shaped titanium panels; CATIA 3D modelling software — first architectural application; Jeff Koons's 'Puppy' (exterior); Richard Serra's 'The Matter of Time' (permanent interior); 1 million annual visitors added to Bilbao tourism; model for museum-led urban regeneration worldwide (Dundee, Abu Dhabi).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Basque government's post-industrial regeneration strategy — converting Bilbao's abandoned waterfront into a cultural and commercial district — required a landmark building to signal Bilbao's transformation and attract international attention, creating the commission that produced Gehry's masterwork",
            "Frank Gehry's use of CATIA (3D modelling software developed for the French aerospace industry) for the first time in architecture — allowing him to design and engineer curved and folded forms that would have been impossible to construct without digital modelling — was the technological breakthrough that made the building's formal complexity constructable",
            "The Solomon R. Guggenheim Foundation's 'Guggenheim effect' — the international brand recognition that made the Bilbao museum immediately known worldwide even before opening — was essential to the project's commercial success, with the Foundation's global network providing the curatorial and institutional credibility that made Bilbao's gamble pay off"
        ],
        "effects": [
            "The 'Bilbao Effect' — the concept that a single iconic cultural building can transform a declining city's fortunes — became one of the most influential ideas in urban planning and cultural economics in the late 20th and early 21st centuries, with dozens of cities worldwide commissioning 'starchitect' buildings in imitation of Gehry's model",
            "The Guggenheim Bilbao's economic impact — generating €500 million annually for the Basque economy, 1 million visitors added to Bilbao tourism, 5,000 permanent jobs — provided the empirical foundation for the 'cultural regeneration' theory that has justified cultural investment in post-industrial cities worldwide",
            "Gehry's use of CATIA for architectural design established the paradigm for parametric and computational design that has dominated 21st-century architecture — every subsequent 'blobby' building by Zaha Hadid, Rem Koolhaas, and others descends from the modelling techniques pioneered in Bilbao",
            "Richard Serra's permanent installation 'The Matter of Time' (2005) — 8 massive steel sculptures (including a 44-metre long snaking steel wall) occupying the museum's largest gallery — is considered the greatest public sculpture programme in any museum and has established Bilbao as a primary destination for contemporary sculpture"
        ],
        "relationships": [
            {"entity": "Frank Gehry (architect, titanium design 1991–1997)", "relationship": "DESIGNED_BY", "note": "Gehry's titanium-clad design — using CATIA for the first time in architecture — created the most celebrated museum building of the 20th century"},
            {"entity": "'Bilbao Effect' (concept of museum-as-urban-regenerator)", "relationship": "ORIGIN_AND_PRIMARY_EXAMPLE_OF_THE", "note": "The Guggenheim Bilbao's commercial success created the 'Bilbao Effect' concept — inspiring urban planners worldwide to commission iconic cultural buildings as regeneration tools"},
            {"entity": "Richard Serra — 'The Matter of Time' (permanent installation 2005)", "relationship": "HOUSES_THE_MOST_CELEBRATED_CONTEMPORARY_SCULPTURE_PROGRAMME", "note": "Serra's 8 massive steel sculptures — including a 44-metre snaking steel wall — occupy the museum's largest gallery and are considered the greatest public sculpture programme in any museum"},
            {"entity": "Basque government (urban regeneration strategy)", "relationship": "BUILT_AS_CENTREPIECE_OF_THE", "note": "The Basque government's post-industrial regeneration of Bilbao's waterfront — of which the Guggenheim was the centrepiece — is the most successful example of museum-led urban regeneration"},
            {"entity": "CATIA software (first architectural application)", "relationship": "PIONEERED_THE_ARCHITECTURAL_USE_OF", "note": "Gehry's use of CATIA for Bilbao established the paradigm for parametric and computational design that has dominated 21st-century architecture"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 36 — {len(ENTITIES)} entities (Class 361: World-Famous Museums)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
