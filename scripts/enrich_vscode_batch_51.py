#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 51 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-green-book (Gaddafi), ruhnama (Niyazov), struwwelpeter (Hoffmann),
          snow-white (Brothers Grimm), the-emperors-new-clothes (Andersen),
          the-snow-queen (Andersen), rapunzel (Brothers Grimm),
          the-mousetrap (Agatha Christie)

NOTE: All entities had short stubs from a subagent (~100c) — summaries are below
the 800c skip threshold, so this script will properly overwrite them.
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-51-may2026"

ENRICHMENTS = {

"the-green-book": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-green-book.json",
  "slug": "the-green-book",
  "data": {
    "summary": "The Green Book (Arabic: الكتاب الأخضر, Al-Kitāb Al-Aḫḍar) is the political manifesto and ideological text of Muammar Gaddafi (1942–2011), leader of Libya from 1969 to 2011, published in three parts between 1975 and 1979 and presented as the foundational ideology of the Libyan state. Part One ('The Solution of the Problem of Democracy: The Authority of the People', 1975) introduces Gaddafi's concept of direct democracy through 'People's Congresses', rejecting parliamentary democracy and political parties as instruments of the few; Part Two ('The Solution of the Economic Problem: Socialism', 1977) advocates the abolition of wage labour, the worker ownership of means of production, and the elimination of rent; Part Three ('The Social Basis of the Third Universal Theory', 1978) develops Gaddafi's 'Third Universal Theory' — a Third Way between capitalism and communism — and addresses the role of women, education, sport, and the family.\n\nThe Green Book was made compulsory reading in Libyan schools, factories, and military units, translated into dozens of languages, and widely distributed by Libyan embassies abroad as part of Gaddafi's attempt to promote his Third Universal Theory as a global alternative ideology. Its ideas were applied in the Libyan Arab Jamahiriyya ('state of the masses'), the governmental system established in 1977 in which formal governmental structures were replaced by a system of People's Congresses and People's Committees — a political system unique in the world and which Gaddafi claimed had abolished all governments. In practice, Gaddafi retained effective control through his position as 'Leader of the Revolution' and through the military and security apparatus.\n\nThe Green Book is significant not as a coherent political philosophy (scholars have noted its incoherence, eclecticism, and practical inapplicability) but as a document of 20th-century revolutionary nationalism, Third World ideology, and the political culture of the 'era of revolutions' — and as the foundational document of a 42-year dictatorship that shaped Libya until Gaddafi's overthrow and death during the Arab Spring (2011).",
    "causes": [
      "Gaddafi's 1969 coup (Operation Jerusalem) — the Free Officers' Movement's overthrow of the Libyan monarchy under King Idris I — created a revolutionary government that required an ideological foundation, and Gaddafi's intellectual ambition to formulate a Third Way between capitalism and Soviet communism drove the development of the Third Universal Theory articulated in the Green Book.",
      "The 1970s context of Third World revolutionary nationalism — the Non-Aligned Movement, Arab socialism, the Palestinian cause, anti-imperialism, and the desire of post-colonial states to forge ideological independence from both the US-led West and the Soviet bloc — provided the political environment in which Gaddafi's Green Book sought to position Libya as the vanguard of a new global ideology.",
      "Gaddafi's intellectual background — his Bedouin heritage, his Islamic identity, his Arab nationalist formation, and his reading of Rousseau's direct democracy, Proudhon's anarchism, and Islamic political thought — provided the eclectic intellectual sources that were synthesised (inconsistently) in the Green Book."
    ],
    "effects": [
      "The Green Book provided the ideological basis for the Jamahiriyya ('state of the masses') system established in Libya in 1977 — in which formal governmental ministries were abolished and replaced by People's Congresses and People's Committees — a political experiment unique in the world, however ineffective in practice, that made Libya the laboratory of Gaddafi's political ideas for over three decades.",
      "The Green Book was distributed globally by Libyan embassies and state-funded organisations as part of Gaddafi's attempt to promote his Third Universal Theory as an alternative to capitalism and communism — influencing some Third World leftist movements, though its practical influence outside Libya was minimal.",
      "The Green Book's legacy was destroyed by the 2011 Arab Spring uprising and Gaddafi's overthrow — the Libyan Civil War that ended Gaddafi's 42-year rule exposed the Jamahiriyya's failure and made the Green Book a symbol of authoritarian pseudo-ideology rather than revolutionary vision."
    ],
    "relationships": [
      {"sourceSlug": "muammar-gaddafi", "sourceName": "Muammar Gaddafi (1942–2011, Leader of the Libyan Revolution 1969–2011)", "verb": "AUTHORS", "targetSlug": "the-green-book", "targetName": "The Green Book (Al-Kitāb Al-Aḫḍar, 1975–1979, Third Universal Theory)", "context": "Gaddafi authored The Green Book in three parts (1975–1979) as the ideological foundation of the Libyan state — presenting his Third Universal Theory as an alternative to capitalism and communism."},
      {"sourceSlug": "the-green-book", "sourceName": "The Green Book (Jamahiriyya — People's Congresses, Third Universal Theory)", "verb": "ESTABLISHES_IDEOLOGY_FOR", "targetSlug": "libyan-arab-jamahiriyya", "targetName": "Libyan Arab Jamahiriyya (1977–2011 — 'state of the masses' under Gaddafi)", "context": "The Green Book provided the ideological basis for the Jamahiriyya system (1977) — in which formal governments were replaced by People's Congresses and People's Committees, implementing Gaddafi's direct democracy theory."},
      {"sourceSlug": "the-green-book", "sourceName": "The Green Book (Third Way — Non-Aligned Movement, Third World ideology)", "verb": "RESPONDS_TO", "targetSlug": "cold-war", "targetName": "Cold War ideological competition (capitalism vs. communism)", "context": "The Green Book positioned Gaddafi's Third Universal Theory as a Third Way between capitalism and communism — an attempt to provide post-colonial Third World states with an ideological alternative during the Cold War."}
    ],
    "places": [
      {"name": "Libya (Libyan Arab Jamahiriyya, 1977–2011 — compulsory in schools, factories, military)", "role": "The Green Book was the foundational ideology of Libya under Gaddafi's 42-year rule — compulsory reading in schools, factories, and the military, and the basis for the Jamahiriyya political system"},
      {"name": "Global (Libyan embassies — Third Universal Theory exported; translated into dozens of languages)", "role": "The Green Book was distributed globally by Libyan embassies as part of Gaddafi's attempt to promote the Third Universal Theory — translated into dozens of languages and promoted by Libyan-funded organisations worldwide"}
    ],
    "subjects": ["Arabic Literature", "20th Century", "Political Ideology", "Libya", "Muammar Gaddafi", "Third Universal Theory", "Jamahiriyya", "Arab Nationalism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Green Book (1975–1979) is Gaddafi's political manifesto and the foundational ideology of Libya's Jamahiriyya ('state of the masses') — a unique political experiment that replaced formal government with People's Congresses in one of the Arab world's most unusual experiments in revolutionary politics. Significant as a document of 20th-century Third World ideology and as the founding text of a 42-year dictatorship ended by the 2011 Arab Spring.",
      "significanceCategory": "highly-significant"
    }
  }
},

