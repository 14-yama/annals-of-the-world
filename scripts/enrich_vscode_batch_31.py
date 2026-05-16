#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 31 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: gospel-of-thomas, gospel-of-luke, first-they-came,
          commentarii-de-bello-gallico, book-of-the-later-han,
          commentaries-on-the-laws-of-england-blackstone,
          animal-farm, and-then-there-were-none
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-31-may2026"

ENRICHMENTS = {

"gospel-of-thomas": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-thomas.json",
  "slug": "gospel-of-thomas",
  "data": {
    "summary": "The Gospel of Thomas is a non-canonical collection of 114 sayings attributed to Jesus, discovered as part of the Nag Hammadi library in December 1945 near Nag Hammadi, Upper Egypt, and first published in full in 1959 — one of the most significant finds in the history of early Christian scholarship, and the most complete example of the genre of 'sayings gospel' in contrast to the narrative Gospels of the New Testament. The text exists in a Coptic translation (from the Greek original) and is dated by scholars to the 1st or 2nd century CE — with debate about whether it preserves authentic early Jesus sayings (possibly predating the Synoptic Gospels) or represents a 2nd-century Gnostic reworking. The text begins: 'These are the secret sayings which the living Jesus spoke, and which Didymos Judas Thomas wrote down' — the attribution to 'Doubting Thomas' (as the twin of Jesus in some Syriac traditions) gives the text its name.\n\nThe Gospel of Thomas contains a number of sayings that parallel the canonical Gospels (the parables of the Mustard Seed, the Pearl, the Sower) and others that have no canonical parallel — including the famous 'split a piece of wood, and I am there; lift up the stone, and you will find me there' (Saying 77) and 'If you bring forth what is within you, what you bring forth will save you; if you do not bring forth what is within you, what you do not bring forth will destroy you' (Saying 70), which have a distinctly Gnostic, inward-turning spirituality. The Gospel of Thomas has no narrative, no Passion, no resurrection — it is a purely wisdom text, presenting Jesus as a revealer of hidden knowledge (gnosis) rather than a saviour through sacrifice.\n\nThe Gospel of Thomas is one of the most debated texts in New Testament scholarship — the question of its date and its relationship to the Synoptic Gospels is central to the reconstruction of the history of early Christianity. If it preserves an early stratum of Jesus sayings independent of the Synoptics, it provides invaluable evidence for the diversity of early Christianity; if it is a 2nd-century Gnostic composition, it illustrates the development of Gnostic Christianity from the canonical tradition.",
    "causes": [
      "The Gnostic Christian tradition — the early Christian movement that emphasised the salvific power of hidden knowledge (gnosis) rather than faith, sacrifice, and resurrection, and which produced a rich alternative literature (the Nag Hammadi texts) alongside and in competition with what became canonical Christianity — created the context in which the Gospel of Thomas was composed, preserved, and transmitted.",
      "The early Christian practice of collecting the sayings of Jesus — evident in the hypothetical Q source (the common sayings material of Matthew and Luke), in the Didache, and in scattered citations of agrapha (unwritten sayings of Jesus) — provided the literary genre into which the Gospel of Thomas fits, suggesting that sayings collections were an important early form of Jesus tradition alongside narrative Gospels.",
      "The Egyptian Christian monastic community responsible for the Nag Hammadi library — which buried a collection of Gnostic texts in a sealed jar c. 350 CE, possibly to preserve them from destruction during the establishment of Catholic orthodoxy — was the immediate cause of the Gospel of Thomas's preservation and modern discovery."
    ],
    "effects": [
      "The discovery of the Gospel of Thomas in 1945 transformed the scholarly understanding of early Christianity's diversity — it demonstrated that the canonical New Testament represented the victory of one form of Christianity over many competing alternatives, and that sayings gospels (without Passion narrative) may have been among the earliest forms of Christian literature.",
      "The Gospel of Thomas became central to the academic and popular Jesus Seminar movement (1985 onwards) — which used it alongside the canonical Gospels to reconstruct the 'historical Jesus' — and to the broader cultural reassessment of Christian origins that produced popular works like Elaine Pagels's The Gnostic Gospels (1979) and Bart Ehrman's bestsellers.",
      "The Gospel of Thomas's 'secret sayings' — particularly those with Gnostic, interior, or pantheistic resonance ('Split a piece of wood, and I am there') — have been widely adopted in contemporary spirituality movements seeking a 'mystical Jesus' alternative to institutional Christianity, making the text influential far beyond academic New Testament scholarship."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-thomas", "sourceName": "Gospel of Thomas (Nag Hammadi, 1945)", "verb": "PART_OF", "targetSlug": "nag-hammadi-library", "targetName": "Nag Hammadi library (discovery 1945)", "context": "The Gospel of Thomas was discovered as part of the Nag Hammadi library in December 1945 — a collection of Gnostic texts buried in Upper Egypt c. 350 CE, the most important discovery for the study of Gnostic Christianity."},
      {"sourceSlug": "gospel-of-thomas", "sourceName": "Gospel of Thomas", "verb": "PARALLELS", "targetSlug": "synoptic-gospels", "targetName": "Synoptic Gospels (Mark, Matthew, Luke)", "context": "The Gospel of Thomas contains sayings paralleling the Synoptic Gospels — the question of whether these represent independent early Jesus tradition or Gnostic reworkings of the canonical texts is central to the debate about early Christian literature."},
      {"sourceSlug": "gospel-of-thomas", "sourceName": "Gospel of Thomas", "verb": "INFLUENCES", "targetSlug": "jesus-seminar", "targetName": "Jesus Seminar (1985–) and historical Jesus scholarship", "context": "The Gospel of Thomas became a central text for the Jesus Seminar — which used it alongside the canonical Gospels to reconstruct the historical Jesus — and for the broader academic reassessment of early Christian diversity."}
    ],
    "places": [
      {"name": "Nag Hammadi, Upper Egypt (discovery, December 1945)", "role": "The Nag Hammadi region of Upper Egypt — where local farmers accidentally discovered the library of Gnostic texts, including the Gospel of Thomas, buried in a sealed jar c. 350 CE"},
      {"name": "Syria-Palestine (probable composition context, 1st–2nd century CE)", "role": "The Gospel of Thomas is probably associated with the Syrian Christian tradition — its attribution to Thomas as the twin of Jesus is a Syriac tradition, and Syria is the probable region of its composition or early transmission"}
    ],
    "subjects": ["Gnostic Christianity", "Classical Era", "New Testament Apocrypha", "Early Christianity", "Jesus", "Christian Texts", "Nag Hammadi", "Biblical Scholarship"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Gospel of Thomas (1st–2nd century CE, discovered 1945) is the most complete example of the sayings-gospel genre and the most important text discovered outside the canonical New Testament — its discovery transformed the scholarly understanding of early Christian diversity and placed the question of Gnostic Christianity at the centre of 20th-century biblical scholarship. Its influence through Elaine Pagels's The Gnostic Gospels and the Jesus Seminar has been substantial.",
      "significanceCategory": "highly-significant"
    }
  }
},

