#!/usr/bin/env python3
"""
VS Code Enrichment Batch 64 — 8 Historical Figures
Jesus Christ, Martin Luther, Thomas Aquinas, René Descartes,
Sigmund Freud, Hippocrates, Gottfried Wilhelm Leibniz, Pythagoras

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-64-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-64-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Jesus Christ ──────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201jesus-christ.json",
        "slug": "jesus-christ",
        "era_correction": None,
        "data": {
            "summary": (
                "Jesus of Nazareth (c. 4 BCE – c. 30–33 CE) was a 1st-century Jewish preacher, healer, and teacher from Galilee whose life, death, and reported resurrection became the foundation of Christianity — the world's largest religion, with 2.4 billion adherents. More books have been written about him than any other human being, and the Western calendar counts years from his birth (Anno Domini). Whether viewed as the Son of God incarnate (Christian theology), a prophet (Islamic tradition), a failed messianic claimant (Talmudic view), or a historical reformer (secular scholarship), no other individual has more fundamentally shaped human civilization.\n\n"
                "Historical evidence places Jesus in 1st-century Roman-occupied Judea: John the Baptist baptized him (corroborated by Josephus); Roman prefect Pontius Pilate crucified him (confirmed by Tacitus and Josephus); and within decades his followers had established communities across the Mediterranean. His ministry (lasting 1–3 years) centered on the Kingdom of God, radical love of enemies and neighbors, care for the poor and outcast, and a prophetic challenge to religious and political authority. The Sermon on the Mount ('Blessed are the peacemakers') remains one of history's most influential ethical texts.\n\n"
                "Paul of Tarsus, who encountered the risen Christ on the road to Damascus (c. 33–36 CE), transformed the Jewish sect into a universal movement — removing circumcision requirements and extending membership to Gentiles. Within 300 years, Christianity had become the Roman Empire's official religion under Constantine (313 CE). The New Testament, compiled over the first century, provides the primary textual record.\n\n"
                "'Love your neighbor as yourself' (Matthew 22:39) — eight simple words that have inspired cathedrals, hospitals, universities, the abolition of slavery, and the modern concept of human rights, while also being invoked to justify crusades, inquisitions, and colonialism."
            ),
            "causes": [
                "Roman occupation of Judea generating messianic expectation among Jewish people",
                "John the Baptist's apocalyptic preaching creating the spiritual context for Jesus's ministry",
                "Jewish prophetic tradition providing the framework for his teachings on justice and mercy",
                "Roman crucifixion as political execution — the specific manner of death shaping resurrection theology",
            ],
            "effects": [
                "Christianity — world's largest religion, 2.4 billion adherents",
                "New Testament — core Christian scripture shaping Western literature and ethics",
                "Roman Empire's Christianization under Constantine (313 CE)",
                "Western calendar — Anno Domini dating system from his birth",
                "Christian monastic tradition — hospitals, universities, libraries",
                "Crusades, Inquisition, Protestant Reformation — all responding to his teachings",
                "Modern concepts of human rights, dignity, and universal brotherhood",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Paul the Apostle", "targetSlug": "paul-the-apostle", "note": "Paul's encounter with risen Christ transformed Jesus's movement to universal religion"},
                {"type": "INFLUENCES", "target": "Christianity", "targetSlug": "christianity", "note": "He is the founder — the religion is entirely centered on his person"},
                {"type": "INFLUENCES", "target": "New Testament", "targetSlug": "new-testament", "note": "Primary textual record of his life and teachings"},
                {"type": "INFLUENCES", "target": "Roman Empire", "targetSlug": "roman-empire", "note": "Empire that executed him and then adopted his religion"},
                {"type": "INFLUENCES", "target": "Constantine I", "targetSlug": "constantine-i", "note": "Made Christianity Rome's official religion (313 CE)"},
                {"type": "INFLUENCES", "target": "John the Baptist", "targetSlug": "john-the-baptist", "note": "Precursor who baptized Jesus and announced his coming"},
                {"type": "INFLUENCES", "target": "Pontius Pilate", "targetSlug": "pontius-pilate", "note": "Roman prefect who ordered his crucifixion"},
                {"type": "INFLUENCES", "target": "Islam", "targetSlug": "islam", "note": "Quran recognizes Jesus as a prophet (Isa)"},
                {"type": "INFLUENCES", "target": "The Sermon on the Mount", "targetSlug": "sermon-on-the-mount", "note": "Core ethical teaching: Beatitudes, Lord's Prayer, love of enemies"},
                {"type": "OCCURS_IN", "target": "Israel/Palestine", "targetSlug": "israel-palestine", "note": "Born in Bethlehem, ministry in Galilee, crucified in Jerusalem"},
                {"type": "INFLUENCES", "target": "Martin Luther", "targetSlug": "martin-luther", "note": "Luther's Protestant Reformation was a dispute about authentic Christianity"},
                {"type": "INFLUENCES", "target": "Francis of Assisi", "targetSlug": "francis-of-assisi", "note": "Francis took his poverty and love teachings to radical conclusion"},
                {"type": "INFLUENCES", "target": "Thomas Aquinas", "targetSlug": "thomas-aquinas", "note": "Scholastic theology synthesizing Aristotle with Christ's teachings"},
                {"type": "INFLUENCES", "target": "Western calendar", "targetSlug": "gregorian-calendar", "note": "Years counted from his birth (BC/AD or BCE/CE)"},
                {"type": "INFLUENCES", "target": "Crusades", "targetSlug": "crusades", "note": "Medieval military campaigns launched in his name"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Jesus of Nazareth is the most influential single human being in recorded history — the founder of the world's largest religion (2.4 billion adherents), the subject of more scholarship than any other person, the basis of the Western calendar, and the inspiration for both the highest human achievements and the worst religious atrocities across two millennia."
            },
            "quote": "'Love your neighbor as yourself.' (Matthew 22:39)",
            "places": ["Jerusalem, Israel (ministry and death)", "Nazareth, Galilee (upbringing)", "Bethlehem, Judea (birth)", "Capernaum (ministry base)"],
            "subjectHeadings": "Jesus Christ — Religious Founders — Israel/Palestine — Classical",
            "subjects": ["Israel", "Christianity", "religion", "Classical era", "Roman Empire", "theology", "ethics", "Judaism", "spirituality", "Western civilization"],
            "frameworks": ["religious-thought", "liberation-theology", "social-revolution"],
        }
    },

    # ── 2. Martin Luther ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201martin-luther.json",
        "slug": "martin-luther",
        "era_correction": None,
        "data": {
            "summary": (
                "Martin Luther (1483–1546) was the German Augustinian friar and theologian whose Ninety-Five Theses (October 31, 1517) — a scholarly challenge to the sale of indulgences — ignited the Protestant Reformation, permanently fracturing Western Christianity and reshaping the political, cultural, and intellectual landscape of Europe. No single act of scholarship has had more geopolitical consequences: Luther's challenge led to a century of religious wars, created the foundations of the modern nation-state, and enabled both the Scientific Revolution and the Enlightenment by breaking the Catholic Church's monopoly on legitimate knowledge.\n\n"
                "Luther's core theological insight — justification by faith alone (sola fide), not works or sacraments — challenged 1,000 years of Catholic doctrine. When ordered to recant at the Diet of Worms (1521), he refused: 'Here I stand. I can do no other.' Excommunicated by Pope Leo X and declared an outlaw by Holy Roman Emperor Charles V, he translated the New Testament into German while hiding at Wartburg Castle — creating the standard for the modern German language as Shakespeare did for English.\n\n"
                "The printing press (Gutenberg's invention, 60 years earlier) was essential: Luther's pamphlets spread across Europe in weeks, with 300,000 copies sold in three years. The Peasants' Revolt (1524–25) revealed the social radicalism Luther had unleashed — which he violently disowned, urging princes to crush the peasants. His antisemitic writings (especially 'On the Jews and Their Lies', 1543) would later be invoked by Nazis.\n\n"
                "Luther established the first Protestant church (Lutheran), the concept of pastoral marriage and family life for clergy, vernacular Scripture for ordinary believers, and the model of conscience as the ultimate religious authority — principles that remain central to Protestant identity today."
            ),
            "causes": [
                "Catholic Church's sale of indulgences to fund St. Peter's Basilica sparking his protest",
                "Printing press enabling rapid spread of his ideas beyond Church censorship",
                "Renaissance humanism (Erasmus, ad fontes) preparing scholars for direct biblical engagement",
                "German nationalist sentiment against papal extraction of funds from German territories",
            ],
            "effects": [
                "Protestant Reformation — Christianity permanently divided into Catholic and Protestant branches",
                "Ninety-Five Theses (1517) — most consequential academic document in Western history",
                "German Bible translation (1534) — standard for modern German language",
                "Wars of Religion (1524–1648) — century of conflict culminating in Peace of Westphalia",
                "Sola fide, sola scriptura — Protestant theological principles still active today",
                "Secularization and rise of nation-state from religious wars",
                "Lutheran Church — 80 million members globally",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Protestant Reformation", "targetSlug": "protestant-reformation", "note": "He IS the Reformation — his 1517 protest started it"},
                {"type": "INFLUENCES", "target": "Johannes Gutenberg", "targetSlug": "johannes-gutenberg", "note": "Printing press made Luther's ideas unstoppable"},
                {"type": "INFLUENCES", "target": "John Calvin", "targetSlug": "john-calvin", "note": "Calvin built a more systematic Protestant theology on Luther's foundation"},
                {"type": "INFLUENCES", "target": "Jesus Christ", "targetSlug": "jesus-christ", "note": "Luther's theology was about authentic Christianity — faith alone"},
                {"type": "INFLUENCES", "target": "Pope Leo X", "targetSlug": "pope-leo-x", "note": "Excommunicated Luther with Exsurge Domine (1520)"},
                {"type": "INFLUENCES", "target": "Charles V, Holy Roman Emperor", "targetSlug": "charles-v-holy-roman-emperor", "note": "Declared Luther an outlaw at Diet of Worms (1521)"},
                {"type": "INFLUENCES", "target": "Philip Melanchthon", "targetSlug": "philip-melanchthon", "note": "Closest theological collaborator; wrote Augsburg Confession (1530)"},
                {"type": "INFLUENCES", "target": "Peasants' Revolt (1524–25)", "targetSlug": "peasants-revolt-1524", "note": "Radical social uprising Luther unleashed — then denounced"},
                {"type": "INFLUENCES", "target": "Ninety-Five Theses", "targetSlug": "ninety-five-theses", "note": "His 1517 challenge to indulgences — Reformation's founding document"},
                {"type": "OCCURS_IN", "target": "Germany", "targetSlug": "germany", "note": "German-born; Wittenberg University professor"},
                {"type": "INFLUENCES", "target": "Peace of Westphalia", "targetSlug": "peace-of-westphalia", "note": "1648 settlement of religious wars he started — modern state system"},
                {"type": "INFLUENCES", "target": "Henry VIII of England", "targetSlug": "henry-viii-of-england", "note": "Luther's challenge inspired Henry's break with Rome"},
                {"type": "INFLUENCES", "target": "Erasmus", "targetSlug": "erasmus", "note": "Renaissance humanist ally turned critic — their debate on free will"},
                {"type": "INFLUENCES", "target": "Council of Trent", "targetSlug": "council-of-trent", "note": "Catholic Counter-Reformation response to Lutheran challenge"},
                {"type": "INFLUENCES", "target": "Thirty Years War", "targetSlug": "thirty-years-war", "note": "1618–48 catastrophic war rooted in Lutheran-Catholic conflict"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Martin Luther's Ninety-Five Theses broke the Catholic Church's monopoly on spiritual authority, permanently divided Western Christianity, triggered a century of wars, produced the modern German language, and established the principle of individual conscience over institutional authority — making him the father of both Protestantism and modern Western individualism."
            },
            "quote": "'Here I stand. I can do no other. So help me God.' — Martin Luther, Diet of Worms (April 18, 1521)",
            "places": ["Wittenberg, Germany (university and Reformation center)", "Eisleben, Germany (birthplace and death)", "Wartburg Castle, Germany (hiding, German Bible translation)"],
            "subjectHeadings": "Martin Luther — Religious Reformers — Germany — Early Modern",
            "subjects": ["Germany", "Protestant Reformation", "Christianity", "theology", "Early Modern era", "printing press", "church history", "Europe", "religious freedom", "Bible translation"],
            "frameworks": ["religious-thought", "social-revolution", "state-formation"],
        }
    },

    # ── 3. Thomas Aquinas ────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201thomas-aquinas.json",
        "slug": "thomas-aquinas",
        "era_correction": None,
        "data": {
            "summary": (
                "Thomas Aquinas (1225–1274) was an Italian Dominican friar, priest, and philosopher-theologian whose monumental Summa Theologica (begun 1265) synthesized Aristotelian philosophy with Christian theology to create Thomism — the intellectual foundation of Catholic doctrine from the Council of Trent to the present day. Called the 'Angelic Doctor,' he is regarded as the Catholic Church's greatest thinker; Pope Leo XIII mandated Thomism as the basis of Catholic philosophy in 1879, and it remains so.\n\n"
                "Aquinas's great achievement was arguing that reason and faith are not opposed but complementary — that Aristotle's logic could be used to explore and defend Christian theology. His Five Ways (Quinque Viae) — proofs for God's existence — remain the most systematically developed natural theology in Western philosophy. He distinguished between natural law (accessible to human reason) and divine law (revealed through Scripture), a distinction that became the foundation of natural rights theory.\n\n"
                "His intellectual career ranged from Paris to Naples to Rome. At Paris he defeated Averroism — the Arabic Aristotelian tradition — in public debate. His prolific output (8 million words) included commentaries on Aristotle, Peter Lombard's Sentences, Scripture, and the Summa Theologica. He reportedly stopped writing weeks before his death, saying everything he had written 'seems like straw' compared to what he had experienced in mystical vision.\n\n"
                "Aquinas's natural law theory — that moral laws are discoverable by reason and grounded in human nature — underpins the modern Catholic teaching on human rights, just war, and social ethics, and influenced secular rights theorists from Grotius to John Locke."
            ),
            "causes": [
                "Recovery of Aristotle's texts via Arabic translation (Al-Farabi, Averroes) into medieval Europe",
                "Tension between faith and reason in medieval universities requiring a systematic synthesis",
                "Dominican Order's intellectual mission equipping Aquinas with rigorous training",
                "Albert the Great's mentorship introducing him to Aristotelian natural philosophy",
            ],
            "effects": [
                "Summa Theologica — greatest systematic theology in Christian history",
                "Thomism — Catholic Church's official philosophical tradition",
                "Natural law theory — foundational for human rights discourse",
                "Five Ways — most influential philosophical arguments for God's existence",
                "Integration of Aristotle into Christian theology — saved Greek rational tradition in Europe",
                "Council of Trent (1545) enshrining Aquinas alongside the Bible",
                "Modern Catholic social teaching on labor rights, just war, human dignity",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Aristotle", "targetSlug": "aristotle", "note": "Synthesized Aristotelian philosophy with Christian theology"},
                {"type": "INFLUENCES", "target": "Summa Theologica", "targetSlug": "summa-theologica", "note": "His masterwork — systematic theology of 3,000+ articles"},
                {"type": "INFLUENCES", "target": "Albert the Great", "targetSlug": "albert-the-great", "note": "Mentor who introduced him to Aristotle's works"},
                {"type": "INFLUENCES", "target": "Jesus Christ", "targetSlug": "jesus-christ", "note": "His theology was an attempt to rationally expound Christian revelation"},
                {"type": "INFLUENCES", "target": "Averroes", "targetSlug": "averroes", "note": "Arabic Aristotelian whose interpretation Aquinas contested in Paris"},
                {"type": "INFLUENCES", "target": "Natural law theory", "targetSlug": "natural-law", "note": "His development of natural law grounded modern rights theory"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Natural rights theory inherited Aquinas's natural law framework"},
                {"type": "INFLUENCES", "target": "Hugo Grotius", "targetSlug": "hugo-grotius", "note": "Father of international law who built on Thomist natural law"},
                {"type": "INFLUENCES", "target": "Council of Trent", "targetSlug": "council-of-trent", "note": "Summa Theologica placed on the altar alongside Bible at Trent"},
                {"type": "OCCURS_IN", "target": "Italy", "targetSlug": "italy", "note": "Born in Roccasecca; taught at Naples and Rome"},
                {"type": "INFLUENCES", "target": "Paris, University of", "targetSlug": "university-of-paris", "note": "Taught at Paris — center of medieval intellectual life"},
                {"type": "INFLUENCES", "target": "Dominican Order", "targetSlug": "dominican-order", "note": "His religious order — committed to preaching and scholarship"},
                {"type": "INFLUENCES", "target": "Martin Luther", "targetSlug": "martin-luther", "note": "Luther rejected Scholasticism; Protestant Reformation partly a rejection of Thomism"},
                {"type": "INFLUENCES", "target": "Pope Leo XIII", "targetSlug": "pope-leo-xiii", "note": "1879 encyclical Aeterni Patris made Thomism official Catholic philosophy"},
                {"type": "INFLUENCES", "target": "René Descartes", "targetSlug": "rene-descartes", "note": "Descartes's rationalism was partly a break from Scholastic Aristotelianism"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Thomas Aquinas's synthesis of Aristotle and Christianity in the Summa Theologica became the intellectual foundation of Catholic doctrine, preserved Greek rational philosophy in the West, created natural law theory that underpins modern human rights, and remains the Catholic Church's official philosophical tradition 750 years after his death."
            },
            "quote": "'To one who has faith, no explanation is necessary. To one without faith, no explanation is possible.' — attributed to Thomas Aquinas",
            "places": ["Roccasecca, Italy (birthplace)", "Paris, France (teaching)", "Naples, Italy (teaching)", "Fossanova Abbey, Italy (death)"],
            "subjectHeadings": "Thomas Aquinas — Theologians and Philosophers — Italy — Medieval",
            "subjects": ["Italy", "theology", "philosophy", "Christianity", "Medieval era", "natural law", "Aristotle", "Dominican Order", "scholasticism", "human rights"],
            "frameworks": ["religious-thought", "political-philosophy", "intellectual-history"],
        }
    },

    # ── 4. René Descartes ────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210rene-descartes.json",
        "slug": "rene-descartes",
        "era_correction": None,
        "data": {
            "summary": (
                "René Descartes (1596–1650) was a French philosopher, mathematician, and scientist who founded modern Western philosophy with a single act of radical doubt: stripping away every belief that could be questioned, he arrived at the bedrock certainty 'Cogito, ergo sum' (I think, therefore I am). His Meditations on First Philosophy (1641) established the mind-body problem, rationalism, and systematic scepticism as philosophy's central concerns — concerns still debated today. He is rightly called the 'Father of Modern Philosophy.'\n\n"
                "Descartes's method was revolutionary: start from absolute doubt, accept nothing that can be questioned, and rebuild knowledge from self-evident principles. From the Cogito, he inferred the existence of God, the external world, and the reliability of clear and distinct ideas — a rationalist programme that influenced Spinoza, Leibniz, and Kant. His Cartesian coordinate system (x,y axes on a grid) — invented to describe where a fly was on his ceiling — united algebra and geometry into analytic geometry, enabling Newton's calculus.\n\n"
                "He spent most of his adult life in the Dutch Republic (Netherlands), choosing it for intellectual freedom. His Discourse on Method (1637) was the first major philosophical work published in French rather than Latin — democratizing philosophical discourse. He died in Stockholm in February 1650, having moved to Sweden to tutor Queen Christina, reportedly succumbing to pneumonia from the early morning lectures she demanded.\n\n"
                "Descartes's dualism — mind (res cogitans) and body (res extensa) as fundamentally different substances — created the 'hard problem of consciousness' still unresolved in philosophy and neuroscience. His mechanistic physics was superseded by Newton, but his metaphysical legacy endures in every introductory philosophy course."
            ),
            "causes": [
                "Scholastic philosophy's crisis of authority following Reformation and Scientific Revolution",
                "Mathematical certainty (geometry) as a model for philosophical knowledge",
                "Religious conflict in Europe motivating a search for neutral, universal truths",
                "Galileo's condemnation (1633) prompting Descartes to suppress his cosmology",
            ],
            "effects": [
                "Cogito ergo sum — philosophy's most famous proposition",
                "Mind-body dualism — created the 'hard problem of consciousness'",
                "Analytic geometry — Cartesian coordinates uniting algebra and geometry",
                "Rationalist tradition: Spinoza, Leibniz — 17th-century continental philosophy",
                "Meditations on First Philosophy — foundational text of modern epistemology",
                "Discourse on Method — first philosophical work in French, democratizing discourse",
                "Modern scientific methodology: systematic doubt, hypothesis testing",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Baruch Spinoza", "targetSlug": "baruch-spinoza", "note": "Spinoza's rationalism built on Cartesian method"},
                {"type": "INFLUENCES", "target": "Gottfried Wilhelm Leibniz", "targetSlug": "gottfried-wilhelm-leibniz", "note": "Leibniz extended Cartesian rationalism"},
                {"type": "INFLUENCES", "target": "Immanuel Kant", "targetSlug": "immanuel-kant", "note": "Kant's critical philosophy responded to Descartes and Hume"},
                {"type": "INFLUENCES", "target": "Isaac Newton", "targetSlug": "isaac-newton", "note": "Newton's calculus built on Cartesian analytic geometry"},
                {"type": "INFLUENCES", "target": "Meditations on First Philosophy", "targetSlug": "meditations-on-first-philosophy", "note": "1641 masterwork establishing modern epistemology"},
                {"type": "INFLUENCES", "target": "Discourse on Method", "targetSlug": "discourse-on-the-method", "note": "1637 work introducing Cogito and scientific method"},
                {"type": "INFLUENCES", "target": "Queen Christina of Sweden", "targetSlug": "queen-christina-of-sweden", "note": "Invited him to Stockholm — he died there 1650"},
                {"type": "INFLUENCES", "target": "Galileo Galilei", "targetSlug": "galileo-galilei", "note": "Galileo's condemnation made Descartes suppress his heliocentrism"},
                {"type": "INFLUENCES", "target": "Thomas Aquinas", "targetSlug": "thomas-aquinas", "note": "Descartes rejected Scholastic Aristotelianism, beginning modern philosophy"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Born in La Haye en Touraine (now Descartes)"},
                {"type": "OCCURS_IN", "target": "Netherlands", "targetSlug": "netherlands", "note": "Lived in Dutch Republic for 20 years — intellectual refuge"},
                {"type": "INFLUENCES", "target": "Analytic geometry", "targetSlug": "analytic-geometry", "note": "Cartesian coordinate system — foundation of modern mathematics"},
                {"type": "INFLUENCES", "target": "David Hume", "targetSlug": "david-hume", "note": "Hume's empiricism was a direct challenge to Cartesian rationalism"},
                {"type": "INFLUENCES", "target": "Mind-body problem", "targetSlug": "mind-body-problem", "note": "His dualism created the philosophical problem of consciousness"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Locke's empiricism challenged Cartesian innate ideas"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "René Descartes founded modern Western philosophy with the Cogito, established rationalism as a systematic programme, invented analytic geometry that enabled Newton's calculus, and created the mind-body problem — the deepest philosophical puzzle still unresolved in neuroscience — making him the philosopher who most directly shaped the intellectual DNA of modern Western thought."
            },
            "quote": "'Cogito, ergo sum.' (I think, therefore I am.) — René Descartes, Discourse on Method (1637)",
            "places": ["La Haye en Touraine, France (birthplace)", "Amsterdam, Netherlands (residence)", "Stockholm, Sweden (death)", "Paris, France (education)"],
            "subjectHeadings": "René Descartes — Philosophers and Mathematicians — France — Early Modern",
            "subjects": ["France", "philosophy", "mathematics", "rationalism", "Early Modern era", "mind-body problem", "analytic geometry", "epistemology", "scientific revolution", "Netherlands"],
            "frameworks": ["scientific-revolution", "intellectual-history", "political-philosophy"],
        }
    },

    # ── 5. Sigmund Freud ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210sigmund-freud.json",
        "slug": "sigmund-freud",
        "era_correction": None,
        "data": {
            "summary": (
                "Sigmund Freud (1856–1939) was an Austrian neurologist who founded psychoanalysis — a theory of the mind and a clinical method that revolutionized how Western civilization understands human motivation, sexuality, childhood, dreams, and unconscious thought. His central proposition — that much of mental life occurs in an unconscious region inaccessible to ordinary introspection, shaped by early childhood experience and repressed sexuality — was so controversial that it was rejected by mainstream medicine for decades, yet so culturally compelling that it transformed literature, art, film, anthropology, and popular psychology.\n\n"
                "Freud's key innovations: the unconscious as the site of repressed wishes; the Oedipus complex (children's sexual desire for the opposite-sex parent and rivalry with the same-sex parent); dream analysis as the 'royal road to the unconscious'; the tripartite model of the psyche (id, ego, superego); and the 'talking cure' — free association as a therapeutic method. The Interpretation of Dreams (1899), which he considered his greatest work, transformed the study of mental life.\n\n"
                "In 1938, at age 82, he fled Nazi-occupied Vienna with his daughter Anna (herself an important psychoanalyst) to London, where he died of oral cancer in September 1939. His personal library and collection of antiquities are preserved at the Freud Museum in London.\n\n"
                "Most of Freud's specific theories — the Oedipus complex, penis envy, libido theory — have been substantially revised or rejected by modern neuroscience and psychology. Yet the very vocabulary he created (unconscious, repression, Freudian slip, ego, id, complex, libido) entered everyday language, and the idea that we are not entirely transparent to ourselves remains one of the most important contributions to human self-understanding."
            ),
            "causes": [
                "Neurological medicine's limits in treating hysteria prompting new psychological theories",
                "Josef Breuer's cathartic method providing the clinical foundation for psychoanalysis",
                "Victorian sexuality's repression creating the social context for his sexual theories",
                "Jean-Martin Charcot's work on hypnosis and hysteria at Paris inspiring his approach",
            ],
            "effects": [
                "Psychoanalysis — influential theory of mind and clinical method",
                "The Interpretation of Dreams (1899) — founding text of psychoanalysis",
                "Unconscious/ego/id/superego — vocabulary entering all of psychology and culture",
                "Talking cure — foundational for all modern psychotherapy",
                "Surrealism, modernist literature, film theory — influenced by Freudian ideas",
                "Psychological understanding of childhood development",
                "Modern psychology's development partly as a response to revise and correct Freud",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Carl Jung", "targetSlug": "carl-jung", "note": "Collaborator who split to develop analytical psychology (1912)"},
                {"type": "INFLUENCES", "target": "Anna Freud", "targetSlug": "anna-freud", "note": "Daughter and close collaborator; pioneer of child psychoanalysis"},
                {"type": "INFLUENCES", "target": "Josef Breuer", "targetSlug": "josef-breuer", "note": "Clinical mentor whose cathartic method inspired psychoanalysis"},
                {"type": "INFLUENCES", "target": "The Interpretation of Dreams", "targetSlug": "interpretation-of-dreams-freud", "note": "His 1899 masterwork — psychoanalysis's founding text"},
                {"type": "INFLUENCES", "target": "Jean-Martin Charcot", "targetSlug": "jean-martin-charcot", "note": "Studied hypnosis and hysteria under Charcot in Paris"},
                {"type": "INFLUENCES", "target": "Alfred Adler", "targetSlug": "alfred-adler", "note": "Early psychoanalyst who broke with Freud over power vs. sex"},
                {"type": "INFLUENCES", "target": "Surrealism", "targetSlug": "surrealism", "note": "André Breton's movement drew directly on Freudian unconscious"},
                {"type": "INFLUENCES", "target": "Modernist literature", "targetSlug": "modernist-literature", "note": "Stream of consciousness and interior monologue shaped by Freud"},
                {"type": "INFLUENCES", "target": "Nazi Germany", "targetSlug": "nazi-germany", "note": "Fled Vienna in 1938 — Jewish intellectual targeted by antisemitism"},
                {"type": "OCCURS_IN", "target": "Austria", "targetSlug": "austria", "note": "Lived and worked in Vienna for most of his life"},
                {"type": "INFLUENCES", "target": "Jacques Lacan", "targetSlug": "jacques-lacan", "note": "French psychoanalyst who re-read Freud through linguistics"},
                {"type": "INFLUENCES", "target": "Modern psychology", "targetSlug": "psychology", "note": "Modern psychology developed partly by criticizing and revising Freud"},
                {"type": "INFLUENCES", "target": "Gender studies", "targetSlug": "gender-studies", "note": "His theories about women were widely critiqued by feminist scholars"},
                {"type": "INFLUENCES", "target": "Karl Marx", "targetSlug": "karl-marx", "note": "Both 19th-c. theorists whose influence shaped 20th-c. thought"},
                {"type": "INFLUENCES", "target": "Friedrich Nietzsche", "targetSlug": "friedrich-nietzsche", "note": "Both mapped depths of human irrationality and will"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Sigmund Freud created the vocabulary of the modern mind — unconscious, repression, ego, id, libido — that transformed how humanity understands itself, invented psychotherapy as a practice, shaped modernist art and literature, and established the principle that we are not transparent to ourselves: perhaps the most unsettling and consequential idea of the 20th century."
            },
            "quote": "'The unconscious is the true psychical reality; in its innermost nature it is as much unknown to us as the reality of the external world.' — Sigmund Freud, The Interpretation of Dreams (1899)",
            "places": ["Vienna, Austria (life and work)", "Freiberg, Moravia (birthplace)", "Paris, France (study with Charcot)", "London, England (death, 1939)"],
            "subjectHeadings": "Sigmund Freud — Psychologists and Scientists — Austria — Modern",
            "subjects": ["Austria", "psychology", "psychoanalysis", "medicine", "Modern era", "unconscious", "sexuality", "Vienna", "20th century", "Europe"],
            "frameworks": ["scientific-revolution", "social-theory", "intellectual-history"],
        }
    },

    # ── 6. Hippocrates ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210hippocrates.json",
        "slug": "hippocrates",
        "era_correction": None,
        "data": {
            "summary": (
                "Hippocrates of Cos (c. 460–370 BCE) was a Greek physician from the island of Cos who is called the 'Father of Medicine' for establishing medicine as a rational, empirical discipline — systematically separating it from supernatural explanations and religious practice. His fundamental insight — that diseases have natural causes observable in the body and environment, not the wrath of gods — was so radical that it took nearly 2,000 years to fully take hold. The Hippocratic Oath, taken by physicians for 2,500 years, remains the foundational ethical statement of medical practice.\n\n"
                "Hippocrates taught at the school of Cos and trained physicians in careful clinical observation: noting symptoms, recording case histories, observing the course of disease over time, and making prognoses based on pattern recognition. His Corpus Hippocraticum (c. 60 texts, though most written by disciples) includes descriptions of diseases, clinical reports, surgical techniques, and ethical guidelines. His theory of the four humors (blood, phlegm, yellow bile, black bile) was medically incorrect but scientifically important as a naturalistic framework that endured through Galen to the Renaissance.\n\n"
                "His principle 'First, do no harm' (Primum non nocere, though this phrase may be later) established a foundational medical ethic. His clinical descriptions of epilepsy (arguing it was a brain disease, not sacred possession), clubfoot, mumps, and certain cancers were accurate observations that anticipated later medical understanding.\n\n"
                "Hippocrates's legacy is not any specific medical knowledge (much was wrong) but a method: observe, record, reason from evidence, make probabilistic prognoses, and treat the patient with care for their dignity. This empirical-ethical method is the foundation all modern medicine builds on."
            ),
            "causes": [
                "Greek natural philosophy (pre-Socratic) seeking natural explanations for all phenomena",
                "Temple healing traditions in competition with rational medicine creating reform space",
                "Cos island's medical school providing institutional support for systematic observation",
                "Sufficiency of clinical observation to demonstrate natural disease causation",
            ],
            "effects": [
                "Hippocratic Oath — medical ethics observed for 2,500 years",
                "Medicine as rational, empirical practice separated from religion",
                "Corpus Hippocraticum — 60+ texts founding Western medical literature",
                "Four humors theory — dominant medical paradigm for 2,000 years",
                "Clinical observation method — foundation of all modern diagnosis",
                "Galen built on Hippocratic foundations to synthesize Greek medicine",
                "'First, do no harm' — most influential principle in medical ethics",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Galen", "targetSlug": "galen", "note": "Galen systematized Hippocratic medicine and extended it for 1,500 years"},
                {"type": "INFLUENCES", "target": "Avicenna", "targetSlug": "avicenna", "note": "Islamic synthesis of Hippocratic and Galenic medicine in Canon of Medicine"},
                {"type": "INFLUENCES", "target": "Corpus Hippocraticum", "targetSlug": "corpus-hippocraticum", "note": "60+ medical texts attributed to him and his school"},
                {"type": "INFLUENCES", "target": "Hippocratic Oath", "targetSlug": "hippocratic-oath", "note": "Medical ethics oath observed continuously for 2,500 years"},
                {"type": "INFLUENCES", "target": "Aristotle", "targetSlug": "aristotle", "note": "Aristotle's empirical biology built on Hippocratic observation methodology"},
                {"type": "INFLUENCES", "target": "Andreas Vesalius", "targetSlug": "andreas-vesalius", "note": "16th-century anatomist who corrected Galenic errors — working within Hippocratic tradition"},
                {"type": "INFLUENCES", "target": "Florence Nightingale", "targetSlug": "florence-nightingale", "note": "Her statistical nursing reforms operated within the empirical tradition Hippocrates began"},
                {"type": "INFLUENCES", "target": "William Harvey", "targetSlug": "william-harvey", "note": "Discovery of blood circulation continued Hippocratic empirical tradition"},
                {"type": "OCCURS_IN", "target": "Greece", "targetSlug": "greece", "note": "Born on Cos; traveled throughout Greek world"},
                {"type": "INFLUENCES", "target": "Four humors", "targetSlug": "humoral-theory", "note": "Naturalistic framework that structured medicine for 2,000 years"},
                {"type": "INFLUENCES", "target": "Asclepius", "targetSlug": "asclepius", "note": "Divine healer whose temple medicine Hippocrates's school competed with"},
                {"type": "INFLUENCES", "target": "Ancient Greek philosophy", "targetSlug": "ancient-greek-philosophy", "note": "Greek natural philosophy provided framework for empirical medicine"},
                {"type": "INFLUENCES", "target": "Louis Pasteur", "targetSlug": "louis-pasteur", "note": "Germ theory eventually confirmed Hippocratic hunch about environmental disease causation"},
                {"type": "INFLUENCES", "target": "Medical ethics", "targetSlug": "medical-ethics", "note": "Hippocratic tradition is the foundation of all bioethical discourse"},
                {"type": "INFLUENCES", "target": "Plato", "targetSlug": "plato", "note": "Plato cited Hippocrates as the model of medical science in Phaedrus"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Hippocrates separated medicine from religion, established clinical observation as the basis of diagnosis and treatment, formulated the ethical framework of the Hippocratic Oath still used 2,500 years later, and made the foundational claim that diseases have natural, not supernatural, causes — making him the architect of scientific medicine."
            },
            "quote": "'Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult.' — Hippocrates, Aphorisms (first aphorism)",
            "places": ["Cos, Greece (birthplace and school)", "Larissa, Thessaly, Greece (death)", "Athens, Greece (visited)"],
            "subjectHeadings": "Hippocrates — Physicians and Scientists — Greece — Classical",
            "subjects": ["Greece", "medicine", "Classical era", "medical ethics", "science", "ancient world", "philosophy", "Hippocratic Oath", "empiricism", "healing"],
            "frameworks": ["scientific-revolution", "intellectual-history", "cultural-exchange"],
        }
    },

    # ── 7. Gottfried Wilhelm Leibniz ─────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210gottfried-wilhelm-leibniz.json",
        "slug": "gottfried-wilhelm-leibniz",
        "era_correction": None,
        "data": {
            "summary": (
                "Gottfried Wilhelm Leibniz (1646–1716) was a German polymath who independently invented calculus simultaneously with Isaac Newton, developed the binary number system that underlies all digital computing, and created a comprehensive philosophical system (monadology) exploring the nature of reality, space, time, and God. Known as the 'last universal genius' alongside Leonardo da Vinci, Leibniz made foundational contributions to mathematics, philosophy, physics, logic, history, diplomacy, and linguistics — never once holding a university position.\n\n"
                "His calculus (independently published 1684, several years before Newton's 1687 Principia, though Newton had privately worked it out years earlier) used the notation d/dx and the integral sign ∫ that every calculus student still uses today. The bitter priority dispute with Newton poisoned relations between British and Continental mathematicians for a century. Leibniz's notation won: the entire world uses it.\n\n"
                "His binary arithmetic (0s and 1s) — which he connected to Chinese hexagrams and I Ching symbolism — became the mathematical foundation of all digital computation 200 years later. His Monadology (1714) proposed that reality consists of simple, irreducible 'monads' — a metaphysical theory whose influence stretched from Kant to Whitehead. His famous theodicy — that we live in 'the best of all possible worlds' — was memorably satirized by Voltaire in Candide.\n\n"
                "Leibniz spent decades in Hanover as a court librarian and diplomat; his work on a universal characteristic (a logical calculus for all reasoning) directly anticipates Boole's algebra and Frege's predicate logic — the foundations of modern computer science."
            ),
            "causes": [
                "17th-century need for mathematical tools to solve problems of motion and area",
                "Cartesian rationalism providing framework for his philosophical ambitions",
                "Leibniz's extraordinary breadth of curiosity spanning all intellectual disciplines",
                "Hanover court employment giving financial security but limiting scientific community",
            ],
            "effects": [
                "Calculus notation (d/dx, ∫) — used universally in mathematics",
                "Binary number system — foundation of all digital computing",
                "Monadology — metaphysical system influencing Kant and process philosophy",
                "Theodicy — concept of 'best of all possible worlds' (and Voltaire's satire)",
                "Universal characteristic — anticipating Boolean logic and computer science",
                "Newton-Leibniz calculus priority dispute — lasting damage to British-Continental relations",
                "Diplomatic career — early advocate of European unity",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Isaac Newton", "targetSlug": "isaac-newton", "note": "Simultaneous independent calculus — bitter priority dispute followed"},
                {"type": "INFLUENCES", "target": "René Descartes", "targetSlug": "rene-descartes", "note": "Extended Cartesian rationalism into his own metaphysics"},
                {"type": "INFLUENCES", "target": "Immanuel Kant", "targetSlug": "immanuel-kant", "note": "Kant's critical philosophy responded directly to Leibniz and Newton"},
                {"type": "INFLUENCES", "target": "George Boole", "targetSlug": "george-boole", "note": "Leibniz's binary and logical calculus ideas anticipated Boolean algebra"},
                {"type": "INFLUENCES", "target": "Gottlob Frege", "targetSlug": "gottlob-frege", "note": "Frege's predicate logic realized Leibniz's universal characteristic"},
                {"type": "INFLUENCES", "target": "Voltaire", "targetSlug": "voltaire", "note": "Voltaire's Candide satirized Leibniz's optimism ('best of all possible worlds')"},
                {"type": "INFLUENCES", "target": "Binary number system", "targetSlug": "binary-number-system", "note": "Leibniz's invention — foundation of all digital computing"},
                {"type": "INFLUENCES", "target": "Monadology", "targetSlug": "monadology-leibniz", "note": "His 1714 metaphysical treatise proposing reality consists of monads"},
                {"type": "INFLUENCES", "target": "Royal Society", "targetSlug": "royal-society", "note": "Fellow of the Royal Society; center of Newton priority dispute"},
                {"type": "OCCURS_IN", "target": "Germany", "targetSlug": "germany", "note": "Spent most of career in Hanover as court librarian"},
                {"type": "INFLUENCES", "target": "Baruch Spinoza", "targetSlug": "baruch-spinoza", "note": "Met Spinoza; their metaphysics diverged sharply"},
                {"type": "INFLUENCES", "target": "Digital computing", "targetSlug": "digital-computing", "note": "Binary system directly underlies all modern computing"},
                {"type": "INFLUENCES", "target": "Alfred North Whitehead", "targetSlug": "alfred-north-whitehead", "note": "Process philosophy extends monadological ideas"},
                {"type": "INFLUENCES", "target": "I Ching", "targetSlug": "i-ching", "note": "Connected binary arithmetic to Chinese hexagram symbolism"},
                {"type": "INFLUENCES", "target": "Bertrand Russell", "targetSlug": "bertrand-russell", "note": "Russell's early work on Leibniz (1900) revived his philosophical reputation"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Gottfried Leibniz independently invented calculus (with notation still used globally), created the binary number system foundational to all digital computing, and built a philosophical system whose influence stretched from Kant to modern logic — making him perhaps the most broadly consequential thinker who never received credit commensurate with his contributions."
            },
            "quote": "'Music is the pleasure the human mind experiences from counting without being aware that it is counting.' — Gottfried Wilhelm Leibniz",
            "places": ["Hanover, Germany (court employment)", "Leipzig, Germany (birthplace)", "Berlin, Germany (founded Prussian Academy of Sciences)"],
            "subjectHeadings": "Gottfried Wilhelm Leibniz — Mathematicians and Philosophers — Germany — Early Modern",
            "subjects": ["Germany", "mathematics", "philosophy", "calculus", "binary", "computing", "Early Modern era", "Enlightenment", "rationalism", "logic"],
            "frameworks": ["scientific-revolution", "intellectual-history", "technological-change"],
        }
    },

    # ── 8. Pythagoras ────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210pythagoras.json",
        "slug": "pythagoras",
        "era_correction": None,
        "data": {
            "summary": (
                "Pythagoras of Samos (c. 570–495 BCE) was a Greek philosopher and mathematician whose name every schoolchild learns from the theorem bearing it: in a right-angled triangle, the square on the hypotenuse equals the sum of squares on the other two sides (a² + b² = c²). But Pythagoras was far more than a mathematician — he founded a religious-philosophical brotherhood (the Pythagorean school at Croton, Italy) that believed the universe is fundamentally mathematical and that numbers are the key to understanding reality, a conviction that underpins all modern physics.\n\n"
                "The Pythagorean theorem was known in Babylonian and Indian mathematics centuries before Pythagoras, but he or his school is credited with its first deductive proof — the conceptual leap from observed fact to logical demonstration that defines mathematics. His discovery that musical harmonies correspond to simple numerical ratios (the octave = 2:1, fifth = 3:2) was a stunning realization that the sensory world encodes mathematical structure. 'All is number' — his core insight — eventually became the foundation of mathematical physics.\n\n"
                "His community at Croton combined philosophical inquiry with ascetic religious practices: vegetarianism, communal property, metempsychosis (transmigration of souls — possibly influenced by Indian thought), and a semi-secret brotherhood with strict rules. After political conflict, the community was suppressed and Pythagoras fled to Metapontum, where he died.\n\n"
                "The Pythagorean mathematical tradition was transmitted through Plato (especially Timaeus) to the Neoplatonists, medieval astronomers, and Galileo, whose famous 'Book of Nature is written in the language of mathematics' is pure Pythagorean metaphysics — making Pythagoras, 2,500 years later, the patron saint of theoretical physics."
            ),
            "causes": [
                "Ionian natural philosophy (Thales, Anaximander) establishing mathematical cosmology",
                "Babylonian and Egyptian mathematical knowledge accessible to Greek travelers",
                "Musical harmony observation leading to numerical ratios as cosmic principles",
                "Pythagorean brotherhood providing institutional framework for accumulated knowledge",
            ],
            "effects": [
                "Pythagorean theorem — cornerstone of Euclidean geometry and all engineering",
                "'All is number' — the foundational claim of mathematical physics",
                "Musical harmony as numerical ratios — music theory and acoustics",
                "Platonic mathematics: Forms as numbers — via Pythagorean influence",
                "Pythagorean theorem still taught to every student globally",
                "Metempsychosis (soul transmigration) — influenced Plato's immortal soul doctrine",
                "Mathematical description of nature — Galileo, Newton, Einstein all Pythagorean heirs",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Plato", "targetSlug": "plato", "note": "Platonic Forms and mathematical reality deeply Pythagorean"},
                {"type": "INFLUENCES", "target": "Euclid", "targetSlug": "euclid", "note": "Elements systematizes geometry built on Pythagorean foundations"},
                {"type": "INFLUENCES", "target": "Galileo Galilei", "targetSlug": "galileo-galilei", "note": "'Book of Nature written in mathematics' — Pythagorean metaphysics"},
                {"type": "INFLUENCES", "target": "Pythagorean theorem", "targetSlug": "pythagorean-theorem", "note": "a²+b²=c² — foundational to all geometry and engineering"},
                {"type": "INFLUENCES", "target": "Thales of Miletus", "targetSlug": "thales-of-miletus", "note": "Predecessor natural philosopher whose rationalism Pythagoras extended"},
                {"type": "INFLUENCES", "target": "Aristotle", "targetSlug": "aristotle", "note": "Aristotle wrote about Pythagoreans extensively in Metaphysics"},
                {"type": "INFLUENCES", "target": "Neoplatonism", "targetSlug": "neoplatonism", "note": "Pythagorean number mysticism central to Neoplatonic thought"},
                {"type": "INFLUENCES", "target": "Johannes Kepler", "targetSlug": "johannes-kepler", "note": "Kepler's harmonic astronomy ('music of the spheres') directly Pythagorean"},
                {"type": "OCCURS_IN", "target": "Greece", "targetSlug": "greece", "note": "Born Samos; founded school at Croton (Italy)"},
                {"type": "OCCURS_IN", "target": "Italy", "targetSlug": "italy", "note": "Founded philosophical school at Croton (Magna Graecia)"},
                {"type": "INFLUENCES", "target": "Musical harmony", "targetSlug": "music-theory", "note": "Demonstrated that harmonies correspond to simple numerical ratios"},
                {"type": "INFLUENCES", "target": "Isaac Newton", "targetSlug": "isaac-newton", "note": "Mathematical physics is the Pythagorean programme realized"},
                {"type": "INFLUENCES", "target": "Albert Einstein", "targetSlug": "albert-einstein", "note": "Einstein's mathematical physics fulfills Pythagorean vision"},
                {"type": "INFLUENCES", "target": "Archimedes", "targetSlug": "archimedes", "note": "Archimedes' mathematical physics built on Pythagorean-Euclidean tradition"},
                {"type": "INFLUENCES", "target": "Hindu-Arabic numerals", "targetSlug": "hindu-arabic-numerals", "note": "Pythagorean number philosophy created the demand for universal number symbols"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Pythagoras's theorem underpins all geometry and engineering; his claim that 'all is number' is the foundational metaphysics of mathematical physics; his discovery that musical harmony is mathematical ratio connects sensory beauty to abstract structure — making him, 2,500 years later, the patron saint of theoretical physics from Galileo to Einstein."
            },
            "quote": "'Number is the ruler of forms and ideas, and the cause of gods and demons.' — attributed to Pythagoras",
            "places": ["Samos, Greece (birthplace)", "Croton, Italy (philosophical school)", "Metapontum, Italy (death)"],
            "subjectHeadings": "Pythagoras — Mathematicians and Philosophers — Greece — Classical",
            "subjects": ["Greece", "mathematics", "philosophy", "Classical era", "geometry", "ancient world", "music theory", "physics foundations", "Pythagorean theorem", "Italy"],
            "frameworks": ["scientific-revolution", "intellectual-history", "religious-thought"],
        }
    },
]


# ── Core writer ──────────────────────────────────────────────────────────────

def enrich_entity(file_path, slug, data, era_correction, dry_run=False):
    if not os.path.exists(file_path):
        return f"FILE NOT FOUND: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entities = doc.get("entities", [])
    target = next((e for e in entities if e.get("slug") == slug), None)
    if not target:
        return f"SLUG NOT FOUND: {slug} in {file_path}"

    dj = target.get("detailsJson")
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    current_summary = (dj or {}).get("summary", "")
    new_summary = data["summary"]

    if len(current_summary) >= SKIP_THRESHOLD:
        return f"SKIP {slug} (already {len(current_summary)}c)"

    if dry_run:
        return f"→ Enriching {slug}  (was {len(current_summary)}c → {len(new_summary)}c)"

    if "detailsJson" not in target or target["detailsJson"] is None or isinstance(target["detailsJson"], str):
        target["detailsJson"] = {}

    dj = target["detailsJson"]
    now = datetime.now(timezone.utc).isoformat()

    edit_log = dj.get("_editLog", [])
    for field in ["summary", "causes", "effects", "relationships", "historicalSignificance",
                  "quote", "places", "subjectHeadings", "subjects", "frameworks"]:
        if field in data:
            old_val = dj.get(field, None)
            new_val = data[field]
            if old_val != new_val:
                edit_log.append({
                    "field": field,
                    "oldValue": old_val,
                    "newValue": new_val if len(str(new_val)) < 200 else str(new_val)[:200] + "…",
                    "editorId": EDITOR_ID,
                    "sessionId": SESSION_ID,
                    "timestamp": now,
                })

    for field, value in data.items():
        dj[field] = value

    dj["_editLog"] = edit_log

    if era_correction:
        target["era"] = era_correction

    target["_unsyncedEdits"] = True

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    return f"✓ Saved {file_path}"


def main():
    if DRY_RUN:
        print("=== DRY RUN — no files will be written ===\n")

    print(f"Batch 64 enrichment — {len(ENRICHMENTS)} entities\n")

    enriched, skipped, failed = 0, 0, 0
    for item in ENRICHMENTS:
        slug = item["slug"]
        print(f"[{slug}]")
        result = enrich_entity(
            item["file"], slug, item["data"],
            item.get("era_correction"), dry_run=DRY_RUN
        )
        print(f"  {result}")
        if "SKIP" in result:
            skipped += 1
        elif result.startswith("✓") or result.startswith("→"):
            enriched += 1
        else:
            failed += 1

    tag = "DRY RUN" if DRY_RUN else "DONE"
    print(f"\n{tag}: {enriched} enriched, {skipped} skipped, {failed} failed")
    if not DRY_RUN and enriched > 0:
        print("\nNext step: env $(cat .env | xargs) npx tsx scripts/sync_gateway.ts --local")


if __name__ == "__main__":
    main()
