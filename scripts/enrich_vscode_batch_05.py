#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 05 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: zai-yu, gonçalo-coelho, antiochus-chuzon, latin-america,
          americas, oceania, cristoforo-landino (already in 04 — skip if needed),
          (replaced with) vortimer, ammonius-grammaticus, orientius,
          jan-van-lannoy, abu-amra-kaysan
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-05-may2026"

ENRICHMENTS = {

"zai-yu": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210zai-yu.json",
  "slug": "zai-yu",
  "data": {
    "summary": "Zai Yu (宰予, c. 522–458 BCE), also known as Zai Wo, was one of Confucius's most intellectually challenging disciples — a figure remembered in the Analects less as a model student than as a provocateur whose pointed questions exposed the tensions and limits of Confucian orthodoxy. He belonged to Confucius's inner circle of ten distinguished students (the 'Ten Philosophers') and was recognised as the most gifted among them in the art of rhetoric and oration. Unlike the more deferential disciples who accepted Confucius's teachings, Zai Yu was known for direct argument and intellectual challenge — a style that drew Confucius's famous reproof when Zai Yu proposed shortening the three-year mourning period to one year: 'The Master said: If you feel no anxiety, then shorten it. The exemplary person in mourning finds no joy in food, no pleasure in music, no comfort in his dwelling — therefore he does not shorten it. If you feel no anxiety, then shorten it.'\n\nZai Yu's arguments anticipated debates that would become central to Confucian and Daoist philosophy. His questioning of the three-year mourning period was, at its core, a utilitarian challenge to tradition — asking whether ritual practice should be justified by its social function or followed as an intrinsic obligation regardless of subjective feeling. This tension between ritual form and moral feeling (li versus ren) remained one of the central axes of Confucian philosophical debate for centuries. The Analects record that Confucius also criticised Zai Yu for sleeping during the day — delivering the famous line: 'Rotten wood cannot be carved; a wall of dried dung cannot be trowelled. What is the use of my reproving him?'\n\nZai Yu is also recorded in the Zuo Zhuan as a diplomat who served in Qi. Despite the negative portrait in the Analects, his later reputation underwent significant rehabilitation: in 1 CE he was honoured with a posthumous title by Han Emperor Ping; he was later canonised as Duke of Qi in 739 CE by Tang Emperor Xuanzong and elevated to a senior position in the Confucian temple pantheon. His inclusion among the Ten Philosophers meant that he was reverenced in Confucian temples across East Asia for over two millennia.",
    "causes": [
      "Confucius's cultivation of a diverse group of disciples with different temperaments and intellectual approaches — some deferential, some challenging — created the philosophical community in which Zai Yu's argumentative style found expression and in which the tensions of Confucian thought became visible.",
      "The social instability of the Spring and Autumn Period (770–476 BCE), in which traditional Zhou ritual order was visibly breaking down under interstate competition, made questions about the proper relationship between ritual obligation and practical utility immediately relevant rather than merely academic.",
      "Zai Yu's rhetorical talent — acknowledged even by Confucius despite the criticism — gave him the intellectual standing to raise arguments that other disciples would not dare to formulate."
    ],
    "effects": [
      "Zai Yu's challenges to Confucius's positions — recorded in the Analects — preserved a record of philosophical debate within the founding circle of Confucianism that revealed the tensions between ritual form (li) and human feeling (ren) at the heart of the tradition.",
      "His posthumous canonisation and inclusion in the Confucian temple pantheon meant that his image was worshipped in Confucian temples across China, Korea, Japan, and Vietnam for over two thousand years — a remarkable reversal of his generally critical portrait in the primary sources.",
      "The debate between Zai Yu and Confucius over the mourning period became a canonical reference point in East Asian ethical discussion of the relationship between ritual obligation, social function, and human feeling — cited in philosophical commentaries from the Han dynasty through the Neo-Confucian revival of the Song dynasty."
    ],
    "relationships": [
      {"sourceSlug": "confucius", "sourceName": "Confucius", "verb": "TEACHES", "targetSlug": "zai-yu", "targetName": "Zai Yu", "context": "Confucius taught Zai Yu as one of his ten distinguished disciples, though the Analects record several sharp rebukes of Zai Yu's intellectual challenges — most notably the mourning period debate."},
      {"sourceSlug": "zai-yu", "sourceName": "Zai Yu", "verb": "INFLUENCES", "targetSlug": "confucian-philosophy", "targetName": "Confucian Philosophy", "context": "Zai Yu's recorded challenges to Confucius on mourning duration and ritual obligation preserved the tensions within early Confucianism between ritual form and human feeling that became central to subsequent philosophical debate."},
      {"sourceSlug": "analects", "sourceName": "Analects of Confucius", "verb": "DOCUMENTS", "targetSlug": "zai-yu", "targetName": "Zai Yu", "context": "The Analects record several episodes featuring Zai Yu — including the mourning debate and the sleeping incident — providing the primary source for both his intellectual position and Confucius's critical responses."}
    ],
    "places": [
      {"name": "Lu, China (modern Shandong Province)", "role": "Home state of Confucius and the primary context for Zai Yu's education in the Confucian school"},
      {"name": "Qi, China (modern Shandong Province)", "role": "State where Zai Yu served as a diplomat according to the Zuo Zhuan — evidence of his practical political career beyond philosophical education"}
    ],
    "subjects": ["Confucianism", "Chinese Philosophy", "Classical China", "Classical Era", "Ethics", "Education", "Intellectual History", "Religion"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Zai Yu was one of Confucius's ten distinguished disciples — his recorded intellectual challenges to Confucius on the mourning period preserved a crucial debate about ritual versus human feeling that became central to Confucian philosophy. His posthumous canonisation placed his image in Confucian temples across East Asia for two millennia, making him a venerated figure in one of the world's most influential intellectual traditions.",
      "significanceCategory": "regional"
    }
  }
},

