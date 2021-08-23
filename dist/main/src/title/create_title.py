from src.frames.scroll_frame import TemplateScrollFrame
from src.methods import popup_showinfo, get_text_data, handle_selection_change
from src.title.title import Title
from src.title.title_widget import TitleWidget


class CreateTitle(TemplateScrollFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home = kwargs['home']

        self.title_widget = TitleWidget(
            create_title=self.create_title,
            widgets=self.template_scroll.widgets,
            buttons=self.template_scroll.buttons,
            add_entity_frame=lambda: self.template_scroll.add_entity_frame(TitleWidget)
        )

        self.set_widgets_conf()
        self.set_buttons_conf()
        self.append_to_frames(self.title_widget)

    def create_title(self) -> None:
        create_title = None

        for title_frame in self.template_scroll.frames:
            character = handle_selection_change(title_frame.character_entry, title_frame.characters)
            npc = handle_selection_change(title_frame.npc_entry, title_frame.npcs)
            monster = handle_selection_change(title_frame.monster_entry, title_frame.monsters)

            users = character + npc + monster

            name = title_frame.name.get()
            requirements = get_text_data(title_frame.requirements_entry)
            description = get_text_data(title_frame.description_entry)

            title = Title(
                name=name,
                requirements=requirements,
                description=description,
                users=users
            )

            create_title = title.create_title()

        self.home() if create_title else popup_showinfo('Something went wrong, please, try again!')
