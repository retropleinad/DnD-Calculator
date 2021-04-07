from DnD4py import lookup_5e as lookup


def search(name):
    monster = lookup.Roll20Monster(name=name)
    return to_dict(monster.str_attributes)


def to_dict(string):
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
