#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 43 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: wealth-of-nations, metamorphoses, meditations, panchatantra,
          one-thousand-and-one-nights, talmud, the-divine-comedy, parallel-lives
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-43-may2026"

ENRICHMENTS = {

"wealth-of-nations": {
  "filepath": "data/appwrite-export/entities/780-Class-780/78012-wealth-of-nations.json",
  "slug": "wealth-of-nations",
  "data": {
    "summary": "An Inquiry into the Nature and Causes of the Wealth of Nations is a foundational work in the history of economic thought, written by the Scottish moral philosopher Adam Smith (1723–1790) and first published in London and Edinburgh on 9 March 1776 by W. Strahan and T. Cadell. Running to five books in two volumes, it is the first systematic analysis of the causes of economic productivity and national prosperity, the mechanisms of market exchange, and the critique of the then-dominant mercantilist theory of wealth — making it the founding document of classical economics and one of the most influential works of political economy ever written.\n\nThe Wealth of Nations develops several foundational arguments: that the primary source of national wealth is productive labour (not gold, silver, or favourable trade balances, as mercantilism held); that the division of labour — the specialisation of workers in specific tasks — is the primary mechanism by which labour productivity is increased (illustrated by Smith's famous example of pin manufacture, in which ten workers specialising in different tasks can produce 48,000 pins per day, while a single unspecialised worker could produce perhaps 20); that market exchange, directed by the price mechanism (the 'invisible hand'), spontaneously allocates resources more efficiently than state direction; and that the mercantilist policy of artificial trade restrictions and monopoly privileges harms rather than promotes national wealth. Book IV contains Smith's extended critique of mercantilism and the East India Company; Book V analyses the proper functions of government (defence, justice, public works, education) and the appropriate modes of public finance.\n\nThe Wealth of Nations was composed in the context of the Scottish Enlightenment — Smith was a professor of moral philosophy at Glasgow and a friend of David Hume — and drew on Smith's earlier lectures on jurisprudence and political economy, as well as his observations from a trip to France (1764–1766) during which he met the Physiocrats (Quesnay, Turgot). The work's influence on subsequent economic thought, policy, and practice — the development of free trade doctrine, the critique of protectionism, and the theoretical foundations of classical and neoclassical economics (Ricardo, Mill, Marshall, eventually Keynes) — make it one of the most consequential intellectual contributions in the history of the social sciences.",
    "causes": [
      "The Scottish Enlightenment's tradition of empirical moral philosophy — the project of applying natural philosophy methods to the study of human society — provided the intellectual framework for Smith's approach: his desire to analyse economic behaviour as part of a comprehensive science of human nature and society, drawing on his earlier Theory of Moral Sentiments (1759) and his lectures on jurisprudence.",
      "The dominance of mercantilist economic policy in 18th-century Britain — the theory that national wealth consisted of gold and silver accumulation, best achieved through export surpluses and trade restrictions — provided the primary intellectual target against which Smith's analysis was developed: the Wealth of Nations is, in large part, a sustained critique of mercantilist doctrine.",
      "The Industrial Revolution's early stirrings in 18th-century Britain — the beginnings of factory production, the transformation of craft manufacture, and the visible productivity gains from specialisation — provided the empirical context for Smith's division of labour analysis: his pin manufacture example drew directly on observable British manufacturing practice."
    ],
    "effects": [
      "The Wealth of Nations established the intellectual foundations of classical economics — providing the theoretical framework that David Ricardo, James Mill, John Stuart Mill, and eventually Alfred Marshall built upon, culminating in the neoclassical synthesis that dominated economics through the late 19th and early 20th centuries.",
      "Smith's critique of mercantilism and his argument for free trade — that artificial trade restrictions harm rather than promote national wealth — became the intellectual foundation of the free trade movement, embodied in the repeal of the Corn Laws (1846), the Cobden-Chevalier Treaty (1860), and the broader movement towards free trade that shaped British economic policy for a century.",
      "The 'invisible hand' metaphor — Smith's argument that market exchange, directed by the price mechanism, spontaneously allocates resources more efficiently than state direction — became the foundational argument of economic liberalism and free market theory, invoked by economists from Ricardo to Hayek to Friedman in defence of market-based economic organisation."
    ],
    "relationships": [
      {"sourceSlug": "adam-smith", "sourceName": "Adam Smith (1723–1790, Scottish moral philosopher)", "verb": "AUTHORS", "targetSlug": "wealth-of-nations", "targetName": "The Wealth of Nations (London/Edinburgh, 9 March 1776)", "context": "Smith published the Wealth of Nations on 9 March 1776 — the culmination of over a decade of economic research and the founding document of classical economics."},
      {"sourceSlug": "wealth-of-nations", "sourceName": "Wealth of Nations (invisible hand, free trade critique of mercantilism)", "verb": "ESTABLISHES", "targetSlug": "classical-economics", "targetName": "Classical economics (Ricardo, Mill, Marshall)", "context": "The Wealth of Nations provided the foundational theoretical framework for classical economics — the division of labour, the price mechanism, and the critique of mercantilism that Ricardo, Mill, and Marshall built upon."},
      {"sourceSlug": "wealth-of-nations", "sourceName": "Wealth of Nations (critique of mercantilism, free trade argument)", "verb": "INFLUENCES", "targetSlug": "free-trade-movement", "targetName": "Free trade movement (Corn Laws repeal 1846, Cobden-Chevalier 1860)", "context": "Smith's argument that trade restrictions harm national wealth became the intellectual foundation of the free trade movement — embodied in the repeal of the Corn Laws and the subsequent free trade treaties of the 19th century."}
    ],
    "places": [
      {"name": "Glasgow and Edinburgh (Smith's intellectual home, Scottish Enlightenment context)", "role": "Smith was a professor of moral philosophy at Glasgow and the Wealth of Nations was published in Edinburgh and London — the Scottish Enlightenment provided the intellectual context of the work's development"},
      {"name": "France (Smith's trip 1764–1766, Physiocrats, Quesnay, Turgot)", "role": "Smith's trip to France (1764–1766), during which he met the Physiocrats (Quesnay, Turgot), significantly influenced the economic theory developed in the Wealth of Nations — the Physiocrats' analysis of the productive sector provided a framework Smith both drew on and critiqued"}
    ],
    "subjects": ["Political Economy", "Modern Era", "Adam Smith", "Scottish Enlightenment", "Classical Economics", "Free Trade", "18th Century", "Economics"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Wealth of Nations (Adam Smith, 1776) is the founding document of classical economics and one of the most influential works of political economy in history. Its analysis of the division of labour, the price mechanism, and the critique of mercantilism shaped the development of economics from Ricardo and Mill to Marshall and Keynes, and its free trade argument provided the intellectual foundation for 19th-century British economic policy. One of the most consequential intellectual contributions to the modern world.",
      "significanceCategory": "world-changing"
    }
  }
},

"metamorphoses": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780metamorphoses.json",
  "slug": "metamorphoses",
  "data": {
    "summary": "Metamorphoses (Latin: Metamorphōseōn librī, 'Books of Transformations') is an epic poem in fifteen books by the Roman poet Publius Ovidius Naso (43 BCE – c. 17/18 CE), composed c. 8 CE and published shortly before Ovid's exile to Tomis on the Black Sea in 8 CE. It is the most comprehensive collection of Greco-Roman mythology in Latin literature — a continuous narrative of approximately 250 mythological transformation stories from the beginning of the world (the creation from primordial chaos) to the deification of Julius Caesar, framing the entire history of the universe as a series of metamorphoses (physical transformations). Running to approximately 11,995 lines of hexameter verse, it is one of the most influential texts in the Western literary tradition.\n\nThe Metamorphoses is structured as a loosely chronological progression through mythological time — from the creation and the Four Ages (Golden, Silver, Bronze, Iron), through the stories of the gods and heroes (Io, Narcissus and Echo, Actaeon, Orpheus and Eurydice, Daedalus and Icarus, Perseus and Andromeda, Hercules, Medea, Midas, the Trojan War and its aftermath, Aeneas), to the historical period (Romulus, Rome, Julius Caesar) — but the chronological framework is loose and the poem is primarily organised by thematic and narrative juxtaposition. Ovid's treatment of myth is characteristically sophisticated, ironic, and psychologically acute — transforming the archaic violence of Greek mythology through a Hellenistic-Roman aesthetic of wit, pathos, and eroticism.\n\nThe poem's influence on Western art and literature from late antiquity through the Renaissance to the present is incalculable — it was among the most widely read texts in medieval European schools (alongside Virgil's Aeneid and Statius's Thebaid), a primary source for Renaissance artists (Botticelli, Titian, Michelangelo, Bernini drew directly on Ovidian myths), and a central influence on Chaucer, Shakespeare (directly cited in A Midsummer Night's Dream, The Tempest, and dozens of other plays), Dante, Milton, Spenser, and Keats. The 'Ovidian tradition' in Western literature — ironic, erotic, sophisticated, focused on transformation and ambiguity — is one of the defining strands of Western literary culture.",
    "causes": [
      "Ovid's ambition to write an epic work that would transcend the conventional Augustan epic tradition — his deliberate reframing of the mythology of Rome not as heroic founding narrative (Virgil's Aeneid model) but as an ironic, erotic, and psychologically sophisticated collection of transformation stories — provided the creative motivation for the Metamorphoses' distinctive approach.",
      "The Augustan literary programme and its court culture — the political and cultural context of Rome under Augustus, in which poets were expected to contribute to the ideological programme of Augustan renewal — provided both the opportunities and the tensions against which Ovid wrote: the Metamorphoses' ironic engagement with Augustan ideology (culminating in the deification of Julius Caesar) is both a celebration and a subtle critique.",
      "The Greek literary tradition of mythological catalogue poetry — Hesiod's Theogony, the Hellenistic mythological handbooks, Nicander's Heteroioumena ('Transformations') — provided the generic framework that Ovid transformed: the Metamorphoses is the culmination of a Greek tradition of systematic mythological collection, transformed by Ovid's Roman literary sophistication."
    ],
    "effects": [
      "The Metamorphoses became the primary source of Greco-Roman mythology in medieval Europe — read in schools alongside Virgil, it was the main channel through which mythological knowledge was transmitted and transformed in the Latin Middle Ages, and its stories (Orpheus, Narcissus, Daedalus, Midas, Pygmalion) became the common cultural currency of Western literary culture.",
      "Renaissance artists' use of Ovidian mythology — Botticelli's Birth of Venus and Primavera, Titian's mythological paintings, Bernini's Apollo and Daphne, Shakespeare's Midsummer Night's Dream — established the Metamorphoses as the primary visual and literary source for mythological subjects in European art from the 14th to the 18th centuries, making it the indispensable reference for the Western visual tradition.",
      "The 'Ovidian tradition' in Western literature — characterised by wit, irony, psychological sophistication, erotic content, and focus on transformation and ambiguity — became one of the defining literary traditions of Western culture, in contrast to the 'Virgilian tradition' of heroic epic, and the tension between these two modes shapes the history of Western literary aesthetics."
    ],
    "relationships": [
      {"sourceSlug": "ovid", "sourceName": "Ovid (43 BCE – c. 17/18 CE, Roman poet)", "verb": "AUTHORS", "targetSlug": "metamorphoses", "targetName": "Metamorphoses (c. 8 CE, 15 books, ~12,000 hexameter lines)", "context": "Ovid composed the Metamorphoses c. 8 CE — the most comprehensive collection of Greco-Roman mythology in Latin literature, running to approximately 11,995 hexameter lines across 15 books."},
      {"sourceSlug": "metamorphoses", "sourceName": "Metamorphoses (mythology, Orpheus, Narcissus, Daedalus)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "greco-roman-mythology-transmission", "targetName": "Transmission of Greco-Roman mythology in medieval Europe", "context": "The Metamorphoses was the primary source of Greco-Roman mythology in medieval European schools — the main channel through which mythological knowledge was transmitted and transformed in Latin medieval culture."},
      {"sourceSlug": "metamorphoses", "sourceName": "Metamorphoses (Renaissance mythology, Botticelli, Titian, Shakespeare)", "verb": "INFLUENCES", "targetSlug": "renaissance-art-and-literature", "targetName": "Renaissance art and literature (15th–17th century)", "context": "Renaissance artists (Botticelli, Titian, Bernini) and writers (Shakespeare, Chaucer, Spenser) drew directly on Ovidian mythology — the Metamorphoses was the primary visual and literary source for mythological subjects in European art from the 14th to the 18th centuries."}
    ],
    "places": [
      {"name": "Rome (Augustan literary court, Ovid's home until exile, c. 8 CE)", "role": "Ovid lived in Rome and composed the Metamorphoses within the Augustan literary culture — his exile in 8 CE (to Tomis on the Black Sea, by order of Augustus) interrupted the poem's publication and shaped its reception"},
      {"name": "Medieval European schools (Metamorphoses as school text alongside Virgil)", "role": "The Metamorphoses was read in medieval European schools as a primary educational text alongside Virgil — the school tradition was the primary channel through which Ovidian mythology was transmitted through the Middle Ages to the Renaissance"}
    ],
    "subjects": ["Latin Literature", "Ancient Era", "Ovid", "Roman Literature", "Mythology", "Epic Poetry", "Renaissance Influence", "Western Literary Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Metamorphoses (Ovid, c. 8 CE) is the most comprehensive collection of Greco-Roman mythology in Latin literature and one of the most influential texts in the Western literary tradition. Its role as the primary source of mythology in medieval European schools, its influence on Renaissance art (Botticelli, Titian, Bernini, Shakespeare), and the 'Ovidian tradition' of wit, irony, and transformation make it indispensable to Western art and literature across 2,000 years.",
      "significanceCategory": "world-changing"
    }
  }
},

"meditations": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780meditations.json",
  "slug": "meditations",
  "data": {
    "summary": "Meditations (Greek: Τὰ εἰς ἑαυτόν, Ta eis heauton, 'Things to Oneself') is a collection of private philosophical writings by the Roman Emperor Marcus Aurelius (121–180 CE), written during his military campaigns on the Danube frontier (c. 170–180 CE) and never intended for publication — a personal journal of Stoic philosophical reflection, self-examination, and moral instruction. Written in Greek, the Meditations are organised in twelve books (or 'books' in the manuscript tradition) of aphoristic and discursive passages, characterised by recurring Stoic themes: the importance of reason and virtue as the only true goods; the indifference of external circumstances (wealth, fame, power, physical pleasure and pain); the transience of all things and the acceptance of death; the duty to act in accordance with nature and for the common good; and the discipline of perception (phantasia), impulse (horme), and assent (synkatathesis) that constitutes Stoic philosophical practice.\n\nMarcus Aurelius was Roman Emperor from 161 to 180 CE — the last of the 'Five Good Emperors' of the Principate and one of the most effective emperors in Roman history — who spent much of his reign on campaign against the Germanic tribes (the Marcomannic Wars, 166–180 CE) and the Parthian Empire. The Meditations were written at the front, amid the pressures of military leadership and imperial administration, and their remarkable personal quality — the voice of one of the most powerful men in the world practising philosophical humility and self-discipline — has given them a unique place in the history of Stoic philosophy. They represent the most direct surviving record of the lived practice of Stoic philosophy by an individual.\n\nThe Meditations were first published in 1558 (the first printed edition, edited by Wilhelm Xylander from a medieval manuscript that has since disappeared), and have been among the most widely read works of practical philosophy in the modern world — a central text of Stoic philosophy, consistently recommended by business leaders, military commanders, athletes, and anyone engaged in the practice of self-discipline and rational self-governance.",
    "causes": [
      "The Stoic philosophical tradition — the school founded by Zeno of Citium (c. 300 BCE) and developed by Cleanthes, Chrysippus, Panaetius, and Posidonius — provided the philosophical framework of the Meditations: the Stoic analysis of virtue, reason, emotion, and the indifference of external circumstances is the theoretical context for Marcus's personal reflections.",
      "Marcus Aurelius's imperial responsibilities and the pressures of the Marcomannic Wars (166–180 CE) — the sustained military campaigns on the Danube frontier that dominated the last decade of his reign — provided the specific context for the Meditations' composition: the writings are a record of practical philosophical discipline under the pressures of military command and political responsibility.",
      "The Stoic tradition of self-examination and philosophical journaling — the practice of philosophical askēsis (spiritual exercise) including self-examination, journaling, and meditation — provided the literary form that the Meditations adopt: Marcus was following a recognised Stoic practice in writing to himself."
    ],
    "effects": [
      "The Meditations became the most widely read Stoic philosophical text in modernity — its direct, personal voice, accessible style, and practical emphasis on self-discipline made it more immediately engaging than the systematic treatises of Chrysippus or even Epictetus's Discourses, and it has been among the most consistently recommended practical philosophy books since the 16th century.",
      "The modern Stoicism revival of the late 20th and early 21st centuries — including the popularisation of Stoic philosophy through books such as Ryan Holiday's The Obstacle Is the Way (2014) and the growth of the Stoicism movement in business, sports psychology, and self-help culture — drew heavily on the Meditations as its primary accessible text, making Marcus Aurelius's private journal the entry point for millions of readers into Stoic philosophy.",
      "The Meditations' portrayal of a powerful emperor practising philosophical humility — the most powerful man in the Roman world reflecting on his own insignificance, the transience of power, and the duty to serve the common good — has made it a touchstone for reflections on the ethics of power and political leadership across cultures and centuries."
    ],
    "relationships": [
      {"sourceSlug": "marcus-aurelius", "sourceName": "Marcus Aurelius (121–180 CE, Roman Emperor, Stoic philosopher)", "verb": "AUTHORS", "targetSlug": "meditations", "targetName": "Meditations (Τὰ εἰς ἑαυτόν, c. 170–180 CE, private journal)", "context": "Marcus Aurelius wrote the Meditations during his Danube campaigns (c. 170–180 CE) — a private journal of Stoic philosophical reflection never intended for publication, discovered in the medieval manuscript tradition and first published in 1558."},
      {"sourceSlug": "meditations", "sourceName": "Meditations (Stoic philosophy, self-discipline, virtue)", "verb": "EXPRESSES", "targetSlug": "stoicism", "targetName": "Stoic philosophy (Zeno, Chrysippus, Epictetus)", "context": "The Meditations are the most accessible and widely read expression of Stoic philosophy — Marcus's personal practice of Stoic askēsis (self-discipline, virtue, acceptance of circumstances) is the primary entry point for modern readers into Stoic thought."},
      {"sourceSlug": "meditations", "sourceName": "Meditations (modern Stoicism revival, business culture)", "verb": "INFLUENCES", "targetSlug": "modern-stoicism-movement", "targetName": "Modern Stoicism movement (21st-century business and self-help culture)", "context": "The modern Stoicism revival — popularised through Ryan Holiday's books and the growth of Stoicism in business and sports psychology — drew heavily on the Meditations as its primary accessible text."}
    ],
    "places": [
      {"name": "Danube frontier (Carnuntum, Sirmium — Marcomannic Wars campaigns, c. 170–180 CE)", "role": "The Meditations were written during Marcus Aurelius's military campaigns on the Danube frontier — the 'Front' where the most powerful man in the world practiced philosophical humility amid military command"},
      {"name": "Rome (imperial administration context; first publication 1558, Wilhelm Xylander)", "role": "Marcus was Emperor of Rome (161–180 CE) and the Meditations reflect the pressures of imperial administration alongside military command — the work was first published from a medieval manuscript in 1558"}
    ],
    "subjects": ["Roman Philosophy", "Ancient Era", "Marcus Aurelius", "Stoicism", "Roman Literature", "Philosophy", "Ethics", "Self-Discipline"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Meditations (Marcus Aurelius, c. 170–180 CE) is the most widely read Stoic philosophical text in modernity and the most direct surviving record of Stoic philosophical practice by an individual. Written by the Emperor of Rome as a private journal of self-examination, its accessibility and practical emphasis on self-discipline have made it a perennial touchstone for practical philosophy — and the primary text of the 21st-century Stoicism revival.",
      "significanceCategory": "world-changing"
    }
  }
},

