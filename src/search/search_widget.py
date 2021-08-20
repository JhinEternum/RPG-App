import tkinter as tk
from tkinter import ttk

from src.images.image import get_avatar, get_monster, get_npc, get_proficiency, get_armors, get_weapons, get_title, \
    get_ability


class SearchWidget:
    def __init__(self, **kwargs):
        self.interface_result = kwargs['interface_result'] if 'interface_result' in kwargs else None
        widgets = kwargs['widgets']
        self.entities = kwargs['entities']
        self.type = kwargs['type_']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None

        self.char_icon_types = {
            'Character': get_avatar(),
            'Monster': get_monster(),
            'NPC': get_npc()
        }
        self.item_icon_types = {
            'Armor': get_armors(),
            'Weapon': get_weapons()
        }
        print(self.type)
        if self.type in self.char_icon_types:
            self.icon = self.char_icon_types[self.type]
        elif self.type == 'Proficiency':
            self.icon = get_proficiency()
        elif self.type in self.item_icon_types:
            self.icon = self.item_icon_types[self.type]
        elif self.type == 'Title':
            self.icon = get_title()
        elif self.type == 'Ability':
            self.icon = get_ability()

        self.set_widgets_abilities(widgets) if self.type == 'Ability' else self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets):
        result_entity_type = ttk.Label(
            widgets,
            text='  ' + self.type + 's',
            image=self.icon,
            compound=tk.LEFT
        )
        result_entity_type.grid(column=0, padx=5, pady=5, sticky='EW')

        result_separator = ttk.Separator(
            widgets
        )
        result_separator.grid(column=0, columnspan=1, sticky='EW')

        for entity in self.entities:
            entity_button = ttk.Button(
                widgets,
                text=entity.name,
                command=lambda current_entity=entity: self.interface_result(current_entity),
                style='DarkButton.TButton',
                cursor="hand2"
            )
            if self.type == 'Proficiency' and entity.icon != 'none':
                entity_button['text'] = '  ' + entity.name
                entity_button['image'] = entity.icon
                entity_button['compound'] = tk.LEFT
            entity_button.grid(column=0, padx=5, pady=5, sticky='EW')

    def set_widgets_abilities(self, widgets):
        entities_title = [
            'Characters Abilities',
            'NPCs Abilities',
            'Monsters Abilities'
            # 'Items Abilities'
        ]

        row = 0
        for entities in self.entities:
            result_entity_type = ttk.Label(
                widgets,
                text='  ' + entities_title[row],
                image=self.icon,
                compound=tk.LEFT
            )
            result_entity_type.grid(column=0, padx=5, pady=5, sticky="EW")

            result_separator = ttk.Separator(
                widgets
            )
            result_separator.grid(column=0, columnspan=1, sticky="EW")

            row += 1

            for entity in entities:
                entity_button = ttk.Button(
                    widgets,
                    text=entity.name,
                    command=lambda current_entity=entity: self.interface_result(current_entity),
                    style='DarkButton.TButton',
                    cursor="hand2"
                )
                entity_button.grid(column=0, padx=5, pady=5, sticky="EW")

    def set_buttons(self, buttons):
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)
