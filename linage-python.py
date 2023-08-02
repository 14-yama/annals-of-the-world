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
Joel_D_uuid = family_tree[Reuben_uuid].children[7].uuid
Joel2_D_uuid = family_tree[Reuben_uuid].children[8].uuid


add_children("Pallu", Pallu_uuid, ["Eliab", "Peleth_D"])
add_children("Zaccur_D", Zaccur_uuid, ["Shammua"])
add_children("Joel_D", Joel_D_uuid, ["Shemaiah"])
add_children("Joel_D", Joel2_D_uuid, ["Shema"])


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
             "Mahli", "Mushi", "Hosah_D", "Jaaziah_D", "Abdi_D"])
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
             "Zimri (Zabdi)", "Ethan", "Heman", "Calcol", "Dara"])
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

add_children("Manasseh", Manasseh_uuid, ["Asriel", "Machir", "Unknown"])
add_children("Ephraim", Ephraim_uuid, [
             "Shuthelah", "Beriah", "Shiphtan_D", "Hillel_D", "Azaziah_D", "Zuph_D"])

add_children("Bela", family_tree[Benjamin_uuid].children[0].uuid, [
             "Ard (Addar)", "Naaman", "Ezbon", "Uzzi", "Uzziel", "Jerimoth", "Iri", "Gera"])
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
    "Aphiah_D", Enan_D_uuid, ["Bechorah"])

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
##############################################

Eliab_uuid = family_tree[Pallu_uuid].children[0].uuid
Peleth_uuid = family_tree[Pallu_uuid].children[1].uuid
add_children("Eliab", Eliab_uuid, ["Nemuel", "Dathan", "Abiram"])
add_children("Peleth_D", Peleth_uuid, ["On"])


Shemaiah_uuid = family_tree[Joel_D_uuid].children[0].uuid
Shema_uuid = family_tree[Joel_D_uuid].children[1].uuid
add_children("Shemaiah", Shemaiah_uuid, ["Gog"])
add_children("Shema", Shema_uuid, ["Azaz"])

Shallum_uuid = family_tree[Shaul_uuid].children[0].uuid
add_children("Shallum", ["Mibsam"])

Lael_uuid = family_tree[Gershon_uuid].children[2].uuid
Jahath_uuid = family_tree[Gershon_uuid].children[3].uuid
add_children("Lael", Lael_uuid, ["Eliasaph"])
add_children("Jahath", ["Shimel"])


Izhar_uuid = family_tree[Kohath_uuid].children[1].uuid
add_children("Izhar", ["Korah", "Nepheg", "Zichri"])
############### INCOMPLETE##############################################
add_children("Hebron", ["Jeriah", "Amariah", "Jehaziel", "Jekameam"])
add_children("Uzziel", ["Mishael", "Elzaphan", "Sithri", "Micah", "Isshiah"])
add_children("Mahli", ["Eleazar", "Kish", "Libni"])
add_children("Mushi", ["Mahli", "Eder", "Jeremoth"])
add_children("Hosah", ["Shimri", "Hilkaih", "Tebaliah", "Zechariah"])
add_children("Jaaziah", ["Beno", "Shoham", "Zaccur", "Ibri"])
add_children("Abdi", ["Kish"])
add_children("Abihail", ["Zuriel"])
add_children("Miriam", ["Uri", "Shobel", "Salma",
             "Hareph", "Etam", "Ishi", "Abinadab"])
add_children("Aaron", ["Nadab", "Abihu", "Eleazer", "Ithamar"])
add_children("Moses", ["Gershom", "Eliezer"])
add_children("Hashabiah", ["Laadan"])
add_children("Er", ["Lecah"])
add_children("Laadah", ["Mareshah"])
add_children("Saraph", ["Jashubilehem"])
add_children("Hezron", ["Jerahmeel", "Ram",
             "Caleb (Chelubai)", "Segub", "Ashhur"])
add_children("Zimri (Zabdi)", ["Carmi"])
add_children("Ethan", ["Azariah"])
add_children("Reaiah", ["Jahath"])
add_children("Uzzi", ["Izrahiah"])
add_children("Puah", ["Tola"])
add_children("Machir", ["Peresh", "Sheresh", "Gilead",
             "Hammolechet", "Daughter of Machir"])
add_children("Unknown", ["Adnah*", "Jozabad*", "Jediael*", "Michael*", "Jediael*", "Elihu*", "Zillethai*", "Epher*", "Ishi*", "Eliel*",
                         "Azriel*", "Jeremiah*", "Hodaviah*", "Jahdie*", "Pedahzur*", "Susi*", "Ephod*", "Jair*", "Nobah*"])
add_children("Shuthelah", ["Bered (Becher)"])
add_children("Beriah", ["Sheerah", "Rephah"])
add_children("Shiphtan*", ["Kemuel"])
add_children("Hillel*", ["Abdon"])
add_children("Azaziah*", ["Hoshea"])
add_children("Zuph*", ["Tohu"])
add_children("Bilhan", ["Jeush", "Benjamin", "Ehud",
             "Chenaana", "Zethan", "Tarshish", "Ahishahar"])
add_children("Bechorah", ["Zeror"])
add_children("Raguel*", ["Raphael"])
add_children("Jahdo", ["Jeshishai"])
add_children("Abdiel", ["Ahi"])
add_children("Heber", ["Japhlet", "Shomer", "Hotham (Helem)", "Shua"])
add_children("Malchiel", ["Birzaith"])


####################################################

def print_family_tree(person, generation=1):
    indentation = "    " * generation
    print(f"{indentation}+ {person.name} ({person.father.name if person.father else 'Unknown'})")
    for child in person.children:
        print_family_tree(child, generation + 1)


# Print the family tree starting from Adam
print_family_tree(family_tree[adam_uuid])