"ruhnama": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780ruhnama.json",
  "slug": "ruhnama",
  "data": {
    "summary": "The Ruhnama (Turkmen: Ruhname, 'Book of the Soul') is a two-volume spiritual and political manifesto authored by Saparmurat Niyazov (1940–2006), President of Turkmenistan and self-styled Turkmenbashi ('Father of all Turkmen'), published in 2001 (Volume 1) and 2004 (Volume 2). The Ruhnama combines a mythologised history of the Turkmen people (tracing their origins to Oguz Khan, a semi-legendary Turkish ancestor), a moral and spiritual code for Turkmen citizens, a set of life lessons and proverbs, and a cult of personality text centring on Niyazov's own biography — including an account of his spiritual mission and the divine inspiration of the book. Niyazov declared the Ruhnama to be of equal religious authority with the Quran, displayed giant rotating statues of the book in public spaces, and required it to be studied in all Turkmen schools, universities, and government offices.\n\nThe Ruhnama is one of the most extreme examples of a state-sponsored personality cult book in world history — a document without intellectual merit but with extraordinary institutional power during the Niyazov era (1990–2006). Knowledge of the Ruhnama was required for driving licences, university entrance examinations, and government employment; passages from it were engraved on mosques; and a giant mechanical rotating monument to the book (the Neutrality Arch in Ashgabat) played recordings from the text. The Ruhnama became a symbol worldwide of the extreme forms that post-Soviet Central Asian authoritarianism could take.\n\nAfter Niyazov's death in December 2006, his successor Gurbanguly Berdimuhamedow quietly removed the Ruhnama from school curricula and demolished many of its monuments — though Berdimuhamedow subsequently authored his own analogous texts (the Ruhnama of the Horse, the Ruhnama of Tea), demonstrating the persistence of the personality cult book tradition in Turkmen political culture. The Ruhnama's history illustrates the use of text as an instrument of totalitarian control and national myth-making in the post-Soviet space.",
    "causes": [
      "The collapse of the Soviet Union (1991) and Turkmenistan's independence — leaving a political vacuum filled by Niyazov's assertion of a new national identity grounded in a mythologised Turkmen history — drove the creation of the Ruhnama as the founding ideological document of an independent Turkmen national consciousness.",
      "The tradition of post-Soviet Central Asian authoritarianism — the pattern of former Soviet leaders establishing personal cults and using national ideology to consolidate power in the absence of democratic institutions — provided the political context for the Ruhnama's creation as an instrument of state power.",
      "Niyazov's extraordinary concentration of power — his assumption of the title Turkmenbashi ('Father of all Turkmen'), his renaming of months and days of the week after himself and his family, and his elimination of all political opposition — created the conditions in which the Ruhnama could be imposed on all aspects of Turkmen public life without challenge."
    ],
    "effects": [
      "The Ruhnama was imposed on all aspects of Turkmen public life — required in school curricula, university entrance examinations, and government employment, engraved on mosques, read aloud on state television at 8pm daily, and required for driving licence examinations — making it the most intensively institutionalised personality cult text in post-Soviet history.",
      "The Ruhnama became an international symbol of post-Soviet authoritarian excess — its extravagant personality cult, its displacement of Islamic and scientific education, and its mechanical rotating monument in Ashgabat made it a widely cited example of the extremes of Central Asian authoritarianism in international human rights discourse.",
      "After Niyazov's death (2006), the Ruhnama was quietly withdrawn from public life — but its successor-texts by Berdimuhamedow (the Ruhnama of the Horse, etc.) demonstrated the persistence of the tradition of leader-authored national ideological texts in Turkmen political culture."
    ],
    "relationships": [
      {"sourceSlug": "saparmurat-niyazov", "sourceName": "Saparmurat Niyazov (Turkmenbashi, 1940–2006, President of Turkmenistan 1990–2006)", "verb": "AUTHORS", "targetSlug": "ruhnama", "targetName": "Ruhnama ('Book of the Soul', 2001/2004, Turkmenistan)", "context": "Niyazov authored the Ruhnama in 2001 and 2004 — declaring it equal in authority to the Quran and requiring it in all Turkmen schools, government offices, and public examinations."},
      {"sourceSlug": "ruhnama", "sourceName": "Ruhnama (personality cult — Turkmen national myth, equal to the Quran)", "verb": "EXEMPLIFIES", "targetSlug": "post-soviet-authoritarianism", "targetName": "Post-Soviet Central Asian authoritarianism (personality cults, national ideology)", "context": "The Ruhnama is one of the most extreme examples of a post-Soviet personality cult book — required in all aspects of Turkmen public life and declared by Niyazov to be of equal religious authority with the Quran."},
      {"sourceSlug": "ruhnama", "sourceName": "Ruhnama (national myth — Oguz Khan, Turkmen history and identity)", "verb": "CONSTRUCTS", "targetSlug": "turkmen-national-identity", "targetName": "Turkmen national identity (post-Soviet independence — mythologised history)", "context": "The Ruhnama constructed a mythologised Turkmen national identity — tracing Turkmen origins to Oguz Khan and providing a national origin story for post-Soviet Turkmenistan's independent identity."}
    ],
    "places": [
      {"name": "Ashgabat, Turkmenistan (Neutrality Arch — giant rotating monument; schools, mosques, television)", "role": "The Ruhnama was ubiquitous in Ashgabat and across Turkmenistan — a giant rotating mechanical monument played recordings from it; passages were engraved on mosques; state television broadcast readings daily"},
      {"name": "Turkmenistan (nationwide — school curricula, university exams, driving licences, government employment)", "role": "Knowledge of the Ruhnama was required for driving licences, university entrance examinations, and government employment across Turkmenistan during the Niyazov era (1990–2006)"}
    ],
    "subjects": ["Turkmen Literature", "20th Century", "Personality Cult", "Post-Soviet Politics", "Authoritarianism", "Turkmenistan", "National Ideology", "Central Asia"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Ruhnama (2001/2004) is one of the most extreme personality cult texts in post-Soviet history — required in all aspects of Turkmen public life, declared equal to the Quran, and enshrined in a giant rotating monument in Ashgabat. Significant as a document of post-Soviet Central Asian authoritarianism and the use of text as an instrument of totalitarian control and national myth-making.",
      "significanceCategory": "highly-significant"
    }
  }
},

