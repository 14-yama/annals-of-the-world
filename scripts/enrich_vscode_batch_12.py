#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 12 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: henry-cromwell, postumus-cominius-auruncus, wikimedia-foundation,
          hieronymus-van-beverningh, alfonso-i-deste, tuldila, middle-ages, hortar
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-12-may2026"

ENRICHMENTS = {

"henry-cromwell": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220henry-cromwell.json",
  "slug": "henry-cromwell",
  "data": {
    "summary": "Henry Cromwell (1628–1674) was the fourth son of Oliver Cromwell and served as Lord Deputy and then Lord Lieutenant of Ireland (1655–1659) — the most powerful administrative position in the Cromwellian settlement of Ireland, and the longest-serving effective ruler of Ireland during the Interregnum. Henry's Irish administration represented one of the more pragmatic and relatively moderate phases of Cromwellian rule: where his father had been associated with the catastrophic military campaigns of 1649–1650 (the sieges of Drogheda and Wexford), Henry's tenure in Dublin was characterised by attempts at stable civilian administration, patronage of the reformed church in Ireland, and a degree of accommodation with Irish Protestant landowners that contrasted with the more ideologically rigid elements of the English Puritan military government.\n\nHenry Cromwell was appointed to Ireland in 1655 in the face of considerable opposition from the Anabaptist and radical Puritan factions within the Parliamentary army in Ireland, who viewed him as insufficiently committed to godly reformation. His gradual consolidation of authority over the Irish administration — marginalising the army radicals, building relationships with the Irish Protestant gentry, and promoting a moderate Presbyterian-influenced church settlement — reflected the broader conservative turn in the English Interregnum under his father's later Protectorate. He was given the title Lord Lieutenant (replacing Lord Deputy) in 1657, making him nominally the highest authority in Ireland.\n\nHenry's career was cut short by the fall of the Protectorate: following his father Oliver's death (September 1658) and the rapid collapse of his brother Richard Cromwell's brief Protectorate (April–May 1659), Henry resigned his position in Ireland and retired to private life in England. He lived out the remaining fifteen years of his life as a private gentleman, escaping the executions and persecutions that followed the Restoration of Charles II in 1660 — a relatively fortunate end for a member of the Cromwell family.",
    "causes": [
      "Oliver Cromwell's military conquest of Ireland (1649–1650) — the Drogheda and Wexford sieges and the subsequent land settlement that dispossessed Catholic landowners — created the Cromwellian Ireland that Henry Cromwell was appointed to administer and stabilise.",
      "The factional struggles within the English Interregnum between radical army Puritans (Anabaptists, Fifth Monarchists) and more conservative Protectorate supporters directly shaped Henry's appointment to Ireland and his approach to governing it — he was sent partly to check the influence of the radical army faction.",
      "Oliver Cromwell's conservative turn after the dissolution of the Barebones Parliament (1653) and the establishment of the Protectorate created the political environment that allowed Henry to pursue a relatively moderate Irish settlement aligned with the interests of the Protestant landowning class."
    ],
    "effects": [
      "Henry Cromwell's administration contributed to the consolidation of the Cromwellian land settlement in Ireland — the massive transfer of land from Catholic to Protestant ownership that reshaped Irish land tenure for centuries and that remains a significant factor in Irish historical grievance.",
      "His relatively moderate approach to Irish Protestant governance helped establish the Protestant ascendancy class — the Anglo-Irish landowning elite — as the dominant social force in Ireland, a position that characterised Irish society until the late 19th century.",
      "Henry Cromwell's quiet retirement after 1659 and his survival through the Restoration (unlike many regicides) illustrates both the pragmatic flexibility of the Restoration settlement and the distinctions drawn between direct participants in Charles I's execution and those who had served the Protectorate in administrative rather than judicial roles."
    ],
    "relationships": [
      {"sourceSlug": "henry-cromwell", "sourceName": "Henry Cromwell", "verb": "ADMINISTERS", "targetSlug": "cromwellian-ireland", "targetName": "Cromwellian Ireland", "context": "Henry served as Lord Deputy/Lieutenant of Ireland (1655–1659) — the primary administrator of the Cromwellian settlement that had dispossessed Catholic landowners and established Protestant governance."},
      {"sourceSlug": "oliver-cromwell", "sourceName": "Oliver Cromwell", "verb": "APPOINTS", "targetSlug": "henry-cromwell", "targetName": "Henry Cromwell", "context": "Oliver Cromwell appointed his son Henry to Ireland in 1655 — a reflection of both familial trust and the need for a Cromwell family member to manage the increasingly fractious Irish administration."},
      {"sourceSlug": "henry-cromwell", "sourceName": "Henry Cromwell", "verb": "SHAPES", "targetSlug": "protestant-ascendancy", "targetName": "Protestant Ascendancy in Ireland", "context": "Henry's administration contributed to the consolidation of the Protestant landowning class in Ireland — his governance supported the Anglo-Irish gentry whose dominance of Irish society persisted until the late 19th century."}
    ],
    "places": [
      {"name": "Dublin, Ireland", "role": "The seat of Henry Cromwell's government — Dublin Castle as the centre of English colonial administration in Ireland during the Interregnum"},
      {"name": "Ireland", "role": "The territory Henry governed (1655–1659) — Cromwellian Ireland was undergoing the massive land confiscations and Protestant settlement that reshaped Irish society"}
    ],
    "subjects": ["Cromwellian Ireland", "English Interregnum", "Early Modern History", "Early Modern Era", "Ireland", "British History", "Protectorate", "Irish History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Henry Cromwell, son of Oliver Cromwell, was Lord Lieutenant of Ireland (1655–1659) — a relatively moderate administrator who consolidated the Cromwellian land settlement and promoted the Protestant ascendancy class that dominated Irish society for two centuries. His career illustrates the Protectorate's conservative turn and the establishment of the Anglo-Irish colonial structure.",
      "significanceCategory": "regional"
    }
  }
},

