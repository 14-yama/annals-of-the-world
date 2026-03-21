/* ─── Quiz Question Bank — Annals of the World ─── */
import type { QuizQuestion, QuizSession } from '../types'

const ALL_QUESTIONS: QuizQuestion[] = [
  // ─── BEGINNER ───
  {
    id: 'b1', question: 'What is considered the "cradle of humankind"?',
    options: ['Asia', 'Europe', 'Africa', 'Americas'],
    correctIndex: 2, explanation: 'The earliest Homo sapiens fossils were found in East Africa, making it the cradle of humankind.',
    era: 'prehistory', difficulty: 'beginner', category: 'places',
  },
  {
    id: 'b2', question: 'Which ancient civilization built the Great Pyramids of Giza?',
    options: ['Mesopotamia', 'Ancient Egypt', 'Ancient Greece', 'Indus Valley'],
    correctIndex: 1, explanation: 'The Great Pyramids were built during Egypt\'s Old Kingdom, around 2560 BCE.',
    era: 'ancient', difficulty: 'beginner', category: 'places',
  },
  {
    id: 'b3', question: 'What writing system did the Mesopotamians develop?',
    options: ['Hieroglyphics', 'Cuneiform', 'Sanskrit', 'Chinese characters'],
    correctIndex: 1, explanation: 'Cuneiform, a wedge-shaped script pressed into clay tablets, was developed around 3400 BCE.',
    era: 'ancient', difficulty: 'beginner', category: 'ideas',
  },
  {
    id: 'b4', question: 'Which empire was the largest contiguous land empire in history?',
    options: ['Roman Empire', 'British Empire', 'Mongol Empire', 'Ottoman Empire'],
    correctIndex: 2, explanation: 'The Mongol Empire under Genghis Khan and his successors spanned 24 million km².',
    era: 'medieval', difficulty: 'beginner', category: 'events',
  },
  {
    id: 'b5', question: 'Where did the Industrial Revolution begin?',
    options: ['France', 'Germany', 'United States', 'Great Britain'],
    correctIndex: 3, explanation: 'The Industrial Revolution began in Great Britain in the late 18th century.',
    era: 'modern', difficulty: 'beginner', category: 'events',
  },
  {
    id: 'b6', question: 'What invention by Gutenberg revolutionized communication in the 15th century?',
    options: ['Telescope', 'Printing press', 'Compass', 'Gunpowder'],
    correctIndex: 1, explanation: 'Johannes Gutenberg\'s movable-type printing press (c. 1440) enabled mass production of books.',
    era: 'early-modern', difficulty: 'beginner', category: 'artifacts',
  },
  {
    id: 'b7', question: 'Which continent has the youngest median age (19.7 years)?',
    options: ['Asia', 'South America', 'Africa', 'Oceania'],
    correctIndex: 2, explanation: 'Africa has the youngest population with a median age of 19.7 years.',
    difficulty: 'beginner', category: 'places',
  },
  {
    id: 'b8', question: 'Which structure was built by Mughal Emperor Shah Jahan?',
    options: ['Great Wall of China', 'Taj Mahal', 'Colosseum', 'Parthenon'],
    correctIndex: 1, explanation: 'The Taj Mahal was built by Shah Jahan (1632-1653) as a mausoleum for his wife Mumtaz Mahal.',
    era: 'early-modern', difficulty: 'beginner', category: 'artifacts',
  },

  // ─── INTERMEDIATE ───
  {
    id: 'i1', question: 'The "Axial Age" (800-200 BCE) saw the rise of which parallel developments?',
    options: ['Bronze weapons across Europe', 'Independent philosophical traditions worldwide', 'Maritime trade in the Pacific', 'Iron smelting in Africa'],
    correctIndex: 1, explanation: 'The Axial Age saw Confucius, Buddha, Socrates, and Hebrew prophets emerge independently across civilizations.',
    era: 'ancient', difficulty: 'intermediate', category: 'ideas',
  },
  {
    id: 'i2', question: 'What was the significance of the Code of Hammurabi?',
    options: ['First astronomical observations', 'One of the earliest written legal codes', 'First use of iron weapons', 'Development of democracy'],
    correctIndex: 1, explanation: 'Created c. 1754 BCE by Babylonian King Hammurabi, it codified 282 laws governing daily life.',
    era: 'ancient', difficulty: 'intermediate', category: 'artifacts',
  },
  {
    id: 'i3', question: 'Which institution preserved classical knowledge during Europe\'s "Dark Ages"?',
    options: ['Roman Senate', 'Byzantine & Islamic scholars', 'Viking traders', 'Egyptian temples'],
    correctIndex: 1, explanation: 'Byzantine and Islamic scholars translated and preserved Greek/Roman texts that would later fuel the Renaissance.',
    era: 'medieval', difficulty: 'intermediate', category: 'movements',
  },
  {
    id: 'i4', question: 'What percentage of world GDP did the Mughal Empire contribute at its peak?',
    options: ['5%', '12%', '25%', '40%'],
    correctIndex: 2, explanation: 'At its height under Aurangzeb, the Mughal Empire produced roughly 25% of global GDP.',
    era: 'early-modern', difficulty: 'intermediate', category: 'events',
  },
  {
    id: 'i5', question: 'What was the "3% GDP paradox" regarding Africa?',
    options: ['Africa has 3% literacy rate', 'Africa has 17% of world population but only ~3% of GDP', 'Africa contributes 3% of global trade', '3% of African countries are democracies'],
    correctIndex: 1, explanation: 'Despite having 17% of the global population and 30% of mineral reserves, Africa produces only ~3% of world GDP.',
    difficulty: 'intermediate', category: 'ideas',
  },
  {
    id: 'i6', question: 'The Silk Road connected which two major regions?',
    options: ['Africa and Europe', 'China and the Mediterranean', 'India and Egypt', 'Japan and Arabia'],
    correctIndex: 1, explanation: 'The Silk Road was a network of trade routes connecting China to the Mediterranean, facilitating exchange of goods, culture, and ideas.',
    era: 'ancient', difficulty: 'intermediate', category: 'places',
  },

  // ─── ADVANCED ───
  {
    id: 'a1', question: 'In the Annals knowledge graph schema, what is the mandatory metadata for all interpretive edges?',
    options: ['TAGGED_AS with category', 'FRAMED_BY with citation_style, evidence_url, page_refs, source_note', 'LINKED_TO with confidence_score', 'DESCRIBED_BY with source_text'],
    correctIndex: 1, explanation: 'The schema requires FRAMED_BY edges with full citation metadata for scholarly auditability.',
    difficulty: 'advanced', category: 'ideas',
  },
  {
    id: 'a2', question: 'What is the "228:1 wealth gap" in Asian data?',
    options: ['Japan vs Cambodia GDP', 'Qatar vs Afghanistan GDP per capita', 'Singapore vs Myanmar GDP per capita', 'South Korea vs North Korea GDP'],
    correctIndex: 1, explanation: 'Qatar\'s GDP per capita is roughly 228 times that of Afghanistan, representing the extreme wealth disparity in Asia.',
    difficulty: 'advanced', category: 'events',
  },
  {
    id: 'a3', question: 'Which ancient civilization had an undeciphered writing system?',
    options: ['Mesopotamia', 'Egypt', 'Indus Valley (Harappan)', 'China (Shang Dynasty)'],
    correctIndex: 2, explanation: 'The Indus Valley script remains undeciphered despite numerous attempts, making Harappan culture uniquely mysterious.',
    era: 'ancient', difficulty: 'advanced', category: 'artifacts',
  },
  {
    id: 'a4', question: 'How many core node labels exist in the Annals schema v4?',
    options: ['7', '9', '11', '15'],
    correctIndex: 2, explanation: 'The 11 labels are: Idea, Person, Place, EventWindow, Institution, Movement, Text, Evidence, Corpus, Framework, Timeframe.',
    difficulty: 'advanced', category: 'ideas',
  },
  {
    id: 'a5', question: 'What statistical phenomenon explains Africa\'s colonial linguistic imprint?',
    options: ['23 French-speaking, 20 English-speaking nations', 'All 55 countries use European languages', 'Only 5 countries have indigenous official languages', 'Arabic is the dominant language in Sub-Saharan Africa'],
    correctIndex: 0, explanation: 'The colonial linguistic echo: 23 nations speak French and 20 speak English as official languages — far exceeding indigenous language adoption at the state level.',
    difficulty: 'advanced', category: 'movements',
  },

  // ─── EXPERT ───
  {
    id: 'e1', question: 'In the Annals curator workflow, what are the 6 stages in order?',
    options: [
      'Draft → Review → Cite → Frame → Publish → Archive',
      'Propose → Cite → Frame → Place → Review → Publish',
      'Create → Validate → Link → Map → Approve → Deploy',
      'Research → Write → Cite → Review → Edit → Publish'
    ],
    correctIndex: 1, explanation: 'The 6-stage workflow ensures scholarly rigor: Propose → Cite → Frame → Place → Review → Publish.',
    difficulty: 'expert', category: 'ideas',
  },
  {
    id: 'e2', question: 'Which base-number system did the ancient Mesopotamians develop, still used in modern timekeeping?',
    options: ['Base-10 (decimal)', 'Base-2 (binary)', 'Base-60 (sexagesimal)', 'Base-12 (duodecimal)'],
    correctIndex: 2, explanation: 'The Sumerian/Babylonian base-60 system gives us 60 seconds in a minute and 60 minutes in an hour.',
    era: 'ancient', difficulty: 'expert', category: 'ideas',
  },
  {
    id: 'e3', question: 'According to the Annals schema, what relationship verb indicates "knowledge transmission across generations"?',
    options: ['INFLUENCES', 'TRANSMITS', 'CANONIZES', 'DEFINES'],
    correctIndex: 1, explanation: 'TRANSMITS captures the concept of passing knowledge, texts, or traditions forward through generations.',
    difficulty: 'expert', category: 'ideas',
  },
]

