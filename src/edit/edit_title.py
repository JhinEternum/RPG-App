import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_entity
from src.edit.edit_template import EditTemplate
from src.methods import get_text_data, popup_showinfo
from src.title.title import Title


class EditTitle(EditTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        print(f'parent_name {self.parent_name}')

        self.font = font.Font(size=11)

        # --- Attributes ---
        self.name = tk.StringVar(value=self.entity.name)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
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

        # --- Requirements ---

        requirements_label = ttk.Label(
            widgets,
            text="Requirements"
        )
        requirements_label.grid(row=1, column=0, sticky="EW")

        self.requirements_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.requirements_entry.grid(row=1, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=1, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, self.entity.requirements)

        # --- Description ---

        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=2, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=15
        )
        self.description_entry.grid(row=2, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=2, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.entity.description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.entity.name, self.search_type)

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
        requirements = get_text_data(self.requirements_entry)
        description = get_text_data(self.description_entry)

        title = Title(
            id=self.entity.id,
            name=name,
            requirements=requirements,
            description=description
        )

        edit_title = title.update_title()

        self.search_result = get_entity(name, self.search_type)

        if edit_title:
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
