from .database import *
from .database import DatabaseConnection


def create_category(name, description) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki (name, description) VALUES (?, ?)', (name, description))

    return True


def create_section(name, description, category_id) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki_sections (name, description, category_id) VALUES (?, ?, ?)',
                       (name, description, category_id))

    return True


def create_chapter(name, description, section_id) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki_chapters (name, description, section_id) VALUES (?, ?, ?)',
                       (name, description, section_id))

    return True


def create_topic(name, description, chapter_id) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki_topics (name, description, chapter_id) VALUES (?, ?, ?)',
                       (name, description, chapter_id))

    return True


def get_categories():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki ORDER BY name')

        categories = get_categories_attributes(cursor)

    return categories


def get_sections():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_sections')

        sections = get_sections_attributes(cursor)

    return sections


def get_chapters():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_chapters')

        sections = get_chapters_attributes(cursor)

    return sections


def get_topics():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_topics')

        sections = get_topics_attributes(cursor)

    return sections


def get_sections_by_category_id(category_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_sections WHERE category_id=?', (category_id,))

        sections = get_sections_attributes(cursor)

    return sections


def get_chapters_by_section_id(section_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_chapters WHERE section_id=?', (section_id,))

        chapters = get_chapters_attributes(cursor)

    return chapters


def get_topics_by_chapter_id(chapter_id):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM wiki_topics WHERE chapter_id=?', (chapter_id,))

        topics = get_topics_attributes(cursor)

    return topics


def get_categories_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2]
    } for row in cursor.fetchall()]


def get_sections_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'category_id': row[3]
    } for row in cursor.fetchall()]


def get_chapters_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'section_id': row[3]
    } for row in cursor.fetchall()]


def get_topics_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'chapter_id': row[3]
    } for row in cursor.fetchall()]
