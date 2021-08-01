from .attributes import get_items_attributes
from .database import DatabaseConnection
from src.connection.handle_abilities import get_abilities_by_id
from src.connection.handle_titles import get_titles_by_id
from src.connection.handle_proficiencies import get_proficiencies_by_id
from .handle_classes import get_classes_attributes
from ..title.title import Title


def get_list(cursor) -> list:
    return [row[0] for row in cursor.fetchall()]


# --- USERS ---
def add_user(avatar) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (avatar.name, avatar.type, avatar.strength_lv, avatar.magic_lv, avatar.health, avatar.adrenaline,
                        avatar.physical_ability, avatar.description))

        if len(avatar.classes) > 0:
            for class_ in avatar.classes:
                cursor.execute('INSERT INTO users_classes (class_id, user_name) VALUES (?, ?)', (class_, avatar.name))

        if len(avatar.items) > 0:
            for item in avatar.items:
                cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item, avatar.name))

        if len(avatar.titles) > 0:
            for title in avatar.titles:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title, avatar.name))

        if len(avatar.abilities) > 0:
            for ability in avatar.abilities:
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)', (ability, avatar.name))

        if len(avatar.proficiency) > 0:
            for proficiency in avatar.proficiency:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, level, rank, user_name) '
                               'VALUES (?, ?, ?, ?)',
                               (proficiency[0], proficiency[1], proficiency[2], avatar.name))

    return True


def update_user(avatar, current_name: str) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE users SET name=?, type=?, strength_lv=?, magic_lv=?, health=?, adrenaline=?, '
                       'physical_ability=?, description=? WHERE name=?',
                       (avatar.name, avatar.type, avatar.strength_lv, avatar.magic_lv, avatar.health, avatar.adrenaline,
                        avatar.physical_ability, avatar.description, current_name))

        cursor.execute('DELETE FROM users_classes WHERE user_name=?', (current_name,))
        if len(avatar.classes) > 0:
            for class_ in avatar.classes:
                cursor.execute('INSERT INTO users_classes (class_id, user_name) VALUES (?, ?)', (class_, avatar.name))

        cursor.execute('DELETE FROM users_items WHERE user_name=?', (current_name,))
        if len(avatar.items) > 0:
            for item in avatar.items:
                cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item, avatar.name))

        cursor.execute('DELETE FROM users_titles WHERE user_name=?', (current_name,))
        if len(avatar.titles) > 0:
            for title in avatar.titles:
                cursor.execute('INSERT INTO users_titles (title_id, user_name) VALUES (?, ?)', (title, avatar.name))

        cursor.execute('DELETE FROM users_abilities WHERE user_name=?', (current_name,))
        if len(avatar.abilities) > 0:
            for ability in avatar.abilities:
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)',
                               (ability, avatar.name))

        cursor.execute('DELETE FROM users_proficiencies WHERE user_name=?', (current_name,))
        if len(avatar.proficiency) > 0:
            for proficiency in avatar.proficiency:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, level, rank, user_name) '
                               'VALUES (?, ?, ?, ?)',
                               (proficiency[0], proficiency[1], proficiency[2], avatar.name))

    return True


def get_users_name(name: str, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT name FROM users WHERE type=?', (type_,))
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


def get_user_classes(user_name: str):
    classes = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT class_id FROM users_classes WHERE user_name=?', (user_name,))
        classes_id = get_list(cursor)

        for class_id in classes_id:
            cursor.execute('SELECT * FROM classes WHERE id=?', (class_id,))
            classes += get_classes_attributes(cursor)

    return classes


def get_user_items(user_name: str):
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


def get_user_abilities(user_name: str):
    abilities = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT ability_id FROM users_abilities WHERE user_name=?', (user_name,))
        abilities_id = get_list(cursor)

        for ability in abilities_id:
            abilities += get_abilities_by_id(ability)

    return abilities


def get_user_proficiencies(user_name: str):
    proficiencies = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT proficiency_id, level, rank FROM users_proficiencies WHERE user_name=?', (user_name,))
        proficiencies_id = get_user_proficiencies_attributes(cursor)

        for proficiency in proficiencies_id:
            proficiencies += get_proficiencies_by_id(proficiency['proficiency_id'])

        for proficiency in proficiencies:
            for proficiency_level in proficiencies_id:
                if proficiency['id'] == proficiency_level['proficiency_id']:
                    proficiency['level'] = proficiency_level['level']
                    proficiency['rank'] = proficiency_level['rank']
                    break

    return proficiencies


def get_user_proficiencies_attributes(cursor):
    return [{
        'proficiency_id': row[0],
        'level': row[1],
        'rank': row[2]
    } for row in cursor.fetchall()]


def get_user_titles(user_name):
    titles = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT title_id FROM users_titles WHERE user_name=?', (user_name,))
        titles_id = get_list(cursor)

        # for title in titles_id:
        #     current_title = get_titles_by_id(title)
        #     titles.append(Title(**current_title[0]))

        for title in titles_id:
            titles += get_titles_by_id(title)

    return titles
