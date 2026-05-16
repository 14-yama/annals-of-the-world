#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 14 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: felix-of-como, peter-of-toledo, marcus-valerius-volusus, maturinus,
          federico-savelli, jayavarman-kaundinya, sarduri-iii, eusebius
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-14-may2026"

ENRICHMENTS = {

"felix-of-como": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250felix-of-como.json",
  "slug": "felix-of-como",
  "data": {
    "summary": "Felix of Como (died 8 October 391 CE) was the first known Bishop of Como in northern Italy — venerated as a saint in the Catholic Church with feast day on 8 October. He was consecrated bishop of the newly organised diocese of Como (Roman Comum), a city of considerable strategic importance in the late Roman Empire as a gateway to the Alpine passes and the major road linking the Po plain with the trans-Alpine territories north of the Alps. His appointment as bishop in the late 4th century falls within the great period of Latin church organisation under Ambrose of Milan — and Felix of Como is understood to have been a bishop consecrated during or shortly after Ambrose's tenure as Bishop of Milan (374–397 CE), which transformed the Milanese church into the dominant ecclesiastical centre of northern Italy.\n\nThe historical evidence for Felix of Como beyond his status as founding bishop and saint is thin — the principal source being the later hagiographic tradition and the church calendars that preserve his name and feast day. What can be said with confidence is that his episcopate falls in a critical moment for the northern Italian church: the conversion of Constantine (312 CE), the Council of Nicaea (325 CE), and the subsequent Arian controversy had transformed the church from a persecuted minority to the state religion of the empire, and Ambrose's forceful personality and theological energy were reshaping the ecclesiastical organisation of the Milan-centred northern Italian church in precisely the decades when Felix was establishing the diocese of Como.\n\nComo's importance as an Alpine gateway — its position on Lake Como (Lacus Larius) at the foot of the Splügen and Maloja passes connecting northern Italy with the Rhine valley — gave the diocese of Como a lasting significance in the church's trans-Alpine communications and in the commercial and strategic life of the region. Felix's establishment of the bishopric laid the institutional foundation for a diocese that would persist through the medieval period and beyond.",
    "causes": [
      "The post-Constantinian reorganisation of the western church — the systematic creation of episcopal sees in the major towns of the empire following Constantine's conversion — created the institutional context in which the diocese of Como was organised and Felix was appointed as its founding bishop.",
      "Ambrose of Milan's dominant influence over the northern Italian church (374–397 CE) — his organisation of the Milanese church's suffragen sees and his forceful assertion of episcopal authority — provided the specific ecclesiastical environment in which Felix's episcopate at Como was shaped.",
      "Como's strategic position as a gateway to the Alpine passes — its importance for trans-Alpine communication and trade — made the organisation of a bishop at Como a logical step in the church's administrative integration of the northern Italian dioceses."
    ],
    "effects": [
      "Felix's establishment of the diocese of Como created an enduring ecclesiastical institution that would persist through the medieval period — the diocese of Como as a permanent feature of the northern Italian church's structure.",
      "Felix's veneration as the founding bishop of Como — embedded in the local liturgical calendar and church tradition — gave the diocese of Como a founding saint around whose memory the early Christian community of the region could organise its identity.",
      "The diocese of Como's later medieval and early modern significance — as an important diocese on the major trans-Alpine route and as part of the extensive Ambrosian church tradition of Milan — built on the foundation that Felix's 4th-century episcopate established."
    ],
    "relationships": [
      {"sourceSlug": "felix-of-como", "sourceName": "Felix of Como", "verb": "FOUNDS", "targetSlug": "diocese-of-como", "targetName": "Diocese of Como", "context": "Felix was the first bishop of Como — the founding figure of the diocesan church that would become a permanent institution of northern Italian Christianity."},
      {"sourceSlug": "ambrose-of-milan", "sourceName": "Ambrose of Milan", "verb": "INFLUENCES", "targetSlug": "felix-of-como", "targetName": "Felix of Como", "context": "Felix's episcopate at Como was shaped by the dominant ecclesiastical influence of Ambrose of Milan (374–397 CE), who organised the northern Italian church and consecrated bishops throughout his metropolitan province."},
      {"sourceSlug": "late-roman-church", "sourceName": "Late Roman Church (4th Century)", "verb": "PRODUCES", "targetSlug": "felix-of-como", "targetName": "Felix of Como", "context": "Felix was a product of the post-Constantinian church's systematic organisation of episcopal sees — the transformation of Christianity from persecuted minority to imperial institution that produced the network of bishops across the western empire."}
    ],
    "places": [
      {"name": "Como (Comum), Lombardy, Italy", "role": "Felix's diocesan city — the gateway to the Alpine passes, strategically important as a northern Italian communication hub"},
      {"name": "Lake Como (Lacus Larius), northern Italy", "role": "The geographic context of Felix's diocese — the lake town at the foot of the Splügen and Maloja Alpine passes"}
    ],
    "subjects": ["Early Christianity", "Late Roman Church", "Classical Era", "Italy", "Church Organisation", "4th Century CE", "Northern Italy", "Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Felix of Como was the founding bishop of Como (died 391 CE) — an early Christian episcopal see established during the great post-Constantinian organisation of the western church under Ambrose of Milan's influence. Venerated locally as a saint with feast day October 8, Felix represents the foundational figures of the northern Italian diocesan church whose careers are preserved primarily through liturgical tradition.",
      "significanceCategory": "local"
    }
  }
},

