#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 40 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: kama-sutra, la-celestina,
          day-of-infamy-speech-1941, heimskringla,
          around-the-world-in-eighty-days, chai-symbol,
          natural-approach, philology
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-40-may2026"

ENRICHMENTS = {

"kama-sutra": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780kama-sutra.json",
  "slug": "kama-sutra",
  "data": {
    "summary": "The Kama Sutra (Sanskrit: कामसूत्र, Kāmasūtra, 'Aphorisms on Love/Pleasure') is an ancient Indian Sanskrit text on sexuality, eroticism, and emotional fulfilment in human life, composed by the sage Vātsyāyana — probably in the 3rd century CE (estimated range: 2nd–4th century CE) — and the most well-known work on kama (desire, pleasure, love) in the Sanskrit literary and philosophical tradition. Despite its modern reputation as primarily a sex manual, only one of its seven books (the Samprayogika, Book 2) deals with sexual techniques in detail; the remaining six books address topics including the nature and acquisition of kama (Book 1), the organisation of a householder's daily life (Book 3), finding a wife (Book 4), maintaining a wife and dealing with other women's wives (Book 5), the conduct of courtesans (Book 6), and occult practices (Book 7). The Kama Sutra thus presents a comprehensive philosophy of love and desire within the framework of the three classical Hindu aims of human life (purusharthas): dharma (right conduct), artha (wealth), and kama (pleasure).\n\nVātsyāyana's Kama Sutra synthesised and condensed an earlier, much larger tradition of kama shastra (science of love) texts — he explicitly cites and condensed the works of earlier authors (Babhravya, Gonardiya, Suvarnanabha, and others) whose texts are now lost — into a single comprehensive work of approximately 1,250 verses. The text's treatment of sexuality is remarkably systematic and non-judgmental by the standards of any period: it includes extended discussion of female sexuality, desire, and satisfaction; it discusses third-gender (tritiya-prakriti) individuals; and it frames sexual life as a legitimate and important domain of human knowledge and cultivation, within the dharmic framework of the ideal householder's life.\n\nThe Kama Sutra was first translated into English by Richard Burton and F. F. Arbuthnot in 1883 — a private edition distributed to subscribers to avoid obscenity prosecution — and has since been translated into dozens of languages and become one of the most widely read and discussed ancient texts in the world, often stripped of its philosophical and cultural context to be read as a sexual guidebook. This modern reception has obscured the text's original significance as a comprehensive philosophy of the erotic life within the framework of classical Hindu thought.",
    "causes": [
      "The ancient Indian kama shastra tradition — the long-standing tradition of scholarly literature on the science of love and sexual arts, attributed to works of Babhravya and others, which Vātsyāyana explicitly condensed and synthesised — provided the intellectual context and source material from which the Kama Sutra was compiled.",
      "The classical Hindu framework of the four purusharthas (aims of life) — dharma (right conduct), artha (wealth/success), kama (pleasure/desire), and moksha (liberation) — provided the philosophical justification for the Kama Sutra as a legitimate domain of systematic human knowledge: kama is one of the three recognised aims of life, and its systematic study is therefore a legitimate scholarly enterprise.",
      "The social context of the ideal Sanskrit-culture householder — the wealthy, educated urbanite (nagaraka) whose cultivation of the arts of love, conversation, music, and aesthetic pleasure is presented as the ideal of civilised life — provided the practical social context for the Kama Sutra's prescriptions, which are addressed to the educated, leisured male householder of the urban Sanskrit cultural world."
    ],
    "effects": [
      "The Kama Sutra's influence on the Indian erotic literary and artistic tradition — the kamashastra tradition that continued after Vātsyāyana (Kokkoka's Ratirahasya, c. 11th century; Kalyana Malla's Ananga Ranga, c. 15th–16th century) and the erotic temple sculpture tradition (Khajuraho, Konarak) — established it as the foundational text of the Indian science of love, with a continuous tradition of commentary and adaptation.",
      "Richard Burton's English translation (1883) — published privately to avoid obscenity prosecution — initiated the Western reception of the Kama Sutra, which transformed it from a specialist Sanskrit text to a globally known work, and stimulated the more general European engagement with Indian philosophy and culture that was part of the 19th-century Orientalist tradition.",
      "The Kama Sutra's modern global reception — its status as one of the most famous ancient texts in the world, widely read and discussed outside its cultural context — has made it a reference point in contemporary debates about sexuality, gender, and the diversity of human sexual cultures, often used to relativise Western cultural assumptions about sexuality."
    ],
    "relationships": [
      {"sourceSlug": "kama-sutra", "sourceName": "Kama Sutra (Vātsyāyana, c. 3rd century CE)", "verb": "PART_OF", "targetSlug": "ancient-indian-philosophical-tradition", "targetName": "Ancient Indian philosophical tradition (kama shastra)", "context": "The Kama Sutra is the primary surviving text of the kama shastra tradition — the ancient Indian scholarly literature on the science of love — synthesising and condensing earlier works within the framework of the classical Hindu purusharthas."},
      {"sourceSlug": "kama-sutra", "sourceName": "Kama Sutra (Burton translation, 1883)", "verb": "TRANSLATED_BY", "targetSlug": "richard-burton", "targetName": "Sir Richard Burton (1821–1890, explorer and translator)", "context": "Burton's English translation (1883) — published privately to avoid obscenity laws — initiated the Western reception of the Kama Sutra and its transformation from a Sanskrit philosophical text to a globally known work."},
      {"sourceSlug": "kama-sutra", "sourceName": "Kama Sutra (erotic arts, householder philosophy)", "verb": "INFLUENCES", "targetSlug": "khajuraho-temples", "targetName": "Khajuraho temple sculpture (erotic art, 10th–12th century)", "context": "The Kama Sutra's philosophical framework of the erotic arts within the householder's life influenced the tradition of erotic temple sculpture in medieval India, represented most famously by the Khajuraho temples."}
    ],
    "places": [
      {"name": "Northern India (Sanskrit cultural sphere, 3rd century CE)", "role": "The Kama Sutra was composed in the Sanskrit cultural sphere of northern India — probably during the Gupta period (320–550 CE) or slightly before — addressed to the educated, urban householder (nagaraka) of the Sanskrit cultural world"},
      {"name": "Global (Burton translation 1883, worldwide modern reception)", "role": "The Kama Sutra's global reception began with Burton's 1883 English translation — it has since been translated into dozens of languages and become one of the most widely known ancient texts in the world"}
    ],
    "subjects": ["Ancient Indian Literature", "Ancient Era", "Sanskrit Literature", "Hindu Philosophy", "Sexuality", "Classical India", "Kama", "Vatsyayana"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Kama Sutra (Vātsyāyana, c. 3rd century CE) is the primary text of the ancient Indian kama shastra tradition — a comprehensive philosophy of love and desire within the classical Hindu purusharthas framework. Widely misread as merely a sex manual, it is a sophisticated Sanskrit philosophical text addressing the full range of the ideal householder's erotic life. Its influence on Indian erotic art, literature, and temple sculpture, and its global reception following Burton's 1883 translation, make it one of the most widely known ancient texts in the world.",
      "significanceCategory": "highly-significant"
    }
  }
},

