import tkinter as tk
import tksheet

import regressions
import damage


# This class is the first screen users see and serves as the portal screen to other major screens.
# The user is presented with buttons to travel to other screens.
class IntroScreen:

    # The key is the name of each button, and the value is the text to display on that button
    __button_text = {
        "cr_button": "Calculate CR",
        "damage_button": "Calculate Damage",
        "instruct_button": "Instructions",
        "spells_button": "Balance Spells",
        "saving_throw_button": "Saving Throw Success",
        "monster_lookup_button": "Monster Lookup"
    }

    # Buttons are buttons
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("DM Tools")

        self.cr_button = None
        self.damage_button = None
        self.instruct_button = None
        self.spells_button = None
        self.saving_throw_button = None
        self.monster_lookup_button = None

        self.draw_buttons()

    # Method to draw each button on the screen
    def draw_buttons(self):
        self.cr_button = tk.Button(master=self.screen, text=self.__button_text["cr_button"], width=15,
                                   height=2, command=lambda: self.switch_screen("cr"))
        self.damage_button = tk.Button(master=self.screen, text=self.__button_text["damage_button"], width=15,
                                       height=2, command=lambda: self.switch_screen("dps"))
        self.instruct_button = tk.Button(master=self.screen, text=self.__button_text["instruct_button"], width=15,
                                         height=2, command=lambda: self.switch_screen("instruct"))
        self.spells_button = tk.Button(master=self.screen, text=self.__button_text["spells_button"], width=15,
                                       height=2, command=lambda: self.switch_screen("spells"))
        self.saving_throw_button = tk.Button(master=self.screen, text=self.__button_text["saving_throw_button"],
                                             width=15, height=2, command=lambda: self.switch_screen("saves"))
        self.monster_lookup_button = tk.Button(master=self.screen, text=self.__button_text["monster_lookup_button"],
                                               width=15, height=2, command=lambda: self.switch_screen("monster_lookup"))

        self.cr_button.grid(row=0, column=0, padx=5, pady=2)
        self.damage_button.grid(row=0, column=2, padx=5, pady=2)
        self.instruct_button.grid(row=0, column=1, padx=5, pady=2)
        self.spells_button.grid(row=1, column=1, padx=5, pady=2)
        self.saving_throw_button.grid(row=1, column=0, padx=5, pady=2)
        self.monster_lookup_button.grid(row=1, column=2, padx=5, pady=2)

    # When a button is clicked, this method is called and takes the users to the appropriate screen
    def switch_screen(self, window):
        if window.lower() == "cr":
            cr_screen = CRScreen()
        elif window.lower() == "dps":
            dps_screen = DamageScreen()
        elif window.lower() == "instruct":
            info_screen = InfoScreen()
        elif window.lower() == "spells":
            spell_screen = SpellScreen()
        elif window.lower() == "saves":
            save_screen = SavingThrowScreen()
        elif window.lower() == "monster_lookup":
            monster_screen = MonsterLookupScreen()
        else:
            raise Exception("incorrect command: enter --cr, --dps, or --instruct")

    def mainloop(self):
        self.screen.mainloop()


# This screen provides users with information on the app and how to use it
class InfoScreen:

    # This information is displayed on the screen:
    __info = "Welcome to the early alpha CR calculator version 1.0.1. " \
             "Currently it can only calculate a CR estimate from AC and HP Instructions: " \
             "Enter AC and HP, hit calculate, and the CR will be output in the CR field."

    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("Instructions")
        self.draw_text()

    # Method to draw text on the screen
    def draw_text(self):
        text = tk.Text(master=self.screen, height=20, width=45, relief="sunken", wrap="word", padx=5, pady=5)
        text.insert(tk.END, self.__info)
        text.pack()

    def mainloop(self):
        self.screen.mainloop()


