import tkinter as tk
from tkinter import ttk, font

from src.wiki.wiki_template import WikiTemplate


class WikiTopic(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.topic = kwargs['topic']

        self.set_topic()

    def set_topic(self) -> None:
        name = ttk.Label(
            self.widgets,
            text=self.topic.name,
            font=font.Font(size=13)
        )
        name.grid(row=0, column=0, sticky='EW')

        if len(self.topic.description) > 0:
            description = ttk.Label(
                self.widgets,
                text=self.topic.description,
                font=font.Font(size=11)
            )
            description.grid(row=1, column=0, sticky='EW')

            def reconfigure_labels(event) -> None:
                description.configure(wraplength=self.widgets.winfo_width() - 25)

            self.widgets.bind("<Configure>", reconfigure_labels)

    def set_buttons(self) -> None:
        pass
