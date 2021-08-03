from tkinter import ttk


class SearchWidget:
    def __init__(self, **kwargs):
        self.interface_result = kwargs['interface_result'] if 'interface_result' in kwargs else None
        widgets = kwargs['widgets']
        self.entities = kwargs['entities']
        self.type = kwargs['type_']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None

        self.set_widgets_abilities(widgets) if self.type == 'Ability' else self.set_widgets(widgets)
        self.set_buttons(buttons)

    def set_widgets(self, widgets):
        result_entity_type = ttk.Label(
            widgets,
            text=self.type + 's'
        )
        result_entity_type.grid(column=0, padx=5, pady=5, sticky='EW')

        result_separator = ttk.Separator(
            widgets
        )
        result_separator.grid(column=0, columnspan=1, sticky='EW')

        for entity in self.entities:
            entity_button = ttk.Button(
                widgets,
                text=entity,
                command=lambda current_entity=entity: self.interface_result(current_entity),
                cursor="hand2"
            )
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
                text=entities_title[row]
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
                    text=entity,
                    command=lambda current_entity=entity: self.interface_result(current_entity),
                    cursor="hand2"
                )
                entity_button.grid(column=0, padx=5, pady=5, sticky="EW")

    def set_buttons(self, buttons):
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)
