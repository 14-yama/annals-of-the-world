import uuid

# Define a Person class to represent individuals in the family tree


class Person:
    def __init__(self, name, father=None):
        # Generate a unique identifier for each person
        self.uuid = uuid.uuid4()
        self.name = name
        self.father = father
        self.children = []

    # Method to add a child to the person's list of children
    def add_child(self, child):
        self.children.append(child)
        child.father = self  # Update the child's father attribute

    def __str__(self):
        # Return a human-readable string representation of the person
        return f"{self.name} ({self.father.name if self.father else 'Unknown'})"

# Function to add children to an existing person or create a new person


def add_children(parent_name, parent_uuid, children):
    # Check if the parent already exists in the family tree
    if parent_uuid in family_tree:
        parent = family_tree[parent_uuid]
    else:
        # If the parent is not in the family tree, create a new person for them
        parent = Person(parent_name)
        family_tree[parent_uuid] = parent

    # Create new Person objects for each child and link them to their father
    for child_name in children:
        # Pass the existing parent as the father
        child = Person(child_name, father=parent)
        parent.add_child(child)
        family_tree[child.uuid] = child


# Initialize an empty family tree dictionary
family_tree = {}

# Create the root of the family tree for Adam
adam_uuid = uuid.uuid4()
adam = Person("Adam")
family_tree[adam_uuid] = adam

# Example usage to build the family tree:

# 1 Generation
add_children("Adam", adam_uuid, ["Cain", "Abel", "Seth"])

# 2 Generation
cain_uuid = family_tree[adam_uuid].children[0].uuid
add_children("Cain", cain_uuid, ["Enoch"])

seth_uuid = family_tree[adam_uuid].children[2].uuid
add_children("Seth", seth_uuid, ["Enosh"])

# 3 Generation
enoch_uuid = family_tree[cain_uuid].children[0].uuid
add_children("Enoch", enoch_uuid, ["Irad"])

enosh_uuid = family_tree[seth_uuid].children[0].uuid
add_children("Enosh", enosh_uuid, ["Kenan"])

# 4 Generation
irad_uuid = family_tree[enoch_uuid].children[0].uuid
add_children("Irad", irad_uuid, ["Mehujael"])

kenan_uuid = family_tree[enosh_uuid].children[0].uuid
add_children("Kenan", kenan_uuid, ["Mahalalel"])

# 5 Generation
mehujael_uuid = family_tree[irad_uuid].children[0].uuid
add_children("Mehujael", mehujael_uuid, ["Methushael"])

mahalalel_uuid = family_tree[kenan_uuid].children[0].uuid
add_children("Mahalalel", mahalalel_uuid, ["Jared"])

# 6 Generation
methushael_uuid = family_tree[mehujael_uuid].children[0].uuid
add_children("Methushael", methushael_uuid, ["Lamech"])

jared_uuid = family_tree[mahalalel_uuid].children[0].uuid
add_children("Jared", jared_uuid, ["Enoch"])

# 7 Generation
lamech_uuid = family_tree[methushael_uuid].children[0].uuid
add_children("Lamech", lamech_uuid, ["Jabal", "Jubal", "Tubal Cain", "Naamah"])

enoch_uuid = family_tree[jared_uuid].children[0].uuid
add_children("Enoch", enoch_uuid, ["Methuselah"])

# 8 Generation
methuselah_uuid = family_tree[enoch_uuid].children[0].uuid
add_children("Methuselah", methuselah_uuid, ["Lamech"])

# 9 Generation
lamech_uuid = family_tree[methuselah_uuid].children[0].uuid
add_children("Lamech", lamech_uuid, ["Noah"])

# 10 Generation
noah_uuid = family_tree[lamech_uuid].children[0].uuid
add_children("Noah", noah_uuid, ["Shem", "Ham", "Japheth"])

# 11 Generation
shem_uuid = family_tree[noah_uuid].children[0].uuid
add_children('Shem', shem_uuid, ["Elam", "Ashur", "Arpachshad", "Lud", "Aram"])
ham_uuid = family_tree[noah_uuid].children[1].uuid
add_children('Ham', ham_uuid, ["Cush", "Mizraim", "Put", "Canaan"])
jap_uuid = family_tree[noah_uuid].children[2].uuid
add_children("Japheth", jap_uuid, [
             "Gomer", "Magog", "Madai", "Javan", "Tubal", "Meshech", "Tiras"])

# 12 Generation
Arpachshad_uuid = family_tree[shem_uuid].children[2].uuid
Aram_uuid = family_tree[shem_uuid].children[4].uuid

Cush_uuid = family_tree[ham_uuid].children[0].uuid
Mizraim_uuid = family_tree[ham_uuid].children[1].uuid
Canaan_uuid = family_tree[ham_uuid].children[3].uuid

Gomer_uuid = family_tree[jap_uuid].children[0].uuid
Javan_uuid = family_tree[jap_uuid].children[3].uuid

add_children("Arpachshad", Arpachshad_uuid, ["Shelah"])
add_children("Aram", Aram_uuid, ["Uz", "Hul", "Gether", "Mash"])
add_children("Cush", Cush_uuid, [
             "Seba", "Havilah", "Sabtah", "Raamah", "Sabtecha", "Nimrod"])
add_children("Mizraim", Mizraim_uuid, [
             "Ludim", "Anamim", "Lehabim", "Naphtuhim", "Pathrusim", "Casluhim", "Caphtorim"])
