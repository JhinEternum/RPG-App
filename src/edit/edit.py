from src.frames.scroll_frame import TemplateScrollFrame
from src.edit.edit_widget import EditWidget


class Edit(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.type = kwargs['type_']
        self.show_proficiencies_level = kwargs['show_proficiencies_level']

        self.edit_widget = EditWidget(
            save=self.save,
            back=self.back,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            bind_label=self.template_scroll.bind_label,
            **kwargs
        )

        self.set_widgets_conf()
        self.set_buttons_conf()

    def save(self, **kwargs) -> None:
        edit = kwargs['edit']
        if self.type == 'Character' or self.type == 'NPC' or self.type == 'Monster':
            set_proficiencies = kwargs['set_proficiencies']
            proficiency = set_proficiencies()

            if proficiency is not None:
                proficiencies = proficiency['proficiency']
                proficiency_result = proficiency['proficiency_result']
                user_proficiencies = proficiency['user_proficiencies']
                self.show_proficiencies_level(
                    proficiencies=proficiencies,
                    proficiency_result=proficiency_result,
                    edit=edit,
                    user_proficiencies=user_proficiencies
                )
            else:
                edit()
        else:
            edit()
