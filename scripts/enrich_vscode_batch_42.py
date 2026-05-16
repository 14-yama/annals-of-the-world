#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 42 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: fantastic-beasts-and-where-to-find-them,
          das-kapital-1867, anglosaxon-chronicle-viking-entries,
          gilgamesh-and-aga, a-series-of-unfortunate-events,
          artemis-fowl, carroccio, plan-do-check-adjust
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-42-may2026"

ENRICHMENTS = {

"fantastic-beasts-and-where-to-find-them": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780fantastic-beasts-and-where-to-find-them.json",
  "slug": "fantastic-beasts-and-where-to-find-them",
  "data": {
    "summary": "Fantastic Beasts and Where to Find Them is a fictional companion book to the Harry Potter series, written by J. K. Rowling under the pen name Newt Scamander — first published in 2001 by Bloomsbury and Scholastic, presented as a reproduction of the textbook used by Hogwarts students in the Care of Magical Creatures class, with handwritten annotations by Harry Potter, Ron Weasley, and Hermione Granger. The book catalogues 75 magical creatures of the Harry Potter wizarding world (Acromantula, Basilisk, Bowtruckle, Centaur, Graphorn, Hippogriff, Niffler, Nundu, Phoenix, Thunderbird, and many others), describing each creature's classification, physical characteristics, habitat, and behaviour in the format of a naturalist's handbook, mimicking the style of a real-world zoological reference. The original 2001 edition was published as a Comic Relief fundraising book alongside Quidditch Through the Ages; a revised and expanded edition appeared in 2017.\n\nThe fictional author, Newton Artemis Fido 'Newt' Scamander, is a Magizoologist (a scholar of magical animals) who became the protagonist of a film franchise: the Fantastic Beasts film series produced by Warner Bros. (Fantastic Beasts and Where to Find Them, 2016; The Crimes of Grindelwald, 2018; The Secrets of Dumbledore, 2022), starring Eddie Redmayne as Newt Scamander, and written by Rowling herself. The film series is set in the 1920s–1940s and explores the wizarding world of that period — pre-dating the Harry Potter novels by several decades — with New York, Paris, and Brazil as settings, and the conflict between Newt Scamander and the dark wizard Gellert Grindelwald (the predecessor to Voldemort) as its primary narrative.\n\nThe 2001 companion book's publication as a Comic Relief fundraising title — with handwritten annotations from the 'original owners' (Harry, Ron, and Hermione) — was a significant moment in J. K. Rowling's engagement with the practice of world-building through paratextual materials: the book simultaneously exists in the Harry Potter world as a Hogwarts textbook and in the real world as a charity publication, creating a playful blurring of the boundary between fiction and reality that became characteristic of Rowling's approach to extending the Potter universe.",
    "causes": [
      "Comic Relief's approach to J. K. Rowling to write a fundraising book — the initial commission from the charity (for its Red Nose Day campaign) provided the institutional context for the companion book's creation: the combination of an established fictional world (Harry Potter), a charitable purpose, and the format of a fictional in-world textbook was the genesis of Fantastic Beasts.",
      "J. K. Rowling's world-building impulse — her creation of an extraordinarily detailed fictional universe for the Harry Potter series, including numerous named magical creatures that appear throughout the novels — provided the narrative raw material from which the companion book's 75 beast entries were compiled and expanded.",
      "The commercial and creative success of the Harry Potter series (1997–2007) — which had established itself as the most successful children's book series in history by 2001 — created the audience and the brand recognition that made a companion book a commercially viable proposition and a culturally significant publishing event."
    ],
    "effects": [
      "The Fantastic Beasts companion book's success as a Comic Relief fundraiser — raising over £17 million for charity — demonstrated the commercial power of the Harry Potter brand extended to paratextual companion volumes, establishing a pattern of world-building through reference books that influenced subsequent fantasy franchise publishing.",
      "The Fantastic Beasts film franchise (2016–2022) — a prequel film series starring Eddie Redmayne as Newt Scamander — extended the Harry Potter universe into a major cinematic franchise, demonstrating the capacity of a fictional textbook's named author to become the protagonist of a major film series and generating significant commercial revenue.",
      "The Fantastic Beasts companion book's approach to world-building through fictional paratexts — reference books, encyclopaedias, and in-world documents that simultaneously exist within the fiction and outside it — influenced the approach to franchise world-building in the 2000s and 2010s, contributing to the broader culture of expanded universe content that has become characteristic of major fantasy and science fiction franchises."
    ],
    "relationships": [
      {"sourceSlug": "j-k-rowling", "sourceName": "J. K. Rowling (born 1965)", "verb": "AUTHORS", "targetSlug": "fantastic-beasts-and-where-to-find-them", "targetName": "Fantastic Beasts and Where to Find Them (2001)", "context": "Rowling wrote the companion book under the pen name Newt Scamander for Comic Relief (2001) — a fictional Hogwarts textbook cataloguing 75 magical creatures from the Harry Potter universe, raising £17 million for charity."},
      {"sourceSlug": "fantastic-beasts-and-where-to-find-them", "sourceName": "Fantastic Beasts (companion book, world-building)", "verb": "PART_OF", "targetSlug": "harry-potter-series", "targetName": "Harry Potter series (J. K. Rowling, 1997–2007)", "context": "Fantastic Beasts is a paratextual companion to the Harry Potter series — a fictional in-world Hogwarts textbook that simultaneously exists in the fictional universe and in the real world as a charity publication."},
      {"sourceSlug": "fantastic-beasts-and-where-to-find-them", "sourceName": "Fantastic Beasts (Newt Scamander, film franchise)", "verb": "ADAPTED_AS", "targetSlug": "fantastic-beasts-film-series", "targetName": "Fantastic Beasts film series (Warner Bros., 2016–2022)", "context": "The fictional author Newt Scamander became the protagonist of the Fantastic Beasts film franchise (2016–2022) — a prequel series set in the 1920s–1940s wizarding world, written by Rowling and starring Eddie Redmayne."}
    ],
    "places": [
      {"name": "United Kingdom (Bloomsbury, 2001 publication; Hogwarts fictional setting)", "role": "Fantastic Beasts was published in the UK by Bloomsbury in 2001 as a Comic Relief fundraiser — the fictional setting is the Hogwarts universe of the Harry Potter series"},
      {"name": "New York, Paris, Brazil (Fantastic Beasts film franchise settings, 1920s–1940s)", "role": "The Fantastic Beasts film franchise (2016–2022) is set primarily in New York, Paris, and Brazil in the 1920s–1940s — extending the Harry Potter wizarding world into a new era and geography"}
    ],
    "subjects": ["English Literature", "Modern Era", "J.K. Rowling", "Fantasy Literature", "World-Building", "Children's Literature", "Companion Volume", "Film Adaptation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Fantastic Beasts and Where to Find Them (Rowling, 2001) is a significant companion volume to the Harry Potter series — its fundraising model (£17 million for Comic Relief) and its world-building approach (fictional paratextual reference book) influenced subsequent fantasy franchise publishing. Its transformation into a major film franchise (2016–2022) demonstrates the commercial power of fictional in-world documents as franchise extensions.",
      "significanceCategory": "significant"
    }
  }
},

