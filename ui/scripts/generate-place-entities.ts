#!/usr/bin/env npx tsx
/**
 * generate-place-entities.ts
 *
 * Generates comprehensive Place entities for all Class 4 divisions:
 *   410 Continents, 420-428 Regions, 430 Countries/Polities,
 *   440-444 Cities, 450-455 Empires, 460-463 Civilizations,
 *   470-473 Culture Areas
 *
 * Reads country metadata from geo-registry country index files.
 * Outputs to: ui/src/data/catalog/placeEntities.ts
 */
import * as fs from 'fs'
import * as path from 'path'

interface Entity {
  slug: string
  name: string
  label: string
  callNumber: string
  subjectHeadings: string[]
  subjects: string[]
  summary: string
  era: string
  eraSlug: string
  region: string
  continent: string
  status: string
  frameworks: string[]
  causes: { title: string; type: string; year: string; slug?: string }[]
  effects: { title: string; type: string; year: string; slug?: string }[]
  relationships: { sourceSlug: string; sourceName: string; verb: string; targetSlug: string; targetName: string; context?: string }[]
  places: { name: string; role: string; slug?: string }[]
  texts: { title: string; slug?: string }[]
  founded?: string
  period?: string
}

// ── Continent entities (410) ──
const CONTINENTS: Entity[] = [
  {
    slug: 'continent-africa', name: 'Africa', label: 'Place', callNumber: '410.continent-africa',
    subjectHeadings: ['Places — Continents — Africa'], subjects: ['Africa', 'Continent'],
    summary: 'Africa is the second-largest continent, home to 55 nations and the cradle of human civilization. It spans from the Mediterranean coast to the Cape of Good Hope, encompassing the Sahara, the Congo Basin, the Great Rift Valley, and the Nile — the world\'s longest river.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Africa', continent: 'Africa', status: 'Published',
    frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS'],
    causes: [{ title: 'Tectonic formation of the African continent', type: 'Context', year: '' }],
    effects: [{ title: 'Cradle of Homo sapiens and earliest civilizations', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'continent-africa', sourceName: 'Africa', verb: 'CONTAINS', targetSlug: 'nile-valley', targetName: 'Nile Valley', context: 'Continent containing key geographic feature' }],
    places: [{ name: 'Africa', role: 'Continent' }], texts: [],
  },
  {
    slug: 'continent-asia', name: 'Asia', label: 'Place', callNumber: '410.continent-asia',
    subjectHeadings: ['Places — Continents — Asia'], subjects: ['Asia', 'Continent'],
    summary: 'Asia is the largest and most populous continent, stretching from the Ural Mountains to the Pacific. It is home to 48 nations, the Himalayas, the Yangtze and Ganges rivers, and the birthplace of major world religions and ancient civilizations.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Asia', continent: 'Asia', status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'COMPARATIVE_RELIGION'],
    causes: [{ title: 'Continental collision forming the Himalayan orogen', type: 'Context', year: '' }],
    effects: [{ title: 'Emergence of Mesopotamian, Indus Valley, and Chinese civilizations', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'continent-asia', sourceName: 'Asia', verb: 'CONTAINS', targetSlug: 'fertile-crescent', targetName: 'Fertile Crescent', context: 'Continent containing key geographic feature' }],
    places: [{ name: 'Asia', role: 'Continent' }], texts: [],
  },
  {
    slug: 'continent-europe', name: 'Europe', label: 'Place', callNumber: '410.continent-europe',
    subjectHeadings: ['Places — Continents — Europe'], subjects: ['Europe', 'Continent'],
    summary: 'Europe is the second-smallest continent, bounded by the Atlantic, Arctic, and Mediterranean. Home to 44 nations, it was central to the Renaissance, Enlightenment, Industrial Revolution, and the modern state system.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Europe', continent: 'Europe', status: 'Published',
    frameworks: ['POLITICAL_PHILOSOPHY', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Post-glacial settlement of the European peninsula', type: 'Context', year: '' }],
    effects: [{ title: 'Development of Greek democracy and Roman law', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'continent-europe', sourceName: 'Europe', verb: 'CONTAINS', targetSlug: 'rome', targetName: 'Rome', context: 'Continent containing key city' }],
    places: [{ name: 'Europe', role: 'Continent' }], texts: [],
  },
  {
    slug: 'continent-americas', name: 'The Americas', label: 'Place', callNumber: '410.continent-americas',
    subjectHeadings: ['Places — Continents — Americas'], subjects: ['Americas', 'Continent'],
    summary: 'The Americas comprise North and South America, spanning from the Arctic to Patagonia. Home to 35 nations, the continent features the Amazon rainforest, the Andes, the Great Plains, and was the seat of Maya, Aztec, and Inca civilizations.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Americas', continent: 'Americas', status: 'Published',
    frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION', 'COLONIALISM_POSTCOLONIALISM'],
    causes: [{ title: 'Migration across the Bering land bridge', type: 'Context', year: '' }],
    effects: [{ title: 'Rise of Mesoamerican and Andean civilizations', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'continent-americas', sourceName: 'The Americas', verb: 'CONTAINS', targetSlug: 'mesoamerica-region', targetName: 'Mesoamerica', context: 'Continent containing key region' }],
    places: [{ name: 'Americas', role: 'Continent' }], texts: [],
  },
  {
    slug: 'continent-oceania', name: 'Oceania', label: 'Place', callNumber: '410.continent-oceania',
    subjectHeadings: ['Places — Continents — Oceania'], subjects: ['Oceania', 'Continent'],
    summary: 'Oceania encompasses Australia, New Zealand, and the Pacific Islands across Melanesia, Micronesia, and Polynesia. Home to 14 nations and thousands of islands, the region features diverse ecosystems and the world\'s oldest continuous cultures.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Oceania', continent: 'Oceania', status: 'Published',
    frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Austronesian maritime expansion across the Pacific', type: 'Context', year: '' }],
    effects: [{ title: 'Settlement of Polynesian islands and development of navigation traditions', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'continent-oceania', sourceName: 'Oceania', verb: 'CONTAINS', targetSlug: 'polynesian-triangle-region', targetName: 'Polynesian Triangle', context: 'Continent containing key region' }],
    places: [{ name: 'Oceania', role: 'Continent' }], texts: [],
  },
  {
    slug: 'continent-antarctica', name: 'Antarctica', label: 'Place', callNumber: '410.continent-antarctica',
    subjectHeadings: ['Places — Continents — Antarctica'], subjects: ['Antarctica', 'Continent'],
    summary: 'Antarctica is the southernmost continent, a frozen landmass governed by the Antarctic Treaty System. Though uninhabited by permanent populations, it has been the focus of scientific exploration since the 19th century.',
    era: 'Contemporary', eraSlug: 'contemporary', region: 'Antarctica', continent: 'Antarctica', status: 'Published',
    frameworks: ['ENVIRONMENTAL_HISTORY', 'SCIENCE_AND_TECHNOLOGY'],
    causes: [{ title: 'Continental drift separating Antarctica from Gondwana', type: 'Context', year: '' }],
    effects: [{ title: 'Establishment of international research stations', type: 'Outcome', year: '' }],
    relationships: [],
    places: [{ name: 'Antarctica', role: 'Continent' }], texts: [],
  },
]