add_children("Canaan", Canaan_uuid, ["Sidon", "Heth", "Jebusite", "Amorite",
             "Girgasite", "Hivite", "Arkite", "Sinite", "Arvadite", "Zemarite", "Hamathite"])
add_children("Gomer", Gomer_uuid, ["Ashkenaz", "Riphath", "Togarmah"])
add_children("Javan", Javan_uuid, ["Elishah", "Tarshish", "Kittim", "Rodanim"])

# 13 Generation
Shelah_uuid = family_tree[Arpachshad_uuid].children[0].uuid

Raamah_uuid = family_tree[Cush_uuid].children[3].uuid

Heth_uuid = family_tree[Canaan_uuid].children[1].uuid
Hivite_uuid = family_tree[Canaan_uuid].children[5].uuid

add_children("Shelah", Shelah_uuid, ["Eber"])
add_children("Raamah", Raamah_uuid, ["Sheba", "Dedan"])
add_children("Heth", Heth_uuid, ["Zohar"])
add_children("Hivite", Hivite_uuid, ["Hamor"])


# 14 Generation
Eber_uuid = family_tree[Shelah_uuid].children[0].uuid

Zohar_uuid = family_tree[Heth_uuid].children[0].uuid

Hamor_uuid = family_tree[Hivite_uuid].children[0].uuid
add_children("Eber", Eber_uuid, ["Peleg", "Joktan"])
add_children("Zohar", Zohar_uuid, ["Ephron"])
add_children("Hamor", Hamor_uuid, ["Shechem"])

# 15 Generation
Peleg_uuid = family_tree[Eber_uuid].children[0].uuid
Joktan_uuid = family_tree[Eber_uuid].children[1].uuid
add_children("Peleg", Peleg_uuid, ["Reu"])
add_children("Joktan", Joktan_uuid, ["Almodad", "Sheleph", "Hazarmaveth", "Jerah",
             "Hadoram", "Uzal", "Diklah", "Obal", "Abimael", "Sheba", "Ophir", "Havilah", "Jobab"])

# 16 Generation
Reu_uuid = family_tree[Peleg_uuid].children[0].uuid
add_children("Reu", Reu_uuid, ["Serug"])

# 17 Generation
Serug_uuid = family_tree[Reu_uuid].children[0].uuid
add_children("Serug", Serug_uuid, ["Nahor"])

# 18 Generation
Nahor_uuid = family_tree[Serug_uuid].children[0].uuid
add_children("Nahor", Nahor_uuid, ["Terah"])

# 19 Generation
Terah_uuid = family_tree[Nahor_uuid].children[0].uuid
add_children("Terah", Terah_uuid, ["Abram", "Nahor", "Haran", "Sarah"])

# 20 Generation
Abram_uuid = family_tree[Terah_uuid].children[0].uuid
Nahor_uuid = family_tree[Terah_uuid].children[1].uuid
Haran_uuid = family_tree[Terah_uuid].children[2].uuid
add_children("Abram", Abram_uuid, [
             "Isaac", "Ishmael", "Zimran", "Jokshan", "Medan", "Midian", "Ishbak", "Shuah"])
add_children("Nahor", Nahor_uuid, ["Uz", "Buz", "Kemuel", "Chesed", "Hazo",
             "Phildash", "Jidlaph", "Bethuel", "Tebah", "Gaham", "Tahash", "Maacah"])
add_children("Haran", Haran_uuid, ["Milcah", "Lot", "Iscah"])

# 21 Generation
Isaac_uuid = family_tree[Abram_uuid].children[0].uuid
Ishmael_uuid = family_tree[Abram_uuid].children[1].uuid
Jokshan_uuid = family_tree[Abram_uuid].children[3].uuid
Midian_uuid = family_tree[Abram_uuid].children[5].uuid

Kemuel_uuid = family_tree[Nahor_uuid].children[2].uuid
Bethuel_uuid = family_tree[Nahor_uuid].children[7].uuid

Lot_uuid = family_tree[Haran_uuid].children[1].uuid
add_children("Isaac", Isaac_uuid, ["Esau", "Jacob"])
add_children("Ishmael", Ishmael_uuid, ["Nabaioth", "Kedar", "Adbeel", "Mibsam",
             "Mishma", "Dumah", "Massa", "Hadad", "Tema", "Jetur", "Napsish", "Kedemah", "Mahalath", "Bashemath"])
add_children("Jokshan", Jokshan_uuid, [
             "Sheba", "Dedan"])
add_children("Midian", Midian_uuid, [
             "Ephah", "Epher", "Hanoch", "Abida", "Eldaah"])
add_children("Kemuel", Kemuel_uuid, ["Aram"])
add_children("Bethuel", Bethuel_uuid, ["Laban", "Rebekah"])
add_children("Lot", Lot_uuid, [
             "First Daughter", "Second Daughter", "Moab", "Ben-ammi"])

# 22 Generation
Esau_uuid = family_tree[Isaac_uuid].children[0].uuid
Jacob_uuid = family_tree[Isaac_uuid].children[1].uuid

Dedan_uuid = family_tree[Jokshan_uuid].children[1].uuid

Laban_uuid = family_tree[Bethuel_uuid].children[0].uuid
add_children("Esau", Esau_uuid, ["Eliphaz",
             "Jeush", "Jaalam", "Korah", "Reuel"])