"postumus-cominius-auruncus": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220postumus-cominius-auruncus.json",
  "slug": "postumus-cominius-auruncus",
  "data": {
    "summary": "Postumus Cominius Auruncus (fl. early 5th century BCE; consul 501 BCE and 493 BCE) was a Roman Republican politician and military commander notable primarily for his role in the capture of the Volscian town of Corioli in 493 BCE — the victory that gave the Roman general Gnaeus Marcius his cognomen 'Coriolanus' (the subject of Plutarch's biography and, via Plutarch, Shakespeare's tragedy). As consul during the Roman Republic's early period of military and political consolidation, Postumus Cominius participated in the wars against the Volsci, Sabines, and other Latin and Italian peoples that defined Roman military activity in the late 6th and early 5th centuries BCE.\n\nCominius served twice as consul — in 501 BCE (when Rome was threatened by the Latin League and the exiled king Tarquinius Superbus) and in 493 BCE (the year of the Corioli campaign). He is remembered in ancient sources primarily as the commander-in-chief under whom Gnaeus Marcius Coriolanus distinguished himself in battle at Corioli — an episode central to the Coriolanus tradition, in which Marcius's superhuman bravery in single-handedly entering the city of Corioli while the Roman troops hesitated is the foundational act of the Coriolanus legend. Cominius, as the consul in command, recommended Marcius for military honours and gave him the cognomen that commemorated his victory.\n\nThe historical figure of Cominius illustrates the nature of Roman Republican memory and its selective focus: he is preserved in the historical tradition not for his own importance but as the supporting character who recognises and rewards the legendary bravery of Coriolanus. This pattern — in which minor historical figures survive in the record primarily because they intersected with more famous events — is characteristic of the annalistic tradition that transmitted early Roman history.",
    "causes": [
      "The early Roman Republic's ongoing conflicts with the Volsci, Sabines, Aequi, and other Italic peoples — the persistent military frontier wars of the 5th century BCE that shaped Roman military culture and produced the legends of early Roman virtue — provided the military context for Cominius's consular campaigns.",
      "The Roman Republican cursus honorum and the institution of the consulship — under which two annually elected consuls held supreme military and civil authority — gave Cominius the command position from which he directed the Corioli campaign and recognised Coriolanus's bravery.",
      "The Roman annalistic tradition — the recording of consular fasti (the lists of annual magistrates) and the historical tradition built around them — preserved Cominius's name in the record as the consul of 493 BCE, even though his individual significance is primarily as the commander in the Coriolanus episode."
    ],
    "effects": [
      "Cominius's naming of Gnaeus Marcius 'Coriolanus' — the award of a cognomen commemorating the capture of Corioli — created the legendary name that gave Shakespeare's tragedy its title and that has made Coriolanus one of the most recognisable figures of early Roman Republican legend.",
      "The Corioli campaign of 493 BCE was part of the Roman military consolidation of Latium and the surrounding regions that, over two centuries, would transform Rome from a regional Latin power to the hegemon of the Italian peninsula.",
      "The tradition of the Coriolanus story — preserved through Livy, Dionysius of Halicarnassus, and Plutarch — provides important (if legendised) evidence for early Roman Republican military practices, the Roman system of military honours, and the social tensions between patricians and plebeians that produced the Conflict of the Orders."
    ],
    "relationships": [
      {"sourceSlug": "postumus-cominius-auruncus", "sourceName": "Postumus Cominius Auruncus", "verb": "COMMANDS", "targetSlug": "coriolanus", "targetName": "Gnaeus Marcius Coriolanus", "context": "Cominius was the consul who commanded the Roman forces at Corioli (493 BCE) — under whose command Coriolanus performed his legendary acts of bravery, and who awarded Marcius the cognomen 'Coriolanus'."},
      {"sourceSlug": "volscian-wars", "sourceName": "Volscian Wars", "verb": "SHAPES", "targetSlug": "postumus-cominius-auruncus", "targetName": "Postumus Cominius Auruncus", "context": "The Roman wars against the Volsci in the early 5th century BCE were the military theatre of Cominius's consular command — the conflicts that produced both his historical record and the legendary Coriolanus episode."},
      {"sourceSlug": "postumus-cominius-auruncus", "sourceName": "Postumus Cominius Auruncus", "verb": "PARTICIPATES_IN", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "As consul of 501 BCE and 493 BCE, Cominius was a senior magistrate of the early Roman Republic — one of the holders of supreme Roman authority during the formative period of Republican institutions."}
    ],
    "places": [
      {"name": "Corioli, Latium (Italy)", "role": "The Volscian town captured in 493 BCE under Cominius's command — whose name gave Gnaeus Marcius his cognomen 'Coriolanus'"},
      {"name": "Rome, Italian Peninsula", "role": "The political centre of Cominius's career — Rome where he held the consulship twice and from which the campaigns against the Volsci were directed"}
    ],
    "subjects": ["Roman Republic", "Ancient Rome", "Classical Era", "Early Roman History", "Italy", "Republican Rome", "Coriolanus Legend", "Consular History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Postumus Cominius Auruncus was the Roman consul (501, 493 BCE) who commanded the Corioli campaign in which Gnaeus Marcius performed his legendary bravery — and who awarded Marcius the cognomen 'Coriolanus' that gave Shakespeare's tragedy its name. His historical significance is primarily as the supporting character in the Coriolanus legend, preserved in the Roman annalistic tradition via Livy, Plutarch, and Shakespeare.",
      "significanceCategory": "local"
    }
  }
},

