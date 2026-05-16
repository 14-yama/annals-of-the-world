#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 50 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: jtaka (Jataka Tales), landnmabk (Landnámabók), manysh (Man'yōshū),
          rubiyt-of-omar-khayym (Rubáiyát), the-shepherd-of-hermas,
          te-deum, terminologia-anatomica, parkinsons-law

NOTE: Several entities have Unicode filenames but ASCII-stripped slugs.
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-50-may2026"

ENRICHMENTS = {

"jtaka": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780jātaka.json",
  "slug": "jtaka",
  "data": {
    "summary": "The Jātakas (Pali: Jātaka, Sanskrit: Jātaka, 'birth story') are a collection of 547 canonical Buddhist stories narrating the previous lives of Gautama Buddha, preserved as part of the Pali Canon (Khuddaka Nikāya, 'Minor Collection') and constituting one of the oldest surviving bodies of narrative literature in the world, with the earliest strata (the Jātaka verses) dated c. 3rd century BCE and the prose commentary (Jātakatthavannanā) compiled c. 5th century CE. Each Jātaka tells the story of one of the Buddha's past lives — as a human, an animal, or a spirit — in which the Bodhisatta (the being destined to become Buddha) exemplifies one of the ten perfections (pāramitā: generosity, virtue, renunciation, wisdom, energy, patience, truth, resolution, loving-kindness, equanimity) required for eventual Buddhahood.\n\nThe Jātakas are the most narratively diverse and imaginatively rich body of literature in the Pali Canon — they include fables, folk tales, romance narratives, adventure stories, didactic tales, and satire, many of which have parallels in the Panchatantra, Aesop's Fables, and the Arabian Nights tradition. The most famous include the Vesantara Jātaka (the Bodhisatta gives away everything including his children — the supreme example of dāna, generosity), the Saddanta Jātaka (the six-tusked elephant), the Mahosadha Jātaka, and the Nimi Jātaka. As narratives of the Bodhisatta's progressive moral development across hundreds of lives, they constitute the world's earliest and most extensive narrative exploration of moral psychology and the gradual cultivation of virtue.\n\nThe Jātakas had an extraordinary diffusion across Asian Buddhist cultures — they were translated into Sanskrit, Chinese, Tibetan, Sinhalese, Thai, Burmese, Khmer, and Javanese, and their stories became the basis of Buddhist art across South and Southeast Asia (the Sanchi and Ajanta cave paintings, the Borobudur reliefs), demonstrating the narrative power that made Buddhism the first truly pan-Asian religion.",
    "causes": [
      "The Theravāda Buddhist tradition's need for a narrative account of the Bodhisatta's gradual moral development — the Jātakas provided the narrative evidence for the doctrine that the historical Buddha had spent hundreds of past lives cultivating the perfections required for Buddhahood — created the demand for a comprehensive collection of birth stories.",
      "The Indian oral narrative tradition's extraordinary richness — the vast store of folk tales, fables, and didactic stories circulating in oral tradition in ancient India — provided the narrative materials that Buddhist compilers adapted and incorporated into the Jātaka collection, giving Buddhist teaching access to the widest range of narrative genres.",
      "The Buddhist missionary tradition's use of narrative as pedagogy — the teaching that complicated doctrinal points could be made concrete and memorable through story — drove the development of the Jātaka collection as a primary tool of Buddhist popular education, making narrative the vehicle for the transmission of Buddhist ethics."
    ],
    "effects": [
      "The Jātakas had an enormous influence on Asian Buddhist art — the stories of the Bodhisatta's previous lives were depicted in stone reliefs at Sanchi (2nd–1st century BCE), the Ajanta cave paintings (5th–6th century CE), the Borobudur reliefs (Java, 9th century CE), and temple art across Southeast Asia — making them the primary iconographic source for Buddhist visual culture.",
      "The Jātaka stories became a primary channel for the diffusion of Indian narrative traditions across Asia — their tales of talking animals, clever heroes, and moral tests were adapted into Sinhalese, Thai, Burmese, Khmer, and Javanese literature, contributing to the formation of national literary traditions across Buddhist Asia.",
      "Many Jātaka stories have parallels in the Western fable tradition (Aesop) and the Panchatantra/Arabian Nights narrative complex — though the direction of influence is debated, the parallels demonstrate the antiquity and diffusion of a shared Indo-European narrative stock that the Jātakas preserved and elaborated."
    ],
    "relationships": [
      {"sourceSlug": "jtaka", "sourceName": "Jātaka Tales (547 birth stories, Pali Canon, c. 3rd century BCE–5th century CE)", "verb": "PART_OF", "targetSlug": "pali-canon", "targetName": "Pali Canon (Theravāda Buddhist scriptures — Tipiṭaka)", "context": "The Jātakas form part of the Khuddaka Nikāya ('Minor Collection') of the Pali Canon — the earliest Jātaka verses are among the oldest texts in the Canon, with the prose commentary compiled c. 5th century CE."},
      {"sourceSlug": "jtaka", "sourceName": "Jātaka Tales (Sanchi, Ajanta, Borobudur — Buddhist art iconography)", "verb": "SOURCE_OF", "targetSlug": "buddhist-art", "targetName": "Buddhist art across Asia (Sanchi, Ajanta, Borobudur, Southeast Asian temple art)", "context": "The Jātaka stories were depicted in stone reliefs at Sanchi (2nd–1st century BCE) and Borobudur (9th century CE) and in the Ajanta cave paintings — making them the primary iconographic source for Buddhist visual culture across Asia."},
      {"sourceSlug": "jtaka", "sourceName": "Jātaka Tales (talking animals, moral fables — Aesop, Panchatantra parallels)", "verb": "SHARES_NARRATIVE_STOCK_WITH", "targetSlug": "aesops-fables", "targetName": "Aesop's Fables (and Panchatantra — shared Indo-European narrative tradition)", "context": "Many Jātaka stories have parallels in Aesop's Fables and the Panchatantra — the parallels demonstrate the antiquity of a shared narrative stock that the Jātakas preserved and elaborated for Buddhist pedagogical purposes."}
    ],
    "places": [
      {"name": "Ancient India and Sri Lanka (composition c. 3rd century BCE; Theravāda Buddhist tradition)", "role": "The Jātaka verses were compiled in ancient India and Sri Lanka c. 3rd century BCE — the prose commentary was compiled in Sri Lanka c. 5th century CE by Dhammapāla"},
      {"name": "Buddhist Asia (Sanchi, Ajanta, Borobudur; Thailand, Burma, Cambodia, Bali — narrative diffusion)", "role": "The Jātakas were diffused across Buddhist Asia in translation and adaptation — depicted in temple art from India (Sanchi, Ajanta) through Java (Borobudur) to Southeast Asia (Thailand, Burma, Cambodia)"}
    ],
    "subjects": ["Pali Literature", "Ancient Era", "Buddhist Scripture", "Birth Stories", "Fables", "Bodhisatta", "Buddhist Art", "Indian Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Jātakas (c. 3rd century BCE–5th century CE) are the world's earliest and most extensive collection of narrative birth stories — 547 tales of the Bodhisatta's previous lives that provided the iconographic source for Buddhist art across Asia (Sanchi, Ajanta, Borobudur) and the primary vehicle for Buddhist narrative pedagogy. Their diffusion across Buddhist Asia in translation contributed to the formation of national literary traditions from Sri Lanka to Java.",
      "significanceCategory": "world-changing"
    }
  }
},