add_children("Jacob", Jacob_uuid, ["Reuben", "Simeon", "Levi", "Judah", "Issachar",
             "Zebulun", "Dinah", "Joseph", "Benjamin", "Dan", "Naphtali", "Gad", "Asher"])
add_children("Dedan", Dedan_uuid, ["Asshurim", "Letushim", "Leummim"])
add_children("Laban", Laban_uuid, ["Leah", "Rachel"])

# 23 Generation
Eliphaz_uuid = family_tree[Esau_uuid].children[0].uuid
Reuel_uuid = family_tree[Esau_uuid].children[4].uuid

Reuben_uuid = family_tree[Jacob_uuid].children[0].uuid
Simeon_uuid = family_tree[Jacob_uuid].children[1].uuid
Levi_uuid = family_tree[Jacob_uuid].children[2].uuid
Judah_uuid = family_tree[Jacob_uuid].children[3].uuid
Issachar_uuid = family_tree[Jacob_uuid].children[4].uuid
Zebulun_uuid = family_tree[Jacob_uuid].children[5].uuid
Joseph_uuid = family_tree[Jacob_uuid].children[7].uuid
Benjamin_uuid = family_tree[Jacob_uuid].children[8].uuid
Dan_uuid = family_tree[Jacob_uuid].children[9].uuid
Naphtali_uuid = family_tree[Jacob_uuid].children[10].uuid
Gad_uuid = family_tree[Jacob_uuid].children[11].uuid
Asher_uuid = family_tree[Jacob_uuid].children[12].uuid


add_children("Eliphaz", Eliphaz_uuid, [
             "Teman", "Omar", "Zepho", "Gatam", "Kenaz", "Korah", "Timna", "Amalek"])
add_children("Reuel", Reuel_uuid, ["Nahath", "Zerah", "Shammah", "Mizzah"])

add_children("Reuben", Reuben_uuid, ["Hanoch", "Pallu", "Hezron", "Carmi",
             "Bohan_D", "Elizur_D", "Zaccur_D", "Joel_D", "Joel_D", "Zichri_D"])
add_children("Simeon", Simeon_uuid, [
             "Jemuel", "Jamin", "Ohad", "Jarib", "Zerah", "Shaul", "Hori_D"])
add_children("Levi", Levi_uuid, [
             "Gershon", "Kohath", "Merari", "Jochebed", "Kemuel_D", "Shimei_D"])
add_children("Judah", Judah_uuid, [
             "Er", "Onan", "Shelah", "Perez", "Zerah", "Shobal"])
add_children("Issachar", Issachar_uuid, [
             "Tola", "Puah", "Jashub", "Shimron", "Zuar_D", "Michael_D", "Dodo_D", "Azzan_D", "Joseph_D"])
add_children("Zebulun", Zebulun_uuid, [
             "Sered", "Elon", "Jahleel", "Elon_D", "Helon_D", "Sodi_D", "Parnach_D", "Obadiah_D"])
add_children("Joseph", Joseph_uuid, ["Manasseh", "Ephraim"])
add_children("Benjamin", Benjamin_uuid, ["Bela", "Jediael", "Becher", "Ashbel", "Gera", "Naaman", "Ehi", "Rosh", "Muppim", "Huppin",
             "Ard", "Aharah", "Nohah", "Rapha", "Aphiah_D", "Matri_D", "Gideoni_D", "Raphu_D", "Shaharaim_D", "Chislon_D", "Bichri_D", "Rimmon_D"])
add_children("Dan", Dan_uuid, [
             "Hushim", "Ammiahaddai_D", "Gemalli_D", "Ahisamach_D", "Dibri_D", "Manoah_D"])
add_children("Naphtali", Naphtali_uuid, [
             "Jahzeel", "Geni", "Jezer", "Shillem", "Vopshi_D", "Ammihud_D", "Asiel_D", "Enan_D", "Azrel_D"])
add_children("Gad", Gad_uuid, ["Ziphion", "Haggi", "Shuni", "Ezbon", "Eri", "Arodi", "Areli", "Deuel_D", "Machi_D",
             "Unknown_D", "Bani_D", "Buz_D", "Guni_D", "Unknown Descendant of Gad_D", "Joel_D", "Shapham_D", "Jannai_D", "Shaphat_D"])
add_children("Asher", Asher_uuid, ["Imnah", "Ishauah",
             "Isui", "Beriah", "Sarah", "Jether_D", "Phanuel_D", "Michael_D"])
# 24 Generation
Pallu_uuid = family_tree[Reuben_uuid].children[1].uuid
Zaccur_uuid = family_tree[Reuben_uuid].children[6].uuid
Joel1_D_uuid = family_tree[Reuben_uuid].children[7].uuid
Joel2_D_uuid = family_tree[Reuben_uuid].children[8].uuid


add_children("Pallu", Pallu_uuid, ["Eliab", "Peleth_D"])
add_children("Zaccur_D", Zaccur_uuid, ["Shammua"])
add_children("Joel I_D", Joel1_D_uuid, ["Shemaiah"])
add_children("Joel II_D", Joel2_D_uuid, ["Shema"])


Shaul_uuid = family_tree[Simeon_uuid].children[5].uuid
Hori_D_uuid = family_tree[Simeon_uuid].children[6].uuid
add_children("Shaul", Shaul_uuid, ["Shallum"])
add_children("Hori_D", Hori_D_uuid, ["Shaphat"])

