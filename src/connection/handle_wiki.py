from .database import DatabaseConnection


def create_category(name: str, description: str) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki (name, description) VALUES (?, ?)', (name, description))

    return True


def create_section(name: str, description: str, category_id: int) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki_sections (name, description, category_id) VALUES (?, ?, ?)',
                       (name, description, category_id))

    return True


def create_chapter(name: str, description: str, section_id: int) -> bool:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO wiki_chapters (name, description, section_id) VALUES (?, ?, ?)',
                       (name, description, section_id))

    return True


def create_topic(name: str, description: str, chapter_id: int) -> bool:
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


def get_sections(category_id: int = 0):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if category_id == 0:
            cursor.execute('SELECT * FROM wiki_sections')
        else:
            cursor.execute('SELECT * FROM wiki_sections WHERE category_id=?', (category_id,))

        sections = get_sections_attributes(cursor)

    return sections


def get_chapters(section_id: int = 0):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if section_id == 0:
            cursor.execute('SELECT * FROM wiki_chapters')
        else:
            cursor.execute('SELECT * FROM wiki_chapters WHERE section_id=?', (section_id,))

        sections = get_chapters_attributes(cursor)

    return sections


def get_topics(chapter_id: int = 0):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        if chapter_id == 0:
            cursor.execute('SELECT * FROM wiki_topics')
        else:
            cursor.execute('SELECT * FROM wiki_topics WHERE chapter_id=?', (chapter_id,))

        sections = get_topics_attributes(cursor)

    return sections


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
