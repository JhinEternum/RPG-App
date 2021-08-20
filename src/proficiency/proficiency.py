from src.connection import handle_proficiencies
from src.images.image import get_proficiencies


class Proficiency:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.icon = kwargs['icon'] if 'icon' in kwargs else None

        self.id = kwargs['id'] if 'id' in kwargs else None
        self.level = kwargs['level'] if 'level' in kwargs else None
        self.rank = kwargs['rank'] if 'rank' in kwargs else None

        if self.icon != 'none' and self.icon:
            self.icon = get_proficiencies(self.icon)

    def create_proficiency(self) -> bool:
        return handle_proficiencies.add_proficiency(self)

    def update_proficiency(self) -> bool:
        return handle_proficiencies.update_proficiency(self)
