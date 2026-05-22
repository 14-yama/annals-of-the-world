#!/usr/bin/env python3
"""
Batch 25 — 8 entities (Class 343): Ancient & Sacred Temples — Greece, Rome, Nepal, Japan, Italy
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

    ("swayambhunath", {
        "summary": (
            "Swayambhunath (स्वयम्भूनाथ, the Self-Arisen Lord, Monkey Temple, est. traditionally 5th century CE — archaeological evidence suggests 3rd–5th century BCE) in Kathmandu, Nepal, is the most sacred Buddhist stupa in Nepal — a hilltop complex dominated by a great white dome and golden tower, with the eyes of the Buddha painted on all four sides of the tower watching over the Kathmandu Valley. It is one of the oldest religious sites in Nepal, predating the Hindu-Buddhist synthesis of the Valley's culture, and is sacred to both Buddhists and Hindus.\n\n"
            "The stupa's great white hemisphere (anda) represents the world — the dome of the sky, the cosmic egg of creation — and the gilded four-sided tower above it is painted with the all-seeing eyes of the Buddha on each face, watching the four cardinal directions. The complex includes shrines to both Buddhist and Hindu deities — Hariti (smallpox goddess), Vajrayogini, and the Pancha Buddhas — reflecting the syncretic religious culture of the Kathmandu Valley, where Buddhist and Hindu devotion have coexisted for more than a millennium.\n\n"
            "Swayambhunath was heavily damaged in the 2015 Nepal earthquake but has been partially restored. The resident troop of rhesus macaques — which inhabit the complex and give it the English nickname 'Monkey Temple' — are considered sacred descendants of lice picked from the head of Manjushri, the bodhisattva of wisdom who is said to have cut the valley's drainage with his sword. The stupa is a UNESCO World Heritage Site as part of the Kathmandu Valley inscription (1979)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most sacred Buddhist stupa in Nepal (est. traditionally 5th century CE, archaeological evidence 3rd–5th century BCE); all-seeing Buddha eyes on golden tower watching four cardinal directions; syncretic Buddhist-Hindu sacred complex; UNESCO World Heritage (Kathmandu Valley, 1979); damaged in 2015 earthquake; sacred monkeys (descendants of Manjushri's lice); Kathmandu Valley's oldest religious site.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Kathmandu Valley's extraordinarily fertile position — a former lake drained, according to legend, by the bodhisattva Manjushri — created an ancient centre of population and religious culture in which Buddhist stupa-building began in the earliest centuries of the Common Era",
            "The syncretic religious culture of the Kathmandu Valley — where Buddhist and Hindu traditions coexisted within a single ritual community — drove the development of Swayambhunath as a multi-denominational sacred site incorporating both Buddhist and Hindu shrines",
            "The Licchavi dynasty's patronage of Buddhist sacred sites in the Kathmandu Valley (4th–9th centuries CE) — creating endowments for Swayambhunath and related stupas — established the institutional basis for the stupa's maintenance across 1,500+ years of continuous religious use"
        ],
        "effects": [
            "Swayambhunath's all-seeing Buddha eyes — painting the stupa's tower with four pairs of eyes watching the cardinal directions — became the defining visual icon of Nepalese Buddhist art, reproduced on thousands of objects and adopted as the symbol of Nepal in international visual culture",
            "The stupa's sacred monkey population — maintained by the religious community as descendants of Manjushri — created one of the first examples of sacred animal protection at a religious site, anticipating the concept of wildlife sanctuaries embedded within religious culture",
            "The 2015 Nepal earthquake's damage to Swayambhunath — and the subsequent international fundraising and restoration effort — made the stupa a symbol of Nepalese cultural resilience and the international responsibility for protecting UNESCO World Heritage sites from natural disaster",
            "The Kathmandu Valley's UNESCO World Heritage inscription (1979) — covering seven monument zones including Swayambhunath — established Nepal as one of the earliest Asian countries to achieve international recognition for its extraordinary concentration of religious architecture"
        ],
        "relationships": [
            {"entity": "Kathmandu Valley (Nepal)", "relationship": "HILLTOP_LANDMARK_ABOVE_THE", "note": "Swayambhunath's hilltop position — overlooking the Kathmandu Valley — makes its golden tower and Buddha eyes visible from across the valley"},
            {"entity": "UNESCO World Heritage (Kathmandu Valley, 1979)", "relationship": "INSCRIBED_AS_PART_OF", "note": "Swayambhunath is one of seven monument zones in the Kathmandu Valley UNESCO World Heritage inscription (1979)"},
            {"entity": "Bodhisattva Manjushri (Buddhist mythology)", "relationship": "CONNECTED_THROUGH_LEGEND_TO", "note": "The Kathmandu Valley's formation — and the sacred monkeys of Swayambhunath — are attributed in Buddhist legend to the bodhisattva Manjushri"},
            {"entity": "Nepal 2015 earthquake", "relationship": "DAMAGED_AND_SUBSEQUENTLY_RESTORED_AFTER", "note": "The 2015 earthquake damaged significant parts of Swayambhunath — prompting international restoration efforts"},
            {"entity": "Buddhist-Hindu syncretism (Kathmandu Valley)", "relationship": "SUPREME_EXAMPLE_OF", "note": "Swayambhunath's combined Buddhist and Hindu shrines reflect the unique syncretic religious culture of the Kathmandu Valley"}
        ],
    }),

    ("temple-of-athena-nike", {
        "summary": (
            "The Temple of Athena Nike (Ναός Ἀθηνᾶς Νίκης, Temple of Athena Victorious, est. c.427–421 BCE) on the Acropolis of Athens, Greece, is the smallest classical temple on the Athenian Acropolis — a tiny Ionic tetrastyle temple (8.27 × 5.44 metres) built at the highest and most prominent point of the Acropolis bastion, jutting out over the cliff to command the approach to the Propylaea. Despite its small scale, it is one of the most perfect and technically refined temples of the classical period.\n\n"
            "The temple was built during the Periclean building programme on the Athenian Acropolis (which also produced the Parthenon and the Erechtheion) to house the ancient cult image of Athena Nike — the goddess of victory in war, represented without wings (Athena Apteros) to prevent her fleeing Athens. The frieze that ran around all four sides of the temple — of which significant sections survive — depicted battles between Greeks and Persians (south frieze) and Greeks and Greeks (north, west, east friezes), celebrating Athenian military victories.\n\n"
            "The temple was dismantled by the Ottomans (1686) to build a gun emplacement during the Great Turkish War, and the stones were used to build a bastion at the entrance to the Acropolis. The temple was reconstructed twice: once in 1836–1842 using the original blocks found in the Ottoman bastion, and again in 1936–1940 and 1998–2010 when repeated dismantling and reassembly corrected earlier errors, making it one of the most studied examples of 19th–20th century archaeological reconstruction."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Smallest and most technically refined classical temple on Athenian Acropolis (est. c.427–421 BCE); Ionic tetrastyle at highest point of Acropolis bastion; Athena Apteros (wingless) cult — goddess kept wingless to prevent her fleeing Athens; frieze depicts battles against Persians and Greeks; dismantled by Ottomans (1686) for gun emplacement; reconstructed 1836–2010; part of Periclean building programme.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Periclean building programme (c.450–400 BCE) — transforming the Athenian Acropolis into the supreme expression of Athenian power and artistic achievement after the Persian Wars — included the Temple of Athena Nike as the first building on the Acropolis to be completed, preceding the Parthenon",
            "The ancient cult of Athena Apteros (wingless Athena) at the Acropolis bastion — whose wooden cult image was traditionally kept without wings to prevent her abandoning Athens — drove the temple's construction on the most prominent point of the Acropolis where the cult had been practiced for centuries",
            "The military friezes commissioned for the temple — depicting Greek victories over Persians at Marathon and Plataea — reflected the Athenians' desire to celebrate their military successes at the most visible point of the Acropolis, where approaching visitors would see the celebration of Athenian power before entering through the Propylaea"
        ],
        "effects": [
            "The Temple of Athena Nike's Ionic order — the smallest and most elegant of the three Greek orders — influenced the subsequent development of Ionic temple design in the Roman world, with its delicate proportions and refined entasis establishing a standard for Ionic refinement",
            "The temple's Ottoman dismantling (1686) and subsequent reconstruction (1836–2010) made it a foundational case study in the archaeology of restoration, establishing the principles of anastylosis (reassembly using original materials) that govern contemporary architectural heritage practice",
            "The temple's position on the Acropolis bastion — jutting over the cliff at the highest and most visible point of the hill — made it the architectural threshold between the secular world below and the sacred precinct above, its Nike imagery greeting every visitor with the promise of Athenian victory",
            "The Nike Apteros tradition — keeping the goddess of victory wingless to bind her to Athens — represents a fascinating example of ancient Greek religious anxiety about divine loyalty, the belief that the gods' continued favour required physical constraint as well as prayer"
        ],
        "relationships": [
            {"entity": "Athenian Acropolis (Periclean programme)", "relationship": "FIRST_COMPLETED_TEMPLE_IN_THE_PERICLEAN_PROGRAMME_OF", "note": "The Temple of Athena Nike was the first building of the Periclean Acropolis programme to be completed (c.427–421 BCE)"},
            {"entity": "Athena Nike (Athena Apteros — wingless goddess of victory)", "relationship": "HOUSES_CULT_OF", "note": "The temple housed the ancient wingless (Apteros) cult image of Athena Nike — kept wingless so the goddess could not abandon Athens"},
            {"entity": "Propylaea (entrance to Athenian Acropolis)", "relationship": "FRAMES_THE_APPROACH_TO_THE", "note": "The temple's position on the bastion at the entrance to the Acropolis made it the first building greeting visitors before the Propylaea"},
            {"entity": "Ottoman dismantling (1686) and modern anastylosis", "relationship": "FOUNDATIONAL_CASE_STUDY_IN", "note": "The temple's Ottoman dismantling and 1836–2010 reconstructions established anastylosis as the standard method for reconstructing ancient buildings"},
            {"entity": "Battle of Plataea (479 BCE)", "relationship": "MILITARY_VICTORIES_CELEBRATED_ON_FRIEZE_OF", "note": "The temple's south frieze depicted Greek victories over Persians — celebrating Athens' role in defeating the Persian invasions"}
        ],
    }),

    ("temple-of-hera-olympia", {
        "summary": (
            "The Temple of Hera at Olympia (Ἡραῖον, Heraion, est. c.590 BCE) in Olympia, Greece, is the oldest standing Greek temple — built more than a century before the Parthenon — and the most historically important panhellenic sanctuary after Delphi. The temple was the religious centrepiece of the sanctuary of Olympia, where the Olympic Games were held every four years from 776 BCE until their suppression by the Christian emperor Theodosius I in 393 CE. The eternal flame that is lit at the Heraion for each modern Olympic Games — in the ceremony conducted by women dressed as priestesses of Hera — makes the ancient temple a living source of one of the world's great sporting traditions.\n\n"
            "The temple's original columns were wooden, replaced one by one in stone as the original timber rotted — a process that happened over such a long period that the replacements represent every phase of Doric column design from the 6th to the 2nd centuries BCE, making the ruined colonnade a museum of the evolution of the Doric order. The great chryselephantine statue of Hera — one of the largest cult statues in ancient Greece — once dominated the temple's interior; the famous statue of Hermes by Praxiteles (c.330 BCE) was also found within the temple.\n\n"
            "The temple is now a field of fallen columns — toppled by earthquakes in the medieval period — but remains one of the most powerfully evocative ancient Greek sites, its stone drums lying in the grass of the sanctuary that still holds the altar where the Olympic flame ceremony is conducted every four years."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest standing Greek temple (est. c.590 BCE); predates Parthenon by 150 years; religious centrepiece of Olympia — site of Olympic Games from 776 BCE to 393 CE; Olympic flame ceremony conducted at the Heraion ruins for each modern Games; original wooden columns replaced in stone over centuries — museum of Doric order evolution; Hermes by Praxiteles found here.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Olympia's status as the primary panhellenic religious sanctuary — where all the major Greek city-states gathered every four years regardless of political conflicts for the Olympic Games — drove the construction of the earliest major stone temple in Greece, establishing the panhellenic character of the sanctuary",
            "The ancient wooden cult image of Hera — one of the oldest cult statues in Greece — required a permanent temple structure to house it, creating the Heraion as the sacred enclosure for the goddess who was the primary deity of Olympia before Zeus",
            "The transition from wooden to stone column construction in Greek sacred architecture (the 'petrification' of Greek temples, c.700–550 BCE) is perfectly illustrated at the Heraion, where the original wooden columns were replaced in stone over 400 years, creating the complete record of Doric evolution"
        ],
        "effects": [
            "The Heraion's role as the site of the Olympic flame lighting ceremony for the modern Olympic Games — established by the International Olympic Committee in 1936 and continued at every subsequent Games — makes the ancient temple a living source of the global sporting tradition, creating an unbroken symbolic connection from 776 BCE to the present",
            "The temple's archaeological history — wood columns replaced by stone over 400 years, preserving every phase of Doric design — made it one of the foundational sites of classical archaeology, establishing the stratigraphic method for dating Greek temples by their column proportions",
            "The discovery of the Hermes and the Infant Dionysus by Praxiteles (c.330 BCE) within the Heraion — now in the Olympia Museum — provided one of the few works attributed with certainty to a named ancient Greek sculptor, making the temple the archaeological context for the most celebrated ancient Greek marble sculpture",
            "The suppression of the Olympic Games by Theodosius I (393 CE) — ending 1,169 years of continuous Games held at the sanctuary of Olympia — and the abandonment of the Heraion marked the triumph of Christianity over pagan religious practice in the Roman Empire"
        ],
        "relationships": [
            {"entity": "Olympic Games (ancient, 776 BCE–393 CE)", "relationship": "PRINCIPAL_SANCTUARY_TEMPLE_FOR_THE", "note": "The Heraion was the oldest and most sacred temple at Olympia — the sanctuary where the Olympic Games were held for 1,169 years"},
            {"entity": "Modern Olympic Games (flame ceremony)", "relationship": "SITE_OF_FLAME-LIGHTING_CEREMONY_FOR_THE", "note": "The Olympic flame is lit at the Heraion ruins in each modern Olympic year — creating a living connection between the ancient sanctuary and the contemporary Games"},
            {"entity": "Hermes by Praxiteles (c.330 BCE)", "relationship": "ARCHAEOLOGICAL_FINDSPOT_OF_THE", "note": "The Hermes and Infant Dionysus — the most celebrated surviving Greek marble sculpture — was found within the Heraion"},
            {"entity": "Doric order (evolution of)", "relationship": "COMPLETE_MUSEUM_OF_THE", "note": "Original wooden columns replaced in stone over 400 years — making the colonnade a complete record of Doric order evolution from 590 to 200 BCE"},
            {"entity": "Theodosius I (suppression of Olympic Games, 393 CE)", "relationship": "SANCTUARY_ABANDONED_FOLLOWING_DECREE_OF", "note": "Theodosius I's suppression of the Games (393 CE) ended 1,169 years of Olympic history and led to the abandonment of the Olympia sanctuary"}
        ],
    }),

    ("temple-of-saturn", {
        "summary": (
            "The Temple of Saturn (Templum Saturni, est. traditionally 498 BCE — earliest parts of current visible structure 42 BCE, extensively rebuilt 283 CE) in the Roman Forum, Rome, is the oldest surviving monument in the Forum Romanum — eight grey granite columns standing in ruins against the sky, representing the eternal image of Roman antiquity. The temple was one of the oldest in Rome, dedicated to Saturn (the god of time, harvest, and the golden age before civilization's decline), and served for most of its history as the Roman state treasury (aerarium Saturni), holding the gold and silver reserves of the Republic.\n\n"
            "The temple's role as the aerarium — the treasury of the Roman state — made it the physical embodiment of Roman fiscal power: the public financial accounts were kept here, the standards of the legions were stored here during peacetime, and its strong rooms held the gold that funded Rome's wars. The temple's consecration festival (Saturnalia, 17 December) — the most popular Roman holiday, during which social hierarchies were suspended, gifts exchanged, and slaves sat at table with their masters — was the ancient ancestor of Christmas and New Year's celebrations in Western culture.\n\n"
            "The eight columns visible today — all that survives of the original temple — represent the most photographed image of ancient Rome after the Colosseum. The temple was rebuilt for the last time in 283 CE after a fire, giving the current columns their late antique form. The Forum's ruin — abandoned for grazing cattle in the medieval period and named the 'Campo Vaccino' (cow field) — and its subsequent archaeological excavation (18th–20th century) make it the defining site for the modern understanding of ancient Rome."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest surviving monument in the Roman Forum (est. 498 BCE; current columns 42 BCE and 283 CE); Roman state treasury (aerarium Saturni) holding Rome's gold and silver reserves; Saturnalia festival (17 December) — ancestor of Christmas/New Year celebrations; social hierarchies suspended during Saturnalia; slaves sat with masters; eight surviving columns are most iconic image of Forum Romanum; Forum abandoned as 'cow field' in medieval period.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Saturn's status as one of the oldest Roman deities — predating the Etruscan and Greek religious influences that shaped the Roman Olympian pantheon — created the religious basis for a temple at the heart of the Forum Romanum, where Rome's earliest civic religion was practiced",
            "The identification of the temple with the aerarium (state treasury) — a function that may predate the formal temple structure — reflects the ancient association between religious sanctity and the protection of civic wealth, with the god's divine protection guaranteeing the security of the state's financial reserves",
            "The Saturnalia festival's popularity — a reversal of social order during the winter solstice period, when slaves were served by masters and social restrictions were suspended — reflected deep Roman cultural anxiety about slavery and social hierarchy, creating a ritual safety valve that was essential to social stability"
        ],
        "effects": [
            "The Saturnalia festival (17 December — one week in duration) — with its gifts, role reversals, and suspension of social hierarchy — was the primary cultural ancestor of Christmas gift-giving traditions, the twelve days of Christmas, and New Year's celebrations across Western culture",
            "The aerarium Saturni's function as the Roman state treasury — holding the gold and silver that funded Roman military campaigns — made the temple the financial heart of the Roman Republic and early Empire, the physical embodiment of Rome's fiscal power",
            "The Temple of Saturn's eight surviving columns — the most iconic image of the ruined Forum Romanum — became the defining visual symbol of Roman antiquity in European culture from the Renaissance onwards, appearing in countless paintings, prints, and travel engravings of 'the ruins of Rome'",
            "The Forum Romanum's transformation from the civic heart of Rome to the 'Campo Vaccino' (cow field) of the medieval period — grazed by cattle for a thousand years — and its subsequent archaeological excavation created the modern discipline of classical archaeology"
        ],
        "relationships": [
            {"entity": "Roman Forum (Forum Romanum)", "relationship": "OLDEST_SURVIVING_MONUMENT_OF_THE", "note": "The Temple of Saturn — traditionally est. 498 BCE — is the oldest surviving monument in the Forum Romanum"},
            {"entity": "Roman state treasury (aerarium Saturni)", "relationship": "HOUSED_THE", "note": "The temple served as the Roman state treasury — holding the gold, silver, and public accounts of the Republic and early Empire"},
            {"entity": "Saturnalia festival (17 December)", "relationship": "CONSECRATION_FESTIVAL_IS_THE", "note": "The Saturnalia — a week of gift-giving, role reversals, and social license — was the most popular Roman holiday and the cultural ancestor of Christmas"},
            {"entity": "Christmas and New Year's traditions (Western)", "relationship": "CULTURAL_ANCESTOR_OF", "note": "The Saturnalia's gifts, role reversals, and winter festival character are the primary cultural ancestors of Western Christmas and New Year's celebrations"},
            {"entity": "Classical archaeology (Forum Romanum excavations)", "relationship": "PRIMARY_SITE_FOR_THE_FORMATION_OF", "note": "The Forum's excavation — from the 'Campo Vaccino' medieval cow field to the modern archaeological park — created the modern discipline of classical archaeology"}
        ],
    }),

    ("atsuta-jingy\u016b", {
        "summary": (
            "Atsuta Jingū (熱田神宮, Atsuta Grand Shrine, est. traditionally 113 CE) in Nagoya, Japan, is the second most important Shinto shrine in Japan after Ise Grand Shrine — and the most sacred site associated with the three imperial treasures of Japan. Atsuta Jingū enshrines the Kusanagi-no-Tsurugi (草薙の剣, Grass-Cutting Sword) — one of Japan's three imperial treasures (along with the Yata no Kagami mirror and the Yasakani no Magatama jewel) — which according to Shinto tradition was found in the tail of the eight-headed serpent Yamata no Orochi by the storm god Susanoo.\n\n"
            "The shrine's wooded grounds — 6.2 hectares of ancient camphor and cypress trees in the heart of Nagoya — preserve a sacred forest within the modern city, creating one of the most striking contrasts in Japan between ancient natural sanctuary and contemporary urban environment. More than nine million visitors make the traditional New Year's visit (hatsumode) to Atsuta Jingū each year — the third highest number of any Japanese shrine or temple after the Meiji Shrine (Tokyo) and Naritasan Shinshoji Temple (Narita).\n\n"
            "The Kusanagi sword is never displayed publicly — its existence can be verified only indirectly through imperial ritual — making Atsuta Jingū a shrine whose supreme sacred object is permanently invisible. This tradition of aniconic concealment — the divine hidden from public view — reflects the deepest level of Shinto sacred practice, where proximity to the deity is expressed through ritual distance rather than visual representation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Second most important Shinto shrine in Japan (est. traditionally 113 CE); enshrines Kusanagi-no-Tsurugi — one of three Japanese imperial treasures (sword found in Yamata no Orochi's tail); 9 million New Year's visitors annually; 6.2 hectares of ancient forest in Nagoya; Kusanagi sword permanently concealed — never displayed publicly; aniconic sacred tradition.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The mythological story of the Kusanagi sword — found by the storm god Susanoo in the tail of the eight-headed serpent, given to the sun goddess Amaterasu, and eventually passed to the imperial line through the legendary hero Yamato Takeru — created the theological basis for the shrine's extraordinary sacred importance as the repository of a divine imperial treasure",
            "The imperial household's association with the three sacred treasures (sanshu no jingi) — the sword, mirror, and jewel representing valor, wisdom, and benevolence — created the political basis for the shrine's central role in legitimating the imperial line",
            "Nagoya's position as the capital of the powerful Owari domain — and later as one of Japan's major industrial cities — provided the economic base and population density that made Atsuta Jingū the focus of one of Japan's largest New Year's pilgrimage traditions"
        ],
        "effects": [
            "Atsuta Jingū's enshrinement of the Kusanagi sword — one of the three symbols of Japanese imperial authority — makes the shrine a foundational site of the legitimacy of the Japanese imperial institution, whose continuity depends in part on the sacred relationship with the three treasures",
            "The shrine's annual New Year's hatsumode (nine million visitors) maintains Atsuta Jingū as one of the three primary focal points of Japan's most widely observed annual religious ritual — the first shrine visit of the new year — alongside Meiji Shrine and Naritasan",
            "The ancient camphor trees of Atsuta Jingū's forest — some estimated to be over a thousand years old — create an urban sacred grove in Nagoya that has been protected by religious prohibition from the city's development, preserving an ancient landscape within a modern industrial city",
            "The tradition of permanently concealing the Kusanagi sword — so that no modern person has ever verified its physical existence — represents the extreme form of aniconic sacred practice, creating a theological tradition where the most sacred object is defined by its absolute invisibility"
        ],
        "relationships": [
            {"entity": "Kusanagi-no-Tsurugi (imperial sword treasure)", "relationship": "ENSHRINES_THE", "note": "Atsuta Jingū enshrines the Kusanagi sword — one of the three Japanese imperial treasures — which is permanently concealed and never displayed publicly"},
            {"entity": "Japanese Imperial House", "relationship": "SACRED_REPOSITORY_OF_IMPERIAL_REGALIA_OF_THE", "note": "The shrine's enshrinement of the Kusanagi sword makes it a foundational site of Japanese imperial legitimacy"},
            {"entity": "Ise Grand Shrine", "relationship": "SECOND_MOST_IMPORTANT_SHRINE_AFTER_THE", "note": "Atsuta Jingū is the second most important Shinto shrine in Japan after Ise Grand Shrine — the primary sanctuary of the sun goddess Amaterasu"},
            {"entity": "Shinto aniconic tradition (concealment of the divine)", "relationship": "SUPREME_EXAMPLE_OF", "note": "The permanent concealment of the Kusanagi sword — never displayed, verified only through ritual — represents the deepest level of Shinto sacred practice"},
            {"entity": "Japanese New Year (hatsumode pilgrimage)", "relationship": "THIRD_MOST_VISITED_SITE_DURING", "note": "Nine million visitors make the New Year's hatsumode visit to Atsuta Jingū — the third highest of any Japanese shrine or temple"}
        ],
    }),

    ("asakusa-shrine", {
        "summary": (
            "Asakusa Shrine (浅草神社, Asakusa Jinja, also known as Sanja-sama, est. 628 CE) in Asakusa, Tokyo, Japan, is the shrine enshrining the three men who founded the Senso-ji Temple complex — the most visited religious site in Japan (annually 30 million visitors) — and the site of the Sanja Matsuri (三社祭, Three Shrine Festival), which is the most famous and raucous festival in Tokyo, held each May and attracting 1.8 million spectators over three days. Asakusa Shrine and Senso-ji Temple form the most celebrated religious complex in Tokyo.\n\n"
            "The shrine was founded to honour Hinokuma Hamanari, Hinokuma Takenari, and Hajino Matsuchi — two fishermen brothers and their patron who, in 628 CE, discovered a golden image of Kannon (the bodhisattva of compassion) in their fishing nets in the Sumida River and enshrined it, founding what would become Senso-ji. The shrine thus embodies the characteristic Japanese phenomenon of jingū-ji (shrines and temples co-located) — Shinto and Buddhist practice coexisting at a single sacred site.\n\n"
            "The Sanja Matsuri — with its three massive portable shrines (mikoshi) carried by thousands of participants through the streets of Asakusa — is the defining cultural event of the shitamachi (old downtown) culture of Tokyo's east side. The festival's participants include yakuza members tattooed with full-body irezumi designs, whose visible participation in the public religious ritual is one of the most striking examples of the intersection of criminal subculture and mainstream religious tradition."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Shrine at heart of Japan's most visited religious site — Senso-ji complex (30 million annual visitors, est. 628 CE); enshrines three founders of Senso-ji; Sanja Matsuri (Three Shrine Festival) — Tokyo's most famous festival, 1.8 million spectators over 3 days; exemplifies Japanese jingū-ji (Shinto-Buddhist co-location); yakuza irezumi (full-body tattoo) tradition visible at Sanja Matsuri.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The legendary founding story of Senso-ji (628 CE) — two fishermen discovering a golden Kannon image in their nets — created the mythological narrative that generated both the temple and the shrine to the founders, establishing the sacred character of the Asakusa site that has drawn pilgrims for 1,400 years",
            "The Tokugawa shogunate's development of Edo (now Tokyo) as the seat of Japanese government (from 1603) — and Asakusa's position as the principal entertainment and religious district at the eastern edge of the city — created the urban context that made Senso-ji and Asakusa Shrine the primary religious destinations of the new capital",
            "The shitamachi culture of Edo-period Tokyo — the artisan and merchant culture of the city's east side, distinct from the samurai culture of the west side — generated the vibrant popular religious culture (festivals, pilgrimages, theatrical events) centred on Senso-ji and Asakusa Shrine"
        ],
        "effects": [
            "The Senso-ji/Asakusa Shrine complex — 30 million annual visitors — is the most visited religious site in Japan and one of the most visited religious sites in the world, making Asakusa the primary destination for international tourists to Tokyo seeking traditional Japanese religious experience",
            "The Sanja Matsuri — with its three massive mikoshi (portable shrines) carried through Asakusa's streets by thousands of participants — is the defining event of Tokyo's traditional festival calendar and the most visually spectacular manifestation of Tokyo's shitamachi popular culture",
            "The festival's yakuza participation — full-body irezumi (tattoo) designs displayed during the Sanja Matsuri's summer heat — created the international association between Japanese tattooing and the yakuza, making the Asakusa festival a formative site in the global cultural understanding of Japanese body art",
            "The jingū-ji model — Shinto shrine and Buddhist temple coexisting at a single sacred site — embodies the syncretic religious tradition of Japan before the Meiji government's forced separation of Shinto and Buddhism (1868), making Asakusa Shrine a living witness to pre-Meiji Japanese religious culture"
        ],
        "relationships": [
            {"entity": "Senso-ji Temple (Asakusa, Tokyo)", "relationship": "SHRINE_AT_HEART_OF_THE", "note": "Asakusa Shrine enshrines the three founders of Senso-ji Temple — forming with the temple the most celebrated religious complex in Tokyo"},
            {"entity": "Sanja Matsuri (Three Shrine Festival)", "relationship": "DEFINES_THE_IDENTITY_OF_THROUGH", "note": "The Sanja Matsuri — 1.8 million spectators, three massive mikoshi — is the defining event of Asakusa and Tokyo's most famous popular festival"},
            {"entity": "Shitamachi culture of Tokyo (Edo period)", "relationship": "RELIGIOUS_CENTRE_OF_THE", "note": "Asakusa Shrine and Senso-ji are the spiritual heart of Tokyo's shitamachi (old downtown) popular culture"},
            {"entity": "Yakuza irezumi (full-body tattoo tradition)", "relationship": "PUBLIC_DISPLAY_FORUM_FOR", "note": "Yakuza full-body tattoos are displayed during the Sanja Matsuri — creating the international association between Japanese tattooing and the festival"},
            {"entity": "Japanese jingū-ji tradition (Shinto-Buddhist co-location)", "relationship": "LIVING_EXAMPLE_OF_PRE-MEIJI", "note": "The shrine-temple coexistence at Asakusa embodies pre-Meiji Japanese syncretic religious culture — before the 1868 separation of Shinto and Buddhism"}
        ],
    }),

    ("basilica-of-st-anthony-of-padua", {
        "summary": (
            "The Basilica of Saint Anthony of Padua (Basilica di Sant'Antonio di Padova, 'il Santo', est. 1232–1310 CE) in Padua, Italy, is one of the most visited pilgrimage sites in the Christian world — with approximately 5–6 million pilgrims annually — and the shrine of Saint Anthony of Padua (1195–1231), the patron saint of lost items, travellers, and the poor, who is one of the most beloved and widely invoked saints in Catholicism. The basilica is a masterpiece of Romanesque-Gothic-Byzantine architecture, with eight domes, two towers, and a profile that combines Italian Gothic with Byzantine cupola forms.\n\n"
            "Saint Anthony — a Franciscan friar born in Lisbon (Portugal) who spent his ministry in northern Italy — died in Padua in 1231 and was canonised within a year (1232), the fastest canonisation in Catholic history. The basilica was begun the year of his canonisation, marking the extraordinary speed with which his cult spread across medieval Europe. The interior houses Donatello's celebrated bronze reliefs and statues (1443–1450) — including the bronze equestrian statue of Gattamelata (outside) and the high altar's bronze reliefs depicting miracles of Saint Anthony — which are among the greatest works of Renaissance sculpture.\n\n"
            "The chapel of the Arca del Santo — where Anthony's body is enshrined — is the focus of the pilgrimage, with an annual stream of devotees touching the marble sarcophagus and praying for the recovery of lost people and objects. Anthony of Padua's global reach — with shrines, churches, and hospitals named after him on every continent — makes the Padua basilica the focal point of a worldwide devotional network."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "One of most visited pilgrimage sites in Christian world (est. 1232–1310 CE); 5–6 million pilgrims annually; shrine of Saint Anthony of Padua — patron saint of lost items; canonised 1232, one year after death — fastest canonisation in Catholic history; Donatello's bronze high altar reliefs and equestrian Gattamelata (Renaissance masterpiece); Romanesque-Gothic-Byzantine architecture with 8 domes.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Saint Anthony's canonisation within one year of his death (1232) — driven by widespread popular devotion and the extraordinary number of miracles attributed to him — created the theological and popular demand for a basilica commensurate with his immense cult",
            "Padua's position as a wealthy northern Italian city — with a flourishing university (est. 1222, one of the oldest in Europe) and a prosperous merchant class — provided the financial base for the construction of a large pilgrimage basilica",
            "The Franciscan order's institutional interest in promoting Anthony's cult — he was one of the most important early Franciscan theologians, whose ministry in Padua made him the embodiment of Franciscan preaching and pastoral charity — drove the construction of a basilica that would serve both pilgrimage and the Franciscan liturgical programme"
        ],
        "effects": [
            "The basilica's 5–6 million annual pilgrims make it one of the most continuously visited Christian pilgrimage sites in the world — its pilgrimage tradition unbroken since Anthony's canonisation in 1232, constituting 800 years of continuous pilgrimage culture",
            "Donatello's bronze works for the basilica (1443–1450) — the high altar's miracle reliefs and the equestrian Gattamelata outside — established Padua as a centre of Renaissance sculpture comparable to Florence, transforming the pilgrimage city into a venue for the highest artistic achievement",
            "Anthony of Padua's invocation for 'lost items' — the most widely practised form of private Catholic devotion worldwide — generates a global devotional network centred on the Padua basilica, with Saint Anthony chapels in virtually every Catholic church in the world",
            "The basilica's extraordinary architectural form — 8 domes, Romanesque-Gothic-Byzantine synthesis — influenced the subsequent development of pilgrimage church architecture in northern Italy, creating a precedent for multi-domed basilica design that shaped several subsequent pilgrimage buildings"
        ],
        "relationships": [
            {"entity": "Saint Anthony of Padua (1195–1231)", "relationship": "PRIMARY_SHRINE_OF", "note": "The basilica enshrines Saint Anthony — patron saint of lost items — canonised 1232 (one year after death) in the fastest canonisation in Catholic history"},
            {"entity": "Franciscan Order", "relationship": "OWNED_AND_OPERATED_BY_THE", "note": "The basilica is the principal Franciscan church in Italy — built to house the cult of the most beloved early Franciscan preacher"},
            {"entity": "Donatello (sculptor, 1386–1466)", "relationship": "GREATEST_ARTISTIC_COMMISSION_OF_THE", "note": "Donatello's bronze high altar reliefs (1443–1450) and the Gattamelata equestrian statue are among the greatest works of Renaissance sculpture"},
            {"entity": "Padua (Università di Padova, est. 1222)", "relationship": "PILGRIMAGE_COMPLEMENT_TO_THE_UNIVERSITY_OF", "note": "Padua's combination of one of the oldest European universities (1222) and Italy's most visited pilgrimage church made it one of the most important medieval cities in Italy"},
            {"entity": "Global Catholic devotional network (Saint Anthony chapels)", "relationship": "FOCAL_POINT_OF_THE", "note": "Anthony's global invocation for lost items — with shrines on every continent — makes the Padua basilica the centre of a worldwide Catholic devotional tradition"}
        ],
    }),

    ("temple-of-apollo-sosianus", {
        "summary": (
            "The Temple of Apollo Sosianus (Templum Apollinis Sosianum, est. originally c.430 BCE — rebuilt by Gaius Sosius, 34–20 BCE) in Rome, Italy, is one of the most significant Republican-era temples in Rome — located in the Area Sacra of Largo Argentina, near the Theatre of Marcellus — and one of the best-preserved examples of Republican Roman temple architecture. Three of the original Corinthian columns stand in situ, rising dramatically from the excavated level of ancient Rome several metres below the modern street level.\n\n"
            "The temple was originally built by the consul Gnaeus Julius Mento (c.430 BCE) in fulfilment of a vow to Apollo during a Roman plague, and was rebuilt on a grand scale by Gaius Sosius — one of Mark Antony's generals — following his triumph from Judaea in 34 BCE. Sosius adorned the temple with works of art plundered from Greece and Asia Minor, including the famous sculptural group (Apollo, Artemis, and Latona) found in its vicinity that is now in the Capitoline Museum. The temple's location near the Theatre of Marcellus — in the densely sacred and theatrical area of the Campus Martius — made it part of the most important complex of Republican sacred buildings in Rome.\n\n"
            "The three surviving columns and entablature fragment of the Temple of Apollo Sosianus are the most visible ancient Roman monument in the densely occupied area of Rome between the Jewish Ghetto and the Tiber, rising as a dramatic ancient presence within the medieval and Renaissance urban fabric."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "One of best-preserved Republican-era temples in Rome (est. c.430 BCE; rebuilt 34–20 BCE); three standing Corinthian columns rising from excavated level; founded in fulfilment of plague vow to Apollo; rebuilt by Gaius Sosius (Mark Antony's general) following triumph from Judaea (34 BCE); plundered Greek art including Apollo, Artemis, Latona group now in Capitoline Museum; part of Campus Martius Republican sacred complex.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Roman plague of c.430 BCE — and the consul Gnaeus Julius Mento's vow to Apollo for the city's preservation — created the original theological obligation for a temple to Apollo in the Campus Martius, establishing the sacred site that would be elaborated over the following five centuries",
            "Gaius Sosius's desire to commemorate his triumph from Judaea (34 BCE) — and his political alliance with Mark Antony against Octavian — drove the grand rebuilding of the temple as a monument of military success and political ambition in the final years of the Roman Republic",
            "Apollo's growing importance in Roman religion — culminating in his adoption as the divine patron of Augustus Caesar, who built the Temple of Apollo on the Palatine Hill (28 BCE) — created an intense period of Apollo temple building in the late Republic and early Empire"
        ],
        "effects": [
            "The Temple of Apollo Sosianus's sculptural programme — works of art plundered from Greece and Asia Minor and displayed in the temple — established the Roman cultural pattern of transforming conquered culture's art into a display of Roman imperial power",
            "The three surviving Corinthian columns of the Sosianus temple — rising from the excavated level of ancient Rome several metres below the modern street — became one of the defining images of Roman archaeological layering, expressing the temporal depth of the city's built history",
            "The temple's location near the Theatre of Marcellus — in the densely sacred Campus Martius — contributed to the concentration of Republican sacred buildings that defined Roman religious life in the late Republic, creating the model for the imperial building programmes that replaced Republican piety with imperial spectacle",
            "The temple's plundered sculptural group (Apollo, Artemis, and Latona, now in the Capitoline Museum) represents the transfer of Greek artistic tradition to Rome that was the foundation of Roman art, making the Sosianus temple a key node in the artistic transmission from Greece to Rome"
        ],
        "relationships": [
            {"entity": "Gaius Sosius (general of Mark Antony)", "relationship": "REBUILT_IN_TRIUMPH_BY", "note": "Sosius rebuilt the temple (34–20 BCE) following his triumph from Judaea — a monument to military success and loyalty to Mark Antony"},
            {"entity": "Mark Antony (Roman general and politician)", "relationship": "POLITICAL_PATRON_CONTEXT_OF", "note": "Sosius rebuilt the temple as an ally of Mark Antony — making it a monument caught between the Republic's end and Augustus's triumph"},
            {"entity": "Apollo, Artemis, and Latona sculptural group (Capitoline Museum)", "relationship": "ORIGINAL_LOCATION_OF_PLUNDERED_GROUP", "note": "The sculptural group now in the Capitoline Museum was plundered from Greece or Asia Minor and displayed in the Sosianus temple"},
            {"entity": "Theatre of Marcellus (Campus Martius)", "relationship": "LOCATED_ADJACENT_TO_THE", "note": "The temple's location in the Campus Martius — near the Theatre of Marcellus — places it in the most important Republican sacred and theatrical complex in Rome"},
            {"entity": "Republican Roman sacred architecture", "relationship": "BEST-PRESERVED_EXAMPLE_OF", "note": "Three standing Corinthian columns make the Sosianus temple one of the most visible and best-preserved Republican-era temples in Rome"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 25 — {len(ENTITIES)} entities (Class 343: Ancient & Sacred Temples — Greece, Rome, Nepal, Japan, Italy)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
