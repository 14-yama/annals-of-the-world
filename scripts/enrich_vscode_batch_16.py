#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 16 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: gordas, jiong-of-xia, william-ii-of-narbonne, anterus,
          hammad-ibn-salama, pha-mueang, confucianism, ecology
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-16-may2026"

ENRICHMENTS = {

"gordas": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221gordas.json",
  "slug": "gordas",
  "data": {
    "summary": "Gordas (also Gord or Grod; fl. c. 527–528 CE) was a king of the Kutrigur Huns — one of the fragmented successor peoples of Attila's Hunnic Empire, who by the 6th century inhabited the steppes north of the Black Sea — who converted to Christianity and formed an alliance with the Byzantine Empire under Emperor Justin I (518–527 CE) before being overthrown and killed by his own people. The Kutrigur Huns were a Eurasian steppe people who, after the collapse of Attila's empire in 453 CE, maintained a nomadic polity in the Pontic steppe north of the Danube and the Black Sea, raiding the Balkans and occasionally fighting as Byzantine federates.\n\nGordas's conversion to Christianity and his alliance with Byzantium were recorded by the Byzantine historian Procopius of Caesarea (in his 'Wars' and 'Secret History'). According to Procopius, Gordas visited Constantinople (c. 527–528 CE), was baptised there with Justin I as his godfather, received honours and gifts, and returned to his people as a Byzantine ally. He then made the politically fatal mistake of melting down the silver and electrum cult idols of his people and selling the metal to Byzantine merchants — a direct assault on Hunnic religious practice that his brother Muageris used as the occasion for a coup. Gordas was killed, Muageris became king, and the Kutrigurs reverted to paganism and resumed raiding Byzantine territory.\n\nGordas's story is a revealing episode in the Byzantine Empire's strategy of managing steppe peoples through religious conversion, imperial patronage, and the creation of client relationships — a policy pursued consistently from the reign of Constantine onward. His failure illustrates the limits of this strategy: religious and political transformation imposed from above without popular support could trigger violent backlash, and the Byzantine imperial model of Christianisation-as-client-creation was not always transferable across the cultural divide between the agrarian empire and the nomadic steppe.",
    "causes": [
      "The Byzantine Empire's consistent policy of converting neighbouring peoples to Christianity as a tool of diplomacy and client-building — exemplified by Justin I's sponsorship of Gordas's baptism and his reception as an imperial protégé — created the context for Gordas's religious and political transformation.",
      "The post-Attilanic fragmentation of the Hunnic peoples into successor groups (Kutrigurs, Utigurs, and others) left these steppe polities competing for power and resources, making Byzantine alliance and patronage an attractive option for ambitious leaders like Gordas seeking an edge over rivals.",
      "The theological and cultural incompatibility between Gordas's adopted Christianity and the traditional Hunnic religious culture — centred on the metallic cult idols whose destruction he ordered — created the flash point that his brother Muageris exploited to overthrow him."
    ],
    "effects": [
      "Gordas's overthrow and the reversion of the Kutrigurs to paganism and raiding demonstrated the limits of Byzantine religious conversion as a diplomatic tool — when a converted client king attempted to impose the religious transformation on his people, the result was a coup and the resumption of Byzantine-Hunnic hostility.",
      "The Gordas episode reinforced the Byzantine Empire's understanding that steppe conversion was a generational process rather than a royal decision — a lesson applied in subsequent Byzantine missionary strategies that emphasised gradual community-level evangelisation.",
      "Gordas's fate exemplified the precarious position of nomadic leaders who aligned too closely with Byzantine culture and imperial demands — becoming caught between the demands of their imperial patron and the expectations of their own people, a structural tension that recurred throughout Byzantine steppe diplomacy."
    ],
    "relationships": [
      {"sourceSlug": "gordas", "sourceName": "Gordas (Kutrigur King)", "verb": "ALLIES_WITH", "targetSlug": "justin-i", "targetName": "Justin I (Byzantine Emperor)", "context": "Gordas visited Constantinople, was baptised with Justin I as his godfather, and became a Byzantine client king — an alliance that ended with his overthrow by his pagan brother Muageris."},
      {"sourceSlug": "gordas", "sourceName": "Gordas", "verb": "OVERTHROWN_BY", "targetSlug": "muageris", "targetName": "Muageris (Brother)", "context": "Muageris used Gordas's destruction of Hunnic cult idols as the pretext for a coup — killing Gordas, taking the Kutrigur kingship, and reversing his brother's Christianisation and Byzantine alliance."},
      {"sourceSlug": "byzantine-empire", "sourceName": "Byzantine Empire", "verb": "CONVERTS", "targetSlug": "gordas", "targetName": "Gordas (and Kutrigur Huns)", "context": "The Byzantine conversion of Gordas exemplified the imperial strategy of Christianising steppe leaders as a tool of client-building and frontier management — a policy with mixed results."}
    ],
    "places": [
      {"name": "Constantinople (Istanbul), Byzantine Empire", "role": "The site of Gordas's baptism and imperial reception — the Byzantine capital where Justin I sponsored his conversion and alliance"},
      {"name": "Pontic Steppe (north of Black Sea)", "role": "The homeland of the Kutrigur Huns and the scene of Gordas's subsequent overthrow — the steppe zone that was the operational environment of the post-Attilanic Hunnic peoples"}
    ],
    "subjects": ["Byzantine History", "Hunnic Peoples", "Classical Era", "Steppe Peoples", "Late Antiquity", "Christianisation", "Early Medieval History", "Roman Frontier"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Gordas was the first Kutrigur Hunnic king to convert to Christianity (c. 527–528 CE), creating a Byzantine client relationship before being overthrown by his brother Muageris for destroying traditional Hunnic cult idols. His story is a revealing case study in the limits of Byzantine religious diplomacy and the structural tensions faced by steppe leaders who adopted Byzantine imperial culture.",
      "significanceCategory": "regional"
    }
  }
},

