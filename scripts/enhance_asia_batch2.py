#!/usr/bin/env python3
"""
Enhance Asian countries with new template sections + expanded fields.
Batch 2: Georgia, Hong Kong, India, Indonesia, Iran, Iraq, Israel, Japan
Sources: World Bank, IMF, CIA Factbook, UNDP HDR, WHO, FAO, GPI, Freedom House,
         WJP, EPI, ITU, WIPO GII, UNWTO (2023-2024 estimates).

NOTE: Small batches to avoid HTTP/2 error block (rate-limiting).
"""
import json, os, copy

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "geo-registry", "places", "countries")

DATA = {
"georgia": {
  "_basics": {
    "capital_coordinates": {"lat": 41.7151, "lon": 44.8271},
    "other_major_cities": ["Batumi", "Kutaisi", "Rustavi", "Zugdidi", "Gori"],
    "national_motto": "Strength is in Unity",
    "national_anthem": "Tavisupleba (Freedom)",
    "currency_code": "GEL",
    "internet_tld": ".ge",
    "utc_offset": "UTC+4",
    "drives_on": "right",
    "other_languages": ["Mingrelian", "Svan", "Abkhaz", "Ossetic", "Azerbaijani", "Armenian", "Russian"]
  },
  "geography": {
    "coordinates": {"lat": 42.3154, "lon": 43.3569},
    "bounding_box": {"north": 43.59, "south": 41.05, "east": 46.74, "west": 40.00},
    "land_area_km2": 69700,
    "water_area_km2": 310,
    "coastline_km": 310,
    "borders": ["Russia", "Turkey", "Armenia", "Azerbaijan"],
    "border_lengths_km": {"Russia": 894, "Turkey": 273, "Armenia": 219, "Azerbaijan": 428},
    "highest_point": {"name": "Mount Shkhara", "elevation_m": 5193},
    "lowest_point": {"name": "Black Sea", "elevation_m": 0},
    "terrain": "Mountainous; Greater Caucasus in north, Lesser Caucasus in south; Kolkheti lowlands west; fertile Kakheti valley east",
    "land_use": {"agricultural_pct": 35.5, "arable_pct": 5.8, "forest_pct": 39.4, "other_pct": 25.1},
    "major_rivers": ["Mtkvari (Kura)", "Rioni", "Inguri"],
    "major_lakes": ["Paravani", "Tabatskuri"],
    "exclusive_economic_zone_km2": 22038,
    "landlocked": False,
    "notes": "Crossroads of Europe and Asia; Greater Caucasus provides natural border with Russia; Abkhazia and South Ossetia occupied by Russia (20% of territory); Black Sea coastline."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$28 billion",
    "gdp_ppp_usd": "$72 billion",
    "gdp_per_capita_nominal_usd": 7500,
    "gdp_per_capita_ppp_usd": 19300,
    "gdp_growth_rate_pct": 7.5,
    "inflation_rate_pct": 2.5,
    "unemployment_rate_pct": 16.4,
    "youth_unemployment_rate_pct": 30.0,
    "poverty_rate_pct": 15.6,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 34.5,
    "income_classification": "Upper-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 7, "industry_pct_gdp": 21, "services_pct_gdp": 72},
    "labor_force": 1900000,
    "labor_force_by_sector": {"agriculture_pct": 40, "industry_pct": 14, "services_pct": 46},
    "fdi_inflow_usd": "$1.8 billion",
    "fdi_outflow_usd": "$200 million",
    "foreign_exchange_reserves_usd": "$5.0 billion",
    "ease_of_doing_business_rank": 7,
    "economic_freedom_index_score": 73.4,
    "credit_rating": {"moodys": "Ba2", "sp": "BB", "fitch": "BB"},
    "notes": "Remarkably high ease of doing business rank; post-2022 boom from Russian immigration/capital flight; wine tourism; transit corridor (BTC pipeline, BTK railway); EU candidate status 2023."
  },
  "health": {
    "health_expenditure_pct_gdp": 7.6,
    "health_expenditure_per_capita_usd": 540,
    "physicians_per_1k": 5.1,
    "nurses_midwives_per_1k": 4.3,
    "hospital_beds_per_1k": 2.8,
    "maternal_mortality_per_100k": 28,
    "hiv_prevalence_pct": 0.4,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 50,
    "access_to_clean_water_pct": 98,
    "access_to_sanitation_pct": 95,
    "vaccination_coverage_pct": 90,
    "stunting_under5_pct": 6,
    "obesity_rate_pct": 21.7,
    "universal_health_coverage_index": 63,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Chronic respiratory diseases", "Diabetes"],
    "notes": "Universal Healthcare Programme (UHC) since 2013; high physician density but quality uneven; medical tourism growing (dental, cosmetic); Soviet-era facilities being modernized."
  },
  "food_agriculture": {
    "food_security_index_score": 55.0,
    "food_security_index_rank": 72,
    "arable_land_pct": 5.8,
    "agricultural_land_pct": 35.5,
    "irrigated_land_pct": 43,
    "major_crops": ["grapes", "citrus", "tea", "hazelnuts", "corn", "wheat", "vegetables"],
    "major_livestock": ["cattle", "sheep", "goats", "pigs", "poultry"],
    "food_import_dependency_pct": 45,
    "cereal_yield_kg_per_hectare": 2800,
    "agricultural_employment_pct": 40,
    "notes": "8,000-year winemaking tradition (qvevri method, UNESCO heritage); world's oldest wine culture; hazelnut top export crop; tea production in western Georgia; organic farming growing."
  },
  "energy": {
    "primary_energy_sources": ["hydropower", "natural gas", "oil"],
    "electricity_generation_gwh": 13500,
    "electricity_consumption_per_capita_kwh": 2700,
    "renewable_share_pct": 80,
    "fossil_fuel_share_pct": 20,
    "nuclear_share_pct": 0,
    "oil_production_bpd": 400,
    "oil_consumption_bpd": 20000,
    "natural_gas_production_bcm": 0,
    "proved_oil_reserves_bbl": "35 million",
    "proved_gas_reserves_tcm": "0.008",
    "energy_imports_pct": 65,
    "electrification_rate_pct": 100,
    "notes": "Hydropower 80% of electricity; BTC oil pipeline transit country; Shah Deniz gas (Azerbaijan to Europe) transits Georgia; energy dependency on imports; wind/solar potential underexploited; Namakhvani HPP project cancelled after protests."
  },
  "transport": {
    "airports": 22,
    "airports_paved": 18,
    "railways_km": 1363,
    "roadways_km": 20295,
    "paved_roads_pct": 94,
    "waterways_km": 0,
    "major_ports": ["Batumi", "Poti", "Anaklia (planned)"],
    "national_airline": "Georgian Airways",
    "vehicle_ownership_per_1k": 320,
    "notes": "BTK railway (Baku-Tbilisi-Kars) links Caucasus and Turkey; Poti/Batumi Black Sea ports; Middle Corridor transit route (China-Europe); Tbilisi International Airport; mountainous terrain limits infrastructure."
  },
  "tourism": {
    "international_arrivals": 7100000,
    "tourism_revenue_usd": "$3.5 billion",
    "tourism_pct_gdp": 12.5,
    "major_attractions": ["Tbilisi Old Town", "Vardzia cave monastery", "Svaneti (UNESCO)", "Kazbegi (Stepantsminda)", "Batumi", "Kakheti wine region"],
    "unesco_world_heritage_sites": 3,
    "notes": "Tourism boom post-2010; wine tourism major draw; ski resorts (Gudauri, Bakuriani); UNESCO 8,000-year qvevri winemaking; culinary tourism; e-visa/visa-free for many; Digital Nomad visa programme."
  },
  "legal_system": {
    "type": "Civil law",
    "supreme_court": "Supreme Court of Georgia",
    "international_court_jurisdiction": "ICJ accepted",
    "suffrage": "18 years, universal",
    "legal_traditions": ["Continental civil law", "Post-Soviet legal system"],
    "death_penalty": False,
    "notes": "EU candidate country (Dec 2023); constitutional reforms ongoing; judiciary independence concerns; Rose Revolution (2003) led to governance reforms; foreign agent law controversy (2024, EU accession implications)."
  },
  "human_rights_gender": {
    "freedom_house_score": 58,
    "freedom_house_status": "Partly Free",
    "gender_inequality_index": 0.275,
    "gender_inequality_rank": 71,
    "women_in_parliament_pct": 19,
    "female_labor_force_participation_pct": 51,
    "maternal_leave_weeks": 24,
    "child_marriage_pct": 14,
    "lgbtq_legal_status": "Legal (constitutional ban on same-sex marriage, 2024)",
    "press_freedom_rank": 103,
    "notes": "Democratic backsliding concerns (foreign agent law 2024); anti-LGBTQ+ violence (2021 Tbilisi Pride attacks); patriarchal traditions in rural areas; EU conditionality on human rights reforms; media polarized."
  },
  "security_stability": {
    "global_peace_index_score": 2.026,
    "global_peace_index_rank": 68,
    "homicide_rate_per_100k": 2.7,
    "terrorism_index_score": 0.5,
    "terrorism_index_rank": 100,
    "armed_conflict": True,
    "internally_displaced_persons": 304000,
    "landmine_contamination": True,
    "notes": "20% of territory occupied by Russia (Abkhazia, South Ossetia since 2008 war); 'borderization' creeping annexation; NATO aspirations blocked by Russia; 280,000+ IDPs from 1990s/2008 conflicts."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Georgian polyphonic singing", "Qvevri winemaking", "Living culture of three writing systems of Georgian alphabet"],
    "notable_cultural_exports": ["Wine (qvevri method)", "Polyphonic singing", "Georgian cuisine", "Georgian alphabet (unique script)"],
    "major_museums": ["Georgian National Museum", "Simon Janashia Museum", "Open Air Museum of Ethnography"],
    "world_heritage_sites_list": ["Historical Monuments of Mtskheta", "Gelati Monastery", "Upper Svaneti"],
    "culinary_traditions": ["Khachapuri", "Khinkali", "Churchkhela", "Pkhali", "Satsivi"],
    "notes": "One of the world's oldest and most unique alphabets (14 letters, 3 scripts); 8,000-year wine tradition (world's oldest); Georgian polyphonic singing sent into space on Voyager Golden Record."
  },
  "comparative_rankings": {
    "human_development_index_rank": 63,
    "global_competitiveness_rank": 74,
    "happiness_index_rank": 117,
    "environmental_performance_rank": 79,
    "gender_gap_rank": 78,
    "soft_power_rank": 0,
    "notes": "Exceptionally high ease of doing business; strong anti-corruption progress post-Rose Revolution; occupied territories drag security scores; EU candidacy milestone."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.70,
    "ict_development_index": 5.8,
    "mobile_money_accounts": 400000,
    "digital_payments_pct_adults": 60,
    "fintech_companies": 40,
    "startup_ecosystem_value_usd": "$300 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 55.0,
    "innovation_index_score": 30.0,
    "innovation_index_rank": 64,
    "ai_readiness_index": 40.0
  }
},

"hong-kong": {
  "_basics": {
    "capital_coordinates": {"lat": 22.3193, "lon": 114.1694},
    "other_major_cities": ["Kowloon", "Tsuen Wan", "Sha Tin", "Tuen Mun", "Tai Po"],
    "national_motto": "None (SAR of PRC)",
    "national_anthem": "Yìyǒngjūn Jìnxíngqǔ (March of the Volunteers, PRC anthem)",
    "currency_code": "HKD",
    "internet_tld": ".hk",
    "utc_offset": "UTC+8",
    "drives_on": "left",
    "other_languages": ["English", "Mandarin", "Fukienese", "Hakka"]
  },
  "geography": {
    "coordinates": {"lat": 22.3964, "lon": 114.1095},
    "bounding_box": {"north": 22.56, "south": 22.15, "east": 114.43, "west": 113.84},
    "land_area_km2": 1114,
    "water_area_km2": 35,
    "coastline_km": 733,
    "borders": ["China (Guangdong)"],
    "border_lengths_km": {"China": 33},
    "highest_point": {"name": "Tai Mo Shan", "elevation_m": 958},
    "lowest_point": {"name": "South China Sea", "elevation_m": 0},
    "terrain": "Hilly to mountainous; lowlands in north; 263 islands; extensive reclamation",
    "land_use": {"agricultural_pct": 5.0, "arable_pct": 3.2, "forest_pct": 25.0, "other_pct": 70.0},
    "major_rivers": [],
    "major_lakes": [],
    "exclusive_economic_zone_km2": 0,
    "landlocked": False,
    "notes": "Special Administrative Region of China; one of world's most densely populated places; Victoria Harbour iconic; 75% green/country park; land reclamation creates new territory."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$383 billion",
    "gdp_ppp_usd": "$527 billion",
    "gdp_per_capita_nominal_usd": 51000,
    "gdp_per_capita_ppp_usd": 70000,
    "gdp_growth_rate_pct": 3.2,
    "inflation_rate_pct": 2.1,
    "unemployment_rate_pct": 2.9,
    "youth_unemployment_rate_pct": 8.0,
    "poverty_rate_pct": 20.0,
    "poverty_line_definition": "Government poverty line (50% median household income)",
    "gini_coefficient": 53.9,
    "income_classification": "High income",
    "sector_breakdown": {"agriculture_pct_gdp": 0.1, "industry_pct_gdp": 6, "services_pct_gdp": 94},
    "labor_force": 3900000,
    "labor_force_by_sector": {"agriculture_pct": 0, "industry_pct": 6, "services_pct": 94},
    "fdi_inflow_usd": "$117 billion",
    "fdi_outflow_usd": "$88 billion",
    "foreign_exchange_reserves_usd": "$425 billion",
    "ease_of_doing_business_rank": 3,
    "economic_freedom_index_score": 89.7,
    "credit_rating": {"moodys": "Aa3", "sp": "AA+", "fitch": "AA-"},
    "notes": "World's freest economy (Heritage Foundation); global financial centre (#4); world's most expensive real estate; no sales tax; HKD pegged to USD (Linked Exchange Rate); re-export hub for China; extreme inequality (highest Gini in developed world)."
  },
  "health": {
    "health_expenditure_pct_gdp": 6.8,
    "health_expenditure_per_capita_usd": 3500,
    "physicians_per_1k": 2.1,
    "nurses_midwives_per_1k": 8.0,
    "hospital_beds_per_1k": 4.9,
    "maternal_mortality_per_100k": 2,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 57,
    "access_to_clean_water_pct": 100,
    "access_to_sanitation_pct": 100,
    "vaccination_coverage_pct": 95,
    "stunting_under5_pct": 0,
    "obesity_rate_pct": 5.3,
    "universal_health_coverage_index": 91,
    "leading_causes_of_death": ["Cancer", "Cardiovascular diseases", "Pneumonia", "Cerebrovascular diseases"],
    "notes": "World's highest life expectancy (~85 years); dual public/private healthcare system; Doctor-Hong Kong shortage; world's first SARS outbreak 2003; COVID zero policy 2020-22."
  },
  "food_agriculture": {
    "food_security_index_score": 78.0,
    "food_security_index_rank": 25,
    "arable_land_pct": 3.2,
    "agricultural_land_pct": 5.0,
    "irrigated_land_pct": 0,
    "major_crops": ["vegetables"],
    "major_livestock": ["poultry", "pigs"],
    "food_import_dependency_pct": 95,
    "cereal_yield_kg_per_hectare": 0,
    "agricultural_employment_pct": 0,
    "notes": "98% food imported (primarily from mainland China); agriculture <0.1% GDP; rooftop/vertical farming experiments; world-class food culture; Michelin-star density among world's highest."
  },
  "energy": {
    "primary_energy_sources": ["natural gas", "coal", "nuclear (from Daya Bay)", "renewables"],
    "electricity_generation_gwh": 35000,
    "electricity_consumption_per_capita_kwh": 5700,
    "renewable_share_pct": 1,
    "fossil_fuel_share_pct": 74,
    "nuclear_share_pct": 25,
    "oil_production_bpd": 0,
    "oil_consumption_bpd": 0,
    "natural_gas_production_bcm": 0,
    "proved_oil_reserves_bbl": "0",
    "proved_gas_reserves_tcm": "0",
    "energy_imports_pct": 100,
    "electrification_rate_pct": 100,
    "notes": "100% energy imported; 25% electricity from Daya Bay nuclear plant (Guangdong); phasing out coal for natural gas; offshore wind potential; CLP and HK Electric duopoly; world-class grid reliability."
  },
  "transport": {
    "airports": 2,
    "airports_paved": 2,
    "railways_km": 77,
    "roadways_km": 2107,
    "paved_roads_pct": 100,
    "waterways_km": 0,
    "major_ports": ["Victoria Harbour (Kwai Tsing container terminal)"],
    "national_airline": "Cathay Pacific",
    "vehicle_ownership_per_1k": 90,
    "notes": "MTR metro system world-class (99.9% on-time); Hong Kong International Airport (HKIA) among world's top cargo airports; Octopus card universal payment; Hong Kong-Zhuhai-Macau Bridge (55 km, world's longest sea crossing bridge); Star Ferry iconic."
  },
  "tourism": {
    "international_arrivals": 34000000,
    "tourism_revenue_usd": "$38 billion",
    "tourism_pct_gdp": 10.0,
    "major_attractions": ["Victoria Peak", "Victoria Harbour", "Big Buddha (Tian Tan)", "Temple Street Night Market", "Disneyland", "Ocean Park"],
    "unesco_world_heritage_sites": 0,
    "notes": "One of world's most visited cities; shopping/dining destination; Chinese mainland visitors dominant; post-COVID recovery; Star Ferry and Peak Tram iconic; Geopark volcanic formations."
  },
  "legal_system": {
    "type": "Mixed legal system",
    "supreme_court": "Court of Final Appeal",
    "international_court_jurisdiction": "Not applicable (SAR)",
    "suffrage": "18 years (limited elections — LegCo partially elected)",
    "legal_traditions": ["English common law", "Chinese customary law (limited)"],
    "death_penalty": False,
    "notes": "One Country Two Systems (until 2047); National Security Law (2020) fundamentally changed legal landscape; Basic Law mini-constitution; once-independent judiciary facing Beijing pressure; Article 23 enacted 2024."
  },
  "human_rights_gender": {
    "freedom_house_score": 43,
    "freedom_house_status": "Partly Free",
    "gender_inequality_index": 0.041,
    "gender_inequality_rank": 4,
    "women_in_parliament_pct": 20,
    "female_labor_force_participation_pct": 55,
    "maternal_leave_weeks": 14,
    "child_marriage_pct": 0,
    "lgbtq_legal_status": "Legal (no marriage/civil union; partial court victories)",
    "press_freedom_rank": 135,
    "notes": "Dramatic decline in freedoms post-NSL 2020; Apple Daily shut down; pro-democracy activists imprisoned; media self-censorship; foreign domestic helpers (400k+) exploitation concerns; previously strong rule of law eroding."
  },
  "security_stability": {
    "global_peace_index_score": 1.640,
    "global_peace_index_rank": 28,
    "homicide_rate_per_100k": 0.3,
    "terrorism_index_score": 1.0,
    "terrorism_index_rank": 95,
    "armed_conflict": False,
    "internally_displaced_persons": 0,
    "landmine_contamination": False,
    "notes": "Extremely low crime rate; PLA garrison present but rarely visible; 2019 pro-democracy protests (2M+ marchers); post-NSL political stability through suppression; no conventional security threats."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": [],
    "notable_cultural_exports": ["Cantonese cinema (kung fu films)", "Cantopop music", "Dim sum culture", "Financial services"],
    "major_museums": ["Hong Kong Museum of Art", "Hong Kong Heritage Museum", "Hong Kong Museum of History", "M+ Museum"],
    "world_heritage_sites_list": [],
    "culinary_traditions": ["Dim sum", "Wonton noodles", "Char siu", "Egg tarts", "Milk tea", "Roast goose"],
    "notes": "Bruce Lee and kung fu cinema global impact; Cantopop golden era (1980s); East-meets-West cultural fusion; world capital of dim sum; M+ museum (Asia's largest modern art museum); comic book culture (manhua)."
  },
  "comparative_rankings": {
    "human_development_index_rank": 4,
    "global_competitiveness_rank": 7,
    "happiness_index_rank": 86,
    "environmental_performance_rank": 46,
    "gender_gap_rank": 51,
    "soft_power_rank": 0,
    "notes": "World's freest economy and top financial centre; HDI among highest globally; sharp decline in freedom/press rankings post-2020; extreme housing unaffordability."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.88,
    "ict_development_index": 8.5,
    "mobile_money_accounts": 5000000,
    "digital_payments_pct_adults": 90,
    "fintech_companies": 600,
    "startup_ecosystem_value_usd": "$20 billion",
    "data_protection_law": True,
    "cybersecurity_index_score": 82.0,
    "innovation_index_score": 57.0,
    "innovation_index_rank": 14,
    "ai_readiness_index": 72.0
  }
},

"india": {
  "_basics": {
    "capital_coordinates": {"lat": 28.6139, "lon": 77.2090},
    "other_major_cities": ["Mumbai", "Bengaluru", "Kolkata", "Chennai", "Hyderabad", "Ahmedabad", "Pune", "Surat"],
    "national_motto": "Satyameva Jayate (Truth Alone Triumphs)",
    "national_anthem": "Jana Gana Mana",
    "currency_code": "INR",
    "internet_tld": ".in",
    "utc_offset": "UTC+5:30",
    "drives_on": "left",
    "other_languages": ["Bengali", "Telugu", "Marathi", "Tamil", "Gujarati", "Urdu", "Kannada", "Odia", "Malayalam", "Punjabi"]
  },
  "geography": {
    "coordinates": {"lat": 20.5937, "lon": 78.9629},
    "bounding_box": {"north": 35.50, "south": 6.75, "east": 97.40, "west": 68.17},
    "land_area_km2": 3287263,
    "water_area_km2": 314070,
    "coastline_km": 7516,
    "borders": ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"],
    "border_lengths_km": {"Pakistan": 3190, "China": 3488, "Nepal": 1770, "Bhutan": 659, "Bangladesh": 4142, "Myanmar": 1468},
    "highest_point": {"name": "Kangchenjunga", "elevation_m": 8586},
    "lowest_point": {"name": "Kuttanad", "elevation_m": -2},
    "terrain": "Himalayas north; Indo-Gangetic plain; Deccan Plateau south; Western/Eastern Ghats; Thar Desert west",
    "land_use": {"agricultural_pct": 60.5, "arable_pct": 52.8, "forest_pct": 24.0, "other_pct": 15.5},
    "major_rivers": ["Ganges", "Brahmaputra", "Indus", "Godavari", "Krishna", "Narmada"],
    "major_lakes": ["Chilika Lake", "Wular Lake", "Vembanad Lake"],
    "exclusive_economic_zone_km2": 2305143,
    "landlocked": False,
    "notes": "7th largest country; world's most populous (1.43B); Himalayas world's highest mountain range; monsoon climate critical for agriculture; Andaman & Nicobar Islands; Lakshadweep."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$3.9 trillion",
    "gdp_ppp_usd": "$14.6 trillion",
    "gdp_per_capita_nominal_usd": 2730,
    "gdp_per_capita_ppp_usd": 10200,
    "gdp_growth_rate_pct": 7.8,
    "inflation_rate_pct": 5.4,
    "unemployment_rate_pct": 7.1,
    "youth_unemployment_rate_pct": 23.0,
    "poverty_rate_pct": 10.0,
    "poverty_line_definition": "Below $2.15/day (World Bank)",
    "gini_coefficient": 35.7,
    "income_classification": "Lower-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 17, "industry_pct_gdp": 26, "services_pct_gdp": 57},
    "labor_force": 530000000,
    "labor_force_by_sector": {"agriculture_pct": 42, "industry_pct": 26, "services_pct": 32},
    "fdi_inflow_usd": "$71 billion",
    "fdi_outflow_usd": "$14 billion",
    "foreign_exchange_reserves_usd": "$640 billion",
    "ease_of_doing_business_rank": 63,
    "economic_freedom_index_score": 55.7,
    "credit_rating": {"moodys": "Baa3", "sp": "BBB-", "fitch": "BBB-"},
    "notes": "World's 5th largest economy; fastest growing major economy; IT/BPO global leader (Bengaluru, Hyderabad); UPI digital payments revolution; Make in India manufacturing push; demographic dividend; informal sector ~80% employment."
  },
  "health": {
    "health_expenditure_pct_gdp": 3.3,
    "health_expenditure_per_capita_usd": 78,
    "physicians_per_1k": 0.7,
    "nurses_midwives_per_1k": 1.7,
    "hospital_beds_per_1k": 0.5,
    "maternal_mortality_per_100k": 97,
    "hiv_prevalence_pct": 0.2,
    "malaria_incidence_per_1k": 4,
    "tuberculosis_incidence_per_100k": 199,
    "access_to_clean_water_pct": 93,
    "access_to_sanitation_pct": 72,
    "vaccination_coverage_pct": 93,
    "stunting_under5_pct": 31,
    "obesity_rate_pct": 3.9,
    "universal_health_coverage_index": 55,
    "leading_causes_of_death": ["Cardiovascular diseases", "Chronic respiratory diseases", "Diarrheal diseases", "Tuberculosis"],
    "notes": "World's largest vaccination programme; Ayushman Bharat (500M beneficiaries, world's largest health insurance); 'pharmacy of the world' (generic drugs); COVID made 2B+ vaccine doses; AIIMS premier hospitals; air pollution major health burden."
  },
  "food_agriculture": {
    "food_security_index_score": 51.0,
    "food_security_index_rank": 81,
    "arable_land_pct": 52.8,
    "agricultural_land_pct": 60.5,
    "irrigated_land_pct": 48,
    "major_crops": ["rice", "wheat", "sugarcane", "cotton", "tea", "spices", "pulses", "oilseeds"],
    "major_livestock": ["cattle (world's largest herd)", "buffalo", "goats", "sheep", "poultry"],
    "food_import_dependency_pct": 5,
    "cereal_yield_kg_per_hectare": 3200,
    "agricultural_employment_pct": 42,
    "notes": "World's #1 producer of milk, pulses, spices, tea, jute; #2 rice and wheat producer; Green Revolution transformed food security; MSP procurement system; world's largest food subsidy programme (800M people); water stress critical."
  },
  "energy": {
    "primary_energy_sources": ["coal", "oil", "natural gas", "solar", "wind", "nuclear", "hydropower", "biomass"],
    "electricity_generation_gwh": 1900000,
    "electricity_consumption_per_capita_kwh": 1200,
    "renewable_share_pct": 22,
    "fossil_fuel_share_pct": 75,
    "nuclear_share_pct": 3,
    "oil_production_bpd": 600000,
    "oil_consumption_bpd": 5500000,
    "natural_gas_production_bcm": 34,
    "proved_oil_reserves_bbl": "4.5 billion",
    "proved_gas_reserves_tcm": "1.38",
    "energy_imports_pct": 40,
    "electrification_rate_pct": 100,
    "notes": "World's 3rd largest energy consumer; coal 70% of electricity; massive solar expansion (target 500 GW renewable by 2030); Jamnagar world's largest refinery; energy poverty despite 100% electrification claim; LNG imports growing."
  },
  "transport": {
    "airports": 346,
    "airports_paved": 253,
    "railways_km": 68525,
    "roadways_km": 6371847,
    "paved_roads_pct": 65,
    "waterways_km": 14500,
    "major_ports": ["Mumbai (JNPT)", "Chennai", "Visakhapatnam", "Kandla", "Paradip", "Kolkata"],
    "national_airline": "Air India",
    "vehicle_ownership_per_1k": 60,
    "notes": "Indian Railways: world's 4th largest network, 13M passengers/day; highway expansion (Bharatmala Pariyojana); Delhi Metro largest in India; bullet train (Mumbai-Ahmedabad) under construction; IndiGo world's fastest growing airline."
  },
  "tourism": {
    "international_arrivals": 10900000,
    "tourism_revenue_usd": "$35 billion",
    "tourism_pct_gdp": 0.9,
    "major_attractions": ["Taj Mahal", "Jaipur", "Varanasi", "Kerala backwaters", "Goa", "Golden Temple (Amritsar)", "Ladakh"],
    "unesco_world_heritage_sites": 42,
    "notes": "42 UNESCO World Heritage Sites; incredible diversity of attractions; medical tourism growing ($9B); spiritual/yoga tourism; Incredible India campaign; domestic tourism massive (2B+ trips/year)."
  },
  "legal_system": {
    "type": "Common law",
    "supreme_court": "Supreme Court of India",
    "international_court_jurisdiction": "ICJ accepted (with reservations)",
    "suffrage": "18 years, universal",
    "legal_traditions": ["English common law", "Hindu personal law", "Muslim personal law", "Customary law"],
    "death_penalty": True,
    "notes": "World's largest democracy; independent judiciary (activist Supreme Court); PIL (Public Interest Litigation) unique; sedition law repealed 2023; CAA and farm laws controversies; personal law system (Hindu/Muslim/Christian)."
  },
  "human_rights_gender": {
    "freedom_house_score": 66,
    "freedom_house_status": "Partly Free",
    "gender_inequality_index": 0.437,
    "gender_inequality_rank": 108,
    "women_in_parliament_pct": 15,
    "female_labor_force_participation_pct": 24,
    "maternal_leave_weeks": 26,
    "child_marriage_pct": 23,
    "lgbtq_legal_status": "Legal (Section 377 struck down 2018; no marriage recognition)",
    "press_freedom_rank": 159,
    "notes": "World's largest democracy but declining press freedom; Section 377 decriminalized 2018; gender-based violence concern (Nirbhaya case); caste discrimination; religious polarization; Women's Reservation Bill passed 2023."
  },
  "security_stability": {
    "global_peace_index_score": 2.315,
    "global_peace_index_rank": 126,
    "homicide_rate_per_100k": 3.0,
    "terrorism_index_score": 7.2,
    "terrorism_index_rank": 13,
    "armed_conflict": True,
    "internally_displaced_persons": 631000,
    "landmine_contamination": True,
    "notes": "Nuclear weapons state; Kashmir conflict and Line of Control; Naxalite-Maoist insurgency; India-China LAC tensions (Ladakh); northeast insurgencies declining; world's 4th largest military budget; border disputes with Pakistan and China."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Yoga", "Kumbh Mela", "Ramlila", "Vedic chanting", "Classical dance traditions (Bharatanatyam, Kathak, etc.)"],
    "notable_cultural_exports": ["Bollywood", "Yoga", "Ayurveda", "Spices", "IT services", "Cricket"],
    "major_museums": ["National Museum (Delhi)", "Indian Museum (Kolkata)", "Chhatrapati Shivaji Museum (Mumbai)", "Salar Jung Museum"],
    "world_heritage_sites_list": ["Taj Mahal", "Ajanta Caves", "Ellora Caves", "Hampi", "Khajuraho", "Red Fort", "Kaziranga", "Sundarbans"],
    "culinary_traditions": ["Biryani", "Dosa", "Butter chicken", "Curry", "Samosa", "Masala chai", "Roti"],
    "notes": "One of world's oldest civilisations (Indus Valley, 3300 BCE); birthplace of Hinduism, Buddhism, Jainism, Sikhism; Sanskrit literature; zero and decimal system; Bollywood largest film industry by output."
  },
  "comparative_rankings": {
    "human_development_index_rank": 134,
    "global_competitiveness_rank": 40,
    "happiness_index_rank": 126,
    "environmental_performance_rank": 180,
    "gender_gap_rank": 127,
    "soft_power_rank": 0,
    "notes": "5th largest economy but low per-capita rankings; demographic dividend; space programme (Chandrayaan-3 Moon landing 2023); IT and pharmaceutical powerhouse; environmental challenges acute."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.91,
    "ict_development_index": 3.5,
    "mobile_money_accounts": 500000000,
    "digital_payments_pct_adults": 40,
    "fintech_companies": 4000,
    "startup_ecosystem_value_usd": "$300 billion",
    "data_protection_law": True,
    "cybersecurity_index_score": 63.0,
    "innovation_index_score": 38.0,
    "innovation_index_rank": 40,
    "ai_readiness_index": 60.0
  }
},

"indonesia": {
  "_basics": {
    "capital_coordinates": {"lat": -6.2088, "lon": 106.8456},
    "other_major_cities": ["Surabaya", "Bandung", "Medan", "Semarang", "Makassar", "Palembang", "Yogyakarta"],
    "national_motto": "Bhinneka Tunggal Ika (Unity in Diversity)",
    "national_anthem": "Indonesia Raya (Great Indonesia)",
    "currency_code": "IDR",
    "internet_tld": ".id",
    "utc_offset": "UTC+7 to UTC+9 (3 time zones)",
    "drives_on": "left",
    "other_languages": ["Javanese", "Sundanese", "Madurese", "Minangkabau", "Batak", "Balinese", "Buginese"]
  },
  "geography": {
    "coordinates": {"lat": -0.7893, "lon": 113.9213},
    "bounding_box": {"north": 5.91, "south": -11.01, "east": 141.02, "west": 95.01},
    "land_area_km2": 1904569,
    "water_area_km2": 93000,
    "coastline_km": 54716,
    "borders": ["Malaysia", "Papua New Guinea", "Timor-Leste"],
    "border_lengths_km": {"Malaysia": 1881, "Papua New Guinea": 824, "Timor-Leste": 253},
    "highest_point": {"name": "Puncak Jaya (Carstensz Pyramid)", "elevation_m": 4884},
    "lowest_point": {"name": "Indian Ocean", "elevation_m": 0},
    "terrain": "World's largest archipelago (17,000+ islands); volcanic mountains, tropical lowlands, dense rainforest",
    "land_use": {"agricultural_pct": 31.2, "arable_pct": 13.0, "forest_pct": 49.1, "other_pct": 19.7},
    "major_rivers": ["Kapuas", "Mahakam", "Barito", "Musi", "Citarum"],
    "major_lakes": ["Lake Toba (world's largest volcanic lake)", "Sentani"],
    "exclusive_economic_zone_km2": 6159032,
    "landlocked": False,
    "notes": "World's largest archipelago (17,508 islands, 6,000 inhabited); Ring of Fire (active volcanoes 127); Krakatoa 1883 eruption; 2004 Indian Ocean tsunami; Borneo/Sumatra/Java/Papua; new capital Nusantara (IKN) under construction."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$1.42 trillion",
    "gdp_ppp_usd": "$4.4 trillion",
    "gdp_per_capita_nominal_usd": 5100,
    "gdp_per_capita_ppp_usd": 15800,
    "gdp_growth_rate_pct": 5.0,
    "inflation_rate_pct": 3.6,
    "unemployment_rate_pct": 5.3,
    "youth_unemployment_rate_pct": 14.0,
    "poverty_rate_pct": 9.4,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 37.9,
    "income_classification": "Upper-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 13, "industry_pct_gdp": 40, "services_pct_gdp": 47},
    "labor_force": 140000000,
    "labor_force_by_sector": {"agriculture_pct": 28, "industry_pct": 22, "services_pct": 50},
    "fdi_inflow_usd": "$22 billion",
    "fdi_outflow_usd": "$5 billion",
    "foreign_exchange_reserves_usd": "$137 billion",
    "ease_of_doing_business_rank": 73,
    "economic_freedom_index_score": 60.7,
    "credit_rating": {"moodys": "Baa2", "sp": "BBB", "fitch": "BBB"},
    "notes": "G20 member; SE Asia's largest economy; world's largest palm oil producer; nickel dominant (EV battery supply chain); digital economy booming (GoTo, Tokopedia); new capital Nusantara (IKN); commodity-driven growth."
  },
  "health": {
    "health_expenditure_pct_gdp": 3.4,
    "health_expenditure_per_capita_usd": 148,
    "physicians_per_1k": 0.6,
    "nurses_midwives_per_1k": 2.4,
    "hospital_beds_per_1k": 1.0,
    "maternal_mortality_per_100k": 173,
    "hiv_prevalence_pct": 0.4,
    "malaria_incidence_per_1k": 2,
    "tuberculosis_incidence_per_100k": 354,
    "access_to_clean_water_pct": 92,
    "access_to_sanitation_pct": 80,
    "vaccination_coverage_pct": 80,
    "stunting_under5_pct": 22,
    "obesity_rate_pct": 6.9,
    "universal_health_coverage_index": 57,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Tuberculosis", "Chronic respiratory diseases"],
    "notes": "JKN (Jaminan Kesehatan Nasional) — world's largest single-payer health insurance (90% coverage); TB burden world's 2nd highest; stunting reduction national priority; rural access challenges across archipelago."
  },
  "food_agriculture": {
    "food_security_index_score": 54.0,
    "food_security_index_rank": 73,
    "arable_land_pct": 13.0,
    "agricultural_land_pct": 31.2,
    "irrigated_land_pct": 15,
    "major_crops": ["palm oil", "rice", "rubber", "cocoa", "coffee", "tea", "sugarcane", "cloves", "nutmeg"],
    "major_livestock": ["cattle", "poultry", "goats"],
    "food_import_dependency_pct": 10,
    "cereal_yield_kg_per_hectare": 5200,
    "agricultural_employment_pct": 28,
    "notes": "World's #1 palm oil producer (60% global share); spice islands heritage (Maluku); 3rd largest rice producer; coffee (Sumatra, Java) globally renowned; deforestation for palm oil plantations major environmental concern."
  },
  "energy": {
    "primary_energy_sources": ["coal", "oil", "natural gas", "geothermal", "hydropower", "solar"],
    "electricity_generation_gwh": 310000,
    "electricity_consumption_per_capita_kwh": 1100,
    "renewable_share_pct": 14,
    "fossil_fuel_share_pct": 86,
    "nuclear_share_pct": 0,
    "oil_production_bpd": 640000,
    "oil_consumption_bpd": 1700000,
    "natural_gas_production_bcm": 60,
    "proved_oil_reserves_bbl": "2.4 billion",
    "proved_gas_reserves_tcm": "1.41",
    "energy_imports_pct": 15,
    "electrification_rate_pct": 99,
    "notes": "World's #1 coal exporter; left OPEC (net oil importer); world's largest geothermal capacity (2.4 GW); nickel processing boom increasing energy demand; JETP $20B green energy transition deal; biomass potential vast."
  },
  "transport": {
    "airports": 673,
    "airports_paved": 186,
    "railways_km": 8159,
    "roadways_km": 496607,
    "paved_roads_pct": 56,
    "waterways_km": 21579,
    "major_ports": ["Tanjung Priok (Jakarta)", "Tanjung Perak (Surabaya)", "Belawan (Medan)", "Makassar"],
    "national_airline": "Garuda Indonesia",
    "vehicle_ownership_per_1k": 120,
    "notes": "Archipelago transport challenges; Lion Air and Garuda Indonesia main airlines; Jakarta MRT (2019); Trans-Java toll road; inter-island ferries critical; Jakarta among world's worst traffic congestion."
  },
  "tourism": {
    "international_arrivals": 11700000,
    "tourism_revenue_usd": "$10 billion",
    "tourism_pct_gdp": 0.7,
    "major_attractions": ["Bali", "Borobudur (UNESCO)", "Komodo National Park (UNESCO)", "Raja Ampat", "Yogyakarta", "Lake Toba"],
    "unesco_world_heritage_sites": 9,
    "notes": "Bali among world's top tourist destinations; Borobudur world's largest Buddhist temple; Komodo dragons unique; Raja Ampat marine biodiversity; super priority destinations programme; digital nomad visa."
  },
  "legal_system": {
    "type": "Civil law",
    "supreme_court": "Supreme Court (Mahkamah Agung)",
    "international_court_jurisdiction": "ICJ not accepted (compulsory)",
    "suffrage": "17 years or married, universal",
    "legal_traditions": ["Dutch colonial civil law", "Islamic law (Aceh province)", "Customary law (adat)"],
    "death_penalty": True,
    "notes": "Pancasila state ideology; 2024 Criminal Code overhaul (controversial — criminalizes cohabitation, insults president); Aceh province implements Sharia law; Constitutional Court independent but controversy (2023 election age ruling)."
  },
  "human_rights_gender": {
    "freedom_house_score": 58,
    "freedom_house_status": "Partly Free",
    "gender_inequality_index": 0.444,
    "gender_inequality_rank": 110,
    "women_in_parliament_pct": 22,
    "female_labor_force_participation_pct": 54,
    "maternal_leave_weeks": 13,
    "child_marriage_pct": 11,
    "lgbtq_legal_status": "Legal (except Aceh; social stigma high)",
    "press_freedom_rank": 111,
    "notes": "World's 3rd largest democracy; Aceh Sharia law (public caning for homosexuality); West Papua indigenous rights concerns; ITE law restricts online speech; domestic worker exploitation (Gulf migration); progressive women's movements."
  },
  "security_stability": {
    "global_peace_index_score": 1.823,
    "global_peace_index_rank": 49,
    "homicide_rate_per_100k": 0.4,
    "terrorism_index_score": 4.4,
    "terrorism_index_rank": 42,
    "armed_conflict": True,
    "internally_displaced_persons": 72000,
    "landmine_contamination": False,
    "notes": "Low-level insurgency in Papua; Jemaah Islamiyah dismantled (Bali bombings 2002); BNPT counter-terrorism effective; maritime piracy Malacca Strait; natural disaster vulnerability (Ring of Fire, tsunamis); South China Sea tensions."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Wayang (puppet theatre)", "Batik", "Angklung", "Pencak silat", "Gamelan"],
    "notable_cultural_exports": ["Batik textiles", "Gamelan music", "Wayang puppetry", "Coffee (Java/Sumatra)", "Spices"],
    "major_museums": ["National Museum of Indonesia", "Museum Nasional", "Ullen Sentalu (Yogyakarta)"],
    "world_heritage_sites_list": ["Borobudur Temple", "Prambanan Temple", "Komodo National Park", "Ujung Kulon", "Sangiran Early Man Site"],
    "culinary_traditions": ["Nasi goreng", "Rendang", "Satay", "Gado-gado", "Soto", "Bakso"],
    "notes": "Rendang named 'world's most delicious food' (CNN poll); most populous Muslim-majority nation; Borobudur world's largest Buddhist monument; 700+ languages; batik UNESCO heritage; spice trade shaped world history."
  },
  "comparative_rankings": {
    "human_development_index_rank": 112,
    "global_competitiveness_rank": 50,
    "happiness_index_rank": 80,
    "environmental_performance_rank": 97,
    "gender_gap_rank": 87,
    "soft_power_rank": 0,
    "notes": "SE Asia's largest economy; G20; world's 4th most populous country; nickel processing making it critical in EV supply chain; 2045 'Golden Indonesia Vision'."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.80,
    "ict_development_index": 4.3,
    "mobile_money_accounts": 50000000,
    "digital_payments_pct_adults": 35,
    "fintech_companies": 500,
    "startup_ecosystem_value_usd": "$80 billion",
    "data_protection_law": True,
    "cybersecurity_index_score": 48.0,
    "innovation_index_score": 28.0,
    "innovation_index_rank": 61,
    "ai_readiness_index": 45.0
  }
},

"iran": {
  "_basics": {
    "capital_coordinates": {"lat": 35.6892, "lon": 51.3890},
    "other_major_cities": ["Isfahan", "Mashhad", "Tabriz", "Shiraz", "Ahvaz", "Kerman", "Qom"],
    "national_motto": "Independence, Freedom, Islamic Republic",
    "national_anthem": "Soroud-e Jomhouri-ye Eslami-ye Iran",
    "currency_code": "IRR",
    "internet_tld": ".ir",
    "utc_offset": "UTC+3:30",
    "drives_on": "right",
    "other_languages": ["Azerbaijani (Turkish)", "Kurdish", "Luri", "Balochi", "Arabic", "Turkmen", "Gilaki", "Mazandarani"]
  },
  "geography": {
    "coordinates": {"lat": 32.4279, "lon": 53.6880},
    "bounding_box": {"north": 39.78, "south": 25.06, "east": 63.32, "west": 44.05},
    "land_area_km2": 1648195,
    "water_area_km2": 116600,
    "coastline_km": 2440,
    "borders": ["Afghanistan", "Armenia", "Azerbaijan", "Iraq", "Pakistan", "Turkey", "Turkmenistan"],
    "border_lengths_km": {"Afghanistan": 921, "Armenia": 44, "Azerbaijan": 689, "Iraq": 1599, "Pakistan": 959, "Turkey": 534, "Turkmenistan": 1148},
    "highest_point": {"name": "Mount Damavand", "elevation_m": 5671},
    "lowest_point": {"name": "Caspian Sea", "elevation_m": -28},
    "terrain": "Central plateau surrounded by mountains (Zagros west, Alborz north); deserts (Dasht-e Kavir, Dasht-e Lut); Caspian coast; Persian Gulf coast",
    "land_use": {"agricultural_pct": 30.1, "arable_pct": 10.7, "forest_pct": 6.8, "other_pct": 63.1},
    "major_rivers": ["Karun", "Karkheh", "Zayandeh Rud"],
    "major_lakes": ["Lake Urmia (shrinking)", "Caspian Sea"],
    "exclusive_economic_zone_km2": 168718,
    "landlocked": False,
    "notes": "18th largest country; Dasht-e Lut hottest recorded surface temperature (70.7°C); Lake Urmia ecological disaster (lost 80% volume); Strait of Hormuz controls 20% of world oil; seismically active (Bam 2003 earthquake, 30,000 killed)."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$401 billion",
    "gdp_ppp_usd": "$1.6 trillion",
    "gdp_per_capita_nominal_usd": 4700,
    "gdp_per_capita_ppp_usd": 18700,
    "gdp_growth_rate_pct": 5.4,
    "inflation_rate_pct": 40.0,
    "unemployment_rate_pct": 9.0,
    "youth_unemployment_rate_pct": 27.0,
    "poverty_rate_pct": 18.0,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 40.8,
    "income_classification": "Lower-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 12, "industry_pct_gdp": 35, "services_pct_gdp": 53},
    "labor_force": 27000000,
    "labor_force_by_sector": {"agriculture_pct": 18, "industry_pct": 35, "services_pct": 47},
    "fdi_inflow_usd": "$1.5 billion",
    "fdi_outflow_usd": "$200 million",
    "foreign_exchange_reserves_usd": "$30 billion (estimated)",
    "ease_of_doing_business_rank": 127,
    "economic_freedom_index_score": 41.7,
    "credit_rating": {"moodys": "", "sp": "", "fitch": ""},
    "notes": "Crippled by US/EU sanctions (re-imposed 2018); world's 3rd/4th largest oil reserves; 2nd largest gas reserves; 'resistance economy' policy; massive brain drain; rial lost 90%+ value since 2015; IRGC controls 30%+ of economy."
  },
  "health": {
    "health_expenditure_pct_gdp": 7.0,
    "health_expenditure_per_capita_usd": 350,
    "physicians_per_1k": 1.6,
    "nurses_midwives_per_1k": 2.4,
    "hospital_beds_per_1k": 1.6,
    "maternal_mortality_per_100k": 22,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 14,
    "access_to_clean_water_pct": 97,
    "access_to_sanitation_pct": 92,
    "vaccination_coverage_pct": 98,
    "stunting_under5_pct": 5,
    "obesity_rate_pct": 25.8,
    "universal_health_coverage_index": 65,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Road injuries", "Diabetes"],
    "notes": "Advanced healthcare for region; sanctions impact medicine/equipment imports; COVIran Barekat locally developed COVID vaccine; road traffic deaths among world's highest; thalassemia screening programme; medical tourism (nose jobs capital of world)."
  },
  "food_agriculture": {
    "food_security_index_score": 52.0,
    "food_security_index_rank": 77,
    "arable_land_pct": 10.7,
    "agricultural_land_pct": 30.1,
    "irrigated_land_pct": 50,
    "major_crops": ["wheat", "rice", "barley", "pistachios", "saffron", "dates", "pomegranates", "citrus"],
    "major_livestock": ["sheep", "goats", "cattle", "poultry"],
    "food_import_dependency_pct": 20,
    "cereal_yield_kg_per_hectare": 3100,
    "agricultural_employment_pct": 18,
    "notes": "World's #1 saffron producer (90%+ global share); #1 pistachio producer; pomegranate and date exports significant; water crisis threatening agriculture (aquifer depletion); qanat irrigation systems (UNESCO heritage)."
  },
  "energy": {
    "primary_energy_sources": ["oil", "natural gas", "hydropower"],
    "electricity_generation_gwh": 370000,
    "electricity_consumption_per_capita_kwh": 3600,
    "renewable_share_pct": 7,
    "fossil_fuel_share_pct": 93,
    "nuclear_share_pct": 2,
    "oil_production_bpd": 3200000,
    "oil_consumption_bpd": 1800000,
    "natural_gas_production_bcm": 260,
    "proved_oil_reserves_bbl": "157 billion",
    "proved_gas_reserves_tcm": "34",
    "energy_imports_pct": 0,
    "electrification_rate_pct": 100,
    "notes": "World's 4th largest oil reserves, 2nd largest gas reserves (South Pars/North Dome); Bushehr nuclear plant; JCPOA nuclear deal collapsed; sanctions limit oil exports; massive gas flaring; energy subsidies consume 12%+ GDP."
  },
  "transport": {
    "airports": 319,
    "airports_paved": 140,
    "railways_km": 14000,
    "roadways_km": 223485,
    "paved_roads_pct": 73,
    "waterways_km": 850,
    "major_ports": ["Bandar Abbas", "Bushehr", "Chabahar", "Bandar Imam Khomeini"],
    "national_airline": "Iran Air",
    "vehicle_ownership_per_1k": 230,
    "notes": "Sanctions impact aviation (aged fleet, safety concerns); rail network being expanded; Chabahar Port (India-funded, bypasses Pakistan); INSTC (International North-South Transport Corridor); world's highest road fatality rate."
  },
  "tourism": {
    "international_arrivals": 4800000,
    "tourism_revenue_usd": "$5 billion",
    "tourism_pct_gdp": 1.2,
    "major_attractions": ["Isfahan (Naqsh-e Jahan Square, UNESCO)", "Persepolis (UNESCO)", "Shiraz (Hafez/Saadi tombs)", "Yazd (UNESCO)", "Tehran Grand Bazaar"],
    "unesco_world_heritage_sites": 27,
    "notes": "27 UNESCO World Heritage Sites (10th most globally); enormous potential limited by sanctions, visa restrictions, mandatory hijab; Persian hospitality renowned; 7,000+ year civilisational heritage; medical/health tourism growing."
  },
  "legal_system": {
    "type": "Islamic (theocratic) legal system",
    "supreme_court": "Supreme Court of Iran",
    "international_court_jurisdiction": "ICJ accepted (limited)",
    "suffrage": "15 years (lowered from 18), universal",
    "legal_traditions": ["Shia (Twelver) Islamic jurisprudence (Jafari school)", "Continental civil law elements"],
    "death_penalty": True,
    "notes": "Velayat-e faqih (guardianship of the jurist) system; Guardian Council vets all candidates; Supreme Leader above all; second highest executions globally (after China); morality police; Mahsa Amini protests 2022."
  },
  "human_rights_gender": {
    "freedom_house_score": 14,
    "freedom_house_status": "Not Free",
    "gender_inequality_index": 0.459,
    "gender_inequality_rank": 113,
    "women_in_parliament_pct": 6,
    "female_labor_force_participation_pct": 15,
    "maternal_leave_weeks": 9,
    "child_marriage_pct": 17,
    "lgbtq_legal_status": "Illegal (death penalty)",
    "press_freedom_rank": 176,
    "notes": "Mahsa Amini protests (2022) — 'Woman, Life, Freedom' movement; mandatory hijab enforcement; LGBTQ+ executions; massive internet shutdowns; political prisoners; journalist/activist detentions; theocratic control of all aspects of life."
  },
  "security_stability": {
    "global_peace_index_score": 2.797,
    "global_peace_index_rank": 147,
    "homicide_rate_per_100k": 2.5,
    "terrorism_index_score": 4.8,
    "terrorism_index_rank": 38,
    "armed_conflict": True,
    "internally_displaced_persons": 0,
    "landmine_contamination": True,
    "notes": "Regional power projection (proxy forces in Iraq, Syria, Lebanon, Yemen — 'Axis of Resistance'); IRGC-Quds Force; nuclear programme (JCPOA collapsed); US-Iran tensions; Kurdish insurgency (PJAK); Baloch insurgency; Israel-Iran shadow war."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Nowruz", "Radif of Iranian music", "Ta'ziye", "Persian carpet weaving", "Qanat irrigation"],
    "notable_cultural_exports": ["Persian carpets", "Saffron", "Poetry (Hafez, Rumi, Ferdowsi)", "Cinema (Kiarostami, Farhadi)", "Miniature painting"],
    "major_museums": ["National Museum of Iran", "Golestan Palace", "Iran National Jewelry Treasury", "Persepolis Museum"],
    "world_heritage_sites_list": ["Persepolis", "Naqsh-e Jahan Square (Isfahan)", "Tchogha Zanbil", "Meidan Emam", "Pasargadae", "Golestan Palace", "Historic City of Yazd"],
    "culinary_traditions": ["Chelow kebab", "Ghormeh sabzi", "Tahdig", "Fesenjan", "Ash reshteh"],
    "notes": "Persian Empire (550 BCE) one of history's largest; Persian language literary tradition (Shahnameh, Hafez, Rumi); Zoroastrianism originated here; Persian gardens (UNESCO); cinema internationally acclaimed despite censorship."
  },
  "comparative_rankings": {
    "human_development_index_rank": 76,
    "global_competitiveness_rank": 99,
    "happiness_index_rank": 100,
    "environmental_performance_rank": 170,
    "gender_gap_rank": 143,
    "soft_power_rank": 0,
    "notes": "Enormous potential undermined by sanctions, isolation, and theocratic governance; high HDI for region despite sanctions; brain drain massive (highest globally); cultural/civilisational soft power significant."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.65,
    "ict_development_index": 4.5,
    "mobile_money_accounts": 20000000,
    "digital_payments_pct_adults": 65,
    "fintech_companies": 100,
    "startup_ecosystem_value_usd": "$1 billion",
    "data_protection_law": False,
    "cybersecurity_index_score": 45.0,
    "innovation_index_score": 33.0,
    "innovation_index_rank": 62,
    "ai_readiness_index": 35.0
  }
},

"iraq": {
  "_basics": {
    "capital_coordinates": {"lat": 33.3128, "lon": 44.3615},
    "other_major_cities": ["Basra", "Erbil", "Mosul", "Sulaymaniyah", "Najaf", "Karbala"],
    "national_motto": "God is the Greatest (Allahu Akbar)",
    "national_anthem": "Mawtini (My Homeland)",
    "currency_code": "IQD",
    "internet_tld": ".iq",
    "utc_offset": "UTC+3",
    "drives_on": "right",
    "other_languages": ["Kurdish (Sorani, Kurmanji)", "Turkmen", "Assyrian Neo-Aramaic"]
  },
  "geography": {
    "coordinates": {"lat": 33.2232, "lon": 43.6793},
    "bounding_box": {"north": 37.38, "south": 29.06, "east": 48.57, "west": 38.79},
    "land_area_km2": 438317,
    "water_area_km2": 950,
    "coastline_km": 58,
    "borders": ["Turkey", "Iran", "Kuwait", "Saudi Arabia", "Jordan", "Syria"],
    "border_lengths_km": {"Turkey": 367, "Iran": 1599, "Kuwait": 254, "Saudi Arabia": 811, "Jordan": 179, "Syria": 599},
    "highest_point": {"name": "Cheekha Dar (Haji Ibrahim)", "elevation_m": 3611},
    "lowest_point": {"name": "Persian Gulf", "elevation_m": 0},
    "terrain": "Alluvial plains of Tigris-Euphrates (Mesopotamia); mountains in northeast (Kurdistan); desert west/south",
    "land_use": {"agricultural_pct": 18.1, "arable_pct": 8.4, "forest_pct": 1.9, "other_pct": 80.0},
    "major_rivers": ["Tigris", "Euphrates", "Shatt al-Arab"],
    "major_lakes": ["Lake Tharthar", "Lake Habbaniyah"],
    "exclusive_economic_zone_km2": 0,
    "landlocked": False,
    "notes": "Cradle of civilisation (Mesopotamia); Tigris-Euphrates river system; Marshlands of southern Iraq (UNESCO — partly restored after Saddam's draining); Kurdistan Region semi-autonomous."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$264 billion",
    "gdp_ppp_usd": "$512 billion",
    "gdp_per_capita_nominal_usd": 6000,
    "gdp_per_capita_ppp_usd": 11600,
    "gdp_growth_rate_pct": -2.9,
    "inflation_rate_pct": 5.0,
    "unemployment_rate_pct": 15.5,
    "youth_unemployment_rate_pct": 36.0,
    "poverty_rate_pct": 23.0,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 29.5,
    "income_classification": "Upper-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 3, "industry_pct_gdp": 62, "services_pct_gdp": 35},
    "labor_force": 10000000,
    "labor_force_by_sector": {"agriculture_pct": 20, "industry_pct": 18, "services_pct": 62},
    "fdi_inflow_usd": "$8 billion",
    "fdi_outflow_usd": "$300 million",
    "foreign_exchange_reserves_usd": "$100 billion",
    "ease_of_doing_business_rank": 172,
    "economic_freedom_index_score": 42.0,
    "credit_rating": {"moodys": "Caa1", "sp": "B-", "fitch": "B-"},
    "notes": "Oil-dependent economy (95% government revenue, 99% exports); 5th largest oil reserves globally; post-ISIS reconstruction ongoing; Kurdistan Region separate economy; massive public sector employment; Development Road project (Grand Faw Port)."
  },
  "health": {
    "health_expenditure_pct_gdp": 4.6,
    "health_expenditure_per_capita_usd": 240,
    "physicians_per_1k": 0.8,
    "nurses_midwives_per_1k": 1.8,
    "hospital_beds_per_1k": 1.3,
    "maternal_mortality_per_100k": 76,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 31,
    "access_to_clean_water_pct": 86,
    "access_to_sanitation_pct": 88,
    "vaccination_coverage_pct": 70,
    "stunting_under5_pct": 11,
    "obesity_rate_pct": 30.4,
    "universal_health_coverage_index": 48,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Road injuries", "Conflict-related"],
    "notes": "Healthcare devastated by sanctions (1990s), 2003 invasion, and ISIS conflict; massive brain drain of doctors; sectarian-divided health system; Kurdistan Region better healthcare; depleted uranium health effects debated."
  },
  "food_agriculture": {
    "food_security_index_score": 45.0,
    "food_security_index_rank": 90,
    "arable_land_pct": 8.4,
    "agricultural_land_pct": 18.1,
    "irrigated_land_pct": 65,
    "major_crops": ["wheat", "barley", "rice", "dates", "vegetables"],
    "major_livestock": ["sheep", "goats", "cattle", "poultry"],
    "food_import_dependency_pct": 60,
    "cereal_yield_kg_per_hectare": 2200,
    "agricultural_employment_pct": 20,
    "notes": "Once 'breadbasket of the Middle East'; dates #1 export crop (7th global producer); salinization and desertification devastating agricultural land; Turkish/Iranian upstream dams reducing Tigris-Euphrates water flow; food import dependent."
  },
  "energy": {
    "primary_energy_sources": ["oil", "natural gas"],
    "electricity_generation_gwh": 90000,
    "electricity_consumption_per_capita_kwh": 1700,
    "renewable_share_pct": 2,
    "fossil_fuel_share_pct": 98,
    "nuclear_share_pct": 0,
    "oil_production_bpd": 4400000,
    "oil_consumption_bpd": 800000,
    "natural_gas_production_bcm": 10,
    "proved_oil_reserves_bbl": "145 billion",
    "proved_gas_reserves_tcm": "3.7",
    "energy_imports_pct": 0,
    "electrification_rate_pct": 100,
    "notes": "OPEC 2nd largest producer; flares enormous gas volumes (world's 2nd highest); 12-16 hours daily power cuts despite oil wealth; Iran gas imports for electricity; TotalEnergies $27B gas capture mega-project; Kurdistan Region separate oil exports."
  },
  "transport": {
    "airports": 104,
    "airports_paved": 75,
    "railways_km": 2272,
    "roadways_km": 59623,
    "paved_roads_pct": 74,
    "waterways_km": 5279,
    "major_ports": ["Umm Qasr", "Basra", "Grand Faw (under construction)"],
    "national_airline": "Iraqi Airways",
    "vehicle_ownership_per_1k": 150,
    "notes": "Infrastructure decimated by wars; Development Road mega-project (Grand Faw Port to Turkey rail/road corridor); Basra-Baghdad highway; Baghdad International Airport; waterways important for oil export; bridge reconstruction ongoing."
  },
  "tourism": {
    "international_arrivals": 3200000,
    "tourism_revenue_usd": "$5.5 billion",
    "tourism_pct_gdp": 2.1,
    "major_attractions": ["Babylon (UNESCO)", "Erbil Citadel (UNESCO)", "Najaf/Karbala holy cities", "Iraqi Kurdistan mountains", "Marshes of Southern Iraq (UNESCO)"],
    "unesco_world_heritage_sites": 6,
    "notes": "Shia pilgrimage tourism dominant (Karbala ~20M visitors for Arba'een — world's largest annual gathering); Kurdistan Region adventure tourism; Babylon restored (UNESCO 2019); ancient Mesopotamian sites; security concerns limit general tourism."
  },
  "legal_system": {
    "type": "Mixed legal system",
    "supreme_court": "Federal Supreme Court",
    "international_court_jurisdiction": "ICJ not accepted",
    "suffrage": "18 years, universal",
    "legal_traditions": ["Civil law", "Islamic law (source of legislation per constitution)", "tribal customary law"],
    "death_penalty": True,
    "notes": "2005 constitution; federal system with Kurdistan Region autonomy; Article 2 (Islam a source of legislation); sectarian power-sharing (muhasasa); judiciary political interference; honour killings under-prosecuted."
  },
  "human_rights_gender": {
    "freedom_house_score": 29,
    "freedom_house_status": "Not Free",
    "gender_inequality_index": 0.540,
    "gender_inequality_rank": 134,
    "women_in_parliament_pct": 29,
    "female_labor_force_participation_pct": 12,
    "maternal_leave_weeks": 9,
    "child_marriage_pct": 28,
    "lgbtq_legal_status": "Illegal (2024 amendment: up to 15 years imprisonment)",
    "press_freedom_rank": 169,
    "notes": "Post-conflict human rights challenges; 2024 anti-LGBTQ+ law (15-year sentences); honour killings; press freedom declining; Tishreen (October 2019) protest movement violently suppressed (600+ killed); Iran-backed militia influence."
  },
  "security_stability": {
    "global_peace_index_score": 2.967,
    "global_peace_index_rank": 153,
    "homicide_rate_per_100k": 9.0,
    "terrorism_index_score": 6.7,
    "terrorism_index_rank": 11,
    "armed_conflict": True,
    "internally_displaced_persons": 1200000,
    "landmine_contamination": True,
    "notes": "Post-ISIS recovery (Mosul liberated 2017); Iran-backed PMF/Hashd dominance; US military presence (~2,500); Turkish operations in Kurdistan; ISIS sleeper cells; massive UXO/IED contamination; sectarian tensions persist."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Iraqi Maqam", "Khidr Elias ceremony"],
    "notable_cultural_exports": ["Mesopotamian heritage (Sumerian, Babylonian, Assyrian)", "Oud music", "Arabic calligraphy", "Dates"],
    "major_museums": ["Iraq Museum (Baghdad)", "Erbil Civilisation Museum", "Basra Museum"],
    "world_heritage_sites_list": ["Hatra", "Ashur", "Samarra Archaeological City", "Babylon", "Erbil Citadel", "The Ahwar (Marshlands)"],
    "culinary_traditions": ["Masgouf (grilled fish)", "Dolma", "Biryani", "Kleicha (date cookies)", "Kubba"],
    "notes": "Mesopotamia: 'cradle of civilisation'; writing invented here (cuneiform, ~3400 BCE); Code of Hammurabi; Hanging Gardens of Babylon (one of Seven Wonders); Abbasid Caliphate (Baghdad golden age); ISIS destroyed Nimrud, Palmyra damaged."
  },
  "comparative_rankings": {
    "human_development_index_rank": 121,
    "global_competitiveness_rank": 130,
    "happiness_index_rank": 106,
    "environmental_performance_rank": 164,
    "gender_gap_rank": 152,
    "soft_power_rank": 0,
    "notes": "Oil-rich but conflict-devastated; enormous reconstruction needs; Kurdistan Region better indicators than federal Iraq; ancient civilisational heritage underexplored."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.35,
    "ict_development_index": 2.8,
    "mobile_money_accounts": 3000000,
    "digital_payments_pct_adults": 15,
    "fintech_companies": 30,
    "startup_ecosystem_value_usd": "$200 million",
    "data_protection_law": False,
    "cybersecurity_index_score": 20.0,
    "innovation_index_score": 15.0,
    "innovation_index_rank": 0,
    "ai_readiness_index": 20.0
  }
},

"israel": {
  "_basics": {
    "capital_coordinates": {"lat": 31.7683, "lon": 35.2137},
    "other_major_cities": ["Tel Aviv-Yafo", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod", "Beer Sheva"],
    "national_motto": "None officially",
    "national_anthem": "Hatikvah (The Hope)",
    "currency_code": "ILS",
    "internet_tld": ".il",
    "utc_offset": "UTC+2 (UTC+3 summer)",
    "drives_on": "right",
    "other_languages": ["Arabic", "English", "Russian", "Amharic", "French"]
  },
  "geography": {
    "coordinates": {"lat": 31.0461, "lon": 34.8516},
    "bounding_box": {"north": 33.33, "south": 29.48, "east": 35.90, "west": 34.27},
    "land_area_km2": 22072,
    "water_area_km2": 440,
    "coastline_km": 273,
    "borders": ["Lebanon", "Syria", "Jordan", "Egypt", "West Bank", "Gaza Strip"],
    "border_lengths_km": {"Lebanon": 81, "Syria": 83, "Jordan": 307, "Egypt": 208},
    "highest_point": {"name": "Mount Meron", "elevation_m": 1208},
    "lowest_point": {"name": "Dead Sea", "elevation_m": -431},
    "terrain": "Coastal plain; central highlands; Jordan Rift Valley; Negev desert (60% of land area)",
    "land_use": {"agricultural_pct": 23.8, "arable_pct": 13.7, "forest_pct": 7.1, "other_pct": 69.1},
    "major_rivers": ["Jordan"],
    "major_lakes": ["Dead Sea (world's lowest point)", "Sea of Galilee (Kinneret)"],
    "exclusive_economic_zone_km2": 26000,
    "landlocked": False,
    "notes": "Dead Sea (-431m) lowest point on Earth's surface; Negev desert 60% of territory; Sea of Galilee critical freshwater source; diverse climate zones in small area; occupied territories disputed."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$530 billion",
    "gdp_ppp_usd": "$530 billion",
    "gdp_per_capita_nominal_usd": 54700,
    "gdp_per_capita_ppp_usd": 54700,
    "gdp_growth_rate_pct": 2.0,
    "inflation_rate_pct": 3.3,
    "unemployment_rate_pct": 3.4,
    "youth_unemployment_rate_pct": 7.0,
    "poverty_rate_pct": 21.0,
    "poverty_line_definition": "Relative poverty (50% median income)",
    "gini_coefficient": 38.6,
    "income_classification": "High income",
    "sector_breakdown": {"agriculture_pct_gdp": 1, "industry_pct_gdp": 19, "services_pct_gdp": 80},
    "labor_force": 4300000,
    "labor_force_by_sector": {"agriculture_pct": 1, "industry_pct": 17, "services_pct": 82},
    "fdi_inflow_usd": "$28 billion",
    "fdi_outflow_usd": "$12 billion",
    "foreign_exchange_reserves_usd": "$205 billion",
    "ease_of_doing_business_rank": 35,
    "economic_freedom_index_score": 68.1,
    "credit_rating": {"moodys": "A1", "sp": "AA-", "fitch": "A+"},
    "notes": "'Start-up Nation' — highest VC per capita globally; tech sector 18% GDP; natural gas discoveries (Leviathan, Tamar); diamond cutting/trading hub; OECD member; defense industry major exporter; economic impact of Oct 7 war significant."
  },
  "health": {
    "health_expenditure_pct_gdp": 8.3,
    "health_expenditure_per_capita_usd": 3900,
    "physicians_per_1k": 3.7,
    "nurses_midwives_per_1k": 5.1,
    "hospital_beds_per_1k": 2.9,
    "maternal_mortality_per_100k": 3,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 3,
    "access_to_clean_water_pct": 100,
    "access_to_sanitation_pct": 100,
    "vaccination_coverage_pct": 95,
    "stunting_under5_pct": 0,
    "obesity_rate_pct": 26.1,
    "universal_health_coverage_index": 88,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Diabetes", "Chronic respiratory diseases"],
    "notes": "Universal healthcare (1995 National Health Insurance Law); world leader in medical research; highest life expectancy in Middle East (83 years); world's fastest COVID vaccine rollout; Magen David Adom emergency services."
  },
  "food_agriculture": {
    "food_security_index_score": 79.0,
    "food_security_index_rank": 22,
    "arable_land_pct": 13.7,
    "agricultural_land_pct": 23.8,
    "irrigated_land_pct": 58,
    "major_crops": ["citrus", "vegetables", "cotton", "flowers", "avocados", "dates"],
    "major_livestock": ["poultry", "cattle", "sheep"],
    "food_import_dependency_pct": 50,
    "cereal_yield_kg_per_hectare": 4500,
    "agricultural_employment_pct": 1,
    "notes": "World leader in agricultural technology (drip irrigation invented by Netafim); 'made the desert bloom'; highest crop yields per hectare in many categories; agri-tech exports global; kibbutz farming tradition."
  },
  "energy": {
    "primary_energy_sources": ["natural gas", "oil", "solar", "coal"],
    "electricity_generation_gwh": 75000,
    "electricity_consumption_per_capita_kwh": 7200,
    "renewable_share_pct": 10,
    "fossil_fuel_share_pct": 90,
    "nuclear_share_pct": 0,
    "oil_production_bpd": 0,
    "oil_consumption_bpd": 230000,
    "natural_gas_production_bcm": 22,
    "proved_oil_reserves_bbl": "14 million",
    "proved_gas_reserves_tcm": "0.60",
    "energy_imports_pct": 30,
    "electrification_rate_pct": 100,
    "notes": "Leviathan and Tamar gas fields transformed from energy importer to exporter; gas exports to Egypt and Jordan; 30% renewable target by 2030; Dimona nuclear facility (undeclared nuclear arsenal); Negev solar potential."
  },
  "transport": {
    "airports": 42,
    "airports_paved": 33,
    "railways_km": 1384,
    "roadways_km": 19555,
    "paved_roads_pct": 100,
    "waterways_km": 0,
    "major_ports": ["Haifa", "Ashdod", "Eilat"],
    "national_airline": "El Al",
    "vehicle_ownership_per_1k": 370,
    "notes": "Ben Gurion Airport major hub; high-speed rail Jerusalem-Tel Aviv (A1 train); light rail systems in Jerusalem and Tel Aviv (Red Line 2023); compact country — most destinations within 1-2 hours; security-intensive aviation."
  },
  "tourism": {
    "international_arrivals": 3000000,
    "tourism_revenue_usd": "$7 billion",
    "tourism_pct_gdp": 1.3,
    "major_attractions": ["Jerusalem Old City (UNESCO)", "Western Wall", "Dead Sea", "Masada (UNESCO)", "Tel Aviv beaches", "Haifa Bahá'í Gardens"],
    "unesco_world_heritage_sites": 9,
    "notes": "Religious tourism (Christianity, Judaism, Islam); Dead Sea lowest point on Earth; Tel Aviv 'White City' (Bauhaus, UNESCO); Oct 7 war severely impacted 2024 tourism; tech tourism/conferences; Birthright programme."
  },
  "legal_system": {
    "type": "Mixed legal system",
    "supreme_court": "Supreme Court of Israel",
    "international_court_jurisdiction": "ICJ jurisdiction disputed",
    "suffrage": "18 years, universal",
    "legal_traditions": ["English common law", "Ottoman/civil law remnants", "Jewish religious law (personal status)", "Military law (occupied territories)"],
    "death_penalty": True,
    "notes": "No formal constitution (Basic Laws serve as quasi-constitution); 2023 judicial overhaul crisis (massive protests); Coalition politics (proportional representation); military court system for occupied territories; ICJ ruling on occupation (2024)."
  },
  "human_rights_gender": {
    "freedom_house_score": 74,
    "freedom_house_status": "Free",
    "gender_inequality_index": 0.084,
    "gender_inequality_rank": 19,
    "women_in_parliament_pct": 30,
    "female_labor_force_participation_pct": 62,
    "maternal_leave_weeks": 15,
    "child_marriage_pct": 0,
    "lgbtq_legal_status": "Legal (no marriage but recognition of foreign marriages; military service open)",
    "press_freedom_rank": 101,
    "notes": "Strong democracy for citizens within Green Line; West Bank/Gaza occupation human rights concerns (B'Tselem, HRW, ICJ); conscription includes women; LGBTQ+ most progressive in Middle East; settler violence; Oct 7 aftermath civil liberties debate."
  },
  "security_stability": {
    "global_peace_index_score": 2.757,
    "global_peace_index_rank": 143,
    "homicide_rate_per_100k": 1.8,
    "terrorism_index_score": 7.7,
    "terrorism_index_rank": 8,
    "armed_conflict": True,
    "internally_displaced_persons": 100000,
    "landmine_contamination": True,
    "notes": "Oct 7, 2023 Hamas attack (1,200 killed, 250 hostages); Gaza war ongoing; nuclear weapons state (undeclared, est. 80-400 warheads); Iron Dome missile defense; Hezbollah threat (north); Iran existential threat; multi-front security posture."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": [],
    "notable_cultural_exports": ["Technology/Start-ups", "Dead Sea cosmetics", "Israeli cuisine", "Hebrew language revival"],
    "major_museums": ["Israel Museum (Dead Sea Scrolls)", "Yad Vashem (Holocaust)", "Tel Aviv Museum of Art"],
    "world_heritage_sites_list": ["Old City of Acre", "White City of Tel Aviv", "Masada", "Biblical Tels", "Caves of Maresha and Bet-Guvrin", "Nahal Me'arot/Wadi el-Mughara Caves"],
    "culinary_traditions": ["Hummus", "Falafel", "Shakshuka", "Israeli salad", "Sabich", "Schnitzel"],
    "notes": "Only country to revive a dead language (Hebrew); kibbutz movement unique; Holy Land significance for Judaism, Christianity, Islam; Israeli tech culture ('chutzpah'); Dead Sea Scrolls; diverse immigrant cultures."
  },
  "comparative_rankings": {
    "human_development_index_rank": 22,
    "global_competitiveness_rank": 20,
    "happiness_index_rank": 5,
    "environmental_performance_rank": 57,
    "gender_gap_rank": 83,
    "soft_power_rank": 0,
    "notes": "Start-up Nation — highest VC per capita; top happiness despite conflict; high HDI; tech innovation powerhouse; security situation drags peace rankings; Nasdaq-listed companies (most outside US)."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.85,
    "ict_development_index": 7.1,
    "mobile_money_accounts": 3000000,
    "digital_payments_pct_adults": 80,
    "fintech_companies": 500,
    "startup_ecosystem_value_usd": "$100 billion",
    "data_protection_law": True,
    "cybersecurity_index_score": 90.0,
    "innovation_index_score": 57.0,
    "innovation_index_rank": 14,
    "ai_readiness_index": 78.0
  }
},

"japan": {
  "_basics": {
    "capital_coordinates": {"lat": 35.6762, "lon": 139.6503},
    "other_major_cities": ["Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kyoto"],
    "national_motto": "None officially",
    "national_anthem": "Kimigayo (His Imperial Majesty's Reign)",
    "currency_code": "JPY",
    "internet_tld": ".jp",
    "utc_offset": "UTC+9",
    "drives_on": "left",
    "other_languages": ["Ryukyuan languages", "Ainu"]
  },
  "geography": {
    "coordinates": {"lat": 36.2048, "lon": 138.2529},
    "bounding_box": {"north": 45.52, "south": 24.40, "east": 153.99, "west": 122.93},
    "land_area_km2": 377975,
    "water_area_km2": 13430,
    "coastline_km": 29751,
    "borders": [],
    "border_lengths_km": {},
    "highest_point": {"name": "Mount Fuji", "elevation_m": 3776},
    "lowest_point": {"name": "Hachirōgata (reclaimed land)", "elevation_m": -4},
    "terrain": "Mountainous archipelago (6,852 islands); volcanic; 73% forested; narrow coastal plains",
    "land_use": {"agricultural_pct": 12.5, "arable_pct": 11.7, "forest_pct": 68.5, "other_pct": 19.0},
    "major_rivers": ["Shinano", "Tone", "Ishikari"],
    "major_lakes": ["Lake Biwa (largest freshwater)"],
    "exclusive_economic_zone_km2": 4470000,
    "landlocked": False,
    "notes": "Ring of Fire (111 active volcanoes); world's most seismically active country; 2011 Tōhoku earthquake/tsunami/Fukushima; four main islands (Honshu, Hokkaido, Kyushu, Shikoku); 6th largest EEZ globally."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$4.2 trillion",
    "gdp_ppp_usd": "$6.5 trillion",
    "gdp_per_capita_nominal_usd": 33800,
    "gdp_per_capita_ppp_usd": 52100,
    "gdp_growth_rate_pct": 1.9,
    "inflation_rate_pct": 3.2,
    "unemployment_rate_pct": 2.6,
    "youth_unemployment_rate_pct": 3.7,
    "poverty_rate_pct": 15.4,
    "poverty_line_definition": "Relative poverty (OECD definition)",
    "gini_coefficient": 32.9,
    "income_classification": "High income",
    "sector_breakdown": {"agriculture_pct_gdp": 1, "industry_pct_gdp": 29, "services_pct_gdp": 70},
    "labor_force": 69000000,
    "labor_force_by_sector": {"agriculture_pct": 3, "industry_pct": 25, "services_pct": 72},
    "fdi_inflow_usd": "$32 billion",
    "fdi_outflow_usd": "$183 billion",
    "foreign_exchange_reserves_usd": "$1.27 trillion",
    "ease_of_doing_business_rank": 29,
    "economic_freedom_index_score": 69.3,
    "credit_rating": {"moodys": "A1", "sp": "A+", "fitch": "A"},
    "notes": "World's 4th largest economy; lost decades (1991-2010) stagnation; Abenomics; yen weakness (2022-24); automotive giant (Toyota largest global automaker); robotics leader; world's largest government debt-to-GDP ratio (260%+); aging population economic challenge."
  },
  "health": {
    "health_expenditure_pct_gdp": 11.0,
    "health_expenditure_per_capita_usd": 4700,
    "physicians_per_1k": 2.5,
    "nurses_midwives_per_1k": 12.1,
    "hospital_beds_per_1k": 12.6,
    "maternal_mortality_per_100k": 4,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 10,
    "access_to_clean_water_pct": 100,
    "access_to_sanitation_pct": 100,
    "vaccination_coverage_pct": 98,
    "stunting_under5_pct": 0,
    "obesity_rate_pct": 4.3,
    "universal_health_coverage_index": 93,
    "leading_causes_of_death": ["Cancer", "Cardiovascular diseases", "Pneumonia", "Cerebrovascular diseases"],
    "notes": "World's highest life expectancy (84+ years); universal healthcare since 1961; highest hospital beds per capita globally; aging society (29% over 65); mental health/suicide concerns; Okinawa blue zone."
  },
  "food_agriculture": {
    "food_security_index_score": 78.0,
    "food_security_index_rank": 23,
    "arable_land_pct": 11.7,
    "agricultural_land_pct": 12.5,
    "irrigated_land_pct": 54,
    "major_crops": ["rice", "vegetables", "fruits", "tea", "wheat", "soybeans"],
    "major_livestock": ["poultry", "pigs", "cattle (Wagyu)"],
    "food_import_dependency_pct": 63,
    "cereal_yield_kg_per_hectare": 6600,
    "agricultural_employment_pct": 3,
    "notes": "Only 37% food self-sufficiency (calorie basis, lowest among major economies); rice staple (declining consumption); Wagyu beef globally premium; calorie-based food self-sufficiency declining; fisheries historically important (whaling controversy)."
  },
  "energy": {
    "primary_energy_sources": ["natural gas", "coal", "oil", "nuclear", "solar", "hydropower"],
    "electricity_generation_gwh": 1000000,
    "electricity_consumption_per_capita_kwh": 7500,
    "renewable_share_pct": 22,
    "fossil_fuel_share_pct": 70,
    "nuclear_share_pct": 8,
    "oil_production_bpd": 3000,
    "oil_consumption_bpd": 3200000,
    "natural_gas_production_bcm": 2,
    "proved_oil_reserves_bbl": "44 million",
    "proved_gas_reserves_tcm": "0.02",
    "energy_imports_pct": 90,
    "electrification_rate_pct": 100,
    "notes": "World's #1 LNG importer; Fukushima disaster (2011) led nuclear shutdown — slow restart (33 of 54 reactors decommissioned); aggressive hydrogen strategy; 46% GHG reduction target by 2030; solar expansion rapid; ocean/tidal energy research."
  },
  "transport": {
    "airports": 175,
    "airports_paved": 142,
    "railways_km": 27311,
    "roadways_km": 1218772,
    "paved_roads_pct": 80,
    "waterways_km": 1770,
    "major_ports": ["Tokyo", "Yokohama", "Kobe", "Nagoya", "Osaka"],
    "national_airline": "Japan Airlines (JAL) / All Nippon Airways (ANA)",
    "vehicle_ownership_per_1k": 600,
    "notes": "Shinkansen (bullet train) since 1964 — zero fatalities; world's most punctual rail system; Tokyo Metro world's busiest; new maglev line (Chuo Shinkansen, 500 km/h) under construction; automotive nation (Toyota, Honda, Nissan)."
  },
  "tourism": {
    "international_arrivals": 25000000,
    "tourism_revenue_usd": "$33 billion",
    "tourism_pct_gdp": 0.8,
    "major_attractions": ["Tokyo", "Kyoto", "Mount Fuji", "Osaka", "Hiroshima Peace Memorial (UNESCO)", "Nara", "Fushimi Inari Shrine"],
    "unesco_world_heritage_sites": 25,
    "notes": "Record 31.9M visitors in 2023 (pre-pandemic record broken); weak yen driving tourism boom; overtourism in Kyoto; anime/manga pilgrimage tourism; cherry blossom season; food tourism (most Michelin stars globally); onsen culture."
  },
  "legal_system": {
    "type": "Civil law",
    "supreme_court": "Supreme Court of Japan",
    "international_court_jurisdiction": "ICJ accepted (compulsory, with reservations)",
    "suffrage": "18 years, universal",
    "legal_traditions": ["German-influenced civil law (Meiji era)", "Post-WWII US-influenced constitutional law"],
    "death_penalty": True,
    "notes": "1947 Constitution (drafted under US occupation); Article 9 renounces war (reinterpreted for self-defense); 99.9% conviction rate (prosecutor-driven system); Emperor purely ceremonial; Liberal Democratic Party dominated since 1955."
  },
  "human_rights_gender": {
    "freedom_house_score": 96,
    "freedom_house_status": "Free",
    "gender_inequality_index": 0.083,
    "gender_inequality_rank": 18,
    "women_in_parliament_pct": 10,
    "female_labor_force_participation_pct": 54,
    "maternal_leave_weeks": 14,
    "child_marriage_pct": 0,
    "lgbtq_legal_status": "Legal (some local partnership certificates; no national marriage)",
    "press_freedom_rank": 70,
    "notes": "Strong democracy; persistent gender gap (lowest women in STEM among OECD; 'womenomics' policies); homogeneous society (2% foreign residents, rising); death penalty retained (hanging); press club system (kisha clubs) limits press freedom."
  },
  "security_stability": {
    "global_peace_index_score": 1.336,
    "global_peace_index_rank": 9,
    "homicide_rate_per_100k": 0.2,
    "terrorism_index_score": 1.0,
    "terrorism_index_rank": 95,
    "armed_conflict": False,
    "internally_displaced_persons": 0,
    "landmine_contamination": False,
    "notes": "Among world's safest countries; Article 9 pacifist constitution but increasing militarization (2022 security strategy revision — 2% GDP defense target); US-Japan alliance cornerstone; China/North Korea threats; Senkaku/Diaoyu Islands dispute."
  },
  "cultural_heritage": {
    "unesco_intangible_heritage": ["Kabuki theatre", "Noh theatre", "Washoku (Japanese cuisine)", "Washi papermaking", "Yama, Hoko, Yatai festivals"],
    "notable_cultural_exports": ["Anime/Manga", "Sushi/Ramen", "Toyota/Sony/Nintendo", "Samurai/Bushido", "Zen Buddhism", "J-Pop"],
    "major_museums": ["Tokyo National Museum", "Kyoto National Museum", "Hiroshima Peace Memorial Museum", "teamLab Borderless"],
    "world_heritage_sites_list": ["Historic Monuments of Ancient Kyoto", "Hiroshima Peace Memorial", "Mount Fuji", "Himeji Castle", "Itsukushima Shrine", "Historic Villages of Shirakawa-go"],
    "culinary_traditions": ["Sushi", "Ramen", "Tempura", "Wagyu beef", "Matcha", "Sake", "Okonomiyaki"],
    "notes": "Anime/manga $25B+ industry (global soft power); most Michelin-starred city (Tokyo); samurai/bushido cultural heritage; tea ceremony (sado); ikebana flower arrangement; wabi-sabi aesthetic philosophy; Nintendo/Sony/Pokémon global impact."
  },
  "comparative_rankings": {
    "human_development_index_rank": 22,
    "global_competitiveness_rank": 6,
    "happiness_index_rank": 51,
    "environmental_performance_rank": 25,
    "gender_gap_rank": 125,
    "soft_power_rank": 4,
    "notes": "World's 4th largest economy; top soft power globally (anime/cuisine/technology); peace rankings among best; gender gap worst in G7; aging/declining population major challenge."
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.90,
    "ict_development_index": 8.4,
    "mobile_money_accounts": 50000000,
    "digital_payments_pct_adults": 40,
    "fintech_companies": 300,
    "startup_ecosystem_value_usd": "$25 billion",
    "data_protection_law": True,
    "cybersecurity_index_score": 82.0,
    "innovation_index_score": 52.0,
    "innovation_index_rank": 13,
    "ai_readiness_index": 75.0
  }
}
}  # end DATA


def patch_country(slug, patch):
    path = os.path.join(BASE, slug, "index.json")
    with open(path) as f:
        data = json.load(f)
    cp = data["country_profile"]

    basics = patch.pop("_basics", {})
    for k, v in basics.items():
        cp[k] = v

    new_sections = {k: v for k, v in patch.items() if not k.startswith("_")}
    for sec, val in new_sections.items():
        cp[sec] = val

    for key, val in patch.items():
        if key.startswith("_expand_"):
            sec_name = key.replace("_expand_", "")
            if sec_name in cp and isinstance(cp[sec_name], dict):
                cp[sec_name].update(val)

    meta = data.get("_meta", {})
    meta["data_year"] = 2024

    lead = data.get("leadership", {})
    if "head_of_government" not in lead:
        lead["head_of_government"] = {"name": "", "title": "", "since": "", "party": ""}
    if "legislature" not in lead:
        lead["legislature"] = {"type": "", "chambers": [], "total_seats": 0, "ruling_party": "", "next_election": ""}
    for lk in ["current_leader", "head_of_state"]:
        if lk in lead and isinstance(lead[lk], dict) and "party" not in lead[lk]:
            lead[lk]["party"] = ""

    data["country_profile"] = cp
    data["_meta"] = meta
    data["leadership"] = lead

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return len(new_sections)


def main():
    total = 0
    for slug in sorted(DATA):
        n = patch_country(slug, copy.deepcopy(DATA[slug]))
        print(f"  OK  {slug}: {n} new sections + expanded fields added")
        total += 1
    print(f"\nBatch 2 done. {total} countries enhanced.")


if __name__ == "__main__":
    main()
