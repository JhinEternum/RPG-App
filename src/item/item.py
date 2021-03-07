from src.connection.handle_items import add_item, update_item


class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type_ = kwargs['type_']
        self.reduction = kwargs['reduction']
        self.damage = kwargs['damage']
        self.range_ = kwargs['range_']
        self.health = kwargs['health']
        self.area = kwargs['area']
        self.abilities = kwargs['abilities']
        self.effects = kwargs['effects']
        self.description = kwargs['description']
        self.user = kwargs['user'] if 'user' in kwargs else None

        self.item = {
            'name': self.name,
            'type': self.type_,
            'reduction': self.reduction,
            'damage': self.damage,
            'range': self.range_,
            'health': self.health,
            'area': self.area,
            'abilities': self.abilities,
            'effects': self.effects,
            'description': self.description
        }

    def create_item(self) -> bool:
        return add_item(self.item, self.user)

    def update_item(self, id_) -> bool:
        return update_item(self.item, id_)
