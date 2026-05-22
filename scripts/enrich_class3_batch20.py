#!/usr/bin/env python3
"""
Batch 20 — 8 entities (Class 343): Famous World Temples
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/343-Class-343"
FILE_PREFIX = "343"


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

    ("a-ma-temple", {
        "summary": (
            "A-Ma Temple (媽閣廟, Mazu Temple, est. c.1488 CE) in Macau, China, is the oldest surviving temple in Macau and the source of the city's name — Portuguese sailors arriving c.1557 asked locals the name of the place, who replied 'A-Ma Gau' (Bay of A-Ma, referring to the Mazu goddess) which became Macau. Dedicated to Mazu (A-Ma), the Chinese goddess of seafarers and the sea, it was the spiritual centre of the fishing and trading community of the peninsula long before the Portuguese established their colonial presence.\n\n"
            "The temple complex — built into the base of Barra Hill above the waterfront — contains four main halls (prayer hall, Buddhist hall, Guanyin Pavilion, Zhenghao Temple) spanning different religious traditions: Taoism, Buddhism, and folk religion coexist within its precinct, reflecting the syncretic nature of Chinese popular religion. The complex's organic layout — built around and between the boulders of the hillside — makes it one of the most naturally sited religious complexes in East Asia.\n\n"
            "A-Ma Temple's international significance was confirmed when it was included as part of the Historic Centre of Macau — inscribed as a UNESCO World Heritage Site in 2005. The temple remains an active place of worship, with the annual Mazu Festival (Festa da Deusa A-Má) drawing hundreds of thousands of worshippers and transforming the temple precinct into a smoke-filled celebration of fire, incense, and sea-goddess devotion. The temple embodies the unique Macanese synthesis of Chinese and Portuguese colonial history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest surviving temple in Macau (est. c.1488 CE); source of the name 'Macau' (from 'A-Ma Gau'); dedicated to Mazu — Chinese goddess of seafarers; UNESCO World Heritage (2005) as part of Historic Centre of Macau; embodies Sino-Portuguese colonial history; annual Mazu Festival draws hundreds of thousands of pilgrims.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The importance of Mazu (A-Ma) as the patron goddess of seafarers to the fishing and trading communities of southern China's coast meant that a temple dedicated to her at the sheltered bay of Macau was both religiously necessary and practically important for the maritime trade routes",
            "The establishment of the Portuguese trading post at Macau (c.1557) — at a location already associated with the A-Ma Temple — created the historical coincidence of Portuguese colonial presence and Chinese sacred landscape that gave Macau its distinctive hybrid identity",
            "The syncretic tradition of Chinese popular religion — where Taoist, Buddhist, and folk deities coexist in the same sacred complex — shaped the organic growth of the temple over five centuries to encompass multiple religious traditions and architectural styles"
        ],
        "effects": [
            "The name 'Macau' itself derives from the A-Ma Temple — Portuguese sailors' misunderstanding of the locals' description of the bay as 'A-Ma Gau' — making it the rare example of a temple name that became a nation's capital city name",
            "A-Ma Temple's inclusion in the UNESCO World Heritage Site designation for the Historic Centre of Macau (2005) anchors the temple as the historical and spiritual origin point of the entire Macanese heritage landscape",
            "The annual Mazu Festival at the temple — one of the largest religious festivals in Macau — has maintained the continuity of Chinese popular religious practice through the entire Portuguese colonial period (1557–1999) and into the SAR era, demonstrating the resilience of pre-colonial religious traditions",
            "The temple's syncretic design — Taoism, Buddhism, and folk religion coexisting in a hillside complex — became a model for the Chinese religious syncretism that characterises popular religion throughout South China and the Chinese diaspora worldwide"
        ],
        "relationships": [
            {"entity": "Mazu (A-Ma)", "relationship": "DEDICATED_TO", "note": "A-Ma Temple is dedicated to Mazu — the Chinese goddess of seafarers — the paramount deity of Chinese maritime culture"},
            {"entity": "Name of Macau", "relationship": "SOURCE_OF", "note": "The Portuguese misinterpretation of 'A-Ma Gau' (Bay of A-Ma) gave Macau its name — a temple that named a nation's capital"},
            {"entity": "Historic Centre of Macau (UNESCO)", "relationship": "PART_OF", "note": "A-Ma Temple is included in the UNESCO World Heritage designation for the Historic Centre of Macau (2005)"},
            {"entity": "Portuguese colonial Macau (1557–1999)", "relationship": "SPIRITUAL_COUNTERPOINT_TO", "note": "The temple's continuous Chinese religious life through the entire Portuguese colonial period embodies Macau's unique Sino-Portuguese hybrid identity"},
            {"entity": "Chinese maritime trade (South China Sea)", "relationship": "SPIRITUAL_CENTRE_OF", "note": "As a Mazu temple, it was the religious focus of the fishing and trading communities of Macau's peninsula"}
        ],
    }),

    ("ananda-temple", {
        "summary": (
            "Ananda Temple (ဘုရားတော်ကြီး အာနန္ဒာ, est. c.1105 CE) in Bagan, Myanmar, is the finest, best-preserved, and most revered temple of the ancient Pagan Empire — considered the masterpiece of Mon architecture and a synthesis of Indian and native Burmese architectural traditions. Built by King Kyansittha, the Ananda is a perfect cross-shaped temple with four large gilded Buddha images facing the cardinal directions, each 9.5 metres high, housed in deep corridor recesses lit only by narrow skylights that create a dramatic chiaroscuro effect on the golden figures.\n\n"
            "The temple's architectural synthesis is extraordinary: its tiered pyramidal superstructure draws from Indian Buddhist temple forms (following the cosmic mountain Meru), while its square plan with four porticoes, whitewashed exterior, and interior vaulted corridors reflect Burmese and Mon architectural innovation. The four standing Buddhas — Kakusandha, Koṇāgamana, Kassapa, and Gautama — represent the four most recent Buddhas of the current world cycle, making the Ananda a temple of cosmic completeness.\n\n"
            "The Ananda Temple survived the 1975 Bagan earthquake that damaged many of the city's 3,000+ temples, and its restoration (completed in 1990) returned the gilded spire and whitewashed exterior to their original splendour. Annual Ananda Temple Festival (December/January, during the full moon of Pyatho) draws tens of thousands of worshippers who offer robes to monks and circumambulate the temple in the traditional Buddhist act of reverence."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Masterpiece of Mon architecture (est. c.1105 CE); best-preserved temple of the Pagan Empire; four 9.5m gilded Buddhas of four cardinal directions; synthesis of Indian cosmic mountain form with Burmese/Mon architecture; survived 1975 earthquake; annual Pyatho festival draws tens of thousands; one of Southeast Asia's supreme Buddhist monuments.",
            "significanceCategory": "continental"
        },
        "causes": [
            "King Kyansittha's patronage (c.1105 CE) — driven by his desire to build a temple of cosmic completeness representing all four Buddhas of the current world cycle — created the architectural brief that produced the Ananda's unique four-directional design",
            "The Pagan Empire's encounter with Indian Buddhist architectural traditions — transmitted through Mon monks and craftsmen who had direct knowledge of Indian temple forms — provided the technical and iconographic models that Burmese architects synthesised with local traditions",
            "The Pagan Empire's royal competition in Buddhist temple patronage — each king building more impressive temples than the last — drove the architectural ambition that produced the Ananda as the crowning achievement of Pagan-era temple architecture"
        ],
        "effects": [
            "The Ananda Temple's four-directional Buddha chambers — each creating a dramatically lit encounter with a 9.5-metre golden figure — established the experiential model for Burmese Buddhist temple design that influenced sacred architecture across Myanmar for centuries",
            "The temple's preservation through the collapse of the Pagan Empire (13th century), the Mongol invasion (1287), and the 1975 earthquake makes it the primary physical record of Pagan-era Mon-Burmese Buddhist architectural synthesis",
            "The Ananda Temple Festival (annual Pyatho full moon) has maintained continuous ritual engagement with the temple for nearly 900 years — one of the longest-running Buddhist festival traditions in Southeast Asia",
            "The temple's designation as part of the Bagan UNESCO World Heritage Site (2019) confirmed its status as one of Southeast Asia's most important cultural monuments, ensuring international resources for its preservation"
        ],
        "relationships": [
            {"entity": "King Kyansittha (Pagan Empire)", "relationship": "BUILT_BY", "note": "King Kyansittha commissioned the Ananda Temple (c.1105 CE) as the crowning achievement of Pagan royal Buddhist patronage"},
            {"entity": "Four Buddhas of the current world cycle", "relationship": "HOUSES_IMAGES_OF", "note": "Four 9.5m gilded Buddhas facing the cardinal directions — Kakusandha, Koṇāgamana, Kassapa, Gautama — making the temple cosmically complete"},
            {"entity": "Mon architectural tradition (Southeast Asia)", "relationship": "MASTERPIECE_OF", "note": "The Ananda is considered the masterpiece of Mon architecture — the supreme synthesis of Indian and Burmese building traditions"},
            {"entity": "Bagan Archaeological Zone (UNESCO)", "relationship": "FINEST_TEMPLE_WITHIN", "note": "The Ananda is the finest and best-preserved temple among 3,000+ surviving structures in the Bagan UNESCO World Heritage Zone (2019)"},
            {"entity": "Ananda Temple Festival (Pyatho)", "relationship": "FOCUS_OF", "note": "The annual Pyatho festival at Ananda draws tens of thousands — one of the longest-running Buddhist festival traditions in Southeast Asia"}
        ],
    }),

    ("shwedagon-pagoda", {
        "summary": (
            "Shwedagon Pagoda (ရွှေတိဂုံဘုရားတော်, The Golden Pagoda, legend: est. 2,500+ years ago; confirmed pre-14th century) in Yangon, Myanmar, is the most sacred Buddhist site in Myanmar — a 98-metre gilded stupa (the 60th-tallest structure in Myanmar) whose golden dome, visible from across Yangon, has been continuously maintained in gold by Burmese kings and ordinary devotees for at least 600 years. The stupa's solid gold tip is set with 4,531 diamonds, 2,317 rubies, 1,065 gold bells, and a 76-carat diamond at the very apex.\n\n"
            "The Shwedagon's legendary history claims it enshrines eight strands of the historical Buddha's hair, presented to two merchant brothers (Taphussa and Bhallika) who are said to have been the first lay followers of the Buddha after his enlightenment. While this legendary founding date is mythological, archaeological evidence confirms the pagoda was constructed during the Bagan period (11th–13th centuries CE) and expanded by successive Burmese kings. Queen Shinsawbu (15th century) is credited with surrounding the stupa with the current terrace and donating her own weight in gold to the pagoda.\n\n"
            "The Shwedagon Pagoda is deeply embedded in Burmese political history: it was the site of Aung San Suu Kyi's first public speech (1988), the 1988 pro-democracy uprising, and the 2007 Saffron Revolution. During the colonial period, British troops twice violated the sacred precinct (1824, 1852) — an act that galvanised Burmese nationalist sentiment and made the pagoda a symbol of both religious and political resistance."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most sacred Buddhist site in Myanmar; 98m gilded stupa with 4,531 diamonds, 76-carat apex diamond; legendary enshrining of 8 Buddha hair relics; gold donations maintained for 600+ years; site of 1988 pro-democracy uprising and Aung San Suu Kyi's first speech; symbol of Burmese religious and nationalist resistance; confirmed construction pre-14th century.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The legendary gift of eight Buddha hair relics to the pagoda — embedded in the founding mythology of Burmese Buddhism — gave the Shwedagon its status as the most sacred site in Myanmar, attracting royal patronage and popular devotion for centuries",
            "Queen Shinsawbu's (15th century) expansion of the pagoda terrace and her donation of her weight in gold established the royal tradition of gold donation that has maintained the Shwedagon's gilded surface continuously for over 600 years",
            "The British colonial violations of the pagoda precinct (1824, 1852) — seizing it as a military garrison — created a profound wound in Burmese religious and cultural identity that was channelled into anti-colonial nationalism"
        ],
        "effects": [
            "The Shwedagon's continuous gold maintenance — by kings donating their weight in gold, and by ordinary devotees applying gold leaf — is the most sustained act of collective religious devotion to a single monument in human history, creating a golden surface that grows thicker with each generation's contributions",
            "The pagoda's role as the spiritual epicentre of Burmese Buddhist nationalism made it the natural site for the 1988 pro-democracy uprising and the 2007 Saffron Revolution — the most politically significant Buddhist temple in modern Asian political history",
            "Aung San Suu Kyi's first major public speech at the Shwedagon (26 August 1988) — calling for a multi-party democratic system — launched the most famous democratic movement in Southeast Asia and transformed the pagoda into a globally recognised symbol of peaceful resistance",
            "The British colonial violation of the Shwedagon (1824, 1852) became one of the most potent symbols of imperial disregard for Asian religious traditions, fuelling Burmese nationalist sentiment and contributing to the eventual independence movement"
        ],
        "relationships": [
            {"entity": "Burmese Buddhist tradition", "relationship": "HOLIEST_SITE_OF", "note": "The Shwedagon is the most sacred Buddhist site in Myanmar — the spiritual heart of Burmese religious identity"},
            {"entity": "Queen Shinsawbu (15th century)", "relationship": "EXPANDED_AND_GOLD-DONATED_BY", "note": "Queen Shinsawbu expanded the terrace and donated her weight in gold — establishing the royal tradition of gold donation"},
            {"entity": "Aung San Suu Kyi", "relationship": "SITE_OF_FIRST_MAJOR_SPEECH_BY", "note": "Aung San Suu Kyi's first public speech (26 August 1988) at the Shwedagon launched the Burmese democracy movement"},
            {"entity": "1988 Pro-Democracy Uprising (Myanmar)", "relationship": "SPIRITUAL_CENTRE_OF", "note": "The 1988 uprising centred on the Shwedagon — transforming it from a religious site into a global symbol of democratic aspiration"},
            {"entity": "British colonial Myanmar (1824–1948)", "relationship": "VIOLATED_BY", "note": "British troops occupied the Shwedagon (1824, 1852) — galvanising Burmese nationalist sentiment"}
        ],
    }),

    ("jokhang", {
        "summary": (
            "Jokhang Temple (གཙུག་ལག་ཁང་, The House of the Lord, est. 642 CE) in Lhasa, Tibet, is the most sacred Buddhist temple in Tibet — the spiritual heart of Tibetan Buddhism and the destination of the Barkhor Circuit, the most important pilgrimage route in Tibetan Buddhism, around which the entire old city of Lhasa has grown. Built by King Songtsen Gampo, the founding ruler of the Tibetan Empire, to enshrine the Jowo Rinpoche — a life-size statue of Shakyamuni Buddha at age 12, said to be created in the Buddha's own lifetime and brought to Tibet as the dowry of Princess Wencheng of Tang China — the Jokhang is the most venerated object of devotion in Tibetan Buddhism.\n\n"
            "The Jowo Rinpoche statue — considered the most sacred object in Tibet — survived the Cultural Revolution (when the Jokhang was converted into a pig farm and granary, 1959–1980), the destruction of thousands of other Tibetan religious artifacts, and multiple historical disasters. The statue's survival is considered miraculous by Tibetan Buddhists and is a central element of Tibetan cultural and religious identity.\n\n"
            "The Jokhang is the focal point of the Barkhor — the 800-metre circular street that surrounds the temple, the most important pilgrimage circuit in Tibetan Buddhism, walked clockwise by hundreds of thousands of pilgrims annually. The entire Jokhang area was designated a UNESCO World Heritage Site (as part of the Historic Ensemble of the Potala Palace) in 2000. The temple's golden roof and prayer wheels are the defining visual symbols of Tibetan sacred architecture."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most sacred Buddhist temple in Tibet (est. 642 CE); enshrines the Jowo Rinpoche — most venerated object in Tibetan Buddhism; built by Songtsen Gampo (founding ruler of Tibetan Empire); focus of the Barkhor — most important Tibetan pilgrimage circuit; survived Cultural Revolution; UNESCO World Heritage (2000); spiritual heart of Tibetan Buddhism.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "King Songtsen Gampo's decision to build the Jokhang (642 CE) as the primary shrine for the Jowo Rinpoche — the gift of Princess Wencheng of Tang China — established the temple as the symbolic union of Tibetan and Chinese Buddhism and the foundation of the Tibetan Buddhist state",
            "The arrival of the Jowo Rinpoche statue in Tibet — as part of the diplomatic marriage between Songtsen Gampo and Princess Wencheng — created the religious object of supreme veneration around which Tibetan Buddhist identity was organised for the next 1,380 years",
            "The Jokhang's position at the centre of Lhasa — with the Barkhor pilgrimage circuit growing around it — made it the nucleus of Tibetan urban development, with the entire old city of Lhasa organised around the temple's sacred geography"
        ],
        "effects": [
            "The Barkhor Circuit — the 800-metre pilgrimage street encircling the Jokhang — has structured Lhasa's urban geography for 1,380 years, creating the most sacred street in Tibetan Buddhism and the commercial and cultural hub of the Tibetan capital",
            "The Jowo Rinpoche's survival through the Cultural Revolution (when the Jokhang was converted to a pig farm) became the most powerful symbol of Tibetan cultural and religious resilience — and of the Tibetan Buddhists' conviction that their holiest traditions would outlast political suppression",
            "The Jokhang's role as the destination of the Barkhor pilgrimage — walked annually by hundreds of thousands of Tibetan pilgrims, including those performing the three-step-one-prostration circuit — has maintained continuous ritual engagement with the temple across 13 centuries",
            "The Jokhang's designation as a UNESCO World Heritage Site (2000) — as part of the Potala Palace ensemble — gave the temple international protection status, creating a layer of global heritage governance over one of Asia's most politically sensitive religious sites"
        ],
        "relationships": [
            {"entity": "Jowo Rinpoche (statue of Shakyamuni at age 12)", "relationship": "ENSHRINES_THE_MOST_VENERATED_OBJECT_IN", "note": "The Jowo Rinpoche — said to be created in the Buddha's lifetime — is the most sacred object in Tibetan Buddhism, housed in the Jokhang since 642 CE"},
            {"entity": "King Songtsen Gampo (Tibetan Empire)", "relationship": "FOUNDED_BY", "note": "Songtsen Gampo built the Jokhang (642 CE) as the shrine for the Jowo Rinpoche, establishing it as the spiritual centre of the Tibetan Empire"},
            {"entity": "Princess Wencheng (Tang China)", "relationship": "JOWO_STATUE_BROUGHT_TO_TIBET_BY", "note": "The Jowo Rinpoche was the dowry of Princess Wencheng — the symbolic union of Tibetan and Chinese Buddhism"},
            {"entity": "Barkhor pilgrimage circuit (Lhasa)", "relationship": "FOCAL_POINT_OF", "note": "The 800-metre Barkhor Circuit — the most important Tibetan pilgrimage route — has structured Lhasa's urban geography for 1,380 years around the Jokhang"},
            {"entity": "UNESCO World Heritage (Potala Palace ensemble)", "relationship": "INSCRIBED_AS_PART_OF", "note": "The Jokhang is included in the UNESCO World Heritage designation for the Historic Ensemble of the Potala Palace (2000)"}
        ],
    }),

    ("fushimi-inari-taisha", {
        "summary": (
            "Fushimi Inari Taisha (伏見稲荷大社, est. 711 CE) in Kyoto, Japan, is the head shrine (honsha) of approximately 32,000 Inari shrines across Japan — the most numerous type of Shinto shrine in the country — dedicated to Inari Ōkami, the Shinto deity of rice, foxes, fertility, and industry. The shrine is renowned for its thousands of vermilion torii gates (senbon torii, 'thousands of torii'), which form a continuous tunnel along the mountain paths behind the shrine, creating the most photographed sacred path in Japan and one of the most recognised images of Japanese culture worldwide.\n\n"
            "The Inari cult — centred on Fushimi — was adopted by the merchant class of Edo-period Japan (17th–19th centuries) as the patron deity of commercial success, leading to the tradition of wealthy merchants and corporations donating torii gates inscribed with their business names. The result is a sacred mountain covered with over 10,000 torii gates donated across centuries, creating a tunnel of vermilion wood that winds for 4 kilometres through the forested hillside.\n\n"
            "Fushimi Inari receives approximately 3 million visitors at New Year alone (the highest visitation of any Shinto shrine in Japan), and is consistently ranked as Japan's most-visited tourist attraction by foreign visitors. The shrine complex includes the main hall (honden), the inner shrine (okusha), and the thousands of miniature torii and stone fox guardians (kitsune) donated by worshippers that crowd the paths to the summit of Mount Inari (233 metres)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Head shrine of 32,000 Inari shrines across Japan (est. 711 CE); dedicated to Inari — Shinto deity of rice, foxes, fertility and industry; 10,000+ vermilion torii gates donated across centuries; 3 million New Year visitors — highest of any Japanese shrine; most-visited tourist attraction in Japan by foreign visitors; patron of Japan's merchant class since Edo period.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The ancient Inari cult — predating the shrine's formal establishment in 711 CE — already associated the hill of Fushimi with Inari, the deity of rice and agricultural abundance, making it the natural location for the head shrine of the Inari tradition",
            "The adoption of the Inari cult by Edo-period (17th–19th century) merchants as the patron deity of commercial success transformed the shrine from an agricultural deity's residence into the patron of Japan's urban merchant class, vastly expanding its social base",
            "The tradition of donating torii gates as offerings — inscribed with the donor's business name as a commercial vow — created the unique visual landscape of thousands of continuous vermilion gates that makes Fushimi Inari the most photographed shrine in Japan"
        ],
        "effects": [
            "The network of 32,000 Inari shrines across Japan — all acknowledging Fushimi Inari as the head shrine — creates the most distributed sacred network of any single Shinto deity, embedding Inari worship in virtually every Japanese community from Hokkaido to Okinawa",
            "The 10,000+ torii gates at Fushimi Inari — donated across centuries by merchants and corporations — create the most dramatic example of cumulative religious patronage in Japanese culture, transforming the mountain into a living monument of commercial devotion",
            "The shrine's position at the top of Japan's most-visited tourist attraction rankings has made Fushimi Inari the international symbol of Japanese Shinto aesthetics — vermilion torii over forested paths are among the most widely reproduced images of Japanese culture globally",
            "The Inari fox tradition — stone kitsune guardians donated by thousands of worshippers — has made the fox (kitsune) the most widely represented supernatural guardian figure in Japanese folk religion, appearing in art, literature, and anime as the defining Japanese spirit"
        ],
        "relationships": [
            {"entity": "Inari Ōkami (Shinto deity)", "relationship": "HEAD_SHRINE_DEDICATED_TO", "note": "Fushimi Inari is the head shrine of Inari — the most widely worshipped Shinto deity, patron of rice, foxes, fertility, and industry"},
            {"entity": "32,000 Inari shrines across Japan", "relationship": "HONSHA_OF", "note": "Fushimi Inari is the head shrine (honsha) acknowledging approximately 32,000 Inari shrines across Japan — the most numerous shrine type"},
            {"entity": "Senbon torii (thousands of vermilion gates)", "relationship": "CONTAINS_THE_MOST_CELEBRATED_EXAMPLE_OF", "note": "The 10,000+ torii gates forming a 4km tunnel of vermilion are the most photographed sacred path in Japan"},
            {"entity": "Edo-period Japanese merchant class", "relationship": "PATRON_SHRINE_OF", "note": "Merchants adopted Inari as patron of commercial success in the Edo period — transforming the agricultural deity's shrine into a commercial patronage network"},
            {"entity": "Japanese Shinto tradition", "relationship": "MOST_VISITED_SHRINE_IN", "note": "3 million New Year visitors — the highest of any Japanese shrine — make Fushimi Inari the most visited Shinto shrine in Japan"}
        ],
    }),

    ("kinkaku-ji-temple", {
        "summary": (
            "Kinkaku-ji (金閣寺, Temple of the Golden Pavilion, original est. 1397 CE; rebuilt 1955) in Kyoto, Japan, is the most famous Buddhist temple in Japan and one of the most internationally recognised Japanese buildings — a three-storey pavilion whose upper two floors are entirely covered in gold leaf, reflected in the Mirror Pond below. Originally built as the retirement villa of Shogun Ashikaga Yoshimitsu (1358–1408), it was converted into a Buddhist temple (Rokuon-ji) after his death per his wishes.\n\n"
            "The Golden Pavilion's three storeys each represent a different architectural style: the ground floor uses the Shinden style of the aristocratic Heian court; the second floor uses the Bukke-zukuri (samurai residential) style; the third floor uses Karayo (Chinese Zen) style — making it a unique synthesis of court, samurai, and Buddhist architectural traditions in a single building. The tension between worldly splendour (gold-covered walls) and Buddhist spiritual aspiration (Zen monastery) is at the heart of the building's meaning.\n\n"
            "The original pavilion was burned to the ground in 1950 by a deranged young monk, Hayashi Yoken, who was obsessed with its beauty — an act made famous by Yukio Mishima's novel 'The Temple of the Golden Pavilion' (1956). The rebuilt pavilion (1955) is covered in five times more gold leaf than the original. Kinkaku-ji is a UNESCO World Heritage Site (1994) as part of the Historic Monuments of Ancient Kyoto."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most famous Buddhist temple in Japan (original est. 1397 CE); Shogun Ashikaga Yoshimitsu's retirement villa converted to Zen temple; gold leaf covers upper two floors; three storeys = three architectural traditions (Heian court, samurai, Chinese Zen); burned by monk in 1950, rebuilt 1955 with 5× more gold leaf; UNESCO World Heritage (1994); subject of Yukio Mishima's novel.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Shogun Ashikaga Yoshimitsu's desire to build the most splendid retirement villa ever seen — at a time when the Muromachi Shogunate was at the peak of its cultural and political power — drove the construction of the Golden Pavilion as a statement of shogunal magnificence",
            "The Zen Buddhist tradition of converting powerful men's residences into temple monasteries after their deaths — creating a spiritual legacy from worldly wealth — led to the conversion of the pavilion into Rokuon-ji temple following Yoshimitsu's death (1408)",
            "The deliberate synthesis of three architectural styles in the pavilion's three floors — Heian court, samurai residential, and Chinese Zen — expressed the Muromachi Shogunate's ambition to unite the cultural traditions of the aristocracy, the warrior class, and Chinese Buddhist learning"
        ],
        "effects": [
            "Kinkaku-ji's gold leaf reflection in the Mirror Pond created the defining image of Muromachi-era Japanese aesthetic ideals — the union of worldly magnificence and Buddhist spiritual aspiration — that influenced Japanese art and architecture for centuries",
            "Yukio Mishima's novel 'The Temple of the Golden Pavilion' (1956) — inspired by the 1950 arson — made the building a symbol of the Japanese postwar psyche's obsession with beauty, destruction, and the tension between tradition and modernity",
            "The rebuilt pavilion (1955) — covered in five times more gold leaf than the original — is one of the most visited tourist attractions in Japan, making it the primary international symbol of Japanese Buddhist heritage",
            "The 1950 arson by Hayashi Yoken — a monk who burned the national treasure he loved — became a defining parable of destructive obsession in Japanese culture, entering literature, philosophy, and cultural commentary as a metaphor for the danger of perfectionism"
        ],
        "relationships": [
            {"entity": "Shogun Ashikaga Yoshimitsu", "relationship": "ORIGINALLY_BUILT_AS_RETIREMENT_VILLA_OF", "note": "Yoshimitsu built the Golden Pavilion as his retirement villa (1397); converted to Rokuon-ji Buddhist temple after his death (1408)"},
            {"entity": "Rokuon-ji (Zen temple)", "relationship": "PART_OF", "note": "The Golden Pavilion is the sub-temple of Rokuon-ji — the Rinzai Zen temple that manages the entire complex"},
            {"entity": "Yukio Mishima (The Temple of the Golden Pavilion)", "relationship": "SUBJECT_OF_NOVEL_BY", "note": "Mishima's 1956 novel was inspired by the 1950 arson — making the temple a symbol of beauty, obsession, and destruction"},
            {"entity": "1950 arson (Hayashi Yoken)", "relationship": "DESTROYED_AND_REBUILT_AFTER", "note": "The original pavilion was burned in 1950 by a monk; rebuilt in 1955 with five times more gold leaf"},
            {"entity": "UNESCO World Heritage (Historic Monuments of Ancient Kyoto)", "relationship": "INSCRIBED_AS_PART_OF", "note": "Kinkaku-ji is included in the UNESCO World Heritage designation for the Historic Monuments of Ancient Kyoto (1994)"}
        ],
    }),

    ("meiji-jingū", {
        "summary": (
            "Meiji Jingū (明治神宮, Meiji Shrine, est. 1920 CE) in Tokyo, Japan, is the most visited Shinto shrine in Japan — receiving over 3 million visitors in the first three days of each New Year alone, the highest visitation of any shrine in the country — and the most important shrine of the modern imperial era, dedicated to the deified spirits of Emperor Meiji (1852–1912) and Empress Shōken. Set within a 70-hectare forested sanctuary in central Tokyo (containing 120,000 trees donated from across Japan), the shrine is an island of ancient Shinto ritual space in the heart of the world's largest city.\n\n"
            "Emperor Meiji's reign (1868–1912) transformed Japan from a feudal shogunate to a modern constitutional monarchy capable of defeating both China (1895) and Russia (1905) — making him the most transformative Japanese ruler since the introduction of Buddhism and Chinese culture in the 6th century. His deification at Meiji Jingū (1920) — eight years after his death — reflects the Meiji government's strategy of using Shinto ritual to legitimise the new imperial order and create a modern Japanese national identity.",
            "\n\nThe shrine's modern establishment (1920) and complete destruction in World War II (1945) followed by immediate rebuilding (1958) mirrors Japan's modern history: creation of a modern national identity, catastrophic defeat, and determined reconstruction. The 120,000 trees donated from across Japan and the overseas territories make the forest a living symbol of the pre-war Japanese Empire's geographic extent."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most visited Shinto shrine in Japan (est. 1920 CE); 3 million New Year visitors in first 3 days; dedicated to deified Emperor Meiji — Japan's most transformative modern ruler; 70-hectare forested sanctuary in central Tokyo; 120,000 donated trees from across Japan; destroyed 1945, rebuilt 1958; mirrors Japan's modern history of transformation, defeat, and reconstruction.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Emperor Meiji's extraordinary reign (1868–1912) — transforming Japan from feudal shogunate to constitutional monarchy and imperial power capable of defeating both China and Russia — created a ruler of such historical significance that his deification was judged necessary by the Meiji government's successors",
            "The Meiji government's State Shinto programme — systematically using Shinto ritual, shrine networks, and imperial deification to create a modern Japanese national identity — drove the construction of Meiji Jingū as the supreme expression of imperial Shinto reverence",
            "The donation of 120,000 trees from across Japan and overseas territories — creating the shrine's forested precinct — was a national act of collective participation that made the shrine a physical symbol of the Japanese Empire's geographic extent at its peak"
        ],
        "effects": [
            "Meiji Jingū's 3 million New Year visitors (in three days) make it the focal point of Japan's most important annual ritual — hatsumode (first shrine visit of the New Year) — concentrating the national ritual of the world's third-largest economy at a single Shinto sacred site",
            "The shrine's 70-hectare forest — an island of ancient woodland in the centre of Tokyo — has become a model for urban green space design, demonstrating the capacity of religious land preservation to create ecologically significant habitats within megacities",
            "The shrine's rebuilding after its 1945 destruction — completed in 1958 as part of Japan's postwar reconstruction — symbolised the continuity of Japanese Shinto tradition through defeat and represented the nation's determination to reclaim its cultural heritage",
            "Emperor Meiji's deification at the shrine established the model for 20th-century Japanese state-religion relationships that would eventually be constitutionally separated (1947) — making Meiji Jingū a site where the tensions of modern Japanese identity between imperial tradition and democratic modernity are permanently embodied"
        ],
        "relationships": [
            {"entity": "Emperor Meiji (1852–1912)", "relationship": "DEDICATED_TO_DEIFIED_SPIRIT_OF", "note": "Meiji Jingū is dedicated to the deified spirits of Emperor Meiji and Empress Shōken — the most transformative modern Japanese ruler"},
            {"entity": "Meiji Restoration (1868)", "relationship": "SHRINE_HONOURING_THE_ARCHITECT_OF", "note": "Emperor Meiji's reign (1868–1912) transformed Japan from shogunate to modern constitutional monarchy — the Meiji Restoration's supreme achievement"},
            {"entity": "Japanese State Shinto (Meiji–1945)", "relationship": "SUPREME_EXPRESSION_OF", "note": "Meiji Jingū embodies the Meiji government's strategy of using Shinto shrine networks and imperial deification to create modern Japanese national identity"},
            {"entity": "Hatsumode (New Year shrine visit)", "relationship": "PRIMARY_DESTINATION_OF", "note": "3 million visitors in the first three days of each New Year — the most concentrated Hatsumode pilgrimage in Japan"},
            {"entity": "Urban forest conservation (Tokyo)", "relationship": "PIONEERING_EXAMPLE_OF", "note": "The 70-hectare forested precinct in central Tokyo is a landmark example of religious land preservation creating significant urban ecological habitat"}
        ],
    }),

    ("asuka-dera-temple", {
        "summary": (
            "Asuka-dera Temple (飛鳥寺, officially Hōkō-ji, est. 593 CE) in Asuka, Nara Prefecture, Japan, is the first permanent Buddhist temple in Japan — built by Soga no Umako, the most powerful minister of the Asuka period, following the official introduction of Buddhism to Japan (538 or 552 CE). The temple marks the beginning of Japanese Buddhist architectural history and the start of the Japanese temple-building tradition that would produce over 75,000 Buddhist temples across Japan over the following 1,400 years.\n\n"
            "The original Asuka-dera was constructed by craftsmen sent from Baekje (Korean kingdom) — the first transmission of Korean architectural technology to Japan — and its layout (a central pagoda surrounded by three golden halls) established the floor plan that would influence Japanese temple architecture for centuries. The temple housed the Asuka Daibutsu — the oldest surviving large-scale bronze Buddha in Japan (606 CE), cast by the craftsman Kuratsukuri no Tori and still in situ at the temple site.\n\n"
            "The Asuka period (593–710 CE) — named after the political centre near Asuka-dera — produced the first Japanese legal codes (Taihō Code), the first constitution (Prince Shōtoku's Seventeen-Article Constitution), and the first systematic engagement with Chinese and Korean learning. Asuka-dera stands at the centre of this transformative period, as both its physical monument and the institutional base from which the Soga clan exercised its power at the Japanese court."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "First permanent Buddhist temple in Japan (est. 593 CE); built by Soga no Umako following official introduction of Buddhism; first transmission of Korean architectural technology to Japan; houses Asuka Daibutsu — oldest surviving large-scale bronze Buddha in Japan (606 CE); origin of Japan's 75,000-temple Buddhist tradition; centre of the transformative Asuka period.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The official introduction of Buddhism to Japan (538 or 552 CE) — from the Korean kingdom of Baekje — created both the religious impetus and the political occasion for building Japan's first permanent Buddhist temple",
            "Soga no Umako's political investment in Buddhism — using the new religion as a tool against rivals who supported the traditional Shinto deities — drove the construction of Asuka-dera as the physical symbol of the Buddhist faction's victory at the Japanese court",
            "The dispatch of craftsmen from Baekje (Korea) to Japan for the temple's construction — the first transfer of Korean architectural technology to Japan — provided the technical knowledge needed to build the first permanent stone-founded, tile-roofed religious building in the Japanese archipelago"
        ],
        "effects": [
            "Asuka-dera's construction initiated the Japanese temple-building tradition that would produce over 75,000 Buddhist temples across Japan over 1,400 years — the most extensive national Buddhist institutional network in the world",
            "The Asuka Daibutsu (606 CE) — the oldest surviving large-scale bronze Buddha in Japan — established the iconographic and technical tradition of Japanese Buddhist sculpture, directly influencing the Nara Daibutsu (752 CE) and the subsequent tradition of monumental Japanese Buddhist image-making",
            "The transmission of Korean architectural technology through Asuka-dera's construction — tile roofing, stone foundations, cardinal-axis planning — transformed Japanese construction methods and created the architectural foundation for the subsequent Nara, Heian, and later Japanese building traditions",
            "The Asuka period's Buddhist legal and intellectual culture — centred around the Asuka-dera and the Soga clan's patronage — produced Japan's first constitution, first legal codes, and first systematic engagement with Chinese learning, shaping Japanese civilisation's foundational institutions"
        ],
        "relationships": [
            {"entity": "Soga no Umako", "relationship": "BUILT_BY_THE_PATRONAGE_OF", "note": "Soga no Umako built Asuka-dera (593 CE) as the physical symbol of the Buddhist faction's political victory at the Japanese court"},
            {"entity": "Japanese Buddhist temple tradition", "relationship": "FOUNDING_MONUMENT_OF", "note": "Asuka-dera is the first permanent Buddhist temple in Japan — the origin of the tradition that would produce 75,000+ temples"},
            {"entity": "Asuka Daibutsu (606 CE)", "relationship": "HOUSES_THE_OLDEST_SURVIVING_LARGE-SCALE_BRONZE_BUDDHA_IN", "note": "The Asuka Daibutsu — cast by Kuratsukuri no Tori in 606 CE — is the oldest surviving large-scale bronze Buddha in Japan"},
            {"entity": "Baekje (Korean kingdom)", "relationship": "CRAFTSMEN_AND_TECHNOLOGY_RECEIVED_FROM", "note": "Baekje craftsmen built Asuka-dera — the first transmission of Korean architectural technology (tile roofing, stone foundations) to Japan"},
            {"entity": "Asuka period (593–710 CE)", "relationship": "CENTRAL_INSTITUTION_OF", "note": "Asuka-dera stands at the centre of the transformative Asuka period — Japan's first legal codes, constitution, and systematic Chinese/Korean learning"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 20 — {len(ENTITIES)} entities (Class 343: Famous World Temples)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
