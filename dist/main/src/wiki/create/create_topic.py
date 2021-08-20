import tkinter as tk
from tkinter import ttk, font

from src.methods import get_text_data, popup_showinfo
from src.wiki.chapter import Chapter
from src.wiki.wiki_template import WikiTemplate
from styles import BUTTON_BACKGROUND_COLOR2, WHITE_COLOR


class CreateTopic(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.preview_chapter: Chapter = kwargs['preview_entity'] if 'preview_entity' in kwargs else None

        self.chapters = [chapter.name for chapter in self.wiki.get_chapters()]

        chapter_index = 0

        if self.preview_chapter:
            chapter_index = self.chapters.index(self.preview_chapter.name)

        self.name = tk.StringVar()
        self.chapter_name = tk.StringVar(value=self.chapters[chapter_index])

        self.description_entry = tk.Text

        self.set_widgets()
        self.set_buttons('Create Topic', self.create_topic, self.preview_chapter)

    def set_widgets(self):
        title_label = ttk.Label(
            self.widgets,
            text='Create Topic',
            font=font.Font(size=13)
        )
        title_label.grid(row=0, column=0, sticky='EW')

        title_separator = ttk.Separator(
            self.widgets
        )
        title_separator.grid(row=1, column=0, columnspan=3, sticky='EW')

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

        chapter_label = ttk.Label(
            self.widgets,
            text='Chapter'
        )
        chapter_label.grid(row=3, column=0, sticky='EW')

        chapter_menu = ttk.Combobox(
            self.widgets,
            textvariable=self.chapter_name,
            values=self.chapters,
            state="readonly"
        )
        chapter_menu.grid(row=3, column=1, sticky='EW')

        description_label = ttk.Label(
            self.widgets,
            text='Description'
        )
        description_label.grid(row=4, column=0, sticky='EW')

        self.description_entry = tk.Text(
            self.widgets,
            width=50,
            height=10,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
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

    def create_topic(self):
        name = self.name.get()
        description = get_text_data(self.description_entry)
        chapter = self.chapter_name.get()
        chapter_id = self.wiki.chapter_mapping[chapter]

        create = self.wiki.create_topic(name, description, chapter_id)

        if create is None:
            popup_showinfo('Error!')
            return

        if self.preview_chapter:
            self.show_wiki(factory=self.back, entity=self.preview_chapter)
        else:
            self.show_wiki(factory=self.back)
