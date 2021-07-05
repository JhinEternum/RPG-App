import tkinter as tk
from tkinter import ttk

from src.ability.create_ability import CreateAbility
from src.avatar.create_avatar import CreateAvatar
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
        self.show_wiki = kwargs['show_wiki']

        self.type_values = ('Character', 'NPC', 'Monster', 'Proficiency', 'Armor', 'Weapon', 'Title', 'Ability', 'Wiki')

        self.name = tk.StringVar()
        self.type = tk.StringVar(value=self.type_values[0])

        self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text='Name'
        )
        name_label.grid(row=0, column=0)

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=90
        )
        name_entry.grid(row=0, column=1)

        # --- Type ---
        type_label = ttk.Label(
            widgets,
            text="Type"
        )
        type_label.grid(row=1, column=0)

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type,
            values=self.type_values,
            state="readonly"
        )
        type_entry.grid(row=1, column=1)

    def set_buttons(self, buttons) -> None:
        main = self.parent.parent
        search_button = ttk.Button(
            buttons,
            text='Search',
            command=self.search,
            cursor='hand2'
        )
        search_button.grid(row=0)

        create_avatar_button = ttk.Button(
            buttons,
            text='Crate Avatar',
            command=lambda: self.create_entity(container=main.create_avatar, container_class=CreateAvatar,
                                               extra_frame=self.proficiencies_level),
            cursor='hand2'
        )
        create_avatar_button.grid(row=1)

        create_item_button = ttk.Button(
            buttons,
            text='Crate Item',
            command=lambda: self.create_entity(container=main.create_item, container_class=CreateItem),
            cursor='hand2'
        )

        create_item_button.grid(row=2)

        create_ability_button = ttk.Button(
            buttons,
            text='Crate Ability',
            command=lambda: self.create_entity(container=main.create_ability, container_class=CreateAbility),
            cursor='hand2'
        )
        create_ability_button.grid(row=3)

        create_title_button = ttk.Button(
            buttons,
            text='Crate Title',
            command=lambda: self.create_entity(container=main.create_title, container_class=CreateTitle),
            cursor='hand2'
        )
        create_title_button.grid(row=4)

        create_proficiency_button = ttk.Button(
            buttons,
            text='Crate Proficiency',
            command=lambda: self.create_entity(container=main.create_proficiency, container_class=CreateProficiency),
            cursor='hand2'
        )
        create_proficiency_button.grid(row=5)

        wiki_button = ttk.Button(
            buttons,
            text='Wiki',
            command=lambda: self.show_wiki(factory='home'),
            cursor='hand2'
        )
        wiki_button.grid(row=6)
