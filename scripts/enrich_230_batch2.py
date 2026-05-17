#!/usr/bin/env python3
"""
Batch 2 enrichment for 230-Class-230 entities.
Enriches 8 foundational common law jurists and legal figures.
Follows git-first bot rules: writes _unsyncedEdits=True + _editLog diffs.
"""

import json
import os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "henry-de-bracton": {
        "summary": (
            "Henry de Bracton (c. 1210–1268) was an English cleric, royal justice, and legal "
            "scholar who authored De Legibus et Consuetudinibus Angliae (On the Laws and Customs "
            "of England), the first comprehensive and systematic treatise on English common law. "
            "Written over several decades in the mid-13th century, this monumental work gave "
            "the common law its first systematic jurisprudential framework and earned Bracton "
            "enduring recognition as the 'father of the common law.'\n\n"
            "Bracton served as a royal judge on the circuits of England from the 1240s to the "
            "1260s, giving him direct experience of the law in practice as well as in theory. "
            "His treatise — approximately 500 chapters drawing on over 2,000 actual plea rolls "
            "— synthesized Roman and canon law concepts into the distinctively English legal "
            "tradition, insisting that the common law was a coherent system capable of scholarly "
            "articulation. His famous maxim 'Rex non debet esse sub homine, sed sub Deo et lege' "
            "('The king ought not to be under man, but under God and the law') became a "
            "touchstone of English constitutional thought for centuries.\n\n"
            "Bracton's work was quoted by Edward Coke in the 17th century to argue against "
            "royal absolutism, and it was cited in constitutional debates on both sides of the "
            "Atlantic through the American Revolution. Though later scholars found errors and "
            "interpolations in the manuscript tradition, De Legibus remains the foundational "
            "text of medieval English jurisprudence and a monument of legal scholarship."
        ),
        "causes": [
            {
                "title": "The growth of royal court litigation under Henry III created demand for systematic exposition of common law writs and procedures",
                "type": "Institution",
                "year": "c. 1230–1260, England"
            },
            {
                "title": "Reception of Roman and canon law at English universities provided Bracton with the jurisprudential tools to systematize English custom",
                "type": "Idea",
                "year": "c. 1210–1260, Oxford"
            },
            {
                "title": "Bracton's access to plea rolls as a royal justice gave him the empirical foundation of actual case precedents to draw on",
                "type": "EventWindow",
                "year": "c. 1240–1268, England"
            }
        ],
        "effects": [
            {
                "title": "De Legibus et Consuetudinibus Angliae established the first systematic treatise on English common law, shaping legal education and practice for centuries",
                "type": "Text",
                "year": "c. 1235–1259, England"
            },
            {
                "title": "Bracton's maxim 'Rex non debet esse sub homine sed sub Deo et lege' became a cornerstone of English constitutional thought",
                "type": "Idea",
                "year": "c. 1250–1800, England"
            },
            {
                "title": "Edward Coke's citation of Bracton in constitutional disputes with James I carried Bracton's authority into 17th-century constitutionalism",
                "type": "Person",
                "year": "1606–1628, England"
            },
            {
                "title": "Bracton's framework influenced American founding jurisprudence through Coke and Blackstone's references to his constitutional maxims",
                "type": "EventWindow",
                "year": "1776–1789, America"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "henry-de-bracton",
                "sourceName": "Henry de Bracton",
                "verb": "AUTHORED",
                "targetSlug": "de-legibus-et-consuetudinibus-angliae",
                "targetName": "De Legibus et Consuetudinibus Angliae",
                "context": "Bracton wrote the first comprehensive treatise on English common law, c. 1235–1259"
            },
            {
                "sourceSlug": "henry-de-bracton",
                "sourceName": "Henry de Bracton",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-iii-of-england",
                "targetName": "Henry III of England",
                "context": "Bracton served as a royal justice under Henry III from the 1240s, gaining access to plea rolls for his research"
            },
            {
                "sourceSlug": "henry-de-bracton",
                "sourceName": "Henry de Bracton",
                "verb": "INFLUENCED",
                "targetSlug": "edward-coke",
                "targetName": "Edward Coke",
                "context": "Coke cited Bracton's 'Rex non debet esse sub homine, sed sub Deo et lege' in his constitutional confrontations with James I"
            },
            {
                "sourceSlug": "henry-de-bracton",
                "sourceName": "Henry de Bracton",
                "verb": "SYNTHESIZED",
                "targetSlug": "roman-law",
                "targetName": "Roman Law",
                "context": "Bracton drew heavily on Justinian's Digest and Institutes, incorporating Roman law concepts into the English legal framework"
            },
            {
                "sourceSlug": "henry-de-bracton",
                "sourceName": "Henry de Bracton",
                "verb": "DEFINED",
                "targetSlug": "english-common-law",
                "targetName": "English Common Law",
                "context": "De Legibus gave the common law its first systematic jurisprudential structure, establishing precedent-based reasoning"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Henry de Bracton's De Legibus et Consuetudinibus Angliae gave English common law its first systematic treatise, establishing the constitutional principle that the king is subject to law — a maxim that would resonate from Coke's confrontations with James I through the American founding.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "ranulf-de-glanvill": {
        "summary": (
            "Ranulf de Glanvill (c. 1130–1190) was Chief Justiciar of England from 1180 to 1189 "
            "and the probable author of Tractatus de Legibus et Consuetudinibus Regni Angliae "
            "(Treatise on the Laws and Customs of the Kingdom of England), the earliest surviving "
            "systematic treatise on English law. Written around 1187–1189, the Tractatus was the "
            "first attempt to explain the new system of royal writs and common law procedures "
            "that had developed under Henry II, and it remained the standard introduction to "
            "English law for a generation.\n\n"
            "As Chief Justiciar — the highest judicial and administrative office in the kingdom "
            "after the king — Glanvill presided over the development of the legal reforms that "
            "Henry II had introduced through the Assizes of Clarendon (1166) and Northampton "
            "(1176), which created systematic procedures for jury trial and the presentation of "
            "criminal cases. He also developed the system of royal writs that gave plaintiffs "
            "access to royal courts, centralizing English justice under the Crown. Glanvill's "
            "administration saw the common law emerge as a distinct, professional legal system "
            "accessible through standardized procedures.\n\n"
            "When Richard I came to the throne in 1189, Glanvill was succeeded in the "
            "justiciaryship, but he accompanied Richard on the Third Crusade, dying at the "
            "siege of Acre in 1190. His Tractatus — whether or not he wrote it personally — "
            "established the tradition of common law writing that Bracton would bring to "
            "systematic fruition half a century later."
        ),
        "causes": [
            {
                "title": "Henry II's legal reforms through the Assizes of Clarendon and Northampton created a new system of royal justice requiring exposition",
                "type": "EventWindow",
                "year": "1166–1176, England"
            },
            {
                "title": "The proliferation of royal writs as the mechanism for accessing royal courts demanded systematic explanation for practitioners",
                "type": "Institution",
                "year": "c. 1180s, England"
            },
            {
                "title": "Glanvill's position as Chief Justiciar gave him unparalleled insight into the emerging common law system and its writs",
                "type": "Person",
                "year": "1180–1189, England"
            }
        ],
        "effects": [
            {
                "title": "Tractatus de Legibus became the first systematic treatise on English law, establishing the tradition of common law writing",
                "type": "Text",
                "year": "c. 1187–1189, England"
            },
            {
                "title": "Glanvill's justiciaryship consolidated the common law court system, making royal justice the default forum for English disputes",
                "type": "Institution",
                "year": "1180–1189, England"
            },
            {
                "title": "The Tractatus served as the foundational text for English legal education until superseded by Bracton's more comprehensive work",
                "type": "Idea",
                "year": "1189–c. 1260, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "ranulf-de-glanvill",
                "sourceName": "Ranulf de Glanvill",
                "verb": "AUTHORED",
                "targetSlug": "tractatus-de-legibus",
                "targetName": "Tractatus de Legibus et Consuetudinibus Regni Angliae",
                "context": "Glanvill is the probable author of the first systematic treatise on English common law, c. 1187–1189"
            },
            {
                "sourceSlug": "ranulf-de-glanvill",
                "sourceName": "Ranulf de Glanvill",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-ii-of-england",
                "targetName": "Henry II of England",
                "context": "Glanvill served as Chief Justiciar under Henry II from 1180 to 1189, overseeing his legal reforms"
            },
            {
                "sourceSlug": "ranulf-de-glanvill",
                "sourceName": "Ranulf de Glanvill",
                "verb": "IMPLEMENTED",
                "targetSlug": "assizes-of-clarendon",
                "targetName": "Assizes of Clarendon",
                "context": "As Chief Justiciar, Glanvill implemented Henry II's Assizes, systematizing jury trial and criminal procedure"
            },
            {
                "sourceSlug": "ranulf-de-glanvill",
                "sourceName": "Ranulf de Glanvill",
                "verb": "INFLUENCED",
                "targetSlug": "henry-de-bracton",
                "targetName": "Henry de Bracton",
                "context": "Bracton built on Glanvill's Tractatus when composing his own more systematic De Legibus in the mid-13th century"
            },
            {
                "sourceSlug": "ranulf-de-glanvill",
                "sourceName": "Ranulf de Glanvill",
                "verb": "OCCURS_DURING",
                "targetSlug": "third-crusade",
                "targetName": "Third Crusade",
                "context": "Glanvill died at the siege of Acre in 1190 while accompanying Richard I on the Third Crusade"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Ranulf de Glanvill's Tractatus — the first systematic exposition of English common law and the royal writ system — established the tradition of common law writing and the professional legal culture that would define English and eventually Anglo-American jurisprudence.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "edward-coke": {
        "summary": (
            "Sir Edward Coke (1552–1634) was an English barrister, judge, and parliamentarian "
            "widely regarded as the greatest jurist of the Elizabethan and Jacobean eras. His "
            "voluminous Institutes of the Laws of England (4 volumes) and thirteen volumes of "
            "Reports systematized the common law and became the foundational texts for legal "
            "education in England and America for over two centuries. More than any other "
            "individual, Coke shaped the idea that the common law was a supreme constitutional "
            "constraint on both Crown and Parliament.\n\n"
            "Coke served as Solicitor General, Attorney General (prosecuting Essex, Raleigh, and "
            "the Gunpowder Plot conspirators), Chief Justice of the Common Pleas (1606–1613), "
            "and Chief Justice of the King's Bench (1613–1616). His pivotal confrontation with "
            "James I came in 1608 and 1616, when he asserted that the King had no right to "
            "withdraw cases from common law courts, invoking Bracton's maxim that the king is "
            "under God and the law. James dismissed him from office in 1616. Undeterred, Coke "
            "returned to Parliament, where he championed the Petition of Right (1628), the "
            "foundational constitutional document asserting parliamentary supremacy over "
            "arbitrary imprisonment and taxation.\n\n"
            "Coke's Institutes and Reports traveled to America with the colonists and became "
            "the primary legal education of Founding Fathers including Jefferson, Hamilton, "
            "and Adams. His articulation of due process, judicial review, natural rights, "
            "and the rule of law directly shaped the United States Constitution and Bill of "
            "Rights. His famous aphorism — 'an Englishman's house is his castle' — entered "
            "common law as a principle of privacy and security against arbitrary state power."
        ),
        "causes": [
            {
                "title": "James I's belief in the divine right of kings clashed directly with Coke's common law constitutionalism",
                "type": "Person",
                "year": "1606–1616, England"
            },
            {
                "title": "The rapid proliferation of royal prerogative courts (Star Chamber, High Commission) threatened the jurisdiction of common law courts",
                "type": "Institution",
                "year": "c. 1580–1616, England"
            },
            {
                "title": "Coke's decades of legal practice and judicial experience gave him unparalleled command of the common law's precedents and principles",
                "type": "Person",
                "year": "1578–1616, England"
            }
        ],
        "effects": [
            {
                "title": "Coke's Institutes and Reports became the foundational texts of English and American common law education for two centuries",
                "type": "Text",
                "year": "1628–1644, England"
            },
            {
                "title": "His Petition of Right (1628) established parliamentary limits on royal arbitrary arrest, taxation, and billeting of troops",
                "type": "EventWindow",
                "year": "1628, England"
            },
            {
                "title": "Coke's constitutional arguments were adopted by American revolutionaries as the jurisprudential foundation for independence from parliamentary tyranny",
                "type": "EventWindow",
                "year": "1776, America"
            },
            {
                "title": "Bonham's Case (1610) established the germ of judicial review — that courts could strike down Acts of Parliament contrary to common right",
                "type": "Idea",
                "year": "1610, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "OPPOSED",
                "targetSlug": "james-i-of-england",
                "targetName": "James I of England",
                "context": "Coke's assertion that the King was under the law, not above it, led to his dismissal as Chief Justice in 1616"
            },
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "AUTHORED",
                "targetSlug": "institutes-of-the-laws-of-england",
                "targetName": "Institutes of the Laws of England",
                "context": "Coke's four-volume Institutes became the bible of common law education in England and America"
            },
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "CHAMPIONED",
                "targetSlug": "petition-of-right",
                "targetName": "Petition of Right",
                "context": "Coke was the principal architect of the 1628 Petition of Right, the foundational constitutional document of parliamentary liberties"
            },
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "INFLUENCED",
                "targetSlug": "american-founding",
                "targetName": "American Founding",
                "context": "Coke's Institutes were the primary legal education of Jefferson, Adams, and Hamilton; his constitutional ideas shaped the US Bill of Rights"
            },
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "CITED",
                "targetSlug": "henry-de-bracton",
                "targetName": "Henry de Bracton",
                "context": "Coke invoked Bracton's 'Rex non debet esse sub homine' in his constitutional arguments against James I"
            },
            {
                "sourceSlug": "edward-coke",
                "sourceName": "Edward Coke",
                "verb": "DEFINED",
                "targetSlug": "rule-of-law",
                "targetName": "Rule of Law",
                "context": "Coke's jurisprudence established that no person — including the king — was above the common law"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Edward Coke's fusion of common law constitutionalism, judicial independence, and parliamentary supremacy made him the most influential jurist in the Anglo-American legal tradition, his Institutes shaping two centuries of legal education and his constitutional principles underpinning both the English Revolution and the American founding.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "thomas-audley-1st-baron-audley-of-walden": {
        "summary": (
            "Thomas Audley, 1st Baron Audley of Walden (c. 1488–1544) was an English lawyer, "
            "judge, and royal minister who served as Lord Chancellor of England from 1533 to 1544 "
            "— the entire decade of Henry VIII's most radical break with Rome. A skilled legal "
            "draftsman who rose through the Inns of Court and Parliament, Audley became the "
            "indispensable parliamentary manager who steered Henry VIII's Reformation legislation "
            "through Parliament and presided over the trials of Henry's most famous victims.\n\n"
            "Audley served as Speaker of the House of Commons (1529–1532) before succeeding "
            "Thomas More as Lord Chancellor when More resigned over the break with Rome. As "
            "Chancellor, Audley presided over the legislation that established royal supremacy "
            "over the Church of England — the Act of Supremacy (1534), the Treason Act (1534), "
            "and the acts dissolving the monasteries (1536, 1539). He also presided as a judge "
            "at the trials of Bishop John Fisher and Thomas More in 1535, and at the trial of "
            "Anne Boleyn and her alleged co-conspirators in 1536 — proceedings widely regarded "
            "as legally improper manipulations of Tudor law.\n\n"
            "Audley was rewarded with a peerage (Baron Audley of Walden, 1538) and extensive "
            "monastic lands. He founded Magdalene College, Cambridge in 1542 — a foundation "
            "that survives as one of Cambridge's historic colleges. His career exemplified the "
            "type of legally trained, politically compliant royal servant that Tudor governance "
            "depended upon: a man who placed Crown service above personal scruples in an age "
            "when resistance meant death."
        ),
        "causes": [
            {
                "title": "Henry VIII's determination to annul his marriage to Catherine of Aragon required a Lord Chancellor willing to manage Reformation legislation through Parliament",
                "type": "EventWindow",
                "year": "1532–1534, England"
            },
            {
                "title": "Thomas More's resignation over the break with Rome created the vacancy that a more compliant lawyer — Audley — was needed to fill",
                "type": "Person",
                "year": "1532, England"
            },
            {
                "title": "Audley's career as a parliamentary draftsman and Speaker made him the natural choice to manage the complex legislation of the English Reformation",
                "type": "Institution",
                "year": "1529–1532, England"
            }
        ],
        "effects": [
            {
                "title": "Audley steered the Act of Supremacy (1534) through Parliament, legally establishing Henry VIII as Supreme Head of the Church of England",
                "type": "EventWindow",
                "year": "1534, England"
            },
            {
                "title": "Presided at the trials of Thomas More and John Fisher in 1535, and Anne Boleyn in 1536 — legal proceedings that remain controversial for their procedural propriety",
                "type": "EventWindow",
                "year": "1535–1536, London"
            },
            {
                "title": "Founded Magdalene College, Cambridge (1542), which survives as one of Cambridge's historic institutions",
                "type": "Institution",
                "year": "1542, Cambridge"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thomas-audley-1st-baron-audley-of-walden",
                "sourceName": "Thomas Audley",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-viii-of-england",
                "targetName": "Henry VIII of England",
                "context": "Audley was Henry VIII's Lord Chancellor throughout the decade of the English Reformation, 1533–1544"
            },
            {
                "sourceSlug": "thomas-audley-1st-baron-audley-of-walden",
                "sourceName": "Thomas Audley",
                "verb": "SUCCEEDED",
                "targetSlug": "thomas-more",
                "targetName": "Thomas More",
                "context": "Audley succeeded More as Lord Chancellor in 1532 when More resigned over the break with Rome"
            },
            {
                "sourceSlug": "thomas-audley-1st-baron-audley-of-walden",
                "sourceName": "Thomas Audley",
                "verb": "PRESIDED_OVER",
                "targetSlug": "trial-of-thomas-more",
                "targetName": "Trial of Thomas More",
                "context": "Audley was one of the judges presiding over More's trial for treason in 1535"
            },
            {
                "sourceSlug": "thomas-audley-1st-baron-audley-of-walden",
                "sourceName": "Thomas Audley",
                "verb": "FOUNDED",
                "targetSlug": "magdalene-college-cambridge",
                "targetName": "Magdalene College, Cambridge",
                "context": "Audley founded Magdalene College, Cambridge in 1542, using wealth accumulated from dissolved monastic properties"
            },
            {
                "sourceSlug": "thomas-audley-1st-baron-audley-of-walden",
                "sourceName": "Thomas Audley",
                "verb": "ENACTED",
                "targetSlug": "act-of-supremacy-1534",
                "targetName": "Act of Supremacy (1534)",
                "context": "As Lord Chancellor, Audley managed the Act of Supremacy through Parliament, establishing Henry VIII as head of the English Church"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Thomas Audley's decade as Lord Chancellor provided the legal machinery for the English Reformation, steering the acts of supremacy and dissolution through Parliament while presiding over the politically driven trials that eliminated Henry VIII's principal opponents.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "ulrich-zasius": {
        "summary": (
            "Ulrich Zasius (1461–1535) was a German jurist and humanist scholar who became one "
            "of the leading legal minds of the early 16th century, pioneering the application of "
            "Renaissance humanist philological methods to the study of Roman law. A native of "
            "Constance, he studied law and eventually became Professor of Law at the University "
            "of Freiburg im Breisgau, where he taught for nearly four decades and transformed "
            "legal scholarship in German-speaking Europe.\n\n"
            "Zasius was a central figure in what historians call legal humanism (mos gallicus) — "
            "the movement to replace the medieval scholastic approach to Roman law (mos italicus) "
            "with a historically critical reading of the original classical texts. He applied "
            "the philological methods of Erasmus and other Northern humanists to Justinian's "
            "Corpus Juris Civilis, seeking to understand Roman law in its historical context "
            "rather than through medieval glossators. His friendship and correspondence with "
            "Erasmus, and his place alongside Guillaume Budé and Andrea Alciato as a founder "
            "of legal humanism, cemented his European reputation. His collected works, Lucubrationes "
            "(1518), were widely read across the continent.\n\n"
            "Zasius's humanist jurisprudence had practical as well as scholarly dimensions: he "
            "advised the city of Freiburg on legal matters and wrote extensively on municipal "
            "law, Jewish legal status, and the reception of Roman law into German urban "
            "governance. His career exemplified how Renaissance humanism transformed not only "
            "classical scholarship but also the practical science of law in early modern Europe."
        ),
        "causes": [
            {
                "title": "Northern European Renaissance humanism, particularly Erasmus's philological methods, provided Zasius with tools to historicize Roman legal texts",
                "type": "Movement",
                "year": "c. 1490–1510, Europe"
            },
            {
                "title": "The stagnation of scholastic legal commentary (mos italicus) created an opening for a historically critical approach to Roman law",
                "type": "Idea",
                "year": "c. 1480–1510, Europe"
            },
            {
                "title": "The University of Freiburg provided Zasius with an institutional platform to develop and disseminate humanist jurisprudence",
                "type": "Institution",
                "year": "1496–1535, Freiburg im Breisgau"
            }
        ],
        "effects": [
            {
                "title": "Zasius's Lucubrationes (1518) established legal humanism as a viable scholarly movement in German-speaking Europe",
                "type": "Text",
                "year": "1518, Freiburg"
            },
            {
                "title": "His influence helped shift German legal education from scholastic toward humanist methods during the early 16th century",
                "type": "Institution",
                "year": "c. 1510–1550, Germany"
            },
            {
                "title": "Zasius's approach to Roman law influenced Guillaume Budé in France and contributed to the broader 'mos gallicus' tradition that shaped European jurisprudence",
                "type": "Movement",
                "year": "c. 1510–1600, Europe"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "ulrich-zasius",
                "sourceName": "Ulrich Zasius",
                "verb": "CORRESPONDED_WITH",
                "targetSlug": "desiderius-erasmus",
                "targetName": "Desiderius Erasmus",
                "context": "Zasius and Erasmus maintained a scholarly correspondence, and Erasmus praised Zasius as the foremost jurist of Germany"
            },
            {
                "sourceSlug": "ulrich-zasius",
                "sourceName": "Ulrich Zasius",
                "verb": "TAUGHT_AT",
                "targetSlug": "university-of-freiburg",
                "targetName": "University of Freiburg im Breisgau",
                "context": "Zasius taught law at Freiburg for nearly four decades, making it a center of humanist jurisprudence in Germany"
            },
            {
                "sourceSlug": "ulrich-zasius",
                "sourceName": "Ulrich Zasius",
                "verb": "PIONEERED",
                "targetSlug": "legal-humanism",
                "targetName": "Legal Humanism (mos gallicus)",
                "context": "Zasius was one of the founders of legal humanism, applying philological methods to Roman law alongside Budé and Alciato"
            },
            {
                "sourceSlug": "ulrich-zasius",
                "sourceName": "Ulrich Zasius",
                "verb": "AUTHORED",
                "targetSlug": "lucubrationes-zasius",
                "targetName": "Lucubrationes (1518)",
                "context": "Zasius's collected legal writings were published in 1518 and widely circulated across Europe"
            },
            {
                "sourceSlug": "ulrich-zasius",
                "sourceName": "Ulrich Zasius",
                "verb": "INFLUENCED",
                "targetSlug": "guillaume-bude",
                "targetName": "Guillaume Budé",
                "context": "Zasius and Budé were fellow pioneers of legal humanism, each influencing the other's approach to classical legal texts"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ulrich Zasius pioneered the application of Renaissance humanist methods to Roman law in German-speaking Europe, helping transform legal scholarship from medieval scholasticism to historically critical jurisprudence — a shift that reshaped European legal education for centuries.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "john-fortescue": {
        "summary": (
            "Sir John Fortescue (c. 1394–c. 1479) was an English jurist, Chief Justice of the "
            "King's Bench (1442–1461), and political philosopher whose writings articulated the "
            "first systematic defence of English constitutional monarchy over absolute royal "
            "power. His distinction between dominium regale (absolute kingship) and dominium "
            "politicum et regale (kingship limited by law and parliament) profoundly influenced "
            "English and subsequently American constitutional thought.\n\n"
            "Fortescue served Henry VI as Chief Justice throughout the turbulent middle of the "
            "15th century, before his Lancastrian loyalties forced him into exile after the "
            "Yorkist victory at Towton in 1461. He spent over a decade in exile in France and "
            "Scotland, accompanying Henry VI's court-in-exile. During this period he wrote his "
            "most influential works: De Laudibus Legum Angliae (In Praise of the Laws of "
            "England, c. 1468–1471, published 1543), written as a dialogue with Henry VI's "
            "young son Edward, and The Governance of England (c. 1471–1476), an analysis of "
            "English constitutional arrangements. Both works argued that England's constitution, "
            "with its Parliament and common law, protected subjects' property and liberty far "
            "better than the absolute monarchies of France.\n\n"
            "Fortescue returned to England after the Lancastrian cause collapsed, submitting to "
            "Edward IV and recanting his political writings. Yet his ideas survived intact and "
            "were rediscovered in the 16th and 17th centuries as foundational arguments for "
            "parliamentary government. John Adams cited Fortescue when arguing the American "
            "colonial position before the Revolution, and his concept of dominium politicum et "
            "regale became a touchstone of Anglo-American constitutionalism."
        ),
        "causes": [
            {
                "title": "The Wars of the Roses forced Fortescue into Lancastrian exile, giving him occasion to write systematic political philosophy comparing English and French governance",
                "type": "EventWindow",
                "year": "1461–1471, France and Scotland"
            },
            {
                "title": "The practical question of educating Henry VI's heir in the principles of English law motivated the dialogue form of De Laudibus",
                "type": "Person",
                "year": "c. 1468, France"
            },
            {
                "title": "Fortescue's three decades as Chief Justice gave him unparalleled practical knowledge of how English law and Parliament functioned",
                "type": "Institution",
                "year": "1442–1461, England"
            }
        ],
        "effects": [
            {
                "title": "De Laudibus Legum Angliae (published 1543) provided the foundational constitutional argument for English parliamentary government over royal absolutism",
                "type": "Text",
                "year": "c. 1468–1543, England"
            },
            {
                "title": "Fortescue's concept of dominium politicum et regale was cited by 17th-century parliamentarians against Stuart absolutism",
                "type": "Idea",
                "year": "1620s–1640s, England"
            },
            {
                "title": "John Adams cited Fortescue in colonial constitutional debates, carrying his ideas into the American founding",
                "type": "Person",
                "year": "1770s, America"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-fortescue",
                "sourceName": "John Fortescue",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-vi-of-england",
                "targetName": "Henry VI of England",
                "context": "Fortescue served as Chief Justice of the King's Bench under Henry VI from 1442 and followed him into exile after 1461"
            },
            {
                "sourceSlug": "john-fortescue",
                "sourceName": "John Fortescue",
                "verb": "AUTHORED",
                "targetSlug": "de-laudibus-legum-angliae",
                "targetName": "De Laudibus Legum Angliae",
                "context": "Fortescue wrote De Laudibus as a constitutional dialogue in exile c. 1468–1471, published posthumously in 1543"
            },
            {
                "sourceSlug": "john-fortescue",
                "sourceName": "John Fortescue",
                "verb": "DEFINED",
                "targetSlug": "dominium-politicum-et-regale",
                "targetName": "Dominium Politicum et Regale",
                "context": "Fortescue's distinction between absolute (regale) and constitutional (politicum et regale) kingship became the foundational framework for English constitutional theory"
            },
            {
                "sourceSlug": "john-fortescue",
                "sourceName": "John Fortescue",
                "verb": "INFLUENCED",
                "targetSlug": "edward-coke",
                "targetName": "Edward Coke",
                "context": "Coke and other common lawyers built on Fortescue's constitutional framework in their arguments against Stuart prerogative"
            },
            {
                "sourceSlug": "john-fortescue",
                "sourceName": "John Fortescue",
                "verb": "OCCURS_DURING",
                "targetSlug": "wars-of-the-roses",
                "targetName": "Wars of the Roses",
                "context": "Fortescue's political philosophy was largely developed during his Lancastrian exile following the Yorkist victory at Towton (1461)"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John Fortescue's articulation of English constitutional monarchy as dominium politicum et regale — government by law and parliament, not royal will alone — provided the foundational framework for the parliamentary constitutionalism that would define English and American governance.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "matthew-hale": {
        "summary": (
            "Sir Matthew Hale (1609–1676) was an English barrister, judge, and legal scholar "
            "who served as Chief Justice of the King's Bench (1671–1676) and left an enduring "
            "mark on English common law through his posthumously published treatises. His "
            "Historia Placitorum Coronæ (History of the Pleas of the Crown, published 1736) "
            "remained the standard English criminal law treatise for over a century, and his "
            "writings on evidence, criminal procedure, and the common law's history shaped "
            "legal practice well into the 19th century.\n\n"
            "Hale navigated the turbulent politics of the Civil War era with extraordinary care, "
            "defending both royalist clients (including Archbishop Laud and the Earl of Strafford) "
            "and parliamentarians, before serving as a judge under Cromwell's Interregnum "
            "government. After the Restoration, Charles II appointed him Chief Baron of the "
            "Exchequer (1660) and then Chief Justice of the King's Bench (1671). Hale was a "
            "deeply pious Puritan who wrote extensively on theology as well as law. His History "
            "of the Common Law of England (published 1713) provided the first scholarly account "
            "of English law's historical development from Anglo-Saxon custom through the "
            "common law's emergence under the Plantagenet kings.\n\n"
            "Hale's career is also marked by two enduring controversies. In 1662 he presided "
            "over the conviction and hanging of Amy Duny and Rose Cullender for witchcraft — "
            "a case cited in later American witch trials including Salem. His doctrine on "
            "marital rape — that a husband could not rape his wife because she had 'given "
            "herself' in marriage — was not formally overturned in English law until 1991, "
            "a reminder that influential jurists may leave problematic as well as positive legacies."
        ),
        "causes": [
            {
                "title": "The English Civil War and Interregnum forced practicing lawyers to navigate competing jurisdictions and loyalties, shaping Hale's pragmatic constitutionalism",
                "type": "EventWindow",
                "year": "1640–1660, England"
            },
            {
                "title": "The absence of a comprehensive criminal law treatise in English created the scholarly gap that Hale's posthumous Historia filled",
                "type": "Idea",
                "year": "c. 1640–1676, England"
            },
            {
                "title": "Hale's deep Puritan piety and commitment to learned legal scholarship drove him to synthesize law, history, and theology",
                "type": "Person",
                "year": "1609–1676, England"
            }
        ],
        "effects": [
            {
                "title": "Historia Placitorum Coronæ (1736) became the standard English criminal law treatise, shaping practice through the 19th century",
                "type": "Text",
                "year": "1736, England"
            },
            {
                "title": "History of the Common Law of England (1713) established the scholarly tradition of common law historiography",
                "type": "Text",
                "year": "1713, England"
            },
            {
                "title": "Hale's 1662 witchcraft conviction influenced similar proceedings in New England, including the Salem witch trials (1692)",
                "type": "EventWindow",
                "year": "1692, Salem, Massachusetts"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "matthew-hale",
                "sourceName": "Matthew Hale",
                "verb": "AUTHORED",
                "targetSlug": "historia-placitorum-coronae",
                "targetName": "Historia Placitorum Coronæ",
                "context": "Hale's History of the Pleas of the Crown, published posthumously in 1736, remained the standard English criminal law treatise for a century"
            },
            {
                "sourceSlug": "matthew-hale",
                "sourceName": "Matthew Hale",
                "verb": "SERVED_UNDER",
                "targetSlug": "charles-ii-of-england",
                "targetName": "Charles II of England",
                "context": "Hale served as Chief Baron of the Exchequer (1660) and Chief Justice of the King's Bench (1671–1676) under Charles II"
            },
            {
                "sourceSlug": "matthew-hale",
                "sourceName": "Matthew Hale",
                "verb": "INFLUENCED",
                "targetSlug": "william-blackstone",
                "targetName": "William Blackstone",
                "context": "Blackstone's Commentaries drew heavily on Hale's historical and doctrinal framework for English common law"
            },
            {
                "sourceSlug": "matthew-hale",
                "sourceName": "Matthew Hale",
                "verb": "PRESIDED_OVER",
                "targetSlug": "bury-st-edmunds-witch-trial",
                "targetName": "Bury St Edmunds Witch Trial",
                "context": "In 1662 Hale presided over the conviction and execution of two women for witchcraft, a case later cited at Salem"
            },
            {
                "sourceSlug": "matthew-hale",
                "sourceName": "Matthew Hale",
                "verb": "SURVIVED",
                "targetSlug": "english-civil-war",
                "targetName": "English Civil War",
                "context": "Hale navigated the Civil War by defending clients from all political factions and serving under both Cromwellian and Restoration governments"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Matthew Hale's posthumous criminal law treatises became the authoritative texts of English criminal procedure for over a century, while his judicial decisions left both a lasting jurisprudential legacy and troubling precedents on witchcraft and marital immunity that required centuries to overturn.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "zenas-the-lawyer": {
        "summary": (
            "Zenas the Lawyer (1st century CE) is a figure briefly mentioned in the New Testament "
            "in Paul the Apostle's Epistle to Titus (3:13), making him one of the earliest "
            "named Christians identified by his legal profession. Paul instructs Titus: 'Bring "
            "Zenas the lawyer and Apollos on their journey diligently, that nothing be wanting "
            "unto them' (KJV). This single passage, combined with later ecclesiastical traditions, "
            "has generated considerable scholarly and theological discussion about the nature "
            "of early Christian communities and their relationship to the legal professions.\n\n"
            "The name Zenas is a contracted form of Zenodoros ('gift of Zeus'), indicating "
            "probable Greek or Hellenized Jewish origin. Scholars debate whether his designation "
            "as 'lawyer' (Greek: nomikos) refers to expertise in Jewish Torah law or in Roman "
            "civil law — both professions were active in the 1st-century eastern Mediterranean. "
            "Some early Church traditions count Zenas among the Seventy (or Seventy-Two) "
            "disciples sent out by Jesus according to Luke 10:1, though this identification "
            "rests on tradition rather than scripture. The Eastern Orthodox Church and some "
            "Catholic martyrologies name him Bishop of Diospolis (Lydda) in Palestine, a claim "
            "that cannot be independently verified.\n\n"
            "Zenas's significance lies less in his individual biography — which is almost entirely "
            "unknown — than in what his brief mention reveals: that the earliest Christian "
            "communities included legally trained professionals, and that Paul's mission networks "
            "relied on educated intermediaries who could move between Jewish, Greek, and Roman "
            "legal cultures. He is venerated as a saint in both Eastern and Western Christian "
            "traditions, his feast day celebrated on June 23 in the Roman Martyrology."
        ),
        "causes": [
            {
                "title": "The spread of early Christianity across the eastern Mediterranean created networks of educated intermediaries connecting Jewish, Greek, and Roman legal cultures",
                "type": "Movement",
                "year": "c. 50–70 CE, Eastern Mediterranean"
            },
            {
                "title": "Paul's missionary network required trusted legal and ecclesiastical intermediaries capable of organizing travel and logistics",
                "type": "Person",
                "year": "c. 50–65 CE, Eastern Mediterranean"
            },
            {
                "title": "The pluralistic legal environment of the 1st-century Mediterranean — Torah law, Greek customary law, Roman civil law — produced bilingual lawyer-missionaries",
                "type": "Idea",
                "year": "c. 30–70 CE, Eastern Mediterranean"
            }
        ],
        "effects": [
            {
                "title": "Zenas's mention in Titus 3:13 provides one of the earliest New Testament references to a named Christian legal professional",
                "type": "Text",
                "year": "c. 65–100 CE, Eastern Mediterranean"
            },
            {
                "title": "Later tradition named Zenas as one of the Seventy Disciples and Bishop of Diospolis, establishing him in Eastern Christian hagiography",
                "type": "Institution",
                "year": "2nd–4th century CE"
            },
            {
                "title": "Scholarly debate about whether Zenas was a Torah lawyer or Roman advocate has contributed to understanding of law and Christianity in the 1st century",
                "type": "Idea",
                "year": "19th–21st century, academic scholarship"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "zenas-the-lawyer",
                "sourceName": "Zenas the Lawyer",
                "verb": "ASSOCIATED_WITH",
                "targetSlug": "paul-the-apostle",
                "targetName": "Paul the Apostle",
                "context": "Paul mentions Zenas alongside Apollos in Titus 3:13, indicating Zenas was a trusted member of Paul's mission network"
            },
            {
                "sourceSlug": "zenas-the-lawyer",
                "sourceName": "Zenas the Lawyer",
                "verb": "MENTIONED_IN",
                "targetSlug": "epistle-to-titus",
                "targetName": "Epistle to Titus",
                "context": "Zenas is named in Titus 3:13, the only New Testament reference to him"
            },
            {
                "sourceSlug": "zenas-the-lawyer",
                "sourceName": "Zenas the Lawyer",
                "verb": "OCCURS_IN",
                "targetSlug": "early-christian-movement",
                "targetName": "Early Christian Movement",
                "context": "Zenas exemplifies the legal professionals who participated in the first generation of Pauline Christianity"
            },
            {
                "sourceSlug": "zenas-the-lawyer",
                "sourceName": "Zenas the Lawyer",
                "verb": "ASSOCIATED_WITH",
                "targetSlug": "apollos",
                "targetName": "Apollos",
                "context": "Apollos and Zenas are named together in Titus 3:13 as companions Paul asks Titus to assist on their journey"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Zenas the Lawyer's brief New Testament mention provides a rare glimpse of the legally trained professionals in early Christian networks, illustrating how the first century church integrated individuals from Jewish, Greek, and Roman legal cultures into its missionary structure.",
            "significanceCategory": "regional"
        },
        "importanceScore": 5
    }
}


# ---------------------------------------------------------------------------
# Apply enrichments to JSON files
# ---------------------------------------------------------------------------

def enrich_entity(slug: str, data: dict) -> None:
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (file not found): {fname}")
        return

    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    updated_fields = []

    if "summary" in data:
        old_val = entity.get("summary", "")
        entity["summary"] = data["summary"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "summary",
            "oldValue": old_val[:300],
            "newValue": data["summary"][:300]
        })
        updated_fields.append("summary")

    if "importanceScore" in data:
        old_val = entity.get("importanceScore")
        entity["importanceScore"] = data["importanceScore"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "importanceScore",
            "oldValue": str(old_val),
            "newValue": str(data["importanceScore"])
        })
        updated_fields.append("importanceScore")

    if "historicalSignificance" in data:
        old_val = entity.get("historicalSignificance")
        entity["historicalSignificance"] = data["historicalSignificance"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "historicalSignificance",
            "oldValue": json.dumps(old_val)[:200],
            "newValue": json.dumps(data["historicalSignificance"])[:200]
        })
        updated_fields.append("historicalSignificance")

    for field in ("causes", "effects", "relationships"):
        if field in data:
            old_val = det.get(field, [])
            det[field] = data[field]
            edit_log.append({
                "timestamp": NOW,
                "editorId": EDITOR_ID,
                "field": field,
                "oldValue": json.dumps(old_val)[:300],
                "newValue": json.dumps(data[field])[:300]
            })
            updated_fields.append(field)

    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)

    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    slen = len(entity.get("summary", ""))
    nc = len(det.get("causes", []))
    ne = len(det.get("effects", []))
    nr = len(det.get("relationships", []))
    print(f"  ✓ {entity['name']} — sum={slen}c c={nc} e={ne} r={nr} [{', '.join(updated_fields)}]")


if __name__ == "__main__":
    print(f"Enriching {len(ENRICHMENTS)} entities in 230-Class-230 (Batch 2)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone. Files with _unsyncedEdits=True will be picked up by the sync gateway watchdog.")
