def get_entities_ids(entities: list, entities_names: list) -> list:
    result = []

    for entity_name in entities_names:
        for entity in entities:
            if entity_name == entity['name']:
                entity_id = entity['id']
                result.append(entity_id)

    return result


def get_entity_ids(entities: list, entities_names: list) -> list:
    result = []

    for entity_name in entities_names:
        for entity in entities:
            if entity_name == entity.name:
                entity_id = entity.id
                result.append(entity_id)

    return result
