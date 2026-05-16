#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 35 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: gospel-of-peter, gospel-of-philip,
          enma-eli (Enûma Eliš), alexandreis,
          a-clash-of-kings, ashoka-chakra,
          ethnomethodology, hazard-analysis-and-critical-control-points
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-35-may2026"

ENRICHMENTS = {

"gospel-of-peter": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-peter.json",
  "slug": "gospel-of-peter",
  "data": {
    "summary": "The Gospel of Peter is an early Christian apocryphal gospel of which a significant fragment was discovered in 1886–87 at Akhmim in Upper Egypt — an eighth-century parchment codex (the Akhmim Fragment, or Codex Panopolitanus) containing approximately 60 verses covering the trial, crucifixion, burial, guard at the tomb, and resurrection of Jesus Christ. The text is noteworthy as the only non-canonical source to include a dramatic narration of the actual moment of the Resurrection — in which two gigantic angels descend, open the tomb, and lead out Jesus (whose head reaches to the clouds), followed by a speaking cross — a visionary scene absent from all four canonical Gospels, which record only the empty tomb and post-resurrection appearances. First mentioned by Serapion of Antioch (c. 200 CE), who condemned it as docetic (teaching that Jesus only appeared to suffer), the Gospel of Peter is usually dated to the mid-2nd century CE, with some scholars arguing for an early 1st-century origin.\n\nThe docetic quality identified by Serapion — and debated by modern scholars — appears in the text's description of Jesus's silence during crucifixion ('He was silent, as though having no pain') and possibly in the variant of Jesus's last words ('My power, my power, why have you forsaken me?'). The Gospel of Peter's Passion narrative shares substantial material with the canonical Gospels (particularly Matthew, with the guard at the tomb) but also contains independent traditions: the attribution of responsibility for the crucifixion to Herod Antipas rather than Pilate, the role of Joseph of Arimathea, and the unique Resurrection scene. John Dominic Crossan controversially argued (1985) that an earlier 'Cross Gospel' embedded in the Gospel of Peter was a pre-canonical source used by all four canonical Gospels — a thesis that has not won broad scholarly acceptance but stimulated significant debate about the sources of the Passion narrative.\n\nThe Gospel of Peter, like the Gospel of Thomas and the Gospel of Mary, is evidence for the diversity of early Christian communities and their narratives about Jesus — demonstrating that the canonical fixation of the Gospels represented the triumph of one tradition (proto-orthodox, Petrine, anti-docetic) over several competing alternatives.",
    "causes": [
      "The diversity of early Christian communities and their Christological theologies — particularly docetism (the belief that Jesus's physical body was an appearance, not a material reality, and that he therefore only appeared to suffer) — created the context for the composition of alternative gospels that reflected different theological commitments about the nature of Jesus's suffering, resurrection, and relationship to matter.",
      "The Petrine tradition in early Christianity — the authority of Peter as the chief apostle and the theological centre of the proto-orthodox Christian community — provided both the attribution (the text is written in the first person as Peter's eyewitness account) and the polemical significance of the Gospel: attributing a docetically-flavoured account to Peter was both authoritative and theologically contentious.",
      "The discovery of the Akhmim Fragment in 1886–87 — which provided the first substantial text of the Gospel of Peter since antiquity — revived scholarly interest in early Christian apocrypha and stimulated the comparative study of the canonical Gospels' sources and the range of early Christian Christological traditions."
    ],
    "effects": [
      "The Gospel of Peter's unique Resurrection scene — the two gigantic angels, the speaking cross, and the figures whose heads reach to the clouds — influenced subsequent Christian art and apocryphal traditions, contributing to the elaboration of the Resurrection narrative in the broader Christian literary imagination.",
      "John Dominic Crossan's controversial 'Cross Gospel' hypothesis (The Cross That Spoke, 1985) — that the Gospel of Peter contains an earlier source used by all four canonical Gospels — stimulated significant scholarly debate about the sources of the Passion narrative and the relationships among the canonical Gospels, even though the thesis has not won broad acceptance.",
      "The Gospel of Peter, together with the Gospel of Thomas and the Gospel of Mary, contributed to the 20th-century scholarly and popular reassessment of early Christian diversity — demonstrating that the canonical New Testament represented the victory of proto-orthodox Christianity over a range of competing Christological traditions including docetism."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-peter", "sourceName": "Gospel of Peter (Akhmim Fragment, c. 150 CE)", "verb": "ATTRIBUTED_TO", "targetSlug": "peter-the-apostle", "targetName": "Peter the Apostle (chief apostle, Petrine tradition)", "context": "The Gospel of Peter is written in the first person as Peter's eyewitness account of the Passion and Resurrection — the Petrine attribution is part of the text's claim to apostolic authority."},
      {"sourceSlug": "gospel-of-peter", "sourceName": "Gospel of Peter (docetic elements)", "verb": "CONDEMNED_BY", "targetSlug": "serapion-of-antioch", "targetName": "Serapion of Antioch (c. 200 CE)", "context": "Serapion of Antioch condemned the Gospel of Peter as docetic — this early patristic condemnation (c. 200 CE) is the earliest external attestation of the text and established its status as a rejected heretical gospel."},
      {"sourceSlug": "gospel-of-peter", "sourceName": "Gospel of Peter (unique Resurrection scene)", "verb": "PART_OF", "targetSlug": "early-christian-apocrypha", "targetName": "Early Christian apocryphal literature (Nag Hammadi, Akhmim)", "context": "The Gospel of Peter is part of the body of early Christian apocryphal literature — texts that did not enter the canonical New Testament but reflect the diversity of early Christian communities' narratives about Jesus."}
    ],
    "places": [
      {"name": "Akhmim (Panopolis), Upper Egypt (Akhmim Fragment discovered 1886–87)", "role": "The Akhmim Fragment — the only substantial surviving text of the Gospel of Peter — was discovered in a tomb in Akhmim (ancient Panopolis) in 1886–87 during a French archaeological expedition"},
      {"name": "Antioch, Syria (Serapion's condemnation, c. 200 CE)", "role": "Serapion of Antioch's condemnation of the Gospel of Peter (c. 200 CE) is the earliest external attestation of the text — establishing that the Gospel was circulating in Syria in the late 2nd century"}
    ],
    "subjects": ["Early Christianity", "Classical Era", "Gnostic Christianity", "Apocryphal Gospels", "Passion Narrative", "Docetism", "Biblical Scholarship", "New Testament Apocrypha"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Gospel of Peter (c. 150 CE, rediscovered 1886–87) is the only non-canonical source to narrate the actual moment of the Resurrection — its unique dramatisation influenced subsequent Christian art and apocryphal traditions. It is evidence for early docetic Christology and for the diversity of early Christian Passion narratives, and it stimulated significant 20th-century debate about the sources of the canonical Gospels.",
      "significanceCategory": "significant"
    }
  }
},

