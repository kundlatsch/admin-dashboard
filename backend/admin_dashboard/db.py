import pymysql.cursors


connection_dict = {
    "host": 'database',
    "user": 'root',
    "password": 'my-secret-pw',
    "database": 'ADMIN',
    "cursorclass": pymysql.cursors.DictCursor
}

def fetch_one(query):
    connection = pymysql.connect(**connection_dict)
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                return result
    except Exception as Er:
        print(Er)

def fetch_all(query):
    connection = pymysql.connect(**connection_dict)
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
    except Exception as Er:
        print(Er)

def execute(query):
    connection = pymysql.connect(**connection_dict)
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
    except Exception as Er:
        print(Er)