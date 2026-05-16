#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 28 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: a-streetcar-named-desire, catechism-of-the-catholic-church, ethics (Spinoza),
          annals-tacitus, chronicle-of-the-black-death-de-mussis,
          a-tale-of-two-cities, a-study-in-scarlet, a-journey-to-the-centre-of-the-earth
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-28-may2026"

ENRICHMENTS = {

"a-streetcar-named-desire": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780a-streetcar-named-desire.json",
  "slug": "a-streetcar-named-desire",
  "data": {
    "summary": "A Streetcar Named Desire is the play by Tennessee Williams (1911–1983), which premiered on Broadway on 3 December 1947 (directed by Elia Kazan, with Marlon Brando as Stanley Kowalski and Jessica Tandy as Blanche DuBois), won the Pulitzer Prize for Drama in 1948, and has become one of the defining works of American theatrical history — a psychological drama of desire, memory, illusion, and the destruction of a fragile, refined sensibility by a brutal, elemental male force. Its protagonist, Blanche DuBois — an ageing Southern belle fleeing a past of promiscuity, alcoholism, and the loss of her family estate (Belle Reve) — arrives at the New Orleans apartment of her sister Stella and Stella's husband, the raw, sexual, Polish-American factory worker Stanley Kowalski; over the course of the play, Stanley systematically destroys Blanche's pretensions to refinement and her psychological defenses until, at the play's climax, he rapes her; the play ends with Blanche being taken to a mental institution, speaking the play's most famous line: 'Whoever you are — I have always depended on the kindness of strangers.'\n\nA Streetcar Named Desire established Tennessee Williams as the preeminent poetic realist of the American stage — his evocation of New Orleans's heat, sexuality, and social decay; his complex and compassionate portrayal of Blanche as simultaneously pathetic and magnificent; and his use of music, lighting, and theatrical expressionism to externalise interior psychological states set a new standard for American drama. The play's sexual frankness was extraordinary for 1947 — its depiction of rape, desire, and female psychological collapse challenged the conventions of American theatrical representation and contributed to the loosening of censorship in American theatre.\n\nThe 1951 film adaptation (again directed by Kazan, with Brando repeating his stage performance) created one of the most memorable performances in American cinema — Brando's Stanley is the foundational image of the Method Acting tradition — and the play has been continuously produced worldwide, its contest between Blanche's world of illusion and Stanley's brutal reality read as allegory for the replacement of the Old South by industrial modernity, for the destruction of feminine sensibility by male power, and for the universal human need for illusion to sustain life against reality.",
    "causes": [
      "Tennessee Williams's autobiographical experience of his mother's Southern belle pretensions, his sister Rose's mental illness and lobotomy, and his own outsider sexuality (he was gay, in a period when that required concealment) gave A Streetcar Named Desire its emotional truth — Blanche's fragility, Rose Williams's shadow behind her, and the experience of social ostracism that structures Williams's entire dramatic vision.",
      "The post-World War II American cultural context — the replacement of the pre-industrial Old South's values (refinement, poetry, beauty) by the brash industrial modernity of the North (Stanley's immigrant working-class vitality) — gave the play's conflict its social and historical dimensions, making Blanche and Stanley emblems of two incompatible versions of America.",
      "Elia Kazan's direction and Marlon Brando's performance created the theatrical conditions that made A Streetcar's impact possible — Brando's use of Method acting to make Stanley's raw sexuality and violence viscerally present transformed American stage and screen performance and gave the play its explosive reception."
    ],
    "effects": [
      "A Streetcar Named Desire established Method acting — Marlon Brando's technique of total psychological and physical identification with the character — as the dominant performance style of American stage and screen, directly influencing the careers of James Dean, Paul Newman, Dustin Hoffman, Al Pacino, and Robert De Niro.",
      "Williams's theatrical technique — the use of music, lighting, and expressionistic staging to externalise psychological states; the 'plastic theatre' of symbolic and sensory elements — influenced the development of American theatrical production design and the rejection of naturalistic staging conventions.",
      "The play's frank depiction of sexual desire, rape, and psychological breakdown — its refusal to punish desire only with moral judgment but instead with tragic sympathy — contributed to the relaxation of American theatrical censorship in the late 1940s and 1950s and to the development of American drama's willingness to address sexuality, violence, and mental illness directly."
    ],
    "relationships": [
      {"sourceSlug": "tennessee-williams", "sourceName": "Tennessee Williams (1911–1983)", "verb": "AUTHORS", "targetSlug": "a-streetcar-named-desire", "targetName": "A Streetcar Named Desire (1947)", "context": "Williams wrote A Streetcar Named Desire drawing on autobiographical experience of his mother's Southern belle pretensions, his sister Rose's mental illness, and his own experience of sexual outsiderdom."},
      {"sourceSlug": "a-streetcar-named-desire", "sourceName": "A Streetcar Named Desire", "verb": "ESTABLISHES", "targetSlug": "method-acting", "targetName": "Method Acting (Brando as Stanley Kowalski)", "context": "Marlon Brando's performance as Stanley Kowalski — raw, sexual, psychologically identified — is the foundational demonstration of Method Acting as a theatrical and cinematic performance style."},
      {"sourceSlug": "a-streetcar-named-desire", "sourceName": "A Streetcar Named Desire", "verb": "CONTRASTS_WITH", "targetSlug": "death-of-a-salesman", "targetName": "Death of a Salesman (1949, Arthur Miller)", "context": "A Streetcar (1947) and Death of a Salesman (1949) together defined the golden age of American drama — Williams's poetic, expressionistic tragedy of desire and Miller's social tragedy of masculine aspiration covering the full range of American theatrical possibility in the postwar period."}
    ],
    "places": [
      {"name": "New Orleans, French Quarter (play's setting)", "role": "The sweltering, sensual New Orleans French Quarter — its music, heat, and mixed ethnic vitality — provides the social and physical environment in which Blanche's Old South pretensions collide with Stanley's immigrant working-class modernity"},
      {"name": "Broadway, New York (3 December 1947 premiere)", "role": "The Ethel Barrymore Theatre premiere — directed by Elia Kazan with Marlon Brando and Jessica Tandy — which ran for 855 performances and established Williams as the preeminent American playwright"}
    ],
    "subjects": ["American Drama", "Contemporary Era", "Tennessee Williams", "Theatre", "20th Century", "American Literature", "Drama", "Southern Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Streetcar Named Desire (Tennessee Williams, 1947) is one of the defining works of American theatre — its contest between Blanche DuBois's fragile Southern refinement and Stanley Kowalski's brutal industrial modernity remains the most powerful dramatic image of the tensions within American culture. Brando's Stanley established Method Acting as the dominant performance style of American cinema. The play won the Pulitzer Prize in 1948 and has been continuously produced worldwide.",
      "significanceCategory": "world-changing"
    }
  }
},

