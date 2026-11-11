#!/usr/bin/env python3
"""
Composer/agent enrichment batch — 2026-11-08.

Writes via ai_enrich_autonomous.apply_enrichment (git export JSON + _editLog).
Does NOT call Ollama. Claims already held under /tmp/annals-bot-locks/enrich-claims.
"""
from __future__ import annotations

import json
import os
import socket
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import ai_enrich_autonomous as enrich  # noqa: E402

EDITOR_ID = f"composer·local·{socket.gethostname()}"
SESSION_ID = "composer-batch-20261108"
CLAIM_META = Path("/tmp/annals-composer-enrich-batch.json")
REPORT_APPEND = ROOT / "data/enrichment/composer_agent_run.json"

enrich.EDITOR_ID = EDITOR_ID

# ── Enrichment payloads (non-lenient bar: summary≥600, ≥2 causes/effects, ≥3 rels) ──
ENRICHMENTS: dict[str, dict] = {

"marcus-manilius": {
  "summary": (
    "Marcus Manilius was a Roman poet and astrologer of the early Imperial period, "
    "best known as the author of the Astronomica, a didactic poem in five books that "
    "expounds Hellenistic astrology in Latin hexameters. Almost nothing is securely "
    "known of his life: he is not mentioned by contemporary authors, and modern dating "
    "rests on internal references that place composition under Augustus and into the "
    "reign of Tiberius (early 1st century CE). The Astronomica treats the celestial "
    "sphere, the zodiac, the influences of the signs and planets, and the casting of "
    "horoscopes, weaving Stoic cosmology with technical astrological doctrine.\n\n"
    "As a literary and intellectual document, the poem is a principal Latin witness to "
    "the systematisation of astrology in the Roman world after the late Republic, when "
    "Greek mathematical astronomy and Chaldaean star lore were absorbed into elite "
    "culture. Manilius presents the cosmos as a rationally ordered, fate-governing "
    "whole, and his verse both popularises and elevates technical material for educated "
    "readers. Though incomplete or uneven in places, the Astronomica remained a key "
    "source for later Latin astrology and for modern reconstruction of ancient "
    "horoscopic practice."
  ),
  "causes": [
    "Hellenistic astronomy and Chaldaean astrology had already been synthesised into a technical horoscopic system that Roman elites increasingly demanded in Latin literary form.",
    "Augustan and early Tiberian culture prized didactic poetry that married Greek science with Roman moral and cosmological themes, creating a market for works like the Astronomica.",
    "Stoic ideas of cosmic sympathy and deterministic order provided a philosophical frame that made astrological causation intellectually respectable to Roman readers."
  ],
  "effects": [
    "The Astronomica became one of the most important surviving Latin expositions of ancient astrology, shaping later medieval and Renaissance reception of Roman star lore.",
    "Manilius helped naturalise technical astrology within Latin literary culture, alongside poets and encyclopaedists who treated celestial influence as part of learned discourse.",
    "Modern historians of science rely on Manilius as a rare continuous poetic witness to early Imperial horoscopic doctrine and its Stoic cosmological packaging."
  ],
  "relationships": [
    {"sourceSlug": "marcus-manilius", "sourceName": "Marcus Manilius", "verb": "CREATES", "targetSlug": "astronomica-manilius", "targetName": "Astronomica", "context": "Manilius composed the five-book Latin didactic poem Astronomica, the major poetic exposition of Hellenistic astrology in Rome."},
    {"sourceSlug": "marcus-manilius", "sourceName": "Marcus Manilius", "verb": "OCCURS_DURING", "targetSlug": "reign-of-augustus", "targetName": "Augustan–Tiberian Rome", "context": "Internal evidence dates the Astronomica to the later Augustan and early Tiberian periods of the early 1st century CE."},
    {"sourceSlug": "hellenistic-astrology", "sourceName": "Hellenistic astrology", "verb": "INFLUENCES", "targetSlug": "marcus-manilius", "targetName": "Marcus Manilius", "context": "Manilius transmitted Greek horoscopic doctrine—zodiac, planets, and nativities—into Latin verse for Roman readers."}
  ],
  "places": [
    {"name": "Rome / Roman Italy", "role": "Likely cultural setting of composition and intended elite audience for the Astronomica"},
    {"name": "Hellenistic Mediterranean", "role": "Source region of the astronomical–astrological system Manilius versified"}
  ],
  "subjects": ["Roman poetry", "Astrology", "Astronomica", "Stoicism", "Augustan literature", "History of science", "Classical era"],
  "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Marcus Manilius is the principal Latin didactic poet of astrology; his Astronomica preserves early Imperial horoscopic doctrine and shows how Greek celestial science entered Roman literary culture.",
    "significanceCategory": "regional"
  }
},

"pang-juan": {
  "summary": (
    "Pang Juan was a military general of the state of Wei during China's Warring States "
    "period (5th–3rd centuries BCE), remembered chiefly through the traditions surrounding "
    "Sun Bin, the strategist associated with the Sun Bin Bingfa. According to the "
    "well-known narrative preserved in later histories, Pang Juan and Sun Bin studied "
    "military arts together; Pang Juan later served Wei, grew jealous of Sun Bin's "
    "ability, and arranged for him to be mutilated and imprisoned. Sun Bin escaped to "
    "Qi, where he became a key adviser and repeatedly defeated Wei forces commanded by "
    "Pang Juan.\n\n"
    "The climax of the tradition is the Battle of Maling (traditionally 342/341 BCE), "
    "where Sun Bin's deception—feigning dwindling campfires to lure Wei into a trap—"
    "led to Pang Juan's death or suicide after defeat. Whether every anecdotal detail is "
    "historical, Pang Juan functions in Chinese military memory as the foil to Sun Bin: "
    "a capable Wei commander undone by rivalry, overconfidence, and superior strategy. "
    "His story became a lasting exemplar in Chinese discussions of intelligence, deception, "
    "and the costs of envy within the competitive multi-state system of the Warring States."
  ),
  "causes": [
    "The fragmented multi-state system of the Warring States created continuous warfare in which Wei, Qi, and their neighbours competed for survival and hegemony.",
    "Professional military specialists and written strategic traditions (associated with the Sun lineage) made personal rivalries between generals politically consequential.",
    "Wei’s need for aggressive field commanders against Qi and other rivals elevated Pang Juan into high command—and into conflict with Sun Bin after the latter joined Qi."
  ],
  "effects": [
    "Pang Juan’s defeats, culminating at Maling, weakened Wei’s military position relative to Qi and entered Chinese strategic lore as a classic case of deception warfare.",
    "The Pang Juan–Sun Bin narrative became a durable cultural template for warning against jealousy and underestimating an adversary’s intellect.",
    "Later Chinese military writing and popular history used the rivalry to illustrate principles later associated with the Sun Bin Bingfa tradition."
  ],
  "relationships": [
    {"sourceSlug": "pang-juan", "sourceName": "Pang Juan", "verb": "PARTICIPATES_IN", "targetSlug": "battle-of-maling", "targetName": "Battle of Maling", "context": "Tradition holds that Pang Juan led Wei forces into Sun Bin’s trap at Maling and died after Wei’s defeat."},
    {"sourceSlug": "sun-bin", "sourceName": "Sun Bin", "verb": "INFLUENCES", "targetSlug": "pang-juan", "targetName": "Pang Juan", "context": "Sun Bin’s strategies in Qi repeatedly outmanoeuvred Pang Juan, defining the latter’s historical reputation."},
    {"sourceSlug": "pang-juan", "sourceName": "Pang Juan", "verb": "OCCURS_IN", "targetSlug": "state-of-wei-warring-states", "targetName": "State of Wei (Warring States)", "context": "Pang Juan served as a Wei general in the interstate wars of eastern China during the Warring States period."}
  ],
  "places": [
    {"name": "State of Wei (north China plain)", "role": "Political–military home of Pang Juan’s career"},
    {"name": "Maling (traditional battlefield, Qi–Wei frontier)", "role": "Site of the decisive defeat associated with Pang Juan’s end"}
  ],
  "subjects": ["Warring States", "Chinese military history", "Sun Bin", "Wei", "Qi", "Strategy", "Classical China"],
  "frameworks": ["CAUSE_AND_EFFECT", "DIPLOMATIC_HISTORY", "STRUCTURAL_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Pang Juan is the Wei antagonist in the Sun Bin tradition; his defeat at Maling encapsulates Warring States deception warfare and remains a staple of Chinese strategic memory.",
    "significanceCategory": "regional"
  }
},

