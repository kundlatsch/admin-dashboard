import pymysql.cursors



def fetch_one(query):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='my-secret-pw',
                                database='ADMIN',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        # Example insert
        # with connection.cursor() as cursor:
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        # connection.commit()

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result