"landnmabk": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780landnámabók.json",
  "slug": "landnmabk",
  "data": {
    "summary": "The Landnámabók (Old Norse: 'Book of Settlements', or 'Land-Taking Book') is a medieval Icelandic prose work recording the settlement of Iceland in the late 9th and early 10th centuries (c. 874–930 CE), compiled in its first form c. 12th century CE and surviving in five primary redactions (Sturlubók, Hauksbók, Melabók, Þórðarbók, and Skarðsárbok), the earliest surviving redaction dating to the 13th century. It is the most detailed account of any medieval colonisation in world literature — providing the names, genealogies, land claims, and anecdotes of approximately 400 settlers (settlers of land-taking level) and their 3,000 associates, covering the entire coastline of Iceland.\n\nThe Landnámabók is the primary source for Icelandic medieval history and the founding document of Icelandic genealogical tradition — the Icelanders' claim to know their ancestry in exhaustive detail begins with this text, and its genealogies connect virtually every major Icelandic saga character to the original settlers. It served as a legal record of land claims (the land boundaries and ownership described in the Landnámabók were legally operative in the medieval period), as a genealogical register (allowing Icelanders to establish their descent from the settlers), and as a mythological and heroic account (many entries include anecdotes of the settlers' encounters with pagan gods, land spirits, and Norse mythological figures).\n\nThe Landnámabók provides evidence for one of the most remarkable political experiments in medieval history — the Icelandic Commonwealth (930–1262 CE), a stateless society governed by the Althing (the world's oldest surviving parliament, established 930 CE), without a king and with an elaborate system of chieftaincy (goðorð) that governed disputes through a combination of law, arbitration, and the threat of feud. The settlement accounts in the Landnámabók are the foundation for understanding this unique political experiment.",
    "causes": [
      "The Norwegian settlement of Iceland (c. 874–930 CE) — motivated primarily by the flight of Norwegian chieftains from Harald Fairhair's consolidation of Norway into a unified kingdom and their desire for land and autonomy — created the historical events that the Landnámabók records, providing the specific occasion for the compilation of the settlement accounts.",
      "The Icelandic legal and genealogical tradition — the practical need to establish land boundaries and ownership claims through reference to the original settlers' land-takings, and the social importance of genealogy in establishing status and descent in a society without a hereditary nobility — drove the compilation of the Landnámabók as a practical legal and genealogical reference.",
      "The 12th–13th century Icelandic literary renaissance — the extraordinary flowering of saga writing and historical scholarship in Iceland that produced the Prose Edda (Snorri Sturluson), the Kings' Sagas (Heimskringla), the Family Sagas, and the historical compilations — provided the intellectual context for the Landnámabók's composition."
    ],
    "effects": [
      "The Landnámabók is the most detailed record of any medieval colonisation in world literature — its account of approximately 400 settler families, their land claims, genealogies, and anecdotes provides a uniquely granular window into the process of medieval Scandinavian settlement that is unparalleled in any other medieval source.",
      "The Landnámabók's genealogical tradition established the basis for Icelandic family sagas — the major Íslendingasögur (Family Sagas: Njáls saga, Egils saga, Laxdæla saga, Grettis saga) presuppose the genealogical knowledge codified in the Landnámabók and use the settler-descendants as their protagonists.",
      "Modern Icelandic genealogical culture — Iceland's extraordinary genealogical consciousness (virtually all Icelanders can trace their ancestry to the original settlers) and the Íslendingabók online genealogy database (covering all 330,000 Icelanders) descend directly from the tradition established by the Landnámabók."
    ],
    "relationships": [
      {"sourceSlug": "landnmabk", "sourceName": "Landnámabók ('Book of Settlements', c. 12th century CE, 5 redactions)", "verb": "RECORDS", "targetSlug": "icelandic-settlement", "targetName": "Settlement of Iceland (c. 874–930 CE — approximately 400 settler families)", "context": "The Landnámabók is the primary source for the settlement of Iceland — recording approximately 400 settler families and 3,000 associates, covering the entire coastline and providing the foundation for Icelandic genealogical tradition."},
      {"sourceSlug": "landnmabk", "sourceName": "Landnámabók (genealogical foundation for Íslendingasögur — Family Sagas)", "verb": "FOUNDATIONAL_TO", "targetSlug": "icelandic-family-sagas", "targetName": "Icelandic Family Sagas (Íslendingasögur — Njáls saga, Egils saga, Laxdæla saga)", "context": "The Landnámabók's genealogies established the foundation for the Icelandic Family Sagas — the major Íslendingasögur presuppose the genealogical knowledge codified in the Landnámabók and use settler-descendants as their protagonists."},
      {"sourceSlug": "landnmabk", "sourceName": "Landnámabók (Icelandic Commonwealth — Althing, stateless society)", "verb": "CONTEXTUALISES", "targetSlug": "icelandic-commonwealth", "targetName": "Icelandic Commonwealth (930–1262 CE — Althing, world's oldest parliament)", "context": "The Landnámabók provides the settlement context for understanding the Icelandic Commonwealth — the stateless society governed by the Althing (established 930 CE, the world's oldest surviving parliament) that emerged from the original settler families."}
    ],
    "places": [
      {"name": "Iceland (settlement c. 874–930 CE; entire coastline and interior — land claims documented)", "role": "The Landnámabók covers the entire Icelandic coastline and interior — documenting the land claims of approximately 400 settler families from the initial settlement (Ingólfr Arnarson, c. 874 CE) through the completion of the land-taking (c. 930 CE)"},
      {"name": "Norway (Harald Fairhair's consolidation — motivation for settlement; Norwegian/Celtic settlers)", "role": "Most Icelandic settlers came from western Norway, fleeing Harald Fairhair's consolidation of Norway — the Landnámabók records their Norwegian and, in some cases, Celtic (Hiberno-Norse) origins"}
    ],
    "subjects": ["Old Norse Literature", "Medieval Era", "Icelandic Sagas", "Settlement History", "Genealogy", "Viking Age", "Norse Culture", "Medieval History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Landnámabók (c. 12th century CE) is the most detailed record of any medieval colonisation in world literature — documenting approximately 400 settler families and providing the genealogical foundation for Icelandic Family Sagas. Its accounts contextualise the Icelandic Commonwealth (930–1262 CE) — one of the most remarkable political experiments of the medieval period — and establish the basis for Iceland's extraordinary genealogical culture.",
      "significanceCategory": "highly-significant"
    }
  }
},

