import uuid

# Define a Person class to represent individuals in the family tree
class Person:
    def __init__(self, name, father=None):
        # Generate a unique identifier for each person
        self.uuid = uuid.uuid4()
        self.name = name
        self.father_uuid = father.uuid if father else None
        self.children = []

    # Method to add a child to the person's list of children
    def add_child(self, child):
        self.children.append(child)

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
        child = Person(child_name, father=parent)
        parent.add_child(child)
        family_tree[child.uuid] = child

# Initialize an empty family tree dictionary
family_tree = {}

# Example usage to build the family tree:

# 1 Generation
add_children("Adam", None, ["Cain", "Abel", "Seth"])

# 2 Generation
add_children("Cain", family_tree[None].uuid, ["Enoch"])
add_children("Seth", family_tree[None].uuid, ["Enosh"])

# 3 Generation
add_children("Enoch", family_tree[family_tree[None].uuid].uuid, ["Irad"])
add_children("Enosh", family_tree[family_tree[None].uuid].uuid, ["Kenan"])

# 4 Generation
add_children("Irad", family_tree[family_tree[None].uuid].uuid, ["Mehujael"])
add_children("Kenan", family_tree[family_tree[None].uuid].uuid, ["Mahalalel"])

# 5 Generation
add_children("Mehujael", family_tree["Irad"].uuid, ["Methushael"])
add_children("Mahalalel", family_tree["Kenan"].uuid, ["Jared"])

# 6 Generation
add_children("Methushael", family_tree[None].uuid, ["Lamech"])
add_children("Jared", family_tree[None].uuid, ["Enoch"])

# 7 Generation
add_children("Lamech", family_tree["Methushael"].uuid, ["Jabal", "Jubal", "Tubal Cain", "Naamah"])
add_children("Enoch", family_tree["Jared"].uuid, ["Methuselah"])

# 8 Generation
add_children("Methuselah", family_tree["Enoch"].uuid, ["Lamech"])

# 9 Generation
add_children("Lamech", family_tree["Methuselah"].uuid, ["Noah"])

# 10 Generation
add_children("Noah", family_tree["Lamech"].uuid, ["Shem", "Ham", "Japheth"])

# 11 Generation
add_children("Shem", family_tree["Noah"].uuid, ["Elam", "Ashur", "Arpachshad", "Lud", "Aram"])
add_children("Ham", family_tree["Noah"].uuid, ["Cush", "Mizraim", "Put", "Canaan"])
add_children("Japheth", family_tree["Noah"].uuid, ["Gomer", "Magog", "Madai", "Javan", "Tubal", "Meshech", "Tiras"])

# 12 Generation
add_children("Arpachshad", family_tree["Shem"].uuid, ["Shelah"])
add_children("Aram", family_tree["Shem"].uuid, ["Uz", "Hul", "Gether", "Mash"])
add_children("Cush", family_tree["Ham"].uuid, ["Seba", "Havilah", "Sabtah", "Raamah", "Sabtecha", "Nimrod"])
add_children("Mizraim", family_tree["Ham"].uuid, ["Ludim", "Anamim", "Lehabim", "Naphtuhim", "Pathrusim", "Casluhim", "Caphtorim"])
add_children("Canaan", family_tree["Ham"].uuid, ["Sidon", "Heth", "Jebusite", "Amorite", "Girgasite", "Hivite", "Arkite", "Sinite", "Arvadite", "Zemarite", "Hamathite"])
add_children("Gomer", family_tree["Japheth"].uuid, ["Ashkenaz", "Riphath", "Togarmah"])
add_children("Javan", family_tree["Japheth"].uuid, ["Elishah", "Tarshish", "Kittim", "Rodanim"])

# 13 Generation
add_children("Shelah", family_tree["Arpachshad"].uuid, ["Eber"])
add_children("Raamah", family_tree["Cush"].uuid, ["Sheba", "Dedan"])
add_children("Heth", family_tree["Canaan"].uuid, ["Zohar"])
add_children("Hivite", family_tree["Canaan"].uuid, ["Hamor"])

# 14 Generation
add_children("Eber", family_tree["Shelah"].uuid, ["Peleg", "Joktan"])
add_children("Zohar", family_tree["Heth"].uuid, ["Ephron"])
add_children("Hamor", family_tree["Hivite"].uuid, ["Shechem"])