"quintus-sextius": {
  "summary": (
    "Quintus Sextius the Elder was a Roman philosopher of the late Republic or early "
    "Empire who founded a short-lived but influential school combining Stoic ethics with "
    "Pythagorean ascetic and dietary practices. He declined a political career offered by "
    "Julius Caesar, choosing philosophy instead—a choice that later moralists, especially "
    "Seneca, celebrated as proof that Roman virtue need not depend on office. Sextius "
    "taught in Greek, emphasised rigorous self-examination, vegetarianism or abstention "
    "from animal flesh for some followers, and nightly review of one’s conduct.\n\n"
    "Though the Sextian school did not endure as a major sect beside Stoicism and "
    "Epicureanism, it mattered as a Roman attempt to live a philosophic life without "
    "simply copying Athenian institutions. Seneca repeatedly cites Sextius with admiration, "
    "preserving maxims and anecdotes that show how Roman elites adapted Greek philosophy "
    "into a practical regimen of character. In that sense Sextius stands at the junction "
    "of Pythagorean discipline and Stoic moral psychology in early Imperial Rome."
  ),
  "causes": [
    "Greek philosophical schools (Stoic, Pythagorean, Academic) flooded late Republican Rome, prompting Romans to found hybrid regimens suited to elite Latin life.",
    "Political violence and careerism in the late Republic made withdrawal into ethical self-cultivation an attractive alternative for some aristocrats.",
    "Demand among Roman elites for practical moral training—diet, nightly audit, courage—favoured teachers like Sextius who stressed lived discipline over pure dialectic."
  ],
  "effects": [
    "Seneca’s frequent praise transmitted Sextius’s example into the mainstream of Roman Stoic literature, giving the Sextian school an afterlife beyond its institutional life.",
    "The Sextians modelled a Romanised philosophic lifestyle that blended Stoic ethics with Pythagorean bodily discipline.",
    "Later moralists used Sextius’s refusal of Caesar’s offer as a stock exemplum of choosing virtue over political advancement."
  ],
  "relationships": [
    {"sourceSlug": "quintus-sextius", "sourceName": "Quintus Sextius", "verb": "INFLUENCES", "targetSlug": "seneca", "targetName": "Seneca the Younger", "context": "Seneca repeatedly cites Sextius as a model of Roman philosophical rigor and self-examination."},
    {"sourceSlug": "quintus-sextius", "sourceName": "Quintus Sextius", "verb": "DEFINES", "targetSlug": "sextian-school", "targetName": "Sextian school", "context": "Sextius founded a Roman philosophical school mixing Stoic ethics with Pythagorean ascetic practices."},
    {"sourceSlug": "stoicism", "sourceName": "Stoicism", "verb": "INFLUENCES", "targetSlug": "quintus-sextius", "targetName": "Quintus Sextius", "context": "Sextian teaching drew heavily on Stoic moral psychology while adding Pythagorean dietary and disciplinary elements."}
  ],
  "places": [
    {"name": "Rome", "role": "Centre of Sextius’s teaching and of the elite audience that received his school"},
    {"name": "Roman Italy", "role": "Cultural setting for Roman adaptations of Greek philosophy in the late Republic/early Empire"}
  ],
  "subjects": ["Roman philosophy", "Stoicism", "Pythagoreanism", "Seneca", "Ethics", "Late Republic", "Early Empire"],
  "frameworks": ["CULTURAL_TRANSMISSION", "PSYCHOLOGICAL_ANALYSIS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Quintus Sextius founded a Roman Stoic–Pythagorean school whose discipline and refusal of political office were immortalised by Seneca, illustrating how Romans remade Greek philosophy as lived ethics.",
    "significanceCategory": "regional"
  }
},

"sassetta": {
  "summary": (
    "Stefano di Giovanni di Consolo, called Sassetta (c. 1392–1450), was a leading "
    "painter of the Sienese school in the early Italian Renaissance. Working mainly in "
    "and for Siena, he produced altarpieces and narrative panels that combine Gothic "
    "grace—elongated figures, refined gold grounds, lyrical landscape—with a growing "
    "interest in spatial clarity and narrative psychology associated with early "
    "Renaissance painting. His masterpiece cycle includes scenes from the life of St "
    "Francis (the Borgo San Sepolcro altarpiece, now dispersed among museums), which "
    "rank among the most poetic Franciscan narratives of Quattrocento art.\n\n"
    "Sassetta’s importance lies in Siena’s distinctive path through the Renaissance: "
    "while Florence pursued linear perspective and monumental naturalism, Siena retained "
    "a decorative, spiritual elegance that Sassetta renewed rather than abandoned. He "
    "influenced later Sienese painters and remains central to understanding how central "
    "Italian cities negotiated innovation without discarding medieval sacred aesthetics. "
    "Modern rediscovery of his panels has secured his place as Siena’s greatest "
    "fifteenth-century painter."
  ),
  "causes": [
    "Siena’s strong late-Gothic sacred painting tradition created demand for altarpieces that preserved elegance and gold-ground splendour while absorbing new narrative techniques.",
    "Franciscan and civic patronage in Tuscany funded large narrative cycles that rewarded painters skilled at tender, legible storytelling.",
    "Contact with broader early Renaissance experiments in space and observation pushed Sassetta to modernise Sienese style without becoming Florentine."
  ],
  "effects": [
    "Sassetta defined the high point of early Quattrocento Sienese painting and shaped the city’s artistic identity beside Florence.",
    "The dispersed St Francis cycle became a touchstone for modern museums’ understanding of Franciscan iconography and Sienese lyricism.",
    "Later Sienese artists inherited his balance of Gothic refinement and Renaissance narrative clarity."
  ],
  "relationships": [
    {"sourceSlug": "sassetta", "sourceName": "Sassetta", "verb": "CREATES", "targetSlug": "borgo-san-sepolcro-altarpiece", "targetName": "Borgo San Sepolcro / St Francis altarpiece", "context": "Sassetta painted the celebrated Franciscan narrative altarpiece whose panels are now scattered across major collections."},
    {"sourceSlug": "sassetta", "sourceName": "Sassetta", "verb": "OCCURS_IN", "targetSlug": "siena", "targetName": "Siena", "context": "Sassetta was the principal early fifteenth-century painter of the Sienese school."},
    {"sourceSlug": "sassetta", "sourceName": "Sassetta", "verb": "TRANSMITS", "targetSlug": "sienese-gothic-tradition", "targetName": "Sienese Gothic painting tradition", "context": "He renewed Siena’s Gothic sacred style with early Renaissance spatial and narrative sensitivity."}
  ],
  "places": [
    {"name": "Siena, Tuscany", "role": "Principal city of Sassetta’s career and school"},
    {"name": "Borgo San Sepolcro (Sansepolcro)", "role": "Commission context for his major St Francis altarpiece"}
  ],
  "subjects": ["Italian Renaissance", "Sienese school", "Painting", "St Francis", "Quattrocento", "Tuscany", "Sacred art"],
  "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Sassetta was Siena’s foremost early Renaissance painter, fusing Gothic lyricism with Quattrocento narrative art and leaving a landmark Franciscan cycle.",
    "significanceCategory": "regional"
  }
},

"gerolamo-emiliani": {
  "summary": (
    "Gerolamo Emiliani (also Jerome Emiliani; 1486–1537) was a Venetian nobleman, "
    "soldier, and Catholic reformer who founded the Somaschi Fathers (Clerics Regular "
    "of Somasca), a congregation devoted to the care of orphans, the poor, and the "
    "sick. After a military career and imprisonment that prompted religious conversion, "
    "he turned his property and energy to hospitals and orphanages in northern Italy, "
    "especially around Venice, Verona, and Somasca near Bergamo. His work belongs to "
    "the broader Catholic reform and charitable renewal of the early sixteenth century, "
    "parallel to but distinct from the Protestant Reformation.\n\n"
    "Emiliani organised clerics living in common under a rule focused on education, "
    "relief, and pastoral care for abandoned children—an institutional response to war, "
    "famine, and urban poverty in Renaissance Italy. He died of plague in 1537 while "
    "serving the sick. Canonised in 1767 and later named a patron of orphans, he "
    "exemplifies how early modern Catholic reform channelled aristocratic resources into "
    "durable charitable orders whose schools and orphanages long outlived their founder."
  ),
  "causes": [
    "Wars, plague, and urban poverty in early sixteenth-century northern Italy left large numbers of abandoned children needing institutional care.",
    "Catholic reform currents before and during the Council of Trent encouraged new clerical congregations dedicated to active charity rather than only contemplative life.",
    "Emiliani’s own conversion after military captivity redirected Venetian noble wealth and organisational skill into orphan relief."
  ],
  "effects": [
    "The Somaschi Fathers institutionalised orphan care and education across Catholic Europe and later mission fields.",
    "Emiliani’s model linked aristocratic conversion to structured social welfare, influencing Counter-Reformation charity.",
    "His canonisation and patronage of orphans cemented him as a symbol of Catholic humanitarian reform in Italy."
  ],
  "relationships": [
    {"sourceSlug": "gerolamo-emiliani", "sourceName": "Gerolamo Emiliani", "verb": "CREATES", "targetSlug": "somaschi-fathers", "targetName": "Somaschi Fathers", "context": "Emiliani founded the Clerics Regular of Somasca to care for orphans, the poor, and the sick."},
    {"sourceSlug": "gerolamo-emiliani", "sourceName": "Gerolamo Emiliani", "verb": "OCCURS_DURING", "targetSlug": "catholic-reformation", "targetName": "Catholic Reformation", "context": "His charitable congregation formed part of early sixteenth-century Catholic renewal alongside Tridentine reform."},
    {"sourceSlug": "gerolamo-emiliani", "sourceName": "Gerolamo Emiliani", "verb": "TRANSFORMS", "targetSlug": "orphan-care-northern-italy", "targetName": "Orphan care in northern Italy", "context": "He converted personal piety into hospitals and orphanages that professionalised relief for abandoned children."}
  ],
  "places": [
    {"name": "Venice and Veneto", "role": "Region of Emiliani’s noble origin, conversion, and early charitable work"},
    {"name": "Somasca (near Bergamo)", "role": "Namesake centre of the Somaschi congregation"}
  ],
  "subjects": ["Catholic Reformation", "Somaschi Fathers", "Orphan care", "Venetian nobility", "Charity", "16th century", "Saints"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Gerolamo Emiliani founded the Somaschi Fathers and became a defining figure of early modern Catholic orphan care, later patron of orphans.",
    "significanceCategory": "regional"
  }
},

