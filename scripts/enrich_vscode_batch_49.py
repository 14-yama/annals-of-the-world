#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 49 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: stabat-mater, the-government-inspector, the-threepenny-opera,
          the-tale-of-the-bamboo-cutter, the-raven, vande-mataram, salome, watchmen
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-49-may2026"

ENRICHMENTS = {

"stabat-mater": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780stabat-mater.json",
  "slug": "stabat-mater",
  "data": {
    "summary": "The Stabat Mater (Latin: 'The Mother Was Standing') is a medieval Catholic hymn attributed to the Italian Franciscan poet Jacopone da Todi (c. 1230–1306 CE), composed c. 1290–1300 CE and one of the most celebrated and widely set texts in the history of Western sacred music. The hymn consists of 20 stanzas in rhymed Latin verse describing the grief of the Virgin Mary at the foot of the cross during the crucifixion of Jesus — presenting a meditation on compassion (compassio), suffering, and the devotion of the believer who seeks to share in Mary's grief and in Christ's passion. The hymn begins: 'Stabat mater dolorosa / Iuxta crucem lacrimosa / Dum pendebat filius' ('The grieving mother was standing / Weeping beside the cross / While her Son was hanging there').\n\nThe Stabat Mater was widely used in Catholic liturgy and devotion — it was adopted as a sequence for the Feast of the Seven Sorrows of Our Lady and for the Stations of the Cross. Its text was set to music by virtually every major European composer from the 14th century to the 20th: Giovanni da Palestrina (c. 1590), Agostino Steffani, Alessandro Scarlatti, Vivaldi (1712), Pergolesi (1736 — the most performed setting, composed in the last weeks of his life), Haydn (1767), Boccherini, Schubert (1816), Rossini (1832/1841), Dvořák (1877), Verdi (1898), and Poulenc (1950/1951), among many others — making it the most multiply-composed Latin text other than the Mass and the Magnificat.\n\nThe Stabat Mater is a supreme expression of medieval Franciscan affective piety — the devotional tradition, pioneered by Francis of Assisi and his followers, that emphasised emotional identification with the suffering Christ and the grieving Mary as the primary method of spiritual growth. Its influence extended beyond Catholic devotion to Protestant musical culture (J.S. Bach's Widerstehe doch der Sünde is a parody of Pergolesi's Stabat Mater) and to the broader tradition of Western sacred art.",
    "causes": [
      "The Franciscan affective piety movement — Francis of Assisi's revolutionary emphasis on emotional identification with the suffering Christ (the stigmata, the crucifix, the Nativity scene) as the path to spiritual transformation — provided the theological and devotional framework for the Stabat Mater's meditation on compassion with Mary at the foot of the cross.",
      "The development of the medieval sequence as a liturgical genre — the tradition of elaborate poetic texts composed for singing at Mass after the Alleluia — provided the literary form for the Stabat Mater, which was adopted as a liturgical sequence after initially circulating as a popular devotional poem.",
      "The cult of the Virgin Mary and its emotional dimension in late medieval Catholicism — the development of the Seven Sorrows of Mary as a devotional focus, and the broader medieval interest in Mary's compassion (compassio Mariae) as a model for the Christian's emotional participation in salvation — provided the devotional context for the hymn."
    ],
    "effects": [
      "The Stabat Mater became the most multiply-composed Latin text in Western music history (outside the Mass and Magnificat) — from Palestrina through Vivaldi, Pergolesi, Haydn, Schubert, Rossini, Dvořák, and Poulenc, virtually every major European composer set the text, making it a sustained creative stimulus across six centuries of Western musical composition.",
      "Pergolesi's Stabat Mater (1736) — composed in the last weeks of his life, when he was dying of tuberculosis at age 26 — became the most performed sacred music of the 18th century: it was the most frequently copied manuscript music in the century (over 100 extant copies), transcribed by J.S. Bach as his BWV 1083, and remained the most popular orchestral sacred work in the concert repertoire for decades.",
      "The Stabat Mater's text and its settings established the grief of the Virgin Mary at the cross as a central aesthetic subject in Western art — from medieval sculpture (Pietà) through opera (the influence of Pergolesi's Stabat Mater on the development of the operatic aria) to the concert hall, Mary's compassion at the cross was one of the most productively generative themes in Western sacred art."
    ],
    "relationships": [
      {"sourceSlug": "jacopone-da-todi", "sourceName": "Jacopone da Todi (c. 1230–1306, Italian Franciscan poet)", "verb": "AUTHORS", "targetSlug": "stabat-mater", "targetName": "Stabat Mater (c. 1290–1300 CE, 20 stanzas, most-set Latin text)", "context": "Jacopone da Todi composed the Stabat Mater c. 1290–1300 CE — it became the most multiply-composed Latin text in Western music history, set by Vivaldi, Pergolesi, Haydn, Schubert, Rossini, Dvořák, and Poulenc among others."},
      {"sourceSlug": "stabat-mater", "sourceName": "Stabat Mater (Pergolesi 1736 — most performed 18th-century sacred music)", "verb": "INSPIRES", "targetSlug": "giovanni-battista-pergolesi", "targetName": "Giovanni Battista Pergolesi (1710–1736, Italian composer)", "context": "Pergolesi's Stabat Mater (1736) — composed as he was dying at age 26 — became the most performed sacred music of the 18th century, transcribed by J.S. Bach (BWV 1083) and copied in over 100 manuscripts."},
      {"sourceSlug": "stabat-mater", "sourceName": "Stabat Mater (Franciscan affective piety — Mary's grief as devotional model)", "verb": "EXEMPLIFIES", "targetSlug": "franciscan-affective-piety", "targetName": "Franciscan affective piety and compassio Mariae tradition", "context": "The Stabat Mater is the supreme literary expression of Franciscan affective piety — the devotional tradition (pioneered by Francis of Assisi) emphasising emotional identification with the suffering Christ and the grieving Mary as the path to spiritual transformation."}
    ],
    "places": [
      {"name": "Italy (Jacopone da Todi, Umbria c. 1290–1300; Franciscan devotional tradition)", "role": "The Stabat Mater was composed in Umbria, Italy by the Franciscan Jacopone da Todi c. 1290–1300 CE — the heartland of the Franciscan movement that developed affective piety"},
      {"name": "Europe (Catholic liturgy, Stations of the Cross; every major composer — Vivaldi, Pergolesi, Haydn, Rossini, Dvořák)", "role": "The Stabat Mater was adopted across Catholic Europe as a liturgical sequence and devotional text — set by virtually every major European composer from the 14th to the 20th century"}
    ],
    "subjects": ["Latin Literature", "Medieval Era", "Catholic Liturgy", "Sacred Music", "Franciscan Spirituality", "Marian Devotion", "Church Music", "Italian Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Stabat Mater (Jacopone da Todi, c. 1290–1300 CE) is the most multiply-composed Latin text in Western music history — set by Vivaldi, Pergolesi, Haydn, Schubert, Rossini, Dvořák, and Poulenc, among many others. Pergolesi's 1736 setting became the most performed sacred music of the 18th century; the text's sustained creative stimulus across six centuries makes it one of the most generative texts in the history of Western sacred art.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-government-inspector": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-government-inspector.json",
  "slug": "the-government-inspector",
  "data": {
    "summary": "The Government Inspector (Russian: Ревизор, Revizor) is a satirical comedy in five acts by the Ukrainian-Russian writer Nikolai Gogol (1809–1852), first performed at the Alexandrinsky Theatre in St Petersburg on 19 April 1836 and published in the same year. It is the most celebrated Russian comedy and one of the great works of satirical drama in any language. The play depicts the corrupt officials of a small provincial Russian town who mistake a penniless and fraudulent official (Khlestakov) for the feared government inspector (revizor) from St Petersburg — the inspector who has come to audit their corrupt practices. The officials' terror of exposure drives them to bribe and flatter Khlestakov, who accepts their money and flattery without understanding what he is supposed to be, until he is exposed and the real government inspector arrives.\n\nThe Government Inspector is a masterpiece of comic mechanism — its plot is driven entirely by the terror of the officials' guilty consciences, not by any deception on Khlestakov's part (he barely understands what is happening). Gogol's satirical technique is the exposure of the universal desire to seem rather than to be: all the characters, including Khlestakov, are performing versions of themselves for an audience they wish to impress or fear. The play ends with the famous 'mute scene' — the arrival of the real inspector is announced, and all the characters freeze in attitudes of horror, held in a tableaux for ninety seconds that Gogol specified should last long enough to become uncomfortable.\n\nGogol insisted that the Government Inspector was not a satire of Russia specifically but of 'that spiritual city which is built up in every one of us'. Tsar Nicholas I reportedly enjoyed the play, remarking 'Everybody got it — and I most of all!', while the liberal intelligentsia celebrated it as an indictment of Tsarist corruption. The play directly influenced the tradition of Russian satirical writing and theatrical comedy from Chekhov through the Soviet era.",
    "causes": [
      "Gogol's satire of Russian provincial bureaucratic corruption — his experience of the grotesque incompetence, vanity, and venality of Russian provincial officials, and his acute observation of the social performance of status in a hierarchical society — provided the social material for the play.",
      "Alexander Pushkin's suggestion (1835) — Pushkin reportedly told Gogol the story of a traveller mistaken for an official inspector, which provided the central comic premise — gave Gogol the plot around which he built his satirical mechanism.",
      "The Russian theatrical tradition's need for a native comedy of social manners — the absence of a great Russian comedy comparable to Molière or Sheridan — created the cultural space for Gogol's play, which achieved immediate and lasting canonical status as the Russian comedy."
    ],
    "effects": [
      "The Government Inspector established Gogol as the supreme Russian satirist and the founding figure of the Russian 'natural school' of literature — the tradition of social realism and satirical observation of Russian provincial and bureaucratic life that shaped Turgenev, Dostoyevsky, and Chekhov.",
      "The 'mute scene' — the final frozen tableau when the real inspector's arrival is announced — became one of the most famous theatrical devices in Russian drama, widely analysed as a symbol of collective guilt, social paralysis, and the moment when reality interrupts performance.",
      "The Government Inspector's satirical framework — the corrupt provincial town as a microcosm of the Russian state, the terror of accountability driving the officials' self-exposure — became the paradigm for Russian social satire from Saltykov-Shchedrin through the Soviet dissident tradition (Bulgakov, Zoshchenko, Erofeev)."
    ],
    "relationships": [
      {"sourceSlug": "nikolai-gogol", "sourceName": "Nikolai Gogol (1809–1852, Ukrainian-Russian writer)", "verb": "AUTHORS", "targetSlug": "the-government-inspector", "targetName": "The Government Inspector (Revizor, first performed 19 April 1836, St Petersburg)", "context": "Gogol's Government Inspector premiered at the Alexandrinsky Theatre on 19 April 1836 — the most celebrated Russian comedy, establishing Gogol as the supreme satirist of Russian provincial bureaucratic life."},
      {"sourceSlug": "the-government-inspector", "sourceName": "Government Inspector (natural school, social satire — provincial Russia)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "russian-natural-school", "targetName": "Russian 'natural school' (social realism, Turgenev, Dostoyevsky, Chekhov)", "context": "The Government Inspector established Gogol as the founding figure of the Russian 'natural school' — the tradition of social realism and satirical observation that shaped Turgenev, Dostoyevsky, and Chekhov."},
      {"sourceSlug": "the-government-inspector", "sourceName": "Government Inspector (mute scene — collective guilt, social paralysis)", "verb": "INFLUENCES", "targetSlug": "russian-theatre", "targetName": "Russian theatrical tradition (Chekhov, Bulgakov, Soviet satirical drama)", "context": "The Government Inspector's 'mute scene' and its satirical framework shaped Russian theatrical tradition — from Chekhov's use of social comedy through Soviet dissident satire (Bulgakov, Zoshchenko)."}
    ],
    "places": [
      {"name": "St Petersburg, Russia (Alexandrinsky Theatre, first performance 19 April 1836)", "role": "The Government Inspector was first performed at the Alexandrinsky Theatre in St Petersburg on 19 April 1836 — Tsar Nicholas I was reportedly in attendance and enjoyed the play"},
      {"name": "Fictional provincial Russian town (satirical microcosm of the Russian state)", "role": "The play is set in an unnamed provincial Russian town — a microcosm of the Russian state's corruption, serving as the setting for Gogol's satirical dissection of bureaucratic venality and social performance"}
    ],
    "subjects": ["Russian Literature", "Modern Era", "Nikolai Gogol", "Satirical Comedy", "Russian Theatre", "Social Satire", "Drama", "19th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Government Inspector (Gogol, 1836) is the most celebrated Russian comedy and the founding text of Russian satirical literature. Its savage dissection of provincial bureaucratic corruption, its famous 'mute scene', and its influence on the Russian 'natural school' (Turgenev, Dostoyevsky, Chekhov) make it one of the most consequential works of Russian culture. Gogol's satirical method — guilt-driven self-exposure, the comedy of social performance — shaped Russian literature for two centuries.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-threepenny-opera": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-threepenny-opera.json",
  "slug": "the-threepenny-opera",
  "data": {
    "summary": "The Threepenny Opera (German: Die Dreigroschenoper) is a 'play with music' in a prologue and three acts by the German playwright and poet Bertolt Brecht (1898–1956), with music by Kurt Weill (1900–1950), first performed at the Theater am Schiffbauerdamm in Berlin on 31 August 1928. It is based on John Gay's The Beggar's Opera (1728) — adapting and updating Gay's satirical ballad opera to the Weimar Republic — and is the most successful theatrical work of the Weimar era: running for 350 performances in its first Berlin production, it was translated into 18 languages within a year and has been continuously performed since 1928. It is the supreme example of Brecht's 'epic theatre' and the most widely performed German-language play of the 20th century.\n\nThe Threepenny Opera follows the criminal Macheath (Mack the Knife — Mackie Messer), who secretly marries Polly Peachum, daughter of the 'king of the beggars' Peachum — who controls London's begging industry. Peachum informs the police, Macheath is arrested, escapes with the help of his former girlfriend Jenny, is re-arrested, and is about to be hanged when a royal messenger arrives on horseback to reprieve him and give him a noble title — a parodic happy ending that Brecht uses to expose the arbitrary nature of bourgeois justice and the complicity of society's respectable institutions with criminality. The play's central argument — 'What is robbing a bank compared to founding one?' — is its definitive statement of the moral equivalence between crime and capitalism.\n\nKurt Weill's music — a synthesis of jazz, cabaret, tango, Baroque pastiche, and music hall, combining tonal accessibility with Brechtian alienation effects — created a new musical theatre idiom. 'Mack the Knife' (Die Moritat von Mackie Messer) became one of the most recorded popular songs of the 20th century (Louis Armstrong's 1956 recording, Bobby Darin's 1959 recording).",
    "causes": [
      "John Gay's The Beggar's Opera (1728) — the satirical ballad opera that used popular tunes to mock Italian opera and the conventions of theatrical romance — provided the direct model and source text for The Threepenny Opera: Brecht and Weill updated Gay's London criminals to Weimar Berlin, keeping the structural satirical logic but replacing Gay's popular tunes with Weill's jazz-inflected score.",
      "The Weimar Republic's theatrical culture — the extraordinary density of avant-garde theatrical innovation in 1920s Berlin (Piscator's political theatre, the Volksbühne, the commercial boulevard theatre) and the cabaret tradition — provided the artistic environment for The Threepenny Opera's combination of political satire, cabaret song, and theatrical experiment.",
      "Brecht's development of 'epic theatre' (episches Theater) — the theory of a theatre that alienates the audience from emotional identification with the characters in order to produce critical reflection (Verfremdungseffekt, the alienation effect) — found its first major popular realisation in The Threepenny Opera, which uses the musical numbers, direct address, and parodic happy ending to distance the audience from the narrative."
    ],
    "effects": [
      "The Threepenny Opera was the most commercially successful theatrical work of the Weimar era — its 350-performance Berlin run, immediate translation into 18 languages, and subsequent global performance history established Brecht as an international theatrical figure and demonstrated that political theatre could also be popular entertainment.",
      "'Mack the Knife' (Die Moritat von Mackie Messer) became one of the most recorded popular songs of the 20th century — recorded by Louis Armstrong (1956), Bobby Darin (1959, Grammy Award), Ella Fitzgerald, Frank Sinatra, and hundreds of others, it achieved a commercial life entirely separate from its theatrical context.",
      "The Threepenny Opera's concept of epic theatre — the alienation effect, the use of music to interrupt rather than intensify emotion, the exposure of theatrical conventions — became the dominant theoretical framework for politically engaged theatre worldwide, influencing the Living Theatre, theatre of the oppressed (Boal), and post-dramatic theatre."
    ],
    "relationships": [
      {"sourceSlug": "bertolt-brecht", "sourceName": "Bertolt Brecht (1898–1956, German playwright and poet)", "verb": "AUTHORS", "targetSlug": "the-threepenny-opera", "targetName": "The Threepenny Opera (Die Dreigroschenoper, music by Kurt Weill, premiere 31 August 1928, Berlin)", "context": "Brecht's Threepenny Opera (music by Weill) premiered in Berlin on 31 August 1928 — 350 performances in the first production, translated into 18 languages within a year, the most successful work of Weimar theatre."},
      {"sourceSlug": "the-threepenny-opera", "sourceName": "Threepenny Opera (Mack the Knife — Louis Armstrong, Bobby Darin)", "verb": "SOURCE_OF", "targetSlug": "mack-the-knife", "targetName": "'Mack the Knife' (Die Moritat von Mackie Messer — one of most recorded songs of 20th century)", "context": "'Mack the Knife' became one of the most recorded popular songs of the 20th century — Louis Armstrong (1956), Bobby Darin (Grammy 1959), Ella Fitzgerald, Frank Sinatra, among hundreds of recordings."},
      {"sourceSlug": "the-threepenny-opera", "sourceName": "Threepenny Opera (epic theatre, Verfremdungseffekt — political theatre model)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "epic-theatre", "targetName": "Epic theatre / Brechtian theatre (Verfremdungseffekt — politically engaged theatre worldwide)", "context": "The Threepenny Opera was the first major popular realisation of Brecht's epic theatre — the alienation effect, political satire through musical interruption, and parodic ending established the Brechtian method that became the dominant framework for politically engaged theatre worldwide."}
    ],
    "places": [
      {"name": "Berlin, Germany (Theater am Schiffbauerdamm, 31 August 1928 — Weimar Republic)", "role": "The Threepenny Opera premiered at the Theater am Schiffbauerdamm in Berlin on 31 August 1928 — the Weimar Republic's theatrical culture and political climate were the immediate context for its satirical critique"},
      {"name": "Global (18 language translations within one year; continuous performance worldwide to present)", "role": "The Threepenny Opera spread globally within months of its premiere — translated into 18 languages and performed continuously since 1928, it is the most widely performed German-language play of the 20th century"}
    ],
    "subjects": ["German Literature", "Modern Era", "Bertolt Brecht", "Kurt Weill", "Epic Theatre", "Musical Theatre", "Weimar Republic", "Political Drama"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Threepenny Opera (Brecht/Weill, 1928) is the supreme example of Brechtian epic theatre and the most widely performed German-language play of the 20th century. Its political satire of capitalism and bourgeois justice, its fusion of jazz and cabaret with theatrical alienation effects, and 'Mack the Knife' (one of the most recorded songs of the 20th century) make it a defining cultural achievement of the Weimar Republic and a foundational text for politically engaged theatre worldwide.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-tale-of-the-bamboo-cutter": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-tale-of-the-bamboo-cutter.json",
  "slug": "the-tale-of-the-bamboo-cutter",
  "data": {
    "summary": "The Tale of the Bamboo Cutter (Japanese: 竹取物語, Taketori Monogatari) is the earliest surviving Japanese prose narrative, composed c. 909–910 CE (with some scholars proposing 850–950 CE), written in Chinese characters (kanji) rather than in the kana that would later characterise Heian women's literature, and attributed to an unknown author. It is the founding text of Japanese narrative prose — referred to by Murasaki Shikibu in the Tale of Genji as 'the ancestor of all tales' (monogatari no oya) — and one of the earliest examples of science fiction in world literature.\n\nThe tale narrates the discovery by an old bamboo cutter (Taketori no Okina) of a tiny luminous girl inside a shining bamboo stalk, whom he raises as his daughter, naming her Kaguya-hime ('Shining Princess'). As she grows, her extraordinary beauty attracts five noble suitors (including the Emperor himself), each of whom she sends on impossible quests for legendary treasures — a robe of fire-rat fur, the jewelled branch of the island of Hōrai, the stone begging bowl of the Buddha, the jewel from a dragon's neck, and the cowrie-shell born from a swallow — all of which fail. When the suitors (and the Emperor) are all rebuffed, Kaguya-hime reveals that she is from the Moon — the armies of Heaven descend to return her, and she ascends to the Moon, leaving the grieving Emperor a letter and the elixir of immortality, which he orders burned on the summit of Mount Fuji, the 'mountain nearest Heaven'.\n\nThe Tale of the Bamboo Cutter is the founding text of Japanese mono no aware aesthetics — the beauty of transience and loss — and the source of Japan's most enduring cultural image: the Moon as the origin of celestial beings and the destination of the soul. The story is still actively told and retold in manga (Princess Kaguya), anime (Isao Takahata's The Tale of Princess Kaguya, 2013), and pop culture worldwide.",
    "causes": [
      "The Nara-period (710–794 CE) and early Heian oral narrative tradition — the folk tales and mythological narratives circulating in Japan before the development of written kana prose — provided the folk-tale elements (the luminous child found in a plant, the impossible quests, the celestial origin) that the tale synthesised into a literary narrative.",
      "The influence of Chinese literary culture — the tale's use of kanji rather than kana, its allusions to Chinese cosmography (the Island of Hōrai, the divine treasures), and its engagement with Chinese literary conventions — reflects the Japanese court's intense engagement with Tang Dynasty Chinese culture in the 9th century CE.",
      "The Heian court's sophisticated literary culture — its cultivation of narrative prose as an aesthetic achievement, the development of the monogatari ('tale') as a genre — provided the context for the tale's composition and the literary standard against which it was measured: Murasaki Shikibu's later identification of it as 'the ancestor of all tales' reflects the Heian court's retrospective recognition of its founding importance."
    ],
    "effects": [
      "The Tale of the Bamboo Cutter established the monogatari genre (Japanese prose narrative) — Murasaki Shikibu called it 'the ancestor of all tales' in the Tale of Genji, and it provided the model for the psychological and romantic elaboration of narrative that Murasaki Shikibu brought to its highest expression.",
      "The tale's central image — Kaguya-hime as a celestial being temporarily dwelling on Earth, unable to remain in the mortal world — established the aesthetic of the Moon and celestial transience that became one of the defining images of Japanese culture, from the Heian period through classical poetry, Noh drama, and contemporary manga and anime.",
      "The tale is one of the earliest examples of science fiction motifs in world literature — the extraterrestrial origin of the protagonist, the suitors' impossible quests (analogous to sf 'MacGuffin' missions), and the celestial rescue mission — making it frequently cited in histories of science fiction as a precursor of the genre."
    ],
    "relationships": [
      {"sourceSlug": "the-tale-of-the-bamboo-cutter", "sourceName": "Tale of the Bamboo Cutter (c. 909–910 CE — 'ancestor of all tales')", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "japanese-monogatari-genre", "targetName": "Japanese monogatari genre (prose narrative — Genji, Ise Monogatari, etc.)", "context": "The Tale of the Bamboo Cutter is the earliest surviving Japanese prose narrative — Murasaki Shikibu called it 'the ancestor of all tales' in the Tale of Genji, recognising it as the founding text of Japanese narrative prose."},
      {"sourceSlug": "the-tale-of-the-bamboo-cutter", "sourceName": "Tale of the Bamboo Cutter (Kaguya-hime — Moon, celestial beings, transience)", "verb": "ESTABLISHES", "targetSlug": "japanese-moon-imagery", "targetName": "Japanese Moon aesthetic and celestial imagery in literature and art", "context": "The tale established the Moon as the origin of celestial beings in Japanese culture — Kaguya-hime's lunar origin and celestial ascent became one of the defining images of Japanese aesthetics, from Heian poetry through Noh, manga, and contemporary anime."},
      {"sourceSlug": "the-tale-of-the-bamboo-cutter", "sourceName": "Bamboo Cutter (Takahata 2013 anime — Studio Ghibli)", "verb": "ADAPTED_AS", "targetSlug": "studio-ghibli", "targetName": "Studio Ghibli (Isao Takahata's The Tale of Princess Kaguya, 2013)", "context": "Isao Takahata's The Tale of Princess Kaguya (2013, Studio Ghibli) is the most celebrated modern adaptation of the tale — an Oscar-nominated anime film that introduced the story to global audiences."}
    ],
    "places": [
      {"name": "Heian Japan (c. 909–910 CE — Heiankyō court; 'ancestor of all tales')", "role": "The Tale of the Bamboo Cutter was composed at the Heian court c. 909–910 CE — the earliest surviving Japanese prose narrative and the founding text of the monogatari genre"},
      {"name": "Japan (millennium-long reception — Noh, manga, anime — and global diffusion via Ghibli)", "role": "The tale has been continuously retold in Japan for over a millennium — in Noh drama, manga, and anime, and through Takahata's 2013 Studio Ghibli film it reached global audiences"}
    ],
    "subjects": ["Japanese Literature", "Ancient Era", "Heian Period", "Monogatari", "Science Fiction Origins", "Folk Tale", "Kaguya-hime", "Japanese Mythology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Tale of the Bamboo Cutter (c. 909–910 CE) is the earliest surviving Japanese prose narrative and the founding text of the monogatari genre — Murasaki Shikibu called it 'the ancestor of all tales'. Its central image (Kaguya-hime's lunar origin and celestial ascent) became one of the defining images of Japanese culture; it is also one of the earliest examples of science fiction motifs in world literature. Isao Takahata's 2013 Studio Ghibli adaptation introduced the tale to global audiences.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-raven": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-raven.json",
  "slug": "the-raven",
  "data": {
    "summary": "The Raven is a narrative poem by the American writer Edgar Allan Poe (1809–1849), first published in the New York Evening Mirror on 29 January 1845 and subsequently in the American Review: A Whig Journal (February 1845). It is the most famous American poem of the 19th century and one of the most recognised poems in the English language — a 108-line poem in trochaic octameter with the rhyme scheme ABCBBB in which a grieving narrator, alone at midnight with his books, is visited by a raven who can only say 'Nevermore', and whom the narrator questions increasingly desperately about the possibility of reunion with his lost love Lenore, receiving always the same devastating answer.\n\nThe Raven's formal achievement is extraordinary: Poe's relentless trochaic octameter ('Once upon a midnight dreary, while I pondered, weak and weary'), its intricate internal rhyme scheme, the repetition of 'Nevermore' as a refrain that grows more terrible with each repetition, and the poem's controlled escalation from mournful meditation to psychological terror established a standard of formal virtuosity in American poetry. Poe himself wrote an essay ('The Philosophy of Composition', 1846) purporting to explain exactly how he constructed the poem — a claim that the essay describes his compositional method as a purely logical process working backwards from the desired effect — though most scholars regard this as a critical fiction.",
    "causes": [
      "Poe's personal grief — his wife Virginia Clemm's tuberculosis (she died in January 1847, two years after the poem's publication) — is frequently cited as biographical background for the poem's meditation on irrecoverable loss, though the poem's formal qualities suggest that the emotional content was as carefully constructed as the verse form.",
      "The English Romantic and Gothic tradition — Coleridge's Rime of the Ancient Mariner (the supernatural bird as omen), Byron's Gothic melancholy, and the tradition of the Gothic dream-vision — provided literary models for the poem's combination of supernatural visitor and psychological terror.",
      "Poe's literary ambition — his determination to write a poem that would be simultaneously a popular sensation and a formal masterpiece — drove the extraordinary attention to the poem's technical construction documented in 'The Philosophy of Composition': the choice of trochaic octameter, the selection of 'Nevermore' as the maximally resonant single word, the decision to build the poem to a single climactic effect."
    ],
    "effects": [
      "The Raven was an immediate popular sensation — reprinted throughout the US and Britain within weeks of publication, memorised and recited across the country, and making Poe (who had been virtually unknown outside literary circles) immediately famous, though the fame did not alleviate his poverty.",
      "'The Raven' and 'Nevermore' entered the cultural vocabulary — the raven as a symbol of grief, obsession, and the refusal of hope; the word 'Nevermore' as the most resonant English monosyllable of despair — becoming one of the most widely parodied, referenced, and adapted poems in the Western literary tradition.",
      "The Raven's French translation by Charles Baudelaire — who translated Poe's fiction and poetry into French throughout the 1850s–1860s and became Poe's most fervent European champion — was decisive for the French Symbolist movement: Mallarmé translated the poem (with illustrations by Manet), and the Poe-Baudelaire axis was the primary channel through which American Gothic imagination influenced French Symbolism and Modernism."
    ],
    "relationships": [
      {"sourceSlug": "edgar-allan-poe", "sourceName": "Edgar Allan Poe (1809–1849, American writer and poet)", "verb": "AUTHORS", "targetSlug": "the-raven", "targetName": "The Raven (first published 29 January 1845, New York Evening Mirror)", "context": "Poe published The Raven in January 1845 — immediately famous, it became the most recognised American poem of the 19th century and made Poe a literary celebrity."},
      {"sourceSlug": "the-raven", "sourceName": "The Raven (Baudelaire translation; French Symbolism — Mallarmé, Manet)", "verb": "INFLUENCES", "targetSlug": "french-symbolist-movement", "targetName": "French Symbolism (Baudelaire, Mallarmé, Verlaine — 1850s–1880s)", "context": "Baudelaire's translation of Poe's works (including The Raven) was decisive for French Symbolism — Mallarmé translated The Raven with illustrations by Manet, and the Poe-Baudelaire axis was the primary channel through which American Gothic influenced French Modernism."},
      {"sourceSlug": "the-raven", "sourceName": "The Raven (trochaic octameter, 'Nevermore' — formal mastery)", "verb": "EXEMPLIFIES", "targetSlug": "american-gothic-literature", "targetName": "American Gothic literature and Poe's theory of effect", "context": "The Raven is the supreme example of Poe's theory of the single unified effect — the poem's formal mastery (trochaic octameter, internal rhyme, the 'Nevermore' refrain) exemplifies his conception of poetry as pure technique in service of a single emotional effect."}
    ],
    "places": [
      {"name": "New York, USA (first published New York Evening Mirror, 29 January 1845)", "role": "The Raven was first published in the New York Evening Mirror on 29 January 1845 — an immediate popular sensation, reprinted throughout the US and Britain"},
      {"name": "France (Baudelaire translation 1853; Mallarmé translation 1875 — Poe's decisive European reception)", "role": "Baudelaire translated The Raven into French (1853) and became Poe's European champion — Mallarmé's later translation (1875), with Manet's illustrations, made the poem a central text of French Symbolism"}
    ],
    "subjects": ["American Literature", "Modern Era", "Edgar Allan Poe", "Gothic Poetry", "American Gothic", "Narrative Poetry", "19th Century", "French Symbolism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Raven (Poe, 1845) is the most famous American poem of the 19th century — its formal virtuosity (trochaic octameter, 'Nevermore' refrain) and its immediate popular impact made Poe famous and the poem one of the most widely parodied and referenced texts in the Western literary tradition. Through Baudelaire's translation it influenced French Symbolism; through Mallarmé and Manet's edition it became a central text of European Modernism.",
      "significanceCategory": "world-changing"
    }
  }
},

"vande-mataram": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780vande-mataram.json",
  "slug": "vande-mataram",
  "data": {
    "summary": "Vande Mataram (Sanskrit/Bengali: বন্দে মাতরম, 'I bow to thee, Mother') is a poem in Bengali and Sanskrit by the Bengali novelist Bankim Chandra Chattopadhyay (Chatterjee, 1838–1894), composed c. 1876 CE and first published in his novel Anandamath (1882). The poem serves as a hymn to the motherland of India, personified as a goddess (Durga) — its opening two stanzas address the mother figure as abundant ('with thy waters, O my Mother'), beautiful, and divine. Set to music by Rabindranath Tagore, the poem became the war-cry (warcry) of the Indian independence movement against British colonial rule, was adopted by the Indian National Congress as its official song (1896, when Tagore first sang it at the Congress session), and was subsequently declared the National Song of India (alongside Jana Gana Mana as the National Anthem).\n\nVande Mataram's cultural and political significance in Indian history is extraordinary — it was the most powerful rallying cry of the independence movement, chanted by protesters during the Swadeshi Movement (1905–1908, triggered by the British partition of Bengal), sung by freedom fighters before their execution, and used as a patriotic anthem across the independence struggle. Its adoption by Hindu nationalist movements (as a specifically Hindu poem, invoking the goddess Durga) and the controversy over its use in Muslim communities (who saw the invocation of Durga as incompatible with Islam) made it one of the most politically contested texts of the colonial and post-independence period.\n\nBankim Chandra Chattopadhyay's novel Anandamath, in which the poem appears, is itself a foundational text of Bengali cultural nationalism — a historical novel about Sanyasi ascetics fighting British rule that established the narrative of Bengali Hindu resistance to colonial power. Vande Mataram thus emerged from and gave cultural form to the first major articulation of Indian cultural nationalism in the modern period.",
    "causes": [
      "Bankim Chandra Chattopadhyay's Bengali cultural nationalism — his response to British colonial rule and his project of articulating a distinctively Bengali (and Indian) cultural identity through literature — provided the political and cultural motivation for the poem: Vande Mataram expressed the devotion to the motherland as a spiritual and political act simultaneously.",
      "The Bengal Renaissance — the 19th-century cultural and intellectual revival in Bengal (Rammohan Roy, Iswar Chandra Vidyasagar, Bankim Chandra, Tagore) that combined Western education with pride in Indian cultural tradition — provided the intellectual context for Bankim Chandra's synthesis of Sanskrit devotional imagery with Bengali literary nationalism.",
      "The specific political crisis of the 1905 Bengal Partition — the British partition of Bengal (announced by Lord Curzon in 1905) was experienced as a deliberate attack on Bengal's cultural and religious unity, and the Swadeshi Movement's adoption of Vande Mataram as its chant transformed the poem from a literary text into a mass political cry."
    ],
    "effects": [
      "Vande Mataram became the primary rallying cry of the Indian independence movement — chanted at protests, sung by freedom fighters before execution (Bhagat Singh), and adopted as the Congress's official song in 1896 — making it one of the most potent political anthems in the history of anti-colonial movements worldwide.",
      "The National Song controversy — the debate over whether Vande Mataram (which invokes Durga) or Jana Gana Mana (Tagore's secular anthem) should be the National Anthem — encapsulates the foundational tension in Indian nationalism between Hindu cultural nationalism (Vande Mataram) and secular inclusive nationalism (Jana Gana Mana), a debate that continues in Indian politics.",
      "Bankim Chandra's Anandamath and Vande Mataram together established the framework of Hindu cultural nationalism that would shape the RSS, the Hindu Mahasabha, and eventually the BJP — the identification of India as mother goddess (Bharat Mata), the ideal of the ascetic freedom fighter, and the invocation of Hindu mythological imagery in political struggle."
    ],
    "relationships": [
      {"sourceSlug": "bankim-chandra-chattopadhyay", "sourceName": "Bankim Chandra Chattopadhyay (1838–1894, Bengali novelist)", "verb": "AUTHORS", "targetSlug": "vande-mataram", "targetName": "Vande Mataram (c. 1876, first published in Anandamath 1882)", "context": "Bankim Chandra composed Vande Mataram c. 1876 and published it in his novel Anandamath (1882) — Tagore set it to music, it was adopted by the Indian National Congress in 1896, and it became the primary anthem of the independence movement."},
      {"sourceSlug": "vande-mataram", "sourceName": "Vande Mataram (Swadeshi Movement, freedom fighters, independence anthem)", "verb": "RALLYING_CRY_OF", "targetSlug": "indian-independence-movement", "targetName": "Indian independence movement (Congress, Swadeshi, Bhagat Singh, Gandhi)", "context": "Vande Mataram was the primary rallying cry of the Indian independence movement — chanted during the Swadeshi Movement (1905), sung by freedom fighters before execution, and adopted as the Congress's official song."},
      {"sourceSlug": "vande-mataram", "sourceName": "Vande Mataram vs Jana Gana Mana — National Song controversy", "verb": "CONTESTED_ALONGSIDE", "targetSlug": "jana-gana-mana", "targetName": "Jana Gana Mana (Tagore's National Anthem of India)", "context": "The debate over Vande Mataram vs Jana Gana Mana as India's National Anthem encapsulates the foundational tension between Hindu cultural nationalism and secular inclusive nationalism — a debate that continues in contemporary Indian politics."}
    ],
    "places": [
      {"name": "Bengal, India (Bankim Chandra's composition c. 1876; Swadeshi Movement 1905–1908)", "role": "Vande Mataram was composed in Bengal c. 1876 and became the primary anthem of the Swadeshi Movement (1905–1908) — the first mass anti-colonial protest movement in India, triggered by the British partition of Bengal"},
      {"name": "India (National Song — chanted at independence movement protests, sung at Congress sessions, contested post-independence)", "role": "Vande Mataram was India's primary independence anthem — sung at Congress sessions from 1896, chanted at protests, and declared the National Song of independent India (alongside Jana Gana Mana as the National Anthem)"}
    ],
    "subjects": ["Bengali Literature", "Modern Era", "Bankim Chandra Chattopadhyay", "Indian Nationalism", "Independence Movement", "National Anthem", "Colonial Resistance", "Hindu Nationalism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Vande Mataram (Bankim Chandra, c. 1876) is one of the most politically potent anthems in the history of anti-colonial movements — the primary rallying cry of the Indian independence movement, chanted by freedom fighters before execution. Its National Song status, the controversy over its Hindu imagery, and its role in shaping both the independence movement and Hindu cultural nationalism make it one of the most consequential literary texts in Indian political history.",
      "significanceCategory": "world-changing"
    }
  }
},

"salome": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780salome.json",
  "slug": "salome",
  "data": {
    "summary": "Salomé is a one-act play in French by the Irish playwright and poet Oscar Wilde (1854–1900), written in French in 1891 and first published in Paris in 1893 (illustrated by Aubrey Beardsley), with the English translation (by Lord Alfred Douglas, revised by Wilde) published in London in 1894. The play dramatises the biblical story of Salome's dance before Herod Tetrarch (the 'Dance of the Seven Veils') and her demand for the head of Jokanaan (John the Baptist) on a silver platter — transforming the biblical episode into a study of obsessive desire, the power of the gaze, and the fatal consequences of refused love. Salome's lust for Jokanaan (who refuses her) and her final necrophilic kiss of his severed head are the play's most extreme dramatic moments.\n\nWilde wrote Salomé in Paris in 1891, having been immersed in French Symbolist culture (Mallarmé, Maeterlinck, Flaubert's Hérodias). The play was first performed in Paris in February 1896 (while Wilde was imprisoned in Reading Gaol) by Sarah Bernhardt — a production that made the play internationally famous. Its London performance was banned by the Lord Chamberlain (on the grounds that it was illegal to depict biblical characters on the English stage) — the ban itself became a celebrated cause célèbre that contributed to the play's notoriety and Wilde's image as a martyred artist.\n\nThe play's most significant cultural afterlife was Richard Strauss's opera Salome (1905), based directly on Wilde's text (translated by Hedwig Lachmann) — the opera, premiered in Dresden on 9 December 1905, was an immediate international sensation, performed over fifty times in its first year, and became one of the most important works of early 20th-century music. Strauss's Salome established the fin-de-siècle femme fatale as an operatic type and is now a core work of the operatic repertoire.",
    "causes": [
      "Wilde's immersion in French Symbolist culture — his friendship with Mallarmé, his engagement with Maeterlinck's Symbolist drama, and his reading of Flaubert's Hérodias and Huysmans' À Rebours (with its discussion of the Moreau Salome paintings) — provided the aesthetic context for a play written in French about the femme fatale as the supreme Symbolist subject.",
      "Gustave Moreau's paintings of Salome (1874–1876) — described in Huysmans' À Rebours as the ultimate expression of the decadent femme fatale — established the visual and thematic framework that Wilde translated into dramatic form: Moreau's Salome dancing before Herod, her obsessive gaze, and the Baptist's severed head.",
      "Wilde's personal situation — his homosexuality, his aesthetic theory of art as pure form transcending morality, and his confrontation with Victorian sexual and social convention — gave the play's exploration of transgressive desire, the death wish, and the law's prohibition of Eros a personal urgency."
    ],
    "effects": [
      "Richard Strauss's Salome opera (1905) — based directly on Wilde's play — was the most sensational opera premiere of the early 20th century, performed over fifty times in its first year and establishing the femme fatale as a central type of modern opera; it is now a core work of the operatic repertoire and has proved more durable than any other Strauss opera.",
      "The ban on the London performance of Salomé — prohibited by the Lord Chamberlain for depicting a biblical character — became a celebrated cause of Victorian theatrical censorship and contributed to the campaign to abolish the Lord Chamberlain's powers of theatrical censorship (which were finally abolished in 1968).",
      "Salomé established the fin-de-siècle femme fatale as the supreme figure of decadent culture — the dangerous, desiring woman who demands the death of the man who refuses her — an image that circulated through Symbolist painting (Moreau, Klimt), poetry (Mallarmé's Hérodiade), and opera (Strauss) as the defining figure of the 1890s decadent imagination."
    ],
    "relationships": [
      {"sourceSlug": "oscar-wilde", "sourceName": "Oscar Wilde (1854–1900, Irish playwright and poet)", "verb": "AUTHORS", "targetSlug": "salome", "targetName": "Salomé (written in French 1891; French publication 1893; English 1894)", "context": "Wilde wrote Salomé in French in 1891 — published in Paris in 1893 with Beardsley's illustrations; London performance banned; first performed by Sarah Bernhardt in Paris in 1896 while Wilde was in prison."},
      {"sourceSlug": "salome", "sourceName": "Salomé (Wilde's text — Strauss opera 1905 — Dresden premiere)", "verb": "SOURCE_TEXT_FOR", "targetSlug": "salome-opera-richard-strauss", "targetName": "Salome opera (Richard Strauss, 1905 Dresden premiere — core operatic repertoire)", "context": "Richard Strauss's Salome (1905) — based directly on Wilde's play — was the most sensational opera premiere of the early 20th century; it is now a core work of the operatic repertoire."},
      {"sourceSlug": "salome", "sourceName": "Salomé (femme fatale, decadent aesthetics — Moreau, Klimt, Symbolism)", "verb": "EXEMPLIFIES", "targetSlug": "fin-de-siecle-decadent-aesthetics", "targetName": "Fin-de-siècle decadent aesthetics (1890s — Symbolism, femme fatale, Moreau, Klimt)", "context": "Salomé is the supreme dramatic expression of fin-de-siècle decadent aesthetics — the femme fatale, transgressive desire, the aestheticisation of death — connecting Wilde's play to Moreau's paintings, Klimt's visual imagery, and the broader Symbolist obsession with the dangerous woman."}
    ],
    "places": [
      {"name": "Paris, France (written 1891; first published 1893; first performed February 1896 by Sarah Bernhardt)", "role": "Wilde wrote Salomé in Paris in 1891 — the city's Symbolist culture inspired the play; Sarah Bernhardt premiered it in Paris in February 1896 while Wilde was imprisoned in Reading Gaol"},
      {"name": "Dresden, Germany (Strauss opera premiere 9 December 1905 — international sensation)", "role": "Richard Strauss's Salome opera — based on Wilde's play — had its world premiere in Dresden on 9 December 1905, becoming the most sensational opera premiere of the early 20th century"}
    ],
    "subjects": ["Irish Literature", "Modern Era", "Oscar Wilde", "Symbolist Drama", "Femme Fatale", "Opera", "Fin-de-Siècle", "Decadent Aesthetics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Salomé (Wilde, 1891/1893) is the supreme dramatic expression of fin-de-siècle decadent aesthetics — and the source text for Richard Strauss's Salome opera (1905), one of the most important works of early 20th-century music. The London performance ban was a landmark in Victorian theatrical censorship; the play's femme fatale established a cultural type that circulated through Symbolist painting, poetry, and opera as the defining figure of the 1890s imagination.",
      "significanceCategory": "world-changing"
    }
  }
},

"watchmen": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780watchmen.json",
  "slug": "watchmen",
  "data": {
    "summary": "Watchmen is a twelve-issue limited series (graphic novel) by the British writer Alan Moore (b. 1953) and artist Dave Gibbons (b. 1949), published monthly by DC Comics from September 1986 to October 1987, and collected as a graphic novel in 1987. It is the most critically acclaimed graphic novel ever published — in 1988 it became the first (and for many years the only) graphic novel to win a Hugo Award, and it has consistently been included in lists of the greatest English-language novels of the 20th century (including Time magazine's 'All-Time 100 Novels'). Watchmen is the work that definitively established the graphic novel as a form capable of sustaining literary complexity and ambition comparable to prose fiction.\n\nWatchmen is set in an alternate-history United States in 1985, where superheroes have existed since the 1940s. A retired hero named The Comedian is murdered, and Rorschach (a vigilante whose mask reflects a shifting Rorschach inkblot pattern, symbolising moral ambiguity) begins investigating, uncovering a conspiracy that connects to the imminent threat of nuclear war between the US and USSR. The story interrogates every convention of the superhero genre — the nature of heroism, the relationship between power and morality ('Who watches the watchmen?' — the Juvenal epigraph), the psychology of violence, the political implications of superhuman power, and the complicity of the audience that consumes and celebrates heroic violence. The mystery plot resolves in a disturbing climax that forces the reader to confront the utilitarian logic of mass murder in service of a greater good.\n\nAlan Moore's script and Dave Gibbons' nine-panel grid artwork (every page uses a strict 3×3 panel grid, with variations and interruptions used for specific effect) demonstrated the unique formal capabilities of the comics medium — the simultaneous experience of image and text, the use of parallel narratives (the pirate comic 'Tales of the Black Freighter' within the story), and the integration of supplementary prose documents (in-universe excerpts from memoirs, reports, psychological profiles) created a narrative density unprecedented in comics.",
    "causes": [
      "DC Comics' acquisition of the Charlton Comics characters (Captain Atom, Blue Beetle, The Question, etc.) and Alan Moore's initial proposal to use them in a story that would 'put them through the wringer' — DC's concern that this would make the characters unusable led Moore to create analogues (Dr. Manhattan, Nite Owl, Rorschach) — provided the direct occasion for Watchmen.",
      "The 1980s political context — the Reagan administration's nuclear buildup, the renewed Cold War tensions (1983 Able Archer exercise, the Euromissile crisis), the moral certainty of American conservatism — provided the political content for the story's alternate 1985, where Nixon is in his fifth term and nuclear annihilation is imminent.",
      "The formal and critical possibilities of the comics medium — Moore and Gibbons' shared determination to produce a work that demonstrated what only comics (not film, not prose fiction) could do — drove the formal innovations of the strict nine-panel grid, the parallel narrative, and the in-universe documents."
    ],
    "effects": [
      "Watchmen definitively elevated the graphic novel to the status of serious literary achievement — its Hugo Award (1988) and its inclusion in Time magazine's 'All-Time 100 Novels' established it as a work comparable to major prose fiction, initiating a critical re-evaluation of the comics medium that has continued to the present.",
      "Watchmen transformed the superhero genre — its deconstruction of superhero conventions (the psychology of violence, the political implications of power, the moral ambiguity of heroism) influenced virtually every subsequent serious treatment of superheroes in comics (Frank Miller's The Dark Knight Returns), film (the 'dark superhero' genre from Batman Begins through Logan), and television.",
      "Alan Moore's narrative technique — the nine-panel grid as formal constraint, the parallel pirate narrative, the in-universe documents — established a new standard for structural and formal complexity in comics, influencing Grant Morrison, Neil Gaiman, and the entire generation of ambitious comics creators who emerged in the 1990s–2000s."
    ],
    "relationships": [
      {"sourceSlug": "alan-moore", "sourceName": "Alan Moore (b. 1953, British comics writer)", "verb": "AUTHORS", "targetSlug": "watchmen", "targetName": "Watchmen (illustrated by Dave Gibbons, DC Comics 1986–1987, 12 issues)", "context": "Alan Moore and Dave Gibbons created Watchmen for DC Comics (1986–1987) — the most critically acclaimed graphic novel ever published, the first to win a Hugo Award, and included in Time's 'All-Time 100 Novels'."},
      {"sourceSlug": "watchmen", "sourceName": "Watchmen (deconstruction of superhero genre — dark psychology of heroism)", "verb": "TRANSFORMS", "targetSlug": "superhero-genre", "targetName": "Superhero genre (comics, film, television — dark superhero trend)", "context": "Watchmen's deconstruction of superhero conventions influenced virtually every subsequent serious treatment of superheroes — in comics (The Dark Knight Returns), film (Batman Begins, Logan), and television."},
      {"sourceSlug": "watchmen", "sourceName": "Watchmen (Hugo Award 1988; Time 100 Novels — graphic novel as literature)", "verb": "ESTABLISHES", "targetSlug": "graphic-novel-literary-form", "targetName": "Graphic novel as literary form (serious literary achievement, critical recognition)", "context": "Watchmen definitively established the graphic novel as a form capable of literary complexity — its Hugo Award (1988) and inclusion in Time's 'All-Time 100 Novels' initiated a critical re-evaluation of the comics medium that continues to the present."}
    ],
    "places": [
      {"name": "United States (DC Comics, New York; alternate-history 1985 America — Cold War, Nixon fifth term)", "role": "Watchmen was published by DC Comics in New York (1986–1987) and is set in an alternate-history 1985 America — the Reagan-era Cold War tensions and political context are central to the story's political dimensions"},
      {"name": "United Kingdom (Alan Moore from Northampton; British writers' dominance of 1980s American comics)", "role": "Alan Moore (Northampton, England) was part of the British Invasion of American comics in the 1980s — alongside Grant Morrison and Neil Gaiman, Moore transformed American superhero comics with British literary ambition and formal experimentation"}
    ],
    "subjects": ["Comics", "Modern Era", "Alan Moore", "Dave Gibbons", "Graphic Novel", "Superhero Genre", "Cold War Literature", "American Comics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Watchmen (Moore/Gibbons, 1986–1987) is the most critically acclaimed graphic novel ever published — the first to win a Hugo Award, included in Time's 'All-Time 100 Novels', and the work that definitively established the graphic novel as a literary form. Its deconstruction of the superhero genre transformed comics, film, and television; its formal innovations (the nine-panel grid, parallel narratives, in-universe documents) established a new standard for structural complexity in the medium.",
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
