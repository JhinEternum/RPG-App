from src.connection.handle_proficiencies import add_proficiency, update_proficiency


class Proficiency:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']

        self.proficiency = {
            'name': self.name,
            'description': self.description
        }

    def create_proficiency(self) -> bool:
        return add_proficiency(self.proficiency)

    def update_proficiency(self, id_) -> bool:
        return update_proficiency(self.proficiency, id_)
