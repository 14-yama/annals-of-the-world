#!/usr/bin/env python3
"""
Populate empty country_profile sections for African countries Lesotho–Mozambique.
Data sourced from: World Bank, IMF, UNDP HDR, CIA Factbook, Transparency International,
RSF, EIU, Fragile States Index, ITU, UNESCO (publicly available 2023-2024 estimates).

Usage: python3 scripts/populate_africa_profiles_batch1.py
"""
import json, os

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "geo-registry", "places", "countries",
)

DATA = {
  "lesotho": {
    "demographics": {
      "median_age": 24.7,
      "urbanization_pct": 30.4,
      "fertility_rate": 3.0,
      "life_expectancy": 54.3,
      "infant_mortality_per_1k": 45.0,
      "literacy_rate_pct": 79.4,
      "net_migration_rate": -3.0
    },
    "natural_resources": {
      "primary": ["water (Lesotho Highlands Water Project)", "diamonds", "sand", "clay", "building stone", "wool", "mohair"],
      "resource_dependency_pct_gdp": 8,
      "notes": "Lesotho Highlands Water Project is largest infrastructure project in Africa selling water to South Africa; Letseng diamond mine produces some of the world's highest-value diamonds by average price per carat; limited arable land."
    },
    "military": {
      "budget_usd": "45 million",
      "pct_of_gdp": 1.8,
      "active_personnel": 2000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC"],
      "notes": "Lesotho Defence Force (LDF); historically intervened in politics; SADC deployed forces in 1998 to restore order after political crisis."
    },
    "trade": {
      "top_exports": ["diamonds", "garments (AGOA)", "water", "wool", "mohair", "food products"],
      "top_imports": ["food", "manufactured goods", "machinery", "petroleum", "chemicals"],
      "major_partners": ["South Africa (90%+ of trade)", "USA (AGOA garments)", "Belgium (diamonds)", "EU"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 23.0
    },
    "infrastructure": {
      "internet_penetration_pct": 36.0,
      "electricity_access_pct": 47.0,
      "mobile_subscriptions_per_100": 60,
      "railway_km": 2,
      "paved_roads_pct": 18
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 37, "rank": 99, "year": 2023},
      "press_freedom_index": {"rank": 88, "year": 2024},
      "democracy_index": {"score": 6.64, "category": "Flawed democracy", "year": 2023},
      "fragile_states_index": {"score": 77.2, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Subtropical highland (mild summers, cold winters)", "Continental (mountain areas)"],
      "co2_emissions_mt": 3,
      "renewable_energy_pct": 50,
      "natural_hazards": ["droughts", "snowstorms", "soil erosion"],
      "protected_areas_pct": 0.5
    },
    "debt_aid": {
      "national_debt_pct_gdp": 51.3,
      "foreign_aid_received_usd": "150 million",
      "notes": "SACU revenue distribution critical (~50% of government revenue); highly dependent on South Africa economically; MCC Compact for water/sanitation."
    },
    "education": {
      "primary_enrollment_pct": 82,
      "secondary_enrollment_pct": 45,
      "tertiary_enrollment_pct": 11,
      "pisa_participation": False,
      "top_universities": ["National University of Lesotho (NUL, 1945)", "Limkokwing University of Creative Technology (Maseru campus)"],
      "notes": "One of Africa's highest literacy rates; free primary education since 2000; severe teacher shortages in rural highlands; herder boys often miss school."
    },
    "diaspora_migration": {
      "diaspora_population": "350,000+ (primarily in South Africa)",
      "refugees_hosted": 500,
      "refugees_produced": 100,
      "remittances_usd": "500 million",
      "notes": "Basotho migrant mineworkers in South African gold and platinum mines historically formed backbone of economy; declining mine employment; remittances ~23% of GDP."
    },
    "digital_economy": {
      "e_government_index": 0.37,
      "mobile_money_adoption": "Growing (Mpesa, EcoCash)",
      "tech_hubs": ["Maseru (innovation hub nascent)"],
      "notes": "Limited broadband; Vodacom and Econet primary operators; mobile money expanding in rural areas; Lesotho Communications Authority regulating; digital divide between urban Maseru and rural highlands."
    }
  },
  "liberia": {
    "demographics": {
      "median_age": 18.1,
      "urbanization_pct": 53.1,
      "fertility_rate": 4.2,
      "life_expectancy": 64.7,
      "infant_mortality_per_1k": 54.0,
      "literacy_rate_pct": 48.3,
      "net_migration_rate": -0.5
    },
    "natural_resources": {
      "primary": ["iron ore", "rubber", "timber", "diamonds", "gold", "hydropower"],
      "resource_dependency_pct_gdp": 25,
      "notes": "ArcelorMittal iron ore mine at Yekepa; Firestone rubber plantation (one of world's largest); timber exports significant but deforestation concern; artisanal gold and diamond mining; offshore oil exploration."
    },
    "military": {
      "budget_usd": "18 million",
      "pct_of_gdp": 0.5,
      "active_personnel": 2000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "ECOWAS", "MRU"],
      "notes": "Armed Forces of Liberia (AFL) restructured by US after civil wars; UNMIL peacekeeping mission withdrew 2018; Coast Guard established with US support."
    },
    "trade": {
      "top_exports": ["iron ore", "rubber", "gold", "timber", "palm oil", "cocoa", "diamonds"],
      "top_imports": ["fuels", "chemicals", "machinery", "food", "manufactured goods"],
      "major_partners": ["China", "Germany", "USA", "Japan", "South Korea", "EU"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 8.5
    },
    "infrastructure": {
      "internet_penetration_pct": 16.2,
      "electricity_access_pct": 26.0,
      "mobile_subscriptions_per_100": 42,
      "railway_km": 0,
      "paved_roads_pct": 6
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 25, "rank": 145, "year": 2023},
      "press_freedom_index": {"rank": 62, "year": 2024},
      "democracy_index": {"score": 5.53, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 88.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (hot, humid)", "Equatorial monsoon"],
      "co2_emissions_mt": 2,
      "renewable_energy_pct": 28,
      "natural_hazards": ["tropical storms", "flooding", "deforestation", "coastal erosion"],
      "protected_areas_pct": 3.0
    },
    "debt_aid": {
      "national_debt_pct_gdp": 53.6,
      "foreign_aid_received_usd": "600 million",
      "notes": "HIPC debt relief 2010; heavily aid-dependent; US primary donor; post-war reconstruction ongoing; Ebola (2014-16) severely set back development."
    },
    "education": {
      "primary_enrollment_pct": 65,
      "secondary_enrollment_pct": 35,
      "tertiary_enrollment_pct": 12,
      "pisa_participation": False,
      "top_universities": ["University of Liberia (1862)", "Cuttington University (1889)", "Stella Maris Polytechnic"],
      "notes": "Education system devastated by 14 years of civil war; University of Liberia is Africa's oldest degree-granting institution; 2017 education reform act; teacher quality challenges."
    },
    "diaspora_migration": {
      "diaspora_population": "600,000+ (USA, Ghana, Nigeria, Sierra Leone, Guinea)",
      "refugees_hosted": 8000,
      "refugees_produced": 5000,
      "remittances_usd": "320 million",
      "notes": "Large diaspora in US (Minnesota, Philadelphia, New York); many returned post-civil war; Ivorian refugees hosted during 2011 crisis."
    },
    "digital_economy": {
      "e_government_index": 0.27,
      "mobile_money_adoption": "Emerging (Orange Money, Lonestar MTN Mobile Money)",
      "tech_hubs": ["iLab Liberia (Monrovia)"],
      "notes": "ACE submarine cable landed 2012; one of Africa's lowest internet penetration rates; mobile-first economy; digital financial inclusion growing slowly."
    }
  },
  "libya": {
    "demographics": {
      "median_age": 29.0,
      "urbanization_pct": 81.0,
      "fertility_rate": 2.2,
      "life_expectancy": 73.4,
      "infant_mortality_per_1k": 10.0,
      "literacy_rate_pct": 91.0,
      "net_migration_rate": 2.0
    },
    "natural_resources": {
      "primary": ["petroleum", "natural gas", "gypsum", "iron ore", "potash", "limestone", "sulfur"],
      "resource_dependency_pct_gdp": 60,
      "notes": "Africa's largest proven oil reserves (~48 billion barrels); National Oil Corporation (NOC); oil production ~1.2 mbpd when stable; Great Man-Made River Project (world's largest irrigation system); petroleum revenues >95% of export revenue."
    },
    "military": {
      "budget_usd": "3 billion (fragmented)",
      "pct_of_gdp": 8.0,
      "active_personnel": 30000,
      "reserve_personnel": 40000,
      "nuclear_status": "Non-nuclear (renounced WMD 2003)",
      "alliances": ["AU", "Arab League", "OIC"],
      "notes": "Fragmented between GNU (Tripoli) and LNA (Haftar, east); Turkish, Russian (Wagner), and Emirati foreign forces present; multiple militias; no unified national army since 2011."
    },
    "trade": {
      "top_exports": ["crude oil", "natural gas", "refined petroleum", "chemicals"],
      "top_imports": ["food", "machinery", "transport equipment", "consumer goods", "semi-finished goods"],
      "major_partners": ["Italy", "Germany", "Spain", "France", "China", "Turkey", "South Korea"],
      "trade_balance": "surplus (when oil production stable)",
      "remittances_pct_gdp": 0.3
    },
    "infrastructure": {
      "internet_penetration_pct": 46.0,
      "electricity_access_pct": 70.0,
      "mobile_subscriptions_per_100": 63,
      "railway_km": 0,
      "paved_roads_pct": 57
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 18, "rank": 170, "year": 2023},
      "press_freedom_index": {"rank": 143, "year": 2024},
      "democracy_index": {"score": 2.06, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 93.2, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Hot desert (Saharan, 90%+ of territory)", "Mediterranean (narrow coastal strip, Tripolitania and Cyrenaica)"],
      "co2_emissions_mt": 50,
      "renewable_energy_pct": 1,
      "natural_hazards": ["sandstorms (ghibli)", "droughts", "desertification", "flash floods"],
      "protected_areas_pct": 0.1
    },
    "debt_aid": {
      "national_debt_pct_gdp": 5.0,
      "foreign_aid_received_usd": "250 million",
      "notes": "Low formal debt; Libyan Investment Authority sovereign wealth fund (~$67 billion, largely frozen); central bank split between Tripoli/Benghazi; UN-mediated reconciliation efforts."
    },
    "education": {
      "primary_enrollment_pct": 95,
      "secondary_enrollment_pct": 85,
      "tertiary_enrollment_pct": 35,
      "pisa_participation": False,
      "top_universities": ["University of Tripoli (1957)", "University of Benghazi (1955)", "Misrata University"],
      "notes": "Free education at all levels under Gaddafi; high literacy rates; conflict since 2011 has damaged infrastructure; many students study abroad; brain drain significant."
    },
    "diaspora_migration": {
      "diaspora_population": "1 million+ (Egypt, Tunisia, Turkey, Europe)",
      "refugees_hosted": 50000,
      "refugees_produced": 130000,
      "remittances_usd": "100 million",
      "notes": "Major transit country for African migrants heading to Europe via Mediterranean; detention centres criticised by UN; internally displaced ~300,000 due to conflict."
    },
    "digital_economy": {
      "e_government_index": 0.38,
      "mobile_money_adoption": "Limited",
      "tech_hubs": ["Tripoli (nascent)", "Benghazi"],
      "notes": "Conflict-damaged telecom infrastructure; Libyana and Al-Madar mobile operators; internet censorship varied; submarine cable connections to Europe; highly cash-based economy."
    }
  },
  "madagascar": {
    "demographics": {
      "median_age": 20.3,
      "urbanization_pct": 39.9,
      "fertility_rate": 3.9,
      "life_expectancy": 67.0,
      "infant_mortality_per_1k": 38.0,
      "literacy_rate_pct": 76.7,
      "net_migration_rate": -0.1
    },
    "natural_resources": {
      "primary": ["graphite", "chromite", "coal", "bauxite", "rare earth elements", "salt", "quartz", "mica", "gemstones (sapphires)", "vanilla", "hydropower", "nickel"],
      "resource_dependency_pct_gdp": 12,
      "notes": "World's largest vanilla producer (~80% of global supply); Ambatovy nickel/cobalt mine (one of largest in world); ilmenite mining at Fort Dauphin; massive sapphire deposits; unique biodiversity (90% endemic species) is itself a resource via ecotourism."
    },
    "military": {
      "budget_usd": "75 million",
      "pct_of_gdp": 0.5,
      "active_personnel": 13500,
      "reserve_personnel": 8000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC", "IOC"],
      "notes": "People's Armed Forces; historically involved in politics (2009 coup); gendarmerie handles most rural security; limited naval capacity despite enormous maritime zone."
    },
    "trade": {
      "top_exports": ["vanilla", "nickel", "cobalt", "cloves", "coffee", "lychees", "shrimp", "textiles (AGOA)", "graphite", "essential oils"],
      "top_imports": ["petroleum", "rice", "capital goods", "vehicles", "food products", "pharmaceuticals"],
      "major_partners": ["France", "USA", "China", "India", "Germany", "Japan", "UAE"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 3.5
    },
    "infrastructure": {
      "internet_penetration_pct": 22.0,
      "electricity_access_pct": 34.0,
      "mobile_subscriptions_per_100": 44,
      "railway_km": 854,
      "paved_roads_pct": 11
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 25, "rank": 145, "year": 2023},
      "press_freedom_index": {"rank": 98, "year": 2024},
      "democracy_index": {"score": 3.93, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 82.4, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical along coast", "Temperate inland", "Arid in south"],
      "co2_emissions_mt": 4,
      "renewable_energy_pct": 55,
      "natural_hazards": ["cyclones (Dec-Mar)", "droughts (south)", "flooding", "locust invasions", "deforestation"],
      "protected_areas_pct": 10
    },
    "debt_aid": {
      "national_debt_pct_gdp": 45.2,
      "foreign_aid_received_usd": "800 million",
      "notes": "HIPC debt relief; heavily aid-dependent; France, World Bank, AfDB major donors; political instability deters investment; vanilla price volatility affects economy."
    },
    "education": {
      "primary_enrollment_pct": 85,
      "secondary_enrollment_pct": 35,
      "tertiary_enrollment_pct": 5,
      "pisa_participation": False,
      "top_universities": ["University of Antananarivo (1961)", "University of Fianarantsoa", "University of Toamasina"],
      "notes": "Education quality declining; many children drop out by secondary level; language of instruction debates (Malagasy vs French); teacher absenteeism; private schooling growing in cities."
    },
    "diaspora_migration": {
      "diaspora_population": "200,000+ (France, Réunion, Comoros, Canada)",
      "refugees_hosted": 200,
      "refugees_produced": 1000,
      "remittances_usd": "400 million",
      "notes": "French diaspora largest community; relatively low outmigration given population size; internal rural-urban migration significant."
    },
    "digital_economy": {
      "e_government_index": 0.33,
      "mobile_money_adoption": "Growing (Mvola/Telma, Orange Money, Airtel Money)",
      "tech_hubs": ["Antananarivo (multiple incubators)"],
      "notes": "METISS submarine cable improved connectivity; mobile money expanding rapidly; BPO/call centre industry serving French market; Telma, Orange, Airtel operators."
    }
  },
  "malawi": {
    "demographics": {
      "median_age": 16.5,
      "urbanization_pct": 17.8,
      "fertility_rate": 4.1,
      "life_expectancy": 64.3,
      "infant_mortality_per_1k": 33.0,
      "literacy_rate_pct": 62.1,
      "net_migration_rate": -0.2
    },
    "natural_resources": {
      "primary": ["limestone", "arable land", "hydropower", "uranium", "coal", "bauxite", "niobium", "rare earths"],
      "resource_dependency_pct_gdp": 5,
      "notes": "Lake Malawi provides fish (usipa, chambo) critically important for protein; Kayelekera uranium mine (mothballed); heavily agricultural economy (tobacco, tea, sugar, cotton); Shire River hydropower."
    },
    "military": {
      "budget_usd": "35 million",
      "pct_of_gdp": 0.8,
      "active_personnel": 5300,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC"],
      "notes": "Malawi Defence Force; active in UN peacekeeping (DR Congo, Darfur); professional reputation; limited equipment; army, navy (Lake Malawi), air wing."
    },
    "trade": {
      "top_exports": ["tobacco (50%+ of export revenue)", "tea", "sugar", "cotton", "coffee", "peanuts", "wood products", "uranium"],
      "top_imports": ["food", "petroleum products", "consumer goods", "fertilizers", "transport equipment"],
      "major_partners": ["Belgium", "South Africa", "UAE", "Egypt", "Germany", "UK", "India", "China", "Mozambique"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 2.5
    },
    "infrastructure": {
      "internet_penetration_pct": 18.0,
      "electricity_access_pct": 15.0,
      "mobile_subscriptions_per_100": 50,
      "railway_km": 797,
      "paved_roads_pct": 21
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 34, "rank": 110, "year": 2023},
      "press_freedom_index": {"rank": 57, "year": 2024},
      "democracy_index": {"score": 5.74, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 85.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Subtropical", "Semi-arid (lower Shire Valley)", "Temperate (highlands)"],
      "co2_emissions_mt": 2,
      "renewable_energy_pct": 82,
      "natural_hazards": ["floods", "droughts", "Cyclone Freddy (2023)", "earthquakes (minor)"],
      "protected_areas_pct": 17
    },
    "debt_aid": {
      "national_debt_pct_gdp": 64.0,
      "foreign_aid_received_usd": "1.2 billion",
      "notes": "One of world's poorest countries; highly aid-dependent; 'Cashgate' corruption scandal (2013) affected donor confidence; IMF bailout 2023; MK depreciation."
    },
    "education": {
      "primary_enrollment_pct": 89,
      "secondary_enrollment_pct": 18,
      "tertiary_enrollment_pct": 1,
      "pisa_participation": False,
      "top_universities": ["University of Malawi (1964, now split into UNIMA constituent colleges)", "Mzuzu University (1997)", "Lilongwe University of Agriculture and Natural Resources"],
      "notes": "Free primary education since 1994; massive enrollment growth strained quality; Kamuzu Academy (elite boarding school); very low tertiary enrollment; girls face early marriage barriers."
    },
    "diaspora_migration": {
      "diaspora_population": "300,000+ (South Africa, UK, Mozambique, Zambia)",
      "refugees_hosted": 55000,
      "refugees_produced": 3000,
      "remittances_usd": "200 million",
      "notes": "Hosts large Mozambican refugee population from conflict in Cabo Delgado; brain drain of medical professionals to UK/South Africa; seasonal labour migration to South Africa."
    },
    "digital_economy": {
      "e_government_index": 0.29,
      "mobile_money_adoption": "Growing rapidly (Mpamba/TNM, Airtel Money)",
      "tech_hubs": ["mHub (Lilongwe)", "Blantyre Tech Hub"],
      "notes": "2Africa submarine cable connection via Mozambique; mobile money replacing banking for unbanked majority; TNM and Airtel primary operators; digital agriculture platforms emerging."
    }
  },
  "mali": {
    "demographics": {
      "median_age": 15.8,
      "urbanization_pct": 45.4,
      "fertility_rate": 5.9,
      "life_expectancy": 59.3,
      "infant_mortality_per_1k": 62.0,
      "literacy_rate_pct": 35.5,
      "net_migration_rate": -3.5
    },
    "natural_resources": {
      "primary": ["gold", "phosphates", "kaolin", "salt", "limestone", "uranium", "hydropower", "iron ore", "bauxite", "manganese", "lithium"],
      "resource_dependency_pct_gdp": 10,
      "notes": "Africa's third-largest gold producer; Fekola, Loulo-Gounkoto, Syama mines; gold is ~70% of export revenue; large-scale artisanal gold mining (orpaillage); cattle and livestock significant; Niger and Senegal rivers vital for irrigation."
    },
    "military": {
      "budget_usd": "600 million",
      "pct_of_gdp": 3.2,
      "active_personnel": 22000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "G5 Sahel"],
      "notes": "Military junta in power since 2020/2021 coups; expelled French forces (Operation Barkhane) and MINUSMA (UN) in 2023; contracted Russian Wagner/Africa Corps; fighting jihadist groups (JNIM/ISGS) and Tuareg separatists in the north (Kidal captured 2023)."
    },
    "trade": {
      "top_exports": ["gold", "cotton", "livestock", "salt", "phosphates"],
      "top_imports": ["petroleum", "machinery", "food (rice, wheat)", "construction materials", "chemicals"],
      "major_partners": ["UAE", "Switzerland", "Senegal", "Cote d'Ivoire", "China", "South Africa", "France"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 6.0
    },
    "infrastructure": {
      "internet_penetration_pct": 27.0,
      "electricity_access_pct": 50.0,
      "mobile_subscriptions_per_100": 55,
      "railway_km": 593,
      "paved_roads_pct": 6
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 28, "rank": 137, "year": 2023},
      "press_freedom_index": {"rank": 114, "year": 2024},
      "democracy_index": {"score": 3.36, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 97.6, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Saharan (north)", "Sahelian (centre)", "Sudanian savanna (south)", "Tropical (far south)"],
      "co2_emissions_mt": 5,
      "renewable_energy_pct": 33,
      "natural_hazards": ["droughts", "desertification", "harmattan dust storms", "floods (Niger River)", "locust invasions"],
      "protected_areas_pct": 2.4
    },
    "debt_aid": {
      "national_debt_pct_gdp": 52.0,
      "foreign_aid_received_usd": "1.5 billion",
      "notes": "ECOWAS suspended after coups; Western sanctions; shifting to Russian/Chinese partnerships; WAEMU franc zone member; BCEAO monetary policy; artisanal gold partially smuggled."
    },
    "education": {
      "primary_enrollment_pct": 72,
      "secondary_enrollment_pct": 38,
      "tertiary_enrollment_pct": 6,
      "pisa_participation": False,
      "top_universities": ["University of Bamako (1996, now split into multiple universities)", "University of Sciences, Techniques and Technologies of Bamako"],
      "notes": "One of the world's lowest literacy rates; koranic schools parallel secular system; conflict in north closed many schools; Timbuktu manuscripts preservation; language of instruction (Bambara vs French) debated."
    },
    "diaspora_migration": {
      "diaspora_population": "4 million+ (Cote d'Ivoire, France, Senegal, Burkina Faso, Spain, Congo)",
      "refugees_hosted": 40000,
      "refugees_produced": 400000,
      "remittances_usd": "1.1 billion",
      "notes": "Major diaspora in Cote d'Ivoire and France; seasonal migration to cocoa plantations; conflict displaced hundreds of thousands internally and externally; circular migration tradition."
    },
    "digital_economy": {
      "e_government_index": 0.32,
      "mobile_money_adoption": "Growing (Orange Money dominant)",
      "tech_hubs": ["Bamako (Jokkolabs, DoniLab)"],
      "notes": "Orange Mali and Moov Africa primary operators; low broadband penetration; mobile money used for remittances; internet shutdowns during political crises."
    }
  },
  "mauritania": {
    "demographics": {
      "median_age": 20.7,
      "urbanization_pct": 57.0,
      "fertility_rate": 4.4,
      "life_expectancy": 64.9,
      "infant_mortality_per_1k": 47.0,
      "literacy_rate_pct": 53.5,
      "net_migration_rate": -0.8
    },
    "natural_resources": {
      "primary": ["iron ore", "gold", "copper", "gypsum", "phosphate", "diamonds", "oil", "fish", "natural gas"],
      "resource_dependency_pct_gdp": 30,
      "notes": "SNIM iron ore (Zouérat mine/Nouadhibou railway, one of world's longest trains); Tasiast gold mine (Kinross); fishing waters among richest in the world; gas discovery (GTA field with BP/Kosmos); artisanal gold mining booming."
    },
    "military": {
      "budget_usd": "200 million",
      "pct_of_gdp": 2.8,
      "active_personnel": 16000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "Arab League", "G5 Sahel", "OIC"],
      "notes": "President Ghazouani is former army chief; military historically central to politics (multiple coups); counterterrorism operations in Sahel (AQIM); successful in reducing jihadist attacks post-2011."
    },
    "trade": {
      "top_exports": ["iron ore", "gold", "fish/seafood", "copper", "oil"],
      "top_imports": ["food (wheat, rice)", "machinery", "petroleum products", "consumer goods", "vehicles"],
      "major_partners": ["China", "Switzerland", "Spain", "Japan", "UAE", "France", "EU (fishing agreements)"],
      "trade_balance": "variable (depends on commodity prices)",
      "remittances_pct_gdp": 1.0
    },
    "infrastructure": {
      "internet_penetration_pct": 40.0,
      "electricity_access_pct": 47.0,
      "mobile_subscriptions_per_100": 110,
      "railway_km": 728,
      "paved_roads_pct": 26
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 30, "rank": 130, "year": 2023},
      "press_freedom_index": {"rank": 95, "year": 2024},
      "democracy_index": {"score": 3.81, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 88.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Hot desert (Saharan, majority)", "Sahelian (south)"],
      "co2_emissions_mt": 4,
      "renewable_energy_pct": 30,
      "natural_hazards": ["droughts", "desertification", "sandstorms", "locust invasions"],
      "protected_areas_pct": 1.5
    },
    "debt_aid": {
      "national_debt_pct_gdp": 47.0,
      "foreign_aid_received_usd": "300 million",
      "notes": "Heavily indebted (HIPC); gas revenues expected to transform economy (GTA field first gas expected 2024-25); slavery legacy creates socioeconomic stratification; Gulf states provide aid."
    },
    "education": {
      "primary_enrollment_pct": 75,
      "secondary_enrollment_pct": 28,
      "tertiary_enrollment_pct": 5,
      "pisa_participation": False,
      "top_universities": ["University of Nouakchott Al Aasriya (1981)", "Higher Institute of Scientific Research"],
      "notes": "Bilingual education system (Arabic/French) contentious politically; mahadra (traditional Koranic school) tradition; low female secondary enrollment in rural areas; slavery legacy affects education access for Haratine community."
    },
    "diaspora_migration": {
      "diaspora_population": "200,000+ (Senegal, France, Gulf states)",
      "refugees_hosted": 90000,
      "refugees_produced": 30000,
      "remittances_usd": "70 million",
      "notes": "Hosts Malian refugees in Mbera camp; 1989 Senegal-Mauritania crisis expelled thousands of Black Mauritanians; Haratine (descendants of slaves) remain marginalised."
    },
    "digital_economy": {
      "e_government_index": 0.34,
      "mobile_money_adoption": "Growing (Sedad, Bankily/Mauritel)",
      "tech_hubs": ["Nouakchott (emerging)"],
      "notes": "ACE submarine cable; mobile penetration over 100%; Mauritel (Maroc Telecom) and Mattel primary operators; data costs relatively high; Nouakchott concentrates most tech activity."
    }
  },
  "mauritius": {
    "demographics": {
      "median_age": 37.7,
      "urbanization_pct": 40.8,
      "fertility_rate": 1.4,
      "life_expectancy": 75.1,
      "infant_mortality_per_1k": 12.0,
      "literacy_rate_pct": 91.3,
      "net_migration_rate": 0.5
    },
    "natural_resources": {
      "primary": ["arable land", "fish", "sugarcane"],
      "resource_dependency_pct_gdp": 3,
      "notes": "Limited natural resources; transformed from sugar monoculture to diversified economy (textiles, tourism, financial services, ICT); Exclusive Economic Zone is 2.3 million km²; deep-sea mining potential; Mauritius-Chagos sovereignty dispute with UK."
    },
    "military": {
      "budget_usd": "22 million",
      "pct_of_gdp": 0.2,
      "active_personnel": 2000,
      "reserve_personnel": 1500,
      "nuclear_status": "Non-nuclear (Indian Ocean nuclear-free zone advocate)",
      "alliances": ["AU", "SADC", "IOC", "Commonwealth"],
      "notes": "No standing army; Mauritius Police Force Special Mobile Force (paramilitary); National Coast Guard handles maritime security; India provides maritime defence support."
    },
    "trade": {
      "top_exports": ["clothing/textiles", "sugar", "fish (tuna)", "precious stones", "financial services", "IT services"],
      "top_imports": ["petroleum", "food", "manufactured goods", "capital equipment", "chemicals"],
      "major_partners": ["France", "UK", "USA", "South Africa", "India", "China", "Madagascar", "UAE"],
      "trade_balance": "deficit (offset by services surplus)",
      "remittances_pct_gdp": 1.5
    },
    "infrastructure": {
      "internet_penetration_pct": 72.0,
      "electricity_access_pct": 100.0,
      "mobile_subscriptions_per_100": 152,
      "railway_km": 0,
      "paved_roads_pct": 97
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 50, "rank": 57, "year": 2023},
      "press_freedom_index": {"rank": 64, "year": 2024},
      "democracy_index": {"score": 8.14, "category": "Full democracy", "year": 2023},
      "fragile_states_index": {"score": 37.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical maritime"],
      "co2_emissions_mt": 5,
      "renewable_energy_pct": 24,
      "natural_hazards": ["cyclones (Nov-Apr)", "flash floods", "coastal erosion", "coral reef degradation"],
      "protected_areas_pct": 4.5
    },
    "debt_aid": {
      "national_debt_pct_gdp": 82.5,
      "foreign_aid_received_usd": "50 million",
      "notes": "Upper-middle-income economy; no longer highly aid-dependent; financial services sector significant; Global Business (offshore) sector under EU grey-listing pressure; Chagos Islands sovereignty regained (ICJ ruling 2019)."
    },
    "education": {
      "primary_enrollment_pct": 98,
      "secondary_enrollment_pct": 91,
      "tertiary_enrollment_pct": 40,
      "pisa_participation": False,
      "top_universities": ["University of Mauritius (1965)", "University of Technology, Mauritius", "Open University of Mauritius", "Curtin University Mauritius"],
      "notes": "Free education through tertiary level; high literacy; Cambridge/IGCSE exam system; education hub for African and Indian Ocean students; competitive meritocratic system."
    },
    "diaspora_migration": {
      "diaspora_population": "200,000+ (UK, France, Australia, Canada, South Africa)",
      "refugees_hosted": 100,
      "refugees_produced": 50,
      "remittances_usd": "200 million",
      "notes": "Brain drain of skilled professionals (doctors, IT); Mauritian diaspora in UK dates to 1960s; return migration also occurring; foreign workers imported for construction/domestic work."
    },
    "digital_economy": {
      "e_government_index": 0.63,
      "mobile_money_adoption": "Established (Juice by MCB, my.t Money)",
      "tech_hubs": ["Cybercity Ebène (technology park)", "Port Louis"],
      "notes": "Africa's digital leader; SAFE/LION submarine cables; Cybercity Ebène hosts BPO/IT firms; ICT sector ~6% GDP; e-government advanced; Mauritius Telecom and Emtel operators; attracted international tech firms."
    }
  },
  "morocco": {
    "demographics": {
      "median_age": 30.3,
      "urbanization_pct": 64.6,
      "fertility_rate": 2.3,
      "life_expectancy": 77.0,
      "infant_mortality_per_1k": 17.0,
      "literacy_rate_pct": 73.8,
      "net_migration_rate": -1.6
    },
    "natural_resources": {
      "primary": ["phosphates (world's largest reserves)", "iron ore", "manganese", "lead", "zinc", "fish", "salt", "cobalt", "natural gas"],
      "resource_dependency_pct_gdp": 8,
      "notes": "World's largest phosphate reserves (~75% of global reserves) controlled by OCP Group; fisheries (Atlantic sardines); growing renewable energy sector (Noor-Ouarzazate solar complex, one of world's largest CSP plants); cannabis (recently legalised for medical/industrial use); automobile manufacturing hub (Renault, Stellantis)."
    },
    "military": {
      "budget_usd": "5.4 billion",
      "pct_of_gdp": 3.8,
      "active_personnel": 196000,
      "reserve_personnel": 150000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "Arab League", "OIC", "Non-NATO ally (US, since 2004)"],
      "notes": "Royal Armed Forces (FAR); sixth-largest military in Africa; extensive US military cooperation; involved in Western Sahara (UN MINURSO ceasefire observers); 2020 US recognised Moroccan sovereignty over Western Sahara; modern equipment (F-16s, M1 Abrams pending); compulsory military service reintroduced 2019."
    },
    "trade": {
      "top_exports": ["phosphates/fertilizers", "automobiles/auto parts", "electrical components/cables", "textiles/clothing", "agricultural products (citrus, tomatoes, olives)", "fish", "aerospace components"],
      "top_imports": ["petroleum", "machinery", "wheat", "plastics", "chemicals", "steel", "electronics"],
      "major_partners": ["Spain", "France", "India", "Brazil", "USA", "Italy", "Turkey", "China", "Germany"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 7.5
    },
    "infrastructure": {
      "internet_penetration_pct": 88.0,
      "electricity_access_pct": 100.0,
      "mobile_subscriptions_per_100": 136,
      "railway_km": 2110,
      "paved_roads_pct": 70
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 38, "rank": 97, "year": 2023},
      "press_freedom_index": {"rank": 144, "year": 2024},
      "democracy_index": {"score": 4.85, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 65.1, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Mediterranean (north/coast)", "Semi-arid (interior)", "Saharan desert (southeast)", "Mountain (Atlas)"],
      "co2_emissions_mt": 72,
      "renewable_energy_pct": 20,
      "natural_hazards": ["earthquakes (2023 Al Haouz earthquake, 6.8 magnitude)", "droughts", "flooding", "desertification", "locusts"],
      "protected_areas_pct": 26
    },
    "debt_aid": {
      "national_debt_pct_gdp": 71.6,
      "foreign_aid_received_usd": "2 billion",
      "notes": "Middle-income economy; Maroc 2030 Vision; Tanger Med port (largest in Africa/Mediterranean); high-speed rail (Al Boraq, Africa's first TGV); Mohammed VI investment fund; earthquake reconstruction ($11.7B programme)."
    },
    "education": {
      "primary_enrollment_pct": 99,
      "secondary_enrollment_pct": 74,
      "tertiary_enrollment_pct": 36,
      "pisa_participation": True,
      "top_universities": ["Mohammed V University (Rabat, 1957)", "Cadi Ayyad University (Marrakech)", "Hassan II University (Casablanca)", "Al Akhawayn University (Ifrane)", "Al-Qarawiyyin University (Fes, 859 CE, world's oldest)"],
      "notes": "Al-Qarawiyyin is recognised as world's oldest existing university; bilingual (Arabic/French) education with growing English; PISA performance below average; Francophone business schools; large student population; rural-urban education gap."
    },
    "diaspora_migration": {
      "diaspora_population": "5 million+ (France, Spain, Italy, Belgium, Netherlands, Germany, Israel, Canada)",
      "refugees_hosted": 10000,
      "refugees_produced": 5000,
      "remittances_usd": "11 billion",
      "notes": "Remittances critical (~7.5% GDP); large diaspora in Europe; becoming transit/destination country for sub-Saharan migrants; regularisation programmes for African migrants; Moroccan Jews in Israel (~700,000 of Moroccan descent)."
    },
    "digital_economy": {
      "e_government_index": 0.57,
      "mobile_money_adoption": "Growing (M-Wallet, bank mobile apps)",
      "tech_hubs": ["Casablanca (Technopark, largest in Africa)", "Rabat", "Tangier"],
      "notes": "Africa's largest tech park (Casablanca Technopark); auto-industry digitalisation; Maroc Telecom, Orange, inwi operators; submarine cables; nearshoring destination for European companies; Huawei cloud data centre."
    }
  },
  "mozambique": {
    "demographics": {
      "median_age": 17.2,
      "urbanization_pct": 38.0,
      "fertility_rate": 4.7,
      "life_expectancy": 60.9,
      "infant_mortality_per_1k": 55.0,
      "literacy_rate_pct": 63.4,
      "net_migration_rate": -0.3
    },
    "natural_resources": {
      "primary": ["natural gas (massive offshore reserves)", "coal", "titanium", "tantalite", "graphite", "hydropower (Cahora Bassa)", "timber", "iron ore", "rubies"],
      "resource_dependency_pct_gdp": 20,
      "notes": "Rovuma Basin LNG reserves among world's largest ('found gas' ~180 tcf); TotalEnergies $20B LNG project (suspended due to insurgency); Cahora Bassa Dam (one of Africa's largest hydropower plants); Montepuez ruby mine (world's largest); coal exports from Tete province via Nacala Corridor."
    },
    "military": {
      "budget_usd": "250 million",
      "pct_of_gdp": 1.5,
      "active_personnel": 11200,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC", "CPLP"],
      "notes": "FADM (Armed Forces); SADC Mission in Mozambique (SAMIM) deployed 2021 to combat Cabo Delgado insurgency; Rwandan forces also deployed; limited capacity; Islamist insurgency (al-Shabaab/ASWJ) in Cabo Delgado since 2017."
    },
    "trade": {
      "top_exports": ["aluminium", "coal", "natural gas", "tobacco", "electricity", "sugar", "timber", "prawns", "heavy mineral sands"],
      "top_imports": ["machinery", "vehicles", "petroleum", "food", "chemicals", "metal products"],
      "major_partners": ["South Africa", "India", "China", "Netherlands", "UAE", "Portugal", "Italy"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 2.0
    },
    "infrastructure": {
      "internet_penetration_pct": 21.0,
      "electricity_access_pct": 31.0,
      "mobile_subscriptions_per_100": 47,
      "railway_km": 4787,
      "paved_roads_pct": 21
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 26, "rank": 142, "year": 2023},
      "press_freedom_index": {"rank": 104, "year": 2024},
      "democracy_index": {"score": 3.51, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 89.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (north)", "Subtropical (south)", "Semi-arid (interior south)"],
      "co2_emissions_mt": 9,
      "renewable_energy_pct": 65,
      "natural_hazards": ["cyclones (Idai 2019, Kenneth 2019, Freddy 2023)", "floods", "droughts", "coastal erosion"],
      "protected_areas_pct": 16
    },
    "debt_aid": {
      "national_debt_pct_gdp": 101.0,
      "foreign_aid_received_usd": "2.2 billion",
      "notes": "Hidden debt scandal (2016, $2B secret loans) devastated donor relations and led to IMF suspension; heavily aid-dependent; LNG revenues expected mid-2020s; Nacala transport corridor critical for coal exports."
    },
    "education": {
      "primary_enrollment_pct": 90,
      "secondary_enrollment_pct": 26,
      "tertiary_enrollment_pct": 6,
      "pisa_participation": False,
      "top_universities": ["Eduardo Mondlane University (Maputo, 1962)", "Catholic University of Mozambique (Beira)", "Universidade Pedagógica"],
      "notes": "Portuguese language of instruction; massive post-war education expansion; low completion rates; insurgency in Cabo Delgado has closed hundreds of schools; teacher shortages severe in rural areas."
    },
    "diaspora_migration": {
      "diaspora_population": "1.5 million+ (South Africa, Portugal, Tanzania, Malawi)",
      "refugees_hosted": 30000,
      "refugees_produced": 100000,
      "remittances_usd": "400 million",
      "notes": "Mozambican mineworkers in South Africa (historic); Cabo Delgado insurgency displaced 1 million internally; cross-border movement with Tanzania and Malawi; xenophobic violence in South Africa affects Mozambicans."
    },
    "digital_economy": {
      "e_government_index": 0.31,
      "mobile_money_adoption": "Growing rapidly (M-Pesa Vodacom, mKesh)",
      "tech_hubs": ["Maputo (UX, various incubators)"],
      "notes": "EASSy and SEACOM submarine cables; Vodacom and Tmcel primary operators; mobile money expanding especially in rural areas; e-Government platform (SISTAFE for public finance); low broadband penetration."
    }
  }
}


def patch_country(slug, patch):
    path = os.path.join(BASE, slug, "index.json")
    with open(path) as f:
        data = json.load(f)
    cp = data["country_profile"]
    for section, values in patch.items():
        cp[section] = values
    data["country_profile"] = cp
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return list(patch.keys())


def main():
    updated = 0
    for slug in sorted(DATA):
        sections = patch_country(slug, DATA[slug])
        print(f"  OK   {slug}: {len(sections)} sections patched")
        updated += 1
    print(f"\nBatch 1 done. {updated} countries updated.")


if __name__ == "__main__":
    main()
