import tkinter as tk
from tkinter import ttk

from src.connection.database import get_search_entities, get_entity
from src.images.image import get_ability
from src.interface.interface_template import InterfaceTemplate


class AbilityInterface(InterfaceTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.abilities_type = {1: 'Character Ability', 2: 'NPC Ability', 3: 'Monster Ability', 4: 'Item Ability'}

        self.ability_icon = get_ability()

        print(self.entity)
        print(self.entity.type)

        self.set_widgets(widgets)
        if buttons:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name = ttk.Label(
            widgets,
            text='  ' + self.entity.name,
            image=self.ability_icon,
            compound=tk.LEFT
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            widgets
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Type ---

        type_ = ttk.Label(
            widgets,
            text='Type:  ' + self.abilities_type[self.entity.type]
        )
        type_.grid(column=0, sticky="EW")

        # --- Casting ---

        casting = ttk.Label(
            widgets,
            text='Casting:  ' + self.entity.casting
        )
        casting.grid(column=0, sticky="EW")

        # --- Components ---

        components = ttk.Label(
            widgets,
            text='Components:  ' + self.entity.components
        )
        components.grid(column=0, sticky="EW")

        # --- Requirements ---

        requirements = ttk.Label(
            widgets,
            text='Requirements:  ' + self.entity.requirements
        )
        requirements.grid(column=0, sticky="EW")

        # --- Conditions ---

        conditions = ttk.Label(
            widgets,
            text='Conditions'
        )
        conditions.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        conditions_description = ttk.Label(
            widgets,
            text=self.entity.conditions
        )
        conditions_description.grid(column=0, sticky='EW')

        # --- Effects ---

        effects = ttk.Label(
            widgets,
            text='Effects'
        )
        effects.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        effects_description = ttk.Label(
            widgets,
            text=self.entity.effects
        )
        effects_description.grid(column=0, sticky='EW')

        # --- Description ---

        description = ttk.Label(
            widgets,
            text='Description'
        )
        description.grid(column=0, sticky='EW')

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        description_description = ttk.Label(
            widgets,
            text=self.entity.description
        )
        description_description.grid(column=0, sticky='EW')

        self.bind_label([
            casting,
            components,
            requirements,
            conditions_description,
            effects_description,
            description_description
        ])

    def set_buttons(self, buttons) -> None:
        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        search_result = get_search_entities(self.search_name, self.search_type)

        if self.go_parent:
            search_result = get_entity(self.parent_name, self.parent_type)

        edit_button = ttk.Button(
            buttons,
            text='  Edit',
            command=lambda: self.edit(
                name=self.search_name,
                entity=self.entity,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type,
                go_parent=self.go_parent
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
                self.go_parent,
                name=self.search_name if self.search_parent_name is None else self.search_parent_name,
                entities=search_result,
                entity=search_result,
                type_=self.search_type if self.parent_type is None else self.parent_type
            ),
            style='DarkButton.TButton',
            image=self.back_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        back_button.grid(row=2)
