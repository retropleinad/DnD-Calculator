import tkinter as tk
import tksheet

import damage

from gui import help


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
            error_screen = help.ErrorScreen("damage")
        finally:
            self.target_ac_entry.delete(0, tk.END)
            self.target_ac_entry.insert(string="0", index=0)

            self.number_turns_entry.delete(0, tk.END)
            self.number_turns_entry.insert(string="0", index=0)

            self.draw_table()

    # When the user clicks the help button, create a help screen
    def draw_help(self):
        help_screen = help.HelpScreen("damage")

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
            error_screen = help.ErrorScreen("attack")
        finally:
            self.max_dice_entry.delete(0, tk.END)
            self.hit_modifier_entry.delete(0, tk.END)
            self.damage_modifier_entry.delete(0, tk.END)
            self.number_turns_entry.delete(0, tk.END)
            self.attacks_turn_entry.delete(0, tk.END)

    # Draw the help screen when the help button is clicked
    def draw_help(self):
        help_screen = help.HelpScreen("attack")

    def mainloop(self):
        self.screen.mainloop()


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
        help_screen = help.HelpScreen("damage_saves")

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
            error_screen = help.ErrorScreen("damage_saves")
        finally:
            self.ability_modifier_entry.delete(0, tk.END),
            self.dc_entry.delete(0, tk.END),
            self.max_dice_entry.delete(0, tk.END),
            self.number_turns_entry.delete(0, tk.END),
            self.attacks_turn_entry.delete(0, tk.END)

    def mainloop(self):
        self.screen.mainloop()