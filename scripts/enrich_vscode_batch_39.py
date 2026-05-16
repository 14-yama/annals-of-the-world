#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 39 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: i-ching, jabberwocky, kalila-and-demna,
          golden-legend, a-dance-with-dragons,
          caduceus, minimal-group-paradigm,
          manifest-der-kommunistischen-partei
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-39-may2026"

ENRICHMENTS = {

"i-ching": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780i-ching.json",
  "slug": "i-ching",
  "data": {
    "summary": "The I Ching (易經, Yì Jīng, 'Classic of Changes' or 'Book of Changes') is one of the oldest and most influential texts in the world — a Chinese divination manual and philosophical classic, probably reaching its textual form during the Western Zhou dynasty (c. 1000–750 BCE), though its core component, the 64 hexagrams (six-line symbols composed of broken and unbroken lines), may be significantly older. The I Ching is one of the Five Classics of Confucian literature (alongside the Book of Odes, Book of Documents, Book of Rites, and Spring and Autumn Annals) and is the foundation of traditional Chinese cosmological, philosophical, and ethical thought. It was the primary resource for the traditional Chinese practice of divination (yarrow stalk casting, coin tossing) and has been continuously used for divinatory, philosophical, and literary purposes for over three thousand years.\n\nThe I Ching's structure consists of 64 hexagrams — binary symbols formed from combinations of six yin (broken, −−) and yang (unbroken, —) lines, representing all possible combinations of change — each accompanied by a brief textual statement (the gua ci, hexagram statement) and six additional statements for each individual line (the yao ci, line statements), traditionally attributed to King Wen of Zhou (the hexagram statements) and the Duke of Zhou (the line statements). These core texts are supplemented by the Ten Wings (Shi Yi), a set of philosophical commentaries traditionally attributed to Confucius (though modern scholarship dates them to the Warring States period, 5th–3rd century BCE), which transform the divination manual into a philosophical text on the nature of change, the cosmos, and human virtue.\n\nThe I Ching's influence extends far beyond China — introduced to Europe via the Jesuit missionaries and their translations (notably Leibniz's encounter with the binary hexagrams in 1701, which influenced his development of binary arithmetic), translated by Richard Wilhelm (I Ging, 1923 — the most influential Western translation), and adopted by the Western counter-culture in the 1960s–1970s. The I Ching's 64 hexagrams have been compared to binary code (two values: yin/yang = 0/1) and to the genetic code (64 codons = 64 hexagrams), demonstrating its enduring capacity to generate new interpretations.",
    "causes": [
      "The ancient Chinese practice of divination — the use of oracle bones (Shang dynasty, c. 1600–1046 BCE) and yarrow stalks to determine the will of heaven and the auspiciousness of actions — provided the divinatory context from which the I Ching's hexagram system developed: the binary line system replaced bone-crack divination as the primary Chinese divinatory method.",
      "The cosmological philosophy of yin and yang — the Chinese concept of the universe as constituted by two complementary, dynamic forces (yin: dark, passive, female; yang: bright, active, male) — provided the philosophical framework of the I Ching's hexagram system: the 64 hexagrams represent all possible combinations of yin and yang change, and the text's commentary tradition interprets the hexagrams in terms of cosmic change and human action.",
      "The Confucian canonisation of the I Ching — its inclusion in the Five Classics of Confucian education — ensured its transmission as the foundational text of Chinese philosophical and cosmological thought, and the composition of the Ten Wings (philosophical commentaries) transformed it from a divination manual into a philosophical classic."
    ],
    "effects": [
      "The I Ching's influence on Chinese philosophy, literature, and culture over three thousand years has been pervasive — from its role in the development of Daoist cosmology (the Daodejing's yin-yang imagery), to its influence on Neo-Confucian metaphysics (the Song dynasty philosophers, particularly Zhou Dunyi and Zhu Xi), to its use in Chinese medicine, geomancy (feng shui), and martial arts.",
      "Leibniz's encounter with the I Ching hexagrams in 1701 — through the Jesuit missionary Joachim Bouvet's presentation of the hexagrams' binary structure — reinforced his independent development of binary arithmetic, creating one of the most remarkable cross-cultural intellectual encounters in history: the Chinese binary system of yin and yang prefiguring the mathematical foundation of modern computing.",
      "Richard Wilhelm's German translation (I Ging, 1923) — introduced to English-speaking readers via Cary Baynes's translation (1950) and Carl Jung's foreword — initiated the I Ching's adoption by Western psychology (Jung's concept of synchronicity was partly developed from I Ching divination) and the Western counter-culture of the 1960s–1970s."
    ],
    "relationships": [
      {"sourceSlug": "i-ching", "sourceName": "I Ching (Classic of Changes, c. 1000 BCE)", "verb": "PART_OF", "targetSlug": "five-classics-confucian", "targetName": "Five Classics of Confucian literature", "context": "The I Ching is one of the Five Classics of Confucian literature — its Confucian canonisation ensured its transmission as the foundational text of Chinese philosophical and cosmological thought for over two millennia."},
      {"sourceSlug": "i-ching", "sourceName": "I Ching (binary hexagrams, Leibniz)", "verb": "INFLUENCES", "targetSlug": "binary-arithmetic", "targetName": "Binary arithmetic and modern computing (Leibniz 1701)", "context": "Leibniz's encounter with the I Ching hexagrams (via Bouvet, 1701) reinforced his development of binary arithmetic — the Chinese binary yin/yang system influencing the mathematical foundation of modern computing."},
      {"sourceSlug": "i-ching", "sourceName": "I Ching (Wilhelm translation, Jung)", "verb": "INFLUENCES", "targetSlug": "carl-jung", "targetName": "Carl Jung (synchronicity, analytical psychology)", "context": "Carl Jung's foreword to the Wilhelm/Baynes translation (1950) and his concept of synchronicity were partly developed from I Ching divination — one of the most significant encounters between Eastern and Western thought in 20th-century psychology."}
    ],
    "places": [
      {"name": "China (Western Zhou dynasty origin, c. 1000 BCE; continuous use)", "role": "The I Ching originated in China during the Western Zhou dynasty — compiled from earlier divinatory traditions — and has been continuously used for divination, philosophy, and literary commentary for over three thousand years"},
      {"name": "Europe and the West (Jesuit transmission, Leibniz, Wilhelm translation)", "role": "The I Ching was transmitted to Europe via the Jesuit missionaries — Leibniz's engagement with the hexagrams (1701) and Richard Wilhelm's German translation (1923) introduced it to Western intellectual and counter-cultural thought"}
    ],
    "subjects": ["Chinese Literature", "Ancient Era", "Chinese Philosophy", "Divination", "Confucianism", "Cosmology", "Binary Systems", "Classic Text"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The I Ching (c. 1000 BCE) is one of the oldest and most influential texts in the world — a foundational Chinese philosophical classic, continuously used for three thousand years. Its influence ranges from Chinese cosmology, Daoist and Neo-Confucian philosophy, and traditional medicine to Leibniz's binary arithmetic (from the hexagrams) and Western counter-cultural adoption. Its 64 hexagram binary system is one of the most remarkable intellectual structures in human civilisation.",
      "significanceCategory": "world-changing"
    }
  }
},

