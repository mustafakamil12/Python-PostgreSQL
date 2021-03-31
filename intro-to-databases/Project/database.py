# import psycopg2
from psycopg2 import pool

"""
def connect():
    return psycopg2.connect(database="learning", user="mustafaalogaidi", password="Pit5cxcy", host="localhost")

"""


class Database:
    __connection_pool = None

    """
    @classmethod
    def initialise(cls):
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          10,
                                                          database="learning",
                                                          user="mustafaalogaidi",
                                                          password="Pit5cxcy",
                                                          host="localhost")
    """
    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          10,
                                                          **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls):
        cls.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):    # where with begin
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):  # return connection when with end
        if exception_value is not None:     # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
