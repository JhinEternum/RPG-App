import tkinter as tk
from tkinter import ttk, font

from src.creation.create_template import CreateTemplate
from src.images.image import get_item
from styles import BUTTON_BACKGROUND_COLOR2, WHITE_COLOR


class ItemWidget(CreateTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_item = kwargs['create_item'] if 'create_item' in kwargs else None
        widgets = kwargs['widgets']
        buttons = kwargs['buttons'] if 'buttons' in kwargs else None

        self.font = font.Font(size=11)

        self.item_icon = get_item()

        self.types_ = ('Armor', 'Weapon')

        # --- Attributes ---
        self.item = 'Item ' + self.frame_id
        self.name = tk.StringVar()
        self.type_ = tk.StringVar(value=self.types_[0])
        self.reduction = tk.StringVar(value='0')
        self.damage = tk.StringVar(value='0')
        self.range_ = tk.StringVar(value='0')
        self.health = tk.StringVar(value='0')
        self.area = tk.StringVar(value='0')

        self.character = tk.StringVar(value=self.characters[1])
        self.npc = tk.StringVar(value=self.npcs[0])
        self.monster = tk.StringVar(value=self.monsters[0])

        # --- Widgets ---
        self.character_menu = ttk.Combobox()
        self.npc_menu = ttk.Combobox()
        self.monster_menu = ttk.Combobox()

        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Item ---
        item_label = ttk.Label(
            widgets,
            text=self.item
        )
        item_label.grid(row=0, column=0, sticky="EW")

        item_separator = ttk.Separator(
            widgets
        )
        item_separator.grid(row=1, column=0, columnspan=3, sticky="EW")

        # --- Name ---
        name_label = ttk.Label(
            widgets,
            text="Name"
        )
        name_label.grid(row=2, column=0, sticky="EW")

        name_entry = ttk.Entry(
            widgets,
            textvariable=self.name,
            width=60
        )
        name_entry.grid(row=2, column=1, sticky="EW")

        # --- User ---
        user_label = ttk.Label(
            widgets,
            text="User"
        )
        user_label.grid(row=3, column=0, sticky="EW")

        self.character_menu = ttk.Combobox(
            widgets,
            name='character',
            textvariable=self.character,
            values=self.characters,
            state="readonly"
        )
        self.character_menu.grid(row=3, column=1, sticky="EW")

        # --- NPC ---
        self.npc_menu = ttk.Combobox(
            widgets,
            name='npc',
            textvariable=self.npc,
            values=self.npcs,
            state="readonly"
        )
        self.npc_menu.grid(row=4, column=1, sticky="EW")

        # --- Monster ---
        self.monster_menu = ttk.Combobox(
            widgets,
            name='monster',
            textvariable=self.monster,
            values=self.monsters,
            state="readonly"
        )
        self.monster_menu.grid(row=5, column=1, sticky="EW")

        self.character_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.npc_menu.bind("<<ComboboxSelected>>", self.selected_value)
        self.monster_menu.bind("<<ComboboxSelected>>", self.selected_value)

        # --- Type ---
        type_label = ttk.Label(
            widgets,
            text="Type"
        )
        type_label.grid(row=6, column=0, sticky="EW")

        type_entry = ttk.Combobox(
            widgets,
            textvariable=self.type_,
            values=self.types_,
            exportselection=False,
            state="readonly"
        )
        type_entry.grid(row=6, column=1, sticky="EW")

        # --- Reduction ---
        reduction_label = ttk.Label(
            widgets,
            text="Reduction"
        )
        reduction_label.grid(row=7, column=0, sticky="EW")

        reduction_entry = ttk.Entry(
            widgets,
            textvariable=self.reduction,
            width=60
        )
        reduction_entry.grid(row=7, column=1, sticky="EW")

        # --- Damage ---
        damage_label = ttk.Label(
            widgets,
            text="Damage"
        )
        damage_label.grid(row=8, column=0, sticky="EW")

        damage_entry = ttk.Entry(
            widgets,
            textvariable=self.damage,
            width=60
        )
        damage_entry.grid(row=8, column=1, sticky="EW")

        # --- Range ---
        range_label = ttk.Label(
            widgets,
            text="Range"
        )
        range_label.grid(row=9, column=0, sticky="EW")

        range_entry = ttk.Entry(
            widgets,
            textvariable=self.range_,
            width=60
        )
        range_entry.grid(row=9, column=1, sticky="EW")

        # --- Health ---
        health_label = ttk.Label(
            widgets,
            text="Health"
        )
        health_label.grid(row=10, column=0, sticky="EW")

        health_entry = ttk.Entry(
            widgets,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=10, column=1, sticky="EW")

        # --- Area ---
        area_label = ttk.Label(
            widgets,
            text="Area"
        )
        area_label.grid(row=11, column=0, sticky="EW")

        area_entry = ttk.Entry(
            widgets,
            textvariable=self.area,
            width=60
        )
        area_entry.grid(row=11, column=1, sticky="EW")

        # --- Effects ---
        effects_label = ttk.Label(
            widgets,
            text="Effects"
        )
        effects_label.grid(row=13, column=0, sticky="EW")

        self.effects_entry = tk.Text(
            widgets,
            width=1,
            height=15,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.effects_entry.grid(row=13, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=13, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, 'None')

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=14, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.description_entry.grid(row=14, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=14, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, 'None')

    def selected_value(self, event):
        selected_entity = str(event.widget).split(".")[-1]

        if selected_entity == 'character':
            self.npc_menu.current(0)
            self.monster_menu.current(0)
        elif selected_entity == 'npc':
            self.character_menu.current(0)
            self.monster_menu.current(0)
        elif selected_entity == 'monster':
            self.character_menu.current(0)
            self.npc_menu.current(0)

    def set_buttons(self, buttons) -> None:
        title_separator = ttk.Separator(
            buttons
        )
        title_separator.grid(row=0, columnspan=1)

        create_button = ttk.Button(
            buttons,
            text='  Create Item',
            command=self.create_item,
            style='DarkButton.TButton',
            image=self.confirm_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        create_button.grid(row=1)

        add_button = ttk.Button(
            buttons,
            text='Add Item',
            command=self.add_entity_frame,
            style='DarkButton.TButton',
            image=self.item_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        add_button.grid(row=2)
