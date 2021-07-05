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

        self.category_mapping = {}
        self.section_mapping = {}
        self.chapter_mapping = {}
        self.topic_mapping = {}

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
        self.category_mapping = {category.name: category.id for category in self.categories}
        return self.categories

    def get_sections(self, category_id: int = 0) -> list:
        self.sections = [Section(**section) for section in get_sections(category_id)]
        self.section_mapping = {section.name: section.id for section in self.sections}
        return self.sections

    def get_chapters(self, section_id: int = 0) -> list:
        self.chapters = [Chapter(**chapter) for chapter in get_chapters(section_id)]
        self.chapter_mapping = {chapter.name: chapter.id for chapter in self.chapters}
        return self.chapters

    def get_topics(self, chapter_id: int = 0) -> list:
        self.topics = [Topic(**topic) for topic in get_topics(chapter_id)]
        self.topic_mapping = {topic.name: topic.id for topic in self.topics}
        return self.topics

    def update(self) -> None:
        self.categories = get_categories()
        self.sections = get_sections()
        self.chapters = get_chapters()
        self.topics = get_topics()