"gospel-of-luke": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-luke.json",
  "slug": "gospel-of-luke",
  "data": {
    "summary": "The Gospel of Luke is the third Gospel in the New Testament canon, traditionally attributed to Luke the Evangelist (a physician and companion of Paul) and dated by most scholars to c. 80–90 CE — the longest of the four canonical Gospels and, together with the Acts of the Apostles (which shares its author and addressee, Theophilus), the longest contribution to the New Testament from a single author. Luke is the most literary of the Gospel writers — his prologue ('Since many have undertaken to compile a narrative of the things that have been accomplished among us...') is written in elegant Greek and follows the conventions of ancient historical prologues — and his Gospel is characterised by special concern for the poor, for women, for outcasts (Samaritans, tax collectors, sinners), and for the universality of Jesus's mission beyond Israel.\n\nThe Gospel of Luke contains some of the most beloved narratives in the New Testament, many of which are found only in Luke: the Annunciation to Mary and the Magnificat (1:46–55, 'My soul magnifies the Lord... he has filled the hungry with good things, and the rich he has sent away empty'), the Nativity with the shepherds in the fields, the Parable of the Good Samaritan (10:25–37), the Parable of the Prodigal Son (15:11–32), the story of Zacchaeus the tax collector, the healing of the ten lepers, and the Road to Emmaus resurrection appearance. Luke's distinctive theological emphasis — on God's special concern for the poor and marginalised ('Blessed are you who are poor, for yours is the kingdom of God'), on forgiveness and repentance, on the role of women in Jesus's ministry — gives the Lucan Gospel its characteristic 'Gospel of mercy' character.\n\nLuke–Acts (the two-volume work) is the most historically ambitious writing in the New Testament — its account of the spread of Christianity from Jerusalem to Rome (Acts) presents the Christian movement as the fulfilment of Jewish prophecy and the salvation of the Gentile world, structured to mirror Virgil's Aeneid in presenting Christianity as the true foundation story of the civilised world.",
    "causes": [
      "Luke's Gentile Christian readership — addressed to Theophilus (possibly a Roman official or patron) and written for non-Jewish Christians who needed the Jewish context of Jesus's life explained and the significance of Old Testament prophecy demonstrated — gave the Gospel of Luke its distinctive focus on explaining Jewish customs for outsiders and its emphasis on the universal scope of Jesus's mission.",
      "The Markan source (Mark's Gospel, used as a primary narrative source by both Matthew and Luke) and the Q source (the collection of Jesus sayings shared by Matthew and Luke but not Mark) provided the literary materials from which Luke constructed his Gospel — but Luke's distinctive 'Special L' material (the parables unique to Luke) represents either independent tradition or Luke's own theological and literary creativity.",
      "Luke's theological programme — his concern to demonstrate both the historical continuity of Christianity with Jewish prophecy and the radical inclusion of the poor, women, Samaritans, and Gentiles in the Jesus movement — gave the Gospel of Luke its distinctive profile: the 'Gospel of mercy' that became foundational for the social justice tradition in Christianity."
    ],
    "effects": [
      "Luke's Parable of the Good Samaritan (10:25–37) became the foundational text of the Western tradition of humanitarian obligation — the image of the Samaritan who helps the wounded stranger despite ethnic and religious enmity has been the most cited Christian text in arguments for universal human solidarity and has given English the common noun 'Good Samaritan'.",
      "The Magnificat (Luke 1:46–55) — Mary's song of praise celebrating God's reversal of social hierarchies ('he has put down the mighty from their thrones, and exalted those of low degree; he has filled the hungry with good things, and the rich he has sent away empty') — became the foundational text of liberation theology and the Christian tradition of God's preferential option for the poor.",
      "Luke's narrative of the Nativity — the shepherds in the fields, the angels' 'Gloria in excelsis Deo', the manger — is the primary source for the Western tradition of the Christmas nativity scene (the crèche/presepio introduced by Francis of Assisi in 1223), and his narrative is the basis for virtually all Christmas art, music, and devotion in the Western tradition."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-luke", "sourceName": "Gospel of Luke (c. 80–90 CE)", "verb": "PART_OF", "targetSlug": "new-testament", "targetName": "New Testament (canonical Gospels)", "context": "Luke's Gospel is the third of the four canonical Gospels — its two-volume structure (Luke–Acts) makes it the largest single contribution to the New Testament and the most historically ambitious account of Jesus's ministry and the spread of early Christianity."},
      {"sourceSlug": "gospel-of-luke", "sourceName": "Luke's Parable of the Good Samaritan", "verb": "FOUNDS", "targetSlug": "humanitarian-obligation", "targetName": "Western tradition of humanitarian obligation", "context": "The Good Samaritan parable (Luke 10:25–37) is the most cited Christian text in arguments for universal human solidarity and gave English the term 'Good Samaritan' — foundational for the Western tradition of humanitarian obligation across ethnic and religious lines."},
      {"sourceSlug": "gospel-of-luke", "sourceName": "Luke's Magnificat (1:46–55)", "verb": "INSPIRES", "targetSlug": "liberation-theology", "targetName": "Liberation theology (preferential option for the poor)", "context": "The Magnificat's reversal of social hierarchies ('he has put down the mighty... he has filled the hungry with good things') became foundational for liberation theology's argument for God's preferential option for the poor."}
    ],
    "places": [
      {"name": "Antioch or Rome (probable composition location, c. 80–90 CE)", "role": "The Gospel of Luke was probably written in a Gentile Christian community — Antioch (Syria) or Rome are the traditional candidates — for a readership that needed the Jewish context of Jesus explained"},
      {"name": "Jerusalem and Galilee (narrative setting)", "role": "Luke's Gospel begins and ends in Jerusalem — its narrative of Jesus's ministry in Galilee and his final journey to Jerusalem gives the Gospel its geographical structure and theological movement toward the holy city"}
    ],
    "subjects": ["New Testament", "Classical Era", "Christianity", "Biblical Literature", "Luke", "Gospel", "Ancient Christianity", "Religious Texts"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Gospel of Luke (c. 80–90 CE) is the most literary of the four canonical Gospels and the source of some of Christianity's most influential texts — the Good Samaritan parable (foundational for humanitarian ethics), the Magnificat (foundational for liberation theology), and the Nativity narrative (foundational for Christmas tradition). Its two-volume Luke–Acts is the most historically ambitious writing in the New Testament.",
      "significanceCategory": "world-changing"
    }
  }
},

