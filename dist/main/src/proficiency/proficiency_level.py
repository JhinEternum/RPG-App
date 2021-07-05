import tkinter as tk
from tkinter import ttk

# from src.edit.edit_user import EditUser


class ProficiencyLevel(tk.Toplevel):
    def __init__(self, **kwargs):
        parent = kwargs['parent']
        super().__init__(parent)

        parent.eval(f'tk::PlaceWindow {str(self)} center')

        self.resizable(False, False)
        self.columnconfigure(1, weight=1)
        self.title('Proficiencies')
        self.focus()

        print(kwargs)

        self.proficiencies = kwargs['proficiencies']
        self.proficiency_result = kwargs['proficiency_result']
        self.create_avatar = kwargs['create_avatar'] if 'create_avatar' in kwargs else None
        self.edit = kwargs['edit'] if 'edit' in kwargs else None
        self.user_proficiencies = kwargs['user_proficiencies'] if 'user_proficiencies' in kwargs else None

        self.levels = (1, 2, 3, 4, 5)
        self.ranks = ('None', 'S', 'A', 'B')
        self.proficiencies_list = []
        self.proficiencies_rank = []

        proficiency_frame = ttk.Frame(self)
        proficiency_frame.grid(row=0, column=0, sticky="NSEW")
        proficiency_frame.columnconfigure(0, weight=1)

        proficiency = ttk.Label(
            proficiency_frame,
            text='Proficiencies'
        )
        proficiency.grid(row=0, column=0)

        proficiency_lv = ttk.Label(
            proficiency_frame,
            text='Level'
        )
        proficiency_lv.grid(row=0, column=1)

        proficiency_rank = ttk.Label(
            proficiency_frame,
            text='Rank'
        )
        proficiency_rank.grid(row=0, column=2)

        title_separator = ttk.Separator(proficiency_frame)
        title_separator.grid(row=1, column=0, pady=(15, 0), columnspan=3, sticky='EW')

        index = 2
        for proficiency in self.proficiencies:
            proficiency_variable = tk.StringVar(value=self.levels[self.set_level(proficiency) - 1])
            rank_variable = tk.StringVar(value=self.ranks[self.set_rank(proficiency)])

            proficiency_label = ttk.Label(
                proficiency_frame,
                text=proficiency
            )
            proficiency_label.grid(row=index, column=0)

            proficiency_entry = ttk.Combobox(
                proficiency_frame,
                textvariable=proficiency_variable,
                values=self.levels,
                state="readonly"
            )
            proficiency_entry.grid(row=index, column=1)

            proficiency_rank = ttk.Combobox(
                proficiency_frame,
                textvariable=rank_variable,
                values=self.ranks,
                state='readonly'
            )
            proficiency_rank.grid(row=index, column=2)

            self.proficiencies_list.append(proficiency_variable)
            self.proficiencies_rank.append(rank_variable)
            index += 1

        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, sticky="EW")
        button_frame.columnconfigure(0, weight=1)

        title_separator = ttk.Separator(button_frame)
        title_separator.grid(row=0, column=0, pady=(15, 0), columnspan=1, sticky='EW')

        create_button = ttk.Button(
            button_frame,
            text='Create Avatar' if self.edit is None else 'Finalize',
            command=self.get_proficiencies,
            cursor='hand2'
        )
        create_button.grid(row=1, column=0, padx=15, pady=15, sticky='EW')

        for child in proficiency_frame.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')

    def set_level(self, proficiency_name: str) -> int:
        if self.user_proficiencies is None:
            return 1

        for proficiency in self.user_proficiencies:
            if proficiency['name'] == proficiency_name:
                return int(proficiency['level'])

        return 1

    def set_rank(self, proficiency_name: str) -> int:
        if self.user_proficiencies is None:
            return 0

        for proficiency in self.user_proficiencies:
            if proficiency['name'] == proficiency_name:
                return int(proficiency['rank'])

        return 0

    def get_proficiencies(self) -> None:
        proficiencies_result = []

        for index in range(len(self.proficiency_result)):
            print(f'asdoasdjkkqwjfk{self.ranks.index(self.proficiencies_rank[index].get())}')
            proficiencies_result.append(
                (
                    self.proficiency_result[index],
                    self.proficiencies_list[index].get(),
                    self.ranks.index(self.proficiencies_rank[index].get())
                )
            )

        if self.edit is None:
            self.create_avatar(tuple(proficiencies_result))
        else:
            self.edit(tuple(proficiencies_result))

        self.destroy()
        self.update()
