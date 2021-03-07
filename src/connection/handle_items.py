from .database import *
from .database import DatabaseConnection
from src.connection.handle_abilities import get_abilities_by_id


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


def add_item(item, user_name) -> bool:
    name = item['name']
    type_ = item['type']
    reduction = item['reduction']
    damage = item['damage']
    range_ = item['range']
    health = item['health']
    area = item['area']
    effects = item['effects']
    description = item['description']

    abilities_id = item['abilities']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO items (name, type, reduction, damage, range, health, area, effects, description) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, type_, reduction, damage, range_, health, area, effects, description))

        item_id = cursor.lastrowid

        if len(abilities_id) > 0:
            for ability in abilities_id:
                cursor.execute('INSERT INTO items_abilities (ability_id, item_id) VALUES (?, ?)', (ability, item_id))

        user_types = ['Character', 'NPC', 'Monster']

        if user_name != '' and user_name not in user_types:
            cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item_id, user_name))

    return True


def update_item(item, id_) -> bool:
    name = item['name']
    type_ = item['type']
    reduction = item['reduction']
    damage = item['damage']
    range_ = item['range']
    health = item['health']
    area = item['area']
    effects = item['effects']
    description = item['description']

    abilities_id = item['abilities']

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE items SET name=?, type=?, reduction=?,'
                       'damage=?, range=?, health=?, area=?, effects=?, description=? WHERE id=?',
                       (name, type_, reduction, damage, range_, health, area, effects, description, id_))

        cursor.execute('DELETE FROM items_abilities WHERE item_id=?', (id_,))
        if len(abilities_id) > 0:
            for ability in abilities_id:
                cursor.execute('INSERT INTO items_abilities (ability_id, item_id) VALUES (?, ?)', (ability, id_))

    return True


def get_items_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'reduction': row[3],
        'damage': row[4],
        'range': row[5],
        'health': row[6],
        'area': row[7],
        'effects': row[8],
        'description': row[9]
    } for row in cursor.fetchall()]


def get_item_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'reduction': row[3],
        'damage': row[4],
        'range': row[5],
        'health': row[6],
        'area': row[7],
        'effects': row[8],
        'description': row[9]
    } for row in cursor.fetchall()][0]


def get_items():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items')

        entity = get_items_attributes(cursor)

    return entity


def get_specific_items(name, type_):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if name == '':
            cursor.execute('SELECT * FROM items WHERE type=? ORDER BY name', (type_,))
        else:
            cursor.execute('SELECT * FROM items WHERE name=? ORDER BY name', (name,))

        entity = get_items_attributes(cursor)

    return entity


def get_item_abilities(item_id):
    abilities = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT ability_id FROM items_abilities WHERE item_id=?', (item_id,))
        abilities_id = get_list(cursor)

        for ability in abilities_id:
            abilities += get_abilities_by_id(ability)

    return abilities