"gospel-of-philip": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-philip.json",
  "slug": "gospel-of-philip",
  "data": {
    "summary": "The Gospel of Philip is a Gnostic text discovered at Nag Hammadi in Egypt in 1945 — Codex II, tractate 3 of the Nag Hammadi library — and dated by scholars to the 3rd century CE, probably composed in the Syrian Christian tradition and reflecting the theology of the Valentinian Gnostic school. Unlike the Gospel of Thomas (a collection of sayings) or the Gospel of Mary (a dialogue), the Gospel of Philip is an anthology of theological reflections, spiritual aphorisms, and commentary on the Christian sacraments — covering baptism, chrism (anointing), the Eucharist, redemption, and the bridal chamber — with particular emphasis on the spiritual significance of sacramental union and the concept of the 'bridal chamber' as the consummation of spiritual knowledge (gnosis). The text contains approximately 100 pericopes of varying length in Coptic translation from a Greek original.\n\nThe Gospel of Philip is particularly known for its references to Mary Magdalene as Jesus's 'companion' (koinônos) and the statement that Jesus 'loved her more than [all] the disciples and used to kiss her on her [mouth — the lacuna in the manuscript leaves the body part uncertain]' — a passage that has been widely interpreted (and misinterpreted, particularly in popular culture influenced by The Da Vinci Code) as suggesting a romantic or marital relationship between Jesus and Mary Magdalene, but which in its Valentinian theological context more plausibly reflects the spiritual symbolism of the bridal chamber gnosis. The Gospel of Philip's Mary Magdalene passages, read alongside the Gospel of Mary, provided the popular foundation for feminist theological arguments about Mary Magdalene's spiritual authority.\n\nThe Valentinian theological framework of the Gospel of Philip — its emphasis on sacramental knowledge, the spiritual significance of the bridal chamber, the distinction between psychic and pneumatic (spiritual) Christians, and its complex treatment of truth, falsehood, and the nature of names — reflects the sophisticated sacramental theology of one of the major Gnostic schools of the 2nd–3rd centuries CE. Its discovery at Nag Hammadi contributed substantially to the modern scholarly understanding of Valentinian Gnosticism.",
    "causes": [
      "The Valentinian Gnostic school — one of the major Gnostic Christian movements of the 2nd–3rd centuries CE, founded by Valentinus (c. 100–160 CE) — provided the theological framework of the Gospel of Philip: its distinction between psychic and pneumatic Christians, its sacramental theology of the bridal chamber, and its treatment of knowledge and spiritual transformation as the path to salvation.",
      "The Syrian Christian tradition — the distinctive theological culture of the Christian communities of Syria, which emphasised spiritual union, encratism (sexual asceticism), and a complex sacramental spirituality different from the Roman tradition — provided the likely compositional context for the Gospel of Philip, which scholars generally place in Syrian Valentinianism.",
      "The discovery of the Nag Hammadi library in Egypt in 1945 — a collection of 52 texts in 13 Coptic codices buried c. 390 CE — provided the archaeological context for the recovery of the Gospel of Philip, which (along with the Gospel of Thomas, the Gospel of Truth, and other Valentinian texts) substantially expanded modern knowledge of Gnostic Christianity."
    ],
    "effects": [
      "The Gospel of Philip's 'bridal chamber' theology — its emphasis on spiritual union as the consummation of gnosis — contributed to modern scholarship on Valentinian sacramental theology and on the diversity of early Christian approaches to sexuality, marriage, and spiritual practice.",
      "The Gospel of Philip's references to Mary Magdalene as Jesus's 'companion' whom he kissed — widely popularised by Dan Brown's The Da Vinci Code (2003) and subsequent popular culture — have stimulated both popular and scholarly discussion of Mary Magdalene's role in early Christianity and the question of women's spiritual authority, even though the text's actual meaning in its Valentinian context is more nuanced than popular treatments suggest.",
      "The Gospel of Philip, as part of the Nag Hammadi library, contributed to the 20th-century scholarly revolution in the understanding of early Christianity — demonstrating the diversity of early Christian theological traditions (Valentinian, Sethian, Thomasine) and the range of Christological, sacramental, and soteriological approaches in the pre-Nicene Christian world."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-philip", "sourceName": "Gospel of Philip (Nag Hammadi II, 3)", "verb": "PART_OF", "targetSlug": "nag-hammadi-library", "targetName": "Nag Hammadi library (1945 discovery, 52 texts)", "context": "The Gospel of Philip is Codex II, tractate 3 of the Nag Hammadi library — discovered in Egypt in 1945, a collection of 52 Gnostic and related texts in 13 Coptic codices."},
      {"sourceSlug": "gospel-of-philip", "sourceName": "Gospel of Philip (Valentinian theology)", "verb": "REFLECTS", "targetSlug": "valentinian-gnosticism", "targetName": "Valentinian Gnostic school (Valentinus, c. 100–160 CE)", "context": "The Gospel of Philip reflects the sacramental theology of the Valentinian Gnostic school — one of the major Gnostic Christian movements of the 2nd–3rd centuries, whose sophisticated theology of the bridal chamber and pneumatic/psychic distinction is developed throughout the text."},
      {"sourceSlug": "gospel-of-philip", "sourceName": "Gospel of Philip (Mary Magdalene as companion)", "verb": "REFERENCES", "targetSlug": "mary-magdalene", "targetName": "Mary Magdalene ('companion', Jesus kissed her)", "context": "The Gospel of Philip's statement that Jesus 'loved her more than all the disciples and used to kiss her' — in its Valentinian theological context about spiritual union — became widely known through The Da Vinci Code and stimulated popular and scholarly debate about Mary Magdalene's role in early Christianity."}
    ],
    "places": [
      {"name": "Nag Hammadi, Upper Egypt (December 1945, discovery site)", "role": "The Nag Hammadi library — including the Gospel of Philip — was discovered near Nag Hammadi in Upper Egypt in December 1945 by local farmers; the 52 texts in Coptic translation are the most important discovery for the study of Gnostic Christianity"},
      {"name": "Syria (probable compositional context, 3rd century CE)", "role": "The Gospel of Philip is generally placed in the Syrian Christian tradition — the distinctive theological culture of Christian communities in Syria that produced Valentinian texts with an emphasis on sacramental spirituality and the bridal chamber"}
    ],
    "subjects": ["Gnostic Christianity", "Classical Era", "Nag Hammadi", "Valentinian Gnosticism", "Mary Magdalene", "Early Christianity", "Sacramental Theology", "Biblical Scholarship"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Gospel of Philip (3rd century CE, Nag Hammadi discovery 1945) is a key text of Valentinian Gnostic sacramental theology — its bridal chamber theology and its references to Mary Magdalene as Jesus's 'companion' have made it a significant text for the study of early Christian diversity, feminist theology, and Gnostic practice. Part of the Nag Hammadi library, it substantially expanded modern knowledge of Valentinian Christianity.",
      "significanceCategory": "significant"
    }
  }
},