/* ─── Pre-built Quiz Sessions ─── */
export const QUIZ_SESSIONS: QuizSession[] = [
  {
    id: 'world-history-basics',
    title: 'World History Basics',
    description: 'Test your knowledge of fundamental world history events and civilizations.',
    difficulty: 'beginner',
    questions: ALL_QUESTIONS.filter(q => q.difficulty === 'beginner'),
  },
  {
    id: 'intermediate-history',
    title: 'Deeper into History',
    description: 'Intermediate questions on historical patterns, trade, and cultural exchange.',
    difficulty: 'intermediate',
    questions: ALL_QUESTIONS.filter(q => q.difficulty === 'intermediate'),
  },
  {
    id: 'advanced-knowledge',
    title: 'Advanced Historical Knowledge',
    description: 'Challenge yourself with advanced questions about civilizations, data patterns, and the Annals project.',
    difficulty: 'advanced',
    questions: ALL_QUESTIONS.filter(q => q.difficulty === 'advanced'),
  },
  {
    id: 'expert-challenge',
    title: 'Expert Challenge',
    description: 'Only for true history scholars and Annals contributors.',
    difficulty: 'expert',
    questions: ALL_QUESTIONS.filter(q => q.difficulty === 'expert'),
  },
  {
    id: 'ancient-world-focus',
    title: 'Ancient Civilizations',
    description: 'Focus on the Ancient World era — Egypt, Mesopotamia, Greece, Rome, and beyond.',
    difficulty: 'intermediate',
    era: 'ancient',
    questions: ALL_QUESTIONS.filter(q => q.era === 'ancient'),
  },
  {
    id: 'all-eras-mixed',
    title: 'All Eras Mixed',
    description: 'A mix of questions from all difficulty levels and eras.',
    difficulty: 'intermediate',
    questions: ALL_QUESTIONS,
  },
]

export { ALL_QUESTIONS }