"la-celestina": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780la-celestina.json",
  "slug": "la-celestina",
  "data": {
    "summary": "La Celestina (full title: Tragicomedia de Calisto y Melibea, 'Tragicomedy of Calisto and Melibea') is a Spanish literary work first published as La Comedia de Calisto y Melibea in 1499 (Burgos, 16 acts) and then expanded to 21 acts in the 1502 Tragicomedia edition — attributed primarily to Fernando de Rojas (c. 1465–1541), a converso (Jewish convert to Christianity) lawyer from Puebla de Montalbán, though the first act may have an earlier, anonymous author. La Celestina is written entirely in dialogue (it has no narration), making it technically a dialogue novel or a play too long for performance — its 21 acts of extended dramatic dialogue represent one of the most important innovations in Spanish literary history, a text that stands between the medieval dialogue tradition and the modern novel and drama. The title character, Celestina, is a bawd (procuress, alcahueta) hired by the young nobleman Calisto to help him seduce the noble young woman Melibea — a character of such theatrical power and psychological complexity that she has been ranked alongside Hamlet, Don Quixote, and Falstaff as one of the great European literary characters.\n\nLa Celestina's plot moves from social comedy to catastrophe: Celestina's manipulation of Calisto and Melibea's servants (Sempronio and Pármeno, bribed with promises of sexual favours from the prostitutes Elicia and Areúsa) leads to her own murder by her accomplices (in a dispute over the gold chain Calisto gave her as payment), the execution of the murderers, Calisto's accidental fall from a wall while leaving Melibea after a night visit, and Melibea's suicide by throwing herself from a tower as her father Pleberio watches in horror. The tragedy of La Celestina is unique in 15th-century literature for its complete rejection of providential or divine resolution: there is no redemption, no justice, and no consolation — only the catastrophic consequences of desire, greed, and moral corruption.\n\nLa Celestina was enormously influential in the development of Spanish and European literature — it was widely read and imitated in the 16th century, translated into Italian (1505), French (1527), English (1530), German, and other languages, and its influence has been traced in Shakespeare (Romeo and Juliet shares its plot of tragic young lovers), Lope de Vega, Calderón, and the 16th-century Spanish picaresque tradition.",
    "causes": [
      "The converso cultural context of Fernando de Rojas — as a Jewish convert to Christianity in late 15th-century Spain, operating under the Inquisition's surveillance, Rojas's ambiguous position in Spanish society informed La Celestina's radical moral vision: the text's rejection of providential consolation and its dark portrayal of social corruption can be read as the perspective of a socially marginal author.",
      "The late medieval Spanish dialogue tradition — the tradition of extended prose dialogues dealing with love, desire, and the moral consequences of passion (influenced by Boccaccio's Fiammetta, the Libro de Buen Amor, and the sentimental romance tradition) — provided the generic models from which La Celestina's dialogue form was developed.",
      "The social conditions of late 15th-century Castile — the fluid, transitional society of the emerging Spanish Renaissance, with its mixing of noble and non-noble urban cultures, the precarious social position of conversos, and the monetisation of social relations — provided the social texture of La Celestina's world: a world in which old social hierarchies are being dissolved by money and desire."
    ],
    "effects": [
      "La Celestina's influence on the development of Spanish literature was foundational — the Celestina character influenced the tradition of the literary bawd and procuress in Spanish drama and prose (the prostitute characters in the picaresque novel, the alcahueta figure in Lope de Vega and Calderón), and the text's extended dramatic dialogue influenced the development of the Spanish comedia.",
      "La Celestina's influence on European literature extended through translation — the Italian, French, English, and German translations of the 16th century introduced the Celestina character and the tragic plot of young lovers destroyed by social forces to the European literary tradition, with traces in Shakespeare's Romeo and Juliet and in the English and Italian Renaissance dramatic tradition.",
      "La Celestina's radical moral vision — its rejection of providential consolation, its portrayal of social corruption, and its tragic ending without redemption — represents one of the earliest examples of what would become the modern secular tragic vision in European literature, anticipating the moral outlook of Renaissance and early modern tragedy."
    ],
    "relationships": [
      {"sourceSlug": "fernando-de-rojas", "sourceName": "Fernando de Rojas (c. 1465–1541)", "verb": "AUTHORS", "targetSlug": "la-celestina", "targetName": "La Celestina (Tragicomedia de Calisto y Melibea, 1499/1502)", "context": "Rojas authored La Celestina — the most important Spanish literary work of the 15th century, a 21-act dialogue narrative of tragic love and social corruption that stands between the medieval dialogue and the modern novel."},
      {"sourceSlug": "la-celestina", "sourceName": "La Celestina (Celestina character, procuress)", "verb": "INFLUENCES", "targetSlug": "spanish-golden-age-literature", "targetName": "Spanish Golden Age literature (drama, picaresque)", "context": "The Celestina character influenced the tradition of the literary bawd in Spanish drama and prose — appearing in the picaresque novel, Lope de Vega, and Calderón — making La Celestina one of the foundational texts of the Spanish literary tradition."},
      {"sourceSlug": "la-celestina", "sourceName": "La Celestina (tragic young lovers, European reception)", "verb": "INFLUENCES", "targetSlug": "romeo-and-juliet-shakespeare", "targetName": "Romeo and Juliet (Shakespeare, c. 1595)", "context": "La Celestina's plot of tragic young lovers destroyed by social forces — translated into Italian (1505), French, and English in the 16th century — has been traced as an influence on Shakespeare's Romeo and Juliet."}
    ],
    "places": [
      {"name": "Burgos and Salamanca, Spain (first editions 1499, 1502; converso cultural context)", "role": "La Celestina was first published in Burgos (1499) and Salamanca — Fernando de Rojas's Salamanca university context (he was a law student there) and the converso cultural world of late 15th-century Castile shaped the text's radical moral vision"},
      {"name": "Europe (Italian, French, English translations, 16th century)", "role": "La Celestina was widely translated across Europe in the 16th century — Italian (1505), French (1527), English (1530) — spreading the Celestina character and the tragic young lovers plot to European literary culture"}
    ],
    "subjects": ["Spanish Literature", "Medieval Era", "Fernando de Rojas", "Renaissance Literature", "Drama", "15th Century", "Converso Literature", "Dialogue"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "La Celestina (Rojas, 1499/1502) is the most important Spanish literary work of the 15th century and one of the foundational texts of European Renaissance literature. The Celestina character is one of the great figures of European literary tradition. Its influence on Spanish drama, the picaresque, and European tragedy (including Shakespeare's Romeo and Juliet via translation) was foundational. Its radical secular tragic vision — rejecting providential consolation — anticipates the moral outlook of modern secular tragedy.",
      "significanceCategory": "highly-significant"
    }
  }
},

