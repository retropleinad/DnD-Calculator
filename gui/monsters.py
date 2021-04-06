import tkinter as tk


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

    def draw_buttons(self):
        pass