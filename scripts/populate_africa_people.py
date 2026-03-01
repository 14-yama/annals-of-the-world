#!/usr/bin/env python3
"""
Populate people.json for all African countries that have empty thematic arrays.
Each country gets historically notable figures distributed across timeframes.

Usage:
    python3 scripts/populate_africa_people.py
"""

import json
import os
from datetime import datetime, timezone

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "geo-registry", "places", "countries",
)

TIMEFRAMES = ["910", "920", "930", "940", "950", "960"]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

LANG_SCRIPT = {
    "burundi": ("rn","Latn"), "cabo-verde": ("pt","Latn"), "cameroon": ("fr","Latn"),
    "central-african-republic": ("fr","Latn"), "chad": ("fr","Latn"),
    "comoros": ("ar","Arab"), "congo": ("fr","Latn"), "cote-divoire": ("fr","Latn"),
    "djibouti": ("fr","Latn"), "dr-congo": ("fr","Latn"),
    "equatorial-guinea": ("es","Latn"), "eritrea": ("ti","Ethi"),
    "eswatini": ("en","Latn"), "ethiopia": ("am","Ethi"),
    "gabon": ("fr","Latn"), "gambia": ("en","Latn"), "ghana": ("en","Latn"),
    "guinea": ("fr","Latn"), "guinea-bissau": ("pt","Latn"),
    "kenya": ("sw","Latn"), "lesotho": ("en","Latn"), "liberia": ("en","Latn"),
    "libya": ("ar","Arab"), "madagascar": ("mg","Latn"), "malawi": ("en","Latn"),
    "mali": ("fr","Latn"), "mauritania": ("ar","Arab"), "mauritius": ("en","Latn"),
    "morocco": ("ar","Arab"), "mozambique": ("pt","Latn"), "namibia": ("en","Latn"),
    "niger": ("ha","Latn"), "nigeria": ("en","Latn"), "rwanda": ("rw","Latn"),
    "sao-tome-and-principe": ("pt","Latn"), "senegal": ("fr","Latn"),
    "seychelles": ("en","Latn"), "sierra-leone": ("en","Latn"),
    "somalia": ("so","Latn"), "south-africa": ("en","Latn"),
    "south-sudan": ("en","Latn"), "sudan": ("ar","Arab"),
    "tanzania": ("sw","Latn"), "togo": ("fr","Latn"), "tunisia": ("ar","Arab"),
    "uganda": ("en","Latn"), "western-sahara": ("ar","Arab"),
    "zambia": ("en","Latn"), "zimbabwe": ("en","Latn"),
}

