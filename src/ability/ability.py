from src.connection.handle_abilities import add_ability, update_ability


class Ability:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.casting = kwargs['casting']
        self.components = kwargs['components']
        self.requirements = kwargs['requirements']
        self.conditions = kwargs['conditions']
        self.effects = kwargs['effects']
        self.description = kwargs['description']
        self.type_ = kwargs['type_']
        self.user = kwargs['user'] if 'user' in kwargs else None

        self.ability = {
            'name': self.name,
            'type': self.type_,
            'casting': self.casting,
            'components': self.components,
            'requirements': self.requirements,
            'conditions': self.conditions,
            'effects': self.effects,
            'description': self.description
        }

    def create_ability(self) -> bool:
        return add_ability(self.ability, self.user)

    def update_ability(self, id_) -> bool:
        return update_ability(self.ability, id_)