# 15 Generation
add_children("Peleg", family_tree["Eber"].uuid, ["Reu"])
add_children("Joktan", family_tree["Eber"].uuid, ["Almodad", "Sheleph", "Hazarmaveth", "Jerah", "Hadoram", "Uzal", "Diklah", "Obal", "Abimael", "Sheba", "Ophir", "Havilah", "Jobab"])

# 16 Generation
add_children("Reu", family_tree["Peleg"].uuid, ["Serug"])

# 17 Generation
add_children("Serug", family_tree["Reu"].uuid, ["Nahor"])

# 18 Generation
add_children("Nahor", family_tree["Serug"].uuid, ["Terah"])

# 19 Generation
add_children("Terah", family_tree["Nahor"].uuid, ["Abraham (Abram)", "Nahor", "Haran", "Sarah"])

# 20 Generation
add_children("Abraham (Abram)", family_tree["Terah"].uuid, ["Isaac", "Ishmael", "Zimran", "Jokshan", "Medan", "Midian", "Ishbak", "Shuah"])
add_children("Nahor", family_tree["Terah"].uuid, ["Uz", "Buz", "Kemuel", "Chesed", "Hazo", "Phildash", "Jidlaph", "Bethuel", "Tebah", "Gaham", "Tahash", "Maacah"])
add_children("Haran", family_tree["Terah"].uuid, ["Milcah", "Lot", "Iscah"])

# 21 Generation
add_children("Isaac", family_tree["Abraham (Abram)"].uuid, ["Esau", "Jacob"])
add_children("Ishmael", family_tree["Abraham (Abram)"].uuid, ["Nabaioth (Nebajoth)", "Kedar", "Adbeel", "Mibsam", "Mishma", "Dumah", "Massa", "Hadad", "Tema", "Jetur", "Napsish", "Kedemah", "Mahalath", "Bashemath"])
add_children("Jokshan", family_tree["Abraham (Abram)"].uuid, ["Sheba", "Dedan"])
add_children("Midian", family_tree["Abraham (Abram)"].uuid, ["Ephah", "Epher", "Hanoch", "Abida", "Eldaah"])
add_children("Kemuel", family_tree["Nahor"].uuid, ["Aram"])
add_children("Bethuel", family_tree["Nahor"].uuid, ["Laban", "Rebekah"])
add_children("Lot", family_tree["Haran"].uuid, ["First Daughter", "Second Daughter", "Moab", "Ben-ammi"])

# 22 Generation
add_children("Esau", family_tree["Isaac"].uuid, ["Timnah*", "Aliah*", "Jetheth*", "Oholibamah*", "Elah*", "Pinon*", "Mibzar*", "Magdiel*", "Iram*", "Eliphaz", "Jeush", "Jaalam", "Korah", "Reuel"])
add_children("Jacob", family_tree["Isaac"].uuid, ["Reuben", "Simeon", "Levi", "Judah", "Issachar", "Zebulun", "Dinah", "Joseph", "Benjamin", "Dan", "Naphtali", "Gad", "Asher"])
add_children("Dedan", family_tree["Jokshan"].uuid, ["Asshurim", "Letushim", "Leummim"])
add_children("Laban", family_tree["Bethuel"].uuid, ["Leah", "Rachel"])

