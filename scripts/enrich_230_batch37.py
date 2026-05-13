#!/usr/bin/env python3
"""
Batch 37 — 8 entities: Caesar Rodney, Robert Barnwell Rhett, Adolphe Crémieux,
William Jackson, Samuel McRoberts, William H. Cabell, Oliver H. Prince,
Thomas B. Robertson
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    # 1 — Caesar Rodney
    ("caesar-rodney", {
        "summary": (
            "Caesar Rodney (1728–1784) was a Delaware Founding Father, "
            "Continental Congressman, signer of the Declaration of "
            "Independence, and the hero of one of the most celebrated "
            "individual acts of the Revolutionary era: his legendary "
            "80-mile midnight ride through a thunderstorm from Dover, "
            "Delaware to Philadelphia to break the Delaware delegation's "
            "tie vote on independence on July 2, 1776. Ill with facial "
            "cancer, Rodney rode through rain and darkness overnight, "
            "arriving in time to vote for independence and give Delaware "
            "a 2-1 majority — providing the decisive contribution to "
            "the unanimous colonial vote that made the Declaration "
            "of Independence possible.\n\n"
            "Rodney served as a Continental Congressman from Delaware "
            "(1774–1776, 1777–1778), as a general in the Delaware militia, "
            "as Speaker of the Delaware Assembly, and as President of "
            "Delaware (1778–1781) — the state's highest executive office "
            "during the most critical years of the Revolutionary War. "
            "He administered Delaware's government while supporting the "
            "Continental Army and maintaining the state's commitment "
            "to the American cause.\n\n"
            "His facial cancer grew progressively more debilitating "
            "throughout his later years — he wore a green silk scarf "
            "over his face in public — yet he continued to serve in "
            "public office until he could no longer manage the journey. "
            "He died in 1784 at 56, before the Constitution was drafted, "
            "never seeing the full republic he helped found.\n\n"
            "His midnight ride is one of the founding era's most vivid "
            "moments of individual sacrifice for a larger cause — "
            "commemorated on Delaware's state quarter."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Founding Father; signer of the Declaration of Independence; President of Delaware (1778–1781); hero of the legendary 80-mile overnight ride to break Delaware's tie vote for independence on July 2, 1776 — despite being ill with facial cancer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's divided delegation — George Read voted against independence, Thomas McKean voted for it, creating a 1-1 tie that only Rodney's vote could break — made his 80-mile overnight ride a historical necessity if Delaware was to vote for independence",
            "His deep commitment to the colonial cause — rooted in Delaware's Quaker and Presbyterian traditions of political engagement and resistance to arbitrary authority — motivated him to ride through illness and storm to reach the decisive vote",
            "The Continental Congress's June 1776 independence debate and its July 2 vote — driven by Richard Henry Lee's resolution and Thomas Jefferson's draft declaration — created the exact historical moment that Rodney's midnight ride served"
        ],
        "effects": [
            "His July 2, 1776 vote broke Delaware's delegation tie — giving Delaware a 2-1 majority for independence and contributing to the unanimous colonial vote that made the Declaration of Independence possible as the unified voice of all thirteen colonies",
            "His presidency of Delaware (1778–1781) during the Revolutionary War's most critical years maintained Delaware's institutional continuity and its material support for the Continental Army through the darkest period of the war",
            "His signature on the Declaration of Independence made Delaware one of the thirteen founding states — his personal sacrifice becoming the permanent symbol of individual commitment to the founding cause",
            "His legacy as the hero of the midnight ride became one of the founding era's most enduring symbols of personal courage — commemorated on Delaware's state quarter and in countless schools as the embodiment of individual sacrifice for collective self-determination"
        ],
        "relationships": [
            {"entity": "Declaration of Independence (July 2–4, 1776)", "relationship": "SIGNER_WHOSE_MIDNIGHT_RIDE_ENABLED_DELAWARE_VOTE_FOR", "note": "Rode 80 miles overnight through illness and storm to break Delaware's tie vote — arriving in time to give Delaware a 2-1 majority for independence and sign the Declaration"},
            {"entity": "Delaware delegation tie vote (July 2, 1776)", "relationship": "TIE-BREAKING_VOTE_IN", "note": "His vote broke the 1-1 tie between Thomas McKean (for) and George Read (against) — his midnight ride making Delaware's unanimous founding contribution possible"},
            {"entity": "President of Delaware (1778–1781)", "relationship": "PRESIDENT_DURING_REVOLUTIONARY_WAR_AS", "note": "Served as Delaware's President (governor) during the most critical years of the Revolutionary War — maintaining the state's institutional continuity and Continental Army support"},
            {"entity": "Delaware state quarter (commemorative legacy)", "relationship": "COMMEMORATED_ON", "note": "His midnight ride is depicted on Delaware's state quarter — one of the founding era's most enduring symbols of individual sacrifice for collective independence"},
            {"entity": "Continental Congress (Delaware, 1774–1778)", "relationship": "CONTINENTAL_CONGRESSMAN_FROM_DELAWARE", "note": "Served as Continental Congressman from Delaware (1774–1776, 1777–1778) — representing the colony and then state at its most critical constitutional moments"}
        ]
    }),

    # 2 — Robert Barnwell Rhett
    ("robert-barnwell-rhett", {
        "summary": (
            "Robert Barnwell Rhett (1800–1876) was a South Carolina "
            "fire-eater politician, US Representative (1837–1849), "
            "US Senator (1850–1852), and Confederate Congressman — "
            "known as the 'Father of Secession' for his decades-long "
            "advocacy of Southern independence, which finally materialized "
            "in 1860–1861 after more than 30 years of his agitation. "
            "His political career was defined by a consuming conviction "
            "that the South's interests were irreconcilable with the "
            "Northern majority and that secession was not only desirable "
            "but historically inevitable.\n\n"
            "Rhett first called publicly for secession as early as the "
            "1830 tariff debates. He organized the 'Bluffton Movement' "
            "in South Carolina in 1844 — an attempt at nullification "
            "that failed — and was involved in every subsequent Southern "
            "rights crisis through the 1850s. When secession came in "
            "1860, he was deeply involved in drafting the Confederate "
            "Constitution and served in the Provisional Confederate "
            "Congress (1861–1862). His newspaper, the Charleston Mercury "
            "(operated with his son), was the primary journalistic "
            "voice of radical secessionism throughout the antebellum era.\n\n"
            "His deepest bitterness came after secession: he believed "
            "Jefferson Davis was too moderate, too bureaucratic, and "
            "too slow to pursue Confederate independence aggressively "
            "enough. The Mercury became one of Davis's harshest critics, "
            "and Rhett died in 1876 convinced that the Confederate "
            "failure was Davis's fault rather than secession's inherent "
            "contradictions.\n\n"
            "He embodied the fire-eater tragedy: he had worked 30 years "
            "for a cause that was won — and then catastrophically lost — "
            "within four years."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "'Father of Secession' — the fire-eater who called for Southern independence from the 1830s; SC congressman and senator; involved in drafting the Confederate Constitution; his Charleston Mercury was the primary voice of radical secessionism; bitterly criticized Jefferson Davis's management of the Confederacy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's fire-eater political culture — rooted in the Nullification Crisis (1832) and the state's extreme sensitivity to any federal limitation on slavery — created the political environment that sustained Rhett's decades of radical secessionism",
            "The Charleston Mercury — the Southern press organ he and his son operated — provided the institutional platform for translating his secessionist convictions into a 30-year media campaign that shaped elite South Carolina opinion",
            "Each successive sectional crisis — the Bluffton Movement (1844), the Compromise of 1850, Bleeding Kansas, and John Brown's raid — provided Rhett with fresh evidence for his core argument that Southern interests were incompatible with Northern majority rule"
        ],
        "effects": [
            "His 30 years of secessionist agitation — through the Charleston Mercury and his political career — contributed to the cultural and political normalization of secession as a legitimate option in South Carolina, making 1860's rapid secession psychologically prepared",
            "His involvement in drafting the Confederate Constitution contributed to the document's specific provisions — including explicit protections for slavery and states' rights that were more explicit than the US Constitution's comparable provisions",
            "His sustained criticism of Jefferson Davis — through the Mercury — contributed to the internal Confederate political fragmentation that hampered the Confederate war effort in the East",
            "His career illustrated the fire-eater political trajectory: how decades of intransigent advocacy for a revolutionary cause can eventually produce the revolution — and how the revolutionaries then often lose control of what they have created"
        ],
        "relationships": [
            {"entity": "Charleston Mercury (secessionist newspaper)", "relationship": "EDITOR_AND_OWNER_OF_PRIMARY_FIRE-EATER_ORGAN", "note": "Operated the Charleston Mercury — the primary journalistic voice of radical secessionism — with his son throughout the antebellum era and Civil War"},
            {"entity": "Confederate Constitution (1861 draft)", "relationship": "CO-DRAFTER_OF", "note": "Deeply involved in drafting the Confederate Constitution — contributing the explicit slavery protections and states' rights provisions that distinguished it from the US Constitution"},
            {"entity": "South Carolina secession (December 1860)", "relationship": "'FATHER_OF_SECESSION'_WHOSE_30_YEARS_OF_AGITATION_PREPARED", "note": "Known as the 'Father of Secession' — his 30 years of agitation from the 1830s to 1860 helped normalize and prepare South Carolina for its December 1860 secession"},
            {"entity": "Jefferson Davis (Confederate president, target of criticism)", "relationship": "HARSHEST_PRESS_CRITIC_OF", "note": "His Mercury was one of Jefferson Davis's most relentless critics — arguing Davis was too moderate and too slow, contributing to the internal Confederate political fragmentation"},
            {"entity": "US Congress from South Carolina (1837–1852)", "relationship": "REPRESENTATIVE_AND_SENATOR", "note": "Served as US Representative (1837–1849) and Senator (1850–1852) from South Carolina — the political platform from which he amplified his secessionist arguments before a national audience"}
        ]
    }),

    # 3 — Adolphe Crémieux
    ("adolphe-crémieux", {
        "summary": (
            "Adolphe Crémieux (Isaac Moïse Crémieux, 1796–1880) was a "
            "French Jewish lawyer, statesman, and civil rights advocate "
            "who twice served as France's Minister of Justice — under "
            "the Second Republic (1848) and the Government of National "
            "Defense (1870–1871) — and who was one of the most consequential "
            "figures in 19th-century Jewish civil rights history. Born "
            "in Nîmes to a Jewish family, he rose through the French "
            "bar to become one of its most celebrated advocates, was "
            "elected to the Chamber of Deputies in 1842, and spent his "
            "career at the intersection of French republicanism and "
            "Jewish emancipation.\n\n"
            "His most lasting single act was the Crémieux Decree of "
            "October 24, 1870 — issued during the Government of National "
            "Defense after Napoleon III's capture at Sedan — which granted "
            "French citizenship to the approximately 35,000 Jewish "
            "inhabitants of French Algeria. This decree was one of the "
            "most consequential extensions of citizenship rights in French "
            "colonial history — extending the principles of Revolutionary "
            "emancipation to a colonial Jewish community — and remained "
            "a point of fierce controversy for 70 years until it was "
            "revoked by the Vichy government in 1940 and restored "
            "after liberation.\n\n"
            "He also played a key role in the Damascus Blood Libel "
            "affair of 1840 — traveling to Alexandria with Moses "
            "Montefiore to negotiate the release of Jewish prisoners "
            "falsely accused of ritual murder — and was co-founder "
            "and long-serving president of the Alliance Israélite "
            "Universelle (1860–1880), the first international Jewish "
            "civil rights organization.\n\n"
            "His life spanned the French Revolution's emancipation "
            "promises to their colonial extension under the Third Republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Jewish statesman; twice Minister of Justice (1848, 1870–71); issued the Crémieux Decree (1870) granting French citizenship to Algerian Jews — revoked by Vichy (1940), restored after liberation; co-founder and president of the Alliance Israélite Universelle; key figure in the Damascus Blood Libel (1840) rescue mission.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Republican tradition's commitment to universal citizenship — rooted in the Revolution's 1791 emancipation of French Jews — provided the ideological foundation for Crémieux's career as both a Jewish advocate and a French republican statesman",
            "The Government of National Defense's extraordinary circumstances — Napoleon III captured at Sedan, French territory under Prussian invasion — created the political moment when Crémieux could issue the Algerian Jewish citizenship decree without facing the full weight of colonialist opposition",
            "The Alliance Israélite Universelle's establishment in 1860 — and Crémieux's leadership of it — provided the institutional framework for coordinated Jewish civil rights advocacy across the French colonial world and beyond"
        ],
        "effects": [
            "The Crémieux Decree (1870) granted French citizenship to Algeria's 35,000 Jewish inhabitants — a citizenship that was revoked by the Vichy government in 1940, restored after liberation, and remained a touchstone of French colonial citizenship law for a century",
            "His role in the Damascus Blood Libel affair (1840) — helping secure the release of falsely accused Jewish prisoners — was an early demonstration that international Jewish civil rights advocacy could succeed when organized and diplomatically engaged",
            "The Alliance Israélite Universelle (1860) — which he co-founded and led — became the first international Jewish civil rights organization and a model for subsequent transnational Jewish advocacy institutions",
            "His career demonstrated that Jewish politicians could reach the highest levels of French republican government — both symbolizing and actively advancing the project of Jewish integration into French civic life that the Revolution had promised in 1791"
        ],
        "relationships": [
            {"entity": "Crémieux Decree (October 24, 1870)", "relationship": "ISSUER_OF", "note": "Issued the Crémieux Decree granting French citizenship to Algeria's 35,000 Jewish inhabitants — revoked by Vichy (1940), restored after liberation"},
            {"entity": "Alliance Israélite Universelle (1860–1880)", "relationship": "CO-FOUNDER_AND_PRESIDENT", "note": "Co-founded and served as long-time president of the Alliance Israélite Universelle — the first international Jewish civil rights organization"},
            {"entity": "Damascus Blood Libel (1840) — prisoner rescue", "relationship": "KEY_NEGOTIATOR_FOR_RELEASE_OF_PRISONERS_IN", "note": "Traveled to Alexandria with Moses Montefiore to negotiate the release of Jewish prisoners falsely accused in the Damascus Blood Libel affair of 1840"},
            {"entity": "French Ministry of Justice (1848 and 1870–71)", "relationship": "MINISTER_OF_JUSTICE_TWICE", "note": "Served twice as France's Minister of Justice — under the Second Republic (1848) and the Government of National Defense (1870–71)"},
            {"entity": "French Jewish emancipation / Algerian Jewish citizenship", "relationship": "MOST_CONSEQUENTIAL_ADVOCATE_AND_LEGISLATOR_OF", "note": "The most consequential advocate for extending French Revolutionary emancipation principles to colonial Jewish communities — his decree was the primary instrument of that extension"}
        ]
    }),

    # 4 — William Jackson
    ("william-jackson", {
        "summary": (
            "William Jackson (1759–1828) was a British-born American "
            "military officer, political secretary, and diplomat — "
            "best known as the secretary of the 1787 Constitutional "
            "Convention, whose signature appears on the United States "
            "Constitution as the convention's official recorder rather "
            "than as a delegate. Born in England and raised in South "
            "Carolina after his parents' early deaths, Jackson served "
            "as an aide-de-camp during the Revolutionary War, became "
            "secretary of the Constitutional Convention through George "
            "Washington's sponsorship, and kept the official journal "
            "of the convention's proceedings.\n\n"
            "His responsibilities at the Constitutional Convention were "
            "procedural and archival: he recorded votes, managed delegate "
            "correspondence, and was entrusted with the confidential "
            "convention records that were not published until 1818. "
            "His journal was less complete than Madison's private notes — "
            "leaving gaps that historians have grappled with — but he "
            "preserved the essential procedural record of the convention "
            "and authenticated the document by signing it as secretary.\n\n"
            "After the convention, Jackson served as aide-de-camp to "
            "President Washington (1789–1791), as secretary to John Adams "
            "on diplomatic missions, and briefly as editor of the "
            "Federalist newspaper United States Gazette in Philadelphia. "
            "In 1795 he married Elizabeth Willing — daughter of Thomas "
            "Willing, the prominent Philadelphia banker and co-founder "
            "of the Bank of North America — connecting him to "
            "Philadelphia's most influential financial family.\n\n"
            "His unique constitutional position — the only non-delegate "
            "to sign the Constitution — makes him a minor but "
            "irreplaceable figure in the founding record."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Secretary of the 1787 Constitutional Convention; the only non-delegate to sign the US Constitution (as official secretary/recorder); aide-de-camp to President Washington (1789–1791); married into the Willing banking family of Philadelphia; kept the official convention journal.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Washington's personal trust and patronage — rooted in their relationship during the Revolutionary War — created the sponsorship that secured Jackson the constitutional convention secretaryship and later the presidential aide-de-camp position",
            "The Constitutional Convention's need for a trusted secretary who could maintain strict confidentiality about proceedings that were conducted under a secrecy oath — a role that Jackson's military discretion and Washington's recommendation made him suited for",
            "His Revolutionary War connections to the Philadelphia elite — developed through his aide-de-camp service — positioned him for the political and social networks that defined his post-war career"
        ],
        "effects": [
            "His official convention journal — though incomplete relative to Madison's private notes — provided the foundational procedural record of the Constitutional Convention, preserving the essential documentary evidence of how the Constitution was drafted",
            "His signature on the Constitution as secretary authenticated the document's physical integrity and attested to the convention's official proceedings — making him the only non-delegate whose name appears on the founding document",
            "His marriage to Elizabeth Willing (1795) connected him to the Willing financial dynasty — integrating the convention secretary into Philadelphia's commercial elite through the same family networks that Hamilton had engaged in his Treasury program",
            "His service as presidential aide-de-camp (1789–1791) contributed to the administrative development of the early presidency — one of the first instances of an executive personal staff supporting presidential operations"
        ],
        "relationships": [
            {"entity": "US Constitution (1787) / Constitutional Convention", "relationship": "SECRETARY_AND_SOLE_NON-DELEGATE_SIGNER_OF", "note": "Served as secretary of the Constitutional Convention — the only non-delegate to sign the Constitution, attesting to the document's authenticity as official recorder"},
            {"entity": "George Washington (Convention sponsor, President employer)", "relationship": "AIDE-DE-CAMP_AND_CONVENTION_SECRETARY_APPOINTED_BY", "note": "Washington's personal sponsorship secured him the convention secretaryship; he later served as aide-de-camp to Washington as president (1789–1791)"},
            {"entity": "Constitutional Convention official journal (1787, published 1818)", "relationship": "KEEPER_OF", "note": "Kept the official convention journal — less complete than Madison's private notes but preserved as the foundational procedural record, not published until 1818"},
            {"entity": "Thomas Willing family / Philadelphia banking elite", "relationship": "SON-IN-LAW_THROUGH_MARRIAGE_INTO", "note": "Married Elizabeth Willing (1795) — daughter of Thomas Willing, Philadelphia banker and Bank of North America co-founder — connecting him to Philadelphia's financial elite"},
            {"entity": "United States Gazette (Philadelphia Federalist newspaper)", "relationship": "EDITOR", "note": "Briefly edited the United States Gazette — Philadelphia's Federalist newspaper — in his post-aide-de-camp years"}
        ]
    }),

    # 5 — Samuel McRoberts
    ("samuel-mcroberts", {
        "summary": (
            "Samuel McRoberts (1799–1843) was an Illinois Democratic "
            "lawyer and politician who served as a US Senator from "
            "Illinois from March 1843 until his death on March 27, 1843 — "
            "one of the shortest Senate careers in American history, "
            "measured in days rather than months. Born in Monroe County, "
            "Illinois, he was educated by private tutors and attended "
            "the law department of Transylvania University in Lexington, "
            "Kentucky — the frontier gateway to legal training for "
            "ambitious young men of the Mississippi Valley in the 1820s.\n\n"
            "After admission to the bar in 1821, McRoberts practiced "
            "in Monroe County and served in various county and judicial "
            "positions in Illinois — including as a US circuit court "
            "commissioner — before his election to the US Senate by "
            "the Illinois legislature in 1843. He died within days "
            "of taking his seat, leaving no meaningful Senate record.\n\n"
            "His significance lies in what he represented: the rapid "
            "institutional development of frontier Illinois in the "
            "1820s–1840s, when the state's Democratic political machinery "
            "was producing a generation of lawyers and politicians — "
            "including Abraham Lincoln, Stephen Douglas, and Lyman Trumbull "
            "— who would define the antebellum crisis. McRoberts did "
            "not survive to participate in that history.\n\n"
            "His brief Senate career and early death at 43 rendered him "
            "a footnote in Illinois's rich antebellum political history — "
            "a reminder that many careers of potential significance were "
            "cut off by the frontier's characteristic early mortality."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Illinois Democratic senator (March 1843, died within days of taking office — one of the shortest Senate careers in US history); Transylvania University law graduate; part of the frontier Illinois Democratic political generation that preceded Lincoln and Douglas.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Illinois's rapidly developing frontier Democratic political machinery — building the state party infrastructure that supported Polk and Jackson — created the organizational context in which McRoberts's legal career and judicial experience translated into Senate election",
            "Transylvania University's law department in Lexington, Kentucky — the premier frontier legal training institution for the Mississippi Valley in the 1820s — provided the credentials that distinguished him within Monroe County's legal community",
            "Illinois's early statehood political culture (1818 statehood) — with its rapid institutional development and competitive Democratic-Whig rivalry — created the electoral environment in which an experienced circuit court lawyer could rise to Senate election by the state legislature"
        ],
        "effects": [
            "His death within days of taking his Senate seat left Illinois's Senate delegation incomplete at a moment of significant antebellum political development — creating the vacancy that allowed the Illinois Democratic Party to place a different voice in the Senate",
            "His legal career in Monroe County contributed to the development of Illinois's frontier bar — one of the networks from which Lincoln's generation of Illinois lawyers emerged in the 1830s–1840s",
            "His Senate election by the Illinois legislature illustrated the competitive Democratic Party machinery developing in the Old Northwest — the same machinery that would manage the Lincoln-Douglas debates and the 1858 Senate contest 15 years later",
            "His early death at 43 embodied the characteristic vulnerability of frontier careers — the life expectancy gap between the professional aspirations of frontier politicians and the mortality realities of the antebellum Midwest"
        ],
        "relationships": [
            {"entity": "US Senate from Illinois (March 1843, died in office)", "relationship": "SENATOR_WHO_DIED_WITHIN_DAYS_OF_TAKING_OFFICE", "note": "Elected to the US Senate by the Illinois legislature — died March 27, 1843, within days of taking his seat, one of the shortest Senate careers in American history"},
            {"entity": "Transylvania University law department (Lexington, KY)", "relationship": "GRADUATE", "note": "Attended Transylvania University's law department — the premier frontier legal training institution for the Mississippi Valley in the 1820s"},
            {"entity": "Illinois Democratic Party machinery (1840s)", "relationship": "PRODUCT_OF_FRONTIER", "note": "Part of the Illinois Democratic political machinery developing in the 1830s–1840s — the same organizational context that would produce the Lincoln-Douglas generation"},
            {"entity": "Monroe County, Illinois (legal practice and career base)", "relationship": "ESTABLISHED_LEGAL_CAREER_IN", "note": "Built his legal and judicial career in Monroe County — admitted to the bar in 1821, served as US circuit court commissioner before Senate election"},
            {"entity": "Illinois frontier bar (1820s–1840s)", "relationship": "MEMBER_OF_FORMATIVE_GENERATION_OF", "note": "Part of the frontier Illinois bar's formative generation — the legal community from which Lincoln, Douglas, and Trumbull emerged in the antebellum era"}
        ]
    }),

    # 6 — William H. Cabell
    ("william-h-cabell", {
        "summary": (
            "William H. Cabell (1772–1853) was a Virginia Democratic-Republican "
            "politician and judge who served as Governor of Virginia (1805–1808) "
            "and then as a judge on the Virginia Supreme Court of Appeals "
            "(1808–1850) — an extraordinary 42-year tenure on Virginia's "
            "highest court that made him one of the most significant "
            "contributors to the development of Virginia's antebellum "
            "legal jurisprudence. Educated at the College of William "
            "and Mary, he served in the Virginia House of Delegates before "
            "his election to the governorship by the legislature.\n\n"
            "His three-year governorship (1805–1808) was competent if "
            "unremarkable — managing Virginia's affairs during Jefferson's "
            "presidency and the escalating maritime tensions with Britain "
            "that would eventually produce the War of 1812. He administered "
            "the state during a period of relative stability, maintaining "
            "Virginia's Democratic-Republican political dominance and "
            "its plantation economic culture.\n\n"
            "His 42-year tenure on the Virginia Supreme Court of Appeals "
            "(1808–1850) was his primary historical contribution — "
            "providing judicial continuity from the early republic through "
            "the Jacksonian era to the antebellum crisis. He served "
            "alongside some of Virginia's most distinguished jurists and "
            "contributed to the development of Virginia's common law "
            "through hundreds of opinions across more than four decades.\n\n"
            "A minor eccentricity: his middle initial 'H.' — adopted "
            "in 1795 to distinguish him from other William Cabells "
            "in Virginia's prominent Cabell family — stood for no actual "
            "name, a reminder of Virginia's complex family-name culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Governor (1805–1808); Virginia Supreme Court of Appeals judge (1808–1850, 42 years) — one of the longest judicial tenures in Virginia history; Democratic-Republican; College of William and Mary graduate; the 'H.' in his name stood for no actual name.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's College of William and Mary tradition — the training ground for Virginia's colonial and early republican legal and political elite — provided Cabell with the educational credentials and social networks that established his professional career",
            "Virginia's Democratic-Republican political culture — which dominated the state's legislature and governance from the 1790s through the Jacksonian era — created the political environment that elevated Cabell to the governorship and then the judiciary",
            "The Virginia Supreme Court of Appeals's institutional continuity — serving Virginia's legal system as its highest judicial authority for over a century — created the stable environment in which a 42-year tenure was structurally possible"
        ],
        "effects": [
            "His 42-year tenure on the Virginia Supreme Court of Appeals (1808–1850) contributed to the development of Virginia's antebellum common law — providing judicial continuity through the most transformative decades in American legal history",
            "His governorship (1805–1808) maintained Virginia's Democratic-Republican political dominance during Jefferson's presidency — contributing to the state's institutional stability during a period of escalating external tensions",
            "His career exemplified the Virginia planter-lawyer-politician career trajectory — from legislature to executive to judiciary — that characterized the Jeffersonian generation's approach to public service as lifelong institutional stewardship",
            "His name convention — adopting a middle initial that stood for nothing — illustrated the practical family-management strategies of Virginia's complex aristocratic naming culture, in which multiple prominent family members required distinguishing markers"
        ],
        "relationships": [
            {"entity": "Virginia governorship (1805–1808)", "relationship": "GOVERNOR", "note": "Served as Governor of Virginia (1805–1808) — managing the state during Jefferson's presidency and the escalating maritime tensions preceding the War of 1812"},
            {"entity": "Virginia Supreme Court of Appeals (1808–1850, 42 years)", "relationship": "JUDGE_FOR_42_YEARS_ON", "note": "Served on the Virginia Supreme Court of Appeals for 42 years (1808–1850) — one of the longest judicial tenures in Virginia history, contributing to antebellum legal jurisprudence"},
            {"entity": "College of William and Mary (Virginia legal-political elite)", "relationship": "GRADUATE_AND_PRODUCT_OF", "note": "Educated at the College of William and Mary — the training ground for Virginia's colonial and early republican elite that shaped his career trajectory"},
            {"entity": "Virginia Democratic-Republican Party (1800s–1820s)", "relationship": "ALIGNED_POLITICIAN_AND_GOVERNOR_OF", "note": "Virginia Democratic-Republican politician who served in the House of Delegates before his gubernatorial election — embodying the party's dominance of Virginia governance"},
            {"entity": "Cabell family (Virginia political dynasty)", "relationship": "PROMINENT_MEMBER_OF", "note": "Member of Virginia's prominent Cabell family — adopting the middle initial 'H.' (which stood for no actual name) in 1795 to distinguish himself from other William Cabells"}
        ]
    }),

    # 7 — Oliver H. Prince
    ("oliver-h-prince", {
        "summary": (
            "Oliver Hillhouse Prince (1787–1837) was a Connecticut-born "
            "Georgia lawyer, journalist, and legal scholar who compiled "
            "the first comprehensive digest of Georgia law, served "
            "briefly as a US Senator from Georgia (1828–1829, appointed), "
            "and contributed to the development of Georgia's frontier "
            "legal culture during the state's formative antebellum decades. "
            "Born in Connecticut to a family with New England roots, "
            "he migrated to Georgia as a child with his parents, "
            "grew up in the state, and built a legal and journalistic "
            "career serving Georgia's rapidly developing frontier society.\n\n"
            "His most lasting contribution was his 'Digest of the Laws "
            "of the State of Georgia' — a systematic compilation and "
            "organization of Georgia's statutes that served as the "
            "foundational reference for Georgia legal practice during "
            "the antebellum period. In an era before comprehensive legal "
            "publishing, such digests were essential tools for frontier "
            "lawyers and judges navigating the accumulated legislation "
            "of a rapidly developing state.\n\n"
            "His appointment to the US Senate in 1828 — filling the "
            "vacancy created by the resignation of John Forsyth — "
            "gave him a brief congressional presence, though he served "
            "only until 1829 and left no significant legislative record. "
            "His prior service in the Georgia state senate and his "
            "work as a journalist — editing Georgia newspapers — "
            "had established him as a recognized figure in Georgia's "
            "professional community.\n\n"
            "He died in 1837 at 50, leaving a legacy more in legal "
            "scholarship than political achievement."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut-born Georgia lawyer who compiled the first comprehensive 'Digest of the Laws of the State of Georgia' — a foundational reference for antebellum Georgia legal practice; briefly US Senator (1828–1829, appointed); Georgia state senator; journalist and newspaper editor.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's frontier legal culture — rapidly developing in the 1820s–1830s as the state expanded westward into Creek and Cherokee territories — created the acute need for systematic legal compilation that Prince's Digest addressed",
            "His Connecticut New England education and legal training — combined with Georgia's frontier professional culture — gave him the scholarly inclinations and organizational skills that distinguished him from typical frontier practitioners",
            "John Forsyth's Senate resignation (1828) — to accept appointment as Secretary of State — created the vacancy that the Georgia legislature chose to fill with Prince's appointment"
        ],
        "effects": [
            "His 'Digest of the Laws of the State of Georgia' became the foundational reference for Georgia legal practice — enabling the systematic navigation of Georgia's accumulated legislation by frontier lawyers and judges who could not otherwise access the state's legal record",
            "His brief Senate appointment (1828–1829) was part of Georgia's turbulent 1820s Senate representation — the era of Crawford vs. Adams vs. Jackson factional politics — and contributed to Georgia's representation during the tariff debates",
            "His journalistic career contributed to the development of Georgia's frontier press — one of the institutional pillars of antebellum Southern society that formed opinion and mediated political communication",
            "His career illustrated the New England migrant contribution to Southern frontier professionalism — the pattern of New England-trained lawyers and scholars who built the legal and intellectual infrastructure of the antebellum South"
        ],
        "relationships": [
            {"entity": "'Digest of the Laws of the State of Georgia'", "relationship": "COMPILER_AND_AUTHOR_OF", "note": "Compiled the first comprehensive digest of Georgia law — the foundational reference for antebellum Georgia legal practice"},
            {"entity": "US Senate from Georgia (1828–1829, appointed)", "relationship": "SENATOR", "note": "Appointed to the US Senate (1828–1829) to fill the vacancy created by John Forsyth's resignation — served briefly without significant legislative record"},
            {"entity": "Georgia frontier legal culture (1820s–1830s)", "relationship": "LEGAL_SCHOLAR_WHO_SYSTEMATIZED", "note": "His Digest of Georgia law systematized the state's accumulated legislation — an essential tool for frontier lawyers navigating Georgia's rapidly developing legal environment"},
            {"entity": "Georgia state senate / Georgia journalism (antebellum)", "relationship": "STATE_SENATOR_AND_NEWSPAPER_EDITOR_IN", "note": "Served in the Georgia state senate and edited Georgia newspapers — building the institutional presence that led to his Senate appointment"},
            {"entity": "Connecticut-to-Georgia migration (New England frontier contribution)", "relationship": "MIGRANT_WHO_BUILT_LEGAL_INFRASTRUCTURE_IN", "note": "Connecticut-born migrant who brought New England legal training to Georgia's frontier — part of the pattern of New England professionals building Southern frontier institutions"}
        ]
    }),

    # 8 — Thomas B. Robertson
    ("thomas-b-robertson", {
        "summary": (
            "Thomas Bolling Robertson (1779–1828) was a Virginia-born "
            "Louisiana politician who served across nearly every level "
            "of Louisiana's governmental architecture in its transition "
            "from French colonial possession to American territory to "
            "statehood: Attorney General and Secretary of Orleans Territory "
            "(1807–1811), US Representative from Louisiana (1812–1818), "
            "3rd Governor of Louisiana (1820–1824), and US District "
            "Court judge for Louisiana's eastern district — tracing the "
            "full arc of Louisiana's founding political generation.\n\n"
            "Robertson came from Virginia — the state that sent more "
            "lawyers and planters to the Old Southwest than any other — "
            "and arrived in Louisiana when it was still Orleans Territory, "
            "building his career through the territorial period before "
            "Louisiana achieved statehood in 1812. His congressional "
            "service (1812–1818) placed him in Washington during the "
            "War of 1812 and the post-war era, representing one of "
            "America's newest and most distinctive states.\n\n"
            "His governorship (1820–1824) was marked by the tensions "
            "characteristic of Louisiana's complex social landscape: "
            "the uneasy coexistence of Anglo-American settlers, "
            "Creole French population, free people of color, "
            "and the enslaved workforce of the expanding plantation "
            "economy. His administration managed Louisiana's participation "
            "in the Missouri Compromise era's sectional politics "
            "while governing one of the most ethnically heterogeneous "
            "states in the union.\n\n"
            "He died in 1828 at 49 — cut off before what might have "
            "been a more prominent national career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia-born Louisiana politician who held nearly every major office in Louisiana's founding era: Orleans Territory AG and Secretary, US Representative (1812–1818), 3rd Governor of Louisiana (1820–1824), US District Court judge; part of Louisiana's Virginia-origin founding political generation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's tradition of exporting its surplus professional class to the frontier territories of the Old Southwest — lawyers, planters, and merchants seeking new opportunities in the newly acquired Louisiana Territory — brought Robertson to New Orleans at the height of territorial development",
            "Louisiana's unique administrative needs as a former French and Spanish colonial possession — requiring English-speaking lawyers who could navigate the Territory's civil law heritage and Anglo-American common law future — created the professional demand that Robertson's territorial career addressed",
            "The War of 1812's political dynamics — and Louisiana's particular strategic importance as the gateway to the Mississippi Valley — shaped the congressional career of the state's newly elected first representatives"
        ],
        "effects": [
            "His governorship (1820–1824) managed Louisiana's participation in the Missouri Compromise era's sectional politics — governing one of the most ethnically complex states in the union during the period when slavery's expansion became the defining national issue",
            "His career traced the full arc of Louisiana's institutional development from territorial governance to statehood — his multiple offices contributing to the administrative foundations of Louisiana's early state governance",
            "His judicial appointment as US District Court judge after his governorship contributed to the development of Louisiana's federal judicial architecture — the institution that would manage the intersection of civil law tradition and common law federal jurisdiction",
            "His Virginia-origin career trajectory illustrated the founding-generation pattern of southwestern state-building by Virginia migrant professionals — the human capital transfer that shaped the governance of the Old Southwest"
        ],
        "relationships": [
            {"entity": "Louisiana governorship (3rd Governor, 1820–1824)", "relationship": "3RD_GOVERNOR", "note": "Served as 3rd Governor of Louisiana (1820–1824) — governing one of America's most ethnically complex states during the Missouri Compromise era's sectional politics"},
            {"entity": "Orleans Territory / Louisiana territorial administration (1807–1811)", "relationship": "ATTORNEY_GENERAL_AND_SECRETARY", "note": "Served as Attorney General and Secretary of Orleans Territory (1807–1811) — navigating the Territory's French civil law heritage and Anglo-American administrative future"},
            {"entity": "US Congress from Louisiana (1812–1818)", "relationship": "REPRESENTATIVE", "note": "Served as US Representative from Louisiana (1812–1818) — representing one of America's newest states in Congress during the War of 1812 and post-war era"},
            {"entity": "US District Court for Eastern District of Louisiana", "relationship": "JUDGE", "note": "Served as US District Court judge for Louisiana's eastern district — contributing to the federal judicial architecture managing Louisiana's unique civil-law/common-law intersection"},
            {"entity": "Virginia-to-Louisiana migration (Old Southwest frontier)", "relationship": "PROFESSIONAL_MIGRANT_WHO_BUILT_LOUISIANA_INSTITUTIONS", "note": "Virginia-born migrant who built Louisiana's territorial and state institutions — part of the pattern of Virginia professionals founding the governance of the Old Southwest"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 37)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
