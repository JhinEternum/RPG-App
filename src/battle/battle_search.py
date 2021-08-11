import tkinter as tk
from tkinter import ttk

from src.battle.battle_system import BattleSystem
from src.connection.database import get_entity


class BattleSearch:
    def __init__(self, **kwargs):
        self.master = kwargs['master']
        self.widgets = kwargs['widgets']

        self.type_values = ('Character', 'NPC', 'Monster')

        self.entities = kwargs['entities']
        self.type = kwargs['type']

        self.set_widgets()

    def set_widgets(self):
        result_entity_type = ttk.Label(
            self.widgets,
            text=self.type + 's'
        )
        result_entity_type.grid(column=0, padx=5, pady=5, sticky='EW')

        result_separator = ttk.Separator(
            self.widgets
        )
        result_separator.grid(column=0, columnspan=1, sticky='EW')

        for entity in self.entities:
            entity_button = ttk.Button(
                self.widgets,
                text=entity,
                command=lambda current_entity=entity: self.battleSystem(current_entity),
                cursor="hand2"
            )
            entity_button.grid(column=0, padx=5, pady=5, sticky='EW')

    def battleSystem(self, entity: str):
        entity = get_entity(entity, self.type)

        config = {
            'master': self.master,
            'entity': entity
        }

        BattleSystem(**config)