# 23 Generation
add_children("Eliphaz", family_tree["Esau"].uuid, ["Teman", "Omar", "Zepho", "Gatam", "Kenaz", "Korah", "Timna", "Amalek"])
add_children("Reuel", family_tree["Esau"].uuid, ["Nahath*", "Zerah*", "Shammah*", "Mizzah*"])
add_children("Reuben", family_tree["Jacob"].uuid, ["Hanoch", "Pallu", "Hezron", "Carmi", "Bohan*", "Elizur*", "Zaccur*", "Joel*", "Joel*", "Zichri*"])
add_children("Simeon", family_tree["Jacob"].uuid, ["Jemuel (Nemuel)", "Jamin", "Ohad", "Jarib", "Zerah", "Shaul", "Hori*"])
add_children("Levi", family_tree["Jacob"].uuid, ["Gershon", "Kohath", "Merari", "Jochebed", "Kemuel*", "Shimei*"])
add_children("Judah", family_tree["Jacob"].uuid, ["Er", "Onan", "Shelah", "Perez", "Zerah", "Shobal"])
add_children("Issachar", family_tree["Jacob"].uuid, ["Tola", "Puah", "Jashub (Job)", "Shimron", "Zuar*", "Michael*", "Dodo*", "Azzan*", "Joseph*"])
add_children("Zebulun", family_tree["Jacob"].uuid, ["Sered", "Elon", "Jahleel", "Elon*", "Helon*", "Sodi*", "Parnach*", "Obadiah*"])
add_children("Joseph", family_tree["Jacob"].uuid, ["Manasseh", "Ephraim"])
add_children("Benjamin", family_tree["Jacob"].uuid, ["Bela", "Jediael", "Becher", "Ashbel", "Gera", "Naaman", "Ehi", "Rosh", "Muppim", "Huppin", "Ard", "Aharah", "Nohah", "Rapha", "Aphiah*", "Matri*", "Gideoni*", "Raphu*", "Shaharaim*", "Chislon*", "Bichri*", "Rimmon*"])
add_children("Dan", family_tree["Jacob"].uuid, ["Hushim", "Ammiahaddai*", "Gemalli*", "Ahisamach*", "Dibri*", "Manoah*"])
add_children("Naphtali", family_tree["Jacob"].uuid, ["Jahzeel", "Geni", "Jezer", "Shillem", "Vopshi*", "Ammihud*", "Asiel*", "Enan*", "Azrel*"])
add_children("Gad", family_tree["Jacob"].uuid, ["Ziphion", "Haggi", "Shuni", "Ezbon", "Eri", "Arodi", "Areli", "Deuel*", "Machi*", "Unknown*", "Bani*", "Buz*", "Guni*", "Unknown Descendant of Gad*", "Joel*", "Shapham*", "Jannai*", "Shaphat*"])
add_children("Asher", family_tree["Jacob"].uuid, ["Imnah (Jimnah)", "Ishauah", "Isui", "Beriah", "Sarah", "Jether*", "Phanuel*", "Michael*"])
# 24 Generation
add_children("Reuben (1st)", family_tree[None].uuid, ["Pallu", "Zaccur*", "Joel*", "Joel*"])
add_children("Pallu", family_tree["Reuben (1st)"].uuid, ["Eliab", "Peleth*"])
add_children("Zaccur*", family_tree["Reuben (1st)"].uuid, ["Shammua"])
add_children("Joel*", family_tree["Reuben (1st)"].uuid, ["Shemaiah"])
add_children("Joel*", family_tree["Reuben (1st)"].uuid, ["Shema"])

add_children("Simeon (2nd)", family_tree[None].uuid, ["Shaul", "Hori*"])
add_children("Shaul", family_tree["Simeon (2nd)"].uuid, ["Shallum"])
add_children("Hori*", family_tree["Simeon (2nd)"].uuid, ["Shaphat"])

add_children("Levi (3rd)", family_tree[None].uuid, ["Gershon", "Kohath", "Merari", "Kemuel*", "Shimei*"])
add_children("Gershon", family_tree["Levi (3rd)"].uuid, ["Libni (Ladan)", "Shimei", "Lael*", "Jahath"])
add_children("Kohath", family_tree["Levi (3rd)"].uuid, ["Amram", "Izhar", "Hebron", "Uzziel"])
add_children("Merari", family_tree["Levi (3rd)"].uuid, ["Mahli", "Mushi", "Hosah*", "Jaaziah*", "Abdi*"])
add_children("Kemuel*", family_tree["Levi (3rd)"].uuid, ["Hashabiah"])
add_children("Shimei*", family_tree["Levi (3rd)"].uuid, ["Shelomoth", "Haziel", "Haran", "Jahath", "Zina", "Jeush", "Beriah"])

add_children("Judah (4th)", family_tree[None].uuid, ["Shelah", "Perez", "Zerah", "Shobal"])
add_children("Shelah", family_tree["Judah (4th)"].uuid, ["Er", "Laadah", "Jokim", "Joash", "Saraph"])
add_children("Perez", family_tree["Judah (4th)"].uuid, ["Hezron", "Hamul"])
add_children("Zerah", family_tree["Judah (4th)"].uuid, ["Zimri (Zabdi)", "Ethan", "Heman", "Calcol", "Dara"])
add_children("Shobal", family_tree["Judah (4th)"].uuid, ["Reaiah"])

add_children("Issachar (9th)", family_tree[None].uuid, ["Tola", "Zuar*", "Michael*", "Dodo*", "Azzan*"])
add_children("Tola", family_tree["Issachar (9th)"].uuid, ["Uzzi", "Rephaiah", "Jeriel", "Jahmai", "Ibsam", "Shemuel"])
add_children("Zuar*", family_tree["Issachar (9th)"].uuid, ["Nethanel"])
add_children("Michael*", family_tree["Issachar (9th)"].uuid, ["Omri"])
add_children("Dodo*", family_tree["Issachar (9th)"].uuid, ["Puah"])
add_children("Azzan*", family_tree["Issachar (9th)"].uuid, ["Paltiel"])