"first-they-came": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780first-they-came.json",
  "slug": "first-they-came",
  "data": {
    "summary": "'First they came...' is the confessional poem attributed to Martin Niemöller (1892–1984), a German Lutheran pastor who was initially supportive of the Nazi regime but became one of its most prominent opponents and was imprisoned in concentration camps (Sachsenhausen and Dachau) from 1938 to 1945. The poem exists in numerous versions — Niemöller never published a single authoritative text, and its precise wording is disputed — but its most commonly cited English form is: 'First they came for the socialists, and I did not speak out — because I was not a socialist. / Then they came for the trade unionists, and I did not speak out — because I was not a trade unionist. / Then they came for the Jews, and I did not speak out — because I was not a Jew. / Then they came for me — and there was no one left to speak for me.'\n\nThe poem's power lies in its formal simplicity — the anaphoric structure ('First they came... Then they came... Then they came... Then they came for me') mimics the logic of passive complicity, showing how each act of silence creates the conditions for the next until the silence has become absolute. Its theme — the moral catastrophe of the bystander's passivity in the face of incremental persecution — has made it the canonical poetic statement of bystander responsibility and the obligation of solidarity across difference.\n\n'First they came...' has become one of the most widely quoted texts in the post-Holocaust tradition of moral and political reflection — cited in Holocaust memorials, human rights campaigns, civil rights speeches, and anti-authoritarian rhetoric worldwide. Its influence extends far beyond the Holocaust context: it has been adapted and applied to virtually every situation in which a minority group faces persecution while the majority remains silent, making it the most versatile political poem of the 20th century. The United States Holocaust Memorial Museum in Washington, D.C. displays the poem prominently.",
    "causes": [
      "Niemöller's own experience — his initial support for Hitler (he voted for the Nazis in 1933) followed by his growing opposition to the Nazi state's interference in church affairs, his founding of the Confessing Church, his arrest in 1937, and his eight years in concentration camps — gave the poem its autobiographical moral authority: it is a confession of personal failure as much as an indictment of collective passivity.",
      "The Nazi regime's strategy of incremental persecution — targeting political opponents, then trade unionists, then Jews, then other minorities in sequence, allowing each group to be destroyed while others remained passive — provided the poem's specific historical content and its demonstration of how systematic silence enables systematic persecution.",
      "The post-Holocaust need for moral reckoning — the question of how ordinary Germans had allowed the Holocaust to happen, and what the obligations of bystanders are in the face of persecution — created the cultural context for the poem's widespread adoption as the canonical statement of bystander responsibility."
    ],
    "effects": [
      "'First they came...' has become the canonical poetic expression of bystander responsibility — its structural demonstration of how passive complicity enables successive acts of persecution has been cited in human rights campaigns, Holocaust education, civil rights rhetoric, and anti-authoritarian discourse worldwide.",
      "The poem's formal influence — the anaphoric list structure that accumulates moral weight through repetition — has been widely imitated in political poetry and oratory, becoming a model for anti-persecution rhetoric that adapts the poem's logic to new contexts (LGBT persecution, racial profiling, religious discrimination).",
      "The poem's prominence at the United States Holocaust Memorial Museum and in Holocaust education curricula worldwide has made it the most widely taught Holocaust-related text in English-speaking countries — shaping generations of students' first encounter with the moral lessons of the Holocaust."
    ],
    "relationships": [
      {"sourceSlug": "martin-niemöller", "sourceName": "Martin Niemöller (1892–1984)", "verb": "AUTHORS", "targetSlug": "first-they-came", "targetName": "'First they came...' (various versions, post-1945)", "context": "Niemöller composed multiple versions of the poem, drawing on his post-war speeches about the failure of German Protestants to resist Nazism — a confession of his own complicity as well as an indictment of collective passivity."},
      {"sourceSlug": "first-they-came", "sourceName": "'First they came...'", "verb": "ARTICULATES", "targetSlug": "bystander-responsibility", "targetName": "Bystander responsibility (Holocaust ethics and beyond)", "context": "The poem's anaphoric structure — demonstrating how each act of silence enables the next persecution — is the canonical poetic statement of bystander responsibility, widely cited in Holocaust education and human rights discourse."},
      {"sourceSlug": "first-they-came", "sourceName": "'First they came...' (Niemöller)", "verb": "DISPLAYED_AT", "targetSlug": "us-holocaust-memorial-museum", "targetName": "United States Holocaust Memorial Museum, Washington D.C.", "context": "The poem is prominently displayed at the USHMM — one of the most visited museum sites in the United States — making it the first Holocaust text encountered by millions of visitors annually."}
    ],
    "places": [
      {"name": "Dachau concentration camp (1941–1945, Niemöller's imprisonment)", "role": "Niemöller spent most of his concentration camp imprisonment at Dachau — his personal experience of persecution gave the poem its autobiographical moral authority"},
      {"name": "United States Holocaust Memorial Museum, Washington D.C. (post-1993 global reach)", "role": "The poem's prominence at the USHMM and in Holocaust education worldwide has made it the most widely known Holocaust-related text in English-speaking countries"}
    ],
    "subjects": ["Holocaust", "Modern Era", "German History", "Political Poetry", "World War II", "Martin Niemöller", "Human Rights", "Ethics"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "'First they came...' (Niemöller, various versions) is the canonical poetic statement of bystander responsibility — its anaphoric demonstration of how passive complicity enables successive acts of persecution has been cited in Holocaust education, human rights campaigns, and anti-authoritarian rhetoric worldwide. Prominently displayed at the US Holocaust Memorial Museum, it is the most widely taught Holocaust-related text in English-speaking countries.",
      "significanceCategory": "highly-significant"
    }
  }
},

