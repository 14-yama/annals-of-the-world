#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 24 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: confessions, book-of-rites, classic-of-poetry, beyond-good-and-evil,
          candide, ashokas-rock-edicts, anglo-saxon-chronicle, argonautica
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-24-may2026"

ENRICHMENTS = {

"confessions": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780confessions.json",
  "slug": "confessions",
  "data": {
    "summary": "Confessions (Latin: Confessiones) is the autobiographical work of Augustine of Hippo (354–430 CE), composed approximately 397–400 CE, in which Augustine narrates his life from birth to his conversion to Christianity (386 CE) and his mother Monica's death (387 CE), framed as a continuous prayer and confession addressed directly to God. It is one of the most remarkable texts in Western literature — simultaneously the first fully developed autobiography in the Western tradition, a masterwork of Latin rhetorical prose, a profound theological meditation on grace, time, memory, and the human will, and a spiritual journey narrative that established the template for confessional writing from Petrarch and Rousseau through modern memoir. Augustine's famous opening line — 'You stir us to take pleasure in praising You; for You have made us for Yourself, and our heart is restless, until it rests in You' (Latin: fecisti nos ad te et inquietum est cor nostrum donec requiescat in te) — is one of the most celebrated sentences in religious literature.\n\nConfessions traces Augustine's intellectual and spiritual biography: his childhood in Thagaste (modern Algeria), his brilliant rhetorical education in Carthage, his decade as a Manichaean auditor, his career as a rhetoric professor in Carthage, Rome, and Milan, his encounter with Neoplatonism and with Bishop Ambrose, the famous scene in the garden in Milan (386 CE) where he hears the child's voice 'tolle lege' ('pick up and read') and opens Paul's Letter to the Romans to the passage condemning immorality, and his conversion. The philosophical books (Books 10–13) — meditations on memory, time, and the interpretation of Genesis — are as significant for Western philosophy as the autobiographical narrative is for literature.\n\nAugustine's influence on Western Christianity and Western intellectual history is almost impossible to overstate — his theology of grace and original sin (developed in the anti-Pelagian controversies after Confessions) shaped Latin Christian doctrine for a millennium and divided Catholic and Protestant Christianity at the Reformation (Luther and Calvin were both profoundly Augustinian). Confessions is the primary source for his intellectual biography and the direct model for Petrarch's Letter to Posterity, Rousseau's Confessions, and the entire modern tradition of confessional autobiography.",
    "causes": [
      "Augustine's conversion to Christianity in 386 CE — after a decade of intellectual searching through Manichaeanism and Neoplatonism — and his growing role as a bishop and theological controversialist (he became Bishop of Hippo in 395 CE) created both the personal retrospective motive and the pastoral purpose for writing Confessions as a public account of divine grace working through a sinful life.",
      "The Donatist controversy in North Africa — the theological conflict over the validity of sacraments administered by traditors (clergy who had surrendered scriptures under persecution) — gave Augustine's narrative of his own conversion and God's patient pursuit of his restless will a direct pastoral relevance to the question of divine grace versus human merit.",
      "The Neoplatonic philosophical tradition that Augustine encountered in Milan (through the Latin translations of Marius Victorinus) provided him with the philosophical framework — the soul's ascent to the One through intellectual contemplation — that he then transformed through his encounter with Paul and his Christian account of will, grace, and the limits of self-sufficient reason."
    ],
    "effects": [
      "Confessions established the template for Western autobiographical and confessional writing — its combination of personal narrative, intellectual self-examination, and address to God created the form that Petrarch adapted (Letter to Posterity), Rousseau secularised and radicalised (Confessions, 1782), and the modern memoir tradition continues in a post-religious key.",
      "Augustine's theological synthesis in Confessions — his account of original sin, the bound will, the primacy of divine grace, and the restlessness of the human heart — shaped Latin Christian theology for a millennium and became the contested centre of the Reformation: Luther and Calvin's Augustinian theology of grace versus the Pelagian tendencies they attributed to medieval Catholicism.",
      "Books 10–13 of Confessions — Augustine's philosophical meditations on memory (as the mind's inner space), time (as distension of the soul rather than objective measurement), and the interpretation of Genesis — are foundational contributions to Western philosophy of mind and of time, anticipating Bergson's theory of duration and Husserl's phenomenology of inner time-consciousness."
    ],
    "relationships": [
      {"sourceSlug": "augustine-of-hippo", "sourceName": "Augustine of Hippo (354–430 CE)", "verb": "AUTHORS", "targetSlug": "confessions", "targetName": "Confessions (c. 397–400 CE)", "context": "Augustine wrote Confessions shortly after becoming Bishop of Hippo — a retrospective account of his intellectual and spiritual journey from birth to conversion, addressed directly to God."},
      {"sourceSlug": "confessions", "sourceName": "Confessions", "verb": "INFLUENCES", "targetSlug": "jean-jacques-rousseau", "targetName": "Rousseau's Confessions (1782)", "context": "Rousseau's Confessions — the foundational text of modern autobiographical introspection — directly responds to Augustine, secularising the confessional form while retaining its radical self-exposure and its interrogation of the relationship between individual experience and universal truth."},
      {"sourceSlug": "confessions", "sourceName": "Confessions", "verb": "SHAPES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation (Augustine's theology of grace)", "context": "Augustine's theology of grace and original sin — developed in the controversies that followed Confessions — became the theological foundation of Luther's and Calvin's Reformation critique of Catholic Pelagianism."}
    ],
    "places": [
      {"name": "Hippo Regius, North Africa (c. 397–400 CE)", "role": "The place of composition — Augustine wrote Confessions as the newly installed Bishop of Hippo (modern Annaba, Algeria), the North African port city where he served until his death"},
      {"name": "Thagaste, Carthage, Rome, Milan (narrative settings, 354–387 CE)", "role": "The biographical geography of Confessions — the cities tracing Augustine's intellectual journey from his birth in Thagaste through his education in Carthage and his conversion in Milan"}
    ],
    "subjects": ["Christian Theology", "Classical Era", "Autobiography", "North Africa", "Patristics", "Philosophy of Mind", "Latin Literature", "Augustine"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Confessions (Augustine, c. 397–400 CE) is simultaneously the first developed autobiography in Western literature, a masterwork of theological reflection on grace, memory, and time, and the foundational source for Augustine's theology — which shaped Latin Christianity for a millennium and divided Catholic and Protestant Christianity at the Reformation. Its confessional form established the template for Western introspective writing from Petrarch and Rousseau through modern memoir.",
      "significanceCategory": "world-changing"
    }
  }
},

