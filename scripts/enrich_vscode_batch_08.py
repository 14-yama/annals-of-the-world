#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 08 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: johann-pfeffinger, andrea-dittis, lucius-lucretius-flavus-tricipitinus,
          saint-marcouf, gaius-sallustius-crispus-passienus,
          marcus-popillius-laenas, felician-of-foligno,
          luis-antonio-belluga-y-moncada
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-08-may2026"

ENRICHMENTS = {

"johann-pfeffinger": {
  "filepath": "data/appwrite-export/entities/252-Class-252/252johann-pfeffinger.json",
  "slug": "johann-pfeffinger",
  "data": {
    "summary": "Johann Pfeffinger (1493–1573) was a German Lutheran theologian and one of the first major expositors of Philippism — the moderate theological tendency associated with Philip Melanchthon that sought to soften Luther's strict doctrinal positions, particularly on free will and the role of human cooperation in salvation. A student of Luther and Melanchthon at Wittenberg, Pfeffinger served as superintendent in Leipzig and became one of the most significant theologians in Electoral Saxony during the mid-16th century. His career was defined by the fierce theological controversies that divided Lutheranism after Luther's death (1546): the Adiaphora Controversy (1548–1555), the Osiandrian Controversy, the Majorist Controversy, and above all the Synergist Controversy in which his own theological positions were a central flashpoint.\n\nPfeffinger's major theological contribution — and the controversy it provoked — centred on his 1555 treatise 'De Libero Arbitrio' (On Free Will), in which he argued that the human will retains a limited capacity to cooperate with the Holy Spirit in conversion (synergism), drawing on Melanchthon's later theology that had softened Luther's absolute rejection of free will. This position made him the principal target of the strict Lutherans (Gnesio-Lutherans) — particularly Matthias Flacius Illyricus and Nikolaus von Amsdorf — who accused him of reverting to the semi-Pelagianism that Luther had combated in his 'De Servo Arbitrio' (On the Bound Will, 1525). The Synergist Controversy became one of the bitterest theological disputes in Lutheran history and directly contributed to the Formula of Concord (1577) — the definitive Lutheran confessional statement that resolved the dispute four years after Pfeffinger's death.\n\nPfeffinger also participated in the Adiaphora Controversy — the dispute over whether Lutheran churches could accept certain Catholic ceremonies under political pressure (the Leipzig Interim, 1548) as 'adiaphora' (indifferent matters). He was accused of excessive accommodation to imperial demands, further placing him among the 'moderate' or 'syncretic' wing of Lutheranism that the Gnesio-Lutherans attacked as betrayers of the Reformation.",
    "causes": [
      "Melanchthon's theological evolution — particularly his later editions of the Loci Communes which introduced greater nuance on free will than Luther's absolute position — provided Pfeffinger with the theological precedent for his synergist position, making him a representative of Philippism within the Lutheran movement.",
      "The political pressures of the Augsburg Interim (1548) and Leipzig Interim (1548) — Emperor Charles V's attempts to impose a compromise settlement on the Lutheran territories — forced Lutheran theologians to choose between doctrinal purity and political accommodation, with Pfeffinger choosing a path of limited concession.",
      "The death of Luther (1546) and the subsequent 'Interimist Crisis' created a leadership vacuum in Lutheranism that allowed the disputes latent in Luther's and Melanchthon's different theological tendencies to emerge as open controversies — with Pfeffinger on the Melanchthonian side."
    ],
    "effects": [
      "The Synergist Controversy provoked by Pfeffinger's 'De Libero Arbitrio' (1555) became one of the defining intra-Lutheran theological battles of the later Reformation — contributing to the 'second wave' of confessional formation that ultimately produced the Formula of Concord (1577) and the Book of Concord (1580), which definitively rejected synergism.",
      "Pfeffinger's role as the leading Philippist theologian in Electoral Saxony shaped the theological culture of Leipzig University — one of the most important Lutheran educational centres — during the critical decades of Lutheran consolidation.",
      "The defeat of Philippism in the Formula of Concord established a stricter Augustinian-Lutheran theology of grace that distinguished Lutheranism from both Catholicism and Reformed (Calvinist) Christianity on the question of human will and divine grace — a doctrinal distinction that persists in Lutheran confessional theology."
    ],
    "relationships": [
      {"sourceSlug": "johann-pfeffinger", "sourceName": "Johann Pfeffinger", "verb": "INFLUENCES", "targetSlug": "lutheran-synergism-controversy", "targetName": "Synergist Controversy", "context": "Pfeffinger's 1555 'De Libero Arbitrio' sparked the Synergist Controversy — one of the bitterest intra-Lutheran theological disputes, ultimately resolved by the Formula of Concord (1577)."},
      {"sourceSlug": "philip-melanchthon", "sourceName": "Philip Melanchthon", "verb": "INFLUENCES", "targetSlug": "johann-pfeffinger", "targetName": "Johann Pfeffinger", "context": "Pfeffinger represented Philippism — the moderate Melanchthonian theological tendency — and drew on Melanchthon's later nuanced position on free will in his controversial treatise."},
      {"sourceSlug": "formula-of-concord", "sourceName": "Formula of Concord (1577)", "verb": "REFUTES", "targetSlug": "johann-pfeffinger", "targetName": "Johann Pfeffinger", "context": "The Formula of Concord definitively rejected Pfeffinger's synergist position — establishing strict Lutheran doctrine on the human will's total incapacity without divine grace."}
    ],
    "places": [
      {"name": "Leipzig, Saxony, Germany", "role": "Where Pfeffinger served as Lutheran superintendent — the institutional base from which his Philippist theology shaped Electoral Saxon Lutheranism"},
      {"name": "Wittenberg, Saxony, Germany", "role": "Where Pfeffinger studied under Luther and Melanchthon — the originating context of his theological formation"}
    ],
    "subjects": ["Lutheran Reformation", "Protestant Theology", "Medieval History", "Saxony", "Medieval Era", "Germany", "Church History", "Intellectual History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Johann Pfeffinger was the principal theologian of Philippist Lutheranism whose 'De Libero Arbitrio' (1555) sparked the Synergist Controversy — one of the defining intra-Lutheran doctrinal battles that was resolved only by the Formula of Concord (1577). His career embodied the tension between Luther's strict Augustinianism and Melanchthon's more moderate anthropology that shaped confessional Lutheranism for centuries.",
      "significanceCategory": "significant"
    }
  }
},

"andrea-dittis": {
  "filepath": "data/appwrite-export/entities/202-Class-202/202andrea-dittis.json",
  "slug": "andrea-dittis",
  "data": {
    "summary": "Andrea Dittis (c. 1585–1625), also known as 'China', was a Chinese-born merchant and trader who became one of the most prominent members of the Chinese community in Jacobean London — an early and historically documented instance of a Chinese immigrant achieving social and economic prominence in early modern England. He is remarkable as one of the earliest named and documented Chinese individuals in English history, appearing in court records, City of London registers, and the correspondence of figures including the East India Company. His nickname 'China' (a common English designation for Chinese traders in the period) appears in period documents alongside his Anglicised name, suggesting a degree of social integration while also marking his ethnic distinctiveness.\n\nDittis operated as a merchant in London in the early 17th century, working within the network of trade between England, the Dutch Republic, and Asia that was emerging around the nascent East India Company (founded 1600). He appears to have been well-connected: his name appears in documents relating to Asian trade and he was apparently known to figures in the merchant community. His death in 1625 is recorded in English parish registers — a documentation of his presence in London society at a time when the Chinese community in England was extremely small.\n\nDittis represents a category of historical figure who is significant not for any single act but for what his existence demonstrates: that the global trade networks of the early 17th century were already producing transoceanic migrations that brought Asian individuals to European cities well before the formal colonial structures of the later centuries. His documented presence in London in the 1610s–1620s is evidence that the Asian-European encounter was not limited to colonial frontiers but was creating hybrid social worlds in European metropolitan centres as early as the Jacobean period.",
    "causes": [
      "The founding of the English East India Company (1600) and the Dutch East India Company (1602) created the institutional infrastructure for trans-oceanic trade that brought Asian merchants, sailors, and intermediaries to European port cities — the commercial network within which Dittis operated.",
      "The existing Chinese merchant diaspora in Southeast Asia (particularly in Batavia/Jakarta and Malacca) provided the community networks and commercial connections through which Chinese traders like Dittis could access the European trade system and eventually reach London.",
      "London's emergence as a major centre of global trade in the early 17th century — drawing merchants from across the known world — created the urban environment that could accommodate unusual figures like a Chinese merchant with sufficient commercial ties to survive and be documented."
    ],
    "effects": [
      "Dittis's documented presence in early 17th-century London is primary historical evidence for the extraordinary reach of early modern globalisation — demonstrating that the networks of the nascent Asian trade were already producing Chinese residents in the English capital within a generation of the East India Company's founding.",
      "Court records, city registers, and correspondence documenting Dittis contribute to the fragmentary but growing historical evidence base for the presence of non-European individuals in early modern Europe — evidence that complicates the narrative of Europe's encounter with Asia as purely a story of European expansion.",
      "Dittis's career as a merchant in London established a very early precedent for Chinese participation in European-Asian trade at a metropolitan level — a social phenomenon that the later 17th and 18th centuries would develop significantly, culminating in substantial Chinese communities in European port cities by the 18th century."
    ],
    "relationships": [
      {"sourceSlug": "andrea-dittis", "sourceName": "Andrea Dittis ('China')", "verb": "OCCURS_IN", "targetSlug": "east-india-company", "targetName": "English East India Company", "context": "Dittis operated within the commercial networks of the emerging Asian trade that the East India Company was developing, appearing in documents related to this trade system."},
      {"sourceSlug": "andrea-dittis", "sourceName": "Andrea Dittis ('China')", "verb": "REPRESENTS", "targetSlug": "early-modern-globalisation", "targetName": "Early Modern Globalisation", "context": "Dittis's presence in Jacobean London — as a documented Chinese merchant — is evidence of how early modern trade networks were producing transoceanic migrations that created multicultural urban environments in European cities."}
    ],
    "places": [
      {"name": "London, England", "role": "Where Dittis lived, traded, and died — his documented presence in London parish registers and court records is the primary source for his biography"},
      {"name": "China / Southeast Asia", "role": "Dittis's probable origins — the Chinese merchant diaspora in Southeast Asia was the community network that connected Chinese traders to European commerce"}
    ],
    "subjects": ["Early Modern History", "Global History", "Trade", "Classical Era", "England", "China", "Asian Diaspora", "Early Modern Era"],
    "frameworks": ["WORLD_SYSTEMS", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Andrea Dittis ('China') was one of the earliest documented Chinese residents in English history — a merchant in Jacobean London whose presence in court records and parish registers is evidence of how early modern Asian trade networks were already producing transoceanic migrations to European cities. He represents the human face of early modern globalisation at its earliest stages.",
      "significanceCategory": "local"
    }
  }
},

"lucius-lucretius-flavus-tricipitinus": {
  "filepath": "data/appwrite-export/entities/280-Class-280/280lucius-lucretius-flavus-tricipitinus.json",
  "slug": "lucius-lucretius-flavus-tricipitinus",
  "data": {
    "summary": "Lucius Lucretius Flavus Tricipitinus (fl. 5th century BCE) was a Roman patrician who served as consul of the Roman Republic in 393 BCE, representing one of the traditional Roman patrician families that dominated the early Republican magistracy. The Lucretii were an ancient patrician gens (clan) of the early Republic — closely associated with the foundational period of Roman constitutional history — and multiple members of the family held consulships in the 5th and 4th centuries BCE. The cognomen 'Tricipitinus' appears in several branches of the Lucretii, and the family's political importance is illustrated by the legendary figure Lucretia, whose rape by the Etruscan Tarquinius and subsequent suicide is tradition held responsible for the overthrow of the Roman monarchy and the founding of the Republic in 509 BCE.\n\nThe context of Lucius Lucretius Flavus Tricipitinus's consulship in 393 BCE places him in one of the most turbulent periods of early Roman history: the aftermath of the Gallic sack of Rome (traditionally dated 390 BCE, though the exact date is disputed — Polybius dates it to 387/386 BCE). The Gallic invasion of northern Italy by the Senones under Brennus devastated the Roman army at the Battle of the Allia (18 July, traditionally), followed by the sack and burning of Rome itself — the most catastrophic military defeat in early Roman history and a trauma that shaped Roman military culture and foreign policy for centuries. In this period, the Roman state was engaged in the slow reconstruction of its military capacity, the continuation of the wars against the Volsci and Aequi, and the political tensions of the Struggle of the Orders (the conflict between patricians and plebeians over political rights).\n\nAs a figure of the early Republic, Lucius Lucretius Flavus Tricipitinus is primarily known through the surviving fasti consulares (the consular lists) that were compiled and preserved in the Roman tradition. Individual consuls of this early period are often poorly documented beyond their names and dates, but their accumulation in the fasti represents the Roman commitment to recording the annual magistracy as a form of civic identity.",
    "causes": [
      "The patrician dominance of the early Republic's consulship — the result of the social settlement after the overthrow of the Tarquins — meant that men like Lucius Lucretius Flavus Tricipitinus, from established patrician gentes, routinely occupied the senior magistracy in the 5th–4th centuries BCE.",
      "The Gallic sack of Rome (c. 390–387 BCE) and its aftermath — military rebuilding, financial recovery, diplomatic realignment — shaped the political agenda of the consuls of this period, creating the institutional context of Tricipitinus's magistracy.",
      "The Struggle of the Orders — the plebeian challenge to patrician exclusivity in the consulship, ultimately resolved by the Licinio-Sextian laws of 367 BCE — was the defining constitutional conflict of early Republican politics, making patrician consuls like Tricipitinus representatives of the contested political order."
    ],
    "effects": [
      "The annual consulship — of which Lucius Lucretius Flavus Tricipitinus's 393 BCE tenure is one recorded instance — was the core magistracy of the Roman Republic, and the accumulated record of consuls in the fasti provided Roman civic identity with its principal chronological framework, dating events 'in the consulship of X and Y'.",
      "The Lucretii's long presence in the Republican consular class contributed to the entrenchment of patrician political leadership in the generations before the Licinio-Sextian compromise (367 BCE) that finally opened the consulship to plebeians.",
      "The reconstruction of Rome after the Gallic sack (in which the consuls of the 390s–380s BCE played central roles) laid the institutional foundations for the Roman military expansion of the 4th–3rd centuries BCE that would eventually produce the Mediterranean empire."
    ],
    "relationships": [
      {"sourceSlug": "lucius-lucretius-flavus-tricipitinus", "sourceName": "Lucius Lucretius Flavus Tricipitinus", "verb": "REPRESENTS", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "As consul in 393 BCE, Tricipitinus was one of the two supreme magistrates of the early Republic — representing the patrician-dominated consular class that governed Rome in the century before the Licinio-Sextian reforms."},
      {"sourceSlug": "gallic-sack-of-rome", "sourceName": "Gallic Sack of Rome (c. 390 BCE)", "verb": "SHAPES", "targetSlug": "lucius-lucretius-flavus-tricipitinus", "targetName": "Lucius Lucretius Flavus Tricipitinus", "context": "Tricipitinus's consulship in 393 BCE places him in the immediate aftermath of the Gallic sack — the period of Roman military reconstruction that shaped the agenda of consuls in this decade."},
      {"sourceSlug": "lucretia", "sourceName": "Lucretia", "verb": "PRECEDES", "targetSlug": "lucius-lucretius-flavus-tricipitinus", "targetName": "Lucius Lucretius Flavus Tricipitinus", "context": "Lucretia — the legendary Lucretian ancestor whose story tradition links to the founding of the Republic — was part of the same gens Lucretia that produced Tricipitinus a century later."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "The city whose annual magistracy Lucius Lucretius Flavus Tricipitinus served as consul — Rome in 393 BCE was in the early phase of reconstruction after the Gallic sack"}
    ],
    "subjects": ["Roman Republic", "Classical Rome", "Political History", "Classical Era", "Italy", "Ancient History", "Constitution", "Roman Magistracy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Lucius Lucretius Flavus Tricipitinus was a Roman consul of 393 BCE, representing the patrician Lucretii clan that helped define the early Republic's magistracy. His tenure placed him in the critical aftermath of the Gallic sack of Rome — the period of reconstruction that shaped the Roman military and institutional framework for subsequent expansion. He is primarily significant as a member of the fasti consulares that provided the Roman Republic with its chronological and civic identity.",
      "significanceCategory": "local"
    }
  }
},

"saint-marcouf": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250saint-marcouf.json",
  "slug": "saint-marcouf",
  "data": {
    "summary": "Saint Marcouf (also Marculf, Marculphus; c. 490–558 CE), was a 6th-century Frankish abbot and monastic founder in Normandy whose post-mortem cult acquired a remarkable royal association: his relics were used in the coronation ceremonies of French kings for centuries, as the royal 'touching for scrofula' (the king's evil) was traditionally preceded or accompanied by veneration of Saint Marcouf's relics. This association between a Norman monastic saint and the most symbolic expression of French royal theocratic power — the miraculous healing of scrofula by the king's touch, which was presented as evidence of divine mandate — made Marcouf one of the minor but distinctively important figures in the history of medieval French kingship.\n\nBorn in Bayeux of a noble family, Marcouf was ordained a priest and initially served in the pastoral ministry of the Cotentin peninsula in northwestern Normandy. He later established a monastery on the island of Nanteuil (near Coutances), creating one of the monastic communities that were multiplying across Frankish Gaul in the 6th century as the Merovingian church built its institutional infrastructure. He had a reputation for asceticism and miraculous healing during his lifetime, which formed the basis of his post-mortem cult. His monastery at Nanteuil (later known as Saint-Marcouf) became a centre of pilgrimage and preserved his relics, which were translated several times during the Norman Invasions and the Carolingian period.\n\nThe royal association came through the transfer of his relics to Corbeny (in the Aisne), near Laon, in the 9th century — the site was close enough to Reims, the coronation city of French kings, to become incorporated into the coronation ritual. From the Capetian period onward, newly crowned French kings made a pilgrimage to Corbeny to touch Marcouf's relics before performing the royal touching for scrofula — a ceremony that Marc Bloch analysed in his landmark study 'The Royal Touch' (1924) as evidence for the sacred character attributed to medieval kingship.",
    "causes": [
      "The 6th-century Merovingian expansion of monasticism in Gaul — driven by the Irish-Frankish monastic reform tradition and the patronage of the Merovingian royal house — created the institutional context in which Marcouf founded his Norman monastery and acquired his reputation for holiness.",
      "The 9th-century Viking raids on Normandy (which began in 820 CE) forced the translation of Marcouf's relics to inland sites for safety — the transfer to Corbeny created the geographic proximity to Reims that enabled the royal association.",
      "The Capetian monarchy's construction of a sacral kingship ideology — combining anointing at Reims, Sainte-Ampoule holy oil tradition, and the royal healing touch — created institutional demand for saintly associations that reinforced the king's sacred character, into which Marcouf's cult was incorporated."
    ],
    "effects": [
      "The royal pilgrimage to Corbeny before the king's touching for scrofula — a ceremony performed by French kings from the Capetian period through Louis XVI — made Marcouf's name known throughout France as a saint associated with royal miraculous power, giving a minor Norman abbot a peculiar national significance.",
      "Marc Bloch's analysis of the royal touching ceremony (including Marcouf's role) in 'Les Rois Thaumaturges' (1924) — a founding text of the Annales school of historical sociology — made Marcouf a subject of major historical scholarship, embedding his cult in the historiography of medieval political religion.",
      "The transfer and preservation of Marcouf's relics across multiple sites in Normandy and Picardy is evidence for the logistics of relic translation during the Viking invasions — a process that shaped the regional distribution of sacred geography in northern France."
    ],
    "relationships": [
      {"sourceSlug": "saint-marcouf", "sourceName": "Saint Marcouf", "verb": "ENABLES", "targetSlug": "royal-touch-ceremony", "targetName": "French Royal Touching for Scrofula", "context": "Marcouf's relics at Corbeny were venerated by newly crowned French kings before the royal touching ceremony — his cult was incorporated into the sacral kingship ritual that claimed divine endorsement of royal power."},
      {"sourceSlug": "saint-marcouf", "sourceName": "Saint Marcouf", "verb": "INFLUENCES", "targetSlug": "marc-bloch", "targetName": "Marc Bloch", "context": "Marc Bloch's landmark historical study 'The Royal Touch' (1924) — one of the founding texts of the Annales school — analysed the royal touching ceremony including Marcouf's role, making him central to the historiography of sacred kingship."},
      {"sourceSlug": "merovingian-church", "sourceName": "Merovingian Church", "verb": "PRODUCES", "targetSlug": "saint-marcouf", "targetName": "Saint Marcouf", "context": "Marcouf's monastic career — founded in the Merovingian church's 6th-century expansion of Norman monasticism — was the institutional context of his holiness and cult."}
    ],
    "places": [
      {"name": "Nanteuil (near Coutances), Normandy, France", "role": "Site of Marcouf's monastery — the institution he founded and where his cult originated before the Viking invasions forced the translation of his relics"},
      {"name": "Corbeny, Aisne, France", "role": "Final destination of Marcouf's translated relics — the site near Reims incorporated into the French royal coronation ritual for centuries"}
    ],
    "subjects": ["Hagiography", "Medieval France", "Church History", "Classical Era", "Normandy", "Medieval Era", "Kingship", "Merovingian History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Saint Marcouf was a 6th-century Norman abbot whose relics, transferred to Corbeny near Reims, became incorporated into the French royal coronation ritual — the touching for scrofula ceremony that French kings performed from the Capetians through Louis XVI as evidence of divine mandate. Marc Bloch's analysis of this ceremony in 'The Royal Touch' (1924) made Marcouf central to the historiography of medieval sacred kingship.",
      "significanceCategory": "regional"
    }
  }
},

