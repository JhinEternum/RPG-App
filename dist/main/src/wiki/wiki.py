# A Category may have multiple Sections.
# A Section may have multiple Chapters.
# A Chapter may have multiple Topics.
# Category : Section.
# Section : Chapter.
# Chapter : Topic.
from src.connection.handle_wiki import *


class Wiki:
    def __init__(self):
        self.categories = list()
        self.sections = list()
        self.chapters = list()
        self.topics = list()

        self.last_section = dict()
        self.last_chapter = dict()
        self.last_topic = dict()

    def create_category(self, name, description) -> bool:
        return create_category(name, description)

    def create_section(self, name, description, category_id) -> bool:
        return create_section(name, description, category_id)

    def create_chapter(self, name, description, section_id) -> bool:
        return create_chapter(name, description, section_id)

    def create_topic(self, name, description, chapter_id) -> bool:
        return create_topic(name, description, chapter_id)

    def get_categories(self) -> list:
        self.categories = get_categories()
        return self.categories

    def get_sections(self, category_id=0) -> list:
        if category_id > 0:
            self.sections = get_sections_by_category_id(category_id)
        else:
            self.sections = get_sections()

        return self.sections

    def get_chapters(self, section_id=0) -> list:
        if section_id > 0:
            self.chapters = get_chapters_by_section_id(section_id)
        else:
            self.chapters = get_chapters()

        return self.chapters

    def get_topics(self, chapter_id=0) -> list:
        if chapter_id > 0:
            self.topics = get_topics_by_chapter_id(chapter_id)
        else:
            self.topics = get_topics()

        return self.topics

    def update(self):
        self.categories = get_categories()
        self.sections = get_sections()
        self.chapters = get_chapters()
        self.topics = get_topics()