"enma-eli": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782enûma-eliš.json",
  "slug": "enma-eli",
  "data": {
    "summary": "The Enûma Eliš (Akkadian: 'When on high...', the opening words of the text) is the ancient Babylonian creation epic — the primary Mesopotamian cosmogonic narrative, composed in Akkadian cuneiform in the late 2nd millennium BCE (probably during the reign of Nebuchadnezzar I, c. 1125–1104 BCE, or earlier), and surviving in multiple cuneiform clay tablet copies from the Neo-Assyrian period (7th century BCE, discovered at Nineveh in Ashurbanipal's library). The epic consists of seven tablets and approximately 1,000 lines — narrating the creation of the cosmos through a theogonic and cosmogonic battle: the primordial salt-water goddess Tiamat and her consort Apsu give birth to the gods, whose noise disturbs Apsu's sleep; Apsu is killed by the god Ea; Tiamat gathers an army of monsters for revenge; the young god Marduk is chosen as champion of the gods; Marduk defeats and kills Tiamat in single combat; he splits her body to form the sky and earth; and from the blood of Tiamat's general Kingu, mixed with clay, he creates human beings as servants of the gods.\n\nThe Enûma Eliš is the foundational cosmogonic text of Mesopotamian religion and the primary literary celebration of Marduk as the supreme deity of the Babylonian pantheon — its composition reflects the elevation of Babylon as the political and religious centre of Mesopotamia under the Kassites and Neo-Babylonians, and the corresponding elevation of Marduk from a local city god to the supreme creator deity. The epic was recited in full on the fourth day of the Babylonian New Year festival (Akitu), making it a ritual text performed annually in the most important religious ceremony of the Babylonian year.\n\nThe Enûma Eliš has been of extraordinary importance for biblical scholarship and comparative religion — its structural parallels with the Genesis creation narrative (the primordial waters, creation by divine word and division of waters, the sequence of creation days) stimulated the 'Babel and Bible' controversy (Friedrich Delitzsch's lectures, 1902–1905) about the dependence of the Hebrew Bible on Babylonian literary traditions. Modern scholars generally recognise that the Genesis account reflects Mesopotamian cosmogonic traditions while also transforming them through its monotheistic theological framework.",
    "causes": [
      "The political rise of Babylon as the dominant city of Mesopotamia — from the Old Babylonian period (18th century BCE) through the Kassite period and Neo-Babylonian empire — required a theological framework that elevated Marduk from Babylon's local deity to the supreme creator and ruler of the cosmos. The Enûma Eliš is the primary theological document of this elevation of Marduk.",
      "The ancient Mesopotamian mythological tradition — including earlier Sumerian and Akkadian theogonic and cosmogonic narratives (the Sumerian myth of Enlil and the Eridu Genesis) — provided the raw material from which the Enûma Eliš was constructed: the combat with Tiamat, the creation from a slain deity's body, and the creation of humans as divine servants all have Sumerian antecedents.",
      "The Babylonian New Year festival (Akitu) — the most important religious ceremony of the Babylonian year, held over eleven days in the spring month of Nisannu — provided the ritual context for the Enûma Eliš, which was recited in full on the fourth day as part of the re-enactment of the cosmic creation that was understood to renew the world and validate royal power for another year."
    ],
    "effects": [
      "The Enûma Eliš's combat mythology — the creation of the world from a primordial monster's body through divine combat — is the primary ancient Near Eastern example of the Chaoskampf (chaos struggle) cosmogonic pattern, which has been identified by scholars (especially Hermann Gunkel) in the Hebrew Bible's creation and Flood narratives, in the Ugaritic Baal cycle, and in other ancient Near Eastern texts.",
      "Friedrich Delitzsch's lectures 'Babel und Bibel' (1902–1905) — arguing that the Hebrew Bible's creation narrative was derived from the Enûma Eliš — triggered a major public and scholarly controversy (the 'Babel-Bible controversy') about the relationships between Babylonian and Hebrew literature, stimulating the development of comparative Ancient Near Eastern studies and transforming biblical scholarship's understanding of the Hebrew Bible's literary context.",
      "The discovery of the Enûma Eliš — first identified by George Smith of the British Museum in 1875 among cuneiform tablets from Ashurbanipal's library at Nineveh (excavated by Layard in 1849–1851) — was a landmark event in the decipherment of cuneiform and in the growing 19th-century understanding of Mesopotamian civilisation as the cultural precursor of much of Western literary and religious tradition."
    ],
    "relationships": [
      {"sourceSlug": "enma-eli", "sourceName": "Enûma Eliš (Babylonian creation epic, c. 1100 BCE)", "verb": "CELEBRATES", "targetSlug": "marduk", "targetName": "Marduk (supreme deity of the Babylonian pantheon)", "context": "The Enûma Eliš is the primary literary celebration of Marduk as the supreme creator and ruler of the cosmos — its composition reflects the political elevation of Babylon and the corresponding elevation of Marduk from a local city god to the supreme deity."},
      {"sourceSlug": "enma-eli", "sourceName": "Enûma Eliš (cosmogonic combat)", "verb": "PARALLELS", "targetSlug": "genesis-creation-narrative", "targetName": "Genesis creation narrative (Hebrew Bible)", "context": "The Enûma Eliš's structural parallels with Genesis — primordial waters, creation by division, the creation sequence — stimulated the 'Babel-Bible controversy' (Delitzsch, 1902–1905) and transformed biblical scholars' understanding of the Hebrew Bible's Mesopotamian literary context."},
      {"sourceSlug": "enma-eli", "sourceName": "Enûma Eliš (Akitu recitation)", "verb": "PERFORMED_IN", "targetSlug": "babylonian-new-year-festival", "targetName": "Babylonian New Year festival (Akitu)", "context": "The Enûma Eliš was recited in full on the fourth day of the Babylonian Akitu (New Year) festival — the most important religious ceremony of the year — making it a living ritual text that renewed the cosmos and validated royal power annually."}
    ],
    "places": [
      {"name": "Babylon (cult centre of Marduk, composition and ritual context)", "role": "Babylon is the political and religious context of the Enûma Eliš — the epic's elevation of Marduk as supreme creator reflects and legitimises Babylon's dominance as the centre of Mesopotamian civilisation"},
      {"name": "Nineveh (Ashurbanipal's library, 7th century BCE, primary survival)", "role": "The best-preserved copies of the Enûma Eliš survive from Ashurbanipal's great library at Nineveh — excavated by Henry Layard (1849–1851) and first identified by George Smith (1875) — the primary source for modern knowledge of the text"}
    ],
    "subjects": ["Ancient Mesopotamia", "Ancient Era", "Babylonian Religion", "Creation Mythology", "Ancient Near East", "Cosmogony", "Akkadian Literature", "Biblical Studies"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Enûma Eliš (c. 1100 BCE) is the primary Mesopotamian creation epic — the foundational cosmogonic text of Babylonian religion, recited annually at the New Year festival, and the text whose structural parallels with the Genesis creation narrative triggered the 'Babel-Bible controversy' that transformed biblical scholarship. As the literary celebration of Marduk's supremacy, it reflects the cultural achievement of ancient Babylon and is among the most important texts of ancient world literature.",
      "significanceCategory": "world-changing"
    }
  }
},