Gershon_uuid = family_tree[Levi_uuid].children[0].uuid
Kohath_uuid = family_tree[Levi_uuid].children[1].uuid
Merari_uuid = family_tree[Levi_uuid].children[2].uuid
Kemuel_D_uuid = family_tree[Levi_uuid].children[4].uuid
Shimei_D_uuid = family_tree[Levi_uuid].children[5].uuid
add_children("Gershon", Gershon_uuid, [
             "Libni", "Shimei", "Lael_D", "Jahath"])
add_children("Kohath", Kohath_uuid, ["Amram", "Izhar", "Hebron", "Uzziel"])
add_children("Merari", Merari_uuid, [
             "Mahli", "Mushi", "Hosah_D", "Jaaziah_D", "Abdi_D", "Jehallelel_D", "Abihail_D"])
add_children("Kemuel_D", Kemuel_D_uuid, ["Hashabiah"])
add_children("Shimei_D", Shimei_D_uuid, [
             "Shelomoth", "Haziel", "Haran", "Jahath", "Zina", "Jeush", "Beriah"])


Shelah_uuid = family_tree[Judah_uuid].children[2].uuid
Perez_uuid = family_tree[Judah_uuid].children[3].uuid
Zerah_uuid = family_tree[Judah_uuid].children[4].uuid
Shobal_uuid = family_tree[Judah_uuid].children[5].uuid
add_children("Shelah", Shelah_uuid, [
             "Er", "Laadah", "Jokim", "Joash", "Saraph"])
add_children("Perez", Perez_uuid, ["Hezron", "Hamul"])
add_children("Zerah", Zerah_uuid, [
             "Zimri", "Ethan", "Heman", "Calcol", "Dara"])
add_children("Shobal", Shobal_uuid, ["Reaiah"])


Tola_uuid = family_tree[Issachar_uuid].children[0].uuid
Zuar_D_uuid = family_tree[Issachar_uuid].children[4].uuid
Michael_D_uuid = family_tree[Issachar_uuid].children[5].uuid
Dodo_D_uuid = family_tree[Issachar_uuid].children[6].uuid
Azzan_D_uuid = family_tree[Issachar_uuid].children[7].uuid
add_children("Tola", Tola_uuid, [
             "Uzzi", "Rephaiah", "Jeriel", "Jahmai", "Ibsam", "Shemuel"])
add_children("Zuar_D", Zuar_D_uuid, ["Nethanel"])
add_children("Michael_D", Michael_D_uuid, ["Omri"])
add_children("Dodo_D", Dodo_D_uuid, ["Puah"])
add_children("Azzan_D", Azzan_D_uuid, ["Paltiel"])

Manasseh_uuid = family_tree[Joseph_uuid].children[0].uuid
Ephraim_uuid = family_tree[Joseph_uuid].children[1].uuid

add_children("Manasseh", Manasseh_uuid, ["Asriel", "Machir", "Unknown_D"])
add_children("Ephraim", Ephraim_uuid, [
             "Shuthelah", "Beriah", "Shiphtan_D", "Hillel_D", "Azaziah_D", "Zuph_D"])

add_children("Bela", family_tree[Benjamin_uuid].children[0].uuid, [
             "Ard (Addar)", "Naaman", "Ezbon", "Uzzi", "Uzziel", "Jerimoth", "Iri", "Gera"])
Jediael_uuid = family_tree[Benjamin_uuid].children[0].uuid
add_children(
    "Jediael", family_tree[Benjamin_uuid].children[1].uuid, ["Bilhan"])
add_children("Gera", family_tree[Benjamin_uuid].children[4].uuid, [
             "Shimei_D", "Ehud_D"])
add_children(
    "Matri_D", family_tree[Benjamin_uuid].children[15].uuid, ["Jeiel_D"])
add_children(
    "Gideoni_D", family_tree[Benjamin_uuid].children[16].uuid, ["Abidan"])
add_children(
    "Raphu_D", family_tree[Benjamin_uuid].children[17].uuid, ["Palti"])
add_children(
    "Bichri_D", family_tree[Benjamin_uuid].children[20].uuid, ["Sheba"])
add_children("Rimmon_D", family_tree[Benjamin_uuid].children[21].uuid, [
             "Baanah", "Rechab"])


add_children("Dan", Dan_uuid, [
             "Hushim", "Ammiahaddai_D", "Gemalli_D", "Ahisamach_D", "Dibri_D", "Manoah_D"])

add_children("Ammiahaddai_D",
             family_tree[Dan_uuid].children[1].uuid, ["Ahiezer"])
add_children("Gemalli_D", family_tree[Dan_uuid].children[2].uuid, ["Ammiel"])
add_children(
    "Ahisamach_D", family_tree[Dan_uuid].children[3].uuid, ["Oholiab"])
add_children("Dibri_D", family_tree[Dan_uuid].children[4].uuid, ["Shelomith"])
add_children("Manoah_D", family_tree[Dan_uuid].children[5].uuid, ["Samson"])

Vopshi_D_uuid = family_tree[Naphtali_uuid].children[4].uuid
Ammihud_D_uuid = family_tree[Naphtali_uuid].children[5].uuid
Asiel_D_uuid = family_tree[Naphtali_uuid].children[6].uuid
Enan_D_uuid = family_tree[Naphtali_uuid].children[7].uuid
Azrel_D_uuid = family_tree[Naphtali_uuid].children[8].uuid
Aphiah_D_uuid = family_tree[Benjamin_uuid].children[14].uuid
add_children(
    "Vopshi_D", Vopshi_D_uuid, ["Nahbi"])
