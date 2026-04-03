/**
 * Call Number Classification System
 *
 * Dewey-style "shelf address" for every node: Class.Division.Slug
 * Designed after the Library of Alexandria navigation metaphor.
 *
 * Classes 0–9 map to top-level node families:
 *   0 = Ideas (Core: Political, Ethical, Legal)
 *   1 = Ideas (Other: Economic, Scientific, Technological, Religious, Cultural, etc.)
 *   2 = People
 *   3 = Institutions
 *   4 = Places
 *   5 = Events
 *   6 = Movements
 *   7 = Artifacts & Texts
 *   8 = Evidence
 *   9 = Timeframes
 */

export interface ClassEntry {
  code: number
  heading: string
  nodeTypes: string[]
}

export interface DivisionEntry {
  code: string   // e.g. "010", "220", "510"
  heading: string
  parentClass: number
}

/* ── Top-Level Classes (the 10 shelves) ── */
export const CLASSES: ClassEntry[] = [
  { code: 0, heading: 'Ideas – Core Categories', nodeTypes: ['Political', 'Ethical', 'Legal'] },
  { code: 1, heading: 'Ideas – Other Theories', nodeTypes: ['Economic', 'Scientific', 'Technological', 'Religious', 'Cultural', 'Environmental', 'Artistic'] },
  { code: 2, heading: 'People', nodeTypes: ['Philosophers', 'Leaders', 'Scientists', 'Activists', 'Artists', 'Military', 'Explorers'] },
  { code: 3, heading: 'Institutions', nodeTypes: ['Political', 'Legal', 'Economic', 'Religious', 'Scientific', 'Cultural', 'International', 'Educational', 'Military'] },
  { code: 4, heading: 'Places', nodeTypes: ['Continent', 'Region', 'Country', 'City', 'Empire', 'Civilization'] },
  { code: 5, heading: 'Events', nodeTypes: ['Wars', 'Revolutions', 'Elections', 'Scientific Discoveries', 'Environmental Crises', 'Agricultural', 'Economic'] },
  { code: 6, heading: 'Movements', nodeTypes: ['Political', 'Social', 'Religious', 'Cultural', 'Scientific', 'Technological', 'Environmental'] },
  { code: 7, heading: 'Artifacts & Texts', nodeTypes: ['Constitutions', 'Codes', 'Scriptures', 'Scientific Works', 'Artworks', 'Technologies'] },
  { code: 8, heading: 'Evidence', nodeTypes: ['Primary', 'Secondary', 'Archaeological', 'Quantitative', 'Oral'] },
  { code: 9, heading: 'Timeframes', nodeTypes: ['Period', 'Era', 'Epoch'] },
]