"peter-of-toledo": {
  "filepath": "data/appwrite-export/entities/241-Class-241/241peter-of-toledo.json",
  "slug": "peter-of-toledo",
  "data": {
    "summary": "Peter of Toledo (died c. 1156) was a 12th-century Christian scholar and translator active in Toledo, Spain — a participant in the extraordinary translating enterprise of the Toledo School of Translators (sometimes called the Toledo Translation School), which was one of the most significant intellectual projects of the medieval world. Working in Toledo under the patronage of Archbishop Raymond I of Toledo (1124–1152), Peter of Toledo — along with colleagues including Herman the German, Dominicus Gundissalinus, and Robert of Ketton — translated works from Arabic into Latin, transmitting the accumulated knowledge of the Islamic world (including Arabic translations of Greek philosophical and scientific texts) to the Latin West.\n\nPeter of Toledo is credited with translating Al-Kindi's 'Risāla fī ibṭāl aḥkām al-nujūm' (On the Invalidity of the Judgements of the Astrologers) and other Arabic philosophical texts into Latin — a work he undertook in collaboration with other scholars. More significantly, Peter of Toledo was involved in one of the most provocative translation projects of the 12th century: he collaborated with the English scholar Robert of Ketton on the Latin translation of the Quran — the 'Lex Mahumet pseudoprophete' (1143), the first Latin translation of the Quran, commissioned by Peter the Venerable (Abbot of Cluny) specifically to provide Christian polemicists with ammunition for arguing against Islam. This translation — although deeply polemical in intent — was nevertheless an extraordinary act of cross-cultural intellectual engagement and was the primary Latin Quran used by Christian scholars for the next four centuries.\n\nThe Toledo translators' enterprise was made possible by Toledo's unique position as a multicultural city: captured by Alfonso VI of Castile from the Moors in 1085, Toledo contained a substantial Jewish, Arab, and Mozarabic (Christian) population, and the three-way collaboration of Arabic-speaking translators, Latinate scholars, and Jewish intermediaries was the human infrastructure of the translation project. Peter of Toledo and his colleagues were at the heart of the most significant intellectual bridge between the Islamic and Christian worlds of the medieval period.",
    "causes": [
      "The Reconquista's capture of Toledo by Alfonso VI in 1085 — creating a multicultural city under Christian rule where Arabic, Latin, and Hebrew scholarship could collaborate — provided the unique human and cultural infrastructure that made the Toledo translation enterprise possible.",
      "Archbishop Raymond I of Toledo's patronage (1124–1152) — his deliberate organisation of translators from diverse linguistic backgrounds — created the institutional framework within which Peter of Toledo and his colleagues could undertake sustained translation projects.",
      "The intellectual hunger of 12th-century Latin Europe for the classical Greek philosophical and scientific texts that had been preserved and developed in Arabic translation — Aristotle, Ptolemy, Euclid, Galen — motivated the Archbishop's translation programme and created the demand for the translators' output."
    ],
    "effects": [
      "The Toledo translators' work — including Peter of Toledo's contributions — transmitted the accumulated philosophical, scientific, and medical knowledge of the Islamic world to Latin Europe, catalysing the 12th-century Renaissance and providing the intellectual foundations for Scholasticism and the later scientific revolution.",
      "The first Latin translation of the Quran (1143) — in which Peter of Toledo participated — gave Latin-Christian scholars direct access to Islamic scripture for the first time and became the primary reference for Christian theological polemic against Islam for four centuries, including by Thomas Aquinas and Nicholas of Cusa.",
      "The translation enterprise at Toledo created a model of cross-cultural scholarly collaboration — Arab, Jewish, and Christian scholars working together — that influenced subsequent translation and intellectual exchange projects and that represents one of the most productive episodes of medieval cultural transmission."
    ],
    "relationships": [
      {"sourceSlug": "peter-of-toledo", "sourceName": "Peter of Toledo", "verb": "PARTICIPATES_IN", "targetSlug": "toledo-school-of-translators", "targetName": "Toledo School of Translators", "context": "Peter was one of the core translators at 12th-century Toledo — collaborating with Robert of Ketton, Dominicus Gundissalinus, and others in transmitting Arabic philosophical and scientific texts to Latin Europe."},
      {"sourceSlug": "peter-of-toledo", "sourceName": "Peter of Toledo", "verb": "TRANSLATES", "targetSlug": "quran-latin-translation", "targetName": "First Latin Translation of the Quran (1143)", "context": "Peter collaborated with Robert of Ketton on the first Latin Quran ('Lex Mahumet pseudoprophete', 1143) commissioned by Peter the Venerable — the primary Latin Quran for four centuries."},
      {"sourceSlug": "islamic-golden-age", "sourceName": "Islamic Golden Age", "verb": "TRANSMITS_TO", "targetSlug": "peter-of-toledo", "targetName": "Peter of Toledo (and Toledo Translators)", "context": "The Islamic world's accumulated philosophical, scientific, and mathematical knowledge — preserved and developed in Arabic — was the primary source material that Peter and his Toledo colleagues transmitted to Latin Europe."}
    ],
    "places": [
      {"name": "Toledo, Castile (Spain)", "role": "The multicultural city — captured from the Moors 1085 — where Peter's translation activity was centred, exploiting Toledo's unique Arabic-Latin-Hebrew scholarly community"},
      {"name": "Iberian Peninsula", "role": "The broader context of Peter's work — the zone of contact between Christian and Islamic civilisations where medieval cross-cultural intellectual exchange was most intensive"}
    ],
    "subjects": ["Medieval Scholarship", "Translation History", "Medieval Era", "Spain", "Islamic Golden Age", "Medieval History", "12th Century", "Knowledge Transfer"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Peter of Toledo was a 12th-century translator at the Toledo School who participated in the first Latin translation of the Quran (1143) and helped transmit Arabic philosophical knowledge to Latin Europe. The Toledo translators' enterprise — of which Peter was a part — catalysed the 12th-century Renaissance and provided the intellectual foundations for Scholasticism by transmitting the accumulated knowledge of the Islamic world.",
      "significanceCategory": "significant"
    }
  }
},

