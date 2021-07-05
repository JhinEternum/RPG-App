from src.wiki.entity import Entity


class Topic(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chapter_id: int = kwargs['chapter_id']