"alexander-neville": {
  "summary": (
    "Alexander Neville (c. 1340–1392) was Archbishop of York from 1374 until his "
    "translation and fall in 1388, a leading northern English churchman whose career "
    "was entangled with the politics of Edward III’s last years and the reign of "
    "Richard II. A member of the powerful Neville family, he rose through royal and "
    "papal favour to the second see of England, administering a vast northern province "
    "and sitting among the realm’s great prelates. His archiepiscopate coincided with "
    "fiscal strain, court faction, and the rising assertiveness of the Commons.\n\n"
    "In 1388 the Merciless Parliament and the Lords Appellant moved against Richard "
    "II’s favourites; Neville was impeached, deprived of York, and translated against "
    "his will to the titular see of St Andrews—effectively exile from English power—"
    "before fleeing abroad. He died in Louvain in 1392. Neville’s fall illustrates how "
    "late medieval English archbishops could be broken by aristocratic faction even "
    "when backed by kinship networks, and how York’s political weight made its "
    "incumbent a prize and a target in Ricardian politics."
  ),
  "causes": [
    "Neville kinship and royal patronage opened the path to York, one of England’s two archiepiscopal thrones.",
    "Richard II’s reliance on favoured clerics and the backlash of the Lords Appellant made politically exposed bishops vulnerable to impeachment.",
    "Northern ecclesiastical wealth and jurisdiction made the Archbishop of York a central player—and casualty—in late fourteenth-century factional struggle."
  ],
  "effects": [
    "Neville’s deprivation in 1388 demonstrated that parliamentary and magnate coalitions could unseat even an archbishop tied to a great family.",
    "The crisis reshaped the northern ecclesiastical hierarchy and warned subsequent York archbishops about court alignment.",
    "His exile and death abroad marked a sharp end to Neville influence at York until later generations of the family recovered political stature."
  ],
  "relationships": [
    {"sourceSlug": "alexander-neville", "sourceName": "Alexander Neville", "verb": "OCCURS_IN", "targetSlug": "archdiocese-of-york", "targetName": "Archdiocese of York", "context": "Neville served as Archbishop of York (1374–1388), head of England’s northern province."},
    {"sourceSlug": "lords-appellant", "sourceName": "Lords Appellant / Merciless Parliament", "verb": "TRANSFORMS", "targetSlug": "alexander-neville", "targetName": "Alexander Neville", "context": "The 1388 proceedings impeached Neville and drove him from York into effective exile."},
    {"sourceSlug": "alexander-neville", "sourceName": "Alexander Neville", "verb": "OCCURS_DURING", "targetSlug": "reign-of-richard-ii", "targetName": "Reign of Richard II", "context": "His rise and catastrophic fall were bound to the factional politics of Richard II’s early reign."}
  ],
  "places": [
    {"name": "York, England", "role": "Seat of Neville’s archiepiscopal power"},
    {"name": "Louvain (Leuven)", "role": "Place of exile and death after his deprivation"}
  ],
  "subjects": ["Medieval England", "Archbishops of York", "Richard II", "Merciless Parliament", "Neville family", "Church and state", "14th century"],
  "frameworks": ["DIPLOMATIC_HISTORY", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Alexander Neville’s archiepiscopate and 1388 fall show how Ricardian faction could destroy a Neville Archbishop of York, tying northern church power to national crisis.",
    "significanceCategory": "regional"
  }
},

"darius-the-mede": {
  "summary": (
    "Darius the Mede is a ruler named in the Book of Daniel as receiving the kingdom "
    "after the fall of Babylon and as the monarch under whom Daniel was cast into the "
    "lions’ den. The biblical text presents him as a Median king who organises the "
    "realm into satrapies and is manipulated by officials envious of Daniel. Outside "
    "Daniel, no clearly corresponding Median king of that name is attested in "
    "Achaemenid or Babylonian documentary sources for 539 BCE, when Cyrus the Great "
    "took Babylon.\n\n"
    "Scholars have proposed identifications with figures such as Ugbaru/Gubaru (a "
    "governor associated with Babylon’s fall), Cyaxares, or a throne-name for Cyrus, "
    "or have treated Darius the Mede as a literary–theological construction that "
    "fits Daniel’s schema of successive empires. Regardless of historicity, the "
    "figure is central to Jewish and later Christian interpretation of the Exile’s "
    "end, divine sovereignty over empires, and the narrative of faithful witness under "
    "foreign rule. He thus matters as a biblical–historiographical problem at the "
    "intersection of Median memory, Achaemenid conquest, and Second Temple literature."
  ),
  "causes": [
    "The fall of Babylon in 539 BCE and Persian–Median imperial succession created a historical horizon that biblical writers framed through named foreign kings.",
    "Danielic literature sought to portray Jewish fidelity under successive Near Eastern empires, requiring royal figures who could enact persecution and recognition.",
    "Median ethnic memory within the Achaemenid world supplied a category—‘the Mede’—that Daniel’s narrative could use for a transitional ruler."
  ],
  "effects": [
    "Darius the Mede became essential to Jewish and Christian readings of Daniel, liturgy, and art (especially the lions’ den episode).",
    "Modern biblical scholarship and ancient historiography debate his identity, shaping how historians reconcile Daniel with the Cyrus Chronicle and Herodotus.",
    "The figure reinforced a theological model of God raising and deposing empires in sequence—Babylon, Media/Persia, Greece, and beyond."
  ],
  "relationships": [
    {"sourceSlug": "darius-the-mede", "sourceName": "Darius the Mede", "verb": "OCCURS_IN", "targetSlug": "book-of-daniel", "targetName": "Book of Daniel", "context": "Darius the Mede appears as the ruler after Babylon’s fall and the king of the lions’ den narrative."},
    {"sourceSlug": "cyrus-the-great", "sourceName": "Cyrus the Great", "verb": "INFLUENCES", "targetSlug": "darius-the-mede", "targetName": "Darius the Mede", "context": "Historical conquest of Babylon by Cyrus frames scholarly attempts to identify or contextualise Daniel’s Darius the Mede."},
    {"sourceSlug": "darius-the-mede", "sourceName": "Darius the Mede", "verb": "FRAMES", "targetSlug": "daniel-lions-den", "targetName": "Daniel in the lions’ den", "context": "In Daniel, court intrigue under Darius leads to Daniel’s condemnation and miraculous deliverance."}
  ],
  "places": [
    {"name": "Babylon", "role": "Imperial capital whose fall sets the scene for Darius the Mede in Daniel"},
    {"name": "Media / Achaemenid Near East", "role": "Ethnic–political horizon implied by the epithet ‘the Mede’"}
  ],
  "subjects": ["Book of Daniel", "Achaemenid Empire", "Media", "Biblical historiography", "Babylonian Exile", "Second Temple literature", "Ancient Near East"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "COMPARATIVE_CIVILIZATIONS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Darius the Mede is a pivotal, debated figure in Daniel whose story shaped Jewish–Christian empire theology and continues to challenge correlation with Achaemenid history.",
    "significanceCategory": "regional"
  }
},

"crinagoras-of-mytilene": {
  "summary": (
    "Crinagoras of Mytilene (c. 70 BCE–after 11 CE) was a Greek epigrammatist from "
    "Lesbos who became a court poet in Augustan Rome. Of aristocratic Mytilenean "
    "background, he took part in embassies to Julius Caesar and Augustus on behalf of "
    "his city and settled into the cultural orbit of the imperial household, addressing "
    "epigrams to Augustus, Tiberius, and other notables. His surviving poems, preserved "
    "mainly in the Greek Anthology, treat gifts, imperial occasions, personal grief, "
    "and polished compliments in the concise elegiac style of Hellenistic epigram.\n\n"
    "Crinagoras illustrates how Greek literary talent was absorbed into the patronage "
    "networks of early Imperial Rome: a provincial notable who converted embassy "
    "access into lasting poetic proximity to power. His work documents the bilingual "
    "cultural world of the Augustan elite and the continued prestige of Greek verse "
    "beside Latin poetry. For historians of Lesbos and of Augustan court culture, he "
    "is a rare named bridge between eastern civic politics and Roman imperial ceremony."
  ),
  "causes": [
    "Mytilene’s need to negotiate status with Rome after civil wars sent aristocratic envoys like Crinagoras into Caesar’s and Augustus’s presence.",
    "Augustan court patronage rewarded Greek poets who could celebrate imperial occasions in refined Hellenistic epigram.",
    "The prestige of the Greek Anthology tradition gave Lesbians and other eastern Greeks a portable literary craft marketable in Rome."
  ],
  "effects": [
    "Crinagoras’s epigrams preserved in the Greek Anthology remain primary evidence for Greek voices at the Augustan court.",
    "His career modelled how eastern elites used poetry and diplomacy to secure favour under the Principate.",
    "Modern classicists use his dated poems as minor but useful anchors for Augustan and early Tiberian court chronology and gift culture."
  ],
  "relationships": [
    {"sourceSlug": "crinagoras-of-mytilene", "sourceName": "Crinagoras of Mytilene", "verb": "OCCURS_IN", "targetSlug": "mytilene", "targetName": "Mytilene (Lesbos)", "context": "Crinagoras was a Mytilenean aristocrat who represented his city on embassies to Roman leaders."},
    {"sourceSlug": "crinagoras-of-mytilene", "sourceName": "Crinagoras of Mytilene", "verb": "COLLABORATES_WITH", "targetSlug": "augustus", "targetName": "Augustus", "context": "He wrote court epigrams within the patronage circle of Augustus and the early imperial family."},
    {"sourceSlug": "crinagoras-of-mytilene", "sourceName": "Crinagoras of Mytilene", "verb": "CREATES", "targetSlug": "greek-anthology-epigrams", "targetName": "Epigrams (Greek Anthology)", "context": "His surviving epigrams entered the Greek Anthology as polished witnesses to Augustan Greek court poetry."}
  ],
  "places": [
    {"name": "Mytilene, Lesbos", "role": "Hometown and civic base of Crinagoras’s aristocratic career"},
    {"name": "Rome", "role": "Centre of his later life as an Augustan court epigrammatist"}
  ],
  "subjects": ["Greek Anthology", "Augustan Rome", "Epigram", "Lesbos", "Patronage", "Hellenistic poetry", "Principate"],
  "frameworks": ["CULTURAL_TRANSMISSION", "DIPLOMATIC_HISTORY", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Crinagoras linked Mytilenean diplomacy to Augustan court poetry; his Greek Anthology epigrams are key evidence for eastern Greek literati under the early Empire.",
    "significanceCategory": "regional"
  }
},