# Historical figures per country, keyed by timeframe
# Each entry: (slug, name, birthYear, deathYear, description)
# birthYear/deathYear can be None
PEOPLE = {
    "burundi": {
        "910": [("Ntare_Rushatsi", "Ntare Rushatsi", None, None, "Legendary founder of the Burundian monarchy (c. 17th century).")],
        "920": [("Ntare_IV", "Ntare IV", None, 1908, "Last powerful independent mwami (king) of Burundi.")],
        "930": [("Mwezi_Gisabo", "Mwezi IV Gisabo", None, 1908, "Long-reigning king who resisted German colonisation.")],
        "940": [("Mwambutsa_IV", "Mwambutsa IV", 1912, 1977, "King of Burundi during the transition from Belgian mandate to independence.")],
        "950": [("Louis_Rwagasore", "Prince Louis Rwagasore", 1932, 1961, "Independence hero and first elected prime minister, assassinated shortly after.")],
        "960": [("Pierre_Nkurunziza", "Pierre Nkurunziza", 1963, 2020, "President who ended the civil war but controversially extended his rule.")],
    },
    "cabo-verde": {
        "910": [("Early_Settlers_CV", "Early Portuguese Settlers", None, None, "First Portuguese and Genoese settlers who colonised the uninhabited islands from 1462.")],
        "920": [("Antonio_de_Noli", "António de Noli", 1419, 1497, "Genoese navigator credited with discovering Cabo Verde for Portugal.")],
        "930": [("Slave_Trade_Merchants_CV", "Ribeira Grande Slave Traders", None, None, "Merchants who made Santiago a hub of the transatlantic slave trade.")],
        "940": [("Eugenio_Tavares", "Eugénio Tavares", 1867, 1930, "Poet and journalist, pioneer of Cape Verdean Creole literature.")],
        "950": [("Amilcar_Cabral", "Amílcar Cabral", 1924, 1973, "Revolutionary leader of PAIGC, fought for independence of Cabo Verde and Guinea-Bissau.")],
        "960": [("Aristides_Pereira", "Aristides Pereira", 1923, 2011, "First President of independent Cabo Verde.")],
    },
    "cameroon": {
        "910": [("Sao_People_Leaders", "Sao Civilisation Leaders", None, None, "Leaders of the ancient Sao civilisation near Lake Chad.")],
        "920": [("Bamoun_Sultan_Njoya", "Sultan Ibrahim Njoya", 1860, 1933, "Bamoun sultan who invented the Shümom alphabet and reformed his kingdom.")],
        "930": [("Douala_Manga_Bell", "Rudolf Douala Manga Bell", 1873, 1914, "Douala chief executed by Germans for resisting land expropriation.")],
        "940": [("Charles_Atangana", "Charles Atangana", 1880, 1943, "Paramount chief who navigated German and French colonial administrations.")],
        "950": [("Ahmadou_Ahidjo", "Ahmadou Ahidjo", 1924, 1989, "First President of Cameroon; led the country to reunification.")],
        "960": [("Paul_Biya", "Paul Biya", 1933, None, "President of Cameroon since 1982, one of Africa's longest-serving leaders.")],
    },
    "central-african-republic": {
        "910": [("Gbaya_Founders", "Gbaya Community Founders", None, None, "Early Gbaya settlers in the Ubangi-Shari region.")],
        "920": [("Bangassou_Chief", "Sultan Bangassou", None, 1907, "Nzakara sultan who resisted French colonial expansion.")],
        "930": [("Karnu_Revolt_Leaders", "Kongo-Wara Revolt Leaders", None, None, "Leaders of the 1928–1931 anti-colonial Kongo-Wara rebellion.")],
        "940": [("Barthelemy_Boganda", "Barthélémy Boganda", 1910, 1959, "Founding father of the Central African Republic, died before independence.")],
        "950": [("David_Dacko", "David Dacko", 1930, 2003, "First President of the Central African Republic.")],
        "960": [("Jean_Bedel_Bokassa", "Jean-Bédel Bokassa", 1921, 1996, "Military ruler who declared himself emperor in 1977.")],
    },
    "chad": {
        "910": [("Sahelanthropus_tchadensis", "Sahelanthropus tchadensis Discovery", None, None, "Discovery in Chad of one of the oldest known hominid fossils (c. 7 million years).")],
        "920": [("Dunama_Dibbalemi", "Dunama Dibbalemi", None, 1259, "Mai (king) of the Kanem Empire who expanded its territory significantly.")],
        "930": [("Idris_Alooma", "Idris Alooma", 1564, 1596, "Sultan of Bornu who modernised the military and expanded trade.")],
        "940": [("Rabih_az_Zubayr", "Rabih az-Zubayr", 1842, 1900, "Sudanese warlord who conquered Bornu before French intervention.")],
        "950": [("Francois_Tombalbaye", "François Tombalbaye", 1918, 1975, "First President of Chad, overthrown in a coup.")],
        "960": [("Hissene_Habre", "Hissène Habré", 1942, 2021, "President convicted of crimes against humanity by an African court."),
                ("Idriss_Deby", "Idriss Déby", 1952, 2021, "President who ruled Chad for 30 years until killed in battle.")],
    },
    "comoros": {
        "910": [("Bantu_Settlers_KM", "Early Bantu-Malay Settlers", None, None, "First settlers combining Bantu, Malay-Indonesian, and Arab origins.")],
        "920": [("Shirazi_Sultans_KM", "Shirazi Sultans", None, None, "Muslim rulers who established sultanates on the Comoros islands.")],
        "930": [("Sultan_Said_Ali", "Sultan Saïd Ali", 1852, 1916, "Last sultan of Grande Comore who ceded sovereignty to France.")],
        "940": [("Colonial_Administrators_KM", "French Colonial Administrators", None, None, "French officials who governed the Comoros as part of Madagascar.")],
        "950": [("Ahmed_Abdallah", "Ahmed Abdallah", 1919, 1989, "First President of independent Comoros, later restored by mercenaries.")],
        "960": [("Bob_Denard", "Bob Denard", 1929, 2007, "French mercenary who intervened repeatedly in Comorian politics.")],
    },
    "congo": {
        "910": [("Kongo_Kings_CG", "Early Kongo and Teke Kings", None, None, "Rulers of the Kongo and Teke kingdoms in the Congo basin.")],
        "920": [("Makoko_Iloo_I", "Makoko Iloo I", None, None, "Teke king who signed a treaty with Pierre de Brazza.")],
        "930": [("Pierre_de_Brazza", "Pierre Savorgnan de Brazza", 1852, 1905, "Franco-Italian explorer who established French presence on the Congo River.")],
        "940": [("Andre_Matswa", "André Matswa", 1899, 1942, "Congolese political activist and founder of the Amicale movement.")],
        "950": [("Fulbert_Youlou", "Fulbert Youlou", 1917, 1972, "First President of the Republic of the Congo.")],
        "960": [("Denis_Sassou_Nguesso", "Denis Sassou Nguesso", 1943, None, "Long-serving president who has led Congo in two separate periods.")],
    },
    "cote-divoire": {
        "910": [("Senufo_Founders_CI", "Senufo Community Founders", None, None, "Early Senufo societies in northern Côte d'Ivoire.")],
        "920": [("Queen_Abla_Pokou", "Queen Abla Pokou", 1720, 1760, "Akan queen who led the Baoulé migration from the Gold Coast to Côte d'Ivoire.")],
        "930": [("Samori_Ture_CI", "Samori Ture", 1830, 1900, "Mandinka empire-builder who resisted French colonisation.")],
        "940": [("Gabriel_Dadié", "Bernard Dadié", 1916, 2019, "Writer and politician, major figure of Francophone African literature.")],
        "950": [("Felix_Houphouet_Boigny", "Félix Houphouët-Boigny", 1905, 1993, "Founding father and first President, known as the 'Sage of Africa'.")],
        "960": [("Alassane_Ouattara", "Alassane Ouattara", 1942, None, "President since 2011, who took power after a disputed election and civil conflict.")],
    },
    "djibouti": {
        "910": [("Afar_Issa_Ancestors", "Afar and Issa Ancestors", None, None, "Indigenous Afar and Issa Somali communities settling the region.")],
        "920": [("Ifat_Sultanate_Rulers", "Ifat Sultanate Rulers", None, None, "Muslim rulers of the Ifat and Adal states influencing the Djibouti coast.")],
        "930": [("Ahmed_Gragn_DJ", "Ahmed ibn Ibrahim al-Ghazi (Ahmed Gragn)", 1506, 1543, "Adal imam who led jihad against the Ethiopian Empire.")],
        "940": [("Léonce_Lagarde", "Léonce Lagarde", 1860, 1936, "First governor of French Somaliland (Djibouti).")],
        "950": [("Hassan_Gouled_Aptidon", "Hassan Gouled Aptidon", 1916, 2006, "First President of independent Djibouti.")],
        "960": [("Ismail_Omar_Guelleh", "Ismaïl Omar Guelleh", 1947, None, "President since 1999, overseeing Djibouti's rise as a strategic military base hub.")],
    },
    "dr-congo": {
        "910": [("Luba_Founders", "Founding Chiefs of the Luba Kingdom", None, None, "Legendary founders of the Luba kingdom in the Katanga region.")],
        "920": [("Msiri", "Msiri", 1830, 1891, "Yeke kingdom ruler of Katanga.")],
        "930": [("Leopold_II_DRC", "Leopold II of Belgium", 1835, 1909, "Belgian king whose brutal Congo Free State killed millions.")],
        "940": [("Patrice_Lumumba", "Patrice Lumumba", 1925, 1961, "First Prime Minister of independent Congo, assassinated shortly after.")],
        "950": [("Mobutu_Sese_Seko", "Mobutu Sese Seko", 1930, 1997, "Dictator who renamed the country Zaïre and ruled for 32 years.")],
        "960": [("Laurent_Desire_Kabila", "Laurent-Désiré Kabila", 1939, 2001, "Rebel leader who overthrew Mobutu and became president."),
                ("Denis_Mukwege", "Denis Mukwege", 1955, None, "Nobel Peace Prize laureate for treating victims of sexual violence in eastern Congo.")],
    },
    "equatorial-guinea": {
        "910": [("Bubi_Ancestors", "Bubi Indigenous Ancestors", None, None, "Indigenous Bubi people who first settled Bioko island.")],
        "920": [("Fang_Migrants_GQ", "Fang Migration Leaders", None, None, "Leaders of Fang migrations into the mainland Río Muni region.")],
        "930": [("Spanish_Colonists_GQ", "Spanish Colonial Governors", None, None, "Spanish administrators of Fernando Pó and Río Muni.")],
        "940": [("Acacio_Mañé", "Acacio Mañé Ela", 1920, 1969, "Early Equatoguinean independence activist.")],
        "950": [("Francisco_Macias_Nguema", "Francisco Macías Nguema", 1924, 1979, "First president, whose brutal dictatorship led to mass emigration.")],
        "960": [("Teodoro_Obiang", "Teodoro Obiang Nguema Mbasogo", 1942, None, "World's longest-serving president, in power since 1979.")],
    },
    "eritrea": {
        "910": [("Dmt_Rulers", "Kingdom of D'mt Rulers", None, None, "Rulers of the ancient kingdom of D'mt in Eritrea/northern Ethiopia (c. 980–400 BCE).")],
        "920": [("Aksumite_Kings_ER", "Aksumite Kings of the Eritrean Coast", None, None, "Aksumite rulers who controlled the Red Sea port of Adulis.")],
        "930": [("Bahr_Negash", "Bahr Negash Yeshaq", None, None, "Medieval Eritrean governor who governed the Red Sea coast under Ethiopian suzerainty.")],
        "940": [("Ras_Alula", "Ras Alula", 1827, 1897, "Ethiopian general from Eritrea who fought against Italian expansion.")],
        "950": [("Hamid_Idris_Awate", "Hamid Idris Awate", 1910, 1962, "Leader who launched the Eritrean armed struggle for independence in 1961.")],
        "960": [("Isaias_Afwerki", "Isaias Afwerki", 1946, None, "EPLF leader and sole President of Eritrea since independence in 1993.")],
    },
    "eswatini": {
        "910": [("Dlamini_I", "Dlamini I", None, None, "Semi-legendary founder of the Swazi royal Dlamini dynasty.")],
        "920": [("Ngwane_III", "Ngwane III", None, None, "King who led the Swazi from Mozambique into present-day Eswatini (c.1745).")],
        "930": [("Sobhuza_I", "Sobhuza I", None, 1836, "King who consolidated the Swazi nation during the Mfecane upheavals.")],
        "940": [("Mswati_II", "Mswati II", 1820, 1868, "Greatest Swazi warrior-king who expanded the kingdom's territory.")],
        "950": [("Sobhuza_II", "Sobhuza II", 1899, 1982, "World's longest-reigning monarch, overseeing independence from Britain in 1968.")],
        "960": [("Mswati_III", "Mswati III", 1968, None, "Current king of Eswatini, ruling as Africa's last absolute monarch.")],
    },
    "ethiopia": {
        "910": [("Lucy_Australopithecus", "Lucy (Australopithecus afarensis)", None, None, "Famous hominin fossil discovered in Hadar, Ethiopia, c. 3.2 million years old.")],
        "920": [("Ezana_of_Aksum", "King Ezana of Aksum", None, None, "Aksumite king who converted to Christianity and expanded the empire (c. 320–360 CE).")],
        "930": [("Lalibela", "King Lalibela", None, 1221, "Zagwe dynasty king who built the famous rock-hewn churches of Lalibela.")],
        "940": [("Menelik_II", "Emperor Menelik II", 1844, 1913, "Emperor who defeated Italy at the Battle of Adwa and modernised Ethiopia.")],
        "950": [("Haile_Selassie", "Emperor Haile Selassie I", 1892, 1975, "Last emperor of Ethiopia, Rastafari icon, dethroned by the Derg in 1974.")],
        "960": [("Abiy_Ahmed", "Abiy Ahmed", 1976, None, "Prime Minister and Nobel Peace laureate who pursued peace with Eritrea."),
                ("Mengistu_Haile_Mariam", "Mengistu Haile Mariam", 1937, None, "Derg military ruler whose Red Terror caused mass atrocities.")],
    },
    "gabon": {
        "910": [("Pygmy_Ancestors_GA", "Babongo Pygmy Ancestors", None, None, "Indigenous forest dwellers who were the first inhabitants of Gabon.")],
        "920": [("Mpongwe_Chiefs", "Mpongwe Coastal Chiefs", None, None, "Coastal chiefs who traded with European navigators.")],
        "930": [("Brazza_Gabon", "Pierre de Brazza in Gabon", 1852, 1905, "Explorer who established French authority along the Ogooué River.")],
        "940": [("Leon_Mba", "Léon Mba", 1902, 1967, "First President of Gabon.")],
        "950": [("Omar_Bongo", "Omar Bongo", 1935, 2009, "President for 42 years (1967–2009), one of Africa's longest-serving rulers.")],
        "960": [("Ali_Bongo", "Ali Bongo Ondimba", 1959, None, "Succeeded his father as president; ousted in a 2023 military coup.")],
    },
    "gambia": {
        "910": [("Senegambia_Ancestors", "Early Senegambian Settlements", None, None, "Iron Age communities along the River Gambia.")],
        "920": [("Kaabu_Empire_GM", "Rulers of the Kaabu Empire", None, None, "Mandinka empire that controlled the Gambia region.")],
        "930": [("Slave_Trade_Gambia", "James Island Slave Traders", None, None, "European and African traders at the Gambia River slave-trading posts.")],
        "940": [("Lamin_Bojang", "Lamin Bojang", None, None, "Mandinka marabout who resisted British expansion in The Gambia.")],
        "950": [("Dawda_Jawara", "Sir Dawda Jawara", 1924, 2019, "First President of independent Gambia.")],
        "960": [("Yahya_Jammeh", "Yahya Jammeh", 1965, None, "Military ruler (1994–2017) ousted after refusing to accept election defeat."),
                ("Adama_Barrow", "Adama Barrow", 1965, None, "President who won the 2016 election and ushered in democratic transition.")],
    },
    "ghana": {
        "910": [("Kintampo_Culture_Leaders", "Kintampo Culture Communities", None, None, "Neolithic communities who developed early agriculture in the Ghana forest zone.")],
        "920": [("Osei_Tutu_I", "Osei Tutu I", 1660, 1717, "Founder and first Asantehene (king) of the Ashanti Empire.")],
        "930": [("Yaa_Asantewaa", "Yaa Asantewaa", 1840, 1921, "Queen Mother who led the last Ashanti rebellion against the British in 1900.")],
        "940": [("J_E_Casely_Hayford", "J.E. Casely Hayford", 1866, 1930, "Lawyer, journalist, and Pan-African nationalist leader.")],
        "950": [("Kwame_Nkrumah", "Kwame Nkrumah", 1909, 1972, "First President of Ghana, leading figure of Pan-Africanism and African independence.")],
        "960": [("Jerry_Rawlings", "Jerry Rawlings", 1947, 2020, "Military ruler who later became a democratically elected president."),
                ("Kofi_Annan", "Kofi Annan", 1938, 2018, "Ghanaian diplomat, 7th Secretary-General of the United Nations, Nobel Peace laureate.")],
    },
    "guinea": {
        "910": [("Susu_Ancestors_GN", "Susu and Baga Ancestors", None, None, "Early Susu and Baga settlers in coastal Guinea.")],
        "920": [("Samori_Ture", "Samori Ture", 1830, 1900, "Mandinka empire-builder and military strategist who resisted French colonisation.")],
        "930": [("Fulbe_Jihad_Fouta_Djallon", "Fulbe Jihad Leaders of Fouta Djallon", None, None, "Islamic reformers who established the Imamate of Fouta Djallon (1727).")],
        "940": [("Alpha_Yaya_Diallo", "Alpha Yaya Diallo", 1850, 1912, "King of Labé who resisted French colonial rule.")],
        "950": [("Ahmed_Sekou_Toure", "Ahmed Sékou Touré", 1922, 1984, "First President who defiantly rejected de Gaulle's offer of community membership.")],
        "960": [("Lansana_Conte", "Lansana Conté", 1934, 2008, "Military ruler who became president and led Guinea for 24 years.")],
    },
    "guinea-bissau": {
        "910": [("Papel_Manjaco_Ancestors", "Papel and Manjaco Ancestors", None, None, "Indigenous Papel and Manjaco communities of coastal Guinea-Bissau.")],
        "920": [("Kaabu_Empire_GW", "Kaabu Empire Rulers", None, None, "Mandinka empire controlling Guinea-Bissau before Portuguese arrival.")],
        "930": [("Cacheu_Slave_Trade", "Cacheu Slave Trade", None, None, "Portuguese slave trading port at Cacheu, one of the oldest in West Africa.")],
        "940": [("Honório_Barreto", "Honório Pereira Barreto", 1813, 1859, "Governor of Portuguese Guinea and advocate for abolition.")],
        "950": [("Amilcar_Cabral_GW", "Amílcar Cabral", 1924, 1973, "PAIGC leader who fought for independence of Guinea-Bissau and Cabo Verde.")],
        "960": [("Nino_Vieira", "João Bernardo 'Nino' Vieira", 1939, 2009, "President of Guinea-Bissau in multiple terms, assassinated in 2009.")],
    },
    "kenya": {
        "910": [("Turkana_Boy", "Turkana Boy (Homo erectus)", None, None, "1.6-million-year-old hominin skeleton discovered at Lake Turkana.")],
        "920": [("Swahili_Merchants_KE", "Swahili Coast Merchants", None, None, "Swahili traders who built prosperous city-states along the Kenyan coast.")],
        "930": [("Mekatilili_wa_Menza", "Mekatilili wa Menza", 1860, 1924, "Giriama woman leader who resisted British forced labour policies.")],
        "940": [("Harry_Thuku", "Harry Thuku", 1895, 1970, "Kikuyu political activist and pioneer of Kenyan nationalism.")],
        "950": [("Jomo_Kenyatta", "Jomo Kenyatta", 1897, 1978, "Freedom fighter and first President of Kenya, 'Father of the Nation'.")],
        "960": [("Wangari_Maathai", "Wangari Maathai", 1940, 2011, "Environmental activist and Nobel Peace Prize laureate, founder of the Green Belt Movement."),
                ("Daniel_arap_Moi", "Daniel arap Moi", 1924, 2020, "Second president who ruled Kenya for 24 years.")],
    },
    "lesotho": {
        "910": [("San_Rock_Artists_LS", "San Rock Art Communities", None, None, "San hunter-gatherer communities who created rock art in the Maluti Mountains.")],
        "920": [("Sotho_Ancestors_LS", "Early Sotho Settlers", None, None, "Bantu-speaking Sotho communities settling in the highlands.")],
        "930": [("Moshoeshoe_I", "Moshoeshoe I", 1786, 1870, "Founder and first king of the Basotho nation who unified the people during the Mfecane.")],
        "940": [("Lerotholi", "Paramount Chief Lerotholi", 1836, 1905, "Chief who navigated the transition to British protectorate status.")],
        "950": [("Moshoeshoe_II", "Moshoeshoe II", 1938, 1996, "King during independence and the turbulent early decades of the kingdom.")],
        "960": [("Letsie_III", "Letsie III", 1963, None, "Current king of Lesotho, serving as constitutional monarch.")],
    },
    "liberia": {
        "910": [("Dei_and_Bassa_Ancestors", "Dei and Bassa Ancestors", None, None, "Indigenous communities inhabiting Liberia before Americo-Liberian settlement.")],
        "920": [("Americo_Liberian_Settlers", "Americo-Liberian Settlers", None, None, "Freed American slaves who established the colony of Liberia in 1822.")],
        "930": [("Joseph_Jenkins_Roberts", "Joseph Jenkins Roberts", 1809, 1876, "First and seventh President of Liberia, Americo-Liberian leader.")],
        "940": [("William_Tubman", "William Tubman", 1895, 1971, "Long-serving president who promoted national unification policies.")],
        "950": [("Samuel_Doe", "Samuel Doe", 1951, 1990, "First indigenous head of state, overthrown and killed during the civil war.")],
        "960": [("Ellen_Johnson_Sirleaf", "Ellen Johnson Sirleaf", 1938, None, "Africa's first elected female head of state, Nobel Peace Prize laureate."),
                ("Charles_Taylor", "Charles Taylor", 1948, None, "Warlord and president convicted of war crimes by an international court.")],
    },
    "libya": {
        "910": [("Garamantes", "Garamantes Leaders", None, None, "Rulers of the ancient Garamantian kingdom in the Fezzan (c. 500 BCE–700 CE).")],
        "920": [("Greek_Colonists_Cyrene", "Greek Colonists of Cyrene", None, None, "Founders of the Greek colony of Cyrene in eastern Libya (c. 631 BCE).")],
        "930": [("Ahmad_al_Qaramanli", "Ahmad al-Qaramanli", 1686, 1745, "Founder of the Qaramanli dynasty that ruled Ottoman Tripolitania.")],
        "940": [("Omar_Mukhtar", "Omar al-Mukhtar", 1858, 1931, "National hero who led resistance against Italian colonisation.")],
        "950": [("King_Idris_I", "King Idris I", 1889, 1983, "First and only king of independent Libya (1951–1969).")],
        "960": [("Muammar_Gaddafi", "Muammar Gaddafi", 1942, 2011, "Revolutionary leader who ruled Libya for 42 years until the 2011 uprising.")],
    },
    "madagascar": {
        "910": [("Austronesian_Settlers_MG", "Austronesian Settlers", None, None, "Malay-Indonesian seafarers who first settled Madagascar (c. 350–550 CE).")],
        "920": [("Andriamanelo", "Andriamanelo", None, None, "Merina king who began the political unification of the central highlands.")],
        "930": [("Radama_I", "Radama I", 1793, 1828, "Merina king who modernised Madagascar and expanded the kingdom.")],
        "940": [("Ranavalona_I", "Ranavalona I", 1778, 1861, "Queen who fiercely resisted European influence and Christianity.")],
        "950": [("Tsiranana", "Philibert Tsiranana", 1912, 1978, "First President of the Malagasy Republic after independence from France.")],
        "960": [("Didier_Ratsiraka", "Didier Ratsiraka", 1936, 2021, "Military leader and president who pursued socialist and then liberal policies.")],
    },
    "malawi": {
        "910": [("Bantu_Settlers_MW", "Early Bantu Settlers", None, None, "Bantu-speaking peoples who settled around Lake Malawi.")],
        "920": [("Maravi_Confederacy_Leaders", "Maravi Confederacy Leaders", None, None, "Rulers of the Maravi (Chewa) confederacy that gave Malawi its name.")],
        "930": [("David_Livingstone_MW", "David Livingstone", 1813, 1873, "Scottish explorer who documented the slave trade around Lake Malawi.")],
        "940": [("John_Chilembwe", "John Chilembwe", 1871, 1915, "Pastor who led a 1915 uprising against colonial injustice in Nyasaland.")],
        "950": [("Hastings_Kamuzu_Banda", "Hastings Kamuzu Banda", 1898, 1997, "First President who ruled Malawi as a one-party state for three decades.")],
        "960": [("Bingu_wa_Mutharika", "Bingu wa Mutharika", 1934, 2012, "President who initially reformed governance but later turned authoritarian.")],
    },
    "mali": {
        "910": [("Soundjata_Keita", "Soundjata Keïta", 1217, 1255, "Founder of the Mali Empire after the Battle of Kirina (1235).")],
        "920": [("Mansa_Musa", "Mansa Musa", 1280, 1337, "Emperor of Mali famed for his lavish pilgrimage to Mecca; possibly history's richest person.")],
        "930": [("Askia_Muhammad_I", "Askia Muhammad I", 1443, 1538, "Emperor of the Songhai Empire who expanded trans-Saharan trade and Islamic scholarship.")],
        "940": [("El_Hadj_Umar_Tall", "El Hadj Umar Tall", 1794, 1864, "Toucouleur jihad leader who founded the Toucouleur Empire.")],
        "950": [("Modibo_Keita", "Modibo Keïta", 1915, 1977, "First President of Mali, socialist pan-Africanist.")],
        "960": [("Alpha_Oumar_Konare", "Alpha Oumar Konaré", 1946, None, "First democratically elected president after 1991 revolution."),
                ("Amadou_Hampate_Ba", "Amadou Hampâté Bâ", 1901, 1991, "Writer and ethnologist who preserved West African oral traditions.")],
    },
    "mauritania": {
        "910": [("Berber_Sanhaja_MR", "Sanhaja Berber Leaders", None, None, "Nomadic Sanhaja Berber tribes of western Sahara.")],
        "920": [("Almoravid_Founders", "Almoravid Movement Founders", None, None, "Launched the Almoravid movement from Mauritania that conquered the Maghreb and Spain.")],
        "930": [("Nasir_al_Din_MR", "Nāṣir al-Dīn", None, 1674, "Marabout leader of the Char Bouba war, seeking to impose Islamic law.")],
        "940": [("Xavier_Coppolani", "Xavier Coppolani", 1866, 1905, "French colonial administrator who 'pacified' Mauritania.")],
        "950": [("Mokhtar_Ould_Daddah", "Mokhtar Ould Daddah", 1924, 2003, "First President of independent Mauritania.")],
        "960": [("Mohamed_Ould_Abdel_Aziz", "Mohamed Ould Abdel Aziz", 1956, None, "Military coup leader and president (2008–2019).")],
    },
    "mauritius": {
        "910": [("Arab_Navigators_MU", "Arab and Malay Navigators", None, None, "Early Arab and Malay sailors who knew of the uninhabited Mascarene islands.")],
        "920": [("Dutch_Colonists_MU", "Dutch Colonists", None, None, "First European colonists who named the island after Prince Maurits (1598–1710).")],
        "930": [("French_Colonists_MU", "French Isle de France Colonists", None, None, "French planters who developed sugar plantations using enslaved labour.")],
        "940": [("Remy_Ollier", "Rémy Ollier", 1816, 1845, "Early Mauritian journalist and advocate for civil rights of people of colour.")],
        "950": [("Seewoosagur_Ramgoolam", "Sir Seewoosagur Ramgoolam", 1900, 1985, "Father of the Nation and first Prime Minister after independence (1968).")],
        "960": [("Anerood_Jugnauth", "Sir Anerood Jugnauth", 1930, 2021, "Long-serving leader who transformed Mauritius into an economic success story.")],
    },
    "morocco": {
        "910": [("Berber_Rock_Art_MA", "Berber Rock Art Communities", None, None, "Prehistoric communities who created rock carvings in the Atlas Mountains.")],
        "920": [("Idris_I", "Idris I", 745, 791, "Founder of the Idrisid dynasty and the city of Fes, first Moroccan Muslim dynasty.")],
        "930": [("Ahmad_al_Mansur", "Ahmad al-Mansur", 1549, 1603, "Saadian sultan who defeated Portugal at Battle of Alcácer Quibir and conquered Songhai.")],
        "940": [("Abdelkrim_El_Khattabi", "Abdelkrim el-Khattabi", 1882, 1963, "Rif Republic leader who fought Spanish and French colonisers.")],
        "950": [("Mohammed_V", "Mohammed V", 1909, 1961, "Sultan and later king who led Morocco to independence from French protectorate.")],
        "960": [("Hassan_II", "Hassan II", 1929, 1999, "King who consolidated royal power through the Years of Lead."),
                ("Mohammed_VI", "Mohammed VI", 1963, None, "Current king who has pursued modernisation and reconciliation reforms.")],
    },
    "mozambique": {
        "910": [("Bantu_Settlers_MZ", "Early Bantu Settlers", None, None, "Bantu-speaking communities settling the Mozambican coast.")],
        "920": [("Swahili_Traders_MZ", "Swahili and Arab Traders", None, None, "Traders who established coastal settlements like Sofala and Ilha de Moçambique.")],
        "930": [("Mutapa_Empire_Rulers", "Mutapa Empire Rulers", None, None, "Rulers of the Mutapa (Monomotapa) gold-trading empire.")],
        "940": [("Gungunhana", "Gungunhana", 1850, 1906, "Last ruler of the Gaza Empire who resisted Portuguese colonisation.")],
        "950": [("Eduardo_Mondlane", "Eduardo Mondlane", 1920, 1969, "Founder of FRELIMO and leader of the independence struggle, assassinated in 1969."),
                ("Samora_Machel", "Samora Machel", 1933, 1986, "First President of Mozambique who led FRELIMO to victory.")],
        "960": [("Joaquim_Chissano", "Joaquim Chissano", 1939, None, "President who oversaw the end of the civil war and democratic transition.")],
    },
    "namibia": {
        "910": [("San_Ancestors_NA", "San Ancestors of Namibia", None, None, "San hunter-gatherers, among the oldest continuous populations in the world.")],
        "920": [("Herero_Nama_Chiefs", "Early Herero and Nama Chiefs", None, None, "Pastoralist leaders who migrated into Namibia.")],
        "930": [("Hendrik_Witbooi", "Hendrik Witbooi", 1830, 1905, "Nama chief and guerrilla leader who resisted German colonisation.")],
        "940": [("Samuel_Maharero", "Samuel Maharero", 1856, 1923, "Herero paramount chief who led the 1904 uprising against German genocide.")],
        "950": [("Andimba_Toivo_ya_Toivo", "Andimba Toivo ya Toivo", 1924, 2017, "SWAPO co-founder and anti-apartheid freedom fighter.")],
        "960": [("Sam_Nujoma", "Sam Nujoma", 1929, None, "SWAPO leader and first President of independent Namibia (1990)."),
                ("Hage_Geingob", "Hage Geingob", 1941, 2024, "Third president who championed economic development.")],
    },
    "niger": {
        "910": [("Neolithic_Saharan_NE", "Neolithic Saharan Communities", None, None, "Communities that thrived when the Sahara was green, leaving rock art at Aïr Mountains.")],
        "920": [("Songhai_Emperor_NE", "Songhai Rulers of Niger Region", None, None, "Songhai Empire's extension into western Niger.")],
        "930": [("Bornu_Influence_NE", "Bornu Empire Influence in Niger", None, None, "Kanem-Bornu Empire's political influence in eastern Niger.")],
        "940": [("Sarraounia_Mangou", "Sarraounia Mangou", None, None, "Queen of the Azna who resisted the French Voulet-Chanoine expedition in 1899.")],
        "950": [("Hamani_Diori", "Hamani Diori", 1916, 1989, "First President of independent Niger.")],
        "960": [("Mamadou_Tandja", "Mamadou Tandja", 1938, 2020, "President who was overthrown for attempting to extend his term."),
                ("Mahamadou_Issoufou", "Mahamadou Issoufou", 1952, None, "President who oversaw Niger's first peaceful democratic transfer of power.")],
    },
    "nigeria": {
        "910": [("Nok_Culture_Artisans", "Nok Culture Artisans", None, None, "Creators of Africa's earliest known terracotta sculptures (c. 1500 BCE–500 CE).")],
        "920": [("Oba_Ewuare", "Oba Ewuare the Great", None, None, "15th-century Oba of Benin who expanded the Benin Empire.")],
        "930": [("Usman_dan_Fodio", "Usman dan Fodio", 1754, 1817, "Islamic scholar who led the Fulani jihad and founded the Sokoto Caliphate.")],
        "940": [("Frederick_Lugard", "Frederick Lugard", 1858, 1945, "British administrator who amalgamated northern and southern Nigeria in 1914.")],
        "950": [("Nnamdi_Azikiwe", "Nnamdi Azikiwe", 1904, 1996, "First President of Nigeria and key independence figure."),
                ("Obafemi_Awolowo", "Obafemi Awolowo", 1909, 1987, "Yoruba leader and premier of Western Nigeria.")],
        "960": [("Chinua_Achebe", "Chinua Achebe", 1930, 2013, "Author of Things Fall Apart, 'father of African literature'."),
                ("Wole_Soyinka", "Wole Soyinka", 1934, None, "Playwright and Africa's first Nobel Prize laureate in Literature (1986).")],
    },
    "rwanda": {
        "910": [("Twa_Ancestors_RW", "Twa (Batwa) Ancestors", None, None, "Indigenous forest-dwelling Twa people, earliest inhabitants of Rwanda.")],
        "920": [("Ruganzu_Ndori", "Ruganzu II Ndori", None, None, "Legendary king who consolidated the Rwandan kingdom (c. 17th century).")],
        "930": [("Kigeli_IV_Rwabugiri", "Kigeli IV Rwabugiri", None, 1895, "Powerful king who expanded and centralised the Rwandan state.")],
        "940": [("Musinga", "Yuhi V Musinga", 1883, 1944, "King deposed by Belgian colonisers for resisting missionary influence.")],
        "950": [("Gregoire_Kayibanda", "Grégoire Kayibanda", 1924, 1976, "Leader of the Hutu revolution and first President of Rwanda.")],
        "960": [("Paul_Kagame", "Paul Kagame", 1957, None, "RPF leader who ended the 1994 genocide and has led Rwanda since 2000.")],
    },
    "sao-tome-and-principe": {
        "910": [("Portuguese_Discovery_STP", "Portuguese Discovery (1470s)", None, None, "Portuguese navigators discovered the uninhabited islands around 1470.")],
        "920": [("Sugar_Plantation_STP", "Sugar Plantation Economy", None, None, "Development of slave-based sugar plantations in the 16th century.")],
        "930": [("Amador_Revolt_STP", "Amador (Rei Amador)", None, 1596, "Enslaved leader who led a major slave revolt on São Tomé in 1595.")],
        "940": [("Cocoa_Plantation_STP", "Roça System Owners", None, None, "Portuguese plantation owners during the cocoa boom era.")],
        "950": [("Manuel_Pinto_da_Costa", "Manuel Pinto da Costa", 1937, None, "First President of independent São Tomé and Príncipe.")],
        "960": [("Fradique_de_Menezes", "Fradique de Menezes", 1942, None, "President who navigated the country's transition to multiparty democracy.")],
    },
    "senegal": {
        "910": [("Serer_Ancestors_SN", "Serer Ancestors", None, None, "Indigenous Serer communities and megaliths at Sine Ngayène.")],
        "920": [("Jolof_Empire_Rulers", "Jolof Empire Rulers", None, None, "Rulers of the Jolof Empire that united Wolof states.")],
        "930": [("Lat_Dior_Diop", "Lat Dior Diop", 1842, 1886, "Damel (king) of Cayor who resisted French expansion.")],
        "940": [("Blaise_Diagne", "Blaise Diagne", 1872, 1934, "First Black African elected to the French National Assembly.")],
        "950": [("Leopold_Sedar_Senghor", "Léopold Sédar Senghor", 1906, 2001, "Poet-president, Négritude co-founder, and first President of Senegal.")],
        "960": [("Abdoulaye_Wade", "Abdoulaye Wade", 1926, None, "President whose election in 2000 marked Senegal's first democratic alternance."),
                ("Youssou_NDour", "Youssou N'Dour", 1959, None, "World-renowned musician and cultural ambassador of Senegalese music.")],
    },
    "seychelles": {
        "910": [("Arab_Explorers_SC", "Arab Explorers", None, None, "Early Arab navigators who charted the Seychelles islands.")],
        "920": [("French_Colonists_SC", "French Colonists", None, None, "French settlers who established plantations on the islands from 1770.")],
        "930": [("British_Period_SC", "British Colonial Period", None, None, "British administrators who governed Seychelles from 1811.")],
        "940": [("Pierre_Louis_Poiret", "Pierre-Louis Poiret", None, None, "French intendant who governed the early colonial Seychelles.")],
        "950": [("James_Mancham", "James Mancham", 1939, 2017, "First President of independent Seychelles, ousted in a 1977 coup.")],
        "960": [("France_Albert_Rene", "France-Albert René", 1935, 2019, "Socialist president who ruled for 27 years after a coup.")],
    },
    "sierra-leone": {
        "910": [("Temne_Mende_Ancestors", "Temne and Mende Ancestors", None, None, "Indigenous Temne and Mende communities of Sierra Leone.")],
        "920": [("Province_of_Freedom", "Province of Freedom Settlers", None, None, "Freed Black Loyalists and 'Black Poor' who settled Freetown in 1787.")],
        "930": [("Bai_Bureh", "Bai Bureh", 1840, 1908, "Temne chief who led the Hut Tax War resistance against the British in 1898.")],
        "940": [("Sierra_Leone_Creoles", "Krio (Creole) Community Leaders", None, None, "Prominent Krio professionals and administrators in colonial Freetown.")],
        "950": [("Siaka_Stevens", "Siaka Stevens", 1905, 1988, "First executive president who established one-party rule.")],
        "960": [("Ahmad_Tejan_Kabbah", "Ahmad Tejan Kabbah", 1932, 2014, "President during the brutal civil war (1991–2002) who oversaw its end.")],
    },
    "somalia": {
        "910": [("Land_of_Punt", "Rulers of the Land of Punt", None, None, "Ancient civilisation on the Horn of Africa trading with Egypt.")],
        "920": [("Ajuran_Sultanate_Rulers", "Ajuran Sultanate Rulers", None, None, "Rulers of the Ajuran hydraulic empire of southern Somalia.")],
        "930": [("Ahmed_Gurey_SO", "Ahmed ibn Ibrahim (Ahmed Gurey)", 1506, 1543, "Adal imam who launched a celebrated campaign against Ethiopia.")],
        "940": [("Sayyid_Mohamed_Hassan", "Sayyid Mohamed Abdullah Hassan", 1856, 1920, "The 'Mad Mullah' who led Dervish resistance against British, Italian, and Ethiopian forces.")],
        "950": [("Aden_Abdulle_Osman", "Aden Abdulle Osman", 1908, 2007, "First President of the Somali Republic.")],
        "960": [("Siad_Barre", "Siad Barre", 1919, 1995, "Military dictator whose fall led to state collapse and civil war.")],
    },
    "south-africa": {
        "910": [("San_Ancestors_ZA", "San First Peoples", None, None, "San hunter-gatherers, among the world's oldest continuing peoples.")],
        "920": [("Shaka_Zulu", "Shaka Zulu", 1787, 1828, "Founder of the Zulu Kingdom who revolutionised warfare in southern Africa.")],
        "930": [("Paul_Kruger", "Paul Kruger", 1825, 1904, "President of the South African Republic (Transvaal) during the Boer Wars.")],
        "940": [("Mahatma_Gandhi_ZA", "Mahatma Gandhi in South Africa", 1869, 1948, "Developed satyagraha resistance while living in South Africa (1893–1914).")],
        "950": [("Nelson_Mandela", "Nelson Mandela", 1918, 2013, "Anti-apartheid leader, prisoner for 27 years, first Black president of South Africa."),
                ("Desmond_Tutu", "Desmond Tutu", 1931, 2021, "Archbishop and Nobel Peace laureate who championed the anti-apartheid movement.")],
        "960": [("Thabo_Mbeki", "Thabo Mbeki", 1942, None, "Second president who promoted the African Renaissance and NEPAD."),
                ("Miriam_Makeba", "Miriam Makeba", 1932, 2008, "Singer and civil rights activist known as 'Mama Africa'.")],
    },
    "south-sudan": {
        "910": [("Nilotic_Ancestors_SS", "Nilotic Ancestors", None, None, "Dinka, Nuer, and Shilluk peoples settled in the White Nile region.")],
        "920": [("Shilluk_Kingdom", "Shilluk Kingdom Rulers", None, None, "Rulers of the Shilluk (Collo) kingdom on the White Nile.")],
        "930": [("Slave_Raids_SS", "Slave Raid Resistance Leaders", None, None, "Nilotic leaders who resisted Turco-Egyptian and Mahdist slave raids.")],
        "940": [("Anyanya_I_Leaders", "Anyanya I Rebellion Leaders", None, None, "Leaders of the first Sudanese civil war (1955–1972).")],
        "950": [("John_Garang", "John Garang de Mabior", 1945, 2005, "SPLA leader who fought for South Sudanese self-determination.")],
        "960": [("Salva_Kiir_Mayardit", "Salva Kiir Mayardit", 1951, None, "First President of South Sudan since independence in 2011.")],
    },
    "sudan": {
        "910": [("Kerma_Rulers", "Kingdom of Kerma Rulers", None, None, "Rulers of the powerful Nubian kingdom of Kerma (c. 2500–1500 BCE).")],
        "920": [("Meroë_Queens", "Kandakes (Queens) of Meroë", None, None, "Female rulers of the Meroitic kingdom who governed and warred with Rome.")],
        "930": [("Funj_Sultanate_Founders", "Funj Sultanate Founders", None, None, "Founders of the Sennar kingdom that Islamised the Nilotic Sudan.")],
        "940": [("Muhammad_Ahmad_Mahdi", "Muhammad Ahmad (the Mahdi)", 1844, 1885, "Self-proclaimed Mahdi who led jihad against Anglo-Egyptian rule.")],
        "950": [("Ismail_al_Azhari", "Ismail al-Azhari", 1900, 1969, "First Prime Minister and later President of independent Sudan.")],
        "960": [("Omar_al_Bashir", "Omar al-Bashir", 1944, None, "Military dictator indicted by the ICC for genocide in Darfur, ousted in 2019.")],
    },
    "tanzania": {
        "910": [("Olduvai_Gorge_Hominids", "Olduvai Gorge Hominids", None, None, "Homo habilis and early tool-making discoveries at Olduvai Gorge.")],
        "920": [("Kilwa_Sultanate_Rulers", "Kilwa Sultanate Rulers", None, None, "Rulers of the wealthy Swahili trading state of Kilwa Kisiwani.")],
        "930": [("Mirambo", "Mirambo", 1840, 1884, "Nyamwezi warlord who built a powerful trading empire in western Tanzania.")],
        "940": [("Abushiri_bin_Salim", "Abushiri ibn Salim", 1845, 1889, "Arab-Swahili leader of the Abushiri Revolt against German colonisation.")],
        "950": [("Julius_Nyerere", "Julius Nyerere", 1922, 1999, "Father of the Nation, first President, architect of Ujamaa socialism.")],
        "960": [("Jakaya_Kikwete", "Jakaya Kikwete", 1950, None, "President who pursued economic growth and regional diplomacy."),
                ("Benjamin_Mkapa", "Benjamin Mkapa", 1938, 2020, "President who implemented economic liberalisation reforms.")],
    },
    "togo": {
        "910": [("Ewe_Kabye_Ancestors", "Ewe and Kabyé Ancestors", None, None, "Early Ewe and Kabyé communities settling in present-day Togo.")],
        "920": [("Slave_Coast_TG", "Slave Coast Trading Period", None, None, "Togo as part of the 'Slave Coast' during the transatlantic slave trade.")],
        "930": [("German_Togoland", "German Togoland Administration", None, None, "German colonial rulers who governed Togoland (1884–1914).")],
        "940": [("Sylvanus_Olympio_Early", "Sylvanus Olympio (early career)", 1902, 1963, "Educated leader who campaigned for Togolese independence within French Africa.")],
        "950": [("Sylvanus_Olympio", "Sylvanus Olympio", 1902, 1963, "First President of Togo, assassinated in Africa's first military coup in 1963.")],
        "960": [("Gnassingbe_Eyadema", "Gnassingbé Eyadéma", 1935, 2005, "Military dictator who ruled Togo for 38 years."),
                ("Faure_Gnassingbe", "Faure Gnassingbé", 1966, None, "President since 2005, succeeding his father in a dynastic transition.")],
    },
    "tunisia": {
        "910": [("Carthage_Founders", "Founders of Carthage", None, None, "Phoenician colonists who founded Carthage (c. 814 BCE).")],
        "920": [("Hannibal_Barca", "Hannibal Barca", -247, -183, "Carthaginian general who crossed the Alps to invade Rome.")],
        "930": [("Hafsid_Dynasty_Rulers", "Hafsid Dynasty Rulers", None, None, "Rulers of the Hafsid dynasty centred in Tunis (1229–1574).")],
        "940": [("Khayr_al_Din_Barbarossa", "Khayr al-Din Barbarossa", 1478, 1546, "Ottoman corsair who made Tunisia part of the Ottoman Empire.")],
        "950": [("Habib_Bourguiba", "Habib Bourguiba", 1903, 2000, "Father of independence and first President of Tunisia, moderniser and seculariser.")],
        "960": [("Zine_El_Abidine_Ben_Ali", "Zine El Abidine Ben Ali", 1936, 2019, "President ousted by the 2011 Jasmine Revolution, spark of the Arab Spring."),
                ("Mohamed_Bouazizi", "Mohamed Bouazizi", 1984, 2011, "Street vendor whose self-immolation triggered the Tunisian revolution and Arab Spring.")],
    },
    "uganda": {
        "910": [("Bunyoro_Founders", "Bunyoro-Kitara Kingdom Founders", None, None, "Founders of the Bunyoro-Kitara kingdom, one of East Africa's oldest states.")],
        "920": [("Buganda_Kabakas", "Early Buganda Kabakas", None, None, "Founding rulers (kabakas) of the Buganda kingdom.")],
        "930": [("Kabaka_Mutesa_I", "Kabaka Mutesa I", 1837, 1884, "Buganda king who welcomed European explorers and missionaries.")],
        "940": [("Kabaka_Mwanga_II", "Kabaka Mwanga II", 1868, 1903, "Buganda king who fought British expansion and was exiled.")],
        "950": [("Milton_Obote", "Milton Obote", 1925, 2005, "First Prime Minister and later President of Uganda."),
                ("Idi_Amin", "Idi Amin", 1925, 2003, "Military dictator whose brutal rule (1971–1979) claimed hundreds of thousands of lives.")],
        "960": [("Yoweri_Museveni", "Yoweri Museveni", 1944, None, "NRM leader and President of Uganda since 1986.")],
    },
    "western-sahara": {
        "910": [("Saharan_Nomads_EH", "Saharan Nomadic Tribes", None, None, "Berber and Arab-Berber nomadic communities of the western Sahara.")],
        "920": [("Sanhaja_Tribes_EH", "Sanhaja Confederacy", None, None, "Sanhaja Berber tribal confederacy that controlled western Saharan trade routes.")],
        "930": [("Ma_al_Aynayn", "Ma al-'Aynayn", 1831, 1910, "Sahrawi religious leader who resisted French and Spanish colonisation.")],
        "940": [("Spanish_Sahara_Admin", "Spanish Sahara Administrators", None, None, "Spanish colonial officials governing the territory.")],
        "950": [("El_Ouali_Mustapha_Sayed", "El-Ouali Mustapha Sayed", 1947, 1976, "Founder of the Polisario Front and leader of the Sahrawi independence movement.")],
        "960": [("Mohamed_Abdelaziz", "Mohamed Abdelaziz", 1947, 2016, "President of the Sahrawi Arab Democratic Republic for 40 years.")],
    },
    "zambia": {
        "910": [("Bantu_Settlers_ZM", "Early Bantu Settlers", None, None, "Bantu-speaking peoples who settled in the Zambian region.")],
        "920": [("Lozi_Kingdom_Rulers", "Lozi Kingdom Rulers", None, None, "Rulers of the Barotseland (Lozi) kingdom in western Zambia.")],
        "930": [("David_Livingstone_ZM", "David Livingstone at Victoria Falls", 1813, 1873, "Explorer who 'discovered' Mosi-oa-Tunya (Victoria Falls) for the European world in 1855.")],
        "940": [("Northern_Rhodesia_Labour", "Northern Rhodesian Mine Workers", None, None, "African mineworkers in the Copperbelt who organised early labour strikes.")],
        "950": [("Kenneth_Kaunda", "Kenneth Kaunda", 1924, 2021, "Founding father and first President of Zambia, led the independence movement.")],
        "960": [("Frederick_Chiluba", "Frederick Chiluba", 1943, 2011, "Trade unionist who became president and introduced multiparty democracy."),
                ("Levy_Mwanawasa", "Levy Mwanawasa", 1948, 2008, "President known for anti-corruption efforts.")],
    },
    "zimbabwe": {
        "910": [("Great_Zimbabwe_Builders", "Great Zimbabwe Builders", None, None, "Creators of the Great Zimbabwe stone city, largest ancient structure in sub-Saharan Africa.")],
        "920": [("Mutapa_Rulers_ZW", "Mutapa Empire Rulers", None, None, "Rulers of the Mutapa kingdom that succeeded Great Zimbabwe.")],
        "930": [("Mzilikazi", "Mzilikazi", 1790, 1868, "Founder of the Ndebele kingdom in present-day Zimbabwe.")],
        "940": [("Lobengula", "Lobengula", 1845, 1894, "Last king of the Ndebele, tricked into the Rudd Concession by Cecil Rhodes.")],
        "950": [("Robert_Mugabe", "Robert Mugabe", 1924, 2019, "Independence leader and first prime minister/president, later authoritarian ruler."),
                ("Joshua_Nkomo", "Joshua Nkomo", 1917, 1999, "ZAPU leader and 'Father Zimbabwe', co-leader of the liberation struggle.")],
        "960": [("Morgan_Tsvangirai", "Morgan Tsvangirai", 1952, 2018, "MDC opposition leader who challenged Mugabe's rule."),
                ("Emmerson_Mnangagwa", "Emmerson Mnangagwa", 1942, None, "President since 2017 after a military-backed transition.")],
    },
}


