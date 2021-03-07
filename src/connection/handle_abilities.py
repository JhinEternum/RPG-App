from .database import *
from .database import DatabaseConnection


def add_ability(ability, user) -> bool:
    name = ability['name']
    type_ = ability['type']
    casting = ability['casting']
    components = ability['components']
    requirements = ability['requirements']
    conditions = ability['conditions']
    effects = ability['effects']
    description = ability['description']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO abilities (name, type, casting, components, requirements, conditions, effects, '
                       'description) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, type_, casting, components, requirements, conditions, effects, description))

        ability_id = cursor.lastrowid

        user_types = ['Character', 'NPC', 'Monster']
        ability_types = [1, 2, 3]

        if user not in user_types and type_ in ability_types:
            cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES (?, ?)', (ability_id, user))
        elif user != 'Item' and type_ == 4:
            item = get_specific_items(user, 0)[0]
            item_id = item['id']
            cursor.execute('INSERT INTO items_abilities (ability_id, item_id) VALUES (?, ?)', (ability_id, item_id))

    return True


def update_ability(ability, id_) -> bool:
    name = ability['name']
    type_ = ability['type']
    casting = ability['casting']
    components = ability['components']
    requirements = ability['requirements']
    conditions = ability['conditions']
    effects = ability['effects']
    description = ability['description']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE abilities SET name=?, casting=?, components=?, requirements=?, conditions=?,'
                       'effects=?, description=? WHERE id=?',
                       (name, casting, components, requirements, conditions, effects, description, id_))

    return True


def get_abilities():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities ORDER BY name')

        entity = get_abilities_attributes(cursor)

    return entity


def get_abilities_by_id(ability_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities WHERE id=? ORDER BY name', (ability_id,))

        entity = get_abilities_attributes(cursor)

    return entity


def get_abilities_name_by_type(ability_type):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM abilities WHERE type=? ORDER BY name', (ability_type,))

        entity = get_list(cursor)

    return entity


def get_abilities_by_type(ability_type):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities WHERE type=? ORDER BY name', (ability_type,))

        entity = get_abilities_attributes(cursor)

    return entity


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


def get_abilities_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'casting': row[3],
        'components': row[4],
        'requirements': row[5],
        'conditions': row[6],
        'effects': row[7],
        'description': row[8]
    } for row in cursor.fetchall()]


def get_ability_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'casting': row[3],
        'components': row[4],
        'requirements': row[5],
        'conditions': row[6],
        'effects': row[7],
        'description': row[8]
    } for row in cursor.fetchall()][0]