"gonçalo-coelho": {
  "filepath": "data/appwrite-export/entities/290-Class-290/290gonçalo-coelho.json",
  "slug": "gonçalo-coelho",
  "data": {
    "summary": "Gonçalo Coelho (died c. 1512) was a Portuguese explorer and commander who led the two most significant Portuguese expeditions to Brazil in the first decade after its discovery, making him the primary figure responsible for establishing Portugal's systematic knowledge of the South American coast and for securing the early territorial claims that would develop into colonial Brazil. A royal official with previous experience in African coastal exploration, Coelho was chosen by King Manuel I to follow up Pedro Álvares Cabral's accidental contact with Brazil in 1500 with deliberate exploratory voyages that would map the coastline and assess its commercial and strategic potential.\n\nCoelho's first expedition (1501–1502) was scientifically and commercially remarkable. The voyage carried Amerigo Vespucci as a crew member and navigator, and it was the observations and letters from this voyage — particularly Vespucci's accounts — that established to European geographic consciousness that Brazil was part of a 'New World' rather than an Asian extension. The expedition systematically mapped approximately 2,500 kilometres of the Brazilian coastline from roughly modern Recife south to the Rio de la Plata region, assigned Portuguese place names to the landmarks they found (many still in use), and collected the brazilwood that gave the territory its enduring name. Coelho's second expedition (1503–1504) established the first permanent Portuguese trading posts in Brazil, founding what were arguably the earliest European settlements in South America.\n\nThough Gonçalo Coelho lacks the celebrity of Vasco da Gama or Cabral, his systematic mapping voyages were more consequential for the actual establishment of Brazilian Portugal than the initial 'discovery': they transformed a coastal contact into a territorial claim with known geography, commercial resources, and the beginning of a settler presence. He died around 1512, before the full colonial machinery that his voyages enabled was deployed.",
    "causes": [
      "Cabral's accidental contact with Brazil in 1500 — and the commercial value immediately attributed to its brazilwood — created the royal mandate for systematic follow-up exploration, which Coelho was appointed to lead as the appropriate combination of naval experience and administrative reliability.",
      "Portugal's Treaty of Tordesillas (1494) with Spain required Portugal to demonstrate effective occupation and knowledge of its South American hemisphere, giving Coelho's mapping voyages legal and diplomatic as well as commercial importance.",
      "Amerigo Vespucci's participation in Coelho's 1501–1502 voyage and his subsequent letters describing the Brazilian coast as a 'New World' transformed the geographic significance of Coelho's findings — it was Vespucci's interpretation of Coelho's voyage that reshaped European geographic consciousness."
    ],
    "effects": [
      "Coelho's 1501–1502 voyage, through Amerigo Vespucci's accounts, established that Brazil was part of a continental landmass distinct from Asia — the 'New World' concept that would eventually give two continents their name (America/Vespucci).",
      "His second expedition's trading posts (1503–1504) were the first permanent European settlements in South America, establishing the infrastructure from which Portuguese colonial Brazil would develop over the following century.",
      "The systematic place-name assignment during Coelho's voyages created much of Brazil's coastal geographic vocabulary — many names from his 1501–1502 expedition remain in use today, including Rio de Janeiro (River of January — named on his passage in January 1502)."
    ],
    "relationships": [
      {"sourceSlug": "gonçalo-coelho", "sourceName": "Gonçalo Coelho", "verb": "ENABLES", "targetSlug": "colonial-brazil", "targetName": "Colonial Brazil", "context": "Coelho's systematic mapping voyages (1501–1504) and his establishment of the first Portuguese trading posts transformed Cabral's accidental 'discovery' into the territorial foundation of colonial Brazil."},
      {"sourceSlug": "amerigo-vespucci", "sourceName": "Amerigo Vespucci", "verb": "OCCURS_IN", "targetSlug": "gonçalo-coelho", "targetName": "Gonçalo Coelho", "context": "Vespucci sailed with Coelho's 1501–1502 expedition and his account of the voyage established that Brazil was a 'New World' — the observation that eventually gave the Americas their name."},
      {"sourceSlug": "pedro-alvares-cabral", "sourceName": "Pedro Álvares Cabral", "verb": "PRECEDES", "targetSlug": "gonçalo-coelho", "targetName": "Gonçalo Coelho", "context": "Cabral's 1500 contact with Brazil was accidental and brief; Coelho's 1501 follow-up voyage was the first systematic exploration commissioned to assess what Cabral had found."},
      {"sourceSlug": "portuguese-empire", "sourceName": "Portuguese Empire", "verb": "SENDS", "targetSlug": "gonçalo-coelho", "targetName": "Gonçalo Coelho", "context": "King Manuel I of Portugal commissioned Coelho to map and assess the Brazilian coast — part of the systematic Portuguese programme of Atlantic expansion that built the first global empire."}
    ],
    "places": [
      {"name": "Brazil (South American Coast)", "role": "Primary destination of Coelho's voyages — 2,500 km of coastline mapped on the 1501–1502 expedition, establishing Portugal's territorial knowledge and claims"},
      {"name": "Lisbon, Portugal", "role": "Home port for Coelho's expeditions and base of King Manuel I's colonial programme"},
      {"name": "Rio de Janeiro, Brazil", "role": "Bay encountered by Coelho's fleet in January 1502 and named 'River of January' — one of many Brazilian place names originating from Coelho's mapping voyage"}
    ],
    "subjects": ["Age of Exploration", "Portuguese Empire", "Brazil", "Medieval Era", "Navigation", "Colonial History", "Atlantic World", "Geography"],
    "frameworks": ["WORLD_SYSTEMS", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Gonçalo Coelho led the two expeditions that transformed Brazil from an accidental contact into a known and claimed territory. His 1501–1502 voyage — with Amerigo Vespucci aboard — was the observation base for the 'New World' concept that gave the Americas their geographic identity. His 1503–1504 trading posts were the first permanent European settlements in South America.",
      "significanceCategory": "significant"
    }
  }
},

