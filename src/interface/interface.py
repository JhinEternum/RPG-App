from src.frames.scroll_frame import TemplateScrollFrame
from src.interface.interface_widget import InterfaceWidget


class Interface(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.interface_widget = InterfaceWidget(
            back=self.back,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            bind_label=self.template_scroll.bind_label,
            **kwargs
        )

        self.set_widgets_conf()
        self.set_buttons_conf()