add_children(
    "Ammihud_D", Ammihud_D_uuid, ["Pedahel"])
add_children(
    "Asiel_D", Asiel_D_uuid, ["Raguel_D"])
add_children("Enan_D", Enan_D_uuid, ["Ahira"])
add_children(
    "Azrel_D", Azrel_D_uuid, ["Jerimoth"])
add_children(
    "Aphiah_D", Aphiah_D_uuid, ["Bechorah"])

add_children("Gad", Gad_uuid, ["Ziphion", "Haggi", "Shuni", "Ezbon", "Eri", "Arodi", "Areli", "Deuel_D", "Machi_D",
             "Unknown_D", "Bani_D", "Buz_D", "Guni_D", "Unknown Descendant of Gad_D", "Joel_D", "Shapham_D", "Jannai_D", "Shaphat_D"])

Deuel_D_uuid = family_tree[Gad_uuid].children[7].uuid
Machi_D_uuid = family_tree[Gad_uuid].children[8].uuid
Unknown_D_uuid = family_tree[Gad_uuid].children[9].uuid
Buz_D_uuid = family_tree[Gad_uuid].children[11].uuid
Guni_D_uuid = family_tree[Gad_uuid].children[12].uuid
Unknown_Descendant_of_Gad_D_uuid = family_tree[Gad_uuid].children[13].uuid
add_children("Deuel_D", Deuel_D_uuid, ["Eliasaph"])
add_children("Machi_D", Machi_D_uuid, ["Geuel"])
add_children("Unknown_D", Machi_D_uuid, ["Ezer_D", "Obadiah_D", "Eliab_D",
             "Mishmannah_D", "Jeremiah_D", "Attai_D", "Eliel_D", "Johanan_D", "Elzabad_D", "Jeremiah_D", "Machbanai_D"])
add_children("Buz_D", Buz_D_uuid, ["Jahdo"])
add_children("Guni_D", Guni_D_uuid, ["Abdiel"])
add_children("Unknown Descendant of Gad_D", Unknown_Descendant_of_Gad_D_uuid, [
             "Joel_D", "Shapham_D", "Jannai_D", "Shaphat_D"])

Beriah_uuid = family_tree[Asher_uuid].children[3].uuid
Jether_D_uuid = family_tree[Asher_uuid].children[5].uuid
Phanuel_D_uuid = family_tree[Asher_uuid].children[6].uuid,
Michael_D_uuid = family_tree[Asher_uuid].children[7].uuid

add_children("Beriah", Beriah_uuid, [
             "Heber", "Malchiel"])
add_children("Jether_D", Jether_D_uuid, [
             "Jephunneh", "Pispa", "Ara"])
add_children("Phanuel_D", Phanuel_D_uuid, ["Anna"])
add_children("Michael_D", Michael_D_uuid, ["Sethur"])

# ---------------------------------------------------25 Generation------------------------------------------------------------------
# Pallu-Reuben
Eliab_uuid = family_tree[Pallu_uuid].children[0].uuid
Peleth_uuid = family_tree[Pallu_uuid].children[1].uuid
add_children("Eliab", Eliab_uuid, ["Nemuel", "Dathan", "Abiram"])
add_children("Peleth_D", Peleth_uuid, ["On"])

# Joel1_D-Reuben
Shemaiah_uuid = family_tree[Joel1_D_uuid].children[0].uuid
add_children("Shemaiah", Shemaiah_uuid, ["Gog"])

# Joel2_D-Reuben
Shema_uuid = family_tree[Joel2_D_uuid].children[0].uuid
add_children("Shema", Shema_uuid, ["Azaz"])

# Shaul-Simeon
Shallum_uuid = family_tree[Shaul_uuid].children[0].uuid
add_children("Shallum", Shallum_uuid, ["Mibsam"])

# Gershon-Levi
Lael_uuid = family_tree[Gershon_uuid].children[2].uuid
Jahath_uuid = family_tree[Gershon_uuid].children[3].uuid
add_children("Lael", Lael_uuid, ["Eliasaph"])
add_children("Jahath", Jahath_uuid, ["Shimel"])

# Kohath-Levi
Amram_uuid = family_tree[Kohath_uuid].children[0].uuid
Izhar_uuid = family_tree[Kohath_uuid].children[1].uuid
Hebron_uuid = family_tree[Kohath_uuid].children[2].uuid
Uzziel_uuid = family_tree[Kohath_uuid].children[3].uuid
add_children("Amram", Amram_uuid, ["Aaron", "Miriam", "Moses"])
add_children("Izhar", Izhar_uuid, ["Korah", "Nepheg", "Zichri"])
add_children("Hebron", Hebron_uuid, [
             "Jeriah", "Amariah", "Jehaziel", "Jekameam"])
add_children("Uzziel", Uzziel_uuid, [
             "Mishael", "Elzaphan", "Sithri", "Micah", "Isshiah"])

