# A Category may have multiple Sections.
# A Section may have multiple Chapters.
# A Chapter may have multiple Topics.
# Category : Section.
# Section : Chapter.
# Chapter : Topic.
from src.connection.handle_wiki import *
from src.wiki.category import Category
from src.wiki.chapter import Chapter
from src.wiki.section import Section
from src.wiki.topic import Topic


class Wiki:
    def __init__(self):
        self.categories = list()
        self.sections = list()
        self.chapters = list()
        self.topics = list()

        self.last_section = dict()
        self.last_chapter = dict()
        self.last_topic = dict()

    def create_category(self, name: str, description: str) -> bool:
        return create_category(name, description)

    def create_section(self, name: str, description: str, category_id: int) -> bool:
        return create_section(name, description, category_id)

    def create_chapter(self, name: str, description: str, section_id: int) -> bool:
        return create_chapter(name, description, section_id)

    def create_topic(self, name: str, description: str, chapter_id: int) -> bool:
        return create_topic(name, description, chapter_id)

    def get_categories(self) -> list:
        self.categories = [Category(**category) for category in get_categories()]
        return self.categories

    def get_sections(self, category_id: int = 0) -> list:
        self.sections = [Section(**section) for section in get_sections(category_id)]
        return self.sections

    def get_chapters(self, section_id: int = 0) -> list:
        self.chapters = [Chapter(**chapter) for chapter in get_chapters(section_id)]
        return self.chapters

    def get_topics(self, chapter_id: int = 0) -> list:
        self.topics = [Topic(**topic) for topic in get_topics(chapter_id)]
        return self.topics

    def update(self) -> None:
        self.categories = get_categories()
        self.sections = get_sections()
        self.chapters = get_chapters()
        self.topics = get_topics()