"antiochus-chuzon": {
  "filepath": "data/appwrite-export/entities/231-Class-231/231antiochus-chuzon.json",
  "slug": "antiochus-chuzon",
  "data": {
    "summary": "Antiochus Chuzon (fl. 5th century CE) was a Samaritan leader who led a major revolt against Byzantine imperial rule in Palestine around 484–486 CE — one of the most significant Samaritan uprisings in the late antique period and an episode that illustrates both the resilience of Samaritan religious identity under Christian Roman rule and the explosive intersection of taxation, religious coercion, and ethnic autonomy in the late imperial periphery. The Samaritans — the people of ancient Samaria who maintained a distinctive form of Israelite religion centred on Mount Gerizim rather than Jerusalem — had been the subject of increasing Christian imperial pressure since the reign of Constantine, as successive emperors converted Samaritan sacred sites to churches and restricted Samaritan religious practice.\n\nThe revolt under Antiochus Chuzon erupted when Byzantine imperial policy — probably involving the forced consecration of the Samaritan synagogue on Mount Gerizim as a church — passed the threshold of tolerance. Antiochus led his followers in armed resistance, reportedly appointing himself king or messianic leader of the Samaritans in an explicitly nationalist and religious framework. Byzantine forces under the command of the dux (military commander) of Palestine eventually suppressed the revolt with considerable violence, imposing additional restrictions on Samaritan religious practice and further reducing their legal standing in the empire. The rebellion was one of several Samaritan revolts in the 4th–7th centuries (the largest occurred in 529–530 and 556 CE) that together represent a sustained pattern of resistance to Christian imperial homogenisation.\n\nAntiochus Chuzon is a figure primarily known from brief references in Byzantine chronicles and anti-Samaritan polemical literature. His revolt contributed to the progressive deterioration of the Samaritan position in the Byzantine Empire — a pressure that ultimately made many Samaritans receptive to the Arab-Muslim conquest of Palestine in 636 CE, which offered greater religious tolerance than Christian Byzantine administration had provided.",
    "causes": [
      "Byzantine religious policy under Zeno (474–491 CE) increasingly moved to suppress non-Christian religious practice, converting sacred sites including the Samaritan sanctuary on Mount Gerizim to Christian use — a direct assault on Samaritan religious identity.",
      "The fiscal and legal disabilities imposed on Samaritans under Christian imperial law — including restrictions on inheritance, testamentary rights, and public office — created material grievances that amplified the religious motivations for revolt.",
      "The Samaritan tradition of messianic expectation — that a restorer figure would re-establish Samaritan sovereignty and rebuild the sanctuary on Mount Gerizim — provided the ideological framework within which Antiochus could mobilise his followers around a nationalist-religious programme."
    ],
    "effects": [
      "The revolt intensified Byzantine repression of the Samaritan community, resulting in additional legal disabilities and the consolidation of Christian control over remaining Samaritan sacred sites in Palestine.",
      "The pattern of Samaritan revolts — from Antiochus Chuzon through the great revolts of 529 and 556 CE — significantly depopulated Samaria through Byzantine military reprisals, fundamentally altering the demographic and agricultural landscape of the central Palestinian hill country.",
      "The cumulative effect of Byzantine religious persecution that Antiochus Chuzon's revolt exemplified contributed to the relative Samaritan acquiescence in or welcome for the Arab-Muslim conquest of Palestine (636 CE), which instituted a dhimmi system that, while subordinate, was more tolerant than Byzantine Christian administration."
    ],
    "relationships": [
      {"sourceSlug": "antiochus-chuzon", "sourceName": "Antiochus Chuzon", "verb": "RESISTS", "targetSlug": "byzantine-empire", "targetName": "Byzantine Empire", "context": "Antiochus led a Samaritan armed revolt against Byzantine imperial rule in Palestine around 484–486 CE, challenging the religious coercion and legal discrimination imposed on Samaritans under Christian Roman governance."},
      {"sourceSlug": "emperor-zeno", "sourceName": "Emperor Zeno", "verb": "CAUSES", "targetSlug": "antiochus-chuzon", "targetName": "Antiochus Chuzon", "context": "Zeno's religious policies — including the conversion of the Samaritan holy site on Mount Gerizim to a Christian church — created the conditions that triggered the revolt under Antiochus Chuzon."},
      {"sourceSlug": "samaritan-revolts", "sourceName": "Samaritan Revolts", "verb": "INCLUDES", "targetSlug": "antiochus-chuzon", "targetName": "Antiochus Chuzon", "context": "Antiochus Chuzon's revolt was one of the first in a series of major Samaritan uprisings against Byzantine rule (484, 529, 556 CE) that collectively represented the most sustained resistance to Christian imperial homogenisation in the late antique Near East."}
    ],
    "places": [
      {"name": "Samaria, Palestine (West Bank)", "role": "Historic homeland of the Samaritan people and theatre of Antiochus Chuzon's revolt against Byzantine rule"},
      {"name": "Mount Gerizim, Samaria", "role": "Sacred mountain of Samaritan religion — its forced conversion to a Christian site was the immediate provocation for the revolt"}
    ],
    "subjects": ["Late Antiquity", "Byzantine Empire", "Palestine", "Religious History", "Resistance", "Classical Era", "Near East", "Minority History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Antiochus Chuzon led one of the first major Samaritan revolts against Byzantine religious coercion — an episode that illustrates the limits of imperial Christian homogenisation in the late antique Near East and contributed to the broader Samaritan pattern of resistance that eventually made many receptive to the Arab-Muslim conquest as a tolerable alternative to Byzantine oppression.",
      "significanceCategory": "regional"
    }
  }
},