"wikimedia-foundation": {
  "filepath": "data/appwrite-export/entities/373-Class-373/373wikimedia-foundation.json",
  "slug": "wikimedia-foundation",
  "data": {
    "summary": "The Wikimedia Foundation is an American non-profit organisation founded on 20 June 2003 by Wikipedia co-founder Jimmy Wales — established to host and support the free knowledge projects including Wikipedia (launched 2001), Wikimedia Commons, Wikidata, Wikisource, Wiktionary, and related sister projects. Headquartered in San Francisco, California, the Wikimedia Foundation is one of the most significant organisations in the history of the internet and of human knowledge production: Wikipedia, its primary project, has become the world's largest and most widely consulted encyclopaedia — with over 60 million articles in approximately 330 languages as of 2024, serving approximately 1.5 billion unique devices per month.\n\nThe foundation's mission is to make the sum of all human knowledge freely available to every person on the planet — a goal stated in explicitly universalist terms that has positioned the Wikimedia projects as a global public infrastructure for knowledge access. Unlike the major internet platforms (Google, Facebook, Amazon), the Wikimedia Foundation is a non-profit that operates without advertising revenue, depending entirely on donations from millions of individuals and institutional grants. This financial model — which has been periodically controversial as Wikipedia's servers and staff costs have grown — has preserved the encyclopaedia's independence from commercial pressures and advertising influence.\n\nWikipedia's epistemological impact on human knowledge access has been transformative: it is the first reference source consulted by hundreds of millions of people globally, it has displaced commercial encyclopaedias (Encyclopædia Britannica ceased print publication in 2012), and its collaborative authoring model — in which millions of volunteer editors create, verify, and maintain content under transparent policies — represents an entirely new model of knowledge production. Wikidata (launched 2012) has become a major linked data infrastructure for the semantic web, while Wikimedia Commons holds over 90 million freely licensed media files that are used across the internet.",
    "causes": [
      "The launch of Wikipedia in January 2001 — the wiki-based encyclopaedia project that grew from Nupedia's open-content experiment — created a rapidly expanding volunteer-produced knowledge resource that required a formal non-profit institutional home, leading Jimmy Wales to establish the Wikimedia Foundation in 2003.",
      "The open-source and free knowledge movements of the late 1990s–2000s — the 'information wants to be free' culture of the early web, combined with the GNU/Linux precedent of volunteer collaborative software production — provided the philosophical and technical framework within which Wikipedia's collaborative authoring model could be conceived and implemented.",
      "The internet's radical reduction in the marginal cost of knowledge distribution — making it technically feasible to serve encyclopaedia content to billions of people at near-zero marginal cost — removed the primary economic barrier to universal knowledge access and made the Wikimedia Foundation's mission practically achievable in ways that would have been impossible in the pre-internet era."
    ],
    "effects": [
      "Wikipedia has become the world's primary first-access reference resource — displacing commercial encyclopaedias, reducing the information asymmetry between the developed and developing worlds, and fundamentally changing how billions of people access basic factual information.",
      "The Wikimedia Foundation's model of volunteer-produced, freely licensed knowledge has demonstrated the viability of collaborative open content production at massive scale — influencing the design of countless other collaborative platforms and contributing to the broader open-source, open-access, and open-data movements.",
      "Wikidata — the Wikimedia Foundation's structured data project (launched 2012) — has become a foundational layer of the semantic web, providing machine-readable, multilingual linked data that underlies Google's Knowledge Graph, countless digital humanities projects, and AI training datasets including those used for large language models."
    ],
    "relationships": [
      {"sourceSlug": "wikimedia-foundation", "sourceName": "Wikimedia Foundation", "verb": "OPERATES", "targetSlug": "wikipedia", "targetName": "Wikipedia", "context": "The Wikimedia Foundation is the institutional operator of Wikipedia — the world's largest encyclopaedia, whose content it hosts on a non-profit, advertising-free basis."},
      {"sourceSlug": "jimmy-wales", "sourceName": "Jimmy Wales", "verb": "FOUNDS", "targetSlug": "wikimedia-foundation", "targetName": "Wikimedia Foundation", "context": "Jimmy Wales — Wikipedia's co-founder — established the Wikimedia Foundation in 2003 to provide institutional and financial support for Wikipedia and the growing ecosystem of Wikimedia projects."},
      {"sourceSlug": "wikimedia-foundation", "sourceName": "Wikimedia Foundation", "verb": "ENABLES", "targetSlug": "open-knowledge-movement", "targetName": "Open Knowledge Movement", "context": "The Wikimedia Foundation's mission — free knowledge for every person — has been the most visible institutional expression of the open knowledge movement, demonstrating that volunteer collaborative production can create world-class reference resources."}
    ],
    "places": [
      {"name": "San Francisco, California, USA", "role": "Headquarters of the Wikimedia Foundation since 2008 — the centre of the organisation's operations and governance"},
      {"name": "Global Internet", "role": "The primary operational environment of the Wikimedia projects — Wikipedia and the other Wikimedia sites are global digital infrastructure serving 1.5 billion users monthly"}
    ],
    "subjects": ["Digital History", "Internet History", "Contemporary Era", "Knowledge Access", "Information Technology", "Open Source", "Encyclopedia", "Non-profit Organisations"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Wikimedia Foundation is one of the most consequential institutions of the digital age — the non-profit operator of Wikipedia, the world's largest encyclopaedia serving 1.5 billion users monthly in 330 languages. Its volunteer-collaborative knowledge model has displaced commercial encyclopaedias, reduced global information asymmetry, and created the Wikidata infrastructure that underlies much of the semantic web. It is arguably the most successful realisation of the 'information wants to be free' ethos of the early internet.",
      "significanceCategory": "world-changing"
    }
  }
},

