#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 41 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: bluebeard, akbarnama-abulfazl, epigoni-epic, eteriani,
          aubrey-maturin-series, camunian-rose, physiology, pinch-analysis
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-41-may2026"

ENRICHMENTS = {

"bluebeard": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780bluebeard.json",
  "slug": "bluebeard",
  "data": {
    "summary": "Bluebeard (French: La Barbe bleue) is a French literary fairy tale written by Charles Perrault (1628–1703), first published in his Histoires ou contes du temps passé (1697) — the collection that also includes Cinderella, Sleeping Beauty, Little Red Riding Hood, and Puss in Boots — and one of the most psychologically compelling and culturally analysed tales in the Western fairy tale tradition. The tale narrates the story of a wealthy nobleman with a blue beard who marries a young woman after she overcomes her revulsion at his appearance; gives her the keys to all the rooms of his castle when he departs on a journey, forbidding her to enter one specific room; discovers on his return that she has disobeyed the prohibition (blood on the key), prepares to execute her for her disobedience, and is himself killed by her brothers who arrive to rescue her at the last moment. The tale's central motif — the forbidden room and the transgressive discovery — is one of the most ancient narrative patterns in world folklore.\n\nBluebeard's narrative pattern (the forbidden room, the dangerous curiosity, the murderous husband with multiple dead wives) draws on much older folk traditions — analogues appear in Norse mythology (Odin's forbidden knowledge, the price of wisdom), in the story of Psyche (Apuleius, The Golden Ass), in the Arabian Nights, and in German and Scandinavian folklore — but Perrault's literary version became the canonical Western text and the source of most subsequent literary and operatic treatments. The tale has attracted an extraordinary range of feminist, psychoanalytic, and literary interpretations: early readers saw it as a moral tale warning women against disobedience and curiosity; feminist critics (Angela Carter, Margaret Atwood, Marina Warner) have reread it as a tale of female subjugation, the dangerous husband, and the violence concealed in domestic spaces; psychoanalytic critics have interpreted the forbidden room as a figure for repressed knowledge, sexuality, and death.\n\nBluebeard's influence on European literature, opera, and popular culture has been immense — the Bluebeard figure and the forbidden room appear in Charlotte Brontë's Jane Eyre (Rochester's mad wife in the attic), in Béla Bartók's opera Duke Bluebeard's Castle (1911), in dozens of Gothic novels, and in Angela Carter's revisionist fairy tales (The Bloody Chamber, 1979).",
    "causes": [
      "The ancient folkloric motif of the forbidden room and the dangerous curiosity — appearing in multiple world mythologies and folk traditions — provided the narrative skeleton for Perrault's literary version: the Bluebeard tale is Perrault's literary crystallisation of a widespread folk narrative pattern that predates his 1697 version.",
      "Perrault's broader programme of collecting and literarising French folk tales — his Histoires ou contes du temps passé (1697) was a deliberate literary enterprise of elevating oral folk tales to literary status through elegant prose, moral appendages, and witty framing — provided the cultural context for Bluebeard: the tale is simultaneously a folk narrative and a refined literary product of the court culture of Louis XIV.",
      "The 17th-century context of marriage, property, and female agency — the legal and social context in which wives were subject to husbands' authority and in which a nobleman's right to dispose of a disobedient wife was not purely fictional — gives the Bluebeard tale its specific historical charge: the tale expresses real anxieties about the violence concealed within the domestic structures of early modern European marriage."
    ],
    "effects": [
      "Bluebeard's influence on the Gothic novel tradition — particularly on the figure of the dangerous husband who conceals violent secrets (Rochester in Jane Eyre, the Count in Dracula, the narrator's husband in The Yellow Wallpaper) — established the Bluebeard pattern as one of the foundational structures of Gothic domestic fiction, with its characteristic tension between domestic safety and hidden violence.",
      "Béla Bartók's one-act opera Duke Bluebeard's Castle (A kékszakállú herceg vára, 1911, libretto by Béla Balázs) transformed the Bluebeard tale into one of the masterpieces of 20th-century opera — the seven doors of Bluebeard's castle representing the layers of a soul's inner life — making Bluebeard a major figure in 20th-century music as well as literature.",
      "The feminist re-reading of Bluebeard — particularly Angela Carter's The Bloody Chamber (1979), which recasts the tale from the wife's perspective and transforms the male violence from punishment to horror — established Bluebeard as a primary site for feminist fairy tale criticism, demonstrating how the fairy tale genre can be both a vehicle of ideological normalisation and a resource for ideological critique."
    ],
    "relationships": [
      {"sourceSlug": "charles-perrault", "sourceName": "Charles Perrault (1628–1703)", "verb": "AUTHORS", "targetSlug": "bluebeard", "targetName": "Bluebeard (La Barbe bleue, 1697)", "context": "Perrault published Bluebeard in his Histoires ou contes du temps passé (1697) — the literary fairy tale collection that canonised Cinderella, Sleeping Beauty, and Bluebeard as foundational Western fairy tales."},
      {"sourceSlug": "bluebeard", "sourceName": "Bluebeard (forbidden room, Gothic domestic fiction)", "verb": "INFLUENCES", "targetSlug": "jane-eyre-bronte", "targetName": "Jane Eyre (Charlotte Brontë, 1847)", "context": "Bluebeard's pattern of the dangerous husband who conceals violent secrets influenced Charlotte Brontë's Jane Eyre — Rochester's mad wife in the attic replicates the Bluebeard forbidden room structure in the Gothic domestic novel."},
      {"sourceSlug": "bluebeard", "sourceName": "Bluebeard (feminist reinterpretation)", "verb": "REINTERPRETED_BY", "targetSlug": "angela-carter-bloody-chamber", "targetName": "Angela Carter, The Bloody Chamber (1979)", "context": "Angela Carter's The Bloody Chamber (1979) recast Bluebeard from the wife's perspective — a foundational feminist fairy tale revisioning that demonstrated how the Bluebeard pattern encodes ideologies of female subjugation."}
    ],
    "places": [
      {"name": "France (Perrault, court of Louis XIV, 1697 publication)", "role": "Bluebeard was published by Perrault in 1697 at the French court — the tale is simultaneously rooted in French folk tradition and shaped by the literary culture of Louis XIV's court"},
      {"name": "Europe and the world (Gothic novel, Bartók opera, feminist criticism)", "role": "Bluebeard's influence spread from France through European Gothic literature (Jane Eyre), opera (Bartók, 1911), and global feminist literary criticism — making it one of the most widely analysed fairy tales in the world"}
    ],
    "subjects": ["French Literature", "Early Modern Era", "Charles Perrault", "Fairy Tales", "Gothic Literature", "Feminist Criticism", "Folklore", "17th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Bluebeard (Perrault, 1697) is one of the most psychologically compelling and culturally analysed fairy tales in the Western tradition — a tale of the forbidden room, the dangerous husband, and the violence concealed in domestic spaces. Its influence on Gothic literature (Jane Eyre), opera (Bartók's Duke Bluebeard's Castle, 1911), and feminist fairy tale criticism (Angela Carter's The Bloody Chamber) is foundational. It remains a primary site for feminist and psychoanalytic interpretation of the fairy tale genre.",
      "significanceCategory": "highly-significant"
    }
  }
},