# Merari-Levi
Mahli_uuid = family_tree[Merari_uuid].children[0].uuid
Mushi_uuid = family_tree[Merari_uuid].children[1].uuid
Hosah_D_uuid = family_tree[Merari_uuid].children[2].uuid
Jaaziah_D_uuid = family_tree[Merari_uuid].children[3].uuid
Abdi_D_uuid = family_tree[Merari_uuid].children[4].uuid
Abihail_D_uuid = family_tree[Merari_uuid].children[6].uuid
add_children("Mahli", Mahli_uuid, ["Eleazar", "Kish", "Libni"])
add_children("Mushi", Mushi_uuid, ["Mahli", "Eder", "Jeremoth"])
add_children("Hosah_D", Hosah_D_uuid, [
             "Shimri", "Hilkaih", "Tebaliah", "Zechariah"])
add_children("Jaaziah_D", Jaaziah_D_uuid, ["Beno", "Shoham", "Zaccur", "Ibri"])
add_children("Abdi_D", Abdi_D_uuid, ["Kish"])
add_children("Abihail", Abihail_D_uuid, ["Zuriel"])

# Aram-Kohath
Aaron_uuid = family_tree[Amram_uuid].children[0].uuid
Miriam_uuid = family_tree[Amram_uuid].children[1].uuid
Moses_uuid = family_tree[Amram_uuid].children[2].uuid
add_children("Aaron", Aaron_uuid, ["Nadab", "Abihu", "Eleazer", "Ithamar"])
add_children("Miriam", Miriam_uuid, ["Uri", "Shobel", "Salma",
             "Hareph", "Etam", "Ishi", "Abinadab"])
add_children("Moses", Moses_uuid, ["Gershom", "Eliezer"])

add_children("Levi", Levi_uuid, [
             "Gershon", "Kohath", "Merari", "Jochebed", "Kemuel_D", "Shimei_D"])

# Kemuel_D-Levi
Hashabiah_uuid = family_tree[Kemuel_D_uuid].children[0].uuid
add_children("Hashabiah", Hashabiah_uuid, ["Laadan"])

# Shelah-Judah
Er_uuid = family_tree[Shelah_uuid].children[0].uuid
Laadah_uuid = family_tree[Shelah_uuid].children[1].uuid
Saraph_uuid = family_tree[Shelah_uuid].children[4].uuid
add_children("Er", Er_uuid, ["Lecah"])
add_children("Laadah", Laadah_uuid, ["Mareshah"])
add_children("Saraph", Saraph_uuid, ["Jashubilehem"])

# Perez-Judah
Hezron_uuid = family_tree[Perez_uuid].children[0].uuid
add_children("Hezron", Hezron_uuid, ["Jerahmeel", "Ram",
             "Caleb (Chelubai)", "Segub", "Ashhur"])

# Zerah-Judah
Zimri_uuid = family_tree[Zerah_uuid].children[0].uuid
Etan_uuid = family_tree[Zerah_uuid].children[1].uuid
add_children("Zimri", Zimri_uuid, ["Carmi"])
add_children("Ethan", Etan_uuid, ["Azariah"])

# Shobal-Judah
Reaiah_uuid = family_tree[Shobal_uuid].children[0].uuid
add_children("Reaiah", Reaiah_uuid, ["Jahath"])

# Tola-Issachar
Uzzi_uuid = family_tree[Tola_uuid].children[0].uuid
add_children("Uzzi", Uzzi_uuid, ["Izrahiah"])

# Doda_D-Issachar
Puah_uuid = family_tree[Dodo_D_uuid].children[0].uuid
add_children("Puah", Puah_uuid, ["Tola"])

# Manasseh-Joseph
Machir_uuid = family_tree[Manasseh_uuid].children[1].uuid
Unknown_D_uuid = family_tree[Manasseh_uuid].children[2].uuid
add_children("Machir", Machir_uuid, ["Peresh", "Sheresh", "Gilead",
             "Hammolechet", "Daughter of Machir"])
add_children("Unknown", Unknown_D_uuid, ["Adnah*", "Jozabad*", "Jediael*", "Michael*", "Jediael*", "Elihu*", "Zillethai*", "Epher*", "Ishi*", "Eliel*",
                                         "Azriel*", "Jeremiah*", "Hodaviah*", "Jahdie*", "Pedahzur*", "Susi*", "Ephod*", "Jair*", "Nobah*"])

# Ephraim-Joseph
Shuthelah_uuid = family_tree[Ephraim_uuid].children[0].uuid
Beriah_uuid = family_tree[Ephraim_uuid].children[1].uuid
Shiphtan_uuid = family_tree[Ephraim_uuid].children[2].uuid
Hillel_D_uuid = family_tree[Ephraim_uuid].children[3].uuid
Azaziah_D_uuid = family_tree[Ephraim_uuid].children[4].uuid
Zuph_D_uuid = family_tree[Ephraim_uuid].children[5].uuid
add_children("Shuthelah", Shuthelah_uuid, ["Bered (Becher)"])
add_children("Beriah", Beriah_uuid, ["Sheerah", "Rephah"])
add_children("Shiphtan_D", Shiphtan_uuid, ["Kemuel"])
add_children("Hillel_D", Hillel_D_uuid, ["Abdon"])
add_children("Azaziah_D", Azaziah_D_uuid, ["Hoshea"])
add_children("Zuph_D", Zuph_D_uuid, ["Tohu"])

# Jediael-Benjamin
Bilhan_uuid = family_tree[Jediael_uuid].children[0].uuid
add_children("Bilhan", Bilhan_uuid, ["Jeush", "Benjamin", "Ehud",
             "Chenaana", "Zethan", "Tarshish", "Ahishahar"])