"marcus-valerius-volusus": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220marcus-valerius-volusus.json",
  "slug": "marcus-valerius-volusus",
  "data": {
    "summary": "Marcus Valerius Volusus (fl. c. 500 BCE; consul 505 BCE) was a Roman Republican politician of the early Republic — one of the patrician consuls of the first generation of the Roman Republic following the expulsion of the Tarquin kings (traditional date: 509 BCE). The Valerian gens (clan) was among the most prestigious of the early Republican patriciate: the Valerians were consistently at the forefront of the early Republican aristocracy, and Marcus Valerius Volusus was one of the members of this dynasty who held the consulship in the Republic's first decades.\n\nMarcus Valerius Volusus is recorded by ancient tradition (primarily through Livy and Dionysius of Halicarnassus) as consul in 505 BCE — a period when the early Roman Republic was engaged in the persistent wars against the Sabines, the Volsci, and other neighbouring Latin and Italic peoples that dominated Roman military activity in the late 6th and early 5th centuries BCE. He is also mentioned in some ancient sources in connection with the early Roman tradition of the dictator (the appointment of a single emergency commander in periods of crisis) — one of the key Republican constitutional innovations. The historical reliability of these early Republican records is contested by modern scholarship: the traditional Roman account of the early Republic was transmitted in writing centuries after the events, and the consul fasti (lists of annual magistrates) may contain interpolations and anachronisms.\n\nThe Valerian gens connection is significant beyond Marcus Valerius Volusus himself: the Valerians produced multiple consuls and generals in the early Republic, and the 'Lex Valeria' tradition (associated with Publius Valerius Publicola, the Valerians' most famous early Republican hero) — giving citizens the right of appeal (provocatio) against magistrates — was one of the foundational traditions of Roman Republican liberty. Marcus Valerius Volusus's consulship is one entry in the broader Valerian tradition of early Republican leadership.",
    "causes": [
      "The expulsion of the Tarquin kings (traditional date 509 BCE) and the establishment of the Roman Republic created the consular system — the annual election of two consuls as supreme military and civil authorities — within which Marcus Valerius Volusus held office.",
      "The Valerian gens's established position in the Roman patrician aristocracy — their wealth, their client networks, and their family tradition of military service and public office — enabled Marcus Valerius Volusus and other Valerians to reach the consulship in the early Republic's competitive aristocratic environment.",
      "The early Republic's persistent military pressure from the Sabines, Volsci, and other Italic peoples — requiring competent military leadership year after year — created the martial context within which consuls like Marcus Valerius Volusus demonstrated their worth and preserved their family's standing."
    ],
    "effects": [
      "Marcus Valerius Volusus's consulship contributed to the Roman annalistic record of the early Republic — one entry in the consul fasti that, together with others, preserved the documentary foundation of Roman historical memory and the tradition of patrician families' public service.",
      "The Valerian gens's consistent presence in the early Republican leadership — of which Marcus Valerius Volusus was one representative — helped to stabilise the patrician aristocratic system and establish the norms of Roman Republican political culture.",
      "The ancient tradition connecting Valerians with key Republican constitutional innovations (provocatio, the dictatorship) — whether historically accurate or retrospective elaboration — contributed to the ideological framework of Roman Republican liberty within which subsequent generations of Romans understood their constitution."
    ],
    "relationships": [
      {"sourceSlug": "marcus-valerius-volusus", "sourceName": "Marcus Valerius Volusus", "verb": "MEMBER_OF", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "As consul of 505 BCE, Marcus Valerius Volusus was one of the annual supreme magistrates of the early Roman Republic — the highest political and military authority in the nascent Republican state."},
      {"sourceSlug": "valerian-gens", "sourceName": "Valerian Gens (Patrician Clan)", "verb": "PRODUCES", "targetSlug": "marcus-valerius-volusus", "targetName": "Marcus Valerius Volusus", "context": "Marcus Valerius Volusus was a member of the Valerian gens — one of the most prestigious patrician clans of the early Roman Republic, associated with constitutional innovations including provocatio and the dictatorship."},
      {"sourceSlug": "early-roman-republic", "sourceName": "Early Roman Republic (509–264 BCE)", "verb": "SHAPES", "targetSlug": "marcus-valerius-volusus", "targetName": "Marcus Valerius Volusus", "context": "Marcus Valerius Volusus's career exemplifies the early Roman Republic's consular system — the annual election of patrician military leaders that was the basic constitutional mechanism of the pre-democratic Roman state."}
    ],
    "places": [
      {"name": "Rome, Italian Peninsula", "role": "The city of Marcus Valerius Volusus's political career — the early Republican city-state whose patrician aristocracy produced his consulship"},
      {"name": "Central Italy (Sabine/Volscian borderlands)", "role": "The military theatre of the early Republican wars — the territory where consuls like Marcus Valerius Volusus would have commanded Roman armies"}
    ],
    "subjects": ["Roman Republic", "Early Roman History", "Classical Era", "Ancient Rome", "Republican Rome", "Patrician Aristocracy", "Consular History", "Classical Italy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Marcus Valerius Volusus was a Roman consul of 505 BCE — one of the early patrician magistrates of the first Roman Republic, a member of the prestigious Valerian gens whose family tradition included key Republican constitutional innovations. His historical significance is primarily as an entry in the consul fasti and as a representative of the Valerian clan's early Republican leadership.",
      "significanceCategory": "local"
    }
  }
},