"akbarnama-abulfazl": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781akbarnama-abulfazl.json",
  "slug": "akbarnama-abulfazl",
  "data": {
    "summary": "The Akbarnama (Persian: اکبرنامہ, 'Book of Akbar') is the official biography and chronicle of the Mughal Emperor Akbar (r. 1556–1605), commissioned by Akbar himself and written by his court historian Abu'l-Fazl ibn Mubarak (1551–1602) — composed in Persian between c. 1590 and 1596, though the third volume (the Ain-i-Akbari, 'Institutes of Akbar') was revised over a longer period. The Akbarnama is the most important primary source for the reign of Akbar — the third Mughal emperor, the architect of the Mughal imperial system, and the ruler who oversaw the greatest territorial expansion and cultural florescence of the Mughal Empire. The work is divided into three volumes: the first two comprise the biographical narrative of Akbar's reign (from his birth and ancestry through the military campaigns, administrative reforms, and religious and cultural policies of his rule); the third volume, the Ain-i-Akbari, is a detailed administrative encyclopaedia of the Mughal Empire — a description of the empire's provinces, administrative structures, military organisation, revenues, and the customs, arts, and sciences of the Mughal court.\n\nAbu'l-Fazl was not merely a chronicler but a court ideologue — his Akbarnama presents Akbar through an elaborate theological and philosophical framework (the 'Perfect Man', Insan-i-Kamil, of Sufi thought) that legitimised Akbar's authority as a divine figure transcending conventional Islam and claiming universal spiritual sovereignty. Abu'l-Fazl's literary style — complex, ornate, metaphor-laden Persian prose — is both a monument of Mughal literary culture and a challenge to modern translators. The Akbarnama was translated into English by Henry Beveridge (3 volumes, 1897–1921, Calcutta) and has been the primary scholarly source for Akbar's reign since.\n\nThe Ain-i-Akbari's administrative encyclopaedia — its descriptions of the mansabdari system, the land revenue settlements (the Ain-i-Dah-Sala), the military, the court, and the arts — is one of the most valuable administrative and social documents of the 16th-century Mughal Empire, providing detail on the workings of the imperial system that cannot be recovered from any other source.",
    "causes": [
      "Akbar's programme of creating a legitimate, comprehensive imperial ideology — his synthesis of Persian, Hindu, and Islamic elements in the Din-i-Ilahi ('Religion of God'), his patronage of art and literature, and his administrative reforms — required an authoritative historical and administrative record, and the Akbarnama was the official historical expression of his imperial vision.",
      "Abu'l-Fazl's position as Akbar's closest intellectual companion and court ideologue — his relationship with Akbar involved not just historical documentation but the philosophical legitimation of Akbar's claim to universal spiritual authority — shaped the Akbarnama's combination of historical narrative and ideological framework.",
      "The Persian administrative and biographical chronicle tradition — the long-standing tradition of Persian court histories (tarikh) from Firdausi's Shahnameh through the chronicles of the Timurid and Safavid courts — provided the literary and generic models for the Akbarnama, which adapts the Persian court chronicle tradition to the ideological requirements of the Mughal imperial project."
    ],
    "effects": [
      "The Akbarnama's status as the primary source for Akbar's reign has made it the foundation of all modern scholarship on the Mughal Empire under Akbar — its historical narrative, administrative data, and court descriptions are the primary evidence for historians reconstructing the political, cultural, and administrative history of the most significant period of Mughal rule.",
      "The Ain-i-Akbari's administrative encyclopaedia — particularly its land revenue data, mansabdari lists, and provincial descriptions — provided the British colonial administration with its primary historical reference for understanding the pre-colonial Mughal administrative system, influencing colonial revenue settlements and administrative categories throughout India.",
      "Abu'l-Fazl's death in 1602 (assassinated on the orders of Prince Salim, the future Jahangir) before completing final revisions of the Akbarnama is itself a historical event that marks the end of Akbar's cultural circle — the assassination of the empire's ideologue signalled the transition to the next reign and the transformation of the Mughal imperial project."
    ],
    "relationships": [
      {"sourceSlug": "abul-fazl", "sourceName": "Abu'l-Fazl ibn Mubarak (1551–1602)", "verb": "AUTHORS", "targetSlug": "akbarnama-abulfazl", "targetName": "Akbarnama (c. 1590–1602)", "context": "Abu'l-Fazl wrote the Akbarnama at Akbar's commission — the official biography and administrative encyclopaedia of the Mughal Empire under Akbar, the primary source for the reign of the third Mughal emperor."},
      {"sourceSlug": "akbarnama-abulfazl", "sourceName": "Akbarnama (primary source for Akbar's reign)", "verb": "COMMISSIONED_BY", "targetSlug": "akbar", "targetName": "Mughal Emperor Akbar (r. 1556–1605)", "context": "The Akbarnama was commissioned by Akbar himself — Abu'l-Fazl's chronicle presents Akbar through a Sufi theological framework that legitimised his authority as a universal spiritual sovereign transcending conventional Islam."},
      {"sourceSlug": "akbarnama-abulfazl", "sourceName": "Ain-i-Akbari (administrative encyclopaedia)", "verb": "DOCUMENTS", "targetSlug": "mughal-empire-administration", "targetName": "Mughal Empire administrative system (mansabdari, land revenue)", "context": "The Ain-i-Akbari — the third volume of the Akbarnama — is a detailed administrative encyclopaedia of the Mughal Empire, providing data on the mansabdari system, land revenues, military, and provincial administration."}
    ],
    "places": [
      {"name": "Mughal court (Fatehpur Sikri, Agra, 1590s)", "role": "The Akbarnama was written at the Mughal court during the 1590s — Abu'l-Fazl was Akbar's court historian and closest intellectual companion, and the text was composed in the context of Akbar's cultural and administrative florescence"},
      {"name": "India (Mughal Empire, primary source for 16th-century Indian history)", "role": "The Akbarnama and Ain-i-Akbari are the primary sources for 16th-century Mughal India — used by modern historians and previously by British colonial administrators to understand the Mughal administrative system"}
    ],
    "subjects": ["Mughal History", "Early Modern Era", "Abu'l-Fazl", "Persian Literature", "Akbar", "Mughal Empire", "Historical Chronicle", "South Asian History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Akbarnama (Abu'l-Fazl, c. 1590–1602) is the primary historical source for the reign of Akbar — the most significant Mughal emperor — and the Ain-i-Akbari's administrative encyclopaedia is one of the most valuable administrative documents of 16th-century Asia. Abu'l-Fazl's ideological framing of Akbar as a divine universal sovereign shaped Mughal political theology. The work was used by British colonial administrators as their primary reference for pre-colonial Mughal administration.",
      "significanceCategory": "highly-significant"
    }
  }
},

