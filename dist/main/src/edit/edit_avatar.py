import tkinter as tk
from tkinter import ttk, font

from src.avatar.avatar import Avatar
from src.avatar.avatar_properties import get_entities_ids, get_entity_ids
from src.connection.database import get_entity, get_search_entities
from src.connection.handle_abilities import get_abilities_by_type
from src.connection.handle_classes import get_classes
from src.connection.handle_items import get_item_by_type
from src.connection.handle_proficiencies import get_proficiencies
from src.connection.handle_titles import get_titles
from src.connection.handle_users import get_user_type_by_name
from src.edit.edit_functions import set_stored_items, set_stored_entity
from src.edit.edit_template import EditTemplate
from src.methods import handle_selection_change, get_text_data, popup_showinfo
from styles import BUTTON_BACKGROUND_COLOR2, WHITE_COLOR


class EditAvatar(EditTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        widgets = kwargs['widgets']
        buttons = kwargs['buttons']

        self.font = font.Font(size=11)

        self.type_values = ('Character', 'NPC', 'Monster')

        self.lv_values = ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5')

        self.classes_total = get_classes()
        self.classes = ['None'] + [_class['name'] for _class in self.classes_total]

        self.armors_total = get_item_by_type(1)
        self.armors = ['None'] + [armor.name for armor in self.armors_total]

        self.weapons_total = get_item_by_type(2)
        self.weapons = ['None'] + [weapon.name for weapon in self.weapons_total]

        self.titles_total = get_titles()
        self.titles = ['None'] + [title.name for title in self.titles_total]

        self.abilities_total = get_abilities_by_type(1) + get_abilities_by_type(2) + get_abilities_by_type(3)
        self.abilities = ['None'] + [ability.name for ability in self.abilities_total]

        self.proficiencies_total = get_proficiencies()
        self.proficiencies = ['None'] + [proficiency.name for proficiency in self.proficiencies_total]

        self.entity: Avatar

        # --- Attributes ---
        self.name = tk.StringVar(value=self.entity.name)
        self.type = tk.StringVar(value=self.type_values[self.entity.type - 1])
        self.strength_lv = tk.StringVar(value=self.lv_values[self.entity.strength_lv - 1])
        self.magic_lv = tk.StringVar(value=self.lv_values[self.entity.magic_lv - 1])
        self.health = tk.StringVar(value=self.entity.health)
        self.adrenaline = tk.StringVar(value=self.entity.adrenaline)
        self.class_ = tk.StringVar(value=self.classes)
        self.armor = tk.StringVar(value=self.generate_armor())
        self.weapon = tk.StringVar(value=self.weapons)
        self.physical_ability = tk.StringVar(value=self.entity.physical_ability)
        self.title = tk.StringVar(value=self.titles)
        self.ability = tk.StringVar(value=self.abilities)
        self.proficiency = tk.StringVar(value=self.proficiencies)

        # --- Widgets ---
        self.class_entry = tk.Listbox()
        self.weapon_entry = tk.Listbox()
        self.title_entry = tk.Listbox()
        self.ability_entry = tk.Listbox()
        self.proficiency_entry = tk.Listbox()
        self.description_entry = tk.Text()

        self.set_widgets(widgets)
        if buttons is not None:
            self.set_buttons(buttons)

    def set_widgets(self, widgets) -> None:
        # --- Name ---
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
            textvariable=self.type,
            values=self.type_values,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")

        # --- Strength Level ---
        strength_lv_label = ttk.Label(
            widgets,
            text='Strength Lv'
        )
        strength_lv_label.grid(row=2, column=0, sticky='EW')

        strength_lv_entry = ttk.Combobox(
            widgets,
            textvariable=self.strength_lv,
            values=self.lv_values,
            state="readonly"
        )
        strength_lv_entry.grid(row=2, column=1, sticky='EW')

        # --- Magic Level ---
        magic_lv_label = ttk.Label(
            widgets,
            text='Magic Lv'
        )
        magic_lv_label.grid(row=3, column=0, sticky='EW')

        magic_lv_entry = ttk.Combobox(
            widgets,
            textvariable=self.magic_lv,
            values=self.lv_values,
            state="readonly"
        )
        magic_lv_entry.grid(row=3, column=1, sticky='EW')

        # --- Health ---
        health_label = ttk.Label(
            widgets,
            text="Health"
        )
        health_label.grid(row=4, column=0, sticky="EW")

        health_entry = ttk.Entry(
            widgets,
            textvariable=self.health,
            width=60
        )
        health_entry.grid(row=4, column=1, sticky="EW")

        # --- Adrenaline ---
        adrenaline_label = ttk.Label(
            widgets,
            text="Adrenaline"
        )
        adrenaline_label.grid(row=5, column=0, sticky="EW")

        adrenaline_entry = ttk.Entry(
            widgets,
            textvariable=self.adrenaline
        )
        adrenaline_entry.grid(row=5, column=1, sticky="EW")

        # --- Physical Ability ---
        physical_ability_label = ttk.Label(
            widgets,
            text="Physical Ab."
        )
        physical_ability_label.grid(row=6, column=0, sticky="EW")

        physical_ability_entry = ttk.Entry(
            widgets,
            textvariable=self.physical_ability
        )
        physical_ability_entry.grid(row=6, column=1, sticky="EW")

        # --- Class ---
        class_label = ttk.Label(
            widgets,
            text="Class"
        )
        class_label.grid(row=7, column=0, sticky="EW")

        self.class_entry = tk.Listbox(
            widgets,
            listvariable=self.class_,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            background=BUTTON_BACKGROUND_COLOR2,
            borderwidth=0,
            fg=WHITE_COLOR,
            font=self.font,
            width=1,
            height=5
        )
        self.class_entry.grid(row=7, column=1, sticky="EW")

        set_stored_items(self.class_entry, self.entity.classes, self.classes)

        class_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        class_scrollbar.config(command=self.class_entry.yview)
        class_scrollbar.grid(row=7, column=2, sticky="NS")

        self.class_entry.config(yscrollcommand=class_scrollbar.set)

        # --- Armor ---
        armor_label = ttk.Label(
            widgets,
            text="Armor"
        )
        armor_label.grid(row=8, column=0, sticky="EW")

        armor_entry = ttk.Combobox(
            widgets,
            textvariable=self.armor,
            values=self.armors,
            state="readonly"
        )
        armor_entry.grid(row=8, column=1, sticky="EW")

        # --- Weapon ---
        weapon_label = ttk.Label(
            widgets,
            text="Weapon"
        )
        weapon_label.grid(row=9, column=0, sticky="EW")

        self.weapon_entry = tk.Listbox(
            widgets,
            listvariable=self.weapon,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            background=BUTTON_BACKGROUND_COLOR2,
            borderwidth=0,
            fg=WHITE_COLOR,
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=9, column=1, sticky="EW")

        set_stored_entity(self.weapon_entry, self.get_user_weapons(), self.weapons)

        weapon_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        weapon_scrollbar.config(command=self.weapon_entry.yview)
        weapon_scrollbar.grid(row=9, column=2, sticky="NS")

        self.weapon_entry.config(yscrollcommand=weapon_scrollbar.set)

        # --- Title ---
        title_label = ttk.Label(
            widgets,
            text="Title"
        )
        title_label.grid(row=10, column=0, sticky="EW")

        self.title_entry = tk.Listbox(
            widgets,
            listvariable=self.title,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            background=BUTTON_BACKGROUND_COLOR2,
            borderwidth=0,
            fg=WHITE_COLOR,
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=10, column=1, sticky="EW")

        set_stored_entity(self.title_entry, self.entity.titles, self.titles)

        title_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        title_scrollbar.config(command=self.title_entry.yview)
        title_scrollbar.grid(row=10, column=2, sticky="NS")

        self.title_entry.config(yscrollcommand=title_scrollbar.set)

        # --- Ability ---
        ability_label = ttk.Label(
            widgets,
            text="Ability"
        )
        ability_label.grid(row=11, column=0, sticky="EW")

        self.ability_entry = tk.Listbox(
            widgets,
            listvariable=self.ability,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            background=BUTTON_BACKGROUND_COLOR2,
            borderwidth=0,
            fg=WHITE_COLOR,
            font=self.font,
            width=1,
            height=5
        )
        self.ability_entry.grid(row=11, column=1, sticky="EW")

        set_stored_entity(self.ability_entry, self.entity.abilities, self.abilities)

        ability_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        ability_scrollbar.config(command=self.ability_entry.yview)
        ability_scrollbar.grid(row=11, column=2, sticky="NS")

        self.ability_entry.config(yscrollcommand=ability_scrollbar.set)

        # --- Proficiency ---
        proficiency_label = ttk.Label(
            widgets,
            text="Proficiency"
        )
        proficiency_label.grid(row=12, column=0, sticky="EW")

        self.proficiency_entry = tk.Listbox(
            widgets,
            listvariable=self.proficiency,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            background=BUTTON_BACKGROUND_COLOR2,
            borderwidth=0,
            fg=WHITE_COLOR,
            font=self.font,
            width=1,
            height=5
        )
        self.proficiency_entry.grid(row=12, column=1, sticky="EW")

        # set_stored_items(self.proficiency_entry, self.user_proficiencies, self.proficiencies)
        set_stored_entity(self.proficiency_entry, self.entity.proficiencies, self.proficiencies)

        proficiency_scrollbar = ttk.Scrollbar(widgets, orient="vertical")
        proficiency_scrollbar.config(command=self.proficiency_entry.yview)
        proficiency_scrollbar.grid(row=12, column=2, sticky="NS")

        self.proficiency_entry.config(yscrollcommand=proficiency_scrollbar.set)

        # --- Description ---
        description_label = ttk.Label(
            widgets,
            text="Description"
        )
        description_label.grid(row=13, column=0, sticky="EW")

        self.description_entry = tk.Text(
            widgets,
            width=1,
            height=5,
            background=BUTTON_BACKGROUND_COLOR2,
            foreground=WHITE_COLOR
        )
        self.description_entry.grid(row=13, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=13, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.entity.description)

    def set_buttons(self, buttons) -> None:
        search_result = get_entity(self.name.get(), self.search_type)

        separator = ttk.Separator(
            buttons
        )
        separator.grid(row=0, columnspan=1)

        save_button = ttk.Button(
            buttons,
            text='  Save',
            command=lambda: self.save(set_proficiencies=self.set_proficiencies, edit=self.edit),
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
                True,
                name=self.search_name,
                entity=search_result,
                type_=self.search_type
            ),
            style='DarkButton.TButton',
            image=self.back_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        back_button.grid(row=2)

    def set_proficiencies(self) -> dict:
        proficiency = handle_selection_change(self.proficiency_entry, self.proficiencies)
        proficiency_result = get_entity_ids(self.proficiencies_total, proficiency)

        print(proficiency)
        print(self.entity.proficiencies)
        print(proficiency_result)

        if len(proficiency) > 0:
            result = {
                'proficiency': proficiency,
                'proficiency_result': proficiency_result,
                'edit': self.edit,
                'user_proficiencies': self.entity.proficiencies
            }
            return result

    def edit(self, proficiencies=None) -> None:
        if proficiencies is None:
            proficiencies = []

        items = []

        name = self.name.get()

        type_ = self.type.get()
        type_result = get_user_type_by_name(type_)

        strength_lv = int(self.strength_lv.get()[6])
        magic_lv = int(self.magic_lv.get()[6])

        health = self.health.get()
        adrenaline = self.adrenaline.get()

        print(f'classes: {self.classes}')

        class_ = handle_selection_change(self.class_entry, self.classes)
        class_result = []
        if len(class_) > 0:
            class_result = get_entities_ids(self.classes_total, class_)

        armor = [self.armor.get()]
        weapon = handle_selection_change(self.weapon_entry, self.weapons)
        physical_ability = self.physical_ability.get()

        title = handle_selection_change(self.title_entry, self.titles)
        title_result = get_entity_ids(self.titles_total, title)

        ability = handle_selection_change(self.ability_entry, self.abilities)
        ability_result = get_entity_ids(self.abilities_total, ability)

        description = get_text_data(self.description_entry)

        if len(armor) == 1 and armor[0] == 'None':
            armor = []

        if armor:
            items += get_entity_ids(self.armors_total, armor)

        if weapon:
            items += get_entity_ids(self.weapons_total, weapon)

        avatar = Avatar(
            name=name,
            type=type_result,
            strength_lv=strength_lv,
            magic_lv=magic_lv,
            health=health,
            adrenaline=adrenaline,
            classes=class_result,
            items=items,
            physical_ability=physical_ability,
            titles=title_result,
            abilities=ability_result,
            proficiencies=proficiencies,
            description=description
        )

        edit_avatar = avatar.update_user(self.entity.name)

        search_result = get_search_entities(self.search_name, self.search_type)
        entity = get_entity(name, self.search_type)

        print('---------------------------------')
        print(self.search_name)
        print(search_result)
        print(self.search_type)

        if edit_avatar:
            self.back(
                True,
                name=self.search_name,
                entity=entity,
                entities=search_result,
                type_=self.search_type
            )
        else:
            popup_showinfo('Something went wrong, try again!')

    def generate_armor(self):
        # [item for item in self.entity.items if item.type != 1]

        for item in self.entity.items:
            if item.type == 1:
                return item.name

        return 'None'

    def get_user_weapons(self) -> list:
        weapons = [item for item in self.entity.items if item.type != 1]
        return weapons
