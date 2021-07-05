import tkinter as tk
from tkinter import ttk


class WikiHome:
    def __init__(self, **kwargs):

        self.show_wiki = kwargs['show_wiki']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

        self.type_values = ('Category', 'Section', 'Chapter', 'Topic')

        self.name = tk.StringVar()
        self.type = tk.StringVar(value=self.type_values[0])

        self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text='Name'
        )
        name_label.grid(row=0, column=0, sticky='EW')

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=90
        )
        name_entry.grid(row=0, column=1, sticky='EW')

        # --- Type ---
        type_label = ttk.Label(
            widgets,
            text='Type'
        )
        type_label.grid(row=1, column=0, sticky='EW')

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type,
            values=self.type_values,
            state='readonly'
        )
        type_entry.grid(row=1, column=1, sticky='EW')

    def set_buttons(self, buttons) -> None:
        search_button = ttk.Button(
            buttons,
            text='Search',
            command=self.search,
            cursor='hand2'
        )
        search_button.grid(row=0)

        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=1, columnspan=1)

    def search(self) -> None:
        pass
        # print(self.type.get())
