import type { Entity } from '../entityTypes'

/**
 * Division 380 — Educational Institutions (hand-curated expansion)
 * Major seats of learning across all eras and continents.
 */
export const DIV_380_ENTITIES: Entity[] = [

  {
    slug: 'platonic_academy',
    name: 'Platonic Academy',
    label: 'Institution',
    callNumber: '380.04-platonic-academy',
    subjectHeadings: ['Institutions — Educational — Greece — Classical'],
    subjects: ['Education', 'Philosophy', 'Athens', 'Greece', 'Plato', 'Academy'],
    summary: 'Founded by Plato around 387 BCE near Athens, the Academy was the Western world\'s first institution of higher learning. For nearly 900 years (until Justinian closed it in 529 CE), it taught philosophy, mathematics, and dialectics. It educated Aristotle, shaped Neoplatonism, and established the model of the philosophical school that influenced all subsequent Western universities.',
    founded: 'c. 387 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT'],
    causes: [
      { title: 'Socratic philosophical tradition', type: 'Movement', year: '5th century BCE' },
      { title: 'Athenian democratic culture fosters intellectual life', type: 'EventWindow', year: '5th century BCE' },
    ],
    effects: [
      { title: 'Aristotle trained → founds Lyceum', type: 'Person', year: '335 BCE' },
      { title: 'Neoplatonism develops from Academic tradition', type: 'Movement', year: '3rd century CE' },
      { title: 'Model for Western higher education', type: 'Idea', year: '387 BCE–529 CE' },
    ],
    relationships: [
      { sourceSlug: 'platonic_academy', sourceName: 'Platonic Academy', verb: 'OCCURS_IN', targetSlug: 'greece', targetName: 'Greece', context: 'Located in Athens' },
    ],
    places: [
      { name: 'Athens', role: 'Location, near the sacred grove of Academus' },
    ],
    texts: [
      { title: 'Republic (Plato)', type: 'Philosophical dialogue' },
      { title: 'Timaeus (Plato)', type: 'Philosophical dialogue' },
    ],
  },

  {
    slug: 'nalanda_university',
    name: 'Nalanda University',
    label: 'Institution',
    callNumber: '380.05-nalanda-university',
    subjectHeadings: ['Institutions — Educational — India — Classical/Medieval'],
    subjects: ['Education', 'Buddhism', 'India', 'Monastery', 'Translation', 'Library'],
    summary: 'One of the world\'s oldest residential universities, active from the 5th century to 1193 CE in Bihar, India. At its height, Nalanda housed 10,000 students and 2,000 teachers studying Buddhist philosophy, logic, grammar, medicine, and astronomy. The great library (Dharmagañja) reportedly burned for months when Bakhtiyar Khilji\'s forces destroyed the university in 1193.',
    founded: 'c. 427 CE',
    period: '427 CE – 1193 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'South Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'TEXTUAL_TRANSMISSION', 'COMPARATIVE_RELIGION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Gupta Empire patronage of Buddhist learning', type: 'Institution', year: '5th century' },
      { title: 'Silk Road intellectual exchange', type: 'Movement', year: '1st millennium CE' },
    ],
    effects: [
      { title: 'Trained Xuanzang, Yijing, and generations of scholars', type: 'Person', year: '7th century' },
      { title: 'Buddhist texts transmitted across Asia', type: 'Movement', year: '5th–12th century' },
      { title: 'Destruction ends institutional Buddhism in India', type: 'EventWindow', year: '1193' },
    ],
    relationships: [
      { sourceSlug: 'nalanda_university', sourceName: 'Nalanda University', verb: 'OCCURS_IN', targetSlug: 'india', targetName: 'India', context: 'Bihar, India' },
      { sourceSlug: 'nalanda_university', sourceName: 'Nalanda University', verb: 'INFLUENCES', targetSlug: 'xuanzang', targetName: 'Xuanzang', context: 'Studied here for 5 years' },
    ],
    places: [
      { name: 'Nalanda, Bihar', role: 'Location' },
      { name: 'Rajgir', role: 'Nearby Buddhist pilgrimage site' },
    ],
    texts: [
      { title: 'Great Tang Records on the Western Regions (Xuanzang)', type: 'Travel account describing Nalanda' },
    ],
  },

  {
    slug: 'university_of_oxford',
    name: 'University of Oxford',
    label: 'Institution',
    callNumber: '380.06-university-of-oxford',
    subjectHeadings: ['Institutions — Educational — England — Medieval'],
    subjects: ['Education', 'University', 'England', 'Theology', 'Law', 'Science'],
    summary: 'The oldest university in the English-speaking world, with teaching documented as early as 1096. Oxford became a major center of learning after Henry II banned English students from attending the University of Paris in 1167. Its colleges, libraries (especially the Bodleian), and scholars — Roger Bacon, John Wycliffe, Thomas More — have shaped Western thought for over nine centuries.',
    founded: 'c. 1096',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION', 'INNOVATION_AND_TECHNOLOGY'],
    causes: [
      { title: 'Henry II bans English students from Paris', type: 'EventWindow', year: '1167' },
      { title: 'Cathedral school tradition in England', type: 'Movement', year: '11th century' },
    ],
    effects: [
      { title: 'Roger Bacon\'s scientific method at Oxford', type: 'Person', year: '13th century' },
      { title: 'Wycliffe\'s Bible translation movement', type: 'Person', year: '14th century' },
      { title: 'Model for Cambridge, Harvard, and global research universities', type: 'Institution', year: '13th century onward' },
    ],
    relationships: [
      { sourceSlug: 'university_of_oxford', sourceName: 'University of Oxford', verb: 'OCCURS_IN', targetSlug: 'united-kingdom', targetName: 'England', context: 'Oxfordshire, England' },
    ],
    places: [
      { name: 'Oxford, England', role: 'Location' },
    ],
    texts: [
      { title: 'Opus Majus (Roger Bacon)', type: 'Scientific treatise, written at Oxford' },
    ],
  },

  {
    slug: 'university_of_paris',
    name: 'University of Paris (Sorbonne)',
    label: 'Institution',
    callNumber: '380.07-university-of-paris',
    subjectHeadings: ['Institutions — Educational — France — Medieval'],
    subjects: ['Education', 'University', 'France', 'Theology', 'Scholasticism', 'Canon Law'],
    summary: 'Founded c. 1150, the University of Paris was the preeminent center of theological and philosophical learning in medieval Europe. Thomas Aquinas, Bonaventure, and Albertus Magnus taught there; the Sorbonne college (1257) became synonymous with the university itself. Its theology faculty wielded such influence it was called the "second magisterium" of the Catholic Church.',
    founded: 'c. 1150',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'COMPARATIVE_RELIGION', 'TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Cathedral school of Notre-Dame grows into studium generale', type: 'Institution', year: '12th century' },
      { title: 'Papal recognition grants autonomy', type: 'EventWindow', year: '1215' },
    ],
    effects: [
      { title: 'Scholasticism systematized (Aquinas, Bonaventure)', type: 'Movement', year: '13th century' },
      { title: 'Model for European university structure (nations, faculties)', type: 'Idea', year: '12th–13th century' },
    ],
    relationships: [
      { sourceSlug: 'university_of_paris', sourceName: 'University of Paris', verb: 'OCCURS_IN', targetSlug: 'france', targetName: 'France', context: 'Paris, France' },
    ],
    places: [
      { name: 'Paris, Latin Quarter', role: 'Location' },
    ],
    texts: [
      { title: 'Summa Theologica (Aquinas)', type: 'Major work composed by Paris professor' },
    ],
  },

  {
    slug: 'al_azhar_university',
    name: 'Al-Azhar University',
    label: 'Institution',
    callNumber: '380.08-al-azhar-university',
    subjectHeadings: ['Institutions — Educational — Egypt — Medieval'],
    subjects: ['Education', 'Islam', 'Egypt', 'Theology', 'Jurisprudence', 'Arabic'],
    summary: 'Founded in 970 CE in Cairo by the Fatimid Caliphate, Al-Azhar is one of the oldest continuously operating universities in the world. Initially a center of Ismaili Shia learning, it became the foremost Sunni theological institution under Saladin. For over a millennium, it has been the supreme authority on Islamic jurisprudence and Arabic linguistics.',
    founded: '970 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'North Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'COMPARATIVE_RELIGION', 'TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Fatimid Caliphate establishes Cairo as capital', type: 'EventWindow', year: '969 CE' },
      { title: 'Desire to promote Ismaili Shia scholarship', type: 'Movement', year: '10th century' },
    ],
    effects: [
      { title: 'Becomes preeminent Sunni institution under Saladin', type: 'EventWindow', year: '1171' },
      { title: 'Supreme authority on Islamic jurisprudence for over 1,000 years', type: 'Institution', year: '970 CE–present' },
    ],
    relationships: [
      { sourceSlug: 'al_azhar_university', sourceName: 'Al-Azhar University', verb: 'OCCURS_IN', targetSlug: 'egypt', targetName: 'Egypt', context: 'Cairo, Egypt' },
    ],
    places: [
      { name: 'Cairo', role: 'Location — within Al-Azhar Mosque' },
    ],
    texts: [],
  },

  {
    slug: 'imperial_academy_china',
    name: 'Imperial Academy (Guozijian)',
    label: 'Institution',
    callNumber: '380.09-imperial-academy-china',
    subjectHeadings: ['Institutions — Educational — China — Classical/Medieval'],
    subjects: ['Education', 'Confucianism', 'China', 'Civil Service', 'Imperial Examination'],
    summary: 'The Guozijian (Imperial Academy), first established during the Sui Dynasty (c. 605 CE) and formalized under the Tang, was China\'s premier institution for training civil service officials through the keju (imperial examination) system. For over 1,300 years, this meritocratic system educated and selected administrators who governed a quarter of the world\'s population.',
    founded: 'c. 605 CE (Sui refounding; roots to 124 BCE Taixue)',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'East Asia',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['LEGAL_INTERPRETATION', 'DOCTRINE_DEVELOPMENT', 'CAUSE_AND_EFFECT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Confucian tradition of scholar-officials', type: 'Movement', year: '6th century BCE onward' },
      { title: 'Sui Dynasty reunifies China, centralizes education', type: 'EventWindow', year: '581–618 CE' },
    ],
    effects: [
      { title: 'Imperial examination system lasts 1,300 years', type: 'Institution', year: '605–1905' },
      { title: 'Meritocratic model influences East Asian governance', type: 'Idea', year: 'throughout' },
    ],
    relationships: [
      { sourceSlug: 'imperial_academy_china', sourceName: 'Imperial Academy (Guozijian)', verb: 'OCCURS_IN', targetSlug: 'china', targetName: 'China', context: 'Chang\'an, then Beijing' },
    ],
    places: [
      { name: 'Chang\'an (Xi\'an)', role: 'Tang Dynasty location' },
      { name: 'Beijing', role: 'Ming/Qing location — preserved today' },
    ],
    texts: [
      { title: 'Analects (Confucius)', type: 'Core curriculum text' },
    ],
  },

  {
    slug: 'university_of_salamanca',
    name: 'University of Salamanca',
    label: 'Institution',
    callNumber: '380.10-university-of-salamanca',
    subjectHeadings: ['Institutions — Educational — Spain — Medieval'],
    subjects: ['Education', 'University', 'Spain', 'Law', 'Theology', 'International Law'],
    summary: 'Founded in 1218 by Alfonso IX of León, Salamanca is the oldest university in the Hispanic world and one of the four oldest in Europe. The School of Salamanca (16th century) pioneered international law, developed early economic theory (just price, supply-and-demand), and debated the morality of Spanish colonization. Francisco de Vitoria\'s work there is the foundation of modern international law.',
    founded: '1218',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['LEGAL_INTERPRETATION', 'DOCTRINE_DEVELOPMENT', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Reconquista creates demand for educated administrators', type: 'Movement', year: '13th century' },
      { title: 'Alfonso IX royal charter', type: 'EventWindow', year: '1218' },
    ],
    effects: [
      { title: 'School of Salamanca pioneers international law', type: 'Movement', year: '16th century' },
      { title: 'Columbus\'s proposal evaluated by Salamanca scholars', type: 'EventWindow', year: '1486' },
      { title: 'Early economic theory (supply/demand, just price)', type: 'Idea', year: '16th century' },
    ],
    relationships: [
      { sourceSlug: 'university_of_salamanca', sourceName: 'University of Salamanca', verb: 'OCCURS_IN', targetSlug: 'spain', targetName: 'Spain', context: 'Salamanca, Spain' },
    ],
    places: [
      { name: 'Salamanca', role: 'Location' },
    ],
    texts: [
      { title: 'De Indis (Francisco de Vitoria)', type: 'Legal treatise on rights of indigenous peoples' },
    ],
  },

  {
    slug: 'timbuktu_university',
    name: 'University of Timbuktu (Sankore)',
    label: 'Institution',
    callNumber: '380.11-timbuktu-university',
    subjectHeadings: ['Institutions — Educational — Mali — Medieval'],
    subjects: ['Education', 'Islam', 'Mali', 'Sahara', 'Manuscripts', 'West Africa'],
    summary: 'The Sankore Madrasah in Timbuktu, reaching its height under the Songhai Empire (15th–16th century), was West Africa\'s greatest center of Islamic scholarship. With an estimated 25,000 students and collections exceeding 700,000 manuscripts, it taught theology, astronomy, mathematics, law, and medicine. The Timbuktu manuscripts remain one of the world\'s most important yet understudied archives.',
    founded: '14th century (expanded 15th–16th century)',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION', 'ECONOMIC_SYSTEMS'],
    causes: [
      { title: 'Trans-Saharan trade brings wealth and scholars to Timbuktu', type: 'Movement', year: '13th–14th century' },
      { title: 'Mansa Musa\'s hajj elevates Mali\'s international prestige', type: 'EventWindow', year: '1324' },
    ],
    effects: [
      { title: '700,000+ Timbuktu manuscripts survive', type: 'Text', year: '14th–17th century' },
      { title: 'West African Islamic intellectual tradition established', type: 'Movement', year: '15th century' },
    ],
    relationships: [
      { sourceSlug: 'timbuktu_university', sourceName: 'University of Timbuktu', verb: 'OCCURS_IN', targetSlug: 'mali', targetName: 'Mali', context: 'Timbuktu, Mali' },
    ],
    places: [
      { name: 'Timbuktu', role: 'Location' },
    ],
    texts: [],
  },

  {
    slug: 'humboldt_university_berlin',
    name: 'Humboldt University of Berlin',
    label: 'Institution',
    callNumber: '380.12-humboldt-university-berlin',
    subjectHeadings: ['Institutions — Educational — Germany — Modern'],
    subjects: ['Education', 'University', 'Germany', 'Research', 'Reform', 'Enlightenment'],
    summary: 'Founded in 1810 by Wilhelm von Humboldt, the University of Berlin pioneered the modern research university model: integrating teaching with original research and giving academic freedom to faculty and students. This Humboldtian model was adopted by Johns Hopkins, Harvard, and virtually every major research university worldwide, making it arguably the most influential institutional innovation in higher education since Bologna.',
    founded: '1810',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    frameworks: ['INNOVATION_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION', 'CAUSE_AND_EFFECT', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Napoleonic defeat shocks Prussia into reform', type: 'EventWindow', year: '1806' },
      { title: 'Enlightenment ideals of Bildung (self-cultivation)', type: 'Idea', year: '18th century' },
    ],
    effects: [
      { title: 'Modern research university model adopted globally', type: 'Idea', year: '19th–20th century' },
      { title: '29 Nobel laureates among alumni and faculty', type: 'Institution', year: '20th century' },
    ],
    relationships: [
      { sourceSlug: 'humboldt_university_berlin', sourceName: 'Humboldt University of Berlin', verb: 'OCCURS_IN', targetSlug: 'germany', targetName: 'Germany', context: 'Berlin, Germany' },
    ],
    places: [
      { name: 'Berlin', role: 'Location' },
    ],
    texts: [
      { title: 'On the Internal and External Organization of the Higher Scientific Institutions (W. von Humboldt)', type: 'Educational manifesto' },
    ],
  },
]
