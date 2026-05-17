"""
Batch 67d: Create/update key New Testament people entities referenced by Jesus Christ.
- peter-the-apostle (Person, Class 252)
- mary-magdalene (Person, Class 252)
- pontius-pilate (Person, Class 252)
- paul-the-apostle enrichment (Person, Class 252) — add evidence + texts
Also update dead-sea-scrolls (Text, Class 810) — add summary + relationships
"""
import json
import os
import datetime

NOW = datetime.datetime.utcnow().isoformat() + "+00:00"
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-67-may2026"
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "appwrite-export", "entities")


def make_entity_file(class_code: str, slug: str, name: str, label: str, era: str,
                     call_number: str, details: dict) -> dict:
    details.setdefault("sessionId", SESSION_ID)
    details.setdefault("enrichedBy", EDITOR_ID)
    details.setdefault("enrichedAt", NOW)
    if "_editLog" not in details:
        details["_editLog"] = []
    return {
        "_meta": {
            "classCode": class_code,
            "exportedAt": NOW,
            "source": "local-bot"
        },
        "entities": [{
            "slug": slug,
            "name": name,
            "label": label,
            "era": era,
            "callNumber": call_number,
            "_unsyncedEdits": True,
            "detailsJson": json.dumps(details, ensure_ascii=False)
        }]
    }


