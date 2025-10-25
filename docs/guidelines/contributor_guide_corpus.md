# Contributor Guide: Corpus Nodes & Major Corpora

This guide helps contributors seed, curate, and expand corpus nodes in the Annals of the World knowledge graph. It covers the structure for the Biblical corpus and outlines other major corpora to anticipate, ensuring consistency and interoperability across traditions.

---

## 1. What is a Corpus Node?
- A `:Corpus` node represents a canonical grouping of texts, traditions, or cultural artifacts.
- Used to organize evidence, link related entities, and support comparative analysis.
- Example: `BIBLICAL_CORPUS` for the Hebrew Bible, Dead Sea Scrolls, and related texts.

## 2. How to Seed a Corpus
- Create a `:Corpus` node with a unique slug, name, and description.
- Link `:Evidence` nodes to the corpus using `(:Evidence)-[:BELONGS_TO]->(:Corpus)`.
- Use corpus tiers (A–D) to indicate primary, peer-reviewed, institutional, or digital sources.
- Include major texts, entities, and their importance in the corpus description.

## 3. The Biblical Corpus (Example)
- **Texts:** Hebrew Bible/Tanakh, Septuagint, New Testament, Dead Sea Scrolls.
- **Entities:** Prophets, scribes, priesthoods, major places (Jerusalem, Babylon).
- **Importance:** Foundation for Abrahamic religions, law, literature, and historical chronology.
- **Cypher Example:**
  ```
  MERGE (c:Corpus {slug:'biblical_corpus', name:'Biblical Corpus'})
  MERGE (e:Evidence {slug:'dead_sea_scrolls'})
  MERGE (e)-[:BELONGS_TO]->(c)
  ```

## 4. Other Major Corpora to Anticipate

### Mesopotamian Corpus
- **Texts:** Epic of Gilgamesh, Enuma Elish, Code of Hammurabi
- **Entities:** Sumerians, Akkadians, Babylonians, Assyrians
- **Importance:** Oldest urban civilizations, early legal codes, mythologies, empires

### Greco-Roman Corpus
- **Texts:** Homeric Epics, Herodotus, Plato, Aristotle, Roman historians, Roman law
- **Entities:** Athens, Sparta, Rome, Caesar, Senate, Republic/Empire
- **Importance:** Political systems, philosophy, law, citizenship, classical literature

### Egyptian Corpus
- **Texts:** Book of the Dead, Pyramid Texts, Egyptian king lists
- **Entities:** Pharaohs, dynasties, gods (Ra, Osiris), pyramids, Nile-based events
- **Importance:** Longest continuous civilization, religion, monumental architecture

### Indic Corpus
- **Texts:** Rigveda, Mahabharata, Ramayana, Arthashastra, Buddhist Canon
- **Entities:** Vedic tribes, Maurya/Gupta dynasties, Ashoka, Hindu & Buddhist concepts
- **Importance:** Religion, philosophy, statecraft, cultural diffusion across Asia

### Chinese Corpus
- **Texts:** Shujing (Book of Documents), Analects, Dao De Jing, Han Histories
- **Entities:** Dynasties (Shang, Zhou, Han, Tang), Confucius, Laozi, Sun Tzu
- **Importance:** State philosophy, meritocracy, dynastic cycles, technological innovation

### Islamic Corpus
- **Texts:** Qur’an, Hadith, early Islamic historiography
- **Entities:** Muhammad, Rashidun/Umayyad/Abbasid Caliphates, scholars (Avicenna, Al-Ghazali)
- **Importance:** Religion, science, law, political structures, cultural transmission

### Medieval Christian Corpus
- **Texts:** Church Fathers, Scholastics, Papal Bulls, Canon Law
- **Entities:** Augustine, Thomas Aquinas, Popes, Crusades, Inquisitions
- **Importance:** Religious-political fusion, scholastic thought, institutional church

### Modern Secular Corpus
- **Texts:** Enlightenment philosophers, Constitutions, Declarations (e.g., UN)
- **Entities:** Locke, Rousseau, Marx, US Constitution, French Revolution, UN
- **Importance:** Political ideas, legal frameworks, globalization, human rights

---

## 5. Contributor Checklist
- [ ] Use unique slugs and descriptive names for corpus nodes.
- [ ] Link evidence and major texts to the corpus using `BELONGS_TO`.
- [ ] Document entities and importance in the corpus description.
- [ ] Follow schema and classification guidelines for consistency.
- [ ] Anticipate and propose new corpora as the project expands.

---

For more details, see:
- [Schema Reference](./schema.md)
- [Classification & Corpus Registry](./classification.md)
- [Node Descriptions](./node_descriptions.md)
