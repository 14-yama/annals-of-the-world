#!/usr/bin/env python3
"""
VS Code Enrichment Batch 65 — 8 Historical Figures
Sun Tzu, Michelangelo, Leonardo da Vinci, Paul the Apostle,
Francis of Assisi, Oliver Cromwell, Ho Chi Minh, Alexander the Great

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-65-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-65-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Sun Tzu ───────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/210sun-tzu.json",
        "slug": "sun-tzu",
        "era_correction": None,
        "data": {
            "summary": (
                "Sun Tzu (c. 544–496 BCE) was a Chinese military general, strategist, and philosopher whose The Art of War (Sunzi Bingfa) — written during the Spring and Autumn period — became the most influential military treatise in history, read by generals from Cao Cao to Napoleon, Mao Zedong to Norman Schwarzkopf, and applied beyond warfare to business, sports, politics, and martial arts. In 13 concise chapters (approximately 6,000 characters), he distilled the principles of strategy, intelligence, deception, and decisive action that define effective leadership in competitive environments.\n\n"
                "His core thesis — 'All warfare is based on deception' — inverted the Greek heroic model of frontal confrontation. Sun Tzu argued that the supreme excellence is to subdue the enemy without fighting; that victory comes from knowing yourself and knowing the enemy; that adaptability, speed, and intelligence defeat brute force. He wrote during the Warring States period's precursor when Chinese city-states competed intensely, and his 13 chapters were distilled from hard-won experience commanding forces for King Helü of Wu.\n\n"
                "His ideas influenced Chinese military thought for 2,500 years — Cao Cao wrote the first major commentary (c. 200 CE); Zhuge Liang applied them in the Three Kingdoms period; Mao Zedong cited him constantly in guerrilla warfare doctrine. Japanese samurai tradition absorbed the Art of War from the 8th century. The first European translation appeared in 1772 (Père Amiot, French), and Napoleon reportedly studied it.\n\n"
                "'Know your enemy, know yourself, and you need not fear the result of a hundred battles.' This single line encapsulates why the Art of War is studied not just in war colleges but in MBA programs and sports coaching manuals worldwide — its strategic logic transcends any particular competitive domain."
            ),
            "causes": [
                "Spring and Autumn period's interstate warfare creating demand for systematic military thought",
                "Chinese philosophical tradition's systematic analysis of natural patterns applied to conflict",
                "King Helü of Wu's patronage enabling practical command experience",
                "Warring States competition among Chinese states requiring strategic innovation",
            ],
            "effects": [
                "The Art of War — most influential military treatise in world history",
                "Chinese military tradition shaped for 2,500 years",
                "Japanese martial tradition — samurai strategy deeply influenced",
                "Mao Zedong's guerrilla warfare doctrine citing Sun Tzu",
                "Modern business strategy literature — 'boardroom battles' framed in Sun Tzu",
                "Napoleon's campaigns influenced by Art of War (via French translation)",
                "Global MBA curriculum — strategy courses regularly assign the Art of War",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "The Art of War", "targetSlug": "art-of-war", "note": "His sole surviving work — most-read military text in history"},
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Cited Sun Tzu constantly; People's Liberation Army doctrine is Sunzian"},
                {"type": "INFLUENCES", "target": "Cao Cao", "targetSlug": "cao-cao", "note": "First major Art of War commentator (c. 200 CE)"},
                {"type": "INFLUENCES", "target": "Zhuge Liang", "targetSlug": "zhuge-liang", "note": "Three Kingdoms strategist whose brilliance was compared to Sun Tzu"},
                {"type": "INFLUENCES", "target": "Napoleon Bonaparte", "targetSlug": "napoleon-bonaparte", "note": "Reportedly studied French translation of Art of War"},
                {"type": "INFLUENCES", "target": "Miyamoto Musashi", "targetSlug": "miyamoto-musashi", "note": "Book of Five Rings follows Sun Tzu's strategic philosophy"},
                {"type": "INFLUENCES", "target": "Clausewitz", "targetSlug": "carl-von-clausewitz", "note": "On War (1832) is the Western counterpart — similar abstract strategic principles"},
                {"type": "OCCURS_IN", "target": "China", "targetSlug": "china", "note": "Lived during Spring and Autumn period in the state of Wu"},
                {"type": "INFLUENCES", "target": "Warring States period", "targetSlug": "warring-states-period", "note": "His ideas formed in response to the interstate warfare of this era"},
                {"type": "INFLUENCES", "target": "Japanese martial arts", "targetSlug": "japanese-martial-arts", "note": "Art of War absorbed into Japanese military culture from 8th century CE"},
                {"type": "INFLUENCES", "target": "Confucius", "targetSlug": "confucius", "note": "Both lived in same Spring and Autumn period; offered contrasting human ideals"},
                {"type": "INFLUENCES", "target": "Ho Chi Minh", "targetSlug": "ho-chi-minh", "note": "Viet Minh guerrilla doctrine deeply informed by Sun Tzu via Mao"},
                {"type": "INFLUENCES", "target": "Norman Schwarzkopf", "targetSlug": "norman-schwarzkopf", "note": "Gulf War commander who cited Sun Tzu in planning"},
                {"type": "INFLUENCES", "target": "Business strategy", "targetSlug": "business-strategy", "note": "Art of War is standard text in business schools globally"},
                {"type": "INFLUENCES", "target": "King Helu of Wu", "targetSlug": "king-helu-of-wu", "note": "Patron who commissioned Sun Tzu to train his army"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Sun Tzu's Art of War has shaped military strategy across 2,500 years and all continents — from Chinese dynastic warfare to Maoist guerrilla tactics to US Army doctrine — while simultaneously becoming the most widely read strategy text in global business and leadership culture."
            },
            "quote": "'Know your enemy, know yourself, and you need not fear the result of a hundred battles.' — Sun Tzu, The Art of War",
            "places": ["State of Wu, China (military career)", "Qi, China (birthplace, disputed)"],
            "subjectHeadings": "Sun Tzu — Military Strategists — China — Classical",
            "subjects": ["China", "military strategy", "philosophy", "Classical era", "ancient world", "warfare", "Taoism", "East Asia", "leadership", "strategy"],
            "frameworks": ["state-formation", "intellectual-history", "technological-change"],
        }
    },

    # ── 2. Michelangelo ──────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/204-Class-204/204michelangelo.json",
        "slug": "michelangelo",
        "era_correction": None,
        "data": {
            "summary": (
                "Michelangelo di Lodovico Buonarroti Simoni (1475–1564) was an Italian sculptor, painter, architect, and poet of the High Renaissance whose works are among the most celebrated in Western art. The Sistine Chapel ceiling (1508–12), the sculpture of David (1501–04), the Pietà (1498–99), and the architectural design of St. Peter's Basilica dome define the cultural zenith of Renaissance achievement. As both Giorgio Vasari (his biographer) and his contemporaries recognized, Michelangelo represented the ideal of the artist as divine creator — a 'divine genius' transcending mere craft.\n\n"
                "Working in an era when sculpture was considered the supreme art, Michelangelo transformed marble with unprecedented technical mastery. His David (17 feet tall, 6 tons of Carrara marble) shows an ideal human figure with perfect anatomical accuracy and psychological intensity — a man on the verge of action rather than after it. His Pietà, completed when he was just 24, displays a Madonna holding the dead Christ with such technical perfection that witnesses refused to believe it was done by human hands. Both became icons of Western art.\n\n"
                "The Sistine Chapel ceiling commission (1508–12) was initially unwanted — Michelangelo considered himself a sculptor, not a painter. Over four years, lying on scaffolding, he painted 300 figures across 5,800 square feet, creating the most complex iconographic programme in Christian art. The Creation of Adam — God and Adam's fingers nearly touching — became the most reproduced image in art history.\n\n"
                "He lived to 88 (extraordinary for the Renaissance) and remained productive until his death. He was the first Western artist to have his biography published while still alive, and the first to be recognized universally in his own lifetime as the greatest artist who had ever lived — a position largely unchallenged 500 years later."
            ),
            "causes": [
                "Medici patronage in Florence providing training at the sculpture garden of San Marco",
                "Lorenzo de' Medici's humanist circle exposing him to classical philosophy",
                "Renaissance cultural belief in the individual artist's potential for transcendent achievement",
                "Papal commissions (Julius II) enabling the grandest artistic projects in history",
            ],
            "effects": [
                "Sistine Chapel ceiling — most complex iconographic program in Christian art",
                "David — the defining image of the idealized human form",
                "Pietà — technical perfection that made contemporaries refuse to believe human hands made it",
                "St. Peter's Basilica dome — architectural masterpiece still standing",
                "Raised the cultural status of visual artists from craftsmen to 'divine geniuses'",
                "High Renaissance aesthetic — the model all subsequent Western art responds to",
                "Mannerism — immediate successor style reacting against his perfection",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Lorenzo de' Medici", "targetSlug": "lorenzo-de-medici", "note": "Patron who recognized his genius and trained him in his household"},
                {"type": "INFLUENCES", "target": "Pope Julius II", "targetSlug": "pope-julius-ii", "note": "Papal patron who commissioned Sistine Chapel ceiling and tomb"},
                {"type": "INFLUENCES", "target": "Leonardo da Vinci", "targetSlug": "leonardo-da-vinci", "note": "Great rival and contemporary; competitive and contrasting genius"},
                {"type": "INFLUENCES", "target": "Raphael", "targetSlug": "raphael", "note": "Third great High Renaissance master; studied Michelangelo's ceiling"},
                {"type": "INFLUENCES", "target": "Giorgio Vasari", "targetSlug": "giorgio-vasari", "note": "Lives of the Artists biographer — Michelangelo was his living subject"},
                {"type": "INFLUENCES", "target": "Sistine Chapel", "targetSlug": "sistine-chapel", "note": "Ceiling (1508–12) and Last Judgement (1536–41) — his dual masterpieces"},
                {"type": "INFLUENCES", "target": "St. Peter's Basilica", "targetSlug": "st-peters-basilica", "note": "Designed the dome — architectural masterpiece of Rome"},
                {"type": "INFLUENCES", "target": "Donatello", "targetSlug": "donatello", "note": "Predecessor sculptor whose David inspired his own"},
                {"type": "INFLUENCES", "target": "Mannerism", "targetSlug": "mannerism", "note": "Artistic movement that followed by deliberately distorting his ideals"},
                {"type": "OCCURS_IN", "target": "Italy", "targetSlug": "italy", "note": "Born in Caprese; worked primarily in Florence and Rome"},
                {"type": "INFLUENCES", "target": "Baroque art", "targetSlug": "baroque-art", "note": "Baroque artists like Bernini inherited Michelangelo's dynamic energy"},
                {"type": "INFLUENCES", "target": "Neoclassicism", "targetSlug": "neoclassicism", "note": "Winckelmann's classical ideal was inspired by Michelangelo's sculptures"},
                {"type": "INFLUENCES", "target": "Botticelli", "targetSlug": "botticelli", "note": "Earlier Florentine contemporary in Medici circle"},
                {"type": "INFLUENCES", "target": "Dante Alighieri", "targetSlug": "dante-alighieri", "note": "Greatest influence on his poetry and much of his iconographic thought"},
                {"type": "INFLUENCES", "target": "Classical Greek sculpture", "targetSlug": "classical-greek-sculpture", "note": "Laocoön discovery (1506) directly influenced his sculptural language"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Michelangelo's Sistine Chapel ceiling, David, and Pietà set the aesthetic standard for Western art for 500 years, transformed the social status of the visual artist from craftsman to 'divine genius,' and created images so culturally dominant that the Creation of Adam became the most reproduced image in art history."
            },
            "quote": "'The sculpture is already complete within the marble block, before I start my work. It is already there — I just have to chisel away the superfluous material.' — attributed to Michelangelo",
            "places": ["Florence, Italy (training and David)", "Rome, Italy (Sistine Chapel, St. Peter's)", "Caprese, Italy (birthplace)"],
            "subjectHeadings": "Michelangelo — Artists and Architects — Italy — Early Modern",
            "subjects": ["Italy", "art", "Renaissance", "Early Modern era", "sculpture", "painting", "architecture", "Florence", "Rome", "Catholic Church"],
            "frameworks": ["artistic-cultural", "religious-thought", "intellectual-history"],
        }
    },

    # ── 3. Leonardo da Vinci ─────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/204-Class-204/204leonardo-da-vinci.json",
        "slug": "leonardo-da-vinci",
        "era_correction": None,
        "data": {
            "summary": (
                "Leonardo di ser Piero da Vinci (1452–1519) was an Italian polymath of the Renaissance — simultaneously one of the greatest painters who ever lived and the most broadly curious scientist-engineer of his age. His notebooks (c. 13,000 surviving pages) contain anatomical drawings of unmatched precision, designs for flying machines, helicopters, armored vehicles, solar power, and hydraulic machines, mathematical studies, geology, optics, and music — all produced 200–400 years before their realization. The Mona Lisa and The Last Supper are among the world's most recognized paintings.\n\n"
                "Born illegitimate in Vinci, Florence, he apprenticed with Andrea del Verrocchio, whose workshop taught him goldsmithing, sculpture, painting, and engineering. By his early twenties his skill surpassed his master's. His sfumato technique — blending tones without visible borders using layers of thin glaze — created the revolutionary atmospheric perspective and psychological depth of the Mona Lisa's smile and The Last Supper's emotional intensity.\n\n"
                "His anatomical drawings, made by dissecting over 30 human corpses, were scientifically ahead of published medicine and would have revolutionized anatomy if published. His engineering notebooks — flying machines, screw jack, ball bearings, armored car, double-hull ship — show a mind able to conceive mechanical solutions unbuilt for centuries. His hydrological studies of water flow, turbulence, and erosion were 20th-century science in 15th-century language.\n\n"
                "'Learning never exhausts the mind.' Leonardo embodied the Renaissance ideal of the uomo universale (universal man), but he was no mere Renaissance man — his scientific imagination was genuinely centuries ahead of his time, making him the most astonishing single intellect documented in the historical record."
            ),
            "causes": [
                "Florentine Renaissance patronage system enabling gifted craftsmen to reach full potential",
                "Verrocchio's workshop providing cross-disciplinary training in art and engineering",
                "Medici Florence's culture of intellectual cross-pollination across disciplines",
                "His own insatiable curiosity that rejected the boundaries between disciplines",
            ],
            "effects": [
                "Mona Lisa — most recognized and visited painting in history",
                "The Last Supper — defining image of Christian iconography",
                "Anatomical drawings — first scientifically accurate visual atlas of the human body",
                "Engineering notebooks — designed helicopter, armored car, solar power concept 400 years early",
                "Sfumato technique — revolutionized oil painting",
                "Renaissance ideal of universal genius — 'Leonardo' became the archetype",
                "Scientific illustration — his botanical and anatomical drawings set the standard",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Andrea del Verrocchio", "targetSlug": "andrea-del-verrocchio", "note": "Master who trained him; Leonardo reportedly surpassed him quickly"},
                {"type": "INFLUENCES", "target": "Michelangelo", "targetSlug": "michelangelo", "note": "Great rival — contrasting approaches to Renaissance idealism"},
                {"type": "INFLUENCES", "target": "Raphael", "targetSlug": "raphael", "note": "Younger contemporary deeply influenced by Leonardo's sfumato"},
                {"type": "INFLUENCES", "target": "Ludovico Sforza", "targetSlug": "ludovico-sforza", "note": "Milan patron for 18 years — commissioned The Last Supper"},
                {"type": "INFLUENCES", "target": "Francis I of France", "targetSlug": "francis-i-of-france", "note": "Final patron; Leonardo died at Amboise castle in France"},
                {"type": "INFLUENCES", "target": "Mona Lisa", "targetSlug": "mona-lisa", "note": "His most famous painting — most visited artwork in history"},
                {"type": "INFLUENCES", "target": "The Last Supper", "targetSlug": "last-supper-painting", "note": "Fresco at Santa Maria delle Grazie — defining Christian iconography"},
                {"type": "INFLUENCES", "target": "Vitruvian Man", "targetSlug": "vitruvian-man", "note": "Drawing symbolizing the Renaissance synthesis of art and science"},
                {"type": "INFLUENCES", "target": "Galileo Galilei", "targetSlug": "galileo-galilei", "note": "Leonardo's scientific notebooks influenced the Italian scientific tradition"},
                {"type": "OCCURS_IN", "target": "Italy", "targetSlug": "italy", "note": "Born Vinci; worked in Florence, Milan, Venice, Rome"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Last years at Amboise — brought Mona Lisa to France"},
                {"type": "INFLUENCES", "target": "Medici family", "targetSlug": "medici-family", "note": "Grew up in Florence during Medici cultural golden age"},
                {"type": "INFLUENCES", "target": "Human anatomy", "targetSlug": "human-anatomy", "note": "30+ corpse dissections produced unmatched anatomical illustrations"},
                {"type": "INFLUENCES", "target": "Flight", "targetSlug": "aviation", "note": "Designed ornithopter and aerial screw (helicopter concept) 400 years early"},
                {"type": "INFLUENCES", "target": "Renaissance humanism", "targetSlug": "renaissance-humanism", "note": "Embodied the uomo universale ideal at its fullest realization"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Leonardo da Vinci produced the most recognized painting in history (Mona Lisa), created anatomical drawings 400 years ahead of published medicine, designed machines not built until the 20th century, and embodied the Renaissance ideal of universal genius so completely that his name became the definition of human intellectual potential."
            },
            "quote": "'Learning never exhausts the mind.' — Leonardo da Vinci",
            "places": ["Florence, Italy (training and early work)", "Milan, Italy (18 years under Sforza)", "Rome, Italy (later career)", "Amboise, France (death, 1519)", "Vinci, Italy (birthplace)"],
            "subjectHeadings": "Leonardo da Vinci — Artists and Scientists — Italy — Early Modern",
            "subjects": ["Italy", "art", "science", "Renaissance", "Early Modern era", "engineering", "anatomy", "painting", "polymath", "innovation"],
            "frameworks": ["artistic-cultural", "scientific-revolution", "intellectual-history"],
        }
    },

    # ── 4. Paul the Apostle ──────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/252-Class-252/252paul-the-apostle.json",
        "slug": "paul-the-apostle",
        "era_correction": None,
        "data": {
            "summary": (
                "Paul of Tarsus (c. 5–67 CE) was a 1st-century Jewish-Roman citizen and Christian apostle who transformed Christianity from a Jewish sect into a universal world religion. His 13 letters (epistles) in the New Testament constitute the earliest Christian writings (predating the Gospels), defining the theology of grace, faith, and salvation that became Western Christianity's doctrinal foundation. More than any other person except Jesus himself, Paul determined what Christianity would become.\n\n"
                "Born Saul in Tarsus (modern Turkey), he was educated as a Pharisee in Jerusalem under Gamaliel and initially persecuted Christians zealously. His conversion on the road to Damascus (c. 33–36 CE) — a sudden blinding vision of the risen Jesus — transformed him into Christianity's most energetic missionary. Over three missionary journeys covering thousands of miles, he established churches in Antioch, Corinth, Ephesus, Philippi, Thessaloniki, and Rome — the backbone of the early church.\n\n"
                "His crucial theological innovation was removing the requirement for Gentile converts to follow Jewish law (circumcision, dietary restrictions), opening Christianity to the entire Greco-Roman world. His letter to the Romans — a systematic theology of grace, sin, and salvation — is the most theologically dense document in the New Testament. 'For by grace you have been saved through faith... not by works.' This line defined Western soteriology.\n\n"
                "He was executed in Rome (c. 67 CE) under Nero. His letters were collected and read widely before the Gospels were written — meaning Paul's theology shaped how the early church understood Jesus. His influence on Augustine, Luther, Calvin, and Wesley makes him the single most important theologian in Christian history."
            ),
            "causes": [
                "Jewish apocalyptic tradition preparing for a messianic age",
                "Dramatic Damascus road conversion transforming a persecutor into Christianity's greatest advocate",
                "Roman citizenship enabling travel throughout the Empire and legal protection",
                "Greco-Roman philosophical vocabulary (logos, pneuma) available to express Christian theology",
            ],
            "effects": [
                "13 Pauline epistles — earliest Christian writings; New Testament's theological core",
                "Christianity opened to Gentiles — removal of Jewish law requirements",
                "Universal church established across Mediterranean — Antioch, Corinth, Rome, Ephesus",
                "Grace theology (sola gratia) — foundational for Augustine, Luther, Calvin",
                "Romans 1–8 — most influential theological argument in Christian history",
                "Western soteriology: salvation by faith, not works",
                "Christian martyrdom — Paul's own execution became a model of witness",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Jesus Christ", "targetSlug": "jesus-christ", "note": "Encountered risen Jesus on Damascus road — foundation of his theology"},
                {"type": "INFLUENCES", "target": "Peter the Apostle", "targetSlug": "peter-the-apostle", "note": "Confronted Peter at Antioch over Gentile inclusion (Galatians 2)"},
                {"type": "INFLUENCES", "target": "Augustine of Hippo", "targetSlug": "augustine-of-hippo", "note": "Augustine's conversion mediated by Romans; grace theology inherited from Paul"},
                {"type": "INFLUENCES", "target": "Martin Luther", "targetSlug": "martin-luther", "note": "Luther's Reformation built on Paul's sola fide — justification by faith alone"},
                {"type": "INFLUENCES", "target": "John Calvin", "targetSlug": "john-calvin", "note": "Reformed theology's double predestination rooted in Pauline election doctrine"},
                {"type": "INFLUENCES", "target": "Letter to the Romans", "targetSlug": "epistle-to-the-romans", "note": "Paul's systematic theology — most influential document in Christian history"},
                {"type": "INFLUENCES", "target": "Barnabas", "targetSlug": "barnabas", "note": "First missionary partner who introduced Paul to the Jerusalem apostles"},
                {"type": "INFLUENCES", "target": "Luke the Evangelist", "targetSlug": "luke-the-evangelist", "note": "Travel companion who wrote Acts of the Apostles — primary Paul biography"},
                {"type": "INFLUENCES", "target": "Roman Empire", "targetSlug": "roman-empire", "note": "Used Roman road network to spread Christianity; executed under Nero"},
                {"type": "OCCURS_IN", "target": "Turkey", "targetSlug": "turkey", "note": "Born in Tarsus (modern Turkey); planted churches throughout Asia Minor"},
                {"type": "INFLUENCES", "target": "Corinthian church", "targetSlug": "church-of-corinth", "note": "Founded and corresponded with — 1 Corinthians 13 on love"},
                {"type": "INFLUENCES", "target": "Jerusalem Council (49 CE)", "targetSlug": "jerusalem-council", "note": "Defended Gentile Christians at landmark early church debate"},
                {"type": "INFLUENCES", "target": "John Wesley", "targetSlug": "john-wesley", "note": "Wesley's evangelical conversion at Aldersgate reading Paul on Romans"},
                {"type": "INFLUENCES", "target": "Karl Barth", "targetSlug": "karl-barth", "note": "Barth's 1919 Romans commentary launched 20th-century dialectical theology"},
                {"type": "INFLUENCES", "target": "Gamaliel", "targetSlug": "gamaliel", "note": "Pharisee teacher under whom Paul studied in Jerusalem"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Paul the Apostle transformed Christianity from a Jewish sect to a universal world religion by opening it to Gentiles; wrote the New Testament's earliest and most theologically formative documents; created the grace-faith soteriology that shaped Augustine, Luther, Calvin, and all Western Christianity — making him the most consequential single theologian in history."
            },
            "quote": "'For I am convinced that neither death nor life... nor anything else in all creation, will be able to separate us from the love of God.' — Romans 8:38–39",
            "places": ["Tarsus, Turkey (birthplace)", "Jerusalem, Israel (education)", "Damascus, Syria (conversion)", "Antioch, Turkey (mission base)", "Rome, Italy (martyrdom)"],
            "subjectHeadings": "Paul the Apostle — Religious Figures — Turkey/Israel — Classical",
            "subjects": ["Christianity", "theology", "Classical era", "Roman Empire", "Israel", "Turkey", "Bible", "New Testament", "missions", "grace"],
            "frameworks": ["religious-thought", "social-revolution", "intellectual-history"],
        }
    },

    # ── 5. Francis of Assisi ─────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/252-Class-252/252francis-of-assisi.json",
        "slug": "francis-of-assisi",
        "era_correction": None,
        "data": {
            "summary": (
                "Francis of Assisi (1181–1226) was an Italian Catholic friar and preacher who founded the Franciscan Order and is venerated as one of the most beloved figures in Christian history. Renouncing a wealthy merchant family to embrace radical poverty, he lived among lepers, preached to the poor, and reportedly even preached to birds — his Canticle of Brother Sun (1224) was among the first poems written in Italian and expressed his revolutionary vision of all creation as a family of God. Pope Francis took his name in 2013 — the most powerful tribute to his enduring inspiration.\n\n"
                "Born Giovanni di Pietro di Bernardone in Assisi (his father called him 'Francesco' — 'the Frenchman'), Francis lived a typical wealthy merchant son's life until his mid-twenties. A period of illness and imprisonment (during local warfare) triggered a conversion: he stripped off his fine clothes in Assisi's public square, renounced his inheritance, and committed himself to radical poverty and service to the poor. His early community attracted followers with his joyful, charismatic holiness.\n\n"
                "In 1219, during the Fifth Crusade, Francis walked into the enemy camp to meet Sultan Malik al-Kamil of Egypt — an act of unarmed dialogue completely at odds with crusading warfare. The Sultan received him courteously; the encounter became the first Christian-Muslim dialogue at the highest level. Francis received the stigmata (wounds corresponding to Christ's) in 1224 — the first historically attested stigmatist.\n\n"
                "The Franciscan Order he founded grew to become one of the largest in the Church. His legacy includes modern environmentalism (he is the patron saint of ecology), interfaith dialogue, Christian poverty movements, and Italian literature. His life inspired generations from Dante (who placed him in Paradiso) to Tolkien's hobbits ('elemental creatures of good')."
            ),
            "causes": [
                "Medieval Italy's economic stratification between wealthy merchants and the poor",
                "Illness and imprisonment triggering a spiritual conversion in his mid-twenties",
                "Cistercian reform movement emphasizing apostolic poverty creating space for new expressions",
                "Troubadour courtly love culture shaping his poetry and joyful spirituality",
            ],
            "effects": [
                "Franciscan Order — one of largest Catholic religious orders (300,000+ members)",
                "Radical poverty movement — challenge to Church wealth and corruption",
                "Canticle of Brother Sun — first major poem in Italian vernacular",
                "Interfaith dialogue — pioneered meeting with Muslim sultan during Crusades",
                "Stigmata — first historically attested case, deepening devotion to Christ's passion",
                "Environmental ethics — patron saint of ecology; inspired St. Francis Prayer",
                "Pope Francis (2013) — current pope named after him",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Pope Innocent III", "targetSlug": "pope-innocent-iii", "note": "Approved Franciscan rule and order verbally in 1209"},
                {"type": "INFLUENCES", "target": "Clare of Assisi", "targetSlug": "clare-of-assisi", "note": "Founded the Poor Clares (female Franciscans) under his guidance"},
                {"type": "INFLUENCES", "target": "Bonaventure", "targetSlug": "bonaventure", "note": "Franciscan theologian who systematized his spirituality"},
                {"type": "INFLUENCES", "target": "Sultan al-Kamil", "targetSlug": "sultan-al-kamil", "note": "Received Francis courteously during Fifth Crusade — historic dialogue"},
                {"type": "INFLUENCES", "target": "Jesus Christ", "targetSlug": "jesus-christ", "note": "Identified completely with Christ — received stigmata 1224"},
                {"type": "INFLUENCES", "target": "Dante Alighieri", "targetSlug": "dante-alighieri", "note": "Dante placed Francis in Paradiso as a sun among saints"},
                {"type": "INFLUENCES", "target": "Franciscan Order", "targetSlug": "franciscan-order", "note": "Founded c. 1209 — now one of largest Catholic religious orders"},
                {"type": "INFLUENCES", "target": "Pope Francis", "targetSlug": "pope-francis", "note": "Current pope took his name in 2013 — greatest modern tribute"},
                {"type": "INFLUENCES", "target": "Environmental ethics", "targetSlug": "environmental-ethics", "note": "Patron saint of ecology; Laudato Si (2015) by Pope Francis builds on him"},
                {"type": "OCCURS_IN", "target": "Italy", "targetSlug": "italy", "note": "Born, lived, and died in Assisi, Umbria, Italy"},
                {"type": "INFLUENCES", "target": "Italian literature", "targetSlug": "italian-literature", "note": "Canticle of Brother Sun is among first major Italian vernacular poems"},
                {"type": "INFLUENCES", "target": "Thomas Aquinas", "targetSlug": "thomas-aquinas", "note": "Dominican Scholasticism partly in dialogue with Franciscan spiritualism"},
                {"type": "INFLUENCES", "target": "Medieval poverty movements", "targetSlug": "medieval-poverty-movements", "note": "Inspired Waldensians, Humiliati, later Spiritual Franciscans"},
                {"type": "INFLUENCES", "target": "Martin Luther", "targetSlug": "martin-luther", "note": "Franciscan critique of Church wealth preceded and partly inspired Reformation"},
                {"type": "INFLUENCES", "target": "Christian mysticism", "targetSlug": "christian-mysticism", "note": "His experiential, affective spirituality shaped Western mystical tradition"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "continental",
                "significanceNarrative": "Francis of Assisi founded the largest Catholic religious order, pioneered Christian-Muslim dialogue during the Crusades, created one of the first Italian vernacular poems, pioneered the theology of radical poverty that prefigured Reformation critique of Church wealth, and remains so beloved 800 years later that the current pope took his name."
            },
            "quote": "'Start by doing what's necessary, then what's possible, and suddenly you are doing the impossible.' — attributed to Francis of Assisi",
            "places": ["Assisi, Italy (birthplace and home)", "Damietta, Egypt (meeting with Sultan al-Kamil)", "La Verna, Italy (received stigmata)"],
            "subjectHeadings": "Francis of Assisi — Religious Founders — Italy — Medieval",
            "subjects": ["Italy", "Christianity", "Medieval era", "Franciscans", "poverty", "ecology", "religion", "mysticism", "interfaith", "Italian literature"],
            "frameworks": ["religious-thought", "social-revolution", "liberation-theology"],
        }
    },

    # ── 6. Oliver Cromwell ───────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222oliver-cromwell.json",
        "slug": "oliver-cromwell",
        "era_correction": None,
        "data": {
            "summary": (
                "Oliver Cromwell (1599–1658) was the English soldier-statesman and Puritan leader who commanded Parliament's New Model Army during the English Civil War (1642–51), organized the trial and execution of King Charles I (January 30, 1649), and then ruled England as Lord Protector (1653–58) — the only period in English history without a monarch. His military campaigns in Ireland (1649–50) left a legacy of massacre and dispossession that shaped Irish history and identity for centuries.\n\n"
                "A middling Cambridgeshire gentleman with no military training, Cromwell proved himself a military genius through natural talent and religious conviction. His Ironsides cavalry — drilled to absolute discipline and motivated by Calvinist belief that they were doing God's work — transformed the Parliamentary forces. His victories at Marston Moor (1644) and Naseby (1645) were decisive; his later conquest of Scotland and Ireland was devastating.\n\n"
                "The execution of Charles I was the most radical act in European political history since antiquity — the first public trial and legal execution of a reigning monarch, establishing the principle that kings govern under law and can be held accountable. The precedent terrified European monarchs and inspired European republicans, directly influencing the French Revolution 140 years later.\n\n"
                "His legacy is fiercely contested: in England, a parliamentary democracy champion; in Ireland, a genocidal oppressor; in Puritan memory, a saint who built godly discipline; in royalist memory, a regicide tyrant. After his death, Charles II had his corpse exhumed and posthumously executed. Yet his fundamental achievement — establishing Parliament's sovereignty over the Crown — was confirmed by the Glorious Revolution of 1688 and endures in every Westminster parliamentary system."
            ),
            "causes": [
                "Charles I's insistence on divine-right monarchy conflicting with Parliamentary tradition",
                "Puritan religious movement providing Cromwell with ideology and motivation",
                "English Civil War's military demands revealing his exceptional military talent",
                "New Model Army's professional discipline enabling Parliamentary military superiority",
            ],
            "effects": [
                "Execution of Charles I (1649) — first legal trial and execution of a reigning monarch",
                "English Commonwealth — republic replacing monarchy",
                "Interregnum (1649–60) — only republic in English history",
                "New Model Army — model for professional standing armies",
                "Irish massacres (Drogheda, Wexford 1649) — generational wound in Irish history",
                "Glorious Revolution (1688) — his work confirmed by parliamentary supremacy",
                "Republican inspiration for French Revolution and American founders",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Charles I of England", "targetSlug": "charles-i-of-england", "note": "Defeated, tried, and executed him — January 30, 1649"},
                {"type": "INFLUENCES", "target": "Parliament of England", "targetSlug": "parliament-of-england", "note": "Led Parliamentary forces; established its supremacy over Crown"},
                {"type": "INFLUENCES", "target": "New Model Army", "targetSlug": "new-model-army", "note": "Designed and commanded the professional army that won the Civil War"},
                {"type": "INFLUENCES", "target": "John Milton", "targetSlug": "john-milton", "note": "Milton served as Cromwell's Latin Secretary and wrote in his defense"},
                {"type": "INFLUENCES", "target": "Charles II of England", "targetSlug": "charles-ii-of-england", "note": "Cromwell's successor was the restored king who had his corpse exhumed"},
                {"type": "INFLUENCES", "target": "Ireland", "targetSlug": "ireland", "note": "1649–50 campaigns — Drogheda and Wexford massacres remain in Irish memory"},
                {"type": "INFLUENCES", "target": "Glorious Revolution (1688)", "targetSlug": "glorious-revolution-1688", "note": "1688 confirmed his work by definitively subordinating Crown to Parliament"},
                {"type": "INFLUENCES", "target": "French Revolution", "targetSlug": "french-revolution", "note": "Execution of Charles I was the precedent — Louis XVI's trial followed its model"},
                {"type": "INFLUENCES", "target": "Puritanism", "targetSlug": "puritanism", "note": "His government institutionalized Puritan social and religious discipline"},
                {"type": "OCCURS_IN", "target": "England", "targetSlug": "england", "note": "Born Huntingdon; governed England 1649–58"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Locke's Two Treatises were direct responses to the debates Cromwell's era raised"},
                {"type": "INFLUENCES", "target": "Thomas Hobbes", "targetSlug": "thomas-hobbes", "note": "Leviathan (1651) written in direct response to Civil War chaos"},
                {"type": "INFLUENCES", "target": "Scotland", "targetSlug": "scotland", "note": "Conquered Scotland (1650–51) in union with England"},
                {"type": "INFLUENCES", "target": "Calvinist theology", "targetSlug": "calvinism", "note": "His conviction of being an instrument of God's will came from Calvinist predestination"},
                {"type": "INFLUENCES", "target": "American Revolution", "targetSlug": "american-revolution", "note": "American founders cited his precedent — Parliament over Crown"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Oliver Cromwell executed a reigning king, establishing the principle that monarchs govern under law — the precedent for the French Revolutionary execution of Louis XVI and the foundation of modern parliamentary democracy; his New Model Army became the template for professional standing armies; and his conquest of Ireland created a wound in British-Irish relations lasting to the present day."
            },
            "quote": "'Put your trust in God, my boys, but mind to keep your powder dry.' — attributed to Oliver Cromwell",
            "places": ["Huntingdon, England (birthplace)", "London, England (Parliament and rule)", "Dublin, Ireland (campaign headquarters)", "Westminster, London (death and burial)"],
            "subjectHeadings": "Oliver Cromwell — Statesmen and Military Leaders — England — Early Modern",
            "subjects": ["England", "military", "politics", "Early Modern era", "Puritanism", "Parliament", "Ireland", "republic", "English Civil War", "regicide"],
            "frameworks": ["state-formation", "religious-thought", "social-revolution"],
        }
    },

    # ── 7. Ho Chi Minh ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222ho-chi-minh.json",
        "slug": "ho-chi-minh",
        "era_correction": None,
        "data": {
            "summary": (
                "Ho Chi Minh (1890–1969) was a Vietnamese Communist revolutionary and statesman who founded the Democratic Republic of Vietnam (1945) and led the Viet Minh independence movement against French colonial rule and, later, American military intervention. His 30-year struggle — combining Marxist-Leninist ideology with Vietnamese nationalist sentiment, guerrilla warfare doctrine, and extraordinary personal charisma — made him the most consequential figure in Southeast Asian history and a defining figure of 20th-century anti-colonial struggle.\n\n"
                "Born Nguyen Sinh Cung in central Vietnam (French Indochina), he worked as a cook's assistant on French ships, then spent years in France, England, the Soviet Union, and China — absorbing Marxism, Vietnamese nationalist thought, and Maoist guerrilla strategy. He co-founded the French Communist Party in 1920, attended the Comintern in Moscow, and modeled himself on Lenin, Mao, and Vietnamese resistance heroes. His legendary ability to connect with peasants — eating simple food, wearing sandals made from rubber tires — made him genuinely beloved.\n\n"
                "His Declaration of Vietnamese Independence (September 2, 1945) — beginning with the words of America's own Declaration — was addressed partly to the Americans he hoped would support Vietnamese independence. Instead, with French colonialism returning and the Cold War beginning, the US backed France and eventually sent 500,000 troops. Ho Chi Minh died in 1969, six years before Saigon fell to North Vietnamese forces (1975).\n\n"
                "The Vietnam War cost 58,000 American lives and 2–3 million Vietnamese lives. It ended with the US's most humiliating military defeat and transformed American domestic politics, military strategy ('Vietnam syndrome'), and public trust in government. Ho Chi Minh City (formerly Saigon) bears his name."
            ),
            "causes": [
                "French colonial rule imposing exploitation on Vietnamese society",
                "World War I and Wilson's Fourteen Points inspiring anti-colonial nationalism",
                "Lenin's anti-imperialist theory providing ideological framework for resistance",
                "Mao's Long March and guerrilla warfare strategy offering a military template",
            ],
            "effects": [
                "Democratic Republic of Vietnam (1945) — first Vietnamese state in a century",
                "First Indochina War (1946–54) — defeat of French colonial power at Dien Bien Phu",
                "Geneva Accords (1954) — division of Vietnam at 17th parallel",
                "Vietnam War (1955–75) — defining conflict of Cold War and American 20th century",
                "Fall of Saigon (1975) — US's greatest military defeat",
                "Unified Socialist Republic of Vietnam",
                "Domino theory, Vietnam syndrome — shaped US foreign policy for decades",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Viet Minh", "targetSlug": "viet-minh", "note": "Founded and led the Viet Minh independence movement (1941)"},
                {"type": "INFLUENCES", "target": "Vo Nguyen Giap", "targetSlug": "vo-nguyen-giap", "note": "His brilliant general who won Dien Bien Phu and commanded vs. US"},
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Key ally and model — Chinese weapons and guerrilla doctrine crucial"},
                {"type": "INFLUENCES", "target": "Lenin", "targetSlug": "vladimir-lenin", "note": "Lenin's anti-imperialism was the primary ideological inspiration"},
                {"type": "INFLUENCES", "target": "Vietnam War", "targetSlug": "vietnam-war", "note": "His war — he died 1969, 6 years before North Vietnamese victory"},
                {"type": "INFLUENCES", "target": "Sun Tzu", "targetSlug": "sun-tzu", "note": "Art of War embedded in Vietnamese guerrilla strategy via Chinese tradition"},
                {"type": "INFLUENCES", "target": "Dwight D. Eisenhower", "targetSlug": "dwight-eisenhower", "note": "US president who first committed advisors to South Vietnam"},
                {"type": "INFLUENCES", "target": "John F. Kennedy", "targetSlug": "john-f-kennedy", "note": "Escalated US military presence in Vietnam"},
                {"type": "INFLUENCES", "target": "Lyndon B. Johnson", "targetSlug": "lyndon-b-johnson", "note": "Escalated to 500,000 US troops — the full Vietnam War"},
                {"type": "OCCURS_IN", "target": "Vietnam", "targetSlug": "vietnam", "note": "Born Kim Lien; founded DRV; died in Hanoi 1969"},
                {"type": "INFLUENCES", "target": "French Communist Party", "targetSlug": "french-communist-party", "note": "Co-founded in 1920 at Tours Congress"},
                {"type": "INFLUENCES", "target": "Anti-colonial movements", "targetSlug": "anti-colonial-movements", "note": "Inspired independence movements across Southeast Asia and Africa"},
                {"type": "INFLUENCES", "target": "Cuba", "targetSlug": "cuba", "note": "Castro and Guevara saw Vietnam War as model of guerrilla anti-imperialism"},
                {"type": "INFLUENCES", "target": "Che Guevara", "targetSlug": "che-guevara", "note": "Vietnamese success inspired Guevara's global guerrilla strategy"},
                {"type": "INFLUENCES", "target": "Dien Bien Phu (1954)", "targetSlug": "battle-of-dien-bien-phu", "note": "Decisive French defeat that ended colonialism in Indochina"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Ho Chi Minh defeated both French colonialism and American military power — the only leader of a Third World country to defeat the United States in war — making his victory the defining event of the anti-colonial 20th century and transforming US domestic politics, military strategy, and public trust in government for generations."
            },
            "quote": "'Nothing is more precious than independence and freedom.' — Ho Chi Minh",
            "places": ["Hanoi, Vietnam (capital)", "Kim Lien, Vietnam (birthplace)", "Paris, France (political formation)", "Moscow, USSR (Comintern training)"],
            "subjectHeadings": "Ho Chi Minh — Revolutionary Leaders — Vietnam — Contemporary",
            "subjects": ["Vietnam", "communism", "anti-colonialism", "Contemporary era", "Cold War", "guerrilla warfare", "Vietnam War", "Southeast Asia", "nationalism", "revolution"],
            "frameworks": ["state-formation", "social-revolution", "liberation-theology"],
        }
    },

    # ── 8. Alexander the Great ───────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221alexander-the-great.json",
        "slug": "alexander-the-great",
        "era_correction": None,
        "data": {
            "summary": (
                "Alexander III of Macedon (356–323 BCE), universally known as Alexander the Great, created the largest empire in ancient history at 23 years of age and conquered a territory stretching from Greece to northwestern India — approximately 2 million square miles — in just 13 years of continuous campaigning. Never defeated in battle, he transformed the ancient world's political geography, spread Greek culture (Hellenism) across the Near East, Egypt, Persia, and Central Asia, and founded approximately 20 cities bearing his name, including Alexandria in Egypt, which became the world's greatest center of learning.\n\n"
                "Tutored by Aristotle from ages 13–16, Alexander was prepared philosophically and intellectually for the role. His father Philip II had already unified Greece; Alexander inherited both a superb army (the Macedonian phalanx) and a vision of Persian conquest. His campaign began in 334 BCE with the crossing of the Hellespont. He defeated Darius III three times — Granicus (334), Issus (333), and Gaugamela (331) — each time with forces smaller than the Persian army. The conquest of Persepolis (330), administrative capital of the Achaemenid Empire, symbolized the fall of the ancient Near Eastern order.\n\n"
                "In Egypt he was acclaimed pharaoh and visited the oracle of Ammon (Siwa), where he was reportedly told he was the son of the god. He pushed east into Bactria (Afghanistan), married the Bactrian princess Roxana (327), and crossed the Hindu Kush into India, winning at the Hydaspes River (326) against war elephants before his exhausted troops refused to go further. He died in Babylon at 32, his empire immediately fracturing among the Diadochi (successors).\n\n"
                "His lasting legacy was cultural: Hellenism — the fusion of Greek and Eastern civilization — became the dominant cultural matrix of the ancient world from the Mediterranean to India, providing the cultural medium in which early Christianity and rabbinic Judaism took shape."
            ),
            "causes": [
                "Philip II's unification of Macedonia and Greece creating the platform for eastern conquest",
                "Aristotle's tutoring providing philosophical and scientific preparation",
                "Persian Empire's administrative fragility after internal succession disputes",
                "Greek military innovation — Macedonian phalanx and combined-arms tactics",
            ],
            "effects": [
                "Largest ancient empire — 2 million square miles from Greece to India",
                "Hellenism — Greek cultural spread across Near East, Egypt, Persia, Central Asia",
                "Alexandria, Egypt — greatest center of ancient learning (Library of Alexandria)",
                "Diadochi Wars — 40+ years of successor state conflict reshaping the ancient world",
                "Seleucid, Ptolemaic, Antigonid dynasties — endured centuries after his death",
                "Greek as lingua franca — medium for early Christianity and ancient Judaism",
                "Silk Road routes — opened by his conquests linking East and West",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Aristotle", "targetSlug": "aristotle", "note": "Personal tutor for 3 years — philosophical foundation for leadership"},
                {"type": "INFLUENCES", "target": "Philip II of Macedon", "targetSlug": "philip-ii-of-macedon", "note": "Father who built the army and unified Greece — Alexander's inheritance"},
                {"type": "INFLUENCES", "target": "Darius III", "targetSlug": "darius-iii", "note": "Persian Great King defeated at Granicus, Issus, and Gaugamela"},
                {"type": "INFLUENCES", "target": "Ptolemy I", "targetSlug": "ptolemy-i", "note": "Childhood friend who ruled Egypt after his death — founded Ptolemaic dynasty"},
                {"type": "INFLUENCES", "target": "Seleucus I", "targetSlug": "seleucus-i", "note": "General who ruled the eastern empire — Seleucid dynasty (including Persia/Mesopotamia)"},
                {"type": "INFLUENCES", "target": "Hephaestion", "targetSlug": "hephaestion", "note": "Closest companion and general; Alexander mourned his death like Achilles for Patroclus"},
                {"type": "INFLUENCES", "target": "Alexandria, Egypt", "targetSlug": "alexandria-egypt", "note": "Greatest of his 20 eponymous cities — became Library of Alexandria's home"},
                {"type": "INFLUENCES", "target": "Hellenism", "targetSlug": "hellenism", "note": "Greek cultural spread he enabled — dominated ancient world for centuries"},
                {"type": "INFLUENCES", "target": "Julius Caesar", "targetSlug": "julius-caesar", "note": "Caesar wept before Alexander's statue — yearned to match his achievement"},
                {"type": "OCCURS_IN", "target": "Greece", "targetSlug": "greece", "note": "Born in Pella, Macedonia; inherited Greek hegemony"},
                {"type": "OCCURS_IN", "target": "Egypt", "targetSlug": "egypt", "note": "Conquered 332 BCE; founded Alexandria; proclaimed pharaoh"},
                {"type": "INFLUENCES", "target": "Achaemenid Persian Empire", "targetSlug": "achaemenid-empire", "note": "Conquered and ended the Achaemenid Empire (550–330 BCE)"},
                {"type": "INFLUENCES", "target": "Buddhism", "targetSlug": "buddhism", "note": "His Bactrian-Indian campaigns created first contact between Greek and Buddhist civilizations"},
                {"type": "INFLUENCES", "target": "Napoleon Bonaparte", "targetSlug": "napoleon-bonaparte", "note": "Napoleon modeled himself on Alexander — studying his campaigns obsessively"},
                {"type": "INFLUENCES", "target": "Cynicism", "targetSlug": "cynicism", "note": "Allegedly met Diogenes the Cynic; reportedly said 'Were I not Alexander, I would be Diogenes'"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Alexander the Great created the world's largest ancient empire in 13 years, spread Greek civilization (Hellenism) from Egypt to India — creating the cultural medium in which Christianity and rabbinic Judaism took shape — founded Alexandria which became antiquity's greatest center of learning, and set the template for world-conquest that Caesar, Napoleon, and countless others consciously followed."
            },
            "quote": "'I am not afraid of an army of lions led by a sheep; I am afraid of an army of sheep led by a lion.' — attributed to Alexander the Great",
            "places": ["Pella, Macedonia, Greece (birthplace)", "Babylon, Iraq (death 323 BCE)", "Alexandria, Egypt (founded)", "Persepolis, Iran (conquered)", "Taxila, Pakistan (eastern frontier)"],
            "subjectHeadings": "Alexander the Great — Military Leaders and Rulers — Greece/Macedonia — Classical",
            "subjects": ["Greece", "Macedonia", "empire", "Classical era", "Hellenism", "military", "ancient world", "Egypt", "Persia", "conquest"],
            "frameworks": ["state-formation", "cultural-exchange", "intellectual-history"],
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

    print(f"Batch 65 enrichment — {len(ENRICHMENTS)} entities\n")

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
