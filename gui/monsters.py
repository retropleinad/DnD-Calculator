import tkinter as tk

from gui import help

from calculations import monster_lookup as lookup


# Class for the monster lookup screen GUI
class MonsterLookupScreen:

    # Declare labels, entries, and buttons
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title = "Monster Lookup"
        self.attributes = ("STR", "DEX", "CON", "INT", "WIS", "CHA")

        self.name_label = None
        self.hp_label = None
        self.speed_label = None
        self.cr_label = None
        self.type_label = None
        self.size_label = None
        self.alignment_label = None
        self.senses_label = None
        self.languages_label = None

        self.name_entry = None
        self.hp_entry = None
        self.speed_entry = None
        self.cr_entry = None
        self.type_entry = None
        self.size_entry = None
        self.alignment_entry = None
        self.senses_entry = None
        self.languages_entry = None
        self.attribute_entries = []

        self.search_button = None
        self.help_button = None

        self.draw_labels()
        self.draw_entries()
        self.draw_attributes()
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

    def draw_attributes(self):
        for i in range(0, 6):
            label = tk.Label(master=self.screen, text=self.attributes[i], width=15, height=1)
            entry = tk.Entry(master=self.screen, width=10)
            label.grid(row=i, column=2, padx=1, pady=5)
            entry.grid(row=i, column=3, padx=1, pady=5)
            self.attribute_entries.append(entry)

    def draw_buttons(self):
        self.search_button = tk.Button(master=self.screen, text="Search", width=10, height=1, command=self.search)
        self.help_button = tk.Button(master=self.screen, text="Help", width=10, height=1, command=self.draw_help)

        self.search_button.grid(row=0, column=4, padx=1, pady=1)
        self.help_button.grid(row=8, column=4, padx=1, pady=1)

    def search(self):
        try:
            name = self.name_entry.get()
            traits = lookup.get_traits(name)

            self.hp_entry.delete(0, tk.END)
            self.speed_entry.delete(0, tk.END)
            self.cr_entry.delete(0, tk.END)
            self.type_entry.delete(0, tk.END)
            self.size_entry.delete(0, tk.END)
            self.alignment_entry.delete(0, tk.END)
            self.senses_entry.delete(0, tk.END)
            self.languages_entry.delete(0, tk.END)

            self.hp_entry.insert(string=traits["hp"], index=0)
            self.speed_entry.insert(string=traits["speed"], index=0)
            self.cr_entry.insert(string=traits["cr"], index=0)
            self.type_entry.insert(string=traits["type"], index=0)
            self.size_entry.insert(string=traits["size"], index=0)
            self.alignment_entry.insert(string=traits["alignment"], index=0)
            self.senses_entry.insert(string=traits["senses"], index=0)
            self.languages_entry.insert(string=traits["languages"], index=0)

            attributes = lookup.get_attributes(name)
            print(len(attributes))
            for i in range(0, 6):
                self.attribute_entries[i].delete(0, tk.END)
                self.attribute_entries[i].insert(string=attributes[i], index=0)
            
        except OSError or TypeError:
            error_screen = help.ErrorScreen("monster_lookup")

    def draw_help(self):
        helpscreen = help.HelpScreen("monster_lookup")