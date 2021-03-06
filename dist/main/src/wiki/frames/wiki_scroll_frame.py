import tkinter as tk
from tkinter import ttk

from src.images.image import get_home


class WikiScrollFrame(ttk.Frame):
    def __init__(self, **kwargs):
        self.parent = kwargs['parent']
        super().__init__(self.parent)

        self.kwargs = kwargs
        self.parent = kwargs['parent']
        self.back = kwargs['back'] if 'back' in kwargs else 'home'

        self.home = kwargs['home']

        self.home_icon = get_home()

        self.configure(style='DarkTheme.TFrame')

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.template_scroll = WikiTemplateScroll(self, **kwargs)
        self.template_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def set_widgets_conf(self) -> None:
        for child in self.template_scroll.widgets.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def append_to_frames(self, Entity) -> None:
        self.template_scroll.frames.append(Entity)

    def set_buttons_conf(self) -> None:
        title_separator = ttk.Separator(
            self.template_scroll.buttons
        )
        title_separator.grid(column=0, columnspan=1, sticky='EW')

        home_button = ttk.Button(
            self.template_scroll.buttons,
            text='Home',
            command=self.home,
            style='DarkButton.TButton',
            image=self.home_icon,
            compound=tk.LEFT,
            cursor='hand2'
        )
        home_button.grid()

        for child in self.template_scroll.buttons.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky='EW')


class WikiTemplateScroll(tk.Canvas):
    def __init__(self, container, **kwargs):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container
        self.kwargs = kwargs
        scroll = kwargs['scroll'] if 'scroll' in kwargs else False
        single_widgets = kwargs['single_widgets'] if 'single_widgets' in kwargs else False

        self['background'] = '#303030'

        self.screen = tk.Frame(container, background='#303030')
        self.screen.columnconfigure(0, weight=1)

        self.frames = []
        self.widgets = None
        self.buttons = None

        self.scrollable_window = self.create_window((0, 0), window=self.screen, anchor="nw")

        def configure_scroll_region(event) -> None:
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event) -> None:
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.screen.bind("<Configure>", configure_scroll_region)

        if scroll:
            self.bind_all("<MouseWheel>", self._on_mouse_wheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

        self.widgets = ttk.Frame(self.screen, style='DarkTheme.TFrame')
        self.widgets.grid(row=0, column=0, sticky='NSEW')

        if single_widgets:
            self.widgets.columnconfigure(0, weight=1)
        else:
            self.widgets.columnconfigure((0, 1), weight=1)

        self.buttons = ttk.Frame(self.screen, style='DarkTheme.TFrame')
        self.buttons.grid(row=1, column=0, sticky='EW')
        self.buttons.columnconfigure(0, weight=1)

    def _on_mouse_wheel(self, event) -> None:
        self.yview_scroll(-int(event.delta/120), "units")

    def add_entity_frame(self, Entity) -> None:
        current_rows = self.screen.grid_size()[1]
        frame_number = str(len(self.frames) + 1)

        self.widgets = ttk.Frame(self.screen, style='DarkTheme.TFrame')
        new_entity_frame = Entity(
            widgets=self.widgets,
            frame_id=frame_number
        )
        self.widgets.grid(row=current_rows - 1, column=0, sticky='NSEW')
        self.widgets.columnconfigure(0, weight=1)

        self.frames.append(new_entity_frame)

        self.container.set_widgets_conf()

        self.buttons.grid_configure(row=current_rows)

        print(self.frames)

    def bind_label(self, labels):
        def reconfigure_labels(event):
            for label in labels:
                label.configure(wraplength=self.widgets.winfo_width() - 25)

        self.widgets.bind("<Configure>", reconfigure_labels)
