class Entity:
    def __init__(self, **kwargs):
        self.id: int = kwargs['id']
        self.name: str = kwargs['name']
        self.description: str = kwargs['description']