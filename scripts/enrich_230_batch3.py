#!/usr/bin/env python3
"""
Batch 3 enrichment for 230-Class-230 entities.
Enriches 8 landmark modern American jurists and legal figures.
Follows git-first bot rules: writes _unsyncedEdits=True + _editLog diffs.
"""

import json
import os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "thurgood-marshall": {
        "summary": (
            "Thurgood Marshall (1908–1993) was an American civil rights lawyer and jurist who "
            "became the first African American justice of the United States Supreme Court "
            "(1967–1991) and one of the most consequential legal advocates of the 20th century. "
            "Born in Baltimore to a steward father who taught him to argue by example, Marshall "
            "attended Howard University School of Law, where he was galvanized by the injustice "
            "of racially segregated legal education and resolved to dismantle Jim Crow through "
            "the courts.\n\n"
            "As director-counsel of the NAACP Legal Defense and Educational Fund, Marshall argued "
            "32 cases before the Supreme Court and won 29. His greatest achievement was "
            "Brown v. Board of Education (1954), in which the Court unanimously declared racially "
            "segregated public schools unconstitutional — overturning the 58-year-old Plessy v. "
            "Ferguson doctrine of 'separate but equal.' The case stands as arguably the most "
            "transformative judicial decision in American history. Marshall also argued Shelley v. "
            "Kraemer (1948, racially restrictive covenants) and Smith v. Allwright (1944, white "
            "primaries) among numerous landmark civil rights victories. He served as US Solicitor "
            "General (1965–1967) before President Lyndon Johnson appointed him to the Court.\n\n"
            "On the Supreme Court, Marshall became the consistent liberal conscience of the "
            "bench, writing passionate dissents on capital punishment, criminal procedure, and "
            "the rights of the poor. His judicial philosophy held that the Constitution's "
            "promise of equal protection demanded active judicial enforcement against "
            "discrimination. 'In recognizing the humanity of our fellow beings,' he wrote, "
            "'we pay ourselves the highest tribute.' He retired in 1991 and died two years later, "
            "having transformed American law and society through six decades of advocacy."
        ),
        "causes": [
            {
                "title": "The 'separate but equal' doctrine of Plessy v. Ferguson (1896) enshrined racial segregation in American law, creating the injustice Marshall devoted his career to dismantling",
                "type": "EventWindow",
                "year": "1896, United States"
            },
            {
                "title": "Howard University Law School under Charles Hamilton Houston trained a generation of civil rights lawyers with a mission to use the courts as a tool of racial justice",
                "type": "Institution",
                "year": "1930–1933, Washington DC"
            },
            {
                "title": "The NAACP Legal Defense Fund's strategic litigation campaign systematically challenged segregation in education, voting, and housing",
                "type": "Movement",
                "year": "1940–1961, United States"
            }
        ],
        "effects": [
            {
                "title": "Brown v. Board of Education (1954) overturned 'separate but equal', mandating school desegregation and catalyzing the modern civil rights movement",
                "type": "EventWindow",
                "year": "1954, United States"
            },
            {
                "title": "Marshall's Supreme Court appointment made him the first African American justice, permanently integrating the nation's highest court",
                "type": "Institution",
                "year": "1967, Washington DC"
            },
            {
                "title": "His litigation record — 29 SCOTUS wins in 32 cases — established the template for strategic constitutional litigation as a tool of social change",
                "type": "Idea",
                "year": "1940–1961, United States"
            },
            {
                "title": "Marshall's dissents on capital punishment shaped the later debate over the death penalty's constitutionality under the Eighth Amendment",
                "type": "Idea",
                "year": "1967–1991, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "WON",
                "targetSlug": "brown-v-board-of-education",
                "targetName": "Brown v. Board of Education",
                "context": "Marshall argued and won Brown v. Board (1954), the landmark SCOTUS ruling that declared school segregation unconstitutional"
            },
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "LED",
                "targetSlug": "naacp-legal-defense-fund",
                "targetName": "NAACP Legal Defense Fund",
                "context": "Marshall served as director-counsel of the NAACP LDF, directing its strategic litigation campaign against Jim Crow"
            },
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "APPOINTED_BY",
                "targetSlug": "lyndon-b-johnson",
                "targetName": "Lyndon B. Johnson",
                "context": "President Johnson appointed Marshall to the Supreme Court in 1967, making him the first African American justice"
            },
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "OVERTURNED",
                "targetSlug": "plessy-v-ferguson",
                "targetName": "Plessy v. Ferguson",
                "context": "Brown v. Board, argued by Marshall, directly overturned Plessy's 'separate but equal' doctrine"
            },
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "MENTORED_BY",
                "targetSlug": "charles-hamilton-houston",
                "targetName": "Charles Hamilton Houston",
                "context": "Houston trained Marshall at Howard Law and instilled the philosophy of the 'social engineer' lawyer who uses courts to achieve social justice"
            },
            {
                "sourceSlug": "thurgood-marshall",
                "sourceName": "Thurgood Marshall",
                "verb": "OPPOSED",
                "targetSlug": "capital-punishment",
                "targetName": "Capital Punishment",
                "context": "Marshall maintained in every death penalty case before the Court that capital punishment violated the Eighth Amendment's prohibition of cruel and unusual punishment"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Thurgood Marshall's victory in Brown v. Board of Education dismantled the legal foundations of American racial segregation and catalyzed the civil rights movement, while his appointment as the first Black Supreme Court Justice permanently transformed the composition and self-understanding of America's highest court.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "ruth-bader-ginsburg": {
        "summary": (
            "Ruth Bader Ginsburg (1933–2020) was an American lawyer, jurist, and cultural icon "
            "who served as an associate justice of the United States Supreme Court from 1993 "
            "until her death, and who spent the preceding two decades as the nation's leading "
            "legal advocate for gender equality. Born Joan Ruth Bader in Brooklyn to Jewish "
            "immigrant parents, she graduated first in her class from Columbia Law School in "
            "1959 but found law firms unwilling to hire a woman, an experience that shaped "
            "her lifelong commitment to anti-discrimination law.\n\n"
            "In the 1970s, Ginsburg became the ACLU Women's Rights Project director and "
            "argued six landmark cases before the Supreme Court, winning five. She deliberately "
            "chose plaintiffs strategically — often men disadvantaged by gender stereotypes "
            "— to broaden the Court's understanding of sex discrimination. In Reed v. Reed "
            "(1971) and Frontiero v. Richardson (1973) she established that the Equal "
            "Protection Clause applied to sex-based discrimination. Appointed to the DC "
            "Circuit in 1980 and to the Supreme Court in 1993 by President Clinton, she "
            "became the second woman to serve on the nation's highest court. Her majority "
            "opinion in United States v. Virginia (1996) struck down the Virginia Military "
            "Institute's male-only admissions policy in a sweeping declaration of equal "
            "constitutional protection for women.\n\n"
            "In her later years, Ginsburg became 'Notorious RBG' — a cultural phenomenon "
            "embodied in her lace collar, workout regimen, and searing dissents. Her dissents "
            "in Ledbetter v. Goodyear (2007, which provoked the Lilly Ledbetter Fair Pay Act) "
            "and Shelby County v. Holder (2013, on voting rights) shaped public debate. "
            "Her death six weeks before the 2020 presidential election triggered a "
            "constitutional clash over her replacement that reshaped the Court's ideological "
            "balance for a generation."
        ),
        "causes": [
            {
                "title": "Sex-based employment discrimination — law firms refusing to hire women law graduates in the 1950s–60s — drove Ginsburg toward gender equality advocacy",
                "type": "Idea",
                "year": "1959–1963, United States"
            },
            {
                "title": "The second-wave feminist movement of the 1960s–70s created political and cultural demand for constitutional gender equality litigation",
                "type": "Movement",
                "year": "1960–1975, United States"
            },
            {
                "title": "The ACLU Women's Rights Project provided the institutional framework for Ginsburg's strategic Supreme Court litigation campaign",
                "type": "Institution",
                "year": "1972–1980, United States"
            }
        ],
        "effects": [
            {
                "title": "Reed v. Reed (1971) and Frontiero v. Richardson (1973) established that the Equal Protection Clause applies to sex-based discrimination",
                "type": "EventWindow",
                "year": "1971–1973, United States"
            },
            {
                "title": "United States v. Virginia (1996) struck down VMI's male-only admissions policy in a landmark ruling on gender equality in public education",
                "type": "EventWindow",
                "year": "1996, United States"
            },
            {
                "title": "Her Ledbetter dissent inspired the Lilly Ledbetter Fair Pay Act (2009), the first bill signed by President Obama",
                "type": "EventWindow",
                "year": "2009, United States"
            },
            {
                "title": "Her death in 2020 triggered the Senate's confirmation of Amy Coney Barrett, reshaping the Supreme Court's ideological balance",
                "type": "EventWindow",
                "year": "2020, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "ruth-bader-ginsburg",
                "sourceName": "Ruth Bader Ginsburg",
                "verb": "WON",
                "targetSlug": "reed-v-reed",
                "targetName": "Reed v. Reed",
                "context": "Ginsburg argued Reed v. Reed (1971), the first SCOTUS ruling striking down a law that discriminated based on sex"
            },
            {
                "sourceSlug": "ruth-bader-ginsburg",
                "sourceName": "Ruth Bader Ginsburg",
                "verb": "LED",
                "targetSlug": "aclu-womens-rights-project",
                "targetName": "ACLU Women's Rights Project",
                "context": "Ginsburg directed the ACLU Women's Rights Project in the 1970s, strategically litigating gender equality at the Supreme Court"
            },
            {
                "sourceSlug": "ruth-bader-ginsburg",
                "sourceName": "Ruth Bader Ginsburg",
                "verb": "APPOINTED_BY",
                "targetSlug": "bill-clinton",
                "targetName": "Bill Clinton",
                "context": "President Clinton appointed Ginsburg to the Supreme Court in 1993; she was the second woman to serve as a justice"
            },
            {
                "sourceSlug": "ruth-bader-ginsburg",
                "sourceName": "Ruth Bader Ginsburg",
                "verb": "AUTHORED",
                "targetSlug": "united-states-v-virginia-1996",
                "targetName": "United States v. Virginia (1996)",
                "context": "Ginsburg wrote the 7-1 majority opinion ordering VMI to admit women, a landmark in gender equality jurisprudence"
            },
            {
                "sourceSlug": "ruth-bader-ginsburg",
                "sourceName": "Ruth Bader Ginsburg",
                "verb": "CHAMPIONED",
                "targetSlug": "gender-equality-law",
                "targetName": "Gender Equality Law",
                "context": "Ginsburg's decades-long advocacy through litigation and adjudication fundamentally transformed American law on sex discrimination"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Ruth Bader Ginsburg's two-decade litigation campaign before the Supreme Court established the constitutional framework for sex-discrimination law, and her 27 years on the Court produced landmark rulings on gender equality that transformed the legal status of women in American life.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "kamala-harris": {
        "summary": (
            "Kamala Devi Harris (born 1964) is an American politician, attorney, and the 49th "
            "Vice President of the United States (2021–2025), becoming the first woman, first "
            "African American, and first person of South Asian descent to hold that office. "
            "Born in Oakland, California to an Indian-born mother (a cancer researcher) and "
            "a Jamaican-born father (an economist), Harris graduated from UC Hastings College "
            "of the Law and built her legal career in the San Francisco Bay Area.\n\n"
            "Harris served as District Attorney of San Francisco (2004–2011) and as Attorney "
            "General of California (2011–2017) — the first woman and the first Black person "
            "to hold both offices. As Attorney General she won a landmark $25 billion "
            "settlement from major banks for mortgage fraud following the 2008 financial "
            "crisis, and declined to defend California's Proposition 8 banning same-sex "
            "marriage. Elected to the US Senate in 2016, she gained national recognition "
            "through sharp questioning during Senate hearings. Joe Biden selected her as "
            "his running mate in August 2020; their ticket won the November election and "
            "she was inaugurated as vice president on January 20, 2021. As VP she played "
            "key roles in domestic policy, became the first woman to exercise presidential "
            "authority (when Biden underwent anesthesia), and secured the 2024 Democratic "
            "presidential nomination after Biden withdrew — losing the general election to "
            "Donald Trump.\n\n"
            "Harris's career represents a series of historic 'firsts' across American "
            "prosecutorial, law enforcement, legislative, and executive institutions, "
            "reflecting both the opportunities opened by the civil rights movement and "
            "the continuing evolution of American political representation in the 21st century."
        ),
        "causes": [
            {
                "title": "The civil rights movement and subsequent political reforms opened pathways for African American and South Asian Americans to reach the highest offices",
                "type": "Movement",
                "year": "1960s–2020s, United States"
            },
            {
                "title": "California's diverse electorate and progressive political culture created the conditions for Harris's successive electoral breakthroughs",
                "type": "Institution",
                "year": "2004–2016, California"
            },
            {
                "title": "Biden's decision to select a woman of color as running mate reflected the Democratic Party's commitment to diverse representation at the highest levels",
                "type": "EventWindow",
                "year": "2020, United States"
            }
        ],
        "effects": [
            {
                "title": "As Vice President, Harris became the first woman, first Black American, and first South Asian American in the executive succession line, permanently altering the precedent for American leadership",
                "type": "Institution",
                "year": "2021, United States"
            },
            {
                "title": "Her $25 billion mortgage settlement as California AG set a national precedent for state-level enforcement of federal banking law",
                "type": "EventWindow",
                "year": "2012, California"
            },
            {
                "title": "Harris's 2024 presidential campaign — the first by a woman of color to receive a major party nomination — continued the expansion of American presidential politics",
                "type": "EventWindow",
                "year": "2024, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "kamala-harris",
                "sourceName": "Kamala Harris",
                "verb": "SERVED_UNDER",
                "targetSlug": "joe-biden",
                "targetName": "Joe Biden",
                "context": "Harris served as Biden's Vice President from January 2021 to January 2025"
            },
            {
                "sourceSlug": "kamala-harris",
                "sourceName": "Kamala Harris",
                "verb": "ADMINISTERED",
                "targetSlug": "office-of-the-vice-president",
                "targetName": "Office of the Vice President of the United States",
                "context": "Harris was the 49th Vice President, the first woman and person of color to hold the office"
            },
            {
                "sourceSlug": "kamala-harris",
                "sourceName": "Kamala Harris",
                "verb": "NEGOTIATED",
                "targetSlug": "national-mortgage-settlement-2012",
                "targetName": "National Mortgage Settlement (2012)",
                "context": "As California AG, Harris secured a $25 billion settlement from major banks over fraudulent mortgage practices"
            },
            {
                "sourceSlug": "kamala-harris",
                "sourceName": "Kamala Harris",
                "verb": "ELECTED_TO",
                "targetSlug": "united-states-senate",
                "targetName": "United States Senate",
                "context": "Harris was elected US Senator for California in 2016, becoming the first South Asian American and second Black woman elected to the Senate"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Kamala Harris's election as Vice President — the first woman, first Black American, and first South Asian American to hold the office — marked a historic milestone in American political representation and redrew the demographic possibilities of the nation's highest executive offices.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "sandra-day-oconnor": {
        "summary": (
            "Sandra Day O'Connor (1930–2023) was an American jurist who served as an associate "
            "justice of the United States Supreme Court from 1981 to 2006, the first woman "
            "ever to hold that position. Her appointment by President Ronald Reagan fulfilled "
            "a campaign promise and placed a moderate conservative at the center of the Court "
            "during one of its most consequential periods, when O'Connor's position as "
            "the pivotal swing vote shaped American jurisprudence across abortion, affirmative "
            "action, church-state relations, and election law.\n\n"
            "Born in El Paso, Texas and raised on an Arizona cattle ranch, O'Connor graduated "
            "third in her Stanford Law class (alongside William Rehnquist) in 1952, only to "
            "find that law firms would not hire women. She entered public service, eventually "
            "becoming an Arizona state senator and majority leader before joining the Arizona "
            "Court of Appeals. Reagan nominated her in 1981. On the Supreme Court, O'Connor "
            "became the decisive vote in landmark cases: in Planned Parenthood v. Casey (1992) "
            "she replaced Roe v. Wade's trimester framework with the 'undue burden' standard, "
            "preserving abortion rights while permitting broader restrictions. In Grutter v. "
            "Bollinger (2003) she upheld affirmative action in university admissions. In "
            "Bush v. Gore (2000) her vote was decisive in ending the Florida recount and "
            "resolving the presidential election.\n\n"
            "O'Connor's pragmatic, case-by-case jurisprudence reflected her deep skepticism "
            "of sweeping legal rules. She retired in 2006 to care for her husband, who had "
            "Alzheimer's disease. In retirement she campaigned for civics education and later "
            "disclosed her own Alzheimer's diagnosis in 2018. She died in December 2023 at 93, "
            "having defined a generation of American constitutional law through the power of "
            "a single, carefully considered vote."
        ),
        "causes": [
            {
                "title": "Reagan's 1980 campaign pledge to appoint the first woman to the Supreme Court provided the political impetus for O'Connor's nomination",
                "type": "Person",
                "year": "1981, United States"
            },
            {
                "title": "The growing number of women in state government and the judiciary created a pool of qualified female candidates from which O'Connor emerged",
                "type": "Institution",
                "year": "1960s–1981, United States"
            },
            {
                "title": "Sex discrimination in the legal profession — law firms refusing to hire women law graduates in the 1950s — pushed O'Connor toward public service",
                "type": "Idea",
                "year": "1952–1960, Arizona"
            }
        ],
        "effects": [
            {
                "title": "As the first female Supreme Court justice, O'Connor transformed the composition and public perception of the nation's highest court",
                "type": "Institution",
                "year": "1981, United States"
            },
            {
                "title": "Planned Parenthood v. Casey (1992) replaced Roe's trimester framework with the 'undue burden' standard, redefining abortion jurisprudence for three decades",
                "type": "EventWindow",
                "year": "1992, United States"
            },
            {
                "title": "Her decisive vote in Bush v. Gore (2000) ended the Florida recount and resolved the presidential election — one of the most consequential judicial decisions in modern political history",
                "type": "EventWindow",
                "year": "2000, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "sandra-day-oconnor",
                "sourceName": "Sandra Day O'Connor",
                "verb": "APPOINTED_BY",
                "targetSlug": "ronald-reagan",
                "targetName": "Ronald Reagan",
                "context": "Reagan nominated O'Connor as the first woman to the Supreme Court in 1981"
            },
            {
                "sourceSlug": "sandra-day-oconnor",
                "sourceName": "Sandra Day O'Connor",
                "verb": "AUTHORED",
                "targetSlug": "planned-parenthood-v-casey",
                "targetName": "Planned Parenthood v. Casey",
                "context": "O'Connor co-authored the plurality opinion in Casey (1992) replacing Roe's trimester framework with the 'undue burden' standard"
            },
            {
                "sourceSlug": "sandra-day-oconnor",
                "sourceName": "Sandra Day O'Connor",
                "verb": "DECIDED",
                "targetSlug": "bush-v-gore",
                "targetName": "Bush v. Gore",
                "context": "O'Connor's vote was decisive in the 5-4 Bush v. Gore (2000) ruling halting the Florida recount and deciding the presidential election"
            },
            {
                "sourceSlug": "sandra-day-oconnor",
                "sourceName": "Sandra Day O'Connor",
                "verb": "CHAMPIONED",
                "targetSlug": "civics-education",
                "targetName": "Civics Education",
                "context": "In retirement O'Connor founded iCivics, a nonprofit promoting civics education in American schools"
            },
            {
                "sourceSlug": "sandra-day-oconnor",
                "sourceName": "Sandra Day O'Connor",
                "verb": "SERVED_WITH",
                "targetSlug": "william-rehnquist",
                "targetName": "William Rehnquist",
                "context": "O'Connor and Rehnquist were Stanford Law classmates in 1952 and later colleagues on the Supreme Court"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Sandra Day O'Connor's appointment as the first female Supreme Court justice permanently changed the face of American justice, and her pivotal role as the Court's swing vote for 25 years gave her outsized influence over abortion rights, affirmative action, religious liberty, and the 2000 presidential election.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "louis-brandeis": {
        "summary": (
            "Louis Dembitz Brandeis (1856–1941) was an American lawyer and jurist who served "
            "as the first Jewish justice of the United States Supreme Court (1916–1939) and "
            "who made enduring contributions to American law through his pioneering advocacy "
            "for privacy rights, antitrust enforcement, and the use of social-scientific "
            "evidence in constitutional adjudication. Known as the 'People's Attorney' for "
            "his willingness to take on powerful corporate interests without fee, he was one "
            "of the most influential legal thinkers of the Progressive Era.\n\n"
            "Before his Court appointment, Brandeis made two landmark contributions to "
            "American law. In 1890, with Samuel Warren, he published 'The Right to Privacy' "
            "in the Harvard Law Review — arguably the most influential law review article "
            "in American legal history — articulating for the first time a legal right to "
            "be 'let alone' that would eventually underpin modern privacy doctrine. In 1908, "
            "in Muller v. Oregon, he submitted the famous 'Brandeis Brief' — a legal document "
            "incorporating 113 pages of sociological and medical evidence about the effects "
            "of overwork on women's health, revolutionizing constitutional advocacy by "
            "supplementing legal argument with empirical social science. On the Court, Brandeis "
            "consistently dissented against unchecked corporate power and authored influential "
            "opinions on free speech, Fourth Amendment searches, and states' rights as "
            "laboratories of democracy.\n\n"
            "Brandeis championed small-scale capitalism, cooperative enterprise, and distributed "
            "economic power against the 'curse of bigness' — concentrations of corporate "
            "power he believed threatened democracy itself. His free speech dissents in Whitney "
            "v. California (1927) articulated the 'marketplace of ideas' principle in terms "
            "that shaped First Amendment jurisprudence for generations. Brandeis University "
            "was founded in his honor in 1948, seven years after his death."
        ),
        "causes": [
            {
                "title": "The rapid concentration of corporate power in Gilded Age America — trusts, monopolies, railroad combines — drove Brandeis's antitrust advocacy",
                "type": "EventWindow",
                "year": "1880–1916, United States"
            },
            {
                "title": "The emergence of mass media and commercial photography in the 1880s prompted Brandeis and Warren's theorization of a legal right to privacy",
                "type": "Idea",
                "year": "1890, Boston"
            },
            {
                "title": "Woodrow Wilson's Progressive reform agenda created the political opening for Brandeis's controversial Court nomination as the first Jewish justice",
                "type": "Person",
                "year": "1916, United States"
            }
        ],
        "effects": [
            {
                "title": "'The Right to Privacy' (1890) established the theoretical foundation for American privacy law, ultimately underpinning Griswold v. Connecticut and Roe v. Wade",
                "type": "Text",
                "year": "1890–present, United States"
            },
            {
                "title": "The Brandeis Brief transformed constitutional advocacy by introducing social-scientific evidence into constitutional adjudication",
                "type": "Idea",
                "year": "1908–present, United States"
            },
            {
                "title": "His Whitney dissent articulated the 'marketplace of ideas' free speech principle that became the foundation of modern First Amendment doctrine",
                "type": "Idea",
                "year": "1927–present, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "louis-brandeis",
                "sourceName": "Louis Brandeis",
                "verb": "AUTHORED",
                "targetSlug": "the-right-to-privacy-1890",
                "targetName": "The Right to Privacy (1890)",
                "context": "Brandeis co-authored with Samuel Warren the 1890 Harvard Law Review article that created the legal concept of a right to privacy"
            },
            {
                "sourceSlug": "louis-brandeis",
                "sourceName": "Louis Brandeis",
                "verb": "SUBMITTED",
                "targetSlug": "brandeis-brief",
                "targetName": "Brandeis Brief (1908)",
                "context": "In Muller v. Oregon, Brandeis submitted a brief with 113 pages of sociological evidence, revolutionizing constitutional advocacy"
            },
            {
                "sourceSlug": "louis-brandeis",
                "sourceName": "Louis Brandeis",
                "verb": "APPOINTED_BY",
                "targetSlug": "woodrow-wilson",
                "targetName": "Woodrow Wilson",
                "context": "Wilson nominated Brandeis to the Supreme Court in 1916; his confirmation was bitterly contested and he became the first Jewish justice"
            },
            {
                "sourceSlug": "louis-brandeis",
                "sourceName": "Louis Brandeis",
                "verb": "CHAMPIONED",
                "targetSlug": "antitrust-law",
                "targetName": "Antitrust Law",
                "context": "Brandeis was a leading antitrust advocate before and on the Court, arguing that concentrated corporate power ('the curse of bigness') threatened democracy"
            },
            {
                "sourceSlug": "louis-brandeis",
                "sourceName": "Louis Brandeis",
                "verb": "INFLUENCED",
                "targetSlug": "modern-privacy-doctrine",
                "targetName": "Modern Privacy Doctrine",
                "context": "Brandeis's 1890 privacy article ultimately underpinned the privacy rights recognized in Griswold, Roe, and subsequent SCOTUS decisions"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Louis Brandeis's theorization of the right to privacy, revolutionary Brandeis Brief methodology, and First Amendment jurisprudence made him one of the most intellectually generative jurists in American legal history, with influences still shaping privacy, speech, and antitrust law today.",
            "significanceCategory": "continental"
        },
        "importanceScore": 9
    },

    "hugo-black": {
        "summary": (
            "Hugo Lafayette Black (1886–1971) was an American jurist who served as an associate "
            "justice of the United States Supreme Court from 1937 to 1971 and became one of "
            "the 20th century's most influential champions of civil liberties, particularly "
            "of an absolutist reading of the First Amendment. His 34-year tenure on the Court "
            "produced landmark opinions on free speech, the right to counsel, and the "
            "incorporation of the Bill of Rights against the states — opinions that "
            "fundamentally expanded American constitutional freedoms.\n\n"
            "Black's biography encompasses one of American history's most dramatic "
            "transformations. Born in rural Alabama, he joined the Ku Klux Klan in 1923 as "
            "a political necessity in Alabama Democratic politics — a membership he resigned "
            "two years later and publicly repudiated. President Franklin Roosevelt appointed "
            "him to the Court in 1937 to shore up New Deal legislation. On the bench, Black "
            "evolved into a fierce advocate for civil liberties whose judicial philosophy "
            "was grounded in the literal text of the Constitution. 'Congress shall make no "
            "law,' he argued, 'means no law' — an absolutist position on the First Amendment. "
            "His majority opinion in Gideon v. Wainwright (1963) guaranteed the right to "
            "counsel for all criminal defendants. He led the majority in Engel v. Vitale "
            "(1962) striking down state-sponsored prayer in public schools. And he dissented "
            "passionately in Korematsu v. United States (1944) — only to be overruled by "
            "history in 2018 when the Court formally repudiated that decision.\n\n"
            "Black's jurisprudence of 'incorporation' — applying Bill of Rights guarantees "
            "to state governments through the 14th Amendment — transformed American "
            "constitutional law, protecting citizens from state as well as federal "
            "infringement of their fundamental liberties."
        ),
        "causes": [
            {
                "title": "FDR's New Deal majority-building strategy led him to appoint a loyal Democratic senator whose fitness for the Court was soon vindicated",
                "type": "Person",
                "year": "1937, United States"
            },
            {
                "title": "The Supreme Court's failure to incorporate the Bill of Rights against state governments left vast gaps in constitutional protection that Black's incorporation doctrine filled",
                "type": "Idea",
                "year": "c. 1925–1940, United States"
            },
            {
                "title": "The Great Depression, New Deal, and threats to civil liberties from both left and right shaped Black's evolution from Alabama politician to constitutional absolutist",
                "type": "EventWindow",
                "year": "1930s–1950s, United States"
            }
        ],
        "effects": [
            {
                "title": "Gideon v. Wainwright (1963) guaranteed the right to counsel to all criminal defendants, regardless of ability to pay — a landmark expansion of due process",
                "type": "EventWindow",
                "year": "1963, United States"
            },
            {
                "title": "Engel v. Vitale (1962) struck down state-sponsored school prayer, establishing the modern Establishment Clause doctrine on religion in public education",
                "type": "EventWindow",
                "year": "1962, United States"
            },
            {
                "title": "Black's total incorporation doctrine — applying all Bill of Rights guarantees to the states via the 14th Amendment — reshaped the constitutional relationship between citizens and state governments",
                "type": "Idea",
                "year": "1940s–1971, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "hugo-black",
                "sourceName": "Hugo Black",
                "verb": "APPOINTED_BY",
                "targetSlug": "franklin-d-roosevelt",
                "targetName": "Franklin D. Roosevelt",
                "context": "FDR appointed Black to the Supreme Court in 1937 to build a New Deal-friendly majority"
            },
            {
                "sourceSlug": "hugo-black",
                "sourceName": "Hugo Black",
                "verb": "AUTHORED",
                "targetSlug": "gideon-v-wainwright",
                "targetName": "Gideon v. Wainwright",
                "context": "Black wrote the unanimous opinion in Gideon v. Wainwright (1963) guaranteeing the right to counsel in all criminal cases"
            },
            {
                "sourceSlug": "hugo-black",
                "sourceName": "Hugo Black",
                "verb": "CHAMPIONED",
                "targetSlug": "incorporation-doctrine",
                "targetName": "Incorporation Doctrine",
                "context": "Black consistently argued for total incorporation of the Bill of Rights against state governments via the 14th Amendment"
            },
            {
                "sourceSlug": "hugo-black",
                "sourceName": "Hugo Black",
                "verb": "CHAMPIONED",
                "targetSlug": "first-amendment-absolutism",
                "targetName": "First Amendment Absolutism",
                "context": "Black argued that 'no law' in the First Amendment means no law — an absolutist free speech position that shaped decades of constitutional debate"
            },
            {
                "sourceSlug": "hugo-black",
                "sourceName": "Hugo Black",
                "verb": "OPPOSED",
                "targetSlug": "felix-frankfurter",
                "targetName": "Felix Frankfurter",
                "context": "Black and Frankfurter engaged in a famous decades-long doctrinal dispute: Black's absolutism vs. Frankfurter's judicial restraint and balancing approach"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Hugo Black's 34-year Supreme Court tenure produced a string of landmark civil liberties decisions — on the right to counsel, school prayer, and First Amendment freedom — while his incorporation doctrine extended the Bill of Rights against state governments, permanently expanding the constitutional protection of American citizens.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "felix-frankfurter": {
        "summary": (
            "Felix Frankfurter (1882–1965) was an American jurist, scholar, and public intellectual "
            "who served as an associate justice of the United States Supreme Court from 1939 to "
            "1962. Born in Vienna and brought to New York at age 12, he graduated from Harvard "
            "Law School in 1906 and returned to join its faculty, becoming one of the most "
            "influential law professors in American history before his judicial appointment. "
            "He co-founded the American Civil Liberties Union in 1920 and the New Republic "
            "magazine, and he was a senior confidential adviser to President Franklin Roosevelt "
            "before his Supreme Court appointment.\n\n"
            "On the Court, Frankfurter became the principal champion of judicial restraint — "
            "the doctrine that courts should defer to legislative judgment in matters of "
            "social and economic policy rather than imposing their own constitutional readings. "
            "His philosophy placed him in sustained conflict with colleagues like Hugo Black "
            "who favored more expansive constitutional adjudication. Frankfurter's balancing "
            "approach to the First Amendment, his deference to the political branches, and "
            "his concept of 'ordered liberty' as the touchstone of due process shaped "
            "jurisprudence through the 1950s. His opinion in Minersville School District v. "
            "Gobitis (1940) — upholding mandatory flag salutes for Jehovah's Witnesses — was "
            "overturned three years later in West Virginia v. Barnette, becoming one of the "
            "Court's most notorious self-reversals.\n\n"
            "Frankfurter's influence was felt as much through his Harvard network — placing "
            "former students ('Frankfurter's Happy Hot Dogs') throughout the Roosevelt "
            "administration and judiciary — as through his judicial opinions. He suffered a "
            "stroke in 1962 and retired, having shaped American legal education and "
            "constitutional thought across five decades."
        ),
        "causes": [
            {
                "title": "Harvard Law School's tradition of empirical, sociological jurisprudence — embodied by Brandeis's law review scholarship — shaped Frankfurter's approach to constitutional adjudication",
                "type": "Institution",
                "year": "1906–1939, Harvard"
            },
            {
                "title": "FDR's need for a trusted constitutional authority on the Supreme Court after the 'Court-packing' crisis led to Frankfurter's appointment",
                "type": "Person",
                "year": "1939, United States"
            },
            {
                "title": "The European experience of activist courts overriding democratic legislatures reinforced Frankfurter's conviction that judicial restraint was essential to democracy",
                "type": "Idea",
                "year": "1920s–1939, Europe and United States"
            }
        ],
        "effects": [
            {
                "title": "Frankfurter's judicial restraint doctrine shaped a generation of constitutional jurisprudence and the debate between textualism/restraint and expansive constitutional interpretation",
                "type": "Idea",
                "year": "1939–1970s, United States"
            },
            {
                "title": "His Harvard network placed former students throughout the New Deal administration and federal judiciary, spreading his influence far beyond the Court",
                "type": "Institution",
                "year": "1930s–1950s, United States"
            },
            {
                "title": "Gobitis (1940) and its reversal in Barnette (1943) produced one of the Court's most important early rulings on religious freedom in public education",
                "type": "EventWindow",
                "year": "1940–1943, United States"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "felix-frankfurter",
                "sourceName": "Felix Frankfurter",
                "verb": "APPOINTED_BY",
                "targetSlug": "franklin-d-roosevelt",
                "targetName": "Franklin D. Roosevelt",
                "context": "FDR appointed Frankfurter to the Supreme Court in 1939 after years of informal constitutional advising"
            },
            {
                "sourceSlug": "felix-frankfurter",
                "sourceName": "Felix Frankfurter",
                "verb": "CHAMPIONED",
                "targetSlug": "judicial-restraint",
                "targetName": "Judicial Restraint",
                "context": "Frankfurter was the Court's most consistent advocate for deference to legislative judgment, opposing expansive constitutional interpretation"
            },
            {
                "sourceSlug": "felix-frankfurter",
                "sourceName": "Felix Frankfurter",
                "verb": "OPPOSED",
                "targetSlug": "hugo-black",
                "targetName": "Hugo Black",
                "context": "Frankfurter and Black engaged in a decades-long jurisprudential debate: Frankfurter's balancing approach vs. Black's absolutism"
            },
            {
                "sourceSlug": "felix-frankfurter",
                "sourceName": "Felix Frankfurter",
                "verb": "TAUGHT_AT",
                "targetSlug": "harvard-law-school",
                "targetName": "Harvard Law School",
                "context": "Frankfurter taught at Harvard Law from 1914 to 1939, making it a pipeline for judicial and administrative talent during the New Deal era"
            },
            {
                "sourceSlug": "felix-frankfurter",
                "sourceName": "Felix Frankfurter",
                "verb": "CO-FOUNDED",
                "targetSlug": "american-civil-liberties-union",
                "targetName": "American Civil Liberties Union",
                "context": "Frankfurter was a founding member of the ACLU in 1920, before his jurisprudence evolved toward restraint over liberal activism"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Felix Frankfurter's judicial restraint philosophy, Harvard Law network, and engagement in the great constitutional debates of the New Deal era shaped American jurisprudence for a generation, even as his reputation was complicated by prominent doctrinal defeats including Gobitis's reversal.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "clarence-darrow": {
        "summary": (
            "Clarence Seward Darrow (1857–1938) was the most celebrated criminal defense "
            "attorney in American history, whose career spanned from labor movement advocacy "
            "in the Gilded Age to landmark confrontations over evolution, capital punishment, "
            "and racial justice in the 1920s. Born in Kinsman, Ohio, and largely self-taught "
            "in the law, he became the indispensable defender of those the legal system was "
            "most likely to destroy: labor organizers, murderers on death row, Black defendants "
            "before racist juries, and thinkers prosecuted for their ideas.\n\n"
            "Darrow's most famous cases became cultural landmarks. In 1894 he defended Eugene "
            "V. Debs during the Pullman Strike. In 1924 he saved Nathan Leopold and Richard "
            "Loeb from the death penalty in the 'crime of the century' through a 12-hour "
            "summation that became one of the most eloquent speeches against capital punishment "
            "in American history. In 1925 he faced William Jennings Bryan at the Scopes "
            "'Monkey' Trial in Dayton, Tennessee, defending John Scopes's right to teach "
            "evolution — subjecting Bryan to a devastating cross-examination that exposed "
            "biblical literalism to national ridicule. In 1925–1926 he won acquittal for "
            "Ossian Sweet, a Black physician who had fired in self-defense when a white mob "
            "attacked his home in Detroit — a trial addressing racial violence and the right "
            "of self-defense.\n\n"
            "Darrow was deeply shaped by the philosophy of determinism — the belief that "
            "human behavior is the product of heredity and environment rather than free will "
            "— and he translated this into courtroom arguments against capital punishment that "
            "challenged the retributive foundations of American criminal justice. In over "
            "100 capital murder cases, he never lost a client to execution. His legacy "
            "encompasses both the heights and contradictions of American liberal advocacy."
        ),
        "causes": [
            {
                "title": "The brutal suppression of the American labor movement in the Gilded Age drove Darrow toward advocacy for workers and the powerless against corporate power",
                "type": "Movement",
                "year": "1880s–1900s, United States"
            },
            {
                "title": "The philosophy of determinism — that behavior is produced by environment rather than free will — formed Darrow's intellectual foundation against capital punishment",
                "type": "Idea",
                "year": "c. 1890–1938, United States"
            },
            {
                "title": "The cultural battles of the 1920s — the Scopes Trial, racial violence, and criminalized labor activism — created the landmark cases that defined Darrow's legacy",
                "type": "EventWindow",
                "year": "1920s, United States"
            }
        ],
        "effects": [
            {
                "title": "Darrow's Scopes Trial cross-examination of Bryan exposed fundamentalist biblical literalism to devastating public criticism, shaping the American debate over evolution and religion in public education",
                "type": "EventWindow",
                "year": "1925, Dayton, Tennessee"
            },
            {
                "title": "His Leopold-Loeb summation became a foundational text of the American argument against capital punishment, cited in death penalty debates for a century",
                "type": "Text",
                "year": "1924, Chicago"
            },
            {
                "title": "The Ossian Sweet defense addressed the right of Black Americans to defend their homes against white mob violence, contributing to civil rights advocacy",
                "type": "EventWindow",
                "year": "1925–1926, Detroit"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "clarence-darrow",
                "sourceName": "Clarence Darrow",
                "verb": "DEFENDED",
                "targetSlug": "john-scopes",
                "targetName": "John Scopes",
                "context": "Darrow defended Scopes at the 1925 'Monkey Trial' for teaching evolution, cross-examining William Jennings Bryan on biblical literalism"
            },
            {
                "sourceSlug": "clarence-darrow",
                "sourceName": "Clarence Darrow",
                "verb": "OPPOSED",
                "targetSlug": "william-jennings-bryan",
                "targetName": "William Jennings Bryan",
                "context": "Darrow's devastating cross-examination of Bryan at Scopes became one of the most famous legal confrontations in American history"
            },
            {
                "sourceSlug": "clarence-darrow",
                "sourceName": "Clarence Darrow",
                "verb": "CHAMPIONED",
                "targetSlug": "anti-capital-punishment",
                "targetName": "Anti-Capital Punishment",
                "context": "Darrow never lost a capital client to execution in over 100 cases, and his Leopold-Loeb summation remains a foundational abolitionist text"
            },
            {
                "sourceSlug": "clarence-darrow",
                "sourceName": "Clarence Darrow",
                "verb": "DEFENDED",
                "targetSlug": "eugene-v-debs",
                "targetName": "Eugene V. Debs",
                "context": "Darrow defended Debs in the 1894 Pullman Strike prosecution, establishing his reputation as America's foremost labor lawyer"
            },
            {
                "sourceSlug": "clarence-darrow",
                "sourceName": "Clarence Darrow",
                "verb": "CHAMPIONED",
                "targetSlug": "racial-justice",
                "targetName": "Racial Justice",
                "context": "Darrow won acquittal for Ossian Sweet, a Black physician who fired in self-defense against a white mob, in a landmark civil rights trial"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Clarence Darrow's landmark defenses in the Scopes Trial, Leopold-Loeb case, and Ossian Sweet trial defined the American tradition of criminal defense advocacy, advanced the cause of abolishing capital punishment, and placed evolution and racial justice at the center of national legal debate.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    }
}


# ---------------------------------------------------------------------------
# Apply enrichments to JSON files
# ---------------------------------------------------------------------------

def enrich_entity(slug: str, data: dict) -> None:
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (file not found): {fname}")
        return

    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    updated_fields = []

    if "summary" in data:
        old_val = entity.get("summary", "")
        entity["summary"] = data["summary"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "summary",
            "oldValue": old_val[:300],
            "newValue": data["summary"][:300]
        })
        updated_fields.append("summary")

    if "importanceScore" in data:
        old_val = entity.get("importanceScore")
        entity["importanceScore"] = data["importanceScore"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "importanceScore",
            "oldValue": str(old_val),
            "newValue": str(data["importanceScore"])
        })
        updated_fields.append("importanceScore")

    if "historicalSignificance" in data:
        old_val = entity.get("historicalSignificance")
        entity["historicalSignificance"] = data["historicalSignificance"]
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "historicalSignificance",
            "oldValue": json.dumps(old_val)[:200],
            "newValue": json.dumps(data["historicalSignificance"])[:200]
        })
        updated_fields.append("historicalSignificance")

    for field in ("causes", "effects", "relationships"):
        if field in data:
            old_val = det.get(field, [])
            det[field] = data[field]
            edit_log.append({
                "timestamp": NOW,
                "editorId": EDITOR_ID,
                "field": field,
                "oldValue": json.dumps(old_val)[:300],
                "newValue": json.dumps(data[field])[:300]
            })
            updated_fields.append(field)

    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)

    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    slen = len(entity.get("summary", ""))
    nc = len(det.get("causes", []))
    ne = len(det.get("effects", []))
    nr = len(det.get("relationships", []))
    print(f"  ✓ {entity['name']} — sum={slen}c c={nc} e={ne} r={nr} [{', '.join(updated_fields)}]")


if __name__ == "__main__":
    print(f"Enriching {len(ENRICHMENTS)} entities in 230-Class-230 (Batch 3)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone. Files with _unsyncedEdits=True will be picked up by the sync gateway watchdog.")
