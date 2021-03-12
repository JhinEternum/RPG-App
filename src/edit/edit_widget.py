from src.edit.edit_avatar import EditAvatar


class EditWidget:
    def __init__(self, **kwargs):
        type_ = kwargs['type_']
        if type_ == 'Character' or type_ == 'NPC' or type_ == 'Monster':
            EditAvatar(**kwargs)
