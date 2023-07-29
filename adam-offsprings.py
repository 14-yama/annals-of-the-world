import uuid

# Define a Person class to represent individuals in the family tree


class Person:
    def __init__(self, name, father=None):
        # Generate a unique identifier for each person
        self.uuid = uuid.uuid4()
        self.name = name
        self.father = father
        self.children = []

    # Method to add a child to the person's list of children
    def add_child(self, child):
        self.children.append(child)
        child.father = self  # Update the child's father attribute

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
        # Pass the existing parent as the father
        child = Person(child_name, father=parent)
        parent.add_child(child)
        family_tree[child.uuid] = child


# Initialize an empty family tree dictionary
family_tree = {}

# Create the root of the family tree for Adam
adam_uuid = uuid.uuid4()
adam = Person("Adam")
family_tree[adam_uuid] = adam

# Example usage to build the family tree:

# 1 Generation
add_children("Adam", adam_uuid, ["Cain", "Abel", "Seth"])

# 2 Generation
cain_uuid = family_tree[adam_uuid].children[0].uuid
add_children("Cain", cain_uuid, ["Enoch"])

seth_uuid = family_tree[adam_uuid].children[2].uuid
add_children("Seth", seth_uuid, ["Enosh"])

# 3 Generation
enoch_uuid = family_tree[cain_uuid].children[0].uuid
add_children("Enoch", enoch_uuid, ["Irad"])

enosh_uuid = family_tree[seth_uuid].children[0].uuid
add_children("Enosh", enosh_uuid, ["Kenan"])

# 4 Generation
irad_uuid = family_tree[enoch_uuid].children[0].uuid
add_children("Irad", irad_uuid, ["Mehujael"])

kenan_uuid = family_tree[enosh_uuid].children[0].uuid
add_children("Kenan", kenan_uuid, ["Mahalalel"])

# 5 Generation
mehujael_uuid = family_tree[irad_uuid].children[0].uuid
add_children("Mehujael", mehujael_uuid, ["Methushael"])

mahalalel_uuid = family_tree[kenan_uuid].children[0].uuid
add_children("Mahalalel", mahalalel_uuid, ["Jared"])

# 6 Generation
methushael_uuid = family_tree[mehujael_uuid].children[0].uuid
add_children("Methushael", methushael_uuid, ["Lamech"])

jared_uuid = family_tree[mahalalel_uuid].children[0].uuid
add_children("Jared", jared_uuid, ["Enoch"])

# Function to print the family tree recursively


def print_family_tree(person, generation=1):
    indentation = "    " * generation
    print(f"{indentation}+ {person.name} ({person.father.name if person.father else 'Unknown'})")
    for child in person.children:
        print_family_tree(child, generation + 1)


# Print the family tree starting from Adam
print_family_tree(family_tree[adam_uuid])
