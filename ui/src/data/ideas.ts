/* ─── Ideas That Transformed the World — Master Registry ─── */
/* Ideas are the KEY actor in the Annals knowledge graph.                        */
/* While People die, Institutions crumble, and Events pass —                    */
/* Ideas propagate, mutate, merge, and compound across millennia.               */
/* Every other actor (Person, Institution, Movement) is merely                  */
/* a vehicle for the Idea that outlives them all.                                */

export interface HistoricalIdea {
  slug: string
  name: string
  domain: string
  subdomain: string
  era: string
  yearOrigin: number
  yearLabel: string
  originator: string
  originatorType: 'Person' | 'Institution' | 'Movement' | 'Civilization' | 'Collective'
  originPlace: string
  region: string
  description: string
  impact: string
  /** Slugs of ideas this one builds on or descends from */
  parentIdeas: string[]
  /** Slugs of ideas this one enabled or gave rise to */
  childIdeas: string[]
  transformativeScore: number // 1-10 how much it changed humanity
}

export interface IdeaDomain {
  id: string
  label: string
  color: string
  icon: string
  count?: number
}

export const IDEA_DOMAINS: IdeaDomain[] = [
  { id: 'philosophy',    label: 'Philosophy & Epistemology',   color: '#6B3FA0', icon: 'Brain' },
  { id: 'physics',       label: 'Physics & Cosmology',         color: '#4A90D9', icon: 'Atom' },
  { id: 'mathematics',   label: 'Mathematics & Logic',         color: '#2F855A', icon: 'Binary' },
  { id: 'biology',       label: 'Biology & Life Sciences',     color: '#38B2AC', icon: 'Dna' },
  { id: 'chemistry',     label: 'Chemistry & Materials',       color: '#DD6B20', icon: 'FlaskConical' },
  { id: 'medicine',      label: 'Medicine & Health',           color: '#C53030', icon: 'Heart' },
  { id: 'politics',      label: 'Politics & Governance',       color: '#8B3A3A', icon: 'Landmark' },
  { id: 'economics',     label: 'Economics & Trade',           color: '#D4AF37', icon: 'TrendingUp' },
  { id: 'religion',      label: 'Religion & Spirituality',     color: '#805AD5', icon: 'Sparkles' },
  { id: 'technology',    label: 'Technology & Engineering',     color: '#718096', icon: 'Cpu' },
  { id: 'social',        label: 'Social & Cultural Theory',    color: '#D69E2E', icon: 'Users' },
  { id: 'environment',   label: 'Environment & Earth Science', color: '#276749', icon: 'Globe' },
  { id: 'information',   label: 'Information & Computing',     color: '#3182CE', icon: 'Database' },
  { id: 'art',           label: 'Art & Aesthetics',            color: '#B83280', icon: 'Palette' },
]

/* ───────────────────────────────────────────────────────────
   WHY IDEAS ARE THE KEY ACTOR
   ───────────────────────────────────────────────────────────
   
   People die. Alexander lived 32 years.
   Institutions collapse. Rome lasted 1,000 years.
   Events pass. Wars end.
   
   But Ideas? Democracy is 2,500 years old and spreading.
   The Scientific Method is 400 years old and accelerating.
   Monotheism is 3,400 years old and believed by 4 billion.
   
   Every Person is a vessel for Ideas.
   Every Institution is a structure to propagate Ideas.
   Every Event is a collision of Ideas.
   Every Movement is an Idea that found legs.
   
   Ideas are the DNA of civilization.
   ─────────────────────────────────────────────────────────── */