"das-kapital-1867": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781das-kapital-1867.json",
  "slug": "das-kapital-1867",
  "data": {
    "summary": "Das Kapital. Kritik der politischen Ökonomie, Band I ('Capital. A Critique of Political Economy, Volume I') is the first volume of Karl Marx's major theoretical work on capitalism, published in Hamburg on 14 September 1867 by Verlag von Otto Meissner — the culmination of over twenty years of economic research and the foundational theoretical text of Marxist political economy. The 1867 first edition is the primary text that established the theoretical framework of Capital: the analysis of the commodity form as the 'cell-form' of capitalist society, the theory of value (the Labour Theory of Value — that value is determined by the socially necessary labour time required to produce a commodity), the concept of surplus value (Mehrwert) — the difference between the value workers create and the wages they receive — as the source of capitalist profit, and the accumulation of capital as the driving mechanism of capitalist development.\n\nDas Kapital Band I is structured in seven parts (in later editions): commodities and money; the transformation of money into capital; the production of absolute surplus value; the production of relative surplus value; the production of absolute and relative surplus value; wages; the accumulation of capital. Marx's analysis moves from the simplest economic form (the commodity) through increasingly complex determinations to the historical dynamics of capitalist accumulation, the primitive accumulation of capital (the historical process of dispossession through which pre-capitalist forms were destroyed to create a free labour force), and the tendencies of capitalist development including the concentration of capital and the immiseration of the working class.\n\nDas Kapital 1867 was not an immediate popular success — the first edition sold slowly, and Engels reviewed it under different pseudonyms in the German press to generate attention — but its influence grew enormously after the formation of the First International (1864), the Paris Commune (1871), and the growth of the German Social Democratic Party. Engels edited and prepared Volume II (1885) and Volume III (1894) from Marx's manuscripts after Marx's death (1883). The 1867 first edition is catalogued separately as the primary source document of Capital's theoretical framework and its specific historical context of the 1860s German labour movement.",
    "causes": [
      "Marx's lifelong engagement with the political economy of capitalism — beginning with his critique of Hegel's Philosophy of Right (1843), the Economic and Philosophical Manuscripts (1844), The German Ideology (1845–46), the Grundrisse (1857–58), and the Contribution to the Critique of Political Economy (1859) — provided the accumulated theoretical foundation from which Das Kapital's systematic analysis was constructed over more than two decades.",
      "The specific social and economic context of mid-19th century capitalism — the industrial revolution in Britain (Marx's primary empirical source, drawing on Factory Inspectors' Reports, parliamentary inquiries, and statistical evidence), the growth of the German working class, and the formation of the First International (1864) — provided both the empirical material and the political motivation for Marx's theoretical analysis.",
      "Marx's engagement with the classical political economists (Adam Smith, David Ricardo) and his critique of their theoretical limitations — particularly Ricardo's inability to explain surplus value within the framework of the Labour Theory of Value — drove the theoretical innovation of Das Kapital: Marx's surplus value theory was his solution to the theoretical problem that Ricardo could not resolve."
    ],
    "effects": [
      "Das Kapital's theoretical framework — the Labour Theory of Value, surplus value, capital accumulation, and the tendency of capitalist crises — became the theoretical foundation of Marxist political economy, socialist parties, and communist movements worldwide, shaping the economic programmes of the First and Second Internationals, the Russian Revolution (1917), and the socialist states of the 20th century.",
      "Engels's editions of Volumes II and III (1885, 1894) — compiled from Marx's unfinished manuscripts — completed the Capital project, but the 1867 first edition of Volume I remained the primary theoretical text that shaped the understanding of Marxist political economy.",
      "Das Kapital's methodological innovation — its use of the dialectical method applied to economic analysis, its movement from abstract (commodity) to concrete (capitalist accumulation), and its integration of historical evidence with theoretical analysis — influenced the methodology of economic and social theory beyond the Marxist tradition."
    ],
    "relationships": [
      {"sourceSlug": "karl-marx", "sourceName": "Karl Marx (1818–1883)", "verb": "AUTHORS", "targetSlug": "das-kapital-1867", "targetName": "Das Kapital Band I (first edition, Hamburg, 14 September 1867)", "context": "Marx published Das Kapital Band I on 14 September 1867 — the culmination of over twenty years of economic research and the foundational theoretical text of Marxist political economy, establishing the Labour Theory of Value and surplus value theory."},
      {"sourceSlug": "das-kapital-1867", "sourceName": "Das Kapital (Labour Theory of Value, surplus value)", "verb": "ESTABLISHES", "targetSlug": "marxist-political-economy", "targetName": "Marxist political economy (surplus value, capital accumulation)", "context": "Das Kapital's theoretical framework — surplus value as the source of capitalist profit, capital accumulation as the driving mechanism — became the foundation of Marxist political economy and socialist party programmes worldwide."},
      {"sourceSlug": "das-kapital-1867", "sourceName": "Das Kapital (critique of classical political economy)", "verb": "RESPONDS_TO", "targetSlug": "david-ricardo", "targetName": "David Ricardo (1772–1823, classical political economy)", "context": "Marx's surplus value theory was developed as the solution to Ricardo's inability to explain profit within the Labour Theory of Value — Das Kapital is both a synthesis and a critique of the classical political economy tradition."}
    ],
    "places": [
      {"name": "Hamburg (Otto Meissner, first publication, 14 September 1867)", "role": "Das Kapital Band I was first published in Hamburg by Otto Meissner on 14 September 1867 — the primary publication event of the most influential work of political economy in the 19th and 20th centuries"},
      {"name": "London (Marx's research base, British Museum library, Factory Reports)", "role": "Marx conducted the empirical research for Das Kapital primarily in London — reading at the British Museum library and drawing on British Factory Inspectors' Reports and parliamentary inquiries as his primary empirical sources"}
    ],
    "subjects": ["Political Economy", "Modern Era", "Karl Marx", "Marxism", "Capitalism", "Labour Theory of Value", "19th Century", "German"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Das Kapital Band I (Marx, Hamburg, 14 September 1867) is the foundational text of Marxist political economy — the Labour Theory of Value, surplus value, and capital accumulation theory that shaped socialist and communist movements, the Russian Revolution (1917), and the socialist states governing over a third of the world's population in the 20th century. One of the most consequential works of social science in history, its theoretical framework continues to influence political economy, economic history, and social theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"anglosaxon-chronicle-viking-entries": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781anglosaxon-chronicle-viking-entries.json",
  "slug": "anglosaxon-chronicle-viking-entries",
  "data": {
    "summary": "The Viking entries of the Anglo-Saxon Chronicle are the annals — year-by-year entries — in the various manuscript versions of the Anglo-Saxon Chronicle that record the Viking raids, invasions, settlements, and political interactions with Scandinavian peoples in England from the first recorded raid (793 CE, the attack on Lindisfarne) through the Danish conquest of England (1013–1016, Sweyn Forkbeard and Cnut) and the period of the Danelaw (the Scandinavian-controlled territories of northern and eastern England in the 9th–10th centuries). These entries constitute the primary contemporary narrative source for the Viking Age in England — the principal English-language documentary record through which historians reconstruct the Viking impact on England over two and a half centuries.\n\nThe Anglo-Saxon Chronicle's Viking entries span all manuscript versions (the A-manuscript or Winchester Chronicle, B, C, D, E, F manuscripts, preserved at various locations), with the most detailed coverage of the Viking Age in manuscripts compiled in the 9th–10th centuries — particularly the entries covering the Great Heathen Army's invasion of England in 865–879 (the Danes who overran Northumbria, East Anglia, and Mercia), Alfred the Great's resistance and his treaty with Guthrum establishing the Danelaw boundary (880 CE), and the subsequent campaigns of Alfred's children and grandchildren (Edward the Elder, Æthelflæd, Æthelstan) to reconquer the Danelaw in the early 10th century. The entries covering the reign of Æthelred the Unready (978–1016) describe the second wave of Viking raids — the campaigns of Olaf Tryggvason, Sweyn Forkbeard, and eventually Cnut — in dramatic detail, recording the payment of Danegeld (tribute) and the political collapse of Anglo-Saxon England before the Danish conquest.\n\nThe Viking entries of the Anglo-Saxon Chronicle are notable for their perspective — the chronicle was compiled and maintained at English monasteries (Winchester, Abingdon, Worcester, Canterbury), and the Viking entries reflect the English ecclesiastical perspective on the Scandinavian attacks: the destruction of churches and monasteries is prominent, and the Danes are frequently described as 'pagans' (hæðen) in contrast to the Christian English. This perspective shapes the historical evidence in important ways — it emphasises religious damage and downplays Scandinavian settlement and cultural contribution — and modern historians must read the entries critically against other evidence.",
    "causes": [
      "The Viking Age's impact on Anglo-Saxon England — the raids, invasions, and settlements of Scandinavian peoples that fundamentally altered the political, cultural, and linguistic landscape of England from the 790s through the 1040s — provided the events that the Anglo-Saxon Chronicle's Viking entries document: without the Viking Age, there would be no Viking entries.",
      "The English monastic tradition of historical record-keeping — the practice of maintaining annalistic records of significant events at major monasteries — created the documentary form that the Anglo-Saxon Chronicle adopted and maintained: the year-by-year annal format that records events as they occurred is the characteristic form of the Viking entries.",
      "Alfred the Great's programme of cultural and educational renewal — his commissioning of the original Anglo-Saxon Chronicle c. 892 and his promotion of English literacy — created the primary compilation of the Chronicle's Viking entries for the crucial period of the Great Heathen Army and the Danelaw establishment, making Alfred's court the origin point of the most important source for the 9th-century Viking Age in England."
    ],
    "effects": [
      "The Anglo-Saxon Chronicle's Viking entries became the foundational primary source for the history of Viking-Age England — all subsequent scholarship on the Viking impact on England, the Danelaw, Alfred's resistance, and the Danish conquest must engage with these entries, making them the central documentary evidence for two and a half centuries of Anglo-Scandinavian history.",
      "The Viking entries' framing of the Danes as 'pagans' who attack Christian England — reflecting the ecclesiastical perspective of the chronicle's compilers — shaped the medieval and early modern image of the Vikings as destructive and anti-Christian, contributing to the negative stereotype that modern scholarship has had to work to revise.",
      "The specific events recorded in the Viking entries — the sack of Lindisfarne (793), the Great Heathen Army (865), the establishment of the Danelaw, Alfred's treaty with Guthrum, the payment of Danegeld, and Cnut's conquest — are the primary historical data points around which the Viking Age in England is structured, demonstrating the chronicle's constitutive role in the historical knowledge of this period."
    ],
    "relationships": [
      {"sourceSlug": "anglosaxon-chronicle-viking-entries", "sourceName": "Anglo-Saxon Chronicle Viking entries (793–1042)", "verb": "PART_OF", "targetSlug": "anglo-saxon-chronicle", "targetName": "Anglo-Saxon Chronicle (c. 892, multiple manuscripts)", "context": "The Viking entries are a specific body of content within the Anglo-Saxon Chronicle — the year-by-year annals recording Viking raids, invasions, and the Danelaw from 793 to the Danish conquest, compiled in the 9th–11th centuries."},
      {"sourceSlug": "anglosaxon-chronicle-viking-entries", "sourceName": "Anglo-Saxon Chronicle Viking entries (Alfred, Great Heathen Army)", "verb": "DOCUMENTS", "targetSlug": "alfred-the-great", "targetName": "Alfred the Great (r. 871–899, Danelaw establishment)", "context": "The Chronicle entries covering Alfred's resistance to the Great Heathen Army, his treaty with Guthrum, and the establishment of the Danelaw are the primary narrative sources for the most significant period of Alfred's reign."},
      {"sourceSlug": "anglosaxon-chronicle-viking-entries", "sourceName": "Viking entries (primary source, Viking Age England)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "viking-age-england", "targetName": "Viking Age in England (793–1042)", "context": "The Anglo-Saxon Chronicle's Viking entries are the primary contemporary narrative source for the Viking Age in England — the foundational documentary record through which historians reconstruct Viking raids, the Danelaw, and the Danish conquest."}
    ],
    "places": [
      {"name": "Lindisfarne (793 raid, first Chronicle entry), Northumbria, England", "role": "The 793 attack on Lindisfarne — the first major Viking raid recorded in the Chronicle — is the defining opening event of the Viking Age in England, described in the Chronicle as pagans (hæðen) attacking the holy island"},
      {"name": "Winchester, Abingdon, Worcester, Canterbury (manuscript compilation locations)", "role": "The multiple manuscript versions of the Anglo-Saxon Chronicle were compiled and maintained at English monastic centres — Winchester, Abingdon, Worcester, Canterbury — reflecting the English ecclesiastical perspective that shapes the Viking entries"}
    ],
    "subjects": ["Medieval History", "Medieval Era", "Anglo-Saxon England", "Viking Age", "Primary Sources", "English History", "Danelaw", "Alfred the Great"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Viking entries of the Anglo-Saxon Chronicle (793–1042) are the primary contemporary narrative source for the Viking Age in England — the foundational documentary record of Viking raids, the Great Heathen Army, the Danelaw, Alfred the Great's resistance, and the Danish conquest. As the central evidence for two and a half centuries of Anglo-Scandinavian history, their ecclesiastical perspective (Danes as pagan destroyers) shaped the medieval and early modern image of Vikings and remains a central interpretive challenge for modern historians.",
      "significanceCategory": "highly-significant"
    }
  }
},

"gilgamesh-and-aga": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782gilgamesh-and-aga.json",
  "slug": "gilgamesh-and-aga",
  "data": {
    "summary": "Gilgamesh and Aga (Sumerian: dGilgameš u Akka) is a short Sumerian epic poem of approximately 115 lines, one of approximately eight Sumerian epic poems about Gilgamesh — composed in Sumerian in the early 2nd millennium BCE (probably during the Ur III or early Old Babylonian period, c. 2000–1800 BCE), though it describes events set in the Early Dynastic period of Mesopotamia (c. 2700 BCE). The poem narrates a political confrontation between Gilgamesh, king of Uruk, and Aga (or Agga), king of Kish — the leading city of Sumer before Uruk — over the question of Uruk's submission to Kish. Gilgamesh, against the advice of the elders' assembly, rallies the warriors' assembly and refuses to submit to Aga; the poem culminates in a siege of Uruk by Aga's forces, the dramatic appearance of Gilgamesh on the battlements, the recognition of Gilgamesh's power by Aga's men, and a surprising resolution in which Gilgamesh releases Aga without battle, acknowledging an old debt of gratitude.\n\nGilgamesh and Aga has attracted particular scholarly attention because it is the only Sumerian Gilgamesh poem with no mythological or divine elements — it is a purely historical or pseudo-historical narrative about political relationships between city-states, and it has been used as evidence for the existence of a historical Gilgamesh (the historical king of Uruk who founded the dynasty that broke Kish's hegemony) and for early Mesopotamian political institutions (the 'bicameral' assembly of elders and warriors that Gilgamesh consults is the earliest known reference to a representative political assembly in world history). This reference to a bicameral assembly — predating Greek democracy by almost two thousand years — has made Gilgamesh and Aga a significant document in the history of political thought.\n\nThe poem is also notable for its literary technique — particularly the poem's climactic scene in which Gilgamesh's heroic appearance on the battlements causes Aga's men to fall back in awe — which has been analysed as an early example of the literary technique of the hero's radiant power (melammu, divine aura) that appears throughout Mesopotamian literature.",
    "causes": [
      "The political history of Early Dynastic Sumer — the competition between the city-states of Kish and Uruk for hegemony over Mesopotamia in the 3rd millennium BCE — provided the historical context for the narrative: the poem reflects, in literary form, the political transition in which Uruk under the Gilgamesh dynasty broke Kish's hegemony.",
      "The Ur III literary programme — the systematic composition and transmission of Sumerian literary texts at the schools (edubba) of Nippur and other cities during the Ur III and early Old Babylonian periods — created the context for the composition and preservation of the Sumerian Gilgamesh poems, including Gilgamesh and Aga.",
      "The Sumerian tradition of composing literary texts about heroic kings — the practice of celebrating historical or legendary kings through poetry that blended historical memory, mythological elaboration, and literary convention — provided the generic framework for Gilgamesh and Aga as a political narrative about a historical king."
    ],
    "effects": [
      "Gilgamesh and Aga's reference to a 'bicameral' assembly of elders and warriors — an early form of deliberative political institution in which Gilgamesh consults two assemblies before deciding on war — has been cited in the history of political thought as the earliest known reference to a representative or consultative political assembly, predating the Greek demos by almost two thousand years.",
      "The poem's status as the only Sumerian Gilgamesh poem with no supernatural elements — making it the primary evidence for a historical Gilgamesh and his political relationships — has made it an important source for historians attempting to reconstruct the historical kernel of the Gilgamesh tradition.",
      "The melammu (divine aura) literary technique in Gilgamesh and Aga — the hero's appearance causing enemies to fall back in awe — is an early literary example of a technique that recurs throughout ancient Near Eastern and biblical literature, demonstrating the literary continuities across the ancient Near Eastern textual tradition."
    ],
    "relationships": [
      {"sourceSlug": "gilgamesh-and-aga", "sourceName": "Gilgamesh and Aga (Sumerian epic, c. 2000–1800 BCE)", "verb": "PART_OF", "targetSlug": "sumerian-gilgamesh-cycle", "targetName": "Sumerian Gilgamesh cycle (8 Sumerian poems)", "context": "Gilgamesh and Aga is one of approximately eight Sumerian epic poems about Gilgamesh — the only one with no supernatural elements, making it the primary evidence for a historical Gilgamesh and his political relationships."},
      {"sourceSlug": "gilgamesh-and-aga", "sourceName": "Gilgamesh and Aga (bicameral assembly, political institutions)", "verb": "DOCUMENTS", "targetSlug": "ancient-mesopotamian-politics", "targetName": "Early Mesopotamian political institutions (assembly of elders and warriors)", "context": "Gilgamesh and Aga contains the earliest known reference to a representative/consultative political assembly (elders' and warriors' assemblies) — cited in the history of political thought as evidence for pre-democratic deliberative institutions."},
      {"sourceSlug": "gilgamesh-and-aga", "sourceName": "Gilgamesh and Aga (Uruk vs. Kish, hegemony)", "verb": "DESCRIBES", "targetSlug": "gilgamesh-king-of-uruk", "targetName": "Gilgamesh, king of Uruk (legendary/historical, c. 2700 BCE)", "context": "The poem describes Gilgamesh's refusal to submit to Aga of Kish — reflecting the historical political transition in which Uruk under the Gilgamesh dynasty broke Kish's hegemony over Sumer."}
    ],
    "places": [
      {"name": "Uruk and Kish, Mesopotamia (Early Dynastic Sumer, c. 2700 BCE)", "role": "Uruk (Gilgamesh's city) and Kish (Aga's city) are the two great rival city-states of the poem's setting — the political confrontation between them reflects the Early Dynastic Sumerian competition for hegemony"},
      {"name": "Nippur (Ur III schools, edubba, poem composition and preservation)", "role": "The Sumerian Gilgamesh poems, including Gilgamesh and Aga, were composed and preserved in the edubba (scribal schools) of Nippur during the Ur III and early Old Babylonian periods — the primary context for the composition and transmission of Sumerian literary texts"}
    ],
    "subjects": ["Ancient Mesopotamian Literature", "Ancient Era", "Sumerian Literature", "Epic Poetry", "Gilgamesh", "Political History", "Ancient Near East", "Early Civilisation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Gilgamesh and Aga (Sumerian, c. 2000–1800 BCE) is the only Sumerian Gilgamesh poem without supernatural elements and the primary evidence for a historical Gilgamesh. Its reference to a bicameral assembly (elders and warriors) is the earliest known reference to a representative political institution in world history, predating Greek democracy by almost two thousand years. The poem demonstrates the literary and political sophistication of Early Dynastic Sumerian civilisation.",
      "significanceCategory": "significant"
    }
  }
},

"a-series-of-unfortunate-events": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-series-of-unfortunate-events.json",
  "slug": "a-series-of-unfortunate-events",
  "data": {
    "summary": "A Series of Unfortunate Events is a thirteen-volume children's and young adult novel series by Lemony Snicket (the pen name of Daniel Handler, born 1970), published by HarperCollins between 1999 (The Bad Beginning) and 2006 (The End), following the three Baudelaire orphans — Violet (inventor), Klaus (researcher), and Sunny (biter) — through a relentless series of disasters, near-escapes, and encounters with the villainous Count Olaf as they attempt to unravel the mysterious secret society (VFD — the Volunteer Fire Department) that their parents were involved in. The series sold over 65 million copies worldwide and is one of the most commercially successful children's novel series of the early 21st century.\n\nThe series is distinctive for its self-consciously literary and ironic narrative voice — Lemony Snicket addresses the reader directly throughout, repeatedly warning them not to read further, defining difficult words mid-sentence, and commenting on the artificiality of fiction — and for its sustained refusal of the consolations of conventional children's fiction: the children never fully defeat Count Olaf, their parents remain dead, the mysteries of VFD are never fully resolved, and the final volume ends ambiguously rather than with the conventional happy ending. This sustained darkness and irony — combined with a vocabulary-rich, self-aware prose style — gave the series an unusual appeal across multiple reading levels and contributed to its critical reputation as a significant literary achievement in the children's novel genre.\n\nThe series explores themes of institutional failure (the adults in positions of authority are almost universally ineffective, corrupt, or easily deceived), the importance of independent inquiry and scepticism, the unreliability of 'official' narratives, and the moral ambiguity of both heroes and villains — themes that resonated with an adult readership alongside the series' primary child audience. The series has been adapted as a film (2004, starring Jim Carrey as Count Olaf) and as a Netflix television series (2017–2019), which won critical acclaim for its faithful adaptation of the books' dark tone and ironic voice.",
    "causes": [
      "The fin-de-siècle Gothic literary tradition and its children's literary adaptations — the tradition of dark, uncanny, and ironic children's fiction (Edward Gorey's illustrations, Charles Addams's The Addams Family, Edward Lear's nonsense verse) — provided the aesthetic and tonal context for the series' sustained darkness and irony.",
      "Daniel Handler's deliberate choice to write anti-conventional children's fiction — his reaction against the conventions of children's literature that promise safety, adult competence, and happy resolution — drove the series' characteristic refusal of consolation and its sustained irony about the inadequacy of adult institutions.",
      "The late 1990s–2000s children's book market's appetite for long, complex novel series — created in part by the Harry Potter phenomenon (1997 onwards) — provided the commercial context for a thirteen-volume dark fantasy series aimed at the middle-grade and young adult readership."
    ],
    "effects": [
      "The series' commercial success (65 million copies) and critical reputation established dark, ironic, and vocabulary-rich children's fiction as a commercially viable alternative to conventional reassuring children's literature, contributing to the broader diversification of children's fiction in the early 21st century.",
      "The Netflix television adaptation (2017–2019) — critically praised for its faithful tone and Neil Patrick Harris's portrayal of Count Olaf — demonstrated the adaptability of the series' self-aware ironic voice to television and contributed to the wave of literary children's fiction adaptations for streaming platforms in the late 2010s.",
      "The series' exploration of institutional failure, scepticism toward 'official' narratives, and moral ambiguity contributed to a post-Harry Potter tradition of morally complex children's fiction that engaged with the realities of adult incompetence and institutional failure rather than assuming a protective and competent adult world."
    ],
    "relationships": [
      {"sourceSlug": "lemony-snicket", "sourceName": "Lemony Snicket (Daniel Handler, born 1970)", "verb": "AUTHORS", "targetSlug": "a-series-of-unfortunate-events", "targetName": "A Series of Unfortunate Events (1999–2006, 13 volumes)", "context": "Handler, writing as Lemony Snicket, published the thirteen-volume series between 1999 and 2006 — selling over 65 million copies and establishing the dark, ironic, self-aware voice as a distinctive contribution to children's literature."},
      {"sourceSlug": "a-series-of-unfortunate-events", "sourceName": "A Series of Unfortunate Events (dark ironic children's fiction)", "verb": "ADAPTED_AS", "targetSlug": "asoe-netflix-series", "targetName": "A Series of Unfortunate Events Netflix series (2017–2019)", "context": "The Netflix adaptation (2017–2019) starring Neil Patrick Harris as Count Olaf was critically praised for its faithful dark tone — demonstrating the series' ironic voice could be effectively translated to television."},
      {"sourceSlug": "a-series-of-unfortunate-events", "sourceName": "A Series of Unfortunate Events (Lemony Snicket narrative voice)", "verb": "RESPONDS_TO", "targetSlug": "conventional-childrens-fiction", "targetName": "Conventional children's fiction (adult competence, happy resolution)", "context": "The series is a deliberate anti-conventional children's fiction — its sustained refusal of adult competence, happy endings, and consoling resolution is a pointed reaction against the conventions of mainstream children's literature."}
    ],
    "places": [
      {"name": "United States (HarperCollins, 1999–2006 publication; American readership)", "role": "The series was published in the United States by HarperCollins between 1999 and 2006 — its dark tone and sophisticated irony resonated with an American readership across multiple age groups"},
      {"name": "Global (65 million copies, Netflix adaptation)", "role": "The series achieved global success — 65 million copies sold worldwide and the Netflix adaptation (2017–2019) bringing it to international streaming audiences"}
    ],
    "subjects": ["American Literature", "Modern Era", "Lemony Snicket", "Children's Literature", "Dark Fantasy", "Young Adult Fiction", "21st Century", "Novel Series"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Series of Unfortunate Events (Snicket/Handler, 1999–2006) is one of the most commercially successful children's novel series of the early 21st century (65 million copies), distinguished by its dark ironic tone, sophisticated narrative voice, and sustained refusal of conventional children's fiction reassurances. Its critical reputation as a significant literary achievement in children's fiction and the success of the Netflix adaptation (2017–2019) established dark, self-aware children's fiction as a commercially and critically viable alternative to conventional reassuring children's literature.",
      "significanceCategory": "significant"
    }
  }
},