"gaius-sallustius-crispus-passienus": {
  "filepath": "data/appwrite-export/entities/280-Class-280/280gaius-sallustius-crispus-passienus.json",
  "slug": "gaius-sallustius-crispus-passienus",
  "data": {
    "summary": "Gaius Sallustius Crispus Passienus (c. 1 CE–47 CE), commonly known as Passienus Crispus, was a Roman orator, politician, and wit of the early Principate — a figure whose reputation for brilliant improvised oratory and sharp humour made him one of the most celebrated conversationalists of the Julio-Claudian court. He served as consul twice (consul ordinarius in 27 CE and suffect consul in 44 CE), governed Asia as proconsul, and was notably twice married: first to Domitia (sister of the emperor Domitian's father, Domitius Ahenobarbus), and second to Agrippina the Younger — the future mother of the Emperor Nero and one of the most powerful women in Roman imperial history. His second marriage, by which he passed his substantial fortune to Agrippina, was particularly significant: Passienus died in 47 CE (reportedly poisoned, possibly by Agrippina), and his wealth helped finance Agrippina's subsequent political rise and ultimately contributed to Nero's imperial succession.\n\nPassienus Crispus was the adopted son of Gaius Sallustius Crispus (the historian Sallust's great-nephew, a powerful Augustan-era adviser), from whom he inherited both name and property. His reputation rests primarily on his wit: the elder Pliny and Quintilian both preserve examples of his sharp repartee, including his famous reply to the emperor Caligula who boasted of not having slept with his sisters (as incest was alleged) — 'You haven't yet, sire' (a remark that somehow did not cost him his life). This anecdote captures the dangerous comedy of the Julio-Claudian court, where wit was both currency and peril.\n\nPassienus Crispus is a figure of the nexus between Roman oratorical culture, dynastic court politics, and the extraordinary women of the Julio-Claudian family — his career illustrates how wealth, eloquence, and advantageous marriage connected the senatorial elite to imperial power in ways that shaped succession and policy.",
    "causes": [
      "The Julio-Claudian court's culture of literary and oratorical display — in which brilliant improvised wit was a form of social capital and a pathway to imperial favour — created the environment in which Passienus Crispus's reputation as an orator could translate into political prominence.",
      "The adoption system of the Roman elite — through which Passienus inherited the name, property, and connections of the Sallustian family — provided the financial and social base for his political career and his attractiveness as a marriage partner for Agrippina the Younger.",
      "Agrippina the Younger's calculated use of marriage as a political tool — having already been widowed from Gnaeus Domitius Ahenobarbus (Nero's father) — made Passienus Crispus's wealth and connections valuable to her succession strategy for her son Nero."
    ],
    "effects": [
      "Passienus Crispus's fortune, inherited by Agrippina after his death (47 CE), provided the financial resources that supported her political strategy in the final years of Claudius's reign — including her cultivation of the praetorian guard and court factions that ultimately placed Nero on the throne.",
      "His posthumous reputation as one of the great wits of the Julio-Claudian period preserved several anecdotes (in Pliny, Quintilian, Suetonius) that are primary sources for the social and conversational culture of the early Principate.",
      "The pattern of Passienus Crispus's career — twice consul, proconsul of Asia, intimate of the imperial court, married to an emperor's relative — illustrates the social mechanisms by which senatorial wealth and oratorical reputation were converted into political access in the early Empire."
    ],
    "relationships": [
      {"sourceSlug": "gaius-sallustius-crispus-passienus", "sourceName": "Passienus Crispus", "verb": "MARRIED_TO", "targetSlug": "agrippina-the-younger", "targetName": "Agrippina the Younger", "context": "Passienus Crispus's second marriage to Agrippina the Younger transferred his substantial fortune to her on his death (47 CE), financing her political rise and contributing to Nero's subsequent succession."},
      {"sourceSlug": "gaius-sallustius-crispus-passienus", "sourceName": "Passienus Crispus", "verb": "OCCURS_IN", "targetSlug": "julio-claudian-dynasty", "targetName": "Julio-Claudian Dynasty", "context": "Passienus Crispus navigated the dangerous court culture of the Julio-Claudian emperors — surviving Caligula's court with his famous riposte and playing a significant role in the dynastic politics of Claudius's reign."},
      {"sourceSlug": "sallust", "sourceName": "Sallust (historian)", "verb": "PRECEDES", "targetSlug": "gaius-sallustius-crispus-passienus", "targetName": "Passienus Crispus", "context": "The Sallustian family fortune passed through Gaius Sallustius Crispus (Augustus's adviser) to Passienus Crispus — a transmission of wealth and name that provided the foundation for Passienus's political and social career."}
    ],
    "places": [
      {"name": "Rome, Italy (Julio-Claudian court)", "role": "The site of Passienus Crispus's oratorical reputation, political career, and his two significant marriages — the social world of the early imperial court"},
      {"name": "Asia (province)", "role": "Where Passienus Crispus served as proconsul — his administrative record in one of the empire's most prosperous provinces"}
    ],
    "subjects": ["Roman Empire", "Classical Rome", "Oratory", "Classical Era", "Julio-Claudian Dynasty", "Political History", "Marriage Politics", "Ancient History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Passienus Crispus was the twice-consul Roman orator whose wit made him famous at the Julio-Claudian court and whose wealth, inherited by Agrippina the Younger on his death (47 CE), helped finance Nero's imperial succession. He is the human nexus between Roman oratorical culture, dynastic marriage politics, and the extraordinary power of Julio-Claudian women — a case study in how eloquence and fortune translated into court influence.",
      "significanceCategory": "local"
    }
  }
},

