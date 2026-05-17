#!/usr/bin/env python3
"""
Batch 3 enrichment for 231-Class-231 entities (Jurisprudence & Canon Law).
Enriches 8 foundational Roman and medieval legal scholars.
Follows git-first bot rules: writes _unsyncedEdits=True + _editLog diffs.
"""

import json
import os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/231-Class-231"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "irnerius": {
        "summary": (
            "Irnerius (c. 1050–c. 1125) was an Italian jurist and teacher at Bologna who is "
            "widely recognized as the founder of the medieval study of Roman law and the first "
            "of the great Glossators. By recovering and systematically teaching Justinian's "
            "Corpus Juris Civilis, he launched a legal revolution that would shape European "
            "law for the next millennium.\n\n"
            "Working at Bologna — then the pre-eminent centre of Italian learning — Irnerius "
            "began lecturing on the full Digest of Justinian at a time when only fragments of "
            "Roman law circulated in the West. He developed the gloss, a method of annotating "
            "the text word-by-word and resolving contradictions through rational argument, "
            "transforming law from a craft into an academic discipline. His students spread "
            "his method across Europe, and Bologna under his influence became the first "
            "university in the Western world dedicated to law.\n\n"
            "His legacy is immeasurable: the Glossator school he founded produced Accursius, "
            "whose Glossa Ordinaria became the standard commentary on Roman law for three "
            "centuries. Every civil law system in continental Europe — French, Spanish, "
            "Italian, German — traces its intellectual ancestry to the classroom Irnerius "
            "created in Bologna around 1088."
        ),
        "causes": [
            {"title": "Recovery of Justinian's Digest in complete form prompted systematic scholarly study of Roman law in the West", "type": "Idea", "year": "c. 1070–1090, Italy"},
            {"title": "Patronage of Countess Matilda of Tuscany and Holy Roman Emperor Henry IV gave Irnerius political backing for his school", "type": "Institution", "year": "c. 1088–1115, Bologna"},
            {"title": "Growth of long-distance trade and urban communes created demand for a sophisticated legal system to regulate contracts and property", "type": "EventWindow", "year": "c. 1050–1100, Northern Italy"},
        ],
        "effects": [
            {"title": "Irnerius's Gloss method became the standard academic approach to legal texts, copied by every Glossator after him", "type": "Idea", "year": "c. 1090–1250, Europe"},
            {"title": "University of Bologna established as the first European law school, model for Oxford, Paris, and all later universities", "type": "Institution", "year": "c. 1088–1150, Bologna"},
            {"title": "Civil law tradition spread across continental Europe as his students carried the gloss method to France, Spain, and the Holy Roman Empire", "type": "Movement", "year": "c. 1100–1300, Europe"},
            {"title": "Corpus Juris Civilis became the foundation of every continental legal system, entrenching Roman law as the ius commune", "type": "Text", "year": "c. 1100–1500, Europe"},
        ],
        "relationships": [
            {"targetSlug": "accursius", "verb": "INFLUENCES", "note": "Irnerius founded the Glossator tradition that culminated in Accursius's Glossa Ordinaria"},
            {"targetSlug": "university-of-bologna", "verb": "INFLUENCES", "note": "Irnerius's teaching c.1088 is the founding moment of the University of Bologna"},
            {"targetSlug": "corpus-juris-civilis", "verb": "TRANSMITS", "note": "Irnerius recovered and disseminated the full Corpus Juris Civilis to the medieval West"},
            {"targetSlug": "henry-de-bracton", "verb": "INFLUENCES", "note": "The Bolognese tradition Irnerius founded reached England and shaped Bracton's systematic approach"},
            {"targetSlug": "bartolus-de-saxoferrato", "verb": "INFLUENCES", "note": "The Glossator school Irnerius founded was the precursor to the Commentators, of whom Bartolus was the peak"},
        ],
        "places": ["Bologna, Italy"],
        "subjects": ["Law", "Roman Law", "Bologna", "Medieval Europe", "Jurisprudence", "Glossators", "Legal Education", "Corpus Juris Civilis"],
        "subjectHeadings": "Jurisprudence — Legal Scholarship — Italy — Medieval",
        "frameworks": ["intellectual-history", "institutional-history"],
        "born": "c. 1050",
        "died": "c. 1125",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Irnerius is the founding figure of Western legal science — his recovery and systematic teaching of Roman law at Bologna created the civil law tradition that governs the majority of the world's legal systems today.",
            "significanceCategory": "world-changing"
        },
    },
    "accursius": {
        "summary": (
            "Accursius (c. 1182–1263) was an Italian jurist and the last and greatest of the "
            "Glossators, whose monumental Glossa Ordinaria became the standard commentary on "
            "Justinian's Corpus Juris Civilis for three centuries and established him as the "
            "undisputed authority in medieval Roman law.\n\n"
            "Born near Florence and trained at Bologna, Accursius spent decades synthesizing "
            "the accumulated glosses of his predecessors — from Irnerius to Azo — into a "
            "single authoritative apparatus attached to every major text in the Corpus Juris. "
            "The resulting Glossa Ordinaria, completed around 1230, comprised nearly 100,000 "
            "individual glosses and resolved the contradictions and redundancies of earlier "
            "commentary into a coherent exposition. It was so comprehensive and authoritative "
            "that it was printed alongside the Corpus Juris Civilis itself in virtually every "
            "edition up to the 18th century.\n\n"
            "His achievement marked the end of the Glossator era and made Roman law fully "
            "teachable and accessible across Europe. The legal systems of France, Spain, "
            "Portugal, Germany, and Italy — and through them the Americas — all carry the "
            "imprint of Accursius's synthesis. His son Francesco Accursius later taught at "
            "Oxford, carrying the tradition to England."
        ),
        "causes": [
            {"title": "Accumulated century of glosses by Azo, Bulgarus, and other Glossators created an unwieldy mass requiring systematic synthesis", "type": "Text", "year": "c. 1100–1220, Bologna"},
            {"title": "Demand from Italian city-states for authoritative Roman law guidance to settle property, contract, and inheritance disputes", "type": "EventWindow", "year": "c. 1200–1250, Northern Italy"},
            {"title": "University of Bologna as an institutional home giving Accursius access to all prior glossatorial manuscripts", "type": "Institution", "year": "c. 1220–1260, Bologna"},
        ],
        "effects": [
            {"title": "Glossa Ordinaria became the standard commentary printed alongside every edition of the Corpus Juris Civilis through the 18th century", "type": "Text", "year": "c. 1230–1750, Europe"},
            {"title": "Marked the end of the Glossator era and paved the way for the Commentators (Post-Glossators) who applied Roman law to medieval conditions", "type": "Movement", "year": "c. 1250–1400, Europe"},
            {"title": "Roman law firmly established as the ius commune across continental Europe through the authority of Accursius's synthesis", "type": "Idea", "year": "c. 1250–1800, Europe"},
            {"title": "Francesco Accursius (son) carried Bolognese learning to Oxford, influencing English common law thinking", "type": "Person", "year": "c. 1275–1289, England"},
        ],
        "relationships": [
            {"targetSlug": "irnerius", "verb": "INFLUENCES", "note": "Accursius was the culmination of the Glossator school Irnerius founded; his Glossa Ordinaria sealed that tradition"},
            {"targetSlug": "bartolus-de-saxoferrato", "verb": "INFLUENCES", "note": "The Commentators, led by Bartolus, moved beyond Accursius's glosses to apply Roman law to contemporary society"},
            {"targetSlug": "corpus-juris-civilis", "verb": "TRANSMITS", "note": "The Glossa Ordinaria was printed alongside the Corpus Juris Civilis in virtually every edition"},
            {"targetSlug": "henry-de-bracton", "verb": "INFLUENCES", "note": "Bracton's De Legibus drew on the Bolognese tradition that Accursius crowned"},
            {"targetSlug": "university-of-bologna", "verb": "OCCURS_IN", "note": "Accursius taught and produced the Glossa Ordinaria at Bologna"},
        ],
        "places": ["Bologna, Italy"],
        "subjects": ["Law", "Roman Law", "Bologna", "Jurisprudence", "Glossators", "Medieval Europe", "Glossa Ordinaria"],
        "subjectHeadings": "Jurisprudence — Legal Scholarship — Italy — Medieval",
        "frameworks": ["intellectual-history", "institutional-history"],
        "born": "c. 1182",
        "died": "c. 1263",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Accursius's Glossa Ordinaria was the single most influential commentary on Roman law in the Middle Ages, making the Corpus Juris Civilis fully accessible and authoritative across Europe and cementing the civil law tradition.",
            "significanceCategory": "world-changing"
        },
    },
    "john-selden": {
        "summary": (
            "John Selden (1584–1654) was an English jurist, legal antiquary, and polymath — "
            "one of the most erudite scholars of his age — whose writings on the history of "
            "English law, parliamentary privilege, and the law of the sea made him a towering "
            "figure in both legal scholarship and political thought.\n\n"
            "Born in Sussex and educated at Hart Hall, Oxford, and the Inner Temple, Selden "
            "combined meticulous historical research with sharp legal argument. His Historia "
            "Tithe Controversy (1618) challenged clerical tithes, earning him brief imprisonment. "
            "His Mare Clausum (1635), written at royal command to rebut Grotius's Mare Liberum, "
            "argued that the English Crown held dominion over adjacent seas — laying the "
            "groundwork for modern concepts of territorial waters. As a Member of Parliament, "
            "he was a leading defender of the common law against royal prerogative and helped "
            "draft the Petition of Right (1628).\n\n"
            "His Table Talk, published posthumously in 1689, is among the most quoted collections "
            "of English aphorisms. A man equally at home in Hebrew, Arabic, Syriac, and Greek, "
            "Selden was called by Milton 'the chief of learned men reputed in this land.'"
        ),
        "causes": [
            {"title": "English common law tradition provided Selden with a historical method for defending parliamentary rights against Stuart royal prerogative", "type": "Idea", "year": "c. 1600–1628, England"},
            {"title": "Anglo-Dutch maritime rivalry prompted royal commission to Selden to write a legal counter-argument to Grotius's Mare Liberum", "type": "EventWindow", "year": "1618–1635, England"},
            {"title": "Humanist legal scholarship in the tradition of Budé and Hotman gave Selden tools to use history as a legal argument", "type": "Movement", "year": "c. 1580–1620, Europe"},
        ],
        "effects": [
            {"title": "Mare Clausum established the legal concept of territorial waters and national sovereignty over adjacent seas", "type": "Text", "year": "1635, England"},
            {"title": "Petition of Right (1628) — co-drafted by Selden — codified limits on taxation without consent and imprisonment without cause", "type": "Text", "year": "1628, England"},
            {"title": "Table Talk preserved as aphorisms on church, state, and law that influenced Enlightenment political thought", "type": "Text", "year": "1689, England"},
            {"title": "Selden's historical method for defending common law rights shaped the Whig constitutional tradition through Coke and Blackstone", "type": "Idea", "year": "c. 1650–1750, England"},
        ],
        "relationships": [
            {"targetSlug": "edward-coke", "verb": "INFLUENCES", "note": "Selden and Coke were allies in Parliament defending common law against royal prerogative"},
            {"targetSlug": "hugo-grotius", "verb": "INFLUENCES", "note": "Selden's Mare Clausum directly rebutted Grotius's Mare Liberum on the freedom of the seas"},
            {"targetSlug": "petition-of-right", "verb": "INFLUENCES", "note": "Selden helped draft the Petition of Right 1628 as an MP and legal scholar"},
            {"targetSlug": "english-civil-war", "verb": "INFLUENCES", "note": "Selden's parliamentary career and legal scholarship shaped the constitutional arguments that led to the Civil War"},
            {"targetSlug": "william-blackstone", "verb": "INFLUENCES", "note": "Selden's historical approach to common law influenced Blackstone's Commentaries a century later"},
        ],
        "places": ["London, England", "Oxford, England"],
        "subjects": ["Law", "English Common Law", "Maritime Law", "Parliamentary History", "England", "17th Century", "Legal Scholarship", "Constitutional History"],
        "subjectHeadings": "Jurisprudence — Common Law — England — Early Modern",
        "frameworks": ["constitutional-history", "intellectual-history"],
        "born": "16 December 1584",
        "died": "30 November 1654",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "John Selden was the foremost legal historian of 17th-century England, whose defence of parliamentary rights and invention of the territorial sea doctrine shaped both English constitutional law and international maritime law.",
            "significanceCategory": "continental"
        },
    },
    "guillaume-de-nogaret": {
        "summary": (
            "Guillaume de Nogaret (c. 1260–1313) was a French royal jurist and chancellor who "
            "served Philip IV of France as the chief architect of his confrontation with Pope "
            "Boniface VIII — the most dramatic clash between royal and papal power in the "
            "Middle Ages and a turning point in the development of secular sovereignty.\n\n"
            "Born to a family of Cathar heretics in southern France and trained in Roman law "
            "at Montpellier, Nogaret combined civilian legal sophistication with fierce loyalty "
            "to the French crown. In 1303, he personally led a raid on the papal residence at "
            "Anagni, arresting and briefly imprisoning Boniface VIII in what became known as "
            "'the slap of Anagni.' Though the pope was released within days and died a month "
            "later, the episode shattered the political prestige of the papacy and emboldened "
            "secular rulers across Europe. Nogaret also orchestrated the destruction of the "
            "Knights Templar in 1307–1312, securing their wealth for the French crown.\n\n"
            "Nogaret never faced canonical punishment — Philip IV protected him — but his "
            "actions accelerated the Avignon papacy (1309–1377), when French-controlled popes "
            "were effectively subordinate to the French crown. He stands as an early and "
            "ruthless practitioner of the doctrine that the king was sovereign within his realm."
        ),
        "causes": [
            {"title": "Conflict between Philip IV of France and Boniface VIII over clerical taxation and royal sovereignty created the political crisis Nogaret weaponized", "type": "EventWindow", "year": "1296–1303, France"},
            {"title": "Recovery and teaching of Roman law in southern France gave Nogaret the intellectual tools to argue for royal sovereignty over the Church", "type": "Idea", "year": "c. 1270–1300, Montpellier"},
            {"title": "Unam Sanctam (1302) — Boniface VIII's extreme claim of papal supremacy over all secular rulers — forced a direct confrontation", "type": "Text", "year": "1302, Rome"},
        ],
        "effects": [
            {"title": "Attack on Anagni (1303) destroyed Boniface VIII's authority and dealt the papacy a blow from which its universal political claims never recovered", "type": "EventWindow", "year": "1303, Anagni"},
            {"title": "Avignon papacy (1309–1377) established as French-controlled popes yielded to French royal influence, fracturing papal independence", "type": "Institution", "year": "1309–1377, Avignon"},
            {"title": "Dissolution of the Knights Templar (1312) at French instigation enriched the French crown and set a precedent for secular suppression of religious orders", "type": "EventWindow", "year": "1307–1312, France"},
            {"title": "Precedent for secular states asserting sovereignty over church affairs, accelerating the Gallican tradition and later Reformation arguments", "type": "Idea", "year": "c. 1303–1517, Europe"},
        ],
        "relationships": [
            {"targetSlug": "philip-iv-of-france", "verb": "INFLUENCES", "note": "Nogaret was Philip IV's chief legal adviser and the executor of his anti-papal strategy"},
            {"targetSlug": "pope-boniface-viii", "verb": "INFLUENCES", "note": "Nogaret orchestrated the attack on Anagni that broke Boniface VIII's political authority"},
            {"targetSlug": "knights-templar", "verb": "INFLUENCES", "note": "Nogaret orchestrated the arrest, trial, and dissolution of the Knights Templar 1307–1312"},
            {"targetSlug": "avignon-papacy", "verb": "CAUSES", "note": "The Anagni affair and French dominance Nogaret helped establish led directly to the Avignon papacy"},
            {"targetSlug": "unam-sanctam", "verb": "INFLUENCES", "note": "Unam Sanctam was the papal overreach Nogaret used to justify his confrontational strategy"},
        ],
        "places": ["Paris, France", "Anagni, Italy"],
        "subjects": ["Law", "Medieval France", "Papal History", "Church and State", "Royal Sovereignty", "13th Century", "14th Century"],
        "subjectHeadings": "Jurisprudence — Royal Governance — France — Medieval",
        "frameworks": ["political-history", "church-state-relations"],
        "born": "c. 1260",
        "died": "11 April 1313",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Nogaret's assault on Boniface VIII at Anagni was one of the most audacious acts in medieval political history, shattering the papacy's claim to supremacy over secular rulers and opening the path to national sovereign churches.",
            "significanceCategory": "continental"
        },
    },
    "antoine-duprat": {
        "summary": (
            "Antoine Duprat (1463–1535) was a French jurist, royal chancellor, and cardinal "
            "who served Francis I of France as the chief architect of the Concordat of Bologna "
            "(1516) — a landmark agreement between France and the papacy that gave the French "
            "crown control over ecclesiastical appointments for nearly three centuries.\n\n"
            "Born into a legal family in Issoire and trained in Roman law, Duprat rose rapidly "
            "through the French judicial system, becoming First President of the Parlement of "
            "Paris in 1507 and Chancellor of France in 1515. His greatest achievement was "
            "negotiating the Concordat of Bologna with Pope Leo X after Francis I's Italian "
            "victory at Marignano, replacing the Pragmatic Sanction of Bourges (1438) with an "
            "agreement granting the king the right to nominate bishops and abbots in France — "
            "making the French church in practice a crown institution. This 'Gallican' arrangement "
            "persisted until the Revolution.\n\n"
            "Duprat also presided over the trial of Lutheran heretics and built the magnificent "
            "château of Nantouillet. Ordained a priest only after his wife's death, he became "
            "Archbishop of Sens and a cardinal in 1527, combining the highest offices of church "
            "and state in one formidable career."
        ),
        "causes": [
            {"title": "French military victory at Marignano (1515) gave Francis I the leverage to renegotiate French relations with Rome from a position of strength", "type": "EventWindow", "year": "1515, Marignano"},
            {"title": "Pragmatic Sanction of Bourges (1438) had established French autonomy from Rome but created ongoing tension with the papacy that needed resolution", "type": "Text", "year": "1438, Bourges"},
            {"title": "Duprat's mastery of Roman law and his position as Chancellor gave him the legal tools and political authority to negotiate with Leo X", "type": "Institution", "year": "1515–1516, France"},
        ],
        "effects": [
            {"title": "Concordat of Bologna (1516) gave the French crown control over episcopal appointments, subordinating the French church to royal patronage until 1789", "type": "Text", "year": "1516, Bologna"},
            {"title": "Gallican church established as a permanent institution — Catholic in doctrine but controlled by the French crown, insulating France from Protestant Reformation", "type": "Institution", "year": "1516–1789, France"},
            {"title": "French bishops and abbots became creatures of royal patronage, entrenching crown-church alliance and preventing an independent French Reformation", "type": "Idea", "year": "c. 1516–1789, France"},
        ],
        "relationships": [
            {"targetSlug": "francis-i-of-france", "verb": "INFLUENCES", "note": "Duprat served as Chancellor and chief legal adviser to Francis I, executing his ecclesiastical policy"},
            {"targetSlug": "pope-leo-x", "verb": "INFLUENCES", "note": "Duprat negotiated the Concordat of Bologna with Leo X, reshaping Franco-papal relations"},
            {"targetSlug": "concordat-of-bologna", "verb": "CAUSES", "note": "Duprat was the chief negotiator and drafter of the Concordat of Bologna"},
            {"targetSlug": "gallicanism", "verb": "CAUSES", "note": "The Concordat institutionalised Gallican control of the French church by the crown"},
        ],
        "places": ["Paris, France", "Bologna, Italy"],
        "subjects": ["Law", "France", "Papal History", "Church and State", "16th Century", "Gallicanism", "French Monarchy", "Concordat of Bologna"],
        "subjectHeadings": "Jurisprudence — Royal Governance — France — Early Modern",
        "frameworks": ["political-history", "church-state-relations"],
        "born": "17 January 1463",
        "died": "9 July 1535",
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Duprat's Concordat of Bologna made the French church a pillar of royal power for 273 years and ensured France remained Catholic while much of Europe broke with Rome — a defining act of Early Modern statecraft.",
            "significanceCategory": "continental"
        },
    },
    "julius-paulus": {
        "summary": (
            "Julius Paulus (c. 160–235 CE) was one of the most prolific and influential jurists "
            "of classical Roman law, whose writings — numbering some 80 works and over 300 books "
            "— constitute the largest surviving corpus from any single Roman jurist and account "
            "for roughly one-sixth of Justinian's Digest.\n\n"
            "A student of Cervidius Scaevola and contemporary of Ulpian, Paulus rose to become "
            "Praetorian Prefect under Emperor Alexander Severus. His most widely read work, the "
            "Sententiae Receptae (Received Opinions), was a concise, practical compendium of "
            "legal rulings that remained in use across the post-Roman West for centuries and was "
            "included in the Visigothic Breviary (506 CE). He addressed virtually every branch "
            "of Roman law — property, obligations, procedure, criminal law, and constitutional "
            "questions — in encyclopaedic commentaries on the Edict and on Sabinus.\n\n"
            "Paulus represents the pinnacle of the classical juristic tradition: rigorous in "
            "method, encyclopaedic in scope, and relentlessly practical. His influence on "
            "Justinian's codification made him, alongside Ulpian, one of the two supreme "
            "authorities of Roman law that later European legal systems drew upon."
        ),
        "causes": [
            {"title": "Severan dynasty's patronage of legal scholarship created the institutional conditions for prolific juristic output", "type": "Institution", "year": "c. 193–235, Rome"},
            {"title": "Classical juristic tradition of Scaevola and Papinian provided Paulus with methodological models and unsolved problems to address", "type": "Idea", "year": "c. 150–200, Rome"},
            {"title": "Growth of Roman imperial bureaucracy required codified legal opinions to guide provincial administrators", "type": "EventWindow", "year": "c. 200–235, Roman Empire"},
        ],
        "effects": [
            {"title": "Sententiae Receptae circulated widely in post-Roman West, preserved in the Visigothic Breviary (506) and influencing early medieval law", "type": "Text", "year": "c. 300–600, Western Europe"},
            {"title": "Paulus's writings constituted roughly one-sixth of Justinian's Digest, embedding his jurisprudence in the foundation of all civil law systems", "type": "Text", "year": "533, Constantinople"},
            {"title": "His encyclopaedic commentaries on the Praetorian Edict became the reference works for later Byzantine and medieval jurists", "type": "Text", "year": "c. 220–533, Rome/Byzantine Empire"},
        ],
        "relationships": [
            {"targetSlug": "corpus-juris-civilis", "verb": "TRANSMITS", "note": "Paulus's writings comprise approximately one-sixth of Justinian's Digest"},
            {"targetSlug": "ulpian", "verb": "INFLUENCES", "note": "Paulus and Ulpian were the two dominant classical jurists whose works dominated the Digest"},
            {"targetSlug": "irnerius", "verb": "INFLUENCES", "note": "The Paulus texts transmitted through the Digest were central to the Glossator study Irnerius pioneered"},
            {"targetSlug": "visigothic-code", "verb": "INFLUENCES", "note": "Paulus's Sententiae were incorporated in the Visigothic Breviary, transmitting Roman law to the medieval West"},
        ],
        "places": ["Rome, Italy", "Roman Empire"],
        "subjects": ["Law", "Roman Law", "Classical Antiquity", "Jurisprudence", "Corpus Juris Civilis", "Roman Empire", "3rd Century"],
        "subjectHeadings": "Jurisprudence — Roman Law — Rome — Classical",
        "frameworks": ["intellectual-history", "legal-history"],
        "born": "c. 160 CE",
        "died": "c. 235 CE",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Julius Paulus was the most prolific classical Roman jurist and, through his dominance of Justinian's Digest, one of the two supreme authorities (with Ulpian) on whom all subsequent European civil law was based.",
            "significanceCategory": "world-changing"
        },
    },
    "alfenus-varus": {
        "summary": (
            "Publius Alfenus Varus (fl. c. 70–30 BCE) was a Roman jurist of the late Republic "
            "who served as consul in 39 BCE and was the most distinguished pupil of Servius "
            "Sulpicius Rufus, the founder of the systematic study of Roman private law. Alfenus "
            "is celebrated for his Digesta — forty books of legal opinions — which constituted "
            "the earliest juristic work to be included in Justinian's sixth-century compilation.\n\n"
            "Originally from Cremona and reportedly a cobbler before coming to Rome, Alfenus "
            "embodied the meritocratic possibilities of Roman legal education. As a student of "
            "Servius, he absorbed the new analytical method his master had introduced — reasoning "
            "from principles rather than merely citing custom — and applied it in his multi-volume "
            "Digesta. These opinions addressed complex questions of sale, lease, tort, and "
            "inheritance with a conciseness and logical precision that later jurists admired. "
            "Several of his opinions survive verbatim in Justinian's Digest.\n\n"
            "His political career culminated in the consulship of 39 BCE, making him one of the "
            "very few Roman jurists to have held the highest magistracy. The poet Virgil mourned "
            "his death in the Eclogues, a rare tribute that speaks to his stature in Augustan Rome."
        ),
        "causes": [
            {"title": "Teaching of Servius Sulpicius Rufus introduced a systematic, analytical method to Roman legal science that Alfenus inherited and developed", "type": "Person", "year": "c. 70–50 BCE, Rome"},
            {"title": "Late Republic's social mobility allowed provincials of humble origin to rise through legal mastery to the highest offices", "type": "EventWindow", "year": "c. 80–40 BCE, Rome"},
        ],
        "effects": [
            {"title": "Alfenus's Digesta (40 books) preserved his legal opinions and were excerpted directly in Justinian's sixth-century Digest", "type": "Text", "year": "c. 50 BCE–533 CE"},
            {"title": "Analytical method inherited from Servius was refined by Alfenus and transmitted through the Proculian school to later classical jurists", "type": "Idea", "year": "c. 40 BCE–200 CE, Rome"},
        ],
        "relationships": [
            {"targetSlug": "servius-sulpicius-rufus", "verb": "INFLUENCES", "note": "Alfenus was the chief pupil of Servius and continued his systematic legal method"},
            {"targetSlug": "corpus-juris-civilis", "verb": "TRANSMITS", "note": "Alfenus's Digesta was excerpted in Justinian's Digest — the earliest jurist represented there"},
            {"targetSlug": "julius-paulus", "verb": "INFLUENCES", "note": "Alfenus's analytical tradition fed into the classical juristic school culminating in Paulus and Ulpian"},
        ],
        "places": ["Rome, Italy", "Cremona, Italy"],
        "subjects": ["Law", "Roman Law", "Classical Antiquity", "Jurisprudence", "Roman Republic", "1st Century BCE"],
        "subjectHeadings": "Jurisprudence — Roman Law — Rome — Classical",
        "frameworks": ["intellectual-history", "legal-history"],
        "born": "c. 105 BCE",
        "died": "c. 24 BCE",
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Alfenus Varus was the earliest jurist included in Justinian's Digest and a key transmitter of the systematic legal method Servius Sulpicius Rufus introduced — bridging the late Republic to the classical juristic tradition.",
            "significanceCategory": "regional"
        },
    },
    "gaius-aquilius-gallus": {
        "summary": (
            "Gaius Aquilius Gallus (c. 140–66 BCE) was a Roman praetor, jurist, and the "
            "most creative legal technician of the late Roman Republic, credited with inventing "
            "the actio doli — the action for fraud — one of the most consequential procedural "
            "innovations in the history of Roman law.\n\n"
            "A colleague and close friend of Cicero and a pupil of Quintus Mucius Scaevola, "
            "Gallus served as praetor peregrinus in 66 BCE, the magistrate responsible for "
            "disputes involving non-citizens. In that role — and through his juristic writings — "
            "he developed several major legal remedies: the actio doli (fraud), the stipulatio "
            "Aquiliana (a procedural device for settling complex multiple obligations), and the "
            "exceptio doli (the fraud defence). These tools allowed Roman law to address "
            "bad-faith conduct that earlier, formalistic remedies could not reach, transforming "
            "the law of obligations from rigid formulas into a flexible instrument of justice.\n\n"
            "Gallus's innovations were adopted universally in Roman private law and were "
            "preserved in Justinian's Digest, where they influenced every subsequent civil law "
            "system's treatment of fraud, unjust enrichment, and equitable defences."
        ),
        "causes": [
            {"title": "Growth of commercial activity between citizens and non-citizens in Rome exposed the inadequacy of formalistic civil law remedies for fraud", "type": "EventWindow", "year": "c. 100–66 BCE, Rome"},
            {"title": "Praetorian edict system gave creative magistrates the power to develop new legal actions when existing law was insufficient", "type": "Institution", "year": "c. 200–50 BCE, Rome"},
            {"title": "Teaching of Quintus Mucius Scaevola provided Gallus with systematic juristic method to deploy in his procedural innovations", "type": "Person", "year": "c. 120–90 BCE, Rome"},
        ],
        "effects": [
            {"title": "Actio doli (action for fraud) gave Roman law a general remedy against bad-faith conduct, transforming the law of obligations", "type": "Idea", "year": "66 BCE onwards, Roman Empire"},
            {"title": "Stipulatio Aquiliana became the standard procedural device for settling complex multi-party obligations", "type": "Idea", "year": "66 BCE onwards, Roman Empire"},
            {"title": "Gallus's remedies preserved in the Digest were adopted across all civil law systems and underlie modern fraud and unjust enrichment law", "type": "Text", "year": "533 CE–present, Europe"},
        ],
        "relationships": [
            {"targetSlug": "cicero", "verb": "INFLUENCES", "note": "Gallus and Cicero were colleagues who influenced each other's legal and rhetorical thinking"},
            {"targetSlug": "servius-sulpicius-rufus", "verb": "INFLUENCES", "note": "Gallus and Servius were contemporaries at the peak of Republican juristic activity"},
            {"targetSlug": "corpus-juris-civilis", "verb": "TRANSMITS", "note": "Gallus's actio doli and stipulatio Aquiliana were preserved in Justinian's Digest"},
            {"targetSlug": "alfenus-varus", "verb": "INFLUENCES", "note": "Gallus and Alfenus Varus both belonged to the late Republican school that shaped classical jurisprudence"},
        ],
        "places": ["Rome, Italy"],
        "subjects": ["Law", "Roman Law", "Classical Antiquity", "Jurisprudence", "Roman Republic", "Fraud Law", "1st Century BCE"],
        "subjectHeadings": "Jurisprudence — Roman Law — Rome — Classical",
        "frameworks": ["intellectual-history", "legal-history"],
        "born": "c. 140 BCE",
        "died": "c. 66 BCE",
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Gallus invented the actio doli — the general action for fraud — transforming Roman law from a rigid formalism into a flexible instrument capable of policing bad faith, a contribution preserved in every civil law system.",
            "significanceCategory": "regional"
        },
    },
}


