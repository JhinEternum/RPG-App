# --- User ---
from src.connection.database import get_entity


def generate_items(items, item_types):
    text = '\n\t'
    item_result = []

    if len(items) == 0:
        return 'Items:  None'

    for item in items:
        item_type = item_types[item['type']]
        item_name = item['name']

        item_string = f'{item_type}  -  {item_name}'

        item_result.append(item_string)

    text = f'Items:\n\t{text.join(item_result)}'

    return text


def generate_classes(classes):
    text = ', '
    class_result = []

    if len(classes) == 0:
        return 'Class:  None'

    for class_ in classes:
        class_result.append(class_['name'])

    text = f'Classes:  {text.join(class_result)}'

    return text


def generate_titles(titles):
    text = '\n\t'
    titles_result = []

    if len(titles) == 0:
        return 'Titles:  None'

    for title in titles:
        titles_result.append(title['name'])

    text = f'Titles:\n\t{text.join(titles_result)}'

    return text


def generate_proficiencies(proficiencies):
    text = ''
    proficiencies_result = []

    if len(proficiencies) == 0:
        return 'Proficiencies:  None'

    for proficiency in proficiencies:
        proficiencies_result.append('\t' + proficiency['name'] + ' ' + proficiency['level'] + '\n')

    text = f'Proficiencies\n{text.join(proficiencies_result)}'

    return text

# ----------------------


def generate_abilities(abilities):
    text = '\n\t'
    ability_result = []

    if len(abilities) == 0:
        return 'Abilities:  None'

    for ability in abilities:
        ability_name = ability['name']
        ability_result.append(ability_name)

    text = f'Abilities:\n\t{text.join(ability_result)}'

    return text


def button_state(entity_list):
    if len(entity_list) == 0:
        return 'disabled'

    return 'normal'


def interface(name, type_, show_interface, search_name, search_type):
    new_entity = get_entity(name, type_)
    show_interface(new_entity, type_, search_name, search_type)
