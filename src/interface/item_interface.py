import tkinter as tk
from tkinter import ttk

from src.connection.database import get_search_entities, get_entity
from src.images.image import get_armors, get_sword
from src.interface.interface_template import InterfaceTemplate


class ItemInterface(InterfaceTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.types_ = {1: 'Armor', 2: 'Weapon'}

        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.icon_types = {
            1: get_armors(),
            2: get_sword()
        }
        self.item_icon = self.icon_types[self.entity.type]

        self.set_widgets(widgets)
        if buttons:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Item ---

        name = ttk.Label(
            widgets,
            text='  ' + self.entity.name,
            image=self.item_icon,
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
            text='Type:  ' + self.types_[self.entity.type]
        )
        type_.grid(row=2, column=0, sticky="EW")

        # --- Reduction ---

        reduction = ttk.Label(
            widgets,
            text='Reduction:  ' + self.entity.reduction
        )
        reduction.grid(row=3, column=0, sticky="EW")

        # --- Damage ---

        damage = ttk.Label(
            widgets,
            text='Damage:  ' + self.entity.damage
        )
        damage.grid(row=4, column=0, sticky="EW")

        # --- Range ---

        range_ = ttk.Label(
            widgets,
            text='Range:  ' + self.entity.range
        )
        range_.grid(row=5, column=0, sticky="EW")

        # --- Health ---

        health = ttk.Label(
            widgets,
            text='Health:  ' + self.entity.health
        )
        health.grid(row=6, column=0, sticky="EW")

        # --- Area ---

        area = ttk.Label(
            widgets,
            text='Area:  ' + self.entity.area
        )
        area.grid(row=7, column=0, sticky="EW")

        # --- Effects ---

        effects = ttk.Label(
            widgets,
            text='Effects'
        )
        effects.grid(row=8, column=0, sticky='EW')

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
        description.grid(column=0, sticky="EW")

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        description_description = ttk.Label(
            widgets,
            text=self.entity.description
        )
        description_description.grid(column=0, sticky='EW')

        self.bind_label([effects_description, description_description])

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