"commentarii-de-bello-gallico": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781commentarii-de-bello-gallico.json",
  "slug": "commentarii-de-bello-gallico",
  "data": {
    "summary": "The Commentarii de Bello Gallico (Commentaries on the Gallic War) is the military memoir of Gaius Julius Caesar (100–44 BCE), composed c. 58–51 BCE — a contemporaneous account of Caesar's campaigns in Gaul (modern France, Belgium, and parts of Switzerland, Germany, and the Netherlands) from 58 to 52 BCE, including his two expeditions to Britain (55 and 54 BCE) and the final Gallic revolt led by Vercingetorix (culminating in the Siege of Alesia in 52 BCE). Caesar wrote the work in the field during his campaigns, composing and distributing each book (corresponding to one year's campaigning) as a political document addressed to the Roman public and Senate — justifying his military actions, maintaining his political position in Rome during his absence, and constructing his public image as Rome's greatest military commander.\n\nThe Commentarii de Bello Gallico is one of the most read texts in the history of European education — for two millennia it was the primary Latin text used to teach Latin in European schools, and its clear, direct, third-person narrative style ('Caesar went... Caesar ordered... Caesar saw...') was deliberately designed for wide readability. This simplicity and directness make it the ideal Latin text for beginners, and 'all Gaul is divided into three parts' (Gallia est omnis divisa in partes tres) is perhaps the most famous opening sentence in Latin literature. Caesar's strategic genius — his rapid marches, his engineering feats (the Rhine bridge, the Alesia circumvallation), his negotiation with tribal leaders — is presented with deceptive matter-of-factness that has fascinated military historians and strategists for 2,000 years.\n\nBello Gallico is simultaneously a primary historical source for the history of Gaul and the Celtic and Germanic peoples at the moment of Roman conquest, and a brilliant piece of political propaganda — Caesar's account of his wars, written in the third person to convey impartiality, is nonetheless a carefully constructed self-presentation by one of history's most skilled self-publicists. His descriptions of the Gauls and Germans are the primary ancient literary sources for the early history of these peoples.",
    "causes": [
      "Caesar's political situation in Rome — his need to maintain public prominence and Senate support during his long absence from Rome on campaign, his rivalry with Pompey and the conservative Senate faction (boni), and his need to justify the scale and cost of his Gallic campaigns — gave the Commentarii its propagandistic character: each book was distributed in Rome as a political document designed to shape opinion.",
      "The Gallic War itself — which Caesar initiated with the pretext of protecting Rome's Gallic allies from migrating tribes (the Helvetii, the Germanic Ariovistus), and which expanded into a systematic conquest of all of Gaul over eight years — provided the military narrative and the succession of military challenges (Alesia, the channel crossings, the Rhine bridges) that gave the Commentarii its structure and drama.",
      "The Roman political culture's demand for military gloria — the expectation that a great Roman aristocrat would demonstrate his virtus (martial virtue) through military victory and use his military achievements as the foundation of political authority — gave Caesar both the incentive and the framework for self-presentation: the Commentarii is an extended demonstration of Caesar's virtus for his Roman audience."
    ],
    "effects": [
      "The Commentarii de Bello Gallico became the primary Latin text of European education for approximately 2,000 years — from Roman schools through medieval monastic education to the 20th-century Latin curriculum — making 'all Gaul is divided into three parts' one of the most widely read Latin sentences in history and introducing more generations of students to Latin than any other text.",
      "Caesar's conquest of Gaul — documented in the Commentarii — permanently transformed European history: the Romanisation of Gaul over the following centuries produced the linguistic, cultural, and institutional foundations of what became France, and the Roman road network, cities, and legal culture of Gaul were the infrastructure on which medieval and modern France was built.",
      "The Commentarii's descriptions of the Gauls and Germans — their customs, religion, political organisation, and tribal structures — are the primary ancient literary sources for the early history of Celtic Gaul and the Germanic peoples, making Caesar's propaganda document an irreplaceable historical and ethnographic record despite its obvious ideological shaping."
    ],
    "relationships": [
      {"sourceSlug": "julius-caesar", "sourceName": "Julius Caesar (100–44 BCE)", "verb": "AUTHORS", "targetSlug": "commentarii-de-bello-gallico", "targetName": "Commentarii de Bello Gallico (c. 58–51 BCE)", "context": "Caesar wrote the Commentarii in the field during his Gallic campaigns — distributing each book as a political document to Rome — a combination of military memoir, political propaganda, and strategic self-presentation."},
      {"sourceSlug": "commentarii-de-bello-gallico", "sourceName": "Bello Gallico", "verb": "DOCUMENTS", "targetSlug": "roman-conquest-of-gaul", "targetName": "Roman conquest of Gaul (58–50 BCE)", "context": "The Commentarii is the primary contemporary source for Caesar's conquest of Gaul — its accounts of the battles of the Helvetii, Alesia, and the Rhine crossings are the foundation of our knowledge of the Roman military in Gaul."},
      {"sourceSlug": "commentarii-de-bello-gallico", "sourceName": "Bello Gallico (Latin education text)", "verb": "SHAPES", "targetSlug": "latin-education", "targetName": "Latin education in European schools (Roman through 20th century)", "context": "The Commentarii was the primary Latin text used to teach Latin in European schools for approximately 2,000 years — 'all Gaul is divided into three parts' is one of the most widely read Latin sentences in history."}
    ],
    "places": [
      {"name": "Gaul (modern France, Belgium, Switzerland, 58–51 BCE campaigns)", "role": "The territory of ancient Gaul — from the Pyrenees to the Rhine, from the Atlantic to the Alps — is the theatre of Caesar's campaigns and the subject of his ethnographic and military descriptions"},
      {"name": "Rome (political audience, 58–51 BCE, propagandistic distribution)", "role": "The books of the Commentarii were distributed in Rome as political documents during Caesar's campaigns — the Roman public and Senate were Caesar's primary audience, and the text was a sustained political self-presentation"}
    ],
    "subjects": ["Roman History", "Classical Era", "Julius Caesar", "Latin Literature", "Military History", "Ancient Rome", "Gaul", "Primary Source"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Caesar's Commentarii de Bello Gallico (c. 58–51 BCE) is the primary source for the Roman conquest of Gaul and one of the most consequential Latin texts in the history of education — read in European schools for 2,000 years, 'all Gaul is divided into three parts' is among the most famous openings in Latin literature. Caesar's conquest permanently transformed European history, establishing the Romanised Gaul that became medieval and modern France.",
      "significanceCategory": "world-changing"
    }
  }
},