export const IDEAS: HistoricalIdea[] = [
  /* ═══════════════════════════════════════════════════════════
     PREHISTORIC IDEAS — The First Abstractions
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'animism', name: 'Animism', domain: 'religion', subdomain: 'Belief Systems',
    era: 'prehistoric', yearOrigin: -100000, yearLabel: '~100,000 BCE',
    originator: 'Early Homo sapiens', originatorType: 'Collective',
    originPlace: 'Africa', region: 'East Africa',
    description: 'The belief that all objects, places, and creatures possess a spiritual essence. The first metaphysical framework — humans imagining that the world has interior life.',
    impact: 'Foundation of ALL subsequent religious thought. From animism came shamanism, polytheism, and eventually monotheism. Every religion carries animism\'s DNA.',
    parentIdeas: [], childIdeas: ['shamanism', 'totemism', 'polytheism'],
    transformativeScore: 10,
  },
  {
    slug: 'tool-making-concept', name: 'Intentional Tool-Making', domain: 'technology', subdomain: 'Engineering',
    era: 'prehistoric', yearOrigin: -2500000, yearLabel: '~2,500,000 BCE',
    originator: 'Homo habilis', originatorType: 'Collective',
    originPlace: 'Olduvai Gorge, Tanzania', region: 'East Africa',
    description: 'The concept that natural materials can be intentionally modified to serve a purpose. Not just using a stick — but envisioning a better stick and making it.',
    impact: 'The idea that launched the human species. Every technology, from stone axes to smartphones, descends from this single cognitive leap.',
    parentIdeas: [], childIdeas: ['fire-control', 'agriculture-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'fire-control', name: 'Control of Fire', domain: 'technology', subdomain: 'Energy',
    era: 'prehistoric', yearOrigin: -1000000, yearLabel: '~1,000,000 BCE',
    originator: 'Homo erectus', originatorType: 'Collective',
    originPlace: 'Wonderwerk Cave, South Africa', region: 'Southern Africa',
    description: 'The understanding that fire can be captured, maintained, and directed. Cooking food, warmth, protection from predators, and social gathering around the hearth.',
    impact: 'Cooking enabled brain growth (smaller gut = bigger brain). Fire extended the day, enabling storytelling and abstract thought. Literally made modern humans possible.',
    parentIdeas: ['tool-making-concept'], childIdeas: ['metallurgy-concept', 'ceramics-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'symbolic-thinking', name: 'Symbolic Representation', domain: 'philosophy', subdomain: 'Cognition',
    era: 'prehistoric', yearOrigin: -100000, yearLabel: '~100,000 BCE',
    originator: 'Homo sapiens', originatorType: 'Collective',
    originPlace: 'Blombos Cave, South Africa', region: 'Southern Africa',
    description: 'The ability to let one thing represent another: a line means a river, a carved figure means a deity, a sound means a word. The foundation of all language, art, and mathematics.',
    impact: 'Without symbolic thinking, there is no language, no writing, no mathematics, no science, no religion, no law. It is the meta-idea that enables all other ideas.',
    parentIdeas: [], childIdeas: ['language-concept', 'counting-concept', 'art-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'language-concept', name: 'Spoken Language', domain: 'social', subdomain: 'Communication',
    era: 'prehistoric', yearOrigin: -100000, yearLabel: '~100,000 BCE',
    originator: 'Homo sapiens', originatorType: 'Collective',
    originPlace: 'Africa (exact location unknown)', region: 'East Africa',
    description: 'Structured vocal communication using symbolic sounds with grammar. The ability to transmit complex information, coordinate action, and share abstract concepts.',
    impact: 'Language IS civilization. It enabled cooperation at scale, accumulation of knowledge across generations, and the social structures that define humanity.',
    parentIdeas: ['symbolic-thinking'], childIdeas: ['oral-tradition', 'writing-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'agriculture-concept', name: 'Agriculture (The Neolithic Idea)', domain: 'technology', subdomain: 'Food Production',
    era: 'prehistoric', yearOrigin: -10000, yearLabel: '~10,000 BCE',
    originator: 'Neolithic farmers', originatorType: 'Collective',
    originPlace: 'Fertile Crescent', region: 'West Asia',
    description: 'The revolutionary insight that wild plants can be deliberately cultivated and animals domesticated. Instead of following food, grow it. Stay in one place.',
    impact: 'Created civilization itself. Without agriculture: no surplus, no specialization, no cities, no writing, no armies, no states, no history. The most consequential idea after language.',
    parentIdeas: ['tool-making-concept', 'fire-control'], childIdeas: ['surplus-concept', 'property-concept', 'irrigation-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'counting-concept', name: 'Counting & Numeracy', domain: 'mathematics', subdomain: 'Arithmetic',
    era: 'prehistoric', yearOrigin: -35000, yearLabel: '~35,000 BCE',
    originator: 'Upper Paleolithic humans', originatorType: 'Collective',
    originPlace: 'Lebombo Mountains, Eswatini', region: 'Southern Africa',
    description: 'Tally marks on the Lebombo bone — the realization that quantities can be recorded and compared. The birth of mathematics.',
    impact: 'From tally marks to calculus, quantum mechanics, and AI. Every quantitative discipline in existence descends from this simple act of counting.',
    parentIdeas: ['symbolic-thinking'], childIdeas: ['writing-concept', 'zero-concept', 'geometry-concept'],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     ANCIENT IDEAS — The Axial Age & Classical Foundations
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'writing-concept', name: 'Writing Systems', domain: 'technology', subdomain: 'Information',
    era: 'ancient', yearOrigin: -3400, yearLabel: '~3400 BCE',
    originator: 'Sumerian temple scribes', originatorType: 'Institution',
    originPlace: 'Uruk, Mesopotamia', region: 'West Asia',
    description: 'Cuneiform: the conversion of speech into visible, permanent marks. Initially for accounting (grain tallies), it rapidly expanded to record laws, myths, letters, and history.',
    impact: 'Writing ended prehistory and began history. It enabled law codes, religious texts, scientific records, and bureaucracy. Without writing, knowledge dies with each generation.',
    parentIdeas: ['symbolic-thinking', 'counting-concept', 'language-concept'], childIdeas: ['alphabet-concept', 'codification-of-law', 'historiography'],
    transformativeScore: 10,
  },
  {
    slug: 'monotheism', name: 'Monotheism', domain: 'religion', subdomain: 'Theology',
    era: 'ancient', yearOrigin: -1350, yearLabel: '~1350 BCE',
    originator: 'Akhenaten / Moses (contested)', originatorType: 'Person',
    originPlace: 'Egypt / Sinai', region: 'North Africa',
    description: 'The radical claim that there is ONE God, not many. Akhenaten\'s Atenism and/or Mosaic monotheism rejected the polytheistic worldview that had dominated for millennia.',
    impact: 'Judaism, Christianity, Islam — 4 billion believers today. Monotheism restructured morality, politics, law, and identity across Eurasia and Africa. The most believed idea in human history.',
    parentIdeas: ['animism', 'polytheism'], childIdeas: ['covenantal-theology', 'natural-law-theory', 'islamic-philosophy'],
    transformativeScore: 10,
  },
  {
    slug: 'democracy-concept', name: 'Democracy', domain: 'politics', subdomain: 'Governance',
    era: 'ancient', yearOrigin: -508, yearLabel: '508 BCE',
    originator: 'Cleisthenes', originatorType: 'Person',
    originPlace: 'Athens, Greece', region: 'Western Europe',
    description: 'Demos (people) + kratos (power). The idea that the governed should choose their governors. Athenian citizens voted directly on laws and policy in the Assembly.',
    impact: 'Dormant for 2,000 years, then revived during the Enlightenment. Today ~60% of humanity lives under some form of democratic governance. The idea that power belongs to all, not to kings.',
    parentIdeas: ['codification-of-law'], childIdeas: ['republic-concept', 'social-contract', 'human-rights'],
    transformativeScore: 10,
  },
  {
    slug: 'logic-formal', name: 'Formal Logic', domain: 'philosophy', subdomain: 'Epistemology',
    era: 'ancient', yearOrigin: -350, yearLabel: '~350 BCE',
    originator: 'Aristotle', originatorType: 'Person',
    originPlace: 'Athens, Greece', region: 'Western Europe',
    description: 'The Organon: syllogisms, deduction, categories, and the laws of thought (identity, non-contradiction, excluded middle). The first systematic framework for valid reasoning.',
    impact: 'Foundation of ALL rigorous thinking: mathematics, science, law, computer science. Boolean logic (AND/OR/NOT) that powers every computer descends directly from Aristotle.',
    parentIdeas: ['symbolic-thinking'], childIdeas: ['scientific-method', 'mathematical-proof', 'boolean-logic'],
    transformativeScore: 10,
  },
  {
    slug: 'geometry-concept', name: 'Euclidean Geometry', domain: 'mathematics', subdomain: 'Geometry',
    era: 'ancient', yearOrigin: -300, yearLabel: '~300 BCE',
    originator: 'Euclid', originatorType: 'Person',
    originPlace: 'Alexandria, Egypt', region: 'North Africa',
    description: 'The Elements: 13 books deriving 465 propositions from 5 axioms. The first axiomatic system — proving truths from self-evident starting points.',
    impact: 'The most influential textbook in history (in print for 2,300 years). Taught every architect, engineer, and physicist. Inspired the entire axiomatic method in all of mathematics.',
    parentIdeas: ['counting-concept', 'logic-formal'], childIdeas: ['non-euclidean-geometry', 'calculus', 'mathematical-proof'],
    transformativeScore: 9,
  },
  {
    slug: 'zero-concept', name: 'The Concept of Zero', domain: 'mathematics', subdomain: 'Number Theory',
    era: 'ancient', yearOrigin: -300, yearLabel: '~300 BCE (Babylonian placeholder) / 628 CE (full number)',
    originator: 'Babylonian scribes → Brahmagupta', originatorType: 'Person',
    originPlace: 'Babylon → Ujjain, India', region: 'South Asia',
    description: 'First as a placeholder in Babylonian positional notation, then as a full number with arithmetic rules by Brahmagupta. The idea that "nothing" is "something."',
    impact: 'Without zero: no place-value notation, no algebra, no calculus, no computers (binary = 0s and 1s). Zero traveled from India → Arabia → Europe and revolutionized each.',
    parentIdeas: ['counting-concept'], childIdeas: ['algebra-concept', 'calculus', 'binary-system'],
    transformativeScore: 10,
  },
  {
    slug: 'codification-of-law', name: 'Codified Written Law', domain: 'politics', subdomain: 'Jurisprudence',
    era: 'ancient', yearOrigin: -1754, yearLabel: '~1754 BCE',
    originator: 'Hammurabi', originatorType: 'Person',
    originPlace: 'Babylon, Mesopotamia', region: 'West Asia',
    description: 'The Code of Hammurabi: 282 laws carved in stone for all to see. The idea that laws should be written, public, and apply consistently — not merely the king\'s whim.',
    impact: 'Foundation of rule of law. Every legal system — Roman law, common law, civil law, sharia — builds on this principle. The idea that law should be knowable and predictable.',
    parentIdeas: ['writing-concept'], childIdeas: ['democracy-concept', 'natural-law-theory', 'human-rights'],
    transformativeScore: 9,
  },
  {
    slug: 'heliocentrism-ancient', name: 'Heliocentrism (Ancient)', domain: 'physics', subdomain: 'Astronomy',
    era: 'ancient', yearOrigin: -270, yearLabel: '~270 BCE',
    originator: 'Aristarchus of Samos', originatorType: 'Person',
    originPlace: 'Samos / Alexandria', region: 'Western Europe',
    description: 'Earth revolves around the Sun, not the reverse. Aristarchus proposed this 1,800 years before Copernicus but was dismissed by a geocentric consensus.',
    impact: 'The idea that our intuitions about our place in the universe can be wrong. Suppressed for millennia, then revived to trigger the Scientific Revolution.',
    parentIdeas: ['geometry-concept'], childIdeas: ['copernican-heliocentrism'],
    transformativeScore: 8,
  },
  {
    slug: 'republic-concept', name: 'The Republic (Res Publica)', domain: 'politics', subdomain: 'Governance',
    era: 'ancient', yearOrigin: -509, yearLabel: '509 BCE',
    originator: 'Roman aristocracy', originatorType: 'Institution',
    originPlace: 'Rome', region: 'Western Europe',
    description: 'The "public thing" — governance through elected magistrates, a Senate, and constitutional checks. Power distributed among offices with term limits.',
    impact: 'The Roman Republic\'s model influenced every republic since: the US Constitution, the French Republic, and 150+ modern republics. Separation of powers began here.',
    parentIdeas: ['democracy-concept', 'codification-of-law'], childIdeas: ['separation-of-powers', 'social-contract'],
    transformativeScore: 9,
  },
  {
    slug: 'buddhist-philosophy', name: 'Buddhist Philosophy (Four Noble Truths)', domain: 'religion', subdomain: 'Soteriology',
    era: 'ancient', yearOrigin: -528, yearLabel: '~528 BCE',
    originator: 'Siddhartha Gautama (Buddha)', originatorType: 'Person',
    originPlace: 'Bodh Gaya, India', region: 'South Asia',
    description: 'Life is suffering (dukkha); suffering arises from desire (tanha); cessation is possible (nirvana); the Eightfold Path leads there. A diagnostic framework for the human condition.',
    impact: '500+ million adherents. Spread across all of Asia. Influenced psychology (mindfulness-based therapy), neuroscience, and Western philosophy. The idea that suffering has a cure.',
    parentIdeas: ['animism'], childIdeas: ['zen-buddhism', 'mindfulness-concept'],
    transformativeScore: 9,
  },
  {
    slug: 'confucian-ethics', name: 'Confucian Ethics', domain: 'philosophy', subdomain: 'Ethics',
    era: 'ancient', yearOrigin: -500, yearLabel: '~500 BCE',
    originator: 'Confucius (Kong Qiu)', originatorType: 'Person',
    originPlace: 'Qufu, Lu (Shandong), China', region: 'East Asia',
    description: 'Ren (benevolence), li (ritual propriety), xiao (filial piety), and junzi (the exemplary person). Society is ordered by relationships, duty, and moral cultivation.',
    impact: 'Shaped 2,500 years of Chinese, Korean, Japanese, and Vietnamese civilization. Confucian meritocracy influenced the examination system and remains the cultural operating system of East Asia.',
    parentIdeas: [], childIdeas: ['meritocracy-concept', 'neo-confucianism'],
    transformativeScore: 9,
  },
  {
    slug: 'atomic-theory-ancient', name: 'Atomism', domain: 'physics', subdomain: 'Matter Theory',
    era: 'ancient', yearOrigin: -460, yearLabel: '~460 BCE',
    originator: 'Democritus / Leucippus', originatorType: 'Person',
    originPlace: 'Abdera, Thrace', region: 'Western Europe',
    description: 'All matter is composed of tiny indivisible particles (atomos) moving through void. Properties arise from atomic shape, arrangement, and motion — not divine will.',
    impact: 'Suppressed for 2,000 years by Aristotelian and religious orthodoxy, then revived by Dalton (1803). The ancient idea that MATTER explains matter — no gods needed.',
    parentIdeas: ['logic-formal'], childIdeas: ['dalton-atomic-theory', 'kinetic-theory', 'quantum-mechanics'],
    transformativeScore: 9,
  },
  {
    slug: 'polytheism', name: 'Polytheism', domain: 'religion', subdomain: 'Theology',
    era: 'ancient', yearOrigin: -4000, yearLabel: '~4000 BCE',
    originator: 'Sumerian/Egyptian priesthoods', originatorType: 'Institution',
    originPlace: 'Mesopotamia / Egypt', region: 'West Asia',
    description: 'Multiple gods governing different aspects of reality: sky, earth, war, love, death. A structured pantheon with hierarchies, myths, and rituals.',
    impact: 'Dominated human belief for 5,000+ years. Greek, Roman, Norse, Hindu, Shinto pantheons shaped art, literature, law, and morality across the ancient world.',
    parentIdeas: ['animism'], childIdeas: ['monotheism', 'mythology-as-framework'],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     MEDIEVAL IDEAS — Synthesis, Preservation, Transmission
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'algebra-concept', name: 'Algebra', domain: 'mathematics', subdomain: 'Abstract Mathematics',
    era: 'medieval', yearOrigin: 820, yearLabel: '~820 CE',
    originator: 'Al-Khwarizmi', originatorType: 'Person',
    originPlace: 'Baghdad, House of Wisdom', region: 'West Asia',
    description: 'Al-Kitab al-Mukhtasar: systematic methods for solving equations using variables. The word "algebra" comes from "al-jabr" (restoration/completion).',
    impact: 'Made modern science, engineering, and computing possible. Without algebra: no physics equations, no economics models, no algorithms, no AI. "Algorithm" is a Latinization of Al-Khwarizmi.',
    parentIdeas: ['zero-concept', 'geometry-concept'], childIdeas: ['calculus', 'algorithm-concept', 'modern-cryptography'],
    transformativeScore: 10,
  },
  {
    slug: 'islamic-philosophy', name: 'Islamic Golden Age Philosophy', domain: 'philosophy', subdomain: 'Synthesis',
    era: 'medieval', yearOrigin: 800, yearLabel: '~800 CE',
    originator: 'Al-Kindi, Ibn Sina, Ibn Rushd', originatorType: 'Movement',
    originPlace: 'Baghdad → Córdoba', region: 'West Asia',
    description: 'The systematic translation, commentary, and extension of Greek philosophy through an Islamic lens. Preserved and transmitted Aristotle, Plato, and Galen to the Latin West.',
    impact: 'Without Islamic philosophy, Europe would have LOST Aristotle. Aquinas\'s entire system depends on Ibn Rushd\'s commentaries. The Islamic world was the bridge between antiquity and modernity.',
    parentIdeas: ['logic-formal', 'monotheism'], childIdeas: ['scholasticism', 'scientific-method'],
    transformativeScore: 9,
  },
  {
    slug: 'scholasticism', name: 'Scholasticism', domain: 'philosophy', subdomain: 'Methodology',
    era: 'medieval', yearOrigin: 1100, yearLabel: '~1100 CE',
    originator: 'Peter Abelard / Thomas Aquinas', originatorType: 'Person',
    originPlace: 'Paris / Naples', region: 'Western Europe',
    description: 'Rigorous dialectical method: question, objection, reply, determination. Sic et Non — reconciling contradictory authorities through systematic reasoning.',
    impact: 'Created the university as an institution of organized inquiry. The disputation format is the ancestor of the scientific peer-review process and legal argumentation.',
    parentIdeas: ['islamic-philosophy', 'logic-formal'], childIdeas: ['scientific-method', 'university-concept'],
    transformativeScore: 8,
  },
  {
    slug: 'compass-navigation', name: 'Magnetic Compass Navigation', domain: 'technology', subdomain: 'Navigation',
    era: 'medieval', yearOrigin: 1040, yearLabel: '~1040 CE',
    originator: 'Chinese scholars (Song Dynasty)', originatorType: 'Civilization',
    originPlace: 'China', region: 'East Asia',
    description: 'Using magnetized iron needles floating in water to find magnetic north. Transmitted to Europe by ~1190. Combined with portolan charts for open-ocean navigation.',
    impact: 'Without the compass: no Age of Exploration, no Columbus, no Magellan, no global trade networks. The compass literally connected the world.',
    parentIdeas: ['tool-making-concept'], childIdeas: ['age-of-exploration', 'cartography-revolution'],
    transformativeScore: 9,
  },
  {
    slug: 'printing-press-idea', name: 'Movable Type Printing', domain: 'technology', subdomain: 'Communication',
    era: 'medieval', yearOrigin: 1040, yearLabel: '1040 CE (Bi Sheng) / 1440 CE (Gutenberg)',
    originator: 'Bi Sheng → Johannes Gutenberg', originatorType: 'Person',
    originPlace: 'China → Mainz, Germany', region: 'Western Europe',
    description: 'Reusable characters/letters cast in metal and arranged to print pages. Gutenberg\'s press combined movable type, oil-based ink, and the screw press.',
    impact: 'Gutenberg\'s press created the information revolution: Reformation, Scientific Revolution, Enlightenment, democracy. Books went from 30,000 in all of Europe to 20 million in 50 years.',
    parentIdeas: ['writing-concept'], childIdeas: ['mass-literacy', 'scientific-publishing', 'reformation-ideas'],
    transformativeScore: 10,
  },
  {
    slug: 'university-concept', name: 'The University', domain: 'social', subdomain: 'Education',
    era: 'medieval', yearOrigin: 859, yearLabel: '859 CE (al-Qarawiyyin) / 1088 CE (Bologna)',
    originator: 'Fatima al-Fihri (Fez) / Bologna scholars', originatorType: 'Person',
    originPlace: 'Fez, Morocco → Bologna, Italy', region: 'North Africa',
    description: 'A self-governing community of scholars with permanent faculties, degree-granting authority, and academic freedom. Al-Qarawiyyin (859) is the oldest; Bologna (1088) the oldest European.',
    impact: 'Universities are idea factories. Every major intellectual revolution since — Reformation, Scientific Revolution, Enlightenment, Industrial Revolution — was incubated in universities.',
    parentIdeas: ['scholasticism'], childIdeas: ['scientific-revolution', 'academic-freedom'],
    transformativeScore: 9,
  },
  {
    slug: 'natural-law-theory', name: 'Natural Law Theory', domain: 'philosophy', subdomain: 'Political Philosophy',
    era: 'medieval', yearOrigin: 1270, yearLabel: '~1270 CE',
    originator: 'Thomas Aquinas (building on Aristotle/Cicero)', originatorType: 'Person',
    originPlace: 'Paris / Naples', region: 'Western Europe',
    description: 'Moral principles are inherent in nature and discoverable by reason, not merely decreed by authority. Human laws must conform to natural/divine law to be legitimate.',
    impact: 'Foundation of human rights philosophy. Locke, Jefferson, and the UN Declaration of Human Rights all build on natural law. The idea that rights are NOT granted by governments.',
    parentIdeas: ['logic-formal', 'monotheism', 'codification-of-law'], childIdeas: ['social-contract', 'human-rights', 'constitutionalism'],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     EARLY MODERN IDEAS — The Scientific Revolution & Enlightenment
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'copernican-heliocentrism', name: 'Copernican Heliocentrism', domain: 'physics', subdomain: 'Astronomy',
    era: 'earlyModern', yearOrigin: 1543, yearLabel: '1543 CE',
    originator: 'Nicolaus Copernicus', originatorType: 'Person',
    originPlace: 'Frauenburg (Frombork), Poland', region: 'Eastern Europe',
    description: 'De Revolutionibus: the Sun, not Earth, is the center. Published on his deathbed. Destroyed the 1,400-year Ptolemaic model and the theological cosmology it supported.',
    impact: 'Triggered the Scientific Revolution. If Earth isn\'t the center, maybe humans aren\'t either. Opened the door to Kepler, Galileo, Newton, and all of modern astronomy.',
    parentIdeas: ['heliocentrism-ancient', 'geometry-concept'], childIdeas: ['scientific-method', 'newtonian-mechanics'],
    transformativeScore: 10,
  },
  {
    slug: 'scientific-method', name: 'The Scientific Method', domain: 'philosophy', subdomain: 'Epistemology',
    era: 'earlyModern', yearOrigin: 1620, yearLabel: '1620 CE',
    originator: 'Francis Bacon / Galileo Galilei', originatorType: 'Person',
    originPlace: 'London / Florence', region: 'Western Europe',
    description: 'Novum Organum: systematic observation, hypothesis, experimentation, and replication. Replace authority and intuition with evidence. "Read the book of nature, not the book of Aristotle."',
    impact: 'The most powerful idea in human history after language. Science created medicine, technology, agriculture, and everything that separates modernity from antiquity. 400 years → more progress than 100,000.',
    parentIdeas: ['logic-formal', 'copernican-heliocentrism', 'scholasticism', 'islamic-philosophy'], childIdeas: ['empiricism', 'falsifiability', 'peer-review'],
    transformativeScore: 10,
  },
  {
    slug: 'empiricism', name: 'Empiricism', domain: 'philosophy', subdomain: 'Epistemology',
    era: 'earlyModern', yearOrigin: 1689, yearLabel: '1689 CE',
    originator: 'John Locke', originatorType: 'Person',
    originPlace: 'London, England', region: 'Western Europe',
    description: 'All knowledge comes from sensory experience. The mind begins as a "blank slate" (tabula rasa). There are no innate ideas — only experience and reflection.',
    impact: 'Demolished the divine right of kings and hereditary privilege. If all minds start equal, then authority must be earned, not inherited. Foundation of liberalism and modern psychology.',
    parentIdeas: ['scientific-method'], childIdeas: ['social-contract', 'positivism', 'behavioral-psychology'],
    transformativeScore: 9,
  },
  {
    slug: 'social-contract', name: 'Social Contract Theory', domain: 'politics', subdomain: 'Political Philosophy',
    era: 'earlyModern', yearOrigin: 1651, yearLabel: '1651 CE (Hobbes) / 1689 CE (Locke) / 1762 CE (Rousseau)',
    originator: 'Thomas Hobbes → John Locke → Jean-Jacques Rousseau', originatorType: 'Person',
    originPlace: 'England / France', region: 'Western Europe',
    description: 'Government derives its authority from the consent of the governed. People surrender some freedoms in exchange for protection and order. If the contract is broken, revolution is justified.',
    impact: 'Direct cause of the American Revolution (1776), French Revolution (1789), and the Universal Declaration of Human Rights (1948). The idea that power comes from below, not above.',
    parentIdeas: ['natural-law-theory', 'empiricism', 'republic-concept', 'democracy-concept'], childIdeas: ['human-rights', 'constitutionalism', 'separation-of-powers'],
    transformativeScore: 10,
  },
  {
    slug: 'calculus', name: 'Calculus', domain: 'mathematics', subdomain: 'Analysis',
    era: 'earlyModern', yearOrigin: 1687, yearLabel: '1665–1687 CE',
    originator: 'Isaac Newton / Gottfried Leibniz', originatorType: 'Person',
    originPlace: 'Cambridge, England / Hanover, Germany', region: 'Western Europe',
    description: 'The mathematics of change and accumulation. Differentiation (rates of change) and integration (accumulated quantities). Newton\'s "method of fluxions" and Leibniz\'s notation.',
    impact: 'Without calculus: no physics, no engineering, no economics, no machine learning. Every bridge, airplane, satellite, and neural network depends on calculus. The language of science itself.',
    parentIdeas: ['algebra-concept', 'geometry-concept', 'zero-concept'], childIdeas: ['newtonian-mechanics', 'differential-equations', 'optimization-theory'],
    transformativeScore: 10,
  },
  {
    slug: 'newtonian-mechanics', name: 'Newtonian Mechanics', domain: 'physics', subdomain: 'Classical Physics',
    era: 'earlyModern', yearOrigin: 1687, yearLabel: '1687 CE',
    originator: 'Isaac Newton', originatorType: 'Person',
    originPlace: 'Cambridge, England', region: 'Western Europe',
    description: 'Principia Mathematica: three laws of motion + universal gravitation. The same force that drops an apple holds the Moon. A single mathematical framework explaining ALL macroscopic motion.',
    impact: 'Made the universe predictable. Enabled the Industrial Revolution, space travel, GPS, and every mechanical invention. Showed that the cosmos obeys simple, discoverable laws.',
    parentIdeas: ['calculus', 'copernican-heliocentrism', 'scientific-method'], childIdeas: ['thermodynamics', 'electromagnetism', 'relativity-theory'],
    transformativeScore: 10,
  },
  {
    slug: 'human-rights', name: 'Universal Human Rights', domain: 'politics', subdomain: 'Ethics',
    era: 'earlyModern', yearOrigin: 1776, yearLabel: '1776 / 1789 / 1948 CE',
    originator: 'Jefferson / Déclaration / UN Assembly', originatorType: 'Institution',
    originPlace: 'Philadelphia / Paris / New York', region: 'Americas',
    description: '"All men are created equal...with certain unalienable Rights: Life, Liberty, and the pursuit of Happiness." Rights inhere in personhood, not citizenship.',
    impact: 'Abolished slavery, enfranchised women, decolonized the world, and created international humanitarian law. The idea that rights apply to ALL humans — the most contested and consequential moral claim.',
    parentIdeas: ['social-contract', 'natural-law-theory', 'codification-of-law'], childIdeas: ['abolition-of-slavery', 'womens-suffrage-idea', 'decolonization-idea'],
    transformativeScore: 10,
  },
  {
    slug: 'free-market', name: 'Free Market Economics', domain: 'economics', subdomain: 'Political Economy',
    era: 'earlyModern', yearOrigin: 1776, yearLabel: '1776 CE',
    originator: 'Adam Smith', originatorType: 'Person',
    originPlace: 'Edinburgh, Scotland', region: 'Western Europe',
    description: 'The Wealth of Nations: the "invisible hand" — individuals pursuing self-interest inadvertently benefit society. Division of labor, comparative advantage, and free trade.',
    impact: 'Created modern capitalism. Lifted billions from poverty through economic growth. Also created inequality, exploitation, and environmental destruction. The most debated economic idea ever.',
    parentIdeas: ['empiricism', 'social-contract'], childIdeas: ['capitalism-concept', 'marxism', 'keynesian-economics'],
    transformativeScore: 10,
  },
  {
    slug: 'separation-of-powers', name: 'Separation of Powers', domain: 'politics', subdomain: 'Constitutional Theory',
    era: 'earlyModern', yearOrigin: 1748, yearLabel: '1748 CE',
    originator: 'Montesquieu', originatorType: 'Person',
    originPlace: 'Paris, France', region: 'Western Europe',
    description: 'The Spirit of the Laws: executive, legislative, and judicial power must be held by separate bodies. No single person or group holds all authority.',
    impact: 'Built into the US Constitution (1787) and virtually every democratic constitution since. The structural idea that prevents tyranny through institutional design.',
    parentIdeas: ['republic-concept', 'social-contract'], childIdeas: ['constitutionalism', 'judicial-review'],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     MODERN IDEAS (1800–1945) — Industrial & Scientific Revolutions
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'evolution-natural-selection', name: 'Evolution by Natural Selection', domain: 'biology', subdomain: 'Evolutionary Biology',
    era: 'modern', yearOrigin: 1859, yearLabel: '1859 CE',
    originator: 'Charles Darwin / Alfred Russel Wallace', originatorType: 'Person',
    originPlace: 'London, England', region: 'Western Europe',
    description: 'On the Origin of Species: organisms vary, resources are limited, the fittest survive and reproduce. No designer needed — natural selection creates complexity from simplicity.',
    impact: 'Unified all of biology. Changed humanity\'s self-conception: we are animals, not angels. Inspired genetics, ecology, medicine, and (unfortunately) social Darwinism. The most explanatory idea in biology.',
    parentIdeas: ['scientific-method', 'empiricism'], childIdeas: ['genetics', 'ecology-concept', 'sociobiology'],
    transformativeScore: 10,
  },
  {
    slug: 'thermodynamics', name: 'Thermodynamics', domain: 'physics', subdomain: 'Energy Science',
    era: 'modern', yearOrigin: 1824, yearLabel: '1824 CE',
    originator: 'Sadi Carnot / Rudolf Clausius / Lord Kelvin', originatorType: 'Person',
    originPlace: 'Paris / Berlin / Glasgow', region: 'Western Europe',
    description: 'Four laws governing energy: (1) energy is conserved, (2) entropy always increases, (3) absolute zero is unreachable. Energy can be converted but never created or destroyed.',
    impact: 'Powered the Industrial Revolution — understanding heat engines. Entropy gives time its direction. The second law is the most universal physical principle: everything decays.',
    parentIdeas: ['newtonian-mechanics'], childIdeas: ['statistical-mechanics', 'information-theory', 'quantum-mechanics'],
    transformativeScore: 9,
  },
  {
    slug: 'electromagnetism', name: 'Electromagnetism', domain: 'physics', subdomain: 'Field Theory',
    era: 'modern', yearOrigin: 1865, yearLabel: '1865 CE',
    originator: 'James Clerk Maxwell', originatorType: 'Person',
    originPlace: 'London / Edinburgh', region: 'Western Europe',
    description: 'Maxwell\'s equations: four equations unifying electricity, magnetism, and light. Electromagnetic waves propagate at the speed of light — because light IS electromagnetic radiation.',
    impact: 'Enabled radio, television, radar, WiFi, smartphones, and all wireless communication. Maxwell\'s equations are the foundation of the electronic age.',
    parentIdeas: ['newtonian-mechanics', 'calculus'], childIdeas: ['relativity-theory', 'quantum-mechanics', 'radio-communication'],
    transformativeScore: 10,
  },
  {
    slug: 'germ-theory', name: 'Germ Theory of Disease', domain: 'medicine', subdomain: 'Epidemiology',
    era: 'modern', yearOrigin: 1862, yearLabel: '1862 CE',
    originator: 'Louis Pasteur / Robert Koch', originatorType: 'Person',
    originPlace: 'Paris / Berlin', region: 'Western Europe',
    description: 'Diseases are caused by microorganisms (bacteria, viruses, fungi), not miasma, humoral imbalance, or divine punishment. Specific germs cause specific diseases (Koch\'s postulates).',
    impact: 'Doubled human life expectancy in 150 years. Created vaccines, antibiotics, sanitation, surgery, and public health. The idea that saved more lives than any other in history.',
    parentIdeas: ['scientific-method', 'empiricism'], childIdeas: ['vaccination-concept', 'antibiotics-concept', 'epidemiology'],
    transformativeScore: 10,
  },
  {
    slug: 'marxism', name: 'Marxism (Historical Materialism)', domain: 'economics', subdomain: 'Political Economy',
    era: 'modern', yearOrigin: 1848, yearLabel: '1848 CE',
    originator: 'Karl Marx / Friedrich Engels', originatorType: 'Person',
    originPlace: 'London / Brussels', region: 'Western Europe',
    description: 'Das Kapital: history is driven by class struggle between those who own the means of production and those who sell their labor. Capitalism will collapse under its own contradictions.',
    impact: 'Inspired the Russian Revolution, Chinese Revolution, Cold War, and billions of lives. Whether as ideology or critique, Marxism is the most influential economic idea after free-market capitalism.',
    parentIdeas: ['free-market'], childIdeas: ['communism', 'welfare-state', 'critical-theory'],
    transformativeScore: 9,
  },
  {
    slug: 'relativity-theory', name: 'Theory of Relativity', domain: 'physics', subdomain: 'Theoretical Physics',
    era: 'modern', yearOrigin: 1905, yearLabel: '1905 CE (Special) / 1915 CE (General)',
    originator: 'Albert Einstein', originatorType: 'Person',
    originPlace: 'Bern / Berlin', region: 'Western Europe',
    description: 'Special: c is constant, E=mc². General: gravity is the curvature of spacetime caused by mass-energy. Space and time are not fixed — they stretch, warp, and flow.',
    impact: 'GPS correction (general relativity), nuclear energy/weapons (E=mc²), black holes, gravitational waves, and the expanding universe. Overturned 200 years of Newtonian certainty.',
    parentIdeas: ['newtonian-mechanics', 'electromagnetism'], childIdeas: ['quantum-mechanics', 'big-bang-theory', 'nuclear-energy'],
    transformativeScore: 10,
  },
  {
    slug: 'quantum-mechanics', name: 'Quantum Mechanics', domain: 'physics', subdomain: 'Theoretical Physics',
    era: 'modern', yearOrigin: 1925, yearLabel: '1925–1927 CE',
    originator: 'Heisenberg, Schrödinger, Dirac, Born', originatorType: 'Collective',
    originPlace: 'Göttingen / Munich / Cambridge', region: 'Western Europe',
    description: 'Particles are also waves. Measurement changes the system. Outcomes are probabilistic, not deterministic. Superposition, entanglement, and the uncertainty principle.',
    impact: 'Underlies ALL modern technology: semiconductors, lasers, MRI, LEDs, nuclear power, quantum computing. The most successful predictive theory in physics history (accurate to 12 decimal places).',
    parentIdeas: ['relativity-theory', 'electromagnetism', 'atomic-theory-ancient', 'thermodynamics'], childIdeas: ['semiconductor-theory', 'quantum-computing', 'standard-model'],
    transformativeScore: 10,
  },
  {
    slug: 'genetics', name: 'Genetics (Mendelian Inheritance)', domain: 'biology', subdomain: 'Molecular Biology',
    era: 'modern', yearOrigin: 1866, yearLabel: '1866 CE (Mendel) / 1953 CE (Watson & Crick)',
    originator: 'Gregor Mendel → Watson, Crick, Franklin', originatorType: 'Person',
    originPlace: 'Brno, Austria-Hungary → Cambridge, England', region: 'Eastern Europe',
    description: 'Traits are inherited through discrete units (genes). Mendel\'s laws of segregation and independent assortment. Watson & Crick revealed DNA\'s double helix structure (1953).',
    impact: 'Created modern medicine (gene therapy, CRISPR), forensics, agriculture (GMOs), and evolutionary biology. Understanding the code of life transformed every biological science.',
    parentIdeas: ['evolution-natural-selection', 'scientific-method'], childIdeas: ['dna-double-helix', 'crispr-gene-editing', 'genomics'],
    transformativeScore: 10,
  },
  {
    slug: 'vaccination-concept', name: 'Vaccination', domain: 'medicine', subdomain: 'Immunology',
    era: 'modern', yearOrigin: 1796, yearLabel: '1796 CE',
    originator: 'Edward Jenner', originatorType: 'Person',
    originPlace: 'Berkeley, Gloucestershire, England', region: 'Western Europe',
    description: 'Deliberately infecting with cowpox prevents smallpox. The idea that the body can be trained to fight disease before encountering it. From variolation to mRNA vaccines.',
    impact: 'Eradicated smallpox (killed 500 million in the 20th century alone). Saved billions of lives via polio, measles, tetanus, and COVID vaccines. The single most life-saving medical intervention.',
    parentIdeas: ['germ-theory'], childIdeas: ['mrna-vaccines', 'public-health-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'abolition-of-slavery', name: 'Abolition of Slavery', domain: 'politics', subdomain: 'Moral Progress',
    era: 'modern', yearOrigin: 1807, yearLabel: '1807 (UK trade) / 1863 (US Emancipation)',
    originator: 'William Wilberforce / Frederick Douglass / Harriet Tubman', originatorType: 'Person',
    originPlace: 'London / Washington DC', region: 'Western Europe',
    description: 'The idea that no human being can be another\'s property. That chattel slavery is morally incompatible with human rights, natural law, and Christian ethics.',
    impact: 'Ended legal slavery across the Western world. The abolitionist movement was the first global human rights campaign. Its unfinished legacy drives civil rights movements today.',
    parentIdeas: ['human-rights', 'social-contract'], childIdeas: ['civil-rights-movement', 'decolonization-idea'],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     CONTEMPORARY IDEAS (1945–Present) — Digital, Global, Existential
     ═══════════════════════════════════════════════════════════ */
  {
    slug: 'information-theory', name: 'Information Theory', domain: 'information', subdomain: 'Mathematics',
    era: 'contemporary', yearOrigin: 1948, yearLabel: '1948 CE',
    originator: 'Claude Shannon', originatorType: 'Person',
    originPlace: 'Bell Labs, Murray Hill, New Jersey', region: 'Americas',
    description: 'A Mathematical Theory of Communication: information is measurable in bits. Entropy quantifies uncertainty. Channel capacity limits data transmission. Compression is possible.',
    impact: 'Foundation of the entire digital age. The Internet, compression, encryption, error correction, coding theory, and AI all rest on Shannon\'s 1948 paper. The Magna Carta of the Information Age.',
    parentIdeas: ['boolean-logic', 'thermodynamics', 'calculus'], childIdeas: ['internet-concept', 'digital-computing', 'machine-learning'],
    transformativeScore: 10,
  },
  {
    slug: 'digital-computing', name: 'Digital Computing (Turing Machine)', domain: 'information', subdomain: 'Computer Science',
    era: 'contemporary', yearOrigin: 1936, yearLabel: '1936 CE (theory) / 1945 CE (implementation)',
    originator: 'Alan Turing / John von Neumann', originatorType: 'Person',
    originPlace: 'Cambridge, England / Princeton, New Jersey', region: 'Western Europe',
    description: 'A universal machine that can simulate any computation. Turing proved that a simple tape-reading device can compute anything that is computable. Von Neumann designed the stored-program architecture.',
    impact: 'Created the computer industry. Every device — smartphones, servers, satellites, cars — is a Turing machine. Computing is the most transformative technology since the printing press.',
    parentIdeas: ['information-theory', 'logic-formal', 'algebra-concept'], childIdeas: ['internet-concept', 'artificial-intelligence', 'machine-learning'],
    transformativeScore: 10,
  },
  {
    slug: 'internet-concept', name: 'The Internet', domain: 'technology', subdomain: 'Communication Networks',
    era: 'contemporary', yearOrigin: 1969, yearLabel: '1969 CE (ARPANET) / 1991 CE (World Wide Web)',
    originator: 'Vint Cerf, Bob Kahn (TCP/IP) / Tim Berners-Lee (WWW)', originatorType: 'Person',
    originPlace: 'UCLA / CERN, Geneva', region: 'Americas',
    description: 'Packet-switched network connecting every computer on Earth. Berners-Lee\'s World Wide Web added hypertext, URLs, and browsers. From 4 nodes (1969) to 5 billion users (2024).',
    impact: 'Reshaped civilization: commerce, communication, politics, education, entertainment, warfare, and social structures. The most rapid and comprehensive technological transformation in human history.',
    parentIdeas: ['digital-computing', 'information-theory'], childIdeas: ['social-media', 'artificial-intelligence', 'cryptocurrency'],
    transformativeScore: 10,
  },
  {
    slug: 'artificial-intelligence', name: 'Artificial Intelligence', domain: 'information', subdomain: 'Computer Science',
    era: 'contemporary', yearOrigin: 1956, yearLabel: '1956 CE (Dartmouth) / 2012 CE (Deep Learning) / 2022 CE (LLMs)',
    originator: 'John McCarthy, Marvin Minsky → Geoffrey Hinton → OpenAI', originatorType: 'Person',
    originPlace: 'Dartmouth College / Toronto / San Francisco', region: 'Americas',
    description: 'Machines that can learn, reason, and solve problems. From symbolic AI (1956) to neural networks (1986) to deep learning (2012) to large language models (2022).',
    impact: 'Potentially the last invention humanity needs to make. AI is transforming medicine, science, warfare, art, and commerce. The most existentially significant technology since nuclear weapons.',
    parentIdeas: ['digital-computing', 'information-theory', 'logic-formal'], childIdeas: [],
    transformativeScore: 10,
  },
  {
    slug: 'dna-double-helix', name: 'DNA Double Helix Structure', domain: 'biology', subdomain: 'Molecular Biology',
    era: 'contemporary', yearOrigin: 1953, yearLabel: '1953 CE',
    originator: 'James Watson, Francis Crick, Rosalind Franklin', originatorType: 'Person',
    originPlace: 'Cambridge, England', region: 'Western Europe',
    description: 'The structure of DNA: a double helix of complementary base pairs (A-T, G-C). "We have found the secret of life." The mechanism of heredity is molecular, not mystical.',
    impact: 'Enabled genetic engineering, forensics, CRISPR, gene therapy, and the Human Genome Project. Understanding the molecule that encodes all life on Earth.',
    parentIdeas: ['genetics', 'quantum-mechanics'], childIdeas: ['crispr-gene-editing', 'genomics'],
    transformativeScore: 10,
  },
  {
    slug: 'crispr-gene-editing', name: 'CRISPR Gene Editing', domain: 'biology', subdomain: 'Genetic Engineering',
    era: 'contemporary', yearOrigin: 2012, yearLabel: '2012 CE',
    originator: 'Jennifer Doudna / Emmanuelle Charpentier', originatorType: 'Person',
    originPlace: 'Berkeley, California / Umeå, Sweden', region: 'Americas',
    description: 'Clustered Regularly Interspaced Short Palindromic Repeats — a bacterial immune system repurposed as a molecular scissors that can edit any DNA sequence with unprecedented precision.',
    impact: 'Curing genetic diseases (sickle cell, 2023), engineering crops, and potentially editing human embryos. The most powerful biological technology ever invented. Nobel Prize 2020.',
    parentIdeas: ['dna-double-helix', 'genetics'], childIdeas: [],
    transformativeScore: 9,
  },
  {
    slug: 'climate-science', name: 'Climate Change Science', domain: 'environment', subdomain: 'Earth Science',
    era: 'contemporary', yearOrigin: 1896, yearLabel: '1896 CE (Arrhenius) / 1988 CE (IPCC)',
    originator: 'Svante Arrhenius → IPCC', originatorType: 'Institution',
    originPlace: 'Stockholm → Geneva', region: 'Western Europe',
    description: 'CO₂ from fossil fuels traps heat in the atmosphere (greenhouse effect), warming the planet. Arrhenius calculated it in 1896; IPCC confirmed it with global consensus by 1990.',
    impact: 'The defining challenge of the 21st century. Driving energy transition, international treaties (Paris Agreement), and potentially civilizational risk. The idea that changed how we think about the future.',
    parentIdeas: ['scientific-method', 'thermodynamics'], childIdeas: [],
    transformativeScore: 9,
  },
  {
    slug: 'machine-learning', name: 'Machine Learning & Neural Networks', domain: 'information', subdomain: 'AI',
    era: 'contemporary', yearOrigin: 1986, yearLabel: '1986 CE (Backpropagation) / 2012 CE (AlexNet)',
    originator: 'Geoffrey Hinton / Yann LeCun / Yoshua Bengio', originatorType: 'Person',
    originPlace: 'Toronto / Montreal / New York', region: 'Americas',
    description: 'Algorithms that learn patterns from data without explicit programming. Neural networks with backpropagation, convolutional networks for vision, transformers for language.',
    impact: 'Powers self-driving cars, language translation, drug discovery, protein folding (AlphaFold), and generative AI. The technology that made AI practical after 50 years of "AI winter."',
    parentIdeas: ['digital-computing', 'information-theory', 'calculus'], childIdeas: ['artificial-intelligence'],
    transformativeScore: 9,
  },
  {
    slug: 'big-bang-theory', name: 'Big Bang Theory', domain: 'physics', subdomain: 'Cosmology',
    era: 'contemporary', yearOrigin: 1927, yearLabel: '1927 CE (Lemaître) / 1965 CE (CMB confirmation)',
    originator: 'Georges Lemaître / Arno Penzias & Robert Wilson', originatorType: 'Person',
    originPlace: 'Leuven, Belgium / Holmdel, New Jersey', region: 'Western Europe',
    description: 'The universe began as an infinitely dense singularity ~13.8 billion years ago and has been expanding ever since. Confirmed by cosmic microwave background radiation (1965).',
    impact: 'Gave humanity its origin story in scientific terms. The universe has a beginning, a history, and a future. Changed philosophy, theology, and cosmology forever.',
    parentIdeas: ['relativity-theory'], childIdeas: ['dark-matter', 'dark-energy'],
    transformativeScore: 9,
  },
  {
    slug: 'decolonization-idea', name: 'Decolonization & Self-Determination', domain: 'politics', subdomain: 'International Relations',
    era: 'contemporary', yearOrigin: 1947, yearLabel: '1947 CE (India) / 1960 CE (Africa)',
    originator: 'Gandhi, Nehru, Nkrumah, Fanon, Mandela', originatorType: 'Movement',
    originPlace: 'India / Ghana / Algeria / South Africa', region: 'South Asia',
    description: 'The idea that colonized peoples have the right to self-governance. Colonialism is not "civilization" — it is exploitation. Every nation has the right to determine its own destiny.',
    impact: 'Created 100+ new nations (1945–1970). Ended European colonial empires. Reshaped the world map, the UN, and international law. An unfinished project still reverberating today.',
    parentIdeas: ['human-rights', 'abolition-of-slavery'], childIdeas: [],
    transformativeScore: 9,
  },
  {
    slug: 'feminism-concept', name: 'Feminism & Gender Equality', domain: 'social', subdomain: 'Social Theory',
    era: 'contemporary', yearOrigin: 1949, yearLabel: '1792 CE (Wollstonecraft) / 1949 CE (Beauvoir) / 1963 CE (Friedan)',
    originator: 'Mary Wollstonecraft → Simone de Beauvoir → Betty Friedan', originatorType: 'Person',
    originPlace: 'London / Paris / New York', region: 'Western Europe',
    description: 'The idea that women are fully human, with equal rights, capacities, and claims to participation in public life. From suffrage to workplace equality to bodily autonomy.',
    impact: 'Doubled the talent pool. Women\'s education correlates with economic growth, lower birth rates, better child health, and democratic stability. The unfinished revolution that changed everything.',
    parentIdeas: ['human-rights', 'social-contract'], childIdeas: [],
    transformativeScore: 9,
  },

  /* ═══════════════════════════════════════════════════════════
     SCIENTIFIC PARADIGMS FROM BATCH 1 & 3 (idea.txt)
     These are the user's new ideas, placed in historical context
     ═══════════════════════════════════════════════════════════ */
  // Scientific Method & Philosophy of Science
  {
    slug: 'falsifiability', name: 'Falsifiability', domain: 'philosophy', subdomain: 'Philosophy of Science',
    era: 'contemporary', yearOrigin: 1934, yearLabel: '1934 CE',
    originator: 'Karl Popper', originatorType: 'Person',
    originPlace: 'Vienna, Austria', region: 'Western Europe',
    description: 'A theory is scientific only if it can be falsified — disproved by observation. Pseudoscience makes unfalsifiable claims. The demarcation criterion for real science.',
    impact: 'Changed how we evaluate scientific claims. If it can\'t be tested, it isn\'t science. Influences FDA trials, peer review, and every experimental design.',
    parentIdeas: ['scientific-method', 'empiricism'], childIdeas: ['kuhn-paradigm-shifts'],
    transformativeScore: 8,
  },
  {
    slug: 'kuhn-paradigm-shifts', name: 'Kuhn\'s Paradigm Shifts', domain: 'philosophy', subdomain: 'Philosophy of Science',
    era: 'contemporary', yearOrigin: 1962, yearLabel: '1962 CE',
    originator: 'Thomas Kuhn', originatorType: 'Person',
    originPlace: 'Harvard / Berkeley', region: 'Americas',
    description: 'Science doesn\'t progress linearly. Normal science operates within a paradigm until anomalies accumulate, triggering a "paradigm shift" — a scientific revolution (e.g., Newton → Einstein).',
    impact: 'Revolutionized how we think about scientific progress. "Paradigm shift" entered everyday language. Showed that science is a social process, not just logical deduction.',
    parentIdeas: ['falsifiability', 'scientific-method'], childIdeas: [],
    transformativeScore: 7,
  },
  {
    slug: 'systems-theory', name: 'Systems Theory', domain: 'philosophy', subdomain: 'Complexity',
    era: 'contemporary', yearOrigin: 1968, yearLabel: '1968 CE',
    originator: 'Ludwig von Bertalanffy', originatorType: 'Person',
    originPlace: 'Vienna → Edmonton, Canada', region: 'Americas',
    description: 'A system is more than the sum of its parts. Feedback loops, emergence, and self-organization apply across biology, ecology, economics, and social systems.',
    impact: 'Foundation of cybernetics, ecology, organizational theory, and complex systems science. Changed how we understand interconnected wholes vs. isolated parts.',
    parentIdeas: ['thermodynamics', 'evolution-natural-selection'], childIdeas: ['chaos-theory', 'complexity-theory'],
    transformativeScore: 8,
  },
  {
    slug: 'chaos-theory', name: 'Chaos Theory', domain: 'mathematics', subdomain: 'Dynamical Systems',
    era: 'contemporary', yearOrigin: 1963, yearLabel: '1963 CE',
    originator: 'Edward Lorenz', originatorType: 'Person',
    originPlace: 'MIT, Cambridge, Massachusetts', region: 'Americas',
    description: 'Deterministic systems can produce unpredictable behavior. The "butterfly effect" — tiny differences in initial conditions lead to vastly different outcomes. Order within disorder.',
    impact: 'Transformed meteorology, ecology, economics, and mathematics. Showed that predictability has fundamental limits even without randomness.',
    parentIdeas: ['systems-theory', 'calculus'], childIdeas: ['complexity-theory'],
    transformativeScore: 7,
  },
  {
    slug: 'complexity-theory', name: 'Complexity Theory', domain: 'philosophy', subdomain: 'Complex Systems',
    era: 'contemporary', yearOrigin: 1984, yearLabel: '1984 CE',
    originator: 'Santa Fe Institute (Gell-Mann, Holland, Kauffman)', originatorType: 'Institution',
    originPlace: 'Santa Fe, New Mexico', region: 'Americas',
    description: 'How simple rules produce complex behavior: ant colonies, markets, brains, cities. Emergence, adaptation, and self-organization at the edge of chaos.',
    impact: 'The science of the 21st century. Understanding epidemics, financial markets, ecosystems, and AI all require complexity thinking. Reductionism alone is insufficient.',
    parentIdeas: ['systems-theory', 'chaos-theory', 'evolution-natural-selection'], childIdeas: [],
    transformativeScore: 8,
  },
  // Standards Model & Quantum
  {
    slug: 'standard-model', name: 'The Standard Model of Particle Physics', domain: 'physics', subdomain: 'Particle Physics',
    era: 'contemporary', yearOrigin: 1973, yearLabel: '1973 CE / 2012 CE (Higgs confirmed)',
    originator: 'Glashow, Weinberg, Salam / CERN', originatorType: 'Institution',
    originPlace: 'Harvard / CERN, Geneva', region: 'Americas',
    description: '17 fundamental particles (6 quarks, 6 leptons, 4 gauge bosons, 1 Higgs) explaining 3 of 4 fundamental forces (electromagnetic, weak, strong — gravity excluded).',
    impact: 'The most successful theory in physics. Every particle physics experiment confirms it. The Higgs boson\'s 2012 discovery was the culmination of 50 years of theoretical prediction.',
    parentIdeas: ['quantum-mechanics', 'relativity-theory', 'electromagnetism'], childIdeas: [],
    transformativeScore: 8,
  },
  {
    slug: 'semiconductor-theory', name: 'Semiconductor Theory', domain: 'physics', subdomain: 'Solid State Physics',
    era: 'contemporary', yearOrigin: 1947, yearLabel: '1947 CE',
    originator: 'John Bardeen, Walter Brattain, William Shockley', originatorType: 'Person',
    originPlace: 'Bell Labs, Murray Hill, New Jersey', region: 'Americas',
    description: 'Transistor: solid-state device that amplifies and switches electronic signals using semiconductor materials (silicon). Replaced vacuum tubes. One trillion transistors on a single chip (2024).',
    impact: 'The transistor IS the modern world. Computers, phones, internet, AI — all built on semiconductors. The most manufactured object in human history.',
    parentIdeas: ['quantum-mechanics'], childIdeas: ['digital-computing', 'internet-concept'],
    transformativeScore: 10,
  },
  {
    slug: 'quantum-computing', name: 'Quantum Computing', domain: 'information', subdomain: 'Computing',
    era: 'contemporary', yearOrigin: 1981, yearLabel: '1981 CE (Feynman) / 2019 CE (quantum supremacy)',
    originator: 'Richard Feynman / Peter Shor / Google', originatorType: 'Person',
    originPlace: 'Caltech / MIT / Mountain View', region: 'Americas',
    description: 'Using quantum superposition and entanglement to process information. Qubits can be 0 and 1 simultaneously. Exponential speedup for specific problems (factoring, simulation, optimization).',
    impact: 'Could break current encryption, simulate molecules for drug design, and solve optimization problems beyond classical computers. Still early but potentially civilization-altering.',
    parentIdeas: ['quantum-mechanics', 'digital-computing', 'information-theory'], childIdeas: [],
    transformativeScore: 8,
  },
  // Biology from Batch 3
  {
    slug: 'epigenetics', name: 'Epigenetic Inheritance', domain: 'biology', subdomain: 'Genetics',
    era: 'contemporary', yearOrigin: 1942, yearLabel: '1942 CE (Waddington) / 2000s CE (confirmed)',
    originator: 'Conrad Waddington / Adrian Bird', originatorType: 'Person',
    originPlace: 'Edinburgh, Scotland', region: 'Western Europe',
    description: 'Gene expression can be modified by environmental factors without changing the DNA sequence. Methyl groups, histone modifications, and RNA interference regulate which genes are active.',
    impact: 'Showed that nurture affects nature at the molecular level. Trauma, diet, and environment alter gene expression across generations. Blurred the nature/nurture divide.',
    parentIdeas: ['genetics', 'dna-double-helix'], childIdeas: [],
    transformativeScore: 8,
  },
  {
    slug: 'mrna-vaccines', name: 'mRNA Vaccine Technology', domain: 'medicine', subdomain: 'Immunology',
    era: 'contemporary', yearOrigin: 2020, yearLabel: '2005 CE (Karikó) / 2020 CE (COVID vaccines)',
    originator: 'Katalin Karikó / Drew Weissman / BioNTech / Moderna', originatorType: 'Person',
    originPlace: 'Philadelphia / Mainz, Germany', region: 'Americas',
    description: 'Using synthetic mRNA to instruct cells to produce a target protein (e.g., spike protein), triggering immune response. No live virus needed. Designed in days, manufactured at scale.',
    impact: 'Saved millions of lives during COVID-19. Platform technology: potentially applicable to cancer, HIV, malaria, and autoimmune diseases. Fastest vaccine development in history (11 months).',
    parentIdeas: ['vaccination-concept', 'dna-double-helix', 'genetics'], childIdeas: [],
    transformativeScore: 9,
  },
  {
    slug: 'microbiome-science', name: 'Human Microbiome Science', domain: 'medicine', subdomain: 'Microbiology',
    era: 'contemporary', yearOrigin: 2007, yearLabel: '2007 CE (Human Microbiome Project)',
    originator: 'Human Microbiome Project / NIH', originatorType: 'Institution',
    originPlace: 'Bethesda, Maryland', region: 'Americas',
    description: 'The 38 trillion microorganisms in and on the human body are not passengers — they are essential partners. The gut microbiome influences digestion, immunity, mental health, and disease.',
    impact: 'Redefined what it means to be human (more bacterial cells than human cells). Opened new treatments for obesity, depression, autoimmunity, and cancer through microbiome modulation.',
    parentIdeas: ['germ-theory', 'genetics'], childIdeas: [],
    transformativeScore: 7,
  },
  // Technology & Information
  {
    slug: 'boolean-logic', name: 'Boolean Logic', domain: 'mathematics', subdomain: 'Logic',
    era: 'modern', yearOrigin: 1854, yearLabel: '1854 CE',
    originator: 'George Boole', originatorType: 'Person',
    originPlace: 'Cork, Ireland', region: 'Western Europe',
    description: 'An Investigation of the Laws of Thought: algebra of logic using TRUE/FALSE (1/0), AND, OR, NOT operations. Formalized Aristotle\'s logic into mathematical notation.',
    impact: 'The mathematical foundation of all digital computing. Every circuit, every program, every search query uses Boolean logic. Aristotle\'s logic made computational.',
    parentIdeas: ['logic-formal', 'algebra-concept'], childIdeas: ['digital-computing', 'information-theory'],
    transformativeScore: 9,
  },
  {
    slug: 'algorithm-concept', name: 'Algorithm Design', domain: 'mathematics', subdomain: 'Computer Science',
    era: 'medieval', yearOrigin: 825, yearLabel: '~825 CE',
    originator: 'Al-Khwarizmi', originatorType: 'Person',
    originPlace: 'Baghdad, House of Wisdom', region: 'West Asia',
    description: 'A finite sequence of well-defined instructions to solve a class of problems. The word "algorithm" is a Latinization of Al-Khwarizmi\'s name. Systematic problem-solving codified.',
    impact: 'Algorithms run the world: Google Search, GPS routing, financial trading, social media feeds, medical diagnostics, and AI training. From medieval Baghdad to Silicon Valley.',
    parentIdeas: ['algebra-concept'], childIdeas: ['digital-computing', 'machine-learning'],
    transformativeScore: 9,
  },
  // Environment
  {
    slug: 'ecology-concept', name: 'Ecology', domain: 'environment', subdomain: 'Ecology',
    era: 'modern', yearOrigin: 1866, yearLabel: '1866 CE',
    originator: 'Ernst Haeckel', originatorType: 'Person',
    originPlace: 'Jena, Germany', region: 'Western Europe',
    description: 'The scientific study of interactions between organisms and their environment. Food webs, ecosystems, nutrient cycles, and the interdependence of all living things.',
    impact: 'Foundation of conservation, environmentalism, and sustainability science. Without ecology: no understanding of biodiversity loss, deforestation, or climate change impacts.',
    parentIdeas: ['evolution-natural-selection'], childIdeas: ['climate-science'],
    transformativeScore: 8,
  },
  // Economics
  {
    slug: 'keynesian-economics', name: 'Keynesian Economics', domain: 'economics', subdomain: 'Macroeconomics',
    era: 'contemporary', yearOrigin: 1936, yearLabel: '1936 CE',
    originator: 'John Maynard Keynes', originatorType: 'Person',
    originPlace: 'Cambridge, England', region: 'Western Europe',
    description: 'The General Theory: markets don\'t self-correct. During recessions, government should spend more (deficit spending) to stimulate demand. Aggregate demand drives the economy.',
    impact: 'Shaped post-WWII economic policy worldwide. The New Deal, Marshall Plan, and 2008 financial crisis response all applied Keynesian principles. Saved capitalism from itself.',
    parentIdeas: ['free-market', 'marxism'], childIdeas: [],
    transformativeScore: 8,
  },
]

/* ── Aggregation helpers ── */
export const TOTAL_IDEAS = IDEAS.length
export const IDEAS_BY_ERA = IDEAS.reduce<Record<string, number>>((acc, i) => {
  acc[i.era] = (acc[i.era] || 0) + 1; return acc
}, {})
export const IDEAS_BY_DOMAIN = IDEAS.reduce<Record<string, number>>((acc, i) => {
  acc[i.domain] = (acc[i.domain] || 0) + 1; return acc
}, {})