"hieronymus-van-beverningh": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220hieronymus-van-beverningh.json",
  "slug": "hieronymus-van-beverningh",
  "data": {
    "summary": "Hieronymus van Beverningh (1614–1690) was a Dutch statesman, diplomat, and regent — one of the most active Dutch diplomatic negotiators of the 17th century, whose career spanned the height of the Dutch Golden Age and the complex European power politics that followed the Peace of Westphalia (1648). A member of the Gouda regent class, Beverningh served as one of the Netherlands' principal diplomats in the critical decades of Anglo-Dutch and European rivalry that shaped the geopolitical order of the late 17th century.\n\nBeverningh's most significant diplomatic roles included participation in the negotiations for the Peace of Westminster (1654) — the peace that ended the First Anglo-Dutch War and that, controversially, contained the 'Act of Seclusion' (secretly negotiated by Johan de Witt, but with Beverningh as a key participant) excluding the House of Orange from stadtholdership; his role in the negotiations for the Treaty of Breda (1667) ending the Second Anglo-Dutch War; and most significantly, his crucial role in the preparation of the 1688 Glorious Revolution — Beverningh was one of the Dutch statesmen who participated in the preparations for William of Orange's invasion of England, helping to secure the constitutional and diplomatic framework that made the Revolution possible.\n\nBeverningh's career illustrates the distinctive character of Dutch Republican foreign policy under the First Stadtholderless Period (1650–1672) and the personal union with England after 1688: the Holland regent class maintained a complex relationship with the House of Orange, alternately supporting and limiting its power, and conducting foreign policy primarily in the interests of Amsterdam commercial capitalism rather than dynastic ambition. His diplomatic activity across four decades of Anglo-Dutch conflict and eventually reconciliation (through the Glorious Revolution) made him one of the most experienced diplomatic practitioners of his era.",
    "causes": [
      "The First Anglo-Dutch War (1652–1654) and the subsequent series of Anglo-Dutch conflicts over maritime trade dominance, colonial possessions, and the carrying trade created the diplomatic challenges that brought Beverningh to prominence as one of the Netherlands' senior negotiators.",
      "The Dutch Republic's distinctive political structure — in which the Holland regent oligarchy (rather than a monarch or army) controlled foreign policy — produced a diplomatic tradition focused on commercial interests, balance-of-power calculations, and the careful management of European alliances.",
      "Johan de Witt's leadership of Dutch foreign policy during the First Stadtholderless Period (1650–1672) created a framework of anti-Orangist, commercially-oriented diplomacy within which Beverningh operated as a trusted and technically expert negotiator."
    ],
    "effects": [
      "Beverningh's participation in the negotiations for the Act of Seclusion (1654) — secretly excluding the House of Orange from the stadtholdership — contributed to the First Stadtholderless Period that shaped the Dutch Republic's political character and its foreign policy approach for over two decades.",
      "His role in the diplomatic preparations for the Glorious Revolution (1688) was significant in ensuring that William of Orange's invasion of England was supported by the political framework necessary for its success — the Dutch statesmen who prepared the constitutional ground for the Revolution were as important as the military operation itself.",
      "Beverningh's diplomatic career contributed to the development of the Dutch tradition of professional, technically expert diplomacy — an approach centred on legal precision, commercial calculation, and careful treaty drafting that became a model for European diplomatic practice."
    ],
    "relationships": [
      {"sourceSlug": "hieronymus-van-beverningh", "sourceName": "Hieronymus van Beverningh", "verb": "PARTICIPATES_IN", "targetSlug": "glorious-revolution", "targetName": "Glorious Revolution (1688)", "context": "Beverningh was among the Dutch statesmen who participated in the diplomatic preparations for William of Orange's 1688 invasion of England — helping to build the political framework that made the constitutional revolution possible."},
      {"sourceSlug": "hieronymus-van-beverningh", "sourceName": "Hieronymus van Beverningh", "verb": "NEGOTIATES", "targetSlug": "peace-of-westminster-1654", "targetName": "Peace of Westminster (1654)", "context": "Beverningh was one of the Dutch negotiators for the Peace of Westminster (1654) ending the First Anglo-Dutch War — including the controversial Act of Seclusion excluding the House of Orange."},
      {"sourceSlug": "dutch-republic", "sourceName": "Dutch Republic", "verb": "EMPLOYS", "targetSlug": "hieronymus-van-beverningh", "targetName": "Hieronymus van Beverningh", "context": "The Dutch Republic's regent oligarchy — particularly the Holland ruling class — employed Beverningh as one of its principal diplomats across four decades of European power politics."}
    ],
    "places": [
      {"name": "Gouda, Dutch Republic (Netherlands)", "role": "Beverningh's home city — the member of the Holland regent class whose oligarchic governance he represented"},
      {"name": "London and The Hague", "role": "The primary locations of Beverningh's diplomatic activity — the Anglo-Dutch relationship was the central axis of his career"}
    ],
    "subjects": ["Dutch Republic", "17th Century Diplomacy", "Early Modern Era", "Netherlands", "Anglo-Dutch Relations", "Early Modern History", "Glorious Revolution", "Dutch Golden Age"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Hieronymus van Beverningh was one of the Dutch Republic's most active diplomats — participating in the Peace of Westminster (1654), the Treaty of Breda (1667), and the diplomatic preparations for the Glorious Revolution (1688). His career spans four decades of Anglo-Dutch rivalry and eventual partnership, illustrating the distinctive character of Dutch Republican foreign policy under the Holland regent oligarchy.",
      "significanceCategory": "regional"
    }
  }
},

