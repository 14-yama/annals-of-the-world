#!/usr/bin/env python3
"""Enrich hand-curated catalog entities with text nodes.

Reads each catalog .ts file, finds entities with `texts: []`,
looks up appropriate texts from a curated mapping, and replaces
the empty array with the enriched texts.
"""

import re
import os

# ── Curated text mapping: slug → list of {title, type, year?} ──────────────

TEXT_MAP: dict[str, list[dict]] = {
    # ═══════════════════════ PREHISTORIC ═══════════════════════
    "animism": [
        {"title": "The Golden Bough", "type": "Anthropological study", "year": "1890"},
    ],
    "fire_control": [
        {"title": "Traces of Early Fire Use (Wonderwerk Cave)", "type": "Archaeological report"},
    ],
    "tool_making": [
        {"title": "Oldowan Tool Assemblage Records", "type": "Archaeological catalogue"},
    ],
    "symbolic_thinking": [
        {"title": "Blombos Cave Ochre Engravings", "type": "Archaeological record"},
    ],
    "language_origin": [
        {"title": "On the Origin of Language (Herder)", "type": "Philosophical treatise", "year": "1772"},
    ],
    "agriculture_concept": [
        {"title": "Guns, Germs, and Steel", "type": "Historical analysis", "year": "1997"},
    ],
    "domestication": [
        {"title": "The Variation of Animals and Plants under Domestication", "type": "Scientific treatise", "year": "1868"},
    ],
    "neolithic_revolution": [
        {"title": "Man Makes Himself", "type": "Archaeological study", "year": "1936"},
    ],
    "last_ice_age_end": [
        {"title": "Ice Age Geological Survey Records", "type": "Geological report"},
    ],
    "early_human_migration": [
        {"title": "Out of Africa Migration Studies", "type": "Genetic study"},
    ],
    "fertile_crescent": [
        {"title": "The Rise of the Fertile Crescent", "type": "Archaeological survey"},
    ],
    "gobekli_tepe": [
        {"title": "Göbekli Tepe Excavation Reports", "type": "Archaeological report", "year": "1995"},
    ],
    "catalhoyuk": [
        {"title": "Çatalhöyük Excavation Records", "type": "Archaeological report"},
    ],
    "lascaux_paintings": [
        {"title": "Lascaux Cave Documentation", "type": "Archaeological record", "year": "1940"},
    ],
    "stone_tools": [
        {"title": "Acheulean Handaxe Catalogues", "type": "Archaeological catalogue"},
    ],

    # ═══════════════════════ CLASSICAL ═══════════════════════
    "socrates": [
        {"title": "Apology (Plato's account)", "type": "Philosophical dialogue"},
        {"title": "Memorabilia (Xenophon)", "type": "Biographical memoir"},
    ],
    "aristotle": [
        {"title": "Nicomachean Ethics", "type": "Philosophical treatise"},
        {"title": "Politics", "type": "Philosophical treatise"},
        {"title": "Metaphysics", "type": "Philosophical treatise"},
    ],
    "alexander_the_great": [
        {"title": "Anabasis of Alexander (Arrian)", "type": "Historical chronicle"},
        {"title": "Life of Alexander (Plutarch)", "type": "Biography"},
    ],
    "cleopatra": [
        {"title": "Life of Antony (Plutarch)", "type": "Biography"},
    ],
    "ramesses_ii": [
        {"title": "Poem of Pentaur (Battle of Kadesh)", "type": "Ancient text"},
        {"title": "Abu Simbel Temple Inscriptions", "type": "Inscription"},
    ],
    "democracy": [
        {"title": "The Athenian Constitution (Aristotle)", "type": "Political treatise"},
        {"title": "History of the Peloponnesian War (Thucydides)", "type": "Historical chronicle"},
    ],
    "republic": [
        {"title": "The Republic (Plato)", "type": "Philosophical dialogue"},
        {"title": "De Re Publica (Cicero)", "type": "Political treatise"},
    ],
    "greek_natural_philosophy": [
        {"title": "On Nature (Parmenides)", "type": "Philosophical fragment"},
        {"title": "Physics (Aristotle)", "type": "Philosophical treatise"},
    ],
    "roman_senate": [
        {"title": "Ab Urbe Condita (Livy)", "type": "Historical chronicle"},
    ],
    "athenian_assembly": [
        {"title": "The Athenian Constitution (Aristotle)", "type": "Political treatise"},
    ],
    "library_of_alexandria": [
        {"title": "Elements (Euclid)", "type": "Mathematical treatise"},
        {"title": "The Geography (Strabo)", "type": "Geographical compendium"},
    ],
    "punic_wars": [
        {"title": "The Histories (Polybius)", "type": "Historical chronicle"},
    ],
    "battle_of_thermopylae": [
        {"title": "Histories (Herodotus)", "type": "Historical chronicle"},
    ],
    "battle_of_marathon": [
        {"title": "Histories (Herodotus)", "type": "Historical chronicle"},
    ],
    "fall_of_rome": [
        {"title": "The History of the Decline and Fall of the Roman Empire", "type": "Historical analysis", "year": "1776"},
    ],
    "crucifixion": [
        {"title": "The Gospels (Matthew, Mark, Luke, John)", "type": "Scripture"},
        {"title": "Annals (Tacitus)", "type": "Historical chronicle"},
    ],
    "spread_of_christianity": [
        {"title": "Acts of the Apostles", "type": "Scripture"},
        {"title": "Ecclesiastical History (Eusebius)", "type": "Church history"},
    ],
    "greek_enlightenment": [
        {"title": "Theogony (Hesiod)", "type": "Epic poem"},
        {"title": "Fragments of the Pre-Socratics", "type": "Philosophical fragments"},
    ],
    "republic_plato": [
        {"title": "The Republic (Plato)", "type": "Philosophical dialogue"},
    ],
    "art_of_war": [
        {"title": "The Art of War (Sun Tzu)", "type": "Military treatise", "year": "-500"},
    ],
    "code_of_hammurabi": [
        {"title": "Code of Hammurabi Stele Inscription", "type": "Legal code", "year": "-1754"},
    ],
    "torah": [
        {"title": "The Five Books of Moses", "type": "Scripture"},
    ],
    "rome": [
        {"title": "Ab Urbe Condita (Livy)", "type": "Historical chronicle"},
    ],
    "athens": [
        {"title": "The Athenian Constitution", "type": "Political treatise"},
    ],
    "jerusalem": [
        {"title": "The Jewish War (Josephus)", "type": "Historical chronicle"},
    ],
    "alexandria": [
        {"title": "The Geography (Strabo)", "type": "Geographical compendium"},
    ],
    "roman_empire": [
        {"title": "Res Gestae Divi Augusti", "type": "Imperial inscription"},
        {"title": "Annals (Tacitus)", "type": "Historical chronicle"},
    ],
    "persian_empire": [
        {"title": "Behistun Inscription", "type": "Royal inscription"},
        {"title": "Cyropaedia (Xenophon)", "type": "Historical chronicle"},
    ],
    "ancient_egypt": [
        {"title": "Book of the Dead", "type": "Funerary text"},
        {"title": "Palermo Stone", "type": "Royal annals"},
    ],
    "sanhedrin": [
        {"title": "Mishnah Sanhedrin", "type": "Rabbinic text"},
    ],

    # ═══════════════════════ MEDIEVAL ═══════════════════════
    "charlemagne": [
        {"title": "Vita Karoli Magni (Einhard)", "type": "Biography", "year": "830"},
        {"title": "Capitulare de Villis", "type": "Imperial decree"},
    ],
    "saladin": [
        {"title": "The Rare and Excellent History of Saladin", "type": "Biography"},
    ],
    "mansa_musa": [
        {"title": "Rihla (Ibn Battuta, accounts)", "type": "Travel chronicle"},
        {"title": "Catalan Atlas depiction", "type": "Cartographic record", "year": "1375"},
    ],
    "joan_of_arc": [
        {"title": "Trial of Joan of Arc (1431)", "type": "Legal transcript", "year": "1431"},
        {"title": "Rehabilitation Trial (1456)", "type": "Legal transcript", "year": "1456"},
    ],
    "feudalism": [
        {"title": "Capitulary of Quierzy", "type": "Legal decree", "year": "877"},
    ],
    "scholasticism": [
        {"title": "Sic et Non (Abelard)", "type": "Theological treatise"},
        {"title": "Summa Theologica (Aquinas)", "type": "Theological treatise"},
    ],
    "chivalry": [
        {"title": "The Song of Roland", "type": "Chanson de geste"},
        {"title": "The Book of the Order of Chivalry (Llull)", "type": "Treatise"},
    ],
    "islamic_golden_age_science": [
        {"title": "The Canon of Medicine (Ibn Sina)", "type": "Medical treatise", "year": "1025"},
        {"title": "Kitab al-Optics (Ibn al-Haytham)", "type": "Scientific treatise"},
    ],
    "catholic_church": [
        {"title": "Dictatus Papae", "type": "Papal decree", "year": "1075"},
        {"title": "Unam Sanctam", "type": "Papal bull", "year": "1302"},
    ],
    "holy_roman_empire": [
        {"title": "Golden Bull of 1356", "type": "Imperial charter", "year": "1356"},
    ],
    "university_of_bologna": [
        {"title": "Authentica Habita (1158)", "type": "Imperial charter", "year": "1158"},
    ],
    "abbasid_caliphate": [
        {"title": "Kitab al-Kharaj (Abu Yusuf)", "type": "Administrative treatise"},
    ],
    "first_crusade": [
        {"title": "Gesta Francorum", "type": "Chronicle", "year": "1101"},
        {"title": "Council of Clermont decrees (1095)", "type": "Papal decree", "year": "1095"},
    ],
    "mongol_invasions": [
        {"title": "The Secret History of the Mongols", "type": "Historical chronicle"},
    ],
    "hundred_years_war": [
        {"title": "Chronicles (Froissart)", "type": "Historical chronicle"},
        {"title": "Treaty of Troyes (1420)", "type": "Treaty", "year": "1420"},
    ],
    "black_death": [
        {"title": "The Decameron (Boccaccio)", "type": "Literary work", "year": "1353"},
        {"title": "Chronicle of the Black Death (de Mussis)", "type": "Chronicle"},
    ],
    "fall_of_constantinople": [
        {"title": "Doukas Chronicle", "type": "Historical chronicle"},
    ],
    "spread_of_islam": [
        {"title": "Quran", "type": "Scripture"},
        {"title": "Sahih al-Bukhari", "type": "Hadith collection"},
    ],
    "crusading_movement": [
        {"title": "Gesta Dei per Francos (Guibert of Nogent)", "type": "Chronicle"},
    ],
    "islamic_golden_age": [
        {"title": "The Book of Healing (Ibn Sina)", "type": "Philosophical encyclopedia"},
        {"title": "Al-Jabr (al-Khwarizmi)", "type": "Mathematical treatise", "year": "820"},
    ],
    "viking_expansion": [
        {"title": "The Saga of the Greenlanders", "type": "Saga"},
        {"title": "Anglo-Saxon Chronicle (Viking entries)", "type": "Chronicle"},
    ],
    "magna_carta": [
        {"title": "Magna Carta (1215)", "type": "Legal charter", "year": "1215"},
    ],
    "divine_comedy": [
        {"title": "Divina Commedia (Dante)", "type": "Epic poem", "year": "1320"},
    ],
    "summa_theologica": [
        {"title": "Summa Theologica (Thomas Aquinas)", "type": "Theological treatise", "year": "1274"},
    ],
    "quran": [
        {"title": "The Quran", "type": "Scripture"},
    ],
    "constantinople": [
        {"title": "Procopius, Buildings", "type": "Historical chronicle"},
    ],
    "baghdad": [
        {"title": "Travels of Ibn Battuta", "type": "Travel chronicle"},
    ],
    "byzantine_empire": [
        {"title": "Corpus Juris Civilis (Justinian)", "type": "Legal code", "year": "534"},
    ],
    "mongol_empire": [
        {"title": "The Secret History of the Mongols", "type": "Historical chronicle"},
    ],

    # ═══════════════════════ EARLY MODERN ═══════════════════════
    "elizabeth_i": [
        {"title": "Tilbury Speech (1588)", "type": "Speech", "year": "1588"},
        {"title": "Act of Supremacy (1559)", "type": "Legal document", "year": "1559"},
    ],
    "louis_xiv": [
        {"title": "Mémoires pour l'instruction du Dauphin", "type": "Memoir"},
        {"title": "Edict of Fontainebleau (1685)", "type": "Royal decree", "year": "1685"},
    ],
    "akbar": [
        {"title": "Akbarnama (Abu'l-Fazl)", "type": "Historical chronicle"},
        {"title": "Ain-i-Akbari", "type": "Administrative compendium"},
    ],
    "leonardo_da_vinci": [
        {"title": "Codex Leicester", "type": "Scientific notebook"},
        {"title": "Treatise on Painting", "type": "Art treatise"},
    ],
    "tokugawa_ieyasu": [
        {"title": "Legacy of Ieyasu (Tōshōgū Goikun)", "type": "Political testament"},
    ],
    "humanism": [
        {"title": "Oration on the Dignity of Man (Pico della Mirandola)", "type": "Philosophical oration", "year": "1486"},
    ],
    "enlightenment_thought": [
        {"title": "An Essay Concerning Human Understanding (Locke)", "type": "Philosophical treatise", "year": "1689"},
        {"title": "Encyclopédie (Diderot & d'Alembert)", "type": "Encyclopedia", "year": "1751"},
    ],
    "east_india_company": [
        {"title": "Royal Charter (1600)", "type": "Charter", "year": "1600"},
    ],
    "diet_of_worms": [
        {"title": "Edict of Worms (1521)", "type": "Imperial edict", "year": "1521"},
    ],
    "scientific_revolution": [
        {"title": "De Revolutionibus Orbium Coelestium (Copernicus)", "type": "Scientific treatise", "year": "1543"},
        {"title": "Principia Mathematica (Newton)", "type": "Scientific treatise", "year": "1687"},
    ],
    "renaissance": [
        {"title": "Lives of the Artists (Vasari)", "type": "Biographical compendium", "year": "1550"},
    ],
    "age_of_exploration": [
        {"title": "Journal of the First Voyage (Columbus)", "type": "Voyage journal", "year": "1493"},
        {"title": "Os Lusíadas (Camões)", "type": "Epic poem", "year": "1572"},
    ],
    "ninety_five_theses": [
        {"title": "Disputatio pro Declaratione Virtutis Indulgentiarum", "type": "Theological treatise", "year": "1517"},
    ],
    "principia_mathematica": [
        {"title": "Philosophiæ Naturalis Principia Mathematica", "type": "Scientific treatise", "year": "1687"},
    ],
    "us_constitution": [
        {"title": "Constitution of the United States", "type": "Legal document", "year": "1787"},
        {"title": "The Federalist Papers", "type": "Political essays", "year": "1788"},
    ],
    "declaration_of_independence": [
        {"title": "Declaration of Independence", "type": "Political declaration", "year": "1776"},
    ],
    "utopia_book": [
        {"title": "Utopia (Thomas More)", "type": "Political fiction", "year": "1516"},
    ],
    "ottoman_empire": [
        {"title": "Kanunname of Suleiman the Magnificent", "type": "Legal code"},
    ],
    "mughal_empire": [
        {"title": "Baburnama", "type": "Memoir"},
        {"title": "Akbarnama", "type": "Historical chronicle"},
    ],

    # ═══════════════════════ MODERN ═══════════════════════
    "treaty_of_versailles": [
        {"title": "Treaty of Versailles", "type": "International treaty", "year": "1919"},
    ],
    "spanish_civil_war": [
        {"title": "Homage to Catalonia (Orwell)", "type": "Memoir", "year": "1938"},
        {"title": "For Whom the Bell Tolls (Hemingway)", "type": "Novel", "year": "1940"},
    ],
    "queen_victoria": [
        {"title": "Queen Victoria's Journals", "type": "Personal diary"},
        {"title": "Letters of Queen Victoria", "type": "Correspondence"},
    ],
    "otto_von_bismarck": [
        {"title": "Ems Dispatch (1870)", "type": "Diplomatic dispatch", "year": "1870"},
        {"title": "Gedanken und Erinnerungen (Memoirs)", "type": "Memoir", "year": "1898"},
    ],
    "gandhi": [
        {"title": "The Story of My Experiments with Truth", "type": "Autobiography", "year": "1927"},
        {"title": "Hind Swaraj", "type": "Political treatise", "year": "1909"},
    ],
    "hitler": [
        {"title": "Mein Kampf", "type": "Political manifesto", "year": "1925"},
    ],
    "albert_einstein": [
        {"title": "On the Electrodynamics of Moving Bodies", "type": "Scientific paper", "year": "1905"},
        {"title": "General Theory of Relativity", "type": "Scientific paper", "year": "1915"},
    ],
    "nikola_tesla": [
        {"title": "My Inventions (autobiography)", "type": "Autobiography", "year": "1919"},
        {"title": "Experiments with Alternate Currents (lecture)", "type": "Scientific lecture", "year": "1891"},
    ],
    "imperialism": [
        {"title": "Imperialism, the Highest Stage of Capitalism (Lenin)", "type": "Political treatise", "year": "1917"},
    ],
    "relativity": [
        {"title": "On the Electrodynamics of Moving Bodies", "type": "Scientific paper", "year": "1905"},
        {"title": "The Foundation of the General Theory of Relativity", "type": "Scientific paper", "year": "1916"},
    ],
    "british_parliament": [
        {"title": "Bill of Rights (1689)", "type": "Legal document", "year": "1689"},
        {"title": "Parliament Acts (1911, 1949)", "type": "Legal statute"},
    ],
    "napoleonic_wars": [
        {"title": "Treaty of Tilsit (1807)", "type": "Treaty", "year": "1807"},
        {"title": "War and Peace (Tolstoy)", "type": "Novel", "year": "1869"},
    ],
    "american_civil_war": [
        {"title": "Gettysburg Address (Lincoln)", "type": "Speech", "year": "1863"},
        {"title": "Emancipation Proclamation", "type": "Executive order", "year": "1863"},
    ],
    "russian_revolution": [
        {"title": "The State and Revolution (Lenin)", "type": "Political treatise", "year": "1917"},
        {"title": "Ten Days That Shook the World (Reed)", "type": "Journalistic account", "year": "1919"},
    ],
    "industrial_revolution": [
        {"title": "The Condition of the Working Class in England (Engels)", "type": "Social study", "year": "1845"},
    ],
    "abolitionism": [
        {"title": "Narrative of the Life of Frederick Douglass", "type": "Autobiography", "year": "1845"},
        {"title": "Uncle Tom's Cabin (Stowe)", "type": "Novel", "year": "1852"},
    ],
    "labor_movement": [
        {"title": "The Communist Manifesto", "type": "Political manifesto", "year": "1848"},
    ],
    "fascism_movement": [
        {"title": "The Doctrine of Fascism (Mussolini/Gentile)", "type": "Political treatise", "year": "1932"},
    ],
    "british_empire": [
        {"title": "The Expansion of England (Seeley)", "type": "Historical analysis", "year": "1883"},
    ],
    "communist_manifesto": [
        {"title": "Manifest der Kommunistischen Partei", "type": "Political manifesto", "year": "1848"},
    ],
    "origin_of_species": [
        {"title": "On the Origin of Species (Darwin)", "type": "Scientific treatise", "year": "1859"},
    ],
    "emancipation_proclamation": [
        {"title": "Emancipation Proclamation", "type": "Executive order", "year": "1863"},
    ],
    "geneva_conventions": [
        {"title": "Geneva Convention (1864)", "type": "International treaty", "year": "1864"},
        {"title": "Geneva Conventions (1949)", "type": "International treaty", "year": "1949"},
    ],

    # ═══════════════════════ CONTEMPORARY ═══════════════════════
    "deng_xiaoping": [
        {"title": "Selected Works of Deng Xiaoping", "type": "Political writings"},
    ],
    "margaret_thatcher": [
        {"title": "The Downing Street Years (memoir)", "type": "Memoir", "year": "1993"},
    ],
    "korean_war": [
        {"title": "Korean War Armistice Agreement (1953)", "type": "Treaty", "year": "1953"},
    ],
    "cuban_missile_crisis": [
        {"title": "Thirteen Days (Robert Kennedy)", "type": "Memoir", "year": "1969"},
    ],
    "fall_berlin_wall": [
        {"title": "Tear Down This Wall (Reagan speech)", "type": "Speech", "year": "1987"},
    ],
    "apartheid": [
        {"title": "Long Walk to Freedom (Mandela)", "type": "Autobiography", "year": "1994"},
        {"title": "Truth and Reconciliation Commission Report", "type": "Government report", "year": "1998"},
    ],
    "september_11": [
        {"title": "The 9/11 Commission Report", "type": "Government report", "year": "2004"},
    ],
    "war_afghanistan": [
        {"title": "The Afghanistan Papers (Washington Post)", "type": "Investigative report", "year": "2019"},
    ],
    "iraq_war": [
        {"title": "The Iraq Study Group Report", "type": "Government report", "year": "2006"},
    ],
    "civil_rights_movement": [
        {"title": "Letter from Birmingham Jail (King)", "type": "Letter", "year": "1963"},
        {"title": "Why We Can't Wait (King)", "type": "Political treatise", "year": "1964"},
    ],
    "digital_revolution": [
        {"title": "Being Digital (Negroponte)", "type": "Technology treatise", "year": "1995"},
    ],
    "globalization": [
        {"title": "The World Is Flat (Friedman)", "type": "Economic analysis", "year": "2005"},
    ],
    "environmental_movement": [
        {"title": "Silent Spring (Rachel Carson)", "type": "Environmental study", "year": "1962"},
        {"title": "The Limits to Growth (Club of Rome)", "type": "Report", "year": "1972"},
    ],
    "udhr": [
        {"title": "Universal Declaration of Human Rights", "type": "International declaration", "year": "1948"},
    ],
    "civil_rights_act": [
        {"title": "Civil Rights Act of 1964", "type": "Legal statute", "year": "1964"},
    ],
    "paris_climate_agreement": [
        {"title": "Paris Agreement", "type": "International treaty", "year": "2015"},
    ],

    # ═══════════════════════ BIBLICAL ═══════════════════════
    "biblical_corpus": [
        {"title": "The Bible (canonical collections)", "type": "Scripture"},
    ],
    "genesis": [
        {"title": "Book of Genesis", "type": "Scripture"},
    ],
    "exodus_book": [
        {"title": "Book of Exodus", "type": "Scripture"},
    ],
    "leviticus": [
        {"title": "Book of Leviticus", "type": "Scripture"},
    ],
    "numbers_book": [
        {"title": "Book of Numbers", "type": "Scripture"},
    ],
    "deuteronomy": [
        {"title": "Book of Deuteronomy", "type": "Scripture"},
    ],
    "joshua_book": [
        {"title": "Book of Joshua", "type": "Scripture"},
    ],
    "judges_book": [
        {"title": "Book of Judges", "type": "Scripture"},
    ],
    "first_samuel": [
        {"title": "First Book of Samuel", "type": "Scripture"},
    ],
    "second_samuel": [
        {"title": "Second Book of Samuel", "type": "Scripture"},
    ],
    "first_kings": [
        {"title": "First Book of Kings", "type": "Scripture"},
    ],
    "psalms": [
        {"title": "Book of Psalms", "type": "Scripture"},
    ],
    "proverbs": [
        {"title": "Book of Proverbs", "type": "Scripture"},
    ],
    "ecclesiastes": [
        {"title": "Book of Ecclesiastes", "type": "Scripture"},
    ],
    "song_of_solomon": [
        {"title": "Song of Solomon", "type": "Scripture"},
    ],
    "job_book": [
        {"title": "Book of Job", "type": "Scripture"},
    ],
    "lamentations": [
        {"title": "Book of Lamentations", "type": "Scripture"},
    ],
    "isaiah_book": [
        {"title": "Book of Isaiah", "type": "Scripture"},
    ],
    "jeremiah_book": [
        {"title": "Book of Jeremiah", "type": "Scripture"},
    ],
    "ezekiel_book": [
        {"title": "Book of Ezekiel", "type": "Scripture"},
    ],
    "daniel_book": [
        {"title": "Book of Daniel", "type": "Scripture"},
    ],
    "gospel_of_matthew": [
        {"title": "Gospel According to Matthew", "type": "Scripture"},
    ],
    "gospel_of_mark": [
        {"title": "Gospel According to Mark", "type": "Scripture"},
    ],
    "gospel_of_luke": [
        {"title": "Gospel According to Luke", "type": "Scripture"},
    ],
    "gospel_of_john": [
        {"title": "Gospel According to John", "type": "Scripture"},
    ],
    "acts_of_the_apostles": [
        {"title": "Acts of the Apostles", "type": "Scripture"},
    ],
    "epistle_to_the_romans": [
        {"title": "Epistle to the Romans", "type": "Epistle"},
    ],
    "first_corinthians": [
        {"title": "First Epistle to the Corinthians", "type": "Epistle"},
    ],
    "galatians": [
        {"title": "Epistle to the Galatians", "type": "Epistle"},
    ],
    "revelation": [
        {"title": "Book of Revelation", "type": "Apocalyptic literature"},
    ],
    "twelve_tribes": [
        {"title": "Genesis (tribal narratives)", "type": "Scripture"},
    ],
    "levitical_priesthood": [
        {"title": "Book of Leviticus", "type": "Scripture"},
        {"title": "Book of Numbers (priestly duties)", "type": "Scripture"},
    ],
    "first_temple": [
        {"title": "First Book of Kings (Temple construction)", "type": "Scripture"},
    ],
    "second_temple": [
        {"title": "Book of Ezra", "type": "Scripture"},
        {"title": "Book of Nehemiah", "type": "Scripture"},
    ],
    "early_church": [
        {"title": "Didache", "type": "Early church manual"},
        {"title": "First Epistle of Clement", "type": "Epistle"},
    ],
    "great_flood": [
        {"title": "Genesis 6–9 (Flood narrative)", "type": "Scripture"},
        {"title": "Epic of Gilgamesh (Tablet XI)", "type": "Ancient epic"},
    ],
    "exodus_event": [
        {"title": "Book of Exodus", "type": "Scripture"},
    ],
    "conquest_of_canaan": [
        {"title": "Book of Joshua", "type": "Scripture"},
    ],
    "babylonian_exile": [
        {"title": "Book of Jeremiah (exile prophecies)", "type": "Scripture"},
        {"title": "Book of Ezekiel (exile visions)", "type": "Scripture"},
    ],
    "pentecost": [
        {"title": "Acts of the Apostles ch. 2", "type": "Scripture"},
    ],
    "council_of_jerusalem": [
        {"title": "Acts of the Apostles ch. 15", "type": "Scripture"},
    ],
    "destruction_second_temple": [
        {"title": "The Jewish War (Josephus)", "type": "Historical chronicle", "year": "75"},
    ],
    "babylon": [
        {"title": "Babylonian Chronicles", "type": "Ancient chronicle"},
    ],
    "egypt": [
        {"title": "Book of the Dead", "type": "Funerary text"},
    ],
    "mount_sinai": [
        {"title": "Book of Exodus (Sinai theophany)", "type": "Scripture"},
    ],
    "second_temple_judaism": [
        {"title": "Dead Sea Scrolls", "type": "Religious manuscripts"},
        {"title": "Mishnah", "type": "Rabbinic text"},
    ],
    "early_christianity": [
        {"title": "Didache", "type": "Early church manual"},
        {"title": "Letters of Ignatius of Antioch", "type": "Epistle"},
    ],
    "abrahamic_covenant": [
        {"title": "Genesis 12, 15, 17 (covenant passages)", "type": "Scripture"},
    ],
    "sinai_covenant": [
        {"title": "Exodus 19–24 (covenant at Sinai)", "type": "Scripture"},
    ],
    "davidic_covenant": [
        {"title": "2 Samuel 7 (Davidic promise)", "type": "Scripture"},
    ],
    "new_covenant": [
        {"title": "Jeremiah 31:31–34 (New Covenant prophecy)", "type": "Scripture"},
        {"title": "Hebrews 8 (New Covenant exposition)", "type": "Epistle"},
    ],
    "ten_commandments": [
        {"title": "Exodus 20 / Deuteronomy 5 (Decalogue)", "type": "Scripture"},
    ],
    "dead_sea_scrolls": [
        {"title": "Dead Sea Scrolls (Qumran library)", "type": "Religious manuscripts", "year": "-200"},
    ],
    "codex_sinaiticus": [
        {"title": "Codex Sinaiticus", "type": "Biblical manuscript", "year": "350"},
    ],

    # ═══════════════════════ REFORMATION ═══════════════════════
    "thomas_muenzter": [
        {"title": "Sermon to the Princes", "type": "Sermon", "year": "1524"},
        {"title": "Prague Manifesto", "type": "Manifesto", "year": "1521"},
    ],
    "council_of_trent": [
        {"title": "Decrees of the Council of Trent", "type": "Church decree", "year": "1563"},
    ],
    "peace_of_augsburg": [
        {"title": "Peace of Augsburg", "type": "Treaty", "year": "1555"},
    ],
    "st_bartholomews_day_massacre": [
        {"title": "Mémoires de Marguerite de Valois", "type": "Memoir"},
    ],
    "hussite_wars": [
        {"title": "De Ecclesia (Jan Hus)", "type": "Theological treatise", "year": "1413"},
    ],
    "society_of_jesus": [
        {"title": "Spiritual Exercises (Ignatius of Loyola)", "type": "Devotional manual", "year": "1548"},
        {"title": "Formula of the Institute (1540)", "type": "Founding charter", "year": "1540"},
    ],
    "catholic_reformation_movement": [
        {"title": "Decrees of the Council of Trent", "type": "Church decree", "year": "1563"},
    ],
    "book_of_common_prayer": [
        {"title": "Book of Common Prayer", "type": "Liturgical text", "year": "1549"},
    ],
    "augsburg_confession": [
        {"title": "Augsburg Confession (Confessio Augustana)", "type": "Confessional document", "year": "1530"},
    ],

    # ═══════════════════════ DIVISION ENRICHMENT ═══════════════════════
    "mercantilism": [
        {"title": "England's Treasure by Forraign Trade (Mun)", "type": "Economic treatise", "year": "1664"},
    ],
    "neoliberalism": [
        {"title": "The Road to Serfdom (Hayek)", "type": "Political treatise", "year": "1944"},
        {"title": "Capitalism and Freedom (Friedman)", "type": "Economic treatise", "year": "1962"},
    ],
    "gaia_hypothesis": [
        {"title": "Gaia: A New Look at Life on Earth (Lovelock)", "type": "Scientific treatise", "year": "1979"},
    ],
    "deep_ecology": [
        {"title": "The Shallow and the Deep (Næss)", "type": "Philosophical essay", "year": "1973"},
    ],
    "romanticism_movement": [
        {"title": "Lyrical Ballads (Wordsworth & Coleridge)", "type": "Poetry collection", "year": "1798"},
    ],
    "impressionism": [
        {"title": "Impression, Sunrise (Monet)", "type": "Artwork", "year": "1872"},
    ],
    "modernism_art": [
        {"title": "Les Demoiselles d'Avignon (Picasso)", "type": "Artwork", "year": "1907"},
    ],
    "postmodernism_art": [
        {"title": "The Postmodern Condition (Lyotard)", "type": "Philosophical treatise", "year": "1979"},
    ],
    "ruth_bader_ginsburg": [
        {"title": "My Own Words (RBG)", "type": "Collected writings", "year": "2016"},
    ],
    "emmeline_pankhurst": [
        {"title": "My Own Story", "type": "Autobiography", "year": "1914"},
    ],
    "desmond_tutu": [
        {"title": "No Future Without Forgiveness", "type": "Memoir", "year": "1999"},
    ],
    "international_court_of_justice": [
        {"title": "Statute of the International Court of Justice (1945)", "type": "Legal statute", "year": "1945"},
    ],
    "supreme_court_us": [
        {"title": "Marbury v. Madison opinion", "type": "Legal opinion", "year": "1803"},
    ],
    "achaemenid_empire": [
        {"title": "Behistun Inscription (Darius I)", "type": "Royal inscription"},
    ],
    "qing_dynasty": [
        {"title": "Sacred Edict of the Kangxi Emperor", "type": "Imperial decree"},
    ],
    "mongol_empire_place": [
        {"title": "The Secret History of the Mongols", "type": "Historical chronicle"},
    ],
    "silk_road_corridor": [
        {"title": "Travels of Marco Polo", "type": "Travel chronicle", "year": "1300"},
    ],
    "mediterranean_world": [
        {"title": "The Mediterranean (Braudel)", "type": "Historical analysis", "year": "1949"},
    ],
    "sahel_zone": [
        {"title": "Tarikh al-Sudan", "type": "Historical chronicle", "year": "1655"},
    ],
    "open_source_movement": [
        {"title": "The Cathedral and the Bazaar (Raymond)", "type": "Essay", "year": "1999"},
    ],
    "space_exploration_movement": [
        {"title": "The Right Stuff (Wolfe)", "type": "Narrative non-fiction", "year": "1979"},
    ],
    "internet_revolution": [
        {"title": "RFC 791 (Internet Protocol)", "type": "Technical specification", "year": "1981"},
    ],
    "conservation_movement": [
        {"title": "A Sand County Almanac (Leopold)", "type": "Environmental essay", "year": "1949"},
    ],
    "climate_justice_movement": [
        {"title": "This Changes Everything (Klein)", "type": "Environmental treatise", "year": "2014"},
    ],
    "rosetta_stone": [
        {"title": "Rosetta Stone Decree", "type": "Trilingual inscription", "year": "-196"},
    ],
    "mona_lisa": [
        {"title": "Mona Lisa (La Gioconda)", "type": "Artwork", "year": "1503"},
    ],
    "sistine_chapel_ceiling": [
        {"title": "Sistine Chapel Ceiling (Michelangelo)", "type": "Artwork", "year": "1512"},
    ],
    "guernica": [
        {"title": "Guernica (Picasso)", "type": "Artwork", "year": "1937"},
    ],
    "gutenberg_press": [
        {"title": "Gutenberg Bible", "type": "Printed book", "year": "1455"},
    ],
    "steam_engine_artifact": [
        {"title": "A Treatise on the Steam Engine (Tredgold)", "type": "Engineering treatise", "year": "1827"},
    ],
    "telegraph": [
        {"title": "What Hath God Wrought (first message)", "type": "Historical communication", "year": "1844"},
    ],
    "world_wide_web": [
        {"title": "Information Management: A Proposal (Berners-Lee)", "type": "Technical proposal", "year": "1989"},
    ],
    "domesday_book": [
        {"title": "Domesday Book", "type": "Census record", "year": "1086"},
    ],
    "federalist_papers": [
        {"title": "The Federalist Papers", "type": "Political essays", "year": "1788"},
    ],
    "nuremberg_trial_records": [
        {"title": "Nuremberg Trial Proceedings", "type": "Legal transcript", "year": "1946"},
    ],
    "histories_herodotus": [
        {"title": "The Histories (Herodotus)", "type": "Historical chronicle", "year": "-430"},
    ],
    "muqaddimah": [
        {"title": "Muqaddimah (Ibn Khaldun)", "type": "Historical analysis", "year": "1377"},
    ],
    "decline_and_fall_roman_empire": [
        {"title": "The History of the Decline and Fall of the Roman Empire (Gibbon)", "type": "Historical analysis", "year": "1776"},
    ],
    "lascaux_cave_paintings": [
        {"title": "Lascaux Cave Documentation", "type": "Archaeological record", "year": "1940"},
    ],
    "pompeii_excavations": [
        {"title": "Letters of Pliny the Younger (eruption account)", "type": "Epistle", "year": "79"},
    ],
    "terracotta_army": [
        {"title": "Records of the Grand Historian (Sima Qian)", "type": "Historical chronicle", "year": "-94"},
    ],
    "tutankhamun_tomb": [
        {"title": "The Tomb of Tut-Ankh-Amen (Carter)", "type": "Excavation report", "year": "1923"},
    ],
    "maddison_gdp_dataset": [
        {"title": "The World Economy: A Millennial Perspective (Maddison)", "type": "Economic dataset", "year": "2001"},
    ],
    "world_population_estimates": [
        {"title": "World Population Prospects (UN)", "type": "Statistical report"},
    ],
    "slave_trade_database": [
        {"title": "Trans-Atlantic Slave Trade Database", "type": "Historical database"},
    ],
    "griots_west_africa": [
        {"title": "Sundiata: An Epic of Old Mali (Niane)", "type": "Oral tradition transcription", "year": "1960"},
    ],
    "aboriginal_dreamtime": [
        {"title": "The Dreaming (Stanner, essay)", "type": "Anthropological essay", "year": "1953"},
    ],
    "homeric_oral_tradition": [
        {"title": "Iliad (Homer)", "type": "Epic poem"},
        {"title": "Odyssey (Homer)", "type": "Epic poem"},
    ],
    "common_law": [
        {"title": "Commentaries on the Laws of England (Blackstone)", "type": "Legal treatise", "year": "1765"},
    ],
    "world_bank": [
        {"title": "Bretton Woods Agreement", "type": "International agreement", "year": "1944"},
    ],
    "smithsonian_institution": [
        {"title": "Smithsonian Institution Act (1846)", "type": "Legal statute", "year": "1846"},
    ],
    "brown_v_board": [
        {"title": "Brown v. Board of Education opinion", "type": "Legal opinion", "year": "1954"},
    ],
    "germ_theory": [
        {"title": "Germ Theory and Its Applications to Medicine (Pasteur)", "type": "Scientific paper", "year": "1878"},
    ],
    "marie_curie": [
        {"title": "Recherches sur les substances radioactives (thesis)", "type": "Doctoral thesis", "year": "1903"},
    ],
    "moon_landing": [
        {"title": "Apollo 11 Mission Report", "type": "Technical report", "year": "1969"},
    ],
    "universal_declaration_human_rights": [
        {"title": "Universal Declaration of Human Rights", "type": "International declaration", "year": "1948"},
    ],
    "continent_africa": [
        {"title": "Things Fall Apart (Achebe)", "type": "Novel", "year": "1958"},
    ],
    "continent_asia": [
        {"title": "The Art of War (Sun Tzu)", "type": "Military treatise"},
    ],
    "continent_europe": [
        {"title": "The Iliad (Homer)", "type": "Epic poem"},
    ],
    "continent_americas": [
        {"title": "Popol Vuh", "type": "Mythological text"},
    ],
    "middle_east_region": [
        {"title": "Epic of Gilgamesh", "type": "Ancient epic"},
    ],
    "southeast_asia_region": [
        {"title": "Ramayana (Valmiki)", "type": "Epic poem"},
    ],
    "maya_civilization": [
        {"title": "Popol Vuh", "type": "Mythological text"},
        {"title": "Dresden Codex", "type": "Maya manuscript"},
    ],
    "nile_valley_civilization": [
        {"title": "Book of the Dead", "type": "Funerary text"},
        {"title": "Pyramid Texts", "type": "Funerary inscriptions"},
    ],
    "napoleonic_code": [
        {"title": "Code Napoléon (Code civil des Français)", "type": "Legal code", "year": "1804"},
    ],
    "roman_legions": [
        {"title": "De Bello Gallico (Caesar)", "type": "Military chronicle"},
    ],
    "pentagon_us_military": [
        {"title": "National Security Act of 1947", "type": "Legal statute", "year": "1947"},
    ],

    # ── Timeframes in divisionEnrichment — brief ──
    "tf_paleolithic": [
        {"title": "Paleolithic archaeological survey records", "type": "Archaeological report"},
    ],
    "tf_neolithic": [
        {"title": "Neolithic settlement excavation reports", "type": "Archaeological report"},
    ],
    "tf_bronze_age": [
        {"title": "Bronze Age metallurgical records", "type": "Archaeological report"},
    ],
    "tf_iron_age": [
        {"title": "Iron Age site documentation", "type": "Archaeological report"},
    ],
    "tf_axial_age": [
        {"title": "Jaspers, The Origin and Goal of History", "type": "Philosophical treatise", "year": "1949"},
    ],
    "tf_pax_romana": [
        {"title": "Res Gestae Divi Augusti", "type": "Imperial inscription"},
    ],
    "tf_dark_ages": [
        {"title": "Bede, Ecclesiastical History of the English People", "type": "Church history", "year": "731"},
    ],
    "tf_high_middle_ages": [
        {"title": "Summa Theologica (Aquinas)", "type": "Theological treatise"},
    ],
    "tf_late_middle_ages": [
        {"title": "The Decameron (Boccaccio)", "type": "Literary work", "year": "1353"},
    ],
    "tf_age_of_exploration": [
        {"title": "Journal of the First Voyage (Columbus)", "type": "Voyage journal", "year": "1493"},
    ],
    "tf_enlightenment_period": [
        {"title": "Encyclopédie (Diderot)", "type": "Encyclopedia", "year": "1751"},
    ],
    "tf_reformation_era": [
        {"title": "95 Theses (Luther)", "type": "Theological treatise", "year": "1517"},
    ],
    "tf_industrial_age": [
        {"title": "The Wealth of Nations (Smith)", "type": "Economic treatise", "year": "1776"},
    ],
    "tf_age_of_revolution": [
        {"title": "Declaration of the Rights of Man (1789)", "type": "Political declaration", "year": "1789"},
    ],
    "tf_world_wars_era": [
        {"title": "Treaty of Versailles (1919)", "type": "International treaty", "year": "1919"},
    ],
    "tf_cold_war_era": [
        {"title": "Long Telegram (Kennan)", "type": "Diplomatic dispatch", "year": "1946"},
    ],
    "tf_decolonization_era": [
        {"title": "The Wretched of the Earth (Fanon)", "type": "Political treatise", "year": "1961"},
    ],
    "tf_information_age": [
        {"title": "The Information (Gleick)", "type": "Science treatise", "year": "2011"},
    ],
    "tf_globalization_era": [
        {"title": "The World Is Flat (Friedman)", "type": "Economic analysis", "year": "2005"},
    ],
    "ottoman_empire": [
        {"title": "Kanunname of Suleiman", "type": "Legal code"},
    ],
    "leonardo_da_vinci": [
        {"title": "Codex Leicester", "type": "Scientific notebook"},
        {"title": "Treatise on Painting", "type": "Art treatise"},
    ],
}