# This screen appears with an appropriate message whenever the user clicks on a help button
class HelpScreen:

    # The keys are a label for the topic and the values are the help messages
    messages = {
        "crscreen": "Enter the armor class and hitpoints, "
                    "then click calculate to view the predicted challenge rating",
        "attack": "Enter the hit modifier for the attack, the maximum non-crit non-vulnerabilities damage, "
                  "(e.g. 3d12 would be 36), the combined damage modifiers for the attack, the number of turns"
                  "the attack is fired and the number of attacks a turn ",
        "damage": "Enter the target's AC, the number of turns, then add attacks",
        "spell": "Placeholder for spells",
        "saves": "This screen calculates the rate that the target succeeds on a saving throw.\n "
                 "DC is calculated as 8 + proficiency modifier + spellcasting modifier",
        "damage_saves": "Add an attack that hits based off of the target's saving throw.",
        "monster_lookup": "Enter a monster's name then hit the search button."
    }

    def __init__(self, window):
        self.screen = tk.Tk()
        self.screen.title("Help")
        self.draw_text(window)

    # Draws text onto the screen
    def draw_text(self, window):
        text = tk.Text(master=self.screen, height=20, width=45, relief="sunken", wrap="word", padx=5, pady=5)
        text.insert(tk.END, self.messages[window])
        text.pack()

    def mainloop(self):
        self.screen.mainloop()


# Error screens appear whenever the user incorrectly attempts to calculate data and provides instructions
# Uses the same advice that is provided in HelpScreen
class ErrorScreen(HelpScreen):

    def __init__(self, window):
        self.error_message = "Error: Please input a numerical value.\n\n"
        super().__init__(window)
        self.screen.title("Error")

    # Draws text onto the screen
    def draw_text(self, window):
        text = tk.Text(master=self.screen, height=20, width=45, relief="sunken", wrap="word", padx=5, pady=5)
        text.insert(tk.END, self.error_message + self.messages[window])
        text.pack()


# Currently a placeholder ... gives users the ability to balance spells
class SpellScreen:

    def __init__(self):
        pass


# Allows the user to calculate AC, HP, and CR based off of values for the other variables
# Includes calculate buttons, labels, and entries for all three labels
class CRScreen:

    # Entries, labels, and calculate buttons are provided for CR, HP, and AC
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("CR Calculator")

        self.ac_entry = None
        self.hp_entry = None
        self.cr_entry = None

        self.cr_label = None
        self.ac_label = None
        self.hp_label = None

        self.cr_button = None
        self.hp_button = None
        self.ac_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_buttons()

    # Outputs labels onto the screen
    def draw_labels(self):
        self.cr_label = tk.Label(master=self.screen, text="CR", width=10, height=1)
        self.hp_label = tk.Label(master=self.screen, text="HP", width=10, height=1)
        self.ac_label = tk.Label(master=self.screen, text="AC", width=10, height=1)

        self.cr_label.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        self.hp_label.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
        self.ac_label.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")

    # Draws buttons onto the screen
    def draw_buttons(self):
        self.cr_button = tk.Button(master=self.screen, text="Calculate CR", width=10, height=1,
                                   command=self.calculate_cr)
        self.hp_button = tk.Button(master=self.screen, text="Calculate HP", width=10, height=1,
                                   command=self.calculate_hp)
        self.ac_button = tk.Button(master=self.screen, text="Calculate AC", width=10, height=1,
                                   command=self.calculate_ac)
        self.help_button = tk.Button(master=self.screen, text="Help", width=7, height=1, command=self.draw_help)

        self.cr_button.grid(row=0, column=2, padx=5, pady=5)
        self.hp_button.grid(row=1, column=2, padx=5, pady=5)
        self.ac_button.grid(row=2, column=2, padx=5, pady=5)
        self.help_button.grid(row=3, column=0, pady=5)

    # When the help button is clicked, create a help screen with the appropriate message
    def draw_help(self):
        help_screen = HelpScreen("crscreen")

    # Grabs data from entries and outputs an appropriate value for CR
    def calculate_cr(self):
        try:
            health = float(self.hp_entry.get())
            armor = float(self.ac_entry.get())
            self.cr_entry.delete(0, tk.END)
            self.cr_entry.insert(string=str(regressions.predict(target="cr", hp=health, ac=armor)), index=0)
        except ValueError:
            error_screen = ErrorScreen("crscreen")
        finally:
            self.hp_entry.delete(0, tk.END)
            self.ac_entry.delete(0, tk.END)

    # Grabs data from entries and outputs an appropriate value for AC
    def calculate_ac(self):
        try:
            cr = float(self.cr_entry.get())
            health = float(self.hp_entry.get())
            self.ac_entry.delete(0, tk.END)
            self.ac_entry.insert(string=str(regressions.predict(target="ac", cr=cr, hp=health)), index=0)
        except ValueError:
            error_screen = ErrorScreen("crscreen")
        finally:
            self.hp_entry.delete(0, tk.END)
            self.cr_entry.delete(0, tk.END)

    # Grabs data from entries and outputs an appropriate value for HP
    def calculate_hp(self):
        try:
            cr = float(self.cr_entry.get())
            armor = float(self.ac_entry.get())
            self.hp_entry.delete(0, tk.END)
            self.hp_entry.insert(string=str(regressions.predict(target="hp", cr=cr, ac=armor)), index=0)
        except ValueError:
            error_screen = ErrorScreen("crscreen")
        finally:
            self.ac_entry.delete(0, tk.END)
            self.cr_entry.delete(0, tk.END)

    # Outputs entries onto the screen
    def draw_entries(self):
        self.cr_entry = tk.Entry(master=self.screen, width=10)
        self.ac_entry = tk.Entry(master=self.screen, width=10)
        self.hp_entry = tk.Entry(master=self.screen, width=10)

        self.cr_entry.grid(row=0, column=1, padx=5, pady=0, sticky="w")
        self.hp_entry.grid(row=1, column=1, padx=5, pady=0)
        self.ac_entry.grid(row=2, column=1, padx=5, pady=0)

        self.cr_entry.insert(string="Enter CR", index=0)
        self.ac_entry.insert(string="Enter AC", index=0)
        self.hp_entry.insert(string="Enter HP", index=0)

    # Maybe remove in the future ???
    def mainloop(self):
        self.screen.mainloop()


