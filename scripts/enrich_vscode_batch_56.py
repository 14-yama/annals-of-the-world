#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 56 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

From 781-Class (milestone documents):
  gettysburg-address-1863, fourteen-points-1918, federal-reserve-act-1913,
  de-bello-gallico-caesar, funeral-oration-via-thucydides
From 782-Class (epic poetry):
  paradise-lost, ramayana, pan-tadeusz
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-56-may2026"

ENRICHMENTS = {

"gettysburg-address-1863": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781gettysburg-address-1863.json",
  "slug": "gettysburg-address-1863",
  "data": {
    "summary": "The Gettysburg Address is a speech delivered by President Abraham Lincoln (1809–1865) on 19 November 1863 at the dedication of the Soldiers' National Cemetery at Gettysburg, Pennsylvania — four and a half months after the Battle of Gettysburg (1–3 July 1863), the bloodiest battle of the American Civil War. The speech is approximately 272 words long and was delivered in approximately two minutes — Lincoln was the second speaker of the day, following Edward Everett's two-hour oration. Five manuscript copies of the speech exist in Lincoln's hand (the Bliss copy is considered the authoritative text), and the speech was reported slightly differently by the journalists present.\n\nThe Gettysburg Address redefined the purpose of the Civil War — Lincoln reframed the war not merely as a constitutional struggle to preserve the Union, but as a new birth of freedom that would vindicate the Declaration of Independence's proposition that 'all men are created equal.' The speech's opening 'Four score and seven years ago' referred to 1776 (not 1787, the year of the Constitution), deliberately placing the Declaration of Independence — with its equality principle — as the foundational American document, over the heads of those who argued that the Constitution protected slavery. In this sense, the Gettysburg Address is simultaneously a eulogy, a war aim, and a constitutional argument.\n\nThe Gettysburg Address is arguably the most influential political speech in American history — it shaped the post-Civil War amendments to the Constitution (the 13th, 14th, and 15th amendments), inspired Woodrow Wilson's Fourteen Points (1918), and has been cited in every subsequent American debate about equality, democracy, and national purpose. Its closing phrase — 'government of the people, by the people, for the people' — is one of the most quoted definitions of democracy in the world. The speech's conciseness (272 words, two minutes) in contrast to Everett's two-hour address has made it a permanent model of political brevity.",
    "causes": [
      "The Battle of Gettysburg (1–3 July 1863) — the largest and bloodiest battle of the American Civil War, with approximately 51,000 casualties — created the immediate context for the dedication of the Soldiers' National Cemetery and Lincoln's address, which was intended to give meaning to the deaths of thousands of Union soldiers.",
      "Lincoln's evolving thinking about the meaning of the Civil War — his Preliminary Emancipation Proclamation (22 September 1862) and the Emancipation Proclamation (1 January 1863) had already linked the Union cause to the abolition of slavery, and the Gettysburg Address extended this by connecting the war to the Declaration of Independence's equality principle.",
      "The rhetorical tradition of the American funeral oration — the genre of the civic eulogy, exemplified by Pericles's Funeral Oration (via Thucydides) — gave Lincoln a classical model for transforming a dedication ceremony into a statement of national purpose, though his speech achieved its effect through radical brevity rather than the extended oratory of the classical tradition."
    ],
    "effects": [
      "The Gettysburg Address shaped the post-Civil War constitutional amendments — the 14th Amendment's equal protection and due process clauses (1868) embodied the equality principle that Lincoln had articulated at Gettysburg, making the speech a constitutional as well as rhetorical landmark.",
      "Lincoln's phrase 'government of the people, by the people, for the people' — derived from Daniel Webster and Theodore Parker but given its definitive form at Gettysburg — became the most widely quoted definition of democracy in the world, cited in constitutions, speeches, and political arguments across every continent.",
      "The Gettysburg Address established the model of the short, focused political speech as a vehicle for profound national redefinition — its 272-word text, delivered in contrast to Everett's two-hour oration, demonstrated that concision could achieve greater rhetorical power than elaboration, and the speech has been a model for political brevity ever since."
    ],
    "relationships": [
      {"sourceSlug": "abraham-lincoln", "sourceName": "Abraham Lincoln (1809–1865 — 16th US President; Civil War; Emancipation Proclamation)", "verb": "DELIVERS", "targetSlug": "gettysburg-address-1863", "targetName": "Gettysburg Address (1863 — 272 words; equality principle; 'of the people, by the people, for the people')", "context": "Lincoln delivered the Gettysburg Address on 19 November 1863 — reframing the Civil War as a struggle to vindicate the Declaration of Independence's equality principle."},
      {"sourceSlug": "gettysburg-address-1863", "sourceName": "Gettysburg Address (14th Amendment — equal protection; due process; constitutional legacy)", "verb": "SHAPES", "targetSlug": "fourteenth-amendment-1868", "targetName": "14th Amendment (1868 — equal protection; due process; post-Civil War constitutional revision)", "context": "The 14th Amendment (1868) embodied the equality principle Lincoln articulated at Gettysburg — making the speech a constitutional as well as rhetorical landmark in American history."},
      {"sourceSlug": "funeral-oration-via-thucydides", "sourceName": "Funeral Oration of Pericles (via Thucydides — civic eulogy; democratic purpose; rhetorical model)", "verb": "MODELS", "targetSlug": "gettysburg-address-1863", "targetName": "Gettysburg Address (1863 — Lincoln; 272 words; civic eulogy as national redefinition)", "context": "Pericles's Funeral Oration (via Thucydides) provided the classical model of the civic eulogy as a statement of national purpose that Lincoln adapted — though with radical brevity rather than extended oratory."}
    ],
    "places": [
      {"name": "Gettysburg, Pennsylvania (1863 — Soldiers' National Cemetery dedication; Battle of Gettysburg 1–3 July 1863)", "role": "The Gettysburg Address was delivered at the dedication of the Soldiers' National Cemetery on 19 November 1863 — four months after the bloodiest battle of the Civil War on the same ground"},
      {"name": "United States (constitutional legacy — 14th Amendment; democracy definition; global influence)", "role": "The Gettysburg Address's equality principle shaped the 14th Amendment and its phrase 'government of the people, by the people, for the people' became the most widely quoted definition of democracy in the world"}
    ],
    "subjects": ["American History", "19th Century", "Abraham Lincoln", "Political Speeches", "Civil War", "American Democracy", "Constitutional History", "Rhetoric"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Gettysburg Address (Lincoln, 1863) is arguably the most influential political speech in American history — its 272 words redefined the Civil War as a struggle for equality, shaped the 14th Amendment, and gave the world its most quoted definition of democracy ('government of the people, by the people, for the people'). Its model of radical brevity has defined the ideal of political speech ever since.",
      "significanceCategory": "world-changing"
    }
  }
},