"vortimer": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221vortimer.json",
  "slug": "vortimer",
  "data": {
    "summary": "Vortimer (fl. 5th century CE) was a legendary British prince and military leader — son of the High King Vortigern — who according to early medieval Welsh and Latin tradition led four successful battles against the Anglo-Saxon foederati led by the brothers Hengist and Horsa in sub-Roman Britain. He appears in Nennius's 'Historia Brittonum' (c. 830 CE), the 'Anglo-Saxon Chronicle', and Geoffrey of Monmouth's influential 'Historia Regum Britanniae' (c. 1138) as a defender of British Romano-Christian civilisation against the Saxon mercenaries whom his father Vortigern had fatally invited into Britain as auxiliary soldiers.\n\nThe historical kernel beneath the legendary Vortimer, if one exists, would belong to the turbulent period c. 440–480 CE when the sub-Roman British polities — fragmented successors to Roman provincial administration — were struggling to repel the growing power of the Germanic settlers in Kent and the east. His legendary career represents the British literary tradition's attempt to make sense of this period through heroic narrative: a 'good son' who reverses his father's catastrophic invitation of the Saxons and fights back, ultimately dying before he can secure victory. The same narrative logic would later crystallise in the Arthurian tradition, in which Arthur (like Vortimer) temporarily defeats the Saxon advance before a final catastrophe.\n\nVortimer is significant primarily as a literary and cultural figure: his story, preserved across multiple early medieval sources, reflects the trauma of the Anglo-Saxon settlement processed through the lens of hero and betrayal narrative. His legendary association with a burial mound that would protect Britain from sea-borne invasion — a pagan-type narrative given Christian colouring in later sources — reflects the layered traditions through which early medieval Britons made sense of their lost Romano-British past.",
    "causes": [
      "Vortigern's reported invitation of Hengist and Horsa as mercenary foederati — a common late Roman strategy for supplementing weakened regular forces — produced the Saxon presence in Kent that Vortimer according to tradition then spent his career fighting, making his father's policy the direct cause of his military context.",
      "The collapse of Roman administrative and military structures in Britain after 410 CE created the power vacuum in which sub-Roman warlords like the legendary Vortimer and Vortigern operated, with no imperial authority to arbitrate between British political factions and incoming Germanic settlers.",
      "The preservation of the Vortimer tradition by Welsh monastic chroniclers — particularly in Nennius — reflects the ongoing cultural project of maintaining British-Roman-Christian identity against the dominant Anglo-Saxon political and cultural order, giving the tradition its literary vitality."
    ],
    "effects": [
      "The Vortimer narrative contributed to the development of the Arthurian literary tradition: both figures represent British leaders who temporarily hold back the Saxon advance before ultimately failing, and the structural parallels between Vortimer's story and Arthur's suggest that one influenced the development of the other in early Welsh tradition.",
      "Geoffrey of Monmouth's amplification of the Vortimer story in 'Historia Regum Britanniae' (c. 1138) introduced it to pan-European literary culture, making it part of the Matter of Britain that influenced French, German, and eventually English medieval romance literature.",
      "The Vortimer tradition preserved cultural memory of the sub-Roman period that would otherwise be almost entirely invisible in the historical record — the chaotic 5th-century generation between Roman withdrawal and the stabilisation of the Anglo-Saxon kingdoms."
    ],
    "relationships": [
      {"sourceSlug": "vortigern", "sourceName": "Vortigern", "verb": "PRECEDES", "targetSlug": "vortimer", "targetName": "Vortimer", "context": "In medieval tradition, Vortimer's career was defined by his opposition to his father Vortigern's policy of Saxon settlement — the 'good son' repairing the 'bad father's' fatal invitation of Hengist and Horsa."},
      {"sourceSlug": "vortimer", "sourceName": "Vortimer", "verb": "RESISTS", "targetSlug": "anglo-saxon-settlement", "targetName": "Anglo-Saxon Settlement", "context": "Vortimer's legendary battles against Hengist and Horsa represent British resistance to the Anglo-Saxon advance — a narrative encapsulating the sub-Roman British experience of the 5th-century transition."},
      {"sourceSlug": "nennius", "sourceName": "Nennius", "verb": "DOCUMENTS", "targetSlug": "vortimer", "targetName": "Vortimer", "context": "Nennius's 'Historia Brittonum' (c. 830 CE) is the earliest major source for the Vortimer tradition — part of the Welsh monastic effort to preserve British historical memory against Anglo-Saxon cultural dominance."},
      {"sourceSlug": "vortimer", "sourceName": "Vortimer", "verb": "INFLUENCES", "targetSlug": "arthurian-legend", "targetName": "Arthurian Legend", "context": "Vortimer's narrative structure — a British hero temporarily defeating the Saxon advance before dying — parallels and likely contributed to the development of the Arthurian tradition in early Welsh sources."}
    ],
    "places": [
      {"name": "Kent, England", "role": "Primary theatre of Vortimer's legendary battles against Hengist and Horsa — the first Anglo-Saxon kingdom and the crucible of the early Anglo-Saxon settlement"},
      {"name": "Sub-Roman Britain", "role": "The political and cultural context of fragmented Romano-British polities in which the legendary Vortimer operated"}
    ],
    "subjects": ["Medieval History", "Sub-Roman Britain", "Anglo-Saxon History", "Classical Era", "Arthurian Legend", "British History", "Folklore", "Migration Period"],
    "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Vortimer is a legendary figure whose narrative represents the trauma of sub-Roman Britain's encounter with Anglo-Saxon settlement. As a literary character he contributed to the development of the Arthurian tradition, and his story — preserved in Nennius, Geoffrey of Monmouth, and Welsh tradition — was a vehicle for British-Roman cultural memory during the centuries of Anglo-Saxon political dominance.",
      "significanceCategory": "regional"
    }
  }
},