"day-of-infamy-speech-1941": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781day-of-infamy-speech-1941.json",
  "slug": "day-of-infamy-speech-1941",
  "data": {
    "summary": "The 'Day of Infamy' speech (formally known as the 'Address to Congress Requesting a Declaration of War with Japan') is the speech delivered by United States President Franklin D. Roosevelt (1882–1945) to a joint session of the US Congress at 12:30 PM on 8 December 1941 — the day after the Japanese attack on the US naval base at Pearl Harbor, Hawaii (7 December 1941) — requesting a declaration of war against Japan. Roosevelt's speech is 506 words long, one of the shortest and most concise war messages in US presidential history, and its opening line — 'Yesterday, December 7th, 1941 — a date which will live in infamy — the United States of America was suddenly and deliberately attacked by naval and air forces of the Empire of Japan' — is one of the most famous sentences in American political rhetoric. Within one hour of the speech's conclusion, Congress passed the declaration of war (with one dissenting vote: Jeannette Rankin of Montana), formally bringing the United States into World War II.\n\nRoosevelt delivered the speech before approximately 1,000 members of Congress and Cabinet officials, but it was broadcast live on radio to an estimated 81 million American listeners — the largest radio audience in US history to that point. The speech's rhetorical power derived from its deliberate simplicity: Roosevelt listed, in measured, factual tones, the sequence of Japanese attacks across the Pacific (Pearl Harbor, Malaya, Hong Kong, Guam, the Philippine Islands, Wake Island, Midway Island) that had occurred over the previous 24 hours, building to the declaration that the United States was in a state of war. The speech transformed American public opinion — isolationism, which had been a powerful force in US politics through the late 1930s, effectively ended with Pearl Harbor and Roosevelt's address — and united the American public behind the war effort.\n\nThe 'Day of Infamy' speech is one of the most consequential speeches in US presidential history — it ended American neutrality in World War II and set in motion the American war effort that would be decisive in the Allied victory. Roosevelt's original draft had used the phrase 'a date which will live in world history', but Roosevelt himself changed it in manuscript to 'a date which will live in infamy' — one of the most celebrated examples of presidential editorial revision in American rhetorical history.",
    "causes": [
      "The Japanese attack on Pearl Harbor (7 December 1941) — the surprise attack on the US Pacific Fleet at anchor in Pearl Harbor, Hawaii, which destroyed or damaged 18 ships (including 8 battleships) and killed 2,403 Americans — was the direct cause and subject of Roosevelt's speech: the attack made the declaration of war constitutionally necessary and politically inevitable.",
      "The American isolationist political tradition — the powerful domestic opposition to US involvement in European and Asian wars that had constrained US foreign policy through the late 1930s — created the political context for Roosevelt's rhetorical strategy: the speech needed to build public support for a war that isolationist sentiment had previously resisted, and the deliberate narrative of Japanese aggression was designed to unite public opinion.",
      "Roosevelt's long preparation for the potential need to bring the United States into the war — his 'Lend-Lease' programme, his Atlantic Charter meeting with Churchill (August 1941), and his administration's gradual steps toward supporting the Allies — created the geopolitical context in which Pearl Harbor provided the decisive casus belli."
    ],
    "effects": [
      "The speech ended American isolationism and brought the United States into World War II — the congressional declaration of war passed within one hour of the speech's conclusion with only one dissenting vote, setting in motion the American military mobilisation that would become decisive in the Allied victory in Europe and the Pacific.",
      "The 'Day of Infamy' speech united American public opinion behind the war effort with extraordinary speed — isolationism effectively collapsed after Pearl Harbor, and Roosevelt's measured, factual rhetoric channelled the shock and anger of the American public into determination rather than panic.",
      "The speech's impact on American political rhetoric has been enduring — the phrase 'a date which will live in infamy' became one of the most cited presidential utterances in US history, and the speech itself became a reference point for presidential crisis communication, studied in American rhetoric and political science as an example of effective presidential speech in a moment of national crisis."
    ],
    "relationships": [
      {"sourceSlug": "franklin-d-roosevelt", "sourceName": "Franklin D. Roosevelt (1882–1945)", "verb": "DELIVERS", "targetSlug": "day-of-infamy-speech-1941", "targetName": "Day of Infamy speech (8 December 1941)", "context": "Roosevelt delivered the 'Day of Infamy' speech to Congress on 8 December 1941 — the 506-word address requesting a declaration of war against Japan, broadcast to 81 million radio listeners, that brought the United States into World War II."},
      {"sourceSlug": "day-of-infamy-speech-1941", "sourceName": "Day of Infamy speech (Pearl Harbor, war declaration)", "verb": "RESPONDS_TO", "targetSlug": "attack-on-pearl-harbor", "targetName": "Attack on Pearl Harbor (7 December 1941)", "context": "The Day of Infamy speech was the direct political response to the Japanese attack on Pearl Harbor — Roosevelt's address to Congress requesting the declaration of war that brought the United States into World War II."},
      {"sourceSlug": "day-of-infamy-speech-1941", "sourceName": "Day of Infamy speech (US entry into WWII)", "verb": "INITIATES", "targetSlug": "us-in-world-war-ii", "targetName": "United States participation in World War II (1941–1945)", "context": "The Day of Infamy speech and the subsequent declaration of war formally brought the United States into World War II — the American military mobilisation that followed was decisive in the Allied victory in Europe and the Pacific."}
    ],
    "places": [
      {"name": "Washington D.C. (US Capitol, joint session of Congress, 8 December 1941)", "role": "Roosevelt delivered the Day of Infamy speech to a joint session of Congress at the US Capitol on 8 December 1941 — broadcast live to 81 million American radio listeners, one of the largest broadcast audiences in US history"},
      {"name": "Pearl Harbor, Hawaii (site of attack, subject of speech)", "role": "Pearl Harbor — the US naval base in Hawaii attacked by Japanese forces on 7 December 1941 — is the primary subject of the Day of Infamy speech: Roosevelt's listing of the Japanese attacks across the Pacific that day built to the declaration of war"}
    ],
    "subjects": ["American History", "Modern Era", "Franklin Roosevelt", "World War II", "Presidential Rhetoric", "Pearl Harbor", "20th Century", "Political Speech"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The 'Day of Infamy' speech (Roosevelt, 8 December 1941) is one of the most consequential speeches in US presidential history — bringing the United States into World War II, ending American isolationism, and uniting American public opinion behind the war effort with extraordinary speed. Its opening sentence ('a date which will live in infamy') is one of the most famous in American political rhetoric. The American military mobilisation it initiated was decisive in the Allied victory.",
      "significanceCategory": "world-changing"
    }
  }
},

