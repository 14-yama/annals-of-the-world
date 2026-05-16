#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 55 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities from 782-Class (epic poetry):
  odyssey (Homer), nibelungenlied, kalevala, jerusalem-delivered (Tasso),
  orlando-furioso (Ariosto), la-araucana (Ercilla)
From 781-Class (historical documents):
  first-folio-1623 (Shakespeare), domesday-book-1086
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-55-may2026"

ENRICHMENTS = {

"odyssey": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782odyssey.json",
  "slug": "odyssey",
  "data": {
    "summary": "The Odyssey (Ancient Greek: Ὀδύσσεια, Odysseia) is an ancient Greek epic poem attributed to Homer, composed in the 8th century BCE and regarded as one of the foundational texts of Western literature and world literary culture. The poem narrates in 24 books (approximately 12,110 lines of dactylic hexameter) the ten-year homeward journey of the hero Odysseus (Ulysses in Latin tradition) from Troy to his kingdom of Ithaca after the Trojan War — a journey complicated by divine wrath (the sea-god Poseidon), supernatural obstacles (the Cyclops Polyphemus, the witch Circe, the Sirens, Scylla and Charybdis), the temptations of immortality (the nymph Calypso), and the suitors who have invaded his household and court his wife Penelope in his absence.\n\nThe Odyssey is the paradigmatic text of the literary journey — the archetype from which all subsequent quest narratives, voyage tales, and homecoming stories derive their fundamental structure. The Homeric concept of nostos (νόστος, homecoming) gave English the word 'nostalgia' (coined in 1688 by Swiss physician Johannes Hofer from nóstos and álgos, 'pain'), and Odysseus's journey has been read as the prototype for the human condition of exile, longing, and return. The poem's episodic structure — each island a different trial, each encounter a different temptation or ordeal — established the episodic quest narrative as a fundamental literary form.\n\nThe Odyssey's influence on Western literature is incalculable — James Joyce's Ulysses (1922) uses the Odyssey as its structural framework, mapping Homer's episodes onto a single day in Dublin; Tennyson's Ulysses (1833) reimagines Odysseus in old age; Dante's Inferno (Canto 26) gives Odysseus a tragic final voyage beyond the pillars of Hercules; and the figure of the cunning, resourceful wanderer seeking home — the 'man of many devices' (polytropos) — is one of the most pervasive archetypes in world narrative. The Odyssey has been continuously read, translated, and reinterpreted across 2,800 years, generating an unbroken tradition of literary engagement.",
    "causes": [
      "The Greek oral tradition of epic poetry — the Mycenaean and Archaic Greek tradition of bardic performance, using the dactylic hexameter metre and a repertoire of formulaic phrases, epithets, and story patterns — produced the Odyssey as a summation of the oral epic tradition, attributed to the blind bard Homer and composed (or crystallised into its current form) in the 8th century BCE.",
      "The Bronze Age Greek memory of the Trojan War — whether historical or mythologised — provided the narrative framework for the Odyssey as the story of one hero's return from Troy, set against the background of a generation of displaced warriors whose homecomings ranged from triumphant to catastrophic.",
      "The geographical and cultural horizon of Archaic Greek exploration — the expansion of Greek trading and colonising voyages into the Mediterranean and Black Sea — provided the imaginative backdrop for Odysseus's wanderings, with the poem's mythologised geography (the land of the dead, the island of Circe, the Phaeacians) mapping onto the known and unknown edges of the Greek world."
    ],
    "effects": [
      "The Odyssey established the episodic quest narrative — the hero's journey through a series of trials and encounters toward a final homecoming — as one of the most fundamental and pervasive structures in world literature, influencing narrative forms from the Aeneid to the Arabian Nights to the modern novel.",
      "The Odyssey's influence on James Joyce's Ulysses (1922) — which uses the poem as its structural framework, mapping Homer's 24 books onto the 18 episodes of a single day in Dublin — is the most celebrated example of the poem's generative power in modern literature, demonstrating how the Homeric structure could be used to give shape to the modern stream-of-consciousness novel.",
      "The word 'odyssey' has entered most European languages as a common noun meaning a long, eventful journey or wandering — one of the most productive linguistic derivations from a literary title, demonstrating how completely the poem's narrative concept has been absorbed into everyday language and thought."
    ],
    "relationships": [
      {"sourceSlug": "homer", "sourceName": "Homer (8th century BCE — attributed composer; oral epic tradition; dactylic hexameter)", "verb": "AUTHORS", "targetSlug": "odyssey", "targetName": "The Odyssey (c. 8th century BCE — Odysseus's ten-year journey; foundational Western epic)", "context": "The Odyssey is attributed to Homer and composed in the 8th century BCE — the paradigmatic episodic quest narrative and one of the foundational texts of Western literary culture."},
      {"sourceSlug": "odyssey", "sourceName": "The Odyssey (Ulysses — Joyce 1922; stream-of-consciousness; modern novel structure)", "verb": "STRUCTURES", "targetSlug": "ulysses-joyce", "targetName": "Ulysses (James Joyce, 1922 — Homeric framework; 18 episodes; single day in Dublin)", "context": "James Joyce's Ulysses (1922) uses the Odyssey as its structural framework — mapping Homer's 24 books onto 18 episodes of a single day in Dublin, demonstrating the Homeric structure's capacity to give form to the modern novel."},
      {"sourceSlug": "odyssey", "sourceName": "The Odyssey (nostos — homecoming; nostalgia etymology; exile and return archetype)", "verb": "GENERATES_CONCEPT", "targetSlug": "nostalgia-concept", "targetName": "Nostalgia (from nóstos + álgos — coined 1688; longing for home; Odyssean archetype)", "context": "The Odyssey's concept of nostos (homecoming) gave English 'nostalgia' (coined 1688 by Hofer from nóstos and álgos) — demonstrating how the poem's central theme became a fundamental human psychological concept."}
    ],
    "places": [
      {"name": "Ancient Greece (8th century BCE — Archaic Greek oral tradition; Ionia; dactylic hexameter performance)", "role": "The Odyssey was composed in the oral tradition of Archaic Greece in the 8th century BCE — attributed to Homer, it crystallised the conventions of Greek epic performance into a text of extraordinary narrative complexity"},
      {"name": "Mediterranean (Odysseus's wandering — mythologised geography; Troy to Ithaca; Greek exploration horizon)", "role": "The Odyssey's mythologised Mediterranean geography — from Troy to the edges of the known world — reflects the horizon of Archaic Greek exploration, with each island representing a different encounter with the unknown"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Homer", "Epic Poetry", "Classical Literature", "Mythology", "Quest Narrative", "Western Canon"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Odyssey (Homer, c. 8th century BCE) is one of the foundational texts of Western literature — the episodic quest narrative that structured all subsequent voyage and homecoming tales, from the Aeneid to Ulysses (Joyce, 1922). The word 'odyssey' has entered most European languages as a common noun, and the concept of nostos (homecoming/nostalgia) is one of the most generative ideas in world literary and psychological culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"nibelungenlied": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782nibelungenlied.json",
  "slug": "nibelungenlied",
  "data": {
    "summary": "The Nibelungenlied (Middle High German: 'The Song of the Nibelungs') is a Middle High German epic poem composed around 1200 CE, preserved in three principal manuscripts (A, B, and C), with the B manuscript (Hohenems-Munich Codex) generally considered the most authoritative. The poem is divided into two parts (Aventiuren): the first part narrates the story of the hero Siegfried (Sigurd in Norse tradition) — his invulnerability (bathed in dragon's blood with a vulnerable spot where a linden leaf fell), his wooing of Kriemhild at the Burgundian court of Worms, his marriage to her, his role in winning the Icelandic queen Brunhild for King Gunther, and his murder by Hagen on orders of Gunther after a quarrel between the two queens; the second part narrates Kriemhild's revenge — her marriage to Attila (Etzel) the Hun, and her orchestration of the slaughter of the Burgundian court at the court of the Huns, culminating in the deaths of all the principal figures.\n\nThe Nibelungenlied is the German national epic — a work of extraordinary violence, tragedy, and psychological complexity that traces the collapse of an entire heroic world through conflicting loyalties, pride, deception, and revenge. Unlike the Arthurian romances contemporary with it, the Nibelungenlied offers no chivalric redemption, no spiritual transcendence: its world ends in mutual annihilation, and the poem's final image (Kriemhild herself killed by the old vassal Hildebrand) is one of absolute tragic waste.\n\nThe Nibelungenlied achieved enormous cultural significance in Germany and Austria — Richard Wagner's four-opera cycle Der Ring des Nibelungen (1876) is the most celebrated creative response to the Nibelungen material, transmuting the medieval poem into the most ambitious operatic project of the 19th century. The Nazis appropriated the 'Nibelungentreue' (loyalty of the Nibelungs) as a propaganda concept during World War II, associating German military sacrifice with Hagen's nihilistic loyalty — a legacy that complicated the poem's reception in postwar Germany.",
    "causes": [
      "The Norse-Germanic heroic tradition — the older Norse versions of the same story preserved in the Volsunga saga and the Poetic Edda (Eddic lays) — provided the raw material from which the Nibelungenlied was composed around 1200 CE by an anonymous Austrian or Bavarian court poet, who transformed the pagan heroic material into a courtly epic with contemporary medieval manners.",
      "The historical tradition of the Burgundian kingdom — the Burgundians were destroyed by Hunnic attack in 437 CE, preserving a historical memory of the encounter between Germanic peoples and Attila's Hunnic empire that became mythologised in the Nibelungen legend — provided the historical substratum for the poem's second part.",
      "The flourishing of courtly literary culture in the German-speaking lands around 1200 CE — the same cultural context that produced Wolfram von Eschenbach's Parzival and Gottfried von Straßburg's Tristan — provided the courtly literary context in which the Nibelungenlied was composed and received."
    ],
    "effects": [
      "Richard Wagner's Ring des Nibelungen (1876) — the four-opera cycle based on Nibelungen and Norse material, first performed complete at Bayreuth in 1876 — is the most celebrated creative response to the Nibelungenlied, transmuting medieval heroic tragedy into the most ambitious operatic project of the 19th century and establishing Bayreuth as a cultural institution.",
      "The Nazi appropriation of 'Nibelungentreue' — the concept of loyalty unto death derived from Hagen's nihilistic fidelity to the Burgundian cause — as a propaganda concept during World War II (notably in Joseph Goebbels's Sportpalast speech after Stalingrad, 1943) created a deeply problematic legacy that complicated the poem's postwar reception in Germany.",
      "The Nibelungenlied was inscribed by UNESCO in the Memory of the World register in 2009 — one of only a handful of literary manuscripts to receive this designation — recognising its status as a document of fundamental importance to world cultural heritage."
    ],
    "relationships": [
      {"sourceSlug": "nibelungenlied", "sourceName": "Nibelungenlied (c. 1200 CE — Siegfried, Kriemhild, Gunther, Hagen, Brunhild; German national epic)", "verb": "INSPIRES", "targetSlug": "ring-des-nibelungen-wagner", "targetName": "Der Ring des Nibelungen (Richard Wagner — 4-opera cycle; Bayreuth 1876; 19th-century German culture)", "context": "Wagner's Ring des Nibelungen (1876) is the most celebrated response to Nibelungen material — transmuting the medieval poem into a 19th-century operatic cycle that established Bayreuth as a cultural institution."},
      {"sourceSlug": "nibelungenlied", "sourceName": "Nibelungenlied (Nibelungentreue — Nazi propaganda; Goebbels; Stalingrad 1943)", "verb": "APPROPRIATED_BY", "targetSlug": "nazi-propaganda", "targetName": "Nazi propaganda (Nibelungentreue — loyalty unto death; Goebbels Sportpalast speech 1943)", "context": "The Nazis appropriated 'Nibelungentreue' as a propaganda concept — Goebbels invoked it in his Sportpalast speech after Stalingrad (1943), associating German military sacrifice with the poem's nihilistic heroic loyalty."},
      {"sourceSlug": "nibelungenlied", "sourceName": "Nibelungenlied (Volsunga saga, Norse Edda — same heroic material in different traditions)", "verb": "PARALLELS", "targetSlug": "volsunga-saga", "targetName": "Volsunga saga (Norse — Sigurd/Brynhildr/Gunnar; same Nibelungen heroic tradition)", "context": "The Nibelungenlied and the Volsunga saga narrate the same core Nibelungen story (the dragon-slayer, the queen quarrel, the revenge) in German and Norse traditions respectively — the comparison illuminates the shared Germanic heroic heritage."}
    ],
    "places": [
      {"name": "German-speaking lands (c. 1200 CE — Austrian/Bavarian court; Worms, Burgundy; historical setting)", "role": "The Nibelungenlied was composed around 1200 CE by an anonymous Austrian or Bavarian court poet — set at the Burgundian court of Worms and the court of Attila the Hun, it synthesised pagan heroic material with courtly medieval manners"},
      {"name": "Bayreuth, Germany (Wagner's Ring cycle — 1876 world premiere; Bayreuth Festspielhaus; cultural institution)", "role": "Wagner's Ring des Nibelungen (1876) established Bayreuth as a major cultural institution — the annual Bayreuth Festival remains one of the most important operatic events in the world, built on the Nibelungen cultural inheritance"}
    ],
    "subjects": ["German Literature", "Medieval Era", "Epic Poetry", "Germanic Culture", "Richard Wagner", "Opera", "Heroic Tradition", "World Heritage"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Nibelungenlied (c. 1200 CE) is the German national epic — a masterwork of medieval heroic tragedy that inspired Wagner's Ring des Nibelungen (1876) and was appropriated by Nazi propaganda ('Nibelungentreue'). Inscribed in UNESCO's Memory of the World register (2009), it is one of the foundational texts of German cultural identity and a document of fundamental importance to world cultural heritage.",
      "significanceCategory": "world-changing"
    }
  }
},

"kalevala": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782kalevala.json",
  "slug": "kalevala",
  "data": {
    "summary": "The Kalevala (Finnish: 'The Land of Heroes' or 'Land of the Kaleva') is the Finnish national epic, compiled and edited by Elias Lönnrot (1802–1884) from Finnish and Karelian oral folk poetry, published in its first edition (Old Kalevala, 32 runos) in 1835 and in its definitive second edition (50 runos, 22,795 lines) in 1849. Lönnrot collected folk songs (runosongs) from rural singers in Finland, Karelia, and Ingria — the Finnic runo-singing tradition in which songs were performed in pairs of singers using the kalevalaic metre (a form of trochaic tetrameter with extensive alliteration and parallelism) — and synthesised the collected material into a unified narrative epic.\n\nThe Kalevala narrates the mythological creation of the world and the adventures of the heroes and sorcerers of an ancient Finnish mythological age — centred on the wise old bard and shaman Väinämöinen, the craftsman and smith Ilmarinen (who forges the Sampo, a magical mill of prosperity), and the boisterous warrior Lemminkäinen — across cosmological, heroic, and tragic episodes that include the creation of the world from a duck's egg, the forging of the Sampo and its theft by the evil sorceress Louhi of the North, the creation of the first fire, and the tragic story of Kullervo (which J.R.R. Tolkien used as the basis for the story of Túrin Turambar in The Silmarillion).\n\nThe Kalevala is one of the most consequential acts of national myth-making in 19th-century Europe — its publication in 1835 and 1849 played a central role in the development of Finnish national consciousness during a period of Russian rule (Finland was a Grand Duchy of Russia 1809–1917), providing Finns with a mythological foundation for a distinct national identity comparable to the Norse Eddas or the Greek epics. The Kalevala directly inspired Jean Sibelius's orchestral and choral works (Kullervo, 1892; Lemminkäinen Suite, 1895–1897), became the inspiration for Henry Wadsworth Longfellow's The Song of Hiawatha (1855), and influenced J.R.R. Tolkien's mythology.",
    "causes": [
      "The Finnish and Karelian oral runo-singing tradition — the ancient tradition of collaborative performance of mythological and heroic songs in the kalevalaic metre, transmitted by rural singers across the Finnish and Karelian countryside — preserved the raw material from which Lönnrot compiled the Kalevala.",
      "Elias Lönnrot's extraordinary scholarly commitment — eleven field trips into rural Finland, Karelia, and Ingria between 1828 and 1844, collecting thousands of runosong variants from hundreds of singers — provided the empirical basis for the Kalevala's synthesis, demonstrating the convergence of Romantic nationalism and philological fieldwork.",
      "The political context of Finnish national awakening under Russian rule (1809–1917) — the desire for a distinctively Finnish national cultural identity, separate from both Swedish cultural dominance and Russian imperial rule — drove the reception of the Kalevala as a founding national text, comparable in its function to the Iliad for Greece or the Nibelungenlied for Germany."
    ],
    "effects": [
      "The Kalevala became the founding text of Finnish national identity — providing Finland with a mythological heritage that supported the development of national consciousness under Russian rule, and contributing to the eventual declaration of Finnish independence on 6 December 1917.",
      "Jean Sibelius drew extensively on the Kalevala for his major orchestral and choral works — Kullervo Symphony (1892), the Lemminkäinen Suite (1895–1897), and Pohjola's Daughter — establishing the Kalevala as the cultural foundation of the Finnish classical music tradition and making Sibelius the musical voice of Finnish national identity.",
      "Henry Wadsworth Longfellow's The Song of Hiawatha (1855) was directly modelled on the Kalevala — Longfellow used the kalevalaic metre (trochaic tetrameter) and the structural approach of the Kalevala as the framework for his American epic, demonstrating the Kalevala's international literary influence in the 19th century."
    ],
    "relationships": [
      {"sourceSlug": "elias-lonnrot", "sourceName": "Elias Lönnrot (1802–1884 — Finnish folklorist; eleven field trips; runo-singing collection)", "verb": "COMPILES", "targetSlug": "kalevala", "targetName": "Kalevala (1835/1849 — Finnish national epic; Väinämöinen, Sampo, Kullervo; Finnish identity)", "context": "Lönnrot compiled the Kalevala from oral runosong tradition collected during eleven field trips to Finland, Karelia, and Ingria — the definitive 1849 edition became the founding text of Finnish national identity."},
      {"sourceSlug": "kalevala", "sourceName": "Kalevala (Sibelius — Kullervo 1892; Lemminkäinen Suite; Finnish classical music tradition)", "verb": "INSPIRES", "targetSlug": "jean-sibelius", "targetName": "Jean Sibelius (1865–1957 — Kullervo Symphony 1892; Lemminkäinen Suite; Finnish national music)", "context": "Sibelius drew extensively on the Kalevala for his major orchestral works — Kullervo Symphony (1892), Lemminkäinen Suite (1895–1897) — establishing the Kalevala as the cultural foundation of Finnish classical music."},
      {"sourceSlug": "kalevala", "sourceName": "Kalevala (Kullervo — Tolkien's Túrin Turambar; The Silmarillion; mythology influence)", "verb": "INFLUENCES", "targetSlug": "j-r-r-tolkien", "targetName": "J.R.R. Tolkien (Kullervo story — Túrin Turambar; The Silmarillion; Finnish mythology)", "context": "Tolkien used the Kalevala's tragic Kullervo story as the basis for Túrin Turambar in The Silmarillion — and drew on the Finnish kalevalaic metre for the constructed Quenya language, demonstrating the Kalevala's deep influence on his mythology."}
    ],
    "places": [
      {"name": "Finland and Karelia (Lönnrot's field trips — runo-singing tradition; Finnish-Russian border region)", "role": "The Kalevala's raw material was collected in rural Finland, Karelia, and Ingria — the Finnish-Russian borderland where the ancient runo-singing tradition had survived, preserving Finnish mythological memory"},
      {"name": "Finland (Grand Duchy of Russia 1809–1917 — national awakening; independence 1917; founding national text)", "role": "The Kalevala played a central role in the development of Finnish national consciousness under Russian rule — the national epic provided the mythological foundation for Finnish identity, contributing to independence in 1917"}
    ],
    "subjects": ["Finnish Literature", "19th Century", "Folk Literature", "National Epic", "Mythology", "Elias Lönnrot", "Jean Sibelius", "Finnish Identity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Kalevala (Lönnrot, 1835/1849) is the Finnish national epic — one of the most consequential acts of national myth-making in 19th-century Europe, providing Finland with a mythological foundation for its national identity under Russian rule. It inspired Sibelius's major orchestral works, influenced Tolkien's mythology, and modelled Longfellow's Song of Hiawatha — demonstrating extraordinary international literary reach.",
      "significanceCategory": "world-changing"
    }
  }
},

"jerusalem-delivered": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782jerusalem-delivered.json",
  "slug": "jerusalem-delivered",
  "data": {
    "summary": "Jerusalem Delivered (Italian: Gerusalemme Liberata) is an Italian epic poem by Torquato Tasso (1544–1595), published in 1581 (an authorised edition of the text Tasso had been circulating in manuscript for years). The poem narrates the First Crusade (1095–1099) and the capture of Jerusalem in twenty cantos of ottava rima (eight-line stanzas in iambic elevens), centred on the Christian commander Goffredo di Buglione (Godfrey of Bouillon) and his efforts to unite the Crusader armies for the final assault on Jerusalem, complicated by the love affairs, distractions, and interventions of both Christian and Muslim warriors, pagan sorceresses, and the supernatural agency of God and Satan.\n\nJerusalem Delivered is the masterwork of the Italian Renaissance epic tradition and the final major product of the Counter-Reformation's attempt to unite Christian heroic values with classical epic form. Tasso consciously modelled his poem on both the Iliad and the Aeneid while subordinating classical epic conventions to the demands of Christian morality and Counter-Reformation orthodoxy — a project that generated the poem's central tension between the classical demands of epic (erotic episodes, heroic individualism, pagan magic) and the Christian demands of religious seriousness.\n\nJerusalem Delivered was enormously influential across European literature — it was the primary source for Peter Paul Rubens and Nicolas Poussin (both painted its scenes), it generated decades of operatic adaptations (Handel's Rinaldo, 1711, was based on Tasso's characters), and it was deeply read by Edmund Spenser (whose Faerie Queene is indebted to Tasso), John Milton (Paradise Lost echoes Tasso's Christian epic), and Voltaire (whose Henriade was modelled on Tasso). The poem's fame rested partly on Tasso's tragic biography — he spent seven years in an asylum at Sant'Anna in Ferrara (1579–1586), generating the Romantic myth of the 'mad genius' poet.",
    "causes": [
      "The Counter-Reformation cultural programme — the Catholic Church's attempt to use humanist literary culture for devotional and apologetic purposes — created the demand for a Christian epic that would unite the classical prestige of Homer and Virgil with the moral authority of the Church, producing the cultural context for Tasso's ambitious synthesis.",
      "Tasso's own complex personality — his simultaneous attraction to classical epic freedom (erotic episodes, pagan magic, heroic individualism) and anxiety about Counter-Reformation orthodoxy — drove both the poem's internal tensions and the obsessive revisions (Gerusalemme Conquistata, 1593) that consumed his later career.",
      "The historical memory of the Crusades and the ongoing Ottoman-Christian conflict in the Mediterranean — the Ottoman siege of Malta (1565) and the Battle of Lepanto (1571) were part of Tasso's world — gave the First Crusade subject matter contemporary political resonance and made the poem a contribution to Counter-Reformation Christian identity."
    ],
    "effects": [
      "Jerusalem Delivered generated a vast tradition of operatic adaptation — Handel's Rinaldo (1711), Vivaldi's Armida (1718), Monteverdi's Combattimento di Tancredi e Clorinda (1624), and dozens of later operas based on Tasso's episodes made the poem one of the most fertile sources of operatic material in the 17th and 18th centuries.",
      "Tasso's tragic biography — his seven years in the Sant'Anna asylum (1579–1586) — generated the Romantic myth of the 'mad genius' poet, inspiring Goethe's play Torquato Tasso (1790), Byron's The Lament of Tasso (1817), and Donizetti's opera Torquato Tasso (1833), making him one of the founding figures of the Romantic cult of the suffering artist.",
      "Jerusalem Delivered's influence on English literature — Spenser's Faerie Queene (1590–1596) is deeply indebted to Tasso's allegorical Christian epic structure, and Milton's Paradise Lost (1667) engages directly with Tasso's Counter-Reformation heroic theology — demonstrates the poem's transmission into the Protestant literary tradition despite its Catholic origins."
    ],
    "relationships": [
      {"sourceSlug": "torquato-tasso", "sourceName": "Torquato Tasso (1544–1595 — Italian Renaissance poet; Counter-Reformation epic; Sant'Anna asylum)", "verb": "AUTHORS", "targetSlug": "jerusalem-delivered", "targetName": "Jerusalem Delivered (1581 — Gerusalemme Liberata; First Crusade epic; ottava rima)", "context": "Tasso published Jerusalem Delivered in 1581 — the masterwork of the Italian Renaissance epic, attempting to unite classical epic form with Counter-Reformation Christian orthodoxy."},
      {"sourceSlug": "jerusalem-delivered", "sourceName": "Jerusalem Delivered (Handel's Rinaldo 1711 — operatic adaptations; Baroque opera; Tasso episodes)", "verb": "INSPIRES", "targetSlug": "baroque-opera-tasso", "targetName": "Baroque opera based on Tasso (Handel Rinaldo 1711; Vivaldi Armida; Monteverdi Combattimento)", "context": "Jerusalem Delivered generated a vast operatic tradition — Handel's Rinaldo (1711), Vivaldi's Armida, and Monteverdi's Combattimento di Tancredi e Clorinda made Tasso one of the most fertile sources of Baroque operatic material."},
      {"sourceSlug": "jerusalem-delivered", "sourceName": "Jerusalem Delivered (Spenser Faerie Queene; Milton Paradise Lost — English Protestant epic reception)", "verb": "INFLUENCES", "targetSlug": "paradise-lost-milton", "targetName": "Paradise Lost (Milton, 1667 — Counter-Reformation heroic theology; Christian epic tradition)", "context": "Milton's Paradise Lost (1667) engages directly with Tasso's Counter-Reformation heroic theology — demonstrating how Jerusalem Delivered transmitted the Italian Christian epic tradition into English Protestant literature."}
    ],
    "places": [
      {"name": "Ferrara, Italy (Tasso — Este court; Sant'Anna asylum 1579–1586; mad genius myth)", "role": "Tasso wrote Jerusalem Delivered at the Este court in Ferrara — his seven years in the Sant'Anna asylum (1579–1586) generated the Romantic myth of the 'mad genius' poet"},
      {"name": "Europe (Counter-Reformation — operatic adaptations; Spenser, Milton, Handel; continental influence)", "role": "Jerusalem Delivered's influence spread across Europe — generating operatic adaptations (Handel, Vivaldi, Monteverdi) and influencing English epic poets (Spenser, Milton), demonstrating the Italian Renaissance epic's transmission into Protestant literary culture"}
    ],
    "subjects": ["Italian Literature", "Renaissance Era", "Torquato Tasso", "Epic Poetry", "Counter-Reformation", "Opera", "Crusades Literature", "European Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Jerusalem Delivered (Tasso, 1581) is the masterwork of the Italian Renaissance epic — its synthesis of classical epic form and Counter-Reformation orthodoxy influenced Spenser's Faerie Queene and Milton's Paradise Lost, generated a vast operatic tradition (Handel's Rinaldo, 1711), and created the Romantic myth of the 'mad genius' poet through Tasso's seven years in the Sant'Anna asylum.",
      "significanceCategory": "highly-significant"
    }
  }
},

"orlando-furioso": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782orlando-furioso.json",
  "slug": "orlando-furioso",
  "data": {
    "summary": "Orlando Furioso ('Raging Roland') is an Italian Renaissance epic poem by Ludovico Ariosto (1474–1533), first published in 40 cantos in 1516 and completed in its definitive 46-canto form in 1532 — one of the longest poems in European literature at approximately 38,736 lines of ottava rima. The poem continues Matteo Maria Boiardo's unfinished Orlando Innamorato (c. 1495) and narrates the adventures of the paladins of Charlemagne in their wars against the Saracens, centred on the knight Orlando (Roland of the Chanson de Roland) who falls into a mad rage (the furioso) after the Saracen princess Angelica, whom he loves, elopes with the common soldier Medoro. The poem's multiple interwoven plotlines involve the knight Ruggiero (ancestor of the Este dynasty of Ferrara) and the female warrior Bradamante, the sorcerer Atlante's enchanted palace, the hippogryph, Astolfo's voyage to the Moon to recover Orlando's lost wits in a vial, and dozens of other episodes of love, war, magic, and adventure.\n\nOrlando Furioso is the supreme achievement of the Italian Renaissance romanzo — a form that combines the classical epic tradition (the war against external enemies) with the medieval romance tradition (individual adventure, love, magic, quest) in a consciously playful, ironic, humanist register. Ariosto's poem is distinguished by its narrative sophistication — the interlaced structure (entrelacement) that interrupts stories at moments of maximum tension to pursue other threads — and its constantly self-aware, witty narrator who comments on the action, addresses the reader directly, and makes clear that the poem is a literary artifice as much as a heroic narrative.\n\nOrlando Furioso is one of the most influential texts in European literary history — it influenced Edmund Spenser's Faerie Queene (1590–1596), William Shakespeare (Much Ado About Nothing, Othello), Miguel de Cervantes (Don Quixote engages directly with the romanzo tradition Ariosto perfected), and George Frideric Handel (Orlando, 1733; Alcina, 1735). The poem's complex, ironic narration and its self-aware critique of heroic convention anticipate the modern novel in important ways.",
    "causes": [
      "The Italian Renaissance court culture — particularly the Este court at Ferrara, where Ariosto spent most of his career — provided the aristocratic patronage and literary environment in which Orlando Furioso was composed, with the Este family directly honoured in the poem through the Ruggiero-Bradamante subplot that makes them the ancestors of a line of heroic Christian warriors.",
      "Boiardo's Orlando Innamorato (c. 1495) — left unfinished at Boiardo's death — provided the narrative starting point for Ariosto's poem: the characters, the setting, the Saracen war, and the central love triangle were all inherited from Boiardo and developed in Ariosto's more sophisticated, ironic register.",
      "The humanist culture of the Italian Renaissance — with its revival of classical learning, its self-conscious engagement with the classical epic tradition (Homer, Virgil), and its capacity for ironic distance from both classical and medieval traditions — provided the intellectual environment in which Ariosto could write a poem that is simultaneously a celebration of and an ironic commentary on the heroic tradition."
    ],
    "effects": [
      "Orlando Furioso's narrative technique — the interlaced structure (entrelacement) that weaves multiple plots simultaneously, interrupting each at moments of suspense — became one of the defining features of the romanzo tradition and profoundly influenced the development of the novel, with its capacity to manage multiple simultaneous storylines.",
      "The poem's influence on Shakespeare is significant — the plot of Much Ado About Nothing is largely derived from an episode in Orlando Furioso (Ariodante and Ginevra), and Othello's Iago-Cassio-Desdemona plot shares structural features with Ariosto's jealousy episodes, demonstrating the Italian Renaissance epic's transmission into English Renaissance drama.",
      "Ariosto's ironic, self-aware narrator — who comments on the action, addresses the reader directly, and makes clear that the poem is a literary artifice — is an important precursor to the self-aware narrative voice of the novel, and Don Quixote's direct engagement with the romanzo tradition (Cervantes's hero goes mad from reading too many romances) is a direct response to the Ariosto tradition."
    ],
    "relationships": [
      {"sourceSlug": "ludovico-ariosto", "sourceName": "Ludovico Ariosto (1474–1533 — Este court, Ferrara; 1516/1532 definitive edition)", "verb": "AUTHORS", "targetSlug": "orlando-furioso", "targetName": "Orlando Furioso (1516/1532 — 46 cantos; Orlando's madness; hippogryph; Moon voyage)", "context": "Ariosto published Orlando Furioso in 1516 (40 cantos) and completed it in 1532 (46 cantos) — the supreme achievement of the Italian Renaissance romanzo, combining epic and romance in a sophisticated ironic register."},
      {"sourceSlug": "orlando-furioso", "sourceName": "Orlando Furioso (Shakespeare — Much Ado About Nothing, Othello; Italian Renaissance influence)", "verb": "INFLUENCES", "targetSlug": "william-shakespeare", "targetName": "William Shakespeare (Much Ado About Nothing — Ariodante/Ginevra episode; Ariosto's jealousy plots)", "context": "Orlando Furioso directly influenced Shakespeare — the plot of Much Ado About Nothing derives from the Ariodante-Ginevra episode, demonstrating the Italian Renaissance epic's transmission into English Renaissance drama."},
      {"sourceSlug": "orlando-furioso", "sourceName": "Orlando Furioso (romanzo tradition — Don Quixote; Cervantes; self-aware heroic irony)", "verb": "ANTICIPATES", "targetSlug": "don-quixote", "targetName": "Don Quixote (Cervantes — romanzo parody; knight who goes mad from reading romances)", "context": "Don Quixote engages directly with the romanzo tradition that Ariosto perfected — Cervantes's hero goes mad from reading too many romances, making Ariosto's ironic treatment of heroic convention a direct precursor to Cervantes's satirical novel."}
    ],
    "places": [
      {"name": "Ferrara, Italy (Este court — Ariosto's patron; Ruggiero-Bradamante subplot; Renaissance literary culture)", "role": "Ariosto spent most of his career at the Este court in Ferrara — the poem honours the Este dynasty through the Ruggiero-Bradamante subplot, making it an exemplary product of Renaissance court patronage"},
      {"name": "Europe (Spenser's Faerie Queene; Shakespeare; Cervantes; Handel; French and English reception)", "role": "Orlando Furioso's influence spread across Europe — Spenser's Faerie Queene, Shakespeare's plots, Cervantes's Don Quixote, and Handel's operas (Orlando 1733, Alcina 1735) all demonstrate the poem's extraordinary transmission across European literary culture"}
    ],
    "subjects": ["Italian Literature", "Renaissance Era", "Ludovico Ariosto", "Epic Poetry", "Romance Literature", "Italian Renaissance", "European Literature", "Opera"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Orlando Furioso (Ariosto, 1516/1532) is the supreme achievement of the Italian Renaissance romanzo — its interlaced narrative structure, ironic self-aware narrator, and synthesis of epic and romance profoundly influenced Spenser, Shakespeare, Cervantes, and Handel. As a precursor to the novel's multiple-plotline technique and self-aware narration, it occupies a unique position in the transition from medieval epic to modern fiction.",
      "significanceCategory": "world-changing"
    }
  }
},