add_children("Joseph (11th)", family_tree[None].uuid, ["Manasseh", "Ephraim"])
add_children("Manasseh", family_tree["Joseph (11th)"].uuid, ["Asriel", "Machir", "Unknown"])
add_children("Ephraim", family_tree["Joseph (11th)"].uuid, ["Shuthelah", "Beriah", "Shiphtan*", "Hillel*", "Azaziah*", "Zuph*"])

add_children("Benjamin (12th)", family_tree[None].uuid, ["Bela", "Jediael", "Gera", "Aphiah*", "Matri*", "Gideoni*", "Raphu*", "Bichri*", "Rimmon*"])
add_children("Bela", family_tree["Benjamin (12th)"].uuid, ["Ard (Addar)", "Naaman", "Ezbon", "Uzzi", "Uzziel", "Jerimoth", "Iri", "Gera"])
add_children("Jediael", family_tree["Benjamin (12th)"].uuid, ["Bilhan"])
add_children("Gera", family_tree["Benjamin (12th)"].uuid, ["Shimei*", "Ehud*"])
add_children("Aphiah*", family_tree["Benjamin (12th)"].uuid, ["Bechorah"])
add_children("Matri*", family_tree["Benjamin (12th)"].uuid, ["Jeiel*"])
add_children("Gideoni*", family_tree["Benjamin (12th)"].uuid, ["Abidan"])
add_children("Raphu*", family_tree["Benjamin (12th)"].uuid, ["Palti"])
add_children("Bichri*", family_tree["Benjamin (12th)"].uuid, ["Sheba"])
add_children("Rimmon*", family_tree["Benjamin (12th)"].uuid, ["Baanah", "Rechab"])

add_children("Dan (5th)", family_tree[None].uuid, ["Ammiahaddai*", "Gemalli*", "Ahisamach*", "Dibri*", "Manoah*"])
add_children("Ammiahaddai*", family_tree["Dan (5th)"].uuid, ["Ahiezer"])
add_children("Gemalli*", family_tree["Dan (5th)"].uuid, ["Ammiel"])
add_children("Ahisamach*", family_tree["Dan (5th)"].uuid, ["Oholiab"])
add_children("Dibri*", family_tree["Dan (5th)"].uuid, ["Shelomith"])
add_children("Manoah*", family_tree["Dan (5th)"].uuid, ["Samson"])

add_children("Naphtali (6th)", family_tree[None].uuid, ["Vopshi*", "Ammihud*", "Asiel*", "Enan*", "Azrel*"])
add_children("Vopshi*", family_tree["Naphtali (6th)"].uuid, ["Nahbi"])
add_children("Ammihud*", family_tree["Naphtali (6th)"].uuid, ["Pedahel"])
add_children("Asiel*", family_tree["Naphtali (6th)"].uuid, ["Raguel*"])
add_children("Enan*", family_tree["Naphtali (6th)"].uuid, ["Ahira"])
add_children("Azrel*", family_tree["Naphtali (6th)"].uuid, ["Jerimoth"])

add_children("Gad (7th)", family_tree[None].uuid, ["Deuel*", "Machi*", "Unknown*", "Buz*", "Guni*", "Unknown Descendant of Gad*", "Rimmon*"])
add_children("Deuel*", family_tree["Gad (7th)"].uuid, ["Eliasaph"])
add_children("Machi*", family_tree["Gad (7th)"].uuid, ["Geuel"])
add_children("Unknown*", family_tree["Gad (7th)"].uuid, ["Ezer*", "Obadiah*", "Eliab*", "Mishmannah*", "Jeremiah*", "Attai*", "Eliel*", "Johanan*", "Elzabad*", "Jeremiah*", "Machbanai*"])
add_children("Buz*", family_tree["Gad (7th)"].uuid, ["Jahdo"])
add_children("Guni*", family_tree["Gad (7th)"].uuid, ["Abdiel"])
add_children("Unknown Descendant of Gad*", family_tree["Gad (7th)"].uuid, ["Joel*", "Shapham*", "Jannai*", "Shaphat*"])
add_children("Rimmon*", family_tree["Gad (7th)"].uuid, ["Baanah", "Rechab"])

