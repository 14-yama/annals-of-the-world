#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 30 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: georgics, gitanjali, gayatri-mantra, germania, exodus,
          chronicles-froissart, alices-adventures-in-wonderland,
          all-quiet-on-the-western-front
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-30-may2026"

ENRICHMENTS = {

"georgics": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780georgics.json",
  "slug": "georgics",
  "data": {
    "summary": "The Georgics (Latin: Georgica) is the didactic poem in four books by Publius Vergilius Maro (Virgil, 70–19 BCE), composed c. 36–29 BCE and published c. 29 BCE — the work that Virgil himself is said to have considered his finest, and which ancient critics often ranked above the Aeneid for its sustained technical and lyrical achievement. The poem purports to be a manual on farming: Book I on crops and weather; Book II on vines and trees; Book III on livestock; Book IV on beekeeping. But the Georgics is simultaneously a complex meditation on the relationship between human labour and nature, on the costs and meanings of agricultural civilisation, on the cycle of death and renewal, and on the political meaning of Italy's land and history in the aftermath of the civil wars. Its celebration of Italy ('Salve, magna parens frugum, Saturnia tellus, / magna virum' — 'Hail, great mother of crops, Saturnian earth, great mother of heroes') and of the values of agricultural labour and Italian country life served the Augustan programme of restoration and renewal after decades of civil war.\n\nThe Georgics' fourth book ends with the Aristaeus epyllion — the myth of the beekeeper Aristaeus who loses his bees through the death of Eurydice (killed while fleeing his advances), and who must perform elaborate ritual sacrifices to restore them through bugonia (the spontaneous generation of bees from the corpse of a bull) — and embedded within the Aristaeus story is the Orpheus episode: the most celebrated passage in the Georgics, in which Orpheus descends to the underworld to retrieve Eurydice, nearly succeeds, but looks back at the last moment and loses her forever, wandering inconsolably until his death. This narrative of irreversible loss — 'What could I do? Madness took him again, and Eurydice, now recovered, alas! again fell back' — is one of the most moving passages in Latin poetry.\n\nThe Georgics exercised enormous influence on subsequent European literature — it was the model for Virgil's Renaissance imitators (Vida, Pontano, Fracastoro), for English agricultural poetry (Thomson's Seasons, Cowper's Task, Keats's 'To Autumn'), and for the tradition of nature poetry that takes human labour and seasonal rhythm as the basis for meditation on the human condition.",
    "causes": [
      "Augustus's (then Octavian's) programme of agricultural and moral restoration after the decades of civil war that had depopulated the Italian countryside — the need to repopulate rural Italy, restore its farms, and legitimise the new political order through the celebration of traditional Italian values of labour, frugality, and piety — gave the Georgics its political context and its Augustan patronage through Maecenas.",
      "Virgil's experience of the dispossession of Italian farmers to settle his veterans (including, according to tradition, the dispossession of Virgil's own family at Mantua) — which had produced the Eclogues' plaintive laments over the loss of the pastoral world — gave the Georgics its autobiographical emotional investment in the question of what Italian land means and what it costs to cultivate it.",
      "The Hellenistic tradition of didactic poetry — particularly Hesiod's Works and Days (the original farming poem) and the Hellenistic didactic tradition of Nicander and Aratus (Phaenomena, which Virgil imitates in the astronomical sections of Book I) — provided the literary models that Virgil both drew on and transcended, elevating the genre from technical instruction to philosophical poetry."
    ],
    "effects": [
      "The Georgics' fourth book's Orpheus episode — Orpheus's failed retrieval of Eurydice from the underworld — became one of the most retold myths in Western culture, its image of irrevocable loss and the self-defeating nature of love's desire influencing Ovid's Metamorphoses, Rilke's Sonnets to Orpheus, and countless subsequent treatments of the myth in literature, opera, and visual art.",
      "The Georgics' celebration of Italian rural life and agricultural labour — 'O fortunatos nimium, sua si bona norint, / agricolas!' ('O too fortunate, did they but know their happiness, the farmers!') — became the founding text of the Western tradition of georgic poetry: the celebration of agricultural labour and rural life as morally and aesthetically valuable, influencing Thomson, Cowper, Keats, and the entire tradition of English nature poetry.",
      "The Georgics' influence on Western agricultural writing — the idea that farming is simultaneously practical activity and ethical vocation, that the cultivation of land is metaphor for the cultivation of the self and the state — runs through the entire European tradition of agricultural writing from Columella and Palladius through the medieval estate manuals to the 18th-century Physiocrats."
    ],
    "relationships": [
      {"sourceSlug": "virgil", "sourceName": "Virgil (70–19 BCE)", "verb": "AUTHORS", "targetSlug": "georgics", "targetName": "Georgics (c. 29 BCE)", "context": "Virgil wrote the Georgics over seven years (c. 36–29 BCE) under the patronage of Maecenas and the political inspiration of Augustus's programme of Italian renewal — his mature work before the Aeneid."},
      {"sourceSlug": "georgics", "sourceName": "Georgics (Book IV, Orpheus episode)", "verb": "CONTAINS", "targetSlug": "orpheus-myth", "targetName": "Orpheus and Eurydice myth (Georgics IV treatment)", "context": "The Georgics' Orpheus episode — embedded in the Aristaeus myth — is the most celebrated literary treatment of the Orpheus and Eurydice story before Ovid's Metamorphoses, and its image of irreversible loss became foundational for all subsequent treatments."},
      {"sourceSlug": "georgics", "sourceName": "Georgics", "verb": "ESTABLISHES", "targetSlug": "georgic-poetry", "targetName": "Georgic poetry tradition (English nature poetry, 18th century)", "context": "The Georgics is the founding text of the georgic tradition — agricultural and nature poetry that combines practical instruction with ethical and philosophical meditation — influencing Thomson, Cowper, Keats, and the English Romantic nature poetry tradition."}
    ],
    "places": [
      {"name": "Italy (29 BCE, publication and celebration)", "role": "The Georgics is a sustained celebration of Italy — its landscape, its agriculture, its rural people, and its history — serving Augustus's programme of Italian renewal and the reconstitution of Italian identity after the civil wars"},
      {"name": "Naples and Rome (composition context, c. 36–29 BCE)", "role": "Virgil composed the Georgics primarily in Naples, reading the completed work to Augustus over four days in 29 BCE — an event that marked the work's entry into the cultural programme of the new Augustan order"}
    ],
    "subjects": ["Latin Literature", "Classical Era", "Virgil", "Roman Poetry", "Ancient Rome", "Didactic Poetry", "Nature Poetry", "Augustan Age"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Virgil's Georgics (c. 29 BCE) is the greatest didactic poem in Latin literature and one of the most influential texts in the Western poetic tradition. Its Orpheus episode became foundational for all subsequent treatments of the myth; its celebration of Italian rural life founded the Georgian poetic tradition; and its meditation on labour, loss, and renewal — written in the shadow of Rome's civil wars — made it a model for subsequent traditions of nature poetry.",
      "significanceCategory": "world-changing"
    }
  }
},

