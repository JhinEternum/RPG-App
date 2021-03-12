import tkinter as tk
from tkinter import ttk, font


class EditItem:
    def __init__(self, **kwargs):
        self.search_name = kwargs['name']
        self.search_type = kwargs['type_']

        self.entity = kwargs['entity']
        self.save = kwargs['save']
        self.back = kwargs['back']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']
        self.show_interface = kwargs['show_interface']

        self.font = font.Font(size=11)

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        pass

    def set_buttons(self, buttons) -> None:
        pass
