from src.frames.scroll_frame import TemplateScrollFrame
from src.search.search_widget import SearchWidget


class Search(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']

        self.search_widget = SearchWidget(
            interface_result=self.interface_result,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            **kwargs
        )

        self.set_widgets_conf()
        self.set_buttons_conf()

    def interface_result(self, entity: str) -> None:
        pass
