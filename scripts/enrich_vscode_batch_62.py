#!/usr/bin/env python3
"""
VS Code Enrichment Batch 62 — 8 Historical Persons
Adolf Hitler, Vladimir Lenin, Franklin D. Roosevelt, Mao Zedong,
Deng Xiaoping, Rosa Parks, Che Guevara, Guru Nanak

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-62-may2026
"""

import json
import os
import sys
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-62-may2026"
SKIP_THRESHOLD = 800


ENRICHMENTS = [
    # ── 1. Adolf Hitler ──────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222adolf-hitler.json",
        "slug": "adolf-hitler",
        "era_correction": None,
        "data": {
            "summary": (
                "Adolf Hitler (1889–1945) was the Austrian-born dictator of Nazi Germany (1933–1945) whose ideology of racial antisemitism and German expansionism led directly to World War II and the Holocaust — the systematic murder of six million Jews and five to six million other victims (Roma, disabled people, Slavs, political opponents, and LGBTQ+ individuals), representing the most industrialized genocide in history. He is the paradigmatic symbol of totalitarian evil in the 20th century.\n\n"
                "Hitler rose from a failed artist and World War I corporal to Chancellor of Germany in January 1933, exploiting the Weimar Republic's political instability, the trauma of the 1929 Great Depression, and the humiliation of the 1919 Versailles Treaty. As Führer he dismantled democratic institutions within months, rearmed Germany in violation of Versailles, annexed Austria and Czechoslovakia, and invaded Poland (September 1, 1939) — starting World War II. His Blitzkrieg campaigns conquered France, Norway, the Balkans, and drove into Soviet Russia.\n\n"
                "The Holocaust was systematically organized from 1941 with the establishment of extermination camps (Auschwitz, Treblinka, Sobibor, etc.) following the Wannsee Conference (January 1942). As the war turned against Germany after Stalingrad (1943) and D-Day (1944), Hitler refused surrender, ordering continued resistance until Berlin's fall. He died by suicide on April 30, 1945, with Soviet forces blocks from the Führerbunker.\n\n"
                "Hitler's name has become a universal reference point for absolute evil — his methods, ideology, and the Holocaust set the terms for all subsequent discussions of genocide, totalitarianism, and the dangers of extremist nationalism."
            ),
            "causes": [
                "Weimar Republic's instability and Great Depression (1929) creating mass unemployment and political crisis",
                "Versailles Treaty's humiliation of Germany fueling nationalist resentment",
                "Antisemitism and racial nationalism as tools for political mobilization",
                "WWI defeat and the 'stab-in-the-back' myth providing scapegoating narrative",
            ],
            "effects": [
                "World War II (1939–1945) — 70–85 million total deaths",
                "Holocaust — systematic murder of 6 million Jews and 5–6 million others",
                "Fall of Nazi Germany and partition of Europe between US and Soviet spheres",
                "Nuremberg Trials establishing international criminal law for crimes against humanity",
                "Creation of Israel (1948) as direct response to Holocaust",
                "Cold War — Soviet occupation of Eastern Europe resulting from WWII outcome",
                "United Nations and Universal Declaration of Human Rights (1948) as anti-totalitarian institutions",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Holocaust", "targetSlug": "holocaust", "note": "Ordered and directed the systematic genocide of 6 million Jews"},
                {"type": "INFLUENCES", "target": "World War II", "targetSlug": "world-war-ii", "note": "Initiated with Poland invasion (Sept 1, 1939)"},
                {"type": "INFLUENCES", "target": "Joseph Stalin", "targetSlug": "joseph-stalin", "note": "Molotov-Ribbentrop pact then war to the death; both totalitarians"},
                {"type": "INFLUENCES", "target": "Nuremberg Trials", "targetSlug": "nuremberg-trials", "note": "Posthumous judgment of Nazi crimes established international law"},
                {"type": "INFLUENCES", "target": "Mein Kampf", "targetSlug": "mein-kampf", "note": "His autobiographical manifesto outlining racial ideology (1925)"},
                {"type": "INFLUENCES", "target": "Wannsee Conference", "targetSlug": "wannsee-conference", "note": "1942 meeting coordinating the 'Final Solution'"},
                {"type": "INFLUENCES", "target": "Weimar Republic", "targetSlug": "weimar-republic", "note": "Democratic republic he destroyed from within"},
                {"type": "INFLUENCES", "target": "Benito Mussolini", "targetSlug": "benito-mussolini", "note": "Fascist ally and model; the 'Rome-Berlin Axis'"},
                {"type": "INFLUENCES", "target": "Winston Churchill", "targetSlug": "winston-churchill", "note": "Churchill's resistance defined Allied opposition to Hitler"},
                {"type": "INFLUENCES", "target": "Franklin D. Roosevelt", "targetSlug": "franklin-d-roosevelt", "note": "FDR's leadership against Nazi Germany"},
                {"type": "OCCURS_IN", "target": "Germany", "targetSlug": "germany", "note": "Chancellor and Führer of Germany 1933–1945"},
                {"type": "INFLUENCES", "target": "Creation of Israel", "targetSlug": "state-of-israel", "note": "Holocaust directly motivated international support for Jewish homeland"},
                {"type": "INFLUENCES", "target": "Battle of Stalingrad", "targetSlug": "battle-of-stalingrad", "note": "Turning point where German advance into USSR was halted"},
                {"type": "INFLUENCES", "target": "D-Day (Normandy)", "targetSlug": "d-day-normandy", "note": "Allied invasion opening Western Front; began Germany's final defeat"},
                {"type": "INFLUENCES", "target": "Auschwitz", "targetSlug": "auschwitz", "note": "Largest extermination camp; 1.1 million murdered"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Adolf Hitler caused World War II and the Holocaust — the most destructive war and the most industrial genocide in history — reshaping the entire world order, creating the Cold War, founding the United Nations, and making his name the universal shorthand for absolute political evil."
            },
            "quote": "'The great masses of the people will more easily fall victims to a big lie than to a small one.' — Adolf Hitler, Mein Kampf (1925)",
            "places": ["Berlin, Germany (capital)", "Braunau am Inn, Austria (birthplace)", "Munich, Germany (political base)", "Berchtesgaden, Germany (retreat)"],
            "subjectHeadings": "Adolf Hitler — Dictators and War Criminals — Germany — Modern",
            "subjects": ["Germany", "World War II", "Holocaust", "Nazism", "totalitarianism", "genocide", "antisemitism", "20th century", "fascism", "Europe"],
            "frameworks": ["totalitarianism", "nationalism", "genocide"],
        }
    },

    # ── 2. Vladimir Lenin ────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222vladimir-lenin.json",
        "slug": "vladimir-lenin",
        "era_correction": None,
        "data": {
            "summary": (
                "Vladimir Lenin (1870–1924) was the founder and leader of the Bolshevik Party who led the Russian Revolution of 1917, overthrew the Provisional Government in October, and created the Soviet state — establishing the world's first communist government and inspiring revolutionary movements on every continent for the next 70 years. His theoretical innovations in Marxist organization and his ruthless political pragmatism made him the 20th century's most consequential revolutionary.\n\n"
                "Lenin's core contribution to Marxist theory was the concept of the 'vanguard party': a highly disciplined professional revolutionary organization that would lead the working class to revolution rather than waiting for spontaneous mass action. His April Theses (1917) called for immediate Soviet power and peace; his October coup overthrew the Provisional Government with minimal resistance. He immediately signed the Treaty of Brest-Litovsk withdrawing Russia from WWI at enormous territorial cost, and launched the Red Terror (1918) — systematic political violence against class enemies.\n\n"
                "He survived an assassination attempt in 1918 (two bullets, one lodged near his spine) that he believed accelerated his death. His New Economic Policy (1921) made pragmatic concessions to capitalism to rebuild a devastated economy. He died in 1924, leaving a 'testament' warning against Stalin's 'coarseness' — advice the Party ignored.\n\n"
                "Lenin's embalmed body has lain in Red Square's mausoleum since 1924. His legacy: the Soviet Union, which collapsed in 1991; communist parties in China, Vietnam, Cuba, and Korea; and the template for single-party revolutionary states that shaped the 20th century's political geography."
            ),
            "causes": [
                "Marxist revolutionary theory providing framework for organized socialist politics",
                "WWI's catastrophic human cost delegitimizing tsarist government",
                "1905 Revolution and October 1917 political vacuum enabling Bolshevik seizure",
                "German military intelligence funding Lenin's return to Russia (April 1917)",
            ],
            "effects": [
                "Russian Revolution (October 1917) — world's first communist state",
                "Soviet Union (USSR) founded (1922) — global superpower until 1991",
                "Red Terror (1918) — systematic political violence establishing Soviet security state",
                "Comintern (1919) — international organization spreading communist revolution",
                "Treaty of Brest-Litovsk (1918) — Russian exit from WWI at huge cost",
                "Marxism-Leninism as the ideology of communist states globally",
                "Model for Mao, Ho Chi Minh, Castro, and all 20th-century communist leaders",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Russian Revolution (1917)", "targetSlug": "russian-revolution-1917", "note": "Led the October Revolution overthrowing Provisional Government"},
                {"type": "INFLUENCES", "target": "Joseph Stalin", "targetSlug": "joseph-stalin", "note": "Stalin succeeded Lenin and transformed his state into totalitarianism"},
                {"type": "INFLUENCES", "target": "Leon Trotsky", "targetSlug": "leon-trotsky", "note": "Revolutionary partner who led Red Army in Civil War"},
                {"type": "INFLUENCES", "target": "Karl Marx", "targetSlug": "karl-marx", "note": "Applied and adapted Marxist theory to Russian conditions"},
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Mao adopted Leninist vanguard party model for China"},
                {"type": "INFLUENCES", "target": "Soviet Union", "targetSlug": "soviet-union", "note": "Founder and first leader"},
                {"type": "INFLUENCES", "target": "Comintern", "targetSlug": "comintern", "note": "Founded to coordinate global communist revolution"},
                {"type": "INFLUENCES", "target": "What Is to Be Done? (1902)", "targetSlug": "what-is-to-be-done-lenin", "note": "Vanguard party theory — defining Leninist text"},
                {"type": "INFLUENCES", "target": "Bolshevik Party", "targetSlug": "bolshevik-party", "note": "Founded and led the party that seized power"},
                {"type": "OCCURS_IN", "target": "Russia", "targetSlug": "russia", "note": "Led Russian revolution and Soviet state"},
                {"type": "INFLUENCES", "target": "Treaty of Brest-Litovsk", "targetSlug": "treaty-of-brest-litovsk", "note": "Controversial peace with Germany withdrawing from WWI"},
                {"type": "INFLUENCES", "target": "Fidel Castro", "targetSlug": "fidel-castro", "note": "Cuban Revolution modeled on Leninist party organization"},
                {"type": "INFLUENCES", "target": "Ho Chi Minh", "targetSlug": "ho-chi-minh", "note": "Vietnamese communist leader inspired by Leninism"},
                {"type": "INFLUENCES", "target": "Nicholas II", "targetSlug": "nicholas-ii-of-russia", "note": "Last Tsar whose execution Lenin ordered (1918)"},
                {"type": "INFLUENCES", "target": "New Economic Policy", "targetSlug": "new-economic-policy", "note": "Pragmatic capitalism concessions (1921) saving Soviet economy"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Vladimir Lenin created the first communist state, founded the Soviet Union, and established the Leninist model of vanguard party revolution that shaped every communist movement of the 20th century — from Mao and Castro to Ho Chi Minh — making him arguably the most consequential revolutionary in history."
            },
            "quote": "'A lie told often enough becomes the truth.' — attributed to Vladimir Lenin",
            "places": ["Moscow, Russia (Soviet capital)", "Ulyanovsk (Simbirsk), Russia (birthplace)", "Zurich, Switzerland (exile)", "Petrograd (St Petersburg) (revolution)"],
            "subjectHeadings": "Vladimir Lenin — Revolutionary Leaders — Russia — Modern",
            "subjects": ["Russia", "Soviet Union", "communism", "revolution", "Marxism", "Bolshevism", "20th century", "Cold War", "political theory", "USSR"],
            "frameworks": ["revolution", "totalitarianism", "social-theory"],
        }
    },

    # ── 3. Franklin D. Roosevelt ─────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222franklin-d-roosevelt.json",
        "slug": "franklin-d-roosevelt",
        "era_correction": None,
        "data": {
            "summary": (
                "Franklin D. Roosevelt (1882–1945) was the 32nd President of the United States (1933–1945), the only American president elected to four terms, who led the country through its two greatest 20th-century crises: the Great Depression and World War II. Widely considered the greatest American president after Lincoln, FDR reshaped the relationship between citizens and government through the New Deal — creating the regulatory and social safety net that still defines American liberalism.\n\n"
                "When Roosevelt took office in March 1933, 25% of Americans were unemployed and the banking system was in collapse. His First Hundred Days launched the New Deal: the FDIC insuring bank deposits, the CCC providing work relief, the AAA reforming agriculture, the PWA building infrastructure, and (in 1935) the Social Security Act — the most consequential piece of domestic legislation in American history, still paying benefits to millions.\n\n"
                "Diagnosed with polio in 1921 at age 39, Roosevelt governed from a wheelchair — a disability he largely concealed from the public, demonstrating extraordinary physical and political resilience. His four-times-a-week 'fireside chats' on radio established direct communication with the American people that transformed presidential communication.\n\n"
                "As WWII commander-in-chief, he forged the Allied coalition (Churchill, Stalin), oversaw the Lend-Lease program supporting Britain, organized the D-Day invasion, and shaped the postwar order at Yalta — dying in Warm Springs, Georgia, on April 12, 1945, just weeks before Germany's surrender."
            ),
            "causes": [
                "Great Depression (1929) creating mass unemployment requiring government intervention",
                "Democratic political traditions enabling activist government through congressional majorities",
                "Polio diagnosis (1921) reshaping his empathy and political resilience",
                "Japanese attack on Pearl Harbor (December 7, 1941) forcing full US entry into WWII",
            ],
            "effects": [
                "New Deal (1933–39) — regulatory state, work relief, and social insurance",
                "Social Security Act (1935) — America's foundational social welfare program",
                "FDIC — federal deposit insurance preventing bank-run panics",
                "Allied coalition in WWII — Lend-Lease, D-Day, defeat of Nazi Germany",
                "United Nations framework designed at Yalta and Dumbarton Oaks",
                "Presidential fireside chats transforming mass political communication",
                "Modern American liberalism — government responsibility for economic welfare",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Winston Churchill", "targetSlug": "winston-churchill", "note": "Closest wartime partner; Atlantic Charter (1941)"},
                {"type": "INFLUENCES", "target": "Joseph Stalin", "targetSlug": "joseph-stalin", "note": "Allied with Stalin at Tehran and Yalta; granted Soviet sphere"},
                {"type": "INFLUENCES", "target": "New Deal", "targetSlug": "new-deal", "note": "His domestic program transforming American government"},
                {"type": "INFLUENCES", "target": "Social Security Act (1935)", "targetSlug": "social-security-act", "note": "Most consequential domestic legislation; still operative"},
                {"type": "INFLUENCES", "target": "Harry Truman", "targetSlug": "harry-truman", "note": "Succeeded FDR; dropped atomic bombs; launched Cold War"},
                {"type": "INFLUENCES", "target": "Eleanor Roosevelt", "targetSlug": "eleanor-roosevelt", "note": "Wife and political partner who advanced civil rights"},
                {"type": "INFLUENCES", "target": "Great Depression", "targetSlug": "great-depression", "note": "Economic catastrophe his New Deal addressed"},
                {"type": "INFLUENCES", "target": "D-Day (Normandy)", "targetSlug": "d-day-normandy", "note": "Oversaw largest amphibious operation in history"},
                {"type": "INFLUENCES", "target": "Pearl Harbor attack", "targetSlug": "pearl-harbor", "note": "'A date which will live in infamy' — US entry into WWII"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "32nd President — only 4-term president"},
                {"type": "INFLUENCES", "target": "Lend-Lease Act", "targetSlug": "lend-lease-act", "note": "Armed Britain and Soviet Union before US entry"},
                {"type": "INFLUENCES", "target": "Theodore Roosevelt", "targetSlug": "theodore-roosevelt", "note": "Distant cousin; both activist presidents"},
                {"type": "INFLUENCES", "target": "United Nations", "targetSlug": "united-nations", "note": "Coined 'United Nations' term; designed postwar order"},
                {"type": "INFLUENCES", "target": "Manhattan Project", "targetSlug": "manhattan-project", "note": "Authorized atomic bomb development (though Truman used it)"},
                {"type": "INFLUENCES", "target": "Japanese American internment", "targetSlug": "japanese-american-internment", "note": "His Executive Order 9066 interned 120,000 Japanese Americans — major civil rights failure"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Franklin D. Roosevelt rescued American democracy from the Great Depression with the New Deal, led the Allied coalition to victory in World War II, and shaped the entire postwar international order — governing through America's two greatest crises and defining American liberalism for generations."
            },
            "quote": "'The only thing we have to fear is fear itself.' — Franklin D. Roosevelt, First Inaugural Address (March 4, 1933)",
            "places": ["Washington D.C. (White House)", "Hyde Park, New York (home and burial)", "Warm Springs, Georgia (death)", "Yalta, Crimea (conference)"],
            "subjectHeadings": "Franklin D. Roosevelt — Presidents and Statesmen — United States — Modern",
            "subjects": ["United States", "New Deal", "World War II", "Great Depression", "presidency", "social security", "Allied coalition", "20th century", "liberalism", "Cold War origins"],
            "frameworks": ["state-formation", "social-theory", "military-history"],
        }
    },

    # ── 4. Mao Zedong ────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222mao-zedong.json",
        "slug": "mao-zedong",
        "era_correction": None,
        "data": {
            "summary": (
                "Mao Zedong (1893–1976) was the founding chairman of the People's Republic of China (1949–1976), whose communist revolution ended a century of humiliation and civil war — but whose subsequent campaigns, the Great Leap Forward (1958–62) and the Cultural Revolution (1966–76), caused the deaths of an estimated 45–55 million people through famine, violence, and political persecution, making him responsible for more peacetime deaths than any other ruler in history.\n\n"
                "Mao's Long March (1934–35) — a 6,000-mile strategic retreat that became Communist legend — established his leadership of the Chinese Communist Party. After defeating Chiang Kai-shek's Nationalists (1949), he proclaimed the People's Republic from Tiananmen. His land reform (1950–52) redistributed land to 300 million peasants while executing an estimated 1–2 million landlords.\n\n"
                "The Great Leap Forward attempted to rapidly industrialize China through mass mobilization, abolishing private farming and launching backyard steel production — resulting in the worst famine in human history (30–45 million dead, 1959–61). The Cultural Revolution (1966–76) was a decade-long purge of intellectuals, teachers, party officials, and 'capitalist roaders' that destroyed cultural heritage, closed universities, and sent millions to labor camps.\n\n"
                "Mao's diplomatic opening to Nixon (1972) — the most dramatic Cold War realignment — demonstrated his willingness to abandon ideology for strategic advantage. His legacy is China's continued single-party rule, his portrait on Tiananmen Square, and the paradox of being revered by the government of a capitalist power while responsible for history's deadliest peacetime famine."
            ),
            "causes": [
                "Century of Humiliation — foreign invasions, Opium Wars, Japanese occupation",
                "Chinese Civil War between Communists and Kuomintang (1927–1949)",
                "Marxism-Leninism adapted to agrarian peasant society by Mao Zedong Thought",
                "Stalin's support and Soviet model providing template for communist state",
            ],
            "effects": [
                "People's Republic of China proclaimed October 1, 1949",
                "Land reform redistributing land to 300 million peasants; 1–2 million landlords killed",
                "Great Leap Forward famine (1959–61): 30–45 million dead",
                "Cultural Revolution (1966–76): destruction of cultural heritage, millions persecuted",
                "Korean War — Chinese intervention saving North Korea (1950)",
                "Nixon-Mao diplomatic opening (1972) — Cold War realignment",
                "Mao Zedong Thought as foundation of PRC's one-party system to this day",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "People's Republic of China", "targetSlug": "peoples-republic-of-china", "note": "Founder and first chairman"},
                {"type": "INFLUENCES", "target": "Chinese Communist Party", "targetSlug": "chinese-communist-party", "note": "Led from Long March to final victory"},
                {"type": "INFLUENCES", "target": "Chiang Kai-shek", "targetSlug": "chiang-kai-shek", "note": "Defeated in Civil War; Chiang retreated to Taiwan"},
                {"type": "INFLUENCES", "target": "Great Leap Forward", "targetSlug": "great-leap-forward", "note": "Industrialization campaign causing 30–45 million deaths (1959–61)"},
                {"type": "INFLUENCES", "target": "Cultural Revolution", "targetSlug": "cultural-revolution", "note": "Decade-long political purge destroying culture (1966–76)"},
                {"type": "INFLUENCES", "target": "Joseph Stalin", "targetSlug": "joseph-stalin", "note": "Soviet patron who funded and trained CCP"},
                {"type": "INFLUENCES", "target": "Deng Xiaoping", "targetSlug": "deng-xiaoping", "note": "Successor who reversed Mao's economic policies"},
                {"type": "INFLUENCES", "target": "Vladimir Lenin", "targetSlug": "vladimir-lenin", "note": "Leninist vanguard party model adapted to China"},
                {"type": "INFLUENCES", "target": "Richard Nixon", "targetSlug": "richard-nixon", "note": "1972 diplomatic opening — most dramatic Cold War realignment"},
                {"type": "INFLUENCES", "target": "Korean War", "targetSlug": "korean-war", "note": "Chinese intervention (1950) saving North Korea from UN forces"},
                {"type": "OCCURS_IN", "target": "China", "targetSlug": "china", "note": "Chairman of People's Republic of China"},
                {"type": "INFLUENCES", "target": "Long March (1934–35)", "targetSlug": "long-march", "note": "6,000-mile retreat establishing Mao's leadership"},
                {"type": "INFLUENCES", "target": "Ho Chi Minh", "targetSlug": "ho-chi-minh", "note": "Allied Vietnamese communist leader"},
                {"type": "INFLUENCES", "target": "Zhou Enlai", "targetSlug": "zhou-enlai", "note": "Premier and closest associate throughout Mao's rule"},
                {"type": "INFLUENCES", "target": "Little Red Book", "targetSlug": "little-red-book", "note": "Quotations from Chairman Mao — most printed book of the 1960s"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Mao Zedong unified China after a century of humiliation, founded the People's Republic, and established the single-party system that governs the world's most populous nation — while the Great Leap Forward and Cultural Revolution caused an estimated 45–55 million deaths, making his legacy history's most paradoxical combination of national achievement and mass atrocity."
            },
            "quote": "'Political power grows out of the barrel of a gun.' — Mao Zedong (1938)",
            "places": ["Beijing (Peking), China (capital)", "Shaoshan, Hunan (birthplace)", "Yan'an, Shaanxi (Long March terminus)", "Tiananmen Square (proclamation site)"],
            "subjectHeadings": "Mao Zedong — Revolutionary Leaders and Dictators — China — Contemporary",
            "subjects": ["China", "communism", "revolution", "Cultural Revolution", "Great Leap Forward", "Cold War", "20th century", "Marxism", "famine", "Asia"],
            "frameworks": ["revolution", "totalitarianism", "empire-building"],
        }
    },

    # ── 5. Deng Xiaoping ─────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/222-Class-222/222deng-xiaoping.json",
        "slug": "deng-xiaoping",
        "era_correction": None,
        "data": {
            "summary": (
                "Deng Xiaoping (1904–1997) was China's paramount leader from 1978 to 1989 (formally) and the architect of China's economic reform — the man who transformed a Maoist command economy into the world's largest trading nation through 'Reform and Opening Up' (改革开放), generating the fastest large-scale economic growth in human history. His pragmatism — 'It doesn't matter if a cat is black or white, so long as it catches mice' — reversed 30 years of communist orthodoxy.\n\n"
                "Twice purged by Mao during the Cultural Revolution, Deng returned to power after Mao's death (1976) and outmaneuvered the 'Gang of Four' to become China's dominant leader by 1978. His reforms: agricultural decollectivization giving peasants incentive to produce (1978–84); Special Economic Zones (Shenzhen, 1979) allowing foreign investment; TVE (Township and Village Enterprise) growth; and progressive opening to global trade. Between 1979 and 2012, China's economy grew at ~10% annually — lifting 800 million people out of poverty, the largest poverty reduction in history.\n\n"
                "His reputation is permanently shadowed by the Tiananmen Square massacre (June 4, 1989), in which he ordered the military suppression of pro-democracy protests, killing hundreds to thousands of students and civilians. He reportedly said: 'If we had to shed blood, we had to shed blood.'\n\n"
                "Deng left China as the world's largest manufacturer and exporter, established the 'one country, two systems' framework for Hong Kong, and created the political-economic model — authoritarian capitalism — that defines the 21st century's major challenge to liberal democracy."
            ),
            "causes": [
                "Mao's death (1976) and Cultural Revolution's economic devastation requiring reform",
                "Deng's pragmatic pragmatism versus Maoist ideological orthodoxy",
                "Asian Tiger development models (Taiwan, South Korea) demonstrating export-led growth",
                "US-China normalization (1979) opening Western markets to Chinese exports",
            ],
            "effects": [
                "China's GDP grew ~10%/year 1979–2012 — fastest large-scale growth in history",
                "800 million people lifted out of poverty — largest poverty reduction in history",
                "Shenzhen Special Economic Zone — template for global manufacturing hub",
                "World Trade Organization membership (2001) integrating China in global economy",
                "Tiananmen Square massacre (1989) — democracy movement suppressed",
                "'One country, two systems' — framework for Hong Kong handover (1997)",
                "Authoritarian capitalism model — China as 21st-century challenge to liberal democracy",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Purged twice by Mao; reversed his economic policies"},
                {"type": "INFLUENCES", "target": "China's economic reform", "targetSlug": "chinese-economic-reform", "note": "Architect of Reform and Opening Up (1978)"},
                {"type": "INFLUENCES", "target": "Tiananmen Square massacre", "targetSlug": "tiananmen-square-massacre", "note": "Ordered military suppression of 1989 democracy movement"},
                {"type": "INFLUENCES", "target": "Shenzhen", "targetSlug": "shenzhen", "note": "First Special Economic Zone — prototype of China's manufacturing"},
                {"type": "INFLUENCES", "target": "Jiang Zemin", "targetSlug": "jiang-zemin", "note": "Chosen successor after Tiananmen"},
                {"type": "INFLUENCES", "target": "Jimmy Carter", "targetSlug": "jimmy-carter", "note": "US-China normalization (1979) under Carter"},
                {"type": "INFLUENCES", "target": "Hong Kong", "targetSlug": "hong-kong", "note": "Negotiated 'one country, two systems' with UK"},
                {"type": "INFLUENCES", "target": "Margaret Thatcher", "targetSlug": "margaret-thatcher", "note": "Negotiated Hong Kong handover (1997) with Britain"},
                {"type": "INFLUENCES", "target": "People's Republic of China", "targetSlug": "peoples-republic-of-china", "note": "Paramount leader who redefined China's development path"},
                {"type": "INFLUENCES", "target": "Gang of Four", "targetSlug": "gang-of-four", "note": "Arrested after Mao's death; Deng outmaneuvered them"},
                {"type": "OCCURS_IN", "target": "China", "targetSlug": "china", "note": "Chinese paramount leader 1978–1997"},
                {"type": "INFLUENCES", "target": "Xi Jinping", "targetSlug": "xi-jinping", "note": "Current leader who built on Deng's economic base"},
                {"type": "INFLUENCES", "target": "Asian financial systems", "targetSlug": "asian-financial-development", "note": "China's model influenced development economics globally"},
                {"type": "INFLUENCES", "target": "World Trade Organization", "targetSlug": "world-trade-organization", "note": "China joined WTO 2001 under Deng's reform trajectory"},
                {"type": "INFLUENCES", "target": "Zhao Ziyang", "targetSlug": "zhao-ziyang", "note": "Liberal Party Secretary Deng removed after Tiananmen"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Deng Xiaoping's economic reforms lifted 800 million people out of poverty, transformed China into the world's largest manufacturer and trading nation, and created the authoritarian-capitalist model that defines the 21st century's central geopolitical challenge — making him the most consequential economic policy-maker of the modern era."
            },
            "quote": "'It doesn't matter if a cat is black or white, so long as it catches mice.' — Deng Xiaoping",
            "places": ["Beijing, China (capital)", "Guang'an, Sichuan (birthplace)", "Shenzhen, China (SEZ symbol)"],
            "subjectHeadings": "Deng Xiaoping — Leaders and Reformers — China — Contemporary",
            "subjects": ["China", "economic reform", "communism", "capitalism", "Tiananmen", "Cold War", "poverty reduction", "20th century", "geopolitics", "Asia"],
            "frameworks": ["economic-history", "state-formation", "totalitarianism"],
        }
    },

    # ── 6. Rosa Parks ────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/270-Class-270/270rosa-parks.json",
        "slug": "rosa-parks",
        "era_correction": None,
        "data": {
            "summary": (
                "Rosa Parks (1913–2005) was an African American civil rights activist whose arrest on December 1, 1955, for refusing to give up her seat to a white passenger on a Montgomery, Alabama, bus triggered the Montgomery Bus Boycott — a 381-day mass economic protest that became the first major victory of the American civil rights movement and launched Martin Luther King Jr. as its national leader.\n\n"
                "Parks was not, as legend sometimes portrays, a tired seamstress who spontaneously refused to move. She was a trained NAACP activist who had attended the Highlander Folk School, was experienced in civil rights organizing, and was deliberately chosen as the test case for a legal challenge to bus segregation. Her composure, dignity, and unimpeachable respectability made her the ideal plaintiff.\n\n"
                "The Montgomery Bus Boycott (December 5, 1955 – December 20, 1956) organized 40,000 Black Montgomery residents to walk, carpool, or use taxis for 381 days rather than ride segregated buses — costing the transit system 65% of its revenue. The Supreme Court ultimately ruled (Browder v. Gayle, 1956) that bus segregation was unconstitutional. The boycott demonstrated that nonviolent economic pressure could achieve civil rights victories and established King as the movement's leader.\n\n"
                "Parks was fired from her seamstress job and received death threats; she relocated to Detroit in 1957. President Clinton awarded her the Presidential Medal of Freedom (1996) and the Congressional Gold Medal (1999). She died in 2005 at 92; her body lay in honor at the Capitol Rotunda."
            ),
            "causes": [
                "Montgomery bus segregation laws requiring Black passengers to yield seats to whites",
                "NAACP civil rights organizing network seeking a test case for legal challenge",
                "Highlander Folk School training Parks in civil rights strategy",
                "History of Black women's resistance to bus segregation (Claudette Colvin, others)",
            ],
            "effects": [
                "Montgomery Bus Boycott (1955–56) — 381 days of mass nonviolent economic protest",
                "Browder v. Gayle (1956) — Supreme Court ruling bus segregation unconstitutional",
                "Martin Luther King Jr. elevated to national civil rights leadership",
                "Template for nonviolent economic protest in civil rights movement",
                "Civil Rights Act (1964) and Voting Rights Act (1965) — downstream outcomes",
                "Congressional Gold Medal (1999) — highest US civilian honor",
                "Icon of ordinary courage — the power of individual nonviolent resistance",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Martin Luther King Jr.", "targetSlug": "martin-luther-king-jr", "note": "Her arrest and boycott launched King as national leader"},
                {"type": "INFLUENCES", "target": "Montgomery Bus Boycott", "targetSlug": "montgomery-bus-boycott", "note": "Her arrest triggered the 381-day boycott she inspired"},
                {"type": "INFLUENCES", "target": "NAACP", "targetSlug": "naacp", "note": "NAACP organizer who was deliberately chosen as test case"},
                {"type": "INFLUENCES", "target": "Civil Rights Act (1964)", "targetSlug": "civil-rights-act-1964", "note": "Downstream legislative achievement of the movement she triggered"},
                {"type": "INFLUENCES", "target": "Browder v. Gayle", "targetSlug": "browder-v-gayle", "note": "Supreme Court case ruling bus segregation unconstitutional (1956)"},
                {"type": "INFLUENCES", "target": "Highlander Folk School", "targetSlug": "highlander-folk-school", "note": "Attended training school for civil rights activists"},
                {"type": "INFLUENCES", "target": "Frederick Douglass", "targetSlug": "frederick-douglass", "note": "Part of the long African American freedom struggle he pioneered"},
                {"type": "INFLUENCES", "target": "Claudette Colvin", "targetSlug": "claudette-colvin", "note": "15-year-old who refused to move on bus nine months before Parks"},
                {"type": "OCCURS_IN", "target": "United States", "targetSlug": "united-states", "note": "African American Alabaman; later Detroit resident"},
                {"type": "INFLUENCES", "target": "Jim Crow laws", "targetSlug": "jim-crow-laws", "note": "Segregation system her act began dismantling"},
                {"type": "INFLUENCES", "target": "Nonviolent resistance", "targetSlug": "nonviolent-resistance", "note": "Her arrest demonstrated power of peaceful refusal"},
                {"type": "INFLUENCES", "target": "Voting Rights Act (1965)", "targetSlug": "voting-rights-act-1965", "note": "Her boycott contributed to momentum for voting rights"},
                {"type": "INFLUENCES", "target": "John Lewis", "targetSlug": "john-lewis", "note": "Fellow civil rights movement leader who honored her legacy"},
                {"type": "INFLUENCES", "target": "Barack Obama", "targetSlug": "barack-obama", "note": "Obama's election partly traced to civil rights movement Parks ignited"},
                {"type": "INFLUENCES", "target": "Coretta Scott King", "targetSlug": "coretta-scott-king", "note": "Fellow Montgomery activist; wife of Martin Luther King Jr."},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Rosa Parks' refusal to give up her bus seat triggered the Montgomery Bus Boycott, the first major victory of the American civil rights movement, launched Martin Luther King Jr. as its leader, and demonstrated that nonviolent mass economic protest could dismantle legal racial segregation."
            },
            "quote": "'I would like to be remembered as a person who wanted to be free... so other people would also be free.' — Rosa Parks",
            "places": ["Montgomery, Alabama (arrest and boycott)", "Tuskegee, Alabama (birthplace)", "Detroit, Michigan (later home)"],
            "subjectHeadings": "Rosa Parks — Civil Rights Activists — United States — Contemporary",
            "subjects": ["United States", "civil rights", "African American history", "segregation", "Montgomery", "nonviolent resistance", "NAACP", "20th century", "Alabama", "Jim Crow"],
            "frameworks": ["liberation-theology", "human-rights", "social-revolution"],
        }
    },

    # ── 7. Che Guevara ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/270-Class-270/270che-guevara.json",
        "slug": "che-guevara",
        "era_correction": None,
        "data": {
            "summary": (
                "Ernesto 'Che' Guevara (1928–1967) was an Argentine-born Marxist revolutionary, guerrilla leader, and physician who played a central role in the Cuban Revolution (1956–59) alongside Fidel Castro — then spent the rest of his life attempting to export guerrilla revolution to Congo and Bolivia, where he was captured and executed by Bolivian forces with CIA assistance on October 9, 1967. His iconic photograph by Alberto Korda (1960) became the most reproduced image in photography history, making his face the universal symbol of revolutionary anti-imperialism.\n\n"
                "Guevara's transformation from bourgeois Argentine medical student to global revolutionary began with the Motorcycle Diaries journey (1952) — a 8,000-mile Latin American odyssey that confronted him with poverty, indigenous displacement, and US corporate exploitation. He joined Castro in Mexico (1955) and proved a brilliant guerrilla commander in Cuba, leading the Battle of Santa Clara that sealed Batista's defeat.\n\n"
                "As Cuba's Minister of Industries (1961–65) and head of the National Bank, he attempted rapid industrialization — largely a failure — before departing to lead guerrilla campaigns in Congo (1965, also unsuccessful) and Bolivia (1966–67). His 'foco' theory of guerrilla warfare — that a small armed group could create the conditions for revolution rather than waiting for political conditions to mature — proved tactically flawed but intellectually influential.\n\n"
                "Guevara's legacy is paradoxical: the revolutionary icon who appears on student T-shirts globally was also a commander who ordered executions and endorsed Stalinist economic methods. He remains history's most romanticized revolutionary."
            ),
            "causes": [
                "Motorcycle Diaries journey (1952) exposing Latin American poverty and US exploitation",
                "US-backed overthrow of Guatemalan democracy (1954) radicalizing his anti-imperialism",
                "Meeting Fidel Castro in Mexico (1955) channeling his revolutionary commitment",
                "Cuban popular support for armed resistance against Batista's dictatorship",
            ],
            "effects": [
                "Cuban Revolution success (1959) — Batista overthrown, socialist state established",
                "Battle of Santa Clara (1958) — his decisive guerrilla victory",
                "Guerrilla Warfare (1961) — manual on foco theory influencing revolutionaries worldwide",
                "Korda photograph — most reproduced image in history",
                "Execution in Bolivia (1967) — martyrdom cementing revolutionary mythology",
                "Inspiration for armed leftist movements: Tupamaros, FARC, Red Brigades, etc.",
                "Icon of anti-imperialism in global popular culture",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Fidel Castro", "targetSlug": "fidel-castro", "note": "Revolutionary partner; Che was second-in-command of Cuban Revolution"},
                {"type": "INFLUENCES", "target": "Cuban Revolution", "targetSlug": "cuban-revolution", "note": "Central commander; Battle of Santa Clara was his greatest victory"},
                {"type": "INFLUENCES", "target": "Battle of Santa Clara (1958)", "targetSlug": "battle-of-santa-clara", "note": "Decisive guerrilla victory sealing Batista's defeat"},
                {"type": "INFLUENCES", "target": "Raul Castro", "targetSlug": "raul-castro", "note": "Fellow Cuban revolutionary commander"},
                {"type": "INFLUENCES", "target": "Guerrilla Warfare (book, 1961)", "targetSlug": "guerrilla-warfare-guevara", "note": "His manual on foco theory"},
                {"type": "INFLUENCES", "target": "Motorcycle Diaries", "targetSlug": "motorcycle-diaries", "note": "Journey documenting his political awakening"},
                {"type": "INFLUENCES", "target": "Alberto Korda", "targetSlug": "alberto-korda", "note": "Photographer of the iconic 1960 portrait"},
                {"type": "INFLUENCES", "target": "Fulgencio Batista", "targetSlug": "fulgencio-batista", "note": "Cuban dictator overthrown by the revolution"},
                {"type": "INFLUENCES", "target": "FARC (Colombia)", "targetSlug": "farc", "note": "Colombian guerrilla group inspired by Che's theory"},
                {"type": "OCCURS_IN", "target": "Cuba", "targetSlug": "cuba", "note": "Led Cuban Revolution; Minister of Industries 1961–65"},
                {"type": "OCCURS_IN", "target": "Bolivia", "targetSlug": "bolivia", "note": "Captured and executed in La Higuera (1967)"},
                {"type": "INFLUENCES", "target": "CIA", "targetSlug": "central-intelligence-agency", "note": "CIA assisted Bolivian forces who captured and executed him"},
                {"type": "INFLUENCES", "target": "Mao Zedong", "targetSlug": "mao-zedong", "note": "Adapted Maoist guerrilla theory to Latin American conditions"},
                {"type": "INFLUENCES", "target": "Jacobo Árbenz", "targetSlug": "jacobo-arbenz", "note": "Guatemalan president whose CIA-backed overthrow radicalized Guevara"},
                {"type": "INFLUENCES", "target": "Vladimir Lenin", "targetSlug": "vladimir-lenin", "note": "Leninist vanguard model inspired Guevara's revolutionary theory"},
            ],
            "historicalSignificance": {
                "significanceScore": 8,
                "significanceCategory": "continental",
                "significanceNarrative": "Che Guevara's military leadership was critical to the Cuban Revolution, his guerrilla warfare theory influenced revolutionary movements on three continents, and his martyrdom and Korda photograph made him the most iconic symbol of revolutionary anti-imperialism in history — the paradox of an idealist who ordered executions."
            },
            "quote": "'Hasta la victoria siempre.' (Ever onward to victory.) — Che Guevara",
            "places": ["Santa Clara, Cuba (Battle of Santa Clara)", "Rosario, Argentina (birthplace)", "Havana, Cuba (Minister of Industries)", "La Higuera, Bolivia (execution site)"],
            "subjectHeadings": "Che Guevara — Revolutionaries — Argentina/Cuba — Contemporary",
            "subjects": ["Cuba", "Argentina", "revolution", "guerrilla warfare", "Cold War", "communism", "Latin America", "anti-imperialism", "20th century", "Bolivia"],
            "frameworks": ["revolution", "liberation-theology", "social-theory"],
        }
    },

    # ── 8. Guru Nanak ────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/204-Class-204/204guru-nanak.json",
        "slug": "guru-nanak",
        "era_correction": None,
        "data": {
            "summary": (
                "Guru Nanak (1469–1539) was the founder of Sikhism, born in Nankana Sahib (modern Pakistan) into a Hindu Khatri family, who proclaimed a radically egalitarian spiritual message: that there is one God (Ik Onkar), that all human beings are equal before God regardless of caste, gender, or religion, and that devotion, honest work, and sharing with others (Naam Japna, Kirat Karni, Vand Chhakna) constitute the path to liberation. His teachings became the foundation of the world's fifth-largest religion, with 25–30 million adherents.\n\n"
                "At age 30, Nanak underwent a transformative experience — emerging from the Vein River after three days, saying 'There is no Hindu, there is no Muslim' — which he spent the next 24 years making reality through four great Udasees (journeys) covering an estimated 28,000 km across India, the Middle East, Persia, and Mesopotamia, engaging in dialogue with Hindu saints, Muslim Sufis, Buddhist monks, and Jain ascetics.\n\n"
                "His hymns, collected in the Adi Granth (later Guru Granth Sahib), combine devotional poetry with philosophical depth in the Punjabi language. The langar (free community kitchen), which he institutionalized at Kartarpur, became Sikhism's defining symbol of radical equality — people of all castes eating together seated on the floor, still practiced in every gurdwara worldwide.\n\n"
                "Nanak's message of human equality and devotion to a formless God represented a profound challenge to both the caste system and religious orthodoxy — establishing a tradition that has produced some of history's bravest defenders of religious freedom."
            ),
            "causes": [
                "Hindu caste system and its exclusion of lower-caste people from spiritual equality",
                "Bhakti movement's devotional mysticism providing context for Nanak's experience",
                "Islamic Sufism's influence on North Indian religious culture",
                "Transformative spiritual experience in Vein River (c. 1499) that catalyzed his mission",
            ],
            "effects": [
                "Sikhism — world's fifth-largest religion, 25–30 million adherents",
                "Guru Granth Sahib — eternal living Guru and sacred scripture",
                "Langar (free community kitchen) — institutionalized radical equality",
                "Nine successor Gurus continuing and developing his spiritual lineage",
                "Khalsa (community of initiated Sikhs) founded by Guru Gobind Singh",
                "Kartarpur Corridor (2019) — modern India-Pakistan diplomatic project honoring Nanak",
                "Sikh diaspora in UK, Canada, USA — global community maintaining tradition",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Guru Granth Sahib", "targetSlug": "guru-granth-sahib", "note": "Sacred scripture containing his hymns — the eternal Guru"},
                {"type": "INFLUENCES", "target": "Sikhism", "targetSlug": "sikhism", "note": "Founder of the world's fifth-largest religion"},
                {"type": "INFLUENCES", "target": "Guru Angad", "targetSlug": "guru-angad", "note": "His chosen successor — second Sikh Guru"},
                {"type": "INFLUENCES", "target": "Mardana", "targetSlug": "mardana", "note": "Muslim companion and musician on all four Udasees"},
                {"type": "INFLUENCES", "target": "Kabir", "targetSlug": "kabir", "note": "Contemporary Sant poet whose traditions overlapped with Nanak's"},
                {"type": "INFLUENCES", "target": "Bhakti movement", "targetSlug": "bhakti-movement", "note": "North Indian devotional tradition Nanak developed"},
                {"type": "INFLUENCES", "target": "Guru Gobind Singh", "targetSlug": "guru-gobind-singh", "note": "Tenth Guru who founded the Khalsa and closed the lineage"},
                {"type": "INFLUENCES", "target": "Kartarpur", "targetSlug": "kartarpur", "note": "Community he founded — site of first Sikh congregation"},
                {"type": "INFLUENCES", "target": "Caste system", "targetSlug": "caste-system", "note": "He rejected caste as spiritually irrelevant — radical challenge"},
                {"type": "INFLUENCES", "target": "Islam", "targetSlug": "islam", "note": "Engaged deeply with Muslim Sufis; synthesized Hindu-Islamic insights"},
                {"type": "OCCURS_IN", "target": "India", "targetSlug": "india", "note": "Born and active in Punjab — Northwest India/Pakistan"},
                {"type": "OCCURS_IN", "target": "Pakistan", "targetSlug": "pakistan", "note": "Born in Nankana Sahib (modern Pakistan)"},
                {"type": "INFLUENCES", "target": "Langar (community kitchen)", "targetSlug": "langar", "note": "Free meal served to all — radical equality institutionalized"},
                {"type": "INFLUENCES", "target": "Golden Temple (Harmandir Sahib)", "targetSlug": "golden-temple", "note": "Sikh holiest site built on ground Nanak sanctified"},
                {"type": "INFLUENCES", "target": "Hinduism", "targetSlug": "hinduism", "note": "Born Hindu; transcended and critiqued orthodox caste practice"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Guru Nanak founded Sikhism — the world's fifth-largest religion — on radical principles of human equality, one God, and community service that challenged both caste hierarchy and religious orthodoxy, establishing a tradition of 25–30 million people globally who have historically defended religious freedom with extraordinary courage."
            },
            "quote": "'There is no Hindu, there is no Muslim.' — Guru Nanak (upon emerging from the Vein River, c. 1499)",
            "places": ["Nankana Sahib, Pakistan (birthplace)", "Kartarpur, Pakistan (community founded)", "Sultanpur Lodhi, India (early career)"],
            "subjectHeadings": "Guru Nanak — Religious Founders — India/Pakistan — Medieval",
            "subjects": ["India", "Pakistan", "Sikhism", "religion", "Bhakti movement", "Punjab", "spirituality", "equality", "Medieval era", "16th century"],
            "frameworks": ["religious-thought", "liberation-theology", "cultural-exchange"],
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

    print(f"Batch 62 enrichment — {len(ENRICHMENTS)} entities\n")

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