"book-of-rites": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780book-of-rites.json",
  "slug": "book-of-rites",
  "data": {
    "summary": "The Book of Rites (Chinese: 禮記, Lǐjì, 'Records of Ritual') is one of the Five Classics (五經) of the Confucian literary canon — a collection of texts on the norms, administration, and ceremonial usages of the Zhou dynasty, compiled and edited by Han dynasty scholars (particularly Dai Sheng, fl. 1st century BCE) from earlier materials attributed to Confucius's disciples and other Zhou-period sources. Together with the Rites of Zhou (周禮) and the Rites of Etiquette and Ceremony (儀禮), it forms the Three Ritual Texts (三禮) at the heart of the Confucian conception of social and political order. The Book of Rites codifies the ritual forms (lǐ 禮) — the ceremonial practices governing all dimensions of social life from court ceremony and ancestral veneration through marriage, mourning, and hospitality — that Confucianism holds to be the foundation of harmonious social and political order.\n\nThe Book of Rites encompasses a remarkably diverse range of material: essays on the philosophy of ritual, descriptions of court and aristocratic ceremony, accounts of the ancient kings' virtuous governance, educational theory, medical knowledge, monthly calendar prescriptions, and two chapters — the 'Great Learning' (大學, Dàxué) and the 'Doctrine of the Mean' (中庸, Zhōngyōng) — that became two of the Four Books of the Neo-Confucian curriculum, the most influential educational canon in Chinese history. The 'Great Learning' articulates the Confucian programme of self-cultivation extending through family, state, and the world ('investigate things → extend knowledge → rectify the mind → cultivate the self → regulate the family → govern the state → bring peace to all under Heaven'), and the 'Doctrine of the Mean' develops the concept of zhongyong (balance, centrality, sincerity) as the foundation of moral cultivation.\n\nAs one of the Five Classics, the Book of Rites was central to the Chinese imperial examination curriculum that shaped the education of China's ruling elite from the Han through the Qing dynasties — making its philosophical framework one of the most practically consequential educational texts in world history. Its influence on Chinese social practice (funeral rites, wedding ceremonies, ancestral veneration), court protocol, and educational philosophy extended throughout East Asia.",
    "causes": [
      "The Zhou dynasty's elaborate ritual system — the ceremonial forms governing the relationships between the king, the feudal lords, and the various ranks of the nobility — provided the cultural materials that Confucius sought to restore and that the Book of Rites systematically codifies, preserving ritual forms threatened by the disorder of the Warring States period.",
      "The Han dynasty's institutionalisation of Confucianism as the state ideology (under Han Wudi, r. 141–87 BCE) — and the establishment of the Imperial Academy (Taixue) with the Five Classics as its curriculum — created the institutional context within which the Book of Rites was canonised as one of the core texts of official Chinese culture.",
      "The Neo-Confucian revival of the Song dynasty (960–1279 CE) — particularly Zhu Xi's extraction of the 'Great Learning' and 'Doctrine of the Mean' from the Book of Rites and their elevation to the Four Books — gave two chapters of the Book of Rites extraordinary cultural influence as the most studied texts of the imperial examination system from 1313 to 1905."
    ],
    "effects": [
      "The Book of Rites' systematic codification of Chinese ritual practice — funerary rites, wedding ceremonies, ancestral veneration, court protocol — shaped Chinese social life for two millennia, providing the normative framework within which Chinese families and courts conducted the ceremonies that structured social relations and transmitted culture.",
      "The 'Great Learning' chapter's eight-step programme of moral cultivation — from the investigation of things through self-cultivation to the governance of the world — became the foundational framework of Neo-Confucian education, shaping the curriculum of the imperial examinations and the moral self-understanding of China's educated elite from the Song through the Qing dynasties.",
      "The Book of Rites' influence spread throughout East Asia — to Korea (where Confucian ritual forms were adopted by the Joseon dynasty, 1392–1897), Japan (where the concept of lǐ/rei shaped aristocratic and samurai culture), and Vietnam — making it one of the most widely transmitted components of Chinese cultural influence in the region."
    ],
    "relationships": [
      {"sourceSlug": "book-of-rites", "sourceName": "Book of Rites (Lǐjì)", "verb": "PART_OF", "targetSlug": "five-classics-confucian", "targetName": "Five Classics (Confucian canon)", "context": "The Book of Rites is one of the Five Classics — the core texts of the Confucian literary canon that formed the curriculum of the Chinese imperial examination system."},
      {"sourceSlug": "book-of-rites", "sourceName": "Book of Rites", "verb": "CONTAINS", "targetSlug": "great-learning", "targetName": "Great Learning (大學)", "context": "The 'Great Learning' is a chapter of the Book of Rites that Zhu Xi elevated to one of the Four Books — the most influential educational text of Neo-Confucianism, articulating the programme of moral cultivation from investigation of things to world governance."},
      {"sourceSlug": "book-of-rites", "sourceName": "Book of Rites", "verb": "SYSTEMATISES", "targetSlug": "confucianism", "targetName": "Confucianism (ritual theory)", "context": "The Book of Rites is the primary Confucian text on ritual practice (lǐ) — systematising the ceremonial forms that Confucianism holds to be the foundation of social and political order."}
    ],
    "places": [
      {"name": "Han dynasty China (1st century BCE, compilation and canonisation)", "role": "The context of the Book of Rites' final compilation and canonisation — Han Confucian scholars collected and edited earlier ritual texts, making the Book of Rites one of the Five Classics"},
      {"name": "East Asia (China, Korea, Japan, Vietnam — ongoing influence)", "role": "The geographic sphere of the Book of Rites' influence — its ritual framework shaped social practice, court ceremony, and educational culture throughout the East Asian cultural sphere"}
    ],
    "subjects": ["Chinese Philosophy", "Confucianism", "Classical Era", "Chinese History", "Ritual", "East Asia", "Han Dynasty", "Imperial Examination"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Book of Rites (Lǐjì, compiled c. 1st century BCE) is one of the Five Confucian Classics — the core text of Chinese ritual philosophy whose codification of ceremonial forms shaped Chinese social practice for two millennia. Its contained chapters 'Great Learning' and 'Doctrine of the Mean' became two of the Four Books of the Neo-Confucian curriculum — the most studied texts of the imperial examination system that shaped the education of China's ruling elite from 1313 to 1905.",
      "significanceCategory": "highly-significant"
    }
  }
},

