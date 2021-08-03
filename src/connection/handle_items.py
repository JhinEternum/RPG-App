from .database import DatabaseConnection
from ..item.item import Item


def add_item(item: Item, user_name) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO items (name, type, reduction, damage, range, health, area, effects, description) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (item.name, item.type, item.reduction, item.damage, item.range, item.health, item.area,
                        item.effects, item.description))

        item_id = cursor.lastrowid

        user_types = ['Character', 'NPC', 'Monster']
        if user_name != '' and user_name not in user_types:
            cursor.execute('INSERT INTO users_items (item_id, user_name) VALUES (?, ?)', (item_id, user_name))

    return True


def update_item(item: Item, id_) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE items SET name=?, type=?, reduction=?,'
                       'damage=?, range=?, health=?, area=?, effects=?, description=? WHERE id=?',
                       (item.name, item.type, item.reduction, item.damage, item.range, item.health, item.area,
                        item.effects, item.description, id_))

    return True


def get_items_attributes(cursor):
    return [Item(**{
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
    }) for row in cursor.fetchall()]


def get_items():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items')

        entity = get_items_attributes(cursor)

    return entity


def get_item_by_name(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items WHERE name=? ORDER BY name', (name,))

        entity = get_items_attributes(cursor)

    return entity


def get_item_by_type(_type: int):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM items WHERE type=? ORDER BY name', (_type,))

        entity = get_items_attributes(cursor)

    return entity
