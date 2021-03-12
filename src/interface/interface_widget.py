from src.interface.ability_interface import AbilityInterface
from src.interface.avatar_interface import AvatarInterface
from src.interface.item_interface import ItemInterface
from src.interface.proficiency_interface import ProficiencyInterface
from src.interface.title_interface import TitleInterface


class InterfaceWidget:
    def __init__(self, **kwargs):
        print(kwargs['type_'])

        type_ = kwargs['type_']
        if type_ == 'Character' or type_ == 'NPC' or type_ == 'Monster':
            AvatarInterface(**kwargs)
        elif type_ == 'Item' or type_ == 'Armor' or type_ == 'Weapon':
            ItemInterface(**kwargs)
        elif type_ == 'Ability':
            AbilityInterface(**kwargs)
        elif type_ == 'Title':
            TitleInterface(**kwargs)
        elif type_ == 'Proficiency':
            ProficiencyInterface(**kwargs)