"jiong-of-xia": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221jiong-of-xia.json",
  "slug": "jiong-of-xia",
  "data": {
    "summary": "Jiong of Xia (also written Jiong; fl. c. 2000 BCE, traditional chronology) was a legendary ruler in the traditional Chinese historical sequence of the Xia dynasty — the first dynasty in Chinese historical tradition, whose historicity has been a subject of scholarly debate between those who accept the traditional accounts and those who regard the Xia as legendary. In the traditional chronology preserved in the 'Records of the Grand Historian' (Shiji) by Sima Qian (c. 100 BCE), Jiong appears as one of the later rulers of the Xia, succeeding in the dynastic line that traces back to the legendary founder Yu the Great, who is credited with taming the great floods of ancient China.\n\nThe Xia dynasty (traditionally c. 2070–1600 BCE) occupies a crucial position in Chinese historical memory: it is the dynasty that bridges the era of legendary sage-rulers (Yao, Shun, and Yu) and the historically more documented Shang dynasty (c. 1600–1046 BCE). Whether the Xia dynasty as described in Chinese historical texts represents an actual Bronze Age polity, a legendary confederation of Neolithic cultures, or a later invention of Zhou-era historiography remains one of the central debates in Chinese archaeology. The discovery and excavation of Erlitou culture sites (c. 1900–1500 BCE) in the Yellow River valley — with their palace complexes, bronze artefacts, and signs of political centralisation — has led many scholars to identify Erlitou as the Xia civilisation, though the identification remains contested.\n\nJiong of Xia, like most rulers in the traditional Xia king list, is a name without independently datable documentation — his existence depends on the accuracy of the traditional historical lists transmitted through Chinese court historiography. His significance lies primarily as an entry in the record of China's claimed dynastic continuity — the unbroken sequence of dynasties from Xia through Shang, Zhou, and beyond that was central to Chinese political legitimacy and historical consciousness.",
    "causes": [
      "The traditional Chinese historical framework — the dynastic sequence preserved through court historiography from the Zhou period onward — systematised the memory (or construction) of the Xia rulers as part of the legitimate dynastic continuity that justified subsequent rulers' claims to the Mandate of Heaven.",
      "The Bronze Age political development of the Yellow River valley — the emergence of complex stratified polities in the Erlitou culture period (c. 1900–1500 BCE) — may reflect the historical reality underlying the Xia dynasty tradition, even if individual rulers like Jiong cannot be independently documented.",
      "The Chinese tradition of ancestor veneration and dynastic legitimacy — in which the ability to trace one's dynasty to the Xia founder Yu the Great and through him to the sage-rulers Yao and Shun was politically significant — motivated the preservation and elaboration of the Xia king lists by later dynasties."
    ],
    "effects": [
      "The Xia dynasty tradition — including the king list that preserved Jiong's name — became the foundation of Chinese dynastic historiography and the concept of legitimacy through unbroken dynastic succession, a framework that structured Chinese political culture for three thousand years.",
      "The scholarly and archaeological debate about the Xia dynasty's historicity — catalysed by the discovery of Erlitou culture and the ongoing 'Xia-Shang-Zhou Chronology Project' (1996–2000) — has made the question of pre-Shang Chinese civilisation one of the most active areas of Chinese archaeological research.",
      "Jiong's position in the Xia king list represents the broader phenomenon of legendary rulers in Chinese historical tradition whose names were preserved through ritual and historiographical practice even when their independent historical existence could not be verified."
    ],
    "relationships": [
      {"sourceSlug": "jiong-of-xia", "sourceName": "Jiong of Xia", "verb": "BELONGS_TO", "targetSlug": "xia-dynasty", "targetName": "Xia Dynasty (China)", "context": "Jiong is one of the rulers listed in the traditional Xia dynasty king list — the sequence of rulers from Yu the Great preserved in Chinese historical tradition."},
      {"sourceSlug": "yu-the-great", "sourceName": "Yu the Great (Xia founder)", "verb": "PRECEDES", "targetSlug": "jiong-of-xia", "targetName": "Jiong of Xia", "context": "Yu the Great's legendary founding of the Xia dynasty — through his taming of the floods — is the origin point of the dynastic sequence in which Jiong appears as a later ruler."},
      {"sourceSlug": "shang-dynasty", "sourceName": "Shang Dynasty (c. 1600–1046 BCE)", "verb": "SUCCEEDS", "targetSlug": "xia-dynasty", "targetName": "Xia Dynasty (including Jiong)", "context": "The Shang dynasty — the first Chinese dynasty with extensive contemporary written records (oracle bones) — succeeded the Xia in Chinese historical tradition, making the Xia the preliterate foundation of Chinese dynastic history."}
    ],
    "places": [
      {"name": "Yellow River Valley, Central China", "role": "The geographic setting of the traditional Xia dynasty — the loess plateau and river plain of central China where Erlitou culture evidence suggests Bronze Age political complexity"},
      {"name": "Erlitou (modern Henan province, China)", "role": "The main archaeological site identified by many scholars as the Xia capital — providing the physical evidence used to argue for the historical reality of a Xia polity"}
    ],
    "subjects": ["Ancient China", "Chinese Dynasties", "Classical Era", "Bronze Age", "Chinese History", "Ancient History", "Xia Dynasty", "Chinese Historiography"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Jiong of Xia is a ruler in the traditional Xia dynasty king list (c. 2000 BCE) — one of the legendary pre-Shang rulers whose existence depends on the accuracy of Chinese court historiography. His significance lies in his place in the dynastic sequence that forms the foundation of Chinese historical memory and political legitimacy.",
      "significanceCategory": "local"
    }
  }
},

