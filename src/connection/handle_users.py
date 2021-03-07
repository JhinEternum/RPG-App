from .database import *
from .database import DatabaseConnection
from src.connection.handle_abilities import get_abilities_by_id
from src.connection.handle_titles import get_titles_by_id
from src.connection.handle_proficiencies import get_proficiencies_by_id
from .handle_classes import get_classes_attributes


def get_list(cursor) -> list:
    return [row[0] for row in cursor.fetchall()]


# --- USERS ---
def add_user(user) -> bool:
    name = user['name']
    type_ = user['type']
    strength_lv = user['strength_lv']
    magic_lv = user['magic_lv']
    health = user['health']
    adrenaline = user['adrenaline']
    physical_ability = user['physical_ability']
    description = user['description']

    classes_id = user['class']
    items_id = user['items']
    titles_id = user['titles']
    abilities_id = user['abilities']
    proficiencies_id = user['proficiency']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, type_, strength_lv, magic_lv, health, adrenaline, physical_ability, description))

        if len(classes_id) > 0:
            for class_ in classes_id:
                cursor.execute('INSERT INTO users_classes (class_id, user_name) VALUES (?, ?)', (class_, name))

        if len(items_id) > 0:
            for item in items_id:
                cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item, name))

        if len(titles_id) > 0:
            for title in titles_id:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title, name))

        if len(abilities_id) > 0:
            for ability in abilities_id:
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)', (ability, name))

        if len(proficiencies_id) > 0:
            for proficiency in proficiencies_id:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, level, user_name) VALUES (?, ?, ?)',
                               (proficiency[0], proficiency[1], name))

    return True


def update_user(user, current_name) -> bool:
    name = user['name']
    type_ = user['type']
    strength_lv = user['strength_lv']
    magic_lv = user['magic_lv']
    health = user['health']
    adrenaline = user['adrenaline']
    physical_ability = user['physical_ability']
    description = user['description']

    classes_id = user['class']
    items_id = user['items']
    titles_id = user['titles']
    abilities_id = user['abilities']
    proficiencies_id = user['proficiency']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE users SET name=?, type=?, strength_lv=?, magic_lv=?, health=?, adrenaline=?, '
                       'physical_ability=?, description=? WHERE name=?',
                       (name, type_, strength_lv, magic_lv, health, adrenaline, physical_ability, description,
                        current_name))

        cursor.execute('DELETE FROM users_classes WHERE user_name=?', (current_name,))
        if len(classes_id) > 0:
            for class_ in classes_id:
                cursor.execute('INSERT INTO users_classes (class_id, user_name) VALUES (?, ?)', (class_, name))

        cursor.execute('DELETE FROM users_items WHERE user_name=?', (current_name,))
        if len(items_id) > 0:
            for item in items_id:
                cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item, name))

        cursor.execute('DELETE FROM users_titles WHERE user_name=?', (current_name,))
        if len(titles_id) > 0:
            for title in titles_id:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title, name))

        cursor.execute('DELETE FROM users_abilities WHERE user_name=?', (current_name,))
        if len(abilities_id) > 0:
            for ability in abilities_id:
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)', (ability, name))

        cursor.execute('DELETE FROM users_proficiencies WHERE user_name=?', (current_name,))
        if len(proficiencies_id) > 0:
            for proficiency in proficiencies_id:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, level, user_name) VALUES (?, ?, ?)',
                               (proficiency[0], proficiency[1], name))

    return True


def get_users_name(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT name FROM users WHERE type=?', (type_,))
            result = get_list(cursor)
        else:
            cursor.execute('SELECT name FROM users WHERE name=? AND type=?', (name, type_))
            result = get_list(cursor)

    return result


def get_user(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE name=?', (name,))
        characters = get_user_attributes(cursor)

    return characters


def get_user_attributes(cursor):
    return [{
        'name': row[0],
        'type': row[1],
        'strength_lv': row[2],
        'magic_lv': row[3],
        'health': row[4],
        'adrenaline': row[5],
        'physical_ability': row[6],
        'description': row[7]
    } for row in cursor.fetchall()][0]


def get_user_classes(user_name):
    classes = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT class_id FROM users_classes WHERE user_name=?', (user_name,))
        classes_id = get_list(cursor)

        for class_id in classes_id:
            cursor.execute('SELECT * FROM classes WHERE id=?', (class_id,))
            classes += get_classes_attributes(cursor)

    return classes


def get_user_items(user_name):
    items = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT item_id FROM users_items WHERE user_name=?', (user_name,))
        items_id = get_list(cursor)

        for item in items_id:
            cursor.execute('SELECT * FROM items WHERE id=?', (item,))
            items += get_items_attributes(cursor)

    return items


def get_user_types():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users_types')

        entity = get_user_types_attributes(cursor)

    return entity


def get_user_types_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


def get_user_abilities(user_name):
    abilities = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT ability_id FROM users_abilities WHERE user_name=?', (user_name,))
        abilities_id = get_list(cursor)

        for ability in abilities_id:
            abilities += get_abilities_by_id(ability)

    return abilities


def get_user_proficiencies(user_name):
    proficiencies = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT proficiency_id, level FROM users_proficiencies WHERE user_name=?', (user_name,))
        proficiencies_id = get_user_proficiencies_attributes(cursor)

        for proficiency in proficiencies_id:
            proficiencies += get_proficiencies_by_id(proficiency['proficiency_id'])

        for proficiency in proficiencies:
            for proficiency_level in proficiencies_id:
                if proficiency['id'] == proficiency_level['proficiency_id']:
                    proficiency['level'] = proficiency_level['level']
                    break

    return proficiencies


def get_user_proficiencies_attributes(cursor):
    return [{
        'proficiency_id': row[0],
        'level': row[1]
    } for row in cursor.fetchall()]


def get_user_titles(user_name):
    titles = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT title_id FROM users_titles WHERE user_name=?', (user_name,))
        titles_id = get_list(cursor)

        for title in titles_id:
            titles += get_titles_by_id(title)

    return titles