"classic-of-poetry": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780classic-of-poetry.json",
  "slug": "classic-of-poetry",
  "data": {
    "summary": "The Classic of Poetry (Chinese: 詩經, Shījīng, 'Book of Songs' or 'Book of Odes') is the oldest existing collection of Chinese poetry, comprising 305 poems dated to the Western Zhou and early Eastern Zhou dynasties (c. 1046–600 BCE), and one of the Five Classics of the Confucian literary canon. It encompasses a remarkable range of poetic forms and themes: folk songs (guofeng, 'airs of the states') from fifteen different regions describing everyday life, love, courtship, farming, and seasonal change; court hymns (ya) used in aristocratic ceremonies; and ritual hymns (song) used in ancestral worship. Confucius himself reportedly edited the Classic of Poetry and attached great importance to it — the Analects records him saying 'If a man has not studied the Odes, he will be at a loss to express himself' — and the canonical status the Confucian tradition gave the collection ensured that Chinese literary culture and the Chinese classical examination system took it as their foundational poetic text for over two millennia.\n\nThe Classic of Poetry's influence on Chinese literary tradition is comparable to Homer's on the Greek tradition and the Bible's on Western medieval literature — it established the forms, themes, and allusive tradition within which all subsequent Chinese poetry was written, and a sophisticated literary-critical tradition of interpreting the Odes developed over centuries. The Confucian hermeneutical tradition interpreted even the apparently simple love songs as allegorical expressions of political loyalty and moral relationships — the 'fishhawk' poem that opens the collection ('Guan guan goes the fishhawk, on the islet in the river; beautiful is this noble lady, a good mate for the lord') was read as an allegory of the king seeking virtuous ministers. This allegorical tradition shaped the entire Chinese classical literary culture and its approach to reading literary texts as expressions of moral and political truth.\n\nThe Classic of Poetry also played a significant role in women's literary culture in imperial China — its representation of female voices (the folk songs include poems from women's perspectives on love, abandonment, and the hardships of marriage) and the female poets of the Tang dynasty who wrote in its tradition made it one of the few canonical texts in which women's voices were represented.",
    "causes": [
      "The Zhou dynasty's practice of collecting folk songs from the various states — attributed to the Zhou court's system of gathering songs to assess the moral condition of the people and the quality of governance — provided the institutional mechanism for the collection of the regional folk poetry that forms the bulk of the Classic of Poetry.",
      "Confucius's educational programme — which made the study of the Odes central to moral and social education — gave the collection its canonical status and ensured its preservation and transmission as a foundational text of Chinese classical culture.",
      "The development of the Chinese literary tradition's allegorical approach to the Odes — the Confucian hermeneutical practice of reading even folk songs as political and moral allegories — created a sophisticated literary-critical tradition that enriched and transformed the collection's cultural significance beyond its original folk contexts."
    ],
    "effects": [
      "The Classic of Poetry established the foundational conventions of Chinese poetry — the four-character line, the parallelism, the nature imagery (the 'correlative' style using natural images to express human feelings), and the allusive tradition — that shaped Chinese verse for three millennia, from the Han through Tang, Song, and Ming dynasties.",
      "As one of the Five Classics, the Classic of Poetry was central to the imperial examination curriculum — memorised and mastered by every aspiring scholar-official in imperial China — making it, through the examination system's influence on Chinese bureaucracy, governance, and culture, one of the most practically influential texts in Chinese history.",
      "The Classic of Poetry's representation of diverse regional voices, women's perspectives, and everyday life — alongside the court hymns and ritual songs — preserved a remarkable record of early Zhou dynasty social and cultural life that is a primary source of exceptional value for historians and scholars of early China."
    ],
    "relationships": [
      {"sourceSlug": "confucius", "sourceName": "Confucius (551–479 BCE)", "verb": "EDITS_AND_CANONISES", "targetSlug": "classic-of-poetry", "targetName": "Classic of Poetry (Shījīng)", "context": "The Analects attributes the editing of the Classic of Poetry to Confucius, who reportedly selected 305 poems from a larger corpus and attached great educational significance to their study."},
      {"sourceSlug": "classic-of-poetry", "sourceName": "Classic of Poetry", "verb": "PART_OF", "targetSlug": "five-classics-confucian", "targetName": "Five Classics (Confucian canon)", "context": "The Classic of Poetry is one of the Five Classics that form the core of the Confucian literary canon and the imperial examination curriculum."},
      {"sourceSlug": "classic-of-poetry", "sourceName": "Classic of Poetry", "verb": "FOUNDS", "targetSlug": "chinese-literary-tradition", "targetName": "Chinese classical literary tradition", "context": "The Classic of Poetry established the formal conventions, imagistic vocabulary, and allusive tradition that shaped Chinese poetry for three millennia — the foundational text of the Chinese literary tradition analogous to Homer in the Greek tradition."}
    ],
    "places": [
      {"name": "Western and Eastern Zhou China (c. 1046–600 BCE, composition)", "role": "The historical context of the poems — collected from fifteen regional 'states' of the Zhou kingdom, representing a cross-section of early Zhou culture from court to countryside"},
      {"name": "Imperial China (Han–Qing, as examination text)", "role": "The educational context of the Classic of Poetry's greatest influence — as a required text of the imperial examination curriculum, shaping the literary culture and values of China's governing elite for two millennia"}
    ],
    "subjects": ["Chinese Literature", "Classical Era", "Confucianism", "Chinese History", "Poetry", "East Asia", "Zhou Dynasty", "Imperial Examination"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Classic of Poetry (Shījīng, c. 1046–600 BCE) is the oldest existing collection of Chinese poetry and one of the Five Confucian Classics — the foundational text of the Chinese literary tradition, establishing the formal conventions and allusive vocabulary that shaped Chinese verse for three millennia. As a required text of the imperial examination curriculum, it shaped the literary culture and values of China's governing elite for over two thousand years.",
      "significanceCategory": "highly-significant"
    }
  }
},

