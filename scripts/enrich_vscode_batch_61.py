#!/usr/bin/env python3
"""
VS Code Enrichment Batch 61 — 8 Historical Persons
Neil Armstrong, Tim Berners-Lee, Frederick Douglass, Theodore Roosevelt,
Nefertiti, Tutankhamun, Richard the Lionheart, Tamerlane

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-61-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-61-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Neil Armstrong ────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201neil-armstrong.json",
        "slug": "neil-armstrong",
        "era_correction": None,
        "data": {
            "summary": (
                "Neil Armstrong (1930–2012) was an American astronaut and the first human being to walk on the Moon, stepping onto the lunar surface on July 20, 1969 at 02:56 UTC during the Apollo 11 mission. His words — 'That's one small step for [a] man, one giant leap for mankind' — were heard by 600 million people worldwide, the largest television audience in history to that point, and represent one of the defining moments of 20th-century civilization.\n\n"
                "Armstrong flew 78 combat missions in the Korean War as a Navy pilot before becoming a NASA test pilot, logging over 1,100 hours in experimental aircraft including the X-15 rocket plane. He commanded Gemini 8 (1966), performing the first successful docking of two spacecraft in orbit. His selection as Apollo 11 commander was partly attributed to his reputation for calm under pressure — during the final descent, he manually overrode the guidance computer and landed with 25 seconds of fuel remaining.\n\n"
                "Armstrong spent 2 hours and 31 minutes on the lunar surface alongside Buzz Aldrin, collecting 47.5 pounds of samples and planting the American flag. After returning, he served as Deputy Associate Administrator for Aeronautics at NASA before leaving for academia, teaching aerospace engineering at the University of Cincinnati (1971–1979) and remaining publicly reticent about his historic role.\n\n"
                "The Apollo program that Armstrong led represented the culmination of 400,000 engineers, technicians, and scientists working across a decade — and remains the most ambitious peacetime technological achievement in history."
            ),
            "causes": [
                "Cold War space race between US and Soviet Union following Sputnik (1957)",
                "Kennedy's 1961 declaration 'We choose to go to the Moon' committing national resources",
                "Apollo program engineering — Saturn V rocket, LM design, AGC guidance computer",
                "Armstrong's combat experience and X-15 test piloting building exceptional skill",
            ],
            "effects": [
                "First Moon landing (July 20, 1969) — first human presence beyond Earth",
                "Apollo program producing 842 lbs of lunar samples advancing planetary science",
                "600 million viewers — largest TV audience to that date",
                "American technological prestige secured in Cold War competition",
                "Space program legacy inspiring a generation of scientists and engineers",
                "Unified humanity in a single moment of collective wonder",
                "Demonstrated possibility of human spaceflight beyond low Earth orbit",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Apollo 11", "targetSlug": "apollo-11", "note": "Commander — first Moon landing mission"},
                {"type": "INFLUENCES", "target": "Buzz Aldrin", "targetSlug": "buzz-aldrin", "note": "Lunar module pilot; joined Armstrong on the surface"},
                {"type": "INFLUENCES", "target": "Michael Collins", "targetSlug": "michael-collins", "note": "Command module pilot; orbited while others walked"},
                {"type": "INFLUENCES", "target": "NASA", "targetSlug": "nasa", "note": "Apollo program commander; later Deputy Administrator"},
                {"type": "INFLUENCES", "target": "Space Race", "targetSlug": "space-race", "note": "Apollo 11 ended the Moon race decisively"},
                {"type": "INFLUENCES", "target": "John F. Kennedy", "targetSlug": "john-f-kennedy", "note": "Kennedy's 1961 pledge — Armstrong delivered the fulfillment"},
                {"type": "INFLUENCES", "target": "Saturn V rocket", "targetSlug": "saturn-v", "note": "Carried Armstrong, Aldrin, Collins to the Moon"},
                {"type": "INFLUENCES", "target": "Cold War", "targetSlug": "cold-war", "note": "Apollo 11 was the definitive US victory in the space race"},
                {"type": "INFLUENCES", "target": "Soviet space program", "targetSlug": "soviet-space-program", "note": "The lunar race Armstrong won against Soviet cosmonauts"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "American astronaut and test pilot"},
                {"type": "INFLUENCES", "target": "Moon", "targetSlug": "moon", "note": "First human to set foot on another world"},
                {"type": "INFLUENCES", "target": "Korean War", "targetSlug": "korean-war", "note": "Flew 78 combat missions as Navy pilot"},
                {"type": "INFLUENCES", "target": "X-15 research aircraft", "targetSlug": "x-15", "note": "Test pilot in edge-of-space aircraft before NASA"},
                {"type": "INFLUENCES", "target": "Yuri Gagarin", "targetSlug": "yuri-gagarin", "note": "Soviet cosmonaut whose first spaceflight triggered Armstrong's race"},
                {"type": "INFLUENCES", "target": "Human spaceflight", "targetSlug": "human-spaceflight", "note": "Demonstrated humans could reach and return from another world"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Neil Armstrong became the first human being to walk on another world on July 20, 1969 — the culmination of humanity's oldest dream of reaching the Moon and the most technologically ambitious achievement of the 20th century, watched by 600 million people as it happened."
            },
            "quote": "'That's one small step for [a] man, one giant leap for mankind.' — Neil Armstrong, July 20, 1969",
            "places": ["Cape Canaveral, Florida (launch)", "Sea of Tranquility, Moon (landing)", "Wapakoneta, Ohio (birthplace)"],
            "subjectHeadings": "Neil Armstrong — Astronauts and Aviators — United States — Modern",
            "subjects": ["United States", "space exploration", "Moon landing", "Apollo program", "NASA", "Cold War", "aviation", "20th century", "science", "technology"],
            "frameworks": ["technological-change", "cold-war", "scientific-revolution"],
        }
    },

    # ── 2. Tim Berners-Lee ───────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201tim-berners-lee.json",
        "slug": "tim-berners-lee",
        "era_correction": None,
        "data": {
            "summary": (
                "Sir Tim Berners-Lee (born 1955) is a British computer scientist who invented the World Wide Web in 1989 while working at CERN in Geneva — creating the foundational protocols (HTTP, HTML, URL) that connected the world's computers into an open, globally accessible information system. His invention is arguably the single most transformative technology of the 20th century, reshaping commerce, democracy, science, culture, and human communication more radically than any invention since the printing press.\n\n"
                "Berners-Lee's insight was to combine hypertext (clickable links between documents) with the Internet's existing TCP/IP infrastructure, and to make the resulting system royalty-free and openly available to all. His proposal at CERN (1989), his NeXT computer running the first web server (December 25, 1990), and his decision not to patent the Web — instead dedicating it to humanity — were choices of extraordinary consequence. The Web's open architecture was the precondition for everything from Wikipedia and Google to e-commerce and social media.\n\n"
                "He founded the World Wide Web Consortium (W3C) at MIT in 1994 to govern web standards, ensuring the Web remained vendor-neutral and interoperable. In 2009 he founded the World Wide Web Foundation to promote universal web access as a human right. In recent years he has led initiatives to decentralize the web and restore user data sovereignty through his Solid project.\n\n"
                "'The Web as I envisaged it, we have not seen it yet,' he has said — advocating for a more open, decentralized Web that fulfills its democratic potential."
            ),
            "causes": [
                "CERN's need to manage distributed scientific knowledge among thousands of researchers",
                "Ted Nelson's hypertext concept (1965) providing theoretical foundation",
                "Internet's TCP/IP infrastructure (1983) providing the transport layer",
                "NeXT Computer platform enabling rapid prototype development",
            ],
            "effects": [
                "World Wide Web (1991) — open information system transforming human communication",
                "HTTP, HTML, and URL — foundational protocols of all web activity",
                "First website at CERN (info.cern.ch) operational 1991",
                "W3C (1994) — standards body governing web interoperability",
                "e-commerce, search engines, social media — enabled by Web's open architecture",
                "Wikipedia, Google, Amazon — all rest on Berners-Lee's free protocols",
                "World Wide Web Foundation promoting universal access as human right",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "World Wide Web", "targetSlug": "world-wide-web", "note": "Inventor of HTTP, HTML, URL — the Web's protocols"},
                {"type": "INFLUENCES", "target": "CERN", "targetSlug": "cern", "note": "Proposed and built the Web at CERN (1989–1991)"},
                {"type": "INFLUENCES", "target": "Internet", "targetSlug": "internet", "note": "Built the Web on top of existing Internet infrastructure"},
                {"type": "INFLUENCES", "target": "W3C", "targetSlug": "w3c", "note": "Founded World Wide Web Consortium (1994) for open standards"},
                {"type": "INFLUENCES", "target": "Google", "targetSlug": "google", "note": "Google's search engine built on Web's open protocols"},
                {"type": "INFLUENCES", "target": "Wikipedia", "targetSlug": "wikipedia", "note": "Open knowledge project enabled by Web's open architecture"},
                {"type": "INFLUENCES", "target": "Ted Nelson", "targetSlug": "ted-nelson", "note": "Invented hypertext concept Berners-Lee built upon"},
                {"type": "INFLUENCES", "target": "Vint Cerf", "targetSlug": "vint-cerf", "note": "TCP/IP inventor whose Internet the Web runs on"},
                {"type": "INFLUENCES", "target": "Digital Revolution", "targetSlug": "digital-revolution", "note": "Web is the defining technology of the Digital Revolution"},
                {"type": "OCCURS_IN", "target": "United Kingdom", "targetSlug": "united-kingdom", "note": "British scientist educated and born in London"},
                {"type": "OCCURS_IN", "target": "Switzerland", "targetSlug": "switzerland", "note": "Invented the Web at CERN, Geneva"},
                {"type": "INFLUENCES", "target": "e-commerce", "targetSlug": "e-commerce", "note": "Web's open architecture enabled Amazon, eBay, global trade"},
                {"type": "INFLUENCES", "target": "Social media", "targetSlug": "social-media", "note": "Facebook, Twitter — all built on Web's protocol stack"},
                {"type": "INFLUENCES", "target": "Solid (project)", "targetSlug": "solid-project", "note": "His current project to decentralize web data"},
                {"type": "INFLUENCES", "target": "Open source movement", "targetSlug": "open-source", "note": "His royalty-free decision established open Web principle"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Tim Berners-Lee invented the World Wide Web in 1989 and gave it to humanity for free — his open protocols (HTTP, HTML, URL) created the information infrastructure that transformed commerce, democracy, science, and human communication more radically than any technology since Gutenberg's press."
            },
            "quote": "'The Web as I envisaged it, we have not seen it yet. The future is still so much bigger than the past.' — Tim Berners-Lee",
            "places": ["CERN, Geneva, Switzerland (Web invented)", "London, England (birthplace)", "MIT, Cambridge, USA (W3C)"],
            "subjectHeadings": "Tim Berners-Lee — Computer Scientists and Inventors — United Kingdom — Contemporary",
            "subjects": ["United Kingdom", "internet", "World Wide Web", "computing", "information technology", "open source", "CERN", "digital revolution", "20th century", "technology"],
            "frameworks": ["technological-change", "information-age", "globalization"],
        }
    },

    # ── 3. Frederick Douglass ────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/205-Class-205/205frederick-douglass.json",
        "slug": "frederick-douglass",
        "era_correction": None,
        "data": {
            "summary": (
                "Frederick Douglass (c. 1818–1895) was an American abolitionist, orator, writer, and statesman who escaped slavery at age 20 and became the foremost African American intellectual and activist of the 19th century. His Narrative of the Life of Frederick Douglass (1845), written when he was 27, is one of the most powerful autobiographical works in American literature — a first-person refutation of the proslavery argument, demonstrating with searing clarity that enslaved people were fully human persons.\n\n"
                "Douglass's oratory was legendary. As a Black man who had been enslaved, his physical presence and devastating eloquence destroyed the claim that African Americans were intellectually inferior. His July 4, 1852 speech, 'What to the Slave is the Fourth of July?' — delivered in Rochester, New York — is considered among the greatest speeches in American history: 'This Fourth July is yours, not mine. You may rejoice, I must mourn.'\n\n"
                "He advised Presidents Lincoln and Grant, campaigned for the 13th, 14th, and 15th Amendments, founded the abolitionist newspaper The North Star, and late in life championed women's suffrage (he was the only man to attend the Seneca Falls Convention, 1848). Lincoln called him 'the most meritorious man in the United States.'\n\n"
                "Douglass demonstrated through his own life that the human capacity for self-education, oratory, and moral leadership could not be bound by chains — his life was the argument against slavery."
            ),
            "causes": [
                "American chattel slavery — the system he escaped and dedicated his life to destroying",
                "Self-education through the Columbian Orator and Bible — literacy became his liberation",
                "Escape from slavery in Baltimore (1838) providing freedom to speak",
                "William Lloyd Garrison's abolitionist movement providing platform and network",
            ],
            "effects": [
                "Narrative of the Life of Frederick Douglass (1845) — definitive abolitionist autobiography",
                "'What to the Slave is the Fourth of July?' (1852) — greatest anti-slavery oration",
                "The North Star newspaper (1847) — leading abolitionist publication",
                "Counsel to Lincoln on emancipation and Black soldiers",
                "Advocacy for 13th, 14th, 15th Amendments codifying Black civil rights",
                "Model of African American intellectual achievement refuting scientific racism",
                "Enduring symbol of resistance, education, and self-liberation",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Abraham Lincoln", "targetSlug": "abraham-lincoln", "note": "Met three times; Lincoln called him 'the most meritorious man'"},
                {"type": "INFLUENCES", "target": "William Lloyd Garrison", "targetSlug": "william-lloyd-garrison", "note": "Early abolitionist mentor; later broke with Garrison over tactics"},
                {"type": "INFLUENCES", "target": "Narrative of the Life (1845)", "targetSlug": "narrative-of-the-life-of-frederick-douglass", "note": "His autobiography refuting proslavery arguments"},
                {"type": "INFLUENCES", "target": "American Civil War", "targetSlug": "american-civil-war", "note": "Advised Lincoln on Black troops; pressed for emancipation"},
                {"type": "INFLUENCES", "target": "Abolitionist movement", "targetSlug": "abolitionism-us", "note": "America's foremost abolitionist speaker and writer"},
                {"type": "INFLUENCES", "target": "Seneca Falls Convention (1848)", "targetSlug": "seneca-falls-convention", "note": "Only man present; championed women's suffrage"},
                {"type": "INFLUENCES", "target": "13th Amendment", "targetSlug": "thirteenth-amendment", "note": "Abolishing slavery — outcome he campaigned for"},
                {"type": "INFLUENCES", "target": "The North Star (newspaper)", "targetSlug": "the-north-star-newspaper", "note": "Abolitionist newspaper founded 1847"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "Enslaved in Maryland; free in Massachusetts, New York"},
                {"type": "INFLUENCES", "target": "Harriet Tubman", "targetSlug": "harriet-tubman", "note": "Fellow freedom fighter; both former enslaved Marylanders"},
                {"type": "INFLUENCES", "target": "Harriet Beecher Stowe", "targetSlug": "harriet-beecher-stowe", "note": "Met and influenced Uncle Tom's Cabin author"},
                {"type": "INFLUENCES", "target": "Civil rights movement", "targetSlug": "civil-rights-movement-usa", "note": "Direct intellectual predecessor to 20th-century civil rights"},
                {"type": "INFLUENCES", "target": "Ulysses S. Grant", "targetSlug": "ulysses-s-grant", "note": "Advised Grant on Reconstruction and civil rights enforcement"},
                {"type": "INFLUENCES", "target": "Susan B. Anthony", "targetSlug": "susan-b-anthony", "note": "Alliance between abolitionism and women's suffrage"},
                {"type": "INFLUENCES", "target": "American slavery", "targetSlug": "american-slavery", "note": "Born into and escaped the institution he spent his life destroying"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Frederick Douglass escaped slavery to become America's foremost abolitionist, whose autobiography and oratory demolished the intellectual case for slavery, advised Lincoln during the Civil War, and established the template of African American intellectual leadership that extended directly to W.E.B. Du Bois and the civil rights movement."
            },
            "quote": "'If there is no struggle, there is no progress.' — Frederick Douglass",
            "places": ["Talbot County, Maryland (birthplace, enslaved)", "Baltimore, Maryland (enslaved)", "Rochester, New York (home base)", "Washington D.C. (later career)"],
            "subjectHeadings": "Frederick Douglass — Abolitionists and Civil Rights Leaders — United States — Modern",
            "subjects": ["United States", "abolitionism", "slavery", "civil rights", "American Civil War", "oratory", "autobiography", "19th century", "African American history", "journalism"],
            "frameworks": ["liberation-theology", "social-revolution", "human-rights"],
        }
    },

    # ── 4. Theodore Roosevelt ────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/205-Class-205/205theodore-roosevelt.json",
        "slug": "theodore-roosevelt",
        "era_correction": None,
        "data": {
            "summary": (
                "Theodore Roosevelt (1858–1919) was the 26th President of the United States (1901–1909), the youngest ever to hold that office, who transformed the American presidency into an activist institution and reshaped the US role in world affairs. A prolific author, explorer, naturalist, soldier, and politician, he embodied the Progressive Era's confidence that vigorous government action could tame the excesses of industrial capitalism and project American power globally.\n\n"
                "Roosevelt's domestic presidency — his 'Square Deal' — broke up 44 corporations and trusts (the Northern Securities Company, Standard Oil, etc.) using the Sherman Antitrust Act with a vigor no previous president had attempted, establishing the regulatory state that still governs American business. He created 150 national forests, 51 federal bird reserves, 5 national parks, and 18 national monuments — setting aside 230 million acres of public land as the foundation of the American conservation movement.\n\n"
                "In foreign policy, he built the Panama Canal, expanded the Monroe Doctrine into an explicit American right to intervene in Latin American affairs (the Roosevelt Corollary), and mediated the end of the Russo-Japanese War (1905) — winning the Nobel Peace Prize, the first American to receive it. He won the Medal of Honor for leading the Rough Riders charge up San Juan Hill in Cuba (1898).\n\n"
                "'Speak softly and carry a big stick' encapsulated his foreign policy; 'Do what you can, with what you have, where you are' his approach to life."
            ),
            "causes": [
                "McKinley's assassination (1901) making Roosevelt president at 42",
                "Gilded Age industrial trusts accumulating monopoly power requiring regulatory response",
                "Frontier experience and Spanish-American War forging his activist temperament",
                "Progressive Era reformist politics challenging laissez-faire capitalism",
            ],
            "effects": [
                "44 antitrust suits breaking up industrial monopolies (Square Deal)",
                "230 million acres of public land protected (national parks, forests, monuments)",
                "Panama Canal construction completed — US engineering triumph",
                "Roosevelt Corollary to Monroe Doctrine — US as hemispheric policeman",
                "Nobel Peace Prize (1906) for mediating Russo-Japanese War",
                "FDA and Pure Food and Drug Act (1906) establishing food safety regulation",
                "Great White Fleet world tour demonstrating US naval power",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "William Howard Taft", "targetSlug": "william-howard-taft", "note": "Successor whom Roosevelt split from over progressive policy"},
                {"type": "INFLUENCES", "target": "Woodrow Wilson", "targetSlug": "woodrow-wilson", "note": "Wilson won 1912 because Roosevelt split Republican vote"},
                {"type": "INFLUENCES", "target": "Panama Canal", "targetSlug": "panama-canal", "note": "Engineered the political and physical construction of the canal"},
                {"type": "INFLUENCES", "target": "US conservation movement", "targetSlug": "conservation-movement-us", "note": "Set aside 230 million acres — founder of American conservation"},
                {"type": "INFLUENCES", "target": "John Muir", "targetSlug": "john-muir", "note": "Camped with Muir in Yosemite (1903); shared conservation vision"},
                {"type": "INFLUENCES", "target": "Russo-Japanese War", "targetSlug": "russo-japanese-war", "note": "Mediated peace at Portsmouth (1905); Nobel Prize result"},
                {"type": "INFLUENCES", "target": "Spanish-American War", "targetSlug": "spanish-american-war", "note": "Led Rough Riders at San Juan Hill (1898); Medal of Honor"},
                {"type": "INFLUENCES", "target": "Square Deal", "targetSlug": "square-deal", "note": "Domestic program: trust-busting, labor rights, consumer protection"},
                {"type": "INFLUENCES", "target": "Pure Food and Drug Act (1906)", "targetSlug": "pure-food-and-drug-act", "note": "Established federal food safety regulation"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "26th President of the United States"},
                {"type": "INFLUENCES", "target": "Progressive Era", "targetSlug": "progressive-era", "note": "Defining figure of Progressive political movement"},
                {"type": "INFLUENCES", "target": "William McKinley", "targetSlug": "william-mckinley", "note": "Predecessor; McKinley's assassination elevated Roosevelt"},
                {"type": "INFLUENCES", "target": "Bull Moose Party", "targetSlug": "progressive-party-1912", "note": "Founded after break with Taft; split Republican vote"},
                {"type": "INFLUENCES", "target": "Alfred Mahan", "targetSlug": "alfred-mahan", "note": "Sea power theorist who influenced Roosevelt's naval strategy"},
                {"type": "INFLUENCES", "target": "Franklin D. Roosevelt", "targetSlug": "franklin-d-roosevelt", "note": "Cousin; FDR modeled his activist presidency on TR"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Theodore Roosevelt transformed the US presidency into an activist institution, created the regulatory state and modern conservation movement, built the Panama Canal, and established American global power projection — defining American politics for the 20th century."
            },
            "quote": "'Speak softly and carry a big stick; you will go far.' — Theodore Roosevelt",
            "places": ["Washington D.C. (White House)", "New York City (birthplace)", "Oyster Bay, New York (home)", "Cuba (San Juan Hill)"],
            "subjectHeadings": "Theodore Roosevelt — Presidents and Statesmen — United States — Modern",
            "subjects": ["United States", "presidency", "progressive era", "conservation", "trust-busting", "Panama Canal", "foreign policy", "Nobel Peace Prize", "20th century", "imperialism"],
            "frameworks": ["state-formation", "empire-building", "environmental-history"],
        }
    },

    # ── 5. Nefertiti ─────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221nefertiti.json",
        "slug": "nefertiti",
        "era_correction": None,
        "data": {
            "summary": (
                "Nefertiti (c. 1370–1330 BCE) was the Great Royal Wife of Pharaoh Akhenaten and one of the most powerful women in ancient Egyptian history, who co-ruled during the Amarna Period — the remarkable religious revolution that replaced Egypt's polytheistic pantheon with exclusive worship of the sun disc Aten. Her painted limestone bust (c. 1345 BCE), discovered in 1912 in Thutmose's workshop at Amarna and now in Berlin's Neues Museum, is among the most recognized artworks in the world and has made her face synonymous with ancient beauty and feminine power.\n\n"
                "Alongside Akhenaten, Nefertiti appears in unprecedented numbers in Amarna art — driving a chariot, smiting enemies, performing priestly roles previously restricted to the pharaoh — roles that suggest she held extraordinary political and religious authority. Some Egyptologists argue she eventually ruled as pharaoh in her own right under the name Neferneferuaten, based on analysis of royal cartouches from the period, though this remains debated.\n\n"
                "The Amarna Period she helped shape was one of ancient history's most dramatic experiments: a monotheistic (or henotheistic) revolution closing established temple cults, moving the capital to Akhetaten (modern Amarna), transforming art, language, and religion. After Akhenaten's death it was rapidly reversed, with his name and Nefertiti's systematically erased from monuments — an ancient 'damnatio memoriae.'\n\n"
                "Her disappearance from records around Year 12 of Akhenaten's reign and the location of her tomb remain mysteries that continue to animate Egyptological debate."
            ),
            "causes": [
                "Akhenaten's religious revolution replacing Egyptian polytheism with Aten worship",
                "Egyptian royal tradition of powerful Great Royal Wives with religious roles",
                "Amarna art's break from convention allowing new representations of royal women",
                "Akhenaten's health or incapacity possibly necessitating Nefertiti's expanded role",
            ],
            "effects": [
                "Co-rule of Amarna Period's monotheistic revolution (c. 1353–1336 BCE)",
                "Nefertiti Bust (c. 1345 BCE) — most famous ancient portrait and beauty icon",
                "Possible reign as pharaoh Neferneferuaten after Akhenaten",
                "Symbol of female power in ancient Egypt for modern audiences",
                "Amarna art tradition — new naturalistic style breaking Egyptian conventions",
                "Ongoing diplomatic controversy between Egypt and Germany over bust's return",
                "Inspired Egyptological debates on Amarna succession and female pharaohs",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Akhenaten", "targetSlug": "akhenaten", "note": "Husband and pharaoh; co-led Amarna religious revolution"},
                {"type": "INFLUENCES", "target": "Amarna Period", "targetSlug": "amarna-period", "note": "Central figure of the monotheistic Aten revolution"},
                {"type": "INFLUENCES", "target": "Tutankhamun", "targetSlug": "tutankhamun", "note": "Possibly his stepmother or mother (still debated)"},
                {"type": "INFLUENCES", "target": "Neferneferuaten", "targetSlug": "neferneferuaten", "note": "She may have ruled as pharaoh under this name"},
                {"type": "INFLUENCES", "target": "Aten (deity)", "targetSlug": "aten", "note": "Chief priest of Aten cult alongside Akhenaten"},
                {"type": "INFLUENCES", "target": "Amarna art", "targetSlug": "amarna-art", "note": "New naturalistic style depicting royals in intimate scenes"},
                {"type": "INFLUENCES", "target": "Thutmose (sculptor)", "targetSlug": "thutmose-sculptor", "note": "Her bust carved in his workshop at Amarna"},
                {"type": "OCCURS_IN", "target": "Egypt", "targetSlug": "egypt", "note": "Queen of Egypt during Amarna Period"},
                {"type": "INFLUENCES", "target": "Akhetaten (Amarna)", "targetSlug": "amarna", "note": "New capital built for Aten worship"},
                {"type": "INFLUENCES", "target": "Neues Museum, Berlin", "targetSlug": "neues-museum-berlin", "note": "Her bust's current home; subject of repatriation demands"},
                {"type": "INFLUENCES", "target": "18th Dynasty Egypt", "targetSlug": "eighteenth-dynasty-egypt", "note": "Ruled at peak of Egypt's most glorious dynasty"},
                {"type": "INFLUENCES", "target": "Tiye", "targetSlug": "tiye", "note": "Akhenaten's mother; powerful queen before Nefertiti"},
                {"type": "INFLUENCES", "target": "Female pharaohs", "targetSlug": "female-pharaohs", "note": "Possible pharaoh herself — part of tradition with Hatshepsut"},
                {"type": "INFLUENCES", "target": "Hatshepsut", "targetSlug": "hatshepsut", "note": "Earlier female pharaoh tradition she may have continued"},
                {"type": "INFLUENCES", "target": "Ancient Egyptian religion", "targetSlug": "ancient-egyptian-religion", "note": "Her reign disrupted and then restored polytheistic tradition"},
            ],
            "historicalSignificance": {
                "significanceScore": 8,
                "significanceCategory": "continental",
                "significanceNarrative": "Nefertiti co-ruled Egypt's most dramatic religious revolution, may have governed as pharaoh in her own right, and left a painted bust so perfect it became the most recognized face of ancient civilization — an enduring symbol of female power, beauty, and the enigma of the Amarna Period."
            },
            "quote": "'The beautiful one has come.' — meaning of the name Nefertiti (ancient Egyptian)",
            "places": ["Akhetaten (Amarna), Egypt", "Thebes (Luxor), Egypt", "Memphis, Egypt"],
            "subjectHeadings": "Nefertiti — Queens and Rulers — Egypt — Classical",
            "subjects": ["Egypt", "ancient Egypt", "Amarna Period", "New Kingdom", "Aten", "monotheism", "female rulers", "Classical era", "archaeology", "Egyptology"],
            "frameworks": ["religious-thought", "state-formation", "feminist-history"],
        }
    },

    # ── 6. Tutankhamun ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221tutankhamun.json",
        "slug": "tutankhamun",
        "era_correction": None,
        "data": {
            "summary": (
                "Tutankhamun (c. 1341–1323 BCE) was an Egyptian pharaoh of the 18th Dynasty who reigned from approximately age 9 to his death at 18 or 19, making him a historically minor king during his lifetime — yet the most famous pharaoh in the world today, entirely because of the spectacular discovery of his intact tomb (KV62) by Howard Carter in November 1922. The tomb contained over 5,000 objects including his golden death mask (now in the Cairo Museum), golden throne, ritual chariots, and extensive ritual equipment — the greatest archaeological discovery of the 20th century.\n\n"
                "Tutankhamun's historical significance during his reign was the reversal of the Amarna revolution: he restored the traditional polytheistic cults closed by his predecessor Akhenaten, moved the capital back to Thebes, and restored the Amun priesthood to power — actions almost certainly directed by his advisors (the general Horemheb and the official Ay) given his extreme youth. He changed his name from Tutankhaten ('Living image of Aten') to Tutankhamun ('Living image of Amun').\n\n"
                "His cause of death — investigated through CT scanning of his mummy — revealed a complex picture of malaria, bone disease from congenital defects, and a leg fracture, dispelling sensational 'curse' stories. The 'Curse of the Pharaohs' legend arose from the deaths of several people connected to the tomb opening, though none died unusually fast by statistical standards.\n\n"
                "Tutankhamun's global fame is entirely posthumous — the intact condition of KV62, the visual splendor of its contents, and Carter's meticulous documentation made this the world's most celebrated archaeological find."
            ),
            "causes": [
                "Akhenaten's Amarna religious revolution creating need for restoration under a young king",
                "18th Dynasty's wealth and power enabling magnificent royal burial assemblage",
                "Tomb's dry sealed conditions preserving contents uniquely across 3,300 years",
                "Howard Carter's systematic search funded by Lord Carnarvon discovering KV62 (1922)",
            ],
            "effects": [
                "Howard Carter's discovery of KV62 (1922) — greatest archaeological find of 20th century",
                "5,000+ objects including golden death mask in Cairo Museum",
                "Reversal of Amarna revolution — restoration of Amun cult and polytheism",
                "'Tutmania' — global obsession with ancient Egypt sparked by 1922 discovery",
                "Traveling exhibition 'Tutankhamun and the Golden Age of the Pharaohs' — seen by 8 million",
                "Curse of the Pharaohs legend — enduring cultural myth",
                "Egyptological methodology advanced by Carter's unprecedented documentation",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Howard Carter", "targetSlug": "howard-carter", "note": "Archaeologist who discovered his intact tomb KV62 (1922)"},
                {"type": "INFLUENCES", "target": "Akhenaten", "targetSlug": "akhenaten", "note": "Predecessor whose Amarna revolution he reversed; possibly father"},
                {"type": "INFLUENCES", "target": "Nefertiti", "targetSlug": "nefertiti", "note": "Possibly his mother or stepmother"},
                {"type": "INFLUENCES", "target": "Ay", "targetSlug": "ay", "note": "Advisor and successor who directed policy"},
                {"type": "INFLUENCES", "target": "Horemheb", "targetSlug": "horemheb", "note": "Military commander and eventual pharaoh after Ay"},
                {"type": "INFLUENCES", "target": "Valley of the Kings", "targetSlug": "valley-of-the-kings", "note": "His tomb KV62 is the most famous in the Valley"},
                {"type": "INFLUENCES", "target": "Golden death mask", "targetSlug": "mask-of-tutankhamun", "note": "11 kg solid gold — most recognized object in Egyptology"},
                {"type": "INFLUENCES", "target": "Lord Carnarvon", "targetSlug": "lord-carnarvon", "note": "Patron who funded Carter's excavations; died 1923"},
                {"type": "OCCURS_IN", "target": "Egypt", "targetSlug": "egypt", "note": "Pharaoh of Upper and Lower Egypt"},
                {"type": "INFLUENCES", "target": "Amun (deity)", "targetSlug": "amun", "note": "Restored Amun cult to supremacy in Egyptian religion"},
                {"type": "INFLUENCES", "target": "18th Dynasty Egypt", "targetSlug": "eighteenth-dynasty-egypt", "note": "Reigned at the dynasty's richest period"},
                {"type": "INFLUENCES", "target": "Egyptian Museum Cairo", "targetSlug": "egyptian-museum-cairo", "note": "His treasures housed in Cairo's national museum"},
                {"type": "INFLUENCES", "target": "Ankhesenamun", "targetSlug": "ankhesenamun", "note": "His wife — possibly Nefertiti's daughter"},
                {"type": "INFLUENCES", "target": "Amarna Period", "targetSlug": "amarna-period", "note": "His brief reign formally ended the Amarna experiment"},
                {"type": "INFLUENCES", "target": "Egyptology", "targetSlug": "egyptology", "note": "KV62 discovery defined modern Egyptological practice"},
            ],
            "historicalSignificance": {
                "significanceScore": 8,
                "significanceCategory": "continental",
                "significanceNarrative": "Tutankhamun's intact tomb, discovered in 1922 after 3,300 years, contained the greatest collection of ancient Egyptian material culture ever found — transforming global knowledge of the New Kingdom and sparking 'Tutmania,' the modern world's fascination with ancient Egypt."
            },
            "quote": "'At first I could see nothing, the hot air escaping from the chamber causing the candle flame to flicker, but presently, as my eyes grew accustomed to the light, details of the room within emerged slowly from the mist — strange animals, statues, and gold — everywhere the glint of gold.' — Howard Carter, November 26, 1922",
            "places": ["Valley of the Kings, Luxor, Egypt (tomb KV62)", "Amarna (early life)", "Thebes (capital during his reign)"],
            "subjectHeadings": "Tutankhamun — Pharaohs and Rulers — Egypt — Classical",
            "subjects": ["Egypt", "ancient Egypt", "archaeology", "New Kingdom", "18th Dynasty", "Amarna Period", "Egyptology", "Classical era", "golden mask", "Valley of the Kings"],
            "frameworks": ["cultural-history", "religious-thought", "state-formation"],
        }
    },

    # ── 7. Richard the Lionheart ─────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221richard-the-lionheart.json",
        "slug": "richard-the-lionheart",
        "era_correction": None,
        "data": {
            "summary": (
                "Richard I 'the Lionheart' (1157–1199) was King of England, Duke of Normandy, and the most celebrated military commander of the Third Crusade — a warrior king who spent less than six months of his ten-year reign on English soil, yet whose chivalric legend became the central archetype of medieval kingship in Western imagination. Contemporary chroniclers, including Muslim writers like Baha ad-Din and Imad ad-Din, praised his courage and military genius even as they fought against him.\n\n"
                "Richard led the Third Crusade (1189–1192) after the catastrophic fall of Jerusalem to Saladin (1187). He captured Cyprus (1191), won the decisive Battle of Arsuf, and retook Jaffa — demonstrating tactical genius that forced Saladin's respect. In a famous moment recorded by both sides, Saladin sent a horse to Richard when his was killed in battle. Though Richard never retook Jerusalem, he negotiated the Treaty of Jaffa (1192) securing Christian access to Jerusalem's holy sites.\n\n"
                "On his return, he was captured by Duke Leopold of Austria and held for ransom — costing England 150,000 marks (roughly three years of national revenue) for his release. He died at 41 from a crossbow wound at the minor castle of Chalus-Chabrol, reportedly forgiving the young bowman who shot him.\n\n"
                "His legacy is paradoxical: as an English king he was an absentee Norman ruler who spoke almost no English; as a military hero he remains the exemplar of crusading chivalry in literature from Ivanhoe to modern fantasy fiction."
            ),
            "causes": [
                "Saladin's conquest of Jerusalem (1187) triggering Pope Gregory VIII's Third Crusade call",
                "Henry II's death (1189) making Richard king and giving him resources for crusading",
                "Crusading ideology tying Christian knighthood to reconquest of Holy Land",
                "Angevin Empire's wealth and power enabling the largest crusading force of the era",
            ],
            "effects": [
                "Third Crusade (1189–1192) — capture of Cyprus, Jaffa, Arsuf victory",
                "Treaty of Jaffa (1192) securing Christian pilgrimage access to Jerusalem",
                "Ransom crisis (1192–94) depleting English royal treasury",
                "Chivalric legend — defining archetype of the warrior-king in Western culture",
                "Ivanhoe, Crusades fiction, Robin Hood legend — built around Richard's myth",
                "Diplomatic precedent of Saladin-Richard mutual respect across religious war",
                "Saladin admired Richard's valor even in opposition — cross-cultural military reputation",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Saladin", "targetSlug": "saladin", "note": "Greatest opponent; mutual military respect across religious war"},
                {"type": "INFLUENCES", "target": "Third Crusade", "targetSlug": "third-crusade", "note": "Led the defining crusade of the medieval period"},
                {"type": "INFLUENCES", "target": "Henry II of England", "targetSlug": "henry-ii-of-england", "note": "Father; rebelled against and succeeded him"},
                {"type": "INFLUENCES", "target": "Philip II of France", "targetSlug": "philip-ii-of-france", "note": "Crusade partner who deserted and attacked Normandy"},
                {"type": "INFLUENCES", "target": "Eleanor of Aquitaine", "targetSlug": "eleanor-of-aquitaine", "note": "Mother who secured his ransom and regency"},
                {"type": "INFLUENCES", "target": "Holy Roman Emperor Henry VI", "targetSlug": "henry-vi-holy-roman-emperor", "note": "Ransomed Richard from Duke Leopold through imperial extortion"},
                {"type": "INFLUENCES", "target": "Crusades", "targetSlug": "crusades", "note": "Greatest crusader king — personified crusading ideal"},
                {"type": "INFLUENCES", "target": "Jerusalem", "targetSlug": "jerusalem", "note": "Failed to retake the city he campaigned three years to reach"},
                {"type": "INFLUENCES", "target": "Battle of Arsuf", "targetSlug": "battle-of-arsuf", "note": "Decisive tactical victory over Saladin's forces (1191)"},
                {"type": "OCCURS_IN", "target": "England", "targetSlug": "england", "note": "King of England — spent < 6 months in country during reign"},
                {"type": "OCCURS_IN", "target": "Holy Land (Israel/Palestine)", "targetSlug": "holy-land", "note": "Theater of his military campaigns"},
                {"type": "INFLUENCES", "target": "Cyprus", "targetSlug": "cyprus", "note": "Conquered in 1191; sold to Knights Templar"},
                {"type": "INFLUENCES", "target": "Chivalry (concept)", "targetSlug": "chivalry", "note": "Embodied the chivalric ideal in both Christian and Muslim accounts"},
                {"type": "INFLUENCES", "target": "Walter Scott", "targetSlug": "walter-scott", "note": "Ivanhoe (1819) made Richard the literary archetype of knighthood"},
                {"type": "INFLUENCES", "target": "Angevin Empire", "targetSlug": "angevin-empire", "note": "Ruled England, Normandy, Anjou, Aquitaine"},
            ],
            "historicalSignificance": {
                "significanceScore": 8,
                "significanceCategory": "continental",
                "significanceNarrative": "Richard the Lionheart led the Third Crusade with military genius that earned the respect of Saladin himself, negotiated Christian access to Jerusalem's holy sites, and became the defining archetype of the warrior-king in Western chivalric tradition — his legend enduring in literature from Ivanhoe to modern fantasy."
            },
            "quote": "'I would sell London itself if I could find a buyer.' — Richard I (attributed, on financing the Crusade)",
            "places": ["Oxford, England (birthplace)", "Acre, Israel (Third Crusade base)", "Chalus-Chabrol, France (death)"],
            "subjectHeadings": "Richard the Lionheart — Kings and Crusaders — England — Medieval",
            "subjects": ["England", "Crusades", "medieval Europe", "Holy Land", "chivalry", "Angevin Empire", "Third Crusade", "Saladin", "medieval warfare", "12th century"],
            "frameworks": ["religious-conflict", "military-history", "state-formation"],
        }
    },

    # ── 8. Tamerlane ─────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221tamerlane.json",
        "slug": "tamerlane",
        "era_correction": None,
        "data": {
            "summary": (
                "Timur (Tamerlane) (1336–1405) was a Turco-Mongol conqueror from Transoxiana who built the last great Mongol empire, conquering from Delhi to Anatolia in a career of systematic devastation that killed an estimated 17 million people — perhaps 5% of the world's population. He claimed descent from Genghis Khan and saw himself as both a Muslim ruler and a world conqueror in the Mongol tradition, combining piety and mass atrocity in equal measure.\n\n"
                "Tamerlane's campaigns were campaigns of deliberate terror: at Delhi (1398) he massacred 100,000 prisoners before battle; at Baghdad (1401) he built towers of skulls; at Isfahan (1387) he ordered the execution of 70,000 civilians whose severed heads were stacked into pyramids. His speed and logistical mastery were legendary: he defeated the Golden Horde (1395), sacked Delhi (1398), destroyed Damascus (1401), captured the Ottoman Sultan Bayezid I at Ankara (1402), and turned toward China before his death in 1405.\n\n"
                "The paradox of Tamerlane is cultural: while devastating cities across Asia, he adorned his capital Samarkand with the greatest architecture of the Islamic world, employing captured craftsmen to build the Gur-e-Amir mausoleum (his tomb), the Registan, and Bibi-Khanym Mosque. His court was a center of Persian literature and scholarship; he was reportedly a brilliant chess player.\n\n"
                "His empire did not long survive him, but the Timurid dynasty he founded produced Babur — who conquered India and founded the Mughal Empire — making Tamerlane the ancestor of the rulers who built the Taj Mahal."
            ),
            "causes": [
                "Mongol imperial legacy of Genghis Khan providing model and legitimacy",
                "Fragmentation of Mongol khanates creating power vacuum Timur exploited",
                "Transoxiana's strategic position at the heart of Silk Road trade",
                "Personal military genius and ruthless elimination of rivals",
            ],
            "effects": [
                "17 million deaths (est. 5% of world population) — among history's highest death tolls",
                "Destruction of Delhi sultanate opening India to future Mughal conquest",
                "Battle of Ankara (1402) — Ottoman Sultan Bayezid I captured; empire temporarily fragmented",
                "Samarkand as architectural marvel — Registan, Gur-e-Amir, Bibi-Khanym",
                "Timurid dynasty founding Mughal Empire (Babur) — builders of Taj Mahal",
                "Disruption of Silk Road trade through Central Asian devastation",
                "Prolonged Ottoman recovery delaying fall of Constantinople by 50 years",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Genghis Khan", "targetSlug": "genghis-khan", "note": "Model and claimed ancestor; Timur revived Mongol imperial tradition"},
                {"type": "INFLUENCES", "target": "Bayezid I (Ottoman)", "targetSlug": "bayezid-i", "note": "Ottoman Sultan captured at Battle of Ankara (1402)"},
                {"type": "INFLUENCES", "target": "Delhi Sultanate", "targetSlug": "delhi-sultanate", "note": "Sacked Delhi (1398), killing 100,000; permanent damage to sultanate"},
                {"type": "INFLUENCES", "target": "Mughal Empire", "targetSlug": "mughal-empire", "note": "His great-great-grandson Babur founded the Mughal Empire"},
                {"type": "INFLUENCES", "target": "Babur", "targetSlug": "babur", "note": "Timurid prince who founded the Mughal dynasty"},
                {"type": "INFLUENCES", "target": "Battle of Ankara (1402)", "targetSlug": "battle-of-ankara-1402", "note": "Destroyed Ottoman army; captured Bayezid I"},
                {"type": "INFLUENCES", "target": "Samarkand", "targetSlug": "samarkand", "note": "Capital adorned with Islamic world's greatest architecture"},
                {"type": "INFLUENCES", "target": "Gur-e-Amir mausoleum", "targetSlug": "gur-e-amir", "note": "His magnificent tomb in Samarkand"},
                {"type": "INFLUENCES", "target": "Golden Horde", "targetSlug": "golden-horde", "note": "Defeated and destroyed Golden Horde at Terek River (1395)"},
                {"type": "INFLUENCES", "target": "Baghdad", "targetSlug": "baghdad", "note": "Sacked in 1401; built towers of severed skulls"},
                {"type": "OCCURS_IN", "target": "Uzbekistan", "targetSlug": "uzbekistan", "note": "Born in Kesh (Shahrisabz), modern Uzbekistan"},
                {"type": "INFLUENCES", "target": "Mamluk Sultanate", "targetSlug": "mamluk-sultanate", "note": "Sacked Damascus (1401), displacing thousands of craftsmen to Samarkand"},
                {"type": "INFLUENCES", "target": "Silk Road", "targetSlug": "silk-road", "note": "His campaigns disrupted Central Asian trade routes"},
                {"type": "INFLUENCES", "target": "Ottoman Empire", "targetSlug": "ottoman-empire", "note": "Battle of Ankara fragmented Ottoman power for 50 years"},
                {"type": "INFLUENCES", "target": "Persian literature", "targetSlug": "persian-literature", "note": "His court patronized Persian poetry and scholarship at Samarkand"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Tamerlane killed approximately 17 million people — 5% of the world's population — in campaigns from Delhi to Ankara, shattered the Ottoman and Delhi sultanates, adorned Samarkand with Islam's greatest architecture, and founded the Timurid dynasty whose descendant Babur established the Mughal Empire."
            },
            "quote": "'I am not a man of blood; and God is my witness that in all my wars I have never been the aggressor, and that my enemies have always been the authors of their own calamity.' — Tamerlane (from his purported autobiography, Tuzukat-i-Timuri)",
            "places": ["Samarkand, Uzbekistan (capital)", "Kesh (Shahrisabz), Uzbekistan (birthplace)", "Delhi, India", "Ankara, Turkey"],
            "subjectHeadings": "Tamerlane — Conquerors and Rulers — Central Asia — Medieval",
            "subjects": ["Uzbekistan", "Central Asia", "Mongol Empire", "Ottoman Empire", "India", "Medieval Islam", "Silk Road", "Samarkand", "14th century", "military conquest"],
            "frameworks": ["empire-building", "military-history", "cultural-exchange"],
        }
    },
]


# ── Core writer ──────────────────────────────────────────────────────────────

def enrich_entity(file_path, slug, data, era_correction, dry_run=False):
    if not os.path.exists(file_path):
        return f"FILE NOT FOUND: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entities = doc.get("entities", [])
    target = next((e for e in entities if e.get("slug") == slug), None)
    if not target:
        return f"SLUG NOT FOUND: {slug} in {file_path}"

    dj = target.get("detailsJson")
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    current_summary = (dj or {}).get("summary", "")
    new_summary = data["summary"]

    if len(current_summary) >= SKIP_THRESHOLD:
        return f"SKIP {slug} (already {len(current_summary)}c)"

    if dry_run:
        return f"→ Enriching {slug}  (was {len(current_summary)}c → {len(new_summary)}c)"

    if "detailsJson" not in target or target["detailsJson"] is None or isinstance(target["detailsJson"], str):
        target["detailsJson"] = {}

    dj = target["detailsJson"]
    now = datetime.now(timezone.utc).isoformat()

    edit_log = dj.get("_editLog", [])
    for field in ["summary", "causes", "effects", "relationships", "historicalSignificance",
                  "quote", "places", "subjectHeadings", "subjects", "frameworks"]:
        if field in data:
            old_val = dj.get(field, None)
            new_val = data[field]
            if old_val != new_val:
                edit_log.append({
                    "field": field,
                    "oldValue": old_val,
                    "newValue": new_val if len(str(new_val)) < 200 else str(new_val)[:200] + "…",
                    "editorId": EDITOR_ID,
                    "sessionId": SESSION_ID,
                    "timestamp": now,
                })

    for field, value in data.items():
        dj[field] = value

    dj["_editLog"] = edit_log

    if era_correction:
        target["era"] = era_correction

    target["_unsyncedEdits"] = True

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    return f"✓ Saved {file_path}"


def main():
    if DRY_RUN:
        print("=== DRY RUN — no files will be written ===\n")

    print(f"Batch 61 enrichment — {len(ENRICHMENTS)} entities\n")

    enriched, skipped, failed = 0, 0, 0
    for item in ENRICHMENTS:
        slug = item["slug"]
        print(f"[{slug}]")
        result = enrich_entity(
            item["file"], slug, item["data"],
            item.get("era_correction"), dry_run=DRY_RUN
        )
        print(f"  {result}")
        if "SKIP" in result:
            skipped += 1
        elif result.startswith("✓") or result.startswith("→"):
            enriched += 1
        else:
            failed += 1

    tag = "DRY RUN" if DRY_RUN else "DONE"
    print(f"\n{tag}: {enriched} enriched, {skipped} skipped, {failed} failed")
    if not DRY_RUN and enriched > 0:
        print("\nNext step: env $(cat .env | xargs) npx tsx scripts/sync_gateway.ts --local")


if __name__ == "__main__":
    main()
