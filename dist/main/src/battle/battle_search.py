import tkinter as tk
from tkinter import ttk

from src.battle.battle_system import BattleSystem
from src.images.image import get_avatar, get_monster, get_npc


class BattleSearch:
    def __init__(self, **kwargs):
        self.master = kwargs['master']
        self.widgets = kwargs['widgets']

        self.type_values = ('Character', 'NPC', 'Monster')

        self.entities = kwargs['entities']
        self.type = kwargs['type']

        self.icon_types = {
            'Character': get_avatar(),
            'Monster': get_monster(),
            'NPC': get_npc()
        }
        self.icon = self.icon_types[self.type]

        self.set_widgets()

    def set_widgets(self):
        result_entity_type = ttk.Label(
            self.widgets,
            text=self.type + 's',
            image=self.icon,
            compound=tk.LEFT
        )
        result_entity_type.grid(column=0, padx=5, pady=5, sticky='EW')

        result_separator = ttk.Separator(
            self.widgets
        )
        result_separator.grid(column=0, columnspan=1, sticky='EW')

        for entity in self.entities:
            entity_button = ttk.Button(
                self.widgets,
                text=entity.name,
                command=lambda current_entity=entity: self.battle_system(current_entity),
                style='DarkButton.TButton',
                cursor="hand2"
            )
            entity_button.grid(column=0, padx=5, pady=5, sticky='EW')

    def battle_system(self, entity):
        config = {
            'master': self.master,
            'entity': entity
        }

        BattleSystem(**config)