"gitanjali": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gitanjali.json",
  "slug": "gitanjali",
  "data": {
    "summary": "Gitanjali (Bengali: গীতাঞ্জলি, 'Song Offerings') is the poetry collection by Rabindranath Tagore (1861–1941), originally published in Bengali in 1910 (Gitanjali: Naivedya) and translated into English by Tagore himself and published by the India Society (London) in 1912 with an introduction by W.B. Yeats — winning Tagore the Nobel Prize in Literature in 1913, making him the first Asian laureate and one of the most significant literary events in the history of colonial Asia's engagement with European culture. The collection comprises 103 prose poems (in the English version) — lyrical expressions of devotion, love, nature, and the relationship between the human soul and the divine — drawing on the tradition of Bengali devotional poetry (bhakti), the Vaishnava lyric tradition of Chaitanya, the Baul folk singers of Bengal, and Tagore's own philosophical synthesis of Bengali Hinduism with the universalist spirituality he developed in response to Brahmo Samaj and the influence of the Upanishads.\n\nTagore's English Gitanjali — translated by himself and shaped for a Western audience by his collaboration with Yeats, who called it 'the work of a supreme culture' — is one of the most successful examples of literary self-translation in the history of world literature. The prose poems' lyrical simplicity, their metaphors of longing and surrender, and their evocation of a spirituality without institutional religion appealed enormously to the Edwardian literary world's fascination with Eastern mysticism, and Gitanjali's Nobel Prize gave Tagore global celebrity.\n\nTagore's Gitanjali is the most significant single text in the history of modern Bengali literature and the work through which Indian literature first achieved global recognition — its success opened the Western literary market to Indian writing and established Tagore as the first non-Western writer to shape the global literary conversation. His song 'Amar Sonar Bangla' (written 1905, drawn from the Gitanjali tradition) became the national anthem of Bangladesh; 'Jana Gana Mana' (written 1911, in the same devotional lyric tradition) became the national anthem of India.",
    "causes": [
      "Tagore's grief following the deaths of his wife (1902), his father (1905), and two of his children — and the devastating floods in Bengal (1907) — intensified the devotional and searching quality of the poetry that eventually became Gitanjali, giving the collection its tone of personal spiritual seeking rather than conventional religious observance.",
      "The Bengali bhakti devotional tradition — the tradition of the Vaishnava lyric poets (Chandidas, Vidyapati, Jayadeva) and the Baul folk singers of Bengal, whose poetry expresses personal love and devotion to the divine in the metaphor of the beloved — provided the literary tradition from which Tagore drew Gitanjali's vocabulary of longing, surrender, and love.",
      "Tagore's visit to England in 1912 — which brought him into contact with W.B. Yeats, who read his English translations and immediately championed them — provided the literary context for Gitanjali's reception: Yeats's introduction, his championing of the work at the Poetry Society, and the India Society publication created the conditions for the Nobel Prize."
    ],
    "effects": [
      "Tagore's 1913 Nobel Prize for Literature — awarded primarily on the basis of Gitanjali — was the first Nobel Prize awarded to an Asian and made Tagore the global representative of Indian/Asian literature, fundamentally changing the relationship between Indian literature and the Western literary establishment.",
      "Gitanjali's success established Tagore's songs (Rabindra Sangeet) as the cultural foundation of Bengali literary identity — his 2,000 songs remain central to Bengali cultural life in both West Bengal and Bangladesh, and two of his songs became the national anthems of India and Bangladesh, making Tagore's lyric tradition unique in the history of world literature.",
      "Tagore's self-translation of Gitanjali — shaping his own work for a Western audience — pioneered the practice of postcolonial literary self-translation and the engagement of Asian writers with the Western literary market on their own terms, establishing a model followed by subsequent Indian writers in English."
    ],
    "relationships": [
      {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore (1861–1941)", "verb": "AUTHORS", "targetSlug": "gitanjali", "targetName": "Gitanjali (1910 Bengali, 1912 English)", "context": "Tagore wrote Gitanjali in Bengali in 1910 and translated it into English prose poems in 1912 — the translation, introduced by W.B. Yeats, won him the Nobel Prize in Literature in 1913."},
      {"sourceSlug": "gitanjali", "sourceName": "Gitanjali (Nobel Prize, 1913)", "verb": "ESTABLISHES", "targetSlug": "indian-literature-global-recognition", "targetName": "Indian literature's global recognition (first Asian Nobel Prize)", "context": "Gitanjali's Nobel Prize was the first awarded to an Asian writer — making Tagore the global representative of Indian literature and fundamentally changing the relationship between Indian writing and the Western literary establishment."},
      {"sourceSlug": "gitanjali", "sourceName": "Gitanjali / Tagore's songs", "verb": "CONTRIBUTES_TO", "targetSlug": "india-bangladesh-national-anthems", "targetName": "National anthems of India (Jana Gana Mana) and Bangladesh (Amar Sonar Bangla)", "context": "Tagore's devotional songs in the tradition of Gitanjali became the national anthems of both India and Bangladesh — a unique case of a single poet's work forming the national anthems of two nations."}
    ],
    "places": [
      {"name": "Calcutta and Santiniketan, Bengal, India (composition, 1910)", "role": "Tagore wrote and composed the songs that became Gitanjali in Bengal — at his home and at Santiniketan (the school he founded in 1901) — drawing on the Bengali landscape, the Ganges, and the bhakti tradition"},
      {"name": "London (1912, English publication and Nobel Prize context)", "role": "Tagore's visit to London in 1912, his collaboration with Yeats, and the India Society publication of the English Gitanjali — the events that led to the 1913 Nobel Prize and Tagore's global celebrity"}
    ],
    "subjects": ["Indian Literature", "Modern Era", "Rabindranath Tagore", "Bengali Literature", "Nobel Prize", "Devotional Poetry", "20th Century", "Colonial India"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Gitanjali (Tagore, 1910/1912) is the most significant single text in the history of modern Bengali literature and the work through which Indian literature first achieved global recognition — its Nobel Prize in 1913 was the first awarded to an Asian writer. Two songs in Tagore's devotional lyric tradition became the national anthems of India and Bangladesh, making his work uniquely central to the founding identities of two nations.",
      "significanceCategory": "world-changing"
    }
  }
},

