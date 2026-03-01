#!/usr/bin/env python3
"""
Patch African countries' index.json country_profile to fill:
  1. notes_unique   – a distinguishing historical/geographic fact
  2. international_memberships – accurate list of international orgs
  3. other_languages – additional languages spoken (where missing)

Usage:
    python3 scripts/patch_africa_index_profiles.py
"""

import json, os

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "geo-registry", "places", "countries",
)

# ── DATA ──────────────────────────────────────────────────────────────
# Each entry: (notes_unique, international_memberships, other_languages_or_None)

PATCHES = {
    "algeria": {
        "notes_unique": "Largest country in Africa by area; fought an eight-year war of independence from France (1954–1962) that became a model for anti-colonial struggles worldwide.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "OPEC", "NAM", "G-77", "AMU"],
        "other_languages": ["French", "Tamazight (Berber dialects)"],
    },
    "angola": {
        "notes_unique": "Sub-Saharan Africa's second-largest oil producer; endured a 27-year civil war (1975–2002) between MPLA and UNITA that shaped Cold War proxy dynamics in Africa.",
        "international_memberships": ["UN", "AU", "SADC", "OPEC", "CPLP", "NAM", "G-77", "ACP"],
        "other_languages": ["Umbundu", "Kimbundu", "Kikongo", "Chokwe", "Lunda"],
    },
    "benin": {
        "notes_unique": "Historical cradle of the Vodun (Voodoo) religion; the Kingdom of Dahomey fielded the famous all-female Mino ('Amazons') warrior regiment.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "NAM", "G-77", "ACP", "La Francophonie"],
        "other_languages": ["Fon", "Yoruba", "Bariba", "Dendi"],
    },
    "botswana": {
        "notes_unique": "Africa's longest continuous multi-party democracy since independence (1966); transformed from one of the poorest countries to upper-middle-income through diamond revenues.",
        "international_memberships": ["UN", "AU", "SADC", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Setswana", "Kalanga", "Sekgalagadi"],
    },
    "burkina-faso": {
        "notes_unique": "Formerly Upper Volta, renamed by Thomas Sankara (the 'African Che Guevara') who led revolutionary social programmes before his 1987 assassination.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "NAM", "G-77", "ACP", "La Francophonie"],
        "other_languages": ["Mooré", "Dyula", "Fulfulde", "Gourma"],
    },
    "burundi": {
        "notes_unique": "One of the most densely populated countries in Africa; drum-playing (the Royal Drummers of Burundi) is a UNESCO Intangible Cultural Heritage.",
        "international_memberships": ["UN", "AU", "EAC", "COMESA", "NAM", "G-77", "ACP", "La Francophonie", "OIC"],
        "other_languages": ["Swahili"],
    },
    "cabo-verde": {
        "notes_unique": "Volcanic archipelago 570 km off West Africa; developed a unique Creole culture blending African and Portuguese traditions; one of Africa's most stable democracies.",
        "international_memberships": ["UN", "AU", "ECOWAS", "CPLP", "NAM", "G-77", "ACP", "WTO", "La Francophonie"],
        "other_languages": ["Kabuverdianu (Cape Verdean Creole)"],
    },
    "cameroon": {
        "notes_unique": "Known as 'Africa in Miniature' for its geographic and cultural diversity; one of the few African nations with both English and French as official languages.",
        "international_memberships": ["UN", "AU", "CEMAC", "Commonwealth", "La Francophonie", "OIC", "NAM", "G-77", "ACP"],
        "other_languages": ["Cameroon Pidgin English", "Fulfulde", "Ewondo", "Bamileke languages"],
    },
    "central-african-republic": {
        "notes_unique": "Rich in diamonds and gold yet one of the world's least developed countries; Jean-Bédel Bokassa crowned himself 'emperor' in a lavish 1977 ceremony.",
        "international_memberships": ["UN", "AU", "CEMAC", "La Francophonie", "OIC", "NAM", "G-77", "ACP"],
        "other_languages": ["Banda", "Gbaya", "Ngbandi", "Zande"],
    },
    "chad": {
        "notes_unique": "Home to the oldest known hominid fossil (Sahelanthropus tchadensis, c. 7 million years); Lake Chad has shrunk by 90% since the 1960s due to climate change.",
        "international_memberships": ["UN", "AU", "CEMAC", "OIC", "NAM", "G-77", "ACP", "La Francophonie", "OPEC (observer)"],
        "other_languages": ["Sara", "Kanembou", "Mundang", "Massa", "Mussei"],
    },
    "comoros": {
        "notes_unique": "Archipelago between Mozambique and Madagascar; world's largest producer of ylang-ylang essential oil; has experienced over 20 coups or attempted coups since 1975.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "La Francophonie", "NAM", "G-77", "COMESA", "IOC"],
        "other_languages": ["French", "Comorian (Shikomori)"],
    },
    "congo": {
        "notes_unique": "Brazzaville (capital) sits directly across the Congo River from Kinshasa (DR Congo) — the closest pair of national capitals in the world.",
        "international_memberships": ["UN", "AU", "CEMAC", "La Francophonie", "OIC", "NAM", "G-77", "ACP", "OPEC"],
        "other_languages": ["Lingala", "Kituba", "Teke", "Mbochi"],
    },
    "cote-divoire": {
        "notes_unique": "World's largest cocoa producer (~40% of global supply); the Basilica of Our Lady of Peace in Yamoussoukro is the largest church in the world.",
        "international_memberships": ["UN", "AU", "ECOWAS", "La Francophonie", "OIC", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Dyula", "Baoulé", "Bété", "Senufo", "Dan"],
    },
    "djibouti": {
        "notes_unique": "Strategic location at the Bab el-Mandeb strait; hosts military bases of the US, France, China, Japan, and Italy — the densest concentration of foreign bases in the world.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "IGAD", "COMESA", "La Francophonie", "NAM", "G-77", "ACP"],
        "other_languages": ["Afar", "Somali", "Ta'izzi-Adeni Arabic"],
    },
    "dr-congo": {
        "notes_unique": "Second-largest country in Africa; holds ~70% of the world's coltan reserves essential for electronics; the Congo River is the world's deepest river.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "CEPGL", "La Francophonie", "NAM", "G-77", "ACP", "OIC"],
        "other_languages": ["Lingala", "Swahili", "Tshiluba", "Kikongo"],
    },
    "egypt": {
        "notes_unique": "Home to one of the world's oldest civilisations (c. 3100 BCE); the Great Pyramid of Giza was the tallest man-made structure for over 3,800 years; the Suez Canal handles ~12% of world trade.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "NAM", "COMESA", "G-77", "WTO"],
    },
    "equatorial-guinea": {
        "notes_unique": "The only African country with Spanish as an official language; oil wealth gives it Africa's highest GDP per capita, though wealth distribution is extremely unequal.",
        "international_memberships": ["UN", "AU", "CEMAC", "La Francophonie", "CPLP", "NAM", "G-77", "ACP", "OPEC"],
        "other_languages": ["Fang", "Bubi", "Annobonese Creole Portuguese", "Pidgin English"],
    },
    "eritrea": {
        "notes_unique": "Won independence from Ethiopia in 1993 after a 30-year guerrilla war; the capital Asmara's Modernist architecture is a UNESCO World Heritage Site.",
        "international_memberships": ["UN", "AU", "IGAD", "NAM", "G-77", "ACP"],
        "other_languages": ["Arabic", "Tigre", "Afar", "Saho", "Bilen", "Kunama"],
    },
    "eswatini": {
        "notes_unique": "Africa's last absolute monarchy; renamed from Swaziland to Eswatini in 2018; the annual Umhlanga (Reed Dance) ceremony involves tens of thousands of young women.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "Commonwealth", "NAM", "G-77", "ACP"],
        "other_languages": ["Zulu", "Tsonga", "Afrikaans"],
    },
    "ethiopia": {
        "notes_unique": "One of only two African countries never colonised (alongside Liberia); uses the Ge'ez calendar (7–8 years behind Gregorian); home of the African Union headquarters in Addis Ababa.",
        "international_memberships": ["UN", "AU", "IGAD", "COMESA", "NAM", "G-77", "ACP", "WTO (observer)"],
        "other_languages": ["Oromo", "Somali", "Tigrinya", "Sidamo", "Wolaytta", "Gurage", "Afar"],
    },
    "gabon": {
        "notes_unique": "Over 80% of the country is covered by tropical rainforest; the Lopé-Okanda landscape is a UNESCO World Heritage Site blending dense forest and savanna.",
        "international_memberships": ["UN", "AU", "CEMAC", "La Francophonie", "OIC", "NAM", "G-77", "ACP", "OPEC"],
        "other_languages": ["Fang", "Myene", "Nzebi", "Bapounou/Eschira", "Bandjabi"],
    },
    "gambia": {
        "notes_unique": "Africa's smallest mainland country; the River Gambia is navigable deep into the interior; the country was the setting for Alex Haley's 'Roots'.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "Commonwealth", "NAM", "G-77", "ACP"],
        "other_languages": ["Mandinka", "Wolof", "Fula", "Serer", "Jola"],
    },
    "ghana": {
        "notes_unique": "First sub-Saharan African country to gain independence (1957); named after the medieval Ghana Empire; the Ashanti Golden Stool is the symbol of national unity.",
        "international_memberships": ["UN", "AU", "ECOWAS", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Akan (Twi/Fante)", "Ewe", "Ga", "Dagbani", "Nzema", "Hausa"],
    },
    "guinea": {
        "notes_unique": "First French-speaking African country to gain independence (1958) after voting 'No' in de Gaulle's referendum; holds the world's largest bauxite reserves.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "La Francophonie", "NAM", "G-77", "ACP", "MRU"],
        "other_languages": ["Pular/Fulfulde", "Maninka", "Susu", "Kissi", "Kpelle"],
    },
    "guinea-bissau": {
        "notes_unique": "Bijagos Archipelago is a UNESCO Biosphere Reserve; the country has experienced multiple coups; cashew nuts are the primary export (~90% of export earnings).",
        "international_memberships": ["UN", "AU", "ECOWAS", "CPLP", "OIC", "La Francophonie", "NAM", "G-77", "ACP"],
        "other_languages": ["Crioulo (Guinea-Bissau Creole)", "Balanta", "Fula", "Mandinka", "Papel"],
    },
    "kenya": {
        "notes_unique": "Home to the Great Rift Valley and major fossil hominid discoveries (Turkana Boy, 'Millennium Man'); Maasai Mara hosts the world's largest annual wildlife migration.",
        "international_memberships": ["UN", "AU", "EAC", "COMESA", "IGAD", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Kikuyu", "Luhya", "Luo", "Kalenjin", "Kamba", "Maasai"],
    },
    "lesotho": {
        "notes_unique": "Entirely surrounded by South Africa; the only country in the world with all its territory above 1,000m elevation; known as the 'Kingdom in the Sky'.",
        "international_memberships": ["UN", "AU", "SADC", "Commonwealth", "NAM", "G-77", "ACP"],
        "other_languages": ["Zulu", "Xhosa", "Phuthi"],
    },
    "liberia": {
        "notes_unique": "Founded by freed American slaves in 1847; Africa's oldest republic; Ellen Johnson Sirleaf became Africa's first elected female head of state in 2006.",
        "international_memberships": ["UN", "AU", "ECOWAS", "MRU", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Kpelle", "Bassa", "Grebo", "Vai", "Kru", "Liberian English Creole"],
    },
    "libya": {
        "notes_unique": "Holds Africa's largest proven oil reserves; the ancient Roman city of Leptis Magna is one of the best-preserved Roman sites in the Mediterranean.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "OPEC", "NAM", "G-77", "AMU"],
        "other_languages": ["Berber (Nafusi, Tamahaq)", "Italian (widely understood in Tripoli)"],
    },
    "madagascar": {
        "notes_unique": "World's fourth-largest island; over 90% of its wildlife is found nowhere else on Earth; Austronesian origins link its language and culture to Southeast Asia.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "La Francophonie", "OIC", "NAM", "G-77", "ACP", "IOC"],
        "other_languages": ["French", "Malagasy dialects (Merina, Betsimisaraka, Sakalava)"],
    },
    "malawi": {
        "notes_unique": "Known as 'The Warm Heart of Africa'; Lake Malawi (Lake Nyasa) holds more species of freshwater fish than any other lake in the world (~1,000 cichlid species).",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "Commonwealth", "NAM", "G-77", "ACP"],
        "other_languages": ["Chichewa/Chinyanja", "Yao", "Tumbuka", "Lomwe", "Sena"],
    },
    "mali": {
        "notes_unique": "Timbuktu was a medieval centre of Islamic scholarship with the world's oldest university (Sankore); Mansa Musa's 1324 hajj is considered history's most lavish pilgrimage.",
        "international_memberships": ["UN", "AU", "ECOWAS (suspended)", "OIC", "La Francophonie (suspended)", "NAM", "G-77", "ACP"],
        "other_languages": ["Bambara", "Fulfulde", "Songhai", "Soninke", "Tamasheq", "Dogon"],
    },
    "mauritania": {
        "notes_unique": "Bridges Arab North Africa and sub-Saharan West Africa; the Richat Structure ('Eye of the Sahara') is a 40 km geological formation visible from space; last country to legally abolish slavery (1981).",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "AMU", "NAM", "G-77", "ACP", "La Francophonie"],
        "other_languages": ["French", "Pulaar", "Soninke", "Wolof"],
    },
    "mauritius": {
        "notes_unique": "Home of the extinct dodo bird; a model of multi-ethnic harmony (Indian, Creole, Chinese, Franco-Mauritian communities); consistently ranks as Africa's most democratic and prosperous nation.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "Commonwealth", "La Francophonie", "NAM", "G-77", "ACP", "IOC", "WTO"],
        "other_languages": ["Mauritian Creole (Kreol Morisien)", "French", "Bhojpuri", "Hindi", "Tamil", "Telugu", "Urdu", "Mandarin"],
    },
    "morocco": {
        "notes_unique": "Home to the University of al-Qarawiyyin (859 CE), recognised as the world's oldest existing university; controls most of disputed Western Sahara; the only African country bordering the Mediterranean and Atlantic.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "AMU", "La Francophonie", "NAM", "G-77", "WTO"],
        "other_languages": ["French", "Hassaniya Arabic", "Tarifit", "Tashelhit", "Central Atlas Tamazight"],
    },
    "mozambique": {
        "notes_unique": "The Mozambique Channel is one of the richest marine biodiversity corridors; massive offshore natural gas discoveries are reshaping the economy; one of the few African flags featuring a modern weapon (AK-47).",
        "international_memberships": ["UN", "AU", "SADC", "CPLP", "Commonwealth", "OIC", "La Francophonie", "NAM", "G-77", "ACP"],
        "other_languages": ["Makhuwa", "Sena", "Ndau", "Tsonga", "Lomwe", "Swahili"],
    },
    "namibia": {
        "notes_unique": "The Namib Desert is considered the world's oldest desert (55–80 million years); one of the least densely populated countries on Earth; Namibia's constitution was the first in Africa to include environmental protection.",
        "international_memberships": ["UN", "AU", "SADC", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Afrikaans", "German", "Oshiwambo", "Otjiherero", "Nama/Damara", "Kavango languages"],
    },
    "niger": {
        "notes_unique": "Named after the Niger River; the Aïr Mountains contain some of the Sahara's finest rock art; one of the world's youngest populations (median age ~15 years) and highest fertility rates.",
        "international_memberships": ["UN", "AU", "ECOWAS (suspended)", "OIC", "La Francophonie (suspended)", "NAM", "G-77", "ACP"],
        "other_languages": ["Hausa", "Zarma/Songhai", "Fulfulde", "Tamajaq (Tuareg)", "Kanuri", "Arabic"],
    },
    "nigeria": {
        "notes_unique": "Africa's most populous country (~220 million) and largest economy; Nollywood is the world's second-largest film industry by volume; the Nok civilisation produced sub-Saharan Africa's earliest known terracottas.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "OPEC", "Commonwealth", "NAM", "G-77", "ACP", "WTO", "D-8"],
        "other_languages": ["Hausa", "Yoruba", "Igbo", "Fulfulde", "Tiv", "Kanuri", "Ijaw"],
    },
    "rwanda": {
        "notes_unique": "Has the world's highest proportion of women in parliament (~60%); underwent devastating 1994 genocide then became one of Africa's fastest-growing economies; first country to ban plastic bags (2008).",
        "international_memberships": ["UN", "AU", "EAC", "COMESA", "Commonwealth", "La Francophonie", "NAM", "G-77", "ACP"],
        "other_languages": ["Swahili"],
    },
    "sao-tome-and-principe": {
        "notes_unique": "Second-smallest African country; the equator passes through it; once the world's largest producer of cocoa; the islands were uninhabited before Portuguese discovery in the 1470s.",
        "international_memberships": ["UN", "AU", "CPLP", "La Francophonie", "NAM", "G-77", "ACP"],
        "other_languages": ["Forro Creole", "Angolar", "Principense"],
    },
    "senegal": {
        "notes_unique": "Gorée Island was a major slave-trading centre now serving as a memorial; Dakar is the westernmost point of continental Africa; the country has never experienced a military coup.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "La Francophonie", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Wolof", "Pulaar", "Serer", "Jola", "Mandinka", "Soninke"],
    },
    "seychelles": {
        "notes_unique": "Smallest African country by population (~100,000); the Vallée de Mai on Praslin island holds the world's largest seed (coco de mer palm); the country has the highest GDP per capita in Africa.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "Commonwealth", "La Francophonie", "NAM", "G-77", "ACP", "IOC"],
        "other_languages": ["Seychellois Creole", "French"],
    },
    "sierra-leone": {
        "notes_unique": "Freetown was founded in 1787 as a settlement for freed slaves; the country supplied many of the first Western-educated Africans; rich in diamonds that fuelled a brutal civil war (1991–2002).",
        "international_memberships": ["UN", "AU", "ECOWAS", "MRU", "Commonwealth", "OIC", "NAM", "G-77", "ACP"],
        "other_languages": ["Krio (Creole)", "Mende", "Temne", "Limba", "Kuranko"],
    },
    "somalia": {
        "notes_unique": "Has the longest coastline in mainland Africa (~3,025 km); one of the most ethnically homogeneous countries in Africa; the ancient Land of Punt was likely in this region.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "IGAD", "NAM", "G-77", "ACP"],
        "other_languages": ["Arabic", "Italian", "English", "Swahili (in the south)"],
    },
    "south-africa": {
        "notes_unique": "Has 11 official languages; ended apartheid in 1994 with the first democratic election; the Cradle of Humankind near Johannesburg holds some of the world's oldest hominid fossils.",
        "international_memberships": ["UN", "AU", "SADC", "BRICS", "Commonwealth", "G-20", "G-77", "NAM", "ACP", "WTO"],
        "other_languages": ["Afrikaans", "isiXhosa", "Sepedi", "Setswana", "Sesotho", "Xitsonga", "siSwati", "Tshivenda", "isiNdebele"],
    },
    "south-sudan": {
        "notes_unique": "World's youngest country (independent 2011); largest swamp in Africa (the Sudd); massive oil reserves supply ~98% of government revenue; endured civil war from 2013 to 2018.",
        "international_memberships": ["UN", "AU", "EAC", "IGAD", "NAM", "G-77"],
        "other_languages": ["Arabic (Juba Arabic)", "Dinka", "Nuer", "Bari", "Zande", "Shilluk"],
    },
    "sudan": {
        "notes_unique": "Ancient Nubia (Kush/Meroë) rivalled Egypt in power; has more pyramids than Egypt (~255); the confluence of the White and Blue Nile occurs at Khartoum.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "IGAD", "COMESA", "NAM", "G-77", "ACP"],
        "other_languages": ["Nubian languages", "Beja", "Fur", "Zaghawa", "Nuba languages"],
    },
    "tanzania": {
        "notes_unique": "Home to Kilimanjaro — Africa's highest peak (5,895 m); the Serengeti hosts the Great Migration; Olduvai Gorge is one of the most important paleoanthropological sites in the world.",
        "international_memberships": ["UN", "AU", "EAC", "SADC", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Sukuma", "Chagga", "Haya", "Makonde", "Nyamwezi", "Arabic (in Zanzibar)"],
    },
    "togo": {
        "notes_unique": "Narrow country stretching 579 km from the Gulf of Guinea to the Sahel; the Batammariba mud tower-houses (Tata Somba) are a UNESCO World Heritage Site.",
        "international_memberships": ["UN", "AU", "ECOWAS", "OIC", "La Francophonie", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Ewe", "Kabyè", "Kotokoli/Tem", "Moba", "Gourma"],
    },
    "tunisia": {
        "notes_unique": "Site of ancient Carthage, Rome's greatest rival; birthplace of the 2011 Arab Spring (Jasmine Revolution); the Saharan oasis town of Tozeur was a Star Wars filming location.",
        "international_memberships": ["UN", "AU", "Arab League", "OIC", "AMU", "La Francophonie", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["French", "Tunisian Arabic (Derja)", "Berber (Shelha)"],
    },
    "uganda": {
        "notes_unique": "Source of the White Nile (Lake Victoria); Winston Churchill called it 'the Pearl of Africa'; home to roughly half the world's remaining mountain gorillas in Bwindi Impenetrable Forest.",
        "international_memberships": ["UN", "AU", "EAC", "IGAD", "COMESA", "Commonwealth", "OIC", "NAM", "G-77", "ACP"],
        "other_languages": ["Luganda", "Lusoga", "Runyankole", "Runyoro", "Ateso", "Luo (Acholi, Langi)"],
    },
    "western-sahara": {
        "notes_unique": "A disputed territory claimed by Morocco and the Polisario Front (Sahrawi Arab Democratic Republic); one of the world's most sparsely populated territories; rich in phosphate reserves and fisheries.",
        "international_memberships": ["AU (SADR member)", "NAM (observer)"],
        "other_languages": ["Hassaniya Arabic", "Berber (Zenaga)"],
    },
    "zambia": {
        "notes_unique": "Home to Victoria Falls (Mosi-oa-Tunya, 'The Smoke That Thunders'), shared with Zimbabwe; one of Africa's most urbanised countries; the Copperbelt was once the world's third-largest copper producer.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "Commonwealth", "NAM", "G-77", "ACP", "WTO"],
        "other_languages": ["Bemba", "Nyanja/Chewa", "Tonga", "Lozi", "Kaonde", "Luvale", "Lunda"],
    },
    "zimbabwe": {
        "notes_unique": "Named after Great Zimbabwe, the largest ancient stone structure in sub-Saharan Africa; experienced hyperinflation peaking at 79.6 billion percent in 2008; Victoria Falls is one of the Seven Natural Wonders.",
        "international_memberships": ["UN", "AU", "SADC", "COMESA", "NAM", "G-77", "ACP", "WTO (observer)"],
        "other_languages": ["Shona", "Ndebele", "Tonga", "Venda", "Kalanga", "Sotho", "Nambya"],
    },
}


def main():
    updated = 0
    for slug, patch in sorted(PATCHES.items()):
        path = os.path.join(BASE, slug, "index.json")
        if not os.path.exists(path):
            print(f"  SKIP  {slug}: index.json not found")
            continue

        with open(path) as f:
            data = json.load(f)

        cp = data.get("country_profile", {})
        changed = False

        # 1. notes_unique
        if "notes_unique" in patch and (not cp.get("notes_unique")):
            cp["notes_unique"] = patch["notes_unique"]
            changed = True

        # 2. international_memberships
        if "international_memberships" in patch and (not cp.get("international_memberships")):
            cp["international_memberships"] = patch["international_memberships"]
            changed = True

        # 3. other_languages
        if "other_languages" in patch and "other_languages" not in cp:
            cp["other_languages"] = patch["other_languages"]
            changed = True

        if changed:
            data["country_profile"] = cp
            with open(path, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated += 1
            fields = []
            if "notes_unique" in patch:
                fields.append("notes_unique")
            if "international_memberships" in patch:
                fields.append("intl_memberships")
            if "other_languages" in patch:
                fields.append("other_languages")
            print(f"  OK   {slug}: patched {', '.join(fields)}")
        else:
            print(f"  ---  {slug}: already complete")

    print(f"\nDone. {updated} countries patched.")


if __name__ == "__main__":
    main()