# This screen allows the user to calculate the average damage certain attacks will do against a target with a specific
# armor class over a span of a specific number of turns.
class DamageScreen:

    # Text for the headers in a table that holds entered attacks
    __attack_table_headers = (
        "Max Dice Damage",
        "Hit Modifier",
        "Damage Modifier",
        "Turns Attacked",
        "Attacks per Turn"
    )

    # Text for the headers in a table that holds entered attacks involving saving throws
    __save_table_headers = (
        "Ability Modifier",
        "Save DC",
        "Max Dice Damage",
        "Damage Modifiers",
        "Turns Attacked",
        "Attacks per Turn",
        "Half on Success?"
    )

    # Creates labels, entries, buttons, and tables
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("Calculate Damage")

        self.target_ac_label = None
        self.number_turns_label = None
        self.average_damage_label = None

        self.target_ac_entry = None
        self.number_turns_entry = None
        self.average_damage_entry = None

        self.calculate_button = None
        self.help_button = None
        self.add_attack_button = None
        self.add_save_button = None

        self.attack_table = None
        self.save_table = None

        self.attacks = damage.AttackHandler()

        self.draw_table()
        self.draw_labels()
        self.draw_entries()
        self.draw_buttons()

    # Outputs labels onto the screen
    def draw_labels(self):
        self.target_ac_label = tk.Label(master=self.screen, text="Target AC", width=20, height=1)
        self.number_turns_label = tk.Label(master=self.screen, text="Number of turns", width=20, height=1)
        self.average_damage_label = tk.Label(master=self.screen, text="Average Damage", width=20, height=1)

        self.target_ac_label.grid(row=0, column=1, pady=10, padx=10, sticky="ne")
        self.number_turns_label.grid(row=0, column=1, pady=10, padx=10, sticky="e")
        self.average_damage_label.grid(row=0, column=1, pady=10, padx=10, sticky="se")

    # Draws entries onto the screen
    def draw_entries(self):
        self.target_ac_entry = tk.Entry(master=self.screen, width=10)
        self.number_turns_entry = tk.Entry(master=self.screen, width=10)
        self.average_damage_entry = tk.Entry(master=self.screen, width=10)

        self.target_ac_entry.grid(row=0, column=2, pady=10, padx=10, sticky="n")
        self.number_turns_entry.grid(row=0, column=2, pady=10, padx=10, sticky="w")
        self.average_damage_entry.grid(row=0, column=2, pady=10, padx=10, sticky="s")

    # Draws buttons onto the screen
    def draw_buttons(self):
        self.calculate_button = tk.Button(master=self.screen, text="Calculate Damage",
                                          width=14, height=1, command=self.calculate_damage)
        self.help_button = tk.Button(master=self.screen, text="Help",
                                     width=14, height=1, command=self.draw_help)
        self.add_attack_button = tk.Button(master=self.screen, text="Add Attack",
                                           width=14, height=1, command=self.add_attack)
        self.add_save_button = tk.Button(master=self.screen, text="Add Save",
                                         width=14, height=1, command=self.add_save)

        self.calculate_button.grid(row=0, column=3, pady=10, padx=10, sticky="n")
        self.help_button.grid(row=0, column=3, pady=10, padx=10, sticky="w")
        self.add_attack_button.grid(row=0, column=3, pady=10, padx=10, sticky="s")
        self.add_save_button.grid(row=1, column=3, pady=10, padx=10, sticky="n")

    # When the user clicks the "Add Attack" button, create a new attack screen
    def add_attack(self):
        attack_screen = AttackScreen(self.attacks, self.attack_table)

    # When the user clicks the "Add Save" button, create a new save screen
    def add_save(self):
        save_screen = DamageSaveScreen(self.attacks, self.save_table)

    # Calculate and output the average damage over the entered number of turns
    def calculate_damage(self):
        try:
            if self.attacks.has_attacks():
                self.attacks.armor_class = float(self.target_ac_entry.get())
            self.attacks.turns = float(self.number_turns_entry.get())
            dps = self.attacks.calculate()

            self.average_damage_entry.delete(0, tk.END)
            self.average_damage_entry.insert(string=str(dps), index=0)
        except ValueError:
            error_screen = ErrorScreen("damage")
        finally:
            self.target_ac_entry.delete(0, tk.END)
            self.target_ac_entry.insert(string="0", index=0)

            self.number_turns_entry.delete(0, tk.END)
            self.number_turns_entry.insert(string="0", index=0)

            self.draw_table()

    # When the user clicks the help button, create a help screen
    def draw_help(self):
        help_screen = HelpScreen("damage")

    # Outputs tables onto the screen
    def draw_table(self):
        self.attack_table = tksheet.Sheet(self.screen, total_columns=5, total_rows=0,
                                          show_x_scrollbar=False, width=645, height=300)
        self.save_table = tksheet.Sheet(self.screen, total_columns=7, total_rows=0,
                                        show_x_scrollbar=False, width=875, height=300)

        self.attack_table.headers((f"{header}" for header in self.__attack_table_headers))
        self.save_table.headers((f"{header}" for header in self.__save_table_headers))

        self.save_table.grid(row=1, column=0, sticky="w")
        self.attack_table.grid(row=0, column=0)

    def mainloop(self):
        self.screen.mainloop()


