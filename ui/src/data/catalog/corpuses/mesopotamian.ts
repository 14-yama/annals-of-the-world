/**
 * Mesopotamian Corpus — Sumerian & Akkadian texts
 *
 * Covers: Enūma Eliš, Epic of Gilgamesh, royal inscriptions, law codes,
 * mathematical tablets, astronomical records, and administrative archives
 * from the cradle of civilization (c. 3400 BCE – 539 BCE).
 *
 * Call Number Assignments:
 *   730.02  — Corpus node
 *   730.20–39 — Mesopotamian Texts
 *   250.10–19 — Mesopotamian Figures
 *   340.10–14 — Mesopotamian Institutions
 *   440.10–14 — Mesopotamian Places
 *   570.10–14 — Mesopotamian Events
 *   140.10–14 — Mesopotamian Ideas
 *   810.10–14 — Mesopotamian Evidence
 */
import type { Entity } from '../../entityTypes'

export const MESOPOTAMIAN_ENTITIES: Entity[] = [
  // ═══════════════════════════════════════════════════════════════════
  //  CORPUS NODE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'mesopotamian_corpus',
    name: 'The Mesopotamian Corpus',
    label: 'Text',
    callNumber: '730.02-mesopotamian-corpus',
    subjectHeadings: ['Artifacts & Texts — Ancient Near Eastern Texts — Mesopotamian Canon'],
    subjects: ['Mesopotamia', 'Sumer', 'Akkad', 'Babylon', 'Assyria', 'Cuneiform', 'Ancient Near East', 'Cradle of Civilization'],
    summary: 'The Mesopotamian Corpus comprises thousands of cuneiform tablets spanning nearly three millennia of Sumerian, Akkadian, Babylonian, and Assyrian civilization (c. 3400–539 BCE). It includes humanity\'s earliest known literature (the Epic of Gilgamesh), the first law codes (Code of Ur-Nammu, Code of Hammurabi), creation narratives (Enūma Eliš), astronomical observations, mathematical treatises, royal inscriptions, administrative records, and temple hymns. Written on clay tablets in cuneiform script, this corpus represents the foundational literary and intellectual tradition of human civilization, predating and influencing Greek, Hebrew, and Persian literary cultures.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 3400 BCE – 539 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Invention of cuneiform writing in Sumer', type: 'Event', year: 'c. 3400 BCE' },
      { title: 'Urbanization and temple administration create demand for record-keeping', type: 'Idea', year: 'c. 3500 BCE' },
    ],
    effects: [
      { title: 'Gilgamesh flood narrative influences Hebrew Bible', type: 'Text', year: 'c. 700 BCE' },
      { title: 'Code of Hammurabi shapes ancient legal traditions', type: 'Idea', year: 'c. 1750 BCE' },
      { title: 'Babylonian astronomy transmits to Greek science', type: 'Idea', year: 'c. 500 BCE' },
    ],
    relationships: [
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'CONTAINS', targetSlug: 'epic_of_gilgamesh', targetName: 'Epic of Gilgamesh', context: 'Oldest great work of literature' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'CONTAINS', targetSlug: 'enuma_elish', targetName: 'Enūma Eliš', context: 'Babylonian creation epic' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'CONTAINS', targetSlug: 'code_of_hammurabi', targetName: 'Code of Hammurabi', context: 'Famous ancient law code' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'CONTAINS', targetSlug: 'code_of_ur_nammu', targetName: 'Code of Ur-Nammu', context: 'Oldest surviving law code' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'CONTAINS', targetSlug: 'descent_of_inanna', targetName: 'Descent of Inanna', context: 'Sumerian underworld myth' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'INFLUENCES', targetSlug: 'biblical_corpus', targetName: 'The Biblical Corpus', context: 'Flood narrative, creation themes, legal parallels' },
      { sourceSlug: 'mesopotamian_corpus', sourceName: 'The Mesopotamian Corpus', verb: 'INFLUENCES', targetSlug: 'graeco_roman_corpus', targetName: 'The Graeco-Roman Corpus', context: 'Astronomical knowledge transmitted via Persia' },
    ],
    places: [
      { name: 'Nineveh', role: 'Ashurbanipal\'s library — largest cuneiform archive', slug: 'nineveh' },
      { name: 'Babylon', role: 'Political and cultural center', slug: 'babylon_city' },
      { name: 'Ur', role: 'Sumerian city-state and literary center', slug: 'ur_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  TEXTS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'epic_of_gilgamesh',
    name: 'Epic of Gilgamesh',
    label: 'Text',
    callNumber: '730.20-epic-of-gilgamesh',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Mesopotamian Epic'],
    subjects: ['Gilgamesh', 'Enkidu', 'Uruk', 'Flood Narrative', 'Immortality', 'Mesopotamian Literature', 'Cuneiform', 'Epic Poetry'],
    summary: 'The oldest great work of literature in human history, composed in Sumerian and later in Akkadian across multiple versions (c. 2100–1200 BCE). The Standard Babylonian version comprises twelve tablets narrating King Gilgamesh of Uruk\'s quest for immortality, his friendship with Enkidu, their battle with Humbaba, the death of Enkidu, and the encounter with Utnapishtim (the flood survivor). Tablet XI contains a flood narrative strikingly parallel to Genesis 6–9. The epic explores themes of mortality, civilization vs. nature, divine power, and the meaning of a life well-lived.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 2100–1200 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Historical King Gilgamesh of Uruk inspires oral traditions', type: 'Person', year: 'c. 2700 BCE' },
      { title: 'Sumerian literary tradition and scribal schools', type: 'Institution', year: 'c. 2100 BCE' },
    ],
    effects: [
      { title: 'Flood motif echoed in Genesis and Greek myth', type: 'Text', year: 'c. 700 BCE' },
      { title: 'Establishes friendship-quest archetype in world literature', type: 'Idea', year: 'c. 1200 BCE' },
    ],
    relationships: [
      { sourceSlug: 'epic_of_gilgamesh', sourceName: 'Epic of Gilgamesh', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Flood narrative parallel (Utnapishtim / Noah)' },
      { sourceSlug: 'nebuchadnezzar_ii', sourceName: 'Nebuchadnezzar II', verb: 'RULES', targetSlug: 'babylon_city', targetName: 'Babylon', context: 'Neo-Babylonian Empire capital under Nebuchadnezzar II' }
    ],
    places: [
      { name: 'Uruk', role: 'Setting of the epic; Gilgamesh\'s city', slug: 'uruk_city' },
      { name: 'Nineveh', role: 'Ashurbanipal\'s library preserved the Standard Babylonian version', slug: 'nineveh' },
    ],
    texts: [],
  },
  {
    slug: 'enuma_elish',
    name: 'Enūma Eliš',
    label: 'Text',
    callNumber: '730.21-enuma-elish',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Mesopotamian Creation Epic'],
    subjects: ['Creation Myth', 'Marduk', 'Tiamat', 'Babylonian Cosmogony', 'Theology', 'Ritual', 'Cuneiform'],
    summary: 'The Babylonian creation epic, composed on seven tablets in Akkadian (c. 1100 BCE), recounts the cosmic battle between the storm god Marduk and the chaos dragon Tiamat. After Marduk defeats Tiamat and fashions the cosmos from her body, he is proclaimed king of the gods and creates humanity from the blood of the rebel god Kingu to serve the gods. Recited annually at the Akitu (New Year) festival in Babylon, Enūma Eliš served as both theological cosmology and political propaganda legitimizing Babylon\'s supremacy over rival city-states.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 1100 BCE',
    frameworks: ['DOCTRINE_DEVELOPMENT', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Babylonian rise to political supremacy under Nebuchadnezzar I', type: 'Event', year: 'c. 1125 BCE' },
      { title: 'Earlier Sumerian creation traditions and theogonies', type: 'Text', year: 'c. 2000 BCE' },
    ],
    effects: [
      { title: 'Cosmogonic themes parallel Genesis 1 creation account', type: 'Text', year: 'c. 500 BCE' },
      { title: 'Shapes Mesopotamian ritual calendar via Akitu festival', type: 'Event', year: 'c. 1000 BCE' },
    ],
    relationships: [
      { sourceSlug: 'enuma_elish', sourceName: 'Enūma Eliš', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Creation narrative parallels — cosmos from watery chaos, structured creation sequence' },
    ],
    places: [
      { name: 'Babylon', role: 'Composed and ritually recited here', slug: 'babylon_city' },
    ],
    texts: [],
  },
  {
    slug: 'code_of_hammurabi',
    name: 'Code of Hammurabi',
    label: 'Text',
    callNumber: '730.22-code-of-hammurabi',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Babylonian Law Code'],
    subjects: ['Law Code', 'Hammurabi', 'Babylon', 'Justice', 'Lex Talionis', 'Ancient Law', 'Cuneiform', 'Stele'],
    summary: 'One of the oldest and most complete written legal codes, inscribed on a 2.25-meter diorite stele during the reign of King Hammurabi of Babylon (r. 1792–1750 BCE). Contains 282 laws organized by topic — property, family, labor, commerce, assault, and professional liability — framed by a prologue invoking divine mandate and an epilogue with curses against those who alter the laws. Famous for its lex talionis ("eye for an eye") provisions, though punishments varied by social class (awīlum, muškēnum, wardum). Discovered at Susa in 1901–1902, now in the Louvre.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 1754 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Hammurabi unifies Mesopotamia and seeks to standardize justice', type: 'Person', year: 'c. 1792 BCE', slug: 'hammurabi' },
      { title: 'Earlier legal traditions: Code of Ur-Nammu, Laws of Eshnunna', type: 'Text', year: 'c. 2100 BCE' },
    ],
    effects: [
      { title: 'Influences biblical covenant code (Exodus 21–23)', type: 'Text', year: 'c. 1200 BCE' },
      { title: 'Sets precedent for written statutory law', type: 'Idea', year: 'c. 1750 BCE' },
    ],
    relationships: [
      { sourceSlug: 'code_of_hammurabi', sourceName: 'Code of Hammurabi', verb: 'INFLUENCES', targetSlug: 'exodus_book', targetName: 'Exodus', context: 'Covenant Code parallels (Exodus 21–23)' },
    ],
    places: [
      { name: 'Babylon', role: 'Capital of Hammurabi\'s empire', slug: 'babylon_city' },
    ],
    texts: [],
  },
  {
    slug: 'code_of_ur_nammu',
    name: 'Code of Ur-Nammu',
    label: 'Text',
    callNumber: '730.23-code-of-ur-nammu',
    subjectHeadings: ['Artifacts & Texts — Legal Texts — Sumerian Law Code'],
    subjects: ['Law Code', 'Ur-Nammu', 'Ur', 'Sumer', 'Third Dynasty of Ur', 'Ancient Law', 'Cuneiform'],
    summary: 'The oldest surviving law code in history, promulgated by King Ur-Nammu (or his son Shulgi) of Ur during the Third Dynasty of Ur (c. 2100–2050 BCE). Written in Sumerian on clay tablets, the code contains a prologue invoking the gods Nanna and Utu, followed by some 30+ surviving provisions. Unlike later Babylonian law, it favors monetary compensation over physical punishment. Fragments survive from Nippur and Ur, establishing the template for all subsequent Mesopotamian legal codification.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 2100–2050 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Centralized administration of Ur III empire requires legal standardization', type: 'Institution', year: 'c. 2112 BCE' },
    ],
    effects: [
      { title: 'Template for Laws of Eshnunna and Code of Hammurabi', type: 'Text', year: 'c. 1930 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Ur', role: 'Capital of the Ur III dynasty', slug: 'ur_city' },
    ],
    texts: [],
  },
  {
    slug: 'descent_of_inanna',
    name: 'Descent of Inanna',
    label: 'Text',
    callNumber: '730.24-descent-of-inanna',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Sumerian Mythology'],
    subjects: ['Inanna', 'Ishtar', 'Underworld', 'Ereshkigal', 'Dumuzi', 'Sumerian Mythology', 'Death and Resurrection'],
    summary: 'A Sumerian mythological poem (c. 1900–1600 BCE) narrating the goddess Inanna\'s descent into the underworld (Kur) ruled by her sister Ereshkigal. Inanna must pass through seven gates, removing an article of clothing/power at each, until she stands naked before the judges of the dead. She is killed but later resurrected through divine intervention, with her consort Dumuzi sent as her substitute. The Akkadian version, "Descent of Ishtar," is a later adaptation. The myth explores themes of death, resurrection, divine power, and the boundary between the living and the dead — motifs echoed in later Greek (Persephone), Egyptian (Osiris), and Christian theology.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 1900–1600 BCE',
    frameworks: ['CULTURAL_DIFFUSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [
      { title: 'Sumerian temple cult of Inanna at Uruk', type: 'Institution', year: 'c. 3000 BCE' },
    ],
    effects: [
      { title: 'Death-resurrection motif echoes through later mythologies', type: 'Idea', year: 'c. 1000 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Uruk', role: 'Center of Inanna worship', slug: 'uruk_city' },
    ],
    texts: [],
  },
  {
    slug: 'atrahasis_epic',
    name: 'Atrahasis Epic',
    label: 'Text',
    callNumber: '730.25-atrahasis-epic',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Babylonian Flood Narrative'],
    subjects: ['Atrahasis', 'Flood Myth', 'Creation', 'Enlil', 'Human Creation', 'Akkadian Literature'],
    summary: 'A Babylonian epic (Old Babylonian period, c. 1700 BCE) that narrates the creation of humanity by the gods, the subsequent overpopulation crisis, divine attempts to reduce humanity through plague and famine, and culminates in the Great Flood sent by Enlil. The hero Atrahasis (meaning "exceedingly wise") is warned by the god Enki to build an ark, surviving the deluge with his family and animals. This narrative predates and directly influences the Gilgamesh Tablet XI flood story and the Genesis flood narrative, making it a critical link in the chain of ancient Near Eastern flood traditions.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 1700 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Earlier Sumerian flood traditions (Eridu Genesis)', type: 'Text', year: 'c. 2100 BCE' },
    ],
    effects: [
      { title: 'Flood narrative incorporated into Epic of Gilgamesh Tablet XI', type: 'Text', year: 'c. 1200 BCE', slug: 'epic_of_gilgamesh' },
      { title: 'Parallels with Genesis 6–9 flood account', type: 'Text', year: 'c. 500 BCE', slug: 'genesis' },
    ],
    relationships: [
      { sourceSlug: 'atrahasis_epic', sourceName: 'Atrahasis Epic', verb: 'INFLUENCES', targetSlug: 'epic_of_gilgamesh', targetName: 'Epic of Gilgamesh', context: 'Flood narrative source for Tablet XI' },
      { sourceSlug: 'atrahasis_epic', sourceName: 'Atra-Ḫasīs', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Flood narrative parallel predating Gilgamesh version; creation-of-humanity theme' }
    ],
    places: [
      { name: 'Sippar', role: 'Possible composition site (Old Babylonian scribal tradition)', slug: 'sippar_city' },
    ],
    texts: [],
  },
  {
    slug: 'sumerian_king_list',
    name: 'Sumerian King List',
    label: 'Text',
    callNumber: '730.26-sumerian-king-list',
    subjectHeadings: ['Artifacts & Texts — Historical Records — Mesopotamian Chronology'],
    subjects: ['King List', 'Sumer', 'Chronology', 'Antediluvian Kings', 'Dynasties', 'Cuneiform'],
    summary: 'A cuneiform composition preserved on multiple tablets and prisms (most complete: Weld-Blundell Prism, c. 1827 BCE) that lists the rulers of Sumer from the beginning of kingship — "when kingship descended from heaven" — through historical dynasties. Includes fantastically long reigns for antediluvian kings (tens of thousands of years each), a reference to the Great Flood, then progressively more realistic reign lengths for historical dynasties. The King List served as political propaganda, legitimizing whichever dynasty currently held power by connecting it to an unbroken chain of sovereignty from the gods. Invaluable for Mesopotamian chronology despite its mythological framing.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 2100–1800 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Political need to legitimize Isin dynasty after fall of Ur III', type: 'Event', year: 'c. 2004 BCE' },
    ],
    effects: [
      { title: 'Framework for Mesopotamian historical chronology', type: 'Idea', year: 'c. 1800 BCE' },
      { title: 'Antediluvian king motif parallels Genesis 5 patriarchal ages', type: 'Text', year: 'c. 500 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Nippur', role: 'Major find-spot for king list tablets' },
    ],
    texts: [],
  },
  {
    slug: 'enheduanna_hymns',
    name: 'Hymns of Enheduanna',
    label: 'Text',
    callNumber: '730.27-enheduanna-hymns',
    subjectHeadings: ['Artifacts & Texts — Ancient Literature — Sumerian Religious Poetry'],
    subjects: ['Enheduanna', 'Inanna', 'Hymns', 'Temple Hymns', 'Sumerian Poetry', 'First Author'],
    summary: 'A collection of 42 temple hymns and personal devotional poems composed by Enheduanna (fl. c. 2285–2250 BCE), high priestess of the moon god Nanna at Ur and daughter of Sargon of Akkad. Enheduanna is the earliest known author in human history whose name is recorded. Her most famous works — "The Exaltation of Inanna" (Nin-me-šára), "Inanna and Ebih," and the 42 Temple Hymns — combine passionate personal devotion with sophisticated theological reflection, establishing models for religious lyric poetry that persist through the Psalms and into modern hymnody.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 2285–2250 BCE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Sargon of Akkad appoints daughter as high priestess to consolidate power', type: 'Person', year: 'c. 2285 BCE', slug: 'enheduanna' },
    ],
    effects: [
      { title: 'Earliest model for first-person devotional literature', type: 'Idea', year: 'c. 2250 BCE' },
      { title: 'Influence on Psalms and later hymnic traditions', type: 'Text', year: 'c. 1000 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Ur', role: 'Enheduanna\'s temple at Ur', slug: 'ur_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PEOPLE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'gilgamesh',
    name: 'Gilgamesh',
    label: 'Person',
    callNumber: '250.10-gilgamesh',
    subjectHeadings: ['People — Ancient Rulers — Mesopotamian Kings'],
    subjects: ['Uruk', 'Epic Hero', 'Semi-divine King', 'Third Millennium BCE', 'Sumerian Mythology'],
    summary: 'Semi-legendary king of Uruk (c. 2700 BCE) who became the subject of the world\'s oldest great literary work. Historical evidence (the Tummal Inscription and the Sumerian King List) suggests a real ruler underlies the legendary figure. In the epic, Gilgamesh is described as two-thirds divine, a tyrannical ruler who becomes wise through friendship with Enkidu, grief over Enkidu\'s death, and the failed quest for immortality. His story encapsulates the Mesopotamian understanding that eternal fame through great deeds, not literal immortality, is humanity\'s true destiny.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 2700 BCE',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Subject of the Epic of Gilgamesh — oldest known literature', type: 'Text', year: 'c. 2100 BCE', slug: 'epic_of_gilgamesh' },
    ],
    relationships: [
      { sourceSlug: 'gilgamesh', sourceName: 'Gilgamesh', verb: 'INFLUENCES', targetSlug: 'epic_of_gilgamesh', targetName: 'Epic of Gilgamesh', context: 'Historical figure inspiring the epic' },
    ],
    places: [
      { name: 'Uruk', role: 'Ruled as king', slug: 'uruk_city' },
    ],
    texts: [],
  },
  {
    slug: 'enheduanna',
    name: 'Enheduanna',
    label: 'Person',
    callNumber: '250.12-enheduanna',
    subjectHeadings: ['People — Ancient Authors — Mesopotamian Poets'],
    subjects: ['First Author', 'High Priestess', 'Nanna', 'Inanna', 'Sargon of Akkad', 'Sumerian Poetry', 'Women in History'],
    summary: 'High priestess of the moon god Nanna at Ur and daughter of Sargon of Akkad (fl. c. 2285–2250 BCE). Enheduanna is the earliest known named author in human history. She composed 42 temple hymns and several personal devotional poems to the goddess Inanna, including "The Exaltation of Inanna" (Nin-me-šára). Her works combine passionate religious experience with sophisticated literary composition, making her the first known individual to sign their name to literary works. A calcite disk depicting her was found at Ur, and her works continued to be copied in scribal schools for centuries after her death.',
    born: 'c. 2285 BCE',
    died: 'c. 2250 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Established tradition of authorial attribution in literature', type: 'Idea', year: 'c. 2280 BCE' },
    ],
    relationships: [
      { sourceSlug: 'enheduanna', sourceName: 'Enheduanna', verb: 'AUTHORS', targetSlug: 'enheduanna_hymns', targetName: 'Hymns of Enheduanna', context: 'First known named author in history' },
    ],
    places: [
      { name: 'Ur', role: 'High priestess at the temple of Nanna', slug: 'ur_city' },
    ],
    texts: [],
  },
  {
    slug: 'sargon_of_akkad',
    name: 'Sargon of Akkad',
    label: 'Person',
    callNumber: '250.13-sargon-of-akkad',
    subjectHeadings: ['People — Ancient Rulers — Akkadian Kings'],
    subjects: ['Akkadian Empire', 'First Empire', 'Sumer', 'Conquest', 'Mesopotamia', 'Empire Builder'],
    summary: 'Founder of the Akkadian Empire (r. c. 2334–2279 BCE), the world\'s first known multi-ethnic empire stretching from the Persian Gulf to the Mediterranean. Born of obscure origins (his birth legend parallels Moses\'), Sargon rose from cupbearer to king, conquered Sumerian city-states, and established Akkadian as the lingua franca of Mesopotamia. His empire\'s bureaucratic innovations, road systems, and cultural patronage (including his daughter Enheduanna\'s literary works) established templates for imperial governance that persisted for two millennia.',
    born: 'c. 2334 BCE',
    died: 'c. 2279 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Creates world\'s first multi-ethnic empire', type: 'Event', year: 'c. 2334 BCE' },
      { title: 'Akkadian becomes lingua franca of the Near East', type: 'Idea', year: 'c. 2300 BCE' },
    ],
    relationships: [
      { sourceSlug: 'sargon_of_akkad', sourceName: 'Sargon of Akkad', verb: 'FOUNDS', targetSlug: 'edubba_scribal_schools', targetName: 'Edubba Scribal Schools', context: 'Akkadian empire spread cuneiform literacy through scribal institutions' },
    ],
    places: [
      { name: 'Akkad', role: 'Capital city (exact location unknown)' },
    ],
    texts: [],
  },
  {
    slug: 'ashurbanipal',
    name: 'Ashurbanipal',
    label: 'Person',
    callNumber: '250.14-ashurbanipal',
    subjectHeadings: ['People — Ancient Rulers — Assyrian Kings'],
    subjects: ['Assyria', 'Library of Nineveh', 'Cuneiform', 'Scholar King', 'Neo-Assyrian Empire'],
    summary: 'Last great king of the Neo-Assyrian Empire (r. 668–631 BCE), renowned both as a warrior and the most literate ruler in Mesopotamian history. Ashurbanipal assembled the Library of Nineveh — one of the ancient world\'s greatest libraries — containing over 30,000 cuneiform tablets covering literature, science, medicine, astronomy, ritual, and law. His systematic collection and cataloging of Mesopotamian literary heritage preserved texts like the Epic of Gilgamesh and Enūma Eliš for posterity. The library\'s discovery by Austen Henry Layard in the 1850s revolutionized modern understanding of ancient civilization.',
    born: 'c. 685 BCE',
    died: 'c. 631 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [],
    effects: [
      { title: 'Library of Nineveh preserves Mesopotamian literary heritage', type: 'Institution', year: 'c. 650 BCE', slug: 'library_of_nineveh' },
    ],
    relationships: [
      { sourceSlug: 'ashurbanipal', sourceName: 'Ashurbanipal', verb: 'ESTABLISHES', targetSlug: 'library_of_nineveh', targetName: 'Library of Nineveh', context: 'Assembled 30,000+ cuneiform tablets' },
    ],
    places: [
      { name: 'Nineveh', role: 'Capital and site of the royal library', slug: 'nineveh' },
    ],
    texts: [],
  },
  {
    slug: 'nebuchadnezzar_ii',
    name: 'Nebuchadnezzar II',
    label: 'Person',
    callNumber: '250.15-nebuchadnezzar-ii',
    subjectHeadings: ['People — Ancient Rulers — Babylonian Kings'],
    subjects: ['Neo-Babylonian Empire', 'Babylon', 'Jerusalem', 'Destruction of Temple', 'Babylonian Exile', 'Hanging Gardens'],
    summary: 'King of the Neo-Babylonian Empire (r. 605–562 BCE), the most powerful ruler of the Chaldean dynasty. Nebuchadnezzar II rebuilt Babylon into the largest and most magnificent city in the ancient world — including the Ishtar Gate, the Processional Way, and the legendary Hanging Gardens (one of the Seven Wonders). He conquered Jerusalem in 586 BCE, destroyed Solomon\'s Temple, and deported the Judean elite to Babylon, initiating the Babylonian Exile — a transformative event in Jewish history that catalyzed the canonization of Hebrew scriptures. He figures prominently in the Book of Daniel.',
    born: 'c. 634 BCE',
    died: '562 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION', 'DOCTRINE_DEVELOPMENT'],
    causes: [],
    effects: [
      { title: 'Destruction of First Temple and Babylonian Exile', type: 'Event', year: '586 BCE', slug: 'babylonian_exile' },
      { title: 'Exile catalyzes canonization of Hebrew scripture', type: 'Text', year: 'c. 550 BCE' },
    ],
    relationships: [
      { sourceSlug: 'nebuchadnezzar_ii', sourceName: 'Nebuchadnezzar II', verb: 'CAUSES', targetSlug: 'babylonian_exile', targetName: 'Babylonian Exile', context: 'Destroys First Temple 586 BCE; deports Judean elite to Babylon' },
    ],
    places: [
      { name: 'Babylon', role: 'Capital of his empire', slug: 'babylon_city' },
      { name: 'Jerusalem', role: 'Conquered and destroyed the Temple', slug: 'jerusalem' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  INSTITUTIONS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'library_of_nineveh',
    name: 'Library of Nineveh',
    label: 'Institution',
    callNumber: '340.10-library-of-nineveh',
    subjectHeadings: ['Institutions — Archives & Libraries — Ancient Libraries'],
    subjects: ['Ashurbanipal', 'Cuneiform', 'Nineveh', 'Assyria', 'Ancient Library', 'Manuscript Preservation'],
    summary: 'The royal library of the Neo-Assyrian king Ashurbanipal at Nineveh (c. 668–631 BCE), containing over 30,000 cuneiform tablets and fragments — one of the greatest collections of knowledge in the ancient world. The library systematically collected, copied, and cataloged texts from across Mesopotamia: literary epics, medical treatises, astronomical observations, mathematical tables, omen collections, hymns, prayers, royal correspondence, and law codes. Its discovery in the 1850s by Austen Henry Layard and Hormuzd Rassam unlocked the ancient Mesopotamian world for modern scholarship.',
    founded: 'c. 668 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Ashurbanipal\'s passion for literacy and collecting', type: 'Person', year: 'c. 668 BCE', slug: 'ashurbanipal' },
    ],
    effects: [
      { title: 'Preserved Epic of Gilgamesh, Enūma Eliš, and thousands of texts', type: 'Text', year: 'c. 650 BCE' },
      { title: 'Modern discovery revolutionizes Assyriology', type: 'Event', year: '1853 CE' },
    ],
    relationships: [],
    places: [
      { name: 'Nineveh', role: 'Site of the library', slug: 'nineveh' },
    ],
    texts: [],
  },
  {
    slug: 'edubba_scribal_schools',
    name: 'Edubba (Scribal Schools)',
    label: 'Institution',
    callNumber: '340.11-edubba-scribal-schools',
    subjectHeadings: ['Institutions — Educational Institutions — Mesopotamian Schools'],
    subjects: ['Scribal Education', 'Cuneiform', 'Sumer', 'Literacy', 'Tablet House', 'Education'],
    summary: 'The edubba ("tablet house") was the Sumerian institution of scribal education, active from the mid-third millennium BCE through the Old Babylonian period (c. 2500–1600 BCE). Students (predominantly male, from elite families) underwent years of rigorous training: copying signs, mastering bilingual (Sumerian-Akkadian) vocabularies, composing mathematical and literary exercises, and eventually producing original works. The edubba preserved and transmitted the Mesopotamian literary canon across generations, and its student exercises are among our richest sources for understanding both pedagogy and literature in ancient Sumer. "Schooldays" literary compositions provide vivid first-person accounts of student life.',
    founded: 'c. 2500 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Growing administrative complexity requires trained scribes', type: 'Idea', year: 'c. 2600 BCE' },
    ],
    effects: [
      { title: 'Preserved and transmitted Sumerian literary canon', type: 'Text', year: 'c. 2000 BCE' },
      { title: 'Created bilingual Sumerian-Akkadian lexical tradition', type: 'Idea', year: 'c. 1800 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Nippur', role: 'Major scribal school center' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  PLACES
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'nineveh',
    name: 'Nineveh',
    label: 'Place',
    callNumber: '440.10-nineveh',
    subjectHeadings: ['Places — Ancient Cities — Mesopotamian Cities'],
    subjects: ['Assyria', 'Tigris River', 'Library of Ashurbanipal', 'Capital City', 'Ancient Iraq'],
    summary: 'Capital of the Neo-Assyrian Empire at its zenith (c. 705–612 BCE), located on the eastern bank of the Tigris River in modern Mosul, Iraq. Under Sennacherib and Ashurbanipal, Nineveh was one of the largest and most magnificent cities in the ancient world, enclosed by a 12-kilometer wall with fifteen gates. Home to Ashurbanipal\'s library, the Palace Without Rival, and extensive irrigation works. Its dramatic fall in 612 BCE to a coalition of Babylonians and Medes became a symbol of divine judgment in the Hebrew Bible (Book of Nahum, Book of Jonah).',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 6000 BCE – 612 BCE',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Fall of Nineveh ends Assyrian Empire', type: 'Event', year: '612 BCE' },
    ],
    relationships: [
      { sourceSlug: 'library_of_nineveh', sourceName: 'Library of Nineveh', verb: 'OCCURS_IN', targetSlug: 'nineveh', targetName: 'Nineveh', context: "Ashurbanipal's royal library located in Nineveh" }
    ],
    places: [],
    texts: [],
  },
  {
    slug: 'uruk_city',
    name: 'Uruk',
    label: 'Place',
    callNumber: '440.11-uruk',
    subjectHeadings: ['Places — Ancient Cities — Sumerian Cities'],
    subjects: ['Sumer', 'First City', 'Gilgamesh', 'Cuneiform Origins', 'Urbanization', 'Inanna'],
    summary: 'One of the world\'s first true cities (modern Warka, Iraq), flourishing from c. 4000 BCE and becoming the largest city in the world by c. 3200 BCE with a population of 40,000–80,000. Uruk is where the earliest known writing (proto-cuneiform) emerged, where monumental architecture first appeared (the White Temple, the Eanna precinct dedicated to Inanna), and where the legendary king Gilgamesh supposedly ruled. The "Uruk Period" (c. 4000–3100 BCE) is named after this city, marking humanity\'s transition from agricultural villages to complex urban civilization.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 4000–300 BCE',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Invention of writing emerges from Uruk administration', type: 'Idea', year: 'c. 3400 BCE' },
      { title: 'Template for Near Eastern urban civilization', type: 'Idea', year: 'c. 3200 BCE' },
    ],
    relationships: [],
    places: [],
    texts: [],
  },
  {
    slug: 'ur_city',
    name: 'Ur',
    label: 'Place',
    callNumber: '440.12-ur',
    subjectHeadings: ['Places — Ancient Cities — Sumerian Cities'],
    subjects: ['Sumer', 'Third Dynasty of Ur', 'Ziggurat', 'Abraham', 'Ur-Nammu', 'Nanna'],
    summary: 'Major Sumerian city-state on the Euphrates River (modern Tell el-Muqayyar, Iraq), reaching its apogee during the Third Dynasty of Ur (Ur III, c. 2112–2004 BCE) under kings Ur-Nammu and Shulgi. Home to the Great Ziggurat dedicated to the moon god Nanna, elaborate royal tombs with extraordinary grave goods (Royal Tombs of Ur, excavated by Leonard Woolley in the 1920s–1930s), and the administrative center that produced the Code of Ur-Nammu. Biblically identified as "Ur of the Chaldees," traditional birthplace of Abraham.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 3800–500 BCE',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [],
    effects: [
      { title: 'Code of Ur-Nammu — oldest surviving law code', type: 'Text', year: 'c. 2100 BCE', slug: 'code_of_ur_nammu' },
    ],
    relationships: [],
    places: [],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  EVENTS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'fall_of_nineveh',
    name: 'Fall of Nineveh',
    label: 'EventWindow',
    callNumber: '570.10-fall-of-nineveh',
    subjectHeadings: ['Events — Military Events — Ancient Sieges'],
    subjects: ['Assyria', 'Nineveh', 'Babylonia', 'Medes', 'Empire Collapse', '612 BCE'],
    summary: 'The siege and destruction of Nineveh in 612 BCE by a coalition of Babylonians (under Nabopolassar), Medes (under Cyaxares), and Scythian allies, ending the Neo-Assyrian Empire — the ancient world\'s most powerful military state. The city was sacked and largely abandoned, its ruins disappearing under the soil for over two millennia. The fall fulfilled Hebrew prophetic texts (Nahum, Zephaniah) and triggered a complete reorganization of Near Eastern geopolitics, enabling the rise of the Neo-Babylonian and Median empires.',
    startDate: '612 BCE',
    endDate: '612 BCE',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    frameworks: ['CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Overextension and civil wars weaken Assyrian Empire', type: 'Event', year: 'c. 630 BCE' },
    ],
    effects: [
      { title: 'Rise of Neo-Babylonian Empire under Nebuchadnezzar', type: 'Person', year: '605 BCE', slug: 'nebuchadnezzar_ii' },
      { title: 'Transformed into biblical symbol of divine judgment', type: 'Idea', year: 'c. 600 BCE' },
    ],
    relationships: [],
    places: [
      { name: 'Nineveh', role: 'Site of the siege', slug: 'nineveh' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  IDEAS
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'cuneiform_writing',
    name: 'Cuneiform Writing',
    label: 'Idea',
    callNumber: '140.10-cuneiform-writing',
    subjectHeadings: ['Ideas — Writing Systems — Ancient Scripts'],
    subjects: ['Writing', 'Sumer', 'Script', 'Clay Tablets', 'Literacy', 'Record-Keeping'],
    summary: 'The world\'s earliest writing system, developed in southern Mesopotamia (Sumer) c. 3400–3200 BCE, initially for administrative record-keeping. Evolved from pictographic tokens to wedge-shaped (Latin: cuneus, "wedge") impressions on wet clay tablets made with a reed stylus. Over three millennia, cuneiform was adapted to write Sumerian, Akkadian, Babylonian, Assyrian, Elamite, Hittite, Hurrian, and Urartian, serving as the writing system of an entire civilization complex. Deciphered in the 1850s by Henry Rawlinson using the trilingual Behistun Inscription.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 3400 BCE – 75 CE',
    frameworks: ['TEXTUAL_TRANSMISSION', 'CULTURAL_DIFFUSION'],
    causes: [
      { title: 'Administrative needs of Sumerian temple economies', type: 'Institution', year: 'c. 3500 BCE' },
    ],
    effects: [
      { title: 'Enables recording of literature, law, science, and history', type: 'Idea', year: 'c. 3000 BCE' },
      { title: 'Model for later writing systems across the Near East', type: 'Idea', year: 'c. 2500 BCE' },
    ],
    relationships: [
      { sourceSlug: 'cuneiform_writing', sourceName: 'Cuneiform Writing', verb: 'ENABLES', targetSlug: 'mesopotamian_corpus', targetName: 'Mesopotamian Corpus', context: 'Cuneiform script preserved all major Mesopotamian literary traditions' },
    ],
    places: [
      { name: 'Uruk', role: 'Earliest proto-cuneiform tablets found here', slug: 'uruk_city' },
    ],
    texts: [],
  },

  // ═══════════════════════════════════════════════════════════════════
  //  EVIDENCE
  // ═══════════════════════════════════════════════════════════════════
  {
    slug: 'flood_tablet_gilgamesh_xi',
    name: 'The Flood Tablet (Gilgamesh Tablet XI)',
    label: 'Evidence',
    callNumber: '810.10-flood-tablet',
    subjectHeadings: ['Evidence — Archaeological Artifacts — Cuneiform Tablets'],
    subjects: ['Flood Narrative', 'Gilgamesh', 'Ashurbanipal', 'British Museum', 'George Smith', 'Cuneiform'],
    summary: 'A cuneiform tablet (K.3375) from the Library of Nineveh, now in the British Museum, containing the Mesopotamian flood narrative as told in Tablet XI of the Standard Babylonian Epic of Gilgamesh. Deciphered by George Smith in 1872, its publication caused a sensation in Victorian England because of its striking parallels to the Genesis flood account — including a divine warning, construction of a vessel, loading of animals, a great flood, the sending of birds (dove, swallow, raven), and a post-flood sacrifice. This single tablet revolutionized the relationship between biblical and ancient Near Eastern studies.',
    era: 'Classical',
    eraSlug: 'classical',
    region: 'Middle East',
    continent: 'Asia',
    status: 'Published',
    period: 'c. 650 BCE (copied from older originals)',
    frameworks: ['TEXTUAL_TRANSMISSION'],
    causes: [
      { title: 'Ashurbanipal\'s library collection project', type: 'Person', year: 'c. 650 BCE', slug: 'ashurbanipal' },
    ],
    effects: [
      { title: 'Transforms biblical scholarship by demonstrating Near Eastern parallels', type: 'Idea', year: '1872 CE' },
    ],
    relationships: [
      { sourceSlug: 'flood_tablet_gilgamesh_xi', sourceName: 'Flood Tablet (Gilgamesh XI)', verb: 'FRAMES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Physical evidence demonstrating Mesopotamian flood parallel to Genesis 6–9' },
    ],
    places: [
      { name: 'Nineveh', role: 'Found in Ashurbanipal\'s library', slug: 'nineveh' },
    ],
    texts: [],
  },
]