"marcus-popillius-laenas": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220marcus-popillius-laenas.json",
  "slug": "marcus-popillius-laenas",
  "data": {
    "summary": "Marcus Popillius Laenas (fl. 3rd–2nd century BCE) was a Roman consul and general whose family — the Popillii Laenates — was one of the plebeian gentes that rose to consular prominence in the middle Republic period following the Licinio-Sextian reforms (367 BCE) that opened the consulship to plebeians. The cognomen 'Laenas' (from the Latin for a woollen cloak) was characteristic of this branch of the Popillia gens. The most famous incident associated with the broader Laenas family is the 'Day of Eleusis' (168 BCE), when the Roman legate Gaius Popillius Laenas drew a circle in the sand around King Antiochus IV of Syria and demanded he make his decision about withdrawing from Egypt before stepping out of it — an act of extraordinary Roman diplomatic assertiveness that became a byword for ultimatum diplomacy. Marcus Popillius Laenas, an earlier member of the same family, represents the consular tradition from which this later notoriety emerged.\n\nThe Popillii Laenates provide an instructive example of the rise of the 'new' plebeian nobility of the middle Republic — families that had no consular tradition before the Licinio-Sextian reforms but who, within two generations, established themselves as regular participants in the consular class. Marcus Popillius Laenas served as consul in 359, 356, 354, and 350 BCE — a remarkable four consulships that indicate extraordinary political standing in the turbulent mid-4th century BCE, a period of significant military pressure on Rome from the Gauls, Latins, and Italian peoples.\n\nHis multiple consulships place him in the period of Roman expansion in central Italy — the decades in which Rome consolidated its dominance of the Latin League and began the expansion that would eventually encompass all of Italy. The military campaigns of consuls like Marcus Popillius Laenas against Rome's Italian neighbours were the building blocks of the Roman territorial state that eventually created the Mediterranean empire.",
    "causes": [
      "The Licinio-Sextian reforms (367 BCE) that opened the consulship to plebeians created the constitutional framework within which the Popillii Laenates could rise to consular prominence — Marcus Popillius Laenas was among the first generation of plebeian consuls in the newly reformed Republic.",
      "The military pressures of the mid-4th century BCE — from Gallic incursions, Latin uprisings, and the pressure of the Samnite peoples in central Italy — required experienced military commanders, which gave capable generals like Marcus Popillius Laenas the opportunity to accumulate multiple consulships.",
      "The competitive dynamics of the Roman senatorial elite in the middle Republic — where military reputation was the primary currency of political advancement — rewarded consuls who demonstrated battlefield success with repeat magistracies."
    ],
    "effects": [
      "Marcus Popillius Laenas's four consulships contributed to the Roman military campaigns of the mid-4th century BCE that progressively consolidated Roman dominance in central Italy — the territorial accumulation that eventually produced Roman hegemony over the peninsula.",
      "The Popillii Laenates' establishment as a prominent consular family in the mid-4th century BCE provided the lineage and political capital from which the later Gaius Popillius Laenas (of 'Day of Eleusis' fame) descended — linking Marcus's political achievement to one of the most celebrated acts of Roman diplomacy.",
      "His career illustrates the integration of the new plebeian nobility into the Roman consular class — a social transformation that permanently expanded the political base of the Republic and created the more inclusive 'nobility' of the middle and late Republic."
    ],
    "relationships": [
      {"sourceSlug": "marcus-popillius-laenas", "sourceName": "Marcus Popillius Laenas", "verb": "REPRESENTS", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "As consul four times (359, 356, 354, 350 BCE), Marcus Popillius Laenas was a member of the new plebeian nobility created by the Licinio-Sextian reforms — one of the expanding consular class of the middle Republic."},
      {"sourceSlug": "licinio-sextian-laws", "sourceName": "Licinio-Sextian Laws (367 BCE)", "verb": "ENABLES", "targetSlug": "marcus-popillius-laenas", "targetName": "Marcus Popillius Laenas", "context": "The Licinio-Sextian reforms that opened the consulship to plebeians created the constitutional framework within which the Popillii Laenates rose to consular prominence."},
      {"sourceSlug": "marcus-popillius-laenas", "sourceName": "Marcus Popillius Laenas", "verb": "PRECEDES", "targetSlug": "gaius-popillius-laenas", "targetName": "Gaius Popillius Laenas", "context": "Marcus Popillius Laenas was an ancestor of Gaius Popillius Laenas — the legate whose 'circle in the sand' ultimatum to Antiochus IV (168 BCE) became one of the most famous acts of Roman diplomacy."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "Where Marcus Popillius Laenas held his four consulships and participated in the political and military governance of the mid-Republic"}
    ],
    "subjects": ["Roman Republic", "Classical Rome", "Political History", "Classical Era", "Roman Magistracy", "Military History", "Ancient History", "Italy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Marcus Popillius Laenas was a four-time consul of the Roman Republic in the mid-4th century BCE — one of the first generation of the new plebeian nobility created by the Licinio-Sextian reforms. His multiple consulships placed him at the centre of Rome's 4th-century Italian consolidation and his family lineage connects to Gaius Popillius Laenas, famous for the 'circle in the sand' ultimatum to Antiochus IV in 168 BCE.",
      "significanceCategory": "local"
    }
  }
},