"artemis-fowl": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783artemis-fowl.json",
  "slug": "artemis-fowl",
  "data": {
    "summary": "Artemis Fowl is an eight-volume young adult fantasy novel series by the Irish author Eoin Colfer (born 1965), published by Puffin Books between 2001 (Artemis Fowl) and 2012 (The Last Guardian), featuring the eponymous protagonist Artemis Fowl II — a twelve-year-old Irish criminal mastermind and genius — and the LEPrecon (Lower Elements Police reconnaissance) fairy world hidden beneath the Earth's surface. The series follows Artemis's complex relationship with the fairy police officer Captain Holly Short and the underground fairy civilisation (a high-tech, scientifically advanced society of fairies, dwarfs, centaurs, and goblins) — beginning with Artemis's attempt to steal the fairy Book to learn their secrets and extort their gold, and evolving through the subsequent volumes into an alliance between Artemis and the fairy world to combat various threats, including rogue trolls, human villains, and time paradoxes. The series sold over 25 million copies worldwide and was described by Colfer as 'Die Hard with fairies'.\n\nArtemis Fowl's distinctive contribution to young adult fantasy is its subversion of the fairy tale genre conventions — its fairies are not ethereal, benevolent beings of folklore but technologically sophisticated, bureaucratically organised, and morally complex creatures, policing the human world from a hidden underground civilisation, armed with advanced weapons (neutrinos, bio-bombs), time-stop capability (the time field), and fairy magic (healing, mesmerising, the shield). The series combines the conventions of the heist thriller (Artemis as criminal mastermind planning elaborate schemes), the spy thriller (LEPrecon's intelligence operations), and the fantasy adventure, creating a hybrid genre that appealed to the action-oriented young adult readership of the early 21st century.\n\nThe series was adapted as a film by Disney (Artemis Fowl, 2020, directed by Kenneth Branagh) — a production that received generally negative reviews, was released directly to Disney+ during the COVID-19 pandemic, and was criticised for substantially altering the source material's tone and plot.",
    "causes": [
      "The late 1990s–early 2000s young adult fantasy boom — driven by the Harry Potter phenomenon — created a market for inventive, high-concept fantasy series that could appeal to older children and young adults, providing the commercial context for Artemis Fowl's reception.",
      "Colfer's deliberate subversion of fairy tale genre conventions — his decision to reimagine fairies as technologically sophisticated underground beings rather than ethereal folklore creatures — provided the creative concept that distinguished the series from the fantasy genre field: the 'sci-fi thriller fairy tale' concept was the series' primary market differentiator.",
      "The heist thriller tradition — the elaborate criminal planning and execution sequences that structure many of the novels' central plots — provided the narrative model for Artemis Fowl's distinctive combination of criminal mastermind protagonist and fantasy world-building: Colfer grafted heist thriller conventions onto fantasy genre structures."
    ],
    "effects": [
      "Artemis Fowl's commercial success (25 million copies) established the Irish author Eoin Colfer as one of the most commercially successful fantasy writers of the early 21st century and demonstrated the global appeal of Irish children's fiction beyond its domestic market.",
      "The series' conception of fairies as technologically advanced underground beings — equipped with advanced weapons, time-stop capability, and bureaucratic organisations — influenced the subsequent development of the 'urban fantasy' and 'tech-fantasy' genres, where magical beings are embedded in modern technological contexts.",
      "The Disney film adaptation (2020) — despite its critical failure — demonstrated the commercial ambitions of the Disney franchise machine for non-American fantasy properties in the streaming era, and the circumstances of its pandemic release (directly to Disney+) contributed to the broader discussion about theatrical vs. streaming release strategies."
    ],
    "relationships": [
      {"sourceSlug": "eoin-colfer", "sourceName": "Eoin Colfer (born 1965, Ireland)", "verb": "AUTHORS", "targetSlug": "artemis-fowl", "targetName": "Artemis Fowl series (2001–2012, 8 volumes)", "context": "Colfer, an Irish author, published the eight-volume Artemis Fowl series between 2001 and 2012 — selling over 25 million copies and establishing the concept of technologically sophisticated underground fairy civilisation."},
      {"sourceSlug": "artemis-fowl", "sourceName": "Artemis Fowl (subverted fairy fantasy)", "verb": "RESPONDS_TO", "targetSlug": "traditional-fairy-tale-genre", "targetName": "Traditional fairy tale genre (benevolent ethereal fairies)", "context": "Artemis Fowl deliberately subverts fairy tale genre conventions — its fairies are technologically advanced, bureaucratically organised underground beings, not the ethereal benevolent creatures of folklore."},
      {"sourceSlug": "artemis-fowl", "sourceName": "Artemis Fowl (Disney film, 2020)", "verb": "ADAPTED_AS", "targetSlug": "artemis-fowl-film-2020", "targetName": "Artemis Fowl (Disney film, Kenneth Branagh, 2020)", "context": "Disney's 2020 film adaptation — directed by Kenneth Branagh and released directly to Disney+ during the pandemic — received generally negative reviews for substantially altering the source material's tone."}
    ],
    "places": [
      {"name": "Ireland (Eoin Colfer, Dublin setting of series opener)", "role": "Colfer is an Irish author and Artemis Fowl's home is in Ireland — the Irish setting grounds the series in a specific cultural geography, with Fowl Manor as the protagonist's base"},
      {"name": "The Lower Elements (underground fairy world beneath the Earth's surface)", "role": "The Lower Elements — the technologically advanced underground civilisation of fairies, dwarfs, centaurs, and goblins — is the primary fantasy setting of the series, a hidden world existing beneath the human world"}
    ],
    "subjects": ["Irish Literature", "Modern Era", "Eoin Colfer", "Young Adult Fiction", "Fantasy Fiction", "Children's Literature", "21st Century", "Novel Series"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Artemis Fowl (Colfer, 2001–2012) is one of the most commercially successful young adult fantasy series of the early 21st century (25 million copies), distinguished by its subversion of fairy tale conventions through a technologically sophisticated underground fairy civilisation and its heist thriller protagonist. As the most commercially successful Irish children's fantasy series of its era, it demonstrated the global appeal of Irish children's fiction and influenced the tech-fantasy subgenre.",
      "significanceCategory": "significant"
    }
  }
},