"book-of-the-later-han": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781book-of-the-later-han.json",
  "slug": "book-of-the-later-han",
  "data": {
    "summary": "The Book of the Later Han (Chinese: 後漢書, Hòu Hànshū) is the official dynastic history of the Eastern Han dynasty (25–220 CE), compiled by Fan Ye (398–445 CE) of the Liu Song dynasty — one of the Four Standard Histories of China (alongside the Records of the Grand Historian, the Book of Han, and the Records of the Three Kingdoms) and one of the Twenty-Four Histories that constitute the official historical record of Chinese civilisation. Fan Ye compiled the work from earlier Han accounts, presenting the history of the Eastern Han dynasty — its founding by Emperor Guangwu (Liu Xiu), who restored the Han dynasty after the Xin interregnum of Wang Mang (9–23 CE), through its gradual decline due to eunuch faction, Yellow Turban rebellion (184 CE), and the rise of the warlords that preceded the Three Kingdoms period.\n\nThe Book of the Later Han is a critical primary source for Chinese history of the 1st–3rd centuries CE, covering the period of Han expansion into Central Asia (the campaigns of Ban Chao who reached the Caspian Sea), the earliest known diplomatic contact between Rome and China (the Da Qin section, describing a Roman embassy c. 166 CE under Emperor Huan), and the Silk Road's flourishing as a channel of commercial and cultural exchange between China, Central Asia, Parthia, and Rome. Its biographies include the mathematician and cartographer Zhang Heng (inventor of the seismoscope, the armillary sphere, and the water-powered orrery), the historian Ban Gu (who completed the Book of Han), and the female scholar Ban Zhao (who completed the Book of Han after her brother's death and wrote the Admonitions for Women).\n\nFan Ye's compilation is admired for its literary style — his introductory essays and the 'Treatise on Astronomy' and 'Treatise on the Five Elements' represent significant achievements in Han historical writing — and its portrait of the Eastern Han court's culture, including the development of paper manufacture (Cai Lun's papermaking improvements, 105 CE) and the arrival of Buddhism in China, is invaluable for the history of technology and religion.",
    "causes": [
      "The Chinese historical tradition — the institutionalised practice of compiling official dynastic histories (zheng shi) documenting the political, administrative, cultural, and economic history of each dynasty — created both the demand for and the form of the Book of the Later Han: Fan Ye's work follows the model established by Sima Qian (Records of the Grand Historian) and Ban Gu (Book of Han) in combining annals, treatises, and biographies.",
      "Fan Ye's scholarly project — his recognition that existing accounts of the Eastern Han were scattered, inconsistent, and inadequate — led him to compile a synthesis that drew on multiple earlier sources (including the earlier Han Ji by Xun Yue) to produce a comprehensive and critically evaluated history, a process of compilation and synthesis characteristic of Chinese dynastic historiography.",
      "The Eastern Han dynasty's complex history — the interplay of imperial authority, scholar-official culture, eunuch faction, and regional military power that defined the 2nd century CE and culminated in the warlordism of the late Eastern Han — provided the political narrative framework around which Fan Ye organised his history."
    ],
    "effects": [
      "The Book of the Later Han is the primary historical source for the history of the Eastern Han dynasty — its coverage of the Yellow Turban Rebellion (184 CE), the campaigns in Central Asia, the diplomatic exchanges with the Parthian and Roman empires, and the rise of the regional warlords who ended the Han is the foundation of our knowledge of this crucial period of Chinese history.",
      "The Book of the Later Han's accounts of early Sino-Roman contact — the Da Qin section describing a Roman embassy to China c. 166 CE, and the account of Chinese silk reaching Rome through Parthian intermediaries — are the primary Chinese sources for the study of the ancient Silk Road and the earliest connections between East Asian and Mediterranean civilisations.",
      "The Book of the Later Han's biography of Cai Lun — the court official who improved papermaking techniques c. 105 CE — is the primary source for the history of paper manufacture in China, and its account of Buddhism's arrival in China (the White Horse Temple legend, c. 67 CE) is an important early source for the history of Buddhism's spread along the Silk Road."
    ],
    "relationships": [
      {"sourceSlug": "fan-ye", "sourceName": "Fan Ye (398–445 CE)", "verb": "AUTHORS", "targetSlug": "book-of-the-later-han", "targetName": "Book of the Later Han (compiled c. 432–445 CE)", "context": "Fan Ye compiled the Book of the Later Han during his imprisonment under the Liu Song dynasty — drawing on earlier sources to produce a comprehensive account of the Eastern Han (25–220 CE) that became one of the Four Standard Histories."},
      {"sourceSlug": "book-of-the-later-han", "sourceName": "Book of the Later Han (Da Qin section)", "verb": "DOCUMENTS", "targetSlug": "ancient-sino-roman-contact", "targetName": "Ancient Sino-Roman contact (Da Qin, c. 166 CE)", "context": "The Book of the Later Han's Da Qin section — describing a Roman embassy to China c. 166 CE — is the primary Chinese source for the earliest known diplomatic contact between China and Rome and for the study of the Silk Road's role in East-West cultural exchange."},
      {"sourceSlug": "book-of-the-later-han", "sourceName": "Book of the Later Han", "verb": "PART_OF", "targetSlug": "twenty-four-histories", "targetName": "Twenty-Four Histories (official Chinese dynastic histories)", "context": "The Book of the Later Han is one of the Four Standard Histories and among the Twenty-Four Histories that constitute the official historical record of Chinese civilisation — the most comprehensive and authoritative body of historical documentation in any pre-modern culture."}
    ],
    "places": [
      {"name": "China (Eastern Han dynasty, 25–220 CE, subject of history)", "role": "The Book of the Later Han covers the history of the Eastern Han dynasty — its founding, its expansion, its cultural achievements, and its decline — across the territory of the Chinese empire from Korea and Vietnam to Central Asia"},
      {"name": "Liu Song dynasty (432–445 CE, Fan Ye's compilation context)", "role": "Fan Ye compiled the Book of the Later Han during the Liu Song dynasty — completing the work shortly before his execution on political charges in 445 CE"}
    ],
    "subjects": ["Chinese History", "Classical Era", "Han Dynasty", "Chinese Literature", "Historiography", "Silk Road", "East Asia", "Primary Source"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Book of the Later Han (Fan Ye, c. 432–445 CE) is the primary historical source for the Eastern Han dynasty — covering the flourishing of the Silk Road, the earliest Sino-Roman diplomatic contact, Cai Lun's papermaking improvements, and the arrival of Buddhism in China. One of the Four Standard Histories, it is an essential document of Chinese civilisation at the height of the Han and its transformation into the Three Kingdoms period.",
      "significanceCategory": "highly-significant"
    }
  }
},