"heimskringla": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782heimskringla.json",
  "slug": "heimskringla",
  "data": {
    "summary": "Heimskringla (Old Norse: 'The Circle of the World', or 'The Orb of the World') is a collection of sagas of the Norwegian kings (konungasögur) written in Old Norse by the Icelandic scholar and statesman Snorri Sturluson (1179–1241), probably composed c. 1230 CE — the most comprehensive and historically authoritative account of the Norwegian kings from the legendary origins of the Norse royal dynasties to the reign of Magnus Erlingsson (d. 1184), and the primary source for the history of Norway and Scandinavia from the Viking Age to the 12th century. Heimskringla comprises sixteen sagas, beginning with the Ynglinga saga (a mythological account of the origins of the Yngling dynasty, drawing on Snorri's Prose Edda, Scandinavian mythology, and the traditions of the Swedish royal house) and continuing through the historical sagas of the Norwegian kings: Hákon góði, Óláfr Tryggvason, Óláfr Haraldsson (St. Olaf), Magnús góði, Haráldr harðráði, and others, concluding with the saga of Magnus Erlingsson.\n\nSnorri Sturluson is the most important figure in the preservation of Old Norse literary and historical tradition — his Prose Edda (a handbook of Norse mythology and poetic technique, c. 1220) and Heimskringla together constitute the primary sources for our knowledge of Norse mythology, the skaldic poetic tradition, and the history of early medieval Norway. Snorri was himself a major Icelandic political figure — a chieftain, twice lawspeaker of the Althing (Iceland's parliament), and an important player in the complex Norwegian-Icelandic political relations of the 13th century — who was eventually assassinated in 1241 on the orders of the Norwegian King Hákon Hákonarson.\n\nHeimdskringla's historical method — Snorri explicitly distinguishes between myth, legendary narrative, and historical testimony, and appeals to skaldic poetry as his most reliable source ('for we believe what is said in those poems to be true') — represents a sophisticated early medieval approach to historical evidence that anticipates modern historiographical concerns. Snorri's engagement with the tension between legendary tradition and historical plausibility makes Heimskringla one of the most intellectually sophisticated historical works of the medieval period.",
    "causes": [
      "Snorri Sturluson's extraordinary learning — his mastery of Old Norse literature, skaldic poetry, and the Norwegian dynastic traditions, combined with his political engagement with the Norwegian royal court — provided the intellectual and practical motivation for Heimskringla: Snorri was commissioned by the Norwegian king Hákon IV and Earl Skúli to produce an authoritative account of the Norwegian kings.",
      "The 13th-century Icelandic literary golden age — the period of intensive saga composition that produced the Icelandic family sagas (Íslendingasögur), the mythological sagas (fornaldarsögur), and the kings' sagas (konungasögur) — created the cultural context for Snorri's historical work: Heimskringla is both the culmination of the kings' saga tradition and a major contribution to the 13th-century Icelandic literary achievement.",
      "The political relationship between Norway and Iceland in the 13th century — Iceland's gradual subordination to Norwegian royal authority (formalised in 1262–64) — provided the political context for Snorri's engagement with Norwegian royal history: his Heimskringla reflects his complex engagement with the Norwegian crown, both as client and as an autonomous Icelandic chieftain."
    ],
    "effects": [
      "Heimskringla's preservation of Norse historical tradition and skaldic poetry — Snorri quotes hundreds of stanzas of skaldic verse as historical evidence — made it the primary source for the history of Norway and Scandinavia from the Viking Age to the 12th century, and for the preservation of the skaldic poetic tradition that would otherwise be largely lost.",
      "Heimskringla's influence on Scandinavian national historiography was foundational — it was the primary source for the romantic national histories of Norway, Sweden, and Denmark in the 19th century, shaping the nationalist constructions of Viking Age identity that influenced Scandinavian literature, art, and political culture.",
      "The Prose Edda and Heimskringla together make Snorri Sturluson the single most important figure in the preservation of Norse literary and mythological tradition — without Snorri, much of our knowledge of Norse mythology, skaldic poetry, and Viking Age Scandinavian history would be lost."
    ],
    "relationships": [
      {"sourceSlug": "snorri-sturluson", "sourceName": "Snorri Sturluson (1179–1241)", "verb": "AUTHORS", "targetSlug": "heimskringla", "targetName": "Heimskringla (c. 1230 CE)", "context": "Snorri composed Heimskringla c. 1230 — the primary source for the history of the Norwegian kings from the legendary origins to the 12th century, and the most comprehensive account of Viking Age Scandinavia."},
      {"sourceSlug": "heimskringla", "sourceName": "Heimskringla (Norwegian kings, Viking Age history)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "viking-age-history", "targetName": "Viking Age Scandinavian history", "context": "Heimskringla is the primary source for the history of Norway and Scandinavia from the Viking Age to the 12th century — Snorri's citations of skaldic poetry as historical evidence preserve hundreds of stanzas that would otherwise be lost."},
      {"sourceSlug": "heimskringla", "sourceName": "Heimskringla (Prose Edda companion)", "verb": "COMPLEMENTS", "targetSlug": "prose-edda", "targetName": "Prose Edda (Snorri Sturluson, c. 1220)", "context": "Heimskringla and the Prose Edda together constitute Snorri's dual contribution to the preservation of Norse tradition — the Prose Edda preserving Norse mythology and skaldic technique, Heimskringla preserving Norwegian royal history."}
    ],
    "places": [
      {"name": "Iceland and Norway (Snorri Sturluson's world, c. 1230)", "role": "Heimskringla was composed in Iceland by the Icelandic chieftain Snorri Sturluson, in the context of his complex political relationship with the Norwegian royal court — it covers the history of Norway from legendary origins to the 12th century"},
      {"name": "Scandinavia (subject matter, Viking Age Norway and its kings)", "role": "Heimskringla covers the history of the Norwegian kings — from the Yngling dynasty's Swedish origins through the Viking Age kings to Magnus Erlingsson — making it the foundational text for Scandinavian medieval history"}
    ],
    "subjects": ["Old Norse Literature", "Medieval Era", "Snorri Sturluson", "Viking Age", "Norwegian History", "Kings' Sagas", "Medieval Historiography", "Norse Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Heimskringla (Snorri Sturluson, c. 1230) is the primary source for Viking Age Scandinavian history and Norse literary tradition — comprising sixteen sagas of the Norwegian kings from legendary origins to the 12th century, and preserving hundreds of stanzas of skaldic poetry. Snorri's sophisticated historical method (appealing to skaldic verse as primary evidence) anticipates modern historiography. Alongside the Prose Edda, Heimskringla makes Snorri the single most important figure in the preservation of Norse literary and historical tradition.",
      "significanceCategory": "highly-significant"
    }
  }
},

