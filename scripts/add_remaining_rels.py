"""Add remaining cross-corpus relationships using line-by-line approach."""
import re

def add_rels_to_entity(content, entity_slug, new_rels_text):
    """Find entity by slug, find its relationships: [], and replace with new rels."""
    lines = content.split('\n')
    
    # Find the line with this slug as entity slug (starts with spaces + slug:)
    slug_line_idx = None
    for i, line in enumerate(lines):
        if line.strip() == f"slug: '{entity_slug}',":
            slug_line_idx = i
            break
    
    if slug_line_idx is None:
        return content, False
    
    # Find the nearest relationships line after the slug
    for j in range(slug_line_idx + 1, min(slug_line_idx + 30, len(lines))):
        stripped = lines[j].strip()
        if stripped == 'relationships: [],':
            # Replace with new relationships
            indent = '    '
            new_line = f'{indent}relationships: [\n'
            for k, rel in enumerate(new_rels_text):
                new_line += f'      {rel}'
                if k < len(new_rels_text) - 1:
                    new_line += ','
                new_line += '\n'
            new_line += f'{indent}],'
            lines[j] = new_line
            return '\n'.join(lines), True
        # If we hit a non-empty relationships, skip
        if stripped.startswith('relationships: [') and stripped != 'relationships: [],':
            return content, False
    
    return content, False

# All the updates that were skipped
REMAINING = {
    'ui/src/data/catalog/corpuses/mesopotamian.ts': {
        'enuma_elish': [
            "{ sourceSlug: 'enuma_elish', sourceName: 'Enūma Eliš', verb: 'INFLUENCES', targetSlug: 'genesis', targetName: 'Genesis', context: 'Creation narrative parallels — cosmos from watery chaos, structured creation sequence' }",
        ],
        'nineveh': [
            "{ sourceSlug: 'library_of_nineveh', sourceName: 'Library of Nineveh', verb: 'OCCURS_IN', targetSlug: 'nineveh', targetName: 'Nineveh', context: \"Ashurbanipal's royal library located in Nineveh\" }",
        ],
    },
    'ui/src/data/catalog/corpuses/graecoRoman.ts': {
        'iliad': [
            "{ sourceSlug: 'homer_poet', sourceName: 'Homer', verb: 'AUTHORS', targetSlug: 'iliad', targetName: 'Iliad', context: 'Attributed author of the foundational Greek epic' }",
        ],
        'histories_herodotus': [
            "{ sourceSlug: 'histories_herodotus', sourceName: 'Histories (Herodotus)', verb: 'DESCRIBES', targetSlug: 'babylon_city', targetName: 'Babylon', context: 'Herodotus Book I provides detailed ethnographic account of Babylon' }",
        ],
        'athens_city': [
            "{ sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Academy in Athens c. 387 BCE' }",
            "{ sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'TEACHES_IN', targetSlug: 'athens_city', targetName: 'Athens', context: 'Founded the Lyceum in Athens c. 335 BCE' }",
        ],
        'the_republic_plato': [
            "{ sourceSlug: 'plato_philosopher', sourceName: 'Plato', verb: 'AUTHORS', targetSlug: 'the_republic_plato', targetName: 'The Republic', context: \"Plato's masterwork on justice, ideal governance, and the Form of the Good\" }",
        ],
        'nicomachean_ethics': [
            "{ sourceSlug: 'aristotle_philosopher', sourceName: 'Aristotle', verb: 'AUTHORS', targetSlug: 'nicomachean_ethics', targetName: 'Nicomachean Ethics', context: \"Aristotle's major ethical treatise on virtue and the good life\" }",
        ],
        'corpus_iuris_civilis': [
            "{ sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'INFLUENCES', targetSlug: 'islamic_fiqh_kalam_falsafa_corpus', targetName: 'Islamic Jurisprudence', context: 'Roman legal categories parallel and may have influenced early Islamic jurisprudence' }",
        ],
        'rome_city': [
            "{ sourceSlug: 'corpus_iuris_civilis', sourceName: 'Corpus Iuris Civilis', verb: 'OCCURS_IN', targetSlug: 'rome_city', targetName: 'Rome', context: 'Codification of Roman law under Justinian, compiled in Constantinople' }",
        ],
    },
    'ui/src/data/catalog/corpuses/iranCentralAsia.ts': {
        'gathas': [
            "{ sourceSlug: 'gathas', sourceName: 'Gāthās', verb: 'INFLUENCES', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Zoroastrian moral dualism, angels, and resurrection shape post-exilic Judaism' }",
        ],
        'quran': [
            "{ sourceSlug: 'quran', sourceName: \"Qur'an\", verb: 'TRANSMITS', targetSlug: 'biblical_corpus', targetName: 'Biblical Corpus', context: 'Retells narratives of Adam, Noah, Abraham, Moses, Jesus, and Mary' }",
        ],
    },
    'ui/src/data/catalog/corpuses/eastAsia.ts': {
        'analects_confucius': [
            "{ sourceSlug: 'confucius', sourceName: 'Confucius', verb: 'AUTHORS', targetSlug: 'analects_confucius', targetName: 'Analects', context: 'Compiled sayings and ideas attributed to Confucius by his disciples' }",
        ],
        'dao_de_jing': [
            "{ sourceSlug: 'dao_de_jing', sourceName: 'Dào Dé Jīng', verb: 'INFLUENCES', targetSlug: 'sinic_classics_corpus', targetName: 'Sinic Classics Corpus', context: 'Foundational Daoist text that complements and contrasts Confucian thought' }",
        ],
    },
}

for filepath, entity_updates in REMAINING.items():
    with open(filepath, 'r') as f:
        content = f.read()
    
    total = 0
    for slug, rels in entity_updates.items():
        content, success = add_rels_to_entity(content, slug, rels)
        if success:
            total += len(rels)
            print(f"  ADDED: {slug} ({len(rels)} rels)")
        else:
            print(f"  SKIP: {slug}")
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"  {filepath}: {total} relationships added\n")

print("Done!")