"alfonso-i-deste": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220alfonso-i-deste.json",
  "slug": "alfonso-i-deste",
  "data": {
    "summary": "Alfonso I d'Este (1476–1534) was Duke of Ferrara, Modena, and Reggio from 1505 until his death — one of the most politically complex and culturally brilliant princes of the Italian Renaissance, whose reign coincided with the most turbulent decades of the Italian Wars (1494–1559). Son of Ercole I d'Este and Eleonora of Aragon, Alfonso is perhaps most famous as the third husband of Lucrezia Borgia (married 1502) — the famously notorious daughter of Pope Alexander VI whose marriage to Alfonso was a diplomatic alliance between the Este duchy and the Borgia papacy. Their marriage, which proved surprisingly stable and affectionate, coincided with one of the most challenging periods of the Este duchy's existence.\n\nAlfonso was one of the most skilled artillery commanders of his era: the Este duchy's expertise in bronze cannon manufacture made Ferrara a significant centre of Renaissance military technology, and Alfonso personally supervised the development and deployment of artillery in his campaigns. He fought against Pope Julius II (who sought to recover Ferrara for the Papal States) in the War of the League of Cambrai (1508–1516) — an extraordinary conflict in which Alfonso allied with France against the Pope, was excommunicated, and successfully defended his duchy against papal forces through a combination of military skill and political flexibility. The spectacle of a prince using artillery effectively against papal armies was one of the more dramatic illustrations of Italian Renaissance political fragmentation.\n\nAlfonso was also a major patron of the arts: Titian painted several famous works for him including the 'Bacchanal of the Andrians' and the 'Feast of the Gods' (completing Bellini's painting), Ludovico Ariosto dedicated 'Orlando Furioso' (1516) to him, and the Ferrarese court was one of the most culturally vibrant of the Italian Renaissance. The Este patronage tradition — centred on the painted studiolo, literary commissions, and musical performance — made Alfonso's Ferrara a benchmark of Renaissance courtly culture.",
    "causes": [
      "The Italian Wars (1494–1559) — the successive French, Spanish, and imperial invasions of Italy that turned the peninsula into a battlefield — created the military and political crises that defined Alfonso's reign and forced the Este duchy into a constant game of alliance management between the great powers.",
      "The Borgia papacy's aggressive political ambitions — and the subsequent Julius II papacy's equally aggressive determination to recover Ferrara for the Papal States — directly threatened Este independence and forced Alfonso into the military and diplomatic struggle that dominated his reign.",
      "Alfonso's inheritance of the Este artistic patronage tradition — going back to his father Ercole I and grandfather Borso d'Este — created the cultural environment in which Titian, Ariosto, and the Ferrarese school flourished, building on and enriching the tradition Alfonso received."
    ],
    "effects": [
      "Alfonso's successful defence of Ferrara against Pope Julius II during the War of the League of Cambrai established Este independence at a time when many smaller Italian principalities were being absorbed by the great powers — his political and military survival was a significant achievement of Renaissance statecraft.",
      "Alfonso's patronage of Titian — who painted the famous 'camerino d'alabastro' series for Alfonso's private study — was one of the most significant artist-patron relationships of the Renaissance, producing some of Titian's greatest mythological works and establishing the Este court as a major centre of High Renaissance painting.",
      "The d'Este marriage alliance with Lucrezia Borgia — which proved to be one of the more successful of the era's dynastic marriages — contributed to Lucrezia's rehabilitation from Borgia notoriety to respected Renaissance duchess, though the Borgia association remained a defining feature of how posterity remembered both of them."
    ],
    "relationships": [
      {"sourceSlug": "alfonso-i-deste", "sourceName": "Alfonso I d'Este", "verb": "MARRIES", "targetSlug": "lucrezia-borgia", "targetName": "Lucrezia Borgia", "context": "Alfonso's marriage to Lucrezia Borgia (1502) — the diplomatic alliance between the Este duchy and the Borgia papacy — proved surprisingly stable and contributed to Lucrezia's rehabilitation as Duchess of Ferrara."},
      {"sourceSlug": "titian", "sourceName": "Titian", "verb": "SERVES", "targetSlug": "alfonso-i-deste", "targetName": "Alfonso I d'Este", "context": "Titian painted several of his greatest works for Alfonso — including the 'Bacchanal of the Andrians' and the completion of Bellini's 'Feast of the Gods' — making the Este court a defining context of High Renaissance painting."},
      {"sourceSlug": "italian-wars", "sourceName": "Italian Wars (1494–1559)", "verb": "THREATENS", "targetSlug": "alfonso-i-deste", "targetName": "Alfonso I d'Este", "context": "The Italian Wars — particularly Pope Julius II's campaign to recover Ferrara — directly threatened Este independence and forced Alfonso into the military and diplomatic struggles that defined his reign."}
    ],
    "places": [
      {"name": "Ferrara, Italy", "role": "Capital of the Este duchy and site of Alfonso's court — one of the most culturally vibrant courts of the Italian Renaissance under his patronage"},
      {"name": "Italian Peninsula", "role": "The broader context of Alfonso's reign — the Italian Wars that turned the peninsula into a battlefield between France, Spain, and the Papacy defined the political environment Alfonso had to navigate"}
    ],
    "subjects": ["Italian Renaissance", "Este Dynasty", "Medieval Era", "Italy", "Renaissance Art", "Medieval History", "Italian Wars", "Ferrara"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Alfonso I d'Este was Duke of Ferrara (1505–1534) — Renaissance prince, artillery innovator, husband of Lucrezia Borgia, patron of Titian and Ariosto, and successful defender of Este independence against Pope Julius II. His court was one of the High Renaissance's most brilliant cultural centres, and his military and political survival during the Italian Wars was a significant achievement of Renaissance statecraft.",
      "significanceCategory": "significant"
    }
  }
},

