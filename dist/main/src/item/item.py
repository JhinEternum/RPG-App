from src.connection import handle_items


class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type_'] if 'type_' in kwargs else kwargs['type']
        self.reduction = kwargs['reduction']
        self.damage = kwargs['damage']
        self.range = kwargs['range_'] if 'range_' in kwargs else kwargs['range']
        self.health = kwargs['health']
        self.area = kwargs['area']
        self.effects = kwargs['effects']
        self.description = kwargs['description']
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.user = kwargs['user'] if 'user' in kwargs else None

    def create_item(self) -> bool:
        return handle_items.add_item(self, self.user)

    def update_item(self, id_) -> bool:
        return handle_items.update_item(self, id_)