/* ── Second-Level Divisions ── */
export const DIVISIONS: DivisionEntry[] = [
  // 0 – Ideas (Core: Political, Ethical, Legal)
  { code: '010', heading: 'Political Systems & Governance', parentClass: 0 },
  { code: '011', heading: 'Democracy & Republicanism', parentClass: 0 },
  { code: '012', heading: 'Monarchy & Autocracy', parentClass: 0 },
  { code: '013', heading: 'Federalism & Confederalism', parentClass: 0 },
  { code: '014', heading: 'Theocracy & Divine Rule', parentClass: 0 },
  { code: '015', heading: 'Colonialism & Imperialism', parentClass: 0 },
  { code: '016', heading: 'Sovereignty & Self-Determination', parentClass: 0 },
  { code: '020', heading: 'Ethical Systems', parentClass: 0 },
  { code: '021', heading: 'Virtue Ethics', parentClass: 0 },
  { code: '022', heading: 'Deontology & Duty Ethics', parentClass: 0 },
  { code: '023', heading: 'Consequentialism & Utilitarianism', parentClass: 0 },
  { code: '024', heading: 'Natural Law Theory', parentClass: 0 },
  { code: '025', heading: 'Social Contract Theory', parentClass: 0 },
  { code: '030', heading: 'Legal Systems & Law', parentClass: 0 },
  { code: '031', heading: 'Common Law', parentClass: 0 },
  { code: '032', heading: 'Civil Law & Roman Law', parentClass: 0 },
  { code: '033', heading: 'Religious & Canon Law', parentClass: 0 },
  { code: '034', heading: 'Customary & Indigenous Law', parentClass: 0 },
  { code: '035', heading: 'International Law & Treaties', parentClass: 0 },
  { code: '036', heading: 'Constitutional Law', parentClass: 0 },

  // 1 – Ideas (Other: Economic, Scientific, Technological, Religious, Cultural, etc.)
  { code: '110', heading: 'Economic Theories & Systems', parentClass: 1 },
  { code: '111', heading: 'Mercantilism & Trade Theory', parentClass: 1 },
  { code: '112', heading: 'Classical & Neoclassical Economics', parentClass: 1 },
  { code: '113', heading: 'Marxism & Socialist Economics', parentClass: 1 },
  { code: '114', heading: 'Keynesian & Monetary Economics', parentClass: 1 },
  { code: '115', heading: 'Agricultural & Land Economics', parentClass: 1 },
  { code: '120', heading: 'Scientific Paradigms', parentClass: 1 },
  { code: '121', heading: 'Natural Philosophy & Classical Science', parentClass: 1 },
  { code: '122', heading: 'Astronomy & Cosmology', parentClass: 1 },
  { code: '123', heading: 'Physics & Mechanics', parentClass: 1 },
  { code: '124', heading: 'Chemistry & Alchemy', parentClass: 1 },
  { code: '125', heading: 'Biology & Evolution', parentClass: 1 },
  { code: '126', heading: 'Medicine & Public Health', parentClass: 1 },
  { code: '130', heading: 'Technological Innovations', parentClass: 1 },
  { code: '131', heading: 'Agricultural Technology', parentClass: 1 },
  { code: '132', heading: 'Manufacturing & Industrial', parentClass: 1 },
  { code: '133', heading: 'Transportation & Navigation', parentClass: 1 },
  { code: '134', heading: 'Communication & Information', parentClass: 1 },
  { code: '135', heading: 'Military Technology', parentClass: 1 },
  { code: '136', heading: 'Computing & Digital Technology', parentClass: 1 },
  { code: '140', heading: 'Religious & Philosophical Concepts', parentClass: 1 },
  { code: '141', heading: 'Monotheism & Abrahamic Theology', parentClass: 1 },
  { code: '142', heading: 'Polytheism & Mythology', parentClass: 1 },
  { code: '143', heading: 'Eastern Philosophy & Dharmic Thought', parentClass: 1 },
  { code: '144', heading: 'Mysticism & Esotericism', parentClass: 1 },
  { code: '145', heading: 'Secular & Humanist Philosophy', parentClass: 1 },
  { code: '150', heading: 'Social & Cultural Theories', parentClass: 1 },
  { code: '151', heading: 'Sociology & Social Structure', parentClass: 1 },
  { code: '152', heading: 'Anthropology & Ethnography', parentClass: 1 },
  { code: '153', heading: 'Linguistics & Language Theory', parentClass: 1 },
  { code: '154', heading: 'Psychology & Human Behavior', parentClass: 1 },
  { code: '155', heading: 'Education & Pedagogy', parentClass: 1 },
  { code: '160', heading: 'Environmental & Ecological Ideas', parentClass: 1 },
  { code: '161', heading: 'Conservation & Preservation', parentClass: 1 },
  { code: '162', heading: 'Climate & Atmospheric Science', parentClass: 1 },
  { code: '163', heading: 'Sustainability & Resource Management', parentClass: 1 },
  { code: '170', heading: 'Artistic & Aesthetic Movements', parentClass: 1 },
  { code: '171', heading: 'Classical & Renaissance Aesthetics', parentClass: 1 },
  { code: '172', heading: 'Modernism & Avant-Garde', parentClass: 1 },
  { code: '173', heading: 'Postmodernism & Deconstruction', parentClass: 1 },

  // 2 – People
  { code: '201', heading: 'Educators & Academics', parentClass: 2 },
  { code: '202', heading: 'Merchants & Economists', parentClass: 2 },
  { code: '203', heading: 'Athletes & Competitors', parentClass: 2 },
  { code: '204', heading: 'Architects & Engineers', parentClass: 2 },
  { code: '205', heading: 'Journalists & Chroniclers', parentClass: 2 },
  { code: '210', heading: 'Philosophers & Thinkers', parentClass: 2 },
  { code: '211', heading: 'Logicians & Mathematicians', parentClass: 2 },
  { code: '212', heading: 'Ethicists & Moralists', parentClass: 2 },
  { code: '220', heading: 'Political Leaders', parentClass: 2 },
  { code: '221', heading: 'Monarchs & Rulers', parentClass: 2 },
  { code: '222', heading: 'Heads of State & Government', parentClass: 2 },
  { code: '223', heading: 'Tribal & Indigenous Leaders', parentClass: 2 },
  { code: '230', heading: 'Legal Figures', parentClass: 2 },
  { code: '231', heading: 'Jurists & Legal Scholars', parentClass: 2 },
  { code: '240', heading: 'Scientists & Inventors', parentClass: 2 },
  { code: '241', heading: 'Physicians & Medical Pioneers', parentClass: 2 },
  { code: '242', heading: 'Astronomers & Cosmologists', parentClass: 2 },
  { code: '243', heading: 'Naturalists & Biologists', parentClass: 2 },
  { code: '250', heading: 'Religious Figures', parentClass: 2 },
  { code: '251', heading: 'Prophets & Founders', parentClass: 2 },
  { code: '252', heading: 'Theologians & Scholars', parentClass: 2 },
  { code: '253', heading: 'Missionaries', parentClass: 2 },
  { code: '260', heading: 'Artists & Writers', parentClass: 2 },
  { code: '261', heading: 'Authors & Novelists', parentClass: 2 },
  { code: '262', heading: 'Poets & Playwrights', parentClass: 2 },
  { code: '263', heading: 'Composers & Musicians', parentClass: 2 },
  { code: '264', heading: 'Painters & Sculptors', parentClass: 2 },
  { code: '265', heading: 'Architects & Designers', parentClass: 2 },
  { code: '270', heading: 'Activists & Reformers', parentClass: 2 },
  { code: '271', heading: 'Abolitionists', parentClass: 2 },
  { code: '272', heading: 'Suffragists & Feminists', parentClass: 2 },
  { code: '273', heading: 'Labor Organizers', parentClass: 2 },
  { code: '280', heading: 'Military Leaders & Commanders', parentClass: 2 },
  { code: '281', heading: 'Naval Commanders', parentClass: 2 },
  { code: '282', heading: 'Intelligence & Espionage', parentClass: 2 },
  { code: '283', heading: 'Modern Military Commanders', parentClass: 2 },
  { code: '290', heading: 'Explorers & Navigators', parentClass: 2 },
  { code: '291', heading: 'Space Explorers', parentClass: 2 },
  { code: '292', heading: 'Deep-Sea Explorers', parentClass: 2 },
  { code: '293', heading: 'Cartographers', parentClass: 2 },

  // 3 – Institutions
  { code: '310', heading: 'Political Institutions', parentClass: 3 },
  { code: '311', heading: 'Parliaments & Legislatures', parentClass: 3 },
  { code: '312', heading: 'Monarchies & Royal Courts', parentClass: 3 },
  { code: '313', heading: 'Executive & Presidential Offices', parentClass: 3 },
  { code: '314', heading: 'Colonial & Imperial Administrations', parentClass: 3 },
  { code: '315', heading: 'Tribal & Indigenous Councils', parentClass: 3 },
  { code: '316', heading: 'Political Parties & Organizations', parentClass: 3 },
  { code: '320', heading: 'Legal Institutions', parentClass: 3 },
  { code: '321', heading: 'Courts & Tribunals', parentClass: 3 },
  { code: '322', heading: 'Law Schools & Legal Academies', parentClass: 3 },
  { code: '323', heading: 'Regulatory Bodies & Commissions', parentClass: 3 },
  { code: '330', heading: 'Economic Institutions', parentClass: 3 },
  { code: '331', heading: 'Central Banks & Treasuries', parentClass: 3 },
  { code: '332', heading: 'Stock Exchanges & Markets', parentClass: 3 },
  { code: '333', heading: 'Trade Guilds & Merchant Houses', parentClass: 3 },
  { code: '334', heading: 'Development Banks & Aid Agencies', parentClass: 3 },
  { code: '340', heading: 'Religious Institutions', parentClass: 3 },
  { code: '341', heading: 'Churches & Cathedrals', parentClass: 3 },
  { code: '342', heading: 'Mosques & Islamic Institutions', parentClass: 3 },
  { code: '343', heading: 'Temples & Shrines', parentClass: 3 },
  { code: '344', heading: 'Monasteries & Religious Orders', parentClass: 3 },
  { code: '345', heading: 'Seminaries & Theological Schools', parentClass: 3 },
  { code: '350', heading: 'Scientific Institutions', parentClass: 3 },
  { code: '351', heading: 'Academies & Learned Societies', parentClass: 3 },
  { code: '352', heading: 'Research Laboratories', parentClass: 3 },
  { code: '353', heading: 'Observatories & Expeditions', parentClass: 3 },
  { code: '354', heading: 'Medical Institutions & Hospitals', parentClass: 3 },
  { code: '360', heading: 'Cultural Institutions', parentClass: 3 },
  { code: '361', heading: 'Museums & Galleries', parentClass: 3 },
  { code: '362', heading: 'Libraries & Archives', parentClass: 3 },
  { code: '363', heading: 'Theaters & Performance Venues', parentClass: 3 },
  { code: '364', heading: 'Media & Publishing Houses', parentClass: 3 },
  { code: '370', heading: 'International Organizations', parentClass: 3 },
  { code: '371', heading: 'United Nations System', parentClass: 3 },
  { code: '372', heading: 'Regional Alliances & Blocs', parentClass: 3 },
  { code: '373', heading: 'Humanitarian & Relief Organizations', parentClass: 3 },
  { code: '374', heading: 'Trade Agreements & Economic Unions', parentClass: 3 },
  { code: '380', heading: 'Educational Institutions', parentClass: 3 },
  { code: '381', heading: 'Universities & Colleges', parentClass: 3 },
  { code: '382', heading: 'Schools & Academies', parentClass: 3 },
  { code: '383', heading: 'Madrasas & Religious Schools', parentClass: 3 },
  { code: '384', heading: 'Public Education Systems', parentClass: 3 },
  { code: '390', heading: 'Military & Defense Organizations', parentClass: 3 },
  { code: '391', heading: 'Armies & Ground Forces', parentClass: 3 },
  { code: '392', heading: 'Navies & Maritime Forces', parentClass: 3 },
  { code: '393', heading: 'Intelligence & Security Agencies', parentClass: 3 },
  { code: '394', heading: 'Military Alliances (NATO, etc.)', parentClass: 3 },

  // 4 – Places
  { code: '410', heading: 'Continents', parentClass: 4 },
  { code: '420', heading: 'Regions', parentClass: 4 },
  { code: '421', heading: 'Sub-Saharan Africa', parentClass: 4 },
  { code: '422', heading: 'Middle East & North Africa', parentClass: 4 },
  { code: '423', heading: 'South & Southeast Asia', parentClass: 4 },
  { code: '424', heading: 'East Asia', parentClass: 4 },
  { code: '425', heading: 'Europe (Western & Eastern)', parentClass: 4 },
  { code: '426', heading: 'The Americas', parentClass: 4 },
  { code: '427', heading: 'Oceania & Pacific', parentClass: 4 },
  { code: '428', heading: 'Central Asia & Steppe', parentClass: 4 },
  { code: '430', heading: 'Countries / Polities', parentClass: 4 },
  { code: '440', heading: 'Cities', parentClass: 4 },
  { code: '441', heading: 'Capital Cities', parentClass: 4 },
  { code: '442', heading: 'Port Cities & Trade Hubs', parentClass: 4 },
  { code: '443', heading: 'Holy Cities & Pilgrimage Sites', parentClass: 4 },
  { code: '444', heading: 'Ancient & Ruined Cities', parentClass: 4 },
  { code: '450', heading: 'Empires / Dynasties', parentClass: 4 },
  { code: '451', heading: 'Ancient Empires (Egyptian, Mesopotamian)', parentClass: 4 },
  { code: '452', heading: 'Classical Empires (Roman, Persian, Han)', parentClass: 4 },
  { code: '453', heading: 'Medieval Empires (Byzantine, Mongol, Caliphates)', parentClass: 4 },
  { code: '454', heading: 'Early Modern Empires (Ottoman, Mughal, Ming)', parentClass: 4 },
  { code: '455', heading: 'Colonial Empires (British, French, Spanish)', parentClass: 4 },
  { code: '460', heading: 'Civilizations', parentClass: 4 },
  { code: '461', heading: 'River Valley Civilizations', parentClass: 4 },
  { code: '462', heading: 'Maritime & Island Civilizations', parentClass: 4 },
  { code: '463', heading: 'Steppe & Nomadic Civilizations', parentClass: 4 },
  { code: '470', heading: 'Culture Areas', parentClass: 4 },
  { code: '471', heading: 'Trade Routes & Corridors', parentClass: 4 },
  { code: '472', heading: 'Sacred Landscapes & Monuments', parentClass: 4 },
  { code: '473', heading: 'Battlefields & Conflict Zones', parentClass: 4 },

  // 5 – Events
  { code: '510', heading: 'Wars & Conflicts', parentClass: 5 },
  { code: '511', heading: 'Ancient & Classical Wars', parentClass: 5 },
  { code: '512', heading: 'Medieval Wars & Crusades', parentClass: 5 },
  { code: '513', heading: 'Early Modern Wars & Colonial Conflicts', parentClass: 5 },
  { code: '514', heading: 'World Wars', parentClass: 5 },
  { code: '515', heading: 'Cold War Conflicts & Proxy Wars', parentClass: 5 },
  { code: '516', heading: 'Civil Wars & Internal Conflicts', parentClass: 5 },
  { code: '517', heading: 'Sieges & Battles', parentClass: 5 },
  { code: '520', heading: 'Revolutions & Uprisings', parentClass: 5 },
  { code: '521', heading: 'Political Revolutions', parentClass: 5 },
  { code: '522', heading: 'Social & Peasant Revolts', parentClass: 5 },
  { code: '523', heading: 'Independence & Liberation Movements', parentClass: 5 },
  { code: '524', heading: 'Coups & Palace Revolutions', parentClass: 5 },
  { code: '530', heading: 'Elections & Political Shifts', parentClass: 5 },
  { code: '531', heading: 'Founding Elections & Constitutions', parentClass: 5 },
  { code: '532', heading: 'Regime Changes & Transitions', parentClass: 5 },
  { code: '540', heading: 'Legal Cases', parentClass: 5 },
  { code: '541', heading: 'Landmark Trials', parentClass: 5 },
  { code: '542', heading: 'International Tribunals', parentClass: 5 },
  { code: '550', heading: 'Scientific Discoveries', parentClass: 5 },
  { code: '551', heading: 'Astronomical Observations', parentClass: 5 },
  { code: '552', heading: 'Medical & Biological Discoveries', parentClass: 5 },
  { code: '553', heading: 'Physical & Chemical Discoveries', parentClass: 5 },
  { code: '554', heading: 'Archaeological Discoveries', parentClass: 5 },
  { code: '560', heading: 'Technological Breakthroughs', parentClass: 5 },
  { code: '561', heading: 'Industrial Inventions', parentClass: 5 },
  { code: '562', heading: 'Computing & Digital Milestones', parentClass: 5 },
  { code: '563', heading: 'Space Exploration Milestones', parentClass: 5 },
  { code: '564', heading: 'Ancient & Traditional Technology', parentClass: 5 },
  { code: '565', heading: 'Communication & Transport Technology', parentClass: 5 },
  { code: '570', heading: 'Religious Events', parentClass: 5 },
  { code: '571', heading: 'Church Councils & Synods', parentClass: 5 },
  { code: '572', heading: 'Reformations & Schisms', parentClass: 5 },
  { code: '573', heading: 'Spiritual Awakenings & Revivals', parentClass: 5 },
  { code: '574', heading: 'Persecutions & Martyrdoms', parentClass: 5 },
  { code: '575', heading: 'Biblical & Canonical Events', parentClass: 5 },
  { code: '576', heading: 'General Religious Events', parentClass: 5 },
  { code: '580', heading: 'Environmental Events', parentClass: 5 },
  { code: '581', heading: 'Natural Disasters', parentClass: 5 },
  { code: '582', heading: 'Famines & Droughts', parentClass: 5 },
  { code: '583', heading: 'Epidemics & Pandemics', parentClass: 5 },
  { code: '584', heading: 'Climate Shifts & Ice Ages', parentClass: 5 },
  { code: '590', heading: 'Agricultural & Economic Events', parentClass: 5 },
  { code: '591', heading: 'Agricultural Revolutions', parentClass: 5 },
  { code: '592', heading: 'Economic Crises & Depressions', parentClass: 5 },
  { code: '593', heading: 'Trade Booms & Gold Rushes', parentClass: 5 },

  // 6 – Movements
  { code: '610', heading: 'Political Movements', parentClass: 6 },
  { code: '611', heading: 'Nationalism & Nation-Building', parentClass: 6 },
  { code: '612', heading: 'Anti-Colonial & Decolonization', parentClass: 6 },
  { code: '613', heading: 'Communism & Socialism', parentClass: 6 },
  { code: '614', heading: 'Fascism & Totalitarianism', parentClass: 6 },
  { code: '615', heading: 'Liberalism & Constitutionalism', parentClass: 6 },
  { code: '616', heading: 'Pan-Movements (Pan-Africanism, Pan-Arabism)', parentClass: 6 },
  { code: '620', heading: 'Social Movements', parentClass: 6 },
  { code: '621', heading: 'Abolition & Anti-Slavery', parentClass: 6 },
  { code: '622', heading: 'Women\'s Suffrage & Feminism', parentClass: 6 },
  { code: '623', heading: 'Civil Rights & Racial Justice', parentClass: 6 },
  { code: '624', heading: 'Labor & Workers\' Rights', parentClass: 6 },
  { code: '625', heading: 'LGBTQ+ Rights', parentClass: 6 },
  { code: '626', heading: 'Disability Rights & Inclusion', parentClass: 6 },
  { code: '630', heading: 'Religious Movements', parentClass: 6 },
  { code: '631', heading: 'Protestant Reformation', parentClass: 6 },
  { code: '632', heading: 'Counter-Reformation & Catholic Revival', parentClass: 6 },
  { code: '633', heading: 'Islamic Reform & Revival', parentClass: 6 },
  { code: '634', heading: 'Missionary & Evangelical Movements', parentClass: 6 },
  { code: '635', heading: 'New Religious Movements', parentClass: 6 },
  { code: '640', heading: 'Cultural Movements', parentClass: 6 },
  { code: '641', heading: 'Renaissance & Humanism', parentClass: 6 },
  { code: '642', heading: 'Enlightenment & Rationalism', parentClass: 6 },
  { code: '643', heading: 'Romanticism & Transcendentalism', parentClass: 6 },
  { code: '644', heading: 'Modernist & Avant-Garde Movements', parentClass: 6 },
  { code: '645', heading: 'Vernacular & Language Movements', parentClass: 6 },
  { code: '650', heading: 'Scientific Movements', parentClass: 6 },
  { code: '651', heading: 'Scientific Revolution', parentClass: 6 },
  { code: '652', heading: 'Empiricism & Positivism', parentClass: 6 },
  { code: '653', heading: 'Open Science & Peer Review', parentClass: 6 },
  { code: '660', heading: 'Technological Movements', parentClass: 6 },
  { code: '661', heading: 'Industrial Revolution', parentClass: 6 },
  { code: '662', heading: 'Digital Revolution & Internet', parentClass: 6 },
  { code: '663', heading: 'Green Technology & Renewables', parentClass: 6 },
  { code: '670', heading: 'Environmental Movements', parentClass: 6 },
  { code: '671', heading: 'Conservation & Wilderness Preservation', parentClass: 6 },
  { code: '672', heading: 'Climate Action & Sustainability', parentClass: 6 },
  { code: '673', heading: 'Animal Rights & Wildlife Protection', parentClass: 6 },
  { code: '680', heading: 'Trade & Navigation Movements', parentClass: 6 },
  { code: '681', heading: 'Silk Road & Overland Trade', parentClass: 6 },
  { code: '682', heading: 'Maritime Trade & Age of Sail', parentClass: 6 },
  { code: '683', heading: 'Globalization & Free Trade', parentClass: 6 },

  // 7 – Artifacts & Texts
  { code: '710', heading: 'Constitutions & Charters', parentClass: 7 },
  { code: '711', heading: 'Ancient Codes & Decrees', parentClass: 7 },
  { code: '712', heading: 'Medieval Charters & Concordats', parentClass: 7 },
  { code: '713', heading: 'Modern Constitutions', parentClass: 7 },
  { code: '714', heading: 'Declarations & Proclamations', parentClass: 7 },
  { code: '720', heading: 'Legal Codes', parentClass: 7 },
  { code: '721', heading: 'Ancient Legal Codes (Hammurabi, Roman)', parentClass: 7 },
  { code: '722', heading: 'Canon & Religious Law Codes', parentClass: 7 },
  { code: '723', heading: 'Civil & Commercial Codes', parentClass: 7 },
  { code: '724', heading: 'International Treaties & Conventions', parentClass: 7 },
  { code: '730', heading: 'Religious Texts', parentClass: 7 },
  { code: '731', heading: 'Hebrew Bible & Torah', parentClass: 7 },
  { code: '732', heading: 'New Testament & Christian Texts', parentClass: 7 },
  { code: '733', heading: 'Quran & Islamic Texts', parentClass: 7 },
  { code: '734', heading: 'Vedas, Upanishads & Hindu Texts', parentClass: 7 },
  { code: '735', heading: 'Buddhist Scriptures (Pali Canon, Sutras)', parentClass: 7 },
  { code: '736', heading: 'Other Sacred & Wisdom Texts', parentClass: 7 },
  { code: '740', heading: 'Philosophical Works', parentClass: 7 },
  { code: '741', heading: 'Ancient Philosophy (Greek, Chinese)', parentClass: 7 },
  { code: '742', heading: 'Medieval Scholastic Works', parentClass: 7 },
  { code: '743', heading: 'Enlightenment Philosophical Works', parentClass: 7 },
  { code: '744', heading: 'Modern & Contemporary Philosophy', parentClass: 7 },
  { code: '750', heading: 'Scientific Texts', parentClass: 7 },
  { code: '751', heading: 'Mathematical Treatises', parentClass: 7 },
  { code: '752', heading: 'Natural History & Biology Texts', parentClass: 7 },
  { code: '753', heading: 'Physics & Astronomy Texts', parentClass: 7 },
  { code: '754', heading: 'Medical & Pharmacological Texts', parentClass: 7 },
  { code: '760', heading: 'Artworks', parentClass: 7 },
  { code: '761', heading: 'Paintings & Visual Art', parentClass: 7 },
  { code: '762', heading: 'Sculpture & Monuments', parentClass: 7 },
  { code: '763', heading: 'Music & Compositions', parentClass: 7 },
  { code: '764', heading: 'Architecture & Built Works', parentClass: 7 },
  { code: '770', heading: 'Technological Artifacts', parentClass: 7 },
  { code: '771', heading: 'Tools & Instruments', parentClass: 7 },
  { code: '772', heading: 'Weapons & Armor', parentClass: 7 },
  { code: '773', heading: 'Ships & Vehicles', parentClass: 7 },
  { code: '774', heading: 'Machines & Engines', parentClass: 7 },
  { code: '780', heading: 'Historical & Literary Texts', parentClass: 7 },
  { code: '781', heading: 'Histories & Chronicles', parentClass: 7 },
  { code: '782', heading: 'Epic Poetry & Mythology', parentClass: 7 },
  { code: '783', heading: 'Novels & Prose Fiction', parentClass: 7 },
  { code: '784', heading: 'Travel Writing & Geography', parentClass: 7 },
  { code: '785', heading: 'Political & Polemical Texts', parentClass: 7 },

  // 8 – Evidence
  { code: '810', heading: 'Primary Sources', parentClass: 8 },
  { code: '811', heading: 'Inscriptions & Epigraphy', parentClass: 8 },
  { code: '812', heading: 'Letters & Correspondence', parentClass: 8 },
  { code: '813', heading: 'Official Records & Archives', parentClass: 8 },
  { code: '814', heading: 'Diaries & Memoirs', parentClass: 8 },
  { code: '815', heading: 'Eyewitness Accounts', parentClass: 8 },
  { code: '820', heading: 'Secondary Sources', parentClass: 8 },
  { code: '821', heading: 'Academic Monographs', parentClass: 8 },
  { code: '822', heading: 'Peer-Reviewed Journal Articles', parentClass: 8 },
  { code: '823', heading: 'Encyclopedias & Reference Works', parentClass: 8 },
  { code: '830', heading: 'Archaeological Evidence', parentClass: 8 },
  { code: '831', heading: 'Excavation Reports', parentClass: 8 },
  { code: '832', heading: 'Artifact Analysis', parentClass: 8 },
  { code: '833', heading: 'Radiocarbon & Dating Evidence', parentClass: 8 },
  { code: '840', heading: 'Quantitative Data', parentClass: 8 },
  { code: '841', heading: 'Census & Demographic Data', parentClass: 8 },
  { code: '842', heading: 'Economic & Trade Statistics', parentClass: 8 },
  { code: '843', heading: 'Geospatial & Mapping Data', parentClass: 8 },
  { code: '850', heading: 'Oral Traditions', parentClass: 8 },
  { code: '851', heading: 'Oral Histories & Interviews', parentClass: 8 },
  { code: '852', heading: 'Folklore & Mythological Traditions', parentClass: 8 },
  { code: '853', heading: 'Genealogies & Lineage Records', parentClass: 8 },

  // 9 – Timeframes
  { code: '910', heading: 'Prehistoric', parentClass: 9 },
  { code: '911', heading: 'Paleolithic & Mesolithic', parentClass: 9 },
  { code: '912', heading: 'Neolithic & Chalcolithic', parentClass: 9 },
  { code: '913', heading: 'Bronze Age', parentClass: 9 },
  { code: '920', heading: 'Classical', parentClass: 9 },
  { code: '921', heading: 'Archaic Period', parentClass: 9 },
  { code: '922', heading: 'Hellenistic Period', parentClass: 9 },
  { code: '923', heading: 'Roman Period', parentClass: 9 },
  { code: '924', heading: 'Late Antiquity', parentClass: 9 },
  { code: '930', heading: 'Medieval', parentClass: 9 },
  { code: '931', heading: 'Early Medieval / Dark Ages', parentClass: 9 },
  { code: '932', heading: 'High Medieval', parentClass: 9 },
  { code: '933', heading: 'Late Medieval', parentClass: 9 },
  { code: '940', heading: 'Early Modern', parentClass: 9 },
  { code: '941', heading: 'Age of Exploration', parentClass: 9 },
  { code: '942', heading: 'Renaissance Period', parentClass: 9 },
  { code: '943', heading: 'Reformation Era', parentClass: 9 },
  { code: '944', heading: 'Age of Enlightenment', parentClass: 9 },
  { code: '950', heading: 'Modern', parentClass: 9 },
  { code: '951', heading: 'Industrial Age', parentClass: 9 },
  { code: '952', heading: 'Age of Empire / New Imperialism', parentClass: 9 },
  { code: '953', heading: 'Interwar Period', parentClass: 9 },
  { code: '954', heading: 'World War II Era', parentClass: 9 },
  { code: '960', heading: 'Contemporary', parentClass: 9 },
  { code: '961', heading: 'Cold War Era', parentClass: 9 },
  { code: '962', heading: 'Post-Cold War & Globalization', parentClass: 9 },
  { code: '963', heading: 'Digital Age', parentClass: 9 },
]

