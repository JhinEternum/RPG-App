from .database import DatabaseConnection
from ..title.title import Title


def add_title(title: Title, users_names) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO titles (name, description, requirements) VALUES (?, ?, ?)',
                       (title.name, title.description, title.requirements))

        title_id = cursor.lastrowid

        if users_names is not None and len(users_names) > 0:
            for user_name in users_names:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title_id, user_name))

    return True


def update_title(title: Title) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE titles SET name=?, description=?, requirements=? WHERE id=?',
                       (title.name, title.description, title.requirements, title.id))

    return True


def get_titles():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM titles ORDER BY name')

        entity = get_titles_attributes(cursor)

    return entity


def get_titles_by_id(title_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM titles WHERE id=?', (title_id,))

        entity = get_titles_attributes(cursor)

    return entity


def get_search_title(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM titles WHERE name LIKE ? ORDER BY name',
                       ('%' + name + '%',))

        titles = get_titles_attributes(cursor)

    return titles


def get_titles_attributes(cursor):
    return [Title(**{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'requirements': row[3]
    }) for row in cursor.fetchall()]
