import tkinter as tk

from calculations import regressions

from gui import help


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
        help_screen = help.HelpScreen("crscreen")

    # Grabs data from entries and outputs an appropriate value for CR
    def calculate_cr(self):
        try:
            health = float(self.hp_entry.get())
            armor = float(self.ac_entry.get())
            self.cr_entry.delete(0, tk.END)
            self.cr_entry.insert(string=str(regressions.predict(target="cr", hp=health, ac=armor)), index=0)
        except ValueError:
            error_screen = help.ErrorScreen("crscreen")
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
            error_screen = help.ErrorScreen("crscreen")
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
            error_screen = help.ErrorScreen("crscreen")
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