"beyond-good-and-evil": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780beyond-good-and-evil.json",
  "slug": "beyond-good-and-evil",
  "data": {
    "summary": "Beyond Good and Evil: Prelude to a Philosophy of the Future (German: Jenseits von Gut und Böse: Vorspiel einer Philosophie der Zukunft) is the philosophical work of Friedrich Nietzsche (1844–1900), published in 1886 — the most systematic and comprehensive presentation of his mature philosophy, written after Thus Spoke Zarathustra and intended as a critical demolition of the philosophical tradition from Plato through Kant in preparation for a new, honest philosophy that would affirm the will to power and the creation of new values. In nine parts covering 296 aphorisms and a concluding poem, it attacks philosophical dogmatism, the illusions of objective morality, the slave morality of Christianity and democracy, the philosopher's self-deception about the source of his values, and the decadence of 19th-century European culture — while sketching a positive vision of the philosopher as legislator of values, the noble as affirmer of life, and the possibility of a new, aristocratic philosophy beyond the 'good and evil' of conventional morality.\n\nNietzsche's key moves in Beyond Good and Evil include: his attack on the 'will to truth' as itself a moral assumption that requires philosophical examination ('Supposing truth is a woman — what then?'); his genealogical critique of philosophical systems as expressions of philosophers' drives and prejudices rather than disinterested pursuit of truth; his distinction between master morality (the noble affirmation of one's own power and vitality) and slave morality (the resentment of the powerful, dressed up as moral virtue); his critique of democracy and nationalism as herd phenomena; and his sketch of the 'free spirit' and the 'philosopher of the future' who will legislate new values for humanity. The work is written in Nietzsche's characteristic aphoristic, polemical style — brilliant, provocative, and deliberately combative.\n\nBeyond Good and Evil's influence on 20th-century thought has been enormous and contested: its critique of conventional morality influenced existentialism (Heidegger, Sartre), poststructuralism (Foucault, Derrida), and critical theory; its distinction between slave and master morality was grotesquely appropriated by Nazi ideology (though Nietzsche himself was a fierce anti-nationalist and anti-antisemite); and its positive vision of self-creation, affirmation, and the will to power has been read as both an aristocratic ethic of excellence and a fascist legitimation of domination.",
    "causes": [
      "Nietzsche's break with Schopenhauer and Wagner — the two figures who had dominated his early intellectual life — and his growing conviction that 19th-century European philosophy and culture were exhausted, nihilistic, and in need of a fundamental revaluation drove his mature philosophical project, of which Beyond Good and Evil is the most systematic expression.",
      "The publication of Thus Spoke Zarathustra (1883–1885) — which had presented Nietzsche's positive vision in mythic and prophetic form — left him feeling that he had not been understood, and Beyond Good and Evil was written as a more direct, analytical presentation of the philosophical critique that Zarathustra had expressed poetically.",
      "The European 'death of God' — the collapse of the Christian metaphysical framework under the pressure of scientific materialism, historical criticism of the Bible, and Darwinian evolution — created the cultural crisis that Nietzsche diagnosed as nihilism (the devaluation of the highest values) and to which his philosophy of the will to power and the revaluation of all values was a response."
    ],
    "effects": [
      "Beyond Good and Evil's critique of conventional morality and its genealogical method — tracing moral values back to their psychological and social origins — directly influenced Foucault's genealogical analysis of knowledge and power, and the broader poststructuralist project of denaturalising apparently self-evident cultural norms.",
      "Nietzsche's distinction between master and slave morality — and his critique of democracy, equality, and Christianity as expressions of slave morality's resentment — was appropriated (and distorted) by Nazi ideology, giving Beyond Good and Evil a political afterlife that Nietzsche himself, as a passionate anti-nationalist and anti-antisemite, would have repudiated.",
      "The influence of Beyond Good and Evil's vision of the philosopher as creator of values and the concept of the will to power on existentialism — particularly Heidegger's engagement with Nietzsche as the culmination of Western metaphysics and Sartre's concept of radical freedom and value creation — made it a foundational text of 20th-century continental European philosophy."
    ],
    "relationships": [
      {"sourceSlug": "friedrich-nietzsche", "sourceName": "Friedrich Nietzsche (1844–1900)", "verb": "AUTHORS", "targetSlug": "beyond-good-and-evil", "targetName": "Beyond Good and Evil (1886)", "context": "Nietzsche wrote Beyond Good and Evil as the most comprehensive and systematic presentation of his mature philosophical position — the critical counterpart to the positive vision of Thus Spoke Zarathustra."},
      {"sourceSlug": "beyond-good-and-evil", "sourceName": "Beyond Good and Evil", "verb": "INFLUENCES", "targetSlug": "michel-foucault", "targetName": "Michel Foucault (genealogical method)", "context": "Foucault's genealogical method — tracing the historical origins and power relations embedded in apparently natural moral and epistemic norms — is directly indebted to Nietzsche's genealogical critique of moral philosophy in Beyond Good and Evil and On the Genealogy of Morality."},
      {"sourceSlug": "beyond-good-and-evil", "sourceName": "Beyond Good and Evil", "verb": "CRITIQUES", "targetSlug": "immanuel-kant", "targetName": "Immanuel Kant (moral philosophy)", "context": "Beyond Good and Evil's central philosophical target is the Platonic-Kantian tradition of objective, universal morality — Nietzsche attacks the 'categorical imperative' as the disguised expression of a slave morality that denies the will to life."}
    ],
    "places": [
      {"name": "Sils-Maria, Switzerland and Leipzig (1885–1886, composition and publication)", "role": "Beyond Good and Evil was written primarily at Sils-Maria in the Upper Engadine — Nietzsche's summer retreat — and published in Leipzig in 1886"},
      {"name": "Western European philosophy (20th-century influence)", "role": "The sphere of Beyond Good and Evil's influence — through existentialism, poststructuralism, and critical theory, its critique of conventional morality shaped 20th-century continental European thought"}
    ],
    "subjects": ["Philosophy", "Modern Era", "Nietzsche", "Ethics", "Political Philosophy", "19th Century", "Continental Philosophy", "Existentialism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Beyond Good and Evil (Nietzsche, 1886) is the most systematic presentation of his mature philosophical critique — demolishing the Platonic-Kantian moral tradition, introducing the genealogical method, and sketching a philosophy of the will to power and value creation. Its influence on 20th-century continental philosophy (existentialism, poststructuralism, critical theory) and its contested political afterlife (Nazi appropriation, its actual anti-nationalist content) make it one of the most consequential and debated philosophical texts of the modern era.",
      "significanceCategory": "world-changing"
    }
  }
},