"william-ii-of-narbonne": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221william-ii-of-narbonne.json",
  "slug": "william-ii-of-narbonne",
  "data": {
    "summary": "William II of Narbonne (died 26 August 1424) was the last Viscount of Narbonne from the Viscount dynasty — the final holder of the medieval viscountcy of Narbonne, a significant feudal lordship in Languedoc in southern France centred on the important Mediterranean port city of Narbonne. His death in 1424 without a direct heir ended the viscountcy as an independent title, and Narbonne eventually came under the direct control of the French Crown (it was purchased by the Crown in 1507). William II's tenure as Viscount falls in the context of the late medieval crisis in the Languedoc region — a period of political fragmentation, English-French conflict (Hundred Years War), and the social disruptions following the Black Death.\n\nNarbonne was one of the most historically significant cities of southern France: a major Roman city (Narbo Martius, founded 118 BCE, the first Roman colony in Gaul), the capital of the Roman province of Gallia Narbonensis, a significant medieval Muslim settlement (controlled by the Saracens 719–759 CE), an important ecclesiastical centre with an archbishopric, and a major Mediterranean trading port. The Viscounts of Narbonne had exercised semi-autonomous power over the city and its region since the 9th century — one of the great southern French feudal dynasties who maintained their independence amid the competing claims of the Counts of Toulouse, the Kings of Aragon, and the French Crown.\n\nWilliam II's final years as Viscount coincided with the critical phase of the Hundred Years War following the Battle of Agincourt (1415) — a period when English power in France reached its peak and when the Treaty of Troyes (1420) had disinherited the Dauphin Charles (later Charles VII) in favour of Henry V of England. The political situation of Languedoc in these years was shaped by competing loyalties and the broader crisis of French royal authority.",
    "causes": [
      "The dynastic accident of William II's failure to produce a legitimate heir — combined with the broader weakening of the medieval viscountcy system as the French Crown steadily absorbed independent lordships — created the conditions for the extinction of the Narbonne viscountcy as an independent title.",
      "The Hundred Years War's disruption of southern French political life — the competing claims of English and French factions, the taxation demands of both sides, and the general instability that weakened independent feudal lordships — shaped the challenging context of William II's final years.",
      "The long-term trajectory of French royal centralisation — the steady absorption of independent feudal territories into the royal domain that accelerated after Charles VII's recovery of France from English control — was the structural force that made the eventual incorporation of Narbonne into the Crown domain inevitable."
    ],
    "effects": [
      "William II's death without an heir ended the viscountcy of Narbonne as an independent feudal institution — the line of viscounts that had governed the city since the 9th century came to an end, initiating the process by which Narbonne was eventually absorbed into the French royal domain.",
      "The extinction of the Narbonne viscountcy was one instance in the broader consolidation of French royal power in Languedoc that transformed the region from a semi-autonomous feudal mosaic into a more directly governed part of the French kingdom in the 15th century.",
      "The end of the Narbonne viscountcy contributed to the decline of Narbonne's status as an independent political centre — the city eventually lost its role as a major independent port and ecclesiastical capital as it was absorbed into the French administrative system."
    ],
    "relationships": [
      {"sourceSlug": "william-ii-of-narbonne", "sourceName": "William II of Narbonne", "verb": "RULES", "targetSlug": "viscountcy-of-narbonne", "targetName": "Viscountcy of Narbonne", "context": "William II was the last Viscount of Narbonne — his death in 1424 without an heir ended the viscountcy as an independent feudal title."},
      {"sourceSlug": "hundred-years-war", "sourceName": "Hundred Years War (1337–1453)", "verb": "CONTEXTUALISES", "targetSlug": "william-ii-of-narbonne", "targetName": "William II of Narbonne", "context": "William II's final years as Viscount coincided with the most intense phase of the Hundred Years War — the period of English supremacy after Agincourt that destabilised French political life including in Languedoc."},
      {"sourceSlug": "french-crown", "sourceName": "French Crown (Capetian/Valois)", "verb": "ABSORBS", "targetSlug": "viscountcy-of-narbonne", "targetName": "Viscountcy of Narbonne (after William II)", "context": "Following William II's death, the viscountcy came under Crown control — Narbonne was purchased by the French Crown in 1507, completing the absorption of this formerly independent Languedoc lordship."}
    ],
    "places": [
      {"name": "Narbonne, Languedoc, France", "role": "The capital and core territory of William II's viscountcy — the ancient Roman city, medieval port, and archiepiscopal centre whose viscountcy ended with his death"},
      {"name": "Languedoc, Southern France", "role": "The broader regional context — the southern French zone of Occitan culture and semi-independent feudal lordships within which the Narbonne viscountcy was one significant element"}
    ],
    "subjects": ["Medieval France", "Medieval Feudalism", "Classical Era", "Languedoc", "Southern France", "Hundred Years War", "Medieval History", "French History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "William II of Narbonne (died 1424) was the last Viscount of Narbonne — his death ended the viscountcy that had governed this historically significant Mediterranean city since the 9th century. His significance lies primarily in his role as the final holder of an important Languedoc feudal title whose extinction contributed to the French Crown's consolidation of southern France.",
      "significanceCategory": "local"
    }
  }
},

