import tkinter as tk
from tkinter import ttk, font

from src.connection import get_entity
from src.methods import popup_showinfo, get_text_data
from src.proficiency.proficiency import Proficiency


class EditProficiency:
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

        # --- Proficiency ---
        self.id = self.entity['id']
        self.proficiency_name = self.entity['name']
        self.proficiency_description = self.entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.proficiency_name)

        # --- Widgets ---
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
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

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=3, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.description_entry.grid(row=3, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=3, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.proficiency_description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.proficiency_name, self.search_type)

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
        description = get_text_data(self.description_entry)

        proficiency = Proficiency(
            name=name,
            description=description
        )

        edit_proficiency = proficiency.update_proficiency(self.id)

        self.search_result = get_entity(name, self.search_type)

        if edit_proficiency:
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
