/* ──────────────────────────────────────────────────────────────────────────
   Transportation — Every revolutionary mode of transport from
   dugout canoes to spacecraft across 10,000 years of human mobility.
   ────────────────────────────────────────────────────────────────────────── */

export interface Transportation {
  slug: string
  name: string
  era: string
  category: string
  subcategory: string
  origin: string
  civilization: string
  yearIntroduced: string
  description: string
  impact: string
}

export interface TransportCategory {
  id: string
  label: string
  color: string
  icon: string
}

export const TRANSPORT_CATEGORIES: TransportCategory[] = [
  { id: 'land',      label: 'Land & Road',            color: '#8B4513', icon: 'Route' },
  { id: 'water',     label: 'Water & Maritime',        color: '#4A90D9', icon: 'Ship' },
  { id: 'rail',      label: 'Rail & Trains',           color: '#718096', icon: 'TrainFront' },
  { id: 'air',       label: 'Aviation & Flight',       color: '#6B3FA0', icon: 'Plane' },
  { id: 'space',     label: 'Space Travel',            color: '#2D2A24', icon: 'Rocket' },
  { id: 'animal',    label: 'Animal-Powered Transport',          color: '#38A169', icon: 'Horse' },
  { id: 'urban',     label: 'City Transit & Public Transport',   color: '#DD6B20', icon: 'Bus' },
  { id: 'trade',     label: 'Historic Trade Routes & Networks',  color: '#C53030', icon: 'Globe' },
]

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const TRANSPORTATION: Transportation[] = [
  // ═══════════════════════════════════════════════════════
  // PREHISTORIC — Before 3,000 BCE
  // ═══════════════════════════════════════════════════════

  { slug: 'dugout-canoe', name: 'Dugout Canoe', era: 'prehistoric', category: 'water', subcategory: 'Early Watercraft', origin: 'Multiple Regions', civilization: 'Various', yearIntroduced: '~8,000 BCE', description: 'Hollowed-out tree trunks were humanity\'s first boats. The Pesse canoe (Netherlands, ~8,000 BCE) is the oldest surviving watercraft. Simple but revolutionary — they opened rivers, lakes, and coastlines to travel and trade.', impact: 'Enabled human settlement along waterways and coastlines. The foundation of all maritime technology.' },

  { slug: 'domestication-of-donkey', name: 'Domestication of the Donkey', era: 'prehistoric', category: 'animal', subcategory: 'Beast of Burden', origin: 'Northeast Africa', civilization: 'Nubian / Egyptian', yearIntroduced: '~5,000 BCE', description: 'Wild African asses were domesticated in Nubia and Egypt, becoming humanity\'s first beast of burden. Donkeys could carry 60 kg across desert terrain and survive on minimal water.', impact: 'Enabled long-distance overland trade in arid regions. Without donkeys, early Saharan and Nile trade networks could not have existed.' },

  { slug: 'domestication-of-horse', name: 'Domestication of the Horse', era: 'prehistoric', category: 'animal', subcategory: 'Riding & Cavalry', origin: 'Pontic-Caspian Steppe', civilization: 'Botai / Yamnaya', yearIntroduced: '~4,000 BCE', description: 'Horses were domesticated on the Eurasian steppe, initially for milk and meat. By ~3,500 BCE, humans were riding them. The horse multiplied human speed 5x and transformed warfare, trade, and migration.', impact: 'The most transformative animal domestication in history. Horses reshaped every aspect of civilization — warfare, agriculture, communication, and empire.' },

  { slug: 'wheel-invention', name: 'The Wheel', era: 'prehistoric', category: 'land', subcategory: 'Fundamental Innovation', origin: 'Mesopotamia / Pontic Steppe', civilization: 'Sumerian / Yamnaya', yearIntroduced: '~3,500 BCE', description: 'The wheel appeared almost simultaneously in Mesopotamia and the Eurasian steppe. The key innovation wasn\'t the wheel itself but the axle — fitting a rotating wheel to a fixed platform required sophisticated engineering.', impact: 'The most important mechanical invention in human history. Every vehicle, machine, and gear mechanism descends from this breakthrough.' },

  { slug: 'ox-cart', name: 'Ox Cart', era: 'prehistoric', category: 'land', subcategory: 'Wheeled Vehicles', origin: 'Mesopotamia', civilization: 'Sumerian', yearIntroduced: '~3,200 BCE', description: 'The first wheeled vehicles were heavy four-wheeled carts pulled by oxen. Slow (2 km/h) but able to transport heavy loads — grain, building materials, trade goods — across flat terrain.', impact: 'Created overland bulk transport for the first time. Enabled cities to be supplied from distant farms.' },

  { slug: 'reed-boat', name: 'Reed Boat', era: 'prehistoric', category: 'water', subcategory: 'Early Watercraft', origin: 'Mesopotamia / Egypt', civilization: 'Sumerian / Egyptian', yearIntroduced: '~5,000 BCE', description: 'Boats woven from papyrus reeds or bulrushes. Light, buoyant, and easy to build — they served as fishing boats, ferries, and cargo vessels on the Nile, Tigris, and Euphrates rivers.', impact: 'Made river civilizations possible. The Nile and Tigris-Euphrates were highways of the ancient world.' },

  { slug: 'sled-and-travois', name: 'Sled & Travois', era: 'prehistoric', category: 'land', subcategory: 'Pre-Wheel Transport', origin: 'Multiple Regions', civilization: 'Various', yearIntroduced: '~7,000 BCE', description: 'Before wheels, sleds on runners and A-frame travois dragged by dogs or humans moved goods across snow, sand, and grasslands. Used from Scandinavia to the Great Plains of North America.', impact: 'Proved that land transport was possible without wheels. Native Americans used travois for millennia with no need for the wheel.' },

  { slug: 'outrigger-canoe', name: 'Outrigger Canoe', era: 'prehistoric', category: 'water', subcategory: 'Ocean-Going Vessels', origin: 'Southeast Asia / Pacific', civilization: 'Austronesian', yearIntroduced: '~3,000 BCE', description: 'A stabilizing float (outrigger) attached to a canoe via spars allowed open-ocean sailing. This simple innovation turned fragile canoes into seaworthy vessels capable of crossing thousands of kilometers.', impact: 'Enabled the Austronesian expansion — the colonization of the Pacific, Madagascar, and every island from Taiwan to Easter Island.' },

  // ═══════════════════════════════════════════════════════
  // ANCIENT — 3,000 BCE – 500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'war-chariot', name: 'War Chariot', era: 'ancient', category: 'land', subcategory: 'Horse-Drawn Vehicles', origin: 'Central Asia / Near East', civilization: 'Indo-European / Egyptian', yearIntroduced: '~2,000 BCE', description: 'Light two-wheeled chariots with spoked wheels revolutionized warfare. Egyptian, Hittite, Shang Chinese, and Indian armies all fielded chariot corps. The Battle of Kadesh (1274 BCE) featured 5,000+ chariots.', impact: 'The first mobile weapons platform. Chariot-using peoples conquered most of Eurasia between 2000–1000 BCE.' },

  { slug: 'trireme', name: 'Trireme', era: 'ancient', category: 'water', subcategory: 'Warships', origin: 'Greece', civilization: 'Greek', yearIntroduced: '~700 BCE', description: 'A three-tiered oared warship that could reach 14 knots (26 km/h) — the fastest vessel in the ancient world. The Athenian navy of 200 triremes defeated the Persian fleet at Salamis (480 BCE) and secured Greek freedom.', impact: 'Proved that sea power could decide the fate of civilizations. Athens\' democracy was powered by the rowers of its triremes.' },

  { slug: 'roman-roads', name: 'Roman Road Network', era: 'ancient', category: 'trade', subcategory: 'Road Systems', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~312 BCE', description: 'The Via Appia (312 BCE) began a road network that eventually covered 80,000 km. Roman roads were engineered with multiple layers — gravel, sand, paving stones — and many survive 2,000 years later.', impact: '"All roads lead to Rome." The road network unified the empire, enabled rapid military deployment, and created the infrastructure still visible across Europe.' },

  { slug: 'silk-road', name: 'Silk Road', era: 'ancient', category: 'trade', subcategory: 'Trade Routes', origin: 'China → Mediterranean', civilization: 'Multiple', yearIntroduced: '~130 BCE', description: 'A network of overland trade routes connecting China to Rome via Central Asia. Silk, spices, paper, and gunpowder traveled west; gold, glass, and wool traveled east. Goods changed hands through dozens of intermediaries.', impact: 'The most consequential trade network in history. Technology, religion (Buddhism, Islam, Christianity), and disease traveled the Silk Road.' },

  { slug: 'camel-caravan', name: 'Camel Caravan', era: 'ancient', category: 'animal', subcategory: 'Desert Transport', origin: 'Arabia / North Africa', civilization: 'Arabian / Nabataean', yearIntroduced: '~1,000 BCE', description: 'Domesticated camels carrying 200 kg each traveled in caravans of hundreds across the Sahara and Arabian deserts. A camel could go 10 days without water. Caravan cities like Petra and Palmyra grew fabulously wealthy.', impact: 'Made trans-Saharan and Arabian trade possible. Gold, salt, incense, and slaves flowed along camel routes for 3,000 years.' },

  { slug: 'chinese-junk-ancient', name: 'Chinese Sailing Junk', era: 'ancient', category: 'water', subcategory: 'Cargo Vessels', origin: 'China', civilization: 'Han Dynasty', yearIntroduced: '~200 BCE', description: 'Chinese junks featured watertight bulkhead compartments, stern-mounted rudders, and battened lug sails — all innovations that didn\'t reach Europe for over a thousand years. They could carry hundreds of tons of cargo.', impact: 'Chinese maritime technology was 1,000 years ahead of Europe. The junk\'s design principles influenced all subsequent ship design.' },

  { slug: 'cursus-publicus', name: 'Cursus Publicus (Roman Post)', era: 'ancient', category: 'trade', subcategory: 'Postal Systems', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~20 BCE', description: 'Augustus established a state postal system with relay stations every 12–18 miles across the empire. Riders on fast horses could carry messages at 80 km per day. Rest houses, fresh horses, and armed guards ensured reliability.', impact: 'The first state-run communications network. It held the empire together — commands from Rome reached Britain in 5 days.' },

  { slug: 'roman-concrete-harbors', name: 'Roman Harbor Engineering', era: 'ancient', category: 'water', subcategory: 'Port Infrastructure', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~100 BCE', description: 'Romans invented hydraulic concrete that set underwater, enabling construction of artificial harbors. The Port of Ostia and Harbor of Caesarea (Herod\'s masterpiece) transformed Mediterranean trade.', impact: 'Roman ports created the infrastructure of Mediterranean commerce. Their concrete is stronger today than when it was poured.' },

  // ═══════════════════════════════════════════════════════
  // MEDIEVAL — 500 – 1500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'viking-longship', name: 'Viking Longship', era: 'medieval', category: 'water', subcategory: 'Ocean-Going Vessels', origin: 'Scandinavia', civilization: 'Norse', yearIntroduced: '~800 CE', description: 'Clinker-built vessels with shallow draft (1 meter) that could sail open oceans and navigate rivers. The same ship could cross the North Atlantic and raid 200 miles up a river. Crews of 30–60 rowed and sailed.', impact: 'Gave Vikings reach from Baghdad to Newfoundland. The most versatile vessel ever built until the age of steam.' },

  { slug: 'magnetic-compass', name: 'Magnetic Compass', era: 'medieval', category: 'water', subcategory: 'Navigation Technology', origin: 'China → Europe', civilization: 'Chinese / European', yearIntroduced: '~1100 CE', description: 'Chinese navigators discovered that magnetized iron needles pointed north. By the 12th century, compasses were transforming both Chinese and European navigation, enabling reliable travel beyond sight of land.', impact: 'Made long-distance open-ocean navigation possible. Without the compass, the Age of Exploration could not have happened.' },

  { slug: 'stirrup-adoption', name: 'Stirrup', era: 'medieval', category: 'animal', subcategory: 'Riding Technology', origin: 'China → Europe', civilization: 'Chinese / Frankish', yearIntroduced: '~600 CE', description: 'The stirrup arrived in Europe via Central Asian nomads. It allowed a rider to brace for impact — transforming cavalry from skirmishers into shock troops. The armored knight on a charging destrier became unstoppable.', impact: 'Historian Lynn White argued the stirrup created feudalism — mounted knights required land grants to support them.' },

  { slug: 'hanseatic-cog', name: 'Hanseatic Cog', era: 'medieval', category: 'water', subcategory: 'Cargo Vessels', origin: 'Northern Europe', civilization: 'Hanseatic League', yearIntroduced: '~1200 CE', description: 'Flat-bottomed merchant ships that could carry 200+ tons of cargo. Cogs enabled the Hanseatic League — a trading confederation of 200 cities — to dominate North Sea and Baltic commerce for 300 years.', impact: 'The Hanseatic League was medieval Europe\'s economic superpower. Cogs made northern European trade profitable on a massive scale.' },

  { slug: 'horse-relay-mongol', name: 'Mongol Yam (Postal Relay)', era: 'medieval', category: 'trade', subcategory: 'Postal Systems', origin: 'Mongol Empire', civilization: 'Mongol', yearIntroduced: '~1230 CE', description: 'Genghis Khan established the Yam — a system of relay stations every 40 km across the largest empire in history. Riders changed horses at each station, carrying messages 300 km per day. Marco Polo marveled at it.', impact: 'The most extensive communications network before the telegraph. It held the Mongol Empire together and enabled the Pax Mongolica.' },

  { slug: 'chinese-treasure-fleet', name: 'Zheng He\'s Treasure Fleet', era: 'medieval', category: 'water', subcategory: 'Naval Expeditions', origin: 'China', civilization: 'Ming Dynasty', yearIntroduced: '1405 CE', description: 'Admiral Zheng He commanded fleets of 300+ ships — the largest wooden vessels ever built (400 feet long). Seven voyages reached Africa, Arabia, and Southeast Asia. Then China turned inward and burned the fleet.', impact: 'Demonstrated China\'s technological supremacy. Had the Ming continued, Chinese colonies might have preceded European ones by a century.' },

  { slug: 'caravel', name: 'Caravel', era: 'medieval', category: 'water', subcategory: 'Exploration Vessels', origin: 'Portugal', civilization: 'Portuguese', yearIntroduced: '~1450 CE', description: 'A small, agile ship with lateen sails that could sail close to the wind. Columbus\'s Niña and Pinta were caravels. The caravel allowed Portuguese explorers to navigate African coastlines and beat into trade winds.', impact: 'The ship that launched European global exploration. Without the caravel, there is no Age of Discovery.' },

  // ═══════════════════════════════════════════════════════
  // EARLY MODERN — 1500 – 1800 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'galleon', name: 'Galleon', era: 'earlyModern', category: 'water', subcategory: 'Armed Traders', origin: 'Spain / Portugal', civilization: 'Spanish / Portuguese', yearIntroduced: '~1530 CE', description: 'Multi-decked armed merchant ships that carried the wealth of the Americas to Europe. The Manila Galleon route (1565–1815) connected Asia and the Americas for 250 years. Spanish galleons moved the silver that fueled the global economy.', impact: 'Galleons created the first truly global economy. Spanish silver from potosí, carried by galleon, ended up in Chinese markets.' },

  { slug: 'stagecoach', name: 'Stagecoach', era: 'earlyModern', category: 'land', subcategory: 'Horse-Drawn Public Transport', origin: 'England / France', civilization: 'European', yearIntroduced: '~1600 CE', description: 'Regular horse-drawn coach services with scheduled stops. By the 1700s, stagecoach networks connected every major city in Europe and later America. Travel time: London to Edinburgh in 4 days (1750s).', impact: 'The first public land transportation. Created the concept of scheduled travel, timetables, and standardized routes.' },

  { slug: 'canal-age', name: 'Canal Systems', era: 'earlyModern', category: 'water', subcategory: 'Inland Waterways', origin: 'China / Netherlands / England', civilization: 'Multiple', yearIntroduced: '~1600 CE', description: 'The Chinese Grand Canal (1,776 km) and European canal networks (Dutch, English, French) created inland waterway highways. Canals moved bulk goods at 1/5 the cost of road transport. The Bridgewater Canal (1761) transformed British industry.', impact: 'Canals were the critical infrastructure of the early Industrial Revolution. Cheap bulk transport made factories viable.' },

  { slug: 'clipper-ship', name: 'Clipper Ship', era: 'earlyModern', category: 'water', subcategory: 'Fast Sailing Vessels', origin: 'United States / Britain', civilization: 'Anglo-American', yearIntroduced: '~1845 CE', description: 'Narrow-hulled, heavily rigged sailing ships built for speed. The Cutty Sark and Flying Cloud could reach 20 knots. They raced tea from China and wool from Australia, completing the London-Sydney voyage in under 70 days.', impact: 'The pinnacle of sailing technology. Clipper ships were the fastest commercial vessels until steam overtook them.' },

  { slug: 'hot-air-balloon', name: 'Hot Air Balloon', era: 'earlyModern', category: 'air', subcategory: 'Early Flight', origin: 'France', civilization: 'French', yearIntroduced: '1783 CE', description: 'The Montgolfier brothers launched the first manned balloon flight in Paris (1783). Hydrogen balloons followed within weeks. Ballooning became a craze and was soon adopted for military reconnaissance.', impact: 'Humanity\'s first powered flight. Proved that humans could leave the ground — the psychological barrier to aviation was broken forever.' },

  { slug: 'macadam-roads', name: 'Macadam Roads', era: 'earlyModern', category: 'land', subcategory: 'Road Engineering', origin: 'Scotland', civilization: 'British', yearIntroduced: '1820 CE', description: 'John Loudon McAdam\'s technique of layered crushed stone created smooth, durable, all-weather roads. His method replaced mud tracks with engineered surfaces and halved travel times across Britain.', impact: 'The first road revolution since Rome. McAdam\'s principles still underpin modern road construction — "tarmac" comes from his name.' },

  // ═══════════════════════════════════════════════════════
  // MODERN — 1800 – 1945 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'steam-locomotive', name: 'Steam Locomotive', era: 'modern', category: 'rail', subcategory: 'Steam Power', origin: 'England', civilization: 'British', yearIntroduced: '1804 CE', description: 'Richard Trevithick built the first steam locomotive (1804). George Stephenson\'s Rocket (1829) proved the commercial potential. The Liverpool-Manchester Railway (1830) launched the railway age.', impact: 'The most transformative technology of the 19th century. Railways shrank continents, created national economies, and standardized time zones.' },

  { slug: 'steamship', name: 'Steamship', era: 'modern', category: 'water', subcategory: 'Steam Vessels', origin: 'United States / Britain', civilization: 'Anglo-American', yearIntroduced: '1807 CE', description: 'Robert Fulton\'s Clermont (1807) proved steam-powered boats viable. Isambard Kingdom Brunel\'s Great Western (1838) crossed the Atlantic in 15 days. By 1850, steam was replacing sail on every ocean.', impact: 'Freed shipping from wind dependency. Steam made global trade reliable and predictable, and mass emigration possible.' },

  { slug: 'transcontinental-railroad', name: 'Transcontinental Railroad', era: 'modern', category: 'rail', subcategory: 'Continental Networks', origin: 'United States', civilization: 'American', yearIntroduced: '1869 CE', description: 'The Golden Spike ceremony at Promontory Summit (May 10, 1869) connected the US east and west coasts by rail. The journey from New York to San Francisco dropped from 6 months to 6 days.', impact: 'United the American continent. Similar railways transformed Canada, Russia (Trans-Siberian), India, and every industrializing nation.' },

  { slug: 'bicycle', name: 'Bicycle', era: 'modern', category: 'land', subcategory: 'Human-Powered', origin: 'Germany / France', civilization: 'European', yearIntroduced: '1817 CE', description: 'Karl von Drais\'s "running machine" (1817) evolved into the safety bicycle (1885). Affordable, fast, and requiring no fuel, the bicycle gave ordinary people personal mobility for the first time.', impact: 'Liberated the working class and women from geographic constraint. The Wright Brothers were bicycle mechanics — bikes led to planes.' },

  { slug: 'suez-canal', name: 'Suez Canal', era: 'modern', category: 'water', subcategory: 'Canal Infrastructure', origin: 'Egypt', civilization: 'French / Egyptian', yearIntroduced: '1869 CE', description: 'A 164 km artificial waterway connecting the Mediterranean to the Red Sea, eliminating the 10,000 km voyage around Africa. 10 years of construction, 1.5 million workers, and a human cost of 120,000 lives.', impact: 'Transformed global shipping. The Suez Canal remains one of the world\'s most critical chokepoints — 12% of global trade passes through it.' },

  { slug: 'automobile', name: 'Automobile (Gasoline)', era: 'modern', category: 'land', subcategory: 'Motor Vehicles', origin: 'Germany', civilization: 'German', yearIntroduced: '1886 CE', description: 'Karl Benz\'s Patent-Motorwagen (1886) was the first true automobile. Henry Ford\'s Model T (1908) made cars affordable. By 1930, cars had transformed cities, created suburbs, and built an oil-dependent economy.', impact: 'Reshaped civilization more than any invention since the printing press. Cars redefined how humans live, work, and design cities.' },

  { slug: 'wright-brothers', name: 'Wright Flyer', era: 'modern', category: 'air', subcategory: 'Powered Flight', origin: 'United States', civilization: 'American', yearIntroduced: '1903 CE', description: 'Orville and Wilbur Wright achieved the first powered, sustained, controlled flight at Kitty Hawk (December 17, 1903). The flight lasted 12 seconds and covered 37 meters.', impact: 'Launched the aviation age. Within 66 years, humans went from 12 seconds in the air to walking on the Moon.' },

  { slug: 'panama-canal', name: 'Panama Canal', era: 'modern', category: 'water', subcategory: 'Canal Infrastructure', origin: 'Panama', civilization: 'American / Panamanian', yearIntroduced: '1914 CE', description: 'An 82 km waterway through Panama connecting the Atlantic and Pacific Oceans. The French attempt failed (1881–1889, 22,000 deaths). The US succeeded (1904–1914) by conquering malaria and engineering massive locks.', impact: 'Eliminated the 12,000 km voyage around South America. The canal handles 6% of world trade annually.' },

  { slug: 'london-underground', name: 'London Underground', era: 'modern', category: 'urban', subcategory: 'Metro Systems', origin: 'London, England', civilization: 'British', yearIntroduced: '1863 CE', description: 'The world\'s first underground railway — the Metropolitan Railway opened in 1863 with gas-lit wooden carriages pulled by steam locomotives through tunnels. The "Tube" eventually grew to 402 km and 272 stations.', impact: 'Invented urban mass transit. London\'s Underground inspired every metro system in the world — Moscow, New York, Tokyo, Paris.' },

  { slug: 'zeppelin', name: 'Zeppelin Airship', era: 'modern', category: 'air', subcategory: 'Lighter-Than-Air', origin: 'Germany', civilization: 'German', yearIntroduced: '1900 CE', description: 'Count Ferdinand von Zeppelin\'s rigid airships carried passengers in luxury at 130 km/h. The Graf Zeppelin circled the globe in 21 days (1929). The Hindenburg disaster (1937) ended the airship era.', impact: 'The first practical air travel. Zeppelins proved that sustained air transportation was commercially viable.' },

  { slug: 'ford-model-t', name: 'Ford Model T', era: 'modern', category: 'land', subcategory: 'Mass Production', origin: 'United States', civilization: 'American', yearIntroduced: '1908 CE', description: 'Henry Ford\'s assembly line produced 15 million Model Ts, dropping the price from $850 to $260. The Model T proved that cars could be affordable consumer goods, not luxury items for the rich.', impact: 'Ford\'s assembly line revolutionized not just transportation but all manufacturing. The Model T created America\'s car culture.' },

  // ═══════════════════════════════════════════════════════
  // CONTEMPORARY — 1945 CE – Present
  // ═══════════════════════════════════════════════════════

  { slug: 'jet-airliner', name: 'Jet Airliner', era: 'contemporary', category: 'air', subcategory: 'Commercial Aviation', origin: 'Britain / United States', civilization: 'Anglo-American', yearIntroduced: '1952 CE', description: 'The de Havilland Comet (1952) was the first commercial jet airliner. Boeing\'s 707 (1958) and 747 "Jumbo Jet" (1970) democratized air travel — making it affordable for millions, not just the wealthy.', impact: 'Shrank the world. Jet travel created mass tourism, globalized business, and enabled the modern interconnected economy.' },

  { slug: 'interstate-highways', name: 'US Interstate Highway System', era: 'contemporary', category: 'land', subcategory: 'Highway Networks', origin: 'United States', civilization: 'American', yearIntroduced: '1956 CE', description: 'Eisenhower\'s Federal-Aid Highway Act (1956) built 77,000 km of controlled-access highways. Officially motivated by defense, the Interstates reshaped American geography — creating suburbs, strip malls, and the commuter lifestyle.', impact: 'The largest public works project in history. Suburbanized America, killed passenger rail, and made the US car-dependent.' },

  { slug: 'containerization', name: 'Shipping Container', era: 'contemporary', category: 'water', subcategory: 'Cargo Revolution', origin: 'United States', civilization: 'American', yearIntroduced: '1956 CE', description: 'Malcolm McLean\'s standardized steel container (1956) slashed shipping costs by 96%. Loading a ship went from 7 days of manual labor to 12 hours of crane work. The container is the most important invention you\'ve never thought about.', impact: 'Made globalization possible. Cheap shipping meant manufacturing could move to low-cost countries — reshaping the entire world economy.' },

  { slug: 'bullet-train', name: 'Shinkansen (Bullet Train)', era: 'contemporary', category: 'rail', subcategory: 'High-Speed Rail', origin: 'Japan', civilization: 'Japanese', yearIntroduced: '1964 CE', description: 'The Tōkaidō Shinkansen (Tokyo–Osaka) opened for the 1964 Olympics, running at 210 km/h. Zero fatalities in 60 years. Japan\'s bullet trains have since carried 10+ billion passengers.', impact: 'Proved that rail could compete with air travel. Inspired TGV (France), ICE (Germany), and China\'s 40,000 km HSR network.' },

  { slug: 'apollo-11', name: 'Apollo 11 Moon Landing', era: 'contemporary', category: 'space', subcategory: 'Space Exploration', origin: 'United States', civilization: 'American', yearIntroduced: '1969 CE', description: 'Neil Armstrong and Buzz Aldrin walked on the Moon on July 20, 1969. The Saturn V rocket remains the most powerful vehicle ever built. 600 million people watched live — the largest shared human experience.', impact: '"One small step for man, one giant leap for mankind." Proved that humans could travel beyond Earth. The defining achievement of the 20th century.' },

  { slug: 'concorde', name: 'Concorde', era: 'contemporary', category: 'air', subcategory: 'Supersonic Flight', origin: 'France / Britain', civilization: 'Franco-British', yearIntroduced: '1976 CE', description: 'The only commercially successful supersonic airliner. Concorde flew London–New York in 3 hours at Mach 2.04 (2,180 km/h). Only 20 were built. It retired in 2003 — we\'ve gone slower since.', impact: 'The only time in history that commercial air travel became slower over time. Concorde remains the benchmark for aerospace ambition.' },

  { slug: 'electric-vehicle-revival', name: 'Electric Vehicle Revival', era: 'contemporary', category: 'land', subcategory: 'Electric Transport', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '2008 CE', description: 'Tesla\'s Roadster (2008) proved electric cars could be desirable. The Model 3 (2017) made them mainstream. By 2024, EVs are 18% of global new car sales. Electric cars actually predate gasoline cars (1880s) but lost the early competition.', impact: 'The most significant transportation shift since the Model T. EVs are reshaping energy policy, urban design, and geopolitics.' },

  { slug: 'spacex-reusable-rockets', name: 'SpaceX Reusable Rockets', era: 'contemporary', category: 'space', subcategory: 'Space Infrastructure', origin: 'United States', civilization: 'American', yearIntroduced: '2015 CE', description: 'SpaceX\'s Falcon 9 became the first orbital rocket to land and be reused (2015). This dropped launch costs by 90% and made space access routine. Starship aims to make interplanetary travel possible.', impact: 'Democratized space access. Reusable rockets are creating a space economy of satellite internet, space tourism, and eventually Mars colonization.' },

  { slug: 'ride-sharing', name: 'Ride-Sharing Platforms', era: 'contemporary', category: 'urban', subcategory: 'Digital Transport', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '2009 CE', description: 'Uber (2009), Lyft, and Grab transformed urban mobility by connecting riders with drivers via smartphone apps. The "gig economy" of transportation disrupted taxi industries worldwide.', impact: 'Changed how cities move. Raised questions about labor rights, urban congestion, and whether private platforms should replace public transit.' },

  { slug: 'autonomous-vehicles', name: 'Autonomous Vehicles', era: 'contemporary', category: 'land', subcategory: 'AI-Driven Transport', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '2018 CE', description: 'Waymo launched the first commercial autonomous taxi service in Phoenix (2018). Tesla, Cruise, and Chinese firms are racing toward full self-driving. The technology promises to eliminate 94% of accidents caused by human error.', impact: 'If successful, autonomous vehicles will reshape cities, eliminate millions of driving jobs, and fundamentally change human mobility.' },
]
