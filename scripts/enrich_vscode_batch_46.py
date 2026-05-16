#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 46 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: prose-edda, the-adventures-of-sherlock-holmes, mother-courage-and-her-children,
          periplus-of-the-erythraean-sea, suda, samaveda, the-black-book-of-communism, o-fortuna
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-46-may2026"

ENRICHMENTS = {

"prose-edda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780prose-edda.json",
  "slug": "prose-edda",
  "data": {
    "summary": "The Prose Edda (Old Norse: Edda, also called Snorra Edda after its author) is an Old Norse work by the Icelandic chieftain, poet, and historian Snorri Sturluson (1179–1241), composed c. 1220 CE. Unlike the Poetic Edda (a collection of older mythological and heroic poems), the Prose Edda is a prose handbook for poets written by a single identifiable author — the most important writer of medieval Iceland. It consists of a Prologue and three main sections: the Gylfaginning ('The Deluding of Gylfi'), a systematic narrative of Norse mythology from the creation of the world to Ragnarök and its aftermath, presented as a dialogue between the disguised king Gylfi and the Æsir gods; the Skáldskaparmál ('The Language of Poetry'), a systematic account of the kennings (compound poetic expressions) and heiti (synonyms) used in Old Norse skaldic poetry, with extensive mythological and heroic narratives embedded to explain the origin of specific kennings; and the Háttatal ('Tally of Metres'), a poem demonstrating 102 distinct metres of Old Norse poetry with commentary.\n\nThe Prose Edda is both the most systematic account of Norse mythology available from a medieval Icelandic source and the primary reference work for understanding Old Norse skaldic poetry — its explanations of the kennings (periphrastic compound expressions like 'whale-road' for the sea, 'tree of the sword' for a warrior) and the mythological stories behind them are essential for reading the complex allusive poetry of the Viking Age skalds. Snorri composed the Prose Edda partly as a practical handbook for poets and partly as a nostalgic preservation of the pre-Christian poetic tradition he saw as endangered by Christianisation and the influence of foreign (Latinate) poetry.\n\nSnorri Sturluson's Prose Edda, alongside his Heimskringla (Kings' Sagas) and the Poetic Edda he helped preserve, makes him one of the most important figures in the history of medieval literature — a man who, in Christianised Iceland of the 13th century, systematically preserved and organised the pre-Christian mythological and poetic tradition of the North.",
    "causes": [
      "Snorri's perception that the tradition of skaldic poetry was being lost — that younger poets no longer understood the mythological allusions (kennings) embedded in the complex Old Norse court poetry of the Viking Age — motivated his project to create a systematic reference handbook that would explain the tradition and enable its continuation.",
      "The 13th-century Icelandic literary renaissance — the extraordinary creative and scholarly activity of Icelandic writers in the century after 1200 CE, which produced the family sagas, the kings' sagas, and the preservation of Old Norse mythological material — provided both the cultural context and the intellectual resources for Snorri's ambitious project.",
      "Snorri's visit to the Norwegian court (1218–1220) — where he experienced the demand for skaldic praise poetry and the prestige it conferred — reinforced his concern for the preservation of the skaldic tradition and provided the immediate practical context for composing a handbook that could guide aspiring skalds."
    ],
    "effects": [
      "The Prose Edda's Gylfaginning became the primary systematic account of Norse mythology used by 19th-century Romantic scholars, poets, and artists — Wagner's Ring Cycle, Tolkien's mythology, and the entire modern understanding of Norse mythology as a coherent cosmological system draws primarily on Snorri's narrative synthesis, which was itself a 13th-century Christian scholar's retrospective organisation of older material.",
      "The Prose Edda's systematic account of kennings and skaldic metres in the Skáldskaparmál and Háttatal is the primary reference work for modern scholars studying Old Norse poetry — without Snorri's handbook, much of Viking Age skaldic poetry would be unintelligible, as the kennings require the mythological knowledge that Snorri preserved.",
      "Snorri's narrative synthesis of Norse mythology in the Prose Edda, combined with the Poetic Edda's preservation of older poems, created the textual basis for the 19th-century Nordic revival — the Romantic nationalist interest in Norse mythology as the authentic spiritual heritage of the Germanic peoples that shaped Scandinavian national identities."
    ],
    "relationships": [
      {"sourceSlug": "snorri-sturluson", "sourceName": "Snorri Sturluson (1179–1241, Icelandic chieftain and scholar)", "verb": "AUTHORS", "targetSlug": "prose-edda", "targetName": "Prose Edda (Snorra Edda, c. 1220 CE)", "context": "Snorri Sturluson composed the Prose Edda c. 1220 CE — a systematic handbook of Norse mythology and skaldic poetry that became the primary reference for understanding Old Norse culture."},
      {"sourceSlug": "prose-edda", "sourceName": "Prose Edda (Gylfaginning, Norse cosmology)", "verb": "COMPANION_TO", "targetSlug": "poetic-edda", "targetName": "Poetic Edda (Codex Regius, c. 1270 CE)", "context": "The Prose Edda and Poetic Edda are the two primary sources for Norse mythology — Snorri's systematic prose account draws on and explains the older Eddic poems preserved in the Codex Regius."},
      {"sourceSlug": "prose-edda", "sourceName": "Prose Edda (Norse mythology synthesis, Romantic revival)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "tolkiens-middle-earth", "targetName": "Tolkien's Middle-earth and Norse-inspired modern culture", "context": "Snorri's Prose Edda is one of Tolkien's primary sources — its systematic account of Norse cosmology, the Æsir gods, and the mythological narratives shaped Tolkien's invented mythology and continues to underlie modern Norse-inspired fantasy."}
    ],
    "places": [
      {"name": "Iceland (Snorri's home — Reykholt; 13th-century literary renaissance)", "role": "Snorri composed the Prose Edda at Reykholt in western Iceland — the centre of his political power and scholarly activity, now a museum and research centre dedicated to his work"},
      {"name": "Norway (Snorri's visit 1218–1220; context for skaldic handbook)", "role": "Snorri's visit to the Norwegian court (1218–1220) — experiencing the demand for skaldic praise poetry — reinforced his motivation to compose a handbook preserving the skaldic tradition"}
    ],
    "subjects": ["Norse Literature", "Medieval Era", "Snorri Sturluson", "Norse Mythology", "Old Norse", "Skaldic Poetry", "Icelandic Literature", "Germanic Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Prose Edda (Snorri Sturluson, c. 1220 CE) is the most systematic account of Norse mythology from a medieval source and the primary reference work for understanding Old Norse skaldic poetry. Together with the Poetic Edda, it is the foundation of the modern understanding of Norse mythology — the source for Wagner's Ring Cycle, Tolkien's Middle-earth, and the entire tradition of Norse-inspired culture. Without Snorri's preservation effort, the pre-Christian Norse religious and literary tradition would be largely inaccessible.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-adventures-of-sherlock-holmes": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-adventures-of-sherlock-holmes.json",
  "slug": "the-adventures-of-sherlock-holmes",
  "data": {
    "summary": "The Adventures of Sherlock Holmes is a collection of twelve short stories by Sir Arthur Conan Doyle (1859–1930), first published in the Strand Magazine (July 1891 – June 1892) and collected in book form by George Newnes Ltd in October 1892. The twelve stories — 'A Scandal in Bohemia', 'The Red-Headed League', 'A Case of Identity', 'The Boscombe Valley Mystery', 'The Five Orange Pips', 'The Man with the Twisted Lip', 'The Adventure of the Blue Carbuncle', 'The Adventure of the Speckled Band', 'The Adventure of the Engineer's Thumb', 'The Adventure of the Noble Bachelor', 'The Adventure of the Beryl Coronet', and 'The Adventure of the Copper Beeches' — are among the most celebrated detective short stories in the English language, featuring the consulting detective Sherlock Holmes and his companion Dr. John H. Watson.\n\nThe Adventures of Sherlock Holmes was the first collection of the Holmes stories in the Strand Magazine, and the Strand's serialisation of the Holmes stories (1891–1927) is one of the landmark events in the history of mass-market magazine publishing and popular fiction. The Holmes stories in the Strand transformed Conan Doyle from a struggling novelist into the most popular fiction writer in Victorian and Edwardian England, and the demand for Holmes stories was so great that when Conan Doyle killed off Holmes in 'The Final Problem' (1893), public outcry forced him to revive the character (in 'The Adventure of the Empty House', 1903).\n\nSherlock Holmes — the consulting detective of 221B Baker Street, with his methods of scientific deduction, his violin, his cocaine habit (7% solution), his Moroccan tobacco, and his companion Watson — is the most famous fictional character in the English-speaking world and arguably the most widely recognised character in world literature. The Holmes stories established the conventions of the detective story genre — the brilliant detective with a distinctive personality and method, the Watson-figure as narrator and foil, the locked-room mystery, the revelation scene — that continue to define crime fiction.",
    "causes": [
      "The establishment of the Strand Magazine (1891) as a mass-market illustrated monthly — aimed at a middle-class Victorian readership, publishing short stories with illustrations in each issue — provided the ideal vehicle for the Holmes short story series: the Strand's large circulation (500,000 copies per issue by 1892) and its format (self-contained stories with a continuing protagonist) were perfectly matched to the Holmes series.",
      "Conan Doyle's formation of the Holmes character — drawing on Dr. Joseph Bell (his Edinburgh medical professor, famous for his powers of rapid observation and deduction), Edgar Allan Poe's Dupin stories, and Émile Gaboriau's detective fiction — combined existing detective story conventions with the specific character of Holmes's scientific method and personality.",
      "The Victorian fascination with science and empirical method — the cultural authority of scientific reasoning in the late 19th century, and the desire to apply it to social problems — made Holmes's method of observation and deduction culturally resonant: Holmes is a fantasy of scientific rationality applied to the messy contingency of crime."
    ],
    "effects": [
      "The Holmes stories established the conventions of the detective story as a genre: the brilliant detective with a distinctive method (observation, deduction, disguise), the Watson-figure as narrator and foil, the Baker Street address as a home base, the police as bumbling contrast, the locked-room mystery, the denouement revelation scene — conventions that became the template for Agatha Christie, Dorothy Sayers, P. D. James, and the entire subsequent tradition of crime fiction.",
      "Sherlock Holmes became the most adapted fictional character in history — with more screen adaptations than any other fictional character (according to the Guinness World Records), more pastiches, continuations, and derivative works than any other single fictional creation — demonstrating the extraordinary cultural durability of Conan Doyle's creation.",
      "The Holmes stories transformed the market for short detective fiction and made the short story collection a commercially viable form — their success in the Strand Magazine demonstrated the commercial potential of serialised short fiction featuring a recurring protagonist, a model that shaped subsequent popular magazine fiction through the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "arthur-conan-doyle", "sourceName": "Sir Arthur Conan Doyle (1859–1930)", "verb": "AUTHORS", "targetSlug": "the-adventures-of-sherlock-holmes", "targetName": "The Adventures of Sherlock Holmes (1892, 12 stories, Strand Magazine)", "context": "Conan Doyle published the Holmes stories in the Strand Magazine (1891–1892), collected as The Adventures of Sherlock Holmes (1892) — the most popular short stories of the Victorian era and the foundation of the detective fiction genre."},
      {"sourceSlug": "the-adventures-of-sherlock-holmes", "sourceName": "Holmes stories (detective conventions, brilliant detective genre)", "verb": "ESTABLISHES_CONVENTIONS_OF", "targetSlug": "detective-fiction-genre", "targetName": "Detective fiction genre (Agatha Christie, P. D. James, crime fiction)", "context": "The Holmes stories established the core conventions of the detective story — brilliant detective, Watson-figure narrator, deductive revelation — that became the template for Agatha Christie and the entire subsequent tradition of crime fiction."},
      {"sourceSlug": "the-adventures-of-sherlock-holmes", "sourceName": "Holmes stories (Strand Magazine, Victorian mass market)", "verb": "TRANSFORMS", "targetSlug": "victorian-magazine-publishing", "targetName": "Victorian mass-market magazine publishing (Strand Magazine model)", "context": "The Holmes series transformed the Strand Magazine into the dominant popular magazine of Victorian England — the demand for Holmes stories demonstrated the commercial potential of serialised short fiction with a recurring protagonist, shaping magazine publishing through the 20th century."}
    ],
    "places": [
      {"name": "London, England (Baker Street 221B; Holmes's fictional geography; late Victorian setting)", "role": "The Holmes stories are set in late Victorian London — Baker Street, the London fog, the hansom cabs, Scotland Yard — creating a fictional geography that became as real to readers as the actual city"},
      {"name": "Strand Magazine offices, London (serialisation vehicle, 1891–1927)", "role": "The Strand Magazine's serialisation of the Holmes stories (1891–1927) — reaching 500,000 copies per issue — was the publishing vehicle that made Holmes the most popular fictional character of his era"}
    ],
    "subjects": ["English Literature", "Modern Era", "Arthur Conan Doyle", "Detective Fiction", "Victorian Literature", "Short Stories", "Genre Fiction", "Popular Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Adventures of Sherlock Holmes (Conan Doyle, 1892) established the conventions of the detective fiction genre and created the most recognised fictional character in world literature. Holmes's influence on crime fiction (Agatha Christie, P. D. James, contemporary detective fiction), on popular culture, and on the culture of rational inquiry is unparalleled among fictional characters. With more screen adaptations than any other fictional character, Holmes is the definitive figure of detective fiction.",
      "significanceCategory": "world-changing"
    }
  }
},

"mother-courage-and-her-children": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780mother-courage-and-her-children.json",
  "slug": "mother-courage-and-her-children",
  "data": {
    "summary": "Mother Courage and Her Children (German: Mutter Courage und ihre Kinder) is a play in twelve scenes by the German playwright Bertolt Brecht (1898–1956), written in exile in Sweden in 1939 (within five weeks of the outbreak of the Second World War, which Brecht had anticipated), first performed in Zürich in 1941, and given its landmark production by Brecht's Berliner Ensemble in East Berlin in 1949 (with Helene Weigel in the title role), a production that defined Brecht's Epic Theatre in performance and became one of the most celebrated theatrical productions of the 20th century.\n\nThe play is set during the Thirty Years' War (1618–1648) and follows Anna Fierling ('Mother Courage'), a canteen woman who makes her living by following armies and selling provisions, food, and clothing to soldiers — and who loses all three of her children (Eilif the brave eldest, Swiss Cheese the honest second son, and the mute Kattrin) to the war while continuing to pursue her livelihood from it. The play's central irony — that Mother Courage, who has hitched her survival to the war, loses everything she loves through that same dependence — is the vehicle for Brecht's anti-war argument: war is not a heroic adventure but a commercial enterprise that destroys those who participate in it, and Mother Courage's inability to learn from her losses (she pulls her cart onward at the end) demonstrates the tragedy of those who cannot see the system that destroys them.\n\nMother Courage is the defining work of Brecht's Epic Theatre — his theoretical system of anti-illusionist, politically engaged theatre that uses the Verfremdungseffekt ('alienation effect', defamiliarisation) to prevent the audience from losing itself in emotional identification with the characters and instead to provoke critical thinking about the social and political forces at work in the play. Epic Theatre (songs that interrupt the action, direct addresses to the audience, placards, visible stage machinery) was designed to produce politically informed spectators rather than emotionally satisfied consumers of theatrical illusion.",
    "causes": [
      "The outbreak of the Second World War (September 1939) — which Brecht had anticipated and fled from, writing Mother Courage in Sweden within weeks of the invasion of Poland — was the immediate biographical and political context for the play: Brecht wrote it as an anti-war statement at the moment when European war resumed.",
      "Brecht's theoretical development of Epic Theatre — his sustained theoretical work in the 1930s (the essays collected in Brecht on Theatre) developing a theatrical system opposed to Aristotelian catharsis and designed to produce politically aware spectators — provided the theoretical framework and the theatrical techniques (songs, placards, Verfremdungseffekt) that Mother Courage employs.",
      "The literary source — Hans Hebbel Simplicissimus and particularly the picaresque novels of Hans Jakob Christoffel von Grimmelshausen (Simplicissimus, 1668, set in the Thirty Years' War) — provided the historical setting and the picaresque wandering protagonist that Brecht transformed into the politically allegorical figure of Mother Courage."
    ],
    "effects": [
      "Brecht's Berliner Ensemble production of Mother Courage (1949, Helene Weigel) became the paradigm production of Epic Theatre and established Brecht as the dominant figure of post-war European theatre: the production toured internationally, demonstrating that political theatre could achieve the highest artistic quality and profoundly influencing subsequent directors and playwrights.",
      "Epic Theatre's influence on subsequent 20th-century theatre — the use of anti-illusionist techniques, political engagement, the Verfremdungseffekt, and the rejection of Aristotelian catharsis — spread through the work of Dario Fo, Peter Weiss, Heiner Müller, and the political theatre movements of the 1960s–1970s, making Brecht the most influential theatre theorist and practitioner of the 20th century.",
      "Mother Courage's central figure — a woman who profits from war but loses everything she loves to it, unable to break her dependence — became one of the defining dramatic images of the 20th century's anti-war literature: the play's refusal of heroic or redemptive narrative, its insistence on the systemic character of war's destruction, shaped the theatrical anti-war tradition."
    ],
    "relationships": [
      {"sourceSlug": "bertolt-brecht", "sourceName": "Bertolt Brecht (1898–1956, German playwright)", "verb": "AUTHORS", "targetSlug": "mother-courage-and-her-children", "targetName": "Mother Courage and Her Children (written 1939, performed 1941, Berliner Ensemble 1949)", "context": "Brecht wrote Mother Courage in Sweden in 1939 — set during the Thirty Years' War, it became the defining work of Epic Theatre in Brecht's 1949 Berliner Ensemble production with Helene Weigel."},
      {"sourceSlug": "mother-courage-and-her-children", "sourceName": "Mother Courage (Epic Theatre, Verfremdungseffekt)", "verb": "EXEMPLIFIES", "targetSlug": "epic-theatre", "targetName": "Epic Theatre (Brechtian theatre theory and practice)", "context": "Mother Courage is the defining work of Brecht's Epic Theatre — its anti-illusionist techniques, songs, direct addresses, and Verfremdungseffekt are the practical demonstration of Brecht's theatrical theory."},
      {"sourceSlug": "mother-courage-and-her-children", "sourceName": "Mother Courage (anti-war, Thirty Years' War setting)", "verb": "SET_DURING", "targetSlug": "thirty-years-war", "targetName": "Thirty Years' War (1618–1648)", "context": "Mother Courage is set during the Thirty Years' War — Brecht's choice of the 17th-century European war as an allegory for the 20th-century wars gives the play its historical distance while maintaining its political urgency."}
    ],
    "places": [
      {"name": "Sweden (Brecht in exile, written 1939; first performed Zürich 1941)", "role": "Brecht wrote Mother Courage in Sweden (where he was in exile from Nazi Germany) within five weeks of the outbreak of World War II — the play is simultaneously about the Thirty Years' War and about the contemporary catastrophe"},
      {"name": "East Berlin (Berliner Ensemble 1949 — paradigm Epic Theatre production, Helene Weigel)", "role": "Brecht's Berliner Ensemble production of Mother Courage in East Berlin (1949) with Helene Weigel in the title role became the paradigm production of Epic Theatre and established Brecht as the dominant figure of post-war European theatre"}
    ],
    "subjects": ["German Literature", "Modern Era", "Bertolt Brecht", "Epic Theatre", "Anti-War Literature", "Drama", "20th Century", "Political Theatre"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Mother Courage and Her Children (Brecht, 1939/1949) is the defining work of Epic Theatre and the most influential play of 20th-century European political theatre. Its Berliner Ensemble production (1949) established Brecht as the dominant figure of post-war theatre; his Epic Theatre theory (Verfremdungseffekt, anti-illusionism) shaped Dario Fo, Peter Weiss, Heiner Müller, and the political theatre movements of the 1960s–1970s, making Brecht the most influential theatre theorist of the 20th century.",
      "significanceCategory": "highly-significant"
    }
  }
},

"periplus-of-the-erythraean-sea": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780periplus-of-the-erythraean-sea.json",
  "slug": "periplus-of-the-erythraean-sea",
  "data": {
    "summary": "The Periplus of the Erythraean Sea (Greek: Περίπλους τῆς Ἐρυθρᾶς Θαλάσσης, Periplus Maris Erythraei) is an ancient Greek merchant's guide to the sea routes and trading ports of the Red Sea, the Arabian Peninsula, East Africa, the Persian Gulf, India, and Ceylon (Sri Lanka), written in the 1st century CE (most scholars date it c. 50–70 CE, though dates from 40–150 CE have been proposed) by an anonymous Greek-speaking Egyptian merchant based in Alexandria or the Egyptian Red Sea port of Myos Hormos or Berenice. It is a practical commercial document — a periplus (sailing guide around a sea or coast) — but is the single most important textual source for the commercial and geographic world of the Indian Ocean trade in the Roman period.\n\nThe Periplus of the Erythraean Sea describes, in order from the Egyptian Red Sea ports northward and then southward to Africa (Adulis, Malao, Opone, Rhapta) and eastward through the Arabian Peninsula (Arabia Eudaemon, Muza, Kanê) to India (Barygaza, Muziris, Nelcynda, Poduca, and beyond to the Ganges and the Chryse region), the ports and anchorages, the goods available for trade and the goods required, the political authorities, the navigation conditions, and the prevailing winds. The document's commercial intelligence is precise and detailed — it distinguishes between the goods imported by different ports (wine, olive oil, copper, tin, lead, coral, glass for India; ivory, rhinoceros horn, tortoise shell, incense, silk, pepper, cotton, indigo, and nard in exchange) and provides practical advice on the best season for trading voyages.\n\nThe Periplus is the primary textual evidence for the extraordinary scale and integration of the Roman-period Indian Ocean trade — connecting the Roman Empire to Arabia, East Africa, India, and possibly China through a network of maritime commerce that moved luxury goods, bulk commodities, and precious metals across the ancient world. Archaeological discoveries at Indian sites (Arikamedu, Pattanam) of Roman goods (coins, amphorae, pottery) confirm and extend the Periplus's picture.",
    "causes": [
      "The Roman pacification of Egypt (30 BCE) and the subsequent dramatic expansion of direct Roman trade with India — the harnessing of the monsoon winds (described in the Periplus as the hippalos, named after the sailor who reputedly first used it for direct India voyages) enabled Roman ships to sail directly across the Indian Ocean to India and back, bypassing the Parthian middlemen who had previously controlled the trade.",
      "The extraordinary consumer demand of the Roman Empire for luxury goods — Indian pepper, silk, ivory, gems, cotton, aromatics — drove the expansion of the Indian Ocean trade to the scale documented in the Periplus: pliny the Elder estimated that India, Arabia, and China annually drained 100 million sesterces from Rome in exchange for luxury goods.",
      "The geographical and commercial knowledge accumulated by generations of merchants and sailors — the Periplus is the product of its anonymous author's practical knowledge and the accumulated intelligence of the merchant community at Alexandria and the Egyptian Red Sea ports — represents the practical maritime tradition that made the Indian Ocean trade possible."
    ],
    "effects": [
      "The Periplus of the Erythraean Sea is the primary textual source for the commercial geography of the ancient Indian Ocean world — it is cited in virtually every scholarly study of Roman-period trade with India, East Africa, and Arabia, and has been the foundation for the archaeological identification and interpretation of ancient Indian Ocean port sites.",
      "The Periplus's description of East African ports (Adulis, Malao, Opone, Rhapta) and the goods traded there is the earliest detailed textual account of the East African coast — it documents the beginning of the long-distance commercial connections between the Red Sea / Arabian world and East Africa that would eventually contribute to the development of the Swahili coast culture.",
      "Modern scholarship on the Periplus — particularly since the publication of Lionel Casson's critical edition and commentary (1989) — has established it as the key to understanding the integrated commercial world of the ancient Indian Ocean, contributing to the revisionist understanding of the ancient world as a much more commercially connected global system than traditional classical scholarship had recognised."
    ],
    "relationships": [
      {"sourceSlug": "periplus-of-the-erythraean-sea", "sourceName": "Periplus (Roman-Indian Ocean trade, 1st century CE)", "verb": "DOCUMENTS", "targetSlug": "roman-indian-ocean-trade", "targetName": "Roman-period Indian Ocean trade network (Red Sea to India, 1st–3rd century CE)", "context": "The Periplus is the primary textual source for the Roman-period Indian Ocean trade — documenting the ports, goods, and commercial conditions from Egypt to East Africa, Arabia, and India c. 50–70 CE."},
      {"sourceSlug": "periplus-of-the-erythraean-sea", "sourceName": "Periplus (East Africa — Adulis, Rhapta, Opone)", "verb": "EARLIEST_DETAILED_ACCOUNT_OF", "targetSlug": "east-african-coast-ancient", "targetName": "East African coast in antiquity (Adulis, Rhapta, Opone)", "context": "The Periplus provides the earliest detailed textual account of the East African coast — documenting the ports, goods, and peoples that were the foundation for the long-distance connections that eventually shaped Swahili coast culture."},
      {"sourceSlug": "periplus-of-the-erythraean-sea", "sourceName": "Periplus (Barygaza, Muziris, Indian ports)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "ancient-indo-roman-trade", "targetName": "Indo-Roman trade relations (Arikamedu, Pattanam archaeological sites)", "context": "The Periplus's accounts of Indian ports (Barygaza, Muziris) are confirmed by archaeological discoveries of Roman goods at sites like Arikamedu and Pattanam, making the Periplus the primary textual foundation for the study of Indo-Roman trade."}
    ],
    "places": [
      {"name": "Red Sea, Arabian Sea, Indian Ocean (1st century CE trade network)", "role": "The Periplus describes the entire Indian Ocean trade network from the Egyptian Red Sea ports — documenting the sea routes, ports, and goods across the Red Sea, Arabian Sea, and Indian Ocean"},
      {"name": "Alexandria and Egyptian Red Sea ports (Myos Hormos, Berenice — author's base)", "role": "The anonymous author was probably based in Alexandria or the Egyptian Red Sea ports (Myos Hormos or Berenice) — the primary Roman hubs for Indian Ocean trade"}
    ],
    "subjects": ["Greek Literature", "Ancient Era", "Roman Empire", "Trade History", "Indian Ocean", "Maritime History", "Geography", "Commercial History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Periplus of the Erythraean Sea (c. 50–70 CE) is the primary textual source for the commercial geography of the ancient Indian Ocean world — documenting the ports, goods, and sea routes of the Roman-period Indian Ocean trade network from Egypt to East Africa, Arabia, and India. It is the foundation for the archaeological and historical study of ancient Indo-Roman trade relations and provides the earliest detailed textual account of the East African coast.",
      "significanceCategory": "highly-significant"
    }
  }
},

"suda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780suda.json",
  "slug": "suda",
  "data": {
    "summary": "The Suda (Greek: Σοῦδα, also written Suidas, though the latter name is a misreading of the title — suda may derive from the Byzantine Greek word for 'fortress' or 'stronghold', σοῦδα) is a massive 10th-century Byzantine Greek encyclopaedia, composed c. 970–975 CE under the reign of Emperor John I Tzimiskes (r. 969–976 CE) or possibly under Basil II (r. 976–1025 CE). It contains approximately 30,000 entries arranged alphabetically, covering a vast range of subjects: lexicography (word definitions, grammatical notes, etymologies), biography (entries on hundreds of ancient and Byzantine authors, rulers, and historical figures), literary criticism (quotations from lost works, assessments of authors' styles), historical summaries, mythological notes, and theological discussions. The Suda is the largest and most comprehensive Byzantine encyclopaedia and one of the most important reference works for Greek antiquity.\n\nThe Suda's entries draw on an extraordinary range of earlier sources — many now lost — including lexica (the Hesychius lexicon, the Etymologicum Magnum), historical collections (the excerpts from ancient historians compiled under Constantine VII Porphyrogennetos), biographies (the Onomatologos of Hesychius of Miletus), and a wide range of patristic and classical literature. The Suda's biographical entries — on ancient Greek poets, philosophers, historians, orators, and later Byzantine figures — are often the sole surviving source of information about authors whose works are lost, and its quotations preserve fragments of ancient texts (tragedies, comedies, poetry, prose) that would otherwise be completely unknown.\n\nThe Suda is a crucial tool for classical scholars because of its preservation of otherwise-lost information about ancient Greek literature and history. While its compilation is uneven — some entries are detailed and accurate, others are brief or confused — the Suda's role as a repository of the accumulated learning of the Byzantine scholarly tradition makes it an indispensable reference work. The online Suda On Line (SOL) project has produced an open-access English translation of the complete Suda, making it accessible to non-specialist readers for the first time.",
    "causes": [
      "The Byzantine encyclopaedic tradition of the 10th century — the extraordinary project of Emperor Constantine VII Porphyrogennetos (r. 913–959 CE) to organise and preserve ancient Greek learning through a series of encyclopaedic excerpts — provided both the model and much of the source material for the Suda: the Suda drew heavily on the Constantinian excerpts.",
      "The Byzantine scholarly culture of the 'Macedonian Renaissance' (c. 867–1056 CE) — the period of renewed interest in and preservation of classical Greek learning associated with scholars like Photios, Arethas, and Constantine VII — created the intellectual environment for the Suda's compilation: it is a product of the Byzantine scholarly effort to preserve ancient knowledge.",
      "The practical needs of Byzantine education and scholarship — the need for a comprehensive lexicon and encyclopaedia that could give students and scholars quick access to classical knowledge — motivated the compilation of the Suda as a reference work: it was designed to be used, not merely to preserve."
    ],
    "effects": [
      "The Suda is an indispensable reference work for classical scholarship — its preservation of biographical information about ancient authors (especially minor figures whose works are lost), its quotations from lost tragedies and comedies, and its lexicographical entries make it one of the primary tools for any study of ancient Greek literature and history.",
      "The Suda On Line (SOL) project — a collaborative scholarly project launched in 1998, now at suda.fas.harvard.edu — produced the first complete English translation of the Suda, making it accessible to non-specialist readers and demonstrating the potential of collaborative digital humanities scholarship.",
      "The Suda's preservation of fragments of otherwise-lost ancient texts — including substantial portions of lost Menander comedies, Aeschylus plays, Sappho's poetry, and historical works — has been crucial for the study of these authors: many fragments cited in modern critical editions of ancient authors derive from the Suda."
    ],
    "relationships": [
      {"sourceSlug": "suda", "sourceName": "Suda (c. 970–975 CE, ~30,000 entries, Byzantine encyclopaedia)", "verb": "PRESERVES", "targetSlug": "ancient-greek-literary-fragments", "targetName": "Fragments of lost ancient Greek literature (tragedies, comedies, poetry)", "context": "The Suda preserves quotations from hundreds of ancient Greek works that are otherwise lost — including fragments of Menander, Aeschylus, Sappho, and dozens of other ancient authors — making it an indispensable tool for classical scholarship."},
      {"sourceSlug": "suda", "sourceName": "Suda (Byzantine encyclopaedic tradition, Constantine VII excerpts)", "verb": "PRODUCT_OF", "targetSlug": "macedonian-renaissance-byzantium", "targetName": "Byzantine Macedonian Renaissance (c. 867–1056 CE, scholarly preservation)", "context": "The Suda is a product of the Byzantine 'Macedonian Renaissance' — the 10th-century period of renewed Byzantine interest in and systematic preservation of classical Greek learning associated with Photios, Constantine VII, and the encyclopaedic projects of the Byzantine court."},
      {"sourceSlug": "suda", "sourceName": "Suda On Line (SOL) English translation project", "verb": "DIGITISED_BY", "targetSlug": "suda-on-line", "targetName": "Suda On Line (SOL) collaborative translation project (launched 1998)", "context": "The Suda On Line project (launched 1998) produced the first complete English translation of the Suda through collaborative scholarly effort — a pioneering project in open-access digital humanities."}
    ],
    "places": [
      {"name": "Constantinople (Byzantine imperial court, c. 970–975 CE — Macedonian dynasty)", "role": "The Suda was compiled in Constantinople c. 970–975 CE under the Byzantine imperial court — a product of the Byzantine scholarly culture centred on the capital"},
      {"name": "Byzantine Empire (primary scholarly and educational context, Macedonian Renaissance)", "role": "The Suda is a product of the Byzantine scholarly tradition — the Macedonian Renaissance's systematic effort to preserve and organise classical Greek knowledge for Byzantine educational and scholarly use"}
    ],
    "subjects": ["Byzantine Literature", "Medieval Era", "Greek Language", "Encyclopaedia", "Byzantine Culture", "Classical Scholarship", "Lexicography", "Greek Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Suda (c. 970–975 CE) is the largest and most comprehensive Byzantine Greek encyclopaedia — approximately 30,000 entries covering lexicography, biography, literary criticism, and history. Its preservation of fragments from hundreds of otherwise-lost ancient Greek works makes it an indispensable tool for classical scholarship. The Suda On Line (SOL) project (1998) demonstrated the potential of collaborative digital humanities for making Byzantine scholarship accessible to modern readers.",
      "significanceCategory": "highly-significant"
    }
  }
},

"samaveda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780samaveda.json",
  "slug": "samaveda",
  "data": {
    "summary": "The Sāmaveda (Sanskrit: सामवेद, Sāmaveda, 'Veda of Chants' or 'Veda of Melodies', from sāman 'melody, song' + veda 'knowledge') is the second of the four Vedas — the foundational scriptural texts of Hinduism — and is primarily a liturgical anthology of verses (ṛc) drawn almost entirely from the Ṛgveda, arranged and set to musical notation for use by the udgātṛ priests during the Soma sacrifice (Soma yāga). Of its approximately 1,875 verses, only 75 are unique to the Sāmaveda; the remainder are Ṛgvedic verses reorganised for ritual chanting. The distinctive contribution of the Sāmaveda is not the texts themselves but the musical notation (svaras) and the elaborate system of melodic performance prescribed for them — the Sāmaveda is the foundational text of Indian classical music.\n\nThe Sāmaveda consists of two main sections: the Pūrvārcika ('First Collection', arranged by deity — Agni, Indra, Soma) and the Uttarārcika ('Second Collection', arranged for specific ritual sequences), together with the Gāndhārvaveda (the auxiliary 'Veda of the Gāndhārvas', dealing with music theory) and associated texts. The performance of the Sāmaveda verses in the Soma sacrifice involves an elaborate system of melodic transformation (sāmagāna) in which the basic verse (ṛc) is sung to specific melodies (grama-geyas), with added syllables (stobha), ornamentation, and modulation — a system that is the oldest documented musical tradition in the world.\n\nThe Sāmaveda is considered in the Hindu tradition to be the Veda most closely connected with spiritual realisation through sound — the Bhagavad Gita (10.22) has Krishna declare 'I am the Sāmaveda among the Vedas' — and the tradition of chanting Vedic hymns (particularly Sāmavedic chanting) is one of the oldest continuous musical traditions in the world, preserved orally across three and a half millennia and now recognised as a UNESCO Intangible Cultural Heritage.",
    "causes": [
      "The Soma sacrifice — the central ritual of Vedic religion, in which the intoxicating Soma plant (possibly Ephedra or Amanita muscaria) was pressed, offered, and consumed in a complex multi-day ceremony involving multiple classes of priests — required the specialised musical performance of selected Ṛgvedic verses by the udgātṛ priests, creating the liturgical need for a separate Vedic collection arranged for musical performance.",
      "The Vedic oral tradition and its extraordinary precision — the preservation of Vedic texts through highly formalised oral recitation techniques (pāṭha, the various recitation modes; svara, musical accent) — was the primary mechanism for the Sāmaveda's preservation: the Sāmavedic chanting tradition was transmitted from teacher to student in an unbroken line for over three millennia.",
      "The broader Vedic cultural and religious world of ancient India (c. 1500–500 BCE) — the developed ritual and philosophical culture of the Indo-Aryan peoples of the Gangetic plain, as preserved in the four Vedas and the associated Brāhmaṇas (ritual commentaries), Āraṇyakas (forest texts), and Upaniṣads (philosophical texts) — provided the religious context within which the Sāmaveda's function was defined."
    ],
    "effects": [
      "The Sāmaveda is the foundational text of Indian classical music — the system of svaras (musical notes) and sāmagāna (melodic elaboration) codified in Sāmavedic practice is the historical origin of the rāga system of Indian classical music (Carnatic and Hindustani), making the Sāmaveda the direct ancestor of one of the world's great musical traditions.",
      "The Sāmavedic chanting tradition — preserved in the Jaiminīya and Kauthuma-Rāṇāyanīya sākhās of the Sāmaveda — is one of the oldest continuously practised musical traditions in the world, transmitted orally for over 3,500 years and now recognised as a UNESCO Intangible Cultural Heritage (as part of the broader tradition of Vedic chanting).",
      "The Sāmaveda's influence on Hindu theology and spirituality — the Hindu tradition's elevation of sound (nāda) and chanting as a path to spiritual realisation, the concept of Nāda Brahman ('sound as the ultimate reality'), and the centrality of devotional chanting (bhajan, kīrtan) in Hindu practice — traces to the Sāmavedic valorisation of musical sound as a vehicle of the sacred."
    ],
    "relationships": [
      {"sourceSlug": "samaveda", "sourceName": "Sāmaveda (Veda of Chants, Soma sacrifice)", "verb": "PART_OF", "targetSlug": "four-vedas", "targetName": "The Four Vedas (Ṛgveda, Sāmaveda, Yajurveda, Atharvaveda)", "context": "The Sāmaveda is the second of the four Vedas — an anthology of Ṛgvedic verses arranged for musical chanting during the Soma sacrifice by the udgātṛ priests."},
      {"sourceSlug": "samaveda", "sourceName": "Sāmaveda (svaras, sāmagāna, Indian music foundation)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "indian-classical-music", "targetName": "Indian classical music (Carnatic and Hindustani traditions)", "context": "The Sāmaveda is the foundational text of Indian classical music — its system of svaras (musical notes) and melodic elaboration (sāmagāna) is the historical origin of the rāga system that underlies both Carnatic and Hindustani classical music."},
      {"sourceSlug": "samaveda", "sourceName": "Sāmaveda (oldest continuous musical tradition, UNESCO recognition)", "verb": "RECOGNISED_AS", "targetSlug": "vedic-chanting-unesco", "targetName": "UNESCO Intangible Cultural Heritage (Vedic chanting tradition)", "context": "The Sāmavedic chanting tradition — transmitted orally for over 3,500 years — is part of the broader tradition of Vedic chanting recognised as a UNESCO Intangible Cultural Heritage, one of the oldest continuously practised musical traditions in the world."}
    ],
    "places": [
      {"name": "Ancient India (Vedic civilisation, Gangetic plain, c. 1500–500 BCE)", "role": "The Sāmaveda was composed in the context of the Vedic civilisation of ancient India — the Indo-Aryan cultural world of the Gangetic plain that produced the four Vedas and the associated Brāhmaṇas"},
      {"name": "South India (Carnatic classical music tradition; Jaiminīya sākhā survival)", "role": "The Jaiminīya sākhā of the Sāmaveda — one of the two main surviving recensions — is primarily practised in South India, connecting the Sāmavedic tradition to the Carnatic classical music tradition"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Hindu Scripture", "Vedic Literature", "Indian Music", "Hinduism", "Oral Tradition", "Religious Texts"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Sāmaveda (c. 1500–500 BCE) is the foundational text of Indian classical music — its system of musical notation and melodic performance is the historical origin of the rāga system that underlies both Carnatic and Hindustani classical music. As the Veda of Chants, it valorises sound as a vehicle of the sacred, shaping the musical and devotional dimensions of Hindu practice across three and a half millennia. Its oral transmission tradition is one of the oldest continuously practised musical traditions in the world.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-black-book-of-communism": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-black-book-of-communism.json",
  "slug": "the-black-book-of-communism",
  "data": {
    "summary": "The Black Book of Communism: Crimes, Terror, Repression (French: Le Livre noir du communisme: Crimes, terreur, répression) is a controversial scholarly anthology edited by the French historian Stéphane Courtois and co-authored by six other historians (Nicolas Werth, Jean-Louis Panné, Andrzej Paczkowski, Karel Bartošek, Jean-Louis Margolin, and Rémi Kauffer), published by Harvard University Press in French in 1997 and translated into many languages (English 1999). The book is an attempt to document, in systematic comparative form, the crimes and deaths attributable to communist regimes worldwide — the Soviet Union, China, Cambodia, Korea, Vietnam, Eastern Europe, Cuba, Ethiopia, and elsewhere — and arrives at a controversial aggregate estimate of approximately 94–100 million deaths attributable to communist regimes in the 20th century.\n\nThe Black Book of Communism generated an immediate and sustained controversy, both about its methods and about its political implications. The aggregate death toll estimate (94–100 million) has been contested by other historians (Robert Conquest, whose research on Soviet terror Courtois drew on, and others have given lower estimates for some regimes); the book's co-authors publicly disagreed with Courtois's framing and his political agenda (several co-authors wrote prefaces distancing themselves from Courtois's comparison of communism to Nazism in body count terms); and critics argued that the aggregation of death tolls across diverse regimes over eight decades distorts more than it illuminates.\n\nDespite the controversy, The Black Book of Communism became one of the most widely read works on communist history and an important document in the post-Cold War reassessment of the communist legacy — particularly in Eastern Europe and France, where it provoked intense public debate about the relationship between the French Communist Party and Stalinist repression.",
    "causes": [
      "The fall of the Soviet Union (1991) and the opening of Soviet and Eastern European archives — giving Western and Eastern European historians access to documentary evidence of the scale of Soviet repression (Gulag population statistics, secret police records, famine mortality data) — made possible the systematic documentation of communist crimes that the Black Book attempted.",
      "The post-Cold War political climate in France and Western Europe — the discrediting of Communist parties and the intellectual left's confrontation with its complicity in defending or minimising Soviet crimes — created the political context for the Black Book's provocative argument: the book was a direct challenge to the residual prestige of communism in French intellectual life.",
      "The comparative genocide studies framework — the academic tradition of comparing the Nazi Holocaust with other mass atrocities (the Gulag, the Ukrainian famine, the Cambodian genocide) — provided the intellectual framework for Courtois's comparative approach: the book was controversial partly because it appeared to flatten the distinction between the Holocaust and communist mass deaths."
    ],
    "effects": [
      "The Black Book of Communism provoked one of the most intense intellectual debates in France in the 1990s — about the historical responsibility of communism, the relationship between communist ideology and mass atrocities, and the appropriate methodology for comparing mass killings across different historical contexts — stimulating a wave of further research and public debate.",
      "The Black Book's aggregate death toll estimate (94–100 million) entered political discourse as a reference point — cited by politicians, journalists, and commentators in discussions of communist regimes' historical record — and influenced public memory of communism in Eastern Europe, where it was embraced as validation of the anti-communist narrative.",
      "The controversy within the Black Book's own authorial team — the public disagreements between Courtois and his co-authors — demonstrated the methodological and political tensions within the emerging field of comparative communist studies and set the terms for subsequent debates about how to assess the historical record of communist regimes."
    ],
    "relationships": [
      {"sourceSlug": "stephane-courtois", "sourceName": "Stéphane Courtois (editor, French historian)", "verb": "EDITS", "targetSlug": "the-black-book-of-communism", "targetName": "The Black Book of Communism (Le Livre noir du communisme, 1997)", "context": "Courtois edited and framed the Black Book of Communism — his controversial introduction comparing communism to Nazism in body count terms prompted public disagreements from his co-authors (Nicolas Werth, Jean-Louis Margolin, and others)."},
      {"sourceSlug": "the-black-book-of-communism", "sourceName": "Black Book (94–100 million deaths estimate, communist regimes)", "verb": "DOCUMENTS", "targetSlug": "communist-regime-mass-atrocities", "targetName": "Mass atrocities of 20th-century communist regimes (Soviet Union, China, Cambodia, etc.)", "context": "The Black Book attempts to document the deaths attributable to communist regimes worldwide — arriving at a controversial aggregate estimate of 94–100 million, drawing on new archival evidence from the post-Soviet opening."},
      {"sourceSlug": "the-black-book-of-communism", "sourceName": "Black Book (France 1997, French Communist Party, post-Cold War debate)", "verb": "PROVOKES", "targetSlug": "french-intellectual-debate-1990s-communism", "targetName": "French intellectual debate on communism and political responsibility (1990s–2000s)", "context": "The Black Book provoked one of the most intense intellectual debates in France in the 1990s — directly challenging the residual prestige of the French Communist Party and the intellectual left's complicity in minimising Soviet crimes."}
    ],
    "places": [
      {"name": "France (published Paris 1997; French intellectual debate, French Communist Party)", "role": "The Black Book was published in France in 1997 — its primary target was the French intellectual tradition that had defended or minimised Soviet crimes, and it provoked intense public debate in France about the legacy of communism"},
      {"name": "Soviet Union, China, Cambodia (primary subjects — Soviet archives opening, post-Cold War research)", "role": "The Black Book's chapters on the Soviet Union (Nicolas Werth), China (Jean-Louis Margolin), and Cambodia draw on the post-Soviet opening of archives and are the most substantial historical contributions in the volume"}
    ],
    "subjects": ["History", "Modern Era", "Communism", "Soviet History", "Political History", "Historiography", "Cold War", "20th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Black Book of Communism (Courtois et al., 1997) is the most widely read attempt to document communist regime crimes in systematic comparative form, and one of the most controversial works in post-Cold War historiography. Its aggregate death toll estimate entered public and political discourse; its internal controversy demonstrated the methodological challenges of comparative communist history. As a document of the post-Cold War reassessment of the communist legacy in Europe and France, it remains an important and contentious reference point.",
      "significanceCategory": "significant"
    }
  }
},

"o-fortuna": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780o-fortuna.json",
  "slug": "o-fortuna",
  "data": {
    "summary": "O Fortuna is a medieval Latin poem from the Carmina Burana (a 13th-century manuscript of lyric poems and dramatic texts found at the Benediktbeuern monastery in Bavaria), set to music by the German composer Carl Orff (1895–1982) as the opening and closing movement of his scenic cantata Carmina Burana (1936, first performed Frankfurt 1937). The Latin text — attributed to the Goliard poets of the 12th–13th centuries and dating to the first half of the 13th century CE — is a lament addressed to the goddess Fortuna (Fortune), complaining of the instability of the Wheel of Fortune ('O Fortuna, velut luna statu variabilis' — 'O Fortune, like the moon, ever mutable'), the loss of prosperity, and the suffering of those at Fortune's mercy. It is the opening poem of the Carmina Burana manuscript.\n\nOrff's setting of O Fortuna — a massive choral and orchestral movement in dramatic triple metre, distinguished by its relentless rhythmic drive, its alternation between fortissimo and pianissimo, and its simple but overwhelming melodic line — has become one of the most recognisable musical compositions in the Western canon and arguably the most widely heard piece of classical music in the 20th and 21st centuries through its use in film, television, and advertising. The piece is characterised by enormous forces (large chorus, soloists, full orchestra with massive percussion) and a dramatic simplicity that makes it immediately accessible while retaining genuine musical power.\n\nOrff's Carmina Burana was composed during the Third Reich (premiere 1937), and Orff's relationship to National Socialism has been debated — the work's premiere was received favourably by Nazi cultural authorities, though its pagan, erotic themes are not straightforwardly Nazi-ideological. The combination of theatrical primitivism, massive choral sound, and pagan subject matter has made it a powerful and occasionally controversial work. O Fortuna's ubiquity in popular culture — used in hundreds of films, advertisements, and sporting events — has made it simultaneously one of the most-heard classical pieces and one of the most familiar clichés of dramatic musical punctuation.",
    "causes": [
      "The discovery of the Carmina Burana manuscript (1803, Benediktbeuern Abbey, Bavaria) — and its subsequent scholarly publication by Johann Andreas Schmeller (1847) — made the medieval Latin text available to 20th-century composers: Orff encountered the texts through Schmeller's edition.",
      "Carl Orff's compositional aesthetic of Schulwerk and elemental music — his rejection of the complex chromatic harmony and counterpoint of the late Romantic tradition in favour of elementary rhythmic drive, modal harmonies, and massive choral forces — found its perfect expression in the medieval Latin texts of the Carmina Burana, whose directness and sensuality matched his aesthetic aims.",
      "The German cultural context of the 1930s — the Weimar Republic's theatrical experimentalism and the subsequent Nazi valorisation of monumental public art — provided the cultural and institutional environment for Carmina Burana's premiere: the work's massive forces and theatrical power fit the taste of the era for spectacular public musical events."
    ],
    "effects": [
      "O Fortuna became one of the most ubiquitous pieces of classical music in popular culture — used in hundreds of films (Excalibur, 1981; The Hunt for Red October, Natural Born Killers), television programmes, advertisements, and sporting events — demonstrating the paradoxical capacity of a medieval Latin text set in 1936 to function as a universal emblem of dramatic grandeur and overwhelming fate.",
      "Orff's Carmina Burana established a new model for large-scale choral-orchestral writing — its combination of rhythmic directness, modal simplicity, massive orchestration, and theatrical drama influenced subsequent choral composers and became a model for accessible large-scale choral composition.",
      "The Carmina Burana manuscript's medieval Latin poems — made familiar to millions through Orff's setting — stimulated renewed scholarly and popular interest in medieval lyric poetry, the Goliard tradition, and the culture of the medieval university student: O Fortuna and the other Carmina Burana texts became some of the most widely known medieval poems outside the scholarly world."
    ],
    "relationships": [
      {"sourceSlug": "o-fortuna", "sourceName": "O Fortuna (Latin text, 13th century, Carmina Burana manuscript)", "verb": "PART_OF", "targetSlug": "carmina-burana-manuscript", "targetName": "Carmina Burana manuscript (Codex Buranus, c. 1230 CE, Benediktbeuern)", "context": "O Fortuna is the opening poem of the Carmina Burana manuscript (c. 1230 CE) — a 13th-century collection of Goliard poetry found at Benediktbeuern Abbey, Bavaria, in 1803."},
      {"sourceSlug": "o-fortuna", "sourceName": "O Fortuna (Orff's setting 1936/1937 — cantata premiere)", "verb": "SET_TO_MUSIC_BY", "targetSlug": "carl-orff", "targetName": "Carl Orff (1895–1982, Carmina Burana scenic cantata, 1936)", "context": "Carl Orff set O Fortuna as the opening and closing movement of his scenic cantata Carmina Burana (1936, premiere Frankfurt 1937) — the setting became one of the most recognisable pieces in the Western classical canon."},
      {"sourceSlug": "o-fortuna", "sourceName": "O Fortuna (Wheel of Fortune — medieval cultural motif)", "verb": "EXPRESSES", "targetSlug": "wheel-of-fortune-concept", "targetName": "Wheel of Fortune (Rota Fortunae, medieval cultural concept)", "context": "O Fortuna's central theme — the instability of Fortune's wheel, raising and lowering those at its mercy — expresses the same Wheel of Fortune motif that Boethius established in the Consolation of Philosophy and that was one of the defining images of medieval culture."}
    ],
    "places": [
      {"name": "Benediktbeuern, Bavaria (manuscript found 1803; Codex Buranus origin)", "role": "The Carmina Burana manuscript was found at the Benediktbeuern Abbey in Bavaria in 1803 — the medieval Latin texts were composed c. 1230 CE, probably in the region of the Bavarian-Austrian Alps"},
      {"name": "Frankfurt, Germany (Orff's premiere 1937; 20th-century musical setting context)", "role": "Orff's Carmina Burana had its premiere in Frankfurt in 1937 — composed during the Third Reich, its reception and relationship to Nazi cultural politics has been debated"}
    ],
    "subjects": ["Medieval Latin Literature", "Medieval Era", "Carl Orff", "Choral Music", "Fortune", "Popular Culture", "Music History", "Carmina Burana"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "O Fortuna (13th-century Latin poem, set by Carl Orff in 1936) is one of the most recognisable pieces of classical music in popular culture — used in hundreds of films, advertisements, and sporting events, making it arguably the most widely heard piece of classical music in the 20th and 21st centuries. The medieval poem's theme of Fortune's instability connects it to the Boethian tradition; Orff's setting demonstrates the capacity of medieval texts to achieve popular cultural resonance through the right musical reframing.",
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