"epigoni-epic": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epigoni-epic.json",
  "slug": "epigoni-epic",
  "data": {
    "summary": "The Epigoni (Greek: Ἐπίγονοι, 'Those Born After') is a lost ancient Greek epic poem belonging to the Epic Cycle — the collection of early Greek epic poems that supplemented Homer's Iliad and Odyssey with narratives of the Trojan War and other legendary events. The Epigoni narrated the second campaign against Thebes — the successful expedition led by the sons of the Seven Against Thebes (the Epigoni: Alcmaeon, Aegialeus, Diomedes, Thersander, Sthenelus, Promachus, and Euryalus), who avenged their fathers' failed first expedition (narrated in the earlier Thebaid epic) by sacking Thebes — a mythological event set in the generation before the Trojan War. The poem is known only from ancient testimonia and quotations; no substantial fragment survives, and its length, authorship, and precise content must be reconstructed from Pausanias, Apollodorus, the scholia, and other ancient sources.\n\nThe Seven Against Thebes / Epigoni mythological cycle was one of the most important epic cycles in ancient Greek literature — second only to the Trojan War cycle in its cultural significance — and the subject of numerous tragedies (Aeschylus's Seven Against Thebes; Sophocles's Antigone, Oedipus at Colonus; Euripides's Phoenissae and Suppliant Women) and prose summaries (Apollodorus's Library). The Epigoni's narrative focus on the sons avenging their fathers is a foundational example of the Greek motif of inherited vengeance and generational justice that also structures the Oresteia and Hamlet. The story of Alcmaeon — who killed his mother Eriphyle for accepting a bribe to send his father Amphiaraus to his death at Thebes, and was subsequently driven mad by the Erinyes — is one of the most dramatic narrative sequences of the Theban cycle.\n\nThe Epigoni epic's place in the Epic Cycle — alongside the Cypria, Little Iliad, Iliupersis, Nostoi, and Telegony — demonstrates the systematic organisation of Greek legendary material into a comprehensive narrative of the heroic age that supplemented Homer's central epics with peripheral stories, creating a total narrative framework for the generation of heroes who fought at Thebes and Troy.",
    "causes": [
      "The Theban mythological cycle — the legends of Oedipus, the Seven Against Thebes, and the Epigoni — was one of the most important narrative cycles in archaic Greek culture, reflecting the traditions of early Boeotian and Argive political and religious history, and the Epigoni epic was the final narrative chapter that resolved the Theban conflict.",
      "The archaic Greek tradition of cyclic epic composition — the systematic expansion of the Homeric narrative through supplementary epics covering related legendary material — motivated the composition of the Epigoni as the concluding epic of the Theban cycle, providing the narrative resolution (the successful sack of Thebes) that completed the arc begun in the Thebaid.",
      "The Greek literary and dramatic tradition's interest in the Theban legends — their repeated treatment by the three great tragedians — provided the cultural context for the Epigoni epic's composition and transmission: the poem was known to the tragedians and provided material for their dramatic treatments of Alcmaeon, Antigone, and the aftermath of the Theban wars."
    ],
    "effects": [
      "The Epigoni's narrative material — particularly the story of Alcmaeon killing his mother and being driven mad by the Erinyes — was the subject of several lost tragedies (Sophocles and Euripides each wrote an Alcmaeon play) and the Alcmaeon myth is an important parallel to the Orestes myth in the Greek tragic tradition.",
      "The Epic Cycle's preservation (primarily through summaries by Proclus and quotations in later authors), including the Epigoni, gave modern scholars the framework for understanding the total narrative structure of Greek heroic legend — the Epic Cycle represents a systematic organisation of the entire heroic age, and the Epigoni's place in it shows how Greek literary culture organised its narrative heritage.",
      "The Epigoni epic's loss — like the loss of most Epic Cycle poems — represents one of the most significant gaps in our knowledge of early Greek literature: the poems of the Epic Cycle were widely read in antiquity and were important sources for later poetry, art, and drama, but have survived only in fragments, testimonia, and indirect quotations."
    ],
    "relationships": [
      {"sourceSlug": "epigoni-epic", "sourceName": "Epigoni epic (sons of Seven Against Thebes)", "verb": "PART_OF", "targetSlug": "greek-epic-cycle", "targetName": "Greek Epic Cycle (supplementary epics, Trojan/Theban cycles)", "context": "The Epigoni is part of the Greek Epic Cycle — the collection of supplementary epics that filled in the narrative of the heroic age around Homer's Iliad and Odyssey — covering the successful second campaign against Thebes."},
      {"sourceSlug": "epigoni-epic", "sourceName": "Epigoni (Alcmaeon myth, matricide, Erinyes)", "verb": "PROVIDES_MATERIAL_FOR", "targetSlug": "greek-tragedy", "targetName": "Greek tragedy (Alcmaeon, Antigone, Oedipus cycle)", "context": "The Epigoni's narrative material — particularly Alcmaeon's matricide and madness — was the subject of lost tragedies by Sophocles and Euripides and parallels the Orestes myth in the tradition of inherited vengeance and generational justice."},
      {"sourceSlug": "thebaid-epic", "sourceName": "Thebaid epic (first campaign, Seven Against Thebes)", "verb": "PRECEDES", "targetSlug": "epigoni-epic", "targetName": "Epigoni (second campaign, sons' revenge)", "context": "The Thebaid (the failed first campaign) and the Epigoni (the successful second campaign) form the narrative arc of the Theban cycle — the sons avenging their fathers is the resolution of the conflict begun in the Thebaid."}
    ],
    "places": [
      {"name": "Thebes, Boeotia (subject of the epic, sack by the Epigoni)", "role": "The sack of Thebes by the Epigoni is the central event of the poem — Thebes, the great Boeotian city of Greek legend, is the setting for both the Seven Against Thebes and the Epigoni narratives"},
      {"name": "Ancient Greece (archaic period, Epic Cycle composition)", "role": "The Epigoni epic was composed in the archaic period of Greek literature — probably the 7th–6th centuries BCE — as part of the systematic Epic Cycle tradition of supplementing Homer with related legendary narratives"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Epic Cycle", "Greek Mythology", "Theban Legends", "Lost Texts", "Archaic Greece", "Heroic Age"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Epigoni epic (archaic Greek, c. 7th–6th century BCE) is a lost poem of the Greek Epic Cycle — narrating the successful second campaign against Thebes by the sons of the Seven Against Thebes. Known only from ancient testimonia, it provided narrative material for Greek tragedy (Alcmaeon, Sophocles, Euripides) and represents the concluding chapter of the Theban mythological cycle that was second only to the Trojan War cycle in ancient Greek cultural significance.",
      "significanceCategory": "regional"
    }
  }
},