"orientius": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250orientius.json",
  "slug": "orientius",
  "data": {
    "summary": "Orientius (fl. early 5th century CE) was a Christian Latin poet and bishop of Auch in southwestern Gaul whose single surviving major work — the 'Commonitorium' — is the most vivid literary witness to the catastrophic barbarian invasions of Gaul in 406–409 CE. A man of evident classical education writing in the tradition of late Latin didactic poetry, Orientius composed his 'Commonitorium' (a moral exhortation poem in two books, c. 430 CE) as a meditation on Christian conduct in the face of temporal disaster, using the destruction he had personally witnessed to reinforce his moral and theological arguments. The poem belongs to the genre of late antique Christian poetry that processed the Roman world's collapse through an eschatological lens.\n\nThe 'Commonitorium's' most historically significant passage is Orientius's account of the barbarian crossing of the Rhine in December 406 CE and the subsequent devastation of Gaul: 'All Gaul smoked as a single pyre' — a line so stark and memorable that it has been quoted in virtually every scholarly account of the 406 invasions since its rediscovery. The passage describes the burning of cities and villages, the flight of populations, the disruption of the agricultural calendar, and the moral chaos that accompanied military destruction — providing a contemporary literary account of the event that transformed the western Roman world and opened the era of barbarian kingdoms.\n\nOrientius was bishop of Auch (Ausci in Novempopulana, southwestern Gaul) and is venerated as a saint in the Catholic Church with a feast day on 1 May. His ecclesiastical career situates him in the late Roman church's rapid institutionalisation as the primary surviving organisational framework of Roman civilisation after military and administrative collapse — a process in which local bishops like Orientius became the effective civil authorities of their communities.",
    "causes": [
      "The Rhine crossing of December 406 CE by the Vandals, Alans, and Suebi — which opened Gaul to the first large-scale barbarian penetration of the western provinces — was the formative catastrophe that Orientius personally witnessed and that provided the historical material for his 'Commonitorium's' most powerful passages.",
      "The Christian poetic tradition of didactic exhortation — from Prudentius to Juvencus — provided Orientius with the literary form through which to process contemporary historical trauma within a theological interpretive framework.",
      "The collapse of effective Roman military defence in the western provinces in the early 5th century left local bishops as the practical organisers of community survival, giving Orientius both the social authority and the pastoral motivation to address his congregation's experience of crisis."
    ],
    "effects": [
      "The 'Commonitorium' preserved one of the earliest and most vivid literary accounts of the 406 Rhine crossing and subsequent barbarian devastation of Gaul — a primary source for historians of the late Roman empire's military collapse.",
      "Orientius's literary handling of historical catastrophe within a Christian moral framework contributed to the late antique Christian tradition of interpreting imperial decline as divine judgement — a framework that Augustine developed at length in 'The City of God' (413–426 CE), written partly in response to the same crisis.",
      "As bishop of Auch, Orientius contributed to the transition of southwestern Gaul's Roman urban centres into Christian episcopal communities — the institutional model that preserved urban civilisation and administrative continuity through the Visigothic and Frankish kingdoms."
    ],
    "relationships": [
      {"sourceSlug": "orientius", "sourceName": "Orientius", "verb": "DOCUMENTS", "targetSlug": "barbarian-invasions-of-gaul", "targetName": "Barbarian Invasions of Gaul (406 CE)", "context": "Orientius's 'Commonitorium' contains the most memorable contemporary literary account of the 406 Rhine crossing — 'All Gaul smoked as a single pyre' — providing a primary witness to the catastrophe that opened the era of barbarian kingdoms in the West."},
      {"sourceSlug": "orientius", "sourceName": "Orientius", "verb": "INFLUENCES", "targetSlug": "late-antique-christian-poetry", "targetName": "Late Antique Christian Poetry", "context": "The 'Commonitorium' belongs to the late antique tradition of Christian didactic poetry that processed imperial collapse through eschatological interpretation, contributing to the literary tradition that shaped medieval Christian verse."},
      {"sourceSlug": "augustine-of-hippo", "sourceName": "Augustine of Hippo", "verb": "PARALLELS", "targetSlug": "orientius", "targetName": "Orientius", "context": "Both Orientius and Augustine responded to the same crisis of Roman military collapse in the early 5th century — Orientius in verse, Augustine in 'The City of God' — interpreting imperial disaster as divine pedagogy."}
    ],
    "places": [
      {"name": "Auch, France (Roman Ausci)", "role": "Episcopal see of Orientius — the community whose bishop he served as both spiritual leader and effective civil authority during the barbarian disruption of Gaul"},
      {"name": "Gaul (France/Belgium/Germany)", "role": "The territory devastated by the 406 Rhine crossing that Orientius witnessed and memorialised in the 'Commonitorium'"}
    ],
    "subjects": ["Late Antiquity", "Roman History", "Christian Poetry", "Classical Era", "Migration Period", "Church History", "Literary History", "France"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Orientius was a Christian Latin poet whose 'Commonitorium' (c. 430 CE) contains the most vivid literary witness to the barbarian devastation of Gaul after the 406 Rhine crossing. His verse — particularly 'All Gaul smoked as a single pyre' — is the most quoted contemporary literary source for the event that transformed the western Roman world and opened the age of barbarian kingdoms.",
      "significanceCategory": "regional"
    }
  }
},

