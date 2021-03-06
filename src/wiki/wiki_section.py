from tkinter import ttk, font

from src.wiki.chapter import Chapter
from src.wiki.wiki_template import WikiTemplate


class WikiSection(WikiTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.section = kwargs['entity']
        self.chapters = self.wiki.get_chapters(self.section.id)

        self.config('create_chapter', False, self.section, 'section')

        self.set_section()
        self.set_buttons('Add Chapter', lambda: self.show_wiki(**self.config_show_wiki))

    def set_section(self) -> None:
        name = ttk.Label(
            self.widgets,
            text=self.section.name,
            font=font.Font(size=13)
        )
        name.grid(row=0, column=0, sticky='EW')

        description = ttk.Label(
            self.widgets,
            text=self.section.description,
            font=font.Font(size=11)
        )
        description.grid(row=1, column=0, sticky='EW')

        def reconfigure_labels(event) -> None:
            description.configure(wraplength=self.widgets.winfo_width() - 25)

        self.widgets.bind("<Configure>", reconfigure_labels)

        title_separator = ttk.Separator(
            self.widgets
        )
        title_separator.grid(row=2, column=0, columnspan=1, sticky='EW')

        if len(self.chapters) > 0:
            self.set_chapters()

    def set_chapters(self) -> None:
        for chapter in self.chapters:
            button = ttk.Button(
                self.widgets,
                text=chapter.name,
                command=lambda current_chapter=chapter: self.select_chapter(current_chapter),
                style='DarkButton.TButton',
                cursor='hand2'
            )
            button.grid(column=0, sticky='EW')

    def select_chapter(self, chapter: Chapter):
        self.show_wiki(factory='chapter', entity=chapter, back='section', preview_entity=self.section)
