import tkinter as tk
from tkinter import ttk

from src.battle.battle_search import BattleSearch
from src.battle.battle_template import BattleTemplateFrame
from src.connection.database import get_search_entities
from src.images.image import get_search


class Battle(BattleTemplateFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.battle = kwargs

        self.parent = kwargs['parent']

        self.type_values = ('Character', 'NPC', 'Monster')

        self.search_icon = get_search()

        self.name = tk.StringVar()
        self.type = tk.StringVar(value=self.type_values[0])

        self.set_search()
        self.set_buttons()

        self.set_widgets_conf()
        self.set_buttons_conf()

    def set_search(self):
        # --- Name ---
        name_label = ttk.Label(
            self.template_scroll.widgets,
            text='Name'
        )
        name_label.grid(row=0, column=0, sticky='EW')

        name_entry = ttk.Entry(
            self.template_scroll.widgets,
            textvariable=self.name,
            width=90
        )
        name_entry.grid(row=0, column=1, sticky='EW')

        # --- Type ---
        type_label = ttk.Label(
            self.template_scroll.widgets,
            text="Type"
        )
        type_label.grid(row=1, column=0, sticky='EW')

        type_entry = ttk.Combobox(
            self.template_scroll.widgets,
            textvariable=self.type,
            values=self.type_values,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky='EW')

        search_button = ttk.Button(
            self.template_scroll.widgets,
            text='  Search',
            command=self.search,
            style='DarkButton.TButton',
            image=self.search_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        search_button.grid(row=2, column=0, columnspan=2, sticky='EW')

    def set_buttons(self):
        title_separator = ttk.Separator(
            self.template_scroll.buttons
        )
        title_separator.grid(row=0, columnspan=1, sticky='EW')

    def search(self):
        name = self.name.get()
        type_ = self.type.get()

        search_result = get_search_entities(name, type_)

        config = {
            'master': self.parent,
            'entity': BattleSearch,
            'entities': search_result,
            'type': type_
        }

        self.template_scroll.add_entity_frame(**config)