"anterus": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250anterus.json",
  "slug": "anterus",
  "data": {
    "summary": "Pope Anterus (died 3 January 236 CE) was the eighteenth Bishop of Rome and thus, by Catholic reckoning, the eighteenth pope — who served for only 43 days (21 November 235–3 January 236 CE), making his one of the shortest pontificates in papal history. Anterus was elected to succeed Pope Pontian, who had resigned the papacy after being condemned to labour in the mines of Sardinia by the Emperor Maximinus Thrax — one of the soldiers' emperors of the Crisis of the Third Century, whose hostility to Christianity initiated the first general imperial persecution of the Church.\n\nAnterus's brief pontificate — possibly ended by his own death in the mines as a confessor, or by natural causes — falls in the initial phase of the Decian-era persecutions and the broader crisis of the third century Roman Empire. His name suggests Greek origin (Anterus meaning 'the counter-Love' or from the flower antherion), consistent with the predominantly Greek character of the early Roman Christian community. He is venerated as a martyr in the Roman Catholic Church, though the evidence for his martyrdom is uncertain — the Liber Pontificalis (the official medieval register of popes) records that he died a martyr, but the historical documentation is very thin.\n\nAccording to the Liber Pontificalis, Anterus's brief pontificate was notable for one administrative action: he allegedly ordered the collection and archiving of the acts of the martyrs — the records of trials and executions of Christians — into a formal archive. If accurate, this would represent an early institutional step in the preservation of the hagiographic tradition that would eventually produce the Lives of the Saints. The historical reality of this action is uncertain, but the tradition reflects the growing institutional consciousness of the Roman church in the mid-3rd century, even under persecution.",
    "causes": [
      "The Emperor Maximinus Thrax's persecution of the Christian church — which had condemned Pope Pontian to the Sardinian mines and killed or exiled church leaders — created the crisis of succession and disruption that produced Anterus's emergency election to the papacy.",
      "The third-century crisis of the Roman Empire — the succession of soldier-emperors, military coups, and provincial instability that defined the period 235–284 CE — created the hostile imperial environment in which Anterus's brief pontificate occurred.",
      "The early Roman Church's growing institutional self-consciousness — the development of hierarchical organisation, episcopal authority, and record-keeping practices in the mid-3rd century — provided the context for the tradition that Anterus initiated the archiving of martyrs' acts."
    ],
    "effects": [
      "Anterus's pontificate — though only 43 days — maintained the continuity of the Roman episcopal succession during the Maximinus Thrax persecution, ensuring the institutional survival of the Roman church through one of its earliest phases of imperial hostility.",
      "The tradition that Anterus ordered the archiving of martyrs' acts — if it reflects any historical reality — contributed to the preservation of the hagiographic record that became the foundation of the Roman Martyrology and the cult of saints in the Western church.",
      "Anterus's martyrdom (or death during persecution) added his name to the early list of Roman bishop-martyrs that reinforced the authority and prestige of the Roman see — the tradition of papal martyrdom was a significant element of the Roman church's claim to apostolic primacy."
    ],
    "relationships": [
      {"sourceSlug": "anterus", "sourceName": "Pope Anterus", "verb": "SUCCEEDS", "targetSlug": "pontian", "targetName": "Pope Pontian", "context": "Anterus succeeded Pontian as Bishop of Rome after Pontian resigned the papacy following his condemnation to the Sardinian mines by Maximinus Thrax."},
      {"sourceSlug": "maximinus-thrax", "sourceName": "Maximinus Thrax (Emperor)", "verb": "PERSECUTES", "targetSlug": "anterus", "targetName": "Pope Anterus (and Early Church)", "context": "The Maximinus Thrax persecution — which had exiled Pontian — provided the hostile context within which Anterus's brief pontificate occurred and possibly caused his death."},
      {"sourceSlug": "early-roman-church", "sourceName": "Early Roman Church (3rd Century)", "verb": "MAINTAINS", "targetSlug": "anterus", "targetName": "Pope Anterus", "context": "Anterus maintained the Roman episcopal succession during the Maximinus persecution — a crucial function that preserved the institutional continuity of the Roman church through a dangerous period."}
    ],
    "places": [
      {"name": "Rome, Roman Empire", "role": "The site of Anterus's pontificate — the Roman church whose episcopal succession he maintained during the Maximinus Thrax persecution"},
      {"name": "Sardinia (mines)", "role": "The site of Pope Pontian's exile and death under Maximinus Thrax — the penal context that produced the vacancy Anterus was elected to fill"}
    ],
    "subjects": ["Early Christianity", "Papacy", "Classical Era", "Roman Empire", "Church History", "3rd Century CE", "Early Church Fathers", "Martyrs"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Pope Anterus (235–236 CE) was the 18th Bishop of Rome with one of the shortest pontificates in papal history (43 days) — elected to maintain the Roman episcopal succession during the Maximinus Thrax persecution. His significance lies in the institutional continuity he preserved during a dangerous period, and in the tradition that he initiated the archiving of martyrs' acts.",
      "significanceCategory": "local"
    }
  }
},

