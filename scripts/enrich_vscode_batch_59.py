#!/usr/bin/env python3
"""
VS Code Enrichment Batch 59 — 8 Major Historical Persons
Voltaire, Immanuel Kant, Jean-Jacques Rousseau, Leo Tolstoy,
Thomas Edison, Simón Bolívar, Kublai Khan, Vasco da Gama

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-59-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-59-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Voltaire ──────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/210-Class-210/21008-voltaire.json",
        "slug": "voltaire",
        "era_correction": None,
        "data": {
            "summary": (
                "Voltaire (1694–1778), born François-Marie Arouet, was a French Enlightenment writer, historian, and philosopher who became the most influential and widely read intellectual of 18th-century Europe. His pen name became synonymous with wit, irreverence, and the power of reason to challenge superstition, intolerance, and arbitrary power — values that helped precipitate the French Revolution a decade after his death.\n\n"
                "Imprisoned in the Bastille, exiled from France twice, and perpetually harassed by church and state, Voltaire turned persecution into productivity. His Candide (1759) — a satirical novella skewering religious optimism, aristocratic privilege, and the Lisbon earthquake theodicy — remains one of the most read works of French literature. His Philosophical Dictionary, Letters Concerning the English Nation, and correspondence with Frederick the Great and Catherine the Great placed him at the centre of a European republic of letters.\n\n"
                "Voltaire championed religious tolerance above all other causes. His campaign to rehabilitate Jean Calas — a Protestant falsely executed for murdering his son — galvanized European public opinion against judicial torture and religious persecution, winning a posthumous reversal and establishing the idea of a public intellectual fighting for individual rights.\n\n"
                "On his deathbed, asked to renounce the devil, he reportedly replied: 'This is no time to make new enemies.' He is buried in the Panthéon in Paris. His battle cry — 'Écrasez l'infâme!' ('Crush the infamous thing!', meaning fanaticism and intolerance) — defines the Enlightenment's combative spirit."
            ),
            "causes": [
                "French Ancien Régime's censorship and arbitrary justice motivating satirical attack",
                "Enlightenment intellectual milieu in Paris and European courts",
                "Leibniz's optimism ('best of all possible worlds') providing philosophical target",
                "Lisbon earthquake (1755) challenging providential theology",
            ],
            "effects": [
                "Candide (1759) — masterwork of satirical Enlightenment literature",
                "Calas affair (1762–65) — landmark campaign for judicial reform and religious tolerance",
                "Philosophical Dictionary challenging church authority and superstition",
                "Intellectual influence on French Revolutionary ideology",
                "Secular tradition of French laïcité (secularism)",
                "Model for public intellectual advocacy of individual rights",
                "Correspondence with European monarchs spreading Enlightenment ideas to courts",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "French Enlightenment", "targetSlug": "french-enlightenment", "note": "Central figure of the philosophes"},
                {"type": "INFLUENCES", "target": "Candide", "targetSlug": "candide", "note": "Satirical masterwork (1759)"},
                {"type": "INFLUENCES", "target": "French Revolution", "targetSlug": "french-revolution", "note": "Intellectual forerunner of revolutionary ideology"},
                {"type": "INFLUENCES", "target": "Jean-Jacques Rousseau", "targetSlug": "jean-jacques-rousseau", "note": "Fellow philosophe, later rival"},
                {"type": "INFLUENCES", "target": "Denis Diderot", "targetSlug": "denis-diderot", "note": "Collaborated on Encyclopédie project"},
                {"type": "INFLUENCES", "target": "Catherine the Great", "targetSlug": "catherine-the-great", "note": "Extensive philosophical correspondence"},
                {"type": "INFLUENCES", "target": "Frederick the Great", "targetSlug": "frederick-the-great", "note": "Lived at Prussian court 1750–1753"},
                {"type": "INFLUENCES", "target": "Calas affair", "targetSlug": "calas-affair", "note": "Pioneered public intellectual human rights campaign"},
                {"type": "INFLUENCES", "target": "Religious tolerance", "targetSlug": "religious-tolerance", "note": "His Treatise on Tolerance (1763) — foundational text"},
                {"type": "INFLUENCES", "target": "Laïcité (French secularism)", "targetSlug": "laicite", "note": "His anti-clericalism shaped French secular tradition"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Primary country of activity"},
                {"type": "INFLUENCES", "target": "American Founding Fathers", "targetSlug": "american-founding-fathers", "note": "Jefferson and Franklin read him closely"},
                {"type": "INFLUENCES", "target": "Gottfried Leibniz", "targetSlug": "gottfried-leibniz", "note": "Pangloss in Candide parodies Leibnizian optimism"},
                {"type": "INFLUENCES", "target": "Encyclopédie", "targetSlug": "encyclopedie", "note": "Contributed articles to Diderot's Encyclopédie"},
                {"type": "OCCURS_IN", "target": "Bastille", "targetSlug": "bastille", "note": "Imprisoned twice — became symbol of tyranny he opposed"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Voltaire was the conscience of the European Enlightenment — his wit dismantled religious superstition, his advocacy of the Calas affair invented the modern public intellectual, and his ideas on tolerance and reason flowed directly into the French Revolution and secular democracy."
            },
            "quote": "'I disapprove of what you say, but I will defend to the death your right to say it.' — attributed to Voltaire",
            "places": ["Paris, France", "Geneva, Switzerland (Ferney)", "Cirey, France", "Berlin, Prussia"],
            "subjectHeadings": "Voltaire — Philosophers and Writers — France — Early Modern",
            "subjects": ["France", "Enlightenment", "philosophy", "literature", "religious tolerance", "secularism", "French Revolution", "satire", "human rights", "18th century"],
            "frameworks": ["enlightenment", "intellectual-history", "secularism"],
        }
    },

    # ── 2. Immanuel Kant ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201immanuel-kant.json",
        "slug": "immanuel-kant",
        "era_correction": None,
        "data": {
            "summary": (
                "Immanuel Kant (1724–1804) was a German philosopher whose Critique of Pure Reason (1781) fundamentally reshaped Western philosophy and is widely considered one of the most important philosophical works ever written. Born and dying in Königsberg (modern Kaliningrad), he never traveled more than 40 miles from his birthplace, yet transformed how humanity understands knowledge, morality, beauty, and the limits of reason.\n\n"
                "Kant's 'Copernican revolution in philosophy' proposed that the mind does not passively receive reality but actively structures experience through innate categories of understanding — space, time, causality. This resolved the impasse between rationalism (Descartes, Leibniz) and empiricism (Hume, Locke), earning him the title 'the great synthesizer.' His response to Hume's skepticism is among the most celebrated intellectual moves in philosophical history.\n\n"
                "His moral philosophy — the Categorical Imperative ('act only according to that maxim whereby you can at the same time will that it should become a universal law') — provided the most rigorous secular foundation for universal ethics. His political essays, including Perpetual Peace (1795), directly anticipated the United Nations, international law, and liberal democratic order.\n\n"
                "Kant's influence on virtually every subsequent philosophical tradition — German Idealism (Hegel, Fichte), phenomenology (Husserl), analytic philosophy, and modern ethics — makes him the pivot of modern Western thought. 'All roads in philosophy lead back to Kant,' as the saying goes."
            ),
            "causes": [
                "David Hume's skepticism 'awakening Kant from his dogmatic slumber'",
                "Rationalist tradition (Leibniz, Wolff) providing metaphysical framework to overcome",
                "Empiricist tradition (Locke, Hume) providing epistemological challenge",
                "Königsberg as cosmopolitan Prussian city with access to Enlightenment thought",
            ],
            "effects": [
                "Critique of Pure Reason (1781) — defining work of modern philosophy",
                "Categorical Imperative — secular universal moral framework",
                "Critique of Practical Reason (1788) and Critique of Judgment (1790)",
                "Copernican revolution in epistemology — mind structures experience",
                "Perpetual Peace (1795) — forerunner of UN and international law",
                "Founding of German Idealism (Hegel, Fichte, Schelling built on Kant)",
                "Modern liberal political theory grounded in human dignity and autonomy",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Critique of Pure Reason", "targetSlug": "critique-of-pure-reason", "note": "His magnum opus (1781)"},
                {"type": "INFLUENCES", "target": "David Hume", "targetSlug": "david-hume", "note": "Hume 'awakened him from dogmatic slumber'"},
                {"type": "INFLUENCES", "target": "G.W.F. Hegel", "targetSlug": "hegel", "note": "Built German Idealism in response to Kant"},
                {"type": "INFLUENCES", "target": "Johann Gottlieb Fichte", "targetSlug": "fichte", "note": "Direct Kantian successor in German Idealism"},
                {"type": "INFLUENCES", "target": "Categorical Imperative", "targetSlug": "categorical-imperative", "note": "His universal moral law"},
                {"type": "INFLUENCES", "target": "Perpetual Peace", "targetSlug": "perpetual-peace-kant", "note": "1795 essay anticipating international law"},
                {"type": "INFLUENCES", "target": "United Nations", "targetSlug": "united-nations", "note": "His federation of free states concept"},
                {"type": "INFLUENCES", "target": "Modern ethics", "targetSlug": "modern-ethics", "note": "Deontological ethics still dominant in moral philosophy"},
                {"type": "INFLUENCES", "target": "Gottfried Leibniz", "targetSlug": "gottfried-leibniz", "note": "Rationalist whose system Kant overcame"},
                {"type": "INFLUENCES", "target": "Edmund Burke", "targetSlug": "edmund-burke", "note": "Contemporaneous conservative counterpart"},
                {"type": "OCCURS_IN", "target": "Prussia", "targetSlug": "prussia", "note": "Lifelong resident of Königsberg, Prussia"},
                {"type": "INFLUENCES", "target": "Analytic philosophy", "targetSlug": "analytic-philosophy", "note": "Frege, Russell, and Wittgenstein engaged centrally with Kant"},
                {"type": "INFLUENCES", "target": "Phenomenology", "targetSlug": "phenomenology", "note": "Husserl and Heidegger responded to Kantian epistemology"},
                {"type": "INFLUENCES", "target": "Liberal democracy", "targetSlug": "liberal-democracy", "note": "Human dignity and autonomy ground liberal rights theory"},
                {"type": "INFLUENCES", "target": "Enlightenment", "targetSlug": "enlightenment", "note": "'What is Enlightenment?' essay defined the movement"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Immanuel Kant is the pivot of modern Western philosophy — his Critique of Pure Reason unified rationalism and empiricism, his Categorical Imperative provided the secular foundation of universal ethics, and his Perpetual Peace anticipated modern international law and the United Nations."
            },
            "quote": "'Act only according to that maxim whereby you can at the same time will that it should become a universal law.' — Immanuel Kant, Groundwork of the Metaphysics of Morals",
            "places": ["Königsberg, Prussia (modern Kaliningrad, Russia)"],
            "subjectHeadings": "Immanuel Kant — Philosophers — Germany/Prussia — Early Modern",
            "subjects": ["Germany", "philosophy", "Enlightenment", "ethics", "epistemology", "German Idealism", "moral philosophy", "political theory", "international law", "metaphysics"],
            "frameworks": ["enlightenment", "intellectual-history", "political-philosophy"],
        }
    },

    # ── 3. Jean-Jacques Rousseau ─────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201jean-jacques-rousseau.json",
        "slug": "jean-jacques-rousseau",
        "era_correction": None,
        "data": {
            "summary": (
                "Jean-Jacques Rousseau (1712–1778) was a Genevan-born philosopher, composer, and political theorist whose ideas on human nature, inequality, and social contract theory became the most explosive intellectual fuel of the French Revolution and modern democratic thought. His claim that 'Man is born free, and everywhere he is in chains' — the opening of The Social Contract (1762) — remains one of the most quoted sentences in political philosophy.\n\n"
                "Rousseau argued that civilization corrupts the natural goodness of humanity, and that inequality arises not from nature but from private property and social institutions (Discourse on the Origin of Inequality, 1755). His vision of the 'general will' — the collective moral authority of a sovereign people — provided the philosophical basis for popular sovereignty and republican democracy, directly inspiring Robespierre and the radical phase of the French Revolution.\n\n"
                "His educational treatise Émile (1762) revolutionized pedagogy by arguing that children should learn through experience and natural development rather than rote instruction — a vision that shaped progressive education from Pestalozzi to Dewey to Montessori. His autobiographical Confessions inaugurated modern psychological autobiography.\n\n"
                "Romanticism, nationalism, radical democracy, and progressive education all trace direct lineage to Rousseau. Voltaire, his Enlightenment contemporary, detested him — calling Émile a book 'so stupid and ridiculous.' Their feud encapsulates the tension between liberal reform and radical transformation that has defined Western politics ever since."
            ),
            "causes": [
                "Geneva's Calvinist civic republican tradition shaping his political thought",
                "Personal poverty and social exclusion from Paris Enlightenment salons",
                "Enlightenment optimism about reason and progress (which he contested)",
                "Lockean natural rights theory as foundation he radicalized",
            ],
            "effects": [
                "The Social Contract (1762) — foundational text of popular sovereignty",
                "Discourse on the Origin of Inequality — critique of private property",
                "Émile (1762) — revolutionary educational philosophy",
                "Confessions — inauguration of modern autobiographical writing",
                "Direct intellectual influence on French Revolution and Jacobins",
                "General will concept — basis of modern democratic theory",
                "Romanticism — his celebration of nature and feeling over reason",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "French Revolution", "targetSlug": "french-revolution", "note": "Most cited philosopher of the Revolution"},
                {"type": "INFLUENCES", "target": "Social Contract (1762)", "targetSlug": "social-contract-rousseau", "note": "Foundational text of popular sovereignty"},
                {"type": "INFLUENCES", "target": "Robespierre", "targetSlug": "robespierre", "note": "Called himself 'disciple of Rousseau'"},
                {"type": "INFLUENCES", "target": "Voltaire", "targetSlug": "voltaire", "note": "Famous intellectual antagonist"},
                {"type": "INFLUENCES", "target": "Immanuel Kant", "targetSlug": "immanuel-kant", "note": "Kant kept only Rousseau's portrait in his home"},
                {"type": "INFLUENCES", "target": "Romanticism", "targetSlug": "romanticism", "note": "Rousseau's nature + emotion ethos founded Romanticism"},
                {"type": "INFLUENCES", "target": "Progressive education", "targetSlug": "progressive-education", "note": "Émile directly inspired Pestalozzi, Dewey, Montessori"},
                {"type": "INFLUENCES", "target": "Nationalism", "targetSlug": "nationalism", "note": "General will concept fed into 19th century nationalism"},
                {"type": "INFLUENCES", "target": "John Locke", "targetSlug": "john-locke", "note": "Built on and radicalized Lockean natural rights"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Primary country of intellectual activity"},
                {"type": "OCCURS_IN", "target": "Switzerland", "targetSlug": "switzerland", "note": "Born in Geneva; fled persecution there"},
                {"type": "INFLUENCES", "target": "American Declaration of Independence", "targetSlug": "american-declaration-of-independence", "note": "Jefferson drew on Rousseau's natural rights theory"},
                {"type": "INFLUENCES", "target": "Karl Marx", "targetSlug": "karl-marx", "note": "Inequality critique anticipated historical materialism"},
                {"type": "INFLUENCES", "target": "Denis Diderot", "targetSlug": "denis-diderot", "note": "Early collaborator, later estranged"},
                {"type": "INFLUENCES", "target": "Mary Wollstonecraft", "targetSlug": "mary-wollstonecraft", "note": "Responded to and challenged his views on women in Vindication"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Rousseau's Social Contract gave the French Revolution its philosophical language of popular sovereignty and the general will; his educational ideas shaped progressive pedagogy worldwide; and his critique of inequality anticipated modern socialism — making him the most politically potent philosopher of modernity."
            },
            "quote": "'Man is born free, and everywhere he is in chains.' — Jean-Jacques Rousseau, The Social Contract (1762)",
            "places": ["Geneva, Switzerland", "Paris, France", "Montmorency, France"],
            "subjectHeadings": "Jean-Jacques Rousseau — Philosophers — Switzerland/France — Early Modern",
            "subjects": ["Switzerland", "France", "political philosophy", "Enlightenment", "French Revolution", "social contract", "education", "democracy", "Romanticism", "inequality"],
            "frameworks": ["enlightenment", "political-philosophy", "social-theory"],
        }
    },

    # ── 4. Leo Tolstoy ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201leo-tolstoy.json",
        "slug": "leo-tolstoy",
        "era_correction": None,
        "data": {
            "summary": (
                "Leo Tolstoy (1828–1910) was a Russian novelist, moral philosopher, and social reformer widely regarded as one of the greatest writers in world literary history. His two masterworks — War and Peace (1869) and Anna Karenina (1878) — set the standard for the realistic novel and have never been surpassed in scope, psychological depth, or moral ambition. William Faulkner called him 'the writer I've read most.'\n\n"
                "War and Peace, spanning the Napoleonic invasion of Russia (1805–1812), follows five aristocratic families through battle, love, birth, and death, developing Tolstoy's radical thesis that history is made by millions of individual acts rather than by great men — a direct repudiation of the 'great man' theory of Carlyle and Hegel. Anna Karenina, often called 'the best novel ever written' by Vladimir Nabokov, dissects the collision of individual desire with social convention in 19th-century Russia.\n\n"
                "After a spiritual crisis in the 1870s, Tolstoy renounced his wealth and aristocratic status, developed a form of Christian anarchism (Tolstoyanism), and wrote the influential essays What Then Must We Do? and The Kingdom of God Is Within You. The latter directly influenced Mahatma Gandhi, who wrote that 'it overwhelmed me' and credited it with shaping his philosophy of nonviolent resistance.\n\n"
                "Excommunicated by the Russian Orthodox Church in 1901, he died a global celebrity and moral sage, having shaped not only literature but politics, pacifism, and the nonviolent traditions of Gandhi and Martin Luther King Jr."
            ),
            "causes": [
                "Russian aristocratic literary tradition (Pushkin, Turgenev) as foundation",
                "Personal participation in the Crimean War providing material for realistic battle scenes",
                "Spiritual crisis of the 1870s transforming novelist into moral prophet",
                "Napoleonic invasion of Russia (1812) as historical subject of War and Peace",
            ],
            "effects": [
                "War and Peace (1869) — defining achievement of the realistic novel",
                "Anna Karenina (1878) — psychological novel setting new standard",
                "Tolstoyanism — Christian anarchist and pacifist philosophy",
                "The Kingdom of God Is Within You (1893) — key text of nonviolent resistance",
                "Direct influence on Gandhi's philosophy of nonviolent resistance (ahimsa)",
                "Direct influence on Martin Luther King Jr.'s civil rights strategy",
                "Russian social reform debates about serfdom, poverty, and land",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "War and Peace", "targetSlug": "war-and-peace", "note": "Masterwork depicting Napoleonic Russia"},
                {"type": "INFLUENCES", "target": "Anna Karenina", "targetSlug": "anna-karenina", "note": "Masterwork of psychological realism"},
                {"type": "INFLUENCES", "target": "Mahatma Gandhi", "targetSlug": "mahatma-gandhi", "note": "Kingdom of God directly inspired Gandhi's nonviolence"},
                {"type": "INFLUENCES", "target": "Martin Luther King Jr.", "targetSlug": "martin-luther-king-jr", "note": "Tolstoyan nonviolence shaped King's civil rights strategy"},
                {"type": "INFLUENCES", "target": "Fyodor Dostoevsky", "targetSlug": "fyodor-dostoevsky", "note": "Great rival and counterpart in Russian literature"},
                {"type": "INFLUENCES", "target": "Russian literature", "targetSlug": "russian-literature", "note": "Pinnacle of the Russian realist tradition"},
                {"type": "INFLUENCES", "target": "Nonviolent resistance", "targetSlug": "nonviolent-resistance", "note": "Kingdom of God Is Within You foundational text"},
                {"type": "INFLUENCES", "target": "William Faulkner", "targetSlug": "william-faulkner", "note": "Acknowledged Tolstoy as primary literary influence"},
                {"type": "OCCURS_IN", "target": "Russia", "targetSlug": "russia", "note": "Lifelong Russian subject, set novels in Russia"},
                {"type": "INFLUENCES", "target": "Napoleonic Wars", "targetSlug": "napoleonic-wars", "note": "War and Peace depicts the 1812 invasion"},
                {"type": "INFLUENCES", "target": "Russian Orthodox Church", "targetSlug": "russian-orthodox-church", "note": "Excommunicated 1901 for heterodox beliefs"},
                {"type": "INFLUENCES", "target": "Realism (literary movement)", "targetSlug": "literary-realism", "note": "Greatest practitioner of literary realism"},
                {"type": "INFLUENCES", "target": "Anarchism", "targetSlug": "anarchism", "note": "Christian anarchist tradition shaped by Tolstoy"},
                {"type": "INFLUENCES", "target": "Ivan Turgenev", "targetSlug": "ivan-turgenev", "note": "Russian literary peer and contemporary"},
                {"type": "INFLUENCES", "target": "Virginia Woolf", "targetSlug": "virginia-woolf", "note": "Called Tolstoy's Anna Karenina the greatest novel"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Leo Tolstoy produced two of the greatest novels ever written and then became a global moral prophet — his philosophy of nonviolent resistance shaped Gandhi and Martin Luther King Jr., making him one of the rare writers whose ideas changed history."
            },
            "quote": "'All great literature is one of two stories; a man goes on a journey or a stranger comes to town.' — Leo Tolstoy",
            "places": ["Yasnaya Polyana, Russia (birthplace and estate)", "Moscow, Russia", "St Petersburg, Russia"],
            "subjectHeadings": "Leo Tolstoy — Novelists and Writers — Russia — Modern",
            "subjects": ["Russia", "literature", "novel", "Napoleonic Wars", "nonviolence", "philosophy", "pacifism", "Russian literature", "Christianity", "social reform"],
            "frameworks": ["literary-history", "pacifism", "social-theory"],
        }
    },

    # ── 5. Thomas Edison ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/202-Class-202/202thomas-edison.json",
        "slug": "thomas-edison",
        "era_correction": None,
        "data": {
            "summary": (
                "Thomas Edison (1847–1931) was an American inventor and businessman who holds the record for most patents in US history (1,093) and whose inventions — including the practical incandescent light bulb, the phonograph, and the motion picture camera — fundamentally transformed everyday life in the modern world. More than any individual inventor, he industrialized invention itself by creating the world's first research and development laboratory at Menlo Park, New Jersey (1876).\n\n"
                "Edison's greatest single achievement was making electric light commercially viable. His incandescent bulb (1879) was not the first, but was the first practical, long-lasting system — and critically, he invented the entire supporting infrastructure: power generation (Pearl Street Station, 1882, the first electrical utility), distribution networks, meters, switches, and sockets. This systems-thinking approach to invention, rather than any individual device, was his most lasting contribution.\n\n"
                "His phonograph (1877) — which recorded and played back sound for the first time in history — launched the recorded music industry. His Kinetoscope and collaboration with W.K.L. Dickson created the foundations of cinema. His 'War of Currents' against Nikola Tesla and George Westinghouse over DC vs. AC electricity, which he lost, ultimately shaped the AC electrical grid that powers the modern world.\n\n"
                "'Genius is one percent inspiration and ninety-nine percent perspiration,' he said — a philosophy that described his factory of invention, which employed hundreds of scientists before academic R&D labs existed."
            ),
            "causes": [
                "American industrial expansion creating demand for labor-saving electrical technologies",
                "Telegraphy industry as training ground providing technical foundation",
                "Capitalist investment culture in Gilded Age America funding inventors",
                "Competitive patent economy incentivizing prolific invention",
            ],
            "effects": [
                "Practical incandescent light bulb (1879) — electrification of civilization",
                "Pearl Street Station (1882) — world's first commercial electrical utility",
                "Phonograph (1877) — birth of the recorded music industry",
                "Kinetoscope — foundation of cinema",
                "Menlo Park laboratory — invention of the industrial R&D laboratory model",
                "1,093 US patents — record still stands",
                "General Electric Corporation — continuing innovation powerhouse",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Incandescent light bulb", "targetSlug": "incandescent-light-bulb", "note": "Practical commercial light (1879)"},
                {"type": "INFLUENCES", "target": "Phonograph", "targetSlug": "phonograph", "note": "First sound recording device (1877)"},
                {"type": "INFLUENCES", "target": "Cinema", "targetSlug": "cinema", "note": "Kinetoscope and Kinetograph created film medium"},
                {"type": "INFLUENCES", "target": "Electrical grid", "targetSlug": "electrical-grid", "note": "Pearl Street Station — first electrical utility (1882)"},
                {"type": "INFLUENCES", "target": "Nikola Tesla", "targetSlug": "nikola-tesla", "note": "War of Currents rival (AC vs DC)"},
                {"type": "INFLUENCES", "target": "George Westinghouse", "targetSlug": "george-westinghouse", "note": "AC electricity competitor who ultimately won"},
                {"type": "INFLUENCES", "target": "General Electric", "targetSlug": "general-electric", "note": "His Edison General Electric became GE"},
                {"type": "INFLUENCES", "target": "Research and development", "targetSlug": "research-and-development", "note": "Menlo Park — world's first industrial R&D lab"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "American inventor and industrialist"},
                {"type": "INFLUENCES", "target": "Recorded music industry", "targetSlug": "recorded-music", "note": "Phonograph launched mass music market"},
                {"type": "INFLUENCES", "target": "J.P. Morgan", "targetSlug": "jp-morgan", "note": "Key financier of Edison's electrical empire"},
                {"type": "INFLUENCES", "target": "Alexander Graham Bell", "targetSlug": "alexander-graham-bell", "note": "Contemporary inventor and competitor"},
                {"type": "INFLUENCES", "target": "Second Industrial Revolution", "targetSlug": "second-industrial-revolution", "note": "His electrical inventions defined the era"},
                {"type": "INFLUENCES", "target": "Modern laboratory science", "targetSlug": "laboratory-science", "note": "Created industrial model for systematic invention"},
                {"type": "OCCURS_IN", "target": "New Jersey", "targetSlug": "new-jersey", "note": "Menlo Park and West Orange labs"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Thomas Edison electrified civilization and invented the industrial research laboratory — his practical light bulb and electrical grid system transformed daily life, his phonograph created the music industry, and his R&D lab model became the template for modern technological innovation."
            },
            "quote": "'Genius is one percent inspiration and ninety-nine percent perspiration.' — Thomas Edison",
            "places": ["Menlo Park, New Jersey", "West Orange, New Jersey", "Milan, Ohio (birthplace)", "New York City"],
            "subjectHeadings": "Thomas Edison — Inventors and Industrialists — United States — Modern",
            "subjects": ["United States", "invention", "electricity", "industrial revolution", "phonograph", "cinema", "patents", "technology", "Gilded Age", "R&D"],
            "frameworks": ["technological-change", "scientific-revolution", "capitalism"],
        }
    },

    # ── 6. Simón Bolívar ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/220-Class-220/220simon-bolivar.json",
        "slug": "simon-bolivar",
        "era_correction": None,
        "data": {
            "summary": (
                "Simón Bolívar (1783–1830) was a Venezuelan military commander and political visionary who liberated six South American nations from Spanish colonial rule — Venezuela, Colombia, Ecuador, Peru, Bolivia, and Panama — earning him the title 'El Libertador' (The Liberator). No individual in the Western Hemisphere liberated more territory or more people, and he remains the most revered political figure in Latin American history.\n\n"
                "Born into Caracas' creole aristocracy, Bolívar was inspired by Enlightenment ideals and the American and French Revolutions. After a failed first republic (1811–12), he regrouped in exile and returned to fight a legendary campaign. His decisive victories — the Battle of Boyacá (1819) liberating Colombia, the Battle of Carabobo (1821) liberating Venezuela, and the Battle of Ayacucho (1824) ending Spanish rule in South America — were achieved against daunting odds across jungles, plains, and Andean passes.\n\n"
                "Bolívar's political vision went beyond independence. He dreamed of a united Gran Colombia (Venezuela, Colombia, Ecuador, Panama) and later a Pan-American confederation of republics — a vision of Latin American unity that remains aspirational. His Angostura Address (1819) and Jamaica Letter are founding documents of Latin American political thought.\n\n"
                "He died at 47 of tuberculosis, bitterly disappointed as Gran Colombia fragmented and his former allies turned against him. 'America is ungovernable,' he reportedly said on his deathbed. His image adorns six national currencies and countless public spaces across a continent he helped birth."
            ),
            "causes": [
                "Napoleonic invasion of Spain (1808) weakening colonial authority",
                "Enlightenment ideas of liberty and equality inspiring creole elites",
                "American and French Revolutions as models of successful independence",
                "Spanish colonial economic exclusion of creoles from political power",
            ],
            "effects": [
                "Independence of Venezuela (1821), Colombia (1819), Ecuador (1822), Peru (1821–24), Bolivia (1825), Panama",
                "Battle of Ayacucho (1824) — final defeat of Spanish forces in South America",
                "Gran Colombia — union of Venezuela, Colombia, Ecuador, Panama (1819–1831)",
                "Angostura Address (1819) — founding document of Latin American republicanism",
                "Pan-American ideal of hemispheric solidarity",
                "Bolivia — nation named after him",
                "Template for Latin American revolutionary and independence movements",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Venezuela", "targetSlug": "venezuela", "note": "Birthplace and first liberated nation"},
                {"type": "OCCURS_IN", "target": "Colombia", "targetSlug": "colombia", "note": "Liberated at Battle of Boyacá (1819)"},
                {"type": "INFLUENCES", "target": "Gran Colombia", "targetSlug": "gran-colombia", "note": "Union he founded and led (1819–1831)"},
                {"type": "INFLUENCES", "target": "Battle of Ayacucho", "targetSlug": "battle-of-ayacucho", "note": "Final defeat of Spanish South American forces (1824)"},
                {"type": "INFLUENCES", "target": "Antonio José de Sucre", "targetSlug": "antonio-jose-de-sucre", "note": "Most trusted general; won Battle of Ayacucho"},
                {"type": "INFLUENCES", "target": "Francisco de Miranda", "targetSlug": "francisco-de-miranda", "note": "Predecessor Venezuelan independence leader"},
                {"type": "INFLUENCES", "target": "José de San Martín", "targetSlug": "jose-de-san-martin", "note": "Fellow liberator; met at Guayaquil 1822"},
                {"type": "INFLUENCES", "target": "Spanish Empire", "targetSlug": "spanish-empire", "note": "Ended Spanish colonial rule across South America"},
                {"type": "INFLUENCES", "target": "Latin American independence movements", "targetSlug": "latin-american-independence", "note": "Inspired and led the continental liberation"},
                {"type": "INFLUENCES", "target": "Pan-Americanism", "targetSlug": "pan-americanism", "note": "Convened first Pan-American congress (1826)"},
                {"type": "INFLUENCES", "target": "Bolivia", "targetSlug": "bolivia", "note": "Nation named in his honor"},
                {"type": "INFLUENCES", "target": "Napoleonic Wars", "targetSlug": "napoleonic-wars", "note": "Napoleon's Spain invasion created independence window"},
                {"type": "INFLUENCES", "target": "American Revolution", "targetSlug": "american-revolution", "note": "Model for republican governance"},
                {"type": "INFLUENCES", "target": "French Revolution", "targetSlug": "french-revolution", "note": "Liberty ideals shaped his Enlightenment vision"},
                {"type": "OCCURS_IN", "target": "Peru", "targetSlug": "peru", "note": "Liberated and briefly ruled as dictator"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Simón Bolívar liberated six nations and ended Spanish colonial rule across an entire continent — the most successful military liberator in the Western Hemisphere and the founding visionary of Latin American independence, whose Pan-American dream still shapes hemispheric politics."
            },
            "quote": "'A state too expensive in itself, or by virtue of its dependencies, ultimately falls into decay; its free government is transformed into a tyranny; it disregards the principles which it should preserve, and finally degenerates into despotism.' — Simón Bolívar",
            "places": ["Caracas, Venezuela (birthplace)", "Bogotá, Colombia", "Lima, Peru", "Santa Marta, Colombia (death)"],
            "subjectHeadings": "Simón Bolívar — Revolutionary Leaders — Venezuela/South America — Modern",
            "subjects": ["Venezuela", "Colombia", "Peru", "Bolivia", "Ecuador", "independence", "Latin America", "military history", "revolution", "republicanism"],
            "frameworks": ["revolution", "empire-building", "political-philosophy"],
        }
    },

    # ── 7. Kublai Khan ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221kublai-khan.json",
        "slug": "kublai-khan",
        "era_correction": None,
        "data": {
            "summary": (
                "Kublai Khan (1215–1294) was the fifth Great Khan of the Mongol Empire and the founder and first Emperor of the Yuan dynasty of China — the first non-Chinese ruler to conquer and govern all of China. A grandson of Genghis Khan, he transformed the brutal Mongol conquests into a sophisticated imperial administration, presiding over the largest contiguous empire in history at its height and creating an era of unprecedented contact between East and West.\n\n"
                "Kublai's conquest of the Southern Song dynasty (completed 1279) unified China for the first time in three centuries. He ruled from Khanbaliq (modern Beijing), which he built as his capital, and governed through a meritocratic bureaucracy that retained Chinese Confucian administrative traditions alongside Mongol military power. His court attracted scientists, artists, engineers, and merchants from across Eurasia, including Marco Polo, who served at his court for seventeen years.\n\n"
                "The Pax Mongolica — the Mongol peace that made the Silk Road safe for travel — reached its apogee under Kublai. Chinese innovations including gunpowder, printing, and paper money flowed westward; Islamic and European goods and ideas moved east. His failed invasions of Japan (1274, 1281), Vietnam, and Java demonstrated the limits of Mongol power at sea.\n\n"
                "The Yuan dynasty he founded (1271–1368) lasted nearly a century, transmitted Chinese civilization to Central Asia, and left lasting demographic and cultural imprints across East Asia. Samuel Taylor Coleridge immortalized him in 'Kubla Khan' (1797): 'In Xanadu did Kubla Khan / A stately pleasure-dome decree.'"
            ),
            "causes": [
                "Mongol conquests of Genghis Khan and successors unifying northern China and Eurasia",
                "Death of Möngke Khan (1259) triggering succession crisis Kublai won",
                "Southern Song dynasty's political and military fragmentation enabling conquest",
                "Chinese administrative traditions providing governance model for conquered territories",
            ],
            "effects": [
                "Yuan dynasty (1271–1368) — first complete non-Han conquest of all China",
                "Unification of China under Mongol rule for the first time in three centuries",
                "Pax Mongolica — Silk Road security enabling East-West trade and cultural exchange",
                "Marco Polo's journey (1271–1295) — transmitting China's wonders to Europe",
                "Beijing (Khanbaliq) established as imperial capital of China",
                "Failed invasions of Japan (kamikaze divine winds) — limits of Mongol naval power",
                "Paper money (banknotes) introduced as primary currency across the empire",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Mongol Empire", "targetSlug": "mongol-empire", "note": "Fifth and final Great Khan"},
                {"type": "OCCURS_IN", "target": "Yuan dynasty", "targetSlug": "yuan-dynasty", "note": "Founder and first emperor"},
                {"type": "OCCURS_IN", "target": "China", "targetSlug": "china", "note": "Conquered and unified all of China"},
                {"type": "INFLUENCES", "target": "Genghis Khan", "targetSlug": "genghis-khan", "note": "Grandfather whose empire he inherited and transformed"},
                {"type": "INFLUENCES", "target": "Marco Polo", "targetSlug": "marco-polo", "note": "Venetian merchant who served 17 years at his court"},
                {"type": "INFLUENCES", "target": "Silk Road", "targetSlug": "silk-road", "note": "Pax Mongolica enabled its greatest era of trade"},
                {"type": "INFLUENCES", "target": "Southern Song dynasty", "targetSlug": "southern-song-dynasty", "note": "Conquered and ended Chinese Song dynasty (1279)"},
                {"type": "INFLUENCES", "target": "Invasions of Japan", "targetSlug": "mongol-invasions-of-japan", "note": "Two failed invasions (1274, 1281) — defeated by typhoon"},
                {"type": "INFLUENCES", "target": "Beijing", "targetSlug": "beijing", "note": "Built Khanbaliq as Mongol imperial capital"},
                {"type": "INFLUENCES", "target": "Pax Mongolica", "targetSlug": "pax-mongolica", "note": "Era of Mongol peace enabling Eurasian exchange"},
                {"type": "INFLUENCES", "target": "Paper money", "targetSlug": "paper-money", "note": "Standardized paper currency across China and empire"},
                {"type": "INFLUENCES", "target": "Ibn Battuta", "targetSlug": "ibn-battuta", "note": "Later traveler whose accounts describe Yuan China"},
                {"type": "OCCURS_IN", "target": "Mongolia", "targetSlug": "mongolia", "note": "Ethnic origin and Mongol steppe homeland"},
                {"type": "INFLUENCES", "target": "Samuel Taylor Coleridge", "targetSlug": "samuel-taylor-coleridge", "note": "'Kubla Khan' poem (1797) immortalized his Xanadu"},
                {"type": "INFLUENCES", "target": "Confucian bureaucracy", "targetSlug": "confucian-bureaucracy", "note": "Retained Chinese administrative traditions under Mongol rule"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Kublai Khan completed the Mongol conquest of China, founded the Yuan dynasty, and presided over the Pax Mongolica — the greatest era of East-West trade and cultural exchange before modernity, during which Marco Polo introduced China to Europe and Chinese inventions flowed westward."
            },
            "quote": "'In Xanadu did Kubla Khan / A stately pleasure-dome decree.' — Samuel Taylor Coleridge, 'Kubla Khan' (1797)",
            "places": ["Khanbaliq (modern Beijing), China", "Karakorum, Mongolia", "Xanadu (Shangdu), Inner Mongolia"],
            "subjectHeadings": "Kublai Khan — Emperors and Rulers — China/Mongolia — Medieval",
            "subjects": ["China", "Mongolia", "Mongol Empire", "Yuan dynasty", "Silk Road", "medieval Asia", "Marco Polo", "conquest", "East-West exchange", "Beijing"],
            "frameworks": ["empire-building", "trade-networks", "state-formation"],
        }
    },

    # ── 8. Vasco da Gama ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/281-Class-281/281vasco-da-gama.json",
        "slug": "vasco-da-gama",
        "era_correction": "Early Modern",  # currently Medieval — he lived 1460s–1524
        "data": {
            "summary": (
                "Vasco da Gama (c. 1460–1524) was a Portuguese explorer who became the first European to reach India by sea, completing the first direct maritime trade route from Europe to Asia (1497–1499) and inaugurating the Age of Exploration's most consequential discovery. His voyage around the Cape of Good Hope and across the Indian Ocean to Calicut (Kozhikode) shattered the Ottoman and Venetian monopoly on Asian trade routes and shifted the center of world commerce from the Mediterranean to the Atlantic.\n\n"
                "Departing Lisbon on July 8, 1497 with four ships and 170 men, da Gama sailed south along the West African coast, rounded the Cape of Good Hope, crossed the Indian Ocean with the help of an Arab navigator (likely Ahmad ibn Mājid), and arrived in Calicut on May 20, 1498. His return voyage established that a profitable direct spice trade was possible — though he was contemptuous of local rulers and his initial cargo proved inadequate for Indian markets.\n\n"
                "His second voyage (1502–1503) was larger and explicitly military — he bombarded Calicut, established Portuguese trading forts, and laid the foundation for the Estado da India (Portuguese India). The spice trade that followed made Portugal the richest nation in Europe for half a century and initiated the globalization of world trade.\n\n"
                "Da Gama's voyages ended the Silk Road era as the primary conduit of luxury trade between East and West, triggered European imperialism in Asia, and connected the Indian Ocean to the Atlantic in a permanent global economic system. He died in Goa in 1524 as Viceroy of India, and his career was immortalized in Luís de Camões's epic The Lusiads (1572)."
            ),
            "causes": [
                "Portuguese crown's decade-long exploration of the African coast (Bartolomeu Dias rounding the Cape, 1488)",
                "Ottoman Empire's control of Levant trade routes raising spice prices in Europe",
                "Venetian monopoly on Mediterranean trade motivating Atlantic alternatives",
                "Prince Henry the Navigator's systematic school of maritime exploration",
            ],
            "effects": [
                "First direct European sea route to India (1498) — ending Ottoman/Venetian monopoly",
                "Opening of direct spice trade making Portugal richest European nation",
                "Estado da India — Portuguese maritime empire in the Indian Ocean",
                "Destruction of Arab-controlled Indian Ocean trade networks",
                "Foundation of Goa as Portuguese capital in India (still holds colonial legacy)",
                "Triggering of European imperialism across Asia and Indian Ocean littoral",
                "Globalization of world trade — Atlantic replaces Mediterranean as commercial center",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Portugal", "targetSlug": "portugal", "note": "Birthplace and royal patron"},
                {"type": "INFLUENCES", "target": "Age of Exploration", "targetSlug": "age-of-exploration", "note": "Most consequential voyage of the Age of Exploration"},
                {"type": "INFLUENCES", "target": "India", "targetSlug": "india", "note": "First European to reach India by sea (Calicut, 1498)"},
                {"type": "INFLUENCES", "target": "Estado da India", "targetSlug": "estado-da-india", "note": "Portuguese maritime empire he helped found"},
                {"type": "INFLUENCES", "target": "Spice trade", "targetSlug": "spice-trade", "note": "Opened direct Portuguese spice route to Asia"},
                {"type": "INFLUENCES", "target": "Bartolomeu Dias", "targetSlug": "bartolomeu-dias", "note": "Dias rounded Cape of Good Hope (1488) enabling da Gama's route"},
                {"type": "INFLUENCES", "target": "Ottoman Empire", "targetSlug": "ottoman-empire", "note": "His route bypassed Ottoman trade control"},
                {"type": "INFLUENCES", "target": "Calicut (Kozhikode)", "targetSlug": "calicut", "note": "Destination of his first voyage (1498)"},
                {"type": "INFLUENCES", "target": "Luís de Camões", "targetSlug": "luis-de-camoes", "note": "Da Gama hero of The Lusiads (1572)"},
                {"type": "INFLUENCES", "target": "Cape of Good Hope", "targetSlug": "cape-of-good-hope", "note": "Rounded en route to India"},
                {"type": "INFLUENCES", "target": "Indian Ocean trade", "targetSlug": "indian-ocean-trade", "note": "Disrupted Arab-controlled Indian Ocean commerce"},
                {"type": "INFLUENCES", "target": "Goa", "targetSlug": "goa", "note": "Died there as Viceroy of India (1524)"},
                {"type": "INFLUENCES", "target": "Manuel I of Portugal", "targetSlug": "manuel-i-of-portugal", "note": "Royal patron of first and second voyages"},
                {"type": "INFLUENCES", "target": "Afonso de Albuquerque", "targetSlug": "afonso-de-albuquerque", "note": "Successor who consolidated Portuguese Indian Ocean empire"},
                {"type": "INFLUENCES", "target": "Christopher Columbus", "targetSlug": "christopher-columbus", "note": "Contemporary — Columbus west, da Gama east, both 1492–1499"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Vasco da Gama's voyage to India by sea ended the Silk Road era, transferred world commercial hegemony from the Mediterranean to the Atlantic, and inaugurated five centuries of European maritime imperialism in Asia — one of the decisive turning points of global history."
            },
            "quote": "'We come in search of Christians and spices.' — Vasco da Gama (upon arriving in Calicut, 1498)",
            "places": ["Sines, Portugal (birthplace)", "Calicut (Kozhikode), India", "Goa, India (death)", "Cape of Good Hope, South Africa"],
            "subjectHeadings": "Vasco da Gama — Explorers and Navigators — Portugal — Early Modern",
            "subjects": ["Portugal", "India", "exploration", "spice trade", "Age of Exploration", "imperialism", "Indian Ocean", "sea routes", "Goa", "maritime history"],
            "frameworks": ["empire-building", "trade-networks", "exploration"],
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

    print(f"Batch 59 enrichment — {len(ENRICHMENTS)} entities\n")

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
