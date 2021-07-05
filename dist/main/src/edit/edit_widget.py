from src.edit.edit_ability import EditAbility
from src.edit.edit_avatar import EditAvatar
from src.edit.edit_item import EditItem
from src.edit.edit_proficiency import EditProficiency
from src.edit.edit_title import EditTitle


class EditWidget:
    def __init__(self, **kwargs):
        type_ = kwargs['type_']
        if type_ == 'Character' or type_ == 'NPC' or type_ == 'Monster':
            EditAvatar(**kwargs)
        elif type_ == 'Item' or type_ == 'Armor' or type_ == 'Weapon':
            EditItem(**kwargs)
        elif type_ == 'Ability':
            EditAbility(**kwargs)
        elif type_ == 'Title':
            EditTitle(**kwargs)
        elif type_ == 'Proficiency':
            EditProficiency(**kwargs)
