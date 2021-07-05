from src.frames.scroll_frame import TemplateScrollFrame
from src.methods import popup_showinfo, get_text_data
from src.proficiency.proficiency import Proficiency
from src.proficiency.proficiency_widget import ProficiencyWidget


class CreateProficiency(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']

        self.proficiency_widget = ProficiencyWidget(
            create_proficiency=self.create_proficiency,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            add_entity_frame=lambda: self.template_scroll.add_entity_frame(ProficiencyWidget)
        )

        self.set_widgets_conf()
        self.set_buttons_conf()
        self.append_to_frames(self.proficiency_widget)

    def create_proficiency(self) -> None:
        for proficiency_frame in self.template_scroll.frames:
            name = proficiency_frame.name.get()
            description = get_text_data(proficiency_frame.description_entry)

            proficiency = Proficiency(
                name=name,
                description=description
            )

            create_proficiency = proficiency.create_proficiency()

            self.home() if create_proficiency else popup_showinfo('Something went wrong, please, try again!')
