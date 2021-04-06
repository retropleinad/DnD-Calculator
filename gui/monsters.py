import tkinter as tk

from gui import help


# Class for the monster lookup screen GUI
class MonsterLookupScreen:

    # Declare labels, entries, and buttons
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title = "Monster Lookup"

        self.name_label = None
        self.hp_label = None
        self.speed_label = None
        self.cr_label = None
        self.type_label = None
        self.size_label = None
        self.alignment_label = None
        self.senses_label = None
        self.languages_label = None

        # Attribute labels and entries are both in arrays, because they for sure are grouped together
        # self.attributes contains the labels for self.attribute_labels
        self.attribute_labels = []
        self.attributes = ("STR", "DEX", "CON", "INT", "WIS", "CHA")
        self.attribute_entries = []

        self.name_entry = None
        self.hp_entry = None
        self.speed_entry = None
        self.cr_entry = None
        self.type_entry = None
        self.size_entry = None
        self.alignment_entry = None
        self.senses_entry = None
        self.languages_entry = None

        self.search_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_buttons()

    def draw_labels(self):
        self.name_label = tk.Label(master=self.screen, text="Enter Name:", width=15, height=1)
        self.hp_label = tk.Label(master=self.screen, text="HP", width=15, height=1)
        self.speed_label = tk.Label(master=self.screen, text="Speed", width=15, height=1)
        self.cr_label = tk.Label(master=self.screen, text="CR", width=15, height=1)
        self.type_label = tk.Label(master=self.screen, text="Type", width=15, height=1)
        self.size_label = tk.Label(master=self.screen, text="Size", width=15, height=1)
        self.alignment_label = tk.Label(master=self.screen, text="Alignment", width=15, height=1)
        self.senses_label = tk.Label(master=self.screen, text="Senses", width=15, height=1)
        self.languages_label = tk.Label(master=self.screen, text="Languages", width=15, height=1)

        for i in range(0, 6):
            label = tk.Label(master=self.screen, text=self.attributes[i], width=15, height=1)
            self.attribute_labels.append(label)

        self.name_label.grid(row=0, column=0, padx=1, pady=5)
        self.hp_label.grid(row=1, column=0, padx=1, pady=5)
        self.speed_label.grid(row=2, column=0, padx=1, pady=5)
        self.cr_label.grid(row=3, column=0, padx=1, pady=5)
        self.type_label.grid(row=4, column=0, padx=1, pady=5)
        self.size_label.grid(row=5, column=0, padx=1, pady=5)
        self.alignment_label.grid(row=6, column=0, padx=1, pady=5)
        self.senses_label.grid(row=7, column=0, padx=1, pady=5)
        self.languages_label.grid(row=8, column=0, padx=1, pady=5)

    def draw_entries(self):
        self.name_entry = tk.Entry(master=self.screen, width=10)
        self.hp_entry = tk.Entry(master=self.screen, width=10)
        self.speed_entry = tk.Entry(master=self.screen, width=10)
        self.cr_entry = tk.Entry(master=self.screen, width=10)
        self.type_entry = tk.Entry(master=self.screen, width=10)
        self.size_entry = tk.Entry(master=self.screen, width=10)
        self.alignment_entry = tk.Entry(master=self.screen, width=10)
        self.senses_entry = tk.Entry(master=self.screen, width=10)
        self.languages_entry = tk.Entry(master=self.screen, width=10)

        self.name_entry.grid(row=0, column=1, padx=1, pady=1)
        self.hp_entry.grid(row=1, column=1, padx=1, pady=1)
        self.speed_entry.grid(row=2, column=1, padx=1, pady=1)
        self.cr_entry.grid(row=3, column=1, padx=1, pady=1)
        self.type_entry.grid(row=4, column=1, padx=1, pady=1)
        self.size_entry.grid(row=5, column=1, padx=1, pady=1)
        self.alignment_entry.grid(row=6, column=1, padx=1, pady=1)
        self.senses_entry.grid(row=7, column=1, padx=1, pady=1)
        self.languages_entry.grid(row=8, column=1, padx=1, pady=1)

    def draw_buttons(self):
        self.search_button = tk.Button(master=self.screen, text="Search", width=10, height=1, command=self.search)
        self.help_button = tk.Button(master=self.screen, text="Help", width=10, height=1, command=self.draw_help)
        
        self.search_button.grid(row=0, column=2, padx=1, pady=1)
        self.help_button.grid(row=8, column=2, padx=1, pady=1)

    def search(self):
        pass

    def draw_help(self):
        helpscreen = help.HelpScreen("monster_lookup")