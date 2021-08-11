from src.connection import handle_users


class Avatar:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = kwargs['type']
        self.strength_lv = kwargs['strength_lv']
        self.magic_lv = kwargs['magic_lv']
        self.health = kwargs['health']
        self.adrenaline = kwargs['adrenaline']
        self.classes = kwargs['_class'] if '_class' in kwargs else None
        self.items = kwargs['items'] if 'items' in kwargs else None
        self.physical_ability = kwargs['physical_ability']
        self.titles = kwargs['titles'] if 'titles' in kwargs else None
        self.abilities = kwargs['abilities'] if 'abilities' in kwargs else None
        self.proficiencies = kwargs['proficiencies'] if 'proficiencies' in kwargs else None
        self.description = kwargs['description']

    def create_character(self) -> bool:
        return handle_users.add_user(self)

    def update_user(self, current_name) -> bool:
        return handle_users.update_user(self, current_name)
