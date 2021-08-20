from .database_connection import DatabaseConnection

from src.connection import handle_proficiencies
from src.connection import handle_titles
from src.connection import handle_items
from src.connection import handle_abilities
from src.connection import handle_users


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
            entity = handle_users.get_user(name)
        elif db_entity == 'items':
            entity = handle_items.get_items_attributes(cursor)[0]
        elif db_entity == 'abilities':
            entity = handle_abilities.get_abilities_attributes(cursor)[0]
        elif db_entity == 'titles':
            entity = handle_titles.get_titles_attributes(cursor)[0]
        elif db_entity == 'proficiencies':
            entity = handle_proficiencies.get_proficiencies_attributes(cursor)[0]

    return entity


def get_search_entities(name: str, type_):
    entity_name = name.lower()
    db_entity = search_database[type_]
    db_type = search_types[type_]

    entity = []

    if entity_name == '' or entity_name == '*':
        if db_entity == 'users':
            entity = handle_users.get_users(db_type)
        elif db_entity == 'items':
            entity = handle_items.get_items()
        elif db_entity == 'abilities':
            entity.append(handle_abilities.get_abilities_by_type(1))  # character
            entity.append(handle_abilities.get_abilities_by_type(2))  # npc
            entity.append(handle_abilities.get_abilities_by_type(3))  # monster
        elif db_entity == 'titles':
            entity = handle_titles.get_titles()
        elif db_entity == 'proficiencies':
            entity = handle_proficiencies.get_proficiencies()
    else:
        if db_entity == 'users':
            entity = handle_users.get_search_user(entity_name, db_type)
        elif db_entity == 'items':
            entity = handle_items.get_search_item(entity_name, db_type)
        elif db_entity == 'abilities':
            entity.append(handle_abilities.get_search_ability(entity_name))
        elif db_entity == 'titles':
            entity = handle_titles.get_search_title(entity_name)
        elif db_entity == 'proficiencies':
            entity = handle_proficiencies.get_search_proficiency(entity_name)

    return entity
