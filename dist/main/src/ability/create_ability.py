from src.ability.ability import Ability
from src.ability.ability_widget import AbilityWidget
from src.frames.scroll_frame import TemplateScrollFrame
from src.methods import get_text_data, choose_user_ability, popup_showinfo


class CreateAbility(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']

        self.ability_widget = AbilityWidget(
            create_ability=self.create_ability,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            add_entity_frame=lambda: self.template_scroll.add_entity_frame(AbilityWidget)
        )

        self.set_widgets_conf()
        self.set_buttons_conf()
        self.append_to_frames(self.ability_widget)

    def create_ability(self) -> None:
        for ability_frame in self.template_scroll.frames:
            character = ability_frame.character.get()
            npc = ability_frame.npc.get()
            monster = ability_frame.monster.get()
            item = ability_frame.item.get()

            user, type_ = choose_user_ability(character, npc, monster, item)

            print(f'user: {user} type: {type_}')

            name = ability_frame.name.get()
            casting = ability_frame.casting.get()
            components = ability_frame.components.get()
            requirements = get_text_data(ability_frame.requirements_entry)
            conditions = get_text_data(ability_frame.conditions_entry)
            effects = get_text_data(ability_frame.effects_entry)
            description = get_text_data(ability_frame.description_entry)

            ability = Ability(
                name=name,
                casting=casting,
                components=components,
                requirements=requirements,
                conditions=conditions,
                effects=effects,
                description=description,
                type_=type_,
                user=user
            )

            create_ability = ability.create_ability()

            self.home() if create_ability else popup_showinfo('Something went wrong, please, try again!')
