import pymysql.cursors


connection_dict = {
    "host": 'localhost',
    "user": 'root',
    "password": 'my-secret-pw',
    "database": 'ADMIN',
    "cursorclass": pymysql.cursors.DictCursor
}

def fetch_one(query):
    connection = pymysql.connect(**connection_dict)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result

def execute(query):
    connection = pymysql.connect(**connection_dict)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
