/**
 * Entity Data Store — interconnected historical actors
 *
 * Every relationship uses explicit source → VERB → target direction
 * following the v4 active-voice canonical grammar.
 *
 * Call numbers follow Dewey-style: Class.Division.Slug
 *   0xx = Ideas (Core), 1xx = Ideas (Other), 2xx = People,
 *   3xx = Institutions, 4xx = Places, 5xx = Events,
 *   6xx = Movements, 7xx = Artifacts & Texts,
 *   8xx = Evidence, 9xx = Timeframes
 */

export interface EntityRelationship {
  sourceSlug: string
  sourceName: string
  verb: string
  targetSlug: string
  targetName: string
  context?: string
}

export interface EntityCause {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityEffect {
  title: string
  type: string
  year: string
  slug?: string
}

export interface EntityPlace {
  name: string
  role: string
  slug?: string
}

export interface EntityText {
  title: string
  type: string
  year?: string
  slug?: string
}

export type NodeLabel = 'Person' | 'Idea' | 'Institution' | 'Place' | 'EventWindow' | 'Movement' | 'Text' | 'Evidence'

export interface Entity {
  slug: string
  name: string
  label: NodeLabel
  callNumber: string
  subjectHeadings: string[]
  subjects: string[]
  summary: string
  born?: string
  died?: string
  founded?: string
  period?: string
  startDate?: string
  endDate?: string
  era: string
  eraSlug: string
  region: string
  continent: string
  status: string
  causes: EntityCause[]
  effects: EntityEffect[]
  relationships: EntityRelationship[]
  places: EntityPlace[]
  texts: EntityText[]
}

/* ── Entity Records ──────────────────────────────────────────── */

const ENTITIES: Record<string, Entity> = {
  henry_viii: {
    slug: 'henry_viii',
    name: 'Henry VIII',
    label: 'Person',
    callNumber: '220.01-henry-viii',
    subjectHeadings: ['People — Political Leaders — England — Early Modern'],
    subjects: ['Tudor Dynasty', 'English Reformation', 'Monarchy', 'Church of England'],
    summary:
      'King of England from 1509 to 1547. Henry VIII broke with the authority of the Pope and the Roman Catholic Church, establishing the Church of England and initiating the English Reformation. His six marriages and their political consequences reshaped European diplomacy.',
    born: '28 June 1491, Greenwich Palace',
    died: '28 January 1547, Palace of Whitehall',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Papal Authority over English Crown', type: 'Idea', year: 'c. 1200–1530' },
      { title: 'Desire for Male Heir', type: 'Event', year: '1525–1533' },
      { title: "Catherine of Aragon's Marriage Annulment Denied", type: 'Event', year: '1527–1533' },
      { title: 'Rise of Protestant Theology in Europe', type: 'Idea', year: 'c. 1517' },
    ],
    effects: [
      { title: 'Act of Supremacy', type: 'Text', year: '1534', slug: 'act_of_supremacy' },
      { title: 'Dissolution of the Monasteries', type: 'Event', year: '1536–1541' },
      { title: 'Church of England Established', type: 'Institution', year: '1534', slug: 'church_of_england' },
      { title: 'English Reformation', type: 'Movement', year: '1534–1603', slug: 'english_reformation' },
    ],
    relationships: [
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'ADVISES', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Chief Minister, architect of the Break with Rome' },
      { sourceSlug: 'thomas_more', sourceName: 'Thomas More', verb: 'OPPOSES', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Refused to acknowledge Henry as Supreme Head of the Church' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'MARRIES', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Second wife, 1533–1536' },
      { sourceSlug: 'thomas_cranmer', sourceName: 'Thomas Cranmer', verb: 'SUPPORTS', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Annulled marriage to Catherine, crowned Anne Boleyn' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'EXECUTES', targetSlug: 'thomas_more', targetName: 'Thomas More', context: 'Beheaded 6 July 1535 for treason' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'APPOINTS', targetSlug: 'thomas_cromwell', targetName: 'Thomas Cromwell', context: 'Made Chief Minister and Vicegerent in Spirituals' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'EXECUTES', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Beheaded 19 May 1536 at the Tower of London' },
    ],
    places: [
      { name: 'Greenwich Palace', role: 'Birthplace' },
      { name: 'Hampton Court Palace', role: 'Primary Residence' },
      { name: 'Tower of London', role: 'Imprisonment / Execution site' },
      { name: 'Westminster', role: 'Parliamentary seat' },
    ],
    texts: [
      { title: 'Act of Supremacy (1534)', type: 'Legal document', slug: 'act_of_supremacy' },
      { title: 'Assertio Septem Sacramentorum (1521)', type: 'Theological treatise' },
      { title: 'Six Articles (1539)', type: 'Doctrinal code' },
    ],
  },