"struwwelpeter": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780struwwelpeter.json",
  "slug": "struwwelpeter",
  "data": {
    "summary": "Struwwelpeter (German: 'Shock-headed Peter' or 'Shaggy Peter') is a German children's picture book by the Frankfurt physician and psychiatrist Heinrich Hoffmann (1809–1894), first published in 1845 by the Frankfurt publisher Rütten und Loening (initially printed privately for Hoffmann's son Karl) and one of the best-selling and most influential children's books of the 19th century, eventually translated into over 20 languages with millions of copies sold. The book consists of ten cautionary tales in verse, each illustrated with vivid hand-coloured engravings by Hoffmann himself, in which children who behave badly are punished with extreme, grotesque consequences: Struwwelpeter (a boy who refuses to cut his nails or hair) becomes physically monstrous; Conrad ('Thumbsucker', or Daumenlutscher) has his thumbs cut off by a 'great, long red-legged scissor-man' for sucking his thumbs; Pauline burns to death for playing with matches; Augustus starves to death for refusing his soup; Kaspar disappears from his bowl of soup; and the 'Story of the Inky Boys' presents a blackface caricature.\n\nStruwwelpeter is both a landmark in the history of illustrated children's literature — one of the first books to treat children as a specific audience for visually illustrated narrative — and a disturbing document in the history of pedagogy, discipline, and childhood. Its extreme violence (thumb-cutting, death by starvation, death by fire) reflects the 19th-century belief that frightening stories were an appropriate means of moral instruction for children; later scholarship has analysed Struwwelpeter as a document of Victorian-era anxieties about childhood obedience, bodily control, and social conformity.\n\nStruwwelpeter's cultural legacy is extensive — it influenced German and European children's literature, generated numerous parodies (including Hilaire Belloc's Cautionary Tales for Children, 1907, and the political parody Der Struwwelpeter: Eine Adventskinder-Schreckschreck, with Hitler as Struwwelpeter), and its imagery entered German and European popular culture. The 'scissor-man' figure has become a symbol of violent disciplinary authority in cultural analysis, and Struwwelpeter is frequently studied in the context of the history of childhood, discipline, and children's literature.",
    "causes": [
      "Heinrich Hoffmann's dissatisfaction with the children's books available for his son Karl's Christmas gift (1844) — he found them didactic, dull, and unsuitable for young children — led him to create his own illustrated book combining visual vividness, humour, and moral instruction, which he originally printed privately and then published in 1845.",
      "The 19th-century German pedagogical tradition — the belief that moral instruction of children required clear consequences for bad behaviour, and that frightening stories could be effective instruments of discipline — provided the cultural context for Struwwelpeter's extreme punishments, which Hoffmann intended as darkly humorous rather than genuinely threatening.",
      "The development of illustrated books for children as a distinct genre — the technical possibilities of coloured illustration in printed books, the growing middle-class market for children's books, and the professionalisation of childhood education — created the commercial and cultural context for Struwwelpeter's publication and success."
    ],
    "effects": [
      "Struwwelpeter was a founding text of illustrated German children's literature — its commercial success (millions of copies, 20+ language translations) established the illustrated cautionary tale as a major genre and demonstrated the viability of books specifically designed for young children with visual narrative.",
      "Struwwelpeter's influence on 19th and 20th-century European children's literature was extensive — it inspired Hilaire Belloc's Cautionary Tales for Children (1907) and numerous other satirical cautionary tale collections, as well as political parodies that used its format to critique authority figures.",
      "Struwwelpeter has become a central text in the history of childhood and discipline — studied in the context of Victorian-era anxieties about childhood obedience, bodily control, and social conformity, the book's extreme punishments are analysed as documents of 19th-century pedagogical ideology and its transformation in the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "heinrich-hoffmann", "sourceName": "Heinrich Hoffmann (1809–1894, Frankfurt physician and illustrator)", "verb": "AUTHORS", "targetSlug": "struwwelpeter", "targetName": "Struwwelpeter (1845 — cautionary tales with grotesque punishments; 20+ translations)", "context": "Hoffmann created Struwwelpeter in 1844 as a Christmas gift for his son — published in 1845, it became one of the best-selling children's books of the 19th century with millions of copies sold."},
      {"sourceSlug": "struwwelpeter", "sourceName": "Struwwelpeter (illustrated cautionary tales — 19th-century children's literature)", "verb": "FOUNDS", "targetSlug": "illustrated-childrens-literature", "targetName": "Illustrated German children's literature (19th century — cautionary tale genre)", "context": "Struwwelpeter's commercial success established the illustrated cautionary tale as a major genre in German and European children's literature — its format was widely imitated."},
      {"sourceSlug": "struwwelpeter", "sourceName": "Struwwelpeter (scissor-man, Daumenlutscher — Victorian discipline and childhood)", "verb": "DOCUMENTS", "targetSlug": "history-of-childhood-discipline", "targetName": "History of childhood and discipline (Victorian era — bodily control, moral instruction)", "context": "Struwwelpeter's extreme punishments (thumb-cutting, death by fire, starvation) are studied as documents of Victorian pedagogical ideology — the belief that frightening stories were appropriate moral instruction for children."}
    ],
    "places": [
      {"name": "Frankfurt am Main, Germany (Hoffmann's creation 1844; Rütten und Loening publication 1845)", "role": "Hoffmann created Struwwelpeter in Frankfurt as a private Christmas gift (1844) and published it with Frankfurt's Rütten und Loening in 1845 — the book became an international bestseller from its Frankfurt origins"},
      {"name": "Germany and Europe (20+ language translations; millions of copies — 19th–20th century cultural reach)", "role": "Struwwelpeter was translated into 20+ languages and sold millions of copies across Germany and Europe — its imagery entered German and European popular culture and inspired political parodies"}
    ],
    "subjects": ["German Literature", "19th Century", "Children's Literature", "Illustrated Books", "Heinrich Hoffmann", "Pedagogy", "Cautionary Tales", "Victorian Era"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Struwwelpeter (1845) is one of the most influential and disturbing children's books of the 19th century — its illustrated cautionary tales with extreme punishments established the illustrated children's book genre in Germany and Europe, sold millions of copies in 20+ translations, and became a central text in the history of childhood, discipline, and pedagogy.",
      "significanceCategory": "highly-significant"
    }
  }
},