"fourteen-points-1918": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781fourteen-points-1918.json",
  "slug": "fourteen-points-1918",
  "data": {
    "summary": "The Fourteen Points is a speech delivered by President Woodrow Wilson (1856–1924) to a joint session of the United States Congress on 8 January 1918, articulating fourteen principles for a post-World War I peace settlement and the organisation of international relations. The speech responded to the Russian Bolsheviks' publication of the secret Allied treaties (after the October Revolution, 1917) and to the need to articulate American war aims that were distinct from the imperial war aims of the European powers. The Fourteen Points proposed freedom of navigation, free trade, arms reduction, self-determination of peoples, colonial adjustments, and — most influentially — the establishment of a League of Nations as a general association of nations guaranteeing political independence and territorial integrity to all states.\n\nThe Fourteen Points became the basis for Germany's armistice negotiations in 1918 — Germany accepted the armistice largely on the expectation that the peace would be based on Wilson's principles — and then the framework for the Paris Peace Conference (1919) at which the Treaty of Versailles was negotiated. Wilson's insistence on including the League of Nations covenant in the Treaty of Versailles achieved the creation of the League, though the United States Senate's rejection of the Treaty (March 1920) meant that the United States never joined the organisation Wilson had championed.\n\nThe Fourteen Points are one of the most consequential political documents of the 20th century — the principle of national self-determination reshaped the map of Europe (creating new states from the ruins of the Austro-Hungarian, Russian, and Ottoman empires), the League of Nations established the precedent for international collective security that was inherited by the United Nations (1945), and Wilson's idealistic internationalism defined an entire tradition of American foreign policy. The gap between Wilson's idealistic principles and the punitive reality of the Treaty of Versailles — which Germany experienced as a humiliation — contributed directly to the conditions that made the rise of National Socialism possible.",
    "causes": [
      "The United States' entry into World War I (April 1917) — and Wilson's need to articulate American war aims that were idealistic and distinct from the territorial ambitions of the European Allies — created the context for the Fourteen Points as a democratic, anti-imperialist vision of post-war order.",
      "The Bolshevik Revolution (October 1917) and the Russian Bolsheviks' publication of the secret Allied treaties — revealing that Britain, France, and Russia had agreed to divide the spoils of war in ways that contradicted Allied rhetoric about democratic principles — made it urgent for Wilson to articulate an alternative vision of the war's purpose.",
      "Wilson's idealistic liberal internationalism — shaped by his academic background, his Presbyterian faith, and his reading of American democratic tradition — drove the particular character of the Fourteen Points, which combined Enlightenment principles (self-determination, open diplomacy, free trade) with a new institutional proposal (the League of Nations)."
    ],
    "effects": [
      "The Fourteen Points reshaped the map of Europe — the principle of national self-determination was applied (selectively and imperfectly) at the Paris Peace Conference, creating new states including Poland, Czechoslovakia, Yugoslavia, and the Baltic republics from the ruins of the Austro-Hungarian, Russian, and Ottoman empires.",
      "The League of Nations — Point XIV of Wilson's speech — established the first permanent international collective security organisation, the direct institutional predecessor of the United Nations (1945); though the United States never joined, the League established the principle of multilateral international governance that shaped the post-1945 world order.",
      "The gap between Wilson's idealistic Fourteen Points and the punitive Treaty of Versailles (which Germany experienced as betrayal, since it had accepted the armistice expecting a Wilsonian peace) — particularly the war guilt clause and the reparations demands — contributed directly to the political humiliation that facilitated the rise of National Socialism in Germany."
    ],
    "relationships": [
      {"sourceSlug": "woodrow-wilson", "sourceName": "Woodrow Wilson (1856–1924 — 28th US President; Paris Peace Conference; League of Nations)", "verb": "DELIVERS", "targetSlug": "fourteen-points-1918", "targetName": "Fourteen Points (8 January 1918 — self-determination; League of Nations; post-WWI order)", "context": "Wilson delivered the Fourteen Points to Congress on 8 January 1918 — articulating the principles for post-WWI peace that shaped the Paris Peace Conference and created the League of Nations."},
      {"sourceSlug": "fourteen-points-1918", "sourceName": "Fourteen Points (League of Nations covenant — Treaty of Versailles; collective security; UN predecessor)", "verb": "ESTABLISHES", "targetSlug": "league-of-nations", "targetName": "League of Nations (1920–1946 — collective security; Wilson's Point XIV; UN institutional predecessor)", "context": "Wilson's Point XIV established the League of Nations — the first permanent collective security organisation and the direct institutional predecessor of the United Nations (1945)."},
      {"sourceSlug": "fourteen-points-1918", "sourceName": "Fourteen Points (self-determination gap — Versailles betrayal; German humiliation; rise of Nazism)", "verb": "CONTRIBUTES_TO", "targetSlug": "treaty-of-versailles-1919", "targetName": "Treaty of Versailles (1919 — war guilt clause; reparations; German humiliation; Weimar crisis)", "context": "Germany's experience of the Treaty of Versailles as a betrayal of Wilson's Fourteen Points — accepting the armistice on Wilsonian terms and receiving a punitive peace instead — contributed to the political humiliation that facilitated the rise of National Socialism."}
    ],
    "places": [
      {"name": "Washington DC (8 January 1918 — joint session of Congress; Wilson's address; WWI context)", "role": "Wilson delivered the Fourteen Points to a joint session of Congress on 8 January 1918 — the speech responded to the Bolshevik publication of secret Allied treaties and articulated American war aims"},
      {"name": "Paris (1919 Peace Conference — League of Nations; new European states; Versailles Treaty)", "role": "The Paris Peace Conference (1919) was the arena where Wilson's Fourteen Points were negotiated — the principle of self-determination reshaped the European map while the League of Nations was created as Wilson's institutional legacy"}
    ],
    "subjects": ["American History", "20th Century", "Woodrow Wilson", "World War I", "International Relations", "League of Nations", "Self-Determination", "Peace Treaties"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Fourteen Points (Wilson, 1918) reshaped the post-WWI world — the principle of national self-determination created new European states, Wilson's Point XIV established the League of Nations (UN predecessor), and Germany's armistice was based on Wilson's principles. The gap between Wilsonian idealism and the punitive Versailles Treaty contributed to the conditions that made the rise of National Socialism possible.",
      "significanceCategory": "world-changing"
    }
  }
},

