from DnD4py import lookup_5e as lookup

spell = lookup.Roll20Spell(name="fireball")
print(spell.str_attributes)