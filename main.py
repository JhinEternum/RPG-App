import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from typing import Union

from src.ability.create_ability import CreateAbility
from src.avatar.create_avatar import CreateAvatar
from src.home.home import Home
from src.item.create_item import CreateItem
from src.proficiency.create_proficiency import CreateProficiency
from src.proficiency.proficiency_level import ProficiencyLevel
from src.title.create_title import CreateTitle


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

        self.frames = {
            Home: self.home,
            CreateAvatar: self.create_avatar,
            CreateItem: self.create_item,
            CreateAbility: self.create_ability,
            CreateTitle: self.create_title,
            CreateProficiency: self.create_proficiency
        }

        self.home = Home(
            parent=self,
            create_entity=self.create_entity_frame,
            proficiencies_level=self.show_proficiencies_level,
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


root = Game()

style = ttk.Style(root)

font.nametofont('TkDefaultFont').configure(size=12)

root.mainloop()
