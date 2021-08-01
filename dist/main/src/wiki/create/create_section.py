import tkinter as tk
from tkinter import ttk, font

from src.methods import get_text_data, popup_showinfo
from src.wiki.wiki_template import WikiTemplate


class CreateSection(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.categories = [category.name for category in self.wiki.get_categories()]

        self.name = tk.StringVar()
        self.category_name = tk.StringVar(value=self.categories[0])

        self.description_entry = tk.Text

        self.set_widgets()
        self.set_buttons('Create Section', self.create_section)

    def set_widgets(self):
        title_label = ttk.Label(
            self.widgets,
            text='Create Section',
            font=font.Font(size=13)
        )
        title_label.grid(row=0, column=0, sticky='EW')

        title_separator = ttk.Separator(
            self.widgets
        )
        title_separator.grid(row=1, column=0, columnspan=1, sticky='EW')

        name_label = ttk.Label(
            self.widgets,
            text='Name'
        )
        name_label.grid(row=2, column=0, sticky='EW')

        name_entry = ttk.Entry(
            self.widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=2, column=1, sticky='EW')

        category_label = ttk.Label(
            self.widgets,
            text='Category'
        )
        category_label.grid(row=3, column=0, sticky='EW')

        category_menu = ttk.Combobox(
            self.widgets,
            textvariable=self.category_name,
            values=self.categories,
            state="readonly"
        )
        category_menu.grid(row=3, column=1, sticky='EW')

        description_label = ttk.Label(
            self.widgets,
            text='Description'
        )
        description_label.grid(row=4, column=0, sticky='EW')

        self.description_entry = tk.Text(
            self.widgets,
            width=50,
            height=10
        )
        self.description_entry.grid(row=4, column=1, sticky='EW')

        description_scroll = ttk.Scrollbar(
            self.widgets,
            orient='vertical',
            command=self.description_entry.yview
        )
        description_scroll.grid(row=4, column=2, sticky='ns')

        self.description_entry['yscrollcommand'] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def create_section(self):
        name = self.name.get()
        description = get_text_data(self.description_entry)
        category = self.category_name.get()
        category_id = self.wiki.category_mapping[category]

        create = self.wiki.create_section(name, description, category_id)

        self.show_wiki(factory=self.back) if create else popup_showinfo('Error!')