"federal-reserve-act-1913": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781federal-reserve-act-1913.json",
  "slug": "federal-reserve-act-1913",
  "data": {
    "summary": "The Federal Reserve Act is a United States federal statute signed into law by President Woodrow Wilson on 23 December 1913, establishing the Federal Reserve System as the central bank of the United States. The Act was the product of years of debate about American monetary and banking policy following the Panic of 1907, when J.P. Morgan had personally orchestrated a private banking bailout to prevent financial collapse — demonstrating both the need for a lender of last resort and the unacceptability of allowing that role to be filled by a private individual. The Act created a system of twelve regional Federal Reserve Banks, overseen by a Federal Reserve Board in Washington, with authority to issue Federal Reserve Notes (replacing the national bank notes that had previously served as paper currency), set interest rates, regulate member banks, and act as lender of last resort to the banking system.\n\nThe Federal Reserve Act represented a compromise between competing visions of American banking — those who wanted a single centralised bank (on the European model), those who wanted a system controlled entirely by private bankers, and those (particularly Populist Democrats) who feared both Wall Street dominance and centralised financial power. The resulting system of twelve regional banks, with a mix of government and private oversight, reflected these competing pressures and has remained the basic structure of the Federal Reserve System to the present day.\n\nThe Federal Reserve System has become one of the most powerful financial institutions in the world — its decisions on interest rates (the Federal Funds Rate) affect borrowing costs, inflation, employment, and financial conditions not only in the United States but globally, given the dollar's role as the world's primary reserve currency. The Fed's responses to financial crises (the Great Depression, the 2008 financial crisis, the COVID-19 pandemic) have made it the central actor in American and global economic stabilisation, and its independence from direct political control — established by the Act's structure — has been continuously contested in American political debate.",
    "causes": [
      "The Panic of 1907 — a severe financial panic that threatened to collapse the American banking system and was only resolved by J.P. Morgan's personal intervention as a private lender of last resort — demonstrated the urgent need for an institutional mechanism to prevent banking panics and provide emergency liquidity to the financial system.",
      "The Aldrich-Vreeland Act (1908) and the National Monetary Commission (1908–1912) — established in response to the Panic of 1907 — provided the institutional study and legislative preparation for the Federal Reserve Act, with Senator Nelson Aldrich's plan providing the basis (modified to address Democratic concerns about centralisation and Wall Street control) for the final legislation.",
      "The progressive political environment of the Wilson administration (1913) — with its skepticism of big business concentration and Wall Street power, combined with the need for banking system reform — drove the specific compromise structure of the Federal Reserve Act, balancing the need for central bank functions with the political imperative to prevent Wall Street domination."
    ],
    "effects": [
      "The Federal Reserve System became the central actor in American and global monetary policy — its Federal Funds Rate decisions affect borrowing costs, inflation, and financial conditions worldwide, given the dollar's status as the primary global reserve currency, making the Fed the most powerful central bank in the world.",
      "The Fed's responses to financial crises — Herbert Hoover's Fed's contractionary policy in the Great Depression (widely held to have deepened the Depression), the Bernanke Fed's extraordinary expansion in 2008–2009, and the Powell Fed's massive stimulus in response to COVID-19 — demonstrate the institution's pivotal role in shaping the trajectory of economic crises.",
      "The Federal Reserve Act established the model of the independent central bank — an institution with authority over monetary policy that operates at arm's length from elected government, though subject to congressional oversight — that was adopted by central banks worldwide and has been continuously contested between advocates of monetary independence and political accountability."
    ],
    "relationships": [
      {"sourceSlug": "woodrow-wilson", "sourceName": "Woodrow Wilson (signed Federal Reserve Act 23 December 1913 — progressive reform; banking system)", "verb": "SIGNS", "targetSlug": "federal-reserve-act-1913", "targetName": "Federal Reserve Act (1913 — twelve regional banks; lender of last resort; US central bank)", "context": "Wilson signed the Federal Reserve Act on 23 December 1913 — establishing the Federal Reserve System as the US central bank, the most consequential institutional outcome of Progressive Era financial reform."},
      {"sourceSlug": "federal-reserve-act-1913", "sourceName": "Federal Reserve Act (Panic of 1907 — J.P. Morgan; banking panic; lender of last resort need)", "verb": "RESPONDS_TO", "targetSlug": "panic-of-1907", "targetName": "Panic of 1907 (J.P. Morgan — private banking bailout; institutional lender of last resort need)", "context": "The Panic of 1907 — when J.P. Morgan personally orchestrated a private banking bailout — demonstrated the need for an institutional lender of last resort, directly driving the creation of the Federal Reserve System."},
      {"sourceSlug": "federal-reserve-act-1913", "sourceName": "Federal Reserve (2008 financial crisis — Bernanke; quantitative easing; lender of last resort)", "verb": "ENABLES", "targetSlug": "financial-crisis-2008", "targetName": "2008 Financial Crisis response (Bernanke Fed — quantitative easing; TARP; global financial stabilisation)", "context": "The Federal Reserve's extraordinary response to the 2008 financial crisis — Ben Bernanke's Fed acting as lender of last resort on a massive scale, deploying quantitative easing — demonstrated the Act's institutional legacy in enabling unprecedented monetary intervention."}
    ],
    "places": [
      {"name": "Washington DC (1913 — Wilson signature; Federal Reserve Board; twelve regional banks)", "role": "The Federal Reserve Act was signed in Washington DC on 23 December 1913 — establishing the Federal Reserve Board in Washington and twelve regional Federal Reserve Banks across the United States"},
      {"name": "United States / Global (Federal Funds Rate — dollar reserve currency; global monetary policy influence)", "role": "The Federal Reserve System's global influence derives from the dollar's status as the primary world reserve currency — the Fed's interest rate decisions affect borrowing costs and financial conditions worldwide"}
    ],
    "subjects": ["American History", "20th Century", "Monetary Policy", "Banking History", "Woodrow Wilson", "Progressive Era", "Central Banking", "Financial History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Federal Reserve Act (1913) established the Federal Reserve System — the most powerful central bank in the world. Born from the Panic of 1907, it created the model of the independent central bank that stabilises the financial system as lender of last resort. The Fed's decisions on interest rates affect borrowing costs and financial conditions worldwide, given the dollar's status as the primary global reserve currency.",
      "significanceCategory": "world-changing"
    }
  }
},