"panchatantra": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780panchatantra.json",
  "slug": "panchatantra",
  "data": {
    "summary": "The Panchatantra (Sanskrit: पञ्चतन्त्र, 'Five Treatises' or 'Five Strategies') is an ancient Indian collection of interrelated fables and parables, composed in Sanskrit — traditionally attributed to the Brahmin scholar Vishnu Sharma, who is said to have composed it as a means of instruction in political wisdom (nītiśāstra) for three young princes of the Deccan kingdom of Mahilaropya. The text is estimated to have been composed in its original form c. 3rd century BCE to 3rd century CE (dates are debated), though the core narrative material is likely significantly older. The Panchatantra's five books (tantras) are: Mitra-lābha ('Gaining Friends'), Suhridbheda ('Losing Friends'), Vigraha ('War and Peace'), Labdhapranāśa ('Loss of Gains'), and Aparīkṣitakārakatva ('Ill-considered Action') — each book is a framing narrative containing embedded stories, creating the characteristic 'box-within-a-box' (tandem narratives) structure that is one of the Panchatantra's major literary contributions.\n\nThe Panchatantra's influence on world literature is unparalleled among Sanskrit texts — it was translated into Pahlavi (Middle Persian) by the physician Borzōy in the 6th century CE for the Sasanian king Khosrow I, then from Pahlavi into Syriac, Arabic (as Kalila wa-Dimna, by Ibn al-Muqaffa', c. 750 CE), Hebrew, Greek, Latin, Old Spanish, and eventually into most major European languages through the medieval period, making it the most widely translated secular work in world history before the modern era. The fables of the Panchatantra — the story of the lion and the bull, the monkey and the crocodile, the crane and the fishes, the tortoise and the geese — circulated throughout the medieval world and are the ultimate sources of many fables later attributed to Aesop in European tradition.\n\nThe political wisdom tradition of the Panchatantra — its focus on nīti (political strategy and practical wisdom) rather than dharmic morality — distinguishes it from other Indian didactic texts and connects it to the tradition of the Arthashastra: the Panchatantra is, at its core, a manual of practical statecraft in the form of entertaining fables.",
    "causes": [
      "The Indian tradition of nītiśāstra (political science and practical wisdom literature) — the systematic tradition of instruction in political strategy, diplomacy, and statecraft that includes the Arthashastra and the Nitisara — provided the intellectual framework for the Panchatantra: it is a nītiśāstra text expressed in the form of entertaining fables, designed to make practical political wisdom accessible and memorable.",
      "The Indian tradition of framed narrative structure — the literary technique of a framing story containing embedded stories, which contains further embedded stories (the 'box within a box' structure) — is the characteristic literary form of the Panchatantra and was diffused to world literature through the Panchatantra's translations: the Arabian Nights' frame structure, for example, draws on this tradition.",
      "The Sasanian cultural programme of translation (6th century CE) — King Khosrow I's commission to translate Sanskrit and Greek texts into Pahlavi — was the mechanism by which the Panchatantra entered the Islamic world: Borzōy's Pahlavi translation (c. 550 CE) was the bridge through which Indian narrative wisdom entered Arabic (Kalila wa-Dimna) and eventually European literature."
    ],
    "effects": [
      "The Panchatantra's transmission through the Islamic world (as Kalila wa-Dimna) and thence to medieval Europe was one of the great channels of cultural exchange between India, the Islamic world, and Europe — the fables of the Panchatantra contributed to the European fable tradition attributed to Aesop and directly influenced the development of European fable, parable, and novelistic narrative.",
      "The Panchatantra's 'box within a box' framing structure — a narrative technique in which a framing story contains embedded stories that may themselves contain further embedded stories — was one of the most influential narrative techniques in world literature, transmitted to the Arabian Nights, Boccaccio's Decameron, Chaucer's Canterbury Tales, and the European novella tradition.",
      "The Panchatantra's global reach — translated into more than 50 languages across three millennia — established it as the most widely translated secular work in world history before the modern era, demonstrating the extraordinary power of simple fable narrative to cross linguistic and cultural boundaries."
    ],
    "relationships": [
      {"sourceSlug": "vishnu-sharma", "sourceName": "Vishnu Sharma (legendary author, Brahmin scholar)", "verb": "AUTHORS", "targetSlug": "panchatantra", "targetName": "Panchatantra (Sanskrit, c. 3rd century BCE–3rd century CE)", "context": "The Panchatantra is traditionally attributed to Vishnu Sharma, who is said to have composed it as a manual of political wisdom for three princes — though the attribution is legendary and the text's composition was likely a long process."},
      {"sourceSlug": "panchatantra", "sourceName": "Panchatantra (Pahlavi translation, Borzōy, c. 550 CE)", "verb": "TRANSMITTED_AS", "targetSlug": "kalila-and-demna", "targetName": "Kalila wa-Dimna (Ibn al-Muqaffa', Arabic, c. 750 CE)", "context": "Borzōy's Pahlavi translation for Khosrow I (c. 550 CE) was the bridge by which the Panchatantra entered the Islamic world — Ibn al-Muqaffa's Arabic translation (Kalila wa-Dimna, c. 750 CE) was the most influential transmission vehicle for the text's global diffusion."},
      {"sourceSlug": "panchatantra", "sourceName": "Panchatantra (framing structure, embedded narrative)", "verb": "INFLUENCES", "targetSlug": "world-fable-tradition", "targetName": "World fable tradition (Aesop, Arabian Nights, Boccaccio, Chaucer)", "context": "The Panchatantra's fables and its 'box within a box' framing structure directly influenced the European fable tradition (Aesop), the Arabian Nights, the Decameron, and the Canterbury Tales — it is the original source of much of the world's fable literature."}
    ],
    "places": [
      {"name": "India (Deccan, composition context; traditional attribution to Vishnu Sharma)", "role": "The Panchatantra is traditionally set in a Deccan kingdom and attributed to the Brahmin scholar Vishnu Sharma — composition c. 3rd century BCE to 3rd century CE in the Sanskrit literary tradition"},
      {"name": "Sasanian Iran (Borzōy's Pahlavi translation c. 550 CE, Khosrow I)", "role": "The Sasanian translation programme under Khosrow I (c. 550 CE) — Borzōy's Pahlavi translation of the Panchatantra — was the crucial cultural transmission event that introduced Indian fable wisdom to the Islamic and eventually European worlds"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Indian Literature", "Fable Literature", "Political Philosophy", "World Literature", "Narrative Structure", "Cultural Transmission"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Panchatantra (c. 3rd century BCE–3rd century CE) is the most widely translated secular work in world history before the modern era — translated into more than 50 languages over three millennia. Its transmission through Pahlavi (c. 550 CE) to Arabic (Kalila wa-Dimna, c. 750 CE) and thence to European languages was one of the great channels of cultural exchange between India, the Islamic world, and Europe. Its 'box within a box' framing structure influenced the Arabian Nights, the Decameron, and the Canterbury Tales.",
      "significanceCategory": "world-changing"
    }
  }
},

