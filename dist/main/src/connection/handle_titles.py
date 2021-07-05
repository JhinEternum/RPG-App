from .database import *
from .database import DatabaseConnection


def add_title(title, users_names) -> bool:
    name = title['name']
    description = title['description']
    requirements = title['requirements']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO titles (name, description, requirements) VALUES (?, ?, ?)',
                       (name, description, requirements))

        title_id = cursor.lastrowid

        if users_names is not None and len(users_names) > 0:
            for user_name in users_names:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title_id, user_name))

    return True


def update_title(title, id_) -> bool:
    name = title['name']
    description = title['description']
    requirements = title['requirements']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE titles SET name=?, description=?, requirements=? WHERE id=?',
                       (name, description, requirements, id_))

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


def get_titles_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'requirements': row[3]
    } for row in cursor.fetchall()]


def get_title_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'requirements': row[3]
    } for row in cursor.fetchall()][0]