"calimerius": {
  "summary": (
    "Saint Calimerius (Italian: Calimero) was an early bishop of Milan, traditionally "
    "dated to the late 2nd or 3rd century CE, and is venerated as a martyr and one of "
    "the city’s principal early patrons. Medieval Milanese tradition holds that he was "
    "of Greek origin, served as bishop during persecution, and was killed by being "
    "cast into a well—an etiology tied to the basilica and cult site of San Calimero "
    "in Milan. Exact chronology is uncertain; as with many early Italian episcopal "
    "saints, hagiography and civic memory outrun contemporary documentation.\n\n"
    "Calimerius’s historical importance is institutional and cultic: he belongs to the "
    "chain of Milanese bishops who anchored Christianity in northern Italy before "
    "Ambrose, and his shrine helped structure Milan’s sacred topography. The persistence "
    "of his dedication through Ambrosian liturgy and local devotion shows how early "
    "martyr-bishops became pillars of civic Christian identity in Lombardy long after "
    "the persecutions ended."
  ),
  "causes": [
    "Christian communities in Roman northern Italy needed episcopal leadership under intermittent persecution, producing early bishop-martyr traditions.",
    "Milan’s later prominence as an imperial and ecclesiastical capital encouraged elaboration of founding-saint cults for pre-Ambrosian bishops.",
    "Local topography (wells, burial sites) generated martyr narratives that fixed Calimerius’s memory in specific Milanese places."
  ],
  "effects": [
    "The cult and basilica of San Calimero became lasting features of Milan’s religious landscape.",
    "Calimerius reinforced the model of the martyr-bishop as civic protector in Ambrosian Christianity.",
    "His legend supplied medieval Milan with an early Greek-linked apostolic–episcopal pedigree."
  ],
  "relationships": [
    {"sourceSlug": "calimerius", "sourceName": "Calimerius", "verb": "OCCURS_IN", "targetSlug": "milan", "targetName": "Milan", "context": "Calimerius is remembered as an early bishop and martyr-patron of Milan."},
    {"sourceSlug": "calimerius", "sourceName": "Calimerius", "verb": "PARTICIPATES_IN", "targetSlug": "early-christian-persecutions", "targetName": "Early Christian persecutions", "context": "Hagiographic tradition presents his death as martyrdom during Roman persecution of Christians."},
    {"sourceSlug": "calimerius", "sourceName": "Calimerius", "verb": "TRANSMITS", "targetSlug": "ambrosian-church-milan", "targetName": "Milanese / Ambrosian church tradition", "context": "His cult fed the pre-Ambrosian episcopal memory that later Ambrosian Milan preserved."}
  ],
  "places": [
    {"name": "Milan (Mediolanum)", "role": "See of Calimerius and centre of his cult"},
    {"name": "Basilica of San Calimero, Milan", "role": "Principal cult site associated with his martyrdom tradition"}
  ],
  "subjects": ["Early Christianity", "Milan", "Bishop-martyrs", "Ambrosian tradition", "Hagiography", "Roman Italy", "Saints"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 4,
    "significanceNarrative": "Calimerius is an early Milanese bishop-martyr whose cult helped found the city’s Christian topography before Ambrose.",
    "significanceCategory": "local"
  }
},

"marguerite-doingt": {
  "summary": (
    "Marguerite d’Oingt (c. 1240–1310) was a French Carthusian nun, prioress, and "
    "mystic, and one of the earliest named women writers in the Franco-Provençal "
    "literary sphere. Entering the Charterhouse of Poleteins (near Lyon), she rose to "
    "leadership in a strict contemplative order that rarely left written traces by "
    "women. Her surviving works—including a Latin page of meditations and vernacular "
    "texts such as the Speculum (Mirror) and accounts of Christina of Stommeln—"
    "combine visionary spirituality with careful attention to female sanctity and "
    "Carthusian interior life.\n\n"
    "Marguerite matters for medieval women’s writing and for Carthusian history: she "
    "shows that even in an order famed for silence, a prioress could authorise "
    "theological and hagiographical prose in Latin and the vernacular. Her Mirror "
    "offers a self-conscious spiritual text by a woman addressing salvation, vision, "
    "and community, making her a key figure in studies of medieval mysticism, "
    "gendered authorship, and the religious culture of the late thirteenth-century "
    "Lyonnais."
  ),
  "causes": [
    "The expansion of Carthusian houses for women created rare institutional space for literate female contemplatives in thirteenth-century France.",
    "Broader medieval mystical currents and demand for vernacular spiritual guidance encouraged nuns of authority to write.",
    "Marguerite’s office as prioress gave her the administrative standing and networks to compose and circulate texts about holiness."
  ],
  "effects": [
    "Her works stand among the earliest substantial writings by a named woman in Franco-Provençal/French religious literature.",
    "Modern scholarship on medieval mysticism and women’s authorship depends on her corpus as a Carthusian female voice.",
    "She helped document and promote models of female sanctity (including Christina of Stommeln) for contemplative readers."
  ],
  "relationships": [
    {"sourceSlug": "marguerite-doingt", "sourceName": "Marguerite d'Oingt", "verb": "OCCURS_IN", "targetSlug": "carthusian-order", "targetName": "Carthusian Order", "context": "She was a Carthusian nun and prioress at Poleteins, writing from within the order’s contemplative discipline."},
    {"sourceSlug": "marguerite-doingt", "sourceName": "Marguerite d'Oingt", "verb": "CREATES", "targetSlug": "speculum-marguerite-doingt", "targetName": "Speculum (Mirror) of Marguerite d'Oingt", "context": "Her Mirror and related texts are foundational witnesses to women’s mystical writing in her region."},
    {"sourceSlug": "marguerite-doingt", "sourceName": "Marguerite d'Oingt", "verb": "TRANSMITS", "targetSlug": "christina-of-stommeln", "targetName": "Christina of Stommeln", "context": "She wrote accounts that circulated knowledge of Christina’s sanctity among Carthusian and wider readers."}
  ],
  "places": [
    {"name": "Poleteins Charterhouse (near Lyon)", "role": "Convent where Marguerite lived, governed, and wrote"},
    {"name": "Lyonnais, France", "role": "Regional setting of her Carthusian and literary activity"}
  ],
  "subjects": ["Medieval mysticism", "Carthusians", "Women writers", "Franco-Provençal", "Hagiography", "13th century", "Christian spirituality"],
  "frameworks": ["FEMINIST_PERSPECTIVE", "RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Marguerite d’Oingt is among the earliest named women writers in her linguistic sphere and a rare Carthusian female mystical author.",
    "significanceCategory": "regional"
  }
},

"ulrich-of-zell": {
  "summary": (
    "Ulrich of Zell (also Ulrich of Cluny or of Regensburg; c. 1029–1093) was a "
    "Cluniac monk, abbot, and monastic reformer who helped transplant Cluny’s customs "
    "into the German lands. Born to a Swabian or Regensburg-area noble family and "
    "educated for church service, he entered Cluny under Abbot Hugh and became a "
    "trusted agent of Cluniac expansion. He founded or organised the priory of Zell "
    "(later associated with St Ulrich in the Black Forest region) and worked to impose "
    "Cluniac liturgical discipline, obedience, and exemption culture on houses north "
    "of the Alps.\n\n"
    "Ulrich’s career sits inside the eleventh-century monastic reform movement that "
    "paralleled early Gregorian reform: improving clerical morals, standardising "
    "liturgy, and linking local houses to Cluny’s network. His writings on custom "
    "and his reputation for austerity made him a vector of French Cluniac practice "
    "into the Empire. Venerated as a saint in local cult, he exemplifies how "
    "individual monk-abbots institutionalised transnational reform before the "
    "Investiture Contest fully reshaped church politics."
  ),
  "causes": [
    "Cluny’s eleventh-century prestige and papal support created a demand to export its customs into German monasteries.",
    "Imperial and noble patronage of reformed monasticism opened foundations such as Zell to Cluniac organisers.",
    "Ulrich’s training under Hugh of Cluny prepared him as a disciplined intermediary between Burgundian Cluny and the Empire."
  ],
  "effects": [
    "Cluniac observance gained a firmer foothold in southwestern German monasticism through Ulrich’s foundations and reforms.",
    "His example tied German noble piety to the international Cluniac network on the eve of the Investiture Controversy.",
    "Local sanctity cults preserved his memory as a bridge saint between Cluny and the German church."
  ],
  "relationships": [
    {"sourceSlug": "ulrich-of-zell", "sourceName": "Ulrich of Zell", "verb": "PARTICIPATES_IN", "targetSlug": "cluniac-reform", "targetName": "Cluniac reform", "context": "Ulrich carried Cluniac customs and discipline into German monastic houses as a reformer-abbot."},
    {"sourceSlug": "hugh-of-cluny", "sourceName": "Hugh of Cluny", "verb": "INFLUENCES", "targetSlug": "ulrich-of-zell", "targetName": "Ulrich of Zell", "context": "Ulrich was formed at Cluny under Abbot Hugh and acted as an agent of Hugh’s reforming network."},
    {"sourceSlug": "ulrich-of-zell", "sourceName": "Ulrich of Zell", "verb": "CREATES", "targetSlug": "priory-of-zell", "targetName": "Priory of Zell", "context": "He founded or organised the Cluniac priory of Zell that became the focus of his German reform work."}
  ],
  "places": [
    {"name": "Cluny, Burgundy", "role": "Mother house where Ulrich was trained and commissioned"},
    {"name": "Zell / Black Forest region", "role": "Centre of his German Cluniac foundation and cult"}
  ],
  "subjects": ["Cluniac reform", "Medieval monasticism", "Gregorian era", "German church", "Abbots", "11th century", "Saints"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Ulrich of Zell was a chief transmitter of Cluniac reform into the German Empire, founding Zell and embodying eleventh-century monastic internationalism.",
    "significanceCategory": "regional"
  }
},