add_children("Asher (8th)", family_tree[None].uuid, ["Beriah", "Jether*", "Phanuel*", "Michael*"])
add_children("Beriah", family_tree["Asher (8th)"].uuid, ["Heber", "Malchiel"])
add_children("Jether*", family_tree["Asher (8th)"].uuid, ["Jephunneh", "Pispa", "Ara"])
add_children("Phanuel*", family_tree["Asher (8th)"].uuid, ["Anna"])
add_children("Michael*", family_tree["Asher (8th)"].uuid, ["Sethur"])

#25 Generation
# ... (Previous code for the 24th Generation)

add_children("Eliab", family_tree["Pallu"].uuid, ["Nemuel", "Dathan", "Abiram"])
add_children("Peleth*", family_tree["Pallu"].uuid, ["On"])
add_children("Shemaiah", family_tree["Joel*"].uuid, ["Gog"])
add_children("Shema", family_tree["Joel*"].uuid, ["Azaz"])
add_children("Shallum", family_tree["Shaul"].uuid, ["Mibsam"])
add_children("Lael*", family_tree["Gershon"].uuid, ["Eliasaph"])
add_children("Jahath", family_tree["Gershon"].uuid, ["Shimel"])
add_children("Izhar", family_tree["Kohath"].uuid, ["Korah", "Nepheg", "Zichri"])
add_children("Hebron", family_tree["Kohath"].uuid, ["Jeriah", "Amariah", "Jehaziel", "Jekameam"])
add_children("Uzziel", family_tree["Kohath"].uuid, ["Mishael", "Elzaphan", "Sithri", "Micah", "Isshiah"])
add_children("Mahli", family_tree["Merari"].uuid, ["Eleazar", "Kish", "Libni"])
add_children("Mushi", family_tree["Merari"].uuid, ["Mahli", "Eder", "Jeremoth"])
add_children("Hosah*", family_tree["Merari"].uuid, ["Shimri", "Hilkaih", "Tebaliah", "Zechariah"])
add_children("Jaaziah*", family_tree["Merari"].uuid, ["Beno", "Shoham", "Zaccur", "Ibri"])
add_children("Abdi*", family_tree["Merari"].uuid, ["Kish"])
add_children("Abihail*", family_tree["Merari"].uuid, ["Zuriel"])
add_children("Miriam", family_tree["Jochebed"].uuid, ["Uri", "Shobel", "Salma", "Hareph", "Etam", "Ishi*", "Abinadab*"])
add_children("Aaron", family_tree["Jochebed"].uuid, ["Nadab", "Abihu", "Eleazer", "Ithamar"])
add_children("Moses", family_tree["Jochebed"].uuid, ["Gershom", "Eliezer"])
add_children("Hashabiah", family_tree["Kemuel*"].uuid, ["Laadan"])
add_children("Er", family_tree["Shelah"].uuid, ["Lecah"])
add_children("Laadah", family_tree["Shelah"].uuid, ["Mareshah"])
add_children("Saraph", family_tree["Shelah"].uuid, ["Jashubilehem"])
add_children("Hezron", family_tree["Perez"].uuid, ["Jerahmeel", "Ram", "Caleb (Chelubai)", "Segub", "Ashhur"])
add_children("Zimri (Zabdi)", family_tree["Zerah"].uuid, ["Carmi"])
add_children("Ethan", family_tree["Zerah"].uuid, ["Azariah"])
add_children("Reaiah", family_tree["Shobal"].uuid, ["Jahath"])
add_children("Uzzi", family_tree["Tola"].uuid, ["Izrahiah"])
add_children("Puah", family_tree["Dodo*"].uuid, ["Tola"])
add_children("Machir", family_tree["Manasseh"].uuid, ["Peresh", "Sheresh", "Gilead", "Hammolechet", "Daughter of Machir"])
add_children("Unknown", family_tree["Manasseh"].uuid, ["Adnah*", "Jozabad*", "Jediael*", "Michael*", "Jediael*", "Elihu*", "Zillethai*", "Epher*", "Ishi*", "Eliel*", "Azriel*", "Jeremiah*", "Hodaviah*", "Jahdie*", "Pedahzur*", "Susi*", "Ephod*", "Jair*", "Nobah*"])
add_children("Shuthelah", family_tree["Ephraim"].uuid, ["Bered (Becher)"])
add_children("Beriah", family_tree["Ephraim"].uuid, ["Sheerah", "Rephah"])
add_children("Shiphtan*", family_tree["Ephraim"].uuid, ["Kemuel"])
add_children("Hillel*", family_tree["Ephraim"].uuid, ["Abdon"])
add_children("Azaziah*", family_tree["Ephraim"].uuid, ["Hoshea"])
add_children("Zuph*", family_tree["Ephraim"].uuid, ["Tohu"])
add_children("Bilhan", family_tree["Jediael"].uuid, ["Jeush", "Benjamin", "Ehud", "Chenaana", "Zethan", "Tarshish", "Ahishahar"])
add_children("Bechorah", family_tree["Aphiah*"].uuid, ["Zeror"])
add_children("Raguel*", family_tree["Asiel*"].uuid, ["Raphael"])
add_children("Jahdo", family_tree["Buz*"].uuid, ["Jeshishai"])
add_children("Abdiel", family_tree["Guni*"].uuid, ["Ahi"])
add_children("Heber", family_tree["Beriah"].uuid, ["Japhlet", "Shomer", "Hotham (Helem)", "Shua"])
add_children("Malchiel", family_tree["Beriah"].uuid, ["Birzaith"])