"tuldila": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221tuldila.json",
  "slug": "tuldila",
  "data": {
    "summary": "Tuldila (died 458 CE) was a king or military leader of the Suebi — the Germanic people who had established a kingdom in northwestern Iberia (modern Galicia and northern Portugal) following the Visigothic-led Germanic crossing of the Rhine in 406 CE and the subsequent Suebian settlement of Gallaecia in 409 CE. The Suebian kingdom of Gallaecia (c. 409–585 CE) was one of the first post-Roman successor kingdoms in western Europe, and Tuldila's record represents the turbulent internal politics and military conflicts of the Suebian state in its mid-5th-century phase.\n\nTuldila is documented primarily in the Chronicle of Hydatius — the mid-5th century bishop of Chaves (in modern Portugal) whose chronicle is the primary source for the history of northwestern Iberia from c. 379–468 CE and one of the most important sources for the transitional period from Roman to Germanic rule in the western provinces. Hydatius records Tuldila's death in 458 CE in the context of the Suebian kingdom's internal factional struggles and its conflicts with the Visigothic kingdom (which had conquered most of Iberia by the mid-5th century but had not yet fully subdued the Suebi of the northwest). The Suebian kingdom in this period was characterised by frequent internal dynastic conflicts, Christian controversies (between Catholic and Arian factions), and military confrontations with Visigothic pressure from the south and east.\n\nTuldila's specific role in Suebian politics — whether he was a king, a sub-king, a military commander, or a noble — is uncertain due to the brief and elliptical nature of Hydatius's references. He represents the type of documented but poorly understood figure from the 'Migration Period' whose name survives in the fragmentary chronicles of the post-Roman world without the context that would allow his specific significance to be fully recovered.",
    "causes": [
      "The Suebian migration into Gallaecia (409 CE) — part of the broader Germanic crossing of the Rhine and the disintegration of Roman authority in the western provinces — established the Suebian kingdom within which Tuldila's career unfolded, creating the Germanic successor state context for his documented activity.",
      "The Suebian kingdom's internal factional struggles — the frequent dynastic conflicts among Suebian leaders recorded in Hydatius's chronicle — created the political environment in which figures like Tuldila rose, competed, and died, reflecting the fragmented and contested nature of Suebian political power.",
      "The Visigothic pressure on the Suebian kingdom in the 440s–450s CE — as the Visigoths consolidated their Iberian supremacy and periodically intervened in Suebian internal affairs — created the external military threat that shaped the context of Tuldila's career and death."
    ],
    "effects": [
      "Tuldila's death in 458 CE — recorded by Hydatius — is one of the data points that allows modern historians to reconstruct the sequence of Suebian political leaders and internal conflicts in the mid-5th century, contributing to the historiography of the Migration Period in Iberia.",
      "The Suebian kingdom of which Tuldila was a part survived into the 6th century — ultimately being conquered by the Visigoths in 585 CE — and its Christian conversion (completed by Martin of Braga in the late 6th century) contributed to the Christianisation of the Iberian northwest.",
      "The chronicle tradition that preserves Tuldila's name — Hydatius's chronicle — is one of the most important sources for the transition from Roman to Germanic rule in the western provinces, and Tuldila is among the figures whose documented activity helps to establish the chronological framework of that transition."
    ],
    "relationships": [
      {"sourceSlug": "tuldila", "sourceName": "Tuldila", "verb": "LEADS", "targetSlug": "suebian-kingdom", "targetName": "Suebian Kingdom of Gallaecia", "context": "Tuldila was a leader in the Suebian kingdom of northwestern Iberia — one of the documented figures in the complex internal politics of the Suebian state recorded by Hydatius."},
      {"sourceSlug": "hydatius-chronicle", "sourceName": "Chronicle of Hydatius", "verb": "RECORDS", "targetSlug": "tuldila", "targetName": "Tuldila", "context": "The primary source for Tuldila is Hydatius's chronicle — the 5th-century bishop's account of northwestern Iberian history that is the main evidence for the Suebian kingdom's mid-5th-century internal conflicts."},
      {"sourceSlug": "visigothic-kingdom", "sourceName": "Visigothic Kingdom", "verb": "PRESSURES", "targetSlug": "suebian-kingdom", "targetName": "Suebian Kingdom (including Tuldila)", "context": "Visigothic pressure on the Suebian kingdom in the 440s–460s CE shaped the political context of Tuldila's career — the external threat that complicated Suebian internal politics."}
    ],
    "places": [
      {"name": "Gallaecia (modern Galicia, Spain / northern Portugal)", "role": "The territory of the Suebian kingdom — the northwestern corner of the Iberian Peninsula where Tuldila's political activity was located"},
      {"name": "Iberian Peninsula", "role": "The broader context of Suebian history — the peninsula where Germanic successor kingdoms replaced Roman provincial administration in the early 5th century"}
    ],
    "subjects": ["Migration Period", "Suebian History", "Classical Era", "Iberian History", "Germanic Peoples", "Ancient History", "Post-Roman Europe", "Galicia"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Tuldila was a Suebian leader documented in Hydatius's chronicle as dying in 458 CE — a figure of the Suebian kingdom of Gallaecia whose name survives in the fragmentary record of 5th-century northwestern Iberian history. His significance is primarily as evidence for the turbulent internal politics of the Suebian state in the Migration Period.",
      "significanceCategory": "local"
    }
  }
},

