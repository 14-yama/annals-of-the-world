#!/usr/bin/env python3
"""
Batch 18 — 8 entities (Class 343): Temples and Sacred Sites
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/343-Class-343"
FILE_PREFIX = "343"
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

    ("ajanta-caves", {
        "summary": (
            "The Ajanta Caves (अजंता लेणी, est. 2nd century BCE – 5th century CE) in Maharashtra, India, are 30 rock-cut Buddhist cave monasteries and prayer halls containing the finest surviving examples of ancient Buddhist art — murals depicting the Jataka tales (stories of the Buddha's previous lives), devotional images, and scenes of contemporary Gupta-era life, executed between the 1st and 5th centuries CE by anonymous artists at the height of Indian artistic achievement. Rediscovered by British soldiers in 1819 (having been abandoned c.650 CE and forgotten under jungle for over 1,100 years), the Ajanta murals are among the most important surviving works of ancient world art.\n\n"
            "The Ajanta site divides into two phases: the Hinayana ('Lesser Vehicle') caves (Phase 1: c.100 BCE–100 CE) — simple chaitya-grihas (prayer halls) with plain facades — and the Mahayana ('Greater Vehicle') caves (Phase 2: c.400–480 CE) — elaborately carved viharas (monasteries) with sophisticated narrative murals. The Phase 2 murals, probably executed during the reign of the Vakataka dynasty (allies of the Gupta empire), are the primary artistic record of Mahayana Buddhist iconography and represent the apex of Gupta-era visual culture.\n\n"
            "The painted ceilings, walls, and pillars of the Ajanta caves — depicting court scenes, devotional figures, and Jataka narratives in a sophisticated palette of mineral pigments — influenced Buddhist art traditions from Central Asia to China to Japan. The UNESCO World Heritage Site (1983) draws 300,000+ annual visitors and remains the single most important evidence for the lost tradition of ancient Indian monumental painting."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Finest surviving ancient Buddhist art (est. 2nd century BCE–5th century CE); 30 rock-cut caves; forgotten for 1,100 years, rediscovered 1819; Jataka narrative murals — apex of Gupta-era Indian painting; influenced Buddhist art from Central Asia to Japan; UNESCO World Heritage (1983); the single most important evidence for ancient Indian monumental painting.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The patronage of Buddhist monasticism by the Satavahana dynasty (Phase 1) and the Vakataka dynasty (Phase 2) — who funded the excavation of caves and the painting of murals as acts of religious merit — created the sustained patronage that produced 30 caves of extraordinary quality over 600 years",
            "The Deccan plateau's hard basalt rock — ideal for rock-cut architecture, which requires no separate construction materials and maintains stable temperature and humidity — made the Ajanta gorge an ideal site for the creation of permanent cave monasteries",
            "The Buddhist tradition of rock-cut cave monasteries (inherited from earlier Indian Buddhist practice) and the development of Mahayana Buddhist iconography — with its rich visual programme of devotional images and narrative scenes — created both the institutional form and the artistic programme that Ajanta's craftsmen executed"
        ],
        "effects": [
            "The Ajanta murals' artistic techniques — foreshortening, three-dimensional modelling, psychological portraiture, complex multi-figure narrative composition — demonstrate that Gupta-era Indian painters had achieved an artistic sophistication equal to the greatest traditions of the ancient world, influencing subsequent Buddhist art traditions across Asia",
            "The Ajanta caves' influence on Buddhist art traditions in Central Asia, China, and Japan — transmitted along the Silk Road as Buddhist monks and pilgrims carried artistic models — made the Ajanta aesthetic the foundational vocabulary of Buddhist visual culture across Asia",
            "The 1,100-year abandonment and subsequent rediscovery (1819) preserved the murals in extraordinary condition while also generating the narrative of 'forgotten Indian civilisation' that became central to 19th-century Indian nationalist cultural identity",
            "The preservation challenges at Ajanta — the murals deteriorating after rediscovery due to exposure and inappropriate conservation attempts — made it a test case for the application of modern conservation science to ancient Indian cultural heritage"
        ],
        "relationships": [
            {"entity": "Gupta Empire / Vakataka dynasty", "relationship": "PATRONISED_BY", "note": "The Vakataka dynasty (Gupta allies) patronised the Phase 2 caves (c.400–480 CE) — the primary artistic record of Mahayana Buddhist iconography"},
            {"entity": "Buddhist art (Central Asia, China, Japan)", "relationship": "FOUNDATIONAL_INFLUENCE_ON", "note": "The Ajanta aesthetic — transmitted along the Silk Road — is the foundational vocabulary of Buddhist visual culture across Asia"},
            {"entity": "Jataka tales", "relationship": "PRIMARY_VISUAL_RECORD_OF", "note": "The Ajanta murals are the most important surviving visual record of the Jataka narrative tradition — stories of the Buddha's previous lives"},
            {"entity": "Gupta-era Indian painting", "relationship": "SOLE_MAJOR_SURVIVING_EVIDENCE_OF", "note": "The murals are the single most important evidence for the lost tradition of Gupta-era Indian monumental painting"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Ajanta Caves inscribed as UNESCO World Heritage Site (1983) — 300,000+ annual visitors"}
        ],
    }),

    ("borobudur-temple-compounds", {
        "summary": (
            "Borobudur (Barabudur, est. c.800 CE) on the island of Java, Indonesia, is the largest Buddhist temple in the world — a massive stone mandala rising nine platforms and 34.5 metres above the Kedu Plain, decorated with 2,672 relief panels (the world's most extensive narrative stone reliefs) and 504 Buddha statues, including 72 stupas containing Dhyani Buddha figures. Built during the Sailendra dynasty, Borobudur represents the most ambitious single architectural expression of Mahayana Buddhist cosmology ever constructed.\n\n"
            "Borobudur's design encodes the Buddhist universe in three-dimensional form: the lower levels (Kamadhatu) represent the world of desire, with reliefs depicting karmic consequences; the middle levels (Rupadhatu) represent the world of form, with narrative reliefs illustrating the Jataka tales and the Gandavyuha sutra; the upper circular terraces (Arupadhatu) represent the formless world, with open stupas containing meditating Buddha figures. A pilgrim walking the 5-kilometre circuit from the base to the summit re-enacts the Buddhist path from desire to enlightenment.\n\n"
            "Borobudur was abandoned c.930 CE (possibly after the eruption of Mount Merapi) and forgotten for 900 years — discovered by Raffles' expedition in 1814 — and required the most ambitious archaeological restoration in Southeast Asian history (UNESCO-funded, 1975–1982). A UNESCO World Heritage Site since 1991, it draws 3.5 million annual visitors and has become the symbol of Indonesian national and cultural identity, featured on the country's 20,000-rupiah banknote."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest Buddhist temple (est. c.800 CE); most ambitious architectural expression of Mahayana Buddhist cosmology; 2,672 relief panels — world's most extensive narrative stone reliefs; 504 Buddha statues; abandoned and forgotten for 900 years; UNESCO restoration (1975–1982); UNESCO World Heritage (1991); 3.5 million annual visitors; symbol of Indonesian identity.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Sailendra dynasty's Buddhist patronage — and the convergence of Indian Mahayana Buddhist theological sophistication with Javanese stone-carving traditions — created the unique conditions for Borobudur's construction, combining ambitious theological programme with exceptional craft skills",
            "The Kedu Plain's exceptional agricultural fertility — the richest rice-growing area in Java — generated the surplus wealth that sustained the massive construction project (estimated 1.6 million stone blocks, requiring 75 years of continuous effort) and the artisan class that executed it",
            "Mahayana Buddhist cosmological thought — particularly the concept of the mandala as a three-dimensional representation of the Buddhist universe — provided the architectural concept that gave Borobudur its unique form: not a temple in the conventional sense but a walk-through cosmological model"
        ],
        "effects": [
            "Borobudur's 2,672 relief panels — illustrating the Jataka tales, the Gandavyuha sutra, and scenes of Javanese court life — are the world's most extensive narrative stone relief programme, providing an irreplaceable visual record of 9th-century Javanese Buddhist culture, society, and cosmology",
            "The UNESCO restoration of Borobudur (1975–1982) — dismantling and reassembling 1.3 million stones while adding a concrete foundation and drainage system — is the most extensive archaeological restoration project in Southeast Asian history, establishing the methodological standard for large-scale architectural conservation",
            "Borobudur's rediscovery and restoration became a cornerstone of Indonesian national identity — the monument's image on the 20,000-rupiah note and its designation as UNESCO World Heritage (1991) positioned it as the primary symbol of Indonesian civilisational achievement",
            "The 2006 Yogyakarta earthquake and the 2010 Merapi eruption (which deposited ash on the monument) demonstrated Borobudur's extreme vulnerability to the natural hazards of its volcanic environment, making it the most threatened UNESCO World Heritage Site in Southeast Asia"
        ],
        "relationships": [
            {"entity": "Sailendra dynasty", "relationship": "BUILT_BY", "note": "The Sailendra dynasty built Borobudur (c.800 CE) as the supreme expression of their Buddhist patronage"},
            {"entity": "Mahayana Buddhist cosmology", "relationship": "THREE-DIMENSIONAL_ARCHITECTURAL_EXPRESSION_OF", "note": "Borobudur encodes the Buddhist universe in architectural form — Kamadhatu, Rupadhatu, and Arupadhatu as the three levels of existence"},
            {"entity": "UNESCO restoration (1975–1982)", "relationship": "MOST_EXTENSIVE_SOUTHEAST_ASIAN_RESTORATION_UNDERTAKEN_ON", "note": "UNESCO-funded restoration dismantled and reassembled 1.3 million stones — establishing the standard for large-scale architectural conservation"},
            {"entity": "Indonesian national identity", "relationship": "PRIMARY_SYMBOL_OF", "note": "Borobudur is the primary symbol of Indonesian civilisational achievement — featured on the 20,000-rupiah note"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Inscribed as UNESCO World Heritage Site (1991) — 3.5 million annual visitors"}
        ],
    }),

    ("temple-of-heaven", {
        "summary": (
            "The Temple of Heaven (天坛, Tiāntán, est. 1406–1420 CE) in Beijing is the most architecturally sophisticated ceremonial complex in Chinese imperial history — where the emperors of the Ming and Qing dynasties performed the annual Heaven Worship ceremony (Jiao sacrifices) to maintain the Mandate of Heaven (Tianming) and ensure good harvests. The complex's three primary structures — the circular Hall of Prayer for Good Harvests (Qinian Dian), the Imperial Vault of Heaven, and the Circular Mound Altar — embody the ancient Chinese cosmological distinction between Heaven (round, Yang) and Earth (square, Yin) in their geometric forms.\n\n"
            "The Hall of Prayer for Good Harvests — the triple-roofed circular pavilion whose image is synonymous with Chinese architecture globally — was built entirely without nails, using interlocking wooden components. Its triple blue-tiled roofs (blue representing Heaven) and the 28 massive columns supporting them create a structural and symbolic masterpiece. The entire complex is set within a 273-hectare park whose square outer wall (representing Earth) and circular inner wall (representing Heaven) embody the cosmological principles the complex exists to honour.\n\n"
            "The Temple of Heaven's annual ceremony — the most important ritual of the Chinese imperial calendar — was performed by the emperor alone (it was fatal for any commoner to witness it) as the intermediary between humanity and Heaven. The complex became a public park in 1918 and a UNESCO World Heritage Site in 1998. The Hall of Prayer for Good Harvests is the most reproduced image in Chinese architecture globally."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most architecturally sophisticated Chinese imperial ceremonial complex (est. 1406–1420 CE); site of the annual Heaven Worship ceremony maintaining the Mandate of Heaven; Hall of Prayer for Good Harvests — the most reproduced image in Chinese architecture; cosmological geometry (round Heaven, square Earth); UNESCO World Heritage (1998).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Yongle Emperor's construction of Beijing as the imperial capital (1406–1420) — moving the court from Nanjing — required a ceremonial complex adequate to the imperial claim to Tianming (Mandate of Heaven), motivating the construction of the Temple of Heaven as the primary ritual site",
            "The Chinese cosmological system's distinction between Heaven (round, Yang) and Earth (square, Yin) — fundamental to Chinese metaphysics, astronomy, and political philosophy — provided the geometric programme that determined every architectural decision in the complex",
            "The agricultural basis of the Chinese imperial economy — in which the emperor's ritual relationship with Heaven guaranteed the cosmic order that produced good harvests — created the political and theological imperative for the annual Jiao ceremony that the Temple of Heaven was built to host"
        ],
        "effects": [
            "The Temple of Heaven's ceremonial programme — in which the emperor's correct performance of the Heaven Worship ritual was understood to maintain cosmic order and agricultural abundance — defined the role of the Chinese emperor as cosmic mediator, a concept that shaped Chinese political philosophy for 500 years",
            "The Hall of Prayer for Good Harvests' architectural image — the triple blue-roofed circular pavilion — has become the most internationally recognised symbol of Chinese architecture globally, appearing on countless books, films, and representations of China",
            "The Temple of Heaven's conversion to a public park (1918) — after the fall of the Qing dynasty — democratised a space that had been the most exclusive ritual precinct in China (fatal for commoners to enter during ceremonies), symbolising the collapse of the imperial cosmological order",
            "The complex's architectural influence — the Hall's triple-roof design, the Circular Mound Altar's acoustic properties (a concentric echo effect), the cosmological geometry — shaped subsequent Chinese ceremonial architecture and is studied globally as the finest example of Chinese cosmological architecture"
        ],
        "relationships": [
            {"entity": "Yongle Emperor (Ming dynasty)", "relationship": "COMMISSIONED_BY", "note": "Yongle Emperor built the Temple of Heaven (1406–1420) as part of his construction of Beijing as the imperial capital"},
            {"entity": "Mandate of Heaven (Tianming)", "relationship": "PRIMARY_RITUAL_SITE_FOR_MAINTAINING", "note": "The Temple of Heaven's annual ceremony was the primary ritual maintaining the Mandate of Heaven — the cosmic basis of imperial authority"},
            {"entity": "Chinese cosmological system (round Heaven, square Earth)", "relationship": "ARCHITECTURAL_EXPRESSION_OF", "note": "The complex's geometry — round structures for Heaven, square walls for Earth — encodes the fundamental Chinese cosmological distinction"},
            {"entity": "Chinese imperial architecture", "relationship": "FINEST_CEREMONIAL_EXAMPLE_OF", "note": "The Temple of Heaven is the most architecturally sophisticated ceremonial complex in Chinese imperial history"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Inscribed as UNESCO World Heritage Site (1998) — Hall of Prayer is the most reproduced image in Chinese architecture globally"}
        ],
    }),

    ("mahabodhi-temple", {
        "summary": (
            "The Mahabodhi Temple (महाबोधि मन्दिर, est. original structure 3rd century BCE, current structure 5th–6th century CE) in Bodh Gaya, Bihar, India, marks the site where Siddhartha Gautama attained enlightenment (Bodhi) under the sacred Bodhi Tree approximately 2,500 years ago — making it the holiest site in Buddhism and one of the most sacred pilgrimage destinations in the world. The Bodhi Tree growing adjacent to the temple is a direct descendant of the original tree under which the Buddha sat.\n\n"
            "The current temple structure — a 52-metre pyramidal tower in the Gupta architectural style — is the oldest surviving brick building in the Indian subcontinent (5th–6th century CE) and the most influential temple in the history of Buddhist architecture: its tower form, decorated with small stupa images and rising in diminishing tiers to a large finial, became the template for Buddhist temple architecture across Southeast Asia, Sri Lanka, and Myanmar. The Shwedagon Pagoda in Yangon and thousands of other Buddhist structures derive their form from the Mahabodhi.\n\n"
            "Bodh Gaya's history reflects the broader history of Buddhism in India: abandoned after Islam's arrival in northern India (12th century), rediscovered and restored by the Burmese king Mindon Min (1870s), then contested between Hindu and Buddhist communities (the temple management was under Hindu control until 1953). A UNESCO World Heritage Site since 2002, it draws 3 million+ annual pilgrims from across the Buddhist world — the most important single destination in Buddhist pilgrimage."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Holiest site in Buddhism — where the Buddha attained enlightenment (c.500 BCE); oldest surviving brick building in the Indian subcontinent (5th–6th century CE); most influential Buddhist temple architecture — template for Southeast Asian, Sri Lankan, and Myanmar Buddhist temples; Bodhi Tree is direct descendant of the original; 3 million+ annual pilgrims; UNESCO World Heritage (2002).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Siddhartha Gautama's enlightenment under the Bodhi Tree at Bodh Gaya (c.500 BCE) — the founding event of Buddhism, from which all Buddhist practice and teaching derives — created the theological mandate for the site's permanent sacred status",
            "Emperor Ashoka's visit to Bodh Gaya (c.250 BCE) — his personal pilgrimage to the site of the Buddha's enlightenment — and his construction of the original shrine established the pattern of royal Buddhist patronage that produced the current temple structure",
            "The Gupta Empire's construction of the current pyramidal tower structure (5th–6th century CE) — adapting the Bodhi shrine into a permanent monumental temple in the developing North Indian Hindu-Buddhist architectural tradition — created the architectural form that became the template for Buddhist temple architecture across Asia"
        ],
        "effects": [
            "The Mahabodhi Temple's architectural form — the pyramidal tower with diminishing tiers and small stupa images on the exterior — became the template for Buddhist temple architecture across South and Southeast Asia: the Ananda Temple at Bagan (Myanmar), the Shwedagon Pagoda's spire type, and thousands of Sri Lankan and Thai Buddhist structures derive their forms from the Mahabodhi",
            "The presence of the Bodhi Tree — a direct descendant of the original tree under which the Buddha sat — makes Bodh Gaya's most important relic a living tree, unique among the world's holiest religious sites, and creates a continuous biological chain connecting modern Buddhism to the founding event",
            "The 19th-century restoration of Bodh Gaya — driven by Burmese, Sri Lankan, and Japanese Buddhist communities — catalysed the international Buddhist revival movement and created the model of pan-Asian Buddhist solidarity that has shaped global Buddhist institutional life since the late 19th century",
            "The post-independence transfer of the temple's management to a Buddhist-majority committee (1953) — ending decades of Hindu control — was a landmark event in the Indian religious freedom movement, with implications for the management of sacred sites across pluralistic societies"
        ],
        "relationships": [
            {"entity": "Siddhartha Gautama (the Buddha)", "relationship": "MARKS_ENLIGHTENMENT_SITE_OF", "note": "The Mahabodhi Temple marks the site of the Buddha's enlightenment (c.500 BCE) — the founding event of Buddhism"},
            {"entity": "Bodhi Tree", "relationship": "ADJACENT_TO_DIRECT_DESCENDANT_OF_ORIGINAL", "note": "The Bodhi Tree adjacent to the temple is a direct descendant of the original tree under which the Buddha attained enlightenment"},
            {"entity": "Buddhist temple architecture (Southeast Asia, Sri Lanka)", "relationship": "ARCHITECTURAL_TEMPLATE_FOR", "note": "The Mahabodhi's pyramidal tower became the template for Buddhist temple architecture across South and Southeast Asia"},
            {"entity": "Emperor Ashoka", "relationship": "ORIGINAL_SHRINE_ESTABLISHED_BY", "note": "Ashoka's pilgrimage (c.250 BCE) and construction of the original shrine established the pattern of royal Buddhist patronage at Bodh Gaya"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Inscribed as UNESCO World Heritage Site (2002) — 3 million+ annual pilgrims from the global Buddhist world"}
        ],
    }),

    ("temple-of-ephesian-artemis", {
        "summary": (
            "The Temple of Artemis at Ephesus (Ἀρτεμίσιον, Artemision, est. original c.550 BCE, destroyed and rebuilt c.323 BCE) in Ephesus (near modern Selçuk, Turkey) was one of the Seven Wonders of the Ancient World — the largest temple ever built in the ancient Greek world (137 × 69 metres, 127 columns at 18 metres high) — and served as the primary sanctuary of Artemis (Diana), the goddess of the hunt and patroness of Ephesus. The city's global significance in the ancient world derived directly from the temple's status as the most important sacred site in the Aegean world.\n\n"
            "The temple was destroyed and rebuilt multiple times: the first great temple (c.550 BCE) was funded by the Lydian king Croesus (whose name became proverbial for wealth); it was burned down in 356 BCE by Herostratus, who sought immortality through the act of destruction — the night of Alexander the Great's birth; the rebuilt temple (c.323 BCE) was even larger, became a Wonder of the Ancient World, and stood for nearly 700 years. It was sacked by the Goths in 268 CE and its stones were used to build the Byzantine Hagia Sophia and other buildings.\n\n"
            "The Temple of Artemis was simultaneously a religious sanctuary, a financial institution (acting as a treasury and bank for the ancient Mediterranean world), and a source of immense political power — those who controlled Ephesus controlled the temple, and those who controlled the temple controlled the most important financial and religious institution in the Aegean. Its destruction was truly permanent: today only a single reconstructed column marks the site."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of the Seven Wonders of the Ancient World (est. original c.550 BCE); largest temple in the ancient Greek world; funded by Croesus of Lydia; burned by Herostratus on the night of Alexander the Great's birth (356 BCE); 700-year standing as a Wonder; stones used to build Hagia Sophia; simultaneous religious sanctuary, bank, and political institution.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Lydian king Croesus's funding of the first great temple (c.550 BCE) — motivated by a desire to demonstrate Lydian wealth and piety after his conquest of the Greek cities of Ionia — created the financial basis for a temple whose scale exceeded all previous Greek religious architecture",
            "The burning of the temple by Herostratus (356 BCE) — seeking immortality through the destruction of something celebrated — created the occasion for the rebuilt temple to be even more magnificent, as the Ephesians declared that Artemis was 'too busy attending to the birth of Alexander to be concerned with the temple'",
            "Ephesus's position as one of the greatest commercial cities of the ancient Mediterranean — at the mouth of the Cayster River, where East-West trade routes converged — generated the wealth and the cosmopolitan religious tradition that made the temple a Wonder of the Ancient World"
        ],
        "effects": [
            "The Temple of Artemis served as a bank for the ancient Mediterranean world — accepting deposits from Greek cities, foreign kings, and private individuals — making it the most important financial institution of the Aegean world and giving Ephesus political leverage through financial control",
            "The temple's destruction by Herostratus (356 BCE) created one of antiquity's most famous acts of cultural vandalism and gave rise to the concept of 'damnatio memoriae' — the Ephesians declared it a crime to mention Herostratus's name (ensuring his permanent historical fame through the very prohibition)",
            "The temple's stones — reused in the construction of Byzantine buildings including Hagia Sophia — created a physical continuity between the ancient pagan sacred tradition and the Christian architectural tradition, embodying the material transmutation of classical antiquity into Byzantium",
            "The Temple of Artemis's complete disappearance — only one reconstructed column remains at the site — makes it the most thoroughly destroyed of the Seven Wonders, and its absence has given it a melancholy symbolic power as the emblem of irreversible cultural loss"
        ],
        "relationships": [
            {"entity": "Seven Wonders of the Ancient World", "relationship": "MEMBER_OF", "note": "The Temple of Artemis at Ephesus was one of the Seven Wonders — the largest temple in the ancient Greek world"},
            {"entity": "Croesus of Lydia", "relationship": "ORIGINAL_GREAT_TEMPLE_FUNDED_BY", "note": "Croesus funded the first great temple (c.550 BCE) — his name becoming proverbial for wealth through this and other acts of generosity"},
            {"entity": "Herostratus", "relationship": "BURNED_BY", "note": "Herostratus burned the temple (356 BCE) seeking immortality through destruction — on the night of Alexander the Great's birth"},
            {"entity": "Hagia Sophia (Constantinople)", "relationship": "STONES_REUSED_IN_CONSTRUCTION_OF", "note": "The destroyed temple's stones were used in the construction of Hagia Sophia — material transmutation of pagan antiquity into Byzantine Christianity"},
            {"entity": "Ephesus (ancient city)", "relationship": "FINANCIAL_AND_RELIGIOUS_CENTRE_OF", "note": "The temple was simultaneously the religious sanctuary, treasury-bank, and political institution that made Ephesus the most important city in the Aegean world"}
        ],
    }),

    ("ise-jingū", {
        "summary": (
            "The Ise Grand Shrine (伊勢神宮, Ise Jingū, est. traditionally 4 BCE — current structures rebuilt every 20 years) in Ise, Mie Prefecture, Japan, is the holiest site in Shinto — the shrine of Amaterasu Ōmikami, the sun goddess and divine ancestor of the Imperial Family — and the centre of the unique Japanese tradition of Shikinen Sengū (式年遷宮), in which the shrine buildings are demolished and identically rebuilt on adjacent plots every 20 years, with all fittings renewed. The current structures (2013) are the 62nd rebuilding since the tradition began c.690 CE.\n\n"
            "Ise Jingū's architectural style — Shinmei-zukuri, characterised by raised floors, thatched roofs, unpainted wood (Hinoki cypress), simple geometric forms, and the absence of Buddhist influence — preserves the aesthetic of Japanese proto-historic architecture in living practice. The Inner Shrine (Naikū) — containing Amaterasu's divine mirror (the Yata no Kagami), one of the Three Imperial Treasures — is so sacred that only members of the Imperial Family and senior Shinto priests may enter the innermost precinct.\n\n"
            "Ise Jingū's Shikinen Sengū tradition — which has been performed every 20 years for over 1,300 years — is the most extraordinary example of renewable sacred architecture in the world and embodies the Japanese aesthetic concept of renewal and impermanence (wabi and mono no aware). The tradition also serves a practical purpose: rebuilding every 20 years ensures that the carpentry and craft skills required for the shrine's construction are continuously transmitted to each generation of craftsmen."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Holiest site in Shinto; shrine of Amaterasu, divine ancestor of the Imperial Family; rebuilt identically every 20 years (Shikinen Sengū) for 1,300+ years — 62nd rebuilding in 2013; preserves proto-historic Japanese architectural style in living practice; houses the sacred mirror (one of the Three Imperial Treasures); uniquely models renewable sacred architecture.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Japanese imperial mythology's identification of the Imperial Family as descendants of Amaterasu Ōmikami — the sun goddess — created the theological mandate for a permanent shrine to Amaterasu that could be the focus of imperial devotion and national identity",
            "The Shikinen Sengū tradition's establishment (c.690 CE, attributed to Emperor Tenmu and Empress Jitō) institutionalised the 20-year rebuilding cycle — creating a mechanism that simultaneously renewed the sacred structure and transmitted craft skills across generations",
            "The Meiji restoration's elevation of Shinto to state religion (1868) — and Ise Jingū's designation as the primary national shrine — gave the complex renewed political significance as the spiritual centre of Japanese national identity"
        ],
        "effects": [
            "The Shikinen Sengū tradition — 20-year rebuilding of the shrine buildings for 1,300+ years — has continuously transmitted traditional Japanese carpentry and craft skills, ensuring that the techniques for building in the proto-historic Shinmei-zukuri style are still alive and practiced today",
            "Ise Jingū's preservation of Shinmei-zukuri architecture — unpainted Hinoki cypress, thatched roofs, raised floors — provides the most complete living record of pre-Buddhist Japanese architectural aesthetics, a form that would otherwise survive only in archaeological fragments",
            "The shrine's inaccessibility to non-Imperial visitors in the innermost precincts — maintained for 2,000 years — means that the sacred mirror (Yata no Kagami), one of the Three Imperial Treasures, has not been publicly displayed in living memory, making it the world's most inaccessible sacred relic",
            "Ise Jingū's annual pilgrimage — attracting 8 million annual visitors in modern times — has been a focus of Japanese devotional practice for two millennia, with Edo-period mass pilgrimages (okage-mairi) drawing millions from across Japan in spontaneous waves of popular religious enthusiasm"
        ],
        "relationships": [
            {"entity": "Amaterasu Ōmikami (sun goddess)", "relationship": "PRIMARY_SHRINE_OF", "note": "Ise Jingū is the shrine of Amaterasu — the sun goddess and divine ancestor of the Japanese Imperial Family"},
            {"entity": "Shikinen Sengū (20-year rebuilding)", "relationship": "SUBJECT_OF", "note": "The shrine is rebuilt identically every 20 years — the most extraordinary renewable sacred architecture tradition in the world, maintained since c.690 CE"},
            {"entity": "Japanese Imperial Family", "relationship": "MOST_SACRED_SHRINE_OF", "note": "The Inner Shrine — containing the sacred mirror — is so sacred that only Imperial Family members and senior priests may enter the innermost precinct"},
            {"entity": "Proto-historic Japanese architecture (Shinmei-zukuri)", "relationship": "LIVING_PRESERVATION_OF", "note": "The shrine's unpainted cypress, thatched roofs, and raised floors preserve proto-historic Japanese architectural aesthetics in living practice"},
            {"entity": "Yata no Kagami (sacred mirror)", "relationship": "HOUSES", "note": "The Inner Shrine houses the Yata no Kagami — one of the Three Imperial Treasures, not publicly displayed in living memory"}
        ],
    }),

    ("ranakpur-jain-temple", {
        "summary": (
            "The Ranakpur Jain Temple (राणकपुर जैन मंदिर, est. 1437–1458 CE) in Ranakpur, Rajasthan, India, is the most architecturally elaborate Jain temple in the world — the Chaturmukha Dharana Vihara (Four-Faced Sanctuary of Adinatha), dedicated to Adinatha, the first of the 24 Jain Tirthankaras — with 1,444 elaborately carved marble columns, no two identical, supporting a complex of 29 halls and 80 domed ceilings. The temple is a supreme example of the Māru-Gurjara architectural style and the finest achievement of medieval Rajasthani stone-carving.\n\n"
            "The temple was built under the patronage of Dharana Shah, a Jain merchant and minister of the Rana Kumbha of Mewar, with the master architect Deepa managing a workforce of craftsmen who spent over two decades executing the intricate marble carving. Every surface — columns, ceilings, doorways, brackets, walls — is covered in floral motifs, mythological scenes, celestial beings (apsaras), and depictions of the 24 Tirthankaras, creating an overwhelming visual richness that reflects the Jain theological concept of infinite complexity within cosmic order.\n\n"
            "The four-faced design — the Chaturmukha plan with four entrances facing the cardinal directions, each with a towering sikara (spire) — reflects the Jain belief that the Tirthankara Adinatha can be seen and approached from all directions. The temple complex is still an active place of worship, maintained by the Jain community, and receives 5,000+ visitors daily. The marble columns' shadow patterns change continuously throughout the day as sunlight moves across the carved surfaces, creating a dynamic visual experience unique in Indian temple architecture."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most architecturally elaborate Jain temple (est. 1437–1458 CE); 1,444 unique carved marble columns; 29 halls, 80 domed ceilings; supreme example of Māru-Gurjara architecture; finest medieval Rajasthani stone-carving; Chaturmukha four-faced design; 5,000+ daily visitors; still active place of worship.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Dharana Shah's religious devotion and mercantile wealth — as a Jain merchant and minister in the court of Rana Kumbha of Mewar — created the patronage that funded the 21-year construction programme of the most elaborate Jain temple ever built",
            "The Jain tradition's theological emphasis on the infinite complexity of the cosmos (anekantavada — the doctrine of non-one-sidedness) — expressed architecturally in the profusion of unique carved elements — provided the aesthetic-theological brief that motivated the 1,444 unique columns",
            "The availability of white Rajasthani marble from nearby Makrana — the same quarry that supplied marble for the Taj Mahal — and the highly developed tradition of Rajasthani stone-carving created the material and craft conditions for the temple's extraordinary elaboration"
        ],
        "effects": [
            "The Ranakpur temple's 1,444 unique marble columns — each differently carved, demonstrating the craftsmen's determination to create variety within a unified architectural programme — represent the most ambitious example of individual creative differentiation within a collective architectural project in medieval Indian history",
            "The Māru-Gurjara architectural tradition exemplified at Ranakpur — with its emphasis on carved surface richness, complex spatial sequences, and the integration of structural and decorative elements — influenced subsequent temple architecture across Rajasthan and Gujarat",
            "The temple's continued active use — maintained by the Jain community for 560+ years — demonstrates the extraordinary institutional continuity of the Jain religious tradition, which has sustained a building of extraordinary complexity in active worship since its construction",
            "Ranakpur's position as the finest example of Jain temple architecture has made it the primary reference point for scholars studying the Jain architectural tradition's contribution to Indian cultural heritage"
        ],
        "relationships": [
            {"entity": "Dharana Shah", "relationship": "COMMISSIONED_BY", "note": "Dharana Shah, Jain merchant and minister, funded the construction (1437–1458 CE) over 21 years"},
            {"entity": "Adinatha (first Jain Tirthankara)", "relationship": "DEDICATED_TO", "note": "The Chaturmukha Dharana Vihara is dedicated to Adinatha — the first of the 24 Jain Tirthankaras — approached from all four directions"},
            {"entity": "Māru-Gurjara architectural tradition", "relationship": "SUPREME_EXAMPLE_OF", "note": "Ranakpur is the supreme example of the Māru-Gurjara style — the finest achievement of medieval Rajasthani stone-carving"},
            {"entity": "Jain theological aesthetic (anekantavada)", "relationship": "ARCHITECTURAL_EXPRESSION_OF", "note": "The 1,444 unique columns express the Jain doctrine of infinite cosmic complexity — no two identical, within a unified architectural whole"},
            {"entity": "Rana Kumbha of Mewar", "relationship": "ROYAL_COURT_CONTEXT_OF_PATRON_OF", "note": "Dharana Shah was minister to Rana Kumbha — whose Mewar kingdom provided the political context for the temple's construction"}
        ],
    }),

    ("akshardham", {
        "summary": (
            "Akshardham (अक्षरधाम, est. 2005) in New Delhi, India, is the largest Hindu temple complex in the world by area — sprawling across 100 acres with the central mandap rising 43 metres, featuring 234 ornately carved pillars, 9 ornate domes, 20,000 murtis (divine sculptures), and extensive use of Rajasthani pink sandstone and Italian marble. Built by the BAPS Swaminarayan Sanstha (Bochasanwasi Akshar Purushottam Sanstha) in just five years (2000–2005), it was constructed by 11,000 craftsmen and 7,000 volunteers — with no steel or reinforced concrete used.\n\n"
            "The central monument — 109 metres wide, 96 metres long, 43 metres high — contains the murti of Swaminarayan in the central sanctum and is surrounded by 148 life-size stone elephants forming the lowest register of the exterior. The complex includes Sahaj Anand Water Show, an IMAX-style film theatre showing the life of Swaminarayan, boat rides through 10,000 years of India's cultural heritage, and a garden with 3,000 bronze sculptures — making it as much a spiritual theme park as a traditional temple.\n\n"
            "Akshardham was built in response to Swaminarayan's vision of a temple that would inspire dharma (right action) across generations. It opened in November 2005 — visited by 70 million people in its first 10 years — and holds the Guinness World Record for the world's largest comprehensive Hindu temple. It represents the contemporary Hindu temple as cultural institution: combining worship space, cultural exhibition, garden, and performance."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "World's largest comprehensive Hindu temple by area (est. 2005, New Delhi); 100 acres; 11,000 craftsmen, no steel or concrete; 20,000 murtis; Guinness World Record; 70 million visitors in first 10 years; contemporary model of the Hindu temple as cultural institution combining worship, exhibition, and performance.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The BAPS Swaminarayan Sanstha's 200th anniversary celebrations and its global growth — with 3,850 temples and 55,000 volunteers in 45 countries — created the institutional will and financial resources to build an unprecedented temple complex in the Indian capital as a statement of Swaminarayan Hinduism's global significance",
            "Pramukh Swami Maharaj's vision — shared with President A.P.J. Abdul Kalam — of a temple that would be 'a monument of Hinduism' demonstrating India's cultural achievements drove the ambition to create the world's largest comprehensive Hindu temple",
            "The availability of traditional craftsmen from Rajasthan, Gujarat, and Maharashtra — trained in the generations-old traditions of stone-carving and temple construction — and the revival of traditional no-steel construction methods allowed the BAPS to build in traditional style at unprecedented scale"
        ],
        "effects": [
            "Akshardham's 70 million visitors in its first decade — making it one of the most visited religious sites in the world — demonstrates the contemporary Hindu temple's capacity to function as a cultural destination attracting visitors regardless of religious affiliation",
            "The no-steel, no-concrete construction — using traditional Rajasthani pink sandstone and Italian marble, with traditional Rajasthani joinery techniques — has preserved and revived traditional Hindu temple construction skills that were at risk of disappearing in the era of reinforced concrete construction",
            "Akshardham's model — temple + cultural exhibitions + garden + performance + water show — has influenced subsequent Hindu temple construction globally, with BAPS temples in London, Toronto, and Houston incorporating similar cultural programming",
            "The complex's location adjacent to the 2010 Commonwealth Games village and its role as a diplomatic venue — visited by heads of state, described by President Obama as 'a beautiful embodiment of Indian culture' — has positioned it as a symbol of contemporary India's Hindu cultural identity on the global stage"
        ],
        "relationships": [
            {"entity": "BAPS Swaminarayan Sanstha", "relationship": "BUILT_AND_MAINTAINED_BY", "note": "Built by BAPS (2000–2005) — 11,000 craftsmen, 7,000 volunteers, no steel or concrete"},
            {"entity": "Pramukh Swami Maharaj", "relationship": "CONCEIVED_AND_INSPIRED_BY", "note": "Pramukh Swami Maharaj's vision — of a temple embodying Hinduism for future generations — drove the construction of Akshardham"},
            {"entity": "Swaminarayan movement (BAPS)", "relationship": "PRIMARY_MONUMENT_OF", "note": "Akshardham is the primary monument of the BAPS Swaminarayan movement — 3,850 temples and 55,000 volunteers globally"},
            {"entity": "Guinness World Records", "relationship": "HOLDS_RECORD_FOR_LARGEST_COMPREHENSIVE_HINDU_TEMPLE", "note": "Akshardham holds the Guinness World Record for the world's largest comprehensive Hindu temple"},
            {"entity": "Contemporary Hindu temple architecture", "relationship": "DEFINING_MODEL_OF", "note": "Akshardham's model — worship + cultural exhibition + garden + performance — defines the contemporary Hindu temple as cultural institution"}
        ],
    }),

]

# Skip any placeholder entries
ENTITIES_CLEAN = [
    (slug, data) for slug, data in ENTITIES
    if not data.get("summary", "").startswith("placeholder")
    and not (data.get("causes") and data["causes"][0].startswith("placeholder"))
]

if __name__ == "__main__":
    run_list = [
        ("ajanta-caves", ENTITIES[0][1]),
        ("borobudur-temple-compounds", ENTITIES[1][1]),
        ("temple-of-heaven", ENTITIES[2][1]),
        ("mahabodhi-temple", ENTITIES[3][1]),
        ("temple-of-ephesian-artemis", ENTITIES[4][1]),
        ("ise-jingū", ENTITIES[5][1]),
        ("ranakpur-jain-temple", ENTITIES[6][1]),
        ("akshardham", ENTITIES[7][1]),
    ]
    print(f"Batch 18 — {len(run_list)} entities (Class 343: Temples and Sacred Sites)")
    for slug, data in run_list:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
