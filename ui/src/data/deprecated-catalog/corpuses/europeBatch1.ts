/**
 * European Post-Classical Corpuses — Batch 1
 *
 * 1. BYZANTINE_CORPUS
 * 2. SLAVIC_ORTHODOX_CORPUS
 * 3. MEDIEVAL_LATIN_CORPUS
 * 4. CAROLINGIAN_FRANKISH_CORPUS
 * 5. IBERIAN_CORPUS
 * 6. ITALIAN_COMMUNAL_CORPUS
 * 7. FRENCH_MEDIEVAL_CORPUS
 * 8. GERMANIC_MEDIEVAL_CORPUS
 * 9. CELTIC_MEDIEVAL_CORPUS
 * 10. VIKING_NORDIC_CORPUS
 * 11. OTTOMAN_BALKAN_CORPUS
 * 12. JUDEO_SEPHARDIC_CORPUS
 * 13. ARMENIAN_CORPUS
 */
import type { Entity } from '../../entityTypes'

export const EUROPE_BATCH1_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  1. BYZANTINE CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'byzantine_corpus',
    name: 'The Byzantine Corpus',
    label: 'Text',
    callNumber: '730.25-byzantine-corpus',
    subjectHeadings: ['Artifacts & Texts — Imperial Texts — Byzantine Christian Literature'],
    subjects: ['Byzantium', 'Constantinople', 'Justinian', 'Procopius', 'Anna Komnene', 'Greek', 'Orthodox Christianity', 'Roman Law'],
    summary: 'The Byzantine Corpus comprises the vast literary, legal, historiographic, and theological output of the Eastern Roman (Byzantine) Empire from its effective foundation by Constantine I (330 CE) to the fall of Constantinople (1453 CE). As the direct continuation of the Roman Empire in the East, Byzantium preserved and transmitted Greek classical learning through centuries when it was largely lost in Western Europe. Key works include: the Corpus Iuris Civilis of Justinian I (529–534 CE, shared with the Graeco-Roman corpus) — the codification of Roman law that became the foundation of European legal tradition; the histories of Procopius (Secret History, Wars), Theophanes the Confessor, Anna Komnene (the Alexiad — the first historical work by a woman in the Western tradition), and Michael Psellos; the Suda (10th-century encyclopedic lexicon of 30,000+ entries); the Bibliotheca of Photius (9th century — summaries of 280 classical works, many now lost); and a rich tradition of theological literature (Church Fathers, conciliar acts, hymnography). The Byzantine preservation of Greek texts — through continuous copying in scriptoria — made possible the Italian Renaissance when Greek scholars fled Constantinople after 1453.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: '330–1453 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Constantine founds Constantinople as New Rome', type: 'Event', year: '330 CE' },
    ],
    effects: [
      { title: 'Justinian\'s Corpus Iuris Civilis becomes foundation of European law', type: 'Text', year: '534 CE' },
      { title: 'Byzantine preservation of Greek texts enables the Italian Renaissance', type: 'Idea', year: 'c. 1400 CE' },
    ],
    relationships: [
      { sourceSlug: 'byzantine_corpus', sourceName: 'The Byzantine Corpus', verb: 'CONTAINS', targetSlug: 'alexiad_anna_komnene', targetName: 'The Alexiad', context: 'First history by a woman in the Western tradition' },
    ],
    places: [
      { name: 'Constantinople', role: 'Byzantine capital and center of literary culture' },
    ],
    texts: [],
  },
  {
    slug: 'alexiad_anna_komnene',
    name: 'The Alexiad',
    label: 'Text',
    callNumber: '730.111-alexiad',
    subjectHeadings: ['Artifacts & Texts — Historical Texts — Byzantine Historiography'],
    subjects: ['Anna Komnene', 'Alexios I', 'First Crusade', 'Constantinople', 'Byzantine Princess', 'Female Historian'],
    summary: 'A history of the reign of Emperor Alexios I Komnenos (r. 1081–1118) written by his daughter, the Byzantine princess and scholar Anna Komnene (1083–1153), completed c. 1148. The Alexiad is remarkable on multiple counts: it is the first major historical work by a woman in the Western literary tradition; it provides the primary Byzantine perspective on the First Crusade (1096–1099), describing the Frankish crusaders from the viewpoint of the sophisticated Eastern Roman Empire; and it demonstrates Anna\'s mastery of classical Greek historiographic conventions (modeling herself after Thucydides and Polybius). The work\'s vivid character portraits, including her admiring but critical depiction of her father and her wary descriptions of the Norman adventurer Bohemond of Taranto, make it one of the finest works of medieval historiography.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1148 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Primary Byzantine source on the First Crusade', type: 'Evidence', year: 'c. 1148 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Constantinople', role: 'Anna\'s lifelong home and writing site' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  2. SLAVIC ORTHODOX CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'slavic_orthodox_corpus',
    name: 'The Slavic Orthodox Corpus',
    label: 'Text',
    callNumber: '730.26-slavic-orthodox-corpus',
    subjectHeadings: ['Artifacts & Texts — Historical & Religious Texts — Eastern Slavic Literature'],
    subjects: ['Russian Primary Chronicle', 'Old Church Slavonic', 'Cyrillic', 'Nestor', 'Orthodox', 'Rus\'', 'Kiev', 'Moscow'],
    summary: 'The Slavic Orthodox Corpus encompasses the historical, religious, and literary texts of the Eastern and South Slavic Orthodox Christian civilizations — primarily the Kievan Rus\', Muscovite Russia, Bulgaria, and Serbia — written in Old Church Slavonic and its regional variants. The foundational text is the Russian Primary Chronicle (Povest\' Vremennykh Let, c. 1113 CE), attributed to the monk Nestor of the Caves Monastery in Kiev, narrating the history of the East Slavic peoples from the biblical table of nations through the Varangian princes to 1110 CE. Other key works include: the Russkaya Pravda (Rus\' Law Code, 11th century), the earliest East Slavic legal code; the Tale of Igor\'s Campaign (Slovo o Polku Igoreve, c. 1185–1187), the greatest work of Old Slavic secular literature; the Domostroi (16th century, a guide to household management and morality); and the vast body of Orthodox liturgical texts, saints\' lives, and chronicles. The corpus also includes the Cyrillic alphabet — created by Saints Cyril and Methodius (9th century) to translate the Bible into Slavonic, giving the Slavic peoples their written tradition.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: '863 CE – 1700 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Saints Cyril and Methodius create Slavonic alphabet for Bible translation', type: 'Person', year: '863 CE' },
      { title: 'Conversion of Kievan Rus\' to Orthodox Christianity', type: 'Event', year: '988 CE' },
    ],
    effects: [
      { title: 'Cyrillic script becomes the writing system of Russia, Bulgaria, Serbia, and others', type: 'Idea', year: 'c. 900 CE' },
      { title: 'Russian Primary Chronicle establishes the historical identity of the Rus\' peoples', type: 'Text', year: 'c. 1113 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Kiev', role: 'Center of early East Slavic literary culture' },
      { name: 'Moscow', role: 'Later center of Muscovite literary production' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  3. MEDIEVAL LATIN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'medieval_latin_corpus',
    name: 'The Medieval Latin Corpus',
    label: 'Text',
    callNumber: '730.27-medieval-latin-corpus',
    subjectHeadings: ['Artifacts & Texts — Scholarly Texts — Latin Christendom'],
    subjects: ['Scholasticism', 'Thomas Aquinas', 'Summa Theologica', 'Papal Bulls', 'Monastic Rules', 'University', 'Latin', 'Christendom'],
    summary: 'The Medieval Latin Corpus encompasses the vast body of scholarly, theological, legal, and administrative texts produced in Latin — the universal language of learning, law, and the Church — across Western Christendom from c. 500 to 1500 CE. Its intellectual pinnacle is the Scholastic tradition: Thomas Aquinas\'s Summa Theologica (1265–1274, the most systematic synthesis of Christian theology and Aristotelian philosophy); Peter Lombard\'s Sentences (c. 1150, the standard theology textbook for 400 years); Anselm\'s Proslogion (the ontological argument for God); and Abelard\'s Sic et Non. The corpus includes: papal bulls and decretals governing Christendom; monastic rules (the Rule of St. Benedict, c. 530 — the charter of Western monasticism); university statutes and disputations; natural philosophy (Roger Bacon, Albertus Magnus); and histories (Bede\'s Ecclesiastical History of the English People, c. 731 — the foundational work of English historiography). Medieval Latin was the operating system of European intellectual life for a millennium.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 500–1500 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Latin Church maintains linguistic unity across post-Roman Europe', type: 'Institution', year: 'c. 500 CE' },
    ],
    effects: [
      { title: 'Summa Theologica becomes masterwork of Christian philosophy', type: 'Text', year: '1274 CE', slug: 'summa_theologica' },
      { title: 'Rule of St. Benedict shapes Western monasticism for 1,500 years', type: 'Text', year: 'c. 530 CE' },
      { title: 'Medieval universities (Bologna, Paris, Oxford) create institutional model of higher education', type: 'Institution', year: 'c. 1088 CE' },
    ],
    relationships: [
      { sourceSlug: 'medieval_latin_corpus', sourceName: 'The Medieval Latin Corpus', verb: 'CONTAINS', targetSlug: 'summa_theologica', targetName: 'Summa Theologica', context: 'Greatest synthesis of medieval philosophy' },
    ],
    places: [
      { name: 'Paris', role: 'Center of Scholastic philosophy and theology' },
      { name: 'Rome', role: 'Center of papal administration' },
    ],
    texts: [],
  },
  {
    slug: 'summa_theologica',
    name: 'Summa Theologica',
    label: 'Text',
    callNumber: '730.112-summa-theologica',
    subjectHeadings: ['Artifacts & Texts — Theological Texts — Scholastic Philosophy'],
    subjects: ['Thomas Aquinas', 'Scholasticism', 'Natural Law', 'Five Ways', 'Aristotle', 'Catholic Theology'],
    summary: 'The magnum opus of Thomas Aquinas (1225–1274), the most comprehensive and systematic work of Christian theology and philosophy ever written. Composed between 1265 and 1274 (left unfinished at Aquinas\'s death), the Summa contains 512 questions, 2,669 articles, and approximately 10,000 objections and replies, organized in three parts: God\'s existence and nature (including the Five Ways or proofs for God\'s existence); moral theology (virtue, law, grace); and Christology and the sacraments. Aquinas achieved an unprecedented synthesis of Aristotelian philosophy with Christian revelation, establishing the framework of natural law theory that profoundly influenced Western legal, political, and ethical thought. Pope Leo XIII declared the Summa the definitive expression of Catholic philosophy (1879), and it remains the standard reference in Catholic seminaries.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: '1265–1274 CE',
    frameworks: ['DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Definitive synthesis of Christian theology and Aristotelian philosophy', type: 'Idea', year: '1274 CE' },
      { title: 'Natural law theory influences Western legal and political thought', type: 'Idea', year: 'c. 1300 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Paris', role: 'Aquinas taught at the University of Paris' },
      { name: 'Naples', role: 'Aquinas\'s birthplace region and study' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  4. CAROLINGIAN & FRANKISH CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'carolingian_frankish_corpus',
    name: 'The Carolingian & Frankish Corpus',
    label: 'Text',
    callNumber: '730.28-carolingian-frankish-corpus',
    subjectHeadings: ['Artifacts & Texts — Administrative & Literary Texts — Frankish Empire'],
    subjects: ['Charlemagne', 'Carolingian Renaissance', 'Capitularies', 'Royal Annals', 'Einhard', 'Alcuin', 'Aachen'],
    summary: 'The Carolingian & Frankish Corpus encompasses the administrative, historical, and literary texts of the Frankish kingdoms and the Carolingian Empire (c. 500–987 CE), centered on the monumental reign of Charlemagne (r. 768–814 CE) and the Carolingian Renaissance he initiated. Key texts include: the Capitularies — royal legislation covering governance, justice, church reform, and economic regulation (Admonitio Generalis of 789, Capitulare de Villis on estate management); the Royal Frankish Annals (Annales Regni Francorum, 741–829) — the official chronicle of the Carolingian dynasty; Einhard\'s Vita Karoli Magni (Life of Charlemagne, c. 825–830) — modeled on Suetonius, the first medieval biography of a secular ruler; and the immense corpus of manuscript production from scriptoria organized by Alcuin of York at Tours, which standardized Caroline minuscule script (the basis of modern lowercase letters) and preserved classical Latin texts through systematic copying. The Carolingian Renaissance was a deliberate program of cultural renewal ("correctio") that saved much of the Latin literary heritage from oblivion.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 500–987 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Charlemagne commissions cultural renewal program (correctio)', type: 'Person', year: 'c. 780 CE' },
    ],
    effects: [
      { title: 'Caroline minuscule becomes basis of modern lowercase letters', type: 'Idea', year: 'c. 800 CE' },
      { title: 'Carolingian scriptoria preserve majority of surviving classical Latin texts', type: 'Text', year: 'c. 800 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Aachen', role: 'Charlemagne\'s capital and center of the Carolingian Renaissance' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  5. IBERIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'iberian_corpus',
    name: 'The Iberian Corpus',
    label: 'Text',
    callNumber: '730.29-iberian-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — Medieval Iberia'],
    subjects: ['Reconquista', 'Cantigas', 'Alfonso X', 'Fueros', 'Mozarabic', 'Convivencia', 'Castilian', 'Portuguese'],
    summary: 'The Iberian Corpus encompasses the remarkably multicultural literary and legal heritage of medieval Iberia (c. 711–1492 CE) — a peninsula where Christian, Muslim, and Jewish civilizations coexisted, clashed, and cross-fertilized. Key works include: the Cantigas de Santa Maria (c. 1270–1284) — over 400 songs composed (or commissioned) by Alfonso X of Castile ("the Wise") in Galician-Portuguese, with exquisite miniature illustrations, constituting the largest collection of vernacular monophonic song from the Middle Ages; Alfonso X\'s legal and scholarly works (Siete Partidas law code, Primera Crónica General, translations of Arabic scientific texts into Castilian at the Toledo School of Translators); the fueros (municipal charters granting legal autonomy, crucial for understanding medieval self-governance); the Poema de Mio Cid (c. 1207, the earliest surviving Castilian epic); the Mozarabic (Christian Arabic) liturgical tradition; and the Hebrew poetry of al-Andalus (Shlomo ibn Gabirol, Yehuda Halevi). This corpus uniquely documents the "convivencia" — the dynamic coexistence of three Abrahamic civilizations — and includes the transmission of Greek philosophy from Arabic to Latin through the Toledo School that catalyzed the European Scholastic revolution.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 711–1492 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Muslim conquest of Iberia creates multicultural society', type: 'Event', year: '711 CE' },
    ],
    effects: [
      { title: 'Toledo School translates Greek philosophy from Arabic to Latin', type: 'Text', year: 'c. 1150 CE' },
      { title: 'Cantigas de Santa Maria — largest medieval monophonic song collection', type: 'Text', year: 'c. 1280 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Toledo', role: 'Center of the great Arabic-Latin translation movement' },
      { name: 'Córdoba', role: 'Capital of al-Andalus — center of Andalusian culture' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  6. ITALIAN COMMUNAL CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'italian_communal_corpus',
    name: 'The Italian Communal Corpus',
    label: 'Text',
    callNumber: '730.30-italian-communal-corpus',
    subjectHeadings: ['Artifacts & Texts — Urban Texts — Italian City-State Literature'],
    subjects: ['Dante', 'Divine Comedy', 'City-States', 'Merchant Manuals', 'Florence', 'Venice', 'Petrarch', 'Boccaccio', 'Humanism'],
    summary: 'The Italian Communal Corpus encompasses the literary, commercial, legal, and historical texts produced by the Italian city-states (comuni) from c. 1100–1500 CE — the period when Italy was the vanguard of European civilization. Its supreme achievement is Dante Alighieri\'s Divina Commedia (c. 1308–1321) — the greatest poem in the Italian language and one of the supreme literary works in all of world literature, depicting a journey through Hell, Purgatory, and Paradise that synthesizes Christian theology, classical philosophy, and contemporary politics. The corpus also includes: Petrarch\'s Canzoniere (establishing the sonnet tradition and the concept of literary humanism); Boccaccio\'s Decameron (1353, 100 stories — the foundation of Italian prose fiction); merchant manuals (Francesco Pegolotti\'s Pratica della Mercatura, c. 1340 — an encyclopedia of international trade); city statutes and communal legal codes; humanist scholarship (Bruni, Valla, Ficino); and the political theory of Machiavelli (The Prince, 1513) and Guicciardini. This corpus documents the transition from the medieval to the early modern world.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1100–1500 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Italian city-states achieve economic and cultural preeminence', type: 'Institution', year: 'c. 1100 CE' },
    ],
    effects: [
      { title: 'Divine Comedy establishes Italian as a literary language', type: 'Text', year: '1321 CE', slug: 'divine_comedy' },
      { title: 'Humanist scholarship inaugurates the Renaissance', type: 'Movement', year: 'c. 1400 CE' },
    ],
    relationships: [
      { sourceSlug: 'italian_communal_corpus', sourceName: 'The Italian Communal Corpus', verb: 'CONTAINS', targetSlug: 'divine_comedy', targetName: 'The Divine Comedy', context: 'Supreme masterwork of Italian literature' },
    ],
    places: [
      { name: 'Florence', role: 'Center of Tuscan literary culture and humanism' },
    ],
    texts: [],
  },
  {
    slug: 'divine_comedy',
    name: 'The Divine Comedy (Divina Commedia)',
    label: 'Text',
    callNumber: '730.113-divine-comedy',
    subjectHeadings: ['Artifacts & Texts — Literary Texts — Italian Poetry'],
    subjects: ['Dante', 'Hell', 'Purgatory', 'Paradise', 'Beatrice', 'Virgil', 'Terza Rima', 'Florence'],
    summary: 'The supreme masterwork of Italian literature and one of the greatest poems in any language, composed by Dante Alighieri (1265–1321) during his exile from Florence (c. 1308–1321). In 14,233 lines of terza rima (interlocking tercets), the poem narrates Dante\'s journey through the three realms of the Christian afterlife: Inferno (Hell — 9 concentric circles of increasingly severe punishment), Purgatorio (Purgatory — 7 terraces of purification), and Paradiso (Paradise — 9 celestial spheres culminating in the vision of God). Guided first by Virgil (reason) and then by Beatrice (divine grace), Dante encounters hundreds of historical and mythological figures, creating a panoramic encyclopedia of medieval knowledge, theology, philosophy, politics, and human psychology. T.S. Eliot called it "the highest point that poetry has ever reached or ever can reach." The poem established the Tuscan dialect as the literary Italian language.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1308–1321 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Establishes Italian as a literary language', type: 'Idea', year: '1321 CE' },
      { title: 'Supreme literary achievement — influences 700 years of world literature', type: 'Text', year: '1321 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Florence', role: 'Dante\'s birthplace and political context' },
      { name: 'Ravenna', role: 'City of exile where Dante died and is buried' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  7. FRENCH MEDIEVAL CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'french_medieval_corpus',
    name: 'The French Medieval Corpus',
    label: 'Text',
    callNumber: '730.31-french-medieval-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — French Medieval Literature'],
    subjects: ['Chanson de Roland', 'Chrétien de Troyes', 'Arthurian Romance', 'Capetian', 'Trouvères', 'Troubadours', 'Beaumanoir'],
    summary: 'The French Medieval Corpus encompasses the literary, legal, and historical output of medieval France — one of the richest vernacular literary traditions in medieval Europe. Its twin pillars are the chanson de geste (epic) and the romance: the Chanson de Roland (c. 1100) — the oldest and greatest French epic, memorializing Charlemagne\'s rearguard at Roncevaux; and the Arthurian romances of Chrétien de Troyes (c. 1170–1190) — Lancelot, Perceval, Yvain, Erec — which invented the literary genre of chivalric romance and introduced the Quest for the Holy Grail. The corpus also includes: troubadour and trouvère lyric poetry (inventing courtly love — fin\'amor); the Roman de la Rose (c. 1230–1275, the most influential French poem of the Middle Ages); Jean de Joinville\'s Life of Saint Louis (1309, vivid eyewitness chronicle of the Seventh Crusade); Philippe de Beaumanoir\'s Coutumes de Beauvaisis (1283, the most systematic medieval French legal treatise); and the chronicles of Jean Froissart (covering the Hundred Years\' War). French was the lingua franca of European aristocracy and diplomacy, and this corpus\'s influence extended across all of medieval Christendom.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1000–1500 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Capetian France becomes the cultural center of Latin Christendom', type: 'Institution', year: 'c. 1100 CE' },
    ],
    effects: [
      { title: 'Arthurian romance genre spreads across all European literatures', type: 'Text', year: 'c. 1200 CE' },
      { title: 'Courtly love (fin\'amor) transforms European conceptions of love and gender', type: 'Idea', year: 'c. 1170 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Paris', role: 'Center of French royal and intellectual culture' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  8. GERMANIC MEDIEVAL CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'germanic_medieval_corpus',
    name: 'The Germanic Medieval Corpus',
    label: 'Text',
    callNumber: '730.32-germanic-medieval-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — German Medieval Literature'],
    subjects: ['Nibelungenlied', 'Sachsenspiegel', 'Minnesang', 'Wolfram von Eschenbach', 'Parzival', 'Imperial Records', 'HRE'],
    summary: 'The Germanic Medieval Corpus encompasses the literary, legal, and historical texts of the German-speaking lands of the Holy Roman Empire (c. 800–1500 CE). Its literary peaks include: the Nibelungenlied (c. 1200) — the great Middle High German epic of Siegfried, Kriemhild, and the fall of the Burgundians (the poem Wagner transformed into his Ring Cycle); Wolfram von Eschenbach\'s Parzival (c. 1200–1210) — the most profound Arthurian-Grail romance, exploring the spiritual journey from ignorance to divine wisdom; the Minnesang lyric tradition (Walther von der Vogelweide — the greatest medieval German poet); and the prose mysticism of Meister Eckhart (13th–14th century — a precursor to German philosophical idealism). The legal corpus is anchored by the Sachsenspiegel (Mirror of the Saxons, c. 1220–1235) by Eike von Repgow — the most influential medieval German law book, which served as the template for legal codification across Central and Eastern Europe. Imperial records (diplomas, Golden Bull of 1356) document the governance of the Holy Roman Empire.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 800–1500 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Nibelungenlied becomes foundational German national epic', type: 'Text', year: 'c. 1200 CE' },
      { title: 'Sachsenspiegel shapes Central/Eastern European legal tradition', type: 'Text', year: 'c. 1230 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Vienna', role: 'Major center of medieval German literary patronage' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  9. CELTIC MEDIEVAL CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'celtic_medieval_corpus',
    name: 'The Celtic Medieval Corpus',
    label: 'Text',
    callNumber: '730.33-celtic-medieval-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Legal Texts — Celtic/Insular Literature'],
    subjects: ['Irish Annals', 'Welsh Law', 'Bardic Poetry', 'Mabinogion', 'Book of Kells', 'Tain Bo Cuailnge', 'Brehon Law'],
    summary: 'The Celtic Medieval Corpus encompasses the rich literary, legal, historiographic, and artistic heritage of the Celtic-speaking peoples — primarily Ireland and Wales, with extensions to Scotland, Brittany, Cornwall, and the Isle of Man. Ireland possesses the oldest vernacular literature in Western Europe north of the Alps, beginning with Ogham inscriptions (c. 4th century CE) and flowering into an extraordinarily rich manuscript tradition. Key works include: the Táin Bó Cúailnge (Cattle Raid of Cooley — the Irish national epic, featuring the hero Cú Chulainn); the Irish Annals (Annals of Ulster, Annals of the Four Masters — among the most detailed pre-modern chronicles of any European nation); the Brehon Laws (Fenechas — native Irish law, one of the most complex pre-modern legal systems, regulating everything from hospitality obligations to beekeeping rights); the Welsh Mabinogion (11 prose tales including Arthurian material predating Chrétien de Troyes); and the bardic poetry tradition maintained by Irish filid and Welsh bards through hereditary schools. The corpus is also celebrated for its illuminated manuscripts — the Book of Kells (c. 800 CE) is widely considered the most beautiful medieval manuscript in existence.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 400–1600 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Irish monastic tradition preserves learning through the "Dark Ages"', type: 'Institution', year: 'c. 500 CE' },
    ],
    effects: [
      { title: 'Book of Kells — most beautiful medieval manuscript', type: 'Evidence', year: 'c. 800 CE' },
      { title: 'Oldest vernacular literature in Western Europe north of the Alps', type: 'Text', year: 'c. 600 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Dublin', role: 'Home of Trinity College Library — keeper of the Book of Kells' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  10. VIKING & NORDIC CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'viking_nordic_corpus',
    name: 'The Viking & Nordic Corpus',
    label: 'Text',
    callNumber: '730.34-viking-nordic-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Historical Texts — Norse/Scandinavian Literature'],
    subjects: ['Sagas', 'Eddas', 'Runic Inscriptions', 'Snorri Sturluson', 'Icelandic', 'Norse Mythology', 'Vikings', 'Odin', 'Ragnarok'],
    summary: 'The Viking & Nordic Corpus encompasses the literary, mythological, historical, and legal texts of Scandinavian civilization, centered on the extraordinary Icelandic manuscript tradition. Its pillars are: the Poetic Edda (Codex Regius, c. 1270, collecting much older poems) — the primary source for Norse mythology (Odin, Thor, Ragnarok, the Norns, Valhalla); Snorri Sturluson\'s Prose Edda (c. 1220) — a masterful literary retelling and analysis of Norse mythology and poetics; the Icelandic family sagas (Njál\'s Saga, Egil\'s Saga, Laxdæla Saga — c. 1200–1350) — prose narratives of Icelandic settlement-age families, remarkable for their psychological realism, understated irony, and tragic grandeur; the Vinland Sagas (recording Norse exploration of North America c. 1000 CE — confirmed by archaeology at L\'Anse aux Meadows); runic inscriptions (approximately 6,000 known inscriptions across Scandinavia, including the Rök Stone — the longest runic inscription, c. 800 CE); and the Grágás (Icelandic Commonwealth law code). Iceland\'s unique distinction: a small, isolated island produced arguably the richest medieval vernacular prose literature in Europe.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Northern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 800–1400 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Icelandic Commonwealth (930–1262) creates unique literary culture', type: 'Institution', year: '930 CE' },
    ],
    effects: [
      { title: 'Norse mythology profoundly influences Western fantasy literature (Tolkien)', type: 'Idea', year: 'c. 1900 CE' },
      { title: 'Vinland Sagas document North American contact 500 years before Columbus', type: 'Evidence', year: 'c. 1000 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Reykjavik', role: 'Center of Icelandic manuscript tradition' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  11. OTTOMAN BALKAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'ottoman_balkan_corpus',
    name: 'The Ottoman Balkan Corpus',
    label: 'Text',
    callNumber: '730.35-ottoman-balkan-corpus',
    subjectHeadings: ['Artifacts & Texts — Administrative Records — Ottoman Balkan Provinces'],
    subjects: ['Defters', 'Balkans', 'Ottoman Empire', 'Imperial Decrees', 'Multi-ethnic', 'Millet System'],
    summary: 'The Ottoman Balkan Corpus comprises the administrative, legal, and literary records of the Ottoman Empire\'s Balkan provinces (Rumelia) from the 14th to the early 20th century CE. While overlapping with the Ottoman Archive Corpus in its imperial administrative component, this corpus specifically documents the governance of the multi-ethnic, multi-religious Balkan populations — Greeks, Serbs, Bulgarians, Albanians, Wallachians, Bosnians, and others — under Ottoman rule. Key document types include: tahrir defters (tax surveys meticulously recording every village, household, and farm in the Balkans); imperial decrees (firmans); şer\'iyye sicilleri (Islamic court records documenting daily disputes, transactions, and social relations across religious communities); vakıf (endowment) documents showing Ottoman charitable infrastructure; chronicles by Balkan Christian and Muslim authors; and the records of the millet system (the Ottoman framework for governing non-Muslim communities through their religious leaders). This corpus is essential for understanding five centuries of Balkan history and the deep Ottoman imprint on Southeastern European society.',
    era: 'Early Modern',
    eraSlug: 'early-modern',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 1350–1912 CE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Ottoman conquest of the Balkans (14th–15th centuries)', type: 'Event', year: 'c. 1350 CE' },
    ],
    effects: [
      { title: 'Provides detailed documentation of Balkan social history under Ottoman rule', type: 'Evidence', year: 'c. 1500 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Istanbul', role: 'Ottoman imperial capital and archive center' },
      { name: 'Sarajevo', role: 'Major Ottoman Balkan administrative center' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  12. JUDEO-SEPHARDIC CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'judeo_sephardic_corpus',
    name: 'The Judeo-Sephardic Corpus',
    label: 'Text',
    callNumber: '730.36-judeo-sephardic-corpus',
    subjectHeadings: ['Artifacts & Texts — Religious & Cultural Texts — Sephardic Jewish Tradition'],
    subjects: ['Ladino', 'Responsa', 'Maimonides', 'al-Andalus', 'Sephardic', 'Kabbalah', 'Zohar', 'Expulsion 1492'],
    summary: 'The Judeo-Sephardic Corpus encompasses the literary, philosophical, legal, mystical, and communal records of the Sephardic Jewish tradition — the Jewish civilization of the Iberian Peninsula and its global diaspora after the expulsion from Spain (1492) and Portugal (1497). This tradition produced some of the greatest Jewish intellectuals in history: Maimonides (Moses ben Maimon, 1138–1204) — whose Guide for the Perplexed and Mishneh Torah represent the pinnacle of medieval Jewish philosophy and legal codification; Solomon ibn Gabirol (c. 1021–1058) — philosopher and poet; Yehuda Halevi (c. 1075–1141) — poet and the author of the Kuzari; and the Zohar (attributed to Moses de León, c. 1280s) — the masterwork of Jewish mystical literature (Kabbalah). The corpus also includes: Sephardic responsa (rabbinic legal opinions documenting communal life); Ladino (Judeo-Spanish) literature post-1492; the Cairo Geniza documents (250,000+ manuscript fragments from medieval Jewish life, discovered in the Ben Ezra Synagogue in Cairo — one of the most important documentary finds in history); and communal records (ketubbot, tax rolls, communal ordinances) from Sephardic communities in Thessaloniki, Amsterdam, Istanbul, and the Americas.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Western Europe',
    continent: 'Europe',
    status: 'Published',
    period: 'c. 711–1700 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Jewish settlement in al-Andalus under Islamic rule', type: 'Event', year: 'c. 711 CE' },
    ],
    effects: [
      { title: 'Maimonides\' Guide for the Perplexed — greatest work of Jewish philosophy', type: 'Text', year: 'c. 1190 CE' },
      { title: 'Zohar becomes foundational text of Kabbalah', type: 'Text', year: 'c. 1280 CE' },
      { title: 'Cairo Geniza — 250K+ fragments document medieval Jewish life', type: 'Evidence', year: '1896 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Córdoba', role: 'Birthplace of Maimonides — center of Andalusian Jewish thought' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  13. ARMENIAN CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'armenian_corpus',
    name: 'The Armenian Corpus',
    label: 'Text',
    callNumber: '730.37-armenian-corpus',
    subjectHeadings: ['Artifacts & Texts — Literary & Historical Texts — Armenian Christian Tradition'],
    subjects: ['Mesrop Mashtots', 'Armenian Alphabet', 'Armenian Church', 'Chronicles', 'Cilicia', 'Genocide', 'Hagiography'],
    summary: 'The Armenian Corpus encompasses the literary, historical, theological, and legal heritage of the Armenian people — one of the oldest continuously Christian nations (Armenia adopted Christianity as a state religion in 301 CE, before the Roman Empire). The corpus is inseparable from the Armenian alphabet, created by the monk and scholar Mesrop Mashtots in 405 CE specifically to translate the Bible and transmit Armenian Christian culture — the Armenians call their script "holy letters" (surb grer). The first major work in Armenian was a translation of the Bible so elegant it is called the "Queen of Translations." Key works include: the History of the Armenians by Movses Khorenatsi (5th century, the foundational Armenian national history); the chronicles of the Kingdom of Armenian Cilicia (1078–1375); extensive hagiographies; the theological writings of the Armenian Church Fathers; and the Datastanagirk\' (law code of Mkhitar Gosh, 1184). The Armenian manuscript tradition — with its distinctive illumination style — is preserved across the global Armenian diaspora, with the largest collection at the Matenadaran Institute in Yerevan (over 17,000 manuscripts). The corpus bears witness to a civilization that survived conquest by Romans, Persians, Arabs, Seljuks, Mongols, Ottomans, and the Genocide of 1915.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'Eastern Europe',
    continent: 'Europe',
    status: 'Published',
    period: '301 CE – present',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Armenia adopts Christianity as state religion (301 CE — first nation to do so)', type: 'Event', year: '301 CE' },
      { title: 'Mesrop Mashtots creates the Armenian alphabet', type: 'Person', year: '405 CE' },
    ],
    effects: [
      { title: 'Armenian Bible translation ("Queen of Translations") preserves textual variants', type: 'Text', year: 'c. 410 CE' },
      { title: 'Matenadaran preserves 17,000+ manuscripts of Armenian literary heritage', type: 'Evidence', year: 'present' },
    ],
    relationships: [],
    places: [
      { name: 'Yerevan', role: 'Home of the Matenadaran — largest Armenian manuscript collection' },
      { name: 'Etchmiadzin', role: 'Seat of the Armenian Apostolic Church (since 301 CE)' },
    ],
    texts: [],
  },
]
