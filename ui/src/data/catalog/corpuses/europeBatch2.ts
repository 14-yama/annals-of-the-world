/**
 * European Post-Classical Corpuses — Batch 2
 *
 * 14. GEORGIAN_CORPUS
 * 15. MAGYAR_HUNGARIAN_CORPUS
 * 16. POLISH_LITHUANIAN_CORPUS
 * 17. CZECH_BOHEMIAN_CORPUS
 * 18. BALKAN_SLAVIC_CORPUS
 * 19. ROMANIAN_MOLDAVIAN_CORPUS
 * 20. VENETIAN_CORPUS
 * 21. SICILIAN_NORMAN_CORPUS
 * 22. MALTESE_CORPUS
 * 23. CYPRIOT_CORPUS
 * 24. GREEK_MEDIEVAL_CORPUS
 * 25. ALBANIAN_CORPUS
 */
import type { Entity } from '../../entityTypes'

export const EUROPE_BATCH2_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  14. GEORGIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'georgian_corpus',
    name: 'The Georgian Corpus',
    label: 'Text',
    callNumber: '730.38-georgian-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Religious Texts — Georgian Christian Tradition'],
    subjects: ['Georgian Alphabet', 'Knight in Panther Skin', 'Shota Rustaveli', 'Kartlis Tskhovreba', 'Caucasus', 'Hagiography'],
    summary: 'The Georgian Corpus encompasses the literary, historical, theological, and legal heritage of the Georgian people and their unique Kartvelian civilization in the Caucasus. Georgia adopted Christianity c. 337 CE, and its literary tradition is anchored by its own alphabet — one of only 14 independent writing systems in the world. The supreme literary achievement is Shota Rustaveli\'s The Knight in the Panther\'s Skin (Vepkhistqaosani, c. 1189–1207) — a 1,600-quatrain epic poem of courtly love, friendship, and chivalric virtue, which Georgians consider their national masterwork. It was written during the Golden Age of the Georgian Kingdom under Queen Tamar (r. 1184–1213), when Georgia reached its greatest territorial extent and cultural flowering. Other key works include: the Kartlis Tskhovreba (Chronicle of Georgia — the comprehensive national history compiled over centuries); the Martyrdom of Shushanik (5th century — the oldest surviving work of Georgian literature); Georgian hagiographies (lives of St. Nino, the evangelist of Georgia); Georgian Bible translations from the 5th century; and the corpus of Georgian polyphonic hymns (UNESCO Intangible Heritage). Georgia\'s mountainous isolation allowed its literary tradition to develop with remarkable independence from neighboring Byzantine, Persian, and Arab cultures.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 337 CE – 1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Georgia converts to Christianity under St. Nino', type: 'Event', year: 'c. 337 CE' },
    ],
    effects: [
      { title: 'The Knight in the Panther\'s Skin — Georgian national masterwork', type: 'Text', year: 'c. 1200 CE' },
      { title: 'Georgian polyphonic hymns recognized as UNESCO heritage', type: 'Evidence', year: '2001 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Tbilisi', role: 'Georgian capital and center of literary culture' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  15. MAGYAR / HUNGARIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'magyar_hungarian_corpus',
    name: 'The Magyar / Hungarian Corpus',
    label: 'Text',
    callNumber: '730.39-magyar-hungarian-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — Hungarian Medieval Tradition'],
    subjects: ['Gesta Hungarorum', 'Golden Bull 1222', 'Halotti Beszéd', 'Matthias Corvinus', 'Bibliotheca Corviniana', 'Pannonian Basin'],
    summary: 'The Magyar / Hungarian Corpus encompasses the literary, legal, and historical heritage of the Kingdom of Hungary from the Árpád dynasty through the Renaissance court of Matthias Corvinus. The Hungarians (Magyars) — a Uralic-speaking people who settled the Pannonian (Carpathian) Basin c. 895 CE — adopted Christianity under King Stephen I (r. 1000–1038) and produced a remarkable literary culture blending Latin Christendom with Central Asian heritage. Key works include: the Gesta Hungarorum (Deeds of the Hungarians, c. 1200) by "Anonymus" — the earliest Hungarian chronicle, narrating the Magyar conquest in heroic Latin prose; the Halotti Beszéd és Könyörgés (Funeral Sermon and Prayer, c. 1192–1195) — the oldest surviving continuous Hungarian-language text; the Golden Bull of 1222 — Hungary\'s charter of noble rights, issued just seven years after England\'s Magna Carta, which limited royal power and established noble privileges; and the Bibliotheca Corviniana (c. 1458–1490) — the legendary library of King Matthias Corvinus, one of the largest and most splendid libraries in Renaissance Europe (estimated 2,000–2,500 volumes of beautifully illuminated corvinae), second only to the Vatican. Though largely dispersed after the Ottoman conquest (1526), surviving corvinae are UNESCO Memory of the World treasures.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1000–1526 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Magyar settlement of the Carpathian Basin', type: 'Event', year: 'c. 895 CE' },
      { title: 'Christianization of Hungary under King Stephen I', type: 'Person', year: '1000 CE' },
    ],
    effects: [
      { title: 'Golden Bull of 1222 — early charter of constitutional rights', type: 'Text', year: '1222 CE' },
      { title: 'Bibliotheca Corviniana — among the greatest Renaissance libraries', type: 'Evidence', year: 'c. 1480 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Buda', role: 'Hungarian capital and site of the Corvinian Library' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  16. POLISH-LITHUANIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'polish_lithuanian_corpus',
    name: 'The Polish-Lithuanian Corpus',
    label: 'Text',
    callNumber: '730.40-polish-lithuanian-corpus',
    subjectHeadings: ['Artifacts & Texts — Historical & Legal Texts — Polish-Lithuanian Commonwealth'],
    subjects: ['Długosz', 'Copernicus', 'Kraków Academy', 'Nihil Novi', 'Sarmatism', 'Statutes of Lithuania', 'Elective Monarchy'],
    summary: 'The Polish-Lithuanian Corpus encompasses the literary, legal, scientific, and historical output of the Polish Crown and the Grand Duchy of Lithuania — which formed the enormous Polish-Lithuanian Commonwealth (1569–1795), at its peak the largest state in Europe. Key works include: Jan Długosz\'s Annales seu Cronicae Incliti Regni Poloniae (Annals of Poland, 12 volumes, completed 1480) — the most comprehensive medieval chronicle of any Central European nation; the Nihil Novi act of 1505 ("nothing new [without the common consent]") — a constitutional milestone establishing that no laws could be passed without the agreement of the Sejm (parliament); the Statutes of Lithuania (three editions: 1529, 1566, 1588) — remarkable legal codes for the Grand Duchy, compiled in Chancery Slavonic/Polish; Nicolaus Copernicus\'s De Revolutionibus Orbium Coelestium (1543) — the heliocentric revolution, written at Frombork in Royal Prussia; and the literary legacy of Polish Golden Age humanism (Jan Kochanowski\'s Treny — elegiac laments, 1580, the finest lyric poetry in Renaissance Polish). The Commonwealth\'s tradition of religious tolerance (Warsaw Confederation of 1573 — the first European act of religious freedom) and elective monarchy represents a unique political experiment.',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1000–1795 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Union of Lublin creates the Polish-Lithuanian Commonwealth', type: 'Event', year: '1569 CE' },
    ],
    effects: [
      { title: 'Copernicus publishes heliocentric theory', type: 'Text', year: '1543 CE' },
      { title: 'Warsaw Confederation — first European act of religious freedom', type: 'Text', year: '1573 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Kraków', role: 'Royal capital and home of Jagiellonian University (1364)' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  17. CZECH / BOHEMIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'czech_bohemian_corpus',
    name: 'The Czech / Bohemian Corpus',
    label: 'Text',
    callNumber: '730.41-czech-bohemian-corpus',
    subjectHeadings: ['Artifacts & Texts — Historical & Religious Texts — Bohemian Tradition'],
    subjects: ['Jan Hus', 'Hussite', 'Cosmas of Prague', 'Czech Bible', 'Charles University', 'Prague', 'Kralice Bible'],
    summary: 'The Czech / Bohemian Corpus encompasses the literary, historical, theological, and legal heritage of the Bohemian Crown lands — a culturally rich kingdom at the heart of Central Europe. The corpus is defined by two extraordinary episodes: the reign of Holy Roman Emperor Charles IV (r. 1346–1378), who made Prague the cultural capital of the Empire and founded Charles University (1348, the first university in Central Europe); and the Hussite movement (1415–1436), when Jan Hus\'s reformist preaching (anticipating Luther by a century) ignited a revolutionary religious and national movement. Key works include: the Chronica Boemorum of Cosmas of Prague (c. 1119–1125) — the foundational Czech chronicle; the writings and letters of Jan Hus (c. 1369–1415), including De Ecclesia (On the Church, 1413) — a radical challenge to papal authority that contributed to his burning at the Council of Constance; the Czech Bible tradition (the Leskovecko-Drážďanská Bible, c. 1360 — one of the earliest complete Bible translations into any modern European language); the Kralice Bible (1579–1593, by the Bohemian Brethren — one of the finest vernacular Bible translations, comparable in literary influence to the King James Version for English); and Czech hymnals that made Bohemia a pioneer of congregational singing in the vernacular.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1100–1620 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Charles IV makes Prague the cultural capital of the Holy Roman Empire', type: 'Person', year: 'c. 1350 CE' },
    ],
    effects: [
      { title: 'Jan Hus\'s reform movement anticipates the Protestant Reformation by a century', type: 'Person', year: '1415 CE' },
      { title: 'Kralice Bible — masterpiece of Czech literary language', type: 'Text', year: '1593 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Prague', role: 'Bohemian capital — center of Czech literary culture' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  18. BALKAN SLAVIC CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'balkan_slavic_corpus',
    name: 'The Balkan Slavic Corpus',
    label: 'Text',
    callNumber: '730.42-balkan-slavic-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — South Slavic Tradition'],
    subjects: ['Serbian', 'Bulgarian', 'Bosnian', 'Saint Sava', 'Tsar Samuel', 'Zakonopravilo', 'Epic Poetry', 'Kosovo Cycle'],
    summary: 'The Balkan Slavic Corpus encompasses the literary, legal, religious, and oral heritage of the South Slavic peoples — primarily the Serbs, Bulgarians, and Bosnians — whose intertwined histories shaped the cultural landscape of Southeastern Europe. Key works include: the Zakonopravilo (Nomocanon) of Saint Sava (1219) — the foundational legal code of medieval Serbia, synthesizing Byzantine canon law with Serbian customary law, compiled by St. Sava Nemanjić (patron saint of Serbian education and culture); the Life of St. Simeon by St. Sava — the first work of Serbian hagiographic literature; the Bulgarian literary schools of Ohrid (founded by St. Clement of Ohrid, c. 893 — the first Slavic-language university) and Tarnovo (14th century); the Bosnian Church\'s Slavic manuscripts and tombstone inscriptions (stećci — UNESCO heritage); and one of the world\'s greatest oral epic traditions — the South Slavic heroic poems collected by Vuk Stefanović Karadžić in the 19th century, centered on the Kosovo Cycle (the Battle of Kosovo, 1389). These oral epics, performed by gusle-playing bards, were studied by Milman Parry and Albert Lord in the 1930s, leading to the Oral Theory that transformed Homeric scholarship.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 800–1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Christianization of the South Slavs by Byzantine missionaries', type: 'Event', year: 'c. 860 CE' },
    ],
    effects: [
      { title: 'St. Sava\'s Zakonopravilo establishes Serbian legal and ecclesiastical tradition', type: 'Text', year: '1219 CE' },
      { title: 'South Slavic oral epics inspire the Parry-Lord Oral Theory', type: 'Idea', year: '1935 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Ohrid', role: 'First Slavic literary school (893 CE)' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  19. ROMANIAN / MOLDAVIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'romanian_moldavian_corpus',
    name: 'The Romanian / Moldavian Corpus',
    label: 'Text',
    callNumber: '730.43-romanian-moldavian-corpus',
    subjectHeadings: ['Artifacts & Texts — Historical & Religious Texts — Romanian Tradition'],
    subjects: ['Wallachia', 'Moldavia', 'Slavonic', 'Neacșu Letter', 'Stephen the Great', 'Painted Monasteries', 'Chronicle'],
    summary: 'The Romanian / Moldavian Corpus encompasses the literary, historical, and religious heritage of the Romanian-speaking principalities — Wallachia, Moldavia, and Transylvania — across their medieval and early modern periods. Unique among the Romance-speaking peoples of Europe, the Romanians used the Cyrillic (Old Church Slavonic) script for their official and religious texts until the 19th century, creating a fascinating bilingual literary culture. Key works include: the Neacșu Letter (1521) — the oldest surviving document written in Romanian, a brief but precious letter warning of an Ottoman military movement; the Internal Slavonic chronicles of Stephen III the Great of Moldavia (r. 1457–1504), who fought 36 battles against the Ottomans, Poles, and Hungarians; the Moldavian chronicles of Grigore Ureche (Letopisețul Țării Moldovei, 1642–1647) and Miron Costin; the religious manuscripts of the painted monasteries of Bucovina (Voroneț, Sucevița, Moldovița — UNESCO sites whose exterior biblical frescoes are among the greatest achievements of medieval art); and Dimitrie Cantemir\'s Descriptio Moldaviae (1714–1716) — a pioneering Enlightenment-era geographical and ethnographic description, written by the prince of Moldavia who was also an Ottoman scholar and member of the Berlin Academy of Sciences.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1300–1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Formation of the principalities of Wallachia and Moldavia', type: 'Event', year: 'c. 1300 CE' },
    ],
    effects: [
      { title: 'Neacșu Letter — oldest surviving Romanian-language document', type: 'Evidence', year: '1521 CE' },
      { title: 'Painted monasteries of Bucovina — UNESCO-recognized masterworks', type: 'Evidence', year: 'c. 1500 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Suceava', role: 'Capital of medieval Moldavia' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  20. VENETIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'venetian_corpus',
    name: 'The Venetian Corpus',
    label: 'Text',
    callNumber: '730.44-venetian-corpus',
    subjectHeadings: ['Artifacts & Texts — Commercial & Diplomatic Texts — Republic of Venice'],
    subjects: ['Venice', 'Marco Polo', 'Trade', 'Diplomacy', 'Senate Deliberations', 'Maritime Law', 'Aldus Manutius'],
    summary: 'The Venetian Corpus encompasses the commercial, diplomatic, legal, and literary records of the Republic of Venice (Serenissima Repubblica di Venezia, c. 697–1797 CE) — the longest-lived republic in world history and one of the greatest maritime powers. Venice\'s meticulous bureaucratic culture produced, over a millennium, an archival corpus of extraordinary depth. Key works include: the Venetian Senate deliberations and diplomatic dispatches (relazioni) — systematic reports by Venetian ambassadors across Europe and the Ottoman Empire, providing unparalleled intelligence on foreign courts and constituting one of the most valuable sources for European diplomatic history; Marco Polo\'s Il Milione (The Travels, c. 1298) — dictated in a Genoese prison, the most influential travel account in Western history, which introduced Europe to the vastness of the Mongol Empire and China; Venetian maritime law (statutes governing trade, navigation, and shipbuilding at the Arsenal — the largest industrial complex in the pre-modern world); the Aldine Press of Aldus Manutius (founded 1494) — which revolutionized European publishing by introducing italic type, the pocket-sized octavo format, and authoritative editions of Greek classics; and the Venetian State Archives (Archivio di Stato) — containing 80+ linear kilometers of documents, one of the most complete records of any pre-modern state.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 697–1797 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Venice emerges as a major trading power', type: 'Institution', year: 'c. 900 CE' },
    ],
    effects: [
      { title: 'Marco Polo\'s Travels introduces Europe to the Mongol Empire and China', type: 'Text', year: '1298 CE' },
      { title: 'Aldine Press revolutionizes publishing with italic type and pocket format', type: 'Institution', year: '1494 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Venice', role: 'Capital of the Serenissima and center of Venetian literary culture' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  21. SICILIAN-NORMAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'sicilian_norman_corpus',
    name: 'The Sicilian-Norman Corpus',
    label: 'Text',
    callNumber: '730.45-sicilian-norman-corpus',
    subjectHeadings: ['Artifacts & Texts — Administrative & Literary Texts — Norman Kingdom of Sicily'],
    subjects: ['Sicily', 'Roger II', 'Frederick II', 'Sicilian School', 'Al-Idrisi', 'Constitutions of Melfi', 'Trilingual'],
    summary: 'The Sicilian-Norman Corpus encompasses the literary, scientific, legal, and administrative heritage of the Norman Kingdom of Sicily and its Hohenstaufen successor (c. 1061–1266 CE) — a unique trilingual civilization where Latin, Greek, and Arabic coexisted in a remarkable multicultural synthesis. Key works include: the Tabula Rogeriana (1154) by the Arab geographer Muhammad al-Idrisi — the most accurate world map of the medieval period, commissioned by the Norman King Roger II; the poetry of the Sicilian School (c. 1220–1260) at the court of Holy Roman Emperor Frederick II — which invented the sonnet form (later perfected by Petrarch and Shakespeare), making Sicily the birthplace of Italian vernacular poetry; the Constitutions of Melfi (Liber Augustalis, 1231) — Frederick II\'s comprehensive legal code, the most advanced secular law code in medieval Europe, anticipating modern state administration; and the diplomatic, administrative, and monastic records preserved in Latin, Greek, and Arabic — including bilingual and trilingual charters that document the integration of Norman, Byzantine, and Arab administrative traditions. The Norman Roger II\'s royal mantle (1133), with its Arabic inscription and Byzantine-style lions, symbolizes this extraordinary cultural fusion.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1061–1266 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Norman conquest of Sicily creates trilingual Latin-Greek-Arabic society', type: 'Event', year: '1061 CE' },
    ],
    effects: [
      { title: 'Sicilian School invents the sonnet form', type: 'Text', year: 'c. 1230 CE' },
      { title: 'Al-Idrisi\'s Tabula Rogeriana — most accurate medieval world map', type: 'Text', year: '1154 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Palermo', role: 'Capital of the Norman Kingdom of Sicily — trilingual court' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  22. MALTESE CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'maltese_corpus',
    name: 'The Maltese Corpus',
    label: 'Text',
    callNumber: '730.46-maltese-corpus',
    subjectHeadings: ['Artifacts & Texts — Historical Texts — Maltese / Knights Hospitaller Tradition'],
    subjects: ['Malta', 'Knights Hospitaller', 'Great Siege 1565', 'Cantilena', 'Maltese Language', 'Mediterranean'],
    summary: 'The Maltese Corpus encompasses the literary, administrative, and historical heritage of the Maltese Islands — a Mediterranean crossroads whose unique Semitic-Romance bilingual culture reflects centuries of Arab, Norman, Aragonese, Hospitaller, and British rule. Key texts include: the Cantilena (Il-Kantilena, attributed to Pietru Caxaro, c. 1450–1485) — the oldest known literary text in Maltese (a Semitic language written in Latin script — the only such language in Europe); the extensive archives of the Sovereign Military Order of St. John (Knights Hospitaller), who ruled Malta from 1530 to 1798 — documenting Mediterranean naval warfare, diplomacy, medical care, and fortification engineering; accounts of the Great Siege of Malta (1565), when the Knights and Maltese population repelled an Ottoman invasion force of 40,000+, one of the decisive battles of the Mediterranean world; and the records of Malta\'s role as a center of Mediterranean trade, piracy suppression, and cultural exchange between Christian Europe and the Islamic world. The Maltese language itself — Arabic in structure overlaid with Sicilian and Italian vocabulary — is a living linguistic monument to the island\'s multicultural history.',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1091–1798 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Knights Hospitaller establish Malta as their headquarters', type: 'Institution', year: '1530 CE' },
    ],
    effects: [
      { title: 'Great Siege of Malta saves Christian Mediterranean from Ottoman advance', type: 'Event', year: '1565 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Valletta', role: 'Built by the Knights after the Great Siege — Hospitaller capital' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  23. CYPRIOT CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'cypriot_corpus',
    name: 'The Cypriot Corpus',
    label: 'Text',
    callNumber: '730.47-cypriot-corpus',
    subjectHeadings: ['Artifacts & Texts — Administrative & Literary Texts — Medieval Cyprus'],
    subjects: ['Lusignan', 'Cyprus', 'Crusader', 'Chronicle of Leontios Makhairas', 'Frankish', 'Nicosia'],
    summary: 'The Cypriot Corpus encompasses the literary, administrative, and historical records of medieval and early modern Cyprus — a strategically essential island at the crossroads of the Byzantine, Latin Crusader, Venetian, and Ottoman worlds. Following its conquest by Richard I of England during the Third Crusade (1191) and subsequent sale to the Lusignan dynasty, Cyprus became the last functioning Crusader state (Kingdom of Cyprus, 1192–1489). Key texts include: the Chronicle of Leontios Makhairas (early 15th century) — written in Cypriot Greek, the most detailed and vivid narrative of the Lusignan period, covering the period from Richard I\'s conquest to the 1430s; the Chronicle of George Boustronios (late 15th century) — continuing where Makhairas left off through the Venetian takeover; the Assises of Jerusalem (the Crusader legal code, used extensively on Cyprus); Lusignan royal charters in French, Latin, and Greek; and records from the Venetian administration (1489–1571) and Ottoman period (1571–1878). The Cypriot corpus uniquely documents the coexistence and friction between Latin Catholic and Greek Orthodox Christian communities under Frankish rule — a medieval predecessor to modern debates about cultural plurality.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: '1191–1878 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Richard I conquers Cyprus during the Third Crusade', type: 'Event', year: '1191 CE' },
    ],
    effects: [
      { title: 'Cyprus becomes the last functioning Crusader state', type: 'Institution', year: '1192 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Nicosia', role: 'Capital of the Lusignan Kingdom of Cyprus' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  24. GREEK MEDIEVAL CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'greek_medieval_corpus',
    name: 'The Greek Medieval Corpus',
    label: 'Text',
    callNumber: '730.48-greek-medieval-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Religious Texts — Post-Byzantine Greek Tradition'],
    subjects: ['Cretan Renaissance', 'Erotokritos', 'Digenis Akritas', 'Venetian Crete', 'Demotic Greek', 'Folk Song'],
    summary: 'The Greek Medieval Corpus encompasses the vernacular (demotic) Greek literary heritage produced outside the main Byzantine court tradition — particularly the texts from Crete during Venetian rule (1204–1669), the Greek provinces, and the post-1453 diaspora. While the Byzantine Corpus covers the high literary tradition of Constantinople in learned Greek, this corpus captures the vibrant popular literature in the regional Greek vernacular. Key works include: the Digenis Akritas (10th–12th century) — the Byzantine folk epic of a half-Arab, half-Greek border warrior on the eastern frontier, the earliest known work of modern Greek literature; the Cretan Renaissance (16th–17th century) — a flowering of Greek literature under Venetian rule, whose masterwork is Vitsentzos Kornaros\'s Erotokritos (c. 1600–1669), a 10,000-line verse romance of unwavering love considered one of the greatest works of modern Greek literature; the Sacrifice of Abraham (Erophili) — a Cretan drama influenced by the Italian Renaissance; Greek folk songs (demotika tragoudia) — an extraordinary oral tradition spanning centuries and regions, documenting klephtic resistance, love, death, and the experience of Ottoman rule; and the scholarly output of Greek émigrés in Venice, Padua, and Rome who preserved and transmitted Greek identity during Ottoman domination.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 900–1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Venetian rule in Crete stimulates Greek Renaissance literature', type: 'Event', year: '1204 CE' },
    ],
    effects: [
      { title: 'Erotokritos — masterwork of modern Greek literature', type: 'Text', year: 'c. 1650 CE' },
      { title: 'Greek folk song tradition preserves national identity under Ottoman rule', type: 'Evidence', year: 'c. 1500 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Heraklion', role: 'Center of the Cretan Renaissance (Venetian Candia)' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  25. ALBANIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'albanian_corpus',
    name: 'The Albanian Corpus',
    label: 'Text',
    callNumber: '730.49-albanian-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Historical Texts — Albanian Tradition'],
    subjects: ['Skanderbeg', 'Gjon Buzuku', 'Meshari', 'Kanun', 'Arbëreshë', 'Illyrian', 'Ottoman Albania'],
    summary: 'The Albanian Corpus encompasses the literary, legal, and historical heritage of the Albanian-speaking peoples — speakers of a unique Indo-European language that forms its own branch, possibly descended from ancient Illyrian. Albania\'s late emergence as a literary culture (its alphabet was not standardized until 1908) makes the surviving earlier texts exceptionally precious. Key works include: the Meshari (Missal) of Gjon Buzuku (1555) — the earliest known printed book in Albanian, a Catholic liturgical text that provides the oldest substantial sample of the language; the Kanun of Lekë Dukagjini — an orally transmitted customary law code governing northern Albanian tribal society (formally compiled by Shtjefën Gjeçovi in the early 20th century but dating to the 15th century), regulating blood feuds (gjakmarrja), hospitality (besa — the sacred oath of honor), property, marriage, and governance; the letters and chronicles of Marin Barleti (Historia de Vita et Gestis Scanderbegi, 1508–1510), documenting the epic resistance of Gjergj Kastrioti Skanderbeg against the Ottoman Empire (1443–1468) — Albania\'s national hero; and the literature of the Arbëreshë (Italo-Albanian diaspora in southern Italy, from the 15th century) who preserved Albanian language and culture in exile. The Albanian oral tradition — especially the epic songs of the Lahuta (northern Albanian one-stringed fiddle) — connects this corpus to the broader Balkan heroic tradition.',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1400–1900 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION'],
    causes: [
      { title: 'Skanderbeg\'s resistance preserves Albanian identity against Ottoman conquest', type: 'Person', year: '1443 CE' },
    ],
    effects: [
      { title: 'Meshari of Buzuku — first printed book in Albanian', type: 'Text', year: '1555 CE' },
      { title: 'Kanun of Lekë Dukagjini — customary law preserved for centuries', type: 'Text', year: 'c. 1400 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Krujë', role: 'Castle of Skanderbeg — center of Albanian resistance' },
    ],
    texts: [],
  },
]