"de-bello-gallico-caesar": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781de-bello-gallico-caesar.json",
  "slug": "de-bello-gallico-caesar",
  "data": {
    "summary": "De Bello Gallico (Commentarii de Bello Gallico, 'Commentaries on the Gallic War') is Julius Caesar's account of the Gallic Wars (58–50 BCE), written largely during or shortly after the campaigns he describes and published as seven books (with an eighth book added by Aulus Hirtius after Caesar's death). Caesar's text is one of the best-preserved works of Classical Latin and has been a cornerstone of Latin education for two thousand years — its clear, elegant prose style (the models of the third-person 'Caesar did this' construction), direct narrative, and vivid accounts of battles, sieges, peoples, and geography made it the standard Latin schoolroom text from late antiquity through the 20th century.\n\nDe Bello Gallico is simultaneously a military memoir, a political propaganda document, and an ethnographic text. Caesar wrote it to communicate his achievements to the Roman public during his absence in Gaul — countering his political enemies in Rome, justifying the enormous expense and violence of the wars, and building the public reputation that would support his eventual bid for supreme power. The ethnographic sections — Caesar's descriptions of the Gauls and the Germanic peoples (their customs, religion, social organisation, and geography) — are the primary ancient source for the cultures of pre-Roman northwestern Europe, making Caesar's text a document of fundamental historical importance even as its political purposes colour every observation.\n\nThe campaigns described in De Bello Gallico permanently transformed Western Europe — Caesar's conquest of Gaul (roughly modern France, Belgium, Switzerland, and parts of Germany) brought the Celtic cultures of northwestern Europe under Roman rule, accelerating the process of Romanisation that shaped the linguistic, legal, and cultural foundations of modern France (whose name derives from the Franks who eventually succeeded the Romans in the region). Caesar's strategic and tactical methods — his use of fortification, engineering, speed of movement, and psychological warfare — remain objects of military study, and his accounts of the sieges of Avaricum and Alesia are classics of military history.",
    "causes": [
      "Caesar's political need to justify and publicise his Gallic campaigns — he wrote De Bello Gallico partly as political propaganda to counter his enemies in Rome, explain the enormous cost of the wars, and build the popular reputation he needed for his eventual bid for supreme power, making the text as much a political document as a military memoir.",
      "The structure of the Roman Republic's provincial government — Caesar's appointment as proconsul of Gaul (58 BCE) gave him command of four legions and the legal authority to wage war in the province, creating the institutional context in which eight years of military expansion could occur under a single commander's direction.",
      "The political and social instability of Gaul in the 50s BCE — Gallic tribal conflicts, the migration of the Helvetii, the threat of Germanic expansion under Ariovistus — provided the immediate occasions for Caesar's initial military interventions, which he used to justify expanding operations across all of Gaul."
    ],
    "effects": [
      "Caesar's conquest of Gaul permanently transformed Western Europe — bringing Celtic northwestern Europe under Roman rule, the conquest accelerated Romanisation (the adoption of Latin, Roman law, and Roman urbanism) in the region that became modern France, Belgium, and Switzerland, shaping the foundations of French language and culture.",
      "De Bello Gallico's ethnographic sections — Caesar's accounts of Gallic and Germanic society, religion, and customs — are the primary ancient source for the cultures of pre-Roman northwestern Europe, making the text a document of fundamental historical importance despite its political purposes and Caesar's limited direct knowledge of the peoples he describes.",
      "De Bello Gallico became the standard Latin schoolroom text from late antiquity through the 20th century — its clear, accessible prose and vivid narrative made it the first substantial Latin text read by generations of students, shaping the Latin education tradition and ensuring Caesar's account remained the dominant framework for understanding the Gallic Wars."
    ],
    "relationships": [
      {"sourceSlug": "julius-caesar", "sourceName": "Julius Caesar (100–44 BCE — Roman general; proconsul of Gaul; political propagandist)", "verb": "AUTHORS", "targetSlug": "de-bello-gallico-caesar", "targetName": "De Bello Gallico (58–50 BCE — Gallic Wars; Gaul conquest; primary source; Latin schoolroom text)", "context": "Caesar wrote De Bello Gallico as both a military memoir and political propaganda during the Gallic Wars (58–50 BCE) — it became the standard Latin schoolroom text and the primary ancient source for pre-Roman Gaul."},
      {"sourceSlug": "de-bello-gallico-caesar", "sourceName": "De Bello Gallico (Gallic conquest — Romanisation; French language foundation; Latin cultural transmission)", "verb": "DOCUMENTS", "targetSlug": "romanisation-of-gaul", "targetName": "Romanisation of Gaul (Latin language; Roman law; modern France linguistic foundation)", "context": "Caesar's conquest of Gaul (documented in De Bello Gallico) brought Celtic northwestern Europe under Roman rule — the resulting Romanisation shaped the Latin-derived foundations of the French language and French cultural identity."},
      {"sourceSlug": "de-bello-gallico-caesar", "sourceName": "De Bello Gallico (siege of Alesia 52 BCE — Vercingetorix; military engineering; fortification)", "verb": "DESCRIBES", "targetSlug": "siege-of-alesia-52-bce", "targetName": "Siege of Alesia (52 BCE — Vercingetorix; Roman circumvallation/contravallation; Gallic resistance end)", "context": "De Bello Gallico's account of the Siege of Alesia (52 BCE) — Caesar's double ring of fortifications besieging Vercingetorix while simultaneously defending against a relief army — is one of the classics of ancient military history."}
    ],
    "places": [
      {"name": "Gaul (58–50 BCE — modern France, Belgium, Switzerland; Caesar's eight-year campaign; Romanisation)", "role": "De Bello Gallico documents Caesar's eight-year conquest of Gaul — the campaigns that brought Celtic northwestern Europe under Roman rule and began the Romanisation that shaped modern French language and culture"},
      {"name": "Rome (political context — propaganda; absent proconsul; Pompey rivalry; Civil War prelude)", "role": "Caesar wrote De Bello Gallico for a Roman audience — the text was political propaganda designed to build his public reputation and counter his enemies in Rome during his absence, making it a prelude to the Civil War"}
    ],
    "subjects": ["Roman History", "Ancient Era", "Julius Caesar", "Military History", "Latin Literature", "Classical Texts", "Gallic Culture", "Roman Republic"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "De Bello Gallico (Caesar, 58–50 BCE) is simultaneously a military memoir, political propaganda, and the primary ancient source for pre-Roman Gaul. Caesar's conquest permanently transformed Western Europe — accelerating the Romanisation that shaped French language and culture — and the text became the standard Latin schoolroom text for two millennia, making it one of the most read works of classical antiquity.",
      "significanceCategory": "world-changing"
    }
  }
},