"gayatri-mantra": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gayatri-mantra.json",
  "slug": "gayatri-mantra",
  "data": {
    "summary": "The Gayatri Mantra is a sacred Vedic hymn from the Rigveda (Rigveda 3.62.10), traditionally attributed to the sage Vishwamitra and composed c. 1500–1200 BCE — one of the oldest and most sacred prayers in Hinduism, recited for more than three thousand years and considered the most important of all Vedic mantras. In Sanskrit, the mantra reads: 'Oṃ bhūr bhuvaḥ svaḥ / tát savitúr váreṇyaṃ / bhárgo devásya dhīmahi / dhíyo yó naḥ pracodáyāt' — typically translated as 'We meditate on the glory of that Being who has produced this universe; may He enlighten our minds.' The mantra is composed in the Gayatri metre (24 syllables, 3 padas of 8 syllables each) — the metre named after the mantra — and is addressed to Savitri, the solar deity, the divine light that illumines both the physical world and the mind.\n\nThe Gayatri Mantra is the most sacred mantra in the Brahmanical Hindu tradition — traditionally transmitted through the upanayana (sacred thread) initiation ceremony, which admitted the twice-born (dvija) castes (Brahmin, Kshatriya, and Vaishya) to Vedic learning, and which marks the beginning of a student's formal religious education. The mantra is to be recited at the three daily sandhyas (dawn, midday, and dusk), and daily sandhyavandanam (dawn worship including the Gayatri recitation) is one of the central daily ritual obligations of the traditional Hindu. The mantra's restriction to the twice-born castes (from which women and Shudras were traditionally excluded) became a focus of Hindu reform movements in the 19th and 20th centuries — Swami Vivekananda and the Arya Samaj argued for the universal availability of the mantra as a matter of spiritual equality.\n\nThe Gayatri Mantra's three-thousand-year history of continuous recitation makes it one of the oldest continuously used prayers in human religious history. Its philosophical meaning — the meditation on divine light as the source of both physical existence (bhurloka, antariksha, svarloka — earth, atmosphere, heaven) and intellectual illumination — makes it simultaneously a cosmological statement and a prayer for enlightenment, and its simplicity and power have made it central to virtually every tradition of Hindu practice.",
    "causes": [
      "The Vedic religious tradition's understanding of the mantra as a vehicle of cosmic power — the Sanskrit syllables as not merely representing but participating in the divine forces they name — gave the Gayatri Mantra its central role in Brahmanical religious practice, where its correct pronunciation and daily recitation is understood as maintaining the cosmic order (rta).",
      "The solar theology of the Rigveda — its celebration of Savitri (the solar deity) as the source of divine illumination, warmth, and life — gave the Gayatri Mantra its specific theological content: the meditation on the divine light that produces the universe and illumines the human mind, making it simultaneously a cosmological and epistemological prayer.",
      "The brahmanical caste system's organisation of religious knowledge — the restriction of Vedic learning and the Gayatri initiation to the three twice-born castes through the upanayana ceremony — gave the Gayatri Mantra its social function as the marker of brahmanical religious identity and the vehicle of its transmission across generations."
    ],
    "effects": [
      "The Gayatri Mantra's 19th and 20th-century universalisation — Swami Vivekananda's advocacy of making Vedic knowledge available to all, the Arya Samaj's rejection of caste restrictions, and the global spread of yoga and Hindu spirituality in the 20th century — transformed the mantra from the exclusive property of the twice-born castes into a universally available spiritual practice recited by millions of Hindus and non-Hindus worldwide.",
      "The Gayatri Mantra's spread through the global yoga movement — its recitation at the beginning and end of yoga classes, its incorporation into the practice of Western practitioners of meditation and yoga, and its recording and distribution in hundreds of musical versions — has made it one of the most widely known Sanskrit texts outside India, introducing Vedic spirituality to millions of non-Hindu practitioners.",
      "The mantra's philosophical interpretation — its meditation on the divine light as both cosmic creator and inner illuminator — has made it a touchstone for Hindu philosophical theology from Shankara's Advaita Vedanta (which interprets the mantra as a meditation on the universal Brahman) through the Neo-Vedantic tradition of Ramakrishna, Vivekananda, and Aurobindo."
    ],
    "relationships": [
      {"sourceSlug": "gayatri-mantra", "sourceName": "Gayatri Mantra (Rigveda 3.62.10)", "verb": "PART_OF", "targetSlug": "rigveda", "targetName": "Rigveda (c. 1500–1200 BCE)", "context": "The Gayatri Mantra is from Rigveda 3.62.10 — one of the 1,028 hymns of the oldest of the four Vedas — and its attribution to the sage Vishwamitra is one of the oldest poet-attribution traditions in world literature."},
      {"sourceSlug": "gayatri-mantra", "sourceName": "Gayatri Mantra (upanayana ceremony)", "verb": "CENTRAL_TO", "targetSlug": "upanayana", "targetName": "Upanayana (sacred thread initiation ceremony)", "context": "The Gayatri Mantra is the central text of the upanayana — the initiation ceremony admitting the twice-born castes to Vedic learning — which has been the rite of passage for brahmanical religious education for three thousand years."},
      {"sourceSlug": "gayatri-mantra", "sourceName": "Gayatri Mantra (universalisation)", "verb": "PROMOTED_BY", "targetSlug": "swami-vivekananda", "targetName": "Swami Vivekananda (universalisation of Vedic knowledge)", "context": "Vivekananda's advocacy of making Vedic knowledge — including the Gayatri Mantra — available to all people regardless of caste or gender was part of his universalist reform of Hinduism, helping transform the mantra from an exclusive brahmanical ritual to a universally available spiritual practice."}
    ],
    "places": [
      {"name": "Indian subcontinent (c. 1500 BCE–present, continuous use)", "role": "The Gayatri Mantra has been recited daily by Hindus across the Indian subcontinent for approximately 3,000 years — one of the longest continuous religious practices in human history"},
      {"name": "Global (20th–21st century, yoga movement spread)", "role": "The global spread of yoga and Hindu spirituality in the 20th century brought the Gayatri Mantra to practitioners worldwide — making it one of the most widely known Sanskrit texts outside India"}
    ],
    "subjects": ["Hinduism", "Classical Era", "Sanskrit Literature", "Vedic Religion", "Indian History", "Religious Texts", "Mantra", "Ancient India"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Gayatri Mantra (Rigveda 3.62.10, c. 1500 BCE) is the most sacred Vedic prayer in Hinduism — recited daily at dawn, midday, and dusk by hundreds of millions of Hindus for three thousand years, making it one of the longest continuously used prayers in human religious history. Its universalisation through the global yoga movement has made it one of the most widely known Sanskrit texts in the world.",
      "significanceCategory": "world-changing"
    }
  }
},

