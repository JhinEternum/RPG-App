import tkinter as tk
from tkinter import ttk, font

from src.avatar.avatar_properties import get_entities_names
from src.connection.handle_abilities import get_abilities_by_type
from src.connection.handle_classes import get_classes
from src.connection.handle_items import get_specific_items
from src.connection.handle_proficiencies import get_proficiencies
from src.connection.handle_titles import get_titles


class AvatarWidget:
    def __init__(self, **kwargs):
        self.set_proficiencies = kwargs['set_proficiencies']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.font = font.Font(size=11)

        self.type_values = ('Character', 'NPC', 'Monster')

        self.classes_total = get_classes()
        self.classes = ['None'] + get_entities_names(self.classes_total)

        self.armors_total = get_specific_items('', 1)
        self.armors = ['None'] + get_entities_names(self.armors_total)

        self.weapons_total = get_specific_items('', 2)
        self.weapons = ['None'] + get_entities_names(self.weapons_total)

        self.titles_total = get_titles()
        self.titles = ['None'] + get_entities_names(self.titles_total)

        self.abilities_total = get_abilities_by_type(1) + get_abilities_by_type(2) + get_abilities_by_type(3)
        self.abilities = ['None'] + get_entities_names(self.abilities_total)

        self.proficiencies_total = get_proficiencies()
        self.proficiencies = ['None'] + get_entities_names(self.proficiencies_total)

        self.lv_values = ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5')

        # --- Attributes ---
        self.name = tk.StringVar()
        self.strength_lv = tk.StringVar(value=self.lv_values[0])
        self.magic_lv = tk.StringVar(value=self.lv_values[0])
        self.health = tk.StringVar(value=0)
        self.type = tk.StringVar(value=self.type_values[0])
        self.adrenaline = tk.StringVar(value=0)
        self.class_ = tk.StringVar(value=self.classes)
        self.armor = tk.StringVar(value=self.armors[0])
        self.weapon = tk.StringVar(value=self.weapons)
        self.physical_ability = tk.StringVar(value='None')
        self.title = tk.StringVar(value=self.titles)
        self.ability = tk.StringVar(value=self.abilities)
        self.proficiency = tk.StringVar(value=self.proficiencies)

        # --- Widgets ---
        self.class_entry = tk.Listbox()
        self.weapon_entry = tk.Listbox()
        self.title_entry = tk.Listbox()
        self.ability_entry = tk.Listbox()
        self.proficiency_entry = tk.Listbox()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text='Name'
        )
        name_label.grid(row=0, column=0, sticky='EW')

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=0, column=1, sticky='EW')

        # --- Type ---
        type_label = ttk.Label(
            widgets,
            text='Type'
        )
        type_label.grid(row=1, column=0, sticky='EW')

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type,
            values=self.type_values,
            state='readonly'
        )
        type_entry.grid(row=1, column=1, sticky='EW')

        # --- Strength Level ---
        strength_lv_label = ttk.Label(
            widgets,
            text='Strength Lv'
        )
        strength_lv_label.grid(row=2, column=0, sticky='EW')

        strength_lv_entry = ttk.Combobox(
            widgets,
            textvariable=self.strength_lv,
            values=self.lv_values,
            state='readonly'
        )
        strength_lv_entry.grid(row=2, column=1, sticky='EW')

        # --- Magic Level ---
        magic_lv_label = ttk.Label(
            widgets,
            text='Magic Lv'
        )
        magic_lv_label.grid(row=3, column=0, sticky='EW')

        magic_lv_entry = ttk.Combobox(
            widgets,
            textvariable=self.magic_lv,
            values=self.lv_values,
            state='readonly'
        )
        magic_lv_entry.grid(row=3, column=1, sticky='EW')

        # --- Health ---
        health_label = ttk.Label(
            widgets,
            text='Health'
        )
        health_label.grid(row=4, column=0, sticky='EW')

        health_entry = ttk.Entry(
            widgets,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=4, column=1, sticky='EW')

        # --- Adrenaline ---
        adrenaline_label = ttk.Label(
            widgets,
            text='Adrenaline'
        )
        adrenaline_label.grid(row=5, column=0, sticky='EW')

        adrenaline_entry = ttk.Entry(
            widgets,
            textvariable=self.adrenaline
        )
        adrenaline_entry.grid(row=5, column=1, sticky='EW')

        # --- Class ---
        class_label = ttk.Label(
            widgets,
            text='Class'
        )
        class_label.grid(row=6, column=0, sticky='EW')

        self.class_entry = tk.Listbox(
            widgets,
            listvariable=self.class_,
            selectmode='extended',
            exportselection=False,
            selectbackground='#2CCC5B',
            highlightcolor='#1DE557',
            font=self.font,
            width=1,
            height=5
        )
        self.class_entry.grid(row=6, column=1, sticky='EW')

        self.class_entry.select_set(0)

        class_scrollbar = ttk.Scrollbar(widgets, orient='vertical')
        class_scrollbar.config(command=self.class_entry.yview)
        class_scrollbar.grid(row=6, column=2, sticky='NS')

        self.class_entry.config(yscrollcommand=class_scrollbar.set)

        # --- Armor ---
        armor_label = ttk.Label(
            widgets,
            text='Armor'
        )
        armor_label.grid(row=7, column=0, sticky='EW')

        armor_entry = ttk.Combobox(
            widgets,
            textvariable=self.armor,
            values=self.armors,
            state='readonly'
        )
        armor_entry.grid(row=7, column=1, sticky='EW')

        # --- Weapon ---
        weapon_label = ttk.Label(
            widgets,
            text='Weapon'
        )
        weapon_label.grid(row=8, column=0, sticky='EW')

        self.weapon_entry = tk.Listbox(
            widgets,
            listvariable=self.weapon,
            selectmode='extended',
            exportselection=False,
            selectbackground='#2CCC5B',
            highlightcolor='#1DE557',
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=8, column=1, sticky='EW')

        self.weapon_entry.select_set(0)

        weapon_scrollbar = ttk.Scrollbar(widgets, orient='vertical')
        weapon_scrollbar.config(command=self.weapon_entry.yview)
        weapon_scrollbar.grid(row=8, column=2, sticky='NS')

        self.weapon_entry.config(yscrollcommand=weapon_scrollbar.set)

        # --- Physical Ability ---
        physical_ability_label = ttk.Label(
            widgets,
            text='Physical Ab.'
        )
        physical_ability_label.grid(row=9, column=0, sticky='EW')

        physical_ability_entry = ttk.Entry(
            widgets,
            textvariable=self.physical_ability
        )
        physical_ability_entry.grid(row=9, column=1, sticky='EW')

        # --- Title ---
        title_label = ttk.Label(
            widgets,
            text='Title'
        )
        title_label.grid(row=10, column=0, sticky="EW")

        self.title_entry = tk.Listbox(
            widgets,
            listvariable=self.title,
            selectmode='extended',
            exportselection=False,
            selectbackground='#2CCC5B',
            highlightcolor='#1DE557',
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=10, column=1, sticky='EW')
        self.title_entry.select_set(0)

        title_scrollbar = ttk.Scrollbar(widgets, orient='vertical')
        title_scrollbar.config(command=self.title_entry.yview)
        title_scrollbar.grid(row=10, column=2, sticky='NS')

        self.title_entry.config(yscrollcommand=title_scrollbar.set)

        # --- Ability ---
        ability_label = ttk.Label(
            widgets,
            text='Ability'
        )
        ability_label.grid(row=11, column=0, sticky='EW')

        self.ability_entry = tk.Listbox(
            widgets,
            listvariable=self.ability,
            selectmode='extended',
            exportselection=False,
            selectbackground='#2CCC5B',
            highlightcolor='#1DE557',
            font=self.font,
            width=1,
            height=5
        )
        self.ability_entry.grid(row=11, column=1, sticky='EW')

        self.ability_entry.select_set(0)

        ability_scrollbar = ttk.Scrollbar(widgets, orient='vertical')
        ability_scrollbar.config(command=self.ability_entry.yview)
        ability_scrollbar.grid(row=11, column=2, sticky='NS')

        self.ability_entry.config(yscrollcommand=ability_scrollbar.set)

        # --- Proficiency ---
        proficiency_label = ttk.Label(
            widgets,
            text='Proficiency'
        )
        proficiency_label.grid(row=12, column=0, sticky="EW")

        self.proficiency_entry = tk.Listbox(
            widgets,
            listvariable=self.proficiency,
            selectmode='extended',
            exportselection=False,
            selectbackground='#2CCC5B',
            highlightcolor='#1DE557',
            font=self.font,
            width=1,
            height=5
        )
        self.proficiency_entry.grid(row=12, column=1, sticky='EW')

        self.proficiency_entry.select_set(0)

        proficiency_scrollbar = ttk.Scrollbar(widgets, orient='vertical')
        proficiency_scrollbar.config(command=self.proficiency_entry.yview)
        proficiency_scrollbar.grid(row=12, column=2, sticky='NS')

        self.proficiency_entry.config(yscrollcommand=proficiency_scrollbar.set)

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text='Description'
        )
        description_label.grid(row=13, column=0, sticky='EW')

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.description_entry.grid(row=13, column=1, sticky='EW')

        description_scroll = ttk.Scrollbar(
            widgets,
            orient='vertical',
            command=self.description_entry.yview
        )
        description_scroll.grid(row=13, column=2, sticky='ns')

        self.description_entry['yscrollcommand'] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def set_buttons(self, buttons) -> None:
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)

        create_button = ttk.Button(
            buttons,
            text='Create Avatar',
            command=self.set_proficiencies,
            cursor='hand2'
        )
        create_button.grid(row=1)