"funeral-oration-via-thucydides": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781funeral-oration-via-thucydides.json",
  "slug": "funeral-oration-via-thucydides",
  "data": {
    "summary": "The Funeral Oration of Pericles is a speech attributed to the Athenian statesman Pericles (c. 495–429 BCE) and preserved in Thucydides's History of the Peloponnesian War (Book II, chapters 35–46), delivered at the end of the first year of the Peloponnesian War (431–430 BCE) to honour those Athenians who had fallen in the war's first battles. The speech is Thucydides's reconstruction of what Pericles 'said in substance' — a convention of ancient historiography in which the historian composed speeches that captured the speaker's ideas and the occasion's significance, rather than verbatim transcripts — and it stands as one of the most celebrated prose passages in Western literature.\n\nThe Funeral Oration articulates the ideological foundations of Athenian democracy — the openness of Athenian society ('our constitution does not copy the laws of neighbouring states; we are rather a pattern to others than imitators ourselves'), the equality of citizens before the law, the combination of individual freedom with collective civic duty, the intellectual and cultural achievements of Athens, and the distinction between Athenian voluntarism and Spartan compulsion. In Thucydides's framing, the speech is a sustained contrast between the democratic Athenian way of life and the oligarchic Spartan model — a political and cultural manifesto delivered over the bodies of the war dead.\n\nThe Funeral Oration is one of the foundational texts of democratic political thought — its articulation of democratic values (equality, liberty, open debate, civic participation, the rule of law) has been continuously cited in political argument from antiquity to the present, and it provided the direct model for Abraham Lincoln's Gettysburg Address (1863), which shares the funeral oration's structure of using the eulogy of the war dead as a vehicle for defining the political principles for which they died. The speech is the most famous ancient statement of the democratic ideal and a touchstone for every subsequent defence of democratic values.",
    "causes": [
      "The first year of the Peloponnesian War (431–430 BCE) — the annual public funeral (demosion sema) for Athenians killed in war, a civic institution that called for a public eulogy (epitaphios logos) by a prominent citizen — provided the occasion for Pericles's funeral oration and the institutional context in which the speech was delivered.",
      "Pericles's political position at the height of Athenian power — the architect of the Periclean building programme (the Parthenon), the dominant political figure of Athenian democracy in its 'golden age', and the strategic author of the defensive war strategy against Sparta — gave the speech its specific character as a defence of Athenian civilisation and its democratic way of life.",
      "Thucydides's historical method — his practice of composing speeches that captured the substance and significance of historical occasions — shaped the surviving form of the Funeral Oration, making it simultaneously a record of Periclean political thought and a monument of Thucydidean historical writing."
    ],
    "effects": [
      "The Funeral Oration provided the model for the civic eulogy as a vehicle for democratic political statement — its structure (honouring the war dead as the occasion for defining the political principles for which they died) was directly adopted by Lincoln's Gettysburg Address (1863), which shares the Funeral Oration's form, purpose, and rhetorical logic.",
      "The Funeral Oration's articulation of democratic values — equality before the law, open public debate, civic participation, individual freedom within collective obligation — has been continuously cited in democratic political argument from antiquity to the present, making it the most famous ancient statement of the democratic ideal and a touchstone for every subsequent defence of democracy.",
      "The Funeral Oration established Athens's self-image as 'an education to Greece' — a phrase that has resonated through Western political and cultural thought, from Cicero's admiration of Athens to the Enlightenment's recovery of Greek democracy as a model, contributing to the central place of democratic Athens in the Western political imagination."
    ],
    "relationships": [
      {"sourceSlug": "thucydides", "sourceName": "Thucydides (c. 460–400 BCE — History of the Peloponnesian War; speeches reconstructed in substance)", "verb": "RECORDS", "targetSlug": "funeral-oration-via-thucydides", "targetName": "Funeral Oration of Pericles (Thucydides Book II chs 35–46 — Athenian democracy statement; Lincoln model)", "context": "Thucydides preserved the Funeral Oration in Book II of his History — reconstructing Pericles's speech 'in substance,' making the surviving text both a historical document and a monument of Thucydidean historical writing."},
      {"sourceSlug": "funeral-oration-via-thucydides", "sourceName": "Funeral Oration (Lincoln's Gettysburg Address model — civic eulogy structure; democratic war dead)", "verb": "MODELS", "targetSlug": "gettysburg-address-1863", "targetName": "Gettysburg Address (Lincoln, 1863 — civic eulogy; democratic principles; war dead honour)", "context": "The Funeral Oration provided the structural and rhetorical model for Lincoln's Gettysburg Address (1863) — both speeches use the eulogy of the war dead as a vehicle for defining the political principles for which they died."},
      {"sourceSlug": "pericles", "sourceName": "Pericles (c. 495–429 BCE — Athenian statesman; Periclean building programme; Athenian golden age)", "verb": "DELIVERS", "targetSlug": "funeral-oration-via-thucydides", "targetName": "Funeral Oration (431–430 BCE — Athenian democracy defence; 'education to Greece')", "context": "Pericles delivered the Funeral Oration at the public funeral for Athenians killed in the first year of the Peloponnesian War — at the height of Athenian democratic power and cultural achievement."}
    ],
    "places": [
      {"name": "Athens (431–430 BCE — demosion sema; Peloponnesian War; Athenian golden age; Pericles)", "role": "The Funeral Oration was delivered at the Athenian public funeral (demosion sema) at the end of the first year of the Peloponnesian War — at the height of Periclean Athens's cultural and political achievement"},
      {"name": "Western political tradition (democratic ideal — Lincoln, Gettysburg; civic eulogy model; universal democratic touchstone)", "role": "The Funeral Oration has been the most cited ancient statement of democratic values — from Cicero's Rome to the American Founding to Lincoln's Gettysburg Address, it has served as the touchstone for every defence of the democratic ideal"}
    ],
    "subjects": ["Ancient Greek History", "Ancient Era", "Pericles", "Political Thought", "Democratic Theory", "Classical Literature", "Thucydides", "Athenian Democracy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Funeral Oration of Pericles (via Thucydides, 430 BCE) is the foundational statement of democratic political ideals — equality before the law, open debate, civic freedom — and the model for Lincoln's Gettysburg Address (1863). As 'Athens's most famous self-description,' it has been the most cited ancient text in democratic political argument for 2,400 years and the touchstone for every subsequent defence of democratic values.",
      "significanceCategory": "world-changing"
    }
  }
},