"carroccio": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784carroccio.json",
  "slug": "carroccio",
  "data": {
    "summary": "The carroccio (plural: carrocci) is a large ox-drawn war-wagon bearing the standard and bell of a medieval Italian commune, used as a rallying point and symbol of civic unity in battle by the city-states of northern Italy from approximately the 11th to the 14th century CE. The carroccio was typically a four-wheeled ox-drawn cart bearing a large mast from which the civic standard (gonfalon) of the commune flew, accompanied by a large bell (the campanile mobile, 'mobile bell tower') that was used to signal tactical commands during battle. The oxen drawing the carroccio were usually white, specially fed and cared for, and considered sacred; the cart itself was decorated with the civic colours and symbols of the commune; and the standard-bearer defending the carroccio in battle was a position of the highest honour — the loss of the carroccio in battle was a catastrophic symbol of defeat, and its capture by an enemy was the ultimate humiliation.\n\nThe carroccio was first recorded in use by Archbishop Aribert of Milan (c. 1039 CE) and became a central feature of the military organisation of the Lombard communes during the Lombard League's wars against the Holy Roman Emperor Frederick I Barbarossa in the 12th century — most famously at the Battle of Legnano (29 May 1176), where the combined forces of the Lombard League defeated Barbarossa's army, protecting the carroccio of Milan as the symbolic centre of communal resistance. The Battle of Legnano and the carroccio of Milan are among the most powerful symbols in Italian national memory — the battle is cited as the first great Italian military victory against imperial domination.\n\nThe carroccio is one of the most distinctive symbols of the medieval Italian commune — a physical embodiment of the civic unity, collective honour, and communal identity that the communes of northern Italy developed in opposition to feudal hierarchies and imperial authority. As a symbol, it represents the transition from feudal military culture (in which loyalty was personal, to a lord) to communal military culture (in which loyalty was collective, to the city), making it a significant marker in the history of Italian civic culture.",
    "causes": [
      "The development of the medieval Italian communes — the city-states of northern Italy (Milan, Florence, Bologna, Cremona, Pavia, Lodi) that emerged from episcopal and royal control in the 11th–12th centuries — created the civic culture that gave rise to the carroccio: the need for a physical symbol of collective civic identity and honour in battle.",
      "The Lombard League's wars against Frederick Barbarossa (1167–1183) — the alliance of northern Italian communes against imperial domination — gave the carroccio its most dramatic historical context: the Battle of Legnano (1176), where the carroccio of Milan was the symbolic centre of communal resistance to imperial authority.",
      "The Italian tradition of civic symbolism — the elaborate system of civic banners, standards, communal bells, and ceremonial objects through which the medieval Italian communes expressed their collective identity and exercised civic religion — provided the cultural context for the carroccio as a sacred and political symbol of communal unity."
    ],
    "effects": [
      "The Battle of Legnano (1176) and the carroccio's role in it became a central element of Italian national memory — Verdi's opera La battaglia di Legnano (1849, originally 'La vittoria di Legnano') was performed during the 1848 Risorgimento revolutions as a symbol of Italian resistance to Austrian domination, drawing directly on the medieval carroccio tradition.",
      "The carroccio's symbolism — the communal war-wagon as an expression of civic unity and collective honour — influenced the development of Italian civic culture and the tradition of municipal self-governance that has shaped northern Italian political culture from the medieval communes to the modern Lega Nord's invocations of communal heritage.",
      "The carroccio is one of the primary symbols discussed in the modern Italian historical literature on the medieval communes — its role in the Battle of Legnano and the Lombard League's resistance to Barbarossa has made it a central reference point in the historiography of Italian civic identity and the origins of Italian communal self-governance."
    ],
    "relationships": [
      {"sourceSlug": "carroccio", "sourceName": "Carroccio (Lombard communes, communal standard)", "verb": "SYMBOL_OF", "targetSlug": "lombard-communes", "targetName": "Medieval Lombard city-states and communes (11th–14th century)", "context": "The carroccio was the primary symbol of the medieval Italian communes — a physical embodiment of civic unity and collective honour, used as a rallying point in battle by the city-states of northern Italy."},
      {"sourceSlug": "carroccio", "sourceName": "Carroccio (Battle of Legnano, 1176)", "verb": "CENTRAL_TO", "targetSlug": "battle-of-legnano-1176", "targetName": "Battle of Legnano (29 May 1176, Lombard League vs. Barbarossa)", "context": "The Battle of Legnano (1176) — where the Lombard League defeated Frederick Barbarossa — is the most famous episode involving the carroccio: the Milan carroccio was the symbolic centre of communal resistance and the battle became a central element of Italian national memory."},
      {"sourceSlug": "carroccio", "sourceName": "Carroccio (Risorgimento, Verdi)", "verb": "SYMBOLISES", "targetSlug": "italian-risorgimento", "targetName": "Italian Risorgimento (19th-century unification movement)", "context": "Verdi's opera La battaglia di Legnano (1849) drew on the carroccio tradition to symbolise Italian resistance to Austrian domination during the 1848 Risorgimento revolutions — connecting medieval communal symbolism to 19th-century national liberation."}
    ],
    "places": [
      {"name": "Milan and northern Italy (Lombard communes, 11th–14th century)", "role": "The carroccio was used by the city-states of northern Italy — particularly Milan, whose carroccio was central to the Battle of Legnano — as a symbol of communal unity and military honour"},
      {"name": "Legnano, Lombardy (Battle of Legnano, 29 May 1176)", "role": "The Battle of Legnano — where the Lombard League defeated Barbarossa's imperial forces — is the defining historical moment of the carroccio tradition, the event that made the Milan carroccio a symbol of Italian civic resistance"}
    ],
    "subjects": ["Medieval History", "Medieval Era", "Italian Communes", "Civic Culture", "Military History", "Lombardy", "Symbol History", "Medieval Italy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The carroccio — the ox-drawn war-wagon and civic standard of the medieval Italian communes — is one of the most distinctive symbols of communal civic culture in medieval European history. Its role at the Battle of Legnano (1176), where the Lombard League defeated Frederick Barbarossa, made it a central symbol of Italian civic identity and national memory, later invoked by Verdi's Risorgimento opera and modern Italian regional politics. It represents the transition from feudal personal loyalty to communal collective identity.",
      "significanceCategory": "significant"
    }
  }
},

