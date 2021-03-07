from src.frames.normal_frame import TemplateFrame
from src.home.home_widget import HomeWidget


class Home(TemplateFrame):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        create_entity = kwargs['create_entity']
        proficiencies_level = kwargs['proficiencies_level']

        self.home_widget = HomeWidget(
            parent=self,
            create_entity=create_entity,
            widgets=self.widgets,
            buttons=self.buttons,
            proficiencies_level=proficiencies_level
        )
        self.set_widgets_conf()
        self.set_buttons_conf()
