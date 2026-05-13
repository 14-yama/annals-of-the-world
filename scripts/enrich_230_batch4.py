#!/usr/bin/env python3
"""
Batch 4: Ancient Roman and Greek jurists/orators.
Enriches 6 foundational figures of classical law and rhetoric.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "hypereides": {
        "summary": (
            "Hypereides (390–322 BCE) was one of the ten canonical Attic orators of ancient "
            "Athens and one of the most formidable advocates and prosecutors of the classical "
            "period. A pupil of both Plato and Isocrates, he combined philosophical training "
            "with rhetorical craft and worked for decades as a logographer (speechwriter for "
            "hire) and forensic advocate before becoming a prominent politician. His oratory "
            "was renowned for its wit, elegance, and devastating irony — Plutarch ranked him "
            "second only to Demosthenes among Attic orators.\n\n"
            "Hypereides handled several of the most sensational trials of the 4th century BCE. "
            "He prosecuted the general Philippides and other Macedonian sympathizers, defended "
            "Phryne the famous courtesan (hetaira) in a trial of impiety whose outcome became "
            "legendary, and — most consequentially — led the prosecution of Demosthenes in "
            "the Harpalus affair (324 BCE), when his former ally was accused of accepting "
            "bribes from Alexander the Great's runaway treasurer. Politically, Hypereides "
            "was the leading voice of the anti-Macedonian faction in Athens after Alexander's "
            "conquest of Persia, and following Alexander's death in 323 BCE he was the "
            "principal architect of the Lamian War — Athens's last bid to break free from "
            "Macedonian dominance.\n\n"
            "After Macedonia crushed the Lamian War at the Battle of Crannon (322 BCE), "
            "Antipater demanded the surrender of Hypereides and Demosthenes. Hypereides "
            "fled but was captured, and according to tradition had his tongue cut out before "
            "execution — a peculiarly symbolic punishment for the man who had wielded Athens's "
            "most feared voice. His speeches were largely lost until Egyptian papyrus "
            "discoveries in the 19th century recovered substantial portions of several, "
            "including Against Demosthenes and the Funeral Oration."
        ),
        "causes": [
            {
                "title": "Macedonian expansion under Philip II and then Alexander forced Athenian politicians to choose between accommodation and resistance — Hypereides chose resistance",
                "type": "EventWindow",
                "year": "359–323 BCE, Greece"
            },
            {
                "title": "Athens's democratic tradition of forensic oratory created both a market for logographers and an arena for political combat through the courts",
                "type": "Institution",
                "year": "c. 450–322 BCE, Athens"
            },
            {
                "title": "The Harpalus affair — the flight of Alexander's treasurer Harpalus to Athens with 700 talents — created the political crisis that split Athens's anti-Macedonian leaders",
                "type": "EventWindow",
                "year": "324 BCE, Athens"
            }
        ],
        "effects": [
            {
                "title": "The Lamian War (323–322 BCE) — the anti-Macedonian revolt that Hypereides championed — marked Athens's last bid for independence and ended with Macedonian suzerainty over Greece",
                "type": "EventWindow",
                "year": "323–322 BCE, Greece"
            },
            {
                "title": "Hypereides's prosecution of Demosthenes in the Harpalus affair split the anti-Macedonian alliance at a critical moment",
                "type": "EventWindow",
                "year": "324 BCE, Athens"
            },
            {
                "title": "Papyrus discoveries of his speeches (1847–1890s) restored much of his surviving work and cemented his reputation as one of the greatest Attic orators",
                "type": "Text",
                "year": "1847–1890s, Egypt/England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "hypereides",
                "sourceName": "Hypereides",
                "verb": "PROSECUTED",
                "targetSlug": "demosthenes",
                "targetName": "Demosthenes",
                "context": "Hypereides led the prosecution of his former ally Demosthenes in the Harpalus affair (324 BCE)"
            },
            {
                "sourceSlug": "hypereides",
                "sourceName": "Hypereides",
                "verb": "CHAMPIONED",
                "targetSlug": "lamian-war",
                "targetName": "Lamian War",
                "context": "Hypereides was the principal political architect of the Lamian War (323–322 BCE), Athens's last bid for independence"
            },
            {
                "sourceSlug": "hypereides",
                "sourceName": "Hypereides",
                "verb": "STUDIED_UNDER",
                "targetSlug": "isocrates",
                "targetName": "Isocrates",
                "context": "Hypereides studied rhetoric under Isocrates, Athens's most celebrated rhetoric teacher"
            },
            {
                "sourceSlug": "hypereides",
                "sourceName": "Hypereides",
                "verb": "OPPOSED",
                "targetSlug": "macedonian-hegemony",
                "targetName": "Macedonian Hegemony over Greece",
                "context": "Hypereides was the leading voice of Athenian resistance to Macedonian domination throughout his political career"
            },
            {
                "sourceSlug": "hypereides",
                "sourceName": "Hypereides",
                "verb": "EXECUTED_BY",
                "targetSlug": "antipater",
                "targetName": "Antipater",
                "context": "After the Lamian War, Antipater demanded Hypereides's surrender; he was captured and executed in 322 BCE"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Hypereides was one of the supreme masters of Attic forensic oratory and the principal political leader of Athenian resistance to Macedonian hegemony — his prosecution of Demosthenes, defense of Phryne, and championship of the Lamian War placed him at the center of Athens's last great democratic struggles.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "publius-mucius-scaevola": {
        "summary": (
            "Publius Mucius Scaevola (died c. 115 BCE) was a Roman jurist, consul (133 BCE), "
            "and Pontifex Maximus who is credited by Pomponius in the Digest as one of the "
            "three founders of Roman civil law — alongside Marcus Junius Brutus and Manius "
            "Manilius. His legal writings, while fragmentary, contributed to the systematic "
            "development of Roman private law at a critical period when Rome was transitioning "
            "from city-state to Mediterranean empire and its legal institutions were under "
            "corresponding pressure to mature.\n\n"
            "His consulship in 133 BCE — the year of Tiberius Gracchus's controversial land "
            "reform and assassination — placed him at the center of one of Rome's most violent "
            "constitutional crises. As a jurist and pontifex, Scaevola took a cautious position: "
            "he refused to authorize the consul Nasica's illegal lynching of Tiberius, arguing "
            "that Gracchus had broken no law, but equally he did not defend Gracchus's more "
            "radical proposals. This legalistic conservatism — defending law against both "
            "popular and aristocratic violence — exemplified the Roman jurist's self-conception "
            "as a neutral guardian of the ius civile.\n\n"
            "Scaevola served as Pontifex Maximus from approximately 130 to 115 BCE and left "
            "behind legal writings that were cited by later jurists. His son, Quintus Mucius "
            "Scaevola 'Pontifex,' carried on and greatly extended the family's legal tradition, "
            "writing the first comprehensive systematic treatise on Roman civil law. The two "
            "Scaevolae together represent one of the great intellectual dynasties of the Roman "
            "Republic's jurisprudential tradition."
        ),
        "causes": [
            {
                "title": "Rome's expanding empire and the proliferation of legal disputes required a class of professional jurists to systematize and interpret the ius civile",
                "type": "Institution",
                "year": "c. 200–100 BCE, Rome"
            },
            {
                "title": "The Gracchan crisis (133 BCE) forced jurists to take positions on the limits of popular assemblies, consular authority, and senatorial violence",
                "type": "EventWindow",
                "year": "133 BCE, Rome"
            },
            {
                "title": "The pontifical college's custodianship of legal formulae and calendars gave leading pontifices like Scaevola a key role in early Roman legal development",
                "type": "Institution",
                "year": "c. 250–100 BCE, Rome"
            }
        ],
        "effects": [
            {
                "title": "Scaevola's legal writings and opinions contributed to the foundational layer of Roman civil law systematized by his son and by Cicero's generation",
                "type": "Idea",
                "year": "c. 130–80 BCE, Rome"
            },
            {
                "title": "His refusal to sanction the illegal murder of Tiberius Gracchus set a precedent for jurists maintaining rule-of-law positions during political violence",
                "type": "EventWindow",
                "year": "133 BCE, Rome"
            },
            {
                "title": "His son Quintus Mucius Scaevola Pontifex built directly on his father's jurisprudence to write the first systematic treatise on Roman civil law",
                "type": "Person",
                "year": "c. 95–82 BCE, Rome"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "publius-mucius-scaevola",
                "sourceName": "Publius Mucius Scaevola",
                "verb": "FATHERED",
                "targetSlug": "quintus-mucius-scaevola-pontifex",
                "targetName": "Quintus Mucius Scaevola Pontifex",
                "context": "Quintus Mucius Scaevola Pontifex was the son of Publius and carried the family's jurisprudential tradition to its classical height"
            },
            {
                "sourceSlug": "publius-mucius-scaevola",
                "sourceName": "Publius Mucius Scaevola",
                "verb": "SERVED_IN",
                "targetSlug": "roman-pontifical-college",
                "targetName": "Roman Pontifical College",
                "context": "Scaevola served as Pontifex Maximus c. 130–115 BCE, giving him custodianship of Rome's legal-religious formulae"
            },
            {
                "sourceSlug": "publius-mucius-scaevola",
                "sourceName": "Publius Mucius Scaevola",
                "verb": "DEFINED",
                "targetSlug": "roman-civil-law",
                "targetName": "Roman Civil Law",
                "context": "Pomponius named Scaevola one of the three founders of the ius civile alongside Brutus and Manilius"
            },
            {
                "sourceSlug": "publius-mucius-scaevola",
                "sourceName": "Publius Mucius Scaevola",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "tiberius-gracchus",
                "targetName": "Tiberius Gracchus",
                "context": "Scaevola was consul the year Gracchus's land reform and assassination convulsed the Republic; he refused to sanction the illegal mob violence against Gracchus"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Publius Mucius Scaevola's contributions to the foundations of Roman civil law — as one of three jurists credited by Pomponius with creating it — and his principled rule-of-law stance during the Gracchan crisis established the Roman jurist's self-conception as a guardian of law against political violence.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "quintus-mucius-scaevola-pontifex": {
        "summary": (
            "Quintus Mucius Scaevola 'Pontifex' (c. 140–82 BCE) was the greatest jurist of "
            "the Roman Republic, consul in 95 BCE, and the author of Ius Civile — the first "
            "comprehensive, systematically organized treatise on Roman private law, written "
            "in 18 books. Son of Publius Mucius Scaevola, another of Rome's founding jurists, "
            "he brought the Roman legal tradition to its republican zenith: a systematic "
            "jurisprudence organized by categories and concepts rather than by the traditional "
            "aggregation of responses (responsa) and formulae.\n\n"
            "Scaevola's Ius Civile was the foundational text of Roman legal science. While "
            "earlier jurists had collected cases and responses, Scaevola imposed systematic "
            "order — organizing his treatment by categories of law (inheritance, contracts, "
            "persons, actions) and analyzing each with consistent conceptual methods. "
            "Cicero, who studied under him as a young man, spoke of him with profound "
            "admiration as both jurist and advocate. The later jurist Pomponius wrote that "
            "Scaevola was the first to give civil law systematic literary form. He also served "
            "as governor of Asia (c. 94 BCE) with unusual fairness and probity — his edicts "
            "against corruption became a model, and Cicero's own provincial administration "
            "consciously imitated his example.\n\n"
            "Scaevola's death encapsulates the violence of his era: he was murdered in 82 BCE, "
            "during the proscriptions of Sulla's civil war, apparently by the Marian faction, "
            "at the altar of Vesta — the most sacred spot in Rome. His Ius Civile remained "
            "the touchstone for subsequent jurists. Through the vast commentaries it generated "
            "— including Servius Sulpicius Rufus's commentary 'Against Scaevola' — it shaped "
            "Roman law through to Justinian's Digest five centuries later."
        ),
        "causes": [
            {
                "title": "Rome's growing empire demanded comprehensive, portable legal doctrine that could be applied by governors and local magistrates far from the city",
                "type": "Institution",
                "year": "c. 150–100 BCE, Rome"
            },
            {
                "title": "The tradition of pontifical and jurist custodianship of the ius civile, inherited from his father, gave Scaevola both authority and accumulated precedents",
                "type": "Person",
                "year": "c. 140–100 BCE, Rome"
            },
            {
                "title": "The growth of Greek philosophical method in Rome provided Scaevola with categorical and systematic tools to organize Roman legal doctrine scientifically",
                "type": "Idea",
                "year": "c. 150–90 BCE, Rome"
            }
        ],
        "effects": [
            {
                "title": "Ius Civile (18 books) became the foundational text of Roman legal science, generating centuries of commentary and directly influencing Justinian's Digest",
                "type": "Text",
                "year": "c. 95–90 BCE, Rome"
            },
            {
                "title": "Cicero's legal education under Scaevola shaped Roman jurisprudence's intersection with rhetoric and philosophy in the late Republic",
                "type": "Person",
                "year": "c. 90–80 BCE, Rome"
            },
            {
                "title": "His Asian governorship set a model of provincial administration against extortion that Cicero and others consciously emulated",
                "type": "Institution",
                "year": "c. 94 BCE, Asia"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "quintus-mucius-scaevola-pontifex",
                "sourceName": "Quintus Mucius Scaevola Pontifex",
                "verb": "AUTHORED",
                "targetSlug": "ius-civile-scaevola",
                "targetName": "Ius Civile (18 books)",
                "context": "Scaevola's 18-book Ius Civile was the first systematic treatise on Roman private law and the foundation of the subsequent juristic tradition"
            },
            {
                "sourceSlug": "quintus-mucius-scaevola-pontifex",
                "sourceName": "Quintus Mucius Scaevola Pontifex",
                "verb": "TAUGHT",
                "targetSlug": "cicero",
                "targetName": "Cicero",
                "context": "The young Cicero studied under Scaevola, who deeply influenced his legal and philosophical education"
            },
            {
                "sourceSlug": "quintus-mucius-scaevola-pontifex",
                "sourceName": "Quintus Mucius Scaevola Pontifex",
                "verb": "MURDERED_BY",
                "targetSlug": "marian-faction",
                "targetName": "Marian Faction",
                "context": "Scaevola was murdered at the altar of Vesta in Rome in 82 BCE during the Sullan proscriptions"
            },
            {
                "sourceSlug": "quintus-mucius-scaevola-pontifex",
                "sourceName": "Quintus Mucius Scaevola Pontifex",
                "verb": "SON_OF",
                "targetSlug": "publius-mucius-scaevola",
                "targetName": "Publius Mucius Scaevola",
                "context": "Quintus inherited his father's juristic tradition and greatly extended it to produce Rome's first systematic legal treatise"
            },
            {
                "sourceSlug": "quintus-mucius-scaevola-pontifex",
                "sourceName": "Quintus Mucius Scaevola Pontifex",
                "verb": "INFLUENCED",
                "targetSlug": "justinians-digest",
                "targetName": "Justinian's Digest",
                "context": "Scaevola's Ius Civile was excerpted and cited extensively in Justinian's Digest (533 CE), preserving his jurisprudence for posterity"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Quintus Mucius Scaevola Pontifex's systematic 18-book treatise on Roman civil law gave Roman jurisprudence its first scientific organization, shaped the education of Cicero, and through centuries of commentary reached directly into Justinian's Digest — making him one of the most consequential architects of the Western legal tradition.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "quintus-hortensius": {
        "summary": (
            "Quintus Hortensius Hortalus (114–50 BCE) was the greatest Roman advocate of his "
            "generation — until Cicero eclipsed him. For fifteen years he was the undisputed "
            "master of the Roman courts, celebrated for a prodigious memory, physical grace, "
            "and an ornate Asianic oratorical style that dazzled his contemporaries. Cicero "
            "himself wrote a lost dialogue Hortensius (which inspired Augustine's conversion "
            "to philosophy) in his friend and former rival's honor after his death.\n\n"
            "Hortensius dominated Roman forensic oratory from his debut at age 19 until "
            "approximately 70 BCE, when Cicero's prosecution of Verres effectively ended "
            "Hortensius's reign. Hortensius had been retained to defend Gaius Verres — the "
            "corrupt governor of Sicily — and was so confident of acquittal that he advised "
            "Verres to request a postponement (actio secunda). Cicero, however, presented "
            "his evidence so overwhelmingly in the actio prima that Verres fled into voluntary "
            "exile before Hortensius could even speak in the second hearing. This disaster "
            "marked the turning point: thereafter Hortensius and Cicero were colleagues "
            "rather than rivals, frequently appearing on the same side.\n\n"
            "Hortensius was famous beyond the courts for his magnificent lifestyle — his "
            "fish ponds (piscinae) were so celebrated that Cicero called him and other "
            "aristocratic fish-fanciers the piscinarii ('fish-pond men'). He maintained "
            "elaborate gardens, kept the first (according to tradition) plane trees in "
            "Italy, and was renowned for his wine cellar and dinner parties. His will "
            "bequeathed to Rome a tradition of legal advocacy as a competitive art form "
            "embedded in aristocratic culture, a tradition Cicero theorized in his dialogues "
            "Brutus and De Oratore, in both of which Hortensius appears as a major character."
        ),
        "causes": [
            {
                "title": "The Roman Republic's competitive court culture made forensic advocacy the highest form of elite public performance — a career path and status competition rolled into one",
                "type": "Institution",
                "year": "c. 200–50 BCE, Rome"
            },
            {
                "title": "Prodigious natural gifts — voice, memory, physical presence — combined with a rigorous rhetorical education made Hortensius the supreme advocate of his age",
                "type": "Person",
                "year": "c. 114–95 BCE, Rome"
            },
            {
                "title": "The Asianic rhetorical style's dominance in the early 1st century BCE gave Hortensius an aesthetic framework suited to his flamboyant temperament",
                "type": "Idea",
                "year": "c. 100–70 BCE, Rome"
            }
        ],
        "effects": [
            {
                "title": "Hortensius's defeat in the Verres trial (70 BCE) marked the decisive transfer of Rome's rhetorical supremacy from his Asianic style to Cicero's more Attic approach",
                "type": "EventWindow",
                "year": "70 BCE, Rome"
            },
            {
                "title": "Cicero's dialogue Hortensius immortalized his memory and exercised enormous posthumous influence — it was the text that converted Augustine to philosophy",
                "type": "Text",
                "year": "46 BCE/354 CE"
            },
            {
                "title": "Hortensius's 15-year reign at the Roman bar set the competitive standard of forensic excellence against which all subsequent Roman advocates measured themselves",
                "type": "Idea",
                "year": "c. 95–70 BCE, Rome"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "quintus-hortensius",
                "sourceName": "Quintus Hortensius",
                "verb": "DEFEATED_BY",
                "targetSlug": "cicero",
                "targetName": "Cicero",
                "context": "Cicero's prosecution of Verres (70 BCE) outmaneuvered Hortensius as defense counsel, effectively ending Hortensius's reign as Rome's supreme advocate"
            },
            {
                "sourceSlug": "quintus-hortensius",
                "sourceName": "Quintus Hortensius",
                "verb": "DEFENDED",
                "targetSlug": "gaius-verres",
                "targetName": "Gaius Verres",
                "context": "Hortensius was retained to defend the corrupt governor Verres against Cicero's prosecution; Verres fled before the case concluded"
            },
            {
                "sourceSlug": "quintus-hortensius",
                "sourceName": "Quintus Hortensius",
                "verb": "CELEBRATED_IN",
                "targetSlug": "cicero-hortensius",
                "targetName": "Cicero's Hortensius",
                "context": "Cicero wrote the dialogue Hortensius after his death in 50 BCE, immortalizing him and inspiring Augustine's conversion to philosophy"
            },
            {
                "sourceSlug": "quintus-hortensius",
                "sourceName": "Quintus Hortensius",
                "verb": "APPEARED_IN",
                "targetSlug": "de-oratore",
                "targetName": "De Oratore",
                "context": "Hortensius is a major character in Cicero's De Oratore and Brutus, Roman dialogues on the theory and history of Latin oratory"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Quintus Hortensius was the supreme master of Roman forensic oratory for fifteen years and Cicero's greatest rival; his legacy encompassed both the height of Asianic rhetorical style and a posthumous influence through Cicero's Hortensius that reached Augustine and shaped the philosophy of the Latin West.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "marcus-antistius-labeo": {
        "summary": (
            "Marcus Antistius Labeo (c. 50 BCE – c. 18 CE) was the most prolific and arguably "
            "the most original Roman jurist of the Augustan era, and the founder of the "
            "Proculian school of Roman law — one of the two great juristic schools that "
            "shaped classical Roman law for two centuries. A man of pronounced republican "
            "sympathies who refused both the consulship and other honors offered by Augustus, "
            "Labeo spent half his year in Rome teaching law and answering legal questions, "
            "and the other half in retreat writing — reportedly composing over 400 books "
            "of jurisprudence, more than any other classical jurist.\n\n"
            "Labeo's jurisprudence was characterized by bold conceptual innovation. He was "
            "willing to extend legal principles to new situations rather than restricting "
            "himself to precedent, giving Roman law a creative adaptability that his rival "
            "Gaius Ateius Capito — founder of the competing Sabinian school — lacked. Where "
            "Capito was politically compliant with Augustus and juristically conservative, "
            "Labeo's political independence and juristic creativity went together. Tacitus "
            "notes this conjunction: Labeo's 'freedom of mind' manifested in both politics "
            "and law. His innovations in contract, property, and obligations were preserved "
            "through his students and excerpted in enormous quantities in Justinian's Digest — "
            "more Labeo passages survive than those of almost any other pre-classical jurist.\n\n"
            "The Proculian and Sabinian schools that Labeo and Capito respectively founded "
            "debated dozens of precise legal questions across two centuries — on the law of "
            "sale, specification (manufacturing goods from another's materials), and the "
            "status of mixtures and alloys — giving Roman law much of its systematic "
            "precision. Labeo's work represents the apex of the Republic's juristic tradition "
            "being channeled into the imperial legal machine."
        ),
        "causes": [
            {
                "title": "The Augustan principate's transformation of Rome from republic to monarchy drove jurists with republican sympathies to express their independence through legal scholarship rather than politics",
                "type": "EventWindow",
                "year": "27 BCE – 14 CE, Rome"
            },
            {
                "title": "The enormous growth in civil litigation under the principate created demand for original legal analysis beyond the simple recitation of precedents",
                "type": "Institution",
                "year": "c. 30 BCE – 20 CE, Rome"
            },
            {
                "title": "Labeo's private school of jurisprudence — where he taught for half the year — institutionalized the transmission of Roman legal doctrine from master to student",
                "type": "Institution",
                "year": "c. 15 BCE – 18 CE, Rome"
            }
        ],
        "effects": [
            {
                "title": "The Proculian school Labeo founded continued for two centuries, debating with the Sabinian school on dozens of precise legal questions that refined Roman civil law",
                "type": "Institution",
                "year": "c. 18 CE – 200 CE, Rome"
            },
            {
                "title": "Labeo's writings were excerpted more than almost any other pre-classical jurist in Justinian's Digest, transmitting his doctrines to medieval and modern civil law",
                "type": "Text",
                "year": "533 CE, Constantinople"
            },
            {
                "title": "Labeo's bold doctrinal innovations in contract and obligations expanded Roman private law's adaptability to new commercial and social situations",
                "type": "Idea",
                "year": "c. 15 BCE – 18 CE, Rome"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "marcus-antistius-labeo",
                "sourceName": "Marcus Antistius Labeo",
                "verb": "FOUNDED",
                "targetSlug": "proculian-school",
                "targetName": "Proculian School of Roman Law",
                "context": "Labeo's innovative jurisprudential approach was carried on by Proculus and subsequent jurists of the Proculian school"
            },
            {
                "sourceSlug": "marcus-antistius-labeo",
                "sourceName": "Marcus Antistius Labeo",
                "verb": "OPPOSED",
                "targetSlug": "gaius-ateius-capito",
                "targetName": "Gaius Ateius Capito",
                "context": "Labeo and Capito were the founding rivals of the Proculian and Sabinian schools respectively, differing in both politics (Labeo republican, Capito Augustan) and juristic method"
            },
            {
                "sourceSlug": "marcus-antistius-labeo",
                "sourceName": "Marcus Antistius Labeo",
                "verb": "EXCERPTED_IN",
                "targetSlug": "justinians-digest",
                "targetName": "Justinian's Digest",
                "context": "Labeo's writings were cited more than almost any other pre-classical jurist in Justinian's Digest of 533 CE"
            },
            {
                "sourceSlug": "marcus-antistius-labeo",
                "sourceName": "Marcus Antistius Labeo",
                "verb": "REFUSED",
                "targetSlug": "augustus",
                "targetName": "Augustus",
                "context": "Labeo declined the consulship offered by Augustus, maintaining his political independence throughout the principate"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Marcus Antistius Labeo's founding of the Proculian school and his prolific innovative jurisprudence — 400+ books, more than any other pre-classical jurist — made him one of the most consequential legal thinkers of the Roman classical period, shaping private law doctrines transmitted through Justinian's Digest to modern civil law systems.",
            "significanceCategory": "continental"
        },
        "importanceScore": 7
    },

    "marcus-minucius-felix": {
        "summary": (
            "Marcus Minucius Felix (active c. 150–250 CE) was a Roman lawyer and Christian "
            "apologist, author of the Octavius — the earliest surviving Latin work of "
            "Christian apologetics and one of the most sophisticated defences of Christianity "
            "addressed to a pagan Roman intellectual audience. Almost nothing is known of "
            "his biography beyond what the Octavius itself reveals: he was a practicing "
            "advocate (causidicus) in Rome, and the dialogue takes place among three "
            "friends — Minucius Felix, the Christian Octavius Januarius, and the pagan "
            "Caecilius Natalis — walking along the beach at Ostia.\n\n"
            "The Octavius is a forensic dialogue in the tradition of Cicero, deliberately "
            "modelled on Cicero's De Natura Deorum and De Re Publica. Minucius Felix "
            "constructed his defense of Christianity using the tools of Roman philosophical "
            "rhetoric rather than scripture — arguing from natural theology, reason, and "
            "the incoherence of pagan polytheism rather than from biblical authority. "
            "Caecilius raises the standard anti-Christian charges of the era: atheism, "
            "secrecy, immorality, and political disloyalty. Octavius responds with "
            "arguments for monotheism, the providential order of the universe, and the "
            "moral superiority of Christian practice. Minucius Felix serves as the judge "
            "who finds in favor of Octavius at the end — a forensic structure unique in "
            "early Christian apologetics.\n\n"
            "The Octavius's precise relationship to Tertullian's Apologeticum (c. 197 CE) "
            "has been debated since the 17th century — some passages are nearly identical — "
            "with most modern scholars concluding that Minucius Felix drew on Tertullian. "
            "The work was rediscovered in a manuscript of Arnobius in 1543 and recognized "
            "as a separate text. Its elegant Ciceronian Latin and sophisticated philosophical "
            "reasoning made it an important document of the cultured Christianity that "
            "sought respectability among Rome's educated classes."
        ),
        "causes": [
            {
                "title": "Roman anti-Christian persecution and intellectual contempt — charges of atheism, immorality, and political disloyalty — required a sophisticated literary defense of Christianity to educated pagans",
                "type": "EventWindow",
                "year": "c. 150–250 CE, Rome"
            },
            {
                "title": "The Ciceronian philosophical dialogue tradition provided Minucius Felix with both a literary model and a philosophical vocabulary for natural theology",
                "type": "Text",
                "year": "c. 54–44 BCE, Rome"
            },
            {
                "title": "The educated urban lawyering class in Rome included converts to Christianity who brought rhetorical and legal training to the church's intellectual defense",
                "type": "Institution",
                "year": "c. 150–250 CE, Rome"
            }
        ],
        "effects": [
            {
                "title": "The Octavius established natural theological argumentation — from reason and universal consent rather than scripture — as a key strategy of Latin Christian apologetics",
                "type": "Text",
                "year": "c. 200 CE, Rome"
            },
            {
                "title": "The dialogue's rediscovery in 1543 contributed to early modern knowledge of second-century Christian intellectual culture",
                "type": "Idea",
                "year": "1543, Europe"
            },
            {
                "title": "Minucius Felix exemplified the type of culturally Roman, legally trained Christian apologist who sought to bridge Roman elite culture and Christianity",
                "type": "Person",
                "year": "c. 200–250 CE"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "marcus-minucius-felix",
                "sourceName": "Marcus Minucius Felix",
                "verb": "AUTHORED",
                "targetSlug": "octavius",
                "targetName": "Octavius",
                "context": "Minucius Felix wrote the Octavius, the earliest surviving Latin Christian apologetic work, as a forensic dialogue defending Christianity to educated pagans"
            },
            {
                "sourceSlug": "marcus-minucius-felix",
                "sourceName": "Marcus Minucius Felix",
                "verb": "MODELLED_ON",
                "targetSlug": "cicero-de-natura-deorum",
                "targetName": "Cicero's De Natura Deorum",
                "context": "The Octavius is deliberately styled on Cicero's philosophical dialogues, using classical rhetorical form to argue for Christianity"
            },
            {
                "sourceSlug": "marcus-minucius-felix",
                "sourceName": "Marcus Minucius Felix",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "tertullian",
                "targetName": "Tertullian",
                "context": "Minucius Felix's Octavius shares extensive passages with Tertullian's Apologeticum; the exact relationship remains debated by scholars"
            },
            {
                "sourceSlug": "marcus-minucius-felix",
                "sourceName": "Marcus Minucius Felix",
                "verb": "CONTRIBUTED_TO",
                "targetSlug": "latin-christian-apologetics",
                "targetName": "Latin Christian Apologetics",
                "context": "The Octavius was the foundational text of Latin apologetics, establishing natural-theological argumentation as a defense strategy"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Marcus Minucius Felix's Octavius — the earliest Latin Christian apologetic — brought Ciceronian philosophical dialogue form to the defense of Christianity, demonstrating that Roman legal and rhetorical culture could be fully appropriated by the church and establishing natural theology as a key weapon of Latin apologetics.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    }
}


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}")
        return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    updated = []

    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
            updated.append(field)

    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
            updated.append(field)

    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


if __name__ == "__main__":
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 4: ancient law/rhetoric)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
