from src.connection import handle_titles


class Title:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.requirements = kwargs['requirements']
        self.description = kwargs['description']
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.users = kwargs['users'] if 'users' in kwargs else None

    def create_title(self) -> bool:
        return handle_titles.add_title(self, self.users)

    def update_title(self, id_) -> bool:
        return handle_titles.update_title(self, id_)