"paradise-lost": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782paradise-lost.json",
  "slug": "paradise-lost",
  "data": {
    "summary": "Paradise Lost is an English epic poem by John Milton (1608–1674), first published in ten books in 1667 and revised into twelve books in 1674, the year of Milton's death. The poem narrates the Fall of Man — the disobedience of Adam and Eve in the Garden of Eden, tempted by Satan, and their subsequent expulsion — drawing on the Genesis narrative and the entire tradition of Christian theology, classical epic, and Renaissance literature. Milton wrote Paradise Lost while blind (he had been totally blind since 1652), dictating it to amanuenses, and the poem's extraordinary scope — twelve books, approximately 10,565 lines of blank verse (unrhymed iambic pentameter) — represents one of the supreme achievements of English literature.\n\nParadise Lost opens in medias res with Satan's awakening in Hell after the War in Heaven, and Satan's sustained, complex characterisation — his magnificent defiance ('Better to reign in Hell than serve in Heav'n'), his corruption by envy and pride, his gradual moral degradation as he pursues his revenge against God through humanity — is the poem's most psychologically compelling element. The Romantic poets, particularly William Blake and Percy Bysshe Shelley, famously read Satan as the poem's real hero ('Milton was of the Devil's party without knowing it,' Blake wrote), generating a tradition of interpretation that finds in Satan's defiance an expression of the human spirit's resistance to tyranny.\n\nParadise Lost is the supreme English Protestant epic — its ambition to 'justify the ways of God to men' deploys the full resources of classical epic (invocations of the Muse, the catalogue of heroes, the council of the gods, the hero's journey to the underworld) in service of a Protestant theological argument about free will, the nature of evil, and the means of redemption. The poem's blank verse — Milton's deliberate rejection of rhyme as a 'barbarous' constraint — became the model for subsequent English narrative poetry (Thomson's Seasons, Wordsworth's Prelude) and established blank verse as the elevated register of English epic.",
    "causes": [
      "Milton's Protestant theology and his lifelong engagement with the question of free will — his Arminian conviction that God had given humanity genuine freedom of choice, and that the Fall was therefore genuinely Adam and Eve's responsible act, not divine predestination — drove the poem's theological project of justifying God's ways in a world of sin and suffering.",
      "Milton's personal circumstances at the poem's composition — his blindness, his political defeat after the Restoration of Charles II (1660) undid everything he had worked for during the Interregnum), his sense of surviving as a remnant of a failed revolution — shaped the poem's emotional register, making Paradise Lost a meditation on defeat, loss, and the possibility of inner freedom even in outward bondage.",
      "The entire tradition of Renaissance epic — Ariosto, Tasso, Spenser, Virgil, Homer — provided the literary models against which Milton consciously positioned Paradise Lost, claiming to write an epic 'not less but more heroic' than the classical tradition by choosing a spiritual subject rather than the physical heroism of war."
    ],
    "effects": [
      "Paradise Lost established blank verse as the elevated form of English narrative poetry — Milton's 'verse without rhyme' became the model for Thomson's Seasons, Cowper's The Task, Wordsworth's Prelude, and Keats's Hyperion, establishing a tradition of unrhymed narrative verse that dominated English poetry for two centuries.",
      "The Romantic reinterpretation of Satan as the poem's hero — Blake's 'Milton was of the Devil's party without knowing it' and Shelley's reading of Satan as the spirit of rebellion against tyranny — generated one of the most productive and controversial traditions of literary reinterpretation in English literature, continuing in Philip Pullman's His Dark Materials (which rewrites Paradise Lost from Satan's perspective).",
      "Paradise Lost has been the most influential English poem since Shakespeare — cited as the supreme achievement of English epic by Samuel Johnson, Wordsworth, Blake, and Keats, it set the standard against which all subsequent English narrative poetry was measured and remains one of the two or three poems (with the Faerie Queene and the Canterbury Tales) that define the English literary tradition."
    ],
    "relationships": [
      {"sourceSlug": "john-milton", "sourceName": "John Milton (1608–1674 — Protestant; blind; dictated; Restoration aftermath; 'justify God's ways')", "verb": "AUTHORS", "targetSlug": "paradise-lost", "targetName": "Paradise Lost (1667/1674 — 12 books; blank verse; Fall of Man; Satan's complex characterisation)", "context": "Milton published Paradise Lost in 1667 (10 books), revised to 12 books in 1674 — dictated while blind, it is the supreme English Protestant epic and one of the masterworks of world literature."},
      {"sourceSlug": "paradise-lost", "sourceName": "Paradise Lost (Blake — 'Devil's party'; Shelley — Satan as rebel hero; Romantic reinterpretation)", "verb": "INSPIRES", "targetSlug": "romantic-poets-satan", "targetName": "Romantic reading of Satan (Blake — Devil's party; Shelley — resistance to tyranny; Romantic tradition)", "context": "The Romantic poets reinterpreted Paradise Lost's Satan as the poem's real hero — Blake's 'Milton was of the Devil's party without knowing it' generated a tradition of reading Satan's defiance as an expression of the human spirit."},
      {"sourceSlug": "paradise-lost", "sourceName": "Paradise Lost (Philip Pullman — His Dark Materials; rewrites Paradise Lost; Milton reinterpreted)", "verb": "REWRITTEN_BY", "targetSlug": "his-dark-materials-pullman", "targetName": "His Dark Materials (Philip Pullman — Paradise Lost rewritten; Satan as hero; Dust theology)", "context": "Philip Pullman's His Dark Materials trilogy (1995–2000) explicitly rewrites Paradise Lost from the perspective of the Romantic Satan tradition — one of the most significant modern reinterpretations of Milton's epic."}
    ],
    "places": [
      {"name": "England (1667 — Milton blind; Restoration; Protestant epic; blank verse; English literary tradition)", "role": "Paradise Lost was written and published in Restoration England (1667) — Milton dictated it while blind, a political exile from the Interregnum cause, and the poem reflects both the personal defeat and the spiritual aspiration of its circumstances"},
      {"name": "Western literary tradition (blank verse model — Wordsworth, Thomson, Keats; English epic standard)", "role": "Paradise Lost established blank verse as the elevated form of English narrative poetry and set the standard for English epic — cited as the supreme achievement of English poetry by Johnson, Wordsworth, Blake, and Keats"}
    ],
    "subjects": ["English Literature", "17th Century", "John Milton", "Epic Poetry", "Protestant Theology", "English Language", "Romantic Literature", "Western Canon"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Paradise Lost (Milton, 1667/1674) is the supreme English Protestant epic — its 12 books of blank verse established the elevated narrative form of English poetry, its complex Satan generated the Romantic tradition of the rebel hero, and it set the standard for English epic poetry against which all subsequent work was measured. Philip Pullman's His Dark Materials (1995–2000) is the most recent major rewriting of Milton's epic, demonstrating its continuing generative power.",
      "significanceCategory": "world-changing"
    }
  }
},

