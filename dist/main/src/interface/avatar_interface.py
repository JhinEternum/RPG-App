from tkinter import ttk

from src.connection import get_user_classes, get_user_items, get_user_titles, get_user_abilities, \
    get_user_proficiencies, get_search_entities
from src.interface.interface_functions import generate_classes


class AvatarInterface:
    def __init__(self, **kwargs):
        self.item_types = {1: 'Armor', 2: 'Weapon'}

        self.search_name = kwargs['name']
        self.search_type = kwargs['type_']

        self.entity = kwargs['entity']
        self.back = kwargs['back']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']
        self.show_interface = kwargs['show_interface']
        self.edit = kwargs['edit']

        self.name = self.entity['name']
        self.type = self.entity['type']
        self.strength_lv = f'Strength Level:  {self.entity["strength_lv"]}'
        self.magic_lv = f'Magic Level:  {self.entity["magic_lv"]}'
        self.health = 'Health:  ' + self.entity['health']
        self.adrenaline = 'Adrenaline:  ' + self.entity['adrenaline']
        self.class_ = get_user_classes(self.name)
        self.physical_ability = 'Physical Ability:  ' + self.entity['physical_ability']
        self.items = get_user_items(self.name)
        self.titles = get_user_titles(self.name)
        self.abilities = get_user_abilities(self.name)
        self.proficiency = get_user_proficiencies(self.name)
        self.description = self.entity['description']

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name = ttk.Label(
            widgets,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            widgets
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        strength_lv = ttk.Label(
            widgets,
            text=self.strength_lv
        )
        strength_lv.grid(row=2, column=0, sticky='EW')

        magic_lv = ttk.Label(
            widgets,
            text=self.magic_lv
        )
        magic_lv.grid(row=3, column=0, sticky='EW')

        health = ttk.Label(
            widgets,
            text=self.health
        )
        health.grid(column=0, sticky="EW")

        adrenaline = ttk.Label(
            widgets,
            text=self.adrenaline
        )
        adrenaline.grid(column=0, sticky="NSEW")

        physical_ability = ttk.Label(
            widgets,
            text=self.physical_ability
        )
        physical_ability.grid(column=0, sticky="NSEW")

        class_ = ttk.Label(
            widgets,
            text=generate_classes(self.class_)
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

        if len(self.items) > 0:
            for item in self.items:
                item_type = self.item_types[item['type']]
                item_name = item['name']

                btn = ttk.Button(
                    widgets,
                    text=f'{item_type}  -  {item_name}',
                    command=lambda current_item=item: self.show_entity(current_item, item_type),
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

        titles = ttk.Label(
            widgets,
            text='Titles'
        )
        titles.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        if len(self.titles) > 0:
            for title in self.titles:
                title_name = title['name']

                btn = ttk.Button(
                    widgets,
                    text=f'{title_name}',
                    command=lambda current_title=title: self.show_entity(current_title, 'Title'),
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

        abilities = ttk.Label(
            widgets,
            text='Abilities'
        )
        abilities.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        if len(self.abilities) > 0:
            for ability in self.abilities:
                ability_name = ability['name']

                btn = ttk.Button(
                    widgets,
                    text=f'{ability_name}',
                    command=lambda current_ability=ability: self.show_entity(current_ability, 'Ability'),
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

        proficiency = ttk.Label(
            widgets,
            text='Proficiencies'
        )
        proficiency.grid(column=0, sticky="NSEW")

        separator = ttk.Separator(
            widgets
        )
        separator.grid(columnspan=1, sticky='EW')

        ranks = ('None', 'S', 'A', 'B')

        if len(self.proficiency) > 0:
            for proficiency in self.proficiency:
                proficiency_name = proficiency['name']
                proficiency_level = proficiency['level']
                proficiency_rank = ranks[int(proficiency['rank'])]

                text = f'{proficiency_name} {proficiency_level}'

                if proficiency_rank != 'None':
                    text = f'{proficiency_rank} - {proficiency_name} {proficiency_level}'

                btn = ttk.Button(
                    widgets,
                    text=text,
                    command=lambda current_proficiency=proficiency: self.show_entity(
                        current_proficiency,
                        'Proficiency'
                    ),
                    cursor='hand2'
                )
                btn.grid(column=0, sticky="NSEW")

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

    def set_buttons(self, buttons) -> None:
        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        search_result = get_search_entities(self.search_name, self.search_type)

        edit_button = ttk.Button(
            buttons,
            text='Edit',
            command=lambda: self.edit(
                name=self.search_name,
                entity=self.entity,
                type_=self.search_type
            ),
            cursor='hand2'
        )
        edit_button.grid(row=1)

        back_button = ttk.Button(
            buttons,
            text='← Back',
            command=lambda: self.back(
                False,
                name=self.search_name,
                entities=search_result,
                type_=self.search_type
            ),
            cursor='hand2'
        )
        back_button.grid(row=2)

    def show_entity(self, entity, entity_type) -> None:
        parent_name = self.name
        parent_type = self.search_type

        self.show_interface(
            name=self.search_name,
            entity=entity,
            type_=entity_type,
            parent_name=parent_name,
            parent_type=parent_type,
            go_parent=True
        )