"maturinus": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250maturinus.json",
  "slug": "maturinus",
  "data": {
    "summary": "Saint Maturinus (also Mathurin or Materne; died c. 388 CE, or by some traditions c. 301 CE) was a Christian confessor and saint of the late Roman period — associated with Larchant (Roman Larca/Larcha) in the Gâtinais region of what is now north-central France (Seine-et-Marne, Île-de-France). He is venerated in the Catholic Church and his feast day is celebrated on 1 November in some local traditions and on 9 November in the Roman Martyrology. Maturinus is the patron saint of Larchant and is traditionally credited with the evangelisation of the Gâtinais region, with exorcising the daughter of the Roman emperor Maximianus (a legendary element typical of early Christian hagiography), and with working miracles of healing.\n\nThe historical evidence for Maturinus is almost entirely hagiographic: his life is known primarily through the 'Vita Sancti Maturini' composed much later than the events it purports to describe, and the historical details (including the story of Maximianus's daughter) are standard hagiographic topoi. What can be said with more confidence is that Maturinus was venerated in the Gâtinais region from an early period — the medieval pilgrimage church of Saint-Mathurin at Larchant was one of the major pilgrimage centres of the Île-de-France, attracting pilgrims from across the region throughout the medieval period. The 13th-century Gothic church of Saint-Mathurin at Larchant, built to accommodate the pilgrimage cult, was a significant medieval architectural achievement whose imposing tower (now ruined) is still a regional landmark.\n\nMaturinus became associated in popular tradition with madness and mental illness — as the patron who could cure insanity — and this association gave his name to the 'Maisons de Mathurins' (later 'Maisons des fous'), the French institutions for the mentally ill. The 'Mathurins' designation for religious orders who ran charitable institutions reflects the popular association between Saint Mathurin and charitable care of the afflicted. The Order of the Most Holy Trinity (Trinitarians), who ran ransoming houses for captives and were known in France as the 'Mathurins,' had their Parisian house near the church of the Mathurins that was associated with the saint's name.",
    "causes": [
      "The Christianisation of Roman Gaul in the 3rd–4th centuries CE — the spread of Christianity into the rural provinces of northern France through missionary activity and the establishment of episcopal and monastic centres — created the context for Maturinus's evangelising activity in the Gâtinais region.",
      "The hagiographic tradition's standard topoi — the conversion of pagan families (Maturinus's parents), the working of miracles, the exorcism of possessed individuals (including the emperor's daughter) — shaped the 'Vita Sancti Maturini' and determined how the saint's memory was preserved and transmitted.",
      "The medieval pilgrimage economy — the system of shrines, relics, and miraculous cures that drew pilgrims across Europe — created the institutional and financial incentive to develop the cult of Maturinus at Larchant, producing the Gothic church whose construction reflected the pilgrimage's economic value to the community."
    ],
    "effects": [
      "The pilgrimage cult of Saint Mathurin at Larchant developed into one of the significant medieval pilgrimage sites of the Île-de-France — the Gothic church of Saint-Mathurin (13th century) at Larchant attracted royal patronage and pilgrims and became a major ecclesiastical monument of the region.",
      "The popular association of Maturinus/Mathurin with the cure of madness and mental illness gave his name to French charitable institutions for the mentally ill — the 'Maisons de Mathurins' — and contributed to the language of French charity and institutional care for the afflicted.",
      "The Trinitarian order's Parisian house ('les Mathurins') — named after the saint — became an important institution in medieval Paris and the site of various ecclesiastical and political events, extending Maturinus's name into the broader culture of medieval French Christianity."
    ],
    "relationships": [
      {"sourceSlug": "maturinus", "sourceName": "Saint Maturinus", "verb": "EVANGELISES", "targetSlug": "gatinais-region", "targetName": "Gâtinais Region, northern France", "context": "Maturinus is credited with the Christianisation of the Gâtinais (Larchant area) — his missionary activity in the late Roman period laid the foundation for the subsequent pilgrimage cult."},
      {"sourceSlug": "larchant-pilgrimage", "sourceName": "Larchant Pilgrimage (Gothic church)", "verb": "COMMEMORATES", "targetSlug": "maturinus", "targetName": "Saint Maturinus", "context": "The 13th-century Gothic church of Saint-Mathurin at Larchant — one of the major pilgrimage sites of the Île-de-France — was built around the saint's tomb and memory, reflecting the pilgrimage cult's medieval importance."},
      {"sourceSlug": "maturinus", "sourceName": "Saint Maturinus", "verb": "INSPIRES", "targetSlug": "trinitarian-order", "targetName": "Trinitarian Order (Mathurins)", "context": "The Trinitarian order's Parisian house became known as 'les Mathurins' after the saint — connecting Maturinus's name with one of medieval France's important charitable institutions."}
    ],
    "places": [
      {"name": "Larchant, Seine-et-Marne, France", "role": "The centre of the Saint Mathurin cult — the town where he was venerated, where his relics were kept, and where the major pilgrimage church was built"},
      {"name": "Gâtinais region, north-central France", "role": "The territory of Maturinus's missionary activity — the region he is credited with Christianising in the late Roman period"}
    ],
    "subjects": ["Early Christianity", "French Saints", "Classical Era", "France", "Medieval Pilgrimage", "Hagiography", "Late Roman Gaul", "Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Saint Maturinus (Mathurin) was a late Roman Christian saint associated with Larchant in northern France — his cult produced one of the significant medieval pilgrimage sites of the Île-de-France and gave his name to French charitable institutions for the mentally ill ('Maisons de Mathurins'). The 13th-century Gothic church of Saint-Mathurin at Larchant reflects the pilgrimage cult's medieval importance and royal patronage.",
      "significanceCategory": "local"
    }
  }
},