"alexandreis": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782alexandreis.json",
  "slug": "alexandreis",
  "data": {
    "summary": "The Alexandreis is a Latin epic poem by Walter of Châtillon (c. 1135–c. 1190), a French poet and theologian, composed c. 1178–1182 and dedicated to Archbishop William of Reims — the most celebrated Latin epic of the 12th-century medieval renaissance and one of the most widely distributed and studied Latin texts of the medieval period, surviving in approximately 200 manuscripts. The Alexandreis narrates the military campaigns and death of Alexander the Great in ten books of approximately 5,500 hexameter verses, drawing primarily on Quintus Curtius Rufus's history of Alexander but also on Justin, Valerius Maximus, and the classical Latin epic tradition (Virgil's Aeneid, Lucan's Pharsalia, Statius's Thebaid). Walter's poem was widely used in medieval schools as a model of Latin style and learned composition, making it one of the primary vehicles through which medieval readers encountered the Alexander legend and the literary conventions of classical Latin epic.\n\nThe Alexandreis belongs to the 12th-century renaissance of Latin learning — the period of intellectual renewal associated with the cathedral schools of France (Chartres, Paris, Orleans), the rise of scholasticism, and the recovery and reinterpretation of classical Latin texts. Walter was a member of the circle of John of Salisbury and was associated with the learned culture of the French cathedral schools, and the Alexandreis demonstrates the characteristic preoccupations of the 12th-century renaissance: the use of classical sources to explore philosophical and ethical questions, the allegorical interpretation of history, and the tension between fortune and virtue as the explanation of historical change.\n\nThe Alexandreis's most influential passage — the underworld speech of the personified Nature, complaining about Alexander's insatiable ambition as a violation of natural order — provided a philosophical framework for the Alexander legend as a meditation on the limits of human ambition and the moral dangers of excessive conquest. Alexander is presented as both heroic and dangerously transgressive, a tension that gave the poem its moral complexity and contributed to the medieval tradition of Alexander as an exemplar of both greatness and pride.",
    "causes": [
      "The 12th-century renaissance of Latin learning — the revival of classical Latin literature, rhetoric, and philosophy in the cathedral schools of France and England — created the intellectual context for the Alexandreis: Walter's ambition to write a major Latin epic in the tradition of Virgil and Lucan, demonstrating mastery of classical style, reflected the 12th century's self-conscious identification with classical antiquity.",
      "The medieval fascination with Alexander the Great — the Alexander legend as mediated through Curtius, Justin, and the Alexander Romance tradition was one of the most popular narrative traditions of the Middle Ages — gave Walter a subject of guaranteed appeal and educational utility, while allowing him to explore the philosophical themes of ambition, fortune, and virtue through a historical narrative.",
      "The patronage system of the 12th-century cathedral schools — Archbishop William of Reims's patronage of the Alexandreis demonstrates the role of ecclesiastical patrons in supporting learned Latin composition — created the social conditions for major literary projects like the Alexandreis, which required years of sustained scholarly effort."
    ],
    "effects": [
      "The Alexandreis's widespread use in medieval schools — as a model of Latin composition, a source of classical allusions, and an example of the hexameter epic tradition — made it one of the most influential vehicles for the transmission of classical Latin literary technique and the Alexander legend in the 12th–15th centuries, surviving in approximately 200 manuscripts.",
      "Walter's treatment of Alexander as both heroic conqueror and dangerously transgressive overreacher — the speech of Nature condemning Alexander's violation of natural limits — contributed to the medieval moral tradition that used Alexander as an example of pride and the dangers of ambition, influencing the treatment of Alexander in Dante's Inferno, Chaucer, and other medieval writers.",
      "The Alexandreis's synthesis of classical Latin epic technique (hexameter, divine machinery, extended similes, underworld scene) with medieval Christian moral framework was influential on subsequent medieval Latin epic and on the broader project of the 12th-century renaissance — demonstrating that classical form could be used to convey Christian moral and philosophical content."
    ],
    "relationships": [
      {"sourceSlug": "walter-of-chatillon", "sourceName": "Walter of Châtillon (c. 1135–c. 1190)", "verb": "AUTHORS", "targetSlug": "alexandreis", "targetName": "Alexandreis (c. 1178–1182)", "context": "Walter composed the Alexandreis in ten books of hexameter verse — the most celebrated Latin epic of the 12th-century renaissance, drawing on Curtius Rufus's Alexander history and the classical Latin epic tradition."},
      {"sourceSlug": "alexandreis", "sourceName": "Alexandreis (Nature's speech, ambition and limits)", "verb": "INFLUENCES", "targetSlug": "medieval-alexander-tradition", "targetName": "Medieval Alexander tradition (moral exemplar, Dante, Chaucer)", "context": "Walter's presentation of Alexander as both heroic and transgressive — Nature's speech condemning his violation of natural limits — contributed to the medieval moral tradition that used Alexander as an exemplar of pride and the dangers of ambition."},
      {"sourceSlug": "alexandreis", "sourceName": "Alexandreis (12th-century Latin epic)", "verb": "PART_OF", "targetSlug": "twelfth-century-renaissance", "targetName": "12th-century renaissance (Latin learning, cathedral schools)", "context": "The Alexandreis is a central work of the 12th-century renaissance — the revival of classical Latin learning in the cathedral schools — demonstrating how classical form could be used to explore Christian moral and philosophical content."}
    ],
    "places": [
      {"name": "France (cathedral school context, c. 1178–1182)", "role": "The Alexandreis was composed in the French cathedral school environment — associated with the learned culture of Archbishop William of Reims's circle — the centre of the 12th-century renaissance of Latin learning"},
      {"name": "Medieval Europe (approximately 200 manuscripts, widespread school use)", "role": "The Alexandreis survives in approximately 200 manuscripts distributed across medieval Europe — evidence of its extraordinarily wide use as a school text and model of Latin composition in the 12th–15th centuries"}
    ],
    "subjects": ["Medieval Latin Literature", "Medieval Era", "Alexander the Great", "12th Century Renaissance", "Latin Epic", "Medieval Education", "Walter of Châtillon", "Alexander Legend"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Alexandreis (Walter of Châtillon, c. 1178–1182) is the most celebrated Latin epic of the 12th-century medieval renaissance — surviving in approximately 200 manuscripts and widely used in medieval schools as a model of Latin composition. Its treatment of Alexander as both heroic and transgressive contributed to the medieval moral tradition of Alexander as an exemplar of pride, and it exemplifies the 12th century's synthesis of classical Latin form with Christian moral philosophy.",
      "significanceCategory": "significant"
    }
  }
},