def save(class_code: str, filename: str, data: dict):
    dir_name = f"{class_code}-Class-{class_code}"
    dir_path = os.path.join(BASE, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    path = os.path.join(dir_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {path}")
    return path


def patch_existing(path: str, new_details: dict) -> bool:
    """Merge new_details into existing entity's detailsJson."""
    with open(path) as f:
        data = json.load(f)
    e = data["entities"][0]
    existing = json.loads(e.get("detailsJson", "{}"))
    # Merge — new values win
    existing.update(new_details)
    e["detailsJson"] = json.dumps(existing, ensure_ascii=False)
    e["_unsyncedEdits"] = True
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return True


# =============================================================================
# 1. PETER THE APOSTLE
# =============================================================================
peter_details = {
    "summary": (
        "Simon Peter (died c. 64–68 CE) was a Galilean fisherman who became the leading apostle of Jesus Christ "
        "and the foundational figure of the Christian Church. Born in Bethsaida and working in Capernaum, he was "
        "called by Jesus alongside his brother Andrew and renamed 'Peter' (Aramaic: Kephas, meaning 'rock'), "
        "symbolizing his future role. His impulsive devotion, including his confession of Jesus as the Messiah at "
        "Caesarea Philippi, and his later denial of Jesus on the night of the arrest, make him the most humanly "
        "complex figure in the Gospels.\n\n"
        "After the resurrection, Peter became the de facto leader of the Jerusalem church. His speech at Pentecost, "
        "recorded in Acts 2, is credited as the first Christian sermon. He performed healings, presided over the "
        "admission of Gentiles (the baptism of Cornelius, Acts 10), and was imprisoned by Herod Agrippa. His "
        "encounter with Paul in Antioch — the 'incident at Antioch' (Galatians 2:11–14) — reveals the early "
        "tensions between Jewish and Gentile Christianity.\n\n"
        "Peter's legacy is immense: he is regarded as the first pope by the Catholic Church, with his authority "
        "grounded in Matthew 16:18 ('upon this rock I will build my church'). Tradition holds that he was martyred "
        "in Rome under Nero, crucified upside down at his own request out of humility. The Vatican Basilica stands "
        "over his traditional tomb. Two New Testament epistles bear his name, and the Gospel of Mark is considered "
        "to reflect his eyewitness testimony.\n\n"
        "'You are the Christ, the Son of the living God.' — Peter's confession at Caesarea Philippi (Matthew 16:16)"
    ),
    "causes": [
        "Jesus's call of Simon and Andrew from their fishing nets (Mark 1:16–18)",
        "Peter's confession of Jesus as Messiah at Caesarea Philippi",
        "The post-resurrection appearances giving Peter renewed leadership",
        "Pentecost empowerment (Acts 2) energizing his public preaching"
    ],
    "effects": [
        "First public proclamation of the gospel at Pentecost (Acts 2), converting 3,000",
        "Presiding over the Jerusalem church and its council decisions on Gentile admission",
        "Catholic papal succession doctrine rooted in Petrine authority (Matthew 16:18)",
        "Martyrdom in Rome anchoring early Christian community there",
        "Gospel of Mark preserving his eyewitness testimony of Jesus"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "First and foremost among the Twelve Apostles; confessed Jesus as Messiah"},
        {"verb": "INFLUENCES", "targetSlug": "roman-catholic-church", "targetName": "Roman Catholic Church",
         "context": "Regarded as the first pope; Petrine authority is the theological basis for papal succession"},
        {"verb": "INFLUENCES", "targetSlug": "gospel-of-mark", "targetName": "Gospel of Mark",
         "context": "Early tradition (Papias) identifies Mark's Gospel as recording Peter's preaching"},
        {"verb": "INFLUENCES", "targetSlug": "paul-the-apostle", "targetName": "Paul the Apostle",
         "context": "Peter met with Paul in Jerusalem (Galatians 1:18); conflict in Antioch (Galatians 2)"},
        {"verb": "OCCURS_IN", "targetSlug": "jerusalem", "targetName": "Jerusalem",
         "context": "Led the Jerusalem church; preached at Pentecost in Jerusalem"},
        {"verb": "OCCURS_DURING", "targetSlug": "classical-3000bce-500ce", "targetName": "Classical Era",
         "context": "Died c. 64–68 CE under Nero's persecution in Rome"},
        {"verb": "AUTHORS", "targetSlug": "first-epistle-of-peter", "targetName": "First Epistle of Peter",
         "context": "New Testament letter attributed to Peter, addressing dispersed Christians"},
        {"verb": "TRANSMITS", "targetSlug": "early-church", "targetName": "Early Church",
         "context": "Led the earliest Christian community in Jerusalem and Antioch"}
    ],
    "texts": [
        {
            "title": "First Epistle of Peter",
            "slug": "first-epistle-of-peter",
            "type": "scripture",
            "year": "c. 60–90 CE",
            "description": "New Testament letter attributed to Peter, encouraging Christians facing persecution"
        },
        {
            "title": "Gospel of Mark",
            "slug": "gospel-of-mark",
            "type": "scripture",
            "year": "c. 65–70 CE",
            "description": "Considered to reflect Peter's eyewitness testimony of Jesus's ministry"
        },
        {
            "title": "Acts of the Apostles",
            "slug": "acts-of-the-apostles",
            "type": "scripture",
            "year": "c. 80–90 CE",
            "description": "Primary source for Peter's leadership in the Jerusalem church and Pentecost sermon"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "Acts of the Apostles, chapters 1–15",
            "note": "Primary historical source for Peter's leadership in the early church",
            "citationStyle": "chapter:verse"
        },
        {
            "tier": "A",
            "source": "Galatians 1:18–2:14 (Paul's epistles)",
            "note": "Paul's first-person account of meeting Peter in Jerusalem and the Antioch incident",
            "citationStyle": "chapter:verse"
        },
        {
            "tier": "B",
            "source": "Clement of Rome, 1 Clement c. 96 CE",
            "note": "Early attestation of Peter's martyrdom in Rome",
            "citationStyle": "chapter"
        },
        {
            "tier": "C",
            "source": "Raymond E. Brown, An Introduction to the New Testament (1997)",
            "note": "Scholarly analysis of the Petrine letters and historical Peter",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "c. 1 BCE", "event": "Born in Bethsaida, Galilee (tradition)"},
        {"year": "c. 28–30 CE", "event": "Called by Jesus from fishing on the Sea of Galilee"},
        {"year": "c. 30 CE", "event": "Confession at Caesarea Philippi: 'You are the Christ'"},
        {"year": "c. 33 CE", "event": "Three-fold denial of Jesus on the night of arrest"},
        {"year": "c. 33 CE", "event": "Post-resurrection appearances restore his leadership"},
        {"year": "c. 33 CE", "event": "Pentecost sermon in Jerusalem converts 3,000"},
        {"year": "c. 49 CE", "event": "Jerusalem Council: affirms Gentile admission without circumcision"},
        {"year": "c. 50 CE", "event": "Conflict with Paul in Antioch over table fellowship"},
        {"year": "c. 64–68 CE", "event": "Martyrdom in Rome under Nero; crucified upside down by tradition"}
    ],
    "places": [
        {"name": "Bethsaida", "type": "birthplace"},
        {"name": "Capernaum", "type": "home base"},
        {"name": "Jerusalem", "type": "ministry center"},
        {"name": "Rome", "type": "martyrdom location"}
    ],
    "quote": "You are the Christ, the Son of the living God. — Peter's confession (Matthew 16:16)",
    "frameworks": [
        "theological-history", "biography", "religious-movements", "institution-building"
    ],
    "historicalSignificance": {
        "significanceScore": 9,
        "significanceNarrative": "Peter is the most consequential figure in early Christianity after Jesus himself. His leadership shaped the Jerusalem church, his martyrdom in Rome anchored Western Christianity there, and his authority became the theological foundation of the papacy — one of the most enduring institutions in human history.",
        "significanceCategory": "world-changing"
    }
}
peter_data = make_entity_file("252", "peter-the-apostle", "Peter the Apostle",
                               "Person", "Classical", "252.peter-the-apostle", peter_details)
save("252", "252peter-the-apostle.json", peter_data)
print("Created peter-the-apostle: OK")


# =============================================================================
# 2. MARY MAGDALENE
# =============================================================================
mary_details = {
    "summary": (
        "Mary Magdalene (active c. 28–33 CE) was a Jewish woman from Magdala on the Sea of Galilee who became one "
        "of the most prominent followers of Jesus Christ. She is described in all four Gospels as having been healed "
        "by Jesus ('seven demons cast out', Luke 8:2) and subsequently joining his itinerant ministry. Unlike the "
        "male disciples who fled at the arrest, Mary Magdalene and other women remained at the crucifixion and burial "
        "— a witness role the Gospel writers consistently emphasize.\n\n"
        "Her most transformative moment is the resurrection appearance: all four Gospels record that women came first "
        "to the empty tomb, and in John's Gospel, Mary Magdalene is explicitly the first person to whom the risen "
        "Jesus appeared (John 20:11–18). Jesus commissions her to announce the resurrection to the other disciples — "
        "earning her the title 'Apostle to the Apostles' (apostola apostolorum) in patristic tradition. This role "
        "made her a subject of intense early Christian reflection and later controversy.\n\n"
        "Mary Magdalene's reputation was complicated by a 6th-century conflation — by Pope Gregory I (591 CE) — "
        "with the unnamed sinful woman of Luke 7 and Mary of Bethany, a fusion rejected by modern scholarship and "
        "formally corrected by the Catholic Church in 1969. She was elevated to feast day status in 2016. Gnostic "
        "gospels such as the Gospel of Mary and Gospel of Philip cast her as a favored disciple in conflict with "
        "Peter, reflecting early disputes about women's spiritual authority.\n\n"
        "'Woman, why are you weeping? Whom are you seeking?' — Jesus to Mary at the empty tomb (John 20:15)"
    ),
    "causes": [
        "Healing by Jesus (described as exorcism of seven demons, Luke 8:2)",
        "Her decision to remain at the crucifixion when male disciples fled",
        "Arriving at the tomb on the third day to anoint the body"
    ],
    "effects": [
        "First witness to the resurrection in all Gospel accounts (primary or explicitly named)",
        "First to proclaim the resurrection to the other apostles — 'Apostle to the Apostles'",
        "Subject of significant Gnostic Christian texts asserting her spiritual authority over Peter",
        "Her conflation with Luke 7's sinful woman shaped Western Christian views of female sexuality for 1,400 years",
        "2016 elevation of her feast day to apostolic ranking by the Catholic Church"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "One of Jesus's most devoted followers; first witness to the resurrection"},
        {"verb": "INFLUENCES", "targetSlug": "early-church", "targetName": "Early Church",
         "context": "Her 'Apostle to the Apostles' role was cited in debates about women's ministry"},
        {"verb": "OCCURS_IN", "targetSlug": "jerusalem", "targetName": "Jerusalem",
         "context": "Present at crucifixion and first at the empty tomb outside Jerusalem"},
        {"verb": "OCCURS_DURING", "targetSlug": "classical-3000bce-500ce", "targetName": "Classical Era",
         "context": "Active during Jesus's Galilean ministry c. 28–33 CE"},
        {"verb": "TRANSMITS", "targetSlug": "gospel-of-john", "targetName": "Gospel of John",
         "context": "John 20 gives her the fullest post-resurrection encounter narrative"}
    ],
    "texts": [
        {
            "title": "Gospel of John",
            "slug": "gospel-of-john",
            "type": "scripture",
            "year": "c. 90–100 CE",
            "description": "John 20:1–18 records her as the first to see the risen Jesus"
        },
        {
            "title": "Gospel of Mary",
            "slug": "gospel-of-mary",
            "type": "gnostic-text",
            "year": "c. 2nd century CE",
            "description": "Gnostic gospel presenting Mary Magdalene as a favored disciple surpassing Peter"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "All four canonical Gospels (Matthew 27–28, Mark 15–16, Luke 8 & 24, John 20)",
            "note": "Consistent attestation across all four Gospels of her presence at crucifixion and tomb",
            "citationStyle": "chapter:verse"
        },
        {
            "tier": "C",
            "source": "Elizabeth Schüssler Fiorenza, In Memory of Her (1983)",
            "note": "Feminist theological reconstruction of Mary Magdalene's historical role",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "c. 28 CE", "event": "Joined Jesus's itinerant ministry after healing in Galilee"},
        {"year": "c. 33 CE", "event": "Present at the crucifixion of Jesus at Golgotha (all four Gospels)"},
        {"year": "c. 33 CE", "event": "First witness to the empty tomb; first to see the risen Jesus (John 20)"},
        {"year": "591 CE", "event": "Pope Gregory I conflates her with Luke 7's sinful woman in a sermon"},
        {"year": "1969 CE", "event": "Catholic Church separates her feast from Luke 7's sinful woman"},
        {"year": "2016 CE", "event": "Feast day elevated to double feast, equivalent to apostolic feasts"}
    ],
    "places": [
        {"name": "Magdala", "type": "hometown"},
        {"name": "Jerusalem", "type": "witness location"}
    ],
    "quote": "Woman, why are you weeping? Whom are you seeking? — Jesus to Mary at the empty tomb (John 20:15)",
    "frameworks": [
        "theological-history", "biography", "gender-history", "religious-movements"
    ],
    "historicalSignificance": {
        "significanceScore": 7,
        "significanceNarrative": "Mary Magdalene was the first witness to the defining claim of Christianity — the resurrection. Her role as 'Apostle to the Apostles' made her a flashpoint for 2,000 years of debates about women's authority in religion. Few figures have been more misrepresented or more recently rehabilitated in scholarly and ecclesiastical rethinking.",
        "significanceCategory": "continental"
    }
}
mary_data = make_entity_file("252", "mary-magdalene", "Mary Magdalene",
                              "Person", "Classical", "252.mary-magdalene", mary_details)
