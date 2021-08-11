from src.connection import handle_proficiencies


class Proficiency:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']

        self.id = kwargs['id'] if 'id' in kwargs else None
        self.level = kwargs['level'] if 'level' in kwargs else None
        self.rank = kwargs['rank'] if 'rank' in kwargs else None

    def create_proficiency(self) -> bool:
        return handle_proficiencies.add_proficiency(self)

    def update_proficiency(self, id_) -> bool:
        return handle_proficiencies.update_proficiency(self, id_)
