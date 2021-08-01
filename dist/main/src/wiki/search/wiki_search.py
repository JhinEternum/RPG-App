import tkinter as tk
from tkinter import ttk

from src.wiki.wiki import Wiki


class WikiSearch(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(kwargs['container'])

        self.wiki: Wiki = kwargs['wiki']

        self.type_values = ('Category', 'Section', 'Chapter', 'Topic')

        self.name = tk.StringVar()
        self.type = tk.StringVar(value=self.type_values[0])

        self.set_widgets()
        self.set_buttons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def set_widgets(self) -> None:
        # --- Name ---
        name_label = ttk.Label(
            self,
            text='Name'
        )
        name_label.grid(row=0, column=0, sticky='EW')

        name_entry = ttk.Entry(
            self,
            textvariable=self.name,
            width=90
        )
        name_entry.grid(row=0, column=1, sticky='EW')

        # --- Type ---
        type_label = ttk.Label(
            self,
            text='Type'
        )
        type_label.grid(row=1, column=0, sticky='EW')

        type_entry = ttk.Combobox(
            self,
            textvariable=self.type,
            values=self.type_values,
            state='readonly'
        )
        type_entry.grid(row=1, column=1, sticky='EW')

    def set_buttons(self) -> None:
        search_button = ttk.Button(
            self,
            text='Search',
            command=self.search,
            cursor='hand2'
        )
        search_button.grid(row=2, column=0, columnspan=2, sticky='EW')

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(row=3, columnspan=2, sticky='EW')

    def search(self) -> None:
        type_ = self.type.get()

        if type_ == 'Category':
            self.wiki.search_category()
        elif type_ == 'Section':
            self.wiki.search_section()
        elif type_ == 'Chapter':
            self.wiki.search_chapter()
        else:
            self.wiki.search_topic()