"ramayana": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782ramayana.json",
  "slug": "ramayana",
  "data": {
    "summary": "The Ramayana (Sanskrit: रामायण, Rāmāyaṇa, 'Journey/career of Rama') is one of the two great Sanskrit epics of ancient India — attributed to the sage-poet Valmiki and composed in seven kandas (books) of approximately 24,000 Sanskrit slokas (verses) in the Anushtubh metre. The earliest layers of the Ramayana are generally dated to the 5th–4th centuries BCE, though the text reached its current form over several centuries and contains later interpolations. The poem narrates the life of Rama, a prince of the solar dynasty of Ayodhya who is an avatar (divine incarnation) of the god Vishnu — his exile from Ayodhya due to his stepmother Kaikeyi's scheming, his fourteen-year forest exile with his wife Sita and brother Lakshmana, Sita's abduction by the demon king Ravana of Lanka, and Rama's eventual rescue of Sita with the aid of the monkey-king Sugriva and the devotee Hanuman, culminating in the battle at Lanka and Ravana's defeat.\n\nThe Ramayana is one of the most influential texts in South and Southeast Asian cultural history — its narrative has been continuously retold, adapted, and reinterpreted across South Asia, Southeast Asia, and the diaspora for more than two thousand years. The Indonesian shadow puppet tradition (wayang), the Thai Ramakien, the Cambodian Reamker, the Malay Hikayat Seri Rama, and hundreds of regional oral and written versions demonstrate the poem's extraordinary geographic and cultural reach. The annual performance of the Ramlila (dramatisation of the Ramayana) across South Asia is one of the world's largest participatory cultural events, and the 1987 Indian television serial Ramayan (directed by Ramanand Sagar) achieved viewing figures among the highest in Indian television history.\n\nThe Ramayana is a foundational religious, ethical, and cultural text for Hinduism — Rama as the ideal king and dharmic hero (Maryada Purushottam, 'the exemplary man'), Sita as the ideal wife, Hanuman as the ideal devotee, and Lakshmana as the ideal brother provide models of duty, loyalty, and virtue that have shaped Hindu ethical thought for millennia. The Ayodhya site associated with Rama's birth has been a centre of Hindu religious politics, most dramatically in the Babri Masjid mosque demolition (1992) and the subsequent legal and political controversy that culminated in the Supreme Court's 2019 decision to award the contested site to Hindu claimants.",
    "causes": [
      "The ancient Sanskrit oral tradition of the itihasa (literally 'thus it was') — the genre of heroic narrative that included both the Ramayana and the Mahabharata — provided the compositional and performance context in which the Ramayana took shape, attributed to the sage Valmiki who is presented within the text itself as the poem's author.",
      "The theological development of Vaishnavism — the devotional movement centred on Vishnu and his avatars — incorporated Rama as the seventh avatar of Vishnu, making the Ramayana not merely an epic narrative but a devotional religious text, and driving its incorporation into Hindu religious practice across the subcontinent.",
      "The cultural and political spread of Hindu influence across Southeast Asia — through trade networks, religious missions, and the adoption of Sanskrit as a prestige literary language by Southeast Asian courts — carried the Ramayana across South and Southeast Asia, where it was adapted into local languages and performance traditions while retaining the core narrative."
    ],
    "effects": [
      "The Ramayana generated one of the world's largest narrative traditions — hundreds of regional versions in South and Southeast Asian languages (Tamil Kambaramayanam, Telugu Ranganatha Ramayanam, Kannada Torave Ramayana, Thai Ramakien, Cambodian Reamker, Indonesian Kakawin Ramayana) demonstrate the poem's extraordinary capacity to be adapted to different cultures while maintaining recognisable identity.",
      "The 1987 Indian television serial Ramayan (Ramanand Sagar) — broadcast on Doordarshan to viewing figures of approximately 650 million per episode, the highest audience figures in Indian television history at that time — demonstrated the Ramayana's continuing mass cultural reach in modern India, bringing the epic to a television audience larger than any previous performance tradition could have achieved.",
      "The Ayodhya controversy — centred on the site traditionally identified as Rama's birthplace, on which the Babri Masjid mosque stood until its demolition by Hindu nationalist activists in 1992 — demonstrates how the Ramayana's narrative has become embedded in modern Hindu identity politics, with the subsequent Ayodhya Ram Temple (inaugurated by Prime Minister Narendra Modi in January 2024) representing the political resolution of a 500-year dispute."
    ],
    "relationships": [
      {"sourceSlug": "valmiki", "sourceName": "Valmiki (sage-poet — Adi Kavi 'first poet'; Ramayana attributed author; Sanskrit oral tradition)", "verb": "AUTHORS", "targetSlug": "ramayana", "targetName": "Ramayana (c. 5th–4th c. BCE — 24,000 slokas; Rama, Sita, Hanuman; Hindu foundational text)", "context": "The Ramayana is attributed to the sage Valmiki (Adi Kavi, 'first poet') — composed in approximately 24,000 Sanskrit slokas, it is one of the two great Sanskrit epics and a foundational text of Hinduism."},
      {"sourceSlug": "ramayana", "sourceName": "Ramayana (Southeast Asian adaptations — Thai Ramakien; Cambodian Reamker; Indonesian wayang)", "verb": "GENERATES", "targetSlug": "southeast-asian-ramayana-traditions", "targetName": "Southeast Asian Ramayana traditions (Thai Ramakien; Cambodian Reamker; Indonesian Kakawin Ramayana)", "context": "The Ramayana generated a vast tradition of Southeast Asian adaptations — Thai Ramakien, Cambodian Reamker, and Indonesian Kakawin Ramayana demonstrate the epic's extraordinary cultural reach across South and Southeast Asia."},
      {"sourceSlug": "ramayana", "sourceName": "Ramayana (Ayodhya — Babri Masjid 1992; Ram Temple 2024; Hindu nationalism; religious politics)", "verb": "GROUNDS", "targetSlug": "ayodhya-controversy", "targetName": "Ayodhya controversy (Babri Masjid 1992; Ram Temple 2024 — Hindu nationalist political movement)", "context": "The Ayodhya site (traditionally Rama's birthplace) has been the centre of Hindu religious politics — the Babri Masjid demolition (1992) and the Ram Temple inauguration (January 2024) demonstrate the Ramayana's embedding in modern Hindu identity."}
    ],
    "places": [
      {"name": "Ancient India (c. 5th–4th c. BCE — Sanskrit oral tradition; Ayodhya; solar dynasty; Valmiki)", "role": "The Ramayana's earliest layers are dated to the 5th–4th centuries BCE — composed in Sanskrit and attributed to Valmiki, it narrates events set in the ancient kingdoms of northern India"},
      {"name": "South and Southeast Asia (Ramayana traditions — 2,000+ years; Thai, Cambodian, Indonesian adaptations)", "role": "The Ramayana spread across South and Southeast Asia through Hindu cultural influence — generating hundreds of regional versions in Thai, Cambodian, Indonesian, and other languages over more than two millennia"}
    ],
    "subjects": ["Sanskrit Literature", "Ancient Era", "Hinduism", "Epic Poetry", "South Asian Culture", "Southeast Asian Literature", "Valmiki", "Indian Religious Texts"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Ramayana (Valmiki, c. 5th–4th c. BCE) is one of the two great Sanskrit epics and a foundational religious, ethical, and cultural text for Hinduism — its narrative tradition spans South and Southeast Asia in hundreds of regional versions (Thai Ramakien, Cambodian Reamker, Indonesian Kakawin Ramayana). The 1987 Doordarshan television serial reached 650 million viewers per episode, and the 2024 Ram Temple inauguration demonstrates the epic's continuing political and religious centrality.",
      "significanceCategory": "world-changing"
    }
  }
},

