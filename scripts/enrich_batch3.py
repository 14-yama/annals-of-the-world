#!/usr/bin/env python3
"""
Batch 3: Enrich 20 existing entities + create 12 new ones.
"""
import json, glob, os

BASE = "data/appwrite-export/entities"

def rel(src_slug, src_name, verb, tgt_slug, tgt_name, ctx=""):
    return {"sourceSlug": src_slug, "sourceName": src_name, "verb": verb,
            "targetSlug": tgt_slug, "targetName": tgt_name, "context": ctx}

# ─── ENRICHMENTS: existing entities with weak summaries ───

ENRICHMENTS = {
    "pythagoras": {
        "summary": "Pythagoras of Samos (c. 570–495 BCE) was a Greek philosopher and mathematician whose ideas profoundly shaped Western thought. He founded a religious-philosophical brotherhood in Croton, southern Italy, that combined rigorous mathematical inquiry with mystical beliefs about the harmony of the cosmos.\n\nBest known for the Pythagorean theorem (a² + b² = c²), Pythagoras pioneered the concept that numbers underlie all reality. His school discovered irrational numbers, musical harmonics based on numerical ratios, and the idea that celestial bodies produce a 'music of the spheres.'\n\nHis influence extended far beyond mathematics — Pythagorean ideas about transmigration of souls, vegetarianism, and communal living anticipated later philosophical and religious movements. Plato, Copernicus, and Kepler all drew on Pythagorean cosmology.",
        "causes": ["Pre-Socratic inquiry into nature of reality", "Egyptian and Babylonian mathematical traditions", "Greek colonization of southern Italy"],
        "effects": ["Foundation of mathematical proof as a method", "Platonic philosophy adopts Pythagorean number theory", "Musical theory based on mathematical ratios", "Western tradition linking mathematics to cosmic order", "Influence on Copernican heliocentric model", "Vegetarian and communal living movements"],
        "relationships": [
            rel("pythagoras","Pythagoras","INFLUENCES","plato","Plato","Pythagorean number mysticism shaped Plato's Theory of Forms"),
            rel("pythagoras","Pythagoras","INFLUENCES","copernicus","Copernicus","Pythagorean cosmic harmony inspired heliocentric thinking"),
            rel("pythagoras","Pythagoras","DEFINES","pythagoras","Mathematical Proof","Established deductive proof as foundation of mathematics"),
            rel("pythagoras","Pythagoras","OCCURS_IN","croton-italy","Croton, Italy","Founded Pythagorean school in Magna Graecia"),
            rel("pythagoras","Pythagoras","TRANSMITS","aristotle","Aristotle","Pythagorean ideas transmitted through Aristotle's critiques")
        ]
    },
    "ramesses-ii": {
        "summary": "Ramesses II (c. 1303–1213 BCE), also known as Ramesses the Great, was the third pharaoh of the Nineteenth Dynasty of Egypt and arguably the most powerful ruler of the ancient world. His 66-year reign (1279–1213 BCE) was the second longest in Egyptian history.\n\nHe fought the Hittites at the Battle of Kadesh (1274 BCE) — one of the largest chariot battles ever — and negotiated the world's first known peace treaty (1259 BCE). He launched massive building campaigns: Abu Simbel's colossal temples, the Ramesseum, and expansions at Karnak and Luxor.\n\nWith over 100 children and a vast empire stretching from Nubia to Syria, Ramesses II embodied Egyptian imperial power at its zenith. His mummy, rediscovered in 1881, remains one of the best-preserved royal remains in history.",
        "causes": ["Nineteenth Dynasty military ambitions", "Hittite expansionism threatening Egyptian border", "Egyptian monumental building tradition"],
        "effects": ["World's first recorded peace treaty with Hittites", "Abu Simbel temples as UNESCO World Heritage site", "Model for pharaonic absolute power", "Egyptian cultural golden age in arts and architecture", "Diplomatic precedent for international treaties", "Lasting influence on Egyptian national identity"],
        "relationships": [
            rel("ramesses-ii","Ramesses II","CAUSES","abu-simbel","Abu Simbel","Commissioned the rock-cut temples at Abu Simbel"),
            rel("ramesses-ii","Ramesses II","DEFINES","kadesh","Battle of Kadesh","Led largest chariot battle in history, 1274 BCE"),
            rel("ramesses-ii","Ramesses II","OCCURS_IN","thebes","Thebes","Capital of New Kingdom Egypt during his reign"),
            rel("ramesses-ii","Ramesses II","TRANSFORMS","egypt","Egypt","Expanded Egypt's borders and monumental architecture"),
            rel("moses","Moses","OCCURS_DURING","ramesses-ii","Ramesses II","Traditional identification as pharaoh of the Exodus")
        ]
    },
    "hammurabi": {
        "summary": "Hammurabi (c. 1810–1750 BCE) was the sixth king of the First Babylonian Dynasty who transformed a minor city-state into one of the most powerful empires in the ancient Near East. His 42-year reign (c. 1792–1750 BCE) established Babylon as the cultural and political center of Mesopotamia.\n\nHe is best known for the Code of Hammurabi — 282 laws inscribed on a black diorite stele, now in the Louvre. These laws covered commerce, property, family, and criminal justice with the principle of 'an eye for an eye.' It was not the first law code but the most complete and influential of the ancient world.\n\nHammurabi's legacy extends beyond law: he unified Mesopotamia, established Marduk as the supreme deity of Babylon, and created administrative systems that influenced governance for millennia. His code became a model for later legal traditions including Mosaic law.",
        "causes": ["Amorite migration into Mesopotamia", "Sumerian legal tradition (Code of Ur-Nammu)", "Political fragmentation of post-Ur III Mesopotamia"],
        "effects": ["Unification of Mesopotamia under Babylon", "Codification of law as governance principle", "Establishment of Marduk as supreme deity", "Influence on Mosaic and later legal codes", "Model for centralized imperial administration", "Precedent for written constitutionalism"],
        "relationships": [
            rel("hammurabi","Hammurabi","DEFINES","hammurabi","Code of Hammurabi","Created 282 laws governing Babylonian society"),
            rel("hammurabi","Hammurabi","TRANSFORMS","babylon","Babylon","Elevated from city-state to regional empire"),
            rel("hammurabi","Hammurabi","INFLUENCES","moses","Moses","Hammurabi's code influenced Mosaic legal tradition"),
            rel("hammurabi","Hammurabi","OCCURS_IN","babylon","Babylon","Ruled from Babylon for 42 years"),
            rel("hammurabi","Hammurabi","CAUSES","marduk","Marduk Worship","Established Marduk as chief deity of Babylonian pantheon")
        ]
    },
    "peter-the-great": {
        "summary": "Peter I (1672–1725), known as Peter the Great, was Tsar and first Emperor of Russia who single-handedly dragged his nation from medieval isolation into European modernity. His reign (1682–1725) was the most transformative in Russian history.\n\nAfter his famous 'Grand Embassy' tour of Western Europe (1697–1698) — where he worked incognito in Dutch shipyards — Peter modernized Russia's military, founded the Russian Navy, reformed the Orthodox Church, and imposed Western dress on the nobility. He built Saint Petersburg from scratch on swampland as Russia's 'Window on the West.'\n\nHis victory over Sweden at Poltava (1709) established Russia as a great European power. Peter's ruthless reforms — including taxing beards, executing the Streltsy, and even condemning his own son to death — exemplified his conviction that progress required absolute authority.",
        "causes": ["Russian military defeats by Ottoman Empire and Sweden", "Influence of Western European visitors in Moscow", "Personal curiosity during Grand Embassy to Europe (1697–1698)"],
        "effects": ["Foundation of Saint Petersburg (1703)", "Creation of the Russian Navy", "Russia's emergence as European great power after Poltava", "Westernization of Russian aristocracy and government", "Abolition of the Patriarchate; state control of Church", "Table of Ranks meritocratic system"],
        "relationships": [
            rel("peter-the-great","Peter the Great","CAUSES","saint-petersburg","Saint Petersburg","Founded Russia's new capital on the Neva, 1703"),
            rel("peter-the-great","Peter the Great","TRANSFORMS","russia","Russia","Westernized military, government, and culture"),
            rel("peter-the-great","Peter the Great","DEFINES","poltava","Battle of Poltava","Decisively defeated Sweden, 1709"),
            rel("peter-the-great","Peter the Great","INFLUENCES","catherine-the-great","Catherine the Great","Continued Peter's modernization program"),
            rel("peter-the-great","Peter the Great","OCCURS_IN","moscow","Moscow","Ruled Russia from Moscow before founding Petersburg")
        ]
    },
    "suleiman-the-magnificent": {
        "summary": "Suleiman I (1494–1566), known in the West as 'the Magnificent' and in Islam as 'the Lawgiver' (Kanuni), presided over the Ottoman Empire at the height of its power. His 46-year reign (1520–1566) was the longest and most glorious in Ottoman history.\n\nHe conquered Belgrade (1521), Rhodes (1522), and much of Hungary after the Battle of Mohács (1526). His navy under Hayreddin Barbarossa dominated the Mediterranean. At home, he reformed the legal system, patronized architecture (the Süleymaniye Mosque by Sinan remains Istanbul's masterpiece), and oversaw a golden age of Ottoman arts and literature.\n\nSuleiman's empire stretched from Algeria to Iraq, from Hungary to Yemen — governing over 25 million people. His partnership with Grand Vizier Ibrahim Pasha and his legendary love for Hürrem Sultan (Roxelana) shaped both politics and palace culture for generations.",
        "causes": ["Ottoman military dominance inherited from Selim I", "Mature administrative system from Mehmed II's reforms", "Christian Europe weakened by internal divisions"],
        "effects": ["Ottoman Empire's territorial zenith — 3 continents", "Kanuni legal code governing Ottoman society for centuries", "Süleymaniye Mosque as pinnacle of Islamic architecture", "Ottoman Mediterranean dominance under Barbarossa", "Precedent of royal consort (Hürrem Sultan) influencing politics", "Long decline after his death — 'post-Suleimanic' period"],
        "relationships": [
            rel("suleiman-the-magnificent","Suleiman","TRANSFORMS","ottoman-empire","Ottoman Empire","Brought empire to territorial and cultural zenith"),
            rel("suleiman-the-magnificent","Suleiman","DEFINES","mohacs","Battle of Mohács","Destroyed Hungarian kingdom, 1526"),
            rel("suleiman-the-magnificent","Suleiman","CAUSES","suleymaniye","Süleymaniye Mosque","Commissioned masterwork of architect Sinan"),
            rel("suleiman-the-magnificent","Suleiman","OCCURS_IN","istanbul","Istanbul","Ruled from Topkapi Palace for 46 years"),
            rel("suleiman-the-magnificent","Suleiman","INFLUENCES","ottoman-law","Ottoman Legal System","Kanuni reforms governed empire for centuries")
        ]
    },
    "joseph-stalin": {
        "summary": "Joseph Stalin (1878–1953) was the dictator of the Soviet Union from 1924 to 1953 whose rule combined rapid industrialization with unprecedented political terror. Born Ioseb Jughashvili in Georgia, he rose through Bolshevik ranks to succeed Lenin and reshape the USSR.\n\nHis Five-Year Plans transformed the Soviet Union from an agrarian society into an industrial superpower, but at catastrophic human cost. Forced collectivization caused the Holodomor famine in Ukraine (1932–33), killing millions. The Great Purge (1936–38) eliminated perceived enemies through show trials and mass executions — an estimated 750,000 executed, millions more sent to the Gulag.\n\nStalin led the Soviet Union to victory over Nazi Germany in World War II, at the cost of 27 million Soviet lives. His postwar expansion into Eastern Europe initiated the Cold War. 'One death is a tragedy; a million deaths is a statistic' — a quote attributed to him that captures the chilling calculus of his rule.",
        "causes": ["Bolshevik Revolution and Civil War chaos", "Lenin's death and power vacuum in 1924", "Russian imperial tradition of autocratic rule"],
        "effects": ["Soviet industrialization — second largest economy by 1940", "Holodomor and forced collectivization famines", "Great Purge — destruction of Old Bolsheviks and military leadership", "Soviet victory in WWII at cost of 27 million lives", "Cold War division of Europe", "Gulag system imprisoning millions"],
        "relationships": [
            rel("joseph-stalin","Joseph Stalin","TRANSFORMS","soviet-union","Soviet Union","Industrialized USSR through Five-Year Plans"),
            rel("joseph-stalin","Joseph Stalin","CAUSES","cold-war","Cold War","Soviet expansion into Eastern Europe triggered Cold War"),
            rel("joseph-stalin","Joseph Stalin","OCCURS_IN","moscow","Moscow","Ruled from the Kremlin for 29 years"),
            rel("joseph-stalin","Joseph Stalin","INFLUENCES","mao-zedong","Mao Zedong","Stalinist model influenced Chinese communism"),
            rel("adolf-hitler","Adolf Hitler","CAUSES","joseph-stalin","Joseph Stalin","Nazi invasion forced Stalin into WWII alliance with West")
        ]
    },
    "mao-zedong": {
        "summary": "Mao Zedong (1893–1976) was the founding chairman of the People's Republic of China whose revolutionary vision reshaped the most populous nation on Earth. A peasant's son from Hunan province, he merged Marxism-Leninism with Chinese agrarian revolution to create 'Maoism.'\n\nHe led the Chinese Communist Party through the Long March (1934–35), the war against Japan, and civil war against Chiang Kai-shek's Nationalists, proclaiming the People's Republic on October 1, 1949. His rule brought land reform and literacy campaigns but also catastrophic failures: the Great Leap Forward (1958–62) caused a famine killing 15–55 million people.\n\nThe Cultural Revolution (1966–76) unleashed Red Guards against 'bourgeois elements,' devastating China's intellectual and cultural life. Yet Mao also normalized relations with the US (Nixon's 1972 visit) and remains a deeply complex figure — revered as China's liberator, condemned for its worst peacetime catastrophe.",
        "causes": ["May Fourth Movement and anti-imperialism", "Marxist-Leninist ideology adapted to peasant revolution", "Japanese invasion and Chinese Civil War"],
        "effects": ["Founding of People's Republic of China (1949)", "Great Leap Forward famine — 15–55 million dead", "Cultural Revolution — decade of political chaos", "US-China rapprochement (1972)", "Maoist ideology inspiring Third World revolutions", "Foundation for Deng Xiaoping's economic reforms"],
        "relationships": [
            rel("mao-zedong","Mao Zedong","TRANSFORMS","china","China","Established People's Republic, restructured Chinese society"),
            rel("mao-zedong","Mao Zedong","INFLUENCES","ho-chi-minh","Ho Chi Minh","Maoist guerrilla strategy adopted in Vietnam"),
            rel("joseph-stalin","Joseph Stalin","INFLUENCES","mao-zedong","Mao Zedong","Soviet model shaped early PRC policies"),
            rel("mao-zedong","Mao Zedong","OCCURS_IN","beijing","Beijing","Ruled from Zhongnanhai for 27 years"),
            rel("mao-zedong","Mao Zedong","CAUSES","cultural-revolution","Cultural Revolution","Launched decade-long political upheaval, 1966–76")
        ]
    },
    "voltaire": {
        "summary": "Voltaire (1694–1778), born François-Marie Arouet, was the most influential writer of the European Enlightenment — a philosopher, historian, satirist, and tireless advocate for civil liberties, freedom of religion, and separation of church and state.\n\nHis satirical masterpiece 'Candide' (1759) lampooned philosophical optimism with savage wit. His 'Letters on the English' (1733) introduced French readers to Newton, Locke, and British parliamentary government, igniting reform movements across Europe. Twice imprisoned in the Bastille and repeatedly exiled, he wielded his pen as a weapon against tyranny and superstition.\n\n'I disapprove of what you say, but I will defend to the death your right to say it' — while likely apocryphal, this captures Voltaire's legacy as champion of free expression. His ideas directly shaped the American and French Revolutions.",
        "causes": ["French absolutism under Louis XIV and XV", "Newton's scientific revolution and British empiricism", "Personal experience of royal persecution and imprisonment"],
        "effects": ["Intellectual foundation for the French Revolution", "Advancement of religious tolerance in Europe", "Popularization of Newtonian science on the continent", "Influence on American founding fathers (Jefferson, Franklin)", "Modern concept of freedom of expression", "Model of the public intellectual engaging in political discourse"],
        "relationships": [
            rel("voltaire","Voltaire","INFLUENCES","french-revolution","French Revolution","Enlightenment ideas fueled revolutionary ideology"),
            rel("voltaire","Voltaire","TRANSMITS","isaac-newton","Isaac Newton","Popularized Newtonian physics in France"),
            rel("voltaire","Voltaire","INFLUENCES","thomas-jefferson","Thomas Jefferson","Shaped Jefferson's views on religious freedom"),
            rel("voltaire","Voltaire","OCCURS_IN","paris","Paris","Lived and wrote in Paris, imprisoned in the Bastille"),
            rel("john-locke","John Locke","INFLUENCES","voltaire","Voltaire","Locke's empiricism shaped Voltaire's philosophy")
        ]
    },
    "immanuel-kant": {
        "summary": "Immanuel Kant (1724–1804) was a German philosopher whose 'Critique of Pure Reason' (1781) is arguably the most important work in modern philosophy. Born and dying in Königsberg, Prussia — which he never left — he revolutionized epistemology, ethics, and aesthetics from his study.\n\nKant resolved the empiricism-rationalism debate by arguing that the mind actively structures experience through innate categories (space, time, causality). His 'categorical imperative' — act only according to rules you could will as universal laws — became the foundation of deontological ethics.\n\nHis 'Perpetual Peace' (1795) proposed a federation of free states and international law — anticipating the United Nations by 150 years. Kant's three Critiques (Pure Reason, Practical Reason, Judgment) remain the towering architecture of Western philosophy, influencing everything from human rights theory to cognitive science.",
        "causes": ["Hume's skepticism 'awakened Kant from dogmatic slumber'", "Leibniz-Wolff rationalist tradition in German universities", "Newtonian physics and its philosophical implications"],
        "effects": ["Foundation of modern epistemology (transcendental idealism)", "Categorical imperative as basis for deontological ethics", "Influence on German Idealism (Hegel, Fichte, Schelling)", "Perpetual Peace anticipating international organizations", "Human rights philosophy grounded in rational dignity", "Cognitive science's debt to Kantian categories"],
        "relationships": [
            rel("immanuel-kant","Immanuel Kant","INFLUENCES","hegel","G.W.F. Hegel","Kant's philosophy provoked Hegel's dialectical response"),
            rel("immanuel-kant","Immanuel Kant","DEFINES","epistemology","Epistemology","Transcendental idealism redefined the theory of knowledge"),
            rel("david-hume","David Hume","INFLUENCES","immanuel-kant","Immanuel Kant","Hume's skepticism inspired the Critique of Pure Reason"),
            rel("immanuel-kant","Immanuel Kant","OCCURS_IN","konigsberg","Königsberg","Never left his hometown in 80 years of life"),
            rel("immanuel-kant","Immanuel Kant","INFLUENCES","united-nations","United Nations","Perpetual Peace anticipated international federation")
        ]
    },
    "rumi": {
        "summary": "Jalal ad-Din Muhammad Rumi (1207–1273) was a 13th-century Persian poet, Sufi mystic, and Islamic scholar whose poetry transcends language, culture, and religion. Born in Balkh (present-day Afghanistan), he settled in Konya (present-day Turkey) where he composed the 'Masnavi' — a 25,000-verse epic called 'the Quran in Persian.'\n\nHis transformative encounter with the wandering dervish Shams-i-Tabrizi in 1244 ignited his poetic genius. After Shams's mysterious disappearance, Rumi poured his grief and spiritual ecstasy into the 'Divan-i-Shams-i-Tabrizi,' one of the greatest collections of mystical love poetry ever written.\n\nRumi founded the Mevlevi Order — the 'Whirling Dervishes' — whose spinning meditation ceremony (sema) became a UNESCO Intangible Cultural Heritage. In the 21st century, Rumi is the best-selling poet in the United States, his verses on love and unity resonating across every boundary he would have wished dissolved.",
        "causes": ["Sufi mystical tradition within Islam", "Encounter with Shams-i-Tabrizi (1244)", "Persian literary tradition from Ferdowsi to Attar"],
        "effects": ["Mevlevi Order (Whirling Dervishes) founded in Konya", "Masnavi as foundational text of Sufi literature", "Best-selling poet in 21st-century America", "UNESCO recognition of Sema ceremony", "Cross-cultural bridge between Islamic and Western spirituality", "Influence on Sufi orders across the Islamic world"],
        "relationships": [
            rel("rumi","Rumi","DEFINES","mevlevi","Mevlevi Order","Founded the Whirling Dervishes spiritual order"),
            rel("rumi","Rumi","OCCURS_IN","konya","Konya","Lived and taught in Seljuk Konya for decades"),
            rel("rumi","Rumi","TRANSMITS","shams-tabrizi","Shams-i-Tabrizi","Shams catalyzed Rumi's poetic awakening"),
            rel("rumi","Rumi","INFLUENCES","sufi-tradition","Sufi Tradition","Masnavi became cornerstone of Sufi thought"),
            rel("attar","Attar of Nishapur","INFLUENCES","rumi","Rumi","Attar's mystical poetry inspired Rumi's path")
        ]
    },
    "avicenna": {
        "summary": "Ibn Sina (c. 980–1037), known in the West as Avicenna, was a Persian polymath who composed over 450 works on philosophy, medicine, astronomy, and theology. He was the most influential philosopher-scientist of the Islamic Golden Age and one of the most significant thinkers in human history.\n\nHis 'Canon of Medicine' (al-Qanun fi al-Tibb) served as the standard medical textbook in both Islamic and European universities for over 500 years — longer than any other medical text. It systematized Greek, Roman, and Islamic medical knowledge into a coherent framework covering anatomy, pharmacology, and clinical practice.\n\nHis philosophical magnum opus, 'The Book of Healing' (Kitab al-Shifa), fused Aristotelian philosophy with Islamic theology and independently anticipated several modern philosophical arguments. Avicenna's 'flying man' thought experiment — imagining consciousness without sensory input — prefigured Descartes' cogito by six centuries.",
        "causes": ["Islamic Golden Age fostering scholarship", "Greek philosophical and medical texts preserved in Arabic translation", "Samanid court patronage of learning in Central Asia"],
        "effects": ["Canon of Medicine dominating medical education for 500 years", "Synthesis of Aristotelian philosophy with Islamic thought", "Influence on Scholastic philosophy (Thomas Aquinas, Duns Scotus)", "'Flying man' thought experiment anticipating Cartesian doubt", "Standardization of pharmacological classification", "Foundation for evidence-based clinical medicine"],
        "relationships": [
            rel("avicenna","Avicenna","INFLUENCES","thomas-aquinas","Thomas Aquinas","Scholastic philosophy incorporated Avicenna's metaphysics"),
            rel("avicenna","Avicenna","DEFINES","canon-of-medicine","Canon of Medicine","Standard medical text for 500 years"),
            rel("aristotle","Aristotle","INFLUENCES","avicenna","Avicenna","Aristotelian philosophy formed Avicenna's framework"),
            rel("avicenna","Avicenna","INFLUENCES","descartes","René Descartes","Flying man anticipated cogito ergo sum"),
            rel("avicenna","Avicenna","OCCURS_IN","bukhara","Bukhara","Educated and first practiced medicine in Bukhara")
        ]
    },
    "ibn-khaldun": {
        "summary": "Ibn Khaldun (1332–1406) was a North African Arab historian, sociologist, and philosopher who wrote the 'Muqaddimah' — widely considered the first work of sociology, historiography, and economics. Born in Tunis to an elite Andalusian family, he served as diplomat and judge across the Maghreb, al-Andalus, and Mamluk Egypt.\n\nThe Muqaddimah (1377) introduced the concept of 'asabiyyah' (social cohesion/group solidarity) as the driving force of civilization. He argued that dynasties follow a cyclical pattern — nomadic groups with strong asabiyyah conquer settled peoples, then lose cohesion through luxury, falling to the next wave. This framework predated modern cycle-of-civilization theories by centuries.\n\nHis empirical approach to history — rejecting myths, analyzing causes, studying economics and climate — earned him recognition as 'the father of sociology.' Arnold Toynbee called the Muqaddimah 'the greatest work of its kind that has ever been created by any mind in any time or place.'",
        "causes": ["Decline of the Almohad and Marinid dynasties in North Africa", "Personal experience serving multiple courts and witnessing regime changes", "Greek and Islamic historiographical traditions"],
        "effects": ["Foundation of sociology as a discipline", "Cyclical theory of civilizations (asabiyyah)", "Empirical approach to historiography", "Influence on Toynbee, Gellner, and modern social science", "Economic theory of labor, taxation, and market dynamics", "Precursor to modern political economy"],
        "relationships": [
            rel("ibn-khaldun","Ibn Khaldun","DEFINES","muqaddimah","Muqaddimah","Foundational work of sociology and historiography"),
            rel("ibn-khaldun","Ibn Khaldun","INFLUENCES","toynbee","Arnold Toynbee","Toynbee called the Muqaddimah the greatest of its kind"),
            rel("ibn-khaldun","Ibn Khaldun","OCCURS_IN","tunis","Tunis","Born and educated in Tunis"),
            rel("ibn-khaldun","Ibn Khaldun","OCCURS_IN","cairo","Cairo","Served as judge in Mamluk Egypt"),
            rel("ibn-khaldun","Ibn Khaldun","INFLUENCES","adam-smith","Adam Smith","Labor theory of value anticipated by Ibn Khaldun")
        ]
    },
    "akbar": {
        "summary": "Akbar the Great (1542–1605), born Jalal-ud-din Muhammad Akbar, was the third Mughal Emperor who transformed India's most powerful dynasty from a Central Asian conquest state into a genuinely Indian empire. His 49-year reign (1556–1605) was the longest and most consequential in Mughal history.\n\nAscending the throne at age 13, Akbar consolidated power through military brilliance and revolutionary statecraft. His policy of 'sulh-i-kul' (universal peace) promoted religious tolerance among Hindus, Muslims, Jains, Christians, and Zoroastrians. He abolished the discriminatory jizya tax on non-Muslims, married Rajput princesses, and created a syncretic 'Divine Faith' (Din-i-Ilahi).\n\nHis mansabdari system of ranked military-civil officials, revenue reforms under Todar Mal, and patronage of arts (the Mughal school of miniature painting) created a cultural golden age. Fatehpur Sikri and the Agra Fort stand as monuments to his vision of imperial grandeur tempered by pluralism.",
        "causes": ["Mughal military tradition from Babur and Humayun", "Indian subcontinent's religious diversity demanding tolerance", "Revenue crisis requiring administrative reform"],
        "effects": ["Religious tolerance policy (sulh-i-kul) ahead of its time", "Mughal administrative system lasting until British Raj", "Golden age of Mughal art, architecture, and literature", "Precedent for secular governance in religiously diverse states", "Fatehpur Sikri as architectural wonder of syncretic design", "Foundation for 200 years of Mughal imperial power"],
        "relationships": [
            rel("akbar","Akbar","TRANSFORMS","mughal-empire","Mughal Empire","Transformed conquest state into Indian empire"),
            rel("akbar","Akbar","DEFINES","fatehpur-sikri","Fatehpur Sikri","Built syncretic capital city near Agra"),
            rel("akbar","Akbar","INFLUENCES","shah-jahan","Shah Jahan","Grandson continued Mughal architectural patronage"),
            rel("akbar","Akbar","OCCURS_IN","agra","Agra","Primary capital and site of Agra Fort"),
            rel("babur","Babur","CAUSES","akbar","Akbar","Mughal dynasty founded by Babur enabled Akbar's reign")
        ]
    },
    "tamerlane": {
        "summary": "Timur (1336–1405), known in the West as Tamerlane (from Timur-i-lang, 'Timur the Lame'), was a Turco-Mongol conqueror who built the last great nomadic empire, stretching from Delhi to Damascus to the Russian steppe. Born near Samarkand, he claimed descent from Genghis Khan's lineage.\n\nHis military campaigns were devastating in scale: the sack of Delhi (1398) killed an estimated 100,000 captives in a single day; the sieges of Baghdad, Aleppo, and Damascus left pyramids of skulls. He defeated the Ottoman Sultan Bayezid I at Ankara (1402), temporarily saving Constantinople from Ottoman conquest.\n\nYet Timur was also a patron of art and architecture. He made Samarkand one of the most magnificent cities in the world, building the Registan, Bibi-Khanym Mosque, and the Gur-e-Amir (his own mausoleum). His dynasty, the Timurids, produced a cultural renaissance in Central Asia and Persia that rivaled Renaissance Italy.",
        "causes": ["Mongol imperial tradition and Chagatai Khanate fragmentation", "Central Asian nomadic military culture", "Personal ambition modeled on Genghis Khan"],
        "effects": ["Devastation of Delhi Sultanate and Middle Eastern cities", "Temporary halt of Ottoman expansion after Ankara (1402)", "Timurid Renaissance in Central Asian art and architecture", "Samarkand as world cultural capital", "Mughal Empire founded by his descendant Babur", "Shift of trade routes due to destruction of established centers"],
        "relationships": [
            rel("tamerlane","Tamerlane","TRANSFORMS","samarkand","Samarkand","Made Samarkand a world-class cultural capital"),
            rel("tamerlane","Tamerlane","CAUSES","babur","Babur","Timurid dynasty produced Babur, founder of Mughal Empire"),
            rel("tamerlane","Tamerlane","DEFINES","ankara","Battle of Ankara","Defeated Ottoman Sultan Bayezid I, 1402"),
            rel("genghis-khan","Genghis Khan","INFLUENCES","tamerlane","Tamerlane","Claimed Chinggisid legacy and conquest model"),
            rel("tamerlane","Tamerlane","OCCURS_IN","samarkand","Samarkand","Capital of the Timurid Empire")
        ]
    },
    "william-the-conqueror": {
        "summary": "William I (c. 1028–1087), known as William the Conqueror, was the Duke of Normandy who seized the English throne at the Battle of Hastings (October 14, 1066) — the most consequential military event in English history. Born the illegitimate son of Duke Robert I, he earned his realm through ruthless determination.\n\nHastings was decided in a single day: Harold II's Saxon shield wall collapsed when William's cavalry feigned retreat, then struck. William's coronation on Christmas Day 1066 began the Norman transformation of England — French became the language of court, feudalism replaced Saxon landholding, and 8,000 Norman knights received English estates.\n\nThe Domesday Book (1086), his comprehensive survey of English wealth and property, remains one of history's greatest administrative achievements. William permanently fused English, Norman, and French cultures — transforming the English language, legal system, and architecture (Tower of London, Durham Cathedral) forever.",
        "causes": ["Edward the Confessor's childless death and disputed succession", "Norman military superiority in cavalry and castle warfare", "William's claim through Edward's alleged promise and papal backing"],
        "effects": ["Norman Conquest reshaping English language and culture", "Feudal system imposed on England", "Domesday Book — first comprehensive national survey", "French influence on English language (40% of English words)", "Castle-building transforming English landscape", "Foundation of Anglo-Norman aristocracy ruling for centuries"],
        "relationships": [
            rel("william-the-conqueror","William the Conqueror","DEFINES","hastings","Battle of Hastings","Defeated Harold II on October 14, 1066"),
            rel("william-the-conqueror","William the Conqueror","CAUSES","domesday-book","Domesday Book","Commissioned comprehensive survey of England, 1086"),
            rel("william-the-conqueror","William the Conqueror","TRANSFORMS","england","England","Norman Conquest permanently reshaped English culture"),
            rel("william-the-conqueror","William the Conqueror","OCCURS_IN","london","London","Crowned at Westminster Abbey, Christmas Day 1066"),
            rel("william-the-conqueror","William the Conqueror","CAUSES","tower-of-london","Tower of London","Began construction of the White Tower, 1078")
        ]
    },
    "thomas-aquinas": {
        "summary": "Thomas Aquinas (1225–1274) was an Italian Dominican friar, philosopher, and theologian who synthesized Aristotelian philosophy with Christian theology — a monumental intellectual achievement that remains the foundation of Catholic thought. His 'Summa Theologica' is one of the most influential works in Western philosophy.\n\nBorn to Italian nobility near Naples, he chose the life of a mendicant friar against his family's wishes. At the University of Paris and in Rome, he produced an astonishing body of work: the 'Summa Theologica,' 'Summa contra Gentiles,' and commentaries on Aristotle that demonstrated faith and reason were complementary, not contradictory.\n\nHis 'Five Ways' — five arguments for God's existence from natural reason — became the cornerstone of natural theology. Pope Leo XIII declared Thomism the official philosophy of the Catholic Church in 1879. Aquinas remains the most important philosopher-theologian in Christian history.",
        "causes": ["Recovery of Aristotle's works via Arabic translations", "Dominican Order's emphasis on learning and preaching", "Medieval university system enabling philosophical inquiry"],
        "effects": ["Synthesis of faith and reason as Catholic philosophical foundation", "Five Ways as standard natural theology arguments", "Thomism declared official Catholic philosophy (1879)", "Influence on natural law theory and human rights", "Foundation for Catholic social teaching", "Model for integrating secular philosophy with religious tradition"],
        "relationships": [
            rel("thomas-aquinas","Thomas Aquinas","TRANSMITS","aristotle","Aristotle","Integrated Aristotelian philosophy into Christian theology"),
            rel("avicenna","Avicenna","INFLUENCES","thomas-aquinas","Thomas Aquinas","Islamic philosophy shaped Scholastic metaphysics"),
            rel("thomas-aquinas","Thomas Aquinas","DEFINES","summa-theologica","Summa Theologica","Masterwork of systematic theology"),
            rel("thomas-aquinas","Thomas Aquinas","OCCURS_IN","paris","Paris","Taught at the University of Paris"),
            rel("thomas-aquinas","Thomas Aquinas","INFLUENCES","catholic-church","Catholic Church","Thomism became official church philosophy")
        ]
    },
    "al-khwarizmi": {
        "summary": "Muhammad ibn Musa al-Khwarizmi (c. 780–850) was a Persian mathematician, astronomer, and geographer whose works fundamentally shaped mathematics and science. Working at the House of Wisdom in Baghdad during the Islamic Golden Age, he produced treatises that introduced algebra and Hindu-Arabic numerals to the world.\n\nHis book 'Al-Kitab al-Mukhtasar fi Hisab al-Jabr wal-Muqabala' (c. 820) gave the world the word 'algebra' (from al-jabr, 'restoration'). His treatise on Hindu-Arabic numerals introduced the decimal positional system to the Islamic world and later to Europe — the word 'algorithm' derives from the Latinization of his name (Algoritmi).\n\nAl-Khwarizmi also produced improved astronomical tables, a world geography, and works on the Jewish calendar. His mathematical innovations — transmitted to Europe through Latin translations — made modern computation, science, and engineering possible.",
        "causes": ["Abbasid Caliphate patronage of science at House of Wisdom", "Indian mathematical traditions (Hindu numerals, zero)", "Greek mathematical heritage preserved in Arabic translation"],
        "effects": ["Invention of algebra as a mathematical discipline", "Introduction of Hindu-Arabic numeral system to the world", "Word 'algorithm' derived from his name", "Foundation for all modern computation and mathematics", "Astronomical tables used for centuries", "European mathematical revolution via Latin translations"],
        "relationships": [
            rel("al-khwarizmi","Al-Khwarizmi","DEFINES","algebra","Algebra","Founded algebra as a systematic discipline"),
            rel("al-khwarizmi","Al-Khwarizmi","OCCURS_IN","baghdad","Baghdad","Worked at the House of Wisdom under al-Ma'mun"),
            rel("al-khwarizmi","Al-Khwarizmi","INFLUENCES","fibonacci","Fibonacci","Hindu-Arabic numerals reached Europe through al-Khwarizmi"),
            rel("al-khwarizmi","Al-Khwarizmi","TRANSMITS","indian-mathematics","Indian Mathematics","Transmitted Hindu numerals and zero to Islamic world"),
            rel("al-khwarizmi","Al-Khwarizmi","INFLUENCES","computer-science","Computer Science","'Algorithm' named after him — foundation of computing")
        ]
    },
    "henry-viii-of-england": {
        "summary": "Henry VIII (1491–1547) was King of England from 1509 to 1547, best known for his six marriages and his break with the Roman Catholic Church — a decision that reshaped English religion, politics, and identity for centuries. His desire for a male heir drove him to annul his marriage to Catherine of Aragon, defying Pope Clement VII.\n\nWhen the Pope refused the annulment, Henry declared himself Supreme Head of the Church of England (1534), dissolved the monasteries, and seized their vast wealth. This English Reformation was initially more political than theological — Henry remained doctrinally conservative — but it unleashed forces that would transform Britain into a Protestant nation.\n\nBeyond religion, Henry expanded the Royal Navy (laying foundations for British naval supremacy), united England and Wales through the Laws in Wales Acts, and strengthened parliamentary sovereignty. His six wives — divorced, beheaded, died, divorced, beheaded, survived — remain the most memorable marital saga in royal history.",
        "causes": ["Desire for male heir driving annulment crisis with Catherine of Aragon", "Papal refusal of annulment under Habsburg pressure", "Renaissance humanism questioning papal authority"],
        "effects": ["English Reformation — Church of England breaks from Rome", "Dissolution of monasteries redistributing wealth to gentry", "Royal supremacy doctrine — monarch as head of church", "Foundation of British naval power", "Parliamentary sovereignty strengthened through Reformation statutes", "Wales united with England under English law"],
        "relationships": [
            rel("henry-viii-of-england","Henry VIII","CAUSES","english-reformation","English Reformation","Broke with Rome to annul marriage, creating Church of England"),
            rel("henry-viii-of-england","Henry VIII","DEFINES","act-of-supremacy","Act of Supremacy","Declared himself Supreme Head of Church of England, 1534"),
            rel("henry-viii-of-england","Henry VIII","INFLUENCES","elizabeth-i","Elizabeth I","Daughter who completed the Protestant settlement"),
            rel("henry-viii-of-england","Henry VIII","OCCURS_IN","london","London","Ruled from Hampton Court and Greenwich palaces"),
            rel("martin-luther","Martin Luther","INFLUENCES","henry-viii-of-england","Henry VIII","Protestant Reformation context enabled Henry's break with Rome")
        ]
    },
    "louis-xiv-of-france": {
        "summary": "Louis XIV (1638–1715), the 'Sun King,' was King of France for 72 years (1643–1715) — the longest verified reign of any sovereign in European history. His rule epitomized absolute monarchy: 'L'État, c'est moi' ('I am the state') captured his belief that royal authority was indivisible and divinely ordained.\n\nHe built the Palace of Versailles — transforming a hunting lodge into the most magnificent court in Europe, where 10,000 nobles competed for royal favor. French became the language of European diplomacy, French fashion set Continental trends, and French arts (Molière, Racine, Lully) defined the Baroque age.\n\nYet his ambitions overreached: the Revocation of the Edict of Nantes (1685) expelled 200,000 Huguenots, draining France of skilled workers. His wars of expansion — the War of Spanish Succession chief among them — exhausted the treasury. He left France culturally triumphant but financially ruined, sowing seeds for the Revolution 74 years later.",
        "causes": ["Minority experience during the Fronde rebellions (1648–53)", "Cardinal Mazarin's mentorship in statecraft", "French cultural confidence after Renaissance and Wars of Religion"],
        "effects": ["Versailles as model for European absolute monarchy", "French language adopted as lingua franca of diplomacy", "Revocation of Edict of Nantes — Huguenot exodus", "Financial exhaustion contributing to French Revolution", "Baroque cultural golden age in arts and literature", "Centralized French state administration"],
        "relationships": [
            rel("louis-xiv-of-france","Louis XIV","CAUSES","versailles","Palace of Versailles","Built the most magnificent court in European history"),
            rel("louis-xiv-of-france","Louis XIV","DEFINES","absolute-monarchy","Absolute Monarchy","Epitomized divine-right kingship in Europe"),
            rel("louis-xiv-of-france","Louis XIV","INFLUENCES","french-revolution","French Revolution","Financial ruin from wars sowed revolutionary seeds"),
            rel("louis-xiv-of-france","Louis XIV","OCCURS_IN","versailles","Versailles","Moved court from Paris to Versailles, 1682"),
            rel("louis-xiv-of-france","Louis XIV","CAUSES","war-of-spanish-succession","War of Spanish Succession","European coalition war against French hegemony")
        ]
    },
    "theodore-roosevelt": {
        "summary": "Theodore Roosevelt (1858–1919) was the 26th President of the United States (1901–1909), a larger-than-life figure who transformed the American presidency and the nation's role in world affairs. At 42, he became the youngest president in history after William McKinley's assassination.\n\nHis 'Square Deal' domestic program broke up monopolies (40+ antitrust suits), established the Food and Drug Administration, and created the National Parks system — protecting 230 million acres of public land. He was the first American to win the Nobel Peace Prize (1906) for mediating the Russo-Japanese War.\n\nRoosevelt's 'Big Stick' foreign policy built the Panama Canal, asserted American power in the Caribbean (Roosevelt Corollary to Monroe Doctrine), and sent the Great White Fleet around the world. A prolific author, Rough Rider, big-game hunter, and conservationist, he embodied the strenuous life he preached: 'Do what you can, with what you have, where you are.'",
        "causes": ["McKinley assassination elevating VP Roosevelt to presidency", "Progressive Era reform movement against Gilded Age excess", "American industrial power creating new global role"],
        "effects": ["National Parks system — 230 million acres protected", "Panama Canal connecting Atlantic and Pacific oceans", "Roosevelt Corollary expanding Monroe Doctrine", "Modern presidential activism as policy driver", "Antitrust enforcement against corporate monopolies", "Nobel Peace Prize for Russo-Japanese War mediation"],
        "relationships": [
            rel("theodore-roosevelt","Theodore Roosevelt","CAUSES","panama-canal","Panama Canal","Drove construction of the canal connecting two oceans"),
            rel("theodore-roosevelt","Theodore Roosevelt","DEFINES","national-parks","National Parks","Protected 230 million acres of American wilderness"),
            rel("theodore-roosevelt","Theodore Roosevelt","OCCURS_IN","washington-dc","Washington D.C.","26th President from 1901 to 1909"),
            rel("theodore-roosevelt","Theodore Roosevelt","INFLUENCES","franklin-d-roosevelt","FDR","Distant cousin who expanded TR's progressive legacy"),
            rel("theodore-roosevelt","Theodore Roosevelt","TRANSFORMS","united-states","United States","Expanded American global power and domestic reform")
        ]
    },
}

