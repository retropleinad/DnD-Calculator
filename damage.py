from collections import deque

# The damage dice has 20 sides
D20 = 20.


# Class to take attacks and saves and calculate average damage
class AttackHandler:

    # Stores attacks and saves in appropriate deques
    def __init__(self, armor_class=15, turns=10):
        self.attacks = deque()
        self.saves = deque()
        self.armor_class = armor_class
        self.turns = turns

    # Add an attack to the attack handler
    def add_attack(self, attack):
        self.attacks.append(attack)

    # Add a save to the attack handler
    def add_save(self, save):
        self.saves.append(save)

    # What is an attack's hit rate?
    def hit_rate(self, hit_modifier):
        return (D20 - self.armor_class + hit_modifier) / D20

    # Are there any attacks in the attack handler?
    def has_attacks(self):
        if len(self.attacks) > 0:
            return True
        return False

    # Are there any saves in the attack handler?
    def has_saves(self):
        if len(self.saves) > 0:
            return True
        return False

    # Calculate the damage
    def calculate(self):
        damage = 0.
        while self.has_attacks():
            attack = self.attacks.popleft()
            damage_hit = (attack.max_dice_damage / 2) + attack.damage_modifiers + .5
            attacks_landed = attack.number_turn * attack.attacks_turn * self.hit_rate(attack.hit_modifier)
            damage += damage_hit * attacks_landed
        while self.has_saves():
            save = self.saves.popleft()
            damage_hit = (save.max_dice_damage / 2) + save.damage_modifier + .5
            damage_fail = 0
            if save.half_on_success:
                damage_fail = damage_hit / 2
            damage += damage_hit * save.HIT_RATE
            damage += damage_fail * (1 - save.HIT_RATE)
        return damage


# Stores data associated with an attack
class Attack:

    def __init__(self, max_dice_damage, hit_modifier=0, damage_modifiers=0,
                 number_turn=1, attacks_turn=0):
        self.hit_modifier = hit_modifier
        self.max_dice_damage = max_dice_damage
        self.damage_modifiers = damage_modifiers
        self.number_turn = number_turn
        self.attacks_turn = attacks_turn


# Saves data associated with a saving throw
class SavingThrow:

    # For success calculator, ignore max_dice_damage, half_on_success, number_turns, and attacks_turn
    def __init__(self, ability_modifier=0, dc=8, max_dice_damage=0, damage_modifier=0,
                 half_on_success=False, number_turns=1, attacks_turn=1):
        self.ability_modifier = ability_modifier
        self.dc = float(dc)
        self.max_dice_damage = max_dice_damage
        self.damage_modifier = damage_modifier
        self.half_on_success = half_on_success
        self.number_turns = number_turns
        self.attacks_turn = attacks_turn
        self.HIT_RATE = 1 - ((self.dc - self.ability_modifier) / D20)
