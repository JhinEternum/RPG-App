import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

from src.ability.create_ability import CreateAbility
from src.avatar.create_avatar import CreateAvatar
from src.images.image import *
from src.item.create_item import CreateItem
from src.proficiency.create_proficiency import CreateProficiency
from src.title.create_title import CreateTitle


class HomeWidget:
    def __init__(self, **kwargs):
        self.parent = kwargs['parent']
        self.create_entity = kwargs['create_entity']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.proficiencies_level = kwargs['proficiencies_level'] if 'proficiencies_level' in kwargs else None
        self.search = kwargs['search']
        self.set_battle = kwargs['set_battle']
        self.show_wiki = kwargs['show_wiki']

        self.ability_icon = get_ability()
        self.battle_icon = get_battle()
        self.sword_icon = get_sword()
        self.title_icon = get_title()
        self.proficiency_icon = get_proficiency()
        self.avatar_icon = get_avatar()
        self.search_icon = get_search()
        self.wiki_icon = get_wiki()

        self.type_values = ('Character', 'NPC', 'Monster', 'Proficiency', 'Armor', 'Weapon', 'Title', 'Ability', 'Wiki')

        self.name = tk.StringVar()
        self.type = tk.StringVar(value=self.type_values[0])

        self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text='Name',
            style='DarkTheme.TLabel'
        )
        name_label.grid(row=0, column=0)

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            style='DarkEntry.TEntry',
            width=90
        )
        name_entry.grid(row=0, column=1)

        # --- Type ---
        type_label = ttk.Label(
            widgets,
            text="Type",
            style='DarkTheme.TLabel'
        )
        type_label.grid(row=1, column=0)

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type,
            values=self.type_values,
            style='DarkCombobox.TCombobox',
            state="readonly",
            cursor='hand2'
        )
        type_entry.grid(row=1, column=1)

    def set_buttons(self, buttons) -> None:
        main = self.parent
        search_button = ttk.Button(
            buttons,
            text='  Search',
            command=self.search,
            style='DarkButton.TButton',
            image=self.search_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        search_button.grid(row=0)

        create_avatar_button = ttk.Button(
            buttons,
            text='  Create Avatar',
            command=lambda: self.create_entity(container=main.create_avatar, container_class=CreateAvatar,
                                               extra_frame=self.proficiencies_level),
            style='DarkButton.TButton',
            image=self.avatar_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        create_avatar_button.grid(row=1)

        create_item_button = ttk.Button(
            buttons,
            text='  Create Item',
            command=lambda: self.create_entity(container=main.create_item, container_class=CreateItem),
            style='DarkButton.TButton',
            image=self.sword_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )

        create_item_button.grid(row=2)

        create_ability_button = ttk.Button(
            buttons,
            text='  Create Ability',
            command=lambda: self.create_entity(container=main.create_ability, container_class=CreateAbility),
            style='DarkButton.TButton',
            image=self.ability_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        create_ability_button.grid(row=3)

        create_title_button = ttk.Button(
            buttons,
            text='  Create Title',
            command=lambda: self.create_entity(container=main.create_title, container_class=CreateTitle),
            style='DarkButton.TButton',
            image=self.title_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        create_title_button.grid(row=4)

        create_proficiency_button = ttk.Button(
            buttons,
            text='  Create Proficiency',
            command=lambda: self.create_entity(container=main.create_proficiency, container_class=CreateProficiency),
            style='DarkButton.TButton',
            image=self.proficiency_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        create_proficiency_button.grid(row=5)

        battle_button = ttk.Button(
            buttons,
            text=' Battle System',
            command=self.set_battle,
            style='DarkButton.TButton',
            image=self.battle_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        battle_button.grid(row=6)

        wiki_button = ttk.Button(
            buttons,
            text='  Wiki',
            command=lambda: self.show_wiki(factory='home'),
            style='DarkButton.TButton',
            image=self.wiki_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        wiki_button.grid(row=7)
