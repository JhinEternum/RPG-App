from src.wiki.wiki import Wiki
from tkinter import ttk


class WikiTemplate:
    def __init__(self, **kwargs):
        self.wiki: Wiki = kwargs['wiki']

        self.back = kwargs['back']
        self.show_wiki = kwargs['show_wiki']
        self.widgets = kwargs['widgets']
        self.buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

        self.config_show_wiki = None

        self.preview_entity = kwargs['preview_entity'] if 'preview_entity' in kwargs else None

        self.stored_section = kwargs['stored_section'] if 'stored_section' in kwargs else None

        self.parent = None

    def set_buttons(self, name: str, method, parent=None):
        self.parent = parent

        title_separator = ttk.Separator(
            self.buttons
        )
        title_separator.grid(row=0, column=0, sticky='EW')

        generic_button = ttk.Button(
            self.buttons,
            text=name,
            command=method,
            cursor='hand2'
        )
        generic_button.grid(row=1, column=0, sticky='EW')

        back_button = ttk.Button(
            self.buttons,
            text='← Back',
            command=self.back_command,
            cursor='hand2'
        )
        back_button.grid(row=2, column=0, sticky='EW')

    def back_command(self):
        if self.preview_entity is None:
            self.show_wiki(factory=self.back)
            return

        print(self.parent)

        self.show_wiki(factory=self.back, entity=self.preview_entity, stored_section=self.stored_section)

    def config(self, factory: str, widget_type: bool, preview_entity, back: str):
        print(type(preview_entity))
        self.config_show_wiki = {
            'factory': factory,
            'widgets_type': widget_type,
            'preview_entity': preview_entity,
            'back': back
        }
