/**
 * Africa Corpuses (beyond Egypt)
 *
 * 1. ETHIOSEMITIC_GEEZ_CORPUS — Ge'ez scriptures, Book of Enoch, Kebra Nagast
 * 2. TIMBUKTU_MANUSCRIPT_CORPUS — West African Islamic scholarly manuscripts
 * 3. AFRICAN_ORAL_EPIC_CYCLE — Sundiata, Mwindo, Ozidi, oral traditions
 */
import type { Entity } from '../../entityTypes'

export const AFRICA_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  1. ETHIOSEMITIC GE'EZ CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'ethiosemitic_geez_corpus',
    name: 'The Ethio-Semitic Ge\'ez Corpus',
    label: 'Text',
    callNumber: '730.20-ethiosemitic-geez-corpus',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Ethiopian Christian Canon'],
    subjects: ['Ge\'ez', 'Ethiopia', 'Book of Enoch', 'Kebra Nagast', 'Ethiopian Orthodox', 'Aksumite', 'Semitic', 'Africa'],
    summary: 'The Ethio-Semitic Ge\'ez Corpus encompasses the rich literary heritage of Ethiopian civilization preserved in the Ge\'ez language (the classical liturgical language of Ethiopia, a South Semitic language related to Arabic and Hebrew). Ethiopia possesses the most extensive indigenous literary tradition in sub-Saharan Africa, and its Christian civilization — the oldest in Africa, dating to the 4th century CE — produced a remarkable body of scripture, hagiography, historiography, and theological literature. The Ethiopian biblical canon is the largest of any Christian tradition (81 books vs. 66 Protestant / 73 Catholic), uniquely preserving complete texts of 1 Enoch (Book of Enoch) and the Book of Jubilees — Jewish Second Temple texts lost in all other traditions and rediscovered in Ge\'ez manuscripts. The Kebra Nagast (Glory of Kings, 14th century CE) — the national epic narrating the Queen of Sheba\'s visit to Solomon, the birth of their son Menelik I, and the transfer of the Ark of the Covenant to Ethiopia — legitimized the Solomonic dynasty that ruled Ethiopia until 1974. Other treasures include the Fetha Nagast (Law of Kings, a legal code), extensive hagiographies of Ethiopian saints, and Amharic royal chronicles.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'East Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 350 CE – 1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Aksumite Kingdom adopts Christianity (4th century CE)', type: 'Event', year: 'c. 340 CE' },
      { title: 'Ge\'ez script develops from South Arabian precursors', type: 'Idea', year: 'c. 500 BCE' },
    ],
    effects: [
      { title: 'Preserves 1 Enoch and Jubilees — lost in all other traditions', type: 'Text', year: 'c. 500 CE', slug: 'book_of_enoch_geez' },
      { title: 'Kebra Nagast legitimizes Solomonic dynasty for 700 years', type: 'Text', year: 'c. 1300 CE', slug: 'kebra_nagast' },
      { title: 'Largest Christian biblical canon (81 books)', type: 'Text', year: 'c. 400 CE' },
    ],
    relationships: [
      { sourceSlug: 'ethiosemitic_geez_corpus', sourceName: 'The Ethio-Semitic Ge\'ez Corpus', verb: 'CONTAINS', targetSlug: 'book_of_enoch_geez', targetName: 'Book of Enoch (1 Enoch)', context: 'Only complete version survived in Ge\'ez' },
      { sourceSlug: 'ethiosemitic_geez_corpus', sourceName: 'The Ethio-Semitic Ge\'ez Corpus', verb: 'CONTAINS', targetSlug: 'kebra_nagast', targetName: 'Kebra Nagast', context: 'Ethiopian national epic' },
    ],
    places: [
      { name: 'Aksum', role: 'Ancient capital — center of early Ge\'ez literature' },
      { name: 'Lalibela', role: 'Rock-hewn churches — living manuscript tradition' },
    ],
    texts: [],
  },
  {
    slug: 'book_of_enoch_geez',
    name: 'Book of Enoch (1 Enoch)',
    label: 'Text',
    callNumber: '730.104-book-of-enoch',
    subjectHeadings: ['Artifacts & Texts — Religious Texts — Jewish/Ethiopian Apocalyptic Literature'],
    subjects: ['Enoch', 'Apocalyptic', 'Watchers', 'Nephilim', 'Son of Man', 'Second Temple', 'Ethiopic', 'Pseudepigrapha'],
    summary: 'A composite Jewish apocalyptic text attributed to the antediluvian patriarch Enoch (Gen. 5:18–24), composed in stages between the 3rd century BCE and 1st century CE. The complete text survives only in Ge\'ez (Ethiopic) translation — part of the Ethiopian biblical canon — though fragments were found among the Dead Sea Scrolls in Aramaic. The book comprises five sections: the Book of the Watchers (fallen angels who mate with human women, producing the giant Nephilim — expanding Gen. 6:1–4); the Parables of Enoch (introducing the "Son of Man" figure, a pre-existent heavenly judge); the Astronomical Book (a 364-day solar calendar); the Book of Dreams (apocalyptic visions); and the Epistle of Enoch (ethical exhortation and apocalyptic judgment). 1 Enoch profoundly influenced early Christianity — its "Son of Man" concept is central to the Gospels, and it is directly quoted in the Epistle of Jude (Jude 14–15). Its survival exclusively in Ethiopia makes the Ge\'ez literary tradition uniquely important for Jewish and Christian textual studies.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'East Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 300 BCE – 100 CE (composition); c. 500 CE (Ge\'ez translation)',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: '"Son of Man" concept influences Gospel christology', type: 'Idea', year: 'c. 30 CE' },
      { title: 'Quoted in canonical Epistle of Jude (Jude 14–15)', type: 'Text', year: 'c. 65 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Aksum', role: 'Center of Ge\'ez manuscript preservation' },
    ],
    texts: [],
  },
  {
    slug: 'kebra_nagast',
    name: 'Kebra Nagast (Glory of Kings)',
    label: 'Text',
    callNumber: '730.105-kebra-nagast',
    subjectHeadings: ['Artifacts & Texts — Historical-Religious Texts — Ethiopian National Epic'],
    subjects: ['Queen of Sheba', 'Solomon', 'Menelik I', 'Ark of the Covenant', 'Solomonic Dynasty', 'Ethiopian Identity'],
    summary: 'The Ethiopian national epic, composed or compiled in its present form c. 1300–1320 CE (though drawing on much older traditions), narrating the encounter between the Queen of Sheba (Makeda) and King Solomon of Israel, the birth of their son Menelik I, and Menelik\'s journey to Jerusalem and return to Ethiopia — secretly bringing with him the Ark of the Covenant, which, according to Ethiopian tradition, rests to this day in the Church of Our Lady Mary of Zion in Aksum. The Kebra Nagast served as the constitutional foundation of the Solomonic dynasty that ruled Ethiopia from 1270 to 1974 (when Emperor Haile Selassie was deposed). It also became a sacred text of the Rastafari movement in the 20th century, which venerates Haile Selassie as the returned Messiah and Ethiopia as the promised land. UNESCO inscribed it in its Memory of the World Register.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'East Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1300–1320 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Legitimizes Solomonic dynasty ruling Ethiopia for 700 years', type: 'Institution', year: 'c. 1270 CE' },
      { title: 'Sacred text of Rastafari movement in 20th century', type: 'Movement', year: 'c. 1930 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Aksum', role: 'Claimed resting place of the Ark of the Covenant' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  2. TIMBUKTU MANUSCRIPT CORPUS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'timbuktu_manuscript_corpus',
    name: 'The Timbuktu Manuscript Corpus',
    label: 'Text',
    callNumber: '730.21-timbuktu-manuscript-corpus',
    subjectHeadings: ['Artifacts & Texts — Scholarly Manuscripts — West African Islamic Tradition'],
    subjects: ['Timbuktu', 'Mali', 'Songhai', 'Islamic Scholarship', 'African Manuscripts', 'Sankore', 'Arabic', 'Trans-Saharan'],
    summary: 'The Timbuktu Manuscript Corpus comprises an estimated 300,000–700,000 manuscripts preserved in private family libraries and public repositories in and around Timbuktu, Mali — the largest body of written records from sub-Saharan Africa and one of the most significant collections of Islamic manuscripts in the world. Dating from the 13th to the 18th century CE, these manuscripts were produced by scholars associated with the great Islamic learning centers of Timbuktu — particularly the Sankore Mosque and University, which at its height (15th–16th centuries) attracted scholars from across the Muslim world. The manuscripts cover an extraordinary range of subjects: Qur\'anic exegesis, Islamic jurisprudence, Sufi mysticism, astronomy, mathematics, medicine, pharmacology, chemistry, botany, governance, history, poetry, and inter-ethnic diplomacy. They are written primarily in Arabic, with significant bodies in Ajami (African languages written in Arabic script). The corpus decisively refutes the colonial myth that sub-Saharan Africa had no written intellectual tradition. Heroic preservation efforts — including Dr. Abdel Kader Haidara\'s smuggling of 350,000+ manuscripts out of Timbuktu during the 2012–2013 jihadist occupation — have saved this irreplaceable heritage.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1200–1800 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Trans-Saharan trade brings Islamic scholarship to West Africa', type: 'Movement', year: 'c. 1000 CE' },
      { title: 'Mali and Songhai empires patronize Timbuktu as a center of learning', type: 'Institution', year: 'c. 1300 CE' },
    ],
    effects: [
      { title: 'Largest corpus of written records from sub-Saharan Africa (300K–700K MSS)', type: 'Text', year: 'c. 1500 CE' },
      { title: 'Refutes colonial narrative of a "preliterate" sub-Saharan Africa', type: 'Idea', year: 'c. 2000 CE' },
    ],
    relationships: [
      { sourceSlug: 'timbuktu_manuscript_corpus', sourceName: 'The Timbuktu Manuscript Corpus', verb: 'TRANSMITS', targetSlug: 'islamic_quran_hadith_corpus', targetName: 'The Islamic Qur\'an & Hadith Corpus', context: 'West African transmission of Islamic learning' },
    ],
    places: [
      { name: 'Timbuktu', role: 'Center of West African Islamic scholarship', slug: 'timbuktu_city' },
    ],
    texts: [],
  },
  {
    slug: 'timbuktu_city',
    name: 'Timbuktu',
    label: 'Place',
    callNumber: '440.35-timbuktu',
    subjectHeadings: ['Places — Centers of Learning — West African Cities'],
    subjects: ['Mali', 'Songhai', 'Sankore', 'Islamic Scholarship', 'Trans-Saharan Trade', 'Manuscripts', 'Gold'],
    summary: 'A city in present-day Mali, located at the southern edge of the Sahara near the Niger River, that became one of the most important centers of learning in the Islamic world and the intellectual capital of West Africa during the 15th–16th centuries CE. Founded c. 1100 CE as a seasonal camp for Tuareg nomads, Timbuktu rose to prominence under the Mali Empire (13th–15th centuries) and the Songhai Empire (15th–16th centuries). The Sankore Mosque and University, along with the Djinguereber and Sidi Yahia mosques (all UNESCO World Heritage Sites), attracted 25,000 students and scholars from across the Muslim world. The private libraries of Timbuktu\'s scholarly families preserved hundreds of thousands of manuscripts on subjects ranging from theology to astronomy to medicine. Leo Africanus (1526) described Timbuktu as a city where "more profit is made from the sale of books than from any other merchandise."',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1100 CE – present',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [],
    relationships: [],
    places: [],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  3. AFRICAN ORAL EPIC CYCLE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'african_oral_epic_cycle',
    name: 'The African Oral Epic Cycle',
    label: 'Text',
    callNumber: '730.22-african-oral-epic-cycle',
    subjectHeadings: ['Artifacts & Texts — Oral Literature — African Epic Traditions'],
    subjects: ['Sundiata', 'Mwindo', 'Ozidi', 'Griot', 'Jeli', 'Oral Tradition', 'African Literature', 'Epic Poetry'],
    summary: 'The African Oral Epic Cycle encompasses the great oral literary traditions of sub-Saharan Africa — performance-based narrative traditions transmitted by specialized hereditary bards (griots/jeliw in West Africa, imbongi in southern Africa, azmari in Ethiopia) over centuries. These are not "primitive" folk tales but sophisticated, multi-hour epic performances combining narrative, song, music, genealogy, praise poetry, and moral philosophy. Key traditions include: the Epic of Sundiata (Sunjata Fasa) — the foundational narrative of the Mali Empire and the Mande people, narrating the rise of Sundiata Keita from a crippled prince to the Lion King who defeated the sorcerer-king Sumanguru at the Battle of Kirina (c. 1235 CE) and established one of the largest empires in African history; the Mwindo Epic — a Nyanga (Congo) hero tale of supernatural adventures through underworld and sky; the Ozidi Saga — a Ijaw (Nigeria) epic of vengeance and spiritual warfare; the Lianja Epic (Congo); Kambili and Da Monzon (Mali/Bamana); and the Zulu izibongo (praise poetry) tradition. These traditions represent an alternative model of literary preservation — not through writing but through embodied, performed memory — and contain profound philosophical, historical, and ethical content.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1200 CE – present (oldest documented traditions)',
    frameworks: ['TEXTUAL_TRANSMISSION', 'ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Griot/jeli hereditary bard tradition preserves history through performance', type: 'Institution', year: 'c. 1000 CE' },
    ],
    effects: [
      { title: 'Sundiata epic becomes foundation narrative of Mande civilization', type: 'Text', year: 'c. 1240 CE', slug: 'epic_of_sundiata' },
      { title: 'Demonstrates alternative literary model — embodied performed memory', type: 'Idea', year: 'c. 1960 CE' },
    ],
    relationships: [
      { sourceSlug: 'african_oral_epic_cycle', sourceName: 'The African Oral Epic Cycle', verb: 'CONTAINS', targetSlug: 'epic_of_sundiata', targetName: 'Epic of Sundiata', context: 'Foundation narrative of the Mali Empire' },
    ],
    places: [
      { name: 'Niani', role: 'Capital of the Mali Empire — Sundiata\'s seat' },
    ],
    texts: [],
  },
  {
    slug: 'epic_of_sundiata',
    name: 'Epic of Sundiata (Sunjata Fasa)',
    label: 'Text',
    callNumber: '730.106-epic-of-sundiata',
    subjectHeadings: ['Artifacts & Texts — Oral Literature — West African Epic'],
    subjects: ['Sundiata Keita', 'Mali Empire', 'Mande', 'Griot', 'Kirina', 'Lion King', 'Oral Epic'],
    summary: 'The foundational oral epic of the Mande people of West Africa, narrating the miraculous life of Sundiata Keita (c. 1217–c. 1255 CE) — from his birth prophecy through his childhood disability (he could not walk until age seven), his exile, his gathering of allies, and his triumphant return to defeat the sorcerer-tyrant Sumanguru Kante at the Battle of Kirina (c. 1235 CE), founding the Mali Empire — one of the largest and wealthiest empires in African and world history. Performed by jeliw (griots) across Mali, Guinea, Gambia, Senegal, and Burkina Faso, the epic exists in multiple versions (each jeli\'s performance is unique) and was first transcribed in the 20th century (notably by Djibril Tamsir Niane in 1960). The Sundiata epic is often compared to the Iliad or the Arthurian legends — a foundational heroic narrative that defines civilizational identity and encodes values of leadership, justice, and destiny.',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    period: 'c. 1235 CE (events); c. 1200 CE+ (oral transmission); 1960 CE (first transcription)',
    frameworks: ['ORAL_TRADITION', 'CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Defines Mande civilizational identity across West Africa', type: 'Idea', year: 'c. 1300 CE' },
      { title: 'Encodes the Mande Charter (Kouroukan Fouga) — early human rights declaration', type: 'Idea', year: 'c. 1236 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Niani', role: 'Capital of the Mali Empire founded by Sundiata' },
    ],
    texts: [],
  },
  {
    slug: 'sundiata_keita',
    name: 'Sundiata Keita',
    label: 'Person',
    callNumber: '250.55-sundiata-keita',
    subjectHeadings: ['People — Rulers — West African Kings'],
    subjects: ['Mali Empire', 'Mande', 'Lion King', 'Battle of Kirina', 'Griot Tradition', 'Empire Builder'],
    summary: 'Founder of the Mali Empire (c. 1217–c. 1255 CE), one of the largest and wealthiest empires in African history, stretching from the Atlantic coast to the Niger River bend and controlling the trans-Saharan gold and salt trade. According to the griot-preserved oral epic, Sundiata was born a cripple to a prophesied destiny — he miraculously gained the power to walk at age seven, was exiled by a jealous rival, and returned with an army of allies to defeat the sorcerer-king Sumanguru Kante at the Battle of Kirina (c. 1235 CE). He is credited with establishing the Kouroukan Fouga (Charter of Manden) — an oral constitution that codified human rights, religious tolerance, and the abolition of slavery, which some scholars regard as an early declaration of human rights. His title "Mari Djata" (Lion Prince) is the origin of the Mande concept of the "Lion King."',
    born: 'c. 1217 CE',
    died: 'c. 1255 CE',
    era: 'Medieval',
    eraSlug: 'medieval',
    region: 'West Africa',
    continent: 'Africa',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Founded the Mali Empire — one of the largest in African history', type: 'Institution', year: 'c. 1235 CE' },
      { title: 'His epic becomes the Iliad of West Africa', type: 'Text', year: 'c. 1300 CE', slug: 'epic_of_sundiata' },
    ],
    relationships: [
      { sourceSlug: 'sundiata_keita', sourceName: 'Sundiata Keita', verb: 'DEFINES', targetSlug: 'epic_of_sundiata', targetName: 'Epic of Sundiata', context: 'Subject of the foundational West African oral epic' },
    ],
    places: [
      { name: 'Niani', role: 'Capital of the Mali Empire' },
    ],
    texts: [],
  },
]
