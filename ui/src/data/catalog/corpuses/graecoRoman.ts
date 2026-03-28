/**
 * Graeco-Roman Corpus — Greek & Latin classics, philosophy, Roman law
 *
 * Covers: Homer, tragedy, philosophy (Plato, Aristotle, Stoics), history (Herodotus,
 * Thucydides), Roman law (Corpus Iuris Civilis), poetry (Virgil, Ovid),
 * rhetoric, science, and medicine spanning c. 800 BCE – 565 CE.
 */
import type { Entity } from '../../entityTypes'

export const GRAECO_ROMAN_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  CORPUS NODE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'graeco_roman_corpus',
    name: 'The Graeco-Roman Corpus',
    label: 'Text',
    callNumber: '730.05-graeco-roman-corpus',
    subjectHeadings: ['Artifacts & Texts — Classical Literature — Greek & Latin Canon'],
    subjects: ['Greek Literature', 'Latin Literature', 'Classical Philosophy', 'Roman Law', 'Homer', 'Plato', 'Aristotle', 'Western Canon'],
    summary: 'The Graeco-Roman Corpus encompasses the literary, philosophical, legal, scientific, and historical texts of ancient Greek and Roman civilization (c. 800 BCE – 565 CE). This corpus forms the bedrock of the Western intellectual tradition: Homer\'s epics, Athenian tragedy and comedy, Platonic and Aristotelian philosophy, Stoic and Epicurean ethics, the historical works of Herodotus and Thucydides, Roman oratory (Cicero), epic poetry (Virgil), lyric poetry (Sappho, Horace, Ovid), scientific treatises (Euclid, Archimedes, Ptolemy, Galen), and the Corpus Iuris Civilis of Justinian — the legal foundation of European civil law. Transmitted through Hellenistic libraries, medieval monasteries, Byzantine scriptoria, and Arabic translations, this corpus has shaped Western philosophy, law, science, democracy, literature, and art for over two millennia.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 800 BCE – 565 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Greek alphabetic literacy enables widespread literary composition', type: 'Idea', year: 'c. 800 BCE' },
      { title: 'Athenian democracy and public discourse foster oratory, philosophy, and drama', type: 'Institution', year: 'c. 500 BCE' },
    ],
    effects: [
      { title: 'Foundation of Western philosophy, science, and political theory', type: 'Idea', year: 'c. 300 BCE' },
      { title: 'Corpus Iuris Civilis becomes basis of European civil law', type: 'Text', year: '534 CE' },
      { title: 'Renaissance revival transforms European culture', type: 'Movement', year: 'c. 1400 CE' },
    ],
    relationships: [
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'iliad', targetName: 'Iliad', context: 'Foundational Greek epic' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'the_republic_plato', targetName: 'The Republic', context: 'Foundational work of political philosophy' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'nicomachean_ethics', targetName: 'Nicomachean Ethics', context: 'Foundational work of ethics' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'histories_herodotus', targetName: 'Histories', context: 'First work of Western history' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'corpus_iuris_civilis', targetName: 'Corpus Iuris Civilis', context: 'Foundation of European civil law' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'CONTAINS', targetSlug: 'aeneid', targetName: 'Aeneid', context: 'Roman national epic' },
      { sourceSlug: 'graeco_roman_corpus', sourceName: 'The Graeco-Roman Corpus', verb: 'INFLUENCES', targetSlug: 'biblical_corpus', targetName: 'The Biblical Corpus', context: 'Septuagint translation; NT written in Koine Greek' },
    ],
    places: [
      { name: 'Athens', role: 'Intellectual and cultural center of the Greek world', slug: 'athens_city' },
      { name: 'Rome', role: 'Political and legal center of the Roman world', slug: 'rome_city' },
      { name: 'Alexandria', role: 'Great Library and center of Hellenistic scholarship', slug: 'alexandria_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  TEXTS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'iliad',
    name: 'Iliad',
    label: 'Text',
    callNumber: '730.60-iliad',
    subjectHeadings: ['Artifacts & Texts — Classical Literature — Greek Epic Poetry'],
    subjects: ['Homer', 'Trojan War', 'Achilles', 'Epic Poetry', 'Greek Literature', 'Oral Poetry'],
    summary: 'The foundational work of Western literature, attributed to Homer (c. 750–700 BCE). In 15,693 lines of dactylic hexameter, the Iliad narrates a few weeks during the tenth year of the Trojan War, centering on the wrath of Achilles — his quarrel with Agamemnon, withdrawal from battle, return after Patroclus\'s death, and slaying of Hector. Far more than a war story, the Iliad explores universal themes of mortality, glory (kleos), honor, love, grief, and the pity of war. It established the conventions of epic poetry, shaped Greek religion and ethics, and has been continuously read, imitated, and debated for nearly three millennia.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 750–700 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Mycenaean oral bardic tradition', type: 'Text', year: 'c. 1200 BCE' },
      { title: 'Adoption of the Greek alphabet enables transcription', type: 'Idea', year: 'c. 800 BCE' },
    ],
    effects: [
      { title: 'Establishes conventions of Western epic poetry', type: 'Idea', year: 'c. 700 BCE' },
      { title: 'Virgil\'s Aeneid models itself on Homeric epic', type: 'Text', year: '19 BCE', slug: 'aeneid' },
    ],
    relationships: [
      { sourceSlug: 'homer_poet', sourceName: 'Homer', verb: 'AUTHORS', targetSlug: 'iliad', targetName: 'Iliad', context: 'Attributed author of the foundational Greek epic' },
    ],
    places: [
      { name: 'Troy (Ilion)', role: 'Setting of the epic' },
    ],
    texts: [],
  },
  {
    slug: 'the_republic_plato',
    name: 'The Republic (Politeia)',
    label: 'Text',
    callNumber: '730.61-republic-plato',
    subjectHeadings: ['Artifacts & Texts — Philosophy — Greek Political Philosophy'],
    subjects: ['Plato', 'Justice', 'Philosopher King', 'Allegory of the Cave', 'Forms', 'Ideal State', 'Political Philosophy'],
    summary: 'Plato\'s most famous dialogue (c. 375 BCE), a sweeping exploration of justice, the ideal state, the nature of the soul, education, and the theory of Forms. Through Socrates\' conversation with Glaucon, Adeimantus, and Thrasymachus, Plato constructs an ideal city-state (kallipolis) governed by philosopher-kings, introduces the tripartite soul (reason, spirit, appetite), presents the Allegory of the Cave (the most famous philosophical metaphor in Western thought), the Allegory of the Divided Line, and the Allegory of the Sun. The Republic has shaped political philosophy, epistemology, ethics, and educational theory for 2,400 years.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 375 BCE',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Athenian democracy and its problems inspire political philosophy', type: 'Institution', year: 'c. 400 BCE' },
    ],
    effects: [
      { title: 'Foundation of Western political philosophy', type: 'Idea', year: 'c. 375 BCE' },
      { title: 'Theory of Forms shapes Neoplatonism and Christian theology', type: 'Idea', year: 'c. 250 CE' },
    ],
    relationships: [
      { sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'AUTHORS', targetSlug: 'the_republic_plato', targetName: 'The Republic', context: "Plato's masterwork on justice, ideal governance, and the Form of the Good" }
    ],
    places: [
      { name: 'Athens', role: 'Written and discussed at the Academy', slug: 'athens_city' },
    ],
    texts: [],
  },
  {
    slug: 'nicomachean_ethics',
    name: 'Nicomachean Ethics',
    label: 'Text',
    callNumber: '730.62-nicomachean-ethics',
    subjectHeadings: ['Artifacts & Texts — Philosophy — Greek Ethics'],
    subjects: ['Aristotle', 'Ethics', 'Virtue', 'Eudaimonia', 'Golden Mean', 'Practical Wisdom', 'Phronesis'],
    summary: 'Aristotle\'s foundational treatise on ethics (c. 340 BCE), considered the most influential single work on moral philosophy in the Western tradition. In ten books, Aristotle argues that the highest human good (eudaimonia, "flourishing") is achieved through the practice of virtue (aretē) as habitual activity according to reason. He develops the doctrine of the golden mean (virtue as the intermediate between excess and deficiency), analyzes specific virtues (courage, temperance, justice, generosity), introduces the concept of practical wisdom (phronesis), and explores friendship, pleasure, and the contemplative life. Named for his son Nicomachus, the work profoundly shaped medieval Christian ethics (via Thomas Aquinas), Islamic philosophy (via Averroes), and modern virtue ethics.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 340 BCE',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Shapes Aquinas\'s Christian ethical synthesis', type: 'Idea', year: 'c. 1270 CE' },
      { title: 'Revives as foundation of modern virtue ethics', type: 'Idea', year: 'c. 1958 CE' },
    ],
    relationships: [
      { sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'AUTHORS', targetSlug: 'nicomachean_ethics', targetName: 'Nicomachean Ethics', context: "Aristotle's major ethical treatise on virtue and the good life" }
    ],
    places: [
      { name: 'Athens', role: 'Written at the Lyceum', slug: 'athens_city' },
    ],
    texts: [],
  },
  {
    slug: 'histories_herodotus',
    name: 'Histories (Herodotus)',
    label: 'Text',
    callNumber: '730.63-histories-herodotus',
    subjectHeadings: ['Artifacts & Texts — Historical Texts — Greek Historiography'],
    subjects: ['Herodotus', 'Persian Wars', 'History', 'Ethnography', 'Father of History', 'Greco-Persian Wars'],
    summary: 'The first work of history in the Western tradition, written by Herodotus of Halicarnassus (c. 484–425 BCE) in nine books named after the Muses. Herodotus investigates (historiē, "inquiry") the causes and events of the Greco-Persian Wars (499–479 BCE), while also providing extensive ethnographic, geographic, and cultural digressions on Egypt, Scythia, Persia, Lydia, and Babylon. Cicero called him "the father of history" — though Plutarch called him "the father of lies" for his credulity. The Histories established the genre of historical writing as systematic inquiry into human events, distinguished from myth and epic, and pioneered comparative cultural analysis.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 440–420 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Greco-Persian Wars provide subject matter', type: 'Event', year: '490–479 BCE' },
    ],
    effects: [
      { title: 'Establishes the genre of historical writing in the West', type: 'Idea', year: 'c. 440 BCE' },
      { title: 'Thucydides refines the method into political/military history', type: 'Text', year: 'c. 411 BCE' },
    ],
    relationships: [
      { sourceSlug: 'histories_herodotus', sourceName: 'Histories (Herodotus)', verb: 'DESCRIBES', targetSlug: 'babylon_city', targetName: 'Babylon', context: 'Herodotus Book I provides detailed ethnographic account of Babylon' }
    ],
    places: [
      { name: 'Athens', role: 'Herodotus settled and possibly read his work publicly', slug: 'athens_city' },
    ],
    texts: [],
  },
  {
    slug: 'corpus_iuris_civilis',
    name: 'Corpus Iuris Civilis',
    label: 'Text',
    callNumber: '730.64-corpus-iuris-civilis',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Roman Law'],
    subjects: ['Justinian', 'Roman Law', 'Civil Law', 'Digest', 'Institutes', 'Codex', 'Legal Foundation'],
    summary: 'The monumental codification of Roman law commissioned by Emperor Justinian I (r. 527–565 CE) and compiled by the jurist Tribonian between 529 and 534 CE. Comprising four parts — the Codex (imperial constitutions), the Digest/Pandects (jurists\' opinions from 1,500 years of legal thought), the Institutes (a student textbook), and the Novels (new legislation) — it systematized the entire body of Roman law. Rediscovered in Italy in the 11th century, the Corpus Iuris Civilis became the foundation of the European civil law tradition (used in most of continental Europe, Latin America, East Asia, and parts of Africa) and is the single most influential legal text in human history, second only to religious scriptures in its impact on civilization.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: '529–534 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Justinian seeks to consolidate and simplify 1,000 years of Roman legal tradition', type: 'Person', year: '527 CE' },
    ],
    effects: [
      { title: 'Foundation of European civil law tradition (continental, Latin American, East Asian)', type: 'Idea', year: 'c. 1100 CE' },
      { title: 'Canon law borrows extensively from Roman legal categories', type: 'Text', year: 'c. 1140 CE' },
    ],
    relationships: [
      { sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'INFLUENCES', targetSlug: 'islamic_fiqh_kalam_falsafa_corpus', targetName: 'Islamic Jurisprudence', context: 'Roman legal categories parallel and may have influenced early Islamic jurisprudence' }
    ],
    places: [
      { name: 'Constantinople', role: 'Compiled in the Byzantine capital' },
    ],
    texts: [],
  },
  {
    slug: 'aeneid',
    name: 'Aeneid',
    label: 'Text',
    callNumber: '730.65-aeneid',
    subjectHeadings: ['Artifacts & Texts — Classical Literature — Roman Epic Poetry'],
    subjects: ['Virgil', 'Rome', 'Aeneas', 'Troy', 'Epic Poetry', 'Roman Identity', 'Augustus'],
    summary: 'The Roman national epic, composed by Virgil (Publius Vergilius Maro) between 29 and 19 BCE, left unfinished at his death. In twelve books of dactylic hexameter, the Aeneid narrates the journey of the Trojan hero Aeneas from the fall of Troy to Italy, where he becomes the ancestor of the Romans. Consciously modeled on Homer (books 1–6 echo the Odyssey, 7–12 the Iliad), the Aeneid weaves together mythology, history, and politics to legitimize Augustus\'s reign and celebrate Roman destiny (the famous "mission statement" of empire: parcere subiectis et debellare superbos). It became the central text of Western classical education for 2,000 years and profoundly influenced Dante, Milton, and the entire tradition of epic poetry.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: '29–19 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Augustus\'s Rome seeks literary legitimation of imperial mission', type: 'Event', year: 'c. 29 BCE' },
    ],
    effects: [
      { title: 'Central text of Western classical education for two millennia', type: 'Text', year: 'c. 19 BCE' },
      { title: 'Shapes Dante\'s Divine Comedy (Virgil as guide through Hell)', type: 'Text', year: '1320 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Rome', role: 'Written under Augustan patronage', slug: 'rome_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PEOPLE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'homer_poet',
    name: 'Homer',
    label: 'Person',
    callNumber: '250.30-homer',
    subjectHeadings: ['People — Ancient Authors — Greek Poets'],
    subjects: ['Iliad', 'Odyssey', 'Epic Poetry', 'Oral Tradition', 'Ionia', 'Western Literature'],
    summary: 'The semi-legendary Greek poet traditionally credited with composing the Iliad and the Odyssey (c. 750–700 BCE), the two foundational epics of Western literature. Ancient tradition held him to be a blind bard from Ionia (perhaps Smyrna or Chios). The "Homeric Question" — whether one man composed both epics, or whether they are compilations of oral tradition — has been debated since antiquity. Regardless, the Homeric poems were the "Bible" of ancient Greece: memorized by schoolchildren, quoted by philosophers, and imitated by every subsequent poet. Homer defined the Greek gods, heroes, and moral universe.',
    born: 'c. 800 BCE (traditional)',
    died: 'c. 700 BCE (traditional)',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Iliad and Odyssey become foundation of Western literature', type: 'Text', year: 'c. 750 BCE', slug: 'iliad' },
    ],
    relationships: [
      { sourceSlug: 'homer_poet', sourceName: 'Homer', verb: 'AUTHORS', targetSlug: 'iliad', targetName: 'Iliad', context: 'Traditionally attributed author' },
    ],
    places: [
      { name: 'Ionia', role: 'Traditional homeland (Smyrna or Chios)' },
    ],
    texts: [],
  },
  {
    slug: 'plato_philosopher',
    name: 'Plato',
    label: 'Person',
    callNumber: '250.31-plato',
    subjectHeadings: ['People — Philosophers — Greek Philosophers'],
    subjects: ['Academy', 'Forms', 'Dialogue', 'Philosophy', 'Socrates', 'Political Philosophy', 'Epistemology'],
    summary: 'Athenian philosopher (c. 428–348 BCE), student of Socrates and teacher of Aristotle, founder of the Academy (the first institution of higher learning in the West). Plato\'s 35+ surviving dialogues — featuring Socrates as interlocutor — established or profoundly shaped virtually every branch of Western philosophy: metaphysics (Theory of Forms), epistemology (the Allegory of the Cave), ethics (the Form of the Good), political philosophy (The Republic), aesthetics, logic, and mathematics. Alfred North Whitehead famously said the entire European philosophical tradition "consists of a series of footnotes to Plato."',
    born: 'c. 428 BCE',
    died: 'c. 348 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Founded the Academy — first university in the West', type: 'Institution', year: 'c. 387 BCE' },
      { title: 'Theory of Forms shapes Christian theology via Neoplatonism', type: 'Idea', year: 'c. 250 CE' },
    ],
    relationships: [
      { sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'AUTHORS', targetSlug: 'the_republic_plato', targetName: 'The Republic', context: 'Most famous dialogue' },
    ],
    places: [
      { name: 'Athens', role: 'Founded and taught at the Academy', slug: 'athens_city' },
    ],
    texts: [],
  },
  {
    slug: 'aristotle_philosopher',
    name: 'Aristotle',
    label: 'Person',
    callNumber: '250.32-aristotle',
    subjectHeadings: ['People — Philosophers — Greek Philosophers'],
    subjects: ['Lyceum', 'Logic', 'Physics', 'Metaphysics', 'Ethics', 'Biology', 'Political Philosophy', 'Universal Genius'],
    summary: 'Greek philosopher and polymath (384–322 BCE), student of Plato, tutor of Alexander the Great, and founder of the Lyceum. Aristotle\'s works span virtually every field of knowledge — logic (the Organon, establishing syllogistic reasoning), metaphysics, physics, biology (he classified over 500 species), ethics (Nicomachean Ethics), politics, rhetoric, poetics, and psychology. He was the dominant intellectual authority in the medieval Islamic and Christian worlds (Ibn Rushd and Thomas Aquinas called him simply "The Philosopher"). His influence on Western thought is arguably unsurpassed by any other single thinker.',
    born: '384 BCE',
    died: '322 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Logic (syllogism) dominates Western and Islamic philosophy for 2,000 years', type: 'Idea', year: 'c. 340 BCE' },
      { title: 'Aquinas synthesizes Aristotle with Christian theology', type: 'Idea', year: 'c. 1270 CE' },
    ],
    relationships: [
      { sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'AUTHORS', targetSlug: 'nicomachean_ethics', targetName: 'Nicomachean Ethics', context: 'Foundational ethical treatise' },
    ],
    places: [
      { name: 'Athens', role: 'Founded and taught at the Lyceum', slug: 'athens_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  INSTITUTIONS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'library_of_alexandria',
    name: 'Library of Alexandria',
    label: 'Institution',
    callNumber: '340.20-library-of-alexandria',
    subjectHeadings: ['Institutions — Archives & Libraries — Ancient Libraries'],
    subjects: ['Alexandria', 'Ptolemies', 'Scholarship', 'Hellenistic', 'Mouseion', 'Ancient Library'],
    summary: 'The greatest library and research institution of the ancient world, founded by Ptolemy I Soter (or Ptolemy II Philadelphus) in Alexandria, Egypt, c. 295 BCE. Part of the Mouseion (Museum, "shrine of the Muses"), a state-funded research center, the Library aimed to collect copies of every book in the world — reportedly holding 400,000–700,000 scrolls. It attracted scholars like Euclid, Archimedes, Eratosthenes (who calculated Earth\'s circumference), Aristarchus (who proposed heliocentrism), and the grammarian Callimachus. The Library produced the Septuagint (Greek translation of the Hebrew Bible). Its gradual decline over several centuries (not a single catastrophic burning) marks one of history\'s greatest intellectual losses.',
    founded: 'c. 295 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Ptolemaic ambition to make Alexandria the intellectual capital of the Hellenistic world', type: 'Event', year: 'c. 300 BCE' },
    ],
    effects: [
      { title: 'Preserves and transmits Greek literary and scientific heritage', type: 'Text', year: 'c. 200 BCE' },
      { title: 'Septuagint produced under its patronage', type: 'Text', year: 'c. 250 BCE' },
    ],
    relationships: [
      { sourceSlug: 'library_of_alexandria', sourceName: 'Library of Alexandria', verb: 'TRANSMITS', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Septuagint Greek Old Testament produced under Ptolemaic patronage c. 250 BCE' },
      { sourceSlug: 'library_of_alexandria', sourceName: 'Library of Alexandria', verb: 'OCCURS_IN', targetSlug: 'alexandria_city', targetName: 'Alexandria', context: 'Located in Ptolemaic Alexandria; largest ancient library' },
    ],
    places: [
      { name: 'Alexandria', role: 'Located in the Bruchion quarter', slug: 'alexandria_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PLACES
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'athens_city',
    name: 'Athens',
    label: 'Place',
    callNumber: '440.20-athens',
    subjectHeadings: ['Places — Ancient Cities — Greek City-States'],
    subjects: ['Democracy', 'Philosophy', 'Drama', 'Acropolis', 'Parthenon', 'Classical Greece'],
    summary: 'The cradle of Western democracy, philosophy, drama, and art. Athens in the Classical period (5th–4th centuries BCE) was the intellectual capital of the ancient world: birthplace of democracy (Cleisthenes, Pericles), tragedy (Aeschylus, Sophocles, Euripides), comedy (Aristophanes), historiography (Thucydides), philosophy (Socrates, Plato, Aristotle), and oratory (Demosthenes). The Acropolis, crowned by the Parthenon, remains the supreme architectural symbol of Classical civilization. Though politically eclipsed after Macedonian conquest, Athens remained the preeminent "university city" of the Graeco-Roman world for nearly a millennium.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 3000 BCE – present',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Invention of democracy shapes Western political tradition', type: 'Idea', year: 'c. 508 BCE' },
    ],
    relationships: [
      { sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Academy in Athens c. 387 BCE' },
      { sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Lyceum in Athens c. 335 BCE' }
    ],
    places: [],
    texts: [],
  },
  {
    slug: 'rome_city',
    name: 'Rome',
    label: 'Place',
    callNumber: '440.21-rome',
    subjectHeadings: ['Places — Ancient Cities — Roman Cities'],
    subjects: ['Roman Empire', 'Republic', 'Law', 'Engineering', 'Papacy', 'Eternal City'],
    summary: 'The "Eternal City," capital of the Roman Republic and Empire, seat of the papacy, and one of the most consequential cities in human history. From its legendary founding (753 BCE) through the fall of the Western Empire (476 CE) and beyond, Rome developed the most sophisticated legal system of antiquity, the most extensive road and aqueduct networks, monumental architecture (Colosseum, Pantheon, Forum), and a model of imperial governance that persisted culturally for millennia. As the center of the Catholic Church, Rome continued to shape Western civilization through the medieval and modern periods.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 753 BCE – present',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [],
    relationships: [
      { sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'OCCURS_IN', targetSlug: 'rome_city', targetName: 'Rome', context: 'Codification of Roman law under Justinian, compiled in Constantinople' }
    ],
    places: [],
    texts: [],
  },
  {
    slug: 'alexandria_city',
    name: 'Alexandria',
    label: 'Place',
    callNumber: '440.22-alexandria',
    subjectHeadings: ['Places — Ancient Cities — Hellenistic Cities'],
    subjects: ['Egypt', 'Library', 'Ptolemies', 'Hellenistic', 'Lighthouse', 'Scholarship', 'Multicultural'],
    summary: 'Founded by Alexander the Great in 331 BCE, Alexandria became the greatest city of the Hellenistic world and the intellectual capital of the ancient Mediterranean. Located on the Egyptian coast at the western edge of the Nile Delta, it housed the Library and Mouseion (the ancient world\'s greatest research institution), the Pharos Lighthouse (one of the Seven Wonders), and a cosmopolitan population of Greeks, Egyptians, Jews, and others. The Septuagint was produced here, Euclid wrote the Elements here, and the city remained a center of learning through the Roman period, birthplace of Neoplatonism and early Christian theology (Clement, Origen, Athanasius).',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: '331 BCE – present',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [],
    relationships: [],
    places: [],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  EVIDENCE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'oxyrhynchus_papyri',
    name: 'Oxyrhynchus Papyri',
    label: 'Evidence',
    callNumber: '810.20-oxyrhynchus-papyri',
    subjectHeadings: ['Evidence — Archaeological Artifacts — Greek Papyri'],
    subjects: ['Papyrus', 'Egypt', 'Lost Literature', 'Grenfell', 'Hunt', 'Textual Recovery'],
    summary: 'An enormous collection of over 500,000 papyrus fragments discovered at Oxyrhynchus, Egypt, beginning in 1896–1897 by Bernard Grenfell and Arthur Hunt. The collection includes fragments of lost works by Sappho, Pindar, Sophocles, Euripides, and Menander; early Christian texts (fragments of the Gospel of Thomas); official documents, private letters, tax receipts, and literary exercises — providing an unparalleled window into Graeco-Roman daily life, literature, and religion in Egypt. The Oxyrhynchus Papyri remain the single most important source for recovering lost Greek literature and for understanding the ancient book trade and reading culture.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: '3rd century BCE – 7th century CE (contents); 1896 CE (discovery)',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Recovery of lost Greek literary works (Sappho, Menander, etc.)', type: 'Text', year: '1897 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Oxyrhynchus', role: 'Discovery site in Middle Egypt' },
    ],
    texts: [],
  },
]