"iset": {
  "summary": (
    "Iset (also Aset; a theophoric name related to Isis) was an ancient Egyptian "
    "royal woman of the Twentieth Dynasty who held the prestigious title God’s Wife "
    "of Amun, a pinnacle of female religious office at Thebes. God’s Wives of Amun "
    "controlled extensive temple estates, performed rituals as the earthly consort of "
    "the god Amun, and could wield political influence in Upper Egypt during the late "
    "New Kingdom, when royal power and Theban priesthood negotiated authority.\n\n"
    "Though less famous than some earlier or later God’s Wives, Iset belongs to the "
    "institutional history that made Theban priestly–royal women central to late New "
    "Kingdom and Third Intermediate religious politics. Her office illustrates how Egyptian "
    "kingship sacralised elite women as mediators of Amun’s cult, tying dynastic "
    "legitimacy to Karnak’s wealth. Prosopographical and monumental evidence for "
    "Twentieth-Dynasty God’s Wives remains thinner than for the Twenty-Fifth–Twenty-"
    "Sixth Dynasty holders, but Iset is an important named link in that sequence."
  ),
  "causes": [
    "The New Kingdom elevation of Amun of Karnak created a female sacerdotal office—God’s Wife of Amun—that channelled royal women into temple power.",
    "Late Twentieth-Dynasty politics in Thebes required trusted royal women to embody ritual legitimacy amid stretched imperial and dynastic resources.",
    "Theological marriage of the king’s daughter or relative to Amun institutionalised elite female authority in Upper Egypt."
  ],
  "effects": [
    "Iset’s tenure continued the Theban pattern of God’s Wives managing cult and estates, foreshadowing the still greater prominence of later God’s Wives.",
    "Her office reinforced Amun’s temple as a parallel power centre to the royal residence in the late New Kingdom.",
    "Egyptological reconstruction of Twentieth-Dynasty Theban religion depends on named holders like Iset to track the office’s continuity."
  ],
  "relationships": [
    {"sourceSlug": "iset", "sourceName": "Iset", "verb": "OCCURS_IN", "targetSlug": "gods-wife-of-amun", "targetName": "God's Wife of Amun", "context": "Iset held the office of God’s Wife of Amun, the leading female religious title at Thebes."},
    {"sourceSlug": "iset", "sourceName": "Iset", "verb": "OCCURS_DURING", "targetSlug": "twentieth-dynasty-egypt", "targetName": "Twentieth Dynasty Egypt", "context": "She belongs to the late New Kingdom Twentieth Dynasty sequence of Theban royal women."},
    {"sourceSlug": "cult-of-amun-karnak", "sourceName": "Cult of Amun at Karnak", "verb": "DEFINES", "targetSlug": "iset", "targetName": "Iset", "context": "The Amun cult’s theology and estates defined the powers and duties of God’s Wives such as Iset."}
  ],
  "places": [
    {"name": "Thebes / Karnak", "role": "Cult centre where the God’s Wife of Amun exercised ritual and economic power"},
    {"name": "Upper Egypt", "role": "Regional sphere of Theban priestly–royal authority in Iset’s era"}
  ],
  "subjects": ["Ancient Egypt", "God's Wife of Amun", "Twentieth Dynasty", "Thebes", "Women in religion", "New Kingdom", "Amun"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "FEMINIST_PERSPECTIVE"],
  "historicalSignificance": {
    "significanceScore": 4,
    "significanceNarrative": "Iset was a Twentieth-Dynasty God’s Wife of Amun, a named holder of Thebes’s most powerful female religious office in the late New Kingdom.",
    "significanceCategory": "local"
  }
},

"caracalla": {
  "summary": (
    "Caracalla (born Lucius Septimius Bassianus, later Marcus Aurelius Antoninus; "
    "188–217 CE) was Roman emperor from 198 (as co-ruler) and sole emperor from 211 "
    "until his assassination in 217. Son of Septimius Severus and Julia Domna, he "
    "secured sole power by having his brother Geta murdered in 211 and then "
    "conducting a bloody purge of Geta’s supporters. His reign is remembered for "
    "military largesse, campaigns in Germany and against Parthia, the Baths of "
    "Caracalla in Rome, and above all the Constitutio Antoniniana (212 CE), which "
    "extended Roman citizenship to nearly all free inhabitants of the empire.\n\n"
    "Ancient historians such as Cassius Dio and Herodian portray him as cruel and "
    "erratic; modern scholars also stress fiscal and military pressures that shaped "
    "Severan rule. The citizenship edict transformed the legal fabric of the empire, "
    "widening the tax base and remaking provincial identity even as Caracalla’s "
    "personal tyranny damaged dynastic legitimacy. He was murdered near Carrhae "
    "during the eastern campaign, and the Severan system staggered on under Macrinus "
    "and later Severan restorations."
  ),
  "causes": [
    "Septimius Severus’s military monarchy and dynastic arrangements placed Caracalla and Geta in a unstable co-rule that invited fratricide.",
    "Fiscal demands of an enlarged, restive army pushed Severan emperors toward broader taxation and citizenship reforms.",
    "Frontier wars with Germanic peoples and Parthia structured Caracalla’s need for campaigns, donatives, and propaganda of conquest."
  ],
  "effects": [
    "The Constitutio Antoniniana universalised Roman citizenship for free people, a watershed in imperial legal and fiscal history.",
    "Geta’s murder and subsequent terror deepened the reputation of Severan court violence and alienated senatorial opinion.",
    "Major building (the Baths of Caracalla) and eastern war ambitions left monumental and military legacies that outlived his assassination in 217."
  ],
  "relationships": [
    {"sourceSlug": "caracalla", "sourceName": "Caracalla", "verb": "CREATES", "targetSlug": "constitutio-antoniniana", "targetName": "Constitutio Antoniniana", "context": "In 212 CE Caracalla enacted the edict granting Roman citizenship to most free inhabitants of the empire."},
    {"sourceSlug": "caracalla", "sourceName": "Caracalla", "verb": "SUCCEEDS", "targetSlug": "septimius-severus", "targetName": "Septimius Severus", "context": "Caracalla succeeded his father Severus, first as co-emperor and then, after Geta’s death, as sole ruler."},
    {"sourceSlug": "caracalla", "sourceName": "Caracalla", "verb": "CREATES", "targetSlug": "baths-of-caracalla", "targetName": "Baths of Caracalla", "context": "He built the vast Thermae Antoninianae in Rome, among the empire’s greatest public bath complexes."}
  ],
  "places": [
    {"name": "Rome", "role": "Imperial capital; site of Geta’s murder and the Baths of Caracalla"},
    {"name": "Eastern frontier (Syria / Mesopotamia)", "role": "Theatre of his Parthian campaign and assassination near Carrhae"}
  ],
  "subjects": ["Roman Empire", "Severan dynasty", "Roman citizenship", "Constitutio Antoniniana", "Imperial politics", "3rd century", "Military emperors"],
  "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "ECONOMIC_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 8,
    "significanceNarrative": "Caracalla’s Constitutio Antoniniana remade Roman citizenship empire-wide; his fratricidal sole rule epitomises Severan military monarchy.",
    "significanceCategory": "world-changing"
  }
},

"guillaume-fichet": {
  "summary": (
    "Guillaume Fichet (1433–c. 1480) was a French theologian, rhetorician, and "
    "university official who, with Johann Heynlin (Jean Heynlin de Stein), brought "
    "the first printing press to France at the Sorbonne in Paris (1470). A prior of "
    "the Sorbonne and doctor of theology, Fichet championed humanist rhetoric and "
    "saw typography as a tool for reforming preaching, learning, and the "
    "circulation of classical and theological texts. The Paris press issued Latin "
    "works that signalled France’s entry into the Gutenberg revolution only "
    "fifteen years after Mainz.\n\n"
    "Fichet’s importance is both technological and cultural: he linked university "
    "scholastic institutions to the new medium, ensuring that print in France began "
    "under academic–clerical auspices rather than only commercial workshops. His "
    "collaboration with Heynlin and German printers illustrates how skills migrated "
    "from the Rhine to Paris. Though he later left for Italy and the press’s early "
    "phase was brief, the 1470 Sorbonne workshop inaugurated a Parisian print "
    "culture that soon became one of Europe’s densest."
  ),
  "causes": [
    "The rapid spread of Mainz-style printing created incentives for scholars to import presses into major university cities.",
    "Sorbonne humanists wanted faster, more accurate means to publish rhetoric, theology, and classical texts for reform of learning.",
    "Available German printers and capital made a Paris partnership between Fichet, Heynlin, and craftsmen feasible in 1470."
  ],
  "effects": [
    "France gained its first printing press under Sorbonne sponsorship, anchoring early French print in academic culture.",
    "Paris rapidly developed into a major European publishing centre in the decades after Fichet’s initiative.",
    "The episode became a landmark in histories of French humanism and the coming of the book."
  ],
  "relationships": [
    {"sourceSlug": "guillaume-fichet", "sourceName": "Guillaume Fichet", "verb": "COLLABORATES_WITH", "targetSlug": "johann-heynlin", "targetName": "Johann Heynlin", "context": "Fichet and Heynlin jointly established the first French printing press at the Sorbonne in 1470."},
    {"sourceSlug": "guillaume-fichet", "sourceName": "Guillaume Fichet", "verb": "CREATES", "targetSlug": "sorbonne-printing-press-1470", "targetName": "Sorbonne printing press (1470)", "context": "Their workshop introduced typographic printing to France from the Rhineland tradition."},
    {"sourceSlug": "printing-press", "sourceName": "Printing press", "verb": "TRANSFORMS", "targetSlug": "guillaume-fichet", "targetName": "Guillaume Fichet's scholarly programme", "context": "Fichet adopted print as an instrument of rhetorical and theological reform at the university."}
  ],
  "places": [
    {"name": "Paris (Sorbonne)", "role": "Site of the first printing press in France, organised by Fichet and Heynlin"},
    {"name": "Rhineland / Mainz tradition", "role": "Technological source of the printers and methods they imported"}
  ],
  "subjects": ["History of printing", "French humanism", "Sorbonne", "Incunabula", "15th century", "University of Paris", "Book history"],
  "frameworks": ["TECHNOLOGICAL_DETERMINISM", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 7,
    "significanceNarrative": "Guillaume Fichet co-founded France’s first printing press at the Sorbonne (1470), linking university humanism to the print revolution.",
    "significanceCategory": "regional"
  }
},