save("252", "252mary-magdalene.json", mary_data)
print("Created mary-magdalene: OK")


# =============================================================================
# 3. PONTIUS PILATE
# =============================================================================
pilate_details = {
    "summary": (
        "Pontius Pilate (governed 26–36 CE) was the fifth Roman prefect of the province of Judaea, appointed by "
        "Emperor Tiberius. He is primarily remembered in history as the Roman official who authorized the crucifixion "
        "of Jesus of Nazareth c. 30–33 CE. His name appears in three early extra-biblical sources — Tacitus, "
        "Josephus, and the Pilate Stone discovered at Caesarea Maritima in 1961 — making him one of the best-attested "
        "Roman officials in Palestine during the first century.\n\n"
        "Pilate's tenure was marked by repeated provocations against Jewish religious sensibilities: he introduced "
        "Roman military standards bearing the emperor's image into Jerusalem, appropriated Temple funds to build an "
        "aqueduct, and massacred a group of Samaritans — the incident that led to his recall to Rome. The trial of "
        "Jesus, as recorded in all four Gospels, depicts Pilate as ambivalent — finding 'no fault' in Jesus but "
        "bowing to crowd pressure and handing him over for crucifixion. The Latin phrase 'sub Pontio Pilato' (under "
        "Pontius Pilate) appears in both the Apostles' Creed and Nicene Creed, anchoring the crucifixion historically.\n\n"
        "Pilate's fate after his recall to Rome in 36 CE is unknown. Eusebius of Caesarea recorded a tradition that "
        "he committed suicide under Caligula, though this is uncertain. He appears as a surprisingly complex figure "
        "in early Christian literature — even venerated as a saint in the Ethiopian and Coptic churches. The Pilate "
        "Stone remains the only physical inscription confirming his name and title.\n\n"
        "'What is truth?' — Pilate's question to Jesus (John 18:38)"
    ),
    "causes": [
        "Appointment by Tiberius as prefect of Judaea in 26 CE",
        "Roman policy of delegating capital punishment through local prefects in occupied territories",
        "Jewish high priests' request to condemn Jesus on charges of sedition"
    ],
    "effects": [
        "Authorization of the crucifixion of Jesus, anchoring the event in Roman imperial history",
        "His name embedded in both the Apostles' Creed and Nicene Creed as a historical timestamp",
        "The Pilate Stone (1961) provides the only non-literary confirmation of his existence and title",
        "His recalled from Judaea after the Samaritan massacre ended a turbulent decade of Roman-Jewish relations"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "Authorized the crucifixion of Jesus after the Sanhedrin trial; Gospel trial narrative"},
        {"verb": "OCCURS_IN", "targetSlug": "jerusalem", "targetName": "Jerusalem",
         "context": "Seat of Roman administration during the trial of Jesus"},
        {"verb": "OCCURS_DURING", "targetSlug": "classical-3000bce-500ce", "targetName": "Classical Era",
         "context": "Governed Judaea 26–36 CE under Emperor Tiberius"},
        {"verb": "TRANSMITS", "targetSlug": "roman-empire", "targetName": "Roman Empire",
         "context": "Represented Roman imperial authority in Judaea"}
    ],
    "texts": [
        {
            "title": "Tacitus, Annals XV.44",
            "slug": "tacitus-annals",
            "type": "historical",
            "year": "c. 116 CE",
            "description": "Names Pilate explicitly as the official who executed Christus under Tiberius"
        },
        {
            "title": "Josephus, Antiquities 18.3.1",
            "slug": "josephus-antiquities",
            "type": "historical",
            "year": "c. 93 CE",
            "description": "References Pilate's role in Jesus's death and his other provocations in Judaea"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "Pilate Stone, Caesarea Maritima (discovered 1961)",
            "note": "Latin inscription naming 'Pontius Pilate, Prefect of Judaea' — only physical evidence of his existence",
            "citationStyle": "archaeological"
        },
        {
            "tier": "B",
            "source": "Tacitus, Annals 15.44 (c. 116 CE)",
            "note": "Roman historian explicitly names Pilate as the official who executed Christus under Tiberius",
            "citationStyle": "book:chapter"
        },
        {
            "tier": "B",
            "source": "Josephus, Antiquities of the Jews 18.3 (c. 93 CE)",
            "note": "Jewish historian references Pilate's administration and provocations in Judaea",
            "citationStyle": "book:chapter"
        }
    ],
    "timeline": [
        {"year": "26 CE", "event": "Appointed by Emperor Tiberius as prefect of Judaea"},
        {"year": "26 CE", "event": "Introduces Roman military standards into Jerusalem — first major provocation"},
        {"year": "c. 30–33 CE", "event": "Presides over the trial and crucifixion of Jesus of Nazareth"},
        {"year": "c. 36 CE", "event": "Massacres Samaritan pilgrims on Mount Gerizim"},
        {"year": "36 CE", "event": "Recalled to Rome by governor Vitellius following the Samaritan incident"},
        {"year": "1961 CE", "event": "Pilate Stone discovered at Caesarea Maritima, confirming his existence and title"}
    ],
    "places": [
        {"name": "Caesarea Maritima", "type": "administrative center"},
        {"name": "Jerusalem", "type": "site of Jesus's trial"}
    ],
    "quote": "What is truth? — Pilate's question to Jesus (John 18:38)",
    "frameworks": [
        "political-history", "theological-history", "roman-empire", "biography"
    ],
    "historicalSignificance": {
        "significanceScore": 7,
        "significanceNarrative": "Pontius Pilate is one of the most frequently named individuals in world religious history — his name appears billions of times in Christian recitations of the Apostles' Creed. His decision to crucify Jesus, reluctant or not, set in motion the founding narrative of the world's largest religion. The Pilate Stone remains a landmark of biblical archaeology.",
        "significanceCategory": "world-changing"
    }
}
pilate_data = make_entity_file("252", "pontius-pilate", "Pontius Pilate",
                                "Person", "Classical", "252.pontius-pilate", pilate_details)
