import mysql.connector
from app.utils.config import Config

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host= Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor
    
    def commit(self):
        self.connection.commit()
    def close(self):
        self.connection.close()

db = Database()