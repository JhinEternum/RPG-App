import tkinter as tk
from tkinter import ttk


class TemplateScrollFrame(ttk.Frame):
    def __init__(self, **kwargs):
        self.parent = kwargs['parent']
        super().__init__(self.parent)

        self.kwargs = kwargs
        self.parent = kwargs['parent']

        self.home = kwargs['home']

        # --- Create Widget Frame ---
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.template_scroll = TemplateScroll(self, **kwargs)
        self.template_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def set_widgets_conf(self) -> None:
        for child in self.template_scroll.widgets.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def append_to_frames(self, Entity) -> None:
        self.template_scroll.frames.append(Entity)

    def set_buttons_conf(self) -> None:
        home_button = ttk.Button(
            self.template_scroll.buttons,
            text='Home',
            command=self.home,
            cursor='hand2'
        )
        home_button.grid()

        for child in self.template_scroll.buttons.winfo_children():
            child.grid_configure(padx=15, pady=5, sticky='EW')


class TemplateScroll(tk.Canvas):
    def __init__(self, container, **kwargs):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container
        self.kwargs = kwargs
        isScroll = kwargs['isScroll'] if 'isScroll' in kwargs else False

        self.screen = tk.Frame(container)
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

        if isScroll:
            self.bind_all("<MouseWheel>", self._on_mouse_wheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

        self.widgets = ttk.Frame(self.screen)
        self.widgets.grid(row=0, column=0, sticky='NSEW')
        self.widgets.columnconfigure((0, 1), weight=1)

        self.buttons = ttk.Frame(self.screen)
        self.buttons.grid(row=1, column=0, sticky='EW')
        self.buttons.columnconfigure(0, weight=1)

    def _on_mouse_wheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

    def add_entity_frame(self, Entity):
        current_rows = self.screen.grid_size()[1]
        frame_number = str(len(self.frames) + 1)

        self.widgets = ttk.Frame(self.screen)
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