"a-clash-of-kings": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-clash-of-kings.json",
  "slug": "a-clash-of-kings",
  "data": {
    "summary": "A Clash of Kings is the second novel in George R. R. Martin's A Song of Ice and Fire epic fantasy series, published on 16 November 1998 by Bantam Books — with over 9 million copies sold worldwide and consistently ranked among the best-selling epic fantasy novels of the late 20th century. Set in Westeros following the death of King Robert Baratheon at the end of A Game of Thrones (1996), A Clash of Kings depicts the War of the Five Kings — the four-way civil war in which Robb Stark (King in the North), Stannis Baratheon (King by right), Renly Baratheon (King by popularity), Joffrey Baratheon (King in King's Landing), and Balon Greyjoy (King of the Iron Islands) simultaneously contest for the Iron Throne. The novel introduces the major characters of Stannis Baratheon and the red priestess Melisandre, continues the arc of Daenerys Targaryen with her dragons in Essos, and depicts the Battle of the Blackwater (the climactic naval battle in which Stannis's attack on King's Landing is repulsed by wildfire) — one of the most praised battle sequences in the series.\n\nA Clash of Kings is notable in the series for its elaboration of the supernatural and religious dimensions of the narrative — the resurrection of the religion of R'hllor (the Lord of Light) through Melisandre, the growing power of the White Walkers beyond the Wall as experienced by Jon Snow, and the reawakening of the dragons (now flying and fire-breathing) in Daenerys's arc. The novel's political complexity — the multi-sided civil war in which every claimant has legitimate and illegitimate arguments — continues Martin's rejection of Tolkienian moral clarity and his historically-grounded exploration of the Machiavellian dynamics of power.\n\nA Clash of Kings was adapted as the second season of the HBO series Game of Thrones (2012), which included the spectacular Battle of the Blackwater episode (directed by Neil Marshall) — widely praised as one of the finest battle sequences in television history. The HBO adaptation substantially raised the novel's profile and contributed to the global phenomenon that made the Game of Thrones franchise the most watched television drama in history.",
    "causes": [
      "The narrative momentum of A Game of Thrones — particularly the shocking execution of Ned Stark at the end of the first novel, which established Martin's willingness to kill major sympathetic characters — created the reader demand for A Clash of Kings and established the expectation that the series would continue to challenge the conventions of fantasy heroism and moral resolution.",
      "Martin's historical models for the War of the Five Kings — primarily the Wars of the Roses (the 15th-century English dynastic conflict between Lancaster and York) and the English civil war after Stephen and Matilda — provided the complex multi-sided dynastic conflict structure that gives A Clash of Kings its distinctive political texture: no clear hero, multiple legitimate claimants, and the chaos of competing loyalties.",
      "The introduction of Melisandre and the Lord of Light religion — which gives the supernatural dimension of the series a new force through the theme of resurrection and divine prophecy — reflects Martin's elaboration of the religious and magical dimensions of Westeros that were underdeveloped in the first novel, adding the messianic prophecy ('Azor Ahai reborn') that drives much of the subsequent series."
    ],
    "effects": [
      "A Clash of Kings established the multi-POV narrative structure of A Song of Ice and Fire — expanding from the Stark-centric first novel to a genuinely multi-polar narrative with equal weight given to Stannis, Daenerys, Jon, Arya, Sansa, Tyrion, and Theon Greyjoy — creating the large-cast ensemble narrative that became the template for subsequent epic fantasy series.",
      "The Battle of the Blackwater — the climactic naval battle in which Stannis's attack on King's Landing is repulsed by the explosion of wildfire — became one of the most admired set pieces in the series, and its HBO adaptation in Season 2 set a new standard for battle spectacle in television, influencing subsequent prestige television's approach to large-scale combat sequences.",
      "The Lord of Light religious arc introduced in A Clash of Kings — Melisandre's prophecies, the king's blood sacrifices, and eventually the resurrection of Jon Snow — became one of the most significant supernatural elements of the series, contributing to the narrative's exploration of the relationship between religion, prophecy, and power."
    ],
    "relationships": [
      {"sourceSlug": "george-r-r-martin", "sourceName": "George R. R. Martin (born 1948)", "verb": "AUTHORS", "targetSlug": "a-clash-of-kings", "targetName": "A Clash of Kings (1998)", "context": "Martin published A Clash of Kings as the second volume of A Song of Ice and Fire — depicting the War of the Five Kings and introducing Stannis Baratheon, Melisandre, and the Battle of the Blackwater."},
      {"sourceSlug": "a-clash-of-kings", "sourceName": "A Clash of Kings (War of the Five Kings)", "verb": "PART_OF", "targetSlug": "a-song-of-ice-and-fire", "targetName": "A Song of Ice and Fire (Martin series, 1996–)", "context": "A Clash of Kings is the second volume of A Song of Ice and Fire — expanding the political conflict of the first novel into the four-way War of the Five Kings and developing the supernatural and religious dimensions of the series."},
      {"sourceSlug": "a-clash-of-kings", "sourceName": "A Clash of Kings (Battle of the Blackwater)", "verb": "ADAPTED_AS", "targetSlug": "game-of-thrones-season-2", "targetName": "Game of Thrones Season 2 (HBO, 2012)", "context": "A Clash of Kings was adapted as the second season of HBO's Game of Thrones — the Battle of the Blackwater episode (directed by Neil Marshall) set a new standard for battle spectacle in television."}
    ],
    "places": [
      {"name": "King's Landing (Battle of the Blackwater, central conflict)", "role": "King's Landing — the capital of the Seven Kingdoms and the seat of the Iron Throne — is the primary contested location in A Clash of Kings, culminating in the spectacular Battle of the Blackwater as Stannis's fleet attacks by sea"},
      {"name": "Westeros and Essos (multi-POV narrative geography)", "role": "A Clash of Kings expands the narrative geography of the series — with viewpoint chapters across the North, the Wall, King's Landing, the Stormlands, the Iron Islands, and Daenerys's arc in Essos — developing the multi-polar world of the series"}
    ],
    "subjects": ["Fantasy Fiction", "Modern Era", "George R. R. Martin", "Epic Fantasy", "War of the Five Kings", "21st Century", "American Literature", "Television Adaptation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Clash of Kings (Martin, 1998) is the second volume of A Song of Ice and Fire — the most culturally impactful fantasy series since Tolkien. Its depiction of the War of the Five Kings, the introduction of Melisandre and the Lord of Light, and the Battle of the Blackwater established the series' narrative and supernatural framework. The HBO adaptation's Battle of the Blackwater episode set a new standard for television battle spectacle.",
      "significanceCategory": "significant"
    }
  }
},