#26 Generation
add_children("Shimei", family_tree["Gog"].uuid, [])
add_children("Bela", family_tree["Azaz"].uuid, [])
add_children("Zechariah*", family_tree["Azaz"].uuid, [])
add_children("Jeiel*", family_tree["Azaz"].uuid, [])
add_children("Mishma", family_tree["Mibsam"].uuid, [])
add_children("Zimmah", family_tree["Shimel"].uuid, [])
add_children("Assir", family_tree["Korah"].uuid, [])
add_children("Elkanah", family_tree["Korah"].uuid, [])
add_children("Ebiasaph", family_tree["Korah"].uuid, [])
add_children("Shamir", family_tree["Micah"].uuid, [])
add_children("Zechariah", family_tree["Isshiah"].uuid, [])
add_children("Jerameel", family_tree["Kish"].uuid, [])
add_children("Shimei", family_tree["Libni"].uuid, [])
add_children("Mahli", family_tree["Mahli"].uuid, [])
add_children("Jerahmeel", family_tree["Kish"].uuid, [])
add_children("Bezaleel", family_tree["Uri"].uuid, [])
add_children("Reaiah", family_tree["Shobel"].uuid, [])
add_children("Kiriath-jearim", family_tree["Shobel"].uuid, [])
add_children("Horeth", family_tree["Shobel"].uuid, [])
add_children("Bethlehem", family_tree["Salma"].uuid, [])
add_children("Netophathites", family_tree["Salma"].uuid, [])
add_children("Ataroth", family_tree["Salma"].uuid, [])
add_children("Beth-Joab", family_tree["Salma"].uuid, [])
add_children("Manahethites", family_tree["Salma"].uuid, [])
add_children("Zorites", family_tree["Salma"].uuid, [])
add_children("Abinadab*", family_tree["Salma"].uuid, [])
add_children("Shimon*", family_tree["Salma"].uuid, [])
add_children("Bani*", family_tree["Salma"].uuid, [])
add_children("Beth-gader", family_tree["Hareph"].uuid, [])
add_children("Jezreel", family_tree["Etam"].uuid, [])
add_children("Ishma", family_tree["Etam"].uuid, [])
add_children("Idbash", family_tree["Etam"].uuid, [])
add_children("Hazzelelponi", family_tree["Etam"].uuid, [])
add_children("Phinehas", family_tree["Eleazer"].uuid, [])
add_children("Eli", family_tree["Ithamar"].uuid, [])
add_children("Shebuel", family_tree["Gershom"].uuid, [])
add_children("Jonathan", family_tree["Gershom"].uuid, [])
add_children("Rehabiah", family_tree["Eliezer"].uuid, [])
add_children("Jehiel", family_tree["Laadan"].uuid, [])
add_children("Zetham", family_tree["Laadan"].uuid, [])
add_children("Joel", family_tree["Laadan"].uuid, [])
add_children("Ram", family_tree["Jerahmeel"].uuid, [])
add_children("Bunah", family_tree["Jerahmeel"].uuid, [])
add_children("Oren", family_tree["Jerahmeel"].uuid, [])
add_children("Ozem", family_tree["Jerahmeel"].uuid, [])
add_children("Ahijah", family_tree["Jerahmeel"].uuid, [])
add_children("Onam", family_tree["Jerahmeel"].uuid, [])
add_children("Amminadab", family_tree["Ram"].uuid, [])
add_children("Juphunneh*", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Mesha", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Mareshah", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Jesher", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Shobab", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Ardon", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Hur", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Haran", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Moza", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Gazez", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Sheber", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Tirhanah", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Shaaph", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Sheva", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Achsah", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Jahdai", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Ulam", family_tree["Sheresh"].uuid, [])
add_children("Rekem", family_tree["Sheresh"].uuid, [])
add_children("Lezer (Jeezer)*", family_tree["Gilead"].uuid, [])
add_children("Helek*", family_tree["Gilead"].uuid, [])
add_children("Asriel*", family_tree["Gilead"].uuid, [])
add_children("Shechem*", family_tree["Gilead"].uuid, [])
add_children("Shemida*", family_tree["Gilead"].uuid, [])
add_children("Hepher*", family_tree["Gilead"].uuid, [])
add_children("Jephthah*", family_tree["Gilead"].uuid, [])
add_children("Ishhod", family_tree["Hammolechet"].uuid, [])
add_children("Abiezer", family_tree["Hammolechet"].uuid, [])
add_children("Mahlah", family_tree["Hammolechet"].uuid, [])
add_children("Tahath", family_tree["Bered"].uuid, [])
add_children("Resheph", family_tree["Rephah"].uuid, [])
add_children("Elihu", family_tree["Tohu"].uuid, [])
add_children("Abiel", family_tree["Zeror"].uuid, [])
add_children("Gabael", family_tree["Raphael"].uuid, [])
add_children("Michael", family_tree["Jeshishai"].uuid, [])
add_children("Pasach", family_tree["Japhlet"].uuid, [])
add_children("Bimhal", family_tree["Japhlet"].uuid, [])
add_children("Ashvath", family_tree["Japhlet"].uuid, [])
add_children("Ahi", family_tree["Shomer"].uuid, [])
add_children("Rohgah", family_tree["Shomer"].uuid, [])
add_children("Jehubbah", family_tree["Shomer"].uuid, [])
add_children("Aram", family_tree["Shomer"].uuid, [])
add_children("Zophah", family_tree["Hotham (Helem)"].uuid, [])
add_children("Imna", family_tree["Hotham (Helem)"].uuid, [])
add_children("Shelesh", family_tree["Hotham (Helem)"].uuid, [])
add_children("Amal", family_tree["Hotham (Helem)"].uuid, [])

