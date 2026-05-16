#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 44 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-canterbury-tales, the-decameron, masnavi,
          the-consolation-of-philosophy, les-fleurs-du-mal,
          life-is-a-dream, the-city-of-god, liber-pontificalis
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-44-may2026"

ENRICHMENTS = {

"the-canterbury-tales": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-canterbury-tales.json",
  "slug": "the-canterbury-tales",
  "data": {
    "summary": "The Canterbury Tales is a collection of 24 stories in verse and prose by the English poet Geoffrey Chaucer (c. 1343–1400), written primarily in Middle English rhyming couplets (iambic pentameter) and composed in the last decade of Chaucer's life (c. 1387–1400), left unfinished at his death. The frame narrative — modelled on Boccaccio's Decameron — presents a group of 31 pilgrims (including Chaucer himself as a character) travelling from the Tabard Inn in Southwark to the shrine of St Thomas Becket at Canterbury Cathedral, each agreeing to tell four tales (two going, two returning) to pass the time, with the Host Harry Bailey judging the best tale. Only 24 tales are complete and the return journey is never reached, but the collection as it stands is the greatest achievement in Middle English literature and one of the foundational texts of English poetry.\n\nThe Canterbury Tales is distinguished by its extraordinary range — social (pilgrims from every level of 14th-century English society: Knight, Prioress, Miller, Wife of Bath, Pardoner, Merchant, Clerk, Franklin, Cook), generic (chivalric romance, fabliau, sermon, tragedy, saint's life, beast fable, philosophical dialogue), and tonal (courtly, bawdy, pious, satirical, ironic) — and by the sophisticated relationship between the characters' social identities and the tales they tell. The most celebrated tales include the Knight's Tale (chivalric romance derived from Boccaccio's Teseida), the Miller's Tale (bawdy fabliau), the Wife of Bath's Prologue and Tale (feminist proto-autobiography), the Pardoner's Tale (sermon on greed, with embedded tale of three men seeking Death), the Nun's Priest's Tale (beast fable), and the Franklin's Tale (Breton lai).\n\nChaucer's importance for English literature is unequalled before Shakespeare — he established the iambic pentameter line as the primary metre of English verse, shaped the prestige of the East Midlands dialect as the basis for standard literary English, and demonstrated the capacity of vernacular English for all registers of literary expression. His direct use of Boccaccio, Petrarch, and French models also connects English literature to the European humanist tradition.",
    "causes": [
      "Chaucer's extensive reading in Italian literature — his two trips to Italy (1372, 1378) and his direct knowledge of Boccaccio's Decameron and Teseida and Petrarch's Latin translations — provided both the frame narrative model (the Decameron's pilgrimage/storytelling frame) and many of the individual tale sources; without the Italian models, the Canterbury Tales in its form would not exist.",
      "The English pilgrimage tradition and the specific prominence of the Canterbury pilgrimage to St Thomas Becket's shrine — the most popular pilgrim destination in England in the 14th century — provided the social and geographical frame that makes the Canterbury Tales' social panorama possible: the mix of pilgrims from different social levels that would actually have made such a journey together.",
      "The 14th-century English social crisis — the aftermath of the Black Death (1348–1349), the Peasants' Revolt (1381), the anti-clerical Lollard movement, and the instability of Richard II's court — provided the social and political context for the Canterbury Tales' satirical engagement with the institutions of medieval England: Chaucer's portraits of the Pardoner, the Friar, and the Monk reflect specific late 14th-century ecclesiastical corruption."
    ],
    "effects": [
      "Chaucer's Canterbury Tales established the iambic pentameter couplet as the dominant metre of English verse narrative — the 'heroic couplet' that Dryden and Pope would develop into the dominant form of 17th and 18th-century English poetry — and his prestige helped establish the East Midlands dialect as the foundation of standard literary English.",
      "The Canterbury Tales' influence on the English literary tradition is foundational — Spenser, Shakespeare, Milton, Keats, and countless others engaged with Chaucer directly, and the Wife of Bath's Prologue in particular has become a touchstone for the history of women's voices in English literature and proto-feminist criticism.",
      "The Canterbury Tales' model of social panorama — its ambition to represent all levels and types of English society through a collection of voices — became a defining ambition of English fiction: from Shakespeare's history plays through Dickens's novels to the 20th century, the desire to capture the totality of English social experience draws on the Canterbury Tales tradition."
    ],
    "relationships": [
      {"sourceSlug": "geoffrey-chaucer", "sourceName": "Geoffrey Chaucer (c. 1343–1400)", "verb": "AUTHORS", "targetSlug": "the-canterbury-tales", "targetName": "The Canterbury Tales (c. 1387–1400, unfinished, 24 tales)", "context": "Chaucer composed the Canterbury Tales in the last decade of his life (c. 1387–1400) — 24 tales in verse and prose, the greatest achievement in Middle English literature and the foundational text of English poetry."},
      {"sourceSlug": "the-canterbury-tales", "sourceName": "Canterbury Tales (frame narrative model)", "verb": "RESPONDS_TO", "targetSlug": "the-decameron", "targetName": "Boccaccio's Decameron (1353, framed novella collection)", "context": "Chaucer's pilgrimage frame — a group of travellers telling stories — is directly modelled on Boccaccio's Decameron; the Knight's Tale is adapted from Boccaccio's Teseida."},
      {"sourceSlug": "the-canterbury-tales", "sourceName": "Canterbury Tales (Wife of Bath, Pardoner, social panorama)", "verb": "INFLUENCES", "targetSlug": "english-literary-tradition", "targetName": "English literary tradition (Shakespeare, Spenser, Dickens)", "context": "Chaucer's Canterbury Tales established iambic pentameter, shaped literary English, and its social panorama — the ambition to capture all levels of English society — became a defining tradition of English fiction from Shakespeare to Dickens."}
    ],
    "places": [
      {"name": "London to Canterbury, England (pilgrimage route, Tabard Inn Southwark to Canterbury Cathedral)", "role": "The Canterbury pilgrimage route — from the Tabard Inn in Southwark to Thomas Becket's shrine at Canterbury Cathedral — is the literal setting of the Tales and its social panorama"},
      {"name": "Italy (Chaucer's trips 1372, 1378; Boccaccio and Petrarch models)", "role": "Chaucer's two trips to Italy (1372 and 1378) gave him direct knowledge of Boccaccio's Decameron and Petrarch's work — Italian models were decisive for the Canterbury Tales' form and several of its tales"}
    ],
    "subjects": ["English Literature", "Medieval Era", "Geoffrey Chaucer", "Middle English", "Frame Narrative", "Poetry", "Medieval Literature", "English Language"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Canterbury Tales (Chaucer, c. 1387–1400) is the greatest achievement in Middle English literature — it established iambic pentameter as the primary metre of English verse, shaped literary English, and created the model of social panorama that defines the English fictional tradition. Its influence on Shakespeare, Spenser, Dickens, and the entire subsequent English literary tradition makes it one of the foundational texts of English-language culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-decameron": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-decameron.json",
  "slug": "the-decameron",
  "data": {
    "summary": "The Decameron (Italian: Decamerone, 'Ten-Day Work', from Greek δέκα ἡμέρα, deka hēmera) is a collection of 100 novellas by the Italian author Giovanni Boccaccio (1313–1375), written c. 1348–1353 in the vernacular Tuscan Italian. The frame narrative presents ten young Florentines (seven women and three men) who retreat from plague-stricken Florence to a country villa outside the city during the Black Death (1348) and pass ten days (in Italian: dieci giorni — hence Decameron) each telling one story per day, on themes assigned by the day's 'king' or 'queen'. The 100 stories cover the full range of human experience — love (requited, unrequited, adulterous, tragic), fortune (reversals of fate, merchants' adventures), and wit (clever schemes, wordplay, the outwitting of the powerful by the ingenious) — told with a characteristic combination of sympathy, irony, and psychological realism that distinguishes Boccaccio's prose from previous medieval narrative.\n\nThe Decameron is the founding text of European prose fiction — its prose narrative technique, its psychological realism, its ironic perspective on clerical hypocrisy and social convention, and its celebration of human wit and love as positive values created the template for the European novella tradition (Marguerite de Navarre's Heptaméron, the Spanish novella, Shakespeare's plot sources) and, through the novella, for the novel itself. Dante's Comedy had demonstrated the capacity of the Tuscan vernacular for sublime verse; Boccaccio's Decameron demonstrated its capacity for sophisticated prose narrative — together they established the prestige of Tuscan Italian as the literary standard.\n\nThe Decameron's framing device — the Black Death as the condition for storytelling, the stories as a form of sociable distraction from catastrophe — gives the collection a remarkable historical density: the Black Death of 1348 killed perhaps a third of Europe's population, and Boccaccio's introduction, a precise and devastating description of plague-struck Florence, is one of the most important contemporary accounts of the Black Death's social impact.",
    "causes": [
      "The Black Death of 1348 — which killed approximately 60% of Florence's population and devastated European society — provided both the historical setting for the Decameron's frame narrative and the existential urgency that makes the collection's celebration of human wit, love, and sociability so powerful: the stories are told in the face of mass death.",
      "Boccaccio's literary formation — his reading of Ovid, Virgil, Dante, and French romance, and his direct knowledge of the Latin rhetorical tradition — provided the literary toolkit for the Decameron's prose narrative technique, while his experience as a merchant's son (commercial Florence, Naples) provided the social observation and psychological realism that distinguishes the Decameron from previous medieval narrative.",
      "The Italian novella tradition — the short prose narrative of sharp plot, surprise, and psychological acuity — provided the generic framework from which Boccaccio developed the Decameron: earlier Italian novella collections (Novellino) gave him a model he radically transformed through the framing device and the sustained prose style."
    ],
    "effects": [
      "The Decameron established the novella as the dominant short prose narrative form in European literature — Marguerite de Navarre's Heptaméron, the Spanish novella tradition (Cervantes's Novelas ejemplares), the English jest-book tradition, and Shakespeare's comedy plots (All's Well, Much Ado, Measure for Measure, Cymbeline all draw on Decameron stories) all trace directly to Boccaccio's model.",
      "Boccaccio's Decameron and its critical promotion of Dante's Divine Comedy (Boccaccio was the first to call it 'Divina') together established the Tuscan vernacular as the prestige literary Italian — the model for subsequent Italian prose that Bembo systematised in Prose della volgar lingua (1525) and that became the foundation of the Italian literary standard.",
      "The Decameron's framing of storytelling as a social response to catastrophe — the stories as a humane distraction and affirmation of life against death — became a model for subsequent writers in times of crisis: Chaucer's Canterbury Tales (plague aftermath), Marguerite de Navarre's Heptaméron (written during her illness), and numerous later works in crisis contexts draw on the Decameron's fundamental model."
    ],
    "relationships": [
      {"sourceSlug": "giovanni-boccaccio", "sourceName": "Giovanni Boccaccio (1313–1375)", "verb": "AUTHORS", "targetSlug": "the-decameron", "targetName": "The Decameron (c. 1348–1353, 100 novellas)", "context": "Boccaccio wrote the Decameron c. 1348–1353 — 100 novellas framed by ten Florentines fleeing the Black Death, the founding text of European prose fiction."},
      {"sourceSlug": "the-decameron", "sourceName": "Decameron (novella model, plot sources)", "verb": "INFLUENCES", "targetSlug": "the-canterbury-tales", "targetName": "Chaucer's Canterbury Tales (c. 1387–1400)", "context": "Chaucer modelled his pilgrimage frame on the Decameron's storytelling frame; the Knight's Tale is adapted from Boccaccio's Teseida; the Decameron is the primary Italian model for the Canterbury Tales."},
      {"sourceSlug": "the-decameron", "sourceName": "Decameron (novella plots, Shakespeare's comedies)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "shakespeare-comedies", "targetName": "Shakespeare's comedies and romances (plot sources)", "context": "Several of Shakespeare's comedies and romances draw directly on Decameron stories for their plots: All's Well That Ends Well (Day 3 Story 9), Much Ado About Nothing (Day 2 Story 9), Cymbeline (Day 2 Story 9), and others."}
    ],
    "places": [
      {"name": "Florence (plague-struck 1348, frame narrative setting; Boccaccio's home)", "role": "Florence during the Black Death of 1348 is both the literal frame setting (the ten young Florentines fleeing plague) and the social world depicted throughout the Decameron's stories"},
      {"name": "Naples (Boccaccio's early formation, 1327–1340)", "role": "Boccaccio spent his formative years in Naples at the Angevin court — his Neapolitan experience provided the social observation and psychological realism that distinguishes the Decameron from previous Italian narrative"}
    ],
    "subjects": ["Italian Literature", "Medieval Era", "Giovanni Boccaccio", "Prose Fiction", "Novella", "Black Death", "Frame Narrative", "European Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Decameron (Boccaccio, c. 1348–1353) is the founding text of European prose fiction — it established the novella as a literary form, influenced Chaucer's Canterbury Tales and Shakespeare's comedies, and (alongside Dante's Comedy) established the prestige of Tuscan Italian as the literary standard. Its Black Death frame narrative is also one of the most important contemporary accounts of the plague's social impact.",
      "significanceCategory": "world-changing"
    }
  }
},

"masnavi": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780masnavi.json",
  "slug": "masnavi",
  "data": {
    "summary": "The Masnavi (Persian: مثنوی معنوی, Maṡnavī-ye Maʿnavī, 'Spiritual Couplets') is a six-volume poem in rhyming couplets (masnavi metre) by the Persian Sufi poet and mystic Jalāl al-Dīn Muḥammad Rūmī (1207–1273), composed in Konya (in present-day Turkey) c. 1258–1273 at the instigation of his disciple Husam al-Din Chalabi. Running to approximately 25,000 couplets (51,000 lines) and one of the longest poems in any language, the Masnavi is the summit of Persian Sufi poetry and the work that earned Rumi the title 'Mawlana' (Our Master). It is sometimes called 'the Quran of the Persian language' — a reflection of its central position in Persian literary and spiritual culture.\n\nThe Masnavi's structure is associative rather than linear — it moves through stories, parables, Quranic commentary, philosophical discussions, and lyrical passages in a manner that enacts the Sufi understanding of spiritual reality as a web of interconnected meanings rather than a sequential argument. Its opening verses — the 'reed flute' (ney) passage — are among the most famous in all of Persian literature: the image of the reed flute's music as the cry of separation from its origin (the reed bed) as an allegory of the soul's longing for union with the divine is one of the defining metaphors of Sufi thought. The Masnavi contains dozens of embedded stories — many drawn from the Quran, Hadith, Persian folk tradition, and Hindu narratives — that are used as vehicles for Sufi teaching: the story of the reed flute, the elephant in the dark room (a parable for the divine beyond human comprehension), the three fishermen, the lion who hunts alone (on free will and divine help), and hundreds of others.\n\nRumi's Masnavi has been translated into dozens of languages and is among the best-selling poetry collections in the United States in the late 20th and early 21st centuries (in the translations of Coleman Barks, which, though free paraphrases, introduced millions of English-speaking readers to Sufi mystical poetry). It remains a foundational text of Persian literary culture and of the Sufi tradition worldwide.",
    "causes": [
      "Rumi's relationship with the wandering dervish Shams-i-Tabrizi — the mystical friendship (beginning c. 1244) that transformed Rumi from a conventional scholar and jurist into an ecstatic poet — was the biographical foundation of Rumi's poetry; the trauma of Shams's disappearance and probable murder drove the extraordinary creative outpouring of the Masnavi and the Diwan-e Shams.",
      "Husam al-Din Chalabi's role as the catalyst and collaborator of the Masnavi — his suggestion that Rumi compose a long Sufi poem in the masnavi metre (like Sanai's Hadiqat al-Haqiqa and Attar's Mantiq al-Tayr) and his sustained encouragement, recording, and organisation of the poem over fifteen years — was the direct occasion for the Masnavi's composition.",
      "The Persian Sufi literary tradition — the earlier masnavi poetry of Sanai (Hadiqat al-Haqiqa, c. 1130) and Attar (Mantiq al-Tayr, c. 1177) — provided both the generic model (the long Sufi poem in rhyming couplets) and the thematic framework (the soul's journey toward union with the divine) that Rumi transformed and expanded in the Masnavi."
    ],
    "effects": [
      "The Masnavi became the central text of the Mevlevi Sufi order — the order founded by Rumi's son Sultan Walad after Rumi's death, whose characteristic practice (the sama, the whirling ceremony of the dervishes) became one of the most recognised Sufi practices worldwide — and has been studied and commented upon continuously in the Persian-language world for seven centuries.",
      "Rumi's emergence as the best-selling poet in the United States in the late 20th century — through Coleman Barks's free paraphrases (The Essential Rumi, 1995) — demonstrated the global appeal of Sufi mystical poetry and introduced millions of English-speaking readers to Persian literary and spiritual culture, making Rumi the most-read poet in America.",
      "The Masnavi's influence on Persian literary culture — its standing as 'the Quran of the Persian language', its central place in the curriculum of traditional Persian education, and its status as the summit of the masnavi genre — has been continuous and foundational for seven centuries, shaping Persian poetry, philosophy, and spiritual culture."
    ],
    "relationships": [
      {"sourceSlug": "rumi", "sourceName": "Jalāl al-Dīn Rūmī (1207–1273, Persian Sufi poet)", "verb": "AUTHORS", "targetSlug": "masnavi", "targetName": "Masnavi-ye Maʿnavī (c. 1258–1273, ~25,000 couplets)", "context": "Rumi composed the Masnavi c. 1258–1273 in Konya — approximately 25,000 couplets of Sufi mystical poetry, the summit of Persian Sufi poetry and the central text of the Mevlevi order."},
      {"sourceSlug": "masnavi", "sourceName": "Masnavi (Sufi mysticism, reed flute metaphor, divine union)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "mevlevi-sufi-order", "targetName": "Mevlevi Sufi order (Whirling Dervishes, Konya)", "context": "The Masnavi is the central sacred text of the Mevlevi Sufi order — founded by Rumi's son Sultan Walad, known for the sama (whirling ceremony) — and has been studied and commented upon in the Mevlevi tradition continuously for seven centuries."},
      {"sourceSlug": "masnavi", "sourceName": "Masnavi (Coleman Barks, best-selling US poetry)", "verb": "TRANSMITTED_AS", "targetSlug": "rumi-english-paraphrases", "targetName": "Coleman Barks's Rumi translations (The Essential Rumi, 1995)", "context": "Coleman Barks's free English paraphrases (The Essential Rumi, 1995) made Rumi the best-selling poet in the United States — introducing millions to Sufi mystical poetry, though through paraphrases rather than scholarly translations."}
    ],
    "places": [
      {"name": "Konya, Anatolia (present-day Turkey — Rumi's home, Masnavi's composition, Mevlevi shrine)", "role": "Rumi lived in Konya from 1228 until his death (1273) — the Masnavi was composed there, and Konya is the site of Rumi's tomb (Mevlâna Museum), a major pilgrimage destination"},
      {"name": "Persian literary world (Central Asia, Iran, Anatolia, India)", "role": "The Masnavi was composed in Persian — the literary language of the Islamic world from Central Asia to Anatolia and India — and its influence has been continuous across the entire Persian-language literary world for seven centuries"}
    ],
    "subjects": ["Persian Literature", "Medieval Era", "Rumi", "Sufi Poetry", "Islamic Mysticism", "Persian Culture", "Epic Poetry", "Mystical Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Masnavi (Rumi, c. 1258–1273) is the summit of Persian Sufi poetry — approximately 25,000 couplets of mystical verse that earned Rumi the title 'the Quran of the Persian language'. It is the central text of the Mevlevi Sufi order and has been studied continuously for seven centuries across the Persian-language world. In the late 20th century, Rumi became the best-selling poet in the United States through free English paraphrases, demonstrating the global reach of Sufi mystical poetry.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-consolation-of-philosophy": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-consolation-of-philosophy.json",
  "slug": "the-consolation-of-philosophy",
  "data": {
    "summary": "The Consolation of Philosophy (Latin: De Consolatione Philosophiae) is a philosophical dialogue in prose and verse by the Roman statesman and philosopher Anicius Manlius Severinus Boethius (c. 480–524 CE), composed in prison while awaiting execution on charges of treason under the Ostrogothic King Theoderic. Written in the Menippean satire tradition (alternating prose and verse — 39 metrical poems interspersed with prose dialogue), it imagines the allegorical figure of Lady Philosophy visiting Boethius in his cell, consoling him for his fall from fortune and leading him through a philosophical dialogue on the nature of true happiness, the instability of fortune, divine providence, and the reconciliation of free will with God's foreknowledge. The work draws on Platonic, Neoplatonic, Stoic, and Aristotelian traditions.\n\nThe Consolation of Philosophy was the most widely read philosophical text in medieval Europe after the Bible — translated into Old English by King Alfred the Great (c. 888 CE), into Middle English by Chaucer (c. 1380), into French by Jean de Meun (c. 1300), and commented upon by virtually every major medieval philosopher (Remigius of Auxerre, William of Conches, Thomas Aquinas). Its central concept — the Wheel of Fortune (the goddess Fortuna constantly turning her wheel, raising some and lowering others) — became the defining medieval metaphor for the instability of worldly prosperity and one of the most enduring images in Western culture. Its argument for the reconciliation of divine foreknowledge with human free will was central to medieval theological debate.\n\nThe Consolation's remarkable literary achievement — the equanimity and philosophical depth of a man composing a philosophical masterpiece while awaiting execution — has given it a special place in the literature of adversity: Boethius's figure is invoked in discussions of how to face death and reversal, and the Consolation has remained in print virtually continuously for 1,500 years.",
    "causes": [
      "Boethius's arrest and imprisonment (523 CE) by King Theoderic — on charges of treason and consorting with the Eastern Emperor Justin I, charges that Boethius denied — created the specific biographical conditions for the Consolation's composition: the work was written in the crisis of Boethius's fall from the height of power (he was magister officiorum, the top administrative office in the Ostrogothic kingdom) to imprisonment and imminent execution.",
      "Boethius's philosophical formation in the Platonic, Aristotelian, and Stoic traditions — his lifelong project of translating Aristotle's logical works into Latin and writing commentaries on Porphyry and Cicero — provided the intellectual resources for the Consolation's synthesis: the work is the summation of Boethius's philosophical learning applied to his personal crisis.",
      "The Menippean satire tradition (alternating prose and verse, as in Varro, Martianus Capella, and Seneca) provided the literary form for the Consolation — the alternation of philosophical prose with lyrical verse, and the use of an allegorical interlocutor (Lady Philosophy), draws on a well-established late antique literary model."
    ],
    "effects": [
      "The Consolation of Philosophy became the most widely read philosophical text in medieval Europe — more widely read, copied, and commented upon than any other philosophical work except Aristotle — shaping the understanding of fortune, providence, free will, and happiness across the entire medieval period.",
      "The Wheel of Fortune (Rota Fortunae) — Boethius's allegorical figure of the goddess Fortuna turning a wheel on which men rise and fall — became the defining medieval metaphor for the instability of worldly prosperity, depicted in thousands of medieval manuscripts, cathedrals (the west rose windows of several cathedrals represent the Wheel of Fortune), and literary works.",
      "Boethius's influence on medieval philosophy — through the Consolation and through his translations of Aristotle's logical works (which were the primary texts of medieval logic) — was so pervasive that he has been called 'the last Roman and the first Scholastic': he transmitted classical learning to medieval Europe and shaped the framework within which medieval philosophy operated."
    ],
    "relationships": [
      {"sourceSlug": "boethius", "sourceName": "Boethius (c. 480–524 CE, Roman philosopher, prisoner)", "verb": "AUTHORS", "targetSlug": "the-consolation-of-philosophy", "targetName": "Consolation of Philosophy (De Consolatione, c. 523–524 CE)", "context": "Boethius composed the Consolation while awaiting execution in prison (c. 523–524 CE) — the most widely read philosophical text in medieval Europe after the Bible."},
      {"sourceSlug": "the-consolation-of-philosophy", "sourceName": "Consolation (Wheel of Fortune, medieval metaphor)", "verb": "ESTABLISHES", "targetSlug": "wheel-of-fortune-concept", "targetName": "Wheel of Fortune (Rota Fortunae, medieval cultural concept)", "context": "Boethius's Wheel of Fortune became the defining medieval metaphor for the instability of worldly prosperity — depicted in manuscripts, cathedral windows, and literary works across the entire medieval period."},
      {"sourceSlug": "the-consolation-of-philosophy", "sourceName": "Consolation (Alfred, Chaucer translations)", "verb": "TRANSLATED_BY", "targetSlug": "alfred-the-great", "targetName": "Alfred the Great (translated Consolation into Old English c. 888 CE)", "context": "King Alfred the Great translated the Consolation into Old English c. 888 CE — one of five texts Alfred chose for his educational programme, demonstrating the Consolation's centrality to early medieval intellectual culture."}
    ],
    "places": [
      {"name": "Pavia (Boethius's imprisonment and execution, c. 523–524 CE)", "role": "Boethius was imprisoned and executed at Pavia — the Consolation was composed in his cell, and Boethius's tomb is in the church of San Pietro in Ciel d'Oro in Pavia"},
      {"name": "Medieval Europe (translation into Old English, French, Middle English; commentary tradition)", "role": "The Consolation was translated into Old English by Alfred (c. 888), French by Jean de Meun (c. 1300), and Middle English by Chaucer (c. 1380) — its diffusion across medieval Europe demonstrates its extraordinary importance as a philosophical text"}
    ],
    "subjects": ["Latin Philosophy", "Late Antique Era", "Boethius", "Medieval Philosophy", "Stoicism", "Neoplatonism", "Fortune", "Prison Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Consolation of Philosophy (Boethius, c. 523–524 CE) is the most widely read philosophical text in medieval Europe after the Bible — composed while its author awaited execution. Its Wheel of Fortune became the defining medieval metaphor for the instability of worldly prosperity; its argument on free will and divine providence shaped medieval theology; and its translations (Alfred, Chaucer, Jean de Meun) demonstrate its centrality to European intellectual culture for a millennium.",
      "significanceCategory": "world-changing"
    }
  }
},

"les-fleurs-du-mal": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780les-fleurs-du-mal.json",
  "slug": "les-fleurs-du-mal",
  "data": {
    "summary": "Les Fleurs du mal ('The Flowers of Evil') is a collection of poems by the French poet Charles Baudelaire (1821–1867), first published in Paris on 25 June 1857 by the publisher Poulet-Malassis, immediately condemned as obscene by a French court (Baudelaire, his publisher, and his printer were convicted; six poems were ordered suppressed; the conviction was overturned only in 1949), and recognised in the 20th century as the most important collection of French poetry of the 19th century and a founding document of literary Modernism. The first edition contained 100 poems; the second edition (1861, after the suppression of six poems) contained 126 poems; a posthumous third edition (1868) added 25 more, for a total of 151.\n\nLes Fleurs du mal is organised into six sections: 'Spleen et Idéal' (the largest, containing the great lyric poems of beauty, melancholy, and the tension between spiritual aspiration and sensual experience), 'Tableaux Parisiens' (urban poems of Paris, the anonymous modern city), 'Le Vin', 'Fleurs du Mal', 'Révolte', and 'La Mort' (death as the final escape). The collection's central subject is the tension between spleen (ennui, acedia, spiritual deadness) and idéal (spiritual aspiration, beauty, transcendence) — a tension that Baudelaire finds in the most repulsive subjects (decay, prostitution, the city's underworld, death) as well as the most beautiful. The famous opening poem, 'Au Lecteur' ('To the Reader'), addresses the reader directly as a fellow sinner: 'Hypocrite lecteur, — mon semblable, — mon frère!' ('Hypocrite reader — my likeness — my brother!')\n\nBaudelaire's innovations — the concept of 'correspondances' (synesthetic connections between senses, the idea that perfumes, colours, and sounds correspond to one another and to spiritual states), the idea of the poet as an alienated figure ('spleen'), the urban flaneur, the erotic poem as a form of spiritual investigation — inaugurated the Symbolist movement (Verlaine, Rimbaud, Mallarmé) and, through Symbolism, Modernism. T. S. Eliot directly quoted 'Au Lecteur' in The Waste Land (1922).",
    "causes": [
      "Baudelaire's personal biography — his dandyism and deliberate cultivation of transgression, his complex relationship with his mother and stepfather General Aupick, his syphilis (contracted in his early twenties), his financial recklessness, and his sustained engagement with hashish and opium (documented in Les Paradis artificiels) — provided the experiential raw material for the collection's themes of vice, degradation, and spiritual aspiration.",
      "The 1857 obscenity trial and the suppression of six poems — including 'Lesbos', 'Femmes damnées', and 'Les Bijoux' — gave the collection an immediate notoriety that, paradoxically, contributed to its subsequent influence: the poems were known to the Symbolist poets (Verlaine, Rimbaud) precisely because they had been prosecuted.",
      "Baudelaire's engagement with Edgar Allan Poe — he spent seventeen years translating Poe's prose into French, and his theory of poetry as a deliberate creation of beauty and intensity (the 'poème en prose', the 'poetic effect' as distinct from moral instruction) draws directly on Poe's 'Philosophy of Composition' — provided the theoretical framework for the collection's conception of poetry."
    ],
    "effects": [
      "Les Fleurs du mal directly inaugurated the Symbolist movement — Verlaine's 'Poèmes saturniens' (1866) and 'Fêtes galantes' (1869), Rimbaud's 'vowel sonnet' ('Correspondances'), and Mallarmé's dense symbolic poetry all draw directly on Baudelaire's innovations — creating the movement that transformed European poetry in the late 19th century.",
      "Baudelaire's urban poetry — the 'Tableaux Parisiens' section's anonymous, alienated depiction of modern Paris — created the foundational model for literary Modernism's engagement with the modern city: Walter Benjamin's Arcades Project is essentially a philosophical commentary on Baudelaire's urban poetry, and T. S. Eliot's unreal city in The Waste Land draws directly on Baudelaire's Paris.",
      "The 'Baudelairean' sensibility — spleen, ennui, the dandy's cultivated transgression, the erotic as spiritual, the aestheticisation of vice and suffering — became a defining strand of fin-de-siècle culture (Huysmans's À rebours, Wilde's Picture of Dorian Gray, Decadentism, and Aestheticism all draw on Baudelaire)."
    ],
    "relationships": [
      {"sourceSlug": "charles-baudelaire", "sourceName": "Charles Baudelaire (1821–1867, French poet)", "verb": "AUTHORS", "targetSlug": "les-fleurs-du-mal", "targetName": "Les Fleurs du mal (Paris, 25 June 1857)", "context": "Baudelaire published Les Fleurs du mal on 25 June 1857 — immediately prosecuted for obscenity, six poems suppressed, but recognised in the 20th century as the most important French poetry collection of the 19th century."},
      {"sourceSlug": "les-fleurs-du-mal", "sourceName": "Les Fleurs du mal (correspondances, Symbolism)", "verb": "INAUGURATES", "targetSlug": "symbolism-literary-movement", "targetName": "Symbolist literary movement (Verlaine, Rimbaud, Mallarmé)", "context": "Les Fleurs du mal directly inaugurated French Symbolism — Verlaine, Rimbaud, and Mallarmé all drew on Baudelaire's 'correspondances', his spleen/idéal tension, and his concept of the poem as deliberate beauty-creation."},
      {"sourceSlug": "les-fleurs-du-mal", "sourceName": "Les Fleurs du mal (urban alienation, Modernist city)", "verb": "INFLUENCES", "targetSlug": "literary-modernism", "targetName": "Literary Modernism (T. S. Eliot, The Waste Land, Walter Benjamin)", "context": "T. S. Eliot directly quoted Baudelaire's 'Au Lecteur' in The Waste Land; Walter Benjamin's Arcades Project is a philosophical commentary on Baudelaire's urban poetry — making Les Fleurs du mal a foundational text of literary Modernism."}
    ],
    "places": [
      {"name": "Paris (Baudelaire's city, Tableaux Parisiens, 19th-century modernity)", "role": "Paris — the great modern city being transformed by Haussmann's boulevards — is the central urban subject of Les Fleurs du mal's Tableaux Parisiens section and Baudelaire's primary imaginative space"},
      {"name": "France (1857 obscenity trial; 1949 conviction overturned)", "role": "France prosecuted Baudelaire for obscenity in 1857 (six poems suppressed) — the conviction was overturned only in 1949, in a belated recognition of the collection's literary importance"}
    ],
    "subjects": ["French Literature", "Modern Era", "Charles Baudelaire", "Poetry", "Symbolism", "Modernism", "19th Century", "French Poetry"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Les Fleurs du mal (Baudelaire, 1857) is the most important collection of French poetry of the 19th century and a founding document of literary Modernism. Its innovations (correspondances, spleen/idéal, the urban flaneur) inaugurated French Symbolism (Verlaine, Rimbaud, Mallarmé) and, through Symbolism, Modernism (T. S. Eliot, Walter Benjamin). The Baudelairean sensibility — aestheticised transgression, urban alienation, erotic spirituality — defined fin-de-siècle culture and shaped the 20th-century literary imagination.",
      "significanceCategory": "world-changing"
    }
  }
},

"life-is-a-dream": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780life-is-a-dream.json",
  "slug": "life-is-a-dream",
  "data": {
    "summary": "Life Is a Dream (Spanish: La vida es sueño) is a philosophical play by the Spanish Baroque playwright Pedro Calderón de la Barca (1600–1681), first performed in Madrid c. 1635 and published in 1636 as part of his Primera parte de comedias. It is generally regarded as the masterpiece of the Spanish Golden Age drama and one of the greatest plays in the Western theatrical tradition. The play dramatises the story of Segismundo, a Polish prince who has been imprisoned from birth in a tower by his father King Basilio (who has been told by astrology that his son will be a tyrant), released for one day to test the prophecy, behaves tyrannically, and is returned to the tower and told his experience was a dream — only to lead a rebellion against his father, reconquer his throne, and demonstrate that he has overcome fate through free will and virtue.\n\nLa vida es sueño is a philosophical drama exploring the nature of reality and illusion (is life a dream?), the tension between fate and free will, the ethics of honour and justice, and the capacity for human transformation through self-mastery. Segismundo's famous soliloquy ('What is life? A frenzy. What is life? An illusion, a shadow, a fiction...') is among the most celebrated speeches in Spanish literature, condensing the Baroque philosophical meditation on the dreamlike quality of human experience into a passionate and despairing lyric. The play's philosophical themes connect it to the Stoic tradition (virtue and self-mastery against fortune), the Neo-Platonic tradition (the world as shadow of a higher reality), and the Jesuit theology of Calderón's formation.\n\nCalderón was a priest and a member of the Order of St Francis; his drama is deeply shaped by Counter-Reformation Catholic theology, and Life Is a Dream can be read as a dramatisation of the Jesuit theological emphasis on free will and human responsibility against the Calvinist doctrine of predestination.",
    "causes": [
      "The Spanish Baroque philosophical and theological context — the Counter-Reformation's emphasis on human free will (against Calvinist predestination), the Jesuit tradition of moral casuistry, and the Spanish Baroque aesthetic of desengaño (disillusionment, the recognition of life's illusory nature) — provided the philosophical framework for the play's central questions about fate, free will, and the dreamlike quality of experience.",
      "Calderón's formation in Jesuit education (he studied at the Colegio Imperial in Madrid) — which emphasised both classical learning and dramatic performance (the Jesuit school drama tradition) — provided both the intellectual toolkit and the theatrical practice that shaped his drama.",
      "The theatrical tradition of the Spanish comedia — the three-act play structure, the mixing of tragic and comic elements, the use of verse forms (romance, redondilla, décima) — provided the generic framework within which Calderón's philosophical drama operates: Life Is a Dream is formally a comedia that transcends the genre through its philosophical ambition."
    ],
    "effects": [
      "Life Is a Dream had a substantial influence on German Romanticism — Schopenhauer's philosophy of the world as will and representation (the dreamlike nature of phenomenal reality) draws on related philosophical themes, and August Wilhelm Schlegel's discussion of Calderón in his Vienna lectures (1808–1812) introduced the play to German Romantic culture.",
      "The play's exploration of the dream/reality dichotomy and the question of whether human consciousness can distinguish the real from the illusory has made it a recurring reference point in the philosophy of consciousness and in literary discussions of epistemology — from Descartes's dream argument through Schopenhauer to 20th-century surrealism.",
      "As a canonical text of the Spanish Golden Age and of Western drama, Life Is a Dream has been continuously performed and staged from the 17th century to the present — it is one of the most frequently performed Spanish plays outside Spain and has been adapted into opera (by several composers), ballet, and film."
    ],
    "relationships": [
      {"sourceSlug": "pedro-calderon-de-la-barca", "sourceName": "Pedro Calderón de la Barca (1600–1681, Spanish playwright)", "verb": "AUTHORS", "targetSlug": "life-is-a-dream", "targetName": "Life Is a Dream (La vida es sueño, c. 1635, Madrid)", "context": "Calderón wrote Life Is a Dream c. 1635 — the masterpiece of Spanish Golden Age drama, exploring free will, fate, and the dreamlike quality of human experience through the story of Prince Segismundo."},
      {"sourceSlug": "life-is-a-dream", "sourceName": "Life Is a Dream (dream/reality, desengaño)", "verb": "REFLECTS", "targetSlug": "spanish-baroque-theology", "targetName": "Spanish Baroque Counter-Reformation theology (free will, desengaño)", "context": "Life Is a Dream dramatises the Jesuit theological emphasis on free will and human transformation — its 'life is a dream' theme reflects the Spanish Baroque aesthetic of desengaño (disillusionment with the illusory nature of worldly experience)."},
      {"sourceSlug": "life-is-a-dream", "sourceName": "Life Is a Dream (German Romanticism, Schlegel)", "verb": "INFLUENCES", "targetSlug": "german-romanticism", "targetName": "German Romantic literary movement (Schlegel, Schopenhauer)", "context": "August Wilhelm Schlegel's lectures on Calderón (Vienna, 1808–1812) introduced Life Is a Dream to German Romantic culture — its philosophical themes resonated with Schopenhauer's analysis of phenomenal reality as illusion."}
    ],
    "places": [
      {"name": "Madrid (first performance c. 1635; Calderón's theatrical career at the Spanish court)", "role": "Life Is a Dream was first performed in Madrid c. 1635 — Calderón was the leading dramatist of the Spanish court, writing for the royal theatres and the public corrales de comedias"},
      {"name": "Poland (fictional setting of the play — King Basilio's court)", "role": "The play is set in a fictional Poland — an exotic European locale that provided Baroque Spanish drama with the geographic distance appropriate for philosophical allegory"}
    ],
    "subjects": ["Spanish Literature", "Early Modern Era", "Pedro Calderón de la Barca", "Spanish Golden Age", "Drama", "Philosophy", "Baroque Literature", "Theatre"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Life Is a Dream (Calderón, c. 1635) is the masterpiece of Spanish Golden Age drama and one of the great philosophical plays in the Western theatrical tradition. Its exploration of the dream/reality dichotomy, fate and free will, and the capacity for human transformation through self-mastery connects the Spanish Baroque theological tradition to the European Romantic and philosophical tradition. Its influence on German Romanticism (Schlegel, Schopenhauer) and its continuous performance history demonstrate its enduring cultural significance.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-city-of-god": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-city-of-god.json",
  "slug": "the-city-of-god",
  "data": {
    "summary": "The City of God Against the Pagans (Latin: De Civitate Dei contra Paganos) is a major philosophical and theological work by Augustine of Hippo (354–430 CE), Bishop of Hippo Regius in North Africa, composed c. 413–426 CE in response to the sack of Rome by Alaric's Visigoths in 410 CE — an event that shocked the Roman world and prompted accusations that Christianity's abolition of the pagan cults was responsible for Rome's military weakness. In 22 books, Augustine develops a comprehensive philosophy of history and a theological account of the two 'cities' (civitates) — the City of God (civitas Dei, the community of those who love God above all things, including the angels and the predestined elect among humans) and the City of Man (civitas terrena, the community of those who love self above God, including the fallen angels and the damned) — which exist intermingled in earthly history but will be separated at the Last Judgement.\n\nThe City of God performs multiple tasks: Books I–X refute the pagan argument that Rome's adoption of Christianity caused its military collapse, reviewing Rome's entire history of military defeats and showing that pagan religion never guaranteed Roman security; Books XI–XXII develop Augustine's positive theology of history, the nature of the two cities, the fall of the angels, the fall of Adam, human free will and divine predestination, the City of God's pilgrimage through earthly history, and the eschatological culmination in the Last Judgement and the beatific vision. The City of God is both a massive work of Christian apologetics and the first systematic philosophy of history in the Western tradition.\n\nAugustine's influence on subsequent Christian thought — on the theology of grace and predestination that shaped the debates of the Reformation (Luther and Calvin drew heavily on Augustine's anti-Pelagian writings, which are closely related to the City of God's theology), on medieval political theology (the distinction between spiritual and temporal authority), and on the philosophy of history (the idea of history as a meaningful narrative directed toward an eschatological goal) — is unparalleled among Western theologians.",
    "causes": [
      "The sack of Rome (410 CE) by Alaric's Visigoths — the first sack of Rome in 800 years — shocked the Roman world and generated accusations that Christianity's abolition of the pagan cults had weakened Rome's divine protection: Augustine began writing the City of God directly in response to these accusations, which were articulated by pagan Roman aristocrats who had taken refuge in North Africa.",
      "Augustine's anti-Pelagian controversies — his theological battles against Pelagius's teaching that humans can achieve salvation through free will without divine grace — shaped the theological argument of the City of God: Augustine's doctrine of predestination and grace, developed in response to Pelagianism, is central to his account of the City of God.",
      "The Platonic and Neoplatonic philosophical tradition — Augustine's early philosophical formation in Platonism and his encounter with Plotinus's Enneads — provided the philosophical framework for the City of God's metaphysics: the two cities are a Christianisation of the Platonic distinction between the intelligible and sensible worlds, and Augustine's theological ontology draws heavily on Neoplatonic concepts."
    ],
    "effects": [
      "The City of God established the framework for medieval Christian political theology — the distinction between the spiritual and temporal powers (Church and State), and the subordination of temporal authority to spiritual ends — that shaped the medieval Church's claims to political authority and the Investiture Controversy.",
      "Augustine's theology of grace and predestination in the City of God directly influenced Luther's and Calvin's Reformation theology — Luther explicitly relied on Augustine's anti-Pelagian writings in his attack on works-righteousness, and Calvin's doctrine of double predestination is a systematisation of Augustinian themes.",
      "Augustine's philosophy of history — the idea that earthly history has a meaning directed toward an eschatological goal, that the City of God and the City of Man are intermingled in history but will be separated at the Last Judgement — created the foundational framework for Christian philosophy of history that shaped Western historiography from Orosius through the medieval chronicles to Hegel's secular version of the Christian historical narrative."
    ],
    "relationships": [
      {"sourceSlug": "augustine-of-hippo", "sourceName": "Augustine of Hippo (354–430 CE, Bishop of Hippo, Church Father)", "verb": "AUTHORS", "targetSlug": "the-city-of-god", "targetName": "The City of God (De Civitate Dei, c. 413–426 CE, 22 books)", "context": "Augustine composed the City of God c. 413–426 CE in response to the sack of Rome (410 CE) — a 22-book work of Christian apologetics and the first systematic philosophy of history in the Western tradition."},
      {"sourceSlug": "the-city-of-god", "sourceName": "City of God (grace, predestination, anti-Pelagian)", "verb": "INFLUENCES", "targetSlug": "protestant-reformation-theology", "targetName": "Protestant Reformation theology (Luther, Calvin — grace and predestination)", "context": "Luther's attack on works-righteousness and Calvin's doctrine of predestination both drew heavily on Augustine's theology of grace in the City of God and the related anti-Pelagian writings."},
      {"sourceSlug": "the-city-of-god", "sourceName": "City of God (two cities, temporal/spiritual distinction)", "verb": "ESTABLISHES", "targetSlug": "medieval-political-theology", "targetName": "Medieval Christian political theology (Church and State)", "context": "Augustine's distinction between the City of God and the City of Man established the framework for medieval Christian political theology — the subordination of temporal power to spiritual ends that shaped the medieval Church's political claims."}
    ],
    "places": [
      {"name": "Hippo Regius, North Africa (Augustine's see; sack of Rome 410 CE, the immediate context)", "role": "Augustine was Bishop of Hippo Regius in Roman North Africa — the City of God was written there in response to the sack of Rome (410 CE), with pagan refugees from Rome who blamed Christianity for the disaster"},
      {"name": "Rome (sack by Alaric, 410 CE — the political crisis that prompted the City of God)", "role": "The sack of Rome in 410 CE — the first in 800 years — was the immediate political occasion for the City of God: Augustine's work is a direct response to pagan accusations that Christianity had weakened Rome's divine protection"}
    ],
    "subjects": ["Christian Theology", "Late Antique Era", "Augustine of Hippo", "Philosophy of History", "Christian Apologetics", "Latin Literature", "Political Theology", "Church Fathers"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The City of God (Augustine, c. 413–426 CE) is the most influential work of Christian theology after the New Testament. Its two-city framework shaped medieval political theology; its grace and predestination theology directly influenced Luther and Calvin; its philosophy of history created the framework for Christian historical thought from Orosius to Hegel. Written in response to the sack of Rome (410 CE), it is the definitive Christian response to the collapse of Roman civilisation and a foundational text of Western intellectual culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"liber-pontificalis": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780liber-pontificalis.json",
  "slug": "liber-pontificalis",
  "data": {
    "summary": "The Liber Pontificalis ('Book of the Popes') is a collection of Latin papal biographies covering the bishops of Rome from St Peter (traditionally) to the 15th century — begun in the 6th century CE (the first major compilation c. 530–540 CE is attributed to various editors, with the first certain datable section covering Agapetus I, 535–536 CE), continued by successive papal chancery scribes and biographers across the following centuries, and extending in various manuscript traditions to the 15th century. The Liber Pontificalis is the primary narrative source for the history of the papacy from late antiquity through the early medieval period — a continuous series of papal biographies that record the building programme of each pope, the donations and relics given to Roman churches, major political events, relations with emperors and kings, heresies confronted and condemned, and the deaths and burials of each bishop of Rome.\n\nThe Liber Pontificalis is an extraordinary historical source for multiple fields: it is the most detailed surviving record of the building programme of early medieval Rome (the churches, cemeteries, basilicas, and baths built or restored by each pope, often with precise measurements and descriptions of the decoration), making it the primary source for the history of early Christian art and architecture; it records major political events of the 6th–9th centuries from a Roman perspective (the Lombard invasions, the role of the papacy in the formation of the Carolingian alliance, the coronation of Charlemagne in 800 CE); and it provides the genealogical and biographical data for hundreds of medieval popes.\n\nThe Liber Pontificalis is not a single author's work but a cumulative institutional production — each generation added lives of the most recent popes, sometimes by contemporaries, sometimes by retrospective biographers — and its reliability varies considerably from section to section. The most reliable sections are those written close to the events they describe; the earliest sections (covering the first centuries of the papacy) contain legendary and hagiographic material.",
    "causes": [
      "The institutional needs of the Roman papacy — the need to establish and maintain the authority and prestige of the Roman episcopal see through a continuous record of its bishops, connecting the current pope to St Peter through an unbroken succession — provided the primary motivation for the Liber Pontificalis's compilation: it is a document of papal institutional identity.",
      "The 6th-century crisis of the Roman church — the Ostrogothic kingdom's control of Italy, the Justinianic reconquest (535–554 CE), and the subsequent Lombard invasions — created the political context for the Liber Pontificalis's first major compilation: the papacy's need to document its political and building activities in the context of its increasingly independent role as protector of Rome.",
      "The Roman tradition of biographical record-keeping — the late antique genre of the imperial biography (Suetonius's Lives of the Twelve Caesars, the Historia Augusta) — provided the generic model for the Liber Pontificalis: papal biography was modelled on imperial biography, reflecting the papacy's self-conception as the heir of Roman imperial authority."
    ],
    "effects": [
      "The Liber Pontificalis's records of the building programme of each pope — the churches, basilicas, and decorative programmes commissioned by the popes from the 4th century to the 9th — are the primary source for the history of early Christian art and architecture in Rome, preserving information about lost works and providing the documentary basis for the attribution of surviving ones.",
      "The Liber Pontificalis's account of the formation of the Carolingian-papal alliance — the visits of Pippin III to Rome (754, 756), the Donation of Pippin, the coronation of Charlemagne (800 CE) — provides the primary contemporary narrative for one of the most important political developments in early medieval European history: the formation of the papal states and the Carolingian alliance.",
      "The Liber Pontificalis became a model for subsequent medieval institutional chronicle-writing — the practice of maintaining continuous institutional histories through accretive biographical records — and its prestige as a source of papal authority was cited repeatedly in medieval political and ecclesiastical controversies."
    ],
    "relationships": [
      {"sourceSlug": "liber-pontificalis", "sourceName": "Liber Pontificalis (papal biographies, 6th–15th century)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "medieval-papal-history", "targetName": "History of the medieval papacy (4th–15th century)", "context": "The Liber Pontificalis is the primary narrative source for the history of the papacy from late antiquity through the early medieval period — recording the building programme, political events, and biographical data for each bishop of Rome."},
      {"sourceSlug": "liber-pontificalis", "sourceName": "Liber Pontificalis (Carolingian coronation, papal states formation)", "verb": "DOCUMENTS", "targetSlug": "carolingian-papal-alliance", "targetName": "Carolingian-papal alliance (Pippin III, Charlemagne coronation 800 CE)", "context": "The Liber Pontificalis provides the primary contemporary narrative for the formation of the Carolingian-papal alliance — Pippin III's donations (754, 756), the foundation of the papal states, and Charlemagne's coronation in Rome (800 CE)."},
      {"sourceSlug": "liber-pontificalis", "sourceName": "Liber Pontificalis (building programme, early Christian art)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "early-christian-rome-architecture", "targetName": "Early Christian art and architecture in Rome (4th–9th century)", "context": "The Liber Pontificalis's records of the churches, basilicas, and decorations commissioned by each pope are the primary source for the history of early Christian art and architecture in Rome."}
    ],
    "places": [
      {"name": "Rome (papal chancery, composition of Liber Pontificalis; churches documented)", "role": "The Liber Pontificalis was compiled by the Roman papal chancery and primarily documents the built environment and institutional history of Rome — it is a Roman document produced by the Roman church for the documentation of Rome"},
      {"name": "Latin Europe (manuscript tradition; use in political and ecclesiastical controversies)", "role": "The Liber Pontificalis was copied and used across Latin Europe — its documentation of papal authority and the Carolingian alliance was cited in medieval political and ecclesiastical controversies throughout the Middle Ages"}
    ],
    "subjects": ["Medieval History", "Late Antique Era", "Papal History", "Latin Literature", "Institutional History", "Early Christian Art", "Biography", "Church History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Liber Pontificalis (begun c. 530–540 CE, continued to the 15th century) is the primary narrative source for the history of the papacy from late antiquity through the medieval period. Its records of papal building programmes are the primary source for early Christian art and architecture in Rome; its accounts of the Carolingian-papal alliance document one of the most consequential political developments in early medieval history. As a continuous institutional record spanning a millennium, it is one of the great documents of medieval institutional history.",
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