"ashoka-chakra": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784ashoka-chakra.json",
  "slug": "ashoka-chakra",
  "data": {
    "summary": "The Ashoka Chakra (Sanskrit: अशोक चक्र, 'Wheel of Ashoka' or 'Wheel of the Law/Dharma') is a 24-spoked navy blue wheel featured at the centre of the National Flag of India (adopted 22 July 1947) — derived from the Lion Capital of Ashoka at Sarnath (c. 250 BCE), the stone column capital erected by the Mauryan Emperor Ashoka (r. c. 268–232 BCE) at the site of the Buddha's First Sermon, now the national emblem of India. The Chakra represents the dharmachakra (Wheel of Dharma) — the Buddhist symbol of the eternal and universal law, of ceaseless motion and progress, and of the Buddha's First Sermon at Sarnath ('Setting the Wheel of Dharma in motion'). In the context of the Indian national flag, the Ashoka Chakra represents the nation's commitment to progress and movement — replacing the spinning wheel (charkha) of Gandhi's flag with a symbol of Dharmic law and cosmic order.\n\nThe Lion Capital of Ashoka at Sarnath — from which the Ashoka Chakra is derived — is the most iconic example of Mauryan imperial art and the emblem adopted as the national emblem of India at independence (1950): the capital's four lions (back to back, representing strength and courage) with the Ashoka Chakra beneath them form the Emblem of India on all government seals, currency, and official documents. The Lions and Chakra are accompanied by the motto 'Satyameva Jayate' (Truth alone triumphs, from the Mundaka Upanishad) — together constituting the symbolic foundation of Indian national identity.\n\nThe Ashoka Chakra's adoption on the national flag was a deliberate act of symbolic choices by the Constitution Assembly — replacing Gandhi's charkha (which was associated with the independence movement but was also specifically Hindu, specifically Gandhian, and specifically about cottage industry) with an ancient, ecumenical, Buddhist symbol associated with the greatest emperor in Indian history. The choice of the Ashokan wheel was championed by B. R. Ambedkar — the architect of the Indian Constitution, a Buddhist himself — as a symbol that transcended the Hindu-Muslim divide and evoked India's pre-Hindu Buddhist heritage.",
    "causes": [
      "The need for a national symbol of independent India (1947) that could transcend the Hindu-Muslim communal divide and represent the entire subcontinent — the flag debate in the Constituent Assembly reflected the search for symbols of unity that did not privilege any single religious community, and the Ashokan chakra's Buddhist origin and ancient imperial associations gave it a neutrality that the charkha lacked.",
      "B. R. Ambedkar's advocacy for the Ashokan wheel — as the Buddhist symbol of the dharmachakra and a symbol of the greatest ruler in Indian history, whose rock edicts expressed the values of religious tolerance, non-violence, and social welfare that Ambedkar saw as the foundations of the new republic — gave the Ashoka Chakra its political champion in the Constituent Assembly debates.",
      "Emperor Ashoka's pan-Indian imperial project — his network of rock edicts, pillar edicts, and monuments across the subcontinent, establishing a common administrative and ethical framework — gave the Lion Capital and its chakra the authority of ancient all-Indian imperial precedent, making it a symbol that represented the entire subcontinent rather than any particular regional or religious tradition."
    ],
    "effects": [
      "The adoption of the Ashoka Chakra on the national flag made it the most visible symbol of Indian national identity worldwide — appearing on the flag flown at every government building, official ceremony, and international representation of India, and on the national emblem used on all official seals, currency, and documents.",
      "The Ashoka Chakra's adoption stimulated a major revival of scholarly and popular interest in Ashoka as a historical figure — the Emperor who had converted to Buddhism after the Kalinga War (c. 262–261 BCE), renounced military conquest, and established a programme of religious tolerance and welfare was presented as the model of the ideal ruler for independent India.",
      "The choice of the Ashokan wheel over Gandhi's charkha — and its association with the Buddhist tradition — was part of Ambedkar's broader political project of recovering India's Buddhist heritage as an alternative to upper-caste Hindu nationalism, and contributed to the symbolic framework of the Indian republic's secularism and constitutional democracy."
    ],
    "relationships": [
      {"sourceSlug": "ashoka-chakra", "sourceName": "Ashoka Chakra (24-spoked wheel, National Flag of India)", "verb": "DERIVED_FROM", "targetSlug": "lion-capital-of-ashoka", "targetName": "Lion Capital of Ashoka at Sarnath (c. 250 BCE)", "context": "The Ashoka Chakra on the Indian national flag is derived from the Lion Capital of Ashoka at Sarnath — the Mauryan column capital erected at the site of the Buddha's First Sermon, now the national emblem of India."},
      {"sourceSlug": "ashoka-chakra", "sourceName": "Ashoka Chakra (National Flag of India, 1947)", "verb": "SYMBOL_OF", "targetSlug": "republic-of-india", "targetName": "Republic of India (independence 1947, secular democracy)", "context": "The Ashoka Chakra at the centre of India's national flag represents the new republic's commitment to the Dharmic law — replacing Gandhi's charkha with an ancient Buddhist symbol transcending the Hindu-Muslim divide."},
      {"sourceSlug": "ashoka-chakra", "sourceName": "Ashoka Chakra (B.R. Ambedkar's advocacy)", "verb": "CHAMPIONED_BY", "targetSlug": "br-ambedkar", "targetName": "B. R. Ambedkar (architect of Indian Constitution, Buddhist)", "context": "Ambedkar championed the Ashokan wheel as a symbol transcending the Hindu-Muslim communal divide — its Buddhist origin and ancient imperial associations gave it the ecumenical neutrality required for the symbol of a secular republic."}
    ],
    "places": [
      {"name": "Sarnath, India (Lion Capital of Ashoka, c. 250 BCE)", "role": "Sarnath — the site of the Buddha's First Sermon — is where Ashoka erected the column capital from which the Ashoka Chakra is derived; the Lion Capital of Sarnath is now housed in the Sarnath Museum and is the national emblem of India"},
      {"name": "New Delhi (Constituent Assembly, flag adoption 22 July 1947)", "role": "The Constituent Assembly of India adopted the national flag — with the Ashoka Chakra at its centre — on 22 July 1947, two days before Indian independence; the debates over the flag's symbolism were conducted in New Delhi"}
    ],
    "subjects": ["Indian History", "Modern Era", "National Symbols", "Ashoka", "Buddhism", "Indian Independence", "B.R. Ambedkar", "Mauryan Empire"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Ashoka Chakra (adopted 1947) is the central symbol of the Indian national flag and national emblem — seen by over a billion people daily. Derived from the Lion Capital of Ashoka at Sarnath (c. 250 BCE), it represents the fusion of ancient Buddhist heritage with modern Indian national identity. Its adoption over Gandhi's charkha was a deliberate choice by B. R. Ambedkar to create a secular, ecumenical symbol for a diverse republic.",
      "significanceCategory": "highly-significant"
    }
  }
},

