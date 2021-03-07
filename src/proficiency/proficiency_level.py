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
        self.avatar_frame = kwargs['create_avatar']
        self.edit_user = kwargs['edit_user'] if 'edit_user' in kwargs else None
        self.user_proficiencies = kwargs['user_proficiencies'] if 'user_proficiencies' in kwargs else None

        self.levels = (1, 2, 3, 4, 5)
        self.proficiencies_list = []

        proficiency_frame = ttk.Frame(self)
        proficiency_frame.grid(row=0, column=0, sticky="NSEW")
        proficiency_frame.columnconfigure(0, weight=1)

        index = 0
        for proficiency in self.proficiencies:
            proficiency_variable = tk.StringVar(value=self.levels[self.set_level(proficiency) - 1])

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

            self.proficiencies_list.append(proficiency_variable)
            index += 1

        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, sticky="EW")
        button_frame.columnconfigure(0, weight=1)

        title_separator = ttk.Separator(button_frame)
        title_separator.grid(row=0, column=0, pady=(15, 0), columnspan=1, sticky='EW')

        create_button = ttk.Button(
            button_frame,
            text='Create Avatar',
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

    def get_proficiencies(self) -> None:
        proficiencies_result = []

        for index in range(len(self.proficiency_result)):
            proficiencies_result.append((self.proficiency_result[index], self.proficiencies_list[index].get()))

        if self.edit_user is None:
            self.avatar_frame.create_avatar(tuple(proficiencies_result))
        else:
            self.edit_user.edit_entity(tuple(proficiencies_result))

        self.destroy()
        self.update()