"middle-ages": {
  "filepath": "data/appwrite-export/entities/920-Class-920/920middle-ages.json",
  "slug": "middle-ages",
  "data": {
    "summary": "The Middle Ages (also Medieval Period or Medieval Era) is the historiographical term for the central period of European history, conventionally dated from approximately 500 CE (the collapse of the Western Roman Empire in 476 CE or the death of Boethius in 524 CE) to approximately 1500 CE (the expulsion of the Moors from Spain and Columbus's voyage to the Americas in 1492, or Luther's Reformation in 1517). The term was coined during the Italian Renaissance — first implied by humanists like Flavio Biondo and Petrarch as a way of distinguishing the 'middle' period of history between the grandeur of classical antiquity and the recovery of that grandeur in their own era from both bookends. The very concept thus embeds a value judgment: the Middle Ages were, from the Renaissance humanist perspective, an unfortunate interval that interrupted the superior civilisation of ancient Rome.\n\nThe Middle Ages encompass enormous diversity — geographically (European, Byzantine, Islamic, Chinese, and other civilisations all have their 'medieval' periods, though the European usage is most conventional), chronologically (the 'Early Middle Ages' c. 500–1000 CE and 'High/Late Middle Ages' c. 1000–1500 CE are often distinguished), and culturally (the period spans from the Benedictine monasteries of early medieval Europe to the Gothic cathedrals, scholastic universities, Black Death, and early capitalism of the later medieval period). The conventional division into Early, High, and Late Middle Ages reflects real differences in European historical experience: depopulation and cultural contraction in the early period, demographic and economic expansion in the High Middle Ages, and the crises (Black Death, Great Schism, Hundred Years' War) and transformations of the later period.\n\nThe reputation of the Middle Ages has been profoundly shaped by historiographical tradition. The Renaissance humanist dismissal (the term 'Dark Ages' for the early medieval period) has been gradually revised by modern medieval historians who have demonstrated the period's significant intellectual, artistic, architectural, and institutional achievements — the preservation of classical learning in Irish and Carolingian monasteries, the construction of the great cathedrals, the invention of the university, the development of common law, and the agricultural and commercial revolution of the High Middle Ages.",
    "causes": [
      "The collapse of Western Roman imperial authority (476 CE) — the deposition of the last Western Roman emperor and the fragmentation of the imperial administrative structure into Germanic successor kingdoms — created the political and cultural conditions that marked the beginning of what European historiography calls the Middle Ages.",
      "The Christianisation of Europe — completed across most of the continent by approximately 1000 CE — created the institutional, intellectual, and cultural framework that unified medieval European civilisation and gave it its distinctive character, distinct from both the pagan Roman past and the Islamic and Byzantine contemporaries.",
      "The Islamic conquests of the 7th–8th centuries CE — which transformed the Mediterranean world by permanently separating the European north from the African south and redirecting trade and cultural exchange — fundamentally shaped the economic and intellectual conditions of early medieval Europe."
    ],
    "effects": [
      "The medieval period produced the institutional infrastructure of modern European civilisation — the Roman Catholic Church and its canon law, the university system (Bologna, Paris, Oxford), parliamentary assemblies (the English Parliament, the Cortes, the Estates-General), and the common law tradition — all of which have direct continuity with the modern world.",
      "Medieval agricultural and commercial innovation — the three-field system, the heavy plough, the windmill, and the commercial revolution of the 12th–13th centuries — produced the population growth and economic expansion that made possible the Renaissance and early modern transformations of European society.",
      "The Black Death (1347–1351) — which killed approximately 30–50% of Europe's population — was the most catastrophic demographic event in European history and produced social, economic, religious, and cultural transformations (labour scarcity, peasant revolts, questioning of religious authority) that directly contributed to the crises of the late medieval period and the conditions that produced both the Renaissance and the Reformation."
    ],
    "relationships": [
      {"sourceSlug": "middle-ages", "sourceName": "Middle Ages", "verb": "FOLLOWS", "targetSlug": "roman-empire", "targetName": "Roman Empire", "context": "The Middle Ages conventionally begin with the collapse of the Western Roman Empire (476 CE) — the fall of Roman imperial authority that the humanists used to define the start of the 'middle' period."},
      {"sourceSlug": "middle-ages", "sourceName": "Middle Ages", "verb": "PRECEDES", "targetSlug": "renaissance", "targetName": "Renaissance", "context": "The Middle Ages end with the Renaissance — the Italian humanist recovery of classical culture that defined itself precisely as a break from the medieval period, giving the 'Middle Ages' its very name."},
      {"sourceSlug": "black-death", "sourceName": "Black Death (1347–1351)", "verb": "TRANSFORMS", "targetSlug": "middle-ages", "targetName": "Late Middle Ages", "context": "The Black Death — killing 30–50% of Europe's population — was the catastrophic event that most dramatically shaped the Late Middle Ages, producing the demographic, social, and cultural transformations that ended the medieval equilibrium."}
    ],
    "places": [
      {"name": "Western Europe", "role": "The primary geographic reference of the conventional 'Middle Ages' — the territories of the former Western Roman Empire where medieval European civilisation developed"},
      {"name": "Constantinople (Byzantine Empire)", "role": "The eastern continuation of Roman civilisation that persisted through the medieval period until 1453 CE — a parallel medieval civilisation that shaped European history through religious controversy, intellectual preservation, and military interaction"},
      {"name": "Mediterranean World", "role": "The geographic context within which medieval European, Byzantine, and Islamic civilisations interacted — trade routes, crusades, and intellectual exchange crossed this space throughout the medieval period"}
    ],
    "subjects": ["Medieval History", "European History", "Medieval Era", "Historiography", "World History", "Classical Era", "Periodisation", "Historical Framework"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Middle Ages is the historiographical framework for approximately a millennium of European history (c. 500–1500 CE) — the period that produced the institutional foundations of modern European civilisation: the Catholic Church, the university system, parliamentary governance, common law, and the Gothic cathedral. The very concept of the 'Middle Ages' — coined by Renaissance humanists to distinguish antiquity and their own era from the 'middle' period — is itself a major historiographical construct that has profoundly shaped how western civilisation understands its own history.",
      "significanceCategory": "world-changing"
    }
  }
},