# Screen used for entering an attack to be calculated on the damage screen
# After entered, the attack appears in the damage table on the damage screen
class AttackScreen:

    # Text for each label on this screen
    __label_text = {
        "max_dice_label": "Max Dice Damage",
        "hit_modifier_label": "Hit Modifier",
        "damage_modifier_label": "Total damage modifiers",
        "number_turns_label": "Number of turns",
        "attacks_turn_label": "Attacks per turn",
    }

    # Creates labels, entries, and buttons
    def __init__(self, attacks, table):
        self.screen = tk.Tk()
        self.screen.title("Enter Attack")

        self.attack = damage.Attack
        self.attacks = attacks
        self.table = table

        self.max_dice_label = None
        self.hit_modifier_label = None
        self.damage_modifier_label = None
        self.number_turns_label = None
        self.attacks_turn_label = None

        self.max_dice_entry = None
        self.hit_modifier_entry = None
        self.damage_modifier_entry = None
        self.number_turns_entry = None
        self.attacks_turn_entry = None

        self.add_attack_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_buttons()

    # Draws labels onto the screen
    def draw_labels(self):
        self.max_dice_label = tk.Label(master=self.screen, text=self.__label_text["max_dice_label"],
                                       width=20, height=1)
        self.hit_modifier_label = tk.Label(master=self.screen, text=self.__label_text["hit_modifier_label"],
                                           width=20, height=1)
        self.damage_modifier_label = tk.Label(master=self.screen, text=self.__label_text["damage_modifier_label"],
                                              width=20, height=1)
        self.number_turns_label = tk.Label(master=self.screen, text=self.__label_text["number_turns_label"],
                                           width=20, height=1)
        self.attacks_turn_label = tk.Label(master=self.screen, text=self.__label_text["attacks_turn_label"],
                                           width=20, height=1)

        self.max_dice_label.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        self.hit_modifier_label.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
        self.damage_modifier_label.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
        self.number_turns_label.grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
        self.attacks_turn_label.grid(row=4, column=0, padx=1, pady=1, sticky="nsew")

    # Draws entries onto the screen
    def draw_entries(self):
        self.max_dice_entry = tk.Entry(master=self.screen, width=10)
        self.hit_modifier_entry = tk.Entry(master=self.screen, width=10)
        self.damage_modifier_entry = tk.Entry(master=self.screen, width=10)
        self.number_turns_entry = tk.Entry(master=self.screen, width=10)
        self.attacks_turn_entry = tk.Entry(master=self.screen, width=10)

        self.max_dice_entry.grid(row=0, column=1, padx=0, pady=0)
        self.hit_modifier_entry.grid(row=1, column=1, padx=0, pady=0)
        self.damage_modifier_entry.grid(row=2, column=1, padx=0, pady=0)
        self.number_turns_entry.grid(row=3, column=1, padx=0, pady=0)
        self.attacks_turn_entry.grid(row=4, column=1, padx=0, pady=0)

    # Draws buttons onto the screen
    def draw_buttons(self):
        self.add_attack_button = tk.Button(master=self.screen, text="Add Attack",
                                           width=10, height=1, command=self.make_attack)
        self.help_button = tk.Button(master=self.screen, text="Help",
                                     width=7, height=1, command=self.draw_help)

        self.add_attack_button.grid(row=0, column=2, padx=2, pady=2)
        self.help_button.grid(row=1, column=2, padx=2, pady=2)

    # After the data for the attack is entered, grab it, then create and store an attack object
    def make_attack(self):
        try:
            max_dice = float(self.max_dice_entry.get())
            hit_modifier = float(self.hit_modifier_entry.get())
            damage_modifier = float(self.damage_modifier_entry.get())
            number_turns = float(self.number_turns_entry.get())
            attacks_turn = float(self.attacks_turn_entry.get())

            attack = damage.Attack(
                max_dice_damage=max_dice,
                hit_modifier=hit_modifier,
                damage_modifiers=damage_modifier,
                number_turn=number_turns,
                attacks_turn=attacks_turn
            )
            self.attacks.add_attack(attack)

            entries = (max_dice, hit_modifier, damage_modifier, number_turns, attacks_turn)
            self.table.insert_row(f"{e}" for e in entries)
            self.table.refresh()
        except ValueError:
            error_screen = ErrorScreen("attack")
        finally:
            self.max_dice_entry.delete(0, tk.END)
            self.hit_modifier_entry.delete(0, tk.END)
            self.damage_modifier_entry.delete(0, tk.END)
            self.number_turns_entry.delete(0, tk.END)
            self.attacks_turn_entry.delete(0, tk.END)

    # Draw the help screen when the help button is clicked
    def draw_help(self):
        help_screen = HelpScreen("attack")

    def mainloop(self):
        self.screen.mainloop()


