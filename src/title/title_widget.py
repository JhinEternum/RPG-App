import tkinter as tk
from tkinter import ttk, font

from src.connection import get_search_entities


class TitleWidget:
    def __init__(self, **kwargs):
        self.create_title = kwargs['create_title'] if 'create_title' in kwargs else None
        widgets = kwargs['widgets']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None
        self.frame_id = kwargs['frame_id'] if 'frame_id' in kwargs else ''
        self.add_entity_frame = kwargs['add_entity_frame'] if 'add_entity_frame' in kwargs else None

        self.font = font.Font(size=11)

        self.characters = ['None'] + get_search_entities('', 'Character')
        self.npcs = ['None'] + get_search_entities('', 'NPC')
        self.monsters = ['None'] + get_search_entities('', 'Monster')

        # --- Attributes ---
        self.title = 'Title ' + self.frame_id
        self.name = tk.StringVar()
        self.character = tk.StringVar(value=self.characters)
        self.npc = tk.StringVar(value=self.npcs)
        self.monster = tk.StringVar(value=self.monsters)

        # --- Widgets ---
        self.character_entry = tk.Listbox()
        self.npc_entry = tk.Listbox()
        self.monster_entry = tk.Listbox()
        self.requirements_entry = tk.Text()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Title ---
        title_label = ttk.Label(
            widgets,
            text=self.title
        )
        title_label.grid(row=0, column=0, sticky="EW")

        title_separator = ttk.Separator(
            widgets
        )
        title_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

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

        self.character_entry = tk.Listbox(
            widgets,
            listvariable=self.character,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.character_entry.grid(row=3, column=1, sticky="EW")

        self.character_entry.select_set(0)

        character_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        character_scrollbar.config(command=self.character_entry.yview)
        character_scrollbar.grid(row=3, column=2, sticky="NS")

        self.character_entry.config(yscrollcommand=character_scrollbar.set)

        # --- NPC ---
        self.npc_entry = tk.Listbox(
            widgets,
            listvariable=self.npc,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.npc_entry.grid(row=4, column=1, sticky="EW")

        self.npc_entry.select_set(0)

        npc_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        npc_scrollbar.config(command=self.npc_entry.yview)
        npc_scrollbar.grid(row=4, column=2, sticky="NS")

        self.npc_entry.config(yscrollcommand=npc_scrollbar.set)

        # --- Monster ---
        self.monster_entry = tk.Listbox(
            widgets,
            listvariable=self.monster,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=4
        )
        self.monster_entry.grid(row=5, column=1, sticky="EW")

        self.monster_entry.select_set(0)

        monster_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        monster_scrollbar.config(command=self.monster_entry.yview)
        monster_scrollbar.grid(row=5, column=2, sticky="NS")

        self.monster_entry.config(yscrollcommand=monster_scrollbar.set)

        # --- Requirements ---
        requirements_label = ttk.Label(
            widgets,
            text="Requirements"
        )
        requirements_label.grid(row=6, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.requirements_entry.grid(row=6, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=6, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, 'None')

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=7, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=7
        )
        self.description_entry.grid(row=7, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=7, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def set_buttons(self, buttons) -> None:
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)

        create_button = ttk.Button(
            buttons,
            text='Create Title',
            command=self.create_title,
            cursor='hand2'
        )
        create_button.grid(row=1)

        add_button = ttk.Button(
            buttons,
            text='Add Title',
            command=self.add_entity_frame,
            cursor='hand2'
        )
        add_button.grid(row=2)
