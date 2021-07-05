import tkinter as tk
from tkinter import ttk, font

from src.wiki.topic import Topic
from src.wiki.wiki import Wiki


class WikiChapter:
    def __init__(self, **kwargs):
        self.wiki: Wiki = kwargs['wiki']

        self.show_wiki = kwargs['show_wiki']
        self.widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

        self.chapter = kwargs['chapter']
        self.topics = self.wiki.get_topics(self.chapter.id)

        self.set_chapter()
        self.set_buttons(buttons)

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

    def set_buttons(self, buttons: ttk.Frame) -> None:
        pass

    def select_topic(self, topic: Topic) -> None:
        self.show_wiki(factory='topic', topic=topic)