"federico-savelli": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220federico-savelli.json",
  "slug": "federico-savelli",
  "data": {
    "summary": "Federico Savelli (died 19 December 1649) was an Italian aristocrat and military commander (condottiere) from the ancient Roman nobility — a member of the Savelli family, one of the oldest and most distinguished Roman baronial dynasties, whose roots went back to the medieval Roman nobility of the Alban Hills region. The Savelli were one of Rome's most significant baronial families of the medieval and early modern periods, producing popes (Honorius III, Honorius IV), cardinals, and military commanders, and owning vast estates in the Castelli Romani (the hill towns southeast of Rome). Federico Savelli represents the family in its late phase — a member of the old Roman nobility navigating the political and military world of early modern Italy.\n\nFederico Savelli served as a military commander in the service of various Italian powers and the Holy Roman Empire — the typical career path for members of the Roman baronial nobility in the early modern period, when the political fragmentation of Italy made military service to foreign powers the primary career option for Roman noble families outside the church. He served in campaigns associated with the Thirty Years' War (1618–1648) — the great pan-European conflict that devastated central Europe and in which Italian military commanders frequently served as mercenary generals in the armies of various powers. As a condottiere of the later Roman nobility, Federico Savelli exemplifies the long tradition of Roman aristocratic military service that stretched back to the medieval condottiere system.\n\nThe Savelli family's decline in the late 17th century — their eventual extinction of the main line and the sale of their estates — marks the end of one of Rome's most ancient noble dynasties, a process characteristic of the broader decline of the old Roman baronial nobility in the early modern period as the papacy consolidated its territorial control and the medieval aristocratic independence of the Roman barons was increasingly curtailed.",
    "causes": [
      "The Savelli family's ancient landed wealth and aristocratic status in the Alban Hills region of Lazio — their control of Castel Gandolfo (before its acquisition by the papacy), Albano, and other Castelli Romani estates — provided the resources and status that sustained Federico's career as a military commander.",
      "The political fragmentation of early modern Italy — the absence of a unified Italian state and the dominance of foreign powers (Spain, France, Austria) — made military service to foreign patrons the primary career option for Italian aristocrats who did not enter the church, producing the condottiere tradition that Federico Savelli continued.",
      "The Thirty Years' War (1618–1648) — the massive central European conflict — created enormous demand for military commanders and soldiers from all parts of Europe, drawing Italian condottieri including Savelli into service in the armies fighting across the Rhine and Danube theatres."
    ],
    "effects": [
      "Federico Savelli's military service contributed to the condottiere tradition's final phase — the late-medieval and early modern Italian military commander system's persistence into the era of the Thirty Years' War, even as national armies and professional standing forces increasingly displaced the old mercenary system.",
      "The Savelli family's trajectory — from medieval baronial power to the extinction of their main line in the late 17th century — illustrates the broader decline of the old Roman baronial nobility, as papal territorial consolidation and the social transformations of the Counter-Reformation reshaped Roman aristocratic society.",
      "The succession of Federico Savelli by later family members and the eventual sale of the Savelli estates (including Castel Gandolfo to the papacy) marked the end of the family's independent landed power in the Alban Hills — a process of aristocratic decline typical of the late-feudal Roman noble class."
    ],
    "relationships": [
      {"sourceSlug": "federico-savelli", "sourceName": "Federico Savelli", "verb": "MEMBER_OF", "targetSlug": "savelli-family", "targetName": "Savelli Family (Roman Barons)", "context": "Federico was a member of the Savelli — one of Rome's oldest baronial dynasties, producers of popes and military commanders, whose ancient estates in the Castelli Romani gave them their medieval and early modern power."},
      {"sourceSlug": "thirty-years-war", "sourceName": "Thirty Years' War (1618–1648)", "verb": "EMPLOYS", "targetSlug": "federico-savelli", "targetName": "Federico Savelli", "context": "Federico Savelli served as a military commander in campaigns associated with the Thirty Years' War — the pan-European conflict that drew Italian condottieri into service in various armies."},
      {"sourceSlug": "condottiere-tradition", "sourceName": "Italian Condottiere Tradition", "verb": "SHAPES", "targetSlug": "federico-savelli", "targetName": "Federico Savelli", "context": "Federico Savelli was a product of the Italian condottiere tradition — the Roman baronial nobility's career as military commanders in service to various powers that characterised the late medieval and early modern period."}
    ],
    "places": [
      {"name": "Rome and Castelli Romani, Lazio, Italy", "role": "The base of the Savelli family's power — their ancient estates in the Alban Hills southeast of Rome, including Albano and other hill towns"},
      {"name": "Central Europe (Thirty Years' War theatre)", "role": "The military theatre of Federico Savelli's campaigns — the central European battlefields of the 1618–1648 conflict in which Italian condottieri served"}
    ],
    "subjects": ["Italian Nobility", "Condottiere", "Early Modern Era", "Italy", "Roman Aristocracy", "Early Modern History", "Thirty Years War", "Papal States"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Federico Savelli (died 1649) was a member of the ancient Roman Savelli baronial dynasty — condottiere and military commander active in the Thirty Years' War era. He represents the late phase of one of Rome's most ancient noble families, whose subsequent extinction and estate sales marked the end of medieval Roman baronial independence under papal territorial consolidation.",
      "significanceCategory": "local"
    }
  }
},

