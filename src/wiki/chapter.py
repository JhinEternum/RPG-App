from src.wiki.entity import Entity


class Chapter(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.section_id: int = kwargs['section_id']
