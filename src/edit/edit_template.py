from src.images.image import get_edit, get_back, get_save


class EditTemplate:
    def __init__(self, **kwargs):
        self.search_name = kwargs['name']
        self.search_type = kwargs['type_']

        self.entity = kwargs['entity']
        self.save = kwargs['save']
        self.back = kwargs['back']

        self.bind_label = kwargs['bind_label']
        self.show_interface = kwargs['show_interface']

        self.search_parent_name = kwargs['search_parent_name'] if 'search_parent_name' in kwargs else None
        self.parent_name = kwargs['parent_name'] if 'parent_name' in kwargs else None
        self.parent_type = kwargs['parent_type'] if 'parent_type' in kwargs else None
        self.go_parent = kwargs['go_parent'] if 'go_parent' in kwargs else False

        self.search_result = None

        self.edit_icon = get_edit()
        self.back_icon = get_back()
        self.save_icon = get_save()