"one-thousand-and-one-nights": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780one-thousand-and-one-nights.json",
  "slug": "one-thousand-and-one-nights",
  "data": {
    "summary": "One Thousand and One Nights (Arabic: أَلْفُ لَيْلَةٍ وَلَيْلَةٌ, Alf Layla wa-Layla) is a medieval Arabic-language frame narrative collection of stories — assembled, compiled, and augmented over several centuries from diverse sources (Indian, Persian, Arabic, and Egyptian folklore) into a composite work that reached its approximate present form in the 14th–15th century CE (Mamluk Egypt), though the earliest Arabic manuscript fragments date from the 9th century CE and the oldest surviving complete manuscript from the 14th century. The collection is framed by the story of the Sasanian king Shahryar — who, having discovered his first wife's infidelity, resolves to marry a new virgin bride each night and execute her the following morning — and Scheherazade (Shahrazad), the vizier's daughter, who volunteers to marry the king and delays her execution by telling him a new story each night, always ending at a suspenseful moment to ensure the king keeps her alive to hear the conclusion. The frame continues for one thousand and one nights until the king, transformed by the stories, spares Scheherazade's life.\n\nThe collection contains the most famous stories of the medieval literary world — Ali Baba and the Forty Thieves, Sinbad the Sailor (seven voyages), Aladdin and the Magic Lamp, the tale of the Three Apples (often cited as the earliest detective story), and hundreds of others — stories that range from court intrigue, merchant adventures, and voyages of discovery to love stories, ghost stories, comic tales, and philosophical parables. The collection demonstrates the extraordinary diversity of the Arabic narrative tradition — drawing on Indian tale collections (the Panchatantra tradition), Sasanian Persian stories (the Hazar Afsana, 'Thousand Fictions'), and original Arabic material in a synthesis that exemplifies the cosmopolitan cultural exchange of the medieval Islamic world.\n\nThe One Thousand and One Nights was introduced to Europe by Antoine Galland's French translation (Les Mille et Une Nuits, 1704–1717) — a free and embellished translation that immediately became a literary sensation and inaugurated the European fashion for Orientalism. Several of the most famous stories (Aladdin, Ali Baba) are not found in any known Arabic manuscript and were probably added by Galland himself. The collection has subsequently shaped European literature (Byron, Goethe, Dickens, Poe, Proust, Borges, Rushdie), Hollywood cinema, and world popular culture.",
    "causes": [
      "The synthesis of Indian (Panchatantra), Sasanian Persian (Hazar Afsana), and Arabic narrative traditions in the Islamic world (8th–14th centuries CE) — the cultural exchange of the Abbasid and Mamluk eras — created the composite body of material from which the One Thousand and One Nights was compiled: the collection is a testament to the cosmopolitan literary culture of medieval Islam.",
      "The Scheherazade frame narrative — the figure of a storyteller who delays death through storytelling — provided the structural genius of the collection: by embedding all stories within the frame of Scheherazade's survival strategy, the collection models a theory of narrative as life-saving and therapeutic, giving storytelling itself a moral and existential significance.",
      "Antoine Galland's French translation (1704–1717) and its enormous European reception were the crucial transmission event — without Galland's embellished and freely adapted translation (which introduced several stories not found in Arabic manuscripts), the One Thousand and One Nights would not have become the European cultural phenomenon that shaped Romanticism, Orientalism, and world popular culture."
    ],
    "effects": [
      "Galland's French translation (1704–1717) inaugurated European Orientalism — the fascination with the Islamic world as a space of exotic, erotic, and marvellous difference — and directly influenced the literary and artistic Orientalism of the 18th and 19th centuries (Byron's Turkish Tales, Delacroix's paintings, Ingres's odalisques, Rimsky-Korsakov's Scheherazade symphony).",
      "The characters and stories of the One Thousand and One Nights — Sinbad, Aladdin, Ali Baba, Scheherazade — became among the most globally recognisable fictional figures in world culture, adapted into films, cartoons, pantomimes, and theme parks on every continent, making the collection one of the most influential sources of world popular culture.",
      "Borges's engagement with the One Thousand and One Nights — his essays on the collection (in 'Other Inquisitions') and his short stories that draw on its structure and themes — made the collection a foundational text for 20th-century metafiction and the theory of narrative: Borges saw the Nights as the definitive example of the self-referential narrative that questions the nature of storytelling itself."
    ],
    "relationships": [
      {"sourceSlug": "scheherazade", "sourceName": "Scheherazade (Shahrazad, fictional frame narrator)", "verb": "FRAMES", "targetSlug": "one-thousand-and-one-nights", "targetName": "One Thousand and One Nights (Alf Layla wa-Layla)", "context": "Scheherazade — the vizier's daughter who delays execution by telling stories for 1,001 nights — is the framing narrator of the collection and the figure whose survival strategy structures the entire work."},
      {"sourceSlug": "one-thousand-and-one-nights", "sourceName": "One Thousand and One Nights (Galland translation, European Orientalism)", "verb": "INFLUENCES", "targetSlug": "european-orientalism", "targetName": "European Orientalism (18th–19th century art, literature, culture)", "context": "Galland's 1704–1717 French translation inaugurated European Orientalism — the literary and artistic fascination with the Islamic world as exotic and marvellous — directly influencing Byron, Delacroix, Ingres, and Rimsky-Korsakov."},
      {"sourceSlug": "one-thousand-and-one-nights", "sourceName": "One Thousand and One Nights (Indian, Persian, Arabic synthesis)", "verb": "SYNTHESISES", "targetSlug": "panchatantra", "targetName": "Panchatantra and medieval Islamic narrative traditions", "context": "The One Thousand and One Nights synthesises Indian (Panchatantra), Sasanian Persian (Hazar Afsana), and original Arabic material — demonstrating the cosmopolitan cultural exchange of the medieval Islamic world."}
    ],
    "places": [
      {"name": "Mamluk Egypt (14th–15th century compilation; oldest surviving complete manuscript)", "role": "The One Thousand and One Nights reached its approximate present form in Mamluk Egypt (14th–15th century) — the oldest surviving complete manuscript is from this period, representing the compilation's culmination"},
      {"name": "France (Galland translation 1704–1717, European reception)", "role": "Antoine Galland's French translation (Les Mille et Une Nuits, 1704–1717) was the crucial transmission event for the collection's global influence — immediately a literary sensation, it inaugurated European Orientalism"}
    ],
    "subjects": ["Arabic Literature", "Medieval Era", "World Literature", "Frame Narrative", "Folklore", "Islamic Culture", "Scheherazade", "Cultural Transmission"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "One Thousand and One Nights (medieval Arabic, compiled 8th–14th centuries CE) is one of the most influential narrative collections in world history. Its characters (Sinbad, Aladdin, Ali Baba, Scheherazade) are among the most globally recognisable fictional figures, its Scheherazade frame structure influenced the theory of narrative, and Galland's French translation (1704–1717) inaugurated European Orientalism. A testament to the cosmopolitan literary culture of medieval Islam and a foundational work of world popular culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"talmud": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780talmud.json",
  "slug": "talmud",
  "data": {
    "summary": "The Talmud (Hebrew: תַּלְמוּד, 'Teaching' or 'Study') is the central text of Rabbinic Judaism — a vast compilation of Jewish oral law (halakha), legal discussion (mahloket), biblical commentary (aggadah), ethical teachings, folklore, and wisdom literature, organised as a commentary on the Mishnah (the earlier codification of Jewish oral law, redacted c. 200 CE by Rabbi Judah ha-Nasi). There are two Talmuds: the Jerusalem Talmud (Talmud Yerushalmi, compiled in Palestine c. 350–400 CE) and the Babylonian Talmud (Talmud Bavli, compiled in Babylonia c. 500–600 CE) — the Babylonian Talmud is the authoritative text of Rabbinic Judaism, studied and interpreted continuously from the 6th century to the present day. The Babylonian Talmud comprises approximately 2.7 million words across 63 tractates (masekhtot) organised into six orders (sedarim): Zeraim (agriculture), Moed (festivals), Nashim (women), Nezikin (damages), Kodashim (holy things), and Tohorot (purity).\n\nThe Talmud developed from the oral tradition of interpretation of the Hebrew Bible (Torah) — the Pharisaic tradition of 'oral Torah' that the rabbis claimed was given to Moses at Sinai alongside the written Torah. Its characteristic mode is dialectical debate: the Talmud records the discussions of rabbinical academies across multiple generations, preserving minority opinions alongside majority decisions, recording the arguments by which legal conclusions are reached rather than simply stating the conclusions, and creating a multi-layered text in which different generations of rabbis debate across centuries. The names of hundreds of rabbis — Hillel, Shammai, Akiva, Meir, Yochanan, Rava, Abaye — are recorded as they argue about legal, ethical, and theological questions, creating a unique form of canonical literature that functions as an encyclopaedia of debate.\n\nThe Talmud is not only the central legal text of Rabbinic Judaism but the primary intellectual formation of Jewish culture for over fifteen centuries — the yeshiva (rabbinical academy) tradition of Talmud study, the practice of havruta (paired textual study), and the Talmudic style of dialectical reasoning have shaped Jewish intellectual culture, and through it, Jewish contributions to European and global intellectual life.",
    "causes": [
      "The destruction of the Jerusalem Temple (70 CE) and the dispersal of the Jewish people — the crisis that ended Temple-based Judaism and made written and oral Torah study the defining practice of diaspora Jewish life — was the foundational event that necessitated the Talmud's compilation: the need to preserve and codify the oral legal tradition in the absence of the Temple created the conditions for the Talmud's development.",
      "The rabbinic project of oral Torah codification — the Mishnah's compilation by Rabbi Judah ha-Nasi (c. 200 CE) and the subsequent generations of commentary and debate that the Mishnah generated in the Babylonian and Palestinian academies — provided the direct textual occasion for the Talmud: the Talmud is organised as a commentary on the Mishnah.",
      "The flourishing of Jewish intellectual culture in Sasanian Babylonia (2nd–6th centuries CE) — the academies of Sura, Pumbedita, and Nehardea, where the Babylonian Talmud was compiled — provided the institutional context for the Talmud's compilation: the relative tolerance of Sasanian Persia toward Jewish intellectual life created the conditions for the Babylonian academies' extraordinary productivity."
    ],
    "effects": [
      "The Babylonian Talmud became the authoritative legal and intellectual text of Rabbinic Judaism — the basis for subsequent legal codes (Maimonides's Mishneh Torah, the Shulchan Aruch), rabbinic responsa, and the continuing practice of halakha — and the text that defined the character of Jewish religious life from the 6th century to the present day.",
      "The yeshiva tradition of Talmud study — the practice of havruta (paired dialectical textual study) and the yeshiva curriculum of intensive Talmudic analysis — shaped Jewish intellectual culture for fifteen centuries, training a disproportionate share of Jewish scholars, lawyers, businesspeople, and intellectuals in the dialectical reasoning and textual analysis that characterises Talmudic discourse.",
      "The Talmud's treatment in medieval Christian Europe — including the burning of Talmud manuscripts ordered by Pope Gregory IX (Paris, 1242), the disputation at Paris (1240) in which the Talmud was put on trial, and repeated anti-Talmudic censorship and persecution — made Talmud scholarship a symbol of Jewish cultural resistance to persecution and a focal point of Jewish-Christian relations."
    ],
    "relationships": [
      {"sourceSlug": "talmud", "sourceName": "Babylonian Talmud (Talmud Bavli, compiled c. 500–600 CE)", "verb": "COMMENTS_ON", "targetSlug": "mishnah", "targetName": "Mishnah (Rabbi Judah ha-Nasi, c. 200 CE)", "context": "The Talmud is organised as a commentary on the Mishnah — the earlier codification of Jewish oral law redacted by Rabbi Judah ha-Nasi c. 200 CE — with the Babylonian Talmud becoming the authoritative text of Rabbinic Judaism."},
      {"sourceSlug": "talmud", "sourceName": "Talmud (halakha, rabbinical debate, yeshiva tradition)", "verb": "FOUNDATIONAL_TEXT_OF", "targetSlug": "rabbinic-judaism", "targetName": "Rabbinic Judaism (post-Temple period, 70 CE onwards)", "context": "The Talmud is the central text of Rabbinic Judaism — the basis for halakha, the yeshiva curriculum, and the intellectual formation of Jewish culture for fifteen centuries."},
      {"sourceSlug": "talmud", "sourceName": "Talmud (dialectical reasoning, havruta study)", "verb": "SHAPES", "targetSlug": "jewish-intellectual-culture", "targetName": "Jewish intellectual tradition (15th–20th centuries)", "context": "The yeshiva tradition of Talmud study — havruta paired analysis, dialectical reasoning — shaped Jewish intellectual culture across 15 centuries, influencing the disproportionate contribution of Jews to European and global intellectual life."}
    ],
    "places": [
      {"name": "Babylonia (Sura, Pumbedita, Nehardea academies — Babylonian Talmud compilation, c. 500–600 CE)", "role": "The Babylonian Talmud was compiled in the Jewish academies of Sasanian Babylonia (Sura, Pumbedita, Nehardea) — the institutional centre of Jewish intellectual life in the post-Temple period"},
      {"name": "Palestine (Jerusalem Talmud, c. 350–400 CE; Tiberias, Caesarea academies)", "role": "The Jerusalem Talmud was compiled in the Palestinian academies (Tiberias, Caesarea) c. 350–400 CE — the less authoritative of the two Talmuds but an important witness to Palestinian rabbinic tradition"}
    ],
    "subjects": ["Jewish Literature", "Ancient Era", "Rabbinic Judaism", "Jewish Law", "Halakha", "Oral Tradition", "Religious Texts", "Intellectual History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Talmud (Babylonian Talmud, compiled c. 500–600 CE) is the central text of Rabbinic Judaism and the primary intellectual formation of Jewish culture for over fifteen centuries. Its dialectical method, the yeshiva tradition of study, and the halakhic framework it established shaped Jewish religious, intellectual, and cultural life from the 6th century to the present, making it one of the most consequential religious texts in world history.",
      "significanceCategory": "world-changing"
    }
  }
},

"the-divine-comedy": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-divine-comedy.json",
  "slug": "the-divine-comedy",
  "data": {
    "summary": "The Divine Comedy (Italian: La Divina Commedia) is an epic narrative poem by the Italian poet Dante Alighieri (1265–1321), composed c. 1308–1321 in the Florentine vernacular (Tuscan Italian) and completed in the year of Dante's death. It is divided into three canticles — Inferno (Hell), Purgatorio (Purgatory), and Paradiso (Heaven) — each of 33 cantos (plus a single introductory canto for Inferno), totalling 100 cantos and approximately 14,233 lines of terza rima (a form of interlocking triple rhyme that Dante invented or standardised for this work: ABA BCB CDC...). The poem narrates Dante's imaginary journey through the three realms of the afterlife — guided by the Roman poet Virgil through Hell and Purgatory, and by Beatrice (Dante's idealised beloved, Beatrice Portinari) through Paradise — as an allegory of the soul's journey toward God, populated by over 600 historical, mythological, and fictional characters assigned to their appropriate places in the moral universe.\n\nThe Divine Comedy's significance is impossible to overstate in the history of Italian literature and Western culture. It simultaneously established the Tuscan vernacular as a literary language capable of serious poetry (a decisive contribution to the development of the Italian language as a literary medium), created the definitive medieval synthesis of Christian theology (drawing on Aquinas and Augustine), classical philosophy and literature (Virgil, Aristotle, Cicero), and contemporary political commentary (the poem is dense with Florentine political references and Dante's personal accounts of political exile), and demonstrated the capacity of vernacular literature to achieve the sublime register previously associated exclusively with Latin. The three canticles — Inferno (the most widely read), Purgatorio (the most theologically intricate), and Paradiso (the most technically demanding) — represent respectively the moral degradation of sin, the process of purgation and repentance, and the beatific vision of God.\n\nDante's influence on subsequent European literature and art is second only to Homer and the Bible — Chaucer (Troilus and Criseyde), Boccaccio (who gave the poem the epithet 'Divina'), Petrarch, Michelangelo, Blake, Goethe, T. S. Eliot (The Waste Land directly echoes Inferno), Borges, and Beckett have all named Dante as a primary influence.",
    "causes": [
      "Dante's political exile from Florence (1302 CE) — following the defeat of the White Guelph faction by the Black Guelphs and Pope Boniface VIII — was the biographical event that gave the Divine Comedy its urgency and its political density: the poem was written in exile, and its political judgements (including the placement of contemporary political and religious figures in Hell) reflect Dante's bitterness at his banishment.",
      "The synthesis of Aristotelian philosophy and Christian theology achieved by Thomas Aquinas (1225–1274) — the Scholastic synthesis of classical reason and Christian faith — provided the theological and philosophical framework of the Divine Comedy: Dante's universe is organised by Aquinas's synthesis, and Aquinas himself appears in Paradiso.",
      "The troubadour tradition of courtly love poetry (dolce stil novo) — the Florentine vernacular love poetry tradition in which Dante was a participant before the Comedy — provided the literary tradition from which the Comedy departed: Beatrice, as the idealised beloved who becomes a guide to divine love, is the transformation of the troubadour's donna (lady) into a theological symbol."
    ],
    "effects": [
      "The Divine Comedy's use of the Tuscan vernacular for serious literary expression was a decisive contribution to the development of Italian as a literary language — Dante's choice of vernacular over Latin, and the extraordinary prestige of the Comedy in subsequent Italian literary culture, established Tuscan Italian as the standard literary Italian, shaping the development of the Italian language.",
      "The Divine Comedy's influence on Western art and literature — Botticelli's Dante illustrations, Michelangelo's Last Judgement (deeply Dantean), Blake's illustrations, Rodin's Gates of Hell (based on Inferno), T. S. Eliot's The Waste Land, Primo Levi's Survival in Auschwitz (which draws extensively on Inferno) — demonstrates its role as the defining work of Italian literature and one of the three or four most influential works in the Western literary tradition.",
      "The Comedy's mapping of the afterlife — the specific topography of Hell (funnel-shaped, nine circles), Purgatory (mountain island, seven terraces), and Heaven (nine concentric spheres) — created the most detailed and influential imaginative geography of the Christian afterlife in Western culture, shaping popular conceptions of Heaven and Hell for seven centuries."
    ],
    "relationships": [
      {"sourceSlug": "dante-alighieri", "sourceName": "Dante Alighieri (1265–1321, Florentine poet)", "verb": "AUTHORS", "targetSlug": "the-divine-comedy", "targetName": "The Divine Comedy (La Divina Commedia, c. 1308–1321)", "context": "Dante composed the Divine Comedy c. 1308–1321 in exile from Florence — a 14,233-line vernacular epic in three canticles (Inferno, Purgatorio, Paradiso) that established Tuscan Italian as a literary language."},
      {"sourceSlug": "the-divine-comedy", "sourceName": "Divine Comedy (Dante's journey, Virgil guide)", "verb": "FEATURES", "targetSlug": "virgil", "targetName": "Virgil (70–19 BCE, Roman poet, Aeneid author)", "context": "Virgil — the author of the Aeneid — guides Dante through Hell and Purgatory in the Divine Comedy, representing the limits of classical reason (Virgil cannot enter Paradise) and embodying the synthesis of classical and Christian culture."},
      {"sourceSlug": "the-divine-comedy", "sourceName": "Divine Comedy (Tuscan vernacular, Italian language)", "verb": "ESTABLISHES", "targetSlug": "italian-literary-language", "targetName": "Italian literary language (Tuscan vernacular as standard)", "context": "Dante's choice to write the Comedy in the Tuscan vernacular, and the extraordinary prestige of the Comedy, was decisive in establishing Tuscan Italian as the standard literary Italian — a foundational contribution to the development of the Italian language."}
    ],
    "places": [
      {"name": "Florence and the Florentine exile (Dante's political context, 1302–1321)", "role": "Dante was exiled from Florence in 1302 — the Comedy was written in exile, and its political density (placing contemporary Florentines and popes in Hell) reflects Dante's bitterness at banishment"},
      {"name": "Ravenna (Dante's death, 1321; tomb; completion of Paradiso)", "role": "Dante died in Ravenna in 1321, having completed Paradiso — his tomb in Ravenna is a major site of Italian cultural memory, and Florence eventually erected a cenotaph for the poet it had exiled"}
    ],
    "subjects": ["Italian Literature", "Medieval Era", "Dante Alighieri", "Epic Poetry", "Christian Theology", "Medieval Literature", "Italian Language", "Western Canon"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Divine Comedy (Dante Alighieri, c. 1308–1321) is the supreme work of Italian literature and one of the three or four most influential works in the Western literary tradition. Its establishment of Tuscan vernacular as a literary language shaped the development of the Italian language; its synthesis of classical philosophy and Christian theology created the definitive medieval worldview; and its influence on Western art (Botticelli, Michelangelo, Blake, Rodin) and literature (Chaucer, T. S. Eliot, Borges, Primo Levi) spans seven centuries.",
      "significanceCategory": "world-changing"
    }
  }
},