// ── Region entities (420-428) ──
const REGIONS: Entity[] = [
  { slug: 'region-sub-saharan-africa', name: 'Sub-Saharan Africa', label: 'Place', callNumber: '421.region-sub-saharan-africa',
    subjectHeadings: ['Places — Regions — Sub-Saharan Africa'], subjects: ['Africa', 'Region'],
    summary: 'Sub-Saharan Africa encompasses all African nations south of the Sahara Desert, including West, East, Central, and Southern Africa. Home to great kingdoms like Mali, Songhai, Great Zimbabwe, and the Zulu nation.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Sub-Saharan Africa', continent: 'Africa', status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'],
    causes: [{ title: 'Bantu expansion and agricultural development', type: 'Context', year: '' }],
    effects: [{ title: 'Rise of West African empires and East African trade cities', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-sub-saharan-africa', sourceName: 'Sub-Saharan Africa', verb: 'OCCURS_IN', targetSlug: 'continent-africa', targetName: 'Africa', context: 'Region within continent' }],
    places: [{ name: 'Sub-Saharan Africa', role: 'Region' }], texts: [] },
  { slug: 'region-middle-east-north-africa', name: 'Middle East & North Africa', label: 'Place', callNumber: '422.region-middle-east-north-africa',
    subjectHeadings: ['Places — Regions — Middle East & North Africa'], subjects: ['Middle East', 'North Africa', 'Region'],
    summary: 'The MENA region spans from Morocco to Iran, encompassing the Fertile Crescent, the Arabian Peninsula, and the Nile Valley. Birthplace of agriculture, writing, and the Abrahamic religions.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Middle East', continent: 'Asia', status: 'Published',
    frameworks: ['COMPARATIVE_RELIGION', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Neolithic revolution in the Fertile Crescent', type: 'Context', year: '' }],
    effects: [{ title: 'Rise of Mesopotamian, Egyptian, and Islamic civilizations', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-middle-east-north-africa', sourceName: 'Middle East & North Africa', verb: 'OCCURS_IN', targetSlug: 'continent-asia', targetName: 'Asia', context: 'Region spanning Asia and Africa' }],
    places: [{ name: 'Middle East', role: 'Region' }, { name: 'North Africa', role: 'Region' }], texts: [] },
  { slug: 'region-south-southeast-asia', name: 'South & Southeast Asia', label: 'Place', callNumber: '423.region-south-southeast-asia',
    subjectHeadings: ['Places — Regions — South & Southeast Asia'], subjects: ['South Asia', 'Southeast Asia', 'Region'],
    summary: 'South and Southeast Asia stretches from the Indian subcontinent through the Malay Archipelago. Home to the Indus Valley civilization, the Khmer Empire, and the spice trade routes that connected East and West.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'South Asia', continent: 'Asia', status: 'Published',
    frameworks: ['COMPARATIVE_RELIGION', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Indus Valley urbanization and monsoon agriculture', type: 'Context', year: '' }],
    effects: [{ title: 'Spread of Buddhism and Hinduism across maritime Southeast Asia', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-south-southeast-asia', sourceName: 'South & Southeast Asia', verb: 'OCCURS_IN', targetSlug: 'continent-asia', targetName: 'Asia', context: 'Region within continent' }],
    places: [{ name: 'South Asia', role: 'Region' }, { name: 'Southeast Asia', role: 'Region' }], texts: [] },
  { slug: 'region-east-asia', name: 'East Asia', label: 'Place', callNumber: '424.region-east-asia',
    subjectHeadings: ['Places — Regions — East Asia'], subjects: ['East Asia', 'Region'],
    summary: 'East Asia encompasses China, Japan, Korea, Mongolia, and Taiwan. Home to some of the world\'s oldest continuous civilizations, the invention of paper, printing, gunpowder, and the compass.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'East Asia', continent: 'Asia', status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'SCIENCE_AND_TECHNOLOGY', 'POLITICAL_PHILOSOPHY'],
    causes: [{ title: 'Yellow River valley agriculture and Shang dynasty formation', type: 'Context', year: '' }],
    effects: [{ title: 'Development of Confucian civilization and tributary system', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-east-asia', sourceName: 'East Asia', verb: 'OCCURS_IN', targetSlug: 'continent-asia', targetName: 'Asia', context: 'Region within continent' }],
    places: [{ name: 'East Asia', role: 'Region' }], texts: [] },
  { slug: 'region-europe-western-eastern', name: 'Europe (Western & Eastern)', label: 'Place', callNumber: '425.region-europe-western-eastern',
    subjectHeadings: ['Places — Regions — Europe'], subjects: ['Western Europe', 'Eastern Europe', 'Region'],
    summary: 'Western and Eastern Europe encompass the Mediterranean, the Baltic, the Iberian and Scandinavian peninsulas, the Balkans, and the vast Eastern European plain. From Greek philosophy to the EU, Europe shaped global political thought.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Europe', continent: 'Europe', status: 'Published',
    frameworks: ['POLITICAL_PHILOSOPHY', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Indo-European migrations and Mediterranean urbanization', type: 'Context', year: '' }],
    effects: [{ title: 'Development of democratic institutions and the modern state system', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-europe-western-eastern', sourceName: 'Europe (Western & Eastern)', verb: 'OCCURS_IN', targetSlug: 'continent-europe', targetName: 'Europe', context: 'Region within continent' }],
    places: [{ name: 'Europe', role: 'Region' }], texts: [] },
  { slug: 'region-the-americas', name: 'The Americas', label: 'Place', callNumber: '426.region-the-americas',
    subjectHeadings: ['Places — Regions — The Americas'], subjects: ['Americas', 'Region'],
    summary: 'The Americas span from the Arctic to Tierra del Fuego, encompassing North, Central, and South America. Home to the Maya, Aztec, Inca civilizations, and later the site of European colonization and the formation of modern nation-states.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Americas', continent: 'Americas', status: 'Published',
    frameworks: ['COLONIALISM_POSTCOLONIALISM', 'CULTURAL_DIFFUSION', 'ENVIRONMENTAL_HISTORY'],
    causes: [{ title: 'Migration across Beringia during the last Ice Age', type: 'Context', year: '' }],
    effects: [{ title: 'Development of Mesoamerican and Andean civilizations', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-the-americas', sourceName: 'The Americas', verb: 'OCCURS_IN', targetSlug: 'continent-americas', targetName: 'The Americas', context: 'Region within continent' }],
    places: [{ name: 'Americas', role: 'Region' }], texts: [] },
  { slug: 'region-oceania-pacific', name: 'Oceania & Pacific', label: 'Place', callNumber: '427.region-oceania-pacific',
    subjectHeadings: ['Places — Regions — Oceania & Pacific'], subjects: ['Oceania', 'Pacific', 'Region'],
    summary: 'Oceania and the Pacific encompasses Australia, New Zealand, Melanesia, Micronesia, and Polynesia — thousands of islands spread across the world\'s largest ocean. Austronesian navigators settled these islands over millennia using celestial navigation.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Oceania', continent: 'Oceania', status: 'Published',
    frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'],
    causes: [{ title: 'Austronesian expansion from Taiwan across the Pacific', type: 'Context', year: '' }],
    effects: [{ title: 'Settlement of Polynesia and development of wayfinding traditions', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-oceania-pacific', sourceName: 'Oceania & Pacific', verb: 'OCCURS_IN', targetSlug: 'continent-oceania', targetName: 'Oceania', context: 'Region within continent' }],
    places: [{ name: 'Oceania', role: 'Region' }], texts: [] },
  { slug: 'region-central-asia-steppe', name: 'Central Asia & Steppe', label: 'Place', callNumber: '428.region-central-asia-steppe',
    subjectHeadings: ['Places — Regions — Central Asia & Steppe'], subjects: ['Central Asia', 'Steppe', 'Region'],
    summary: 'Central Asia and the Eurasian Steppe stretches from the Caspian Sea to Mongolia. This vast grassland corridor was the highway of nomadic empires — Scythians, Huns, Turks, Mongols — and the land route of the Silk Road.',
    era: 'Prehistoric', eraSlug: 'prehistoric', region: 'Central Asia', continent: 'Asia', status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'MILITARY_HISTORY'],
    causes: [{ title: 'Horse domestication on the Pontic-Caspian steppe', type: 'Context', year: '' }],
    effects: [{ title: 'Rise of nomadic empires and Silk Road trade networks', type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: 'region-central-asia-steppe', sourceName: 'Central Asia & Steppe', verb: 'OCCURS_IN', targetSlug: 'continent-asia', targetName: 'Asia', context: 'Region within continent' }],
    places: [{ name: 'Central Asia', role: 'Region' }], texts: [] },
]

// ── City entities (440-444) ──
interface CityDef {
  slug: string; name: string; division: string; summary: string; region: string; continent: string;
  era: string; eraSlug: string; subjects: string[]; frameworks: string[];
  cause: string; effect: string; founded?: string;
}

const CITIES: CityDef[] = [
  // 440 - General Cities
  { slug: 'city-cairo', name: 'Cairo', division: '440', summary: 'Capital of Egypt and the largest city in the Arab world, founded near the ancient city of Memphis. Home to Al-Azhar University and the Egyptian Museum.', region: 'North Africa', continent: 'Africa', era: 'Medieval', eraSlug: 'medieval', subjects: ['Egypt', 'Cities'], frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS'], cause: 'Fatimid conquest of Egypt', effect: 'Center of Islamic scholarship and trade', founded: '969 CE' },
  { slug: 'city-beijing', name: 'Beijing', division: '441', summary: 'Capital of China for most of the last millennium, seat of the Ming and Qing dynasties, and home to the Forbidden City.', region: 'East Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['China', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Mongol selection as capital of the Yuan dynasty', effect: 'Center of Chinese imperial governance for 800 years', founded: '1271 CE' },
  { slug: 'city-paris', name: 'Paris', division: '441', summary: 'Capital of France, center of medieval Christendom, the Enlightenment, and the French Revolution. Home to Notre-Dame, the Sorbonne, and the Louvre.', region: 'Western Europe', continent: 'Europe', era: 'Medieval', eraSlug: 'medieval', subjects: ['France', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Gallo-Roman settlement on the Île de la Cité', effect: 'Intellectual and cultural capital of Europe', founded: '3rd century BCE' },
  { slug: 'city-london', name: 'London', division: '441', summary: 'Capital of England and the United Kingdom, founded as Londinium by the Romans. Hub of the British Empire, the Industrial Revolution, and global finance.', region: 'Northern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['United Kingdom', 'Capital Cities'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Roman founding of Londinium c. 43 CE', effect: 'Center of the world\'s largest maritime empire', founded: '43 CE' },
  { slug: 'city-tokyo', name: 'Tokyo', division: '441', summary: 'Capital of Japan since the Meiji Restoration, formerly Edo. The world\'s largest metropolitan area and center of Japanese culture and technology.', region: 'East Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Japan', 'Capital Cities'], frameworks: ['ECONOMIC_SYSTEMS', 'SCIENCE_AND_TECHNOLOGY'], cause: 'Tokugawa shoguns establishing Edo as seat of power', effect: 'Transformation into modern global megacity', founded: '1457 CE' },
  { slug: 'city-moscow', name: 'Moscow', division: '441', summary: 'Capital of Russia, center of Orthodox Christianity, and heart of both the Russian Empire and the Soviet Union. Home to the Kremlin and Red Square.', region: 'Eastern Europe', continent: 'Europe', era: 'Medieval', eraSlug: 'medieval', subjects: ['Russia', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY', 'MILITARY_HISTORY'], cause: 'Foundation by Yuri Dolgorukiy in the 12th century', effect: 'Rise of Moscow as the Third Rome and center of Slavic civilization', founded: '1147 CE' },
  { slug: 'city-delhi', name: 'Delhi', division: '441', summary: 'Capital of India, seat of numerous empires from the Delhi Sultanate to the Mughal Empire to the British Raj. One of the world\'s oldest continuously inhabited cities.', region: 'South Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['India', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Strategic location at the intersection of Indo-Gangetic plain trade routes', effect: 'Center of successive imperial capitals for over 1000 years', founded: '736 CE' },
  { slug: 'city-washington-dc', name: 'Washington, D.C.', division: '441', summary: 'Capital of the United States, purpose-built as the seat of the federal government. Home to the White House, Capitol, and Smithsonian Institution.', region: 'North America', continent: 'Americas', era: 'Modern', eraSlug: 'modern', subjects: ['United States', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY'], cause: 'Constitutional establishment of a federal district', effect: 'Center of American democratic governance and global diplomacy', founded: '1790 CE' },
  { slug: 'city-kyoto', name: 'Kyoto', division: '441', summary: 'Former capital of Japan for over a millennium (794-1868), center of Japanese art, culture, Zen Buddhism, and the imperial court.', region: 'East Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Japan', 'Capital Cities'], frameworks: ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Emperor Kanmu relocating the capital from Nara', effect: 'Flowering of Japanese classical culture and Zen aesthetics', founded: '794 CE' },
  { slug: 'city-canberra', name: 'Canberra', division: '441', summary: 'Capital of Australia, purpose-built in the early 20th century as a compromise between Sydney and Melbourne. Seat of the Australian Parliament.', region: 'Oceania', continent: 'Oceania', era: 'Contemporary', eraSlug: 'contemporary', subjects: ['Australia', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY'], cause: 'Federation of Australia requiring a neutral capital', effect: 'Administrative center of Australian governance', founded: '1913 CE' },
  { slug: 'city-addis-ababa', name: 'Addis Ababa', division: '441', summary: 'Capital of Ethiopia, seat of the African Union, and the diplomatic capital of Africa. Founded by Emperor Menelik II.', region: 'East Africa', continent: 'Africa', era: 'Modern', eraSlug: 'modern', subjects: ['Ethiopia', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Emperor Menelik II seeking a permanent capital', effect: 'Center of pan-African diplomacy and the African Union', founded: '1886 CE' },
  { slug: 'city-brasilia', name: 'Brasília', division: '441', summary: 'Capital of Brazil, a planned modernist city designed by Oscar Niemeyer and Lúcio Costa. UNESCO World Heritage Site and symbol of Brazilian modernization.', region: 'South America', continent: 'Americas', era: 'Contemporary', eraSlug: 'contemporary', subjects: ['Brazil', 'Capital Cities'], frameworks: ['POLITICAL_PHILOSOPHY'], cause: 'Brazilian desire to develop the interior and move the capital from Rio', effect: 'Symbol of modernist urban planning and national development', founded: '1960 CE' },

  // 442 - Port Cities & Trade Hubs
  { slug: 'city-alexandria-port', name: 'Alexandria', division: '442', summary: 'Egyptian port city founded by Alexander the Great in 331 BCE. Home to the Great Library and the Lighthouse (Pharos), one of the Seven Wonders. A cosmopolitan center of Hellenistic learning and Mediterranean trade.', region: 'North Africa', continent: 'Africa', era: 'Classical', eraSlug: 'classical', subjects: ['Egypt', 'Port Cities', 'Trade'], frameworks: ['CULTURAL_DIFFUSION', 'SCIENCE_AND_TECHNOLOGY', 'ECONOMIC_SYSTEMS'], cause: 'Alexander the Great\'s conquest of Egypt', effect: 'Center of Hellenistic scholarship and Mediterranean commerce', founded: '331 BCE' },
  { slug: 'city-shanghai', name: 'Shanghai', division: '442', summary: 'China\'s largest city and one of the world\'s busiest ports. Rose to prominence in the 19th century as a treaty port and became a global financial center.', region: 'East Asia', continent: 'Asia', era: 'Modern', eraSlug: 'modern', subjects: ['China', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Opening as a treaty port after the First Opium War', effect: 'Development into Asia\'s premier financial and commercial hub', founded: '1074 CE' },
  { slug: 'city-mumbai', name: 'Mumbai', division: '442', summary: 'India\'s financial capital and largest port, formerly Bombay. Gateway of India and center of the Bollywood film industry.', region: 'South Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['India', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Portuguese and later British colonial development', effect: 'India\'s commercial and entertainment capital', founded: '1507 CE' },
  { slug: 'city-istanbul-port', name: 'Istanbul', division: '442', summary: 'Straddling Europe and Asia at the Bosphorus, Istanbul (formerly Constantinople and Byzantium) has been the world\'s most strategic port city for 2,600 years. Capital of three empires.', region: 'West Asia', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Turkey', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION', 'MILITARY_HISTORY'], cause: 'Greek colonists founding Byzantion at the Bosphorus', effect: 'Control of trade between the Mediterranean and Black Sea for millennia', founded: '660 BCE' },
  { slug: 'city-singapore', name: 'Singapore', division: '442', summary: 'Island city-state at the tip of the Malay Peninsula, one of the world\'s busiest ports and a global financial center. Strategic crossroads of Indian Ocean and Pacific trade.', region: 'Southeast Asia', continent: 'Asia', era: 'Modern', eraSlug: 'modern', subjects: ['Singapore', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS'], cause: 'Stamford Raffles establishing a British trading post', effect: 'Transformation into a global trade and financial hub', founded: '1819 CE' },
  { slug: 'city-zanzibar', name: 'Zanzibar', division: '442', summary: 'Island port off the East African coast, center of the Indian Ocean spice trade and the Swahili trading network. Notorious for its role in the slave trade.', region: 'East Africa', continent: 'Africa', era: 'Medieval', eraSlug: 'medieval', subjects: ['Tanzania', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Persian and Arab traders establishing settlements', effect: 'Hub of the Indian Ocean spice and slave trade', founded: '8th century CE' },
  { slug: 'city-lisbon', name: 'Lisbon', division: '442', summary: 'Capital of Portugal and launching point of the Age of Exploration. Vasco da Gama, Magellan, and other explorers departed from its harbor to chart new sea routes.', region: 'Southern Europe', continent: 'Europe', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Portugal', 'Port Cities', 'Exploration'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Portuguese maritime ambition and Prince Henry the Navigator', effect: 'Establishment of the first global maritime empire', founded: '1200 BCE' },
  { slug: 'city-new-york', name: 'New York City', division: '442', summary: 'The largest city in the United States, founded as New Amsterdam by the Dutch. Global center of finance, media, culture, and immigration — the gateway city of the New World.', region: 'North America', continent: 'Americas', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['United States', 'Port Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Dutch West India Company establishing New Amsterdam', effect: 'Rise to global financial and cultural capital', founded: '1626 CE' },

  // 443 - Holy Cities & Pilgrimage Sites
  { slug: 'city-varanasi', name: 'Varanasi', division: '443', summary: 'One of the world\'s oldest continuously inhabited cities and the holiest city in Hinduism. Sacred to Buddhists as the site of Buddha\'s first sermon at Sarnath. A center of Sanskrit learning on the banks of the Ganges.', region: 'South Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['India', 'Holy Cities', 'Hinduism', 'Buddhism'], frameworks: ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Ancient Hindu belief in the sanctity of the Ganges confluence', effect: 'Continuous religious pilgrimage for 3,000 years', founded: '11th century BCE' },
  { slug: 'city-bodh-gaya', name: 'Bodh Gaya', division: '443', summary: 'Site of the Bodhi Tree where Siddhartha Gautama attained enlightenment and became the Buddha. The most sacred pilgrimage site in Buddhism.', region: 'South Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['India', 'Holy Cities', 'Buddhism'], frameworks: ['COMPARATIVE_RELIGION'], cause: 'Buddha\'s meditation under the Bodhi Tree c. 528 BCE', effect: 'Establishment of Buddhism and continuous Buddhist pilgrimage', founded: '528 BCE' },
  { slug: 'city-lhasa', name: 'Lhasa', division: '443', summary: 'Holy city of Tibetan Buddhism, seat of the Dalai Lama, and home to the Potala Palace. Center of Tibetan cultural and spiritual life for 1,400 years.', region: 'East Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Tibet', 'China', 'Holy Cities', 'Buddhism'], frameworks: ['COMPARATIVE_RELIGION', 'POLITICAL_PHILOSOPHY'], cause: 'King Songtsen Gampo establishing Lhasa as capital and Buddhist center', effect: 'Center of Tibetan Buddhist civilization and governance', founded: '7th century CE' },
  { slug: 'city-santiago-de-compostela', name: 'Santiago de Compostela', division: '443', summary: 'Destination of the Camino de Santiago, one of Christianity\'s most important pilgrimage routes. Believed to house the relics of the apostle St. James.', region: 'Southern Europe', continent: 'Europe', era: 'Medieval', eraSlug: 'medieval', subjects: ['Spain', 'Holy Cities', 'Christianity'], frameworks: ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Discovery of relics attributed to St. James in the 9th century', effect: 'Creation of Europe\'s most important medieval pilgrimage route', founded: '9th century CE' },

  // 444 - Ancient & Ruined Cities
  { slug: 'city-mohenjo-daro', name: 'Mohenjo-daro', division: '444', summary: 'One of the largest cities of the Indus Valley Civilization, remarkable for its advanced urban planning, drainage systems, and the Great Bath. Abandoned around 1900 BCE.', region: 'South Asia', continent: 'Asia', era: 'Prehistoric', eraSlug: 'prehistoric', subjects: ['Pakistan', 'Ancient Cities', 'Archaeology'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'ENVIRONMENTAL_HISTORY'], cause: 'Indus Valley Civilization\'s urban development along the Indus River', effect: 'Evidence of sophisticated Bronze Age urban planning and water management', founded: '2500 BCE' },
  { slug: 'city-persepolis', name: 'Persepolis', division: '444', summary: 'Ceremonial capital of the Achaemenid Empire, built by Darius I. Its magnificent ruins with relief carvings depict the diversity of the Persian Empire. Burned by Alexander in 330 BCE.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Iran', 'Ancient Cities', 'Archaeology'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Darius I establishing a grand ceremonial capital', effect: 'Symbol of Achaemenid imperial power and multicultural governance', founded: '515 BCE' },
  { slug: 'city-carthage', name: 'Carthage', division: '444', summary: 'Phoenician city-state and maritime empire in present-day Tunisia. Rome\'s greatest rival in the Punic Wars, destroyed in 146 BCE and later rebuilt as a Roman colony.', region: 'North Africa', continent: 'Africa', era: 'Classical', eraSlug: 'classical', subjects: ['Tunisia', 'Ancient Cities', 'Trade'], frameworks: ['MILITARY_HISTORY', 'ECONOMIC_SYSTEMS'], cause: 'Phoenician colonists from Tyre founding a trading settlement', effect: 'Punic Wars that shaped the Mediterranean world order', founded: '814 BCE' },
  { slug: 'city-teotihuacan', name: 'Teotihuacán', division: '444', summary: 'The largest city in pre-Columbian Americas, with the Pyramid of the Sun and the Avenue of the Dead. At its peak, home to over 100,000 people. Mysteriously abandoned around 550 CE.', region: 'Central America', continent: 'Americas', era: 'Classical', eraSlug: 'classical', subjects: ['Mexico', 'Ancient Cities', 'Archaeology'], frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Volcanic eruption forcing population migration to the Basin of Mexico', effect: 'Cultural influence on subsequent Mesoamerican civilizations including the Aztecs', founded: '100 BCE' },
  { slug: 'city-angkor', name: 'Angkor', division: '444', summary: 'Capital of the Khmer Empire in present-day Cambodia. The vast temple complex of Angkor Wat is the largest religious monument ever built. The city supported nearly a million people.', region: 'Southeast Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Cambodia', 'Ancient Cities', 'Archaeology'], frameworks: ['COMPARATIVE_RELIGION', 'ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Jayavarman II unifying the Khmer kingdom and establishing divine kingship', effect: 'Construction of the world\'s largest pre-industrial urban complex', founded: '802 CE' },
  { slug: 'city-great-zimbabwe', name: 'Great Zimbabwe', division: '444', summary: 'Medieval stone city in southern Africa, capital of the Kingdom of Zimbabwe. Its massive stone enclosures are the largest ancient structures south of the Sahara.', region: 'Southern Africa', continent: 'Africa', era: 'Medieval', eraSlug: 'medieval', subjects: ['Zimbabwe', 'Ancient Cities', 'Archaeology'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Shona kingdom\'s control of gold and Indian Ocean trade routes', effect: 'Evidence of sophisticated African urban civilization and long-distance trade', founded: '11th century CE' },
  { slug: 'city-petra', name: 'Petra', division: '444', summary: 'Ancient Nabataean city carved into rose-red sandstone cliffs in present-day Jordan. A major caravan trade hub controlling routes between Arabia, Egypt, and the Mediterranean.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Jordan', 'Ancient Cities', 'Trade'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Nabataean control of Arabian incense trade routes', effect: 'Architectural masterpiece blending Hellenistic, Egyptian, and Arabian styles', founded: '4th century BCE' },
  { slug: 'city-machu-picchu', name: 'Machu Picchu', division: '444', summary: 'Inca citadel set high in the Andes of Peru, built in the 15th century and abandoned during the Spanish Conquest. One of the most iconic archaeological sites in the world.', region: 'South America', continent: 'Americas', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Peru', 'Ancient Cities', 'Archaeology'], frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Emperor Pachacuti\'s construction of a royal estate', effect: 'Symbol of Inca engineering genius and Andean civilization', founded: '1450 CE' },
]

// ── Empire entities (450-455) ──
interface EmpireDef {
  slug: string; name: string; division: string; summary: string; region: string; continent: string;
  era: string; eraSlug: string; subjects: string[]; frameworks: string[];
  cause: string; effect: string; period?: string;
}

const EMPIRES: EmpireDef[] = [
  // 451 - Ancient Empires
  { slug: 'empire-egyptian-old-kingdom', name: 'Egyptian Old Kingdom', division: '451', summary: 'The Age of the Pyramids (c. 2686-2181 BCE). The Third through Sixth Dynasties built the Great Pyramids of Giza and established Egypt as the first great territorial state.', region: 'North Africa', continent: 'Africa', era: 'Classical', eraSlug: 'classical', subjects: ['Egypt', 'Ancient Empires'], frameworks: ['POLITICAL_PHILOSOPHY', 'SCIENCE_AND_TECHNOLOGY'], cause: 'Unification of Upper and Lower Egypt under the pharaohs', effect: 'Construction of the Great Pyramids and development of hieroglyphic writing', period: '2686 BCE – 2181 BCE' },
  { slug: 'empire-neo-assyrian', name: 'Neo-Assyrian Empire', division: '451', summary: 'The first true world empire, controlling Mesopotamia, Egypt, and the Levant. Known for its military innovations, library of Ashurbanipal, and forced deportation policies.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Iraq', 'Syria', 'Ancient Empires'], frameworks: ['MILITARY_HISTORY', 'POLITICAL_PHILOSOPHY'], cause: 'Assyrian military reforms and iron-age weapons technology', effect: 'First empire to control Egypt and Mesopotamia simultaneously', period: '911 BCE – 609 BCE' },
  { slug: 'empire-neo-babylonian', name: 'Neo-Babylonian Empire', division: '451', summary: 'Empire of Nebuchadnezzar II, builder of the Hanging Gardens and the Ishtar Gate. Conquered Jerusalem in 586 BCE, beginning the Babylonian Captivity of the Jews.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Iraq', 'Ancient Empires'], frameworks: ['COMPARATIVE_RELIGION', 'POLITICAL_PHILOSOPHY'], cause: 'Chaldean revolt against Assyrian rule', effect: 'Babylonian Captivity of the Jews and flourishing of Babylonian astronomy', period: '626 BCE – 539 BCE' },

  // 452 - Classical Empires
  { slug: 'empire-achaemenid-persia', name: 'Achaemenid Persian Empire', division: '452', summary: 'Founded by Cyrus the Great, the largest empire the world had yet seen. Known for the Royal Road, satrapy system, and the Cyrus Cylinder — the first declaration of human rights.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Iran', 'Classical Empires'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Cyrus the Great\'s rebellion against the Median Empire', effect: 'Model of multicultural imperial governance and religious tolerance', period: '550 BCE – 330 BCE' },
  { slug: 'empire-macedonian', name: 'Macedonian Empire of Alexander', division: '452', summary: 'Alexander the Great\'s empire stretched from Greece to India, spreading Hellenistic culture across the known world. After his death, it fractured into the Ptolemaic, Seleucid, and Antigonid kingdoms.', region: 'Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Greece', 'Classical Empires'], frameworks: ['CULTURAL_DIFFUSION', 'MILITARY_HISTORY'], cause: 'Philip II\'s unification of Greece and Alexander\'s ambition', effect: 'Hellenistic civilization spreading Greek language and culture to Asia', period: '336 BCE – 323 BCE' },
  { slug: 'empire-maurya', name: 'Maurya Empire', division: '452', summary: 'First empire to unify most of the Indian subcontinent, founded by Chandragupta Maurya. Emperor Ashoka\'s conversion to Buddhism and his rock edicts promoted nonviolence and dharma.', region: 'South Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['India', 'Classical Empires'], frameworks: ['COMPARATIVE_RELIGION', 'POLITICAL_PHILOSOPHY'], cause: 'Chandragupta\'s victory over the Nanda dynasty with Chanakya\'s guidance', effect: 'Ashoka\'s dharma edicts and spread of Buddhism across Asia', period: '322 BCE – 185 BCE' },
  { slug: 'empire-roman', name: 'Roman Empire', division: '452', summary: 'One of the most influential empires in world history, encompassing the entire Mediterranean. Its legal system, engineering, Latin language, and eventual adoption of Christianity shaped Western civilization.', region: 'Southern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Italy', 'Classical Empires'], frameworks: ['POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION', 'MILITARY_HISTORY'], cause: 'Transformation from republic to empire under Augustus', effect: 'Roman law, Latin language, and Christianity shaping European civilization', period: '27 BCE – 476 CE' },
  { slug: 'empire-han-dynasty', name: 'Han Dynasty', division: '452', summary: 'China\'s second imperial dynasty, rivaling Rome in power and extent. Established the Silk Road, Confucian meritocracy, paper-making, and the civil service examination system.', region: 'East Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['China', 'Classical Empires'], frameworks: ['ECONOMIC_SYSTEMS', 'SCIENCE_AND_TECHNOLOGY', 'POLITICAL_PHILOSOPHY'], cause: 'Liu Bang\'s victory in the Chu-Han contention after Qin collapse', effect: 'Establishment of Confucian governance model lasting 2,000 years', period: '206 BCE – 220 CE' },
  { slug: 'empire-gupta', name: 'Gupta Empire', division: '452', summary: 'India\'s Golden Age, marked by advances in mathematics (zero, decimal system), astronomy, literature (Kalidasa), and art. Hinduism flourished as a refined religious and cultural system.', region: 'South Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['India', 'Classical Empires'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Chandragupta I\'s consolidation of the Magadha region', effect: 'Invention of the zero and decimal number system', period: '320 CE – 550 CE' },

  // 453 - Medieval Empires
  { slug: 'empire-byzantine', name: 'Byzantine Empire', division: '453', summary: 'The Eastern Roman Empire, surviving for over a millennium after the fall of Rome. Preserved classical knowledge, codified Roman law (Justinian\'s Code), and spread Orthodox Christianity.', region: 'Southern Europe', continent: 'Europe', era: 'Medieval', eraSlug: 'medieval', subjects: ['Turkey', 'Greece', 'Medieval Empires'], frameworks: ['COMPARATIVE_RELIGION', 'POLITICAL_PHILOSOPHY', 'CULTURAL_DIFFUSION'], cause: 'Constantine\'s founding of Constantinople as the eastern capital', effect: 'Preservation of classical heritage and transmission to the Islamic world and Renaissance Europe', period: '330 CE – 1453 CE' },
  { slug: 'empire-umayyad-caliphate', name: 'Umayyad Caliphate', division: '453', summary: 'The first hereditary Islamic dynasty, expanding the caliphate from Spain to Central Asia — the fifth-largest empire in history. Built the Dome of the Rock and the Great Mosque of Damascus.', region: 'West Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Syria', 'Spain', 'Medieval Empires'], frameworks: ['COMPARATIVE_RELIGION', 'MILITARY_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Muawiya\'s consolidation of power after the First Fitna', effect: 'Arabization and Islamization of the Middle East and North Africa', period: '661 CE – 750 CE' },
  { slug: 'empire-abbasid-caliphate', name: 'Abbasid Caliphate', division: '453', summary: 'The Islamic Golden Age caliphate centered on Baghdad. Patronized the House of Wisdom, which translated Greek, Persian, and Indian works, preserving knowledge that later sparked the European Renaissance.', region: 'West Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Iraq', 'Medieval Empires'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION'], cause: 'Abbasid Revolution overthrowing the Umayyads', effect: 'Islamic Golden Age and preservation of classical knowledge', period: '750 CE – 1258 CE' },
  { slug: 'empire-tang-dynasty', name: 'Tang Dynasty', division: '453', summary: 'Considered the golden age of Chinese civilization. The Tang capital Chang\'an was the world\'s largest city. Poetry (Li Bai, Du Fu), Buddhism, and Silk Road trade flourished.', region: 'East Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['China', 'Medieval Empires'], frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS'], cause: 'Li Yuan\'s founding after the Sui dynasty collapse', effect: 'Peak of Chinese cultural influence across East and Central Asia', period: '618 CE – 907 CE' },
  { slug: 'empire-mali', name: 'Mali Empire', division: '453', summary: 'West African empire that controlled trans-Saharan gold and salt trade. Under Mansa Musa, the world\'s richest person, it established Timbuktu as a center of Islamic learning.', region: 'West Africa', continent: 'Africa', era: 'Medieval', eraSlug: 'medieval', subjects: ['Mali', 'Medieval Empires'], frameworks: ['ECONOMIC_SYSTEMS', 'COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Sundiata Keita\'s defeat of the Sosso and founding of the empire', effect: 'Timbuktu as a center of learning and Mansa Musa\'s famous hajj', period: '1235 CE – 1600 CE' },
  { slug: 'empire-khmer', name: 'Khmer Empire', division: '453', summary: 'Southeast Asian empire centered on Angkor, building the largest pre-industrial city and the temple of Angkor Wat. Mastered hydraulic engineering to manage monsoon water.', region: 'Southeast Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Cambodia', 'Medieval Empires'], frameworks: ['ENVIRONMENTAL_HISTORY', 'COMPARATIVE_RELIGION'], cause: 'Jayavarman II establishing the cult of the devaraja (god-king)', effect: 'Construction of Angkor Wat and the largest urban water management system', period: '802 CE – 1431 CE' },

  // 454 - Early Modern Empires
  { slug: 'empire-ottoman', name: 'Ottoman Empire', division: '454', summary: 'One of the longest-lasting empires in history, spanning southeastern Europe, western Asia, and northern Africa. Conquered Constantinople in 1453 and held the Islamic caliphate until 1924.', region: 'West Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Turkey', 'Early Modern Empires'], frameworks: ['POLITICAL_PHILOSOPHY', 'COMPARATIVE_RELIGION', 'MILITARY_HISTORY'], cause: 'Osman I founding a beylik on the Byzantine frontier', effect: 'Multi-ethnic, multi-religious imperial model lasting 600 years', period: '1299 CE – 1922 CE' },
  { slug: 'empire-mughal', name: 'Mughal Empire', division: '454', summary: 'Central Asian-origin dynasty that ruled most of the Indian subcontinent. Built the Taj Mahal, Red Fort, and established a synthesis of Persian, Turkic, and Indian cultures. India\'s GDP reached 24% of the world under Mughal rule.', region: 'South Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['India', 'Early Modern Empires'], frameworks: ['CULTURAL_DIFFUSION', 'ECONOMIC_SYSTEMS', 'COMPARATIVE_RELIGION'], cause: 'Babur\'s invasion from Central Asia, descending from both Timur and Genghis Khan', effect: 'Mughal architectural masterpieces and Indo-Islamic cultural synthesis', period: '1526 CE – 1857 CE' },
  { slug: 'empire-ming-dynasty', name: 'Ming Dynasty', division: '454', summary: 'Chinese dynasty that restored Han Chinese rule, built the Forbidden City, reconstructed the Great Wall, and sent Zheng He\'s treasure fleets across the Indian Ocean.', region: 'East Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['China', 'Early Modern Empires'], frameworks: ['ECONOMIC_SYSTEMS', 'SCIENCE_AND_TECHNOLOGY'], cause: 'Zhu Yuanzhang\'s peasant rebellion overthrowing Mongol Yuan dynasty', effect: 'Chinese maritime exploration and porcelain trade golden age', period: '1368 CE – 1644 CE' },
  { slug: 'empire-safavid', name: 'Safavid Empire', division: '454', summary: 'Persian empire that established Twelver Shia Islam as the state religion of Iran. Under Shah Abbas I, Isfahan became one of the world\'s most beautiful cities.', region: 'West Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Iran', 'Early Modern Empires'], frameworks: ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Shah Ismail I\'s unification of Iran under Shia Islam', effect: 'Permanent Shia identity of Iran and Persian cultural renaissance', period: '1501 CE – 1736 CE' },
  { slug: 'empire-songhai', name: 'Songhai Empire', division: '454', summary: 'The largest empire in African history, succeeding Mali and controlling trans-Saharan trade. Under Askia Muhammad, Timbuktu and Djenné became centers of Islamic scholarship.', region: 'West Africa', continent: 'Africa', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Mali', 'Niger', 'Early Modern Empires'], frameworks: ['ECONOMIC_SYSTEMS', 'COMPARATIVE_RELIGION'], cause: 'Sunni Ali\'s expansion from the city of Gao', effect: 'Peak of West African Islamic scholarship and trans-Saharan trade', period: '1464 CE – 1591 CE' },

  // 455 - Colonial Empires
  { slug: 'empire-spanish-colonial', name: 'Spanish Colonial Empire', division: '455', summary: 'The first global empire, spanning the Americas, Philippines, and parts of Africa and Oceania. Conquered the Aztec and Inca empires and established the first transatlantic trade system.', region: 'Southern Europe', continent: 'Europe', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Spain', 'Colonial Empires'], frameworks: ['COLONIALISM_POSTCOLONIALISM', 'ECONOMIC_SYSTEMS'], cause: 'Columbus\'s 1492 voyage and the Treaty of Tordesillas', effect: 'Destruction of Mesoamerican civilizations and creation of Latin American cultures', period: '1492 CE – 1975 CE' },
  { slug: 'empire-british-colonial', name: 'British Empire', division: '455', summary: 'The largest empire in human history at its peak, encompassing a quarter of the world\'s land and population. Spread the English language, common law, parliamentary democracy, and industrial capitalism worldwide.', region: 'Northern Europe', continent: 'Europe', era: 'Modern', eraSlug: 'modern', subjects: ['United Kingdom', 'Colonial Empires'], frameworks: ['COLONIALISM_POSTCOLONIALISM', 'ECONOMIC_SYSTEMS', 'POLITICAL_PHILOSOPHY'], cause: 'English maritime expansion and defeat of the Spanish Armada', effect: 'Global spread of English language, common law, and parliamentary institutions', period: '1583 CE – 1997 CE' },
  { slug: 'empire-french-colonial', name: 'French Colonial Empire', division: '455', summary: 'Second-largest colonial empire, spanning North and West Africa, Indochina, the Caribbean, and the Pacific. Spread the French language, civil law, and revolutionary ideals.', region: 'Western Europe', continent: 'Europe', era: 'Modern', eraSlug: 'modern', subjects: ['France', 'Colonial Empires'], frameworks: ['COLONIALISM_POSTCOLONIALISM', 'POLITICAL_PHILOSOPHY'], cause: 'French exploration and rivalry with Britain and Spain', effect: 'Francophone world and French civil law tradition across Africa and Asia', period: '1534 CE – 1980 CE' },
  { slug: 'empire-dutch-colonial', name: 'Dutch Colonial Empire', division: '455', summary: 'Maritime trading empire centered on the Dutch East India Company (VOC), the first multinational corporation. Controlled Indonesian spice islands, South Africa, and parts of the Americas.', region: 'Western Europe', continent: 'Europe', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Netherlands', 'Colonial Empires'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'Dutch revolt against Spain and rise of Amsterdam as a financial center', effect: 'Creation of modern financial capitalism and the first stock exchange', period: '1602 CE – 1975 CE' },
  { slug: 'empire-portuguese-colonial', name: 'Portuguese Colonial Empire', division: '455', summary: 'The first and longest-lasting European colonial empire. Pioneered the Age of Exploration, establishing trading posts from Brazil to Macau, and dominating the Indian Ocean spice trade.', region: 'Southern Europe', continent: 'Europe', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Portugal', 'Colonial Empires'], frameworks: ['COLONIALISM_POSTCOLONIALISM', 'ECONOMIC_SYSTEMS'], cause: 'Prince Henry the Navigator\'s sponsorship of maritime exploration', effect: 'First global maritime trade network and Lusophone world', period: '1415 CE – 1999 CE' },
]

// ── Civilization entities (460-463) ──
const CIVILIZATIONS: EmpireDef[] = [
  // 461 - River Valley Civilizations
  { slug: 'civ-sumerian', name: 'Sumerian Civilization', division: '461', summary: 'The world\'s first civilization, arising in southern Mesopotamia between the Tigris and Euphrates. Invented writing (cuneiform), the wheel, the plow, the sexagesimal number system (base-60), and the first code of laws.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Iraq', 'River Valley Civilizations'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'POLITICAL_PHILOSOPHY'], cause: 'Agricultural surplus in the fertile floodplain of the Tigris-Euphrates', effect: 'Invention of writing, law, and urban civilization', period: '4500 BCE – 1900 BCE' },
  { slug: 'civ-ancient-egyptian', name: 'Ancient Egyptian Civilization', division: '461', summary: 'One of the world\'s longest-lasting civilizations, centered on the Nile River. Built the pyramids, developed hieroglyphic writing, and created a sophisticated system of religion, medicine, and astronomy spanning 3,000 years.', region: 'North Africa', continent: 'Africa', era: 'Classical', eraSlug: 'classical', subjects: ['Egypt', 'River Valley Civilizations'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'COMPARATIVE_RELIGION'], cause: 'Predictable Nile flooding enabling agricultural surplus', effect: 'Monumental architecture (pyramids) and a continuous 3,000-year civilization', period: '3100 BCE – 30 BCE' },
  { slug: 'civ-indus-valley', name: 'Indus Valley Civilization', division: '461', summary: 'One of the three earliest urban civilizations, with major cities at Harappa and Mohenjo-daro. Remarkable for advanced urban planning, standardized weights and measures, and an undeciphered script.', region: 'South Asia', continent: 'Asia', era: 'Prehistoric', eraSlug: 'prehistoric', subjects: ['India', 'Pakistan', 'River Valley Civilizations'], frameworks: ['SCIENCE_AND_TECHNOLOGY', 'ECONOMIC_SYSTEMS'], cause: 'Agricultural development along the Indus River and its tributaries', effect: 'First large-scale urban planning with sewage and water management', period: '3300 BCE – 1300 BCE' },
  { slug: 'civ-shang-dynasty', name: 'Shang Dynasty Civilization', division: '461', summary: 'China\'s first historically verified dynasty, centered on the Yellow River. Developed oracle bone script (the ancestor of Chinese characters), sophisticated bronze casting, and ancestral worship rituals.', region: 'East Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['China', 'River Valley Civilizations'], frameworks: ['COMPARATIVE_RELIGION', 'SCIENCE_AND_TECHNOLOGY'], cause: 'Agricultural communities along the Yellow River developing bronze technology', effect: 'Chinese writing system and the foundation of Chinese dynastic civilization', period: '1600 BCE – 1046 BCE' },

  // 462 - Maritime & Island Civilizations
  { slug: 'civ-minoan', name: 'Minoan Civilization', division: '462', summary: 'Europe\'s first advanced civilization, centered on Crete. Known for the palace of Knossos, vibrant frescoes, maritime trade networks, and the undeciphered Linear A script.', region: 'Southern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Greece', 'Maritime Civilizations'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Strategic island location and control of Mediterranean sea trade', effect: 'Inspiration for Greek mythology (Minotaur, Labyrinth) and later Greek civilization', period: '2700 BCE – 1450 BCE' },
  { slug: 'civ-phoenician', name: 'Phoenician Civilization', division: '462', summary: 'Maritime traders who invented the alphabet — the ancestor of Greek, Latin, Arabic, and Hebrew scripts. Their city-states (Tyre, Sidon, Byblos) dominated Mediterranean trade and founded Carthage.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Lebanon', 'Maritime Civilizations'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION', 'SCIENCE_AND_TECHNOLOGY'], cause: 'Limited agricultural hinterland driving maritime expertise', effect: 'Invention of the alphabet and establishment of Mediterranean trade networks', period: '1500 BCE – 300 BCE' },
  { slug: 'civ-polynesian', name: 'Polynesian Civilization', division: '462', summary: 'Master navigators who settled the vast Pacific Ocean using celestial navigation, ocean swells, and bird flight patterns. From Hawaii to New Zealand to Easter Island — the largest migration in human history by sea.', region: 'Oceania', continent: 'Oceania', era: 'Medieval', eraSlug: 'medieval', subjects: ['Polynesia', 'Maritime Civilizations'], frameworks: ['ENVIRONMENTAL_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Austronesian maritime expansion and double-hulled canoe technology', effect: 'Settlement of the most dispersed island chain on Earth', period: '1000 BCE – 1200 CE' },

  // 463 - Steppe & Nomadic Civilizations
  { slug: 'civ-scythian', name: 'Scythian Civilization', division: '463', summary: 'Nomadic warriors and master horsemen of the Eurasian steppe. Known for their elaborate gold artwork (Scythian animal style), mounted archery, and control of trade routes from the Black Sea to China.', region: 'Central Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Central Asia', 'Steppe Civilizations'], frameworks: ['MILITARY_HISTORY', 'CULTURAL_DIFFUSION'], cause: 'Horse domestication and mastery of mounted warfare', effect: 'Spread of horse-riding culture across Eurasia and the Animal Style art tradition', period: '900 BCE – 200 BCE' },
  { slug: 'civ-xiongnu', name: 'Xiongnu Confederation', division: '463', summary: 'Powerful nomadic confederation on China\'s northern frontier. Their raids prompted the construction of the Great Wall and the Han dynasty\'s Silk Road diplomacy.', region: 'East Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Mongolia', 'China', 'Steppe Civilizations'], frameworks: ['MILITARY_HISTORY', 'ECONOMIC_SYSTEMS'], cause: 'Unification of Mongolian steppe tribes under Modu Chanyu', effect: 'Great Wall construction and opening of the Silk Road', period: '209 BCE – 93 CE' },
  { slug: 'civ-mongol', name: 'Mongol Civilization', division: '463', summary: 'Under Genghis Khan and his successors, the Mongols built the largest contiguous land empire in history. The Pax Mongolica enabled unprecedented exchange across Eurasia.', region: 'Central Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Mongolia', 'Steppe Civilizations'], frameworks: ['MILITARY_HISTORY', 'ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Genghis Khan\'s unification of the Mongol tribes', effect: 'Pax Mongolica enabling transcontinental trade and cultural exchange', period: '1206 CE – 1368 CE' },
]

// ── Culture Areas (470-473) ──
const CULTURE_AREAS: CityDef[] = [
  // 471 - Trade Routes & Corridors
  { slug: 'route-silk-road', name: 'Silk Road', division: '471', summary: 'Ancient network of trade routes connecting China to the Mediterranean via Central Asia. For over 1,500 years, it carried silk, spices, ideas, religions (Buddhism, Islam, Christianity), and technologies between East and West.', region: 'Central Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Trade Routes', 'Central Asia', 'China'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION', 'COMPARATIVE_RELIGION'], cause: 'Han dynasty diplomacy and demand for Western horses', effect: 'Transmission of Buddhism, Islam, paper, and gunpowder across Eurasia' },
  { slug: 'route-trans-saharan', name: 'Trans-Saharan Trade Routes', division: '471', summary: 'Network of caravan routes across the Sahara Desert connecting sub-Saharan Africa with the Mediterranean. Carried gold, salt, slaves, and Islamic learning, sustaining empires like Ghana, Mali, and Songhai.', region: 'North Africa', continent: 'Africa', era: 'Medieval', eraSlug: 'medieval', subjects: ['Trade Routes', 'West Africa', 'North Africa'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Introduction of the camel to the Sahara enabling long-distance trade', effect: 'Rise of West African empires and spread of Islam south of the Sahara' },
  { slug: 'route-indian-ocean', name: 'Indian Ocean Trade Network', division: '471', summary: 'Maritime trade network connecting East Africa, Arabia, India, Southeast Asia, and China. Driven by monsoon winds, it was the world\'s largest trading zone before the Age of Exploration.', region: 'South Asia', continent: 'Asia', era: 'Medieval', eraSlug: 'medieval', subjects: ['Trade Routes', 'Indian Ocean'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Knowledge of monsoon wind patterns enabling regular voyages', effect: 'Swahili coast city-states and spread of Islam to Southeast Asia' },
  { slug: 'route-incense-route', name: 'Incense Route', division: '471', summary: 'Ancient trade route from southern Arabia (Yemen/Oman) through the Arabian Peninsula to the Mediterranean, carrying frankincense and myrrh — commodities more valuable than gold in the ancient world.', region: 'West Asia', continent: 'Asia', era: 'Classical', eraSlug: 'classical', subjects: ['Trade Routes', 'Arabia'], frameworks: ['ECONOMIC_SYSTEMS'], cause: 'Demand for frankincense and myrrh in Egyptian, Greek, and Roman temples', effect: 'Wealth of the Nabataean, Sabaean, and Himyarite kingdoms' },
  { slug: 'route-spice-route', name: 'Spice Routes', division: '471', summary: 'Maritime and overland routes carrying cinnamon, pepper, cloves, and nutmeg from Southeast Asia to Europe. The quest for spices drove the Age of Exploration and European colonization.', region: 'Southeast Asia', continent: 'Asia', era: 'Early Modern', eraSlug: 'early-modern', subjects: ['Trade Routes', 'Southeast Asia', 'India'], frameworks: ['ECONOMIC_SYSTEMS', 'COLONIALISM_POSTCOLONIALISM'], cause: 'European demand for Asian spices and Ottoman control of overland routes', effect: 'Portuguese discovery of the sea route to India and European colonization of Asia' },
  { slug: 'route-amber-road', name: 'Amber Road', division: '471', summary: 'Ancient trade route connecting the Baltic Sea to the Mediterranean, carrying amber — fossilized tree resin prized across the ancient world. Linked Germanic, Celtic, Greek, and Roman civilizations.', region: 'Northern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Trade Routes', 'Europe'], frameworks: ['ECONOMIC_SYSTEMS', 'CULTURAL_DIFFUSION'], cause: 'Mediterranean demand for Baltic amber as precious material', effect: 'Cultural exchange between Northern and Southern Europe' },

  // 472 - Sacred Landscapes & Monuments
  { slug: 'sacred-ganges-river', name: 'Ganges River', division: '472', summary: 'The holiest river in Hinduism, believed to flow from heaven. Over 400 million people live in its basin. Varanasi, Allahabad, and Haridwar on its banks are among India\'s most sacred pilgrimage sites.', region: 'South Asia', continent: 'Asia', era: 'Prehistoric', eraSlug: 'prehistoric', subjects: ['India', 'Sacred Landscapes', 'Hinduism'], frameworks: ['COMPARATIVE_RELIGION', 'ENVIRONMENTAL_HISTORY'], cause: 'Hindu cosmology identifying the Ganges as a divine river', effect: 'Continuous pilgrimage and ritual tradition for 3,000+ years' },
  { slug: 'sacred-mount-sinai', name: 'Mount Sinai', division: '472', summary: 'The mountain where, according to the Torah, Moses received the Ten Commandments from God. Sacred to Judaism, Christianity, and Islam as the site of divine revelation.', region: 'North Africa', continent: 'Africa', era: 'Classical', eraSlug: 'classical', subjects: ['Egypt', 'Sacred Landscapes', 'Judaism', 'Christianity', 'Islam'], frameworks: ['COMPARATIVE_RELIGION'], cause: 'Biblical narrative of the Exodus and divine covenant', effect: 'Foundation of Mosaic law and Abrahamic moral tradition' },
  { slug: 'sacred-mount-olympus', name: 'Mount Olympus', division: '472', summary: 'The highest mountain in Greece, believed to be the home of the twelve Olympian gods. Central to Greek mythology, religion, and the cultural imagination of Western civilization.', region: 'Southern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Greece', 'Sacred Landscapes', 'Greek Religion'], frameworks: ['COMPARATIVE_RELIGION', 'CULTURAL_DIFFUSION'], cause: 'Greek mythological tradition placing the gods on the highest peak', effect: 'Foundation of Greek religious practice and Western literary tradition' },
  { slug: 'sacred-uluru', name: 'Uluru (Ayers Rock)', division: '472', summary: 'Sacred sandstone monolith in central Australia, central to the Dreamtime stories of the Anangu Aboriginal people. One of the world\'s most recognizable natural landmarks and a symbol of Australia\'s Indigenous heritage.', region: 'Oceania', continent: 'Oceania', era: 'Prehistoric', eraSlug: 'prehistoric', subjects: ['Australia', 'Sacred Landscapes', 'Indigenous Peoples'], frameworks: ['COMPARATIVE_RELIGION', 'ENVIRONMENTAL_HISTORY'], cause: 'Aboriginal Dreamtime creation narratives', effect: 'Continuous Indigenous spiritual practice for 30,000+ years' },

  // 473 - Battlefields & Conflict Zones
  { slug: 'battlefield-thermopylae', name: 'Thermopylae', division: '473', summary: 'Narrow coastal pass in Greece where 300 Spartans and their allies made a legendary last stand against Xerxes\' Persian invasion in 480 BCE. One of history\'s most famous battles.', region: 'Southern Europe', continent: 'Europe', era: 'Classical', eraSlug: 'classical', subjects: ['Greece', 'Battlefields'], frameworks: ['MILITARY_HISTORY'], cause: 'Xerxes\' invasion of Greece with a massive Persian army', effect: 'Spartan sacrifice inspiring Greek resistance and eventual Persian defeat' },
  { slug: 'battlefield-hastings', name: 'Battle of Hastings (1066)', division: '473', summary: 'The Norman conquest of England, where William the Conqueror defeated King Harold II. Transformed English language, law, and society, creating the Anglo-Norman ruling class.', region: 'Northern Europe', continent: 'Europe', era: 'Medieval', eraSlug: 'medieval', subjects: ['United Kingdom', 'Battlefields'], frameworks: ['MILITARY_HISTORY', 'POLITICAL_PHILOSOPHY'], cause: 'Disputed English succession after Edward the Confessor\'s death', effect: 'Norman transformation of English language, law, architecture, and governance' },
  { slug: 'battlefield-waterloo', name: 'Battle of Waterloo (1815)', division: '473', summary: 'Napoleon\'s final defeat by the Duke of Wellington and Blücher near Brussels. Ended the Napoleonic Wars and reshaped the European state system at the Congress of Vienna.', region: 'Western Europe', continent: 'Europe', era: 'Modern', eraSlug: 'modern', subjects: ['Belgium', 'France', 'Battlefields'], frameworks: ['MILITARY_HISTORY', 'POLITICAL_PHILOSOPHY'], cause: 'Napoleon\'s return from Elba and the Hundred Days', effect: 'Concert of Europe and a century of relative peace' },
  { slug: 'battlefield-normandy', name: 'D-Day Beaches, Normandy (1944)', division: '473', summary: 'The beaches of Normandy where the Allied invasion of occupied Europe (Operation Overlord) began on June 6, 1944. The largest amphibious invasion in history, turning the tide of World War II.', region: 'Western Europe', continent: 'Europe', era: 'Contemporary', eraSlug: 'contemporary', subjects: ['France', 'Battlefields', 'World War II'], frameworks: ['MILITARY_HISTORY'], cause: 'Allied strategic decision to open a second front in Western Europe', effect: 'Liberation of France and eventual Allied victory in Europe' },
]

// ── Country entities (430) — read from geo-registry ──
function loadCountryEntities(): Entity[] {
  const geoBase = path.resolve(__dirname, '../../geo-registry/places/countries')
  const dirs = fs.readdirSync(geoBase).filter(d => {
    const full = path.join(geoBase, d)
    return fs.statSync(full).isDirectory() && d !== '_template'
  }).sort()

  const entities: Entity[] = []

  for (const slug of dirs) {
    const idxPath = path.join(geoBase, slug, 'index.json')
    if (!fs.existsSync(idxPath)) continue

    const data = JSON.parse(fs.readFileSync(idxPath, 'utf8'))
    const meta = data._meta || {}
    const profile = data.country_profile || {}

    const countryName = meta.country_name || slug.replace(/-/g, ' ').replace(/\b\w/g, (c: string) => c.toUpperCase())
    const region = (meta.region || 'Global').replace(/_/g, ' ')
    const continent = meta.continent || 'Global'
    const capital = profile.capital || ''
    const languages = (profile.official_languages || []).slice(0, 3).join(', ')
    const govType = profile.government_type || ''
    const population = profile.population?.estimate
    const area = profile.area_km2
    const notes = meta.notes || ''

    // Build summary
    let summary = `${countryName} is a sovereign nation in ${region}, ${continent}.`
    if (capital) summary += ` Its capital is ${capital}.`
    if (languages) summary += ` Official languages include ${languages}.`
    if (govType) summary += ` Government: ${govType}.`
    if (population) summary += ` Population: approximately ${(population / 1_000_000).toFixed(1)} million.`
    if (area) summary += ` Area: ${area.toLocaleString()} km².`
    if (notes) summary += ` ${notes}`

    const entity: Entity = {
      slug: `country-${slug}`,
      name: countryName,
      label: 'Place',
      callNumber: `430.country-${slug}`,
      subjectHeadings: [`Places — Countries — ${countryName} — ${continent}`],
      subjects: [countryName, continent, region, 'Countries'],
      summary: summary.slice(0, 9900),
      era: 'Contemporary',
      eraSlug: 'contemporary',
      region,
      continent,
      status: 'Published',
      frameworks: ['POLITICAL_PHILOSOPHY', 'ECONOMIC_SYSTEMS'],
      causes: [{ title: `Historical formation of ${countryName}`, type: 'Context', year: '' }],
      effects: [{ title: `${countryName} as a contemporary sovereign state`, type: 'Outcome', year: '' }],
      relationships: [
        { sourceSlug: `country-${slug}`, sourceName: countryName, verb: 'OCCURS_IN', targetSlug: `continent-${continent.toLowerCase().replace(/\s+/g, '-')}`, targetName: continent, context: `${countryName} located in ${continent}` },
      ],
      places: [{ name: countryName, role: 'Country' }],
      texts: [],
    }

    if (capital) {
      entity.places.push({ name: capital, role: 'Capital' })
    }

    entities.push(entity)
  }

  return entities
}

// ── Convert simple definitions to Entity ──
function cityDefToEntity(c: CityDef): Entity {
  return {
    slug: c.slug, name: c.name, label: 'Place', callNumber: `${c.division}.${c.slug}`,
    subjectHeadings: [`Places — ${c.subjects[1] || 'Cities'} — ${c.name} — ${c.continent}`],
    subjects: [...c.subjects, c.continent], summary: c.summary,
    era: c.era, eraSlug: c.eraSlug, region: c.region, continent: c.continent, status: 'Published',
    frameworks: c.frameworks,
    causes: [{ title: c.cause, type: 'Context', year: '' }],
    effects: [{ title: c.effect, type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: c.slug, sourceName: c.name, verb: 'OCCURS_IN', targetSlug: `continent-${c.continent.toLowerCase().replace(/\s+/g, '-')}`, targetName: c.continent, context: `${c.name} located in ${c.continent}` }],
    places: [{ name: c.name, role: 'Location' }], texts: [],
    ...(c.founded ? { founded: c.founded } : {}),
  }
}

function empireDefToEntity(e: EmpireDef): Entity {
  return {
    slug: e.slug, name: e.name, label: 'Place', callNumber: `${e.division}.${e.slug}`,
    subjectHeadings: [`Places — ${e.subjects[e.subjects.length - 1]} — ${e.name}`],
    subjects: [...e.subjects, e.continent], summary: e.summary,
    era: e.era, eraSlug: e.eraSlug, region: e.region, continent: e.continent, status: 'Published',
    frameworks: e.frameworks,
    causes: [{ title: e.cause, type: 'Context', year: '' }],
    effects: [{ title: e.effect, type: 'Outcome', year: '' }],
    relationships: [{ sourceSlug: e.slug, sourceName: e.name, verb: 'OCCURS_IN', targetSlug: `continent-${e.continent.toLowerCase().replace(/\s+/g, '-')}`, targetName: e.continent, context: `${e.name} in ${e.continent}` }],
    places: [{ name: e.region, role: 'Region' }], texts: [],
    ...(e.period ? { period: e.period } : {}),
  }
}

// ── Main ──
const countryEntities = loadCountryEntities()
const cityEntities = CITIES.map(cityDefToEntity)
const empireEntities = EMPIRES.map(empireDefToEntity)
const civEntities = CIVILIZATIONS.map(empireDefToEntity)
const cultureEntities = CULTURE_AREAS.map(cityDefToEntity)

const ALL: Entity[] = [
  ...CONTINENTS,
  ...REGIONS,
  ...countryEntities,
  ...cityEntities,
  ...empireEntities,
  ...civEntities,
  ...cultureEntities,
]

// Check for duplicate slugs
const slugSet = new Set<string>()
const dupes: string[] = []
for (const e of ALL) {
  if (slugSet.has(e.slug)) dupes.push(e.slug)
  slugSet.add(e.slug)
}
if (dupes.length > 0) {
  console.error('DUPLICATE SLUGS:', dupes)
  process.exit(1)
}

// ── Write TypeScript output ──
const lines: string[] = []
lines.push(`/**`)
lines.push(` * Place Entities — ${ALL.length} entities across all Class 4 (Places) divisions.`)
lines.push(` * Auto-generated by scripts/generate-place-entities.ts`)
lines.push(` *`)
lines.push(` * Coverage:`)
lines.push(` *   410 Continents: ${CONTINENTS.length}`)
lines.push(` *   420-428 Regions: ${REGIONS.length}`)
lines.push(` *   430 Countries: ${countryEntities.length}`)
lines.push(` *   440-444 Cities: ${cityEntities.length}`)
lines.push(` *   450-455 Empires: ${empireEntities.length}`)
lines.push(` *   460-463 Civilizations: ${civEntities.length}`)
lines.push(` *   470-473 Culture Areas: ${cultureEntities.length}`)
lines.push(` */`)
lines.push(`import type { Entity } from '../entityTypes'`)
lines.push(``)
lines.push(`export const placeEntities: Entity[] = [`)

for (const e of ALL) {
  lines.push(`  {`)
  lines.push(`    slug: ${JSON.stringify(e.slug)},`)
  lines.push(`    name: ${JSON.stringify(e.name)},`)
  lines.push(`    label: ${JSON.stringify(e.label)},`)
  lines.push(`    callNumber: ${JSON.stringify(e.callNumber)},`)
  lines.push(`    subjectHeadings: ${JSON.stringify(e.subjectHeadings)},`)
  lines.push(`    subjects: ${JSON.stringify(e.subjects)},`)
  lines.push(`    summary: ${JSON.stringify(e.summary)},`)
  lines.push(`    era: ${JSON.stringify(e.era)},`)
  lines.push(`    eraSlug: ${JSON.stringify(e.eraSlug)},`)
  lines.push(`    region: ${JSON.stringify(e.region)},`)
  lines.push(`    continent: ${JSON.stringify(e.continent)},`)
  lines.push(`    status: ${JSON.stringify(e.status)},`)
  lines.push(`    frameworks: ${JSON.stringify(e.frameworks)},`)
  lines.push(`    causes: ${JSON.stringify(e.causes)},`)
  lines.push(`    effects: ${JSON.stringify(e.effects)},`)
  lines.push(`    relationships: ${JSON.stringify(e.relationships)},`)
  lines.push(`    places: ${JSON.stringify(e.places)},`)
  lines.push(`    texts: ${JSON.stringify(e.texts)},`)
  if (e.founded) lines.push(`    founded: ${JSON.stringify(e.founded)},`)
  if (e.period) lines.push(`    period: ${JSON.stringify(e.period)},`)
  lines.push(`  },`)
}

lines.push(`]`)

const outPath = path.resolve(__dirname, '../src/data/catalog/placeEntities.ts')
fs.writeFileSync(outPath, lines.join('\n') + '\n', 'utf8')

console.log(`\n=== Place Entity Generation Complete ===`)
console.log(`Total: ${ALL.length} entities`)
console.log(`  Continents (410): ${CONTINENTS.length}`)
console.log(`  Regions (420-428): ${REGIONS.length}`)
console.log(`  Countries (430): ${countryEntities.length}`)
console.log(`  Cities (440-444): ${cityEntities.length}`)
console.log(`  Empires (450-455): ${empireEntities.length}`)
console.log(`  Civilizations (460-463): ${civEntities.length}`)
console.log(`  Culture Areas (470-473): ${cultureEntities.length}`)
console.log(`\nOutput: ${outPath}`)
console.log(`Duplicate slugs: ${dupes.length}`)