"germania": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780germania.json",
  "slug": "germania",
  "data": {
    "summary": "Germania (Latin: De Origine et Situ Germanorum, 'On the Origin and Geography of the Germans') is the ethnographic treatise by Publius Cornelius Tacitus (c. 56–c. 120 CE), composed c. 98 CE — a short work (46 chapters) describing the geography, customs, institutions, and tribes of the Germanic peoples east of the Rhine and north of the Danube, peoples who had never been conquered by Rome and who represented the most formidable external threat to the Roman Empire. Germania is simultaneously a work of geographical and ethnographic description (based on earlier literary sources, travellers' reports, and Tacitus's own indirect knowledge), a political commentary on Rome (which Tacitus depicts as corrupted by luxury, vice, and tyranny, contrasted with the virtuous austerity of the Germans), and — through its account of Germanic tribal institutions, marriage customs, and military culture — one of the most important primary sources for the reconstruction of early Germanic society.\n\nTacitus's characterisation of the Germanic tribes is a combination of factual description and moral idealisation — a tradition in classical ethnography (the 'noble savage' topos) that depicts the uncorrupted barbarian as a foil for the corrupted civilised society. The Germans are described as physically impressive, fiercely free, loyal to their oaths, chaste in marriage, and brave in battle — virtues that Roman society had lost. The famous passage on German women — 'Their marriages are strict, and their morals in no respect to be commended' (meaning, highly moral) — and on the sanctity of German marriage became influential in subsequent European discussions of gender and sexual morality.\n\nGermania's subsequent reception history is one of the most charged in Western intellectual history — its rediscovery in 1455 by the Florentine Humanist Enoch of Ascoli transformed it into the founding document of German national identity in the Renaissance and Reformation period, and it was used by German Humanists (Conrad Celtis, Ulrich von Hutten) to construct a proud German identity against Italian cultural condescension. In the 19th and 20th centuries, its description of the Germans as an ethnically pure (corpore ingentes — 'physically mighty'), blue-eyed, blond-haired race was catastrophically misappropriated by German nationalist and Nazi ideologues as scientific evidence for German racial purity and superiority.",
    "causes": [
      "Tacitus's political purpose — the presentation of Germanic virtues as an implicit critique of Roman imperial corruption — gave Germania its rhetorical structure: the idealised German is a moral mirror held up to a Rome degraded by luxury, despotism, and the suppression of political freedom. This is a classical ethnographic convention (the 'noble savage' topos) deployed for Roman political commentary.",
      "The Roman military crisis along the Rhine and Danube frontiers — the memory of the catastrophic Roman defeat in the Teutoburg Forest (9 CE), the ongoing resistance of Germanic tribes to Roman expansion, and the current campaigns of Domitian and Trajan against the Germans — gave Germania its political urgency as a geographical and military intelligence briefing about Rome's most dangerous neighbours.",
      "The tradition of Greek and Latin ethnography — Herodotus, Caesar's De Bello Gallico, Diodorus Siculus, Strabo's Geography — provided Tacitus with the literary conventions of ethnographic description (geography, customs, marriage, religion, military organisation) and the moralising interpretive framework within which he situated his description of the Germans."
    ],
    "effects": [
      "Germania's rediscovery (1455) and its use by German Renaissance Humanists — Conrad Celtis (who organised the Germania society), Ulrich von Hutten, and others — to construct a proud German cultural identity against Italian Humanist condescension initiated the long and fateful history of Tacitus's text as a founding document of German national consciousness.",
      "The misappropriation of Germania by 19th-century German nationalists and 20th-century Nazi ideologues — its description of the ancient Germans as physically superior, ethnically pure, and racially unmixed was used to construct a pseudo-scientific account of German racial destiny — made Tacitus's short ethnographic treatise one of the most catastrophically misused texts in the history of Western scholarship.",
      "Germania remains the primary literary source for the reconstruction of early Germanic society — its descriptions of tribal institutions (the comitatus, the role of women, the assembly, the sacral kingship), of religious practice, and of material culture, while ideologically shaped, contain invaluable evidence for the social history of the pre-Migration-Period Germanic world."
    ],
    "relationships": [
      {"sourceSlug": "tacitus", "sourceName": "Tacitus (c. 56–c. 120 CE)", "verb": "AUTHORS", "targetSlug": "germania", "targetName": "Germania (c. 98 CE)", "context": "Tacitus wrote Germania c. 98 CE — a short ethnographic treatise on the Germanic tribes east of the Rhine, drawing on earlier literary sources and indirect knowledge to construct both a descriptive account and an implicit moral critique of Rome."},
      {"sourceSlug": "germania", "sourceName": "Germania (rediscovery, 1455)", "verb": "FOUNDS", "targetSlug": "german-national-identity", "targetName": "German national cultural identity (Renaissance Humanism)", "context": "Germania's rediscovery by Enoch of Ascoli in 1455 and its use by Conrad Celtis and the German Humanists transformed it into the founding document of German national identity — the ancient text that demonstrated Germany's heroic pre-Roman heritage."},
      {"sourceSlug": "germania", "sourceName": "Germania (racial description)", "verb": "MISAPPROPRIATED_BY", "targetSlug": "nazi-ideology", "targetName": "Nazi racial ideology (20th century)", "context": "Tacitus's description of the ancient Germans as physically impressive and ethnically pure was catastrophically misappropriated by Nazi ideologues as pseudo-scientific evidence for German racial superiority — one of the most harmful misuses of a classical text in Western history."}
    ],
    "places": [
      {"name": "Roman Empire frontier (Rhine and Danube, c. 98 CE context)", "role": "The Rhine and Danube frontiers — where Roman armies faced the unconquered Germanic tribes — provided the military and political context for Germania as a combination of ethnographic description and military intelligence"},
      {"name": "Germany (Renaissance rediscovery and national use, 15th–20th centuries)", "role": "The long history of Germania's use and misuse in German culture — from Conrad Celtis's Renaissance celebrations of German virtus to Nazi racial ideology — is the most consequential example of classical text appropriation in European intellectual history"}
    ],
    "subjects": ["Roman History", "Classical Era", "Tacitus", "Ethnography", "Germanic Peoples", "Ancient Rome", "Latin Literature", "Primary Source"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Tacitus's Germania (c. 98 CE) is the primary literary source for early Germanic society and one of the most consequential ethnographic texts in Western history — used by Renaissance Humanists to found German national identity, and catastrophically misappropriated by Nazi ideologues as pseudo-scientific evidence for German racial purity. Its reception history from 1455 to the 20th century is the most charged of any classical text.",
      "significanceCategory": "highly-significant"
    }
  }
},