"candide": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780candide.json",
  "slug": "candide",
  "data": {
    "summary": "Candide, ou l'Optimisme ('Candide, or Optimism') is the satirical novella of François-Marie Arouet (Voltaire, 1694–1778), published anonymously in Geneva in 1759 — one of the most brilliant and influential satirical works in world literature, and the sharpest single attack on the Leibnizian philosophical optimism (the doctrine that 'this is the best of all possible worlds') that Voltaire found intellectually dishonest and morally scandalous in the face of the Lisbon earthquake of 1755 and the Seven Years' War. In 30 short chapters, the naive young hero Candide — student of the optimistic philosopher Pangloss, who embodies Leibniz's 'best of all possible worlds' doctrine — is expelled from paradise (the castle of Westphalia), suffers every conceivable disaster (war, rape, earthquake, Inquisition, slavery, murder), travels to virtually every part of the known world (Europe, South America, the Ottoman Empire), and eventually concludes with the famous injunction: 'We must cultivate our garden' — a retreat from grand metaphysical optimism into modest, practical engagement with immediate reality.\n\nVoltaire wrote Candide in three days (by his own account) in the aftermath of the Lisbon earthquake of November 1755, which killed between 30,000 and 100,000 people on All Saints' Day and seemed to Voltaire a definitive refutation of Leibniz's theodicy — the philosophical argument that God has created the best of all possible worlds and that apparent evil is part of a larger divine good. The novella's devastating irony — every experience of the 'best of all possible worlds' turns out to involve massacre, slavery, religious persecution, and arbitrary cruelty — is directed equally at Leibnizian optimism, institutional religion (the Inquisition, the Jesuits in Paraguay), war, slavery, and the European colonial system. El Dorado — the hidden city of perfect harmony discovered mid-narrative and immediately abandoned by Candide in his obsessive pursuit of his beloved Cunégonde — functions as Voltaire's utopian counter-image, deliberately unattainable.\n\nCandide's impact on European culture was immediate and enormous — 'Candide' and 'Pangloss' became bywords for naive optimism, and the novella's attack on institutional religion, philosophical theodicy, and the violence of European civilization contributed to the intellectual atmosphere of the French Revolution. It remains one of the most widely read works of the Enlightenment.",
    "causes": [
      "The Lisbon earthquake of 1 November 1755 — which killed between 30,000 and 100,000 people on All Saints' Day as they were in church — was the immediate provocation for Candide's satirical attack on Leibnizian optimism: if this is 'the best of all possible worlds', the earthquake's horror seemed to Voltaire a definitive philosophical refutation of Pangloss's cheerful theodicy.",
      "The Seven Years' War (1756–1763) — the first truly global conflict, spreading violence across Europe, North America, India, and the Caribbean simultaneously — provided Candide with its scenes of military massacre (the satire of military glory in chapters 2–3 depicts the slaughter of the Bulgarian campaign with savage black comedy).",
      "Voltaire's philosophical engagement with Leibniz's Theodicy (1710) and Pope's Essay on Man (1734) — his growing conviction that philosophical optimism was an intellectually dishonest way of explaining away genuine evil and suffering — drove Candide's systematic demolition of the 'best of all possible worlds' doctrine through the accumulation of unmaskable catastrophe."
    ],
    "effects": [
      "Candide's satirical demolition of Leibnizian optimism — the doctrine that this is 'the best of all possible worlds' — contributed decisively to the Enlightenment's critique of religious theodicy and metaphysical system-building, helping to shift European intellectual culture toward empiricism, pragmatism, and the 'cultivation of the garden' of immediate practical improvement.",
      "The novella's attack on religious institutions (the Inquisition, the Jesuits), the slave trade (the horrific description of a mutilated enslaved person in Surinam), and European imperial violence contributed to the intellectual atmosphere of the French Revolution and to the abolitionist and anti-clerical movements of the late 18th century.",
      "Candide's influence on the tradition of philosophical satire, dark comedy, and the satirical novella — from Samuel Johnson's Rasselas (1759, published the same year) through Voltaire's literary successors to 20th-century dark comedy — established it as the defining model of the philosophical satirical novella in Western literature."
    ],
    "relationships": [
      {"sourceSlug": "voltaire", "sourceName": "Voltaire (François-Marie Arouet, 1694–1778)", "verb": "AUTHORS", "targetSlug": "candide", "targetName": "Candide (1759)", "context": "Voltaire wrote Candide in the aftermath of the Lisbon earthquake — a devastating satirical response to Leibnizian optimism, written (he claimed) in three days."},
      {"sourceSlug": "lisbon-earthquake-1755", "sourceName": "Lisbon Earthquake (1 November 1755)", "verb": "PROVOKES", "targetSlug": "candide", "targetName": "Candide (1759)", "context": "The Lisbon earthquake — killing tens of thousands on All Saints' Day — was the immediate trigger for Candide's satire of Leibnizian theodicy: if this is the best of all possible worlds, the earthquake seemed a definitive philosophical refutation."},
      {"sourceSlug": "candide", "sourceName": "Candide", "verb": "ATTACKS", "targetSlug": "gottfried-leibniz", "targetName": "Gottfried Leibniz (Theodicy, 1710)", "context": "Candide's philosophical target — the 'best of all possible worlds' doctrine embodied in Pangloss — is Leibniz's theodicy, published in 1710, which argued that God has created the best possible world and that apparent evil serves a larger divine good."}
    ],
    "places": [
      {"name": "Geneva and Paris (January 1759, publication)", "role": "Candide was published anonymously in Geneva in January 1759 — immediately seized by the Geneva city authorities and the Paris Parlement, which increased its circulation enormously"},
      {"name": "Europe, South America, Ottoman Empire (narrative geography)", "role": "The novella's satirical geography — Candide's picaresque travels through virtually every part of the known world, accumulating evidence against the 'best of all possible worlds'"}
    ],
    "subjects": ["Enlightenment", "French Literature", "Early Modern Era", "Satire", "Philosophy", "Voltaire", "18th Century", "Political Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Candide (Voltaire, 1759) is the masterwork of Enlightenment satirical fiction — a devastating attack on Leibnizian philosophical optimism, institutional religion, and European colonial violence that contributed to the intellectual atmosphere of the French Revolution. Its satirical demolition of the 'best of all possible worlds' theodicy, written in the aftermath of the Lisbon earthquake, and its famous conclusion 'We must cultivate our garden' made it the defining model of philosophical satire in Western literature.",
      "significanceCategory": "world-changing"
    }
  }
},