"around-the-world-in-eighty-days": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783around-the-world-in-eighty-days.json",
  "slug": "around-the-world-in-eighty-days",
  "data": {
    "summary": "Around the World in Eighty Days (French: Le Tour du monde en quatre-vingts jours) is an adventure novel by Jules Verne (1828–1905), first published as a serial in Le Temps (6 November–22 December 1872), then in book form by Pierre-Jules Hetzel (1873), and one of the most popular and widely translated French novels of the 19th century. The novel follows the meticulous, punctual English gentleman Phileas Fogg — member of the Reform Club in London, a man of clockwork habits — who bets £20,000 (half his fortune) that he can circumnavigate the globe in eighty days, a feat that the advances of steam travel and the recent opening of the Suez Canal (1869) and the completion of the transcontinental US railroad (1869) have made theoretically possible. Accompanied by his newly hired French manservant Passepartout, Fogg travels from London through the Suez Canal to India (by train across the subcontinent), then to Hong Kong, Yokohama, San Francisco (by steamer), across North America (by train, encountering a snowstorm, a Sioux attack on the train, and a missing bridge), back to New York and across the Atlantic to Liverpool — and then believes he has missed his deadline by a day, only to discover that by travelling eastward he has gained a day, arriving at the Reform Club precisely on time.\n\nAround the World in Eighty Days is one of the founding texts of the adventure novel as a genre — its combination of geographical suspense, technological modernity (steam trains, steamships, the telegraph), and the puzzle-plot of the wager created the template for the adventure story in which the entire world is the stage. The novel reflects the Victorian globalisation of the 1870s — the steamship and railway networks that connected the British Empire, the opening of the Suez Canal, and the completion of the US transcontinental railroad — presenting a world in which the telegraph and steam power have, for the first time, made the circumnavigation of the globe a matter of timetables rather than years of sailing.\n\nAround the World in Eighty Days has been adapted into films at least seven times (the most famous being the 1956 Michael Anderson film starring David Niven as Fogg) and has entered the cultural imagination as the archetypal adventure of speed, global reach, and the conquest of distance by technology.",
    "causes": [
      "The technological transformation of global travel in the 1860s–1870s — the opening of the Suez Canal (November 1869), the completion of the US transcontinental railroad (May 1869), and the expansion of steamship networks — created the factual premise of the novel: that circumnavigation in eighty days was now technologically feasible, and that this was a matter of public fascination and newspaper speculation.",
      "The Victorian culture of speed, progress, and technological achievement — the celebration of steam power, railway engineering, and the telegraph as markers of civilisational advance — provided the cultural context for Verne's novel: the adventure plot is organised around the spectacular feats of Victorian technology and the map of the British Empire's global reach.",
      "Jules Verne's collaboration with his publisher Pierre-Jules Hetzel — whose publishing philosophy of 'voyages extraordinaires' (novels combining adventure narrative with scientific and geographical information) provided the generic framework for Around the World in Eighty Days — shaped the novel's combination of adventure, education, and entertainment."
    ],
    "effects": [
      "Around the World in Eighty Days inspired real-world circumnavigation races — Nellie Bly's famous 1889 circumnavigation attempt (completed in 72 days, beating Fogg's fictional record) was directly inspired by the novel, demonstrating fiction's capacity to inspire reality.",
      "The novel's global reach and popularity — translated into virtually every language and adapted for film, television, theatre, and comic books — made Phileas Fogg and his eighty-day journey one of the most recognisable adventure narratives in world popular culture, and contributed substantially to Jules Verne's status as the most widely translated French author in history.",
      "Around the World in Eighty Days contributed to the genre of the adventure novel and the 'race against time' plot structure — its combination of meticulous scheduling, geographical suspense, and obstacle-overcoming became a template for adventure narrative that influenced Rider Haggard, Conan Doyle, and the 20th-century thriller genre."
    ],
    "relationships": [
      {"sourceSlug": "jules-verne", "sourceName": "Jules Verne (1828–1905)", "verb": "AUTHORS", "targetSlug": "around-the-world-in-eighty-days", "targetName": "Around the World in Eighty Days (1872/1873)", "context": "Verne published Around the World in Eighty Days as a serial in Le Temps in 1872 — one of his most popular 'voyages extraordinaires', translated into virtually every language and adapted for film seven times."},
      {"sourceSlug": "around-the-world-in-eighty-days", "sourceName": "Around the World in Eighty Days (Nellie Bly circumnavigation)", "verb": "INSPIRES", "targetSlug": "nellie-bly", "targetName": "Nellie Bly (1864–1922, 72-day circumnavigation 1889)", "context": "Nellie Bly's 1889 real-world circumnavigation — completed in 72 days, beating Fogg's fictional record — was directly inspired by Verne's novel, demonstrating fiction's capacity to inspire real achievements."},
      {"sourceSlug": "around-the-world-in-eighty-days", "sourceName": "Around the World in Eighty Days (Victorian globalisation)", "verb": "REFLECTS", "targetSlug": "suez-canal", "targetName": "Suez Canal (opened November 1869)", "context": "Around the World in Eighty Days reflects the Victorian technological globalisation of the 1870s — the Suez Canal (1869), the US transcontinental railroad (1869), and steamship networks are the factual basis for the novel's premise."}
    ],
    "places": [
      {"name": "London (Reform Club, start and finish of Fogg's journey)", "role": "The Reform Club in London — where Fogg makes the £20,000 bet — is the symbolic start and finish of the circumnavigation, emblematic of the Victorian British confidence that the world can be circled in eighty days from an armchair"},
      {"name": "Global (India, Hong Kong, Japan, America, Atlantic — the Victorian imperial circuit)", "role": "The route of Fogg's circumnavigation — through the Suez Canal to India, across Southeast Asia, the Pacific, North America, and the Atlantic — maps the Victorian steamship and railway network of the British Empire and its global reach"}
    ],
    "subjects": ["French Literature", "Modern Era", "Jules Verne", "Adventure Novel", "Victorian Literature", "Globalisation", "Technology", "19th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Around the World in Eighty Days (Verne, 1872) is one of the founding texts of the adventure novel — reflecting the Victorian technological globalisation of the 1870s (Suez Canal, transcontinental railroad) and inspiring Nellie Bly's real-world 72-day circumnavigation (1889). One of Verne's most widely translated and adapted works, it contributed to the genre of the 'race against time' adventure narrative and made Phileas Fogg one of the most recognisable characters in world popular culture.",
      "significanceCategory": "highly-significant"
    }
  }
},