"exodus": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780exodus.json",
  "slug": "exodus",
  "data": {
    "summary": "The Book of Exodus is the second book of the Hebrew Bible (Torah/Pentateuch), traditionally attributed to Moses but understood by modern scholarship as a composite text compiled from multiple literary sources (the Documentary Hypothesis identifies the Yahwist, Elohist, Priestly, and Deuteronomic sources) and reaching its final form during the Babylonian exile period (c. 550–450 BCE). The book narrates the foundational story of Israelite religion and national identity: the enslavement of the Israelites in Egypt (under a Pharaoh 'who did not know Joseph'), the birth, upbringing, and call of Moses (the burning bush, Exodus 3: 'I AM WHO I AM'), the ten plagues by which God compels Pharaoh to release the Israelites, the Exodus from Egypt (the Passover, the crossing of the Red Sea), the giving of the Law at Mount Sinai (the Ten Commandments, Exodus 20), and the covenant between God and Israel.\n\nExodus is simultaneously the foundational narrative of Judaism, Christianity, and Islam — the story of divine liberation from slavery, the founding of the covenant relationship between God and a chosen people, and the revelation of the divine name (YHWH, 'I AM WHO I AM') — and one of the most influential narratives in Western political thought, in which the Exodus from Egypt became the paradigmatic story of liberation from oppression and the founding of a covenant community. Its influence on the political imagination is incalculable: from the Pilgrim Fathers who saw themselves as Israel crossing the Red Sea to the American promised land, to the liberation theology of Latin American Catholicism, to Martin Luther King Jr. and the African American civil rights movement ('Let my people go'), the Exodus story is the political myth of liberation that has structured political and religious movements across three millennia.\n\nThe Sinai revelation — the giving of the Ten Commandments and the Mosaic Law — is the foundational legal and ethical code of the Abrahamic traditions, and its influence on Western legal and moral thought (through Deuteronomy and the entire development of Jewish, Christian, and Islamic law) is immeasurable.",
    "causes": [
      "The Babylonian exile (c. 597–539 BCE) — when the Israelites were deported to Babylon following the Babylonian conquest of Jerusalem — provided the editorial context for the final compilation and theological shaping of the Exodus narrative: the story of liberation from Egyptian slavery was the narrative resource that sustained the exiled community's hope for return and restoration.",
      "The earlier oral and written traditions about Moses and the Exodus — whether reflecting historical memory of an actual Egyptian sojourn and exodus (disputed by modern Egyptology) or theological elaboration of foundational religious experience — were the literary materials that the Priestly and Deuteronomic editors shaped into the canonical Exodus narrative.",
      "The institution of Passover (Pesach) — the annual festival commemorating the night of the final plague and the departure from Egypt — was both the occasion for the ritual retelling of the Exodus story and the institutional framework that preserved and transmitted the narrative across generations, long before its canonical scriptural form."
    ],
    "effects": [
      "The Exodus narrative became the foundational political myth of the Western tradition — the paradigm of divine liberation from oppression and the founding of a covenant community — used to justify colonial settlement (the Puritans' 'city on a hill'), inspire revolutionary movements (the American and French Revolutions), and ground liberation theology (Latin American Catholic theology, African American civil rights rhetoric).",
      "The Ten Commandments (Exodus 20) are the foundational legal text of the Abrahamic traditions — their influence on the development of Jewish halakha, Christian canon law, and Islamic sharia, and through these on Western legal systems, is the most consequential legal contribution in human history.",
      "The Passover Seder — the ritual meal that retells the Exodus story ('We were slaves to Pharaoh in Egypt, and the LORD our God brought us out') — is the most widely practised Jewish ritual, observed by Jews worldwide for more than two thousand years and a model for subsequent liberation rituals (the Christian Eucharist as a New Exodus Passover, the civil rights movement's appropriation of Passover imagery)."
    ],
    "relationships": [
      {"sourceSlug": "exodus", "sourceName": "Book of Exodus", "verb": "PART_OF", "targetSlug": "torah", "targetName": "Torah/Pentateuch (Five Books of Moses)", "context": "Exodus is the second book of the Torah — the foundational five books of the Hebrew Bible — and contains the central narrative of Israelite religion: the Exodus from Egypt, the Passover, and the giving of the Law at Sinai."},
      {"sourceSlug": "exodus", "sourceName": "Book of Exodus (liberation narrative)", "verb": "INSPIRES", "targetSlug": "liberation-theology", "targetName": "Liberation theology and political liberation movements", "context": "The Exodus narrative has been the foundational political myth of liberation movements across three millennia — from the Puritan settlers to the African American civil rights movement ('Let my people go') to Latin American liberation theology."},
      {"sourceSlug": "exodus", "sourceName": "Book of Exodus (Ten Commandments)", "verb": "ESTABLISHES", "targetSlug": "mosaic-law", "targetName": "Mosaic Law and Abrahamic legal tradition", "context": "The Ten Commandments and the Mosaic Law given at Sinai (Exodus 20–23) are the foundational legal text of Judaism, Christianity, and Islam, and their influence on the development of Western legal systems through these traditions is immeasurable."}
    ],
    "places": [
      {"name": "Egypt and Sinai Peninsula (narrative setting)", "role": "The narrative geography of the Exodus — Egypt as the land of slavery, the Red Sea as the boundary of liberation, Mount Sinai as the place of divine revelation — which has shaped the sacred geography of the Abrahamic traditions"},
      {"name": "Babylon (c. 597–539 BCE, probable final compilation context)", "role": "The Babylonian exile — when the deportation of the Israelites created the urgent need to preserve and transmit the foundational narrative of divine liberation — is the probable context for the final compilation and theological shaping of the Exodus narrative"}
    ],
    "subjects": ["Hebrew Bible", "Classical Era", "Biblical Literature", "Judaism", "Christianity", "Islam", "Ancient Israel", "Law"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Book of Exodus is one of the most consequential texts in human history — the foundational narrative of Israelite/Jewish identity, the source of the Ten Commandments that underlie the legal traditions of Judaism, Christianity, and Islam, and the political myth of liberation from slavery that has inspired revolutionary movements across three millennia. The Exodus story is the single most widely retold narrative of liberation in the Western tradition.",
      "significanceCategory": "world-changing"
    }
  }
},