"eteriani": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782eteriani.json",
  "slug": "eteriani",
  "data": {
    "summary": "Eteriani (Georgian: ეტერიანი, also known as Abesalom and Eteri or 'The Tale of Eteri') is a medieval Georgian literary work — a romantic narrative poem traditionally attributed to Moses of Khoni (Georgian: მოსე ხონელი, Mose Khoneli), composed c. 12th–13th century CE — that is considered one of the most important works of medieval Georgian literature alongside Shota Rustaveli's The Knight in the Panther's Skin. The narrative tells the love story of Abesalom, a young nobleman, and Eteri, a beautiful young woman of lower social status — a tragic love narrative in which Abesalom and Eteri's love is frustrated by social convention, a rival suitor (Murman), and ultimately by Eteri's death from a poisoned gift sent by Murman. The tale shares structural features with the European Tristan and Iseult legend (the triangular structure of two men and a woman, the potion or magic as an element of love, the tragic ending) and has been compared to both the Tristan legend and the Persian Vis and Ramin (by Fakhr ud-Din Gurgani, c. 1054), suggesting either parallel development or possible literary connections.\n\nEteriani is one of the primary texts of the Georgian literary renaissance of the 12th–13th century — a period of extraordinary cultural flourishing under Queen Tamar (r. 1184–1213) and her successors, which produced Rustaveli's The Knight in the Panther's Skin (c. 1200) and several other major literary works. Georgian literary culture of this period was cosmopolitan — drawing on Persian, Arabic, Byzantine, and indigenous Georgian traditions — and Eteriani's narrative reflects the intersection of these traditions in the sophisticated literary culture of medieval Georgia at its cultural peak.\n\nEteriani's cultural significance in Georgia has been sustained — the story of Abesalom and Eteri is one of the most beloved Georgian folk narratives and literary tales, adapted as an opera (Meliton Balanchivadze's Dariko, 1926; Zakaria Paliashvili's Abesalom da Eteri, 1919 — one of the most celebrated Georgian operas), a ballet, and multiple theatrical productions — making it one of the primary expressions of Georgian national cultural identity alongside Rustaveli.",
    "causes": [
      "The Georgian literary renaissance of the 12th–13th century — the cultural florescence under Queen Tamar and her court at Tbilisi — created the literary environment in which Eteriani was composed: the court patronage of literature, the synthesis of Persian, Byzantine, and indigenous Georgian literary traditions, and the flourishing of courtly romantic narrative.",
      "The Persian romantic narrative tradition — particularly the tradition of the tragic love story in Persian poetry (Vis and Ramin, Leili and Majnun, Layla and Majnun) — provided both literary models and thematic influences for Eteriani: the triangular love structure, the tragic ending, and the social obstacle to love echo the conventions of the Persian romantic tradition that were central to medieval Georgian courtly culture.",
      "The indigenous Georgian oral tradition of love narratives and ballads — the deep popular tradition of songs and stories about tragic love that predates the literary period — provided the folkloric substrate from which Eteriani draws, situating the literary work within a living tradition of popular romance narrative."
    ],
    "effects": [
      "Zakaria Paliashvili's opera Abesalom da Eteri (premiered 21 February 1919) — based on the Eteriani narrative — is the most celebrated Georgian opera and a central text of Georgian national cultural identity, performed at the Tbilisi Opera and Ballet Theatre as the defining work of the Georgian operatic tradition.",
      "Eteriani's status as one of the two great monuments of medieval Georgian literary culture (alongside Rustaveli's Knight in the Panther's Skin) has made the Abesalom and Eteri story one of the primary expressions of Georgian national identity — a love story that Georgians of all periods have claimed as their own.",
      "The scholarly comparison of Eteriani with the Tristan and Iseult tradition and the Persian Vis and Ramin has made it a significant data point in the literary-historical debates about the transmission of romantic narrative structures across medieval Eurasia — the question of whether the tragic love triangle is a universal narrative pattern or a historically transmitted literary motif."
    ],
    "relationships": [
      {"sourceSlug": "mose-khoneli", "sourceName": "Moses of Khoni (Mose Khoneli, 12th–13th century)", "verb": "ATTRIBUTED_TO", "targetSlug": "eteriani", "targetName": "Eteriani (Abesalom and Eteri, c. 12th–13th century)", "context": "Eteriani is traditionally attributed to Moses of Khoni — a medieval Georgian author about whom little is known — composed during the Georgian literary renaissance of the 12th–13th century."},
      {"sourceSlug": "eteriani", "sourceName": "Eteriani (Georgian romantic narrative)", "verb": "COMPARED_WITH", "targetSlug": "tristan-and-iseult", "targetName": "Tristan and Iseult (medieval European tragic love tradition)", "context": "Eteriani's triangular love structure and tragic ending parallel the Tristan and Iseult tradition — scholars debate whether this reflects parallel development or literary connections across medieval Eurasian romantic narrative."},
      {"sourceSlug": "eteriani", "sourceName": "Eteriani (Paliashvili opera, 1919)", "verb": "ADAPTED_AS", "targetSlug": "paliashvili-abesalom-da-eteri", "targetName": "Zakaria Paliashvili, Abesalom da Eteri (opera, 1919)", "context": "Paliashvili's opera Abesalom da Eteri (1919) — based on the Eteriani narrative — is the most celebrated Georgian opera and a central text of Georgian national cultural identity."}
    ],
    "places": [
      {"name": "Georgia (medieval Kartvelian kingdom, 12th–13th century)", "role": "Eteriani was composed in medieval Georgia during the literary renaissance of the 12th–13th century — the period of Queen Tamar's court and the flowering of Georgian courtly culture that also produced Rustaveli's Knight in the Panther's Skin"},
      {"name": "Tbilisi (modern Georgian national cultural centre, Paliashvili opera)", "role": "The Tbilisi Opera and Ballet Theatre is the primary venue for performances of Paliashvili's Abesalom da Eteri — the operatic adaptation of Eteriani that is the central work of Georgian national operatic culture"}
    ],
    "subjects": ["Georgian Literature", "Medieval Era", "Medieval Romance", "South Caucasus", "Georgian Culture", "Tragic Love", "12th Century", "National Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Eteriani (c. 12th–13th century CE) is one of the primary monuments of medieval Georgian literature — the tragic love story of Abesalom and Eteri, composed during Georgia's literary renaissance under Queen Tamar. Adapted as the most celebrated Georgian opera (Paliashvili, 1919) and one of the primary expressions of Georgian national identity, it occupies a place in Georgian cultural tradition comparable to Rustaveli's Knight in the Panther's Skin. Its comparison with the Tristan legend and Persian Vis and Ramin makes it a significant text in the study of medieval Eurasian romantic narrative.",
      "significanceCategory": "regional"
    }
  }
},