"jabberwocky": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780jabberwocky.json",
  "slug": "jabberwocky",
  "data": {
    "summary": "Jabberwocky is a nonsense poem by Lewis Carroll (Charles Lutwidge Dodgson, 1832–1898), first published as part of Through the Looking-Glass, and What Alice Found There (1871) — Carroll's sequel to Alice's Adventures in Wonderland (1865) — and almost certainly the most famous nonsense poem in the English language. The poem narrates in ballad-like stanzas the slaying of a monster called the Jabberwock by a young hero wielding a 'vorpal sword', the hero's triumphant return, and his father's celebrating cry 'O frabjous day! Callooh! Callay!'. Jabberwocky is composed almost entirely of nonsense words — portmanteau words (words Carroll coined by blending two words, like 'slithy' from 'lithe' and 'slimy', 'mimsy' from 'miserable' and 'flimsy') and invented words with no established meaning — yet it manages to convey vivid narrative, emotional force, and a complete dramatic arc through its phonetic and grammatical structures alone.\n\nJabberwocky is the first literary instantiation of what Humpty Dumpty (in Through the Looking-Glass) calls a 'portmanteau word' — Carroll's coinage for a word formed by blending two words and their meanings. Several of the poem's invented words have passed into the English language: 'chortle' (a blend of 'chuckle' and 'snort'), 'galumph' (a blend of 'gallop' and 'triumph'), and 'burble'. The poem is also the primary literary example of Lewis Carroll's interest in the relationship between linguistic form (grammar, phonetics, prosody) and meaning — demonstrating that a text can be grammatically coherent and emotionally resonant while being semantically opaque, a demonstration that has fascinated linguists, philosophers of language, and cognitive scientists.\n\nJabberwocky has been enormously influential in literature, linguistics, and popular culture — it has been translated into multiple languages (demonstrating the challenge of translating nonsense — the translator must invent equivalent nonsense in the target language), parodied, quoted, and alluded to across the full range of English-language literature, and its invented vocabulary (particularly 'chortle' and 'galumph') has become part of standard English.",
    "causes": [
      "Lewis Carroll's fascination with logic, language, and the relationship between linguistic form and meaning — his career as a mathematics lecturer at Oxford and his engagement with formal logic (Symbolic Logic, 1896) — provided the intellectual foundation for Jabberwocky's exploration of grammatical coherence without semantic content: the poem demonstrates that narrative and emotional force can be communicated through grammar and sound alone.",
      "The Victorian tradition of literary nonsense — the tradition of Edward Lear's limericks and nonsense verse (The Owl and the Pussycat, 1871), and the broader Victorian taste for comic, playful, and fantastical literature — provided the generic context for Jabberwocky's nonsense: Carroll's portmanteau words and invented vocabulary are a sophisticated development of the nonsense tradition.",
      "The narrative structure of Through the Looking-Glass — Alice's passage through the looking-glass into a world where language and logic work differently — provided the fictional context for Jabberwocky: the poem appears in a book Alice finds in the looking-glass world, written in mirror-writing, and its nonsense language reflects the inverted logic of the looking-glass world."
    ],
    "effects": [
      "Jabberwocky's contribution of new words to the English language — 'chortle', 'galumph', 'burble', and (through Carroll's broader work) 'portmanteau word' — is Carroll's most direct linguistic legacy: these coinages have entered standard dictionaries and are used without awareness of their Carroll origin.",
      "Jabberwocky's influence on linguistics and philosophy of language — particularly the demonstration that grammatically coherent text can be semantically opaque — made it a reference point for discussions of the relationship between syntax and semantics, from the early 20th century to Chomsky's generative grammar (Chomsky's 'Colorless green ideas sleep furiously' parallels Carroll's method).",
      "Jabberwocky's influence on literature and popular culture has been enormous — it has been translated into over 65 languages (each translation requiring the invention of equivalent nonsense), parodied by countless writers, and its vocabulary and imagery (the Jabberwock, the vorpal sword, frabjous) have entered the English-language cultural imagination as archetypal nonsense references."
    ],
    "relationships": [
      {"sourceSlug": "lewis-carroll", "sourceName": "Lewis Carroll (1832–1898)", "verb": "AUTHORS", "targetSlug": "jabberwocky", "targetName": "Jabberwocky (Through the Looking-Glass, 1871)", "context": "Carroll published Jabberwocky as part of Through the Looking-Glass (1871) — the most famous nonsense poem in English, composed almost entirely of invented portmanteau words."},
      {"sourceSlug": "jabberwocky", "sourceName": "Jabberwocky (portmanteau words, nonsense)", "verb": "CONTRIBUTES_TO", "targetSlug": "english-language", "targetName": "English language (new vocabulary)", "context": "Jabberwocky contributed 'chortle', 'galumph', and 'burble' to the English language — Carroll coinages that entered standard English without awareness of their Carroll origin."},
      {"sourceSlug": "jabberwocky", "sourceName": "Jabberwocky (syntax without semantics)", "verb": "INFLUENCES", "targetSlug": "generative-grammar", "targetName": "Generative grammar and linguistics (Chomsky)", "context": "Jabberwocky's demonstration that grammatically coherent text can be semantically opaque influenced linguistic discussions of syntax-semantics relationships, paralleled by Chomsky's 'Colorless green ideas sleep furiously' in generative grammar."}
    ],
    "places": [
      {"name": "Oxford, England (Lewis Carroll's university context)", "role": "Carroll was a mathematics lecturer at Christ Church, Oxford — his academic context of formal logic, linguistics, and Victorian intellectual culture provided the intellectual foundation for Jabberwocky's exploration of language"},
      {"name": "Global (translation into 65+ languages, worldwide cultural influence)", "role": "Jabberwocky has been translated into over 65 languages — each translation requiring the invention of equivalent nonsense — demonstrating the extraordinary reach of Carroll's nonsense poetry across linguistic and cultural boundaries"}
    ],
    "subjects": ["English Literature", "Modern Era", "Lewis Carroll", "Nonsense Poetry", "Victorian Literature", "Linguistics", "Children's Literature", "Language"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Jabberwocky (Carroll, 1871) is the most famous nonsense poem in English — a linguistic experiment demonstrating that grammatical coherence and emotional force can be achieved without semantic content. It contributed 'chortle', 'galumph', and 'burble' to standard English and influenced linguistics (the syntax-semantics interface) and philosophy of language. Translated into over 65 languages, it is one of the most linguistically provocative short poems in world literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"kalila-and-demna": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780kalila-and-demna.json",
  "slug": "kalila-and-demna",
  "data": {
    "summary": "Kalila and Dimna (Arabic: كليلة ودمنة, Kalīla wa-Dimna) is a collection of Arabic animal fables adapted from the Sanskrit Panchatantra (c. 300 BCE) by Ibn al-Muqaffa' (c. 720–756 CE), an Abbasid scholar and translator who rendered a Middle Persian (Pahlavi) version of the Panchatantra into classical Arabic around 750 CE. The collection is named after two jackals — Kalila (the cautious adviser) and Dimna (the scheming courtier) — whose relationship and the consequences of Dimna's malicious counsel frame the work's first and most famous section. Kalila and Dimna is a 'mirror for princes' (speculum principis) — a book of practical political wisdom presented through animal fables — and is one of the most widely translated and influential texts in the history of world literature, a vehicle through which the ancient Indian wisdom tradition of the Panchatantra was transmitted to the medieval Arabic, Persian, Turkish, Hebrew, and eventually European literary traditions.\n\nIbn al-Muqaffa's Arabic adaptation (c. 750 CE) was itself derived from the Pahlavi translation made for the Sasanian King Khusraw I Anushirvan (r. 531–579 CE), reportedly brought from India by the physician Burzoy. The Arabic Kalila and Dimna became one of the most widely read texts of the Abbasid caliphate and was translated into Persian (by Rudaki, 10th century, and Nasrallah Munshi, 12th century), into Hebrew (by Rabbi Joel, c. 1080), into Latin (Directorium Humanae Vitae, by John of Capua, c. 1270), into Spanish (Calila e Dimna, c. 1251, commissioned by the future Alfonso X), into Italian, Greek, and eventually into most European languages — becoming the primary vehicle for the transmission of the Indian fable tradition to the medieval West, where its animal stories influenced Aesop's fables' reception, La Fontaine's Fables, and the European fable tradition.\n\nThe Panchatantra-Kalila and Dimna transmission is one of the most remarkable examples of literary diffusion in world history — a collection of Indian animal fables composed c. 300 BCE that was translated through Sanskrit, Pahlavi, Arabic, Hebrew, Latin, and the major European vernaculars over a period of nearly two thousand years, reaching every major literary culture of the medieval and early modern world.",
    "causes": [
      "The Sasanian interest in Indian wisdom literature — Khusraw I Anushirvan's commissioning of the physician Burzoy to travel to India and bring back the Panchatantra — created the Pahlavi translation that was the immediate source of Ibn al-Muqaffa's Arabic version: the Sasanian court's cultural programme of absorbing Indian scientific and philosophical knowledge was the institutional context for the text's transmission.",
      "The Abbasid translation movement (bayt al-hikma, 'House of Wisdom') — the massive Arabic translation project of the 8th–9th centuries that rendered Greek, Persian, Indian, and Syriac scientific and literary texts into Arabic — provided the broader cultural context for Ibn al-Muqaffa's adaptation: the Arabic Kalila and Dimna is part of the most important intellectual translation programme in history.",
      "The universal relevance of the Panchatantra's political wisdom — its advice on the conduct of rulers, ministers, and subjects in the form of entertaining animal fables — made it adaptable to the courts and political cultures of vastly different civilisations, from the Indian subcontinent to Persia, the Arab caliphate, the medieval Christian kingdoms, and early modern Europe."
    ],
    "effects": [
      "Kalila and Dimna's transmission through Arabic, Hebrew, and Latin translations to medieval Europe made the Indian fable tradition — originating in the Panchatantra — one of the primary sources of the European fable and novella traditions, influencing La Fontaine's Fables (1668), Boccaccio's Decameron, and the entire European tradition of politically didactic animal story.",
      "Ibn al-Muqaffa's Arabic Kalila and Dimna became the model for classical Arabic prose style — his elegant, clear Arabic was studied as a stylistic exemplar for centuries, and the text was one of the foundational documents of classical Arabic literary prose.",
      "The Kalila and Dimna transmission is the primary example of the Panchatantra's extraordinary diffusion — a text that spread from India through Persia, Arabia, Byzantium, medieval Europe, and the Ottoman Empire, demonstrating how a collection of political fables can be absorbed and adapted by every major literary culture it encounters."
    ],
    "relationships": [
      {"sourceSlug": "kalila-and-demna", "sourceName": "Kalila and Dimna (Ibn al-Muqaffa', c. 750 CE)", "verb": "ADAPTED_FROM", "targetSlug": "panchatantra", "targetName": "Panchatantra (Sanskrit, c. 300 BCE)", "context": "Kalila and Dimna is Ibn al-Muqaffa's Arabic adaptation of the Panchatantra — transmitted through a Pahlavi intermediary — the primary vehicle through which the Indian fable tradition reached the medieval Arabic, Persian, Hebrew, Latin, and European worlds."},
      {"sourceSlug": "kalila-and-demna", "sourceName": "Kalila and Dimna (Arabic prose model)", "verb": "INFLUENCES", "targetSlug": "classical-arabic-prose", "targetName": "Classical Arabic literary prose tradition", "context": "Ibn al-Muqaffa's Arabic translation of Kalila and Dimna became the model for classical Arabic prose style — his elegant, clear Arabic was studied as a stylistic exemplar for centuries in the Arabic literary tradition."},
      {"sourceSlug": "kalila-and-demna", "sourceName": "Kalila and Dimna (Latin Directorium, La Fontaine)", "verb": "INFLUENCES", "targetSlug": "la-fontaine-fables", "targetName": "La Fontaine's Fables (1668, European fable tradition)", "context": "Through the Latin Directorium Humanae Vitae (John of Capua, c. 1270) and Spanish Calila e Dimna (c. 1251), Kalila and Dimna transmitted the Panchatantra fable tradition to medieval Europe, influencing La Fontaine and the European fable tradition."}
    ],
    "places": [
      {"name": "Baghdad and the Abbasid Caliphate (Ibn al-Muqaffa', c. 750 CE)", "role": "Ibn al-Muqaffa' translated Kalila and Dimna in Baghdad during the early Abbasid caliphate — the text became one of the most widely read texts of the Abbasid court and the model for classical Arabic prose"},
      {"name": "India (Panchatantra origin, c. 300 BCE); Persia (Pahlavi translation, 6th century)", "role": "The Panchatantra-Kalila and Dimna transmission originated in India and was transmitted through Persia (Sasanian Pahlavi translation, commissioned by Khusraw I) before reaching the Arabic-speaking world"}
    ],
    "subjects": ["Arabic Literature", "Medieval Era", "Fables", "Indian Literature", "Political Wisdom", "Translation History", "Animal Stories", "Ibn al-Muqaffa"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Kalila and Dimna (Ibn al-Muqaffa', c. 750 CE) is one of the most widely translated and influential texts in world literary history — the primary vehicle through which the Indian Panchatantra fable tradition was transmitted to the medieval Arabic, Persian, Hebrew, Latin, and European worlds. Its transmission from Sanskrit through Pahlavi, Arabic, and Latin to every major European vernacular over two millennia is a landmark in the history of cross-cultural literary diffusion.",
      "significanceCategory": "world-changing"
    }
  }
},

"golden-legend": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782golden-legend.json",
  "slug": "golden-legend",
  "data": {
    "summary": "The Golden Legend (Latin: Legenda aurea, also Legenda Sanctorum) is a collection of hagiographies (saints' lives) compiled c. 1260 by Jacobus de Voragine (c. 1230–1298), a Genoese Dominican friar who later became Archbishop of Genoa (1292) — one of the most widely read books of the entire medieval period, surviving in over 900 manuscripts in Latin alone (alongside numerous vernacular translations), and second only to the Bible in the number of manuscripts produced in medieval Europe. The Golden Legend collects the lives of approximately 180 saints and apostles, arranged according to the liturgical calendar, with accounts of the major feasts of the Christian year — Christmas, Easter, Pentecost, the feasts of the apostles, the stories of the major martyrs and confessors — drawing on earlier hagiographic sources (the Acta Sanctorum tradition), legendary narratives, and theological commentary to create a comprehensive guide to Christian sanctity and the liturgical year.\n\nThe Golden Legend was the primary source of popular knowledge about Christian saints in the medieval West — it transmitted the canonical stories of St. George and the dragon, St. Christopher, the Virgin Mary's life (including the Assumption and Immaculate Conception narratives), the Three Kings (Magi), the Holy Cross legend, St. Nicholas, St. Barbara, and dozens of other saints whose iconography dominated medieval and Renaissance art. The accounts in the Golden Legend — often dramatic, miraculous, and didactically structured — were the source texts for the iconographic programmes of the major Gothic and Renaissance cathedral decorations, altarpieces, and manuscript illuminations: the artists of medieval and Renaissance Europe depicted saints whose stories they knew from the Golden Legend.\n\nThe Golden Legend's influence on Western art, literature, and culture is incalculable — it was the primary source for the iconographic tradition of Christian saints in Western visual art from the 13th to the 16th centuries, and was one of the first texts printed by William Caxton on his English printing press (The Golden Legend, 1483). The humanist critics of the 16th century (including Erasmus and Polydore Vergil) attacked it as historically unreliable and credulous, but this criticism was part of the broader Protestant-humanist critique of popular Catholic devotion.",
    "causes": [
      "The Dominican Order's pastoral and preaching mission — the need to provide friars with accessible, comprehensive, and narratively engaging accounts of the saints for use in sermons and pastoral instruction — was the primary institutional motivation for the Golden Legend: Jacobus de Voragine compiled it as a practical preaching resource for Dominican friars.",
      "The medieval Western Church's liturgical calendar — which organised the Christian year around the feasts of the saints — created the structural framework of the Golden Legend: the saints' lives are arranged according to the liturgical year, making the collection a comprehensive guide to Christian liturgical observance as well as a repository of hagiographic narrative.",
      "The enormous medieval demand for saints' lives — hagiography was the most widely read genre of medieval Latin literature after the Bible and liturgical texts — reflected the deep popular investment in the saints as intercessors, models of virtue, and objects of devotion that drove the Golden Legend's extraordinary manuscript production and readership."
    ],
    "effects": [
      "The Golden Legend's role as the primary source of iconographic knowledge about Christian saints made it the de facto visual programme guide for medieval and Renaissance art — the stories it transmitted determined which saints were depicted, what attributes they carried, and what scenes were shown, from the mosaics of Venice to the altarpieces of Florence and the windows of Chartres.",
      "William Caxton's printing of the Golden Legend (1483) — one of the first and most substantial English-language printed books — disseminated the saints' lives to English readers and established hagiographic narrative as one of the primary early printed genres, demonstrating the importance of medieval religious content in the early history of print.",
      "The humanist and Protestant critique of the Golden Legend — particularly Erasmus's mockery of its uncritical acceptance of legendary material — contributed to the broader Reformation critique of the cult of saints and the popular Catholic devotional culture that the Golden Legend had sustained, making it one of the contested texts at the centre of the Reformation's debate over authority, tradition, and popular religion."
    ],
    "relationships": [
      {"sourceSlug": "jacobus-de-voragine", "sourceName": "Jacobus de Voragine (c. 1230–1298)", "verb": "COMPILES", "targetSlug": "golden-legend", "targetName": "Golden Legend (Legenda aurea, c. 1260)", "context": "Jacobus de Voragine compiled the Golden Legend c. 1260 as a Dominican preaching resource — the most widely read collection of saints' lives in the medieval West, surviving in over 900 Latin manuscripts."},
      {"sourceSlug": "golden-legend", "sourceName": "Golden Legend (saints' lives, iconographic source)", "verb": "INFLUENCES", "targetSlug": "medieval-renaissance-art", "targetName": "Medieval and Renaissance religious art", "context": "The Golden Legend was the primary iconographic source for medieval and Renaissance art — the stories it transmitted determined the saints depicted, their attributes, and the scenes shown in cathedrals, altarpieces, and manuscript illuminations."},
      {"sourceSlug": "golden-legend", "sourceName": "Golden Legend (Caxton edition, 1483)", "verb": "PRINTED_BY", "targetSlug": "william-caxton", "targetName": "William Caxton (English printing press, 1476)", "context": "William Caxton printed the Golden Legend (1483) on his English press — one of the first and most substantial English-language printed books, disseminating the saints' lives to English readers and establishing hagiography as a primary early printed genre."}
    ],
    "places": [
      {"name": "Genoa, Italy (Jacobus de Voragine, Dominican friar, compilation c. 1260)", "role": "The Golden Legend was compiled by Jacobus de Voragine, a Genoese Dominican — later Archbishop of Genoa — as a practical preaching resource for the Dominican Order, reflecting the Italian Dominican institutional context"},
      {"name": "Medieval Europe (over 900 Latin manuscripts, widespread vernacular translations)", "role": "The Golden Legend was one of the most widely distributed texts in medieval Europe — over 900 Latin manuscripts survive, alongside vernacular translations in Italian, French, English, German, Dutch, and other languages"}
    ],
    "subjects": ["Medieval Literature", "Medieval Era", "Hagiography", "Dominican Order", "Medieval Art", "Catholic Church", "Saints' Lives", "Jacobus de Voragine"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Golden Legend (Jacobus de Voragine, c. 1260) is one of the most widely read books of the medieval period — second only to the Bible in manuscript production. As the primary source of popular knowledge about Christian saints, it determined the iconographic programmes of medieval and Renaissance art across Europe. William Caxton's printing (1483) made it one of the first major English printed books, and humanist/Protestant criticism of its legendary content placed it at the centre of Reformation debates over popular Catholic devotion.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-dance-with-dragons": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-dance-with-dragons.json",
  "slug": "a-dance-with-dragons",
  "data": {
    "summary": "A Dance with Dragons is the fifth novel in George R. R. Martin's A Song of Ice and Fire epic fantasy series, published on 12 July 2011 by Bantam Books — after a six-year gap following A Feast for Crows (2005) and the longest publication interval in the series to that point. A Dance with Dragons runs concurrently with A Feast for Crows (covering the same timeline as the fourth book), then extends beyond it, following the characters absent from the fourth volume: Jon Snow's increasingly difficult command at Castle Black and the Wall, Daenerys Targaryen's troubled rule of Meereen and her struggle to control her dragons, Tyrion Lannister's exile journey eastward, Bran Stark's training beyond the Wall with the Three-Eyed Crow (Brynden Rivers), and Stannis Baratheon's northern campaign. The novel also introduces Dorne's plot (the 'Queenmaker' scheme) and picks up several storylines from A Feast for Crows after the timeline catches up.\n\nA Dance with Dragons is notable for its structural complexity — its parallel-then-sequential relationship with A Feast for Crows created a demanding narrative architecture that Martin has described as the most difficult structural problem he faced in the series. The novel's most significant narrative events include Jon Snow's controversial decisions at the Wall (admitting the wildlings, alliance with the Free Folk) that culminate in his assassination by his own Night's Watch brothers; Daenerys's departure from Meereen astride the dragon Drogon; Tyrion's passage through the ruins of Valyria and his encounter with the stone men (greyscale); and the revelation of Jon Snow's true parentage (strongly implied through the 'R + L = J' foreshadowing). The 'Pink Letter' — Ramsay Bolton's letter to Jon claiming victory at Winterfell — precipitates Jon's decisive action and his subsequent assassination.\n\nA Dance with Dragons sold over 170,000 copies in its first day of publication and debuted at #1 on the New York Times bestseller list — the commercial peak of A Song of Ice and Fire before the HBO series (Game of Thrones, 2011–2019) generated even larger readership. As of 2025, the sixth volume (The Winds of Winter) remains unpublished, making A Dance with Dragons the last completed novel in the series.",
    "causes": [
      "The narrative split between A Feast for Crows and A Dance with Dragons — necessitated by the manuscript's massive size — created the structural complexity of the fifth volume: Martin had to cover the parallel timeline of the 'Crows' characters before extending the narrative beyond them, creating a novel with an unusually complex temporal architecture.",
      "Martin's increasing narrative ambition — the expansion of the world of Westeros and Essos, the multiplication of point-of-view characters (over 30 by the fifth volume), and the complexity of the political and military plots — drove the length and complexity of A Dance with Dragons, contributing to the six-year publication gap.",
      "The HBO series' commissioning and development (Game of Thrones premiered April 2011, shortly before A Dance with Dragons' publication in July 2011) created immense commercial pressure on Martin to complete the novel — the convergence of the TV series and the novel created the largest readership in the series' history."
    ],
    "effects": [
      "A Dance with Dragons' six-year publication gap — the longest in the series — established the pattern of extended delays that has continued with The Winds of Winter (announced as forthcoming since 2011, still unpublished as of 2025), making the question of the series' completion one of the most discussed topics in contemporary popular fiction.",
      "The Jon Snow assassination cliffhanger — and its resolution in the HBO series (Jon's resurrection in Season 6) before Martin published the book equivalent — demonstrated the television adaptation's ability to 'spoil' the novels, reversing the traditional relationship between source text and adaptation.",
      "A Dance with Dragons' strong foreshadowing of Jon Snow's true parentage ('R + L = J', the Tower of Joy flashback in Bran's chapters, the 'promise me, Ned' hint) became the foundation of the most widely discussed fan theory in contemporary popular fiction, demonstrating the series' capacity to generate sustained engagement through embedded narrative puzzles."
    ],
    "relationships": [
      {"sourceSlug": "george-r-r-martin", "sourceName": "George R. R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-dance-with-dragons", "targetName": "A Dance with Dragons (2011)", "context": "Martin published A Dance with Dragons in 2011 — six years after A Feast for Crows — the fifth and currently last completed volume of A Song of Ice and Fire, covering the parallel timeline of the Jon/Daenerys/Tyrion storylines."},
      {"sourceSlug": "a-dance-with-dragons", "sourceName": "A Dance with Dragons (Jon Snow, Daenerys, Tyrion)", "verb": "PART_OF", "targetSlug": "a-song-of-ice-and-fire", "targetName": "A Song of Ice and Fire (Martin series, 1996–)", "context": "A Dance with Dragons is the fifth volume of A Song of Ice and Fire — the last completed novel in the series, covering the Jon Snow, Daenerys, and Tyrion storylines running parallel to and beyond A Feast for Crows."},
      {"sourceSlug": "a-dance-with-dragons", "sourceName": "A Dance with Dragons (Jon Snow assassination)", "verb": "ADAPTED_IN", "targetSlug": "game-of-thrones-season-5-6", "targetName": "Game of Thrones Seasons 5–6 (HBO, 2015–2016)", "context": "The Jon Snow assassination cliffhanger was adapted in Game of Thrones Season 5, and his resurrection in Season 6 — before Martin published the equivalent in The Winds of Winter — reversed the traditional source/adaptation relationship."}
    ],
    "places": [
      {"name": "The Wall and beyond (Jon Snow, Night's Watch, wildlings)", "role": "The Wall and Castle Black are the primary location of Jon Snow's storyline in A Dance with Dragons — his decisions to admit the wildlings and his subsequent assassination are the most consequential events at the Wall"},
      {"name": "Meereen, Essos (Daenerys's troubled rule, dragons)", "role": "Meereen — the Essosi city Daenerys rules as Queen — is the primary location of her storyline in A Dance with Dragons: her struggle to rule and control her dragons culminates in her departure on Drogon's back"}
    ],
    "subjects": ["Fantasy Fiction", "Modern Era", "George R. R. Martin", "Epic Fantasy", "21st Century", "American Literature", "Television Adaptation", "Series Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Dance with Dragons (Martin, 2011) is the fifth and currently last completed volume of A Song of Ice and Fire — selling over 170,000 copies on day one and debuting at #1 on the NYT bestseller list. Its Jon Snow assassination cliffhanger and Jon Snow parentage foreshadowing ('R+L=J') generated some of the most widely discussed fan theories in popular fiction. The ongoing non-publication of The Winds of Winter makes A Dance with Dragons the final word in the primary source of one of the most influential fantasy series of the modern era.",
      "significanceCategory": "significant"
    }
  }
},

"caduceus": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784caduceus.json",
  "slug": "caduceus",
  "data": {
    "summary": "The caduceus (Greek: κηρύκειον, kerykeion, 'herald's staff') is the staff of the Greek god Hermes (Roman: Mercury) — a winged staff entwined by two serpents, one of the most ancient and widely recognised symbols in the world, associated in classical antiquity with heralds, messengers, commerce, travel, and eloquence. The caduceus appears in Greek and Roman art as the primary attribute of Hermes/Mercury — the messenger of the gods, patron of travellers, merchants, thieves, and orators — and is depicted in ancient art from the 7th century BCE onwards. The original Greek kerykeion was a herald's staff (without serpents), but by the Hellenistic period the form with two intertwined serpents was established, and this double-serpent form is what has been transmitted as the 'caduceus' in Western iconographic tradition.\n\nThe caduceus is frequently confused with the Rod of Asclepius — the staff of the Greek god of medicine, Asclepius (Aesculapius), which has a single serpent and no wings — which is the correct symbol of medicine and healing. The confusion arose from the widespread adoption of the caduceus (Hermes/Mercury's staff) by the United States Army Medical Corps in 1902, based on a misidentification of the two symbols, and its subsequent use by many American medical organisations. Most international medical organisations and the World Health Organization use the correct symbol: the Rod of Asclepius with a single serpent. The distinction between the caduceus (two serpents, wings, Hermes/commerce) and the Rod of Asclepius (one serpent, no wings, medicine) is a persistent source of confusion in medical symbolism.\n\nThe caduceus's symbolic range in antiquity — encompassing diplomacy, commerce, communication, negotiation, and the guidance of souls to the underworld (Hermes as psychopomp) — reflects the multifaceted nature of the Hermes/Mercury divine function. In Renaissance and early modern European iconography, the caduceus was a standard symbol of eloquence, peace, and commerce — appearing in the iconography of diplomacy, trade guilds, and learned societies.",
    "causes": [
      "The Greek divine function of Hermes as herald, messenger, and patron of commerce and communication — his role as the divine intermediary between gods and humans, between the living and the dead, and between different human communities — determined the caduceus's symbolic range: a herald's staff, a symbol of safe passage and diplomatic immunity, and an emblem of the commercial and communicative activities Hermes patronises.",
      "The ancient Near Eastern precedent for divine staff symbolism — the entwined-serpent staff appears in Mesopotamian iconography (the caduceus-like symbol of the Sumerian god Ningishzida, c. 2100 BCE) and in the Egyptian tradition — suggests that the Greek caduceus developed in dialogue with Near Eastern divine iconography, though the precise transmission is uncertain.",
      "The Roman adoption and elaboration of the caduceus as Mercury's primary attribute — and its widespread dissemination through Roman art, architecture, and coinage across the Roman Empire — created the iconographic tradition through which the caduceus was transmitted to medieval and Renaissance European iconography."
    ],
    "effects": [
      "The caduceus's adoption as the symbol of the US Army Medical Corps (1902) — and its subsequent use by many American medical organisations — created the persistent confusion between the caduceus (Hermes, commerce) and the Rod of Asclepius (medicine) in American medical symbolism: a confusion that is frequently cited in medical humanities and history of medicine discussions.",
      "The caduceus's role in Renaissance iconography as a symbol of eloquence, peace, diplomacy, and commerce — its appearance in the iconographic programmes of European royal courts, trade guilds, and learned academies — reflects the humanist reinterpretation of ancient divine attributes as allegorical symbols of civic and commercial virtue.",
      "The caduceus's adoption as a symbol in contemporary commercial and communicative contexts — its appearance in the logos of media, pharmaceutical, and financial companies — demonstrates the extraordinary longevity of ancient Greco-Roman divine symbolism in modern commercial iconography, mediated through Renaissance and early modern artistic traditions."
    ],
    "relationships": [
      {"sourceSlug": "caduceus", "sourceName": "Caduceus (kerykeion, Hermes/Mercury staff)", "verb": "ATTRIBUTE_OF", "targetSlug": "hermes", "targetName": "Hermes/Mercury (Greek/Roman messenger god)", "context": "The caduceus is the primary attribute of Hermes (Mercury) in Greek and Roman art — a herald's staff with two entwined serpents and wings, associated with diplomacy, commerce, communication, and the guidance of souls."},
      {"sourceSlug": "caduceus", "sourceName": "Caduceus (US Army Medical Corps confusion)", "verb": "CONFUSED_WITH", "targetSlug": "rod-of-asclepius", "targetName": "Rod of Asclepius (single serpent, correct medical symbol)", "context": "The caduceus is frequently confused with the Rod of Asclepius in American medical symbolism — the US Army Medical Corps adopted the caduceus (Hermes, commerce) in 1902 by mistake, while the correct symbol of medicine is the single-serpent Rod of Asclepius."},
      {"sourceSlug": "caduceus", "sourceName": "Caduceus (Renaissance iconography, eloquence)", "verb": "SYMBOLISES", "targetSlug": "renaissance-humanism", "targetName": "Renaissance humanism (eloquence, commerce, diplomacy)", "context": "In Renaissance iconography, the caduceus was reinterpreted as a symbol of eloquence, peace, and commerce — appearing in the iconographic programmes of European courts, trade guilds, and humanist learned academies."}
    ],
    "places": [
      {"name": "Ancient Greece and Rome (origin, Hermes/Mercury cult, 7th century BCE onwards)", "role": "The caduceus originated in the ancient Greek cult of Hermes and was widely depicted in Greek art from the 7th century BCE — transmitted through Roman adoption of Mercury as the caduceus-carrying messenger god to the entire Mediterranean world"},
      {"name": "United States (Army Medical Corps, 1902, caduceus/Asclepius confusion)", "role": "The US adoption of the caduceus as a medical symbol (1902) by the Army Medical Corps created the widespread American medical use of the caduceus — in contrast to international medical organisations that correctly use the Rod of Asclepius"}
    ],
    "subjects": ["Classical Mythology", "Ancient Era", "Greek Art", "Medical Symbolism", "Roman Art", "Hermes", "Iconography", "Symbol History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The caduceus — Hermes/Mercury's winged staff entwined by two serpents — is one of the most ancient and widely recognised symbols in the world, with a continuous iconographic tradition from 7th-century BCE Greece to the present. Its adoption as a medical symbol in the United States (1902, by confusion with the Rod of Asclepius) created a persistent misuse that reflects the complex transmission of ancient symbolic traditions. Its Renaissance reinterpretation as a symbol of eloquence and commerce influenced European iconographic traditions.",
      "significanceCategory": "significant"
    }
  }
},

"minimal-group-paradigm": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785minimal-group-paradigm.json",
  "slug": "minimal-group-paradigm",
  "data": {
    "summary": "The minimal group paradigm (MGP) is an experimental methodology in social psychology developed by Henri Tajfel (1919–1982) and his colleagues at the University of Bristol in the late 1960s and early 1970s — a controlled experimental design for studying intergroup discrimination by creating artificial groups (minimal groups) based on arbitrary, trivial, or explicitly meaningless criteria, then measuring the extent to which group membership alone (without any history of conflict, competition, or social interaction between groups) leads to ingroup favouritism and outgroup discrimination. Tajfel's foundational experiment (1971), in which schoolboys were assigned to groups ostensibly based on whether they preferred the paintings of Klee or Kandinsky (but actually randomly), showed that group members consistently allocated more resources to members of their own group than to members of the other group — even at personal cost — simply on the basis of group membership, with no prior conflict, no personal interest in maximising ingroup gains, and no social interaction between group members.\n\nThe minimal group paradigm results were the empirical foundation for Social Identity Theory (SIT), developed by Henri Tajfel and John Turner — the theory that individuals derive part of their self-concept from their membership in social groups, and that the motivation to maintain a positive social identity (by favourably comparing the ingroup with outgroups) is a fundamental driver of intergroup behaviour. Social Identity Theory, developed from the minimal group paradigm results, became one of the most influential theories in social psychology, with applications to the understanding of prejudice, discrimination, stereotyping, collective behaviour, political psychology, and organisational behaviour.\n\nThe minimal group paradigm's demonstration that trivial, arbitrary group membership is sufficient to produce intergroup discrimination challenged earlier theories that required realistic conflict of interest (Sherif's Realistic Conflict Theory, based on the Robbers Cave experiments, 1954) or authoritarian personality structures (Adorno's Authoritarian Personality, 1950) to explain prejudice and discrimination. The MGP results suggest that intergroup discrimination is a fundamental feature of human social cognition — triggered by the mere categorisation of people into groups — with profound implications for the social psychology of prejudice, nationalism, racism, and ethnocentrism.",
    "causes": [
      "Tajfel's personal experience as a Jewish Holocaust survivor — his first-hand knowledge of the catastrophic consequences of extreme ethnic prejudice and his conviction that social psychology had a moral obligation to understand the roots of intergroup discrimination — motivated his programme of research on the psychological basis of prejudice, which culminated in the minimal group paradigm.",
      "The inadequacy of existing theories of intergroup discrimination — Sherif's Realistic Conflict Theory, Adorno's Authoritarian Personality — for explaining the ordinary, everyday phenomenon of ingroup favouritism motivated Tajfel's search for the minimal conditions sufficient to produce discrimination: the minimal group paradigm was designed to strip away all confounding factors to reveal the bare psychological mechanism.",
      "The Bristol social psychology group's theoretical and experimental tradition — Tajfel's colleagues John Turner, Michael Billig, and others who contributed to the development of Social Identity Theory — created the institutional and intellectual context for the development of the minimal group paradigm from an experimental curiosity into a full theoretical framework."
    ],
    "effects": [
      "Social Identity Theory (Tajfel and Turner, 1979, 1986) — developed from the minimal group paradigm — became one of the most influential and widely applied theories in social psychology, used to explain prejudice, discrimination, stereotyping, collective behaviour, social movements, organisational behaviour, national and ethnic identity, and political psychology.",
      "The minimal group paradigm's demonstration that arbitrary categorisation alone is sufficient to produce discrimination challenged the assumption that prejudice requires realistic conflict or pathological personality structures, shifting the theoretical focus toward the cognitive and motivational processes of social categorisation and self-esteem maintenance.",
      "The minimal group paradigm's methodological influence extended throughout experimental social psychology — its paradigm design (creating minimal groups and measuring resource allocation) became a standard experimental tool for studying intergroup relations, and its replication across cultures, ages, and contexts demonstrated the robustness of the ingroup favouritism effect."
    ],
    "relationships": [
      {"sourceSlug": "minimal-group-paradigm", "sourceName": "Minimal group paradigm (Tajfel et al., 1971)", "verb": "DEVELOPED_BY", "targetSlug": "henri-tajfel", "targetName": "Henri Tajfel (1919–1982, University of Bristol)", "context": "Tajfel and his colleagues at the University of Bristol developed the minimal group paradigm in the late 1960s–early 1970s — the foundational experimental result showing that arbitrary group membership alone produces intergroup discrimination."},
      {"sourceSlug": "minimal-group-paradigm", "sourceName": "Minimal group paradigm (SIT foundation)", "verb": "PRODUCES", "targetSlug": "social-identity-theory", "targetName": "Social Identity Theory (Tajfel and Turner, 1979)", "context": "The minimal group paradigm results were the empirical foundation for Social Identity Theory — one of the most influential theories in social psychology, explaining intergroup behaviour through social identity, social categorisation, and social comparison."},
      {"sourceSlug": "minimal-group-paradigm", "sourceName": "Minimal group paradigm (Realistic Conflict Theory challenge)", "verb": "CHALLENGES", "targetSlug": "realistic-conflict-theory", "targetName": "Realistic Conflict Theory (Sherif, Robbers Cave, 1954)", "context": "The minimal group paradigm challenged Realistic Conflict Theory — showing that intergroup discrimination does not require realistic conflict of interest, as even arbitrary group membership (without conflict) produces ingroup favouritism."}
    ],
    "places": [
      {"name": "University of Bristol, UK (Tajfel's laboratory, late 1960s–1970s)", "role": "The University of Bristol was the institutional context for the development of the minimal group paradigm — Tajfel's laboratory at Bristol produced the foundational experimental results and the subsequent development of Social Identity Theory"},
      {"name": "Global (replicated across cultures, ages, and contexts)", "role": "The minimal group paradigm has been replicated across cultures, ages, and contexts worldwide — demonstrating the robustness of the ingroup favouritism effect and establishing it as a foundational result of cross-cultural social psychology"}
    ],
    "subjects": ["Social Psychology", "Modern Era", "Henri Tajfel", "Prejudice", "Intergroup Relations", "Social Identity Theory", "Experimental Psychology", "Discrimination"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The minimal group paradigm (Tajfel et al., 1971) is one of the most influential experimental results in social psychology — demonstrating that arbitrary group membership alone produces intergroup discrimination, challenging all prior theories that required realistic conflict or pathological personality. It was the empirical foundation for Social Identity Theory (Tajfel and Turner), which became one of the most widely applied theoretical frameworks in social psychology. Its implications for understanding prejudice, nationalism, and ethnocentrism make it one of the most consequential social psychological discoveries.",
      "significanceCategory": "highly-significant"
    }
  }
},

"manifest-der-kommunistischen-partei": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785manifest-der-kommunistischen-partei.json",
  "slug": "manifest-der-kommunistischen-partei",
  "data": {
    "summary": "Das Manifest der Kommunistischen Partei (The Manifesto of the Communist Party) — known in English as The Communist Manifesto — is the original German-language political pamphlet by Karl Marx (1818–1883) and Friedrich Engels (1820–1895), first published in London on 21 February 1848 by the Workers' Educational Association, commissioned by the Communist League (a radical German emigrant organisation) as a programmatic statement of its aims and principles. The Manifest is approximately 12,000 words long and is structured in four sections: (1) 'Bourgeois and Proletarians' — the materialist theory of history (historical materialism) presenting all history as the history of class struggle; (2) 'Proletarians and Communists' — the programme and aims of the communist movement; (3) 'Socialist and Communist Literature' — a critique of rival socialist traditions; and (4) 'Position of the Communists in Relation to the Various Existing Opposition Parties'. The pamphlet concludes with the famous declaration: 'Die Proletarier haben nichts in ihr zu verlieren als ihre Ketten. Sie haben eine Welt zu gewinnen. Proletarier aller Länder, vereinigt euch!' ('The proletarians have nothing to lose but their chains. They have a world to win. Workers of all countries, unite!').\n\nThe Manifest was one of the most influential political texts of the 19th and 20th centuries — its materialist theory of history, its analysis of capitalism and class conflict, and its call for proletarian revolution provided the theoretical framework for socialist and communist movements worldwide. Published originally in German for a German-speaking audience, it was translated into English (1850, by Helen Macfarlane, anonymously) and subsequently into dozens of languages, and re-editions and translations proliferated after the Paris Commune (1871) and the formation of the First and Second Internationals. By the early 20th century, the Communist Manifesto had been translated into virtually every major world language.\n\nThe Manifest der Kommunistischen Partei is catalogued in the Annals of the World as the German-language original — the primary source document of the global communist movement — distinct from the English Communist Manifesto entry (which covers the reception history primarily through English translation). The German original's specific intellectual and political context — the 1848 revolutions, the German workers' movement, the Communist League — and its precise original language (in which concepts like Proletariat, Bourgeoisie, and Klassenkampf carry their original force) distinguish it as a separate historical document.",
    "causes": [
      "The Communist League's commission of a programmatic statement — the League's Second Congress in London (November–December 1847) commissioned Marx and Engels to write a comprehensive statement of communist principles — provided the immediate context and authorial mandate for the Manifest: it was a political document written to order, not a spontaneous theoretical work.",
      "The revolutionary situation of Europe in 1847–1848 — the economic crisis (the hungry 1840s), the political frustrations of the German bourgeoisie and workers, and the imminent revolutionary upheaval (the Revolutions of 1848 began in France in February 1848, almost simultaneously with the Manifest's publication) — shaped the Manifest's urgent, revolutionary tone and its vision of imminent proletarian revolution.",
      "Marx's theoretical development in the period 1843–1847 — his work on the materialist conception of history (The German Ideology, written with Engels 1845–46, published only in 1932) and his economic analysis (Wages, Price and Profit; Poverty of Philosophy) — provided the theoretical foundation for the Manifest's compact and powerful statement of historical materialism and class conflict."
    ],
    "effects": [
      "The Communist Manifesto's theoretical framework — historical materialism, the theory of class conflict, the analysis of capitalism, the call for proletarian revolution — became the foundational theoretical and political document of the international socialist and communist movements, shaping the politics of the First International (1864), the Second International (1889), the Russian Revolution (1917), and the international communist movements of the 20th century.",
      "The Manifest's translation history — into virtually every major world language, with hundreds of editions produced across the 19th and 20th centuries — is one of the most remarkable examples of political text diffusion in history: from a 12,000-word pamphlet for German emigrant workers in London to a text that shaped the political programmes of states governing more than one-third of the world's population.",
      "The opening sentence of the Manifest — 'Ein Gespenst geht um in Europa — das Gespenst des Kommunismus' ('A spectre is haunting Europe — the spectre of communism') — became one of the most famous opening sentences in political literature, demonstrating Marx and Engels's literary power as political writers alongside their theoretical influence."
    ],
    "relationships": [
      {"sourceSlug": "manifest-der-kommunistischen-partei", "sourceName": "Manifest der Kommunistischen Partei (1848 German original)", "verb": "AUTHORED_BY", "targetSlug": "karl-marx", "targetName": "Karl Marx (1818–1883) and Friedrich Engels (1820–1895)", "context": "Marx and Engels wrote the Manifest at the commission of the Communist League in 1847–1848 — the original German-language text is the primary source document of the global communist movement, translated into virtually every major world language."},
      {"sourceSlug": "manifest-der-kommunistischen-partei", "sourceName": "Manifest (historical materialism, class conflict)", "verb": "ESTABLISHES", "targetSlug": "marxism", "targetName": "Marxism (historical materialism, communist theory)", "context": "The Manifest's compact statement of historical materialism — all history as class struggle — and the call for proletarian revolution established the theoretical foundation of Marxism and the international socialist and communist movements."},
      {"sourceSlug": "manifest-der-kommunistischen-partei", "sourceName": "Manifest (1848 German original)", "verb": "RELATED_TO", "targetSlug": "communist-manifesto", "targetName": "Communist Manifesto (English reception and translation history)", "context": "The Manifest der Kommunistischen Partei is the German original of the Communist Manifesto — the Annals catalogues both the German original and the English translation/reception history as related but distinct entities."}
    ],
    "places": [
      {"name": "London (Workers' Educational Association, first publication 21 February 1848)", "role": "The Manifest was first published in London on 21 February 1848 — by the Workers' Educational Association for the German Communist League — one week before the February Revolution in Paris that began the Revolutions of 1848"},
      {"name": "Europe and the world (1848 revolutions, First/Second Internationals, 20th century communist states)", "role": "The Manifest's rapid translation and diffusion across Europe — in the context of the 1848 revolutions and the First International (1864) — made it a global political document shaping communist movements worldwide"}
    ],
    "subjects": ["Political Philosophy", "Modern Era", "Karl Marx", "Friedrich Engels", "Communism", "Socialism", "Marxism", "Political Pamphlet"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Manifest der Kommunistischen Partei (Marx and Engels, 1848) is the German-language original of one of the most influential political texts in world history — the founding document of the international communist movement, whose theoretical framework shaped the politics of states governing more than a third of the world's population in the 20th century. Its compact statement of historical materialism and class conflict, its translation into virtually every world language, and its role in the Revolutions of 1848 and subsequent revolutionary politics make it a text of world-historical significance.",
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
