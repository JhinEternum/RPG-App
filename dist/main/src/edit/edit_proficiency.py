import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_entity
from src.edit.edit_template import EditTemplate
from src.methods import popup_showinfo, get_text_data
from src.proficiency.proficiency import Proficiency


class EditProficiency(EditTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.font = font.Font(size=11)

        # --- Attributes ---
        self.name = tk.StringVar(value=self.entity.name)

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
            height=15
        )
        self.description_entry.grid(row=3, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=3, column=2, sticky="ns")

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
        description = get_text_data(self.description_entry)

        proficiency = Proficiency(
            name=name,
            description=description
        )

        edit_proficiency = proficiency.update_proficiency(self.entity.id)

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