"ethnomethodology": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785ethnomethodology.json",
  "slug": "ethnomethodology",
  "data": {
    "summary": "Ethnomethodology is a sociological approach founded by Harold Garfinkel (1917–2011), introduced in his Studies in Ethnomethodology (1967) — a radical reorientation of sociological inquiry toward the study of the practical methods ('ethnomethods') that ordinary members of society use to make their everyday activities intelligible, orderly, and accountable to one another. Garfinkel coined the term from 'ethno' (people, member of a group) and 'methodology' (the methods used), reflecting his interest in how ordinary people themselves construct the social order through their practical reasoning and interaction — rather than how social structures, norms, or roles (in the sense of Parsonian structural functionalism) determine behaviour. Ethnomethodology's central claim is that social order is not a given structure imposed on social actors but an ongoing practical achievement — constantly produced and reproduced through members' indexical, reflexive practices of making sense of and accounting for their activities.\n\nGarfinkel's 'breaching experiments' — the now-famous demonstrations in which he had students violate conversational norms (responding to 'How are you?' with detailed medical reports; acting as lodgers in their own family homes) — demonstrated that social order is actively maintained through participants' practical reasoning, and that when this reasoning is disrupted, the fragility and achievement-character of ordinary social interaction becomes visible. These experiments were a methodological innovation that made visible the normally taken-for-granted practical accomplishments of everyday life — the conversational repair mechanisms, the interpretive charity, the use of context to make sense of ambiguous utterances.\n\nEthnomethodology has been particularly influential in generating three major programmes of research: conversation analysis (Harvey Sacks, Emanuel Schegloff, Gail Jefferson) — the rigorous micro-analysis of the sequential organisation of conversation — workplace studies (studies of how scientists, doctors, lawyers, and air traffic controllers organise their practical work), and science and technology studies (the study of how scientific knowledge is practically produced in laboratories). Together, these programmes have substantially influenced sociology, linguistics, communication studies, and human-computer interaction research.",
    "causes": [
      "Garfinkel's intellectual formation — his study with Talcott Parsons at Harvard and his engagement with Alfred Schutz's phenomenological sociology of the lifeworld — combined the sociological concern with social order (Parsons) with the phenomenological concern with the practical, pre-theoretical grounds of social life (Schutz), producing the distinctive ethnomethodological approach to social order as practical achievement.",
      "The dominant Parsonian structural functionalism of American sociology in the 1950s–1960s — which Garfinkel saw as treating social actors as 'cultural dopes' who passively follow norms rather than as competent practical reasoners who actively produce social order — provided the target against which ethnomethodology was defined: the insistence on the practical competence of ordinary members became the central counter-claim of ethnomethodology.",
      "The broader intellectual context of the 1960s sociological crisis — the challenge to structural functionalism from conflict theory (C. Wright Mills, Dahrendorf), symbolic interactionism (Goffman), and phenomenological sociology (Berger and Luckmann) — created the intellectual space for ethnomethodology's radical challenge to sociological orthodoxy, even though Garfinkel's approach was more thoroughgoing in its critique than any of these alternatives."
    ],
    "effects": [
      "Conversation analysis (CA) — founded by Harvey Sacks, Emanuel Schegloff, and Gail Jefferson in the late 1960s and 1970s from ethnomethodological premises — became one of the most productive and internationally influential programmes in linguistics and sociology, providing rigorous sequential analysis of the turn-taking, repair, and sequential organisation of conversation that is now a major field of research worldwide.",
      "Ethnomethodology's workplace studies — developed from the 1980s onwards, studying how professionals (scientists, doctors, airline dispatchers, call centre workers) organise their practical work — influenced the field of computer-supported cooperative work (CSCW) and human-computer interaction (HCI), contributing to the design of workplace technologies and the development of practice-based approaches to technology design.",
      "Ethnomethodology's fundamental insight — that social order is a practical achievement produced through members' ongoing interpretive work rather than a structure imposed by norms — influenced the 'practice turn' in social theory (Bourdieu, Giddens, Schatzki), conversation analysis, discourse analysis, and the sociology of knowledge, making it one of the most theoretically consequential innovations in 20th-century sociology."
    ],
    "relationships": [
      {"sourceSlug": "harold-garfinkel", "sourceName": "Harold Garfinkel (1917–2011)", "verb": "FOUNDS", "targetSlug": "ethnomethodology", "targetName": "Ethnomethodology (Studies in Ethnomethodology, 1967)", "context": "Garfinkel founded ethnomethodology in his Studies in Ethnomethodology (1967) — introducing the approach through breaching experiments and the concept of practical reasoning as the basis of social order."},
      {"sourceSlug": "ethnomethodology", "sourceName": "Ethnomethodology (practical reasoning, Garfinkel)", "verb": "GENERATES", "targetSlug": "conversation-analysis", "targetName": "Conversation analysis (Sacks, Schegloff, Jefferson)", "context": "Conversation analysis — founded by Harvey Sacks, Emanuel Schegloff, and Gail Jefferson from ethnomethodological premises — became one of the most productive and internationally influential research programmes in linguistics and sociology."},
      {"sourceSlug": "ethnomethodology", "sourceName": "Ethnomethodology (social order as achievement)", "verb": "CHALLENGES", "targetSlug": "structural-functionalism", "targetName": "Parsonian structural functionalism", "context": "Ethnomethodology's central claim — that social order is a practical achievement produced through members' ongoing interpretive work — was a direct challenge to Parsonian structural functionalism's treatment of social actors as passive norm-followers rather than competent practical reasoners."}
    ],
    "places": [
      {"name": "University of California, Los Angeles (UCLA, Garfinkel's base)", "role": "Garfinkel was a professor at UCLA from 1954, and the ethnomethodology programme developed in Los Angeles — attracting a generation of sociologists and linguists who developed conversation analysis and workplace studies"},
      {"name": "United States and international (global diffusion from 1970s)", "role": "Ethnomethodology and conversation analysis spread internationally from the 1970s — particularly in the UK (Loughborough, University of York), Scandinavia, and Japan — becoming a major international programme in sociology, linguistics, and communication studies"}
    ],
    "subjects": ["Sociology", "Modern Era", "Harold Garfinkel", "Social Theory", "Qualitative Methods", "Conversation Analysis", "20th Century", "Social Interaction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Ethnomethodology (Garfinkel, 1967) is one of the most theoretically consequential innovations in 20th-century sociology — its claim that social order is a practical achievement rather than an imposed structure launched conversation analysis (now a major international field), influenced workplace studies, and contributed to the 'practice turn' in social theory. Garfinkel's breaching experiments are among the most cited methodological demonstrations in the social sciences.",
      "significanceCategory": "highly-significant"
    }
  }
},

