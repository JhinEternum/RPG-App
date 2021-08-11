import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from src.ability.create_ability import CreateAbility
from src.avatar.create_avatar import CreateAvatar
from src.battle.battle import Battle
from src.edit.edit import Edit
from src.home.home import Home
from src.interface.interface import Interface
from src.item.create_item import CreateItem
from src.proficiency.create_proficiency import CreateProficiency
from src.proficiency.proficiency_level import ProficiencyLevel
from src.search.search import Search
from src.title.create_title import CreateTitle
from src.wiki.wiki import Wiki
from src.wiki.wiki_factory import WikiFactory


def check_frame_existence(frame) -> None:
    if frame is not None and frame.winfo_exists():
        frame.destroy()


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('RPG')

        self.resizable(False, False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frames = dict()

        self.home = None
        self.create_avatar = None
        self.create_item = None
        self.create_ability = None
        self.create_title = None
        self.create_proficiency = None

        self.search = None
        self.interface = None
        self.edit = None

        self.wiki = None

        self.battle = None

        self.frames = {
            Home: self.home,
            CreateAvatar: self.create_avatar,
            CreateItem: self.create_item,
            CreateAbility: self.create_ability,
            CreateTitle: self.create_title,
            CreateProficiency: self.create_proficiency,
            Search: self.search,
            Interface: self.interface,
            Edit: self.edit,
            WikiFactory: self.wiki,
            Battle: self.battle
        }

        self.home = Home(
            parent=self,
            create_entity=self.create_entity_frame,
            proficiencies_level=self.show_proficiencies_level,
            show_search=self.show_search,
            show_wiki=self.show_wiki,
            set_battle=self.set_battle
        )
        self.home.grid(row=0, column=0, sticky='NSEW')

        self.frames[Home] = self.home

        self.show_frame(Home)

    def show_frame(self, container_class) -> None:
        frame = self.frames[container_class]
        frame.tkraise()

    def create_entity_frame(self, **kwargs) -> None:
        container = kwargs['container']
        container_class = kwargs['container_class']
        extra_frame = kwargs['extra_frame'] if 'extra_frame' in kwargs else None

        check_frame_existence(container)

        container = container_class(parent=self, home=lambda: self.show_frame(Home), extra_frame=extra_frame)
        container.grid(row=0, column=0, sticky='NSEW')

        frame = self.set_frames_to_attributes(container_class, container)

        self.frames[container_class] = frame
        self.show_frame(container_class)

    def set_frames_to_attributes(self, container_class, container):
        if container_class == CreateAvatar:
            self.create_avatar = container
            return self.create_avatar
        elif container_class == CreateItem:
            self.create_item = container
            return self.create_item
        elif container_class == CreateAbility:
            self.create_ability = container
            return self.create_ability
        elif container_class == CreateTitle:
            self.create_title = container
            return self.create_title
        elif container_class == CreateProficiency:
            self.create_proficiency = container
            return self.create_proficiency

    def show_proficiencies_level(self, **kwargs) -> None:
        ProficiencyLevel(parent=self, **kwargs)

    def show_search(self, **kwargs) -> None:
        check_frame_existence(self.search)

        self.search = Search(
            parent=self,
            home=lambda: self.show_frame(Home),
            show_interface=self.show_interface,
            **kwargs
        )
        self.search.grid(row=0, column=0, sticky='NSEW')

        self.frames[Search] = self.search
        self.show_frame(Search)

    def show_interface(self, **kwargs) -> None:
        check_frame_existence(self.interface)

        self.interface = Interface(
            parent=self,
            home=lambda: self.show_frame(Home),
            show_search=self.show_search,
            show_interface=self.show_interface,
            edit=self.show_edit,
            scroll=True,
            single_widgets=True,
            **kwargs
        )
        self.interface.grid(row=0, column=0, sticky='NSEW')

        self.frames[Interface] = self.interface
        self.show_frame(Interface)

    def show_edit(self, **kwargs) -> None:
        check_frame_existence(self.edit)

        self.edit = Edit(
            parent=self,
            home=lambda: self.show_frame(Home),
            show_interface=self.show_interface,
            show_proficiencies_level=self.show_proficiencies_level,
            **kwargs
        )
        self.edit.grid(row=0, column=0, sticky='NSEW')

        self.frames[Edit] = self.edit
        self.show_frame(Edit)

    def show_wiki(self, **kwargs) -> None:
        check_frame_existence(self.wiki)

        self.wiki = WikiFactory(
            parent=self,
            home=lambda: self.show_frame(Home),
            wiki=Wiki(),
            show_wiki=self.show_wiki,
            scroll=True,
            single_widgets=kwargs['widgets_type'] if 'widgets_type' in kwargs else True,
            **kwargs
        )
        self.wiki.grid(row=0, column=0, sticky='NSEW')

        self.frames[WikiFactory] = self.wiki
        self.show_frame(WikiFactory)

    def set_battle(self):
        check_frame_existence(self.battle)

        print('set_battle')

        battle = {
            'parent': self,
            'home': lambda: self.show_frame(Home),
            'scroll': True,
            'single_widgets': False
        }

        self.battle = Battle(**battle)
        self.battle.grid(row=0, column=0, sticky='NSEW')

        self.frames[Battle] = self.battle
        self.show_frame(Battle)


root = Game()

style = ttk.Style(root)

font.nametofont('TkDefaultFont').configure(size=12)

root.mainloop()