"hammad-ibn-salama": {
  "filepath": "data/appwrite-export/entities/241-Class-241/241hammad-ibn-salama.json",
  "slug": "hammad-ibn-salama",
  "data": {
    "summary": "Hammad ibn Salamah (c. 708–784 CE; Arabic: حَمَّاد بن سَلَمَة) was one of the most significant early Islamic scholars of hadith (sayings and actions attributed to the Prophet Muhammad), a pioneering figure in the systematic collection and transmission of religious traditions that formed the basis of Islamic jurisprudence and theology. He is particularly associated with the hadith traditions of Basra, the great Iraqi city that was one of the most important centres of early Islamic scholarship, where he studied under the first generation of transmitters and taught the generation that would produce the canonical hadith collections of the 9th century.\n\nHammad ibn Salamah was known for his mastery of multiple areas of Islamic religious scholarship: his collection of hadith was among the largest of his time (reportedly containing several thousand traditions), he was a specialist in Quranic recitation and interpretation, and he was significant in the development of Islamic grammar and Arabic linguistics. He was a student of Thabit al-Bunani (one of the most respected second-generation transmitters of hadith from Basra) and of Anas ibn Malik (the Prophet's personal servant, who was one of the most important direct transmitters of prophetic traditions) — his connection to Anas gave his transmissions an especially high status in Islamic hadith science, as it provided a near-direct chain of transmission to the Prophet.\n\nHammad ibn Salamah's scholarly life spanned the Umayyad-to-Abbasid transition — one of the most politically dramatic periods in early Islamic history, during which the Abbasid revolution of 750 CE overthrew the Umayyad caliphate and moved the capital from Damascus to the new city of Baghdad. He died in Basra in 784 CE, having spent his life in the scholarly community that was transforming the oral traditions of early Islam into the written corpus of hadith that would become the foundation of Sunni Islamic law and theology.",
    "causes": [
      "The enormous project of hadith collection and verification that consumed the second and third Islamic centuries — the systematic effort to preserve, transmit, and evaluate the traditions attributed to the Prophet Muhammad — created the scholarly environment within which Hammad ibn Salamah's career was spent.",
      "Hammad's privileged position as a student of Anas ibn Malik — one of the Prophet's companions and household servants, who was one of the last living direct transmitters of prophetic hadith in the late 7th–early 8th centuries — gave his scholarly work a special authority in the developing science of hadith transmission.",
      "The intellectual culture of Basra in the Umayyad and early Abbasid periods — a city that was simultaneously an Islamic scholarly centre, a major trade hub, and a crucible of Arabic literary and linguistic culture — provided the competitive scholarly environment that shaped Hammad's comprehensive learning across hadith, Quran, and linguistics."
    ],
    "effects": [
      "Hammad ibn Salamah's hadith transmissions — the traditions he collected, verified, and transmitted to his students — formed part of the foundational layer of the hadith corpus on which the 9th-century canonical collections (Sahih al-Bukhari, Sahih Muslim, and the four Sunan) were built, making him a key link in the chain of transmission for a significant portion of Sunni Islamic law.",
      "His role in Arabic grammar and linguistics — as part of the Basran linguistic school that competed with the Kufan school in defining Arabic grammatical norms — contributed to the systematisation of Arabic as a scholarly language and to the tradition of Quranic philology that was central to Islamic scholarship.",
      "Hammad ibn Salamah's comprehensive scholarship in hadith, Quran, and linguistics exemplified the ideal of the classical Islamic scholar and helped establish the model of religious learning that characterised Islamic civilisation's golden age — the integration of prophetic tradition, scripture, and linguistic science."
    ],
    "relationships": [
      {"sourceSlug": "hammad-ibn-salama", "sourceName": "Hammad ibn Salamah", "verb": "TRANSMITS_FROM", "targetSlug": "anas-ibn-malik", "targetName": "Anas ibn Malik (Prophet's companion)", "context": "Hammad ibn Salamah was a student of Anas ibn Malik — one of the Prophet's direct companions and the most prolific transmitter of prophetic hadith — giving Hammad's chains of transmission exceptional authority."},
      {"sourceSlug": "hammad-ibn-salama", "sourceName": "Hammad ibn Salamah", "verb": "CONTRIBUTES_TO", "targetSlug": "hadith-scholarship", "targetName": "Islamic Hadith Scholarship", "context": "Hammad was one of the most significant early collectors and transmitters of hadith — his thousands of preserved traditions became part of the foundation of the canonical Sunni hadith corpus."},
      {"sourceSlug": "basra-scholarship", "sourceName": "Basran Islamic Scholarship", "verb": "SHAPES", "targetSlug": "hammad-ibn-salama", "targetName": "Hammad ibn Salamah", "context": "Hammad was embedded in the Basran scholarly tradition — studying under its greatest teachers and contributing to the Basran school's distinctive approaches to hadith transmission, Quranic recitation, and Arabic grammar."}
    ],
    "places": [
      {"name": "Basra, Iraq (Abbasid caliphate)", "role": "Hammad's scholarly home — the great Iraqi port city that was one of the principal centres of early Islamic scholarship and the site of his education and teaching career"},
      {"name": "Early Islamic Caliphate (Umayyad to Abbasid)", "role": "The political and cultural context of Hammad's life — spanning the Umayyad caliphate's last decades and the early Abbasid period that followed the 750 CE revolution"}
    ],
    "subjects": ["Islamic Scholarship", "Hadith Sciences", "Classical Era", "Early Islam", "Islamic History", "8th Century", "Islamic Jurisprudence", "Arabic Language"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Hammad ibn Salamah (c. 708–784 CE) was one of the most important early Islamic hadith scholars — a key link in the chain of transmission connecting the Prophet's companions to the canonical 9th-century hadith collections. His student-teacher relationship with Anas ibn Malik gave his transmissions special authority, and his comprehensive learning in hadith, Quran, and linguistics exemplified the classical Islamic scholar ideal.",
      "significanceCategory": "significant"
    }
  }
},

