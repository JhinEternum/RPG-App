from src.wiki.frames.wiki_scroll_frame import WikiScrollFrame
from src.wiki.wiki_widget import WikiWidget


class WikiFactory(WikiScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        kwargs['back'] = self.back

        self.wiki_widget = WikiWidget(
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            bind_label=self.template_scroll.bind_label,
            **kwargs
        )
        self.append_to_frames(self.wiki_widget)

        self.set_widgets_conf()
        self.set_buttons_conf()
