#!/usr/bin/env python3
"""
VS Code Enrichment Batch 60 — 8 Major Historical Persons
Thomas Hobbes, Ada Lovelace, Francis Bacon, Fyodor Dostoevsky,
John Calvin, Suleiman the Magnificent, Joseph Stalin, Rembrandt

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-60-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-60-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Thomas Hobbes ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/202-Class-202/202thomas-hobbes.json",
        "slug": "thomas-hobbes",
        "era_correction": None,
        "data": {
            "summary": (
                "Thomas Hobbes (1588–1679) was an English philosopher and political theorist whose Leviathan (1651) is one of the most influential works in the history of political philosophy, providing the first systematic secular justification for sovereign political authority. Writing during the chaos of the English Civil War, Hobbes argued that without government, human life would be 'solitary, poor, nasty, brutish, and short' — one of the most quoted phrases in Western thought.\n\n"
                "Hobbes' social contract theory held that rational individuals in a dangerous 'state of nature' would voluntarily surrender their natural freedoms to a sovereign power in exchange for security and order. Unlike later theorists (Locke, Rousseau), his sovereign was virtually absolute — the price of peace. This framework, while contested, established the terms of political philosophy for three centuries.\n\n"
                "Hobbes was also a pioneering materialist philosopher: he argued that all human thought was ultimately physical motion in the brain, anticipating modern cognitive science. His scientific friendships with Francis Bacon and Galileo and his geometric method of reasoning placed him firmly in the scientific revolution. His geometry of politics — deriving political obligations from first principles — was deeply original.\n\n"
                "Condemned by both Royalists and Parliamentarians, and threatened with prosecution for heresy, he survived to 91. His secular state theory divorced political authority from divine right, making him a foundational figure of modern liberalism, realism in international relations, and the English-speaking political tradition."
            ),
            "causes": [
                "English Civil War (1642–1651) creating the chaos his theory was designed to solve",
                "Scientific Revolution (Galileo, Bacon) inspiring geometric method in philosophy",
                "Thucydides' History (which Hobbes translated) showing politics as power without morality",
                "Religious wars of 16th–17th centuries demonstrating dangers of divided sovereignty",
            ],
            "effects": [
                "Leviathan (1651) — founding text of modern political philosophy",
                "Social contract theory establishing secular basis for political authority",
                "Materialist philosophy anticipating modern psychology and cognitive science",
                "Realist tradition in international relations theory (anarchy of state of nature)",
                "Separation of political authority from divine right",
                "Influence on John Locke, Rousseau, and all subsequent social contract theory",
                "Secularization of political thought in English-speaking tradition",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Leviathan (1651)", "targetSlug": "leviathan-hobbes", "note": "His masterwork on political philosophy"},
                {"type": "INFLUENCES", "target": "Social contract theory", "targetSlug": "social-contract-theory", "note": "Originator of modern social contract"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Responded to and modified Hobbesian social contract"},
                {"type": "INFLUENCES", "target": "Jean-Jacques Rousseau", "targetSlug": "jean-jacques-rousseau", "note": "Rousseau's state of nature inverts Hobbes"},
                {"type": "INFLUENCES", "target": "Francis Bacon", "targetSlug": "francis-bacon", "note": "Served as Bacon's secretary; influenced by empiricism"},
                {"type": "INFLUENCES", "target": "Galileo Galilei", "targetSlug": "galileo-galilei", "note": "Met in Florence; influenced by geometric method"},
                {"type": "INFLUENCES", "target": "English Civil War", "targetSlug": "english-civil-war", "note": "Context shaping his argument for sovereign order"},
                {"type": "INFLUENCES", "target": "International relations realism", "targetSlug": "international-relations-realism", "note": "State of nature = anarchy between states"},
                {"type": "INFLUENCES", "target": "Immanuel Kant", "targetSlug": "immanuel-kant", "note": "Kant's political philosophy responds to Hobbesian problem"},
                {"type": "INFLUENCES", "target": "Thucydides", "targetSlug": "thucydides", "note": "Translated Thucydides; deeply influenced by realist politics"},
                {"type": "OCCURS_IN", "target": "England", "targetSlug": "england", "note": "Primary country of activity"},
                {"type": "INFLUENCES", "target": "Materialist philosophy", "targetSlug": "philosophical-materialism", "note": "All thought is physical motion — systematic materialism"},
                {"type": "INFLUENCES", "target": "Secularism", "targetSlug": "secularism", "note": "Divorced political authority from divine sanction"},
                {"type": "INFLUENCES", "target": "Charles II", "targetSlug": "charles-ii-of-england", "note": "Granted royal protection despite religious controversies"},
                {"type": "INFLUENCES", "target": "Carl Schmitt", "targetSlug": "carl-schmitt", "note": "20th-century political theorist who invoked Hobbes for sovereignty"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Thomas Hobbes' Leviathan provided the first secular justification for sovereign political authority and established the social contract as the foundation of political philosophy — his realist view of human nature still drives debates in political theory, international relations, and jurisprudence."
            },
            "quote": "'The condition of man... is a condition of war of every one against every one.' — Thomas Hobbes, Leviathan (1651)",
            "places": ["London, England", "Paris, France (exile)", "Malmesbury, England (birthplace)"],
            "subjectHeadings": "Thomas Hobbes — Philosophers and Political Theorists — England — Early Modern",
            "subjects": ["England", "political philosophy", "social contract", "Enlightenment", "sovereignty", "English Civil War", "materialism", "secularism", "international relations", "17th century"],
            "frameworks": ["political-philosophy", "enlightenment", "social-theory"],
        }
    },

    # ── 2. Ada Lovelace ──────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/204-Class-204/204ada-lovelace.json",
        "slug": "ada-lovelace",
        "era_correction": None,
        "data": {
            "summary": (
                "Ada Lovelace (1815–1852) was a British mathematician and writer who is widely regarded as the world's first computer programmer, having written the first published algorithm intended to be processed by a machine — Charles Babbage's never-built Analytical Engine — in 1843. Daughter of the poet Lord Byron and the mathematically gifted Annabella Milbanke, she combined her father's creative vision with her mother's scientific rigor in a uniquely prophetic way.\n\n"
                "Lovelace's contribution appeared as footnotes to her translation of Luigi Menabrea's article on Babbage's Analytical Engine — but her notes were three times longer than the original article. Note G contains the first published algorithm: a step-by-step procedure for calculating Bernoulli numbers on the machine, recognizable to modern programmers as a loop with a conditional branch. More remarkably, she grasped that the Engine could manipulate any symbols, not just numbers — that it could compose music, handle language, and process any logical operation.\n\n"
                "Her visionary insight — that machines could go beyond mere calculation to process symbols according to rules — anticipated Alan Turing's concept of the universal computing machine by nearly a century. She foresaw machine intelligence while Babbage himself did not; he called her 'the Enchantress of Number.'\n\n"
                "She died of uterine cancer at 36, her work forgotten for a century. The US Department of Defense named its Ada programming language (1980) after her. Her work is now recognized as the founding document of software engineering."
            ),
            "causes": [
                "Charles Babbage's Analytical Engine — the programmable mechanical computer she analyzed",
                "Mathematical education by her mother Annabella Milbanke countering Byron's poetic legacy",
                "Mary Somerville's mentorship connecting her to the London scientific community",
                "Luigi Menabrea's Sketch of the Analytical Engine providing text for her translation",
            ],
            "effects": [
                "First published algorithm (Note G, 1843) — the founding document of software",
                "First recognition that computers could process any symbols, not just numbers",
                "Anticipation of Turing's universal computing machine by 90 years",
                "Ada programming language (DoD, 1980) named in her honor",
                "Pioneer of women in mathematics and computing",
                "Modern recognition as 'the first programmer' and software engineering foremother",
                "Annual Ada Lovelace Day celebrating women in STEM",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Charles Babbage", "targetSlug": "charles-babbage", "note": "Analytical Engine inventor; called her 'the Enchantress of Number'"},
                {"type": "INFLUENCES", "target": "Algorithm (concept)", "targetSlug": "algorithm", "note": "Published first known algorithm (1843)"},
                {"type": "INFLUENCES", "target": "Alan Turing", "targetSlug": "alan-turing", "note": "Her vision of symbol-processing anticipated Turing machines"},
                {"type": "INFLUENCES", "target": "Ada programming language", "targetSlug": "ada-programming-language", "note": "US DoD named the language in her honor (1980)"},
                {"type": "INFLUENCES", "target": "Computer science", "targetSlug": "computer-science", "note": "Founding figure of software engineering"},
                {"type": "INFLUENCES", "target": "Mary Somerville", "targetSlug": "mary-somerville", "note": "Scientific mentor who introduced her to Babbage"},
                {"type": "INFLUENCES", "target": "Lord Byron", "targetSlug": "lord-byron", "note": "Father — she never knew him; his poetic imagination she inherited"},
                {"type": "INFLUENCES", "target": "Women in science", "targetSlug": "women-in-science", "note": "Pioneer for women in mathematics and computing"},
                {"type": "OCCURS_IN", "target": "England", "targetSlug": "england", "note": "Lifelong English mathematician"},
                {"type": "INFLUENCES", "target": "Artificial intelligence", "targetSlug": "artificial-intelligence", "note": "First to articulate that machines could simulate thought"},
                {"type": "INFLUENCES", "target": "Industrial Revolution", "targetSlug": "industrial-revolution", "note": "Worked during Britain's first age of mechanization"},
                {"type": "INFLUENCES", "target": "Software engineering", "targetSlug": "software-engineering", "note": "Her algorithm is the origin point of the discipline"},
                {"type": "INFLUENCES", "target": "Bernoulli numbers", "targetSlug": "bernoulli-numbers", "note": "Her algorithm computed Bernoulli numbers"},
                {"type": "INFLUENCES", "target": "George Boole", "targetSlug": "george-boole", "note": "Contemporary mathematician whose Boolean logic enables computing"},
                {"type": "INFLUENCES", "target": "Victorian science", "targetSlug": "victorian-science", "note": "Active in peak era of British scientific advance"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Ada Lovelace wrote the world's first computer algorithm in 1843, recognized that machines could process any symbols — not just numbers — and anticipated the universal computer by 90 years, making her the founding figure of software engineering and a pioneer of women in STEM."
            },
            "quote": "'The Analytical Engine weaves algebraical patterns just as the Jacquard loom weaves flowers and leaves.' — Ada Lovelace (1843)",
            "places": ["London, England", "Horsley Towers, Surrey", "Kirkby Mallory, England (birthplace)"],
            "subjectHeadings": "Ada Lovelace — Mathematicians and Computer Scientists — England — Modern",
            "subjects": ["England", "computing", "mathematics", "algorithm", "Analytical Engine", "women in STEM", "Victorian era", "programming", "computer science", "artificial intelligence"],
            "frameworks": ["technological-change", "feminist-history", "scientific-revolution"],
        }
    },

    # ── 3. Francis Bacon ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/205-Class-205/205francis-bacon.json",
        "slug": "francis-bacon",
        "era_correction": None,
        "data": {
            "summary": (
                "Francis Bacon (1561–1626) was an English philosopher, statesman, and essayist who is credited as the father of empiricism and the scientific method. His Novum Organum (1620) proposed replacing Aristotelian deductive logic with inductive reasoning from observation and experiment — a radical reform of how humans produce knowledge that helped launch the Scientific Revolution and shaped the methods of modern science.\n\n"
                "Bacon's 'Great Instauration' (renewal of the sciences) argued that humanity had been held back by four 'Idols' — errors of perception, language, culture, and authority — that prevented clear thinking. His solution was systematic observation, controlled experiment, and inductive generalization: the scientific method as we practice it today. He was the first philosopher to argue that science should be organized, funded by the state, and directed toward practical human improvement.\n\n"
                "As Lord Chancellor of England under James I, he rose to the highest judicial office before being convicted of bribery (1621), ending his political career. His Essays (1597, expanded 1625) — terse, worldly, and psychologically acute observations on ambition, friendship, truth, and power — remain among the most read works of English prose.\n\n"
                "Though he performed few experiments himself, Bacon's influence on the founding of the Royal Society (1660) and the Enlightenment was profound. 'Knowledge is power' — the phrase most associated with him — expresses his core conviction that science is not contemplation but a tool for mastering nature and improving human life."
            ),
            "causes": [
                "Aristotelian scholasticism's dominance in European universities preventing empirical advance",
                "Renaissance humanism's recovery of classical texts opening space for critical philosophy",
                "English court culture under Elizabeth I and James I requiring practical statecraft",
                "Paracelsus and Vesalius pioneering empirical observation in medicine and anatomy",
            ],
            "effects": [
                "Novum Organum (1620) — manifesto of inductive scientific method",
                "Empiricism as philosophy — foundation of Locke, Hume, and British philosophy",
                "Royal Society of London (1660) directly inspired by Baconian program",
                "Scientific Revolution — organized, experimental science in place of scholasticism",
                "Essays (1597) — landmark of English prose literature",
                "'Knowledge is power' — articulation of science as technological mastery",
                "Utopian vision in New Atlantis of state-funded research institution",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Novum Organum (1620)", "targetSlug": "novum-organum", "note": "His manifesto of empirical inductive method"},
                {"type": "INFLUENCES", "target": "Scientific method", "targetSlug": "scientific-method", "note": "Founding theorist of empirical inductive science"},
                {"type": "INFLUENCES", "target": "Royal Society", "targetSlug": "royal-society", "note": "Directly inspired by Bacon's Salomon's House in New Atlantis"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Locke's empiricism built directly on Bacon's framework"},
                {"type": "INFLUENCES", "target": "Thomas Hobbes", "targetSlug": "thomas-hobbes", "note": "Hobbes served as Bacon's secretary"},
                {"type": "INFLUENCES", "target": "Isaac Newton", "targetSlug": "isaac-newton", "note": "Newtonian science practiced Baconian inductive method"},
                {"type": "INFLUENCES", "target": "Scientific Revolution", "targetSlug": "scientific-revolution", "note": "Provided philosophical program for organized science"},
                {"type": "INFLUENCES", "target": "Enlightenment", "targetSlug": "enlightenment", "note": "Baconian empiricism foundational to Enlightenment thought"},
                {"type": "INFLUENCES", "target": "René Descartes", "targetSlug": "rene-descartes", "note": "Parallel founder of scientific method (rationalism vs. empiricism)"},
                {"type": "OCCURS_IN", "target": "England", "targetSlug": "england", "note": "Lifelong English statesman and philosopher"},
                {"type": "INFLUENCES", "target": "James I of England", "targetSlug": "james-i-of-england", "note": "Patron and employer as Lord Chancellor"},
                {"type": "INFLUENCES", "target": "New Atlantis (1627)", "targetSlug": "new-atlantis-bacon", "note": "Utopian vision of state-funded research institution"},
                {"type": "INFLUENCES", "target": "David Hume", "targetSlug": "david-hume", "note": "Hume's empiricism and inductive skepticism developed Bacon's program"},
                {"type": "INFLUENCES", "target": "Voltaire", "targetSlug": "voltaire", "note": "Voltaire called Bacon 'the father of experimental philosophy'"},
                {"type": "INFLUENCES", "target": "Aristotle", "targetSlug": "aristotle", "note": "Bacon directly contested Aristotelian deductive syllogism"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Francis Bacon invented the modern scientific method — his call for inductive reasoning from experiment rather than Aristotelian deduction launched the Scientific Revolution, inspired the Royal Society, and established the philosophical foundation of all modern empirical science."
            },
            "quote": "'Knowledge is power.' — Francis Bacon, Meditationes Sacrae (1597)",
            "places": ["London, England", "York House, London (birthplace)", "Gray's Inn, London"],
            "subjectHeadings": "Francis Bacon — Philosophers and Scientists — England — Early Modern",
            "subjects": ["England", "scientific method", "empiricism", "philosophy", "Scientific Revolution", "Enlightenment", "Royal Society", "inductive reasoning", "statecraft", "17th century"],
            "frameworks": ["scientific-revolution", "enlightenment", "intellectual-history"],
        }
    },

    # ── 4. Fyodor Dostoevsky ─────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/260-Class-260/260fyodor-dostoevsky.json",
        "slug": "fyodor-dostoevsky",
        "era_correction": None,
        "data": {
            "summary": (
                "Fyodor Dostoevsky (1821–1881) was a Russian novelist and thinker whose works — Crime and Punishment (1866), The Idiot (1869), Demons (1872), and The Brothers Karamazov (1880) — represent the summit of psychological realism in world literature and the most profound exploration of guilt, redemption, suffering, and faith in the 19th century. Sigmund Freud called The Brothers Karamazov 'the most magnificent novel ever written.'\n\n"
                "Dostoevsky's biography was as dramatic as his fiction. Arrested for revolutionary activity (1849), he faced a mock execution — soldiers took aim before his reprieve arrived — and spent four years in a Siberian labor camp followed by forced military service. This near-death experience and the suffering of imprisonment transformed him from a liberal idealist into a conservative Christian thinker who believed that suffering was spiritually redemptive.\n\n"
                "His great novels explore the extreme states of the human psyche — murderers justifying their crimes on philosophical grounds (Raskolnikov in Crime and Punishment), saints confronted with evil (Myshkin in The Idiot), nihilists pursuing destruction to its logical end (Demons), and the problem of evil confronting faith (Ivan's 'Grand Inquisitor' in The Brothers Karamazov). His polyphonic narrative technique — multiple competing voices without authorial resolution — was identified by Mikhail Bakhtin as the defining innovation of the modern novel.\n\n"
                "Nietzsche, Kafka, Freud, Camus, and virtually every 20th-century novelist of conscience acknowledged Dostoevsky as a foundational influence."
            ),
            "causes": [
                "Mock execution and Siberian imprisonment (1849–1854) transforming his worldview",
                "Russian Nihilism and revolutionary movements providing intellectual targets",
                "Orthodox Christian tradition of spiritual suffering as redemption",
                "Gogol's literary tradition and Pushkin's psychological depth as Russian precursors",
            ],
            "effects": [
                "Crime and Punishment (1866) — foundational text of psychological realism",
                "The Brothers Karamazov (1880) — the 'Grand Inquisitor' chapter defines existentialist debate on God",
                "Polyphonic novel technique — Bakhtin's theory of the modern novel",
                "Direct influence on Nietzsche, Freud, Kafka, and Camus",
                "Existentialist literature tradition rooted in his psychological extremism",
                "Russian literature's global prestige largely built on Dostoevsky and Tolstoy",
                "Modern psychology's interest in pathological mental states",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Crime and Punishment", "targetSlug": "crime-and-punishment", "note": "His masterwork of psychological guilt (1866)"},
                {"type": "INFLUENCES", "target": "The Brothers Karamazov", "targetSlug": "the-brothers-karamazov", "note": "Final masterwork — 'Grand Inquisitor' chapter"},
                {"type": "INFLUENCES", "target": "Friedrich Nietzsche", "targetSlug": "friedrich-nietzsche", "note": "Called Dostoevsky 'the only psychologist from whom I learned'"},
                {"type": "INFLUENCES", "target": "Sigmund Freud", "targetSlug": "sigmund-freud", "note": "Called Brothers Karamazov 'the greatest novel ever written'"},
                {"type": "INFLUENCES", "target": "Franz Kafka", "targetSlug": "franz-kafka", "note": "Existentialist guilt and alienation trace to Dostoevsky"},
                {"type": "INFLUENCES", "target": "Albert Camus", "targetSlug": "albert-camus", "note": "Camus' absurdism engaged directly with Dostoevsky's Underground Man"},
                {"type": "INFLUENCES", "target": "Leo Tolstoy", "targetSlug": "leo-tolstoy", "note": "Great rival and counterpart in Russian literature"},
                {"type": "INFLUENCES", "target": "Mikhail Bakhtin", "targetSlug": "mikhail-bakhtin", "note": "Bakhtin's theory of polyphonic novel based on Dostoevsky"},
                {"type": "OCCURS_IN", "target": "Russia", "targetSlug": "russia", "note": "Lifelong Russian subject"},
                {"type": "OCCURS_IN", "target": "St Petersburg", "targetSlug": "saint-petersburg", "note": "Setting of Crime and Punishment"},
                {"type": "INFLUENCES", "target": "Existentialism", "targetSlug": "existentialism", "note": "Underground Man — first existentialist literary character"},
                {"type": "INFLUENCES", "target": "Russian literature", "targetSlug": "russian-literature", "note": "Pinnacle of Russian psychological realism"},
                {"type": "INFLUENCES", "target": "Nikolai Gogol", "targetSlug": "nikolai-gogol", "note": "Literary predecessor — 'We all come out from Gogol's overcoat'"},
                {"type": "INFLUENCES", "target": "Petrashevsky Circle", "targetSlug": "petrashevsky-circle", "note": "Revolutionary group whose arrest led to his Siberian exile"},
                {"type": "INFLUENCES", "target": "Orthodox Christianity", "targetSlug": "russian-orthodox-church", "note": "Converted to Christian conservatism after Siberian experience"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Fyodor Dostoevsky invented the modern psychological novel and the existentialist literary tradition — his exploration of guilt, faith, and suffering shaped Nietzsche, Freud, Kafka, and Camus, and his polyphonic technique transformed how fiction depicts consciousness."
            },
            "quote": "'Pain and suffering are always inevitable for a large intelligence and a deep heart.' — Fyodor Dostoevsky, Crime and Punishment",
            "places": ["St Petersburg, Russia (birthplace and primary setting)", "Omsk, Siberia (labor camp)", "Baden-Baden, Germany (gambling)"],
            "subjectHeadings": "Fyodor Dostoevsky — Novelists and Writers — Russia — Modern",
            "subjects": ["Russia", "literature", "psychology", "existentialism", "Christianity", "Russian literature", "Siberia", "guilt", "moral philosophy", "19th century"],
            "frameworks": ["literary-history", "religious-thought", "social-theory"],
        }
    },

    # ── 5. John Calvin ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/230-Class-230/230john-calvin.json",
        "slug": "john-calvin",
        "era_correction": None,
        "data": {
            "summary": (
                "John Calvin (1509–1564) was a French Protestant theologian and reformer who became, after Luther, the most influential figure of the Protestant Reformation. His Institutes of the Christian Religion (1536, expanded 1559) provided the most systematic and comprehensive Protestant theology ever written, and his governance of Geneva transformed that city into a 'Protestant Rome' that trained an international generation of ministers.\n\n"
                "Calvin's central theological innovations — predestination (God has eternally chosen who will be saved), the sovereignty of God over all aspects of life, and the equality of the clergy — had profound social and political consequences beyond theology. Max Weber's influential thesis in The Protestant Ethic and the Spirit of Capitalism (1905) argued that Calvinist doctrines of predestination and worldly calling drove the work ethic and capital accumulation that gave rise to modern capitalism.\n\n"
                "In Geneva, Calvin established a theocratic republic in which theological and civil law were unified — executing Michael Servetus for heresy (1553) in an act that became one of Reformation Europe's most controversial moments. His Academy of Geneva (1559) trained pastors who spread Calvinist doctrine to France (Huguenots), Scotland (Knox), the Netherlands, England, and colonial America (Puritans).\n\n"
                "Calvinism's intellectual legacy includes not only Protestantism's major Reformed tradition but also the theological roots of liberal democracy (covenantal government), modern capitalism, and the Puritan strand of American political culture."
            ),
            "causes": [
                "Luther's Reformation opening space for systematic Protestant theology",
                "French persecution of Protestants forcing Calvin to Geneva (1536)",
                "Humanism (Erasmus) providing textual-critical tools for biblical scholarship",
                "Political fragmentation of Holy Roman Empire enabling regional Reformations",
            ],
            "effects": [
                "Institutes of the Christian Religion (1536–1559) — systematic Protestant theology",
                "Geneva as 'Protestant Rome' — model theocratic city-state",
                "Academy of Geneva (1559) training an international Reformed ministry",
                "Calvinist theology spreading to France (Huguenots), Scotland, Netherlands, England",
                "Puritan movement in England and colonial America rooted in Calvinist theology",
                "Max Weber's Protestant ethic thesis linking Calvinism to capitalism",
                "Reformed Protestant tradition — the world's third largest Christian family",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Institutes of the Christian Religion", "targetSlug": "institutes-of-the-christian-religion", "note": "His systematic Protestant theology (1536–1559)"},
                {"type": "INFLUENCES", "target": "Geneva", "targetSlug": "geneva", "note": "Governed Geneva as Protestant theocracy"},
                {"type": "INFLUENCES", "target": "Martin Luther", "targetSlug": "martin-luther", "note": "Luther began the Reformation; Calvin systematized it"},
                {"type": "INFLUENCES", "target": "Huguenots", "targetSlug": "huguenots", "note": "French Calvinist movement"},
                {"type": "INFLUENCES", "target": "John Knox", "targetSlug": "john-knox", "note": "Trained in Geneva; took Calvinism to Scotland"},
                {"type": "INFLUENCES", "target": "Puritanism", "targetSlug": "puritanism", "note": "English and American Puritans were Calvinist"},
                {"type": "INFLUENCES", "target": "Dutch Reformed Church", "targetSlug": "dutch-reformed-church", "note": "Netherlands became the strongest Calvinist state"},
                {"type": "INFLUENCES", "target": "Max Weber", "targetSlug": "max-weber", "note": "Weber's Protestant ethic thesis linked Calvinism to capitalism"},
                {"type": "INFLUENCES", "target": "Michael Servetus", "targetSlug": "michael-servetus", "note": "Executed for heresy under Calvin (1553)"},
                {"type": "INFLUENCES", "target": "Protestant Reformation", "targetSlug": "protestant-reformation", "note": "Second generation reformer who systematized Protestant theology"},
                {"type": "INFLUENCES", "target": "American Puritans", "targetSlug": "american-puritans", "note": "Calvinist theology shaped New England colonial culture"},
                {"type": "INFLUENCES", "target": "Ulrich Zwingli", "targetSlug": "ulrich-zwingli", "note": "Swiss Reformed predecessor whose tradition Calvin inherited"},
                {"type": "INFLUENCES", "target": "Catholic Counter-Reformation", "targetSlug": "counter-reformation", "note": "Calvinist expansion triggered the Jesuit response"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Born in Noyon, France; fled to Geneva"},
                {"type": "OCCURS_IN", "target": "Switzerland", "targetSlug": "switzerland", "note": "Geneva was his base for 28 years"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "John Calvin systematized Protestant theology, turned Geneva into the training ground for international Reformed Christianity, and shaped the Huguenots, Puritans, and Dutch Reformed — with downstream effects on capitalism, liberal democracy, and American political culture that persist today."
            },
            "quote": "'There is no worse screen to block out the Spirit than confidence in our own intelligence.' — John Calvin",
            "places": ["Geneva, Switzerland", "Noyon, France (birthplace)", "Strasbourg, France (exile)"],
            "subjectHeadings": "John Calvin — Protestant Reformers — France/Switzerland — Early Modern",
            "subjects": ["Switzerland", "France", "Protestant Reformation", "theology", "Geneva", "Calvinism", "Puritanism", "capitalism", "Christianity", "16th century"],
            "frameworks": ["religious-thought", "social-theory", "state-formation"],
        }
    },

    # ── 6. Suleiman the Magnificent ──────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222suleiman-the-magnificent.json",
        "slug": "suleiman-the-magnificent",
        "era_correction": None,
        "data": {
            "summary": (
                "Suleiman I 'the Magnificent' (1494–1566) was the tenth and longest-reigning Sultan of the Ottoman Empire (1520–1566), who presided over its apogee — the period of greatest territorial extent, economic prosperity, legal reform, and cultural achievement. To Ottomans he was known as 'Kanunî' (the Lawgiver) for his comprehensive codification of Ottoman law; to Europeans he was 'the Magnificent' for the splendor of his court.\n\n"
                "His military campaigns reshaped European and Middle Eastern history: he captured Belgrade (1521) and Rhodes (1522), defeated Hungary at the Battle of Mohács (1526), besieged Vienna (1529) — the high-water mark of Ottoman advance into Europe — and expanded Ottoman control across North Africa and into Mesopotamia. At his death, the empire stretched from Hungary to Persia and from Crimea to Yemen, governing 15 million people.\n\n"
                "Suleiman's legal code (Kanun-i-Osmani) unified Ottoman civil and criminal law, standardized taxation, and regulated land tenure — creating the most sophisticated administrative system in the 16th-century world. His patronage produced Ibrahim Pasha's palace complex, the Süleymaniye Mosque (1558, Mimar Sinan's masterpiece), and a golden age of Ottoman poetry, carpets, calligraphy, and ceramics.\n\n"
                "His alliance with France against the Habsburgs — the first strategic partnership between a Christian and Muslim state — established the principle of raison d'état over religious solidarity and shaped European diplomacy for a century."
            ),
            "causes": [
                "Selim I's conquests (Egypt, Syria, Mecca) expanding Ottoman resources and prestige",
                "Habsburg-Valois rivalry in Europe creating openings for Ottoman expansion",
                "Devshirme system of elite trained slave soldiers providing disciplined military",
                "Ottoman administrative and legal tradition inherited from Mehmed II",
            ],
            "effects": [
                "Battle of Mohács (1526) — end of medieval Hungarian kingdom",
                "Siege of Vienna (1529) — furthest Ottoman advance into Europe",
                "Kanun-i-Osmani — comprehensive Ottoman legal code",
                "Süleymaniye Mosque (1558) — Mimar Sinan's architectural masterpiece",
                "Ottoman-French alliance — first inter-confessional strategic partnership",
                "Ottoman control of Eastern Mediterranean trade routes",
                "Golden age of Ottoman arts and architecture",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Ottoman Empire", "targetSlug": "ottoman-empire", "note": "Sultan at the empire's apogee"},
                {"type": "INFLUENCES", "target": "Battle of Mohács", "targetSlug": "battle-of-mohacs", "note": "Crushed Hungary (1526), reshaped Central Europe"},
                {"type": "INFLUENCES", "target": "Siege of Vienna (1529)", "targetSlug": "siege-of-vienna-1529", "note": "Furthest Ottoman advance into Europe"},
                {"type": "INFLUENCES", "target": "Mimar Sinan", "targetSlug": "mimar-sinan", "note": "Chief architect — built Süleymaniye Mosque"},
                {"type": "INFLUENCES", "target": "Süleymaniye Mosque", "targetSlug": "suleymaniye-mosque", "note": "His greatest building, Istanbul (1558)"},
                {"type": "INFLUENCES", "target": "Ibrahim Pasha", "targetSlug": "ibrahim-pasha", "note": "Grand Vizier and closest companion (executed 1536)"},
                {"type": "INFLUENCES", "target": "Hurrem Sultan", "targetSlug": "hurrem-sultan", "note": "Slave turned legal wife — unprecedented political power"},
                {"type": "INFLUENCES", "target": "Habsburg Empire", "targetSlug": "habsburg-empire", "note": "Primary European rival; besieged Vienna against Charles V"},
                {"type": "INFLUENCES", "target": "Francis I of France", "targetSlug": "francis-i-of-france", "note": "Allied with France against Habsburgs — first Muslim-Christian alliance"},
                {"type": "INFLUENCES", "target": "Ottoman law code (Kanun)", "targetSlug": "ottoman-kanun", "note": "Comprehensive civil/criminal code earning 'Lawgiver' title"},
                {"type": "INFLUENCES", "target": "Safavid Persia", "targetSlug": "safavid-dynasty", "note": "Shia rival; Suleiman took Baghdad and Mesopotamia (1534)"},
                {"type": "OCCURS_IN", "target": "Istanbul", "targetSlug": "istanbul", "note": "Capital of the Ottoman Empire"},
                {"type": "INFLUENCES", "target": "Rhodes", "targetSlug": "rhodes", "note": "Captured from Knights Hospitaller (1522)"},
                {"type": "INFLUENCES", "target": "Algiers", "targetSlug": "algiers", "note": "Barbarossa's fleet brought North Africa under Ottoman suzerainty"},
                {"type": "INFLUENCES", "target": "Selim I", "targetSlug": "selim-i", "note": "Father who conquered Egypt and Mecca, expanding empire for Suleiman"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Suleiman the Magnificent ruled the Ottoman Empire at its greatest extent, codified its law, patronized its highest cultural achievements, and shaped European geopolitics for a century — his siege of Vienna defined the fault line between Christendom and Islam that dominated European consciousness for 300 years."
            },
            "quote": "'I who am the Sultan of Sultans, the sovereign of sovereigns, the distributor of crowns to the monarchs on the face of the earth.' — Suleiman the Magnificent (from a letter to Francis I)",
            "places": ["Istanbul, Turkey", "Constantinople (Istanbul — capital)", "Trebizond (birthplace)"],
            "subjectHeadings": "Suleiman the Magnificent — Sultans and Rulers — Ottoman Empire — Early Modern",
            "subjects": ["Turkey", "Ottoman Empire", "Islam", "Early Modern Europe", "military history", "law", "architecture", "Mediterranean", "Habsburg rivalry", "16th century"],
            "frameworks": ["empire-building", "state-formation", "religious-conflict"],
        }
    },

    # ── 7. Joseph Stalin ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222joseph-stalin.json",
        "slug": "joseph-stalin",
        "era_correction": None,
        "data": {
            "summary": (
                "Joseph Stalin (1878–1953) was the General Secretary of the Communist Party of the Soviet Union from 1922 and its de facto leader from the late 1920s until his death in 1953 — one of the most powerful and lethal political figures in history. Under his rule, the USSR was transformed from an agrarian economy into a nuclear superpower, won World War II, and established a Soviet empire stretching from East Germany to North Korea — while simultaneously killing an estimated 6–20 million Soviet citizens through famine, purges, and the Gulag.\n\n"
                "Stalin's Soviet industrialization (Five-Year Plans, 1928–1941) transformed Russia into an industrial state in a decade through forced collectivization of agriculture, which caused the Ukrainian Holodomor famine (1932–33, 3–7 million dead) and millions of additional deaths. The Great Terror (1936–38) executed or imprisoned roughly half the Soviet officer corps, 1.2 million Party members, and destroyed virtually every potential rival.\n\n"
                "His leadership during World War II — particularly the defense of Stalingrad (1942–43), the greatest military victory of the 20th century — turned the tide against Nazi Germany and established Soviet power across Eastern Europe. At Yalta (1945) he secured Soviet spheres of influence in Eastern Europe, establishing the Cold War order that defined world politics for 45 years.\n\n"
                "'One death is a tragedy; a million deaths is a statistic,' Stalin reportedly said. Whether apocryphal or not, this phrase captures the terrifying administrative calculus of his rule — the most consequential and destructive of the 20th century after Hitler."
            ),
            "causes": [
                "Lenin's death (1924) and vacuum of Soviet leadership enabling Stalin's consolidation",
                "Marxist-Leninist ideology providing framework for one-party totalitarian state",
                "Russia's industrial backwardness making rapid forced industrialization seem necessary",
                "Cult of Bolshevik revolutionary violence normalizing terror as a political tool",
            ],
            "effects": [
                "Soviet industrialization — USSR became industrial superpower in 15 years",
                "Holodomor famine (1932–33) — collectivization killing 3–7 million Ukrainians",
                "Great Purge/Terror (1936–38) — elimination of rivals and 1+ million executed",
                "Gulag system — estimated 18 million passed through labor camps",
                "Soviet victory in World War II (Stalingrad, Berlin) — decisive defeat of Nazi Germany",
                "Cold War order — Soviet empire in Eastern Europe, nuclear arms race",
                "Sino-Soviet alliance supporting Mao Zedong's China",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Soviet Union (USSR)", "targetSlug": "soviet-union", "note": "Leader of the USSR 1924–1953"},
                {"type": "INFLUENCES", "target": "Vladimir Lenin", "targetSlug": "vladimir-lenin", "note": "Predecessor; Stalin built on and distorted Lenin's legacy"},
                {"type": "INFLUENCES", "target": "Leon Trotsky", "targetSlug": "leon-trotsky", "note": "Chief rival; had him assassinated in Mexico (1940)"},
                {"type": "INFLUENCES", "target": "Great Terror (1936–38)", "targetSlug": "great-terror-ussr", "note": "Mass purge executing 750,000+ and imprisoning millions"},
                {"type": "INFLUENCES", "target": "Holodomor", "targetSlug": "holodomor", "note": "Ukrainian famine caused by forced collectivization (1932–33)"},
                {"type": "INFLUENCES", "target": "Gulag system", "targetSlug": "gulag", "note": "Network of labor camps imprisoning 18 million people"},
                {"type": "INFLUENCES", "target": "Battle of Stalingrad", "targetSlug": "battle-of-stalingrad", "note": "Decisive WWII turning point under his command"},
                {"type": "INFLUENCES", "target": "Cold War", "targetSlug": "cold-war", "note": "Soviet empire and nuclear program he established"},
                {"type": "INFLUENCES", "target": "Adolf Hitler", "targetSlug": "adolf-hitler", "note": "Allied (Molotov-Ribbentrop pact) then fought to the death"},
                {"type": "INFLUENCES", "target": "Yalta Conference", "targetSlug": "yalta-conference", "note": "Secured Soviet sphere in Eastern Europe (1945)"},
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Supported Mao's revolution; Sino-Soviet alliance"},
                {"type": "OCCURS_IN", "target": "Russia", "targetSlug": "russia", "note": "Georgian-born leader of Russia"},
                {"type": "INFLUENCES", "target": "Five-Year Plans", "targetSlug": "soviet-five-year-plans", "note": "Forced industrialization transforming USSR economy"},
                {"type": "INFLUENCES", "target": "Nuclear weapons program", "targetSlug": "soviet-nuclear-program", "note": "Directed Soviet atomic bomb project (tested 1949)"},
                {"type": "INFLUENCES", "target": "North Korea", "targetSlug": "north-korea", "note": "Established Kim Il-sung's regime as Soviet satellite"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Joseph Stalin transformed the Soviet Union into a nuclear superpower, led the decisive defeat of Nazi Germany, and established the Cold War order — while simultaneously presiding over the deaths of an estimated 6–20 million Soviet citizens in one of history's most consequential and destructive dictatorships."
            },
            "quote": "'One death is a tragedy; a million deaths is a statistic.' — attributed to Joseph Stalin",
            "places": ["Moscow, Russia (power base)", "Gori, Georgia (birthplace)", "Yalta, Crimea", "Stalingrad (Volgograd), Russia"],
            "subjectHeadings": "Joseph Stalin — Dictators and Leaders — Soviet Union — Modern",
            "subjects": ["Soviet Union", "Russia", "communism", "World War II", "Cold War", "totalitarianism", "industrialization", "Gulag", "Holodomor", "20th century"],
            "frameworks": ["totalitarianism", "revolution", "empire-building"],
        }
    },

    # ── 8. Rembrandt ─────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/264-Class-264/264rembrandt.json",
        "slug": "rembrandt",
        "era_correction": None,
        "data": {
            "summary": (
                "Rembrandt van Rijn (1606–1669) was a Dutch Golden Age painter, printmaker, and draughtsman widely regarded as one of the greatest visual artists in the history of Western art. Working in Amsterdam during the height of Dutch commercial and artistic supremacy, he created an unmatched body of work in oil painting, etching, and drawing that set new standards for psychological portraiture, luminosity, and emotional depth.\n\n"
                "Rembrandt's revolutionary technique centered on chiaroscuro — the dramatic play of light and shadow inherited from Caravaggio — deployed with unprecedented subtlety to illuminate the inner emotional states of his subjects. His self-portraits (over 80 across his lifetime) constitute the most sustained exercise in psychological self-examination in the history of art, tracking his face from confident young master to bankrupt old man with unflinching honesty. His group portraits, including The Night Watch (1642) — the largest and most famous Dutch Golden Age painting — brought radical compositional dynamism to a static genre.\n\n"
                "Despite early success, Rembrandt's later life was marked by bankruptcy (1656), the deaths of his wife and son, and artistic obscurity in favor of more fashionable contemporaries. The Night Watch was initially misunderstood; his dark, psychological late style was preferred to his earlier, brighter manner by posterity.\n\n"
                "His influence on Western painting is incalculable: Delacroix, Goya, Van Gogh, Sargent, and virtually every serious portrait painter of the past three centuries cited him as the master above all masters."
            ),
            "causes": [
                "Dutch Golden Age economic prosperity creating wealthy merchant patronage class",
                "Calvinist theology discouraging religious art and redirecting painting toward secular subjects",
                "Caravaggio's chiaroscuro technique arriving in Northern Europe via Utrecht Caravaggists",
                "Leiden's university culture providing intellectual context for his biblical subjects",
            ],
            "effects": [
                "The Night Watch (1642) — definitive masterpiece of Dutch Golden Age painting",
                "80+ self-portraits — most sustained psychological self-examination in art history",
                "Revolutionary chiaroscuro technique raising psychological portraiture to new heights",
                "350 paintings and 300 etchings defining Dutch Golden Age standards",
                "Influence on Delacroix, Goya, Manet, Van Gogh, and modern portraiture",
                "Rijksmuseum collection built around Rembrandt and Dutch Golden Age",
                "Etchings revolutionizing printmaking as a fine art medium",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "The Night Watch", "targetSlug": "the-night-watch", "note": "1642 masterpiece — most famous Dutch painting"},
                {"type": "INFLUENCES", "target": "Dutch Golden Age", "targetSlug": "dutch-golden-age", "note": "Greatest painter of the Dutch Golden Age"},
                {"type": "INFLUENCES", "target": "Caravaggio", "targetSlug": "caravaggio", "note": "Inherited and transformed Caravaggio's chiaroscuro"},
                {"type": "INFLUENCES", "target": "Johannes Vermeer", "targetSlug": "johannes-vermeer", "note": "Contemporary Dutch master in the same tradition"},
                {"type": "INFLUENCES", "target": "Frans Hals", "targetSlug": "frans-hals", "note": "Contemporary Dutch portraitist predecessor"},
                {"type": "INFLUENCES", "target": "Van Gogh", "targetSlug": "vincent-van-gogh", "note": "Cited Rembrandt as greatest influence on his painting"},
                {"type": "INFLUENCES", "target": "Francisco Goya", "targetSlug": "francisco-goya", "note": "Rembrandt's psychological darkness prefigures Goya"},
                {"type": "INFLUENCES", "target": "Eugène Delacroix", "targetSlug": "eugene-delacroix", "note": "Romanticist who called Rembrandt equal to Shakespeare"},
                {"type": "OCCURS_IN", "target": "Amsterdam", "targetSlug": "amsterdam", "note": "Primary city of work — Amsterdam art market center"},
                {"type": "OCCURS_IN", "target": "Netherlands", "targetSlug": "netherlands", "note": "Dutch Republic at peak commercial and cultural power"},
                {"type": "INFLUENCES", "target": "Protestant Reformation art", "targetSlug": "protestant-art", "note": "Calvinist secular art tradition he exemplified"},
                {"type": "INFLUENCES", "target": "Etching (printmaking)", "targetSlug": "etching-printmaking", "note": "His 300+ etchings raised printmaking to fine art status"},
                {"type": "INFLUENCES", "target": "Rijksmuseum", "targetSlug": "rijksmuseum", "note": "Amsterdam's national museum built around Rembrandt"},
                {"type": "INFLUENCES", "target": "Saskia van Uylenburgh", "targetSlug": "saskia-van-uylenburgh", "note": "Wife and model in many early paintings; death 1642"},
                {"type": "INFLUENCES", "target": "Self-portrait tradition", "targetSlug": "self-portrait", "note": "80+ self-portraits from 22 to 63 — unique in art history"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Rembrandt van Rijn elevated psychological portraiture to its greatest heights through revolutionary chiaroscuro technique, documented his own inner life across 80 self-portraits, and created The Night Watch — establishing the Dutch Golden Age as one of the supreme periods of Western art."
            },
            "quote": "'Choose only one master — Nature.' — Rembrandt van Rijn",
            "places": ["Amsterdam, Netherlands", "Leiden, Netherlands (birthplace)"],
            "subjectHeadings": "Rembrandt van Rijn — Painters and Artists — Netherlands — Early Modern",
            "subjects": ["Netherlands", "painting", "Dutch Golden Age", "portraiture", "chiaroscuro", "etchings", "Amsterdam", "Protestant art", "Baroque", "17th century"],
            "frameworks": ["cultural-history", "artistic-patronage", "religious-thought"],
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

    print(f"Batch 60 enrichment — {len(ENRICHMENTS)} entities\n")

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