"pha-mueang": {
  "filepath": "data/appwrite-export/entities/280-Class-280/280pha-mueang.json",
  "slug": "pha-mueang",
  "data": {
    "summary": "Pha Mueang (died c. 1300 CE) was a Thai noble and regional ruler — a vassal lord of the Khmer Empire who played a central role in the founding of the Sukhothai Kingdom, the first major Thai Buddhist polity and one of the origin points of the civilisation that would develop into the Kingdom of Thailand. According to Thai historical tradition (particularly the Ram Khamhaeng inscription, dated 1292 CE), Pha Mueang was lord of the city of Raad (Rad, in the upper Ping River valley) and a vassal or subordinate official under Khmer suzerainty. Together with Bang Klang Hao (later known as King Sri Indraditya), he expelled or defeated the Khmer governor of Sukhothai c. 1238–1257 CE, establishing the independent Thai kingdom of Sukhothai.\n\nThe founding of Sukhothai is one of the most celebrated events in Thai national history — traditionally dated to 1238 CE, it represents the emergence of an independent Thai polity free of Khmer domination in the central Chao Phraya basin. Pha Mueang's role in this founding is ambiguous: some accounts suggest he was the primary military leader who handed control of Sukhothai to Bang Klang Hao after the expulsion of the Khmer; others suggest the two were equals or co-founders. The traditional Thai historiography gives the royal lineage to Bang Klang Hao (Sri Indraditya) and his descendants, including the famous King Ram Khamhaeng (c. 1279–1298), who is credited with creating the Thai alphabet and with making Sukhothai a flourishing Buddhist kingdom.\n\nPha Mueang's story is a window into the complex political geography of mainland Southeast Asia in the 13th century — the twilight of Khmer imperial power, the emergence of new Tai (Thai) political entities in the river valleys of the mainland, and the role of Buddhist institutions and Theravada Buddhism as a cultural alternative to the Brahmanical-Hindu court culture of the Khmer Empire.",
    "causes": [
      "The decline of Khmer imperial power in the 13th century — military exhaustion from conflicts with Dai Viet and Champa, economic pressures, and the growing strength of Tai (Thai) populations in the northern river valleys — created the opportunity for regional lords like Pha Mueang and Bang Klang Hao to assert independence.",
      "The spread of Theravada Buddhism from Sri Lanka into mainland Southeast Asia in the 12th–13th centuries — providing an alternative cultural and religious model to the Brahmanical Khmer court culture — created an ideological foundation for Thai polities that distinguished themselves from Khmer suzerainty.",
      "The political culture of mainland Southeast Asia's mandala states — in which loyalty was personal and hierarchical rather than territorial, and in which the boundary between vassalage and independence was frequently renegotiated — allowed for the relatively rapid transition from Khmer client to independent ruler that Pha Mueang and Bang Klang Hao achieved."
    ],
    "effects": [
      "Pha Mueang's alliance with Bang Klang Hao in the founding of Sukhothai (c. 1238–1257 CE) established the first major independent Thai Buddhist polity — the kingdom whose political, cultural, and religious achievements became a formative reference point for later Thai civilisation, particularly after the subsequent Chakri dynasty adopted Sukhothai's heritage as part of Thai national identity.",
      "The Sukhothai Kingdom — whose founding Pha Mueang co-initiated — created the model of a Thai Buddhist state: with the Sri Lankan Theravada religious tradition, the Thai alphabet (attributed to Ram Khamhaeng), and a political culture of semi-consultative kingship, all of which influenced the later Ayutthaya Kingdom and ultimately the modern Kingdom of Thailand.",
      "Pha Mueang's defection from Khmer vassalage exemplified the broader 13th-century process of Khmer imperial fragmentation — the emergence of independent Thai (Sukhothai, Lanna) and Lao polities that collectively ended Khmer hegemony over mainland Southeast Asia."
    ],
    "relationships": [
      {"sourceSlug": "pha-mueang", "sourceName": "Pha Mueang", "verb": "CO-FOUNDS", "targetSlug": "sukhothai-kingdom", "targetName": "Sukhothai Kingdom (Thailand)", "context": "Pha Mueang allied with Bang Klang Hao to expel the Khmer from Sukhothai (c. 1238–1257 CE) — co-founding the first major independent Thai Buddhist kingdom."},
      {"sourceSlug": "khmer-empire", "sourceName": "Khmer Empire", "verb": "EMPLOYS", "targetSlug": "pha-mueang", "targetName": "Pha Mueang (before revolt)", "context": "Before the Sukhothai founding, Pha Mueang was a regional lord under Khmer suzerainty — his break from Khmer vassalage was the act that co-initiated the Thai independence movement."},
      {"sourceSlug": "sri-indraditya", "sourceName": "Sri Indraditya (Bang Klang Hao)", "verb": "ALLIED_WITH", "targetSlug": "pha-mueang", "targetName": "Pha Mueang", "context": "Bang Klang Hao (Sri Indraditya) and Pha Mueang were co-leaders of the expulsion of the Khmer from Sukhothai — Bang Klang Hao became king while Pha Mueang's subsequent role is less clearly documented."}
    ],
    "places": [
      {"name": "Sukhothai, Thailand (central Chao Phraya basin)", "role": "The city and kingdom co-founded by Pha Mueang — the first major independent Thai Buddhist polity and a foundational reference point in Thai national history"},
      {"name": "Mainland Southeast Asia (13th century)", "role": "The broader regional context — the zone of Khmer imperial decline and emerging Thai and Lao polities that defined the political geography of Pha Mueang's world"}
    ],
    "subjects": ["Thai History", "Southeast Asia", "Medieval Era", "Sukhothai Kingdom", "Khmer Empire", "Buddhism", "Medieval History", "Thailand"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Pha Mueang was the co-founder of the Sukhothai Kingdom (c. 1238–1257 CE) — the first major independent Thai Buddhist polity, whose founding is celebrated as a cornerstone of Thai national identity. His break from Khmer vassalage exemplified the 13th-century process of Khmer imperial fragmentation and the emergence of the Thai kingdoms that shaped mainland Southeast Asian civilisation.",
      "significanceCategory": "significant"
    }
  }
},