"felician-of-foligno": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250felician-of-foligno.json",
  "slug": "felician-of-foligno",
  "data": {
    "summary": "Saint Felician of Foligno (c. 160–249 CE) was according to tradition the first bishop of Foligno in Umbria (central Italy) and a Christian martyr of the mid-3rd century, whose legendary episcopate of over 56 years — from the reign of Marcus Aurelius to the persecution of the Emperor Decius — represents one of the longest claimed episcopal tenures in early Christian hagiographic tradition. If the legendary dates are accepted, Felician was ordained by Pope Victor I (c. 189–199) and served Foligno and surrounding Umbrian towns as bishop throughout the era of the Severan dynasty and the Crisis of the Third Century, dying as a martyr under the Decian persecution (249–251 CE) — the first empire-wide systematic persecution of Christianity.\n\nAccording to the 'Acts of Saint Felician', he was born into a Roman Christian family, consecrated bishop by Pope Victor I, and spent his extraordinarily long episcopate evangelising the towns of Umbria (Foligno, Bevagna, Spello, Trevi, Montefalco). Arrested during the Decian persecution at approximately 94 years of age, he reportedly survived torture and was beheaded on 24 January 249 CE. His remains were venerated at Foligno, where he became the patron saint of the city. The Cathedral of Foligno is dedicated to him, and his feast day (24 January) was observed throughout medieval central Italy.\n\nFelician is a representative figure of the 3rd-century Latin church of central Italy — the generation of bishops who built Christianity's institutional presence in smaller Italian cities before the Constantinian recognition of 313 CE. The historical verifiability of his specific dates is uncertain (the 56-year episcopate is almost certainly exaggerated in hagiographic tradition), but the social reality he represents — Christian communities establishing themselves across Umbrian towns in the 2nd–3rd centuries, building episcopal structures, and providing martyrs for the Decian persecution — is historically attested.",
    "causes": [
      "The expansion of Christianity through the cities of central Italy in the 2nd–3rd centuries — spread along the trade routes of the Roman road system (via Flaminia passed through Foligno) — created the urban Christian communities that required episcopal organisation of the type Felician's tradition represents.",
      "The Decian persecution (249–251 CE) — the first systematic empire-wide anti-Christian campaign, which required all citizens to sacrifice to Roman gods and produced the certificates (libelli) that documented compliance — generated a large number of martyrs across the empire, including figures like Felician who became the foundation stones of local church traditions.",
      "The 3rd-century episcopal structure of the Italian church — in which bishop-founders of individual cities became the institutional anchors of civic Christian identity — created the social demand for founding bishop traditions like that of Felician at Foligno."
    ],
    "effects": [
      "Felician's cult as patron saint of Foligno provided the foundational sacred identity of the city's Christian community through the medieval period — his relics at the Cathedral of Foligno anchored local religious devotion and civic identity for over a millennium.",
      "The hagiographic tradition of Felician contributed to the 3rd-century martyrology that was a primary cultural resource of medieval Christianity — the stories of early bishops who suffered under Roman persecution were the foundational narratives of Christian civic identity throughout medieval Italy.",
      "As a figure of the Decian martyrdom tradition, Felician represents the decisive moment in early Christianity when the refusal to comply with Roman civic religion was systematised as both persecution and martyrdom — the confrontation that clarified the incompatibility of Christianity with Roman religious pluralism and set the stage for the later Constantinian settlement."
    ],
    "relationships": [
      {"sourceSlug": "felician-of-foligno", "sourceName": "Saint Felician of Foligno", "verb": "FOUNDS", "targetSlug": "diocese-of-foligno", "targetName": "Diocese of Foligno", "context": "Felician is venerated as the founding bishop of Foligno — the first bishop who established Christianity's institutional presence in the Umbrian city that became his primary cult centre."},
      {"sourceSlug": "decian-persecution", "sourceName": "Decian Persecution (249–251 CE)", "verb": "KILLS", "targetSlug": "felician-of-foligno", "targetName": "Saint Felician of Foligno", "context": "The Decian persecution — the first systematic empire-wide Christian persecution — produced Felician's martyrdom, which became the foundational sacred event of Foligno's civic Christian identity."},
      {"sourceSlug": "pope-victor-i", "sourceName": "Pope Victor I", "verb": "ORDAINS", "targetSlug": "felician-of-foligno", "targetName": "Saint Felician of Foligno", "context": "According to hagiographic tradition, Felician was consecrated bishop by Pope Victor I (c. 189–199) — placing his ordination in the late 2nd century and the beginning of his extraordinarily long legendary episcopate."}
    ],
    "places": [
      {"name": "Foligno, Umbria, Italy", "role": "The city of Felician's episcopate and martyrdom — where his relics are venerated at the Cathedral and where he remains patron saint"},
      {"name": "Umbria, central Italy", "role": "The region of Felician's legendary evangelisation — Bevagna, Spello, Trevi, and Montefalco were all reportedly within his missionary and episcopal territory"}
    ],
    "subjects": ["Early Christianity", "Church History", "Martyrology", "Classical Era", "Italy", "Hagiography", "Roman Persecution", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Saint Felician of Foligno was the legendary founding bishop of Foligno and a martyr of the Decian persecution (249 CE) — one of the representative figures of the 3rd-century Italian church that established Christianity's institutional presence in smaller cities before Constantine. His 56-year legendary episcopate became the foundational sacred narrative of Foligno's civic Christian identity for over a millennium.",
      "significanceCategory": "local"
    }
  }
},