"catechism-of-the-catholic-church": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780catechism-of-the-catholic-church.json",
  "slug": "catechism-of-the-catholic-church",
  "data": {
    "summary": "The Catechism of the Catholic Church (Latin: Catechismus Catholicae Ecclesiae) is the official compendium of Catholic doctrine and teaching, promulgated by Pope John Paul II on 11 October 1992 — the thirtieth anniversary of the opening of the Second Vatican Council — and published in its definitive edition (the editio typica) in Latin in 1997. It is the first universal catechism since the Roman Catechism (Catechismus Romanus) promulgated after the Council of Trent in 1566 — four centuries previously — and reflects the teaching of Vatican II while presenting the whole of Catholic doctrine in a systematic, accessible form intended for the universal Church. Comprising 2,865 numbered paragraphs organized in four 'pillars' (The Creed; The Sacraments; The Commandments; and Prayer), the Catechism covers the entirety of Catholic belief and moral teaching, from the doctrine of the Trinity and Christology through the seven sacraments, through the moral theology of the commandments (including the Church's positions on abortion, contraception, capital punishment, war, social justice, and sexuality), to a systematic treatment of prayer culminating in the Our Father.\n\nThe Catechism was initiated at the Extraordinary Synod of Bishops (1985) called to evaluate the reception of Vatican II twenty years after its conclusion, and produced by a commission of twelve cardinals and bishops chaired by Cardinal Joseph Ratzinger (later Pope Benedict XVI) over six years of drafting (1986–1992). Its promulgation under John Paul II — who wrote a special Apostolic Constitution (Fidei Depositum) for its presentation — was a major moment in the pontificate, consolidating the interpretation of Vatican II in a way that both welcomed the Council's renewal and resisted more radical post-conciliar interpretations.\n\nThe Catechism has been translated into more than forty languages and has sold tens of millions of copies worldwide — the best-selling catechism in the history of the Catholic Church. Its systematic presentation of Catholic teaching on every aspect of belief, sacramental life, ethics, and prayer makes it the primary reference point for Catholic doctrine for the world's 1.3 billion Catholics and for those seeking to understand Catholic teaching.",
    "causes": [
      "The reception of the Second Vatican Council (1962–1965) generated considerable theological diversity and debate within the Catholic Church — the Extraordinary Synod of 1985 identified the lack of a universal catechism as a factor in the doctrinal confusion, and the production of the Catechism was the direct institutional response to the perceived need for a single authoritative statement of Catholic teaching after Vatican II.",
      "Pope John Paul II's pontificate (1978–2005) — characterised by strong doctrinal clarity and a concern to consolidate the authentic teaching of Vatican II against both progressive and traditionalist misreadings — provided the driving force for the Catechism's production; the project was central to John Paul II's programme of Catholic renewal.",
      "The pastoral tradition of catechism — systematic religious instruction in the form of questions and answers — going back through the Roman Catechism (1566), Luther's Small Catechism (1529), and the medieval theological summae (Aquinas's Summa Theologica) provided the textual tradition within which the 1992 Catechism situates itself and which it was designed to renew for the modern Church."
    ],
    "effects": [
      "The Catechism of the Catholic Church has become the primary reference point for Catholic teaching and doctrine worldwide — its 2,865 numbered paragraphs provide a systematic statement of Catholic belief cited in theological debate, catechetical instruction, legal proceedings, political discussion, and interfaith dialogue.",
      "Cardinal Ratzinger's role as the principal architect of the Catechism — and his interpretation of Vatican II as 'reform in continuity' rather than rupture — established the theological hermeneutics of his later pontificate as Benedict XVI (2005–2013), making the Catechism a key document for understanding the trajectory of post-conciliar Catholic theology.",
      "The Catechism's detailed treatment of social issues — its acknowledgment that capital punishment may be legitimate in extreme circumstances (later modified by Pope Francis in 2018 to declare it 'inadmissible'), its teaching on social justice and the option for the poor, and its treatment of sexual ethics — made it a major reference in political and social debates about Catholic social teaching."
    ],
    "relationships": [
      {"sourceSlug": "pope-john-paul-ii", "sourceName": "Pope John Paul II", "verb": "PROMULGATES", "targetSlug": "catechism-of-the-catholic-church", "targetName": "Catechism of the Catholic Church (1992)", "context": "John Paul II promulgated the Catechism on 11 October 1992 with the Apostolic Constitution Fidei Depositum — presenting it as the definitive statement of Catholic doctrine after Vatican II."},
      {"sourceSlug": "catechism-of-the-catholic-church", "sourceName": "Catechism (1992)", "verb": "FOLLOWS_FROM", "targetSlug": "second-vatican-council", "targetName": "Second Vatican Council (1962–1965)", "context": "The Catechism was produced in direct response to the perceived doctrinal confusion in the Catholic Church following Vatican II — its purpose being to present the Council's teaching in systematic, authoritative form."},
      {"sourceSlug": "catechism-of-the-catholic-church", "sourceName": "Catechism (1992)", "verb": "SUCCEEDS", "targetSlug": "roman-catechism-1566", "targetName": "Roman Catechism (Catechismus Romanus, 1566)", "context": "The 1992 Catechism is the first universal catechism since the Roman Catechism produced after the Council of Trent — four centuries previously — representing the same institutional impulse: to define and systematise Catholic teaching after a major council."}
    ],
    "places": [
      {"name": "Vatican City (production and promulgation, 1986–1992)", "role": "The production of the Catechism — the six-year drafting process under Cardinal Ratzinger's commission, and its promulgation by John Paul II at St Peter's Basilica on 11 October 1992"},
      {"name": "Global Catholic Church (1.3 billion members, reception context)", "role": "The worldwide Catholic Church for which the Catechism is the primary authoritative statement of doctrine — it has been translated into over forty languages and informs Catholic religious education on every continent"}
    ],
    "subjects": ["Catholic Church", "Contemporary Era", "Theology", "Christianity", "Religious Texts", "Doctrine", "20th Century", "Vatican"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Catechism of the Catholic Church (1992) is the first universal catechism in four centuries and the primary reference for the doctrine and teaching of the world's 1.3 billion Catholics. Its production under Pope John Paul II, with Cardinal Ratzinger as principal architect, represents the most significant consolidation of Catholic teaching since the Council of Trent — presenting the inheritance of Vatican II in systematic, authoritative form.",
      "significanceCategory": "highly-significant"
    }
  }
},