# ─── Process enrichments ───
enriched = 0
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        with open(f) as fh:
            data = json.load(fh)
        e = data["entities"][0]
        slug = e.get("slug", "")
        if slug not in ENRICHMENTS:
            continue
        
        enr = ENRICHMENTS[slug]
        e["summary"] = enr["summary"]
        
        # Build or update detailsJson
        dj = e.get("detailsJson", {})
        if isinstance(dj, str):
            try:
                dj = json.loads(dj)
            except:
                dj = {}
        if not isinstance(dj, dict):
            dj = {}
        
        dj["causes"] = enr["causes"]
        dj["effects"] = enr["effects"]
        dj["relationships"] = enr["relationships"]
        e["detailsJson"] = dj
        
        data["entities"][0] = e
        with open(f, 'w') as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        enriched += 1
        paras = enr["summary"].count("\n\n") + 1
        print(f"  ENRICHED {slug}: {len(enr['summary'])}c, {paras}p, {len(enr['causes'])}c/{len(enr['effects'])}e/{len(enr['relationships'])}r")
        del ENRICHMENTS[slug]
    except Exception as ex:
        print(f"  ERROR {f}: {ex}")

if ENRICHMENTS:
    print(f"\nMISSED: {list(ENRICHMENTS.keys())}")
print(f"\nTotal enriched: {enriched}")
