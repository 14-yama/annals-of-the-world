#!/usr/bin/env python3
"""
Batch 22 — 8 entities (Class 342): Famous Mosques — South Asia, West Africa, Persia, Maghreb
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/342-Class-342"
FILE_PREFIX = "342"


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

    ("badshahi-mosque", {
        "summary": (
            "Badshahi Mosque (بادشاہی مسجد, Imperial Mosque, est. 1671–1673 CE) in Lahore, Pakistan, is one of the largest mosques in the world — with a courtyard capable of accommodating 100,000 worshippers — and the supreme achievement of Mughal mosque architecture, built by Emperor Aurangzeb as the last great Mughal imperial monument. The mosque's four minarets (each 53.6 metres) and three marble domes against a red sandstone facade create the definitive image of Mughal architectural grandeur.\n\n"
            "The Badshahi Mosque was built in just two years (1671–1673) — a remarkable speed for a building of such scale — under the supervision of Muzaffar Hussain, a cousin of Aurangzeb. The architectural programme is derived from the Jama Masjid in Delhi (built by Shah Jahan, 1644–1656), which the Badshahi elaborates and supersedes in scale. The red sandstone and white marble combination — the defining palette of Mughal imperial architecture — is used with maximum effect: the red sandstone body contrasting with the white marble domes and inlaid marble decoration.\n\n"
            "The mosque's turbulent post-Mughal history reflects the history of Lahore itself: it was used as a stable by the Sikh Empire under Ranjit Singh (1799–1839), then as a garrison by the British (1848–1856), before being restored to religious use. During Pakistan's partition (1947), the mosque became the symbolic heart of the new Islamic state, hosting some of the largest gatherings in the subcontinent's history. It remains one of the most visited religious monuments in South Asia."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Last great Mughal imperial mosque (est. 1671–1673 CE); built by Aurangzeb; courtyard for 100,000 worshippers; four 53.6m minarets; supreme achievement of Mughal mosque architecture; used as Sikh stable (1799) and British garrison (1848); symbolic heart of Pakistan at partition (1947); one of largest mosques in world.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Emperor Aurangzeb's desire to build a mosque that would surpass Shah Jahan's Jama Masjid in Delhi — the previous supreme expression of Mughal imperial mosque-building — created the architectural brief for the largest Mughal mosque ever constructed",
            "The strategic placement of the Badshahi Mosque opposite the Lahore Fort — creating a monumental civic axis at the heart of the Mughal provincial capital — reflected Aurangzeb's assertion of both religious and imperial authority over his empire's richest province",
            "The Mughal Empire's access to the red sandstone quarries of Rajasthan and the marble quarries of Makrana provided the materials for the mosque's iconic red sandstone and white marble combination"
        ],
        "effects": [
            "The Badshahi Mosque's scale — 100,000-worshipper courtyard, four 53m minarets — established it as the supreme architectural statement of Mughal imperial power at its territorial zenith, making it the defining monument of Aurangzeb's reign",
            "The mosque's use as a Sikh stable (under Ranjit Singh) and British garrison represents the complete subordination of Mughal religious and political authority — its restoration to religious use (1856) is a monument to the endurance of Islamic institutions through colonial transformation",
            "The mosque's role at Pakistan's partition (1947) — becoming the symbolic religious heart of the new Islamic state — transformed a Mughal imperial monument into a Pakistani national icon, demonstrating the capacity of pre-colonial monuments to acquire new national meanings",
            "The Badshahi Mosque's architectural influence — red sandstone, white marble domes, four-minaret scheme — was transmitted across South Asia in subsequent mosque design, becoming the canonical form of the South Asian Friday mosque"
        ],
        "relationships": [
            {"entity": "Emperor Aurangzeb (Mughal Empire)", "relationship": "COMMISSIONED_BY", "note": "Aurangzeb built the Badshahi as the last great Mughal imperial mosque (1671–1673) — surpassing Shah Jahan's Jama Masjid in Delhi"},
            {"entity": "Mughal imperial architecture", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "The Badshahi is the supreme achievement of Mughal mosque architecture — the culmination of the red sandstone and white marble tradition"},
            {"entity": "Lahore Fort (adjacent monument)", "relationship": "MONUMENTAL_AXIS_WITH", "note": "The mosque and fort form the monumental civic axis of Lahore — the supreme ensemble of Mughal provincial architectural grandeur"},
            {"entity": "Sikh Empire (Ranjit Singh)", "relationship": "CONVERTED_TO_STABLE_BY", "note": "Ranjit Singh used the mosque as a stable (1799–1839) — representing the complete reversal of Mughal imperial authority"},
            {"entity": "Pakistan (1947)", "relationship": "SYMBOLIC_HEART_AT_FOUNDING_OF", "note": "The Badshahi Mosque became the symbolic centre of Pakistan's Islamic identity at partition — a Mughal monument adopted by the new nation-state"}
        ],
    }),

    ("djinguereber-mosque", {
        "summary": (
            "Djinguereber Mosque (Sankore Mosque variant; est. 1327 CE) in Timbuktu, Mali, is the oldest mosque in Sub-Saharan Africa — built by King Musa I (Mansa Musa) of the Mali Empire following his legendary Hajj to Mecca in 1324–1325, during which he distributed so much gold that he caused gold price inflation across Egypt and the Middle East for a decade. The mosque is the supreme example of Sudano-Sahelian mosque architecture — a tradition using mud brick (banco), wooden armatures, and ostrich eggs as finials that is entirely distinct from Middle Eastern or North African Islamic architecture.\n\n"
            "The mosque was designed by Abu Ishaq al-Sahili, a poet and architect from Granada (Al-Andalus) whom Mansa Musa brought back from Mecca. The building's organic, sculptural form — with projecting wooden beams (toron) supporting the walls and enabling the annual maintenance replastering, with ostrich eggs on the finials representing fertility and purity — created a new architectural tradition that shaped mosque design across the West African Sahel for 700 years.\n\n"
            "Timbuktu's three great mosques (Djinguereber, Sankore, Sidi Yahia) were the centre of the most important Islamic scholarly community in Sub-Saharan Africa — the University of Sankore system — which at its peak (15th–16th centuries) enrolled up to 25,000 students and possessed a library of 700,000 manuscripts, making Timbuktu the most important centre of Islamic learning in the world outside the Arab heartlands."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest mosque in Sub-Saharan Africa (est. 1327 CE); built by Mansa Musa after his legendary 1324 Hajj (gold distribution caused regional inflation); designed by Abu Ishaq al-Sahili from Granada; supreme example of Sudano-Sahelian mud brick architecture; centre of Timbuktu's Islamic scholarly tradition (25,000 students, 700,000 manuscripts); UNESCO World Heritage.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Mansa Musa's legendary Hajj to Mecca (1324–1325) — during which he distributed so much gold that he caused price inflation across Egypt — brought him into contact with Middle Eastern Islamic architecture and scholarship, inspiring him to commission a great mosque in his capital on his return",
            "The appointment of Abu Ishaq al-Sahili — a poet-architect from Andalusia who had acquired knowledge of North African mud brick construction — to design the mosque created the synthesis of Andalusian Islamic aesthetics with West African building materials that produced Sudano-Sahelian mosque architecture",
            "The establishment of Timbuktu as the Mali Empire's commercial and religious capital — at the intersection of trans-Saharan trade routes — created both the wealth and the intellectual culture that required a mosque of exceptional ambition"
        ],
        "effects": [
            "Djinguereber Mosque established the Sudano-Sahelian architectural tradition — mud brick, projecting wooden beams, ostrich egg finials — that shaped mosque design across the West African Sahel (Mali, Burkina Faso, Nigeria, Niger) for 700 years",
            "The mosque's role as the centre of the University of Sankore system — enrolling up to 25,000 students at its peak — made Timbuktu the most important centre of Islamic scholarship in Sub-Saharan Africa, comparable to medieval European universities",
            "The 700,000-manuscript library of Timbuktu — associated with the Sankore mosque complex — is the most important single archive of African Islamic scholarship and constitutes an irreplaceable record of West African intellectual, scientific, and religious history",
            "Mansa Musa's gold distribution during the 1324 Hajj — which caused a decade of gold price inflation across Egypt and the Middle East — and his commissioning of Djinguereber established the Mali Empire's extraordinary wealth and sophistication in the consciousness of the medieval Islamic world"
        ],
        "relationships": [
            {"entity": "Mansa Musa (Musa I, Mali Empire)", "relationship": "COMMISSIONED_BY_FOLLOWING_HAJJ_OF", "note": "Mansa Musa commissioned the mosque (1327) after returning from his legendary 1324 Hajj — the most celebrated African pilgrimage in history"},
            {"entity": "Abu Ishaq al-Sahili (architect from Granada)", "relationship": "DESIGNED_BY", "note": "Al-Sahili — brought from Mecca by Mansa Musa — fused Andalusian Islamic aesthetics with West African mud brick construction"},
            {"entity": "University of Sankore (Timbuktu)", "relationship": "PART_OF_SCHOLARLY_COMPLEX_OF", "note": "Timbuktu's three mosques formed the centre of a university system with 25,000 students and 700,000 manuscripts — the most important African Islamic scholarly tradition"},
            {"entity": "Sudano-Sahelian mosque architecture", "relationship": "FOUNDING_MONUMENT_OF", "note": "Djinguereber established the mud brick and projecting timber tradition that shaped mosque design across the West African Sahel for 700 years"},
            {"entity": "UNESCO World Heritage (Timbuktu)", "relationship": "INSCRIBED_AS_PART_OF", "note": "The Timbuktu mosques are part of the UNESCO World Heritage inscription for the city of Timbuktu (1988)"}
        ],
    }),

    ("hassan-ii-mosque", {
        "summary": (
            "Hassan II Mosque (المسجد الحسني, Mosquée Hassan II, est. 1986–1993 CE) in Casablanca, Morocco, is the largest mosque in Africa and the fifth-largest mosque in the world — built over the Atlantic Ocean on an artificially reclaimed platform, with a retractable roof, a glass floor over the sea, laser beams pointing toward Mecca from the top of its 210-metre minaret (the tallest minaret in the world), and a capacity for 105,000 worshippers. It is the most technologically advanced mosque ever built.\n\n"
            "The mosque was commissioned by King Hassan II (1929–1999) to mark the 1,400th anniversary of the Prophet Muhammad's birth and to create a monument that would place Morocco at the centre of the contemporary Islamic world. The design by French architect Michel Pinseau incorporates traditional Moroccan craftsmanship — zellige tilework, carved plaster, cedar wood ceilings — at a scale never previously achieved, with 6,000 Moroccan craftsmen spending six years executing the interior's hand-crafted decorations.\n\n"
            "The Hassan II Mosque's coastal position — partly over the Atlantic, with its glass floor allowing worshippers to pray over the sea — realises a verse from the Quran cited by King Hassan II: 'The throne of God was built on water.' The mosque's spectacular scale, technological sophistication, and traditional craftsmanship made it the defining monument of late 20th-century Islamic architecture, demonstrating that contemporary Islamic building could match both traditional craft mastery and modernist engineering."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest mosque in Africa (est. 1986–1993 CE); 210m minaret — tallest in world; glass floor over the Atlantic Ocean; retractable roof; 105,000-worshipper capacity; 6,000 craftsmen, 6 years of hand-crafted zellige and cedar decoration; commissioned by King Hassan II for Prophet's 1,400th birth anniversary; most technologically advanced mosque ever built.",
            "significanceCategory": "continental"
        },
        "causes": [
            "King Hassan II's desire to create a mosque that would mark the 1,400th anniversary of the Prophet Muhammad's birth and establish Morocco as a leader of contemporary Islamic civilisation drove the commission of the most ambitious mosque project of the 20th century",
            "The Quranic verse 'the throne of God was built on water' — cited by King Hassan II as the inspiration for building over the Atlantic — provided the theological justification for the unprecedented coastal location",
            "Morocco's Maliki Islamic tradition — emphasising the craft traditions of zellige, carved plaster, and cedar wood — required that the world's largest contemporary mosque be decorated entirely in traditional Moroccan handicraft techniques, creating the extraordinary combination of technological scale and artisanal precision"
        ],
        "effects": [
            "The Hassan II Mosque's 210-metre minaret — the tallest in the world — and its laser beam pointing toward Mecca created the defining visual symbol of contemporary Moroccan Islamic identity, visible from the Atlantic and across Casablanca",
            "The employment of 6,000 Moroccan craftsmen for six years — executing the zellige, carved plaster, and cedar wood decorations — preserved and transmitted traditional Moroccan craft traditions at a scale that would not otherwise have been economically viable, effectively underwriting the survival of these craft skills for a generation",
            "The mosque's coastal position and architectural spectacle made Casablanca the primary destination for architectural tourism in Morocco, transforming the commercial capital's identity from a French colonial port city to an Islamic architectural landmark",
            "The Hassan II Mosque demonstrated that large-scale contemporary Islamic architecture could successfully integrate traditional craft mastery with modern engineering — establishing a model for subsequent grand mosque projects in Saudi Arabia, Qatar, and elsewhere in the Islamic world"
        ],
        "relationships": [
            {"entity": "King Hassan II of Morocco", "relationship": "COMMISSIONED_BY", "note": "King Hassan II commissioned the mosque to mark the 1,400th anniversary of the Prophet's birth and assert Morocco's Islamic leadership"},
            {"entity": "Casablanca (Morocco)", "relationship": "DEFINES_SKYLINE_OF", "note": "The 210m minaret and coastal position make the mosque the defining landmark of Casablanca — Morocco's commercial capital"},
            {"entity": "Moroccan traditional crafts (zellige, carved plaster, cedar)", "relationship": "LARGEST_COMMISSION_OF", "note": "6,000 craftsmen over six years — the largest single commission of traditional Moroccan handicraft skills in history"},
            {"entity": "210m minaret (world's tallest)", "relationship": "TOPPED_BY_THE", "note": "The 210m minaret — with laser pointing toward Mecca — is the tallest minaret in the world"},
            {"entity": "Contemporary Islamic architecture", "relationship": "DEFINING_MONUMENT_OF", "note": "The Hassan II Mosque demonstrated that contemporary Islamic architecture could combine modern engineering scale with traditional craft mastery"}
        ],
    }),

    ("koutoubia-mosque", {
        "summary": (
            "Koutoubia Mosque (مسجد الكتبية, Mosque of the Booksellers, est. 12th century CE, current structure 1158 CE) in Marrakech, Morocco, is the largest mosque in Marrakech, the prototype for the Giralda tower in Seville and the Hassan Tower in Rabat, and the supreme example of Almohad mosque architecture — whose minaret (70 metres) established the canonical form of the North African and Andalusian mosque minaret that was exported to Spain through the Almohad conquest. The mosque's minaret is the most influential single tower in the history of Islamic architecture west of the Nile.\n\n"
            "The current mosque (1158 CE, under Almohad Caliph Abd al-Mu'min) replaced an earlier mosque built over the remains of a Almoravid palace. The minaret — 12.8 metres square and 67 metres high — established the proportional system (height 5× the base width) that governed North African and Andalusian minaret design for centuries. The minaret's decoration — five tiers of geometric tracery, arched windows, and blind arcades — progressing from simple patterns at the base to complex muqarnas at the crown, became the model for the Giralda (Seville, 1184), the Hassan Tower (Rabat, 1196), and the Kutubiyya itself was imitated in the Mosque of Tinmal.\n\n"
            "The mosque's name — 'Booksellers' — derives from the market of manuscript dealers that surrounded the mosque in the Almohad period, when Marrakech was the capital of an empire stretching from the Atlantic to Tripolitania and from the Sahara to central Spain. The Koutoubia's setting — with the Atlas Mountains visible behind it — is one of the most celebrated natural-architectural compositions in North Africa."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest mosque in Marrakech (est. 1158 CE); supreme example of Almohad mosque architecture; 70m minaret — prototype for the Giralda (Seville) and Hassan Tower (Rabat); established canonical North African minaret proportional system (height 5× base); name derives from manuscript booksellers; Almohad capital spanning Atlantic to Tripolitania; Atlas Mountains backdrop.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Almohad dynasty's imperial ambition — ruling an empire stretching from the Atlantic to Tripolitania and from the Sahara to central Spain — required a capital mosque that expressed the power and religious orthodoxy of the most extensive North African empire since the Romans",
            "Abd al-Mu'min's decision to rebuild the earlier mosque (1158) — destroying the Almoravid predecessor — was a deliberate act of Almohad architectural supremacy, replacing Almoravid decorative exuberance with the severe geometric rigour of Almohad aesthetics",
            "The manuscript market that surrounded the mosque — giving it the name 'Koutoubia' (booksellers) — reflected Marrakech's role as the intellectual capital of the western Islamic world, where the production and trade of religious, scientific, and literary texts was concentrated around the Friday mosque"
        ],
        "effects": [
            "The Koutoubia minaret's proportional system (height 5× base width) became the canonical standard for North African and Andalusian mosque minarets, directly determining the dimensions of the Giralda in Seville (1184), the Hassan Tower in Rabat (1196), and countless subsequent minarets across Morocco and Andalusia",
            "The Giralda — the Almohad mosque minaret in Seville that was later converted to the bell tower of Seville Cathedral — is the most celebrated architectural export of the Koutoubia tradition, making the Koutoubia the architectural ancestor of the most famous building in southern Spain",
            "The manuscript market around the Koutoubia created a model of intellectual commerce centred on the mosque that made Marrakech the primary centre of Islamic book production and trade in the western Mediterranean during the Almohad period",
            "The mosque's Atlas Mountain backdrop — creating the defining image of Marrakech's architectural landscape — has made the Koutoubia the most photographed building in Morocco and the visual symbol of Marrakech internationally"
        ],
        "relationships": [
            {"entity": "Almohad Caliph Abd al-Mu'min", "relationship": "REBUILT_BY", "note": "Abd al-Mu'min commissioned the current mosque (1158 CE) — replacing the Almoravid predecessor with Almohad architectural severity"},
            {"entity": "Giralda tower (Seville Cathedral)", "relationship": "DIRECT_ARCHITECTURAL_PROTOTYPE_OF", "note": "The Giralda — Seville's famous Almohad minaret/bell tower — was directly modelled on the Koutoubia's proportions and decoration"},
            {"entity": "Hassan Tower (Rabat)", "relationship": "DIRECT_ARCHITECTURAL_PROTOTYPE_OF", "note": "The Hassan Tower (Rabat, 1196) follows the same proportional system as the Koutoubia — both express the Almohad canonical minaret form"},
            {"entity": "North African Islamic manuscript trade", "relationship": "COMMERCIAL_CENTRE_FOR", "note": "The manuscript booksellers (kuttubiyyin) surrounding the mosque made Marrakech the primary Islamic book market of the western Mediterranean"},
            {"entity": "Almohad Empire (12th–13th centuries)", "relationship": "SUPREME_RELIGIOUS_MONUMENT_OF", "note": "The Koutoubia was the Friday mosque of the Almohad imperial capital — the supreme monument of the most extensive North African empire since Rome"}
        ],
    }),

    ("nasir-ol-molk-mosque", {
        "summary": (
            "Nasir-ol-Molk Mosque (مسجد نصیرالملک, Pink Mosque, est. 1876–1888 CE) in Shiraz, Iran, is the most visually spectacular mosque in Iran — famous for its extraordinary interior display of coloured light, created by the largest expanse of stained glass in any Iranian mosque, which floods the main prayer hall with pink, red, blue, and gold light each morning, earning it the epithet 'the Pink Mosque'. Built during the Qajar dynasty (1779–1925), it represents the final flowering of Persian mosque architecture before the 20th century.\n\n"
            "The mosque was commissioned by Mirza Hasan Ali Nasir-ol-Molk — a high official of the Qajar court — and built by master architects Mohammad Hassan Memaar and Mohammad Reza Kashi-Paz. The interior is a total artwork: the entire prayer hall ceiling is covered in intricate muqarnas (honeycomb vaulting) with painted plasterwork in geometric and floral patterns; the seven arched bays of the winter prayer hall are separated by twisted fluted columns; and the entire south facade is decorated in faience tile panels in a polychrome palette of extraordinary richness.\n\n"
            "The timing of the morning light — illuminating the prayer hall through the stained glass with a shifting kaleidoscope of colour between 8 and 10 AM — makes the Nasir-ol-Molk Mosque one of the most visited religious buildings in Iran, attracting photographers from around the world who seek the moment when the entire interior is filled with coloured light. It is a UNESCO World Heritage Site candidate and one of the most photographed interiors in the world."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Most visually spectacular mosque in Iran (est. 1876–1888 CE); largest stained glass in any Iranian mosque; 'Pink Mosque' — morning light floods interior with pink, red, blue, gold; intricate muqarnas ceiling; twisted fluted columns; polychrome faience tile facade; final flowering of Persian mosque architecture before 20th century; one of the world's most photographed interiors.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mirza Hasan Ali Nasir-ol-Molk's personal wealth and his position as a high official of the Qajar court enabled the commission of the most ornate mosque construction in Iran since the Safavid period — a private commission that could deploy the full range of Persian craft mastery",
            "The Qajar dynasty's programme of Persian cultural revival — reasserting Persian artistic traditions after the Safavid empire's collapse — drove the employment of master craftsmen from across Iran to create the mosque's extraordinary multicoloured faience, stained glass, and plasterwork",
            "The introduction of stained glass techniques to Persian mosque architecture — influenced by Ottoman and European glass traditions via the Qajar court's international connections — created the novel element (large-scale coloured glass in a mosque's prayer hall) that makes the Nasir-ol-Molk unique"
        ],
        "effects": [
            "The Nasir-ol-Molk Mosque's morning light display — a kaleidoscope of colour through the largest stained glass in any Iranian mosque — became the defining image of Persian mosque interior aesthetics in the international imagination, making it the single most photographed mosque interior in the world",
            "The mosque's extraordinary completeness — faience tiles, stained glass, muqarnas, twisted columns, painted plaster all in perfect condition — makes it the most complete surviving example of late Qajar-era Persian decorative arts, an irreplaceable record of the final flowering of Persian mosque architecture",
            "The mosque's international photographic fame — making it the most googled mosque in the world in some years — has transformed Shiraz into a major destination for architectural tourism, driving economic development in a city that was already known for its poetry (Hafez, Sa'di) and gardens",
            "The stained glass tradition established at Nasir-ol-Molk influenced subsequent Persian and Iranian mosque design, introducing coloured glass as an element of Persian sacred architecture that had not previously been part of the tradition"
        ],
        "relationships": [
            {"entity": "Mirza Hasan Ali Nasir-ol-Molk", "relationship": "COMMISSIONED_BY", "note": "Nasir-ol-Molk — a high Qajar court official — commissioned the mosque (1876–1888) as a private act of patronage"},
            {"entity": "Qajar dynasty (Iran)", "relationship": "SUPREME_ARCHITECTURAL_ACHIEVEMENT_OF", "note": "The mosque represents the final flowering of Persian mosque architecture under the Qajar dynasty (1779–1925)"},
            {"entity": "Persian mosque architectural tradition", "relationship": "FINAL_MASTERPIECE_OF_CLASSICAL", "note": "The Nasir-ol-Molk is the last great classical Persian mosque before the 20th century disrupted traditional patronage systems"},
            {"entity": "Stained glass in Persian mosque architecture", "relationship": "MOST_CELEBRATED_EXAMPLE_OF", "note": "The largest expanse of stained glass in any Iranian mosque creates the morning light display that made the mosque world-famous"},
            {"entity": "Shiraz (city of poetry and gardens)", "relationship": "DEFINING_ARCHITECTURAL_LANDMARK_OF", "note": "The mosque — alongside the tombs of Hafez and Sa'di — makes Shiraz the most culturally layered city in Iran"}
        ],
    }),

    ("sheikh-lotfollah-mosque", {
        "summary": (
            "Sheikh Lotfollah Mosque (مسجد شیخ لطف‌الله, est. 1603–1619 CE) in Isfahan, Iran, is the most intimate and perfect mosque in Iran — built by Shah Abbas I of the Safavid dynasty as the private royal mosque of the imperial court, reserved for the use of the royal family and their entourage rather than the general public. It stands on the east side of the Naqsh-e Jahan Square in Isfahan — one of the largest public squares in the world — directly facing the Ali Qapu royal palace and expressing the spatial dialogue between royal religious devotion and imperial display.\n\n"
            "The mosque is a masterpiece of Persian tile work: the dome — covered in cream-coloured arabesque tiles that shift from pale in early morning to deep gold in late afternoon as the light changes — is considered the most beautiful dome surface in Iranian architecture. The interior is equally exceptional: a single domed prayer hall (with no courtyard, minaret, or columned prayer hall, as it was never used for Friday prayers), where the entire surface — dome, walls, arch reveals — is covered in an unbroken carpet of polychrome faience tile in turquoise, deep blue, and white.\n\n"
            "The mosque contains no minarets (as it was not a congregational mosque requiring a call to prayer), and its entrance is subtly offset from the facade — both features that were deliberate design choices expressing the building's intimate, private character. The Naqsh-e Jahan Square ensemble — Sheikh Lotfollah Mosque, the Imam Mosque (Shah Mosque), and the Ali Qapu Palace — was designated a UNESCO World Heritage Site in 1979."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most perfect mosque in Iran (est. 1603–1619 CE); private royal mosque of Shah Abbas I (Safavid dynasty); most beautiful dome surface in Persian architecture — cream arabesque tiles shifting from pale to gold; single prayer hall with no courtyard or minaret; part of Naqsh-e Jahan Square UNESCO World Heritage (1979); intimate dialogue with Ali Qapu royal palace.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Shah Abbas I's desire to create a private royal mosque worthy of the Safavid court's religious devotion — separate from the public Imam Mosque across the square — drove the commission of a building of extreme intimacy and perfection rather than public scale",
            "The Safavid imperial programme of transforming Isfahan into the most beautiful city in the Islamic world — expressed in the Naqsh-e Jahan Square ensemble — required that every building on the square be a masterwork, creating the patron's brief for a mosque of extraordinary tile craftsmanship",
            "The mosque's dedication to Sheikh Lotfollah Nasiri — a celebrated Shia scholar who was Shah Abbas's father-in-law — gave it a personal religious significance that demanded the highest craft standards as an act of filial and devotional piety"
        ],
        "effects": [
            "The Sheikh Lotfollah Mosque's dome — the most beautiful in Persian architecture — established the standard against which all subsequent Persian mosque domes are measured, its colour-shifting cream arabesques representing the apex of Safavid tile craftsmanship",
            "The mosque's no-courtyard, no-minaret, single-hall plan — breaking every convention of Islamic mosque design — demonstrated that Persian architectural genius could transcend established typologies when freed from the requirement of public religious function",
            "The Naqsh-e Jahan Square ensemble — Sheikh Lotfollah Mosque, Imam Mosque, Ali Qapu Palace — is the most complete surviving 17th-century royal urban ensemble in the world, making Isfahan the best-preserved example of Safavid imperial city planning",
            "The mosque's intimate scale and private function have made it the most beloved mosque in Iran among architects and art historians — cited more frequently than the larger Imam Mosque as the supreme achievement of Persian mosque architecture"
        ],
        "relationships": [
            {"entity": "Shah Abbas I (Safavid Empire)", "relationship": "COMMISSIONED_BY", "note": "Shah Abbas I built the mosque (1603–1619) as his private royal chapel — separate from the public Imam Mosque across Naqsh-e Jahan Square"},
            {"entity": "Naqsh-e Jahan Square (Isfahan)", "relationship": "EASTERN_JEWEL_OF", "note": "Sheikh Lotfollah Mosque faces the Ali Qapu Palace across Naqsh-e Jahan Square — one of the world's greatest urban ensembles"},
            {"entity": "Safavid Persian tile craftsmanship", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "The dome's colour-shifting cream arabesques represent the apex of Safavid faience tile-making — the most beautiful dome surface in Persian architecture"},
            {"entity": "Persian mosque architecture", "relationship": "MOST_PERFECT_EXAMPLE_OF", "note": "The mosque's intimate scale, total tile coverage, and design freedom make it the most perfect example of Persian mosque architecture"},
            {"entity": "UNESCO World Heritage (Naqsh-e Jahan Square)", "relationship": "INSCRIBED_AS_PART_OF", "note": "The Naqsh-e Jahan Square ensemble was the first Iranian site inscribed as UNESCO World Heritage (1979)"}
        ],
    }),

    ("wazir-khan-mosque", {
        "summary": (
            "Wazir Khan Mosque (وزیر خان مسجد, est. 1634–1641 CE) in Lahore, Pakistan, is the most ornate mosque of the Mughal period — built by Hakim Ilm-ud-din Ansari (Wazir Khan), the governor of Punjab under Emperor Shah Jahan, and celebrated as the 'Jewel of Mughal Architecture' for its extraordinary polychrome tile work (kashi-kari) that covers nearly every surface of the building in intricate floral, geometric, and calligraphic patterns executed in more than 45,000 individual tiles.\n\n"
            "The mosque's tile work represents the apex of the kashi-kari tradition — painted and glazed tile panels combining Mughal floral motifs with Persian geometric patterns in a colour palette of cobalt blue, turquoise, green, gold, and white. The five-arched facade, the four minarets (each rising from a corner of the mosque's courtyard and decorated with the same polychrome tiles), and the fresco-decorated kiosks (dalans) create a chromatic spectacle unique among Mughal mosques — combining the robust architectural scale of Mughal building with the intimate, jewel-like decoration of Persian manuscript painting.\n\n"
            "The mosque is located in the Walled City of Lahore — a UNESCO World Heritage Site — and is surrounded by a bazaar (Wazir Khan Chowk) that has been trading continuously since the Mughal period. The mosque's spectacular kashi-kari was restored in a major conservation project (2009–2015) that trained over 200 craftsmen in the traditional tile-making techniques, reviving a craft tradition that had nearly disappeared."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most ornate Mughal mosque (est. 1634–1641 CE); 45,000+ individual polychrome tiles covering every surface (kashi-kari); 'Jewel of Mughal Architecture'; built by Wazir Khan under Shah Jahan; apex of Mughal tile-making tradition; UNESCO Walled City of Lahore; 2009–2015 restoration trained 200 craftsmen, reviving near-extinct tile tradition.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Wazir Khan's personal wealth as governor of Punjab (under Shah Jahan) and his desire to build a mosque that would rival the Badshahi Mosque in beauty if not in scale drove the commission of the most ornate mosque of the Mughal period",
            "The court culture of Shah Jahan — whose reign produced the Taj Mahal, the Red Fort in Delhi, and the Jama Masjid — created an atmosphere of competitive architectural patronage that pushed provincial governors to commission ever more elaborate buildings",
            "The availability of master kashi-kari craftsmen in Lahore — inheriting a tradition transmitted from Persia and Central Asia through Mughal trade networks — made it possible to cover a large mosque with 45,000 individually crafted tiles"
        ],
        "effects": [
            "The Wazir Khan Mosque's kashi-kari established the apex of Mughal polychrome tile tradition — a fusion of Persian glazed tile techniques with Mughal floral and geometric motifs — that influenced mosque decoration across South Asia for centuries",
            "The mosque's 2009–2015 conservation project — training over 200 craftsmen in traditional kashi-kari techniques — revived a craft tradition that had nearly disappeared, creating a living transmission of Mughal tile-making skills to a new generation of Pakistani artisans",
            "The mosque's location in the Walled City of Lahore — at the heart of a continuously occupied Mughal bazaar — makes it the most intact example of Mughal urban commercial and religious life, with the mosque-bazaar relationship unchanged since the 17th century",
            "The mosque's chromatic spectacle — polychrome tiles, frescoes, calligraphy — influenced the subsequent development of Mughal decorative arts in the Punjab, establishing Lahore as the centre of the kashi-kari tradition in South Asia"
        ],
        "relationships": [
            {"entity": "Hakim Ilm-ud-din Ansari (Wazir Khan)", "relationship": "COMMISSIONED_BY", "note": "Wazir Khan, governor of Punjab under Shah Jahan, built the mosque (1634–1641) — the most ornate Mughal religious building"},
            {"entity": "Shah Jahan (Mughal Emperor)", "relationship": "REIGN_DURING_WHICH_BUILT", "note": "Built during Shah Jahan's reign — the same period as the Taj Mahal, Red Fort, and Jama Masjid Delhi — the apex of Mughal architectural patronage"},
            {"entity": "Kashi-kari polychrome tile tradition", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "45,000+ individual polychrome tiles covering every surface — the apex of Mughal kashi-kari craftsmanship"},
            {"entity": "Walled City of Lahore (UNESCO)", "relationship": "JEWEL_OF", "note": "The mosque is the finest building in the UNESCO Walled City of Lahore, surrounded by a Mughal bazaar in continuous use since the 17th century"},
            {"entity": "2009–2015 conservation project", "relationship": "REVIVED_BY", "note": "A conservation project trained 200 craftsmen in traditional kashi-kari — reviving a near-extinct Mughal tile-making tradition"}
        ],
    }),

    ("jama-masjid-delhi", {
        "summary": (
            "Jama Masjid Delhi (جامع مسجد, Friday Mosque, est. 1644–1656 CE) in Delhi, India, is the largest mosque in India — with a courtyard accommodating 25,000 worshippers — and the greatest mosque of Shah Jahan's reign, built simultaneously with the Red Fort (Lal Qila) as the twin monuments of Shahjahanabad, the new Mughal capital. The mosque's three marble domes and two minarets (41 metres) dominate the skyline of Old Delhi from a raised plinth, creating the most magnificent Mughal civic ensemble in existence.\n\n"
            "The mosque was built by Emperor Shah Jahan over twelve years using 5,000 workmen daily — with red sandstone and white marble, the imperial Mughal palette — at a cost of one million rupees. The three marble domes (alternating white marble and black-stripe) and the two minarets (red sandstone with marble bands) represent the perfected version of the Mughal mosque form, elaborating the tradition established by Akbar's mosques at Fatehpur Sikri and refined through the 17th century.\n\n"
            "The Jama Masjid has been the spiritual heart of Delhi's Muslim community since its completion and is the site of some of the most significant events in modern Indian Muslim history — including Mughal emperor Bahadur Shah Zafar's last sermon before the 1857 First War of Indian Independence, the mosque's occupation by British troops after 1857, and its role as the focal point of Delhi's Muslim identity through Partition (1947). The mosque holds a relic of the Prophet Muhammad — a hair, a sandal, and a verse from the Quran in his handwriting — in a marble reliquary."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest mosque in India (est. 1644–1656 CE); greatest Shah Jahan mosque; 25,000-worshipper courtyard; twin monument with Red Fort in Shahjahanabad; 5,000 workmen, 12 years, 1 million rupees; Bahadur Shah Zafar's last sermon before 1857 uprising; spiritual heart of Delhi's Muslim community through Partition; holds Prophet Muhammad's hair relic.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Shah Jahan's programme of constructing a new capital city (Shahjahanabad, now Old Delhi) — with the Red Fort and Jama Masjid as its twin civic monuments — required a mosque of sufficient scale to serve as the Friday mosque for the entire Mughal imperial capital",
            "The Mughal tradition of the emperor personally leading Friday prayers at the imperial mosque — establishing the religious and political unity of the imperial household — drove the construction of a mosque directly adjacent to the Red Fort, connected by a covered passageway",
            "The twelve-year construction timeline (1644–1656) and the daily employment of 5,000 workmen reflected Shah Jahan's determination to create a mosque that would surpass all previous Mughal examples and serve as the definitive statement of Mughal imperial mosque architecture"
        ],
        "effects": [
            "The Jama Masjid became the definitive model for the South Asian Friday mosque — its three-dome and two-minaret scheme, red sandstone and marble palette, and raised plinth overlooking a vast courtyard establishing the canonical form that subsequent mosques across the subcontinent sought to emulate",
            "The Badshahi Mosque in Lahore (1671) — the largest Mughal mosque, built by Aurangzeb — was directly inspired by the Jama Masjid, expanding its scale while maintaining the same architectural vocabulary",
            "The mosque's role in the 1857 First War of Indian Independence — Bahadur Shah Zafar's last sermon, British occupation — made it a symbol of the transition from Mughal imperial rule to British colonial domination and subsequently a focal point of Indian Muslim identity",
            "The holding of the Prophet's relics — a hair, a sandal, a verse in his handwriting — makes the Jama Masjid a pilgrimage destination within the South Asian Muslim community, adding a relic tradition to the mosque's imperial and communal functions"
        ],
        "relationships": [
            {"entity": "Emperor Shah Jahan (Mughal Empire)", "relationship": "COMMISSIONED_BY", "note": "Shah Jahan built the Jama Masjid (1644–1656) — the largest mosque in India — as the Friday mosque of his new capital Shahjahanabad"},
            {"entity": "Red Fort (Lal Qila), Delhi", "relationship": "TWIN_CIVIC_MONUMENT_WITH", "note": "The Jama Masjid and Red Fort were built together as the paired civic monuments of Shahjahanabad — the Mughal imperial capital"},
            {"entity": "Badshahi Mosque (Lahore)", "relationship": "DIRECT_ARCHITECTURAL_MODEL_FOR", "note": "The Badshahi Mosque (1671) was directly inspired by the Jama Masjid — expanding its scale while maintaining the same architectural vocabulary"},
            {"entity": "Bahadur Shah Zafar (last Mughal Emperor)", "relationship": "SITE_OF_LAST_SERMON_BEFORE_EXILE_OF", "note": "Bahadur Shah Zafar's last sermon at the Jama Masjid before the 1857 uprising made it a symbol of the end of Mughal imperial authority"},
            {"entity": "Prophet Muhammad's relics (hair, sandal, verse)", "relationship": "HOUSES_RELICS_OF", "note": "The mosque holds a hair, sandal, and handwritten verse of the Prophet — making it a pilgrimage destination within South Asian Islam"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 22 — {len(ENTITIES)} entities (Class 342: Famous Mosques — South Asia, West Africa, Persia, Maghreb)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