"ethics": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780ethics.json",
  "slug": "ethics",
  "data": {
    "summary": "The Ethics, Demonstrated in Geometrical Order (Latin: Ethica, Ordine Geometrico Demonstrata) is the magnum opus of Baruch Spinoza (1632–1677), published posthumously in 1677 (as part of the Opera Posthuma, four months after Spinoza's death) — one of the most ambitious and rigorous works in the history of Western philosophy, presenting a complete metaphysical, epistemological, psychological, and ethical system in the strict logical form of Euclidean geometry: axioms, definitions, propositions, demonstrations, corollaries, and scholia, built up from five fundamental definitions of God/Nature through to a theory of human freedom and blessedness. In Part I ('On God'), Spinoza argues that there is only one substance — infinite and eternal — which he identifies as both God and Nature (Deus sive Natura), developing a thoroughgoing monist pantheism that makes both God and the physical universe aspects of a single infinite being. Parts II–III develop a theory of the human mind and its emotions (the passions, or affects) from this metaphysical foundation, arguing that human beings are modes of the one substance whose minds are the idea of their body and whose emotions are fundamentally modifications of a basic drive towards self-preservation (the conatus). Parts IV–V address human bondage (the enslavement to the passions) and human freedom (the intellectual love of God — amor intellectualis Dei — by which the philosopher achieves blessedness).\n\nThe geometric method of the Ethics — its demonstration of ethical conclusions from metaphysical premises through strict logical derivation — is the most ambitious exercise of the rationalist method in the history of philosophy, and one of the most controversial: it either represents the highest achievement of rationalist philosophy (as Leibniz and the German Idealists believed) or a magnificent demonstration of its limitations (as Hume, Kant, and subsequent critics argued). Spinoza's pantheism — his identification of God with Nature and his rejection of a personal, transcendent God who cares about human affairs — provoked the charge of atheism that made him one of the most vilified thinkers of his century, and his naturalistic treatment of human beings as part of nature subject to the same causal laws as everything else anticipates both the scientific naturalism of the 19th century and the psychoanalytic tradition.\n\nThe Ethics is one of the foundational texts of Western philosophy — its influence runs through Leibniz, the German Idealists (Goethe, Schelling, Hegel), the Romantic poets (Wordsworth, Coleridge, Shelley), the 19th-century naturalist tradition, Einstein (who famously said he believed in 'Spinoza's God'), and the contemporary philosophy of mind's treatment of the mind-body problem.",
    "causes": [
      "Spinoza's philosophical formation in the rationalist tradition — his study of Descartes's Principles of Philosophy (which he lectured on and reconstructed in geometric form in his first published work) and his engagement with the Cartesian dualism of mind and substance — gave the Ethics its formal ambition: to solve the Cartesian mind-body problem by beginning from a more fundamental metaphysical premise (one substance rather than two).",
      "Spinoza's excommunication (herem) from the Amsterdam Sephardic Jewish community in 1656 — one of the most severe excommunications in recorded Jewish history, whose reasons remain unclear — placed him outside any religious community and freed him to develop a radical philosophical system that neither traditional Judaism, Christianity, nor Cartesian rationalism could accommodate.",
      "The 17th-century scientific revolution — the mechanistic physics of Descartes and Galileo, the demonstration that nature follows mathematical laws, and the progressive displacement of Aristotelian teleology by mechanistic explanation — provided both the model of rigorous demonstration (Euclid's geometry) that Spinoza imitated and the naturalistic worldview within which his identification of God with Nature was intellectually possible."
    ],
    "effects": [
      "Spinoza's pantheism — Deus sive Natura, the identification of God with the single infinite substance of which everything is a mode — became the touchstone for the religious sensibility of German Romanticism and Idealism: Goethe's famous declaration 'I am a pantheist' and Wordsworth's 'natural piety' both develop in the tradition of Spinoza's identification of the divine with the natural order.",
      "The Ethics' naturalistic treatment of human emotion — its analysis of the passions as modifications of the conatus (drive towards self-preservation) operating according to causal laws — anticipates both the psychoanalytic tradition (Freud's psychology of the drives) and the 20th-century neuroscience of emotion (Antonio Damasio's Descartes' Error is explicitly Spinozist in its argument).",
      "Spinoza's argument in the Theological-Political Treatise (companion to the Ethics) for freedom of thought and the separation of philosophy from theology — along with the Ethics' demonstration that a coherent system of ethics could be built without reference to divine command — is one of the foundational arguments of the Enlightenment tradition of secular ethics and political liberalism."
    ],
    "relationships": [
      {"sourceSlug": "baruch-spinoza", "sourceName": "Baruch Spinoza (1632–1677)", "verb": "AUTHORS", "targetSlug": "ethics", "targetName": "Ethics, Demonstrated in Geometrical Order (1677)", "context": "Spinoza spent most of his adult life writing the Ethics, completing it c. 1675 but withholding it from publication; it was published posthumously four months after his death from pulmonary consumption."},
      {"sourceSlug": "ethics", "sourceName": "Ethics (Spinoza)", "verb": "RESPONDS_TO", "targetSlug": "descartes", "targetName": "Descartes's mind-body dualism (Meditations, 1641)", "context": "The Ethics is in part Spinoza's systematic resolution of the Cartesian problem of how an immaterial mind can interact with a material body — by arguing that mind and body are two attributes of the single infinite substance, not two separate substances."},
      {"sourceSlug": "ethics", "sourceName": "Ethics (Spinoza's pantheism)", "verb": "INFLUENCES", "targetSlug": "german-idealism", "targetName": "German Idealism and Romanticism (Goethe, Schelling, Hegel)", "context": "Spinoza's identification of God with Nature became the touchstone for German Romantic and Idealist thought — Schelling called Spinoza 'the hero of philosophy' and his pantheism was the most significant philosophical influence on the German Romantic movement."}
    ],
    "places": [
      {"name": "Amsterdam and The Hague, Dutch Republic (1650s–1677, composition context)", "role": "Spinoza wrote the Ethics in the Dutch Republic — Amsterdam, Voorburg, and The Hague — the most intellectually tolerant society in 17th-century Europe, which made it possible to develop and circulate a system as radical as his"},
      {"name": "European philosophical tradition (1677 onwards, reception)", "role": "The Ethics' reception across European philosophy — from the immediate controversies of the late 17th century through its rehabilitation in German Idealism and its influence on Romantic, naturalist, and psychoanalytic thought"}
    ],
    "subjects": ["Philosophy", "Early Modern Era", "Spinoza", "Metaphysics", "Ethics", "17th Century", "Dutch Republic", "Rationalism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Spinoza's Ethics (1677) is one of the most ambitious works in the history of Western philosophy — its geometric demonstration of a complete metaphysical and ethical system from the premise of one infinite substance (Deus sive Natura) represents the highest point of rationalist philosophy and one of its most enduring achievements. Its influence runs through German Idealism, Romanticism, 19th-century naturalism, and contemporary philosophy of mind.",
      "significanceCategory": "world-changing"
    }
  }
},

