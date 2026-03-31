/* ──────────────────────────────────────────────────────────────────────────
   Clothing & Textiles — Every revolutionary material, garment, and fashion
   milestone across 100,000 years of human self-expression.
   ────────────────────────────────────────────────────────────────────────── */

export interface Clothing {
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

export interface ClothingCategory {
  id: string
  label: string
  color: string
  icon: string
}

export const CLOTHING_CATEGORIES: ClothingCategory[] = [
  { id: 'fiber',       label: 'Fabric Types & Raw Materials',             color: '#8B6914', icon: 'Ribbon' },
  { id: 'garment',     label: 'Garments, Fashion & Footwear',             color: '#6B3FA0', icon: 'Shirt' },
  { id: 'technology',  label: 'Looms, Spinning & Production Tools',       color: '#718096', icon: 'Cog' },
  { id: 'dye',         label: 'Dyes, Pigments & Coloring',                color: '#C53030', icon: 'Palette' },
  { id: 'armor',       label: 'Protective & Military Clothing',           color: '#2D2A24', icon: 'Shield' },
  { id: 'trade',       label: 'Global Textile Trade & Fashion Industry',  color: '#DD6B20', icon: 'Store' },
  { id: 'cultural',    label: 'Cultural Dress & Identity Clothing',       color: '#38A169', icon: 'Crown' },
  { id: 'modern',      label: 'Synthetic Fabrics & Smart Textiles',       color: '#4A90D9', icon: 'Sparkles' },
]

export const ERA_LABELS: Record<string, { label: string; color: string; period: string }> = {
  prehistoric:  { label: 'Prehistoric',     color: '#6B4D1B', period: 'Before 3,000 BCE' },
  ancient:      { label: 'Ancient World',   color: '#8B4513', period: '3,000 BCE – 500 CE' },
  medieval:     { label: 'Medieval',        color: '#A67C2E', period: '500 – 1500 CE' },
  earlyModern:  { label: 'Early Modern',    color: '#C5963A', period: '1500 – 1800 CE' },
  modern:       { label: 'Modern',          color: '#4A90D9', period: '1800 – 1945 CE' },
  contemporary: { label: 'Contemporary',    color: '#6B3FA0', period: '1945 CE – Present' },
}

export const CLOTHING: Clothing[] = [
  // ═══════════════════════════════════════════════════════
  // PREHISTORIC — Before 3,000 BCE
  // ═══════════════════════════════════════════════════════

  { slug: 'animal-hides', name: 'Animal Hide Clothing', era: 'prehistoric', category: 'fiber', subcategory: 'Natural Materials', origin: 'Africa / Eurasia', civilization: 'Various', yearIntroduced: '~100,000 BCE', description: 'The oldest form of clothing — animal skins scraped, cured, and stitched with bone needles. Evidence of tailored fur clothing dates to 100,000 years ago. Clothing enabled modern humans to survive Ice Age Europe.', impact: 'Clothing made migration out of Africa possible. Without it, humans could not have colonized temperate and arctic regions.' },

  { slug: 'bone-needle', name: 'Bone Sewing Needle', era: 'prehistoric', category: 'technology', subcategory: 'Tools', origin: 'Eurasia', civilization: 'Upper Paleolithic', yearIntroduced: '~40,000 BCE', description: 'Eyed needles carved from bone or ivory allowed precise stitching of fitted garments. This is the oldest surviving sewing tool — invented 20,000 years before agriculture.', impact: 'Enabled tailored clothing for the first time. Fitted garments were more efficient at trapping body heat than draped hides.' },

  { slug: 'plant-fiber-weaving', name: 'Plant Fiber Weaving', era: 'prehistoric', category: 'fiber', subcategory: 'Woven Textiles', origin: 'Multiple Regions', civilization: 'Various', yearIntroduced: '~27,000 BCE', description: 'Impressions of woven plant fibers have been found on clay fragments from Dolní Věstonice (Czech Republic). Flax, hemp, and nettle fibers were twisted into thread and woven into fabric long before agriculture.', impact: 'Weaving is one of humanity\'s oldest technologies. It predates pottery, metalwork, and farming.' },

  { slug: 'flax-linen', name: 'Flax / Linen', era: 'prehistoric', category: 'fiber', subcategory: 'Plant Fibers', origin: 'Fertile Crescent', civilization: 'Neolithic', yearIntroduced: '~8,000 BCE', description: 'Flax was one of the first domesticated plants, grown specifically for its fibers. Linen — cool, lightweight, and absorbent — became the fabric of the ancient Near East and Egypt. Egyptian mummies were wrapped in linen.', impact: 'Linen dominated textiles for 5,000 years. Egyptian linen was exported across the Mediterranean and remains a luxury fabric today.' },

  { slug: 'wool-sheep', name: 'Wool from Sheep', era: 'prehistoric', category: 'fiber', subcategory: 'Animal Fibers', origin: 'Mesopotamia', civilization: 'Neolithic', yearIntroduced: '~6,000 BCE', description: 'Early domesticated sheep had hair, not wool. Selective breeding over millennia created woolly sheep. Wool\'s insulating properties — warm when wet, naturally fire-resistant — made it the ideal fiber for Northern European climates.', impact: 'Wool became the economic backbone of medieval Europe. The English wool trade financed cathedrals, wars, and the foundations of capitalism.' },

  { slug: 'bark-cloth', name: 'Bark Cloth (Tapa)', era: 'prehistoric', category: 'fiber', subcategory: 'Natural Materials', origin: 'Southeast Asia / Oceania', civilization: 'Austronesian', yearIntroduced: '~5,000 BCE', description: 'Made by pounding the inner bark of paper mulberry trees into thin, flexible sheets. Tapa cloth was the primary textile of Polynesia, decorated with elaborate geometric patterns using natural dyes.', impact: 'Proved that textiles can be made without spinning or weaving. Tapa cloth remains culturally significant across the Pacific.' },

  // ═══════════════════════════════════════════════════════
  // ANCIENT — 3,000 BCE – 500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'cotton-domestication', name: 'Cotton Domestication', era: 'ancient', category: 'fiber', subcategory: 'Plant Fibers', origin: 'India / Americas', civilization: 'Indus Valley / Mesoamerican', yearIntroduced: '~3,000 BCE', description: 'Cotton was independently domesticated in India and Peru. Indian cotton textiles were so fine that Greeks called them "woven wind." The Indus Valley civilization mass-produced cotton fabric at an industrial scale.', impact: 'Cotton became the world\'s most important textile fiber. It drove the slave trade, the Industrial Revolution, and the American Civil War.' },

  { slug: 'silk-discovery', name: 'Silk', era: 'ancient', category: 'fiber', subcategory: 'Animal Fibers', origin: 'China', civilization: 'Chinese', yearIntroduced: '~2,700 BCE', description: 'Legend attributes silk\'s discovery to Empress Leizu. Bombyx mori silkworms produce fibers 1,000 meters long that are stronger than steel per unit weight. China guarded the secret for 3,000 years — smuggling silkworm eggs was punishable by death.', impact: 'Silk created the Silk Road — the most consequential trade network in history. Worth more than gold by weight, silk was literally money.' },

  { slug: 'tyrian-purple', name: 'Tyrian Purple Dye', era: 'ancient', category: 'dye', subcategory: 'Luxury Dyes', origin: 'Phoenicia (Lebanon)', civilization: 'Phoenician', yearIntroduced: '~1500 BCE', description: 'Extracted from Murex sea snails — 12,000 snails produced just 1.5 grams of dye. Tyrian purple was the most expensive substance in the ancient world. Only royalty and the ultra-wealthy could afford it.', impact: '"Born to the purple" — purple became synonymous with royalty across civilizations. Roman senators wore purple stripes; Byzantine emperors were clad entirely in it.' },

  { slug: 'toga-roman', name: 'Roman Toga', era: 'ancient', category: 'garment', subcategory: 'Status Garments', origin: 'Roman Empire', civilization: 'Roman', yearIntroduced: '~500 BCE', description: 'A 6-meter semicircular wool wrap that only Roman citizens could wear. The toga\'s complexity — requiring assistance to drape properly — made it a status symbol. Different borders (purple, gold) indicated rank.', impact: 'The toga was Rome\'s national garment — a visible marker of citizenship, class, and political status.' },

  { slug: 'indigo-dye', name: 'Indigo Dye', era: 'ancient', category: 'dye', subcategory: 'Plant Dyes', origin: 'India / Egypt', civilization: 'Indian / Egyptian', yearIntroduced: '~2,000 BCE', description: 'Extracted from the Indigofera plant, indigo produces the deepest, most lightfast blue dye in the natural world. Indian indigo (later called "true indigo") was traded across the ancient world — the word "indigo" means "from India."', impact: 'Blue became attainable. Indigo drove colonial trade wars and plantation slavery. Synthetic indigo (1897) made blue jeans possible.' },

  { slug: 'egyptian-linen-refinement', name: 'Egyptian Royal Linen', era: 'ancient', category: 'trade', subcategory: 'Luxury Textiles', origin: 'Egypt', civilization: 'Egyptian', yearIntroduced: '~2,500 BCE', description: 'Egyptian weavers produced linen of extraordinary fineness — 200 threads per inch (modern sheets: 200-800). Pharaonic linen was semitransparent. Tutankhamun was buried with over 100 linen garments.', impact: 'Egyptian linen set the global standard for textile quality for 3,000 years. Exported across the Mediterranean as a luxury commodity.' },

  { slug: 'chinese-silk-robes', name: 'Chinese Silk Court Dress', era: 'ancient', category: 'cultural', subcategory: 'Ceremonial Dress', origin: 'China', civilization: 'Han Dynasty', yearIntroduced: '~200 BCE', description: 'The Han Dynasty codified silk court dress with elaborate rules: specific colors, patterns, and lengths indicated rank. Dragon robes (later longpao) became the ultimate symbol of imperial authority.', impact: 'Chinese court dress influenced fashion across East Asia. The dragon robe tradition continued for 2,000 years until the fall of the Qing Dynasty.' },

  { slug: 'chain-mail', name: 'Chain Mail', era: 'ancient', category: 'armor', subcategory: 'Metal Armor', origin: 'Celtic Europe / Roman', civilization: 'Celtic / Roman', yearIntroduced: '~300 BCE', description: 'Interlocking metal rings created flexible armor that could stop slashing attacks. A Celtic invention adopted by Rome — a Roman lorica hamata contained 30,000+ iron rings and weighed 10 kg.', impact: 'The dominant form of body armor for 1,500 years. Chain mail protected warriors from Rome to medieval Japan (kusari).' },

  // ═══════════════════════════════════════════════════════
  // MEDIEVAL — 500 – 1500 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'spinning-wheel', name: 'Spinning Wheel', era: 'medieval', category: 'technology', subcategory: 'Production Tools', origin: 'India → Europe', civilization: 'Indian / European', yearIntroduced: '~1000 CE', description: 'The spinning wheel (likely invented in India) mechanized thread production, increasing output 10x over hand spindles. It reached Europe by 1280 and became the most important textile tool until the Industrial Revolution.', impact: 'Slashed thread production costs. "Spinster" originally meant a woman who spun thread — the most common female occupation for centuries.' },

  { slug: 'silk-road-fashion', name: 'Silk Road Fashion Exchange', era: 'medieval', category: 'trade', subcategory: 'Cultural Exchange', origin: 'Central Asia / Global', civilization: 'Multiple', yearIntroduced: '~700 CE', description: 'The Silk Road didn\'t just carry silk — it exchanged fashion. Chinese silk reached Byzantine courts; Persian patterns influenced Chinese design; Indian cotton spread eastward. Mongol Period garments blended styles from Korea to Hungary.', impact: 'Created the first global fashion system. Textile designs traveled faster than armies, blending aesthetics across continents.' },

  { slug: 'european-sumptuary-laws', name: 'Sumptuary Laws', era: 'medieval', category: 'cultural', subcategory: 'Regulation', origin: 'Europe / China', civilization: 'European / Chinese', yearIntroduced: '~1200 CE', description: 'Laws regulating what each social class could wear — only nobility could wear ermine, silk, or certain colors. England, France, and China all enforced textile restrictions. Violations were punishable by fines or imprisonment.', impact: 'Proved that clothing is power. Sumptuary laws attempted to freeze social hierarchies through dress — and largely failed as the merchant class grew rich.' },

  { slug: 'velvet', name: 'Velvet', era: 'medieval', category: 'fiber', subcategory: 'Luxury Textiles', origin: 'Italy / Middle East', civilization: 'Italian / Islamic', yearIntroduced: '~1300 CE', description: 'Cut-pile silk velvet — developed in medieval Italy and the Islamic world — became the ultimate luxury fabric. Venetian and Florentine velvets featured brocade patterns, gold thread, and cost more than land per meter.', impact: 'Velvet became the fabric of European royalty and church. The Italian velvet trade funded the Renaissance.' },

  { slug: 'japanese-kimono', name: 'Kimono', era: 'medieval', category: 'cultural', subcategory: 'National Dress', origin: 'Japan', civilization: 'Japanese', yearIntroduced: '~800 CE', description: 'The T-shaped silk garment became Japan\'s national dress during the Heian Period. Kimono colors, patterns, and layering communicated season, age, marital status, and social rank with extraordinary subtlety.', impact: 'The kimono system is one of the most sophisticated clothing languages ever developed. Its aesthetics influenced Western art (Japonisme) and fashion.' },

  { slug: 'plate-armor', name: 'Full Plate Armor', era: 'medieval', category: 'armor', subcategory: 'Metal Armor', origin: 'Italy / Germany', civilization: 'European', yearIntroduced: '~1400 CE', description: 'Articulated steel suits covering the entire body. Milan and Augsburg produced the finest examples — 15-25 kg total, yet a trained knight could run, mount, and fight. Gothic and Maximilian styles are works of art.', impact: 'The peak of personal protection before gunpowder. Plate armor represents the pinnacle of medieval metalworking and engineering.' },

  { slug: 'african-kente-cloth', name: 'Kente Cloth', era: 'medieval', category: 'cultural', subcategory: 'Ceremonial Textiles', origin: 'Ghana', civilization: 'Ashanti', yearIntroduced: '~1100 CE', description: 'Hand-woven silk and cotton strips sewn together into vibrant geometric patterns. Each Kente pattern has a name and meaning — originally reserved for Ashanti royalty. Woven on narrow-strip looms by male weavers.', impact: 'Kente became a global symbol of African identity and pride. Its adoption by the African diaspora made it one of the most recognized textiles in the world.' },

  // ═══════════════════════════════════════════════════════
  // EARLY MODERN — 1500 – 1800 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'calico-trade', name: 'Indian Calico Trade', era: 'earlyModern', category: 'trade', subcategory: 'Global Commerce', origin: 'India', civilization: 'Indian / Mughal', yearIntroduced: '~1600 CE', description: 'Indian cotton calicoes flooded European markets — brighter, softer, and cheaper than European wool or linen. Calico prints became so popular that France and England banned them (Calico Acts) to protect domestic wool industries.', impact: 'Indian textiles drove European colonialism. Britain\'s desire to replicate and surpass Indian cotton directly sparked the Industrial Revolution.' },

  { slug: 'knitting-machine', name: 'Stocking Frame (Knitting Machine)', era: 'earlyModern', category: 'technology', subcategory: 'Mechanization', origin: 'England', civilization: 'British', yearIntroduced: '1589 CE', description: 'William Lee\'s stocking frame mechanized knitting, producing stockings 10x faster than hand knitting. Queen Elizabeth I refused a patent, fearing unemployment. It was the first step toward textile industrialization.', impact: 'The first textile machine. Foreshadowed the entire Industrial Revolution — and the Luddite response to it.' },

  { slug: 'french-haute-couture-origins', name: 'French Fashion Dominance', era: 'earlyModern', category: 'garment', subcategory: 'Fashion Systems', origin: 'France', civilization: 'French', yearIntroduced: '~1670 CE', description: 'Louis XIV made fashion a tool of state power — Versailles set trends that all European courts imitated. Fashion dolls (pandoras) were sent to foreign courts to showcase French styles. Paris became the world\'s fashion capital.', impact: 'France\'s fashion dominance, established by Louis XIV, has lasted 350 years. Paris remains the center of haute couture.' },

  { slug: 'flying-shuttle', name: 'Flying Shuttle', era: 'earlyModern', category: 'technology', subcategory: 'Mechanization', origin: 'England', civilization: 'British', yearIntroduced: '1733 CE', description: 'John Kay\'s flying shuttle doubled weaving speed and allowed wider fabrics to be woven by a single weaver. It created a thread shortage that drove the invention of spinning machines — launching the Industrial Revolution.', impact: 'The flying shuttle was the first domino of the Industrial Revolution. Every subsequent textile invention was a response to Kay\'s innovation.' },

  { slug: 'spinning-jenny', name: 'Spinning Jenny', era: 'earlyModern', category: 'technology', subcategory: 'Industrialization', origin: 'England', civilization: 'British', yearIntroduced: '1764 CE', description: 'James Hargreaves\' multi-spindle spinning frame allowed one worker to spin 8 threads simultaneously. Within a decade, machines spun 80+ threads. Cottage spinning was destroyed in a generation.', impact: 'Launched the mechanization of textiles — the first industry to be fully industrialized. The cotton mills that followed created the modern factory system.' },

  { slug: 'cotton-gin', name: 'Cotton Gin', era: 'earlyModern', category: 'technology', subcategory: 'Processing', origin: 'United States', civilization: 'American', yearIntroduced: '1793 CE', description: 'Eli Whitney\'s cotton gin separated cotton fibers from seeds 50x faster than hand processing. It made short-staple cotton profitable — and massively increased demand for enslaved labor to grow it.', impact: 'The cotton gin revived and expanded American slavery. By 1860, cotton was 60% of US exports. The Civil War was fought over the economy it created.' },

  { slug: 'tartan-plaid', name: 'Scottish Tartan', era: 'earlyModern', category: 'cultural', subcategory: 'Identity Textiles', origin: 'Scotland', civilization: 'Scottish', yearIntroduced: '~1500 CE', description: 'Clan-specific tartan patterns became symbols of Scottish Highland identity. After the Jacobite defeat (1746), the British banned tartan for 36 years — making it a symbol of resistance. Walter Scott\'s romanticization later made it fashionable worldwide.', impact: 'Tartan became the first "branded" textile pattern — each clan pattern a corporate logo. It influenced fashion from punk to high couture.' },

  // ═══════════════════════════════════════════════════════
  // MODERN — 1800 – 1945 CE
  // ═══════════════════════════════════════════════════════

  { slug: 'sewing-machine', name: 'Sewing Machine', era: 'modern', category: 'technology', subcategory: 'Garment Production', origin: 'United States / France', civilization: 'American / French', yearIntroduced: '1846 CE', description: 'Elias Howe and Isaac Singer developed commercial sewing machines that could stitch 250 stitches per minute — 5x a skilled hand sewer. Singer\'s installment payment plan made it the first affordable consumer machine.', impact: 'Democratized clothing. The sewing machine put affordable, well-made garments within reach of ordinary people for the first time.' },

  { slug: 'synthetic-dye-mauveine', name: 'Synthetic Dye (Mauveine)', era: 'modern', category: 'dye', subcategory: 'Synthetic Chemistry', origin: 'England', civilization: 'British', yearIntroduced: '1856 CE', description: 'William Henry Perkin accidentally created mauveine — the first synthetic dye — from coal tar while trying to synthesize quinine. "Mauve mania" swept Europe. The synthetic dye industry funded the birth of the modern chemical industry.', impact: 'Freed color from nature\'s limitations. Synthetic dyes made every color affordable and launched the chemical industry that created pharmaceuticals, explosives, and plastics.' },

  { slug: 'denim-blue-jeans', name: 'Blue Jeans', era: 'modern', category: 'garment', subcategory: 'Workwear', origin: 'United States', civilization: 'American', yearIntroduced: '1873 CE', description: 'Levi Strauss and Jacob Davis patented riveted denim trousers for gold miners and cowboys. Indigo-dyed cotton twill (denim, from "de Nîmes") proved nearly indestructible. Jeans became America\'s most iconic garment.', impact: 'Jeans transcended class — from workwear to counterculture (1950s) to global fashion. The most widely worn garment in human history.' },

  { slug: 'rayon', name: 'Rayon (First Synthetic Fiber)', era: 'modern', category: 'modern', subcategory: 'Synthetic Fibers', origin: 'France / England', civilization: 'European', yearIntroduced: '1894 CE', description: 'Count Hilaire de Chardonnet created "artificial silk" from cellulose dissolved in chemical solvents. Rayon looked like silk at a fraction of the cost. It was the first commercially successful synthetic fiber.', impact: 'Proved that textiles need not come from animals or plants. Opened the door to nylon, polyester, and all synthetic fabrics.' },

  { slug: 'haute-couture-system', name: 'Haute Couture System', era: 'modern', category: 'garment', subcategory: 'Fashion Industry', origin: 'France', civilization: 'French', yearIntroduced: '1858 CE', description: 'Charles Frederick Worth became the first modern fashion designer — creating original designs, labeling garments, and staging fashion shows. The Chambre Syndicale de la Haute Couture (1868) formalized rules that still govern French fashion.', impact: 'Created the modern fashion industry. Worth invented the concept of the designer as artist-celebrity — from Chanel to Dior to today.' },

  { slug: 'nylon', name: 'Nylon', era: 'modern', category: 'modern', subcategory: 'Synthetic Fibers', origin: 'United States', civilization: 'American', yearIntroduced: '1938 CE', description: 'DuPont\'s Wallace Carothers created nylon — the first fully synthetic fiber from petroleum. Nylon stockings sold 64 million pairs in the first year (1940). During WWII, nylon was diverted to parachutes, causing a "nylon riot" when stockings returned.', impact: 'Nylon proved that chemistry could replace nature. It launched the synthetic textile revolution that now dominates global clothing production.' },

  { slug: 'zipper', name: 'Zipper', era: 'modern', category: 'technology', subcategory: 'Fasteners', origin: 'United States', civilization: 'American', yearIntroduced: '1913 CE', description: 'Gideon Sundback\'s "hookless fastener" replaced buttons, hooks, and laces. The military adopted zippers for flying suits and boots. By the 1930s, zippers appeared on civilian clothing. The name came from B.F. Goodrich.', impact: 'A small invention with enormous impact. The zipper changed garment design, enabled new clothing types, and saved billions of hours of buttoning.' },

  { slug: 'military-uniforms-ww1', name: 'WWI Military Uniforms', era: 'modern', category: 'armor', subcategory: 'Military Dress', origin: 'Europe', civilization: 'European', yearIntroduced: '1914 CE', description: 'WWI forced a revolution in military dress — from brightly colored Napoleonic-era uniforms to khaki and field grey camouflage. Trench warfare demanded waterproof trench coats, steel helmets, and practical boots. The trench coat became a civilian fashion icon.', impact: 'WWI proved that visibility killed. Every military adopted camouflage. Civilian fashion adopted trench coats, aviator jackets, and cargo pockets.' },

  // ═══════════════════════════════════════════════════════
  // CONTEMPORARY — 1945 CE – Present
  // ═══════════════════════════════════════════════════════

  { slug: 'polyester', name: 'Polyester', era: 'contemporary', category: 'modern', subcategory: 'Synthetic Fibers', origin: 'Britain / United States', civilization: 'Anglo-American', yearIntroduced: '1951 CE', description: 'Polyester (PET) fiber — wrinkle-resistant, durable, cheap, and easy to wash. Dacron (DuPont) and Terylene (ICI) transformed everyday clothing. By 2023, polyester accounts for 54% of all fiber production globally.', impact: 'The world\'s most-used textile fiber. Polyester made affordable clothing possible for billions — but creates microplastic pollution threatening oceans.' },

  { slug: 'bikini', name: 'Bikini', era: 'contemporary', category: 'garment', subcategory: 'Swimwear Revolution', origin: 'France', civilization: 'French', yearIntroduced: '1946 CE', description: 'Louis Réard\'s two-piece swimsuit was so scandalous he named it after Bikini Atoll\'s nuclear test — explosive impact. No Parisian model would wear it; he hired a nude dancer. The Vatican condemned it. It took 20 years to gain mainstream acceptance.', impact: 'The bikini became a symbol of women\'s liberation and body autonomy. One of the most culturally significant garments of the 20th century.' },

  { slug: 'fast-fashion', name: 'Fast Fashion', era: 'contemporary', category: 'trade', subcategory: 'Mass Production', origin: 'Spain / Sweden / Global', civilization: 'Global', yearIntroduced: '~1990 CE', description: 'Zara, H&M, and Primark pioneered rapid-cycle fashion — from runway to store in 2 weeks instead of 6 months. Clothing became disposable; the average garment is worn 7 times before being discarded. 100 billion garments are produced annually.', impact: 'Democratized fashion but at massive environmental cost. The fashion industry produces 10% of global CO₂ emissions and is the second-largest industrial polluter.' },

  { slug: 'gore-tex', name: 'Gore-Tex', era: 'contemporary', category: 'modern', subcategory: 'Performance Fabrics', origin: 'United States', civilization: 'American', yearIntroduced: '1969 CE', description: 'Bob Gore discovered that expanded PTFE (Teflon) membrane was waterproof yet breathable — water vapor could pass through while rain could not. Gore-Tex revolutionized outdoor clothing, military gear, and medical implants.', impact: 'Made truly waterproof-breathable clothing possible. Gore-Tex technology extended into architecture, medicine, and aerospace.' },

  { slug: 'kevlar', name: 'Kevlar', era: 'contemporary', category: 'armor', subcategory: 'Protective Fabrics', origin: 'United States', civilization: 'American', yearIntroduced: '1965 CE', description: 'Stephanie Kwolek at DuPont created an aramid fiber 5x stronger than steel per unit weight. Kevlar body armor has saved thousands of lives. It\'s also used in tires, boat hulls, aircraft, and spacecraft.', impact: 'Transformed personal protection. Kevlar body armor made it survivable to be shot — changing military and police operations worldwide.' },

  { slug: 'sustainable-fashion', name: 'Sustainable Fashion Movement', era: 'contemporary', category: 'trade', subcategory: 'Ethical Fashion', origin: 'Global', civilization: 'Global', yearIntroduced: '~2013 CE', description: 'The Rana Plaza factory collapse (2013, 1,134 deaths) galvanized the sustainable fashion movement. Brands now face pressure for ethical supply chains, organic materials, circular design, and living wages. "Who made my clothes?" became a global campaign.', impact: 'Challenging the fast fashion model. The concept of fashion as an ethical choice is reshaping consumer expectations worldwide.' },

  { slug: 'smart-textiles', name: 'Smart Textiles & Wearables', era: 'contemporary', category: 'modern', subcategory: 'Digital Fabrics', origin: 'Global', civilization: 'Global', yearIntroduced: '~2015 CE', description: 'Clothing embedded with sensors, conductive fibers, and electronics. Examples: Google\'s Project Jacquard (touch-sensitive denim), heated jackets, biometric shirts for athletes, and color-changing fabrics responsive to temperature.', impact: 'Merging clothing with computing. Smart textiles may transform health monitoring, military gear, and the boundary between body and technology.' },

  { slug: 'sneaker-culture', name: 'Sneaker Culture', era: 'contemporary', category: 'garment', subcategory: 'Footwear Revolution', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '~1984 CE', description: 'Michael Jordan\'s Air Jordan 1 (1985) created sneaker culture — shoes as collectibles, status symbols, and identity markers. Limited releases create frenzies. The global sneaker resale market tops $10 billion annually.', impact: 'Sneakers became the defining fashion item of late capitalism — merging sport, hip-hop culture, and luxury branding into a global phenomenon.' },

  { slug: 'athleisure', name: 'Athleisure', era: 'contemporary', category: 'garment', subcategory: 'Lifestyle Fashion', origin: 'United States / Global', civilization: 'Global', yearIntroduced: '~2010 CE', description: 'The blurring of athletic and casual wear — yoga pants, performance sneakers, and technical fabrics worn as everyday clothing. Lululemon, Nike, and Adidas built empires on the idea that activewear is real clothing.', impact: 'The most significant shift in everyday dress since jeans. COVID-19 accelerated the trend as remote work made comfort the priority.' },
]
