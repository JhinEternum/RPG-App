from .database import DatabaseConnection
from src.connection import handle_classes
from src.connection import handle_abilities
from src.connection import handle_titles
from src.connection import handle_proficiencies
from src.connection import handle_items
from ..avatar.avatar import Avatar


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
                cursor.execute('INSERT INTO users_abilities (ability_id, user_name) VALUES(?, ?)',
                               (ability, avatar.name))

        if len(avatar.proficiencies) > 0:
            for proficiency in avatar.proficiencies:
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
        if len(avatar.proficiencies) > 0:
            for proficiency in avatar.proficiencies:
                cursor.execute('INSERT INTO users_proficiencies (proficiency_id, level, rank, user_name) '
                               'VALUES (?, ?, ?, ?)',
                               (proficiency[0], proficiency[1], proficiency[2], avatar.name))

    return True


def get_user(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        print(user_name)

        cursor.execute('SELECT * FROM users WHERE name=?', (user_name,))
        user = get_user_attributes(cursor)

        user.classes = get_user_classes(user_name)
        user.items = get_user_items(user_name)
        user.titles = get_user_titles(user_name)
        user.abilities = get_user_abilities(user_name)
        user.proficiencies = get_user_proficiencies(user_name)

    return user


def get_users(db_type: int):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE type=? ORDER BY name', (db_type,))
        users = get_users_attributes(cursor)

        for user in users:
            user.classes = get_user_classes(user.name)
            user.items = get_user_items(user.name)
            user.titles = get_user_titles(user.name)
            user.abilities = get_user_abilities(user.name)
            user.proficiencies = get_user_proficiencies(user.name)

    return users


def get_search_user(user_name: str, _type: int):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users WHERE name LIKE ? AND type=? ORDER BY name',
                       ('%' + user_name + '%', _type))

        users = get_users_attributes(cursor)

        for user in users:
            user.classes = get_user_classes(user.name)
            user.items = get_user_items(user.name)
            user.titles = get_user_titles(user.name)
            user.abilities = get_user_abilities(user.name)
            user.proficiencies = get_user_proficiencies(user.name)

    return users


def get_users_attributes(cursor):
    return [Avatar(**{
        'name': row[0],
        'type': row[1],
        'strength_lv': row[2],
        'magic_lv': row[3],
        'health': row[4],
        'adrenaline': row[5],
        'physical_ability': row[6],
        'description': row[7]
    }) for row in cursor.fetchall()]


def get_user_attributes(cursor):
    return [Avatar(**{
        'name': row[0],
        'type': row[1],
        'strength_lv': row[2],
        'magic_lv': row[3],
        'health': row[4],
        'adrenaline': row[5],
        'physical_ability': row[6],
        'description': row[7]
    }) for row in cursor.fetchall()][0]


def get_user_classes(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM classes WHERE id IN (SELECT class_id FROM users_classes WHERE user_name=?) '
                       'ORDER BY name',
                       (user_name,))
        classes = handle_classes.get_classes_attributes(cursor)

    return classes


def get_user_items(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items WHERE id IN (SELECT item_id FROM users_items WHERE user_name=?) '
                       'ORDER BY type, name',
                       (user_name,))
        items = handle_items.get_items_attributes(cursor)

    return items


def get_user_types():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users_types')

        entity = get_user_types_attributes(cursor)

    return entity


def get_user_type_by_name(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT id FROM users_types WHERE name=?', (name,))

        entity = cursor.fetchone()

    return entity[0]


def get_user_types_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1]
    } for row in cursor.fetchall()]


def get_user_abilities(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM abilities WHERE id IN (SELECT ability_id FROM users_abilities WHERE user_name=?)'
                       f' ORDER BY name', (user_name,))
        abilities = handle_abilities.get_abilities_attributes(cursor)

    return abilities


def get_user_proficiencies(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT proficiency_id, level, rank FROM users_proficiencies WHERE user_name=?', (user_name,))
        proficiencies_id = get_user_proficiencies_attributes(cursor)

        cursor.execute(f'SELECT * FROM proficiencies WHERE id IN '
                       f'(SELECT proficiency_id FROM users_proficiencies WHERE user_name=?) ORDER BY name',
                       (user_name,))
        proficiencies = handle_proficiencies.get_proficiencies_attributes(cursor)

        for proficiency in proficiencies:
            for proficiency_level in proficiencies_id:
                if proficiency.id == proficiency_level['proficiency_id']:
                    proficiency.level = proficiency_level['level']
                    proficiency.rank = proficiency_level['rank']
                    break

    return proficiencies


def get_user_proficiencies_attributes(cursor):
    return [{
        'proficiency_id': row[0],
        'level': row[1],
        'rank': row[2]
    } for row in cursor.fetchall()]


def get_user_titles(user_name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM titles WHERE id IN (SELECT title_id FROM users_titles WHERE user_name=?) '
                       'ORDER BY name',
                       (user_name,))
        titles = handle_titles.get_titles_attributes(cursor)

    return titles