"hortar": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221hortar.json",
  "slug": "hortar",
  "data": {
    "summary": "Hortarius (also Hortar; died 364 CE) was an Alamannic king who led his people against the Roman Empire in the mid-4th century CE and was defeated at the decisive Battle of Strasbourg (357 CE), also known as the Battle of Argentoratum — one of the most significant Roman military victories of the 4th century, fought by the Caesar Julian (later Julian the Apostate) against a coalition of Alamannic kings on the Rhine frontier. Hortarius was among the Alamannic kings who participated in the 357 CE alliance that attempted to exploit Roman internal political weakness (the usurpation of Magnentius, 350–353 CE) to establish Alamannic control over Roman Gaul. Julian's decisive victory at Strasbourg — in which a Roman army of approximately 13,000 defeated an Alamannic coalition of approximately 35,000 — ended Alamannic penetration of Gaul and re-established Roman Rhine frontier security.\n\nFollowing the Battle of Strasbourg, Hortarius submitted to Julian and became a client king of Rome — a relationship typical of the Roman Empire's frontier management in which defeated barbarian kings were incorporated into the Roman military and diplomatic system. In the years following the battle, Julian conducted campaigns that forced the Alamanni to restore Roman prisoners and provide grain for the Roman Rhine frontier garrisons, and Hortarius's subordinate position as a Roman client was part of this post-battle settlement. Julian's Rhine campaigns (357–359 CE) are documented by Ammianus Marcellinus, the most important historian of the 4th century, whose account of the Battle of Strasbourg is one of the most vivid battle descriptions to survive from antiquity.\n\nHortarius's death in 364 CE — noted by Ammianus — marks the end of his documented career. He represents the type of barbarian king who played a significant role in the Roman frontier system of the later 4th century: neither fully Roman nor simply an external enemy, but a client ruler whose relationship with Rome was one of coerced cooperation under the implicit threat of Roman military force.",
    "causes": [
      "The usurpation of Magnentius in the Western Roman Empire (350–353 CE) — which diverted Roman military attention to civil war — created the opportunity that Hortarius and other Alamannic kings exploited to raid deeply into Roman Gaul, establishing the Alamannic presence on the left bank of the Rhine that Julian would reverse.",
      "The Alamannic peoples' demographic pressure and desire for agricultural land in the Rhine valley — the fundamental economic driver of Germanic migration pressure on the Roman Rhine frontier throughout the 3rd–5th centuries — motivated the military coalition that Hortarius led against Rome.",
      "Julian's appointment as Caesar for Gaul (355 CE) by Emperor Constantius II — and his subsequent military campaigns — created the Roman military response that culminated in the Battle of Strasbourg and Hortarius's defeat and submission."
    ],
    "effects": [
      "Hortarius's defeat at Strasbourg (357 CE) was a significant Roman military success that stabilised the Rhine frontier and demonstrated Julian's military capability — contributing to Julian's growing popularity with the Roman army that would eventually lead to his proclamation as Augustus (360 CE) and his brief reign as emperor (361–363 CE).",
      "The post-Strasbourg settlement — including Hortarius's client relationship with Julian and the Roman recovery of prisoners and grain supplies — temporarily restored Roman Rhine frontier security and forced the Alamanni back across the Rhine.",
      "Hortarius's career as documented by Ammianus Marcellinus illustrates the functioning of the Roman imperial frontier system in the 4th century — the combination of military force and diplomatic client relationships through which Rome managed the Germanic peoples along its northern boundaries."
    ],
    "relationships": [
      {"sourceSlug": "hortar", "sourceName": "Hortarius", "verb": "DEFEATED_BY", "targetSlug": "julian-the-apostate", "targetName": "Julian the Apostate (Caesar)", "context": "Hortarius was among the Alamannic kings defeated by Julian at the Battle of Strasbourg (357 CE) — the decisive Roman victory that ended Alamannic penetration of Gaul and launched Julian's career as a successful Roman commander."},
      {"sourceSlug": "battle-of-strasbourg", "sourceName": "Battle of Strasbourg (357 CE)", "verb": "DEFINES", "targetSlug": "hortar", "targetName": "Hortarius", "context": "The Battle of Strasbourg was the defining event of Hortarius's documented career — as one of the Alamannic leaders in the coalition that Julian defeated, his subsequent submission and client status shaped his remaining years."},
      {"sourceSlug": "ammianus-marcellinus", "sourceName": "Ammianus Marcellinus", "verb": "RECORDS", "targetSlug": "hortar", "targetName": "Hortarius", "context": "Ammianus Marcellinus — the primary 4th-century historian — records Hortarius's career in his account of Julian's Rhine campaigns, providing the main documentary evidence for his existence and role."}
    ],
    "places": [
      {"name": "Strasbourg (Argentoratum), Rhine frontier", "role": "The site of the Battle of Strasbourg (357 CE) — the decisive defeat of the Alamannic coalition by Julian that ended Hortarius's independent military challenge to Rome"},
      {"name": "Rhine Valley, Roman Empire / Alamannia", "role": "The frontier zone of Hortarius's world — the Rhine river as the boundary between Roman Gaul and the Germanic territories, the zone of conflict and client relationships that defined his career"}
    ],
    "subjects": ["Alamanni", "Late Roman Empire", "Classical Era", "Germanic Peoples", "Roman Frontier", "Ancient History", "Julian the Apostate", "4th Century CE"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Hortarius was an Alamannic king defeated by Julian at the Battle of Strasbourg (357 CE) — one of the documented barbarian leaders in the Roman frontier system whose career illustrates the combination of military confrontation and client relationships through which Rome managed the Rhine boundary in the 4th century. His significance is primarily as evidence for 4th-century Alamannic political leadership and Roman frontier management.",
      "significanceCategory": "local"
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
