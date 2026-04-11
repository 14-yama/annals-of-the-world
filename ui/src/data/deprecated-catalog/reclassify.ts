/**
 * Call Number Reclassification — Auto-assigns entities to expanded sub-divisions
 *
 * Uses keyword matching (name, summary, subjects) and era-based heuristics
 * to promote entities from parent divisions (e.g., 510) to specific
 * sub-divisions (e.g., 512 Medieval Wars & Crusades).
 *
 * Applied in the catalog index pipeline after dedup and enrichment.
 */
import type { Entity } from '../entityTypes'

/* ── Keyword → sub-division rules per parent division ── */

interface Rule {
  div: string
  /** If ANY keyword matches name/summary/subjects (case-insensitive) */
  kw?: string[]
  /** Also require era match (if specified) */
  eras?: string[]
}

/**
 * Rules keyed by parent division code. First matching rule wins.
 * Rules with both keywords AND eras are checked before rules with keywords only.
 */
const RULES: Record<string, Rule[]> = {
  // ── Class 0: Ideas (Core) ──
  '010': [
    { div: '011', kw: ['democracy', 'republic', 'democratic', 'suffrage', 'parliament', 'assembly'] },
    { div: '012', kw: ['monarchy', 'king', 'queen', 'autocracy', 'absolutism', 'divine right', 'dynast'] },
    { div: '013', kw: ['federal', 'confedera', 'devolution'] },
    { div: '014', kw: ['theocrac', 'divine rule', 'caliphate rule'] },
    { div: '015', kw: ['colonial', 'imperial', 'imperialism', 'empire-build'] },
    { div: '016', kw: ['sovereign', 'self-determination', 'independence movement'] },
  ],
  '020': [
    { div: '021', kw: ['virtue ethics', 'virtuous', 'cardinal virtue'] },
    { div: '022', kw: ['deontolog', 'duty', 'categorical imperative', 'kantian'] },
    { div: '023', kw: ['consequential', 'utilitarian', 'greatest good'] },
    { div: '024', kw: ['natural law', 'natural right', 'lex naturalis'] },
    { div: '025', kw: ['social contract', 'compact', 'consent of the governed'] },
  ],
  '030': [
    { div: '031', kw: ['common law', 'precedent', 'stare decisis'] },
    { div: '032', kw: ['civil law', 'roman law', 'justinian', 'code civil', 'napoleonic code'] },
    { div: '033', kw: ['canon law', 'sharia', 'halakh', 'religious law', 'ecclesiastical'] },
    { div: '034', kw: ['customary law', 'indigenous law', 'tribal law', 'adat'] },
    { div: '035', kw: ['international law', 'treaty', 'convention', 'law of nations'] },
    { div: '036', kw: ['constitutional', 'constitution', 'bill of rights', 'fundamental law'] },
  ],

  // ── Class 1: Ideas (Other) ──
  '110': [
    { div: '111', kw: ['mercantil', 'trade theory', 'bullion'] },
    { div: '112', kw: ['classical economics', 'neoclassical', 'adam smith', 'free market', 'laissez'] },
    { div: '113', kw: ['marxis', 'socialist econom', 'communist econom', 'surplus value', 'proletariat'] },
    { div: '114', kw: ['keynesian', 'monetary', 'central bank', 'inflation', 'quantitative easing'] },
    { div: '115', kw: ['agricultural econom', 'land reform', 'physiocrat'] },
  ],
  '120': [
    { div: '121', kw: ['natural philosophy', 'classical science'] },
    { div: '122', kw: ['astronom', 'cosmolog', 'stellar', 'planetary', 'heliocentric', 'geocentric'] },
    { div: '123', kw: ['physics', 'mechanic', 'quantum', 'relativity', 'thermodynamic', 'gravity'] },
    { div: '124', kw: ['chemistry', 'alchemy', 'element', 'compound', 'periodic'] },
    { div: '125', kw: ['biology', 'evolution', 'natural selection', 'genetics', 'darwin'] },
    { div: '126', kw: ['medicine', 'medical', 'health', 'epidemic', 'vaccine', 'anatomy'] },
  ],
  '130': [
    { div: '131', kw: ['agricultural tech', 'irrigation', 'plow', 'seed drill', 'crop rotation'] },
    { div: '132', kw: ['manufactur', 'industrial', 'factory', 'mass production', 'assembly line'] },
    { div: '133', kw: ['transportation tech', 'navigation tech', 'compass', 'locomotive', 'automobile'] },
    { div: '134', kw: ['communicat', 'telegraph', 'telephone', 'radio', 'printing press', 'internet'] },
    { div: '135', kw: ['military tech', 'weapon', 'gunpowder', 'ballistic', 'drone'] },
    { div: '136', kw: ['comput', 'digital', 'software', 'algorithm', 'artificial intelligence', 'AI '] },
  ],
  '140': [
    { div: '141', kw: ['monotheism', 'abrahamic', 'christian theology', 'islamic theology', 'jewish theology', 'trinit'] },
    { div: '142', kw: ['polytheism', 'mythology', 'pantheon', 'pagan', 'animism'] },
    { div: '143', kw: ['eastern philosophy', 'dharma', 'buddhis', 'hindu', 'confucian', 'tao', 'vedanta'] },
    { div: '144', kw: ['mysticism', 'esoteric', 'gnostic', 'sufi', 'kabbala', 'hermeticism'] },
    { div: '145', kw: ['secular', 'humanist', 'atheis', 'agnostic', 'rationalism', 'existential'] },
  ],
  '150': [
    { div: '151', kw: ['sociolog', 'social structure', 'class system', 'stratification'] },
    { div: '152', kw: ['anthropolog', 'ethnograph', 'kinship'] },
    { div: '153', kw: ['linguist', 'language theory', 'grammar', 'syntax', 'phonolog'] },
    { div: '154', kw: ['psycholog', 'behavioral', 'cognitive', 'freud', 'jung'] },
    { div: '155', kw: ['education', 'pedagog', 'schooling', 'curriculum', 'literacy'] },
  ],
  '160': [
    { div: '161', kw: ['conservation', 'preservation', 'national park', 'wildlife refuge'] },
    { div: '162', kw: ['climate', 'atmospheric', 'greenhouse', 'carbon', 'ozone'] },
    { div: '163', kw: ['sustainab', 'resource management', 'renewable', 'circular economy'] },
  ],
  '170': [
    { div: '171', kw: ['classical aesthetic', 'renaissance art', 'neoclassic'] },
    { div: '172', kw: ['modernism', 'avant-garde', 'cubism', 'futurism', 'expressionism'] },
    { div: '173', kw: ['postmodern', 'deconstruct', 'post-structur'] },
  ],

  // ── Class 2: People ──
  '220': [
    /* Within-division: refine leaders FIRST (monarchs/heads of state take priority) */
    { div: '221', kw: ['emperor', 'empress', 'caesar', 'tsar', 'czar', 'pharaoh', 'caliph', 'kaiser', 'shah', 'sultan', 'maharaja', 'king of', 'queen of', 'ruler of', 'dynast', 'founding king', 'royal house', 'regent', 'viceroy', 'shogun', 'khan ', 'prince of', 'princess', 'crowned', 'coronation', 'enthroned', 'ascended the throne', 'reign of', 'his reign', 'her reign', 'reigned'] },
    { div: '222', kw: ['prime minister', 'president', 'chancellor', 'premier', 'first minister', 'statesman', 'stateswoman', 'colonial admin', 'governor', 'administrator', 'dictator', 'leader of'] },
    { div: '223', kw: ['tribal chief', 'clan chief', 'chieftain', 'cacique', 'mansa', 'headman'] },
    /* Cross-division: move to correct person sub-class */
    { div: '250', kw: ['pope', 'bishop', 'patriarch', 'imam', 'rabbi', 'monk', 'saint', 'priest', 'cleric', 'ayatollah', 'dalai lama', 'guru', 'mufti', 'abbess', 'friar', 'cardinal', 'archbishop', 'deacon', 'preacher', 'evangelist', 'apostle', 'prophet', 'prophetess', 'nun ', 'abbess', 'mystic', 'theologian', 'church father'] },
    { div: '240', kw: ['scientist', 'mathematician', 'physicist', 'chemist', 'biologist', 'astronomer', 'inventor', 'naturalist', 'geologist', 'botanist', 'engineer', 'physician', 'surgeon', 'alchemist', 'anatomist'] },
    { div: '280', kw: ['general', 'admiral', 'marshal', 'commander', 'warlord', 'military leader', 'warrior', 'field marshal', 'conquest of', 'conqueror', 'military campaigns', 'troops', 'battle of', 'war hero', 'centurion'] },
    { div: '290', kw: ['explorer', 'navigator', 'cartographer', 'voyager', 'discoverer', 'circumnavigat', 'sailed', 'expedition led'] },
    { div: '270', kw: ['activist', 'reformer', 'abolitionist', 'suffragist', 'dissident', 'revolutionary leader', 'human rights', 'resistance leader', 'protest'] },
    { div: '260', kw: ['artist', 'painter', 'sculptor', 'musician', 'composer', 'writer', 'poet', 'author', 'novelist', 'playwright', 'architect', 'dramatist', 'bard', 'singer', 'calligrapher'] },
    { div: '230', kw: ['scholar', 'historian', 'jurist', 'lawyer', 'judge', 'educator', 'librarian', 'philologist', 'chronicler', 'lexicographer', 'grammarian', 'polymath'] },
    { div: '210', kw: ['philosopher', 'thinker', 'intellectual', 'logician', 'metaphysic', 'stoic ', 'epicurean', 'neo-platonist'] },
  ],

  '250': [
    /* Cross-division: kings/rulers misclassified as religious → 221 */
    { div: '221', kw: ['king of', 'king ', 'queen of', 'emperor', 'empress', 'pharaoh', 'sultan', 'tsar', 'czar', 'shah', 'caliph', 'kaiser', 'ruler of', 'kingdom', 'dynast', 'reign'] },
    { div: '280', kw: ['general', 'military leader', 'commander', 'conqueror', 'warlord', 'warrior', 'battle of'] },
    { div: '222', kw: ['president', 'prime minister', 'chancellor', 'governor', 'leader of', 'dictator', 'statesman'] },
    { div: '251', kw: ['siddhartha', 'buddha', 'bodhisattva', 'arhat', 'zen master', 'buddhist monk', 'buddhist teacher', 'prophet', 'prophetess', 'patriarch', 'matriarch', 'moses', 'abraham', 'jacob', 'joseph', 'adam', 'eve', 'noah', 'david', 'solomon', 'saul', 'samuel', 'elijah', 'isaiah', 'jeremiah', 'ezekiel', 'daniel', 'nehemiah', 'ezra', 'joshua', 'ruth', 'esther', 'deborah', 'gideon', 'samson', 'israelite', 'hebrew', 'genesis', 'jesus', 'christ', 'apostle', 'disciple', 'gospel', 'muhammad'] },
    { div: '252', kw: ['theologian', 'doctor of the church', 'church father', 'scholastic', 'systematic theology', 'dogmatic'] },
    { div: '253', kw: ['missionary', 'mission', 'evangelist', 'proselyt', 'convert'] },
  ],

  '280': [
    /* Cross-division: many entities here are NOT military — reclassify them */
    { div: '221', kw: ['pharaoh', 'emperor', 'empress', 'king of', 'queen of', 'king ', 'queen ', 'ruler of', 'sultan', 'shah', 'caliph', 'tsar', 'kaiser', 'dynast', 'reign', 'kingdom'] },
    { div: '222', kw: ['president', 'prime minister', 'chancellor', 'governor', 'leader of', 'dictator'] },
    { div: '250', kw: ['pope', 'bishop', 'patriarch', 'imam', 'rabbi', 'monk', 'saint', 'priest', 'cleric', 'theologian', 'reformer of the church', 'church father', 'preacher', 'mystic', 'nun', 'friar'] },
    { div: '210', kw: ['philosopher', 'thinker', 'intellectual'] },
    { div: '260', kw: ['artist', 'painter', 'sculptor', 'musician', 'composer', 'writer', 'poet', 'author', 'architect'] },
    { div: '240', kw: ['scientist', 'mathematician', 'physicist', 'chemist', 'biologist', 'astronomer', 'inventor'] },
    { div: '270', kw: ['reformer', 'reform', 'abolitionist', 'suffragist', 'dissident', 'activist', 'human rights', 'resistance leader'] },
    /* Sub-classify actual military leaders */
    { div: '281', kw: ['general', 'field marshal', 'commander', 'military leader', 'admiral', 'naval', 'conquer', 'warrior', 'warlord', 'centurion', 'troops'], eras: ['prehistoric', 'classical'] },
    { div: '282', kw: ['general', 'field marshal', 'commander', 'military leader', 'knight', 'crusad', 'conquer', 'warrior'], eras: ['medieval'] },
    { div: '283', kw: ['general', 'field marshal', 'commander', 'admiral', 'military leader', 'marshal', 'conquer', 'battle of', 'war hero', 'military campaign', 'troops', 'army'] },
  ],

  // ── Class 3: Institutions ──
  '310': [
    { div: '311', kw: ['parliament', 'legislature', 'congress', 'diet', 'duma', 'assembly', 'senate', 'riksdag', 'knesset', 'bundestag', 'cortes', 'althing'] },
    { div: '312', kw: ['monarchy', 'royal', 'crown', 'dynasty', 'sultanate', 'kingdom', 'empire', 'khanate', 'caliphate', 'shogunate', 'principality', 'duchy'] },
    { div: '313', kw: ['president', 'executive', 'prime minister', 'chancellor', 'republic', 'government of'] },
    { div: '314', kw: ['colonial', 'imperial admin', 'viceroy', 'governor-general', 'protectorate', 'mandate', 'east india company'] },
    { div: '315', kw: ['tribal', 'indigenous council', 'chieftain', 'clan', 'confederacy'] },
    /* Broader catch-all: parties, leagues, political organizations */
    { div: '316', kw: ['party', 'league', 'front', 'union', 'congress party', 'communist party', 'coalition', 'bloc', 'faction', 'political movement'] },
  ],
  '320': [
    { div: '321', kw: ['court', 'tribunal', 'supreme court', 'high court', 'judiciary'] },
    { div: '322', kw: ['law school', 'legal academy', 'bar association'] },
    { div: '323', kw: ['regulatory', 'commission', 'agency', 'ombudsman'] },
  ],
  '330': [
    { div: '331', kw: ['central bank', 'treasury', 'reserve bank', 'mint'] },
    { div: '332', kw: ['stock exchange', 'bourse', 'securities', 'exchange'] },
    { div: '333', kw: ['guild', 'merchant', 'trading house', 'hansa', 'chartered company'] },
    { div: '334', kw: ['development bank', 'world bank', 'imf', 'aid agency'] },
  ],
  '340': [
    { div: '341', kw: ['church', 'cathedral', 'basilica', 'chapel'] },
    { div: '342', kw: ['mosque', 'madrasa', 'islamic institution', 'waqf'] },
    { div: '343', kw: ['temple', 'shrine', 'pagoda', 'stupa'] },
    { div: '344', kw: ['monastery', 'abbey', 'priory', 'religious order', 'convent'] },
    { div: '345', kw: ['seminary', 'theological school', 'yeshiva', 'divinity'] },
  ],
  '350': [
    { div: '351', kw: ['academ', 'learned society', 'royal society'] },
    { div: '352', kw: ['laborator', 'research institute', 'research center'] },
    { div: '353', kw: ['observator', 'expedition', 'survey'] },
    { div: '354', kw: ['hospital', 'medical institution', 'clinic', 'infirmary'] },
  ],
  '360': [
    { div: '361', kw: ['museum', 'gallery', 'exhibit'] },
    { div: '362', kw: ['library', 'archive', 'manuscript collection'] },
    { div: '363', kw: ['theater', 'theatre', 'opera house', 'amphitheater'] },
    { div: '364', kw: ['publisher', 'press', 'newspaper', 'journal', 'broadcast'] },
  ],
  '370': [
    { div: '371', kw: ['united nations', 'UN ', 'UNESCO', 'UNICEF', 'WHO', 'security council'] },
    { div: '372', kw: ['NATO', 'ASEAN', 'EU ', 'African Union', 'OAS', 'BRICS', 'alliance'] },
    { div: '373', kw: ['red cross', 'humanitarian', 'relief', 'refugee', 'UNHCR'] },
    { div: '374', kw: ['trade agreement', 'WTO', 'GATT', 'free trade', 'economic union', 'customs union'] },
  ],
  '380': [
    { div: '381', kw: ['university', 'college', 'universitas'] },
    { div: '382', kw: ['school', 'academy', 'gymnasium', 'lyceum'] },
    { div: '383', kw: ['madrasa', 'madrasah', 'religious school', 'monastic school'] },
    { div: '384', kw: ['public education', 'national education', 'education system', 'compulsory'] },
  ],
  '390': [
    { div: '391', kw: ['army', 'ground force', 'infantry', 'cavalry', 'legion'] },
    { div: '392', kw: ['navy', 'naval', 'fleet', 'maritime force', 'admiralty'] },
    { div: '393', kw: ['intelligence', 'espionage', 'CIA', 'MI5', 'MI6', 'secret service', 'KGB'] },
    { div: '394', kw: ['NATO', 'military alliance', 'SEATO', 'Warsaw Pact', 'ANZUS'] },
  ],

  // ── Class 4: Places ──
  '420': [
    { div: '421', kw: ['sub-saharan', 'west africa', 'east africa', 'southern africa', 'central africa', 'sahel'] },
    { div: '422', kw: ['middle east', 'north africa', 'MENA', 'levant', 'maghreb', 'arabian'] },
    { div: '423', kw: ['south asia', 'southeast asia', 'indochina', 'malay'] },
    { div: '424', kw: ['east asia', 'china', 'japan', 'korea', 'sinosphere'] },
    { div: '425', kw: ['western europe', 'eastern europe', 'scandinavia', 'mediterranean', 'balkan'] },
    { div: '426', kw: ['americas', 'latin america', 'north america', 'south america', 'caribbean'] },
    { div: '427', kw: ['oceania', 'pacific', 'polynesia', 'melanesia', 'micronesia', 'australasia'] },
    { div: '428', kw: ['central asia', 'steppe', 'silk road region', 'inner asia'] },
  ],
  '440': [
    { div: '441', kw: ['capital city', 'capital of', 'seat of government'] },
    { div: '442', kw: ['port', 'harbor', 'harbour', 'trade hub', 'entrepot', 'emporium'] },
    { div: '443', kw: ['holy city', 'pilgrimage', 'sacred city', 'jerusalem', 'mecca', 'varanasi'] },
    { div: '444', kw: ['ancient city', 'ruin', 'archaeological site', 'lost city', 'abandoned'] },
  ],
  '450': [
    { div: '451', kw: ['egyptian empire', 'mesopotamian', 'akkadian', 'sumerian', 'babylonian', 'assyrian'], eras: ['prehistoric', 'classical'] },
    { div: '452', kw: ['roman', 'persian', 'han dynasty', 'maurya', 'hellenistic', 'achaemenid'], eras: ['classical'] },
    { div: '453', kw: ['byzantine', 'mongol', 'caliphate', 'abbasid', 'umayyad', 'ottoman', 'song dynasty'], eras: ['medieval'] },
    { div: '454', kw: ['ottoman', 'mughal', 'ming', 'qing', 'safavid', 'tokugawa'], eras: ['early-modern'] },
    { div: '455', kw: ['british empire', 'french empire', 'spanish empire', 'portuguese', 'dutch', 'colonial'] },
  ],
  '460': [
    { div: '461', kw: ['river valley', 'nile', 'mesopotamia', 'indus', 'yellow river', 'fertile crescent'] },
    { div: '462', kw: ['maritime', 'island', 'thalassocracy', 'minoan', 'phoenician', 'polynesian'] },
    { div: '463', kw: ['steppe', 'nomad', 'mongol', 'scythian', 'hun', 'turkic', 'xiongnu'] },
  ],
  '470': [
    { div: '471', kw: ['trade route', 'silk road', 'spice route', 'incense route', 'trans-saharan'] },
    { div: '472', kw: ['sacred', 'monument', 'temple complex', 'pyramid', 'stonehenge'] },
    { div: '473', kw: ['battlefield', 'conflict zone', 'front line', 'war zone'] },
  ],

  // ── Class 5: Events ──
  '510': [
    { div: '514', kw: ['world war i', 'world war ii', 'wwi', 'wwii', 'great war', 'second world war', 'first world war'] },
    { div: '515', kw: ['cold war', 'proxy war', 'korean war', 'vietnam war', 'cuban missile', 'afghan war', 'gulf war', 'iraq war', 'falklands', 'suez crisis'] },
    { div: '516', kw: ['civil war', 'internal conflict', 'insurgency', 'sectarian', 'ethnic conflict', 'revolt', 'uprising', 'rebellion', 'mutiny', 'riots'] },
    { div: '517', kw: ['siege of', 'battle of', 'sack of', 'fall of', 'capture of', 'massacre', 'bombing of', 'raid on'] },
    { div: '511', kw: ['war', 'conflict', 'invasion', 'conquest', 'campaign', 'raid', 'attack', 'corsair', 'pirate'], eras: ['prehistoric', 'classical'] },
    { div: '512', kw: ['war', 'conflict', 'crusade', 'invasion', 'conquest', 'campaign'], eras: ['medieval'] },
    { div: '513', kw: ['war', 'conflict', 'colonial war', 'invasion', 'conquest', 'campaign', 'corsair', 'pirate'], eras: ['early-modern'] },
    /* Any remaining modern/contemporary wars */
    { div: '515', kw: ['war', 'conflict', 'invasion', 'military operation', 'bombing', 'intervention'], eras: ['contemporary'] },
    { div: '514', kw: ['war', 'conflict', 'invasion', 'military campaign'], eras: ['modern'] },
    /* Broader catch-all for remaining violence */
    { div: '517', kw: ['massacre', 'killed', 'reprisal', 'atrocit', 'genocide', 'slaughter', 'assassination', 'terror'] },
  ],
  '520': [
    { div: '521', kw: ['political revolution', 'french revolution', 'american revolution', 'glorious revolution'] },
    { div: '522', kw: ['peasant revolt', 'social uprising', 'rebellion', 'jacquerie', 'boxer'] },
    { div: '523', kw: ['independence', 'liberation', 'decolonization', 'self-rule', 'sovereignty'] },
    { div: '524', kw: ['coup', 'palace revolution', 'overthrow', 'putsch', 'junta'] },
  ],
  '530': [
    /* ── Preserve correctly classified political/election entities first ── */
    { div: '532', kw: ['regime change', 'democratization', 'transition to democracy', 'constitution adopted', 'republic proclaimed', 'republic established', 'one-party', 'martial law', 'state of emergency', 'proclaimed republic', 'abolished monarchy', 'new constitution', 'provisional government', 'national assembly', 'unification'] },
    { div: '531', kw: ['election', 'elected', 'vote', 'ballot', 'referendum', 'plebiscite', 'suffrage', 'inaugurated', 'sworn in', 'electoral'] },

    /* ── Cross-division: Environmental / Natural Events → 58x ── */
    { div: '581', kw: ['volcanic', 'eruption', 'earthquake', 'tsunami', 'flood', 'hurricane', 'cyclone', 'typhoon', 'landslide', 'tidal wave', 'lava', 'caldera'] },
    { div: '582', kw: ['famine', 'drought', 'crop failure', 'starvation', 'food crisis', 'food shortage'] },
    { div: '583', kw: ['epidemic', 'pandemic', 'plague', 'cholera', 'smallpox', 'influenza', 'yellow fever', 'malaria', 'ebola', 'covid', 'black death', 'bubonic', 'typhus', 'leprosy'] },
    { div: '584', kw: ['climate shift', 'ice age', 'little ice age', 'desertification', 'global warming'] },
    { div: '580', kw: ['natural disaster', 'environmental catastrophe'] },

    /* ── Cross-division: Wars & Conflicts → 51x ── */
    { div: '514', kw: ['world war i', 'world war ii', 'wwi', 'wwii', 'first world war', 'second world war', 'great war'] },
    { div: '515', kw: ['cold war', 'proxy war', 'korean war', 'vietnam war', 'cuban missile'] },
    { div: '516', kw: ['civil war'] },
    { div: '517', kw: ['siege of', 'battle of', 'sack of', 'capture ', 'captured ', 'fall of'] },
    { div: '511', kw: ['war ', 'wars ', 'warfare', 'invad', 'conquer', 'subjugat'], eras: ['prehistoric', 'classical'] },
    { div: '512', kw: ['war ', 'wars ', 'warfare', 'crusade', 'invad', 'conquer'], eras: ['medieval'] },
    { div: '513', kw: ['war ', 'wars ', 'warfare', 'colonial war', 'invad', 'conquer'], eras: ['early-modern'] },
    { div: '510', kw: ['war against', 'wars of', 'invasion of', 'military campaign', 'armed conflict', 'genocide', 'massacre', 'bombing', 'raids', 'corsair', 'pirate', 'piracy'] },

    /* ── Cross-division: Revolutions & Uprisings → 52x ── */
    { div: '523', kw: ['independence', 'liberation', 'decolonization', 'self-rule', 'gains independence'] },
    { div: '524', kw: ['coup', "coup d'\u00e9tat", 'overthrow', 'putsch', 'junta', 'military takeover', 'assassinated', 'assassination'] },
    { div: '522', kw: ['rebellion', 'revolt', 'uprising', 'insurrection', 'mutiny', 'riots', 'resistance'] },
    { div: '521', kw: ['revolution'] },

    /* ── Cross-division: Treaties & Alliances → 540 ── */
    { div: '540', kw: ['treaty', 'peace agreement', 'armistice', 'accord', 'peace of', 'pact'] },

    /* ── Cross-division: Scientific Discoveries → 55x ── */
    { div: '554', kw: ['fossil', 'archaeological', 'hominin', 'excavat', 'cave art', 'rock art', 'neanderthal', 'homo erectus', 'homo sapiens', 'paleolithic', 'mesolithic', 'neolithic', 'stone age', 'footprint', 'gorge discover', 'megaliths', 'dolmen', 'ancient ruin'] },
    { div: '554', kw: ['settlement'], eras: ['prehistoric'] },
    { div: '551', kw: ['astronomical discovery', 'comet discovered', 'eclipse recorded'] },
    { div: '552', kw: ['medical breakthrough', 'vaccine discover'] },

    /* ── Cross-division: Technological Breakthroughs → 56x ── */
    { div: '561', kw: ['industrial revolution', 'factory system', 'steam power', 'railroad', 'railway'] },
    { div: '562', kw: ['computer', 'internet', 'digital revolution'] },
    { div: '563', kw: ['space program', 'satellite launch', 'moon landing', 'rocket'] },

    /* ── Cross-division: Religious Events → 57x ── */
    { div: '571', kw: ['council of', 'ecumenical council', 'synod of'] },
    { div: '572', kw: ['reformation', 'schism', 'great schism', 'protestant'] },
    { div: '574', kw: ['persecution', 'martyr', 'inquisition', 'pogrom', 'forced conversion'] },
    { div: '573', kw: ['revival', 'awakening', 'missionary'] },

    /* ── Cross-division: Agricultural & Economic → 59x ── */
    { div: '592', kw: ['economic crisis', 'depression', 'financial crash', 'recession', 'pyramid scheme', 'debt crisis', 'hyperinflation', 'resource curse'] },
    { div: '593', kw: ['trade boom', 'gold rush', 'spice trade', 'rubber boom', 'oil boom', 'slave trade', 'trade route', 'trade network', 'trade hub'] },
    { div: '591', kw: ['agricultural revolution', 'green revolution', 'irrigation project', 'crop domestication', 'agricultural communit'] },

    /* ── Cross-division: Exploration → 560 ── */
    { div: '560', kw: ['exploration', 'expedition', 'voyage of', 'circumnavigation', 'contact 1'] },

    /* ── Cross-division: Cultural & Artistic Events → 550/640 ── */
    { div: '550', kw: ['discovery', 'discovered', 'scientific', 'observatory', 'laboratory'] },

    /* ── Broader catch-all: events about kingdoms, dynasties, empires → 532 ── */
    { div: '532', kw: ['kingdom', 'dynasty', 'empire', 'sultana', 'khanate', 'caliphate', 'abolished', 'annexed', 'establishes', 'established', 'founded', 'formation', 'collapse', 'fragmentation', 'partition', 'merger', 'consolidat', 'centralize', 'decentraliz', 'feudal', 'vassal', 'tributary', 'suzerainty', 'protectorate', 'province', 'provincial', 'colonial rule', 'coloniz', 'settl', 'migrat', 'expansion', 'civilization', 'people', 'inhabit', 'tribe', 'tribal', 'clan', 'indigenous', 'hunter-gatherer', 'nomad', 'pastoral', 'agricultur'] },

    /* ── Migration, settlement, cultural → 531 or 593 ── */
    { div: '531', kw: ['constitution', 'parliament', 'legislative', 'congress', 'assembly established', 'republic declared', 'republic of'] },
    { div: '593', kw: ['trade', 'trading', 'merchant', 'commerce', 'market', 'caravan', 'silk road', 'bazaar', 'import', 'export'] },

    /* ── Cultural & Social Events ── */
    { div: '570', kw: ['church', 'cathedral', 'religion', 'religious', 'convert', 'mission', 'bishop', 'pope', 'monastery', 'temple', 'mosque', 'shrine', 'sacred', 'spiritual', 'pilgrimage', 'worship', 'prayer', 'baptism', 'christening', 'ordain'] },

    /* ── Additional broad catch-alls for remaining 530 entries ── */
    { div: '554', kw: ['UNESCO', 'mound', 'cliff dwelling', 'great house', 'effigy', 'ceremonial', 'serpent', 'stone sphere', 'megalith', 'pitcher', 'basket', 'pottery shard'] },
    { div: '564', kw: ['cultivation', 'woodwork', 'basketry', 'maize', 'pithouse', 'road system'] },
    { div: '592', kw: ['economic', 'economy', 'tax', 'casino', 'financial', 'currency', 'inflation', 'bank', 'debt', 'budget', 'austerity', 'sanctions', 'embargo'] },
    { div: '593', kw: ['oil discover', 'oil export', 'mineral', 'mining', 'lumber', 'fishing', 'plantation'] },
    { div: '517', kw: ['military aid', 'military operation', 'troops', 'killed', 'shooting', 'atrocit', 'crackdown', 'repression'] },
    { div: '524', kw: ['scandal', 'corruption', 'charged', 'fraud', 'deposed', 'removed', 'ousted', 'fled', 'exiled'] },
    { div: '532', kw: ['reform', 'crisis', 'accedes', 'throne', 'marri', 'prince', 'royal', 'submit', 'defeat', 'peacekeeping', 'mediat', 'diplomacy', 'ambassador', 'Nobel', 'award', 'prize'] },
  ],
  '540': [
    { div: '541', kw: ['trial', 'landmark case', 'prosecution', 'sedition trial'] },
    { div: '542', kw: ['international tribunal', 'war crimes', 'nuremberg', 'hague', 'ICC'] },
  ],
  '550': [
    { div: '551', kw: ['astronomical', 'comet', 'eclipse', 'orbit', 'telescope', 'planet', 'star', 'constellation', 'observatory'] },
    { div: '552', kw: ['medical', 'biological', 'vaccine', 'penicillin', 'DNA', 'genome', 'germ theory', 'disease', 'anatomy', 'surgery', 'medicine', 'herbal', 'pharmaceutical', 'antibiotic', 'virus', 'bacteria', 'pathogen'] },
    { div: '553', kw: ['physics', 'chemical', 'atom', 'particle', 'radiation', 'electromagnetic', 'radioactiv', 'nuclear', 'oil', 'petroleum', 'element', 'mineral'] },
    { div: '554', kw: ['archaeological', 'excavat', 'fossil', 'artifact', 'burial', 'cemetery', 'grave', 'tomb', 'ruin', 'ancient site'] },
    /* Cross-division: events misclassified as discoveries */
    { div: '560', kw: ['invention', 'alphabet', 'writing system', 'script', 'printing', 'telegraph', 'telephone', 'radio', 'television'] },
    { div: '532', kw: ['constitutional', 'experiment', 'dissolution'] },
  ],
  '560': [
    { div: '561', kw: ['industrial', 'steam', 'engine', 'factory', 'machine', 'cotton gin', 'textile', 'railroad', 'railway', 'telegraph', 'telephone', 'electric', 'turbine', 'power plant'] },
    { div: '562', kw: ['computer', 'digital', 'internet', 'software', 'processor', 'transistor', 'semiconductor', 'programming'] },
    { div: '563', kw: ['space', 'moon', 'Mars', 'satellite', 'rocket', 'orbital', 'astronaut', 'cosmonaut'] },
    /* Ancient & traditional technology */
    { div: '564', kw: ['weapon', 'club', 'axe', 'spear', 'blade', 'knife', 'bow', 'arrow', 'mace', 'sling', 'atlatl', 'catapult', 'trebuchet', 'crossbow', 'gunpowder', 'cannon', 'sword', 'dagger', 'shield', 'armor', 'tool', 'plough', 'plow', 'wheel', 'forge', 'smelt', 'metallurg', 'bronze', 'iron', 'copper', 'flint', 'obsidian', 'knap', 'fire-harden', 'lever', 'pulley', 'aqueduct', 'irrigat', 'printing press', 'compass', 'astrolabe', 'clock', 'glass', 'mortar', 'cement', 'concrete', 'arch', 'dome', 'vault', 'bridge', 'watermill', 'windmill', 'loom', 'spindle', 'pottery', 'ceramic', 'kiln', 'chariot', 'stirrup', 'saddle', 'harness'] },
    /* Communication & transport */
    { div: '565', kw: ['sail', 'navigation', 'ship', 'boat', 'carriage', 'wagon', 'canal', 'road', 'highway', 'postal', 'courier', 'signal', 'semaphore', 'radio', 'television'] },
    /* Neolithic/general catch-all */
    { div: '564', kw: ['neolithic', 'revolution', 'transition', 'domesticat', 'agricultur'] },
  ],
  '570': [
    /* Cross-division: medical/scientific entries often misclassified as religious */
    { div: '552', kw: ['trepan', 'surgery', 'surgical', 'herbal medicine', 'acupuncture', 'ayurveda', 'pharmacol', 'anatomist', 'rhinoplast', 'papyrus', 'medical', 'physician', 'vaccine', 'penicillin', 'germ theory', 'antiseptic'] },
    { div: '553', kw: ['physics', 'chemical', 'atom', 'particle', 'electromagnetic'] },
    /* Cross-division: political/military events misclassified as religious */
    { div: '517', kw: ['siege of', 'battle of', 'sack of', 'fall of nineveh', 'capture of'] },
    { div: '571', kw: ['council', 'synod', 'conclave', 'ecumenical'] },
    { div: '572', kw: ['reformation', 'schism', 'split', 'protestant', 'great schism', 'reform movement'] },
    { div: '573', kw: ['revival', 'awakening', 'evangelical', 'pentecostal', 'missionary', 'mission'] },
    { div: '574', kw: ['persecution', 'martyr', 'inquisition', 'pogrom', 'crusade against', 'forced conversion', 'heresy trial'] },
    /* Biblical / canonical events */
    { div: '575', kw: ['crucifixion', 'resurrection', 'ascension', 'pentecost', 'nativity', 'transfiguration', 'sermon on the mount', 'last supper', 'passover', 'exodus', 'parting of', 'ten commandments', 'burning bush', 'golden calf', 'flood', 'ark ', 'babel', 'sodom', 'gomorrah', 'manna', 'red sea', 'jordan river', 'jericho', 'canaan', 'tabernacle', 'temple built', 'temple destroyed', 'babylonian exile', 'return from exile', 'second temple'] },
    /* General religious events fallback */
    { div: '576', kw: ['church', 'cathedral', 'monastery', 'abbey', 'mosque', 'temple', 'shrine', 'religion', 'religious', 'sacred', 'holy', 'divine', 'spiritual', 'translation', 'translation movement'] },
  ],
  '580': [
    { div: '581', kw: ['earthquake', 'volcano', 'tsunami', 'flood', 'hurricane', 'cyclone', 'typhoon', 'eruption'] },
    { div: '582', kw: ['famine', 'drought', 'crop failure', 'starvation', 'food shortage'] },
    { div: '583', kw: ['epidemic', 'pandemic', 'plague', 'cholera', 'smallpox', 'influenza', 'covid', 'black death'] },
    { div: '584', kw: ['climate shift', 'ice age', 'little ice age', 'warming', 'desertification'] },
  ],
  '590': [
    { div: '591', kw: ['agricultural revolution', 'green revolution', 'neolithic revolution', 'crop domestication'] },
    { div: '592', kw: ['economic crisis', 'depression', 'recession', 'financial crash', 'hyperinflation', 'debt crisis'] },
    { div: '593', kw: ['trade boom', 'gold rush', 'spice trade', 'rubber boom', 'oil boom'] },
  ],

  // ── Class 6: Movements ──
  '610': [
    /* Cross-division: proto-languages and language families misclassified here → Ideas */
    { div: '153', kw: ['proto-', 'language family', 'linguistic', 'language', 'creole', 'pidgin', 'vernacular', 'script', 'writing system', 'alphabet'] },
    /* Cross-division: artistic/cultural ideas misclassified here */
    { div: '170', kw: ['cave art', 'rock art', 'painting', 'sculpture', 'art movement', 'artistic'] },
    /* Cross-division: technological/tools */
    { div: '560', kw: ['tool', 'weapon', 'spear', 'axe', 'knife', 'bow', 'arrow', 'pottery', 'metallurgy', 'bronze', 'iron', 'copper', 'stone', 'flint', 'obsidian'] },

    { div: '611', kw: ['nationalism', 'nation-building', 'national identity', 'patriotism', 'self-determination'] },
    { div: '612', kw: ['anti-colonial', 'decolonization', 'independence movement', 'liberation movement'] },
    { div: '613', kw: ['communism', 'socialism', 'marxism', 'bolshevism', 'maoism', 'leninist', 'trotskyist'] },
    { div: '614', kw: ['fascism', 'totalitarian', 'nazi', 'authoritarian', 'ultranationalist'] },
    { div: '615', kw: ['liberalism', 'constitutionalism', 'democratic movement', 'whig', 'progressive'] },
    { div: '616', kw: ['pan-african', 'pan-arab', 'pan-islam', 'pan-slav', 'pan-'] },
    /* Broader fallback for political movements */
    { div: '611', kw: ['movement', 'campaign', 'mobilization', 'rally'] },
  ],
  '620': [
    { div: '621', kw: ['abolition', 'anti-slavery', 'emancipation', 'manumission'] },
    { div: '622', kw: ['suffrage', 'feminism', 'women\'s rights', 'gender equality'] },
    { div: '623', kw: ['civil rights', 'racial justice', 'apartheid', 'segregation', 'naacp'] },
    { div: '624', kw: ['labor', 'workers\' rights', 'trade union', 'strike', 'collective bargaining'] },
    { div: '625', kw: ['lgbtq', 'gay rights', 'same-sex', 'sexual orientation'] },
    { div: '626', kw: ['disability', 'inclusion', 'accessible', 'ada'] },
  ],
  '630': [
    { div: '631', kw: ['protestant reformation', 'luther', 'calvin', 'zwingli', '95 theses'] },
    { div: '632', kw: ['counter-reformation', 'catholic reform', 'council of trent', 'jesuit'] },
    { div: '633', kw: ['islamic reform', 'wahhabism', 'salafism', 'islamic revival', 'tanzimat'] },
    { div: '634', kw: ['missionary', 'evangelical', 'proselytiz', 'conversion'] },
    { div: '635', kw: ['new religious movement', 'sect', 'millenarian', 'cargo cult'] },
  ],
  '640': [
    { div: '641', kw: ['renaissance', 'humanism', 'humanist', 'rebirth'] },
    { div: '642', kw: ['enlightenment', 'rationalism', 'reason', 'philosophe'] },
    { div: '643', kw: ['romanticism', 'transcendental', 'romantic era'] },
    { div: '644', kw: ['modernist', 'avant-garde', 'dada', 'surreal', 'abstract'] },
    { div: '645', kw: ['vernacular', 'language movement', 'linguistic revival'] },
  ],
  '650': [
    { div: '651', kw: ['scientific revolution', 'copernican', 'galileo', 'newton'] },
    { div: '652', kw: ['empiricism', 'positivism', 'scientific method'] },
    { div: '653', kw: ['open science', 'peer review', 'reproducib'] },
  ],
  '660': [
    { div: '661', kw: ['industrial revolution', 'industrialization', 'mechanization'] },
    { div: '662', kw: ['digital revolution', 'internet', 'world wide web', 'silicon valley'] },
    { div: '663', kw: ['green tech', 'renewable', 'solar', 'wind power', 'clean energy'] },
  ],
  '670': [
    { div: '671', kw: ['conservation', 'wilderness', 'national park', 'preservation', 'sierra club'] },
    { div: '672', kw: ['climate action', 'sustainability', 'paris agreement', 'kyoto'] },
    { div: '673', kw: ['animal rights', 'wildlife protection', 'endangered species'] },
  ],
  '680': [
    { div: '681', kw: ['silk road', 'overland trade', 'caravan', 'trans-saharan'] },
    { div: '682', kw: ['maritime trade', 'age of sail', 'spice trade', 'naval', 'seafaring'] },
    { div: '683', kw: ['globalization', 'free trade', 'WTO', 'multinational'] },
  ],

  // ── Class 7: Artifacts & Texts ──
  '710': [
    { div: '711', kw: ['ancient code', 'decree', 'edict', 'stele', 'inscription'], eras: ['prehistoric', 'classical'] },
    { div: '712', kw: ['charter', 'concordat', 'magna carta'], eras: ['medieval'] },
    { div: '713', kw: ['modern constitution', 'constitutional'], eras: ['modern', 'contemporary'] },
    { div: '714', kw: ['declaration', 'proclamation', 'manifesto'] },
    /* Broader text classification */
    { div: '711', kw: ['act of', 'law of', 'edict', 'code of', 'decree'], eras: ['prehistoric', 'classical'] },
    { div: '712', kw: ['act of', 'charter', 'statute', 'ordinance'], eras: ['medieval'] },
    { div: '713', kw: ['act of', 'law ', 'statute', 'bill of', 'amendment'], eras: ['early-modern', 'modern', 'contemporary'] },
    /* Constitution catch-all (no era restriction) */
    { div: '713', kw: ['constitution', 'constitutional'] },
    /* Treaty classification */
    { div: '724', kw: ['treaty', 'convention', 'accord', 'agreement', 'pact', 'armistice', 'protocol', 'peace of', 'truce'] },
    /* Charter / act catch-all (no era restriction) */
    { div: '712', kw: ['charter', 'royal charter'] },
    { div: '713', kw: ['act of', 'law ', 'bill of', 'national act'] },
    /* Default: rights documents */
    { div: '714', kw: ['rights', 'freedom', 'liberty', 'emancipation', 'abolition'] },
  ],
  '720': [
    { div: '721', kw: ['hammurabi', 'roman law', 'twelve tables', 'justinian', 'ancient code'] },
    { div: '722', kw: ['canon law', 'decree of gratian', 'sharia', 'halakha'] },
    { div: '723', kw: ['civil code', 'commercial code', 'napoleonic', 'penal code'] },
    { div: '724', kw: ['treaty', 'convention', 'geneva convention', 'hague', 'westphalia'] },
  ],
  '730': [
    { div: '731', kw: ['hebrew bible', 'torah', 'tanakh', 'pentateuch', 'genesis', 'exodus', 'talmud', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', 'samuel', 'kings', 'chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'song of songs', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi', 'book of ', 'old testament', 'wisdom literature', 'prophetic book'] },
    { div: '732', kw: ['new testament', 'gospel', 'epistle', 'revelation', 'acts of', 'pauline', 'matthew', 'mark', 'luke', 'john', 'romans', 'corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', 'thessalonians', 'timothy', 'titus', 'philemon', 'hebrews', 'james', 'peter', 'jude', 'apocalypse'] },
    { div: '733', kw: ['quran', 'qur\'an', 'hadith', 'sunnah', 'islamic text', 'sira', 'tafsir'] },
    { div: '734', kw: ['veda', 'upanishad', 'bhagavad', 'mahabharata', 'ramayana', 'purana', 'dharmasutra'] },
    { div: '735', kw: ['buddhist', 'pali canon', 'tripitaka', 'sutra', 'dharma', 'lotus sutra'] },
    { div: '736', kw: ['sacred text', 'wisdom text', 'avesta', 'guru granth', 'book of the dead', 'zoroastrian', 'confucian text', 'daoist text'] },
  ],
  '740': [
    { div: '741', kw: ['ancient philosophy', 'greek philosophy', 'plato', 'aristotle', 'confucius', 'laozi', 'socrates', 'stoic', 'epicurean'], eras: ['prehistoric', 'classical'] },
    { div: '742', kw: ['scholastic', 'aquinas', 'averroes', 'medieval philosophy', 'maimonides', 'boethius', 'ockham'], eras: ['medieval'] },
    { div: '743', kw: ['enlightenment', 'locke', 'voltaire', 'kant', 'hume', 'rousseau', 'montesquieu', 'descartes'] },
    { div: '744', kw: ['modern philosophy', 'existential', 'phenomenol', 'analytic', 'continental', 'postmodern'] },
    /* Broader keyword matches for philosophical works by topic */
    { div: '785', kw: ['political text', 'polemic', 'pamphlet', 'manifesto', 'treatise on government', 'prince', 'leviathan', 'republic'] },
    { div: '781', kw: ['history', 'historical', 'chronicle', 'annals', 'account of'] },
    { div: '750', kw: ['scientific', 'natural', 'mathematical', 'physics', 'astronomy', 'medicine', 'biology'] },
  ],
  '750': [
    { div: '751', kw: ['mathematical', 'geometry', 'algebra', 'calculus', 'arithmetic'] },
    { div: '752', kw: ['natural history', 'biology', 'botany', 'zoology', 'species'] },
    { div: '753', kw: ['physics', 'astronomy', 'optics', 'principia', 'copernicus'] },
    { div: '754', kw: ['medical', 'pharmacol', 'anatomical', 'herbal', 'materia medica'] },
  ],
  '760': [
    { div: '761', kw: ['painting', 'visual art', 'canvas', 'mural', 'fresco'] },
    { div: '762', kw: ['sculpture', 'monument', 'statue', 'obelisk', 'carved'] },
    { div: '763', kw: ['music', 'composition', 'symphony', 'opera', 'concerto'] },
    { div: '764', kw: ['architecture', 'building', 'temple', 'cathedral', 'palace'] },
  ],
  '770': [
    { div: '771', kw: ['tool', 'instrument', 'device', 'apparatus'] },
    { div: '772', kw: ['weapon', 'armor', 'sword', 'bow', 'gun', 'artillery', 'shield'] },
    { div: '773', kw: ['ship', 'vehicle', 'boat', 'chariot', 'wagon', 'aircraft'] },
    { div: '774', kw: ['machine', 'engine', 'pump', 'mill', 'loom', 'turbine'] },
  ],
  '780': [
    { div: '781', kw: ['history', 'chronicle', 'annals', 'historical account'] },
    { div: '782', kw: ['epic', 'mythology', 'iliad', 'odyssey', 'beowulf', 'saga', 'edda'] },
    { div: '783', kw: ['novel', 'prose fiction', 'literary fiction'] },
    { div: '784', kw: ['travel', 'geography', 'cartograph', 'rihla', 'itinerary'] },
    { div: '785', kw: ['political text', 'polemic', 'pamphlet', 'manifesto', 'treatise on'] },
  ],

  // ── Class 8: Evidence ──
  '810': [
    { div: '811', kw: ['inscription', 'epigraph', 'stele', 'carved text'] },
    { div: '812', kw: ['letter', 'correspondence', 'epistle'] },
    { div: '813', kw: ['official record', 'archive', 'registry', 'census record'] },
    { div: '814', kw: ['diary', 'memoir', 'autobiography', 'personal account'] },
    { div: '815', kw: ['eyewitness', 'firsthand', 'testimony'] },
  ],
  '820': [
    { div: '821', kw: ['monograph', 'academic book', 'scholarly work'] },
    { div: '822', kw: ['journal article', 'peer-reviewed', 'academic paper'] },
    { div: '823', kw: ['encyclopedia', 'reference work', 'dictionary', 'handbook'] },
  ],
  '830': [
    { div: '831', kw: ['excavation', 'dig report', 'archaeological survey'] },
    { div: '832', kw: ['artifact analy', 'pottery', 'ceramic', 'lithic', 'coin'] },
    { div: '833', kw: ['radiocarbon', 'dating', 'dendrochronol', 'stratigraphy'] },
  ],
  '840': [
    { div: '841', kw: ['census', 'demographic', 'population data', 'vital statistics'] },
    { div: '842', kw: ['economic data', 'trade statistic', 'GDP', 'price index'] },
    { div: '843', kw: ['geospatial', 'mapping', 'GIS', 'cartographic data'] },
  ],
  '850': [
    { div: '851', kw: ['oral history', 'interview', 'recorded testimony'] },
    { div: '852', kw: ['folklore', 'myth', 'legend', 'fairy tale', 'oral tradition'] },
    { div: '853', kw: ['genealog', 'lineage', 'family tree', 'dynasty record'] },
  ],

  // ── Class 9: Timeframes ──
  '910': [
    { div: '911', kw: ['paleolithic', 'mesolithic', 'stone age', 'hunter-gatherer'] },
    { div: '912', kw: ['neolithic', 'chalcolithic', 'copper age', 'farming'] },
    { div: '913', kw: ['bronze age', 'bronze'] },
  ],
  '920': [
    { div: '921', kw: ['archaic', 'pre-classical'] },
    { div: '922', kw: ['hellenistic', 'alexander', 'diadochi'] },
    { div: '923', kw: ['roman period', 'roman republic', 'roman empire', 'pax romana'] },
    { div: '924', kw: ['late antiquity', 'late roman', 'fall of rome'] },
  ],
  '930': [
    { div: '931', kw: ['early medieval', 'dark age', 'migration period'] },
    { div: '932', kw: ['high medieval', 'high middle age'] },
    { div: '933', kw: ['late medieval', 'late middle age'] },
  ],
  '940': [
    { div: '941', kw: ['age of exploration', 'age of discovery', 'new world'] },
    { div: '942', kw: ['renaissance period', 'renaissance era'] },
    { div: '943', kw: ['reformation era', 'protestant reform'] },
    { div: '944', kw: ['enlightenment', 'age of reason'] },
  ],
  '950': [
    { div: '951', kw: ['industrial age', 'industrial era'] },
    { div: '952', kw: ['age of empire', 'new imperialism', 'scramble for'] },
    { div: '953', kw: ['interwar', 'between the wars', 'roaring twenties'] },
    { div: '954', kw: ['world war ii era', 'wwii era', 'wartime'] },
  ],
  '960': [
    { div: '961', kw: ['cold war', 'iron curtain', 'bipolar'] },
    { div: '962', kw: ['post-cold war', 'globalization', 'unipolar'] },
    { div: '963', kw: ['digital age', 'information age', 'internet era'] },
  ],
}

/**
 * Extract the base 3-digit division code from a call number.
 * Handles both formats:
 *   - "220.01-slug"  → "220"
 *   - "530.slug"     → "530"
 */
function extractBaseDiv(cn: string): string {
  const dotIdx = cn.indexOf('.')
  if (dotIdx === -1) return cn
  return cn.substring(0, dotIdx)
}

/**
 * Extract the slug portion after the division prefix.
 * "220.01-henry-viii" → "henry-viii"
 * "530.volcanic"      → "volcanic"
 */
function extractSlug(cn: string): string {
  const dotIdx = cn.indexOf('.')
  if (dotIdx === -1) return cn
  const rest = cn.substring(dotIdx + 1)
  // If rest starts with digits followed by '-', strip the serial
  const match = rest.match(/^\d+-(.+)$/)
  return match ? match[1] : rest
}

/** Check if any keyword matches in the combined text (case-insensitive) */
function matchesKeywords(text: string, keywords: string[]): boolean {
  const lower = text.toLowerCase()
  return keywords.some(kw => lower.includes(kw.toLowerCase()))
}

/** Slugs that are pinned to their parent division and exempt from reclassification. */
const PINNED_SLUGS = new Set([
  'legal-codification-traditions',
  'wealth-production-exchange',
  'adjudication-bodies-overview',
  'knowledge-transmission-centers',
  'world-geographic-zones',
  'large-scale-polities-overview',
  'collective-mobilization-for-change',
  'numerical-analysis-in-history',
  'spoken-word-knowledge-systems',
  'early-modern-era-transition',
])

/**
 * Reclassify a single entity's call number to the best matching sub-division.
 * Returns the original call number if no better sub-division is found.
 * Entities in the PINNED_SLUGS set are exempt from reclassification.
 */
export function reclassifyEntity(entity: Entity): string {
  const cn = entity.callNumber

  // Pinned entities are exempt from reclassification
  if (PINNED_SLUGS.has(entity.slug)) return cn

  const baseDiv = extractBaseDiv(cn)
  const rules = RULES[baseDiv]

  // No rules for this division → keep as-is
  if (!rules || rules.length === 0) return cn

  // Build search text from entity metadata
  const searchText = [
    entity.name,
    entity.summary,
    ...(entity.subjects || []),
    ...(entity.subjectHeadings || []),
  ].join(' ')

  const eraSlug = entity.eraSlug || ''

  for (const rule of rules) {
    // Check era filter if specified
    if (rule.eras && !rule.eras.includes(eraSlug)) continue
    // Check keywords
    if (rule.kw && matchesKeywords(searchText, rule.kw)) {
      const slug = extractSlug(cn)
      return `${rule.div}.${slug}`
    }
  }

  return cn // No rule matched — keep parent division
}

/**
 * Reclassify all entities in the catalog to use expanded sub-divisions.
 * Applied as a pipeline step in catalog/index.ts.
 */
export function reclassifyDivisions(entities: Entity[]): Entity[] {
  return entities.map(e => {
    const newCn = reclassifyEntity(e)
    return newCn !== e.callNumber ? { ...e, callNumber: newCn } : e
  })
}