"chai-symbol": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784chai-symbol.json",
  "slug": "chai-symbol",
  "data": {
    "summary": "Chai (Hebrew: חַי, 'life' or 'living') is a Jewish symbol composed of the Hebrew letters Chet (ח) and Yod (י) — whose numerical values (gematria) are 8 and 10 respectively, summing to 18, the traditional Jewish lucky number — used as an amulet, decorative motif, and symbol of Jewish identity and the affirmation of life in Jewish culture. The word chai means 'living' in Hebrew (a form of the root ch-y-h, חיה, 'to live'), and appears in one of the most famous biblical affirmations of life: 'I shall not die, but live (chai), and declare the works of the LORD' (Psalm 118:17). The phrase le'chaim ('לחיים, 'to life!') — the ubiquitous Jewish toast — derives from the same root and encapsulates the same affirmation of life as the chai symbol.\n\nThe chai symbol is one of the most widely used symbols in contemporary Jewish culture and Jewish identity — it appears on jewellery (gold and silver chai pendants), clothing, art, and decorative objects, and is particularly associated with Ashkenazi Jewish culture (where the tradition of giving gifts in multiples of 18 in honour of the chai gematria is common). The symbol's use as an amulet and protective charm draws on the kabbalistic tradition of gematria (the use of the numerical values of Hebrew letters to find hidden meanings and connections in sacred texts) and the broader Jewish tradition of protective symbols and amulets (hamsa, mezuzah).\n\nThe chai symbol's widespread contemporary use reflects the phenomenon of Jewish cultural symbols serving as markers of ethnic and cultural identity in the Jewish diaspora — alongside the Star of David, the menorah, and the hamsa, the chai symbol has become one of the primary visual markers of Jewish identity in secular contexts, worn and displayed by Jews of all levels of religious observance as an expression of cultural and ethnic solidarity rather than specifically religious devotion.",
    "causes": [
      "The Hebrew language's tradition of gematria — the assignment of numerical values to Hebrew letters and the use of these values to find hidden meanings and connections — gave the word chai (numerical value 18) its special significance: the number 18 became the 'lucky number' of Jewish tradition, and the chai symbol its visual expression.",
      "The Jewish theological and cultural emphasis on the value and sanctity of life — expressed in the principle of pikuach nefesh (the preservation of life overrides almost all other commandments) and in the le'chaim toast tradition — provided the symbolic significance of the chai symbol: it is an affirmation of the Jewish commitment to life and living.",
      "The development of Jewish identity markers in the diaspora — the need for symbols that could express Jewish cultural and ethnic identity in non-Hebrew-speaking contexts — drove the proliferation of chai symbols in jewellery, clothing, and art in 20th-century Ashkenazi diaspora culture."
    ],
    "effects": [
      "The chai symbol's adoption as a universal Jewish identity marker — alongside the Star of David and menorah — has made it one of the most widely recognised symbols of Jewish cultural identity in the world, worn by Jews of all levels of religious observance as an expression of cultural and ethnic solidarity.",
      "The tradition of giving gifts in multiples of 18 (chai) — particularly for bar and bat mitzvahs, weddings, and charitable donations — is one of the most distinctive practices of Ashkenazi Jewish culture, reflecting the chai gematria's integration into the social and economic practices of Jewish life.",
      "The chai symbol's integration into the broader system of Jewish protective amulets and identity symbols — alongside the hamsa, mezuzah, and Evil Eye amulet — represents the layering of kabbalistic, biblical, and folk traditions into the visual culture of Jewish identity."
    ],
    "relationships": [
      {"sourceSlug": "chai-symbol", "sourceName": "Chai symbol (Hebrew letters, gematria 18)", "verb": "DERIVES_FROM", "targetSlug": "hebrew-language", "targetName": "Hebrew language and gematria tradition", "context": "The chai symbol derives from the Hebrew letters Chet (ח) and Yod (י) — whose gematria values sum to 18, the Jewish lucky number — embedded in the kabbalistic tradition of gematria."},
      {"sourceSlug": "chai-symbol", "sourceName": "Chai symbol (Jewish identity marker)", "verb": "SYMBOL_OF", "targetSlug": "jewish-diaspora-culture", "targetName": "Jewish diaspora culture and identity", "context": "The chai symbol is one of the primary visual markers of Jewish cultural identity in the diaspora — worn by Jews of all religious observance levels as an expression of ethnic and cultural solidarity."},
      {"sourceSlug": "chai-symbol", "sourceName": "Chai (le'chaim, affirmation of life)", "verb": "EXPRESSES", "targetSlug": "jewish-philosophy-of-life", "targetName": "Jewish theological emphasis on life (pikuach nefesh)", "context": "The chai symbol encapsulates the Jewish theological and cultural emphasis on the sanctity of life — expressed in the le'chaim toast, the principle of pikuach nefesh, and the biblical 'I shall not die, but live' (Psalm 118:17)."}
    ],
    "places": [
      {"name": "Jewish diaspora worldwide (Ashkenazi, Sephardi, Mizrahi communities)", "role": "The chai symbol is used across the Jewish diaspora — particularly in Ashkenazi communities where the tradition of gifts in multiples of 18 is strongest — as a marker of Jewish cultural identity in secular and religious contexts"},
      {"name": "Israel (Hebrew cultural context, le'chaim toast)", "role": "In Israel, chai retains its Hebrew linguistic context — le'chaim is the universal Israeli toast — while the symbol serves as both a religious affirmation and a cultural identity marker"}
    ],
    "subjects": ["Jewish Culture", "Ancient Era", "Hebrew Language", "Jewish Identity", "Symbolism", "Kabbalah", "Gematria", "Diaspora Culture"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The chai symbol (Hebrew letters for 'life', gematria value 18) is one of the most widely used symbols of Jewish cultural identity in the diaspora — alongside the Star of David and menorah. Its integration of gematria, the Jewish affirmation of life (le'chaim), and the kabbalistic amulet tradition makes it a complex cultural symbol reflecting centuries of Jewish religious and diaspora practice. The tradition of gifts in multiples of 18 (chai) is one of the most distinctive practices of Ashkenazi Jewish culture.",
      "significanceCategory": "significant"
    }
  }
},