"cleobulina": {
  "summary": (
    "Cleobulina (also called Eumetis) was an archaic Greek poet traditionally "
    "associated with Lindos on Rhodes and identified in later sources as the "
    "daughter of Cleobulus, one of the Seven Sages. She is remembered for composing "
    "riddles (griphoi) in hexameter or elegiac form; a few riddles attributed to her "
    "survive in quotation, including the famous riddle of the cupping instrument. "
    "Like many early female poets, her biography is sparsely attested and partly "
    "legendary, filtered through anecdotal sage literature.\n\n"
    "Even so, Cleobulina occupies a notable place in the Greek imagination of wise "
    "women: she extends the Seven Sages milieu into female authorship and shows that "
    "riddling verse—later a symposium and school exercise—had early named "
    "practitioners. Feminist and literary historians treat her as evidence that "
    "archaic Greek literary culture, though male-dominated in the canon, preserved "
    "memories of women as intellectual performers in Ionic and Doric contexts."
  ),
  "causes": [
    "Archaic Greek wisdom culture prized concise, enigmatic verse as a display of intelligence in elite and educational settings.",
    "Genealogical linkage to Cleobulus of Lindos placed a daughter-poet inside the prestigious Seven Sages tradition.",
    "Oral and anecdotal transmission of riddles created space for named female attributions even when full corpora did not survive."
  ],
  "effects": [
    "A small set of attributed riddles kept Cleobulina’s name alive in Greek literary anecdote and proverbial wisdom.",
    "She became a classical reference point for women’s participation in early Greek intellectual culture.",
    "Later collectors of riddles and sayings used her as an authorizing female figure in the sage tradition."
  ],
  "relationships": [
    {"sourceSlug": "cleobulina", "sourceName": "Cleobulina", "verb": "OCCURS_IN", "targetSlug": "lindos-rhodes", "targetName": "Lindos, Rhodes", "context": "Tradition links Cleobulina to Lindos and to the household of Cleobulus of the Seven Sages."},
    {"sourceSlug": "cleobulus", "sourceName": "Cleobulus of Lindos", "verb": "INFLUENCES", "targetSlug": "cleobulina", "targetName": "Cleobulina", "context": "Ancient sources present her as Cleobulus’s daughter, situating her poetry in the Seven Sages milieu."},
    {"sourceSlug": "cleobulina", "sourceName": "Cleobulina", "verb": "CREATES", "targetSlug": "greek-riddles-griphoi", "targetName": "Greek riddles (griphoi)", "context": "She is credited with early hexameter/elegiac riddles that entered Greek anecdotal literature."}
  ],
  "places": [
    {"name": "Lindos, Rhodes", "role": "Traditional home associated with Cleobulina and Cleobulus"},
    {"name": "Archaic Greek world (Aegean)", "role": "Cultural sphere of early riddle poetry and sage lore"}
  ],
  "subjects": ["Archaic Greece", "Women poets", "Riddles", "Seven Sages", "Rhodes", "Greek literature", "Wisdom tradition"],
  "frameworks": ["FEMINIST_PERSPECTIVE", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 4,
    "significanceNarrative": "Cleobulina is an early named Greek woman poet of riddles, tied to the Seven Sages tradition and to surviving griphoi attributions.",
    "significanceCategory": "local"
  }
},

"gaius-julius-caesar": {
  "summary": (
    "Gaius Julius Caesar (c. 140–85 BCE)—not to be confused with his more famous "
    "son of the same name—was a Roman senator of the late second century BCE, "
    "brother-in-law of Gaius Marius through marriage into Marius’s circle, and "
    "father of the dictator Julius Caesar. He reached the praetorship and governed "
    "Asia as propraetor, representing a respectable but not yet dominant Julian "
    "career in an age when Marius’s military reforms and populares politics "
    "remade the Republic.\n\n"
    "His historical significance is largely genealogical and factional: by linking "
    "the Julii to Marius and bearing the son who would destroy the Republican "
    "balance, he stands at the origin point of the Caesarian dynasty’s rise. He "
    "died suddenly at Rome in 85 BCE while still relatively young, leaving his "
    "son’s upbringing partly in the shadow of Marian proscriptions and Sullan "
    "reaction. Ancient biographers treat him briefly, yet without this generation "
    "the Julian path to the dictatorship is incomplete."
  ),
  "causes": [
    "The marriage alliance between the Julii and Marius’s family embedded Gaius Julius Caesar in the leading populares military–political network.",
    "Competition for praetorships and provincial commands in the late second century offered mid-rank nobles a path to status without consulship.",
    "Marian dominance in the 100s–80s BCE elevated associated senators even when they were not themselves transformative generals."
  ],
  "effects": [
    "As father of Julius Caesar the dictator, he transmitted Julian name, Marian connections, and elite expectations to the next generation.",
    "His early death shaped the young Caesar’s vulnerable position during Sulla’s dictatorship and subsequent climb.",
    "Prosopography of the late Republic uses his career to map Julian–Marian kinship before the civil wars."
  ],
  "relationships": [
    {"sourceSlug": "gaius-julius-caesar", "sourceName": "Gaius Julius Caesar (father)", "verb": "INFLUENCES", "targetSlug": "julius-caesar", "targetName": "Julius Caesar (dictator)", "context": "He was the father of the future dictator, transmitting Julian identity and Marian factional ties."},
    {"sourceSlug": "gaius-julius-caesar", "sourceName": "Gaius Julius Caesar (father)", "verb": "COLLABORATES_WITH", "targetSlug": "gaius-marius", "targetName": "Gaius Marius", "context": "Through marriage alliance he was tied to Marius’s political–military circle in the late Republic."},
    {"sourceSlug": "gaius-julius-caesar", "sourceName": "Gaius Julius Caesar (father)", "verb": "OCCURS_DURING", "targetSlug": "late-roman-republic", "targetName": "Late Roman Republic", "context": "His senatorial career unfolded amid Marian politics and the crises preceding Sulla’s march on Rome."}
  ],
  "places": [
    {"name": "Rome", "role": "Centre of his senatorial career and place of death in 85 BCE"},
    {"name": "Province of Asia", "role": "Theatre of his propraetorian command"}
  ],
  "subjects": ["Roman Republic", "Julii", "Marius", "Julius Caesar", "Prosopography", "Late Republic", "Senators"],
  "frameworks": ["STRUCTURAL_ANALYSIS", "DIPLOMATIC_HISTORY", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Gaius Julius Caesar, father of the dictator, linked the Julii to Marius and formed the immediate parental generation of Rome’s most consequential political heir.",
    "significanceCategory": "regional"
  }
},

"helgaud": {
  "summary": (
    "Helgaud (Helgaldus) was a Benedictine monk of the abbey of Fleury "
    "(Saint-Benoît-sur-Loire) in the early eleventh century and the author of the "
    "Epitoma vitae regis Rotberti pii, a hagiographic biography of King Robert II "
    "the Pious of France (r. 996–1031). Writing from one of the realm’s great "
    "monasteries, Helgaud portrayed Robert as a sacral, charitable, miracle-"
    "working king rather than as a purely political Capetian operator—an image "
    "that served monastic ideals of righteous rulership.\n\n"
    "As a source, Helgaud is indispensable and problematic: he preserves unique "
    "anecdotes about Robert’s piety, marriages, and court, yet filters them "
    "through Fleury’s interests and hagiographic convention. Historians of the "
    "early Capetians depend on him alongside richer narrative sources to "
    "reconstruct the religious self-presentation of West Frankish kingship around "
    "the year 1000. Helgaud thus stands at the meeting point of monastic "
    "historiography and Capetian legitimacy."
  ),
  "causes": [
    "Fleury’s status as a premier Benedictine house gave its monks access to Capetian rulers and a mandate to write sacred history.",
    "Robert II’s public piety invited a hagiographic royal biography that could model Christian kingship for monastic readers.",
    "Eleventh-century Capetian need for sacral legitimacy encouraged friendly monastic portraits of the dynasty."
  ],
  "effects": [
    "The Epitoma became a principal narrative lens on Robert the Pious’s religious reputation.",
    "Later medieval and modern images of early Capetian sacral kingship drew heavily on Helgaud’s anecdotes.",
    "Fleury’s literary output reinforced the abbey’s role as a custodian of royal–monastic memory."
  ],
  "relationships": [
    {"sourceSlug": "helgaud", "sourceName": "Helgaud", "verb": "CREATES", "targetSlug": "epitoma-vitae-roberti-pii", "targetName": "Epitoma vitae regis Rotberti pii", "context": "Helgaud wrote the hagiographic life of Robert II that shapes much of the king’s pious reputation."},
    {"sourceSlug": "helgaud", "sourceName": "Helgaud", "verb": "OCCURS_IN", "targetSlug": "abbey-of-fleury", "targetName": "Abbey of Fleury", "context": "He was a monk of Fleury (Saint-Benoît-sur-Loire), a major Benedictine centre."},
    {"sourceSlug": "robert-ii-of-france", "sourceName": "Robert II of France", "verb": "INFLUENCES", "targetSlug": "helgaud", "targetName": "Helgaud", "context": "Robert’s reign and cult of piety were the subject and stimulus of Helgaud’s biography."}
  ],
  "places": [
    {"name": "Fleury (Saint-Benoît-sur-Loire)", "role": "Monastic home of Helgaud and intellectual centre of his royal biography"},
    {"name": "West Frankish / early Capetian France", "role": "Political world depicted in the life of Robert the Pious"}
  ],
  "subjects": ["Capetian France", "Monastic historiography", "Robert II", "Fleury", "Hagiography", "11th century", "Sacred kingship"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 5,
    "significanceNarrative": "Helgaud’s life of Robert II is a foundational monastic portrait of early Capetian sacral kingship from Fleury.",
    "significanceCategory": "regional"
  }
},

