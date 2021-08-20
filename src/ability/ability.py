from src.connection import handle_abilities


class Ability:
    def __init__(self, **kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.name = kwargs['name']
        self.casting = kwargs['casting']
        self.components = kwargs['components']
        self.requirements = kwargs['requirements']
        self.conditions = kwargs['conditions']
        self.effects = kwargs['effects']
        self.description = kwargs['description']
        self.type = kwargs['type'] if 'type' in kwargs else None
        self.user = kwargs['user'] if 'user' in kwargs else None

    def create_ability(self) -> bool:
        return handle_abilities.add_ability(self, self.user)

    def update_ability(self) -> bool:
        return handle_abilities.update_ability(self)
