from src.wiki.wiki import Wiki


class WikiTemplate:
    def __init__(self, **kwargs):
        self.wiki: Wiki = kwargs['wiki']

        self.back = kwargs['back']
        self.show_wiki = kwargs['show_wiki']
        self.widgets = kwargs['widgets']
        self.buttons = kwargs['buttons']
        self.bind_label = kwargs['bind_label']