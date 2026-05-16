#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 22 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: analects, arthashastra, ab-urbe-condita-livy, act-of-abjuration,
          communist-manifesto, capital-a-critique-of-political-economy,
          de-re-publica-cicero, declaration-of-sentiments-1848
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-22-may2026"

ENRICHMENTS = {

"analects": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780analects.json",
  "slug": "analects",
  "data": {
    "summary": "The Analects (Chinese: 論語, Lúnyǔ, 'Discussions and Sayings') is the foundational text of Confucianism — a collection of sayings, conversations, and anecdotes attributed to the philosopher Kong Qiu (Confucius, 孔子, 551–479 BCE) and his disciples, compiled by their students over several generations after Confucius's death. Not a systematic philosophical treatise but a collection of short, often gnomic exchanges, the Analects records Confucius's teachings on ritual propriety (lǐ 禮), humaneness (rén 仁), filial piety, loyalty, the cultivation of virtue (dé 德), and the relationship between the ideal ruler and the exemplary person (jūnzǐ 君子) — the ethical and political framework that became the official philosophy of the Chinese imperial state and the dominant intellectual tradition of East Asia for over two millennia.\n\nConfucius taught in the turbulent Spring and Autumn period (771–476 BCE), when the Zhou dynasty was fragmenting and the traditional ritual order collapsing. His central response was that the moral and social order could be restored through the careful cultivation of virtue — beginning with the self, extending through the family, and ultimately governing the state — and through the meticulous performance of traditional ritual forms (lǐ) that expressed and maintained the social relationships constituting the human world. The Analects' famous formulations — 'Do not impose on others what you yourself do not want' (the Silver Rule, Analects 15.24); 'The superior man is not a vessel' (2.12, on the integrated person vs. the specialist); 'At fifteen I set my heart on learning; at thirty I stood firm; at forty I had no doubts' (2.4, Confucius's intellectual autobiography) — express a vision of moral self-cultivation that has influenced Chinese and East Asian ethics for over 2,500 years.\n\nThe Analects was made one of the Four Books (四書) of the Confucian canon by Zhu Xi (1130–1200 CE), which became the curriculum of the imperial examination system from 1313 CE until its abolition in 1905 — meaning that virtually every educated Chinese person for six centuries had studied and memorised it. Its influence on Chinese governance, social structure, family ethics, and intellectual culture is nearly impossible to overstate.",
    "causes": [
      "The political and social crisis of the Spring and Autumn period (771–476 BCE) — the fragmentation of Zhou feudal order, the decline of ritual forms, and the moral corruption of the ruling nobility — created the urgent intellectual problem to which Confucius's teachings were a response: how to restore social and political harmony through moral cultivation.",
      "The Zhou dynasty's ritual tradition — the elaborate system of ceremonial forms (lǐ) that had structured aristocratic social life — provided Confucius with the cultural materials he sought to preserve and revitalise, and the Analects is in large part a record of his passionate commitment to their restoration and correct interpretation.",
      "The Chinese educational tradition of preserving the words of great teachers through memorisation and written record — Confucius himself taught that the study of classical texts was the foundation of moral education — created the cultural practice within which the Analects was compiled, transmitted, and eventually canonised."
    ],
    "effects": [
      "The Analects, through the Confucian tradition it founded, became the dominant intellectual framework of China for over two millennia — shaping Chinese governance (the meritocratic bureaucracy selected through examination of Confucian texts), family ethics (filial piety, ancestor veneration), social hierarchy, and the ideal of the virtuous scholar-official.",
      "The Confucian tradition that the Analects founded spread throughout East Asia — to Korea (where the Confucian examination system was adopted, influencing government and family structure), Japan (where Confucian ethics shaped samurai culture, the education system, and business ethics), and Vietnam — making the Analects one of the most culturally influential texts in world history.",
      "The 20th century's challenges to the Confucian tradition — the May Fourth Movement (1919), Mao's Cultural Revolution (1966–1976), and subsequent revivals — illustrate the text's centrality to Chinese cultural identity: debates about modernisation, democracy, and national identity have repeatedly returned to the question of the Analects' relevance, with its teachings alternately condemned as feudal tradition and celebrated as timeless wisdom."
    ],
    "relationships": [
      {"sourceSlug": "confucius", "sourceName": "Confucius (551–479 BCE)", "verb": "RECORDED_IN", "targetSlug": "analects", "targetName": "Analects", "context": "The Analects records the sayings and conversations of Confucius — compiled by his disciples after his death, it is the primary source for his philosophical teachings."},
      {"sourceSlug": "analects", "sourceName": "Analects", "verb": "CANONISED_BY", "targetSlug": "zhu-xi", "targetName": "Zhu Xi (Neo-Confucian philosopher, 1130–1200 CE)", "context": "Zhu Xi's compilation of the Four Books — making the Analects central to the Neo-Confucian curriculum — led to its adoption as the core text of the imperial examination system, ensuring its dominance in Chinese education from 1313 to 1905."},
      {"sourceSlug": "analects", "sourceName": "Analects", "verb": "FOUNDATIONS_OF", "targetSlug": "confucianism", "targetName": "Confucianism", "context": "The Analects is the foundational text of Confucianism — the philosophical and ethical tradition that dominated Chinese intellectual life and spread throughout East Asia."}
    ],
    "places": [
      {"name": "State of Lu, China (Spring and Autumn period, 6th–5th century BCE)", "role": "Confucius's home state — the context of his teaching and the political world he sought to reform through moral cultivation"},
      {"name": "East Asia (China, Korea, Japan, Vietnam)", "role": "The geographic sphere of Confucian influence — the countries whose intellectual, political, and social traditions were shaped for centuries by the Confucian teachings of the Analects"}
    ],
    "subjects": ["Chinese Philosophy", "Confucianism", "Classical Era", "East Asia", "Ethics", "Political Philosophy", "Chinese History", "World Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Analects (compiled c. 5th–4th century BCE) — the collected sayings of Confucius — is the foundational text of Confucianism, the philosophical tradition that dominated Chinese intellectual and political life for over two millennia. As the core text of the imperial examination system from 1313 to 1905, virtually every educated Chinese person studied it; its influence on Chinese governance, family ethics, and social structure, and on Korean, Japanese, and Vietnamese cultures, makes it one of the most historically consequential texts in human history.",
      "significanceCategory": "world-changing"
    }
  }
},