# ── helpers ─────────────────────────────────────────────────────────────────

import unicodedata


def _norm(s: str) -> str:
    table = str.maketrans({
        'ł': 'l', 'Ł': 'L', 'ø': 'o', 'Ø': 'O', 'ð': 'd', 'Ð': 'D',
        'þ': 'th', 'ß': 'ss', 'æ': 'ae', 'Æ': 'Ae', 'đ': 'd', 'Đ': 'D',
        'ħ': 'h', 'Ħ': 'H', 'ı': 'i', 'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O',
        'ä': 'a', 'Ä': 'A', 'é': 'e', 'É': 'E', 'è': 'e', 'È': 'E', 'ê': 'e',
        'ó': 'o', 'Ó': 'O', 'ñ': 'n', 'Ñ': 'N', 'í': 'i', 'Í': 'I', 'á': 'a',
        'Á': 'A', 'ú': 'u', 'Ú': 'U', 'ã': 'a', 'õ': 'o', 'ç': 'c', 'Ç': 'C',
        'ș': 's', 'ț': 't', 'ř': 'r', 'š': 's', 'č': 'c', 'ž': 'z', 'ý': 'y',
        'ń': 'n', 'ś': 's', 'ź': 'z', 'ż': 'z', 'ą': 'a', 'ę': 'e',
    })
    s = s.translate(table)
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("ascii").lower()