  thomas_cromwell: {
    slug: 'thomas_cromwell',
    name: 'Thomas Cromwell',
    label: 'Person',
    callNumber: '220.02-thomas-cromwell',
    subjectHeadings: ['People — Political Leaders — England — Early Modern'],
    subjects: ['Tudor Administration', 'English Reformation', 'Privy Council', 'Dissolution of Monasteries'],
    summary:
      'Thomas Cromwell, 1st Earl of Essex, served as Henry VIII\'s chief minister from 1532 to 1540. He was the principal architect of the English Reformation, engineering the Break with Rome, the Dissolution of the Monasteries, and the administrative revolution that centralized English government.',
    born: 'c. 1485, Putney, London',
    died: '28 July 1540, Tower Hill (executed)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: "Henry VIII's Need for Annulment", type: 'Event', year: '1527–1533' },
      { title: 'Rise of Humanism and Legal Reform', type: 'Idea', year: 'c. 1500' },
      { title: 'Wolsey\'s Fall from Power', type: 'Event', year: '1529' },
    ],
    effects: [
      { title: 'Break with Rome Enacted', type: 'Event', year: '1534' },
      { title: 'Dissolution of the Monasteries', type: 'Event', year: '1536–1541' },
      { title: 'Administrative Revolution in England', type: 'Movement', year: '1530s' },
      { title: 'Valor Ecclesiasticus – Church Wealth Survey', type: 'Text', year: '1535' },
    ],
    relationships: [
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'ADVISES', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Chief Minister, architect of the Break with Rome' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'OPPOSES', targetSlug: 'thomas_more', targetName: 'Thomas More', context: 'Political rivals with opposing views on religious reform' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'COLLABORATES_WITH', targetSlug: 'thomas_cranmer', targetName: 'Thomas Cranmer', context: 'Co-architects of the English Reformation' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'APPOINTS', targetSlug: 'thomas_cromwell', targetName: 'Thomas Cromwell', context: 'Made Chief Minister and Vicegerent in Spirituals' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'EXECUTES', targetSlug: 'thomas_cromwell', targetName: 'Thomas Cromwell', context: 'Executed 28 July 1540 after fall from favour' },
    ],
    places: [
      { name: 'Putney, London', role: 'Birthplace' },
      { name: 'Austin Friars', role: 'London residence' },
      { name: 'Tower of London', role: 'Imprisonment and execution' },
      { name: 'Westminster', role: 'Seat of government' },
    ],
    texts: [
      { title: 'Act of Supremacy (1534)', type: 'Legal document', slug: 'act_of_supremacy' },
      { title: 'Act of Succession (1534)', type: 'Legal document' },
      { title: 'Valor Ecclesiasticus (1535)', type: 'Survey / Census' },
    ],
  },

  thomas_more: {
    slug: 'thomas_more',
    name: 'Thomas More',
    label: 'Person',
    callNumber: '210.01-thomas-more',
    subjectHeadings: ['People — Philosophers & Thinkers — England — Early Modern'],
    subjects: ['Humanism', 'Catholic Resistance', 'Lord Chancellor', 'Utopia'],
    summary:
      'Sir Thomas More was an English lawyer, philosopher, statesman, and author of Utopia (1516). As Lord Chancellor under Henry VIII, he fiercely opposed the King\'s break with Rome and refused to acknowledge the Act of Supremacy. He was executed for treason in 1535 and later canonized by the Catholic Church.',
    born: '7 February 1478, London',
    died: '6 July 1535, Tower Hill (executed)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Rise of Renaissance Humanism', type: 'Idea', year: 'c. 1450–1520' },
      { title: 'Erasmian Reform Movement', type: 'Movement', year: 'c. 1500' },
      { title: 'Tradition of English Common Law', type: 'Idea', year: 'Medieval' },
    ],
    effects: [
      { title: 'Utopia Published', type: 'Text', year: '1516' },
      { title: 'Catholic Martyrdom Tradition Strengthened', type: 'Movement', year: '1535+' },
      { title: 'Canonized by Catholic Church', type: 'Event', year: '1935' },
    ],
    relationships: [
      { sourceSlug: 'thomas_more', sourceName: 'Thomas More', verb: 'OPPOSES', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Refused to acknowledge Act of Supremacy' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'EXECUTES', targetSlug: 'thomas_more', targetName: 'Thomas More', context: 'Beheaded 6 July 1535 for treason' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'OPPOSES', targetSlug: 'thomas_more', targetName: 'Thomas More', context: 'Political rivals with opposing views on religious reform' },
      { sourceSlug: 'thomas_more', sourceName: 'Thomas More', verb: 'INFLUENCES', targetSlug: 'erasmus', targetName: 'Erasmus of Rotterdam', context: 'Close friends and intellectual collaborators' },
    ],
    places: [
      { name: 'London', role: 'Birthplace and residence' },
      { name: 'Chelsea, London', role: 'Family home' },
      { name: 'Tower of London', role: 'Imprisonment and execution' },
      { name: 'Westminster', role: 'Seat of government' },
    ],
    texts: [
      { title: 'Utopia (1516)', type: 'Political philosophy' },
      { title: 'Dialogue Concerning Heresies (1529)', type: 'Polemical treatise' },
      { title: 'A Dialogue of Comfort Against Tribulation (1534)', type: 'Devotional work' },
    ],
  },

  anne_boleyn: {
    slug: 'anne_boleyn',
    name: 'Anne Boleyn',
    label: 'Person',
    callNumber: '220.03-anne-boleyn',
    subjectHeadings: ['People — Political Leaders — England — Early Modern'],
    subjects: ['Tudor Dynasty', 'Queen Consort', 'English Reformation', 'Boleyn Faction'],
    summary:
      'Anne Boleyn was Queen of England from 1533 to 1536 as the second wife of Henry VIII. Her marriage to Henry precipitated the Break with Rome and the English Reformation. She was the mother of Elizabeth I. Accused of adultery and treason, she was beheaded at the Tower of London.',
    born: 'c. 1501–1507, Blickling Hall, Norfolk',
    died: '19 May 1536, Tower of London (executed)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: "Henry VIII's Desire for Male Heir", type: 'Event', year: '1525–1533' },
      { title: 'Boleyn Family Ambition at Court', type: 'Event', year: '1520s' },
      { title: 'Exposure to French Court Culture', type: 'Event', year: '1514–1521' },
    ],
    effects: [
      { title: 'Break with Rome Catalyzed', type: 'Event', year: '1534' },
      { title: 'Birth of Elizabeth I', type: 'Event', year: '7 September 1533' },
      { title: "Anne's Execution as Political Precedent", type: 'Event', year: '1536' },
    ],
    relationships: [
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'MARRIES', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Second wife, 1533–1536' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'EXECUTES', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Beheaded 19 May 1536 at the Tower of London' },
      { sourceSlug: 'thomas_cranmer', sourceName: 'Thomas Cranmer', verb: 'SUPPORTS', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Officiated secret marriage and coronation' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'OPPOSES', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Orchestrated her downfall in 1536' },
    ],
    places: [
      { name: 'Blickling Hall, Norfolk', role: 'Probable birthplace' },
      { name: 'Hever Castle, Kent', role: 'Family seat' },
      { name: 'Greenwich Palace', role: 'Royal residence' },
      { name: 'Tower of London', role: 'Imprisonment and execution' },
    ],
    texts: [
      { title: "Anne Boleyn's Letter to Henry VIII from the Tower", type: 'Personal correspondence' },
    ],
  },

  thomas_cranmer: {
    slug: 'thomas_cranmer',
    name: 'Thomas Cranmer',
    label: 'Person',
    callNumber: '250.01-thomas-cranmer',
    subjectHeadings: ['People — Religious Figures — England — Early Modern'],
    subjects: ['Church of England', 'English Reformation', 'Archbishop of Canterbury', 'Book of Common Prayer'],
    summary:
      'Thomas Cranmer served as the first Protestant Archbishop of Canterbury (1533–1556). He annulled Henry VIII\'s marriages, shaped the theological foundations of the Church of England, and authored the Book of Common Prayer. Burned at the stake under Mary I for heresy.',
    born: '2 July 1489, Aslockton, Nottinghamshire',
    died: '21 March 1556, Oxford (burned at the stake)',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Henry VIII\'s Need for Annulment', type: 'Event', year: '1527–1533' },
      { title: 'Spread of Lutheran Theology to England', type: 'Movement', year: '1520s' },
      { title: 'Cambridge Protestantism', type: 'Idea', year: '1520s' },
    ],
    effects: [
      { title: 'Book of Common Prayer Published', type: 'Text', year: '1549' },
      { title: 'Forty-Two Articles of Faith', type: 'Text', year: '1553' },
      { title: 'English Liturgical Reform', type: 'Movement', year: '1530s–1550s' },
    ],
    relationships: [
      { sourceSlug: 'thomas_cranmer', sourceName: 'Thomas Cranmer', verb: 'SUPPORTS', targetSlug: 'henry_viii', targetName: 'Henry VIII', context: 'Annulled marriage to Catherine, crowned Anne Boleyn' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'COLLABORATES_WITH', targetSlug: 'thomas_cranmer', targetName: 'Thomas Cranmer', context: 'Co-architects of the English Reformation' },
      { sourceSlug: 'thomas_cranmer', sourceName: 'Thomas Cranmer', verb: 'SUPPORTS', targetSlug: 'anne_boleyn', targetName: 'Anne Boleyn', context: 'Officiated secret marriage and coronation' },
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'APPOINTS', targetSlug: 'thomas_cranmer', targetName: 'Thomas Cranmer', context: 'Made Archbishop of Canterbury in 1533' },
    ],
    places: [
      { name: 'Aslockton, Nottinghamshire', role: 'Birthplace' },
      { name: 'Canterbury Cathedral', role: 'Seat as Archbishop' },
      { name: 'Lambeth Palace', role: 'Official London residence' },
      { name: 'Oxford', role: 'Place of execution' },
    ],
    texts: [
      { title: 'Book of Common Prayer (1549)', type: 'Liturgical text' },
      { title: 'Forty-Two Articles (1553)', type: 'Doctrinal statement' },
      { title: 'Cranmer\'s Recantations (1556)', type: 'Personal document' },
    ],
  },

  english_reformation: {
    slug: 'english_reformation',
    name: 'English Reformation',
    label: 'Movement',
    callNumber: '630.01-english-reformation',
    subjectHeadings: ['Movements — Religious Movements — England — Early Modern'],
    subjects: ['Protestantism', 'Church of England', 'Tudor England', 'Religious Reform'],
    summary:
      'The English Reformation (c. 1534–1603) was the process by which England broke away from the authority of the Pope and the Roman Catholic Church. Initiated by Henry VIII\'s desire for annulment and executed through parliamentary statutes, it transformed English religion, politics, and culture.',
    period: 'c. 1534–1603',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Papal Refusal to Annul Henry\'s Marriage', type: 'Event', year: '1527–1533' },
      { title: 'Rise of Protestant Theology in Continental Europe', type: 'Idea', year: 'c. 1517' },
      { title: 'Anti-Clerical Sentiment in England', type: 'Idea', year: 'c. 1500–1530' },
      { title: 'Humanist Criticism of Church Corruption', type: 'Idea', year: 'c. 1500' },
    ],
    effects: [
      { title: 'Church of England Established', type: 'Institution', year: '1534', slug: 'church_of_england' },
      { title: 'Dissolution of the Monasteries', type: 'Event', year: '1536–1541' },
      { title: 'Book of Common Prayer', type: 'Text', year: '1549' },
      { title: 'Elizabethan Religious Settlement', type: 'Event', year: '1559' },
    ],
    relationships: [
      { sourceSlug: 'henry_viii', sourceName: 'Henry VIII', verb: 'INITIATES', targetSlug: 'english_reformation', targetName: 'English Reformation', context: 'Break with Rome precipitated the movement' },
      { sourceSlug: 'thomas_cromwell', sourceName: 'Thomas Cromwell', verb: 'ARCHITECTS', targetSlug: 'english_reformation', targetName: 'English Reformation', context: 'Designed the legislative programme' },
      { sourceSlug: 'thomas_cranmer', sourceName: 'Thomas Cranmer', verb: 'SHAPES', targetSlug: 'english_reformation', targetName: 'English Reformation', context: 'Theological foundation and liturgical reform' },
      { sourceSlug: 'thomas_more', sourceName: 'Thomas More', verb: 'OPPOSES', targetSlug: 'english_reformation', targetName: 'English Reformation', context: 'Martyred for Catholic resistance' },
    ],
    places: [
      { name: 'Westminster', role: 'Legislative centre' },
      { name: 'Canterbury', role: 'Ecclesiastical centre' },
      { name: 'London', role: 'Political capital' },
    ],
    texts: [
      { title: 'Act of Supremacy (1534)', type: 'Legal document', slug: 'act_of_supremacy' },
      { title: 'Act of Succession (1534)', type: 'Legal document' },
      { title: 'Ten Articles (1536)', type: 'Doctrinal code' },
      { title: 'Book of Common Prayer (1549)', type: 'Liturgical text' },
    ],
  },

  /* ── World War I cluster ── */
  world_war_i: {
    slug: 'world_war_i',
    name: 'World War I',
    label: 'EventWindow',
    callNumber: '510.01-world-war-i',
    subjectHeadings: [
      'Events — Wars & Conflicts — Global — Early 20th Century',
      'Great War — Allied Powers vs Central Powers',
    ],
    subjects: ['Global Conflict', 'Trench Warfare', 'Allied Powers', 'Central Powers', 'Treaty of Versailles'],
    summary:
      'Global conflict centered in Europe from 1914 to 1918, triggered by the July Crisis following the assassination of Archduke Franz Ferdinand. The war involved over 30 nations, introduced industrialized warfare, and caused approximately 20 million deaths. It reshaped geopolitics, dissolved empires, and set the stage for World War II.',
    startDate: '1914-07-28',
    endDate: '1918-11-11',
    period: '1914–1918',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Militarism', type: 'Idea', year: 'c. 1870–1914', slug: 'militarism' },
      { title: 'Alliance Systems', type: 'Idea', year: 'c. 1879–1914', slug: 'alliance_systems' },
      { title: 'Nationalism', type: 'Idea', year: '19th century', slug: 'nationalism' },
      { title: 'Assassination of Archduke Franz Ferdinand', type: 'Event', year: '28 June 1914' },
      { title: 'Imperialism and Colonial Rivalry', type: 'Idea', year: 'c. 1880–1914' },
    ],
    effects: [
      { title: 'Treaty of Versailles', type: 'Text', year: '1919', slug: 'treaty_of_versailles' },
      { title: 'League of Nations Established', type: 'Institution', year: '1920', slug: 'league_of_nations' },
      { title: 'Collapse of Ottoman Empire', type: 'Event', year: '1922' },
      { title: 'Collapse of Austro-Hungarian Empire', type: 'Event', year: '1918' },
      { title: 'Russian Revolution', type: 'Event', year: '1917', slug: 'russian_revolution' },
      { title: 'Rise of Self-Determination', type: 'Idea', year: '1918+' },
    ],
    relationships: [
      { sourceSlug: 'militarism', sourceName: 'Militarism', verb: 'CAUSES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Arms race and military planning escalated tensions' },
      { sourceSlug: 'nationalism', sourceName: 'Nationalism', verb: 'CAUSES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Ethnic tensions ignited conflict across empires' },
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'RESULTS_IN', targetSlug: 'treaty_of_versailles', targetName: 'Treaty of Versailles', context: 'Peace settlement of 1919' },
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'First international peace organization' },
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'INFLUENCES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Fourteen Points and US entry in 1917' },
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'OCCURS_IN', targetSlug: 'europe_place', targetName: 'Europe', context: 'Primary theater of war' },
    ],
    places: [
      { name: 'Western Front (France/Belgium)', role: 'Primary theater' },
      { name: 'Eastern Front (Russia/Germany)', role: 'Major theater' },
      { name: 'Middle East', role: 'Ottoman theater' },
      { name: 'Africa', role: 'Colonial campaigns' },
      { name: 'Sarajevo', role: 'Assassination site' },
      { name: 'Versailles', role: 'Peace conference' },
    ],
    texts: [
      { title: 'Treaty of Versailles (1919)', type: 'International treaty', slug: 'treaty_of_versailles' },
      { title: 'Fourteen Points (1918)', type: 'Policy document' },
      { title: 'Sykes-Picot Agreement (1916)', type: 'Secret agreement' },
    ],
  },

  militarism: {
    slug: 'militarism',
    name: 'Militarism',
    label: 'Idea',
    callNumber: '010.01-militarism',
    subjectHeadings: ['Ideas — Political Systems & Governance — Military Doctrine — Modern'],
    subjects: ['Arms Race', 'Military-Industrial Complex', 'War Doctrine', 'Conscription'],
    summary:
      'The belief that a country should maintain strong armed forces and be prepared to use them aggressively to defend or promote national interests. In the late 19th and early 20th century, European powers engaged in massive arms build-ups that contributed directly to WWI.',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Franco-Prussian War Legacy', type: 'Event', year: '1870–1871' },
      { title: 'Industrial Revolution', type: 'Event', year: '19th century' },
    ],
    effects: [
      { title: 'European Arms Race', type: 'Event', year: '1890–1914' },
      { title: 'World War I', type: 'Event', year: '1914', slug: 'world_war_i' },
    ],
    relationships: [
      { sourceSlug: 'militarism', sourceName: 'Militarism', verb: 'CAUSES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Arms race and military planning escalated tensions' },
      { sourceSlug: 'militarism', sourceName: 'Militarism', verb: 'INFLUENCES', targetSlug: 'nationalism', targetName: 'Nationalism', context: 'Military strength reinforced national identity' },
    ],
    places: [
      { name: 'Germany', role: 'Major militarist state' },
      { name: 'Britain', role: 'Naval arms race' },
      { name: 'France', role: 'Revanchism post-1871' },
    ],
    texts: [
      { title: 'Schlieffen Plan', type: 'Military strategy document' },
    ],
  },

  nationalism: {
    slug: 'nationalism',
    name: 'Nationalism',
    label: 'Idea',
    callNumber: '010.02-nationalism',
    subjectHeadings: ['Ideas — Political Systems & Governance — Ideology — Modern'],
    subjects: ['National Identity', 'Self-Determination', 'Ethnic Nationalism', 'Pan-Slavism'],
    summary:
      'The political ideology that nations should govern themselves and that loyalty to the nation-state supersedes other allegiances. In the 19th and early 20th centuries, competing nationalisms in multi-ethnic empires created the powder keg that detonated in 1914.',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Global',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'French Revolution', type: 'Event', year: '1789' },
      { title: 'Romanticism', type: 'Movement', year: 'c. 1800' },
    ],
    effects: [
      { title: 'World War I', type: 'Event', year: '1914', slug: 'world_war_i' },
      { title: 'Breakup of Empires', type: 'Event', year: '1918' },
      { title: 'Self-Determination Principle', type: 'Idea', year: '1918+' },
    ],
    relationships: [
      { sourceSlug: 'nationalism', sourceName: 'Nationalism', verb: 'CAUSES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Ethnic tensions ignited conflict across empires' },
    ],
    places: [
      { name: 'Balkans', role: 'Epicenter of ethnic nationalism' },
      { name: 'Germany', role: 'Unification nationalism' },
      { name: 'Italy', role: 'Risorgimento' },
    ],
    texts: [
      { title: 'Fourteen Points (1918)', type: 'Policy document' },
    ],
  },

  treaty_of_versailles: {
    slug: 'treaty_of_versailles',
    name: 'Treaty of Versailles',
    label: 'Text',
    callNumber: '710.01-treaty-of-versailles',
    subjectHeadings: ['Artifacts & Texts — Constitutions & Charters — International — Modern'],
    subjects: ['Peace Treaty', 'War Reparations', 'League of Nations', 'German Guilt Clause'],
    summary:
      'The 1919 peace treaty that ended World War I between the Allied Powers and Germany. It imposed severe reparations, territorial losses, and military restrictions on Germany. Its perceived harshness contributed to political instability and the rise of Nazism.',
    period: 'Signed 28 June 1919',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'World War I', type: 'Event', year: '1914–1918', slug: 'world_war_i' },
      { title: 'Paris Peace Conference', type: 'Event', year: '1919' },
    ],
    effects: [
      { title: 'German Reparations', type: 'Event', year: '1919–1932' },
      { title: 'League of Nations Founded', type: 'Institution', year: '1920', slug: 'league_of_nations' },
      { title: 'Rise of Nazism', type: 'Movement', year: '1920s–1930s' },
      { title: 'World War II', type: 'Event', year: '1939', slug: 'world_war_ii' },
    ],
    relationships: [
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'RESULTS_IN', targetSlug: 'treaty_of_versailles', targetName: 'Treaty of Versailles', context: 'Peace settlement of 1919' },
      { sourceSlug: 'treaty_of_versailles', sourceName: 'Treaty of Versailles', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'Covenant embedded in the treaty' },
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'INFLUENCES', targetSlug: 'treaty_of_versailles', targetName: 'Treaty of Versailles', context: 'Fourteen Points shaped the negotiations' },
    ],
    places: [
      { name: 'Versailles, France', role: 'Signing location' },
      { name: 'Paris', role: 'Peace conference' },
    ],
    texts: [],
  },

  league_of_nations: {
    slug: 'league_of_nations',
    name: 'League of Nations',
    label: 'Institution',
    callNumber: '370.01-league-of-nations',
    subjectHeadings: ['Institutions — International Organizations — Global — Modern'],
    subjects: ['International Cooperation', 'Collective Security', 'Mandates', 'Disarmament'],
    summary:
      'The first worldwide intergovernmental organization, established in 1920 as part of the Treaty of Versailles. Its mission was to maintain world peace through collective security, disarmament, and dispute resolution. It ultimately failed to prevent World War II and was dissolved in 1946, replaced by the United Nations.',
    founded: '10 January 1920',
    period: '1920–1946',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Global',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'World War I', type: 'Event', year: '1914–1918', slug: 'world_war_i' },
      { title: "Woodrow Wilson's Fourteen Points", type: 'Idea', year: '1918' },
    ],
    effects: [
      { title: 'Mandate System', type: 'Institution', year: '1920s' },
      { title: 'International Labour Organisation', type: 'Institution', year: '1919' },
      { title: 'United Nations (successor)', type: 'Institution', year: '1945' },
    ],
    relationships: [
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'First international peace organization' },
      { sourceSlug: 'treaty_of_versailles', sourceName: 'Treaty of Versailles', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'Covenant embedded in the treaty' },
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'Principal architect' },
    ],
    places: [
      { name: 'Geneva, Switzerland', role: 'Headquarters' },
    ],
    texts: [
      { title: 'Covenant of the League of Nations', type: 'International charter' },
    ],
  },

  woodrow_wilson: {
    slug: 'woodrow_wilson',
    name: 'Woodrow Wilson',
    label: 'Person',
    callNumber: '220.04-woodrow-wilson',
    subjectHeadings: ['People — Political Leaders — United States — Modern'],
    subjects: ['US President', 'Fourteen Points', 'League of Nations', 'Progressive Era'],
    summary:
      'The 28th President of the United States (1913–1921). Wilson led the US entry into World War I in 1917 and proposed the Fourteen Points as a basis for peace. He was the principal architect of the League of Nations, though the US Senate ultimately refused to join.',
    born: '28 December 1856, Staunton, Virginia',
    died: '3 February 1924, Washington, D.C.',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'North America',
    continent: 'Americas',
    status: 'Published',
    causes: [
      { title: 'Progressive Movement in America', type: 'Movement', year: 'c. 1890–1920' },
      { title: 'German Unrestricted Submarine Warfare', type: 'Event', year: '1917' },
      { title: 'Zimmermann Telegram', type: 'Event', year: '1917' },
    ],
    effects: [
      { title: 'US Entry into World War I', type: 'Event', year: '1917' },
      { title: 'Fourteen Points', type: 'Text', year: '1918' },
      { title: 'League of Nations', type: 'Institution', year: '1920', slug: 'league_of_nations' },
    ],
    relationships: [
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'INFLUENCES', targetSlug: 'world_war_i', targetName: 'World War I', context: 'Fourteen Points and US entry in 1917' },
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'ESTABLISHES', targetSlug: 'league_of_nations', targetName: 'League of Nations', context: 'Principal architect' },
      { sourceSlug: 'woodrow_wilson', sourceName: 'Woodrow Wilson', verb: 'INFLUENCES', targetSlug: 'treaty_of_versailles', targetName: 'Treaty of Versailles', context: 'Fourteen Points shaped the negotiations' },
    ],
    places: [
      { name: 'Washington, D.C.', role: 'White House' },
      { name: 'Paris', role: 'Peace conference 1919' },
      { name: 'Versailles', role: 'Treaty signing' },
    ],
    texts: [
      { title: 'Fourteen Points (1918)', type: 'Policy speech' },
      { title: 'War Message to Congress (1917)', type: 'Presidential address' },
    ],
  },

  world_war_ii: {
    slug: 'world_war_ii',
    name: 'World War II',
    label: 'EventWindow',
    callNumber: '510.02-world-war-ii',
    subjectHeadings: ['Events — Wars & Conflicts — Global — Modern'],
    subjects: ['Global Conflict', 'Holocaust', 'Allied Powers', 'Axis Powers', 'Nuclear Weapons'],
    summary:
      'The deadliest conflict in human history (1939–1945), involving over 30 countries and resulting in 70–85 million deaths. Rooted in the aftermath of WWI and the rise of fascism, it ended with the atomic bombings of Hiroshima and Nagasaki and the establishment of the United Nations.',
    startDate: '1939-09-01',
    endDate: '1945-09-02',
    period: '1939–1945',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Global',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Treaty of Versailles', type: 'Text', year: '1919', slug: 'treaty_of_versailles' },
      { title: 'Rise of Nazism', type: 'Movement', year: '1920s–1930s' },
      { title: 'Failure of League of Nations', type: 'Event', year: '1930s', slug: 'league_of_nations' },
      { title: 'Great Depression', type: 'Event', year: '1929–1939' },
    ],
    effects: [
      { title: 'United Nations Established', type: 'Institution', year: '1945' },
      { title: 'Cold War', type: 'Event', year: '1947–1991' },
      { title: 'Decolonization Movements', type: 'Movement', year: '1945+' },
      { title: 'Universal Declaration of Human Rights', type: 'Text', year: '1948' },
    ],
    relationships: [
      { sourceSlug: 'treaty_of_versailles', sourceName: 'Treaty of Versailles', verb: 'CAUSES', targetSlug: 'world_war_ii', targetName: 'World War II', context: 'Punitive terms fueled German resentment' },
      { sourceSlug: 'world_war_i', sourceName: 'World War I', verb: 'LEADS_TO', targetSlug: 'world_war_ii', targetName: 'World War II', context: 'Unresolved tensions and failed peace' },
    ],
    places: [
      { name: 'Europe', role: 'European theater' },
      { name: 'Pacific', role: 'Pacific theater' },
      { name: 'North Africa', role: 'North African campaign' },
    ],
    texts: [
      { title: 'UN Charter (1945)', type: 'International treaty' },
      { title: 'Geneva Conventions (1949)', type: 'International law' },
    ],
  },

  franco_prussian_war: {
    slug: 'franco_prussian_war',
    name: 'Franco-Prussian War',
    label: 'EventWindow',
    callNumber: '510.00-franco-prussian-war',
    subjectHeadings: ['Events — Wars & Conflicts — Europe — Modern'],
    subjects: ['German Unification', 'French Defeat', 'Alsace-Lorraine', 'Revanchism'],
    summary:
      'War between France and Prussia (1870–1871) that resulted in the unification of Germany under Prussian leadership, the fall of Napoleon III, and the loss of Alsace-Lorraine by France. The humiliating defeat planted seeds of French revanchism that contributed to WWI.',
    startDate: '1870-07-19',
    endDate: '1871-05-10',
    period: '1870–1871',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Ems Dispatch', type: 'Event', year: '1870' },
      { title: 'Prussian Ambition for German Unification', type: 'Idea', year: '1860s' },
    ],
    effects: [
      { title: 'German Empire Proclaimed', type: 'Event', year: '1871' },
      { title: 'French Revanchism', type: 'Idea', year: '1871–1914' },
      { title: 'Militarism', type: 'Idea', year: '1870s+', slug: 'militarism' },
    ],
    relationships: [
      { sourceSlug: 'franco_prussian_war', sourceName: 'Franco-Prussian War', verb: 'CAUSES', targetSlug: 'militarism', targetName: 'Militarism', context: 'Prussian victory spurred arms race' },
    ],
    places: [
      { name: 'Sedan, France', role: 'Decisive battle' },
      { name: 'Paris', role: 'Siege of Paris' },
      { name: 'Versailles', role: 'German Empire proclaimed' },
    ],
    texts: [
      { title: 'Treaty of Frankfurt (1871)', type: 'Peace treaty' },
    ],
  },

  spanish_civil_war: {
    slug: 'spanish_civil_war',
    name: 'Spanish Civil War',
    label: 'EventWindow',
    callNumber: '510.03-spanish-civil-war',
    subjectHeadings: ['Events — Wars & Conflicts — Spain — Modern'],
    subjects: ['Fascism', 'Republic', 'International Brigades', 'Franco'],
    summary:
      'Civil war in Spain (1936–1939) between the Republican government and Nationalist rebels led by Francisco Franco. It served as a testing ground for WWII-era weapons and ideologies, with Nazi Germany and Fascist Italy supporting the Nationalists.',
    startDate: '1936-07-17',
    endDate: '1939-04-01',
    period: '1936–1939',
    era: 'Modern',
    eraSlug: 'modern',
    region: 'Southern Europe',
    continent: 'Europe',
    status: 'Published',
    causes: [
      { title: 'Political Polarization in Spain', type: 'Event', year: '1930s' },
      { title: 'Rise of Fascism in Europe', type: 'Movement', year: '1920s–1930s' },
    ],
    effects: [
      { title: 'Franco Dictatorship', type: 'Event', year: '1939–1975' },
      { title: 'Prelude to WWII', type: 'Event', year: '1939', slug: 'world_war_ii' },
    ],
    relationships: [],
    places: [
      { name: 'Madrid', role: 'Siege of Madrid' },
      { name: 'Guernica', role: 'Bombing site' },
    ],
    texts: [
      { title: 'Guernica by Picasso (1937)', type: 'Artwork response' },
    ],
  },
}

