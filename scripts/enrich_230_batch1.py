#!/usr/bin/env python3
"""
Batch 1 enrichment for 230-Class-230 entities.
Enriches 10 high-priority medieval English legal/ecclesiastical figures.
Follows git-first bot rules: writes _unsyncedEdits=True + _editLog diffs.
Run from the project root: python3 scripts/enrich_230_batch1.py
"""

import json
import os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

# ---------------------------------------------------------------------------
# Enrichment data — 10 high-priority medieval legal/ecclesiastical figures
# ---------------------------------------------------------------------------
ENRICHMENTS = {
    "thomas-becket": {
        "summary": (
            "Thomas Becket (c. 1118–1170) was an English statesman and cleric who served as "
            "Lord Chancellor of England from 1155 to 1162 and Archbishop of Canterbury from 1162 "
            "until his murder in 1170. Born in London to a prosperous Norman merchant family, he "
            "became King Henry II's most trusted adviser before his elevation to the primacy of "
            "England's Church transformed him into the Crown's most formidable adversary.\n\n"
            "As chancellor, Becket loyally advanced royal interests, levying taxes and personally "
            "leading military campaigns in Normandy. His appointment as archbishop in 1162 brought "
            "a dramatic personal conversion: he resigned the chancellorship, adopted an austere "
            "penitential lifestyle, and emerged as a fierce defender of ecclesiastical immunities "
            "against Henry's Constitutions of Clarendon (1164), which sought to curtail clerical "
            "legal privileges. Six years of exile in France followed before an uneasy reconciliation "
            "allowed his return in 1170.\n\n"
            "On 29 December 1170, four knights acting on Henry's exasperated outburst — 'Will no "
            "one rid me of this turbulent priest?' — murdered Becket before the altar of his own "
            "cathedral. The shock reverberated across Christendom. Henry performed public penance "
            "at Canterbury in 1174, and Pope Alexander III canonized Becket within three years "
            "of his death, in 1173. Canterbury Cathedral became one of medieval Europe's foremost "
            "pilgrimage destinations, immortalized by Geoffrey Chaucer in his Canterbury Tales.\n\n"
            "Becket's martyrdom permanently reshaped English church-state relations, establishing "
            "precedents for clerical immunity that endured until Henry VIII dismantled them during "
            "the Reformation. His feast day (29 December) remains on the Roman Catholic calendar, "
            "and his shrine attracted millions of pilgrims over three centuries."
        ),
        "causes": [
            {
                "title": "Henry II's Constitutions of Clarendon (1164) sought to subordinate ecclesiastical courts to royal jurisdiction",
                "type": "EventWindow",
                "year": "1164, Clarendon Palace, England"
            },
            {
                "title": "The Norman Conquest had created unresolved tensions between royal authority and Church independence in England",
                "type": "Idea",
                "year": "1066, England"
            },
            {
                "title": "Becket's personal transformation upon becoming Archbishop — from royal servant to champion of ecclesiastical liberty",
                "type": "Person",
                "year": "1162, Canterbury"
            }
        ],
        "effects": [
            {
                "title": "Henry II's public penance at Canterbury in 1174 acknowledged limits on royal power over the Church",
                "type": "EventWindow",
                "year": "1174, Canterbury"
            },
            {
                "title": "Canonization in 1173 made Canterbury Cathedral one of Europe's premier pilgrimage destinations for three centuries",
                "type": "Place",
                "year": "1173, Rome"
            },
            {
                "title": "Becket's case established legal precedent for benefit of clergy — clerical immunity from secular courts — surviving until the Reformation",
                "type": "Idea",
                "year": "1170–1534, England"
            },
            {
                "title": "Chaucer's Canterbury Tales (c. 1390) made Becket's shrine the setting for England's foundational vernacular literary work",
                "type": "Text",
                "year": "c. 1390, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "OPPOSED",
                "targetSlug": "henry-ii-of-england",
                "targetName": "Henry II of England",
                "context": "Becket resisted Henry II's Constitutions of Clarendon, sparking a conflict over royal vs. ecclesiastical jurisdiction"
            },
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "SERVED_UNDER",
                "targetSlug": "theobald-of-bec",
                "targetName": "Theobald of Bec",
                "context": "Becket served as clerk and archdeacon under Archbishop Theobald before his royal career"
            },
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "CHAMPIONED",
                "targetSlug": "benefit-of-clergy",
                "targetName": "Benefit of Clergy",
                "context": "Becket's central legal argument was that clergy must be tried in ecclesiastical rather than royal courts"
            },
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "INSPIRED",
                "targetSlug": "canterbury-tales",
                "targetName": "The Canterbury Tales",
                "context": "Chaucer's pilgrims travel to venerate Becket's shrine at Canterbury Cathedral, c. 1390"
            },
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "OCCURS_IN",
                "targetSlug": "canterbury-cathedral",
                "targetName": "Canterbury Cathedral",
                "context": "Becket was murdered in Canterbury Cathedral and his shrine made it Europe's foremost pilgrimage site"
            },
            {
                "sourceSlug": "thomas-becket",
                "sourceName": "Thomas Becket",
                "verb": "CANONIZED_BY",
                "targetSlug": "pope-alexander-iii",
                "targetName": "Pope Alexander III",
                "context": "Becket was canonized by Alexander III in 1173, cementing his martyr status"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Thomas Becket's martyrdom and canonization redrew the boundaries between Church and State across medieval Europe, forcing one of England's most powerful kings to public penance and establishing clerical legal immunities that shaped Western jurisprudence for over three centuries.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "étienne-boileau": {
        "summary": (
            "Étienne Boileau (c. 1200–1270) was a French administrator and jurist who served as the "
            "first Prévôt of Paris under King Louis IX from 1261 until his death in 1270. As the "
            "royal representative responsible for justice, policing, and commerce in medieval Paris, "
            "Boileau transformed the office of prévôt into an effective instrument of Capetian "
            "governance and became one of the key architects of urban order in 13th-century France.\n\n"
            "Boileau's most enduring achievement was the compilation of the Livre des Métiers "
            "(Book of Trades), completed around 1268 — an extraordinary codification of the "
            "regulations governing 101 Parisian guilds and craft associations, from bakers and "
            "butchers to goldsmiths and silkweavers. The Livre des Métiers stands as one of "
            "the earliest and most comprehensive documents of medieval urban economic life, "
            "providing invaluable insight into the organization of labor, quality standards, "
            "pricing regulations, and social hierarchies of a major medieval city. Boileau also "
            "dramatically reduced crime and corruption in Paris, executing or expelling numerous "
            "offenders and restoring public confidence in royal administration.\n\n"
            "The Livre des Métiers became a foundational document for French commercial law and "
            "guild regulation, its framework influencing royal ordinances for centuries. Boileau's "
            "tenure demonstrated that strong municipal governance under royal authority could "
            "bring prosperity and order to Europe's largest cities, prefiguring the centralized "
            "administrative state."
        ),
        "causes": [
            {
                "title": "Louis IX's drive to reform royal justice and reduce corruption in Capetian administration",
                "type": "Institution",
                "year": "1248–1270, France"
            },
            {
                "title": "Rapid growth of Paris as a commercial and ecclesiastical capital requiring regulatory frameworks",
                "type": "EventWindow",
                "year": "c. 1200–1270, Paris"
            },
            {
                "title": "Unregulated guild competition and criminality threatening civic order in 13th-century Paris",
                "type": "Idea",
                "year": "1261, Paris"
            }
        ],
        "effects": [
            {
                "title": "The Livre des Métiers (c. 1268) became the foundational codification of medieval Parisian guild regulations",
                "type": "Text",
                "year": "c. 1268, Paris"
            },
            {
                "title": "Boileau's prévôté model became the template for royal urban governance in Capetian and later French administrations",
                "type": "Institution",
                "year": "1270–1400, France"
            },
            {
                "title": "Reduced crime and corruption in Paris established the prévôt as a viable instrument of royal justice",
                "type": "Idea",
                "year": "1261–1270, Paris"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "étienne-boileau",
                "sourceName": "Étienne Boileau",
                "verb": "SERVED_UNDER",
                "targetSlug": "louis-ix-of-france",
                "targetName": "Louis IX of France",
                "context": "Boileau served as Prévôt of Paris under Louis IX's direct appointment from 1261"
            },
            {
                "sourceSlug": "étienne-boileau",
                "sourceName": "Étienne Boileau",
                "verb": "COMPILED",
                "targetSlug": "livre-des-metiers",
                "targetName": "Livre des Métiers",
                "context": "Boileau compiled the Livre des Métiers c. 1268, codifying regulations for 101 Parisian guilds"
            },
            {
                "sourceSlug": "étienne-boileau",
                "sourceName": "Étienne Boileau",
                "verb": "ADMINISTERED",
                "targetSlug": "paris",
                "targetName": "Paris",
                "context": "As Prévôt, Boileau exercised justice, policing, and commercial regulation over the city of Paris"
            },
            {
                "sourceSlug": "étienne-boileau",
                "sourceName": "Étienne Boileau",
                "verb": "REGULATED",
                "targetSlug": "medieval-guild-system",
                "targetName": "Medieval Guild System",
                "context": "The Livre des Métiers codified guild statutes, setting standards for 101 trades"
            },
            {
                "sourceSlug": "étienne-boileau",
                "sourceName": "Étienne Boileau",
                "verb": "INFLUENCED",
                "targetSlug": "french-commercial-law",
                "targetName": "French Commercial Law",
                "context": "The guild regulations compiled by Boileau formed the basis of French commercial ordinances for centuries"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Boileau's compilation of the Livre des Métiers created the first comprehensive codification of medieval urban trade regulation in France, providing a model for guild governance and royal urban administration that shaped French commercial law for centuries.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "walter-de-gray": {
        "summary": (
            "Walter de Gray (c. 1180–1255) was an English prelate and royal administrator who served "
            "as Lord Chancellor of England from 1205 to 1214 and as Archbishop of York from 1215 "
            "until his death — the longest continuous tenure as Archbishop of York in the medieval "
            "period, spanning four decades. A devoted servant of the Plantagenet crown, he navigated "
            "some of the most turbulent decades of English history, from Magna Carta through the "
            "minority of Henry III.\n\n"
            "Gray rose through royal service under King John, obtaining the chancellorship and "
            "becoming one of the most powerful administrative figures in England. His uncle, Bishop "
            "John de Gray, had served John loyally, and Walter continued that family tradition. "
            "During the crisis of 1215 that produced Magna Carta, Walter remained a staunch "
            "loyalist. His appointment to York that same year placed him at the head of the northern "
            "English Church for the next forty years, during which he supervised major construction "
            "at York Minster and supported the young Henry III's administration.\n\n"
            "Gray left a lasting architectural legacy at York Minster, funding the south transept "
            "and serving as one of the great ecclesiastical builders of the 13th century. His "
            "exceptionally long archiepiscopate — covering the reigns of John and Henry III — "
            "made him one of the most consequential figures in the governance of northern England "
            "during a formative era of English constitutional development."
        ),
        "causes": [
            {
                "title": "King John's need for capable administrators loyal to the Crown in the face of baronial rebellion",
                "type": "EventWindow",
                "year": "1205–1215, England"
            },
            {
                "title": "Interdict crisis and papal conflict with King John created instability in English Church appointments",
                "type": "Institution",
                "year": "1208–1213, England"
            },
            {
                "title": "Walter de Gray's family connections to John's administration through his uncle Bishop John de Gray",
                "type": "Person",
                "year": "c. 1205, England"
            }
        ],
        "effects": [
            {
                "title": "Forty-year archiepiscopate provided unusual continuity of governance in the northern English Church during constitutional upheaval",
                "type": "Institution",
                "year": "1215–1255, York"
            },
            {
                "title": "Major construction at York Minster's south transept left an enduring architectural legacy",
                "type": "Place",
                "year": "c. 1220–1255, York"
            },
            {
                "title": "Gray's administrative model shaped the relationship between royal chancellors and ecclesiastical office in 13th-century England",
                "type": "Idea",
                "year": "1205–1255, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "walter-de-gray",
                "sourceName": "Walter de Gray",
                "verb": "SERVED_UNDER",
                "targetSlug": "king-john-of-england",
                "targetName": "King John of England",
                "context": "Gray served as John's Lord Chancellor from 1205 to 1214, one of the most powerful offices in the realm"
            },
            {
                "sourceSlug": "walter-de-gray",
                "sourceName": "Walter de Gray",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-york",
                "targetName": "Archdiocese of York",
                "context": "Gray was Archbishop of York for 40 years (1215–1255), the longest medieval tenure in that see"
            },
            {
                "sourceSlug": "walter-de-gray",
                "sourceName": "Walter de Gray",
                "verb": "OCCURS_DURING",
                "targetSlug": "magna-carta",
                "targetName": "Magna Carta",
                "context": "Gray was a royalist during the 1215 crisis and witnessed Magna Carta's negotiation as a Crown loyalist"
            },
            {
                "sourceSlug": "walter-de-gray",
                "sourceName": "Walter de Gray",
                "verb": "BUILT",
                "targetSlug": "york-minster",
                "targetName": "York Minster",
                "context": "Gray funded and oversaw major construction of York Minster's south transept"
            },
            {
                "sourceSlug": "walter-de-gray",
                "sourceName": "Walter de Gray",
                "verb": "SUPPORTED",
                "targetSlug": "henry-iii-of-england",
                "targetName": "Henry III of England",
                "context": "Gray continued to support the Plantagenet crown through Henry III's minority and reign"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Walter de Gray's record-breaking 40-year archiepiscopate at York and his royal chancellorship gave him an outsized role in English church-state relations across the pivotal decades of Magna Carta and the early Plantagenet constitutional order.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "walter-de-coutances": {
        "summary": (
            "Walter de Coutances (c. 1140–1207) was an Anglo-Norman bishop and royal administrator "
            "who served as Archbishop of Rouen from 1184 to his death, and who acted as Chief "
            "Justiciar of England from 1191 to 1193 — effectively governing the realm in Richard I's "
            "absence on crusade. Born in Cornwall of Norman descent, he rose through the royal "
            "administration of Henry II, serving as vice-chancellor and accumulating a series of "
            "ecclesiastical offices in both England and Normandy.\n\n"
            "Walter's most critical hour came when Richard I departed on the Third Crusade in 1190, "
            "leaving England in the hands of William Longchamp. When Longchamp's arrogant government "
            "provoked a revolt by the English barons and Richard's brother John, Richard empowered "
            "Walter to return to England and assume the justiciarship in 1191. Walter successfully "
            "expelled Longchamp, stabilized the kingdom, and managed the fraught politics of John's "
            "ambitions until Richard's return. He also played a role in organizing the enormous "
            "ransom of 150,000 marks required to free Richard from captivity in 1193.\n\n"
            "As Archbishop of Rouen, Walter presided over one of the wealthiest and most strategically "
            "vital sees in the Angevin empire, bridging England and Normandy during a period of "
            "intense Capetian pressure. His political acumen and loyalty to the Plantagenet cause "
            "through three monarchs — Henry II, Richard I, and early in John's reign — made him "
            "an indispensable figure in the governance of the cross-Channel Anglo-Norman realm."
        ),
        "causes": [
            {
                "title": "Richard I's departure on the Third Crusade left England requiring a trusted royal proxy to maintain order",
                "type": "EventWindow",
                "year": "1190–1191, England"
            },
            {
                "title": "William Longchamp's misgovernment as justiciar provoked baronial revolt and necessitated Walter's appointment",
                "type": "Person",
                "year": "1191, England"
            },
            {
                "title": "The Angevin empire's cross-Channel structure required experienced administrators capable of governing in both England and Normandy",
                "type": "Institution",
                "year": "1184–1207, Normandy and England"
            }
        ],
        "effects": [
            {
                "title": "Stabilized English royal government during the crisis of 1191–1193 by expelling Longchamp and checking John's ambitions",
                "type": "EventWindow",
                "year": "1191–1193, England"
            },
            {
                "title": "Helped organize Richard I's enormous ransom (150,000 marks) from Imperial captivity in 1193",
                "type": "EventWindow",
                "year": "1193–1194, England"
            },
            {
                "title": "His archiepiscopate of Rouen (1184–1207) strengthened Angevin ecclesiastical control over Normandy",
                "type": "Institution",
                "year": "1184–1204, Rouen"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "walter-de-coutances",
                "sourceName": "Walter de Coutances",
                "verb": "SERVED_UNDER",
                "targetSlug": "richard-i-of-england",
                "targetName": "Richard I of England",
                "context": "Walter was appointed Chief Justiciar by Richard I to govern England during the Third Crusade, 1191–1193"
            },
            {
                "sourceSlug": "walter-de-coutances",
                "sourceName": "Walter de Coutances",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-rouen",
                "targetName": "Archdiocese of Rouen",
                "context": "Walter served as Archbishop of Rouen from 1184 to 1207, heading the most important Norman see"
            },
            {
                "sourceSlug": "walter-de-coutances",
                "sourceName": "Walter de Coutances",
                "verb": "EXPELLED",
                "targetSlug": "william-longchamp",
                "targetName": "William Longchamp",
                "context": "Walter replaced and expelled Longchamp as justiciar in 1191 following a baronial revolt"
            },
            {
                "sourceSlug": "walter-de-coutances",
                "sourceName": "Walter de Coutances",
                "verb": "NEGOTIATED",
                "targetSlug": "ransom-of-richard-i",
                "targetName": "Ransom of Richard I",
                "context": "Walter helped organize the raising of 150,000 marks to free Richard I from Imperial captivity in 1193"
            },
            {
                "sourceSlug": "walter-de-coutances",
                "sourceName": "Walter de Coutances",
                "verb": "OPPOSED",
                "targetSlug": "john-of-england",
                "targetName": "John of England",
                "context": "Walter checked Prince John's attempts to seize power during Richard I's absence on crusade"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Walter de Coutances's regency as Chief Justiciar during Richard I's crusade and captivity preserved the stability of the English realm at its most vulnerable moment, demonstrating how ecclesiastical statesmen could serve as indispensable pillars of Plantagenet governance across the cross-Channel Anglo-Norman empire.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "william-courtenay": {
        "summary": (
            "William Courtenay (1342–1396) was an English bishop and Archbishop of Canterbury who "
            "played a decisive role in the suppression of Lollardy — the religious reform movement "
            "inspired by Oxford theologian John Wycliffe. Born into one of England's most powerful "
            "noble families, Courtenay served successively as Bishop of Hereford (1370–1375), "
            "Bishop of London (1375–1381), and Archbishop of Canterbury (1381–1396), wielding "
            "enormous ecclesiastical and political influence during the tumultuous reign of "
            "Richard II.\n\n"
            "Courtenay's confrontation with Wycliffe began at St Paul's in 1377, where he summoned "
            "the reformer before a convocation — only for the proceedings to be disrupted by John "
            "of Gaunt. But Courtenay's decisive moment came after the Peasants' Revolt of 1381, "
            "when he succeeded to Canterbury and immediately convened what became known as the "
            "Earthquake Synod (May 1382), named for a tremor that shook London during proceedings. "
            "The synod condemned 24 Wycliffite theses as heretical and dispatched royal authority "
            "against itinerant Lollard preachers, establishing for the first time a systematic "
            "mechanism for prosecuting heresy in England.\n\n"
            "Courtenay's actions effectively forced Wycliffe's disciples underground and checked "
            "the spread of Lollardy for a generation. Though Lollardy survived and eventually "
            "contributed to the English Reformation, Courtenay's vigorous defense of orthodox "
            "Catholicism shaped the contours of English religious history for over a century."
        ),
        "causes": [
            {
                "title": "John Wycliffe's theological challenge to transubstantiation and papal authority attracted growing followers in Oxford and the clergy",
                "type": "Person",
                "year": "1370s–1380s, Oxford"
            },
            {
                "title": "The Peasants' Revolt of 1381 alarmed the Church establishment, linking social disorder with heterodox preaching",
                "type": "EventWindow",
                "year": "1381, England"
            },
            {
                "title": "John of Gaunt's political protection of Wycliffe had shielded him from earlier prosecution, which Courtenay moved to end",
                "type": "Person",
                "year": "1377–1381, London"
            }
        ],
        "effects": [
            {
                "title": "Earthquake Synod (1382) condemned 24 Wycliffite theses and established systematic heresy prosecution in England",
                "type": "EventWindow",
                "year": "1382, London"
            },
            {
                "title": "Suppression of Lollardy at Oxford forced Wycliffe's followers underground and out of academic institutions",
                "type": "Movement",
                "year": "1382–1400, England"
            },
            {
                "title": "Courtenay's framework for prosecuting heresy paved the way for De Heretico Comburendo (1401), which mandated burning of heretics",
                "type": "Idea",
                "year": "1401, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "william-courtenay",
                "sourceName": "William Courtenay",
                "verb": "OPPOSED",
                "targetSlug": "john-wycliffe",
                "targetName": "John Wycliffe",
                "context": "Courtenay prosecuted Wycliffe's heterodox teachings from 1377, culminating in the Earthquake Synod of 1382"
            },
            {
                "sourceSlug": "william-courtenay",
                "sourceName": "William Courtenay",
                "verb": "CONVENED",
                "targetSlug": "earthquake-synod",
                "targetName": "Earthquake Synod",
                "context": "Courtenay convened the 1382 synod that condemned 24 Wycliffite theses and launched systematic heresy prosecution"
            },
            {
                "sourceSlug": "william-courtenay",
                "sourceName": "William Courtenay",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-canterbury",
                "targetName": "Archdiocese of Canterbury",
                "context": "Courtenay was Archbishop of Canterbury 1381–1396, leading the English Church during the Lollard crisis"
            },
            {
                "sourceSlug": "william-courtenay",
                "sourceName": "William Courtenay",
                "verb": "SUPPRESSED",
                "targetSlug": "lollardy",
                "targetName": "Lollardy",
                "context": "Courtenay's synodal decrees drove Lollard preachers from Oxford and forced the movement underground"
            },
            {
                "sourceSlug": "william-courtenay",
                "sourceName": "William Courtenay",
                "verb": "SERVED_UNDER",
                "targetSlug": "richard-ii-of-england",
                "targetName": "Richard II of England",
                "context": "Courtenay served as Archbishop of Canterbury throughout most of Richard II's reign"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Courtenay's Earthquake Synod created England's first systematic mechanism for prosecuting religious heresy, decisively checking Wycliffite Lollardy and shaping the contours of English religious conformity until the Reformation a century and a half later.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "thomas-arundel": {
        "summary": (
            "Thomas Arundel (1353–1414) was one of medieval England's most powerful ecclesiastical "
            "statesmen, serving as Archbishop of York, Lord Chancellor, and twice as Archbishop of "
            "Canterbury. A member of the powerful FitzAlan noble family, he was one of the chief "
            "architects of the Lancastrian usurpation of 1399 and became the leading ecclesiastical "
            "persecutor of Lollardy in early 15th-century England.\n\n"
            "Arundel served Richard II as Archbishop of York (1388–1396) and Lord Chancellor "
            "(1386–1389, 1391–1396) before falling from royal favor and being exiled in 1397. "
            "During his exile he allied with Henry Bolingbroke, helping to plan the invasion that "
            "deposed Richard II and brought Henry IV to the throne in 1399. Restored as Archbishop "
            "of Canterbury, Arundel became the spiritual arm of the new Lancastrian regime's drive "
            "for orthodoxy. His most consequential act was the Constitutions of Oxford (1409), "
            "which imposed strict censorship on unauthorized biblical translation and preaching, "
            "directly targeting Wycliffite Lollards. The statute De Heretico Comburendo (1401), "
            "enacted under his influence, authorized the burning of unrepentant heretics.\n\n"
            "Three Lollards were burned at the stake under Arundel's tenure, and his Constitutions "
            "remained in force until the English Reformation. Scholars debate whether Arundel's "
            "harsh suppression strengthened or ultimately radicalized the underground Lollard "
            "movement that contributed to the Protestant Reformation in England."
        ),
        "causes": [
            {
                "title": "The spread of Lollard preaching and unauthorized Bible translation threatened ecclesiastical authority under Henry IV",
                "type": "Movement",
                "year": "1399–1414, England"
            },
            {
                "title": "Arundel's exile and alliance with Bolingbroke during Richard II's reign shaped his role as architect of Lancastrian orthodoxy",
                "type": "EventWindow",
                "year": "1397–1399, France and England"
            },
            {
                "title": "The precedent set by Courtenay's 1382 Earthquake Synod for prosecuting heresy gave Arundel a framework to build upon",
                "type": "Idea",
                "year": "1382, London"
            }
        ],
        "effects": [
            {
                "title": "Constitutions of Oxford (1409) imposed stringent censorship of biblical translation and unauthorized preaching, remaining in force until the Reformation",
                "type": "Idea",
                "year": "1409, Oxford"
            },
            {
                "title": "De Heretico Comburendo (1401) authorized burning of heretics, the first English statute to mandate death for religious dissent",
                "type": "EventWindow",
                "year": "1401, England"
            },
            {
                "title": "Arundel's suppression forced Lollardy underground and into the networks that would later connect with early English Protestantism",
                "type": "Movement",
                "year": "1409–1530s, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thomas-arundel",
                "sourceName": "Thomas Arundel",
                "verb": "ALLIED_WITH",
                "targetSlug": "henry-iv-of-england",
                "targetName": "Henry IV of England",
                "context": "Arundel helped engineer Henry Bolingbroke's usurpation of Richard II in 1399, cementing the Lancastrian alliance"
            },
            {
                "sourceSlug": "thomas-arundel",
                "sourceName": "Thomas Arundel",
                "verb": "ISSUED",
                "targetSlug": "constitutions-of-oxford",
                "targetName": "Constitutions of Oxford",
                "context": "Arundel issued the 1409 Constitutions of Oxford, censoring biblical translation and unauthorized preaching"
            },
            {
                "sourceSlug": "thomas-arundel",
                "sourceName": "Thomas Arundel",
                "verb": "SUPPRESSED",
                "targetSlug": "lollardy",
                "targetName": "Lollardy",
                "context": "Arundel prosecuted Lollard heretics under De Heretico Comburendo, burning three at the stake"
            },
            {
                "sourceSlug": "thomas-arundel",
                "sourceName": "Thomas Arundel",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-canterbury",
                "targetName": "Archdiocese of Canterbury",
                "context": "Arundel served as Archbishop of Canterbury 1396–1397 and 1399–1414"
            },
            {
                "sourceSlug": "thomas-arundel",
                "sourceName": "Thomas Arundel",
                "verb": "OPPOSED",
                "targetSlug": "richard-ii-of-england",
                "targetName": "Richard II of England",
                "context": "Arundel was exiled by Richard II in 1397 before allying with Bolingbroke to engineer Richard's deposition"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Arundel's Constitutions of Oxford (1409) and his enforcement of De Heretico Comburendo created the most stringent censorship of religious dissent in English history before the Reformation, shaping the boundaries of permissible religious thought for over a century.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "thomas-bourchier": {
        "summary": (
            "Thomas Bourchier (c. 1404–1486) was an English cardinal and Archbishop of Canterbury "
            "who served as a crucial stabilizing force during the Wars of the Roses, crowning three "
            "successive English monarchs and surviving as primate through one of the most violent "
            "periods in English political history. He was the longest-serving Archbishop of "
            "Canterbury of the 15th century, holding the office for 32 years from 1454 until "
            "his death.\n\n"
            "Born into the powerful Bourchier family connected to both Yorkist and Lancastrian "
            "houses, Thomas served as Bishop of Worcester (1434–1443) and Bishop of Ely (1443–1454) "
            "before his elevation to Canterbury. He served briefly as Lord Chancellor of England "
            "(1455–1456) and was created Cardinal by Pope Paul II in 1467. His consummate political "
            "skill lay in maintaining ecclesiastical authority and royal favor through the dizzying "
            "changes of the Wars of the Roses. He crowned Edward IV in 1461, Richard III in 1483 "
            "(a ceremony he reportedly performed reluctantly), and Henry VII in 1485 — an "
            "extraordinary record of adaptability at the intersection of Church and State.\n\n"
            "Bourchier played a key role in the famous episode of 1483 when he persuaded Queen "
            "Elizabeth Woodville to release the young Duke of York from sanctuary at Westminster "
            "Abbey, the boy who then disappeared into the Tower of London as one of the Princes "
            "in the Tower. His long archiepiscopate left Canterbury's institutional structures "
            "strengthened and provided continuity of ecclesiastical governance through the "
            "transition from Plantagenet to Tudor rule."
        ),
        "causes": [
            {
                "title": "Wars of the Roses created intense pressure on the Church to maintain authority and legitimacy across shifting political allegiances",
                "type": "EventWindow",
                "year": "1455–1485, England"
            },
            {
                "title": "Bourchier's noble birth connected him to both Yorkist and Lancastrian factions, enabling unusual political durability",
                "type": "Person",
                "year": "c. 1404, Essex"
            },
            {
                "title": "The need for ecclesiastical legitimation of English monarchy made the Archbishop of Canterbury indispensable to each successive ruler",
                "type": "Institution",
                "year": "1461–1485, England"
            }
        ],
        "effects": [
            {
                "title": "Crowned three successive monarchs (Edward IV, Richard III, Henry VII), providing ecclesiastical continuity through dynastic upheaval",
                "type": "EventWindow",
                "year": "1461–1485, Westminster Abbey"
            },
            {
                "title": "Persuaded Elizabeth Woodville to release the Duke of York from sanctuary in 1483, contributing to the fate of the Princes in the Tower",
                "type": "EventWindow",
                "year": "1483, Westminster"
            },
            {
                "title": "His 32-year archiepiscopate provided institutional continuity for the English Church from the late Lancastrian period through the early Tudor era",
                "type": "Institution",
                "year": "1454–1486, Canterbury"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thomas-bourchier",
                "sourceName": "Thomas Bourchier",
                "verb": "CROWNED",
                "targetSlug": "edward-iv-of-england",
                "targetName": "Edward IV of England",
                "context": "Bourchier crowned Edward IV at Westminster Abbey in 1461"
            },
            {
                "sourceSlug": "thomas-bourchier",
                "sourceName": "Thomas Bourchier",
                "verb": "CROWNED",
                "targetSlug": "henry-vii-of-england",
                "targetName": "Henry VII of England",
                "context": "Bourchier crowned Henry VII in 1485, cementing the Tudor succession"
            },
            {
                "sourceSlug": "thomas-bourchier",
                "sourceName": "Thomas Bourchier",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-canterbury",
                "targetName": "Archdiocese of Canterbury",
                "context": "Bourchier served as Archbishop of Canterbury for 32 years, 1454–1486"
            },
            {
                "sourceSlug": "thomas-bourchier",
                "sourceName": "Thomas Bourchier",
                "verb": "NEGOTIATED_WITH",
                "targetSlug": "elizabeth-woodville",
                "targetName": "Elizabeth Woodville",
                "context": "In 1483 Bourchier persuaded Elizabeth Woodville to release the Duke of York from sanctuary at Westminster Abbey"
            },
            {
                "sourceSlug": "thomas-bourchier",
                "sourceName": "Thomas Bourchier",
                "verb": "OCCURS_DURING",
                "targetSlug": "wars-of-the-roses",
                "targetName": "Wars of the Roses",
                "context": "Bourchier's entire archiepiscopate unfolded during the Wars of the Roses, through which he maintained Church authority"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Bourchier's 32-year archiepiscopate and his coronation of three successive monarchs made him the pivotal ecclesiastical figure of the Wars of the Roses, providing the institutional continuity that helped the English Church survive the dynastic convulsions of the 15th century.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "walter-reynolds": {
        "summary": (
            "Walter Reynolds (c. 1270–1327) was an English bishop and royal administrator who served "
            "as Archbishop of Canterbury from 1313 to 1327, as well as Lord High Treasurer "
            "(1307–1310) and Lord Chancellor (1310–1314). Long regarded by contemporaries as a "
            "creature of royal patronage rather than a man of learning or spiritual distinction, "
            "Reynolds was nonetheless one of the key ecclesiastical figures in the troubled reign "
            "of Edward II.\n\n"
            "Reynolds rose through royal service as keeper of the wardrobe and financial official "
            "to the future Edward II, gaining church offices as reward for administrative loyalty. "
            "His elevation to Canterbury in 1313 was widely seen as an act of royal patronage, "
            "and contemporary chroniclers were dismissive of his intellectual capacities. Yet "
            "Reynolds proved a politically adroit survivor: he managed to navigate the bitter "
            "conflicts between Edward II and his barons, including the Ordinances of 1311 and the "
            "execution of Piers Gaveston, without forfeiting royal or baronial goodwill for long. "
            "He also acted as a mediator during the crisis with Thomas of Lancaster in 1321–1322.\n\n"
            "Reynolds's most consequential moment came in 1327, when he participated in the "
            "deposition of Edward II — one of the few times an English monarch was removed from "
            "the throne before death. He pronounced the sermon at the parliament that declared "
            "Edward's deposition, using the biblical text 'Vox populi, vox Dei' ('The voice of "
            "the people is the voice of God'). He died shortly after Edward II's deposition and "
            "murder, having witnessed the collapse of a royal dynasty he had served all his life."
        ),
        "causes": [
            {
                "title": "Edward II's system of royal patronage elevated loyal administrators to major ecclesiastical offices regardless of spiritual qualifications",
                "type": "Institution",
                "year": "1307–1313, England"
            },
            {
                "title": "The political crisis of Edward II's reign — Gaveston, the Ordinances, and baronial opposition — demanded an archbishop capable of political navigation",
                "type": "EventWindow",
                "year": "1311–1327, England"
            },
            {
                "title": "Reynolds's decades of loyal financial service to the Crown as keeper of the wardrobe secured his rise",
                "type": "Person",
                "year": "c. 1295–1313, England"
            }
        ],
        "effects": [
            {
                "title": "Reynolds's 1327 deposition sermon legitimized Edward II's removal using canonical and popular authority, setting a precedent for parliamentary deposition",
                "type": "EventWindow",
                "year": "1327, Westminster"
            },
            {
                "title": "His archiepiscopate demonstrated how royal control over Canterbury appointments could subordinate ecclesiastical leadership to political calculation",
                "type": "Idea",
                "year": "1313–1327, England"
            },
            {
                "title": "Reynolds's survival through Edward II's entire reign illustrated the political utility of ecclesiastical office in medieval governance",
                "type": "Institution",
                "year": "1313–1327, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "walter-reynolds",
                "sourceName": "Walter Reynolds",
                "verb": "SERVED_UNDER",
                "targetSlug": "edward-ii-of-england",
                "targetName": "Edward II of England",
                "context": "Reynolds was Edward II's chief financial servant before elevation to Canterbury, and remained loyal to Edward throughout his reign"
            },
            {
                "sourceSlug": "walter-reynolds",
                "sourceName": "Walter Reynolds",
                "verb": "PARTICIPATED_IN",
                "targetSlug": "deposition-of-edward-ii",
                "targetName": "Deposition of Edward II",
                "context": "Reynolds pronounced the deposition sermon in 1327 using 'Vox populi, vox Dei', legitimizing Edward's removal"
            },
            {
                "sourceSlug": "walter-reynolds",
                "sourceName": "Walter Reynolds",
                "verb": "ADMINISTERED",
                "targetSlug": "archdiocese-of-canterbury",
                "targetName": "Archdiocese of Canterbury",
                "context": "Reynolds served as Archbishop of Canterbury 1313–1327"
            },
            {
                "sourceSlug": "walter-reynolds",
                "sourceName": "Walter Reynolds",
                "verb": "NAVIGATED",
                "targetSlug": "piers-gaveston",
                "targetName": "Piers Gaveston Crisis",
                "context": "Reynolds managed relations between Edward II and barons during the Gaveston crisis without permanently losing either side"
            },
            {
                "sourceSlug": "walter-reynolds",
                "sourceName": "Walter Reynolds",
                "verb": "OCCURS_DURING",
                "targetSlug": "ordinances-of-1311",
                "targetName": "Ordinances of 1311",
                "context": "Reynolds's chancellorship overlapped with the period of baronial Ordinances constraining Edward II's power"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Walter Reynolds's deposition sermon in 1327, invoking 'Vox populi, vox Dei' to legitimize Edward II's removal, established a precedent for parliamentary deposition of English monarchs that would resonate through the constitutional crises of the following centuries.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "thomas-de-cantilupe": {
        "summary": (
            "Thomas de Cantilupe (c. 1218–1282) was an English scholar, royal administrator, and "
            "Bishop of Hereford who was canonized as a saint by Pope John XXII in 1320, becoming "
            "the last Englishman to be canonized before the Reformation. A member of the noble "
            "Cantilupe family, he studied at Oxford, Orléans, and Paris, achieving the degree of "
            "Doctor of Canon Law, and lectured in theology at Oxford before entering royal service.\n\n"
            "Thomas served as Lord Chancellor of England in 1265 under Henry III — briefly, during "
            "the reform government of Simon de Montfort — before returning to academic and "
            "ecclesiastical life. He was elected Bishop of Hereford in 1275 and proved an "
            "energetic defender of episcopal rights against both secular encroachments and the "
            "claims of his metropolitan, Archbishop John Pecham of Canterbury. His dispute with "
            "Pecham grew so fierce that Pecham excommunicated him in 1282. Thomas died in "
            "Montefiascone, Italy, while traveling to appeal to the Pope, still under sentence "
            "of excommunication — a canonical complication that did not prevent his eventual "
            "canonization. The shrine at Hereford Cathedral became a major pilgrimage destination "
            "in 14th-century England.\n\n"
            "Historical sources record that Thomas de Cantilupe held anti-Jewish views that were "
            "cited approvingly in evidence presented at his canonization inquiry — a reminder that "
            "medieval sainthood was evaluated against standards very different from modern ones. "
            "He remains the patron saint of Hereford diocese and his cult attracted Edward I "
            "and other royal pilgrims to his shrine."
        ),
        "causes": [
            {
                "title": "The reform government of Simon de Montfort (1265) provided the political opening for Cantilupe's appointment as Lord Chancellor",
                "type": "EventWindow",
                "year": "1265, England"
            },
            {
                "title": "Cantilupe's distinguished scholarly career at Oxford and Paris established his credibility as a canon lawyer and theologian",
                "type": "Institution",
                "year": "c. 1245–1265, Oxford and Paris"
            },
            {
                "title": "Jurisdictional disputes between bishops and archbishops over rights and revenues were endemic in 13th-century English Church",
                "type": "Idea",
                "year": "1275–1282, England"
            }
        ],
        "effects": [
            {
                "title": "Canonization in 1320 made Hereford Cathedral shrine a major pilgrimage destination, drawing Edward I and royal patronage",
                "type": "Place",
                "year": "1320–1400, Hereford"
            },
            {
                "title": "Thomas became the last Englishman canonized before the Reformation, representing the culmination of medieval English saints' cults",
                "type": "Institution",
                "year": "1320, Avignon"
            },
            {
                "title": "His dispute with Archbishop Pecham highlighted the unresolved tensions between episcopal and metropolitan jurisdiction in the English Church",
                "type": "Idea",
                "year": "1275–1282, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thomas-de-cantilupe",
                "sourceName": "Thomas de Cantilupe",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-iii-of-england",
                "targetName": "Henry III of England",
                "context": "Cantilupe briefly served as Lord Chancellor under Henry III during Simon de Montfort's reform government in 1265"
            },
            {
                "sourceSlug": "thomas-de-cantilupe",
                "sourceName": "Thomas de Cantilupe",
                "verb": "OPPOSED",
                "targetSlug": "john-pecham",
                "targetName": "John Pecham",
                "context": "Cantilupe's bitter dispute with Archbishop Pecham over jurisdictional rights led to his excommunication in 1282"
            },
            {
                "sourceSlug": "thomas-de-cantilupe",
                "sourceName": "Thomas de Cantilupe",
                "verb": "CANONIZED_BY",
                "targetSlug": "pope-john-xxii",
                "targetName": "Pope John XXII",
                "context": "Cantilupe was canonized by Pope John XXII in 1320, the last Englishman so honored before the Reformation"
            },
            {
                "sourceSlug": "thomas-de-cantilupe",
                "sourceName": "Thomas de Cantilupe",
                "verb": "OCCURS_IN",
                "targetSlug": "hereford-cathedral",
                "targetName": "Hereford Cathedral",
                "context": "Cantilupe's shrine at Hereford Cathedral became a major pilgrimage site in 14th-century England"
            },
            {
                "sourceSlug": "thomas-de-cantilupe",
                "sourceName": "Thomas de Cantilupe",
                "verb": "PARTICIPATED_IN",
                "targetSlug": "simon-de-montfort-reform-government",
                "targetName": "Simon de Montfort's Reform Government",
                "context": "Cantilupe was appointed Lord Chancellor by Simon de Montfort during the 1265 reform government"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Thomas de Cantilupe's canonization in 1320 — despite dying under excommunication — made him the last pre-Reformation English saint and established Hereford as a significant pilgrimage center, while his career illustrated the complex intersection of scholarship, royal service, and ecclesiastical politics in 13th-century England.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "william-waynflete": {
        "summary": (
            "William Waynflete (c. 1398–1486), born William Patten, was an English bishop, "
            "educator, and royal administrator who founded Magdalen College, Oxford — one of "
            "the greatest acts of educational patronage in 15th-century England. He served "
            "successively as Headmaster of Winchester College (1429–1441), Provost of Eton "
            "College (1442–1447), Bishop of Winchester (1447–1486), and Lord Chancellor of "
            "England (1456–1460), and is remembered as one of the foremost scholar-administrators "
            "of the Lancastrian period.\n\n"
            "Waynflete rose through educational institutions to become one of the most powerful "
            "churchmen in England. As Headmaster of Winchester he reformed the school's "
            "curriculum; as founding Provost of Eton he shaped Henry VI's pet educational "
            "project from its inception. His elevation to the bishopric of Winchester — the "
            "richest see in England — gave him the resources to realize his greatest ambition: "
            "the foundation of Magdalen College, Oxford, in 1458 (formally chartered 1480), "
            "which he endowed with extensive estates and a grammar school, Magdalen College "
            "School. During the Wars of the Roses his tenure as Lord Chancellor placed him "
            "at the centre of Lancastrian government, and he remained a supporter of Henry VI "
            "through the turbulent reversals of the 1460s and 1470s.\n\n"
            "Magdalen College became one of Oxford's most magnificent institutions, famous for "
            "its tower, deer park, and distinguished alumni including Desiderius Erasmus. "
            "Waynflete's educational legacy — shaping two royal schools and founding a "
            "great Oxford college — made him one of the most consequential patrons of "
            "learning in 15th-century England."
        ),
        "causes": [
            {
                "title": "Henry VI's passion for educational endowment created political opportunity for scholar-administrators like Waynflete to found major institutions",
                "type": "Person",
                "year": "1440s–1460s, England"
            },
            {
                "title": "The wealth of the bishopric of Winchester provided Waynflete with the resources needed to endow Magdalen College",
                "type": "Institution",
                "year": "1447–1486, Winchester"
            },
            {
                "title": "The educational reform movement of the early 15th century, drawing on humanist currents from Italy, inspired new college foundations at Oxford",
                "type": "Movement",
                "year": "c. 1430–1460, England"
            }
        ],
        "effects": [
            {
                "title": "Foundation of Magdalen College, Oxford (1458/1480) created one of England's leading academic institutions and a center of Renaissance scholarship",
                "type": "Institution",
                "year": "1458, Oxford"
            },
            {
                "title": "Magdalen College School and the associated grammar schools extended Waynflete's educational patronage beyond university level",
                "type": "Institution",
                "year": "1480, Oxford"
            },
            {
                "title": "Magdalen College attracted Erasmus and became a conduit for Northern European Renaissance humanism entering England",
                "type": "Movement",
                "year": "c. 1499, Oxford"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "william-waynflete",
                "sourceName": "William Waynflete",
                "verb": "FOUNDED",
                "targetSlug": "magdalen-college-oxford",
                "targetName": "Magdalen College, Oxford",
                "context": "Waynflete founded Magdalen College in 1458 (chartered 1480), endowing it with estates and a grammar school"
            },
            {
                "sourceSlug": "william-waynflete",
                "sourceName": "William Waynflete",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-vi-of-england",
                "targetName": "Henry VI of England",
                "context": "Waynflete was a devoted supporter of Henry VI, serving as his Lord Chancellor and founding Magdalen in his reign"
            },
            {
                "sourceSlug": "william-waynflete",
                "sourceName": "William Waynflete",
                "verb": "LED",
                "targetSlug": "eton-college",
                "targetName": "Eton College",
                "context": "Waynflete was the founding Provost of Eton College 1442–1447, shaping Henry VI's royal educational project from its inception"
            },
            {
                "sourceSlug": "william-waynflete",
                "sourceName": "William Waynflete",
                "verb": "ADMINISTERED",
                "targetSlug": "diocese-of-winchester",
                "targetName": "Diocese of Winchester",
                "context": "Waynflete was Bishop of Winchester 1447–1486, using the wealth of England's richest see to fund his educational patronage"
            },
            {
                "sourceSlug": "william-waynflete",
                "sourceName": "William Waynflete",
                "verb": "INFLUENCED",
                "targetSlug": "desiderius-erasmus",
                "targetName": "Desiderius Erasmus",
                "context": "Erasmus visited Magdalen College c. 1499, and the college's humanist culture was part of what drew him to Oxford"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Waynflete's foundation of Magdalen College, Oxford — one of England's greatest acts of educational patronage — helped establish Oxford as a center of Renaissance humanism and created an institution that shaped English intellectual life for centuries.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
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

    # Track fields we update
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

    # Mark as dirty for sync gateway watchdog
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
    print(f"Enriching {len(ENRICHMENTS)} entities in 230-Class-230 (Batch 1)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone. Files with _unsyncedEdits=True will be picked up by the sync gateway watchdog.")
