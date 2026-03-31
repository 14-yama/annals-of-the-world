#!/usr/bin/env python3
"""
Populate demographics, economy, health, governance, military, trade,
infrastructure, climate, education, and digital economy data for all
35 Americas countries in the geo-registry.

Sources: World Bank, CIA World Factbook, UNDP, WHO, ITU (2023–2024 data).

Usage:
    python3 geo-registry/scripts/populate_americas.py          # live run
    python3 geo-registry/scripts/populate_americas.py --dry-run # preview only
"""
import json
import os
import sys
import copy

DRY_RUN = "--dry-run" in sys.argv
BASE = os.path.join(os.path.dirname(__file__), "..", "places", "countries")


def deep_merge(base: dict, overlay: dict) -> dict:
    result = copy.deepcopy(base)
    for key, value in overlay.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def populate_country(slug: str, data: dict) -> bool:
    filepath = os.path.join(BASE, slug, "index.json")
    if not os.path.isfile(filepath):
        print(f"  SKIP: {filepath} not found")
        return False
    with open(filepath, "r") as f:
        country = json.load(f)
    if "data_year" in data:
        country.setdefault("_meta", {})["data_year"] = data["data_year"]
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


AMERICAS_DATA = {
    "united-states": {
        "data_year": 2024,
        "demographics": {
            "median_age": 38.9, "urbanization_pct": 83.3, "fertility_rate": 1.66,
            "life_expectancy": 79.1, "life_expectancy_male": 76.3, "life_expectancy_female": 81.7,
            "infant_mortality_per_1k": 5.4, "under5_mortality_per_1k": 6.5, "literacy_rate_pct": 99.0,
            "net_migration_rate": 3.0, "population_growth_rate": 0.5, "population_density": 36.2,
            "age_structure": {"0_14_pct": 18.0, "15_24_pct": 13.0, "25_54_pct": 38.7, "55_64_pct": 12.9, "65_plus_pct": 17.4}
        },
        "economy_extended": {
            "gdp_growth_pct": 2.5, "inflation_pct": 3.4, "unemployment_pct": 3.7, "poverty_rate_pct": 11.5,
            "gini_index": 39.8, "sector_agriculture_pct": 0.9, "sector_industry_pct": 18.9, "sector_services_pct": 80.2,
            "labor_force": 164000000, "fdi_inflow_usd": 285000000000,
            "ease_of_doing_business_rank": 6, "economic_freedom_index_score": 70.6,
            "credit_ratings": "AA+ (S&P), Aaa (Moody's)"
        },
        "natural_resources": {
            "primary": ["coal", "copper", "lead", "molybdenum", "phosphates", "rare earths", "uranium", "bauxite", "gold", "iron", "mercury", "nickel", "potash", "silver", "tungsten", "zinc", "petroleum", "natural gas", "timber"],
            "resource_dependency_pct_gdp": 1.5, "resource_curse_risk": "Low",
            "notes": "World's largest natural gas producer and 2nd largest oil producer"
        },
        "military": {
            "budget_usd": 886000000000, "pct_of_gdp": 3.4, "active_personnel": 1390000,
            "reserve_personnel": 799500, "nuclear_status": "Nuclear weapon state",
            "alliances": ["NATO", "Five Eyes", "AUKUS", "QUAD", "OAS"],
            "conscription": False, "global_firepower_rank": 1
        },
        "trade": {
            "top_exports": ["refined petroleum", "aircraft", "vehicles", "integrated circuits", "soybeans", "natural gas", "pharmaceuticals"],
            "top_imports": ["crude petroleum", "vehicles", "computers", "broadcasting equipment", "pharmaceuticals"],
            "major_partners": ["Canada", "Mexico", "China", "Japan", "Germany"],
            "trade_balance": "Deficit", "total_exports_usd": 2020000000000, "total_imports_usd": 3170000000000,
            "trade_as_pct_gdp": 25.6, "trade_agreements": ["USMCA", "KORUS FTA", "CAFTA-DR"]
        },
        "infrastructure": {
            "internet_penetration_pct": 92.0, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 110.0, "5g_coverage_pct": 50.0,
            "railway_km": 293564, "road_network_km": 6586610, "paved_roads_pct": 67.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 69, "rank": 24, "year": 2023},
            "press_freedom_index": {"rank": 55, "year": 2024},
            "democracy_index": {"score": 7.85, "category": "Flawed democracy", "year": 2023},
            "fragile_states_index": {"score": 38.7, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 17.8, "health_expenditure_per_capita_usd": 12555,
            "physician_density_per_1k": 2.6, "hospital_beds_per_1k": 2.9,
            "maternal_mortality_per_100k": 21, "vaccination_coverage_pct": 92,
            "obesity_pct": 42.4, "universal_health_coverage_index": 84,
            "leading_causes_of_death": ["heart disease", "cancer", "COVID-19", "accidents", "stroke"]
        },
        "climate_environment": {
            "climate_zones": ["temperate", "continental", "arid", "tropical", "arctic"],
            "co2_emissions_mt": 4853, "co2_per_capita_t": 14.4, "renewable_energy_pct": 21.3,
            "natural_hazards": ["hurricanes", "tornadoes", "earthquakes", "wildfires", "floods"],
            "protected_areas_pct": 26.0, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 6.0, "primary_enrollment_pct": 99, "tertiary_enrollment_pct": 88,
            "mean_years_of_schooling": 13.7, "pisa_participation": True,
            "pisa_scores": {"reading": 504, "math": 465, "science": 499},
            "top_universities": ["MIT", "Stanford", "Harvard", "Caltech", "UChicago", "Princeton"]
        },
        "digital_economy": {
            "e_government_index": 0.92, "fintech_companies": 10000,
            "tech_hubs": ["Silicon Valley", "New York", "Austin", "Seattle", "Boston"],
            "startup_ecosystem_value": 4500000000000, "cybersecurity_index": 100.0, "innovation_index": 3
        },
        "diaspora_migration": {
            "diaspora_population": "3,000,000", "refugees_hosted": 1160000,
            "net_migration_rate": 3.0
        },
        "debt_aid": {
            "national_debt_pct_gdp": 123.3, "foreign_aid_given_usd": "49,000,000,000"
        }
    },

    "canada": {
        "data_year": 2024,
        "demographics": {
            "median_age": 41.8, "urbanization_pct": 81.8, "fertility_rate": 1.33,
            "life_expectancy": 82.7, "life_expectancy_male": 80.6, "life_expectancy_female": 84.7,
            "infant_mortality_per_1k": 4.3, "literacy_rate_pct": 99.0,
            "net_migration_rate": 6.3, "population_growth_rate": 2.7, "population_density": 4.2,
            "age_structure": {"0_14_pct": 15.3, "15_24_pct": 10.8, "25_54_pct": 39.2, "55_64_pct": 14.4, "65_plus_pct": 20.3}
        },
        "economy_extended": {
            "gdp_growth_pct": 1.1, "inflation_pct": 3.9, "unemployment_pct": 5.4, "poverty_rate_pct": 6.4,
            "gini_index": 31.7, "sector_agriculture_pct": 1.6, "sector_industry_pct": 24.4, "sector_services_pct": 74.0,
            "labor_force": 21500000, "fdi_inflow_usd": 37000000000,
            "ease_of_doing_business_rank": 23, "economic_freedom_index_score": 73.7,
            "credit_ratings": "AAA (S&P, Moody's)"
        },
        "natural_resources": {
            "primary": ["oil sands", "natural gas", "potash", "uranium", "gold", "nickel", "zinc", "hydropower", "timber", "iron ore", "coal", "diamonds"],
            "resource_dependency_pct_gdp": 11.0, "resource_curse_risk": "Low",
            "notes": "3rd largest proven oil reserves (oil sands); world's largest potash producer"
        },
        "military": {
            "budget_usd": 26900000000, "pct_of_gdp": 1.3, "active_personnel": 72000,
            "reserve_personnel": 30000, "nuclear_status": "Non-nuclear (NATO nuclear sharing)",
            "alliances": ["NATO", "Five Eyes", "NORAD", "OAS"], "conscription": False,
            "global_firepower_rank": 27
        },
        "trade": {
            "top_exports": ["crude petroleum", "vehicles", "gold", "natural gas", "lumber"],
            "top_imports": ["vehicles", "machinery", "crude petroleum", "electronics"],
            "major_partners": ["United States", "China", "Mexico", "Japan", "Germany"],
            "trade_balance": "Deficit", "total_exports_usd": 597000000000, "total_imports_usd": 608000000000,
            "trade_as_pct_gdp": 66.8, "trade_agreements": ["USMCA", "CPTPP", "CETA"]
        },
        "infrastructure": {
            "internet_penetration_pct": 97.0, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 93.5, "railway_km": 42951,
            "road_network_km": 1042300, "paved_roads_pct": 40.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 76, "rank": 12, "year": 2023},
            "press_freedom_index": {"rank": 14, "year": 2024},
            "democracy_index": {"score": 8.88, "category": "Full democracy", "year": 2023},
            "fragile_states_index": {"score": 20.8, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 12.2, "physician_density_per_1k": 2.7,
            "maternal_mortality_per_100k": 11, "vaccination_coverage_pct": 92,
            "obesity_pct": 29.4, "universal_health_coverage_index": 89,
            "leading_causes_of_death": ["cancer", "heart disease", "COVID-19", "accidents", "stroke"]
        },
        "climate_environment": {
            "climate_zones": ["arctic", "subarctic", "continental", "maritime"],
            "co2_emissions_mt": 556, "co2_per_capita_t": 14.2, "renewable_energy_pct": 68.5,
            "natural_hazards": ["blizzards", "ice storms", "floods", "wildfires"],
            "protected_areas_pct": 12.5, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 5.3, "tertiary_enrollment_pct": 75,
            "mean_years_of_schooling": 13.8, "pisa_participation": True,
            "pisa_scores": {"reading": 507, "math": 497, "science": 515},
            "top_universities": ["University of Toronto", "McGill", "UBC", "University of Waterloo"]
        },
        "digital_economy": {
            "e_government_index": 0.94, "fintech_companies": 900,
            "tech_hubs": ["Toronto", "Vancouver", "Montreal", "Waterloo"],
            "startup_ecosystem_value": 100000000000, "cybersecurity_index": 96.4, "innovation_index": 15
        },
        "diaspora_migration": {
            "diaspora_population": "1,600,000", "refugees_hosted": 168000,
            "net_migration_rate": 6.3
        },
        "debt_aid": {
            "national_debt_pct_gdp": 106.4, "foreign_aid_given_usd": "6,300,000,000"
        }
    },

    "mexico": {
        "data_year": 2024,
        "demographics": {
            "median_age": 29.3, "urbanization_pct": 81.6, "fertility_rate": 1.83,
            "life_expectancy": 75.1, "life_expectancy_male": 72.0, "life_expectancy_female": 78.1,
            "infant_mortality_per_1k": 11.6, "literacy_rate_pct": 95.2,
            "net_migration_rate": -1.0, "population_growth_rate": 0.6, "population_density": 67.0,
            "age_structure": {"0_14_pct": 25.0, "15_24_pct": 16.5, "25_54_pct": 41.1, "55_64_pct": 8.9, "65_plus_pct": 8.5}
        },
        "economy_extended": {
            "gdp_growth_pct": 3.2, "inflation_pct": 5.5, "unemployment_pct": 2.8, "poverty_rate_pct": 36.3,
            "gini_index": 45.4, "sector_agriculture_pct": 3.6, "sector_industry_pct": 31.0, "sector_services_pct": 65.4,
            "labor_force": 59200000, "fdi_inflow_usd": 36000000000,
            "ease_of_doing_business_rank": 60, "credit_ratings": "BBB (S&P)"
        },
        "natural_resources": {
            "primary": ["petroleum", "silver", "copper", "gold", "lead", "zinc", "natural gas", "timber"],
            "resource_dependency_pct_gdp": 3.8, "notes": "World's largest silver producer; nearshoring boom driving manufacturing growth"
        },
        "military": {
            "budget_usd": 11400000000, "pct_of_gdp": 0.6, "active_personnel": 277000,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS"],
            "conscription": True, "global_firepower_rank": 31,
            "notes": "National Guard (115k) focuses on internal security/cartel operations"
        },
        "trade": {
            "top_exports": ["vehicles", "electronics", "machinery", "crude petroleum", "medical instruments", "avocados"],
            "top_imports": ["refined petroleum", "vehicle parts", "integrated circuits", "natural gas"],
            "major_partners": ["United States", "China", "Germany", "Japan", "South Korea"],
            "trade_balance": "Surplus", "total_exports_usd": 593000000000, "total_imports_usd": 580000000000,
            "trade_as_pct_gdp": 78.9, "trade_agreements": ["USMCA", "CPTPP", "Pacific Alliance"]
        },
        "infrastructure": {
            "internet_penetration_pct": 77.7, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 98.2, "railway_km": 23389,
            "road_network_km": 398148, "paved_roads_pct": 36.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 31, "rank": 126, "year": 2023},
            "press_freedom_index": {"rank": 121, "year": 2024},
            "democracy_index": {"score": 5.57, "category": "Hybrid regime", "year": 2023},
            "fragile_states_index": {"score": 65.7, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 5.4, "physician_density_per_1k": 2.4,
            "maternal_mortality_per_100k": 59, "vaccination_coverage_pct": 79,
            "obesity_pct": 28.9, "universal_health_coverage_index": 75,
            "leading_causes_of_death": ["heart disease", "diabetes", "COVID-19", "cancer", "liver disease"]
        },
        "climate_environment": {
            "climate_zones": ["tropical", "arid", "temperate"],
            "co2_emissions_mt": 410, "co2_per_capita_t": 3.2, "renewable_energy_pct": 23.0,
            "natural_hazards": ["earthquakes", "hurricanes", "volcanic eruptions", "floods"],
            "protected_areas_pct": 14.8, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 4.3, "tertiary_enrollment_pct": 40,
            "mean_years_of_schooling": 8.7, "pisa_participation": True,
            "pisa_scores": {"reading": 415, "math": 395, "science": 410},
            "top_universities": ["UNAM", "Monterrey Tech", "IPN", "UAM"]
        },
        "digital_economy": {
            "e_government_index": 0.75, "fintech_companies": 650,
            "tech_hubs": ["Mexico City", "Guadalajara", "Monterrey"],
            "startup_ecosystem_value": 12000000000, "innovation_index": 58
        },
        "diaspora_migration": {
            "diaspora_population": "12,000,000", "remittances_usd": "63,000,000,000",
            "remittances_pct_gdp": 3.8, "net_migration_rate": -1.0
        },
        "debt_aid": {"national_debt_pct_gdp": 49.4}
    },

    "brazil": {
        "data_year": 2024,
        "demographics": {
            "median_age": 34.3, "urbanization_pct": 87.6, "fertility_rate": 1.65,
            "life_expectancy": 76.4, "life_expectancy_male": 72.9, "life_expectancy_female": 80.0,
            "infant_mortality_per_1k": 12.4, "literacy_rate_pct": 93.2,
            "net_migration_rate": 0.1, "population_growth_rate": 0.5, "population_density": 25.5,
            "age_structure": {"0_14_pct": 19.8, "15_24_pct": 14.8, "25_54_pct": 43.2, "55_64_pct": 11.0, "65_plus_pct": 11.2}
        },
        "economy_extended": {
            "gdp_growth_pct": 2.9, "inflation_pct": 4.6, "unemployment_pct": 7.8, "poverty_rate_pct": 4.6,
            "gini_index": 52.9, "sector_agriculture_pct": 6.6, "sector_industry_pct": 20.7, "sector_services_pct": 72.7,
            "labor_force": 107000000, "fdi_inflow_usd": 66000000000,
            "ease_of_doing_business_rank": 124, "credit_ratings": "BB (S&P)"
        },
        "natural_resources": {
            "primary": ["iron ore", "manganese", "bauxite", "nickel", "uranium", "gemstones", "petroleum", "hydropower", "timber", "niobium"],
            "resource_dependency_pct_gdp": 8.0, "notes": "World's largest niobium producer; pre-salt oil reserves; Amazon contains 10% of world's species"
        },
        "military": {
            "budget_usd": 20000000000, "pct_of_gdp": 1.1, "active_personnel": 360000,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS", "MERCOSUR", "BRICS"],
            "global_firepower_rank": 12
        },
        "trade": {
            "top_exports": ["soybeans", "iron ore", "crude petroleum", "sugar", "poultry", "corn", "coffee", "beef"],
            "top_imports": ["refined petroleum", "vehicle parts", "electronics", "natural gas", "pharmaceuticals"],
            "major_partners": ["China", "United States", "Argentina", "Netherlands", "Germany"],
            "trade_balance": "Surplus", "total_exports_usd": 340000000000, "total_imports_usd": 271000000000,
            "trade_as_pct_gdp": 31.5, "trade_agreements": ["MERCOSUR", "BRICS"]
        },
        "infrastructure": {
            "internet_penetration_pct": 84.4, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 100.6, "railway_km": 29850,
            "road_network_km": 1721000, "paved_roads_pct": 12.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 36, "rank": 104, "year": 2023},
            "press_freedom_index": {"rank": 82, "year": 2024},
            "democracy_index": {"score": 6.68, "category": "Flawed democracy", "year": 2023},
            "fragile_states_index": {"score": 58.1, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 9.9, "physician_density_per_1k": 2.3,
            "maternal_mortality_per_100k": 72, "vaccination_coverage_pct": 80,
            "obesity_pct": 22.1, "universal_health_coverage_index": 75,
            "leading_causes_of_death": ["heart disease", "stroke", "cancer", "diabetes", "violence"]
        },
        "climate_environment": {
            "climate_zones": ["tropical", "subtropical", "semi-arid", "equatorial"],
            "co2_emissions_mt": 476, "co2_per_capita_t": 2.2, "renewable_energy_pct": 83.0,
            "natural_hazards": ["droughts", "floods", "frost"],
            "protected_areas_pct": 30.4, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 6.1, "tertiary_enrollment_pct": 55,
            "mean_years_of_schooling": 8.1, "pisa_participation": True,
            "pisa_scores": {"reading": 410, "math": 379, "science": 403},
            "top_universities": ["USP", "UNICAMP", "UFRJ", "UNESP"]
        },
        "digital_economy": {
            "e_government_index": 0.82, "fintech_companies": 1300,
            "tech_hubs": ["São Paulo", "Florianópolis", "Recife", "Belo Horizonte"],
            "startup_ecosystem_value": 55000000000, "innovation_index": 49
        },
        "diaspora_migration": {
            "diaspora_population": "4,500,000", "remittances_usd": "6,000,000,000",
            "remittances_pct_gdp": 0.3, "net_migration_rate": 0.1
        },
        "debt_aid": {"national_debt_pct_gdp": 74.4}
    },

    "argentina": {
        "data_year": 2024,
        "demographics": {
            "median_age": 32.4, "urbanization_pct": 92.2, "fertility_rate": 1.89,
            "life_expectancy": 77.5, "life_expectancy_male": 74.5, "life_expectancy_female": 80.6,
            "infant_mortality_per_1k": 8.5, "literacy_rate_pct": 99.0,
            "net_migration_rate": -0.1, "population_growth_rate": 0.8, "population_density": 16.6,
            "age_structure": {"0_14_pct": 23.5, "15_24_pct": 15.0, "25_54_pct": 39.2, "55_64_pct": 10.9, "65_plus_pct": 11.4}
        },
        "economy_extended": {
            "gdp_growth_pct": -1.6, "inflation_pct": 211.4, "unemployment_pct": 6.2, "poverty_rate_pct": 40.1,
            "gini_index": 42.3, "sector_agriculture_pct": 6.5, "sector_industry_pct": 23.7, "sector_services_pct": 69.8,
            "labor_force": 21000000, "credit_ratings": "CCC (S&P)"
        },
        "natural_resources": {
            "primary": ["fertile farmland", "lead", "zinc", "tin", "copper", "iron ore", "manganese", "petroleum", "uranium", "lithium"],
            "notes": "Vaca Muerta shale formation is world's 2nd largest; key lithium triangle player"
        },
        "military": {
            "budget_usd": 5200000000, "pct_of_gdp": 0.6, "active_personnel": 80000,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS", "MERCOSUR"], "global_firepower_rank": 40
        },
        "trade": {
            "top_exports": ["soybean meal", "corn", "vehicles", "petroleum", "wheat", "beef"],
            "top_imports": ["vehicles", "natural gas", "soybeans", "machinery"],
            "major_partners": ["Brazil", "China", "United States", "Chile"],
            "trade_balance": "Surplus", "total_exports_usd": 83000000000, "total_imports_usd": 73000000000,
            "trade_agreements": ["MERCOSUR"]
        },
        "infrastructure": {
            "internet_penetration_pct": 87.1, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 130.0, "railway_km": 36917,
            "road_network_km": 281290, "paved_roads_pct": 23.0
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 37, "rank": 98, "year": 2023},
            "press_freedom_index": {"rank": 66, "year": 2024},
            "democracy_index": {"score": 6.85, "category": "Flawed democracy", "year": 2023},
            "fragile_states_index": {"score": 45.9, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 10.0, "physician_density_per_1k": 4.0,
            "maternal_mortality_per_100k": 39, "vaccination_coverage_pct": 85,
            "obesity_pct": 28.3, "universal_health_coverage_index": 79,
            "leading_causes_of_death": ["heart disease", "cancer", "stroke", "respiratory diseases", "diabetes"]
        },
        "climate_environment": {
            "climate_zones": ["temperate", "subtropical", "arid", "subpolar"],
            "co2_emissions_mt": 166, "co2_per_capita_t": 3.6, "renewable_energy_pct": 27.0,
            "natural_hazards": ["floods", "droughts", "earthquakes"],
            "protected_areas_pct": 8.8, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 5.0, "tertiary_enrollment_pct": 90,
            "mean_years_of_schooling": 11.1, "pisa_participation": True,
            "pisa_scores": {"reading": 401, "math": 378, "science": 406},
            "top_universities": ["University of Buenos Aires", "ITBA", "Universidad de La Plata"]
        },
        "digital_economy": {
            "e_government_index": 0.80, "fintech_companies": 350,
            "tech_hubs": ["Buenos Aires", "Córdoba", "Rosario"],
            "innovation_index": 73
        },
        "diaspora_migration": {
            "diaspora_population": "1,000,000", "remittances_usd": "1,000,000,000", "net_migration_rate": -0.1
        },
        "debt_aid": {"national_debt_pct_gdp": 89.4}
    },

    "colombia": {
        "data_year": 2024,
        "demographics": {
            "median_age": 32.2, "urbanization_pct": 82.0, "fertility_rate": 1.72,
            "life_expectancy": 77.5, "life_expectancy_male": 74.4, "life_expectancy_female": 80.7,
            "infant_mortality_per_1k": 11.0, "literacy_rate_pct": 95.6,
            "net_migration_rate": -0.6, "population_growth_rate": 0.5, "population_density": 46.0,
            "age_structure": {"0_14_pct": 22.0, "15_24_pct": 15.8, "25_54_pct": 42.2, "55_64_pct": 10.3, "65_plus_pct": 9.7}
        },
        "economy_extended": {
            "gdp_growth_pct": 0.6, "inflation_pct": 11.8, "unemployment_pct": 10.2, "poverty_rate_pct": 33.0,
            "gini_index": 51.3, "sector_agriculture_pct": 7.0, "sector_industry_pct": 25.2, "sector_services_pct": 67.8,
            "labor_force": 25800000, "credit_ratings": "BB+ (S&P)"
        },
        "natural_resources": {
            "primary": ["petroleum", "coal", "nickel", "gold", "silver", "copper", "platinum", "emeralds", "hydropower"],
            "notes": "World's largest emerald producer; 2nd most biodiverse country on Earth"
        },
        "military": {
            "budget_usd": 10500000000, "pct_of_gdp": 3.2, "active_personnel": 295000,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS", "Pacific Alliance"],
            "global_firepower_rank": 43, "notes": "Decades of counter-insurgency experience (FARC peace deal 2016)"
        },
        "trade": {
            "top_exports": ["crude petroleum", "coal", "coffee", "gold", "flowers", "bananas"],
            "top_imports": ["refined petroleum", "vehicles", "machinery", "pharmaceuticals"],
            "major_partners": ["United States", "China", "Panama", "Ecuador", "Brazil"],
            "trade_balance": "Deficit", "total_exports_usd": 57000000000, "total_imports_usd": 66000000000,
            "trade_agreements": ["Pacific Alliance", "CAFTA-DR"]
        },
        "infrastructure": {
            "internet_penetration_pct": 73.0, "electricity_access_pct": 99.8,
            "mobile_subscriptions_per_100": 133.5, "railway_km": 1663
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 40, "rank": 87, "year": 2023},
            "press_freedom_index": {"rank": 119, "year": 2024},
            "democracy_index": {"score": 7.04, "category": "Flawed democracy", "year": 2023},
            "fragile_states_index": {"score": 66.7, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 7.7, "physician_density_per_1k": 2.2,
            "maternal_mortality_per_100k": 75, "vaccination_coverage_pct": 88,
            "obesity_pct": 22.3, "universal_health_coverage_index": 76,
            "leading_causes_of_death": ["heart disease", "stroke", "cancer", "COPD", "violence"]
        },
        "climate_environment": {
            "climate_zones": ["tropical", "equatorial", "highland"],
            "co2_emissions_mt": 85, "co2_per_capita_t": 1.6, "renewable_energy_pct": 72.0,
            "natural_hazards": ["volcanic eruptions", "earthquakes", "floods", "mudslides"],
            "protected_areas_pct": 15.0, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 4.9, "tertiary_enrollment_pct": 55,
            "mean_years_of_schooling": 8.9, "pisa_participation": True,
            "top_universities": ["Universidad de los Andes", "Universidad Nacional", "Javeriana"]
        },
        "digital_economy": {
            "e_government_index": 0.79, "fintech_companies": 300,
            "tech_hubs": ["Bogotá", "Medellín", "Barranquilla"],
            "startup_ecosystem_value": 7000000000, "innovation_index": 66
        },
        "diaspora_migration": {
            "diaspora_population": "5,000,000", "remittances_usd": "10,000,000,000",
            "remittances_pct_gdp": 2.7, "refugees_hosted": 2900000
        },
        "debt_aid": {"national_debt_pct_gdp": 51.8}
    },

    "chile": {
        "data_year": 2024,
        "demographics": {
            "median_age": 35.5, "urbanization_pct": 88.0, "fertility_rate": 1.54,
            "life_expectancy": 80.2, "life_expectancy_male": 77.6, "life_expectancy_female": 82.8,
            "infant_mortality_per_1k": 5.9, "literacy_rate_pct": 97.0,
            "net_migration_rate": 2.5, "population_growth_rate": 0.6, "population_density": 26.0,
            "age_structure": {"0_14_pct": 18.8, "15_24_pct": 13.5, "25_54_pct": 41.9, "55_64_pct": 12.5, "65_plus_pct": 13.3}
        },
        "economy_extended": {
            "gdp_growth_pct": 0.2, "inflation_pct": 7.6, "unemployment_pct": 8.5, "poverty_rate_pct": 6.5,
            "gini_index": 44.9, "sector_agriculture_pct": 3.3, "sector_industry_pct": 30.8, "sector_services_pct": 65.9,
            "labor_force": 9500000, "credit_ratings": "A (S&P)"
        },
        "natural_resources": {
            "primary": ["copper", "lithium", "timber", "iron ore", "nitrates", "molybdenum", "hydropower"],
            "notes": "World's #1 copper producer; #2 lithium producer; mining = 10% GDP"
        },
        "military": {
            "budget_usd": 5700000000, "pct_of_gdp": 1.9, "active_personnel": 80600,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS", "Pacific Alliance"],
            "global_firepower_rank": 56
        },
        "trade": {
            "top_exports": ["copper", "lithium", "cherries", "salmon", "wine", "wood pulp"],
            "top_imports": ["refined petroleum", "vehicles", "natural gas", "machinery"],
            "major_partners": ["China", "United States", "Japan", "South Korea", "Brazil"],
            "trade_balance": "Surplus", "total_exports_usd": 97000000000, "total_imports_usd": 86000000000,
            "trade_agreements": ["CPTPP", "Pacific Alliance", "Chile-US FTA", "Chile-EU FTA"]
        },
        "infrastructure": {
            "internet_penetration_pct": 92.0, "electricity_access_pct": 100.0,
            "mobile_subscriptions_per_100": 138.0, "railway_km": 7282
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 66, "rank": 29, "year": 2023},
            "press_freedom_index": {"rank": 52, "year": 2024},
            "democracy_index": {"score": 8.01, "category": "Full democracy", "year": 2023},
            "fragile_states_index": {"score": 32.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 9.3, "physician_density_per_1k": 2.6,
            "maternal_mortality_per_100k": 15, "vaccination_coverage_pct": 92,
            "obesity_pct": 28.8, "universal_health_coverage_index": 80
        },
        "climate_environment": {
            "climate_zones": ["desert", "Mediterranean", "oceanic", "tundra"],
            "co2_emissions_mt": 81, "co2_per_capita_t": 4.2, "renewable_energy_pct": 49.0,
            "natural_hazards": ["earthquakes", "volcanic eruptions", "tsunamis"],
            "protected_areas_pct": 21.0, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 5.6, "tertiary_enrollment_pct": 90,
            "mean_years_of_schooling": 10.6, "pisa_participation": True,
            "pisa_scores": {"reading": 448, "math": 412, "science": 444},
            "top_universities": ["PUC Chile", "Universidad de Chile", "Universidad de Concepción"]
        },
        "digital_economy": {
            "e_government_index": 0.83, "fintech_companies": 200,
            "tech_hubs": ["Santiago"], "innovation_index": 52
        },
        "diaspora_migration": {
            "diaspora_population": "1,100,000", "remittances_usd": "600,000,000", "net_migration_rate": 2.5
        },
        "debt_aid": {"national_debt_pct_gdp": 38.3}
    },

    "peru": {
        "data_year": 2024,
        "demographics": {
            "median_age": 29.1, "urbanization_pct": 78.7, "fertility_rate": 2.17,
            "life_expectancy": 76.7, "infant_mortality_per_1k": 12.3, "literacy_rate_pct": 94.5,
            "net_migration_rate": 1.0, "population_growth_rate": 0.8, "population_density": 26.0,
            "age_structure": {"0_14_pct": 24.5, "15_24_pct": 17.0, "25_54_pct": 41.2, "55_64_pct": 8.8, "65_plus_pct": 8.5}
        },
        "economy_extended": {
            "gdp_growth_pct": -0.6, "inflation_pct": 6.3, "unemployment_pct": 7.6, "poverty_rate_pct": 27.5,
            "gini_index": 43.8, "sector_agriculture_pct": 7.2, "sector_industry_pct": 32.0, "sector_services_pct": 60.8,
            "labor_force": 18700000, "credit_ratings": "BBB (S&P)"
        },
        "natural_resources": {
            "primary": ["copper", "silver", "gold", "petroleum", "timber", "iron ore", "natural gas", "zinc", "lead"],
            "notes": "World's #2 copper and silver producer; rich marine resources from Humboldt Current"
        },
        "military": {
            "budget_usd": 2900000000, "pct_of_gdp": 1.1, "active_personnel": 95000,
            "nuclear_status": "Non-nuclear", "alliances": ["OAS", "Pacific Alliance"],
            "global_firepower_rank": 44
        },
        "trade": {
            "top_exports": ["copper", "gold", "zinc", "petroleum", "coffee", "asparagus"],
            "top_imports": ["petroleum", "vehicles", "machinery", "wheat", "soybeans"],
            "major_partners": ["China", "United States", "Canada", "South Korea", "Brazil"],
            "trade_balance": "Surplus", "total_exports_usd": 59000000000, "total_imports_usd": 50000000000,
            "trade_agreements": ["CPTPP", "Pacific Alliance"]
        },
        "infrastructure": {
            "internet_penetration_pct": 71.1, "electricity_access_pct": 96.0,
            "mobile_subscriptions_per_100": 110.0, "railway_km": 1854
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 33, "rank": 121, "year": 2023},
            "democracy_index": {"score": 5.93, "category": "Hybrid regime", "year": 2023},
            "fragile_states_index": {"score": 60.3, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 5.2, "physician_density_per_1k": 1.3,
            "maternal_mortality_per_100k": 69, "vaccination_coverage_pct": 80,
            "obesity_pct": 21.0, "universal_health_coverage_index": 64
        },
        "climate_environment": {
            "climate_zones": ["tropical", "arid", "highland", "temperate"],
            "co2_emissions_mt": 58, "co2_per_capita_t": 1.7, "renewable_energy_pct": 61.0,
            "natural_hazards": ["earthquakes", "tsunamis", "El Niño floods", "landslides"],
            "protected_areas_pct": 18.2, "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 4.0, "tertiary_enrollment_pct": 40,
            "mean_years_of_schooling": 9.2, "pisa_participation": True,
            "top_universities": ["PUCP", "Universidad Nacional Mayor de San Marcos", "Universidad de Lima"]
        },
        "digital_economy": {
            "e_government_index": 0.72, "fintech_companies": 150,
            "tech_hubs": ["Lima"], "innovation_index": 76
        },
        "diaspora_migration": {
            "diaspora_population": "3,500,000", "remittances_usd": "4,000,000,000",
            "remittances_pct_gdp": 1.5
        },
        "debt_aid": {"national_debt_pct_gdp": 34.0}
    },

    "venezuela": {
        "data_year": 2024,
        "demographics": {
            "median_age": 30.0, "urbanization_pct": 88.3, "fertility_rate": 2.23,
            "life_expectancy": 72.1, "infant_mortality_per_1k": 14.2, "literacy_rate_pct": 97.1,
            "net_migration_rate": -7.0, "population_growth_rate": -0.8, "population_density": 32.0,
            "age_structure": {"0_14_pct": 25.0, "15_24_pct": 16.4, "25_54_pct": 41.5, "55_64_pct": 9.1, "65_plus_pct": 8.0}
        },
        "economy_extended": {
            "gdp_growth_pct": 5.0, "inflation_pct": 230.0, "unemployment_pct": 50.0, "poverty_rate_pct": 94.5,
            "sector_agriculture_pct": 4.7, "sector_industry_pct": 40.4, "sector_services_pct": 54.9
        },
        "natural_resources": {
            "primary": ["petroleum", "natural gas", "iron ore", "gold", "bauxite", "diamonds"],
            "notes": "World's largest proven oil reserves; economic collapse since 2014; hyperinflation"
        },
        "military": {
            "budget_usd": 500000000, "pct_of_gdp": 0.5, "active_personnel": 343000,
            "nuclear_status": "Non-nuclear", "global_firepower_rank": 55
        },
        "trade": {
            "top_exports": ["crude petroleum", "gold", "iron"],
            "top_imports": ["refined petroleum", "food", "medicine"],
            "major_partners": ["China", "India", "Turkey", "Colombia"],
            "trade_balance": "Surplus"
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 13, "rank": 177, "year": 2023},
            "democracy_index": {"score": 2.06, "category": "Authoritarian", "year": 2023},
            "fragile_states_index": {"score": 88.1, "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 3.8, "physician_density_per_1k": 1.7,
            "maternal_mortality_per_100k": 125, "obesity_pct": 25.6, "universal_health_coverage_index": 65
        },
        "climate_environment": {
            "climate_zones": ["tropical"], "co2_emissions_mt": 91, "co2_per_capita_t": 3.3,
            "paris_agreement_status": "Ratified"
        },
        "education": {
            "expenditure_pct_gdp": 1.3, "tertiary_enrollment_pct": 50,
            "mean_years_of_schooling": 10.3,
            "top_universities": ["UCV", "Simón Bolívar", "Universidad de Los Andes"]
        },
        "diaspora_migration": {
            "diaspora_population": "7,700,000", "remittances_usd": "3,500,000,000",
            "net_migration_rate": -7.0, "notes": "Largest refugee crisis in Western Hemisphere"
        },
        "debt_aid": {"national_debt_pct_gdp": 350.0}
    },

    "ecuador": {
        "data_year": 2024,
        "demographics": {
            "median_age": 28.7, "urbanization_pct": 64.4, "fertility_rate": 2.28,
            "life_expectancy": 77.6, "infant_mortality_per_1k": 11.2, "literacy_rate_pct": 93.6,
            "net_migration_rate": -1.2, "population_growth_rate": 1.0, "population_density": 72.4,
            "age_structure": {"0_14_pct": 24.5, "15_24_pct": 16.8, "25_54_pct": 41.8, "55_64_pct": 8.7, "65_plus_pct": 8.2}
        },
        "economy_extended": {
            "gdp_growth_pct": 2.4, "inflation_pct": 2.2, "unemployment_pct": 3.6, "poverty_rate_pct": 25.0,
            "gini_index": 45.7, "sector_agriculture_pct": 9.5, "sector_industry_pct": 30.0, "sector_services_pct": 60.5,
            "labor_force": 8400000, "credit_ratings": "B- (S&P)"
        },
        "natural_resources": {"primary": ["petroleum", "gold", "silver", "copper", "timber", "shrimp", "fish"]},
        "military": {"budget_usd": 2600000000, "pct_of_gdp": 2.3, "active_personnel": 40000, "global_firepower_rank": 68},
        "trade": {
            "top_exports": ["crude petroleum", "shrimp", "bananas", "flowers", "canned fish", "cocoa"],
            "top_imports": ["refined petroleum", "vehicles", "machinery"],
            "major_partners": ["United States", "China", "Colombia", "Panama"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 35, "rank": 115, "year": 2023},
            "democracy_index": {"score": 5.63, "category": "Hybrid regime", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 8.0, "physician_density_per_1k": 2.1, "maternal_mortality_per_100k": 66},
        "climate_environment": {
            "climate_zones": ["tropical", "highland", "arid"], "co2_emissions_mt": 34,
            "natural_hazards": ["earthquakes", "volcanic eruptions", "floods", "El Niño"],
            "paris_agreement_status": "Ratified", "notes": "Galápagos Islands — UNESCO World Heritage"
        },
        "education": {"expenditure_pct_gdp": 4.3, "mean_years_of_schooling": 8.8},
        "digital_economy": {"e_government_index": 0.66, "innovation_index": 88},
        "diaspora_migration": {"diaspora_population": "2,500,000", "remittances_usd": "4,500,000,000", "remittances_pct_gdp": 4.0},
        "debt_aid": {"national_debt_pct_gdp": 57.0}
    },

    "bolivia": {
        "data_year": 2024,
        "demographics": {
            "median_age": 25.3, "urbanization_pct": 70.5, "fertility_rate": 2.43,
            "life_expectancy": 72.5, "infant_mortality_per_1k": 21.8, "literacy_rate_pct": 92.5,
            "net_migration_rate": -1.0, "population_growth_rate": 1.1, "population_density": 11.1,
            "age_structure": {"0_14_pct": 28.5, "15_24_pct": 18.0, "25_54_pct": 39.5, "55_64_pct": 7.0, "65_plus_pct": 7.0}
        },
        "economy_extended": {
            "gdp_growth_pct": 1.6, "inflation_pct": 2.6, "unemployment_pct": 4.0, "poverty_rate_pct": 36.3,
            "gini_index": 42.2, "sector_agriculture_pct": 13.0, "sector_industry_pct": 28.0, "sector_services_pct": 59.0,
            "labor_force": 5600000
        },
        "natural_resources": {
            "primary": ["lithium", "tin", "natural gas", "petroleum", "zinc", "tungsten", "antimony", "silver", "iron", "lead"],
            "notes": "World's largest lithium reserves in Salar de Uyuni; major natural gas exporter"
        },
        "military": {"budget_usd": 600000000, "pct_of_gdp": 1.4, "active_personnel": 40000, "global_firepower_rank": 88},
        "trade": {
            "top_exports": ["natural gas", "gold", "zinc", "soybeans", "tin"],
            "top_imports": ["vehicles", "machinery", "petroleum", "chemicals"],
            "major_partners": ["Brazil", "Argentina", "United States", "China"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 29, "rank": 133, "year": 2023},
            "democracy_index": {"score": 4.46, "category": "Hybrid regime", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 6.9, "physician_density_per_1k": 1.6, "maternal_mortality_per_100k": 161},
        "climate_environment": {
            "climate_zones": ["tropical", "highland", "semi-arid"], "co2_emissions_mt": 22,
            "natural_hazards": ["floods", "droughts", "landslides"],
            "paris_agreement_status": "Ratified"
        },
        "education": {"expenditure_pct_gdp": 7.3, "mean_years_of_schooling": 9.2},
        "digital_economy": {"e_government_index": 0.55, "innovation_index": 99},
        "diaspora_migration": {"diaspora_population": "900,000", "remittances_usd": "1,400,000,000", "remittances_pct_gdp": 3.3},
        "debt_aid": {"national_debt_pct_gdp": 80.0}
    },

    "paraguay": {
        "data_year": 2024,
        "demographics": {
            "median_age": 28.3, "urbanization_pct": 62.6, "fertility_rate": 2.38,
            "life_expectancy": 74.3, "infant_mortality_per_1k": 14.4, "literacy_rate_pct": 94.7,
            "net_migration_rate": -0.8, "population_growth_rate": 1.1, "population_density": 18.2,
            "age_structure": {"0_14_pct": 27.0, "15_24_pct": 17.5, "25_54_pct": 40.0, "55_64_pct": 7.5, "65_plus_pct": 8.0}
        },
        "economy_extended": {
            "gdp_growth_pct": 4.7, "inflation_pct": 4.6, "unemployment_pct": 6.0, "poverty_rate_pct": 22.0,
            "gini_index": 43.5, "sector_agriculture_pct": 10.0, "sector_industry_pct": 32.0, "sector_services_pct": 58.0,
            "labor_force": 3600000
        },
        "natural_resources": {"primary": ["hydropower", "timber", "iron ore", "manganese", "limestone"]},
        "military": {"budget_usd": 400000000, "pct_of_gdp": 0.9, "active_personnel": 14000, "global_firepower_rank": 95},
        "trade": {
            "top_exports": ["soybeans", "beef", "electricity", "corn", "wheat"],
            "top_imports": ["petroleum", "vehicles", "electronics"],
            "major_partners": ["Brazil", "Argentina", "Chile", "United States"],
            "trade_agreements": ["MERCOSUR"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 28, "rank": 130, "year": 2023},
            "democracy_index": {"score": 6.38, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.6, "physician_density_per_1k": 1.3, "maternal_mortality_per_100k": 71},
        "education": {"expenditure_pct_gdp": 3.4, "mean_years_of_schooling": 8.4},
        "climate_environment": {
            "climate_zones": ["subtropical", "semi-arid"], "co2_emissions_mt": 8, "renewable_energy_pct": 100.0,
            "notes": "Nearly 100% electricity from hydropower (Itaipú, Yacyretá)", "paris_agreement_status": "Ratified"
        },
        "diaspora_migration": {"diaspora_population": "900,000", "remittances_usd": "800,000,000"},
        "debt_aid": {"national_debt_pct_gdp": 34.0}
    },

    "uruguay": {
        "data_year": 2024,
        "demographics": {
            "median_age": 35.8, "urbanization_pct": 95.6, "fertility_rate": 1.48,
            "life_expectancy": 78.4, "infant_mortality_per_1k": 6.1, "literacy_rate_pct": 98.7,
            "net_migration_rate": -1.3, "population_growth_rate": 0.3, "population_density": 19.8
        },
        "economy_extended": {
            "gdp_growth_pct": 0.4, "inflation_pct": 5.9, "unemployment_pct": 8.3, "poverty_rate_pct": 3.0,
            "gini_index": 40.2, "sector_agriculture_pct": 6.2, "sector_industry_pct": 17.4, "sector_services_pct": 76.4,
            "credit_ratings": "BBB (S&P)"
        },
        "natural_resources": {"primary": ["arable land", "hydropower", "minor minerals", "fisheries"]},
        "military": {"budget_usd": 1100000000, "pct_of_gdp": 1.6, "active_personnel": 22000, "global_firepower_rank": 102},
        "trade": {
            "top_exports": ["beef", "cellulose", "soybeans", "rice", "dairy", "wood"],
            "top_imports": ["crude petroleum", "vehicles", "machinery"],
            "major_partners": ["China", "Brazil", "Argentina", "United States"],
            "trade_agreements": ["MERCOSUR"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 73, "rank": 16, "year": 2023},
            "democracy_index": {"score": 8.61, "category": "Full democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 9.3, "physician_density_per_1k": 5.1, "maternal_mortality_per_100k": 19},
        "education": {"expenditure_pct_gdp": 4.9, "mean_years_of_schooling": 9.0, "pisa_participation": True},
        "climate_environment": {"climate_zones": ["temperate"], "co2_emissions_mt": 7, "renewable_energy_pct": 97.0, "paris_agreement_status": "Ratified"},
        "digital_economy": {"e_government_index": 0.85, "innovation_index": 63},
        "debt_aid": {"national_debt_pct_gdp": 62.3}
    },

    "guyana": {
        "data_year": 2024,
        "demographics": {
            "median_age": 27.0, "urbanization_pct": 27.2, "fertility_rate": 2.37,
            "life_expectancy": 69.6, "infant_mortality_per_1k": 22.1, "literacy_rate_pct": 88.5,
            "net_migration_rate": -6.0, "population_growth_rate": 0.3, "population_density": 4.0
        },
        "economy_extended": {
            "gdp_growth_pct": 62.3, "inflation_pct": 6.7, "unemployment_pct": 12.0,
            "sector_agriculture_pct": 12.0, "sector_industry_pct": 52.5, "sector_services_pct": 35.5,
            "notes": "GDP growth surged due to offshore oil (Stabroek block, ExxonMobil); fastest-growing economy globally 2022-2024"
        },
        "natural_resources": {
            "primary": ["petroleum", "bauxite", "gold", "diamonds", "timber", "shrimp", "fish"],
            "notes": "Massive offshore oil discovery (11B+ barrels); oil production started 2019, now ~645k bbl/day"
        },
        "military": {"budget_usd": 92000000, "active_personnel": 3400, "global_firepower_rank": 0},
        "trade": {
            "top_exports": ["crude petroleum", "gold", "rice", "sugar", "shrimp", "bauxite"],
            "major_partners": ["United States", "Trinidad & Tobago", "Canada"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 37, "rank": 95, "year": 2023},
            "democracy_index": {"score": 6.05, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 5.0, "physician_density_per_1k": 1.4, "maternal_mortality_per_100k": 112},
        "education": {"expenditure_pct_gdp": 5.5, "mean_years_of_schooling": 8.5},
        "climate_environment": {"climate_zones": ["tropical"], "paris_agreement_status": "Ratified"},
        "diaspora_migration": {"diaspora_population": "550,000", "remittances_usd": "400,000,000"},
        "debt_aid": {"national_debt_pct_gdp": 26.0}
    },

    "suriname": {
        "data_year": 2024,
        "demographics": {
            "median_age": 30.0, "urbanization_pct": 66.2, "fertility_rate": 2.37,
            "life_expectancy": 72.1, "infant_mortality_per_1k": 17.8, "literacy_rate_pct": 94.4,
            "net_migration_rate": -1.0, "population_growth_rate": 0.9, "population_density": 3.8
        },
        "economy_extended": {
            "gdp_growth_pct": 2.3, "inflation_pct": 52.4, "unemployment_pct": 8.5,
            "sector_agriculture_pct": 11.0, "sector_industry_pct": 30.0, "sector_services_pct": 59.0
        },
        "natural_resources": {"primary": ["gold", "petroleum", "timber", "bauxite", "iron ore", "fish"]},
        "military": {"budget_usd": 45000000, "active_personnel": 1800, "global_firepower_rank": 0},
        "trade": {
            "top_exports": ["gold", "crude petroleum", "rice", "bananas", "shrimp"],
            "major_partners": ["Switzerland", "United Arab Emirates", "India", "United States"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 36, "rank": 104, "year": 2023},
            "democracy_index": {"score": 6.64, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 6.2, "maternal_mortality_per_100k": 96},
        "education": {"expenditure_pct_gdp": 5.0, "mean_years_of_schooling": 9.0},
        "climate_environment": {"climate_zones": ["tropical"], "protected_areas_pct": 14.8, "paris_agreement_status": "Ratified"},
        "debt_aid": {"national_debt_pct_gdp": 122.0}
    },

    "cuba": {
        "data_year": 2024,
        "demographics": {
            "median_age": 42.1, "urbanization_pct": 77.2, "fertility_rate": 1.44,
            "life_expectancy": 79.0, "infant_mortality_per_1k": 4.5, "literacy_rate_pct": 99.8,
            "net_migration_rate": -5.0, "population_growth_rate": -0.2, "population_density": 106.0
        },
        "economy_extended": {
            "gdp_growth_pct": 1.8, "inflation_pct": 45.0, "unemployment_pct": 1.3,
            "sector_agriculture_pct": 3.6, "sector_industry_pct": 22.4, "sector_services_pct": 74.0
        },
        "natural_resources": {"primary": ["cobalt", "nickel", "iron ore", "chromium", "copper", "salt", "timber", "silica", "petroleum"]},
        "military": {"budget_usd": 200000000, "active_personnel": 50000},
        "trade": {
            "top_exports": ["sugar", "nickel", "tobacco", "medical products", "citrus"],
            "major_partners": ["China", "Spain", "Netherlands", "Germany"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 42, "rank": 76, "year": 2023},
            "democracy_index": {"score": 2.84, "category": "Authoritarian", "year": 2023}
        },
        "health": {
            "health_expenditure_pct_gdp": 12.5, "physician_density_per_1k": 8.4,
            "maternal_mortality_per_100k": 39, "universal_health_coverage_index": 80,
            "notes": "Renowned medical system; exports medical professionals globally"
        },
        "education": {
            "expenditure_pct_gdp": 11.0, "tertiary_enrollment_pct": 50,
            "mean_years_of_schooling": 11.8
        },
        "climate_environment": {"climate_zones": ["tropical"], "co2_emissions_mt": 24, "paris_agreement_status": "Ratified"},
        "diaspora_migration": {"diaspora_population": "2,500,000", "net_migration_rate": -5.0},
        "debt_aid": {"national_debt_pct_gdp": 70.0}
    },

    "haiti": {
        "data_year": 2024,
        "demographics": {
            "median_age": 24.0, "urbanization_pct": 58.8, "fertility_rate": 2.84,
            "life_expectancy": 65.6, "infant_mortality_per_1k": 43.5, "literacy_rate_pct": 61.7,
            "net_migration_rate": -3.0, "population_growth_rate": 1.2, "population_density": 414.0
        },
        "economy_extended": {
            "gdp_growth_pct": -1.9, "inflation_pct": 36.8, "unemployment_pct": 15.0, "poverty_rate_pct": 58.5,
            "gini_index": 41.1, "sector_agriculture_pct": 22.0, "sector_industry_pct": 20.0, "sector_services_pct": 58.0
        },
        "natural_resources": {"primary": ["bauxite", "copper", "calcium carbonate", "gold", "marble"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "Military disbanded 1995; police PNH ~15k"},
        "trade": {
            "top_exports": ["apparel", "cocoa", "mangoes", "essential oils"],
            "major_partners": ["United States", "Dominican Republic"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 17, "rank": 172, "year": 2023},
            "democracy_index": {"score": 2.81, "category": "Authoritarian", "year": 2023},
            "fragile_states_index": {"score": 105.9, "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 3.3, "physician_density_per_1k": 0.23, "maternal_mortality_per_100k": 350},
        "education": {"expenditure_pct_gdp": 1.4, "mean_years_of_schooling": 5.6},
        "climate_environment": {
            "climate_zones": ["tropical"], "natural_hazards": ["hurricanes", "earthquakes", "floods"],
            "paris_agreement_status": "Ratified"
        },
        "diaspora_migration": {
            "diaspora_population": "2,000,000", "remittances_usd": "4,000,000,000", "remittances_pct_gdp": 22.0
        },
        "debt_aid": {"national_debt_pct_gdp": 25.0}
    },

    "dominican-republic": {
        "data_year": 2024,
        "demographics": {
            "median_age": 28.5, "urbanization_pct": 84.0, "fertility_rate": 2.22,
            "life_expectancy": 74.9, "infant_mortality_per_1k": 20.4, "literacy_rate_pct": 93.8,
            "net_migration_rate": -2.1, "population_growth_rate": 0.9, "population_density": 228.0
        },
        "economy_extended": {
            "gdp_growth_pct": 2.3, "inflation_pct": 4.8, "unemployment_pct": 5.5, "poverty_rate_pct": 23.0,
            "sector_agriculture_pct": 5.6, "sector_industry_pct": 33.0, "sector_services_pct": 61.4,
            "credit_ratings": "BB (S&P)"
        },
        "natural_resources": {"primary": ["gold", "silver", "nickel", "bauxite"]},
        "military": {"budget_usd": 950000000, "active_personnel": 56000, "global_firepower_rank": 100},
        "trade": {
            "top_exports": ["gold", "cigars", "medical instruments", "cacao", "sugar"],
            "major_partners": ["United States", "Haiti", "China"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 35, "rank": 110, "year": 2023},
            "democracy_index": {"score": 6.52, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 4.1, "physician_density_per_1k": 1.6, "maternal_mortality_per_100k": 107},
        "education": {"expenditure_pct_gdp": 4.6, "mean_years_of_schooling": 8.1},
        "digital_economy": {"e_government_index": 0.63},
        "diaspora_migration": {
            "diaspora_population": "2,300,000", "remittances_usd": "10,200,000,000", "remittances_pct_gdp": 8.5
        },
        "debt_aid": {"national_debt_pct_gdp": 44.7}
    },

    "jamaica": {
        "data_year": 2024,
        "demographics": {
            "median_age": 30.5, "urbanization_pct": 56.7, "fertility_rate": 1.89,
            "life_expectancy": 75.2, "infant_mortality_per_1k": 10.7, "literacy_rate_pct": 88.7,
            "net_migration_rate": -4.8, "population_growth_rate": 0.1, "population_density": 273.0
        },
        "economy_extended": {
            "gdp_growth_pct": 1.7, "inflation_pct": 6.5, "unemployment_pct": 4.5, "poverty_rate_pct": 18.0,
            "gini_index": 35.0, "sector_agriculture_pct": 7.0, "sector_industry_pct": 21.0, "sector_services_pct": 72.0
        },
        "natural_resources": {"primary": ["bauxite", "alumina", "gypsum", "limestone"]},
        "military": {"budget_usd": 300000000, "active_personnel": 4000},
        "trade": {
            "top_exports": ["alumina", "bauxite", "rum", "sugar", "coffee", "yams"],
            "major_partners": ["United States", "Canada", "Netherlands"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 44, "rank": 69, "year": 2023},
            "democracy_index": {"score": 7.31, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 6.1, "physician_density_per_1k": 0.8, "maternal_mortality_per_100k": 99},
        "education": {"expenditure_pct_gdp": 5.2, "mean_years_of_schooling": 9.7},
        "diaspora_migration": {
            "diaspora_population": "3,000,000", "remittances_usd": "3,200,000,000", "remittances_pct_gdp": 18.0
        },
        "debt_aid": {"national_debt_pct_gdp": 73.0}
    },

    "trinidad-and-tobago": {
        "data_year": 2024,
        "demographics": {
            "median_age": 37.0, "urbanization_pct": 53.3, "fertility_rate": 1.63,
            "life_expectancy": 74.0, "infant_mortality_per_1k": 15.2, "literacy_rate_pct": 99.0,
            "net_migration_rate": -6.0, "population_growth_rate": 0.1, "population_density": 272.0
        },
        "economy_extended": {
            "gdp_growth_pct": 2.5, "inflation_pct": 4.6, "unemployment_pct": 4.0,
            "sector_agriculture_pct": 0.4, "sector_industry_pct": 47.8, "sector_services_pct": 51.8,
            "credit_ratings": "BBB- (S&P)"
        },
        "natural_resources": {"primary": ["petroleum", "natural gas", "asphalt"]},
        "military": {"budget_usd": 320000000, "active_personnel": 4000},
        "trade": {
            "top_exports": ["petroleum", "LNG", "methanol", "ammonia", "steel"],
            "major_partners": ["United States", "Guyana", "Suriname"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 39, "rank": 89, "year": 2023},
            "democracy_index": {"score": 7.10, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.0, "physician_density_per_1k": 4.3},
        "education": {"expenditure_pct_gdp": 4.1, "mean_years_of_schooling": 11.0},
        "debt_aid": {"national_debt_pct_gdp": 77.0}
    },

    "costa-rica": {
        "data_year": 2024,
        "demographics": {
            "median_age": 33.3, "urbanization_pct": 82.0, "fertility_rate": 1.43,
            "life_expectancy": 80.8, "infant_mortality_per_1k": 7.0, "literacy_rate_pct": 97.9,
            "net_migration_rate": 0.8, "population_growth_rate": 0.5, "population_density": 101.0
        },
        "economy_extended": {
            "gdp_growth_pct": 5.1, "inflation_pct": -1.1, "unemployment_pct": 9.0, "poverty_rate_pct": 21.0,
            "sector_agriculture_pct": 4.4, "sector_industry_pct": 20.4, "sector_services_pct": 75.2,
            "credit_ratings": "BB- (S&P)"
        },
        "natural_resources": {"primary": ["hydropower"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "Abolished military in 1948; police force only"},
        "trade": {
            "top_exports": ["medical instruments", "bananas", "pineapples", "coffee", "microchips"],
            "major_partners": ["United States", "Guatemala", "Netherlands", "Belgium"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 55, "rank": 49, "year": 2023},
            "democracy_index": {"score": 8.29, "category": "Full democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.3, "physician_density_per_1k": 3.0, "maternal_mortality_per_100k": 22},
        "education": {"expenditure_pct_gdp": 6.7, "mean_years_of_schooling": 8.7, "pisa_participation": True},
        "climate_environment": {
            "climate_zones": ["tropical"], "renewable_energy_pct": 99.0, "protected_areas_pct": 26.0,
            "paris_agreement_status": "Ratified", "notes": "Plans carbon neutrality by 2050; 99% renewable electricity"
        },
        "digital_economy": {"e_government_index": 0.77, "innovation_index": 53},
        "debt_aid": {"national_debt_pct_gdp": 63.0}
    },

    "panama": {
        "data_year": 2024,
        "demographics": {
            "median_age": 30.1, "urbanization_pct": 68.8, "fertility_rate": 2.35,
            "life_expectancy": 79.2, "infant_mortality_per_1k": 10.2, "literacy_rate_pct": 95.4,
            "net_migration_rate": 1.2, "population_growth_rate": 1.4, "population_density": 57.0
        },
        "economy_extended": {
            "gdp_growth_pct": 7.3, "inflation_pct": 1.5, "unemployment_pct": 7.4,
            "gini_index": 49.2, "sector_agriculture_pct": 2.3, "sector_industry_pct": 27.5, "sector_services_pct": 70.2
        },
        "natural_resources": {"primary": ["copper", "mahogany", "shrimp", "hydropower"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "Abolished military in 1990"},
        "trade": {
            "top_exports": ["copper", "bananas", "shrimp", "sugar"],
            "major_partners": ["China", "United States", "Japan"],
            "notes": "Panama Canal generates ~$4.3B/year in revenue; Colón Free Trade Zone"
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 36, "rank": 104, "year": 2023},
            "democracy_index": {"score": 7.18, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.3, "physician_density_per_1k": 1.6, "maternal_mortality_per_100k": 52},
        "education": {"expenditure_pct_gdp": 3.2, "mean_years_of_schooling": 10.2},
        "digital_economy": {"e_government_index": 0.69},
        "debt_aid": {"national_debt_pct_gdp": 53.0}
    },

    "guatemala": {
        "data_year": 2024,
        "demographics": {
            "median_age": 22.9, "urbanization_pct": 52.8, "fertility_rate": 2.61,
            "life_expectancy": 72.8, "infant_mortality_per_1k": 22.3, "literacy_rate_pct": 81.3,
            "net_migration_rate": -2.0, "population_growth_rate": 1.6, "population_density": 167.0
        },
        "economy_extended": {
            "gdp_growth_pct": 3.5, "inflation_pct": 6.2, "unemployment_pct": 2.5, "poverty_rate_pct": 52.4,
            "gini_index": 48.3, "sector_agriculture_pct": 10.0, "sector_industry_pct": 24.0, "sector_services_pct": 66.0
        },
        "natural_resources": {"primary": ["petroleum", "nickel", "iron ore", "timber", "fish"]},
        "military": {"budget_usd": 390000000, "active_personnel": 21600, "global_firepower_rank": 90},
        "trade": {
            "top_exports": ["sugar", "coffee", "bananas", "palm oil", "cardamom", "garments"],
            "major_partners": ["United States", "El Salvador", "Honduras", "Mexico"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 23, "rank": 154, "year": 2023},
            "democracy_index": {"score": 4.60, "category": "Hybrid regime", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 5.8, "physician_density_per_1k": 1.0, "maternal_mortality_per_100k": 96},
        "education": {"expenditure_pct_gdp": 3.2, "mean_years_of_schooling": 5.6},
        "diaspora_migration": {"diaspora_population": "1,800,000", "remittances_usd": "19,400,000,000", "remittances_pct_gdp": 19.0},
        "debt_aid": {"national_debt_pct_gdp": 29.0}
    },

    "honduras": {
        "data_year": 2024,
        "demographics": {
            "median_age": 24.0, "urbanization_pct": 59.0, "fertility_rate": 2.38,
            "life_expectancy": 75.3, "infant_mortality_per_1k": 14.6, "literacy_rate_pct": 87.2,
            "net_migration_rate": -2.5, "population_growth_rate": 1.2, "population_density": 89.0
        },
        "economy_extended": {
            "gdp_growth_pct": 3.5, "inflation_pct": 6.7, "unemployment_pct": 5.3, "poverty_rate_pct": 48.3,
            "sector_agriculture_pct": 12.0, "sector_industry_pct": 27.0, "sector_services_pct": 61.0
        },
        "natural_resources": {"primary": ["timber", "gold", "silver", "copper", "lead", "zinc", "iron ore"]},
        "military": {"budget_usd": 380000000, "active_personnel": 15500, "global_firepower_rank": 103},
        "trade": {
            "top_exports": ["coffee", "bananas", "palm oil", "shrimp", "garments"],
            "major_partners": ["United States", "El Salvador", "Guatemala"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 23, "rank": 154, "year": 2023},
            "democracy_index": {"score": 5.36, "category": "Hybrid regime", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.1, "physician_density_per_1k": 0.5, "maternal_mortality_per_100k": 72},
        "education": {"expenditure_pct_gdp": 6.4, "mean_years_of_schooling": 6.6},
        "diaspora_migration": {"diaspora_population": "1,100,000", "remittances_usd": "9,000,000,000", "remittances_pct_gdp": 26.0},
        "debt_aid": {"national_debt_pct_gdp": 48.0}
    },

    "el-salvador": {
        "data_year": 2024,
        "demographics": {
            "median_age": 28.7, "urbanization_pct": 74.1, "fertility_rate": 1.81,
            "life_expectancy": 74.3, "infant_mortality_per_1k": 11.0, "literacy_rate_pct": 89.0,
            "net_migration_rate": -6.0, "population_growth_rate": 0.4, "population_density": 312.0
        },
        "economy_extended": {
            "gdp_growth_pct": 3.5, "inflation_pct": 4.1, "unemployment_pct": 6.0,
            "sector_agriculture_pct": 5.0, "sector_industry_pct": 25.0, "sector_services_pct": 70.0,
            "notes": "Bitcoin adopted as legal tender in 2021"
        },
        "natural_resources": {"primary": ["hydropower", "geothermal", "petroleum"]},
        "military": {"budget_usd": 420000000, "active_personnel": 25000, "global_firepower_rank": 92},
        "trade": {
            "top_exports": ["garments", "coffee", "sugar", "iron", "ethanol"],
            "major_partners": ["United States", "Guatemala", "Honduras"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 31, "rank": 126, "year": 2023},
            "democracy_index": {"score": 4.57, "category": "Hybrid regime", "year": 2023},
            "notes": "Nayib Bukele's mass incarceration strategy reduced homicides dramatically"
        },
        "health": {"health_expenditure_pct_gdp": 7.2, "physician_density_per_1k": 2.8, "maternal_mortality_per_100k": 43},
        "education": {"expenditure_pct_gdp": 3.8, "mean_years_of_schooling": 7.1},
        "diaspora_migration": {"diaspora_population": "2,800,000", "remittances_usd": "7,800,000,000", "remittances_pct_gdp": 24.0},
        "debt_aid": {"national_debt_pct_gdp": 72.0}
    },

    "nicaragua": {
        "data_year": 2024,
        "demographics": {
            "median_age": 27.7, "urbanization_pct": 59.3, "fertility_rate": 2.35,
            "life_expectancy": 74.5, "infant_mortality_per_1k": 14.9, "literacy_rate_pct": 82.6,
            "net_migration_rate": -3.0, "population_growth_rate": 0.8, "population_density": 55.4
        },
        "economy_extended": {
            "gdp_growth_pct": 4.0, "inflation_pct": 8.5, "unemployment_pct": 5.5, "poverty_rate_pct": 24.9,
            "sector_agriculture_pct": 15.5, "sector_industry_pct": 24.4, "sector_services_pct": 60.1
        },
        "natural_resources": {"primary": ["gold", "silver", "copper", "tungsten", "lead", "zinc", "timber", "fish"]},
        "military": {"budget_usd": 80000000, "active_personnel": 12000},
        "trade": {
            "top_exports": ["gold", "coffee", "beef", "sugar", "peanuts", "cigars"],
            "major_partners": ["United States", "El Salvador", "Mexico", "Honduras"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 17, "rank": 167, "year": 2023},
            "democracy_index": {"score": 2.47, "category": "Authoritarian", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 8.6, "physician_density_per_1k": 1.6, "maternal_mortality_per_100k": 78},
        "education": {"expenditure_pct_gdp": 4.6, "mean_years_of_schooling": 6.8},
        "diaspora_migration": {"diaspora_population": "800,000", "remittances_usd": "4,000,000,000", "remittances_pct_gdp": 25.0},
        "debt_aid": {"national_debt_pct_gdp": 46.0}
    },

    "belize": {
        "data_year": 2024,
        "demographics": {
            "median_age": 23.9, "urbanization_pct": 46.0, "fertility_rate": 2.23,
            "life_expectancy": 75.6, "infant_mortality_per_1k": 10.5, "literacy_rate_pct": 82.7,
            "net_migration_rate": 0.0, "population_growth_rate": 1.6, "population_density": 17.8
        },
        "economy_extended": {
            "gdp_growth_pct": 4.6, "inflation_pct": 4.4, "unemployment_pct": 6.0,
            "sector_agriculture_pct": 9.2, "sector_industry_pct": 13.5, "sector_services_pct": 77.3
        },
        "natural_resources": {"primary": ["arable land", "timber", "fish", "hydropower", "crude oil"]},
        "military": {"budget_usd": 25000000, "active_personnel": 1500},
        "trade": {
            "top_exports": ["sugar", "bananas", "citrus", "garments", "fish", "molasses", "wood"],
            "major_partners": ["United States", "United Kingdom", "Guatemala", "Mexico"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 6.63, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 5.6, "physician_density_per_1k": 1.1, "maternal_mortality_per_100k": 130},
        "education": {"expenditure_pct_gdp": 8.7, "mean_years_of_schooling": 9.3},
        "climate_environment": {
            "climate_zones": ["tropical"], "protected_areas_pct": 36.7,
            "notes": "Belize Barrier Reef — 2nd largest in world, UNESCO World Heritage"
        },
        "debt_aid": {"national_debt_pct_gdp": 53.0}
    },

    "bahamas": {
        "data_year": 2024,
        "demographics": {
            "median_age": 34.0, "urbanization_pct": 83.4, "fertility_rate": 1.39,
            "life_expectancy": 76.1, "infant_mortality_per_1k": 9.9, "literacy_rate_pct": 95.6,
            "net_migration_rate": 0.0, "population_growth_rate": 0.8, "population_density": 39.0
        },
        "economy_extended": {
            "gdp_growth_pct": 4.3, "inflation_pct": 3.0, "unemployment_pct": 9.0,
            "sector_agriculture_pct": 2.3, "sector_industry_pct": 7.7, "sector_services_pct": 90.0
        },
        "natural_resources": {"primary": ["salt", "aragonite", "timber", "fisheries"]},
        "military": {"budget_usd": 120000000, "active_personnel": 1800},
        "trade": {
            "top_exports": ["crude petroleum", "salt", "polystyrene", "aragonite", "crawfish"],
            "major_partners": ["United States", "Poland", "Germany"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 64, "rank": 30, "year": 2023},
            "democracy_index": {"score": 7.31, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 5.8, "physician_density_per_1k": 2.2},
        "education": {"expenditure_pct_gdp": 2.5, "mean_years_of_schooling": 11.6},
        "debt_aid": {"national_debt_pct_gdp": 83.0}
    },

    "barbados": {
        "data_year": 2024,
        "demographics": {
            "median_age": 40.0, "urbanization_pct": 31.2, "fertility_rate": 1.60,
            "life_expectancy": 79.6, "infant_mortality_per_1k": 9.6, "literacy_rate_pct": 99.6,
            "net_migration_rate": -0.3, "population_growth_rate": 0.2, "population_density": 667.0
        },
        "economy_extended": {
            "gdp_growth_pct": 4.4, "inflation_pct": 5.0, "unemployment_pct": 7.5,
            "sector_agriculture_pct": 1.7, "sector_industry_pct": 11.0, "sector_services_pct": 87.3
        },
        "natural_resources": {"primary": ["petroleum", "natural gas", "fisheries"]},
        "military": {"budget_usd": 42000000, "active_personnel": 610},
        "trade": {
            "top_exports": ["refined petroleum", "rum", "chemicals", "electrical components"],
            "major_partners": ["United States", "Jamaica", "Guyana", "Trinidad & Tobago"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 65, "rank": 27, "year": 2023},
            "democracy_index": {"score": 7.67, "category": "Flawed democracy", "year": 2023}
        },
        "health": {"health_expenditure_pct_gdp": 7.2, "physician_density_per_1k": 2.5},
        "education": {"expenditure_pct_gdp": 4.4, "mean_years_of_schooling": 11.0},
        "climate_environment": {"notes": "PM Mia Mottley's Bridgetown Initiative for climate finance reform"},
        "debt_aid": {"national_debt_pct_gdp": 117.0}
    },

    "antigua-and-barbuda": {
        "data_year": 2024,
        "demographics": {
            "median_age": 33.0, "urbanization_pct": 24.4, "fertility_rate": 1.96,
            "life_expectancy": 77.5, "infant_mortality_per_1k": 11.1, "literacy_rate_pct": 99.0,
            "population_growth_rate": 1.2, "population_density": 227.0
        },
        "economy_extended": {
            "gdp_growth_pct": 6.2, "inflation_pct": 5.1, "unemployment_pct": 11.0,
            "sector_agriculture_pct": 1.8, "sector_industry_pct": 18.0, "sector_services_pct": 80.2
        },
        "natural_resources": {"primary": ["fisheries", "cotton", "salt"]},
        "military": {"budget_usd": 14000000, "active_personnel": 180},
        "trade": {
            "top_exports": ["refined petroleum", "ships", "rum"],
            "major_partners": ["United States", "United Kingdom", "Poland"]
        },
        "governance_indices": {
            "corruption_perception_index": {"score": 0, "rank": 0, "year": 0},
            "democracy_index": {"score": 0, "category": "Not rated", "year": 0}
        },
        "health": {"health_expenditure_pct_gdp": 5.6, "physician_density_per_1k": 2.8},
        "education": {"expenditure_pct_gdp": 3.6, "mean_years_of_schooling": 9.2},
        "debt_aid": {"national_debt_pct_gdp": 72.0}
    },

    "dominica": {
        "data_year": 2024,
        "demographics": {
            "median_age": 35.0, "urbanization_pct": 71.1, "fertility_rate": 1.84,
            "life_expectancy": 78.3, "infant_mortality_per_1k": 9.7, "literacy_rate_pct": 94.0,
            "population_growth_rate": -0.1, "population_density": 96.5
        },
        "economy_extended": {
            "gdp_growth_pct": 5.0, "inflation_pct": 3.5, "unemployment_pct": 23.0,
            "sector_agriculture_pct": 22.3, "sector_industry_pct": 12.2, "sector_services_pct": 65.5
        },
        "natural_resources": {"primary": ["timber", "hydropower", "geothermal"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "No military; Regional Security System"},
        "trade": {
            "top_exports": ["bananas", "soap", "bay oil", "vegetables"],
            "major_partners": ["Saudi Arabia", "Trinidad & Tobago", "Jamaica"]
        },
        "governance_indices": {"democracy_index": {"score": 0, "category": "Not rated", "year": 0}},
        "health": {"health_expenditure_pct_gdp": 5.7, "physician_density_per_1k": 1.1},
        "education": {"expenditure_pct_gdp": 5.0, "mean_years_of_schooling": 8.0},
        "climate_environment": {"notes": "First climate-resilient nation ambition; devastated by Hurricane Maria 2017"},
        "debt_aid": {"national_debt_pct_gdp": 78.0}
    },

    "grenada": {
        "data_year": 2024,
        "demographics": {
            "median_age": 33.5, "urbanization_pct": 37.0, "fertility_rate": 1.88,
            "life_expectancy": 75.2, "infant_mortality_per_1k": 9.4, "literacy_rate_pct": 98.6,
            "population_growth_rate": 0.3, "population_density": 332.0
        },
        "economy_extended": {
            "gdp_growth_pct": 5.0, "inflation_pct": 2.7, "unemployment_pct": 12.0,
            "sector_agriculture_pct": 6.0, "sector_industry_pct": 15.0, "sector_services_pct": 79.0
        },
        "natural_resources": {"primary": ["timber", "tropical fruit", "nutmeg", "deepwater harbors"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "No military; Regional Security System"},
        "trade": {
            "top_exports": ["nutmeg", "mace", "cocoa", "fish", "flour"],
            "major_partners": ["United States", "Saint Vincent", "Saint Lucia"],
            "notes": "World's 2nd largest nutmeg producer"
        },
        "governance_indices": {"democracy_index": {"score": 7.17, "category": "Flawed democracy", "year": 2023}},
        "health": {"health_expenditure_pct_gdp": 4.8, "physician_density_per_1k": 1.4},
        "education": {"expenditure_pct_gdp": 3.2, "mean_years_of_schooling": 8.7},
        "debt_aid": {"national_debt_pct_gdp": 63.0}
    },

    "saint-lucia": {
        "data_year": 2024,
        "demographics": {
            "median_age": 36.6, "urbanization_pct": 19.2, "fertility_rate": 1.40,
            "life_expectancy": 78.5, "infant_mortality_per_1k": 11.3, "literacy_rate_pct": 90.1,
            "population_growth_rate": 0.3, "population_density": 298.0
        },
        "economy_extended": {
            "gdp_growth_pct": 3.4, "inflation_pct": 3.7, "unemployment_pct": 15.0,
            "sector_agriculture_pct": 2.9, "sector_industry_pct": 14.2, "sector_services_pct": 82.9
        },
        "natural_resources": {"primary": ["forests", "sandy beaches", "geothermal", "fisheries"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "No military; Royal Saint Lucia Police Force + RSS"},
        "trade": {"top_exports": ["bananas", "clothing", "cocoa", "vegetables", "coconut oil"]},
        "governance_indices": {"democracy_index": {"score": 0, "category": "Not rated", "year": 0}},
        "health": {"health_expenditure_pct_gdp": 4.4, "physician_density_per_1k": 0.6},
        "education": {"expenditure_pct_gdp": 3.6, "mean_years_of_schooling": 8.5},
        "debt_aid": {"national_debt_pct_gdp": 62.0}
    },

    "saint-kitts-and-nevis": {
        "data_year": 2024,
        "demographics": {
            "median_age": 37.1, "urbanization_pct": 30.8, "fertility_rate": 1.76,
            "life_expectancy": 77.2, "infant_mortality_per_1k": 7.7, "literacy_rate_pct": 97.8,
            "population_growth_rate": 0.6, "population_density": 210.0
        },
        "economy_extended": {
            "gdp_growth_pct": 5.0, "inflation_pct": 3.6, "unemployment_pct": 5.0,
            "sector_agriculture_pct": 1.1, "sector_industry_pct": 26.0, "sector_services_pct": 72.9
        },
        "natural_resources": {"primary": ["arable land", "fisheries"]},
        "military": {"budget_usd": 13000000, "active_personnel": 300},
        "trade": {"top_exports": ["electronics", "rum", "cotton"], "major_partners": ["United States", "United Kingdom"]},
        "governance_indices": {"democracy_index": {"score": 0, "category": "Not rated", "year": 0}},
        "health": {"health_expenditure_pct_gdp": 5.4, "physician_density_per_1k": 2.7},
        "education": {"expenditure_pct_gdp": 2.6, "mean_years_of_schooling": 8.4},
        "debt_aid": {"national_debt_pct_gdp": 50.0}
    },

    "saint-vincent-and-the-grenadines": {
        "data_year": 2024,
        "demographics": {
            "median_age": 36.0, "urbanization_pct": 53.9, "fertility_rate": 1.70,
            "life_expectancy": 76.7, "infant_mortality_per_1k": 11.7, "literacy_rate_pct": 96.0,
            "population_growth_rate": -0.2, "population_density": 284.0
        },
        "economy_extended": {
            "gdp_growth_pct": 5.8, "inflation_pct": 4.7, "unemployment_pct": 18.0,
            "sector_agriculture_pct": 7.1, "sector_industry_pct": 17.0, "sector_services_pct": 75.9
        },
        "natural_resources": {"primary": ["hydropower", "cropland"]},
        "military": {"budget_usd": 0, "active_personnel": 0, "notes": "No military; RSS"},
        "trade": {"top_exports": ["bananas", "eddoes/dasheen", "arrowroot starch", "tennis rackets"]},
        "governance_indices": {"democracy_index": {"score": 7.12, "category": "Flawed democracy", "year": 2023}},
        "health": {"health_expenditure_pct_gdp": 4.5, "physician_density_per_1k": 0.7},
        "education": {"expenditure_pct_gdp": 5.7, "mean_years_of_schooling": 8.7},
        "climate_environment": {"notes": "La Soufrière volcano erupted massively April 2021, displacing 16,000"},
        "debt_aid": {"national_debt_pct_gdp": 79.0}
    },
}


def main():
    print(f"{'DRY RUN — ' if DRY_RUN else ''}Populating {len(AMERICAS_DATA)} Americas countries...\n")
    success = 0
    for slug, data in sorted(AMERICAS_DATA.items()):
        print(f"Processing: {slug}")
        if populate_country(slug, data):
            success += 1
    print(f"\nDone. {success}/{len(AMERICAS_DATA)} countries {'would be ' if DRY_RUN else ''}updated.")


if __name__ == "__main__":
    main()