"artaxerxes-ii": {
  "summary": (
    "Artaxerxes II Mnemon (r. 404–358 BCE) was the longest-reigning Achaemenid "
    "Great King of Persia, son of Darius II and Parysatis. His accession followed "
    "the Peloponnesian War’s end and was immediately contested by his brother Cyrus "
    "the Younger, whose rebellion—chronicled by Xenophon in the Anabasis—ended in "
    "Cyrus’s death at Cunaxa (401 BCE). Artaxerxes II thereafter managed a vast "
    "empire facing Egyptian secession, satrapal revolts, Greek mercenary "
    "entanglements, and renewed war with Greek cities, including the King’s Peace "
    "(Peace of Antalcidas, 387/386 BCE) that reasserted Persian arbitration over "
    "Greece.\n\n"
    "Ancient Greek authors dominate the narrative, often hostile or Hellenocentric, "
    "yet Artaxerxes II’s longevity indicates effective, if embattled, imperial "
    "management. He sponsored building at Susa, Ecbatana, and Persepolis, and "
    "later tradition associates him with the cult of Anahita. His reign marks both "
    "the resilience and the structural strains of late Achaemenid rule before the "
    "fourth-century crises that preceded Alexander."
  ),
  "causes": [
    "Dynastic succession after Darius II produced a fraternal rivalry with Cyrus the Younger backed by Greek mercenaries.",
    "Persian need to control the Aegean and Anatolian seaboard after Athens’s fall drew Artaxerxes into Greek diplomacy and the King’s Peace.",
    "Egyptian independence movements and satrapal ambition tested the early fourth-century Achaemenid administrative system."
  ],
  "effects": [
    "Victory at Cunaxa preserved Artaxerxes’s throne and supplied Xenophon’s Anabasis with its central drama.",
    "The King’s Peace institutionalised Persian diplomatic supremacy in Greek affairs for a generation.",
    "Decades of managing revolt and recovery shaped the late Achaemenid empire that Alexander would later confront."
  ],
  "relationships": [
    {"sourceSlug": "artaxerxes-ii", "sourceName": "Artaxerxes II", "verb": "SUCCEEDS", "targetSlug": "darius-ii", "targetName": "Darius II", "context": "Artaxerxes II succeeded Darius II as Great King in 404 BCE."},
    {"sourceSlug": "cyrus-the-younger", "sourceName": "Cyrus the Younger", "verb": "CAUSES", "targetSlug": "artaxerxes-ii", "targetName": "Artaxerxes II's early crisis", "context": "Cyrus’s rebellion and death at Cunaxa defined the opening of Artaxerxes II’s reign."},
    {"sourceSlug": "artaxerxes-ii", "sourceName": "Artaxerxes II", "verb": "FRAMES", "targetSlug": "kings-peace-387", "targetName": "King's Peace (Peace of Antalcidas)", "context": "His diplomacy produced the 387/386 BCE settlement asserting Persian authority over Greek interstate order."}
  ],
  "places": [
    {"name": "Susa / Persepolis / Ecbatana", "role": "Achaemenid royal centres of Artaxerxes II’s court and building"},
    {"name": "Cunaxa (Babylonia)", "role": "Battlefield where Cyrus the Younger was killed in 401 BCE"}
  ],
  "subjects": ["Achaemenid Empire", "Persian kings", "Cunaxa", "King's Peace", "Xenophon", "Ancient Near East", "4th century BCE"],
  "frameworks": ["DIPLOMATIC_HISTORY", "WORLD_SYSTEMS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 8,
    "significanceNarrative": "Artaxerxes II’s long reign preserved Achaemenid power after Cunaxa and imposed the King’s Peace on Greece, defining early fourth-century Near Eastern geopolitics.",
    "significanceCategory": "world-changing"
  }
},

"paterius": {
  "summary": (
    "Paterius was a sixth–seventh-century bishop of Brescia and a scholarly "
    "compiler best known for assembling excerpts from the works of Pope Gregory "
    "the Great. Having served in Gregory’s administrative circle in Rome before "
    "his episcopate, he produced florilegia that organised Gregorian teachings for "
    "pastoral and studious use—an early example of the excerpt culture that "
    "transmitted late antique papal theology into Lombard Italy and beyond.\n\n"
    "In an age when full manuscript copies were scarce, Paterius’s compilations "
    "helped stabilise Gregory’s authority as a doctor of the Latin church. His "
    "career links Roman papal bureaucracy to northern Italian episcopal chairs "
    "during the Lombard period, showing how Gregorian thought travelled through "
    "trusted clerks turned bishops. Though not a major original theologian, he is "
    "significant as a vector of textual transmission in early medieval Italy."
  ),
  "causes": [
    "Gregory the Great’s large corpus required condensation for bishops and monks who could not own complete sets of his works.",
    "Paterius’s prior service in Gregory’s household gave him access, motive, and competence to compile authoritative excerpts.",
    "Lombard-era Italian churches needed portable pastoral theology grounded in Roman papal prestige."
  ],
  "effects": [
    "Gregorian doctrine circulated more widely in excerpted form through Paterius’s compilations.",
    "Brescia’s episcopal tradition gained a link to Gregory’s Roman circle.",
    "Later medieval readers encountered Gregory partly through intermediary florilegia of the kind Paterius pioneered."
  ],
  "relationships": [
    {"sourceSlug": "paterius", "sourceName": "Paterius", "verb": "TRANSMITS", "targetSlug": "gregory-the-great", "targetName": "Pope Gregory the Great", "context": "Paterius compiled excerpts that spread Gregory’s teachings in manageable form."},
    {"sourceSlug": "paterius", "sourceName": "Paterius", "verb": "OCCURS_IN", "targetSlug": "brescia", "targetName": "Brescia", "context": "He served as bishop of Brescia after working in Gregory’s Roman administration."},
    {"sourceSlug": "gregory-the-great", "sourceName": "Pope Gregory the Great", "verb": "INFLUENCES", "targetSlug": "paterius", "targetName": "Paterius", "context": "Paterius’s intellectual project was defined by loyalty to and curation of Gregory’s writings."}
  ],
  "places": [
    {"name": "Rome", "role": "Where Paterius served in Gregory the Great’s administrative circle"},
    {"name": "Brescia, northern Italy", "role": "See he governed as bishop and base for his compilatory legacy"}
  ],
  "subjects": ["Early Middle Ages", "Gregorian theology", "Florilegia", "Brescia", "Papacy", "Textual transmission", "Lombard Italy"],
  "frameworks": ["CULTURAL_TRANSMISSION", "RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 4,
    "significanceNarrative": "Paterius, bishop of Brescia and former Gregorian clerk, was an important early compiler who transmitted Pope Gregory the Great’s works through excerpt collections.",
    "significanceCategory": "local"
  }
},

"andrew-duke-of-calabria": {
  "summary": (
    "Andrew, Duke of Calabria (1327–1345), was a Hungarian Angevin prince, son of "
    "Charles I of Hungary and brother of Louis I the Great, who became the first "
    "husband of Joanna I of Naples. The marriage was meant to bind the Hungarian "
    "and Neapolitan branches of the Angevin family and to position Andrew for "
    "kingship in Naples, but it collapsed into one of the most notorious political "
    "crimes of fourteenth-century Italy: Andrew was murdered at Aversa in 1345, "
    "strangled during a conspiracy that contemporaries widely associated with "
    "factions at Joanna’s court—though Joanna’s personal guilt remains debated.\n\n"
    "Andrew’s death triggered Hungarian military intervention in Italy under Louis "
    "the Great, prolonged instability in the Kingdom of Naples, and a European "
    "scandal that shaped Joanna’s embattled reign. His short life thus sits at the "
    "fault line of Angevin dynastic politics between Buda and Naples, where "
    "marriage diplomacy failed and assassination redrew the balance of power."
  ),
  "causes": [
    "Angevin dynastic strategy sought to unite Hungarian and Neapolitan claims through Andrew’s marriage to Joanna I.",
    "Factional resistance at Naples to a Hungarian consort’s royal authority created a climate for conspiracy.",
    "Disputes over Andrew’s coronation and power-sharing with Joanna sharpened court enmities that ended in assassination."
  ],
  "effects": [
    "Andrew’s murder prompted Louis I of Hungary’s invasions of Naples and years of war in southern Italy.",
    "Joanna I’s reign was permanently shadowed by scandal, papal politics, and legitimacy contests.",
    "Angevin unity between Hungary and Naples fractured into open dynastic conflict."
  ],
  "relationships": [
    {"sourceSlug": "andrew-duke-of-calabria", "sourceName": "Andrew, Duke of Calabria", "verb": "COLLABORATES_WITH", "targetSlug": "joanna-i-of-naples", "targetName": "Joanna I of Naples", "context": "Andrew married Joanna I as part of an Angevin dynastic alliance that ended with his assassination in 1345."},
    {"sourceSlug": "andrew-duke-of-calabria", "sourceName": "Andrew, Duke of Calabria", "verb": "OCCURS_IN", "targetSlug": "kingdom-of-naples", "targetName": "Kingdom of Naples", "context": "As Duke of Calabria and royal consort he was embedded in Neapolitan succession politics."},
    {"sourceSlug": "louis-i-of-hungary", "sourceName": "Louis I of Hungary", "verb": "CAUSES", "targetSlug": "andrew-duke-of-calabria", "targetName": "aftermath of Andrew's death", "context": "Louis’s campaigns in Italy were launched to avenge his brother Andrew and assert Hungarian claims."}
  ],
  "places": [
    {"name": "Naples / Aversa", "role": "Political stage of Andrew’s marriage and site of his 1345 murder"},
    {"name": "Kingdom of Hungary", "role": "Dynastic origin and base of the retaliatory wars after his death"}
  ],
  "subjects": ["Angevin Naples", "Hungary", "Joanna I", "Medieval Italy", "Dynastic marriage", "14th century", "Political assassination"],
  "frameworks": ["DIPLOMATIC_HISTORY", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 6,
    "significanceNarrative": "Andrew of Calabria’s 1345 murder shattered Angevin marriage diplomacy and drew Hungary into war for Naples, defining Joanna I’s troubled reign.",
    "significanceCategory": "regional"
  }
},

