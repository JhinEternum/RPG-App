from src.connection.database import get_entity


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


def set_stored_items(listbox_widget, stored_entities, total_list):
    if type(stored_entities) != list or len(stored_entities) == 0:
        listbox_widget.select_set(0)
        return

    for entity in stored_entities:
        if entity in stored_entities:
            entity_name = entity['name']
            entity_index = total_list.index(entity_name)
            listbox_widget.select_set(entity_index)


def interface(name, type_, show_interface, search_name, search_type):
    new_entity = get_entity(name, type_)
    show_interface(new_entity, type_, search_name, search_type)
