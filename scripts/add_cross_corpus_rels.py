"""Add cross-corpus relationships to entities with empty relationships arrays."""
import re

# File → list of (entity_slug, new_relationships_to_add)
UPDATES = {
    'ui/src/data/catalog/corpuses/mesopotamian.ts': {
        'enuma_elish': [
            "{ sourceSlug: 'enuma_elish', sourceName: 'Enūma Eliš', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Creation narrative parallels — cosmos from watery chaos, structured creation sequence' }",
        ],
        'atrahasis_epic': [
            "{ sourceSlug: 'atrahasis_epic', sourceName: 'Atra-Ḫasīs', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Flood narrative parallel predating Gilgamesh version; creation-of-humanity theme' }",
        ],
        'nebuchadnezzar_ii': [
            "{ sourceSlug: 'nebuchadnezzar_ii', sourceName: 'Nebuchadnezzar II', verb: 'CAUSES', targetSlug: 'babylonian_exile', targetName: 'Babylonian Exile', context: 'Destroys First Temple 586 BCE; deports Judean elite to Babylon' }",
        ],
        'flood_tablet_gilgamesh_xi': [
            "{ sourceSlug: 'flood_tablet_gilgamesh_xi', sourceName: 'Flood Tablet (Gilgamesh XI)', verb: 'FRAMES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Physical evidence demonstrating Mesopotamian flood parallel to Genesis 6–9' }",
        ],
        'nineveh': [
            "{ sourceSlug: 'library_of_nineveh', sourceName: 'Library of Nineveh', verb: 'OCCURS_IN', targetSlug: 'nineveh', targetName: 'Nineveh', context: 'Ashurbanipal\\'s royal library located in Nineveh' }",
        ],
        'babylon_city': [
            "{ sourceSlug: 'nebuchadnezzar_ii', sourceName: 'Nebuchadnezzar II', verb: 'RULES', targetSlug: 'babylon_city', targetName: 'Babylon', context: 'Neo-Babylonian Empire capital under Nebuchadnezzar II' }",
        ],
        'sargon_of_akkad': [
            "{ sourceSlug: 'sargon_of_akkad', sourceName: 'Sargon of Akkad', verb: 'FOUNDS', targetSlug: 'edubba_scribal_schools', targetName: 'Edubba Scribal Schools', context: 'Akkadian empire spread cuneiform literacy through scribal institutions' }",
        ],
        'uruk_city': [
            "{ sourceSlug: 'gilgamesh', sourceName: 'Gilgamesh', verb: 'RULES', targetSlug: 'uruk_city', targetName: 'Uruk', context: 'Legendary king of Uruk; city walls attributed to him' }",
        ],
        'cuneiform_writing': [
            "{ sourceSlug: 'cuneiform_writing', sourceName: 'Cuneiform Writing', verb: 'ENABLES', targetSlug: 'mesopotamian_corpus', targetName: 'Mesopotamian Corpus', context: 'Cuneiform script preserved all major Mesopotamian literary traditions' }",
        ],
    },
    'ui/src/data/catalog/corpuses/graecoRoman.ts': {
        'iliad': [
            "{ sourceSlug: 'homer_poet', sourceName: 'Homer', verb: 'AUTHORS', targetSlug: 'iliad', targetName: 'Iliad', context: 'Attributed author of the foundational Greek epic' }",
        ],
        'library_of_alexandria': [
            "{ sourceSlug: 'library_of_alexandria', sourceName: 'Library of Alexandria', verb: 'TRANSMITS', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Septuagint Greek Old Testament produced under Ptolemaic patronage c. 250 BCE' }",
            "{ sourceSlug: 'library_of_alexandria', sourceName: 'Library of Alexandria', verb: 'OCCURS_IN', targetSlug: 'alexandria_city', targetName: 'Alexandria', context: 'Located in Ptolemaic Alexandria; largest ancient library' }",
        ],
        'histories_herodotus': [
            "{ sourceSlug: 'histories_herodotus', sourceName: 'Histories (Herodotus)', verb: 'DESCRIBES', targetSlug: 'babylon_city', targetName: 'Babylon', context: 'Herodotus Book I provides detailed ethnographic account of Babylon' }",
        ],
        'athens_city': [
            "{ sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Academy in Athens c. 387 BCE' }",
            "{ sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Lyceum in Athens c. 335 BCE' }",
        ],
        'rome_city': [
            "{ sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'OCCURS_IN', targetSlug: 'rome_city', targetName: 'Rome', context: 'Codification of Roman law under Justinian, compiled in Constantinople' }",
        ],
        'the_republic_plato': [
            "{ sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'AUTHORS', targetSlug: 'the_republic_plato', targetName: 'The Republic', context: 'Plato\\'s masterwork on justice, ideal governance, and the Form of the Good' }",
        ],
        'nicomachean_ethics': [
            "{ sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'AUTHORS', targetSlug: 'nicomachean_ethics', targetName: 'Nicomachean Ethics', context: 'Aristotle\\'s major ethical treatise on virtue and the good life' }",
        ],
        'corpus_iuris_civilis': [
            "{ sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'INFLUENCES', targetSlug: 'islamic_fiqh_kalam_falsafa_corpus', targetName: 'Islamic Jurisprudence', context: 'Roman legal categories parallel and may have influenced early Islamic jurisprudence' }",
        ],
    },
    'ui/src/data/catalog/corpuses/iranCentralAsia.ts': {
        'gathas': [
            "{ sourceSlug: 'gathas', sourceName: 'Gāthās', verb: 'INFLUENCES', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Zoroastrian moral dualism, angels, and resurrection shape post-exilic Judaism' }",
        ],
        'quran': [
            "{ sourceSlug: 'quran', sourceName: 'Qur\\'an', verb: 'TRANSMITS', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Retells narratives of Adam, Noah, Abraham, Moses, Jesus, and Mary' }",
        ],
        'translation_movement': [
            "{ sourceSlug: 'translation_movement', sourceName: 'Translation Movement', verb: 'TRANSMITS', targetSlug: 'graeco_roman_corpus', targetName: 'Graeco-Roman Corpus', context: 'Bayt al-Hikma translates Plato, Aristotle, Euclid, Galen into Arabic' }",
        ],
        'mecca_city': [
            "{ sourceSlug: 'prophet_muhammad', sourceName: 'Prophet Muhammad', verb: 'BORN_IN', targetSlug: 'mecca_city', targetName: 'Mecca', context: 'Born in Mecca c. 570 CE; city of the Ka\\'ba and Hajj pilgrimage' }",
        ],
        'medina_city': [
            "{ sourceSlug: 'prophet_muhammad', sourceName: 'Prophet Muhammad', verb: 'MIGRATES_TO', targetSlug: 'medina_city', targetName: 'Medina', context: 'Hijra to Medina 622 CE; established first Islamic polity' }",
        ],
        'first_revelation_610': [
            "{ sourceSlug: 'first_revelation_610', sourceName: 'First Revelation (610 CE)', verb: 'CAUSES', targetSlug: 'quran', targetName: 'Qur\\'an', context: 'Angel Jibril reveals first sura to Muhammad in Cave Hira' }",
        ],
        'shahnameh': [
            "{ sourceSlug: 'ferdowsi', sourceName: 'Ferdowsi', verb: 'AUTHORS', targetSlug: 'shahnameh', targetName: 'Shāhnāmeh', context: 'Persian national epic composed c. 977–1010 CE' }",
        ],
    },
    'ui/src/data/catalog/corpuses/eastAsia.ts': {
        'analects_confucius': [
            "{ sourceSlug: 'confucius', sourceName: 'Confucius', verb: 'AUTHORS', targetSlug: 'analects_confucius', targetName: 'Analects', context: 'Compiled sayings and ideas attributed to Confucius by his disciples' }",
        ],
        'dao_de_jing': [
            "{ sourceSlug: 'dao_de_jing', sourceName: 'Dào Dé Jīng', verb: 'INFLUENCES', targetSlug: 'sinic_classics_corpus', targetName: 'Sinic Classics Corpus', context: 'Foundational Daoist text that complements and contrasts Confucian thought' }",
        ],
        'tripitaka_koreana': [
            "{ sourceSlug: 'tripitaka_koreana', sourceName: 'Tripiṭaka Koreana', verb: 'TRANSMITS', targetSlug: 'south_se_asia_corpus', targetName: 'South & SE Asian Corpus', context: 'Korean woodblock printing of complete Buddhist canon from Indian/Chinese sources' }",
        ],
        'kojiki': [
            "{ sourceSlug: 'kojiki', sourceName: 'Kojiki', verb: 'INFLUENCES', targetSlug: 'japanese_classical_corpus', targetName: 'Japanese Classical Corpus', context: 'Oldest extant Japanese chronicle; foundation of Shinto mythology' }",
        ],
        'hunminjeongeum': [
            "{ sourceSlug: 'king_sejong', sourceName: 'King Sejong', verb: 'CREATES', targetSlug: 'hunminjeongeum', targetName: 'Hunminjeongeum', context: 'Promulgated Korean alphabet (Hangul) in 1443–1446' }",
        ],
    },
}