def find_file(slug: str) -> str | None:
    direct = os.path.join(FOLDER, f"231{slug}.json")
    if os.path.exists(direct):
        return direct
    norm_slug = _norm(slug)
    for fname in os.listdir(FOLDER):
        if fname.endswith(".json") and fname.startswith("231"):
            if _norm(fname[3:-5]) == norm_slug:
                return os.path.join(FOLDER, fname)
    return None


def apply_enrichment(slug: str, enrichment: dict) -> bool:
    path = find_file(slug)
    if not path:
        print(f"  SKIP {slug} — file not found in {FOLDER}")
        return False

    with open(path) as fh:
        doc = json.load(fh)

    entities = doc.get("entities", [])
    if not entities:
        print(f"  SKIP {slug} — empty entities array")
        return False

    entity = entities[0]
    old_summary = entity.get("summary") or ""
    edit_log = entity.get("_editLog") or []

    for field, new_val in enrichment.items():
        old_val = entity.get(field)
        if old_val != new_val:
            edit_log.append({
                "field": field,
                "old": old_val,
                "new": new_val,
                "editor": EDITOR_ID,
                "ts": NOW,
            })
        entity[field] = new_val

    entity["_unsyncedEdits"] = True
    entity["_editLog"] = edit_log
    entity["status"] = "enriched"

    doc["entities"] = [entity]
    with open(path, "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)

    new_summary = entity.get("summary") or ""
    print(f"  OK  {slug:50}  {len(old_summary)}c → {len(new_summary)}c")
    return True


def main():
    print(f"Enriching {len(ENRICHMENTS)} entities in 231-Class-231 (Batch 3 — Roman/Medieval Jurists)...")
    ok = fail = 0
    for slug, enrichment in ENRICHMENTS.items():
        if apply_enrichment(slug, enrichment):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} enriched, {fail} skipped.")


if __name__ == "__main__":
    main()