"commentaries-on-the-laws-of-england-blackstone": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781commentaries-on-the-laws-of-england-blac.json",
  "slug": "commentaries-on-the-laws-of-england-blackstone",
  "data": {
    "summary": "Commentaries on the Laws of England is the systematic exposition of English common law by Sir William Blackstone (1723–1780), published in four volumes between 1765 and 1769 — the most influential work in the history of English legal education and one of the most consequential legal texts in the history of the common law tradition. Blackstone, the first Vinerian Professor of English Law at Oxford (1758), wrote the Commentaries as a systematic, accessible introduction to the entire body of English common law — covering the rights of persons, the rights of things (property law), private wrongs (tort law), and public wrongs (criminal law) — in lucid, elegant prose designed for students and educated laypeople rather than exclusively for practising lawyers.\n\nBlackstone's Commentaries was the primary legal text used to train English and American lawyers for over a century: in England, it dominated legal education until the founding of the law schools in the 19th century; in the American colonies (and subsequently the United States), it was the primary legal reference for the founding generation of American lawyers and statesmen — more copies were sold in pre-Revolutionary America than in England, and the Commentaries was the legal bible of the American Founders. Abraham Lincoln taught himself law primarily by reading Blackstone. The Commentaries' influence on American constitutional and common law is immeasurable — its doctrines on natural rights, property, constitutional law, and the rights of Englishmen were the intellectual foundations on which the American Founders constructed their arguments for independence and the constitutional framework of the new republic.\n\nBlackstone's famous definition of natural rights — 'The absolute rights of man, considered as a free agent, endowed with discernment to know good from evil, and with power of choosing those measures which appear to him to be most desirable, are usually summed up in one general appellation, and denominated the natural liberty of mankind' — and his doctrine of parliamentary sovereignty were the primary jurisprudential frameworks through which the American Founders understood both the British constitution they were challenging and the new constitution they were constructing.",
    "causes": [
      "The absence of systematic, accessible legal education in 18th-century England — legal training was conducted entirely through the Inns of Court, through apprenticeship, and through reading in practice, with no university-based legal education — created the need for a systematic, scholarly account of English common law that Blackstone's Commentaries filled, both justifying the new Vinerian Professorship and providing the textbook the common law tradition had lacked.",
      "The Enlightenment project of systematic, rational exposition of existing institutions — the effort to organise and justify all branches of knowledge in clear, comprehensive, rationally structured form — gave Blackstone's Commentaries its characteristic approach: the aspiration to present the entire body of English common law as a rational, principled system rather than a chaotic accumulation of precedents.",
      "The American colonial crisis — the constitutional debates of the 1760s–1770s over the limits of parliamentary authority, the rights of English subjects, and the nature of natural law — created the urgent demand in the American colonies for a systematic account of English constitutional law, which Blackstone's Commentaries supplied in volumes I–II just as the crisis was developing."
    ],
    "effects": [
      "Blackstone's Commentaries became the foundational legal text of American law — more widely read in pre-Revolutionary America than in England, and the primary reference for the American Founders — its influence on the Declaration of Independence, the Constitution, and the common law tradition of the United States is greater than that of any other single legal work.",
      "Abraham Lincoln's self-education in law through Blackstone's Commentaries — he later described reading it by firelight as a young man — is the most famous example of the Commentaries' role as the self-teaching manual of American lawyers for more than a century, and Lincoln's legal and constitutional thought was shaped fundamentally by Blackstone's framework.",
      "Blackstone's systematic organisation of English common law established the framework for subsequent legal scholarship and education — Jeremy Bentham's fierce critique of Blackstone (in A Fragment on Government, 1776) was the most important single contribution to legal positivism and the development of analytical jurisprudence, making the Commentaries the indispensable foil for the modernisation of legal theory."
    ],
    "relationships": [
      {"sourceSlug": "william-blackstone", "sourceName": "William Blackstone (1723–1780)", "verb": "AUTHORS", "targetSlug": "commentaries-on-the-laws-of-england-blackstone", "targetName": "Commentaries on the Laws of England (1765–1769)", "context": "Blackstone wrote the Commentaries as the first Vinerian Professor of English Law at Oxford — creating the systematic account of English common law that became the foundational legal text of the common law world."},
      {"sourceSlug": "commentaries-on-the-laws-of-england-blackstone", "sourceName": "Commentaries on the Laws of England", "verb": "SHAPES", "targetSlug": "american-constitutional-law", "targetName": "American constitutional and common law (Founders' generation)", "context": "Blackstone's Commentaries was the primary legal reference for the American Founders — more copies were sold in pre-Revolutionary America than in England, and its doctrines on natural rights and constitutional law were the intellectual foundations of American constitutional thought."},
      {"sourceSlug": "commentaries-on-the-laws-of-england-blackstone", "sourceName": "Commentaries (Blackstone)", "verb": "CRITIQUED_BY", "targetSlug": "jeremy-bentham", "targetName": "Jeremy Bentham's Fragment on Government (1776) and legal positivism", "context": "Bentham's fierce critique of Blackstone's natural law jurisprudence — published in the same year as the Declaration of Independence — was the most important contribution to legal positivism and analytical jurisprudence, making the Commentaries the indispensable foil for the modernisation of legal theory."}
    ],
    "places": [
      {"name": "Oxford (1765–1769, composition as Vinerian Professor)", "role": "Blackstone composed the Commentaries as the first Vinerian Professor of English Law at Oxford — the first systematic university-based legal education in England, which the Commentaries both embodied and justified"},
      {"name": "American colonies and United States (primary legal text, 1765–1870s)", "role": "Blackstone's Commentaries was the primary legal reference for the American Founders, the self-education manual of American lawyers for a century, and the foundational text of American common law — more influential in America than in its country of origin"}
    ],
    "subjects": ["English Law", "Early Modern Era", "Blackstone", "Common Law", "Legal History", "American Law", "Constitutional Law", "Legal Education"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Blackstone's Commentaries on the Laws of England (1765–1769) is the most influential work in the history of common law legal education — the foundational legal text of the American Founders, the self-education manual of Abraham Lincoln, and the systematic framework that shaped American constitutional and common law. Its influence on the Declaration of Independence, the Constitution, and the American legal tradition is greater than that of any other single legal work.",
      "significanceCategory": "world-changing"
    }
  }
},