"ammonius-grammaticus": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250ammonius-grammaticus.json",
  "slug": "ammonius-grammaticus",
  "data": {
    "summary": "Ammonius Grammaticus (fl. 2nd century CE) was a Greek grammarian and lexicographer working in the Alexandrian scholarly tradition whose surviving work 'Peri Homoion kai Diaphoron Lexeon' ('On Similar and Different Words') is one of the earliest systematic treatments of synonyms and near-synonyms in the Greek language. The work — more commonly known as the 'Ammonius' — catalogues pairs and groups of Greek words that appear to mean the same thing but which Ammonius argues have distinct and differentiable meanings: a project that belongs to the long Alexandrian grammatical tradition of distinguishing correct usage from incorrect, Attic Greek from degraded Koine, and precise philosophical language from imprecise popular speech.\n\nThe 'Peri Homoion' is a lexicographical work of the type that would be called a 'differentiae' in the Latin tradition — a systematic attempt to distinguish among apparently synonymous terms. Its importance lies less in individual entries than in its contribution to the Alexandrian grammatical enterprise of systematic linguistic analysis that fed into Byzantine scholarship and ultimately into the Renaissance recovery of Greek: the tradition of careful word-distinction that Ammonius exemplifies influenced Byzantine educational grammars and the humanist scholarship of the 15th–16th centuries that drew on Byzantine collections.\n\nAmmonius should be distinguished from several other classical figures named Ammonius: Ammonius of Athens (a Platonist philosopher, c. 50–120 CE), Ammonius Saccas (founder of Neoplatonism, c. 175–242 CE), and the later Ammonius son of Hermias (Neoplatonist commentator on Aristotle, c. 440–520 CE). The grammarian's precise dates are uncertain, placing him tentatively in the 2nd–3rd century CE Alexandrian intellectual milieu.",
    "causes": [
      "The Alexandrian grammatical tradition from the 3rd century BCE onward — represented by Aristarchus, Aristophanes of Byzantium, and their successors — created the institutional and intellectual framework within which systematic Greek lexicography developed, providing Ammonius with the method and the scholarly community his work required.",
      "The linguistic situation of the Roman imperial period — in which educated writers needed to distinguish refined Attic Greek from the widespread Koine of everyday use — created demand for precisely the kind of differentiae literature that Ammonius produced.",
      "The museum and library culture of Alexandria provided the scholarly resources (comprehensive manuscript collections, grammatical commentaries, predecessors' work) that enabled Ammonius to compile his systematic treatment of Greek synonyms."
    ],
    "effects": [
      "The 'Peri Homoion' influenced Byzantine lexicography and the tradition of Greek grammatical scholarship that was transmitted to the Renaissance through Byzantine scholars who brought Greek texts and learning to Italy after 1453.",
      "Ammonius's differentiae tradition contributed to the development of precise philosophical and theological vocabulary in the Greek-speaking church: the need to distinguish homoousios from homoiousios (the central controversy of 4th-century Trinitarian theology) reflects the kind of semantic sensitivity that Alexandrian grammatical scholarship cultivated.",
      "The tradition of systematic synonym-differentiation that Ammonius exemplifies is an ancestor of modern lexicography and semantic analysis — the scholarly impulse to establish the precise boundaries of meaning that drives dictionary-making and philosophical vocabulary analysis."
    ],
    "relationships": [
      {"sourceSlug": "ammonius-grammaticus", "sourceName": "Ammonius Grammaticus", "verb": "PRODUCES", "targetSlug": "peri-homoion", "targetName": "Peri Homoion kai Diaphoron Lexeon", "context": "Ammonius's 'On Similar and Different Words' is the principal surviving Greek differentiae text — a systematic treatment of Greek synonyms that contributed to Alexandrian grammatical scholarship."},
      {"sourceSlug": "alexandrian-scholars", "sourceName": "Alexandrian Grammatical Tradition", "verb": "PRECEDES", "targetSlug": "ammonius-grammaticus", "targetName": "Ammonius Grammaticus", "context": "Ammonius worked within the Alexandrian scholarly tradition of systematic Greek grammar and lexicography established by Aristarchus and Aristophanes of Byzantium in the 3rd–2nd century BCE."},
      {"sourceSlug": "ammonius-grammaticus", "sourceName": "Ammonius Grammaticus", "verb": "INFLUENCES", "targetSlug": "byzantine-scholarship", "targetName": "Byzantine Scholarship", "context": "The differentiae tradition Ammonius represented was incorporated into Byzantine educational grammar and lexicography, contributing to the Greek scholarly inheritance transmitted to the Renaissance."}
    ],
    "places": [
      {"name": "Alexandria, Egypt", "role": "Probable location of Ammonius's scholarly activity — the centre of the grammatical tradition in which he worked"},
      {"name": "Roman Empire (Eastern Mediterranean)", "role": "Broader context of 2nd–3rd century CE Greek scholarly culture in which Ammonius's lexicographical work was produced and circulated"}
    ],
    "subjects": ["Classical Scholarship", "Greek Language", "Linguistics", "Alexandria", "Classical Era", "Intellectual History", "Grammar", "Lexicography"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Ammonius Grammaticus was an Alexandrian lexicographer whose 'Peri Homoion' — a systematic treatment of Greek synonyms — contributed to the Alexandrian grammatical tradition that shaped Byzantine scholarship and ultimately the Renaissance recovery of Greek. His differentiae method is an ancestor of systematic lexicography and the precise vocabulary analysis that shaped both philosophical and theological discourse.",
      "significanceCategory": "regional"
    }
  }
},