"manysh": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780manyōshū.json",
  "slug": "manysh",
  "data": {
    "summary": "The Man'yōshū (Japanese: 万葉集, 'Collection of Ten Thousand Leaves') is the oldest surviving anthology of Japanese poetry, compiled c. 759 CE (during the Nara period, 710–794 CE) and attributed to the compiler Ōtomo no Yakamochi (c. 718–785 CE), though the anthology was assembled over a longer period and includes poems by multiple editors. The Man'yōshū contains approximately 4,516 poems in three main forms — the chōka (long poem), tanka (short poem, 5-7-5-7-7 syllables), and sedōka — composed by poets from the Emperor and court nobles to frontier guards and commoners, spanning approximately 130 years of Japanese literary history (c. 629–759 CE). It is written primarily in Man'yōgana, a system of using Chinese characters to represent Japanese phonetic syllables, predating the development of kana.\n\nThe Man'yōshū is the foundational text of the Japanese literary tradition — its approximately 4,500 poems established the tanka (and its descendant the waka) as the primary form of Japanese poetry, a form that would dominate Japanese literary culture from the Nara period through the modern era. The anthology's aesthetic sensibility — its celebration of the natural world (the seasons, mountains, rivers, birds), its directness and freshness of feeling, its expression of love, separation, and longing — established the aesthetic values (makoto, sincerity; aware, the pathos of things) that would characterise Japanese poetry for centuries.\n\nThe Man'yōshū's cultural significance in modern Japan is extraordinary — it was used by the Meiji Restoration's imperial ideologues as evidence of the Emperor's cultural centrality and the purity of Japanese culture before Chinese influence; and in May 2019 the name of the new imperial era Reiwa (令和, 'beautiful harmony') was taken from the preface to poem 5 in Book 5 of the Man'yōshū ('Under the beautiful harmony of the sky, with a gentle spring breeze, the plum blossoms open like powder before a mirror') — the first imperial era name drawn from a Japanese rather than a Chinese source.",
    "causes": [
      "The Nara court's cultural ambition — the desire of the Japanese court (modelling itself on the Tang Dynasty Chinese imperial court) to demonstrate its cultural achievement through a comprehensive anthology of vernacular poetry — drove the compilation of the Man'yōshū as an expression of Japanese literary civilisation.",
      "The development of Man'yōgana — the phonetic use of Chinese characters to represent Japanese syllables — provided the writing system that made it possible to record Japanese poetry in its native syllabic form rather than in Chinese, though the cumbersome nature of Man'yōgana was one reason for the later development of kana.",
      "The poetic tradition accumulated at court — over 130 years of waka and chōka composition by poets from the Emperor to soldiers — provided the material for the anthology, and Ōtomo no Yakamochi's role as both a major poet and the final compiler gave the Man'yōshū both a personal literary vision and a comprehensive historical scope."
    ],
    "effects": [
      "The Man'yōshū established the tanka (5-7-5-7-7 syllable short poem) as the primary form of Japanese poetry — the 31-syllable tanka, in its later form as waka, dominated Japanese literary culture from the 9th century to the modern era, producing the Kokinshū (905 CE), the Shin Kokinshū (1205 CE), and the entire classical Japanese poetic tradition.",
      "The Man'yōshū's aesthetic values — the directness and freshness of feeling (makoto, sincerity), the celebration of the natural world, and the expression of mono no aware (the pathos of things) — established the foundational aesthetic framework of Japanese literature, influencing poetry, fiction, and aesthetics continuously to the present.",
      "In May 2019 the new imperial era name Reiwa (令和) was drawn from the Man'yōshū's preface — the first era name from a Japanese rather than Chinese source — demonstrating the text's continuing cultural centrality in contemporary Japan and the political significance attached to its antiquity and Japanese authenticity."
    ],
    "relationships": [
      {"sourceSlug": "otomo-no-yakamochi", "sourceName": "Ōtomo no Yakamochi (c. 718–785 CE, Japanese poet and compiler)", "verb": "COMPILES", "targetSlug": "manysh", "targetName": "Man'yōshū (compiled c. 759 CE, c. 4,516 poems, Nara period)", "context": "Ōtomo no Yakamochi compiled the Man'yōshū c. 759 CE — the oldest surviving anthology of Japanese poetry and the foundational text of the Japanese literary tradition."},
      {"sourceSlug": "manysh", "sourceName": "Man'yōshū (tanka, waka — foundational Japanese poetic form)", "verb": "ESTABLISHES", "targetSlug": "japanese-poetic-tradition", "targetName": "Japanese waka/tanka tradition (Kokinshū, Shin Kokinshū — 9th–13th century)", "context": "The Man'yōshū established the tanka (5-7-5-7-7) as the primary Japanese poetic form — the waka tradition it founded produced the Kokinshū (905 CE) and the Shin Kokinshū (1205 CE), dominating Japanese literary culture for a millennium."},
      {"sourceSlug": "manysh", "sourceName": "Man'yōshū (Reiwa era name 2019 — first era from Japanese not Chinese source)", "verb": "SOURCE_OF", "targetSlug": "reiwa-imperial-era", "targetName": "Reiwa imperial era (2019 — Emperor Naruhito's accession)", "context": "The Reiwa imperial era name (2019) was drawn from the Man'yōshū's Book 5 preface — the first era name taken from a Japanese rather than Chinese source, demonstrating the text's continuing cultural centrality."}
    ],
    "places": [
      {"name": "Nara, Japan (Nara court, c. 759 CE — compilation; Tang-influenced court culture)", "role": "The Man'yōshū was compiled at the Nara court c. 759 CE — the court's cultural ambition (modelling itself on Tang China) drove the compilation of a comprehensive national poetry anthology"},
      {"name": "Japan (continuous literary reception — 1,200 years of cultural centrality; Reiwa era 2019)", "role": "The Man'yōshū has been read, studied, and cited in Japan for over 1,200 years — its cultural centrality is demonstrated by the choice of the Reiwa era name from its text in 2019"}
    ],
    "subjects": ["Japanese Literature", "Ancient Era", "Nara Period", "Tanka Poetry", "Waka", "Japanese Poetry Anthology", "Ōtomo no Yakamochi", "Man'yōgana"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Man'yōshū (compiled c. 759 CE) is the oldest surviving anthology of Japanese poetry and the foundational text of the Japanese literary tradition — its 4,516 poems established the tanka as Japan's primary poetic form, its aesthetic values (makoto, aware) shaped Japanese literature for over a millennium, and the choice of the Reiwa era name (2019) from its text demonstrates its continuing cultural centrality.",
      "significanceCategory": "world-changing"
    }
  }
},

