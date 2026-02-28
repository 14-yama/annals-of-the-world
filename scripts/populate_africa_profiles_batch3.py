#!/usr/bin/env python3
"""
Populate empty country_profile sections for African countries Sudan–Zimbabwe.
Data sourced from: World Bank, IMF, UNDP HDR, CIA Factbook, Transparency International,
RSF, EIU, Fragile States Index, ITU, UNESCO (publicly available 2023-2024 estimates).

Usage: python3 scripts/populate_africa_profiles_batch3.py
"""
import json, os

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "geo-registry", "places", "countries",
)

DATA = {
  "sudan": {
    "demographics": {
      "median_age": 19.7,
      "urbanization_pct": 36.0,
      "fertility_rate": 4.4,
      "life_expectancy": 66.1,
      "infant_mortality_per_1k": 41.0,
      "literacy_rate_pct": 60.7,
      "net_migration_rate": -3.0
    },
    "natural_resources": {
      "primary": ["petroleum", "gold", "chromium ore", "iron ore", "copper", "manganese", "zinc", "mica", "silver", "natural gas", "gum arabic"],
      "resource_dependency_pct_gdp": 15,
      "notes": "World's largest producer of gum arabic (~80% global supply); gold second-largest export (artisanal mining ~80%); post-2011 lost 75% of oil revenue to South Sudan's secession; Merowe Dam (largest in Africa at commissioning); agriculture employs 80% of workforce; Nile Valley fertile land."
    },
    "military": {
      "budget_usd": "2 billion",
      "pct_of_gdp": 3.0,
      "active_personnel": 100000,
      "reserve_personnel": 20000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU (suspended)", "Arab League", "IGAD", "OIC"],
      "notes": "Civil war since April 2023 between SAF (Sudanese Armed Forces, Gen. al-Burhan) and RSF (Rapid Support Forces, Gen. Hemedti, evolved from Janjaweed); devastating humanitarian crisis; Wagner Group ties to RSF; US/ICC sanctions history; Darfur atrocities ongoing."
    },
    "trade": {
      "top_exports": ["gold", "sesame seeds", "gum arabic", "livestock", "cotton", "peanuts", "hibiscus"],
      "top_imports": ["wheat/food", "petroleum products (post-South Sudan split)", "machinery", "vehicles", "medicines", "sugar"],
      "major_partners": ["UAE", "China", "Saudi Arabia", "Egypt", "India", "Turkey", "Ethiopia", "Qatar"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 3.0
    },
    "infrastructure": {
      "internet_penetration_pct": 28.0,
      "electricity_access_pct": 54.0,
      "mobile_subscriptions_per_100": 68,
      "railway_km": 4725,
      "paved_roads_pct": 6
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 20, "rank": 162, "year": 2023},
      "press_freedom_index": {"rank": 149, "year": 2024},
      "democracy_index": {"score": 2.47, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 108.1, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Saharan desert (north)", "Sahelian (central)", "Tropical savanna (south)"],
      "co2_emissions_mt": 19,
      "renewable_energy_pct": 60,
      "natural_hazards": ["droughts", "dust storms (haboob)", "floods (Nile)", "desertification"],
      "protected_areas_pct": 6
    },
    "debt_aid": {
      "national_debt_pct_gdp": 186.0,
      "foreign_aid_received_usd": "1.5 billion",
      "notes": "Catastrophic civil war (2023–) has destroyed economy; HIPC debt relief process was progressing before war; US sanctions partially lifted (2017) then re-applied; hyperinflation; currency black market; GDP collapsed; humanitarian appeal $2.7B+ (2024)."
    },
    "education": {
      "primary_enrollment_pct": 65,
      "secondary_enrollment_pct": 35,
      "tertiary_enrollment_pct": 17,
      "pisa_participation": False,
      "top_universities": ["University of Khartoum (1902, oldest in Sudan)", "Ahfad University for Women", "Sudan University of Science and Technology", "University of Gezira"],
      "notes": "University of Khartoum historically prestigious; 2023 war destroyed campuses and displaced students; Arabic main language of instruction; Arabicization policy since 1990s; Khalwa (Islamic schools) widespread; north-south education gap persists after South Sudan split."
    },
    "diaspora_migration": {
      "diaspora_population": "4 million+ (Saudi Arabia, UAE, Egypt, Chad, South Sudan, UK, USA, Gulf states)",
      "refugees_hosted": 1100000,
      "refugees_produced": 1500000,
      "remittances_usd": "900 million",
      "notes": "2023 civil war created 8 million displaced (largest displacement crisis globally); 1.5M+ refugees to Chad, Egypt, South Sudan, Ethiopia; hosts Eritrean, Ethiopian, South Sudanese refugees; Darfur IDPs (since 2003); Gulf diaspora remittances were vital pre-war."
    },
    "digital_economy": {
      "e_government_index": 0.28,
      "mobile_money_adoption": "Growing (MTN MoMo, Bankak)",
      "tech_hubs": ["Khartoum (249Startups — disrupted by war)"],
      "notes": "Telecom infrastructure severely damaged in 2023 war; Zain Sudan, MTN Sudan, Sudani operators; internet shutdowns during protests and war; pre-war fintech growth (Bankak app); submarine cable via Egypt; war has set digital development back years."
    }
  },
  "tanzania": {
    "demographics": {
      "median_age": 17.7,
      "urbanization_pct": 37.4,
      "fertility_rate": 4.6,
      "life_expectancy": 66.2,
      "infant_mortality_per_1k": 36.0,
      "literacy_rate_pct": 77.9,
      "net_migration_rate": -0.5
    },
    "natural_resources": {
      "primary": ["gold", "diamonds", "tanzanite (unique to Tanzania)", "gemstones (rubies, sapphires)", "natural gas", "iron ore", "coal", "nickel", "tin", "phosphates", "hydropower", "wildlife (tourism)"],
      "resource_dependency_pct_gdp": 8,
      "notes": "Africa's 4th-largest gold producer (Geita, NorthMara, Bulyanhulu mines); tanzanite found only near Mount Kilimanjaro; massive offshore natural gas reserves (~57 tcf, Blocks 1&4); Williamson diamond mine; richest gemstone diversity in Africa; Serengeti/Ngorongoro tourism; clove production (Zanzibar)."
    },
    "military": {
      "budget_usd": "700 million",
      "pct_of_gdp": 1.0,
      "active_personnel": 27000,
      "reserve_personnel": 80000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC", "EAC"],
      "notes": "Tanzania People's Defence Force (TPDF); historically supported liberation movements (ANC, FRELIMO, ZANU); intervened in Uganda (1978–79, toppled Idi Amin); deployed in DRC (MONUSCO Force Intervention Brigade); Zanzibar has separate police force; growing defence relationship with Turkey."
    },
    "trade": {
      "top_exports": ["gold", "tobacco", "cashew nuts", "coffee", "cloves (Zanzibar)", "tea", "cotton", "gems", "fish/seaweed"],
      "top_imports": ["petroleum", "machinery", "vehicles", "iron/steel", "food", "palm oil", "chemicals"],
      "major_partners": ["India", "UAE", "China", "Switzerland (gold)", "South Africa", "Kenya", "Congo (DRC)", "Japan"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 0.8
    },
    "infrastructure": {
      "internet_penetration_pct": 35.0,
      "electricity_access_pct": 42.0,
      "mobile_subscriptions_per_100": 87,
      "railway_km": 4567,
      "paved_roads_pct": 7
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 40, "rank": 87, "year": 2023},
      "press_freedom_index": {"rank": 97, "year": 2024},
      "democracy_index": {"score": 4.83, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 78.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (coast/islands)", "Semi-arid (central plateau)", "Highland (mountains)", "Equatorial (Lake Victoria region)"],
      "co2_emissions_mt": 14,
      "renewable_energy_pct": 86,
      "natural_hazards": ["droughts", "floods", "earthquakes (East African Rift)", "volcanic activity (Ol Doinyo Lengai)"],
      "protected_areas_pct": 38
    },
    "debt_aid": {
      "national_debt_pct_gdp": 42.0,
      "foreign_aid_received_usd": "2.5 billion",
      "notes": "One of Africa's fastest-growing economies (6-7% GDP growth); Standard Gauge Railway (SGR) under construction (Dar–Mwanza, Chinese-funded); Julius Nyerere Hydropower Station (2,115 MW, Africa's largest new dam); LNG export terminal planned ($30B); Magufuli's anti-corruption legacy; President Samia (first female president)."
    },
    "education": {
      "primary_enrollment_pct": 91,
      "secondary_enrollment_pct": 32,
      "tertiary_enrollment_pct": 4,
      "pisa_participation": False,
      "top_universities": ["University of Dar es Salaam (1961)", "Sokoine University of Agriculture", "Muhimbili University of Health and Sciences", "Nelson Mandela African Institution of Science and Technology"],
      "notes": "Swahili medium of instruction in primary schools (English in secondary/tertiary); fee-free basic education since 2016 (enrollment surged); secondary transition gap persists; Zanzibar has semi-autonomous education system; UDSM historical hub of African nationalism."
    },
    "diaspora_migration": {
      "diaspora_population": "500,000+ (Kenya, UK, USA, Canada, UAE, South Africa)",
      "refugees_hosted": 280000,
      "refugees_produced": 5000,
      "remittances_usd": "500 million",
      "notes": "Hosts Burundian and Congolese refugees (Nyarugusu, Nduta, Mtendeli camps); historically generous refugee policy; repatriation of Burundians recently emphasised; internal migration to Dar es Salaam (fastest-growing city in Africa)."
    },
    "digital_economy": {
      "e_government_index": 0.42,
      "mobile_money_adoption": "Very high (M-Pesa by Vodacom, Tigo Pesa, Airtel Money — Tanzania pioneered interoperable mobile money)",
      "tech_hubs": ["Dar es Salaam (Buni Hub, Sahara Ventures, COSTECH Hub)"],
      "notes": "Mobile money interoperability achieved first in Africa (2014); M-Pesa transactions = 50%+ of GDP; Vodacom, Airtel, Tigo, TTCL, Halotel operators; EASSy and SEACOM submarine cables; electronic levy controversy (2022); growing fintech ecosystem."
    }
  },
  "togo": {
    "demographics": {
      "median_age": 19.4,
      "urbanization_pct": 44.0,
      "fertility_rate": 4.1,
      "life_expectancy": 61.4,
      "infant_mortality_per_1k": 42.0,
      "literacy_rate_pct": 66.5,
      "net_migration_rate": -0.5
    },
    "natural_resources": {
      "primary": ["phosphates", "limestone", "marble", "iron ore", "manganese", "salt", "arable land"],
      "resource_dependency_pct_gdp": 8,
      "notes": "Major phosphate producer (4th in Africa historically, deposits depleted from peak); Lomé port is West Africa's deep-water continental hub (transhipment); agriculture employs 65% of population (coffee, cocoa, cotton); clinker/cement production for region."
    },
    "military": {
      "budget_usd": "80 million",
      "pct_of_gdp": 1.6,
      "active_personnel": 11000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "ECOWAS"],
      "notes": "Forces Armées Togolaises (FAT); military dominated politics (Gnassingbé dynasty since 1967); deployed in Sahel counter-terrorism; growing jihadist threat in northern Savanes region; French military cooperation; ECOWAS mediator role."
    },
    "trade": {
      "top_exports": ["clinker/cement", "phosphates", "cotton", "coffee", "cocoa", "palm oil", "re-exports (transit trade)"],
      "top_imports": ["petroleum", "food (rice)", "machinery", "vehicles", "chemicals", "consumer goods"],
      "major_partners": ["Benin", "Burkina Faso (transit)", "India", "China", "Ghana", "Niger", "France", "Belgium"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 5.5
    },
    "infrastructure": {
      "internet_penetration_pct": 25.0,
      "electricity_access_pct": 54.0,
      "mobile_subscriptions_per_100": 65,
      "railway_km": 568,
      "paved_roads_pct": 21
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 29, "rank": 130, "year": 2023},
      "press_freedom_index": {"rank": 78, "year": 2024},
      "democracy_index": {"score": 2.97, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 82.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (south, two rainy seasons)", "Tropical savanna (north, one rainy season)"],
      "co2_emissions_mt": 4,
      "renewable_energy_pct": 25,
      "natural_hazards": ["floods", "droughts (north)", "coastal erosion", "deforestation"],
      "protected_areas_pct": 11
    },
    "debt_aid": {
      "national_debt_pct_gdp": 69.0,
      "foreign_aid_received_usd": "350 million",
      "notes": "Lomé port drives transit trade economy for landlocked neighbours; CFA franc zone (BCEAO); Gnassingbé family in power since 1967; PND (Plan National de Développement); growing security costs from Sahel jihadist spillover."
    },
    "education": {
      "primary_enrollment_pct": 94,
      "secondary_enrollment_pct": 52,
      "tertiary_enrollment_pct": 15,
      "pisa_participation": False,
      "top_universities": ["University of Lomé (1970)", "University of Kara"],
      "notes": "French language of instruction; free primary education since 2008; north-south education gap; gender gap narrowing; Koranic schools alongside secular; University of Lomé overcrowded (~70,000 students); PASEC assessments."
    },
    "diaspora_migration": {
      "diaspora_population": "500,000+ (Ghana, Nigeria, France, Germany, USA, Benin)",
      "refugees_hosted": 3000,
      "refugees_produced": 10000,
      "remittances_usd": "500 million",
      "notes": "Historical migration to Ghana (Ewe cross-border community); traders across West Africa; protest-related emigration (2005, 2017 political crises); diaspora contributes to political opposition; Nana Benz market women historical trading class."
    },
    "digital_economy": {
      "e_government_index": 0.38,
      "mobile_money_adoption": "Growing rapidly (Flooz by Moov, T-Money by Togocel)",
      "tech_hubs": ["Lomé (Woelab, first FabLab in West Africa)"],
      "notes": "Woelab famous for building 3D printer from e-waste; TogoFirst.com economic information portal; Togocel and Moov Africa operators; ACE submarine cable (Lomé landing); digital ID system; e-government services expanding."
    }
  },
  "tunisia": {
    "demographics": {
      "median_age": 33.1,
      "urbanization_pct": 70.1,
      "fertility_rate": 2.1,
      "life_expectancy": 77.4,
      "infant_mortality_per_1k": 12.0,
      "literacy_rate_pct": 81.8,
      "net_migration_rate": -1.5
    },
    "natural_resources": {
      "primary": ["petroleum", "phosphates", "iron ore", "lead", "zinc", "salt", "natural gas"],
      "resource_dependency_pct_gdp": 7,
      "notes": "World's 5th-largest phosphate producer (Gafsa basin, CPG); oil production declining (~35,000 bpd); dates (Deglet Nour, world-class quality); olive oil (2nd/3rd largest global exporter); fisheries; significant solar energy potential (Saharan south)."
    },
    "military": {
      "budget_usd": "1.2 billion",
      "pct_of_gdp": 2.5,
      "active_personnel": 36000,
      "reserve_personnel": 12000,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "Arab League", "Francophonie", "OIC"],
      "notes": "Professional apolitical military (did not fire on protesters during 2011 revolution); counter-terrorism operations (Chaambi Mountains, Libyan border); USAFRICOM Major Non-NATO Ally; deployed buffer zone border with Libya; arms from US, France, Turkey."
    },
    "trade": {
      "top_exports": ["textiles/clothing", "electrical machinery/automotive parts", "olive oil", "phosphoric acid/fertiliser", "dates", "petroleum products", "citrus"],
      "top_imports": ["petroleum/energy", "machinery", "vehicles", "food (wheat)", "chemicals", "iron/steel"],
      "major_partners": ["France (30%)", "Italy", "Germany", "Spain", "Libya", "China", "Turkey", "Algeria"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 5.5
    },
    "infrastructure": {
      "internet_penetration_pct": 71.0,
      "electricity_access_pct": 100.0,
      "mobile_subscriptions_per_100": 126,
      "railway_km": 2165,
      "paved_roads_pct": 68
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 40, "rank": 87, "year": 2023},
      "press_freedom_index": {"rank": 118, "year": 2024},
      "democracy_index": {"score": 4.29, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 68.4, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Mediterranean (north)", "Semi-arid (central steppes)", "Saharan desert (south)"],
      "co2_emissions_mt": 28,
      "renewable_energy_pct": 5,
      "natural_hazards": ["droughts", "floods", "earthquakes (minor)", "desertification", "soil erosion"],
      "protected_areas_pct": 8
    },
    "debt_aid": {
      "national_debt_pct_gdp": 80.0,
      "foreign_aid_received_usd": "750 million",
      "notes": "Birthplace of Arab Spring (2010-11); economy struggled post-revolution; President Saied's 2021 power consolidation; IMF $1.9B deal stalled; subsidy reform resistance; EU migration cooperation deal; Tunisian dinar closely managed; Carthage historical tourism asset."
    },
    "education": {
      "primary_enrollment_pct": 99,
      "secondary_enrollment_pct": 80,
      "tertiary_enrollment_pct": 32,
      "pisa_participation": True,
      "top_universities": ["University of Tunis (1960)", "University of Carthage", "University of Sfax", "Tunis Business School", "ESPRIT (engineering)"],
      "notes": "High tertiary enrollment for Africa/MENA; Bourguiba-era education investment; French-Arabic bilingual system; high graduate unemployment (~30%); strong STEM tradition; engineering schools prestigious; PISA participation but low scores."
    },
    "diaspora_migration": {
      "diaspora_population": "1.5 million+ (France, Italy, Germany, Gulf states, Canada, Libya)",
      "refugees_hosted": 9000,
      "refugees_produced": 5000,
      "remittances_usd": "2.3 billion",
      "notes": "Remittances significant (~5.5% GDP); large French-Tunisian community; irregular migration surge to Italy via boats (Sfax/Lampedusa route); sub-Saharan migrants transit through Tunisia; post-revolution youth 'harragas' (irregular migrants)."
    },
    "digital_economy": {
      "e_government_index": 0.55,
      "mobile_money_adoption": "Growing (D17 mobile payment, Flouci app)",
      "tech_hubs": ["Tunis (Techpark Elgazala, BIAT Labs)", "Sfax", "Smart Tunisia programme"],
      "notes": "Elgazala Technopark (2001, first in Africa); strong nearshoring/BPO for French market; Startup Act 2018 (progressive startup legislation); Tunisie Telecom, Ooredoo, Orange operators; submarine cables to Europe; 50,000+ IT professionals; francophone tech outsourcing hub."
    }
  },
  "uganda": {
    "demographics": {
      "median_age": 15.7,
      "urbanization_pct": 26.2,
      "fertility_rate": 4.7,
      "life_expectancy": 63.4,
      "infant_mortality_per_1k": 33.0,
      "literacy_rate_pct": 76.5,
      "net_migration_rate": -2.0
    },
    "natural_resources": {
      "primary": ["copper", "cobalt", "petroleum (Lake Albert basin)", "gold", "hydropower", "limestone", "salt", "arable land", "coltan", "tin"],
      "resource_dependency_pct_gdp": 3,
      "notes": "Oil discovered in Lake Albert Rift Basin (~6.5 billion barrels reserves); EACOP (East Africa Crude Oil Pipeline to Tanga, Tanzania) under construction with TotalEnergies; copper-cobalt deposits (Kilembe); coffee (robusta, main export); fertile volcanic soils; Lake Victoria fisheries (Nile perch)."
    },
    "military": {
      "budget_usd": "1 billion",
      "pct_of_gdp": 2.0,
      "active_personnel": 45000,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "EAC", "IGAD"],
      "notes": "Uganda People's Defence Forces (UPDF); Museveni came to power via NRA bush war (1986); UPDF deployed in Somalia (AMISOM/ATMIS — largest contributor), DRC, South Sudan; LRA (Joseph Kony) defeated domestically but remnants in CAR/DRC; ADF (Allied Democratic Forces) operations in eastern DRC."
    },
    "trade": {
      "top_exports": ["coffee", "gold", "fish (Nile perch)", "tea", "tobacco", "flowers", "vanilla", "sesame", "maize", "cement"],
      "top_imports": ["petroleum", "vehicles", "machinery", "iron/steel", "pharmaceuticals", "electronics"],
      "major_partners": ["Kenya", "UAE (gold)", "Italy", "India", "China", "South Sudan", "DR Congo", "Rwanda", "Germany"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 4.5
    },
    "infrastructure": {
      "internet_penetration_pct": 26.0,
      "electricity_access_pct": 42.0,
      "mobile_subscriptions_per_100": 66,
      "railway_km": 1244,
      "paved_roads_pct": 4
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 26, "rank": 141, "year": 2023},
      "press_freedom_index": {"rank": 128, "year": 2024},
      "democracy_index": {"score": 4.39, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 92.7, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical equatorial (south)", "Tropical savanna (north)", "Highland/montane (Rwenzori Mountains)"],
      "co2_emissions_mt": 6,
      "renewable_energy_pct": 90,
      "natural_hazards": ["droughts (Karamoja)", "floods", "landslides (Mount Elgon)", "earthquakes (Western Rift)"],
      "protected_areas_pct": 17
    },
    "debt_aid": {
      "national_debt_pct_gdp": 48.0,
      "foreign_aid_received_usd": "2.2 billion",
      "notes": "EACOP oil pipeline ($3.5B) and Tilenga/Kingfisher oil projects ($10B+) to transform economy; Karuma (600MW) and Isimba (183MW) hydropower dams; Anti-Homosexuality Act (2023) triggered US sanctions/World Bank lending pause; Museveni in power since 1986."
    },
    "education": {
      "primary_enrollment_pct": 92,
      "secondary_enrollment_pct": 26,
      "tertiary_enrollment_pct": 5,
      "pisa_participation": False,
      "top_universities": ["Makerere University (1922)", "Uganda Christian University", "Mbarara University of Science and Technology", "Kyambogo University"],
      "notes": "Makerere University historically one of Africa's finest (educated leaders across East Africa); Universal Primary Education (UPE, 1997) boosted enrollment (from 2.5M to 8M+) but quality dropped; Universal Secondary Education (USE, 2007); private school sector large."
    },
    "diaspora_migration": {
      "diaspora_population": "1 million+ (Kenya, South Africa, UK, USA, Canada, Rwanda, South Sudan)",
      "refugees_hosted": 1500000,
      "refugees_produced": 10000,
      "remittances_usd": "1.3 billion",
      "notes": "Hosts Africa's largest refugee population (~1.5M from DRC, South Sudan, Burundi, Somalia); progressive refugee policy (right to work, land allocation); Bidibidi and Nakivale settlements; Idi Amin-era Ugandan Asian expulsion (1972) created diaspora."
    },
    "digital_economy": {
      "e_government_index": 0.40,
      "mobile_money_adoption": "Very high (MTN MoMo dominant, Airtel Money)",
      "tech_hubs": ["Kampala (Innovation Village, Outbox Hub, Hive Colab — Africa's first co-working tech hub)"],
      "notes": "Mobile money ~65% of GDP in transactions; social media/OTT tax (controversial, introduced 2018 then modified); MTN, Airtel, Africell operators; Hive Colab was first tech hub in Africa (2010); growing fintech (Xente, NALA); SEACOM submarine cable access via Kenya."
    }
  },
  "western-sahara": {
    "demographics": {
      "median_age": 28.0,
      "urbanization_pct": 87.0,
      "fertility_rate": 2.5,
      "life_expectancy": 70.0,
      "infant_mortality_per_1k": 35.0,
      "literacy_rate_pct": 70.0,
      "net_migration_rate": 0.0
    },
    "natural_resources": {
      "primary": ["phosphates (Bou Craa)", "fish", "iron ore", "sand", "solar/wind energy potential"],
      "resource_dependency_pct_gdp": 30,
      "notes": "Bou Craa phosphate mine (world's largest phosphate conveyor belt, 100km to El Aaiún port, operated by OCP Morocco); some of world's richest fishing waters (Atlantic coast); offshore oil/gas exploration blocked by sovereignty dispute; vast solar/wind potential; Morocco controls resource-rich western zone; Sahrawi Republic (SADR) controls eastern buffer zone."
    },
    "military": {
      "budget_usd": "N/A (disputed territory)",
      "pct_of_gdp": 0,
      "active_personnel": 0,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU (SADR recognised by some members)", "Polisario Front"],
      "notes": "Morocco controls 80% of territory (west of berm/sand wall); Polisario Front (Sahrawi liberation movement) based in Tindouf camps, Algeria; MINURSO (UN Mission for 1991 ceasefire referendum, never held); Morocco resumed military operations (2020 ceasefire breakdown); 2,720-km sand berm/wall divides territory."
    },
    "trade": {
      "top_exports": ["phosphates (via Morocco)", "fish products (via Morocco)"],
      "top_imports": ["food", "fuel", "construction materials (mostly via Moroccan supply chain)"],
      "major_partners": ["Morocco (controls trade)", "Spain (fisheries agreements)", "EU"],
      "trade_balance": "N/A (integrated into Moroccan economy)",
      "remittances_pct_gdp": 0
    },
    "infrastructure": {
      "internet_penetration_pct": 30.0,
      "electricity_access_pct": 55.0,
      "mobile_subscriptions_per_100": 50,
      "railway_km": 0,
      "paved_roads_pct": 30
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 0, "rank": 0, "year": 2023},
      "press_freedom_index": {"rank": 0, "year": 2024},
      "democracy_index": {"score": 0, "category": "N/A (non-self-governing territory)", "year": 2023},
      "fragile_states_index": {"score": 0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Hot desert (Saharan)", "Coastal desert (modified by cold Canary Current)"],
      "co2_emissions_mt": 0.5,
      "renewable_energy_pct": 10,
      "natural_hazards": ["sandstorms/sirocco", "droughts", "flash floods"],
      "protected_areas_pct": 0
    },
    "debt_aid": {
      "national_debt_pct_gdp": 0,
      "foreign_aid_received_usd": "100 million (humanitarian aid to Tindouf camps via UNHCR/WFP/Algeria)",
      "notes": "Africa's last major decolonisation dispute; Morocco claims sovereignty based on historical ties; ICJ 1975 advisory opinion found no sovereignty; Sahrawi Arab Democratic Republic recognised by ~40 states; US recognised Morocco sovereignty (2020, Trump-Abraham Accords deal); EU Court invalidated fisheries/agriculture deals with Morocco over Western Sahara resources; 173,000 Sahrawi refugees in Tindouf camps (Algeria)."
    },
    "education": {
      "primary_enrollment_pct": 80,
      "secondary_enrollment_pct": 50,
      "tertiary_enrollment_pct": 5,
      "pisa_participation": False,
      "top_universities": [],
      "notes": "Moroccan-controlled zone uses Moroccan curriculum; Tindouf refugee camps have Cuban and Algerian-supported education; sahrawi students receive scholarships to Cuba, Algeria, Spain, Libya; near-universal literacy in Polisario-administered camps through Cuban teachers; limited higher education infrastructure."
    },
    "diaspora_migration": {
      "diaspora_population": "173,000+ (Tindouf refugee camps, Algeria; smaller groups in Spain, Mauritania, France)",
      "refugees_hosted": 0,
      "refugees_produced": 173600,
      "remittances_usd": "5 million",
      "notes": "Tindouf camps population (since 1975); Sahrawi diaspora in Spain (historic colonial ties); Morocco has encouraged settler migration into Western Sahara (Moroccan settlers now outnumber indigenous Sahrawis); MINURSO mandate; self-determination referendum repeatedly blocked."
    },
    "digital_economy": {
      "e_government_index": 0,
      "mobile_money_adoption": "N/A (uses Moroccan telecom infrastructure in controlled zone)",
      "tech_hubs": [],
      "notes": "Moroccan-controlled zone uses Maroc Telecom, Orange, Inwi; Tindouf camps have limited satellite internet; no independent digital infrastructure; Morocco has invested in renewables (Foum el Oued wind farm) in the territory."
    }
  },
  "zambia": {
    "demographics": {
      "median_age": 16.9,
      "urbanization_pct": 45.5,
      "fertility_rate": 4.3,
      "life_expectancy": 63.9,
      "infant_mortality_per_1k": 40.0,
      "literacy_rate_pct": 86.7,
      "net_migration_rate": -0.5
    },
    "natural_resources": {
      "primary": ["copper", "cobalt", "zinc", "lead", "coal", "emeralds", "gold", "silver", "uranium", "hydropower", "manganese"],
      "resource_dependency_pct_gdp": 15,
      "notes": "Africa's 2nd-largest copper producer (~700,000 tonnes/year, Copperbelt); world's 2nd-largest cobalt producer; Kagem emerald mine (world's largest, 75% owned by Gemfields); copper accounts for 70%+ of export revenue; Victoria Falls shared with Zimbabwe; Kariba Dam (hydropower, shared); agricultural potential (underutilised arable land)."
    },
    "military": {
      "budget_usd": "400 million",
      "pct_of_gdp": 1.3,
      "active_personnel": 16500,
      "reserve_personnel": 0,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC", "COMESA", "Commonwealth"],
      "notes": "Zambia Defence Force (ZDF); historically hosted liberation movements (ANC, SWAPO); UN peacekeeping contributor; mostly peaceful history (no civil war); professional but under-resourced; Chinese military cooperation growing."
    },
    "trade": {
      "top_exports": ["copper (70%+ of export revenue)", "cobalt", "emeralds", "tobacco", "sugar", "cotton", "maize", "electricity"],
      "top_imports": ["petroleum", "machinery", "vehicles", "fertiliser", "food", "chemicals", "iron/steel"],
      "major_partners": ["Switzerland (copper trading)", "China", "DR Congo", "Singapore", "South Africa", "India", "UAE", "Japan"],
      "trade_balance": "surplus (copper prices dependent)",
      "remittances_pct_gdp": 1.5
    },
    "infrastructure": {
      "internet_penetration_pct": 24.0,
      "electricity_access_pct": 43.0,
      "mobile_subscriptions_per_100": 99,
      "railway_km": 3126,
      "paved_roads_pct": 22
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 35, "rank": 105, "year": 2023},
      "press_freedom_index": {"rank": 57, "year": 2024},
      "democracy_index": {"score": 4.49, "category": "Hybrid regime", "year": 2023},
      "fragile_states_index": {"score": 80.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Tropical (north, wetter)", "Subtropical (south)", "Semi-arid (Luangwa/Zambezi valleys)"],
      "co2_emissions_mt": 8,
      "renewable_energy_pct": 85,
      "natural_hazards": ["droughts", "floods", "power shortages (Kariba Dam low water levels)"],
      "protected_areas_pct": 40
    },
    "debt_aid": {
      "national_debt_pct_gdp": 90.0,
      "foreign_aid_received_usd": "1.2 billion",
      "notes": "First African country to default on sovereign bonds during COVID-19 (2020); Common Framework debt restructuring ($6.3B, China/bondholders); President Hichilema (2021) privatisation-friendly; copper production target 3M tonnes by 2031; load-shedding crisis (2024, drought reduced Kariba hydro); IMF $1.3B programme."
    },
    "education": {
      "primary_enrollment_pct": 88,
      "secondary_enrollment_pct": 46,
      "tertiary_enrollment_pct": 4,
      "pisa_participation": False,
      "top_universities": ["University of Zambia (UNZA, 1966)", "Copperbelt University (CBU)", "Mulungushi University", "Cavendish University Zambia"],
      "notes": "Free primary education (2002); English medium of instruction; UNZA/CBU historically important; Zambian Open University for distance learning; rural school quality challenges; SACMEQ assessment participant; strong student activism tradition."
    },
    "diaspora_migration": {
      "diaspora_population": "300,000+ (South Africa, UK, Australia, USA, Botswana, Namibia)",
      "refugees_hosted": 100000,
      "refugees_produced": 5000,
      "remittances_usd": "250 million",
      "notes": "Hosts Congolese (DRC) refugees (Meheba, Mayukwayukwa settlements); skilled professionals emigrate to South Africa and UK; Asian community (Indian, Chinese) significant in business; 2021 peaceful power transfer (Hichilema election) praised."
    },
    "digital_economy": {
      "e_government_index": 0.40,
      "mobile_money_adoption": "Growing (MTN MoMo, Airtel Money, Zamtel Kwacha)",
      "tech_hubs": ["Lusaka (BongoHive — first tech hub in Zambia)", "Copperbelt"],
      "notes": "BongoHive established 2011; three MNOs (MTN, Airtel, Zamtel); mobile money interoperability progressing; EASSy submarine cable access via Mozambique; Zambia ICT Authority; government digitisation agenda; fintech growing (Zoona pivoted to payments infrastructure)."
    }
  },
  "zimbabwe": {
    "demographics": {
      "median_age": 20.5,
      "urbanization_pct": 32.2,
      "fertility_rate": 3.4,
      "life_expectancy": 61.5,
      "infant_mortality_per_1k": 34.0,
      "literacy_rate_pct": 86.5,
      "net_migration_rate": -4.0
    },
    "natural_resources": {
      "primary": ["platinum group metals", "gold", "diamonds", "lithium", "chromium", "coal", "iron ore", "vanadium", "tin", "copper", "nickel", "asbestos"],
      "resource_dependency_pct_gdp": 12,
      "notes": "Africa's largest lithium reserves (Bikita, Arcadia mines — global EV demand driver); significant PGM deposits (Great Dyke); gold has long been major export; Marange diamond fields (controversial); tobacco is top agricultural export; fertile agricultural land (former 'breadbasket of Africa'); Victoria Falls tourism."
    },
    "military": {
      "budget_usd": "350 million",
      "pct_of_gdp": 1.6,
      "active_personnel": 29000,
      "reserve_personnel": 21800,
      "nuclear_status": "Non-nuclear",
      "alliances": ["AU", "SADC"],
      "notes": "Zimbabwe Defence Forces (ZDF); played role in 2017 coup removing Mugabe; deployed in DRC (SADC); liberation war background (ZANLA/ZIPRA); Gukurahundi massacres (1983-87, Matabeleland); military-business nexus (mining concessions); sanctioned officers."
    },
    "trade": {
      "top_exports": ["gold", "tobacco", "nickel", "diamonds", "ferrochrome", "platinum", "lithium", "cotton"],
      "top_imports": ["petroleum", "electricity", "machinery", "vehicles", "food (wheat, rice)", "chemicals", "fertiliser"],
      "major_partners": ["South Africa (40%+)", "UAE", "Mozambique", "China", "Zambia", "Singapore", "UK", "India"],
      "trade_balance": "deficit",
      "remittances_pct_gdp": 10.0
    },
    "infrastructure": {
      "internet_penetration_pct": 35.0,
      "electricity_access_pct": 50.0,
      "mobile_subscriptions_per_100": 92,
      "railway_km": 3427,
      "paved_roads_pct": 19
    },
    "governance_indices": {
      "corruption_perception_index": {"score": 24, "rank": 149, "year": 2023},
      "press_freedom_index": {"rank": 126, "year": 2024},
      "democracy_index": {"score": 2.53, "category": "Authoritarian", "year": 2023},
      "fragile_states_index": {"score": 95.0, "year": 2024}
    },
    "climate_environment": {
      "climate_zones": ["Subtropical (highveld plateau)", "Semi-arid (lowveld)", "Tropical (Zambezi Valley)"],
      "co2_emissions_mt": 12,
      "renewable_energy_pct": 35,
      "natural_hazards": ["droughts (El Niño related)", "floods", "Cyclone Idai (2019, devastating)"],
      "protected_areas_pct": 28
    },
    "debt_aid": {
      "national_debt_pct_gdp": 93.0,
      "foreign_aid_received_usd": "750 million",
      "notes": "Chronic economic crisis; hyperinflation history ($100 trillion banknotes, 2008); new ZiG currency (Zimbabwe Gold, April 2024); arrears to World Bank/AfDB/IMF ($14B+ external debt); land reform legacy; US/EU sanctions (ZIDERA); lithium export ban (raw ore) to encourage domestic processing."
    },
    "education": {
      "primary_enrollment_pct": 89,
      "secondary_enrollment_pct": 52,
      "tertiary_enrollment_pct": 10,
      "pisa_participation": False,
      "top_universities": ["University of Zimbabwe (1952)", "National University of Science and Technology (NUST)", "Midlands State University", "Africa University (pan-African, UMC affiliated)"],
      "notes": "One of Africa's highest literacy rates (Mugabe-era education investment); O-Level/A-Level British-style system; ZIMSEC examinations; brain drain has severely depleted teaching staff; school fees barrier in economic crisis; strong science/engineering tradition."
    },
    "diaspora_migration": {
      "diaspora_population": "3 million+ (South Africa, UK, Botswana, Australia, Canada, USA, Mozambique, Namibia)",
      "refugees_hosted": 20000,
      "refugees_produced": 30000,
      "remittances_usd": "2 billion",
      "notes": "Massive brain drain (~25% of population in diaspora); South Africa (~1.5M+ Zimbabweans, many undocumented); UK Zimbabwean community large (post-2000 exodus); Zimbabwean professionals (teachers, nurses, doctors) recruited worldwide; remittances ~10% GDP, essential for survival."
    },
    "digital_economy": {
      "e_government_index": 0.35,
      "mobile_money_adoption": "Very high (EcoCash dominant — 90%+ mobile money market, OneMoney, InnBucks)",
      "tech_hubs": ["Harare (Muzinda Hub, Impact Hub)", "Bulawayo"],
      "notes": "EcoCash (Cassava Smartech / Econet) processes ~$8B annually (~80% of Zimbabwe's transactions); mobile money effectively replaced banking for most citizens during currency crises; Econet Wireless (Strive Masiyiwa founded) dominant MNO; Zimbabwe silicon (Cassava, Sasai super-app); currency instability drives digital payment adoption."
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
    print(f"\nBatch 3 done. {updated} countries updated.")


if __name__ == "__main__":
    main()