"ashokas-rock-edicts": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781ashokas-rock-edicts.json",
  "slug": "ashokas-rock-edicts",
  "data": {
    "summary": "Ashoka's Rock Edicts are a collection of inscriptions — carved on polished rock faces and pillars throughout the Maurya Empire (modern India, Pakistan, Bangladesh, Nepal, and Afghanistan) on the orders of the Emperor Ashoka (r. c. 268–232 BCE) — that constitute the oldest surviving written records of an Indian emperor and the most important primary sources for Mauryan history. Written primarily in Prakrit (the vernacular languages of the region), using the Brahmi and Kharosthi scripts, they record Ashoka's conversion to Buddhism following the devastating Kalinga War (c. 261 BCE), his programme of dhamma (righteous law/ethics based on non-violence, tolerance, and compassion), his social welfare measures (hospitals, wells, roads, tree-planting), his renunciation of military conquest in favour of 'conquest by dhamma', and his patronage of Buddhism — including his famous claim to have sent Buddhist missionaries to the Hellenistic kingdoms of the Mediterranean world.\n\nThe Kalinga War — in which Ashoka's forces conquered the eastern Indian kingdom of Kalinga at the cost of approximately 100,000 killed and 150,000 deported — is described in Rock Edict XIII as the pivotal event of Ashoka's life: 'Beloved-of-the-Gods [Ashoka] felt remorse for having conquered the Kalingas, because the conquest of a country previously unconquered involves the slaughter, death, and carrying away captive of the people.' This text, in which a powerful ancient ruler expresses genuine remorse for military conquest and resolves to pursue peace, is one of the most remarkable documents in ancient political history. The edicts proclaim universal religious tolerance, compassion for all living beings, respect for parents and teachers, and the importance of dhamma as the basis of governance.\n\nAshoka's edicts were deciphered by James Prinsep in 1837 (the decipherment of the Brahmi script) — one of the great achievements of 19th-century philology — and their rediscovery transformed the understanding of ancient Indian history. They remain the most important primary source for Mauryan history and for the early development of Buddhism as a political and ethical force.",
    "causes": [
      "The Kalinga War (c. 261 BCE) — Ashoka's brutal conquest of the eastern Indian kingdom of Kalinga — was the pivotal event that, by Ashoka's own account in Rock Edict XIII, transformed him from a conventional conqueror into a Buddhist convert committed to dhamma and non-violence: the scale of the destruction he had ordered produced genuine moral remorse.",
      "The development of Buddhism as a sophisticated ethical and political philosophy — with its emphasis on non-violence (ahimsa), compassion for all sentient beings, and the liberation from suffering through the cultivation of wisdom and morality — provided Ashoka with the ideological framework within which to translate his remorse into a positive programme of governance.",
      "The Maurya Empire's administrative infrastructure — the extensive road network, the use of multiple scripts and languages, the provincial governors (mahamatras) — provided the technical means to inscribe and distribute the edicts across the empire's vast territory, from Afghanistan to South India."
    ],
    "effects": [
      "Ashoka's patronage of Buddhism — his support for the Third Buddhist Council (c. 250 BCE), his construction of stupas, his donation of cave monasteries, and his dispatch of missionary expeditions (including to Sri Lanka under his son Mahinda) — was decisive for Buddhism's transformation from a regional Indian religion into a world religion, spreading across Asia.",
      "The edicts' language of religious tolerance and non-violence — Ashoka's explicit instruction that all religious sects should be respected and that the state should promote the welfare of all its subjects regardless of religion — has made him a model figure for modern Indian secularism and pluralism, cited by Nehru and incorporated in the Indian national emblem (the Ashoka Chakra from his lion capital).",
      "The decipherment of Ashoka's edicts in 1837 — which required the decipherment of the Brahmi script — transformed the understanding of ancient Indian history, providing dateable primary sources that allowed historians to reconstruct the Mauryan period with a confidence previously impossible, and establishing Ashoka as one of the most remarkable figures in world history."
    ],
    "relationships": [
      {"sourceSlug": "ashoka-the-great", "sourceName": "Ashoka the Great (r. c. 268–232 BCE)", "verb": "COMMISSIONS", "targetSlug": "ashokas-rock-edicts", "targetName": "Ashoka's Rock Edicts (c. 268–232 BCE)", "context": "The edicts were commissioned by Ashoka and inscribed on rock faces and pillars throughout the Maurya Empire — they are the primary record of his policies, his Buddhist conversion, and his concept of dhamma governance."},
      {"sourceSlug": "ashokas-rock-edicts", "sourceName": "Ashoka's Rock Edicts", "verb": "DOCUMENTS", "targetSlug": "buddhism-spread", "targetName": "Spread of Buddhism (3rd century BCE)", "context": "The edicts record Ashoka's patronage of Buddhism and his missionary expeditions — including to Sri Lanka and the Hellenistic kingdoms — documenting the crucial phase in Buddhism's transformation from regional Indian philosophy to world religion."},
      {"sourceSlug": "kalinga-war", "sourceName": "Kalinga War (c. 261 BCE)", "verb": "TRANSFORMS", "targetSlug": "ashokas-rock-edicts", "targetName": "Ashoka's Rock Edicts (programme of dhamma)", "context": "Rock Edict XIII describes the Kalinga War's destruction as the event that transformed Ashoka from conqueror to penitent — the moral turning point that the entire edicts programme of dhamma governance was a response to."}
    ],
    "places": [
      {"name": "Maurya Empire (modern India, Pakistan, Afghanistan, Bangladesh, Nepal, c. 268–232 BCE)", "role": "The geographic distribution of the edicts — inscribed on rock faces and pillars throughout the vast Mauryan Empire, from Afghanistan to South India"},
      {"name": "Kalinga (modern Odisha, site of the war, c. 261 BCE)", "role": "The site of the decisive Kalinga War — whose devastation Ashoka describes in Rock Edict XIII as the pivotal event of his moral transformation"}
    ],
    "subjects": ["Ancient India", "Classical Era", "Maurya Empire", "Buddhism", "Political History", "Indian History", "Epigraphy", "Non-Violence"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Ashoka's Rock Edicts (c. 268–232 BCE) are the oldest surviving written records of an Indian emperor and the most important primary source for Mauryan history. Their record of Ashoka's conversion to Buddhism, his remorse for the Kalinga War (the ancient world's most remarkable expression of imperial moral self-examination), his programme of dhamma governance, and his missionary patronage of Buddhism makes them foundational for understanding both Mauryan India and the global spread of Buddhism.",
      "significanceCategory": "world-changing"
    }
  }
},