# Aphiah_D-Benjamin
Bechorah_uuid = family_tree[Aphiah_D_uuid].children[0].uuid
add_children("Bechorah", Bechorah_uuid, ["Zeror"])

# Asiel_D-Naphtali
Raguel_D_uuid = family_tree[Asiel_D_uuid].children[0].uuid
add_children("Raguel*", Raguel_D_uuid, ["Raphael"])


add_children("Gad", Gad_uuid, ["Ziphion", "Haggi", "Shuni", "Ezbon", "Eri", "Arodi", "Areli", "Deuel_D", "Machi_D",
             "Unknown_D", "Bani_D", "Buz_D", "Guni_D", "Unknown Descendant of Gad_D", "Joel_D", "Shapham_D", "Jannai_D", "Shaphat_D"])

# Buz_D-Gad
Jahdo_uuid = family_tree[Buz_D_uuid].children[0].uuid
add_children("Jahdo", Jahdo_uuid, ["Jeshishai"])

# Guni_D-Gad
Abdiel_uuid = family_tree[Guni_D_uuid].children[0].uuid
add_children("Abdiel", Abdiel_uuid, ["Ahi"])

# Beriah-Asher
Heber_uuid = family_tree[Beriah_uuid].children[0].uuid
Malchiel_uuid = family_tree[Beriah_uuid].children[1].uuid
add_children("Heber", Heber_uuid, [
             "Japhlet", "Shomer", "Hotham", "Shua"])
add_children("Malchiel", Malchiel_uuid, ["Birzaith"])

# ---------------------------------------------------26 Generation------------------------------------------------------------------
# Shemaiah-Joel_D
Gog_uuid = family_tree[Shemaiah_uuid].children[0].uuid
add_children('Gog', Gog_uuid, ["Shimei"])

# Shema-Joel2_D
Azaz_uuid = family_tree[Shema_uuid].children[0].uuid
add_children('Azaz', Azaz_uuid, ['Bela', 'Zechariah_D', 'Jeiel_D'])

# Shallum-Shaul
Mibsam_uuid = family_tree[Shallum_uuid].children[0].uuid
add_children('Mibsam', Mibsam_uuid, ["Mishma"])

# Jahath-Gershon
Shimel_uuid = family_tree[Jahath_uuid].children[0].uuid
add_children("Shimel", Shimel_uuid, ["Zimmah"])

# Izhar-Kohath
Korah_uuid = family_tree[Izhar_uuid].children[0].uuid
add_children("Korah", Korah_uuid, ["Assir", "Elkanah", "Ebiasaph"])

# Uzziel-Kohath
Micah_uuid = family_tree[Uzziel_uuid].children[3].uuid
add_children("Micah", Micah_uuid, ["Shamir"])

# Uzziel-Kohath
Isshiah_uuid = family_tree[Uzziel_uuid].children[4].uuid
add_children("Isshiah", Isshiah_uuid, ["Zechariah"])

# Mahli-Merari
Kish_uuid = family_tree[Mahli_uuid].children[1].uuid
Libni_uuid = family_tree[Mahli_uuid].children[2].uuid
add_children("Kish", Kish_uuid, ["Jerameel"])
add_children("Libni", Libni_uuid, ["Shimei"])


Mahli_uuid = family_tree[Mushi_uuid].children[0].uuid
add_children("Mahli", Mahli_uuid, ["Shemer"])

# Abdi_D-Merari
Kish_uuid = family_tree[Abdi_D_uuid].children[0].uuid
add_children("Kish", Kish_uuid, ["Jerahmeel"])

# Miriam-Jechebed
add_children("Miriam", Miriam_uuid, ["Uri", "Shobel", "Salma",
             "Hareph", "Etam", "Ishi", "Abinadab"])
Uri_uuid = family_tree[Miriam_uuid].children[0].uuid
Shobel_uuid = family_tree[Miriam_uuid].children[1].uuid
Salma_uuid = family_tree[Miriam_uuid].children[2].uuid
Hareph_uuid = family_tree[Miriam_uuid].children[3].uuid
Etam_uuid = family_tree[Miriam_uuid].children[4].uuid
add_children("Uri", Uri_uuid, ["Bezaleel"])
add_children("Shobel", Shobel_uuid, ["Reaiah", "Kiriath-jearim", "Horeth"])
add_children("Salma", Salma_uuid, ["Bethlehem", "Netophathites", "Ataroth",
             "Ataroth", "Beth-Joab", "Manahethites", "Zorites", "Abinadab", "Shimon", "Bani"])
add_children("Hareph", Hareph_uuid, ["Beth-gader"])
add_children("Etam", Etam_uuid, ["Jezreel", "Ishma", "Idbash", "Hazzelelponi"])

# Aaron-Amram
Eleazer_uuid = family_tree[Aaron_uuid].children[2].uuid
Ithamar_uuid = family_tree[Aaron_uuid].children[3].uuid
add_children('Eleazer', Eleazer_uuid, ['Phinehas'])
add_children("Ithamar", Ithamar_uuid, ["Eli"])

# Moses-Amram
Gershom_uuid = family_tree[Aaron_uuid].children[0].uuid
Eliezer_uuid = family_tree[Aaron_uuid].children[1].uuid
add_children("Gershom", Gershom_uuid, ["Shebuel", "Jonathan"])
add_children("Eliezer", Eliezer_uuid, ["Rehabiah"])