"natural-approach": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785natural-approach.json",
  "slug": "natural-approach",
  "data": {
    "summary": "The Natural Approach is a language teaching methodology developed by Tracy D. Terrell and Stephen D. Krashen, first described in Terrell's 1977 paper 'A Natural Approach to Second Language Acquisition and Learning' (Modern Language Journal) and developed into a comprehensive methodology in their joint book The Natural Approach: Language Acquisition in the Classroom (1983). The Natural Approach is grounded in Krashen's Input Hypothesis — his theoretical claim that language acquisition occurs when learners are exposed to 'comprehensible input' (language slightly beyond their current level of competence, i+1 in Krashen's notation) in a low-anxiety environment, and that explicit grammar instruction plays a secondary role to exposure to meaningful, comprehensible communication. The method emphasises listening comprehension and early communication in the target language before production, silent period tolerance (allowing learners to remain silent during early stages), affective filter reduction (reducing anxiety and stress), and the use of realia and context to make language meaningful.\n\nThe Natural Approach is closely related to, and in many respects a classroom implementation of, Stephen Krashen's Monitor Model — a set of five hypotheses about second language acquisition: the Acquisition-Learning hypothesis (distinguishing unconscious acquisition from conscious learning), the Monitor Hypothesis (conscious learning serves only as a monitor/editor of output), the Input Hypothesis (acquisition requires comprehensible input), the Affective Filter Hypothesis (emotional factors affect acquisition rate), and the Natural Order Hypothesis (grammatical structures are acquired in a predictable order). The Natural Approach translates these theoretical claims into pedagogical practice: the classroom is designed to maximise comprehensible input, reduce anxiety, and allow natural acquisition rather than explicit grammar learning.\n\nThe Natural Approach and Krashen's Monitor Model were enormously influential in applied linguistics and language teaching in the 1980s–1990s, shifting the dominant paradigm from grammar-translation and audiolingual methods toward communicative and acquisition-focused approaches. While Krashen's theoretical claims (particularly the strict acquisition/learning distinction) have been extensively criticized by researchers (VanPatten, Swain, Long), the Natural Approach's emphasis on communicative input and affective factors contributed to the broader communicative language teaching (CLT) movement that now dominates second language pedagogy.",
    "causes": [
      "Krashen's theoretical synthesis of second language acquisition research — his Monitor Model's five hypotheses — provided the theoretical foundation for the Natural Approach: Terrell and Krashen's methodology is an attempt to translate Krashen's acquisition theory into classroom practice, making it a rare example of an applied linguistics methodology closely tied to a specific theoretical framework.",
      "The dissatisfaction with grammar-translation and audiolingual methodologies — whose emphasis on explicit grammar rules and pattern drilling had come under increasing criticism from both theoretical linguists (Chomsky's critique of behaviorist SLA theory) and classroom practitioners — created the demand for alternative approaches that the Natural Approach aimed to satisfy.",
      "Tracy Terrell's experience as a Spanish language teacher and Krashen's cognitive science background — their collaboration bridging applied pedagogy and theoretical linguistics — produced the Natural Approach as a classroom methodology grounded in acquisition theory rather than grammar instruction."
    ],
    "effects": [
      "The Natural Approach and Krashen's Monitor Model shifted the dominant paradigm in second language teaching in the 1980s — contributing to the rise of communicative language teaching (CLT), task-based language teaching, and content-based instruction, which replaced grammar-translation and audiolingual methods as the mainstream pedagogical approaches in ESL/EFL and foreign language education.",
      "Krashen's comprehensible input hypothesis — and the related concept of the affective filter — became foundational concepts in applied linguistics education programmes worldwide, introducing generations of language teachers to theories of acquisition, input, and affective factors regardless of their specific adoption of the Natural Approach.",
      "The extensive research generated in response to Krashen's Monitor Model — both supporting and criticising the acquisition/learning distinction, the Input Hypothesis, and the Affective Filter — was one of the most productive research programmes in applied linguistics history, driving the field's theoretical and empirical development through the 1980s and 1990s."
    ],
    "relationships": [
      {"sourceSlug": "natural-approach", "sourceName": "Natural Approach (Krashen and Terrell, 1977/1983)", "verb": "DEVELOPED_BY", "targetSlug": "stephen-krashen", "targetName": "Stephen Krashen (Input Hypothesis, Monitor Model)", "context": "Krashen's Monitor Model — particularly the Input Hypothesis and Affective Filter Hypothesis — provided the theoretical foundation for the Natural Approach, which Terrell and Krashen developed as a classroom implementation of Krashen's acquisition theory."},
      {"sourceSlug": "natural-approach", "sourceName": "Natural Approach (communicative, acquisition-focused)", "verb": "CONTRIBUTES_TO", "targetSlug": "communicative-language-teaching", "targetName": "Communicative language teaching (CLT) movement", "context": "The Natural Approach contributed to the broader communicative language teaching movement — shifting the dominant second language pedagogy from grammar-translation and audiolingual methods toward communicative, input-focused approaches."},
      {"sourceSlug": "natural-approach", "sourceName": "Natural Approach (comprehensible input, Monitor Model)", "verb": "GENERATES", "targetSlug": "second-language-acquisition-research", "targetName": "Second language acquisition research (VanPatten, Swain, Long)", "context": "Krashen's Monitor Model — closely tied to the Natural Approach — generated one of the most productive research programmes in applied linguistics history, driving theoretical and empirical development through the extensive debate over the acquisition/learning distinction."}
    ],
    "places": [
      {"name": "University of Southern California (Krashen's academic base)", "role": "Stephen Krashen developed the Monitor Model and collaborated with Terrell at USC — the institutional context for the theoretical and pedagogical development of the Natural Approach"},
      {"name": "Global (ESL/EFL classrooms, second language education worldwide)", "role": "The Natural Approach and Krashen's Input Hypothesis influenced second language teaching globally — shifting pedagogy from grammar-translation to communicative approaches across ESL/EFL and foreign language programmes"}
    ],
    "subjects": ["Applied Linguistics", "Modern Era", "Language Teaching", "Second Language Acquisition", "Stephen Krashen", "Pedagogy", "Input Hypothesis", "Language Education"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Natural Approach (Krashen and Terrell, 1977/1983) is one of the most influential language teaching methodologies of the 20th century — grounded in Krashen's Monitor Model (Input Hypothesis, Affective Filter) and contributing to the shift from grammar-translation to communicative language teaching as the dominant paradigm in second language education. Krashen's comprehensible input hypothesis influenced generations of language teachers worldwide, and the research debate it generated drove applied linguistics development for two decades.",
      "significanceCategory": "significant"
    }
  }
},