"animal-farm": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783animal-farm.json",
  "slug": "animal-farm",
  "data": {
    "summary": "Animal Farm is the political allegory by George Orwell (Eric Arthur Blair, 1903–1950), published in August 1945 by Secker & Warburg — one of the most widely read political satires in world literature and one of Orwell's two masterpieces (alongside Nineteen Eighty-Four, 1949). Written in 1944 and rejected by multiple publishers (including T.S. Eliot at Faber, who found its anti-Soviet message politically inopportune), Animal Farm is a fairy story (as its subtitle calls it) in which the animals of Manor Farm, led by the pigs Napoleon and Snowball, overthrow their human farmer Mr Jones in the name of 'Animalism' (a transparent allegory for Marxism-Leninism) — and then watch as the pigs gradually assume all the privileges of the humans they replaced, culminating in Napoleon's tyranny and the corruption of the Seven Commandments of Animalism to 'All animals are equal, but some animals are more equal than others.'\n\nAnimal Farm is a precise political allegory of the Soviet Union from the 1917 Revolution to the Tehran Conference of 1943: Old Major is Marx/Lenin (the ideological founder whose vision is betrayed after his death), Napoleon is Stalin, Snowball is Trotsky (expelled from the farm/USSR and blamed for all subsequent problems), the pigs are the Communist Party, the dogs are the secret police (NKVD), Boxer the horse is the proletariat (loyal, hardworking, ultimately exploited and destroyed), and the farm's corruption mirrors the Soviet Union's descent from revolutionary idealism into Stalinist tyranny. Squealer (the propagandist pig who rewrites history and manipulates the other animals) is one of the most chilling portrayals of propaganda and political manipulation in literature.\n\nAnimal Farm has been translated into more than 70 languages and has sold tens of millions of copies worldwide — it is one of the most effective anti-totalitarian texts ever written, its fable form making its critique of Soviet communism accessible to readers of all ages and levels of political sophistication. It was used as Cold War propaganda by Western governments (the CIA funded an animated film adaptation in 1954) and has remained continuously in print as a canonical text of political literacy.",
    "causes": [
      "Orwell's disillusionment with Soviet communism — deepened by his experience fighting in the Spanish Civil War (1936–1937) with the POUM (Worker's Party of Marxist Unification), where he witnessed the Soviet-backed Communist suppression of independent leftist forces and the Stalinist purges — gave Animal Farm its specific political content and its urgent need to expose what Orwell saw as the greatest threat to democratic socialism: Soviet totalitarianism disguised as socialist idealism.",
      "The wartime political atmosphere in Britain — the Soviet Union's role as an Allied power after 1941 meant that criticism of Stalin was politically taboo, making Animal Farm difficult to publish despite its obvious literary quality — gave the novel its scandalous political context: Orwell was criticising an ally at the moment of greatest Allied solidarity, which multiple publishers found unacceptable.",
      "Orwell's conviction that the left's failure to criticise Soviet totalitarianism was corrupting democratic socialist politics — his belief that 'intellectual cowardice' about the USSR was the central political failure of the Western left — drove him to write Animal Farm as the clearest possible statement of what had actually happened to the Russian Revolution: its betrayal by the very class in whose name it was made."
    ],
    "effects": [
      "Animal Farm's 'All animals are equal, but some animals are more equal than others' is one of the most quoted sentences in 20th-century political literature — its encapsulation of the logic of revolutionary betrayal and the corruption of egalitarian ideals by those who claim to embody them has become the canonical statement of political cynicism about revolutionary movements.",
      "Animal Farm became one of the primary texts of Cold War Western political education — widely used in schools as an introduction to the critique of Soviet communism and totalitarianism — and its influence on the Western perception of the Soviet Union during the Cold War period was considerable, particularly in the early Cold War years when less information about the USSR was available.",
      "Animal Farm's commercial success (combined with Nineteen Eighty-Four) established Orwell as the canonical political moralist of the 20th century and made 'Orwellian' an adjective for political doublespeak and totalitarian manipulation — his two dystopian fictions together contributed more vocabulary to the English language's political discourse than any other literary works of the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "george-orwell", "sourceName": "George Orwell (1903–1950)", "verb": "AUTHORS", "targetSlug": "animal-farm", "targetName": "Animal Farm (1945)", "context": "Orwell wrote Animal Farm in 1944 following his experience in the Spanish Civil War — the allegory of the Russian Revolution's betrayal that he had been unable to publish during the wartime period of Soviet-Allied solidarity."},
      {"sourceSlug": "animal-farm", "sourceName": "Animal Farm (political allegory)", "verb": "ALLEGORISES", "targetSlug": "soviet-union", "targetName": "Soviet Union (1917 Revolution to Stalin's tyranny)", "context": "Animal Farm is a precise political allegory of the Soviet Union — Napoleon is Stalin, Snowball is Trotsky, Old Major is Marx/Lenin — depicting the betrayal of the revolutionary ideal by those who claim to embody it."},
      {"sourceSlug": "animal-farm", "sourceName": "Animal Farm", "verb": "CONTEMPORARY_WITH", "targetSlug": "nineteen-eighty-four", "targetName": "Nineteen Eighty-Four (Orwell, 1949)", "context": "Animal Farm (1945) and Nineteen Eighty-Four (1949) are Orwell's two dystopian masterpieces — together they constitute the most influential literary critique of totalitarianism in the 20th century and established 'Orwellian' as a political adjective."}
    ],
    "places": [
      {"name": "Britain (1944 composition, wartime political context)", "role": "Orwell wrote Animal Farm in wartime Britain — where the Soviet Union's role as an Allied power made criticism of Stalin politically taboo and led multiple publishers to reject the manuscript"},
      {"name": "Soviet Union (allegorical referent, 1917–1943)", "role": "The USSR from the 1917 Revolution to the Tehran Conference of 1943 is the precise allegorical referent of Animal Farm — each character and event corresponds to a historical figure or episode in Soviet history"}
    ],
    "subjects": ["English Literature", "Modern Era", "George Orwell", "Political Allegory", "Anti-Totalitarianism", "Soviet Union", "20th Century", "Dystopian Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Animal Farm (Orwell, 1945) is one of the most effective anti-totalitarian texts ever written — its precise allegory of the Soviet Union's revolutionary betrayal, translated into more than 70 languages and read by tens of millions, shaped the Western perception of Soviet communism during the Cold War. 'All animals are equal, but some animals are more equal than others' is the canonical statement of revolutionary corruption, and together with Nineteen Eighty-Four, Animal Farm made 'Orwellian' the defining political adjective of the 20th century.",
      "significanceCategory": "world-changing"
    }
  }
},

