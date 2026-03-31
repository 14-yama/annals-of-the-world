#!/usr/bin/env python3
"""
Populate demographics, economy, health, governance, military, trade,
infrastructure, climate, education, and digital economy data for all
14 Oceania countries in the geo-registry.

Sources: World Bank, CIA World Factbook, UNDP, WHO, ITU (2023–2024 data).

Usage:
    python3 geo-registry/scripts/populate_oceania.py          # live run
    python3 geo-registry/scripts/populate_oceania.py --dry-run # preview only
"""
import json
import os
import sys
import copy

DRY_RUN = "--dry-run" in sys.argv
BASE = os.path.join(os.path.dirname(__file__), "..", "places", "countries")

# ──────────────────────────────────────────────────────────────────────
# Real-world data for 14 Oceania countries (2023-2024 estimates)
# ──────────────────────────────────────────────────────────────────────

OCEANIA_DATA = {
    "australia": {
        "data_year": 2024,
        "demographics": {
            "median_age": 37.9,
            "urbanization_pct": 86.6,
            "fertility_rate": 1.63,
            "life_expectancy": 83.7,
            "life_expectancy_male": 81.7,
            "life_expectancy_female": 85.7,
            "infant_mortality_per_1k": 3.1,
            "under5_mortality_per_1k": 3.7,
            "literacy_rate_pct": 99.0,
            "net_migration_rate": 5.9,
            "population_growth_rate": 1.0,
            "urban_population_growth": 1.1,
            "sex_ratio": 0.99,
            "dependency_ratio": 53.7,
            "population_density": 3.3,
            "age_structure": {
                "0_14_pct": 18.7,
                "15_24_pct": 12.2,
                "25_54_pct": 40.8,
                "55_64_pct": 12.0,
                "65_plus_pct": 16.3
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 2.0,
            "inflation_pct": 5.6,
            "unemployment_pct": 3.7,
            "poverty_rate_pct": 0.5,
            "gini_index": 34.3,
            "sector_agriculture_pct": 2.3,
            "sector_industry_pct": 25.3,
            "sector_services_pct": 72.4,
            "labor_force": 14200000,
            "fdi_inflow_usd": 24000000000,
            "foreign_exchange_reserves_usd": 55000000000,
            "ease_of_doing_business_rank": 14,
            "economic_freedom_index_score": 77.7,
            "credit_ratings": "AAA (S&P, Moody's, Fitch)"
        },
        "natural_resources": {
            "primary": ["iron ore", "coal", "natural gas", "gold", "bauxite", "uranium", "lithium", "rare earths", "zinc", "nickel"],
            "resource_dependency_pct_gdp": 10.4,
            "resource_curse_risk": "Low",
            "notes": "World's largest exporter of iron ore and coal; significant LNG exporter; major lithium reserves in Western Australia"
        },
        "military": {
            "budget_usd": 32400000000,
            "pct_of_gdp": 2.0,
            "active_personnel": 59000,
            "reserve_personnel": 29300,
            "paramilitary_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["AUKUS", "Five Eyes", "ANZUS", "QUAD"],
            "conscription": False,
            "global_firepower_rank": 16,
            "notes": "Acquiring nuclear-powered submarines under AUKUS; major US alliance partner in Indo-Pacific"
        },
        "trade": {
            "top_exports": ["iron ore", "coal", "natural gas", "gold", "aluminium", "beef", "wheat", "education services"],
            "top_imports": ["refined petroleum", "vehicles", "telecom equipment", "computers", "pharmaceuticals"],
            "major_partners": ["China", "Japan", "South Korea", "India", "United States"],
            "trade_balance": "Surplus",
            "remittances_pct_gdp": 0.1,
            "total_exports_usd": 464000000000,
            "total_imports_usd": 342000000000,
            "trade_as_pct_gdp": 45.5,
            "trade_agreements": ["CPTPP", "RCEP", "AUSFTA", "AANZFTA", "AUKUS"]
        },
        "infrastructure": {
            "internet_penetration_pct": 96.2,
            "broadband_subscriptions_per_100": 32.8,
            "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 110.7,
            "4g_coverage_pct": 99.4,
            "5g_coverage_pct": 50.0,
            "railway_km": 33168,
            "road_network_km": 877700,
            "paved_roads_pct": 47.0,
            "waterways_km": 2000,
            "notes": "NBN (National Broadband Network) provides fixed broadband; vast road network for remote areas"
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 75, "rank": 14, "year": 2023},
            "press_freedom_index": {"rank": 27, "year": 2024},
            "democracy_index": {"score": 8.71, "category": "Full democracy", "year": 2023},
            "fragile_states_index": {"score": 22.6, "year": 2023},
            "rule_of_law_index": {"score": 0.80, "rank": 16, "year": 2023},
            "government_effectiveness_index": {"percentile": 90.9, "year": 2022},
            "regulatory_quality_index": {"percentile": 95.7, "year": 2022},
            "political_stability_index": {"percentile": 76.4, "year": 2022}
        },
        "health": {
            "health_expenditure_pct_gdp": 10.0,
            "health_expenditure_per_capita_usd": 5627,
            "physician_density_per_1k": 3.8,
            "nurse_density_per_1k": 12.5,
            "hospital_beds_per_1k": 3.8,
            "maternal_mortality_per_100k": 3,
            "vaccination_coverage_pct": 95,
            "malaria_incidence_per_1k": 0,
            "tuberculosis_incidence_per_100k": 6.5,
            "hiv_prevalence_pct": 0.1,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 100,
            "obesity_pct": 31.7,
            "universal_health_coverage_index": 86,
            "leading_causes_of_death": ["heart disease", "dementia", "cerebrovascular disease", "lung cancer", "COPD"]
        },
        "climate_environment": {
            "climate_zones": ["arid", "semi-arid", "tropical", "temperate"],
            "avg_temperature_c": 21.9,
            "avg_rainfall_mm": 534,
            "co2_emissions_mt": 386.1,
            "co2_per_capita_t": 14.9,
            "renewable_energy_pct": 32.5,
            "natural_hazards": ["bushfires", "droughts", "cyclones", "floods"],
            "protected_areas_pct": 20.5,
            "deforestation_rate_pct": 0.0,
            "water_stress_level": "High",
            "environmental_performance_index": {"score": 60.1, "rank": 17},
            "paris_agreement_status": "Ratified",
            "biodiversity": {"known_species": 566398, "endemic_species": 87000, "threatened_species": 1942}
        },
        "education": {
            "expenditure_pct_gdp": 6.1,
            "primary_enrollment_pct": 100,
            "secondary_enrollment_pct": 99,
            "tertiary_enrollment_pct": 113,
            "gender_parity_index": 1.01,
            "mean_years_of_schooling": 12.7,
            "expected_years_of_schooling": 21.1,
            "pisa_participation": True,
            "pisa_scores": {"reading": 498, "math": 487, "science": 507},
            "student_teacher_ratio_primary": 15.4,
            "out_of_school_children": 0,
            "top_universities": ["University of Melbourne", "University of Sydney", "ANU", "UNSW", "University of Queensland", "Monash University"],
            "academic_freedom_index": 0.93
        },
        "digital_economy": {
            "e_government_index": 0.94,
            "e_participation_index": 0.92,
            "ict_development_index": 8.18,
            "mobile_money_adoption": "Low (card-based economy)",
            "fintech_companies": 800,
            "tech_hubs": ["Sydney", "Melbourne", "Brisbane"],
            "startup_ecosystem_value": 25000000000,
            "data_protection_law": "Privacy Act 1988 (amended 2022)",
            "cybersecurity_index": 97.47,
            "innovation_index": 25,
            "ai_readiness_index": 75.8
        },
        "diaspora_migration": {
            "diaspora_population": "1,000,000",
            "top_destinations": ["United Kingdom", "United States", "New Zealand", "Canada"],
            "refugees_hosted": 92700,
            "refugees_produced": 0,
            "remittances_usd": "3,200,000,000",
            "remittances_pct_gdp": 0.2,
            "net_migration_rate": 5.9
        },
        "debt_aid": {
            "national_debt_pct_gdp": 51.0,
            "external_debt_usd": "1,900,000,000,000",
            "foreign_aid_given_usd": "4,800,000,000",
            "notes": "Net aid donor; member of OECD DAC"
        }
    },

    "new-zealand": {
        "data_year": 2024,
        "demographics": {
            "median_age": 37.4,
            "urbanization_pct": 86.9,
            "fertility_rate": 1.56,
            "life_expectancy": 82.5,
            "life_expectancy_male": 80.6,
            "life_expectancy_female": 84.3,
            "infant_mortality_per_1k": 3.5,
            "under5_mortality_per_1k": 4.3,
            "literacy_rate_pct": 99.0,
            "net_migration_rate": 4.9,
            "population_growth_rate": 0.95,
            "urban_population_growth": 1.0,
            "sex_ratio": 0.99,
            "dependency_ratio": 52.9,
            "population_density": 19.3,
            "age_structure": {
                "0_14_pct": 19.2,
                "15_24_pct": 12.8,
                "25_54_pct": 39.8,
                "55_64_pct": 12.1,
                "65_plus_pct": 16.1
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 1.1,
            "inflation_pct": 5.7,
            "unemployment_pct": 3.9,
            "poverty_rate_pct": 0.5,
            "gini_index": 32.7,
            "sector_agriculture_pct": 5.7,
            "sector_industry_pct": 19.5,
            "sector_services_pct": 74.8,
            "labor_force": 2900000,
            "fdi_inflow_usd": 2400000000,
            "ease_of_doing_business_rank": 1,
            "economic_freedom_index_score": 83.9,
            "credit_ratings": "AA+ (S&P), Aaa (Moody's)"
        },
        "natural_resources": {
            "primary": ["natural gas", "iron ore", "sand", "coal", "timber", "hydropower", "gold", "limestone"],
            "resource_dependency_pct_gdp": 3.1,
            "resource_curse_risk": "Low",
            "notes": "Significant geothermal energy resources; dairy and agriculture are primary economic drivers"
        },
        "military": {
            "budget_usd": 3300000000,
            "pct_of_gdp": 1.5,
            "active_personnel": 9700,
            "reserve_personnel": 2400,
            "paramilitary_personnel": 0,
            "nuclear_status": "Nuclear-free zone (1987)",
            "alliances": ["Five Eyes", "ANZUS (suspended US component)"],
            "conscription": False,
            "global_firepower_rank": 87,
            "notes": "Nuclear-free policy since 1987; small professional defense force focused on South Pacific stability"
        },
        "trade": {
            "top_exports": ["dairy products", "meat", "wood", "fruit", "wine", "fish", "wool"],
            "top_imports": ["vehicles", "machinery", "petroleum", "electronics", "textiles"],
            "major_partners": ["China", "Australia", "United States", "Japan", "South Korea"],
            "trade_balance": "Deficit",
            "remittances_pct_gdp": 0.2,
            "total_exports_usd": 48600000000,
            "total_imports_usd": 54200000000,
            "trade_as_pct_gdp": 52.7,
            "trade_agreements": ["CPTPP", "RCEP", "AANZFTA", "NZ-China FTA"]
        },
        "infrastructure": {
            "internet_penetration_pct": 95.3,
            "broadband_subscriptions_per_100": 36.5,
            "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 135.8,
            "4g_coverage_pct": 98.0,
            "5g_coverage_pct": 30.0,
            "railway_km": 4128,
            "road_network_km": 94000,
            "paved_roads_pct": 66.0,
            "waterways_km": 0,
            "notes": "High broadband penetration; fiber rollout ongoing"
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 85, "rank": 3, "year": 2023},
            "press_freedom_index": {"rank": 13, "year": 2024},
            "democracy_index": {"score": 9.61, "category": "Full democracy", "year": 2023},
            "fragile_states_index": {"score": 18.3, "year": 2023},
            "rule_of_law_index": {"score": 0.83, "rank": 7, "year": 2023},
            "government_effectiveness_index": {"percentile": 93.3, "year": 2022},
            "regulatory_quality_index": {"percentile": 97.1, "year": 2022},
            "political_stability_index": {"percentile": 90.6, "year": 2022}
        },
        "health": {
            "health_expenditure_pct_gdp": 9.7,
            "health_expenditure_per_capita_usd": 4490,
            "physician_density_per_1k": 3.6,
            "nurse_density_per_1k": 11.0,
            "hospital_beds_per_1k": 2.6,
            "maternal_mortality_per_100k": 7,
            "vaccination_coverage_pct": 92,
            "malaria_incidence_per_1k": 0,
            "tuberculosis_incidence_per_100k": 6.2,
            "hiv_prevalence_pct": 0.1,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 100,
            "obesity_pct": 32.2,
            "universal_health_coverage_index": 87,
            "leading_causes_of_death": ["heart disease", "cancer", "cerebrovascular disease", "COPD", "dementia"]
        },
        "climate_environment": {
            "climate_zones": ["temperate", "oceanic", "alpine"],
            "avg_temperature_c": 12.1,
            "avg_rainfall_mm": 1732,
            "co2_emissions_mt": 34.2,
            "co2_per_capita_t": 6.6,
            "renewable_energy_pct": 82.0,
            "natural_hazards": ["earthquakes", "volcanic eruptions", "floods", "landslides"],
            "protected_areas_pct": 32.4,
            "deforestation_rate_pct": 0.0,
            "water_stress_level": "Low",
            "environmental_performance_index": {"score": 60.7, "rank": 15},
            "paris_agreement_status": "Ratified",
            "biodiversity": {"known_species": 70000, "endemic_species": 31000, "threatened_species": 936}
        },
        "education": {
            "expenditure_pct_gdp": 6.3,
            "primary_enrollment_pct": 100,
            "secondary_enrollment_pct": 99,
            "tertiary_enrollment_pct": 79,
            "gender_parity_index": 1.02,
            "mean_years_of_schooling": 12.8,
            "expected_years_of_schooling": 18.8,
            "pisa_participation": True,
            "pisa_scores": {"reading": 501, "math": 479, "science": 504},
            "student_teacher_ratio_primary": 14.5,
            "out_of_school_children": 0,
            "top_universities": ["University of Auckland", "University of Otago", "Victoria University of Wellington", "University of Canterbury"],
            "academic_freedom_index": 0.95
        },
        "digital_economy": {
            "e_government_index": 0.94,
            "e_participation_index": 0.91,
            "ict_development_index": 7.86,
            "mobile_money_adoption": "Low (card-based economy)",
            "fintech_companies": 120,
            "tech_hubs": ["Auckland", "Wellington", "Christchurch"],
            "startup_ecosystem_value": 5000000000,
            "data_protection_law": "Privacy Act 2020",
            "cybersecurity_index": 92.42,
            "innovation_index": 24,
            "ai_readiness_index": 72.5
        },
        "diaspora_migration": {
            "diaspora_population": "1,000,000",
            "top_destinations": ["Australia", "United Kingdom", "United States", "Canada"],
            "refugees_hosted": 2500,
            "refugees_produced": 0,
            "remittances_usd": "600,000,000",
            "remittances_pct_gdp": 0.3,
            "net_migration_rate": 4.9
        },
        "debt_aid": {
            "national_debt_pct_gdp": 42.5,
            "external_debt_usd": "102,000,000,000",
            "foreign_aid_given_usd": "800,000,000",
            "notes": "Net aid donor; Pacific Reset development strategy"
        }
    },

    "papua-new-guinea": {
        "data_year": 2024,
        "demographics": {
            "median_age": 22.4,
            "urbanization_pct": 13.2,
            "fertility_rate": 3.5,
            "life_expectancy": 65.0,
            "life_expectancy_male": 63.2,
            "life_expectancy_female": 66.9,
            "infant_mortality_per_1k": 35.3,
            "under5_mortality_per_1k": 44.7,
            "literacy_rate_pct": 64.2,
            "net_migration_rate": 0.0,
            "population_growth_rate": 1.6,
            "urban_population_growth": 2.5,
            "sex_ratio": 1.06,
            "dependency_ratio": 63.2,
            "population_density": 20.0,
            "age_structure": {
                "0_14_pct": 33.6,
                "15_24_pct": 19.6,
                "25_54_pct": 37.2,
                "55_64_pct": 5.7,
                "65_plus_pct": 3.9
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 3.0,
            "inflation_pct": 4.3,
            "unemployment_pct": 2.5,
            "poverty_rate_pct": 39.9,
            "gini_index": 41.9,
            "sector_agriculture_pct": 19.6,
            "sector_industry_pct": 38.3,
            "sector_services_pct": 42.1,
            "labor_force": 3700000,
            "fdi_inflow_usd": 350000000,
            "ease_of_doing_business_rank": 120,
            "economic_freedom_index_score": 54.4
        },
        "natural_resources": {
            "primary": ["gold", "copper", "silver", "natural gas", "oil", "timber", "fisheries"],
            "resource_dependency_pct_gdp": 26.0,
            "resource_curse_risk": "High",
            "notes": "PNG LNG project operated by ExxonMobil; Ok Tedi and Porgera gold mines; 800+ languages make governance complex"
        },
        "military": {
            "budget_usd": 120000000,
            "pct_of_gdp": 0.4,
            "active_personnel": 3800,
            "reserve_personnel": 0,
            "paramilitary_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum", "MSG"],
            "conscription": False,
            "global_firepower_rank": 0,
            "notes": "Small defense force; relies on Australia for security assistance"
        },
        "trade": {
            "top_exports": ["LNG", "gold", "copper", "palm oil", "coffee", "cocoa", "timber"],
            "top_imports": ["machinery", "food", "fuel", "chemicals", "transport equipment"],
            "major_partners": ["Australia", "China", "Japan", "Singapore", "South Korea"],
            "trade_balance": "Surplus",
            "remittances_pct_gdp": 0.1,
            "total_exports_usd": 12500000000,
            "total_imports_usd": 3400000000,
            "trade_as_pct_gdp": 53.0
        },
        "infrastructure": {
            "internet_penetration_pct": 32.0,
            "broadband_subscriptions_per_100": 0.2,
            "electricity_access_pct": 19.0,
            "mobile_subscriptions_per_100": 48.0,
            "4g_coverage_pct": 15.0,
            "5g_coverage_pct": 0,
            "railway_km": 0,
            "road_network_km": 9349,
            "paved_roads_pct": 3.5,
            "waterways_km": 11000,
            "notes": "Extremely challenging terrain; rivers serve as primary transport corridors; limited road infrastructure"
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 28, "rank": 130, "year": 2023},
            "press_freedom_index": {"rank": 62, "year": 2024},
            "democracy_index": {"score": 6.03, "category": "Flawed democracy", "year": 2023},
            "fragile_states_index": {"score": 76.6, "year": 2023},
            "rule_of_law_index": {"score": 0.39, "rank": 103, "year": 2023},
            "government_effectiveness_index": {"percentile": 14.4, "year": 2022}
        },
        "health": {
            "health_expenditure_pct_gdp": 2.5,
            "health_expenditure_per_capita_usd": 75,
            "physician_density_per_1k": 0.07,
            "nurse_density_per_1k": 0.57,
            "hospital_beds_per_1k": 0.0,
            "maternal_mortality_per_100k": 145,
            "vaccination_coverage_pct": 62,
            "malaria_incidence_per_1k": 94.0,
            "tuberculosis_incidence_per_100k": 432,
            "hiv_prevalence_pct": 0.9,
            "clean_water_access_pct": 41,
            "sanitation_access_pct": 19,
            "obesity_pct": 21.3,
            "universal_health_coverage_index": 40,
            "leading_causes_of_death": ["malaria", "tuberculosis", "lower respiratory infections", "diarrheal diseases", "neonatal disorders"]
        },
        "climate_environment": {
            "climate_zones": ["tropical", "equatorial", "highland"],
            "avg_temperature_c": 26.0,
            "avg_rainfall_mm": 2500,
            "co2_emissions_mt": 7.3,
            "co2_per_capita_t": 0.7,
            "renewable_energy_pct": 37.2,
            "natural_hazards": ["volcanic eruptions", "earthquakes", "tsunamis", "floods", "landslides"],
            "protected_areas_pct": 3.1,
            "deforestation_rate_pct": 0.5,
            "water_stress_level": "Low",
            "paris_agreement_status": "Ratified",
            "biodiversity": {"known_species": 31000, "endemic_species": 15000, "threatened_species": 610}
        },
        "education": {
            "expenditure_pct_gdp": 1.4,
            "primary_enrollment_pct": 73,
            "secondary_enrollment_pct": 35,
            "tertiary_enrollment_pct": 6,
            "gender_parity_index": 0.88,
            "mean_years_of_schooling": 4.6,
            "expected_years_of_schooling": 10.0,
            "pisa_participation": False,
            "top_universities": ["University of Papua New Guinea", "PNG University of Technology"],
            "academic_freedom_index": 0.55
        },
        "digital_economy": {
            "e_government_index": 0.36,
            "mobile_money_adoption": "Growing (MiBank, BSP)",
            "tech_hubs": ["Port Moresby"],
            "cybersecurity_index": 19.7,
            "innovation_index": 0
        },
        "diaspora_migration": {
            "diaspora_population": "25,000",
            "top_destinations": ["Australia", "New Zealand"],
            "refugees_hosted": 9700,
            "refugees_produced": 0,
            "remittances_usd": "10,000,000",
            "remittances_pct_gdp": 0.03,
            "net_migration_rate": 0.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 49.5,
            "external_debt_usd": "12,000,000,000",
            "foreign_aid_received_usd": "1,200,000,000",
            "top_donors": ["Australia", "Japan", "New Zealand", "EU", "ADB"],
            "notes": "Largest Pacific Island aid recipient"
        }
    },

    "fiji": {
        "data_year": 2024,
        "demographics": {
            "median_age": 28.9,
            "urbanization_pct": 58.0,
            "fertility_rate": 2.3,
            "life_expectancy": 67.8,
            "life_expectancy_male": 65.3,
            "life_expectancy_female": 70.5,
            "infant_mortality_per_1k": 16.4,
            "under5_mortality_per_1k": 21.3,
            "literacy_rate_pct": 99.1,
            "net_migration_rate": -6.0,
            "population_growth_rate": 0.4,
            "population_density": 49.5,
            "age_structure": {
                "0_14_pct": 26.2,
                "15_24_pct": 15.5,
                "25_54_pct": 41.1,
                "55_64_pct": 9.4,
                "65_plus_pct": 7.8
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 8.0,
            "inflation_pct": 3.4,
            "unemployment_pct": 4.5,
            "poverty_rate_pct": 29.9,
            "gini_index": 36.7,
            "sector_agriculture_pct": 10.0,
            "sector_industry_pct": 17.7,
            "sector_services_pct": 72.3,
            "labor_force": 365000,
            "fdi_inflow_usd": 430000000,
            "ease_of_doing_business_rank": 102
        },
        "natural_resources": {
            "primary": ["timber", "fisheries", "gold", "copper", "hydropower"],
            "resource_dependency_pct_gdp": 4.2,
            "resource_curse_risk": "Low",
            "notes": "Tourism is the primary economic driver; sugar and garments are key exports"
        },
        "military": {
            "budget_usd": 69500000,
            "pct_of_gdp": 1.5,
            "active_personnel": 3500,
            "reserve_personnel": 6000,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum", "MSG"],
            "conscription": False,
            "notes": "Significant UN peacekeeping contributors; Fiji military has staged 4 coups since 1987"
        },
        "trade": {
            "top_exports": ["sugar", "fish", "gold", "garments", "timber", "mineral water"],
            "top_imports": ["machinery", "petroleum", "food", "chemicals", "vehicles"],
            "major_partners": ["Australia", "New Zealand", "United States", "China", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 1200000000,
            "total_imports_usd": 3100000000,
            "trade_as_pct_gdp": 78.0
        },
        "infrastructure": {
            "internet_penetration_pct": 83.0,
            "electricity_access_pct": 94.0,
            "mobile_subscriptions_per_100": 115.0,
            "4g_coverage_pct": 75.0,
            "railway_km": 597,
            "road_network_km": 3440,
            "paved_roads_pct": 49.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 53, "rank": 52, "year": 2023},
            "press_freedom_index": {"rank": 55, "year": 2024},
            "democracy_index": {"score": 5.87, "category": "Hybrid regime", "year": 2023},
            "fragile_states_index": {"score": 63.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 3.8,
            "health_expenditure_per_capita_usd": 236,
            "physician_density_per_1k": 0.86,
            "nurse_density_per_1k": 3.3,
            "maternal_mortality_per_100k": 38,
            "vaccination_coverage_pct": 85,
            "tuberculosis_incidence_per_100k": 48,
            "hiv_prevalence_pct": 0.1,
            "clean_water_access_pct": 94,
            "sanitation_access_pct": 91,
            "obesity_pct": 30.2,
            "universal_health_coverage_index": 56,
            "leading_causes_of_death": ["heart disease", "diabetes", "cerebrovascular disease", "cancer", "respiratory infections"]
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 25.6,
            "avg_rainfall_mm": 2592,
            "co2_emissions_mt": 1.7,
            "co2_per_capita_t": 1.8,
            "renewable_energy_pct": 54.0,
            "natural_hazards": ["cyclones", "floods", "droughts"],
            "protected_areas_pct": 3.8,
            "paris_agreement_status": "Ratified",
            "biodiversity": {"known_species": 4000, "endemic_species": 1500, "threatened_species": 134}
        },
        "education": {
            "expenditure_pct_gdp": 5.5,
            "primary_enrollment_pct": 98,
            "secondary_enrollment_pct": 86,
            "tertiary_enrollment_pct": 16,
            "mean_years_of_schooling": 10.1,
            "expected_years_of_schooling": 14.2,
            "pisa_participation": False,
            "top_universities": ["University of the South Pacific", "Fiji National University"],
            "academic_freedom_index": 0.55
        },
        "digital_economy": {
            "e_government_index": 0.59,
            "mobile_money_adoption": "Growing (M-PAiSA, Vodafone Fiji)",
            "tech_hubs": ["Suva"],
            "cybersecurity_index": 52.3,
            "innovation_index": 0
        },
        "diaspora_migration": {
            "diaspora_population": "200,000",
            "top_destinations": ["Australia", "New Zealand", "United States", "Canada"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "330,000,000",
            "remittances_pct_gdp": 6.0,
            "net_migration_rate": -6.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 81.2,
            "external_debt_usd": "2,200,000,000",
            "foreign_aid_received_usd": "200,000,000",
            "top_donors": ["Australia", "New Zealand", "Japan", "EU"]
        }
    },

    "samoa": {
        "data_year": 2024,
        "demographics": {
            "median_age": 23.5,
            "urbanization_pct": 17.0,
            "fertility_rate": 3.9,
            "life_expectancy": 74.0,
            "life_expectancy_male": 71.3,
            "life_expectancy_female": 76.9,
            "infant_mortality_per_1k": 14.8,
            "under5_mortality_per_1k": 17.5,
            "literacy_rate_pct": 99.1,
            "net_migration_rate": -8.3,
            "population_growth_rate": 0.6,
            "population_density": 70.3,
            "age_structure": {
                "0_14_pct": 30.2,
                "15_24_pct": 19.5,
                "25_54_pct": 36.3,
                "55_64_pct": 7.2,
                "65_plus_pct": 6.8
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 5.0,
            "inflation_pct": 8.8,
            "unemployment_pct": 9.8,
            "poverty_rate_pct": 18.8,
            "sector_agriculture_pct": 10.4,
            "sector_industry_pct": 22.7,
            "sector_services_pct": 66.9,
            "labor_force": 60000
        },
        "natural_resources": {
            "primary": ["hardwood forests", "fisheries", "hydropower"],
            "resource_dependency_pct_gdp": 2.0,
            "notes": "Limited mineral resources; economy dependent on remittances and aid"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum"],
            "notes": "No military; police handle security; New Zealand provides defense under Treaty of Friendship"
        },
        "trade": {
            "top_exports": ["fish", "coconut oil", "copra", "taro", "automotive parts (Yazaki)"],
            "top_imports": ["food", "machinery", "fuels", "chemicals"],
            "major_partners": ["New Zealand", "Australia", "American Samoa", "United States"],
            "trade_balance": "Deficit",
            "total_exports_usd": 105000000,
            "total_imports_usd": 500000000,
            "remittances_pct_gdp": 25.0
        },
        "infrastructure": {
            "internet_penetration_pct": 57.0,
            "electricity_access_pct": 98.0,
            "mobile_subscriptions_per_100": 66.0,
            "road_network_km": 2340,
            "paved_roads_pct": 14.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 31, "year": 2024},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 63.2, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 6.0,
            "health_expenditure_per_capita_usd": 257,
            "physician_density_per_1k": 0.6,
            "maternal_mortality_per_100k": 59,
            "vaccination_coverage_pct": 58,
            "tuberculosis_incidence_per_100k": 18,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 92,
            "sanitation_access_pct": 91,
            "obesity_pct": 47.3,
            "universal_health_coverage_index": 53,
            "leading_causes_of_death": ["heart disease", "diabetes", "stroke", "cancer", "respiratory disease"]
        },
        "climate_environment": {
            "climate_zones": ["tropical"],
            "avg_temperature_c": 26.5,
            "avg_rainfall_mm": 3000,
            "co2_emissions_mt": 0.3,
            "co2_per_capita_t": 1.3,
            "renewable_energy_pct": 50.0,
            "natural_hazards": ["cyclones", "tsunamis", "volcanic activity"],
            "protected_areas_pct": 8.0,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 4.8,
            "primary_enrollment_pct": 98,
            "secondary_enrollment_pct": 79,
            "tertiary_enrollment_pct": 12,
            "mean_years_of_schooling": 10.7,
            "expected_years_of_schooling": 12.8,
            "pisa_participation": False,
            "top_universities": ["National University of Samoa"],
            "academic_freedom_index": 0.65
        },
        "digital_economy": {
            "e_government_index": 0.46,
            "mobile_money_adoption": "Emerging",
            "tech_hubs": [],
            "cybersecurity_index": 12.0
        },
        "diaspora_migration": {
            "diaspora_population": "300,000",
            "top_destinations": ["New Zealand", "Australia", "American Samoa", "United States"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "210,000,000",
            "remittances_pct_gdp": 25.0,
            "net_migration_rate": -8.3
        },
        "debt_aid": {
            "national_debt_pct_gdp": 47.0,
            "foreign_aid_received_usd": "120,000,000",
            "top_donors": ["Australia", "New Zealand", "China", "Japan"]
        }
    },

    "tonga": {
        "data_year": 2024,
        "demographics": {
            "median_age": 22.1,
            "urbanization_pct": 23.0,
            "fertility_rate": 3.1,
            "life_expectancy": 71.3,
            "life_expectancy_male": 69.4,
            "life_expectancy_female": 73.3,
            "infant_mortality_per_1k": 10.6,
            "under5_mortality_per_1k": 13.1,
            "literacy_rate_pct": 99.4,
            "net_migration_rate": -17.9,
            "population_growth_rate": -0.3,
            "population_density": 146.4,
            "age_structure": {
                "0_14_pct": 30.6,
                "15_24_pct": 19.5,
                "25_54_pct": 33.3,
                "55_64_pct": 8.1,
                "65_plus_pct": 8.5
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 2.5,
            "inflation_pct": 6.4,
            "unemployment_pct": 1.0,
            "poverty_rate_pct": 22.1,
            "sector_agriculture_pct": 15.6,
            "sector_industry_pct": 22.1,
            "sector_services_pct": 62.3,
            "labor_force": 36000
        },
        "natural_resources": {
            "primary": ["fisheries", "arable land"],
            "resource_dependency_pct_gdp": 1.0,
            "notes": "Very limited natural resources; economy heavily dependent on remittances (37% of GDP)"
        },
        "military": {
            "budget_usd": 9000000,
            "pct_of_gdp": 1.6,
            "active_personnel": 500,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum"],
            "notes": "Tonga Defence Services; contributed troops to Iraq and Afghanistan"
        },
        "trade": {
            "top_exports": ["squash", "fish", "vanilla", "root crops"],
            "top_imports": ["food", "fuel", "machinery", "vehicles", "building materials"],
            "major_partners": ["New Zealand", "Australia", "United States", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 15000000,
            "total_imports_usd": 310000000,
            "remittances_pct_gdp": 37.0
        },
        "infrastructure": {
            "internet_penetration_pct": 72.0,
            "electricity_access_pct": 98.0,
            "mobile_subscriptions_per_100": 60.0,
            "road_network_km": 680,
            "paved_roads_pct": 27.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 59.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 5.3,
            "health_expenditure_per_capita_usd": 263,
            "physician_density_per_1k": 0.6,
            "maternal_mortality_per_100k": 52,
            "vaccination_coverage_pct": 78,
            "tuberculosis_incidence_per_100k": 12,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 91,
            "obesity_pct": 48.2,
            "universal_health_coverage_index": 52,
            "leading_causes_of_death": ["heart disease", "diabetes", "stroke", "cancer", "respiratory disease"]
        },
        "climate_environment": {
            "climate_zones": ["tropical"],
            "avg_temperature_c": 25.0,
            "avg_rainfall_mm": 1750,
            "co2_emissions_mt": 0.2,
            "co2_per_capita_t": 1.9,
            "renewable_energy_pct": 12.0,
            "natural_hazards": ["cyclones", "earthquakes", "volcanic eruptions"],
            "protected_areas_pct": 3.0,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 6.6,
            "primary_enrollment_pct": 90,
            "secondary_enrollment_pct": 82,
            "tertiary_enrollment_pct": 8,
            "mean_years_of_schooling": 11.0,
            "expected_years_of_schooling": 14.4,
            "pisa_participation": False,
            "top_universities": ["University of the South Pacific (Tonga campus)"],
            "academic_freedom_index": 0.60
        },
        "digital_economy": {
            "e_government_index": 0.47,
            "mobile_money_adoption": "Emerging",
            "tech_hubs": [],
            "cybersecurity_index": 15.0
        },
        "diaspora_migration": {
            "diaspora_population": "120,000",
            "top_destinations": ["New Zealand", "Australia", "United States"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "200,000,000",
            "remittances_pct_gdp": 37.0,
            "net_migration_rate": -17.9
        },
        "debt_aid": {
            "national_debt_pct_gdp": 42.5,
            "foreign_aid_received_usd": "100,000,000",
            "top_donors": ["Australia", "New Zealand", "China", "Japan"]
        }
    },

    "vanuatu": {
        "data_year": 2024,
        "demographics": {
            "median_age": 21.8,
            "urbanization_pct": 25.5,
            "fertility_rate": 3.5,
            "life_expectancy": 71.0,
            "life_expectancy_male": 69.2,
            "life_expectancy_female": 72.9,
            "infant_mortality_per_1k": 21.6,
            "under5_mortality_per_1k": 26.2,
            "literacy_rate_pct": 87.5,
            "net_migration_rate": 0.0,
            "population_growth_rate": 2.3,
            "population_density": 25.6,
            "age_structure": {
                "0_14_pct": 33.2,
                "15_24_pct": 20.0,
                "25_54_pct": 35.6,
                "55_64_pct": 5.8,
                "65_plus_pct": 5.4
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 2.1,
            "inflation_pct": 4.5,
            "unemployment_pct": 5.3,
            "poverty_rate_pct": 12.7,
            "sector_agriculture_pct": 22.0,
            "sector_industry_pct": 9.7,
            "sector_services_pct": 68.3,
            "labor_force": 130000
        },
        "natural_resources": {
            "primary": ["manganese", "hardwood forests", "fisheries"],
            "resource_dependency_pct_gdp": 1.5,
            "notes": "Economy primarily based on agriculture, tourism, and offshore financial services"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum", "MSG"],
            "notes": "No military; Vanuatu Mobile Force (~300 officers) handles paramilitary and police functions"
        },
        "trade": {
            "top_exports": ["copra", "beef", "cocoa", "timber", "kava", "coffee"],
            "top_imports": ["machinery", "food", "fuel", "manufactures"],
            "major_partners": ["Australia", "New Zealand", "China", "Japan", "Thailand"],
            "trade_balance": "Deficit",
            "total_exports_usd": 40000000,
            "total_imports_usd": 420000000,
            "remittances_pct_gdp": 4.0
        },
        "infrastructure": {
            "internet_penetration_pct": 37.0,
            "electricity_access_pct": 62.0,
            "mobile_subscriptions_per_100": 79.0,
            "road_network_km": 1070,
            "paved_roads_pct": 23.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 41, "year": 2024},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 68.2, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 3.2,
            "health_expenditure_per_capita_usd": 110,
            "physician_density_per_1k": 0.17,
            "maternal_mortality_per_100k": 94,
            "vaccination_coverage_pct": 70,
            "tuberculosis_incidence_per_100k": 15,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 87,
            "sanitation_access_pct": 53,
            "obesity_pct": 25.2,
            "universal_health_coverage_index": 45,
            "leading_causes_of_death": ["heart disease", "stroke", "diabetes", "respiratory infections", "cancer"]
        },
        "climate_environment": {
            "climate_zones": ["tropical"],
            "avg_temperature_c": 25.5,
            "avg_rainfall_mm": 2360,
            "co2_emissions_mt": 0.1,
            "co2_per_capita_t": 0.5,
            "renewable_energy_pct": 30.0,
            "natural_hazards": ["cyclones", "earthquakes", "volcanic eruptions", "tsunamis"],
            "protected_areas_pct": 11.0,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 5.4,
            "primary_enrollment_pct": 93,
            "secondary_enrollment_pct": 53,
            "tertiary_enrollment_pct": 5,
            "mean_years_of_schooling": 6.7,
            "expected_years_of_schooling": 11.5,
            "pisa_participation": False,
            "top_universities": ["University of the South Pacific (Emalus campus)"],
            "academic_freedom_index": 0.60
        },
        "digital_economy": {
            "e_government_index": 0.42,
            "mobile_money_adoption": "Emerging",
            "tech_hubs": [],
            "cybersecurity_index": 14.0
        },
        "diaspora_migration": {
            "diaspora_population": "20,000",
            "top_destinations": ["New Caledonia", "Australia", "New Zealand"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "30,000,000",
            "remittances_pct_gdp": 3.0,
            "net_migration_rate": 0.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 48.0,
            "foreign_aid_received_usd": "160,000,000",
            "top_donors": ["Australia", "New Zealand", "China", "Japan", "EU"]
        }
    },

    "solomon-islands": {
        "data_year": 2024,
        "demographics": {
            "median_age": 19.9,
            "urbanization_pct": 25.1,
            "fertility_rate": 3.9,
            "life_expectancy": 73.6,
            "life_expectancy_male": 71.1,
            "life_expectancy_female": 76.3,
            "infant_mortality_per_1k": 14.9,
            "under5_mortality_per_1k": 19.0,
            "literacy_rate_pct": 84.1,
            "net_migration_rate": -2.0,
            "population_growth_rate": 2.3,
            "population_density": 25.6,
            "age_structure": {
                "0_14_pct": 36.8,
                "15_24_pct": 20.3,
                "25_54_pct": 33.4,
                "55_64_pct": 5.2,
                "65_plus_pct": 4.3
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 2.8,
            "inflation_pct": 4.8,
            "unemployment_pct": 2.0,
            "poverty_rate_pct": 12.7,
            "sector_agriculture_pct": 26.7,
            "sector_industry_pct": 11.7,
            "sector_services_pct": 61.6,
            "labor_force": 280000
        },
        "natural_resources": {
            "primary": ["fisheries", "forests", "gold", "bauxite", "phosphates", "lead", "zinc", "nickel"],
            "resource_dependency_pct_gdp": 35.0,
            "resource_curse_risk": "High",
            "notes": "Logging has been the primary revenue source; ban on log exports enacted 2023; shifting to tuna fisheries"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum", "MSG"],
            "notes": "No military; RAMSI (Regional Assistance Mission) 2003-2017 restored order after ethnic tensions"
        },
        "trade": {
            "top_exports": ["timber", "fish", "palm oil", "cocoa", "copra"],
            "top_imports": ["food", "fuel", "machinery", "manufactures", "chemicals"],
            "major_partners": ["China", "Australia", "South Korea", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 500000000,
            "total_imports_usd": 700000000,
            "remittances_pct_gdp": 2.0
        },
        "infrastructure": {
            "internet_penetration_pct": 36.0,
            "electricity_access_pct": 67.0,
            "mobile_subscriptions_per_100": 71.0,
            "road_network_km": 1360,
            "paved_roads_pct": 2.4
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 43, "year": 2024},
            "democracy_index": {"score": 5.33, "category": "Hybrid regime", "year": 2023},
            "fragile_states_index": {"score": 78.1, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 4.2,
            "health_expenditure_per_capita_usd": 90,
            "physician_density_per_1k": 0.19,
            "maternal_mortality_per_100k": 104,
            "vaccination_coverage_pct": 75,
            "malaria_incidence_per_1k": 80.0,
            "tuberculosis_incidence_per_100k": 76,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 65,
            "sanitation_access_pct": 31,
            "obesity_pct": 22.5,
            "universal_health_coverage_index": 42,
            "leading_causes_of_death": ["heart disease", "diabetes", "stroke", "respiratory infections", "malaria"]
        },
        "climate_environment": {
            "climate_zones": ["tropical"],
            "avg_temperature_c": 26.5,
            "avg_rainfall_mm": 3050,
            "co2_emissions_mt": 0.2,
            "co2_per_capita_t": 0.3,
            "renewable_energy_pct": 15.0,
            "natural_hazards": ["cyclones", "earthquakes", "tsunamis", "volcanic eruptions"],
            "protected_areas_pct": 2.0,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 9.9,
            "primary_enrollment_pct": 84,
            "secondary_enrollment_pct": 42,
            "tertiary_enrollment_pct": 4,
            "mean_years_of_schooling": 5.5,
            "expected_years_of_schooling": 10.0,
            "pisa_participation": False,
            "top_universities": ["Solomon Islands National University"],
            "academic_freedom_index": 0.50
        },
        "digital_economy": {
            "e_government_index": 0.33,
            "mobile_money_adoption": "Limited",
            "tech_hubs": [],
            "cybersecurity_index": 8.0
        },
        "diaspora_migration": {
            "diaspora_population": "6,000",
            "top_destinations": ["Australia", "New Zealand"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "30,000,000",
            "remittances_pct_gdp": 2.0,
            "net_migration_rate": -2.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 15.3,
            "foreign_aid_received_usd": "300,000,000",
            "top_donors": ["Australia", "Japan", "New Zealand", "EU", "Taiwan"]
        }
    },

    "kiribati": {
        "data_year": 2024,
        "demographics": {
            "median_age": 23.4,
            "urbanization_pct": 57.0,
            "fertility_rate": 3.4,
            "life_expectancy": 69.2,
            "life_expectancy_male": 66.2,
            "life_expectancy_female": 72.4,
            "infant_mortality_per_1k": 30.0,
            "under5_mortality_per_1k": 47.0,
            "literacy_rate_pct": 96.0,
            "net_migration_rate": -2.0,
            "population_growth_rate": 1.5,
            "population_density": 147.0,
            "age_structure": {
                "0_14_pct": 33.0,
                "15_24_pct": 18.3,
                "25_54_pct": 36.4,
                "55_64_pct": 6.5,
                "65_plus_pct": 5.8
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 3.0,
            "inflation_pct": 2.8,
            "unemployment_pct": 30.6,
            "poverty_rate_pct": 21.8,
            "sector_agriculture_pct": 23.0,
            "sector_industry_pct": 7.0,
            "sector_services_pct": 70.0,
            "labor_force": 39000
        },
        "natural_resources": {
            "primary": ["fisheries (tuna)", "phosphate deposits (exhausted)"],
            "resource_dependency_pct_gdp": 55.0,
            "resource_curse_risk": "Moderate",
            "notes": "Revenue Equalization Reserve Fund (phosphate wealth, ~$1B); fishing licenses provide 50-75% government revenue"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum"],
            "notes": "No military; police force only; Australia and New Zealand provide security assistance"
        },
        "trade": {
            "top_exports": ["copra", "seaweed", "fish"],
            "top_imports": ["food", "fuel", "machinery", "manufactures"],
            "major_partners": ["Australia", "Fiji", "New Zealand", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 12000000,
            "total_imports_usd": 130000000,
            "remittances_pct_gdp": 10.0
        },
        "infrastructure": {
            "internet_penetration_pct": 47.0,
            "electricity_access_pct": 92.0,
            "mobile_subscriptions_per_100": 46.0,
            "road_network_km": 670,
            "paved_roads_pct": 0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 71.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 11.6,
            "health_expenditure_per_capita_usd": 204,
            "physician_density_per_1k": 0.2,
            "maternal_mortality_per_100k": 76,
            "vaccination_coverage_pct": 80,
            "tuberculosis_incidence_per_100k": 350,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 64,
            "sanitation_access_pct": 40,
            "obesity_pct": 46.0,
            "universal_health_coverage_index": 39,
            "leading_causes_of_death": ["diabetes", "heart disease", "stroke", "respiratory infections", "cancer"]
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 28.3,
            "avg_rainfall_mm": 1500,
            "co2_emissions_mt": 0.06,
            "co2_per_capita_t": 0.5,
            "renewable_energy_pct": 18.0,
            "natural_hazards": ["sea level rise", "storm surges", "droughts", "king tides"],
            "protected_areas_pct": 12.0,
            "paris_agreement_status": "Ratified",
            "notes": "Among the most climate-vulnerable nations; average elevation 2m above sea level"
        },
        "education": {
            "expenditure_pct_gdp": 12.4,
            "primary_enrollment_pct": 96,
            "secondary_enrollment_pct": 72,
            "tertiary_enrollment_pct": 4,
            "mean_years_of_schooling": 7.8,
            "expected_years_of_schooling": 11.8,
            "pisa_participation": False,
            "top_universities": ["Kiribati campus of USP"],
            "academic_freedom_index": 0.50
        },
        "digital_economy": {
            "e_government_index": 0.33,
            "mobile_money_adoption": "Very limited",
            "tech_hubs": [],
            "cybersecurity_index": 3.0
        },
        "diaspora_migration": {
            "diaspora_population": "8,000",
            "top_destinations": ["New Zealand", "Australia", "Fiji"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "20,000,000",
            "remittances_pct_gdp": 10.0,
            "net_migration_rate": -2.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 21.0,
            "foreign_aid_received_usd": "100,000,000",
            "top_donors": ["Australia", "New Zealand", "Taiwan", "Japan", "EU"],
            "notes": "Revenue Equalization Reserve Fund provides buffer; highly aid-dependent"
        }
    },

    "tuvalu": {
        "data_year": 2024,
        "demographics": {
            "median_age": 26.4,
            "urbanization_pct": 64.8,
            "fertility_rate": 2.9,
            "life_expectancy": 68.4,
            "life_expectancy_male": 66.1,
            "life_expectancy_female": 70.8,
            "infant_mortality_per_1k": 22.0,
            "under5_mortality_per_1k": 25.6,
            "literacy_rate_pct": 99.0,
            "net_migration_rate": -6.6,
            "population_growth_rate": 0.8,
            "population_density": 435.4,
            "age_structure": {
                "0_14_pct": 29.0,
                "15_24_pct": 18.5,
                "25_54_pct": 37.2,
                "55_64_pct": 8.6,
                "65_plus_pct": 6.7
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 4.0,
            "inflation_pct": 4.3,
            "unemployment_pct": 6.5,
            "poverty_rate_pct": 26.3,
            "sector_agriculture_pct": 16.6,
            "sector_industry_pct": 6.7,
            "sector_services_pct": 76.7,
            "labor_force": 3600
        },
        "natural_resources": {
            "primary": ["fisheries (tuna)"],
            "resource_dependency_pct_gdp": 60.0,
            "notes": "Tuvalu Trust Fund (est. 1987, ~$190M); .tv domain license revenue ~$5-10M/year (~10% govt revenue); fishing licenses major revenue source"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum"],
            "notes": "No military; police force of ~80 officers; Falepili Union with Australia (2023) provides security"
        },
        "trade": {
            "top_exports": ["copra", "fish"],
            "top_imports": ["food", "fuel", "manufactures", "machinery"],
            "major_partners": ["Australia", "Fiji", "New Zealand", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 600000,
            "total_imports_usd": 50000000,
            "remittances_pct_gdp": 13.0
        },
        "infrastructure": {
            "internet_penetration_pct": 49.0,
            "electricity_access_pct": 98.0,
            "mobile_subscriptions_per_100": 72.0,
            "road_network_km": 8,
            "paved_roads_pct": 100
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 72.0, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 16.5,
            "health_expenditure_per_capita_usd": 645,
            "physician_density_per_1k": 1.0,
            "maternal_mortality_per_100k": 0,
            "vaccination_coverage_pct": 82,
            "tuberculosis_incidence_per_100k": 236,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 84,
            "obesity_pct": 51.6,
            "universal_health_coverage_index": 42,
            "leading_causes_of_death": ["diabetes", "heart disease", "cancer", "respiratory infections", "kidney disease"]
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 29.0,
            "avg_rainfall_mm": 3000,
            "co2_emissions_mt": 0.01,
            "co2_per_capita_t": 1.0,
            "renewable_energy_pct": 20.0,
            "natural_hazards": ["sea level rise", "storm surges", "king tides", "tropical cyclones"],
            "protected_areas_pct": 5.0,
            "paris_agreement_status": "Ratified",
            "notes": "Highest point 4.6m; existential climate threat; Falepili Union with Australia offers climate refuge"
        },
        "education": {
            "expenditure_pct_gdp": 7.0,
            "primary_enrollment_pct": 94,
            "secondary_enrollment_pct": 75,
            "tertiary_enrollment_pct": 3,
            "mean_years_of_schooling": 9.3,
            "expected_years_of_schooling": 12.2,
            "pisa_participation": False,
            "top_universities": ["USP extension centre"],
            "academic_freedom_index": 0.55
        },
        "digital_economy": {
            "e_government_index": 0.37,
            "mobile_money_adoption": "Very limited",
            "tech_hubs": [],
            "cybersecurity_index": 5.0,
            "notes": ".tv domain leased to Verisign is major revenue source"
        },
        "diaspora_migration": {
            "diaspora_population": "4,000",
            "top_destinations": ["New Zealand", "Fiji", "Kiribati"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "5,000,000",
            "remittances_pct_gdp": 8.0,
            "net_migration_rate": -6.6
        },
        "debt_aid": {
            "national_debt_pct_gdp": 7.6,
            "foreign_aid_received_usd": "50,000,000",
            "top_donors": ["Australia", "New Zealand", "Taiwan", "Japan"],
            "notes": "Tuvalu Trust Fund protects fiscal stability; low debt burden"
        }
    },

    "marshall-islands": {
        "data_year": 2024,
        "demographics": {
            "median_age": 23.8,
            "urbanization_pct": 78.2,
            "fertility_rate": 2.8,
            "life_expectancy": 74.6,
            "life_expectancy_male": 72.2,
            "life_expectancy_female": 77.1,
            "infant_mortality_per_1k": 19.3,
            "under5_mortality_per_1k": 28.0,
            "literacy_rate_pct": 98.3,
            "net_migration_rate": -5.0,
            "population_growth_rate": 0.3,
            "population_density": 324.5,
            "age_structure": {
                "0_14_pct": 30.7,
                "15_24_pct": 17.0,
                "25_54_pct": 38.5,
                "55_64_pct": 7.8,
                "65_plus_pct": 6.0
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 1.5,
            "inflation_pct": 3.0,
            "unemployment_pct": 36.0,
            "poverty_rate_pct": 30.0,
            "sector_agriculture_pct": 4.4,
            "sector_industry_pct": 9.9,
            "sector_services_pct": 85.7,
            "labor_force": 10000
        },
        "natural_resources": {
            "primary": ["fisheries (tuna)", "deep-sea minerals", "coconut products"],
            "resource_dependency_pct_gdp": 50.0,
            "notes": "Compact of Free Association with US provides ~$70M/year; ship registry is 3rd largest in the world"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Compact of Free Association (USA)", "Pacific Islands Forum"],
            "notes": "US responsible for defense under Compact; Kwajalein Atoll hosts US military missile testing facility"
        },
        "trade": {
            "top_exports": ["copra", "coconut oil", "handicrafts", "fish"],
            "top_imports": ["food", "machinery", "fuel", "beverages", "tobacco"],
            "major_partners": ["United States", "Japan", "Australia", "China"],
            "trade_balance": "Deficit",
            "total_exports_usd": 6400000,
            "total_imports_usd": 130000000,
            "remittances_pct_gdp": 12.0
        },
        "infrastructure": {
            "internet_penetration_pct": 38.0,
            "electricity_access_pct": 95.0,
            "mobile_subscriptions_per_100": 30.0,
            "road_network_km": 2028,
            "paved_roads_pct": 35.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 69.0, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 17.0,
            "health_expenditure_per_capita_usd": 750,
            "physician_density_per_1k": 0.42,
            "maternal_mortality_per_100k": 0,
            "vaccination_coverage_pct": 75,
            "tuberculosis_incidence_per_100k": 480,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 94,
            "sanitation_access_pct": 77,
            "obesity_pct": 52.9,
            "universal_health_coverage_index": 44,
            "leading_causes_of_death": ["diabetes", "heart disease", "cancer", "respiratory infections", "kidney disease"],
            "notes": "Nuclear legacy health effects from US testing at Bikini and Enewetak atolls (1946-1958)"
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 27.8,
            "avg_rainfall_mm": 3350,
            "co2_emissions_mt": 0.1,
            "co2_per_capita_t": 2.6,
            "renewable_energy_pct": 5.0,
            "natural_hazards": ["sea level rise", "droughts", "storm surges", "typhoons"],
            "protected_areas_pct": 2.0,
            "paris_agreement_status": "Ratified",
            "notes": "Average elevation 2m; nuclear testing contaminated Bikini and Enewetak atolls"
        },
        "education": {
            "expenditure_pct_gdp": 13.6,
            "primary_enrollment_pct": 84,
            "secondary_enrollment_pct": 58,
            "tertiary_enrollment_pct": 17,
            "mean_years_of_schooling": 10.9,
            "expected_years_of_schooling": 12.4,
            "pisa_participation": False,
            "top_universities": ["College of the Marshall Islands", "USP"],
            "academic_freedom_index": 0.60
        },
        "digital_economy": {
            "e_government_index": 0.37,
            "mobile_money_adoption": "Very limited",
            "tech_hubs": [],
            "cybersecurity_index": 5.0
        },
        "diaspora_migration": {
            "diaspora_population": "30,000",
            "top_destinations": ["United States (Hawaii, Arkansas, Oregon)", "Guam"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "14,000,000",
            "remittances_pct_gdp": 5.5,
            "net_migration_rate": -5.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 25.0,
            "foreign_aid_received_usd": "110,000,000",
            "top_donors": ["United States", "Japan", "Taiwan", "Australia"],
            "notes": "Compact of Free Association renewed 2023; trust fund for post-Compact sustainability"
        }
    },

    "micronesia": {
        "data_year": 2024,
        "demographics": {
            "median_age": 24.7,
            "urbanization_pct": 23.4,
            "fertility_rate": 2.8,
            "life_expectancy": 71.2,
            "life_expectancy_male": 69.2,
            "life_expectancy_female": 73.3,
            "infant_mortality_per_1k": 18.3,
            "under5_mortality_per_1k": 25.0,
            "literacy_rate_pct": 89.0,
            "net_migration_rate": -20.0,
            "population_growth_rate": -0.7,
            "population_density": 158.3,
            "age_structure": {
                "0_14_pct": 27.7,
                "15_24_pct": 18.8,
                "25_54_pct": 37.1,
                "55_64_pct": 8.9,
                "65_plus_pct": 7.5
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 0.5,
            "inflation_pct": 3.5,
            "unemployment_pct": 16.2,
            "poverty_rate_pct": 41.2,
            "sector_agriculture_pct": 26.3,
            "sector_industry_pct": 18.9,
            "sector_services_pct": 54.8,
            "labor_force": 37000
        },
        "natural_resources": {
            "primary": ["fisheries (tuna)", "forests", "deep-sea minerals"],
            "resource_dependency_pct_gdp": 40.0,
            "notes": "Compact of Free Association with US provides ~$110M/year; four states (Yap, Chuuk, Pohnpei, Kosrae)"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Compact of Free Association (USA)", "Pacific Islands Forum"],
            "notes": "US responsible for defense; citizens serve in US military at high rates"
        },
        "trade": {
            "top_exports": ["fish", "copra", "betel nut", "black pepper"],
            "top_imports": ["food", "beverages", "fuel", "clothing"],
            "major_partners": ["United States", "Japan", "Guam"],
            "trade_balance": "Deficit",
            "total_exports_usd": 88000000,
            "total_imports_usd": 190000000,
            "remittances_pct_gdp": 5.0
        },
        "infrastructure": {
            "internet_penetration_pct": 36.0,
            "electricity_access_pct": 75.0,
            "mobile_subscriptions_per_100": 22.0,
            "road_network_km": 388,
            "paved_roads_pct": 18.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 72.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 12.4,
            "health_expenditure_per_capita_usd": 475,
            "physician_density_per_1k": 0.19,
            "maternal_mortality_per_100k": 74,
            "vaccination_coverage_pct": 68,
            "tuberculosis_incidence_per_100k": 87,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 78,
            "sanitation_access_pct": 57,
            "obesity_pct": 45.8,
            "universal_health_coverage_index": 39,
            "leading_causes_of_death": ["diabetes", "heart disease", "cancer", "stroke", "respiratory infections"]
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 27.0,
            "avg_rainfall_mm": 4890,
            "co2_emissions_mt": 0.15,
            "co2_per_capita_t": 1.3,
            "renewable_energy_pct": 10.0,
            "natural_hazards": ["typhoons", "sea level rise", "droughts"],
            "protected_areas_pct": 3.0,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 9.7,
            "primary_enrollment_pct": 80,
            "secondary_enrollment_pct": 60,
            "tertiary_enrollment_pct": 10,
            "mean_years_of_schooling": 8.8,
            "expected_years_of_schooling": 11.5,
            "pisa_participation": False,
            "top_universities": ["College of Micronesia-FSM", "COM-FSM"],
            "academic_freedom_index": 0.55
        },
        "digital_economy": {
            "e_government_index": 0.36,
            "mobile_money_adoption": "Very limited",
            "tech_hubs": [],
            "cybersecurity_index": 4.0
        },
        "diaspora_migration": {
            "diaspora_population": "50,000",
            "top_destinations": ["United States (Hawaii, Guam)", "CNMI"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "20,000,000",
            "remittances_pct_gdp": 5.0,
            "net_migration_rate": -20.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 15.0,
            "foreign_aid_received_usd": "120,000,000",
            "top_donors": ["United States", "Japan", "China"],
            "notes": "Compact of Free Association renewed 2023; trust fund endowment being built"
        }
    },

    "palau": {
        "data_year": 2024,
        "demographics": {
            "median_age": 33.9,
            "urbanization_pct": 81.0,
            "fertility_rate": 1.7,
            "life_expectancy": 74.2,
            "life_expectancy_male": 71.2,
            "life_expectancy_female": 77.4,
            "infant_mortality_per_1k": 10.3,
            "under5_mortality_per_1k": 15.0,
            "literacy_rate_pct": 96.6,
            "net_migration_rate": 0.8,
            "population_growth_rate": 0.4,
            "population_density": 47.0,
            "age_structure": {
                "0_14_pct": 17.5,
                "15_24_pct": 15.4,
                "25_54_pct": 45.3,
                "55_64_pct": 12.5,
                "65_plus_pct": 9.3
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 1.5,
            "inflation_pct": 8.5,
            "unemployment_pct": 1.7,
            "poverty_rate_pct": 24.9,
            "sector_agriculture_pct": 3.0,
            "sector_industry_pct": 20.0,
            "sector_services_pct": 77.0,
            "labor_force": 11000
        },
        "natural_resources": {
            "primary": ["fisheries", "forests", "minerals (gold)", "deep-sea resources"],
            "resource_dependency_pct_gdp": 5.0,
            "notes": "Tourism is primary driver; 80% of marine territory designated as reserve (Palau National Marine Sanctuary)"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Compact of Free Association (USA)", "Pacific Islands Forum"],
            "notes": "US responsible for defense; Palau is nuclear-free but hosts US military access"
        },
        "trade": {
            "top_exports": ["fish", "shellfish", "copra"],
            "top_imports": ["machinery", "fuel", "food", "metal", "beverages"],
            "major_partners": ["Japan", "United States", "Guam", "Taiwan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 7000000,
            "total_imports_usd": 200000000,
            "remittances_pct_gdp": 1.0
        },
        "infrastructure": {
            "internet_penetration_pct": 86.0,
            "electricity_access_pct": 99.0,
            "mobile_subscriptions_per_100": 111.0,
            "road_network_km": 125,
            "paved_roads_pct": 61.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 54.0, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 12.0,
            "health_expenditure_per_capita_usd": 1800,
            "physician_density_per_1k": 1.4,
            "maternal_mortality_per_100k": 0,
            "vaccination_coverage_pct": 85,
            "tuberculosis_incidence_per_100k": 58,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 100,
            "obesity_pct": 55.3,
            "universal_health_coverage_index": 52,
            "leading_causes_of_death": ["diabetes", "heart disease", "cancer", "stroke", "liver disease"],
            "notes": "Highest obesity rate in world region; citizens can access US healthcare"
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 28.0,
            "avg_rainfall_mm": 3800,
            "co2_emissions_mt": 0.25,
            "co2_per_capita_t": 14.0,
            "renewable_energy_pct": 8.0,
            "natural_hazards": ["typhoons", "flooding"],
            "protected_areas_pct": 80.0,
            "paris_agreement_status": "Ratified",
            "notes": "Palau National Marine Sanctuary covers 500,000 km² — one of world's largest marine reserves"
        },
        "education": {
            "expenditure_pct_gdp": 6.8,
            "primary_enrollment_pct": 97,
            "secondary_enrollment_pct": 90,
            "tertiary_enrollment_pct": 30,
            "mean_years_of_schooling": 12.0,
            "expected_years_of_schooling": 16.5,
            "pisa_participation": False,
            "top_universities": ["Palau Community College"],
            "academic_freedom_index": 0.65
        },
        "digital_economy": {
            "e_government_index": 0.53,
            "mobile_money_adoption": "Limited",
            "tech_hubs": [],
            "cybersecurity_index": 12.0
        },
        "diaspora_migration": {
            "diaspora_population": "8,000",
            "top_destinations": ["United States (Guam, Hawaii)", "CNMI"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "2,000,000",
            "remittances_pct_gdp": 0.6,
            "net_migration_rate": 0.8
        },
        "debt_aid": {
            "national_debt_pct_gdp": 22.0,
            "foreign_aid_received_usd": "80,000,000",
            "top_donors": ["United States", "Japan", "Taiwan", "Australia"],
            "notes": "Compact of Free Association renewed 2023; significant US compact grants"
        }
    },

    "nauru": {
        "data_year": 2024,
        "demographics": {
            "median_age": 27.0,
            "urbanization_pct": 100.0,
            "fertility_rate": 2.6,
            "life_expectancy": 68.4,
            "life_expectancy_male": 65.1,
            "life_expectancy_female": 71.9,
            "infant_mortality_per_1k": 7.4,
            "under5_mortality_per_1k": 30.0,
            "literacy_rate_pct": 96.5,
            "net_migration_rate": -9.0,
            "population_growth_rate": 0.4,
            "population_density": 541.0,
            "age_structure": {
                "0_14_pct": 30.0,
                "15_24_pct": 17.6,
                "25_54_pct": 39.2,
                "55_64_pct": 7.5,
                "65_plus_pct": 5.7
            }
        },
        "economy_extended": {
            "gdp_growth_pct": 1.0,
            "inflation_pct": 1.5,
            "unemployment_pct": 23.0,
            "poverty_rate_pct": 24.0,
            "sector_agriculture_pct": 6.1,
            "sector_industry_pct": 33.0,
            "sector_services_pct": 60.9,
            "labor_force": 3500
        },
        "natural_resources": {
            "primary": ["phosphate (largely exhausted)"],
            "resource_dependency_pct_gdp": 5.0,
            "resource_curse_risk": "Realized",
            "notes": "Once world's richest per-capita nation from phosphate; 80% of island strip-mined; Australia detention center revenue now key"
        },
        "military": {
            "budget_usd": 0,
            "pct_of_gdp": 0,
            "active_personnel": 0,
            "nuclear_status": "Non-nuclear",
            "alliances": ["Pacific Islands Forum"],
            "notes": "No military; informal defense agreement with Australia"
        },
        "trade": {
            "top_exports": ["phosphate"],
            "top_imports": ["food", "fuel", "manufactures", "machinery"],
            "major_partners": ["Australia", "Fiji", "India", "Japan"],
            "trade_balance": "Deficit",
            "total_exports_usd": 30000000,
            "total_imports_usd": 90000000,
            "remittances_pct_gdp": 0
        },
        "infrastructure": {
            "internet_penetration_pct": 57.0,
            "electricity_access_pct": 99.0,
            "mobile_subscriptions_per_100": 95.0,
            "road_network_km": 30,
            "paved_roads_pct": 79.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "press_freedom_index": {"rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0},
            "fragile_states_index": {"score": 64.0, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 9.6,
            "health_expenditure_per_capita_usd": 1400,
            "physician_density_per_1k": 1.2,
            "maternal_mortality_per_100k": 0,
            "vaccination_coverage_pct": 90,
            "tuberculosis_incidence_per_100k": 40,
            "hiv_prevalence_pct": 0.0,
            "clean_water_access_pct": 100,
            "sanitation_access_pct": 66,
            "obesity_pct": 61.0,
            "universal_health_coverage_index": 46,
            "leading_causes_of_death": ["diabetes", "heart disease", "kidney disease", "cancer", "respiratory infection"],
            "notes": "World's highest obesity rate (~61%); type 2 diabetes epidemic"
        },
        "climate_environment": {
            "climate_zones": ["tropical marine"],
            "avg_temperature_c": 27.5,
            "avg_rainfall_mm": 2000,
            "co2_emissions_mt": 0.05,
            "co2_per_capita_t": 4.2,
            "renewable_energy_pct": 2.0,
            "natural_hazards": ["droughts", "sea level rise"],
            "protected_areas_pct": 0,
            "paris_agreement_status": "Ratified",
            "notes": "80% of surface mined for phosphate; topsoil rehabilitation ongoing"
        },
        "education": {
            "expenditure_pct_gdp": 8.0,
            "primary_enrollment_pct": 89,
            "secondary_enrollment_pct": 68,
            "tertiary_enrollment_pct": 5,
            "mean_years_of_schooling": 9.0,
            "expected_years_of_schooling": 12.0,
            "pisa_participation": False,
            "top_universities": ["USP Nauru campus"],
            "academic_freedom_index": 0.45
        },
        "digital_economy": {
            "e_government_index": 0.31,
            "mobile_money_adoption": "Very limited",
            "tech_hubs": [],
            "cybersecurity_index": 3.0
        },
        "diaspora_migration": {
            "diaspora_population": "2,000",
            "top_destinations": ["Australia", "New Zealand"],
            "refugees_hosted": 0,
            "refugees_produced": 0,
            "remittances_usd": "0",
            "remittances_pct_gdp": 0,
            "net_migration_rate": -9.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 62.0,
            "foreign_aid_received_usd": "30,000,000",
            "top_donors": ["Australia", "Taiwan", "Japan"],
            "notes": "Hosts Australia's offshore immigration processing centre"
        }
    }
}


def deep_merge(base: dict, overlay: dict) -> dict:
    """Recursively merge overlay into base. Overlay values win for non-dict/non-zero values."""
    result = copy.deepcopy(base)
    for key, value in overlay.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def populate_country(slug: str, data: dict) -> bool:
    """Populate a single country's index.json with provided data."""
    filepath = os.path.join(BASE, slug, "index.json")
    if not os.path.isfile(filepath):
        print(f"  SKIP: {filepath} not found")
        return False

    with open(filepath, "r") as f:
        country = json.load(f)

    # Set data_year on _meta
    if "data_year" in data:
        country.setdefault("_meta", {})["data_year"] = data["data_year"]

    # Merge into country_profile
    profile = country.setdefault("country_profile", {})
    for section in [
        "demographics", "economy_extended", "natural_resources", "military",
        "trade", "infrastructure", "governance_indices", "health",
        "climate_environment", "education", "digital_economy",
        "diaspora_migration", "debt_aid",
    ]:
        if section in data:
            if section in profile and isinstance(profile[section], dict):
                profile[section] = deep_merge(profile[section], data[section])
            else:
                profile[section] = copy.deepcopy(data[section])

    if DRY_RUN:
        print(f"  DRY-RUN: Would update {filepath}")
        return True

    with open(filepath, "w") as f:
        json.dump(country, f, indent=2, ensure_ascii=False)
    print(f"  UPDATED: {filepath}")
    return True


def main():
    print(f"{'DRY RUN — ' if DRY_RUN else ''}Populating {len(OCEANIA_DATA)} Oceania countries...\n")
    success = 0
    for slug, data in sorted(OCEANIA_DATA.items()):
        print(f"Processing: {slug}")
        if populate_country(slug, data):
            success += 1
    print(f"\nDone. {success}/{len(OCEANIA_DATA)} countries {'would be ' if DRY_RUN else ''}updated.")


if __name__ == "__main__":
    main()
