import tkinter as tk
from tkinter import ttk, font

from src.ability.ability import Ability
from src.connection import get_entity
from src.methods import get_text_data, popup_showinfo


class EditAbility:
    def __init__(self, **kwargs):
        self.search_name = kwargs['name']
        self.search_type = kwargs['type_']

        self.entity = kwargs['entity']
        self.save = kwargs['save']
        self.back = kwargs['back']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']
        self.show_interface = kwargs['show_interface']

        self.search_parent_name = kwargs['search_parent_name'] if 'search_parent_name' in kwargs else None
        self.parent_name = kwargs['parent_name'] if 'parent_name' in kwargs else None
        self.parent_type = kwargs['parent_type'] if 'parent_type' in kwargs else None
        self.go_parent = kwargs['go_parent'] if 'go_parent' in kwargs else False

        self.search_result = None

        print(f'parent_name {self.parent_name}')

        self.font = font.Font(size=11)

        # --- Ability ---
        self.id = self.entity['id']
        self.ability_name = self.entity['name']
        self.ability_casting = self.entity['casting']
        self.ability_components = self.entity['components']
        self.ability_requirements = self.entity['requirements']
        self.ability_conditions = self.entity['conditions']
        self.ability_effects = self.entity['effects']
        self.ability_description = self.entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.ability_name)
        self.casting = tk.StringVar(value=self.ability_casting)
        self.components = tk.StringVar(value=self.ability_components)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name_label = ttk.Label(
            widgets,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="EW")

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Casting ---

        casting_label = ttk.Label(
            widgets,
            text="Casting"
        )
        casting_label.grid(row=1, column=0, sticky="EW")

        casting_entry = ttk.Entry(
            widgets,
            textvariable=self.casting,
            width=60
        )
        casting_entry.grid(row=1, column=1, sticky="EW")

        # --- Components ---

        components_label = ttk.Label(
            widgets,
            text="Components"
        )
        components_label.grid(row=2, column=0, sticky="EW")

        components_entry = ttk.Entry(
            widgets,
            textvariable=self.components,
            width=60
        )
        components_entry.grid(row=2, column=1, sticky="EW")

        # --- Requirements ---

        requirements_label = ttk.Label(
            widgets,
            text="Requirements"
        )
        requirements_label.grid(row=3, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            widgets,
            width=1,
            height=3
        )
        self.requirements_entry.grid(row=3, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=3, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, self.ability_requirements)

        # --- Conditions ---

        conditions_label = ttk.Label(
            widgets,
            text="Conditions"
        )
        conditions_label.grid(row=4, column=0, sticky="EW")

        self.conditions_entry = tk.Text(
            widgets,
            width=1,
            height=3
        )
        self.conditions_entry.grid(row=4, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=4, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, self.ability_conditions)

        # --- Effects ---

        effects_label = ttk.Label(
            widgets,
            text="Effects"
        )
        effects_label.grid(row=5, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            widgets,
            width=1,
            height=10
        )
        self.effects_entry.grid(row=5, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=5, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.ability_effects)

        # --- Description ---

        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=6, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.description_entry.grid(row=6, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=6, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.ability_description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.ability_name, self.search_type)

        save_button = ttk.Button(
            buttons,
            text='Save',
            command=lambda: self.save(edit=self.edit),
            cursor='hand2'
        )
        save_button.grid(row=0)

        back_button = ttk.Button(
            buttons,
            text='← Back',
            command=lambda: self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type,
                is_edit=True
            ),
            cursor='hand2'
        )
        back_button.grid(row=1)

    def edit(self) -> None:
        name = self.name.get()
        casting = self.casting.get()
        components = self.components.get()
        requirements = get_text_data(self.requirements_entry)
        conditions = get_text_data(self.conditions_entry)
        effects = get_text_data(self.effects_entry)
        description = get_text_data(self.description_entry)

        ability = Ability(
            name=name,
            casting=casting,
            components=components,
            requirements=requirements,
            conditions=conditions,
            effects=effects,
            description=description
        )

        update_ability = ability.update_ability(self.id)

        self.search_result = get_entity(name, self.search_type)

        if update_ability:
            self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type,
                is_edit=True
            )
        else:
            popup_showinfo('Something went wrong, try again!')
