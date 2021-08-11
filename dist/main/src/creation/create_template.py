from src.connection.database import get_search_entities
from src.connection.handle_items import get_items


class CreateTemplate:
    def __init__(self, **kwargs):
        self.frame_id = kwargs['frame_id'] if 'frame_id' in kwargs else ''
        self.add_entity_frame = kwargs['add_entity_frame'] if 'add_entity_frame' in kwargs else None

        self.types_ = ('None', 'Character', 'NPC', 'Monster')

        self.characters = ['None', 'Character'] + get_search_entities('', 'Character')
        self.npcs = ['None', 'NPC'] + get_search_entities('', 'NPC')
        self.monsters = ['None', 'Monster'] + get_search_entities('', 'Monster')
        self.items = ['None', 'Item'] + [item.name for item in get_items()]
