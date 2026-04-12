#!/usr/bin/env python3
"""Create new entity JSON files for historically important figures missing from the repository."""
import json, os

BASE = "data/appwrite-export/entities"

def rel(src_slug, src_name, verb, tgt_slug, tgt_name, ctx=""):
    return {"sourceSlug": src_slug, "sourceName": src_name, "verb": verb,
            "targetSlug": tgt_slug, "targetName": tgt_name, "context": ctx}

def make_entity(slug, name, call, label, era, summary, causes, effects, rels, subjects, continent=""):
    return {
        "entities": [{
            "slug": slug, "name": name, "callNumber": call, "label": label,
            "era": era, "summary": summary, "subjects": subjects,
            "continent": continent,
            "subjectHeadings": [f"People — {name} — {era}"],
            "detailsJson": {"causes": causes, "effects": effects, "relationships": rels,
                           "places": [], "texts": [], "frameworks": []}
        }]
    }

NEW_ENTITIES = [
    make_entity(
        "adolf-hitler", "Adolf Hitler", "222.adolf-hitler", "Person", "Modern",
        "Adolf Hitler (1889–1945) was the Austrian-born dictator of Nazi Germany whose ideology of racial supremacy, territorial expansion, and genocide plunged the world into its deadliest conflict. Rising from a failed art student in Vienna to Chancellor of Germany (1933), he dismantled the Weimar Republic and established totalitarian rule.\n\nHis regime unleashed World War II (1939–1945), which killed 70–85 million people. The Holocaust — his systematic murder of six million Jews alongside Roma, disabled persons, and political opponents — remains history's most documented genocide. His invasions consumed Europe from the Atlantic to the gates of Moscow.\n\nDefeated by the Allied powers, Hitler took his own life in a Berlin bunker on April 30, 1945. His legacy is a permanent warning about the consequences of unchecked authoritarianism, racial hatred, and the fragility of democratic institutions.",
        ["Treaty of Versailles humiliation and economic crisis", "Weimar Republic instability and hyperinflation",
         "Antisemitic traditions in European history"],
        ["World War II — 70–85 million dead", "The Holocaust — 6 million Jews murdered",
         "Division of Europe and onset of Cold War", "Creation of the United Nations",
         "Establishment of Israel (1948)", "Nuremberg Trials establishing crimes against humanity doctrine"],
        [rel("adolf-hitler","Adolf Hitler","CAUSES","world-war-ii","World War II","Launched global conflict killing 70–85 million"),
         rel("adolf-hitler","Adolf Hitler","CAUSES","holocaust","The Holocaust","Systematic genocide of 6 million Jews"),
         rel("adolf-hitler","Adolf Hitler","OCCURS_IN","berlin","Berlin","Ruled from Reich Chancellery in Berlin"),
         rel("joseph-stalin","Joseph Stalin","CAUSES","adolf-hitler","Adolf Hitler","Soviet resistance critical to Hitler's defeat"),
         rel("adolf-hitler","Adolf Hitler","INFLUENCES","cold-war","Cold War","WWII's aftermath created bipolar world order")],
        ["Germany", "World War II", "Holocaust", "Fascism", "Nazism", "European History"], "Europe"
    ),
    make_entity(
        "catherine-the-great", "Catherine the Great", "221.catherine-the-great", "Person", "Early Modern",
        "Catherine II (1729–1796), known as Catherine the Great, was Empress of Russia from 1762 to 1796 — the longest-ruling female leader in Russian history. Born Princess Sophie of Anhalt-Zerbst in Prussia, she seized the throne from her husband Peter III in a coup and became Russia's most celebrated monarch.\n\nShe expanded the Russian Empire by 200,000 square miles — annexing Crimea, partitioning Poland, and pushing to the Black Sea. Her embrace of Enlightenment ideas (correspondence with Voltaire and Diderot) earned her the title 'Semiramis of the North,' though her reform of serfdom remained incomplete.\n\nCatherine patronized arts and education, founded the Hermitage Museum collection, established the Russian Academy, and modernized Russia's legal and educational systems. Her reign marked Russia's emergence as one of Europe's great powers, building on Peter the Great's legacy while establishing her own.",
        ["Peter the Great's modernization program", "Enlightenment philosophy spreading to Russian elite",
         "Peter III's unpopular pro-Prussian policies enabling coup"],
        ["Russian Empire expanded to Black Sea and Crimea", "Partition of Poland (1772, 1793, 1795)",
         "Hermitage Museum collection founded", "Russian Academy established",
         "Russia's emergence as European great power", "Enlightened absolutism model for European monarchs"],
        [rel("catherine-the-great","Catherine the Great","TRANSFORMS","russia","Russia","Expanded empire by 200,000 square miles"),
         rel("peter-the-great","Peter the Great","INFLUENCES","catherine-the-great","Catherine the Great","Continued Peter's Westernization program"),
         rel("voltaire","Voltaire","INFLUENCES","catherine-the-great","Catherine the Great","Philosophical correspondence shaped reform agenda"),
         rel("catherine-the-great","Catherine the Great","OCCURS_IN","saint-petersburg","Saint Petersburg","Ruled from Winter Palace for 34 years"),
         rel("catherine-the-great","Catherine the Great","CAUSES","crimea","Crimea","Annexed Crimean Peninsula from Ottoman Empire, 1783")],
        ["Russia", "Enlightenment", "Russian Empire", "Crimea", "European Monarchy"], "Europe"
    ),
    make_entity(
        "che-guevara", "Che Guevara", "270.che-guevara", "Person", "Contemporary",
        "Ernesto 'Che' Guevara (1928–1967) was an Argentine Marxist revolutionary, physician, and guerrilla leader who became one of the most iconic figures of the 20th century. His motorcycle journey across South America (1951–52) exposed him to poverty that radicalized his politics.\n\nAs Fidel Castro's right-hand man, he played a decisive role in the Cuban Revolution (1956–59), then served as president of Cuba's national bank and minister of industries. His theories of guerrilla warfare and 'foco' revolutionary strategy inspired armed movements across Latin America, Africa, and Asia.\n\nCaptured and executed by Bolivian forces (with CIA assistance) on October 9, 1967, Guevara became a martyr of the global left. Alberto Korda's 1960 photograph of him — 'Guerrillero Heroico' — is the most reproduced image in photography history, a symbol of rebellion that transcends its political origins.",
        ["Latin American poverty and inequality witnessed on motorcycle journey",
         "Cold War ideological polarization", "Cuban revolutionary movement led by Fidel Castro"],
        ["Cuban Revolution's success (1959)", "Guerrilla warfare theory inspiring Third World revolutionaries",
         "Iconic status in global counterculture", "Influence on Latin American leftist movements",
         "Foco theory of revolutionary insurgency", "Most reproduced photograph in history (Guerrillero Heroico)"],
        [rel("che-guevara","Che Guevara","CAUSES","cuban-revolution","Cuban Revolution","Key military leader in Castro's revolutionary victory"),
         rel("che-guevara","Che Guevara","INFLUENCES","latin-american-revolution","Latin American Revolutions","Guerrilla warfare theory adopted across the continent"),
         rel("che-guevara","Che Guevara","OCCURS_IN","havana","Havana","Served in Cuban government after revolution"),
         rel("karl-marx","Karl Marx","INFLUENCES","che-guevara","Che Guevara","Marxist ideology drove Guevara's revolutionary vision"),
         rel("che-guevara","Che Guevara","OCCURS_IN","bolivia","Bolivia","Captured and executed in Bolivia, October 9, 1967")],
        ["Cuba", "Argentina", "Bolivia", "Revolution", "Marxism", "Guerrilla Warfare"], "Americas"
    ),
    make_entity(
        "elizabeth-i", "Elizabeth I", "221.elizabeth-i", "Person", "Early Modern",
        "Elizabeth I (1533–1603) was Queen of England and Ireland from 1558 to 1603, whose 45-year reign — the Elizabethan era — is considered one of the most glorious periods in English history. The daughter of Henry VIII and Anne Boleyn, she survived imprisonment, religious persecution, and plots to reach the throne.\n\nShe established the Church of England's moderate Protestant settlement (1559), defeating the Spanish Armada (1588) in one of history's most celebrated naval victories. Her court fostered the English Renaissance — Shakespeare, Marlowe, Spenser, and Francis Bacon all flourished under her patronage.\n\nThe 'Virgin Queen' never married, using the prospect of her hand as a diplomatic tool. Her reign saw England's emergence as a major naval power, the founding of the first English colonies in the Americas, and a cultural flowering that permanently enriched the English language and literature.",
        ["Henry VIII's break with Rome creating the Church of England",
         "Mary I's unpopular Catholic restoration", "English Renaissance cultural ferment"],
        ["Elizabethan religious settlement — moderate Protestantism",
         "Defeat of the Spanish Armada (1588)", "English Renaissance in theatre and literature",
         "Foundation of English colonial enterprise (Roanoke, Virginia)",
         "England's rise as major naval power", "Model of female sovereignty and political acumen"],
        [rel("elizabeth-i","Elizabeth I","DEFINES","spanish-armada","Spanish Armada","Defeated Philip II's invasion fleet, 1588"),
         rel("henry-viii-of-england","Henry VIII","CAUSES","elizabeth-i","Elizabeth I","Father's Reformation shaped Elizabeth's religious settlement"),
         rel("elizabeth-i","Elizabeth I","INFLUENCES","william-shakespeare","William Shakespeare","Elizabethan court patronized Shakespeare's theatre"),
         rel("elizabeth-i","Elizabeth I","OCCURS_IN","london","London","Ruled from Whitehall and Richmond palaces"),
         rel("elizabeth-i","Elizabeth I","TRANSFORMS","england","England","Established England as Protestant naval power")],
        ["England", "Tudor", "Reformation", "Spanish Armada", "Renaissance", "Theatre"], "Europe"
    ),
    make_entity(
        "franklin-d-roosevelt", "Franklin D. Roosevelt", "222.franklin-d-roosevelt", "Person", "Modern",
        "Franklin Delano Roosevelt (1882–1945) was the 32nd President of the United States, serving an unprecedented four terms (1933–1945). He led America through its two greatest 20th-century crises: the Great Depression and World War II. Paralyzed by polio at 39, he concealed his disability while projecting boundless confidence.\n\nHis New Deal programs (1933–39) — Social Security, the SEC, FDIC, Tennessee Valley Authority — transformed the relationship between government and citizens, creating the modern welfare state. His 'fireside chats' on radio pioneered direct presidential communication with the public.\n\nAs wartime commander-in-chief, FDR forged the Allied coalition with Churchill and Stalin, oversaw the Manhattan Project, and planned the postwar order including the United Nations. He died on April 12, 1945 — weeks before VE Day — having guided America from isolationist republic to global superpower.",
        ["Great Depression devastating American economy (1929–33)",
         "Failure of Hoover's laissez-faire response", "Rise of fascism in Europe threatening global order"],
        ["New Deal creating modern American welfare state",
         "Social Security system for 60+ million Americans",
         "Allied victory in World War II",
         "United Nations founding (posthumous vision)",
         "American emergence as global superpower",
         "Precedent of presidential crisis leadership"],
        [rel("franklin-d-roosevelt","FDR","CAUSES","new-deal","New Deal","Transformed role of federal government in American life"),
         rel("franklin-d-roosevelt","FDR","DEFINES","world-war-ii","World War II","Led Allied coalition to victory over Axis powers"),
         rel("franklin-d-roosevelt","FDR","INFLUENCES","united-nations","United Nations","Planned postwar international organization"),
         rel("franklin-d-roosevelt","FDR","OCCURS_IN","washington-dc","Washington D.C.","32nd President, served 1933–1945"),
         rel("winston-churchill","Winston Churchill","CAUSES","franklin-d-roosevelt","FDR","Anglo-American 'special relationship' won the war")],
        ["United States", "New Deal", "World War II", "Great Depression", "United Nations"], "Americas"
    ),
    make_entity(
        "nefertiti", "Nefertiti", "221.nefertiti", "Person", "Classical",
        "Nefertiti (c. 1370–1330 BCE) was the Great Royal Wife of Pharaoh Akhenaten and one of the most powerful women in ancient Egypt. Her name means 'A Beautiful Woman Has Come,' and the painted limestone bust discovered in 1912 at Amarna — now in Berlin's Neues Museum — is one of the most recognized works of art in the world.\n\nShe played an unprecedented role in Akhenaten's religious revolution, which replaced Egypt's traditional polytheism with the worship of a single sun deity, Aten. Reliefs show her performing rituals previously reserved for pharaohs — smiting enemies, making offerings, and driving chariots — suggesting co-regency or near-equal power.\n\nAfter Akhenaten's death, Nefertiti may have briefly ruled as Pharaoh Neferneferuaten before Tutankhamun's succession. Her tomb has never been definitively identified, fueling ongoing archaeological speculation. She remains an enduring symbol of female power, beauty, and artistic excellence in the ancient world.",
        ["Eighteenth Dynasty Egypt's imperial wealth and power",
         "Akhenaten's Aten religious revolution", "Egyptian tradition of powerful royal women"],
        ["Co-regency model of female pharaonic power",
         "Amarna art style revolutionizing Egyptian aesthetics",
         "Bust of Nefertiti as iconic artwork for 3,300 years",
         "Possible precedent for female pharaohs (Neferneferuaten)",
         "Amarna Period as unique experiment in monotheism",
         "Inspiration for modern discourse on women in power"],
        [rel("nefertiti","Nefertiti","OCCURS_IN","amarna","Amarna","Lived in the new capital Akhetaten (Amarna)"),
         rel("akhenaten","Akhenaten","CAUSES","nefertiti","Nefertiti","Nefertiti's power derived from Aten religious revolution"),
         rel("nefertiti","Nefertiti","INFLUENCES","tutankhamun","Tutankhamun","Possible regent before Tutankhamun's accession"),
         rel("nefertiti","Nefertiti","DEFINES","amarna-art","Amarna Art","New artistic style depicting royal family naturalistically"),
         rel("nefertiti","Nefertiti","OCCURS_IN","egypt","Egypt","Great Royal Wife of the Eighteenth Dynasty")],
        ["Egypt", "Amarna", "Akhenaten", "Ancient Egypt", "Art History", "Women in Power"], "Africa"
    ),
    make_entity(
        "rene-descartes", "René Descartes", "210.rene-descartes", "Person", "Early Modern",
        "René Descartes (1596–1650) was a French philosopher, mathematician, and scientist who is regarded as the father of modern philosophy. His famous declaration 'Cogito, ergo sum' ('I think, therefore I am') established the first principle of modern Western philosophy: the certainty of one's own existence as a thinking being.\n\nHis 'Meditations on First Philosophy' (1641) employed radical doubt — questioning the reliability of senses, the existence of the physical world, even mathematics — to find an indubitable foundation for knowledge. His 'Discourse on the Method' (1637) introduced the systematic approach to reasoning that influenced all subsequent science.\n\nIn mathematics, Descartes invented the Cartesian coordinate system — merging algebra and geometry into analytic geometry. His mind-body dualism (the 'mind-body problem') remains one of philosophy's central debates. He spent most of his productive years in the Dutch Republic and died in Stockholm, serving as tutor to Queen Christina of Sweden.",
        ["Skeptical tradition from Montaigne and ancient Pyrrhonism",
         "Scientific revolution of Copernicus, Galileo, and Kepler",
         "Jesuit education at La Flèche providing rigorous philosophical training"],
        ["Foundation of modern philosophy through methodical doubt",
         "Cartesian coordinate system unifying algebra and geometry",
         "Mind-body dualism as enduring philosophical problem",
         "Scientific method formalized in the Discourse",
         "Influence on Spinoza, Leibniz, and all subsequent philosophy",
         "Analytic geometry enabling calculus (Newton, Leibniz)"],
        [rel("rene-descartes","René Descartes","DEFINES","cogito","Cogito ergo sum","Established foundational certainty of modern philosophy"),
         rel("rene-descartes","René Descartes","INFLUENCES","isaac-newton","Isaac Newton","Cartesian mathematics enabled Newtonian physics"),
         rel("rene-descartes","René Descartes","INFLUENCES","immanuel-kant","Immanuel Kant","Cartesian epistemology shaped Kant's critical philosophy"),
         rel("avicenna","Avicenna","INFLUENCES","rene-descartes","René Descartes","Avicenna's flying man anticipated cogito"),
         rel("rene-descartes","René Descartes","OCCURS_IN","amsterdam","Amsterdam","Spent productive years in the Dutch Republic")],
        ["France", "Netherlands", "Philosophy", "Mathematics", "Scientific Revolution"], "Europe"
    ),
    make_entity(
        "richard-the-lionheart", "Richard the Lionheart", "221.richard-the-lionheart", "Person", "Medieval",
        "Richard I (1157–1199), known as Richard the Lionheart (Cœur de Lion), was King of England from 1189 to 1199 and the most celebrated warrior-king of the Middle Ages. Despite ruling England for a decade, he spent only six months there — his heart belonged to crusade and combat.\n\nHe led the Third Crusade (1189–92) alongside Philip II of France and Frederick Barbarossa, recapturing Acre and Jaffa from Saladin. Though he failed to retake Jerusalem, the Treaty of Jaffa secured Christian access to the holy city. His legendary chivalric encounters with Saladin became the stuff of medieval romance.\n\nCaptured by Duke Leopold V of Austria on his return from the Holy Land, Richard was ransomed for 150,000 marks — nearly three times England's annual revenue. He died besieging Châlus-Chabrol castle in France from a crossbow wound. His reign epitomized the crusading ideal that dominated European politics and culture for two centuries.",
        ["Angevin Empire's vast continental holdings",
         "Saladin's conquest of Jerusalem (1187) sparking Third Crusade",
         "Chivalric culture of 12th-century European nobility"],
        ["Third Crusade securing Christian access to Jerusalem",
         "Legendary status as ideal medieval warrior-king",
         "150,000-mark ransom draining English treasury",
         "Chivalric romance tradition inspired by his exploits",
         "Angevin Empire maintained despite king's absence",
         "Model of crusading kingship for later European monarchs"],
        [rel("richard-the-lionheart","Richard I","DEFINES","third-crusade","Third Crusade","Led the largest crusading army against Saladin"),
         rel("saladin","Saladin","CAUSES","richard-the-lionheart","Richard I","Saladin's conquests provoked the Third Crusade"),
         rel("richard-the-lionheart","Richard I","OCCURS_IN","acre","Acre","Captured Acre, key victory of the Third Crusade"),
         rel("richard-the-lionheart","Richard I","OCCURS_IN","london","London","Crowned King of England at Westminster, 1189"),
         rel("henry-ii","Henry II","CAUSES","richard-the-lionheart","Richard I","Angevin Empire inherited from father Henry II")],
        ["England", "Crusades", "Saladin", "Medieval History", "Chivalry"], "Europe"
    ),
    make_entity(
        "simon-bolivar", "Simón Bolívar", "220.simon-bolivar", "Person", "Modern",
        "Simón Bolívar (1783–1830) was the Venezuelan military and political leader who liberated six South American nations from Spanish colonial rule — earning the title 'El Libertador.' Born to a wealthy Creole family in Caracas, he dedicated his life to the vision of a united, free Latin America.\n\nBetween 1811 and 1826, Bolívar led armies across some of the most daunting terrain on Earth — the Andes, the Orinoco basin, the Colombian highlands — liberating Venezuela, Colombia, Ecuador, Peru, and Bolivia (named after him). His dramatic crossing of the Andes in 1819 to surprise Spanish forces at Boyacá rivals Hannibal's Alpine crossing.\n\nHis dream of a unified Gran Colombia ultimately failed — fracturing into separate nations by 1831. Bolívar died disillusioned in Santa Marta, Colombia, at age 47. Yet his vision of Latin American sovereignty and unity endures: 'If my death contributes to the end of factions and the consolidation of the union, I shall be lowered in peace into my grave.'",
        ["Spanish colonial oppression and Bourbon reforms",
         "Enlightenment ideas (Rousseau, Locke) inspiring independence",
         "Haitian Revolution demonstrating colonial overthrow was possible"],
        ["Liberation of Venezuela, Colombia, Ecuador, Peru, and Bolivia",
         "Gran Colombia federation (1819–1831)", "Bolivia named in his honor",
         "Inspiration for Latin American independence movements",
         "Pan-American unity ideal influencing regional organizations",
         "Model of revolutionary military leadership across multiple nations"],
        [rel("simon-bolivar","Simón Bolívar","TRANSFORMS","south-america","South America","Liberated six nations from Spanish colonial rule"),
         rel("simon-bolivar","Simón Bolívar","DEFINES","boyaca","Battle of Boyacá","Decisive victory after Andean crossing, 1819"),
         rel("simon-bolivar","Simón Bolívar","CAUSES","gran-colombia","Gran Colombia","Founded federation uniting Venezuela, Colombia, Ecuador"),
         rel("jean-jacques-rousseau","Rousseau","INFLUENCES","simon-bolivar","Simón Bolívar","Enlightenment ideas drove Bolívar's revolutionary ideology"),
         rel("simon-bolivar","Simón Bolívar","OCCURS_IN","caracas","Caracas","Born in Caracas, capital of modern Venezuela")],
        ["Venezuela", "Colombia", "Ecuador", "Peru", "Bolivia", "Latin American Independence", "Revolution"], "Americas"
    ),
    make_entity(
        "tutankhamun", "Tutankhamun", "221.tutankhamun", "Person", "Classical",
        "Tutankhamun (c. 1341–1323 BCE) was an Egyptian pharaoh of the Eighteenth Dynasty who reigned for about ten years (c. 1332–1323 BCE). Ascending the throne at approximately age nine, he reversed his father Akhenaten's religious revolution, restoring the worship of Amun and the traditional priesthood.\n\nHistorically a minor pharaoh who died young — likely from malaria compounded by a bone disorder — Tutankhamun became the most famous ruler in Egyptian history when Howard Carter discovered his nearly intact tomb in the Valley of the Kings on November 4, 1922. The tomb's 5,398 artifacts, including the iconic gold death mask (11 kg of solid gold), sparked worldwide 'Egyptomania.'\n\nThe 'Curse of the Pharaohs' legend — fueled by Lord Carnarvon's death weeks after the tomb's opening — captured public imagination globally. Tutankhamun's treasures have become the defining image of ancient Egyptian civilization, touring the world's greatest museums and attracting millions of visitors to Cairo's Egyptian Museum.",
        ["Akhenaten's religious revolution requiring restoration",
         "Eighteenth Dynasty imperial power and wealth", "Young pharaoh guided by advisors Ay and Horemheb"],
        ["Restoration of traditional Egyptian polytheism",
         "Howard Carter's 1922 discovery sparking Egyptomania",
         "Gold death mask as most recognized ancient artifact",
         "Modern archaeological science applied to royal mummies",
         "'Curse of the Pharaohs' entering popular culture",
         "Global museum exhibitions drawing millions of visitors"],
        [rel("tutankhamun","Tutankhamun","OCCURS_IN","valley-of-the-kings","Valley of the Kings","Tomb KV62 discovered November 4, 1922"),
         rel("akhenaten","Akhenaten","CAUSES","tutankhamun","Tutankhamun","Reversed father's Aten revolution, restored Amun worship"),
         rel("nefertiti","Nefertiti","INFLUENCES","tutankhamun","Tutankhamun","Possible stepmother and regent"),
         rel("tutankhamun","Tutankhamun","DEFINES","egyptomania","Egyptomania","1922 discovery sparked global fascination with ancient Egypt"),
         rel("tutankhamun","Tutankhamun","OCCURS_IN","egypt","Egypt","Pharaoh of the Eighteenth Dynasty, New Kingdom")],
        ["Egypt", "Valley of the Kings", "Archaeology", "Akhenaten", "Howard Carter", "Ancient Egypt"], "Africa"
    ),
    make_entity(
        "kublai-khan", "Kublai Khan", "221.kublai-khan", "Person", "Medieval",
        "Kublai Khan (1215–1294) was the fifth Great Khan of the Mongol Empire and founder of the Yuan Dynasty in China — the first non-Chinese dynasty to rule all of China. Grandson of Genghis Khan, he completed the Mongol conquest of the Song Dynasty (1279) and presided over the largest contiguous empire in history.\n\nHis capital at Khanbaliq (modern Beijing) became a cosmopolitan marvel described by Marco Polo as the greatest city in the world. Kublai patronized science, arts, and trade — introducing paper money across his realm, building a vast postal relay system, and sponsoring astronomical observatories. He attempted invasions of Japan (1274, 1281) and Java, though both failed.\n\nKublai balanced Mongol military tradition with Chinese administrative sophistication. His Yuan Dynasty connected East and West along the Silk Road, facilitating the greatest period of Eurasian exchange before the Age of Exploration. Coleridge's poem 'In Xanadu did Kubla Khan / A stately pleasure dome decree' immortalized his legendary court.",
        ["Mongol Empire's westward and southward expansion", "Song Dynasty's military weakness",
         "Genghis Khan's imperial legacy and succession system"],
        ["Yuan Dynasty — first non-Chinese to rule all of China",
         "Khanbaliq (Beijing) as cosmopolitan world capital",
         "Paper money system across the empire",
         "Silk Road trade at its medieval peak",
         "Failed invasions of Japan (kamikaze typhoons)",
         "Marco Polo's account spreading knowledge of China to Europe"],
        [rel("kublai-khan","Kublai Khan","TRANSFORMS","china","China","Conquered Song Dynasty, founded Yuan Dynasty (1271)"),
         rel("genghis-khan","Genghis Khan","CAUSES","kublai-khan","Kublai Khan","Grandfather's empire enabled Kublai's conquests"),
         rel("marco-polo","Marco Polo","OCCURS_IN","kublai-khan","Kublai Khan","Polo served Kublai's court for 17 years"),
         rel("kublai-khan","Kublai Khan","OCCURS_IN","beijing","Beijing","Built capital Khanbaliq on site of modern Beijing"),
         rel("kublai-khan","Kublai Khan","DEFINES","yuan-dynasty","Yuan Dynasty","Established Mongol rule over all China, 1271–1368")],
        ["China", "Mongol Empire", "Yuan Dynasty", "Silk Road", "Marco Polo", "Beijing"], "Asia"
    ),
    make_entity(
        "guru-nanak-dev", "Guru Nanak", "251.guru-nanak-dev", "Person", "Early Modern",
        "Guru Nanak (1469–1539) was the founder of Sikhism — the world's fifth-largest organized religion with over 30 million followers. Born in Talwandi (now Nankana Sahib, Pakistan) to a Hindu family in Mughal-ruled Punjab, he received a divine revelation at age 30 that declared 'There is no Hindu, there is no Muslim.'\n\nHe undertook four great journeys (udasis) spanning over 28,000 kilometers across South Asia, the Middle East, and Central Asia — visiting Mecca, Baghdad, Tibet, and Sri Lanka. His teachings rejected caste hierarchies, ritualism, and religious bigotry, emphasizing instead one God (Ik Onkar), honest living, and sharing with others.\n\nGuru Nanak established the institutions of langar (communal kitchen open to all castes and faiths), sangat (congregation), and the Gurmukhi script. His compositions form the opening portion of the Guru Granth Sahib, Sikhism's holy scripture. His ten successor Gurus built on his foundation to create one of history's most egalitarian religious traditions.",
        ["Religious diversity and tension in Mughal-era Punjab",
         "Bhakti and Sufi devotional movements in South Asia",
         "Hindu caste system and ritual exclusion"],
        ["Founding of Sikhism — world's fifth-largest religion",
         "Langar (communal kitchen) as radical egalitarian institution",
         "Gurmukhi script preserving Punjabi language",
         "Guru Granth Sahib as living scripture",
         "Ten Sikh Gurus continuing his mission",
         "Model of interfaith dialogue and religious tolerance"],
        [rel("guru-nanak-dev","Guru Nanak","DEFINES","sikhism","Sikhism","Founded the Sikh faith with its core principles"),
         rel("guru-nanak-dev","Guru Nanak","CAUSES","guru-granth-sahib","Guru Granth Sahib","Compositions form opening of Sikh holy scripture"),
         rel("guru-nanak-dev","Guru Nanak","OCCURS_IN","nankana-sahib","Nankana Sahib","Birthplace in modern Pakistan"),
         rel("guru-nanak-dev","Guru Nanak","INFLUENCES","sikh-gurus","Ten Sikh Gurus","Founded tradition continued by nine successor Gurus"),
         rel("kabir","Kabir","INFLUENCES","guru-nanak-dev","Guru Nanak","Bhakti poet Kabir influenced Nanak's devotional approach")],
        ["India", "Pakistan", "Sikhism", "Punjab", "Religion", "Interfaith Dialogue"], "Asia"
    ),
]

created = 0
for entity_data in NEW_ENTITIES:
    e = entity_data["entities"][0]
    slug = e["slug"]
    call = e["callNumber"]
    div_str = call.split(".")[0]
    
    target_dir = f"{BASE}/{div_str}-Class-{div_str}"
    os.makedirs(target_dir, exist_ok=True)
    target_file = f"{target_dir}/{div_str}{slug}.json"
    
    if os.path.exists(target_file):
        print(f"  SKIP {slug} — already exists")
        continue
    
    with open(target_file, 'w') as f:
        json.dump(entity_data, f, indent=2, ensure_ascii=False)
    created += 1
    slen = len(e["summary"])
    paras = e["summary"].count("\n\n") + 1
    rels_count = len(e["detailsJson"]["relationships"])
    print(f"  CREATED {slug}: {slen}c, {paras}p, {rels_count}r → {target_file}")

print(f"\nTotal created: {created}")