"aubrey-maturin-series": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783aubrey-maturin-series.json",
  "slug": "aubrey-maturin-series",
  "data": {
    "summary": "The Aubrey-Maturin series is a sequence of twenty completed novels (and one unfinished) by Patrick O'Brian (1914–2000), published by Collins and HarperCollins between 1969 (Master and Commander) and 1999 (Blue at the Mizzen), set primarily during the Napoleonic Wars era (1793–1815) and following the naval career of Captain Jack Aubrey of the Royal Navy and his friend, ship's surgeon, naturalist, and intelligence agent Stephen Maturin — widely considered the finest historical novel series in the English language and the supreme literary achievement in maritime fiction. The series follows Aubrey and Maturin across the Atlantic, Mediterranean, Pacific, and Indian Oceans — from the Battles of Cape Finisterre and Trafalgar to operations in South America, the East Indies, and the Baltic — combining the genres of the naval adventure novel (detailed, accurate ship-handling, seamanship, and battle description) with the domestic novel (the private lives, friendships, loves, and intellectual concerns of its two contrasting protagonists) and the historical novel (meticulous recreation of early 19th-century life, culture, and politics).\n\nThe Aubrey-Maturin series is notable for the depth and authenticity of its historical and nautical research — O'Brian's recreation of early 19th-century naval life draws on primary sources (ship's logs, muster books, court martial records, personal letters) and period literature (Jane Austen, the naval memoirs of Lord Cochrane) to create a world of extraordinary historical density and linguistic authenticity. The series' language is deliberately period-appropriate — characters speak and think in early 19th-century English, and the technical vocabulary of seamanship, natural history (Maturin is a natural philosopher and Catalan physician), and the varied cultures the protagonists encounter is rendered with extraordinary precision. The relationship between Aubrey and Maturin — the bluff, musical, sociable sea-captain and the melancholy, scholarly, politically complex Irish-Catalan naturalist — is one of the most complex and richly rendered male friendships in literature.\n\nThe series' critical reputation grew slowly — it was relatively unknown outside a dedicated readership for much of its publication history — but achieved wider recognition after Charlton Heston's advocacy, a TLS poll listing Master and Commander as one of the great novels of the 20th century (2003), and Peter Weir's 2003 film adaptation (Master and Commander: The Far Side of the World, starring Russell Crowe as Aubrey and Paul Bettany as Maturin).",
    "causes": [
      "Patrick O'Brian's extraordinary historical research — his mastery of primary Napoleonic-era naval sources, his reading of period literature (Jane Austen was a major influence on the series' social register), and his own experience of the sea — provided the technical and historical foundations of the series' authenticity.",
      "The tradition of the English historical novel (Walter Scott, George Eliot, Jane Austen) and the maritime adventure novel (C. S. Forester's Hornblower series, Marryat, Cooper) provided the generic models from which O'Brian developed his own distinctive synthesis: a historical novel of manners combined with the maritime adventure tradition and the intelligence thriller (Maturin's role as an Admiralty intelligence agent).",
      "O'Brian's own cosmopolitan intellectual interests — natural history, music (Aubrey and Maturin share a passion for chamber music), philosophy, and the culture of the early 19th century — drove the series' distinctive quality: its combination of intellectual depth, cultural range, and emotional realism that distinguishes it from the adventure novel genre it formally inhabits."
    ],
    "effects": [
      "The Aubrey-Maturin series elevated the historical naval novel to a new literary standard — its combination of historical authenticity, psychological depth, and linguistic richness established a new benchmark for the genre, influencing subsequent maritime historical fiction.",
      "The series' depiction of natural history — Maturin's naturalist observations, his dissections and field notes, and the exotic fauna of the Pacific and Indian Oceans — reflects the early 19th-century culture of natural philosophy in ways that have made the series a resource for historians of science and natural history.",
      "Peter Weir's film adaptation (Master and Commander: The Far Side of the World, 2003) — combining elements from several novels — brought the series to a wider audience and is regarded as one of the finest historical maritime films, demonstrating the cinematic potential of O'Brian's detailed Napoleonic naval world."
    ],
    "relationships": [
      {"sourceSlug": "patrick-obrian", "sourceName": "Patrick O'Brian (1914–2000)", "verb": "AUTHORS", "targetSlug": "aubrey-maturin-series", "targetName": "Aubrey-Maturin series (1969–1999)", "context": "O'Brian wrote the 20-novel Aubrey-Maturin series — beginning with Master and Commander (1969) — the most highly regarded historical novel series in the English language and the supreme achievement of maritime fiction."},
      {"sourceSlug": "aubrey-maturin-series", "sourceName": "Aubrey-Maturin series (Napoleonic naval fiction)", "verb": "BUILDS_ON", "targetSlug": "hornblower-series", "targetName": "C. S. Forester's Hornblower series (maritime adventure tradition)", "context": "The Aubrey-Maturin series builds on the maritime adventure tradition established by C. S. Forester's Hornblower novels, while surpassing it in historical authenticity, psychological depth, and linguistic richness."},
      {"sourceSlug": "aubrey-maturin-series", "sourceName": "Aubrey-Maturin series (Master and Commander film, 2003)", "verb": "ADAPTED_AS", "targetSlug": "master-and-commander-film-2003", "targetName": "Master and Commander: The Far Side of the World (Peter Weir, 2003)", "context": "Peter Weir's 2003 film — starring Russell Crowe and Paul Bettany — brought the Aubrey-Maturin series to a wider audience and is regarded as one of the finest historical maritime films."}
    ],
    "places": [
      {"name": "Atlantic, Mediterranean, Pacific, Indian Oceans (Napoleonic era naval campaigns)", "role": "The Aubrey-Maturin series follows Aubrey and Maturin across the world's oceans during the Napoleonic Wars — the global reach of Royal Navy operations during 1793–1815 is the geographical canvas of the series"},
      {"name": "England, Ireland, Catalonia (Aubrey and Maturin's domestic lives)", "role": "The characters' home lives — Aubrey's estate in Hampshire, Maturin's Irish and Catalan background — provide the domestic and political counterpart to the naval adventures, grounding the series in the social world of Regency England"}
    ],
    "subjects": ["English Literature", "Modern Era", "Patrick O'Brian", "Historical Fiction", "Napoleonic Wars", "Maritime Fiction", "20th Century", "Novel Series"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Aubrey-Maturin series (O'Brian, 1969–1999) is widely regarded as the finest historical novel series in the English language — the supreme literary achievement in maritime fiction. Its combination of meticulous Napoleonic-era historical authenticity, psychological depth, and extraordinary linguistic richness sets a new standard for the historical novel genre. Peter Weir's 2003 film brought the series to a wider audience. O'Brian's creation of Jack Aubrey and Stephen Maturin is one of the greatest literary partnerships in 20th-century fiction.",
      "significanceCategory": "highly-significant"
    }
  }
},

