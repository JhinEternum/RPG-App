import tkinter as tk
from tkinter import ttk, font

from src.connection.database import get_entity
from src.edit.edit_template import EditTemplate
from src.item.item import Item
from src.methods import get_text_data, popup_showinfo
from styles import BUTTON_BACKGROUND_COLOR2, WHITE_COLOR


class EditItem(EditTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.font = font.Font(size=11)

        self.types_ = ('Armor', 'Weapon')

        self.entity: Item

        # --- Attributes ---
        self.name = tk.StringVar(value=self.entity.name)
        self.type_ = tk.StringVar(value=self.types_[self.entity.type - 1])
        self.reduction = tk.StringVar(value=self.entity.reduction)
        self.damage = tk.StringVar(value=self.entity.damage)
        self.range_ = tk.StringVar(value=self.entity.range)
        self.health = tk.StringVar(value=self.entity.health)
        self.area = tk.StringVar(value=self.entity.area)

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
            height=15,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.effects_entry.grid(row=7, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=7, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, self.entity.effects)

        # --- Description ---

        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=8, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.description_entry.grid(row=8, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=8, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.entity.description)

    def set_buttons(self, buttons) -> None:
        self.search_result = get_entity(self.entity.name, self.search_type)

        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        save_button = ttk.Button(
            buttons,
            text='  Save',
            command=lambda: self.save(edit=self.edit),
            style='DarkButton.TButton',
            image=self.save_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        save_button.grid(row=1)

        back_button = ttk.Button(
            buttons,
            text='  Back',
            command=lambda: self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type,
                is_edit=True
            ),
            style='DarkButton.TButton',
            image=self.back_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        back_button.grid(row=2)

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
            id=self.entity.id,
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

        update_item = item.update_item()

        self.search_result = get_entity(name, self.search_type)

        if update_item:
            self.back(
                self.go_parent,
                name=self.search_name,
                entity=self.search_result,
                type_=self.search_type,
                search_parent_name=self.search_parent_name,
                parent_name=self.parent_name,
                parent_type=self.parent_type,
                is_edit=True
            )
        else:
            popup_showinfo('Something went wrong, try again!')