"la-araucana": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782la-araucana.json",
  "slug": "la-araucana",
  "data": {
    "summary": "La Araucana is a Spanish Renaissance epic poem by Alonso de Ercilla y Zúñiga (1533–1594), published in three parts between 1569 and 1589 — the first part (15 cantos) in 1569, the second (14 cantos) in 1578, and the third (8 cantos) in 1589. The poem narrates the Arauco War — the Spanish military campaign against the Mapuche people of what is now Chile, which Ercilla personally participated in as a young soldier — in 37 cantos of ottava rima, making it the first major literary work about the Americas and the first to give sympathetic, heroic treatment to indigenous American fighters resisting Spanish conquest.\n\nLa Araucana is distinguished by the remarkable sympathy and respect with which it portrays the Mapuche (Araucanian) warriors — particularly the leaders Caupolicán, Lautaro, and Colocolo — treating them as epic heroes comparable to the warriors of classical antiquity. Ercilla's poem presents the Spanish conquest of Chile as a genuine war between heroic peoples rather than a simple civilising mission against barbarism, and his portrait of Caupolicán's execution by the Spanish is one of the most emotionally complex passages in the poem. Miguel de Cervantes praised La Araucana in Don Quixote as one of the finest epic poems in Castilian or any other language.\n\nLa Araucana is a foundational text of Latin American cultural identity — the Mapuche warriors' resistance to Spanish conquest has been a symbol of Chilean and Latin American anti-colonial identity, and Caupolicán and Lautaro became national heroes of Chile. The poem established the tradition of the 'conquered peoples' epic in Spanish-language literature and has been central to debates about the Spanish conquest, colonial violence, and the representation of indigenous peoples in literature.",
    "causes": [
      "Ercilla's personal military experience — he participated in the Arauco War in Chile as a young courtier and soldier from 1557, directly witnessing the battles he describes — gave La Araucana an unprecedented firsthand authority and personal engagement that distinguished it from other Renaissance epics about distant historical subjects.",
      "The humanist epic tradition — the classical prestige of Homer and Virgil, the contemporary models of Ariosto and Tasso — provided the literary framework into which Ercilla poured his American experience, producing the paradox of a classical epic about indigenous American warriors who had never heard of Troy.",
      "The political and moral tensions of the Spanish conquest — Ercilla's own ambivalence about the justice of Spanish violence against the Mapuche, expressed throughout the poem in the sympathy he extends to the indigenous heroes — drove the poem's most original contribution: its treatment of the conquered peoples as genuine heroic subjects worthy of classical epic dignity."
    ],
    "effects": [
      "La Araucana became a foundational text of Latin American cultural identity — the Mapuche warriors Caupolicán, Lautaro, and Colocolo became national heroes of Chile, their portraits in Ercilla's poem providing the first literary models for a distinctively American heroic tradition.",
      "Cervantes praised La Araucana in Don Quixote (Part I, Chapter 6) as one of the richest treasures of epic poetry in Castilian and a rival to the best Italian epics — making La Araucana the only Spanish-language poem to receive this extraordinary endorsement from the author of Don Quixote.",
      "La Araucana established the tradition of the epic about indigenous peoples' resistance to colonial conquest — subsequent Spanish and Latin American epics about native resistance (Arauco Domado, 1596; the poems of the 19th-century independence period) followed the precedent set by Ercilla's sympathetic portrait of the Mapuche fighters."
    ],
    "relationships": [
      {"sourceSlug": "alonso-de-ercilla", "sourceName": "Alonso de Ercilla (1533–1594 — Spanish soldier-poet; Arauco War participant; Chile 1557)", "verb": "AUTHORS", "targetSlug": "la-araucana", "targetName": "La Araucana (1569–1589 — Arauco War; Mapuche heroes; first American epic)", "context": "Ercilla published La Araucana in three parts (1569–1589) — the first major literary work about the Americas, treating Mapuche warriors as epic heroes comparable to the warriors of classical antiquity."},
      {"sourceSlug": "la-araucana", "sourceName": "La Araucana (Cervantes — Don Quixote Part I Chapter 6; richest treasures of epic poetry)", "verb": "PRAISED_BY", "targetSlug": "don-quixote", "targetName": "Don Quixote (Cervantes — Part I, Chapter 6; La Araucana as finest Castilian epic)", "context": "Cervantes praised La Araucana in Don Quixote (Part I, Chapter 6) as one of the richest treasures of epic poetry in Castilian — the only Spanish epic to receive Cervantes's explicit endorsement."},
      {"sourceSlug": "la-araucana", "sourceName": "La Araucana (Caupolicán, Lautaro — Chilean national heroes; Mapuche resistance; anti-colonial identity)", "verb": "ESTABLISHES", "targetSlug": "chilean-national-identity", "targetName": "Chilean national identity (Caupolicán, Lautaro — Mapuche resistance heroes; anti-colonial tradition)", "context": "La Araucana's sympathetic portrait of Mapuche heroes Caupolicán and Lautaro made them national heroes of Chile — the poem established the anti-colonial resistance tradition central to Chilean and Latin American cultural identity."}
    ],
    "places": [
      {"name": "Chile (Arauco War 1550s–1880s — Mapuche resistance; Araucanía region; Ercilla's military service)", "role": "La Araucana is set in the Araucanía region of southern Chile — Ercilla's firsthand experience of the Arauco War (1557–1560) gave the poem its unprecedented immediacy and authentic portrayal of the Mapuche people"},
      {"name": "Spain / Latin America (foundational text — Chilean national heroes; anti-colonial identity; Cervantes's praise)", "role": "La Araucana became foundational to both Spanish Renaissance literature and Latin American cultural identity — praised by Cervantes as the finest Castilian epic, it established Caupolicán and Lautaro as Chilean national heroes"}
    ],
    "subjects": ["Spanish Literature", "Renaissance Era", "Alonso de Ercilla", "Epic Poetry", "Latin American Literature", "Mapuche Culture", "Colonial Literature", "Chilean Identity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "La Araucana (Ercilla, 1569–1589) is the first major literary work about the Americas — its sympathetic, heroic portrait of Mapuche warriors resisting Spanish conquest was praised by Cervantes as the finest Castilian epic. The poem established Caupolicán and Lautaro as Chilean national heroes and founded the tradition of the 'conquered peoples' epic in Spanish-language literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"first-folio-1623": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781first-folio-1623.json",
  "slug": "first-folio-1623",
  "data": {
    "summary": "The First Folio — formally Mr. William Shakespeares Comedies, Histories, & Tragedies — is the first collected edition of the plays of William Shakespeare (1564–1616), published in 1623 by the London printers Edward Blount, William Jaggard, and Isaac Jaggard, seven years after Shakespeare's death. The First Folio contains 36 plays — 18 of which appear in print for the first time — compiled and edited by Shakespeare's fellow actors and friends John Heminges and Henry Condell, who dedicated it to William Herbert, Earl of Pembroke, and Philip Herbert, Earl of Montgomery. The volume was printed in a large folio format and sold for approximately £1 (15–20 shillings), with an initial print run estimated at approximately 750 copies.\n\nThe First Folio is one of the most important books in the history of English literature — without it, 18 of Shakespeare's plays would almost certainly have been lost forever, including The Tempest, Macbeth, Measure for Measure, The Comedy of Errors, As You Like It, The Winter's Tale, Henry VI Parts 1 and 2, and Cymbeline. It is the primary source text for Shakespeare's plays and the foundation of all subsequent editions — every edition of Shakespeare's plays published since 1623 traces its lineage to the First Folio or to the quartos (earlier single-play editions) that preceded it.\n\nThe First Folio's cultural significance has only grown with time — approximately 235 copies survive (out of an estimated 750 original copies), making it one of the most valuable books in existence: a complete copy sold at Christie's in 2020 for $9.978 million (£7.5 million), making it the most expensive piece of printed text ever sold at auction. The First Folio is held in collections at the Folger Shakespeare Library (Washington, DC, with 82 copies — the largest single collection), the Bodleian Library (Oxford), and major libraries worldwide. It has been called 'the book that defined English literature.'",
    "causes": [
      "The deaths of Shakespeare's colleagues and collaborators — particularly the decision by Heminges and Condell to preserve Shakespeare's plays before the manuscripts were lost — drove the compilation of the First Folio; the two actors dedicated years of effort to collecting, editing, and seeing through the press the plays that Shakespeare had not himself prepared for publication.",
      "The English publishing trade's development of the folio format for collected works — the prestige of the large folio as a vehicle for serious literary works, used for Ben Jonson's Works (1616) — provided the model and the commercial context for the First Folio, which positioned Shakespeare's plays as worthy of the same literary dignity as classical texts.",
      "The existence of pirated 'bad quartos' — unauthorised, corrupt texts of Shakespeare's most popular plays that had been published during his lifetime — gave additional urgency to Heminges and Condell's project: they explicitly claimed in their preface to be correcting the 'stolen and surreptitious copies, maimed and deformed by the frauds and stealths of injurious impostors.'"
    ],
    "effects": [
      "The First Folio preserved 18 plays that would otherwise almost certainly have been lost forever — including Macbeth, The Tempest, As You Like It, and The Winter's Tale — fundamentally shaping the Shakespeare canon and making it the primary source text for all subsequent editions of Shakespeare's works.",
      "The First Folio is one of the most valuable books in existence — approximately 235 copies survive, and a complete copy sold at Christie's in 2020 for $9.978 million (the most expensive piece of printed text ever sold at auction) — demonstrating how the physical object has become a cultural monument as well as a literary artefact.",
      "The First Folio established the editorial tradition of Shakespeare scholarship — the problems of its text (printer's errors, theatrical revisions, variations between copies) generated the discipline of Shakespeare textual editing, which has produced thousands of editions, scholarly debates, and editorial schools over four centuries."
    ],
    "relationships": [
      {"sourceSlug": "william-shakespeare", "sourceName": "William Shakespeare (1564–1616 — playwright; Heminges and Condell; 36 plays)", "verb": "COLLECTED_IN", "targetSlug": "first-folio-1623", "targetName": "First Folio (1623 — 18 plays preserved; most expensive printed text at auction; primary Shakespeare source)", "context": "The First Folio (1623) collected 36 Shakespeare plays — preserving 18 that would otherwise have been lost, and becoming the primary source text for all subsequent editions of Shakespeare's works."},
      {"sourceSlug": "first-folio-1623", "sourceName": "First Folio (Christie's 2020 — $9.978 million; most expensive printed text at auction)", "verb": "VALUED_AT", "targetSlug": "book-auction-records", "targetName": "Book auction records (Christie's 2020 — $9.978 million; most expensive printed text ever sold)", "context": "A complete First Folio copy sold at Christie's in 2020 for $9.978 million — the most expensive piece of printed text ever sold at auction, demonstrating the book's status as a cultural monument."},
      {"sourceSlug": "first-folio-1623", "sourceName": "First Folio (Folger Shakespeare Library — 82 copies; largest single collection; Washington DC)", "verb": "PRESERVED_AT", "targetSlug": "folger-shakespeare-library", "targetName": "Folger Shakespeare Library (Washington DC — 82 First Folio copies; largest single collection)", "context": "The Folger Shakespeare Library (Washington DC) holds 82 First Folio copies — the largest single collection in the world, making it the primary research centre for the physical history of Shakespeare's collected works."}
    ],
    "places": [
      {"name": "London (1623 — Blount and Jaggard printers; Heminges and Condell; English publishing trade)", "role": "The First Folio was printed in London in 1623 by Blount and Jaggard — compiled by Shakespeare's fellow actors Heminges and Condell, it was printed in the London publishing district around St Paul's Churchyard"},
      {"name": "Washington DC / Oxford (Folger Shakespeare Library — 82 copies; Bodleian Library; global collections)", "role": "The 235 surviving First Folio copies are distributed across major libraries worldwide — the Folger Shakespeare Library (82 copies) and the Bodleian Library (Oxford) are the primary centres of First Folio scholarship"}
    ],
    "subjects": ["English Literature", "Renaissance Era", "William Shakespeare", "Publishing History", "Book History", "Literary Canon", "Textual Scholarship", "British Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The First Folio (1623) is one of the most important books in the history of English literature — without it, 18 Shakespeare plays (including Macbeth, The Tempest, As You Like It) would almost certainly have been lost forever. It is the primary source text for all Shakespeare editions, the most expensive piece of printed text ever sold at auction ($9.978 million, 2020), and 'the book that defined English literature.'",
      "significanceCategory": "world-changing"
    }
  }
},

"domesday-book-1086": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781domesday-book-1086.json",
  "slug": "domesday-book-1086",
  "data": {
    "summary": "The Domesday Book is the record of a comprehensive survey of the landholdings and resources of England commissioned by King William I (William the Conqueror, r. 1066–1087) and completed in 1086 — twenty years after the Norman Conquest of England. The survey was conducted by royal commissioners (legati) who travelled through England's counties, recording the ownership, value, population, and resources of each settlement as they existed in 1086 and (for comparison) at the time of the Conquest in 1066. The original record survives in two volumes: Great Domesday (a single fair copy of the county-by-county surveys for most of England) and Little Domesday (a more detailed record for Essex, Norfolk, and Suffolk). Both volumes are preserved at The National Archives at Kew, London.\n\nThe Domesday Book is the oldest surviving public record in England and one of the most remarkable administrative documents of the medieval world — the product of an extraordinary feat of bureaucratic organisation that surveyed virtually the entire settled kingdom of England in a single year. The survey recorded approximately 13,418 places and covered approximately 70% of England's settled area, providing a snapshot of Anglo-Norman England's social structure: the concentration of landholding in the hands of the Norman aristocracy (replacing the pre-Conquest Anglo-Saxon landowners), the distribution of the rural population between freemen, villeins, bordars, serfs, and slaves, and the relative values of manors across the kingdom.\n\nThe Domesday Book took its popular name from the 12th century — 'doomsday' reflecting both its finality (the judgements of the commissioners were treated as the last word on landholding, with no appeal) and its comprehensive scope. It is a foundational document of English constitutional and legal history — the primary source for Norman feudal landholding, a key text in the history of English common law, and a uniquely detailed demographic and economic snapshot of 11th-century England that has no parallel in medieval European history.",
    "causes": [
      "William the Conqueror's need to know the full extent of England's taxable resources — particularly after twenty years of Norman rule had redistributed almost all major landholdings from Anglo-Saxon to Norman magnates — drove the Domesday survey as an exercise in fiscal control, allowing the king to know exactly what dues and services each landholder owed the crown.",
      "The threat of a Danish invasion in 1085 — Canute IV of Denmark was assembling a fleet to invade England, and William needed to know the military resources available to him and to assess his magnates' obligations — gave additional urgency to the survey, which was decided at William's Christmas court at Gloucester in 1085.",
      "The Norman administrative tradition — the sophisticated bureaucratic capacity of the Norman duchy, with its experience of written governance, royal surveys, and fiscal records — provided the organisational methods and the concept of the comprehensive written survey, applied to England on a scale unprecedented in Anglo-Saxon governance."
    ],
    "effects": [
      "The Domesday Book became the primary legal authority for English property rights and taxation — medieval English courts routinely cited Domesday evidence to settle land disputes, and the book remained an active legal document for centuries after its compilation, demonstrating the extraordinary durability of a single 11th-century administrative survey.",
      "The Domesday Book is the primary source for English demographic and economic history in the 11th century — providing uniquely detailed evidence for the population, settlement, agriculture, and social structure of England at a period for which almost no comparable documentation survives in any other European kingdom.",
      "The Domesday Book is today held at The National Archives and has been digitised and made freely accessible — its digital edition (Open Domesday) and its continuous scholarly study have made it a living historical document consulted daily by researchers, genealogists, and local historians, demonstrating the remarkable longevity of a nearly 1,000-year-old administrative record."
    ],
    "relationships": [
      {"sourceSlug": "william-i-of-england", "sourceName": "William I (William the Conqueror, r. 1066–1087 — Norman Conquest; Christmas court Gloucester 1085)", "verb": "COMMISSIONS", "targetSlug": "domesday-book-1086", "targetName": "Domesday Book (1086 — Great Domesday, Little Domesday; English landholding survey; Norman feudal record)", "context": "William the Conqueror commissioned the Domesday survey at his Christmas court at Gloucester in 1085 — the completed record (1086) was the most comprehensive administrative survey of medieval Europe."},
      {"sourceSlug": "domesday-book-1086", "sourceName": "Domesday Book (fiscal record — landholding, taxation, social structure; Norman aristocracy)", "verb": "DOCUMENTS", "targetSlug": "norman-conquest-of-england", "targetName": "Norman Conquest of England (1066 — landholding redistribution; Anglo-Saxon to Norman aristocracy)", "context": "The Domesday Book documents the social and economic consequences of the Norman Conquest (1066) — recording the redistribution of almost all major landholdings from Anglo-Saxon to Norman magnates across 13,418 places."},
      {"sourceSlug": "domesday-book-1086", "sourceName": "Domesday Book (oldest public record — The National Archives, Kew; Open Domesday digital edition)", "verb": "PRESERVED_AT", "targetSlug": "the-national-archives-uk", "targetName": "The National Archives (Kew, London — oldest surviving English public record; Open Domesday digital)", "context": "The Domesday Book is preserved at The National Archives, Kew — the oldest surviving public record in England, now digitised and freely accessible through the Open Domesday project."}
    ],
    "places": [
      {"name": "England (1086 — Norman Conquest; 13,418 places surveyed; Great Domesday and Little Domesday)", "role": "The Domesday survey covered virtually the entire settled kingdom of England in 1086 — 13,418 places, providing an unparalleled snapshot of Anglo-Norman England's social and economic structure"},
      {"name": "The National Archives, Kew, London (Great Domesday and Little Domesday — preserved; digitised; Open Domesday)", "role": "The two Domesday volumes are preserved at The National Archives, Kew — the oldest surviving public records in England, continuously consulted for 900+ years and now freely accessible through digital edition"}
    ],
    "subjects": ["English History", "Medieval Era", "William the Conqueror", "Administrative History", "Norman Conquest", "Historical Records", "Feudalism", "Legal History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Domesday Book (1086) is the oldest surviving public record in England and one of the most remarkable administrative documents of the medieval world — a comprehensive survey of virtually the entire settled kingdom of England, documenting the social and economic consequences of the Norman Conquest. It remained an active legal document for centuries and is today the primary source for 11th-century English demographic and economic history.",
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
