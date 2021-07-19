from src.connection.handle_users import add_user, update_user


class Avatar:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type_']
        self.strength_lv = kwargs['strength_lv']
        self.magic_lv = kwargs['magic_lv']
        self.health = kwargs['health']
        self.adrenaline = kwargs['adrenaline']
        self.classes = kwargs['class_']
        self.items = kwargs['items']
        self.physical_ability = kwargs['physical_ability']
        self.titles = kwargs['titles']
        self.abilities = kwargs['abilities']
        self.proficiency = kwargs['proficiency']
        self.description = kwargs['description']

        self.avatar = {
            'name': self.name,
            'type': self.type,
            'strength_lv': self.strength_lv,
            'magic_lv': self.magic_lv,
            'health': self.health,
            'adrenaline': self.adrenaline,
            'class': self.classes,
            'items': self.items,
            'physical_ability': self.physical_ability,
            'titles': self.titles,
            'abilities': self.abilities,
            'proficiency': self.proficiency,
            'description': self.description
        }

    def create_character(self) -> bool:
        return add_user(self)

    def update_user(self, current_name) -> bool:
        return update_user(self, current_name)
