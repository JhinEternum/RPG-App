from tkinter import ttk

from src.connection import get_search_entities, get_entity


class ProficiencyInterface:
    def __init__(self, **kwargs):
        self.search_name = kwargs['name']
        self.search_type = kwargs['type_']

        self.entity = kwargs['entity']
        self.back = kwargs['back']
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']

        self.search_parent_name = kwargs['search_parent_name'] if 'search_parent_name' in kwargs else None
        self.parent_name = kwargs['parent_name'] if 'parent_name' in kwargs else None
        self.parent_type = kwargs['parent_type'] if 'parent_type' in kwargs else None
        self.go_parent = kwargs['go_parent'] if 'go_parent' in kwargs else False

        self.id = self.entity['id']
        self.name = self.entity['name']
        self.description = self.entity['description']

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name = ttk.Label(
            widgets,
            text=self.name
        )
        name.grid(row=0, column=0, sticky="EW")

        name_separator = ttk.Separator(
            widgets
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky="EW")

        # --- Description ---
        description = ttk.Label(
            widgets,
            text='Description'
        )
        description.grid(column=0, sticky="EW")

        separator = ttk.Separator(
            widgets
        )
        separator.grid(column=0, columnspan=1, sticky='EW')

        description_description = ttk.Label(
            widgets,
            text=self.description
        )
        description_description.grid(column=0, sticky='EW')

        self.bind_label([description_description])

    def set_buttons(self, buttons) -> None:
        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        search_result = get_search_entities(self.search_name, self.search_type)

        if self.go_parent:
            search_result = get_entity(self.parent_name, self.parent_type)

        edit_button = ttk.Button(
            buttons,
            text='Edit',
            cursor='hand2'
        )
        edit_button.grid(row=1)

        back_button = ttk.Button(
            buttons,
            text='← Back',
            command=lambda: self.back(
                self.go_parent,
                name=self.search_name if self.search_parent_name is None else self.search_parent_name,
                entities=search_result,
                entity=search_result,
                type_=self.search_type if self.parent_type is None else self.parent_type
            ),
            cursor='hand2'
        )
        back_button.grid(row=2)
