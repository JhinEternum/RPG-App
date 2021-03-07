from src.connection.handle_titles import add_title, update_title


class Title:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.requirements = kwargs['requirements']
        self.description = kwargs['description']
        self.users = kwargs['users'] if 'users' in kwargs else None

        self.title = {
            'name': self.name,
            'requirements': self.requirements,
            'description': self.description
        }

    def create_title(self) -> bool:
        return add_title(self.title, self.users)

    def update_title(self, id_) -> bool:
        return update_title(self.title, id_)
