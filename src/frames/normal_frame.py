from tkinter import ttk


class TemplateFrame(ttk.Frame):
    def __init__(self, **kwargs):
        self.parent = kwargs['parent']
        super().__init__(self.parent)

        self.kwargs = kwargs
        self.parent = kwargs['parent']

        # --- Create Widget Frame ---
        self.columnconfigure(0, weight=1)

        self.widgets = ttk.Frame(self)
        self.widgets.grid(row=0, column=0, sticky='NSEW')
        self.widgets.columnconfigure(1, weight=1)

        self.buttons = ttk.Frame(self)
        self.buttons.grid(row=1, column=0, pady=10, sticky='NSEW')
        self.buttons.columnconfigure(0, weight=1)

        self.widgets.grid_configure(padx=10, pady=5, sticky='EW')
        self.buttons.grid_configure(padx=10, pady=5, sticky='EW')

    def set_widgets_conf(self) -> None:
        for child in self.widgets.winfo_children():
            child.grid_configure(padx=15, pady=5, sticky='EW')

    def set_buttons_conf(self) -> None:
        for child in self.buttons.winfo_children():
            child.grid_configure(padx=15, pady=5, sticky='EW')