/* ── Color scheme by class (Golden Markers) ── */
export const CLASS_COLORS: Record<number, string> = {
  0: '#D4AF37', // Gold — Core Ideas
  1: '#C5963A', // Amber — Other Ideas
  2: '#3A7D44', // Green — People
  3: '#8B3A3A', // Empire Red — Institutions
  4: '#3B6BC2', // Blue — Places
  5: '#C5963A', // Amber — Events
  6: '#6B3FA0', // Purple — Movements
  7: '#5A2222', // Dark — Artifacts & Texts
  8: '#787469', // Stone — Evidence
  9: '#96770B', // Dark Gold — Timeframes
}

/* ── Helpers ── */

/**
 * Parse components from a call number.
 * Handles both formats:
 *   "220.01-henry-viii"  → { classCode: 2, division: "220", slug: "henry-viii" }
 *   "530.volcanic"       → { classCode: 5, division: "530", slug: "volcanic" }
 */
export function parseCallNumber(cn: string): { classCode: number; division: string; slug: string } | null {
  // Format 1: "220.01-henry-viii" (with serial number)
  const m1 = cn.match(/^(\d)(\d{2})\.(\d+)-(.+)$/)
  if (m1) {
    return {
      classCode: parseInt(m1[1]),
      division: m1[1] + m1[2],
      slug: m1[4],
    }
  }
  // Format 2: "530.volcanic" (slug-only, no serial)
  const m2 = cn.match(/^(\d)(\d{2})\.([a-z].*)$/i)
  if (m2) {
    return {
      classCode: parseInt(m2[1]),
      division: m2[1] + m2[2],
      slug: m2[3],
    }
  }
  return null
}