"rubiyt-of-omar-khayym": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780rubáiyát-of-omar-khayyám.json",
  "slug": "rubiyt-of-omar-khayym",
  "data": {
    "summary": "The Rubáiyát of Omar Khayyám (Persian: رباعیات عمر خیام) is a collection of quatrains (rubāʿī, pl. rubāʿīyāt) attributed to the Persian polymath Omar Khayyám (c. 1048–1131 CE), composed c. 1100 CE and known in the West primarily through Edward FitzGerald's celebrated English adaptation (The Rubáiyát of Omar Khayyám, 1859), which freely rearranged and rendered approximately 75 of the quatrains into English verse. FitzGerald's Rubáiyát is one of the most widely published English poems of the Victorian era and the most influential English-language poem of the 19th century outside England — its themes of hedonistic carpe diem, scepticism about afterlife, and the consolations of wine and companionship in the face of death resonated with Victorian doubters and became a cult text of the fin-de-siècle.\n\nOmar Khayyám was the pre-eminent Persian mathematician and astronomer of his era — he developed the Jalālī calendar (1079 CE, more accurate than the Gregorian), produced systematic solutions to cubic equations, and made fundamental contributions to algebra. The quatrains attributed to him in Persian manuscripts treat themes of wine, love, the brevity of life, the futility of religious dogma, and the uncertainty of existence in a tone that combines Epicurean hedonism with Sufi mystical imagery and a pessimistic metaphysics. The total corpus of quatrains attributed to Khayyám in Persian manuscripts ranges from approximately 250 to over 2,000 (many attributions are spurious or later additions).\n\nFitzGerald's 1859 translation/adaptation — published anonymously, initially ignored, discovered by Dante Gabriel Rossetti and Algernon Swinburne in a penny box at a London bookseller, and subsequently recognised as a masterpiece — is one of the most remarkable cases of translation as creation in literary history: FitzGerald's English poem has a coherence, beauty, and philosophical consistency that arguably exceeds the original quatrains, even as it departs significantly from literal translation.",
    "causes": [
      "Omar Khayyám's philosophical position — his engagement with Greek philosophy (Avicenna, Aristotle), his scepticism about religious orthodoxy, and his hedonistic response to the uncertainty of existence — provided the intellectual framework for the quatrains' themes of wine, love, and carpe diem in the face of death.",
      "The Persian rubāʿī tradition — the four-line poem with a specific rhyme scheme (AABA, occasionally AAAA) as a vehicle for philosophical and lyrical expression — provided the literary form within which Khayyám composed, and the tradition of attributing philosophical quatrains to learned poets like Khayyám shaped the manuscript corpus.",
      "FitzGerald's encounter with the Persian manuscript tradition (through his friendship with Edward Cowell, who found Khayyám manuscripts at the Bodleian Library and the Asiatic Society Library, Calcutta) and his own Victorian scepticism (responding to the religious uncertainties produced by evolution and biblical criticism) gave his translation its personal intensity and cultural resonance."
    ],
    "effects": [
      "FitzGerald's Rubáiyát became a cult text of Victorian scepticism — its themes of pleasure-seeking in the face of death, its doubt about afterlife, and its hedonistic carpe diem resonated with Victorians whose religious faith had been shaken by Darwinian evolution and biblical criticism, and it became one of the most widely printed and quoted poems of the era.",
      "The Rubáiyát initiated the English-speaking world's fascination with Persian poetry and Islamic civilisation — it preceded and stimulated the broader Orientalist interest in Persian culture (Hafiz, Rumi) and contributed to the Western discovery of Persian literary achievement as a counterweight to classical Greek and Latin culture.",
      "The Rubáiyát's influence on the Arts and Crafts and Aesthetic movements — the Pre-Raphaelites (Rossetti, Burne-Jones), William Morris's Kelmscott Press edition, and the Art Nouveau book arts — made it a central text of 19th-century British aesthetic culture, as lavishly illustrated editions became objects of artistic beauty in themselves."
    ],
    "relationships": [
      {"sourceSlug": "omar-khayyam", "sourceName": "Omar Khayyám (c. 1048–1131 CE, Persian mathematician and poet)", "verb": "AUTHORS", "targetSlug": "rubiyt-of-omar-khayym", "targetName": "Rubáiyát of Omar Khayyám (rubāʿī, c. 1100 CE; FitzGerald adaptation 1859)", "context": "Omar Khayyám composed the rubāʿī quatrains c. 1100 CE; Edward FitzGerald's English adaptation (1859) became a cult Victorian text and one of the most widely published English poems of the 19th century."},
      {"sourceSlug": "rubiyt-of-omar-khayym", "sourceName": "Rubáiyát (FitzGerald — Victorian scepticism, carpe diem, wine and love)", "verb": "RESONATES_WITH", "targetSlug": "victorian-religious-doubt", "targetName": "Victorian religious doubt and Aesthetic movement (Rossetti, Swinburne, Pre-Raphaelites)", "context": "FitzGerald's Rubáiyát resonated with Victorian doubters — its themes of hedonistic carpe diem and scepticism about afterlife responded to the religious uncertainties produced by Darwinian evolution and made it a cult text of the fin-de-siècle Aesthetic movement."},
      {"sourceSlug": "rubiyt-of-omar-khayym", "sourceName": "Rubáiyát (Persian poetry — Western discovery; Hafiz, Rumi reception)", "verb": "INITIATES", "targetSlug": "western-discovery-persian-poetry", "targetName": "Western reception of Persian poetry (Hafiz, Rumi — 19th–21st centuries)", "context": "FitzGerald's Rubáiyát initiated the English-speaking world's fascination with Persian poetry — preceding and stimulating the broader Western discovery of Hafiz and Rumi that expanded in the late 20th century."}
    ],
    "places": [
      {"name": "Nishapur, Khorasan (Omar Khayyám's birthplace; Seljuk period Persia c. 1100 CE)", "role": "Omar Khayyám was born in Nishapur, in the Khorasan region of Persia (now Iran) c. 1048 CE — his mathematical and poetic work was produced in the context of the Seljuk court at Nishapur"},
      {"name": "London, England (FitzGerald's translation 1859 — Rossetti, Swinburne; Arts and Crafts editions)", "role": "FitzGerald's Rubáiyát was published in London in 1859 — discovered by Rossetti and Swinburne, it became a cult text of the Victorian Aesthetic movement and was published in lavish illustrated editions"}
    ],
    "subjects": ["Persian Literature", "Medieval Era", "Omar Khayyám", "Rubāʿī Poetry", "FitzGerald Translation", "Victorian Literature", "Persian Culture", "Hedonism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Rubáiyát of Omar Khayyám (c. 1100 CE; FitzGerald adaptation 1859) is a masterpiece of both Persian poetry and Victorian translation — FitzGerald's adaptation became a cult text of Victorian scepticism, one of the most widely published English poems of the 19th century, and the initiator of the English-speaking world's fascination with Persian literary culture. Omar Khayyám's mathematical achievements (the Jalālī calendar, cubic equations) make him one of the most important scientists of the medieval Islamic world.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-shepherd-of-hermas": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-shepherd-of-hermas.json",
  "slug": "the-shepherd-of-hermas",
  "data": {
    "summary": "The Shepherd of Hermas (Greek: Ποιμήν τοῦ Ἑρμᾶ, Poimēn tou Herma) is an early Christian literary work composed c. 100–160 CE, attributed to a man named Hermas (possibly the brother of Pope Pius I), and one of the most widely read texts in the early Christian Church — included in some early canonical lists (notably the Codex Sinaiticus, where it follows the Apocalypse of John) and considered authoritative scripture by Clement of Alexandria, Origen, and Athanasius. The Shepherd of Hermas is structured as an apocalyptic vision in three sections: the Visions (five visions in which Hermas receives revelations from an elderly woman representing the Church and from the Shepherd, an angel of repentance); the Mandates (twelve commandments given by the Shepherd); and the Similitudes (ten parables explaining the mandates through allegorical imagery).\n\nThe Shepherd of Hermas is historically significant as the most important early Christian document addressing the question of post-baptismal sin — whether Christians who sin after baptism can be forgiven and restored to the Church. The text's answer — that a second repentance is possible, but only once — was a crucial intervention in the early Church's debate about the forgiveness of serious post-baptismal sins (murder, adultery, apostasy), and it influenced the development of the sacrament of penance in the Catholic Church. The text also provides valuable evidence for early Christian community life, prophecy, and eschatological expectation in the 2nd century CE.\n\nThe Shepherd of Hermas is written in a simple Greek style accessible to ordinary Christians, reflecting the Roman Christian community of the early 2nd century — its concern for moral reform, its middle-class economic anxieties (the Shepherd repeatedly warns against over-concern for wealth), and its vibrant apocalyptic prophecy make it a unique window into the life of an early Christian urban community.",
    "causes": [
      "The early Church's acute theological crisis about post-baptismal sin — whether serious sin after baptism (apostasy, adultery, murder) was unforgivable, as some rigorists maintained, or whether a second repentance was possible — created the theological demand for the Shepherd's authoritative answer: one more chance, but only once.",
      "The apocalyptic tradition of early Jewish and Christian writing — the tradition of visionary literature in which a human recipient receives heavenly visions, angelic guides, and divine commands (Enoch, Daniel, Revelation) — provided the literary form for the Shepherd of Hermas's three-part visionary structure.",
      "The conditions of the Roman Christian community in the early 2nd century CE — the prosperity of some Christians, the social pressures of the Roman urban environment, and the Church's need for moral formation of its members — drove the Shepherd's extensive treatment of practical moral questions (wealth, domestic life, prophecy, church governance)."
    ],
    "effects": [
      "The Shepherd of Hermas's doctrine of a second repentance influenced the development of the Catholic sacrament of penance — its argument that serious post-baptismal sins could be forgiven through a formal act of repentance and restoration to the community provided a theological precedent for the later development of auricular confession and penitential discipline.",
      "The Shepherd's widespread use in early Christian education — it was used as a catechetical text in many early Christian communities and was included in several early canonical lists — made it one of the most read texts in the 2nd and 3rd century Church, alongside the four Gospels and Paul's letters.",
      "The Shepherd of Hermas provides uniquely valuable evidence for the social and economic life of the early Roman Christian community — its attention to the problems of wealth, double-mindedness, false prophecy, and domestic relationships makes it an invaluable source for scholars of early Christianity and the social history of the Roman Empire."
    ],
    "relationships": [
      {"sourceSlug": "hermas", "sourceName": "Hermas (fl. c. 100–160 CE, Roman Christian author)", "verb": "AUTHORS", "targetSlug": "the-shepherd-of-hermas", "targetName": "The Shepherd of Hermas (c. 100–160 CE — Visions, Mandates, Similitudes)", "context": "Hermas composed the Shepherd c. 100–160 CE — one of the most widely read texts in the early Church, included in some canonical lists and cited as scripture by Clement of Alexandria, Origen, and Athanasius."},
      {"sourceSlug": "the-shepherd-of-hermas", "sourceName": "Shepherd of Hermas (second repentance — post-baptismal sin)", "verb": "INFLUENCES", "targetSlug": "catholic-sacrament-of-penance", "targetName": "Catholic sacrament of penance (confession and restoration)", "context": "The Shepherd's doctrine of a second repentance for post-baptismal sin influenced the development of the Catholic sacrament of penance — it provided theological precedent for the forgiveness of serious post-baptismal sins through formal penitential discipline."},
      {"sourceSlug": "the-shepherd-of-hermas", "sourceName": "Shepherd of Hermas (Codex Sinaiticus — near-canonical status; Clement, Origen, Athanasius)", "verb": "CONSIDERED_SCRIPTURAL_BY", "targetSlug": "early-christian-church", "targetName": "Early Christian Church (2nd–3rd century — scriptural canon debate)", "context": "The Shepherd of Hermas was included in the Codex Sinaiticus and cited as scripture by Clement of Alexandria, Origen, and Athanasius — making it one of the most significant texts in the early Christian canonical debate."}
    ],
    "places": [
      {"name": "Rome, Italy (Roman Christian community, c. 100–160 CE — 2nd century urban Christianity)", "role": "The Shepherd of Hermas was written for the Roman Christian community c. 100–160 CE — its attention to wealth, domestic life, and church governance reflects the specific conditions of an early Christian urban community in Rome"},
      {"name": "Christian Church worldwide (Codex Sinaiticus, Clement, Origen — widespread 2nd–3rd century use)", "role": "The Shepherd was used as a catechetical text across the early Christian world — cited in Alexandria (Clement, Origen), in North Africa (Tertullian), and preserved in the Codex Sinaiticus (c. 350 CE)"}
    ],
    "subjects": ["Early Christian Literature", "Ancient Era", "Apocalyptic Literature", "Church History", "Repentance", "Greek Literature", "Rome", "Patristic Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Shepherd of Hermas (c. 100–160 CE) was one of the most widely read texts in the early Christian Church — near-canonical in some communities, cited as scripture by Clement, Origen, and Athanasius, and included in the Codex Sinaiticus. Its doctrine of a second repentance influenced the development of the Catholic sacrament of penance; its vivid picture of early Roman Christian community life makes it a uniquely valuable historical source.",
      "significanceCategory": "highly-significant"
    }
  }
},

"te-deum": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780te-deum.json",
  "slug": "te-deum",
  "data": {
    "summary": "The Te Deum (Latin: 'Te Deum laudamus', 'We praise thee, O God') is a late 4th–early 5th century CE Latin Christian hymn of praise, traditionally attributed (in a legend of debatable historicity) to a spontaneous composition by Ambrose of Milan and Augustine of Hippo at Augustine's baptism in Milan on Easter Vigil, 387 CE — the so-called 'Ambrosian Hymn' — though modern scholarship attributes it to Nicetas of Remesiana (c. 335–414 CE), a bishop in present-day Serbia. The Te Deum consists of three sections: a doxological praise of God (verses 1–13); a Christological section praising Christ (verses 14–21); and a closing set of versicle-and-response petitions based on Psalms (verses 22–29).\n\nThe Te Deum is one of the most important liturgical texts of the Western Christian Church — used in the Divine Office at Matins (later Lauds) since at least the 6th century CE, and for special occasions of thanksgiving: victories in battle, royal coronations, treaties of peace, canonisations of saints, and papal elections. The Reformation retained the Te Deum — both Lutheran and Anglican liturgical traditions incorporated it, and it remains a central liturgical text in Catholic, Orthodox, Anglican, and Lutheran worship to the present day. Its musical settings number in the hundreds — from Gregorian chant through Handel's 'Dettingen Te Deum' (1743), Berlioz's Te Deum (1849), Bruckner's Te Deum (1881–1884), and Verdi's Te Deum (1896/1898) to Benjamin Britten's Festival Te Deum (1945).\n\nThe Te Deum's cultural significance in European history extends far beyond liturgy — it was sung at the coronations of English monarchs from the medieval period to Elizabeth II (1953), at the end of the Thirty Years' War (1648), at the Treaty of Utrecht (1713), at the Congress of Vienna (1815), and at every major European political event of thanksgiving, making it one of the primary ritual markers of European political and religious history for over 1,500 years.",
    "causes": [
      "The late 4th century Christian theological synthesis — the Council of Nicaea (325 CE) and the subsequent definition of Trinitarian orthodoxy under Ambrose of Milan and the Nicene tradition — created the theological context for the Te Deum's elaborate Trinitarian praise, particularly its Christological section affirming Christ's pre-existence, incarnation, resurrection, and coming judgment.",
      "The development of the Western Divine Office (the daily round of prayer in monasteries and cathedral churches) — and the need for a substantial Latin hymn of praise for the night office (Matins) — drove the adoption of the Te Deum as a regular element of the Office, giving it the liturgical function that ensured its continuous use for over 1,500 years.",
      "The tradition of special thanksgiving services — the Roman practice of supplicatio (public thanksgiving to the gods for military victories) and its Christian successor (a thanksgiving Mass for victories, treaties, and royal events) — created the use of the Te Deum as the liturgical marker of European political events of thanksgiving."
    ],
    "effects": [
      "The Te Deum was sung at virtually every major European political event of thanksgiving from the medieval period to the 20th century — royal coronations, military victories, peace treaties, and the ends of wars — making it one of the primary ritual markers of European political and religious history for 1,500 years and the sonic embodiment of European Christian political culture.",
      "The Te Deum's musical settings are among the most numerous of any liturgical text — from Gregorian chant through Handel (Dettingen Te Deum, 1743), Berlioz (1849), Bruckner (1881–1884), and Verdi (1896/1898), the text stimulated some of the most ambitious orchestral sacred music in the European tradition.",
      "The Te Deum's crossing of the Reformation divide — retained in Lutheran, Anglican, and all major Protestant liturgical traditions, as well as in Catholic and Orthodox worship — made it one of the few liturgical texts shared across the entire Western Christian world, serving as a point of ecumenical connection even during the centuries of confessional conflict."
    ],
    "relationships": [
      {"sourceSlug": "nicetas-of-remesiana", "sourceName": "Nicetas of Remesiana (c. 335–414 CE, bishop of Remesiana, Serbia)", "verb": "AUTHORS", "targetSlug": "te-deum", "targetName": "Te Deum (c. late 4th century CE — primary Latin Christian hymn of praise)", "context": "Modern scholarship attributes the Te Deum to Nicetas of Remesiana (c. 335–414 CE) — though traditionally attributed to Ambrose and Augustine, Nicetas's authorship is now widely accepted."},
      {"sourceSlug": "te-deum", "sourceName": "Te Deum (coronations, victories, peace treaties — European political thanksgiving)", "verb": "SUNG_AT", "targetSlug": "european-political-thanksgiving", "targetName": "European political and religious events of thanksgiving (coronations, treaties, victories)", "context": "The Te Deum was sung at royal coronations (English monarchs from medieval period to Elizabeth II 1953), peace treaties (Westphalia 1648, Utrecht 1713), and military victories — one of the primary ritual markers of European political history."},
      {"sourceSlug": "te-deum", "sourceName": "Te Deum (Handel, Berlioz, Bruckner, Verdi — musical settings)", "verb": "STIMULATES", "targetSlug": "european-sacred-music", "targetName": "European orchestral sacred music (Handel, Berlioz, Bruckner, Verdi — Te Deum settings)", "context": "The Te Deum text stimulated some of the most ambitious European orchestral sacred music — Handel's Dettingen Te Deum (1743), Berlioz's Te Deum (1849), Bruckner's Te Deum (1881–1884), and Verdi's Te Deum (1896/1898) are major works of the symphonic choral repertoire."}
    ],
    "places": [
      {"name": "Europe (liturgical use from c. 6th century CE — Catholic, Orthodox, Anglican, Lutheran worship)", "role": "The Te Deum has been used in Western Christian liturgy since at least the 6th century CE — in the Divine Office and for special thanksgiving services across Catholic, Anglican, Lutheran, and Orthodox traditions"},
      {"name": "European royal courts and political events (coronations, peace treaties — 1,500 years of use)", "role": "The Te Deum was sung at every major European political event of thanksgiving — royal coronations, peace treaties (Westphalia, Utrecht, Congress of Vienna), and military victories — for 1,500 years"}
    ],
    "subjects": ["Latin Literature", "Ancient Era", "Christian Liturgy", "Hymn", "Patristic Literature", "European Sacred Music", "Catholic Church", "Western Christianity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Te Deum (c. late 4th century CE) is one of the most important liturgical texts of Western Christianity — used continuously in the Divine Office for 1,500 years and sung at every major European political event of thanksgiving (coronations, peace treaties, victories). Its musical settings by Handel, Berlioz, Bruckner, and Verdi are major works of the European sacred music tradition; its crossing of the Reformation divide makes it a rare point of ecumenical connection.",
      "significanceCategory": "world-changing"
    }
  }
},