"jayavarman-kaundinya": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221jayavarman-kaundinya.json",
  "slug": "jayavarman-kaundinya",
  "data": {
    "summary": "Jayavarman (also identified as Jayavarman Kaundinya; died c. 514 CE) was an early king of the Funan kingdom — the first major organised polity in mainland Southeast Asia, centred in the lower Mekong delta (modern Cambodia and southern Vietnam) — and a figure of significant importance in the Indianisation of Southeast Asia. The name 'Kaundinya' connects him to the legendary founding tradition of Funan: according to Chinese chronicles and Cham inscriptions, the earliest rulers of Funan were associated with a legendary Indian Brahmin named Kaundinya who arrived by sea, married a local princess (sometimes called Soma or Willow-Leaf), and founded the royal dynasty — a founding myth that embodied the process of Indian cultural influence on the Southeast Asian coastal kingdoms.\n\nThe historical Jayavarman who died c. 514 CE was a late king of the Funan period whose reign is documented primarily through Chinese dynastic chronicles (the Liang Shu and Wei Shu) that record diplomatic missions between Funan and the Chinese courts of the Northern and Southern dynasties period. These missions — the exchange of diplomatic gifts, tribute, and occasionally monks between Funan and the Chinese courts — are among the primary documentary evidence for Funan's history, since the kingdom left few indigenous inscriptions. Jayavarman's reign falls in the period when Funan was beginning the transition that would eventually lead to its replacement by the Khmer Chenla kingdom (late 6th century CE).\n\nFunan was a maritime trading power of major significance: positioned at the junction of the maritime trade routes connecting the Indian Ocean world with the South China Sea, its ports facilitated the exchange of Indian, Chinese, and Southeast Asian goods and the transmission of Indian cultural, religious, and administrative influences (Hinduism, Buddhism, Sanskrit literacy, Indian legal traditions) that fundamentally shaped the subsequent Khmer and other Southeast Asian civilisations. Jayavarman's reign was a late moment of this formative period of Southeast Asian Indianisation.",
    "causes": [
      "The Indian Ocean maritime trade network — the monsoon-driven exchange of goods between India, Persia, Arabia, and Southeast Asia and China — positioned Funan's lower Mekong delta ports as major trans-shipment points, generating the commercial wealth that sustained the Funan state and funded its cultural and political development.",
      "The Indianisation process — the voluntary adoption of Indian religious (Hindu and Buddhist), administrative, and cultural norms by Southeast Asian elites — created the political ideology and legitimating framework of the Funan kingdom, with rulers like Jayavarman incorporating Indian royal titulature and the Kaundinya founding legend into their dynasties.",
      "The pressure of the nascent Khmer Chenla polity — developing in the middle Mekong region north of Funan — was beginning to challenge Funan's dominance in the late 5th–early 6th century, creating the political context for the transitions of Jayavarman's reign."
    ],
    "effects": [
      "Jayavarman's reign contributed to the consolidation of Funan as a kingdom sufficiently organised and prestigious to exchange regular diplomatic missions with the Chinese courts — missions documented in the Chinese chronicles that provide the primary evidence for Funan's late history.",
      "Funan's Indianisation legacy — the cultural, religious, and administrative patterns established during the Funan period (including Jayavarman's reign) — fundamentally shaped the subsequent Khmer empire and the other Southeast Asian polities that followed, making the Funan period foundational for the civilisational history of mainland Southeast Asia.",
      "The transition from Funan to Chenla that began in the late 6th century — following the reign of Jayavarman and his successors — was the foundational transformation that led to the Khmer empire of Angkor, one of the greatest civilisations of Southeast Asian history."
    ],
    "relationships": [
      {"sourceSlug": "jayavarman-kaundinya", "sourceName": "Jayavarman Kaundinya", "verb": "RULES", "targetSlug": "funan-kingdom", "targetName": "Funan Kingdom (Southeast Asia)", "context": "Jayavarman was a late king of Funan — the first major Indianised kingdom of mainland Southeast Asia, whose diplomatic relations with China are documented in the Chinese dynastic chronicles."},
      {"sourceSlug": "kaundinya-legend", "sourceName": "Kaundinya Founding Legend", "verb": "LEGITIMATES", "targetSlug": "jayavarman-kaundinya", "targetName": "Jayavarman Kaundinya", "context": "The Kaundinya dynasty name — the legendary Indian Brahmin founder of Funan who married a local princess — provided the dynastic legitimacy for rulers like Jayavarman in the Funan tradition."},
      {"sourceSlug": "funan-kingdom", "sourceName": "Funan Kingdom", "verb": "PRECEDES", "targetSlug": "khmer-empire", "targetName": "Khmer Empire (Angkor)", "context": "Funan's Indianisation — consolidated during rulers like Jayavarman — provided the cultural and political foundations for the subsequent Khmer Chenla and Angkor civilisations."}
    ],
    "places": [
      {"name": "Funan (lower Mekong delta, Cambodia/Vietnam)", "role": "Jayavarman's kingdom — the first major Indianised polity of mainland Southeast Asia, a maritime trading power positioned at the junction of Indian Ocean and South China Sea routes"},
      {"name": "Southeast Asia / Mekong Delta", "role": "The broader context of Funan civilisation — the mainland Southeast Asian zone where Indian cultural influence and indigenous traditions combined to produce the foundations of Khmer and other Southeast Asian civilisations"}
    ],
    "subjects": ["Southeast Asian History", "Funan Kingdom", "Classical Era", "Cambodia", "Indianisation", "Ancient History", "Maritime Trade", "Early Southeast Asia"],
    "frameworks": ["CULTURAL_TRANSMISSION", "WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Jayavarman Kaundinya was a late king of Funan (died c. 514 CE) — the first major Indianised kingdom of mainland Southeast Asia, whose diplomatic missions to China are documented in Chinese dynastic chronicles. His reign falls in the formative Indianisation period that established the cultural and political foundations of the subsequent Khmer empire and the broader Southeast Asian civilisational tradition.",
      "significanceCategory": "regional"
    }
  }
},

