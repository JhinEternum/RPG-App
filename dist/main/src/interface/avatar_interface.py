import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.connection.database import get_search_entities
from src.images.image import *
from src.interface.interface_functions import generate_classes
from src.interface.interface_template import InterfaceTemplate
from src.proficiency.proficiency import Proficiency


class AvatarInterface(InterfaceTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_types = {1: 'Armor', 2: 'Weapon'}

        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.widgets = widgets

        print(self.entity)

        self.avatar_icon = get_avatar()
        self.hp_icon = get_hp()
        self.strength_icon = get_strength()
        self.magic_icon = get_magic()
        self.adrenaline_icon = get_adrenaline()
        self.physical_icon = get_physical()

        self.armor_icon = get_armors()
        self.sword_icon = get_sword()

        self.item_icons = {1: self.armor_icon, 2: self.sword_icon}

        self.entity: Avatar

        self.name = '  ' + self.entity.name
        self.type = self.entity.type
        self.strength_lv = f'  Strength  {self.entity.strength_lv}'
        self.magic_lv = f'  Magic  {self.entity.magic_lv}'
        self.health = '  HP  ' + self.entity.health
        self.adrenaline = '  Adrenaline  ' + self.entity.adrenaline
        self._class = self.entity.classes
        self.physical_ability = '  Physical Ab  ' + self.entity.physical_ability
        self.items = self.entity.items
        self.titles = self.entity.titles
        self.abilities = self.entity.abilities
        self.proficiencies = self.entity.proficiencies
        self.description = self.entity.description

        self.set_widgets(widgets)
        if buttons:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name = ttk.Label(
            widgets,
            text=self.name,
            image=self.avatar_icon,
            compound=tk.LEFT
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            widgets
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        strength_lv = ttk.Label(
            widgets,
            text=self.strength_lv,
            image=self.strength_icon,
            compound=tk.LEFT
        )
        strength_lv.grid(row=2, column=0, sticky='EW')

        magic_lv = ttk.Label(
            widgets,
            text=self.magic_lv,
            image=self.magic_icon,
            compound=tk.LEFT
        )
        magic_lv.grid(row=3, column=0, sticky='EW')

        health = ttk.Label(
            widgets,
            text=self.health,
            image=self.hp_icon,
            compound=tk.LEFT
        )
        health.grid(column=0, sticky="EW")

        adrenaline = ttk.Label(
            widgets,
            text=self.adrenaline,
            image=self.adrenaline_icon,
            compound=tk.LEFT
        )
        adrenaline.grid(column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            widgets,
            text=self.physical_ability,
            image=self.physical_icon,
            compound=tk.LEFT
        )
        physical_ability.grid(column=0, sticky="NSEW")

        class_ = ttk.Label(
            widgets,
            text=generate_classes(self._class)
        )
        class_.grid(column=0, sticky="NSEW")

        items = ttk.Label(
            widgets,
            text='Items'
        )
        items.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        # ITEM
        self.set_items(widgets)

        titles = ttk.Label(
            widgets,
            text='Titles'
        )
        titles.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        # TITLE
        self.set_title(widgets)

        abilities = ttk.Label(
            widgets,
            text='Abilities'
        )
        abilities.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        # ABILITY
        self.set_ability(widgets)

        proficiencies = ttk.Label(
            widgets,
            text='Proficiencies'
        )
        proficiencies.grid(column=0, sticky="NSEW")

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        # PROFICIENCY
        self.set_proficiencies(widgets)

        description = ttk.Label(
            widgets,
            text='Description'
        )
        description.grid(column=0, sticky="EW")

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        description_description = ttk.Label(
            widgets,
            text=self.description
        )
        description_description.grid(column=0, sticky='EW')

        self.bind_label([physical_ability, description_description])

    def set_items(self, widgets):
        if len(self.items) > 0:
            for item in self.items:
                item_type = self.item_types[item.type]

                btn = ttk.Button(
                    widgets,
                    text=f'  {item.name}',
                    command=lambda current_item=item: self.show_entity(current_item, item_type),
                    style='DarkButton.TButton',
                    image=self.item_icons[item.type],
                    compound=tk.LEFT,
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

    def set_title(self, widgets):
        if len(self.titles) > 0:
            for title in self.titles:
                btn = ttk.Button(
                    widgets,
                    text=f'{title.name}',
                    command=lambda current_title=title: self.show_entity(current_title, 'Title'),
                    style='DarkButton.TButton',
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

    def set_ability(self, widgets):
        if len(self.abilities) > 0:
            for ability in self.abilities:
                ability_name = ability.name
                btn = ttk.Button(
                    widgets,
                    text=f'{ability_name}',
                    command=lambda current_ability=ability: self.show_entity(current_ability, 'Ability'),
                    style='DarkButton.TButton',
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

    def set_proficiencies(self, widgets):
        ranks = ('None', 'S', 'A', 'B')
        if len(self.proficiencies) > 0:
            for proficiency in self.proficiencies:
                proficiency: Proficiency
                proficiency_rank = ranks[int(proficiency.rank)]

                text = f'  {proficiency.name} {proficiency.level}'

                if proficiency_rank != 'None':
                    text = f'  {proficiency_rank}  •  {proficiency.name} {proficiency.level}'

                btn = ttk.Button(
                    widgets,
                    text=text,
                    command=lambda current_proficiency=proficiency: self.show_entity(
                        current_proficiency,
                        'Proficiency'
                    ),
                    style='DarkButton.TButton',
                    image=proficiency.icon if proficiency.icon != 'none' else None,
                    compound=tk.LEFT,
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

    def set_buttons(self, buttons) -> None:
        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        search_result = get_search_entities(self.search_name, self.search_type)

        edit_button = ttk.Button(
            buttons,
            text='  Edit',
            command=lambda: self.edit(
                name=self.search_name,
                entity=self.entity,
                type_=self.search_type
            ),
            style='DarkButton.TButton',
            image=self.edit_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        edit_button.grid(row=1)

        back_button = ttk.Button(
            buttons,
            text='  Back',
            command=lambda: self.back(
                False,
                name=self.search_name,
                entities=search_result,
                type_=self.search_type
            ),
            style='DarkButton.TButton',
            image=self.back_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        back_button.grid(row=2)

    def show_entity(self, entity, entity_type) -> None:
        parent_name = self.entity.name
        parent_type = self.search_type

        self.show_interface(
            name=self.search_name,
            entity=entity,
            type_=entity_type,
            parent_name=parent_name,
            parent_type=parent_type,
            go_parent=True
        )