"annals-tacitus": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781annals-tacitus.json",
  "slug": "annals-tacitus",
  "data": {
    "summary": "The Annals (Latin: Annales) is the major historical work of Publius Cornelius Tacitus (c. 56 – c. 120 CE), written c. 116–117 CE and covering Roman history from the death of Augustus (14 CE) to the death of Nero (68 CE) — the entire period of the Julio-Claudian dynasty. Of the original 16 books, roughly half survive: Books I–IV (Tiberius's reign, 14–29 CE), portions of Books V–VI (Tiberius, 29–37 CE), and Books XI–XVI (Claudius and Nero, 47–66 CE). The Annals is the primary source for the history of the early Principate and contains some of the most celebrated passages in Latin historical literature, including the account of the death of Augustus and the succession crisis, the career and death of Germanicus, the reign of terror under Tiberius and his minister Sejanus, the fire of Rome under Nero (64 CE), the persecution of the early Christians ('those hated for their abominations, called Christians by the populace'), and the political murder of Seneca.\n\nTacitus's style is the most distinctive in Latin historical writing — the famous brevitas Taciti (Tacitean brevity), in which complex political and psychological content is compressed into dense, allusive, and rhetorically charged prose; the use of indirect statement and innuendo to imply what cannot be directly stated about imperial tyranny; and the structure of ironic contrasts and juxtapositions that reveal the gap between the official ideology of the Principate and its actual practice of surveillance, denunciation, and political murder. Tacitus's historical method combines primary research (he had access to the senatorial acta and other archival sources) with rhetorical shaping and moral judgment — his pessimistic view of Roman imperial history as a progressive corruption of the Republic's virtues by autocracy gives the Annals a distinctive ideological perspective.\n\nThe Annals is a foundational text of Western historiography — its portrait of the early emperors (Tiberius as a brooding hypocrite, Caligula as megalomaniac, Claudius as a puppet of his freedmen, Nero as a monster who killed his own mother) shaped the historical memory of the Julio-Claudian dynasty for two millennia and is the primary narrative account of the period that scholars must use and argue with.",
    "causes": [
      "Tacitus's personal experience of imperial tyranny under Domitian (r. 81–96 CE) — during whose reign he was a senator who 'survived' while better men were executed — gave the Annals its obsessive concern with the corruption of senatorial independence under autocracy and its portrait of the mechanisms by which the Senate was transformed from the governing body of the Republic to the compliant instrument of Julio-Claudian terror.",
      "The literary tradition of Roman historical writing — particularly the senatorial tradition of Sallust, Livy, and the lost Republican historians — provided the formal models and the ideological framework within which Tacitus's critical assessment of imperial history is situated, measuring the Principate against the Republican virtues it claimed to restore while systematically destroying them.",
      "The availability of archival sources — including the senatorial acta, military dispatches, and private memoranda that Tacitus's senatorial position and historical research gave him access to — provided the documentary foundation for the Annals, allowing Tacitus to reconstruct the political history of the early Principate in detail unavailable to most later historians."
    ],
    "effects": [
      "The Annals created the canonical historical portrait of the Julio-Claudian emperors that has dominated Western historical memory for two millennia — Tiberius as a paranoid hypocrite hiding his nature behind cold dissimulation, Nero as a monster who fiddled while Rome burned, Sejanus as the archetype of the dangerous favourite — shaping literary representations from Shakespeare's Sejanus to I, Claudius (Robert Graves, 1934) and countless subsequent dramatisations.",
      "Tacitus's famous reference to the Christians — the earliest surviving non-Christian literary reference to Jesus Christ and the crucifixion — in his account of Nero's persecution after the fire of Rome has been central to the historical debate about the existence of Jesus and the early persecution of Christians, making Annals 15.44 one of the most discussed passages in ancient historical scholarship.",
      "Tacitus's political analysis — his account of how the mechanisms of imperial power (surveillance, denunciation, the suppression of public speech and honest historical record) corrupt both rulers and the ruled — made him the political thinker most cited by Renaissance Humanists trying to understand tyranny (the 'Tacitist' tradition of Machiavelli, Guicciardini, and their heirs), and his analysis of imperial autocracy is still invoked in discussions of authoritarian politics."
    ],
    "relationships": [
      {"sourceSlug": "tacitus", "sourceName": "Publius Cornelius Tacitus (c. 56–c. 120 CE)", "verb": "AUTHORS", "targetSlug": "annals-tacitus", "targetName": "Annals (c. 116–117 CE)", "context": "Tacitus wrote the Annals as the culminating work of his historical career, covering the Julio-Claudian dynasty from Augustus's death to Nero's — drawing on archival research and his experience as a senator under Domitian to produce the definitive critical account of the early Principate."},
      {"sourceSlug": "annals-tacitus", "sourceName": "Annals (15.44)", "verb": "REFERENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ (crucifixion under Pontius Pilate)", "context": "Tacitus's reference to the Christians in Annals 15.44 — 'Christus, from whom the name had its origin, suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus' — is the earliest surviving non-Christian literary reference to Jesus and the crucifixion."},
      {"sourceSlug": "annals-tacitus", "sourceName": "Annals", "verb": "INFLUENCES", "targetSlug": "tacitism", "targetName": "Tacitism (Renaissance political philosophy)", "context": "The Annals was a foundational text for the Renaissance Tacitist tradition — Machiavelli, Guicciardini, and their heirs read Tacitus as the analyst of the mechanisms of tyranny and the corruption of public virtue under autocracy."}
    ],
    "places": [
      {"name": "Rome (c. 116–117 CE, composition)", "role": "Tacitus wrote the Annals in Rome during the reign of Trajan (r. 98–117 CE) — a period of relative political freedom after Domitian's terror that allowed him to write candidly about the surveillance and fear of the Julio-Claudian period"},
      {"name": "Roman Empire (14–68 CE, narrative scope)", "role": "The Annals covers the entire Julio-Claudian dynasty from the death of Augustus (14 CE) through Tiberius, Caligula, Claudius, and Nero — the foundational period of imperial autocracy"}
    ],
    "subjects": ["Roman History", "Classical Era", "Historiography", "Latin Literature", "Roman Empire", "Political History", "Primary Source", "Ancient Rome"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Tacitus's Annals (c. 116–117 CE) is the primary historical source for the Julio-Claudian dynasty and one of the most influential texts in Western historiography — its psychologically penetrating portraits of Tiberius, Claudius, and Nero shaped historical memory for two millennia, its reference to the crucifixion of Christ is the earliest non-Christian literary evidence for Jesus, and its analysis of imperial tyranny became the foundational text of Renaissance political thought.",
      "significanceCategory": "world-changing"
    }
  }
},

