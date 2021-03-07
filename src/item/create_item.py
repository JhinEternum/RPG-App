from src.frames.scroll_frame import TemplateScrollFrame
from src.item.item import Item
from src.item.item_widget import ItemWidget
from src.methods import handle_selection_change, choose_user, get_entity_ids, get_text_data, popup_showinfo


class CreateItem(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']

        self.item_widget = ItemWidget(
            create_item=self.create_item,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            add_entity_frame=lambda: self.template_scroll.add_entity_frame(ItemWidget)
        )
        self.set_widgets_conf()
        self.set_buttons_conf()
        self.append_to_frames(self.item_widget)

        print(self.template_scroll.frames)

    def create_item(self) -> None:
        type_dict = {'Armor': 1, 'Weapon': 2}

        for item_frame in self.template_scroll.frames:
            character = item_frame.character_menu.get()
            npc = item_frame.npc_menu.get()
            monster = item_frame.monster_menu.get()

            abilities = handle_selection_change(item_frame.abilities_entry, item_frame.abilities)
            abilities_result = get_entity_ids('ability', abilities)

            user = choose_user(character, npc, monster)

            name = item_frame.name.get()
            type_ = type_dict[item_frame.type_.get()]
            reduction = item_frame.reduction.get()
            damage = item_frame.damage.get()
            range_ = item_frame.range_.get()
            health = item_frame.health.get()
            area = item_frame.area.get()
            effects = get_text_data(item_frame.effects_entry)
            description = get_text_data(item_frame.description_entry)

            item = Item(
                name=name,
                type_=type_,
                reduction=reduction,
                damage=damage,
                range_=range_,
                health=health,
                area=area,
                abilities=abilities_result,
                effects=effects,
                description=description,
                user=user
            )

            create_item = item.create_item()

            print(f'create_item: {create_item}')
            print(f'type: {type(create_item)}')

            self.home() if create_item else popup_showinfo('Something went wrong, please, try again!')