"arthashastra": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780arthashastra.json",
  "slug": "arthashastra",
  "data": {
    "summary": "The Arthashastra (Sanskrit: अर्थशास्त्र, 'Science of Material Gain' or 'Science of Statecraft') is the ancient Indian treatise on political science, economic policy, and military strategy attributed to Kautilya (also known as Chanakya or Vishnugupta), the adviser who is credited with helping Chandragupta Maurya (r. c. 321–297 BCE) overthrow the Nanda dynasty and found the Maurya Empire. Compiled in approximately the 4th–3rd century BCE (though the text in its surviving form shows evidence of later additions), the Arthashastra is the most comprehensive ancient Indian text on statecraft and the administration of empire — covering taxation, law, military organisation, intelligence operations, diplomacy, economic management, and the duties of a king with a systematic thoroughness that has led to frequent comparison with Machiavelli's Prince and Sun Tzu's Art of War.\n\nThe Arthashastra's worldview is resolutely pragmatic (and often ruthless): the king's primary duty is the welfare of his state (rajadharma), and almost any means are justified in its service. The text describes an elaborate system of secret agents (spies, assassins, provocateurs), recommends the use of psychological warfare and deception against enemies, and provides detailed guidance on how to deal with treacherous ministers, conspiracies, and foreign rivals. The famous analysis of the 'Mandala theory' — the framework of concentric circles of allies and enemies in which a king's natural ally is his neighbour's neighbour — remains a classic formulation of realist geopolitical thinking. The Arthashastra also contains surprisingly modern economic thinking: on market regulation, the prevention of monopoly, the management of state finances, and the importance of trade.\n\nThe Arthashastra was lost to Western and modern Indian scholarship until a palm-leaf manuscript was discovered in Mysore in 1904 and published by R. Shamasastry in 1909. Its rediscovery transformed the understanding of ancient Indian political thought and confirmed that classical India had produced a sophisticated tradition of realist political science independent of and contemporaneous with the Greek political philosophy of Thucydides and Plato.",
    "causes": [
      "The political crisis of the late Nanda dynasty — its oppressive taxation, military weakness, and popular resentment — created the context in which Kautilya and Chandragupta could mobilise a revolutionary force, and the Arthashastra's comprehensive treatise on statecraft reflects the practical problems of building and governing a new empire.",
      "The Indian tradition of political science (nītiśāstra) — including earlier texts like the Nitisara and various treatises attributed to mythological sages — provided the intellectual framework within which Kautilya was working, though the Arthashastra systematises and expands the tradition far beyond any predecessor.",
      "The practical requirements of the Maurya Empire — governing an enormous, diverse subcontinent with limited communications — created the administrative, military, and intelligence challenges that the Arthashastra's systematic treatment of statecraft was designed to address."
    ],
    "effects": [
      "The Arthashastra provided the administrative and political framework for the Maurya Empire — ancient India's first pan-subcontinental empire — whose administrative sophistication (as confirmed by archaeological and epigraphic evidence) broadly reflects the Arthashastra's prescriptions for royal governance.",
      "After its rediscovery in 1909, the Arthashastra transformed the Western scholarly understanding of ancient Indian political thought — demonstrating that classical India had produced a tradition of realist political science of equal sophistication to the Greek tradition, challenging the stereotype of ancient India as primarily spiritual and otherworldly.",
      "The Arthashastra's influence on contemporary Indian political culture — the frequent invocation of 'Chanakya niti' (Kautilya's policy wisdom) in modern Indian political discourse — demonstrates its continuing relevance as a symbol of Indian strategic and political sophistication, cited in debates about Indian foreign policy and statecraft."
    ],
    "relationships": [
      {"sourceSlug": "kautilya", "sourceName": "Kautilya (Chanakya, c. 350–275 BCE)", "verb": "AUTHORS", "targetSlug": "arthashastra", "targetName": "Arthashastra", "context": "Kautilya is the attributed author of the Arthashastra — as Chandragupta Maurya's adviser, his practical experience of imperial administration informs the text's systematic treatment of statecraft."},
      {"sourceSlug": "arthashastra", "sourceName": "Arthashastra", "verb": "INFORMS", "targetSlug": "maurya-empire", "targetName": "Maurya Empire (c. 321–185 BCE)", "context": "The Arthashastra's prescriptions for royal administration are broadly reflected in the Maurya Empire's governance — the empire Kautilya helped Chandragupta found."},
      {"sourceSlug": "arthashastra", "sourceName": "Arthashastra", "verb": "COMPARED_TO", "targetSlug": "the-prince-machiavelli", "targetName": "Machiavelli's The Prince (1513)", "context": "The Arthashastra's pragmatic, sometimes ruthless advice on statecraft — including deception, intelligence, and the justification of means by the state's welfare — has led to frequent comparison with Machiavelli's Prince, though they emerged independently in different cultures."}
    ],
    "places": [
      {"name": "Pataliputra, Maurya Empire (modern Bihar, India, c. 321–297 BCE)", "role": "The political context of the Arthashastra — the Maurya imperial capital from which Chandragupta and Kautilya governed the first pan-Indian empire"},
      {"name": "Mysore, India (1904 rediscovery)", "role": "The site of the Arthashastra's modern rediscovery — a palm-leaf manuscript found in Mysore in 1904 that restored the text to scholarly knowledge after centuries of loss"}
    ],
    "subjects": ["Ancient India", "Political Philosophy", "Classical Era", "Statecraft", "Maurya Empire", "Indian History", "Economics", "Military Strategy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Arthashastra (attributed to Kautilya, c. 4th–3rd century BCE) is ancient India's comprehensive treatise on statecraft — a systematic treatment of political administration, military strategy, economic management, and intelligence operations that provided the framework for the Maurya Empire. Its rediscovery in 1909 demonstrated that classical India had produced a tradition of realist political science of equal sophistication to the Greek tradition, and it remains a living reference in modern Indian political discourse.",
      "significanceCategory": "highly-significant"
    }
  }
},