"confucianism": {
  "filepath": "data/appwrite-export/entities/110-Class-110/110confucianism.json",
  "slug": "confucianism",
  "data": {
    "summary": "Confucianism is the philosophical, ethical, and social tradition originating with the teachings of Confucius (Kong Qiu, 551–479 BCE) and developed by his followers over the subsequent millennia — one of the most influential intellectual and cultural systems in world history, which has shaped Chinese, Korean, Japanese, Vietnamese, and broader East Asian civilisation for over 2,500 years. Confucius was a Chinese philosopher, educator, and political adviser of the Spring and Autumn period who developed a system of thought centred on the cultivation of virtue, the importance of ritual and social propriety (li), humaneness or benevolence (ren), the rectification of names (zhengming), and the hierarchical relationships — between ruler and subject, parent and child, husband and wife, elder and younger brother, and friend and friend — that he believed were the foundation of harmonious society.\n\nConfucianism's development from the teachings of Confucius and his immediate disciples (compiled primarily in the Analects) into a state ideology and a comprehensive civilisational framework was a multi-century process. The philosopher Mencius (Mengzi, c. 372–289 BCE) developed Confucius's ethical ideas into a systematic moral philosophy emphasising the innate goodness of human nature, while Xunzi (c. 310–235 BCE) offered a contrasting vision emphasising the importance of ritual and education in shaping moral character. The Han dynasty's (206 BCE–220 CE) adoption of Confucianism as the official state philosophy — and the establishment of the imperial examination system based on mastery of Confucian classics — transformed Confucianism from a philosophical school into the governing ideology of the Chinese empire, a status it would maintain (with modifications and competitions from Buddhism and Daoism) for two millennia.\n\nNeo-Confucianism — the synthesis of Confucian ethics with Buddhist and Daoist metaphysics developed by Song dynasty philosophers (c. 960–1279 CE), particularly Zhu Xi (1130–1200 CE) — represented a fundamental restatement of the tradition that became the dominant form of Confucian orthodoxy in China, Korea, and Japan until the 19th century. The encounter with Western modernity and its challenge to Confucian social norms — particularly in the May Fourth Movement (1919) in China — produced both anti-Confucian iconoclasm and subsequent Neo-Confucian revival movements seeking to reconcile traditional values with modern democratic and scientific thought.",
    "causes": [
      "The political fragmentation and social disruption of the Spring and Autumn period (c. 771–476 BCE) — an era of continuous warfare between Chinese states, breakdown of Zhou royal authority, and the collapse of the ritualised feudal order — created the intellectual crisis that Confucius's teachings addressed: how to restore social harmony, moral order, and political legitimacy.",
      "The Han dynasty's adoption of Confucianism as state ideology — driven by the bureaucratic needs of a centralised empire, the appeal of Confucian meritocracy through examination, and Confucianism's emphasis on loyalty and filial piety as political virtues — transformed a philosophical school into the official culture of the most populous state in the pre-modern world.",
      "Confucianism's flexibility and capacity for synthesis — its ability to absorb Buddhist metaphysical concepts (in Neo-Confucianism), to adapt to different national contexts (becoming distinctively Korean in Joseon dynasty Confucianism, Japanese in Edo period Confucianism), and to engage modern challenges — allowed it to survive and renew itself across vastly different historical contexts."
    ],
    "effects": [
      "Confucianism's two millennia as the dominant ideology of Chinese civilisation shaped its social structures profoundly: the emphasis on filial piety created the multigenerational family as the fundamental social unit; the examination system based on Confucian classics created a meritocratic bureaucracy and a scholar-gentry elite; and Confucian ethics shaped concepts of social duty, hierarchical respect, and collective orientation that persist in East Asian cultures.",
      "The spread of Confucianism to Korea (significantly influential from the 7th century CE, dominant in the Joseon dynasty from 1392–1897), Japan (Edo period Neo-Confucianism as the official ideology of the Tokugawa shogunate), and Vietnam shaped these societies' political cultures, family structures, educational systems, and social ethics — creating the distinctive Confucian civilisational zone of East Asia.",
      "Confucianism's encounter with Western modernity and its subsequent critique, reform, and revival movements — from the May Fourth iconoclasm to Singapore's state Confucianism to the contemporary New Confucianism academic movement — has made it one of the most actively contested intellectual traditions in contemporary globalisation, as East Asian societies negotiate between Confucian values and Western liberal democratic norms."
    ],
    "relationships": [
      {"sourceSlug": "confucianism", "sourceName": "Confucianism", "verb": "ORIGINATES_WITH", "targetSlug": "confucius", "targetName": "Confucius (551–479 BCE)", "context": "Confucianism originates with the teachings of Confucius — his concepts of ren (benevolence), li (ritual propriety), and the five relationships, compiled in the Analects, form the foundational text of the Confucian tradition."},
      {"sourceSlug": "han-dynasty", "sourceName": "Han Dynasty (206 BCE–220 CE)", "verb": "ADOPTS", "targetSlug": "confucianism", "targetName": "Confucianism (as state ideology)", "context": "The Han dynasty's adoption of Confucianism as state ideology — and the creation of the imperial examination system based on Confucian classics — transformed Confucianism from a philosophical school into the governing culture of Chinese civilisation."},
      {"sourceSlug": "zhu-xi", "sourceName": "Zhu Xi (1130–1200 CE)", "verb": "REFORMULATES", "targetSlug": "confucianism", "targetName": "Confucianism (as Neo-Confucianism)", "context": "Zhu Xi's Neo-Confucian synthesis — integrating Confucian ethics with Buddhist and Daoist metaphysics — became the dominant form of Confucian orthodoxy in China, Korea, and Japan for seven centuries."}
    ],
    "places": [
      {"name": "China (Lu state, modern Shandong province)", "role": "The birthplace of Confucianism — the state of Lu where Confucius was born, taught, and developed his ideas during the Spring and Autumn period"},
      {"name": "East Asia (China, Korea, Japan, Vietnam)", "role": "The civilisational zone shaped by Confucianism — the societies whose family structures, education systems, political cultures, and social ethics were fundamentally shaped by the Confucian tradition"}
    ],
    "subjects": ["Philosophy", "East Asian Civilisation", "Classical Era", "Chinese Philosophy", "Intellectual History", "Ancient China", "Social Ethics", "Chinese Thought"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Confucianism is one of the most influential intellectual and cultural systems in world history — shaping Chinese, Korean, Japanese, and Vietnamese civilisation for over 2,500 years. Originating with Confucius (551–479 BCE), it became the state ideology of the Han empire, spread across East Asia, and produced the distinctive Confucian civilisational zone whose values and social structures continue to shape the world's most populous region.",
      "significanceCategory": "world-changing"
    }
  }
},