"chronicles-froissart": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781chronicles-froissart.json",
  "slug": "chronicles-froissart",
  "data": {
    "summary": "The Chronicles (French: Chroniques) is the historical narrative of Jean Froissart (c. 1337–c. 1405), composed over approximately five decades (c. 1370–1400) and covering European history from 1325 to 1400 — the primary narrative source for the first phase of the Hundred Years' War between England and France, the Black Prince's campaigns, the Battles of Crécy (1346) and Poitiers (1356), the Black Death's impact on European society, the Peasants' Revolt in England (1381), and the chivalric culture of the late medieval aristocracy. Froissart travelled extensively — he was personally acquainted with Edward III and the Black Prince of England, with Jean II of France, with Charles V, and with the great lords of all parties — and his Chronicles is a remarkable work of oral history, combining eyewitness accounts from participants with Froissart's own observations and his chivalric values.\n\nFroissart's Chronicles is the greatest monument of late medieval chivalric historiography — its celebration of the knightly virtues (prowess, courtesy, loyalty, largesse) of the great lords on all sides of the Hundred Years' War, its vivid narrative of battles, tournaments, and diplomatic encounters, and its portrait of the chivalric culture of the 14th-century European aristocracy constitute one of the most vivid and detailed accounts of medieval aristocratic life in existence. Froissart is a partisan (he rewrote his first book multiple times as his patronage changed between English, French, and Flemish lords), but his partiality is itself a historical document of the chivalric culture he chronicled — a culture in which honour, display, and the values of the warrior aristocracy shaped both the conduct of war and the writing of history.\n\nFroissart's Chronicles survived in 150 manuscript copies (an extraordinary number for a medieval text) and was first printed by William Caxton c. 1523 — its influence on subsequent European historiography, on the development of the chivalric romance, and on the popular imagination of the Middle Ages (Walter Scott, Conan Doyle, and countless subsequent historical novelists drew on Froissart) has been enormous.",
    "causes": [
      "Froissart's patronage by the great aristocratic courts of 14th-century Europe — he was clerk and poet at the court of Queen Philippa of England (wife of Edward III), then dependent on successive Flemish, French, and English patrons — gave him both the access and the incentive to produce a chronicle of the European aristocracy, with whom he shared the chivalric values he celebrated.",
      "The Hundred Years' War (1337–1453) — the defining conflict of 14th-century European history, involving England, France, Burgundy, Castile, and their numerous allies and enemies in a generation-spanning struggle for the French throne and the control of European trade — provided Froissart with the central subject of his Chronicles and the dramatic narrative of battles, sieges, and political crises that give it its scope.",
      "The late medieval chivalric culture — the elaborate ceremonial, tournament, and heraldic culture of the European aristocracy in its late medieval flowering — provided Froissart with his interpretive framework: the conviction that the great lords' virtue, prowess, and honour are the meaningful content of history, and that the chronicler's task is to celebrate and preserve the deeds of those who achieved true chivalric distinction."
    ],
    "effects": [
      "Froissart's Chronicles is the primary narrative source for the history of the first phase of the Hundred Years' War and the chivalric culture of the late medieval European aristocracy — his eyewitness accounts of Crécy (1346) and Poitiers (1356), his portraits of Edward III and the Black Prince, and his descriptions of the siege of Calais and the rise of the condottieri are irreplaceable historical evidence.",
      "Froissart's portrait of late medieval chivalric culture — the tournaments, the heraldic ceremonies, the elaborate codes of honour and courtesy — became the primary source for subsequent Romanticised images of the Middle Ages, directly influencing Walter Scott, Arthur Conan Doyle, and the 19th-century revival of medieval chivalric ideals in literature and visual art.",
      "The Chronicles' survival in 150 manuscript copies and its early printing by Caxton demonstrate the extraordinary popularity of Froissart's work in late medieval and early modern Europe — its influence on the development of national historical narratives in France, England, and Flanders, and on the tradition of chronicle historiography, was enormous."
    ],
    "relationships": [
      {"sourceSlug": "jean-froissart", "sourceName": "Jean Froissart (c. 1337–c. 1405)", "verb": "AUTHORS", "targetSlug": "chronicles-froissart", "targetName": "Chronicles (c. 1370–1400)", "context": "Froissart composed his Chronicles over approximately five decades, constantly revising and expanding his work as his patronage and perspective shifted — the most important chronicle of 14th-century European history."},
      {"sourceSlug": "chronicles-froissart", "sourceName": "Chronicles", "verb": "DOCUMENTS", "targetSlug": "hundred-years-war", "targetName": "Hundred Years' War (1337–1453, early phase)", "context": "Froissart's Chronicles is the primary narrative source for the first phase of the Hundred Years' War — his accounts of Crécy, Poitiers, the siege of Calais, and the Black Prince's campaigns are the most detailed contemporary narratives of these events."},
      {"sourceSlug": "chronicles-froissart", "sourceName": "Chronicles", "verb": "INSPIRES", "targetSlug": "medieval-revival-literature", "targetName": "19th-century medieval revival (Walter Scott, historical fiction)", "context": "Froissart's vivid portrait of chivalric culture became the primary source for the 19th-century Romantic revival of medieval ideals — Walter Scott drew on Froissart extensively, and his Chronicles is the foundation of the popular image of medieval chivalric Europe."}
    ],
    "places": [
      {"name": "England, France, and Flanders (Froissart's circuit of patronage)", "role": "Froissart's extraordinary mobility across the courts of 14th-century Europe — from England's Philippa of Hainault to the French court, Flemish lords, and back — gave his Chronicles its remarkable scope and its portrait of the entire European chivalric world"},
      {"name": "Crécy (1346) and Poitiers (1356, battle sites)", "role": "The two great English victories of the early Hundred Years' War — whose narrative in Froissart's Chronicles is the most vivid and detailed contemporary account of medieval pitched battle"}
    ],
    "subjects": ["Medieval History", "Medieval Era", "Hundred Years' War", "French Literature", "Chivalry", "England", "France", "Primary Source"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Froissart's Chronicles (c. 1370–1400) is the greatest monument of late medieval chivalric historiography and the primary narrative source for the first phase of the Hundred Years' War. Its portrait of 14th-century European aristocratic culture — the battles of Crécy and Poitiers, the Black Prince's campaigns, the Peasants' Revolt — became the foundation of the Romantic image of medieval chivalric Europe, directly influencing Walter Scott and the 19th-century medieval revival.",
      "significanceCategory": "highly-significant"
    }
  }
},

