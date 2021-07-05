import tkinter as tk
from tkinter import ttk, font

from src.wiki.wiki_template import WikiTemplate
from src.wiki.topic import Topic


class WikiChapter(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chapter = kwargs['chapter']
        self.topics = self.wiki.get_topics(self.chapter.id)

        self.set_chapter()
        self.set_buttons()

    def set_chapter(self) -> None:
        name = ttk.Label(
            self.widgets,
            text=self.chapter.name,
            font=font.Font(size=13)
        )
        name.grid(row=0, column=0, sticky='EW')

        if len(self.chapter.description) > 0:
            description = ttk.Label(
                self.widgets,
                text=self.chapter.description,
                font=font.Font(size=11)
            )
            description.grid(row=1, column=0, sticky='EW')

            def reconfigure_labels(event) -> None:
                description.configure(wraplength=self.widgets.winfo_width() - 25)

            self.widgets.bind("<Configure>", reconfigure_labels)

        title_separator = ttk.Separator(
            self.widgets
        )
        title_separator.grid(row=2, column=0, columnspan=2, sticky='EW')

        if len(self.topics) > 0:
            self.set_topics()

    def set_topics(self) -> None:
        for topic in self.topics:
            button = ttk.Button(
                self.widgets,
                text=topic.name,
                command=lambda current_topic=topic: self.select_topic(current_topic),
                cursor='hand2'
            )
            button.grid(column=0, sticky='EW')

    def set_buttons(self) -> None:
        pass

    def select_topic(self, topic: Topic) -> None:
        self.show_wiki(factory='topic', topic=topic)