"jan-van-lannoy": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220jan-van-lannoy.json",
  "slug": "jan-van-lannoy",
  "data": {
    "summary": "Jan van Lannoy (c. 1410–1492) was a Flemish nobleman, diplomat, and military commander who served the Dukes of Burgundy across a career spanning five decades — a prominent figure in the court culture of the Burgundian state that was the most sophisticated political entity in 15th-century northwestern Europe. Born into the noble Lannoy family of Hainaut, he built his career through a combination of military service, diplomatic missions, and court ceremonial that exemplified the chivalric aristocratic culture of the Order of the Golden Fleece, to which he was elected around 1445. His career illustrates the political and cultural world of Burgundy under Philip the Good and Charles the Bold that represented the high point of late medieval court civilisation before the Burgundian inheritance passed to the Habsburgs.\n\nJan van Lannoy served on multiple diplomatic missions for Philip the Good and represented Burgundian interests in negotiations with France, England, and the Empire. His military service included campaigns in the Hundred Years War context — Burgundy's complex shifting alliances between English and French sides defined the politics of his early career. He was appointed governor of Holland, Zeeland, and Friesland in the 1450s, one of the most significant administrative appointments in the Burgundian Low Countries, responsible for maintaining order in the commercially vital maritime provinces. His administration of the northern provinces placed him at the intersection of Burgundian court culture and the mercantile world of Flemish and Dutch cities.\n\nAs a knight of the Golden Fleece — the Burgundian chivalric order founded by Philip the Good in 1430, modelled on the English Order of the Garter and the French Order of the Star — Jan van Lannoy participated in the ceremonial and diplomatic institution that was one of the most innovative political instruments of 15th-century monarchy: an order that bound the high nobility to personal loyalty to the duke while creating a pan-European prestige network.",
    "causes": [
      "The Burgundian ducal state's exceptional wealth — drawing on the textile revenues of Flemish cities, the agricultural surpluses of the Netherlandish Low Countries, and ducal toll revenues — provided the economic foundation for the elaborate court culture and chivalric ceremonial in which Jan van Lannoy's career was embedded.",
      "The Lannoy family's established position in Burgundian noble service — his uncle Guillebert de Lannoy had been a celebrated knight and diplomat under Philip the Good's father — gave Jan van Lannoy the social capital and court connections from which his own career developed.",
      "Philip the Good's political strategy of binding the high nobility through the Order of the Golden Fleece and through provincial governorships created the institutional framework that gave nobles like Jan van Lannoy both meaningful authority and strong incentives for loyalty."
    ],
    "effects": [
      "Jan van Lannoy's governorship of Holland, Zeeland, and Friesland contributed to the administrative integration of the northern Low Countries into the Burgundian state — a process that created the political and administrative framework that would eventually become the Habsburg Netherlands and, in the 16th century, the theatre of the Dutch Revolt.",
      "His participation in the Order of the Golden Fleece placed him in the network that bound Burgundian, Habsburg, and English noble culture together across the late medieval period — a diplomatic and ceremonial institution whose significance extended far beyond its chivalric ritual.",
      "The court culture that Jan van Lannoy embodied — combining chivalric ceremony, diplomatic sophistication, and administrative competence — represented the Burgundian synthesis that influenced the Habsburg court style and, through it, the ceremonial culture of early modern European monarchy."
    ],
    "relationships": [
      {"sourceSlug": "jan-van-lannoy", "sourceName": "Jan van Lannoy", "verb": "SERVES", "targetSlug": "philip-the-good", "targetName": "Philip the Good", "context": "Jan van Lannoy was a senior noble and diplomat in the service of Philip the Good, Duke of Burgundy — the most powerful ruler in 15th-century northwestern Europe."},
      {"sourceSlug": "order-of-the-golden-fleece", "sourceName": "Order of the Golden Fleece", "verb": "INCLUDES", "targetSlug": "jan-van-lannoy", "targetName": "Jan van Lannoy", "context": "Jan van Lannoy was elected to the Order of the Golden Fleece around 1445 — the Burgundian chivalric order that was the foremost diplomatic and prestige network of 15th-century European nobility."},
      {"sourceSlug": "burgundy", "sourceName": "Duchy of Burgundy", "verb": "EMPLOYS", "targetSlug": "jan-van-lannoy", "targetName": "Jan van Lannoy", "context": "Burgundy provided the political framework for Jan van Lannoy's entire career — from military service to diplomatic missions to the governorship of Holland, Zeeland, and Friesland."}
    ],
    "places": [
      {"name": "Burgundian Netherlands (Belgium/Netherlands)", "role": "Theatre of Jan van Lannoy's administrative and military career — particularly his governorship of Holland, Zeeland, and Friesland"},
      {"name": "Dijon/Brussels, Burgundy", "role": "Centres of the Burgundian ducal court where Jan van Lannoy participated in chivalric ceremony, Golden Fleece chapters, and diplomatic activity"}
    ],
    "subjects": ["Medieval History", "Burgundy", "Low Countries", "Nobility", "Medieval Era", "Diplomacy", "Chivalry", "Europe"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "DIPLOMATIC_HISTORY", "CULTURAL_TRANSMISSION"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Jan van Lannoy was a senior noble in the Burgundian ducal state who embodied the chivalric court culture of 15th-century Europe — participating in the Order of the Golden Fleece, serving as a diplomat for Philip the Good, and governing the commercially vital northern provinces of Holland and Zeeland. His career illustrates the sophisticated political and administrative culture of the Burgundian state that shaped Habsburg governance of the Netherlands.",
      "significanceCategory": "regional"
    }
  }
},