"camunian-rose": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784camunian-rose.json",
  "slug": "camunian-rose",
  "data": {
    "summary": "The Camunian rose (Italian: rosa camuna) is a geometric rock carving symbol found in the rock art of the Camonica Valley (Valle Camonica) in the province of Brescia, northern Italy — a petalled rosette or rose-like pattern consisting of a central circle surrounded by curved petals or petal-like forms, carved into the rock surfaces (masso inciso, 'engraved rocks') of the valley by the ancient Camunni people, primarily during the Iron Age (c. 1000–15 BCE, the period of Camunni culture before Roman conquest). The Camonica Valley rock art — comprising over 350,000 individual rock carvings at over 24 sites, spanning from the Mesolithic to the Iron Age — was designated a UNESCO World Heritage Site in 1979 (one of the first in Italy), recognised as the largest concentration of prehistoric rock art in Europe. The Camunian rose is the most distinctive and frequently reproduced individual motif from this vast rock art corpus.\n\nThe Camunian rose has been adopted as the official symbol of the Lombardy Region (Regione Lombardia) of Italy — appearing on the Lombardy flag and coat of arms, and used extensively as a regional identity marker — making it the most prominent modern appropriation of an ancient rock art symbol for regional political identity in Europe. The symbol's precise meaning to the ancient Camunni is unknown — it has been interpreted as a sun symbol, a flower symbol, a topographic or astronomical symbol, or a general symbol of life and fertility — but its visual distinctiveness and its association with the ancient pre-Roman inhabitants of the region have made it an emblem of Lombard regional pride.\n\nThe Camonica Valley rock art, including the Camunian rose, is studied by specialists in prehistoric art and archaeology — the corpus spans approximately 10,000 years of human occupation and includes hunting scenes, ritual scenes, maps and topographic representations, weapons, animals, and abstract symbols — making it one of the most important archives of prehistoric visual culture in Europe.",
    "causes": [
      "The ancient Camunni people's rock art tradition — their sustained practice of carving symbolic and figurative images into the glacially smoothed sandstone surfaces of the Camonica Valley over thousands of years — created the context for the Camunian rose's emergence as a distinctive symbol during the Iron Age period of Camunni culture.",
      "The Iron Age cultural context of the Camunni — their contact with Celtic, Etruscan, and Alpine cultural traditions — may have influenced the development of the rose/rosette motif, which appears in Iron Age art across Europe (the rosette is a widespread decorative and symbolic motif in Celtic, Etruscan, and Mediterranean art of the 1st millennium BCE).",
      "The Lombardy Region's search for a distinctive pre-Roman regional identity symbol — in the context of northern Italian regionalist politics and the Lega Nord's emphasis on northern Italian cultural distinctiveness — drove the adoption of the Camunian rose as the Lombardy regional symbol in the late 20th century."
    ],
    "effects": [
      "The Camunian rose's adoption as the symbol of Lombardy — appearing on the regional flag and coat of arms since 1975 — has made it one of the most widely reproduced prehistoric symbols in Europe, visible on public buildings, vehicles, and regional government documents across one of Italy's most populous and economically important regions.",
      "The UNESCO World Heritage designation of the Camonica Valley rock art (1979) brought international scholarly and public attention to the valley and its rock art, establishing it as one of the most important sites of prehistoric art in Europe and driving archaeological research and tourism.",
      "The Camunian rose's modern career as a regional symbol demonstrates the capacity of prehistoric art to be appropriated and recharged with new political and cultural meaning — its ancient origin (Iron Age, c. 1000–15 BCE) and unknown original significance make it an ideal blank screen for projecting contemporary regional identity claims."
    ],
    "relationships": [
      {"sourceSlug": "camunian-rose", "sourceName": "Camunian rose (Iron Age rock art, Camonica Valley)", "verb": "PART_OF", "targetSlug": "camonica-valley-rock-art", "targetName": "Camonica Valley rock art (UNESCO World Heritage, 350,000 carvings)", "context": "The Camunian rose is the most distinctive individual motif of the Camonica Valley rock art — the largest concentration of prehistoric rock art in Europe (350,000 carvings), designated a UNESCO World Heritage Site in 1979."},
      {"sourceSlug": "camunian-rose", "sourceName": "Camunian rose (Lombardy regional symbol)", "verb": "ADOPTED_BY", "targetSlug": "lombardy-region", "targetName": "Lombardy Region (Regione Lombardia, Italy)", "context": "The Camunian rose was adopted as the official symbol of Lombardy — appearing on the regional flag and coat of arms since 1975 — making it the most prominent modern use of a prehistoric rock art symbol for regional political identity in Europe."},
      {"sourceSlug": "camunian-rose", "sourceName": "Camunian rose (Camunni people, ancient symbol)", "verb": "CREATED_BY", "targetSlug": "camunni-people", "targetName": "Camunni people (ancient inhabitants of Camonica Valley, Iron Age)", "context": "The Camunian rose was carved by the ancient Camunni people — the pre-Roman inhabitants of the Camonica Valley in northern Italy — primarily during the Iron Age (c. 1000–15 BCE)."}
    ],
    "places": [
      {"name": "Camonica Valley (Valle Camonica), Brescia province, Lombardy, Italy", "role": "The Camonica Valley is the location of the rock art — including the Camunian rose — carved by the ancient Camunni people over thousands of years; the valley was designated a UNESCO World Heritage Site in 1979"},
      {"name": "Lombardy, Italy (regional symbol, flag and coat of arms)", "role": "The Camunian rose appears on the flag and coat of arms of the Lombardy Region — making it visible across one of Italy's most populous regions as a marker of Lombard regional cultural identity"}
    ],
    "subjects": ["Prehistoric Art", "Ancient Era", "Rock Art", "Italian History", "Camonica Valley", "Symbol History", "Regional Identity", "UNESCO World Heritage"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Camunian rose — an Iron Age rock art motif from the Camonica Valley in northern Italy — is the most distinctive symbol of the largest concentration of prehistoric rock art in Europe (350,000 carvings, UNESCO World Heritage 1979). Its adoption as the official symbol of the Lombardy Region demonstrates the capacity of prehistoric art to be recharged with modern political meaning. It is one of the most widely reproduced prehistoric symbols in Europe through its regional identity function.",
      "significanceCategory": "regional"
    }
  }
},