"pan-tadeusz": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782pan-tadeusz.json",
  "slug": "pan-tadeusz",
  "data": {
    "summary": "Pan Tadeusz, or The Last Foray in Lithuania (Polish: Pan Tadeusz, czyli ostatni zajazd na Litwie) is the Polish national epic, written by Adam Mickiewicz (1798–1855) and published in Paris in 1834. The poem is composed in twelve books of approximately 9,700 lines of rhyming Polish alexandrines (thirteen-syllable lines) and is set in the year 1811–1812 in the Soplicowo estate in Lithuania (then under Napoleonic-allied rule, following French victory over Russia) — the last period of hope for Polish independence before Napoleon's catastrophic Russian campaign ended the possibility of Polish restoration. The poem narrates the dispute between the noble Soplica and Horeszko families over a ruined castle, the young Tadeusz's love for Zosia, and the broader community of Lithuanian-Polish gentry life — its rituals, hospitality, hunting, natural beauty, and political passions — against the backdrop of Napoleon's Russian campaign and the possibility of Polish liberation.\n\nPan Tadeusz is distinguished by its extraordinary celebration of a lost world — Mickiewicz wrote the poem in Parisian exile, and the poem's famous opening invocation ('Lithuania, my homeland!') is the lament of a man who knows he will never return to the country he is evoking with such nostalgic precision. The poem's detailed, loving evocation of Lithuanian-Polish gentry culture — the mushroom foraging, the hunting of bears, the preparations for a feast, the music of the last polonaise at the end — has made it a monument of Polish cultural memory, the text in which Polish identity was most completely embodied during the century and a half of partition (1795–1918) when Poland did not exist as an independent state.\n\nPan Tadeusz is the most widely read and most beloved work of Polish literature — memorised by generations of Polish schoolchildren, quoted in political speeches, invoked in wartime to sustain national identity — and its 1834 Paris publication made it one of the defining texts of Romantic nationalism. Mickiewicz wrote Pan Tadeusz in the context of the failure of the Polish November Uprising (1830–1831) against Russian rule, and the poem's complex relationship to political defeat — celebrating a community and a landscape that the poet cannot reach — gives it its characteristic emotional register of elegy and love.",
    "causes": [
      "The failure of the Polish November Uprising (1830–1831) against Russian rule — and Mickiewicz's subsequent emigration to Paris — created the immediate context of exile in which Pan Tadeusz was written, making the poem's nostalgic evocation of Lithuanian-Polish landscape and community a direct response to the political catastrophe of the uprising's suppression.",
      "The Polish Romantic tradition — of which Mickiewicz was the supreme figure — fused poetry with national identity in a way that made the poet a prophet and national spokesman, and Pan Tadeusz was written in this context as the definitive summation of Polish cultural identity in a period when Poland had no political existence.",
      "The historical moment of Napoleon's Russian campaign (1812) — which had briefly raised the hope of Polish restoration through French victory — provided the poem's historical setting, allowing Mickiewicz to evoke a moment of hope and community that readers in 1834 knew had ended in Napoleon's catastrophic defeat."
    ],
    "effects": [
      "Pan Tadeusz became the foundational text of Polish national identity during the partitions (1795–1918) — memorised by generations of Poles in exile and under foreign rule, quoted in political speeches, and invoked in wartime, the poem sustained Polish cultural identity during the century and a half when Poland had no political existence.",
      "Pan Tadeusz was translated into 43 languages and is the most translated work of Polish literature — its translations include major works in German (1836), French, English, and Russian, demonstrating its reach beyond the Polish linguistic community and its status as a work of world literary significance.",
      "Pan Tadeusz's influence on subsequent Polish literature — as the canonical model of the Polish epic, the touchstone of Polish cultural memory, and the definitive evocation of the lost Lithuanian-Polish landscape — makes it the primary reference point for Polish literary culture, comparable in its function to the Kalevala for Finland or the Nibelungenlied for Germany."
    ],
    "relationships": [
      {"sourceSlug": "adam-mickiewicz", "sourceName": "Adam Mickiewicz (1798–1855 — Polish Romantic poet; Paris exile; national prophet)", "verb": "AUTHORS", "targetSlug": "pan-tadeusz", "targetName": "Pan Tadeusz (1834 Paris — Polish national epic; Lithuania, my homeland; 12 books)", "context": "Mickiewicz wrote Pan Tadeusz in Parisian exile and published it in 1834 — the poem is the supreme work of Polish Romantic literature and the foundational text of Polish national identity."},
      {"sourceSlug": "pan-tadeusz", "sourceName": "Pan Tadeusz (November Uprising 1830–1831 — exile; Polish partition; political defeat context)", "verb": "RESPONDS_TO", "targetSlug": "november-uprising-1830", "targetName": "November Uprising (1830–1831 — Polish revolt against Russian rule; suppression; Mickiewicz's exile)", "context": "Pan Tadeusz was written in response to the failure of the November Uprising (1830–1831) — Mickiewicz's Parisian exile and the uprising's suppression shaped the poem's elegiac evocation of a lost Polish homeland."},
      {"sourceSlug": "pan-tadeusz", "sourceName": "Pan Tadeusz (Polish national identity — partitions 1795–1918; memorised; wartime invocation)", "verb": "SUSTAINS", "targetSlug": "polish-national-identity", "targetName": "Polish national identity (1795–1918 partitions — no Polish state; cultural memory; Mickiewicz)", "context": "Pan Tadeusz sustained Polish national identity during the century and a half of partition (1795–1918) — memorised by generations of Poles under foreign rule, the poem provided the cultural foundation for Polish identity in the absence of a Polish state."}
    ],
    "places": [
      {"name": "Paris, France (1834 — Polish exile community; November Uprising aftermath; Mickiewicz's composition)", "role": "Pan Tadeusz was written and published in Paris in 1834 — Mickiewicz was in exile following the failure of the November Uprising, and the poem's nostalgic evocation of Lithuania was written from the perspective of a man who knew he could never return"},
      {"name": "Lithuania / Poland (Soplicowo — 1811–1812 setting; gentry culture; Napoleonic hope; landscape elegy)", "role": "Pan Tadeusz is set in the Lithuanian countryside of 1811–1812 — evoking the landscape, rituals, and community of Polish-Lithuanian gentry culture with extraordinary nostalgic precision from the distance of Parisian exile"}
    ],
    "subjects": ["Polish Literature", "19th Century", "Adam Mickiewicz", "Epic Poetry", "Romantic Nationalism", "Polish Identity", "European Literature", "National Epics"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Pan Tadeusz (Mickiewicz, 1834) is the Polish national epic — the foundational text of Polish cultural identity during 123 years of partition (1795–1918) when Poland had no political existence. Written in Parisian exile after the failed November Uprising, it sustained Polish national consciousness through its nostalgic evocation of a lost Lithuanian-Polish landscape and community. Translated into 43 languages, it is the most translated work of Polish literature.",
      "significanceCategory": "world-changing"
    }
  }
}

}  # end ENRICHMENTS


def get_entity(filepath, slug):
    with open(filepath) as f:
        data = json.load(f)
    for e in data.get("entities", []):
        if e.get("slug") == slug:
            return e, data
    return None, data

def apply_enrichment(filepath, slug, enrichment_data, dry_run=False):
    entity, data = get_entity(filepath, slug)
    if entity is None:
        print(f"  ERROR: slug '{slug}' not found in {filepath}")
        return False
    raw = entity.get("detailsJson", "{}")
    details = raw if isinstance(raw, dict) else json.loads(raw or "{}")
    old_len = len(details.get("summary", "") or "")
    if old_len >= 800:
        print(f"  SKIP — already enriched ({old_len}c)")
        return False
    if dry_run:
        print(f"  DRY RUN — would enrich {old_len}c → {len(enrichment_data.get('summary',''))}c")
        return True
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for k, v in enrichment_data.items():
        details[k] = v
    edit_log = details.get("_editLog", [])
    edit_log.append({"field": "summary", "editorId": EDITOR_ID, "sessionId": SESSION_ID,
                     "timestamp": now, "oldValue": "", "newValue": enrichment_data.get("summary","")[:200] + "…"})
    details["_editLog"] = edit_log
    entity["detailsJson"] = details
    entity["_unsyncedEdits"] = True
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ENRICHED — {old_len}c → {len(enrichment_data.get('summary',''))}c")
    return True

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("** DRY RUN **\n")
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    enriched = skipped = errors = 0
    for slug, spec in ENRICHMENTS.items():
        fp = os.path.join(repo_root, spec["filepath"])
        print(f"\n[{slug}]")
        if not os.path.exists(fp):
            print(f"  ERROR: not found: {fp}")
            errors += 1
            continue
        ok = apply_enrichment(fp, slug, spec["data"], dry_run=dry_run)
        if ok: enriched += 1
        else: skipped += 1
    print(f"\n{'='*60}\nRESULTS: {enriched} enriched, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
