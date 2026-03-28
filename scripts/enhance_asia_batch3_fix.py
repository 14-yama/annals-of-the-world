#!/usr/bin/env python3
"""
Enrich 20 Asian countries (Jordan → South Korea) with 7 missing attribute keys:
  comparative_rankings, cultural_heritage, energy,
  human_rights_gender, legal_system, tourism, transport

Processes in small batches (5 at a time) with sleep between to avoid HTTP/2 blocks.
"""
import json, os, time

BASE = "/home/manasa151/annals-of-the-world/geo-registry/places/countries"

# ── All 20 countries and their extended data ──────────────────────────────────

COUNTRY_DATA = {
    "jordan": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 24, "global_rank": 89},
            "area": {"continent_rank": 27, "global_rank": 110},
            "gdp_nominal": {"continent_rank": 15, "global_rank": 89},
            "gdp_per_capita": {"continent_rank": 14, "global_rank": 88},
            "hdi": {"continent_rank": 10, "global_rank": 102},
            "life_expectancy": {"continent_rank": 13, "global_rank": 60},
            "ease_of_doing_business": {"continent_rank": 12, "global_rank": 75},
            "internet_penetration": {"continent_rank": 10, "global_rank": 55},
            "press_freedom": {"continent_rank": 32, "global_rank": 146},
            "global_peace_index": {"continent_rank": 11, "global_rank": 63},
            "innovation_index": {"continent_rank": 16, "global_rank": 78},
            "notes": "Small open economy; large refugee population (Syrian, Iraqi, Palestinian)."
        },
        "cultural_heritage": {
            "national_symbols": ["eagle of Saladin"],
            "national_animal": "Arabian oryx",
            "national_flower": "black iris",
            "national_dish": "mansaf (lamb with fermented yoghurt and rice)",
            "national_sport": "Football",
            "major_festivals": ["Jerash Festival of Culture and Arts", "Eid al-Fitr", "Eid al-Adha", "Independence Day (25 May)"],
            "cuisine_highlights": ["mansaf", "falafel", "hummus", "knafeh", "maqluba", "zarb (Bedouin BBQ)"],
            "music_art_traditions": ["Dabke folk dance", "Bedouin poetry (nabati)", "Petra rock-cut architecture", "Mosaic art (Madaba Map)"],
            "intangible_heritage_items": ["As-Samer dance (UNESCO)"],
            "notable_historical_figures": ["King Hussein bin Talal", "King Abdullah II", "T.E. Lawrence (Lawrence of Arabia association)", "Ibrahim Nasrallah (novelist)"],
            "world_heritage_sites": ["Petra", "Quseir Amra", "Um er-Rasas", "Wadi Rum Protected Area", "As-Salt – Place of Tolerance and Urban Hospitality", "Baptism Site 'Bethany Beyond the Jordan'"],
            "media_landscape": "Jordan Times (English); Al-Rai, Ad-Dustour (Arabic); Jordan TV; moderate press environment by regional standards.",
            "notes": "Petra (New 7 Wonders); Nabataean heritage; Hashemite Kingdom; Dead Sea; mosaic tradition; Bedouin culture."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 88, "hydroelectric_pct": 0, "solar_pct": 9, "wind_pct": 2, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 6500,
            "electricity_production_gwh": 21000,
            "electricity_consumption_per_capita_kwh": 2050,
            "energy_imports_pct": 93,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 100000,
            "natural_gas_production_bcm": 0.2,
            "notes": "One of the most energy-import-dependent countries; rapid solar expansion; Baynouna solar plant; oil shale reserves; planned SMR nuclear."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 33,
            "gender_inequality_index": 0.47,
            "gender_inequality_rank": 113,
            "gender_gap_index_score": 0.65,
            "women_in_parliament_pct": 12,
            "women_labor_force_participation_pct": 14,
            "maternal_mortality_per_100k": 41,
            "child_marriage_pct": 8,
            "lgbtq_legal_status": "Technically legal but socially restricted",
            "death_penalty_status": "Retentionist",
            "human_trafficking_tier": "Tier 2",
            "notes": "Constitutional monarchy; Article 16 restricts women's rights in personal status; honour crimes concern; refugee hosting strains services."
        },
        "legal_system": {
            "legal_tradition": "Civil law (French-influenced); Sharia for personal status",
            "constitution_year": 1952,
            "sharia_applicability": "Personal status matters (marriage, divorce, inheritance)",
            "customary_law_role": "Tribal law in Bedouin communities (diminishing)",
            "icc_membership": "State party (2002)",
            "judicial_independence_score": 0.45,
            "contract_enforcement_days": 689,
            "property_rights_index": 55,
            "notes": "Independent judiciary under Constitution; Court of Cassation is highest court; Sharia courts for Muslim personal status; religious courts for Christians."
        },
        "tourism": {
            "annual_visitors": 5300000,
            "tourism_revenue_usd": "$5.8 billion",
            "tourism_pct_gdp": 12,
            "tourism_employment_pct": 10,
            "unesco_world_heritage_sites": 6,
            "unesco_sites_list": ["Petra", "Quseir Amra", "Um er-Rasas", "Wadi Rum", "As-Salt", "Baptism Site"],
            "major_attractions": ["Petra", "Wadi Rum desert", "Dead Sea", "Aqaba (Red Sea diving)", "Jerash (Roman ruins)", "Amman Citadel", "Dana Biosphere Reserve"],
            "visa_free_access_countries": 52,
            "henley_passport_rank": 80,
            "notes": "Tourism major GDP contributor; Petra one of New 7 Wonders; medical tourism hub; adventure tourism growing."
        },
        "transport": {
            "major_airports_international": ["Queen Alia International Airport (Amman)"],
            "major_airports_domestic": ["King Hussein International (Aqaba)"],
            "railway_km": 509,
            "road_network_km": 7200,
            "paved_roads_pct": 100,
            "major_ports": ["Aqaba"],
            "public_transit_systems": ["Amman BRT (under development)"],
            "notes": "Aqaba only seaport; Queen Alia airport regional hub; Hejaz Railway heritage; no national rail network currently; road-dependent."
        }
    },
    "kazakhstan": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 16, "global_rank": 66},
            "area": {"continent_rank": 2, "global_rank": 9},
            "gdp_nominal": {"continent_rank": 10, "global_rank": 55},
            "gdp_per_capita": {"continent_rank": 10, "global_rank": 67},
            "hdi": {"continent_rank": 11, "global_rank": 56},
            "life_expectancy": {"continent_rank": 30, "global_rank": 109},
            "ease_of_doing_business": {"continent_rank": 5, "global_rank": 25},
            "internet_penetration": {"continent_rank": 12, "global_rank": 59},
            "press_freedom": {"continent_rank": 40, "global_rank": 158},
            "global_peace_index": {"continent_rank": 22, "global_rank": 72},
            "innovation_index": {"continent_rank": 20, "global_rank": 81},
            "notes": "Central Asia's largest economy; world's 9th largest country; major oil/uranium producer."
        },
        "cultural_heritage": {
            "national_symbols": ["golden eagle", "snow leopard"],
            "national_animal": "snow leopard",
            "national_flower": "lily (Tulipa kaufmanniana)",
            "national_dish": "beshbarmak (boiled meat with pasta sheets)",
            "national_sport": "Kazakh wrestling (kuresi); horse riding sports",
            "major_festivals": ["Nauryz (Nowruz, 22 March)", "Independence Day (16 December)", "Constitution Day", "Unity Day (1 May)"],
            "cuisine_highlights": ["beshbarmak", "kazy (horse meat sausage)", "kumis (fermented mare's milk)", "baursak", "lagman", "shubat"],
            "music_art_traditions": ["Dombra (two-stringed instrument)", "Kazakh epic poetry (zhyrau)", "Kyz kuu (kiss-the-girl horseback game)", "Felt carpet (syrmaq) art"],
            "intangible_heritage_items": ["Dombra Kuy (UNESCO)", "Kazakh traditional Assyk game (UNESCO)", "Nauryz (UNESCO)"],
            "notable_historical_figures": ["Abai Qunanbayuly (poet, 'father of Kazakh literature')", "Nursultan Nazarbayev (first president)", "Ablai Khan", "Dinmukhamed Konayev"],
            "world_heritage_sites": ["Mausoleum of Khoja Ahmed Yasawi", "Petroglyphs of Tamgaly", "Saryarka – Steppe and Lakes of Northern Kazakhstan", "Silk Roads: Chang'an-Tian Shan Corridor", "Western Tien-Shan", "Cold Winter Deserts of Turan"],
            "media_landscape": "Kazinform (state); Tengrinews (online); Khabar TV; limited press freedom; Russian and Kazakh language media.",
            "notes": "Largest landlocked country; nomadic Turkic-Mongol heritage; Soviet legacy; Baikonur Cosmodrome; rapid modernization under Nazarbayev."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 87, "hydroelectric_pct": 10, "solar_pct": 1, "wind_pct": 1, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 24000,
            "electricity_production_gwh": 113000,
            "electricity_consumption_per_capita_kwh": 5800,
            "energy_imports_pct": 0,
            "oil_production_bpd": 1800000,
            "oil_consumption_bpd": 320000,
            "natural_gas_production_bcm": 27,
            "notes": "Major oil producer (Kashagan, Tengiz, Karachaganak); world's largest uranium producer; Baikonur Cosmodrome; coal-dependent electricity generation."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 23,
            "gender_inequality_index": 0.19,
            "gender_inequality_rank": 46,
            "gender_gap_index_score": 0.71,
            "women_in_parliament_pct": 27,
            "women_labor_force_participation_pct": 64,
            "maternal_mortality_per_100k": 10,
            "child_marriage_pct": 7,
            "lgbtq_legal_status": "Legal (since 1998) but no protections",
            "death_penalty_status": "Abolitionist in practice",
            "human_trafficking_tier": "Tier 2",
            "notes": "Authoritarian governance; 2022 Bloody January protests (Almaty); ethnic Kazakh/Russian tensions; limited political pluralism."
        },
        "legal_system": {
            "legal_tradition": "Civil law (continental European and Soviet-influenced)",
            "constitution_year": 1995,
            "sharia_applicability": "Not applicable",
            "customary_law_role": "Adat (customary law) largely superseded",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.35,
            "contract_enforcement_days": 370,
            "property_rights_index": 50,
            "notes": "Supreme Court; Constitutional Council; heavy executive influence; Astana International Financial Centre uses English common law."
        },
        "tourism": {
            "annual_visitors": 9000000,
            "tourism_revenue_usd": "$3 billion",
            "tourism_pct_gdp": 1.5,
            "tourism_employment_pct": 3,
            "unesco_world_heritage_sites": 6,
            "unesco_sites_list": ["Mausoleum of Khoja Ahmed Yasawi", "Petroglyphs of Tamgaly", "Saryarka Steppe and Lakes", "Silk Roads Corridor", "Western Tien-Shan", "Cold Winter Deserts"],
            "major_attractions": ["Charyn Canyon", "Almaty (former capital)", "Astana (Nur-Sultan) modern architecture", "Big Almaty Lake", "Baikonur Cosmodrome tours", "Kolsai Lakes"],
            "visa_free_access_countries": 77,
            "henley_passport_rank": 64,
            "notes": "Growing ecotourism; ski resorts (Shymbulak); Silk Road heritage; visa-free for 77 countries."
        },
        "transport": {
            "major_airports_international": ["Nursultan Nazarbayev International (Astana)", "Almaty International Airport"],
            "major_airports_domestic": ["Aktau", "Shymkent", "Karaganda", "Atyrau"],
            "railway_km": 16600,
            "road_network_km": 96000,
            "paved_roads_pct": 87,
            "major_ports": ["Aktau (Caspian Sea)"],
            "public_transit_systems": ["Almaty Metro (1 line)", "Astana LRT (under development)"],
            "notes": "Trans-Aral and Trans-Caspian railway links; Khorgos Gateway (China–Kazakhstan dry port); vast distances between cities; Air Astana national carrier."
        }
    },
    "kuwait": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 30, "global_rank": 131},
            "area": {"continent_rank": 41, "global_rank": 152},
            "gdp_nominal": {"continent_rank": 12, "global_rank": 56},
            "gdp_per_capita": {"continent_rank": 5, "global_rank": 23},
            "hdi": {"continent_rank": 5, "global_rank": 50},
            "life_expectancy": {"continent_rank": 15, "global_rank": 46},
            "internet_penetration": {"continent_rank": 5, "global_rank": 20},
            "press_freedom": {"continent_rank": 24, "global_rank": 105},
            "global_peace_index": {"continent_rank": 17, "global_rank": 52},
            "notes": "Oil-rich Gulf state; one of the highest GDP per capita globally."
        },
        "cultural_heritage": {
            "national_symbols": ["dhow (sailing vessel)", "falcon"],
            "national_animal": "falcon",
            "national_dish": "machboos (spiced rice with meat/fish)",
            "national_sport": "Football; falconry",
            "major_festivals": ["National Day (25 February)", "Liberation Day (26 February)", "Eid al-Fitr", "Eid al-Adha", "Hala February Festival"],
            "cuisine_highlights": ["machboos", "harees", "gabout", "jireesh", "muhammar", "luqaimat"],
            "music_art_traditions": ["Sawt (Kuwaiti singing style)", "Fidjeri (pearl-diving songs)", "Al-Ardha (sword dance)", "Dhow-building heritage"],
            "intangible_heritage_items": ["Al-Sadu weaving (UNESCO)", "Fidjeri (UNESCO)"],
            "notable_historical_figures": ["Sheikh Abdullah Al-Salem Al-Sabah (independence architect)", "Sheikh Jaber Al-Ahmad (Emir during invasion)", "Nouri Al-Rawdhan (merchant)"],
            "world_heritage_sites": ["Al Zubarah Archaeological Site (shared cultural context)"],
            "media_landscape": "Al-Qabas, Al-Rai (Arabic newspapers); Kuwait Times (English); KTV; relatively freer press among Gulf states.",
            "notes": "Pearl-diving heritage; Gulf War (1990–91 Iraqi invasion); oil transformation; diwaniya social tradition; parliamentary monarchy."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 100, "hydroelectric_pct": 0, "solar_pct": 0, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0},
            "installed_capacity_mw": 19000,
            "electricity_production_gwh": 65000,
            "electricity_consumption_per_capita_kwh": 15600,
            "energy_imports_pct": 0,
            "oil_production_bpd": 2700000,
            "oil_consumption_bpd": 400000,
            "natural_gas_production_bcm": 18,
            "notes": "OPEC member; Burgan field (one of world's largest); nearly 100% fossil fuel energy; Shagaya renewable energy park planned; extreme per-capita electricity use."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 36,
            "gender_inequality_index": 0.24,
            "gender_inequality_rank": 57,
            "gender_gap_index_score": 0.63,
            "women_in_parliament_pct": 6,
            "women_labor_force_participation_pct": 50,
            "maternal_mortality_per_100k": 12,
            "lgbtq_legal_status": "Illegal (up to 7 years)",
            "death_penalty_status": "Retentionist",
            "human_trafficking_tier": "Tier 2 Watch List",
            "notes": "Only Gulf state with elected parliament; Bidoon (stateless residents) issue; kafala (sponsorship) system for workers; women gained suffrage in 2005."
        },
        "legal_system": {
            "legal_tradition": "Civil law (Egyptian-influenced); Islamic Sharia for personal status",
            "constitution_year": 1962,
            "sharia_applicability": "Personal status (family law, inheritance) for Muslims",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.45,
            "contract_enforcement_days": 566,
            "property_rights_index": 55,
            "notes": "Constitutional emirate with elected National Assembly (Majlis al-Umma); Court of Cassation; Commercial Court; Constitutional Court."
        },
        "tourism": {
            "annual_visitors": 250000,
            "tourism_revenue_usd": "$600 million",
            "tourism_pct_gdp": 0.5,
            "tourism_employment_pct": 2,
            "unesco_world_heritage_sites": 0,
            "major_attractions": ["Kuwait Towers", "Grand Mosque", "Failaka Island", "Souq Al-Mubarakiya", "The Avenues Mall", "Liberation Tower"],
            "visa_free_access_countries": 92,
            "henley_passport_rank": 55,
            "notes": "Primarily business travel; cultural tourism developing; Sheikh Jaber Al-Ahmad Cultural Centre; hot climate limits seasonal tourism."
        },
        "transport": {
            "major_airports_international": ["Kuwait International Airport"],
            "railway_km": 0,
            "road_network_km": 7000,
            "paved_roads_pct": 85,
            "major_ports": ["Shuwaikh Port", "Shuaiba Port", "Mina Al-Ahmadi (oil)"],
            "public_transit_systems": ["Kuwait Metro (planned)"],
            "notes": "No railway system; car-dependent; Kuwait International Airport hub for Kuwait Airways and Jazeera Airways; large highway network."
        }
    },
    "kyrgyzstan": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 27, "global_rank": 110},
            "area": {"continent_rank": 25, "global_rank": 85},
            "gdp_nominal": {"continent_rank": 37, "global_rank": 147},
            "gdp_per_capita": {"continent_rank": 35, "global_rank": 157},
            "hdi": {"continent_rank": 24, "global_rank": 118},
            "life_expectancy": {"continent_rank": 28, "global_rank": 104},
            "press_freedom": {"continent_rank": 15, "global_rank": 72},
            "global_peace_index": {"continent_rank": 27, "global_rank": 97},
            "notes": "Mountainous Central Asian republic; most democratic in region; remittance-dependent economy."
        },
        "cultural_heritage": {
            "national_symbols": ["Tunduk (crown of a yurt)"],
            "national_animal": "snow leopard",
            "national_flower": "Aigul (Fritillaria eduardii)",
            "national_dish": "beshbarmak; kuurdak",
            "national_sport": "Kok-boru (horseback game with goat carcass)",
            "major_festivals": ["Nooruz (21 March)", "Independence Day (31 August)", "World Nomad Games (biennial)"],
            "cuisine_highlights": ["beshbarmak", "kuurdak", "lagman noodles", "samsa", "kumis", "plov"],
            "music_art_traditions": ["Komuz (three-stringed instrument)", "Epic of Manas (world's longest epic poem)", "Shyrdak felt carpet art", "Nomadic yurt culture"],
            "intangible_heritage_items": ["Ak-kalpak craftsmanship (UNESCO)", "Kok-boru (UNESCO)", "Aitysh/Aitys (UNESCO)", "Nooruz (UNESCO)"],
            "notable_historical_figures": ["Manas (legendary hero)", "Chingiz Aitmatov (novelist)", "Kurmanjan Datka (Queen of the South)"],
            "world_heritage_sites": ["Sulaiman-Too Sacred Mountain", "Silk Roads: Chang'an-Tian Shan Corridor", "Western Tien-Shan"],
            "notes": "Nomadic Turkic heritage; Epic of Manas cultural pillar; World Nomad Games host; yurt-dwelling tradition."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 25, "hydroelectric_pct": 73, "solar_pct": 0, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 2},
            "installed_capacity_mw": 3900,
            "electricity_production_gwh": 15500,
            "electricity_consumption_per_capita_kwh": 2300,
            "energy_imports_pct": 30,
            "oil_production_bpd": 1000,
            "oil_consumption_bpd": 35000,
            "notes": "Hydropower-dominant (Toktogul Dam); water-energy nexus disputes with Uzbekistan; imports gas and oil; Kambarata HPP planned."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 28,
            "gender_inequality_index": 0.37,
            "gender_inequality_rank": 87,
            "gender_gap_index_score": 0.68,
            "women_in_parliament_pct": 19,
            "women_labor_force_participation_pct": 44,
            "maternal_mortality_per_100k": 60,
            "child_marriage_pct": 12,
            "lgbtq_legal_status": "Legal since 1998 but no protections",
            "death_penalty_status": "Abolitionist",
            "human_trafficking_tier": "Tier 2",
            "notes": "Bride kidnapping (ala kachuu) persists despite ban; 2020/2021 revolutions; ethnic tensions (Uzbek minority in south); democratic backsliding under Japarov."
        },
        "legal_system": {
            "legal_tradition": "Civil law (Soviet-influenced; continental)",
            "constitution_year": 2021,
            "sharia_applicability": "Not applicable",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.3,
            "contract_enforcement_days": 410,
            "property_rights_index": 40,
            "notes": "2021 constitution expanded presidential powers; Supreme Court; Constitutional Chamber; local courts – Aksakal (elder) mediation."
        },
        "tourism": {
            "annual_visitors": 2000000,
            "tourism_revenue_usd": "$450 million",
            "tourism_pct_gdp": 5,
            "tourism_employment_pct": 5,
            "unesco_world_heritage_sites": 3,
            "unesco_sites_list": ["Sulaiman-Too Sacred Mountain", "Silk Roads Corridor", "Western Tien-Shan"],
            "major_attractions": ["Lake Issyk-Kul", "Ala-Archa National Park", "Song Kol Lake", "Burana Tower", "Jyrgalan Valley", "World Nomad Games"],
            "visa_free_access_countries": 66,
            "henley_passport_rank": 72,
            "notes": "Adventure/eco-tourism growing; CBT (Community Based Tourism) model; horse trekking; yurt stays; Silk Road heritage."
        },
        "transport": {
            "major_airports_international": ["Manas International Airport (Bishkek)"],
            "major_airports_domestic": ["Osh Airport", "Tamchy (Issyk-Kul)"],
            "railway_km": 424,
            "road_network_km": 34000,
            "paved_roads_pct": 92,
            "public_transit_systems": ["Bishkek marshrutka (minibus) system"],
            "notes": "Mountain terrain limits infrastructure; no continuous railway; dependent on marshrutkas; China–Kyrgyzstan–Uzbekistan railway proposed."
        }
    },
    "laos": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 26, "global_rank": 105},
            "area": {"continent_rank": 22, "global_rank": 82},
            "gdp_nominal": {"continent_rank": 35, "global_rank": 135},
            "gdp_per_capita": {"continent_rank": 33, "global_rank": 141},
            "hdi": {"continent_rank": 29, "global_rank": 140},
            "life_expectancy": {"continent_rank": 34, "global_rank": 120},
            "press_freedom": {"continent_rank": 44, "global_rank": 170},
            "global_peace_index": {"continent_rank": 13, "global_rank": 44},
            "notes": "Landlocked; one of few remaining communist states; 'Battery of Southeast Asia' (hydropower)."
        },
        "cultural_heritage": {
            "national_symbols": ["three-headed elephant (Erawan)"],
            "national_animal": "Asian elephant",
            "national_flower": "dok champa (frangipani)",
            "national_dish": "laap (minced meat salad)",
            "national_sport": "Muay Lao (Lao boxing)",
            "major_festivals": ["Boun Pi Mai (Lao New Year, April)", "Boun That Luang (November)", "Boun Ok Phansa (end of Buddhist Lent)", "Boat Racing Festival"],
            "cuisine_highlights": ["laap", "sticky rice (khao niew)", "tam mak houng (papaya salad)", "ping kai (grilled chicken)", "or lam (stew)", "khao piak sen (noodle soup)"],
            "music_art_traditions": ["Khene (mouth organ – UNESCO)", "Lamvong (national dance)", "Lam singing tradition", "Buddhist temple murals", "Pha Lao (silk weaving)"],
            "intangible_heritage_items": ["Khene music (UNESCO)"],
            "notable_historical_figures": ["Fa Ngum (founder Lane Xang kingdom, 1353)", "Kaysone Phomvihane (revolutionary leader)", "Souphanouvong ('Red Prince')"],
            "world_heritage_sites": ["Town of Luang Prabang", "Vat Phou and Associated Ancient Settlements", "Megalithic Jar Sites in Xiengkhouang – Plain of Jars"],
            "notes": "Theravada Buddhist culture; French colonial influence; Lane Xang ('Million Elephants') kingdom; most bombed country per capita (Vietnam War)."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 20, "hydroelectric_pct": 75, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 4},
            "installed_capacity_mw": 11000,
            "electricity_production_gwh": 38000,
            "electricity_consumption_per_capita_kwh": 900,
            "energy_imports_pct": 0,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 18000,
            "notes": "'Battery of Southeast Asia'; 78+ dams; exports electricity to Thailand, Vietnam, Cambodia; Nam Theun 2; Mekong River dam controversies."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 13,
            "gender_inequality_index": 0.46,
            "gender_inequality_rank": 110,
            "gender_gap_index_score": 0.71,
            "women_in_parliament_pct": 22,
            "women_labor_force_participation_pct": 77,
            "maternal_mortality_per_100k": 126,
            "child_marriage_pct": 23,
            "lgbtq_legal_status": "Legal but no protections",
            "death_penalty_status": "Retentionist",
            "human_trafficking_tier": "Tier 2 Watch List",
            "notes": "One-party communist state (LPRP); no independent media; UXO (unexploded ordnance) from Vietnam War; Hmong persecution legacy."
        },
        "legal_system": {
            "legal_tradition": "Civil law (French-influenced; socialist)",
            "constitution_year": 1991,
            "sharia_applicability": "Not applicable",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.2,
            "contract_enforcement_days": 443,
            "property_rights_index": 30,
            "notes": "People's Supreme Court; LPRP controls judiciary; Constitution guarantees rights in theory; land concessions to China/Vietnam controversy."
        },
        "tourism": {
            "annual_visitors": 3500000,
            "tourism_revenue_usd": "$900 million",
            "tourism_pct_gdp": 5,
            "tourism_employment_pct": 8,
            "unesco_world_heritage_sites": 3,
            "unesco_sites_list": ["Town of Luang Prabang", "Vat Phou", "Plain of Jars"],
            "major_attractions": ["Luang Prabang (old royal capital)", "Vang Vieng (karst landscape)", "Plain of Jars", "Kuang Si Falls", "4000 Islands (Si Phan Don)", "Vientiane"],
            "visa_free_access_countries": 48,
            "henley_passport_rank": 89,
            "notes": "Backpacker favourite; eco-tourism growing; Luang Prabang UNESCO town; Mekong River cruises; Laos-China Railway boosting accessibility."
        },
        "transport": {
            "major_airports_international": ["Wattay International Airport (Vientiane)", "Luang Prabang International Airport"],
            "major_airports_domestic": ["Pakse", "Savannakhet", "Xieng Khouang"],
            "railway_km": 422,
            "road_network_km": 39500,
            "paved_roads_pct": 16,
            "public_transit_systems": ["Vientiane city bus (limited)"],
            "notes": "Laos-China Railway (Boten–Vientiane, 2021) transformative; landlocked; Mekong River transport; road quality variable; no domestic rail before 2021."
        }
    },
    "lebanon": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 29, "global_rank": 120},
            "area": {"continent_rank": 43, "global_rank": 161},
            "gdp_nominal": {"continent_rank": 21, "global_rank": 92},
            "gdp_per_capita": {"continent_rank": 17, "global_rank": 95},
            "hdi": {"continent_rank": 13, "global_rank": 112},
            "life_expectancy": {"continent_rank": 10, "global_rank": 50},
            "press_freedom": {"continent_rank": 14, "global_rank": 60},
            "notes": "Severe economic crisis since 2019; historically 'Switzerland of the Middle East'; confessional political system."
        },
        "cultural_heritage": {
            "national_symbols": ["cedar tree"],
            "national_animal": "striped hyena (unofficial)",
            "national_flower": "cedar (Cedrus libani)",
            "national_dish": "kibbeh (minced meat with bulgur)",
            "national_sport": "Football; basketball",
            "major_festivals": ["Baalbeck International Festival", "Beiteddine Art Festival", "Eid al-Fitr", "Eid al-Adha", "Christmas", "Independence Day (22 November)"],
            "cuisine_highlights": ["kibbeh", "tabbouleh", "fattoush", "hummus", "shawarma", "manakish", "baklava", "knafeh"],
            "music_art_traditions": ["Fairuz (iconic singer)", "Dabke dance", "Rahbani Brothers (musical theatre)", "Phoenician art heritage", "Arabic calligraphy"],
            "intangible_heritage_items": ["Al-Zajal (poetic dueling)"],
            "notable_historical_figures": ["Khalil Gibran (The Prophet)", "Fairuz", "Rafik Hariri (PM, assassinated 2005)", "Bachir Gemayel"],
            "world_heritage_sites": ["Anjar", "Baalbek", "Byblos", "Ouadi Qadisha and Forest of the Cedars of God", "Tyre", "Rachid Karami International Fair – Tripoli"],
            "media_landscape": "L'Orient-Le Jour (French); Daily Star (English); LBC, MTV, Future TV; most vibrant media in Arab world (historically).",
            "notes": "Phoenician heritage; Byblos (oldest continuously inhabited city claim); cedar symbol; 18 religious sects; devastating 2020 Beirut explosion."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 97, "hydroelectric_pct": 2, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0},
            "installed_capacity_mw": 3500,
            "electricity_production_gwh": 18000,
            "electricity_consumption_per_capita_kwh": 2700,
            "energy_imports_pct": 97,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 130000,
            "notes": "Chronic electricity crisis; private generators supplement grid; economic collapse worsened supply; potential offshore gas (Block 9); Syrian crisis strain."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 43,
            "gender_inequality_index": 0.41,
            "gender_inequality_rank": 99,
            "gender_gap_index_score": 0.64,
            "women_in_parliament_pct": 5,
            "women_labor_force_participation_pct": 25,
            "maternal_mortality_per_100k": 21,
            "lgbtq_legal_status": "Illegal (Article 534) but rarely enforced",
            "death_penalty_status": "Retentionist (de facto moratorium)",
            "human_trafficking_tier": "Tier 2 Watch List",
            "notes": "Confessional system entrenches sectarian division; no civil marriage law; refugee crisis (1M+ Syrians); economic collapse; Beirut port explosion accountability."
        },
        "legal_system": {
            "legal_tradition": "Civil law (French-influenced); religious courts for personal status",
            "constitution_year": 1926,
            "sharia_applicability": "Personal status for Muslim communities (Sunni and Shia separate courts)",
            "customary_law_role": "Religious community courts handle personal status for 18 sects",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.35,
            "contract_enforcement_days": 721,
            "property_rights_index": 40,
            "notes": "Oldest constitution in Arab world; confessional power-sharing (Taif Agreement 1989); Court of Cassation; 15 separate personal status laws by sect."
        },
        "tourism": {
            "annual_visitors": 2000000,
            "tourism_revenue_usd": "$6 billion (pre-crisis peak)",
            "tourism_pct_gdp": 12,
            "tourism_employment_pct": 10,
            "unesco_world_heritage_sites": 6,
            "unesco_sites_list": ["Anjar", "Baalbek", "Byblos", "Ouadi Qadisha/Cedars of God", "Tyre", "Rachid Karami International Fair"],
            "major_attractions": ["Baalbek Roman temples", "Byblos (ancient port)", "Jeita Grotto", "Beirut nightlife", "Cedars of God", "Harissa (Our Lady of Lebanon)"],
            "visa_free_access_countries": 39,
            "henley_passport_rank": 96,
            "notes": "Tourism devastated by 2019 economic crisis and 2020 Beirut explosion; historically major tourism economy; Baalbek temples rival Parthenon."
        },
        "transport": {
            "major_airports_international": ["Rafic Hariri International Airport (Beirut)"],
            "railway_km": 0,
            "road_network_km": 7000,
            "paved_roads_pct": 85,
            "major_ports": ["Port of Beirut", "Port of Tripoli"],
            "public_transit_systems": ["No formal mass transit; service taxis and buses"],
            "notes": "No operating railway; destroyed in civil war; Beirut port partially rebuilt after 2020 explosion; MEA (Middle East Airlines) national carrier."
        }
    },
    "macau": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 44, "global_rank": 170},
            "area": {"continent_rank": 48, "global_rank": 195},
            "gdp_nominal": {"continent_rank": 30, "global_rank": 95},
            "gdp_per_capita": {"continent_rank": 2, "global_rank": 4},
            "hdi": {"continent_rank": 3, "global_rank": 17},
            "life_expectancy": {"continent_rank": 1, "global_rank": 3},
            "notes": "Highest population density worldwide; gambling capital of the world; highest GDP per capita in Asia."
        },
        "cultural_heritage": {
            "national_symbols": ["lotus flower"],
            "national_flower": "lotus",
            "national_dish": "minchi (ground meat with rice and fried egg)",
            "major_festivals": ["Feast of the Drunken Dragon", "A-Ma Festival", "Chinese New Year", "Macau Grand Prix", "International Fireworks Display Contest"],
            "cuisine_highlights": ["minchi", "African chicken (galinha à africana)", "Portuguese egg tart (pastel de nata)", "serradura", "bacalhau (salt cod)", "Macanese cuisine (fusion)"],
            "music_art_traditions": ["Patuá theatre (creole drama)", "Chinese temple art", "Portuguese tile work (azulejo)", "Lion dance"],
            "notable_historical_figures": ["Matteo Ricci (Jesuit, used Macau as gateway to China)", "A-Ma (sea goddess)"],
            "world_heritage_sites": ["Historic Centre of Macau"],
            "media_landscape": "Macau Daily Times (English); Jornal Tribuna de Macau (Portuguese); TDM (public broadcaster); Chinese-language media dominant.",
            "notes": "Portuguese colonial heritage (1557–1999); SAR of China; world gambling capital (revenue 5× Las Vegas); Macanese creole culture unique fusion."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 20, "hydroelectric_pct": 0, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0},
            "installed_capacity_mw": 470,
            "electricity_production_gwh": 1200,
            "electricity_consumption_per_capita_kwh": 7800,
            "energy_imports_pct": 80,
            "notes": "Almost entirely imports electricity from mainland China (Guangdong); small local gas-fired plants; tiny territory limits generation."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 57,
            "gender_inequality_index": 0.05,
            "gender_inequality_rank": 5,
            "gender_gap_index_score": 0.72,
            "women_in_parliament_pct": 15,
            "women_labor_force_participation_pct": 65,
            "maternal_mortality_per_100k": 3,
            "lgbtq_legal_status": "Legal; decriminalised under Portuguese admin",
            "death_penalty_status": "Abolitionist",
            "notes": "SAR with Basic Law (like Hong Kong); increasing PRC influence; gambling industry working conditions; press freedom declining."
        },
        "legal_system": {
            "legal_tradition": "Civil law (Portuguese-influenced; maintained post-handover)",
            "constitution_year": 1999,
            "sharia_applicability": "Not applicable",
            "icc_membership": "Not applicable (PRC not member)",
            "judicial_independence_score": 0.55,
            "contract_enforcement_days": 350,
            "property_rights_index": 70,
            "notes": "Basic Law as mini-constitution (50-year guarantee until 2049); Court of Final Appeal; Portuguese-derived civil code; bilingual (Chinese/Portuguese) legal system."
        },
        "tourism": {
            "annual_visitors": 28000000,
            "tourism_revenue_usd": "$21 billion",
            "tourism_pct_gdp": 50,
            "tourism_employment_pct": 25,
            "unesco_world_heritage_sites": 1,
            "unesco_sites_list": ["Historic Centre of Macau"],
            "major_attractions": ["The Venetian Macao", "Ruins of St. Paul's", "A-Ma Temple", "Macau Tower", "Senado Square", "Cotai Strip casinos"],
            "visa_free_access_countries": 144,
            "notes": "Gaming capital of the world; 6 casino concessionaires; gambling revenue $20B+; Macau Grand Prix (F3); food tourism (UNESCO Creative City of Gastronomy)."
        },
        "transport": {
            "major_airports_international": ["Macau International Airport"],
            "railway_km": 0,
            "road_network_km": 430,
            "paved_roads_pct": 100,
            "major_ports": ["Inner Harbour", "Outer Harbour Ferry Terminal"],
            "public_transit_systems": ["Macau LRT (Taipa line, 2019)", "Extensive bus network"],
            "notes": "Hong Kong-Zhuhai-Macau Bridge (2018, world's longest sea crossing); ferries to Hong Kong; Macau LRT expanding; compact territory."
        }
    },
    "malaysia": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 13, "global_rank": 46},
            "area": {"continent_rank": 18, "global_rank": 66},
            "gdp_nominal": {"continent_rank": 8, "global_rank": 36},
            "gdp_per_capita": {"continent_rank": 8, "global_rank": 58},
            "hdi": {"continent_rank": 7, "global_rank": 63},
            "life_expectancy": {"continent_rank": 14, "global_rank": 65},
            "ease_of_doing_business": {"continent_rank": 4, "global_rank": 12},
            "internet_penetration": {"continent_rank": 9, "global_rank": 50},
            "press_freedom": {"continent_rank": 27, "global_rank": 113},
            "innovation_index": {"continent_rank": 10, "global_rank": 36},
            "notes": "Upper-middle-income; major palm oil and electronics exporter; multi-ethnic federation; Petronas twin towers."
        },
        "cultural_heritage": {
            "national_symbols": ["Malayan tiger", "hibiscus"],
            "national_animal": "Malayan tiger",
            "national_flower": "bunga raya (hibiscus)",
            "national_dish": "nasi lemak (coconut rice)",
            "national_sport": "Sepak takraw; badminton",
            "major_festivals": ["Hari Raya Aidilfitri", "Chinese New Year", "Deepavali", "Thaipusam", "Hari Malaysia (Malaysia Day, 16 Sept)", "Merdeka Day (31 Aug)"],
            "cuisine_highlights": ["nasi lemak", "satay", "rendang", "roti canai", "char kway teow", "laksa", "cendol", "durian"],
            "music_art_traditions": ["Gamelan", "Mak Yong (UNESCO)", "Dikir barat", "Wayang kulit (shadow puppets)", "Batik art"],
            "intangible_heritage_items": ["Mak Yong theatre (UNESCO)", "Pantun (UNESCO)"],
            "notable_historical_figures": ["Mahathir Mohamad (PM, 22 years)", "Tunku Abdul Rahman (founding PM)", "Parameswara (founded Malacca)", "Hang Tuah (legendary warrior)"],
            "world_heritage_sites": ["Gunung Mulu National Park", "Kinabalu Park", "Melaka and George Town, Historic Cities of Straits of Malacca", "Archaeological Heritage of Lenggong Valley"],
            "media_landscape": "The Star, New Straits Times (English); Berita Harian (Malay); Sin Chew Daily (Chinese); RTM, TV3, Astro; social media dominant.",
            "notes": "Multi-ethnic (Malay, Chinese, Indian, indigenous); Malacca Straits history; Petronas symbolism; food culture one of world's richest."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 82, "hydroelectric_pct": 14, "solar_pct": 2, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 2},
            "installed_capacity_mw": 36000,
            "electricity_production_gwh": 175000,
            "electricity_consumption_per_capita_kwh": 5200,
            "energy_imports_pct": 5,
            "oil_production_bpd": 600000,
            "oil_consumption_bpd": 700000,
            "natural_gas_production_bcm": 73,
            "notes": "Petronas (national oil company; Petronas Towers); major LNG exporter (Sarawak); Bakun Dam (Sarawak); transitioning to renewable energy target 31% by 2025."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 50,
            "gender_inequality_index": 0.26,
            "gender_inequality_rank": 61,
            "gender_gap_index_score": 0.68,
            "women_in_parliament_pct": 15,
            "women_labor_force_participation_pct": 56,
            "maternal_mortality_per_100k": 21,
            "child_marriage_pct": 11,
            "lgbtq_legal_status": "Illegal (Section 377A; Sharia for Muslims)",
            "death_penalty_status": "Retentionist (reform underway)",
            "human_trafficking_tier": "Tier 2 Watch List",
            "notes": "Bumiputera affirmative action policies; ethnic tensions; dual legal system (civil + Sharia for Muslims); migrant worker issues; Sedition Act."
        },
        "legal_system": {
            "legal_tradition": "English common law; Islamic Sharia for Muslims (personal status and some criminal offences)",
            "constitution_year": 1957,
            "sharia_applicability": "Sharia courts for Muslims in personal status (13 states + federal territories); limited criminal jurisdiction (RUU355 debate)",
            "customary_law_role": "Adat (customary law) in Sabah, Sarawak, and some peninsular states",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.5,
            "contract_enforcement_days": 425,
            "property_rights_index": 60,
            "notes": "Federal Court (apex); dual system – civil and Sharia; Bumiputera constitutional provisions; National Security Council Act; reformed under Reformasi."
        },
        "tourism": {
            "annual_visitors": 26000000,
            "tourism_revenue_usd": "$18 billion",
            "tourism_pct_gdp": 5,
            "tourism_employment_pct": 9,
            "unesco_world_heritage_sites": 4,
            "unesco_sites_list": ["Gunung Mulu NP", "Kinabalu Park", "Melaka and George Town", "Lenggong Valley"],
            "major_attractions": ["Petronas Twin Towers (KL)", "Langkawi Island", "Borneo rainforest (Sabah/Sarawak)", "Penang food capital", "Cameron Highlands", "Sipadan diving"],
            "visa_free_access_countries": 182,
            "henley_passport_rank": 12,
            "notes": "Major tourism destination; Malaysia Truly Asia branding; food tourism; tropical islands; Borneo wildlife; medical tourism growing."
        },
        "transport": {
            "major_airports_international": ["Kuala Lumpur International Airport (KLIA)", "Penang International", "Kota Kinabalu International"],
            "major_airports_domestic": ["Langkawi", "Kuching", "Johor Bahru Senai"],
            "railway_km": 1849,
            "road_network_km": 238000,
            "paved_roads_pct": 81,
            "major_ports": ["Port Klang", "Tanjung Pelepas", "Penang Port"],
            "public_transit_systems": ["KL RapidKL (LRT, MRT, Monorail)", "KTM Komuter", "ETS (Kuala Lumpur–Padang Besar)"],
            "notes": "KLIA major regional hub; AirAsia (low-cost carrier HQ); ECRL (East Coast Rail Link) under construction; Penang LRT planned."
        }
    },
    "maldives": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 45, "global_rank": 175},
            "area": {"continent_rank": 47, "global_rank": 186},
            "gdp_nominal": {"continent_rank": 36, "global_rank": 160},
            "gdp_per_capita": {"continent_rank": 13, "global_rank": 75},
            "hdi": {"continent_rank": 12, "global_rank": 87},
            "life_expectancy": {"continent_rank": 9, "global_rank": 48},
            "notes": "Lowest-lying country; existential climate change threat; luxury tourism dependent."
        },
        "cultural_heritage": {
            "national_symbols": ["coconut palm"],
            "national_animal": "yellowfin tuna",
            "national_flower": "pink rose (rosa polyantha)",
            "national_dish": "garudiya (fish broth)",
            "national_sport": "Football; bodu beru drumming",
            "major_festivals": ["National Day (1 Rabi' ul Awwal)", "Independence Day (26 July)", "Eid al-Fitr", "Eid al-Adha", "Republic Day (11 November)"],
            "cuisine_highlights": ["garudiya", "mas huni (tuna with coconut and onion)", "fihunu mas (grilled fish)", "hedhikaa (short eats)", "roshi (flatbread)"],
            "music_art_traditions": ["Bodu Beru drumming and dance", "Thaara (tambourine song)", "Lacquer work (liyeveli)", "Dhoni boat-building"],
            "notable_historical_figures": ["Muhammad Thakurufaanu (liberated from Portuguese, 1573)", "Ibrahim Nasir (first president of republic)", "Sultan Muhammad ibn Abdullah"],
            "world_heritage_sites": [],
            "notes": "100% Muslim nation; Dhivehi language related to Sinhalese; coral atoll nation (1192 islands, 187 inhabited); threatened by sea-level rise."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 93, "hydroelectric_pct": 0, "solar_pct": 5, "wind_pct": 1, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 400,
            "electricity_production_gwh": 700,
            "electricity_consumption_per_capita_kwh": 1300,
            "energy_imports_pct": 100,
            "oil_production_bpd": 0,
            "notes": "100% fossil fuel import-dependent; island diesel generators; floating solar projects; carbon-neutral target (aspirational); geography limits renewables."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 40,
            "gender_inequality_index": 0.37,
            "gender_inequality_rank": 85,
            "gender_gap_index_score": 0.64,
            "women_in_parliament_pct": 4,
            "women_labor_force_participation_pct": 42,
            "maternal_mortality_per_100k": 57,
            "lgbtq_legal_status": "Illegal (Sharia-based penalties)",
            "death_penalty_status": "Retentionist (de facto moratorium)",
            "human_trafficking_tier": "Tier 2",
            "notes": "Growing religious conservatism; political instability; gang violence in Malé; migrant worker exploitation; democratic backsliding concerns."
        },
        "legal_system": {
            "legal_tradition": "Islamic Sharia and English common law hybrid",
            "constitution_year": 2008,
            "sharia_applicability": "Comprehensive; Constitution requires all laws to be compatible with Islam",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.3,
            "contract_enforcement_days": 460,
            "property_rights_index": 40,
            "notes": "Supreme Court; Constitution mandates Islam as state religion; all citizens must be Muslim; judicial reform ongoing; political interference concerns."
        },
        "tourism": {
            "annual_visitors": 1900000,
            "tourism_revenue_usd": "$4.5 billion",
            "tourism_pct_gdp": 66,
            "tourism_employment_pct": 40,
            "unesco_world_heritage_sites": 0,
            "major_attractions": ["Overwater bungalows/resorts", "Coral reef diving and snorkeling", "Bioluminescent beaches (Vaadhoo)", "Malé (capital island)", "Ari Atoll (whale sharks)", "Underwater restaurant"],
            "visa_free_access_countries": 90,
            "henley_passport_rank": 61,
            "notes": "Tourism is 66% of GDP; luxury resort model (one-island-one-resort); Chinese and European tourists dominate; climate change existential threat; guesthouse tourism growing."
        },
        "transport": {
            "major_airports_international": ["Velana International Airport (Malé)"],
            "major_airports_domestic": ["Hanimaadhoo", "Gan", "Kadhdhoo", "Ifuru", "Dharavandhoo"],
            "railway_km": 0,
            "road_network_km": 93,
            "paved_roads_pct": 100,
            "major_ports": ["Malé Commercial Harbour"],
            "public_transit_systems": ["Speedboat/ferry inter-island transport", "Seaplane network (Maldivian Air Taxi/TMA)"],
            "notes": "Seaplane network unique global feature; Sinamalé Bridge (China-Maldives Friendship Bridge, 2018); ferry/speedboat essential; domestic airports expanding."
        }
    },
    "mongolia": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 35, "global_rank": 139},
            "area": {"continent_rank": 5, "global_rank": 18},
            "gdp_nominal": {"continent_rank": 34, "global_rank": 133},
            "gdp_per_capita": {"continent_rank": 20, "global_rank": 107},
            "hdi": {"continent_rank": 17, "global_rank": 96},
            "life_expectancy": {"continent_rank": 31, "global_rank": 110},
            "press_freedom": {"continent_rank": 10, "global_rank": 60},
            "global_peace_index": {"continent_rank": 15, "global_rank": 50},
            "notes": "Most sparsely populated country; landlocked between Russia and China; mining-dependent economy; democratic oasis in region."
        },
        "cultural_heritage": {
            "national_symbols": ["soyombo symbol"],
            "national_animal": "Przewalski's horse (takhi)",
            "national_flower": "scabiosa (lotus flower in Buddhist context)",
            "national_dish": "buuz (steamed dumplings)",
            "national_sport": "Three manly games: wrestling, horse racing, archery",
            "major_festivals": ["Naadam Festival (July 11–13, 'Three Manly Games')", "Tsagaan Sar (Lunar New Year)", "Eagle Festival (October, Bayan-Olgii)"],
            "cuisine_highlights": ["buuz (dumplings)", "khuushuur (fried meat pockets)", "airag (fermented mare's milk)", "tsuivan (noodle stew)", "boodog (goat BBQ from inside)", "suutei tsai (milk tea)"],
            "music_art_traditions": ["Khoomei (throat singing, UNESCO)", "Morin khuur (horse-head fiddle, UNESCO)", "Ger (yurt) culture", "Buddhist thangka painting", "Eagle hunting (Kazakh)"],
            "intangible_heritage_items": ["Khoomei throat singing (UNESCO)", "Morin khuur (UNESCO)", "Naadam (UNESCO)", "Mongolian calligraphy (UNESCO)", "Coaxing ritual for camels (UNESCO)"],
            "notable_historical_figures": ["Genghis Khan (Chinggis Khaan)", "Kublai Khan", "Bogd Khan (last monarch)", "Damdin Sükhbaatar (revolutionary hero)"],
            "world_heritage_sites": ["Orkhon Valley Cultural Landscape", "Petroglyphic Complexes of the Mongolian Altai", "Great Burkhan Khaldun Mountain", "Deer Stone Monuments and Related Bronze Age Sites"],
            "media_landscape": "UB Post, Mongol Messenger (English); MNB, Eagle TV; relatively free press by regional standards.",
            "notes": "Genghis Khan (largest contiguous land empire); nomadic pastoral tradition; ger (yurt) living; Buddhist (Gelug) revival; throat singing world-renowned."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 85, "hydroelectric_pct": 2, "solar_pct": 5, "wind_pct": 7, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 1500,
            "electricity_production_gwh": 7500,
            "electricity_consumption_per_capita_kwh": 2200,
            "energy_imports_pct": 20,
            "oil_production_bpd": 25000,
            "oil_consumption_bpd": 35000,
            "natural_gas_production_bcm": 0,
            "notes": "Coal-dependent; Tavan Tolgoi (world's largest untapped coking coal deposit); wind/solar potential in Gobi; imports electricity from Russia; Gobi wind farms expanding."
        },
        "human_rights_gender": {
            "freedom_house_status": "Free",
            "freedom_house_score": 84,
            "gender_inequality_index": 0.32,
            "gender_inequality_rank": 71,
            "gender_gap_index_score": 0.72,
            "women_in_parliament_pct": 17,
            "women_labor_force_participation_pct": 54,
            "maternal_mortality_per_100k": 45,
            "child_marriage_pct": 5,
            "lgbtq_legal_status": "Legal since 2002; discrimination ban in Criminal Code (2024 reform)",
            "death_penalty_status": "Abolitionist (2017)",
            "human_trafficking_tier": "Tier 2",
            "notes": "Rare democracy in Central/East Asia region; press freedom; mining corruption concerns; domestic violence law (2016); herder displacement."
        },
        "legal_system": {
            "legal_tradition": "Civil law (Germanic/Soviet-influenced); Mongolian tradition",
            "constitution_year": 1992,
            "sharia_applicability": "Not applicable",
            "icc_membership": "State party (2002)",
            "judicial_independence_score": 0.45,
            "contract_enforcement_days": 374,
            "property_rights_index": 45,
            "notes": "Constitutional Court; Supreme Court; democratic constitution since 1992; judicial reform ongoing; mining law critical; nomadic grazing land rights."
        },
        "tourism": {
            "annual_visitors": 650000,
            "tourism_revenue_usd": "$500 million",
            "tourism_pct_gdp": 3,
            "tourism_employment_pct": 5,
            "unesco_world_heritage_sites": 4,
            "unesco_sites_list": ["Orkhon Valley", "Mongolian Altai Petroglyphs", "Great Burkhan Khaldun Mountain", "Deer Stone Monuments"],
            "major_attractions": ["Gobi Desert", "Naadam Festival", "Terelj National Park", "Orkhon Valley", "Khustain Nuruu (wild horses)", "Eagle Festival (Bayan-Olgii)"],
            "visa_free_access_countries": 64,
            "henley_passport_rank": 75,
            "notes": "Adventure and nomadic tourism; ger camps; horseback trekking; Gobi expeditions; limited infrastructure but growing."
        },
        "transport": {
            "major_airports_international": ["Chinggis Khaan International Airport (Ulaanbaatar)"],
            "major_airports_domestic": ["Murun", "Khovd", "Dalanzadgad", "Choibalsan", "Olgii"],
            "railway_km": 1815,
            "road_network_km": 49250,
            "paved_roads_pct": 10,
            "major_ports": [],
            "public_transit_systems": ["Ulaanbaatar bus network"],
            "notes": "Trans-Mongolian Railway (Moscow–Beijing); landlocked; vast unpaved road network; new Chinggis Khaan Airport (2021); MIAT Mongolian Airlines."
        }
    },
    "myanmar": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 11, "global_rank": 26},
            "area": {"continent_rank": 15, "global_rank": 39},
            "gdp_nominal": {"continent_rank": 24, "global_rank": 72},
            "gdp_per_capita": {"continent_rank": 38, "global_rank": 165},
            "hdi": {"continent_rank": 32, "global_rank": 149},
            "life_expectancy": {"continent_rank": 33, "global_rank": 115},
            "press_freedom": {"continent_rank": 47, "global_rank": 171},
            "global_peace_index": {"continent_rank": 46, "global_rank": 163},
            "notes": "Military coup (2021) reversed democratic progress; civil war; sanctioned; Rohingya genocide."
        },
        "cultural_heritage": {
            "national_symbols": ["chinthe (mythical lion)"],
            "national_animal": "green peafowl",
            "national_flower": "padauk (Pterocarpus macrocarpus)",
            "national_dish": "mohinga (fish noodle soup)",
            "national_sport": "Chinlone (cane ball)",
            "major_festivals": ["Thingyan (Water Festival, April New Year)", "Thadingyut (Festival of Lights, October)", "Tazaungdaing", "Ananda Pagoda Festival (Bagan)"],
            "cuisine_highlights": ["mohinga", "shan noodles", "tea leaf salad (laphet thoke)", "htamin jin (rice balls)", "nan gyi thoke", "samosa soup"],
            "music_art_traditions": ["Hne (oboe) and saung gauk (arched harp)", "Yama Zatdaw (Jataka puppetry)", "Bagan temple mural art", "Shwe-chi-doe mandalas"],
            "intangible_heritage_items": ["Thanaka (cosmetic bark paste) tradition"],
            "notable_historical_figures": ["Aung San (independence hero)", "Aung San Suu Kyi (Nobel laureate, detained)", "King Anawrahta (Bagan founder)", "U Thant (UN Secretary-General)"],
            "world_heritage_sites": ["Bagan", "Pyu Ancient Cities"],
            "media_landscape": "State-controlled post-coup; Irrawaddy, Myanmar Now, DVB (in exile); severe censorship and journalist imprisonment.",
            "notes": "Bagan (2000+ temples); Shwedagon Pagoda; Theravada Buddhism; ethnic diversity (135+ groups); civil war since independence (1948); Rohingya crisis."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 55, "hydroelectric_pct": 40, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 4},
            "installed_capacity_mw": 7000,
            "electricity_production_gwh": 22000,
            "electricity_consumption_per_capita_kwh": 400,
            "energy_imports_pct": 5,
            "oil_production_bpd": 10000,
            "oil_consumption_bpd": 120000,
            "natural_gas_production_bcm": 17,
            "notes": "Natural gas exports (Shwe, Yadana fields) to Thailand/China; hydropower potential; low electrification rate (~55%); post-coup investment collapse."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 9,
            "gender_inequality_index": 0.48,
            "gender_inequality_rank": 117,
            "gender_gap_index_score": 0.68,
            "women_in_parliament_pct": 0,
            "women_labor_force_participation_pct": 47,
            "maternal_mortality_per_100k": 179,
            "child_marriage_pct": 16,
            "lgbtq_legal_status": "Illegal (Penal Code Section 377)",
            "death_penalty_status": "Retentionist (executions resumed 2022)",
            "human_trafficking_tier": "Tier 3",
            "notes": "Military coup (Feb 2021); Rohingya genocide (ICJ case); 1600+ killed post-coup; civil disobedience movement; ethnic armed organizations; NUG parallel govt."
        },
        "legal_system": {
            "legal_tradition": "English common law (colonial); customary law; martial law (post-coup)",
            "constitution_year": 2008,
            "sharia_applicability": "Not applicable",
            "customary_law_role": "Ethnic customary law in peripheral states",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.1,
            "contract_enforcement_days": 1160,
            "property_rights_index": 20,
            "notes": "2008 constitution guarantees military 25% of parliament; martial law declared in many areas post-coup; Supreme Court subservient to junta."
        },
        "tourism": {
            "annual_visitors": 100000,
            "tourism_revenue_usd": "$50 million (post-coup collapse)",
            "tourism_pct_gdp": 0.5,
            "tourism_employment_pct": 2,
            "unesco_world_heritage_sites": 2,
            "unesco_sites_list": ["Bagan", "Pyu Ancient Cities"],
            "major_attractions": ["Bagan temples", "Shwedagon Pagoda (Yangon)", "Inle Lake", "Golden Rock (Kyaiktiyo)", "Mandalay", "Ngapali Beach"],
            "visa_free_access_countries": 42,
            "henley_passport_rank": 95,
            "notes": "Tourism collapsed after 2021 coup and COVID; was growing rapidly pre-2020; Bagan UNESCO site; ethical tourism debate (before and after coup)."
        },
        "transport": {
            "major_airports_international": ["Yangon International Airport", "Mandalay International Airport"],
            "major_airports_domestic": ["Heho (Inle Lake)", "Bagan Nyaung U", "Myitkyina"],
            "railway_km": 5031,
            "road_network_km": 157000,
            "paved_roads_pct": 20,
            "major_ports": ["Yangon Port", "Thilawa Port"],
            "public_transit_systems": ["Yangon Circular Railway", "Yangon bus network"],
            "notes": "Yangon Circular Railway (loop train); colonial-era infrastructure; poor road conditions outside highways; Yangon-Mandalay Expressway; river transport on Irrawaddy."
        }
    },
    "nepal": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 15, "global_rank": 50},
            "area": {"continent_rank": 28, "global_rank": 93},
            "gdp_nominal": {"continent_rank": 29, "global_rank": 101},
            "gdp_per_capita": {"continent_rank": 40, "global_rank": 165},
            "hdi": {"continent_rank": 28, "global_rank": 143},
            "life_expectancy": {"continent_rank": 25, "global_rank": 95},
            "press_freedom": {"continent_rank": 16, "global_rank": 76},
            "global_peace_index": {"continent_rank": 25, "global_rank": 82},
            "notes": "Home of Mt. Everest; federal democratic republic since 2008; remittance-dependent economy; birthplace of Buddha."
        },
        "cultural_heritage": {
            "national_symbols": ["cow (sacred animal)", "rhododendron"],
            "national_animal": "cow (national animal); Danphe (national bird, Himalayan monal)",
            "national_flower": "rhododendron (Rhododendron arboreum)",
            "national_dish": "dal bhat (lentil soup with rice)",
            "national_sport": "Volleyball (national sport); cricket and football popular",
            "major_festivals": ["Dashain (Vijaya Dashami)", "Tihar (Festival of Lights)", "Holi", "Teej", "Indra Jatra", "Buddha Jayanti"],
            "cuisine_highlights": ["dal bhat tarkari", "momo (dumplings)", "sel roti", "chatamari", "gundruk (fermented greens)", "yomari"],
            "music_art_traditions": ["Newari pagoda architecture", "Thangka painting (Buddhist)", "Madal drum music", "Kumari (living goddess) tradition", "Paubha painting"],
            "intangible_heritage_items": ["Newah music (preservation)"],
            "notable_historical_figures": ["Prithvi Narayan Shah (unified Nepal)", "Tenzing Norgay (Everest first ascent, 1953)", "Laxmi Prasad Devkota (poet)", "Gautama Buddha (Lumbini)"],
            "world_heritage_sites": ["Sagarmatha National Park (Everest)", "Kathmandu Valley", "Chitwan National Park", "Lumbini (birthplace of Buddha)"],
            "media_landscape": "Kantipur Daily (Nepali); Kathmandu Post, Republica (English); NTV; relatively free press.",
            "notes": "Only Hindu kingdom until 2008; Newari architecture; Lumbini (Buddha's birthplace); Gurkha warrior tradition; Mt. Everest; trekking capital."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 15, "hydroelectric_pct": 80, "solar_pct": 3, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 2},
            "installed_capacity_mw": 2700,
            "electricity_production_gwh": 10500,
            "electricity_consumption_per_capita_kwh": 290,
            "energy_imports_pct": 30,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 50000,
            "notes": "Massive untapped hydropower potential (83,000 MW theoretical); Upper Tamakoshi (456 MW) largest; exports surplus to India; still imports petroleum from India."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 56,
            "gender_inequality_index": 0.45,
            "gender_inequality_rank": 110,
            "gender_gap_index_score": 0.69,
            "women_in_parliament_pct": 34,
            "women_labor_force_participation_pct": 82,
            "maternal_mortality_per_100k": 151,
            "child_marriage_pct": 33,
            "lgbtq_legal_status": "Legal (Supreme Court 2007; same-sex marriage recognised 2024)",
            "death_penalty_status": "Abolitionist",
            "human_trafficking_tier": "Tier 2",
            "notes": "First Asian country to recognise third gender (2007); LGBTQ rights pioneer in South Asia; caste-based discrimination persists; Madhesi rights; child marriage challenge."
        },
        "legal_system": {
            "legal_tradition": "Common law and Hindu legal tradition; statutory law",
            "constitution_year": 2015,
            "sharia_applicability": "Not applicable",
            "customary_law_role": "Caste and indigenous customary law in rural areas",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.4,
            "contract_enforcement_days": 910,
            "property_rights_index": 40,
            "notes": "Federal constitution since 2015 (7 provinces); Supreme Court; transitional justice from Maoist conflict (1996–2006) incomplete; new civil and criminal codes (2018)."
        },
        "tourism": {
            "annual_visitors": 1000000,
            "tourism_revenue_usd": "$700 million",
            "tourism_pct_gdp": 2,
            "tourism_employment_pct": 7,
            "unesco_world_heritage_sites": 4,
            "unesco_sites_list": ["Sagarmatha (Everest) NP", "Kathmandu Valley", "Chitwan NP", "Lumbini"],
            "major_attractions": ["Mount Everest and Himalayan trekking", "Kathmandu Durbar Square", "Lumbini (Buddha's birthplace)", "Pokhara (Fewa Lake, Annapurna)", "Chitwan (tigers, rhinos)", "Annapurna Base Camp trek"],
            "visa_free_access_countries": 38,
            "henley_passport_rank": 100,
            "notes": "Trekking capital of the world; Everest summit expeditions; spiritual/yoga tourism; 2015 earthquake recovery; Visit Nepal campaigns."
        },
        "transport": {
            "major_airports_international": ["Tribhuvan International Airport (Kathmandu)"],
            "major_airports_domestic": ["Pokhara Airport (regional)", "Lukla (Tenzing-Hillary, 'most dangerous airport')", "Bharatpur", "Biratnagar"],
            "railway_km": 59,
            "road_network_km": 27990,
            "paved_roads_pct": 55,
            "major_ports": [],
            "public_transit_systems": ["Kathmandu bus network (sajha yatayat)"],
            "notes": "Extreme terrain challenges; Lukla Airport iconic; cross-border railway from India expanding; road network fragile (landslides); no major railway system."
        }
    },
    "north-korea": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 19, "global_rank": 56},
            "area": {"continent_rank": 26, "global_rank": 97},
            "gdp_nominal": {"continent_rank": 40, "global_rank": 115},
            "gdp_per_capita": {"continent_rank": 43, "global_rank": 178},
            "hdi": {"continent_rank": 35, "global_rank": 0},
            "life_expectancy": {"continent_rank": 27, "global_rank": 100},
            "press_freedom": {"continent_rank": 48, "global_rank": 180},
            "global_peace_index": {"continent_rank": 45, "global_rank": 149},
            "notes": "Most isolated country; nuclear-armed; Juche ideology; Kim dynasty since 1948; heavily sanctioned."
        },
        "cultural_heritage": {
            "national_symbols": ["Chollima (winged horse)", "kimjongilia and kimilsungia flowers"],
            "national_flower": "Magnolia (Magnolia sieboldii)",
            "national_dish": "naengmyeon (cold buckwheat noodles)",
            "national_sport": "Football; mass gymnastics",
            "major_festivals": ["Day of the Sun (Kim Il-sung birthday, 15 April)", "Day of the Shining Star (Kim Jong-il birthday, 16 Feb)", "Foundation Day (9 Sept)", "Mass Games (Arirang)"],
            "cuisine_highlights": ["naengmyeon", "kimchi varieties", "injo gogi bap (rice with artificial meat)", "Pyongyang raengmyŏn", "bindaetteok"],
            "music_art_traditions": ["Mass Games (Arirang, world's largest)", "Mansudae Art Studio (propaganda art)", "Revolutionary opera (Sea of Blood)", "Korean folk instruments (gayageum)"],
            "notable_historical_figures": ["Kim Il-sung (founder)", "Kim Jong-il", "Kim Jong-un (current leader)", "Tangun (mythological founder)"],
            "world_heritage_sites": ["Complex of Koguryo Tombs"],
            "media_landscape": "Rodong Sinmun (party newspaper); KCNA (state news); KCTV; no independent media; total state control.",
            "notes": "Juche (self-reliance) ideology; Kim personality cult; Mass Games spectacle; Koguryo kingdom heritage; DMZ tourism."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 50, "hydroelectric_pct": 45, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 4},
            "installed_capacity_mw": 7500,
            "electricity_production_gwh": 16000,
            "electricity_consumption_per_capita_kwh": 600,
            "energy_imports_pct": 10,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 15000,
            "natural_gas_production_bcm": 0,
            "notes": "Coal and hydropower dominant; frequent blackouts; Pyongyang prioritized; oil from China (pipeline); nuclear weapons program but no civilian nuclear power; deforestation for fuel."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 3,
            "gender_inequality_index": 0.0,
            "gender_inequality_rank": 0,
            "gender_gap_index_score": 0.0,
            "women_in_parliament_pct": 18,
            "women_labor_force_participation_pct": 72,
            "maternal_mortality_per_100k": 89,
            "lgbtq_legal_status": "State claims 'does not exist'; de facto persecution",
            "death_penalty_status": "Retentionist (extensive use)",
            "human_trafficking_tier": "Tier 3",
            "notes": "Among worst human rights records globally; UN COI found crimes against humanity (2014); political prison camps (kwan-li-so, est. 80,000–120,000 inmates); no freedom of press, religion, movement, assembly."
        },
        "legal_system": {
            "legal_tradition": "Socialist civil law; Juche legal theory",
            "constitution_year": 1972,
            "sharia_applicability": "Not applicable",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.0,
            "contract_enforcement_days": 0,
            "property_rights_index": 5,
            "notes": "Judicature subordinate to Korean Workers' Party; Central Court; no rule of law in Western sense; songbun (political caste system) governs citizen status; extra-judicial enforcement."
        },
        "tourism": {
            "annual_visitors": 5000,
            "tourism_revenue_usd": "$50 million (pre-COVID estimate)",
            "tourism_pct_gdp": 0.1,
            "tourism_employment_pct": 1,
            "unesco_world_heritage_sites": 1,
            "unesco_sites_list": ["Complex of Koguryo Tombs"],
            "major_attractions": ["DMZ/Panmunjom", "Pyongyang (Juche Tower, Kumsusan Palace)", "Mount Paektu", "Kaesong","Mass Games (when held)", "Arirang Festival"],
            "visa_free_access_countries": 42,
            "henley_passport_rank": 94,
            "notes": "Extremely restricted tourism; guided tours only; Koryo Tours (Beijing-based) main operator; closed since COVID-19 (2020); US citizens banned since 2017 (Otto Warmbier)."
        },
        "transport": {
            "major_airports_international": ["Pyongyang Sunan International Airport"],
            "railway_km": 5200,
            "road_network_km": 26176,
            "paved_roads_pct": 3,
            "major_ports": ["Nampho", "Wonsan", "Hungnam", "Chongjin"],
            "public_transit_systems": ["Pyongyang Metro (2 lines, very deep)", "Pyongyang trolleybus and tram"],
            "notes": "Pyongyang Metro (one of deepest in world, 100m); rail-dependent (colonial-era Japanese infrastructure); extremely limited private car ownership; Air Koryo (national airline)."
        }
    },
    "oman": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 25, "global_rank": 96},
            "area": {"continent_rank": 19, "global_rank": 70},
            "gdp_nominal": {"continent_rank": 14, "global_rank": 70},
            "gdp_per_capita": {"continent_rank": 7, "global_rank": 40},
            "hdi": {"continent_rank": 6, "global_rank": 54},
            "life_expectancy": {"continent_rank": 8, "global_rank": 40},
            "global_peace_index": {"continent_rank": 5, "global_rank": 30},
            "notes": "Stable Gulf monarchy; Ibadi Islam unique; Sultan Qaboos modernization legacy; strategic Strait of Hormuz location."
        },
        "cultural_heritage": {
            "national_symbols": ["khanjar (curved dagger on flag)"],
            "national_animal": "Arabian oryx",
            "national_flower": "jasmine (Arabian jasmine)",
            "national_dish": "shuwa (slow-roasted lamb in underground pit)",
            "national_sport": "Camel racing; horse racing",
            "major_festivals": ["National Day (18 November)", "Eid al-Fitr", "Eid al-Adha", "Muscat Festival", "Salalah Khareef Festival (monsoon)"],
            "cuisine_highlights": ["shuwa", "majboos", "halwa (Omani sweet)", "mashuai (roasted fish with lemon rice)", "mishkak (BBQ skewers)", "dates"],
            "music_art_traditions": ["Razha war dance", "Liwa and Fann at-Tanbura (African-influenced music)", "Silver jewellery making", "Frankincense traditions", "Dhow-building"],
            "notable_historical_figures": ["Sultan Qaboos bin Said (1970–2020, moderniser)", "Ahmed bin Majid (master navigator)", "Sa'id ibn Sultan (Omani Empire)"],
            "world_heritage_sites": ["Bahla Fort", "Archaeological Sites of Bat, Al-Khutm and Al-Ayn", "Land of Frankincense", "Aflaj Irrigation Systems of Oman", "Ancient City of Qalhat"],
            "media_landscape": "Times of Oman, Muscat Daily (English); Oman Tribune; Oman TV; state-influenced; limited press freedom.",
            "notes": "Ibadi Islam (majority, unique to Oman); frankincense heritage (Dhofar); Omani maritime empire; peaceful transition of power (2020); tolerant society by Gulf standards."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 97, "hydroelectric_pct": 0, "solar_pct": 2, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 11000,
            "electricity_production_gwh": 38000,
            "electricity_consumption_per_capita_kwh": 6800,
            "energy_imports_pct": 0,
            "oil_production_bpd": 1050000,
            "oil_consumption_bpd": 200000,
            "natural_gas_production_bcm": 40,
            "notes": "Oil production declining (PDO major operator); pivoting to gas and LNG; green hydrogen plans (HYPORT Duqm); Ibri II solar plant (500 MW); Vision 2040 diversification."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 23,
            "gender_inequality_index": 0.31,
            "gender_inequality_rank": 73,
            "gender_gap_index_score": 0.61,
            "women_in_parliament_pct": 2,
            "women_labor_force_participation_pct": 32,
            "maternal_mortality_per_100k": 17,
            "lgbtq_legal_status": "Illegal (up to 3 years)",
            "death_penalty_status": "Retentionist",
            "human_trafficking_tier": "Tier 2",
            "notes": "Absolute monarchy with consultative Shura Council; relatively tolerant; Ibadi moderation; women's rights improving under Vision 2040; kafala system for workers."
        },
        "legal_system": {
            "legal_tradition": "Mixed: Anglo-Saxon common law elements, Islamic Sharia, tribal/customary",
            "constitution_year": 1996,
            "sharia_applicability": "Sharia basis for personal status and criminal law; Ibadi jurisprudence",
            "customary_law_role": "Tribal mediation (diminishing)",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.4,
            "contract_enforcement_days": 598,
            "property_rights_index": 55,
            "notes": "Basic Statute of the State (1996) as constitution; Supreme Court; Sharia courts; Commercial Court; Sultan holds ultimate legal authority."
        },
        "tourism": {
            "annual_visitors": 3500000,
            "tourism_revenue_usd": "$3 billion",
            "tourism_pct_gdp": 3,
            "tourism_employment_pct": 5,
            "unesco_world_heritage_sites": 5,
            "unesco_sites_list": ["Bahla Fort", "Bat/Al-Khutm/Al-Ayn Sites", "Land of Frankincense", "Aflaj Irrigation", "Qalhat"],
            "major_attractions": ["Musandam Peninsula (fjords)", "Wahiba Sands desert", "Jebel Akhdar (Green Mountain)", "Nizwa Fort and souq", "Wadi Shab", "Salalah (Khareef season)"],
            "visa_free_access_countries": 80,
            "henley_passport_rank": 60,
            "notes": "Tourism growing under Vision 2040; eco-adventure tourism; less mass tourism than UAE; turtle nesting (Ras al Jinz); Dhofar monsoon unique."
        },
        "transport": {
            "major_airports_international": ["Muscat International Airport", "Salalah Airport"],
            "major_airports_domestic": ["Duqm", "Khasab", "Sohar"],
            "railway_km": 0,
            "road_network_km": 60000,
            "paved_roads_pct": 82,
            "major_ports": ["Port Sultan Qaboos", "Sohar Port", "Salalah Port (major transhipment)", "Duqm Port (new mega-port)"],
            "public_transit_systems": ["Muscat bus network (Mwasalat)"],
            "notes": "No railway (planned Oman-Etihad Rail); excellent highway network; Salalah Port among top transhipment hubs; Oman Air national carrier; Duqm special economic zone."
        }
    },
    "pakistan": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 3, "global_rank": 5},
            "area": {"continent_rank": 10, "global_rank": 33},
            "gdp_nominal": {"continent_rank": 9, "global_rank": 44},
            "gdp_per_capita": {"continent_rank": 31, "global_rank": 154},
            "hdi": {"continent_rank": 31, "global_rank": 161},
            "life_expectancy": {"continent_rank": 36, "global_rank": 131},
            "press_freedom": {"continent_rank": 39, "global_rank": 150},
            "global_peace_index": {"continent_rank": 44, "global_rank": 154},
            "innovation_index": {"continent_rank": 30, "global_rank": 88},
            "notes": "Nuclear-armed; world's 5th most populous; cricket superpower; complex security environment; CPEC (China–Pakistan Economic Corridor)."
        },
        "cultural_heritage": {
            "national_symbols": ["crescent and star", "markhor (national animal)"],
            "national_animal": "markhor (screw-horned goat)",
            "national_flower": "jasmine (chambeli)",
            "national_dish": "nihari (slow-cooked stew)",
            "national_sport": "Field hockey (national); cricket (most popular)",
            "major_festivals": ["Eid al-Fitr", "Eid al-Adha", "Pakistan Day (23 March)", "Independence Day (14 August)", "Basant (spring kite festival)", "Sufi festivals (urs)"],
            "cuisine_highlights": ["biryani", "nihari", "seekh kebab", "haleem", "naan/roti", "karahi", "chapli kebab", "paye"],
            "music_art_traditions": ["Qawwali (Sufi devotional, Nusrat Fateh Ali Khan)", "Mughal miniature painting", "Truck art", "Sufi shrine (darbar) culture", "Indus Valley heritage"],
            "intangible_heritage_items": ["Suri Jagek (solar calendar, UNESCO)"],
            "notable_historical_figures": ["Muhammad Ali Jinnah (founder, Quaid-e-Azam)", "Allama Iqbal (national poet)", "Nusrat Fateh Ali Khan", "Benazir Bhutto", "Abdul Qadeer Khan (nuclear scientist)"],
            "world_heritage_sites": ["Archaeological Ruins at Moenjodaro", "Buddhist Ruins of Takht-i-Bahi", "Fort and Shalamar Gardens, Lahore", "Historical Monuments at Makli, Thatta", "Rohtas Fort", "Taxila"],
            "media_landscape": "Dawn, The News (English); Jang, Express (Urdu); Geo TV, ARY News, Dawn News; vibrant but pressured media landscape.",
            "notes": "Indus Valley (Mohenjo-daro, Harappa); Mughal heritage; Sufi tradition; 6 UNESCO sites; truck art unique; cricket passion; diverse provinces."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 62, "hydroelectric_pct": 27, "solar_pct": 3, "wind_pct": 3, "nuclear_pct": 4, "biomass_other_pct": 1},
            "installed_capacity_mw": 43000,
            "electricity_production_gwh": 150000,
            "electricity_consumption_per_capita_kwh": 600,
            "energy_imports_pct": 30,
            "oil_production_bpd": 85000,
            "oil_consumption_bpd": 500000,
            "natural_gas_production_bcm": 33,
            "notes": "CPEC energy projects; circular debt crisis; loadshedding chronic; Tarbela and Mangla dams; nuclear plants (Chashma, Karachi); LNG imports growing; solar boom."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 37,
            "gender_inequality_index": 0.54,
            "gender_inequality_rank": 145,
            "gender_gap_index_score": 0.56,
            "women_in_parliament_pct": 20,
            "women_labor_force_participation_pct": 22,
            "maternal_mortality_per_100k": 154,
            "child_marriage_pct": 18,
            "lgbtq_legal_status": "Illegal (Section 377; Sharia penalties)",
            "death_penalty_status": "Retentionist (one of highest execution rates)",
            "human_trafficking_tier": "Tier 2",
            "notes": "Honour killings persist; blasphemy law (Section 295-C, death penalty); enforced disappearances (Balochistan); military influence in politics; trans rights (2018 law, unique)."
        },
        "legal_system": {
            "legal_tradition": "English common law with Islamic law (Sharia) provisions",
            "constitution_year": 1973,
            "sharia_applicability": "Objective Resolution; Federal Shariat Court reviews laws for Islamic compliance; Hudood Ordinances",
            "customary_law_role": "Jirga/panchayat (tribal councils) in FATA/rural areas",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.35,
            "contract_enforcement_days": 1071,
            "property_rights_index": 35,
            "notes": "Supreme Court; Federal Shariat Court; dual civil-Islamic system; 18th Amendment (2010) devolved powers; military courts (controversial); FATA merger (2018)."
        },
        "tourism": {
            "annual_visitors": 1500000,
            "tourism_revenue_usd": "$1 billion",
            "tourism_pct_gdp": 0.3,
            "tourism_employment_pct": 3,
            "unesco_world_heritage_sites": 6,
            "unesco_sites_list": ["Moenjodaro", "Takht-i-Bahi", "Lahore Fort/Shalamar", "Makli Necropolis", "Rohtas Fort", "Taxila"],
            "major_attractions": ["Hunza Valley", "Skardu/K2 base camp", "Lahore (Badshahi Mosque, food street)", "Mohenjo-daro", "Fairy Meadows", "Karakoram Highway"],
            "visa_free_access_countries": 31,
            "henley_passport_rank": 103,
            "notes": "Tourism potential massive; security improvements in north; K2 and Karakoram; Gandhara Buddhist heritage; Mughal architecture; e-visa launched."
        },
        "transport": {
            "major_airports_international": ["Jinnah International (Karachi)", "Allama Iqbal International (Lahore)", "Islamabad International Airport"],
            "major_airports_domestic": ["Peshawar", "Quetta", "Multan", "Faisalabad", "Sialkot"],
            "railway_km": 11881,
            "road_network_km": 264000,
            "paved_roads_pct": 72,
            "major_ports": ["Karachi Port", "Port Qasim", "Gwadar Port (CPEC)"],
            "public_transit_systems": ["Lahore Metro (Orange Line)", "Islamabad Metrobus", "Lahore Metrobus", "Rawalpindi Metrobus", "Karachi BRT (Green Line)"],
            "notes": "Pakistan Railways (colonial-era network); Karakoram Highway (China link); CPEC infrastructure boom; Gwadar deep-water port; PIA (national airline, privatisation planned)."
        }
    },
    "philippines": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 7, "global_rank": 13},
            "area": {"continent_rank": 17, "global_rank": 63},
            "gdp_nominal": {"continent_rank": 7, "global_rank": 33},
            "gdp_per_capita": {"continent_rank": 19, "global_rank": 115},
            "hdi": {"continent_rank": 19, "global_rank": 116},
            "life_expectancy": {"continent_rank": 24, "global_rank": 93},
            "ease_of_doing_business": {"continent_rank": 15, "global_rank": 95},
            "internet_penetration": {"continent_rank": 14, "global_rank": 60},
            "press_freedom": {"continent_rank": 35, "global_rank": 132},
            "notes": "Archipelago of 7,641 islands; BPO powerhouse; largest Catholic nation in Asia; major diaspora."
        },
        "cultural_heritage": {
            "national_symbols": ["Philippine eagle", "sampaguita"],
            "national_animal": "Philippine eagle (largest eagle species)",
            "national_flower": "sampaguita (Arabian jasmine)",
            "national_dish": "adobo (braised meat)",
            "national_sport": "Arnis (stick fighting); basketball most popular",
            "major_festivals": ["Sinulog (Cebu)", "Ati-Atihan (Aklan)", "MassKara (Bacolod)", "Pahiyas (Lucban)", "Panagbenga (Baguio)", "Christmas season (world's longest)"],
            "cuisine_highlights": ["adobo", "sinigang (sour soup)", "lechon (roast pig)", "lumpia (spring rolls)", "halo-halo (dessert)", "kare-kare", "sisig"],
            "music_art_traditions": ["Rondalla (string ensemble)", "Kulintang (gong ensemble, Mindanao)", "Tinikling (bamboo dance)", "Harana (serenade tradition)", "Baybayin script revival"],
            "intangible_heritage_items": ["Hudhud chants (UNESCO)", "Darangen epic (UNESCO)", "Tugging rituals and games (UNESCO)"],
            "notable_historical_figures": ["José Rizal (national hero)", "Andres Bonifacio (revolutionary)", "Emilio Aguinaldo (first president)", "Corazon Aquino (People Power)", "Lapu-Lapu (Cebu warrior)"],
            "world_heritage_sites": ["Baroque Churches", "Tubbataha Reefs Natural Park", "Rice Terraces of the Philippine Cordilleras", "Historic City of Vigan", "Mount Hamiguitan Range Wildlife Sanctuary"],
            "media_landscape": "Philippine Inquirer, Philippine Star (English); Manila Bulletin; ABS-CBN, GMA; active social media (top globally in usage time).",
            "notes": "300+ years Spanish colonialism; American period (1898–1946); People Power Revolution (1986); Catholicism 90%+; BPO capital; Christmas starts September."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 57, "hydroelectric_pct": 10, "solar_pct": 5, "wind_pct": 3, "nuclear_pct": 0, "biomass_other_pct": 5, "geothermal_pct": 20},
            "installed_capacity_mw": 27000,
            "electricity_production_gwh": 102000,
            "electricity_consumption_per_capita_kwh": 900,
            "energy_imports_pct": 35,
            "oil_production_bpd": 15000,
            "oil_consumption_bpd": 450000,
            "natural_gas_production_bcm": 3,
            "notes": "World's second-largest geothermal energy producer; Malampaya gas field (declining); coal imports growing; Bataan Nuclear Power Plant (never operated); renewable energy act (2008)."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 47,
            "gender_inequality_index": 0.42,
            "gender_inequality_rank": 103,
            "gender_gap_index_score": 0.79,
            "women_in_parliament_pct": 28,
            "women_labor_force_participation_pct": 46,
            "maternal_mortality_per_100k": 78,
            "child_marriage_pct": 17,
            "lgbtq_legal_status": "Legal but no anti-discrimination law; SOGIE bill pending",
            "death_penalty_status": "Abolitionist (2006)",
            "human_trafficking_tier": "Tier 1",
            "notes": "Duterte drug war (2016–2022, thousands killed, ICC investigation); EJKs; Marcos family return; red-tagging of activists; strong women's rights record."
        },
        "legal_system": {
            "legal_tradition": "Mixed: civil law (Spanish), common law (American), Islamic law (BARMM)",
            "constitution_year": 1987,
            "sharia_applicability": "Sharia in BARMM (Bangsamoro Autonomous Region in Muslim Mindanao)",
            "customary_law_role": "Indigenous Peoples' Rights Act (IPRA, 1997) recognises customary law",
            "icc_membership": "Withdrew (2019, effective); ICC retains jurisdiction for pre-withdrawal acts",
            "judicial_independence_score": 0.4,
            "contract_enforcement_days": 842,
            "property_rights_index": 45,
            "notes": "Supreme Court (15 justices); writ of amparo/habeas data (human rights writs); BARMM Bangsamoro Organic Law (2019); Cybercrime Prevention Act."
        },
        "tourism": {
            "annual_visitors": 5500000,
            "tourism_revenue_usd": "$10 billion",
            "tourism_pct_gdp": 2.5,
            "tourism_employment_pct": 13,
            "unesco_world_heritage_sites": 6,
            "unesco_sites_list": ["Baroque Churches", "Tubbataha Reefs", "Rice Terraces", "Vigan", "Mount Hamiguitan", "Puerto Princesa Subterranean River"],
            "major_attractions": ["Boracay Island", "Palawan (El Nido, Coron)", "Chocolate Hills (Bohol)", "Banaue Rice Terraces", "Cebu (whale sharks, Sinulog)", "Siargao (surfing)"],
            "visa_free_access_countries": 67,
            "henley_passport_rank": 74,
            "notes": "'It's More Fun in the Philippines' branding; island tourism; diving; Boracay rehabilitation (2018); medical/wellness tourism growing."
        },
        "transport": {
            "major_airports_international": ["Ninoy Aquino International (Manila)", "Mactan-Cebu International", "Clark International"],
            "major_airports_domestic": ["Davao", "Iloilo", "Kalibo", "Puerto Princesa", "Bacolod"],
            "railway_km": 77,
            "road_network_km": 210528,
            "paved_roads_pct": 65,
            "major_ports": ["Manila (International Container Terminal)", "Cebu Port", "Subic Bay", "Davao Port"],
            "public_transit_systems": ["Manila LRT (2 lines)", "Manila MRT-3", "Jeepney (iconic)", "PNR Commuter (Manila)"],
            "notes": "Jeepney (iconic transport); Manila traffic among world's worst; North-South Commuter Railway (under construction); inter-island ferries essential; PAL, Cebu Pacific main airlines."
        }
    },
    "qatar": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 34, "global_rank": 142},
            "area": {"continent_rank": 42, "global_rank": 158},
            "gdp_nominal": {"continent_rank": 11, "global_rank": 52},
            "gdp_per_capita": {"continent_rank": 1, "global_rank": 6},
            "hdi": {"continent_rank": 4, "global_rank": 42},
            "life_expectancy": {"continent_rank": 6, "global_rank": 27},
            "internet_penetration": {"continent_rank": 2, "global_rank": 5},
            "press_freedom": {"continent_rank": 28, "global_rank": 119},
            "notes": "Highest GDP per capita globally; FIFA 2022 host; Al Jazeera HQ; world's largest LNG exporter."
        },
        "cultural_heritage": {
            "national_symbols": ["oryx", "dhow"],
            "national_animal": "Arabian oryx",
            "national_flower": "Qataf (Lemonium axillare)",
            "national_dish": "machboos (spiced rice with meat/seafood)",
            "national_sport": "Football; camel racing; falconry",
            "major_festivals": ["Qatar National Day (18 December)", "Eid al-Fitr", "Eid al-Adha", "National Sports Day (February)"],
            "cuisine_highlights": ["machboos", "harees", "madrouba", "balaleet (sweet vermicelli)", "luqaimat", "Arabic coffee (gahwa)"],
            "music_art_traditions": ["Ardah sword dance", "Pearl-diving heritage songs", "Islamic calligraphy and geometry", "Museum of Islamic Art (I.M. Pei)"],
            "notable_historical_figures": ["Sheikh Jassim bin Mohammed (founder)", "Sheikh Hamad bin Khalifa (moderniser)", "Sheikha Moza bint Nasser (education champion)"],
            "world_heritage_sites": ["Al Zubarah Archaeological Site"],
            "media_landscape": "Al Jazeera (founded 1996, globally influential); The Peninsula (English); Qatar Tribune; beIN Media Group; significant soft power through media.",
            "notes": "FIFA 2022 World Cup host; Museum of Islamic Art; Education City; Al Jazeera global influence; pearl-diving heritage; rapid transformation from fishing village."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 100, "hydroelectric_pct": 0, "solar_pct": 0, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0},
            "installed_capacity_mw": 10500,
            "electricity_production_gwh": 48000,
            "electricity_consumption_per_capita_kwh": 15000,
            "energy_imports_pct": 0,
            "oil_production_bpd": 600000,
            "oil_consumption_bpd": 300000,
            "natural_gas_production_bcm": 177,
            "notes": "World's largest LNG exporter; North Field (world's largest gas field, shared with Iran's South Pars); QatarEnergy; NFE expansion to 126 mtpa by 2027; Al Kharsaah solar (800 MW)."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 25,
            "gender_inequality_index": 0.19,
            "gender_inequality_rank": 42,
            "gender_gap_index_score": 0.63,
            "women_in_parliament_pct": 5,
            "women_labor_force_participation_pct": 58,
            "maternal_mortality_per_100k": 8,
            "lgbtq_legal_status": "Illegal (up to 7 years)",
            "death_penalty_status": "Retentionist",
            "human_trafficking_tier": "Tier 2",
            "notes": "Migrant worker rights (kafala reforms post-FIFA scrutiny); FIFA 2022 worker deaths controversy; limited political participation; male guardianship elements."
        },
        "legal_system": {
            "legal_tradition": "Civil law (Egyptian-influenced); Islamic Sharia",
            "constitution_year": 2004,
            "sharia_applicability": "Family law; criminal law partially; main source of legislation per constitution",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.45,
            "contract_enforcement_days": 570,
            "property_rights_index": 60,
            "notes": "Qatar Financial Centre uses common law; Court of Cassation; Supreme Judiciary Council; Shura Council (advisory); Emir holds ultimate authority."
        },
        "tourism": {
            "annual_visitors": 4200000,
            "tourism_revenue_usd": "$16 billion",
            "tourism_pct_gdp": 7,
            "tourism_employment_pct": 8,
            "unesco_world_heritage_sites": 1,
            "unesco_sites_list": ["Al Zubarah Archaeological Site"],
            "major_attractions": ["Museum of Islamic Art", "Souq Waqif", "The Pearl-Qatar", "Lusail Iconic Stadium", "Katara Cultural Village", "Desert safari (inland sea)"],
            "visa_free_access_countries": 93,
            "henley_passport_rank": 52,
            "notes": "FIFA 2022 legacy infrastructure; stopover tourism via Qatar Airways (Hamad Airport hub); Lusail City; rapid hospitality expansion."
        },
        "transport": {
            "major_airports_international": ["Hamad International Airport (Doha)"],
            "railway_km": 0,
            "road_network_km": 9830,
            "paved_roads_pct": 100,
            "major_ports": ["Hamad Port", "Ras Laffan (LNG)"],
            "public_transit_systems": ["Doha Metro (3 lines, 2019)", "Lusail Tram"],
            "notes": "Hamad International Airport (multiple 'World's Best' awards); Qatar Airways hub; Doha Metro (built for FIFA 2022); no railway; excellent road network."
        }
    },
    "saudi-arabia": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 8, "global_rank": 42},
            "area": {"continent_rank": 4, "global_rank": 12},
            "gdp_nominal": {"continent_rank": 1, "global_rank": 17},
            "gdp_per_capita": {"continent_rank": 4, "global_rank": 28},
            "hdi": {"continent_rank": 8, "global_rank": 55},
            "life_expectancy": {"continent_rank": 12, "global_rank": 58},
            "internet_penetration": {"continent_rank": 3, "global_rank": 12},
            "global_peace_index": {"continent_rank": 30, "global_rank": 107},
            "innovation_index": {"continent_rank": 7, "global_rank": 48},
            "notes": "Largest economy in Middle East; OPEC leader; custodian of Islam's two holiest sites; Vision 2030 transformation."
        },
        "cultural_heritage": {
            "national_symbols": ["palm tree and crossed swords", "shahada (creed)"],
            "national_animal": "Arabian horse; Arabian camel",
            "national_flower": "none official",
            "national_dish": "kabsa (spiced rice with meat)",
            "national_sport": "Football; camel racing; falconry",
            "major_festivals": ["National Day (23 September)", "Eid al-Fitr", "Eid al-Adha", "Janadriyah (National Heritage Festival)", "Riyadh Season"],
            "cuisine_highlights": ["kabsa", "mandi", "jareesh", "saleeg", "mutabbaq", "Arabic coffee (qahwa) with dates", "kunafa"],
            "music_art_traditions": ["Ardah (sword dance, UNESCO)", "Nabati (Bedouin) poetry", "Al-Ula rock art", "Hejazi architecture (Jeddah balconies)", "Sadu weaving"],
            "intangible_heritage_items": ["Ardah Najdiyah (UNESCO)", "Arabic coffee (UNESCO)", "Almezmar drumstick dance (UNESCO)", "Al-Qatt Al-Asiri female painting (UNESCO)"],
            "notable_historical_figures": ["King Abdulaziz (Ibn Saud, founder, 1932)", "King Faisal (oil embargo)", "Mohammed bin Salman (MBS, Crown Prince, Vision 2030)"],
            "world_heritage_sites": ["Al-Hijr (Mada'in Salih)", "At-Turaif District in ad-Dir'iyah", "Historic Jeddah", "Rock Art in the Ha'il Region", "Al-Ahsa Oasis", "Ḥimā Cultural Area", "Uruq Bani Ma'arid"],
            "media_landscape": "Arab News, Saudi Gazette (English); Al-Riyadh, Okaz (Arabic); MBC, SBC, Rotana; Saudi Vision media transformation.",
            "notes": "Mecca and Medina (Islam's holiest cities); Hajj pilgrimage (2M+ annually); Vision 2030 (NEOM, The Line, Red Sea Project); rapid social transformation; AlUla heritage tourism."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 99, "hydroelectric_pct": 0, "solar_pct": 1, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0},
            "installed_capacity_mw": 82000,
            "electricity_production_gwh": 380000,
            "electricity_consumption_per_capita_kwh": 10000,
            "energy_imports_pct": 0,
            "oil_production_bpd": 10500000,
            "oil_consumption_bpd": 3500000,
            "natural_gas_production_bcm": 117,
            "notes": "World's largest oil exporter; Saudi Aramco (world's most valuable company); Ghawar field (world's largest); OPEC de facto leader; Vision 2030 renewable targets (50% by 2030); NEOM green hydrogen."
        },
        "human_rights_gender": {
            "freedom_house_status": "Not Free",
            "freedom_house_score": 8,
            "gender_inequality_index": 0.25,
            "gender_inequality_rank": 56,
            "gender_gap_index_score": 0.60,
            "women_in_parliament_pct": 20,
            "women_labor_force_participation_pct": 33,
            "maternal_mortality_per_100k": 16,
            "lgbtq_legal_status": "Illegal (death penalty possible)",
            "death_penalty_status": "Retentionist (one of highest execution rates)",
            "human_trafficking_tier": "Tier 2",
            "notes": "Absolute monarchy; women's driving ban lifted (2018); male guardianship reformed; Jamal Khashoggi killing (2018); mass executions; Wahhabism moderating under MBS."
        },
        "legal_system": {
            "legal_tradition": "Islamic Sharia (Hanbali school primary); royal decrees",
            "constitution_year": 1992,
            "sharia_applicability": "Comprehensive: basis of all law; no codified penal code until 2021 reforms",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.3,
            "contract_enforcement_days": 575,
            "property_rights_index": 55,
            "notes": "Basic Law of Governance (1992, not a constitution); Supreme Court; Shura Council (150 members, advisory); codification of personal status law (2022); KAFD financial courts."
        },
        "tourism": {
            "annual_visitors": 27000000,
            "tourism_revenue_usd": "$36 billion",
            "tourism_pct_gdp": 4,
            "tourism_employment_pct": 6,
            "unesco_world_heritage_sites": 7,
            "unesco_sites_list": ["Al-Hijr (Mada'in Saleh)", "At-Turaif", "Historic Jeddah", "Rock Art Ha'il Region", "Al-Ahsa Oasis", "Ḥimā Cultural Area", "Uruq Bani Ma'arid"],
            "major_attractions": ["Mecca (Hajj/Umrah)", "Medina (Prophet's Mosque)", "AlUla (Hegra)", "NEOM/The Line (under construction)", "Riyadh (Boulevard, Diriyah)", "Red Sea coast"],
            "visa_free_access_countries": 78,
            "henley_passport_rank": 62,
            "notes": "Tourism pillar of Vision 2030; e-visa (2019) opened leisure tourism; religious tourism (Hajj/Umrah ~15M/year); Red Sea Project; Qiddiya entertainment city."
        },
        "transport": {
            "major_airports_international": ["King Abdulaziz (Jeddah)", "King Khalid (Riyadh)", "King Fahd (Dammam)"],
            "major_airports_domestic": ["Medina", "Abha", "Tabuk", "Ha'il", "Jizan"],
            "railway_km": 5200,
            "road_network_km": 221372,
            "paved_roads_pct": 47,
            "major_ports": ["Jeddah Islamic Port", "King Abdulaziz Port (Dammam)", "NEOM Port (planned)", "Yanbu Port"],
            "public_transit_systems": ["Riyadh Metro (6 lines, 2024 opening)", "Mecca Metro (Mashair Railway, Hajj)", "Haramain High-Speed Railway (Mecca–Medina via Jeddah)"],
            "notes": "Haramain HSR (450 km/h); Riyadh Metro (world's largest metro project); Saudia national carrier; massive road network; land bridge railway (SAR)."
        }
    },
    "singapore": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 33, "global_rank": 116},
            "area": {"continent_rank": 49, "global_rank": 192},
            "gdp_nominal": {"continent_rank": 6, "global_rank": 34},
            "gdp_per_capita": {"continent_rank": 3, "global_rank": 5},
            "hdi": {"continent_rank": 2, "global_rank": 9},
            "life_expectancy": {"continent_rank": 2, "global_rank": 4},
            "ease_of_doing_business": {"continent_rank": 1, "global_rank": 2},
            "internet_penetration": {"continent_rank": 1, "global_rank": 3},
            "press_freedom": {"continent_rank": 38, "global_rank": 153},
            "innovation_index": {"continent_rank": 2, "global_rank": 5},
            "notes": "City-state; global financial center; world's busiest port; highest HDI in Asia; 'Garden City'."
        },
        "cultural_heritage": {
            "national_symbols": ["Merlion", "orchid (Vanda Miss Joaquim)"],
            "national_animal": "lion (Singapura = 'Lion City')",
            "national_flower": "Vanda Miss Joaquim (hybrid orchid)",
            "national_dish": "no official; contenders: chicken rice, laksa, chilli crab",
            "national_sport": "Football (national); badminton, swimming popular",
            "major_festivals": ["Chinese New Year", "Hari Raya Aidilfitri", "Deepavali", "National Day (9 August)", "Thaipusam", "Hungry Ghost Festival"],
            "cuisine_highlights": ["Hainanese chicken rice", "chilli crab", "laksa", "char kway teow", "bak kut teh", "satay", "roti prata", "kaya toast"],
            "music_art_traditions": ["Hawker culture (UNESCO)", "Peranakan (Straits Chinese) culture", "Chinese opera (wayang)", "Malay kompang drumming", "Indian classical dance"],
            "intangible_heritage_items": ["Hawker culture (UNESCO, 2020)"],
            "notable_historical_figures": ["Lee Kuan Yew (founding PM)", "Stamford Raffles (founded modern Singapore, 1819)", "S Rajaratnam (foreign affairs)", "Yusof Ishak (first president)"],
            "world_heritage_sites": ["Singapore Botanic Gardens"],
            "media_landscape": "Straits Times (English); Lianhe Zaobao (Chinese); Berita Harian (Malay); CNA (Channel NewsAsia); tightly managed media environment.",
            "notes": "Multi-ethnic harmony model (Chinese 76%, Malay 15%, Indian 8%); hawker centres; Singlish; Marina Bay Sands; world's most expensive city; efficiency and order."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 95, "hydroelectric_pct": 0, "solar_pct": 4, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 1},
            "installed_capacity_mw": 13500,
            "electricity_production_gwh": 55000,
            "electricity_consumption_per_capita_kwh": 9100,
            "energy_imports_pct": 98,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 1400000,
            "natural_gas_production_bcm": 0,
            "notes": "Natural gas dominant (95% of electricity); major oil refining hub; no domestic energy sources; importing electricity from Laos/Malaysia (ASEAN Power Grid); rooftop solar; hydrogen research."
        },
        "human_rights_gender": {
            "freedom_house_status": "Partly Free",
            "freedom_house_score": 47,
            "gender_inequality_index": 0.04,
            "gender_inequality_rank": 6,
            "gender_gap_index_score": 0.73,
            "women_in_parliament_pct": 29,
            "women_labor_force_participation_pct": 62,
            "maternal_mortality_per_100k": 7,
            "lgbtq_legal_status": "Decriminalised Section 377A (2022); no same-sex marriage",
            "death_penalty_status": "Retentionist (mandatory for drug trafficking)",
            "human_trafficking_tier": "Tier 1",
            "notes": "PAP dominant-party system since 1959; strict laws (caning, death penalty for drugs); limited press freedom; POFMA (anti-fake news); efficient governance; Section 377A repealed 2022."
        },
        "legal_system": {
            "legal_tradition": "English common law",
            "constitution_year": 1965,
            "sharia_applicability": "AMLA (Administration of Muslim Law Act) for Muslim personal law; Syariah Court",
            "icc_membership": "Not a state party",
            "judicial_independence_score": 0.7,
            "contract_enforcement_days": 164,
            "property_rights_index": 90,
            "notes": "Supreme Court (Court of Appeal, High Court); renowned for rule of law and contract enforcement; SICC (Singapore International Commercial Court); low corruption; mandatory death penalty for drugs."
        },
        "tourism": {
            "annual_visitors": 16000000,
            "tourism_revenue_usd": "$20 billion",
            "tourism_pct_gdp": 4,
            "tourism_employment_pct": 7,
            "unesco_world_heritage_sites": 1,
            "unesco_sites_list": ["Singapore Botanic Gardens"],
            "major_attractions": ["Marina Bay Sands", "Gardens by the Bay", "Sentosa Island", "Orchard Road", "Chinatown/Little India/Kampong Glam", "Singapore Zoo/Night Safari"],
            "visa_free_access_countries": 195,
            "henley_passport_rank": 1,
            "notes": "World's most powerful passport; Changi Airport ('World's Best' repeatedly); MICE tourism; Sentosa integrated resorts; food tourism; F1 Singapore Grand Prix night race."
        },
        "transport": {
            "major_airports_international": ["Singapore Changi Airport (world's best)"],
            "railway_km": 0,
            "road_network_km": 3500,
            "paved_roads_pct": 100,
            "major_ports": ["Port of Singapore (2nd busiest globally)"],
            "public_transit_systems": ["Singapore MRT (6 lines, 200+ km)", "LRT (3 lines)", "Extensive bus network"],
            "notes": "Changi Airport (Terminal 5 under construction); Port of Singapore handles 37M+ TEU; MRT world-class; ERP (Electronic Road Pricing); COE system (car ownership); Johor Bahru–Singapore RTS Link planned."
        }
    },
    "south-korea": {
        "comparative_rankings": {
            "_note": "Country position relative to continent and global.",
            "population": {"continent_rank": 10, "global_rank": 28},
            "area": {"continent_rank": 29, "global_rank": 107},
            "gdp_nominal": {"continent_rank": 4, "global_rank": 12},
            "gdp_per_capita": {"continent_rank": 9, "global_rank": 30},
            "hdi": {"continent_rank": 1, "global_rank": 19},
            "life_expectancy": {"continent_rank": 4, "global_rank": 7},
            "ease_of_doing_business": {"continent_rank": 2, "global_rank": 5},
            "internet_penetration": {"continent_rank": 3, "global_rank": 5},
            "press_freedom": {"continent_rank": 8, "global_rank": 47},
            "innovation_index": {"continent_rank": 1, "global_rank": 1},
            "notes": "K-wave (Hallyu) cultural superpower; Samsung/Hyundai/LG; world's most innovative country; tech powerhouse; aging crisis."
        },
        "cultural_heritage": {
            "national_symbols": ["taegeuk (yin-yang)", "Mugunghwa (Rose of Sharon)"],
            "national_animal": "Siberian tiger (symbolic); magpie (national bird)",
            "national_flower": "Mugunghwa (Rose of Sharon)",
            "national_dish": "kimchi; bibimbap",
            "national_sport": "Taekwondo (originated in Korea)",
            "major_festivals": ["Chuseok (harvest festival)", "Seollal (Lunar New Year)", "Boryeong Mud Festival", "Lotus Lantern Festival (Buddha's Birthday)", "Jinhae Cherry Blossom"],
            "cuisine_highlights": ["kimchi", "bibimbap", "bulgogi", "Korean BBQ (samgyeopsal)", "tteokbokki", "japchae", "sundae (blood sausage)", "fried chicken"],
            "music_art_traditions": ["K-pop (BTS, BLACKPINK, global phenomenon)", "K-drama", "Pansori (epic singing, UNESCO)", "Korean pottery (celadon)", "Hangul (alphabet, Sejong)"],
            "intangible_heritage_items": ["Kimjang (kimchi making, UNESCO)", "Pansori (UNESCO)", "Ganggangsullae (UNESCO)", "Arirang folk song (UNESCO)", "Jeju Haenyeo (diving women, UNESCO)"],
            "notable_historical_figures": ["King Sejong the Great (Hangul inventor)", "Admiral Yi Sun-sin (turtle ships)", "Ban Ki-moon (UN Secretary-General)", "Park Chung-hee (economic transformation)"],
            "world_heritage_sites": ["Changdeokgung Palace Complex", "Haeinsa Temple Janggyeong Panjeon", "Seokguram Grotto and Bulguksa Temple", "Jongmyo Shrine", "Hwaseong Fortress", "Gyeongju Historic Areas", "Gochang/Hwasun/Ganghwa Dolmen Sites", "Jeju Volcanic Island and Lava Tubes", "Royal Tombs of Joseon", "Historic Villages (Hahoe and Yangdong)", "Namhansanseong", "Baekje Historic Areas", "Sansa (Buddhist Mountain Monasteries)", "Seowon (Neo-Confucian Academies)", "Getbol (Korean Tidal Flats)"],
            "media_landscape": "Chosun Ilbo, JoongAng Ilbo, Dong-a Ilbo (major dailies); KBS, MBC, SBS; Korea Herald (English); vibrant digital media.",
            "notes": "Hallyu (Korean Wave) global cultural export; K-pop, K-drama, K-beauty; 5000-year history; Joseon dynasty; DMZ; tech adoption world-leading; fastest internet globally."
        },
        "energy": {
            "energy_mix": {"fossil_fuels_pct": 63, "hydroelectric_pct": 1, "solar_pct": 5, "wind_pct": 2, "nuclear_pct": 27, "biomass_other_pct": 2},
            "installed_capacity_mw": 134000,
            "electricity_production_gwh": 600000,
            "electricity_consumption_per_capita_kwh": 11000,
            "energy_imports_pct": 93,
            "oil_production_bpd": 0,
            "oil_consumption_bpd": 2700000,
            "natural_gas_production_bcm": 0.5,
            "notes": "World's 5th largest nuclear power producer (25 reactors); major LNG importer; no domestic energy resources; coal phase-out planned; renewable energy target 30% by 2036."
        },
        "human_rights_gender": {
            "freedom_house_status": "Free",
            "freedom_house_score": 83,
            "gender_inequality_index": 0.07,
            "gender_inequality_rank": 15,
            "gender_gap_index_score": 0.68,
            "women_in_parliament_pct": 19,
            "women_labor_force_participation_pct": 54,
            "maternal_mortality_per_100k": 8,
            "lgbtq_legal_status": "Legal but no anti-discrimination law",
            "death_penalty_status": "Abolitionist in practice (since 1997)",
            "human_trafficking_tier": "Tier 1",
            "notes": "Vibrant democracy (since 1987); candlelight revolution (2016, impeached Park Geun-hye); gender pay gap highest in OECD; conscription for males; birth rate crisis (0.72 TFR)."
        },
        "legal_system": {
            "legal_tradition": "Civil law (German/Japanese-influenced)",
            "constitution_year": 1987,
            "sharia_applicability": "Not applicable",
            "icc_membership": "State party (2002)",
            "judicial_independence_score": 0.65,
            "contract_enforcement_days": 290,
            "property_rights_index": 75,
            "notes": "Constitutional Court (powerful; impeachment jurisdiction); Supreme Court; robust rule of law; National Security Law (controversial, restricts pro-North speech)."
        },
        "tourism": {
            "annual_visitors": 15000000,
            "tourism_revenue_usd": "$20 billion",
            "tourism_pct_gdp": 1,
            "tourism_employment_pct": 5,
            "unesco_world_heritage_sites": 16,
            "unesco_sites_list": ["Changdeokgung", "Haeinsa Temple", "Seokguram/Bulguksa", "Jongmyo", "Hwaseong", "Gyeongju", "Dolmen Sites", "Jeju", "Royal Tombs", "Hahoe/Yangdong", "Namhansanseong", "Baekje", "Sansa", "Seowon", "Getbol", "Gaya Tumuli"],
            "major_attractions": ["Seoul (Gyeongbokgung Palace, Myeongdong, Gangnam)", "Jeju Island", "DMZ (Korean Demilitarized Zone)", "Busan (Haeundae Beach)", "Gyeongju (Silla heritage)", "K-pop experiences"],
            "visa_free_access_countries": 192,
            "henley_passport_rank": 2,
            "notes": "Hallyu tourism boom; K-pop and K-drama tourism (filming locations); medical tourism hub; temple stay programs; 2nd most powerful passport globally."
        },
        "transport": {
            "major_airports_international": ["Incheon International Airport (Seoul)", "Gimpo International Airport"],
            "major_airports_domestic": ["Gimhae (Busan)", "Jeju International", "Daegu", "Gwangju"],
            "railway_km": 4071,
            "road_network_km": 112977,
            "paved_roads_pct": 92,
            "major_ports": ["Busan (world's 7th busiest container port)", "Incheon Port", "Gwangyang Port"],
            "public_transit_systems": ["Seoul Metro (9+ lines, one of world's most extensive)", "Busan Metro", "Daegu Metro", "KTX (high-speed rail, 305 km/h)", "Incheon Metro"],
            "notes": "KTX high-speed rail (Seoul–Busan 2h15m); Seoul Metro world-class; Incheon Airport repeatedly 'World's Best'; Busan transshipment hub; Korean Air and Asiana (merging)."
        }
    }
}

def enrich_country(slug, new_data):
    """Merge new_data into an existing country index.json."""
    path = os.path.join(BASE, slug, "index.json")
    with open(path, "r") as f:
        data = json.load(f)
    profile = data.setdefault("country_profile", {})
    for key, val in new_data.items():
        profile[key] = val
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return len(new_data)

def main():
    batch_size = 5
    countries = list(COUNTRY_DATA.items())
    total = len(countries)
    done = 0
    
    for i in range(0, total, batch_size):
        batch = countries[i:i+batch_size]
        print(f"\n── Batch {i//batch_size + 1} ({len(batch)} countries) ──")
        for slug, attrs in batch:
            added = enrich_country(slug, attrs)
            done += 1
            print(f"  ✓ {slug}: +{added} keys ({done}/{total})")
        
        if i + batch_size < total:
            print(f"  ⏳ sleeping 2s to avoid rate-limit blocks...")
            time.sleep(2)
    
    print(f"\n✅ Done: enriched {done} countries with 7 extended attributes each.")

if __name__ == "__main__":
    main()