"sarduri-iii": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221sarduri-iii.json",
  "slug": "sarduri-iii",
  "data": {
    "summary": "Sarduri III (died c. 624 BCE) was King of Urartu — the ancient kingdom centred on the Lake Van region of what is now eastern Turkey, Armenia, and northwestern Iran — who ruled in the late 7th century BCE during a period of severe external pressure from Assyrian and later Median power. Urartu (also known as the Kingdom of Van, or Biainili in the native language) was one of the most powerful states of the ancient Near East in the 9th–7th centuries BCE — a formidable military rival of Assyria, a major metallurgical centre (Urartian bronze and ironwork was famous throughout the ancient world), and the creator of an impressive architectural tradition (including the citadel-city of Tushpa/Van and major canal systems).\n\nSarduri III's reign falls in the terminal phase of Urartian independent power — the period when the combined pressure of Assyrian military campaigns (particularly those of Sargon II in 714 BCE, who sacked the Urartian religious centre of Musasir) and the emerging power of the Medes and the Cimmerians was progressively undermining Urartian strength. The kingdom of Urartu had been in relative decline since Rusa I's defeat by Sargon II in the 714 BCE campaign, though it continued to maintain significant power and conduct construction projects. Sarduri III was among the last rulers of an independent Urartian state before the kingdom was eventually overwhelmed — possibly by the Medes and Scythians — in the late 7th or early 6th century BCE, with the destruction of Tushpa (Van) ending the Urartian state.\n\nUrartian civilisation is significant both for its own achievements — its metallurgy, architecture, hydraulic engineering, and distinctive cuneiform inscriptions in the Urartian language — and as the cultural predecessor and partial founder of Armenian civilisation. The Armenians' emergence as a distinct people in the former Urartian territory after the kingdom's fall owed much to Urartian population, language influence, and cultural memory.",
    "causes": [
      "The Assyrian military campaigns against Urartu — particularly Sargon II's devastating campaign of 714 BCE that sacked the Urartian religious centre of Musasir — weakened the Urartian kingdom and set it on a path of relative decline that continued through Sarduri III's reign.",
      "The emergence of the Medes as a major Near Eastern power in the late 7th century BCE — combined with Scythian and Cimmerian pressure from the north — created new military threats to Urartu that compounded the existing Assyrian pressure and eventually ended Urartian independence.",
      "Urartu's geopolitical position at the junction of Anatolia, the Caucasus, and the Mesopotamian world — simultaneously attractive to multiple great powers as a buffer zone, trade corridor, and resource-rich territory — made it perpetually vulnerable to the competing imperial ambitions of its neighbours."
    ],
    "effects": [
      "The fall of the Urartian kingdom (c. early 6th century BCE) — of which Sarduri III was a penultimate ruler — cleared the way for the consolidation of Median power in the Zagros and eastern Anatolia and for the emergence of the Armenian people in the former Urartian territory.",
      "Urartian metallurgical technology — the bronze and iron working traditions that made Urartian metalwork famous across the ancient Near East — was transmitted to successor cultures in the Caucasus and Anatolia, contributing to the technological heritage of the region.",
      "The Urartian architectural and hydraulic engineering tradition — including the canal systems and citadel-building techniques developed during the Urartian kingdom — influenced the populations who inherited the Urartian landscape and contributed to the later Armenian and Caucasian building traditions."
    ],
    "relationships": [
      {"sourceSlug": "sarduri-iii", "sourceName": "Sarduri III", "verb": "RULES", "targetSlug": "kingdom-of-urartu", "targetName": "Kingdom of Urartu", "context": "Sarduri III was one of the last independent kings of Urartu — ruling during the terminal phase of the kingdom's existence as it faced Assyrian, Median, and nomadic pressure."},
      {"sourceSlug": "assyrian-empire", "sourceName": "Assyrian Empire", "verb": "PRESSURES", "targetSlug": "sarduri-iii", "targetName": "Sarduri III / Urartu", "context": "The Assyrian military campaigns — particularly Sargon II's 714 BCE sack of Musasir — had weakened Urartu before Sarduri III's reign, creating the declining power context of his rule."},
      {"sourceSlug": "median-empire", "sourceName": "Median Empire", "verb": "THREATENS", "targetSlug": "kingdom-of-urartu", "targetName": "Urartu (including Sarduri III)", "context": "The Medes' rise as a major power in the late 7th century BCE was one of the key external pressures that ended Urartian independence — the Median expansion that destroyed or absorbed Urartu's remnant state."}
    ],
    "places": [
      {"name": "Tushpa (Van), eastern Anatolia (Turkey)", "role": "The capital of Urartu — the citadel-city on Lake Van that was the centre of Urartian power and Sarduri III's royal seat"},
      {"name": "Lake Van region (eastern Turkey/Armenia/Iran)", "role": "The core territory of the Urartian kingdom — the volcanic plateau between the Euphrates and the Caspian Sea that Urartu controlled at its height"}
    ],
    "subjects": ["Ancient Near East", "Urartu", "Classical Era", "Anatolia", "Ancient Warfare", "Ancient History", "Armenia", "Iron Age"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Sarduri III was one of the last kings of Urartu (died c. 624 BCE) — the ancient Near Eastern kingdom centred on Lake Van that was a major rival of Assyria and the cultural predecessor of Armenian civilisation. His reign falls in the terminal phase of Urartian independence as Assyrian decline and Median expansion ended the kingdom's power, making him a witness to the end of one of the ancient Near East's most distinctive civilisations.",
      "significanceCategory": "regional"
    }
  }
},