save("252", "252pontius-pilate.json", pilate_data)
print("Created pontius-pilate: OK")


# =============================================================================
# 4. UPDATE DEAD SEA SCROLLS (enrich existing entity at 810-Class-810)
# =============================================================================
DSS_PATH = os.path.join(BASE, "810-Class-810", "81001-dead-sea-scrolls.json")
dss_update = {
    "summary": (
        "The Dead Sea Scrolls are a collection of approximately 981 ancient manuscripts discovered between 1947 and "
        "1956 in eleven caves near Khirbet Qumran on the northwestern shore of the Dead Sea. Composed primarily in "
        "Hebrew with portions in Aramaic and Greek, they date from the 3rd century BCE to the 1st century CE — the "
        "oldest surviving manuscripts of the Hebrew Bible, predating the previously known Masoretic Text by roughly "
        "one thousand years.\n\n"
        "The scrolls include every book of the Hebrew Bible except Esther, as well as sectarian texts, hymns, "
        "calendar documents, and legal codes associated with the Qumran community — widely identified as an Essene "
        "sect. Among the most significant finds: the Great Isaiah Scroll (1QIsa), complete and 2,100 years old; the "
        "Community Rule (1QS), describing the sect's initiation and communal life; and the War Scroll, depicting "
        "an apocalyptic battle between the 'Sons of Light' and 'Sons of Darkness.' The scrolls contain the earliest "
        "known commentary literature (pesharim) on biblical texts.\n\n"
        "The Dead Sea Scrolls transformed biblical scholarship. They demonstrated remarkable continuity of the "
        "biblical text across a millennium, while revealing the diversity of Second Temple Judaism — the matrix in "
        "which both rabbinic Judaism and Christianity emerged. They illuminate the world into which Jesus was born, "
        "including concepts (messianic expectation, divine sonship, communal meals) that parallel early Christian "
        "practice. The Shrine of the Book in Jerusalem houses the most iconic specimens.\n\n"
        "The discovery is ranked among the greatest archaeological finds of the 20th century."
    ),
    "causes": [
        "Qumran community's deliberate concealment of their library (c. 68 CE) ahead of the Roman destruction",
        "1947 discovery by Bedouin shepherd Muhammad edh-Dhib in Cave 1"
    ],
    "effects": [
        "Pushed back the oldest manuscript evidence for the Hebrew Bible by ~1,000 years",
        "Revealed remarkable fidelity of the Masoretic Text tradition over a millennium",
        "Illuminated Second Temple Jewish sectarianism — the world in which Jesus and early Christianity arose",
        "Generated the field of Dead Sea Scrolls studies; decades of international scholarly access disputes",
        "Opened the Isaiah Scroll as evidence for the unity of the Book of Isaiah (against the two-author hypothesis)"
    ],
    "relationships": [
        {"verb": "TRANSMITS", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "The scrolls illuminate the Jewish sectarian world into which Jesus was born; parallel messianic concepts"},
        {"verb": "INFLUENCES", "targetSlug": "early-church", "targetName": "Early Church",
         "context": "Concepts in the scrolls (communal meals, new covenant, Teacher of Righteousness) parallel early Christianity"},
        {"verb": "OCCURS_IN", "targetSlug": "jerusalem", "targetName": "Jerusalem",
         "context": "Housed in the Shrine of the Book, Israel Museum, Jerusalem"},
        {"verb": "OCCURS_DURING", "targetSlug": "classical-3000bce-500ce", "targetName": "Classical Era",
         "context": "Manuscripts date from 3rd century BCE to 68 CE — Second Temple period"}
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "The Great Isaiah Scroll (1QIsa), Israel Antiquities Authority",
            "note": "Complete biblical manuscript, c. 125 BCE — oldest surviving complete Old Testament book",
            "citationStyle": "manuscript"
        },
        {
            "tier": "B",
            "source": "Frank Moore Cross, The Ancient Library of Qumran (1958)",
            "note": "Foundational scholarly analysis of the Qumran community and scrolls",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "c. 3rd cent. BCE", "event": "Earliest manuscripts composed by the Qumran community"},
        {"year": "c. 68 CE", "event": "Scrolls hidden in caves ahead of Roman assault; Qumran destroyed"},
        {"year": "1947 CE", "event": "Cave 1 discovered by Bedouin shepherd; first seven scrolls identified"},
        {"year": "1947–1956 CE", "event": "Eleven caves excavated; ~981 manuscript fragments recovered"},
        {"year": "1955 CE", "event": "Millar Burrows publishes the first Dead Sea Scrolls facsimile edition"},
        {"year": "1991 CE", "event": "Huntington Library releases unauthorized photographs; access dispute resolved"},
        {"year": "2010s CE", "event": "Israel Antiquities Authority digitizes entire collection for public access"}
    ],
    "places": [
        {"name": "Qumran", "type": "discovery site"},
        {"name": "Jerusalem", "type": "current repository (Shrine of the Book)"}
    ],
    "frameworks": ["theological-history", "archaeology", "textual-criticism"],
    "historicalSignificance": {
        "significanceScore": 9,
        "significanceNarrative": "The Dead Sea Scrolls are the most important biblical manuscript discovery in modern history, predating previously known Old Testament manuscripts by a millennium and illuminating the world that gave birth to both Christianity and rabbinic Judaism. They are irreplaceable primary sources.",
        "significanceCategory": "world-changing"
    },
    "_unsyncedEdits": True
}
if os.path.exists(DSS_PATH):
    patch_existing(DSS_PATH, dss_update)
    print("Updated dead-sea-scrolls: OK")
else:
    dss_data = make_entity_file("810", "dead-sea-scrolls", "Dead Sea Scrolls",
                                 "Text", "Classical", "810.dead-sea-scrolls", dss_update)
    save("810", "81001-dead-sea-scrolls.json", dss_data)
    print("Created dead-sea-scrolls: OK")

print("\nBatch 67d complete. Created: Peter the Apostle, Mary Magdalene, Pontius Pilate; Updated: Dead Sea Scrolls")