"hazard-analysis-and-critical-control-points": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785hazard-analysis-and-critical-control-points.json",
  "slug": "hazard-analysis-and-critical-control-points",
  "data": {
    "summary": "Hazard Analysis and Critical Control Points (HACCP) is a systematic preventive food safety management system that identifies, evaluates, and controls hazards (biological, chemical, physical) significant to food safety throughout the food production process — from raw material production through processing, distribution, and consumption. HACCP was developed jointly by the Pillsbury Company, the US Army Natick Laboratories, and NASA in the late 1950s–1960s as part of NASA's requirement for zero-defect food for the manned space programme — astronauts could not risk food poisoning in space — and was first presented publicly by Howard Bauman (Pillsbury's food safety director) at the 1971 National Conference on Food Protection. The system is based on seven principles: identify hazards, determine critical control points (CCPs), establish critical limits, establish monitoring procedures, establish corrective actions, establish verification procedures, and establish documentation.\n\nHACCP represented a revolutionary shift in food safety philosophy — from end-product testing (testing finished food for contamination, which is reactive, statistically limited, and economically wasteful) to process control (identifying the specific points in the production process where hazards can be controlled, monitoring those points, and taking corrective action when critical limits are exceeded). This preventive, process-based approach — with its emphasis on systematic hazard analysis and documented control — proved far more effective at ensuring food safety than the traditional inspection-and-testing model.\n\nHACCP has become the international standard for food safety management — incorporated into the Codex Alimentarius (the UN/WHO international food standards body) in 1993, mandated by the EU for all food businesses from 1995 (Directive 93/43/EEC) and by the US FDA for seafood (1997), meat and poultry, and most recently through the Food Safety Modernization Act (FSMA, 2011). Its systematic, documented approach has influenced the development of ISO 22000 (Food Safety Management Systems) and of analogous hazard analysis approaches in pharmaceutical manufacturing, medical device production, and other industries where process safety is critical.",
    "causes": [
      "NASA's manned space programme — particularly the requirement for zero-defect food for astronauts who could not risk food poisoning in the zero-gravity, remote environment of space — drove the development of HACCP: Pillsbury was contracted to produce food for the Mercury and Apollo programmes, and the requirement for unprecedented food safety standards motivated the development of a preventive, process-based approach.",
      "The inadequacy of traditional food safety inspection — the recognition that end-product testing could only detect a small fraction of contaminated products (statistically, testing every can of food would require destroying it), and that traditional inspection was reactive rather than preventive — motivated the search for a systematic process-control approach that could guarantee safety at the production stage.",
      "The post-World War II development of systems engineering and operations research — the application of systematic, quantitative approaches to complex engineering and process problems, developed in the aerospace and defence industries — provided the conceptual framework for HACCP's systematic identification of critical control points and its emphasis on documented procedures and monitoring."
    ],
    "effects": [
      "HACCP's incorporation into the Codex Alimentarius (1993) and its mandatory adoption by the EU (1995) and US FDA (1997) made it the international standard for food safety management — directly affecting every stage of the global food supply chain and the regulatory requirements for food businesses in over 180 countries.",
      "HACCP's systematic, process-based approach to hazard control influenced the development of analogous quality and safety management systems in pharmaceutical manufacturing (GAMP), medical device production, cosmetics, and other industries — making it the model for process-based safety management more broadly.",
      "HACCP's requirement for documented hazard analysis and critical control point monitoring transformed the food industry's approach to safety management — from a craft-based inspection model to a systematic, scientifically-grounded process control system — and contributed to the major improvements in food safety outcomes in the countries that adopted it."
    ],
    "relationships": [
      {"sourceSlug": "hazard-analysis-and-critical-control-points", "sourceName": "HACCP (Pillsbury/NASA, 1959–1971)", "verb": "DEVELOPED_FOR", "targetSlug": "nasa-space-programme", "targetName": "NASA manned space programme (zero-defect food requirement)", "context": "HACCP was developed for NASA's manned space programme — the requirement for zero-defect food for astronauts in space drove Pillsbury to develop the preventive, process-based food safety system that became the international standard."},
      {"sourceSlug": "hazard-analysis-and-critical-control-points", "sourceName": "HACCP (Codex Alimentarius, 1993)", "verb": "STANDARDISED_BY", "targetSlug": "codex-alimentarius", "targetName": "Codex Alimentarius (UN/WHO food standards body)", "context": "HACCP was incorporated into the Codex Alimentarius in 1993 — making it the international standard for food safety management, subsequently mandated by the EU (1995) and US FDA (1997) and adopted globally."},
      {"sourceSlug": "hazard-analysis-and-critical-control-points", "sourceName": "HACCP (process-based safety management)", "verb": "INFLUENCES", "targetSlug": "iso-22000", "targetName": "ISO 22000 (Food Safety Management Systems)", "context": "HACCP's systematic process-based approach influenced the development of ISO 22000 (Food Safety Management Systems) and of analogous hazard analysis approaches in pharmaceutical, medical device, and other safety-critical industries."}
    ],
    "places": [
      {"name": "Pillsbury Company, Minneapolis, Minnesota (development, late 1950s–1960s)", "role": "HACCP was developed at the Pillsbury Company in Minneapolis in collaboration with NASA and US Army Natick Laboratories — as part of Pillsbury's contract to produce food for the NASA manned space programme"},
      {"name": "Global (Codex Alimentarius 1993, EU 1995, FDA 1997, international standard)", "role": "HACCP is now the international standard for food safety management — mandated across the global food supply chain through the Codex Alimentarius, EU food hygiene regulations, and US FDA requirements"}
    ],
    "subjects": ["Food Safety", "Modern Era", "Systems Engineering", "NASA", "Public Health", "Food Industry", "Regulatory Standards", "Operations Research"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "HACCP (Pillsbury/NASA, 1959–1971, Codex Alimentarius 1993) is the international standard for food safety management — a systematic preventive approach that transformed food safety from end-product testing to process control. Developed for NASA's manned space programme, it has since been mandated across the global food supply chain and influenced analogous safety management systems in pharmaceutical and medical device manufacturing. Its adoption has contributed to major improvements in food safety outcomes worldwide.",
      "significanceCategory": "highly-significant"
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
