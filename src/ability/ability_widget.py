import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_search_entities
from src.connection.handle_items import get_items


class AbilityWidget:
    def __init__(self, **kwargs):
        self.create_ability = kwargs['create_ability'] if 'create_ability' in kwargs else None
        widgets = kwargs['widgets']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None
        self.frame_id = kwargs['frame_id'] if 'frame_id' in kwargs else ''
        self.add_entity_frame = kwargs['add_entity_frame'] if 'add_entity_frame' in kwargs else None

        self.font = font.Font(size=11)

        self.types_ = ('None', 'Character', 'NPC', 'Monster')

        self.characters = ['None', 'Character'] + get_search_entities('', 'Character')
        self.npcs = ['None', 'NPC'] + get_search_entities('', 'NPC')
        self.monsters = ['None', 'Monster'] + get_search_entities('', 'Monster')
        self.items = ['None', 'Item'] + [items['name'] for items in get_items()]

        # --- Attributes ---
        self.ability = 'Ability ' + self.frame_id
        self.name = tk.StringVar()
        self.casting = tk.StringVar(value='None')
        self.components = tk.StringVar(value='None')

        self.character = tk.StringVar(value=self.characters[1])
        self.npc = tk.StringVar(value=self.npcs[0])
        self.monster = tk.StringVar(value=self.monsters[0])
        self.item = tk.StringVar(value=self.items[0])

        # --- Widgets ---
        self.character_menu = ttk.Combobox()
        self.npc_menu = ttk.Combobox()
        self.monster_menu = ttk.Combobox()
        self.item_menu = ttk.Combobox()

        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets):
        # --- Ability ---
        ability_label = ttk.Label(
            widgets,
            text=self.ability
        )
        ability_label.grid(row=0, column=0, sticky="EW")

        ability_separator = ttk.Separator(
            widgets
        )
        ability_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text="Name"
        )
        name_label.grid(row=2, column=0, sticky="EW")

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=2, column=1, sticky="EW")

        # --- User ---
        user_label = ttk.Label(
            widgets,
            text="User"
        )
        user_label.grid(row=3, column=0, sticky="EW")

        self.character_menu = ttk.Combobox(
            widgets,
            name='character',
            textvariable=self.character,
            values=self.characters,
            state="readonly"
        )
        self.character_menu.grid(row=3, column=1, sticky="EW")

        # --- NPC ---
        self.npc_menu = ttk.Combobox(
            widgets,
            name='npc',
            textvariable=self.npc,
            values=self.npcs,
            state="readonly"
        )
        self.npc_menu.grid(row=4, column=1, sticky="EW")

        # --- Monster ---
        self.monster_menu = ttk.Combobox(
            widgets,
            name='monster',
            textvariable=self.monster,
            values=self.monsters,
            state="readonly"
        )
        self.monster_menu.grid(row=5, column=1, sticky="EW")

        # --- Item ---
        self.item_menu = ttk.Combobox(
            widgets,
            name='item',
            textvariable=self.item,
            values=self.items,
            state="readonly"
        )
        self.item_menu.grid(row=6, column=1, sticky="EW")

        self.character_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.npc_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.monster_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.item_menu.bind("<<ComboboxSelected>>", self.selected_value)

        # --- Casting ---
        casting_label = ttk.Label(
            widgets,
            text="Casting"
        )
        casting_label.grid(row=7, column=0, sticky="EW")

        casting_entry = ttk.Entry(
            widgets,
            textvariable=self.casting,
            width=60
        )
        casting_entry.grid(row=7, column=1, sticky="EW")

        # --- Components ---
        components_label = ttk.Label(
            widgets,
            text="Components"
        )
        components_label.grid(row=8, column=0, sticky="EW")

        components_entry = ttk.Entry(
            widgets,
            textvariable=self.components,
            width=60
        )
        components_entry.grid(row=8, column=1, sticky="EW")

        # --- Requirements ---
        requirements_label = ttk.Label(
            widgets,
            text="Requirements"
        )
        requirements_label.grid(row=9, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            widgets,
            width=1,
            height=3
        )
        self.requirements_entry.grid(row=9, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=9, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, 'None')

        # --- Conditions ---
        conditions_label = ttk.Label(
            widgets,
            text="Conditions"
        )
        conditions_label.grid(row=10, column=0, sticky="EW")

        self.conditions_entry = tk.Text(
            widgets,
            width=1,
            height=3
        )
        self.conditions_entry.grid(row=10, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=10, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, 'None')

        # --- Effects ---
        effects_label = ttk.Label(
            widgets,
            text="Effects"
        )
        effects_label.grid(row=11, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            widgets,
            width=1,
            height=10
        )
        self.effects_entry.grid(row=11, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=11, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, 'None')

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=12, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.description_entry.grid(row=12, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=12, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def set_buttons(self, buttons):
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)

        create_button = ttk.Button(
            buttons,
            text='Create Ability',
            command=self.create_ability,
            cursor='hand2'
        )
        create_button.grid(row=1)

        add_button = ttk.Button(
            buttons,
            text='Add Ability',
            command=self.add_entity_frame,
            cursor='hand2'
        )
        add_button.grid(row=2)

    def selected_value(self, event):
        selected_entity = str(event.widget).split(".")[-1]

        if selected_entity == 'character':
            self.npc_menu.current(0)
            self.monster_menu.current(0)
            self.item_menu.current(0)
        elif selected_entity == 'npc':
            self.character_menu.current(0)
            self.monster_menu.current(0)
            self.item_menu.current(0)
        elif selected_entity == 'monster':
            self.character_menu.current(0)
            self.npc_menu.current(0)
            self.item_menu.current(0)
        elif selected_entity == 'item':
            self.character_menu.current(0)
            self.npc_menu.current(0)
            self.monster_menu.current(0)