/** Get the class heading from a call number */
export function getClassHeading(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return ''
  const cls = CLASSES.find(c => c.code === parsed.classCode)
  return cls?.heading || ''
}

/** Get the division heading from a call number */
export function getDivisionHeading(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return ''
  const div = DIVISIONS.find(d => d.code === parsed.division)
  if (div) return div.heading
  // Fallback: try parent division (e.g. 261 → 260)
  const parentCode = parsed.division.slice(0, 2) + '0'
  const parent = DIVISIONS.find(d => d.code === parentCode)
  return parent?.heading || ''
}

/** Build breadcrumb trail from call number */
export function getCallNumberBreadcrumbs(cn: string): { label: string; prefix: string }[] {
  const parsed = parseCallNumber(cn)
  if (!parsed) return []
  const cls = CLASSES.find(c => c.code === parsed.classCode)
  const div = DIVISIONS.find(d => d.code === parsed.division)
  const crumbs = [
    { label: cls?.heading || `Class ${parsed.classCode}`, prefix: `${parsed.classCode}` },
  ]
  // If this is a sub-division (e.g. 261), show parent (260) then sub-division (261)
  const parentCode = parsed.division.slice(0, 2) + '0'
  if (parentCode !== parsed.division) {
    const parent = DIVISIONS.find(d => d.code === parentCode)
    if (parent) crumbs.push({ label: parent.heading, prefix: parentCode })
  }
  crumbs.push({ label: div?.heading || `Division ${parsed.division}`, prefix: parsed.division })
  return crumbs
}

/** Get color for a call number based on its class */
export function getCallNumberColor(cn: string): string {
  const parsed = parseCallNumber(cn)
  if (!parsed) return '#9E9A90'
  return CLASS_COLORS[parsed.classCode] || '#9E9A90'
}
