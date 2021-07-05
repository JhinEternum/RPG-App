import tkinter as tk
from tkinter import ttk, font

from src.wiki.category import Category
from src.wiki.section import Section
from src.wiki.wiki import Wiki
from src.wiki.wiki_search import WikiSearch


class WikiHome:
    def __init__(self, **kwargs):
        self.wiki: Wiki = kwargs['wiki']

        self.show_wiki = kwargs['show_wiki']
        self.widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

        self.categories = self.wiki.get_categories()
        self.sections = list()
        self.categories_descriptions = list()

        self.search = WikiSearch(container=self.widgets)
        self.search.grid(row=0, column=0, sticky='EW')
        self.search.columnconfigure(0, weight=1)

        self.generate_home()
        self.set_buttons(buttons)

    def set_categories(self, category: Category) -> None:
        name = ttk.Label(
            self.widgets,
            text=category.name,
            font=font.Font(size=13)
        )
        name.grid(column=0, sticky='EW')

        if len(category.description) > 0:
            description = ttk.Label(
                self.widgets,
                text=category.description,
                font=font.Font(size=11)
            )
            description.grid(column=0, sticky='EW')
            self.categories_descriptions.append(description)

        title_separator = ttk.Separator(
            self.widgets
        )
        title_separator.grid(column=0, columnspan=1, sticky='EW')

    def set_sections(self) -> None:
        for section in self.sections:
            button = ttk.Button(
                self.widgets,
                text=section.name,
                command=lambda current_section=section: self.select_section(current_section),
                cursor='hand2'
            )
            button.grid(column=0, sticky='EW')

    def select_section(self, section: Section) -> None:
        self.show_wiki(factory='section', section=section)

    def set_buttons(self, buttons: ttk.Frame) -> None:
        wiki_separator = ttk.Separator(
            buttons
        )
        wiki_separator.grid(column=0, columnspan=1, sticky='EW')

        create_category_button = ttk.Button(
            buttons,
            text='Create Category',
            command=lambda: self.show_wiki(factory='create_category', widgets_type=False),
            cursor='hand2'
        )
        create_category_button.grid(column=0, sticky='EW')

        create_section_button = ttk.Button(
            buttons,
            text='Create Section',
            command=lambda: self.show_wiki(factory='create_section', widgets_type=False),
            state=tk.DISABLED if len(self.wiki.categories) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_section_button.grid(column=0, sticky='EW')

        create_chapter_button = ttk.Button(
            buttons,
            text='Create Chapter',
            command=lambda: self.show_wiki(factory='create_chapter', widgets_type=False),
            state=tk.DISABLED if len(self.wiki.get_sections()) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_chapter_button.grid(column=0, sticky='EW')

        create_topic_button = ttk.Button(
            buttons,
            text='Create Topic',
            command=lambda: self.show_wiki(factory='create_topic', widgets_type=False),
            state=tk.DISABLED if len(self.wiki.get_chapters()) == 0 else tk.NORMAL,
            cursor='hand2'
        )
        create_topic_button.grid(column=0, sticky='EW')

    def generate_home(self) -> None:
        if len(self.categories) == 0:
            return

        for category in self.categories:
            self.set_categories(category)

            self.sections = self.wiki.get_sections(category.id)
            if len(self.sections) > 0:
                self.set_sections()

        def reconfigure_labels(event) -> None:
            for label in self.categories_descriptions:
                label.configure(wraplength=self.widgets.winfo_width() - 25)

        self.widgets.bind("<Configure>", reconfigure_labels)