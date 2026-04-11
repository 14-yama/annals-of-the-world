/**
 * Egyptian Corpus — Ancient Egyptian Texts
 *
 * Covers: Pyramid Texts, Coffin Texts, Book of the Dead, Instruction literature,
 * medical papyri, king lists, temple inscriptions, and wisdom texts
 * spanning over 3,000 years of Pharaonic civilization (c. 3100–30 BCE).
 *
 * Call Number Assignments:
 *   730.03  — Corpus node
 *   730.40–59 — Egyptian Texts
 *   250.20–29 — Egyptian Figures
 *   340.15–19 — Egyptian Institutions
 *   440.15–19 — Egyptian Places
 *   570.15–19 — Egyptian Events
 *   140.15–19 — Egyptian Ideas
 *   810.15–19 — Egyptian Evidence
 */
import type { Entity } from '../../entityTypes'

export const EGYPTIAN_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  CORPUS NODE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'egyptian_corpus',
    name: 'The Egyptian Corpus',
    label: 'Text',
    callNumber: '730.03-egyptian-corpus',
    subjectHeadings: ['Artifacts & Texts — Ancient Egyptian Texts — Pharaonic Canon'],
    subjects: ['Egypt', 'Pharaonic', 'Hieroglyphic', 'Papyrus', 'Pyramid Texts', 'Book of the Dead', 'Ancient Egypt'],
    summary: 'The Egyptian Corpus encompasses over three millennia of literary, religious, medical, legal, and administrative texts produced by ancient Egyptian civilization (c. 3100–30 BCE). Written in hieroglyphic, hieratic, and demotic scripts on papyrus, stone, pottery, and tomb walls, this corpus includes humanity\'s oldest religious texts (Pyramid Texts, c. 2400 BCE), the oldest known wisdom literature (Instruction of Ptahhotep), the most elaborate funerary literature (Book of the Dead), sophisticated medical and mathematical treatises, royal propaganda, love poetry, and mythological narratives. The corpus was largely inaccessible until Jean-François Champollion\'s decipherment of hieroglyphics in 1822 using the Rosetta Stone.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 3100–30 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Invention of hieroglyphic writing in predynastic Egypt', type: 'Idea', year: 'c. 3200 BCE' },
      { title: 'Pharaonic state requires administrative and religious record-keeping', type: 'Institution', year: 'c. 3100 BCE' },
    ],
    effects: [
      { title: 'Afterlife theology influences Greek (Orphism) and Christian eschatology', type: 'Idea', year: 'c. 500 BCE' },
      { title: 'Medical and mathematical knowledge transmitted to Greek world', type: 'Text', year: 'c. 300 BCE' },
      { title: 'Wisdom literature parallels in biblical Proverbs and Ecclesiastes', type: 'Text', year: 'c. 700 BCE' },
    ],
    relationships: [
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'CONTAINS', targetSlug: 'pyramid_texts', targetName: 'Pyramid Texts', context: 'Oldest religious texts in the world' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'CONTAINS', targetSlug: 'book_of_the_dead', targetName: 'Book of the Dead', context: 'Premier funerary text collection' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'CONTAINS', targetSlug: 'coffin_texts', targetName: 'Coffin Texts', context: 'Middle Kingdom funerary literature' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'CONTAINS', targetSlug: 'instruction_of_ptahhotep', targetName: 'Instruction of Ptahhotep', context: 'Oldest wisdom literature' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'CONTAINS', targetSlug: 'edwin_smith_papyrus', targetName: 'Edwin Smith Papyrus', context: 'Oldest surgical treatise' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'INFLUENCES', targetSlug: 'biblical_corpus', targetName: 'The Biblical Corpus', context: 'Wisdom literature parallels (Proverbs, Amenemope)' },
      { sourceSlug: 'egyptian_corpus', sourceName: 'The Egyptian Corpus', verb: 'INFLUENCES', targetSlug: 'graeco_roman_corpus', targetName: 'The Graeco-Roman Corpus', context: 'Hermetic tradition, medical knowledge' },
    ],
    places: [
      { name: 'Thebes (Luxor)', role: 'Major temple and tomb complexes', slug: 'thebes_egypt' },
      { name: 'Memphis', role: 'Old Kingdom capital and administrative center', slug: 'memphis_egypt' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  TEXTS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'pyramid_texts',
    name: 'Pyramid Texts',
    label: 'Text',
    callNumber: '730.40-pyramid-texts',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Egyptian Funerary Literature'],
    subjects: ['Old Kingdom', 'Funerary Texts', 'Afterlife', 'Pharaoh', 'Saqqara', 'Unas', 'Oldest Religious Texts'],
    summary: 'The oldest corpus of religious texts in the world, first inscribed on the interior walls of the pyramid of Pharaoh Unas (c. 2345 BCE) at Saqqara, and subsequently in pyramids of later Old Kingdom pharaohs and queens. Comprising over 800 "utterances" (spells), the Pyramid Texts were designed to ensure the pharaoh\'s resurrection and ascension to the stars among the gods. They contain incantations, hymns, mythological allusions (Osiris, Horus, Set), ritual instructions, and cosmological narratives. These texts represent the earliest written expression of Egyptian afterlife theology and directly ancestor the later Coffin Texts and Book of the Dead.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 2400–2200 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Royal ideology demands textual assurance of pharaonic immortality', type: 'Idea', year: 'c. 2500 BCE' },
    ],
    effects: [
      { title: 'Ancestor of Coffin Texts and Book of the Dead', type: 'Text', year: 'c. 2100 BCE', slug: 'coffin_texts' },
      { title: 'Establishes Osiris-centered afterlife theology', type: 'Idea', year: 'c. 2400 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Saqqara', role: 'Pyramid of Unas — first inscribed pyramid', slug: 'saqqara' },
    ],
    texts: [],
  },
  {
    slug: 'coffin_texts',
    name: 'Coffin Texts',
    label: 'Text',
    callNumber: '730.41-coffin-texts',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Egyptian Funerary Literature'],
    subjects: ['Middle Kingdom', 'Funerary Texts', 'Afterlife', 'Democratization of Afterlife', 'Coffins', 'Spells'],
    summary: 'A collection of over 1,185 funerary spells written on the interior surfaces of wooden coffins during the Middle Kingdom (c. 2055–1650 BCE). The Coffin Texts represent a crucial democratization of Egyptian afterlife religion: whereas the Pyramid Texts were reserved for royalty, the Coffin Texts extended the promise of resurrection to non-royal elites. They introduce the concept of the Field of Reeds (the Egyptian paradise), the Book of Two Ways (the earliest known map of the afterlife), and elaborate Osirian mythology. Many spells were later incorporated into the New Kingdom Book of the Dead.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 2055–1650 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Social changes of First Intermediate Period democratize afterlife access', type: 'Event', year: 'c. 2100 BCE' },
    ],
    effects: [
      { title: 'Book of Two Ways creates first "map" of the afterlife', type: 'Text', year: 'c. 2000 BCE' },
      { title: 'Direct ancestor of the Book of the Dead', type: 'Text', year: 'c. 1550 BCE', slug: 'book_of_the_dead' },
    ],
    relationships: [],
    places: [
      { name: 'El-Bersha', role: 'Major find-spot for Coffin Text coffins' },
    ],
    texts: [],
  },
  {
    slug: 'book_of_the_dead',
    name: 'Book of the Dead',
    label: 'Text',
    callNumber: '730.42-book-of-the-dead',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Egyptian Funerary Literature'],
    subjects: ['New Kingdom', 'Funerary Texts', 'Afterlife', 'Judgment', 'Weighing of the Heart', 'Osiris', 'Papyrus'],
    summary: 'The ancient Egyptian funerary text known as "The Book of Coming Forth by Day" (rw nw prt m hrw), a collection of roughly 200 spells, hymns, and instructions composed on papyrus scrolls and placed with the dead during interment. Developed from the Coffin Texts during the New Kingdom (c. 1550–50 BCE), the Book of the Dead guided the deceased through the dangers of the Duat (underworld) to final judgment before Osiris. Its most famous scene — Spell 125, the "Weighing of the Heart" against the feather of Ma\'at by the jackal-headed god Anubis — represents one of the earliest conceptions of moral judgment after death, profoundly influencing later Graeco-Roman, Jewish, and Christian eschatological imagery.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1550–50 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Evolution from Coffin Texts during Second Intermediate Period', type: 'Text', year: 'c. 1650 BCE', slug: 'coffin_texts' },
    ],
    effects: [
      { title: 'Moral judgment theme influences Greek and Christian afterlife concepts', type: 'Idea', year: 'c. 500 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Thebes (Luxor)', role: 'Major production center for papyrus scrolls', slug: 'thebes_egypt' },
    ],
    texts: [],
  },
  {
    slug: 'instruction_of_ptahhotep',
    name: 'Instruction of Ptahhotep',
    label: 'Text',
    callNumber: '730.43-instruction-of-ptahhotep',
    subjectHeadings: ['Artifacts & Texts — Wisdom Literature — Egyptian Instruction Texts'],
    subjects: ['Wisdom Literature', 'Old Kingdom', 'Ethics', 'Vizier', 'Instruction Genre', 'Sebayt'],
    summary: 'One of the oldest works of wisdom literature in the world, attributed to the vizier Ptahhotep of the Fifth Dynasty (c. 2400 BCE), though the surviving copies date to the Middle Kingdom (c. 1850 BCE). Comprising 37 maxims addressed from an aging father to his son on proper conduct, the text covers topics such as humility before superiors, discretion in speech, patience, fidelity, generosity to the poor, and the dangers of greed and sexual misconduct. Part of the Egyptian "sebayt" (instruction) genre, it establishes the template for wisdom literature that extends through the biblical Proverbs, Ecclesiastes, and ben Sira.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 2400 BCE (composition); c. 1850 BCE (earliest copy)',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Egyptian scribal tradition of formal instruction literature', type: 'Institution', year: 'c. 2500 BCE' },
    ],
    effects: [
      { title: 'Template for Biblical wisdom literature (Proverbs, Ecclesiastes)', type: 'Text', year: 'c. 700 BCE' },
    ],
    relationships: [
      { sourceSlug: 'instruction_of_ptahhotep', sourceName: 'Instruction of Ptahhotep', verb: 'INFLUENCES', targetSlug: 'proverbs_book', targetName: 'Proverbs', context: 'Egyptian sebayt genre influences biblical wisdom' },
    ],
    places: [
      { name: 'Memphis', role: 'Old Kingdom court where Ptahhotep served as vizier', slug: 'memphis_egypt' },
    ],
    texts: [],
  },
  {
    slug: 'instruction_of_amenemope',
    name: 'Instruction of Amenemope',
    label: 'Text',
    callNumber: '730.44-instruction-of-amenemope',
    subjectHeadings: ['Artifacts & Texts — Wisdom Literature — Egyptian Instruction Texts'],
    subjects: ['Wisdom Literature', 'New Kingdom', 'Proverbs', 'Ethics', 'Scribal', 'Biblical Parallels'],
    summary: 'An Egyptian wisdom text composed during the New Kingdom or Third Intermediate Period (c. 1100 BCE), consisting of 30 chapters of moral instruction. Attributed to a scribe named Amenemope son of Kanakht, the text advises against greed, dishonesty, and exploitation of the weak. Its direct literary relationship with the biblical Book of Proverbs (especially Proverbs 22:17–24:22, the "Words of the Wise" section) is one of the most significant demonstrated cases of literary borrowing between Egyptian and Hebrew wisdom traditions, making it a keystone text in comparative biblical studies.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1100 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Egyptian sebayt tradition and scribal education system', type: 'Institution', year: 'c. 2000 BCE' },
    ],
    effects: [
      { title: 'Direct literary borrowing in biblical Proverbs 22:17–24:22', type: 'Text', year: 'c. 700 BCE' },
    ],
    relationships: [],
    places: [],
    texts: [],
  },
  {
    slug: 'edwin_smith_papyrus',
    name: 'Edwin Smith Papyrus',
    label: 'Text',
    callNumber: '730.45-edwin-smith-papyrus',
    subjectHeadings: ['Artifacts & Texts — Scientific Texts — Egyptian Medical Literature'],
    subjects: ['Medicine', 'Surgery', 'Anatomy', 'Rational Medicine', 'Papyrus', 'Imhotep'],
    summary: 'The oldest known surgical treatise in human history, a hieratic papyrus dating to c. 1600 BCE (likely copied from an Old Kingdom original, c. 2500 BCE, possibly by Imhotep or his school). The text presents 48 case studies of traumatic injuries — from skull fractures to spinal injuries — organized systematically from head to torso with diagnosis, prognosis ("an ailment I will treat," "an ailment I will contend with," or "an ailment not to be treated"), and treatment protocols. Remarkably, the text relies on empirical observation rather than magical incantations, making it the earliest document of rational medical practice.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1600 BCE (copy); c. 2500 BCE (original)',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Egyptian medical tradition developed from pyramid-age practices', type: 'Institution', year: 'c. 2600 BCE' },
    ],
    effects: [
      { title: 'Earliest example of rational medical documentation', type: 'Idea', year: 'c. 2500 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Thebes (Luxor)', role: 'Purchased in Luxor in 1862' },
    ],
    texts: [],
  },
  {
    slug: 'tale_of_sinuhe',
    name: 'Tale of Sinuhe',
    label: 'Text',
    callNumber: '730.46-tale-of-sinuhe',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Egyptian Narrative'],
    subjects: ['Middle Kingdom', 'Literature', 'Exile', 'Return', 'Masterpiece', 'Egyptian Fiction'],
    summary: 'Considered the masterpiece of ancient Egyptian literature, the Tale of Sinuhe (c. 1875 BCE) is a first-person narrative of a court official who flees Egypt after the assassination of Pharaoh Amenemhat I, lives in exile among the Aamu (Asiatics) in Canaan-Syria where he prospers as a warrior-chieftain, and eventually returns to Egypt to receive the king\'s pardon and a proper burial. Combining autobiography, adventure, psychological depth, and theological reflection on the power of the pharaoh, it was the most widely copied text in ancient Egypt — found on more papyri and ostraca than any other literary work, used as a standard school text for centuries.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1875 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Transition from Eleventh to Twelfth Dynasty inspires exile narrative', type: 'Event', year: 'c. 1985 BCE' },
    ],
    effects: [
      { title: 'Most copied text in ancient Egypt — standard scribal training text', type: 'Text', year: 'c. 1800 BCE' },
    ],
    relationships: [],
    places: [],
    texts: [],
  },
  {
    slug: 'great_hymn_to_the_aten',
    name: 'Great Hymn to the Aten',
    label: 'Text',
    callNumber: '730.47-great-hymn-to-the-aten',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Egyptian Hymnal Literature'],
    subjects: ['Akhenaten', 'Aten', 'Monotheism', 'Amarna Period', 'Solar Worship', 'Psalm 104'],
    summary: 'A hymn to the sun-disk god Aten, inscribed in the tomb of the courtier Ay at Amarna (c. 1350 BCE), attributed to Pharaoh Akhenaten himself. The hymn celebrates the Aten as the sole creator and sustainer of all life — arguably the earliest expression of something approaching monotheism in recorded history. Its striking parallels with Psalm 104 of the Hebrew Bible ("You spread the darkness, and it is night") have generated extensive scholarly debate about possible literary connections. The hymn exemplifies Akhenaten\'s revolutionary religious reform that briefly displaced the traditional Egyptian pantheon.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1350 BCE',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Akhenaten\'s religious revolution displaces Amun priesthood', type: 'Person', year: 'c. 1353 BCE', slug: 'akhenaten' },
    ],
    effects: [
      { title: 'Parallels with Psalm 104 suggest cross-cultural literary influence', type: 'Text', year: 'c. 500 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Amarna', role: 'Akhenaten\'s capital — tomb of Ay inscription site' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PEOPLE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'imhotep',
    name: 'Imhotep',
    label: 'Person',
    callNumber: '250.20-imhotep',
    subjectHeadings: ['People — Ancient Scholars — Egyptian Polymath'],
    subjects: ['Architect', 'Physician', 'Vizier', 'Step Pyramid', 'Djoser', 'Deified Scholar'],
    summary: 'Chancellor of the Pharaoh Djoser, architect of the Step Pyramid at Saqqara (the world\'s first monumental stone structure, c. 2670 BCE), and one of the earliest known physicians. Imhotep was a rare commoner who achieved near-divine status — later deified as a god of medicine and wisdom (equated with Greek Asclepius). He is credited with pioneering stone architecture and possibly authoring the earliest medical and wisdom texts. His reputation persisted for over 2,000 years after his death, making him one of the most enduring intellectual figures of the ancient world.',
    born: 'c. 2700 BCE',
    died: 'c. 2630 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Designed the Step Pyramid — first monumental stone architecture', type: 'Event', year: 'c. 2670 BCE' },
      { title: 'Deified as god of medicine and wisdom', type: 'Idea', year: 'c. 525 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Saqqara', role: 'Designed the Step Pyramid complex', slug: 'saqqara' },
      { name: 'Memphis', role: 'Served as vizier', slug: 'memphis_egypt' },
    ],
    texts: [],
  },
  {
    slug: 'akhenaten',
    name: 'Akhenaten',
    label: 'Person',
    callNumber: '250.21-akhenaten',
    subjectHeadings: ['People — Ancient Rulers — Egyptian Pharaohs'],
    subjects: ['Amarna Period', 'Monotheism', 'Aten', 'Religious Revolution', 'Heretic Pharaoh', 'Nefertiti'],
    summary: 'Pharaoh of the Eighteenth Dynasty (r. c. 1353–1336 BCE), born Amenhotep IV, who initiated a radical religious revolution — replacing the traditional Egyptian pantheon headed by Amun-Ra with exclusive worship of the Aten (the solar disk). He moved the capital from Thebes to a new city, Akhetaten (modern Amarna), closed Amun temples, and commissioned art in a distinctive naturalistic style. His "heresy" was reversed after his death, and his name was erased from king lists. Whether his Atenism constitutes true monotheism or monolatry remains debated. His wife Nefertiti and son Tutankhamun are among the most famous figures of antiquity.',
    born: 'c. 1380 BCE',
    died: 'c. 1336 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Great Hymn to the Aten — possible influence on Hebrew Psalm 104', type: 'Text', year: 'c. 1350 BCE', slug: 'great_hymn_to_the_aten' },
      { title: 'Amarna art style revolutionizes Egyptian aesthetics', type: 'Idea', year: 'c. 1350 BCE' },
    ],
    relationships: [
      { sourceSlug: 'akhenaten', sourceName: 'Akhenaten', verb: 'AUTHORS', targetSlug: 'great_hymn_to_the_aten', targetName: 'Great Hymn to the Aten', context: 'Attributed to the pharaoh' },
    ],
    places: [
      { name: 'Amarna', role: 'Founded new capital Akhetaten' },
    ],
    texts: [],
  },
  {
    slug: 'thutmose_iii',
    name: 'Thutmose III',
    label: 'Person',
    callNumber: '250.22-thutmose-iii',
    subjectHeadings: ['People — Ancient Rulers — Egyptian Pharaohs'],
    subjects: ['New Kingdom', 'Battle of Megiddo', 'Empire Builder', 'Military Genius', 'Eighteenth Dynasty'],
    summary: 'Pharaoh of the Eighteenth Dynasty (r. c. 1479–1425 BCE), often called the "Napoleon of Egypt" for his military genius. After emerging from the co-regency with his stepmother Hatshepsut, Thutmose III conducted at least 17 military campaigns, expanding Egypt to its greatest territorial extent from the Fourth Cataract in Nubia to the Euphrates in Syria. His Annals, inscribed on the walls of the Temple of Karnak, provide the most detailed military records from the ancient world, including the Battle of Megiddo (c. 1457 BCE) — the earliest battle recorded in sufficient detail to be analyzed strategically.',
    born: 'c. 1481 BCE',
    died: '1425 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Egyptian Empire reaches maximum extent', type: 'Event', year: 'c. 1450 BCE' },
      { title: 'Annals provide earliest detailed military history', type: 'Text', year: 'c. 1450 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Thebes (Luxor)', role: 'Capital; Karnak temple inscriptions', slug: 'thebes_egypt' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  INSTITUTIONS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'house_of_life',
    name: 'House of Life (Per Ankh)',
    label: 'Institution',
    callNumber: '340.15-house-of-life',
    subjectHeadings: ['Institutions — Educational Institutions — Egyptian Scriptoria'],
    subjects: ['Scribal School', 'Temple Library', 'Papyrus', 'Religious Texts', 'Medical Texts', 'Egyptian Education'],
    summary: 'The Per Ankh ("House of Life") was an institution attached to major Egyptian temples, functioning as a combination of scriptorium, library, school, and research center. These institutions were responsible for composing, copying, and preserving religious texts (including the Book of the Dead), medical papyri, astronomical records, and ritual manuals. Staffed by lector-priests and scribes, the Houses of Life at temples like Karnak, Edfu, and Dendera were the primary engines of Egyptian intellectual life, maintaining textual traditions across millennia. They are the closest ancient Egyptian equivalent to medieval European monasteries as centers of learning and textual preservation.',
    founded: 'c. 2600 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Preserved Egyptian literary and medical traditions for millennia', type: 'Text', year: 'c. 2000 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Thebes (Luxor)', role: 'Major House of Life at Karnak', slug: 'thebes_egypt' },
    ],
    texts: [],
  },
  {
    slug: 'priesthood_of_amun',
    name: 'Priesthood of Amun',
    label: 'Institution',
    callNumber: '340.16-priesthood-of-amun',
    subjectHeadings: ['Institutions — Religious Institutions — Egyptian Priesthoods'],
    subjects: ['Amun', 'Karnak', 'Thebes', 'Temple Economy', 'Religious Power', 'New Kingdom'],
    summary: 'The most powerful religious institution in ancient Egypt, centered at the great temple complex of Karnak in Thebes. During the New Kingdom (c. 1550–1070 BCE), the priesthood of Amun controlled vast estates, enormous wealth, and wielded political influence rivaling or exceeding that of the pharaoh. The High Priest of Amun effectively ruled Upper Egypt during the late New Kingdom. Akhenaten\'s religious revolution was partly motivated by desire to break Amun\'s priestly monopoly. The institution persisted for over a millennium, accumulating texts, administering temple economies, and conducting elaborate rituals that generated much of the surviving Egyptian religious corpus.',
    founded: 'c. 2000 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Accumulated enormous political and economic power', type: 'Institution', year: 'c. 1100 BCE' },
      { title: 'Akhenaten\'s revolution partly aimed at breaking Amun monopoly', type: 'Event', year: 'c. 1353 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Thebes (Luxor)', role: 'Karnak temple complex — center of Amun worship', slug: 'thebes_egypt' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PLACES
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'thebes_egypt',
    name: 'Thebes (Luxor)',
    label: 'Place',
    callNumber: '440.15-thebes-egypt',
    subjectHeadings: ['Places — Ancient Cities — Egyptian Cities'],
    subjects: ['Upper Egypt', 'Karnak', 'Valley of the Kings', 'Amun', 'New Kingdom Capital'],
    summary: 'Ancient Egyptian city on the east bank of the Nile (modern Luxor), serving as capital during much of the New Kingdom (c. 1550–1070 BCE) and the religious center of Egypt for over two millennia. Home to the Karnak temple complex (the largest religious building ever constructed), the Luxor Temple, and the Valley of the Kings on the west bank. Thebes was the seat of the powerful Amun priesthood and the burial site of pharaohs from Thutmose I through Ramesses XI. Greek visitors called it the "City of a Hundred Gates," and Homer mentioned it in the Iliad.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 3200 BCE – 664 BCE (major period)',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [],
    relationships: [],
    places: [],
    texts: [],
  },
  {
    slug: 'memphis_egypt',
    name: 'Memphis',
    label: 'Place',
    callNumber: '440.16-memphis-egypt',
    subjectHeadings: ['Places — Ancient Cities — Egyptian Cities'],
    subjects: ['Old Kingdom', 'Capital', 'Lower Egypt', 'Ptah', 'Saqqara', 'Administrative Center'],
    summary: 'Capital of ancient Egypt during the Old Kingdom (c. 2686–2181 BCE) and the administrative center of Egypt for much of its history, located at the apex of the Nile Delta near modern Cairo. Founded by Menes (Narmer), the unifier of Upper and Lower Egypt, Memphis was home to the great temple of Ptah, the Saqqara necropolis (including the Step Pyramid of Djoser), and a cosmopolitan population that included foreign traders, diplomats, and craftsmen. The "Memphite Theology," inscribed on the Shabaka Stone, preserves one of the most sophisticated theological compositions from the ancient world.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 3100 BCE – 7th century CE',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [],
    relationships: [],
    places: [],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  IDEAS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'maat_concept',
    name: 'Ma\'at (Cosmic Order)',
    label: 'Idea',
    callNumber: '140.15-maat',
    subjectHeadings: ['Ideas — Philosophical Concepts — Egyptian Ethics'],
    subjects: ['Truth', 'Justice', 'Cosmic Order', 'Ethics', 'Egyptian Philosophy', 'Divine Balance'],
    summary: 'The central ethical and cosmological concept of ancient Egyptian civilization, personified as a goddess wearing an ostrich feather. Ma\'at represented truth, justice, cosmic order, balance, and right conduct — the fundamental principle by which the universe functioned and by which human society should be governed. The pharaoh\'s primary duty was to uphold Ma\'at; the judgment of the dead consisted of weighing the heart against the feather of Ma\'at. It pervaded every aspect of Egyptian life: law, governance, religious ritual, and personal ethics. Ma\'at is one of the earliest articulations of a universal moral order in human thought.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 2400 BCE – 30 BCE',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Concept of moral judgment after death influences Western eschatology', type: 'Idea', year: 'c. 500 BCE' },
    ],
    relationships: [],
    places: [],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  EVIDENCE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'rosetta_stone',
    name: 'Rosetta Stone',
    label: 'Evidence',
    callNumber: '810.15-rosetta-stone',
    subjectHeadings: ['Evidence — Archaeological Artifacts — Egyptian Inscriptions'],
    subjects: ['Decipherment', 'Hieroglyphics', 'Champollion', 'Ptolemaic', 'British Museum', 'Trilingual Inscription'],
    summary: 'A granodiorite stele inscribed in 196 BCE with a priestly decree honoring Ptolemy V in three scripts: Egyptian hieroglyphic, Egyptian demotic, and ancient Greek. Discovered by Napoleon\'s soldiers in 1799 at Rashid (Rosetta), Egypt, and subsequently used by Jean-François Champollion in 1822 to decipher Egyptian hieroglyphics — unlocking 3,000 years of previously unreadable Egyptian texts. Now in the British Museum, the Rosetta Stone is arguably the most important archaeological discovery in the history of Egyptology and one of the most visited objects in any museum worldwide.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    period: '196 BCE (inscription); 1799 CE (discovery)',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Champollion deciphers hieroglyphics, founding modern Egyptology', type: 'Event', year: '1822 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Rashid (Rosetta)', role: 'Discovery site' },
    ],
    texts: [],
  },
]