"alices-adventures-in-wonderland": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783alices-adventures-in-wonderland.json",
  "slug": "alices-adventures-in-wonderland",
  "data": {
    "summary": "Alice's Adventures in Wonderland is the novel by Lewis Carroll (Charles Lutwidge Dodgson, 1832–1898), published by Macmillan in November 1865 — one of the most famous children's books ever written and one of the most widely adapted, translated, and culturally influential texts in the English literary tradition. The story was first told on 4 July 1862, during a rowing trip on the Thames near Oxford by the Rev. Dodgson and his colleague Robinson Duckworth to three young girls — Alice Liddell (aged 10) and her sisters — with Alice asking Dodgson to write it down; the written version (originally titled Alice's Adventures Under Ground) was expanded and published with John Tenniel's illustrations. The novel follows Alice, a seven-year-old girl who falls down a rabbit hole into Wonderland — a world governed by dream logic in which size changes, playing card figures come alive, and the Queen of Hearts shouts 'Off with their heads!' — encountering the White Rabbit, the Cheshire Cat, the Mad Hatter and the March Hare at their perpetual tea party, and finally the Duchess and the Queen of Hearts before waking from the dream.\n\nAlice in Wonderland is simultaneously a children's adventure story and a sophisticated literary creation that operates at multiple levels: as a satire on Victorian educational practices and social conventions (the pompous and irrational adults of Wonderland parody the adults of Victorian society); as a philosophical meditation on identity, language, and logic (Carroll was a mathematician and logician, and the novel is full of logical paradoxes and linguistic games); and as a psychologically rich dream narrative that anticipates Freudian dream interpretation. Carroll's portmanteau words ('brillig', 'slithy', 'frabjous'), his logical paradoxes (the Cheshire Cat's grin that remains when the cat disappears), and his absurdist humour have influenced generations of writers, illustrators, and thinkers.\n\nAlice's cultural influence is incalculable — the novel has been translated into more than 100 languages, adapted into more than 40 films and television productions (including Disney's 1951 animated feature), and its imagery (the rabbit hole, the 'down the rabbit hole' metaphor, the mad tea party, 'Off with their heads!', the Cheshire Cat) has become embedded in Western cultural vocabulary.",
    "causes": [
      "Lewis Carroll's relationship with Alice Liddell and his talent for improvisatory storytelling — his ability to produce fantastical, logically consistent narratives on the spot during their boat trips and croquet games — gave Alice in Wonderland its origin in a specific creative moment (4 July 1862) and its quality of improvised dream narrative.",
      "Carroll's mathematical and logical training — he was a lecturer in mathematics at Christ Church, Oxford, whose serious work was in mathematical logic (Symbolic Logic, 1896) — gave Alice in Wonderland its underlying structure of logical paradox and linguistic play: the 'Drink Me' bottle, the 'Eat Me' cake, the Cheshire Cat's dissolution, and the Queen's arbitrary rule are all explorations of the limits of logical and linguistic convention.",
      "Victorian children's literature — a genre undergoing rapid development in the 1860s, with the increasing specialisation of children's books and the growing seriousness of their artistic and intellectual ambitions — provided both the market and the cultural context for Alice in Wonderland: its original audience was the literate Victorian middle class, and its success transformed the genre."
    ],
    "effects": [
      "Alice in Wonderland established the tradition of literary nonsense as a serious and sophisticated genre — Carroll's linguistic games, logical paradoxes, and absurdist humour influenced Edward Lear (a contemporary), the Surrealist movement (which adopted Carroll as a precursor), and the entire 20th-century tradition of literary nonsense from Edward Gorey through Douglas Adams to contemporary children's literature.",
      "The metaphors and images of Alice in Wonderland have become embedded in English cultural vocabulary — 'down the rabbit hole', 'Wonderland', 'the Mad Hatter', 'Off with her head!', 'curiouser and curiouser' — making Carroll's invention among the most culturally productive in the history of English children's literature.",
      "Alice in Wonderland's influence on cinema, visual art, and popular culture has been continuous since the 1930s — from the Disney animated feature (1951) through Tim Burton's 2010 live-action adaptation through countless versions in animation, theatre, and digital media — making Alice one of the most recognisable fictional characters in world culture."
    ],
    "relationships": [
      {"sourceSlug": "lewis-carroll", "sourceName": "Lewis Carroll (Charles Dodgson, 1832–1898)", "verb": "AUTHORS", "targetSlug": "alices-adventures-in-wonderland", "targetName": "Alice's Adventures in Wonderland (1865)", "context": "Carroll created Alice's Adventures in Wonderland originally as an improvised story for Alice Liddell on 4 July 1862, expanded it into the published novel with Tenniel's illustrations and published it in 1865."},
      {"sourceSlug": "alices-adventures-in-wonderland", "sourceName": "Alice in Wonderland", "verb": "ESTABLISHES", "targetSlug": "literary-nonsense-genre", "targetName": "Literary nonsense as a serious genre (Surrealism, absurdism)", "context": "Carroll's linguistic games, logical paradoxes, and dream logic influenced the Surrealist movement's adoption of Carroll as a precursor and the entire tradition of literary nonsense and absurdism in 20th-century literature."},
      {"sourceSlug": "alices-adventures-in-wonderland", "sourceName": "Alice in Wonderland", "verb": "PRECEDES", "targetSlug": "through-the-looking-glass", "targetName": "Through the Looking-Glass (Carroll, 1871)", "context": "Alice's Adventures in Wonderland was followed by Through the Looking-Glass (1871) — its sequel, in which Alice enters a world structured like a chess game — together forming the canonical Alice texts."}
    ],
    "places": [
      {"name": "Oxford and Thames River (4 July 1862, origin story)", "role": "The river Cherwell near Oxford — where Carroll first told the Alice story to Alice Liddell and her sisters during a rowing trip — is the biographical origin of Alice in Wonderland"},
      {"name": "Victorian England (1865, publication context)", "role": "Victorian England in the 1860s — the period of rapid development of children's literature, the great expansion of literate middle-class readership, and the seriousness with which the Victorians took the education and imagination of children — provided the cultural context for Alice's immediate success"}
    ],
    "subjects": ["English Literature", "Modern Era", "Lewis Carroll", "Children's Literature", "Victorian Literature", "Fantasy", "19th Century", "Nonsense Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Alice's Adventures in Wonderland (Lewis Carroll, 1865) is one of the most culturally influential books in the English language — establishing literary nonsense as a sophisticated genre, embedding its imagery ('down the rabbit hole', the Mad Hatter, 'Off with her head!') in global cultural vocabulary, and influencing Surrealism, absurdism, and a century of children's literature. Translated into over 100 languages and adapted into over 40 films, it is among the most widely known fictional works ever written.",
      "significanceCategory": "world-changing"
    }
  }
},

