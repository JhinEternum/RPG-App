import tkinter as tk
from tkinter import ttk, font

from src.ability.ability import Ability
from src.connection.database import get_entity
from src.edit.edit_template import EditTemplate
from src.methods import get_text_data, popup_showinfo
from styles import BUTTON_BACKGROUND_COLOR2, WHITE_COLOR


class EditAbility(EditTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.font = font.Font(size=11)

        self.entity: Ability

        # --- Attributes ---
        self.name = tk.StringVar(value=self.entity.name)
        self.casting = tk.StringVar(value=self.entity.casting)
        self.components = tk.StringVar(value=self.entity.components)

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
            height=3,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.requirements_entry.grid(row=3, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=3, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, self.entity.requirements)

        # --- Conditions ---

        conditions_label = ttk.Label(
            widgets,
            text="Conditions"
        )
        conditions_label.grid(row=4, column=0, sticky="EW")

        self.conditions_entry = tk.Text(
            widgets,
            width=1,
            height=3,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.conditions_entry.grid(row=4, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=4, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, self.entity.conditions)

        # --- Effects ---

        effects_label = ttk.Label(
            widgets,
            text="Effects"
        )
        effects_label.grid(row=5, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            widgets,
            width=1,
            height=15,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.effects_entry.grid(row=5, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=5, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.entity.effects)

        # --- Description ---

        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=6, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.description_entry.grid(row=6, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=6, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.entity.description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.entity.name, self.search_type)

        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        save_button = ttk.Button(
            buttons,
            text='  Save',
            command=lambda: self.save(edit=self.edit),
            style='DarkButton.TButton',
            image=self.save_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        save_button.grid(row=1)

        back_button = ttk.Button(
            buttons,
            text='  Back',
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
            style='DarkButton.TButton',
            image=self.back_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        back_button.grid(row=2)

    def edit(self) -> None:
        name = self.name.get()
        casting = self.casting.get()
        components = self.components.get()
        requirements = get_text_data(self.requirements_entry)
        conditions = get_text_data(self.conditions_entry)
        effects = get_text_data(self.effects_entry)
        description = get_text_data(self.description_entry)

        ability = Ability(
            id=self.entity.id,
            name=name,
            casting=casting,
            components=components,
            requirements=requirements,
            conditions=conditions,
            effects=effects,
            description=description
        )

        update_ability = ability.update_ability()

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