#27 Generation
# ... (Previous code for the 26th Generation)

add_children("Shimei", family_tree["Gog"].uuid, [])
add_children("Micah", family_tree["Shimei"].uuid, [])

add_children("Mishma", family_tree["Mibsam"].uuid, [])
add_children("Hammuel", family_tree["Mishma"].uuid, [])

add_children("Zimmah", family_tree["Shimel"].uuid, [])
add_children("Ethan", family_tree["Zimmah"].uuid, [])

add_children("Ebiasaph", family_tree["Korah"].uuid, [])
add_children("Assir", family_tree["Ebiasaph"].uuid, [])

add_children("Shimei", family_tree["Libni"].uuid, [])
add_children("Uzzah", family_tree["Shimei"].uuid, [])

add_children("Shemer", family_tree["Mahli"].uuid, [])
add_children("Bani", family_tree["Shemer"].uuid, [])

add_children("Reaiah", family_tree["Shobel"].uuid, [])
add_children("Jahath", family_tree["Reaiah"].uuid, [])

add_children("Kiriath-jearim", family_tree["Shobel"].uuid, [])
add_children("Ithrites", family_tree["Kiriath-jearim"].uuid, [])
add_children("Puhites", family_tree["Kiriath-jearim"].uuid, [])
add_children("Shumathites", family_tree["Kiriath-jearim"].uuid, [])
add_children("Mishraites", family_tree["Kiriath-jearim"].uuid, [])

add_children("Abinadab*", family_tree["Salma"].uuid, [])
add_children("Eleazar", family_tree["Abinadab*"].uuid, [])
add_children("Uzzah", family_tree["Abinadab*"].uuid, [])

add_children("Shimon*", family_tree["Salma"].uuid, [])
add_children("Amnon", family_tree["Shimon*"].uuid, [])
add_children("Rinnah", family_tree["Shimon*"].uuid, [])
add_children("Benhanan", family_tree["Shimon*"].uuid, [])
add_children("Tilon", family_tree["Shimon*"].uuid, [])

add_children("Phinehas", family_tree["Eleazer"].uuid, [])
add_children("Abishua", family_tree["Phinehas"].uuid, [])

add_children("Eli", family_tree["Ithamar"].uuid, [])
add_children("Hophni", family_tree["Eli"].uuid, [])
add_children("Phinehas", family_tree["Eli"].uuid, [])

