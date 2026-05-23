import json, os

USED = set([
    "african-union-commission", "althing-the-worlds-oldest-surviving-parl", "athenian-assembly", "bundesrat", "assembly-of-experts-for-leadership", "cabinet-of-japan", "amyotha-hluttaw", "british-parliament",
    "abbasids", "achaemenid-dynasty", "afsharid-dynasty", "aghlabids", "fatimid-caliphate", "han-dynasty", "maurya-dynasty", "ottoman-dynasty", "ming-dynasty", "mughal-dynasty", "gupta-empire-india", "khmer-empire", "ayyubid-dynasty", "buyid-dynasty", "carolingian-dynasty", "hasmonean-dynasty", "qin-dynasty", "qing-dynasty", "seleucid-dynasty", "umayyad-caliphate", "safavid-empire", "timurid-dynasty", "pallava-dynasty", "zhou-dynasty", "ghaznavids", "khalji-dynasty", "keita-dynasty", "macedonian-dynasty", "kushan-empire-india", "abbadid-dynasty", "abydos-dynasty", "aeacidae", "yuan-dynasty", "almohad-caliphate", "ahom-dynasty", "chakri-dynasty", "tudor-period", "delhi-sultanate-afghanistan", "inca-empire-argentina", "sassanid-empire-iran", "hittite-empire", "lombard-kingdom", "vandal-kingdom", "arsacid-dynasty-of-parthia", "inca-empire-bolivia", "adal-sultanate", "aftasid-dynasty", "ajuran-empire", "al-bu-said-dynasty", "alawi-dynasty", "amarna-period", "amorian-dynasty", "ancient-china", "al-rashid", "al-fayez", "alids",
    "african-national-congress", "aam-aadmi-party", "chinese-communist-party", "bharatiya-janata-party", "amal-movement", "alliance-90the-greens", "all-progressives-congress", "conservative-party", "labour-party", "kuomintang", "republican-party", "national-rally", "social-democratic-party-of-germany", "communist-party-of-india", "inkatha-freedom-party", "national-front", "democratic-party", "libertarian-party", "workers-party", "freedom-party", "peoples-party", "green-party", "justice-and-development-party", "progressive-party", "fianna-fáil", "fine-gael", "sinn-féin", "vox", "baath-party", "brothers-of-italy", "ciudadanos", "forza-italya", "communist-party-of-cuba", "communist-party-of-vietnam", "a-just-russia", "la-france-insoumise", "podemos", "united-russia", "pirate-party", "green-party-of-the-united-states",
    "apple-inc", "amazon", "alphabet-inc", "adobe", "alibaba-group", "baidu", "microsoft", "nvidia", "bank-of-america", "jpmorgan-chase", "goldman-sachs", "hsbc", "deutsche-bank", "barclays", "bnp-paribas", "wells-fargo", "mcdonalds", "nike", "the-coca-cola-company", "the-walt-disney-company", "volkswagen-group", "general-motors", "ford-motor-company", "general-electric", "shell", "exxonmobil", "pfizer", "boeing", "intel", "cisco", "oracle-corporation", "lockheed-martin", "british-airways", "lufthansa", "delta-air-lines", "aeroflot", "air-canada", "american-airlines", "att", "audi-ag", "citibank", "ubs", "unicredit", "credit-suisse", "standard-chartered", "credit-agricole-group", "banco-santander", "bank-of-amsterdam", "bank-of-ireland", "bank-of-italy", "bank-of-scotland", "bank-of-india", "bank-of-montreal", "bank-of-russia", "bank-of-baroda", "banca-monte-dei-paschi-di-siena", "abn-amro", "allied-irish-banks", "alfa-bank", "asian-development-bank", "axis-bank", "banco-ambrosiano", "bank-hapoalim-bm", "bank-leumi-le-israel-bm", "adidas-ag", "ab-volvo", "aston-martin-lagonda", "nissan", "sony-group", "unilever", "prada", "panasonic-holdings-corporation", "dutch-east-india-company", "hyundai-motor-company", "suzuki-motor-corporation", "honda", "china-construction-bank", "sberbank", "ibm", "allianz-trade", "bayer", "canon-inc", "caixabank", "banco-bilbao-vizcaya-argentaria", "alpha-bank", "australia-and-new-zealand-banking-group", "british-south-africa-company", "sumitomo-mitsui-financial-group",
    "al-azhar-al-sharif", "african-methodist-episcopal-church", "coptic-orthodox-church", "eastern-orthodox-church", "buddhist-association-of-china", "evangelical-lutheran-church-in-america", "catholic-church-in-brazil", "armenian-evangelical-church", "church-of-england", "methodist-church-of-great-britain", "methodist-episcopal-church", "presbyterian-church", "the-church-of-jesus-christ-of-latter-day-saints", "greek-orthodoxy", "sufism", "anglican-communion", "church-of-norway", "church-of-sweden", "church-of-ireland", "assemblies-of-god", "church-of-god-in-christ", "church-of-iceland", "church-of-nigeria", "church-of-north-india",
    "aachen-cathedral", "notre-dame-de-chartres", "cologne-cathedral", "milan-cathedral", "florence-cathedral", "bath-abbey", "notre-dame-de-paris", "york-minster", "abbey-of-st-victor", "hagia-sophia-church", "st-pauls-cathedral", "notre-dame-cathedral", "orvieto-cathedral", "ravenna-cathedral", "notre-dame-cathedral-basilica", "st-paulus-dom", "sacré-cœur", "ulm-minster", "seville-cathedral", "albi-cathedral", "notre-dame-de-la-garde", "saint-patricks-cathedral", "st-stephens-basilica", "basilica-of-bom-jesus", "cathedral-of-the-immaculate-conception", "basilica-of-notre-dame-de-fourvière", "crystal-cathedral", "amalfi-cathedral", "anagni-cathedral", "angers-cathedral", "assisi-cathedral", "cremona-cathedral",
    "al-aqsa-mosque", "al-azhar-mosque", "blue-mosque", "sultan-ahmed-mosque", "umayyad-mosque", "hassan-ii-mosque", "jama-masjid-delhi", "dome-of-the-rock", "istiqlal-mosque", "suleymaniye-mosque", "badshahi-mosque", "wazir-khan-mosque", "fatih-mosque", "grand-mosque-of-paris", "faisal-mosque", "al-azhar-great-mosque", "al-masjid-al-haram", "grand-mosque", "mosque-of-amr-ibn-al-as", "mosque-of-ibn-tulun", "nasir-ol-molk-mosque", "sheikh-zayed-mosque", "great-mosque-of-kairouan", "koutoubia-mosque",
    "ajanta-caves", "borobudur-temple-compounds", "fushimi-inari-taisha", "mahabodhi-temple", "shwedagon-pagoda", "temple-of-heaven", "akshardham", "a-ma-temple",
    "clairvaux-abbey", "cluny-abbey", "einsiedeln-abbey", "fountains-abbey", "glastonbury-abbey", "melk-abbey", "mont-saint-michel-abbey", "tintern-abbey", "iona-abbey", "rievaulx-abbey", "whitby-abbey", "ampleforth-abbey", "bury-st-edmunds-abbey", "byland-abbey", "jervaulx-abbey", "klosterneuburg-monastery",
    "acropolis-museum", "american-museum-of-natural-history", "hermitage-museum", "guggenheim-museum-bilbao", "angkor-national-museum", "national-gallery-of-canada", "chicago-history-museum", "academy-museum-of-motion-pictures", "smithsonian-institution", "natural-history-museum", "palace-museum", "field-museum-of-natural-history", "national-museum-of-anthropology", "natural-history-museum-vienna", "natural-history-museum-of-los-angeles-county", "science-museum", "anne-frank-house", "jewish-museum", "national-museum-of-history", "hiroshima-peace-memorial-museum", "nagasaki-atomic-bomb-museum", "auschwitz", "imperial-war-museum-london", "national-war-museum",
    "globe-theatre", "la-scala", "mariinsky-theatre", "metropolitan-opera-house", "carnegie-hall", "royal-opera-house", "apollo-theater", "radio-city-music-hall", "almeida-theatre", "royal-shakespeare-theatre", "royal-court-theatre", "bolshoi-kamenny-theatre", "vienna-state-opera-house", "palace-theatre", "theater-an-der-wien", "theater-am-schiffbauerdamm", "national-theatre", "palais-garnier", "broadway-theatre", "edinburgh-festival-theatre", "lyceum-theatre", "aldwych-theatre", "donmar-warehouse", "odeon-of-domitian",
    "20th-century-studios", "columbia-pictures", "dreamworks", "miramax", "new-line-cinema", "paramount-pictures", "pixar", "sony-pictures", "fox-film-corporation", "harper", "mgm-records", "oxford-university-press", "penguin-books", "random-house", "simon-schuster", "universal-music-group-nashville", "hbo", "lionsgate-films", "universal-pictures", "warner-bros-entertainment", "national-geographic-society", "showtime", "touchstone-pictures", "bbc-film",
    "harvard-university", "princeton-university", "stanford-university", "yale-university", "sorbonne", "nalanda-university", "humboldt-university-berlin", "university-of-oxford", "brown-university", "columbia-university", "cornell-university", "dartmouth-college", "duke-university", "ghent-university", "aarhus-university", "the-rockefeller-university", "massachusetts-institute-of-technology", "eth-zurich", "university-of-chicago", "peking-university", "california-institute-of-technology", "carnegie-mellon-university", "university-of-melbourne", "university-of-bologna", "new-york-university", "university-of-pennsylvania", "rice-university", "emory-university", "tufts-university", "vanderbilt-university", "georgetown-university", "university-of-paris"
])