"anglo-saxon-chronicle": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781anglo-saxon-chronicle.json",
  "slug": "anglo-saxon-chronicle",
  "data": {
    "summary": "The Anglo-Saxon Chronicle is a collection of annals in Old English chronicling the history of the Anglo-Saxons, compiled initially under the direction of King Alfred the Great (r. 871–899 CE) approximately 890–892 CE as a prose record of events from the Roman invasion of Britain through Alfred's own reign, and then continued in various monasteries across England until the mid-12th century (the Peterborough Chronicle extends to 1154 CE). It survives in nine manuscript versions reflecting different textual traditions and regional perspectives, and it is the primary narrative source for the history of Anglo-Saxon England from the 5th through 11th centuries, and for the Viking invasions, the Danelaw, the unification of England under Æthelstan, and the Norman Conquest.\n\nKing Alfred commissioned the Chronicle as part of his extraordinary programme of cultural revival following the catastrophic Danish invasions of the 860s–870s that had overrun all of Anglo-Saxon England except Wessex — the promotion of Old English prose literacy, the translation of key Latin texts, and the writing of history in the vernacular were all components of Alfred's project of restoring English learning and building a unified English identity. The Chronicle's composition in Old English (rather than Latin) — unusual for medieval historical writing — made it both more accessible to a literate lay audience and a foundational document of Old English prose literature. Its continuation after Alfred's death through multiple monasteries and regional centres means it preserves diverse perspectives on the events of the 10th and 11th centuries.\n\nThe Peterborough Chronicle's account of the period after the Norman Conquest (post-1066) — written in a Middle English that shows the transformation of the Old English language under Norman French influence — is particularly valuable as a record of how the Conquest looked from a provincial English monastic perspective, and its famous description of the anarchy of King Stephen's reign (1135–1154) as a time when 'Christ and his saints were asleep' is one of the most powerful passages in medieval historical writing.",
    "causes": [
      "The Viking invasions of Anglo-Saxon England (840s–870s) — which destroyed the monasteries of Northumbria, East Anglia, and Mercia and reduced English learning to near-extinction — created the cultural crisis that Alfred's programme of English literary revival (including the commissioning of the Chronicle) was designed to address.",
      "Alfred's political project of English unification — his claim to be 'King of the Anglo-Saxons' rather than merely King of Wessex, and his self-presentation as the defender of all Christian Englishmen against pagan Vikings — required a historical narrative that could give the English people a sense of shared identity and common history.",
      "The Old English prose tradition — limited before Alfred but enriched by his translation programme (Gregory's Pastoral Care, Bede's Ecclesiastical History, Orosius, Boethius) — provided the literary model within which the Chronicle's vernacular historical prose was composed, establishing Old English as a language capable of serious historical and intellectual writing."
    ],
    "effects": [
      "The Anglo-Saxon Chronicle is the primary narrative source for Anglo-Saxon England — without it, the history of English kings from the 5th through 11th centuries, the Viking invasions, the Danelaw, the reign of Æthelstan (who united England), and the period leading to the Norman Conquest would be far less recoverable. It is irreplaceable as a primary source.",
      "The Chronicle's composition in Old English — and its continuation through the Norman period in transitional Middle English — makes it a foundational text of English literary history: a document of the transformation of the English language across six centuries, from early West Saxon prose through the first stages of Middle English.",
      "Alfred's commissioning of the Chronicle as part of his cultural revival programme established the precedent of royal patronage for vernacular historical writing in England, and the tradition of annalistic historical chronicle that the Anglo-Saxon Chronicle began continued (in Latin and vernacular forms) throughout the medieval English historical tradition."
    ],
    "relationships": [
      {"sourceSlug": "alfred-the-great", "sourceName": "Alfred the Great (r. 871–899 CE)", "verb": "COMMISSIONS", "targetSlug": "anglo-saxon-chronicle", "targetName": "Anglo-Saxon Chronicle (c. 890–892 CE)", "context": "Alfred the Great commissioned the original Anglo-Saxon Chronicle as part of his programme of English literary revival — a vernacular record of English history from Roman Britain through his own reign."},
      {"sourceSlug": "anglo-saxon-chronicle", "sourceName": "Anglo-Saxon Chronicle", "verb": "DOCUMENTS", "targetSlug": "norman-conquest", "targetName": "Norman Conquest of England (1066)", "context": "The Anglo-Saxon Chronicle is the primary English narrative source for the Norman Conquest — its accounts of the events of 1066, Harold Godwinson, and William the Conqueror are essential primary evidence."},
      {"sourceSlug": "anglo-saxon-chronicle", "sourceName": "Anglo-Saxon Chronicle", "verb": "RECORDS", "targetSlug": "viking-age", "targetName": "Viking Age (invasions of England, 793–1066)", "context": "The Chronicle is the primary narrative source for the Viking invasions of England — recording the great Danish army's conquest of Northumbria, East Anglia, and Mercia, and the subsequent Danelaw and its eventual reconquest."}
    ],
    "places": [
      {"name": "Wessex, England (c. 890–892 CE, original compilation)", "role": "The context of the original Chronicle — compiled under Alfred's direction in Wessex as a record of English history for the West Saxon royal court and its monasteries"},
      {"name": "England (multiple monastic centres, 892–1154 CE, continuation)", "role": "The continuation sites — Winchester, Canterbury, Worcester, Abingdon, and Peterborough, each maintaining separate manuscript traditions that provide diverse regional perspectives"}
    ],
    "subjects": ["Old English Literature", "Medieval History", "Medieval Era", "Anglo-Saxon England", "Viking Age", "English History", "Historiography", "Alfred the Great"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Anglo-Saxon Chronicle (begun c. 890 CE under Alfred the Great, continued to 1154 CE) is the primary narrative source for Anglo-Saxon England — without it the history of English kings, the Viking invasions, the Danelaw, and the Norman Conquest would be far less recoverable. As a sustained prose narrative in Old English, it is also a foundational text of English literary history and a document of the transformation of the English language from Old to Middle English.",
      "significanceCategory": "highly-significant"
    }
  }
},

