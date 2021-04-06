import tkinter as tk

import damage

from gui import help


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
            error_screen = help.ErrorScreen("saves")
        finally:
            self.ability_modifier_entry.delete(0, tk.END)
            self.dc_entry.delete(0, tk.END)

    # Create an appropriate help screen when the help button is clicked
    def draw_help(self):
        helpscreen = help.HelpScreen("saves")