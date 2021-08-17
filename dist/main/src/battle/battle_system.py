from tkinter import Toplevel
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

from src.avatar.avatar import Avatar
from src.methods import get_text_data


class BattleSystem(Toplevel):
    def __init__(self, **kwargs):
        master = kwargs['master']
        super().__init__(kwargs['master'])

        master.eval(f'tk::PlaceWindow {str(self)} center')

        # self.resizable(False, False)
        self.columnconfigure(1, weight=1)
        self.title('Battle System')
        self.focus()

        menu_bar = Menu(self)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="New", command=self.attack)
        menu_bar.add_cascade(label="File", menu=menu)
        self.config(menu=menu_bar)

        self.entity: Avatar = kwargs['entity']

        self.hp = self.entity.health
        self.adrenaline = self.entity.adrenaline

        self.current_hp = int(self.generate_total_health())
        self.current_adr = int(self.adrenaline)
        self.health_entry = ttk.Label()
        self.adrenaline_reduction = ttk.Entry()
        self.damage_entry = ttk.Entry()
        self.reduction_entry = ttk.Entry()
        self.adrenaline_entry = ttk.Label()
        self.log_text = tk.Text()

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0, sticky='NSEW')
        self.frame.columnconfigure(0, weight=1)

        self.log_frame = ttk.Frame(self)
        self.log_frame.grid(row=0, column=4, sticky='NSEW')
        self.log_frame.columnconfigure(0, weight=1)

        self.set_avatar()
        self.set_log()

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')

        for child in self.log_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # self.bind('<Return>', self.attack)

    def set_avatar(self):
        name = ttk.Label(
            self.frame,
            text=self.entity.name
        )
        name.grid(row=0, column=0)

        damage = ttk.Label(
            self.frame,
            text='Damage'
        )
        damage.grid(row=0, column=2)

        reduction = ttk.Label(
            self.frame,
            text='Reduction'
        )
        reduction.grid(row=0, column=3)

        name_separator = ttk.Separator(
            self.frame
        )
        name_separator.grid(row=1, column=0, columnspan=4)

        health_label = ttk.Label(
            self.frame,
            text='Health'
        )
        health_label.grid(row=2, column=0)

        self.health_entry = ttk.Label(
            self.frame,
            text=self.generate_total_health()
        )
        self.health_entry.grid(row=2, column=1)

        self.damage_entry = ttk.Entry(self.frame)
        self.damage_entry.grid(row=2, column=2)
        self.damage_entry.bind('<Return>', self.attack)

        self.reduction_entry = ttk.Entry(self.frame)
        self.reduction_entry.grid(row=2, column=3)
        self.reduction_entry.insert(0, '0')

        damage_button = ttk.Button(
            self.frame,
            text='⚔ Attack',
            command=self.attack,
            cursor='hand2'
        )
        damage_button.grid(row=3, column=0, columnspan=4)

        adrenaline_label = ttk.Label(
            self.frame,
            text='Adrenaline'
        )
        adrenaline_label.grid(row=4, column=0)

        self.adrenaline_entry = ttk.Label(
            self.frame,
            text=self.adrenaline
        )
        self.adrenaline_entry.grid(row=4, column=1)

        self.adrenaline_reduction = ttk.Entry(self.frame)
        self.adrenaline_reduction.grid(row=4, column=2)
        self.adrenaline_reduction.bind('<Return>', self.reduce_adrenaline)

        adrenaline_button = ttk.Button(
            self.frame,
            text='⏳ Reduce',
            command=self.reduce_adrenaline,
            cursor='hand2'
        )
        adrenaline_button.grid(row=4, column=3)

        reset_button = ttk.Button(
            self.frame,
            text='Reset',
            command=self.reset,
            cursor='hand2'
        )
        reset_button.grid(row=5, column=0, columnspan=4)

    def set_log(self):
        log = ttk.Label(
            self.log_frame,
            text='Log'
        )
        log.grid(row=0, column=0, sticky='EW')

        name_separator = ttk.Separator(
            self.log_frame
        )
        name_separator.grid(row=1, column=0, columnspan=1, sticky='EW')

        self.log_text = tk.Text(
            self.log_frame,
            width=30,
            height=10,
            state=tk.DISABLED
        )
        self.log_text.grid(row=2, column=0, sticky='NSEW')

        log_scroll = ttk.Scrollbar(
            self.log_frame,
            orient='vertical',
            command=self.log_text.yview
        )
        log_scroll.grid(row=2, column=1, sticky='ns')

        self.log_text['yscrollcommand'] = log_scroll.set

    def config_log(self, action: str, numbers: int):
        current_log = get_text_data(self.log_text)
        action_text = ''
        self.log_text['state'] = tk.NORMAL

        if action == 'd':
            action_text = f'Damaged: {numbers}'
            if numbers < 0:
                action_text = f'Healed: {numbers * -1}'
        elif action == 'a':
            action_text = f'Damaged Adr: {numbers}'
            if numbers < 0:
                action_text = f'Healed Adr: {numbers * -1}'

        new_log = f'{action_text}\n'
        self.log_text.insert(tk.END, new_log)
        self.log_text['state'] = tk.DISABLED

    def reset(self):
        self.health_entry['text'] = self.generate_total_health()
        self.damage_entry.delete(0, 'end')

    def attack(self, event=None):
        damage = int(self.damage_entry.get())
        reduction = int(self.reduction_entry.get()) if self.reduction_entry.get() != '' else 0

        if damage < 0:
            print(damage)
            self.current_hp += damage * -1

            if self.current_hp > self.hp:
                self.current_hp = self.hp
        else:
            calculate = damage - reduction
            self.current_hp -= calculate if calculate > 0 else 0

        self.health_entry['text'] = str(self.current_hp)
        self.damage_entry.delete(0, tk.END)

        self.config_log('d', damage)

    def reduce_adrenaline(self, event=None):
        a_damage = int(self.adrenaline_reduction.get())

        if a_damage < 0:
            self.current_adr += a_damage * -1
            if self.current_adr > int(self.adrenaline):
                self.current_adr = int(self.adrenaline)
        else:
            self.current_adr -= a_damage

        self.adrenaline_entry['text'] = str(self.current_adr)
        self.adrenaline_reduction.delete(0, tk.END)

        self.config_log('a', a_damage)

    def generate_total_health(self) -> str:
        total_health = 0

        for item in self.entity.items:
            if 'mana' in item.health.lower():
                start = item.health.find(" ")
                health = item.health[:start]

                self.adrenaline = str(int(self.entity.adrenaline) + int(health))
            else:
                total_health += int(item.health)

        if '(' in self.entity.health and ')' in self.entity.health:
            start = self.entity.health.find("(")
            end = self.entity.health.find(")")

            health = self.entity.health[:start]
            sub_health = self.entity.health[start + 1:end]

            total_health += int(health) + int(sub_health)
        else:
            total_health += int(self.entity.health)

        self.hp = total_health

        return str(total_health)
