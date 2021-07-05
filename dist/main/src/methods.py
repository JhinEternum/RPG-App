from tkinter.messagebox import showinfo

from src.connection.handle_abilities import get_abilities


def popup_showinfo(message):
    showinfo("ShowInfo", message)


def get_entity_ids(entity_type, entities_names):
    result = []
    entities = select_entity(entity_type)

    for entity in entities_names:
        for stored_entities in entities:
            if entity == stored_entities['name']:
                entity_id = stored_entities['id']
                result.append(entity_id)

    return result


def select_entity(entity):
    if entity == 'ability':
        return get_abilities()
    else:
        return None


def choose_user(character, npc, monster):
    if character != 'None':
        user = character
    elif npc != 'None':
        user = npc
    elif monster != 'None':
        user = monster
    else:
        user = 'Character'

    return user


def choose_user_ability(character, npc, monster, item):
    user = []

    if character != 'None':
        value = (character, 1)
        user.extend(value)
    elif npc != 'None':
        value = (npc, 2)
        user.extend(value)
    elif monster != 'None':
        value = (monster, 3)
        user.extend(value)
    elif item != 'None':
        value = (item, 4)
        user.extend(value)
    else:
        value = ('Character', 1)
        user.extend(value)

    return user


def handle_selection_change(list_widget, total_list):
    selected_indices = list_widget.curselection()
    result_list = []

    if len(selected_indices) == 0 or (len(selected_indices) == 1 and total_list[selected_indices[0]] == 'None'):
        return []

    for i in selected_indices:
        result_list.append(total_list[i])

    return result_list


def get_text_data(text_widget):
    return text_widget.get("1.0", 'end-1c')