# Class for the screen that calculates saving throw success rate
class SavingThrowScreen:

    # Creates labels, entries, and buttons and outputs them onto the screen
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("Saving Throw Success")

        self.ability_modifier_label = None
        self.dc_label = None
        self.success_rate_label = None

        self.ability_modifier_entry = None
        self.dc_entry = None
        self.success_rate_entry = None

        self.calculate_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_buttons()

    # Draws labels onto the screen
    def draw_labels(self):
        self.ability_modifier_label = tk.Label(master=self.screen, text="Ability Modifiers", width=15, height=1)
        self.dc_label = tk.Label(master=self.screen, text="DC", width=15, height=1)
        self.success_rate_label = tk.Label(master=self.screen, text="Success Rate", width=15, height=1)

        self.ability_modifier_label.grid(row=0, column=0, padx=1, pady=5)
        self.dc_label.grid(row=1, column=0, padx=1, pady=5)
        self.success_rate_label.grid(row=2, column=0, padx=1, pady=5)

    # Draws entries onto the screen
    def draw_entries(self):
        self.ability_modifier_entry = tk.Entry(master=self.screen, width=10)
        self.dc_entry = tk.Entry(master=self.screen, width=10)
        self.success_rate_entry = tk.Entry(master=self.screen, width=10)

        self.ability_modifier_entry.grid(row=0, column=1, padx=1, pady=1)
        self.dc_entry.grid(row=1, column=1, padx=1, pady=1)
        self.success_rate_entry.grid(row=2, column=1, padx=1, pady=1)

    # Draws buttons onto the screen
    def draw_buttons(self):
        self.calculate_button = tk.Button(master=self.screen, text="Calculate",
                                          width=10, height=1, command=self.calculate)
        self.help_button = tk.Button(master=self.screen, text="Help", width=10, height=1, command=self.draw_help)

        self.calculate_button.grid(row=0, column=2, padx=1, pady=1)
        self.help_button.grid(row=1, column=2, padx=1, pady=1)

    # Calculate the saving throw success rate
    def calculate(self):
        try:
            dc = float(self.dc_entry.get())
            ability_modifier = float(self.ability_modifier_entry.get())
            save = damage.SavingThrow(dc=dc, ability_modifier=ability_modifier)

            self.success_rate_entry.delete(0, tk.END)
            self.success_rate_entry.insert(0, save.HIT_RATE)
        except ValueError:
            error_screen = ErrorScreen("saves")
        finally:
            self.ability_modifier_entry.delete(0, tk.END)
            self.dc_entry.delete(0, tk.END)

    # Create an appropriate help screen when the help button is clicked
    def draw_help(self):
        helpscreen = HelpScreen("saves")


