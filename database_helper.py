import pymysql

class db_connect:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Ezhil',
            db='ezhil_bus_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchall()