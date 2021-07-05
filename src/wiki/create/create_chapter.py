import tkinter as tk
from tkinter import ttk, font

from src.methods import get_text_data, popup_showinfo
from src.wiki.wiki_template import WikiTemplate


class CreateChapter(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sections = [section.name for section in self.wiki.get_sections()]

        self.name = tk.StringVar()
        self.section_name = tk.StringVar(value=self.sections[0])

        self.description_entry = tk.Text

        self.set_widgets()
        self.set_buttons()

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

        section_label = ttk.Label(
            self.widgets,
            text='Section'
        )
        section_label.grid(row=3, column=0, sticky='EW')

        section_menu = ttk.Combobox(
            self.widgets,
            textvariable=self.section_name,
            values=self.sections,
            state="readonly"
        )
        section_menu.grid(row=3, column=1, sticky='EW')

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

    def set_buttons(self):
        create_button = ttk.Button(
            self.buttons,
            text='Create Chapter',
            command=self.create_chapter,
            cursor='hand2'
        )
        create_button.grid(row=0, column=0, sticky='EW')

    def create_chapter(self):
        name = self.name.get()
        description = get_text_data(self.description_entry)
        section = self.section_name.get()
        section_id = self.wiki.section_mapping[section]

        create = self.wiki.create_chapter(name, description, section_id)

        self.show_wiki(factory='home') if create else popup_showinfo('Error!')