add_children("Jonathan", family_tree["Gershom"].uuid, [])
add_children("Jeahdeiah", family_tree["Jonathan"].uuid, [])

add_children("Ram", family_tree["Jerahmeel"].uuid, [])
add_children("Maaz", family_tree["Ram"].uuid, [])
add_children("Jamin", family_tree["Ram"].uuid, [])
add_children("Eker", family_tree["Ram"].uuid, [])

add_children("Onam", family_tree["Jerahmeel"].uuid, [])

add_children("Amminadab", family_tree["Ram"].uuid, [])
add_children("Nahshon (Naashon)", family_tree["Amminadab"].uuid, [])
add_children("Elisheba", family_tree["Amminadab"].uuid, [])

add_children("Juphunneh*", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Caleb", family_tree["Juphunneh*"].uuid, [])
add_children("Kenaz", family_tree["Juphunneh*"].uuid, [])
add_children("Jehallele*", family_tree["Juphunneh*"].uuid, [])

add_children("Mareshah", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Hebron", family_tree["Mareshah"].uuid, [])

add_children("Jahdai", family_tree["Caleb (Chelubai)"].uuid, [])
add_children("Regem", family_tree["Jahdai"].uuid, [])
add_children("Jotham", family_tree["Jahdai"].uuid, [])
add_children("Geshan", family_tree["Jahdai"].uuid, [])
add_children("Pelet", family_tree["Jahdai"].uuid, [])
add_children("Ephah", family_tree["Jahdai"].uuid, [])
add_children("Shaaph", family_tree["Jahdai"].uuid, [])

add_children("Koz (Coz)", family_tree["Ashhur"].uuid, [])
add_children("Anub", family_tree["Koz (Coz)"].uuid, [])
add_children("Zobebah", family_tree["Koz (Coz)"].uuid, [])
add_children("Harum", family_tree["Koz (Coz)"].uuid, [])

add_children("Ulam", family_tree["Sheresh"].uuid, [])
add_children("Bedan", family_tree["Ulam"].uuid, [])

add_children("Shemida*", family_tree["Gilead"].uuid, [])
add_children("Ahian", family_tree["Shemida*"].uuid, [])
add_children("Shechem", family_tree["Shemida*"].uuid, [])
add_children("Likhi", family_tree["Shemida*"].uuid, [])
add_children("Aniam", family_tree["Shemida*"].uuid, [])

add_children("Hepher*", family_tree["Gilead"].uuid, [])
add_children("Zelophehad", family_tree["Hepher*"].uuid, [])

add_children("Abiezer", family_tree["Hammolechet"].uuid, [])
add_children("Joash*", family_tree["Abiezer"].uuid, [])

add_children("Tahath", family_tree["Bered"].uuid, [])
add_children("Eleadah", family_tree["Tahath"].uuid, [])

add_children("Resheph", family_tree["Rephah"].uuid, [])
add_children("Resheph", family_tree["Resheph"].uuid, [])

add_children("Elihu", family_tree["Tohu"].uuid, [])
add_children("Jeroham", family_tree["Elihu"].uuid, [])

add_children("Abiel", family_tree["Zeror"].uuid, [])
add_children("Kish", family_tree["Abiel"].uuid, [])
add_children("Ner", family_tree["Abiel"].uuid, [])

add_children("Gabael", family_tree["Raphael"].uuid, [])
add_children("Aduel", family_tree["Gabael"].uuid, [])

add_children("Michael", family_tree["Jeshishai"].uuid, [])
add_children("Gilead", family_tree["Michael"].uuid, [])

add_children("Zophah", family_tree["Hotham (Helem)"].uuid, [])
add_children("Shuh", family_tree["Zophah"].uuid, [])
add_children("Harnepher", family_tree["Zophah"].uuid, [])
add_children("Shual", family_tree["Zophah"].uuid, [])
add_children("Beri", family_tree["Zophah"].uuid, [])
add_children("Imrah", family_tree["Zophah"].uuid, [])
add_children("Bezer", family_tree["Zophah"].uuid, [])
add_children("Hod", family_tree["Zophah"].uuid, [])
add_children("Shamma", family_tree["Zophah"].uuid, [])
add_children("Shilshah", family_tree["Zophah"].uuid, [])
add_children("Ithran", family_tree["Zophah"].uuid, [])
add_children("Beera", family_tree["Zophah"].uuid, [])

# ... (Continuing for other individuals)




# Function to print the family tree recursively
def print_family_tree(person, generation=1):
    indentation = "    " * generation
    print(f"{indentation}+ {person
