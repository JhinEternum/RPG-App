from src.connection.database import get_search_entities
from src.frames.normal_frame import TemplateFrame
from src.home.home_widget import HomeWidget
from src.methods import popup_showinfo


class Home(TemplateFrame):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        self.show_search = kwargs['show_search']
        self.show_wiki = kwargs['show_wiki']
        self.set_battle = kwargs['set_battle']

        self.home_widget = HomeWidget(
            widgets=self.widgets,
            buttons=self.buttons,
            search=self.search,
            **kwargs
        )
        self.set_widgets_conf()
        self.set_buttons_conf()

    def search(self) -> None:
        name = self.home_widget.name.get()
        type_ = self.home_widget.type.get()

        search_result = get_search_entities(name, type_)

        if search_result:
            self.show_search(
                name=name,
                entities=search_result,
                type_=type_,
                scroll=True,
                single_widgets=True
            )
            self.home_widget.name.set('')
        else:
            popup_showinfo(f"{name} not found!")
