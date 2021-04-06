import tkinter as tk

from gui import cr
from gui import damage
from gui import monsters
from gui import saves
from gui import spells


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
            cr_screen = cr.CRScreen()
        elif window.lower() == "dps":
            dps_screen = damage.DamageScreen()
        elif window.lower() == "instruct":
            info_screen = InfoScreen()
        elif window.lower() == "spells":
            spell_screen = spells.SpellScreen()
        elif window.lower() == "saves":
            save_screen = saves.SavingThrowScreen()
        elif window.lower() == "monster_lookup":
            monster_screen = monsters.MonsterLookupScreen()
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
        super().__init__(window)
        self.screen.title("Error")

    # Draws text onto the screen
    def draw_text(self, window):
        text = tk.Text(master=self.screen, height=20, width=45, relief="sunken", wrap="word", padx=5, pady=5)
        text.insert(tk.END, self.messages[window])
        text.pack()