"abu-amra-kaysan": {
  "filepath": "data/appwrite-export/entities/204-Class-204/204abu-amra-kaysan.json",
  "slug": "abu-amra-kaysan",
  "data": {
    "summary": "Abu Amra Kaysan (fl. late 7th century CE), also known simply as Kaysan, was an early Islamic figure associated with the origins of the Kaysaniyya — one of the first and most theologically innovative Shia Muslim movements of the formative Islamic period. A mawla (client/freedman) of Ali ibn Abi Talib or of his son Muhammad ibn al-Hanafiyya, Kaysan is associated in early Islamic heresiographic sources with the circle around Mukhtar al-Thaqafi, the Kufan leader who led a major Shia revolt in 685–687 CE in the name of Muhammad ibn al-Hanafiyya (Ali's son by a wife other than Fatima, hence not the son of the Prophet's daughter).\n\nThe Kaysaniyya movement that carried Kaysan's name developed distinctive theological positions that would prove highly influential on later Shia thought: belief in the imamate of Muhammad ibn al-Hanafiyya, the doctrine that the imam had not died but was in occultation (ghayba) on Mount Radwa awaiting his return as the Mahdi — the first systematic development of the occultation doctrine that would become central to Twelver Shia theology in its mature form. This early Kaysanite ghayba concept anticipated by centuries the mature Twelver doctrine of the occultation of the Twelfth Imam (874 CE).\n\nKaysan himself is a shadowy figure whose historical reality is difficult to establish — some scholars have questioned whether he was a historical individual or a narrative vehicle through which later heresiographers organised early Shia tendencies. What is historically clear is that the theological currents associated with Kaysanism — particularly the ghayba/occultation doctrine and the exaltation of Ali's family beyond the immediate Husaynid line — contributed significantly to the diversification of early Shia thought and provided some of the conceptual vocabulary for later Ismaili and Twelver developments.",
    "causes": [
      "The assassination of Husayn ibn Ali at Karbala (680 CE) — which delegitimised Umayyad rule in the eyes of Ali's partisans — created the intense political and theological pressure that generated multiple competing Shia movements in Kufa, each offering different solutions to the question of legitimate Islamic leadership.",
      "Muhammad ibn al-Hanafiyya's position as a son of Ali not born of Fatima created the need for a distinct theological justification of his imamate claim — the Kaysanite doctrine of exceptional imam status and occultation served this political-theological purpose.",
      "Mukhtar al-Thaqafi's revolt in Kufa (685–687 CE) created the political and military context within which Kaysanite theological innovations were developed — the movement's theology was partly shaped by the needs of a revolutionary movement that needed to explain both political failure and continued expectation."
    ],
    "effects": [
      "The Kaysanite doctrine of imam occultation (ghayba) — the belief that the imam had not died but was concealed and would return as the Mahdi — became one of the most theologically productive concepts in Shia Islam, influencing the development of Ismaili Shia doctrine (the 'hidden imam' of the Fatimid line) and ultimately the Twelver Shia doctrine of the occultation of the Twelfth Imam.",
      "The Kaysaniyya's exaltation of the whole Alid family beyond the Husaynid line contributed to the theological diversity of early Shia Islam — demonstrating that the question of legitimate succession was not settled within the Shia tradition itself, but remained contested across multiple claimant lines.",
      "Kaysanite poetry — including verses by Kuthayyir Azza and other poets associated with the movement — preserved Kaysanite theological concepts in literary form that circulated widely in early Islamic culture, contributing to the dissemination of proto-Shia ideas across the Islamic world."
    ],
    "relationships": [
      {"sourceSlug": "abu-amra-kaysan", "sourceName": "Kaysan (Abu Amra)", "verb": "CAUSES", "targetSlug": "kaysaniyya", "targetName": "Kaysaniyya", "context": "The Kaysaniyya Shia movement took its name from Kaysan — whether as its founder, its most prominent early theorist, or a heresiographic cipher for a set of theological tendencies."},
      {"sourceSlug": "mukhtar-al-thaqafi", "sourceName": "Mukhtar al-Thaqafi", "verb": "PRECEDES", "targetSlug": "abu-amra-kaysan", "targetName": "Kaysan", "context": "Mukhtar's Kufan revolt (685–687 CE) in the name of Muhammad ibn al-Hanafiyya was the political context within which Kaysanite theological innovations developed."},
      {"sourceSlug": "kaysaniyya", "sourceName": "Kaysaniyya", "verb": "INFLUENCES", "targetSlug": "twelver-shia", "targetName": "Twelver Shia Islam", "context": "Kaysanite ghayba (occultation) doctrine anticipated the mature Twelver Shia concept of the occulted Twelfth Imam — a theological development that shaped the dominant branch of Shia Islam."},
      {"sourceSlug": "battle-of-karbala", "sourceName": "Battle of Karbala (680 CE)", "verb": "CAUSES", "targetSlug": "abu-amra-kaysan", "targetName": "Kaysan", "context": "Husayn's martyrdom at Karbala (680 CE) created the theological and political crisis that generated the multiple Shia movements of the 680s, including the Kaysaniyya."}
    ],
    "places": [
      {"name": "Kufa, Iraq", "role": "Centre of early Shia political and theological activity where the Kaysaniyya developed — the city that was Mukhtar's base and the incubator of early Shia theological diversity"},
      {"name": "Mount Radwa, Arabia (Hejaz)", "role": "Mountain identified in Kaysanite tradition as the place of Muhammad ibn al-Hanafiyya's occultation — the earliest geographic specificity given to the imam occultation doctrine"}
    ],
    "subjects": ["Islamic History", "Shia Islam", "Medieval History", "Theology", "Medieval Era", "Iraq", "Early Islam", "Religious History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Kaysan/Abu Amra is the eponymous figure of the Kaysaniyya — one of the first Shia movements to develop the imam occultation (ghayba) doctrine that became central to both Ismaili and Twelver Shia theology. Though a shadowy historical figure, the theological current that bore his name contributed the conceptual vocabulary of imam concealment that shapes Shia eschatology to the present day.",
      "significanceCategory": "regional"
    }
  }
}

}  # end ENRICHMENTS


def get_entity(filepath, slug):
    with open(filepath) as f:
        data = json.load(f)
    for e in data.get("entities", []):
        if e.get("slug") == slug:
            return e, data
    return None, data

def apply_enrichment(filepath, slug, enrichment_data, dry_run=False):
    entity, data = get_entity(filepath, slug)
    if entity is None:
        print(f"  ERROR: slug '{slug}' not found in {filepath}")
        return False
    raw = entity.get("detailsJson", "{}")
    details = raw if isinstance(raw, dict) else json.loads(raw or "{}")
    old_len = len(details.get("summary", "") or "")
    if old_len >= 800:
        print(f"  SKIP — already enriched ({old_len}c)")
        return False
    if dry_run:
        print(f"  DRY RUN — would enrich {old_len}c → {len(enrichment_data.get('summary',''))}c")
        return True
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for k, v in enrichment_data.items():
        details[k] = v
    edit_log = details.get("_editLog", [])
    edit_log.append({"field": "summary", "editorId": EDITOR_ID, "sessionId": SESSION_ID,
                     "timestamp": now, "oldValue": "", "newValue": enrichment_data.get("summary","")[:200] + "…"})
    details["_editLog"] = edit_log
    entity["detailsJson"] = details
    entity["_unsyncedEdits"] = True
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ENRICHED — {old_len}c → {len(enrichment_data.get('summary',''))}c")
    return True

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("** DRY RUN **\n")
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    enriched = skipped = errors = 0
    for slug, spec in ENRICHMENTS.items():
        fp = os.path.join(repo_root, spec["filepath"])
        print(f"\n[{slug}]")
        if not os.path.exists(fp):
            print(f"  ERROR: not found: {fp}")
            errors += 1
            continue
        ok = apply_enrichment(fp, slug, spec["data"], dry_run=dry_run)
        if ok: enriched += 1
        else: skipped += 1
    print(f"\n{'='*60}\nRESULTS: {enriched} enriched, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
