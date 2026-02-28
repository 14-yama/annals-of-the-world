#!/usr/bin/env python3
"""
Enhance African countries with new template sections + expanded fields.
Batch 1: Algeria, Angola, Benin, Botswana, Burkina Faso
Sources: World Bank, IMF, CIA Factbook, UNDP HDR, WHO, FAO, GPI, Freedom House,
         WJP, EPI, ITU, WIPO GII, UNWTO (2023-2024 estimates).
"""
import json, os, copy

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "geo-registry", "places", "countries")

# ── New sections + expanded fields for each country ──────────────────────────

DATA = {
"algeria": {
  # ── basics additions ──
  "_basics": {
    "capital_coordinates": {"lat": 36.7538, "lon": 3.0588},
    "other_major_cities": ["Oran", "Constantine", "Annaba", "Blida", "Batna", "Sétif"],
    "national_motto": "By the People and for the People",
    "national_anthem": "Kassaman (We Pledge)",
    "currency_code": "DZD",
    "internet_tld": ".dz",
    "utc_offset": "UTC+1",
    "drives_on": "right"
  },
  # ── new sections ──
  "geography": {
    "coordinates": {"lat": 28.0339, "lon": 1.6596},
    "bounding_box": {"north": 37.09, "south": 18.96, "east": 11.99, "west": -8.67},
    "land_area_km2": 2381741,
    "water_area_km2": 0,
    "coastline_km": 998,
    "borders": ["Tunisia", "Libya", "Niger", "Mali", "Mauritania", "Western Sahara", "Morocco"],
    "border_lengths_km": {"Tunisia": 1034, "Libya": 989, "Niger": 951, "Mali": 1359, "Mauritania": 460, "Western Sahara": 41, "Morocco": 1941},
    "highest_point": {"name": "Mount Tahat", "elevation_m": 2908},
    "lowest_point": {"name": "Chott Melrhir", "elevation_m": -40},
    "terrain": "Mostly high plateau and desert; Atlas Mountains in the north; Sahara covers 80%+ of territory",
    "land_use": {"agricultural_pct": 17.4, "arable_pct": 3.2, "forest_pct": 0.8, "other_pct": 81.8},
    "major_rivers": ["Chelif", "Sebaou", "Medjerda"],
    "major_lakes": ["Chott ech Chergui", "Chott Melrhir"],
    "exclusive_economic_zone_km2": 0,
    "landlocked": False,
    "notes": "Largest country in Africa by area; 80%+ Saharan desert; Tell Atlas and Saharan Atlas mountain ranges; Mediterranean coast."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$195 billion",
    "gdp_ppp_usd": "$580 billion",
    "gdp_per_capita_nominal_usd": 4345,
    "gdp_per_capita_ppp_usd": 12929,
    "gdp_growth_rate_pct": 4.1,
    "inflation_rate_pct": 9.3,
    "unemployment_rate_pct": 11.7,
    "youth_unemployment_rate_pct": 29.7,
    "poverty_rate_pct": 5.5,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 27.6,
    "income_classification": "Lower-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 13, "industry_pct_gdp": 39, "services_pct_gdp": 48},
    "labor_force": 12700000,
    "labor_force_by_sector": {"agriculture_pct": 10, "industry_pct": 31, "services_pct": 59},
    "fdi_inflow_usd": "$1.6 billion",
    "fdi_outflow_usd": "$120 million",
    "foreign_exchange_reserves_usd": "$56 billion",
    "ease_of_doing_business_rank": 157,
    "economic_freedom_index_score": 49.7,
    "credit_rating": {"moodys": "B1", "sp": "", "fitch": "B+"},
    "notes": "Hydrocarbon-dependent economy (95% of export revenue); Sonatrach state oil company; heavy state subsidies on fuel, housing, food; import substitution policy; strict FDI regulations (51/49 rule relaxed 2020)."
  },
  "health": {
    "health_expenditure_pct_gdp": 6.3,
    "health_expenditure_per_capita_usd": 274,
    "physicians_per_1k": 1.8,
    "nurses_midwives_per_1k": 2.2,
    "hospital_beds_per_1k": 1.9,
    "maternal_mortality_per_100k": 112,
    "hiv_prevalence_pct": 0.1,
    "malaria_incidence_per_1k": 0,
    "tuberculosis_incidence_per_100k": 70,
    "access_to_clean_water_pct": 94,
    "access_to_sanitation_pct": 88,
    "vaccination_coverage_pct": 90,
    "stunting_under5_pct": 11,
    "obesity_rate_pct": 27.4,
    "universal_health_coverage_index": 67,
    "leading_causes_of_death": ["Cardiovascular diseases", "Cancer", "Diabetes", "Road accidents"],
    "notes": "Free public healthcare; well-developed hospital network; growing NCD burden; medical tourism to France/Tunisia for specialised care."
  },
  "food_agriculture": {
    "food_security_index_score": 57.5,
    "food_security_index_rank": 68,
    "arable_land_pct": 3.2,
    "agricultural_land_pct": 17.4,
    "irrigated_land_pct": 13,
    "major_crops": ["wheat", "barley", "potatoes", "tomatoes", "dates", "citrus", "olives", "grapes"],
    "major_livestock": ["sheep", "goats", "cattle", "camels"],
    "food_import_dependency_pct": 40,
    "cereal_yield_kg_per_hectare": 1700,
    "agricultural_employment_pct": 10,
    "prevalence_of_undernourishment_pct": 3.0,
    "notes": "Major wheat/barley importer; date palm oases in Sahara (Ghardaia, Biskra); PNDA agricultural renewal programme; dairy sector growing; limited arable land constrains self-sufficiency."
  },
  "energy": {
    "energy_mix": {"fossil_fuels_pct": 99, "hydroelectric_pct": 0.3, "solar_pct": 0.5, "wind_pct": 0.1, "nuclear_pct": 0, "biomass_other_pct": 0.1},
    "installed_capacity_mw": 21000,
    "electricity_production_gwh": 76000,
    "electricity_consumption_per_capita_kwh": 1600,
    "energy_imports_pct": 0,
    "oil_production_bpd": 972000,
    "oil_consumption_bpd": 430000,
    "natural_gas_production_bcm": 100,
    "energy_access_rural_pct": 99,
    "energy_access_urban_pct": 100,
    "notes": "Africa's largest natural gas reserves; OPEC member; Sonatrach 5th-largest gas company globally; Hassi Messaoud oil field; Hassi R'Mel gas field; solar potential enormous (Sahara) but underdeveloped; Tafouk1 solar project planned."
  },
  "transport": {
    "major_airports_international": ["Houari Boumediene (Algiers)", "Ahmed Ben Bella (Oran)", "Mohamed Boudiaf (Constantine)"],
    "major_airports_domestic": ["Batna", "Annaba", "Sétif", "Tlemcen", "Hassi Messaoud"],
    "national_airline": "Air Algérie",
    "major_seaports": ["Algiers", "Oran", "Skikda", "Arzew", "Béjaïa", "Annaba"],
    "major_inland_ports": [],
    "merchant_marine_vessels": 57,
    "registered_vehicles_per_1k": 120,
    "road_fatalities_per_100k": 23,
    "notes": "East-West Highway (1,216 km, connects Morocco border to Tunisia); Trans-Saharan Highway; Algiers Metro (2011); extensive domestic air network to connect Saharan south."
  },
  "tourism": {
    "annual_visitors": 3200000,
    "tourism_revenue_usd": "$265 million",
    "tourism_pct_gdp": 0.1,
    "tourism_employment_pct": 2,
    "unesco_world_heritage_sites": 7,
    "unesco_sites_list": ["Al Qal'a of Beni Hammad", "Djémila", "M'Zab Valley", "Kasbah of Algiers", "Timgad", "Tipasa", "Tassili n'Ajjer"],
    "major_attractions": ["Casbah of Algiers", "Tassili n'Ajjer rock art", "Timgad Roman ruins", "Ghardaia M'zab", "Sahara excursions", "Mediterranean coast"],
    "visa_free_access_countries": 51,
    "henley_passport_rank": 92,
    "notes": "Underdeveloped tourism despite enormous potential; visa restrictions; limited hotel infrastructure outside cities; Saharan tourism growing; Roman ruins rival those in Tunisia."
  },
  "human_rights_gender": {
    "freedom_house_status": "Not Free",
    "freedom_house_score": 32,
    "gender_inequality_index": 0.438,
    "gender_inequality_rank": 104,
    "gender_gap_index_score": 0.602,
    "women_in_parliament_pct": 8,
    "women_labor_force_participation_pct": 15,
    "maternal_mortality_per_100k": 112,
    "child_marriage_pct": 3,
    "fgm_prevalence_pct": 0,
    "lgbtq_legal_status": "Illegal (up to 2 years imprisonment)",
    "death_penalty_status": "Abolitionist in practice (moratorium since 1993)",
    "human_trafficking_tier": "Tier 2 Watch List",
    "child_labor_pct": 5,
    "notes": "Family Code governs personal status; Amazigh cultural rights recognised (2016 constitution); Hirak protest movement 2019-21; press restrictions; women's rights progress mixed."
  },
  "security_stability": {
    "global_peace_index_score": 2.14,
    "global_peace_index_rank": 96,
    "terrorism_index_score": 3.9,
    "terrorism_index_rank": 41,
    "homicide_rate_per_100k": 1.4,
    "active_conflicts": [],
    "border_disputes": ["Western Sahara (supports Polisario/SADR)"],
    "un_peacekeeping_contributions": 0,
    "arms_imports_usd": "$1 billion",
    "internally_displaced_persons": 0,
    "notes": "Relatively stable post-Civil War (1991-2002); strong security apparatus; closed border with Morocco since 1994; arms buildup (largest African military budget); AQIM largely expelled but residual threat in Sahel margins."
  },
  "cultural_heritage": {
    "national_symbols": ["Fennec fox", "Star and crescent"],
    "national_animal": "Fennec fox",
    "national_flower": "Iris",
    "national_dish": "Couscous",
    "national_sport": "Football",
    "major_festivals": ["Independence Day (5 July)", "Revolution Day (1 November)", "Yennayer (Amazigh New Year, 12 January)", "Eid al-Fitr", "Eid al-Adha"],
    "cuisine_highlights": ["Couscous", "Chakchouka", "Mechoui", "Makroud", "Brik/Bourek", "Mint tea"],
    "music_art_traditions": ["Raï (Cheb Khaled, Cheb Mami)", "Chaabi", "Andalusi classical music", "Kabyle music", "Tuareg Saharan blues"],
    "film_industry": "Notable (Z, Battle of Algiers co-production legacy; Algerian Film Commission)",
    "intangible_heritage_items": ["Sbaa ritual", "Ahellil of Gourara", "Annual pilgrimage to the mausoleum of Sidi Abd el-Qader Ben Mohammed"],
    "notable_historical_figures": ["Emir Abdelkader", "Jugurtha", "Saint Augustine", "Albert Camus", "Frantz Fanon", "Kateb Yacine"],
    "world_heritage_sites": ["Djémila", "Timgad", "Tipasa", "M'Zab Valley", "Tassili n'Ajjer", "Kasbah of Algiers", "Al Qal'a of Beni Hammad"],
    "media_landscape": "State-dominated (ENTV, Radio Algérienne); private newspapers; online media growing; press freedom limited",
    "notes": "Rich blend of Amazigh, Arab, Ottoman, French cultural influences; raï music originated in Oran; Algerian literature in French and Arabic; 2022 film 'The Last Queen' international recognition."
  },
  "legal_system": {
    "legal_tradition": "Civil law (French-influenced) with Islamic law for personal status",
    "constitution_year": 2020,
    "sharia_applicability": "Personal status (family law, inheritance)",
    "customary_law_role": "Limited (some Amazigh customary practices in Kabylie)",
    "icc_membership": "Non-member",
    "judicial_independence_score": 0.35,
    "contract_enforcement_days": 630,
    "property_rights_index": 37.7,
    "notes": "Dual French-Islamic legal heritage; 2020 constitutional referendum; Council of State (administrative); Supreme Court; Constitutional Court; state of emergency provisions used historically."
  },
  "comparative_rankings": {
    "_note": "Country position relative to continent and global. 'rank' = 1 is best/largest.",
    "population": {"continent_rank": 1, "global_rank": 32},
    "area": {"continent_rank": 1, "global_rank": 10},
    "gdp_nominal": {"continent_rank": 4, "global_rank": 56},
    "gdp_per_capita": {"continent_rank": 10, "global_rank": 113},
    "hdi": {"continent_rank": 7, "global_rank": 91},
    "life_expectancy": {"continent_rank": 8, "global_rank": 79},
    "ease_of_doing_business": {"continent_rank": 46, "global_rank": 157},
    "internet_penetration": {"continent_rank": 8, "global_rank": 80},
    "press_freedom": {"continent_rank": 40, "global_rank": 136},
    "global_peace_index": {"continent_rank": 18, "global_rank": 96},
    "innovation_index": {"continent_rank": 17, "global_rank": 120},
    "notes": "Africa's largest country by area; top 5 GDP on continent; major gas exporter."
  },
  # ── expanded fields for existing sections ──
  "_expand_demographics": {
    "population_growth_rate_pct": 1.5,
    "urban_population_growth_rate_pct": 2.8,
    "life_expectancy_male": 76.0,
    "life_expectancy_female": 79.0,
    "under5_mortality_per_1k": 23,
    "sex_ratio": 1.02,
    "dependency_ratio": 55.0,
    "population_density_per_km2": 18.9,
    "age_structure": {"0_14_pct": 29, "15_24_pct": 14, "25_54_pct": 42, "55_64_pct": 8, "65_plus_pct": 7}
  },
  "_expand_military": {
    "paramilitary_personnel": 187000,
    "conscription": True,
    "global_firepower_rank": 26
  },
  "_expand_trade": {
    "total_exports_usd": "$38 billion",
    "total_imports_usd": "$35 billion",
    "top_export_destinations": ["Italy", "France", "Spain", "USA", "Turkey"],
    "top_import_origins": ["China", "France", "Italy", "Germany", "Spain"],
    "trade_as_pct_gdp": 37,
    "current_account_balance_usd": "$5 billion",
    "trade_agreements": ["GAFTA", "AfCFTA", "EU Association Agreement"],
    "special_economic_zones": []
  },
  "_expand_infrastructure": {
    "broadband_subscriptions_per_100": 8.5,
    "4g_coverage_pct": 75,
    "5g_availability": False,
    "road_network_km": 108302,
    "waterways_km": 0,
    "submarine_cables": ["SeaMeWe-4", "Alpal-2", "Orval", "Medex"],
    "notes": "East-West Highway; Algiers Metro; national broadband (Algérie Telecom); Algiers-Oran high-speed rail planned."
  },
  "_expand_governance_indices": {
    "rule_of_law_index": {"score": 0.36, "rank": 113, "year": 2023},
    "government_effectiveness_index": {"score": -0.59, "percentile": 26, "year": 2023},
    "regulatory_quality_index": {"score": -0.88, "percentile": 15, "year": 2023},
    "political_stability_index": {"score": -0.74, "percentile": 20, "year": 2023}
  },
  "_expand_climate_environment": {
    "average_temperature_c": 22,
    "average_rainfall_mm": 89,
    "co2_per_capita_t": 3.7,
    "deforestation_rate_pct": 0.5,
    "water_stress_level": "High",
    "environmental_performance_index": {"score": 38.5, "rank": 118, "year": 2022},
    "paris_agreement_status": "Ratified (2016)",
    "biodiversity": {"known_species": 5800, "endemic_species": 300, "threatened_species": 84},
    "notes": "Sahara expanding southward; Great Green Wall participant (limited); water scarcity acute in south; Mediterranean ecosystems under pressure."
  },
  "_expand_debt_aid": {
    "external_debt_usd": "$5 billion",
    "debt_service_pct_revenue": 2,
    "foreign_aid_given_usd": "$100 million",
    "top_donors": ["EU", "France", "Germany"],
    "imf_programme_active": False,
    "world_bank_ida_eligible": False,
    "hipc_status": "N/A"
  },
  "_expand_education": {
    "education_expenditure_pct_gdp": 7.0,
    "primary_completion_rate_pct": 97,
    "gender_parity_index": 1.05,
    "mean_years_of_schooling": 8.0,
    "expected_years_of_schooling": 14.7,
    "pisa_scores": {"reading": 0, "math": 0, "science": 0, "year": 0},
    "student_teacher_ratio_primary": 23,
    "out_of_school_children": 150000,
    "academic_freedom_index": 0.35
  },
  "_expand_diaspora_migration": {
    "diaspora_top_destinations": ["France", "Spain", "Canada", "UK", "Germany"],
    "asylum_seekers": 5000,
    "stateless_persons": 0,
    "internally_displaced_persons": 0,
    "immigration_policy": "Restrictive; transit country for sub-Saharan migrants",
    "remittances_pct_gdp": 1.0,
    "net_migration_rate_per_1k": -0.5
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.42,
    "ict_development_index": 4.7,
    "mobile_money_accounts": 500000,
    "digital_payments_pct_adults": 20,
    "fintech_companies": 15,
    "startup_ecosystem_value_usd": "$100 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 48.0,
    "innovation_index_score": 20.2,
    "innovation_index_rank": 120,
    "ai_readiness_index": 30.0
  },
  "_expand_natural_resources": {
    "resource_curse_risk": "Moderate (Dutch disease symptoms; hydrocarbon dependency)"
  }
},

"angola": {
  "_basics": {
    "capital_coordinates": {"lat": -8.8390, "lon": 13.2894},
    "other_major_cities": ["Huambo", "Lobito", "Benguela", "Lubango", "Malanje", "Cabinda"],
    "national_motto": "Virtue is Stronger United",
    "national_anthem": "Angola Avante! (Forward Angola!)",
    "currency_code": "AOA",
    "internet_tld": ".ao",
    "utc_offset": "UTC+1",
    "drives_on": "right"
  },
  "geography": {
    "coordinates": {"lat": -11.2027, "lon": 17.8739},
    "bounding_box": {"north": -4.37, "south": -18.04, "east": 24.08, "west": 11.67},
    "land_area_km2": 1246700,
    "water_area_km2": 0,
    "coastline_km": 1600,
    "borders": ["DR Congo", "Republic of Congo", "Zambia", "Namibia"],
    "border_lengths_km": {"DR Congo": 2646, "Republic of Congo": 231, "Zambia": 1065, "Namibia": 1427},
    "highest_point": {"name": "Morro de Moco", "elevation_m": 2620},
    "lowest_point": {"name": "Atlantic Ocean", "elevation_m": 0},
    "terrain": "Narrow coastal plain; vast interior plateau (1000-2000m); tropical rainforest in north (Cabinda); semi-arid in south",
    "land_use": {"agricultural_pct": 45.7, "arable_pct": 3.9, "forest_pct": 46.3, "other_pct": 8},
    "major_rivers": ["Kwanza (Cuanza)", "Cunene", "Cubango/Okavango", "Zambezi (headwaters)", "Cassai"],
    "major_lakes": ["Dilolo"],
    "exclusive_economic_zone_km2": 518433,
    "landlocked": False,
    "notes": "Cabinda province is an exclave separated by DR Congo; Kwanza River is longest wholly within Angola; Okavango Delta fed by rivers from Angolan highlands."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$74 billion",
    "gdp_ppp_usd": "$217 billion",
    "gdp_per_capita_nominal_usd": 2040,
    "gdp_per_capita_ppp_usd": 5980,
    "gdp_growth_rate_pct": 0.8,
    "inflation_rate_pct": 13.5,
    "unemployment_rate_pct": 30.0,
    "youth_unemployment_rate_pct": 56.0,
    "poverty_rate_pct": 32.3,
    "poverty_line_definition": "National poverty line ($1.90/day)",
    "gini_coefficient": 51.3,
    "income_classification": "Lower-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 10, "industry_pct_gdp": 49, "services_pct_gdp": 41},
    "labor_force": 14000000,
    "labor_force_by_sector": {"agriculture_pct": 51, "industry_pct": 13, "services_pct": 36},
    "fdi_inflow_usd": "$-3.1 billion",
    "fdi_outflow_usd": "$0",
    "foreign_exchange_reserves_usd": "$14.5 billion",
    "ease_of_doing_business_rank": 177,
    "economic_freedom_index_score": 50.5,
    "credit_rating": {"moodys": "B3", "sp": "B-", "fitch": "B-"},
    "notes": "Oil-dependent (90%+ of exports); Sonangol national oil company; IMF programme 2018-21; kwanza devaluation; diversification efforts; Lobito Corridor rail project (US/EU funded)."
  },
  "health": {
    "health_expenditure_pct_gdp": 2.6,
    "health_expenditure_per_capita_usd": 53,
    "physicians_per_1k": 0.2,
    "nurses_midwives_per_1k": 0.4,
    "hospital_beds_per_1k": 0.8,
    "maternal_mortality_per_100k": 222,
    "hiv_prevalence_pct": 1.8,
    "malaria_incidence_per_1k": 190,
    "tuberculosis_incidence_per_100k": 325,
    "access_to_clean_water_pct": 57,
    "access_to_sanitation_pct": 52,
    "vaccination_coverage_pct": 55,
    "stunting_under5_pct": 38,
    "obesity_rate_pct": 8.2,
    "universal_health_coverage_index": 37,
    "leading_causes_of_death": ["Malaria", "Lower respiratory infections", "Neonatal disorders", "Diarrheal diseases", "HIV/AIDS"],
    "notes": "Severe healthcare worker shortage; urban-rural gap extreme; malaria #1 killer; yellow fever vaccination required; post-civil war healthcare infrastructure still recovering."
  },
  "food_agriculture": {
    "food_security_index_score": 34.5,
    "food_security_index_rank": 104,
    "arable_land_pct": 3.9,
    "agricultural_land_pct": 45.7,
    "irrigated_land_pct": 3,
    "major_crops": ["cassava", "maize", "bananas", "sweet potatoes", "sugarcane", "coffee", "palm oil"],
    "major_livestock": ["cattle", "goats", "pigs"],
    "food_import_dependency_pct": 50,
    "cereal_yield_kg_per_hectare": 800,
    "agricultural_employment_pct": 51,
    "prevalence_of_undernourishment_pct": 19,
    "notes": "Massive agricultural potential (pre-war was coffee exporter); landmines still obstruct farming; cassava staple food; Chinese and Brazilian agricultural partnerships."
  },
  "energy": {
    "energy_mix": {"fossil_fuels_pct": 45, "hydroelectric_pct": 54, "solar_pct": 0.5, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 0.5},
    "installed_capacity_mw": 6800,
    "electricity_production_gwh": 20000,
    "electricity_consumption_per_capita_kwh": 350,
    "energy_imports_pct": 0,
    "oil_production_bpd": 1100000,
    "oil_consumption_bpd": 130000,
    "natural_gas_production_bcm": 7.5,
    "energy_access_rural_pct": 8,
    "energy_access_urban_pct": 72,
    "notes": "Africa's 2nd-largest oil producer; OPEC member; Laúca hydropower dam (2070MW); Caculo Cabaça dam under construction (2172MW); massive rural electrification gap; LNG plant (Soyo)."
  },
  "transport": {
    "major_airports_international": ["Quatro de Fevereiro (Luanda)", "Catumbela (Benguela)"],
    "major_airports_domestic": ["Lubango", "Malanje", "Cabinda", "Huambo", "Soyo"],
    "national_airline": "TAAG Angola Airlines",
    "major_seaports": ["Luanda", "Lobito", "Namibe", "Cabinda", "Soyo"],
    "major_inland_ports": [],
    "merchant_marine_vessels": 40,
    "registered_vehicles_per_1k": 40,
    "road_fatalities_per_100k": 24,
    "notes": "New Luanda International Airport (NAIL/Dr António Agostinho Neto) opened; Lobito Corridor railway rehabilitation (Benguela Railway to DRC/Zambia); road infrastructure heavily damaged by civil war."
  },
  "tourism": {
    "annual_visitors": 218000,
    "tourism_revenue_usd": "$490 million",
    "tourism_pct_gdp": 0.7,
    "tourism_employment_pct": 3,
    "unesco_world_heritage_sites": 1,
    "unesco_sites_list": ["Mbanza-Kongo (2017)"],
    "major_attractions": ["Kalandula Falls", "Tundavala Gap", "Kissama National Park", "Luanda waterfront", "Namibe Desert"],
    "visa_free_access_countries": 49,
    "henley_passport_rank": 83,
    "notes": "Tourism largely undeveloped; high costs (Luanda among world's most expensive cities); visa-on-arrival introduced; ecotourism potential in national parks; civil war legacy constrains infrastructure."
  },
  "human_rights_gender": {
    "freedom_house_status": "Not Free",
    "freedom_house_score": 31,
    "gender_inequality_index": 0.536,
    "gender_inequality_rank": 132,
    "gender_gap_index_score": 0.638,
    "women_in_parliament_pct": 33,
    "women_labor_force_participation_pct": 75,
    "maternal_mortality_per_100k": 222,
    "child_marriage_pct": 30,
    "fgm_prevalence_pct": 0,
    "lgbtq_legal_status": "Legal (decriminalised 2021)",
    "death_penalty_status": "Abolitionist",
    "human_trafficking_tier": "Tier 2 Watch List",
    "child_labor_pct": 24,
    "notes": "MPLA single-party dominance; LGBTQ+ decriminalised in 2021 penal code; high child labour in agriculture; Isabel dos Santos corruption scandal; limited press freedom."
  },
  "security_stability": {
    "global_peace_index_score": 1.96,
    "global_peace_index_rank": 82,
    "terrorism_index_score": 0,
    "terrorism_index_rank": 0,
    "homicide_rate_per_100k": 4.8,
    "active_conflicts": ["Cabinda separatism (low-level, FLEC)"],
    "border_disputes": [],
    "un_peacekeeping_contributions": 50,
    "arms_imports_usd": "$30 million",
    "internally_displaced_persons": 0,
    "notes": "Post-civil war stability (2002 ceasefire); Cabinda FLEC separatism largely dormant; security forces credibly accused of extra-judicial killings in Lunda; landmines remain (~60,000+ still buried)."
  },
  "cultural_heritage": {
    "national_symbols": ["Palanca Negra (Giant sable antelope)"],
    "national_animal": "Giant sable antelope (Palanca Negra)",
    "national_flower": "Welwitschia mirabilis",
    "national_dish": "Muamba de galinha (chicken palm oil stew)",
    "national_sport": "Football, Basketball",
    "major_festivals": ["Independence Day (11 November)", "Carnival (Luanda)", "Armed Forces Day", "MPLA Foundation Day"],
    "cuisine_highlights": ["Muamba de galinha", "Calulu (fish stew)", "Funge (cassava paste)", "Mufete (grilled fish)"],
    "music_art_traditions": ["Semba", "Kuduro", "Kizomba (originated in Angola)", "Rebita"],
    "film_industry": "Emerging (Growing documentary scene)",
    "intangible_heritage_items": [],
    "notable_historical_figures": ["Queen Njinga Mbande", "Agostinho Neto", "Jonas Savimbi", "José Eduardo dos Santos"],
    "world_heritage_sites": ["Mbanza-Kongo"],
    "media_landscape": "State-controlled TV/radio (TPA, RNA); private newspapers; internet access growing; press freedom limited",
    "notes": "Kizomba dance/music originated in Luanda; Kuduro music global influence; strong oral tradition; Mbanza-Kongo capital of ancient Kongo Kingdom; carnival tradition."
  },
  "legal_system": {
    "legal_tradition": "Civil law (Portuguese-influenced)",
    "constitution_year": 2010,
    "sharia_applicability": "None",
    "customary_law_role": "Recognised for local matters in rural areas",
    "icc_membership": "Non-member",
    "judicial_independence_score": 0.25,
    "contract_enforcement_days": 1296,
    "property_rights_index": 30.0,
    "notes": "2010 constitution established presidential republic; Supreme Court; Constitutional Court; customary courts in rural areas; slow judicial reform."
  },
  "comparative_rankings": {
    "_note": "Country position relative to continent and global.",
    "population": {"continent_rank": 6, "global_rank": 42},
    "area": {"continent_rank": 7, "global_rank": 23},
    "gdp_nominal": {"continent_rank": 5, "global_rank": 61},
    "gdp_per_capita": {"continent_rank": 17, "global_rank": 131},
    "hdi": {"continent_rank": 33, "global_rank": 148},
    "life_expectancy": {"continent_rank": 33, "global_rank": 152},
    "ease_of_doing_business": {"continent_rank": 52, "global_rank": 177},
    "internet_penetration": {"continent_rank": 28, "global_rank": 135},
    "press_freedom": {"continent_rank": 39, "global_rank": 132},
    "global_peace_index": {"continent_rank": 13, "global_rank": 82},
    "innovation_index": {"continent_rank": 42, "global_rank": 137},
    "notes": "Africa's 2nd-largest oil producer; vast underutilised agricultural potential."
  },
  "_expand_demographics": {
    "population_growth_rate_pct": 3.2,
    "urban_population_growth_rate_pct": 4.4,
    "life_expectancy_male": 59.0,
    "life_expectancy_female": 65.0,
    "under5_mortality_per_1k": 69,
    "sex_ratio": 0.99,
    "dependency_ratio": 92.0,
    "population_density_per_km2": 29,
    "age_structure": {"0_14_pct": 47, "15_24_pct": 18, "25_54_pct": 29, "55_64_pct": 3, "65_plus_pct": 3}
  },
  "_expand_military": {"paramilitary_personnel": 10000, "conscription": True, "global_firepower_rank": 55},
  "_expand_trade": {
    "total_exports_usd": "$34 billion",
    "total_imports_usd": "$13 billion",
    "top_export_destinations": ["China (60%)", "India", "Spain", "USA", "France"],
    "top_import_origins": ["China", "Portugal", "Belgium", "USA", "Brazil"],
    "trade_as_pct_gdp": 63,
    "current_account_balance_usd": "$5 billion",
    "trade_agreements": ["SADC", "AfCFTA"],
    "special_economic_zones": ["Luanda-Bengo SEZ", "Viana Industrial Park"]
  },
  "_expand_infrastructure": {
    "broadband_subscriptions_per_100": 0.5,
    "4g_coverage_pct": 40,
    "5g_availability": False,
    "road_network_km": 76028,
    "waterways_km": 1300,
    "submarine_cables": ["SAT-3/WASC", "WACS", "SACS (South Atlantic Cable System, to Brazil)", "Monet"],
    "notes": "SACS cable connects Angola directly to Brazil; Lobito Corridor railway revitalisation; Luanda expressway; critical infrastructure still war-damaged."
  },
  "_expand_governance_indices": {
    "rule_of_law_index": {"score": 0.33, "rank": 119, "year": 2023},
    "government_effectiveness_index": {"score": -1.0, "percentile": 14, "year": 2023},
    "regulatory_quality_index": {"score": -0.85, "percentile": 16, "year": 2023},
    "political_stability_index": {"score": -0.2, "percentile": 39, "year": 2023}
  },
  "_expand_climate_environment": {
    "average_temperature_c": 21,
    "average_rainfall_mm": 1010,
    "co2_per_capita_t": 0.8,
    "deforestation_rate_pct": 0.6,
    "water_stress_level": "Low-Medium",
    "environmental_performance_index": {"score": 29.0, "rank": 152, "year": 2022},
    "paris_agreement_status": "Ratified (2020)",
    "biodiversity": {"known_species": 5100, "endemic_species": 200, "threatened_species": 78},
    "notes": "Giant sable antelope (national symbol, endemic, critically endangered); Okavango River source; mangrove forests along coast; charcoal deforestation."
  },
  "_expand_debt_aid": {
    "external_debt_usd": "$52 billion",
    "debt_service_pct_revenue": 45,
    "foreign_aid_given_usd": "$0",
    "top_donors": ["USA (PEPFAR)", "EU", "World Bank", "China"],
    "imf_programme_active": False,
    "world_bank_ida_eligible": True,
    "hipc_status": "N/A"
  },
  "_expand_education": {
    "education_expenditure_pct_gdp": 3.4,
    "primary_completion_rate_pct": 54,
    "gender_parity_index": 0.80,
    "mean_years_of_schooling": 5.1,
    "expected_years_of_schooling": 11.8,
    "pisa_scores": {"reading": 0, "math": 0, "science": 0, "year": 0},
    "student_teacher_ratio_primary": 45,
    "out_of_school_children": 2000000,
    "academic_freedom_index": 0.45
  },
  "_expand_diaspora_migration": {
    "diaspora_top_destinations": ["Portugal", "Brazil", "South Africa", "UK", "Namibia"],
    "asylum_seekers": 3000,
    "stateless_persons": 0,
    "internally_displaced_persons": 5000,
    "immigration_policy": "Moderate; work permits for Chinese/Portuguese workers",
    "remittances_pct_gdp": 0.1,
    "net_migration_rate_per_1k": 0.2
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.30,
    "ict_development_index": 2.3,
    "mobile_money_accounts": 3000000,
    "digital_payments_pct_adults": 15,
    "fintech_companies": 10,
    "startup_ecosystem_value_usd": "$50 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 27.0,
    "innovation_index_score": 13.0,
    "innovation_index_rank": 137,
    "ai_readiness_index": 20.0
  },
  "_expand_natural_resources": {
    "resource_curse_risk": "High (oil dependency >90% of exports; 'Futungo' elite capture)"
  }
},

"benin": {
  "_basics": {
    "capital_coordinates": {"lat": 6.4969, "lon": 2.6289},
    "other_major_cities": ["Cotonou (economic capital)", "Abomey-Calavi", "Parakou", "Djougou", "Bohicon"],
    "national_motto": "Fellowship, Justice, Labour",
    "national_anthem": "L'Aube Nouvelle (The New Dawn)",
    "currency_code": "XOF",
    "internet_tld": ".bj",
    "utc_offset": "UTC+1",
    "drives_on": "right"
  },
  "geography": {
    "coordinates": {"lat": 9.3077, "lon": 2.3158},
    "bounding_box": {"north": 12.42, "south": 6.22, "east": 3.84, "west": 0.77},
    "land_area_km2": 112622,
    "water_area_km2": 2000,
    "coastline_km": 121,
    "borders": ["Togo", "Burkina Faso", "Niger", "Nigeria"],
    "border_lengths_km": {"Togo": 651, "Burkina Faso": 386, "Niger": 277, "Nigeria": 809},
    "highest_point": {"name": "Mont Sokbaro", "elevation_m": 658},
    "lowest_point": {"name": "Atlantic Ocean", "elevation_m": 0},
    "terrain": "Flat coastal plain; marshy lagoons; forested plateau (centre); savanna (north); Atacora mountains (northwest)",
    "land_use": {"agricultural_pct": 31.3, "arable_pct": 22.9, "forest_pct": 40.2, "other_pct": 28.5},
    "major_rivers": ["Ouémé", "Niger (border)", "Mono (border)"],
    "major_lakes": ["Lake Nokoué", "Lake Ahémé"],
    "exclusive_economic_zone_km2": 31313,
    "landlocked": False,
    "notes": "Narrow strip of land between Togo and Nigeria; Ganvié (lake village) is 'Venice of Africa'; Pendjari National Park (W-Arly-Pendjari complex, UNESCO)."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$19 billion",
    "gdp_ppp_usd": "$49 billion",
    "gdp_per_capita_nominal_usd": 1412,
    "gdp_per_capita_ppp_usd": 3680,
    "gdp_growth_rate_pct": 6.0,
    "inflation_rate_pct": 3.0,
    "unemployment_rate_pct": 1.5,
    "youth_unemployment_rate_pct": 3.5,
    "poverty_rate_pct": 38.5,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 37.8,
    "income_classification": "Low income",
    "sector_breakdown": {"agriculture_pct_gdp": 25, "industry_pct_gdp": 23, "services_pct_gdp": 52},
    "labor_force": 5200000,
    "labor_force_by_sector": {"agriculture_pct": 38, "industry_pct": 14, "services_pct": 48},
    "fdi_inflow_usd": "$250 million",
    "fdi_outflow_usd": "$10 million",
    "foreign_exchange_reserves_usd": "$1.5 billion",
    "ease_of_doing_business_rank": 149,
    "economic_freedom_index_score": 56.0,
    "credit_rating": {"moodys": "B1", "sp": "B+", "fitch": "B+"},
    "notes": "Strong recent growth (6%+); cotton is #1 agricultural export; informal trade with Nigeria dominates; Cotonou Port transit hub; PAG (Programme d'Actions du Gouvernement) development plan; Eurobonds issued 2019/2021."
  },
  "health": {
    "health_expenditure_pct_gdp": 2.4,
    "health_expenditure_per_capita_usd": 34,
    "physicians_per_1k": 0.1,
    "nurses_midwives_per_1k": 0.5,
    "hospital_beds_per_1k": 0.5,
    "maternal_mortality_per_100k": 397,
    "hiv_prevalence_pct": 0.9,
    "malaria_incidence_per_1k": 180,
    "tuberculosis_incidence_per_100k": 56,
    "access_to_clean_water_pct": 65,
    "access_to_sanitation_pct": 19,
    "vaccination_coverage_pct": 68,
    "stunting_under5_pct": 32,
    "obesity_rate_pct": 9.6,
    "universal_health_coverage_index": 40,
    "leading_causes_of_death": ["Malaria", "Neonatal disorders", "Lower respiratory infections", "Diarrheal diseases"],
    "notes": "Severe doctor shortage; ARCH health insurance scheme expanding coverage; traditional medicine widely used; Vodun (voodoo) healing practices."
  },
  "food_agriculture": {
    "food_security_index_score": 40.0,
    "food_security_index_rank": 98,
    "arable_land_pct": 22.9,
    "agricultural_land_pct": 31.3,
    "irrigated_land_pct": 2,
    "major_crops": ["cotton", "maize", "cassava", "yams", "palm oil", "pineapple", "cashew nuts", "shea nuts"],
    "major_livestock": ["cattle", "goats", "sheep", "poultry"],
    "food_import_dependency_pct": 20,
    "cereal_yield_kg_per_hectare": 1300,
    "agricultural_employment_pct": 38,
    "prevalence_of_undernourishment_pct": 7.5,
    "notes": "Africa's largest cotton exporter by volume (some years); cashew production growing; informal food trade with Nigeria; pineapple for export; palm oil production."
  },
  "energy": {
    "energy_mix": {"fossil_fuels_pct": 50, "hydroelectric_pct": 5, "solar_pct": 3, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 42},
    "installed_capacity_mw": 500,
    "electricity_production_gwh": 600,
    "electricity_consumption_per_capita_kwh": 100,
    "energy_imports_pct": 85,
    "oil_production_bpd": 0,
    "oil_consumption_bpd": 48000,
    "natural_gas_production_bcm": 0,
    "energy_access_rural_pct": 10,
    "energy_access_urban_pct": 65,
    "notes": "Imports 85% of electricity from Nigeria/Ghana; Maria Gléta gas power plant; solar projects in north; biomass (wood/charcoal) dominant for cooking."
  },
  "transport": {
    "major_airports_international": ["Cadjehoun Airport (Cotonou)"],
    "major_airports_domestic": ["Parakou", "Natitingou", "Tourou (new Glo-Djigbé)"],
    "national_airline": "None currently (Benin Airlines proposed)",
    "major_seaports": ["Cotonou"],
    "major_inland_ports": [],
    "merchant_marine_vessels": 6,
    "registered_vehicles_per_1k": 20,
    "road_fatalities_per_100k": 28,
    "notes": "Cotonou Port handles transit cargo for Niger, Burkina Faso, Chad, Mali; zémidjan (motorcycle taxis) dominant urban transport; new Glo-Djigbé airport under construction."
  },
  "tourism": {
    "annual_visitors": 320000,
    "tourism_revenue_usd": "$200 million",
    "tourism_pct_gdp": 1.1,
    "tourism_employment_pct": 4,
    "unesco_world_heritage_sites": 2,
    "unesco_sites_list": ["Royal Palaces of Abomey", "Koutammakou (shared with Togo)"],
    "major_attractions": ["Royal Palaces of Abomey (Dahomey Kingdom)", "Ganvié (lake village)", "Ouidah (slave route)", "Pendjari National Park", "Route des Pêches"],
    "visa_free_access_countries": 50,
    "henley_passport_rank": 88,
    "notes": "Birthplace of Vodun (voodoo) — international Vodun festival in Ouidah (Jan 10); Abomey Amazons (Agojie) inspiration for film; Talon government investing heavily in tourism infrastructure."
  },
  "human_rights_gender": {
    "freedom_house_status": "Partly Free",
    "freedom_house_score": 54,
    "gender_inequality_index": 0.564,
    "gender_inequality_rank": 142,
    "gender_gap_index_score": 0.633,
    "women_in_parliament_pct": 7.2,
    "women_labor_force_participation_pct": 68,
    "maternal_mortality_per_100k": 397,
    "child_marriage_pct": 26,
    "fgm_prevalence_pct": 9,
    "lgbtq_legal_status": "Legal (no specific laws)",
    "death_penalty_status": "Abolitionist (2022 new penal code)",
    "human_trafficking_tier": "Tier 2",
    "child_labor_pct": 40,
    "notes": "Democratic governance tradition (multi-party since 1991); Talon era political restrictions (opposition candidates barred); vidomégon (child domestic servants) practice; FGM declining."
  },
  "security_stability": {
    "global_peace_index_score": 2.0,
    "global_peace_index_rank": 88,
    "terrorism_index_score": 3.0,
    "terrorism_index_rank": 48,
    "homicide_rate_per_100k": 3.0,
    "active_conflicts": ["Jihadist incursions in north (Alibori, Atacora — JNIM, ISGS spillover from Sahel)"],
    "border_disputes": [],
    "un_peacekeeping_contributions": 700,
    "arms_imports_usd": "$20 million",
    "internally_displaced_persons": 5000,
    "notes": "Northern terrorism threat growing (2022-24 attacks in Pendjari/W park area); historically stable democracy; no coups in democratic era; Operation Mirador counter-terrorism."
  },
  "cultural_heritage": {
    "national_symbols": ["Leopard"],
    "national_animal": "Leopard",
    "national_flower": "",
    "national_dish": "Amiwo (corn dough with tomato sauce)",
    "national_sport": "Football",
    "major_festivals": ["Vodun Day (January 10)", "Gani Festival (January, Nikki)", "Independence Day (August 1)", "Gelede masquerade"],
    "cuisine_highlights": ["Amiwo", "Akassa (fermented corn dough)", "Pâte with sauce (gombo, arachide)", "Piron (yam fufu)"],
    "music_art_traditions": ["Vodun ceremonies", "Gèlèdé masquerade (UNESCO)", "Tchink System music", "Afro-beat"], 
    "film_industry": "Small but growing (FESPACO participant)",
    "intangible_heritage_items": ["Gèlèdé oral heritage", "Ifá divination system (shared with Nigeria/Togo)"],
    "notable_historical_figures": ["King Ghezo (Dahomey)", "Béhanzin (Last king of Dahomey)", "Mathieu Kérékou", "Angélique Kidjo (Grammy winner)"],
    "world_heritage_sites": ["Royal Palaces of Abomey", "Koutammakou (shared with Togo)"],
    "media_landscape": "Diverse private media; ORTB state broadcaster; several private radio/TV stations; online media expanding",
    "notes": "Birthplace of Vodun religion; Kingdom of Dahomey historical legacy; Angélique Kidjo internationally renowned; restitution of royal treasures from France (2021, 26 objects)."
  },
  "legal_system": {
    "legal_tradition": "Civil law (French-influenced)",
    "constitution_year": 1990,
    "sharia_applicability": "None",
    "customary_law_role": "Recognised in family/land matters",
    "icc_membership": "Member",
    "judicial_independence_score": 0.40,
    "contract_enforcement_days": 750,
    "property_rights_index": 42.0,
    "notes": "1990 constitution model for Francophone Africa (Conférence Nationale); Constitutional Court active; 2019 reforms restricted political competition; ECOWAS Court of Justice in Porto-Novo."
  },
  "comparative_rankings": {
    "_note": "Country position relative to continent and global.",
    "population": {"continent_rank": 16, "global_rank": 77},
    "area": {"continent_rank": 31, "global_rank": 101},
    "gdp_nominal": {"continent_rank": 21, "global_rank": 107},
    "gdp_per_capita": {"continent_rank": 33, "global_rank": 157},
    "hdi": {"continent_rank": 36, "global_rank": 166},
    "life_expectancy": {"continent_rank": 27, "global_rank": 141},
    "ease_of_doing_business": {"continent_rank": 38, "global_rank": 149},
    "internet_penetration": {"continent_rank": 22, "global_rank": 120},
    "press_freedom": {"continent_rank": 15, "global_rank": 57},
    "global_peace_index": {"continent_rank": 14, "global_rank": 88},
    "innovation_index": {"continent_rank": 30, "global_rank": 121},
    "notes": "One of Africa's first democracies (1991 Conférence Nationale); cotton powerhouse; fast-growing economy."
  },
  "_expand_demographics": {
    "population_growth_rate_pct": 2.7,
    "urban_population_growth_rate_pct": 3.9,
    "life_expectancy_male": 60.0,
    "life_expectancy_female": 63.0,
    "under5_mortality_per_1k": 90,
    "sex_ratio": 1.01,
    "dependency_ratio": 82.0,
    "population_density_per_km2": 115,
    "age_structure": {"0_14_pct": 42, "15_24_pct": 20, "25_54_pct": 31, "55_64_pct": 4, "65_plus_pct": 3}
  },
  "_expand_military": {"paramilitary_personnel": 2500, "conscription": True, "global_firepower_rank": 120},
  "_expand_trade": {
    "total_exports_usd": "$3.7 billion",
    "total_imports_usd": "$4.2 billion",
    "top_export_destinations": ["Bangladesh (cotton)", "India", "Nigeria", "China", "Niger"],
    "top_import_origins": ["China", "India", "France", "Togo", "Thailand"],
    "trade_as_pct_gdp": 42,
    "current_account_balance_usd": "-$500 million",
    "trade_agreements": ["ECOWAS", "WAEMU", "AfCFTA"],
    "special_economic_zones": ["Glo-Djigbé Industrial Zone (GDIZ)"]
  },
  "_expand_infrastructure": {
    "broadband_subscriptions_per_100": 0.3,
    "4g_coverage_pct": 45,
    "5g_availability": False,
    "road_network_km": 16000,
    "waterways_km": 150,
    "submarine_cables": ["SAT-3/WASC", "ACE", "MainOne"],
    "notes": "Glo-Djigbé Industrial Zone (2022) textile/agro hub; Cotonou-Niamey railway planned; RNIE1 highway; zémidjan motorcycle taxis."
  },
  "_expand_governance_indices": {
    "rule_of_law_index": {"score": 0.45, "rank": 89, "year": 2023},
    "government_effectiveness_index": {"score": -0.30, "percentile": 35, "year": 2023},
    "regulatory_quality_index": {"score": -0.15, "percentile": 42, "year": 2023},
    "political_stability_index": {"score": -0.15, "percentile": 38, "year": 2023}
  },
  "_expand_climate_environment": {
    "average_temperature_c": 27,
    "average_rainfall_mm": 1100,
    "co2_per_capita_t": 0.6,
    "deforestation_rate_pct": 2.5,
    "water_stress_level": "Low-Medium",
    "environmental_performance_index": {"score": 28.6, "rank": 155, "year": 2022},
    "paris_agreement_status": "Ratified (2016)",
    "biodiversity": {"known_species": 3200, "endemic_species": 50, "threatened_species": 45},
    "notes": "W-Arly-Pendjari transboundary biosphere reserve; coastal erosion threatening Cotonou; Lama Forest remnant; rapid deforestation for firewood and farming."
  },
  "_expand_debt_aid": {
    "external_debt_usd": "$5 billion",
    "debt_service_pct_revenue": 15,
    "foreign_aid_given_usd": "$0",
    "top_donors": ["EU", "France", "World Bank", "China", "AfDB"],
    "imf_programme_active": False,
    "world_bank_ida_eligible": True,
    "hipc_status": "Completed (2003)"
  },
  "_expand_education": {
    "education_expenditure_pct_gdp": 3.0,
    "primary_completion_rate_pct": 70,
    "gender_parity_index": 0.87,
    "mean_years_of_schooling": 3.8,
    "expected_years_of_schooling": 12.6,
    "pisa_scores": {"reading": 0, "math": 0, "science": 0, "year": 0},
    "student_teacher_ratio_primary": 47,
    "out_of_school_children": 500000,
    "academic_freedom_index": 0.55
  },
  "_expand_diaspora_migration": {
    "diaspora_top_destinations": ["Nigeria", "Togo", "France", "Côte d'Ivoire", "Gabon"],
    "asylum_seekers": 500,
    "stateless_persons": 0,
    "internally_displaced_persons": 5000,
    "immigration_policy": "Open borders (ECOWAS free movement)",
    "remittances_pct_gdp": 3.0,
    "net_migration_rate_per_1k": 0.5
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.35,
    "ict_development_index": 2.0,
    "mobile_money_accounts": 4000000,
    "digital_payments_pct_adults": 20,
    "fintech_companies": 8,
    "startup_ecosystem_value_usd": "$20 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 30.0,
    "innovation_index_score": 18.0,
    "innovation_index_rank": 121,
    "ai_readiness_index": 22.0
  },
  "_expand_natural_resources": {
    "resource_curse_risk": "Low (not resource-dependent)"
  }
},

"botswana": {
  "_basics": {
    "capital_coordinates": {"lat": -24.6282, "lon": 25.9231},
    "other_major_cities": ["Francistown", "Maun", "Molepolole", "Serowe", "Selibe-Phikwe"],
    "national_motto": "Pula (Rain)",
    "national_anthem": "Fatshe leno la rona (This Land of Ours)",
    "currency_code": "BWP",
    "internet_tld": ".bw",
    "utc_offset": "UTC+2",
    "drives_on": "left"
  },
  "geography": {
    "coordinates": {"lat": -22.3285, "lon": 24.6849},
    "bounding_box": {"north": -17.78, "south": -26.91, "east": 29.37, "west": 19.99},
    "land_area_km2": 581730,
    "water_area_km2": 0,
    "coastline_km": 0,
    "borders": ["South Africa", "Namibia", "Zambia", "Zimbabwe"],
    "border_lengths_km": {"South Africa": 1969, "Namibia": 1544, "Zambia": 0.15, "Zimbabwe": 834},
    "highest_point": {"name": "Tsodilo Hills", "elevation_m": 1489},
    "lowest_point": {"name": "Confluence of Limpopo and Shashe Rivers", "elevation_m": 513},
    "terrain": "Predominantly flat; Kalahari Desert (70%); Okavango Delta (northwest); Makgadikgadi salt pans",
    "land_use": {"agricultural_pct": 45.8, "arable_pct": 0.6, "forest_pct": 19.8, "other_pct": 34.4},
    "major_rivers": ["Okavango", "Limpopo", "Chobe", "Shashe"],
    "major_lakes": ["Makgadikgadi Pans", "Lake Ngami"],
    "exclusive_economic_zone_km2": 0,
    "landlocked": True,
    "notes": "Okavango Delta (world's largest inland delta, UNESCO World Heritage); Kalahari semi-desert; Makgadikgadi Pans largest salt flats in world; four-country meeting point (with Zambia, Namibia, Zimbabwe) at Kazungula."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$19.4 billion",
    "gdp_ppp_usd": "$46 billion",
    "gdp_per_capita_nominal_usd": 7300,
    "gdp_per_capita_ppp_usd": 17300,
    "gdp_growth_rate_pct": 3.8,
    "inflation_rate_pct": 4.1,
    "unemployment_rate_pct": 25.0,
    "youth_unemployment_rate_pct": 38.0,
    "poverty_rate_pct": 16.3,
    "poverty_line_definition": "National poverty line",
    "gini_coefficient": 53.3,
    "income_classification": "Upper-middle income",
    "sector_breakdown": {"agriculture_pct_gdp": 2, "industry_pct_gdp": 28, "services_pct_gdp": 70},
    "labor_force": 1050000,
    "labor_force_by_sector": {"agriculture_pct": 16, "industry_pct": 18, "services_pct": 66},
    "fdi_inflow_usd": "$400 million",
    "fdi_outflow_usd": "$50 million",
    "foreign_exchange_reserves_usd": "$4.7 billion",
    "ease_of_doing_business_rank": 87,
    "economic_freedom_index_score": 69.6,
    "credit_rating": {"moodys": "A3", "sp": "BBB+", "fitch": ""},
    "notes": "Africa's development success story (poorest at independence 1966, now upper-middle income); diamond-driven growth (Debswana); transparent governance; Sovereign Wealth Fund (Pula Fund); diversification challenge; high inequality."
  },
  "health": {
    "health_expenditure_pct_gdp": 5.8,
    "health_expenditure_per_capita_usd": 421,
    "physicians_per_1k": 0.5,
    "nurses_midwives_per_1k": 2.9,
    "hospital_beds_per_1k": 1.8,
    "maternal_mortality_per_100k": 186,
    "hiv_prevalence_pct": 20.7,
    "malaria_incidence_per_1k": 5,
    "tuberculosis_incidence_per_100k": 275,
    "access_to_clean_water_pct": 92,
    "access_to_sanitation_pct": 63,
    "vaccination_coverage_pct": 89,
    "stunting_under5_pct": 24,
    "obesity_rate_pct": 18.9,
    "universal_health_coverage_index": 55,
    "leading_causes_of_death": ["HIV/AIDS", "Cardiovascular diseases", "Tuberculosis", "Diabetes", "Cancer"],
    "notes": "One of the world's highest HIV prevalence rates; pioneering ARV treatment programme (Masa programme, 2002); life expectancy recovered from 43 (2002) to 69; National Health Insurance planned."
  },
  "food_agriculture": {
    "food_security_index_score": 55.0,
    "food_security_index_rank": 72,
    "arable_land_pct": 0.6,
    "agricultural_land_pct": 45.8,
    "irrigated_land_pct": 1,
    "major_crops": ["sorghum", "maize", "millet", "beans", "cowpeas", "sunflower"],
    "major_livestock": ["cattle (Tswana cattle)", "goats", "sheep"],
    "food_import_dependency_pct": 80,
    "cereal_yield_kg_per_hectare": 350,
    "agricultural_employment_pct": 16,
    "prevalence_of_undernourishment_pct": 15,
    "notes": "Cattle culturally and economically important; Beef Protocol (EU export quotas); Botswana Meat Commission; Kalahari limits agriculture; food imports mainly from South Africa."
  },
  "energy": {
    "energy_mix": {"fossil_fuels_pct": 85, "hydroelectric_pct": 0, "solar_pct": 10, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 5},
    "installed_capacity_mw": 892,
    "electricity_production_gwh": 3000,
    "electricity_consumption_per_capita_kwh": 1600,
    "energy_imports_pct": 15,
    "oil_production_bpd": 0,
    "oil_consumption_bpd": 20000,
    "natural_gas_production_bcm": 0,
    "energy_access_rural_pct": 32,
    "energy_access_urban_pct": 77,
    "notes": "Morupule A&B coal power stations; massive coal reserves (200+ billion tonnes); solar potential enormous (300+ sunny days/year); imports from Eskom (South Africa); 100MW solar farm at Lerala."
  },
  "transport": {
    "major_airports_international": ["Sir Seretse Khama (Gaborone)", "Maun Airport", "Kasane Airport"],
    "major_airports_domestic": ["Francistown", "Nata", "Shakawe"],
    "national_airline": "Air Botswana",
    "major_seaports": [],
    "major_inland_ports": [],
    "merchant_marine_vessels": 0,
    "registered_vehicles_per_1k": 100,
    "road_fatalities_per_100k": 24,
    "notes": "Trans-Kalahari Highway (connects to Namibia/Walvis Bay); Kazungula Bridge (2021, connecting to Zambia); landlocked—relies on road transport through South Africa for trade."
  },
  "tourism": {
    "annual_visitors": 1700000,
    "tourism_revenue_usd": "$600 million",
    "tourism_pct_gdp": 3.3,
    "tourism_employment_pct": 5,
    "unesco_world_heritage_sites": 2,
    "unesco_sites_list": ["Tsodilo Hills", "Okavango Delta"],
    "major_attractions": ["Okavango Delta", "Chobe National Park", "Makgadikgadi Pans", "Central Kalahari Game Reserve", "Moremi Game Reserve", "Tsodilo Hills"],
    "visa_free_access_countries": 85,
    "henley_passport_rank": 60,
    "notes": "High-value, low-volume tourism policy; Okavango Delta one of Africa's premier safari destinations; Chobe (largest elephant population in world); luxury wildlife lodges; Botswana Ecotourism Certification."
  },
  "human_rights_gender": {
    "freedom_house_status": "Free",
    "freedom_house_score": 72,
    "gender_inequality_index": 0.428,
    "gender_inequality_rank": 100,
    "gender_gap_index_score": 0.715,
    "women_in_parliament_pct": 11,
    "women_labor_force_participation_pct": 59,
    "maternal_mortality_per_100k": 186,
    "child_marriage_pct": 8,
    "fgm_prevalence_pct": 0,
    "lgbtq_legal_status": "Legal (decriminalised by High Court 2019)",
    "death_penalty_status": "Retentionist (executions carried out)",
    "human_trafficking_tier": "Tier 2",
    "child_labor_pct": 9,
    "notes": "One of Africa's most stable democracies; LGBT decriminalisation (2019 High Court ruling landmark); death penalty still applied (rare); San/Bushman land rights contentious."
  },
  "security_stability": {
    "global_peace_index_score": 1.65,
    "global_peace_index_rank": 42,
    "terrorism_index_score": 0,
    "terrorism_index_rank": 0,
    "homicide_rate_per_100k": 6.7,
    "active_conflicts": [],
    "border_disputes": [],
    "un_peacekeeping_contributions": 50,
    "arms_imports_usd": "$20 million",
    "internally_displaced_persons": 0,
    "notes": "One of Africa's most peaceful and stable nations; Botswana Defence Force professional and apolitical; no history of civil conflict or coups; anti-poaching operations."
  },
  "cultural_heritage": {
    "national_symbols": ["Zebra"],
    "national_animal": "Zebra",
    "national_flower": "",
    "national_dish": "Seswaa (pounded meat)",
    "national_sport": "Football",
    "major_festivals": ["Botswana Day (September 30)", "President's Day", "Dithubaruba Cultural Festival", "Maun Festival"],
    "cuisine_highlights": ["Seswaa", "Bogobe (sorghum porridge)", "Phane (mopane worms)", "Vetkoek"],
    "music_art_traditions": ["Traditional Tswana music", "San Bushman rock art (Tsodilo)", "Setswana poetry/oral traditions"],
    "film_industry": "Small (The No. 1 Ladies' Detective Agency filmed here)",
    "intangible_heritage_items": ["Earthenware pottery tradition", "Dikgafela harvest festival"],
    "notable_historical_figures": ["Seretse Khama (first president)", "Khama III", "Ruth Williams Khama", "Festus Mogae"],
    "world_heritage_sites": ["Tsodilo Hills", "Okavango Delta"],
    "media_landscape": "Relatively free press; Daily News (state), Mmegi, The Voice (private); BTV; private FM stations",
    "notes": "Setswana culture dominant; San/Bushman indigenous heritage; No. 1 Ladies' Detective Agency novels (Alexander McCall Smith) set in Gaborone; Botswana one of world's diamond polishing centres."
  },
  "legal_system": {
    "legal_tradition": "Common law (English-influenced) with customary law",
    "constitution_year": 1966,
    "sharia_applicability": "None",
    "customary_law_role": "Significant (Kgotla customary courts widespread)",
    "icc_membership": "Member",
    "judicial_independence_score": 0.60,
    "contract_enforcement_days": 625,
    "property_rights_index": 60.0,
    "notes": "Dual court system (civil/customary); Kgotla (traditional assembly) still resolves local disputes; High Court/Court of Appeal; SADC Tribunal previously in Gaborone; strong rule of law for Africa."
  },
  "comparative_rankings": {
    "_note": "Country position relative to continent and global.",
    "population": {"continent_rank": 43, "global_rank": 145},
    "area": {"continent_rank": 11, "global_rank": 48},
    "gdp_nominal": {"continent_rank": 16, "global_rank": 108},
    "gdp_per_capita": {"continent_rank": 5, "global_rank": 80},
    "hdi": {"continent_rank": 9, "global_rank": 113},
    "life_expectancy": {"continent_rank": 17, "global_rank": 118},
    "ease_of_doing_business": {"continent_rank": 5, "global_rank": 87},
    "internet_penetration": {"continent_rank": 9, "global_rank": 75},
    "press_freedom": {"continent_rank": 6, "global_rank": 38},
    "global_peace_index": {"continent_rank": 2, "global_rank": 42},
    "innovation_index": {"continent_rank": 6, "global_rank": 85},
    "notes": "Africa's governance and development success story; diamond wealth; strong institutions; high per-capita GDP."
  },
  "_expand_demographics": {
    "population_growth_rate_pct": 1.5,
    "urban_population_growth_rate_pct": 2.5,
    "life_expectancy_male": 65.0,
    "life_expectancy_female": 73.0,
    "under5_mortality_per_1k": 33,
    "sex_ratio": 0.95,
    "dependency_ratio": 58.0,
    "population_density_per_km2": 4.1,
    "age_structure": {"0_14_pct": 31, "15_24_pct": 18, "25_54_pct": 40, "55_64_pct": 6, "65_plus_pct": 5}
  },
  "_expand_military": {"paramilitary_personnel": 1500, "conscription": False, "global_firepower_rank": 108},
  "_expand_trade": {
    "total_exports_usd": "$7.5 billion",
    "total_imports_usd": "$6.5 billion",
    "top_export_destinations": ["Belgium (diamonds)", "India", "UAE", "South Africa", "Israel"],
    "top_import_origins": ["South Africa (65%+)", "Namibia", "Canada"],
    "trade_as_pct_gdp": 72,
    "current_account_balance_usd": "$500 million",
    "trade_agreements": ["SACU", "SADC", "AGOA (US)", "AfCFTA"], 
    "special_economic_zones": ["Gaborone SEZ (SPEDU)", "Selebi-Phikwe"]
  },
  "_expand_infrastructure": {
    "broadband_subscriptions_per_100": 2.0,
    "4g_coverage_pct": 65,
    "5g_availability": False,
    "road_network_km": 31747,
    "waterways_km": 0,
    "submarine_cables": [],
    "notes": "Landlocked — fibre via South Africa and Namibia; Trans-Kalahari Highway; Kazungula Bridge (2021); BotswanaFibre Networks; Masama/BOFINET backbone."
  },
  "_expand_governance_indices": {
    "rule_of_law_index": {"score": 0.60, "rank": 46, "year": 2023},
    "government_effectiveness_index": {"score": 0.35, "percentile": 63, "year": 2023},
    "regulatory_quality_index": {"score": 0.50, "percentile": 66, "year": 2023},
    "political_stability_index": {"score": 0.92, "percentile": 79, "year": 2023}
  },
  "_expand_climate_environment": {
    "average_temperature_c": 21,
    "average_rainfall_mm": 416,
    "co2_per_capita_t": 2.8,
    "deforestation_rate_pct": 0.3,
    "water_stress_level": "High",
    "environmental_performance_index": {"score": 37.0, "rank": 123, "year": 2022},
    "paris_agreement_status": "Ratified (2016)",
    "biodiversity": {"known_species": 4500, "endemic_species": 100, "threatened_species": 35},
    "notes": "Okavango Delta threatened by water extraction upstream (Namibia/Angola); Kalahari desertification; large elephant population management challenge; world's richest diamond biodiversity."
  },
  "_expand_debt_aid": {
    "external_debt_usd": "$3 billion",
    "debt_service_pct_revenue": 5,
    "foreign_aid_given_usd": "$0",
    "top_donors": ["USA (PEPFAR)", "EU", "Germany", "Japan"],
    "imf_programme_active": False,
    "world_bank_ida_eligible": False,
    "hipc_status": "N/A"
  },
  "_expand_education": {
    "education_expenditure_pct_gdp": 8.7,
    "primary_completion_rate_pct": 96,
    "gender_parity_index": 1.03,
    "mean_years_of_schooling": 9.8,
    "expected_years_of_schooling": 12.8,
    "pisa_scores": {"reading": 0, "math": 0, "science": 0, "year": 0},
    "student_teacher_ratio_primary": 24,
    "out_of_school_children": 15000,
    "academic_freedom_index": 0.70
  },
  "_expand_diaspora_migration": {
    "diaspora_top_destinations": ["South Africa", "UK", "USA", "Namibia", "Australia"],
    "asylum_seekers": 200,
    "stateless_persons": 0,
    "internally_displaced_persons": 0,
    "immigration_policy": "Selective; work permits for skilled labour",
    "remittances_pct_gdp": 0.3,
    "net_migration_rate_per_1k": 2.3
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.50,
    "ict_development_index": 4.3,
    "mobile_money_accounts": 500000,
    "digital_payments_pct_adults": 35,
    "fintech_companies": 5,
    "startup_ecosystem_value_usd": "$30 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 45.0,
    "innovation_index_score": 30.0,
    "innovation_index_rank": 85,
    "ai_readiness_index": 35.0
  },
  "_expand_natural_resources": {
    "resource_curse_risk": "Low (transparent diamond revenue management, Pula Fund)"
  }
},

"burkina-faso": {
  "_basics": {
    "capital_coordinates": {"lat": 12.3714, "lon": -1.5197},
    "other_major_cities": ["Bobo-Dioulasso", "Koudougou", "Ouahigouya", "Banfora", "Kaya"],
    "national_motto": "Unity, Progress, Justice",
    "national_anthem": "Une Seule Nuit (A Single Night — renamed: Ditanyè/Victory Song)",
    "currency_code": "XOF",
    "internet_tld": ".bf",
    "utc_offset": "UTC+0",
    "drives_on": "right"
  },
  "geography": {
    "coordinates": {"lat": 12.2383, "lon": -1.5616},
    "bounding_box": {"north": 15.08, "south": 9.39, "east": 2.40, "west": -5.52},
    "land_area_km2": 274200,
    "water_area_km2": 400,
    "coastline_km": 0,
    "borders": ["Mali", "Niger", "Benin", "Togo", "Ghana", "Côte d'Ivoire"],
    "border_lengths_km": {"Mali": 1325, "Niger": 622, "Benin": 386, "Togo": 131, "Ghana": 602, "Côte d'Ivoire": 545},
    "highest_point": {"name": "Ténakourou", "elevation_m": 749},
    "lowest_point": {"name": "Mouhoun (Black Volta) River", "elevation_m": 200},
    "terrain": "Gently undulating peneplain; flat savanna; semi-arid north; sandstone escarpment (Banfora Cliffs)",
    "land_use": {"agricultural_pct": 43.7, "arable_pct": 22.0, "forest_pct": 19.3, "other_pct": 37.0},
    "major_rivers": ["Mouhoun (Black Volta)", "Nakambé (White Volta)", "Nazinon (Red Volta)", "Comoé"],
    "major_lakes": ["Kompienga Reservoir", "Bagré Reservoir"],
    "exclusive_economic_zone_km2": 0,
    "landlocked": True,
    "notes": "Landlocked in West Africa; Volta River system headwaters; 'Land of the Upright People' (Thomas Sankara's naming); Sahel transition zone; climate change hotspot."
  },
  "economy_extended": {
    "gdp_nominal_usd": "$19 billion",
    "gdp_ppp_usd": "$52 billion",
    "gdp_per_capita_nominal_usd": 830,
    "gdp_per_capita_ppp_usd": 2280,
    "gdp_growth_rate_pct": 4.5,
    "inflation_rate_pct": 5.5,
    "unemployment_rate_pct": 5.0,
    "youth_unemployment_rate_pct": 8.6,
    "poverty_rate_pct": 41.4,
    "poverty_line_definition": "National poverty line ($2.15/day)",
    "gini_coefficient": 35.3,
    "income_classification": "Low income",
    "sector_breakdown": {"agriculture_pct_gdp": 25, "industry_pct_gdp": 22, "services_pct_gdp": 53},
    "labor_force": 8500000,
    "labor_force_by_sector": {"agriculture_pct": 80, "industry_pct": 5, "services_pct": 15},
    "fdi_inflow_usd": "$150 million",
    "fdi_outflow_usd": "$0",
    "foreign_exchange_reserves_usd": "$500 million",
    "ease_of_doing_business_rank": 151,
    "economic_freedom_index_score": 55.5,
    "credit_rating": {"moodys": "", "sp": "CCC+", "fitch": "CCC+"},
    "notes": "Cotton and gold main exports; rapidly growing gold mining sector (4th in Africa); post-coup economic uncertainty; sanctions; CFA franc zone; 80% rural subsistence farming."
  },
  "health": {
    "health_expenditure_pct_gdp": 5.4,
    "health_expenditure_per_capita_usd": 42,
    "physicians_per_1k": 0.1,
    "nurses_midwives_per_1k": 0.6,
    "hospital_beds_per_1k": 0.4,
    "maternal_mortality_per_100k": 320,
    "hiv_prevalence_pct": 0.7,
    "malaria_incidence_per_1k": 380,
    "tuberculosis_incidence_per_100k": 48,
    "access_to_clean_water_pct": 54,
    "access_to_sanitation_pct": 22,
    "vaccination_coverage_pct": 88,
    "stunting_under5_pct": 25,
    "obesity_rate_pct": 5.6,
    "universal_health_coverage_index": 38,
    "leading_causes_of_death": ["Malaria", "Neonatal disorders", "Lower respiratory infections", "Diarrheal diseases", "Meningitis"],
    "notes": "Meningitis belt (seasonal epidemics); severe health worker shortage; WHO prequalified malaria vaccine rollout; traditional medicine deeply rooted; free healthcare for under-5s and pregnant women."
  },
  "food_agriculture": {
    "food_security_index_score": 36.0,
    "food_security_index_rank": 99,
    "arable_land_pct": 22.0,
    "agricultural_land_pct": 43.7,
    "irrigated_land_pct": 1.5,
    "major_crops": ["cotton", "sorghum", "millet", "maize", "rice", "cowpeas", "sesame", "shea nuts", "groundnuts"],
    "major_livestock": ["cattle", "goats", "sheep", "donkeys", "poultry"],
    "food_import_dependency_pct": 15,
    "cereal_yield_kg_per_hectare": 1000,
    "agricultural_employment_pct": 80,
    "prevalence_of_undernourishment_pct": 15.5,
    "notes": "Shea nut processing (women's cooperatives) for cosmetics export; cotton 'white gold'; Bagré growth pole (irrigated agriculture); food insecurity worsening due to jihadist displacement."
  },
  "energy": {
    "energy_mix": {"fossil_fuels_pct": 55, "hydroelectric_pct": 8, "solar_pct": 10, "wind_pct": 0, "nuclear_pct": 0, "biomass_other_pct": 27},
    "installed_capacity_mw": 550,
    "electricity_production_gwh": 1700,
    "electricity_consumption_per_capita_kwh": 60,
    "energy_imports_pct": 40,
    "oil_production_bpd": 0,
    "oil_consumption_bpd": 30000,
    "natural_gas_production_bcm": 0,
    "energy_access_rural_pct": 5,
    "energy_access_urban_pct": 70,
    "notes": "Imports electricity from Côte d'Ivoire and Ghana; Zagtouli solar plant (33MW, largest in West Africa at commissioning); Samendéni dam; biomass/charcoal dominant for cooking; severe rural energy poverty."
  },
  "transport": {
    "major_airports_international": ["Thomas Sankara International Airport (Ouagadougou)"],
    "major_airports_domestic": ["Bobo-Dioulasso Airport"],
    "national_airline": "Air Burkina",
    "major_seaports": [],
    "major_inland_ports": [],
    "merchant_marine_vessels": 0,
    "registered_vehicles_per_1k": 10,
    "road_fatalities_per_100k": 30,
    "notes": "Landlocked — relies on Abidjan (Côte d'Ivoire) and Lomé (Togo) ports; Sitarail railway to Abidjan; extensive unpaved road network; motorcycle dominant rural transport."
  },
  "tourism": {
    "annual_visitors": 200000,
    "tourism_revenue_usd": "$70 million",
    "tourism_pct_gdp": 0.4,
    "tourism_employment_pct": 2,
    "unesco_world_heritage_sites": 3,
    "unesco_sites_list": ["Ruins of Loropéni", "Ancient Ferrous Metallurgy Sites", "W-Arly-Pendjari Complex (shared)"],
    "major_attractions": ["Ruins of Loropéni", "Sindou Peaks", "Banfora Cascades", "FESPACO Film Festival", "Nazinga Ranch"],
    "visa_free_access_countries": 52,
    "henley_passport_rank": 87,
    "notes": "FESPACO (Pan-African Film Festival, biennial, Ouagadougou) — Africa's largest film festival; tourism devastated by security crisis; cultural tourism previously strong; artisan crafts (bronze, textiles)."
  },
  "human_rights_gender": {
    "freedom_house_status": "Not Free",
    "freedom_house_score": 30,
    "gender_inequality_index": 0.594,
    "gender_inequality_rank": 147,
    "gender_gap_index_score": 0.612,
    "women_in_parliament_pct": 7,
    "women_labor_force_participation_pct": 60,
    "maternal_mortality_per_100k": 320,
    "child_marriage_pct": 52,
    "fgm_prevalence_pct": 76,
    "lgbtq_legal_status": "Legal (but socially taboo)",
    "death_penalty_status": "Abolitionist (2018)",
    "human_trafficking_tier": "Tier 2 Watch List",
    "child_labor_pct": 39,
    "notes": "Military junta since 2022 (Capt. Traoré); FGM prevalence high despite laws; child marriage widespread; Sankara-era women's rights legacy eroding; press restrictions post-coup."
  },
  "security_stability": {
    "global_peace_index_score": 2.82,
    "global_peace_index_rank": 147,
    "terrorism_index_score": 8.3,
    "terrorism_index_rank": 5,
    "homicide_rate_per_100k": 1.3,
    "active_conflicts": ["Jihadist insurgency (JNIM, ISGS — controls ~40% of territory)", "Ethnic militia violence"],
    "border_disputes": [],
    "un_peacekeeping_contributions": 0,
    "arms_imports_usd": "$50 million",
    "internally_displaced_persons": 2000000,
    "notes": "One of world's fastest-growing crises; JNIM/ISGS control swathes of north/east; 2M+ displaced; French military expelled (2022); Russian Wagner/Africa Corps presence; VDP (Volunteers for Defence of the Fatherland) auxiliary militia; AES alliance with Mali/Niger."
  },
  "cultural_heritage": {
    "national_symbols": ["White Stallion"],
    "national_animal": "White Stallion",
    "national_flower": "",
    "national_dish": "Tô (millet/sorghum paste with sauce)",
    "national_sport": "Football, Cycling",
    "major_festivals": ["FESPACO (Pan-African Film Festival, Ouagadougou)", "SIAO (International Arts and Crafts Fair)", "Moro-Naba ceremony (Mossi court)", "FITD (Theatre Fest)"],
    "cuisine_highlights": ["Tô", "Riz gras (jollof-style)", "Babenda (leaf sauce)", "Poulet bicyclette (free-range grilled chicken)", "Zoom-koom (millet drink)"],
    "music_art_traditions": ["Djembe drumming", "Balafon music", "Mossi mask traditions", "FESPACO cinema culture"],
    "film_industry": "Major (FESPACO host — Ouagadougou is 'Hollywood of Africa')",
    "intangible_heritage_items": ["Balafon cultural practices", "Coat of arms ceremony of the Moogho Naaba"],
    "notable_historical_figures": ["Thomas Sankara ('Africa's Che Guevara')", "Naaba Kango (Mossi emperor)", "Blaise Compaoré"],
    "world_heritage_sites": ["Ruins of Loropéni", "Ancient Ferrous Metallurgy Sites", "W-Arly-Pendjari Complex"],
    "media_landscape": "RTB state broadcaster; private radio active (Radio Omega, Savane FM); press freedom restricted post-coup; community radio vital in rural areas",
    "notes": "Thomas Sankara (1983-87) revolutionary leader (Pan-Africanist icon); FESPACO world-renowned; Mossi Kingdom (Moro-Naba) cultural continuity; artisan traditions (bronze casting, weaving)."
  },
  "legal_system": {
    "legal_tradition": "Civil law (French-influenced)",
    "constitution_year": 2024,
    "sharia_applicability": "None (some informal Islamic dispute resolution in north)",
    "customary_law_role": "Significant in rural areas (land, family disputes)",
    "icc_membership": "Member (under review post-coup)",
    "judicial_independence_score": 0.30,
    "contract_enforcement_days": 446,
    "property_rights_index": 35.0,
    "notes": "Constitution suspended after 2022 coup; transition charter in place; ASCE-LC (anti-corruption authority); Transitional Legislative Assembly; justice system strained by conflict."
  },
  "comparative_rankings": {
    "_note": "Country position relative to continent and global.",
    "population": {"continent_rank": 13, "global_rank": 58},
    "area": {"continent_rank": 18, "global_rank": 74},
    "gdp_nominal": {"continent_rank": 20, "global_rank": 106},
    "gdp_per_capita": {"continent_rank": 43, "global_rank": 178},
    "hdi": {"continent_rank": 47, "global_rank": 184},
    "life_expectancy": {"continent_rank": 28, "global_rank": 143},
    "ease_of_doing_business": {"continent_rank": 40, "global_rank": 151},
    "internet_penetration": {"continent_rank": 31, "global_rank": 145},
    "press_freedom": {"continent_rank": 28, "global_rank": 86},
    "global_peace_index": {"continent_rank": 47, "global_rank": 147},
    "innovation_index": {"continent_rank": 38, "global_rank": 130},
    "notes": "FESPACO host; Sahel security crisis epicentre; major gold producer; Thomas Sankara legacy."
  },
  "_expand_demographics": {
    "population_growth_rate_pct": 2.5,
    "urban_population_growth_rate_pct": 4.3,
    "life_expectancy_male": 60.0,
    "life_expectancy_female": 63.0,
    "under5_mortality_per_1k": 84,
    "sex_ratio": 0.99,
    "dependency_ratio": 88.0,
    "population_density_per_km2": 79,
    "age_structure": {"0_14_pct": 44, "15_24_pct": 20, "25_54_pct": 30, "55_64_pct": 3, "65_plus_pct": 3}
  },
  "_expand_military": {"paramilitary_personnel": 45000, "conscription": True, "global_firepower_rank": 100},
  "_expand_trade": {
    "total_exports_usd": "$4.5 billion",
    "total_imports_usd": "$4.5 billion",
    "top_export_destinations": ["Switzerland (gold)", "India", "Singapore", "Côte d'Ivoire", "Ghana"],
    "top_import_origins": ["Côte d'Ivoire", "China", "France", "Ghana", "Togo"],
    "trade_as_pct_gdp": 47,
    "current_account_balance_usd": "-$500 million",
    "trade_agreements": ["ECOWAS (suspended)", "WAEMU", "AES", "AfCFTA"],
    "special_economic_zones": []
  },
  "_expand_infrastructure": {
    "broadband_subscriptions_per_100": 0.2,
    "4g_coverage_pct": 30,
    "5g_availability": False,
    "road_network_km": 15272,
    "waterways_km": 0,
    "submarine_cables": [],
    "notes": "Landlocked — fibre via Côte d'Ivoire; Ouaga-Pouga road; Sitarail railway (to Abidjan); Thomas Sankara airport renamed 2022; poor rural road network."
  },
  "_expand_governance_indices": {
    "rule_of_law_index": {"score": 0.38, "rank": 109, "year": 2023},
    "government_effectiveness_index": {"score": -0.55, "percentile": 27, "year": 2023},
    "regulatory_quality_index": {"score": -0.30, "percentile": 36, "year": 2023},
    "political_stability_index": {"score": -1.80, "percentile": 4, "year": 2023}
  },
  "_expand_climate_environment": {
    "average_temperature_c": 28,
    "average_rainfall_mm": 750,
    "co2_per_capita_t": 0.2,
    "deforestation_rate_pct": 2.8,
    "water_stress_level": "High",
    "environmental_performance_index": {"score": 27.0, "rank": 160, "year": 2022},
    "paris_agreement_status": "Ratified (2016)",
    "biodiversity": {"known_species": 3500, "endemic_species": 30, "threatened_species": 30},
    "notes": "Sahel desertification advancing; Great Green Wall planting; Arly-Singou-Pama wildlife reserves threatened by conflict; gold mining mercury contamination; wood/charcoal deforestation."
  },
  "_expand_debt_aid": {
    "external_debt_usd": "$5 billion",
    "debt_service_pct_revenue": 18,
    "foreign_aid_given_usd": "$0",
    "top_donors": ["EU", "France", "World Bank", "AfDB", "US"],
    "imf_programme_active": False,
    "world_bank_ida_eligible": True,
    "hipc_status": "Completed (2002)"
  },
  "_expand_education": {
    "education_expenditure_pct_gdp": 5.5,
    "primary_completion_rate_pct": 57,
    "gender_parity_index": 0.92,
    "mean_years_of_schooling": 2.1,
    "expected_years_of_schooling": 9.3,
    "pisa_scores": {"reading": 0, "math": 0, "science": 0, "year": 0},
    "student_teacher_ratio_primary": 42,
    "out_of_school_children": 2000000,
    "academic_freedom_index": 0.35
  },
  "_expand_diaspora_migration": {
    "diaspora_top_destinations": ["Côte d'Ivoire (3M+)", "Mali", "Ghana", "Italy", "France"],
    "asylum_seekers": 30000,
    "stateless_persons": 0,
    "internally_displaced_persons": 2000000,
    "immigration_policy": "Open borders (ECOWAS)",
    "remittances_pct_gdp": 3.5,
    "net_migration_rate_per_1k": -1.5
  },
  "_expand_digital_economy": {
    "e_participation_index": 0.25,
    "ict_development_index": 1.7,
    "mobile_money_accounts": 5000000,
    "digital_payments_pct_adults": 15,
    "fintech_companies": 5,
    "startup_ecosystem_value_usd": "$10 million",
    "data_protection_law": True,
    "cybersecurity_index_score": 25.0,
    "innovation_index_score": 15.0,
    "innovation_index_rank": 130,
    "ai_readiness_index": 18.0
  },
  "_expand_natural_resources": {
    "resource_curse_risk": "Moderate (gold mining revenue allocation; artisanal mining unregulated)"
  }
}
} # end DATA


def patch_country(slug, patch):
    path = os.path.join(BASE, slug, "index.json")
    with open(path) as f:
        data = json.load(f)
    cp = data["country_profile"]

    # 1. Add basic fields
    basics = patch.pop("_basics", {})
    for k, v in basics.items():
        cp[k] = v

    # 2. Add new sections (non-underscore-prefixed, non-_basics)
    new_sections = {k: v for k, v in patch.items() if not k.startswith("_")}
    for sec, val in new_sections.items():
        cp[sec] = val

    # 3. Expand existing sections (underscore-prefixed)
    for key, val in patch.items():
        if key.startswith("_expand_"):
            sec_name = key.replace("_expand_", "")
            if sec_name in cp and isinstance(cp[sec_name], dict):
                cp[sec_name].update(val)

    # 4. Update _meta fields
    meta = data.get("_meta", {})
    meta["sub_region"] = meta.get("sub_region", "")
    meta["iso3166_numeric"] = meta.get("iso3166_numeric", "000")
    meta["data_year"] = 2024

    # 5. Update leadership if needed
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
    print(f"\nBatch 1 done. {total} countries enhanced.")


if __name__ == "__main__":
    main()
