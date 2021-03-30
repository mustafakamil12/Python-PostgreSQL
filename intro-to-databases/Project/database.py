#import psycopg2
from psycopg2 import pool

"""
def connect():
    return psycopg2.connect(database="learning", user="mustafaalogaidi", password="Pit5cxcy", host="localhost")

"""

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            database="learning",
                                            user="mustafaalogaidi",
                                            password="Pit5cxcy",
                                            host="localhost")