"philology": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785philology.json",
  "slug": "philology",
  "data": {
    "summary": "Philology (from Greek φιλολογία, philologia, 'love of words/learning') is the academic discipline concerned with the study of written texts and their linguistic, historical, and literary dimensions — encompassing textual criticism (the reconstruction and authentication of texts), historical linguistics (the study of language change over time), and the interpretation of literary and documentary sources. As an academic discipline, philology developed from the Renaissance humanist tradition of returning to the original languages of ancient texts — the recovery, editing, and interpretation of Greek, Latin, Hebrew, and Arabic manuscripts — and reached its classical form in the German academic tradition of the 19th century (Karl Lachmann, 1793–1851; August Boeckh, 1785–1867; Friedrich Schlegel, 1772–1829; the comparative philology of Rasmus Rask, 1787–1832, and Jacob Grimm, 1785–1863), which created the foundations of both modern historical linguistics and the critical edition traditions.\n\nPhilology as practiced in the 19th century encompassed several overlapping activities: textual criticism (the reconstruction of the most accurate text of a classical or medieval work from multiple manuscripts), comparative linguistics (the study of the genetic relationships between languages through comparative analysis of their vocabulary and grammar), and Altertumswissenschaft ('science of antiquity', August Boeckh's programme of total interpretation of ancient culture through its linguistic and documentary sources). The founding achievement of 19th-century comparative philology was the proof (Rask, Grimm, Bopp) that Sanskrit, Greek, Latin, the Germanic languages, and other languages formed a family of related languages (Indo-European), derived from a common ancestor — a discovery that transformed both linguistics and the historical understanding of ancient peoples and migrations.\n\nPhilology's relationship to modern academic disciplines is complex: it is simultaneously the ancestor of linguistics (which split off as an autonomous discipline in the 20th century), literary studies (which adopted philological methods of textual analysis), and history (which drew on philological methods for source criticism). The term 'philology' is used differently in different national traditions: in Anglo-American usage it often refers specifically to historical and comparative linguistics; in German and continental European usage it more often refers to the combined study of language and literature of a particular cultural tradition.",
    "causes": [
      "The Renaissance humanist programme of returning to the original languages of ancient texts — Lorenzo Valla's (1407–1457) demonstration that the Donation of Constantine was a medieval forgery through linguistic anachronism, Erasmus's Greek New Testament (1516) establishing the original Greek text over the Vulgate Latin — created the foundational methods of philological criticism: close attention to linguistic evidence as a tool for dating and authenticating texts.",
      "The 19th-century German university tradition — the Humboldtian model of research-oriented universities, the seminar system, and the ideal of Wissenschaft (systematic, rigorous knowledge) — provided the institutional framework for the development of classical and comparative philology as autonomous academic disciplines.",
      "The discovery of Sanskrit by European scholars and its comparison with Greek and Latin (Sir William Jones's 1786 lecture on the Indo-European language family) provided the founding problem of 19th-century comparative philology: the reconstruction of the hypothetical common ancestor (Proto-Indo-European) and the systematic comparison of its descendant languages through the sound laws of comparative linguistics."
    ],
    "effects": [
      "The discovery of the Indo-European language family — the proof that Sanskrit, Greek, Latin, Gothic, Old Persian, and other languages all descended from a common ancestor — was one of the most important intellectual achievements of the 19th century, transforming the historical understanding of ancient peoples, migrations, and cultural relations across Eurasia.",
      "Philology's textual criticism tradition — the Lachmann method of reconstructing the best text of a classical or medieval work from the evidence of surviving manuscripts — established the critical edition as the primary vehicle of classical scholarship, providing the textual foundations on which modern classical studies, medieval studies, and biblical studies rest.",
      "Philology's role as the ancestor of modern linguistics (historical linguistics, comparative linguistics, morphology, phonology) and of modern literary studies (close reading, textual analysis, historical criticism) makes it the foundational academic discipline of the modern humanities — despite the disciplinary splits that have largely replaced 'philology' as a unified label."
    ],
    "relationships": [
      {"sourceSlug": "philology", "sourceName": "Philology (textual criticism, historical linguistics)", "verb": "PRODUCES", "targetSlug": "indo-european-linguistics", "targetName": "Indo-European linguistics (Rask, Grimm, Bopp)", "context": "The comparative philology of Rask, Grimm, and Bopp proved the Indo-European language family and established the comparative method — one of the most important intellectual achievements of the 19th century."},
      {"sourceSlug": "philology", "sourceName": "Philology (Renaissance humanism, Valla, Erasmus)", "verb": "DEVELOPS_FROM", "targetSlug": "renaissance-humanism", "targetName": "Renaissance humanism (return to original sources)", "context": "Philology developed from the Renaissance humanist programme of returning to original languages — Valla's authentication methods and Erasmus's Greek New Testament established the foundational methods of philological criticism."},
      {"sourceSlug": "philology", "sourceName": "Philology (ancestor discipline)", "verb": "PRECEDES", "targetSlug": "modern-linguistics", "targetName": "Modern linguistics (Saussure, Chomsky, structural linguistics)", "context": "Philology is the ancestor discipline of modern linguistics — historical and comparative linguistics split off from the broader philological tradition in the late 19th and early 20th centuries, establishing linguistics as an autonomous science of language."}
    ],
    "places": [
      {"name": "Germany (19th-century classical philology, Berlin and Göttingen universities)", "role": "The German university tradition — Karl Lachmann, August Boeckh, Jacob Grimm — was the centre of 19th-century classical and comparative philology, creating the foundations of modern historical linguistics and textual criticism"},
      {"name": "Oxford, Cambridge, and Paris (classical and medieval philology traditions)", "role": "The British and French philological traditions — editing classical and medieval texts, developing classical scholarship — complemented the German tradition and created the Anglo-French classical studies tradition"}
    ],
    "subjects": ["Humanities", "Ancient Era", "Linguistics", "Textual Criticism", "Academic Discipline", "Historical Linguistics", "Classical Studies", "Methodology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Philology is the foundational academic discipline of the modern humanities — the ancestor of historical linguistics, literary studies, classical scholarship, and textual criticism. Its 19th-century achievements (Indo-European linguistics, the critical edition tradition, the Lachmann method) are foundational for the modern study of languages and literature. The discovery of the Indo-European language family — the primary achievement of 19th-century comparative philology — transformed the historical understanding of ancient peoples and their migrations.",
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