CLASSES = {
    "312": "data/appwrite-export/entities/312-Class-312",
    "316": "data/appwrite-export/entities/316-Class-316", 
    "330": "data/appwrite-export/entities/330-Class-330",
    "340": "data/appwrite-export/entities/340-Class-340",
    "341": "data/appwrite-export/entities/341-Class-341",
    "342": "data/appwrite-export/entities/342-Class-342",
    "343": "data/appwrite-export/entities/343-Class-343",
    "344": "data/appwrite-export/entities/344-Class-344",
    "361": "data/appwrite-export/entities/361-Class-361",
    "363": "data/appwrite-export/entities/363-Class-363",
    "364": "data/appwrite-export/entities/364-Class-364",
    "381": "data/appwrite-export/entities/381-Class-381",
    "311": "data/appwrite-export/entities/311-Class-311",
    "350": "data/appwrite-export/entities/350-Class-350",
    "370": "data/appwrite-export/entities/370-Class-370",
}

results = []
for cls_id, path in CLASSES.items():
    if not os.path.exists(path): continue
    cls_count = 0
    # Process up to 1000 files to find matches
    for fname in sorted(os.listdir(path)):
        if not fname.endswith('.json'): continue
        # Extract slug correctly by removing prefix
        slug = fname[len(cls_id):-5].lstrip('-')
        if slug in USED: continue
        
        try:
            with open(os.path.join(path, fname)) as f:
                d = json.load(f)
                e = d['entities'][0]
                name = e.get('name','')
                summary = e.get('summary','')
                slen = len(summary) if summary else 0
                has_sig = bool(e.get('historicalSignificance'))
                
                if not has_sig or slen < 400:
                    results.append(f"{cls_id}|{slug}|{name}|{slen}")
                    cls_count += 1
                    if len(results) >= 420: break 
        except Exception: pass
        if len(results) >= 420: break

for r in results:
    print(r)

print("---350 and 370 samples---")
for c in ["350", "370"]:
    p = CLASSES[c]
    if os.path.exists(p):
        print(f"Class {c}: " + ", ".join(sorted(os.listdir(p))[:10]))
