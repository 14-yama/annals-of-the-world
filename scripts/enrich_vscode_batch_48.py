#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 48 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: the-gulag-archipelago, the-merchant-of-venice, the-rime-of-the-ancient-mariner,
          yoga-sutras-of-patanjali, zohar, works-and-days, the-prophet, the-pillow-book
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-48-may2026"

ENRICHMENTS = {

"the-gulag-archipelago": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-gulag-archipelago.json",
  "slug": "the-gulag-archipelago",
  "data": {
    "summary": "The Gulag Archipelago (Russian: Архипелаг ГУЛАГ, Arkhipelag GULAG) is a three-volume work of non-fiction literature and historical investigation by the Russian novelist and dissident Aleksandr Solzhenitsyn (1918–2008), written in secret in the USSR between 1958 and 1968, smuggled to the West, and first published in Paris (by YMCA Press) in 1973. The work is a monumental account of the Soviet forced-labour camp system (the GULag — Главное управление лагерей, Main Camp Administration) from 1918 to 1956, based on Solzhenitsyn's own experience as a GULag prisoner (1945–1953), the testimonies of 227 witnesses, and extensive documentary research. The title's central metaphor — the GULag as an 'archipelago' of islands scattered across the Soviet Union, a separate country superimposed on the official Soviet map — became one of the defining cultural images of the Cold War.\n\nThe Gulag Archipelago is simultaneously a work of memoir, history, legal analysis, theological reflection, and polemic — Solzhenitsyn documents the arbitrary procedures of Soviet arrest and interrogation, the conditions of transit and camp life, the forms of resistance (escape attempts, strikes, and the moral preservation of dignity), and the psychological effects of the system on prisoners and guards. The work challenges not just the GULag system but the entire ideological foundation of the Soviet state — arguing that the mass terror and the camp system were not aberrations from Lenin's vision but its direct consequences, rooted in the Leninist and Marxist conception of revolutionary violence as a historical necessity.\n\nThe publication of The Gulag Archipelago in the West in 1973 and its clandestine circulation (samizdat) in the USSR was a decisive event in the Cold War ideological struggle — it stripped the Western left of its remaining illusions about the Soviet Union, contributed to the decline of Eurocommunism, and accelerated the delegitimisation of the Soviet system that culminated in the collapse of 1991.",
    "causes": [
      "Solzhenitsyn's personal experience — his arrest (1945, for criticising Stalin in a private letter), his eight years in the GULag (including Ekibastuz special camp), and his subsequent internal exile — provided the biographical foundation for The Gulag Archipelago: he was simultaneously a victim, a witness, and an analyst of the system he described.",
      "The Soviet post-Stalin political opening (the Khrushchev Thaw, 1956–1964) — which allowed Solzhenitsyn to publish One Day in the Life of Ivan Denisovich (1962) — briefly made possible the collection of testimonies from former GULag prisoners, providing the 227 witness accounts that are the evidentiary core of the Archipelago.",
      "The clandestine samizdat (self-publishing) culture of the Soviet intelligentsia — the circulation of typewritten manuscripts that could not be officially published — enabled Solzhenitsyn to write and circulate the Archipelago in secret, while the existence of Western publishers (YMCA Press, Paris) enabled its publication abroad after the KGB discovered a copy in 1973."
    ],
    "effects": [
      "The publication of The Gulag Archipelago in the West in 1973 was a decisive moment in Cold War intellectual history — it forced the Western left to confront the full scale of Soviet mass terror and made continued fellow-travelling intellectually untenable, contributing to the crisis of Eurocommunism and the delegitimisation of Communist parties in Western Europe.",
      "In the Soviet Union, the clandestine circulation of The Gulag Archipelago — and the resulting Soviet expulsion of Solzhenitsyn (February 1974) — became a rallying point for the dissident movement, demonstrating that an individual writer could challenge the Soviet state and survive, and contributing to the moral delegitimisation of the regime that preceded its collapse.",
      "The Gulag Archipelago, together with Hannah Arendt's The Origins of Totalitarianism (1951), established the comparative framework for understanding Nazism and Stalinism as two forms of the same totalitarian political phenomenon — a framework that has shaped political philosophy, historiography, and human rights discourse since the 1970s."
    ],
    "relationships": [
      {"sourceSlug": "aleksandr-solzhenitsyn", "sourceName": "Aleksandr Solzhenitsyn (1918–2008, Russian novelist and dissident)", "verb": "AUTHORS", "targetSlug": "the-gulag-archipelago", "targetName": "The Gulag Archipelago (Arkhipelag GULAG, 3 volumes, first published Paris 1973)", "context": "Solzhenitsyn wrote The Gulag Archipelago in secret between 1958 and 1968, drawing on his eight years as a GULag prisoner and the testimonies of 227 witnesses — published in Paris in 1973 after the KGB discovered a copy."},
      {"sourceSlug": "the-gulag-archipelago", "sourceName": "Gulag Archipelago (Western left, Eurocommunism, Cold War ideology)", "verb": "DELEGITIMISES", "targetSlug": "soviet-union", "targetName": "Soviet Union and Eurocommunist left", "context": "The publication of The Gulag Archipelago in 1973 stripped the Western left of its remaining illusions about the Soviet Union, contributed to the decline of Eurocommunism, and accelerated the intellectual delegitimisation of the Soviet system."},
      {"sourceSlug": "the-gulag-archipelago", "sourceName": "Gulag Archipelago (totalitarianism — Arendt; comparative framework)", "verb": "INFLUENCES", "targetSlug": "totalitarianism-studies", "targetName": "Totalitarianism studies and Cold War political theory (Arendt, Furet, Courtois)", "context": "Alongside Arendt's Origins of Totalitarianism, the Gulag Archipelago established the comparative framework for understanding Nazism and Stalinism as two forms of totalitarianism — shaping political philosophy and human rights discourse."}
    ],
    "places": [
      {"name": "Soviet Union (GULag camps across USSR — Kazakhstan, Siberia, Arctic; Solzhenitsyn's arrest 1945)", "role": "The Gulag Archipelago documents the Soviet forced-labour camp system distributed across the USSR — Solzhenitsyn was imprisoned in camps in Kazakhstan and elsewhere from 1945–1953"},
      {"name": "Paris, France (YMCA Press, first publication December 1973)", "role": "The Gulag Archipelago was first published in Paris by YMCA Press in December 1973 — Solzhenitsyn was expelled from the Soviet Union in February 1974 as a direct consequence"}
    ],
    "subjects": ["Russian Literature", "Modern Era", "Aleksandr Solzhenitsyn", "Soviet History", "GULag", "Totalitarianism", "Cold War", "Dissident Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Gulag Archipelago (Solzhenitsyn, 1973) is the most important document of Soviet totalitarianism — a monumental investigation of the GULag camp system that stripped Western illusions about the Soviet Union, contributed to the crisis of Eurocommunism, and accelerated the intellectual delegitimisation of the Soviet state. Together with Arendt's Origins of Totalitarianism, it established the comparative framework for understanding 20th-century totalitarianism that shaped political philosophy and human rights discourse.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-merchant-of-venice": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-merchant-of-venice.json",
  "slug": "the-merchant-of-venice",
  "data": {
    "summary": "The Merchant of Venice is a comedy (with tragic elements) by William Shakespeare (1564–1616), written c. 1596–1599 and first published in quarto in 1600. It is one of Shakespeare's most performed, most studied, and most contested plays — celebrated for the brilliance of its courtroom scene and the complexity of Shylock's characterisation, and troubled by the anti-semitism embedded in its narrative structure. The play centres on two linked plots: the Belmont plot, in which Bassanio courts the wealthy Portia using money borrowed from his friend Antonio; and the Venice plot, in which Antonio borrows a sum from the Jewish moneylender Shylock, pledging a 'pound of flesh' as forfeit.\n\nThe central dramatic event is Shylock's demand — when Antonio's ships are lost and he cannot repay the loan — that the bond be enforced: the pound of flesh. The play's climax is the trial scene (Act IV, Scene 1), in which Portia disguised as the lawyer Balthasar delivers the famous 'quality of mercy' speech ('The quality of mercy is not strained, / It droppeth as the gentle rain from heaven') and defeats Shylock's legal claim through a technical argument about the bond's exact terms. Shylock is not merely defeated but ruined — forced to convert to Christianity, stripped of his wealth — in an ending that modern productions and critics find troubling in its casual endorsement of Christian triumphalism.\n\nShylock is the most debated character in Shakespeare — his famous speech ('Hath not a Jew eyes?') claims common humanity with extraordinary force, yet the play's structure uses him as the comic villain whose punishment enables the happy ending. The play's long performance history reflects changing attitudes toward Jews and anti-semitism: performed as comedy before the Holocaust, its reception was permanently altered by the Shoah, and modern productions typically present Shylock as a tragic rather than a comic figure.",
    "causes": [
      "Elizabethan anti-semitism and the public execution of Roderigo Lopez (1594) — a Portuguese Jewish physician to Queen Elizabeth I, executed on charges of plotting to poison her — created an immediate anti-semitic political context that Shakespeare exploited with the figure of Shylock, drawing on the theatrical tradition of the stage Jew (Marlowe's Barabas in The Jew of Malta).",
      "The Renaissance Italian novella tradition — Giovanni Fiorentino's Il Pecorone (1558), which contains the bond story and the disguised-lawyer plot — provided the primary source narrative for the play's plot, while the casket competition in Portia's suitors derives from the Gesta Romanorum.",
      "Shakespeare's theatrical enterprise — the need to write commercially successful plays for the Globe Theatre audience — drove the play's combination of comic and romantic elements (the Belmont plot, Portia's wit, Bassanio's romantic success) with the more disturbing elements of the Venice/Shylock plot, creating the genre-mixing that makes it difficult to classify."
    ],
    "effects": [
      "The Merchant of Venice's complex anti-semitic characterisation of Shylock has been debated for four centuries — in the 18th–19th centuries, actors including Edmund Kean (1814) and Henry Irving (1879) gave Shylock sympathetic interpretations that emphasised his humanity; the Holocaust permanently altered the play's reception, making it impossible to perform without awareness of its anti-semitic elements.",
      "Portia's 'quality of mercy' speech and the courtroom scene became one of the most cited passages in Shakespeare outside the tragedies — influencing law (mercy as a component of justice), literature (the speech's structure and imagery), and rhetoric (as a model of legal and moral argument).",
      "The play's exploration of law, contract, and equity — the tension between the letter of the law (Shylock's bond) and the spirit of equity (Portia's mercy) — made it a foundational text for discussions of legal philosophy, contributing to debates about the nature of law, contract, and justice in the Western legal tradition."
    ],
    "relationships": [
      {"sourceSlug": "william-shakespeare", "sourceName": "William Shakespeare (1564–1616, English playwright and poet)", "verb": "AUTHORS", "targetSlug": "the-merchant-of-venice", "targetName": "The Merchant of Venice (c. 1596–1599, comedy/problem play)", "context": "Shakespeare wrote The Merchant of Venice c. 1596–1599 — creating Shylock, one of the most debated characters in dramatic literature, and the 'quality of mercy' speech, one of his most famous passages."},
      {"sourceSlug": "the-merchant-of-venice", "sourceName": "Merchant of Venice (Shylock — anti-semitism, Holocaust reception change)", "verb": "REFLECTS", "targetSlug": "history-of-antisemitism", "targetName": "History of anti-semitism and post-Holocaust reception", "context": "The Merchant of Venice's anti-semitic characterisation of Shylock was received as comedy before the Holocaust — its post-Shoah reception transformed Shylock into a tragic figure and made the play a site for debates about anti-semitism in the literary canon."},
      {"sourceSlug": "the-merchant-of-venice", "sourceName": "Merchant of Venice (quality of mercy — law vs equity)", "verb": "CONTRIBUTES_TO", "targetSlug": "legal-philosophy", "targetName": "Legal philosophy and equity theory (law vs. mercy, letter vs. spirit)", "context": "The Merchant of Venice's courtroom scene — the tension between the letter of the law and Portia's appeal to equity and mercy — contributed to discussions of legal philosophy about the nature of law, contract, and the claims of mercy against strict legal enforcement."}
    ],
    "places": [
      {"name": "Venice and Belmont (fictional/historical Venice — Renaissance trade centre; ducats and merchants)", "role": "The play is set in Venice — the pre-eminent mercantile city of Renaissance Europe — and Belmont, a romantic country house; Venice's association with international trade and Jewish moneylending provides the play's economic and social context"},
      {"name": "London, England (Globe Theatre c. 1598; Roderigo Lopez execution 1594 — anti-semitic context)", "role": "The Merchant of Venice was written and first performed in London — the Lopez affair (1594) created the immediate anti-semitic political context for its composition, and it was performed at the Globe Theatre"}
    ],
    "subjects": ["English Literature", "Early Modern Era", "William Shakespeare", "Drama", "Anti-Semitism", "Legal Philosophy", "Renaissance Literature", "Elizabethan Theatre"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Merchant of Venice (Shakespeare, c. 1596–1599) is one of the most contested plays in the Western canon — its Shylock is the most debated character in drama, simultaneously a vehicle for anti-semitism and a powerful claim for common humanity. Its 'quality of mercy' speech contributed to debates about law and equity; its post-Holocaust reception permanently altered how it is performed and interpreted, making it a site for ongoing reflection on literary anti-semitism.",
      "significanceCategory": "highly-significant"
    }
  }
},

"the-rime-of-the-ancient-mariner": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-rime-of-the-ancient-mariner.json",
  "slug": "the-rime-of-the-ancient-mariner",
  "data": {
    "summary": "The Rime of the Ancient Mariner is a major poem by the English Romantic poet Samuel Taylor Coleridge (1772–1834), first published in the joint collection Lyrical Ballads (1798) — co-authored with William Wordsworth and generally taken as the founding document of English Romanticism. In its final form (revised 1817, with marginal gloss added), the poem consists of seven parts and 625 lines in ballad form, narrating the supernatural voyage of an Ancient Mariner who shoots an albatross (a bird of good omen), brings a curse upon his ship, watches his shipmates die, and is condemned to wander the world, compelled to retell his tale.\n\nThe Rime of the Ancient Mariner is a poem of sin, guilt, and penance — the shooting of the albatross is the Mariner's transgression against the natural order; the curse that follows (dead calm, the spectral ship, Death and Life-in-Death playing dice for the crew, the dead men's eyes staring) is the supernatural punishment; and the Mariner's penance is both the physical suffering on the becalmed ship and the perpetual compulsion to retell his story. The poem contains one of the most famous lines in English literature ('Water, water, every where, / Nor any drop to drink') and the moral conclusion that divine love extends to all natural creatures ('He prayeth best, who loveth best / All things both great and small'). The marginal gloss added in 1817 creates an ironic commentary on the narrative, complicating the poem's meaning.\n\nThe Rime of the Ancient Mariner is the foundational text of English Romanticism's engagement with the sublime and the supernatural — with the terrifying, transgressive power of nature and the supernatural, the psychology of guilt and obsession, and the power of storytelling itself. Its influence extended to Romantic poetry, Gothic fiction, and the broader cultural fascination with sea voyages, obsession, and the uncanny.",
    "causes": [
      "The intellectual partnership of Coleridge and Wordsworth (1797–1798) and their collaborative project of Lyrical Ballads — Coleridge's contribution was to write supernatural poems that would generate 'that willing suspension of disbelief for the moment which constitutes poetic faith' (Biographia Literaria), while Wordsworth's was to write poems about ordinary life with a supernatural colouring — provided the artistic context for the poem.",
      "Coleridge's wide reading in voyages of discovery (including accounts of Antarctic voyages), his engagement with the medieval ballad tradition (Percy's Reliques of Ancient English Poetry, 1765), and his philosophical engagement with natural philosophy and Naturphilosophie provided the literary and intellectual materials for the poem's narrative and imagery.",
      "Coleridge's personal psychological condition — his struggle with opium dependency, his sense of creative guilt and moral failure, his depression and feelings of paralysis — is frequently read as biographical background for the Mariner's sin, curse, and compulsive repetition, though the poem's meaning exceeds any purely biographical reading."
    ],
    "effects": [
      "The Rime of the Ancient Mariner, as the opening poem of Lyrical Ballads (1798), was central to the definition of English Romantic poetry — its supernatural ballad form, its engagement with guilt and the sublime, and its valorisation of the poetic imagination as a faculty that can make the supernatural credible became defining characteristics of the Romantic movement.",
      "The poem's imagery and narrative — the Ancient Mariner stopping one of three wedding guests with his glittering eye, the albatross hung around the Mariner's neck as punishment, the line 'Water, water, every where, / Nor any drop to drink' — entered the English language as cultural images and idioms: 'an albatross around one's neck' for a burden one cannot escape is now a standard English metaphor.",
      "Coleridge's poem influenced a wide range of subsequent literature — from Poe's Gothic sea narratives through Melville's Moby-Dick (the obsessive narrator, the curse of transgression) to the Romantic conception of the artist as a cursed figure compelled to create and retell."
    ],
    "relationships": [
      {"sourceSlug": "samuel-taylor-coleridge", "sourceName": "Samuel Taylor Coleridge (1772–1834, English Romantic poet)", "verb": "AUTHORS", "targetSlug": "the-rime-of-the-ancient-mariner", "targetName": "The Rime of the Ancient Mariner (1798, first in Lyrical Ballads; revised 1817)", "context": "Coleridge wrote The Rime of the Ancient Mariner for the 1798 Lyrical Ballads — the founding document of English Romanticism, co-authored with Wordsworth."},
      {"sourceSlug": "the-rime-of-the-ancient-mariner", "sourceName": "Rime of the Ancient Mariner (Lyrical Ballads, supernatural ballad, Romanticism)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "english-romanticism", "targetName": "English Romanticism (Coleridge, Wordsworth, Lyrical Ballads 1798)", "context": "The Rime of the Ancient Mariner — as the opening poem of Lyrical Ballads (1798) — was central to the definition of English Romantic poetry and its engagement with the supernatural, the sublime, and the power of the imagination."},
      {"sourceSlug": "the-rime-of-the-ancient-mariner", "sourceName": "Rime (albatross metaphor — burden; 'Water water every where' — idiom)", "verb": "CONTRIBUTES_IDIOMS_TO", "targetSlug": "english-language-culture", "targetName": "English language and cultural idiom ('albatross around one's neck')", "context": "Coleridge's poem gave the English language one of its most powerful metaphors — 'an albatross around one's neck' for an inescapable burden — and the line 'Water, water, every where, / Nor any drop to drink' became one of the most quoted lines in English poetry."}
    ],
    "places": [
      {"name": "Lake District, England (Coleridge and Wordsworth's collaboration, Lyrical Ballads composition 1797–1798)", "role": "The Rime of the Ancient Mariner was composed during Coleridge and Wordsworth's period of collaboration in the Lake District (Somerset, then Goslar) — the Lyrical Ballads (1798) was the founding document of English Romanticism"},
      {"name": "Southern Ocean / Antarctic seas (imaginary geography of the Mariner's voyage)", "role": "The Mariner's supernatural voyage is set in the Southern Ocean and Antarctic waters — Coleridge drew on accounts of actual voyages of discovery for the poem's maritime geography"}
    ],
    "subjects": ["English Literature", "Early Modern Era", "Samuel Taylor Coleridge", "Romantic Poetry", "Supernatural", "Guilt and Redemption", "Maritime Literature", "Lyrical Ballads"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Rime of the Ancient Mariner (Coleridge, 1798) is the foundational poem of English Romanticism's supernatural mode — the opening work of Lyrical Ballads, the defining text of Romantic engagement with the sublime, guilt, and the power of narrative. Its imagery gave the English language 'an albatross around one's neck' and 'Water, water, every where, / Nor any drop to drink' as cultural idioms; its influence extended from Gothic fiction through Melville to the Romantic conception of the cursed artist.",
      "significanceCategory": "world-changing"
    }
  }
},

"yoga-sutras-of-patanjali": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780yoga-sutras-of-patanjali.json",
  "slug": "yoga-sutras-of-patanjali",
  "data": {
    "summary": "The Yoga Sūtras of Patañjali (Sanskrit: योगसूत्र, Yoga Sūtra) is a foundational text of classical Indian philosophy and the primary systematic exposition of Yoga as a philosophical system, attributed to the sage Patañjali and composed c. 400 CE (with scholarly estimates ranging from c. 200 BCE to c. 400 CE). The text consists of 196 sūtras (aphoristic formulas) divided into four pādas (chapters): Samādhi Pāda (51 sūtras, on the nature and purpose of yoga and its highest stages); Sādhana Pāda (55 sūtras, on the practice of yoga — the Eight Limbs, aṣṭāṅga yoga); Vibhūti Pāda (56 sūtras, on the supernatural powers — siddhis — that arise through practice); and Kaivalya Pāda (34 sūtras, on liberation, kaivalya, and the nature of consciousness).\n\nThe Yoga Sūtras define yoga as 'citta-vṛtti-nirodha' ('the cessation of the fluctuations of consciousness') and present the path to liberation through the Eight Limbs (Aṣṭāṅga Yoga): Yama (ethical restraints — non-violence, truthfulness, non-stealing, celibacy, non-possessiveness); Niyama (observances — purity, contentment, discipline, study, surrender to the divine); Āsana (posture); Prāṇāyāma (breath control); Pratyāhāra (withdrawal of the senses); Dhāraṇā (concentration); Dhyāna (meditation); and Samādhi (the final state of absorbed concentration and liberation). This system synthesised several earlier Indian philosophical traditions — Sāṃkhya metaphysics (the duality of Puruṣa/consciousness and Prakṛti/matter), Buddhist meditation psychology, and the existing yoga tradition — into the most systematic account of the path to liberation in Hindu thought.\n\nThe Yoga Sūtras were largely unknown in the West before the 19th century but became, through Swami Vivekananda's Raja Yoga (1896) and subsequent translations, the primary textual authority for the global yoga movement — the most widely practiced physical and spiritual discipline of the early 21st century.",
    "causes": [
      "The Indian philosophical tradition's multiple prior explorations of yoga practice — the Bhagavad Gīta's account of jñāna-, bhakti-, and karma-yoga; the Buddhist meditation traditions (the jhānas, samādhi, the Buddhist analysis of mental factors); and the Sāṃkhya metaphysical framework — provided the conceptual materials that Patañjali synthesised into the systematic Eight Limbs framework.",
      "The Indian sūtra genre — the tradition of composing extremely concise aphoristic texts (sūtras, 'threads') that require oral commentary to be understood — provided the literary form of the Yoga Sūtras: the 196 sūtras are so compressed as to be nearly unintelligible without commentary, and the text's history is partly a history of competing commentarial interpretations.",
      "The specific context of classical India's philosophical debates — the competition among Buddhist, Jain, and various Hindu schools of philosophy — drove Patañjali to produce a systematic, philosophically rigorous account of yoga that could hold its own against the sophisticated Buddhist and Jain philosophical traditions."
    ],
    "effects": [
      "The Yoga Sūtras became the primary authoritative text of Yoga philosophy in the Hindu tradition — the major commentaries (Vyāsa's Bhāṣya c. 400 CE; Vācaspati Miśra's Tattvavaiśāradī c. 900 CE; the Yogatattva-Upaniṣad tradition) ensured its continued authority through the medieval period and into the modern era.",
      "Swami Vivekananda's Raja Yoga (1896) — the first major English-language presentation of the Yoga Sūtras, presented at the Parliament of World Religions (1893) and based on Vivekananda's lectures in the United States — was the primary vehicle for the Yoga Sūtras' global reception, making Patañjali's framework the philosophical backbone of the global yoga movement.",
      "The global yoga movement of the late 20th and early 21st centuries — now practiced by hundreds of millions worldwide in its primarily physical (āsana-based) form — traces its theoretical authority to the Yoga Sūtras through the lineage of Krishnamacharya, Pattabhi Jois (Ashtanga Vinyasa Yoga), Iyengar, and the various modern yoga systems, all of which claim fidelity to Patañjali's framework."
    ],
    "relationships": [
      {"sourceSlug": "patanjali", "sourceName": "Patañjali (fl. c. 400 CE, Indian sage and systematiser of yoga)", "verb": "AUTHORS", "targetSlug": "yoga-sutras-of-patanjali", "targetName": "Yoga Sūtras of Patañjali (c. 400 CE, 196 sūtras in 4 pādas)", "context": "Patañjali composed the Yoga Sūtras c. 400 CE — the primary systematic exposition of yoga philosophy, defining yoga as 'citta-vṛtti-nirodha' and presenting the Eight Limbs as the path to liberation."},
      {"sourceSlug": "yoga-sutras-of-patanjali", "sourceName": "Yoga Sūtras (Eight Limbs — aṣṭāṅga yoga — path to liberation)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "yoga-philosophy", "targetName": "Yoga philosophy and global yoga practice (Ashtanga, Iyengar, Vinyasa traditions)", "context": "The Yoga Sūtras are the primary theoretical authority for global yoga practice — the Eight Limbs framework is the basis of Ashtanga, Iyengar, and all major yoga systems worldwide."},
      {"sourceSlug": "yoga-sutras-of-patanjali", "sourceName": "Yoga Sūtras (Vivekananda, Raja Yoga, Parliament of World Religions 1893)", "verb": "TRANSMITTED_BY", "targetSlug": "swami-vivekananda", "targetName": "Swami Vivekananda (1863–1902, Hindu reformer, Parliament of World Religions)", "context": "Swami Vivekananda's Raja Yoga (1896) was the primary vehicle for the Yoga Sūtras' global reception — Vivekananda's lectures in the United States introduced Patañjali's framework to Western audiences and initiated the global yoga movement."}
    ],
    "places": [
      {"name": "Ancient India (classical period c. 400 CE — Gupta period context)", "role": "The Yoga Sūtras were composed in classical India c. 400 CE, during the Gupta period — the era of systematic Hindu philosophical compilation"},
      {"name": "United States and global (Vivekananda 1893–1896; global yoga movement — hundreds of millions of practitioners)", "role": "The Yoga Sūtras' global diffusion began with Vivekananda's American lectures (1893–1896) and the global yoga movement of the late 20th century — making them the philosophical authority for hundreds of millions of yoga practitioners worldwide"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Indian Philosophy", "Yoga", "Hindu Thought", "Patanjali", "Meditation", "Liberation Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Yoga Sūtras of Patañjali (c. 400 CE) are the primary systematic exposition of yoga philosophy and the theoretical authority for the global yoga movement — practiced by hundreds of millions worldwide. The Eight Limbs framework defined the classical Hindu path to liberation; Swami Vivekananda's Raja Yoga (1896) made Patañjali's framework the philosophical backbone of modern yoga's global diffusion.",
      "significanceCategory": "world-changing"
    }
  }
},

"zohar": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780zohar.json",
  "slug": "zohar",
  "data": {
    "summary": "The Zohar (Hebrew: זֹהַר, Zōhar, 'Splendour' or 'Radiance') is the foundational text of Kabbalah (Jewish mysticism), a mystical commentary on the Torah written primarily in Aramaic and composed c. 1280–1286 CE by the Spanish Kabbalist Moses de León (c. 1240–1305), though attributed in the text to the 2nd-century CE Tanna Shimon bar Yochai. First appearing in Spain in the 1280s, the Zohar consists of several discrete works — the main body of the Zohar (Midrash ha-Zohar), the Sifra di-Tsni'uta ('Book of Concealment'), the Idra Rabbā ('Great Assembly'), and several other sections — most presenting themselves as discourses of Shimon bar Yochai and his circle on the mystical meaning of the Torah.\n\nThe Zohar is the supreme work of Jewish mystical theology — its central subject is the nature of the divine (Ein Sof, 'Without Limit' — the infinite and unknowable Godhead) and the ten Sefirot (divine emanations or attributes through which the Ein Sof manifests and creates): Keter (Crown), Ḥokhmah (Wisdom), Binah (Understanding), Ḥesed (Loving-kindness), Gevurah (Strength/Judgment), Tiferet (Beauty), Netzach (Eternity), Hod (Splendour), Yesod (Foundation), Malkhut (Kingdom). The Zohar's theology of divine emanation provides a mystical cosmology in which the entire universe is a manifestation of the divine, Torah is the name of God, and human action (especially the observance of the commandments — mitzvot) affects the harmony of the divine Sefirot.\n\nThe Zohar was accepted by most of the Jewish world as authentic from the 14th century, achieving near-canonical status comparable to the Talmud in some communities — particularly after the expulsion from Spain (1492) and the development of the Safed Kabbalah (Luria, Cordovero, Vital) in the 16th century. Through Christian Kabbalah (Pico della Mirandola, Johannes Reuchlin) it also influenced the Renaissance esoteric tradition and, through later occultism (the Hermetic Order of the Golden Dawn), 20th-century Western esotericism.",
    "causes": [
      "The crisis of Castilian Jewish community in the late 13th century — the pressures of Christian persecution, forced disputations, and conversions, together with the need for a mystical theology that could give the commandments a cosmic significance beyond mere legal obedience — created the religious demand that Moses de León's Zohar met.",
      "The Gerona school of Kabbalah (Nachmanides, Azriel of Gerona) and the earlier Kabbalistic tradition of the Bahir and the Sefer Yetzirah provided the conceptual vocabulary (Sefirot, Ein Sof, divine emanation) that the Zohar systematised and developed into a comprehensive mystical theology.",
      "Moses de León's literary strategy — the pseudepigraphical attribution of the Zohar to the 2nd-century Tanna Shimon bar Yochai and the use of Aramaic (the language of the Babylonian Talmud) — gave the work an aura of antiquity and authority that helped it achieve canonical status, though scholars from Ḥayyim Joseph David Azulai through Gershom Scholem have established that it is a medieval composition."
    ],
    "effects": [
      "The Zohar achieved near-canonical status in medieval Jewish communities — particularly after the 1492 expulsion from Spain, when the Zohar's mystical theodicy (the exile of the Shekhinah mirroring the exile of Israel, and the promise of eschatological restoration) gave the disaster cosmic meaning — and became the primary text of the Lurianic Kabbalah, which dominated Jewish spirituality for centuries.",
      "The Safed school of Kabbalah (Isaac Luria, Moshe Cordovero, Ḥayyim Vital, c. 1550–1600) developed the Zohar's Sefirotic theology into the Lurianic system of tsimtsum (divine contraction), shevirat ha-kelim (breaking of the vessels), and tikkun (restoration) — a mystical cosmology of cosmic tragedy and redemption that profoundly shaped all subsequent forms of Jewish mysticism including Hasidism.",
      "Christian Kabbalah — Pico della Mirandola's Kabbalistic theses (1486), Johannes Reuchlin's De Arte Cabalistica (1517), and the broader Renaissance engagement with Kabbalah as a confirmation of Christian theology — diffused Zoharic ideas through European Renaissance philosophy and laid the groundwork for the Western esoteric tradition."
    ],
    "relationships": [
      {"sourceSlug": "moses-de-leon", "sourceName": "Moses de León (c. 1240–1305, Spanish Kabbalist)", "verb": "AUTHORS", "targetSlug": "zohar", "targetName": "The Zohar (Sefer ha-Zohar, c. 1280–1286, attributed to Shimon bar Yochai)", "context": "Moses de León composed the Zohar c. 1280–1286 in Castile — attributing it to the 2nd-century Tanna Shimon bar Yochai; it became the foundational text of Kabbalah and achieved near-canonical status in medieval Jewish communities."},
      {"sourceSlug": "zohar", "sourceName": "Zohar (Sefirot, Ein Sof, Lurianic Kabbalah — Safed school)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "kabbalah", "targetName": "Kabbalah and Lurianic mysticism (Safed school — Luria, Cordovero, Vital, Hasidism)", "context": "The Zohar is the foundational text of Kabbalah — the Safed school (Luria, Cordovero, Vital, c. 1550–1600) developed Zoharic theology into the Lurianic system, which dominated Jewish spirituality and shaped Hasidism."},
      {"sourceSlug": "zohar", "sourceName": "Zohar (Christian Kabbalah — Pico della Mirandola, Reuchlin, Renaissance)", "verb": "INFLUENCES", "targetSlug": "christian-kabbalah", "targetName": "Christian Kabbalah and Renaissance esotericism (Pico, Reuchlin, Golden Dawn)", "context": "Christian Kabbalah — Pico della Mirandola's Kabbalistic theses (1486) and Reuchlin's De Arte Cabalistica (1517) — diffused Zoharic ideas through Renaissance philosophy and laid the groundwork for Western esotericism."}
    ],
    "places": [
      {"name": "Castile, Spain (c. 1280s — Moses de León's composition; Guadalajara)", "role": "The Zohar was composed by Moses de León in Castile, Spain c. 1280–1286 — appearing first in Guadalajara and spreading rapidly through the Castilian Jewish community"},
      {"name": "Safed, Galilee (16th-century Lurianic Kabbalah — Luria, Cordovero, Vital)", "role": "The Safed school in Galilee (c. 1550–1600) developed Zoharic theology into the Lurianic Kabbalah — the most influential form of Jewish mysticism, shaping all subsequent Kabbalistic and Hasidic traditions"}
    ],
    "subjects": ["Jewish Literature", "Medieval Era", "Jewish Mysticism", "Kabbalah", "Sefirot", "Torah Commentary", "Moses de León", "Esoteric Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Zohar (Moses de León, c. 1280–1286) is the foundational text of Kabbalah — the supreme work of Jewish mystical theology, achieving near-canonical status in medieval Jewish communities and becoming the basis of Lurianic Kabbalah and Hasidism. Through Christian Kabbalah (Pico, Reuchlin) it influenced Renaissance philosophy and the Western esoteric tradition; its theological vocabulary (Ein Sof, Sefirot, tikkun) remains central to Jewish spirituality.",
      "significanceCategory": "world-changing"
    }
  }
},

"works-and-days": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780works-and-days.json",
  "slug": "works-and-days",
  "data": {
    "summary": "Works and Days (Greek: Ἔργα καὶ Ἡμέραι, Erga kai Hēmerai) is a didactic poem in dactylic hexameter by the ancient Greek poet Hesiod (fl. c. 700 BCE), generally dated c. 700–650 BCE and, together with the Theogony, the primary source for ancient Greek mythology and the earliest systematic account of the Greek agricultural and moral world. The poem consists of approximately 828 lines addressed to Hesiod's brother Perses, who has cheated Hesiod out of his inheritance through a corrupt legal judgment — the poem combines moral exhortation, mythological narrative, and practical agricultural instruction in a distinctive genre that has no clear precedent in earlier Greek literature.\n\nWorks and Days contains several of the most influential narrative passages in the Western mythological tradition: the myth of Prometheus and Pandora (explaining how evil and toil entered the world — Pandora opening the jar/pithos and releasing evils, with Hope alone remaining inside); the myth of the Five Ages of Man (Gold, Silver, Bronze, Heroic, and Iron ages — a moral-historical account of humanity's progressive decline from the Golden Age of Cronus through the present Iron Age of toil and injustice); and the fable of the hawk and the nightingale (one of the earliest Greek fables, illustrating the power of the mighty over the weak). The poem's agricultural calendar (the second half) provides detailed instructions for the farmer's year — when to sow, plough, harvest, prune — and preserves the earliest systematic account of Greek agricultural practice.\n\nHesiod's Works and Days established the didactic genre of Greek poetry and the concept of the agricultural year as a moral and cosmic framework — the farmer's relationship to the earth, the seasons, and the divine order of Zeus is both practical and theological. The poem's moral framework (justice, dike, as the foundation of human community; toil as the condition of mortal life) provided the earliest Greek systematic ethical thought outside of the Homeric epics.",
    "causes": [
      "Hesiod's personal situation — the inheritance dispute with his brother Perses, which forms the immediate addressee and occasion of the poem — provides the biographical context for the work: the poem's moral exhortation (justice over injustice, honest toil over dishonest gain) is addressed to a specific person in a specific situation.",
      "The oral didactic tradition of archaic Greek poetry — the tradition of wisdom literature in which the senior figure (father, elder) gives practical and moral instruction to the younger — provided the genre model for Works and Days, synthesised with the mythological tradition (Theogony, Homeric epic) to produce a distinctively Hesiodic genre.",
      "The specific conditions of archaic Boeotian agricultural society — the small-scale farming economy of Ascra (Hesiod's village in Boeotia), the vulnerability of peasants to unjust legal judgments by corrupt 'gift-eating kings', and the practical knowledge of the agricultural year — provided the social and economic context for the poem's combination of moral exhortation and agricultural instruction."
    ],
    "effects": [
      "Works and Days established the myth of the Ages of Man (Gold, Silver, Bronze, Heroic, Iron) as the primary framework for ancient and medieval accounts of historical decline from a primordial state of happiness and justice — the myth was taken up by Plato (Statesman, Republic), Virgil (Eclogues), Ovid (Metamorphoses), and through them transmitted to the entire Western tradition of mythological historiography.",
      "Pandora and her jar became one of the most widely transmitted mythological images in Western culture — from Hesiod's poem, the story passed through Virgil, Renaissance emblem books, and the iconographic tradition to become a standard reference for the origin of evil, the curiosity that cannot be restrained, and the unexpected consequences of transgression.",
      "Hesiod's Works and Days established the didactic poem as a major genre of Western literature — Virgil's Georgics (29 BCE) are explicitly modelled on it, and the tradition of the georgic (agricultural and didactic poetry) extends through Virgil to Thomson, Cowper, and the 18th-century georgic tradition."
    ],
    "relationships": [
      {"sourceSlug": "hesiod", "sourceName": "Hesiod (fl. c. 700 BCE, Boeotian Greek poet)", "verb": "AUTHORS", "targetSlug": "works-and-days", "targetName": "Works and Days (Erga kai Hēmerai, c. 700–650 BCE, 828 lines)", "context": "Hesiod composed Works and Days c. 700–650 BCE — addressing his brother Perses, the poem combines the Pandora and Ages of Man myths with practical agricultural instruction in the founding text of the didactic genre."},
      {"sourceSlug": "works-and-days", "sourceName": "Works and Days (Five Ages of Man — Gold, Silver, Bronze, Heroic, Iron)", "verb": "ESTABLISHES", "targetSlug": "ages-of-man-mythology", "targetName": "Myth of the Ages of Man (Plato, Virgil, Ovid, medieval historiography)", "context": "Hesiod's Works and Days established the myth of the Five Ages of Man as the primary ancient framework for historical decline — taken up by Plato, Virgil, Ovid, and the medieval tradition."},
      {"sourceSlug": "works-and-days", "sourceName": "Works and Days (Pandora — jar of evils; origin of toil)", "verb": "SOURCE_MYTH_FOR", "targetSlug": "pandora-myth", "targetName": "Pandora myth (Western tradition — Renaissance, modern culture)", "context": "Hesiod's Works and Days contains the primary Greek account of Pandora and her jar — transmitted through Virgil, Renaissance emblem books, and the iconographic tradition to become one of the most widely circulated mythological images in Western culture."}
    ],
    "places": [
      {"name": "Ascra, Boeotia, Greece (Hesiod's village — small-scale agricultural community, c. 700 BCE)", "role": "Hesiod composed Works and Days in Ascra, a village in Boeotia — the poem's agricultural calendar reflects the specific conditions of Boeotian farming and the specific moral world of archaic Greek peasant society"},
      {"name": "Western literary tradition (Virgil's Georgics; Ovid; medieval; Renaissance — continuous reception)", "role": "Works and Days was transmitted through the Western literary tradition via Virgil's Georgics (29 BCE) and Ovid's Metamorphoses — its myths (Pandora, Ages of Man) and its didactic genre shaped Western literature continuously from antiquity to the 18th century"}
    ],
    "subjects": ["Greek Literature", "Ancient Era", "Hesiod", "Didactic Poetry", "Greek Mythology", "Agricultural Poetry", "Mythology", "Archaic Greece"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Works and Days (Hesiod, c. 700–650 BCE) is the foundational text of the didactic poem and a primary source for ancient Greek mythology. Its myths (Pandora's jar, the Five Ages of Man) became foundational Western mythological references; its agricultural calendar preserves the earliest systematic account of Greek agricultural practice; and its influence on Virgil's Georgics established the didactic genre as a major mode of Western literature.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-prophet": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-prophet.json",
  "slug": "the-prophet",
  "data": {
    "summary": "The Prophet is a collection of 26 poetic essays (or prose poems) by the Lebanese-American poet, artist, and philosopher Kahlil Gibran (1883–1931), first published in English by Alfred A. Knopf in New York on 23 September 1923. The book presents the wisdom teachings of a prophetic figure named Almustafa ('the chosen and the beloved'), who, on the day of his departure from the city of Orphalese after twelve years, is asked by the people to speak on the great themes of human life — Love, Marriage, Children, Work, Joy and Sorrow, Houses, Clothes, Buying and Selling, Crime and Punishment, Laws, Freedom, Reason and Passion, Pain, Self-Knowledge, Teaching, Friendship, Talking, Time, Good and Evil, Prayer, Pleasure, Beauty, Religion, and Death.\n\nThe Prophet is the best-selling book ever published by Alfred A. Knopf and one of the best-selling books of the 20th century — it remained in print continuously from its first publication, was translated into over 100 languages, and sold over 100 million copies worldwide by the end of the 20th century. It achieved its greatest cultural impact during the counter-culture movement of the 1960s–1970s, when its themes of spiritual freedom, universal love, and transcendence of social convention resonated with the counter-culture's rejection of conventional religion and politics. Passages from The Prophet are regularly read at weddings, funerals, and religious ceremonies, and its aphoristic style has made it one of the most widely quoted books of the 20th century.\n\nGibran's prose style — biblical in its rhythms, Sufi in its imagery, and Transcendentalist in its philosophical temper — synthesises Arabic literary tradition (Arabic poetry, Islamic mysticism), Blake's prophetic books, Nietzsche's Zarathustra, and American Transcendentalism (Emerson, Whitman) into a distinctively accessible mystical idiom. The Prophet is the most commercially successful work of Arabic-language literature in translation and established Gibran as the third best-selling poet in history (after Shakespeare and Laozi).",
    "causes": [
      "Gibran's specific biographical and cultural position — a Maronite Christian born in the Ottoman province of Mount Lebanon, who emigrated to the United States as a child (1895), educated in both Arabic literary tradition and American art (School of the Boston Museum of Fine Arts, studies in Paris), and writing in both Arabic and English — gave him a unique synthesis of cultural resources that enabled The Prophet's distinctive style.",
      "The American Transcendentalist tradition (Emerson, Whitman) — particularly Whitman's combination of prophetic voice, cataloguing style, and celebration of the body and the democratic individual — provided a major formal and philosophical model for The Prophet's prose-poetic form and its treatment of universal themes.",
      "Gibran's long compositional process — he worked on The Prophet for over a decade (c. 1913–1923), in correspondence with and under the patronage of Mary Haskell (who funded his Paris studies and served as his English-language editor) — ensured that the book achieved the distilled, aphoristic quality that contributed to its extraordinary longevity and accessibility."
    ],
    "effects": [
      "The Prophet became the defining popular spiritual text of the 20th century counter-culture — read by millions during the 1960s–1970s as a spiritual alternative to conventional religion, its themes of love, freedom, and the transcendence of social convention resonated with the counter-culture's spiritual search and made it a cultural touchstone of the hippie generation.",
      "The Prophet's commercial success established a market for accessible Eastern-inflected spiritual literature in the English-speaking world — it was a forerunner of the popular spiritual self-help genre that expanded in the late 20th century and contributed to the mainstream acceptance of non-Western spiritual traditions in the West.",
      "The Prophet established Kahlil Gibran as the most commercially successful Arab writer in history and as a cultural symbol of the Arab diaspora's literary contribution to English-language literature — it remains the best-known work of any Arab author worldwide and a point of cultural pride for the Lebanese diaspora."
    ],
    "relationships": [
      {"sourceSlug": "kahlil-gibran", "sourceName": "Kahlil Gibran (1883–1931, Lebanese-American poet and artist)", "verb": "AUTHORS", "targetSlug": "the-prophet", "targetName": "The Prophet (1923, Alfred A. Knopf, 26 prose poems, 100+ languages)", "context": "Gibran published The Prophet in 1923 — the best-selling book ever published by Knopf, translated into over 100 languages, and one of the best-selling books of the 20th century with over 100 million copies sold."},
      {"sourceSlug": "the-prophet", "sourceName": "The Prophet (1960s counter-culture; spiritual freedom, universal love)", "verb": "SHAPED_BY", "targetSlug": "american-counter-culture", "targetName": "American counter-culture (1960s–1970s — spiritual search, hippie movement)", "context": "The Prophet achieved its greatest cultural impact during the 1960s–1970s counter-culture, resonating with the movement's rejection of conventional religion and its spiritual search for freedom and universal love."},
      {"sourceSlug": "the-prophet", "sourceName": "The Prophet (best-known Arab author — Lebanese diaspora — Arabic literature in translation)", "verb": "REPRESENTS", "targetSlug": "arab-diaspora-literature", "targetName": "Arab diaspora literature and Lebanese literary tradition", "context": "The Prophet is the most commercially successful work of Arabic-language literature in translation — Gibran is the most widely read Arab author worldwide and the book remains a cultural symbol of the Arab diaspora's literary contribution to world literature."}
    ],
    "places": [
      {"name": "New York, USA (Alfred A. Knopf, first published 23 September 1923)", "role": "The Prophet was first published in New York by Alfred A. Knopf in 1923 — remaining in print continuously, it became the best-selling book in Knopf's catalogue"},
      {"name": "Global (100+ language translations; 100 million+ copies; weddings, funerals worldwide)", "role": "The Prophet has been translated into over 100 languages and sold over 100 million copies — passages are read at weddings, funerals, and religious ceremonies worldwide, making it one of the most globally diffused literary texts of the 20th century"}
    ],
    "subjects": ["Lebanese Literature", "Modern Era", "Kahlil Gibran", "Prose Poetry", "Spiritual Literature", "Arab-American Literature", "Counter-Culture", "20th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Prophet (Gibran, 1923) is one of the best-selling books of the 20th century — translated into over 100 languages, sold over 100 million copies, and read at ceremonies worldwide. Its role as the defining popular spiritual text of the 1960s–1970s counter-culture, and its status as the most commercially successful work of Arab literature in translation, make it a work of extraordinary cultural reach.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-pillow-book": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-pillow-book.json",
  "slug": "the-pillow-book",
  "data": {
    "summary": "The Pillow Book (Japanese: 枕草子, Makura no Sōshi) is a collection of lists, observations, diary entries, and descriptive passages by the Japanese court lady Sei Shōnagon (c. 966–1025 CE), composed at the Heian imperial court c. 994–1001 CE and presented to Empress Teishi (Sadako), in whose service Sei Shōnagon was a lady-in-waiting. The Pillow Book is one of the two supreme works of Heian women's literature (alongside Murasaki Shikibu's The Tale of Genji) and is one of the most distinctive literary achievements of any era — a proto-essayistic miscellany (zuihitsu, 'following the brush') of extraordinary wit, precision, and perceptual acuity.\n\nThe Pillow Book does not follow a narrative structure but consists of three interleaved types of writing: 'list sections' (enumerating things that are elegant, things that are distressing, things that make one's heart beat faster, hateful things, rare things, embarrassing things — 'lists of things' in a tone that ranges from witty social observation to genuine emotional revelation); 'diary sections' (accounts of specific incidents at court, conversations with the Empress, encounters with court officials); and 'essay sections' (extended meditations on nature, aesthetics, the seasons, and court life). The book's opening passage — 'In spring it is the dawn that is most beautiful. As the light creeps over the hills, their outlines are dyed a faint red and wisps of purplish cloud trail over them' — is one of the most celebrated opening passages in Japanese literature.\n\nSei Shōnagon's aesthetic sensibility — her concept of mono no aware (the pathos of things), her delight in kokoro aru hito ('those who understand'), her sharp social wit and her merciless observation of those who lack elegance and taste — established a standard of aesthetic perception that influenced Japanese literature and the zuihitsu genre continuously. The Pillow Book was composed in competition with (and as a response to) Murasaki Shikibu's Genji, and the two texts together define the achievement of Heian women's literature.",
    "causes": [
      "Sei Shōnagon's position in the service of Empress Teishi — and the specific competitive court culture of the late Heian period, in which Empress Teishi's household (where Sei Shōnagon served) and Empress Shōshi's household (where Murasaki Shikibu served) were rival centres of literary cultivation — provided both the occasion and the competitive motivation for the composition of the Pillow Book.",
      "The availability of paper (specifically, 'pillow books' — blank books kept near one's writing table or sleeping area for jotting observations) — and the Heian court's cultivation of aesthetic sensibility and literary production as primary activities of the educated aristocracy — provided the material and social context for the book's composition.",
      "The zuihitsu ('following the brush') literary tradition — the proto-essayistic genre of informal personal writing that follows the writer's observations and thoughts without a fixed structure — provided the literary form that Sei Shōnagon brought to its first great expression."
    ],
    "effects": [
      "The Pillow Book established the zuihitsu ('following the brush') as a major literary genre in Japanese literature — its combination of personal observation, list-making, and essayistic reflection provided the model for subsequent Japanese miscellany literature, influencing Yoshida Kenkō's Essays in Idleness (Tsurezuregusa, c. 1330) and the tradition of Japanese personal writing to the present.",
      "Sei Shōnagon's aesthetic framework — her lists of 'things that make the heart beat faster', 'things that are distressing', 'hateful things' — created a distinctively Japanese mode of aesthetic perception, cataloguing the world through categories of emotional and aesthetic response rather than through narrative or argument.",
      "The Pillow Book and the Tale of Genji together — composed by women of the same Heian court culture, in the same decade (c. 994–1010 CE), in the kana script — established that women writers were the supreme prose stylists of Japanese literary culture, a fact that shaped the Japanese literary tradition's valorisation of women's writing."
    ],
    "relationships": [
      {"sourceSlug": "sei-shonagon", "sourceName": "Sei Shōnagon (c. 966–1025 CE, Japanese court lady and writer)", "verb": "AUTHORS", "targetSlug": "the-pillow-book", "targetName": "The Pillow Book (Makura no Sōshi, c. 994–1001 CE, zuihitsu miscellany)", "context": "Sei Shōnagon composed the Pillow Book c. 994–1001 CE in service to Empress Teishi — one of the two supreme works of Heian women's literature, alongside Murasaki Shikibu's Tale of Genji."},
      {"sourceSlug": "the-pillow-book", "sourceName": "Pillow Book (zuihitsu, list sections, essays, observations)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "zuihitsu-genre", "targetName": "Zuihitsu genre ('following the brush', Japanese miscellany literature)", "context": "The Pillow Book established the zuihitsu ('following the brush') as a major literary genre — its model of personal observation, list-making, and essayistic reflection influenced Yoshida Kenkō and the Japanese miscellany tradition."},
      {"sourceSlug": "the-pillow-book", "sourceName": "Pillow Book (Heian court — literary competition with Genji)", "verb": "COMPOSED_ALONGSIDE", "targetSlug": "the-tale-of-genji", "targetName": "The Tale of Genji (Murasaki Shikibu, c. 1000–1010 CE)", "context": "The Pillow Book and the Tale of Genji were composed by women of rival Heian court households (c. 994–1010 CE) — together they define the supreme achievement of Heian women's literature and established women writers as the pre-eminent prose stylists of Japanese literary culture."}
    ],
    "places": [
      {"name": "Heiankyō (Kyoto), Japan (Heian imperial court, c. 994–1001 CE — Empress Teishi's household)", "role": "Sei Shōnagon composed the Pillow Book at the Heian imperial court in Heiankyō (Kyoto), in the service of Empress Teishi — the rival court literary culture of the late Heian period provided both the occasion and the aesthetic framework"},
      {"name": "Japan (continuous reception — 1,000 years of commentary, Kenkō, modern manga adaptations)", "role": "The Pillow Book has been read, copied, and commented upon in Japan for over a millennium — it established the zuihitsu genre and influenced Japanese personal writing from Yoshida Kenkō to the present"}
    ],
    "subjects": ["Japanese Literature", "Medieval Era", "Sei Shōnagon", "Heian Period", "Women Writers", "Zuihitsu", "Court Culture", "Personal Essay"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Pillow Book (Sei Shōnagon, c. 994–1001 CE) is one of the two supreme works of Heian women's literature — alongside Murasaki Shikibu's Tale of Genji — and the founding text of the zuihitsu ('following the brush') genre. Its aesthetic sensibility, wit, and precision established a standard of perceptual acuity that influenced Japanese prose literature for a millennium; together with the Tale of Genji, it demonstrated that women writers were the supreme prose stylists of Japanese literary culture.",
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