/* ── Accessors ── */

export function getEntity(slug: string): Entity | undefined {
  return ENTITIES[slug]
}

export function getAllEntities(): Entity[] {
  return Object.values(ENTITIES)
}

/** Get entities by call number prefix (shelf browse) */
export function getEntitiesByShelf(prefix: string): Entity[] {
  return Object.values(ENTITIES)
    .filter(e => e.callNumber.startsWith(prefix))
    .sort((a, b) => a.callNumber.localeCompare(b.callNumber))
}

/** Get shelf neighbors (±N sorted by call number within same division) */
export function getShelfNeighbors(callNumber: string, range = 5): Entity[] {
  const dotIndex = callNumber.indexOf('.')
  if (dotIndex === -1) return []
  const prefix = callNumber.substring(0, dotIndex + 1) // e.g. "510."
  const shelf = getEntitiesByShelf(prefix)
  const idx = shelf.findIndex(e => e.callNumber === callNumber)
  if (idx === -1) return shelf.slice(0, range * 2)
  const start = Math.max(0, idx - range)
  const end = Math.min(shelf.length, idx + range + 1)
  return shelf.slice(start, end)
}

/** Get entity by call number */
export function getEntityByCallNumber(cn: string): Entity | undefined {
  return Object.values(ENTITIES).find(e => e.callNumber === cn)
}

/** Get all distinct division prefixes with entity counts */
export function getShelfSummary(): { prefix: string; heading: string; count: number }[] {
  const map = new Map<string, number>()
  for (const e of Object.values(ENTITIES)) {
    const dotIdx = e.callNumber.indexOf('.')
    if (dotIdx >= 0) {
      const prefix = e.callNumber.substring(0, dotIdx)
      map.set(prefix, (map.get(prefix) || 0) + 1)
    }
  }
  const result: { prefix: string; heading: string; count: number }[] = []
  for (const [prefix, count] of map.entries()) {
    result.push({ prefix, heading: prefix, count })
  }
  return result.sort((a, b) => a.prefix.localeCompare(b.prefix))
}

export function getEntitiesByEra(eraSlug: string): Entity[] {
  return Object.values(ENTITIES).filter((e) => e.eraSlug === eraSlug)
}

export function getEntitiesByContinent(continent: string): Entity[] {
  return Object.values(ENTITIES).filter(
    (e) => e.continent.toLowerCase() === continent.toLowerCase()
  )
}

export function getEntitiesByLabel(label: Entity['label']): Entity[] {
  return Object.values(ENTITIES).filter((e) => e.label === label)
}
