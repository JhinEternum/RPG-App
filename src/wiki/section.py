from src.wiki.entity import Entity


class Section(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category_id: int = kwargs['category_id']