# Hashabiah-Kemuel_D
Laadan_uuid = family_tree[Hashabiah_uuid].children[0].uuid
add_children("Laadan", Laadan_uuid, ["Jehiel", "Zetham", "Joel"])

# Hezron-Perez
Jerahmeel_uuid = family_tree[Hezron_uuid].children[0].uuid
Ram_uuid = family_tree[Hezron_uuid].children[1].uuid
Caleb_uuid = family_tree[Hezron_uuid].children[2].uuid
Segub_uuid = family_tree[Hezron_uuid].children[3].uuid
Ashhur_uuid = family_tree[Hezron_uuid].children[4].uuid
add_children("Jerahmeel", Jerahmeel_uuid, [
             "Ram", "Bunah", "Oren", "Ozem", "Ahijah", "Onam"])
add_children("Ram", Ram_uuid, ["Amminadab"])
add_children("Caleb", Caleb_uuid, ["Juphunneh", "Mesha", "Mareshah", "Jesher", "Shobab", "Ardon",
             "Hur", "Haran", "Moza", "Gazez", "Sheber", "Tirhanah", "Shaaph", "Sheva", "Achsah", "Jahdai"])
add_children("Segub", Segub_uuid, ["Jair"])
add_children("Ashhur", Ashhur_uuid, ["Tekoa", "Ahuzzam", "Hepher",
             "Temeni", "Haahashtar", "Zereth", "Izhar", "Ethnan", "Koz (Coz)"])

# Zimri-Zerah
Carmi_uuid = family_tree[Zimri_uuid].children[0].uuid
add_children("Carmi", Carmi_uuid, ["Achan"])

# Reaiah-Shobal
Jahath_uuid = family_tree[Reaiah_uuid].children[0].uuid
add_children("Jahath", Jahath_uuid, ["Ahumai", "Lahad"])

# Uzzi-Tola
Izrahiah_uuid = family_tree[Uzzi_uuid].children[0].uuid
add_children("Izrahiah", Izrahiah_uuid, [
             "Michael", "Obadiah", "Joel", "Isshiah"])

# Machir-Manasseh
Sheresh_uuid = family_tree[Machir_uuid].children[1].uuid
Gilead_uuid = family_tree[Machir_uuid].children[2].uuid
Hammolechet_uuid = family_tree[Machir_uuid].children[3].uuid
add_children("Sheresh", Sheresh_uuid, ["Ulam", "Rekem"])
add_children("Gilead", Gilead_uuid, [
             "Lezer (Jeezer)", "Helek", "Asriel", "Shechem", "Shemida", "Hepher", "Jephthah"])
add_children("Hammolechet", Hammolechet_uuid, ["Ishhod", "Abiezer", "Mahlah"])

# Unknown-Manasseh
Pedahzur_D_uuid = family_tree[Unknown_D_uuid].children[14].uuid
Susi_D_uuid = family_tree[Unknown_D_uuid].children[15].uuid
Ephod_D_uuid = family_tree[Unknown_D_uuid].children[16].uuid
add_children("Pedahzur_D", Pedahzur_D_uuid, ["Gamaliel"])
add_children("Susi_D", Susi_D_uuid, ["Gaddi"])
add_children("Ephod_D", Ephod_D_uuid, ["Hanniel"])

# Shuthelah-Ephraim
Bered_uuid = family_tree[Shuthelah_uuid].children[0].uuid
add_children("Bered", Bered_uuid, ["Tahath"])

# Beriah-Ephraim
Rephah_uuid = family_tree[Beriah_uuid].children[1].uuid
add_children("Rephah", Rephah_uuid, ["Resheph"])

# Zuph_D-Ephraim
Tohu_D_uuid = family_tree[Zuph_D_uuid].children[0].uuid
add_children("Tohu_D", Tohu_D_uuid, ["Elihu"])

# Bechorah-Aphiah_D
Zeror_uuid = family_tree[Bechorah_uuid].children[0].uuid
add_children("Zeror", Zeror_uuid, ["Abiel"])

# Raguel_D-Asiel_D
Raphael_uuid = family_tree[Raguel_D_uuid].children[0].uuid
add_children("Raphael", Raphael_uuid, ["Gabael"])

# Jahdo-Buz_D
Jeshishai_uuid = family_tree[Jahdo_uuid].children[0].uuid
add_children("Jeshishai", Jeshishai_uuid, ["Michael"])

# Heber-Beriah
Japhlet_uuid = family_tree[Heber_uuid].children[0].uuid
Shomer_uuid = family_tree[Heber_uuid].children[1].uuid
Hotham_uuid = family_tree[Heber_uuid].children[2].uuid
add_children("Japhlet", Japhlet_uuid, ["Pasach", "Bimhal", "Ashvath"])
add_children("Shomer", Shomer_uuid, ["Ahi", "Rohgah", "Jehubbah", "Aram"])
add_children("Hotham", Hotham_uuid, ["Zophah", "Imna", "Shelesh", "Amal"])


# ---------------------------------------------------27 Generation------------------------------------------------------------------


def print_family_tree(person, generation=1):
    indentation = "    " * generation
    print(f"{indentation}+ {person.name} ({person.father.name if person.father else 'Unknown'})")
    for child in person.children:
        print_family_tree(child, generation + 1)


# Print the family tree starting from Adam
print_family_tree(family_tree[adam_uuid])
