from .database import DatabaseConnection
from ..proficiency.proficiency import Proficiency


def add_proficiency(proficiency) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO proficiencies (name, description) VALUES (?, ?)',
                       (proficiency.name, proficiency.description))

    return True


def update_proficiency(proficiency) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE proficiencies SET name=?, description=? WHERE id=?',
                       (proficiency.name, proficiency.description, proficiency.id))

    return True


def get_proficiencies():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM proficiencies ORDER BY name')

        entity = get_proficiencies_attributes(cursor)

    return entity


def get_search_proficiency(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM proficiencies WHERE name LIKE ? ORDER BY name',
                       ('%' + name + '%',))

        proficiencies = get_proficiencies_attributes(cursor)

    return proficiencies


def get_proficiencies_attributes(cursor):
    return [Proficiency(**{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'icon': row[3]
    }) for row in cursor.fetchall()]


def get_proficiencies_by_id(proficiency_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM proficiencies WHERE id=?', (proficiency_id,))

        proficiency = get_proficiencies_attributes(cursor)

    return proficiency