# Screen for adding damage saves to the damage screen
class DamageSaveScreen:

    # Create labels, entries, and buttons
    def __init__(self, saves, table):
        self.screen = tk.Tk()
        self.screen.title = "Add Damage Saving Throw"
        self.saves = saves
        self.table = table

        self.ability_modifier_label = None
        self.dc_label = None
        self.max_dice_label = None
        self.damage_modifier_label = None
        self.number_turns_label = None
        self.attacks_turn_label = None

        self.ability_modifier_entry = None
        self.dc_entry = None
        self.max_dice_entry = None
        self.damage_modifier_entry = None
        self.number_turns_entry = None
        self.attacks_turn_entry = None

        self.half_on_success = tk.StringVar(master=self.screen)
        self.half_on_success_checkbox = None

        self.add_save_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_checkbox()
        self.draw_buttons()

    # Draws labels onto the screen
    def draw_labels(self):
        self.ability_modifier_label = tk.Label(master=self.screen, text="Ability Modifiers", width=15, height=1)
        self.dc_label = tk.Label(master=self.screen, text="DC", width=15, height=1)
        self.max_dice_label = tk.Label(master=self.screen, text="Max Dice Damage", width=15, height=1)
        self.damage_modifier_label = tk.Label(master=self.screen, text="Damage Modifiers", width=15, height=1)
        self.number_turns_label = tk.Label(master=self.screen, text="Number of Turns", width=15, height=1)
        self.attacks_turn_label = tk.Label(master=self.screen, text="Attacks per Turn", width=15, heigh=1)

        self.ability_modifier_label.grid(row=0, column=0, padx=5, pady=2)
        self.dc_label.grid(row=1, column=0, padx=5, pady=2)
        self.max_dice_label.grid(row=2, column=0, padx=5, pady=2)
        self.number_turns_label.grid(row=3, column=0, padx=5, pady=2)
        self.attacks_turn_label.grid(row=4, column=0, padx=5, pady=2)
        self.damage_modifier_label.grid(row=5, column=0, padx=5, pady=2)

    # Draws entries onto the screen
    def draw_entries(self):
        self.ability_modifier_entry = tk.Entry(master=self.screen, width=10)
        self.dc_entry = tk.Entry(master=self.screen, width=10)
        self.max_dice_entry = tk.Entry(master=self.screen, width=10)
        self.damage_modifier_entry = tk.Entry(master=self.screen, width=10)
        self.number_turns_entry = tk.Entry(master=self.screen, width=10)
        self.attacks_turn_entry = tk.Entry(master=self.screen, width=10)

        self.ability_modifier_entry.grid(row=0, column=1, padx=5, pady=2)
        self.dc_entry.grid(row=1, column=1, padx=5, pady=2)
        self.max_dice_entry.grid(row=2, column=1, padx=5, pady=2)
        self.number_turns_entry.grid(row=3, column=1, padx=5, pady=2)
        self.attacks_turn_entry.grid(row=4, column=1, padx=5, pady=2)
        self.damage_modifier_entry.grid(row=5, column=1, padx=5, pady=2)

    # Draws checkbox onto the screen
    def draw_checkbox(self):
        self.half_on_success_checkbox = tk.Checkbutton(master=self.screen, text="Half on success",
                                                       var=self.half_on_success, onvalue='True', offvalue='False')
        self.half_on_success_checkbox.deselect()
        self.half_on_success_checkbox.grid(row=0, column=2, padx=5, pady=2)

    # Draw buttons onto the screen
    def draw_buttons(self):
        self.help_button = tk.Button(master=self.screen, text="Help", width=10, height=1, command=self.draw_help)
        self.add_save_button = tk.Button(master=self.screen, text="Add Save", width=10, height=1, command=self.add_save)

        self.help_button.grid(row=1, column=2, padx=5, pady=2)
        self.add_save_button.grid(row=2, column=2, padx=5, pady=2)

    # Create a help screen whenever the help button is clicked
    def draw_help(self):
        help_screen = HelpScreen("damage_saves")

    # Take data from entries, create and store a save
    def add_save(self):
        try:
            ability_modifier = float(self.ability_modifier_entry.get())
            dc = float(self.dc_entry.get())
            max_dice = float(self.max_dice_entry.get())
            damage_modifier = float(self.damage_modifier_entry.get())
            number_turns = float(self.number_turns_entry.get())
            attacks_turn = float(self.attacks_turn_entry.get())

            save = damage.SavingThrow(
                ability_modifier=ability_modifier,
                dc=dc,
                max_dice_damage=max_dice,
                damage_modifier=damage_modifier,
                number_turns=number_turns,
                attacks_turn=attacks_turn
            )
            self.saves.add_save(save)

            entries = (ability_modifier, dc, max_dice, damage_modifier,
                       number_turns, attacks_turn, self.half_on_success.get())
            self.table.insert_row(f"{e}" for e in entries)
            self.table.refresh()
        except ValueError:
            error_screen = ErrorScreen("damage_saves")
        finally:
            self.ability_modifier_entry.delete(0, tk.END),
            self.dc_entry.delete(0, tk.END),
            self.max_dice_entry.delete(0, tk.END),
            self.number_turns_entry.delete(0, tk.END),
            self.attacks_turn_entry.delete(0, tk.END)

    def mainloop(self):
        self.screen.mainloop()


class MonsterLookupScreen:
    pass