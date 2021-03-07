from src.frames.scroll_frame import TemplateScrollFrame
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
        pass