"parallel-lives": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780parallel-lives.json",
  "slug": "parallel-lives",
  "data": {
    "summary": "Parallel Lives (Greek: Βίοι Παράλληλοι, Bioi Parallēloi) is a series of paired biographical essays by the Greek historian and philosopher Plutarch of Chaeronea (c. 46 – c. 120 CE), comparing a Greek statesman or military figure with a Roman counterpart — e.g. Alexander the Great with Julius Caesar, Demosthenes with Cicero, Themistocles with Camillus, Pericles with Fabius Maximus — and drawing moral conclusions from the comparison. Of the original 50 lives, 48 survive (23 pairs and 4 unpaired), covering figures from the legendary founders of Rome and Athens (Romulus, Theseus) through the period of the Late Republic (Caesar, Pompey, Cicero, Antony, Brutus). The Parallel Lives are the largest surviving collection of ancient biography and one of the most important historical sources for the classical world.\n\nPlutarch's purpose in the Parallel Lives is explicitly moral and philosophical — he states in the introduction to the life of Alexander that he is writing biography, not history, and that his concern is with character (ethos) rather than with military or political events in detail. Each pair of lives is followed by a brief 'syncrisis' (comparison) in which Plutarch explicitly evaluates the moral qualities of the two figures and makes a comparative judgement. This moral-biographical approach — history as a source of exemplary figures from whom ethical lessons can be drawn — made the Parallel Lives enormously influential in subsequent European moral education and political thought, from Renaissance humanism through the 18th century.\n\nThe Parallel Lives' influence on Western literature and history is extraordinary: they were the primary source for Shakespeare's Roman plays (Julius Caesar, Antony and Cleopatra, Coriolanus, Timon of Athens — all drawn from the Lives via North's English translation of Amyot's French, 1579), for the American Founders' political thought (Hamilton, Adams, and Jefferson all read Plutarch extensively), for Montaigne's Essays, and for the French Revolutionaries' self-fashioning as Plutarchan heroes (Robespierre and Saint-Just both modelled themselves on Roman figures in Plutarch).",
    "causes": [
      "Plutarch's philosophical formation in the Platonic and Aristotelian traditions — his education at Athens and his lifelong commitment to moral philosophy — provided the intellectual framework for the Parallel Lives: his biographical practice is driven by the Platonic-Aristotelian concern with character (ethos) as the subject of moral philosophy, not the modern historian's concern with events and causes.",
      "The Greco-Roman cultural world of the Principate — the period under the Roman Empire in which educated Greeks like Plutarch occupied a bilingual and bicultural position, at once Roman subjects and proud inheritors of Greek cultural superiority — provided the comparative framework for the Parallel Lives: pairing Greek and Roman figures was a way of asserting the equivalence of Greek and Roman cultural achievement.",
      "The death of the Roman Republic and the transformation of Rome under the Principate — which Plutarch's Late Republican subjects (Caesar, Pompey, Cicero, Brutus, Antony) had either participated in or resisted — gave the political lives their particular moral gravity: the Republican values of liberty and civic virtue that the Plutarchan heroes embodied were precisely what had been lost under the emperors."
    ],
    "effects": [
      "Plutarch's Parallel Lives became the primary source for Shakespeare's Roman plays — Julius Caesar, Antony and Cleopatra, Coriolanus, and Timon of Athens were all drawn directly from the Lives via Thomas North's 1579 English translation of Jacques Amyot's French — making Plutarch's moral biographies the source of some of the most influential dramatic works in the English language.",
      "The American Founding Fathers' deep engagement with the Parallel Lives — Hamilton, Adams, Jefferson, and Madison all read Plutarch extensively — made Plutarchan civic virtue and Republican self-sacrifice central to the American political imaginary: the Founders modelled their political rhetoric and their understanding of republican government on Plutarch's exemplary lives.",
      "The French Revolutionaries' self-fashioning as Plutarchan heroes — Robespierre modelling himself on the incorruptible Spartan lawgiver, Saint-Just on Lycurgus and Cato — demonstrates the direct political agency of the Parallel Lives: Plutarch's biographies provided the rhetorical framework through which the Revolutionaries understood and presented their own actions."
    ],
    "relationships": [
      {"sourceSlug": "plutarch", "sourceName": "Plutarch of Chaeronea (c. 46 – c. 120 CE)", "verb": "AUTHORS", "targetSlug": "parallel-lives", "targetName": "Parallel Lives (Bioi Parallēloi, c. 75–125 CE, 48 surviving lives)", "context": "Plutarch composed the Parallel Lives c. 75–125 CE — 23 pairs of Greek and Roman biographies compared for moral instruction, the largest surviving collection of ancient biography."},
      {"sourceSlug": "parallel-lives", "sourceName": "Parallel Lives (Shakespeare's Roman plays source)", "verb": "PRIMARY_SOURCE_FOR", "targetSlug": "shakespeare-roman-plays", "targetName": "Shakespeare's Roman plays (Julius Caesar, Antony and Cleopatra, Coriolanus)", "context": "Shakespeare's Roman plays were drawn directly from the Lives via North's 1579 English translation of Amyot's French — Plutarch's moral biographies are the source of the dramatic characters and events in Julius Caesar, Antony and Cleopatra, and Coriolanus."},
      {"sourceSlug": "parallel-lives", "sourceName": "Parallel Lives (American Founders, Republican virtue)", "verb": "INFLUENCES", "targetSlug": "american-founding-political-thought", "targetName": "American Founding political thought (Hamilton, Adams, Jefferson)", "context": "The American Founding Fathers — Hamilton, Adams, Jefferson, Madison — read Plutarch extensively, making Plutarchan civic virtue and Republican self-sacrifice central to the American political imaginary and the rhetoric of the new Republic."}
    ],
    "places": [
      {"name": "Chaeronea, Boeotia, Greece (Plutarch's home; Roman Empire context)", "role": "Plutarch was born and lived in Chaeronea, Boeotia — a small Greek town that had seen the decisive battle of 338 BCE when Philip of Macedon ended Greek political independence — giving his writing about Republican virtue a particular historical poignancy"},
      {"name": "Rome and Athens (Parallel Lives' subject cities; bilateral cultural world)", "role": "Plutarch's paired lives systematically compare Greek figures (Athens, Sparta, Thebes) with Roman figures — the Parallel Lives are a product of the Greco-Roman bilingual world of the Principate in which Greek intellectual life existed within Roman political power"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Plutarch", "Biography", "Roman History", "Greek History", "Moral Philosophy", "Classical Antiquity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Parallel Lives (Plutarch, c. 75–125 CE) is the largest surviving collection of ancient biography and one of the most consequential texts in Western cultural history. As the primary source for Shakespeare's Roman plays (Julius Caesar, Antony and Cleopatra, Coriolanus), a central influence on the American Founding Fathers' political thought, and the model for the French Revolutionaries' self-fashioning as Republican heroes, Plutarch's moral biographies have shaped Western political culture and literature across two millennia.",
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
