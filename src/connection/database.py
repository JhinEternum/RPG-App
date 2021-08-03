from .database_connection import DatabaseConnection

from src.connection import handle_proficiencies
from src.connection import handle_titles
from src.connection import handle_items
from src.connection import handle_abilities
from src.connection import handle_users


def get_list(cursor):
    return [row[0] for row in cursor.fetchall()]


search_database = {
    # users
    'Character': 'users',
    'NPC': 'users',
    'Monster': 'users',
    'users': 'users',
    # items
    'Item': 'items',
    'Armor': 'items',
    'Weapon': 'items',
    'items': 'items',
    # others
    'Proficiency': 'proficiencies',
    'proficiencies': 'proficiencies',
    'Title': 'titles',
    'titles': 'titles',
    'Ability': 'abilities',
    'abilities': 'abilities',
    'Wiki': 'wiki',
    'wiki': 'wiki'
}

search_types = {
    'Character': 1,
    'NPC': 2,
    'Monster': 3,
    'Armor': 1,
    'Weapon': 2,
    'Proficiency': None,
    'Title': None,
    'Ability': None,
    'Wiki': None
}


def get_entity(name: str, type_):
    db_entity = search_database[type_]

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM {db_entity} WHERE name=?', (name,))
        if db_entity == 'users':
            entity = handle_users.get_user_attributes(cursor)
        elif db_entity == 'items':
            entity = handle_items.get_items_attributes(cursor)[0]
        elif db_entity == 'abilities':
            entity = handle_abilities.get_abilities_attributes(cursor)[0]
        elif db_entity == 'titles':
            entity = handle_titles.get_titles_attributes(cursor)[0]
        elif db_entity == 'proficiencies':
            entity = handle_proficiencies.get_proficiencies_attributes(cursor)[0]

    return entity


def get_entity_name_by_id(id_: int, db_entity: str):
    if id_ == 0:
        return 'None'

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT name FROM {db_entity} WHERE id=?', (id_,))
        entity = get_list(cursor)

    return entity


# --- OTHERS ---
def get_search_entities(name, type_):
    entity_name = name.lower()
    db_entity = search_database[type_]
    db_type = search_types[type_]

    entity = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if entity_name == '' or entity_name == '*':
            if db_entity == 'users' or db_entity == 'items':
                cursor.execute(f'SELECT name FROM {db_entity} WHERE type=? ORDER BY name', (db_type,))
                entity = get_list(cursor)
            elif db_entity == 'abilities':
                characters_abilities = handle_abilities.get_abilities_name_by_type(1)
                npcs_abilities = handle_abilities.get_abilities_name_by_type(2)
                monsters_abilities = handle_abilities.get_abilities_name_by_type(3)
                # items_abilities = handle_abilities.get_abilities_name_by_type(4)

                entity.append(characters_abilities)
                entity.append(npcs_abilities)
                entity.append(monsters_abilities)
                # entity.append(items_abilities)
            else:
                cursor.execute(f'SELECT name FROM {db_entity}')
                entity = get_list(cursor)
        else:
            if db_entity == 'users' or db_entity == 'items':
                cursor.execute(f'SELECT name FROM {db_entity} WHERE name LIKE ? AND type=? ORDER BY name',
                               ('%' + entity_name + '%', db_type))
                entity = get_list(cursor)
            else:
                cursor.execute(f'SELECT name FROM {db_entity} WHERE name LIKE ? ORDER BY name',
                               ('%' + entity_name + '%',))
                entity = get_list(cursor)

    return entity
