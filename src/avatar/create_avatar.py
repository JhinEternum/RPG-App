from src.avatar.avatar import Avatar
from src.avatar.avatar_properties import get_entities_ids, get_user_types_ids
from src.avatar.avatar_widget import AvatarWidget
from src.frames.scroll_frame import TemplateScrollFrame
from src.methods import handle_selection_change, get_text_data, popup_showinfo


class CreateAvatar(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']
        self.proficiencies_level = kwargs['extra_frame']

        self.avatar_widget = AvatarWidget(
            set_proficiencies=self.set_proficiencies,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons
        )
        self.set_widgets_conf()
        self.set_buttons_conf()

    def set_proficiencies(self) -> None:
        proficiencies = handle_selection_change(self.avatar_widget.proficiency_entry, self.avatar_widget.proficiencies)
        proficiency_result = get_entities_ids(self.avatar_widget.proficiencies_total, proficiencies)

        if len(proficiencies) > 0:
            self.proficiencies_level(
                proficiencies=proficiencies,
                proficiency_result=proficiency_result,
                create_avatar=self
            )
        else:
            self.create_avatar()

    def create_avatar(self, proficiencies=None) -> None:
        if proficiencies is None:
            proficiencies = []

        widgets = self.avatar_widget
        items = []

        name = widgets.name.get()

        type_ = widgets.type.get()
        type_result = get_user_types_ids(type_)

        strength_lv = int(widgets.strength_lv.get()[6])
        magic_lv = int(widgets.magic_lv.get()[6])

        health = widgets.health.get()
        adrenaline = widgets.adrenaline.get()

        class_ = handle_selection_change(widgets.class_entry, widgets.classes)
        class_result = get_entities_ids(widgets.classes_total, class_)

        armor = [widgets.armor.get()]
        weapon = handle_selection_change(widgets.weapon_entry, widgets.weapons)
        physical_ability = widgets.physical_ability.get()

        title = handle_selection_change(widgets.title_entry, widgets.titles)
        title_result = get_entities_ids(widgets.titles_total, title)

        ability = handle_selection_change(widgets.ability_entry, widgets.abilities)
        ability_result = get_entities_ids(widgets.abilities_total, ability)

        description = get_text_data(widgets.description_entry)

        if len(armor) == 1 and armor[0] == 'None':
            armor = []

        if armor:
            items += get_entities_ids(widgets.armors_total, armor)

        if weapon:
            items += get_entities_ids(widgets.weapons_total, weapon)

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

        create_avatar = avatar.create_character()

        self.home() if create_avatar else popup_showinfo(create_avatar)