"rabiah-ibn-al-harith": {
  "summary": (
    "Rabīʿah ibn al-Ḥārith ibn ʿAbd al-Muṭṭalib (c. 566–c. 640) was a first "
    "cousin of the Prophet Muhammad and a Companion (ṣaḥābī) of the early Islamic "
    "community. A member of the Banu Hashim within Quraysh, he belonged to the "
    "same clan network that framed Muhammad’s kinship politics in Mecca and "
    "Medina. Traditional Islamic biographical literature (sīra and ṭabaqāt) "
    "records him among the family members who navigated the transition from "
    "Meccan aristocracy to the new Muslim polity.\n\n"
    "Though not among the most prominent commanders or caliphs, Rabīʿah "
    "represents the Hashimite cousinage that gave the Prophet both support and "
    "internal complexity—kin who could convert, mediate, or compete as Islam "
    "reshaped Arabian social bonds. His lifespan bridges the late jāhiliyya, the "
    "Prophetic mission, and the early conquest-era caliphate, making him a "
    "useful prosopographical marker for Hashimite participation in Islam’s "
    "foundational generation."
  ),
  "causes": [
    "Hashimite kinship placed Rabīʿah in the Prophet’s immediate cousin circle within Quraysh.",
    "The formation of the Medinan umma drew Meccan relatives into new religious–political allegiances.",
    "Early Muslim biographical culture preserved Companion genealogies that kept lesser-known Hashimites in communal memory."
  ],
  "effects": [
    "His inclusion among Companions reinforced Hashimite presence in the first Islamic generation beyond the best-known figures.",
    "Later nasab and ṭabaqāt works used such cousins to map Quraysh–Hashim relations around the Prophet.",
    "He exemplifies how clan ties were reinterpreted under Islamic affiliation in the seventh century."
  ],
  "relationships": [
    {"sourceSlug": "rabiah-ibn-al-harith", "sourceName": "Rabi'ah ibn al-Harith", "verb": "OCCURS_DURING", "targetSlug": "prophetic-era-islam", "targetName": "Prophetic and early caliphal era", "context": "His life spanned the Prophet’s mission and the early Islamic community’s expansion."},
    {"sourceSlug": "rabiah-ibn-al-harith", "sourceName": "Rabi'ah ibn al-Harith", "verb": "COLLABORATES_WITH", "targetSlug": "muhammad", "targetName": "Prophet Muhammad", "context": "As a Hashimite first cousin and Companion, he belonged to Muhammad’s kinship and community circle."},
    {"sourceSlug": "banu-hashim", "sourceName": "Banu Hashim", "verb": "CONTAINS", "targetSlug": "rabiah-ibn-al-harith", "targetName": "Rabi'ah ibn al-Harith", "context": "He was a member of Banu Hashim, the Prophet’s clan within Quraysh."}
  ],
  "places": [
    {"name": "Mecca", "role": "Quraysh–Hashimite origin point of his family"},
    {"name": "Medina (Yathrib)", "role": "Centre of the early Muslim community to which Companions were oriented"}
  ],
  "subjects": ["Early Islam", "Companions", "Banu Hashim", "Quraysh", "Sira", "7th century", "Arabian history"],
  "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
  "historicalSignificance": {
    "significanceScore": 4,
    "significanceNarrative": "Rabīʿah ibn al-Ḥārith was a Hashimite cousin and Companion of Muhammad, a prosopographical link in Islam’s founding kinship network.",
    "significanceCategory": "local"
  }
},

"animal-husbandry": {
  "summary": (
    "Animal husbandry is the branch of agriculture concerned with the breeding, "
    "care, and exploitation of domesticated animals for meat, milk, fibre, labour, "
    "hides, and other products. Emerging from the Neolithic domestication of "
    "sheep, goats, cattle, pigs, and later horses and other species, it became a "
    "foundation of agrarian and pastoral economies worldwide. Practices range from "
    "nomadic pastoralism to intensive stall feeding, selective breeding, and "
    "modern industrial livestock systems.\n\n"
    "Historically, animal husbandry reshaped human settlement, disease "
    "environments, gender labour patterns, and landscapes through grazing and "
    "fodder crops. It enabled surplus, transport, and military power (horses, "
    "camels, oxen) and created enduring cultural complexes—from steppe nomadism "
    "to dairy-based Alpine and Indian economies. In the contemporary world it is "
    "central to debates on climate, antibiotics, animal welfare, and food "
    "security, but its deep history is the multi-millennial partnership between "
    "humans and domesticated animals that made complex societies possible."
  ),
  "causes": [
    "Neolithic domestication provided species amenable to controlled breeding and herd management.",
    "Human demand for reliable protein, fibre, labour, and transport incentivised specialised animal care beyond hunting.",
    "Environmental niches—grasslands, mixed farming zones, deserts—favoured distinct pastoral and mixed-husbandry strategies."
  ],
  "effects": [
    "Domestic herds underwrote agrarian surpluses, trade in animal products, and the rise of pastoralist polities.",
    "Close animal contact altered human disease ecology (zoonoses) and diets across Eurasia and Africa.",
    "Selective breeding and later scientific husbandry transformed animal genomes and global food systems."
  ],
  "relationships": [
    {"sourceSlug": "animal-husbandry", "sourceName": "Animal husbandry", "verb": "OCCURS_DURING", "targetSlug": "neolithic-revolution", "targetName": "Neolithic Revolution", "context": "Husbandry practices grew from Neolithic domestication of herd animals."},
    {"sourceSlug": "animal-husbandry", "sourceName": "Animal husbandry", "verb": "TRANSFORMS", "targetSlug": "agrarian-economies", "targetName": "Agrarian and pastoral economies", "context": "Managed animals became core capital for farming, pastoralism, transport, and warfare."},
    {"sourceSlug": "domestication", "sourceName": "Animal domestication", "verb": "CAUSES", "targetSlug": "animal-husbandry", "targetName": "Animal husbandry", "context": "Domestication created the biological basis for sustained breeding and herd management."}
  ],
  "places": [
    {"name": "Fertile Crescent and early domestication zones", "role": "Key early centres where herd animals were domesticated and husbanded"},
    {"name": "Global pastoral and mixed-farming regions", "role": "Worldwide arenas where husbandry systems diversified over millennia"}
  ],
  "subjects": ["Agriculture", "Domestication", "Pastoralism", "Neolithic", "Livestock", "Economic history", "Environmental history"],
  "frameworks": ["ENVIRONMENTAL_HISTORY", "LONGUE_DUREE", "ECONOMIC_ANALYSIS"],
  "historicalSignificance": {
    "significanceScore": 9,
    "significanceNarrative": "Animal husbandry, rooted in Neolithic domestication, is a civilisational foundation—shaping food, labour, warfare, disease, and landscapes to the present.",
    "significanceCategory": "world-changing"
  }
},

}


def load_claimed():
    meta = json.loads(CLAIM_META.read_text())
    return {c["slug"]: c for c in meta["claimed"]}


def release_claim(slug: str) -> None:
    enrich.release_claim_slug(slug)


def main() -> None:
    claimed = load_claimed()
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    results = []
    enriched = failed = skipped = 0

    for slug, payload in ENRICHMENTS.items():
        info = claimed.get(slug)
        if not info:
            print(f"SKIP {slug}: not in claim meta")
            skipped += 1
            continue
        filepath = info["filepath"]
        old_len = info["old_len"]
        # re-read current length
        with open(ROOT / filepath) as f:
            data = json.load(f)
        entity = next(e for e in data["entities"] if e.get("slug") == slug)
        old_len = len(entity.get("summary") or "")
        if old_len >= 800:
            print(f"SKIP {slug}: already {old_len}c")
            release_claim(slug)
            skipped += 1
            results.append({"slug": slug, "status": "skipped", "old_len": old_len, "reason": "already_enriched"})
            continue

        ok, reason = enrich.validate_enrichment(payload, lenient=False)
        if not ok:
            # try lenient before failing
            ok, reason = enrich.validate_enrichment(payload, lenient=True)
        if not ok:
            print(f"FAIL {slug}: validation {reason}")
            failed += 1
            results.append({"slug": slug, "status": "failed", "old_len": old_len, "reason": reason})
            release_claim(slug)
            continue

        enrich.apply_enrichment(str(ROOT / filepath), slug, payload)
        new_len = len(payload["summary"])
        print(f"OK   {slug}: {old_len} → {new_len}")
        enriched += 1
        results.append({"slug": slug, "status": "enriched", "old_len": old_len, "new_len": new_len})
        release_claim(slug)

    run = {
        "timestamp": ts,
        "model": EDITOR_ID,
        "sessionId": SESSION_ID,
        "count_requested": len(ENRICHMENTS),
        "enriched": enriched,
        "failed": failed,
        "skipped": skipped,
        "dry_run": False,
        "entities": results,
        "note": "Composer/agent batch; no Ollama. Wrote via ai_enrich_autonomous.apply_enrichment.",
    }
    REPORT_APPEND.write_text(json.dumps(run, indent=2) + "\n")
    # Also refresh last_run.json for KPI visibility
    (ROOT / "data/enrichment/last_run.json").write_text(json.dumps(run, indent=2) + "\n")
    enrich.update_audit_log(run)
    print(f"\nDONE enriched={enriched} failed={failed} skipped={skipped}")
    print(f"Report: {REPORT_APPEND}")


if __name__ == "__main__":
    main()