"all-quiet-on-the-western-front": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783all-quiet-on-the-western-front.json",
  "slug": "all-quiet-on-the-western-front",
  "data": {
    "summary": "All Quiet on the Western Front (German: Im Westen nichts Neues, literally 'Nothing New in the West') is the anti-war novel by Erich Maria Remarque (1898–1970), published in November 1928 in the Vossische Zeitung (Germany's most prestigious newspaper) and as a book by Ullstein Verlag in January 1929 — one of the best-selling and most influential novels of the 20th century, with approximately 20 million copies sold worldwide. The novel is narrated by Paul Bäumer, an 18-year-old German schoolboy who enlists enthusiastically with his classmates following their teacher's patriotic exhortations, only to find the Western Front a hell of artillery, mud, poison gas, and meaningless death. Over the course of the novel, Paul watches his comrades die one by one, loses all connection to civilian life (unable to communicate what the war is like when he returns home on leave), and is himself killed on a quiet day in October 1918 — a month before the Armistice — in one of the most famous ironic endings in modern fiction: 'He had fallen forward and lay on the earth as though sleeping. Turning him over one saw that he could not have suffered long; his face had an expression of calm, as though almost glad the end had come.'\n\nAll Quiet on the Western Front was the first major anti-war novel from the German perspective and one of the most powerful anti-war statements in any language — its refusal of heroism, its portrayal of the physical horror of trench warfare (the gas attacks, the shelling, the rotting corpses), its documentation of the destruction of a generation of young men by an incomprehensible military machine, and its indictment of the older generation who sent the young to die while remaining safely at home ('While they continued to write and talk, we saw the wounded and dying. While they taught that duty to one's country is the greatest thing, we already knew that death-fear is still greater.') made it simultaneously a sensation and a political object.\n\nIn Germany, All Quiet was an immediate bestseller — 500,000 copies in its first week — but also a political lightning rod: the nationalist right attacked it as a slander on German soldiers, and when the Nazis came to power, it was among the first books publicly burned (Berlin, 10 May 1933). Remarque was stripped of German citizenship, and the novel was banned in Germany and Austria. The 1930 Hollywood film adaptation (directed by Lewis Milestone) won the Academy Award for Best Picture.",
    "causes": [
      "Remarque's own service in the German army in World War I — he was conscripted at 18, served on the Western Front, was wounded five times, and lost most of his school friends in the war — gave All Quiet its autobiographical authority and its portrait of the soldier's experience from the inside: the novel is addressed to the generation of young men who were, like Remarque, destroyed by a war they had been taught to embrace.",
      "The late Weimar Republic's political culture — the intense debate about the legacy of World War I, the conflict between the nationalists who insisted the German army had been 'stabbed in the back' and those who saw the war as catastrophic waste — gave All Quiet its explosive political reception: its publication was a political act as much as a literary one, entering directly into the debate about Germany's recent history.",
      "The tradition of European war literature emerging from World War I — the poetry of Sassoon, Owen, and Graves; the memoirs of Robert Graves (Goodbye to All That, 1929) and Siegfried Sassoon; and the earlier German war literature — provided the literary context in which All Quiet appeared, as the German contribution to the extraordinary wave of anti-war writing that 1929 produced (also the year of Hemingway's A Farewell to Arms)."
    ],
    "effects": [
      "All Quiet on the Western Front is the most widely read anti-war novel in the history of literature — its 20 million copies and its translation into dozens of languages have made it the canonical fictional statement of World War I as catastrophic waste of young lives, and its influence on the 20th-century perception of the Great War is comparable to Sassoon's and Owen's poetry.",
      "The Nazi burning of All Quiet on 10 May 1933 — one of the most famous acts of book burning in modern history — made the novel a symbol of the conflict between literature and totalitarian censorship, and Remarque's stripping of German citizenship made him the most prominent German literary exile of the Third Reich.",
      "The 1930 Hollywood film adaptation — which won the Academy Award for Best Picture and was one of the most successful early sound films — transformed All Quiet from a German literary sensation into a global cultural event, and together with A Farewell to Arms established the cinematic genre of the anti-war film that runs through Apocalypse Now (1979) to present."
    ],
    "relationships": [
      {"sourceSlug": "erich-maria-remarque", "sourceName": "Erich Maria Remarque (1898–1970)", "verb": "AUTHORS", "targetSlug": "all-quiet-on-the-western-front", "targetName": "All Quiet on the Western Front (1929)", "context": "Remarque wrote All Quiet on the Western Front drawing on his own experience of the Western Front — the novel is the most powerful literary account of World War I from the German perspective and one of the best-selling novels of the 20th century."},
      {"sourceSlug": "all-quiet-on-the-western-front", "sourceName": "All Quiet on the Western Front", "verb": "CONTEMPORARY_WITH", "targetSlug": "a-farewell-to-arms", "targetName": "A Farewell to Arms (Hemingway, 1929)", "context": "All Quiet (published January 1929) and A Farewell to Arms (published September 1929) together constitute the defining wave of anti-war fiction of 1929 — the German and American perspectives on World War I published in the same year, each the canonical anti-war novel of its national literary tradition."},
      {"sourceSlug": "all-quiet-on-the-western-front", "sourceName": "All Quiet on the Western Front", "verb": "BANNED_BY", "targetSlug": "nazi-germany", "targetName": "Nazi Germany (book burning, 10 May 1933)", "context": "All Quiet was among the first books publicly burned by the Nazis on 10 May 1933 — making Remarque's novel the canonical symbol of the conflict between anti-war literature and totalitarian nationalism."}
    ],
    "places": [
      {"name": "Western Front, France and Belgium (1914–1918, narrative setting)", "role": "The Western Front — the trench warfare of northern France and Belgium, with its poison gas, artillery barrages, and meaningless infantry charges — is the setting of All Quiet and the world that destroys Paul Bäumer's generation"},
      {"name": "Germany (1929 publication, Nazi burning 1933)", "role": "The Weimar Republic context of All Quiet's publication (a political sensation in the debate about World War I's legacy) and the Nazi Germany context of its burning (10 May 1933) — making the novel a defining document of both Weimar culture and Nazi censorship"}
    ],
    "subjects": ["German Literature", "Modern Era", "World War I", "Anti-War Literature", "20th Century", "Remarque", "War Literature", "German History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "All Quiet on the Western Front (Remarque, 1929) is the most widely read anti-war novel in history — its portrayal of World War I's destruction of a generation of young German soldiers shaped the 20th-century perception of the Great War as catastrophic waste. Its Nazi burning in 1933 made it the canonical symbol of the conflict between anti-war literature and totalitarian censorship. Together with A Farewell to Arms (also 1929), it defines the literary response to the First World War.",
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
