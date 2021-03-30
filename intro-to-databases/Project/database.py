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


class ConnectionPool:
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(1,
                                                         1,
                                                         database="learning",
                                                         user="mustafaalogaidi",
                                                         password="Pit5cxcy",
                                                         host="localhost")

    def __enter__(self):
        return self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