"chronicle-of-the-black-death-de-mussis": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781chronicle-of-the-black-death-de-mussis.json",
  "slug": "chronicle-of-the-black-death-de-mussis",
  "data": {
    "summary": "The Chronicle of the Black Death by Gabriele de' Mussi (c. 1280 – c. 1356) is a Latin narrative account of the Black Death in Europe (1347–1351), composed c. 1348–1349 by a Piacenzan notary who lived through the epidemic, describing its arrival in Europe from the East, its catastrophic mortality, and its social and psychological effects on the communities of northern Italy. De' Mussi's chronicle is significant as one of the earliest and most detailed eyewitness accounts of the Black Death and as the source of the famous account of the siege of Caffa (1346) — the Genoese trading colony on the Crimean coast — in which de' Mussi claims that the attacking Mongol army catapulted plague-infected corpses over the walls into the city, and that the Genoese sailors who fled Caffa brought the plague to Sicily and thence to the rest of Europe: a passage that, if historically accurate, would make the Caffa siege one of the first documented instances of biological warfare in history.\n\nDe' Mussi's account captures the overwhelming social and psychological impact of the Black Death with immediacy and detail unusual among contemporary sources: his description of the fear, the abandonment of the sick by family members, the breakdown of normal social bonds, the desperate search for religious meaning in catastrophic mortality, and the scale of the dying — perhaps 30–50% of Europe's population within three years — gives the chronicle its historical and literary value. His account of the Caffa siege — with its dramatic image of plague-infected bodies being catapulted into a besieged city — has been extensively discussed in the historical literature, though some scholars doubt that de' Mussi was present at Caffa himself and may have been reporting second-hand accounts circulating in Piacenza.\n\nDe' Mussi's chronicle, alongside other contemporary accounts (Agnolo di Tura's Sienese chronicle, Boccaccio's preface to the Decameron, the reports of the Florentine bankers and notaries) constitutes the primary literary record of the most catastrophic pandemic in European history — the event that killed approximately 25 million Europeans, transformed the social and economic structures of medieval Europe, and has been called 'the first great European crisis of the modern world.'",
    "causes": [
      "The Black Death itself — the bubonic, pneumonic, and septicaemic plague epidemic caused by the bacterium Yersinia pestis, which arrived in Sicily from the eastern Mediterranean in October 1347 and spread across Europe with devastating speed, killing an estimated 25–50% of the European population by 1353 — generated the overwhelming crisis that de' Mussi's chronicle attempts to comprehend and record.",
      "De' Mussi's professional training as a notary — skilled in Latin composition and accustomed to the precise recording of legal and commercial facts — gave him both the literacy and the documentary instinct to produce a written account of the epidemic, making his chronicle more systematic and detailed than the fragmentary accounts of most other contemporary observers.",
      "The medieval Christian understanding of plague as divine punishment for human sin — a theological framework that de' Mussi employs throughout his chronicle, framing the Black Death as God's judgment on a corrupt humanity — provided both the interpretive lens through which he and his contemporaries understood the epidemic and the moral urgency that drove him to record it."
    ],
    "effects": [
      "De' Mussi's account of the Caffa siege — the catapulting of plague-infected corpses over the city walls — has been widely cited in discussions of biological warfare and the origins of the European Black Death, and his narrative has been used by epidemiologists studying the spread of the 1347–1351 epidemic to reconstruct the route of the plague's westward movement.",
      "De' Mussi's chronicle, alongside Boccaccio's Decameron preface and the other Italian plague accounts, constitutes the primary literary evidence for the social history of the Black Death — the breakdown of social bonds, the abandonment of the sick, the collapse of normal burial practices, and the desperate search for meaning that characterise the epidemic — evidence that has been extensively analysed in the historical scholarship of the 20th and 21st centuries.",
      "The Black Death's demographic devastation — the mortality to which de' Mussi's chronicle bears witness — transformed the social and economic structures of medieval Europe: the labour shortage that followed the epidemic empowered the surviving peasantry to demand better conditions (contributing to the peasant revolts of the 1370s–1380s), disrupted the feudal order, and accelerated the economic and social transformations that led to the Renaissance."
    ],
    "relationships": [
      {"sourceSlug": "chronicle-of-the-black-death-de-mussis", "sourceName": "Chronicle of the Black Death (de' Mussi, c. 1348)", "verb": "DOCUMENTS", "targetSlug": "black-death", "targetName": "Black Death (1347–1351)", "context": "De' Mussi's chronicle is one of the primary eyewitness accounts of the Black Death's arrival in Europe and its catastrophic mortality — written from within the epidemic as it devastated northern Italy."},
      {"sourceSlug": "chronicle-of-the-black-death-de-mussis", "sourceName": "Chronicle (Caffa episode)", "verb": "DESCRIBES", "targetSlug": "siege-of-caffa", "targetName": "Siege of Caffa (1346, alleged biological warfare)", "context": "De' Mussi's account of the Mongol army catapulting plague-infected corpses over the walls of Caffa — a Genoese colony in the Crimea — is the most famous source for the claim that the Black Death was spread westward by the Genoese sailors who fled the siege."},
      {"sourceSlug": "chronicle-of-the-black-death-de-mussis", "sourceName": "Chronicle (Italian plague narrative)", "verb": "CONTEMPORARY_WITH", "targetSlug": "decameron", "targetName": "Boccaccio's Decameron (1353)", "context": "De' Mussi's chronicle and Boccaccio's Decameron (whose preface is the most celebrated literary account of the Black Death in Florence) are the two most important Italian literary responses to the epidemic of 1347–1351."}
    ],
    "places": [
      {"name": "Piacenza, northern Italy (c. 1348–1349, composition)", "role": "De' Mussi wrote his chronicle in Piacenza — one of the first Italian cities devastated by the Black Death — as an eyewitness to the epidemic's catastrophic mortality in northern Italy"},
      {"name": "Caffa (Feodosia), Crimea (1346, siege narrative)", "role": "The Genoese trading colony on the Crimean coast — the setting of de' Mussi's famous account of the Mongol catapulting of plague-infected corpses that he presents as the origin of the epidemic's westward spread"}
    ],
    "subjects": ["Medieval History", "Medieval Era", "Black Death", "Plague", "Primary Source", "Italian History", "14th Century", "Epidemic History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "De' Mussi's Chronicle of the Black Death (c. 1348) is one of the primary eyewitness accounts of the most catastrophic pandemic in European history — its vivid description of the Black Death's social and psychological impact and its famous account of the Caffa siege (an alleged early instance of biological warfare) make it an indispensable source for historians of the 14th-century epidemic.",
      "significanceCategory": "significant"
    }
  }
},