"eusebius": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250eusebius.json",
  "slug": "eusebius",
  "data": {
    "summary": "Pope Eusebius (died c. 17 August 310 CE) was Bishop of Rome from approximately April to August 309 CE (or 309–310 CE) — one of the shortest-reigning popes in history, whose brief pontificate was torn apart by a violent schism within the Roman Christian community over the treatment of the lapsi (Christians who had apostatised under the Diocletianic persecution of 303–312 CE, and who were now seeking readmission to the church). Eusebius is regarded as a saint in the Catholic Church; his feast day is 17 August.\n\nThe schism that destroyed Eusebius's papacy centred on the figure of Heraclius, who led a faction within the Roman church that demanded unconditional and immediate readmission of the lapsi without penance. Eusebius insisted on a programme of defined penance as the condition for reconciliation — a position aligned with the broader western church's emerging tradition of penitential discipline that would be codified by later canon law. The conflict between the two factions was literally violent: physical fighting in the Roman churches between the Eusebian and Heraclian factions prompted the Emperor Maxentius to exile both Eusebius and Heraclius to Sicily, where Eusebius died shortly after his arrival. This exile — prompted by civil disorder, not religious persecution — is documented in the contemporary epigrammatic epitaph composed for Eusebius by his successor Pope Damasus I, which is one of the primary sources for the events.\n\nThe Eusebian controversy is significant beyond its immediate context as an early episode in the western church's development of penitential theology and the principle of conditional reconciliation — the tradition that would lead through Cyprian of Carthage's treatise 'De Lapsis' and ultimately to the systematic penitential discipline of medieval canon law. Pope Eusebius's defence of penance against the 'laxist' faction of Heraclius represents an early moment in this long tradition.",
    "causes": [
      "The Diocletianic persecution (303–312 CE) — the last and most severe Roman imperial persecution of Christianity — produced thousands of lapsi (apostates) across the empire whose status and path to reconciliation became one of the most divisive questions of early 4th century church life.",
      "The fundamental disagreement about Christian identity and the church's boundaries — between rigourists who saw apostasy as an unforgivable sin and reconciliationists who insisted on the church's power to absolve even the worst sins through penance — created the theological fault line that the Heraclian schism exploited.",
      "The Roman church's internal diversity and the lack of effective mechanisms for resolving community disputes (in a period before the papacy had developed its later monarchical authority) allowed the schism between Eusebius and Heraclius to escalate into physical violence that required imperial intervention."
    ],
    "effects": [
      "Eusebius's defence of conditional reconciliation for the lapsi — requiring penance before readmission — contributed to the western church's developing tradition of penitential theology, anticipating the more systematic treatment of the lapsi question by Cyprian of Carthage and ultimately the canonical penitential system.",
      "The exile and death of Eusebius demonstrated both the fragility of early papal authority (the bishop of Rome could be exiled by a pagan emperor for causing public disorder) and the intensity of doctrinal disputes within the Roman Christian community — illustrating the contested nature of early Christian identity.",
      "Pope Damasus I's epitaph for Eusebius — composed in verse — is one of the earliest examples of papal commemoration of martyred/confessorial predecessors, contributing to the Roman papacy's developing tradition of celebrating its martyred history and establishing the spiritual authority of the see."
    ],
    "relationships": [
      {"sourceSlug": "eusebius", "sourceName": "Pope Eusebius", "verb": "OPPOSES", "targetSlug": "heraclius-laxist", "targetName": "Heraclius (Laxist Faction)", "context": "The conflict between Eusebius (who required penance for the lapsi) and Heraclius (who demanded immediate unconditional readmission) tore the Roman church apart and led to both men being exiled to Sicily."},
      {"sourceSlug": "diocletianic-persecution", "sourceName": "Diocletianic Persecution (303–312 CE)", "verb": "CREATES_CRISIS_FOR", "targetSlug": "eusebius", "targetName": "Pope Eusebius", "context": "The Diocletianic persecution produced the lapsi whose reconciliation was the central controversy of Eusebius's brief papacy — the question that split the Roman church into violent factions."},
      {"sourceSlug": "damasus-i", "sourceName": "Pope Damasus I", "verb": "COMMEMORATES", "targetSlug": "eusebius", "targetName": "Pope Eusebius", "context": "Pope Damasus I composed a verse epitaph for Eusebius that is the primary contemporary source for the events of his papacy — one of the earliest examples of papal commemoration of martyred predecessors."}
    ],
    "places": [
      {"name": "Rome", "role": "The scene of Eusebius's brief papacy and the violent factional conflict over the lapsi — the city from which both Eusebius and Heraclius were exiled by Emperor Maxentius"},
      {"name": "Sicily, Roman Empire", "role": "The place of Eusebius's exile and death — where Emperor Maxentius sent him after the violent disorder in Rome, and where he died shortly after arriving"}
    ],
    "subjects": ["Early Christianity", "Papal History", "Classical Era", "Italy", "Early Church", "4th Century CE", "Roman Church", "Penitential Theology"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Pope Eusebius (died 310 CE) had one of the shortest and most turbulent pontificates in early church history — his papacy was destroyed by violent schism over the readmission of lapsed Christians, leading to his exile to Sicily where he died. His defence of penitential requirements for the lapsi was an early moment in the western church's development of canonical penitential theology, and Pope Damasus I's verse epitaph for him is a primary source for the events.",
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