for filepath, entity_updates in UPDATES.items():
    with open(filepath, 'r') as f:
        content = f.read()
    
    total_added = 0
    for slug, new_rels in entity_updates.items():
        # Find: relationships: [],  for this entity
        # Strategy: find the slug, then find the nearest 'relationships: [],' 
        slug_pattern = f"'{slug}'"
        slug_idx = content.find(slug_pattern)
        if slug_idx == -1:
            print(f"  SKIP (slug not found): {slug} in {filepath}")
            continue
        
        # Find relationships: [], after the slug
        search_start = slug_idx
        empty_rel_pattern = 'relationships: [],'
        rel_idx = content.find(empty_rel_pattern, search_start)
        
        if rel_idx == -1 or rel_idx > slug_idx + 2000:
            # Check if it already has relationships
            has_rel = content.find('relationships: [', search_start)
            if has_rel != -1 and has_rel < slug_idx + 2000:
                # Has non-empty relationships, need to append
                # Find the closing ] of the relationships array
                bracket_start = has_rel + len('relationships: [')
                # Find matching ]
                depth = 1
                pos = bracket_start
                while pos < len(content) and depth > 0:
                    if content[pos] == '[':
                        depth += 1
                    elif content[pos] == ']':
                        depth -= 1
                    pos += 1
                insert_pos = pos - 1  # before the closing ]
                # Check if there are existing items
                existing = content[bracket_start:insert_pos].strip()
                if existing:
                    prefix = ',\n      '
                else:
                    prefix = '\n      '
                rel_str = prefix + (',\n      '.join(new_rels))
                content = content[:insert_pos] + rel_str + '\n    ' + content[insert_pos:]
                total_added += len(new_rels)
            else:
                print(f"  SKIP (no rel array found): {slug} in {filepath}")
            continue
        
        # Replace empty array with our relationships
        rel_str = 'relationships: [\n      ' + ',\n      '.join(new_rels) + ',\n    ],'
        content = content[:rel_idx] + rel_str + content[rel_idx + len(empty_rel_pattern):]
        total_added += len(new_rels)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"{filepath}: added {total_added} relationships")

print("\nDone!")