"argonautica": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782argonautica.json",
  "slug": "argonautica",
  "data": {
    "summary": "The Argonautica (Greek: Ἀργοναυτικά) is the epic poem of Apollonius of Rhodes (c. 295–215 BCE), written in four books and approximately 5,835 hexameter lines — the only surviving complete epic poem of the Hellenistic period, and a masterpiece of learned, self-conscious literary epic that stands between Homer and Virgil in the tradition of classical epic poetry. It retells the myth of Jason and the Argonauts — the Greek heroes who sailed on the ship Argo to Colchis (modern Georgia) at the eastern end of the Black Sea to retrieve the Golden Fleece — with elaborate psychological sophistication, Hellenistic erudition, and a remarkable innovation: the first truly developed romantic love story in Western epic poetry, in which Medea's passionate love for Jason drives the narrative of the second half of the poem.\n\nApollonius wrote the Argonautica at Alexandria as the director (or a prominent member) of the Library of Alexandria — the Hellenistic world's pre-eminent centre of scholarship — and the poem reflects both this scholarly environment and the Alexandrian literary aesthetic: it is densely allusive, incorporating hundreds of mythological, geographical, and aetiological digressions that demonstrate the poet's extraordinary erudition, and it is psychologically nuanced in a way that Homer's epics are not. The portrait of Medea in book 3 — her agonising internal conflict between her duty to her father and her overwhelming love for Jason, described in the first sustained psychological analysis of romantic passion in Western literature — is both the literary and emotional climax of the poem, and the direct model for Dido's passion for Aeneas in Virgil's Aeneid.\n\nThe Argonautica's influence on subsequent epic tradition is disproportionate to its relatively modest modern reception — Virgil's debt to Apollonius in the Aeneid (particularly the Dido/Aeneas story, which reverses the Medea/Jason dynamic) is fundamental, and through Virgil the Argonautica shaped the entire tradition of Western epic poetry from Ovid through Dante, Tasso, and Milton.",
    "causes": [
      "The Hellenistic literary culture of Alexandria — centred on the Library, with its vast collection of earlier Greek texts — created an environment of scholarly erudition and self-conscious literary competition in which the Argonautica's dense allusiveness, its reworking of earlier mythological variants, and its engagement with Homer were the defining aesthetic virtues.",
      "The Hellenistic period's shift in literary sensibility toward psychological realism, romantic emotion, and scholarly virtuosity — away from the communal, oral-derived epic of Homer — gave Apollonius the intellectual tools to create the Argonautica's greatest innovation: Medea's psychological portrait as the first extended analysis of romantic passion in Western epic.",
      "The mythological tradition of the Argonauts — one of the most ancient Greek heroic cycles, pre-dating Homer — provided Apollonius with a story rich in geography, mythology, and heroic narrative, but without a canonical poetic treatment, giving him freedom to innovate within the epic tradition."
    ],
    "effects": [
      "The Argonautica's portrait of Medea's love for Jason — the first sustained psychological analysis of romantic passion in Western epic — was the direct model for Virgil's Dido in the Aeneid (Books 1–4), which reversed the Medea/Jason dynamic and became the most influential love story in Western literature, shaping the Western conception of tragic romantic love.",
      "The Argonautica's geographical erudition — its systematic survey of the Black Sea, the Adriatic, the Danube, and other routes — reflected and contributed to the Alexandrian scholarly tradition's interest in geography, providing a poetic framework for the geographical knowledge accumulated by Eratosthenes and other Alexandrian geographers.",
      "The Argonautica's influence on the Western epic tradition — through Virgil's Aeneid, Ovid's Metamorphoses, and the later tradition — shaped the conventions of learned, allusive epic poetry from Latin antiquity through the Renaissance, establishing the model of the psychological epic hero whose quest is complicated by a tragic romantic entanglement."
    ],
    "relationships": [
      {"sourceSlug": "apollonius-of-rhodes", "sourceName": "Apollonius of Rhodes (c. 295–215 BCE)", "verb": "AUTHORS", "targetSlug": "argonautica", "targetName": "Argonautica (c. 270–245 BCE)", "context": "Apollonius wrote the Argonautica as director (or senior scholar) of the Library of Alexandria — his scholarly environment shaped the poem's extraordinary erudition and allusive density."},
      {"sourceSlug": "argonautica", "sourceName": "Argonautica", "verb": "INFLUENCES", "targetSlug": "aeneid", "targetName": "Virgil's Aeneid (Dido episode)", "context": "Virgil's portrait of Dido's fatal passion for Aeneas (Aeneid books 1–4) is directly modelled on Apollonius's Medea — reversing the gender dynamic and deepening the psychological tragedy, and through the Aeneid transmitting Apollonius's innovation to the entire Western literary tradition."},
      {"sourceSlug": "argonautica", "sourceName": "Argonautica", "verb": "ENGAGES_WITH", "targetSlug": "iliad", "targetName": "Homer's Iliad and Odyssey", "context": "The Argonautica is a self-conscious response to Homer — Apollonius's allusive engagement with Homeric language, scenes, and narrative patterns is constant, establishing the poem's Hellenistic aesthetic of learned reworking of the epic tradition."}
    ],
    "places": [
      {"name": "Alexandria, Ptolemaic Egypt (c. 270–245 BCE, composition)", "role": "The scholarly context of composition — Apollonius wrote at the Library of Alexandria, the Hellenistic world's greatest centre of learning"},
      {"name": "Greece, Black Sea, Colchis (narrative geography, mythological)", "role": "The geographic setting of the Argonautica — Jason's voyage from Iolcus in Thessaly through the Aegean, the Hellespont, the Black Sea, to Colchis (modern Georgia)"}
    ],
    "subjects": ["Greek Literature", "Classical Era", "Hellenism", "Epic Poetry", "Ancient Greece", "Mythology", "Alexandria", "World Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Argonautica (Apollonius of Rhodes, c. 270–245 BCE) is the only surviving complete Hellenistic epic and the foundational text of the Western tradition of learned, psychological epic poetry. Its portrait of Medea's love for Jason — the first sustained psychological analysis of romantic passion in Western epic — was the direct model for Virgil's Dido, and through the Aeneid it shaped the conventions of tragic romantic love in the entire subsequent Western literary tradition.",
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
