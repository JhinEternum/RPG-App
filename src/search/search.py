from src.connection.database import get_entity
from src.frames.scroll_frame import TemplateScrollFrame
from src.search.search_widget import SearchWidget


class Search(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']
        self.name = kwargs['name']
        self.type = kwargs['type_']

        self.show_interface = kwargs['show_interface']

        self.search_widget = SearchWidget(
            interface_result=self.interface_result,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            **kwargs
        )

        self.set_widgets_conf()
        self.set_buttons_conf()

    def interface_result(self, entity: str) -> None:
        print(entity)

        entity = get_entity(entity, self.type)
        self.show_interface(
            name=self.name,
            entity=entity,
            type_=self.type
        )
