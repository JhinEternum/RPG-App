from src.wiki.create.create_category import CreateCategory
from src.wiki.wiki_chapter import WikiChapter
from src.wiki.wiki_home import WikiHome
from src.wiki.wiki_section import WikiSection
from src.wiki.wiki_topic import WikiTopic


class WikiWidget:
    def __init__(self, **kwargs):
        factory = kwargs['factory']

        if factory == 'home':
            WikiHome(**kwargs)
        elif factory == 'section':
            WikiSection(**kwargs)
        elif factory == 'chapter':
            WikiChapter(**kwargs)
        elif factory == 'topic':
            WikiTopic(**kwargs)
        elif factory == 'create_category':
            CreateCategory(**kwargs)
