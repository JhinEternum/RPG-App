from .database import *
from .database import DatabaseConnection


# --- CLASSES ---
def get_classes():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM classes')

        entity = get_classes_attributes(cursor)

    return entity


def get_class_id(class_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT id FROM classes WHERE name=?', (class_name,))

        entity = get_classes_attributes(cursor)

    return entity


def get_classes_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
    } for row in cursor.fetchall()]