"physiology": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785physiology.json",
  "slug": "physiology",
  "data": {
    "summary": "Physiology (from Greek φύσις, physis, 'nature', and λόγος, logos, 'study') is the branch of biology concerned with the normal functions and mechanisms of living organisms — the study of how cells, tissues, organs, and organ systems work together to maintain life, respond to the environment, and support vital processes including metabolism, respiration, circulation, digestion, neural signalling, reproduction, and homeostasis. Physiology is both an ancient and a modern discipline — its roots extend to Hippocratic and Galenic medicine (the humoral theory of physiological function that dominated Western medicine from antiquity to the 17th century) and its modern scientific form was established in the 17th–19th centuries through the work of William Harvey (discovery of blood circulation, 1628), René Descartes (mechanical model of the body), Albrecht von Haller (irritability and sensibility of tissues, 1750s), Claude Bernard (internal environment and homeostasis, 1850s–1860s), and the development of experimental physiology as an autonomous discipline.\n\nModern physiology is subdivided into numerous specialisms: cellular and molecular physiology (the function of individual cells and their molecular mechanisms), systems physiology (the function of organ systems — cardiovascular, respiratory, renal, gastrointestinal, neurological, endocrine, reproductive), comparative physiology (comparing physiological mechanisms across different organisms), exercise physiology (the physiological responses to physical activity), and pathophysiology (the physiological mechanisms of disease). The boundaries between physiology and related disciplines — biochemistry, molecular biology, pharmacology, neuroscience, and medicine — are fluid and overlapping, reflecting physiology's position as the integrative discipline that links molecular mechanisms to whole-organism function.\n\nThe history of physiology is inseparable from the history of medicine — the understanding of how the body works in health is the foundation for understanding how it fails in disease, and physiological research has directly generated most of the major advances in clinical medicine: Harvey's circulation underpinning cardiovascular medicine, Bernard's homeostasis concept underpinning metabolic medicine and intensive care, and the discoveries of electrophysiology underpinning cardiology and neurology. The Nobel Prize in Physiology or Medicine has been awarded annually since 1901 and has recognised the most significant physiological discoveries of the 20th and 21st centuries.",
    "causes": [
      "The ancient Greek and Roman medical traditions — the Hippocratic humoral theory (health as the balance of blood, phlegm, yellow bile, and black bile) and Galen's comprehensive physiological system (which dominated Western medicine for over 1,400 years) — established physiology as a systematic inquiry into the body's functions, even if the theoretical framework was later superseded.",
      "The Scientific Revolution's transformation of natural philosophy — Descartes's mechanical model of the body, Harvey's empirical demonstration of blood circulation through quantitative measurement, and the introduction of experimental methods to biological inquiry — established the foundations of modern experimental physiology.",
      "Claude Bernard's concept of the milieu intérieur ('internal environment', 1850s–1860s) — his insight that living organisms maintain a stable internal environment (constant temperature, pH, glucose levels) through regulatory mechanisms — provided the theoretical concept of homeostasis that became the organizing principle of modern physiology."
    ],
    "effects": [
      "Physiology's direct contribution to clinical medicine — from Harvey's blood circulation (cardiovascular medicine), through Starling's heart-lung preparation (cardiac physiology), Sherrington's spinal reflexes (neurology), Banting and Best's insulin discovery (diabetes), to the development of electrophysiology (ECG, EEG, nerve conduction studies) — represents the most direct connection between basic science and medical practice in any biological discipline.",
      "The Nobel Prize in Physiology or Medicine has been awarded for discoveries that include the physiological mechanisms of nerve impulse transmission (Hodgkin and Huxley, 1963), the cellular mechanisms of signal transduction (Martin Rodbell and Alfred Gilman, 1994), the discovery of ion channels (Neher and Sakmann, 1991), and other foundational physiological discoveries that have reshaped medicine and biology.",
      "Physiology's development of the homeostasis concept — extended by Walter Cannon (who coined the term 'homeostasis', 1932) and elaborated throughout the 20th century — provided medicine with its fundamental framework for understanding physiological regulation, disease as the failure of homeostatic mechanisms, and clinical intervention as the restoration of physiological equilibrium."
    ],
    "relationships": [
      {"sourceSlug": "physiology", "sourceName": "Physiology (Harvey, blood circulation, 1628)", "verb": "FOUNDED_BY", "targetSlug": "william-harvey", "targetName": "William Harvey (1578–1657, discovery of blood circulation)", "context": "William Harvey's experimental demonstration of blood circulation (De Motu Cordis, 1628) is the founding achievement of modern physiology — replacing Galenic theory with quantitative experimental evidence."},
      {"sourceSlug": "physiology", "sourceName": "Physiology (Bernard, milieu intérieur, homeostasis)", "verb": "SHAPED_BY", "targetSlug": "claude-bernard", "targetName": "Claude Bernard (1813–1878, internal environment concept)", "context": "Claude Bernard's concept of the milieu intérieur — the stable internal environment maintained by regulatory mechanisms — provided the theoretical concept of homeostasis that became the organising principle of modern physiology."},
      {"sourceSlug": "physiology", "sourceName": "Physiology (foundation of clinical medicine)", "verb": "UNDERPINS", "targetSlug": "modern-medicine", "targetName": "Modern clinical medicine (cardiovascular, neurological, metabolic)", "context": "Physiology's discoveries — from circulation to electrophysiology to homeostasis — directly generated the most significant advances in clinical medicine, establishing physiology as the foundational science of medicine."}
    ],
    "places": [
      {"name": "Europe (Harvey, Harvey's England; Bernard, Bernard's Paris; von Haller, Switzerland)", "role": "Modern experimental physiology developed primarily in Europe — William Harvey in England (1628), Albrecht von Haller in Switzerland (1750s), Claude Bernard in Paris (1850s–1860s) — establishing the experimental tradition that became the global standard"},
      {"name": "Global (Nobel Prize in Physiology or Medicine, worldwide biomedical research)", "role": "Physiology is a global research discipline — the Nobel Prize in Physiology or Medicine (awarded annually since 1901) has recognised physiological discoveries from laboratories worldwide, reflecting the international development of the discipline"}
    ],
    "subjects": ["Biology", "Ancient Era", "Medicine", "Science", "Homeostasis", "Experimental Science", "History of Medicine", "Academic Discipline"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Physiology — the scientific study of how living organisms function — is the foundational biological discipline of clinical medicine. From Harvey's blood circulation (1628) through Claude Bernard's homeostasis concept (1850s) to the Nobel Prize-winning discoveries of electrophysiology and molecular signalling, physiology has directly generated the most significant advances in medicine. The homeostasis concept — the body's maintenance of a stable internal environment — is physiology's central theoretical contribution and the framework for understanding both health and disease.",
      "significanceCategory": "world-changing"
    }
  }
},