"ecology": {
  "filepath": "data/appwrite-export/entities/133-Class-133/133ecology.json",
  "slug": "ecology",
  "data": {
    "summary": "Ecology is the scientific study of the relationships between living organisms and their physical environment — the discipline that examines how organisms interact with each other and with the abiotic components (air, water, soil, sunlight, temperature) of their habitats, from the scale of individual organisms to populations, communities, ecosystems, biomes, and the entire biosphere. The term was coined by the German biologist Ernst Haeckel in 1866 (from Greek oikos, household) — though the scientific study of organism-environment relationships predates the term, appearing in the work of Alexander von Humboldt (1769–1859), whose geographical approach to understanding plant distribution across climatic zones established many of ecology's foundational concepts.\n\nEcology as a scientific discipline developed rapidly in the late 19th and early 20th centuries through the work of scientists including Eugenius Warming (Danish plant ecology, 1895), Charles Elton (animal ecology and the food chain, 1927), and Arthur Tansley, who coined the term 'ecosystem' in 1935 to describe the integrated unit of organisms plus their physical environment. The mid-20th century synthesis of ecology with evolutionary biology — exemplified by the mathematical population ecology of G. Evelyn Hutchinson, Robert MacArthur, and E.O. Wilson's theory of island biogeography (1967) — transformed ecology from a descriptive natural history into a theoretical science with predictive mathematical models of population dynamics, species diversity, energy flow, and nutrient cycling.\n\nThe environmental crisis of the late 20th century transformed ecology from a relatively obscure academic discipline into a science of urgent public and political relevance. Rachel Carson's 'Silent Spring' (1962) — documenting the ecological consequences of pesticide use — awakened public consciousness to ecosystem fragility and was a catalyst for the modern environmental movement. The subsequent decades saw ecology's concepts (biodiversity, ecosystem services, carrying capacity, carbon cycles) become central to environmental policy, conservation biology, climate science, and sustainable development — making ecology one of the most practically consequential of the biological sciences.",
    "causes": [
      "Ernst Haeckel's 1866 coining of 'ecology' and the broader 19th-century development of biogeography — Alexander von Humboldt's systematic mapping of plant distributions across climatic gradients, Darwin's evolutionary framework for understanding organism-environment adaptation — established the conceptual foundations on which ecology as a scientific discipline was built.",
      "The 20th-century mathematical revolution in biology — the application of differential equations and statistical methods to population dynamics, competition theory, and community structure — transformed ecology from descriptive natural history into a predictive quantitative science capable of generating testable models.",
      "The environmental crisis of the post-World War II era — industrial pollution, pesticide overuse (documented by Carson's 'Silent Spring'), and accelerating habitat destruction — created the urgent public and political demand for ecological science as a practical tool for understanding and managing environmental problems."
    ],
    "effects": [
      "Ecology's conceptual frameworks — ecosystem services, biodiversity, carrying capacity, trophic cascades, keystone species, the carbon cycle — have become the scientific foundation of environmental policy, conservation biology, climate science, and sustainable development, making ecological literacy essential for governance in the 21st century.",
      "The modern environmental movement — launched in the 1960s by Rachel Carson's 'Silent Spring', the first Earth Day (1970), and subsequent environmental legislation (Clean Air Act, Endangered Species Act, UNCED) — drew directly on ecological science for its evidence and its concepts, transforming ecology from academic discipline to political force.",
      "The synthesis of ecology with evolutionary biology, genetics, and climate science in the late 20th and early 21st centuries produced conservation biology, restoration ecology, and macroecology — applied scientific disciplines directly addressing the biodiversity crisis and climate change that are among the most urgent problems of our time."
    ],
    "relationships": [
      {"sourceSlug": "ecology", "sourceName": "Ecology", "verb": "COINED_BY", "targetSlug": "ernst-haeckel", "targetName": "Ernst Haeckel (1866)", "context": "Ernst Haeckel coined the term 'ecology' in 1866 — naming the discipline that studies organism-environment relationships, though the study of such relationships predates the term in Humboldt's work."},
      {"sourceSlug": "rachel-carson", "sourceName": "Rachel Carson", "verb": "POPULARISES", "targetSlug": "ecology", "targetName": "Ecology (public consciousness)", "context": "Rachel Carson's 'Silent Spring' (1962) brought ecological concepts — ecosystem fragility, food chain contamination, biodiversity loss — to public consciousness and catalysed the modern environmental movement."},
      {"sourceSlug": "ecology", "sourceName": "Ecology", "verb": "INFORMS", "targetSlug": "conservation-biology", "targetName": "Conservation Biology and Environmental Policy", "context": "Ecology's concepts of ecosystem services, biodiversity, and carrying capacity have become the scientific foundation of conservation biology, environmental policy, and international agreements on climate change and biodiversity."}
    ],
    "places": [
      {"name": "Europe (Germany, Denmark, UK) and North America", "role": "The primary centres of ecology's early development — Haeckel in Germany, Warming in Denmark, Tansley and Elton in the UK, MacArthur and Wilson in North America"},
      {"name": "Global biosphere", "role": "The operational scope of ecology — the entirety of the Earth's ecosystems, from tropical forests to polar tundra, that ecology studies and that the environmental crisis has threatened"}
    ],
    "subjects": ["Natural Sciences", "Biology", "Contemporary Era", "Environmental Science", "Scientific History", "Ecology", "Environmental Movement", "Conservation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Ecology — the scientific study of organism-environment relationships — has become one of the most practically consequential scientific disciplines in human history. From Ernst Haeckel's 1866 coining of the term through Rachel Carson's 'Silent Spring' and to its central role in addressing the climate and biodiversity crises of the 21st century, ecology's concepts now underpin environmental policy, conservation, and sustainable development worldwide.",
      "significanceCategory": "world-changing"
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