"plan-do-check-adjust": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785plan-do-check-adjust.json",
  "slug": "plan-do-check-adjust",
  "data": {
    "summary": "Plan-Do-Check-Act (PDCA, also known as the Deming cycle, Shewhart cycle, or PDSA — Plan-Do-Study-Act in W. Edwards Deming's preferred formulation) is a four-stage iterative management methodology for continuous improvement of processes, products, and services — one of the foundational frameworks of quality management, lean manufacturing, and organisational improvement. The cycle consists of four stages: Plan (identify an opportunity for improvement and plan a change), Do (implement the change on a small scale), Check/Study (analyse the results and determine whether the change achieved the desired improvement), and Act/Adjust (if the improvement was successful, implement it on a larger scale; if not, revise the plan and repeat the cycle). The methodology is designed to be iterative — the 'Act' stage feeds back into the 'Plan' stage of the next cycle — creating a continuous spiral of learning and improvement.\n\nThe PDCA cycle was developed by Walter A. Shewhart (1891–1967) — the American physicist and statistician who pioneered statistical process control at Bell Telephone Laboratories — and was popularised and elaborated by W. Edwards Deming (1900–1993), who introduced it to Japanese industry during the post-war reconstruction period (from 1950 onwards). Deming's influence on Japanese manufacturing quality — through his lectures to Japanese engineers and managers (the Union of Japanese Scientists and Engineers, JUSE, from 1950) and his championing of statistical methods and continuous improvement — is credited as a major factor in Japan's post-war industrial transformation and the development of the Toyota Production System, Total Quality Management (TQM), and the just-in-time manufacturing revolution. The Deming Prize (established by JUSE in 1950) is Japan's most prestigious quality management award, named in Deming's honour.\n\nIn the late 20th and early 21st centuries, PDCA was incorporated into the ISO 9001 quality management standard, the Six Sigma methodology, the ISO 14001 environmental management standard, and numerous other management frameworks, making it one of the most widely applied management methodologies in the world — used in manufacturing, healthcare, education, software development, and public administration.",
    "causes": [
      "Walter Shewhart's development of statistical process control at Bell Telephone Laboratories in the 1920s–1930s — his insight that manufacturing processes vary statistically and that this variation can be monitored and controlled through statistical methods — provided the intellectual foundation from which the PDCA cycle was developed: the cycle is essentially a systematic framework for applying statistical learning to process improvement.",
      "W. Edwards Deming's post-war lectures to Japanese industrialists (1950 onwards) — his introduction of statistical quality methods and the PDCA cycle to Japanese manufacturing companies — created the practical application context in which the methodology proved most transformatively effective: Japan's post-war industrial reconstruction was the proving ground for PDCA's effectiveness at scale.",
      "The failure of American manufacturing quality in the post-war period — the contrast between Japanese quality improvement (driven by Deming's methods) and American quality decline — eventually forced American companies to adopt continuous improvement methodologies in the 1970s–1980s, creating the broader quality management movement (TQM, ISO 9001, Six Sigma) in which PDCA is embedded."
    ],
    "effects": [
      "Deming's introduction of PDCA and statistical quality methods to Japan (1950 onwards) is credited as a major factor in Japan's post-war industrial transformation — the Toyota Production System, lean manufacturing, and Just-In-Time (JIT) all draw on the continuous improvement logic of the PDCA cycle, and Japan's quality revolution reshaped global manufacturing in the late 20th century.",
      "PDCA's incorporation into ISO 9001 (first published 1987, revised 2000, 2008, 2015) — the world's most widely adopted quality management standard, used by over one million organisations in over 170 countries — made it the global framework for quality management practice, embedding continuous improvement cycles in organisational management systems worldwide.",
      "The Deming Prize (established 1950, awarded annually by JUSE) has been Japan's most prestigious quality management award for over 70 years — and the American Deming Medal (established by the American Society of Quality) and related awards demonstrate the global recognition of Deming's contribution to management methodology through the PDCA framework."
    ],
    "relationships": [
      {"sourceSlug": "plan-do-check-adjust", "sourceName": "PDCA cycle (Shewhart, Bell Labs; Deming, Japan 1950)", "verb": "DEVELOPED_BY", "targetSlug": "w-edwards-deming", "targetName": "W. Edwards Deming (1900–1993, quality management)", "context": "Deming popularised the Shewhart-developed PDCA cycle through his lectures to Japanese industrialists from 1950 — his introduction of statistical quality methods and continuous improvement was a major factor in Japan's post-war industrial transformation."},
      {"sourceSlug": "plan-do-check-adjust", "sourceName": "PDCA (Toyota Production System, lean manufacturing)", "verb": "INFLUENCES", "targetSlug": "toyota-production-system", "targetName": "Toyota Production System (TPS, lean manufacturing)", "context": "The PDCA continuous improvement logic is one of the foundational principles of the Toyota Production System and lean manufacturing — the kaizen (continuous improvement) methodology embedded in TPS draws directly on PDCA's iterative learning cycle."},
      {"sourceSlug": "plan-do-check-adjust", "sourceName": "PDCA (ISO 9001, global quality management standard)", "verb": "INCORPORATED_IN", "targetSlug": "iso-9001", "targetName": "ISO 9001 quality management standard (adopted by 1M+ organisations)", "context": "PDCA is incorporated as the foundational framework of ISO 9001 — the world's most widely adopted quality management standard, used by over one million organisations in over 170 countries, embedding continuous improvement methodology globally."}
    ],
    "places": [
      {"name": "Bell Telephone Laboratories, USA (Shewhart, 1920s–1930s)", "role": "Shewhart developed statistical process control and the PDCA cycle at Bell Telephone Laboratories in the 1920s–1930s — the institutional origin of the methodology in the context of telecommunications manufacturing quality"},
      {"name": "Japan (Deming's lectures from 1950, Toyota, post-war industrial transformation)", "role": "Deming's lectures to Japanese industrialists from 1950 were the transformative application context for PDCA — Japan's post-war quality revolution, driven by Deming's methods, reshaped global manufacturing"}
    ],
    "subjects": ["Management Science", "Modern Era", "Quality Management", "Deming", "Continuous Improvement", "Manufacturing", "Methodology", "Business"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "PDCA (Plan-Do-Check-Act, Shewhart/Deming) is one of the most widely applied management methodologies in the world — incorporated into ISO 9001 (used by 1M+ organisations), lean manufacturing, and the Toyota Production System. Deming's introduction of PDCA to Japan from 1950 is credited as a major factor in Japan's post-war industrial transformation and quality revolution. Its influence on global manufacturing, healthcare, education, and public administration through ISO 9001 and related standards makes it one of the most consequential management frameworks in organisational history.",
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
