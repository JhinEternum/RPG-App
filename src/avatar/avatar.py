from src.connection import handle_users


class Avatar:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type_'] if 'type_' in kwargs else kwargs['type']
        self.strength_lv = kwargs['strength_lv']
        self.magic_lv = kwargs['magic_lv']
        self.health = kwargs['health']
        self.adrenaline = kwargs['adrenaline']
        self.classes = kwargs['class_'] if 'class_' in kwargs else kwargs['class']
        self.items = kwargs['items']
        self.physical_ability = kwargs['physical_ability']
        self.titles = kwargs['titles']
        self.abilities = kwargs['abilities']
        self.proficiency = kwargs['proficiency']
        self.description = kwargs['description']

    def create_character(self) -> bool:
        return handle_users.add_user(self)

    def update_user(self, current_name) -> bool:
        return handle_users.update_user(self, current_name)