"terminologia-anatomica": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780terminologia-anatomica.json",
  "slug": "terminologia-anatomica",
  "data": {
    "summary": "Terminologia Anatomica (TA) is the international standard of anatomical nomenclature — the authoritative list of standard anatomical terms for human gross anatomy — published by the Federative International Programme on Anatomical Terminologies (FIPAT, formerly FICAT) on behalf of the International Federation of Associations of Anatomists (IFAA). The current standard is Terminologia Anatomica 2 (TA2), published in 2019, superseding the first edition (TA1, 1998), which itself replaced the previous standard Nomina Anatomica (originally published 1895, last revised 1989). Terminologia Anatomica 2 contains approximately 7,500 terms designating structures of human gross anatomy in Latin (with English equivalents), organised hierarchically by body region and system.\n\nAnatomical nomenclature — the systematic naming of anatomical structures — is one of the oldest branches of scientific terminology, with its origins in ancient Greek medicine (Galen, Herophilus) and its first systematic codification in the Renaissance anatomical tradition (Vesalius's De Humani Corporis Fabrica, 1543). The Basel Nomina Anatomica (BNA, 1895) was the first internationally agreed standard, produced by a commission of 50 anatomists at the Anatomische Gesellschaft meeting in Basel — replacing a chaos of competing national and personal naming traditions with a single Latin standard. The subsequent international revision processes (the Jena Nomina Anatomica 1935, the Paris Nomina Anatomica 1955, the revisions of 1961, 1966, 1977, 1983, and 1989, and the Terminologia Anatomica 1998 and 2019) represent a century-long process of international scientific collaboration to standardise the language of anatomy.\n\nTerminologia Anatomica matters both as a practical scientific standard (enabling communication across languages in anatomy, surgery, radiology, and clinical medicine) and as a symbol of the internationalisation of science — the aspiration to replace the diversity of national terminological traditions with a single universal language of anatomy, accessible to medical practitioners worldwide.",
    "causes": [
      "The pre-19th-century chaos of anatomical nomenclature — the existence of hundreds of competing names for the same structures (eponymous names honouring individual anatomists: the Fallopian tubes, the Circle of Willis, the Islets of Langerhans; national variations; multiple synonyms for the same structure) — created a practical clinical and educational problem that the Basel Nomina Anatomica (1895) was designed to solve.",
      "The internationalisation of science in the late 19th century — the formation of international scientific societies, the development of international standardisation in measurement (the metric system, 1875), and the recognition that scientific communication required agreed terminology — provided the institutional context for the first international anatomical nomenclature conference (Basel, 1895).",
      "The development of modern anatomy as a university discipline — the teaching of gross anatomy in medical schools worldwide required standardised textbooks and nomenclature that could be used across national boundaries — drove the demand for an internationally agreed terminological standard."
    ],
    "effects": [
      "Terminologia Anatomica and its predecessors (the Nomina Anatomica series from 1895) standardised anatomical communication across languages and national medical traditions — enabling surgeons, radiologists, anatomists, and clinicians worldwide to use a shared terminological system and reducing the errors that could arise from competing naming traditions.",
      "The Basel Nomina Anatomica (1895) and its successors contributed to the demise of eponymous anatomical terminology (naming structures after individual anatomists) in official nomenclature — the movement toward descriptive Latin terms that indicate a structure's location, function, or form rather than honouring a discoverer is part of the broader 20th-century trend toward internationalised scientific terminology.",
      "Terminologia Anatomica is a model for the internationalisation of scientific nomenclature in other fields — its century-long revision process and its adoption by the IFAA provided a template for international terminological standards in histology (Terminologia Histologica, 2008), embryology (Terminologia Embryologica, 2013), and neuroanatomy."
    ],
    "relationships": [
      {"sourceSlug": "terminologia-anatomica", "sourceName": "Terminologia Anatomica (TA2, 2019; 7,500 terms — FIPAT/IFAA)", "verb": "SUPERSEDES", "targetSlug": "nomina-anatomica", "targetName": "Nomina Anatomica (1895–1989 — Basel Nomina Anatomica through 6th edition)", "context": "Terminologia Anatomica (1998, TA2 2019) superseded the Nomina Anatomica series — the international anatomical naming standard established at Basel in 1895 and revised six times over the following century."},
      {"sourceSlug": "terminologia-anatomica", "sourceName": "Terminologia Anatomica (international standard — clinical communication, surgery, radiology)", "verb": "STANDARDISES", "targetSlug": "anatomical-science", "targetName": "Anatomical science and clinical medicine (surgery, radiology, medical education worldwide)", "context": "Terminologia Anatomica is the international standard for anatomical nomenclature — enabling surgeons, radiologists, anatomists, and clinicians worldwide to use a shared terminological system."},
      {"sourceSlug": "terminologia-anatomica", "sourceName": "Terminologia Anatomica (Latin terms — replacing eponymous anatomy)", "verb": "EXEMPLIFIES", "targetSlug": "international-scientific-standardisation", "targetName": "International scientific nomenclature standardisation (metric system, IUPAC, ICD)", "context": "Terminologia Anatomica exemplifies the broader 20th-century movement toward internationalised scientific terminology — its century-long revision process provided a model for Terminologia Histologica, Terminologia Embryologica, and other international nomenclature standards."}
    ],
    "places": [
      {"name": "Basel, Switzerland (first international anatomical congress 1895 — Basel Nomina Anatomica)", "role": "The first internationally agreed anatomical nomenclature (Basel Nomina Anatomica, BNA) was produced at the Anatomische Gesellschaft meeting in Basel in 1895 — the founding moment of international anatomical standardisation"},
      {"name": "International (IFAA/FIPAT — global medical education and clinical practice standard)", "role": "Terminologia Anatomica is an international standard — adopted by the International Federation of Associations of Anatomists (IFAA) and used in medical education and clinical practice worldwide"}
    ],
    "subjects": ["Medical Science", "Modern Era", "Anatomy", "Scientific Nomenclature", "Medical Education", "Latin", "International Standards", "Clinical Medicine"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Terminologia Anatomica (TA2, 2019; superseding the Nomina Anatomica series from 1895) is the international standard for anatomical nomenclature — the product of a century-long international scientific collaboration to standardise the language of anatomy across languages and national traditions. Its practical importance for clinical medicine, surgery, and medical education worldwide is considerable, and it exemplifies the broader 20th-century movement toward internationalised scientific terminology.",
      "significanceCategory": "significant"
    }
  }
},

