import os
from tkinter import PhotoImage


image_directory = os.path.dirname(os.path.abspath("main.py")) + '/src/images/'

ui_directory = image_directory + '/ui/'
characters_directory = image_directory + '/characters/'
proficiencies_directory = image_directory + '/proficiencies/'
items_directory = image_directory + '/items/'
battle_directory = image_directory + '/battle/'


# UI
def get_home():
    return PhotoImage(file=f'{ui_directory}home.png')


def get_hp():
    return PhotoImage(file=f'{ui_directory}hp.png')


def get_strength():
    return PhotoImage(file=f'{ui_directory}strength.png')


def get_magic():
    return PhotoImage(file=f'{ui_directory}magic.png')


def get_adrenaline():
    return PhotoImage(file=f'{ui_directory}adrenaline.png')


def get_physical():
    return PhotoImage(file=f'{ui_directory}physical.png')


def get_battle():
    return PhotoImage(file=f'{ui_directory}battle.png')


def get_ability():
    return PhotoImage(file=f'{ui_directory}ability.png')


def get_title():
    return PhotoImage(file=f'{ui_directory}title.png')


def get_search():
    return PhotoImage(file=f'{ui_directory}search.png')


def get_wiki():
    return PhotoImage(file=f'{ui_directory}wiki.png')


def get_edit():
    return PhotoImage(file=f'{ui_directory}edit.png')


def get_back():
    return PhotoImage(file=f'{ui_directory}back.png')


def get_save():
    return PhotoImage(file=f'{ui_directory}save.png')


def get_item():
    return PhotoImage(file=f'{ui_directory}item.png')


def get_proficiency():
    return PhotoImage(file=f'{ui_directory}proficiency.png')
# UI


# Items
def get_axe():
    return PhotoImage(file=f'{items_directory}axe.png')


def get_bow():
    return PhotoImage(file=f'{items_directory}bow.png')


def get_sword():
    return PhotoImage(file=f'{items_directory}sword.png')


def get_armors():
    return PhotoImage(file=f'{items_directory}armors.png')


def get_weapons():
    return PhotoImage(file=f'{items_directory}weapons.png')
# Items


# Characters
def get_avatar():
    return PhotoImage(file=f'{characters_directory}avatar.png')


def get_monster():
    return PhotoImage(file=f'{characters_directory}monster1.png')


def get_npc():
    return PhotoImage(file=f'{characters_directory}npc.png')
# Characters


# Proficiencies
def get_proficiencies(icon: str):
    return PhotoImage(file=f'{proficiencies_directory}{icon}.png')


# Battle
def get_attack():
    return PhotoImage(file=f'{battle_directory}attack.png')


def get_reset():
    return PhotoImage(file=f'{battle_directory}reset.png')
