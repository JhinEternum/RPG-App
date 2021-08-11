from tkinter import Toplevel
import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar


class BattleSystem(Toplevel):
    def __init__(self, **kwargs):
        master = kwargs['master']
        super().__init__(kwargs['master'])

        master.eval(f'tk::PlaceWindow {str(self)} center')

        # self.resizable(False, False)
        self.columnconfigure(1, weight=1)
        self.title('Battle System')
        self.focus()

        self.entity: Avatar = kwargs['entity']

        self.hp = self.entity.health
        self.adrenaline = self.entity.adrenaline
        self.reduction = tk.StringVar()

        self.current_hp = int(self.generate_total_health())
        self.current_adr = int(self.adrenaline)
        self.damage = tk.StringVar()
        self.health_entry = ttk.Label()
        self.adrenaline_reduction = ttk.Entry()
        self.damage_entry = ttk.Entry()
        self.reduction_entry = ttk.Entry()
        self.adrenaline_entry = ttk.Label()

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky='NSEW')
        self.frame.columnconfigure(0, weight=1)

        self.set_avatar()

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')

    def set_avatar(self):
        name = ttk.Label(
            self.frame,
            text=self.entity.name
        )
        name.grid(row=0, column=0, sticky='EW')

        damage = ttk.Label(
            self.frame,
            text='Damage'
        )
        damage.grid(row=0, column=2, sticky='EW')

        reduction = ttk.Label(
            self.frame,
            text='Reduction'
        )
        reduction.grid(row=0, column=3, sticky='EW')

        name_separator = ttk.Separator(
            self.frame
        )
        name_separator.grid(row=1, column=0, columnspan=4, sticky='EW')

        health_label = ttk.Label(
            self.frame,
            text='Health'
        )
        health_label.grid(row=2, column=0, sticky='EW')

        self.health_entry = ttk.Label(
            self.frame,
            text=self.generate_total_health()
        )
        self.health_entry.grid(row=2, column=1, sticky='EW')

        self.damage_entry = ttk.Entry(
            self.frame,
            textvariable=self.damage
        )
        self.damage_entry.grid(row=2, column=2, sticky='EW')

        self.reduction_entry = ttk.Entry(
            self.frame,
            textvariable=self.reduction
        )
        self.reduction_entry.grid(row=2, column=3, sticky='EW')

        damage_button = ttk.Button(
            self.frame,
            text='Calculate',
            command=self.attack,
            cursor='hand2'
        )
        damage_button.grid(row=3, column=1, columnspan=3, sticky='EW')

        adrenaline_label = ttk.Label(
            self.frame,
            text='Adrenaline'
        )
        adrenaline_label.grid(row=4, column=0, sticky='EW')

        self.adrenaline_entry = ttk.Label(
            self.frame,
            text=self.entity.adrenaline
        )
        self.adrenaline_entry.grid(row=4, column=1, sticky='EW')

        self.adrenaline_reduction = ttk.Entry(
            self.frame,
            textvariable=self.adrenaline
        )
        self.adrenaline_reduction.grid(row=4, column=2, sticky='EW')

        adrenaline_button = ttk.Button(
            self.frame,
            text='Reduce',
            command=self.reduce_adrenaline,
            cursor='hand2'
        )
        adrenaline_button.grid(row=4, column=3, sticky='EW')

        reset_button = ttk.Button(
            self.frame,
            text='Reset',
            command=self.reset,
            cursor='hand2'
        )
        reset_button.grid(row=5, column=0, columnspan=4, sticky='EW')

    def reset(self):
        self.health_entry['text'] = self.generate_total_health()
        self.damage_entry.delete(0, 'end')

    def attack(self):
        damage = int(self.damage.get())
        reduction = int(self.reduction.get())

        if damage < 0:
            print(damage)
            damage *= -1
            self.current_hp += damage

            if self.current_hp > self.entity.health:
                self.current_hp = self.entity.health
        else:
            calculate = damage - reduction
            self.current_hp -= calculate if calculate > 0 else 0

        self.health_entry['text'] = str(self.current_hp)

    def reduce_adrenaline(self):
        adrenaline = self.adrenaline_reduction.get()
        self.current_adr -= int(adrenaline)
        self.adrenaline_entry['text'] = str(self.current_adr)

    def generate_total_health(self) -> str:
        total_health = 0

        for item in self.entity.items:
            total_health += int(item.health)

        if '(' in self.entity.health and ')' in self.entity.health:
            start = self.entity.health.find("(") + 1
            end = self.entity.health.find(")")
            sub_health = self.entity.health[start:end]

            print(sub_health)

            total_health += int(sub_health)
        else:
            total_health += int(self.entity.health)

        return str(total_health)
