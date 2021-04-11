from DnD4py import lookup_5e as lookup


def get_traits(name):
    monster = lookup.Roll20Monster(name=name)
    return split_traits(monster.str_attributes)


def split_traits(string):
    elements = string.split("\n")
    out = {
        "hp": elements[0],
        "ac": elements[1],
        "speed": elements[2],
        "cr": elements[3],
        "type": elements[4],
        "size": elements[5],
        "alignment": elements[6],
        "senses": elements[7],
        "skills": elements[8],
        "languages": elements[9]
    }
    return out


def get_attributes(name):
    monster = lookup.Roll20Monster(name=name)
    attributes = monster.str_attributes.split("\n")
    values = attributes[6].replace("\t", "").split(" ")
    return values


get_attributes("goblin")