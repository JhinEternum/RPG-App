def get_items_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'reduction': row[3],
        'damage': row[4],
        'range': row[5],
        'health': row[6],
        'area': row[7],
        'effects': row[8],
        'description': row[9]
    } for row in cursor.fetchall()]


def get_item_attributes(cursor):
    return [{
        'id': row[0],
        'name': row[1],
        'type': row[2],
        'reduction': row[3],
        'damage': row[4],
        'range': row[5],
        'health': row[6],
        'area': row[7],
        'effects': row[8],
        'description': row[9]
    } for row in cursor.fetchall()][0]
