import tkinter as tk
from tkinter import ttk

from src.creation.create_template import CreateTemplate


class ProficiencyWidget(CreateTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_proficiency = kwargs['create_proficiency'] if 'create_proficiency' in kwargs else None
        widgets = kwargs['widgets']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None

        # --- Attributes ---
        self.proficiency = 'Proficiency ' + self.frame_id

        # --- Widgets ---
        self.name = tk.StringVar()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Proficiency ---

        proficiency_label = ttk.Label(
            widgets,
            text=self.proficiency
        )
        proficiency_label.grid(row=0, column=0, sticky="EW")

        proficiency_separator = ttk.Separator(
            widgets
        )
        proficiency_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

        # --- Name ---

        name_label = ttk.Label(
            widgets,
            text='Name'
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
            text='Description'
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

        self.description_entry.insert(tk.END, 'None')

    def set_buttons(self, buttons) -> None:
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)

        create_button = ttk.Button(
            buttons,
            text='Create Proficiency',
            command=self.create_proficiency,
            cursor='hand2'
        )
        create_button.grid(row=1)

        add_button = ttk.Button(
            buttons,
            text='Add Proficiency',
            command=self.add_entity_frame,
            cursor='hand2'
        )
        add_button.grid(row=2)
