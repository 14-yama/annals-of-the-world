#!/usr/bin/env python3
"""
Batch 47 — 8 entities (Class 392): Famous Navies
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/392-Class-392"
FILE_PREFIX = "392"


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

    ("royal-navy", {
        "summary": (
            "The Royal Navy (est. formally under Henry VIII in 1546 as the Navy Board, though royal naval forces existed from at least the 10th century under Alfred the Great) was the world's dominant naval force for nearly 300 years — from the defeat of the Spanish Armada (1588) through the Victorian era and into the First World War — and the primary instrument through which Britain established and maintained the empire that controlled 24% of the world's surface at its peak. The Royal Navy's 200-year dominance of the world's oceans (c. 1690–1914) is without parallel in naval history and is the most consequential single factor in the political geography of the modern world.\n\n"
            "The Royal Navy's decisive moments include the defeat of the Spanish Armada (1588 — ensuring Protestant England's survival and preventing Spanish hegemony over Europe), the Anglo-Dutch Wars (1652–1674 — establishing British commercial dominance over the Dutch), the Seven Years' War (1756–1763 — establishing British global colonial supremacy), and the Battle of Trafalgar (1805 — Nelson's destruction of the Franco-Spanish fleet that ended Napoleon's invasion threat and confirmed British naval supremacy for a century).\n\n"
            "The Royal Navy's institutional legacy includes the development of naval gunnery as a systematic discipline, the chronometer-based longitude determination that made deep-water navigation reliable, the Royal Marines as the world's oldest continuously serving amphibious force, the systematic charting of the world's oceans (HMS Beagle's hydrographic surveys), and the development of the dreadnought battleship (HMS Dreadnought, 1906) — the technological threshold that sparked the Anglo-German naval race and contributed to the conditions of the First World War."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's dominant naval force for nearly 300 years (formal Navy Board 1546, Alfred the Great origins); primary instrument of British Empire (24% of world's surface at peak); defeat of Spanish Armada (1588), Anglo-Dutch Wars (1652–1674), Seven Years' War (1756–1763), Battle of Trafalgar (1805 — Nelson); 200-year ocean dominance (c. 1690–1914) without parallel in naval history; HMS Dreadnought (1906) — Anglo-German naval race; chronometer longitude navigation; systematic world ocean charting.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Henry VIII's creation of the Navy Board (1546) — institutionalising the royal fleet as a permanent peacetime force rather than ships hired for specific campaigns — established the administrative and financial infrastructure of the Royal Navy as a permanent state institution",
            "England's island geography — which made sea power simultaneously the primary defence against invasion and the essential enabler of overseas trade and colonial expansion — created the strategic logic for continuous investment in naval power that no Continental power could fully replicate",
            "Britain's 18th-century commercial wealth — generated by the triangular trade, colonial production, and the financial revolution that created the Bank of England and national debt financing — provided the sustained fiscal capacity to maintain the largest naval force in the world through peacetime as well as wartime"
        ],
        "effects": [
            "The Royal Navy's 200-year dominance of the world's oceans (c. 1690–1914) — maintaining the Pax Britannica through maritime power — created the conditions for the first era of globalisation: the free flow of trade, the expansion of British colonial settlement, and the enforcement of the free trade principles that characterised Victorian British foreign policy",
            "The Royal Navy's systematic charting of the world's oceans — most famously through HMS Beagle's surveys, which also carried Charles Darwin to the Galápagos Islands — produced the hydrographic knowledge that made deep-water global navigation reliable, directly enabling the expansion of international trade",
            "The Battle of Trafalgar's confirmation of British naval supremacy (1805) — which removed the threat of French naval challenge for a century — freed British strategy from the defensive constraint of home waters defence and enabled the global projection of power that reached its apex in the Victorian Empire",
            "HMS Dreadnought's (1906) technological revolution — rendering all previous battleships obsolete and triggering the Anglo-German naval arms race — was a significant contributing factor to the alliance tensions that produced the First World War, demonstrating how military technological innovation can destabilise international security"
        ],
        "relationships": [
            {"entity": "Battle of Trafalgar (1805, Nelson, Franco-Spanish fleet destruction, century of supremacy)", "relationship": "CENTURY-DEFINING_VICTORY_THAT_CONFIRMED_ITS_SUPREMACY_WAS_THE", "note": "Trafalgar — Nelson's destruction of the Franco-Spanish fleet — confirmed British naval supremacy for a century and freed British strategy for global power projection"},
            {"entity": "Spanish Armada (1588, Protestant England survival, Spanish hegemony prevented)", "relationship": "EARLIEST_AND_MOST_EXISTENTIALLY_SIGNIFICANT_VICTORY_WAS_THE_DEFEAT_OF_THE", "note": "The Armada's defeat — ensuring Protestant England's survival — is the Royal Navy's most consequential early achievement"},
            {"entity": "Pax Britannica (c. 1815–1914, maritime enforcement, first globalisation era)", "relationship": "PRIMARY_MILITARY_GUARANTEE_OF_THE", "note": "The Royal Navy's ocean dominance created the conditions for the Pax Britannica — the first era of economic globalisation"},
            {"entity": "HMS Dreadnought (1906, battleship revolution, Anglo-German naval race)", "relationship": "COMMISSIONED_THE_TECHNOLOGICALLY_REVOLUTIONARY_BATTLESHIP", "note": "HMS Dreadnought's obsolescence of all previous battleships triggered the Anglo-German naval arms race — a contributing factor to WWI"},
            {"entity": "HMS Beagle (hydrographic surveys, Charles Darwin Galápagos voyage)", "relationship": "INSTITUTIONAL_SPONSOR_OF_THE", "note": "The Royal Navy's hydrographic surveys — including HMS Beagle's voyages that carried Darwin to the Galápagos — produced the navigational knowledge enabling global trade"}
        ],
    }),

    ("byzantine-navy", {
        "summary": (
            "The Byzantine Navy (the naval arm of the Eastern Roman / Byzantine Empire — c. 330–1453 CE, though the most effective period was 6th–11th centuries) was the most technically advanced navy in the medieval Mediterranean world and the primary guardian of Constantinople's strategic position as the gateway between the Black Sea and the Aegean. The Byzantine Navy's most decisive contribution to world history was Greek fire — the incendiary naval weapon whose formula remains unknown and which stopped the Arab sieges of Constantinople (674–678 CE and 717–718 CE) that might otherwise have ended the Byzantine Empire a millennium before its actual fall.\n\n"
            "The Byzantine Navy inherited the Roman fleet tradition and adapted it to the strategic realities of the post-Roman Mediterranean — the rise of Arab sea power in the 7th century, the Viking incursions into the Black Sea (the Varangian routes), and the Norman and Venetian naval competition of the 11th–12th centuries. The Byzantine Navy's primary vessel was the dromon — a bireme galley optimised for the deployment of Greek fire from bow-mounted siphons — which gave the Byzantine fleet a decisive tactical advantage over opponents who could not counter the incendiary weapon.\n\n"
            "The Byzantine Navy's decline — driven by Alexios I Komnenos's catastrophic grant of trade privileges to Venice (Chrysobull of 1082, exempting Venetian merchants from all Byzantine port duties) in exchange for naval support against the Normans — eliminated the economic base of Byzantine commercial power and created the Venetian commercial dominance of the eastern Mediterranean that ultimately facilitated the Latin capture of Constantinople in the Fourth Crusade (1204)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most technically advanced medieval Mediterranean navy (c. 330–1453 CE; peak 6th–11th centuries); Greek fire — incendiary naval weapon that stopped Arab sieges of Constantinople (674–678 CE and 717–718 CE); dromon bireme galley; guardian of Constantinople gateway (Black Sea to Aegean); Chrysobull of 1082 (Alexios I Komnenos — Venetian trade privileges) eliminated Byzantine commercial power; Fourth Crusade (1204) — Venetian dominance facilitator; Arab naval challenge; Varangian routes (Viking Black Sea).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Constantinople's strategic position — controlling the straits between the Black Sea and the Aegean, making it simultaneously the gateway for Byzantine trade and the primary target of any power seeking to dominate the eastern Mediterranean — created the strategic imperative for maintaining a powerful navy to defend the city's access to the sea",
            "The Arab conquests' creation of a powerful Islamic naval force in the eastern Mediterranean (from the 640s) — which challenged Byzantine maritime supremacy and launched the two great sieges of Constantinople (674–678 and 717–718) — drove the development of Greek fire as the decisive counter-weapon",
            "The Byzantine Empire's commercial wealth — drawn from control of the Constantinople trade route between the Black Sea and the Mediterranean — provided the fiscal basis for maintaining the most technically advanced navy in the medieval Mediterranean, with the dromon's Greek fire siphons representing a capital investment in naval technology"
        ],
        "effects": [
            "Greek fire's defeat of the Arab sieges of Constantinople (674–678 CE and 717–718 CE) — stopping the Arab naval advance that might otherwise have conquered the Byzantine capital and opened Europe to Islamic expansion from the east simultaneously with the advance through Spain — is one of the most consequential naval engagements in history, preserving the Byzantine Empire for another 700+ years",
            "The Chrysobull of 1082 — Alexios I's grant of complete commercial privileges to Venice in exchange for naval support against the Normans — eliminated Byzantine commercial revenues from the eastern Mediterranean trade, creating the Venetian commercial dominance that transformed Venice into the dominant trading power of the medieval Mediterranean and ultimately facilitated the Venetian-directed Fourth Crusade (1204)",
            "The Byzantine Navy's Greek fire — whose formula was known to very few Byzantine officials and was never effectively transferred to any other power — disappeared with the Byzantine Empire, leaving posterity with one of history's most intriguing technological mysteries: the weapon that preserved Christian Europe from Arab conquest cannot be replicated despite 800 years of scholarly investigation",
            "The Byzantine Navy's dromon design — and the tactical doctrine of Greek fire deployment — influenced the naval architecture and tactics of the Islamic and Crusader navies that succeeded Byzantine Mediterranean dominance, creating the framework of medieval Mediterranean naval warfare"
        ],
        "relationships": [
            {"entity": "Greek fire (incendiary naval weapon, formula unknown, Arab sieges defeated)", "relationship": "ORIGINATOR_AND_PRIMARY_USER_OF", "note": "Greek fire — deployed from dromon bow siphons — stopped the Arab sieges of Constantinople that might otherwise have ended the Byzantine Empire"},
            {"entity": "Arab sieges of Constantinople (674–678 CE and 717–718 CE, stopped by Greek fire)", "relationship": "DEFENDER_OF_CONSTANTINOPLE_IN_THE", "note": "The Byzantine Navy's Greek fire stopped the Arab sieges of Constantinople — preserving the Byzantine Empire for another 700 years"},
            {"entity": "Chrysobull of 1082 (Alexios I Komnenos, Venice trade privileges, Byzantine commercial collapse)", "relationship": "INSTITUTIONAL_DECLINE_INITIATED_BY_THE_NAVAL_CONSEQUENCES_OF_THE", "note": "Alexios I's 1082 grant of Venice trade privileges — in exchange for naval support — eliminated Byzantine commercial revenues and created Venetian eastern Mediterranean dominance"},
            {"entity": "Fourth Crusade (1204, Latin capture of Constantinople, Venetian facilitation)", "relationship": "INSTITUTIONAL_WEAKNESS_EXPLOITED_BY_THE_VENETIAN_COMMERCIAL_DOMINANCE_THAT_FACILITATED_THE", "note": "The Byzantine Navy's decline — following the Chrysobull of 1082 — contributed to the Venetian commercial dominance that directed the Fourth Crusade against Constantinople"},
            {"entity": "Dromon bireme galley (primary vessel, Greek fire siphon deployment)", "relationship": "PRIMARY_VESSEL_WAS_THE", "note": "The dromon's Greek fire bow siphons gave the Byzantine fleet a decisive tactical advantage that no opponent could counter in open naval engagement"}
        ],
    }),

    ("venetian-navy", {
        "summary": (
            "The Venetian Navy (the maritime force of the Venetian Republic — La Serenissima, founded c. 697 CE, dissolved 1797 by Napoleon) was the most commercially productive and tactically innovative navy of the medieval and early modern Mediterranean — the primary instrument through which Venice maintained a commercial empire that controlled the eastern Mediterranean trade routes for 500 years (c. 1100–1600 CE) and produced the Arsenal of Venice, the world's first industrial production facility and the model for all subsequent state shipyards. At its peak, the Venice Arsenal employed 16,000 workers and could produce a complete galley in one day.\n\n"
            "The Venetian Navy's defining achievements include the Fourth Crusade (1202–1204 — Venice's Doge Enrico Dandolo directed the Crusade against Constantinople, securing the Venetian commercial empire in the eastern Mediterranean), the Battle of Lepanto (1571 — the Venetian-led Holy League defeated the Ottoman Navy in the last great galley battle), and the development of the galley as the primary Mediterranean warship — with the Venetian galea grossa (great galley) as the merchant and military vessel that dominated Mediterranean trade for 300 years.\n\n"
            "The Arsenal of Venice (est. c. 1104) — the world's first large-scale industrial facility, employing division of labour, standardised components, and assembly-line production centuries before the Industrial Revolution — is the primary organisational innovation of pre-industrial capitalism. Adam Smith's observation of the Arsenal's division of labour (c. 1766) directly influenced his analysis in The Wealth of Nations (1776), making the Venetian Navy the indirect institutional ancestor of modern economic theory."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most commercially productive medieval Mediterranean navy (Venetian Republic, c. 697–1797 CE); Arsenal of Venice (est. c. 1104) — world's first industrial production facility, 16,000 workers, complete galley in one day; Fourth Crusade (1202–1204, Doge Enrico Dandolo directed against Constantinople); Battle of Lepanto (1571, Holy League vs Ottoman Navy, last great galley battle); galea grossa; 500 years of eastern Mediterranean trade route control (c. 1100–1600 CE); Adam Smith observation — direct influence on The Wealth of Nations (1776).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Venice's geographic position — islands in a lagoon at the head of the Adriatic, with no agricultural land but natural harbour protection — created the structural necessity for maritime commerce and naval power as the only viable economic strategy, making the Venetian Navy an institutional expression of Venice's physical geography",
            "The Venetian Republic's commercial relationship with Byzantium — the Byzantine Chrysobull of 1082 giving Venice extraordinary trading privileges — provided the commercial dominance of the eastern Mediterranean that created the wealth funding the Arsenal and the naval forces that protected Venetian trade routes",
            "The Fourth Crusade's redirection against Constantinople (1204) — engineered by Doge Enrico Dandolo to secure Venetian commercial interests — gave Venice direct control of Byzantine trading privileges and created the Stato da Mar (the Venetian maritime empire) that extended from Venice to Cyprus"
        ],
        "effects": [
            "The Arsenal of Venice's industrial organisation — division of labour, standardised components, assembly-line production — was the world's first large-scale industrial facility, producing ships at a speed and cost that no competitor could match, and directly inspiring Adam Smith's analysis of the division of labour in The Wealth of Nations (1776), making it the institutional ancestor of modern industrial economics",
            "The Fourth Crusade's capture of Constantinople (1204) — directed by Venice to secure its commercial interests — ended Byzantine imperial power and created the Latin Empire, distributing Byzantine territories to Western powers and permanently weakening the eastern Christian world, contributing to the eventual Ottoman conquest (1453)",
            "The Battle of Lepanto (1571) — where the Venetian-led Holy League destroyed the Ottoman Navy in the last great galley battle — temporarily halted Ottoman naval expansion in the Mediterranean, preserving Venice's commercial position for another generation and establishing the psychological precedent that Ottoman military power could be defeated",
            "The Venetian Navy's 500-year dominance of eastern Mediterranean trade — controlling the spice routes from Alexandria to the Venetian markets — made Venice the wealthiest city in Europe per capita and the primary conduit for luxury goods from Asia to Europe, until Vasco da Gama's discovery of the Cape route (1498) began the diversion of spice trade away from Venice"
        ],
        "relationships": [
            {"entity": "Arsenal of Venice (est. c. 1104, world's first industrial facility, 16,000 workers)", "relationship": "INSTITUTIONAL_HOME_OF_THE_WORLD'S_FIRST_INDUSTRIAL_PRODUCTION_FACILITY", "note": "The Arsenal's division of labour and assembly-line production — inspected by Adam Smith — directly influenced The Wealth of Nations and modern economic theory"},
            {"entity": "Fourth Crusade (1202–1204, Doge Enrico Dandolo, Constantinople sack, Stato da Mar)", "relationship": "NAVAL_INSTRUMENT_OF_THE_VENETIAN-DIRECTED", "note": "Doge Dandolo's direction of the Fourth Crusade against Constantinople — securing Venetian commercial interests — created the Stato da Mar that extended Venetian maritime empire"},
            {"entity": "Battle of Lepanto (1571, Holy League vs Ottoman Navy, last great galley battle)", "relationship": "PRIMARY_NAVAL_CONTRIBUTOR_TO_THE", "note": "Lepanto — the last great galley battle — temporarily halted Ottoman naval expansion and preserved Venice's commercial Mediterranean position"},
            {"entity": "Adam Smith / The Wealth of Nations (1776, Arsenal division of labour inspiration)", "relationship": "INDUSTRIAL_ORGANISATION_DIRECTLY_INSPIRED_THE_FOUNDATIONAL_ECONOMIC_ANALYSIS_OF", "note": "Smith's observation of the Arsenal's division of labour directly influenced The Wealth of Nations — making the Venetian Navy the institutional ancestor of modern economic theory"},
            {"entity": "Vasco da Gama Cape route (1498, spice trade diversion from Venice, commercial decline)", "relationship": "COMMERCIAL_DOMINANCE_OF_EASTERN_MEDITERRANEAN_SPICE_TRADE_UNDERMINED_BY_THE", "note": "Da Gama's Cape route (1498) diverted the Asian spice trade away from Venice — beginning the long decline of Venetian commercial supremacy"}
        ],
    }),

    ("ottoman-navy", {
        "summary": (
            "The Ottoman Navy (Donanma-yı Hümayûn — est. in earnest under Sultan Mehmed II in the 1450s–1460s, reaching its peak power under Hayreddin Barbarossa and Suleiman the Magnificent in the 16th century) was the dominant naval force in the eastern Mediterranean during the height of Ottoman imperial power — controlling the sea lanes from the Black Sea to the Aegean, the Red Sea, and the Persian Gulf, and posing the most serious threat to Christian Mediterranean powers since the Arab naval expansion of the 7th century. The Ottoman conquest of Constantinople (1453) required the Ottoman Navy to physically carry warships over land to bypass the harbour chain.\n\n"
            "The Ottoman Navy's defining moment was Hayreddin Barbarossa's career (c. 1478–1546 — Kapudan-i Deryâ, Grand Admiral of the Fleet) — the Barbary corsair who became the Ottoman Grand Admiral, reorganised the fleet, defeated the Holy Roman Emperor's navy at the Battle of Preveza (1538), and effectively made the Ottoman Empire the dominant Mediterranean naval power for a generation. The Battle of Preveza — the greatest Ottoman naval victory — is among the least-known decisive battles of the 16th century.\n\n"
            "The Battle of Lepanto (1571) — in which the Holy League (Spain, Venice, the Papacy) destroyed the Ottoman fleet — is traditionally considered the turning point of Ottoman naval power, though the Ottomans rebuilt their fleet within a year and continued to control the eastern Mediterranean. The Ottoman Navy's decline in the 18th–19th centuries — as European naval technology advanced — contributed to the broader Ottoman military weakness that drove the 'Eastern Question' and ultimately the Empire's dissolution."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Dominant eastern Mediterranean naval force at Ottoman peak (est. 1450s Mehmed II); Hayreddin Barbarossa (c. 1478–1546, Kapudan-i Deryâ Grand Admiral) — reorganised fleet, Battle of Preveza (1538, greatest Ottoman naval victory); Constantinople conquest (1453) — warships carried over land; Black Sea, Aegean, Red Sea, Persian Gulf control; Battle of Lepanto (1571, Holy League, fleet destroyed but rebuilt in one year); Suleiman the Magnificent; Ottoman naval decline 18th–19th century contributing to Eastern Question.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Mehmed II's conquest of Constantinople (1453) — which required the Ottoman Navy to carry warships overland to bypass the harbour chain blocking the Golden Horn — demonstrated the Ottoman commitment to naval capability as an essential instrument of imperial expansion, and provided the Bosphorus gateway that made the Black Sea an Ottoman lake",
            "Hayreddin Barbarossa's recruitment as Grand Admiral (1533) — bringing the most experienced corsair commander in the Mediterranean into the Ottoman service — gave the Ottoman Navy the operational and tactical expertise that transformed it from a coastal defence force into a Mediterranean power projection instrument",
            "The Ottomans' control of the Bosphorus and Dardanelles — the straits connecting the Black Sea to the Mediterranean — provided the strategic chokepoint that made the Ottoman Navy simultaneously the guardian of Constantinople and the controller of the most commercially valuable sea lanes in the medieval and early modern world"
        ],
        "effects": [
            "The Ottoman Navy's Mediterranean dominance under Barbarossa (1530s–1540s) — including the Battle of Preveza (1538) and the systematic harassment of Spanish and Italian coastal cities — created the corsair economic system of the Barbary Coast that would persist for 300 years, with North African ports under Ottoman suzerainty raiding European shipping and coastlines until the French conquest of Algeria (1830)",
            "The Battle of Lepanto (1571) — while destroying the Ottoman fleet — demonstrated that Ottoman naval power could be defeated by a united Christian coalition, breaking the psychological aura of Ottoman naval invincibility and contributing to the broader stalling of Ottoman westward expansion in the late 16th century",
            "The Ottoman Navy's control of the Red Sea and the spice routes — challenging Portuguese dominance of the Indian Ocean trade — created the strategic naval competition between the Ottoman and Portuguese empires in the 16th century, a less-studied but significant dimension of the global imperial competition that shaped the early modern world",
            "The Ottoman Navy's decline in the 18th century — as Russian and British naval power advanced — contributed to the Ottoman military vulnerability that created the 'Eastern Question': the diplomatic problem of managing Ottoman imperial decline in a way that preserved European balance of power, which ultimately could not be resolved without the catastrophic violence of the First World War"
        ],
        "relationships": [
            {"entity": "Hayreddin Barbarossa (Kapudan-i Deryâ 1533–1546, Battle of Preveza, Mediterranean dominance)", "relationship": "GREATEST_COMMANDER_AND_ORGANISATIONAL_REFORMER_WAS", "note": "Barbarossa's recruitment as Grand Admiral — bringing corsair expertise into Ottoman service — transformed the navy into the dominant Mediterranean power projection force"},
            {"entity": "Battle of Preveza (1538, greatest Ottoman naval victory, Holy Roman Emperor's navy defeated)", "relationship": "GREATEST_NAVAL_VICTORY_WAS_THE", "note": "Preveza — Barbarossa's destruction of the combined Christian fleet — is the greatest Ottoman naval victory and among the most consequential battles of the 16th century"},
            {"entity": "Ottoman conquest of Constantinople (1453, warships carried over land to bypass harbour chain)", "relationship": "INSTITUTIONALLY_CREATED_BY_THE_NAVAL_REQUIREMENTS_OF_THE", "note": "The 1453 conquest — requiring warships to be physically carried over land — demonstrated Ottoman commitment to naval capability as a strategic instrument"},
            {"entity": "Battle of Lepanto (1571, Holy League, fleet destroyed, rebuilt within a year)", "relationship": "GREATEST_DEFEAT_BUT_RAPID_REBUILDING_AFTER_THE", "note": "Lepanto destroyed the Ottoman fleet but the rapid one-year rebuild demonstrated Ottoman industrial capacity and the limited strategic impact of even decisive naval victories"},
            {"entity": "Barbary Coast corsairs (North African ports, 300 years of Mediterranean raiding, French Algeria 1830)", "relationship": "STRATEGIC_PATRON_AND_PROTECTOR_OF_THE", "note": "The Ottoman Navy's support for Barbary corsairs created the 300-year North African raiding system that persisted until the French conquest of Algeria (1830)"}
        ],
    }),

    ("imperial-japanese-navy", {
        "summary": (
            "The Imperial Japanese Navy (Dai-Nippon Teikoku Kaigun — est. 1869 as the Meiji government's naval modernisation programme, dissolved 1947) was the third-largest navy in the world by 1941 — the most powerful navy in the Asia-Pacific region, and the instrument of the largest and most rapidly executed strategic surprise attack in naval history: the Pearl Harbor attack (7 December 1941), which destroyed the US Pacific Fleet battleship force and opened the Pacific War. The Imperial Japanese Navy's six carrier strike force (Kido Butai) that attacked Pearl Harbor represented the most advanced naval aviation force in the world at that date.\n\n"
            "The Imperial Japanese Navy traced its origins to the Meiji Restoration's decision to model the new navy on the British Royal Navy — with British officers advising, Japanese officers trained at Dartmouth, and Japanese ships initially built in British shipyards. The Battle of Tsushima (1905) — in which Admiral Togo Heihachiro's fleet annihilated the Russian Baltic Fleet (which had sailed 18,000 miles to its destruction) — is considered the most decisive naval victory since Trafalgar and established the Imperial Japanese Navy's global reputation.\n\n"
            "The IJN's strategic trajectory — from the tactical brilliance of Pearl Harbor and the rapid conquest of the Philippines, Dutch East Indies, and Pacific islands (December 1941–April 1942) through the turning point of Midway (June 1942, all four carriers of the Kido Butai lost in one day) to the systematic attrition of its carrier aviation and ultimately its battleship force — traced the complete arc of a naval power's rise and fall in four years."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Third-largest navy in world by 1941; Pearl Harbor attack (7 December 1941 — largest strategic surprise in naval history, US Pacific Fleet battleship force destroyed); Kido Butai (six-carrier strike force, most advanced naval aviation 1941); Meiji naval modernisation (est. 1869, British Royal Navy model); Battle of Tsushima (1905, Admiral Togo, Russian Baltic Fleet annihilated — most decisive naval victory since Trafalgar); Battle of Midway (June 1942, Kido Butai four carriers lost in one day, turning point); est. 1869, dissolved 1947.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Meiji Restoration's decision to model the new Japanese navy on the British Royal Navy — the world's dominant naval force — provided the institutional template, training system, and technological standard that created the Imperial Japanese Navy as one of the world's most effective naval forces within one generation",
            "The Battle of Tsushima's demonstration of Japanese naval effectiveness (1905) — and the US Great White Fleet's circumnavigation (1907–1909) as a response to Japan's growing power — created the strategic competition between Japan and the United States that would ultimately produce the Pearl Harbor attack",
            "The IJN's development of carrier aviation as its primary offensive weapon — inspired by the Royal Navy's pioneering work but quickly surpassing it — created the technological capability for the Pearl Harbor strike, with Japanese aviators and aircraft (the Zero fighter, the Type 97 torpedo bomber) representing the world's most advanced carrier air arm in 1941"
        ],
        "effects": [
            "The Pearl Harbor attack (7 December 1941) — destroying the US Pacific Fleet battleship force but (crucially) missing the US aircraft carriers, which were at sea — triggered the US entry into World War II, transforming what had been a European conflict into the true World War, and ultimately producing the coalition that defeated both Germany and Japan",
            "The Battle of Midway (June 1942) — in which US carriers destroyed all four Kido Butai carriers in a single day — permanently removed Japan's offensive carrier capability and shifted the strategic balance of the Pacific War to the United States, establishing the carrier as the dominant capital ship and ending the battleship era",
            "The IJN's development of the long-range carrier strike — demonstrated at Pearl Harbor — transformed naval warfare, establishing the carrier air group as the dominant naval weapon and making the battleship obsolete, with direct consequences for the design and employment of every subsequent navy in the world",
            "The Pearl Harbor attack's political consequences — the instant unification of American public opinion that had been divided over intervention ('a date which will live in infamy', Roosevelt) — produced the political conditions for the unprecedented US mobilisation (from 189,000 army soldiers to 8.3 million by 1945) that ultimately defeated both Japan and Nazi Germany"
        ],
        "relationships": [
            {"entity": "Pearl Harbor attack (7 December 1941, Kido Butai, Pacific War opening, US entry into WWII)", "relationship": "EXECUTOR_OF_THE_DEFINING_ATTACK_OF_THE_PACIFIC_WAR", "note": "Pearl Harbor — the largest strategic surprise in naval history — triggered US entry into WWII and produced the coalition that defeated Germany and Japan"},
            {"entity": "Battle of Tsushima (1905, Admiral Togo, Russian Baltic Fleet annihilated)", "relationship": "GREATEST_EARLY_VICTORY_ESTABLISHING_GLOBAL_REPUTATION_WAS_THE", "note": "Tsushima — the most decisive naval battle since Trafalgar — established the IJN's reputation as one of the world's most effective naval forces"},
            {"entity": "Battle of Midway (June 1942, four Kido Butai carriers lost, Pacific War turning point)", "relationship": "DECISIVE_DEFEAT_THAT_ENDED_OFFENSIVE_CAPABILITY_WAS_THE", "note": "Midway's loss of all four Kido Butai carriers permanently ended Japan's offensive naval capability and shifted the Pacific War's strategic balance"},
            {"entity": "Meiji Restoration naval modernisation (est. 1869, British Royal Navy model)", "relationship": "INSTITUTIONAL_CREATION_OF_THE", "note": "The Meiji Restoration's British Royal Navy model — Japanese officers trained at Dartmouth, ships built in British yards — created the IJN within one generation"},
            {"entity": "Carrier aviation doctrine (Pearl Harbor strike, carrier as dominant capital ship, battleship obsolescence)", "relationship": "DEMONSTRATED_AND_ESTABLISHED_THE_DOMINANCE_OF", "note": "The IJN's carrier strike doctrine — demonstrated at Pearl Harbor — transformed naval warfare, establishing the carrier as the dominant capital ship and ending the battleship era"}
        ],
    }),

    ("ancient-egyptian-navy", {
        "summary": (
            "The Ancient Egyptian Navy (the maritime forces of pharaonic Egypt — with the earliest evidence from the Old Kingdom period, c. 2500 BCE, with systematic naval forces from the New Kingdom, c. 1550–1070 BCE) was the oldest systematically documented naval force in history — the instrument through which Egypt controlled the Nile River, the Red Sea trade routes to Punt and Arabia, and the eastern Mediterranean coast from the New Kingdom's expansion into Canaan and Nubia. Egypt's naval forces are the earliest example of state-organised sea power for both commercial and military purposes.\n\n"
            "The most significant ancient Egyptian naval engagement is the Battle of the Delta (c. 1175 BCE) — in which Ramesses III's fleet defeated the Sea Peoples' naval invasion in the Nile Delta, preventing a catastrophic migration-invasion that had already destroyed the Hittite Empire, devastated the Mycenaean Greek kingdoms, and threatened the entire eastern Mediterranean civilisational system. This naval battle preserved Egyptian civilisation while the surrounding Bronze Age world collapsed.\n\n"
            "The Egyptian Navy's most visible institutional legacy is the Red Sea trade system — the routes to Punt (Somalia/Eritrea) that brought myrrh, ebony, ivory, and exotic animals to Egypt for 1,500+ years, documented in Queen Hatshepsut's expedition reliefs at Deir el-Bahri (c. 1470 BCE) and the Wadi Hammamat inscriptions. The Red Sea trade routes established by pharaonic naval expeditions were the precursors to the later Roman and Arab Red Sea commerce and ultimately to the Indian Ocean trade network."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest systematically documented naval force in history (earliest evidence c. 2500 BCE Old Kingdom; systematic forces from New Kingdom c. 1550–1070 BCE); Battle of the Delta (c. 1175 BCE, Ramesses III, Sea Peoples defeated — Egyptian civilisation preserved while Bronze Age collapse destroyed surrounding cultures); Red Sea trade routes to Punt (myrrh, ebony, ivory — Queen Hatshepsut expedition c. 1470 BCE); Nile River control; eastern Mediterranean coast control; earliest example of state sea power for commercial and military purposes.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Nile River's role as Egypt's primary transportation and communication artery — making naval control of the river essential for internal governance, military movement, and commercial distribution — drove the development of Egyptian river craft from the earliest dynastic period, creating the institutional foundation of naval capability",
            "The New Kingdom's imperial expansion — into Canaan, Nubia, and the eastern Mediterranean coast — required maritime supply lines, amphibious capability, and naval forces to support land armies operating in coastal regions, driving the development of the Egyptian Navy as a military force alongside its commercial role",
            "The Red Sea's position as the primary route to the exotic luxury goods of Punt and Arabia — myrrh, frankincense, ebony, ivory, and exotic animals essential for pharaonic religious ritual and royal display — created the commercial imperative for the state-organised Red Sea trade expeditions that represent the earliest systematic maritime exploration in history"
        ],
        "effects": [
            "The Battle of the Delta's defeat of the Sea Peoples (c. 1175 BCE) — preserving Egyptian civilisation while the Hittite Empire, Mycenaean Greece, and the Levantine city-states collapsed simultaneously in the Bronze Age Collapse — made the Egyptian Navy the institution that maintained continuity of Egyptian civilisation through the most catastrophic civilisational disruption in the ancient world before the fall of Rome",
            "The Red Sea trade routes established by the pharaonic navy — particularly Hatshepsut's expedition to Punt (c. 1470 BCE) — created the commercial and navigational infrastructure that was later adopted by Ptolemaic Greek, Roman, and ultimately Arab merchants, making the Egyptian Navy the originator of the Indian Ocean trade network that would eventually connect the Mediterranean to India and China",
            "The Egyptian Navy's Nile control — which made the river simultaneously a military highway, commercial artery, and communication system — created the administrative template for river-based state power that influenced subsequent riparian empires from Mesopotamia to China",
            "The Egyptian Navy's preserved relief inscriptions and papyri — particularly Hatshepsut's Deir el-Bahri expedition reliefs — are the most detailed documentation of ancient naval operations surviving from the Bronze Age, providing irreplaceable evidence for the technology, organisation, and practice of the world's first state-organised navy"
        ],
        "relationships": [
            {"entity": "Battle of the Delta (c. 1175 BCE, Ramesses III, Sea Peoples defeated, Bronze Age Collapse context)", "relationship": "PRESERVED_EGYPTIAN_CIVILISATION_THROUGH_ITS_VICTORY_IN_THE", "note": "The Battle of the Delta — stopping the Sea Peoples who had already destroyed the Hittite Empire — preserved Egyptian civilisation through the Bronze Age Collapse"},
            {"entity": "Queen Hatshepsut (Red Sea expedition to Punt c. 1470 BCE, Deir el-Bahri reliefs)", "relationship": "MOST_CELEBRATED_COMMERCIAL_EXPEDITION_COMMISSIONED_BY", "note": "Hatshepsut's Punt expedition — documented at Deir el-Bahri — is the most detailed surviving record of ancient naval commercial operations"},
            {"entity": "Sea Peoples (Bronze Age Collapse, Hittite Empire destroyed, Mycenaean kingdoms devastated)", "relationship": "NAVAL_FORCE_THAT_DEFEATED_THE_INVASION_OF_THE", "note": "The Egyptian Navy's defeat of the Sea Peoples — who had destroyed the Hittite Empire and devastated Mycenae — preserved Egyptian civilisation through the Bronze Age Collapse"},
            {"entity": "Red Sea trade routes (Punt, Arabia, myrrh, frankincense, ivory — Indian Ocean trade precursors)", "relationship": "ESTABLISHED_AND_MAINTAINED_THE", "note": "The Egyptian Navy's Red Sea trade routes — to Punt and Arabia — were the precursors to the later Roman, Arab, and ultimately global Indian Ocean trade network"},
            {"entity": "Ramesses III (Battle of the Delta commander, Sea Peoples defeat)", "relationship": "MOST_SIGNIFICANT_NAVAL_COMMANDER_WAS", "note": "Ramesses III's direction of the Battle of the Delta — defeating the Sea Peoples in Egypt's greatest naval engagement — preserved Egyptian civilisation at the moment of Bronze Age civilisational collapse"}
        ],
    }),

    ("confederate-states-navy", {
        "summary": (
            "The Confederate States Navy (est. 1861, dissolved 1865 — the naval arm of the Confederate States of America during the American Civil War) was a largely improvised naval force that punched dramatically above its weight through technological innovation — developing and deploying the first combat submarine (H.L. Hunley, sinking USS Housatonic on 17 February 1864, the first submarine attack in naval history), commissioning the first effective ironclad warship (CSS Virginia, formerly USS Merrimack, 1862), and establishing the first systematic use of naval mines (torpedoes) as a defensive weapon that sank more Union vessels than any other Confederate naval weapon.\n\n"
            "The Confederate States Navy was created from almost nothing — the Confederacy had no shipbuilding industry, no established navy, and was immediately subjected to the Union blockade (the Anaconda Plan) that progressively strangled Confederate commerce and supply. Secretary of the Navy Stephen Mallory's strategy — substituting technological innovation for the industrial capacity the Confederacy lacked — produced a series of naval firsts that permanently changed naval warfare even though they failed to break the blockade.\n\n"
            "The CSS Virginia's engagement with USS Monitor at Hampton Roads (8–9 March 1862 — the Battle of Hampton Roads, the first ironclad battle in history) obsoleted every wooden warship in the world overnight, demonstrating that steam-powered iron-hulled warships had completely superseded the age of sail. Every naval power in the world immediately began converting or building ironclad fleets, making Hampton Roads the most consequential two-day period in the history of naval warfare."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First combat submarine (H.L. Hunley, sinking USS Housatonic 17 February 1864 — first submarine attack in naval history); first effective ironclad (CSS Virginia/Merrimack, 1862); Battle of Hampton Roads (8–9 March 1862 — first ironclad battle, wooden warships obsoleted worldwide overnight); first systematic naval mines; Confederate States of America naval arm (est. 1861, dissolved 1865); Secretary Stephen Mallory strategy — technological innovation substituting for industrial capacity; Union blockade Anaconda Plan context.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Union's immediate imposition of the Anaconda Plan blockade — which cut Confederate access to overseas supply and markets — created the strategic imperative for the Confederate Navy's technological innovations: if the Confederacy could not match Union naval numbers, it had to develop weapons that could break the blockade through asymmetric means",
            "Secretary of the Navy Stephen Mallory's strategic decision to invest Confederate naval resources in technological innovation (ironclads, submarines, torpedoes) rather than attempting to build a conventional fleet — recognising the Confederacy's industrial limitations — drove the series of naval firsts that permanently changed naval warfare",
            "The availability of the captured USS Merrimack's hull at the Norfolk Navy Yard — which Confederate engineers converted to the CSS Virginia by adding an iron-plated casemate — provided the physical resource for the first effective ironclad warship without the industrial capacity to build one from scratch"
        ],
        "effects": [
            "The Battle of Hampton Roads (March 1862) — the CSS Virginia's engagement with USS Monitor, the first battle between iron-hulled warships — made every wooden warship in every navy in the world obsolete overnight, driving an immediate global naval arms race in ironclad construction and permanently changing the nature of naval architecture",
            "The H.L. Hunley's sinking of USS Housatonic (17 February 1864) — the first successful submarine attack in naval history — established the submarine as a potential naval weapon and initiated the development trajectory that led to the First World War U-boat campaign and the subsequent history of submarine warfare",
            "The Confederate Navy's systematic use of naval mines (called 'torpedoes') — which sank more Union vessels than any other Confederate naval weapon — established the mine as a routine component of naval warfare, directly influencing the mine warfare practices of the First and Second World Wars",
            "The Confederate Navy's technological innovations — ironclads, submarines, mines, commerce raiders (CSS Alabama, which captured or destroyed 65 Union vessels before being sunk off Cherbourg in 1864) — established the principle that technological innovation can compensate for material inferiority, influencing asymmetric naval strategy from the German U-boat campaigns to contemporary drone warfare"
        ],
        "relationships": [
            {"entity": "CSS Virginia / USS Merrimack (first effective ironclad, Hampton Roads 1862)", "relationship": "COMMISSIONED_AND_DEPLOYED_THE_FIRST_EFFECTIVE_IRONCLAD_WARSHIP", "note": "The CSS Virginia's Hampton Roads engagement made every wooden warship in the world obsolete overnight, permanently changing naval architecture"},
            {"entity": "H.L. Hunley (first combat submarine, USS Housatonic sinking 17 February 1864)", "relationship": "DEVELOPED_AND_DEPLOYED_THE_WORLD'S_FIRST_COMBAT_SUBMARINE", "note": "The Hunley's sinking of USS Housatonic — the first successful submarine attack in history — initiated the development trajectory of submarine warfare"},
            {"entity": "Battle of Hampton Roads (8–9 March 1862, first ironclad battle, wooden warships obsoleted)", "relationship": "PARTICIPATED_IN_THE_MOST_CONSEQUENTIAL_TWO-DAY_PERIOD_IN_NAVAL_WARFARE_HISTORY", "note": "Hampton Roads — the first ironclad battle — made wooden warships immediately obsolete worldwide, triggering a global naval arms race"},
            {"entity": "Stephen Mallory (Confederate Secretary of the Navy, technological innovation strategy)", "relationship": "STRATEGIC_ARCHITECT_OF_TECHNOLOGICAL_INNOVATION_APPROACH_WAS", "note": "Mallory's decision to substitute technological innovation for industrial capacity drove the Confederate Navy's series of naval firsts"},
            {"entity": "Anaconda Plan Union blockade (Confederate commerce strangulation, technological innovation driver)", "relationship": "STRATEGIC_PRESSURE_DRIVING_TECHNOLOGICAL_INNOVATION_WAS_THE", "note": "The Union blockade's strategic pressure — cutting Confederate supply — drove the Confederate Navy's asymmetric technological innovations"}
        ],
    }),

    ("austro-hungarian-navy", {
        "summary": (
            "The Austro-Hungarian Navy (k.u.k. Kriegsmarine — Kaiserliche und Königliche Kriegsmarine, est. as the Austrian Imperial Navy in 1797, becoming the Austro-Hungarian Navy in 1867, dissolved 1918) was the smallest of the major European navies but one of the most innovative — achieving its greatest victory at the Battle of Lissa (1866), the first naval battle between ironclad fleets in which Austria's smaller fleet defeated Italy's larger one through the tactical innovation of ramming, demonstrating that ironclad construction had temporarily negated gunnery superiority. The battle's misleading lesson (that ramming was viable) caused every major navy to build rams on their warships for the next 30 years.\n\n"
            "The Austro-Hungarian Navy was landlocked in its strategic logic — the Habsburg Empire's primary interests were continental, and the navy existed primarily to defend the Adriatic coast and support Austrian Adriatic commerce rather than to project power globally. The navy's primary naval base at Pola (now Pula, Croatia) and the secondary bases at Trieste, Cattaro (Kotor), and Sebenico (Šibenik) reflected the Adriatic strategic focus that limited Austrian naval ambitions throughout its history.\n\n"
            "The Austro-Hungarian Navy's most significant officer was Admiral Wilhelm von Tegetthoff (1827–1871) — who commanded at Lissa, invented the modern concept of naval tactical doctrine (Tegetthoff's Tactics), and is considered one of the greatest naval commanders of the ironclad era. The Austrian Navy's dissolution in 1918 — and the distribution of its fleet to Italy, France, and the successor states — ended 120 years of Habsburg maritime power and created the naval forces of Yugoslavia, Czechoslovakia's Danube flotilla, and contributed to the Italian Navy's interwar strength."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Smallest major European navy but highly innovative (k.u.k. Kriegsmarine, est. 1797–1918); Battle of Lissa (1866 — first ironclad naval battle, Austria defeated larger Italian fleet through ramming, most misleading tactical lesson in naval history — every navy built rams for 30 years); Admiral Wilhelm von Tegetthoff (1827–1871, Lissa commander, modern naval tactical doctrine originator); Adriatic focus, Pola naval base; 1918 dissolution and fleet distribution to Italy and successor states.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Habsburg Empire's Adriatic coastline — extending from Trieste to the Dalmatian coast and including the crucial naval base at Pola — created the strategic imperative for an Adriatic defensive navy, even though Austria's primary strategic interests and military investment were continental rather than maritime",
            "Austria's Italian policy — particularly the competition with Sardinia/Italy for control of the Po Valley and Venetia — drove Austrian naval investment in the 1850s–1860s as Italian unification created a rival naval power in the Adriatic that Austria needed to match",
            "The ironclad revolution of the 1860s — which made wooden warship fleets instantly obsolete and required major powers to invest in entirely new naval technology — created the context for the Battle of Lissa (1866), where both Austrian and Italian fleets were operating new ironclad technology without established doctrine"
        ],
        "effects": [
            "The Battle of Lissa's demonstration that ramming (which sank Italian ironclad Re d'Italia when Tegetthoff's flagship Ferdinand Max rammed it at full speed) could destroy ironclad warships caused every major navy to add ram bows to their warships for the next 30 years — despite the fact that Lissa's result was largely accidental and the tactic was never again used successfully in combat — making it one of the most misleading tactical lessons in naval history",
            "Admiral Tegetthoff's tactical doctrine — developed from the Battle of Lissa's experience of controlling fast-moving ironclad squadrons in close combat — influenced naval tactical thinking in the 1870s–1880s and established some of the principles of squadron manoeuvre that were later developed into the line-ahead tactical system of pre-dreadnought naval warfare",
            "The Austro-Hungarian Navy's 1918 dissolution and fleet distribution — with major warships going to Italy, France, and the successor states — contributed to Italy's post-WWI naval strength and created the naval forces of the newly independent South Slavic (Yugoslav) state, shaping the Adriatic naval balance that would be contested in the Second World War",
            "The Austro-Hungarian Navy's technical and engineering culture — which produced innovations in torpedo boat design, mine warfare, and submarine development in the early 20th century — contributed to the naval technology base that Austria-Hungary's successor states (particularly Yugoslavia) incorporated into their interwar naval forces"
        ],
        "relationships": [
            {"entity": "Battle of Lissa (1866, first ironclad naval battle, Italy's larger fleet defeated by Austria)", "relationship": "GREATEST_VICTORY_IN_THE", "note": "Lissa — the first ironclad naval battle — produced the most misleading tactical lesson in naval history: the ram bow, adopted by every navy for 30 years"},
            {"entity": "Admiral Wilhelm von Tegetthoff (1827–1871, Lissa commander, modern naval tactical doctrine)", "relationship": "GREATEST_COMMANDER_AND_MOST_INFLUENTIAL_OFFICER_WAS", "note": "Tegetthoff — who commanded at Lissa and developed modern naval tactical doctrine — is considered one of the greatest naval commanders of the ironclad era"},
            {"entity": "Ram bow adoption (30-year worldwide naval arms race consequence of misleading Lissa lesson)", "relationship": "MISLEADING_TACTICAL_LESSON_OF_WHICH_DROVE_THE_UNIVERSAL", "note": "Lissa's demonstration of ramming drove every major navy to add ram bows — a tactic never again successfully used in combat — for the next 30 years"},
            {"entity": "Adriatic strategic focus (Pola naval base, Trieste, Dalmatian coast, continental Habsburg priorities)", "relationship": "STRATEGIC_SCOPE_LIMITED_TO_THE", "note": "The Austro-Hungarian Navy's Adriatic focus — reflecting continental Habsburg priorities — limited its ambitions throughout its 120-year history"},
            {"entity": "1918 dissolution and fleet distribution (Italy, France, successor states, Yugoslav naval origins)", "relationship": "DISSOLVED_IN_1918_WITH_FLEET_DISTRIBUTED_TO", "note": "The 1918 dissolution's distribution of the Austrian fleet contributed to Italy's interwar naval strength and created the Yugoslav Navy"}
        ],
    }),

]


if __name__ == "__main__":
    print(f"Batch 47 \u2014 {len(ENTITIES)} entities (Class 392: Famous Navies)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
