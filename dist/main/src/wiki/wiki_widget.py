from src.wiki.wiki_home import WikiHome


class WikiWidget:
    def __init__(self, **kwargs):
        factory = kwargs['factory']

        if factory == 'home':
            WikiHome(**kwargs)