"snow-white": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780snow-white.json",
  "slug": "snow-white",
  "data": {
    "summary": "Snow White (German: Schneewittchen) is a German fairy tale first recorded by Jacob and Wilhelm Grimm in their Kinder- und Hausmärchen ('Children's and Household Tales', 1st edition, 1812) as tale KHM 53, and subsequently revised in later editions (the 7th edition, 1857, being the most widely read). The tale narrates the story of a young princess (Snow White) whose beauty provokes the murderous jealousy of her stepmother, the Evil Queen, who repeatedly attempts to kill Snow White (first ordering a hunter to cut out her heart, then attempting to murder her with a poisoned comb, a laced bodice, and finally a poisoned apple). Snow White takes refuge with seven dwarfs in the forest, is placed in a glass coffin by the grieving dwarfs after the poisoned apple falls, and is eventually revived by a prince's kiss (or, in the 1812 version, when a servant jostles the coffin and the piece of apple falls from her throat).\n\nSnow White is one of the most widely known and analysed fairy tales in world literature — its ATU type classification (ATU 709) groups it with related tales across Europe, and the Snow White story exists in versions in German, Italian (Giambattista Basile's 'La bella addormentata nel bosco', 1634), and related tales from Albania, Russia, Armenia, and the African oral tradition. The tale has been analysed as a patriarchal narrative of female competition for male approval (the Evil Queen's anxiety about the mirror's verdict: 'who is the fairest of them all?'), as a coming-of-age initiation story, as a narrative of female sexual awakening and dormancy, and as a document of early modern German folk culture.\n\nSnow White's global cultural reach is largely the product of Walt Disney's Snow White and the Seven Dwarfs (1937) — the first feature-length animated film produced in Hollywood, a commercial and artistic triumph that permanently shaped the visual iconography of Snow White (the glass coffin, the seven dwarfs' names, the red apple) and introduced the Grimm fairy tale tradition to global cinema audiences. The Disney film's success made Snow White one of the three or four best-known fairy tale figures worldwide, alongside Cinderella, Sleeping Beauty, and Red Riding Hood.",
    "causes": [
      "The Brothers Grimm's project of German folkloric collection — the desire to record and preserve the German oral narrative tradition as a contribution to national cultural identity — drove the collection of Snow White from oral informants (primarily the Hassenpflug family and other Hessian informants, who were themselves influenced by earlier French literary fairy tales) and its inclusion in the Kinder- und Hausmärchen (1812).",
      "The pan-European fairy tale tradition — the ATU type 709 story of a beautiful young woman threatened by a jealous older woman and rescued by a prince exists across European cultures, with literary versions in Basile's Neapolitan Pentamerone (1634) and the Grimm collection (1812) — provided a shared narrative substrate from which the Snow White tale emerged.",
      "Walt Disney's decision to adapt Snow White as the first feature-length animated film (1937) — a five-year production at enormous cost ($1.5 million, thought 'Disney's folly') that became the highest-grossing sound film of its era — transformed the Grimm tale into a globally known narrative and established the visual iconography of Snow White that has dominated subsequent adaptations."
    ],
    "effects": [
      "Walt Disney's Snow White and the Seven Dwarfs (1937) was the first feature-length animated film and a landmark in cinema history — its commercial success ($8 million in its initial run) validated the animated feature film as a viable art form and commercial genre, establishing the Disney studio's dominance of feature animation that continues to the present.",
      "The Snow White narrative — the Evil Queen, the magic mirror, the poisoned apple, the glass coffin, the seven dwarfs — has become one of the most widely recognised narrative structures in world culture, generating hundreds of literary, theatrical, cinematic, and operatic adaptations across two centuries and multiple cultural traditions.",
      "Snow White's feminist interpretation — the tale's central anxiety ('who is the fairest of them all?') as a narrative of female competition for male approval and female agency suppressed — has made it a central text in feminist analysis of fairy tales (Bruno Bettelheim, Sandra Gilbert, Angela Carter), generating a rich critical tradition and numerous revisionary retellings."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (Jacob 1785–1863 and Wilhelm 1786–1859, Kinder- und Hausmärchen 1812)", "verb": "RECORDS", "targetSlug": "snow-white", "targetName": "Snow White (KHM 53, Kinder- und Hausmärchen, 1st ed. 1812; 7th ed. 1857)", "context": "The Brothers Grimm recorded Snow White in their Kinder- und Hausmärchen (1812) — the tale was revised in subsequent editions with the 7th edition (1857) becoming the standard text."},
      {"sourceSlug": "snow-white", "sourceName": "Snow White (Disney 1937 — first feature animated film, highest-grossing sound film of its era)", "verb": "ADAPTED_AS", "targetSlug": "snow-white-disney-1937", "targetName": "Snow White and the Seven Dwarfs (Walt Disney, 1937 — first feature-length animated film)", "context": "Walt Disney's Snow White (1937) was the first feature-length animated film — its commercial success validated animated feature films as a commercial art form and established the Disney studio's dominance of animation."},
      {"sourceSlug": "snow-white", "sourceName": "Snow White (Evil Queen, magic mirror — feminist analysis, female competition)", "verb": "EXAMINED_BY", "targetSlug": "feminist-fairy-tale-criticism", "targetName": "Feminist fairy tale criticism (Bettelheim, Gilbert, Carter — 20th century)", "context": "Snow White is a central text in feminist fairy tale analysis — its 'fairest of them all' anxiety is examined as a narrative of female competition for male approval and female agency suppressed in patriarchal culture."}
    ],
    "places": [
      {"name": "Germany (Hessian oral tradition — Grimm collection 1812; 7th edition 1857 definitive text)", "role": "Snow White was recorded by the Grimm brothers from Hessian oral informants (primarily the Hassenpflug family) in Germany — the Kinder- und Hausmärchen (1812, 7th edition 1857) is the definitive text"},
      {"name": "United States (Walt Disney Studios, Hollywood — Snow White and the Seven Dwarfs 1937)", "role": "Walt Disney's 1937 Snow White — produced in Hollywood — gave the tale its globally known visual iconography and introduced it to worldwide cinema audiences"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Disney Animation", "Folklore", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Snow White (Grimm, KHM 53, 1812) is one of the most widely known fairy tales in world literature — its Disney adaptation (1937), the first feature-length animated film, gave it global cultural reach and established the visual iconography recognised worldwide. As a subject of feminist criticism and a document of pan-European folk narrative tradition (ATU 709), it is among the most analysed fairy tales in world literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-emperors-new-clothes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-emperors-new-clothes.json",
  "slug": "the-emperors-new-clothes",
  "data": {
    "summary": "The Emperor's New Clothes (Danish: Kejserens nye Klæder) is a fairy tale by the Danish author Hans Christian Andersen (1805–1875), first published on 7 April 1837 in the first instalment of Eventyr fortalte for Børn ('Fairy Tales Told for Children') alongside The Tinderbox, Little Claus and Big Claus, and The Princess on the Pea. The tale is based on a Spanish story recorded by Juan Manuel in El Conde Lucanor (1335), which Andersen read in a German translation — an early example of Andersen's adaptation of oral and literary sources into his own distinctive literary fairy tale voice.\n\nThe Emperor's New Clothes tells the story of two swindlers who persuade a vain Emperor that they are weaving him a magnificent suit of clothes invisible to anyone who is stupid or unfit for their position — each of the Emperor's courtiers, afraid to reveal that they see nothing, praises the non-existent suit; the Emperor himself, driven by vanity and fear of appearing stupid, parades in his 'new clothes' before his subjects until a child cries out: 'But he hasn't got anything on!' The tale is a fable of collective self-deception, sycophancy, and the power of a child's honest perception to expose the social pretence that adults collude in maintaining.\n\nThe Emperor's New Clothes has entered the English language and most European languages as an idiom for collective self-deception and willingness to follow a false consensus — 'the Emperor has no clothes' is one of the most widely used phrases in political and cultural commentary worldwide. The tale is cited in contexts ranging from corporate groupthink and financial bubbles to political authoritarianism and cultural conformism, making it one of the most practically applied narrative frameworks in modern culture. Its philosophical resonance — the question of who has the courage to speak the truth in a social context organised around a convenient lie — gives it continuing relevance across political and cultural contexts.",
    "causes": [
      "Juan Manuel's Spanish source story in El Conde Lucanor (1335) — the tale of a cloth visible only to legitimate sons — provided the narrative germ that Andersen adapted, shifting the moral focus from legitimacy to vanity and collective self-deception.",
      "Andersen's specific literary gift — his ability to transform folk tale and literary sources into psychologically acute observations of human weakness — gave the tale its distinctive version, in which the Emperor's vanity, the courtiers' sycophancy, and the collective maintenance of a social lie are rendered with precision.",
      "The political context of 1830s Denmark — a period of court culture, aristocratic deference, and the social expectation of conformity to official narratives — provided the specific social target of Andersen's satire, which exposed the deference to authority that his own experience of court culture had taught him."
    ],
    "effects": [
      "'The Emperor has no clothes' has entered virtually every major European and many non-European languages as an idiom for collective self-deception and the willingness to follow a false consensus — one of the most widely used phrases in political and cultural commentary, applied to financial bubbles, corporate groupthink, political authoritarianism, and cultural conformism.",
      "The tale is cited in management theory, psychology, and political analysis as a description of groupthink and organisational conformity — the phenomenon of collective self-deception in which individuals suppress their own perceptions to conform to a false group consensus is named 'Emperor's New Clothes syndrome' in organisational behaviour literature.",
      "The Emperor's New Clothes is one of the most widely adapted of all fairy tales in political satire and commentary — adapted as a critique of every form of authority from communist regimes to corporate culture, the tale's structure provides a ready template for exposing the gap between official narrative and observable reality."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875, Danish author)", "verb": "AUTHORS", "targetSlug": "the-emperors-new-clothes", "targetName": "The Emperor's New Clothes (1837 — collective self-deception fable)", "context": "Andersen published The Emperor's New Clothes in the first instalment of Eventyr fortalte for Børn (1837) — adapting a Spanish source story from Juan Manuel's El Conde Lucanor (1335) into his own distinctive literary fairy tale."},
      {"sourceSlug": "the-emperors-new-clothes", "sourceName": "The Emperor's New Clothes (collective self-deception — 'the Emperor has no clothes')", "verb": "PROVIDES_FRAMEWORK_FOR", "targetSlug": "collective-self-deception", "targetName": "Collective self-deception and groupthink (psychology, management theory, political commentary)", "context": "The Emperor's New Clothes has become the primary cultural reference point for collective self-deception and groupthink — the phrase 'the Emperor has no clothes' is used in political analysis, management theory, and cultural commentary worldwide."},
      {"sourceSlug": "juan-manuel", "sourceName": "Juan Manuel (1282–1348, Spanish nobleman and author — El Conde Lucanor 1335)", "verb": "SOURCE_FOR", "targetSlug": "the-emperors-new-clothes", "targetName": "The Emperor's New Clothes (Andersen 1837 — adapts Juan Manuel's tale of invisible cloth)", "context": "Andersen adapted The Emperor's New Clothes from a story in Juan Manuel's El Conde Lucanor (1335) — which told of a cloth visible only to legitimate sons, which Andersen transformed into a tale of vanity and collective self-deception."}
    ],
    "places": [
      {"name": "Denmark (Andersen's Copenhagen — Eventyr fortalte for Børn, first instalment, April 1837)", "role": "Andersen published The Emperor's New Clothes in Copenhagen in April 1837 — the tale reflected his experience of Danish court culture and the social expectation of deference to authority"},
      {"name": "Global (virtually every language — 'the Emperor has no clothes' as worldwide idiom)", "role": "The Emperor's New Clothes has been translated into virtually every major language and its central phrase has become a worldwide idiom for collective self-deception — one of the most globally diffused of all narrative metaphors"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Social Commentary", "Satire", "Folk Literature", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Emperor's New Clothes (Andersen, 1837) is one of the most globally diffused narrative frameworks in world culture — the phrase 'the Emperor has no clothes' is used in virtually every major language as an idiom for collective self-deception and the exposure of false consensus. Its applications in political commentary, management theory, and cultural analysis make it one of the most practically cited fairy tales in modern discourse.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-snow-queen": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-snow-queen.json",
  "slug": "the-snow-queen",
  "data": {
    "summary": "The Snow Queen (Danish: Snedronningen) is a fairy tale by Hans Christian Andersen (1805–1875), first published on 21 December 1844 in the fifth and final volume of Eventyr fortalte for Børn ('Fairy Tales Told for Children'), alongside The Fir Tree. The Snow Queen is Andersen's longest fairy tale and is widely regarded as one of his greatest — a seven-part narrative of love, adventure, and the rescue of a boy named Kai from the Snow Queen's palace by his friend (and in some readings, his true love) Gerda. Kai's heart has been pierced by a shard of a demon's magic mirror that makes him see only the bad and ugly in everything; Gerda's journey through seasons and kingdoms to find him — meeting a sorceress, robbers, a reindeer, and various magical helpers — ends in the Snow Queen's icy palace, where Gerda's tears and love dissolve the mirror shards from Kai's heart and eye.\n\nThe Snow Queen is an original Andersen tale — unlike his other fairy tales based on oral sources (Thumbelina, The Little Mermaid, The Wild Swans), The Snow Queen is largely Andersen's own invention, drawing loosely on Danish winter mythology but primarily on his own imagination and life experience. Scholars have identified autobiographical elements — the contrast between cold rationality (Kai's mirror-shard view) and warm emotion (Gerda's faithful love) has been read as reflecting Andersen's own creative conflict; and Kai and Gerda's friendship has been read as reflecting Andersen's relationships with his childhood friend Riborg Voigt and his complex emotional life.\n\nThe Snow Queen achieved global cultural reach through Disney's Frozen (2013) — a loose adaptation that made the Snow Queen story the highest-grossing animated film ever made at the time of its release, with the song 'Let It Go' becoming a global cultural phenomenon and the film's themes of sisterhood and female empowerment representing a significant departure from the Andersen original. The commercial and cultural impact of Frozen has made the Snow Queen one of the three or four most recognised Andersen tales worldwide.",
    "causes": [
      "Andersen's creative development in the early 1840s — his movement toward longer, more complex fairy tales with psychological depth — produced The Snow Queen as his most ambitious work of fairy tale fiction, drawing on his imagination, autobiographical experience, and Danish winter mythology.",
      "Danish winter mythology and folklore — the cultural imagery of the 'Snow Queen' as a personification of winter, cold, and death in Scandinavian tradition — provided the central figure of the tale, which Andersen transformed from a folk personification into a complex allegorical figure of cold reason and aesthetic perfection.",
      "Andersen's personal experience of emotional coldness and artistic alienation — his sense of being both gifted and socially marginalised, his complex relationships with men and women he loved — gave the tale's central opposition of warm feeling (Gerda) against cold rationalism (the Snow Queen and Kai's mirror-shard perception) its psychological intensity."
    ],
    "effects": [
      "The Snow Queen is regarded as one of Andersen's greatest and most psychologically complex tales — its structure of a faithful journey of love overcoming cold rationalism has influenced European and American fantasy fiction (C.S. Lewis's The Lion, the Witch and the Wardrobe draws on the Snow Queen figure for the White Witch), and it established the pattern of a determined young girl as the protagonist of a quest narrative.",
      "Walt Disney's Frozen (2013) — a loose adaptation of The Snow Queen — became the highest-grossing animated film of its time ($1.27 billion), with the song 'Let It Go' becoming a global phenomenon, and its themes of sisterhood and female empowerment transforming the Snow Queen story into one of the most commercially successful fairy tale adaptations in history.",
      "The Snow Queen's influence on C.S. Lewis's The Lion, the Witch and the Wardrobe (1950) — Lewis acknowledged the White Witch as directly inspired by Andersen's Snow Queen — demonstrates the tale's importance in the tradition of Northern European fantasy literature and its influence on the development of children's fantasy fiction."
    ],
    "relationships": [
      {"sourceSlug": "hans-christian-andersen", "sourceName": "Hans Christian Andersen (1805–1875, Danish author — original creation, not folk adaptation)", "verb": "AUTHORS", "targetSlug": "the-snow-queen", "targetName": "The Snow Queen (1844 — Andersen's longest and most psychologically complex fairy tale)", "context": "Andersen published The Snow Queen on 21 December 1844 — his longest fairy tale, largely an original creation drawing on Danish winter mythology and autobiographical experience."},
      {"sourceSlug": "the-snow-queen", "sourceName": "The Snow Queen (White Witch — C.S. Lewis's Narnia; Northern European fantasy)", "verb": "INFLUENCES", "targetSlug": "the-lion-the-witch-and-the-wardrobe", "targetName": "The Lion, the Witch and the Wardrobe (C.S. Lewis, 1950 — White Witch inspired by Snow Queen)", "context": "C.S. Lewis acknowledged that the White Witch in The Lion, the Witch and the Wardrobe (1950) was directly inspired by Andersen's Snow Queen — demonstrating the tale's importance in Northern European fantasy fiction."},
      {"sourceSlug": "the-snow-queen", "sourceName": "The Snow Queen (Frozen 2013 — highest-grossing animated film; Let It Go; sisterhood themes)", "verb": "ADAPTED_AS", "targetSlug": "frozen-2013", "targetName": "Frozen (Disney, 2013 — highest-grossing animated film of its time, $1.27 billion)", "context": "Disney's Frozen (2013) — a loose adaptation of The Snow Queen — became the highest-grossing animated film of its time, with 'Let It Go' becoming a global cultural phenomenon and the film transforming Andersen's tale into one of the most commercially successful fairy tale adaptations in history."}
    ],
    "places": [
      {"name": "Denmark (Copenhagen — Andersen's imagination and autobiographical experience; Scandinavian winter mythology)", "role": "The Snow Queen was published in Copenhagen in December 1844 — drawing on Andersen's own imagination, Danish winter mythology, and autobiographical experience of emotional coldness and artistic alienation"},
      {"name": "Global (C.S. Lewis's Narnia; Disney's Frozen 2013 — $1.27 billion; worldwide cultural reach)", "role": "The Snow Queen's cultural reach extended globally — influencing C.S. Lewis's Narnia (1950) and Disney's Frozen (2013), one of the highest-grossing films of all time"}
    ],
    "subjects": ["Danish Literature", "19th Century", "Fairy Tale", "Hans Christian Andersen", "Fantasy Literature", "Children's Literature", "Disney Animation", "Folk Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Snow Queen (Andersen, 1844) is one of the greatest and most psychologically complex fairy tales in world literature — its influence on C.S. Lewis's Narnia (1950) and Disney's Frozen (2013, highest-grossing animated film of its era) gives it extraordinary cultural reach. Andersen's original creation established the pattern of a determined young female protagonist on a quest of faithful love that has shaped children's fantasy fiction and cinema.",
      "significanceCategory": "world-changing"
    }
  }
},

"rapunzel": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780rapunzel.json",
  "slug": "rapunzel",
  "data": {
    "summary": "Rapunzel is a German fairy tale first recorded in published form by Friedrich Schulz in his Kleine Romane (1790), under the title 'Rapunzel', based on a French source story by Charlotte-Rose de Caumont de La Force ('Persinette', 1698), which was itself derived from Giambattista Basile's 'Petrosinella' in the Pentamerone (Naples, 1634). The Brothers Grimm included Rapunzel as tale KHM 12 in their Kinder- und Hausmärchen (1st edition, 1812), and it is primarily through the Grimm version (revised in the 7th edition, 1857 — sanitising the original's references to Rapunzel's pregnancy) that the tale became internationally known. The tale narrates the story of a girl with extraordinarily long golden hair, imprisoned by an enchantress in a tall tower (without a door), who lets down her hair as a ladder for the enchantress (and, later, a prince) to climb — the prince's discovery, the enchantress's punishment (cutting Rapunzel's hair and banishing her to a desert), and the prince's blinding by thorns and eventual reunion with Rapunzel in the desert.\n\nRapunzel belongs to the ATU type 310 ('The Maiden in the Tower') folk tale category, which exists in multiple European and Middle Eastern versions — the most widely distributed motif is of a beautiful girl imprisoned in an inaccessible tower. The tale's central symbol — the hair as rope, the tower as prison, the cutting of hair as punishment and liberation — has generated rich literary and feminist analysis: the tower as patriarchal enclosure, the hair as female sexuality and power, and Rapunzel's relationship with the enchantress as a complex of female power, dependence, and control.\n\nRapunzel's global cultural reach in the 21st century is largely the product of Disney's Tangled (2010) — a computer-animated adaptation that reimagined Rapunzel as an adventurous protagonist and the tower as protective enclosure rather than prison, grossing $590 million worldwide and establishing Rapunzel as a major Disney Princess figure. The tale has also been the subject of numerous literary retellings, from Angela Carter's feminist reimagining to Donna Jo Napoli's novel Zel (1996).",
    "causes": [
      "The pan-European folk narrative tradition of the 'Maiden in the Tower' (ATU type 310) — the story of a beautiful girl imprisoned in an inaccessible tower by a supernatural guardian — provided the shared narrative substrate from which the Italian (Basile, 1634), French (La Force, 1698), German (Schulz, 1790; Grimm, 1812) versions of the Rapunzel story emerged.",
      "The Brothers Grimm's collection project — the desire to document and preserve the German oral fairy tale tradition — drove the recording of Rapunzel in the Kinder- und Hausmärchen (1812), though the Grimm version draws more on the literary French tradition than on authentic German oral sources, and was sanitised in later editions.",
      "The early modern European literary fairy tale tradition — Basile's Pentamerone (1634) and La Force's Contes des fées (1698) — provided the literary sources from which the Rapunzel story was transmitted to the Grimm brothers, demonstrating the complex transmission of fairy tale narratives between oral and literary traditions and across national boundaries."
    ],
    "effects": [
      "Rapunzel has become one of the most widely known fairy tale figures worldwide — the image of the long-haired girl in the tower calling 'Rapunzel, Rapunzel, let down your hair' is recognised across cultures and has generated hundreds of literary, theatrical, and cinematic adaptations, making it one of the most frequently retold of all European fairy tales.",
      "Rapunzel is a central text in feminist fairy tale analysis — the tower as patriarchal enclosure, the cutting of Rapunzel's hair as punishment for sexuality, and the enchantress-Rapunzel relationship as a complex of female power and control are analysed by feminist critics (Sandra Gilbert, Susan Gubar, Anne Sexton) as a narrative of female sexuality and patriarchal constraint.",
      "Disney's Tangled (2010) gave Rapunzel a new global profile — the film's reimagining of Rapunzel as an active, adventurous protagonist grossed $590 million worldwide and established Rapunzel as a major Disney Princess figure, demonstrating the continuing vitality of the fairy tale tradition as a vehicle for contemporary gender narratives."
    ],
    "relationships": [
      {"sourceSlug": "brothers-grimm", "sourceName": "Brothers Grimm (Jacob 1785–1863 and Wilhelm 1786–1859, Kinder- und Hausmärchen 1812)", "verb": "RECORDS", "targetSlug": "rapunzel", "targetName": "Rapunzel (KHM 12, Kinder- und Hausmärchen, 1st ed. 1812; 7th ed. 1857)", "context": "The Grimm brothers recorded Rapunzel in their Kinder- und Hausmärchen (1812) — adapting the French literary source (La Force, 1698) and sanitising the original's references to Rapunzel's pregnancy in later editions."},
      {"sourceSlug": "rapunzel", "sourceName": "Rapunzel (tower, hair, enchantress — feminist analysis of female sexuality and patriarchal constraint)", "verb": "EXAMINED_BY", "targetSlug": "feminist-fairy-tale-criticism", "targetName": "Feminist fairy tale criticism (Gilbert, Gubar, Anne Sexton — tower as patriarchal enclosure)", "context": "Rapunzel is a central text in feminist fairy tale analysis — the tower as patriarchal enclosure and the cutting of Rapunzel's hair as punishment for female sexuality are analysed as narratives of patriarchal constraint and female power."},
      {"sourceSlug": "rapunzel", "sourceName": "Rapunzel (Tangled Disney 2010 — $590 million; Disney Princess; active female protagonist)", "verb": "ADAPTED_AS", "targetSlug": "tangled-2010", "targetName": "Tangled (Disney, 2010 — Rapunzel as active protagonist, $590 million worldwide)", "context": "Disney's Tangled (2010) reimagined Rapunzel as an active, adventurous protagonist — grossing $590 million worldwide and establishing Rapunzel as a major Disney Princess figure."}
    ],
    "places": [
      {"name": "Germany (Brothers Grimm — KHM 12, 1812; based on French literary tradition via Charlotte-Rose de Caumont)", "role": "The Brothers Grimm recorded Rapunzel in Germany in 1812 — drawing more on the French literary tradition (La Force, 1698) than on authentic German oral sources, demonstrating the complex literary transmission of fairy tale narratives"},
      {"name": "Italy (Basile's Pentamerone, Naples 1634 — 'Petrosinella'; earliest known literary version)", "role": "The earliest known literary version of the Rapunzel story is Basile's 'Petrosinella' in the Pentamerone (Naples, 1634) — demonstrating the Italian origin of the story before its French and German adaptations"}
    ],
    "subjects": ["German Literature", "19th Century", "Fairy Tale", "Brothers Grimm", "Folk Literature", "Disney Animation", "Feminist Criticism", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Rapunzel (Grimm, KHM 12, 1812; with origins in Basile 1634 and La Force 1698) is one of the most widely known fairy tales in world literature — its image of the girl in the tower with impossibly long hair is globally recognised. Disney's Tangled (2010, $590 million) gave it 21st-century cultural reach; feminist analysis of the tower and hair as symbols of patriarchal constraint makes it a central text in fairy tale scholarship.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-mousetrap": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-mousetrap.json",
  "slug": "the-mousetrap",
  "data": {
    "summary": "The Mousetrap is a murder mystery play by Agatha Christie (1890–1976), first performed at the Ambassadors Theatre, London, on 25 November 1952, and transferred to St Martin's Theatre in March 1974, where it has run continuously to the present day — making it, as of 2024, the longest-running play in theatrical history, with over 28,000 performances. The play originated as a short BBC radio programme Three Blind Mice (1947), commissioned for Queen Mary's 80th birthday broadcast, which Christie expanded into a play at the request of actor-producer Richard Attenborough and his wife Sheila Sim. The plot concerns a group of guests snowbound at Monkswell Manor, a newly opened guest house, following the murder of a London woman — a detective investigating the case reveals that all of the guests have a connection to the murdered woman, and a second murder occurs before the murderer is unmasked.\n\nThe Mousetrap has a famous tradition of audience-participation: at the end of the play, an actor asks the audience not to reveal the identity of the murderer — a theatrical convention that has been maintained for over 70 years, making 'who did it in The Mousetrap?' one of the most successfully kept theatrical secrets in history. The identity of the killer remains widely known to theatre professionals but is rarely published in mainstream media, and Christie herself regarded the surprise ending as essential to the play's success. The Mousetrap holds a unique cultural position as both the longest-running play in theatre history and a living institution of British theatrical culture.\n\nThe Mousetrap's longevity is as much a social and commercial phenomenon as a literary one — its remarkable run reflects the loyalty of West End theatre audiences to a formula that has become a cultural institution, the steady stream of tourists to London who see it as a required theatrical experience, and the extraordinary durability of the Agatha Christie brand in global popular culture. As of 2024, the production has grossed over £100 million, making it one of the most commercially successful theatrical productions in history.",
    "causes": [
      "Agatha Christie's commission from the BBC (1947) — the request for a short radio programme for Queen Mary's 80th birthday — produced the radio play Three Blind Mice, which Christie then expanded into a stage play at the request of Richard Attenborough and Sheila Sim, who produced the theatrical version.",
      "The post-war London theatre environment — the demand for reliable, commercially safe theatrical entertainment in the 1950s West End, the appetite for mystery plays among London and tourist audiences, and the established Christie brand — created the commercial conditions for The Mousetrap's initial success.",
      "The 'whodunit' tradition in English popular fiction — the Golden Age of Detective Fiction (Christie, Dorothy L. Sayers, John Dickson Carr) established the murder mystery as a central genre of British popular culture — provided the generic conventions that The Mousetrap deploys and that audiences bring pre-formed expectations to."
    ],
    "effects": [
      "The Mousetrap has run continuously since 1952 (with only brief interruptions, including the COVID-19 closure in March 2020 and reopening in May 2021) — achieving over 28,000 performances and becoming the longest-running play in theatre history, a record that appears unlikely to be broken.",
      "The Mousetrap's commercial success (grossing over £100 million since 1952) established the model for the long-running West End theatrical institution — the play has sustained St Martin's Theatre as a permanent West End home and has become a model for theatrical longevity, demonstrating that a commercial play can outlast its initial cultural context by decades.",
      "The Mousetrap's tradition of secrecy about the murderer's identity — maintained by audiences across 70+ years through the play's closing appeal — is a remarkable example of collective theatrical ritual and a unique cultural institution, demonstrating the power of theatrical community and audience loyalty in maintaining a shared secret."
    ],
    "relationships": [
      {"sourceSlug": "agatha-christie", "sourceName": "Agatha Christie (1890–1976, British crime writer — Queen of Crime)", "verb": "AUTHORS", "targetSlug": "the-mousetrap", "targetName": "The Mousetrap (1952 — longest-running play in theatre history; 28,000+ performances)", "context": "Christie wrote The Mousetrap from her BBC radio play Three Blind Mice (1947) — opened at the Ambassadors Theatre, London, in November 1952 and has run continuously since, achieving over 28,000 performances."},
      {"sourceSlug": "the-mousetrap", "sourceName": "The Mousetrap (longest-running play — St Martin's Theatre, West End; 28,000+ performances)", "verb": "HOLDS_RECORD_FOR", "targetSlug": "theatrical-longevity", "targetName": "Longest-running play in theatre history (West End — commercial theatrical institution)", "context": "The Mousetrap has run continuously since 1952 (over 28,000 performances by 2024) — the longest-running play in theatre history and one of the most commercially successful theatrical productions ever."},
      {"sourceSlug": "the-mousetrap", "sourceName": "The Mousetrap (secret ending — audience appeal; 70+ years of theatrical secrecy)", "verb": "EXEMPLIFIES", "targetSlug": "theatrical-ritual", "targetName": "Theatrical ritual and audience community (West End institution; collective secrecy)", "context": "The Mousetrap's tradition of secrecy — the closing appeal to audiences not to reveal the murderer — has been maintained across 70+ years, demonstrating the power of theatrical ritual and collective audience loyalty to maintain a shared secret."}
    ],
    "places": [
      {"name": "London, England (Ambassadors Theatre 1952; St Martin's Theatre 1974–present — West End)", "role": "The Mousetrap opened at the Ambassadors Theatre, London, in November 1952 and transferred to St Martin's Theatre in 1974 — the St Martin's Theatre has been its permanent home for 50+ years"},
      {"name": "United Kingdom (Agatha Christie estate; British theatrical culture — longest-running West End play)", "role": "The Mousetrap is a uniquely British theatrical institution — its extraordinary longevity reflects the loyalty of West End audiences, the steady stream of London tourists, and the global Agatha Christie brand"}
    ],
    "subjects": ["British Literature", "20th Century", "Agatha Christie", "Detective Fiction", "Theatre", "West End Theatre", "Murder Mystery", "Crime Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Mousetrap (Agatha Christie, 1952) is the longest-running play in theatre history — over 28,000 performances in over 70 years of continuous West End run, grossing over £100 million. Its famous tradition of audience secrecy about the murderer's identity is a unique theatrical institution; its longevity demonstrates the extraordinary commercial durability of the Agatha Christie brand in global popular culture.",
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