"a-tale-of-two-cities": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-tale-of-two-cities.json",
  "slug": "a-tale-of-two-cities",
  "data": {
    "summary": "A Tale of Two Cities is the historical novel by Charles Dickens (1812–1870), published in weekly serial instalments in the periodical All the Year Round from 30 April to 26 November 1859, and set during the French Revolution — specifically the years 1775 to 1793, from the calm before the storm through the September Massacres and the Terror to the execution of Sydney Carton on the guillotine. One of the best-selling novels in the history of fiction (with estimated sales of 200 million copies, one of the highest of any novel ever published in English), it begins with the most famous opening sentence in the Victorian novel: 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...' The novel follows the intertwined stories of the English lawyer Sydney Carton (the dissolute but noble-hearted man who sacrifices his life for another in the novel's final act), the French physician Dr. Manette (imprisoned in the Bastille for 18 years and mentally destroyed by the experience), his daughter Lucie, and the French aristocrat Charles Darnay — against the background of revolutionary Paris, the storming of the Bastille, and the Terror.\n\nA Tale of Two Cities is the most political of Dickens's mature novels — its depiction of the French Revolution is simultaneously a sympathetic portrayal of the suffering of the French poor under aristocratic oppression (the novel's most famous scene, the crushing of a child under the carriage wheels of the Marquis St. Evrémonde, emblematises the callousness of the ancien régime) and a horrified critique of the Terror's bloodlust and the dehumanising cycle of violence that replaces one tyranny with another. Dickens's historical imagination was shaped by Thomas Carlyle's The French Revolution (1837), which he read multiple times and which gave him both the period's atmosphere and the philosophical framework of revolutionary catastrophe as the inevitable consequence of aristocratic oppression.\n\nThe novel's ending — Sydney Carton's voluntary sacrifice on the guillotine, taking the place of Charles Darnay and going to his death with the famous last words (the most celebrated in Victorian fiction): 'It is a far, far better thing that I do, than I have ever done; it is a far, far better rest that I go to than I have ever known' — is one of the most celebrated moments of redemptive self-sacrifice in the English novelistic tradition.",
    "causes": [
      "Thomas Carlyle's The French Revolution: A History (1837) — which Dickens read multiple times and described as his primary source — provided A Tale of Two Cities with its historical framework, its atmospheric evocation of the Terror, and its philosophical understanding of the Revolution as the catastrophic consequence of aristocratic oppression's failure to address the suffering of the poor.",
      "Dickens's personal participation (at Wilkie Collins's suggestion) in a theatrical production of The Frozen Deep (Collins, 1856) — in which he played a man who sacrifices his life so that his rival can marry the woman they both love — gave him the emotional seed of Sydney Carton's final sacrifice and the dramatic situation of the novel's climax.",
      "The Victorian crisis of faith — the theological and moral uncertainty produced by Darwinian evolution, biblical criticism, and the challenges of industrial modernity — gave A Tale of Two Cities its redemptive narrative structure: the resurrection theme (Dr. Manette 'recalled to life', Carton's sacrificial death as a form of spiritual rebirth) responding to the period's need for secular narrative of redemption."
    ],
    "effects": [
      "A Tale of Two Cities has sold an estimated 200 million copies, making it one of the best-selling novels in the history of print — its serial format, dramatic narrative, and accessible historical subject matter made it accessible to a mass readership, and its influence on the popular imagination of the French Revolution has been immense.",
      "Sydney Carton's final sacrifice — the most celebrated moment of redemptive self-abnegation in Victorian fiction — became a touchstone of the English cultural tradition of heroic self-sacrifice, influencing subsequent representations of the theme in fiction, drama, and cinema and contributing to the Victorian cult of 'death before dishonour' heroism.",
      "Dickens's portrait of the French Revolution — sympathetic to the oppressed poor who made it, horrified by the Terror's violence — established the dominant English-language narrative of the Revolution as simultaneously necessary (given aristocratic oppression) and corrupted (by the bloodlust it unleashed), a narrative that has shaped popular and educational understanding of the Revolution ever since."
    ],
    "relationships": [
      {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens (1812–1870)", "verb": "AUTHORS", "targetSlug": "a-tale-of-two-cities", "targetName": "A Tale of Two Cities (1859)", "context": "Dickens wrote A Tale of Two Cities for his own periodical All the Year Round in 1859, drawing on Carlyle's French Revolution for historical atmosphere and on his own theatrical experience for the emotional climax of Sydney Carton's sacrifice."},
      {"sourceSlug": "a-tale-of-two-cities", "sourceName": "A Tale of Two Cities", "verb": "INSPIRED_BY", "targetSlug": "french-revolution-carlyle", "targetName": "Thomas Carlyle's The French Revolution: A History (1837)", "context": "Dickens read Carlyle's French Revolution multiple times before writing A Tale of Two Cities — acknowledging it as his primary source for the historical atmosphere and philosophical framework of the novel."},
      {"sourceSlug": "a-tale-of-two-cities", "sourceName": "A Tale of Two Cities", "verb": "SET_DURING", "targetSlug": "french-revolution", "targetName": "French Revolution (1789–1799)", "context": "A Tale of Two Cities is set during the French Revolution — specifically 1775–1793, climaxing in the Terror — making it the most widely read English-language fictional account of the Revolution."}
    ],
    "places": [
      {"name": "London and Paris (narrative setting, 1775–1793)", "role": "The two cities of the title — London (stability, safety, English civilization) and Paris (the Revolution, the Terror, the guillotine) — between which the novel's characters move, embodying the contrast between English constitutional order and French revolutionary catastrophe"},
      {"name": "Victorian Britain (1859, publication context)", "role": "The Britain in which Dickens published A Tale of Two Cities — the period of Chartism, industrial unrest, and the shadow of 1848 — made the French Revolution's lessons about the consequences of social inequality acutely relevant"}
    ],
    "subjects": ["Victorian Literature", "Classical Era", "Historical Fiction", "French Revolution", "Dickens", "English Literature", "19th Century", "Novel"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Tale of Two Cities (Dickens, 1859) is one of the best-selling novels in history — with approximately 200 million copies sold — and has shaped the popular imagination of the French Revolution more than any other English-language fiction. Its opening line, Sydney Carton's sacrifice, and its portrait of revolutionary Paris have become embedded in the cultural memory of the English-speaking world.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-study-in-scarlet": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-study-in-scarlet.json",
  "slug": "a-study-in-scarlet",
  "data": {
    "summary": "A Study in Scarlet is the first novel featuring Sherlock Holmes and Dr. John H. Watson, written by Arthur Conan Doyle (1859–1930) and published in Beeton's Christmas Annual (November 1887) before book publication in 1888 — the founding text of one of the most influential fictional characters in the history of literature and the beginning of a series that comprises four novels and 56 short stories, collectively the Holmesian canon. In A Study in Scarlet, Watson (recently returned from Afghanistan where he was wounded at the Battle of Maiwand) meets Holmes through a mutual acquaintance, they agree to share rooms at 221B Baker Street, and Watson observes Holmes applying his extraordinary powers of deductive reasoning to solve a murder in Lauriston Gardens — the victim a man named Enoch Drebber, killed with no signs of violence but with the word 'RACHE' (German for 'revenge') scrawled in blood on the wall. The novel is divided into two parts — the first set in London, the second in Utah among the Mormons — and resolves the mystery with a backstory of vengeance, forced marriage, and a journey across the American West.\n\nA Study in Scarlet introduced the most recognisable fictional detective in literary history: Sherlock Holmes — with his deerstalker cap (added by the illustrator Sidney Paget in a later story), his meerschaum pipe, his violin, his cocaine habit, his 221B Baker Street address, and above all his method of 'deduction' (more properly, abductive inference) — reasoning from physical clues to conclusions that appear miraculous but are the product of systematic observation and logical inference. Holmes's method ('When you have eliminated the impossible, whatever remains, however improbable, must be the truth') is the foundational formula of the fictional detective tradition and an influential model of scientific reasoning.\n\nThe Sherlock Holmes stories created the detective fiction genre in its modern form — displacing the earlier Gothic and sensationalist detective fiction (Poe's Dupin, Wilkie Collins's The Moonstone) with a ratiocinating hero whose investigations model a secular, scientific approach to truth — and influenced virtually every subsequent detective, from Agatha Christie's Hercule Poirot and Miss Marple through Raymond Chandler's Philip Marlowe to the modern forensic procedural television drama.",
    "causes": [
      "Arthur Conan Doyle's medical training at the University of Edinburgh — particularly his observation of the diagnostic method of the surgeon Dr. Joseph Bell, who could deduce a patient's occupation and history from physical observation — provided the direct model for Holmes's method: the application of systematic physical observation and logical inference to the 'diagnosis' of a crime.",
      "The late Victorian fascination with scientific method — the period's confidence that observation, evidence, and systematic reasoning could solve any problem — gave the Holmes stories their cultural resonance: Holmes embodies the Victorian scientific hero who applies reason and observation to dissolve the apparent mysteries that baffle ordinary minds.",
      "Edgar Allan Poe's detective stories featuring C. Auguste Dupin (The Murders in the Rue Morgue, 1841; The Purloined Letter, 1845) — which Conan Doyle had read and which Holmes explicitly references in A Study in Scarlet — provided the literary template of the brilliant amateur detective whose superior reasoning allows him to solve what the police cannot."
    ],
    "effects": [
      "The Sherlock Holmes canon created the modern detective fiction genre — establishing the formula of the brilliant detective, the chronicling companion (Watson), the baffled official police, and the solution through ratiocination that Christie, Sayers, Chandler, and virtually every subsequent detective writer either followed or defined themselves against.",
      "Sherlock Holmes became one of the most widely adapted fictional characters in history — the subject of over 25,000 stage productions, 70+ film and television adaptations (including the BBC's Sherlock and CBS's Elementary), and hundreds of pastiche novels — with Holmes and Watson among the most globally recognised fictional characters ever created.",
      "Holmes's method of deductive reasoning — the inference from physical clues (footprints, tobacco ash, calluses, clothing) to conclusions — influenced the development of forensic science and detective methodology, and his figure was invoked by Francis Galton in his development of fingerprint identification and by criminal investigators developing systematic forensic procedures."
    ],
    "relationships": [
      {"sourceSlug": "arthur-conan-doyle", "sourceName": "Arthur Conan Doyle (1859–1930)", "verb": "AUTHORS", "targetSlug": "a-study-in-scarlet", "targetName": "A Study in Scarlet (1887)", "context": "Conan Doyle wrote A Study in Scarlet in 1886, drawing on his observation of the Edinburgh surgeon Joseph Bell for Holmes's diagnostic-deductive method — it was published in Beeton's Christmas Annual in 1887 and established Holmes and Watson as the defining fictional detective partnership."},
      {"sourceSlug": "a-study-in-scarlet", "sourceName": "A Study in Scarlet", "verb": "FOUNDS", "targetSlug": "sherlock-holmes-canon", "targetName": "Sherlock Holmes canon (56 stories, 4 novels)", "context": "A Study in Scarlet is the founding text of the Holmes canon — introducing Holmes, Watson, 221B Baker Street, and the deductive method that all subsequent Holmes stories develop."},
      {"sourceSlug": "a-study-in-scarlet", "sourceName": "A Study in Scarlet", "verb": "INFLUENCES", "targetSlug": "detective-fiction", "targetName": "Modern detective fiction (Christie, Chandler, Sayers)", "context": "A Study in Scarlet established the formula of the detective fiction genre — brilliant amateur, chronicling companion, official police, ratiocination — that virtually all subsequent detective fiction either follows or defines itself against."}
    ],
    "places": [
      {"name": "London (Baker Street setting, late Victorian era)", "role": "221B Baker Street — the lodgings of Holmes and Watson — is the most famous fictional address in English literature, and the Victorian London of fog, hansom cabs, and gaslight is the iconic setting of the Holmes stories"},
      {"name": "Edinburgh (Conan Doyle's training, Joseph Bell model)", "role": "Conan Doyle studied medicine at the University of Edinburgh, where the diagnostician Joseph Bell demonstrated the systematic observation method that became Holmes's 'deductive' technique"}
    ],
    "subjects": ["Detective Fiction", "Classical Era", "English Literature", "Sherlock Holmes", "Victorian Literature", "19th Century", "Mystery", "Arthur Conan Doyle"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Study in Scarlet (Conan Doyle, 1887) is the founding text of the Sherlock Holmes canon and the founding document of modern detective fiction as a genre. Holmes's method of deductive reasoning from physical clues became the formula for virtually all subsequent detective fiction and forensic investigation, and Holmes and Watson are among the most globally recognised fictional characters in literary history.",
      "significanceCategory": "world-changing"
    }
  }
},

"a-journey-to-the-centre-of-the-earth": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-journey-to-the-centre-of-the-earth.json",
  "slug": "a-journey-to-the-centre-of-the-earth",
  "data": {
    "summary": "A Journey to the Centre of the Earth (French: Voyage au centre de la Terre) is the science fiction adventure novel by Jules Verne (1828–1905), published in 1864 (serialised in Pierre-Jules Hetzel's Magazine d'éducation et de récréation, then as a book in November 1864) — the third of Verne's extraordinary 'Voyages extraordinaires' series, which would eventually comprise 54 novels and establish Verne as the founding figure of modern science fiction. The novel follows the expedition of Professor Otto Lindenbrock (an eccentric German geologist), his nephew Axel (the narrator), and the Icelandic guide Hans, who descend through a volcanic crater in Iceland (the Snæfellsjökull) following a coded message left by the 16th-century Icelandic scientist Arne Saknussemm, descending to discover an enormous underground ocean, prehistoric creatures (plesiosaurs and ichthyosaurs, mastodons), an electrical storm, and a prehistoric human ('the Guardian') tending a herd of mastodons, before being ejected to the surface by a volcanic eruption through the crater of Stromboli in Sicily.\n\nA Journey to the Centre of the Earth exemplifies Verne's characteristic method: the meticulous, scientifically informed extrapolation from contemporary knowledge to an imagined but plausible scenario — the underground geology of the novel is based on the actual scientific debates of the 1860s about the interior of the earth (whether it was molten or solid), and Verne fills his underground world with the actual prehistoric creatures being discovered in the fossil record by the geologists and palaeontologists of his era. Lindenbrock's debate with the prevailing theory (that the earth's interior is at high temperature) against a competing hypothesis (that it might remain solid and at lower temperatures) is grounded in the actual scientific controversy, and Verne's novel takes the minority position that allows his hero to survive.\n\nVerne's 'Voyages extraordinaires' — comprising A Journey to the Centre of the Earth, Twenty Thousand Leagues Under the Sea (1870), Around the World in Eighty Days (1872), and 51 further novels — are the founding texts of modern science fiction as a genre, establishing its characteristic combination of scientific extrapolation, adventure narrative, and educational purpose ('to outline all the geographical, geological, physical, and astronomical knowledge amassed by modern science and to rewrite the history of the universe').",
    "causes": [
      "The explosion of geological and palaeontological knowledge in the 1850s–1860s — the systematic mapping of geological strata, the discovery of prehistoric fossil creatures (ichthyosaurs, plesiosaurs, mastodons), and the debate about the interior structure of the earth — provided A Journey to the Centre of the Earth with its scientific materials and the 'current science extrapolated to adventure' method that characterises Verne's approach.",
      "Pierre-Jules Hetzel's commission of Verne to write a series of 'educational adventure' novels for his magazine — Hetzel was a progressive publisher who believed that literature should combine entertainment with scientific and geographical education for a mass readership including children and young people — gave Verne the specific format of the Voyages extraordinaires and the mandate to make science accessible through adventure narrative.",
      "The German Romantic literary tradition — particularly E.T.A. Hoffmann's fantastic tales and the tradition of the Bildungsroman in which a young man undergoes transformative adventures — influenced the novel's narrative structure, its Axel/Lindenbrock uncle-nephew relationship, and its combination of scientific rationalism with the uncanny discovery of a hidden prehistoric world."
    ],
    "effects": [
      "A Journey to the Centre of the Earth established the 'lost world' narrative as a science fiction subgenre — the discovery of a hidden domain outside normal history in which prehistoric creatures survive — influencing Arthur Conan Doyle's The Lost World (1912), Edgar Rice Burroughs's Pellucidar series (1914–1963), and countless subsequent underground world and prehistoric survival narratives in fiction and film.",
      "Verne's method of basing adventure narrative on extrapolated current science — making scientific knowledge accessible and exciting through adventure narrative — established science fiction as a genre that could combine entertainment with education, influencing H.G. Wells (who explicitly positioned himself against Verne's method), Isaac Asimov, and the entire tradition of 'hard science fiction.'",
      "The 'Voyages extraordinaires' series — A Journey to the Centre of the Earth, Twenty Thousand Leagues Under the Sea, and Around the World in Eighty Days — have remained continuously in print for 150 years, have been adapted into film dozens of times, and have been cited by scientists (from astronauts to submarine designers) as the books that inspired their careers, making Verne's influence on the scientific imagination of the 20th century impossible to measure."
    ],
    "relationships": [
      {"sourceSlug": "jules-verne", "sourceName": "Jules Verne (1828–1905)", "verb": "AUTHORS", "targetSlug": "a-journey-to-the-centre-of-the-earth", "targetName": "A Journey to the Centre of the Earth (1864)", "context": "Verne wrote A Journey to the Centre of the Earth as the third of his Voyages extraordinaires — his series of scientifically grounded adventure novels published under Pierre-Jules Hetzel's direction."},
      {"sourceSlug": "a-journey-to-the-centre-of-the-earth", "sourceName": "Journey to the Centre of the Earth", "verb": "ESTABLISHES", "targetSlug": "lost-world-genre", "targetName": "Lost world science fiction subgenre", "context": "Verne's underground prehistoric world — with its ichthyosaurs, prehistoric ocean, and ancient human — established the 'lost world' narrative formula that Conan Doyle, Burroughs, and subsequent science fiction writers developed."},
      {"sourceSlug": "a-journey-to-the-centre-of-the-earth", "sourceName": "Voyages extraordinaires (Verne's series)", "verb": "FOUNDS", "targetSlug": "modern-science-fiction", "targetName": "Modern science fiction genre", "context": "Verne's Voyages extraordinaires — of which A Journey to the Centre of the Earth is a key example — established science fiction as a genre combining scientific extrapolation with adventure narrative, directly influencing H.G. Wells, Isaac Asimov, and the entire subsequent tradition."}
    ],
    "places": [
      {"name": "Iceland (Snæfellsjökull volcano) and Stromboli, Italy (narrative geography)", "role": "The expedition descends through the Snæfellsjökull crater in Iceland and emerges through Stromboli in Sicily — Verne's geological research gave these volcanic settings scientific plausibility"},
      {"name": "Paris (1864, composition and publication)", "role": "Verne wrote A Journey to the Centre of the Earth in Paris, working with Hetzel's publishing house to produce the Voyages extraordinaires as a series of scientifically informed adventure novels for a mass readership"}
    ],
    "subjects": ["Science Fiction", "Classical Era", "Jules Verne", "French Literature", "19th Century", "Adventure", "Geology", "Victorian Era"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Journey to the Centre of the Earth (Jules Verne, 1864) is one of the founding texts of modern science fiction — its method of basing adventure narrative on extrapolated current science established the genre's combination of scientific education and entertainment, and its 'lost world' formula influenced Conan Doyle, Burroughs, and the entire science fiction tradition. The Voyages extraordinaires series has been cited by scientists and engineers across the 20th century as the inspiration for their careers.",
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