"ab-urbe-condita-livy": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781ab-urbe-condita-livy.json",
  "slug": "ab-urbe-condita-livy",
  "data": {
    "summary": "Ab Urbe Condita ('From the Founding of the City') is the monumental history of Rome written by Titus Livius (Livy, 64 or 59 BCE–17 CE), comprising 142 books (of which 35 survive: books 1–10 and 21–45) covering Roman history from the legendary founding of Rome (traditionally 753 BCE) to 9 BCE. It is one of the great works of Latin prose and the most comprehensive surviving account of Roman history from its origins through the late Republic — Livy's vivid narrative style, moral seriousness, and gallery of heroic and villainous Roman characters made it the principal source for Roman legendary and Republican history for all subsequent ages, from the Renaissance through the 19th century.\n\nLivy wrote during the reign of Augustus (27 BCE–14 CE), working under the emperor's cultural program of restoring Roman traditional values after the civil wars. His history reflects this Augustan moral project: the great question of Ab Urbe Condita is how Rome rose to greatness through virtue (virtus) and fell into moral decay through success and luxury — the narrative is populated by exemplary Romans (Brutus the elder, Horatius Cocles, Cincinnatus, Camillus, Fabius Maximus, Scipio Africanus) whose individual virtue drives Rome's rise, and by cautionary figures whose ambition or corruption marks its decline. The Hannibalic War (books 21–30, covering 218–201 BCE) — the most complete surviving section — is both the climax of Roman virtue (Fabius, Scipio) and the greatest test of Roman collective character.\n\nLivy's influence on European historical and political thought is immense: Machiavelli's Discourses on Livy (Discorsi sopra la prima deca di Tito Livio, 1517) is the founding text of modern republicanism, structured as a commentary on the first ten books of Ab Urbe Condita, and Livy's heroic Roman exempla (Brutus, Mucius Scaevola, Lucretia, Coriolanus, Virginia) shaped Renaissance humanism, Shakespeare's Roman plays, Neoclassical painting, and the political rhetoric of the French and American revolutions.",
    "causes": [
      "The Augustan cultural program — the emperor's project of restoring Roman traditional values, ancestral religion, and the moral virtue that had supposedly characterised early Rome — provided both the political context and the ideological framework within which Livy wrote his history of Roman origins and the Republic.",
      "The end of the civil wars (31 BCE, Actium) and the establishment of Augustus's stable rule created the political peace in which a long-term literary project of 142 books was feasible, and the need to construct a coherent Roman past for the new Augustan order gave Livy's historical project cultural urgency.",
      "The Roman tradition of exemplary history — using historical narratives to provide moral models (exempla) for contemporary Romans — shaped Livy's method: his stated purpose is to provide instructive portraits of virtue and vice, so that readers can imitate the former and avoid the latter."
    ],
    "effects": [
      "Livy's Ab Urbe Condita became the principal source for Roman Republican history in European culture — the legendary narratives (Romulus and Remus, Horatius Cocles, Lucretia and the Tarquins, Coriolanus, Cincinnatus) that shaped European understanding of ancient Rome were transmitted primarily through Livy, making him one of the most culturally formative historians in the Western tradition.",
      "Machiavelli's Discourses on Livy (1517) — the founding text of modern republican theory — structured its entire analysis of republican government around commentary on Livy's first decade, making Ab Urbe Condita the indirect source of the republican political theory that shaped the American and French revolutions.",
      "Livy's moral exempla — the heroic Romans who sacrificed personal interest for the state's welfare, the virtuous women who died to protect their honour, the stern fathers who executed their sons for military disobedience — became central to Neoclassical aesthetics, inspiring Jacques-Louis David's paintings (The Oath of the Horatii, 1784; Lictors Bring to Brutus the Bodies of His Sons, 1789) and the patriotic rhetoric of the revolutionary era."
    ],
    "relationships": [
      {"sourceSlug": "livy", "sourceName": "Livy (59 BCE–17 CE)", "verb": "AUTHORS", "targetSlug": "ab-urbe-condita-livy", "targetName": "Ab Urbe Condita", "context": "Livy spent most of his adult life composing Ab Urbe Condita — the 142-book history of Rome that was the most comprehensive treatment of Roman Republican history in Latin literature."},
      {"sourceSlug": "ab-urbe-condita-livy", "sourceName": "Ab Urbe Condita", "verb": "INSPIRES", "targetSlug": "machiavelli-discourses", "targetName": "Machiavelli's Discourses on Livy (1517)", "context": "Machiavelli's Discourses — structured as a commentary on Livy's first decade — used Ab Urbe Condita as the foundation for his republican political theory, making Livy's history the indirect source of modern republicanism."},
      {"sourceSlug": "augustus-caesar", "sourceName": "Augustus Caesar (63 BCE–14 CE)", "verb": "CONTEMPORARY_OF", "targetSlug": "ab-urbe-condita-livy", "targetName": "Ab Urbe Condita", "context": "Livy wrote under Augustus's reign and within his cultural program — the history's moral project of restoring Roman republican virtue aligned with the Augustan restoration of traditional Roman values."}
    ],
    "places": [
      {"name": "Rome (Augustan period, late 1st century BCE)", "role": "The context of composition — Livy writing in Augustan Rome about the Roman past, providing the new empire with a coherent mythological and historical foundation"},
      {"name": "Europe (Renaissance and early modern influence)", "role": "The sphere of cultural influence — Livy's history shaped Renaissance humanism, early modern political thought, Neoclassical art, and the revolutionary political rhetoric of the 18th century"}
    ],
    "subjects": ["Roman History", "Latin Literature", "Classical Era", "Ancient Rome", "Historiography", "Republican History", "Livy", "Augustan Age"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Ab Urbe Condita (Livy, 1st century BCE–17 CE) — the 142-book history of Rome from its founding through the early Augustan period — is the primary source for Roman legendary and Republican history, shaping European understanding of ancient Rome from the Renaissance onwards. Machiavelli's foundational republican treatise Discourses on Livy is structured as a commentary on its first ten books, making Livy's history the indirect source of modern republican political theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"act-of-abjuration": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781act-of-abjuration.json",
  "slug": "act-of-abjuration",
  "data": {
    "summary": "The Act of Abjuration (Dutch: Plakkaat van Verlatinghe, 'Placard of Abandonment') is the declaration by which the States General of the United Provinces of the Netherlands formally renounced their allegiance to King Philip II of Spain on 26 July 1581 — making it the formal founding document of the Dutch Republic and the first declaration of independence by a people from a ruling monarch in Western history. It was the culmination of the Eighty Years' War (1568–1648), the Dutch revolt against Spanish Habsburg rule that had begun under William the Silent (William of Orange), and it directly inspired the American Declaration of Independence (1776), which follows its argumentative structure and borrows several of its key formulations.\n\nThe Act was drafted primarily by Pieter van Brederode and written with input from William of Orange, and its political philosophy draws on the Calvinist and natural law theory of the right to resist tyrannical government. It argues that a prince who violates the rights of his subjects and governs as a tyrant forfeits his claim to their allegiance — the people, in the Dutch natural law framework, have entrusted sovereignty to the prince conditionally, and when he breaks that trust, the people may lawfully depose him. The Act catalogues Philip II's specific violations (the Inquisition, the Duke of Alba's atrocities, the violation of ancient privileges) as the justification for the transfer of sovereignty back to the people's representatives.\n\nThe Dutch Republic that the Act of Abjuration founded went on to become, in the 17th century, one of the most remarkable political and economic experiments in European history — the world's first capitalist republic, a centre of religious tolerance and intellectual freedom (sheltering Descartes, Spinoza, Locke during his exile), a global trading empire (VOC, WIC), and a model of republican governance that influenced the English, American, and French revolutions.",
    "causes": [
      "The Eighty Years' War against Spanish rule — triggered by the Spanish Inquisition in the Netherlands, the Duke of Alba's brutal suppression of Protestant worship and civil liberties, and the imposition of heavy taxation — created the popular revolt and the political leadership (William of Orange) that made the Act of Abjuration politically feasible and necessary.",
      "The Calvinist theological justification of resistance to tyranny — drawing on Calvinist political theology (Knox, Beza, the Vindiciae contra tyrannos of 1579) that authorised resistance to rulers who violated divine law and the people's rights — provided the ideological framework within which the Act's argument for justified deposition was constructed.",
      "The failure of repeated negotiations with Philip II and his refusal to acknowledge the privileges and religious freedoms of the Dutch provinces — forcing the States General to choose between submission and full independence — made the formal act of abjuration the only remaining option by July 1581."
    ],
    "effects": [
      "The Act of Abjuration founded the Dutch Republic — the 'Golden Age' republic of the 17th century that was a centre of religious tolerance, philosophical freedom, scientific innovation, and global trade, serving as a model of republican governance that influenced European and world political development.",
      "The Act directly influenced the American Declaration of Independence (1776) — Thomas Jefferson's Declaration follows the same argumentative structure (statement of political philosophy, catalogue of royal abuses, declaration of independence) and borrows several specific formulations, making the Act of Abjuration the most direct political ancestor of American independence.",
      "The Act established the precedent of a formally argued legal-political declaration of independence — the use of natural law theory to justify collective resistance to and deposition of a tyrannical sovereign — that became the template for subsequent independence movements from the American Revolution through the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "william-of-orange", "sourceName": "William of Orange (William the Silent, 1533–1584)", "verb": "LEADS_CREATION_OF", "targetSlug": "act-of-abjuration", "targetName": "Act of Abjuration (1581)", "context": "William of Orange was the political leader of the Dutch revolt whose advocacy and influence were central to the Act of Abjuration — drafted under his direction by Pieter van Brederode."},
      {"sourceSlug": "act-of-abjuration", "sourceName": "Act of Abjuration (1581)", "verb": "INSPIRES", "targetSlug": "united-states-declaration-of-independence", "targetName": "American Declaration of Independence (1776)", "context": "The Declaration of Independence's structure and several formulations derive directly from the Act of Abjuration — making the Dutch declaration the most important direct political ancestor of American independence."},
      {"sourceSlug": "act-of-abjuration", "sourceName": "Act of Abjuration", "verb": "FOUNDS", "targetSlug": "dutch-republic", "targetName": "Dutch Republic (United Provinces, 1581–1795)", "context": "The Act of Abjuration is the founding document of the Dutch Republic — the declaration that formally established the sovereignty of the United Provinces independent of the Spanish Crown."}
    ],
    "places": [
      {"name": "The Hague, Netherlands (26 July 1581)", "role": "The place of signing — The Hague, where the States General formally ratified the Act of Abjuration and declared independence from Philip II of Spain"},
      {"name": "Dutch Republic and global republican tradition", "role": "The sphere of consequence — the Act founded the Dutch Republic and inspired subsequent declarations of independence, particularly the American Declaration of 1776"}
    ],
    "subjects": ["Dutch History", "Political Philosophy", "Early Modern Era", "Dutch Republic", "Eighty Years' War", "Independence", "Natural Law", "Revolutionary History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Act of Abjuration (1581) — the Dutch declaration of independence from Philip II of Spain — is the first formal declaration of independence in Western history and the direct model for the American Declaration of Independence (1776). Its natural law argument for the right to depose a tyrannical sovereign, and the Dutch Republic it founded (the 17th century's model of religious tolerance, republican government, and global trade), gave it an outsized influence on the development of modern democratic theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"communist-manifesto": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785communist-manifesto.json",
  "slug": "communist-manifesto",
  "data": {
    "summary": "The Communist Manifesto (German: Manifest der Kommunistischen Partei, 'Manifesto of the Communist Party') is the political pamphlet written by Karl Marx (1818–1883) and Friedrich Engels (1820–1895) and published in London on 21 February 1848 — commissioned by the Communist League as a statement of its aims and methods. It is one of the most influential political documents in history: its opening declaration 'A spectre is haunting Europe — the spectre of communism' and its closing rallying cry 'Workers of all countries, unite!' are among the most famous passages in political literature, and the pamphlet provided the ideological foundation for the labour movements, socialist parties, and communist revolutions of the 19th and 20th centuries that reshaped the world.\n\nThe Manifesto's core argument rests on Marx and Engels's materialist theory of history: all history is the history of class struggle (between master and slave, lord and serf, bourgeois and proletarian); the modern industrial capitalist system has created a new class of industrial workers (the proletariat) whose interests are irreconcilably opposed to those of the bourgeoisie that employs them; and this contradiction will inevitably produce a communist revolution in which the proletariat seizes political power, abolishes private property and the class system, and creates a classless society. The Manifesto also contains a famous ten-point program for the transitional period (progressive income tax, abolition of inheritance, centralisation of credit, free education) and a withering critique of rival socialist traditions (utopian socialism, petty-bourgeois socialism, 'true' socialism).\n\nPublished on the eve of the 1848 revolutions, the Manifesto had limited immediate impact but grew in influence through the 19th century as the labour movement and the First and Second Internationals spread Marxist ideas. In the 20th century it became the foundational text of communist parties worldwide, and the Soviet Revolution of 1917 made its prescriptions the official ideology of a state that at its peak controlled one-third of the world's population. The Manifesto has been published in over 500 editions and translated into virtually every language — by some measures it is the most printed secular text in history.",
    "causes": [
      "The Industrial Revolution's creation of the industrial proletariat — a new urban working class subject to market conditions, long working hours, child labour, and periodic unemployment — created the social conditions that made Marx and Engels's analysis of capitalist exploitation compelling and gave the communist program its potential mass constituency.",
      "The 1847 Communist League's need for a systematic statement of its program — distinguishing communist aims from the various socialist and radical movements of the period — provided the immediate commission that produced the Manifesto's specific pamphlet form.",
      "Marx's intellectual synthesis of German idealist philosophy (Hegel), French revolutionary politics, and English classical economics — the three sources Engels identified at Marx's graveside as the components of scientific socialism — created the theoretical framework within which the Manifesto's analysis of capitalist society was constructed."
    ],
    "effects": [
      "The Manifesto provided the ideological foundation for the international labour movement of the 19th–20th centuries — the socialist parties, trade unions, and communist parties that changed the political landscape of Europe and beyond, winning the eight-hour day, universal suffrage, and welfare states through decades of struggle.",
      "The Bolshevik Revolution of 1917 — the first successful communist revolution, explicitly drawing on the Manifesto's analysis — created the Soviet Union, which at its peak (1950s) controlled one-third of the world's population and territory and engaged the United States in the Cold War (1947–1991) that defined global politics for four decades.",
      "The 20th century's communist states — the Soviet Union, China, Cuba, North Korea, and others that claimed the Manifesto as their founding document — collectively conducted experiments in command economics, single-party rule, and social transformation that affected hundreds of millions of people, producing both significant social achievements (literacy, public health, industrialisation) and catastrophic human rights abuses (gulags, cultural revolution, famines)."
    ],
    "relationships": [
      {"sourceSlug": "karl-marx", "sourceName": "Karl Marx (1818–1883)", "verb": "CO-AUTHORS", "targetSlug": "communist-manifesto", "targetName": "Communist Manifesto (1848)", "context": "Marx was the primary intellectual author of the Manifesto — Engels contributed the draft and collaborative thinking, but the philosophical framework was primarily Marx's."},
      {"sourceSlug": "communist-manifesto", "sourceName": "Communist Manifesto", "verb": "INSPIRES", "targetSlug": "russian-revolution-1917", "targetName": "Russian Revolution (1917)", "context": "The Manifesto's analysis of capitalism and its call for communist revolution provided the ideological framework of the Bolshevik Revolution — Lenin explicitly drew on Marx and Engels in building the revolutionary party and the Soviet state."},
      {"sourceSlug": "communist-manifesto", "sourceName": "Communist Manifesto", "verb": "PRECEDES", "targetSlug": "capital-a-critique-of-political-economy", "targetName": "Capital (Marx, 1867)", "context": "The Manifesto (1848) stated the political program and historical theory that Capital (1867) provided with systematic economic analysis — together they form the theoretical and practical core of Marxism."}
    ],
    "places": [
      {"name": "London, England (February 1848)", "role": "The place of publication — London, where the Communist League commissioned and published the Manifesto in the weeks before the 1848 revolutions swept Europe"},
      {"name": "Global (20th-century communist states)", "role": "The worldwide spread of the Manifesto's ideas — from the Soviet Union and China to Cuba, Vietnam, and beyond, communist parties claiming the Manifesto as their founding document governed states containing at peak over one-third of humanity"}
    ],
    "subjects": ["Marxism", "Political Philosophy", "Modern Era", "Communism", "Labor History", "Revolution", "Political Economy", "19th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Communist Manifesto (Marx and Engels, 1848) is one of the most politically consequential documents in history — its analysis of capitalism and class struggle, and its call for communist revolution, provided the ideological foundation for the international labour movement, the Soviet Revolution (1917), and the communist states that governed one-third of the world's population at their peak. By some measures the most printed secular text in history, its influence on 20th-century politics, economics, and global conflict was unmatched.",
      "significanceCategory": "world-changing"
    }
  }
},

"capital-a-critique-of-political-economy": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785capital-a-critique-of-political-economy.json",
  "slug": "capital-a-critique-of-political-economy",
  "data": {
    "summary": "Capital: A Critique of Political Economy (German: Das Kapital: Kritik der politischen Ökonomie) is the major theoretical work of Karl Marx (1818–1883), the first volume of which was published in Hamburg on 14 September 1867. The most systematic and comprehensive treatment of Marx's economic theory, it analyses the capitalist mode of production through the categories of classical political economy (Smith, Ricardo) while demolishing their theoretical foundations from within. Its central concepts — commodity, value, surplus value, capital accumulation, the tendency of the rate of profit to fall, the reserve army of labour — constitute the theoretical core of Marxist economics and have made Das Kapital one of the most cited and debated works in social science.\n\nCapital's core argument begins with the commodity as the 'cell-form' of capitalism and the labour theory of value: commodities are exchanged in proportion to the socially necessary labour time required to produce them. But the capitalist buys not labour but labour-power (the worker's capacity to work), for which he pays the worker a wage equivalent to the labour necessary to reproduce that capacity. The worker then works longer than this reproduction time, creating surplus value — the unpaid portion of the worker's labour — which is the source of capitalist profit. Capital is thus, in Marx's formulation, 'dead labour that, vampire-like, only lives by sucking living labour'. The capital accumulation process — the drive to re-invest surplus value to extract more surplus value — generates both the extraordinary productive capacity of capitalism and its recurrent crises (overproduction, falling profit rates), and ultimately creates the conditions for its own overthrow by the proletariat it exploits.\n\nVolumes II and III of Capital were published posthumously by Engels from Marx's manuscripts (1885 and 1894 respectively), and the three volumes together constitute the foundational theoretical framework of Marxist political economy. The influence of Capital on academic economics (whether through direct acceptance or through the responses of neoclassical economics), on political theory, sociology, and the intellectual justification of the 20th century's communist and socialist states, is one of the most profound single-work impacts in the history of social thought.",
    "causes": [
      "Marx's decade of systematic study in the British Museum (1850s–1860s) — reading the complete corpus of classical political economy, economic history, and parliamentary blue books on working-class conditions — provided the empirical and theoretical basis for Capital's comprehensive critique.",
      "The development of industrial capitalism in Britain — the working conditions of Manchester and London factories, the factory acts and their violations, the periodic economic crises — provided the empirical reality that Capital was analysing, and Marx spent years accumulating the evidence of capitalist exploitation that gives the work its political force.",
      "The failure of the 1848 revolutions and Marx's recognition that the revolution he had anticipated in the Communist Manifesto required a more rigorous theoretical foundation — a systematic analysis of how capitalism actually worked — drove the decades of economic study that produced Capital."
    ],
    "effects": [
      "Capital provided the theoretical foundation for Marxist political economy — the analytical framework within which generations of socialist economists, labour movement theorists, and communist party intellectuals understood capitalism and justified their political programs, making it the most influential work of economic theory in the politics of the 20th century.",
      "The Soviet Union's command economy — based on the theoretical principle that capitalist market mechanisms should be replaced by central planning, derived from Marx's critique of commodity production and surplus value extraction — was one of the 20th century's largest social experiments, directly influenced by Capital's theoretical framework.",
      "Capital's analytical concepts — surplus value, commodity fetishism, alienation, the reserve army of labour, capital accumulation — entered the vocabulary of social science and cultural criticism broadly, influencing not just economics but sociology (Lukács, Gramsci, the Frankfurt School), cultural theory, and feminist political economy, shaping intellectual life far beyond the political movements explicitly committed to Marxism."
    ],
    "relationships": [
      {"sourceSlug": "karl-marx", "sourceName": "Karl Marx (1818–1883)", "verb": "AUTHORS", "targetSlug": "capital-a-critique-of-political-economy", "targetName": "Capital (1867)", "context": "Marx worked on Capital for nearly two decades — the first volume was the only one he completed for publication, with volumes II and III prepared from his manuscripts by Engels after his death."},
      {"sourceSlug": "capital-a-critique-of-political-economy", "sourceName": "Capital", "verb": "CRITIQUES", "targetSlug": "adam-smith", "targetName": "Classical Political Economy (Smith, Ricardo)", "context": "Capital's critique of political economy is directed primarily at Adam Smith and David Ricardo — using their own labour theory of value to demonstrate that profit is derived from the exploitation of labour."},
      {"sourceSlug": "capital-a-critique-of-political-economy", "sourceName": "Capital", "verb": "INFORMS", "targetSlug": "soviet-union", "targetName": "Soviet Union (command economy)", "context": "The Soviet command economy was theoretically justified by Capital's critique of commodity production and surplus value — Lenin and Soviet economists drew on Das Kapital as the theoretical foundation for replacing capitalist market mechanisms with central planning."}
    ],
    "places": [
      {"name": "London (British Museum Reading Room) and Hamburg (publication, 1867)", "role": "The context of production and publication — Marx researched Capital at the British Museum's Reading Room and published volume I in Hamburg in 1867"},
      {"name": "Global (20th century socialist/communist world)", "role": "The sphere of political influence — Capital's theoretical framework shaped the economic thinking of socialist and communist parties worldwide, from the Soviet Union and China to the postcolonial left"}
    ],
    "subjects": ["Marxism", "Political Economy", "Modern Era", "Economics", "Capitalism", "Labor Theory", "Social Theory", "19th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Capital (Marx, 1867) is the theoretical foundation of Marxist political economy — the systematic analysis of the capitalist mode of production whose concepts of surplus value, capital accumulation, and the tendency of the rate of profit to fall provided the economic framework for socialist and communist movements globally. Its influence on the Soviet command economy, on 20th-century socialist parties, and on the social sciences broadly (sociology, cultural theory, feminist economics) makes it one of the most consequential theoretical works in history.",
      "significanceCategory": "world-changing"
    }
  }
},

"de-re-publica-cicero": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785de-re-publica-cicero.json",
  "slug": "de-re-publica-cicero",
  "data": {
    "summary": "De Re Publica ('On the Republic') is the political philosophical dialogue written by Marcus Tullius Cicero (106–43 BCE) in approximately 54–51 BCE, modelled on Plato's Republic but drawing on the Roman Stoic tradition and Cicero's own experience as a senator and consul to develop a theory of the ideal state based on the Roman mixed constitution. Composed at a moment of acute political crisis — the breakdown of the Roman Republic under the First Triumvirate of Caesar, Pompey, and Crassus — De Re Publica is both a philosophical treatment of justice and government and a meditation on the political institutions Cicero saw dissolving before him.\n\nThe dialogue is set in 129 BCE at the country estate of Scipio Africanus the Younger (Scipio Aemilianus), and the central participants are historical figures — Scipio, Laelius, and other distinguished Romans — who discuss the nature of the best state, the forms of government, the role of justice in political community, and the qualities of the ideal statesman. Cicero's central argument is that the Roman mixed constitution — combining elements of monarchy (the consuls), aristocracy (the Senate), and democracy (the popular assemblies) — is the practically best form of government because it balances and stabilises the tendencies of each pure form. The famous 'Somnium Scipionis' ('Dream of Scipio') that closes the work — in which the dead Scipio Africanus the Elder reveals to his adopted grandson the cosmic order and the immortal soul's destiny — is one of the most celebrated passages in Latin literature.\n\nLarge portions of De Re Publica were lost in antiquity, and the work was known only through fragments and the Dream of Scipio until Angelo Mai discovered a substantial palimpsest manuscript in the Vatican in 1820. Its influence on medieval Christian political thought (through the Dream of Scipio and Augustine's quotations) and on modern republicanism (through its theory of natural law, the social contract, and the mixed constitution) makes it a foundational text of Western political philosophy.",
    "causes": [
      "The crisis of the Roman Republic in the 50s BCE — the First Triumvirate's effective monopolisation of power, the violence of street politics, and the drift toward civil war — gave Cicero's philosophical meditation on the best republic its urgent political dimension: he was theorising the institutions he saw being destroyed.",
      "Cicero's Platonic model — his explicit intention to do for Roman thought what Plato had done for Greek thought, providing a comprehensive philosophical treatment of politics, ethics, and the cosmos — shaped De Re Publica's form (the dialogue), its Platonic references, and its cosmic-eschatological conclusion (the Dream of Scipio echoing the Myth of Er in Plato's Republic).",
      "The Roman Stoic tradition — particularly the Stoic theory of natural law and universal reason as the foundation of justice and political community — provided Cicero with the philosophical framework for arguing that the best state is grounded in natural justice, not merely convention or power."
    ],
    "effects": [
      "De Re Publica's theory of natural law — the argument that justice is grounded in universal reason and not merely human convention — entered the Western tradition through Cicero's later works (De Legibus, De Officiis) and became a foundational concept of medieval Christian political theology, the basis of later natural rights theory, and a precedent for Locke, Rousseau, and the American Declaration of Independence.",
      "The Dream of Scipio — the cosmological and eschatological finale of De Re Publica — was read as a pagan prefiguration of Christian eschatology throughout the Middle Ages, preserved in Macrobius's Commentary (c. 400 CE), and became one of the most widely read texts of the medieval Latin tradition, shaping the Christian understanding of the soul's cosmic journey.",
      "Cicero's portrait of the Roman mixed constitution as the practically best form of government — and his identification of the Roman Republic's combination of consuls, Senate, and assemblies as the model of stable mixed government — influenced Polybius's constitutional theory, Machiavelli's Discourses, and Montesquieu's theory of the separation of powers."
    ],
    "relationships": [
      {"sourceSlug": "cicero", "sourceName": "Cicero (106–43 BCE)", "verb": "AUTHORS", "targetSlug": "de-re-publica-cicero", "targetName": "De Re Publica (c. 54–51 BCE)", "context": "Cicero wrote De Re Publica in 54–51 BCE as his major contribution to political philosophy — modelled on Plato but drawing on Roman constitutional practice and Stoic natural law theory."},
      {"sourceSlug": "platos-republic", "sourceName": "Plato's Republic", "verb": "MODELS", "targetSlug": "de-re-publica-cicero", "targetName": "De Re Publica", "context": "De Re Publica is explicitly modelled on Plato's Republic — using the same dialogue form, the same three interlocutors/participants structure, and ending with a cosmic eschatological vision (the Dream of Scipio echoing the Myth of Er)."},
      {"sourceSlug": "de-re-publica-cicero", "sourceName": "De Re Publica", "verb": "INFLUENCES", "targetSlug": "augustine-of-hippo", "targetName": "Augustine of Hippo (354–430 CE)", "context": "Augustine extensively quotes and engages De Re Publica in The City of God — his critique of Cicero's definition of justice became the foundational debate of medieval Christian political philosophy."}
    ],
    "places": [
      {"name": "Rome and central Italy (54–51 BCE)", "role": "The context of composition — Cicero writing at his Tusculum estate during the political crisis of the late Republic, theorising the institutions he saw being destroyed"},
      {"name": "Medieval Europe (through the Dream of Scipio)", "role": "The sphere of medieval influence — the Dream of Scipio was preserved by Macrobius and read throughout the Middle Ages as a cosmological and eschatological text"}
    ],
    "subjects": ["Roman Philosophy", "Political Philosophy", "Classical Era", "Ancient Rome", "Natural Law", "Republican Theory", "Cicero", "Roman Republic"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "De Re Publica (Cicero, c. 54–51 BCE) is the foundational work of Roman political philosophy — a meditation on the ideal state drawing on Stoic natural law, the Roman mixed constitution, and the model of Plato's Republic. Its theory of natural law influenced medieval Christian political theology and modern natural rights theory; its 'Dream of Scipio' was one of the most widely read texts of the medieval Latin tradition; and its portrait of the Roman mixed constitution shaped Western constitutional theory from Polybius through Montesquieu.",
      "significanceCategory": "highly-significant"
    }
  }
},

"declaration-of-sentiments-1848": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785declaration-of-sentiments-1848.json",
  "slug": "declaration-of-sentiments-1848",
  "data": {
    "summary": "The Declaration of Sentiments (also known as the Declaration of Rights and Sentiments) is the document drafted primarily by Elizabeth Cady Stanton and adopted at the Seneca Falls Convention in Seneca Falls, New York on 19–20 July 1848 — the first women's rights convention in American history. Modelled deliberately on the American Declaration of Independence, it begins with the famous adaptation 'We hold these truths to be self-evident: that all men and women are created equal' and systematically catalogues the legal, political, educational, and social disabilities under which American women then suffered — from the denial of the vote to their exclusion from education, the professions, and property rights — as grievances requiring redress. It is the founding document of the American women's rights movement and one of the most significant political declarations of the 19th century.\n\nThe convention was organised by Elizabeth Cady Stanton, Lucretia Mott, and three other women, inspired in part by the World Anti-Slavery Convention in London (1840) at which women delegates — including Stanton and Mott — had been refused seats. The Declaration was signed by 68 women and 32 men (including Frederick Douglass, who spoke in support of the suffrage resolution). Its most controversial resolution — demanding women's right to vote — passed by a narrow margin and was widely ridiculed by the press, but it became the central demand of the suffrage movement that, after 72 years of activism, culminated in the Nineteenth Amendment to the US Constitution (ratified 18 August 1920).\n\nThe Declaration of Sentiments drew on Mary Wollstonecraft's A Vindication of the Rights of Woman (1792), the natural rights philosophy of the Enlightenment, and the abolitionist movement's language of universal human dignity to construct a comprehensive argument for women's equality. Its rhetorical strategy of appropriating the Declaration of Independence's language — inserting 'and women' into Jefferson's famous sentence — challenged Americans to apply their founding principles consistently across gender.",
    "causes": [
      "The exclusion of women abolitionists (Stanton, Mott) from the World Anti-Slavery Convention in London (1840) — despite their active participation in the abolitionist movement — made visible the contradiction between abolitionist principles of universal human dignity and the treatment of women in reform movements and society generally.",
      "The legal disabilities of married women in mid-19th century America — coverture laws that made married women legally non-persons (unable to own property, enter contracts, or retain wages), combined with their exclusion from universities, the professions, and political life — created the social conditions that gave the Declaration's grievances their urgency.",
      "The abolitionist movement's development of the language of natural rights and universal human dignity — and the experience of women organisers (Stanton, Mott, Grimké sisters) in that movement — provided both the ideological framework and the organisational skills that made the Seneca Falls convention and the Declaration possible."
    ],
    "effects": [
      "The Seneca Falls Declaration launched the organised American women's rights movement — the 72-year campaign for women's suffrage that passed through the Civil War, the failure of the Fourteenth Amendment to include women, the split between the NWSA and AWSA, and ultimately achieved the Nineteenth Amendment (1920) granting women the right to vote.",
      "The Declaration's rhetorical strategy of inserting 'and women' into the Declaration of Independence's language — claiming equality on the basis of America's own founding principles — became the central rhetorical move of the women's rights movement, forcing Americans to choose between applying their principles consistently or admitting their inconsistency.",
      "The Seneca Falls Declaration inspired women's rights movements internationally — the British suffragette movement (Millicent Fawcett, Emmeline Pankhurst), the women's rights movements of other Western countries, and ultimately the global women's rights framework articulated in the UN's Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW, 1979)."
    ],
    "relationships": [
      {"sourceSlug": "elizabeth-cady-stanton", "sourceName": "Elizabeth Cady Stanton (1815–1902)", "verb": "DRAFTS", "targetSlug": "declaration-of-sentiments-1848", "targetName": "Declaration of Sentiments (1848)", "context": "Stanton was the primary drafter of the Declaration of Sentiments — writing it in the days before the Seneca Falls Convention and modelling it on the Declaration of Independence."},
      {"sourceSlug": "declaration-of-sentiments-1848", "sourceName": "Declaration of Sentiments (1848)", "verb": "MODELLED_ON", "targetSlug": "united-states-declaration-of-independence", "targetName": "US Declaration of Independence (1776)", "context": "The Declaration of Sentiments deliberately echoes and adapts the Declaration of Independence — inserting 'and women' into Jefferson's famous sentence to claim gender equality on the basis of America's founding principles."},
      {"sourceSlug": "declaration-of-sentiments-1848", "sourceName": "Declaration of Sentiments", "verb": "LEADS_TO", "targetSlug": "nineteenth-amendment", "targetName": "Nineteenth Amendment (1920)", "context": "The Declaration's demand for women's suffrage — the most controversial resolution at Seneca Falls — was the founding demand of the 72-year American suffrage movement that culminated in the Nineteenth Amendment."}
    ],
    "places": [
      {"name": "Seneca Falls, New York, USA (19–20 July 1848)", "role": "The place of adoption — the small New York town whose Wesleyan Methodist Chapel hosted the first American women's rights convention and the signing of the Declaration"},
      {"name": "United States and global women's rights movement", "role": "The sphere of influence — the Declaration inspired the American suffrage movement and, through it, women's rights movements worldwide"}
    ],
    "subjects": ["Feminism", "American History", "Modern Era", "Women's Rights", "Suffrage", "Political Philosophy", "19th Century", "Civil Rights"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Declaration of Sentiments (1848) — adopted at Seneca Falls, the first American women's rights convention — is the founding document of the organised American women's suffrage movement, launching the 72-year campaign that culminated in the Nineteenth Amendment (1920). Its rhetorical appropriation of the Declaration of Independence's language ('all men and women are created equal') remains one of the most powerful examples of turning a nation's founding principles against its existing inequalities.",
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
