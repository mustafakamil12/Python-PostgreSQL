#import psycopg2
from psycopg2 import pool

"""
def connect():
    return psycopg2.connect(database="learning", user="mustafaalogaidi", password="Pit5cxcy", host="localhost")

"""
"""
connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            database="learning",
                                            user="mustafaalogaidi",
                                            password="Pit5cxcy",
                                            host="localhost")
"""
connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            database="learning",
                                            user="mustafaalogaidi",
                                            password="Pit5cxcy",
                                            host="localhost")


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):    # where with begin
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):  # return connection when with end
        self.cursor.close()
        self.connection.commit()
        connection_pool.putconn(self.connection)