"pinch-analysis": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785pinch-analysis.json",
  "slug": "pinch-analysis",
  "data": {
    "summary": "Pinch analysis (also called pinch technology or process integration) is a methodology for the optimisation of energy use in industrial processes, developed primarily by Bodo Linnhoff and colleagues at the University of Manchester Institute of Science and Technology (UMIST) in the late 1970s and early 1980s, and independently by Umeda, Itoh, and Shiroko in Japan — a systematic approach to minimising energy consumption in process plants by identifying the thermodynamic constraints ('pinch points') that limit heat recovery and determining the minimum utility (heating and cooling) requirements for a process. The methodology was first formally presented in Linnhoff and Flower's landmark paper 'Synthesis of Heat Exchanger Networks' (AIChE Journal, 1978) and was developed into a comprehensive design methodology in the 'User Guide on Process Integration for the Efficient Use of Energy' (IChemE, 1982) — the founding textbook of process integration as an industrial design discipline.\n\nThe core concept of pinch analysis is the identification of the 'pinch point' — the temperature at which the hot composite curve (the aggregate heat availability of all hot streams in a process) and the cold composite curve (the aggregate heat demand of all cold streams) come closest together on a temperature-enthalpy diagram. The pinch point defines the fundamental thermodynamic constraint on heat recovery: no heat should be transferred across the pinch (from above to below), no cooling utility should be used above the pinch, and no heating utility should be used below the pinch. Violation of these 'golden rules' increases energy consumption above the thermodynamic minimum. By applying these constraints, pinch analysis enables engineers to design heat exchanger networks that approach the thermodynamic minimum energy consumption.\n\nPinch analysis was adopted by the chemical and petrochemical industries in the 1980s–1990s as the standard methodology for energy optimisation in process plants — its application to refineries, chemical plants, and integrated industrial complexes generated energy savings of 20–40% in many cases. The methodology has been extended beyond energy integration to water minimisation (water pinch), hydrogen management (hydrogen pinch), and total site analysis, making it a general framework for resource minimisation in industrial ecology.",
    "causes": [
      "The 1970s oil crisis — the OPEC oil embargo of 1973 and the dramatic increase in energy prices — created powerful industrial incentives for energy efficiency improvement in chemical and petrochemical plants, which are among the most energy-intensive industrial processes, directly motivating the development of systematic energy optimisation methodologies.",
      "The thermodynamic insight that heat recovery in process plants was limited by fundamental thermodynamic constraints that could be identified and quantified — Linnhoff's application of second-law thermodynamic analysis (exergy analysis) to process design — provided the theoretical foundation for pinch analysis: the pinch point is a thermodynamic necessity, not merely a design choice.",
      "The development of systematic process synthesis methods — the academic tradition of chemical engineering process synthesis at UMIST and other leading chemical engineering schools — provided the intellectual context and the methodological tools from which pinch analysis emerged as a systematic, algorithmic design methodology."
    ],
    "effects": [
      "Pinch analysis's adoption by the global chemical and petrochemical industries generated billions of dollars of energy savings in the 1980s–1990s — case studies showed 20–40% energy reduction in major process plants, making it one of the most economically significant methodological innovations in chemical engineering history.",
      "The extension of the pinch concept to water minimisation (Wang and Smith, 1994), hydrogen management, and total site analysis extended pinch analysis from a heat integration tool to a general resource minimisation framework — the foundation of process integration as a broader industrial ecology methodology.",
      "Pinch analysis's influence on chemical engineering education — its introduction into undergraduate and graduate chemical engineering curricula worldwide through the IChemE User Guide (1982) and subsequent textbooks — established process integration as a core competency of modern chemical engineering practice."
    ],
    "relationships": [
      {"sourceSlug": "bodo-linnhoff", "sourceName": "Bodo Linnhoff (UMIST, 1970s–1980s)", "verb": "DEVELOPS", "targetSlug": "pinch-analysis", "targetName": "Pinch analysis (process integration methodology, 1978)", "context": "Linnhoff and colleagues at UMIST developed pinch analysis — first formally presented in Linnhoff and Flower's 1978 AIChE paper — as the founding methodology of process integration and industrial energy optimisation."},
      {"sourceSlug": "pinch-analysis", "sourceName": "Pinch analysis (1973 oil crisis motivation)", "verb": "RESPONDS_TO", "targetSlug": "1973-oil-crisis", "targetName": "1973 OPEC oil crisis (energy price shock, industrial efficiency incentive)", "context": "The 1973 oil crisis — and the dramatic increase in industrial energy costs — created the industrial incentive that motivated the development of systematic energy optimisation methodologies including pinch analysis."},
      {"sourceSlug": "pinch-analysis", "sourceName": "Pinch analysis (water pinch extension, process integration)", "verb": "EXTENDED_TO", "targetSlug": "water-pinch-analysis", "targetName": "Water pinch analysis (Wang and Smith, 1994)", "context": "Pinch analysis was extended from heat integration to water minimisation (Wang and Smith, 1994) — the water pinch concept generalised the thermodynamic framework to resource minimisation in industrial ecology."}
    ],
    "places": [
      {"name": "Manchester, UK (UMIST, Linnhoff, 1978–1982)", "role": "The University of Manchester Institute of Science and Technology (UMIST) was the primary institutional home of pinch analysis development — Linnhoff and his colleagues created the methodology and the IChemE User Guide (1982) there"},
      {"name": "Global (chemical and petrochemical plants, IChemE standards)", "role": "Pinch analysis was adopted globally in the chemical and petrochemical industries in the 1980s–1990s — generating 20–40% energy savings in major process plants and becoming the international standard for heat exchanger network design"}
    ],
    "subjects": ["Chemical Engineering", "Modern Era", "Energy Optimisation", "Process Design", "Thermodynamics", "Industrial Ecology", "Methodology", "Process Integration"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Pinch analysis (Linnhoff et al., UMIST, 1978) is one of the most economically significant methodological innovations in chemical engineering history — generating billions of dollars of energy savings in global process plants through systematic thermodynamic optimisation. Developed in response to the 1973 oil crisis, it became the international standard for heat exchanger network design and was extended to water minimisation and total site analysis, establishing process integration as a core industrial ecology methodology.",
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