def write_people_file(country_slug, people_by_tf):
    """Write people.json for a country."""
    lang, script = LANG_SCRIPT.get(country_slug, ("en", "Latn"))

    thematic = {}
    for tf in TIMEFRAMES:
        entries = []
        for item in people_by_tf.get(tf, []):
            if isinstance(item, tuple):
                slug, name, by, dy, desc = item
                entry = {
                    "slug": slug, "name": name,
                    "label": "Person", "status": "PROPOSED",
                    "lang": lang, "script": script,
                    "description": desc,
                }
                if by is not None:
                    entry["birthYear"] = by
                if dy is not None:
                    entry["deathYear"] = dy
                entries.append(entry)
            elif isinstance(item, dict):
                item.setdefault("lang", lang)
                item.setdefault("script", script)
                entries.append(item)
        thematic[tf] = entries

    doc = {
        "_meta": {
            "country_slug": country_slug,
            "node_kind": "people",
            "registry": "docs/nodes/node-attribute-registry.md",
            "generated_at": NOW,
            "notes": "Country-scoped curated nodes; link via relationships during ingest.",
            "timeframe_coverage": TIMEFRAMES,
            "grouped_by": "timeframe",
        },
        "thematic_clusters": thematic,
    }

    path = os.path.join(BASE, country_slug, "people.json")
    with open(path, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    return path


def main():
    written = 0
    for slug, people_data in PEOPLE.items():
        path = write_people_file(slug, people_data)
        total = sum(len(v) for v in people_data.values())
        print(f"  OK   {slug}: {total} people entries written")
        written += 1

    print(f"\nDone. {written} countries updated with people data.")


if __name__ == "__main__":
    main()