"and-then-there-were-none": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783and-then-there-were-none.json",
  "slug": "and-then-there-were-none",
  "data": {
    "summary": "And Then There Were None (published in the UK as Ten Little Niggers in 1939, later Ten Little Indians, finally standardised as And Then There Were None) is the mystery novel by Agatha Christie (1890–1976), published in November 1939 — with approximately 100 million copies sold, the best-selling mystery novel in history and one of the best-selling fiction books of all time, after the Bible and the works of Shakespeare. Ten people are invited to a remote island off the Devon coast under various pretexts by a mysterious host (U.N. Owen — 'Unknown') and are accused, via a gramophone recording, of murders they have each committed but for which they have escaped justice. One by one they are killed according to the verse of an old nursery rhyme ('Ten Little Indians'), and the mystery — who is the killer? — is solved only in a posthumous confession found in a sealed bottle after the events of the novel.\n\nAnd Then There Were None is Christie's most technically accomplished mystery novel — its premise (ten people on an isolated island, all of them murderers, one of them also the killer) is a virtuoso achievement in the logic of the locked-room mystery, taken to its logical extreme. The isolation of the island, the nursery-rhyme countdown, the systematic elimination of suspects (who are also victims), and the impossibility of the solution (there are no survivors left to be the killer) constitute the most rigorous and satisfying puzzle in the golden age detective fiction tradition. Christie's solution — which turns the detective story's usual logic inside out — was widely considered impossible when she first conceived it, and it has never been successfully plagiarised.\n\nAnd Then There Were None has been adapted for stage, screen, radio, and television more than two dozen times — including Christie's own stage adaptation (1943, which changed the ending), multiple film adaptations (1945, 1965, 2015), and a BBC television production (2015) — and its premise and structure have influenced virtually every subsequent thriller in which characters are killed one by one in isolation.",
    "causes": [
      "Christie's technical challenge to herself — to construct a mystery in which all ten characters are simultaneously suspects and victims, in which there are no survivors, and in which the solution is both impossible-seeming and logically rigorous — gave And Then There Were None its distinctive structure and its status as the most difficult puzzle she ever set herself.",
      "The golden age detective fiction tradition — the genre of the highly stylised, rule-bound mystery puzzle established by Christie, Dorothy L. Sayers, John Dickson Carr, and their contemporaries in the 1920s–1940s — provided the formal conventions (the isolated location, the limited cast of suspects, the fair-play revelation of clues) that Christie both drew on and radically extended in And Then There Were None.",
      "The outbreak of World War II — And Then There Were None was published in November 1939, two months after Britain declared war on Germany — gave the novel's theme of guilt, justice, and the question of who has the right to punish unpunished murderers a contemporary resonance: the novel's isolated judge-executioner (whose identity is the mystery's solution) is a figure of extrajudicial punishment that reflects the moral disorientation of a world about to undergo enormous violence."
    ],
    "effects": [
      "And Then There Were None's commercial success — with approximately 100 million copies sold, it is the best-selling mystery novel in history — established Agatha Christie's reputation as the 'Queen of Crime' and demonstrated that the golden age detective puzzle could achieve mass-market popularity comparable to any other fiction genre.",
      "The novel's premise — ten characters isolated on an island, killed one by one — became the foundational template for the thriller subgenre of the 'isolated group under threat', directly influencing Ira Levin (Ten Little Indians' echo in works like Deathtrap), and more broadly shaping the thriller, horror, and video game genres (the 'battle royale' format of games like Cluedo, Among Us, and the Danganronpa game series).",
      "Christie's own stage adaptation (1943) — which changed the original ending to a romance resolution — demonstrated the commercial and theatrical flexibility of the premise and became one of the longest-running plays in theatrical history, alongside The Mousetrap, establishing Christie as the most successful dramatist of the detective story."
    ],
    "relationships": [
      {"sourceSlug": "agatha-christie", "sourceName": "Agatha Christie (1890–1976)", "verb": "AUTHORS", "targetSlug": "and-then-there-were-none", "targetName": "And Then There Were None (1939)", "context": "Christie wrote And Then There Were None as her most technically ambitious mystery — the locked-room puzzle taken to its logical extreme, which she feared might be unsolvable and which became the best-selling mystery novel in history."},
      {"sourceSlug": "and-then-there-were-none", "sourceName": "And Then There Were None", "verb": "ESTABLISHES", "targetSlug": "isolated-group-thriller", "targetName": "Isolated group under threat thriller (film, game, novel subgenre)", "context": "The novel's premise of ten characters isolated and killed one by one became the foundational template for the isolated-group thriller — directly influencing the horror and thriller genres and the 'battle royale' video game format."},
      {"sourceSlug": "and-then-there-were-none", "sourceName": "And Then There Were None", "verb": "BEST_SELLING", "targetSlug": "mystery-novel-genre", "targetName": "Mystery novel genre (golden age detective fiction)", "context": "With approximately 100 million copies sold, And Then There Were None is the best-selling mystery novel in history — its commercial success established Christie's dominance of the golden age detective fiction tradition and demonstrated the genre's mass-market potential."}
    ],
    "places": [
      {"name": "Devon coast, England (fictional Soldier Island, narrative setting)", "role": "The isolated island off the Devon coast — Soldier Island (sometimes Nigger Island in original editions), accessible only by boat and cut off by storms — is the locked-room setting that gives the novel its claustrophobic tension"},
      {"name": "Global (publication 1939, 100 million copies sold)", "role": "And Then There Were None has sold approximately 100 million copies worldwide in dozens of languages — making it the best-selling mystery novel in history and one of the best-selling fiction books ever published"}
    ],
    "subjects": ["Detective Fiction", "Modern Era", "Agatha Christie", "Mystery Novel", "Golden Age Detective Fiction", "English Literature", "20th Century", "Bestseller"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "And Then There Were None (Christie, 1939) is the best-selling mystery novel in history — approximately 100 million copies sold — and Christie's most technically accomplished work. Its premise of ten isolated characters killed one by one became the foundational template for the isolated-group thriller, influencing horror, crime, and video game genres. Together with The Mousetrap, it established Christie as the most commercially successful crime writer of the 20th century.",
      "significanceCategory": "highly-significant"
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