"luis-antonio-belluga-y-moncada": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220luis-antonio-belluga-y-moncada.json",
  "slug": "luis-antonio-belluga-y-moncada",
  "data": {
    "summary": "Luis Antonio Belluga y Moncada (1662–1743) was a Spanish cardinal, Bishop of Cartagena (1705–1724), and one of the most significant ecclesiastical and political figures of 18th-century Spain — the Church's most energetic defender of Bourbon legitimacy during the War of the Spanish Succession (1701–1714), and later a major figure in the Spanish Church's reform attempts and the early Bourbon administration. Born in Motril (Granada), he studied at Granada and Salamanca, was appointed Bishop of Cartagena-Murcia in 1705 by Philip V, and immediately threw himself into the military and political crisis of the War of Succession.\n\nBelluga's most dramatic role was military: when the Archduke Charles's troops advanced through Valencia and toward Murcia in 1706, Belluga organised and personally led the resistance of his diocese — raising troops, fortifying cities, and engaging in active military operations against the Austrian-backed forces in the region of Cartagena and Murcia. His troops inflicted significant defeats on the Archduke's forces and he personally supervised the defence of Cartagena. This extraordinary bishop-general combination — ecclesiastical authority mobilised for Bourbon military purposes — made him the most visible symbol of the Church's total commitment to the Bourbon cause and earned him tremendous favour with Philip V. He was rewarded with the cardinalship in 1719.\n\nAfter the war, Belluga undertook a major project of social reform: the reclamation of wetlands and salt flats south of Alicante (the Paluds de Elx) to create irrigated agricultural land for the settlement of poor families — the 'Belluga colonisation', which created the towns of San Felipe Neri, San Fulgencio, and Dolores in the Alicante region and represents one of the most significant agrarian reform projects in 18th-century Spain. He moved to Rome in 1724 as a cardinal and spent his last decades as Spain's most influential representative in the papal curia.",
    "causes": [
      "The War of the Spanish Succession (1701–1714) — triggered by the disputed succession to the Spanish throne between Philip V (Bourbon) and Archduke Charles (Habsburg) — created the military and political crisis that forced Spanish bishops to choose sides and that gave militarily effective ecclesiastical leaders like Belluga extraordinary political prominence.",
      "Philip V's need to consolidate Bourbon authority in the Spanish Church after the war — replacing Habsburg-aligned prelates with Bourbon loyalists — made Belluga's demonstrated loyalty and military effectiveness the perfect credential for rapid elevation to the cardinalate.",
      "The social and economic dislocation of the War of Succession in southeastern Spain — including depopulation, ruined agriculture, and displaced communities — created the humanitarian context for Belluga's post-war wetland reclamation project, which combined practical irrigation engineering with the settlement of poor families."
    ],
    "effects": [
      "Belluga's Murcia wetland reclamation project (1715–1724) created three new towns in the Alicante plain (San Felipe Neri, San Fulgencio, Dolores), provided agricultural land for several thousand families, and remains one of the most visible examples of 18th-century Spanish agrarian reform and social engineering.",
      "His cardinalship (1719) and subsequent presence in Rome (1724–1743) made him one of Spain's most effective diplomatic representatives in the papal curia during the critical period of early Bourbon Spain's negotiations with the Holy See over ecclesiastical jurisdictions and patronage — the 'regalist' disputes that defined Church-state relations in 18th-century Spain.",
      "Belluga's wartime career as a bishop who led troops in defence of the Bourbon cause established a model of active clerical engagement in dynastic politics that characterised the Spanish Church's deep integration with Bourbon statecraft throughout the 18th century."
    ],
    "relationships": [
      {"sourceSlug": "luis-antonio-belluga-y-moncada", "sourceName": "Cardinal Belluga", "verb": "SUPPORTS", "targetSlug": "philip-v-of-spain", "targetName": "Philip V of Spain", "context": "Belluga was the Spanish Church's most active military supporter of Philip V during the War of Succession — raising and commanding troops against the Archduke's forces in Murcia and Cartagena, earning cardinalship as reward."},
      {"sourceSlug": "luis-antonio-belluga-y-moncada", "sourceName": "Cardinal Belluga", "verb": "TRANSFORMS", "targetSlug": "murcia-wetlands", "targetName": "Murcia/Alicante Wetlands", "context": "Belluga's post-war wetland reclamation project (1715–1724) created three new towns and settled thousands of poor families on newly irrigated agricultural land — one of the most significant 18th-century Spanish agrarian reform projects."},
      {"sourceSlug": "war-of-the-spanish-succession", "sourceName": "War of the Spanish Succession (1701–1714)", "verb": "SHAPES", "targetSlug": "luis-antonio-belluga-y-moncada", "targetName": "Cardinal Belluga", "context": "The War of Succession created the military crisis that made Belluga's bishop-general role both necessary and historically significant — defining his career and securing his extraordinary royal favour."}
    ],
    "places": [
      {"name": "Cartagena-Murcia, Spain", "role": "Belluga's diocese — the ecclesiastical territory he defended militarily during the War of Succession and where he undertook his major wetland reclamation project"},
      {"name": "Alicante, Spain (Paluds de Elx)", "role": "Site of Belluga's colonisation project — the reclaimed wetlands where San Felipe Neri, San Fulgencio, and Dolores were established"},
      {"name": "Rome, Italy", "role": "Where Belluga spent his final two decades as a cardinal and as Spain's most effective representative in the papal curia"}
    ],
    "subjects": ["Spanish History", "Early Modern History", "Church History", "Early Modern Era", "Spain", "Bourbon Dynasty", "Military History", "Social Reform"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Cardinal Belluga was the most militarily active Spanish bishop of the War of Succession — leading troops against the Archduke's forces in Murcia and earning cardinalship from Philip V. His subsequent wetland reclamation project created three new towns in Alicante and remains one of 18th-century Spain's most significant agrarian reforms. He represents the deep integration of the Spanish Church with Bourbon statecraft that defined 18th-century Spain.",
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
