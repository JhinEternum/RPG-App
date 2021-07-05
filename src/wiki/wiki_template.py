from src.wiki.wiki import Wiki
from tkinter import ttk, font


class WikiTemplate:
    def __init__(self, **kwargs):
        self.wiki: Wiki = kwargs['wiki']

        self.back = kwargs['back']
        self.show_wiki = kwargs['show_wiki']
        self.widgets = kwargs['widgets']
        self.buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

    def set_buttons(self, name: str, method):
        create_button = ttk.Button(
            self.buttons,
            text=name,
            command=method,
            cursor='hand2'
        )
        create_button.grid(row=0, column=0, sticky='EW')
