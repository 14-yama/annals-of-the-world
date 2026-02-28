#!/usr/bin/env python3
"""
Populate empty country_profile sections for African countries Namibia–South Sudan.
Data sourced from: World Bank, IMF, UNDP HDR, CIA Factbook, Transparency International,
RSF, EIU, Fragile States Index, ITU, UNESCO (publicly available 2023-2024 estimates).

Usage: python3 scripts/populate_africa_profiles_batch2.py
"""
import json, os

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "geo-registry", "places", "countries",
)

DATA = {
  "namibia": {
    "demographics": {
      "median_age": 22.0,
      "urbanization_pct": 54.0,
      "fertility_rate": 3.3,
      "life_expectancy": 63.7,
      "infant_mortality_per_1k": 29.0,
      "literacy_rate_pct": 91.5,
      "net_migration_rate": 0.5
    },
    "natural_resources": {
      "primary": ["diamonds", "uranium", "zinc", "copper", "lead", "tin", "gold", "lithium", "natural gas", "fish", "wildlife"],
      "resource_dependency_pct_gdp": 20,
      "notes": "World's 4th-largest uranium producer (Rössing and Husab mines); De Beers joint venture Namdeb leading diamond producer; Namibia's constitution (Article 95) was first in Africa to mandate environmental protection; Green Hydrogen project (Hyphen) planned; rich marine fisheries (Benguela current); SACU member."
    },
    "military": {
      "budget_usd": "450 million",
      "pct_of_gdp": 3.0,
      "active_personnel": 9200,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC"],
      "notes": "Namibia Defence Force (NDF); formed from PLAN (SWAPO guerrilla force) and SWATF after independence; deployed in DR Congo (SADC); professional reputation; limited naval capacity despite long Atlantic coast."
    },
    "trade": {
      "top_exports": ["diamonds", "uranium", "zinc", "fish/seafood", "gold", "beer (Windhoek Lager)", "livestock", "grapes"],
      "top_imports": ["petroleum", "food", "manufactured goods", "vehicles", "machinery"],
      "major_partners": ["South Africa (60%+ of trade)", "China", "Botswana", "Belgium", "Spain", "Zambia", "EU"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 0.5
    },
    "infrastructure": {
      "internet_penetration_pct": 53.0,
      "electricity_access_pct": 56.0,
      "mobile_subscriptions_per_100": 113,
      "railway_km": 2628,
      "paved_roads_pct": 15
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 49, "rank": 59, "year": 2023},
      "press_freedom_index": {"rank": 22, "year": 2024},
      "democracy_index": {"score": 6.52, "category": "Flawed democracy", "year": 2023},
      "fragile_states_index": {"score": 63.8, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Hot desert (Namib Desert, west coast)", "Semi-arid (central)", "Subtropical (Caprivi Strip/Zambezi Region)"],
      "co2_emissions_mt": 4,
      "renewable_energy_pct": 20,
      "natural_hazards": ["droughts", "flash floods", "bush fires"],
      "protected_areas_pct": 38
    },
    "debt_aid": {
      "national_debt_pct_gdp": 68.0,
      "foreign_aid_received_usd": "250 million",
      "notes": "Upper-middle-income economy; SACU revenues important (~30% of government revenue); high inequality (Gini ~59, one of world's highest); Green Hydrogen project ($10B+) could transform economy; Fishrot corruption scandal."
    },
    "education": {
      "primary_enrollment_pct": 97,
      "secondary_enrollment_pct": 62,
      "tertiary_enrollment_pct": 13,
      "pisa_participation": False,
      "top_universities": ["University of Namibia (UNAM, 1992)", "Namibia University of Science and Technology (NUST)", "International University of Management"],
      "notes": "Free primary education; high literacy rate; English is language of instruction (despite being L3 for most); SACMEQ assessments; teacher quality challenges in rural communal conservancies; strong environmental education tradition."
    },
    "diaspora_migration": {
      "diaspora_population": "150,000 (South Africa, Germany, UK, Angola)",
      "refugees_hosted": 6000,
      "refugees_produced": 500,
      "remittances_usd": "30 million",
      "notes": "German-speaking Namibian community maintains ties to Germany; skilled professionals emigrate to South Africa; Angolan refugees in north; SWAPO exile community largely returned post-1990."
    },
    "digital_economy": {
      "e_government_index": 0.48,
      "mobile_money_adoption": "Growing (EWallet MTC, Blue Wallet)",
      "tech_hubs": ["Windhoek (NBII, various incubators)"],
      "notes": "WACS submarine cable; MTC and Telecom Namibia operators; growing fintech sector; NCRST (commission for research) supports innovation; relatively high mobile penetration; rural connectivity challenge."
    }
  },
  "niger": {
    "demographics": {
      "median_age": 14.8,
      "urbanization_pct": 17.1,
      "fertility_rate": 6.8,
      "life_expectancy": 62.4,
      "infant_mortality_per_1k": 46.0,
      "literacy_rate_pct": 37.3,
      "net_migration_rate": -0.5
    },
    "natural_resources": {
      "primary": ["uranium", "coal", "iron ore", "tin", "phosphates", "gold", "molybdenum", "gypsum", "salt", "petroleum"],
      "resource_dependency_pct_gdp": 15,
      "notes": "World's 5th-largest uranium producer (Arlit mines, historically operated by French Orano/Areva); oil production began 2011 (Agadem block, CNPC); very large uranium reserves; livestock and agriculture dominate employment; Saharan solar potential."
    },
    "military": {
      "budget_usd": "300 million",
      "pct_of_gdp": 2.0,
      "active_personnel": 25000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "G5 Sahel"],
      "notes": "Military junta since July 2023 coup; expelled French forces (Operation Barkhane Niamey base); joined Alliance of Sahel States (AES) with Mali and Burkina Faso; fighting ISGS and JNIM jihadists; US drone base at Agadez (status uncertain post-coup); withdrew from ECOWAS."
    },
    "trade": {
      "top_exports": ["uranium", "gold", "oil", "onions", "cattle/livestock", "cowpeas", "gum arabic"],
      "top_imports": ["food (rice, wheat, sugar)", "machinery", "petroleum products", "vehicles", "cement"],
      "major_partners": ["France", "China", "Nigeria", "Thailand", "India", "Benin", "Togo", "Turkey"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 2.5
    },
    "infrastructure": {
      "internet_penetration_pct": 11.0,
      "electricity_access_pct": 19.0,
      "mobile_subscriptions_per_100": 39,
      "railway_km": 0,
      "paved_roads_pct": 21
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 28, "rank": 137, "year": 2023},
      "press_freedom_index": {"rank": 80, "year": 2024},
      "democracy_index": {"score": 3.24, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 98.2, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Saharan desert (north, 80% of territory)", "Sahelian (centre)", "Sudanian savanna (south)"],
      "co2_emissions_mt": 4,
      "renewable_energy_pct": 16,
      "natural_hazards": ["droughts (chronic)", "desertification", "locust invasions", "floods (Niger River)"],
      "protected_areas_pct": 7
    },
    "debt_aid": {
      "national_debt_pct_gdp": 51.0,
      "foreign_aid_received_usd": "1.8 billion",
      "notes": "One of world's poorest countries (bottom of HDI rankings); heavily aid-dependent; post-coup sanctions by ECOWAS and some Western donors; CFA franc zone (BCEAO); 3N Initiative (Nigeriens Nourish Nigeriens) food security programme."
    },
    "education": {
      "primary_enrollment_pct": 67,
      "secondary_enrollment_pct": 15,
      "tertiary_enrollment_pct": 3,
      "pisa_participation": False,
      "top_universities": ["Abdou Moumouni University (Niamey, 1971)", "Islamic University of Say", "Université Dan Dicko Dankoulodo (Maradi)"],
      "notes": "Lowest literacy rate globally; massive gender gap in education; koranic schools widespread; child marriage impacts girls' education; nomadic population challenges; conflict zones in border areas close schools."
    },
    "diaspora_migration": {
      "diaspora_population": "1 million+ (Nigeria, Benin, Cote d'Ivoire, Libya, France)",
      "refugees_hosted": 300000,
      "refugees_produced": 25000,
      "remittances_usd": "400 million",
      "notes": "Hosts Nigerian refugees from Boko Haram conflict and Malian refugees; Agadez historically major migration transit hub to Libya/Europe; EU-funded migration management; seasonal labour migration to Nigeria and coastal West Africa."
    },
    "digital_economy": {
      "e_government_index": 0.22,
      "mobile_money_adoption": "Emerging (Airtel Money, Orange Money)",
      "tech_hubs": ["Niamey (CIPMEN incubator)"],
      "notes": "Lowest internet penetration in Africa; ACE submarine cable via Benin; Airtel and Orange Niger operators; solar-powered mobile charging expanding; digital literacy extremely low; government pushes e-agriculture platforms."
    }
  },
  "nigeria": {
    "demographics": {
      "median_age": 18.1,
      "urbanization_pct": 54.3,
      "fertility_rate": 5.1,
      "life_expectancy": 53.9,
      "infant_mortality_per_1k": 72.0,
      "literacy_rate_pct": 62.0,
      "net_migration_rate": -0.3
    },
    "natural_resources": {
      "primary": ["petroleum", "natural gas", "tin", "iron ore", "coal", "limestone", "niobium", "lead", "zinc", "arable land"],
      "resource_dependency_pct_gdp": 9,
      "notes": "Africa's largest oil producer (~1.4 mbpd); NNPC (national oil company); Niger Delta (Bonny Light crude); massive natural gas reserves (~200 tcf, largely flared); oil theft ($3-5B/year); agriculture employs 35%+ of workforce; Nigerian cocoa fourth globally; palm oil; solid minerals sector underdeveloped."
    },
    "military": {
      "budget_usd": "3 billion",
      "pct_of_gdp": 0.6,
      "active_personnel": 223000,
      "reserve_personnel": 32000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "ECOWAS", "D-8", "Commonwealth"],
      "notes": "Africa's largest military by personnel; fighting Boko Haram/ISWAP insurgency in northeast (14+ years); banditry in northwest; separatist agitation (IPOB/Biafra); ECOMOG intervention force in Liberia/Sierra Leone (1990s); equipment modernisation ongoing."
    },
    "trade": {
      "top_exports": ["crude oil", "natural gas (LNG)", "cocoa", "rubber", "sesame seeds", "cashew nuts", "urea"],
      "top_imports": ["refined petroleum", "wheat", "vehicles", "machinery", "chemicals", "rice", "plastics"],
      "major_partners": ["India", "Spain", "China", "USA", "Netherlands", "France", "Indonesia", "Brazil"],
      "trade_balance": "surplus (oil-dependent)",
      "remittances_pct_gdp": 4.0
    },
    "infrastructure": {
      "internet_penetration_pct": 55.0,
      "electricity_access_pct": 60.0,
      "mobile_subscriptions_per_100": 99,
      "railway_km": 3505,
      "paved_roads_pct": 15
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 25, "rank": 145, "year": 2023},
      "press_freedom_index": {"rank": 112, "year": 2024},
      "democracy_index": {"score": 4.29, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 97.7, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (south)", "Savanna (middle belt)", "Sahelian (north)", "Equatorial (southeast)"],
      "co2_emissions_mt": 115,
      "renewable_energy_pct": 13,
      "natural_hazards": ["floods", "droughts (north)", "oil spills (Niger Delta)", "desertification", "erosion"],
      "protected_areas_pct": 14
    },
    "debt_aid": {
      "national_debt_pct_gdp": 38.0,
      "foreign_aid_received_usd": "3.5 billion",
      "notes": "Africa's largest economy by GDP; Sovereign Wealth Authority (NSIA); fuel subsidy removal 2023 (~$10B/year savings); naira devaluation 2023-24; debt servicing exceeds revenue; Dangote Refinery ($19B, Africa's largest) operational 2024."
    },
    "education": {
      "primary_enrollment_pct": 70,
      "secondary_enrollment_pct": 42,
      "tertiary_enrollment_pct": 10,
      "pisa_participation": False,
      "top_universities": ["University of Ibadan (1948)", "University of Lagos", "Obafemi Awolowo University (Ile-Ife)", "Ahmadu Bello University (Zaria)", "University of Nigeria Nsukka", "Covenant University"],
      "notes": "~20 million out-of-school children (world's highest); massive north-south education gap; ASUU strikes paralyse public universities; private universities growing; 13-million child 'almajiri' system in north; JAMB admission bottleneck."
    },
    "diaspora_migration": {
      "diaspora_population": "15 million+ (USA, UK, Canada, South Africa, Ghana, Cameroon, globally)",
      "refugees_hosted": 90000,
      "refugees_produced": 350000,
      "remittances_usd": "20 billion",
      "notes": "Largest African diaspora globally; 'Japa' phenomenon (youth emigration surge post-2020); remittances ~4% GDP; Nigerian professionals prominent in US/UK health, tech sectors; Boko Haram displaced 2.2 million internally; Cameroonian refugees hosted."
    },
    "digital_economy": {
      "e_government_index": 0.45,
      "mobile_money_adoption": "Rapidly growing (OPay, PalmPay, Paga, Moniepoint)",
      "tech_hubs": ["Lagos (Yaba/Silicon Lagoon: Andela, Flutterwave, Paystack)", "Abuja", "Port Harcourt"],
      "notes": "Africa's largest tech ecosystem; multiple unicorns (Flutterwave, OPay, Interswitch); Paystack acquired by Stripe; MTN, Airtel, Glo, 9mobile operators; NIN digital identity rollout; fintech leads innovation; Lagos startup ecosystem attracts global VC."
    }
  },
  "rwanda": {
    "demographics": {
      "median_age": 20.0,
      "urbanization_pct": 17.6,
      "fertility_rate": 3.9,
      "life_expectancy": 69.6,
      "infant_mortality_per_1k": 26.0,
      "literacy_rate_pct": 73.2,
      "net_migration_rate": -1.0
    },
    "natural_resources": {
      "primary": ["tin (cassiterite)", "coltan (tantalum)", "tungsten (wolframite)", "gold", "methane gas (Lake Kivu)", "hydropower", "peat"],
      "resource_dependency_pct_gdp": 10,
      "notes": "Major tantalum/coltan exporter (essential for electronics); '3T' minerals (tin, tantalum, tungsten); Lake Kivu methane gas extraction (KivuWatt, 25MW); tea and coffee main agricultural exports; limited arable land due to dense population; gorilla tourism (Volcanoes NP)."
    },
    "military": {
      "budget_usd": "150 million",
      "pct_of_gdp": 1.3,
      "active_personnel": 33000,
      "reserve_personnel": 2000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "EAC"],
      "notes": "Rwanda Defence Force (RDF); among Africa's most professional militaries; deployed in Mozambique (Cabo Delgado), CAR, South Sudan; UN peacekeeping contributor; accused of supporting M23 rebels in eastern DR Congo; compulsory civic service (Ingando)."
    },
    "trade": {
      "top_exports": ["gold", "tin ore", "coffee", "tea", "coltan", "tungsten", "niobium", "pyrethrum"],
      "top_imports": ["petroleum", "machinery", "food", "construction materials", "vehicles", "steel"],
      "major_partners": ["UAE", "DR Congo", "Kenya", "Tanzania", "Uganda", "China", "India", "Belgium"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 2.5
    },
    "infrastructure": {
      "internet_penetration_pct": 33.0,
      "electricity_access_pct": 48.0,
      "mobile_subscriptions_per_100": 83,
      "railway_km": 0,
      "paved_roads_pct": 19
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 53, "rank": 49, "year": 2023},
      "press_freedom_index": {"rank": 144, "year": 2024},
      "democracy_index": {"score": 3.16, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 79.4, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical highland (temperate due to altitude)", "Equatorial"],
      "co2_emissions_mt": 1,
      "renewable_energy_pct": 51,
      "natural_hazards": ["floods", "landslides", "droughts", "volcanic activity (Virunga)"],
      "protected_areas_pct": 10
    },
    "debt_aid": {
      "national_debt_pct_gdp": 68.0,
      "foreign_aid_received_usd": "1.3 billion",
      "notes": "Aid finances ~40% of budget; Vision 2050 (transition to upper-middle income); Kigali Convention Centre; BK Arena; new Bugesera International Airport under construction; Arsenal FC and PSG sponsorship deals for tourism promotion; Volkswagen assembly plant."
    },
    "education": {
      "primary_enrollment_pct": 97,
      "secondary_enrollment_pct": 43,
      "tertiary_enrollment_pct": 8,
      "pisa_participation": False,
      "top_universities": ["University of Rwanda (2013, merged national universities)", "African Leadership University (Kigali)", "Carnegie Mellon University Africa (Kigali)"],
      "notes": "Free 12-year basic education; English replaced French as medium of instruction (2009); Carnegie Mellon Africa campus; coding bootcamps (Andela Kigali); ICT in education push; high gender parity in enrollment."
    },
    "diaspora_migration": {
      "diaspora_population": "500,000+ (DR Congo, Uganda, Belgium, France, USA, Canada)",
      "refugees_hosted": 130000,
      "refugees_produced": 80000,
      "remittances_usd": "250 million",
      "notes": "1994 genocide diaspora (Tutsi and later Hutu); hosts Congolese and Burundian refugees; diaspora investment encouraged; Rwandan refugees in neighbouring countries contentious politically."
    },
    "digital_economy": {
      "e_government_index": 0.52,
      "mobile_money_adoption": "High (MTN MoMo, Airtel Money)",
      "tech_hubs": ["Kigali Innovation City (under development)", "kLab", "FabLab"],
      "notes": "Smart Kigali initiative; 4G LTE covers 95%+ of population; Irembo e-government platform (600+ services online); drone delivery (Zipline, blood/vaccine delivery); cashless economy push; MTN Rwanda and Airtel operators."
    }
  },
  "sao-tome-and-principe": {
    "demographics": {
      "median_age": 19.8,
      "urbanization_pct": 76.4,
      "fertility_rate": 3.4,
      "life_expectancy": 70.8,
      "infant_mortality_per_1k": 26.0,
      "literacy_rate_pct": 92.8,
      "net_migration_rate": -5.0
    },
    "natural_resources": {
      "primary": ["fish", "hydropower", "cocoa", "copra", "palm kernels"],
      "resource_dependency_pct_gdp": 5,
      "notes": "Offshore oil exploration in Joint Development Zone with Nigeria (no production yet); economy historically dependent on cocoa (once world's largest producer); fisheries unexploited; eco-tourism potential; Obo National Park covers 30% of territory."
    },
    "military": {
      "budget_usd": "2 million",
      "pct_of_gdp": 0.4,
      "active_personnel": 300,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "CPLP"],
      "notes": "Tiny armed forces; 2003 military coup attempt; Portuguese and Nigerian military cooperation; coast guard handles maritime security; no air force."
    },
    "trade": {
      "top_exports": ["cocoa", "copra", "coffee", "palm oil", "pepper"],
      "top_imports": ["food", "petroleum", "machinery", "electrical equipment", "construction materials"],
      "major_partners": ["Portugal", "Angola", "Netherlands", "Spain", "Belgium", "France", "EU"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 2.0
    },
    "infrastructure": {
      "internet_penetration_pct": 37.0,
      "electricity_access_pct": 78.0,
      "mobile_subscriptions_per_100": 80,
      "railway_km": 0,
      "paved_roads_pct": 68
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 45, "rank": 66, "year": 2023},
      "press_freedom_index": {"rank": 63, "year": 2024},
      "democracy_index": {"score": 6.63, "category": "Flawed democracy", "year": 2023},
      "fragile_states_index": {"score": 66.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (hot, humid)", "Equatorial maritime"],
      "co2_emissions_mt": 0.1,
      "renewable_energy_pct": 45,
      "natural_hazards": ["tropical storms"],
      "protected_areas_pct": 30
    },
    "debt_aid": {
      "national_debt_pct_gdp": 77.0,
      "foreign_aid_received_usd": "50 million",
      "notes": "Heavily aid-dependent; HIPC debt relief; Portugal largest bilateral donor; oil Joint Development Zone with Nigeria (potential revenue windfall); chocolate/premium cocoa niche market strategy; IMF programmes."
    },
    "education": {
      "primary_enrollment_pct": 95,
      "secondary_enrollment_pct": 70,
      "tertiary_enrollment_pct": 12,
      "pisa_participation": False,
      "top_universities": ["University of São Tomé and Príncipe (USTP, 2014)"],
      "notes": "High literacy rate for sub-Saharan Africa; free compulsory education; Portuguese language of instruction; many students go to Portugal for higher education; limited tertiary options domestically."
    },
    "diaspora_migration": {
      "diaspora_population": "50,000+ (Portugal, Angola, France)",
      "refugees_hosted": 0,
      "refugees_produced": 100,
      "remittances_usd": "10 million",
      "notes": "Significant emigration to Portugal for education and work; small country so diaspora proportionally large; contract workers returned from Angola; brain drain concern for medical professionals."
    },
    "digital_economy": {
      "e_government_index": 0.30,
      "mobile_money_adoption": "Nascent",
      "tech_hubs": [],
      "notes": "CST (Companhia Santomense de Telecomunicações) primary operator; limited broadband; ACE submarine cable connected; mobile internet primary access method; e-government services minimal."
    }
  },
  "senegal": {
    "demographics": {
      "median_age": 19.4,
      "urbanization_pct": 49.6,
      "fertility_rate": 4.4,
      "life_expectancy": 68.6,
      "infant_mortality_per_1k": 32.0,
      "literacy_rate_pct": 56.3,
      "net_migration_rate": -1.4
    },
    "natural_resources": {
      "primary": ["fish", "phosphates", "iron ore", "zircon", "gold", "natural gas", "petroleum", "salt", "limestone"],
      "resource_dependency_pct_gdp": 7,
      "notes": "Fisheries vital (employs 600,000+); Grande Côte zircon/titanium mine (world's largest mineral sands); Sangomar oil field (first oil 2024, Woodside); GTA gas field (shared with Mauritania, BP/Kosmos); phosphate mining (ICS); peanuts traditionally major export."
    },
    "military": {
      "budget_usd": "400 million",
      "pct_of_gdp": 1.5,
      "active_personnel": 17000,
      "reserve_personnel": 5000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "ECOWAS"],
      "notes": "One of Africa's most professional and apolitical militaries; never experienced a coup; active in UN/AU peacekeeping (Darfur, Mali, Central Africa); ECOMOG contributor; Casamance separatist conflict (MFDC) largely dormant; French military cooperation."
    },
    "trade": {
      "top_exports": ["gold", "phosphoric acid", "petroleum products (refinery)", "fish/seafood", "cement", "peanuts", "zircon", "titanium"],
      "top_imports": ["petroleum", "food (rice, wheat)", "machinery", "vehicles", "chemicals"],
      "major_partners": ["Mali", "India", "Switzerland", "China", "France", "Cote d'Ivoire", "Spain", "UK"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 10.5
    },
    "infrastructure": {
      "internet_penetration_pct": 58.0,
      "electricity_access_pct": 70.0,
      "mobile_subscriptions_per_100": 110,
      "railway_km": 906,
      "paved_roads_pct": 29
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 43, "rank": 72, "year": 2023},
      "press_freedom_index": {"rank": 94, "year": 2024},
      "democracy_index": {"score": 5.99, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 74.8, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical savanna (south)", "Hot semi-arid (central/north)", "Sahelian (far north)"],
      "co2_emissions_mt": 12,
      "renewable_energy_pct": 20,
      "natural_hazards": ["droughts", "floods (Senegal River)", "coastal erosion", "deforestation", "locust invasions"],
      "protected_areas_pct": 25
    },
    "debt_aid": {
      "national_debt_pct_gdp": 76.0,
      "foreign_aid_received_usd": "1.5 billion",
      "notes": "PSE (Plan Sénégal Émergent) development plan; TER (Train Express Régional Dakar) Africa's first modern commuter rail (2022); BRT Dakar; Diamniadio new city; first oil and gas revenues expected to transform economy; CFA franc zone; Blaise Diagne International Airport (2017)."
    },
    "education": {
      "primary_enrollment_pct": 85,
      "secondary_enrollment_pct": 48,
      "tertiary_enrollment_pct": 12,
      "pisa_participation": False,
      "top_universities": ["Cheikh Anta Diop University (Dakar, 1957)", "Gaston Berger University (Saint-Louis)", "Université Amadou Mahtar Mbow"],
      "notes": "UCAD one of Francophone Africa's largest universities (~80,000 students); daaras (Koranic schools) parallel secular system; talibé children issue; French language of instruction; bilingual Arabic-French schools growing."
    },
    "diaspora_migration": {
      "diaspora_population": "3 million+ (France, Italy, Spain, USA, Gambia, Mauritania)",
      "refugees_hosted": 15000,
      "refugees_produced": 10000,
      "remittances_usd": "2.7 billion",
      "notes": "Remittances critical (~10.5% GDP); large Mouride brotherhood diaspora network; irregular migration via canoe to Canary Islands resumed; Senegalese traders across West Africa; Casamance displacement mostly resolved."
    },
    "digital_economy": {
      "e_government_index": 0.44,
      "mobile_money_adoption": "Growing rapidly (Orange Money dominant, Wave)",
      "tech_hubs": ["Dakar (CTIC Dakar, incubator)", "Diamniadio Digital Park"],
      "notes": "Wave disrupted Orange Money monopoly with lower fees; Sonatel/Orange Senegal dominant operator; SAT-3/WASC/ACE submarine cables; growing BPO sector for French-speaking market; Paydunya, InTouch fintech; Diamniadio tech city under development."
    }
  },
  "seychelles": {
    "demographics": {
      "median_age": 36.8,
      "urbanization_pct": 58.8,
      "fertility_rate": 2.3,
      "life_expectancy": 73.4,
      "infant_mortality_per_1k": 10.0,
      "literacy_rate_pct": 95.9,
      "net_migration_rate": 1.0
    },
    "natural_resources": {
      "primary": ["fish (tuna)", "cinnamon", "copra", "salt", "granite"],
      "resource_dependency_pct_gdp": 3,
      "notes": "Exclusive Economic Zone of 1.37 million km² (vast ocean resources); Indian Ocean tuna fishing hub (Port Victoria is major tuna transhipment port); eco-tourism primary revenue source; coco de mer endemic palm; Blue Economy focus."
    },
    "military": {
      "budget_usd": "20 million",
      "pct_of_gdp": 1.2,
      "active_personnel": 420,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "IOC", "SADC", "Commonwealth"],
      "notes": "Seychelles People's Defence Forces; Coast Guard primary capability; anti-piracy operations (Indian Ocean); Indian naval station (Assumption Island debated); maritime domain awareness critical."
    },
    "trade": {
      "top_exports": ["canned tuna", "frozen fish", "refined petroleum (re-export)", "cinnamon"],
      "top_imports": ["food", "petroleum", "manufactured goods", "machinery", "vehicles"],
      "major_partners": ["UAE", "France", "UK", "Japan", "Spain", "Mauritius", "India", "South Africa"],
      "trade_balance": "deficit (offset by tourism revenue)",
      "remittances_pct_gdp": 1.0
    },
    "infrastructure": {
      "internet_penetration_pct": 79.0,
      "electricity_access_pct": 100.0,
      "mobile_subscriptions_per_100": 198,
      "railway_km": 0,
      "paved_roads_pct": 96
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 70, "rank": 23, "year": 2023},
      "press_freedom_index": {"rank": 13, "year": 2024},
      "democracy_index": {"score": 6.86, "category": "Flawed democracy", "year": 2023},
      "fragile_states_index": {"score": 50.3, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical maritime (warm, humid year-round)"],
      "co2_emissions_mt": 0.5,
      "renewable_energy_pct": 5,
      "natural_hazards": ["tropical cyclones (rare, outside cyclone belt)", "coastal erosion", "coral bleaching", "sea-level rise"],
      "protected_areas_pct": 50
    },
    "debt_aid": {
      "national_debt_pct_gdp": 63.0,
      "foreign_aid_received_usd": "25 million",
      "notes": "Highest GDP per capita in Africa; high-income economy; Blue Bond pioneer (world's first sovereign blue bond, $15M, 2018); debt restructuring 2009 (post financial crisis); tourism ~30% GDP; innovative debt-for-nature swaps."
    },
    "education": {
      "primary_enrollment_pct": 99,
      "secondary_enrollment_pct": 96,
      "tertiary_enrollment_pct": 15,
      "pisa_participation": False,
      "top_universities": ["University of Seychelles (2009)"],
      "notes": "Free compulsory education; one of Africa's highest literacy rates; most students go abroad for university (UK, Australia, Mauritius); Creole, English, and French all used in education; small scale limits specialisation."
    },
    "diaspora_migration": {
      "diaspora_population": "15,000+ (UK, Australia, France)",
      "refugees_hosted": 0,
      "refugees_produced": 50,
      "remittances_usd": "15 million",
      "notes": "Small population means diaspora proportionally significant; foreign workers (~15% of workforce) from India, Bangladesh, Philippines, Madagascar for construction and services; brain drain concern."
    },
    "digital_economy": {
      "e_government_index": 0.57,
      "mobile_money_adoption": "Established (bank mobile apps)",
      "tech_hubs": ["Victoria (nascent)"],
      "notes": "SEAS submarine cable (2012) transformed connectivity; Cable & Wireless (Airtel) and Intelvision operators; high mobile penetration (nearly 200%); Blue Economy digital initiatives; e-government services advancing."
    }
  },
  "sierra-leone": {
    "demographics": {
      "median_age": 19.2,
      "urbanization_pct": 43.8,
      "fertility_rate": 4.2,
      "life_expectancy": 55.9,
      "infant_mortality_per_1k": 78.0,
      "literacy_rate_pct": 43.2,
      "net_migration_rate": -1.0
    },
    "natural_resources": {
      "primary": ["diamonds", "rutile (titanium ore)", "bauxite", "iron ore", "gold", "chromite", "fish"],
      "resource_dependency_pct_gdp": 20,
      "notes": "Rich in diamonds (Sierra Leone Selection Trust historic mine; Koidu mine); world's largest rutile deposits (Sembehun/Sierra Rutile); Tonkolili iron ore (closed); Marampa iron ore; alluvial diamond mining (blood diamonds fuelled civil war); Atlantic fisheries."
    },
    "military": {
      "budget_usd": "25 million",
      "pct_of_gdp": 0.6,
      "active_personnel": 8500,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "ECOWAS", "MRU", "Commonwealth"],
      "notes": "Republic of Sierra Leone Armed Forces (RSLAF); rebuilt by UK International Military Advisory and Training Team (IMATT) after civil war; Kamajor militia (civil defence) disbanded; UN peacekeeping contributor."
    },
    "trade": {
      "top_exports": ["iron ore", "diamonds", "rutile (titanium ore)", "bauxite", "cocoa", "coffee", "fish"],
      "top_imports": ["food (rice)", "petroleum", "machinery", "vehicles", "manufactured goods"],
      "major_partners": ["China", "Belgium (diamonds)", "Cote d'Ivoire", "Netherlands", "USA", "India", "UK"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 3.5
    },
    "infrastructure": {
      "internet_penetration_pct": 17.0,
      "electricity_access_pct": 26.0,
      "mobile_subscriptions_per_100": 54,
      "railway_km": 0,
      "paved_roads_pct": 8
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 34, "rank": 110, "year": 2023},
      "press_freedom_index": {"rank": 46, "year": 2024},
      "democracy_index": {"score": 4.43, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 85.7, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical monsoon (one of the wettest places on the West African coast)", "Tropical savanna (interior)"],
      "co2_emissions_mt": 2,
      "renewable_energy_pct": 38,
      "natural_hazards": ["flooding", "mudslides (Freetown, 2017 disaster killed 1,000+)", "coastal erosion", "deforestation"],
      "protected_areas_pct": 5
    },
    "debt_aid": {
      "national_debt_pct_gdp": 77.0,
      "foreign_aid_received_usd": "700 million",
      "notes": "Heavily aid-dependent; HIPC/MDRI debt relief; economy devastated by civil war (1991-2002) then Ebola (2014-16); iron ore price collapse; IMF ECF programme; Le (leone) has depreciated significantly."
    },
    "education": {
      "primary_enrollment_pct": 86,
      "secondary_enrollment_pct": 40,
      "tertiary_enrollment_pct": 3,
      "pisa_participation": False,
      "top_universities": ["Fourah Bay College (1827, oldest university in West Africa)", "Njala University", "Eastern Technical University"],
      "notes": "Fourah Bay College ('Athens of West Africa') trained elites across British West Africa; Free Quality School Education (FQSE) 2018; civil war destroyed 1,270+ schools; low female secondary enrollment; teacher motivation issues."
    },
    "diaspora_migration": {
      "diaspora_population": "500,000+ (UK, USA, Guinea, Gambia, Liberia)",
      "refugees_hosted": 500,
      "refugees_produced": 5000,
      "remittances_usd": "150 million",
      "notes": "Civil war created massive diaspora (especially UK, US); Krio community globally dispersed; returnees contribute to reconstruction; diaspora engagement strategy launched."
    },
    "digital_economy": {
      "e_government_index": 0.29,
      "mobile_money_adoption": "Growing (Orange Money, Afrimoney by Africell)",
      "tech_hubs": ["Freetown (Sensi Tech Hub, Innovation SL)"],
      "notes": "ACE submarine cable; Africell and Orange SL primary operators; Directorate of Science, Technology and Innovation (DSTI) driving government tech adoption; open data initiative; low broadband penetration."
    }
  },
  "somalia": {
    "demographics": {
      "median_age": 16.7,
      "urbanization_pct": 47.9,
      "fertility_rate": 6.0,
      "life_expectancy": 58.3,
      "infant_mortality_per_1k": 88.0,
      "literacy_rate_pct": 37.8,
      "net_migration_rate": -4.0
    },
    "natural_resources": {
      "primary": ["uranium", "iron ore", "tin", "gypsum", "bauxite", "copper", "salt", "natural gas", "petroleum (unexplored)", "fish", "livestock"],
      "resource_dependency_pct_gdp": 5,
      "notes": "Longest coastline in mainland Africa (~3,025 km) with rich fishing waters; livestock (camels, cattle, goats) backbone of economy (~40% GDP); offshore oil potential (blocks licensed but unexplored); frankincense and myrrh exports; charcoal export (linked to al-Shabaab)."
    },
    "military": {
      "budget_usd": "120 million",
      "pct_of_gdp": 2.0,
      "active_personnel": 20000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "IGAD", "Arab League", "OIC"],
      "notes": "Somali National Army (SNA) rebuilding with US/Turkey/EU training; ATMIS (AU Transition Mission) replacing AMISOM; fighting al-Shabaab (al-Qaeda affiliate); clan militias remain significant; US drone strikes; Puntland and Somaliland have separate forces."
    },
    "trade": {
      "top_exports": ["livestock (camels, cattle, goats, sheep)", "bananas", "hides/skins", "charcoal", "fish", "frankincense", "myrrh"],
      "top_imports": ["food (rice, wheat, sugar)", "petroleum", "khat (from Ethiopia/Kenya)", "construction materials", "vehicles", "consumer goods"],
      "major_partners": ["UAE", "Saudi Arabia", "Oman", "India", "China", "Turkey", "Kenya", "Ethiopia", "Djibouti"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 30.0
    },
    "infrastructure": {
      "internet_penetration_pct": 15.0,
      "electricity_access_pct": 36.0,
      "mobile_subscriptions_per_100": 51,
      "railway_km": 0,
      "paved_roads_pct": 12
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 11, "rank": 180, "year": 2023},
      "press_freedom_index": {"rank": 145, "year": 2024},
      "democracy_index": {"score": 0.0, "category": "Authoritarian (no score)", "year": 2023},
      "fragile_states_index": {"score": 110.9, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Hot desert (north/central)", "Hot semi-arid (south)", "Tropical monsoon (southwest)"],
      "co2_emissions_mt": 1,
      "renewable_energy_pct": 20,
      "natural_hazards": ["droughts (recurrent, devastating)", "floods (Shabelle/Jubba rivers)", "dust storms", "cyclones"],
      "protected_areas_pct": 1
    },
    "debt_aid": {
      "national_debt_pct_gdp": 28.0,
      "foreign_aid_received_usd": "2 billion",
      "notes": "HIPC debt relief 2023 (reduced $4.5B to $557M); heavily aid-dependent; informal hawala remittance system (~$2B/yr) critical; Turkey largest bilateral partner (military base, infrastructure); Somaliland maintains separate de facto economy and currency."
    },
    "education": {
      "primary_enrollment_pct": 30,
      "secondary_enrollment_pct": 10,
      "tertiary_enrollment_pct": 4,
      "pisa_participation": False,
      "top_universities": ["Somali National University (Mogadishu, 1954, reopened 2014)", "University of Hargeisa (Somaliland)", "SIMAD University (Mogadishu)", "Amoud University (Borama)"],
      "notes": "Education system collapsed after 1991; private universities proliferated; clan/diaspora-funded schools; Somaliland has better education indicators; Saudi/Gulf-funded Islamic schools; many study abroad (Turkey, Malaysia, Egypt); under 25% of children complete primary school."
    },
    "diaspora_migration": {
      "diaspora_population": "2 million+ (Kenya, Ethiopia, Yemen, USA, UK, Canada, Sweden, Norway, Netherlands)",
      "refugees_hosted": 35000,
      "refugees_produced": 900000,
      "remittances_usd": "2 billion",
      "notes": "Remittances (~30% GDP) are the lifeline of the economy; hawala system (Dahabshiil largest operator); large communities in Minneapolis, London, Toronto, Stockholm; Dadaab/Kakuma camps in Kenya; IDP camps (2.9 million internally displaced)."
    },
    "digital_economy": {
      "e_government_index": 0.15,
      "mobile_money_adoption": "Very high (Zaad by Telesom, EVC by Hormuud — among Africa's highest mobile money usage rates)",
      "tech_hubs": ["Mogadishu (iRise Hub)", "Hargeisa"],
      "notes": "Paradoxically advanced mobile money adoption; Hormuud Telecom one of Africa's most competitive operators (cheap calls, widespread coverage achieved without regulation); mobile money used for everything; internet via DARE1 and other submarine cables; thriving despite conflict."
    }
  },
  "south-africa": {
    "demographics": {
      "median_age": 28.0,
      "urbanization_pct": 68.3,
      "fertility_rate": 2.3,
      "life_expectancy": 65.0,
      "infant_mortality_per_1k": 25.0,
      "literacy_rate_pct": 87.0,
      "net_migration_rate": 0.9
    },
    "natural_resources": {
      "primary": ["gold", "platinum group metals (world's largest reserves)", "chromium", "manganese", "vanadium", "iron ore", "coal", "diamonds", "uranium", "titanium", "copper", "nickel"],
      "resource_dependency_pct_gdp": 8,
      "notes": "World's largest reserves of platinum (~80% of global), manganese, chromium, vanadium; historically the world's largest gold producer (Witwatersrand Basin); coal provides ~80% of electricity (Eskom); Bushveld Igneous Complex (world's largest layered igneous intrusion); De Beers diamond legacy; wine industry (Western Cape)."
    },
    "military": {
      "budget_usd": "3.5 billion",
      "pct_of_gdp": 0.8,
      "active_personnel": 73000,
      "reserve_personnel": 15000,
      "nuclear_status": "Non-nuclear (voluntarily dismantled 6 nuclear weapons, only country to do so)",
      "alliances": ["AU", "SADC", "BRICS", "Commonwealth"],
      "notes": "SANDF (South African National Defence Force); integrated former apartheid military with MK (ANC) and APLA (PAC) forces; deployed in DRC (MONUSCO), Mozambique; Denel arms manufacturer; Rooivalk attack helicopter; Gripens; ageing equipment; budget constraints."
    },
    "trade": {
      "top_exports": ["gold", "platinum group metals", "iron ore", "coal", "manganese", "vehicles/auto parts", "citrus fruit", "wine", "chemicals", "machinery"],
      "top_imports": ["petroleum", "vehicles", "machinery", "electronics", "chemicals", "food"],
      "major_partners": ["China", "USA", "Germany", "Japan", "India", "UK", "Netherlands", "Botswana", "Mozambique"],
      "trade_balance": "surplus (commodity-driven)",
      "remittances_pct_gdp": 0.3
    },
    "infrastructure": {
      "internet_penetration_pct": 72.0,
      "electricity_access_pct": 85.0,
      "mobile_subscriptions_per_100": 167,
      "railway_km": 20986,
      "paved_roads_pct": 17
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 41, "rank": 83, "year": 2023},
      "press_freedom_index": {"rank": 38, "year": 2024},
      "democracy_index": {"score": 7.05, "category": "Flawed democracy", "year": 2023},
      "fragile_states_index": {"score": 71.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Subtropical (east coast)", "Mediterranean (Western Cape)", "Semi-arid (Karoo/interior)", "Desert (Namib border, Northern Cape)"],
      "co2_emissions_mt": 435,
      "renewable_energy_pct": 9,
      "natural_hazards": ["droughts", "wildfires", "floods", "earthquakes (minor)", "load-shedding (Eskom power crisis)"],
      "protected_areas_pct": 15
    },
    "debt_aid": {
      "national_debt_pct_gdp": 73.0,
      "foreign_aid_received_usd": "1 billion",
      "notes": "Africa's most industrialised economy; load-shedding crisis (2023-24, Eskom); highest inequality globally (Gini ~63); unemployment ~33%; GNU (Government of National Unity) from 2024 coalition; Transnet logistics crisis affecting ports/rail; sovereign downgrade to junk status."
    },
    "education": {
      "primary_enrollment_pct": 97,
      "secondary_enrollment_pct": 87,
      "tertiary_enrollment_pct": 24,
      "pisa_participation": True,
      "top_universities": ["University of Cape Town (1829)", "University of the Witwatersrand (Wits)", "Stellenbosch University", "University of Pretoria", "University of KwaZulu-Natal", "Rhodes University"],
      "notes": "UCT ranks among world's top 200; free higher education (NSFAS) for qualifying students since 2018 (#FeesMustFall movement); high enrollment but quality crisis (PIRLS/TIMSS scores among lowest globally); 11 official language instruction; historically Black universities (Fort Hare, Limpopo)."
    },
    "diaspora_migration": {
      "diaspora_population": "3 million+ (UK, Australia, USA, Canada, New Zealand, UAE, Germany)",
      "refugees_hosted": 250000,
      "refugees_produced": 10000,
      "remittances_usd": "1 billion",
      "notes": "Post-1994 brain drain (white emigration); xenophobic violence against African migrants (Zimbabweans, Nigerians, Mozambicans); hosts largest refugee/migrant population in Africa (~4 million); immigration from Zimbabwe, Mozambique, DRC, Nigeria, Ethiopia, Bangladesh, Pakistan."
    },
    "digital_economy": {
      "e_government_index": 0.60,
      "mobile_money_adoption": "Moderate (bank-led model; PayShap rapid payments)",
      "tech_hubs": ["Cape Town (Silicon Cape)", "Johannesburg (Tshimologong, Jozi Hub)", "Durban (SmartXchange)"],
      "notes": "Africa's largest tech ecosystem by investment value; fintech leader (TymeBank, Discovery Bank, Capitec Go); Naspers/Prosus (Tencent investor); submarine cables (WACS, SAT-3, EASSy, 2Africa); MTN, Vodacom, Cell C, Telkom operators; well-developed banking system enabling digital payments."
    }
  },
  "south-sudan": {
    "demographics": {
      "median_age": 18.6,
      "urbanization_pct": 20.8,
      "fertility_rate": 4.5,
      "life_expectancy": 58.0,
      "infant_mortality_per_1k": 64.0,
      "literacy_rate_pct": 34.5,
      "net_migration_rate": -5.0
    },
    "natural_resources": {
      "primary": ["petroleum", "iron ore", "copper", "chromium ore", "zinc", "tungsten", "mica", "silver", "gold", "hydropower", "timber", "hardwoods", "arable land"],
      "resource_dependency_pct_gdp": 60,
      "notes": "Oil dominates economy (~98% of government revenue, ~60% of GDP); pipeline through Sudan to Port Sudan for export (transit fees contentious); Sudd wetland (Africa's largest swamp); vast unexploited agricultural potential; timber reserves; White Nile hydropower potential."
    },
    "military": {
      "budget_usd": "700 million",
      "pct_of_gdp": 10.0,
      "active_personnel": 185000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "IGAD", "EAC"],
      "notes": "SSPDF (South Sudan People's Defence Forces); merged with opposition fighters (SPLA-IO) under 2018 peace agreement; ethnic Dinka/Nuer divisions within military; UNMISS peacekeeping force (~19,000); arms embargo (partially lifted); political-military elite control."
    },
    "trade": {
      "top_exports": ["crude oil (virtually sole export)", "timber"],
      "top_imports": ["food", "manufactured goods", "machinery", "vehicles", "petroleum products", "arms"],
      "major_partners": ["China (oil)", "Japan", "India", "Uganda", "Kenya", "Sudan", "UAE"],
      "trade_balance": "surplus (oil exports)",
      "remittances_pct_gdp": 6.0
    },
    "infrastructure": {
      "internet_penetration_pct": 8.0,
      "electricity_access_pct": 7.0,
      "mobile_subscriptions_per_100": 30,
      "railway_km": 0,
      "paved_roads_pct": 2
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 13, "rank": 177, "year": 2023},
      "press_freedom_index": {"rank": 142, "year": 2024},
      "democracy_index": {"score": 1.24, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 108.5, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical wet (equatorial south)", "Tropical savanna (central)", "Hot semi-arid (north)"],
      "co2_emissions_mt": 2,
      "renewable_energy_pct": 95,
      "natural_hazards": ["floods (seasonal, devastating)", "droughts", "locust invasions", "disease outbreaks"],
      "protected_areas_pct": 13
    },
    "debt_aid": {
      "national_debt_pct_gdp": 52.0,
      "foreign_aid_received_usd": "2.5 billion",
      "notes": "World's youngest nation (2011); humanitarian crisis (famine risk, 7.7 million food insecure); oil production declined from 350k to ~135k bpd; Revitalised ARCSS peace agreement (2018); transitional government (elections delayed); inflation ~300%+."
    },
    "education": {
      "primary_enrollment_pct": 35,
      "secondary_enrollment_pct": 5,
      "tertiary_enrollment_pct": 1,
      "pisa_participation": False,
      "top_universities": ["University of Juba (1977)", "Upper Nile University (Malakal)", "University of Bahr el Ghazal"],
      "notes": "One of the world's lowest education indicators; conflict closed majority of schools; 2.8 million children out of school; extreme teacher shortages (South Sudan had 20x fewer teachers per capita than regional average); English language of instruction but most teachers trained in Arabic."
    },
    "diaspora_migration": {
      "diaspora_population": "2.3 million+ refugees (Uganda, Sudan, Ethiopia, Kenya, DR Congo)",
      "refugees_hosted": 340000,
      "refugees_produced": 2300000,
      "remittances_usd": "300 million",
      "notes": "Second-largest refugee crisis in Africa; 2.3 million refugees plus 1.8 million IDPs; Bidibidi settlement in Uganda is world's largest refugee settlement; Sudanese refugees fleeing 2023 Sudan war crossing into South Sudan; remittances via informal channels."
    },
    "digital_economy": {
      "e_government_index": 0.12,
      "mobile_money_adoption": "Nascent (M-Gurush by MTN, mPesa)",
      "tech_hubs": ["Juba (218 Space)"],
      "notes": "Extremely limited telecom infrastructure; Zain and MTN operators; no submarine cable (landlocked); relies on satellite and fibre from Uganda/Kenya; internet extremely expensive; mobile money adoption growing from very low base; power outages limit connectivity."
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
    print(f"\nBatch 2 done. {updated} countries updated.")


if __name__ == "__main__":
    main()
