#!/usr/bin/env python3
"""
Batch 15 — 8 entities (Class 341): Churches & Cathedrals
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/341-Class-341"
FILE_PREFIX = "341"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


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

    ("hagia-sophia", {
        "summary": (
            "Hagia Sophia (Holy Wisdom, est. 537 CE) is the most historically significant church in the Eastern Christian world — built in Constantinople by Emperor Justinian I as the centrepiece of his imperial programme of monumental construction — and has served successively as the world's largest cathedral (537–1453), an Ottoman imperial mosque (1453–1934), a secular museum (1934–2020), and a mosque again (from 2020). Its massive dome (31 metres in diameter, rising 55 metres from the floor) was the largest in the world for nearly 1,000 years and remains one of the supreme architectural achievements of human history.\n\n"
            "Justinian reportedly declared upon its dedication: 'Solomon, I have outdone thee' — and the Hagia Sophia's engineering achievement was indeed without precedent: the dome appears to float on a ring of light (created by 40 windows at the drum's base), creating the Byzantine theological concept of a space that mediates between earth and heaven. The mosaics that cover its interior — gold tesserae depicting Christ, the Virgin, emperors, and saints — constitute the most important surviving corpus of Byzantine imperial art.\n\n"
            "The conversion of Hagia Sophia into a mosque by Mehmed II after Constantinople's fall (1453) marked the end of the Byzantine Empire and the beginning of Ottoman Constantinople. Atatürk's conversion to a museum (1934) was a signal of secular Turkish nationalism. Erdoğan's reconversion to a mosque (2020) — condemned by the Orthodox Church, UNESCO, and Western governments — demonstrated how Hagia Sophia remains a living geopolitical and religious symbol 1,500 years after its construction."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Byzantine imperial church (est. 537 CE); world's largest cathedral for nearly 1,000 years; Justinian's 'I have outdone Solomon'; converted to mosque by Mehmed II (1453) marking the Byzantine Empire's end; Atatürk's museum (1934); Erdoğan's reconversion (2020) — still a geopolitical symbol 1,500 years later.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Emperor Justinian I's ambition to rebuild Constantinople after the Nika Revolt (532 CE) destroyed the earlier basilica — and his desire to create a monument that would assert the glory of his reign and the Byzantine Empire's divine mandate — provided the imperial will and resources for Hagia Sophia's construction",
            "The architectural genius of Anthemius of Tralles and Isidore of Miletus — who developed the innovative pendentive system allowing a circular dome to rest on a square base — provided the engineering solution that made Hagia Sophia's extraordinary dome possible",
            "Byzantine imperial theology — the concept that the emperor was God's viceroy on earth and that the imperial church mediated between heaven and earth — created the theological brief for an architectural space that expressed divine immanence through light, scale, and golden mosaic"
        ],
        "effects": [
            "Hagia Sophia's dome (31m diameter, 55m height) was the world's largest for nearly 1,000 years and fundamentally influenced all subsequent domed architecture — the Ottoman imperial mosques (Blue Mosque, Süleymaniye, Selimiye) all used its dome-and-semi-dome system, and its influence extends to St. Peter's Basilica",
            "The conversion to a mosque by Mehmed II (1453) — covering the Christian mosaics with plaster, adding minarets, converting the apse to a mihrab — marked the definitive end of the Byzantine Empire and became the most powerful symbol of Ottoman imperial triumph",
            "The Byzantine mosaic programme — gold-ground mosaics of Christ, the Virgin, emperors, and saints — preserved in the Hagia Sophia represents the most important surviving corpus of Byzantine imperial art, shaping Western art history's understanding of Byzantine visual culture",
            "Erdoğan's reconversion to a mosque (2020) — condemned by UNESCO, the Orthodox Church, Greece, and Western governments — demonstrated that Hagia Sophia remains a living geopolitical symbol, with its status serving as a barometer of Turkish national identity and East-West relations"
        ],
        "relationships": [
            {"entity": "Emperor Justinian I", "relationship": "COMMISSIONED_BY", "note": "Justinian commissioned Hagia Sophia (532–537) — declaring 'Solomon, I have outdone thee' on its dedication"},
            {"entity": "Byzantine Empire", "relationship": "IMPERIAL_RELIGIOUS_CENTRE_OF", "note": "Hagia Sophia was the religious centre of the Byzantine Empire — the site of imperial coronations, councils, and the patriarch's throne"},
            {"entity": "Mehmed II", "relationship": "CONVERTED_TO_MOSQUE_BY_AFTER_CONQUEST", "note": "Mehmed II converted Hagia Sophia to a mosque (1453) after the Fall of Constantinople — the defining symbol of Ottoman triumph over Byzantium"},
            {"entity": "Ottoman imperial architecture", "relationship": "ARCHITECTURAL_MODEL_FOR", "note": "Hagia Sophia's dome system was the model for all major Ottoman imperial mosques — Blue Mosque, Süleymaniye, Selimiye"},
            {"entity": "UNESCO World Heritage", "relationship": "PROTECTED_AS", "note": "Hagia Sophia is a UNESCO World Heritage Site (as part of the Historic Areas of Istanbul) — though its 2020 reconversion to a mosque strained the UNESCO relationship"}
        ],
    }),

    ("westminster-abbey", {
        "summary": (
            "Westminster Abbey (Collegiate Church of Saint Peter at Westminster, est. 960 CE, rebuilt 1245–1269) is the Royal Peculiar church in London — a church directly under the monarch's authority, not a bishop's — that has been the site of every English (and British) coronation since 1066 (William the Conqueror's crowning) and the burial place of 17 monarchs, more than 3,000 notable Britons, and many of the most celebrated figures in English literature, science, and culture. The 'Poets' Corner' — where Chaucer, Spenser, Dryden, Johnson, Dickens, Hardy, and Tennyson are buried or memorialised — is the most concentrated locus of English literary memory in the world.\n\n"
            "Westminster Abbey's Gothic architecture — rebuilt by Henry III (from 1245) in the French Gothic style, inspired by the Sainte-Chapelle in Paris — introduced the highest nave in England (31 metres) and the most ambitious English Gothic programme. The Lady Chapel (Henry VII's Chapel, 1503–1519) — with its extraordinarily intricate fan vaulting — is among the most celebrated Gothic interiors in the world.\n\n"
            "Westminster Abbey's coronation ritual — which has been performed 38 times since 1066 and whose essential elements (anointing, crowning, enthronement, homage) are largely unchanged since Edgar's coronation at Bath (973 CE) — is the oldest continuously performed constitutional ritual in the Western world, making it a living monument to the continuity of the British constitution and monarchy."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Royal Peculiar church (est. 960 CE); site of every English/British coronation since 1066 (38 total); burial place of 17 monarchs and 3,000+ notable Britons; Poets' Corner is the most concentrated locus of English literary memory; Henry VII's Chapel fan vaulting — finest Gothic interior in England; oldest continuously performed constitutional ritual in the West.",
            "significanceCategory": "continental"
        },
        "causes": [
            "King Edward the Confessor's decision to rebuild the earlier Benedictine monastery adjacent to his Westminster Palace (1042–1065) — creating a royal church directly adjacent to the seat of government — established the spatial relationship between church, crown, and government that Westminster Abbey has represented ever since",
            "William the Conqueror's coronation at Westminster Abbey (1066) — establishing it as the site of royal legitimation — created a path dependency that made every subsequent English and British monarch seek coronation in the same space, embedding the Abbey in constitutional practice",
            "Henry III's Gothic rebuilding (from 1245) — inspired by the French Gothic of the Sainte-Chapelle and designed to create a magnificent shrine for Edward the Confessor's relics — established Westminster Abbey's current architectural form and its role as a royal mausoleum"
        ],
        "effects": [
            "Westminster Abbey's coronation ritual — anointing, crowning, enthronement, homage — is the oldest continuously performed constitutional ritual in the Western world, maintaining unchanged elements from Edgar's 973 CE coronation and legitimising every British monarch since the Norman Conquest",
            "Poets' Corner — where Chaucer (d.1400), Spenser, Dryden, Johnson, Dickens, Hardy, Tennyson, Auden, and Lewis Carroll are buried or memorialised — created the most concentrated locus of English literary memory, making Westminster Abbey the national monument to English language culture",
            "Westminster Abbey's Tomb of the Unknown Warrior (1920) — the first such memorial of its kind — created the model for national commemoration of anonymous war dead that was adopted across the world, making Westminster Abbey a pioneer in the politics of public grief",
            "The regular Westminster Abbey broadcasts — coronations (1937, 1953, 2023), royal weddings (1947, 1981, 2011), state funerals (Churchill 1965, Diana 1997, Elizabeth II 2022) — have been watched by the largest global television audiences in history, making the Abbey the most viewed religious building in the world"
        ],
        "relationships": [
            {"entity": "British monarchy", "relationship": "CORONATION_SITE_FOR_EVERY_MONARCH_SINCE_1066", "note": "Westminster Abbey has been the coronation site for every English and British monarch since William I (1066) — 38 coronations"},
            {"entity": "English literature", "relationship": "POETS_CORNER_NATIONAL_MEMORIAL_OF", "note": "Poets' Corner — Chaucer, Dickens, Hardy, Tennyson — is the most concentrated locus of English literary memory"},
            {"entity": "Tomb of the Unknown Warrior (1920)", "relationship": "HOUSES_PIONEERING_WAR_MEMORIAL", "note": "Westminster Abbey's Tomb of the Unknown Warrior (1920) pioneered the model for national commemoration of anonymous war dead — adopted globally"},
            {"entity": "Henry III", "relationship": "REBUILT_IN_GOTHIC_STYLE_BY", "note": "Henry III rebuilt Westminster Abbey (from 1245) in the French Gothic style — creating the present architectural form"},
            {"entity": "British constitutional continuity", "relationship": "LIVING_MONUMENT_TO", "note": "Westminster Abbey's coronation ritual (unchanged since 973 CE) is the oldest continuously performed constitutional ritual in the Western world"}
        ],
    }),

    ("notre-dame-de-paris", {
        "summary": (
            "Notre-Dame de Paris (Our Lady of Paris, construction 1163–1345) is the most celebrated Gothic cathedral in the world — the building that popularised Gothic architecture across Europe — and the spiritual and geographic centre of France, located on the Île de la Cité in the heart of Paris, with kilometre-zero (the point from which all French road distances are measured) directly in front of its façade. Commissioned by Bishop Maurice de Sully, Notre-Dame was one of the first cathedrals to employ the flying buttress systematically — the structural innovation that allowed Gothic walls to be pierced with enormous stained glass windows.\n\n"
            "Notre-Dame's rose windows — three enormous circular windows of tracery and coloured glass, the North rose (1250, largely original) and South rose (1260) being among the most celebrated examples of medieval glass — are the supreme examples of Gothic stained glass, flooding the interior with coloured light that the medieval builders conceived as the visible presence of divine grace. Victor Hugo's novel 'Notre-Dame de Paris' (1831) — which used the cathedral as its central character — was instrumental in saving it from the Revolutionary-era neglect that had left it in partial ruin.\n\n"
            "The 2019 fire — which destroyed the medieval spire and two-thirds of the medieval oak roof (the 'Forest', built 1220–1240) — was experienced as a global cultural trauma, with 1 billion people watching the fire live and €850 million pledged for reconstruction within 48 hours. The ongoing reconstruction (target: 2024 reopening) has generated intense debate about restoration authenticity."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most celebrated Gothic cathedral (construction 1163–1345); popularised flying buttresses and Gothic architecture; geographic centre of France (kilometre-zero); Victor Hugo's novel saved it from ruin; 2019 fire watched by 1 billion people globally; €850M pledged in 48 hours — the most globally mourned architectural event in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Bishop Maurice de Sully's ambition (1160s) to replace the existing Romanesque cathedral with a building worthy of Paris's growing importance — the city was becoming the political and intellectual capital of France and northern Europe — provided the episcopal drive and fundraising capacity for the 182-year construction programme",
            "The development of Gothic structural innovations in the Île-de-France region (1130s–1160s) — the pointed arch, ribbed vault, and eventually the flying buttress — created the engineering vocabulary that Notre-Dame's builders systematically refined and deployed on an unprecedented scale",
            "Medieval Christianity's theology of light — Abbot Suger's argument that physical light is a manifestation of divine grace and that a cathedral filled with coloured light creates a threshold between earth and heaven — provided the theological brief for the enormous stained glass windows that the flying buttress made structurally possible"
        ],
        "effects": [
            "Notre-Dame's systematic use of flying buttresses — allowing the walls to be opened with enormous windows — was the model that spread Gothic architecture across Europe, making every subsequent Gothic cathedral from Cologne to Salisbury to Chartres intellectually indebted to Notre-Dame",
            "Victor Hugo's 'Notre-Dame de Paris' (1831) — using the cathedral as the novel's central character in a tale of Quasimodo and Esmeralda — created the popular identification of Gothic architecture with medieval romance that drove the Gothic Revival, and Hugo's advocacy directly saved the cathedral from Revolutionary neglect",
            "Notre-Dame's kilometre-zero position — the geographic centre from which all French road distances are measured — reflects and reinforces Paris's centrality to French national identity, making the cathedral not merely a religious building but the symbolic centre of the French state",
            "The 2019 fire and its global response — 1 billion viewers, €850 million pledged in 48 hours — demonstrated that Notre-Dame had achieved a status beyond Christianity, as a symbol of European civilisation and shared human heritage, with its reconstruction becoming a global cultural project"
        ],
        "relationships": [
            {"entity": "Gothic architecture", "relationship": "POPULARISED_AND_SPREAD", "note": "Notre-Dame's systematic flying buttresses and stained glass popularised Gothic architecture — the model for cathedrals from Cologne to Salisbury"},
            {"entity": "Victor Hugo", "relationship": "SAVED_FROM_RUIN_AND_MADE_SYMBOL_BY", "note": "Hugo's 'Notre-Dame de Paris' (1831) saved the cathedral from Revolutionary neglect and created its romantic cultural mythology"},
            {"entity": "France (national identity)", "relationship": "SYMBOLIC_CENTRE_OF", "note": "Notre-Dame's kilometre-zero position and its role in French coronations, royal baptisms, and national mourning makes it the symbolic centre of France"},
            {"entity": "2019 Notre-Dame fire", "relationship": "PARTIALLY_DESTROYED_BY", "note": "The 2019 fire destroyed the medieval spire and two-thirds of the medieval roof — the most globally mourned architectural event in history"},
            {"entity": "Medieval stained glass", "relationship": "SUPREME_EXAMPLES_OF_ROSE_WINDOWS", "note": "Notre-Dame's three rose windows — particularly the North rose (1250) — are among the supreme examples of medieval stained glass"}
        ],
    }),

    ("chartres-cathedral", {
        "summary": (
            "Chartres Cathedral (Cathedral of Our Lady of Chartres, rebuilt 1194–1220 after fire) is widely regarded as the most complete and best-preserved example of French Gothic architecture — built with extraordinary speed (26 years) following the 1194 fire — and contains the largest and most important surviving programme of medieval stained glass in the world: 176 windows with approximately 5,000 figures covering 2,600 square metres of glass, 80% of which dates from the original 1194–1220 construction.\n\n"
            "Chartres was one of the most important pilgrimage destinations in medieval France — housing the Sancta Camisa, reputed to be the Virgin Mary's tunic (given by Charles the Bald in 876 CE) — and the cathedral's dedication to the Virgin Mary made it the pre-eminent Marian shrine in northern Europe. The Royal Portal (c.1145, from the earlier Romanesque cathedral) — with its column-statues of Old Testament figures — is the first great sculptural programme of the Gothic period and a foundational work of Western sculpture.\n\n"
            "The two towers of Chartres — built three centuries apart and in completely different styles (the Romanesque south tower, c.1160; the Gothic Flamboyant north tower, 1506–1513) — are one of Western architecture's most celebrated exercises in aesthetic contrast. Malcolm Miller's 50-year guided tour career at Chartres and John James's detailed archaeological study of the cathedral's construction have made Chartres the most intensively studied Gothic building in the world."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most complete French Gothic cathedral (rebuilt 1194–1220); largest surviving medieval stained glass programme (5,000 figures, 2,600 sq m); premier Marian pilgrimage shrine in northern France; Royal Portal is the founding work of Gothic sculpture; two towers (built 350 years apart) are architecture's most celebrated aesthetic contrast.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The fire of 1194 — which destroyed most of the Romanesque cathedral but miraculously spared the Sancta Camisa (the Virgin's relic) — was interpreted as a divine mandate to rebuild on a grander scale, generating the extraordinary public and aristocratic fundraising that financed the 26-year rebuilding",
            "Chartres's position on the pilgrimage route to Santiago de Compostela — and its possession of the Sancta Camisa — made it one of the most visited pilgrimage destinations in France, providing the revenue that justified and financed the monumental construction programme",
            "The Gothic architectural revolution's maturation in the Île-de-France (1140s–1190s) — the systematic refinement of pointed arch, ribbed vault, and flying buttress — provided the technical vocabulary that Chartres's builders deployed with unprecedented completeness and confidence"
        ],
        "effects": [
            "Chartres's stained glass programme — 176 windows, 5,000 figures, 2,600 square metres, 80% original 13th-century glass — is the largest and best-preserved medieval stained glass corpus in the world, providing the primary evidence for medieval glassmakers' techniques and iconographic programmes",
            "The Royal Portal's column-statues (c.1145) — elongated figures of Old Testament kings and queens integrated into the portal architecture — are the founding works of Gothic monumental sculpture, establishing the relationship between architecture and figurative sculpture that defined Gothic portals for 200 years",
            "Chartres's labyrinth (c.1220) — an 11-circuit stone labyrinth set into the cathedral floor, used for penitential pilgrimage — is the best-preserved medieval church labyrinth and has inspired the global labyrinth movement (labyrinths in hospitals, prisons, gardens) as a meditative tool",
            "The 'Chartres model' of Gothic cathedral design — high nave, flying buttresses, three-portal west front, two towers, large clerestory windows — became the template for High Gothic cathedrals across France, England, Germany, and Spain"
        ],
        "relationships": [
            {"entity": "French Gothic architecture", "relationship": "MOST_COMPLETE_EXAMPLE_OF", "note": "Chartres is the most complete and best-preserved example of French High Gothic — the template for Gothic cathedrals across Europe"},
            {"entity": "Medieval stained glass", "relationship": "LARGEST_SURVIVING_PROGRAMME_OF", "note": "Chartres's 176 windows (5,000 figures, 80% original) are the largest and best-preserved medieval stained glass corpus in the world"},
            {"entity": "Gothic sculpture", "relationship": "FOUNDING_PROGRAMME_OF_ROYAL_PORTAL", "note": "The Royal Portal (c.1145) is the founding work of Gothic monumental sculpture — establishing the relationship between architecture and figurative form"},
            {"entity": "Marian pilgrimage (medieval France)", "relationship": "PRE-EMINENT_SHRINE_OF", "note": "Chartres was the premier Marian pilgrimage shrine in northern France — housing the Sancta Camisa (Virgin Mary's tunic)"},
            {"entity": "Cathedral labyrinth tradition", "relationship": "BEST-PRESERVED_EXAMPLE_OF", "note": "Chartres's labyrinth (c.1220) is the best-preserved medieval church labyrinth — inspiring the global labyrinth movement"}
        ],
    }),

    ("cologne-cathedral", {
        "summary": (
            "Cologne Cathedral (Kölner Dom, construction 1248–1880, with an interruption of 300+ years from c.1560 to 1842) is the largest Gothic cathedral in Northern Europe and the most visited landmark in Germany (approximately 6 million visitors annually) — a UNESCO World Heritage Site whose twin spires (157 metres) were the tallest structures in the world from 1880 to 1884. The cathedral was built to house the Shrine of the Three Kings — the reliquary containing the reputed bones of the Magi, brought to Cologne from Milan by Archbishop Rainald of Dassel in 1164 — which made Cologne one of the most important pilgrimage destinations in medieval Europe.\n\n"
            "The Shrine of the Three Kings (c.1190–1225) — a gold reliquary encrusted with gems, cameos, and enamels, measuring 2.2 metres long — is the largest reliquary in the Western world and the supreme masterpiece of medieval Rhenish goldsmithing. It attracted pilgrims from across Europe including three kings (Otto IV, Philip of Swabia, Frederick II) who came to be crowned 'Kings of the Germans' at Aachen after paying homage to the Magi.\n\n"
            "The cathedral's extraordinary construction history — begun in 1248, its construction interrupted for over 300 years with the south tower a truncated stump visible on Cologne's skyline for centuries, and then spectacularly completed in the 1842–1880 Gothic Revival using the original medieval plans — is a unique case in architectural history of a medieval Gothic project resumed and completed in the modern period using the original architects' drawings."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest Gothic cathedral in Northern Europe (construction 1248–1880); twin spires tallest structures in world 1880–1884; UNESCO World Heritage; Shrine of the Three Kings (world's largest reliquary) made Cologne a major medieval pilgrimage site; unique construction history (300-year interruption, completed using original medieval plans).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The arrival of the Shrine of the Three Kings in Cologne (1164) — brought from Milan by Archbishop Rainald of Dassel as war booty from Frederick Barbarossa's Italian campaign — created the major pilgrimage attraction that justified the construction of a Gothic cathedral of unprecedented ambition",
            "Cologne's position as the largest city north of the Alps in the medieval period — the richest and most populous Rhenish city, with a powerful archbishop and a prosperous merchant community — provided the economic resources to fund a centuries-long construction programme",
            "The Gothic Revival's romantic fascination with the incomplete medieval cathedral — Cologne's truncated south tower was the most powerful symbol of an unfinished dream — motivated the 19th-century completion campaign, supported by the Prussian state and pan-German nationalist sentiment"
        ],
        "effects": [
            "Cologne Cathedral's twin spires (157 metres, 1880) — the tallest structures in the world from 1880 to 1884 (when the Washington Monument surpassed them) — demonstrated that Gothic architecture could be built to unprecedented scale using 19th-century construction technology, inspiring Gothic Revival architecture globally",
            "The Shrine of the Three Kings — the world's largest reliquary — made Cologne one of the most visited pilgrimage destinations in medieval Europe, attracting three Holy Roman Emperors and hundreds of thousands of pilgrims, generating the wealth that financed the cathedral's construction",
            "The cathedral's WWII survival — though 70% of Cologne was destroyed by Allied bombing (1942–1945), the cathedral survived largely intact despite 14 direct bomb hits (its massive stone construction absorbed the blasts) — made it the most powerful symbol of German cultural survival, serving as a navigation landmark for Allied bombers (who sometimes deliberately spared it)",
            "The completion of Cologne Cathedral (1880) using the original 13th-century plans — a project that had been interrupted for 300+ years — became a symbol of German national unification (1871) and architectural continuity, demonstrating that medieval ambitions could be realised by modern engineering"
        ],
        "relationships": [
            {"entity": "Shrine of the Three Kings", "relationship": "BUILT_TO_HOUSE", "note": "Cologne Cathedral was built to house the Shrine of the Three Kings — brought from Milan (1164) — the world's largest reliquary and Cologne's primary pilgrimage attraction"},
            {"entity": "German unification (1871)", "relationship": "COMPLETION_CELEBRATED_AS_SYMBOL_OF", "note": "The completion of Cologne Cathedral (1880) was celebrated as a symbol of German national unification — the monument to German cultural achievement"},
            {"entity": "Gothic Revival architecture", "relationship": "MOST_AMBITIOUS_ACHIEVEMENT_OF", "note": "Cologne Cathedral's completion (1880) using original medieval plans is the most ambitious achievement of Gothic Revival architecture"},
            {"entity": "World War II bombing of Cologne", "relationship": "SURVIVED_WHILE_CITY_DESTROYED", "note": "The cathedral survived 14 direct bomb hits while 70% of Cologne was destroyed — becoming the most powerful symbol of German cultural survival"},
            {"entity": "Medieval Rhenish goldsmithing", "relationship": "HOUSES_SUPREME_MASTERPIECE_OF", "note": "The Shrine of the Three Kings (c.1190–1225) — housed in the cathedral — is the supreme masterpiece of medieval Rhenish goldsmithing"}
        ],
    }),

    ("st-peters-basilica", {
        "summary": (
            "St. Peter's Basilica (Basilica Papale di San Pietro in Vaticano, construction 1506–1626) is the largest church in the world by interior volume and the spiritual centre of the Roman Catholic Church — built over the traditional site of St. Peter's tomb on the Vatican hill in Rome, a site of Christian veneration since at least the 2nd century. Its construction — involving Bramante, Raphael, Michelangelo (who designed the dome at age 71), Giacomo della Porta, and Carlo Maderno — spanned 120 years and constitutes the most important single architectural project of the Italian Renaissance and Baroque periods.\n\n"
            "Michelangelo's dome (exterior height 136 metres) is the defining image of Western ecclesiastical architecture — reproduced in hundreds of churches and public buildings globally, from the US Capitol to St. Paul's Cathedral to the Panthéon in Paris. The Bernini-designed piazza (St. Peter's Square, 1656–1667) — an elliptical colonnade of 284 columns in four rows, creating a 'maternal embrace' of Catholic Christianity — is the greatest piece of urban design of the 17th century and the primary assembly space for the Catholic world.\n\n"
            "The fundraising for St. Peter's construction — Pope Julius II's sale of indulgences specifically to finance the basilica — directly provoked Martin Luther's Ninety-Five Theses (1517), making St. Peter's construction the most consequential architectural fundraising project in history. The rebuilding of St. Peter's thus indirectly caused the Protestant Reformation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest church by interior volume (construction 1506–1626); Michelangelo's dome is the defining image of Western ecclesiastical architecture; indulgence sales to fund construction directly provoked Luther's 95 Theses — the Protestant Reformation's trigger; Bernini's piazza is the greatest 17th-century urban design; spiritual centre of 1.3 billion Catholics.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Pope Julius II's decision to demolish Constantine's 4th-century Old St. Peter's and replace it with an entirely new building — despite the protests of Renaissance humanists who valued the ancient basilica — reflected his ambition to create a monument worthy of the papacy's renewed political and spiritual authority",
            "The Renaissance architectural revolution — the rediscovery of classical Roman architecture and the development of new structural and aesthetic principles — provided the intellectual and technical vocabulary for the successive architects who shaped St. Peter's from Bramante's centralised plan to Michelangelo's dome",
            "The Catholic Church's control of the most important pilgrimage site in Western Christianity — St. Peter's tomb — provided the devotional and financial attraction that justified the enormous expenditure of a 120-year construction programme"
        ],
        "effects": [
            "The indulgence sales to fund St. Peter's construction — Pope Leo X's 1515 extension of Julius II's indulgence campaign, preached in Germany by Johann Tetzel — directly provoked Luther's Ninety-Five Theses (1517), making St. Peter's construction the architectural fundraising project that accidentally caused the Protestant Reformation",
            "Michelangelo's dome (136 metres, completed posthumously 1590) became the defining image of Western ecclesiastical architecture, reproduced in hundreds of churches and public buildings globally — the US Capitol, St. Paul's London, the Panthéon Paris — making it the most widely reproduced architectural element in history",
            "Bernini's St. Peter's Square (1656–1667) — the greatest piece of Baroque urban design — created the primary assembly space for the Catholic world, accommodating 300,000+ for papal events and establishing the physical theatre of papal authority",
            "St. Peter's Basilica's role as the primary stage of Catholic global spectacle — papal masses, canonisations, Christmas and Easter celebrations watched by billions globally — makes it the most watched religious space in human history"
        ],
        "relationships": [
            {"entity": "Michelangelo", "relationship": "DOME_DESIGNED_BY", "note": "Michelangelo designed St. Peter's dome (at age 71) — the defining image of Western ecclesiastical architecture, reproduced globally"},
            {"entity": "Protestant Reformation", "relationship": "INDULGENCE_SALES_TO_FUND_CONSTRUCTION_TRIGGERED", "note": "Indulgence sales to finance St. Peter's construction directly provoked Luther's 95 Theses (1517) — the Protestant Reformation's trigger"},
            {"entity": "Gian Lorenzo Bernini", "relationship": "PIAZZA_DESIGNED_BY", "note": "Bernini's St. Peter's Square (1656–1667) is the greatest Baroque urban design — the primary assembly space for 1.3 billion Catholics"},
            {"entity": "Pope Julius II", "relationship": "COMMISSIONED_REBUILDING_BY", "note": "Julius II commissioned the demolition of the original St. Peter's (1506) and the construction of the new basilica — beginning the 120-year project"},
            {"entity": "Roman Catholicism", "relationship": "SPIRITUAL_CENTRE_OF", "note": "St. Peter's Basilica is the spiritual centre of the Roman Catholic Church — built over St. Peter's tomb — the primary site of Catholic identity"}
        ],
    }),

    ("durham-cathedral", {
        "summary": (
            "Durham Cathedral (Cathedral Church of Christ, Blessed Mary the Virgin, and St Cuthbert of Durham, construction 1093–1133) is the supreme example of Norman Romanesque architecture in Britain — described by Bill Bryson as 'the best cathedral on earth, by a long margin' — and was the first large European building to use stone ribbed vaulting throughout (the nave's ribbed vault, c.1100, predating all other examples), making Durham Cathedral the birthplace of the structural innovation that led directly to Gothic architecture.\n\n"
            "Durham Cathedral's position — perched on a 70-metre sandstone peninsula loop of the River Wear, shared with Durham Castle (another UNESCO World Heritage site) — creates one of the most dramatic architectural settings in Europe. The cathedral was built to house the relics of St. Cuthbert (the most venerated Anglo-Saxon saint) and the head of St. Oswald, making it a major pilgrimage destination that attracted Bede, Aelred of Rievaulx, and thousands of medieval pilgrims annually.\n\n"
            "The Galilee Chapel (c.1175) — a rare Romanesque Lady Chapel at the cathedral's western end — contains the tomb of the Venerable Bede (the 'Father of English History'), making Durham the burial place of the most important Anglo-Saxon historian. The spectacular ribbed vaults of the nave were the structural innovation that released Gothic architecture from Romanesque weight — one of the most consequential architectural inventions in history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Supreme example of Norman Romanesque architecture (construction 1093–1133); first large European building with stone ribbed vaulting (c.1100) — the invention that led to Gothic architecture; UNESCO World Heritage; houses tomb of Bede (Father of English History); Bill Bryson's 'best cathedral on earth, by a long margin'.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The translation of St. Cuthbert's relics to Durham (995 CE) — after a century of flight from Viking raids — created the major pilgrimage site that the Norman bishops wanted to enshrine in a building worthy of the saint's importance, motivating the 1093 construction campaign",
            "Bishop William of Saint-Calais's ambition — following the Norman Conquest — to build a cathedral that would demonstrate Norman power and piety on the most dramatic natural site in northern England created the architectural brief that produced Durham's extraordinary scale and innovation",
            "The Norman builders' encounter with the structural challenge of covering a wide nave with stone vaulting — seeking to avoid the fire risk of the timber roofs that had destroyed many Norman churches — motivated the structural experimentation that produced the ribbed vault"
        ],
        "effects": [
            "Durham's ribbed vault (c.1100) — the first systematic use of stone ribbed vaulting in a large European building — was the structural invention that made Gothic architecture possible, allowing forces to be channelled to points rather than distributed across walls, enabling the large windows and soaring heights of Gothic cathedrals",
            "Durham Cathedral's role as the burial place of St. Cuthbert — the most venerated saint of the Northumbrian church — made it a primary pilgrimage destination that shaped the religious culture of northern England for 500 years",
            "The Venerable Bede's tomb in the Galilee Chapel — Bede (672–735 CE) wrote the 'Ecclesiastical History of the English People', the primary source for early English history — makes Durham a pilgrimage site for historians and a repository of English historical consciousness",
            "Durham's UNESCO World Heritage Site status (1986) — shared with Durham Castle — reflects its position as the most important ensemble of Norman architecture in Britain and one of the finest medieval architectural settings in the world"
        ],
        "relationships": [
            {"entity": "Norman Romanesque architecture", "relationship": "SUPREME_EXAMPLE_OF", "note": "Durham Cathedral is the supreme example of Norman Romanesque architecture in Britain — the most ambitious Norman building project in England"},
            {"entity": "Gothic architecture", "relationship": "RIBBED_VAULT_INVENTION_THAT_ENABLED", "note": "Durham's ribbed vault (c.1100) was the structural invention that enabled Gothic architecture — one of the most consequential architectural inventions in history"},
            {"entity": "St. Cuthbert", "relationship": "HOUSES_RELICS_OF", "note": "Durham was built to house St. Cuthbert's relics — the most venerated Anglo-Saxon saint and the primary motivation for the cathedral's construction"},
            {"entity": "Venerable Bede", "relationship": "HOUSES_TOMB_OF", "note": "Bede's tomb in the Galilee Chapel makes Durham the burial place of the Father of English History"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Durham Cathedral and Castle are a UNESCO World Heritage Site (1986) — the most important ensemble of Norman architecture in Britain"}
        ],
    }),

    ("york-minster", {
        "summary": (
            "York Minster (Cathedral and Metropolitical Church of Saint Peter in York, construction largely 1220–1472, on a site of continuous Christian worship since 627 CE) is the largest Gothic cathedral in Northern Europe by volume and the seat of the Archbishop of York — the second most senior Anglican bishop after the Archbishop of Canterbury. The Minster contains the largest expanse of medieval stained glass in Britain (128 windows) and the largest medieval window in existence: the Great East Window (1405–1408), measuring 23 × 9 metres, depicting the beginning and end of the world in 311 panels.\n\n"
            "York Minster's site has been a place of Christian worship for nearly 1,400 years: Edwin of Northumbria was baptised there by Bishop Paulinus (627 CE) — the first northern English royal Christian — and the site has maintained continuous Christian institutional presence through Viking raids, Norman conquest, and Reformation. The Minster's Chapter House (c.1270–1285) — with its unsupported 17-metre stone vault (no central column) — is the most technically ambitious vaulted space in English Gothic architecture.\n\n"
            "The 1984 fire — caused by lightning striking the south transept shortly after the controversial consecration of Bishop David Jenkins (who had questioned the physical Resurrection) — was interpreted by some as divine judgment and generated the most heated British religious controversy of the 1980s. The subsequent restoration revealed previously unknown medieval details and provided the most comprehensive study of English Gothic construction techniques in modern times."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Largest Gothic cathedral in Northern Europe by volume; seat of the Archbishop of York (second Anglican bishop); largest medieval stained glass collection in Britain; Great East Window (1405–1408) is the largest medieval window in existence; 1,400 years of continuous Christian worship on the site; 1984 fire and lightning strike controversy.",
            "significanceCategory": "continental"
        },
        "causes": [
            "York's position as the capital of Roman Britain (Eboracum) and the seat of one of Britain's two archbishops created the institutional and symbolic importance that justified the construction of the largest Gothic building in Northern Europe",
            "Archbishop Walter de Gray's decision to rebuild the existing Norman minster in the new Gothic style (from 1220) — following the completion of Lincoln Cathedral's Early English Gothic — created the 252-year construction programme that produced the present Minster",
            "York's wealth as the primary commercial city of northern England — the wool trade, the textile industry — provided the economic resources that sustained the Minster's construction across the 13th–15th centuries"
        ],
        "effects": [
            "York Minster's Great East Window (1405–1408) — the largest medieval window in existence, 311 panels depicting Genesis to Revelation — is the most ambitious single programme of medieval stained glass narrative in the world",
            "The Chapter House's unsupported vault (c.1280) — 17 metres in diameter with no central column — is the most technically ambitious vaulted space in English Gothic, demonstrating the structural sophistication achieved by English Gothic builders in the 13th century",
            "York Minster's 1984 fire — and the theological controversy surrounding lightning striking the Minster days after David Jenkins's consecration — generated the most heated British religious debate about miracles and divine action in the 20th century",
            "The Minster's role in establishing English ecclesiastical law — as the seat of the northern province of the Church of England — has made it the primary institutional counterweight to Canterbury's southern primacy, maintaining the territorial balance of English ecclesiastical governance for 800 years"
        ],
        "relationships": [
            {"entity": "Church of England (Anglican)", "relationship": "SEAT_OF_SECOND_ARCHBISHOP_OF", "note": "York Minster is the seat of the Archbishop of York — the second most senior Anglican bishop after Canterbury"},
            {"entity": "Great East Window (1405–1408)", "relationship": "HOUSES_LARGEST_MEDIEVAL_WINDOW", "note": "The Great East Window (23×9m, 311 panels) is the largest medieval window in existence — depicting Genesis to Revelation"},
            {"entity": "Edwin of Northumbria", "relationship": "SITE_OF_BAPTISM_OF_FIRST_NORTHERN_ENGLISH_ROYAL_CHRISTIAN", "note": "Edwin's baptism at York (627 CE) — the first northern English royal Christian — began the Minster's 1,400-year continuous Christian history"},
            {"entity": "1984 York Minster fire", "relationship": "DAMAGED_AND_RESTORED_BY", "note": "The 1984 fire (south transept) and its theological controversy — lightning after Bishop Jenkins's consecration — was the most heated British religious debate of the 1980s"},
            {"entity": "Medieval English Gothic architecture", "relationship": "SUPREME_EXAMPLE_OF_CHAPTER_HOUSE_VAULT", "note": "The Chapter House's unsupported 17-metre vault (c.1280) is the most technically ambitious vaulted space in English Gothic architecture"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 15 — {len(ENTITIES)} entities (Class 341: Churches & Cathedrals)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