"parkinsons-law": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780parkinsons-law.json",
  "slug": "parkinsons-law",
  "data": {
    "summary": "Parkinson's Law is a satirical adage and a book (full title: Parkinson's Law, or The Pursuit of Progress) by the British historian, naval historian, and management satirist C. Northcote Parkinson (1909–1993), derived from an essay first published in The Economist on 19 November 1955 and expanded into a book published by Houghton Mifflin in 1958. Parkinson's Law states: 'Work expands so as to fill the time available for its completion.' The essay and book argue, through mock-scholarly historical analysis of the British Admiralty and Colonial Office, that the number of officials in any bureaucracy tends to increase at a fixed annual rate (5.17% to 6.56% per year, Parkinson claims with satirical statistical precision), regardless of the actual work to be done — bureaucratic expansion is self-perpetuating, driven by two motivating factors: the desire of officials to multiply their subordinates (rather than their rivals), and the tendency for officials to create work for each other.\n\nParkinson's Law is one of the most widely cited aphorisms in management theory and organisational science — its formulation of the tendency of bureaucratic expansion to outpace productive need has been verified by empirical research and applied to fields ranging from government administration through software development (in Scrum and Agile methodologies, where Parkinson's Law is cited as a reason for time-boxing tasks) to personal productivity (in time management, where the principle suggests that deadlines should be set aggressively to prevent work from expanding).\n\nParkinson's corollary laws — 'Expenditure rises to meet income', 'Delay is the deadliest form of denial', and 'Officials want to multiply subordinates, not rivals' — have similarly entered the lexicon of management theory. The book was a satirical bestseller in Britain and the United States and remains in print; Parkinson's Law has entered the English language as a widely understood idiom for bureaucratic self-perpetuation.",
    "causes": [
      "Parkinson's experience as a historian of the British Royal Navy and his study of the British Admiralty's administrative expansion during World War I and the interwar period — the Admiralty grew substantially in administrative staff as the fighting Navy declined — provided the empirical data and the satirical inspiration for the law.",
      "The mid-20th century expansion of the British welfare state and the civil service — the post-war growth of government bureaucracy under the Attlee and subsequent governments — provided the political and social context for Parkinson's satirical analysis, which targeted the expanding British civil service's institutional logic.",
      "The tradition of English satirical essays on government and bureaucracy — from Jonathan Swift's 'A Modest Proposal' through the Benthamite reforms and the Victorian administrative history — provided the literary model for Parkinson's mock-scholarly analysis with its satirical pseudo-statistical precision."
    ],
    "effects": [
      "Parkinson's Law entered the English language as a widely understood aphorism — 'work expands so as to fill the time available for its completion' is one of the most cited management principles worldwide, applied in business, government, personal productivity, and software development, demonstrating the remarkable diffusion of a satirical formula into serious organisational theory.",
      "Parkinson's Law stimulated a tradition of similar management satire — C. Peter's The Peter Principle ('In a hierarchy, every employee tends to rise to their level of incompetence', 1969), Poul Anderson's Murphy's Law, and other formulations of organisational pathology — creating a genre of satirical management science that achieved serious analytical standing.",
      "In software development, Parkinson's Law is cited in Agile and Scrum methodologies as a justification for time-boxing (setting firm time limits for tasks) — the principle that work expands to fill available time is used to argue for short, fixed sprints as a countermeasure to bureaucratic expansion in software projects."
    ],
    "relationships": [
      {"sourceSlug": "c-northcote-parkinson", "sourceName": "C. Northcote Parkinson (1909–1993, British historian and satirist)", "verb": "AUTHORS", "targetSlug": "parkinsons-law", "targetName": "Parkinson's Law (The Economist 19 November 1955; book 1958)", "context": "Parkinson formulated Parkinson's Law in The Economist essay (1955) and expanded it into a book (1958) — one of the most widely cited management aphorisms: 'Work expands so as to fill the time available for its completion'."},
      {"sourceSlug": "parkinsons-law", "sourceName": "Parkinson's Law (bureaucratic expansion — Admiralty, Colonial Office)", "verb": "SATIRISES", "targetSlug": "british-civil-service", "targetName": "British civil service and 20th-century bureaucratic expansion", "context": "Parkinson's Law satirises the self-perpetuating logic of British government bureaucracy — using the Admiralty and Colonial Office as case studies to demonstrate that bureaucratic expansion is independent of productive need."},
      {"sourceSlug": "parkinsons-law", "sourceName": "Parkinson's Law (management satire — Peter Principle, Murphy's Law)", "verb": "INSPIRES", "targetSlug": "management-satire-genre", "targetName": "Management satire genre (Peter Principle 1969, Murphy's Law — organisational pathology)", "context": "Parkinson's Law stimulated the genre of satirical management science — The Peter Principle (1969) and other formulations of organisational pathology are direct successors to Parkinson's satirical pseudo-scholarly method."}
    ],
    "places": [
      {"name": "London, England (The Economist, 19 November 1955; British civil service context)", "role": "Parkinson's Law was first published in The Economist in London in 1955 — a satirical analysis of the British civil service's post-war expansion"},
      {"name": "Global (management theory, Agile/Scrum, personal productivity — worldwide adoption of the aphorism)", "role": "Parkinson's Law has been adopted worldwide in management theory, software development (Agile/Scrum time-boxing), and personal productivity — one of the most widely cited organisational aphorisms in the English-speaking world"}
    ],
    "subjects": ["British Literature", "Modern Era", "C. Northcote Parkinson", "Management Theory", "Bureaucracy", "Satire", "Organisational Science", "20th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Parkinson's Law (1955/1958) is one of the most widely cited management aphorisms — 'Work expands so as to fill the time available for its completion' has entered the English language as an understood idiom for bureaucratic self-perpetuation, applied in business, government, and software development. Its stimulation of the management satire genre (The Peter Principle, Murphy's Law) and its adoption in Agile/Scrum methodology demonstrate its remarkable diffusion from satirical essay to serious organisational theory.",
      "significanceCategory": "significant"
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
