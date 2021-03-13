import tkinter as tk
from tkinter import ttk, font

from src.avatar.avatar import Avatar
from src.avatar.avatar_properties import get_entities_names, get_entities_ids, get_user_types_ids
from src.connection import get_specific_items, get_titles, get_abilities_by_type, get_proficiencies, get_user_classes, \
    get_user_items, get_user_titles, get_user_abilities, get_user_proficiencies, get_entity, get_search_entities
from src.connection.handle_classes import get_classes
from src.edit.edit_functions import set_stored_items
from src.methods import handle_selection_change, get_text_data, popup_showinfo


class EditAvatar:
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

        self.font = font.Font(size=11)

        self.type_values = ('Character', 'NPC', 'Monster')

        self.lv_values = ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5')

        self.classes_total = get_classes()
        self.classes = ['None'] + get_entities_names(self.classes_total)

        self.armors_total = get_specific_items('', 1)
        self.armors = ['None'] + get_entities_names(self.armors_total)

        self.weapons_total = get_specific_items('', 2)
        self.weapons = ['None'] + get_entities_names(self.weapons_total)

        self.titles_total = get_titles()
        self.titles = ['None'] + get_entities_names(self.titles_total)

        self.abilities_total = get_abilities_by_type(1) + get_abilities_by_type(2) + get_abilities_by_type(3)
        self.abilities = ['None'] + get_entities_names(self.abilities_total)

        self.proficiencies_total = get_proficiencies()
        self.proficiencies = ['None'] + get_entities_names(self.proficiencies_total)

        # --- User ---
        self.user_name = self.entity['name']
        self.user_type_ = self.entity['type']
        self.user_strength_lv = self.entity['strength_lv']
        self.user_magic_lv = self.entity['magic_lv']
        self.user_health = self.entity['health']
        self.user_adrenaline = self.entity['adrenaline']
        self.user_physical_ability = self.entity['physical_ability']
        self.user_description = self.entity['description']

        self.user_classes = get_user_classes(self.user_name)
        self.user_items = get_user_items(self.user_name)
        self.user_titles = get_user_titles(self.user_name)
        self.user_abilities = get_user_abilities(self.user_name)
        self.user_proficiencies = get_user_proficiencies(self.user_name)

        # --- Attributes ---
        self.name = tk.StringVar(value=self.user_name)
        self.type = tk.StringVar(value=self.type_values[self.user_type_ - 1])
        self.strength_lv = tk.StringVar(value=self.lv_values[self.user_strength_lv - 1])
        self.magic_lv = tk.StringVar(value=self.lv_values[self.user_magic_lv - 1])
        self.health = tk.StringVar(value=self.user_health)
        self.adrenaline = tk.StringVar(value=self.user_adrenaline)
        self.class_ = tk.StringVar(value=self.classes)
        self.armor = tk.StringVar(value=self.generate_armor())
        self.weapon = tk.StringVar(value=self.weapons)
        self.physical_ability = tk.StringVar(value=self.user_physical_ability)
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
            font=self.font,
            width=1,
            height=5
        )
        self.class_entry.grid(row=7, column=1, sticky="EW")

        set_stored_items(self.class_entry, self.user_classes, self.classes)

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
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=9, column=1, sticky="EW")

        set_stored_items(self.weapon_entry, self.get_user_weapons(), self.weapons)

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
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=10, column=1, sticky="EW")

        set_stored_items(self.title_entry, self.user_titles, self.titles)

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
            font=self.font,
            width=1,
            height=5
        )
        self.ability_entry.grid(row=11, column=1, sticky="EW")

        set_stored_items(self.ability_entry, self.user_abilities, self.abilities)

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
            font=self.font,
            width=1,
            height=5
        )
        self.proficiency_entry.grid(row=12, column=1, sticky="EW")

        set_stored_items(self.proficiency_entry, self.user_proficiencies, self.proficiencies)

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
            height=5
        )
        self.description_entry.grid(row=13, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            widgets,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=13, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, self.user_description)

    def set_buttons(self, buttons) -> None:
        search_result = get_entity(self.name.get(), self.search_type)

        save_button = ttk.Button(
            buttons,
            text='Save',
            command=lambda: self.save(set_proficiencies=self.set_proficiencies, edit=self.edit),
            cursor='hand2'
        )
        save_button.grid(row=0)

        back_button = ttk.Button(
            buttons,
            text='← Back',
            command=lambda: self.back(
                True,
                name=self.search_name,
                entity=search_result,
                type_=self.search_type
            ),
            cursor='hand2'
        )
        back_button.grid(row=1)

    def set_proficiencies(self) -> dict:
        proficiency = handle_selection_change(self.proficiency_entry, self.proficiencies)
        proficiency_result = get_entities_ids(self.proficiencies_total, proficiency)

        print(proficiency)
        print(self.user_proficiencies)
        print(proficiency_result)

        if len(proficiency) > 0:
            result = {
                'proficiency': proficiency,
                'proficiency_result': proficiency_result,
                'edit': self.edit,
                'user_proficiencies': self.user_proficiencies
            }
            return result

    def edit(self, proficiencies=None) -> None:
        if proficiencies is None:
            proficiencies = []

        items = []

        name = self.name.get()

        type_ = self.type.get()
        type_result = get_user_types_ids(type_)

        strength_lv = int(self.strength_lv.get()[6])
        magic_lv = int(self.magic_lv.get()[6])

        health = self.health.get()
        adrenaline = self.adrenaline.get()

        class_ = handle_selection_change(self.class_entry, self.classes)
        class_result = get_entities_ids(self.classes_total, class_)

        armor = [self.armor.get()]
        weapon = handle_selection_change(self.weapon_entry, self.weapons)
        physical_ability = self.physical_ability.get()

        title = handle_selection_change(self.title_entry, self.titles)
        title_result = get_entities_ids(self.titles_total, title)

        ability = handle_selection_change(self.ability_entry, self.abilities)
        ability_result = get_entities_ids(self.abilities_total, ability)

        description = get_text_data(self.description_entry)

        if len(armor) == 1 and armor[0] == 'None':
            armor = []

        if armor:
            items += get_entities_ids(self.armors_total, armor)

        if weapon:
            items += get_entities_ids(self.weapons_total, weapon)

        avatar = Avatar(
            name=name,
            type_=type_result,
            strength_lv=strength_lv,
            magic_lv=magic_lv,
            health=health,
            adrenaline=adrenaline,
            class_=class_result,
            items=items,
            physical_ability=physical_ability,
            titles=title_result,
            abilities=ability_result,
            proficiency=proficiencies,
            description=description
        )

        edit_avatar = avatar.update_user(self.user_name)

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
        for item in self.user_items:
            item_type = item['type']

            if item_type == 1:
                return item['name']

        return 'None'

    def get_user_weapons(self):
        weapons = []

        for item in self.user_items:
            if item['type'] != 1:
                weapons.append(item)

        return weapons