def format_text_entry(t: dict) -> str:
    """Format a single text entry as TypeScript object literal."""
    # Escape single quotes for TS single-quoted strings
    title = t['title'].replace("'", "\\'")
    ttype = t['type'].replace("'", "\\'")
    parts = [f"title: '{title}'", f"type: '{ttype}'"]
    if "year" in t:
        parts.append(f"year: '{t['year']}'")
    if "slug" in t:
        parts.append(f"slug: '{t['slug']}'")
    return "{ " + ", ".join(parts) + " }"


def format_texts_array(texts: list[dict]) -> str:
    """Format a list of text entries as a TS array."""
    if len(texts) == 1:
        return "[" + format_text_entry(texts[0]) + "]"
    entries = ",\n      ".join(format_text_entry(t) for t in texts)
    return "[\n      " + entries + ",\n    ]"


def process_file(filepath: str) -> tuple[int, int]:
    """Process a single .ts file, replacing `texts: []` with enriched texts.
    Uses block-based approach: split by top-level entity boundaries.
    Returns (total_empty, enriched).
    """
    with open(filepath, "r") as f:
        content = f.read()

    original = content
    total_empty = 0
    enriched = 0

    # Split into entity blocks by the opening brace of each entity in the array
    # Each entity starts with `  {` (2-space indent) at line start
    blocks = re.split(r'(\n  \{)', content)

    result_parts = [blocks[0]]  # preamble

    i = 1
    while i < len(blocks):
        separator = blocks[i]       # "\n  {"
        block = blocks[i + 1] if i + 1 < len(blocks) else ""
        i += 2

        # Find the top-level slug (4-space indent)
        slug_m = re.search(r"^\s{4}slug:\s*'([^']+)'", block, re.MULTILINE)
        # Check if texts is empty
        has_empty = re.search(r'texts:\s*\[\]', block)

        if slug_m and has_empty:
            slug = slug_m.group(1)
            total_empty += 1
            if slug in TEXT_MAP:
                enriched += 1
                replacement = "texts: " + format_texts_array(TEXT_MAP[slug])
                block = re.sub(r'texts:\s*\[\]', replacement, block, count=1)

        result_parts.append(separator)
        result_parts.append(block)

    content = "".join(result_parts)

    if content != original:
        with open(filepath, "w") as f:
            f.write(content)

    return total_empty, enriched


def main():
    base = os.path.join(
        os.path.dirname(__file__), "..", "ui", "src", "data", "catalog"
    )
    files = [
        "prehistoric.ts",
        "classical.ts",
        "medieval.ts",
        "earlyModern.ts",
        "modern.ts",
        "contemporary.ts",
        "biblical.ts",
        "reformation.ts",
        "divisionEnrichment.ts",
    ]

    grand_empty = 0
    grand_enriched = 0

    for fname in files:
        fpath = os.path.join(base, fname)
        if not os.path.exists(fpath):
            print(f"  SKIP {fname} (not found)")
            continue
        empty, enriched = process_file(fpath)
        print(f"  {fname}: {enriched}/{empty} entities enriched")
        grand_empty += empty
        grand_enriched += enriched

    print(f"\nTotal: {grand_enriched}/{grand_empty} entities enriched with texts")


if __name__ == "__main__":
    main()
