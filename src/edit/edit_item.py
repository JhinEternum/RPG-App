import tkinter as tk
from tkinter import ttk, font

from src.connection import get_entity
from src.item.item import Item
from src.methods import get_text_data, handle_selection_change, popup_showinfo


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

        self.search_parent_name = kwargs['search_parent_name'] if 'search_parent_name' in kwargs else None
        self.parent_name = kwargs['parent_name'] if 'parent_name' in kwargs else None
        self.parent_type = kwargs['parent_type'] if 'parent_type' in kwargs else None
        self.go_parent = kwargs['go_parent'] if 'go_parent' in kwargs else False

        self.search_result = None

        print(f'parent_name {self.parent_name}')

        self.font = font.Font(size=11)

        self.types_ = ('Armor', 'Weapon')

        # --- Item ---
        self.id = self.entity['id']
        self.item_name = self.entity['name']
        self.item_type = self.entity['type']
        self.item_reduction = self.entity['reduction']
        self.item_damage = self.entity['damage']
        self.item_range = self.entity['range']
        self.item_health = self.entity['health']
        self.item_area = self.entity['area']
        self.item_effects = self.entity['effects']
        self.item_description = self.entity['description']

        # --- Attributes ---
        self.name = tk.StringVar(value=self.item_name)
        self.type_ = tk.StringVar(value=self.types_[self.item_type - 1])
        self.reduction = tk.StringVar(value=self.item_reduction)
        self.damage = tk.StringVar(value=self.item_damage)
        self.range_ = tk.StringVar(value=self.item_range)
        self.health = tk.StringVar(value=self.item_health)
        self.area = tk.StringVar(value=self.item_area)

        # --- Widgets ---
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        name_label = ttk.Label(
            widgets,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="EW")

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Type ---

        type_label = ttk.Label(
            widgets,
            text="Type"
        )
        type_label.grid(row=1, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type_,
            values=self.types_,
            exportselection=False,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")

        # --- Reduction ---

        reduction_label = ttk.Label(
            widgets,
            text="Reduction"
        )
        reduction_label.grid(row=2, column=0, sticky="EW")

        reduction_entry = ttk.Entry(
            widgets,
            textvariable=self.reduction,
            width=60
        )
        reduction_entry.grid(row=2, column=1, sticky="EW")

        # --- Damage ---

        damage_label = ttk.Label(
            widgets,
            text="Damage"
        )
        damage_label.grid(row=3, column=0, sticky="EW")

        damage_entry = ttk.Entry(
            widgets,
            textvariable=self.damage,
            width=60
        )
        damage_entry.grid(row=3, column=1, sticky="EW")

        # --- Range ---

        range_label = ttk.Label(
            widgets,
            text="Range"
        )
        range_label.grid(row=4, column=0, sticky="EW")

        range_entry = ttk.Entry(
            widgets,
            textvariable=self.range_,
            width=60
        )
        range_entry.grid(row=4, column=1, sticky="EW")

        # --- Health ---

        health_label = ttk.Label(
            widgets,
            text="Health"
        )
        health_label.grid(row=5, column=0, sticky="EW")

        health_entry = ttk.Entry(
            widgets,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=5, column=1, sticky="EW")

        # --- Area ---

        area_label = ttk.Label(
            widgets,
            text="Area"
        )
        area_label.grid(row=6, column=0, sticky="EW")

        area_entry = ttk.Entry(
            widgets,
            textvariable=self.area,
            width=60
        )
        area_entry.grid(row=6, column=1, sticky="EW")

        # --- Effects ---

        effects_label = ttk.Label(
            widgets,
            text="Effects"
        )
        effects_label.grid(row=7, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            widgets,
            width=1,
            height=10
        )
        self.effects_entry.grid(row=7, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=7, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.item_effects)

        # --- Description ---

        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=8, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5
        )
        self.description_entry.grid(row=8, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=8, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.item_description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.item_name, self.search_type)

        save_button = ttk.Button(
            buttons,
            text='Save',
            command=lambda: self.save(edit=self.edit),
            cursor='hand2'
        )
        save_button.grid(row=0)

        back_button = ttk.Button(
            buttons,
            text='← Back',
            command=lambda: self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type
            ),
            cursor='hand2'
        )
        back_button.grid(row=1)

    def edit(self) -> None:
        type_dict = {'Armor': 1, 'Weapon': 2}

        name = self.name.get()
        type_ = type_dict[self.type_.get()]
        reduction = self.reduction.get()
        damage = self.damage.get()
        range_ = self.range_.get()
        health = self.health.get()
        area = self.area.get()
        effects = get_text_data(self.effects_entry)
        description = get_text_data(self.description_entry)

        item = Item(
            name=name,
            type_=type_,
            reduction=reduction,
            damage=damage,
            range_=range_,
            health=health,
            area=area,
            effects=effects,
            description=description
        )

        update_item = item.update_item(self.id)

        self.search_result = get_entity(name, self.search_type)

        if update_item:
            self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type
            )
        else:
            popup_showinfo('Something went wrong, try again!')
